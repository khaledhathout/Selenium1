# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _kit import CSS, ENGINE

SHELL = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<header class="top">
  <div class="top-in">
    <div class="top-row">
      <div>
        <div class="eyebrow">{eyebrow}</div>
        <h1>{title}</h1>
        <div class="sub">{blurb}</div>
        <div class="ar">{blurb_ar}</div>
      </div>
      <div class="tools">
        <div class="ring">
          <svg viewBox="0 0 60 60" aria-hidden="true"><circle class="bg" cx="30" cy="30" r="26"></circle><circle class="fg" id="ringFg" cx="30" cy="30" r="26"></circle></svg>
          <b id="ringTxt">0%</b>
        </div>
        <div class="iconbtns">
          <button class="ib" id="tDn" title="Smaller text" aria-label="Smaller text">A−</button>
          <button class="ib" id="tUp" title="Bigger text" aria-label="Bigger text">A+</button>
          <button class="ib" id="themeBtn" title="Light or dark" aria-label="Light or dark">◐</button>
        </div>
      </div>
    </div>
  </div>
</header>

<nav class="tabs" aria-label="Sections">
  <button class="tab on" data-go="learn">Learn<span class="ar c">الدرس</span></button>
  <button class="tab" data-go="cards">Cards<span class="ar c">بطاقات</span></button>
  <button class="tab" data-go="play">Play<span class="ar c">لعبة</span></button>
  <button class="tab" data-go="quiz">Quiz<span class="ar c">اختبار</span></button>
</nav>

<main>
  <section class="panel on" id="learn">
    <div class="card">
      <span class="chip">Listen and read</span>
      <h2>{learn_h}</h2>
      <p class="lead">{learn_p}</p>
      <div class="ar">{learn_ar}</div>
      <div class="voicebar">
        <span class="chip" style="background:transparent;color:var(--muted)">Speed</span>
        <div class="seg" id="rateSeg">
          <button data-rate="0.7">0.7×</button><button data-rate="0.85" class="on">0.85×</button>
          <button data-rate="1">1×</button><button data-rate="1.15">1.15×</button>
        </div>
        <button class="btn" id="stopAll">Stop</button>
      </div>
    </div>
    <div id="parts"></div>
  </section>

  <section class="panel" id="cards">
    <div class="card">
      <span class="chip">Flip cards</span>
      <h2>{cards_h}</h2>
      <p class="lead">{cards_p}</p>
      <div class="ar">{cards_ar}</div>
    </div>
    <div class="deck">
      <div class="dcount" id="dcount"></div>
      <div class="flip">
        <div class="flip-in" id="flip" role="button" tabindex="0" aria-label="Flashcard, activate to flip">
          <div class="face face-a"><div class="big" id="cFront"></div><div class="ar c" id="cFrontAr"></div><div class="tapme">Tap to flip · اضغطي للقلب</div></div>
          <div class="face face-b"><div class="def" id="cBack"></div><div class="ar c" id="cBackAr"></div><div class="tapme">Tap to flip back</div></div>
        </div>
      </div>
      <div class="rowbtns" style="justify-content:center">{listen_card}</div>
      <div class="rowbtns"><button class="btn" id="cAgain" style="flex:1">Practise again</button><button class="btn solid" id="cKnow" style="flex:1">I know it</button></div>
      <div class="rowbtns"><button class="btn" id="cPrev" style="flex:1">◀ Back</button><button class="btn" id="cShuf" style="flex:1">Shuffle</button><button class="btn" id="cNext" style="flex:1">Next ▶</button></div>
      <div class="dstat" id="dstat"></div>
    </div>
  </section>

  <section class="panel" id="play">
    <div class="card">
      <span class="chip">Game · answers show at once</span>
      <h2>{play_h}</h2>
      <p class="lead">{play_p}</p>
      <div class="ar">{play_ar}</div>
    </div>
    <div id="playArea"></div>
    <div class="gstat" id="gstat"></div>
  </section>

  <section class="panel" id="quiz">
    <div id="quizLive">
      <div class="sealed">
        <span class="lock">🔒</span>
        <div>
          <p><b>Sealed quiz.</b> No answer and no tick appears while you work. Answer all {nq} questions, then press <b>See my score</b> — only then do the answers appear.</p>
          <div class="ar">اختبار مغلق: لا تظهر أي إجابة أو علامة أثناء الحل. جاوبي على الأسئلة كلها ثم اضغطي «See my score» — عندها فقط تظهر الإجابات.</div>
        </div>
      </div>
      <div class="card">
        <div style="display:flex;align-items:flex-end;justify-content:space-between;gap:1rem;flex-wrap:wrap">
          <div><span class="chip">Quiz</span><h2>{nq} Questions</h2></div>
          <div class="chip" id="clock" style="background:var(--soft);color:var(--muted)">0:00</div>
        </div>
        <div class="qbar"><i id="qfill"></i></div>
        <div class="qcount"><span id="qdone">0 answered</span><span id="qleft">{nq} to go</span></div>
      </div>
      <div class="card" id="qcard">
        <div class="qtop"><span class="qno" id="qno">Q1</span><span class="sp"></span>{listen_q}<button class="flagb" id="qflag">Flag</button></div>
        <div class="qtext" id="qtext"></div>
        <div class="ar" id="qar"></div>
        <div class="opts" id="qopts"></div>
        <div class="qnav"><button class="btn" id="qprev">◀ Back</button><button class="btn solid" id="qnext">Next ▶</button></div>
      </div>
      <div class="card">
        <span class="chip">Question map</span>
        <div class="qmap" id="qmap"></div>
        <div class="acts" style="margin-bottom:0"><button class="btn warm" id="submit">🔓 See my score<div class="ar">شوفي درجتك</div></button></div>
      </div>
    </div>
    <div class="res" id="res">
      <div class="score">
        <div class="dial"><svg viewBox="0 0 120 120" aria-hidden="true"><circle class="bg" cx="60" cy="60" r="54"></circle><circle class="fg" id="dialFg" cx="60" cy="60" r="54"></circle></svg>
          <div class="mid"><div class="pc" id="pct">0%</div><div class="gr" id="grade"></div></div></div>
        <h2 id="verdict"></h2>
        <div class="nt" id="vnote"></div>
        <div class="ar c" id="var" style="color:rgba(255,255,255,.9)"></div>
        <div class="tally"><div><b id="tR">0</b><span>Right</span></div><div><b id="tW">0</b><span>Missed</span></div><div><b id="tT">0:00</b><span>Time</span></div></div>
      </div>
      <div class="acts">
        <button class="btn solid" id="again">Try all again<div class="ar">أعيدي الكل</div></button>
        <button class="btn" id="missed">Retry missed<div class="ar">أعيدي الخطأ</div></button>
        <button class="btn" id="toLesson">Back to lesson<div class="ar">راجعي الدرس</div></button>
      </div>
      <div class="card"><span class="chip">Unsealed</span><h2>Every question and its answer</h2>
        <p class="lead">Your answer next to the right one. Press Listen to hear any question.</p>
        <div class="ar">إجابتك بجانب الإجابة الصحيحة. اضغطي «Listen» لسماع أي سؤال.</div></div>
      <div id="revList"></div>
    </div>
  </section>
</main>

<div class="veil" id="veil"><div class="modal"><h2 id="mTitle" style="font-size:1.15rem"></h2><p id="mBody"></p><div class="ar" id="mAr"></div>
  <div class="acts" style="margin-bottom:0"><button class="btn" id="mBack">Go back</button><button class="btn warm" id="mGo">Show me</button></div></div></div>
<div class="toast" id="toast"></div><div id="fx" aria-hidden="true"></div>

<script>
const PARTS={parts};
const CARDS={cards};
const GAME={game};
const QUIZ={quiz};
const XP_MAX={xpmax};
{engine}
</script>
</body>
</html>
"""

LISTEN = '<button id="{i}" class="listen{extra}" data-label="{l}"><span class="wave"><i></i><i></i><i></i></span><span class="lbl">{l}</span></button>'

def build(p, outdir):
    pal = p['palette']
    css = CSS
    for tok, val in zip(['A','AD','AW','B','BW','AL','ALD','ALW','BL','BLW'], pal):
        css = css.replace('%(' + tok + ')s', val)
    game = p['game']
    n_game = len(game.get('items') or game.get('pairs') or game.get('steps'))
    xpmax = n_game + len(p['quiz'])
    html = SHELL.format(
        title=p['title'], eyebrow=p['eyebrow'], blurb=p['blurb'], blurb_ar=p['blurb_ar'],
        learn_h=p['learn_h'], learn_p=p['learn_p'], learn_ar=p['learn_ar'],
        cards_h=p['cards_h'], cards_p=p['cards_p'], cards_ar=p['cards_ar'],
        play_h=p['play_h'], play_p=p['play_p'], play_ar=p['play_ar'],
        nq=len(p['quiz']), xpmax=xpmax, css=css, engine=ENGINE,
        listen_card=LISTEN.format(l='Listen to this card', extra='', i='cSay'),
        listen_q=LISTEN.format(l='Listen', extra=' mini', i='qsay'),
        parts=json.dumps(p['parts'], ensure_ascii=False),
        cards=json.dumps(p['cards'], ensure_ascii=False),
        game=json.dumps(game, ensure_ascii=False),
        quiz=json.dumps(p['quiz'], ensure_ascii=False))
    path = os.path.join(outdir, p['file'])
    open(path, 'w', encoding='utf-8').write(html)
    return path, xpmax
