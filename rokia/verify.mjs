// Automated gate for every rokia/*.html lesson page.
//
// Opens each page, exercises every part/lab/question exactly as a student
// would, and asserts the four standing invariants:
//   1. Zero Arabic in the exact strings handed to speech synthesis
//      (calls the page's own englishOf(), not a re-implementation).
//   2. Zero answer/score leakage before the quiz is submitted.
//   3. Zero unintended horizontal overflow.
//   4. Zero browser console/page errors.
//
// Usage:  node rokia/verify.mjs           (all pages)
//         node rokia/verify.mjs 17        (only files matching "17")
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Prefer a locally installed playwright; fall back to this environment's
// global install (the Claude Code sandbox ships one at this fixed path).
let chromium;
try {
  ({ chromium } = await import('playwright'));
} catch {
  ({ chromium } = await import('/opt/node22/lib/node_modules/playwright/index.mjs'));
}

const DIR = path.dirname(fileURLToPath(import.meta.url));
const filter = process.argv[2];
const files = fs.readdirSync(DIR)
  .filter(f => f.endsWith('.html'))
  .filter(f => !filter || f.includes(filter))
  .sort();

if (!files.length) {
  console.error('No matching pages in', DIR);
  process.exit(1);
}

const b = await chromium.launch();
const out = [];
let failCount = 0;

for (const f of files) {
  const p = await b.newPage({ viewport: { width: 430, height: 900 }, deviceScaleFactor: 2 });
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto('file://' + DIR + '/' + f);
  await p.waitForTimeout(300);
  const r = { file: f, errs };

  // Learn — open EVERY part and check the text the voice would actually speak
  r.parts = await p.locator('.part').count();
  r.arabicLeak = 0;
  r.leakWhere = [];
  for (let i = 0; i < r.parts; i++) {
    await p.locator('.part-h').nth(i).click();
    await p.waitForTimeout(80);
    const bad = await p.evaluate(i => {
      const b = document.querySelectorAll('.part')[i].querySelector('.part-b');
      const blocks = Array.from(b.querySelectorAll('p,li,h4,td,.def,.qtext'))
        .filter(e => !e.closest('.ar,.gloss')).filter(e => !e.querySelector('p,li,td'));
      return blocks.map(e => englishOf(e)).filter(t => /[؀-ۿ]/.test(t));
    }, i);
    if (bad.length) { r.arabicLeak += bad.length; r.leakWhere.push('part' + (i + 1) + ':' + bad[0].slice(0, 30)); }
    await p.locator('.part-h').nth(i).click();
    await p.waitForTimeout(40);
  }

  // Cards
  await p.locator('.tab[data-go="cards"]').click();
  await p.waitForTimeout(150);
  await p.locator('#flip').click();
  await p.waitForTimeout(300);
  r.cardBackFilled = (await p.locator('#cBack').textContent()).length > 0;

  // Play — solve every lab fully and correctly (GAME is one lab, or an array of labs)
  await p.locator('.tab[data-go="play"]').click();
  await p.waitForTimeout(200);
  const labCount = await p.evaluate(() => Array.isArray(GAME) ? GAME.length : 1);
  const modes = [];
  for (let li = 0; li < labCount; li++) {
    const areaSel = li === 0 ? '#playArea' : '#playArea' + li;
    const mode = await p.evaluate((li) => { const g = Array.isArray(GAME) ? GAME[li] : GAME; return g.mode; }, li);
    modes.push(mode);
    if (mode === 'sort') {
      const items = await p.evaluate((li) => { const g = Array.isArray(GAME) ? GAME[li] : GAME; return g.items.map(i => i.k); }, li);
      for (let i = 0; i < items.length; i++) {
        await p.locator(`${areaSel} .gline`).nth(i).locator(`.pick[data-k="${items[i]}"]`).click();
        await p.waitForTimeout(30);
      }
    } else if (mode === 'match') {
      const n = await p.evaluate((li) => { const g = Array.isArray(GAME) ? GAME[li] : GAME; return g.pairs.length; }, li);
      for (let i = 0; i < n; i++) {
        await p.locator(`${areaSel} .mbtn[data-side="a"][data-i="${i}"]`).click();
        await p.locator(`${areaSel} .mbtn[data-side="b"][data-i="${i}"]`).click();
        await p.waitForTimeout(30);
      }
    } else {
      const n = await p.evaluate((li) => { const g = Array.isArray(GAME) ? GAME[li] : GAME; return g.steps.length; }, li);
      for (let i = 0; i < n; i++) {
        const idx = await p.evaluate(([i, li]) => {
          const g = Array.isArray(GAME) ? GAME[li] : GAME;
          const bs = Array.from(document.querySelectorAll('.step'));
          const order = g.steps.map(s => s.t);
          return bs.findIndex(b => b.textContent.includes(order[i]) && !b.classList.contains('placed'));
        }, [i, li]);
        await p.locator('.step').nth(idx).click();
        await p.waitForTimeout(30);
      }
    }
  }
  r.mode = modes.join('+');
  r.gameStat = (await p.locator('.gstat').allTextContents()).join(' | ');

  // Quiz — sealed check
  await p.locator('.tab[data-go="quiz"]').click();
  await p.waitForTimeout(200);
  const nq = await p.evaluate(() => QUIZ.length);
  let leak = 0;
  for (let i = 0; i < nq; i++) {
    await p.locator('#qopts .opt').first().click();
    await p.waitForTimeout(280);
    leak += await p.locator('.opt.yes, .opt.no, .rev, .res.on').count();
  }
  r.leak = leak;
  r.answered = await p.locator('#qdone').textContent();
  await p.locator('#submit').click();
  await p.waitForTimeout(200);
  await p.locator('#mGo').click();
  await p.waitForTimeout(1200);
  r.pct = await p.locator('#pct').textContent();
  r.revs = await p.locator('.rev').count();
  r.ring = await p.locator('#ringTxt').textContent();
  r.oflow = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);

  r.ok = r.errs.length === 0 && r.arabicLeak === 0 && r.leak === 0 && r.oflow <= 0 && r.revs === nq;
  if (!r.ok) failCount++;
  out.push(r);
  await p.close();
}
await b.close();

for (const r of out) {
  console.log((r.ok ? 'PASS' : 'FAIL') + '  ' + r.file + '  ' + JSON.stringify(r));
}
console.log(`\n${out.length - failCount}/${out.length} pages passed.`);
process.exit(failCount ? 1 : 0);
