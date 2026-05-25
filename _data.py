TITLE = '姿勢チェッカー【無料】猫背・巻き肩・骨盤診断'
DESCRIPTION = '日常の姿勢習慣から猫背・巻き肩・骨盤傾きをセルフチェック。悩み別の改善エクササイズとストレッチをご案内します。'
DESCRIPTION_SHORT = '猫背・巻き肩・骨盤の歪みをセルフチェックして改善アドバイスを取得...'
COLOR1 = '#F5F3FF'
COLOR2 = '#EDE9FE'
COLOR_BTN = '#7C3AED'
FOOTER_LINKS = [('https://appadaycreator.com/sleep-quality-checker/', '睡眠の質チェッカー'), ('https://appadaycreator.com/back-pain-checker/', '腰痛リスクチェッカー'), ('https://appadaycreator.com/stretch-timer/', 'ストレッチタイマー')]

CUSTOM_CSS = ""

MAIN_HTML = """<div class="card" id="quiz-start">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:12px;">🧍 姿勢セルフチェック</h2>
  <p style="color:#666;font-size:14px;margin-bottom:8px;">6つの質問で猫背・巻き肩・骨盤の歪みを診断します</p>
  <ul style="font-size:13px;color:#94a3b8;margin:0 0 16px 16px;"><li>所要時間：約1分</li><li>登録不要・無料</li></ul>
  <button class="btn" onclick="startQuiz()">チェックスタート →</button>
</div>
<div id="quiz-area" style="display:none;">
  <div style="font-size:12px;color:#999;margin-bottom:4px;">質問 <span id="q-num">1</span> / 6</div>
  <div style="height:4px;background:#e5e7eb;border-radius:2px;margin-bottom:16px;">
    <div id="q-bar" style="height:100%;background:#7C3AED;border-radius:2px;transition:width .3s;width:16.7%;"></div>
  </div>
  <p id="q-text" style="font-size:16px;font-weight:600;margin-bottom:16px;"></p>
  <div id="q-options"></div>
</div>
<div class="result" id="result">
  <div class="card">
    <h3 id="r-title" style="font-size:18px;font-weight:700;color:#7C3AED;margin-bottom:8px;"></h3>
    <div id="r-problems" style="margin-bottom:12px;"></div>
    <div style="background:#F5F3FF;border-radius:10px;padding:14px;font-size:13px;line-height:1.9;" id="r-advice"></div>
    <button class="btn" style="margin-top:16px;" onclick="location.reload()">もう一度チェック</button>
  </div>
</div>"""

JS_CODE = """const QS=[
  {{text:'Q1. 長時間パソコン・スマホを使いますか？',opts:['ほぼ使わない（1時間未満）','2〜4時間程度','5〜7時間','8時間以上']}},
  {{text:'Q2. 椅子に座ったとき、背もたれを使いますか？',opts:['常に背筋を伸ばして使う','時々もたれる','ほぼ常にもたれている','前傾みで背もたれを使わない']}},
  {{text:'Q3. 鏡で横から見たとき、耳・肩・股関節が一直線になっていますか？',opts:['まっすぐだと思う','少し前に出ている','明らかに前に傾いている','確認したことがない']}},
  {{text:'Q4. 肩こり・首こりはありますか？',opts:['ほとんどない','たまにある','慢性的にある','常に痛みがある']}},
  {{text:'Q5. 立ったとき、お尻が後ろに突き出ている感じや、腰が反り過ぎる感じがありますか？',opts:['ない','少し気になる','よく言われる','腰痛持ちでもある']}},
  {{text:'Q6. 靴底の減り方は？',opts:['均一に減る','外側がよく減る','内側がよく減る','前の方だけ減る']}},
];
let cur=0; const ans=[];
function startQuiz(){{cur=0;ans.length=0;document.getElementById('quiz-start').style.display='none';document.getElementById('quiz-area').style.display='block';renderQ();}}
function renderQ(){{
  const q=QS[cur];
  document.getElementById('q-num').textContent=cur+1;
  document.getElementById('q-bar').style.width=((cur+1)/QS.length*100)+'%';
  document.getElementById('q-text').textContent=q.text;
  document.getElementById('q-options').innerHTML=q.opts.map((o,i)=>`<button onclick="answer(${{i}})" style="width:100%;padding:12px;margin-bottom:8px;border:2px solid #e5e7eb;border-radius:10px;font-size:14px;cursor:pointer;background:#fff;text-align:left;">${{o}}</button>`).join('');
}}
function answer(idx){{ans.push(idx);cur++;if(cur>=QS.length)showResult();else renderQ();}}
function showResult(){{
  const score=ans.reduce((s,a)=>s+a,0);
  let title,problems=[],advice;
  if(score<=3){{title='✨ 良好な姿勢タイプ';advice='姿勢バランスは良好です！現在の習慣を維持しながら、30分に1回は席を立つ・胸を開くストレッチを取り入れて予防しましょう。';}}
  else if(score<=8){{
    title='😐 軽度の姿勢崩れタイプ';
    if(ans[0]>=2) problems.push('長時間のデバイス使用による前傾姿勢');
    if(ans[3]>=2) problems.push('慢性的な肩こり・首こり');
    advice='【改善エクササイズ】①壁立ち：後頭部・肩・お尻・かかとを壁につけて30秒キープ ②胸張りストレッチ：両手を後ろで組み胸を開く ③あご引き：あごを引いて首の後ろを伸ばす（各10回×3セット）';
  }} else if(score<=14){{
    title='⚠️ 猫背・巻き肩タイプ';
    problems.push('猫背・巻き肩の傾向あり');
    if(ans[4]>=2) problems.push('腰椎前彎（反り腰）の可能性');
    advice='【重点改善】①肩甲骨寄せ：胸を張り肩甲骨を中央に寄せて5秒キープ（10回） ②タオルストレッチ：タオルを両手で持ち上げ・後ろへ ③ドローイン：息を吐きながらお腹を凹ませ5秒キープ。デスクワーク中のモニター高さ調整も重要です。';
  }} else {{
    title='🔴 姿勢改善が急務なタイプ';
    problems.push('複合的な姿勢問題（猫背＋骨盤歪み）');
    advice='【専門家相談推奨】複数の姿勢問題が重なっています。整体・整形外科での診断を推奨します。日常では①座り姿勢を15分に1回リセット ②スマホを目の高さに ③硬めのマットレスで就寝 ④腹筋・背筋のバランストレーニングを開始しましょう。';
  }}
  document.getElementById('r-title').textContent=title;
  document.getElementById('r-problems').innerHTML=problems.map(p=>`<span style="display:inline-block;background:#7C3AED20;color:#7C3AED;padding:4px 10px;border-radius:20px;font-size:12px;margin:2px;">${{p}}</span>`).join('');
  document.getElementById('r-advice').innerHTML=advice.replace(/【/g,'<strong>【').replace(/】/g,'】</strong>');
  document.getElementById('result').classList.add('show');
  document.getElementById('quiz-area').style.display='none';
  document.getElementById('result').scrollIntoView({{behavior:'smooth'}});
}}"""

FAQ = [
    ("姿勢チェッカーは無料で使えますか？", "はい、完全無料・登録不要でご利用いただけます。"),
    ("チェック結果は医療的診断として使えますか？", "本ツールはあくまで日常習慣に基づくセルフチェックです。腰痛・肩こりが重度の場合や長期間続く場合は、整形外科・整体院への受診をおすすめします。"),
    ("姿勢改善にどのくらい時間がかかりますか？", "日常的な意識と改善エクササイズを続けることで、2〜4週間で変化を感じる方が多いです。長年の習慣による姿勢崩れは数ヶ月かかることもあります。"),
    ("猫背とストレートネックは別の問題ですか？", "関連していることが多いです。猫背になると頭が前に出てストレートネック（スマホ首）になりやすくなります。本チェックで両方を評価します。"),
    ("毎日続けてチェックするのが効果的ですか？", "週1〜2回のセルフチェックで変化を追うことをおすすめします。改善エクササイズの継続が重要です。"),
]

HOW_TO = [
    "「チェックスタート」ボタンをクリックする",
    "6つの質問に素直に答える（スクリーン使用時間・座り方・鏡チェックなど）",
    "すべての質問に答えると診断結果が表示される",
    "姿勢タイプと具体的な改善エクササイズを確認する",
    "毎日改善エクササイズを実践して姿勢を改善する",
]

