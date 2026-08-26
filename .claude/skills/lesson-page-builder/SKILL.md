---
name: lesson-page-builder
description: >-
  Turn a scanned worksheet (PDF or photo) into a self-contained interactive
  HTML lesson page — Learn / Cards / Play / Quiz — for Razan, following the
  house standard proven across 19 pages in this repo (English primary,
  Arabic gloss only, English-only read-aloud, sealed quiz). Use this
  whenever new worksheet files arrive and the request is "turn this into a
  page" / "كمل" with attachments / add content to an existing page. Covers
  dedup against prior batches, content authoring, building, automated
  verification, README upkeep, and mirroring the output to the matching
  Grade05/Grade07 folder in Google Drive. Do NOT use for one-off page tweaks
  that don't touch content (pure CSS/layout fixes go straight to the file).
---

# Lesson Page Builder

Source file in, verified interactive page out, with nothing left to do by
hand afterward. This skill is the automated version of the pipeline that
built all 19 pages currently in this repo (`rokia/01-*.html` …
`rokia/17-*.html`, plus the two standalone pages
`razan_civics7_expedition.html` and `razan_farm_tools_manual.html`).

Two systems exist and this skill only owns one of them:

- **This repo (`rokia/`)** — flat, generated, offline HTML. This skill's
  job.
- **The Google Drive "Cowork" project** (`2026_School/Grade05`,
  `2026_School/Grade07`) — a separate, independently-evolved pipeline
  (voxel/Quest/Adventure formats, its own skills: `lesson-voxel-game`,
  `curriculum-pipeline`, `arabic-pdf-to-md`, `file-naming`,
  `arabic-markdown`). Do **not** try to reproduce that system here. This
  skill's only touchpoint with it is the final mirror step (§6) — pushing a
  copy of this repo's finished output into Drive so "what's in GitHub is
  also in Drive," per the standing instruction from the user. If Drive-side
  changes are ever needed, that is a job for a session working from that
  Drive project's own AGENTS.md, not this skill.

## The non-negotiable standard

Every page in this repo obeys these four rules. Verified automatically in
§5 — never take them on faith:

1. **English is primary.** Arabic is a small supporting gloss under the
   English (`.ar` / `.ar-block` / `.gloss` classes), never the main text.
2. **Read-aloud is English-only.** No Arabic character ever reaches
   `speechSynthesis`. Enforced by the `englishOf(el)` helper in
   `rokia/_kit.py` (clones the node, strips `.ar`/`.ar-block`/`.gloss`
   descendants, reads `textContent`). If an Arabic **glyph** must appear
   inside an English sentence (e.g. teaching the Arabic alphabet), wrap it
   as `<span class="glyph" data-en="letter name">` — `englishOf()`
   substitutes `data-en` for speech.
3. **Quizzes are sealed.** Selecting an option only records the choice
   (`.on` class) — no correctness, no score, nothing revealed until
   `submit()` is called at the end.
4. **Content is verbatim, never invented.** Quiz questions, sentences, and
   examples come from the source worksheet. If the worksheet's own answer
   key is wrong, use the grammatically/factually correct answer, not the
   student's marked one, but keep the sentence itself as printed.

## 1. Intake and dedup

New files arrive as PDFs or photos, often repeating pages from a prior
batch ("كمل" with attachments is the recurring pattern).

1. For each new PDF, extract the embedded page images (they're usually
   full-page JPEGs inside the PDF object stream).
2. `md5sum` every extracted page image and compare against the hashes of
   every page image already processed in this repo's history. Keep a
   running log — append to `rokia/README.md`'s source table (the "From"
   column already names the worksheet each page came from) or, for a large
   batch, a scratch file under the session's scratchpad — so this is a
   direct hash lookup next time, not a re-read of every prior PDF.
3. Anything with a matching hash is a duplicate — skip it. Report to the
   user which pages were new vs. duplicate before doing any content work,
   the way prior batches were triaged (e.g. "6 of 8 files are identical to
   the last batch").
4. For genuinely new pages, read the actual worksheet content (do not
   guess from filenames) before writing any content dict.

## 2. Decide: new page, or extend an existing one?

Default is a new page. Extend an existing page instead when the user says
so explicitly (e.g. "أضيف هذا مع صفحة 17") or the new material is a small,
closely-related addition to a topic already covered (a couple more
sentences/definitions on the same grammar point, not a new subject). When
extending:

- Add new `parts` entries to the existing page's `learn` list, new
  `cards`, and new `quiz` questions — do not rewrite existing ones.
- If the new material needs its own game, turn `game` into a list of labs
  (`game = [existing_lab, new_lab]`) rather than replacing the existing
  game. `_build.py` and `_kit.py` already support this (`LABS =
  Array.isArray(GAME) ? GAME : [GAME]`); give the added lab a `title`/
  `titleAr` so it renders as its own titled card.
- Bump `xpmax` is automatic — `_build.py` computes it from `game`/`quiz`
  length, nothing to hand-edit.

## 3. Author the content module

One dict per page, appended to `PAGES` in a `rokia/_content_*.py` module
(pick the module by file-size — start a new letter, e.g. `_content_j.py`,
once the current one is unwieldy; nothing else about the naming matters).

Required keys — copy the shape from any existing page in `_content_a.py`
through `_content_i.py`, don't invent a new schema:

```python
dict(
  file='NN-slug.html',
  title=..., eyebrow=..., palette=[...10 hex colors...],
  blurb=..., blurb_ar=...,
  learn_h=..., learn_p=..., learn_ar=...,
  parts=[...],                    # the Learn tab's accordion sections
  cards_h=..., cards_p=..., cards_ar=..., cards=[...],
  play_h=..., play_p=..., play_ar=..., game={...} or [{...}, {...}],
  quiz=[...],
)
```

Rules while writing it:

- Every English string that has an Arabic counterpart gets its own
  `_ar`/`ar` sibling key — never interleave the two languages in one
  string.
- Any table cell or list item containing both languages puts the Arabic in
  a nested `<div class="ar">...</div>` (or equivalent gloss class) — this
  is what `englishOf()` strips, so getting the class right here is what
  keeps rule 2 of the standard true.
- `game` mode is `sort` (classify into buckets), `match` (two-column
  pairing), or `order` (click into sequence) — pick whichever fits the
  content; look at an existing page using the same mode for the exact item
  shape it expects.
- Pick a `palette` distinct from neighboring pages so each page keeps its
  own visual identity (this repo has never reused a palette across pages).

## 4. Build

```bash
cd rokia && python3 build_all.py
```

This imports every `_content_*.py` module and calls `build()` for every
page in `PAGES` — the same driver for one new page or a full rebuild.
Adding a new `_content_*.py` module requires one line: add it to the
`MODULES` list at the top of `build_all.py`.

## 5. Verify — never skip, never sample

```bash
cd rokia && node verify.mjs           # every page
cd rokia && node verify.mjs 17        # just pages matching "17"
```

This opens each page in headless Chromium and, for every page:

- Opens **every** Learn part (not just the first) and calls the page's own
  `englishOf()` on each block — asserts zero Arabic characters make it
  into what speech synthesis would receive.
- Solves **every** lab in `GAME` (single object or array) to completion
  with correct picks.
- Answers **every** quiz question and asserts zero answer/score leakage
  before `submit()`, then submits and asserts every question got a review
  row.
- Asserts zero horizontal overflow and zero console/page errors.

A page is not done until `verify.mjs` prints `PASS` for it. This is not
optional polish — three real bugs in this repo's history (Arabic leaking
into TTS via nested `.ar` divs, Arabic glyphs leaking via embedded letters,
and a silent JS crash on the second lab of a multi-lab page) were only
caught because this exact check was run against every part/lab, not a
sampled subset. Trust the script's PASS/FAIL, not a visual skim.

If `playwright` isn't resolvable as a bare import in the current
environment, `verify.mjs` already falls back to this sandbox's global
install path — no manual fix needed unless that path itself has moved.

## 6. Update docs, commit, push

1. Add a row to `rokia/README.md`'s page table (or, if extending an
   existing page, update its row's description).
2. `git add` the changed/added `_content_*.py`, `build_all.py` (if new),
   the rebuilt `rokia/*.html` files, and `README.md`.
3. Commit with a message describing the page(s) added, not the mechanics
   ("Add polygon fundamentals page", not "run build_all.py").
4. Push to the working branch per the repo's standing git instructions.

## 7. Mirror to Drive

The user's standing instruction: whatever ships in this GitHub repo should
also exist in the Drive `2026_School` project, so cloud and Drive don't
diverge. After a push:

1. Find the right destination folder: `2026_School/Grade05` or
   `2026_School/Grade07`, matching which grade's worksheet the page came
   from (check the existing `Projects`/subject subfolders there before
   creating a new one — e.g. `Grade07/CIVICS` already exists and is where
   `razan_civics7_expedition.html`-type content belongs).
2. Upload each new/changed page with `mcp__Google_Drive__create_file`,
   `disableConversionToGoogleType: true` so the `.html` stays a plain file
   Drive can serve via `file://` rather than being converted to a Google
   Doc (a Doc conversion is fine for prose like a session export, but
   would break a page's own JS/CSS).
3. If a same-named file already exists at that path from a prior mirror,
   update it in place (`mcp__Google_Drive__update_file` for metadata, or
   trash-and-recreate for content — Drive's API has no in-place content
   overwrite) rather than accumulating duplicates.
4. This is a one-way mirror (GitHub → Drive). Never pull Drive-side voxel/
   Quest content into this repo's `rokia/` system — the two use
   incompatible engines by design.
