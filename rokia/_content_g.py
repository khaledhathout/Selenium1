# -*- coding: utf-8 -*-
PAGES = []

# ─────────────────────────── 14 · FIGURES OF SPEECH ───────────────────────────
FIGS = [
 ('Simile', 'تشبيه', 'Compares two unlike things using "like" or "as".', 'My older brother is a night owl.', False,
  'يشبّه شيئين مختلفين باستخدام "like" أو "as".', 'أخي الأكبر بومة ليلية (يسهر كالبومة).'),
 ('Metaphor', 'استعارة', 'Says one thing IS another, without "like" or "as".', 'A poem is a seagull.', False,
  'يقول إن شيئاً هو شيء آخر مباشرة، بدون "like" أو "as".', 'القصيدة نورس.'),
 ('Personification', 'تشخيص', 'Gives human actions or feelings to something that is not human.', 'The autumn leaves danced across the playground.', False,
  'يمنح صفات أو أفعالاً بشرية لشيء غير بشري.', 'رقصت أوراق الخريف عبر الملعب.'),
 ('Hyperbole', 'مبالغة', 'A huge exaggeration, not meant to be taken literally.', 'My backpack weighs a ton.', False,
  'مبالغة كبيرة لا تُفهم حرفياً.', 'حقيبتي تزن طناً.'),
 ('Alliteration', 'جناس استهلالي', 'The same consonant sound repeats at the start of nearby words.', 'Wild wolves wait for the winter wind.', True,
  'تكرار نفس الصوت الساكن في بداية كلمات متجاورة.', 'تتكرر الـW في بداية كل كلمة.'),
 ('Assonance', 'جناس صوتي (حروف علة)', 'The same vowel sound repeats inside nearby words.', 'The gold stroller rolled past the door.', True,
  'تكرار نفس صوت حرف العلة داخل كلمات متجاورة.', 'يتكرر صوت الـ"o" الطويل.'),
 ('Consonance', 'جناس صوتي (حروف ساكنة)', 'The same consonant sound repeats inside or at the end of nearby words, not just at the start.', 'She wishes for a dish of fresh fish.', True,
  'تكرار نفس الصوت الساكن داخل الكلمات أو في نهايتها، لا في البداية فقط.', 'يتكرر صوت الـ"sh" في كل كلمة تقريباً.'),
]
PAGES.append(dict(
 file='14-figures-of-speech.html',
 title='Figures of Speech',
 eyebrow='English 7',
 palette=['#a6357e','#7c2760','#f9e5f0','#1f7a5c','#dcf3e9',
          '#e07eb8','#f0b3d8','#3a1729','#4fc99a','#0d3225'],
 blurb='Sound and comparison can say what a plain sentence cannot. Learn to hear the difference.',
 blurb_ar='الصوت والتشبيه يقولان ما لا تقوله الجملة العادية. تعلّمي أن تميّزي الفرق.',
 learn_h='Seven figures of speech',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Figure cards',
 cards_p='Say the meaning out loud, then flip the card to check.',
 cards_ar='قولي المعنى بصوت عالٍ ثم اقلبي البطاقة للتأكد.',
 play_h='Match each example to its figure of speech',
 play_p='Tap an example on the left, then tap its figure of speech on the right.',
 play_ar='اضغطي على المثال في اليسار ثم على نوعه في اليمين.',
 parts=[
  dict(n='1', t='Comparing things: simile and metaphor', ta='التشبيه: مباشر وضمني',
    html='<p>Two figures of speech compare one thing to another, but in different ways.</p>'
         '<h4>Simile</h4><p>A <b>simile</b> compares two unlike things using the words <b>“like”</b> or <b>“as”</b>.</p>'
         '<p><i>“My older brother is a night owl.”</i> Wait — that has no “like” or “as”, so look again: it is really saying he acts <i>like</i> a night owl. Compare it with a true simile: <i>“He is as quiet as a mouse.”</i></p>'
         '<h4>Metaphor</h4><p>A <b>metaphor</b> says one thing simply <b>IS</b> another — no “like”, no “as”.</p>'
         '<p><i>“A poem is a seagull.”</i> The poem is not compared to a seagull, it is called one outright.</p>'
         '<div class="hint"><p><b>The test:</b> if you can find “like” or “as” doing the comparing, it is a simile. If the sentence just declares one thing to be another, it is a metaphor.</p></div>',
    gloss='<p><b>التشبيه (Simile)</b> يقارن بين شيئين مختلفين باستخدام "like" أو "as"، مثل «هو هادئ كالفأر» (as quiet as a mouse).</p>'
          '<p><b>الاستعارة (Metaphor)</b> تقول إن الشيء هو شيء آخر مباشرة بدون أداة تشبيه، مثل «القصيدة نورس» (A poem is a seagull).</p>'
          '<p><b>اختبار سريع:</b> لو وجدتِ "like" أو "as" فهو تشبيه، ولو أُعلن أن الشيء هو شيء آخر مباشرة فهي استعارة.</p>'),
  dict(n='2', t='Human feelings for non-human things: personification', ta='التشخيص',
    html='<p><b>Personification</b> gives human actions, feelings, or behaviour to something that is not human — an object, an animal, an idea, even the weather.</p>'
         '<p><i>“The autumn leaves danced across the playground in the breeze.”</i> Leaves cannot dance — only people dance. That human action, given to the leaves, is personification.</p>'
         '<p><i>“The wind whistled a spooky tune through the cracked window.”</i> Wind cannot whistle a tune on purpose — a person can.</p>',
    gloss='<p><b>التشخيص (Personification)</b> يمنح صفات أو أفعالاً بشرية لشيء غير بشري — جماد أو حيوان أو فكرة أو حتى الطقس.</p>'
          '<p>«رقصت أوراق الخريف عبر الملعب في النسيم» — الأوراق لا ترقص، الرقص فعل بشري مُنح للأوراق، وهذا هو التشخيص.</p>'
          '<p>«صفّرت الريح لحناً مخيفاً عبر النافذة المتصدعة» — الريح لا تصفّر لحناً بقصد، الإنسان هو من يفعل ذلك.</p>'),
  dict(n='3', t='Saying too much on purpose: hyperbole', ta='المبالغة',
    html='<p>A <b>hyperbole</b> is a huge exaggeration. Nobody expects you to take it literally — it is used to show strong feeling.</p>'
         '<p><i>“My backpack weighs a ton with all these textbooks inside.”</i> It does not really weigh 1,000 kilograms — it just feels very heavy.</p>'
         '<p><i>“I am so exhausted I could sleep for a hundred years.”</i> Nobody sleeps a hundred years. The exaggeration shows just how tired the speaker is.</p>'
         '<div class="hint"><p>Hyperbole and metaphor can look similar. Ask: is this physically impossible and clearly exaggerated for effect? Then it is hyperbole.</p></div>',
    gloss='<p><b>المبالغة (Hyperbole)</b> تضخيم كبير لا يُقصد به المعنى الحرفي، بل التعبير عن شعور قوي.</p>'
          '<p>«حقيبتي تزن طناً بكل هذه الكتب» — لا تزن حقاً طناً، لكنها تبدو ثقيلة جداً.</p>'
          '<p>«أنا متعبة جداً لدرجة أنني قد أنام مئة عام» — لا أحد ينام مئة عام، لكن المبالغة تُظهر شدة التعب.</p>'
          '<p><b>الفرق عن الاستعارة:</b> إذا كان الأمر مستحيلاً فيزيائياً وواضح أنه مبالغة، فهو هايبربول.</p>'),
  dict(n='4', t='Playing with sound: alliteration, assonance, consonance', ta='الجناس الصوتي بأنواعه',
    html='<p>These three figures of speech are about <b>repeated sounds</b>, not meaning. Read each example aloud — you have to hear it, not just see it.</p>'
         '<h4>Alliteration</h4><p>The same <b>consonant sound</b> repeats at the <b>start</b> of nearby words.</p>'
         '<p><i>“Wild wolves wait for the winter wind.”</i> — five words start with the W sound.</p>'
         '<h4>Assonance</h4><p>The same <b>vowel sound</b> repeats <b>inside</b> nearby words, no matter where each word starts.</p>'
         '<p><i>“The gold stroller rolled past the door.”</i> — listen for the long “o” sound repeating inside gold, stroller, rolled, door.</p>'
         '<h4>Consonance</h4><p>The same <b>consonant sound</b> repeats <b>inside or at the end</b> of nearby words — the sound is not limited to the start, which is what separates it from alliteration.</p>'
         '<p><i>“She wishes for a dish of fresh fish.”</i> — the “sh” sound repeats in wishes, dish, fresh, fish.</p>'
         '<div class="hint"><p><b>Say it out loud.</b> Alliteration is the easy one: same sound, first letters, in a row. Assonance is vowels, consonance is consonants, and both can hide in the middle of a word.</p></div>',
    gloss='<p>هذه الثلاثة عن <b>تكرار الأصوات</b> لا المعنى — اقرئي المثال بصوت عالٍ لتسمعيه.</p>'
          '<p><b>الجناس الاستهلالي (Alliteration):</b> تكرار نفس الصوت الساكن في <b>بداية</b> كلمات متجاورة، مثل «Wild wolves wait for the winter wind» حيث تبدأ خمس كلمات بصوت الـW.</p>'
          '<p><b>جناس حروف العلة (Assonance):</b> تكرار نفس صوت حرف العلة <b>داخل</b> الكلمات، مثل تكرار صوت الـ"o" في «gold, stroller, rolled, door».</p>'
          '<p><b>جناس الحروف الساكنة (Consonance):</b> تكرار نفس الصوت الساكن داخل الكلمة أو في آخرها لا في بدايتها فقط، مثل صوت "sh" في «wishes, dish, fresh, fish».</p>'),
 ],
 cards=[dict(f=fx[0], fa=fx[1], b=fx[2] + ' Example: “' + fx[3] + '”', ba=fx[5] + ' مثال: «' + fx[6] + '»') for fx in FIGS],
 game=dict(mode='match', pairs=[dict(a=fx[3], aa='', b=fx[0], ba=fx[1]) for fx in FIGS]),
 quiz=[
  dict(q='A simile compares two things using which words?', a='التشبيه يقارن بين شيئين باستخدام أي كلمات؟',
       o=['“Like” or “as”','“Is” or “are”','“And” or “but”','No comparing words at all'], c=0),
  dict(q='“A poem is a seagull.” This sentence is a:', a='«القصيدة نورس». هذه الجملة:', o=['Simile','Metaphor','Hyperbole','Alliteration'], c=1),
  dict(q='Giving human actions or feelings to a non-human thing is called:', a='منح صفات بشرية لشيء غير بشري يسمى:',
       o=['Personification','Assonance','Consonance','Simile'], c=0),
  dict(q='“The autumn leaves danced across the playground.” This is an example of:', a='«رقصت أوراق الخريف عبر الملعب» مثال على:',
       o=['Hyperbole','Personification','Alliteration','Metaphor'], c=1),
  dict(q='A huge exaggeration that is not meant literally is called:', a='المبالغة الكبيرة التي لا تُقصد حرفياً تسمى:',
       o=['Hyperbole','Simile','Consonance','Personification'], c=0),
  dict(q='“My backpack weighs a ton.” This sentence is a:', a='«حقيبتي تزن طناً». هذه الجملة:', o=['Metaphor','Simile','Hyperbole','Assonance'], c=2),
  dict(q='The same consonant sound repeating at the START of nearby words is:', a='تكرار نفس الصوت الساكن في بداية كلمات متجاورة يسمى:',
       o=['Assonance','Alliteration','Consonance','Metaphor'], c=1),
  dict(q='“Wild wolves wait for the winter wind.” This is an example of:', a='«Wild wolves wait for the winter wind» مثال على:',
       o=['Consonance','Assonance','Alliteration','Hyperbole'], c=2),
  dict(q='The same VOWEL sound repeating inside nearby words is called:', a='تكرار صوت حرف العلة نفسه داخل كلمات متجاورة يسمى:',
       o=['Assonance','Alliteration','Consonance','Simile'], c=0),
  dict(q='“The gold stroller rolled past the door.” This repeats which kind of sound?', a='«The gold stroller rolled past the door» يكرر أي نوع صوت؟',
       o=['A consonant at the start of each word','A vowel sound inside the words','A whole rhyming word','No repeated sound'], c=1),
  dict(q='The same consonant sound repeating INSIDE or at the END of nearby words is:', a='تكرار الصوت الساكن نفسه داخل الكلمات أو في نهايتها يسمى:',
       o=['Alliteration','Assonance','Consonance','Metaphor'], c=2),
  dict(q='“She wishes for a dish of fresh fish.” This is an example of:', a='«She wishes for a dish of fresh fish» مثال على:',
       o=['Alliteration','Consonance','Assonance','Hyperbole'], c=1),
  dict(q='What is the main difference between alliteration and consonance?', a='ما الفرق الأساسي بين الجناس الاستهلالي والجناس الساكن؟',
       o=['Alliteration is only at the start of words; consonance can be anywhere in the word','They are exactly the same thing','Consonance uses vowels only','Alliteration only happens with numbers'], c=0),
  dict(q='“He is as quiet as a mouse.” This sentence is a:', a='«هو هادئ كالفأر». هذه الجملة:', o=['Metaphor','Simile','Personification','Consonance'], c=1),
 ]))

# ─────────────────────────── 15 · ANGLE PAIRS IN A POLYGON ───────────────────────────
PAGES.append(dict(
 file='15-angle-pairs.html',
 title='Angle Pairs in a Polygon',
 eyebrow='Math 7 · Unit 1',
 palette=['#b5651d','#8a4813','#fbe9d8','#1f6f8a','#dcf0f4',
          '#e8a865','#f3cd9e','#3a2410','#5fb8d4','#0d2e38'],
 blurb='Stretch one side of a shape and a brand-new angle appears outside it. It always plays by the same rule.',
 blurb_ar='مدّي ضلعاً واحداً من الشكل، وتظهر زاوية جديدة خارجه. وهي دائماً تلتزم بالقاعدة نفسها.',
 learn_h='Exterior angles and their partners',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Angle cards',
 cards_p='Work out the answer in your head first, then flip the card to check.',
 cards_ar='احسبي الإجابة في ذهنك أولاً ثم اقلبي البطاقة.',
 play_h='Find the missing angle',
 play_p='Choose the correct adjacent interior angle for each exterior angle.',
 play_ar='اختاري الزاوية الداخلية المجاورة الصحيحة لكل زاوية خارجية.',
 parts=[
  dict(n='1', t='Extending a side of a polygon', ta='مدّ ضلع من الشكل',
    html='<p>When one side of a polygon is extended in one direction, past a corner, a new angle is formed <b>outside</b> the shape. That new angle is called an <b>exterior angle</b> of the polygon.</p>'
         '<p>The angle already inside the shape, right next to it, is the <b>interior angle</b>. The two sit side by side, sharing one side of the shape between them — like two doors on the same hinge, one swinging in and one swinging out.</p>'
         '<div class="hint"><p><b>Take note:</b> “angles of a polygon” usually means the interior angles — the ones already inside the shape.</p></div>',
    gloss='<p>عندما يُمدَّ ضلع من أضلاع الشكل في اتجاه واحد بعد الزاوية، تتشكل زاوية جديدة <b>خارج</b> الشكل تسمى <b>الزاوية الخارجية</b>.</p>'
          '<p>والزاوية الموجودة أصلاً داخل الشكل، بجانبها مباشرة، تسمى <b>الزاوية الداخلية</b>. الاثنتان تجلسان جنباً إلى جنب وتتشاركان ضلعاً واحداً بينهما.</p>'
          '<p><b>ملاحظة:</b> «زوايا الشكل» تعني عادة الزوايا الداخلية الموجودة أصلاً بداخله.</p>'),
  dict(n='2', t='The rule: they always add to 180°', ta='القاعدة: مجموعهما دائماً ١٨٠°',
    html='<p>Measure any exterior angle and the interior angle right next to it, and add them together. The answer is always the same.</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Exterior angle</th><th>Adjacent interior angle</th><th>Sum</th></tr>'
         '<tr><td>60°</td><td>120°</td><td>60 + 120 = 180°</td></tr>'
         '<tr><td>32°</td><td>148°</td><td>32 + 148 = 180°</td></tr>'
         '<tr><td>70°</td><td>110°</td><td>70 + 110 = 180°</td></tr></table></div>'
         '<p><b>The sum of the measures of an exterior angle of the polygon and its adjacent interior angle is always 180°.</b></p>'
         '<div class="hint"><p><b>Why it works:</b> the exterior angle and the interior angle sit on a straight line — the extended side. Angles on a straight line always add up to 180°. This is true for every polygon: a triangle, a square, or a shape with a hundred sides.</p></div>',
    gloss='<p>قيسي أي زاوية خارجية والزاوية الداخلية المجاورة لها، واجمعيهما — النتيجة دائماً واحدة: ١٨٠°.</p>'
          '<p>مثلاً: ٦٠ + ١٢٠ = ١٨٠. و٣٢ + ١٤٨ = ١٨٠. و٧٠ + ١١٠ = ١٨٠.</p>'
          '<p><b>مجموع قياسي الزاوية الخارجية للشكل والزاوية الداخلية المجاورة لها يساوي ١٨٠° دائماً.</b></p>'
          '<p><b>لماذا؟</b> لأن الزاويتين تقعان على خط مستقيم واحد وهو الضلع الممدود، والزوايا على الخط المستقيم مجموعها دائماً ١٨٠°. وهذا صحيح لأي شكل: مثلث أو مربع أو حتى شكل بمئة ضلع.</p>'),
  dict(n='3', t='Finding a missing angle', ta='إيجاد الزاوية المفقودة',
    html='<p>Because the two angles always add to 180°, if you know one you can always find the other. Just subtract from 180°.</p>'
         '<h4>Worked example 1</h4><p>The exterior angle is 60°. What is the adjacent interior angle?</p>'
         '<p>180° − 60° = <b>120°</b></p>'
         '<h4>Worked example 2</h4><p>The exterior angle is 32°. What is the adjacent interior angle?</p>'
         '<p>180° − 32° = <b>148°</b></p>'
         '<div class="hint"><p><b>Check yourself:</b> add your two numbers back together. If they equal 180°, your answer is right.</p></div>',
    gloss='<p>بما أن مجموع الزاويتين دائماً ١٨٠°، إذا عرفتِ إحداهما تجدين الأخرى بالطرح من ١٨٠°.</p>'
          '<p><b>مثال ١:</b> الزاوية الخارجية ٦٠°، فالداخلية المجاورة = ١٨٠ − ٦٠ = <b>١٢٠°</b>.</p>'
          '<p><b>مثال ٢:</b> الزاوية الخارجية ٣٢°، فالداخلية المجاورة = ١٨٠ − ٣٢ = <b>١٤٨°</b>.</p>'
          '<p><b>تحققي من نفسك:</b> اجمعي الرقمين معاً، فإن ساوى الناتج ١٨٠° فإجابتك صحيحة.</p>'),
  dict(n='4', t='Other angle pairs to know', ta='أزواج زوايا أخرى مهمة',
    html='<p>Three more rules about angle pairs, used together with the exterior-interior rule:</p>'
         '<ul><li><b>Linear pair:</b> angles that form a straight line together are <b>supplementary</b> — they add up to 180°. This is exactly why the exterior and interior angle rule works.</li>'
         '<li><b>Supplementary angles:</b> if the sum of the measures of two angles is 180°, then the angles are supplementary — even if they are not next to each other on a line.</li>'
         '<li><b>Complementary angles:</b> if the sum of the measures of two angles is 90°, then the angles are complementary.</li>'
         '<li><b>Congruent angles:</b> if two angles have equal measures, then the angles are congruent.</li></ul>'
         '<div class="hint"><p><b>Keep them straight:</b> supplementary → 180° (think “straight line”). Complementary → 90° (think “corner of a square”). Congruent → equal, no adding at all.</p></div>',
    gloss='<p>ثلاث قواعد إضافية عن أزواج الزوايا تُستخدم مع قاعدة الزاوية الداخلية والخارجية:</p>'
          '<p><b>الزوج الخطي:</b> الزاويتان اللتان تُشكّلان معاً خطاً مستقيماً تكونان <b>متتامتين</b> (مجموعهما ١٨٠°)، وهذا بالضبط سبب صحة قاعدة الزاوية الداخلية والخارجية.</p>'
          '<p><b>الزوايا المتتامة:</b> إذا كان مجموع قياسي زاويتين ١٨٠° فهما متتامتان، حتى لو لم تكونا متجاورتين على خط.</p>'
          '<p><b>الزوايا المتكاملة:</b> إذا كان مجموع قياسي زاويتين ٩٠° فهما متكاملتان.</p>'
          '<p><b>الزوايا المتطابقة:</b> إذا تساوى قياس زاويتين فهما متطابقتان.</p>'),
 ],
 cards=[
  dict(f='Exterior angle', fa='الزاوية الخارجية', b='The new angle formed outside a polygon when one side is extended.', ba='الزاوية الجديدة التي تتشكل خارج الشكل عند مدّ أحد أضلاعه.'),
  dict(f='Interior angle', fa='الزاوية الداخلية', b='An angle already inside the polygon.', ba='زاوية موجودة أصلاً داخل الشكل.'),
  dict(f='Exterior angle + adjacent interior angle', fa='مجموع الزاويتين المتجاورتين', b='Always equals 180°.', ba='يساوي دائماً ١٨٠°.'),
  dict(f='Exterior angle is 60°', fa='الزاوية الخارجية ٦٠°', b='The adjacent interior angle is 120° (180 − 60).', ba='الزاوية الداخلية المجاورة = ١٢٠° (١٨٠ − ٦٠).'),
  dict(f='Exterior angle is 32°', fa='الزاوية الخارجية ٣٢°', b='The adjacent interior angle is 148° (180 − 32).', ba='الزاوية الداخلية المجاورة = ١٤٨° (١٨٠ − ٣٢).'),
  dict(f='Linear pair', fa='الزوج الخطي', b='Angles that together form a straight line — they are supplementary.', ba='زاويتان تشكلان معاً خطاً مستقيماً، وهما متتامتان.'),
  dict(f='Supplementary angles', fa='الزوايا المتتامة', b='Two angles whose measures add up to 180°.', ba='زاويتان مجموع قياسيهما ١٨٠°.'),
  dict(f='Complementary angles', fa='الزوايا المتكاملة', b='Two angles whose measures add up to 90°.', ba='زاويتان مجموع قياسيهما ٩٠°.'),
  dict(f='Congruent angles', fa='الزوايا المتطابقة', b='Two angles that have equal measures.', ba='زاويتان لهما نفس القياس.'),
 ],
 game=dict(mode='match', pairs=[
   dict(a='Exterior 60°', aa='خارجية ٦٠°', b='Interior 120°', ba='داخلية ١٢٠°'),
   dict(a='Exterior 32°', aa='خارجية ٣٢°', b='Interior 148°', ba='داخلية ١٤٨°'),
   dict(a='Exterior 70°', aa='خارجية ٧٠°', b='Interior 110°', ba='داخلية ١١٠°'),
   dict(a='Exterior 90°', aa='خارجية ٩٠°', b='Interior 90°', ba='داخلية ٩٠°'),
   dict(a='Exterior 45°', aa='خارجية ٤٥°', b='Interior 135°', ba='داخلية ١٣٥°'),
   dict(a='Exterior 100°', aa='خارجية ١٠٠°', b='Interior 80°', ba='داخلية ٨٠°'),
 ]),
 quiz=[
  dict(q='When one side of a polygon is extended, the new angle formed outside the shape is called the:', a='عند مدّ ضلع من الشكل، الزاوية الجديدة خارجه تسمى:',
       o=['Interior angle','Exterior angle','Central angle','Right angle'], c=1),
  dict(q='The sum of an exterior angle of a polygon and its adjacent interior angle is:', a='مجموع الزاوية الخارجية والداخلية المجاورة لها:',
       o=['90°','180°','360°','45°'], c=1),
  dict(q='If an exterior angle is 60°, its adjacent interior angle is:', a='إذا كانت الزاوية الخارجية ٦٠°، فالداخلية المجاورة:',
       o=['60°','90°','120°','180°'], c=2),
  dict(q='If an exterior angle is 32°, its adjacent interior angle is:', a='إذا كانت الزاوية الخارجية ٣٢°، فالداخلية المجاورة:',
       o=['58°','138°','148°','168°'], c=2),
  dict(q='If an interior angle is 110°, its adjacent exterior angle is:', a='إذا كانت الزاوية الداخلية ١١٠°، فالخارجية المجاورة:',
       o=['70°','80°','90°','110°'], c=0),
  dict(q='Angles that together form a straight line are called a:', a='الزاويتان اللتان تشكلان معاً خطاً مستقيماً تسميان:',
       o=['Right pair','Linear pair','Vertical pair','Congruent pair'], c=1),
  dict(q='If the sum of the measures of two angles is 180°, the angles are:', a='إذا كان مجموع قياسي زاويتين ١٨٠°، فهما:',
       o=['Complementary','Congruent','Supplementary','Exterior'], c=2),
  dict(q='If the sum of the measures of two angles is 90°, the angles are:', a='إذا كان مجموع قياسي زاويتين ٩٠°، فهما:',
       o=['Supplementary','Complementary','Congruent','Adjacent only'], c=1),
  dict(q='If two angles have equal measures, the angles are:', a='إذا تساوى قياس زاويتين، فهما:',
       o=['Supplementary','Complementary','Congruent','Exterior'], c=2),
  dict(q='Why does an exterior angle and its adjacent interior angle always add to 180°?', a='لماذا تجمع الزاوية الخارجية والداخلية المجاورة دائماً إلى ١٨٠°؟',
       o=['Because they sit on a straight line, and straight-line angles add to 180°','Because all polygons have 180 sides','Because someone decided the rule by chance','Because interior angles are always bigger'], c=0),
  dict(q='“Angles of a polygon” usually refers to which angles?', a='«زوايا الشكل» تشير عادة إلى أي زوايا؟',
       o=['Exterior angles','Interior angles','Both equally, with no difference','Neither — it refers to the sides'], c=1),
  dict(q='Is the 180° rule for exterior and adjacent interior angles true for every polygon?', a='هل قاعدة الـ١٨٠° صحيحة لكل الأشكال؟',
       o=['Yes, for every polygon no matter how many sides','Only for triangles','Only for four-sided shapes','No, it only works sometimes'], c=0),
 ]))
