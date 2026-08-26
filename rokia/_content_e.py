# -*- coding: utf-8 -*-
PAGES = []

# ─────────────────────────── 10 · POETRY: METER AND FEET ───────────────────────────
PAGES.append(dict(
 file='10-poetry-meter.html',
 title='The Beat of a Poem',
 eyebrow='English · Poetry',
 palette=['#8a4b78','#66365a','#f6e8f3','#c78b2a','#faeed6',
          '#d094c4','#e6bfe0','#3a1f34','#e0b463','#3a2c12'],
 blurb='Poems have a heartbeat. Learn to count it, name it, and hear it in every line.',
 blurb_ar='للقصيدة نبض. تعلّمي كيف تعدّينه وتسمّينه وتسمعينه في كل سطر.',
 learn_h='Meter, feet, and rhythm',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Poetry cards',
 cards_p='Say the meaning out loud, then flip the card to check.',
 cards_ar='قولي المعنى بصوت عالٍ ثم اقلبي البطاقة للتأكد.',
 play_h='Match each foot to its beat',
 play_p='Tap a foot on the left, then tap its rhythm on the right.',
 play_ar='اضغطي على التفعيلة في اليسار ثم على إيقاعها في اليمين.',
 parts=[
  dict(n='1', t='What is meter?', ta='ما الوزن الشعري؟',
    html='<p><b>Meter</b> is the measured beat of a line of poetry. Three things decide the meter of a line:</p>'
         '<ol><li>The <b>number of syllables</b> in the line.</li>'
         '<li>The <b>number of feet</b> in the line.</li>'
         '<li>The <b>stress and pattern</b> — which syllables are said louder.</li></ol>'
         '<p>Read a line out loud and tap the table with your finger. The taps you press hardest on are the <b>stressed</b> syllables.</p>',
    gloss='<p><b>الوزن</b> هو الإيقاع المنتظم لسطر الشعر، ويتحدد بثلاثة أمور: <b>عدد المقاطع</b> في السطر، و<b>عدد التفعيلات</b>، و<b>النبر والنمط</b> أي المقاطع التي تُنطق بقوة أكبر.</p>'
          '<p>اقرئي السطر بصوت عالٍ واطرقي بإصبعك على الطاولة؛ الطرقات الأقوى هي المقاطع <b>المنبورة</b>.</p>'),
  dict(n='2', t='What is a foot?', ta='ما التفعيلة؟',
    html='<p>A <b>foot</b> is a unit of rhythm. It is a regular pattern of <b>stressed</b> and <b>unstressed</b> syllables.</p>'
         '<p>Stressed syllables are also called <b>accented</b>. Unstressed syllables are called <b>unaccented</b>.</p>'
         '<div class="hint"><p>We write the beat like a drum: <b>da</b> for a quiet syllable and <b>DUM</b> for a strong one. So “be-LOW” is <b>da-DUM</b>.</p></div>'
         '<p>A line of poetry is simply feet joined one after another, like beads on a string.</p>',
    gloss='<p><b>التفعيلة</b> وحدة إيقاعية، وهي نمط منتظم من المقاطع <b>المنبورة</b> و<b>غير المنبورة</b>.</p>'
          '<p>ويسمى المقطع المنبور <b>accented</b>، وغير المنبور <b>unaccented</b>.</p>'
          '<p>ونكتب الإيقاع كالطبل: <b>da</b> للمقطع الخفيف و<b>DUM</b> للقوي، فكلمة “be-LOW” تكون <b>da-DUM</b>. والسطر الشعري تفعيلات متتابعة كحبات العقد.</p>'),
  dict(n='3', t='The four basic feet', ta='التفعيلات الأربع الأساسية',
    html='<div class="scroll"><table class="tbl"><tr><th>Foot</th><th>Syllables</th><th>Beat</th><th>Example word</th></tr>'
         '<tr><td>Iamb</td><td>2</td><td>da-DUM</td><td>be-LOW, a-GAIN</td></tr>'
         '<tr><td>Trochee</td><td>2</td><td>DUM-da</td><td>GAR-den, HAP-py</td></tr>'
         '<tr><td>Anapaest</td><td>3</td><td>da-da-DUM</td><td>un-der-STAND</td></tr>'
         '<tr><td>Dactyl</td><td>3</td><td>DUM-da-da</td><td>EL-e-phant, BEAU-ti-ful</td></tr></table></div>'
         '<div class="hint"><p><b>The quick way to remember:</b> iamb and trochee are the two-syllable pair and are mirror images. Anapaest and dactyl are the three-syllable pair, and they are mirror images too.</p></div>',
    gloss='<p><b>الأيامب</b> مقطعان: خفيف ثم قوي (da-DUM). و<b>التروكي</b> مقطعان: قوي ثم خفيف (DUM-da). و<b>الأنابيست</b> ثلاثة: خفيف خفيف قوي (da-da-DUM). و<b>الداكتيل</b> ثلاثة: قوي خفيف خفيف (DUM-da-da).</p>'
          '<p><b>للتذكّر:</b> الأيامب والتروكي زوج من مقطعين وكل منهما عكس الآخر، والأنابيست والداكتيل زوج من ثلاثة مقاطع وكل منهما عكس الآخر.</p>'),
  dict(n='4', t='Counting the feet in a line', ta='عدّ التفعيلات في السطر',
    html='<p>Once you know the foot, count how many times it repeats. That gives the line its full name.</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Feet in the line</th><th>Name</th></tr>'
         '<tr><td>1</td><td>Monometer</td></tr><tr><td>2</td><td>Dimeter</td></tr>'
         '<tr><td>3</td><td>Trimeter</td></tr><tr><td>4</td><td>Tetrameter</td></tr>'
         '<tr><td>5</td><td>Pentameter</td></tr><tr><td>6</td><td>Hexameter</td></tr></table></div>'
         '<p>So a line of five iambs — da-DUM da-DUM da-DUM da-DUM da-DUM — is called <b>iambic pentameter</b>. It is the most famous meter in English poetry.</p>',
    gloss='<p>بعد معرفة نوع التفعيلة، عُدّي كم مرة تتكرر ليكتمل اسم السطر: واحدة monometer، واثنتان dimeter، وثلاث trimeter، وأربع tetrameter، وخمس pentameter، وست hexameter.</p>'
          '<p>فالسطر المكوّن من خمس تفعيلات أيامب يسمى <b>iambic pentameter</b>، وهو أشهر وزن في الشعر الإنجليزي.</p>'),
 ],
 cards=[
  dict(f='Meter', fa='الوزن', b='The measured beat of a line of poetry.', ba='الإيقاع المنتظم لسطر الشعر.'),
  dict(f='The three factors of meter', fa='عوامل الوزن الثلاثة', b='Number of syllables, number of feet, and stress and pattern.', ba='عدد المقاطع، وعدد التفعيلات، والنبر والنمط.'),
  dict(f='Foot', fa='التفعيلة', b='A unit of rhythm: a regular pattern of stressed and unstressed syllables.', ba='وحدة إيقاعية: نمط منتظم من المقاطع المنبورة وغير المنبورة.'),
  dict(f='Accented syllable', fa='مقطع منبور', b='A stressed syllable — the one you say louder.', ba='المقطع الذي يُنطق بقوة أكبر.'),
  dict(f='Unaccented syllable', fa='مقطع غير منبور', b='An unstressed syllable — the quieter one.', ba='المقطع الذي يُنطق بصوت أخف.'),
  dict(f='Iamb', fa='أيامب', b='Two syllables: da-DUM, as in “be-LOW”.', ba='مقطعان: خفيف ثم قوي، مثل be-LOW.'),
  dict(f='Trochee', fa='تروكي', b='Two syllables: DUM-da, as in “GAR-den”.', ba='مقطعان: قوي ثم خفيف، مثل GAR-den.'),
  dict(f='Anapaest', fa='أنابيست', b='Three syllables: da-da-DUM, as in “un-der-STAND”.', ba='ثلاثة مقاطع: خفيف خفيف قوي، مثل un-der-STAND.'),
  dict(f='Dactyl', fa='داكتيل', b='Three syllables: DUM-da-da, as in “EL-e-phant”.', ba='ثلاثة مقاطع: قوي خفيف خفيف، مثل EL-e-phant.'),
  dict(f='Iambic pentameter', fa='الخماسي الأيامبي', b='Five iambs in one line — the most famous meter in English poetry.', ba='خمس تفعيلات أيامب في السطر، وهو أشهر وزن في الشعر الإنجليزي.'),
 ],
 game=dict(mode='match', pairs=[
   dict(a='Iamb', aa='أيامب', b='da-DUM', ba='خفيف ثم قوي'),
   dict(a='Trochee', aa='تروكي', b='DUM-da', ba='قوي ثم خفيف'),
   dict(a='Anapaest', aa='أنابيست', b='da-da-DUM', ba='خفيف خفيف قوي'),
   dict(a='Dactyl', aa='داكتيل', b='DUM-da-da', ba='قوي خفيف خفيف'),
   dict(a='Foot', aa='تفعيلة', b='A unit of rhythm', ba='وحدة إيقاعية'),
   dict(a='Meter', aa='وزن', b='The measured beat of a line', ba='الإيقاع المنتظم للسطر'),
   dict(a='Pentameter', aa='خماسي', b='Five feet in one line', ba='خمس تفعيلات في السطر'),
   dict(a='Accented', aa='منبور', b='The stressed syllable', ba='المقطع القوي'),
 ]),
 quiz=[
  dict(q='Meter is decided by three factors. Which of these is NOT one of them?', a='الوزن تحدده ثلاثة عوامل، أيها ليس منها؟',
       o=['Number of syllables','Number of feet','Stress and pattern','Number of letters'], c=3),
  dict(q='A foot is best described as:', a='أفضل وصف للتفعيلة:',
       o=['A unit of rhythm made of stressed and unstressed syllables','The last word of a line','The title of a poem','A rhyme at the end'], c=0),
  dict(q='Another word for a stressed syllable is:', a='كلمة أخرى للمقطع المنبور:',
       o=['Unaccented','Accented','Silent','Rhymed'], c=1),
  dict(q='How many syllables are in an iamb?', a='كم مقطعاً في الأيامب؟', o=['1','2','3','4'], c=1),
  dict(q='How many syllables are in a dactyl?', a='كم مقطعاً في الداكتيل؟', o=['2','3','4','5'], c=1),
  dict(q='Which foot has the beat da-DUM?', a='أي تفعيلة إيقاعها da-DUM؟', o=['Trochee','Iamb','Dactyl','Anapaest'], c=1),
  dict(q='Which foot has the beat DUM-da?', a='أي تفعيلة إيقاعها DUM-da؟', o=['Iamb','Trochee','Anapaest','Dactyl'], c=1),
  dict(q='Which foot has the beat da-da-DUM?', a='أي تفعيلة إيقاعها da-da-DUM؟', o=['Anapaest','Dactyl','Iamb','Trochee'], c=0),
  dict(q='“EL-e-phant” is an example of a:', a='كلمة EL-e-phant مثال على:', o=['Iamb','Trochee','Dactyl','Anapaest'], c=2),
  dict(q='Which two feet have three syllables each?', a='أي تفعيلتين فيهما ثلاثة مقاطع؟',
       o=['Iamb and trochee','Anapaest and dactyl','Iamb and dactyl','Trochee and anapaest'], c=1),
  dict(q='A line with five feet is called:', a='السطر المكوّن من خمس تفعيلات يسمى:', o=['Trimeter','Tetrameter','Pentameter','Hexameter'], c=2),
  dict(q='A line of five iambs is called:', a='السطر المكوّن من خمس تفعيلات أيامب يسمى:',
       o=['Trochaic tetrameter','Iambic pentameter','Dactylic hexameter','Anapaestic dimeter'], c=1),
 ]))

# ─────────────────────────── 11 · VALUE AND PRUDENCE ───────────────────────────
PAGES.append(dict(
 file='11-value-prudence.html',
 title='Value and Prudence',
 eyebrow='Character Education',
 palette=['#8a6a1f','#664e13','#f7eed6','#2f7d6b','#dbf0ec',
          '#e0bd63','#f0d999','#3a2e10','#5fc3ad','#0d3630'],
 blurb='Every good act carries a value. Prudence is knowing how much of it to show, and when.',
 blurb_ar='كل فعل حسن يحمل قيمة، والتعقّل أن تعرفي مقدار ما تُظهرينه منها ومتى.',
 learn_h='Thinking before you act',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Value cards',
 cards_p='Say the meaning out loud, then flip the card to check.',
 cards_ar='قولي المعنى بصوت عالٍ ثم اقلبي البطاقة للتأكد.',
 play_h='What would a prudent person do?',
 play_p='Match each everyday decision to the thoughtful choice.',
 play_ar='وصّلي كل قرار يومي بالاختيار المتعقّل.',
 parts=[
  dict(n='1', t='What is a value?', ta='ما القيمة؟',
    html='<p>A <b>value</b> is the good which is intrinsically found in every being, and in every action which flows from it.</p>'
         '<p><i>Intrinsically</i> means the good is already inside the thing itself — nobody has to add it from outside.</p>'
         '<div class="hint"><p>So honesty is not good because someone praises it. It is good in itself, and the actions that come out of it carry that same goodness.</p></div>',
    gloss='<p><b>القيمة</b> هي الخير الموجود جوهرياً في كل كائن، وفي كل فعل ينبع منه.</p>'
          '<p>وكلمة <i>جوهرياً</i> تعني أن الخير موجود داخل الشيء نفسه، لا يضيفه أحد من الخارج.</p>'
          '<p>فالصدق ليس خيراً لأن أحداً امتدحه، بل هو خير في ذاته، والأفعال النابعة منه تحمل الخير نفسه.</p>'),
  dict(n='2', t='What is prudence?', ta='ما التعقّل؟',
    html='<p><b>Prudence</b> helps all persons to correctly measure the appropriate intensity, or the right amount, of the value a person needs to show.</p>'
         '<p>Notice the two words that matter: <b>measure</b> and <b>appropriate</b>. Prudence is not about doing less good — it is about doing the right good, in the right amount, at the right time.</p>'
         '<div class="hint"><p>Being generous is a value. Prudence tells you whether to give your friend your last pen, or to lend it and ask for it back at the end of the lesson.</p></div>',
    gloss='<p><b>التعقّل</b> يساعد كل إنسان على أن يقيس بدقة الشدة المناسبة، أي المقدار الصحيح، من القيمة التي يحتاج أن يُظهرها.</p>'
          '<p>وانتبهي لكلمتين مهمتين: <b>يقيس</b> و<b>المناسب</b>. فالتعقّل ليس تقليلاً للخير، بل فعل الخير الصحيح بالمقدار الصحيح في الوقت الصحيح.</p>'
          '<p>الكرم قيمة، والتعقّل يخبرك: أتعطين صديقتك آخر قلم لديك، أم تعيرينها إياه وتستردّينه في نهاية الحصة؟</p>'),
  dict(n='3', t='A saying to keep', ta='حكمة تُحفظ',
    html='<p>A Filipino saying puts it simply:</p>'
         '<p style="font-size:1.15rem;font-weight:700">“Bago mo sabihin, sampung beses mo munang isipin.”</p>'
         '<p>It means: <b>before you say it, think about it ten times first</b>.</p>'
         '<p>The pause between the thought and the word is where prudence lives.</p>',
    gloss='<p>يقول مثل فلبيني: «Bago mo sabihin, sampung beses mo munang isipin».</p>'
          '<p>ومعناه: <b>قبل أن تقولي شيئاً، فكّري فيه عشر مرات أولاً</b>.</p>'
          '<p>وفي تلك اللحظة الفاصلة بين الفكرة والكلمة يسكن التعقّل.</p>'),
  dict(n='4', t='Prudence in ordinary decisions', ta='التعقّل في القرارات اليومية',
    html='<p>Making decisions involves simple and mundane things, like these eight:</p>'
         '<ol><li>What time should I wake up?</li><li>How will I fix my hair?</li>'
         '<li>What things should I bring to school?</li><li>What do I eat during recess?</li>'
         '<li>Where do I throw my trash?</li><li>Who will I consult regarding my homework?</li>'
         '<li>What app should I use?</li><li>What time will I go home?</li></ol>'
         '<p>None of these is dramatic. That is exactly the point: prudence is built in small, ordinary choices, long before the big ones arrive.</p>',
    gloss='<p>اتخاذ القرار يشمل أموراً بسيطة يومية، منها هذه الثمانية: متى أستيقظ؟ وكيف أصفف شعري؟ وماذا أحمل إلى المدرسة؟ وماذا آكل في الفسحة؟ وأين أرمي نفاياتي؟ ومن أستشير في واجبي؟ وأي تطبيق أستخدم؟ ومتى أعود إلى البيت؟</p>'
          '<p>لا شيء منها كبير، وهذا هو المقصود: التعقّل يُبنى في الاختيارات الصغيرة اليومية قبل أن تأتي الكبيرة.</p>'),
 ],
 cards=[
  dict(f='Value', fa='القيمة', b='The good which is intrinsically found in every being and every action that flows from it.', ba='الخير الموجود جوهرياً في كل كائن وفي كل فعل ينبع منه.'),
  dict(f='Intrinsic', fa='جوهري', b='Already inside the thing itself, not added from outside.', ba='موجود داخل الشيء نفسه، لا يُضاف من الخارج.'),
  dict(f='Prudence', fa='التعقّل', b='Correctly measuring the appropriate amount of a value a person needs to show.', ba='قياس المقدار المناسب من القيمة التي يحتاج الإنسان أن يُظهرها.'),
  dict(f='Appropriate intensity', fa='الشدة المناسبة', b='The right amount — not too little, not too much.', ba='المقدار الصحيح، لا قليلاً ولا مبالغاً فيه.'),
  dict(f='“Bago mo sabihin…”', fa='المثل الفلبيني', b='Before you say it, think about it ten times first.', ba='قبل أن تقولي شيئاً، فكّري فيه عشر مرات أولاً.'),
  dict(f='Mundane decisions', fa='قرارات يومية', b='Simple everyday choices — where prudence is really built.', ba='الاختيارات اليومية البسيطة، وفيها يُبنى التعقّل حقاً.'),
  dict(f='Consulting someone', fa='الاستشارة', b='Asking a wise person before deciding — a prudent habit.', ba='سؤال شخص حكيم قبل القرار، وهي عادة متعقّلة.'),
  dict(f='The pause', fa='الوقفة', b='The moment between the thought and the word, where prudence lives.', ba='اللحظة بين الفكرة والكلمة، وفيها يسكن التعقّل.'),
 ],
 game=dict(mode='match', pairs=[
   dict(a='Someone says something hurtful', aa='قال أحدهم كلاماً مؤذياً', b='Pause and think ten times before replying', ba='توقّفي وفكّري عشر مرات قبل الرد'),
   dict(a='You are not sure about your homework', aa='لستِ متأكدة من واجبك', b='Consult someone who can help you', ba='استشيري من يستطيع مساعدتك'),
   dict(a='You finish your snack at recess', aa='أنهيتِ وجبتك في الفسحة', b='Throw the wrapper in the bin', ba='ارمي الغلاف في سلة المهملات'),
   dict(a='It is a school night', aa='ليلة يوم دراسي', b='Decide a wake-up time and sleep early', ba='حدّدي وقت الاستيقاظ وناما مبكراً'),
   dict(a='You are packing your bag', aa='تجهّزين حقيبتك', b='Check what today’s lessons actually need', ba='تفقّدي ما تحتاجينه لدروس اليوم'),
   dict(a='A new app looks fun', aa='تطبيق جديد يبدو ممتعاً', b='Ask whether it is safe and useful first', ba='اسألي أولاً: هل هو آمن ومفيد؟'),
 ]),
 quiz=[
  dict(q='A value is defined as:', a='تُعرَّف القيمة بأنها:',
       o=['The good intrinsically found in every being and every action flowing from it','A price written on a label','A rule made by a school','A feeling that comes and goes'], c=0),
  dict(q='“Intrinsically” means the good is:', a='كلمة «جوهرياً» تعني أن الخير:',
       o=['Added from outside','Already inside the thing itself','Only in expensive things','Impossible to find'], c=1),
  dict(q='Prudence helps a person to:', a='التعقّل يساعد الإنسان على أن:',
       o=['Avoid all decisions','Correctly measure the appropriate amount of value to show','Always say yes','Copy what others do'], c=1),
  dict(q='Prudence is mainly about doing the right good:', a='التعقّل أساساً هو فعل الخير الصحيح:',
       o=['In the right amount, at the right time','As loudly as possible','Only when watched','Only for friends'], c=0),
  dict(q='The saying “Bago mo sabihin, sampung beses mo munang isipin” means:', a='معنى المثل الفلبيني:',
       o=['Speak first, think later','Before you say it, think about it ten times first','Never speak at all','Say it ten times'], c=1),
  dict(q='Which of these is a mundane decision from the lesson?', a='أي مما يلي قرار يومي ورد في الدرس؟',
       o=['What time should I wake up','Which country to live in','What career to choose','Which house to buy'], c=0),
  dict(q='“Who will I consult regarding my homework?” shows the prudent habit of:', a='«من أستشير في واجبي؟» تُظهر عادة متعقّلة هي:',
       o=['Asking for guidance before deciding','Copying an answer','Ignoring the work','Guessing quickly'], c=0),
  dict(q='Why does the lesson use small everyday choices as examples?', a='لماذا يستخدم الدرس اختيارات يومية صغيرة كأمثلة؟',
       o=['Because prudence is built in small ordinary choices','Because big decisions do not matter','Because they are easy to forget','Because they have no value'], c=0),
  dict(q='A friend is generous with money. Prudence would help them decide:', a='صديق كريم بماله، التعقّل يساعده أن يقرر:',
       o=['How much to give and when','Never to give anything','To give everything at once','To hide the money'], c=0),
  dict(q='True or False: every action that flows from a being carries value.', a='صح أم خطأ: كل فعل ينبع من الكائن يحمل قيمة.',
       o=['True','False'], c=0),
 ]))
