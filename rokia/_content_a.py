# -*- coding: utf-8 -*-
PAGES = []

# ─────────────────────────── 1 · DENOTATIVE & CONNOTATIVE ───────────────────────────
PAGES.append(dict(
 file='01-word-meanings.html',
 title='Two Meanings of a Word',
 eyebrow='English · Unit 1',
 palette=['#7a4fbf','#5b3392','#efe7fb','#e0723c','#fbeadf',
          '#b590ec','#d3bcf7','#2c1f45','#f0955e','#3a2317'],
 blurb='Every word has a dictionary meaning and a feeling meaning. Learn to hear both.',
 blurb_ar='كل كلمة لها معنى في القاموس ومعنى في المشاعر. تعلّمي تسمعي الاثنين.',
 learn_h='Denotative and connotative meaning',
 learn_p='Open a part to read it. Press Listen and the English is read to you, one paragraph at a time.',
 learn_ar='افتحي أي جزء لقراءته. اضغطي «Listen» ليُقرأ لكِ بالإنجليزية فقرة فقرة.',
 cards_h='Word cards',
 cards_p='See a word, say both meanings out loud, then flip to check.',
 cards_ar='شوفي الكلمة، قولي المعنيين بصوت عالٍ، ثم اقلبي البطاقة للتأكد.',
 play_h='Dictionary meaning or feeling meaning?',
 play_p='Read each sentence. Is it telling you what the word IS, or how it FEELS?',
 play_ar='اقرئي كل جملة: هل تخبرك ما هي الكلمة (حرفي)، أم بالشعور الذي تعطيه (مجازي)؟',
 parts=[
  dict(n='1', t='Two meanings of home', ta='معنيان لكلمة «بيت»',
    html='<p>Home is where a family lives. Our parents and the elderly members are the first to teach us to be kind, nice, and polite to others. They teach us how to speak and act appropriately.</p>'
         '<p>This is why even if we grow old and start to live on our own, we always go back and remember our home as the place where good manners are taught and values are learned. Because of this, we feel love, warmth, and goodness whenever we think of home.</p>'
         '<p>The passage above shows two different meanings of the word <b>home</b>.</p>',
    gloss='<p>البيت هو المكان الذي تعيش فيه الأسرة. والوالدان وكبار السن هم أول من يعلّمنا أن نكون لطفاء ومهذبين مع الآخرين، ويعلّموننا كيف نتحدث ونتصرف بشكل مناسب.</p>'
          '<p>لهذا حتى عندما نكبر ونعيش وحدنا، نعود دائماً ونتذكر بيتنا كمكان تُعلَّم فيه الأخلاق وتُكتسب فيه القيم، فنشعر بالحب والدفء والطيبة كلما فكرنا في البيت.</p>'
          '<p>هذه الفقرة تُظهر معنيين مختلفين لكلمة <b>home</b>.</p>'),
  dict(n='2', t='Denotative meaning', ta='المعنى الحرفي (القاموسي)',
    html='<p>The first meaning of <i>home</i> is literal. It is a place or dwelling where the family lives. This kind of meaning is called <b>denotative meaning</b>.</p>'
         '<p>To find the denotative meaning of a word, you can search for its definition in an online or print dictionary.</p>'
         '<h4>Think of it like this</h4><p>Denotative = the plain, dictionary meaning. It is the same for everybody.</p>',
    gloss='<p>المعنى الأول لكلمة <i>home</i> هو المعنى الحرفي: مكان أو مسكن تعيش فيه الأسرة. هذا النوع يسمى <b>المعنى الحرفي (Denotative)</b>.</p>'
          '<p>لمعرفة المعنى الحرفي لأي كلمة، ابحثي عن تعريفها في قاموس ورقي أو إلكتروني.</p>'
          '<p><b>ببساطة:</b> المعنى الحرفي = معنى القاموس، وهو واحد لكل الناس.</p>'),
  dict(n='3', t='Connotative meaning', ta='المعنى المجازي (الشعوري)',
    html='<p>The second meaning of <i>home</i> is beyond the literal sense. When we link the word <i>home</i> with feelings of love, warmth, affection, and values, the meaning becomes <b>connotative</b>.</p>'
         '<p>The connotative meaning of a word is based on mental and emotional associations. For example, a home may bring back good memories and a sense of growth and belonging.</p>'
         '<p>So <i>home</i> is not just a place made of walls, floor, and roof — it is where a person feels loved and valued.</p>',
    gloss='<p>المعنى الثاني لكلمة <i>home</i> يتجاوز المعنى الحرفي. فعندما نربط الكلمة بمشاعر الحب والدفء والحنان والقيم يصبح المعنى <b>مجازياً (Connotative)</b>.</p>'
          '<p>المعنى المجازي يقوم على ما ترتبط به الكلمة في الذهن والمشاعر. فالبيت قد يعيد إلينا ذكريات جميلة وإحساساً بالنمو والانتماء.</p>'
          '<p>إذن البيت ليس مجرد جدران وأرضية وسقف، بل هو المكان الذي يشعر فيه الإنسان بأنه محبوب وله قيمة.</p>'),
  dict(n='4', t='Why writers use both', ta='لماذا يستخدم الكتّاب الاثنين؟',
    html='<p>Authors express the <b>tone</b> of their writing by using the denotative and connotative meanings of words. Doing so makes their storytelling and narrating richer.</p>'
         '<p>Look at these examples from the lesson:</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Word</th><th>Denotative</th><th>Connotative</th></tr>'
         '<tr><td>Classroom</td><td>A room made of walls, floor, and roof.</td><td>A place where children learn.</td></tr>'
         '<tr><td>Church</td><td>A building made of walls, floor, and roof.</td><td>A place where people pray to God.</td></tr>'
         '<tr><td>Sun</td><td>A star made of hot burning gases.</td><td>Warmth, morning, and a new day.</td></tr>'
         '<tr><td>Rain</td><td>Water falling from the sky.</td><td>Freshness, calm, and growing plants.</td></tr>'
         '<tr><td>Stars</td><td>Shining bodies very far from Earth.</td><td>Dreams, wonder, and wishes.</td></tr></table></div>',
    gloss='<p>يعبّر الكتّاب عن <b>نبرة</b> كتابتهم باستخدام المعنى الحرفي والمعنى المجازي معاً، فيصبح السرد أغنى وأجمل.</p>'
          '<p>أمثلة من الدرس: الفصل حرفياً غرفة بجدران وسقف، ومجازياً مكان يتعلم فيه الأطفال. والشمس حرفياً نجم من غازات ملتهبة، ومجازياً دفء وصباح ويوم جديد. والمطر حرفياً ماء ينزل من السماء، ومجازياً انتعاش وهدوء ونمو للنبات.</p>'),
 ],
 cards=[
  dict(f='Denotative meaning', fa='المعنى الحرفي', b='The plain dictionary meaning of a word. You can look it up.', ba='معنى الكلمة كما في القاموس، ويمكنك البحث عنه.'),
  dict(f='Connotative meaning', fa='المعنى المجازي', b='The feeling and ideas a word makes you think of.', ba='المشاعر والأفكار التي تثيرها الكلمة في ذهنك.'),
  dict(f='Home', fa='بيت', b='Denotative: a place where a family lives. Connotative: love, warmth, and belonging.', ba='حرفياً: مكان تعيش فيه الأسرة. مجازياً: حب ودفء وانتماء.'),
  dict(f='Classroom', fa='فصل دراسي', b='Denotative: a room with walls, floor, and roof. Connotative: a place where children learn.', ba='حرفياً: غرفة بجدران وأرضية وسقف. مجازياً: مكان يتعلم فيه الأطفال.'),
  dict(f='Church', fa='كنيسة', b='Denotative: a building of walls, floor, and roof. Connotative: a place where people pray.', ba='حرفياً: مبنى بجدران وأرضية وسقف. مجازياً: مكان يصلي فيه الناس.'),
  dict(f='Sun', fa='الشمس', b='Denotative: a star made of hot burning gases. Connotative: warmth and a fresh new day.', ba='حرفياً: نجم من غازات ملتهبة. مجازياً: دفء ويوم جديد.'),
  dict(f='Rain', fa='المطر', b='Denotative: water falling from the sky. Connotative: calm, freshness, and growing plants.', ba='حرفياً: ماء ينزل من السماء. مجازياً: هدوء وانتعاش ونمو النبات.'),
  dict(f='Stars', fa='النجوم', b='Denotative: shining bodies far from Earth. Connotative: dreams and wishes.', ba='حرفياً: أجرام مضيئة بعيدة عن الأرض. مجازياً: أحلام وأمنيات.'),
  dict(f='Tone', fa='نبرة الكاتب', b='The feeling an author gives their writing by choosing words carefully.', ba='الإحساس الذي يمنحه الكاتب لنصه من خلال اختيار الكلمات بعناية.'),
 ],
 game=dict(mode='sort',
   buckets=[dict(k='d', label='Dictionary'), dict(k='c', label='Feeling')],
   items=[
    dict(t='A home is a place where a family lives.', ta='البيت مكان تعيش فيه الأسرة.', k='d'),
    dict(t='Home means love, warmth and belonging.', ta='البيت يعني الحب والدفء والانتماء.', k='c'),
    dict(t='Rain is water falling from the sky.', ta='المطر ماء ينزل من السماء.', k='d'),
    dict(t='Rain makes everything feel fresh and calm.', ta='المطر يجعل كل شيء منتعشاً وهادئاً.', k='c'),
    dict(t='The sun is a star made of burning gases.', ta='الشمس نجم من غازات ملتهبة.', k='d'),
    dict(t='The sun means a warm, happy new day.', ta='الشمس تعني يوماً جديداً دافئاً وسعيداً.', k='c'),
    dict(t='A classroom is a room with walls and a roof.', ta='الفصل غرفة لها جدران وسقف.', k='d'),
    dict(t='A classroom is where friends learn together.', ta='الفصل مكان يتعلم فيه الأصدقاء معاً.', k='c'),
    dict(t='Stars are shining bodies far from Earth.', ta='النجوم أجرام مضيئة بعيدة عن الأرض.', k='d'),
    dict(t='Stars make me think of dreams and wishes.', ta='النجوم تذكّرني بالأحلام والأمنيات.', k='c'),
   ]),
 quiz=[
  dict(q='The plain meaning you find in a dictionary is called:', a='المعنى الذي تجدينه في القاموس يسمى:',
       o=['Connotative meaning','Denotative meaning','Tone','A synonym'], c=1),
  dict(q='The meaning built from feelings and memories is called:', a='المعنى الناتج عن المشاعر والذكريات يسمى:',
       o=['Denotative meaning','Spelling','Connotative meaning','A definition'], c=2),
  dict(q='Where can you look up the denotative meaning of a word?', a='أين تبحثين عن المعنى الحرفي للكلمة؟',
       o=['In an online or print dictionary','In a photo album','In a song','In a mirror'], c=0),
  dict(q='“Home is a place or dwelling where a family lives.” This is:', a='«البيت مكان تعيش فيه الأسرة». هذا معنى:',
       o=['Connotative','Denotative','A question','A poem'], c=1),
  dict(q='“Home makes me feel loved and safe.” This is:', a='«البيت يشعرني بالحب والأمان». هذا معنى:',
       o=['Denotative','Connotative','A dictionary entry','A spelling rule'], c=1),
  dict(q='Connotative meaning is based on:', a='المعنى المجازي يقوم على:',
       o=['Mental and emotional associations','The number of letters','The first letter of the word','The page number'], c=0),
  dict(q='Authors use both meanings mainly to:', a='يستخدم الكتّاب المعنيين أساساً من أجل:',
       o=['Make the page longer','Express the tone and enrich their storytelling','Hide the meaning','Count the words'], c=1),
  dict(q='Denotative meaning of the sun:', a='المعنى الحرفي للشمس:',
       o=['A warm, happy new day','A star made of hot burning gases','A wish','A holiday'], c=1),
  dict(q='Which sentence uses connotative meaning?', a='أي جملة تستخدم المعنى المجازي؟',
       o=['Rain is water that falls from the sky','Stars are bodies far from Earth','Her smile was sunshine','A classroom has walls and a roof'], c=2),
  dict(q='True or False: the denotative meaning is the same for everybody.', a='صح أم خطأ: المعنى الحرفي واحد لكل الناس.',
       o=['True','False'], c=0),
 ]))

# ─────────────────────────── 2 · ARABIC ALPHABET ───────────────────────────
LETTERS = [
 ('alif','ا','أليف'),('ba','ب','باء'),('ta','ت','تاء'),('tha','ث','ثاء'),('jim','ج','جيم'),
 ('ha','ح','حاء'),('kha','خ','خاء'),('dal','د','دال'),('zal','ذ','ذال'),('ra','ر','راء'),
 ('zay','ز','زاي'),('sin','س','سين'),('shin','ش','شين'),('sad','ص','صاد'),('dhad','ض','ضاد'),
 ('ta (heavy)','ط','طاء'),('zha','ظ','ظاء'),('ayn','ع','عين'),('gayn','غ','غين'),('fa','ف','فاء'),
 ('qaf','ق','قاف'),('kaf','ك','كاف'),('lam','ل','لام'),('meem','م','ميم'),('nun','ن','نون'),
 ('haa','ه','هاء'),('waw','و','واو'),('ya','ي','ياء'),
]
PAGES.append(dict(
 file='02-arabic-letters.html',
 title='The Arabic Alphabet',
 eyebrow='Arabic · حروف',
 palette=['#0d7f7a','#095e5a','#dcf1f0','#c68a1a','#fbeed3',
          '#48cfc6','#84e3dc','#093330','#e6b95c','#3a2c10'],
 blurb='Twenty-eight letters. Learn the name of each one, then find them in the games.',
 blurb_ar='ثمانية وعشرون حرفاً. تعلّمي اسم كل حرف ثم ابحثي عنه في الألعاب.',
 learn_h='How the alphabet works',
 learn_p='Open a part to read it, and press Listen to hear the English read aloud.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماع الشرح بالإنجليزية.',
 cards_h='Letter cards',
 cards_p='The letter is on the front. Say its name out loud, then flip to check.',
 cards_ar='الحرف في الوجه الأول. قولي اسمه بصوت عالٍ ثم اقلبي البطاقة للتأكد.',
 play_h='Match the letter to its name',
 play_p='Tap a letter on the left, then tap its name on the right.',
 play_ar='اضغطي على الحرف في اليسار، ثم على اسمه في اليمين.',
 parts=[
  dict(n='1', t='Twenty-eight letters', ta='ثمانية وعشرون حرفاً',
    html='<p>The Arabic alphabet has <b>28 letters</b>. Arabic is written and read from <b>right to left</b> — the opposite of English.</p>'
         '<p>Each letter has a name. When you say the alphabet you say the names: alif, ba, ta, tha, jim, and so on.</p>',
    gloss='<p>الأبجدية العربية فيها <b>ثمانية وعشرون حرفاً</b>، وتُكتب وتُقرأ <b>من اليمين إلى اليسار</b> عكس الإنجليزية.</p>'
          '<p>ولكل حرف اسم، فعند قراءة الحروف نقول: ألف، باء، تاء، ثاء، جيم… وهكذا.</p>'),
  dict(n='2', t='The dots make the difference', ta='النقط تصنع الفرق',
    html='<p>Some letters look the same and only the <b>dots</b> tell them apart. Look carefully:</p>'
         '<ul><li>ب has one dot below, ت has two dots above, ث has three dots above.</li>'
         '<li>ج has one dot inside, ح has none, خ has one dot on top.</li>'
         '<li>د has none, ذ has one dot. ر has none, ز has one dot.</li>'
         '<li>س has none, ش has three dots. ص has none, ض has one dot.</li>'
         '<li>ط has none, ظ has one dot. ع has none, غ has one dot.</li></ul>'
         '<p>So counting the dots is a real reading skill!</p>',
    gloss='<p>بعض الحروف تتشابه في الشكل ولا يفرّق بينها إلا <b>النقط</b>: الباء نقطة تحت، والتاء نقطتان فوق، والثاء ثلاث نقاط فوق. والجيم نقطة بالداخل، والحاء بلا نقطة، والخاء نقطة فوق. وكذلك د/ذ و ر/ز و س/ش و ص/ض و ط/ظ و ع/غ.</p>'
          '<p>لذلك عدّ النقط مهارة قراءة حقيقية!</p>'),
  dict(n='3', t='Letters that never join forward', ta='حروف لا تتصل بما بعدها',
    html='<p>Most Arabic letters join to the letter after them. But six letters never join forward:</p>'
         '<p style="font-size:1.6rem;letter-spacing:.5rem;direction:rtl;text-align:center">ا  د  ذ  ر  ز  و</p>'
         '<p>That is alif, dal, zal, ra, zay, and waw. After one of these, the next letter always starts fresh.</p>',
    gloss='<p>معظم الحروف العربية تتصل بالحرف الذي بعدها، لكن ستة حروف لا تتصل بما بعدها أبداً وهي: ا، د، ذ، ر، ز، و.</p>'
          '<p>بعد أي حرف منها يبدأ الحرف التالي منفصلاً.</p>'),
  dict(n='4', t='The full list', ta='القائمة كاملة',
    html='<div class="scroll"><table class="tbl"><tr><th>#</th><th>Letter</th><th>English name</th></tr>' +
         ''.join('<tr><td>%d</td><td style="font-size:1.4rem">%s</td><td>%s<div class="ar l">%s</div></td></tr>' % (i+1,l[1],l[0],l[2]) for i,l in enumerate(LETTERS)) +
         '</table></div>',
    gloss='<p>هذه قائمة الحروف الثمانية والعشرين مرتبة، مع اسم كل حرف مكتوباً بالإنجليزية كما تكتبينه في الواجب.</p>'),
 ],
 cards=[dict(f=l[1], fa=l[2], b='This letter is called “%s”.' % l[0], ba='هذا الحرف اسمه «%s».' % l[2]) for l in LETTERS[:14]],
 game=dict(mode='match', pairs=[dict(a=l[1], aa='', b=l[0], ba=l[2]) for l in
      [LETTERS[0],LETTERS[1],LETTERS[4],LETTERS[7],LETTERS[11],LETTERS[19],LETTERS[23],LETTERS[27]]]),
 quiz=[
  dict(q='How many letters are in the Arabic alphabet?', a='كم عدد حروف الأبجدية العربية؟', o=['24','26','28','30'], c=2),
  dict(q='Arabic is written and read:', a='تُكتب العربية وتُقرأ:', o=['Right to left','Left to right','Top to bottom only','In any direction'], c=0),
  dict(q='Which letter is called “alif”?', a='أي حرف اسمه «ألف»؟', o=['ب','ا','م','ن'], c=1),
  dict(q='Which letter is called “meem”?', a='أي حرف اسمه «ميم»؟', o=['م','ل','ك','ه'], c=0),
  dict(q='ب has one dot below. Which letter has three dots above?', a='الباء لها نقطة تحت. أي حرف له ثلاث نقاط فوق؟', o=['ت','ث','ن','ي'], c=1),
  dict(q='Which letter is “ya”, the last letter?', a='أي حرف هو «ياء» آخر الحروف؟', o=['و','ه','ي','ن'], c=2),
  dict(q='Which of these letters never joins to the letter after it?', a='أي من هذه الحروف لا يتصل بما بعده؟', o=['ب','س','د','ع'], c=2),
  dict(q='ح and خ look alike. What tells them apart?', a='الحاء والخاء متشابهتان. ما الفرق؟', o=['Their size','A dot above the خ','Their colour','Nothing at all'], c=1),
  dict(q='Which letter is called “sin”?', a='أي حرف اسمه «سين»؟', o=['ش','ص','س','ز'], c=2),
  dict(q='Which letter is called “qaf”?', a='أي حرف اسمه «قاف»؟', o=['ف','ق','ك','ع'], c=1),
 ]))

# ─────────────────────────── 3 · SEARCH ENGINES ───────────────────────────
PAGES.append(dict(
 file='03-search-engine.html',
 title='Searching the Web',
 eyebrow='ICT · Lesson 1',
 palette=['#1668c4','#0f4e97','#e0edfb','#e08a1e','#fceedb',
          '#61a8f0','#9ccbf7','#0d2338','#f0ab53','#3a2a10'],
 blurb='A search engine finds what you need among millions of websites. Learn to search like a pro.',
 blurb_ar='محرك البحث يجد ما تحتاجينه بين ملايين المواقع. تعلّمي كيف تبحثين باحتراف.',
 learn_h='How searching works',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Search words',
 cards_p='Say what each word means, then flip the card to check.',
 cards_ar='قولي معنى كل كلمة ثم اقلبي البطاقة للتأكد.',
 play_h='Which search engine is it?',
 play_p='Match each search engine to what makes it special.',
 play_ar='وصّلي كل محرك بحث بما يميّزه.',
 parts=[
  dict(n='1', t='What is a search engine?', ta='ما محرك البحث؟',
    html='<p>A <b>search engine</b> is a tool you use to look for information among millions of websites on the internet.</p>'
         '<p>You type a word or a question, and the search engine brings back a list of pages that might have your answer.</p>'
         '<h4>The top three search engines</h4><ol><li>Google</li><li>Bing</li><li>Yahoo</li></ol>',
    gloss='<p><b>محرك البحث</b> أداة تستخدمينها للبحث عن المعلومات بين ملايين المواقع على الإنترنت. تكتبين كلمة أو سؤالاً فيعرض لكِ قائمة بالصفحات التي قد تحتوي الإجابة.</p>'
          '<p>وأشهر ثلاثة محركات: جوجل، وبينج، وياهو.</p>'),
  dict(n='2', t='Search engines made for children', ta='محركات بحث للأطفال',
    html='<p>Some search engines are built specially for young people, so the results are safer:</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Name</th><th>What makes it special</th></tr>'
         '<tr><td>DuckDuckGo</td><td>Gives a search experience that does not follow you around.</td></tr>'
         '<tr><td>Kiddle</td><td>Powered by Google, offering a safe web for kids.</td></tr>'
         '<tr><td>KidRex</td><td>Made for children — fun and safe.</td></tr>'
         '<tr><td>KidzSearch</td><td>Family friendly. It helps find websites for children.</td></tr></table></div>',
    gloss='<p>هناك محركات بحث مصممة خصيصاً للأطفال لتكون النتائج آمنة:</p>'
          '<p><b>DuckDuckGo</b> يعطي تجربة بحث لا تتعقّبك. <b>Kiddle</b> يعمل بقوة جوجل ويقدّم ويباً آمناً للأطفال. <b>KidRex</b> مصنوع للأطفال، ممتع وآمن. <b>KidzSearch</b> مناسب للعائلة ويساعد على إيجاد مواقع للأطفال.</p>'),
  dict(n='3', t='The World Wide Web', ta='الشبكة العنكبوتية',
    html='<p>The <b>World Wide Web</b> was invented by <b>Tim Berners-Lee</b>. It holds millions of pieces of information: images, videos, and news.</p>'
         '<p>The fastest way to find something is to use a <b>keyword</b> or a short phrase instead of a long sentence.</p>',
    gloss='<p><b>الشبكة العنكبوتية العالمية</b> اخترعها <b>تيم بيرنرز-لي</b>، وتضم ملايين المعلومات من صور وفيديوهات وأخبار.</p>'
          '<p>وأسرع طريقة للوصول هي استخدام <b>كلمة مفتاحية</b> أو عبارة قصيرة بدل الجملة الطويلة.</p>'),
  dict(n='4', t='A search trick: the minus sign', ta='حيلة البحث: علامة الناقص',
    html='<p>If you want to <b>exclude</b> a word from your results, put the symbol <b>−</b> right before it, with no space.</p>'
         '<div class="hint"><p><b>Example:</b> typing <code>types of weather -sunny</code> gives results about all the types of weather <b>except</b> sunny.</p></div>'
         '<p>Two more helpful habits: use a keyword instead of a whole sentence, and check more than one result before you believe it.</p>',
    gloss='<p>إذا أردتِ <b>استبعاد</b> كلمة من النتائج، ضعي علامة <b>−</b> قبلها مباشرة بدون مسافة.</p>'
          '<p><b>مثال:</b> كتابة <code>types of weather -sunny</code> تعطي كل أنواع الطقس <b>ما عدا</b> المشمس.</p>'
          '<p>وعادتان مفيدتان: استخدمي كلمة مفتاحية بدل جملة كاملة، وتحققي من أكثر من نتيجة قبل التصديق.</p>'),
 ],
 cards=[
  dict(f='Search engine', fa='محرك البحث', b='A tool used to look for information among millions of websites.', ba='أداة للبحث عن المعلومات بين ملايين المواقع.'),
  dict(f='Keyword', fa='كلمة مفتاحية', b='The important word you type to find something quickly.', ba='الكلمة المهمة التي تكتبينها لتجدي ما تريدين بسرعة.'),
  dict(f='World Wide Web', fa='الشبكة العنكبوتية', b='The huge collection of pages, images, videos, and news on the internet.', ba='المجموعة الضخمة من الصفحات والصور والفيديوهات والأخبار على الإنترنت.'),
  dict(f='Tim Berners-Lee', fa='تيم بيرنرز-لي', b='The person who invented the World Wide Web.', ba='الشخص الذي اخترع الشبكة العنكبوتية العالمية.'),
  dict(f='The − symbol', fa='علامة الناقص', b='Put it before a word to remove that word from your results.', ba='ضعيها قبل الكلمة لاستبعادها من نتائج البحث.'),
  dict(f='Kiddle', fa='كيدل', b='A search engine powered by Google that offers a safe web for kids.', ba='محرك بحث يعمل بقوة جوجل ويقدم ويباً آمناً للأطفال.'),
  dict(f='KidRex', fa='كيد ركس', b='A search engine made for children — fun and safe.', ba='محرك بحث مصنوع للأطفال، ممتع وآمن.'),
  dict(f='KidzSearch', fa='كيدز سيرش', b='A family-friendly engine that helps find websites for children.', ba='محرك مناسب للعائلة يساعد على إيجاد مواقع للأطفال.'),
  dict(f='DuckDuckGo', fa='داك داك جو', b='A search engine that gives a search experience without following you.', ba='محرك بحث يعطي تجربة بحث دون تعقّبك.'),
 ],
 game=dict(mode='match', pairs=[
   dict(a='Google', aa='', b='One of the top three search engines', ba='من أشهر ثلاثة محركات بحث'),
   dict(a='Kiddle', aa='', b='Powered by Google, safe web for kids', ba='يعمل بقوة جوجل، ويب آمن للأطفال'),
   dict(a='KidRex', aa='', b='Made for children — fun and safe', ba='مصنوع للأطفال، ممتع وآمن'),
   dict(a='KidzSearch', aa='', b='Family friendly, finds sites for children', ba='مناسب للعائلة، يجد مواقع للأطفال'),
   dict(a='DuckDuckGo', aa='', b='Searching without being followed', ba='بحث دون تعقّب'),
   dict(a='Tim Berners-Lee', aa='', b='Invented the World Wide Web', ba='اخترع الشبكة العنكبوتية'),
   dict(a='Keyword', aa='', b='The fastest way to search', ba='أسرع طريقة للبحث'),
   dict(a='The − symbol', aa='', b='Removes a word from the results', ba='يستبعد كلمة من النتائج'),
 ]),
 quiz=[
  dict(q='A search engine is used to:', a='محرك البحث يُستخدم من أجل:',
       o=['Look for information among millions of websites','Print your homework','Charge a tablet','Draw pictures'], c=0),
  dict(q='Which of these is NOT one of the top three search engines in the lesson?', a='أي مما يلي ليس من أشهر ثلاثة محركات في الدرس؟',
       o=['Google','Bing','Yahoo','Kiddle'], c=3),
  dict(q='Kiddle is powered by:', a='محرك كيدل يعمل بقوة:',
       o=['Google','Yahoo','Bing','Opera'], c=0),
  dict(q='Which search engine was made by and for children?', a='أي محرك بحث صُنع للأطفال؟',
       o=['Bing','KidRex','Yahoo','Google'], c=1),
  dict(q='Who invented the World Wide Web?', a='من اخترع الشبكة العنكبوتية؟',
       o=['Tim Berners-Lee','Bill Gates','Steve Jobs','Ada Lovelace'], c=0),
  dict(q='The fastest way to search is to use:', a='أسرع طريقة للبحث هي استخدام:',
       o=['A very long sentence','A keyword or short phrase','Only pictures','Random letters'], c=1),
  dict(q='To exclude a word from your results you type:', a='لاستبعاد كلمة من النتائج تكتبين:',
       o=['A plus sign + before it','A minus sign − before it','A question mark','Nothing'], c=1),
  dict(q='You type: weather -sunny. The results will show:', a='إذا كتبتِ weather -sunny ستظهر النتائج:',
       o=['Only sunny weather','All weather except sunny','No results at all','Only pictures'], c=1),
  dict(q='The World Wide Web holds millions of:', a='تضم الشبكة العنكبوتية ملايين:',
       o=['Only text pages','Images, videos, and news','Only videos','Only games'], c=1),
  dict(q='KidzSearch is described as:', a='يوصف KidzSearch بأنه:',
       o=['Family friendly','Only for teachers','A drawing app','A game console'], c=0),
 ]))
