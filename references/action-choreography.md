# 人物動作：把「動作」寫成 H3 讀得懂的軌跡

來源：官方手冊四、1.2–1.5；Kapwing tip 3/4/7；videotoprompt / morphed 動作範例；AI-KSK camera-action-recipes；Runware 動作遷移指南；MiniMax 官方飛書手冊評論區回覆。

## 1. 動作 = 起始狀態 → 移動 → 結束狀態

短動詞留下太多未定義細節。H3 需要知道哪隻手、碰哪裡、多快、最後停在哪。

```text
❌ the woman picks up the bottle
✅ The bottle begins upright on the counter. She reaches forward with her right hand,
   grips it around the upper third, lifts it smoothly to chest height, and rotates it
   until the front label faces camera.
```

人體動作要給解剖學細節：姿勢、方向、手的用法、視線、重心。

```text
✅ Weight drops onto the left knee, then the torso spirals open, as one arm extends
   and the fabric trails behind the movement.
❌ contemporary dance
```

## 2. 用順序連接詞鎖住節拍順序

`first → then → as → finally`。沒有連接詞，H3 通常把多個事件當成同時發生，結果就是「everything-at-once」的糊片。

```text
First she lifts the cup toward her face, then steam curls upward and catches the
window light, as she pauses and looks out at the street.
```

## 3. 每個 shot 一個主動作

- 一個 6 秒 shot 要角色「進門、坐下、拆包裹、說話、喝水、看窗外、離開」，模型只能壓縮或省略。挑這個 shot 要講的那一個動作，其餘丟到下一個 shot 或下一次生成。
- 「一個主動作」包含它的完整弧線：起手（anticipation）→ 執行 → 接觸/衝擊 → 反應/收勢（settle）。品牌片 skill 的 motion intent 用詞：`setup, anticipation, commitment, impact, brake, settle`。
- 「一個主動作」= 一條完整弧線，可含連貫的子動作：蹬地 → 騰空 → 出手算一個上籃，不是三個動作。子動作之間若各自有獨立的落點（先完成一次交叉換手並站穩，再突破），就拆成兩個 shot。
- 副層動作（頭髮、衣料、背景人物）可以有，但寫成「環境對主動作的反應」，不是另一個動作。

## 4. 環境要「回應」動作

Hailuo 系列對水、布料、頭髮、粒子、衝擊、動量變化特別強。寫因果，不寫「realistic physics」。

```text
Dust lifts from the floor at the landing and trails briefly behind him.
Water sheets down the faceted sides and splits at each edge, as droplets scatter onto the stone.
```

## 5. 打鬥 / 對抗一拍的寫法（AI-KSK fight beat + 社群範例）

每個 shot 只放「一拍」：

1. 建立雙方身體位置與朝向（誰在畫面左、誰在右、距離）
2. 攻擊肢體或武器 + 方向（右手直刺、由上往下劈、左腳側踢）
3. 接觸或格擋（刀鋒碰刀鋒、拳頭打到胸口、被擋開）
4. 反應與恢復（後退兩步、跪倒、重新舉刀）
5. 一個運鏡

```text
[Shot 2] At 00:03.000, the shot cuts to a medium two-shot: the swordswoman stands
frame-left, blade held low; the masked assassin frame-right lunges with a curved knife
aimed at her throat. She rotates her wrist, the flat of her blade meets the knife with
a sharp metallic ring, and the assassin is knocked one step back into a puddle. The
camera trucks right with small amplitude at fast speed to keep both bodies centered.
```

多對一的打鬥：一次只讓一個對手行動，另一個保持可見但靜止（繞位、蓄勢）。三個以上重要角色同框會漂移。

## 6. 慢動作

- 慢動作獨立成一個 shot，開頭就寫 `in slow motion`，不在同一 shot 內「先慢後快」（Contradiction Trap，會出現播放/暫停式卡頓）。
- 降低背景熵：慢動作 shot 裡把大雨改成細雨、狂風改成微風、群眾拿掉。模型需要把生成預算花在主體流暢度。
- 慢動作預期要多抽 3–5 次才會穩定。
- 真正的 speed ramp 用兩次生成 + 剪輯軟體 optical flow 接，不要求 H3 一次做完。

## 7. 一鏡到底 vs. 切鏡

- 一鏡到底：全文一段連續描述，不出現 `[Shot 2]`，靠連續運動、遮擋、材質匹配、空間貫通維持張力。
- 切鏡：每次 cut 要帶來新資訊（主體、空間、狀態、視角、時間）。只是換距離或微調角度 → 用運鏡不用切。
- 切鏡時寫清楚切到「什麼景別」「哪個角色」，幫助跨鏡頭一致性。
- 跨鏡頭因果橋（AI-KSK）：上一鏡最後的動作要能接上下一鏡第一個動作。

```text
摸豬 → 野豬抬頭噴鼻前傾 → 切 → 追逐已經在進行
跑 → 回頭 → 伸手抓鏈條 → 切 → 手完成抓握 → 借力上豬
```

## 8. 用參考影片遷移動作（Ref2VA）

- 「Video 1 只負責動作與時序，Image 1 負責身份與服裝」，並明說不要複製 Video 1 的演員、服裝、場景、燈光、運鏡。
- 給乾淨的參考：素背景、全身入鏡、只含一個動作。臉部表演用緊特寫對緊特寫。
- 身體驅動身體、臉驅動臉才穩；人類舞蹈套到四足動物會漂。
- 參考影片的**聲音**也會被帶進來（女聲笑會變成男角色的笑），要嘛換成匹配的參考，要嘛在 Sound 句明寫想要的聲音。
- 運鏡參考：只描述新主體，不要再用文字描述那個運鏡，否則分不清是文字還是影片在控制。
- 官方例（動作 + 角色）：`圖1的人物動作、表情與表演節奏嚴格參考輸入視頻1`，之後只寫新場景裡發生什麼。

## 9. 角色不說話的正向寫法（MiniMax 官方回覆）

```text
人物全程保持安靜，嘴巴自然閉合，沒有說話或對話，面部只有輕微自然表情。
```

- 補負向：無對白、無人聲、無念白、無口型變化。
- 避免「對著鏡頭、交談、講述、激動表達、嘴唇微動」。
- 給角色持續且明確的動作（專注觀察、低頭閱讀、轉身行走）；「站著看鏡頭」最容易自行補出說話。
- 特寫仍不穩就改側臉、背影或中遠景。

## 10. 身份一致性（動作片特別容易掉）

- 臉在畫面裡越小越難保持。用廣角建立空間，關鍵情緒拍轉中景/特寫。
- 有參考圖時不要在每個 shot 重述外觀，文字和圖片會互相競爭。全局宣告一次不變量，分鏡內只寫新變化。
- 要鎖的東西逐項點名：`Preserve the same facial identity, half-up dark hair, gold hoop earrings, and cream blazer throughout.`
- 要鎖臉時給一張**臉部特寫參考**（Ref2VA：特寫＋全身各一張，寫進同一個 `<Subject>`），不要只靠全身圖當 i2va 首幀：全身圖裡的臉只有幾十像素，中後段眼色等細節會走樣。本機先導實測（n=3, 0.5MP, 6 s）：盲評臉部一致 3/3 勝；混淆是 Ref2VA 臂多了一張特寫，「i2va 首幀＝臉部特寫」沒測，服裝色距離反而 i2va 較近。原始紀錄在私有 repo，未公開。

## 11. 動作鏈十要素（舞蹈、打鬥、運動、特技通用）

本節是 §1 弧線（起手→執行→接觸→收勢）和 `motion-quality.md` §1 的展開版：要檢查哪裡會出錯時用十要素，日常寫 prompt 仍用四段弧線。**預算：每個主動作只挑 2–3 項最容易出錯的要素寫進 prompt（通常是受力/支撐、重心、慣性），不要十項全寫**，否則字數會超過 300–700 的預算。十要素以「有支撐點與重心的身體」為前提，適合人、動物、生物；產品或物件 hero 鏡頭改用 `motion-quality.md` §1 弧線加本檔 §13 的道具軌跡清單。

來源：LoveUolanda〈H3 古風舞蹈創作方法論〉（2026-10-19，MIT 案例庫 LoveRain1997/h3-prompt-journal，有成片但無 A/B）。原文講舞蹈，但「模型要知道人怎麼做出這個動作，而不只是動作叫什麼」套用到任何動作都成立。**方法主張，H3 未做對照實測。**

只寫「完成一個旋轉」「跳起來」「揮劍」太薄。一個主動作用這十項檢查，缺哪項補哪項（不必全寫進 prompt，挑會出錯的）：

| # | 要素 | 範例（旋轉） |
|---|---|---|
| 1 | 起始狀態與受力來源 | 左腳在前、重心壓在前腳，右臂後擺蓄力 |
| 2 | 進入路徑與支撐點 | 以左腳掌為軸 |
| 3 | 重心與身體軸線 | 脊柱保持直立，骨盆先轉 |
| 4 | 動作隨時間的發展 | 先轉髖、再轉肩、最後頭回到定點 |
| 5 | 峰值與重拍完成 | 在重拍或衝擊點完成半圈 |
| 6 | 慣性延續 | 轉完還有半步餘勢 |
| 7 | 各部位回收順序 | 手臂先收，腳最後落穩 |
| 8 | 服裝/物件與身體的物理關係 | 袖子／球拍／韁繩／毛髮晚半拍甩出，隨慣性才落下 |
| 9 | 攝影機空間幾何 | 見 `camera-and-transitions.md` §11 |
| 10 | 音樂/觸發條件 | 綁在鼓點或腳步觸地 |

跳躍要寫起跳與落地吸收；地面動作要寫進入與恢復路徑；長袖、斗篷、裙擺要服從慣性，不能自己飄。

## 12. 三層結構：持續層 / 動鏈層 / 微動作層

一段動作別只給一份動作清單，分三層，避免人物做完一個動作就停下來等下一條指令：

- **持續層**：整段都在的身體動態（呼吸起伏、重心流動、風格基調：舞蹈身韻、武術架勢、運動員節奏）。給生命感。
- **動鏈層**：這段真正要執行的主動作（腳步、轉身、軀幹、手臂路徑、重拍、恢復）。構成動作本身。
- **微動作層**：動作間隙的頭、眼神、手指、手腕。給細節。

三層不是要求每個部位一直動；目的是動作之間不歸零。持續層與微動作層是副層，不算主動作；每個 shot 的主動作仍只有 1 個（§3）。非舞蹈也能用：武打的持續層是呼吸與重心，微動作層是視線與握柄的指尖。

## 13. 狀態機寫法：長動作鏈與道具軌跡

來源：同案例庫 `2026-09-action-chain-sock-fan-comedy`（喜劇動作鏈，約 15 秒，25 個狀態；成片在作者 X 頁／本地，未隨 repo 發布；無 A/B）。**只當寫法參考。**

這裡的「狀態」是同一個連續鏡內的子狀態，不是 shot；整體仍守每 shot 一個主動作與 ≥ 2 秒（本例約每狀態 0.6 秒，是單一案例的極端寫法，未驗證）。

- 每個狀態寫「起始姿態 → 動作 → 結束姿態」，且**上一態的結束 = 下一態的起始**。
- 給身體部位和物件固定的稱呼（左腳、右腳、道具、手 1、手 2），每個狀態重申「誰在動、誰留在原位、物件歸誰」。這和 `motion-quality.md` §10「多角色穩定稱呼」同一道理。
- **因果閘**：用事件控制時機，例如「右腳要等道具碰到鏡頭、開始下落之後才能下降」，避免「道具還在空中、腳已經落地」的並發錯誤。
- **近端鎖定**：只想動手腕與手掌時，明寫肩、上臂、手肘、前臂保持穩定。
- 道具軌跡寫成有序清單（手 → 拋出 → 碰到鏡頭 → 彈回 → 落下），並規定與該軌跡無關的部位在此階段不動。

## 14. 動作主題（motif）與質地

10 秒以上的編排式動作（舞蹈、打鬥套路、運動集錦）建議有「可以被認出、變形、回收」的主題，而不是每秒一套新動作；產品、空鏡、單一動物鏡頭不適用：開場出現一次、中段被打斷或放大、低潮只剩殘留、結尾完整回來。每次重複改變力度、速度、幅度、方向或使用部位之一，保留足夠的動作聯繫。質地詞見 `motion-quality.md` §11。

## 15. 自檢：把鏡頭文字拿掉，動作還成立嗎？

寫完把所有鏡頭詞（push in、tracking、cut）刪掉再讀一次。如果剩下的只是「站著擺姿勢」「一直走路」「原地轉圈」，問題在動作設計，不是鏡頭；先補 §11 的十要素，不要加形容詞或加運鏡來掩蓋。

## 16. 因果五步、尺度參照、不瞬移、招牌技能 〔方法主張：守富提供的 15 秒腳本 system prompt，H3 未 A/B〕

大動作（攻擊、爆發、超能力、機械裝置啟動）一個 shot 內照這個順序寫，每一步都是看得到的事件：

1. **建立**：主體位置、朝向、與目標的距離（`ten meters from the stone gate, facing it`）
2. **起手**：哪個肢體或裝置開始動（`she drops into a low stance and draws her right fist back`）
3. **效果**：能量、武器、機構本身的樣子與方向（`a narrow arc of white flame leaves her fist and travels straight forward`）
4. **環境回應**：撞到什麼、什麼材質怎麼反應（`the gate's surface blackens and cracks outward from the impact point`）
5. **後果**：穩定下來的新狀態（`dust settles; a scorched hole remains; she straightens, breathing hard`）

- 五步不必都塞進同一個 shot，但跨 shot 不能跳步；預算仍是一個 shot 一個主動作（§3）。
- **尺度參照**：巨大或微小的東西要放一個已知大小的參照物在同一畫面（人、門、車、樹），否則 H3 會自己決定大小，切鏡後尺寸跳動。
- **不瞬移**：角色換位置要寫路徑（跑過去、跳下來、被擊飛到哪），切鏡後的位置要跟前一個 shot 的結束位置接得上；需要真的瞬移時把它寫成一個有起點、殘影、落點的效果事件。
- **知名角色 / 既有招式**：保留招牌外觀、服裝、道具、招式的形狀與顏色（不要把招牌招式換成泛用的「能量球」）；轉成真人或其他媒材時只換材質與光，不換設計。原創角色照使用者給的設定，不自行加衝突的特徵。注意：版權角色在 hosted 端點可能被審核擋下，這不是 prompt 問題。
- 和 §11 動作鏈十要素的關係：§11 管身體怎麼動，本節管「動作 → 世界」的因果鏈；兩者一起用。
