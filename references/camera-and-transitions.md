# 鏡頭語言與轉場

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
角度：`eye level`（誠實）、`low angle`（主體變大）、`high angle`（主體變小、看清桌面）、`top down`（開箱、平拍）。

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
