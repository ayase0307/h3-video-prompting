# 情境庫 B：產品、品牌、介面、文字

每個情境：優先順序 → 必寫 → 範本片段 → 坑。

## B1. 極簡產品 hero（有產品圖，I2VA / Ref2VA）

優先：產品幾何 → 材質 → hero 光 → 克制的動作。
必寫順序：產品、一個動作、鏡頭、光、聲音、保留清單。
```text
The matte-black wireless speaker from the reference image sits on dark stone. A narrow warm highlight travels across the fabric grille as the unit rotates about 30 degrees. Locked macro, then a slow push in on an 85mm, studio commercial lighting, deep blacks, controlled speculars. Soft mechanical whoosh and low room tone only. Preserve the exact silhouette, button layout, logo position, and material; no hands, no extra devices, no captions, no music.
```
安全首選動作：slow push in、小幅 arc、高光掃過表面、蒸氣/雨/塵當副動作。
坑：第一次就讓手進來、開箱重建產品、orbit+zoom+crane 五秒內、爆炸與群眾；標籤文字靠生成（後製疊字才穩）。
素材規則：一個產品、素背景、logo 面向鏡頭、裁掉其他 SKU 與手、比例與輸出一致。

## B2. 產品揭露 / 開箱 / 使用示範

優先：清楚 > 電影感；一次一個功能；手與產品接觸保留。
```text
[0–3s] The product begins upright and stationary at center. Slow push in. Small highlights travel across the surface.
[3–6s] A hand enters from frame right, grips the product securely, lifts it, and rotates it about 30 degrees until the front label faces camera.
[6–8s] Cut to a static close-up of the label. The hand tilts the product slightly toward the light, keeping the label square to camera.
Camera: slow dolly in, hard cut at 6 s to a locked close-up, no handheld. Audio: quiet studio room tone, one contact sound as the hand picks up the product, one restrained tonal hit on the close-up, no music. Constraints: product geometry, label, colors, proportions unchanged; no additional text, logos, products.
```
開箱：top down static, close on hands；`Satisfying paper crinkling and gentle tapping sounds`。
坑：鏡頭遮住功能；同時示範兩個功能；拆解時部件數量不守恆。

## B3. 產品物理 / 液體 / 食物

優先：材質狀態與因果。
必寫：`First the stream hits the cap, then water sheets down the faceted sides and splits at each edge, as droplets scatter onto the stone.`；食物：蒸氣、油、凝結水、脆皮、醬汁黏度；動作接聲音（切、滋滋、倒）；食物幾何在切鏡間穩定。
坑：要求複雜流體 + 手部互動 + 慢動作同時；「realistic physics」形容詞。

## B4. 品牌片 / 上市影片（15–30 s，多 shot）

優先：品牌事實 → 使用情境 → 證明 → 收尾 CTA。
必寫：15 s 5–8 個 beat、30 s 8–12 個；每 beat 一個主動作、一個視覺負責者、可讀停留（copy hold）、進出轉場、色彩狀態；2–3 個高能量峰 + 煞車段；只用授權 logo/文字並逐字打出；轉場靠產品/游標/UI/光線/幾何匹配驅動。
15 s 節奏：brand hook → 使用者意圖 → 產品機制 → 能力/情境 → 產出/證明 → 產品 payoff → logo + CTA。
坑：假 HUD、隨機玻璃卡片、文字牆、未驗證數字、每個轉場同樣緩動；快而亂 → 減少同時動作、指定視覺負責者；順但慢 → 縮短 hold、重疊轉場、只在關鍵訊息煞車。

## B5. 時尚 / 美妝

優先：臉與服裝一致 → 允許的服裝運動 → 光合乎物理。
必寫：鎖版型、顏色、配飾數量、髮型；`fabric moves gently in the wind while the lettering follows the folds and remains legible`；表演態度（`stylish passerby caught by chance, walking, turning, swinging arms naturally`、`adjusts her glasses, lifts her chin`）；快切時尚片用 `hard cuts only, no fades`。
美妝應用：中景微笑 → 近景拿產品 → 極特寫塗抹 → macro 產品定格；`Locked-off tripod shots, shallow depth of field`。
一鏡換裝：`the outfit seamlessly morphs into …`，鏡頭 `smooth tracking backward matching her walking pace, single uninterrupted take`，AVOID `cuts, inconsistent facial identity, warped architecture`。
坑：極端運鏡時臉漂；濾鏡感皮膚。

## B6. Logo sting / 片頭字卡 / 動態文字

優先：字逐字正確 → 一次出現一次 → 轉場為事件。
```text
[0–2s] Black background. Fine white strokes progressively reveal the supplied mark from left to right.
[2–4s] The linework resolves into the complete solid mark while the camera performs an extremely subtle push in.
[4–5s] Hold on the completed mark.
Audio: a restrained low-frequency synth swell builds during the reveal and ends with a soft percussive impact as the mark completes.
Constraints: do not change the geometry of the supplied mark; no gradients, extra symbols, additional text, glow, particles.
```
片頭字幕（官方 noir 例）：`Each role and each name appears once only; do not repeat a job title, do not assign multiple roles to one name; do not add Chinese, garbled text, or misspellings`；轉場列舉具體物（vinyl-record wipe、car-door cut、long shadow wipe、red-line slice、letter mask、split-screen reconfiguration）並「all land on the drum hits, no soft dissolves」；文字入場方式 `resolve from soft blur into sharp focus over 0.3–0.5 s; no spins, bounces, or large fly-ins`。
坑：字沒打出來；文字被要求做太多動效。

## B7. UI / 網頁 / App 動效 / 遊戲選單

優先：UI 幾何鎖定 → 互動順序 → 文字逐字 → 狀態變化。
必寫：`Animate the website UI: the headline slides down into place, the copy panel slides up, and the car's lights shift from dark to red.`；互動是動詞（scroll、hover scale-up、colour inversion、selector cycles、panel slides in from the right、CONFIRM CONFIG flashes; click it; all panels collapse inward）；UI 需要螢幕鎖定就明說 `screen-locked, does not drift with camera perspective`；選單文字全部打出（`START NEW GAME, CONTINUE (highlighted), SETTINGS, EXIT GAME`）。
遊戲角色裝備 UI（官方 15 s 例）分時：0–2 s 選單出現與游標選擇 → 2–4 s 推向手臂、面板滑入、機械手重組 → 4–7 s arc 到左臂、裝備格切換、部件逐段拆換 → 7–8.5 s 確認、面板收攏 → 8.5–10 s loading bar → 10–15 s 世界載入、第三人稱、HUD 淡入。
坑：邊緣變形；文字亂碼；同時太多面板動。

## B8. 電商帶貨 / 產品在手

優先：產品與手接觸 → 中近景 → 一次一個賣點。
```text
A hand holds a small amber glass serum bottle against a plain warm wall, turning it slowly so the light moves across the label. Extreme close-up on an 85mm lens, static camera, soft diffused daylight from the left, shallow depth of field. Quiet room tone, no music. Vertical framing.
```
坑：一句台詞 + 三個動作 + 兩個產品。

## B9. 硬體 / 工業 / 機器人 / 具身智能

優先：結構尺寸與部件數 → 關節範圍 → 操作順序 → 接觸受力 → 安全邊界 → 完成狀態。
必寫：`focus on joint motion, grip contact, force feedback, and safety margins`；部件數量守恆；操作按順序寫成動詞鏈；環境反饋（物件位移、聲音）；結束在明確完成狀態。
坑：機構被當成流體變形；跳步。

## B10. 建築 / 旅遊 / 飯店

優先：空間連續。
必寫：先外景再內景；運鏡尊重房間幾何；不穿牆瞬移除非風格化轉場；光線時間一致。
坑：鏡頭穿過牆壁；房間布局在切鏡間變。
