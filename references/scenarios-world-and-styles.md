# 情境庫 C：環境、載具、動物、風格化、VFX、循環

每個情境：優先順序 → 必寫 → 範本片段 → 坑。

## C1. 空鏡 / B-roll / 建立鏡頭

優先：一個物理變化 + 一個結尾狀態；光與材質描述取代形容詞。
```text
Wide coastal fishing town at golden hour. Small working boats sit in a sheltered harbor. Low warm sunlight enters from frame left, creating long shadows across the waterfront. Light atmospheric haze over distant buildings. Natural documentary colour rather than saturated travel-ad grading. First a gull lifts off a mooring post, then the water surface breaks into small ripples, as a single boat engine starts and the bow swings toward the harbor mouth. Slow pedestal up with small amplitude. Sound: gulls, water lapping on hulls, one outboard engine starting, no music.
```
坑：只有形容詞（「stunning, epic」）；沒有任何事件 → 12 秒緩推靜物。

## C2. 自然 / 天氣 / 時間變化

優先：環境動態的因果。
必寫：`cloud shadows move across the valley from left to right, then a wind gust bends the foreground grass, as a thin mist thickens in the far treeline`；霧、雪、雨、光束中的塵；慢動作/延時要明說（`slow motion / real time / timelapse`）。
坑：慢鏡頭配大量高熵粒子；「realistic weather」。

## C3. 動物 / 寵物 / 野生動物紀錄片

優先：步態與觸地 → 環境回應 → 紀錄片鏡頭克制。
```text
Low-angle wildlife documentary shot beside a shallow forest stream. A red fox steps cautiously onto a wet rock, shifts its weight forward, then jumps to the opposite bank; its paws displace moss and small droplets on landing. Ferns move gently in the breeze and the stream flows consistently around stones. The camera remains mostly static with a subtle telephoto adjustment. Overcast morning light. Sound: stream, one small splash, birds; no music.
```
擬人 / 換人成動物（官方 capybara 例）：`Match the action in Video 1 from a locked-off wide camera. Replace the three suited men with three photoreal capybaras. Preserve the original movement path exactly: … Keep the camera fixed and integrate fur, lighting, and shadows realistically.`
毛皮：`fur ruffles in the wind`、`breath visible`。
坑：人類動作套到四足漂；多隻動物同時複雜互動。

## C4. 車輛 / 機車 / 追逐 / 空拍

優先：持續前進的速度感 → 每段一個機位 → 重量與物理回饋。
```text
Exactly two racers on two motorcycles along a wet coastal road at dusk, liveries in matte black and signal yellow, no other vehicles. Continuous forward velocity throughout: rear tracking, then side parallel, then a low-angle finish as the leading bike drifts through the final bend. Water spray, sparks off the footpeg, real weight in the lean. Audio: engine load, tyre hiss on wet tarmac, wind buffet, no music. No slow motion interruptions, no subtitles.
```
甩尾（H3 Max 例）：`0-3s: tires screech as he yanks the handbrake into a 180-degree drift, sparks off the rear bumper against a pillar. 3-6s: the camera whips into a barrel-roll orbit around the spinning car. 6-9s: the car snaps straight and launches through the exit ramp, tires smoking.`
空拍：`high-angle drone tracks the convertible along the coastal highway`；`drone skim into vertical launch`。
坑：車輛數量不寫死會多車；「fast」沒有物理回饋；同一 shot 三個機位。

## C5. 手機偽紀實 / 路人拍到

優先：設備真實感 → 荒謬事件一本正經。
必寫：`continuous single-take, authentic smartphone footage accidentally captured by a passerby, overcast daylight, subtle handheld shake, limited stabilization, occasional autofocus adjustment, realistic smartphone compression; filmed with a completely serious, unscripted documentary feeling`；分時寫事件升級。
坑：加了電影光影；配樂。

## C6. 2D anime

優先：風格用參考圖錨定 → 描述繪製方式不描述類型 → 一 shot 一個 held beat。
```text
@Rin in the school rooftop scene, 2D anime, flat cel shading with two-tone shadows and clean dark linework. Medium shot. She leans on the railing, wind lifts her hair once, she turns her head toward the camera and smiles. Late afternoon sun, long soft shadows, no lens blur. Sound: distant traffic, a single gust, her small laugh at the end.
```
負向只放 3–4 個（`photorealistic skin, 3D render lighting, lens blur`）。先出靜圖確認風格再生影片。
坑：每個 prompt 重述角色外觀（與參考互搶 → 臉變）；「volumetric god rays, shallow DOF」拉向 3D；一個 clip 三個動作。

## C7. 3D 卡通 / Pixar 風 / 遊戲 CG

優先：角色比例與材質一致 → 清楚剪影 pose → 彈性表演 → 環境美術穩定。
必寫：`high-energy poses, clear line of action, forward lean, strong anticipation, fast but readable timing, elastic body mechanics, vivid micro-expressions`；近景/特寫與其他景別交替；荷蘭角用於追逐與失衡；每秒指令要有動作/鏡頭/位置/聲音/交接。
仙俠 3D（官方例）：`Show the face only in close-up or extreme close-up. In wide shots use back view, rear three-quarter view, or empty environment; never a distant frontal face.`
坑：寫實肌肉感；面部在遠景。

## C8. 黏土 / 定格 / 紙藝 / 拼貼 / 毛氈

優先：材質邏輯 → 步進動作 → 觸感音效。
必寫：`claymation, visible fingerprints, matte surface, miniature depth cues`；`stop-motion stepping rather than fluid motion`；紙：`layered paper edges, cut marks, tabs, folds; animate placement, tearing, sliding, layering; halftone texture`；音效：紙摩擦、布料、桌面輕敲；預設不加 BGM 除非要求。
官方黏土例：`A fox sprints to the cliff edge and launches without hesitation, a dramatic heroic leap in slow motion over a lava canyon. Midair, the camera races beneath the fox's belly, revealing the depth of the chasm and the fully extended clay body.`
坑：混入寫實光影；流體般的平滑動作。

## C9. 手繪發光 + 實拍融合

優先：實拍層與手繪層的邊界 → 線條與實體表面互動 → 手機一手拍。
必寫：實拍場景固定物件清單；手繪線材質（`apricot-orange glowing crayon-chalk line`）；連續變形鏈（車票→紙燕→毛毛蟲→箭頭→小帆船…）首尾相連；鏡頭慢半拍追、先拍空掌再匆忙右晃；每段末寫「反向」（不要立體 CG、不要恐怖化、不要新角色、不要切到別的場景）；聲音只有室內音、布料、杯子、電子音與小生物聲。
坑：線條變成 3D；平穩廣告式構圖。

## C10. 動態圖形 / 拼貼片頭 / 大字幕

優先：時間切片 → 每段一個圖形事件 → 轉場落在鼓點 → 文字白名單。
必寫：`linework appears over black, split-screen boundaries snap into place, colour blocks assemble piece by piece`；`credits slide, pop, reveal through masks on the beat`；`no soft dissolves or fluid morphs`；配樂進入時間點；每個字出現一次。
大字幕 MV 五行模板見 `rhythm-and-pacing.md` §4。
坑：字重複、拼錯、多角色同名；轉場寫成「炫酷」。

## C11. 變身 / 生物 / 幻想 VFX

優先：初始形態 → 有序變化 → 保留的身份特徵 → 材質與光互動 → 穩定的最終形態。
必寫：`describe ordered changes; state which identity traits remain; land on a stable final form`；VFX 的材質（`translucent blue water trails, glowing fire`）與對環境的影響（`shockwave of smoke and debris`）；鏡頭保持可讀（wide 或 static）。
一鏡換裝 / 無縫變形：`the outfit seamlessly morphs into …`、`No tearing, black frames, hard cuts, obvious VFX, or compositing seams`。
坑：變形中身份全掉；鏡頭跟著亂。

## C12. 無縫循環 / 網頁首屏動畫

優先：鎖定參考 → 循環動作 → 結尾回到開頭。
社群結構：`[LOCK] Render exactly as @image1. Do not alter hair, bangs, eye colour, coat silhouette, …` → `[LOOP] A perfect cycle: …` → `[CAMERA] completely static` → `[AUDIO]`。
必寫：`End on a frame that matches the opening to allow a seamless loop`；靜態相機；動作幅度小且週期明確（呼吸、髮絲、火焰、雲）。
坑：首尾同圖但尾幀漂（官方回覆：模型會補動作，寫回到原姿勢的路徑，接受後製裁切）。

## C13. 角色設定板 / 角色介紹（aimikoda 兩段式）

板動畫：`Animate the existing static board itself while preserving the exact composition, panel positions, design, palette, and solid off-white background. Camera completely static. Portrait: subtle head turns, gaze changes, breathing, blinking; not a single idle loop. Full-body panels: smooth 360-degree turn in place, like a turntable. Environment panels: small natural actions appropriate to each scene. Do not rearrange panels, expand scenes beyond frames, add elements, duplicate characters.`
角色介紹：同一板當「reference only, do not animate the board itself」，依序：肖像活過來 → 三個全身 pose 短拍 → 三個環境場景 cinematic shot；`elegant camera movement, minimal typography, no redesign`。
坑：把板同時當畫面與參考。

## C14. 綠幕 / 場景替換 / 重打光

見 `references-and-editing.md` §5：`Remove the green-screen background of Video 1 and replace it with … Make every background element respond correctly to the subject's movement, and relight the subject so they blend naturally.`；日轉夜：`Change the lighting from daytime to night; keep geometry and camera the same; birdsong becomes crickets.`

## C15. 多素材電影混剪

優先：素材分工 → 節奏來源 → 每段一個主視覺。
必寫：`Use Images 1–6 as assets. Match Reference Video 1 closely for shot rhythm, transition language, and music.`；圖對應鏡頭順序（`Use Image 1 for storyboard order and pacing`）；`Follow the storyboard beat by beat, with natural camera movement and seamless transitions — never a slideshow`。
坑：六張圖輪播成幻燈片 → 加因果橋（上一鏡末動作接下一鏡首動作）。
