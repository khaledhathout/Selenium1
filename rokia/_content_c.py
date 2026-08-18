# -*- coding: utf-8 -*-
PAGES = []

# ─────────────────────────── 6 · TIME & TIME ZONES ───────────────────────────
PAGES.append(dict(
 file='06-time-zones.html',
 title='Time Around the World',
 eyebrow='Maths · Time',
 palette=['#1f4e8c','#143764','#e3ecf8','#d9891c','#fbeed6',
          '#6fa4e0','#a3c6ef','#0d1b2c','#eaa94f','#3a2b12'],
 blurb='Turn minutes into hours, and find out why it is not the same o’clock everywhere.',
 blurb_ar='حوّلي الدقائق إلى ساعات، واعرفي لماذا الساعة ليست واحدة في كل مكان.',
 learn_h='Minutes, hours, and the world clock',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Time cards',
 cards_p='Work out the answer in your head first, then flip the card.',
 cards_ar='احسبي الإجابة في ذهنك أولاً ثم اقلبي البطاقة.',
 play_h='How many hours and minutes?',
 play_p='Choose the right answer for each number of minutes.',
 play_ar='اختاري الإجابة الصحيحة لكل عدد من الدقائق.',
 parts=[
  dict(n='1', t='Minutes into hours', ta='من الدقائق إلى الساعات',
    html='<p>There are <b>60 minutes</b> in one hour. So to change minutes into hours and minutes, take away 60 for each whole hour.</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Minutes</th><th>Working</th><th>Answer</th></tr>'
         '<tr><td>80</td><td>80 − 60 = 20</td><td>1 hour and 20 minutes</td></tr>'
         '<tr><td>65</td><td>65 − 60 = 5</td><td>1 hour and 5 minutes</td></tr>'
         '<tr><td>95</td><td>95 − 60 = 35</td><td>1 hour and 35 minutes</td></tr>'
         '<tr><td>100</td><td>100 − 60 = 40</td><td>1 hour and 40 minutes</td></tr>'
         '<tr><td>135</td><td>135 − 60 − 60 = 15</td><td>2 hours and 15 minutes</td></tr></table></div>',
    gloss='<p>الساعة الواحدة فيها <b>ستون دقيقة</b>. ولتحويل الدقائق إلى ساعات ودقائق نطرح ٦٠ لكل ساعة كاملة.</p>'
          '<p>مثال: ٨٠ − ٦٠ = ٢٠، أي ساعة و٢٠ دقيقة. و٩٥ − ٦٠ = ٣٥، أي ساعة و٣٥ دقيقة. و١٣٥ − ٦٠ − ٦٠ = ١٥، أي ساعتان و١٥ دقيقة.</p>'),
  dict(n='2', t='What is a time zone?', ta='ما المنطقة الزمنية؟',
    html='<p>A <b>time zone</b> is an area of the world that has the same clock time.</p>'
         '<p>The Earth spins around its axis, and one full turn takes <b>24 hours</b>. Because of this, the Earth is divided into <b>24 time zones</b>, and each zone is <b>1 hour apart</b> from the next one.</p>'
         '<p>That is why, when it is morning where you are, it can already be night on the other side of the world.</p>',
    gloss='<p><b>المنطقة الزمنية</b> منطقة من العالم لها نفس توقيت الساعة.</p>'
          '<p>تدور الأرض حول محورها، وتستغرق الدورة الكاملة <b>٢٤ ساعة</b>، لذلك قُسّمت الأرض إلى <b>٢٤ منطقة زمنية</b>، وبين كل منطقة والتي تليها <b>ساعة واحدة</b>.</p>'
          '<p>لهذا قد يكون الصباح عندك بينما هو ليل في الجهة الأخرى من العالم.</p>'),
  dict(n='3', t='Where time starts', ta='من أين يبدأ الوقت؟',
    html='<p>The time zones start at the <b>Prime Meridian</b>, the line at <b>0° longitude</b>. It is the starting point for measuring time.</p>'
         '<p>The time there is called <b>Coordinated Universal Time (UTC)</b>, also known as <b>Greenwich Mean Time (GMT)</b>.</p>'
         '<p>On the other side of the world is the <b>International Date Line</b> — an imaginary line where the date changes.</p>',
    gloss='<p>تبدأ المناطق الزمنية من <b>خط جرينتش</b> عند <b>خط طول صفر</b>، وهو نقطة البداية لقياس الوقت.</p>'
          '<p>ويسمى التوقيت هناك <b>التوقيت العالمي المنسق (UTC)</b>، ويُعرف أيضاً بـ<b>توقيت جرينتش (GMT)</b>.</p>'
          '<p>وفي الجهة المقابلة من العالم يقع <b>خط التاريخ الدولي</b>، وهو خط وهمي يتغير عنده التاريخ.</p>'),
  dict(n='4', t='Working out another city’s time', ta='حساب توقيت مدينة أخرى',
    html='<p>Each city has a number that shows how many hours it is ahead of (+) or behind (−) UTC.</p>'
         '<div class="hint"><p><b>Rule:</b> if the city is <b>+3</b>, add 3 hours to UTC. If it is <b>−7</b>, take away 7 hours.</p></div>'
         '<div class="scroll"><table class="tbl"><tr><th>City</th><th>Offset</th><th>If UTC is 12:00 noon</th></tr>'
         '<tr><td>Casablanca</td><td>+1</td><td>1:00 pm</td></tr>'
         '<tr><td>Canberra, Australia</td><td>+11</td><td>11:00 pm</td></tr>'
         '<tr><td>Guatemala City</td><td>−6</td><td>6:00 am</td></tr>'
         '<tr><td>Hong Kong</td><td>+8</td><td>8:00 pm</td></tr></table></div>'
         '<p>If your answer goes past 12, keep counting round the clock — and remember the day may change too.</p>',
    gloss='<p>لكل مدينة رقم يوضح كم ساعة تسبق (+) أو تتأخر (−) عن التوقيت العالمي.</p>'
          '<p><b>القاعدة:</b> إذا كانت المدينة <b>+٣</b> نضيف ٣ ساعات، وإذا كانت <b>−٧</b> نطرح ٧ ساعات.</p>'
          '<p>فإذا كانت الساعة ١٢ ظهراً بتوقيت جرينتش: الدار البيضاء ١ ظهراً، وكانبرا ١١ مساءً، وغواتيمالا ٦ صباحاً، وهونغ كونغ ٨ مساءً. وإذا تجاوز الناتج ١٢ نكمل الدوران حول الساعة، وقد يتغير اليوم أيضاً.</p>'),
 ],
 cards=[
  dict(f='60 minutes', fa='٦٠ دقيقة', b='That is exactly 1 hour.', ba='تساوي ساعة واحدة بالضبط.'),
  dict(f='80 minutes', fa='٨٠ دقيقة', b='1 hour and 20 minutes (80 − 60 = 20).', ba='ساعة و٢٠ دقيقة، لأن ٨٠ − ٦٠ = ٢٠.'),
  dict(f='95 minutes', fa='٩٥ دقيقة', b='1 hour and 35 minutes (95 − 60 = 35).', ba='ساعة و٣٥ دقيقة، لأن ٩٥ − ٦٠ = ٣٥.'),
  dict(f='135 minutes', fa='١٣٥ دقيقة', b='2 hours and 15 minutes (135 − 120 = 15).', ba='ساعتان و١٥ دقيقة، لأن ١٣٥ − ١٢٠ = ١٥.'),
  dict(f='Time zone', fa='منطقة زمنية', b='An area of the world that has the same clock time.', ba='منطقة من العالم لها نفس توقيت الساعة.'),
  dict(f='24', fa='٢٤', b='The number of time zones, and the hours in one full spin of the Earth.', ba='عدد المناطق الزمنية، وعدد ساعات دورة الأرض الكاملة.'),
  dict(f='Prime Meridian', fa='خط جرينتش', b='The line at 0° longitude where the time zones start.', ba='خط الطول صفر الذي تبدأ منه المناطق الزمنية.'),
  dict(f='UTC / GMT', fa='التوقيت العالمي', b='Coordinated Universal Time, also called Greenwich Mean Time.', ba='التوقيت العالمي المنسق، ويسمى أيضاً توقيت جرينتش.'),
  dict(f='International Date Line', fa='خط التاريخ الدولي', b='An imaginary line on the other side of the world where the date changes.', ba='خط وهمي في الجهة المقابلة من العالم يتغير عنده التاريخ.'),
 ],
 game=dict(mode='sort',
   buckets=[dict(k='a', label='1 h 20 m'), dict(k='b', label='1 h 35 m'), dict(k='c', label='2 h 5 m')],
   items=[
    dict(t='80 minutes', ta='٨٠ دقيقة', k='a'),
    dict(t='95 minutes', ta='٩٥ دقيقة', k='b'),
    dict(t='125 minutes', ta='١٢٥ دقيقة', k='c'),
    dict(t='60 + 20 minutes', ta='٦٠ + ٢٠ دقيقة', k='a'),
    dict(t='60 + 35 minutes', ta='٦٠ + ٣٥ دقيقة', k='b'),
    dict(t='120 + 5 minutes', ta='١٢٠ + ٥ دقائق', k='c'),
    dict(t='Half an hour after 50 minutes', ta='نصف ساعة بعد ٥٠ دقيقة', k='a'),
    dict(t='Two hours and five minutes', ta='ساعتان وخمس دقائق', k='c'),
   ]),
 quiz=[
  dict(q='How many minutes are in one hour?', a='كم دقيقة في الساعة؟', o=['30','50','60','100'], c=2),
  dict(q='80 minutes is the same as:', a='٨٠ دقيقة تساوي:', o=['1 hour and 20 minutes','1 hour and 30 minutes','2 hours','1 hour and 40 minutes'], c=0),
  dict(q='95 minutes is the same as:', a='٩٥ دقيقة تساوي:', o=['1 hour and 15 minutes','1 hour and 35 minutes','2 hours and 5 minutes','1 hour and 45 minutes'], c=1),
  dict(q='100 minutes is the same as:', a='١٠٠ دقيقة تساوي:', o=['1 hour and 40 minutes','1 hour and 30 minutes','2 hours','1 hour and 10 minutes'], c=0),
  dict(q='A time zone is:', a='المنطقة الزمنية هي:', o=['A country','An area of the world with the same clock time','A kind of clock','A map'], c=1),
  dict(q='One full turn of the Earth on its axis takes:', a='دورة الأرض الكاملة حول محورها تستغرق:', o=['12 hours','24 hours','365 days','60 minutes'], c=1),
  dict(q='How many time zones is the Earth divided into?', a='إلى كم منطقة زمنية تنقسم الأرض؟', o=['12','24','36','60'], c=1),
  dict(q='Each time zone is how far apart from the next?', a='كم الفرق بين كل منطقة زمنية والتي تليها؟', o=['1 hour','2 hours','30 minutes','12 hours'], c=0),
  dict(q='Time zones start at the Prime Meridian, which is at:', a='تبدأ المناطق الزمنية من خط جرينتش عند:', o=['0° longitude','90° longitude','180° longitude','45° latitude'], c=0),
  dict(q='UTC is also known as:', a='يُعرف التوقيت العالمي المنسق أيضاً بـ:', o=['Greenwich Mean Time','Pacific Time','Local Time','Summer Time'], c=0),
  dict(q='The imaginary line on the other side of the world where the date changes is the:', a='الخط الوهمي في الجهة المقابلة حيث يتغير التاريخ هو:', o=['Equator','International Date Line','Prime Meridian','Tropic of Cancer'], c=1),
  dict(q='If UTC is 12:00 noon, what time is it in a city that is +8?', a='إذا كانت الساعة ١٢ ظهراً بتوقيت جرينتش، فكم الساعة في مدينة توقيتها +٨؟', o=['4:00 am','8:00 pm','8:00 am','4:00 pm'], c=1),
 ]))

# ─────────────────────────── 7 · LATITUDE & LONGITUDE ───────────────────────────
PAGES.append(dict(
 file='07-map-lines.html',
 title='Lines on the Globe',
 eyebrow='Geography · Lecture 2',
 palette=['#0f7a6b','#0a5a4f','#dcf1ed','#b8651e','#f9e8d8',
          '#4fc9b4','#8ee0d0','#08302b','#e0965a','#3a2414'],
 blurb='Latitude, longitude, and the imaginary lines that help you find any place on Earth.',
 blurb_ar='خطوط العرض والطول والخطوط الوهمية التي تساعدك على إيجاد أي مكان على الأرض.',
 learn_h='Finding any place on Earth',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Map word cards',
 cards_p='Say the meaning out loud, then flip the card to check.',
 cards_ar='قولي المعنى بصوت عالٍ ثم اقلبي البطاقة للتأكد.',
 play_h='Across or up and down?',
 play_p='Decide whether each clue belongs to latitude or to longitude.',
 play_ar='حدّدي إن كان كل وصف يخص خطوط العرض أم خطوط الطول.',
 parts=[
  dict(n='1', t='Latitude and longitude', ta='خطوط العرض والطول',
    html='<p><b>Latitude</b> lines measure north and south. They run across the globe like the rungs of a ladder.</p>'
         '<p><b>Longitude</b> lines measure east and west. They run from the top of the globe to the bottom, like the slices of an orange.</p>'
         '<div class="hint"><p><b>Easy way to remember:</b> latitude is <i>flat</i> — it lies flat across the map. Longitude lines are <i>long</i> — they run the long way, pole to pole.</p></div>',
    gloss='<p><b>خطوط العرض</b> تقيس الشمال والجنوب، وتمتد أفقياً حول الكرة مثل درجات السلّم.</p>'
          '<p><b>خطوط الطول</b> تقيس الشرق والغرب، وتمتد من أعلى الكرة إلى أسفلها مثل شرائح البرتقالة.</p>'
          '<p><b>للتذكّر:</b> خط العرض «مسطّح» أفقي، وخطوط الطول «طويلة» من قطب إلى قطب.</p>'),
  dict(n='2', t='The important lines', ta='الخطوط المهمة',
    html='<div class="scroll"><table class="tbl"><tr><th>Word</th><th>Meaning</th></tr>'
         '<tr><td>Equator</td><td>An imaginary line around the middle of the Earth.</td></tr>'
         '<tr><td>Prime Meridian</td><td>The starting line for longitude, at 0°.</td></tr>'
         '<tr><td>International Date Line</td><td>The line on the other side of the world where the date changes.</td></tr>'
         '<tr><td>South Pole</td><td>The southernmost point on Earth.</td></tr>'
         '<tr><td>Grid</td><td>Lines used to find places on a map.</td></tr>'
         '<tr><td>360°</td><td>A full circle around the Earth.</td></tr></table></div>',
    gloss='<p><b>خط الاستواء</b> خط وهمي حول منتصف الأرض. <b>خط جرينتش</b> بداية خطوط الطول عند الدرجة صفر. <b>خط التاريخ الدولي</b> في الجهة المقابلة ويتغير عنده التاريخ. <b>القطب الجنوبي</b> أقصى نقطة جنوباً على الأرض. <b>الشبكة</b> خطوط تُستخدم لإيجاد الأماكن على الخريطة. و<b>٣٦٠ درجة</b> دورة كاملة حول الأرض.</p>'),
  dict(n='3', t='Vocabulary from the lecture', ta='مفردات المحاضرة',
    html='<div class="scroll"><table class="tbl"><tr><th>Word</th><th>Meaning</th></tr>'
         '<tr><td>Map</td><td>A flat representation of Earth.</td></tr>'
         '<tr><td>Meridian</td><td>A circle of constant longitude passing through a given place and the poles.</td></tr>'
         '<tr><td>Oblate spheroid</td><td>The shape of the Earth: broader in the middle and flatter at the poles.</td></tr>'
         '<tr><td>Parallel</td><td>An imaginary circle of constant latitude on the Earth’s surface.</td></tr></table></div>',
    gloss='<p><b>الخريطة</b> تمثيل مسطّح للأرض. <b>خط الزوال</b> دائرة خط طول ثابت تمر بمكان معيّن وبالقطبين. <b>الكروي المفلطح</b> شكل الأرض: أعرض في الوسط وأكثر تفلطحاً عند القطبين. <b>الدائرة العرضية</b> دائرة وهمية بخط عرض ثابت على سطح الأرض.</p>'),
  dict(n='4', t='Three kinds of relative location', ta='ثلاثة أنواع للموقع النسبي',
    html='<p><b>Relative location</b> means where a place is compared with something else.</p>'
         '<ul><li><b>Relative location</b> — the location of a place worked out from landmarks such as land and water boundaries.</li>'
         '<li><b>Relative continental location</b> — the location of a place worked out from the landforms around it.</li>'
         '<li><b>Relative maritime location</b> — the location of a place worked out from the bodies of water around it.</li></ul>'
         '<div class="hint"><p>Think: <i>continental</i> → land around it. <i>Maritime</i> → water around it.</p></div>',
    gloss='<p><b>الموقع النسبي</b> يعني موضع المكان بالمقارنة مع شيء آخر.</p>'
          '<p><b>الموقع النسبي</b> يُحدَّد بالمعالم مثل حدود اليابسة والماء. و<b>الموقع النسبي القاري</b> يُحدَّد بالتضاريس المحيطة. و<b>الموقع النسبي البحري</b> يُحدَّد بالمسطحات المائية المحيطة.</p>'
          '<p><b>تذكّري:</b> القاري ← يابسة حوله، والبحري ← ماء حوله.</p>'),
 ],
 cards=[
  dict(f='Latitude', fa='خطوط العرض', b='Lines that measure north and south.', ba='خطوط تقيس الشمال والجنوب.'),
  dict(f='Longitude', fa='خطوط الطول', b='Lines that measure east and west.', ba='خطوط تقيس الشرق والغرب.'),
  dict(f='Equator', fa='خط الاستواء', b='An imaginary line around the middle of the Earth.', ba='خط وهمي حول منتصف الأرض.'),
  dict(f='Grid', fa='الشبكة', b='Lines used to find places on a map.', ba='خطوط تُستخدم لإيجاد الأماكن على الخريطة.'),
  dict(f='South Pole', fa='القطب الجنوبي', b='The southernmost point on Earth.', ba='أقصى نقطة في جنوب الأرض.'),
  dict(f='360°', fa='٣٦٠ درجة', b='A full circle around the Earth.', ba='دورة كاملة حول الأرض.'),
  dict(f='Map', fa='الخريطة', b='A flat representation of Earth.', ba='تمثيل مسطّح للأرض.'),
  dict(f='Meridian', fa='خط الزوال', b='A circle of constant longitude passing through a place and the poles.', ba='دائرة خط طول ثابت تمر بمكان وبالقطبين.'),
  dict(f='Oblate spheroid', fa='كروي مفلطح', b='The Earth’s shape: broader in the middle, flatter at the poles.', ba='شكل الأرض: أعرض في الوسط وأفلط عند القطبين.'),
  dict(f='Parallel', fa='دائرة عرضية', b='An imaginary circle of constant latitude on Earth’s surface.', ba='دائرة وهمية بخط عرض ثابت على سطح الأرض.'),
  dict(f='Relative maritime location', fa='الموقع النسبي البحري', b='Where a place is, worked out from the water around it.', ba='موقع المكان محدداً بالمسطحات المائية حوله.'),
  dict(f='Relative continental location', fa='الموقع النسبي القاري', b='Where a place is, worked out from the landforms around it.', ba='موقع المكان محدداً بالتضاريس حوله.'),
 ],
 game=dict(mode='sort',
   buckets=[dict(k='lat', label='Latitude'), dict(k='lon', label='Longitude')],
   items=[
    dict(t='Measures north and south', ta='تقيس الشمال والجنوب', k='lat'),
    dict(t='Measures east and west', ta='تقيس الشرق والغرب', k='lon'),
    dict(t='The Equator is one of these', ta='خط الاستواء واحد منها', k='lat'),
    dict(t='The Prime Meridian is one of these', ta='خط جرينتش واحد منها', k='lon'),
    dict(t='Also called a parallel', ta='تسمى أيضاً دائرة عرضية', k='lat'),
    dict(t='Also called a meridian', ta='يسمى أيضاً خط زوال', k='lon'),
    dict(t='Runs across, like ladder rungs', ta='تمتد أفقياً مثل درجات السلّم', k='lat'),
    dict(t='Runs pole to pole, like orange slices', ta='يمتد من قطب لقطب مثل شرائح البرتقالة', k='lon'),
   ]),
 quiz=[
  dict(q='Latitude lines measure:', a='خطوط العرض تقيس:', o=['East and west','North and south','Up and down only','Time'], c=1),
  dict(q='Longitude lines measure:', a='خطوط الطول تقيس:', o=['North and south','East and west','Height','Temperature'], c=1),
  dict(q='The imaginary line around the middle of the Earth is the:', a='الخط الوهمي حول منتصف الأرض هو:', o=['Equator','Prime Meridian','International Date Line','Tropic of Cancer'], c=0),
  dict(q='A full circle around the Earth is:', a='الدورة الكاملة حول الأرض تساوي:', o=['90°','180°','270°','360°'], c=3),
  dict(q='Lines used to find places on a map are called a:', a='الخطوط المستخدمة لإيجاد الأماكن على الخريطة تسمى:', o=['Grid','Graph','Ladder','Legend'], c=0),
  dict(q='The southernmost point on Earth is the:', a='أقصى نقطة جنوباً على الأرض هي:', o=['North Pole','South Pole','Equator','Prime Meridian'], c=1),
  dict(q='A map is best described as:', a='أفضل وصف للخريطة:', o=['A flat representation of Earth','A round model of Earth','A photograph of a city','A list of countries'], c=0),
  dict(q='The shape of the Earth is called an:', a='يسمى شكل الأرض:', o=['Oblate spheroid','Perfect cube','Flat disc','Oval box'], c=0),
  dict(q='A parallel is an imaginary circle of constant:', a='الدائرة العرضية دائرة وهمية بـ:', o=['Longitude','Latitude','Temperature','Height'], c=1),
  dict(q='A meridian is a circle of constant longitude passing through a place and the:', a='خط الزوال دائرة خط طول ثابت تمر بمكان وبـ:', o=['Poles','Equator','Oceans','Deserts'], c=0),
  dict(q='Relative maritime location is worked out from the surrounding:', a='الموقع النسبي البحري يُحدَّد من:', o=['Bodies of water','Mountains','Cities','Roads'], c=0),
  dict(q='Relative continental location is worked out from the surrounding:', a='الموقع النسبي القاري يُحدَّد من:', o=['Landforms','Oceans','Stars','Clouds'], c=0),
 ]))

# ─────────────────────────── 8 · NEEDS AND WANTS ───────────────────────────
PAGES.append(dict(
 file='08-needs-and-wants.html',
 title='Needs, Wants and Saving',
 eyebrow='Money sense',
 palette=['#b8365f','#8d2246','#fae4ec','#0f8a7a','#d9f2ee',
          '#f0819f','#f7b0c4','#3d1524','#4fc9b4','#0c322c'],
 blurb='Some things you must have. Some things you would like. Learn to tell them apart — and to save.',
 blurb_ar='أشياء لا بد منها، وأشياء تتمنينها. تعلّمي التفريق بينها، وتعلّمي الادخار.',
 learn_h='Spending with a plan',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Money cards',
 cards_p='Decide need or want first, then flip the card to check.',
 cards_ar='قرري: احتياج أم رغبة؟ ثم اقلبي البطاقة للتأكد.',
 play_h='Need or want?',
 play_p='Sort each thing into the right basket.',
 play_ar='صنّفي كل شيء في السلة الصحيحة.',
 parts=[
  dict(n='1', t='Needs and wants', ta='الاحتياجات والرغبات',
    html='<p>A <b>need</b> is something you must have to live, to be healthy, or to go to school. Food, water, and transport to school are needs.</p>'
         '<p>A <b>want</b> is something that is nice to have, but you would still be fine without it. Snacks, sweet drinks, and toys are wants.</p>'
         '<div class="hint"><p><b>Test it:</b> ask yourself, “What happens if I don’t buy this?” If the answer is “nothing bad”, it is a want.</p></div>',
    gloss='<p><b>الاحتياج</b> شيء لا بد منه للعيش أو الصحة أو الذهاب للمدرسة، مثل الطعام والماء والمواصلات.</p>'
          '<p><b>الرغبة</b> شيء جميل لكن يمكن الاستغناء عنه، مثل الحلويات والمشروبات الغازية واللعب.</p>'
          '<p><b>اختبار سريع:</b> اسألي نفسك «ماذا يحدث لو لم أشترِه؟» إذا كانت الإجابة «لا شيء» فهو رغبة.</p>'),
  dict(n='2', t='A weekly plan', ta='خطة أسبوعية',
    html='<p>Here is the plan from the worksheet. The allowance for the week is <b>400</b> in total.</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Needs</th><th>Amount</th><th>Wants</th><th>Amount</th></tr>'
         '<tr><td>Transportation</td><td>50</td><td>Snacks</td><td>50</td></tr>'
         '<tr><td>School supplies</td><td>50</td><td>Drinks</td><td>50</td></tr>'
         '<tr><td>Water</td><td>50</td><td>Waffle</td><td>50</td></tr>'
         '<tr><td>Food</td><td>50</td><td>Toy</td><td>50</td></tr>'
         '<tr><td><b>Needs total</b></td><td><b>200</b></td><td><b>Wants total</b></td><td><b>200</b></td></tr></table></div>'
         '<p>200 + 200 = <b>400</b>. Everything is spent and nothing is left.</p>',
    gloss='<p>هذه خطة الورقة: المصروف الأسبوعي <b>٤٠٠</b> إجمالاً.</p>'
          '<p>الاحتياجات: مواصلات ٥٠، أدوات مدرسية ٥٠، ماء ٥٠، طعام ٥٠ — المجموع ٢٠٠. والرغبات: وجبات خفيفة ٥٠، مشروبات ٥٠، وافل ٥٠، لعبة ٥٠ — المجموع ٢٠٠.</p>'
          '<p>٢٠٠ + ٢٠٠ = <b>٤٠٠</b>، أي أن كل المبلغ أُنفق ولم يتبقَّ شيء.</p>'),
  dict(n='3', t='Where does saving fit?', ta='أين يأتي الادخار؟',
    html='<p>If every coin is spent, the amount saved is <b>zero</b>. <b>Saving</b> means keeping some money instead of spending it all.</p>'
         '<p>The easy way is to make saving the <b>first</b> thing you do, not the last:</p>'
         '<ol><li>Pay for your needs first.</li><li>Put some money aside to save.</li><li>Spend what is left on wants.</li></ol>'
         '<div class="hint"><p><b>Try it:</b> if one want (say the toy, 50) is moved into savings, the plan becomes needs 200, wants 150, <b>saved 50</b>.</p></div>',
    gloss='<p>إذا أُنفق كل شيء يصبح المدخر <b>صفراً</b>. و<b>الادخار</b> أن تحتفظي بجزء من المال بدل إنفاقه كله.</p>'
          '<p>والطريقة السهلة أن يكون الادخار <b>أولاً</b> لا أخيراً: ادفعي للاحتياجات، ثم ضعي جزءاً للادخار، ثم أنفقي الباقي على الرغبات.</p>'
          '<p><b>جربي:</b> لو نقلتِ اللعبة (٥٠) إلى الادخار تصبح الخطة: احتياجات ٢٠٠، رغبات ١٥٠، <b>مدخر ٥٠</b>.</p>'),
  dict(n='4', t='Three money habits', ta='ثلاث عادات مالية',
    html='<ul><li><b>Plan before you spend.</b> Write your needs and wants down first.</li>'
         '<li><b>Wait one day.</b> If you still want it tomorrow, it might be worth buying.</li>'
         '<li><b>Keep a total.</b> Add up what you spend so you always know what is left.</li></ul>',
    gloss='<p><b>خططي قبل أن تنفقي</b> واكتبي احتياجاتك ورغباتك أولاً. <b>وانتظري يوماً</b>، فإن بقيت الرغبة غداً فربما تستحق الشراء. <b>واحسبي المجموع</b> دائماً لتعرفي كم تبقّى معك.</p>'),
 ],
 cards=[
  dict(f='Need', fa='احتياج', b='Something you must have to live, be healthy, or go to school.', ba='شيء لا بد منه للعيش أو الصحة أو المدرسة.'),
  dict(f='Want', fa='رغبة', b='Something nice to have, but you would be fine without it.', ba='شيء جميل لكن يمكن الاستغناء عنه.'),
  dict(f='Saving', fa='الادخار', b='Keeping some money instead of spending it all.', ba='الاحتفاظ بجزء من المال بدل إنفاقه كله.'),
  dict(f='Allowance', fa='المصروف', b='The money you are given for the week.', ba='المبلغ الذي تحصلين عليه أسبوعياً.'),
  dict(f='Expenses', fa='المصروفات', b='All the things you spend your money on.', ba='كل ما تنفقين مالك عليه.'),
  dict(f='Transportation', fa='المواصلات', b='A need — it gets you to school.', ba='احتياج، لأنه يوصلك إلى المدرسة.'),
  dict(f='School supplies', fa='الأدوات المدرسية', b='A need — you cannot do your work without them.', ba='احتياج، فلا يمكن أداء الواجبات بدونها.'),
  dict(f='A toy', fa='لعبة', b='A want — lovely to have, but not needed.', ba='رغبة، جميلة لكنها ليست ضرورية.'),
  dict(f='200 + 200', fa='٢٠٠ + ٢٠٠', b='400 — the whole weekly allowance in the worksheet.', ba='٤٠٠، وهو كامل المصروف الأسبوعي في الورقة.'),
 ],
 game=dict(mode='sort',
   buckets=[dict(k='n', label='Need'), dict(k='w', label='Want')],
   items=[
    dict(t='Water', ta='ماء', k='n'),
    dict(t='Food', ta='طعام', k='n'),
    dict(t='Transport to school', ta='مواصلات المدرسة', k='n'),
    dict(t='School supplies', ta='أدوات مدرسية', k='n'),
    dict(t='Snacks', ta='وجبات خفيفة', k='w'),
    dict(t='Fizzy drinks', ta='مشروبات غازية', k='w'),
    dict(t='A waffle', ta='وافل', k='w'),
    dict(t='A new toy', ta='لعبة جديدة', k='w'),
    dict(t='Medicine when you are ill', ta='دواء عند المرض', k='n'),
    dict(t='A game for your tablet', ta='لعبة على التابلت', k='w'),
   ]),
 quiz=[
  dict(q='A need is something that:', a='الاحتياج شيء:', o=['You must have to live or learn','Is only for fun','Costs the most money','Is always cheap'], c=0),
  dict(q='Which of these is a want?', a='أي مما يلي رغبة؟', o=['Water','A new toy','Food','School supplies'], c=1),
  dict(q='Which of these is a need?', a='أي مما يلي احتياج؟', o=['Snacks','A waffle','Transportation to school','A tablet game'], c=2),
  dict(q='In the plan, needs cost 200 and wants cost 200. The total spent is:', a='في الخطة: احتياجات ٢٠٠ ورغبات ٢٠٠، فالمجموع المُنفق:', o=['200','300','400','500'], c=2),
  dict(q='If the whole allowance is spent, the amount saved is:', a='إذا أُنفق كل المصروف يكون المدخر:', o=['Zero','Half','All of it','200'], c=0),
  dict(q='Saving means:', a='الادخار يعني:', o=['Spending everything quickly','Keeping some money instead of spending it all','Borrowing money','Losing money'], c=1),
  dict(q='The best order for your money is:', a='أفضل ترتيب لإنفاق مالك:', o=['Wants, then needs, then saving','Needs, then saving, then wants','Saving only','Wants only'], c=1),
  dict(q='If the toy (50) is moved into savings, how much is saved?', a='إذا نُقلت اللعبة (٥٠) إلى الادخار، كم يصبح المدخر؟', o=['0','50','100','200'], c=1),
  dict(q='A good habit before buying something is to:', a='من العادات الجيدة قبل الشراء:', o=['Buy it straight away','Wait one day and see if you still want it','Ask no one','Spend twice as much'], c=1),
  dict(q='Why is it useful to keep a total of what you spend?', a='لماذا من المفيد حساب مجموع ما تنفقين؟', o=['So you always know what is left','So the money grows by itself','So shopping is faster','It is not useful'], c=0),
 ]))
