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
