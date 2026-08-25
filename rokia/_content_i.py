# -*- coding: utf-8 -*-
PAGES = []

# ─────────────────────────── 17 · SUBJECT-VERB AGREEMENT, PRONOUNS, ADJECTIVE ORDER ───────────────────────────
PAGES.append(dict(
 file='17-grammar-toolkit.html',
 title='The Grammar Toolkit',
 eyebrow='English · Unit 1, Lesson 2',
 palette=['#1f6f5c','#154f42','#dcf0ea','#a8501f','#f9e3d6',
          '#5fc0a4','#9adfc8','#0d2e26','#e08a55','#3a2011'],
 blurb='A verb has to match its subject, a pronoun has to match its noun, and adjectives line up in one order. Learn the rules that make a sentence sound right.',
 blurb_ar='الفعل يجب أن يطابق فاعله، والضمير يجب أن يطابق اسمه، والصفات تصطف بترتيب واحد. تعلّمي القواعد التي تجعل الجملة سليمة.',
 learn_h='Three rules that hold a sentence together',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Grammar cards',
 cards_p='Work out the rule in your head first, then flip the card to check.',
 cards_ar='احسبي القاعدة في ذهنك أولاً ثم اقلبي البطاقة للتأكد.',
 play_h='Correct or has an error?',
 play_p='Read each sentence from the worksheet. Is the verb right, or does it need fixing?',
 play_ar='اقرئي كل جملة من الورقة. هل الفعل صحيح أم يحتاج تصحيحاً؟',
 parts=[
  dict(n='1', t='Subject pronouns and their verbs', ta='ضمائر الفاعل وأفعالها',
    html='<p><b>Subject pronouns</b> function as the subject of a sentence. They are: <b>I, we, you, he, she, it,</b> and <b>they</b>.</p>'
         '<p>A pronoun replaces a noun in a sentence to avoid repeating it — and once it does, the verb has to agree with it in number.</p>'
         '<ul><li><b>I, we, you,</b> and <b>they</b> take the <b>plural</b> form of the verb.</li>'
         '<li><b>He, she,</b> and <b>it</b> take the <b>singular</b> form of the verb.</li></ul>'
         '<p><i>“I always have playdates with my friends.”</i> — <i>“She likes baking cookies with her friends.”</i></p>',
    gloss='<p><b>ضمائر الفاعل</b> تعمل كفاعل في الجملة، وهي: I, we, you, he, she, it, they.</p>'
          '<p>الضمير يحل محل الاسم في الجملة لتجنّب تكراره، وبمجرد استخدامه يجب أن يطابقه الفعل في العدد.</p>'
          '<p><b>I, we, you, they</b> تأخذ صيغة الفعل <b>الجمع</b>. و<b>he, she, it</b> تأخذ صيغة الفعل <b>المفرد</b>.</p>'
          '<p>مثال: «I always have playdates» و«She likes baking cookies».</p>'),
  dict(n='2', t='Demonstrative pronouns: near and far', ta='ضمائر الإشارة: قريب وبعيد',
    html='<p><b>Demonstrative pronouns</b> point out specific persons, places, or things, and show how near or far the thing being referred to is.</p>'
         '<p>The four demonstrative pronouns are <b>this, that, these,</b> and <b>those</b>.</p>'
         '<ul><li><b>This</b> (near) and <b>that</b> (far) take the <b>singular</b> form of the verb.</li>'
         '<li><b>These</b> (near) and <b>those</b> (far) take the <b>plural</b> form of the verb.</li></ul>'
         '<p><i>“This is a good place to relax.”</i> — <i>“These look very rare and expensive.”</i></p>'
         '<div class="hint"><p><b>Take note:</b> the near/far pairing is about distance, but the singular/plural pairing is about the verb — this and that always want a singular verb, no matter what they point to.</p></div>',
    gloss='<p><b>ضمائر الإشارة</b> تشير إلى أشخاص أو أماكن أو أشياء محددة، وتوضح مدى قرب أو بعد الشيء المُشار إليه.</p>'
          '<p>الأربعة هي: this, that (قريب/بعيد للمفرد)، وthese, those (قريب/بعيد للجمع).</p>'
          '<p><b>this</b> و<b>that</b> تأخذان صيغة الفعل <b>المفرد</b>. و<b>these</b> و<b>those</b> تأخذان صيغة الفعل <b>الجمع</b>.</p>'
          '<p>مثال: «This is a good place» و«These look very rare».</p>'),
  dict(n='3', t='Relative pronouns and their antecedent', ta='ضمائر الوصل واسمها الموصول',
    html='<p><b>Relative pronouns</b> are found at the start of a relative clause — a clause that gives more information about the noun right before it.</p>'
         '<p>Common relative pronouns are <b>who, that, which, whose,</b> and <b>whom</b>. The noun that the relative pronoun replaces is called the <b>antecedent</b>.</p>'
         '<p>In writing, the verb inside the relative clause must agree with the <b>antecedent</b> in number — not with anything else in the sentence.</p>'
         '<p><i>“The man <b>who</b> sings beautifully is my uncle.”</i> — the antecedent is “the man” (singular), so the verb is “sings”.</p>'
         '<p><i>“The dancing lights <b>that</b> fill the park with colors are fun to watch.”</i> — the antecedent is “the dancing lights” (plural), so the verb is “fill”.</p>'
         '<div class="hint"><p><b>Find the antecedent first.</b> Ask “who or what does the relative pronoun stand for?” — that word decides whether the clause verb is singular or plural.</p></div>',
    gloss='<p><b>ضمائر الوصل</b> تقع في بداية جملة الصلة، وهي جملة تعطي معلومات إضافية عن الاسم الذي يسبقها مباشرة.</p>'
          '<p>الشائعة منها: who, that, which, whose, whom. والاسم الذي يحل محله ضمير الوصل يسمى <b>الاسم الموصول (antecedent)</b>.</p>'
          '<p>يجب أن يطابق الفعل داخل جملة الصلة الاسمَ الموصول في العدد لا أي كلمة أخرى في الجملة.</p>'
          '<p>مثال: «The man who sings beautifully» — الاسم الموصول «the man» مفرد، فالفعل «sings». ومثال: «The dancing lights that fill the park» — الاسم الموصول جمع، فالفعل «fill».</p>'
          '<p><b>ابحثي عن الاسم الموصول أولاً:</b> اسألي «إلى من أو ماذا يعود ضمير الوصل؟» — تلك الكلمة تحدد صيغة الفعل.</p>'),
  dict(n='4', t='Tricky subjects: collective and abstract nouns', ta='فاعلون خادعون: أسماء جماعية ومجردة',
    html='<p>Some subjects look like they should take a plural verb, but they do not.</p>'
         '<ul><li><b>Collective nouns</b> — like <i>family, team, committee,</i> and <i>board</i> — name a group, but the group acts as <b>one unit</b>, so it takes a singular verb: <i>“The family gathers.”</i> “The committee discusses.”</li>'
         '<li><b>A herd/group “of” something</b> — the verb agrees with the collective word, not the plural noun after “of”: <i>“A herd of cattle grazes”</i>, not “graze”.</li>'
         '<li><b>Abstract nouns</b> — like <i>bravery, wisdom,</i> and <i>unity</i> — name an idea, not a person or thing, but they are still singular: <i>“Wisdom comes with experience.”</i></li></ul>'
         '<div class="hint"><p><b>The trap to avoid:</b> “The books on the old man’s shelf are all classics” — the verb agrees with <i>books</i> (the real subject), not with <i>shelf</i>, the closer noun.</p></div>',
    gloss='<p>بعض الفاعلين يبدون وكأنهم يحتاجون فعلاً بصيغة الجمع، لكنهم لا يحتاجون.</p>'
          '<p><b>الأسماء الجماعية</b> مثل family وteam وcommittee وboard تسمي مجموعة، لكن المجموعة تتصرف <b>كوحدة واحدة</b> فتأخذ فعلاً مفرداً: «The family gathers».</p>'
          '<p><b>مجموعة «من» شيء</b> — يطابق الفعل الكلمة الجماعية لا الاسم الجمع بعد «of»: «A herd of cattle grazes» لا «graze».</p>'
          '<p><b>الأسماء المجردة</b> مثل bravery وwisdom وunity تسمي فكرة لا شخصاً أو شيئاً، لكنها تبقى مفردة: «Wisdom comes with experience».</p>'
          '<p><b>فخ يجب تجنبه:</b> «The books on the old man’s shelf are all classics» — يطابق الفعل «books» الفاعل الحقيقي، لا «shelf» الاسم الأقرب.</p>'),
  dict(n='5', t='Putting adjectives in order', ta='ترتيب الصفات',
    html='<p>Writers use <b>adjectives</b> to describe a noun or pronoun — they modify or add information about the word they describe.</p>'
         '<p>When more than one adjective describes the same word, they must be arranged in a certain order:</p>'
         '<p style="font-size:1.05rem;font-weight:700">determiner → quantity → quality → size → shape → color → noun</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Determiner</th><th>Quantity</th><th>Quality</th><th>Size</th><th>Shape</th><th>Color</th><th>Noun</th></tr>'
         '<tr><td>The</td><td>three</td><td>durable</td><td>big</td><td>round</td><td>white</td><td>plates</td></tr></table></div>'
         '<p><i>“The three, durable, big, round, white plates break when Lala drops them onto the kitchen floor.”</i></p>'
         '<div class="hint"><p><b>Say it out loud.</b> Swap two of the categories and the sentence instantly sounds wrong, even if you cannot explain why — that is your ear checking the order for you.</p></div>',
    gloss='<p>يستخدم الكتّاب <b>الصفات</b> لوصف اسم أو ضمير — فهي تعدّل أو تضيف معلومات عن الكلمة التي تصفها.</p>'
          '<p>وعندما تصف أكثر من صفة نفس الكلمة، يجب ترتيبها بطريقة معينة:</p>'
          '<p><b>أداة تعريف ← عدد ← نوعية ← حجم ← شكل ← لون ← الاسم</b></p>'
          '<p>مثال: The (أداة) three (عدد) durable (نوعية) big (حجم) round (شكل) white (لون) plates (الاسم).</p>'
          '<p>«الأطباق الثلاثة المتينة الكبيرة المستديرة البيضاء تنكسر عندما تُسقطها لالا على أرضية المطبخ.»</p>'
          '<p><b>اقرئي بصوت عالٍ:</b> بدّلي ترتيب صفتين وستشعرين فوراً أن الجملة خاطئة، حتى لو لم تستطيعي تفسير السبب — تلك أذنك تتحقق من الترتيب نيابة عنك.</p>'),
 ],
 cards=[
  dict(f='I, we, you, they', fa='I, we, you, they', b='Take the plural form of the verb.', ba='تأخذ صيغة الفعل الجمع.'),
  dict(f='He, she, it', fa='He, she, it', b='Take the singular form of the verb.', ba='تأخذ صيغة الفعل المفرد.'),
  dict(f='This / that', fa='this / that', b='Near and far, singular — take the singular form of the verb.', ba='قريب وبعيد للمفرد، يأخذان صيغة الفعل المفرد.'),
  dict(f='These / those', fa='these / those', b='Near and far, plural — take the plural form of the verb.', ba='قريب وبعيد للجمع، يأخذان صيغة الفعل الجمع.'),
  dict(f='Antecedent', fa='الاسم الموصول', b='The noun that a relative pronoun replaces — the clause verb must agree with it.', ba='الاسم الذي يحل محله ضمير الوصل، ويجب أن يطابقه فعل جملة الصلة.'),
  dict(f='Relative pronouns', fa='ضمائر الوصل', b='who, that, which, whose, whom — start a relative clause.', ba='who, that, which, whose, whom — تبدأ بها جملة الصلة.'),
  dict(f='Collective noun', fa='اسم جماعي', b='Names a group acting as one unit, so it takes a singular verb: family, team, committee, board.', ba='يسمي مجموعة تتصرف كوحدة، فيأخذ فعلاً مفرداً: family, team, committee, board.'),
  dict(f='Abstract noun', fa='اسم مجرد', b='Names an idea, not a thing, and is still singular: bravery, wisdom, unity.', ba='يسمي فكرة لا شيئاً، ويبقى مفرداً: bravery, wisdom, unity.'),
  dict(f='Adjective order', fa='ترتيب الصفات', b='determiner, quantity, quality, size, shape, color, then the noun.', ba='أداة تعريف، عدد، نوعية، حجم، شكل، لون، ثم الاسم.'),
  dict(f='“The three durable big round white plates”', fa='مثال الترتيب', b='Determiner–quantity–quality–size–shape–color, in that order.', ba='أداة تعريف–عدد–نوعية–حجم–شكل–لون، بهذا الترتيب.'),
 ],
 game=dict(mode='sort',
   buckets=[dict(k='ok', label='Correct'), dict(k='fix', label='Has an error')],
   items=[
    dict(t='The family gathers to open the Christmas presents.', ta='العائلة تجتمع لفتح هدايا الكريسماس.', k='ok'),
    dict(t='The plants makes granny’s garden vibrant and colorful.', ta='«The plants makes» — خطأ.', k='fix'),
    dict(t='A herd of cattle grazes peacefully in the grass field.', ta='قطيع الماشية يرعى بسلام.', k='ok'),
    dict(t='This sound like a song from the past.', ta='«This sound» — خطأ.', k='fix'),
    dict(t='The books on the old man’s shelf are all classics.', ta='الكتب على رف الرجل العجوز كلها كلاسيكيات.', k='ok'),
    dict(t='The school bus that fetch me for school is unavailable today.', ta='«that fetch» — خطأ.', k='fix'),
    dict(t='Wisdom always comes with experience.', ta='الحكمة تأتي دائماً مع الخبرة.', k='ok'),
    dict(t='The board decide on the very important matters.', ta='«The board decide» — خطأ.', k='fix'),
    dict(t='The committee discusses the plan for the event.', ta='اللجنة تناقش خطة الحدث.', k='ok'),
    dict(t='These tastes heavenly. Can I have more cookies?', ta='«These tastes» — خطأ.', k='fix'),
   ]),
 quiz=[
  dict(q='Which subject pronouns take the plural form of the verb?', a='أي ضمائر فاعل تأخذ صيغة الفعل الجمع؟',
       o=['He, she, it','I, we, you, they','This, that','Who, which'], c=1),
  dict(q='Which subject pronouns take the singular form of the verb?', a='أي ضمائر فاعل تأخذ صيغة الفعل المفرد؟',
       o=['I, we, you','He, she, it','These, those','They'], c=1),
  dict(q='“This” and “that” take which form of the verb?', a='«this» و«that» تأخذان أي صيغة للفعل؟',
       o=['Plural','Singular','No verb at all','Both forms'], c=1),
  dict(q='“These” and “those” take which form of the verb?', a='«these» و«those» تأخذان أي صيغة للفعل؟',
       o=['Singular','Plural','No verb at all','Depends on the noun'], c=1),
  dict(q='A relative clause gives more information about:', a='جملة الصلة تعطي معلومات إضافية عن:',
       o=['The noun right before it','The whole paragraph','The title of the text','Nothing in particular'], c=0),
  dict(q='The noun that a relative pronoun replaces is called the:', a='الاسم الذي يحل محله ضمير الوصل يسمى:',
       o=['Subject','Antecedent','Determiner','Object'], c=1),
  dict(q='“The man who sings beautifully is my uncle.” The verb “sings” agrees with:', a='في «The man who sings beautifully»، يطابق الفعل «sings»:',
       o=['“Beautifully”','“The man”','“My uncle”','Nothing'], c=1),
  dict(q='“The family gathers to open the presents.” Why is “gathers” singular?', a='لماذا الفعل «gathers» مفرد في «The family gathers»؟',
       o=['Because family is a collective noun acting as one unit','Because it is a mistake','Because presents is plural','There is no reason'], c=0),
  dict(q='Correct the error: “The plants makes granny’s garden vibrant.”', a='صححي الخطأ: «The plants makes granny’s garden vibrant».',
       o=['The plants make granny’s garden vibrant','The plants maked granny’s garden vibrant','No error','The plant makes granny’s garden vibrant'], c=0),
  dict(q='Correct the error: “This sound like a song from the past.”', a='صححي الخطأ: «This sound like a song from the past».',
       o=['This sounds like a song from the past','This sound liked a song from the past','No error','These sound like a song from the past'], c=0),
  dict(q='Correct the error: “The board decide on the very important matters.”', a='صححي الخطأ: «The board decide on the very important matters».',
       o=['The board decides on the very important matters','The boards decide on the very important matters','No error','The board deciding on the matters'], c=0),
  dict(q='Which sentence has NO error in subject-verb agreement?', a='أي جملة لا تحتوي خطأ في تطابق الفاعل والفعل؟',
       o=['Bravery is the choice to face your fears with faith in your heart.','This sound like a song from the past.','The board decide on the matters.','The plants makes the garden vibrant.'], c=0),
  dict(q='Adjectives describing the same noun are arranged in the order:', a='الصفات التي تصف نفس الاسم تُرتَّب بالترتيب:',
       o=['Color, shape, size, quality, quantity, determiner','Determiner, quantity, quality, size, shape, color','Size, color, shape, quantity, quality, determiner','Any order is correct'], c=1),
  dict(q='In “the three durable big round white plates,” which word shows quantity?', a='في «the three durable big round white plates»، أي كلمة تدل على العدد؟',
       o=['Three','Durable','Round','White'], c=0),
  dict(q='In “the three durable big round white plates,” which word is the determiner?', a='في «the three durable big round white plates»، أي كلمة أداة التعريف؟',
       o=['Big','The','Round','Plates'], c=1),
 ]))
