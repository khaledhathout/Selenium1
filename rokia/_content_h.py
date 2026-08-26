# -*- coding: utf-8 -*-
PAGES = []

# ─────────────────────────── 16 · POLYGONS: SHAPE AND ANGLE SUM ───────────────────────────
PAGES.append(dict(
 file='16-polygon-basics.html',
 title='The Shape of a Polygon',
 eyebrow='Math 7 · Unit 1, Lesson 1–2',
 palette=['#1f7a4f','#155c3a','#dcf3e6','#a8471e','#f9e2d6',
          '#5fc98d','#9ee3ba','#0d3322','#e0885a','#3a1f10'],
 blurb='Every polygon hides a number trick. Count its sides, and you can predict every angle inside it.',
 blurb_ar='كل مضلع يخفي حيلة رقمية. عُدّي أضلاعه، وستتوقعين كل زاوية بداخله.',
 learn_h='What makes a shape a polygon',
 learn_p='Open a part to read it, and press Listen to hear it read aloud in English.',
 learn_ar='افتحي أي جزء لقراءته، واضغطي «Listen» لسماعه بالإنجليزية.',
 cards_h='Polygon cards',
 cards_p='Work out the answer in your head first, then flip the card to check.',
 cards_ar='احسبي الإجابة في ذهنك أولاً ثم اقلبي البطاقة.',
 play_h='Sides, sum, or shape family?',
 play_p='Sort each fact into the group it belongs to.',
 play_ar='صنّفي كل معلومة حسب المجموعة التي تنتمي إليها.',
 parts=[
  dict(n='1', t='What counts as a polygon', ta='ما الذي يُعدّ مضلعاً',
    html='<p>A <b>polygon</b> is a closed, two-dimensional figure formed by line segments connected endpoint to endpoint, where no two sides belong to the same line.</p>'
         '<p>Three things can break that definition:</p>'
         '<ul><li><b>Not closed.</b> If the sides do not connect all the way around, it is not a polygon.</li>'
         '<li><b>Not made of straight segments.</b> A shape with a curved edge, like a circle or a half-circle, is not a polygon.</li>'
         '<li><b>Two sides on the same line.</b> If part of the outline doubles back over itself in a straight line, it breaks the rule too.</li></ul>'
         '<div class="hint"><p><b>Quick test:</b> trace the outline with one finger without lifting it. If you end exactly where you started, and every edge was straight, it is a polygon.</p></div>',
    gloss='<p><b>المضلع</b> شكل مغلق ثنائي الأبعاد، مكوَّن من قطع مستقيمة متصلة من طرف إلى طرف، بحيث لا يقع أي ضلعين على نفس الخط المستقيم.</p>'
          '<p>ثلاثة أشياء تنقض هذا التعريف: <b>ألا يكون مغلقاً</b> بالكامل، أو <b>يحتوي حافة منحنية</b> كالدائرة، أو <b>يقع ضلعان على نفس الخط</b> المستقيم.</p>'
          '<p><b>اختبار سريع:</b> تتبعي الحدود الخارجية بإصبعك دون رفعه. إذا عدتِ لنقطة البداية تماماً وكانت كل الحواف مستقيمة، فهو مضلع.</p>'),
  dict(n='2', t='Regular or irregular', ta='منتظم أم غير منتظم',
    html='<p>Every polygon falls into one of two groups, based on its sides and angles.</p>'
         '<h4>Regular polygon</h4><p>All sides and all angles have <b>equal</b> measurements. An equilateral triangle and a square are both regular.</p>'
         '<h4>Irregular polygon</h4><p>Sides and angles have <b>different</b> measurements.</p>'
         '<div class="hint"><p><b>Take note:</b> a shape needs equal sides <i>and</i> equal angles to be regular. Equal sides alone are not enough.</p></div>',
    gloss='<p>كل مضلع ينتمي لإحدى مجموعتين حسب أضلاعه وزواياه.</p>'
          '<p><b>المضلع المنتظم:</b> كل الأضلاع وكل الزوايا متساوية القياس، مثل المثلث متساوي الأضلاع والمربع.</p>'
          '<p><b>المضلع غير المنتظم:</b> الأضلاع والزوايا مختلفة القياس.</p>'
          '<p><b>ملاحظة:</b> يحتاج الشكل لأضلاع متساوية <i>و</i>زوايا متساوية ليكون منتظماً؛ الأضلاع المتساوية وحدها لا تكفي.</p>'),
  dict(n='3', t='Convex or non-convex', ta='محدّب أم غير محدّب',
    html='<p>Draw a line segment between any two points inside a polygon. What happens tells you which family it belongs to.</p>'
         '<h4>Convex polygon</h4><p>Line segments whose both endpoints are inside the polygon are drawn entirely <b>inside</b> the shape — they never cross an edge.</p>'
         '<h4>Non-convex polygon</h4><p>Some of those line segments have parts that lie <b>outside</b> the polygon — one corner “caves in”, and a connecting line escapes the shape before coming back.</p>'
         '<div class="hint"><p><b>Spot it fast:</b> look for a corner that points inward instead of outward, like a bite taken out of the shape. That single dent is enough to make it non-convex.</p></div>',
    gloss='<p>ارسمي قطعة مستقيمة بين أي نقطتين داخل المضلع، وستخبرك النتيجة أي مجموعة ينتمي إليها.</p>'
          '<p><b>المضلع المحدّب:</b> أي قطعة مستقيمة طرفاها داخل الشكل تبقى بالكامل <b>داخله</b> ولا تتقاطع مع أي ضلع.</p>'
          '<p><b>المضلع غير المحدّب:</b> بعض هذه القطع يخرج جزء منها <b>خارج</b> الشكل — زاوية واحدة "تنغرز للداخل" فتهرب القطعة المستقيمة من الشكل قبل أن تعود.</p>'
          '<p><b>للتمييز بسرعة:</b> ابحثي عن زاوية تشير للداخل بدل الخارج، كأن قضمة أُخذت من الشكل — هذه الغرزة الواحدة كافية لجعله غير محدّب.</p>'),
  dict(n='4', t='The sum of the interior angles', ta='مجموع الزوايا الداخلية',
    html='<p>Any polygon can be divided into triangles by drawing diagonals from one corner. Count the triangles, and you can find the sum of all the interior angles — because every triangle contributes exactly 180°.</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Polygon</th><th>Sides</th><th>Triangles formed</th><th>Sum of angles</th></tr>'
         '<tr><td>Triangle</td><td>3</td><td>1</td><td>1 × 180° = 180°</td></tr>'
         '<tr><td>Quadrilateral</td><td>4</td><td>2</td><td>2 × 180° = 360°</td></tr>'
         '<tr><td>Pentagon</td><td>5</td><td>3</td><td>3 × 180° = 540°</td></tr>'
         '<tr><td>Hexagon</td><td>6</td><td>4</td><td>4 × 180° = 720°</td></tr></table></div>'
         '<p>Notice the pattern: the number of triangles is always <b>2 less</b> than the number of sides. That gives the general rule:</p>'
         '<p style="font-size:1.15rem;font-weight:700">Sum of interior angles = (n − 2) × 180°</p>'
         '<p>where <b>n</b> is the number of sides.</p>'
         '<div class="hint"><p><b>Worked example:</b> an octagon has 8 sides. Sum = (8 − 2) × 180° = 6 × 180° = <b>1080°</b>.</p></div>',
    gloss='<p>يمكن تقسيم أي مضلع إلى مثلثات برسم أقطار من زاوية واحدة، وعدّ المثلثات يعطي مجموع كل الزوايا الداخلية — لأن كل مثلث يساهم بـ١٨٠° بالضبط.</p>'
          '<p>المثلث: ٣ أضلاع، مثلث واحد، المجموع ١٨٠°. الرباعي: ٤ أضلاع، مثلثان، المجموع ٣٦٠°. الخماسي: ٥ أضلاع، ثلاثة مثلثات، المجموع ٥٤٠°. السداسي: ٦ أضلاع، أربعة مثلثات، المجموع ٧٢٠°.</p>'
          '<p>لاحظي النمط: عدد المثلثات دائماً أقل بـ٢ من عدد الأضلاع، ومنه القاعدة العامة:</p>'
          '<p><b>مجموع الزوايا الداخلية = (ن − ٢) × ١٨٠°</b> حيث ن عدد الأضلاع.</p>'
          '<p><b>مثال:</b> الثماني الأضلاع: (٨ − ٢) × ١٨٠° = ٦ × ١٨٠° = <b>١٠٨٠°</b>.</p>'),
  dict(n='5', t='Every angle of a regular polygon', ta='زاوية واحدة من مضلع منتظم',
    html='<p>In a <b>regular</b> polygon every interior angle is equal, so once you know the total sum, divide it by the number of angles (which is the same as the number of sides) to find just one.</p>'
         '<p style="font-size:1.15rem;font-weight:700">Each interior angle = (n − 2) × 180° ÷ n</p>'
         '<div class="scroll"><table class="tbl"><tr><th>Regular polygon</th><th>Working</th><th>Each angle</th></tr>'
         '<tr><td>Triangle</td><td>180° ÷ 3</td><td>60°</td></tr>'
         '<tr><td>Quadrilateral</td><td>360° ÷ 4</td><td>90°</td></tr>'
         '<tr><td>Pentagon</td><td>540° ÷ 5</td><td>108°</td></tr>'
         '<tr><td>Octagon</td><td>1080° ÷ 8</td><td>135°</td></tr></table></div>'
         '<p>The exterior angle of a regular polygon has its own shortcut, because all the exterior angles of any polygon always add up to a full turn.</p>'
         '<p style="font-size:1.15rem;font-weight:700">Each exterior angle of a regular polygon = 360° ÷ n</p>'
         '<div class="hint"><p><b>Worked example:</b> a regular pentagon: 360° ÷ 5 = <b>72°</b> for each exterior angle, which matches 180° − 108° from the interior angle above.</p></div>',
    gloss='<p>في المضلع <b>المنتظم</b> كل زاوية داخلية متساوية، فبعد معرفة المجموع الكلي نقسمه على عدد الزوايا (وهو نفس عدد الأضلاع) لنجد زاوية واحدة.</p>'
          '<p><b>الزاوية الداخلية الواحدة = (ن − ٢) × ١٨٠° ÷ ن</b></p>'
          '<p>المثلث: ١٨٠ ÷ ٣ = ٦٠°. الرباعي: ٣٦٠ ÷ ٤ = ٩٠°. الخماسي: ٥٤٠ ÷ ٥ = ١٠٨°. الثماني: ١٠٨٠ ÷ ٨ = ١٣٥°.</p>'
          '<p>وللزاوية الخارجية للمضلع المنتظم اختصار خاص، لأن كل الزوايا الخارجية لأي مضلع تجمع دائماً لدورة كاملة:</p>'
          '<p><b>الزاوية الخارجية الواحدة للمضلع المنتظم = ٣٦٠° ÷ ن</b></p>'
          '<p><b>مثال:</b> الخماسي المنتظم: ٣٦٠ ÷ ٥ = <b>٧٢°</b>، وهذا يطابق ١٨٠ − ١٠٨ من الزاوية الداخلية أعلاه.</p>'),
 ],
 cards=[
  dict(f='Polygon', fa='المضلع', b='A closed, two-dimensional figure made of connected straight line segments.', ba='شكل مغلق ثنائي الأبعاد مكوَّن من قطع مستقيمة متصلة.'),
  dict(f='Regular polygon', fa='مضلع منتظم', b='All sides and all angles are equal.', ba='كل الأضلاع وكل الزوايا متساوية.'),
  dict(f='Irregular polygon', fa='مضلع غير منتظم', b='Sides and angles have different measurements.', ba='الأضلاع والزوايا مختلفة القياس.'),
  dict(f='Convex polygon', fa='مضلع محدّب', b='Any line segment between two interior points stays entirely inside the shape.', ba='أي قطعة بين نقطتين داخليتين تبقى كلها داخل الشكل.'),
  dict(f='Non-convex polygon', fa='مضلع غير محدّب', b='Has at least one corner that caves inward, so some connecting segments escape the shape.', ba='به زاوية واحدة على الأقل تنغرز للداخل.'),
  dict(f='Sum of interior angles', fa='مجموع الزوايا الداخلية', b='(n − 2) × 180°, where n is the number of sides.', ba='(ن − ٢) × ١٨٠°، حيث ن عدد الأضلاع.'),
  dict(f='Sum for a hexagon', fa='مجموع السداسي', b='(6 − 2) × 180° = 720°.', ba='(٦ − ٢) × ١٨٠° = ٧٢٠°.'),
  dict(f='Sum for an octagon', fa='مجموع الثماني', b='(8 − 2) × 180° = 1080°.', ba='(٨ − ٢) × ١٨٠° = ١٠٨٠°.'),
  dict(f='Each angle of a regular polygon', fa='الزاوية الواحدة في المنتظم', b='(n − 2) × 180° ÷ n.', ba='(ن − ٢) × ١٨٠° ÷ ن.'),
  dict(f='Each angle of a regular pentagon', fa='زاوية الخماسي المنتظم', b='540° ÷ 5 = 108°.', ba='٥٤٠° ÷ ٥ = ١٠٨°.'),
  dict(f='Each exterior angle of a regular polygon', fa='الزاوية الخارجية في المنتظم', b='360° ÷ n.', ba='٣٦٠° ÷ ن.'),
  dict(f='Each exterior angle of a regular hexagon', fa='الزاوية الخارجية للسداسي المنتظم', b='360° ÷ 6 = 60°.', ba='٣٦٠° ÷ ٦ = ٦٠°.'),
 ],
 game=dict(mode='sort',
   buckets=[dict(k='def', label='Definition'), dict(k='fam', label='Shape family'), dict(k='sum', label='Angle sum')],
   items=[
    dict(t='A closed 2-D figure made of connected straight segments', ta='شكل مغلق ثنائي الأبعاد بقطع مستقيمة متصلة', k='def'),
    dict(t='All sides and angles are equal', ta='كل الأضلاع والزوايا متساوية', k='fam'),
    dict(t='A corner caves inward', ta='زاوية تنغرز للداخل', k='fam'),
    dict(t='(n − 2) × 180°', ta='(ن − ٢) × ١٨٠°', k='sum'),
    dict(t='Any inside-to-inside segment stays inside the shape', ta='أي قطعة بين نقطتين داخليتين تبقى بالداخل', k='fam'),
    dict(t='A hexagon’s interior angles total 720°', ta='مجموع زوايا السداسي ٧٢٠°', k='sum'),
    dict(t='No two sides lie on the same line', ta='لا يقع ضلعان على نفس الخط', k='def'),
    dict(t='A pentagon’s interior angles total 540°', ta='مجموع زوايا الخماسي ٥٤٠°', k='sum'),
   ]),
 quiz=[
  dict(q='A polygon must be a closed figure made of:', a='يجب أن يكون المضلع شكلاً مغلقاً مكوَّناً من:',
       o=['Curved lines only','Connected straight line segments','Dots with no lines','Any shape at all'], c=1),
  dict(q='Which of these is NOT allowed in a polygon?', a='أي مما يلي غير مسموح في المضلع؟',
       o=['Straight sides','A closed outline','Two sides lying on the same line','Connected endpoints'], c=2),
  dict(q='In a regular polygon:', a='في المضلع المنتظم:',
       o=['Only the sides are equal','Only the angles are equal','All sides and all angles are equal','Nothing needs to be equal'], c=2),
  dict(q='In an irregular polygon, the sides and angles are:', a='في المضلع غير المنتظم، الأضلاع والزوايا:',
       o=['All equal','Different','Always curved','Not connected'], c=1),
  dict(q='In a convex polygon, a line segment between two interior points:', a='في المضلع المحدّب، أي قطعة بين نقطتين داخليتين:',
       o=['Always crosses an edge','Stays entirely inside the shape','Is always curved','Cannot be drawn'], c=1),
  dict(q='A non-convex polygon has at least one corner that:', a='المضلع غير المحدّب فيه زاوية واحدة على الأقل:',
       o=['Points straight up','Caves inward','Is exactly 90°','Is missing'], c=1),
  dict(q='The sum of the interior angles of a polygon is found using:', a='مجموع الزوايا الداخلية للمضلع يُحسب باستخدام:',
       o=['n × 180°','(n − 2) × 180°','n ÷ 180°','(n + 2) × 180°'], c=1),
  dict(q='What is the sum of the interior angles of a hexagon (6 sides)?', a='ما مجموع الزوايا الداخلية للسداسي (٦ أضلاع)؟',
       o=['360°','540°','720°','900°'], c=2),
  dict(q='What is the sum of the interior angles of an octagon (8 sides)?', a='ما مجموع الزوايا الداخلية للثماني (٨ أضلاع)؟',
       o=['720°','900°','1080°','1260°'], c=2),
  dict(q='To find each angle of a regular polygon, you divide the angle sum by:', a='لإيجاد زاوية واحدة من مضلع منتظم، نقسم مجموع الزوايا على:',
       o=['2','The number of sides','180','360'], c=1),
  dict(q='Each interior angle of a regular pentagon measures:', a='قياس الزاوية الداخلية الواحدة للخماسي المنتظم:',
       o=['72°','90°','108°','120°'], c=2),
  dict(q='Each exterior angle of a regular polygon is found using:', a='الزاوية الخارجية الواحدة للمضلع المنتظم تُحسب بـ:',
       o=['360° ÷ n','180° ÷ n','(n − 2) × 180°','n × 90°'], c=0),
  dict(q='Each exterior angle of a regular hexagon measures:', a='قياس الزاوية الخارجية الواحدة للسداسي المنتظم:',
       o=['45°','60°','72°','90°'], c=1),
  dict(q='A polygon with an angle sum of 1080° has how many sides?', a='المضلع الذي مجموع زواياه ١٠٨٠° له كم ضلعاً؟',
       o=['6','7','8','9'], c=2),
 ]))
