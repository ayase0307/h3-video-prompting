# 鏡頭語言與轉場

> 17 式運鏡骨架、實測狀態與「場景意圖→運鏡」選用指南見 [camera-moves-handbook.md](camera-moves-handbook.md)。

來源：官方 base-en.txt 4.2–4.3；minimax3.com 20 種官方運鏡整理；videoai.me 鏡頭語言；官方飛書手冊（環繞寫法、切鏡風格）；fal.ai 44 例；Kapwing；reAPI。

## 1. 每個 shot 一個運鏡，寫成動作，帶落點

H3 沒有鏡頭控制介面，全靠文字。三個習慣決定成敗：

1. **用官方 20 個詞**，不要自創（「camera moves left」不在詞彙裡，模型要猜是 pan 還是 truck）。
2. **給落點**：官方每個範例都以「toward the folded letter」「revealing the open doorway」「as the runner exits the frame」結尾。只給方向不給落點，鏡頭會飄或幾乎不動。
3. **寫在動作句裡**，不要堆在句尾當標籤（`, cinematic, pan right, 4k` 會被當裝飾）。

```text
The camera pushes in with small amplitude at slow speed toward the folded letter in her hands.
The camera pans right with large amplitude at fast speed, revealing the open doorway.
The camera holds a static shot as the runner exits the frame.
```

## 2. 官方 20 種運鏡

| 類型 | 寫法 | 說明 |
|---|---|---|
| Zoom In / Out | `The camera zooms in/out` | 焦距變、機身不動 |
| Push In / Pull Out | `The camera pushes in / pulls out` | 機身前後移動；與 zoom 視差不同 |
| Pan Left / Right | `The camera pans left/right` | 原地水平轉 |
| Tilt Up / Down | `The camera tilts up/down` | 原地垂直轉 |
| Truck Left / Right | `The camera trucks left/right` | 整台橫移；要視點移動用這個不用 pan |
| Pedestal Up / Down | `The camera pedestals up/down` | 整台升降 |
| Arc Shot | `The camera arcs around the subject` | 弧形繞行 |
| Tracking Shot | `The camera tracks the subject` | 跟隨移動主體 |
| Static Shot | `The camera holds a static shot` | 不動 |
| POV | `The camera holds the subject's point of view` | 主觀鏡頭 |
| Roll CW / CCW | `The camera rolls clockwise/counterclockwise` | 沿鏡軸旋轉 |
| Shake Slightly / Strongly | `The camera shakes slightly/strongly` | 手持抖動 |

修飾：`with small amplitude / with large amplitude`、`at slow speed / at fast speed`。中等幅度與正常速度省略不寫。Static、POV、Shake 不加修飾。

**環繞**：官方手冊建議寫 `truck left + pan right`（或反向），不要直接寫 orbit / 環繞；社群自然語言模式 `slow orbit` 對產品可用，對人臉風險高。

## 3. 景別、鏡頭、角度（自然語言模式）

| 景別 | 用途 |
|---|---|
| Wide | 交代環境、生活風格 |
| Medium（腰上） | 拿產品說話的主力 |
| Medium close-up（胸上） | UGC 預設，看得到表情也看得到手 |
| Close-up | 情緒、產品細節 |
| Extreme close-up | 材質、標籤；對白弱 |

鏡頭：`35mm`（環境感、手持 UGC）、`50mm`（中性預設）、`85mm`（壓縮、淺景深、產品與人像）、`anamorphic`（廣告感橫向光暈）。
角度：`eye level`（誠實、對峙）、`low angle`（主體變大、支配）、`high angle`（主體變小、審視）、`top down`（開箱、佈局）。這些是慣例不是公式，要看人物關係；**同一個 shot 只寫一個角度**；俯拍是角度不是運鏡（見 §9）。
鏡頭壓縮感寫成拍攝距離，例如 `shot on an 85mm lens from far away, the background compressed into soft color blocks`，不寫公尺數。

官方純文字模式建議分層：「大全景交代空間 + 中景承載動作 + 特寫強調細節」。

## 4. 各類型的預設鏡頭

| 情境 | 鏡頭 |
|---|---|
| 對白 / talking hook | static 或 handheld slight sway、MCU、eye level；鏡頭動作會跟台詞搶注意力 |
| 產品揭露 | low angle slow push in |
| 開箱 / 示範 | top down static，close on hands |
| 生活風格 / 品牌 | wide settling to medium, slow pull back |
| 走路 hook | handheld selfie framing with natural walking movement |
| 材質特寫 | static 85mm，側光掃過 |
| 打鬥 | 鏡頭比身體簡單：一個 tracking 或 static；切點對衝擊 |
| 跑酷 / 極限 | handheld tracking 跟動量、極低與極高角度、切點對落地 |
| FPS / 遊戲實機 | first-person eye level handheld，`subtle player-driven sway`，開火 `light recoil`，不切第三人稱 |
| UGC | `a small amount of natural sway`；不要寫 shaky（會過度） |
| 慢動作 | static 或 small slow push in |

## 5. 切鏡：每次 cut 要帶新資訊

- 官方切鏡動詞：`the camera cuts to`、`the shot cuts to`、`the shot transitions to`、`the shot changes to`、`the shot switches to`；cross-dissolve / fade / wipe 只在使用者要求時用。
- 新資訊 = 主體、空間、狀態、視角、時間。只是換距離或微調角度 → 用運鏡不用切。
- 切到什麼景別、哪個角色，寫清楚：`the shot cuts to a close-up of the woman in the navy blazer from Shot 1`。
- **Match on action**：前一個 shot 收在動作中段，下一個 shot 從同一動作的後半開始，例如 `… ending as the sword reaches shoulder height.` → `[Shot 3] At 00:05.000, the shot cuts to a close-up as the blade completes its downward stroke …`
- **畫面方向一致（180 度線）**：主體在 Shot 1 由左往右跑，切鏡後仍寫 `moving from frame left to frame right`；兩人對峙時誰在左、誰在右全片不換。要反轉方向就先給一個看得到的轉折（主體轉身、攝影機在畫內越線），不要靠切鏡跳軸。壞掉長怎樣：追逐像在往回跑、兩人好像換了位置。〔方法主張：守富提供的 15 秒腳本 system prompt，H3 未 A/B〕
- 相鄰 shot 怎麼差才不單調：見 `shot-variety-and-staging.md` §3。
- 切鏡風格（官方手冊）：普通切、疊化、隨節奏卡點切、快切。預設會切鏡；要一鏡到底必須明說並全文不出現 `[Shot 2]`。

## 6. 轉場寫成「事件」，不寫效果名

fal.ai 與官方範例：轉場靠描述觸發物落地。

```text
fast binocular-scan transitions with whip movement, motion blur, optical smearing, and
brief exposure flicker. Cut at peak blur, then settle and snap back into focus.
```

可用的觸發物：遮擋（手、扇面、門）、甩動、閃白、材質匹配（咖啡泡沫 → 沙丘）、動作匹配、UI 收攏、物體變形、聲音重拍、圓形唱片遮罩、車門直切、長影掃屏、紅線切割、巨型字母遮罩、分屏重組、色塊硬切。
禁止語：「炫酷轉場」「絲滑轉場」。

一鏡到底的物理轉場（官方 coffee→desert 範例）：`At the exact moment when the cocoa particles resemble the dune ridges, transition seamlessly … No tearing, black frames, hard cuts, obvious VFX, or compositing seams. One continuous shot with no visible edit.`

## 7. 手持與「不完美」

UGC / vlog / 偽紀實要主動移除精緻感：
`one-handed phone-camera feel with visible shake, exposure fluctuation under fluorescent light, delayed autofocus at close range, slightly coarse noise in the shadows`；
`hesitant close-focus pulls, backlit exposure breathing`；
`the camera lags half a beat behind, films the empty palm first, then swings right`。

## 8. 除錯

- 運鏡被忽略：先改 static 重跑；能動了再加回一個運鏡；仍失敗多半是 prompt 內部矛盾（wide + extreme close-up detail 同句）。
- 鏡頭亂飄：多個運鏡競爭 → 只留一個，其餘改成構圖約束。
- 全身被裁：`The camera pulls out with large amplitude at the same speed as the subject walks forward, maintaining a full-body composition.`
- 想同一 clip 內換方向：切第二個 shot，各自一個運鏡。

## 9. 運鏡動機：先決定「固定、運鏡、切鏡」

第一步，先判斷這個 shot 要交付什麼：
- 要讓觀眾看清表演或時序，用 static。
- 要讓觀眾經歷接近、遠離或揭露，用一個運鏡。
- 要交付新的主體、空間、狀態、視角或時間，用切鏡（見 §5）。

運鏡寫成一條鏈：觸發 → 起點 → 路徑 → 新資訊 → 停點。
When she sees the letter, the camera pushes in with small amplitude at slow speed toward her eyes, stopping on a close-up.

敘事任務對照官方詞（抖音第 4 支 remap）：
| 任務 | 官方寫法 | 要鎖定 |
|---|---|---|
| 聚焦、加壓 | pushes in | 起訖景別、落點 |
| 退回環境、孤獨、揭示空間 | pulls out | 最後露出的環境資訊 |
| 環繞、儀式感 | trucks left while panning right to keep <主體> centered（不寫環繞類詞） | 方向、幅度、主體是否固定 |
| 升高、交代地形 | pedestals up | 起訖高度 |
| 俯拍 | 這是角度，不是運鏡：在景別句寫 high-angle 或 top-down，運鏡另外選一個或用 static | 高度、人物在平面上的走位 |
| 橫向觀察、跟拍 | 視點平移用 trucks left/right，原地轉頭用 pans，跟著移動主體用 tracks | 前景遮擋和視差 |

視差要寫成結果，不要寫非官方詞：
The camera trucks right with small amplitude at slow speed; the foreground leaves pass faster than the distant buildings.

運動放在後段（選用，未實測）：
The camera holds still at first, then pushes in with small amplitude toward …
這仍然是一個運鏡。

## 10. 焦點轉移（rack focus，Colab 已實測通過，見 camera-moves-handbook.md）

- 焦點轉移算該 shot 唯一的鏡頭事件，鏡身寫 holds a static shot，同一 shot 不能再加別的運鏡。
- 起點和終點都要是畫面裡能指認的物件：then the focus shifts from her hand to the distant towers, as her hand softens into a blur。
- 用途：取代反應切鏡，在同一鏡裡完成「看見 → 反應」。
- 失敗時退回 static，改用切鏡交代。

## 11. 攝影機幾何：寫實際位置，不只寫角度標籤

來源：LoveUolanda 方法論第 10–12 點（有成片、無 A/B）。**方法主張，H3 未對照實測。**

「low angle」「close-up」本身不保證拿到正確視角。想控制時，寫攝影機相對於人物的真實空間關係：

- 機位在人物哪裡（左前方、肩後、貼近腳邊）
- 鏡頭中心高度，光軸對準身體哪個部位
- 與人物的距離
- 地面與身體的關係
- 運動路徑（沿什麼方向、跟隨多久）

```text
❌ low-angle close-up of the legs
✅ The camera sits near ground level just ahead of her left foot, aimed at the supporting
   ankle, and trucks left a short distance with small amplitude to follow the step.
```

- 不用數字角度（「30 度」）代替機位。
- 景別決定觀眾讀到哪一部分動作：看承重與轉向就讓腳成為主體；看軀幹扭轉與手臂軌跡，鏡頭不能一直只盯著臉。
- 每個 shot 一個主運動（§1），再讓攝影機反應主體/動作的路徑。每次運動或切鏡都要帶新資訊（揭示支撐點、新輪廓、方向改變、強調衝擊或重拍），不為了「顯得高級」而變化。

## 12. 連續運鏡 vs 離散硬鎖：先選模式，不要混寫

來源：journal 多個案例交叉比對。**同一個 repo 裡的案例互相矛盾，這是目標不同，不是誰對誰錯。**

| 模式 | 何時用 | 寫法 | 來源案例 |
|---|---|---|---|
| 連續物理鏡頭 | 要主體之間的連結、單一長鏡 | 一個連續路徑；轉場用遮擋或前景掠過；全文不出現多個 `[Shot N]` | orbital long take（成片在作者 X 頁，未隨 repo 發布；無 A/B） |
| 獨立蒙太奇 | 音樂驅動的剪輯感 | 每段開在不同局部特寫，硬切落在樂句邊界，每個切點帶新資訊 | wuxia 13 段 |
| 兩態相機（硬鎖 / 瞬間 burst） | 編輯式揭示、節拍重擊 | 只有 HARD LOCK（零運動）與 INSTANT BURST（極短、無緩動）兩態，明寫不混合；衝擊要可數（三下） | snap-lock、song-style（同上）；原文三種模式為獨立蒙太奇／連續物理鏡頭／分組一鏡到底，兩態相機出自 snap-lock |

規則：同一段 prompt 只選一種；跨段要換模式須明寫。同一份 prompt 不能同時寫「一鏡到底」又寫硬切，也不能同時寫連續環繞又寫硬鎖（這是 Red flag）。環繞要照本檔 §9 寫成 `truck + pan`，不要用 orbit 類詞。

兩態相機的 burst 只有 0.12–0.2 秒，和 H3 cut 誤差（約 0.12 秒）同量級，不可控，也違反「shot ≥ 2 秒」；屬音樂剪輯例外，未實測。

判讀參考影片是連續運鏡還是離散快切時，稀疏抽幀（4 fps）會跨過 0.12–0.2 秒的 burst，要用 8 fps 以上，再用音訊 onset 對帳；切點都掛在節拍上就是剪輯式。
