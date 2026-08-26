# -*- coding: utf-8 -*-
PAGES = []

# ─────────────────────────── 12 · WORD 2016 ───────────────────────────
PARTS10 = [
 ('Quick Access Toolbar', 'شريط الوصول السريع', 'Holds the buttons you use most, such as Save and Undo, whatever tab you are on.'),
 ('File name', 'اسم الملف', 'Shows the name of the document you are working on.'),
 ('Microsoft account', 'حساب مايكروسوفت', 'Shows who is signed in and lets you reach your files anywhere.'),
 ('Ribbon display options', 'خيارات عرض الشريط', 'Let you hide or show the Ribbon to make more room for the page.'),
 ('Ribbon', 'الشريط', 'The wide band of tabs and commands: Home, Insert, Design, Layout and more.'),
 ('Rulers', 'المسطرتان', 'Show the width and height of the page so you can set margins and tabs.'),
 ('Insertion point', 'مؤشر الكتابة', 'The blinking line that shows where your next letter will appear.'),
 ('Document', 'المستند', 'The white page itself, where your text and pictures go.'),
 ('Vertical scroll bar', 'شريط التمرير الرأسي', 'Moves you up and down through a long document.'),
 ('Status bar', 'شريط الحالة', 'Shows the page number, word count and the view and zoom controls.'),
]
PAGES.append(dict(
 file='12-word-2016.html',
 title='Getting Started with Word',
 eyebrow='Computer · Unit 1, Lesson 1',
 palette=['#1a5fb4','#134a8e','#e2ecf9','#c0392b','#fae3df',
          '#6aa6ee','#a3c9f5','#102437','#f07a68','#3a1a16'],
 blurb='Productivity software turns your ideas into documents. Learn every part of the Word window.',
 blurb_ar='برامج الإنتاجية تحوّل أفكارك إلى مستندات. تعرّفي على كل جزء من نافذة وورد.',
 learn_h='Word 2016 from the beginning',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Interface cards',
 cards_p='Say what each part does, then flip the card to check.',
 cards_ar='قولي وظيفة كل جزء ثم اقلبي البطاقة للتأكد.',
 play_h='Match each part of the window to its job',
 play_p='Tap a part on the left, then tap what it does on the right.',
 play_ar='اضغطي على الجزء في اليسار ثم على وظيفته في اليمين.',
 parts=[
  dict(n='1', t='Productivity software', ta='برامج الإنتاجية',
    html='<p>In some of our school activities we create meaningful information using <b>productivity software</b>. For example:</p>'
         '<ul><li>English essays</li><li>Maths data and graphs</li><li>Science investigation presentations</li></ul>'
         '<p>Productivity software is also called <b>personal</b> or <b>office productivity software</b>. It is an application we use to produce documents, presentations, spreadsheets, charts, and graphs.</p>'
         '<p><b>Microsoft Office</b> has constantly been one of the leading office suites. The version in this lesson is <b>2016</b>, and it runs on Windows 10.</p>',
    gloss='<p>في بعض أنشطتنا المدرسية ننتج معلومات ذات معنى باستخدام <b>برامج الإنتاجية</b>، مثل: مقالات الإنجليزية، وبيانات ورسوم الرياضيات، وعروض البحث العلمي.</p>'
          '<p>وتسمى أيضاً <b>برامج الإنتاجية الشخصية أو المكتبية</b>، وهي تطبيقات نستخدمها لإنتاج المستندات والعروض والجداول والمخططات والرسوم البيانية.</p>'
          '<p>و<b>مايكروسوفت أوفيس</b> من أبرز الحزم المكتبية دائماً، ونسخة هذا الدرس هي <b>2016</b> وتعمل على ويندوز 10.</p>'),
  dict(n='2', t='What Word 2016 is for', ta='فيمَ يُستخدم وورد 2016',
    html='<p><b>Word 2016</b> is a <b>word processing</b> application for creating texts and graphics.</p>'
         '<p>Common outputs are:</p><ul><li>Brochures</li><li>Posters</li><li>Letters</li><li>Reports</li></ul>'
         '<div class="hint"><p>A word processor is not just a typewriter on a screen: it lets you change your mind. You can edit, move, restyle and reprint the same text as often as you like.</p></div>',
    gloss='<p><b>وورد 2016</b> تطبيق <b>معالجة نصوص</b> لإنشاء النصوص والرسوم.</p>'
          '<p>ومن مخرجاته الشائعة: المطويات، والملصقات، والرسائل، والتقارير.</p>'
          '<p>ومعالج النصوص ليس آلة كاتبة على الشاشة، بل يتيح لكِ تغيير رأيك: تعديل النص ونقله وإعادة تنسيقه وطباعته مرات كثيرة.</p>'),
  dict(n='3', t='Two new features in Word 2016', ta='ميزتان جديدتان في وورد 2016',
    html='<h4>1 · Tell Me</h4>'
         '<p>The <b>Tell Me</b> search bar is a versatile tool. You type what you want to do, and it finds the function you need instead of making you hunt through the tabs.</p>'
         '<h4>2 · Smart Lookup</h4>'
         '<p><b>Smart Lookup</b> is designed to deliver useful information. Select a word, and it brings definitions and web results into a pane beside your document.</p>',
    gloss='<p><b>١ · Tell Me</b> — شريط بحث متعدد الاستخدامات: تكتبين ما تريدين فعله فيجد لكِ الأمر المطلوب بدل البحث في التبويبات.</p>'
          '<p><b>٢ · Smart Lookup</b> — مصمم ليقدّم معلومات مفيدة: تحدّدين كلمة فيعرض تعريفها ونتائج الويب في لوحة بجانب المستند.</p>'),
  dict(n='4', t='The Word 2016 interface', ta='واجهة وورد 2016',
    html='<p>To begin, choose <b>Blank Document</b> to open. Then look around the window — these ten parts are the map of it:</p>'
         '<div class="scroll"><table class="tbl"><tr><th>#</th><th>Part</th><th>What it does</th></tr>' +
         ''.join('<tr><td>%d</td><td>%s<div class="ar l">%s</div></td><td>%s</td></tr>' % (i+1, p[0], p[1], p[2]) for i, p in enumerate(PARTS10)) +
         '</table></div>',
    gloss='<p>للبدء اختاري <b>Blank Document</b> لفتح مستند فارغ، ثم تعرّفي على أجزاء النافذة العشرة: شريط الوصول السريع، واسم الملف، وحساب مايكروسوفت، وخيارات عرض الشريط، والشريط، والمسطرتان، ومؤشر الكتابة، والمستند، وشريط التمرير الرأسي، وشريط الحالة.</p>'),
 ],
 cards=[dict(f=p[0], fa=p[1], b=p[2], ba='') for p in PARTS10] + [
  dict(f='Productivity software', fa='برامج الإنتاجية', b='An application used to produce documents, presentations, spreadsheets, charts and graphs.', ba='تطبيق يُستخدم لإنتاج المستندات والعروض والجداول والمخططات والرسوم.'),
  dict(f='Word processing', fa='معالجة النصوص', b='Creating and editing texts and graphics on a computer.', ba='إنشاء النصوص والرسوم وتحريرها على الحاسوب.'),
  dict(f='Tell Me', fa='شريط Tell Me', b='A search bar that finds the function you need.', ba='شريط بحث يجد لكِ الأمر الذي تحتاجينه.'),
  dict(f='Smart Lookup', fa='Smart Lookup', b='A feature designed to deliver useful information about a selected word.', ba='ميزة تقدّم معلومات مفيدة عن الكلمة المحددة.'),
 ],
 game=dict(mode='match', pairs=[
   dict(a='Ribbon', aa='الشريط', b='The band of tabs and commands', ba='شريط التبويبات والأوامر'),
   dict(a='Insertion point', aa='مؤشر الكتابة', b='The blinking line where the next letter appears', ba='الخط الوامض حيث يظهر الحرف التالي'),
   dict(a='Status bar', aa='شريط الحالة', b='Page number, word count, view and zoom', ba='رقم الصفحة وعدد الكلمات والعرض والتكبير'),
   dict(a='Quick Access Toolbar', aa='شريط الوصول السريع', b='The buttons you use most, such as Save', ba='الأزرار الأكثر استخداماً مثل الحفظ'),
   dict(a='Rulers', aa='المسطرتان', b='Show page width and height for margins', ba='تُظهران عرض الصفحة وارتفاعها للهوامش'),
   dict(a='Vertical scroll bar', aa='شريط التمرير', b='Moves you up and down the document', ba='ينقلك أعلى وأسفل المستند'),
   dict(a='Tell Me', aa='Tell Me', b='Type what you want to do and it finds it', ba='اكتبي ما تريدين فعله فيجده لكِ'),
   dict(a='Smart Lookup', aa='Smart Lookup', b='Brings useful information about a selected word', ba='يجلب معلومات مفيدة عن كلمة محددة'),
 ]),
 quiz=[
  dict(q='Productivity software is used to produce:', a='برامج الإنتاجية تُستخدم لإنتاج:',
       o=['Documents, presentations, spreadsheets, charts and graphs','Only photographs','Only games','Only music'], c=0),
  dict(q='Another name for productivity software is:', a='اسم آخر لبرامج الإنتاجية:',
       o=['Operating system','Personal or office productivity software','Antivirus','Web browser'], c=1),
  dict(q='Which of these is an example of school work made with productivity software?', a='أي مما يلي مثال على عمل مدرسي بهذه البرامج؟',
       o=['English essays','Running in PE','Singing in choir','Painting a wall'], c=0),
  dict(q='Word 2016 is best described as a:', a='أفضل وصف لوورد 2016:',
       o=['Spreadsheet application','Word processing application for creating texts and graphics','Video editor','Search engine'], c=1),
  dict(q='Which of these is NOT listed as a common output of Word?', a='أي مما يلي ليس من مخرجات وورد المذكورة؟',
       o=['Brochures','Posters','Letters and reports','Spreadsheets of formulas'], c=3),
  dict(q='The Tell Me search bar helps you:', a='شريط Tell Me يساعدك على:',
       o=['Find the function you need','Delete the document','Change the wallpaper','Turn off the computer'], c=0),
  dict(q='Smart Lookup is designed to:', a='صُمِّم Smart Lookup لـ:',
       o=['Deliver useful information','Print the page','Save the file','Count the pages'], c=0),
  dict(q='To start a new file in Word 2016 you choose:', a='لبدء ملف جديد في وورد 2016 تختارين:',
       o=['Blank Document','Print Preview','Save As','Exit'], c=0),
  dict(q='The blinking line that shows where your next letter appears is the:', a='الخط الوامض الذي يبيّن مكان الحرف التالي هو:',
       o=['Ruler','Insertion point','Status bar','Scroll bar'], c=1),
  dict(q='The wide band that holds the tabs and commands is the:', a='الشريط العريض الذي يضم التبويبات والأوامر هو:',
       o=['Ribbon','Status bar','Rulers','Document'], c=0),
  dict(q='Page number and word count are shown on the:', a='رقم الصفحة وعدد الكلمات يظهران في:',
       o=['Quick Access Toolbar','Status bar','Ribbon','Rulers'], c=1),
  dict(q='Word 2016 in this lesson runs on:', a='وورد 2016 في هذا الدرس يعمل على:',
       o=['Windows 10','Windows 95','A calculator','A smart TV only'], c=0),
 ]))

# ─────────────────────────── 13 · MEASUREMENT AND SI UNITS ───────────────────────────
SI = [
 ('Amount of substance','كمية المادة','mole','mol'),
 ('Electric current','التيار الكهربائي','ampere','A'),
 ('Length','الطول','metre','m'),
 ('Luminous intensity','شدة الإضاءة','candela','cd'),
 ('Mass','الكتلة','kilogram','kg'),
 ('Temperature','درجة الحرارة','kelvin','K'),
 ('Time','الزمن','second','s'),
]
PAGES.append(dict(
 file='13-measurement.html',
 title='Measuring the World',
 eyebrow='Science · Measurement',
 palette=['#0d7490','#095a70','#dbeef4','#c2410c','#fbe6da',
          '#4fc3e0','#8fdcf0','#08313d','#f08a55','#3a2013'],
 blurb='Seven base units, one careful eye, and two formulas that move between scales.',
 blurb_ar='سبع وحدات أساسية، وعين دقيقة، ومعادلتان تنقلان بين المقاييس.',
 learn_h='Units, reading, and converting',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Measurement cards',
 cards_p='Answer in your head first, then flip the card to check.',
 cards_ar='أجيبي في ذهنك أولاً ثم اقلبي البطاقة للتأكد.',
 play_h='Match each quantity to its SI unit',
 play_p='Tap a physical quantity on the left, then tap its unit on the right.',
 play_ar='اضغطي على الكمية الفيزيائية في اليسار ثم على وحدتها في اليمين.',
 parts=[
  dict(n='1', t='The seven SI base units', ta='وحدات النظام الدولي السبع',
    html='<p>Scientists everywhere agree on one set of units, the <b>SI units</b>, so a measurement means the same thing in every country.</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Physical quantity</th><th>SI unit</th><th>Symbol</th></tr>' +
         ''.join('<tr><td>%s<div class="ar l">%s</div></td><td>%s</td><td>%s</td></tr>' % s for s in SI) +
         '</table></div>'
         '<div class="hint"><p>Watch the capitals: units named after people take a capital symbol (A for ampere, K for kelvin), but the unit word itself stays lower case.</p></div>',
    gloss='<p>يتفق العلماء في كل مكان على مجموعة واحدة من الوحدات هي <b>وحدات النظام الدولي (SI)</b>، حتى يعني القياس الشيء نفسه في كل بلد.</p>'
          '<p>كمية المادة: مول (mol). التيار الكهربائي: أمبير (A). الطول: متر (m). شدة الإضاءة: كانديلا (cd). الكتلة: كيلوجرام (kg). درجة الحرارة: كلفن (K). الزمن: ثانية (s).</p>'
          '<p><b>انتبهي للحروف الكبيرة:</b> الوحدات المسماة بأسماء علماء يكون رمزها بحرف كبير مثل A و K، أما اسم الوحدة نفسه فيبقى بحروف صغيرة.</p>'),
  dict(n='2', t='Reading a liquid: the meniscus', ta='قراءة السائل: الهلال',
    html='<p>When you pour a liquid into a narrow cylinder, its surface is not flat. It curves.</p>'
         '<p>That <b>curvature at the surface of a liquid</b> is called the <b>meniscus</b>.</p>'
         '<h4>How to read it correctly</h4>'
         '<ol><li>Put the cylinder on a flat table — never hold it in the air.</li>'
         '<li>Bring your eye down to the same level as the liquid.</li>'
         '<li>Read the mark at the <b>bottom of the curve</b>, not at the edges.</li></ol>'
         '<div class="hint"><p>Reading from above makes the number look bigger than it is, and reading from below makes it look smaller. Only eye level tells the truth.</p></div>',
    gloss='<p>عندما تصبّين سائلاً في مخبار ضيق لا يكون سطحه مستوياً بل ينحني، ويسمى هذا <b>الانحناء عند سطح السائل</b> بـ<b>الهلال (meniscus)</b>.</p>'
          '<p><b>للقراءة الصحيحة:</b> ضعي المخبار على طاولة مستوية، واجعلي عينك في مستوى السائل نفسه، واقرئي العلامة عند <b>أسفل الانحناء</b> لا عند الحافتين.</p>'
          '<p>فالقراءة من أعلى تُظهر الرقم أكبر مما هو، ومن أسفل أصغر مما هو، ولا يصدق إلا مستوى العين.</p>'),
  dict(n='3', t='Converting temperature', ta='تحويل درجات الحرارة',
    html='<p>Two formulas move between Fahrenheit and Celsius:</p>'
         '<p style="font-size:1.1rem;font-weight:700">T<sub>F</sub> = 9/5 × T<sub>C</sub> + 32</p>'
         '<p style="font-size:1.1rem;font-weight:700">T<sub>C</sub> = 5/9 × (T<sub>F</sub> − 32)</p>'
         '<h4>Worked example</h4>'
         '<p>Change 25 °C into Fahrenheit: 9/5 × 25 = 45, then 45 + 32 = <b>77 °F</b>.</p>'
         '<p>Change 212 °F into Celsius: 212 − 32 = 180, then 5/9 × 180 = <b>100 °C</b>.</p>'
         '<div class="hint"><p><b>Order matters.</b> Going to Fahrenheit you multiply first and add last. Coming back you subtract first and multiply last.</p></div>',
    gloss='<p>معادلتان للتحويل بين الفهرنهايت والسيليزيوس:</p>'
          '<p>T<sub>F</sub> = ٩/٥ × T<sub>C</sub> + ٣٢ &nbsp;|&nbsp; T<sub>C</sub> = ٥/٩ × (T<sub>F</sub> − ٣٢)</p>'
          '<p><b>مثال:</b> ٢٥ درجة سيليزية = (٩/٥ × ٢٥) + ٣٢ = ٧٧ فهرنهايت. و٢١٢ فهرنهايت = ٥/٩ × (٢١٢ − ٣٢) = ١٠٠ سيليزية.</p>'
          '<p><b>الترتيب مهم:</b> نحو الفهرنهايت نضرب أولاً ونجمع أخيراً، وفي العودة نطرح أولاً ونضرب أخيراً.</p>'),
  dict(n='4', t='Converting mass', ta='تحويل الكتلة',
    html='<p>Pounds and kilograms measure the same thing in different systems.</p>'
         '<h4>Pounds to kilograms — divide</h4>'
         '<p>1 kg = 2.205 lbs, so: 100 lbs ÷ 2.205 = <b>45.35 kg</b>.</p>'
         '<h4>Kilograms to pounds — multiply</h4>'
         '<p>1 kg = 2.2046 lbs, so: 51 kg × 2.2046 = <b>112.4 lbs</b>.</p>'
         '<div class="hint"><p><b>Check yourself:</b> a kilogram is bigger than a pound, so the number of pounds is always the larger number. If your answer went the other way, you multiplied when you should have divided.</p></div>',
    gloss='<p>الرطل والكيلوجرام يقيسان الشيء نفسه في نظامين مختلفين.</p>'
          '<p><b>من الأرطال إلى الكيلوجرامات — نقسم:</b> ١ كجم = ٢٫٢٠٥ رطل، إذن ١٠٠ رطل ÷ ٢٫٢٠٥ = <b>٤٥٫٣٥ كجم</b>.</p>'
          '<p><b>من الكيلوجرامات إلى الأرطال — نضرب:</b> ٥١ كجم × ٢٫٢٠٤٦ = <b>١١٢٫٤ رطل</b>.</p>'
          '<p><b>تحقّقي:</b> الكيلوجرام أكبر من الرطل، فعدد الأرطال دائماً هو الأكبر. فإذا جاء العكس فقد ضربتِ بدل أن تقسمي.</p>'),
 ],
 cards=[dict(f=s[0], fa=s[1], b='SI unit: %s (%s)' % (s[2], s[3]), ba='وحدة النظام الدولي: %s رمزها %s' % (s[2], s[3])) for s in SI] + [
  dict(f='Meniscus', fa='الهلال', b='The curvature at the surface of a liquid.', ba='الانحناء عند سطح السائل.'),
  dict(f='How to read a meniscus', fa='كيف نقرأ الهلال', b='At eye level, at the bottom of the curve.', ba='في مستوى العين، وعند أسفل الانحناء.'),
  dict(f='T꜀ to Tᶠ', fa='من سيليزيوس إلى فهرنهايت', b='Multiply by 9/5, then add 32.', ba='اضربي في ٩/٥ ثم أضيفي ٣٢.'),
  dict(f='Tᶠ to T꜀', fa='من فهرنهايت إلى سيليزيوس', b='Subtract 32, then multiply by 5/9.', ba='اطرحي ٣٢ ثم اضربي في ٥/٩.'),
  dict(f='100 lbs in kilograms', fa='١٠٠ رطل بالكيلوجرام', b='100 ÷ 2.205 = 45.35 kg.', ba='١٠٠ ÷ ٢٫٢٠٥ = ٤٥٫٣٥ كجم.'),
  dict(f='51 kg in pounds', fa='٥١ كجم بالأرطال', b='51 × 2.2046 = 112.4 lbs.', ba='٥١ × ٢٫٢٠٤٦ = ١١٢٫٤ رطل.'),
 ],
 game=dict(mode='match', pairs=[dict(a=s[0], aa=s[1], b='%s (%s)' % (s[2], s[3]), ba='') for s in SI] +
   [dict(a='Meniscus', aa='الهلال', b='Curvature at the surface of a liquid', ba='انحناء سطح السائل')]),
 quiz=[
  dict(q='The SI unit of mass is the:', a='وحدة الكتلة في النظام الدولي:', o=['gram','kilogram','pound','newton'], c=1),
  dict(q='The SI unit of temperature is the:', a='وحدة درجة الحرارة في النظام الدولي:', o=['celsius','fahrenheit','kelvin','degree'], c=2),
  dict(q='The symbol for the ampere is:', a='رمز الأمبير:', o=['Am','A','a','Ap'], c=1),
  dict(q='The mole is the SI unit of:', a='المول وحدة قياس:', o=['Amount of substance','Length','Time','Mass'], c=0),
  dict(q='The candela measures:', a='الكانديلا تقيس:', o=['Electric current','Luminous intensity','Time','Length'], c=1),
  dict(q='The SI unit of time is the second, whose symbol is:', a='وحدة الزمن هي الثانية ورمزها:', o=['sec','s','S','t'], c=1),
  dict(q='The curvature at the surface of a liquid is called the:', a='الانحناء عند سطح السائل يسمى:', o=['Meniscus','Molecule','Margin','Metre'], c=0),
  dict(q='Where should you read the meniscus?', a='أين نقرأ الهلال؟',
       o=['At the top edges','At the bottom of the curve, at eye level','From above the cylinder','Anywhere on the scale'], c=1),
  dict(q='Which formula changes Celsius into Fahrenheit?', a='أي معادلة تحوّل من سيليزيوس إلى فهرنهايت؟',
       o=['TF = 9/5 × TC + 32','TC = 5/9 × (TF − 32)','TF = TC + 100','TC = TF × 2'], c=0),
  dict(q='25 °C in Fahrenheit is:', a='٢٥ درجة سيليزية بالفهرنهايت تساوي:', o=['57 °F','77 °F','97 °F','45 °F'], c=1),
  dict(q='212 °F in Celsius is:', a='٢١٢ فهرنهايت بالسيليزيوس تساوي:', o=['0 °C','50 °C','100 °C','180 °C'], c=2),
  dict(q='To change pounds into kilograms you:', a='لتحويل الأرطال إلى كيلوجرامات:',
       o=['Divide by 2.205','Multiply by 2.205','Add 32','Subtract 2.205'], c=0),
  dict(q='100 pounds is about:', a='١٠٠ رطل تساوي تقريباً:', o=['22.05 kg','45.35 kg','220.5 kg','100 kg'], c=1),
  dict(q='To change kilograms into pounds you:', a='لتحويل الكيلوجرامات إلى أرطال:',
       o=['Divide by 2.2046','Multiply by 2.2046','Add 2.2046','Subtract 32'], c=1),
 ]))
