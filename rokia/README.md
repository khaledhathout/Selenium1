# Rokia's Lesson Pages

Nine interactive study pages, one per uploaded worksheet, for a 10-year-old.
Each page is a single self-contained HTML file that works offline.

| Page | Subject | From |
|---|---|---|
| `01-word-meanings.html` | Denotative and connotative meaning | English workbook, Unit 1 p.12 |
| `02-arabic-letters.html` | The 28 Arabic letters and their names | Arabic handwriting sheet |
| `03-search-engine.html` | Search engines, kid-safe engines, search tricks | ICT Lesson 1 |
| `04-browsers-netiquette.html` | Parts of a browser, browser names, netiquette | ICT worksheets |
| `05-science-skills.html` | Science skills, scientific method and investigation | Science notebook |
| `06-time-zones.html` | Minutes to hours, world time zones, UTC/GMT | Maths notebook |
| `07-map-lines.html` | Latitude, longitude and map vocabulary | Geography Lecture 2 |
| `08-needs-and-wants.html` | Needs, wants, allowance and saving | Money worksheet |
| `09-review-day.html` | Mixed review of all eight subjects | Combined scan |
| `10-poetry-meter.html` | Poetic meter, feet, and the four basic feet | English notebook |
| `11-value-prudence.html` | Value, prudence and everyday decisions | Character Education notebook |
| `12-word-2016.html` | Productivity software and the Word 2016 window | Computer notebook, Unit 1 |
| `13-measurement.html` | SI base units, the meniscus, temperature and mass conversion | Science notebook |
| `14-figures-of-speech.html` | Simile, metaphor, personification, hyperbole, alliteration, assonance, consonance | English 7 seatwork |
| `15-angle-pairs.html` | Exterior and interior angle pairs of a polygon, and their 180° rule | Math 7 notebook |
| `16-polygon-basics.html` | What makes a polygon, regular/irregular, convex/non-convex, and the (n−2)×180° interior angle sum | Math 7 textbook, Unit 1 |
| `17-grammar-toolkit.html` | Subject-verb agreement (incl. concrete/abstract/collective nouns), the three pronoun types, and adjective order | English Unit 1, Lesson 2 |

A glyph that is not English — an Arabic letter shown inside an English sentence —
is wrapped in `<span class="glyph" data-en="...">` so the eye sees the letter and
the voice says its name.

Every page has the same four sections: **Learn** (the lesson with English
read-aloud), **Cards** (flip cards), **Play** (a game — sort, match or order),
and **Quiz** (sealed: no answer is shown until the whole quiz is submitted).

English leads throughout; Arabic appears under it as a small support gloss and
is never spoken by the read-aloud.

## Rebuilding

The pages are generated so they stay consistent:

```
cd rokia && python3 -c "
import sys; sys.path.insert(0,'.')
from _build import build
import _content_a,_content_b,_content_c,_content_d
for p in _content_a.PAGES+_content_b.PAGES+_content_c.PAGES+_content_d.PAGES: build(p,'.')"
```

- `_kit.py` — the shared design system and engine (audio, cards, games, quiz)
- `_build.py` — page shell and builder
- `_content_*.py` — the lesson content, one dict per page
