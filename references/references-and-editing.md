# 參考素材、動作遷移、影片編輯、續接

來源：官方 ref-en.txt；官方飛書手冊 2.2/3.x 範例；Runware motion/camera/performance 與 editing 指南；virse motion transfer 修法；penposs capability-map；AI-KSK use-case catalog；fal.ai 編輯範例；Kapwing。

## 1. 每個素材一個職責，並說它「不負責」什麼

| 素材 | 最佳角色 | 主要風險 | 寫法 |
|---|---|---|---|
| 圖片 | 身份、臉、服裝、產品幾何、場景、風格、構圖 | 姿勢或背景滲入 | `Image 1 locks face and wardrobe. Image 2 sets lighting and mood only.` |
| 影片 | 動作、時序、運鏡、表演、剪輯節奏、編輯源 | 原演員或原場景滲入 | `Video 1 defines the hand trajectory and timing only. Do not copy its actor, wardrobe, setting, lighting, or camera.` |
| 音檔 | 音色、語氣、節拍、音樂風格、直接復用 | 聲線不符、原句被複製 | `Audio 1 provides the speaker's vocal character and delivery cadence only. Use the dialogue written in this prompt.` |
| 文字 | 定義關係與新內容 | 與參考互相矛盾 | 只寫參考沒決定的事 |

- 沒指派角色的素材仍會影響輸出，只是影響你沒選的部分（多數「身份漂移」其實是參考滲漏）。
- 兩份素材都含人物或場景時，明寫誰決定身份、誰只給姿勢/光線/風格、衝突時以誰為準。
- 素材最少化：三個職責清楚的檔案勝過九個鬆散的；重複素材造成平均臉、產品變形、風格串台。
- 有參考時 prompt 要縮：「References carry identity, the prompt carries action」；每個 shot 重述外觀會讓臉變。

## 2. 官方素材用途詞（中文入口）

人物參考（鎖臉/形象）、物體參考、場景參考、關鍵幀（首/尾幀明說）、音色參考、故事版（依分鏡生成）、風格參考、構圖參考、音頻復用、音頻部分復用（某軌/某時段）、動作參考、運鏡參考、視頻編輯。

## 3. 動作 / 運鏡 / 表演遷移

- 動作：`Use Video 1 as the motion reference and Image 1 as the character. The woman from Image 1 performs the exact dance move from Video 1 … Keep her identity, braids, and orange tracksuit.`
- 官方例：`圖1的人物動作、表情與表演節奏嚴格參考輸入視頻1`，之後描述新場景發生的事。
- 乾淨參考：素背景、良好照明、只含一個動作、全身入鏡。
- 框架匹配：全身動作用全身參考與全身角色；臉部表演用緊特寫對緊特寫。
- 體型相近才穩：人跳舞套四足動物、寬景讀細微手勢都會漂。
- 運鏡參考：`Use Video 1 as the camera reference and follow its exact camera path. Apply that movement to a completely different subject: …`；**只描述新主體，不重述那個運鏡**。
- 表演參考：`delivers the same performance as Video 1, the same widening surprise breaking into a big delighted grin with a hand rising toward his mouth`。
- 參考影片的聲音會跟進來：換匹配聲線或在 Sound 句明寫。
- 保留原影片「拍法」：把時間軸、動作功能、機位、運鏡、轉場、卡點逐層鎖定，不能只寫「參考視頻1」。
- 換皮（visual reskin）：鎖定結構（時間軸/動作/機位/轉場/卡點），重做內容（人物/服裝/產品/環境/色彩/品牌）；最終 prompt 直接寫新成片，不寫「原來是什麼、現在改成什麼」。

## 4. 複雜遷移用兩段式

一次同時換角色 + 換背景 + 精細動作（手指、臉部、口型、複雜編舞）容易漂。virse 實測流程：

1. 第一次：換角色，保留原動作與原環境。
2. 檢查身份、手、臉、時序。
3. 用成功輸出當下一次的影片參考。
4. 第二次：換背景。

一次一個變數；社群回報雙人換臉舞蹈在調整保留指令後約 90% 成功，但 seed 仍影響。

## 5. 影片編輯（Ref2VA 編輯源）

prompt 是**指令**不是描述：指向來源、命名改動、明說保留。

```text
In Video 1, change the lighting from bright day to night: a deep blue sky, a warm lamppost
glow across the bench, and soft moonlight on the grass. Keep the bench, the tree, and the
camera drift exactly the same. Sound: soft night crickets.
```

- 編輯靠「保留」運作：沒提到的都會保留，但重要的要點名進 keep 半句。
- 換物件：`replace the cup with a glass of iced matcha; keep the woman, her exact motion and sip, the table, and the blurred background.`
- 多項編輯：編號列出每項的對象、位置、最終狀態，結尾一句「其餘保持不變」。官方範例一次做 6 項（換報紙→綠皮書、椅子→紅沙發、拿掉墨鏡、拿掉燃燒特效、照片→黑筆記本、左側加一棵樹）。
- 換背景 / 綠幕：`background elements must completely match the actions of the characters in Video 1; modify the lighting of the characters to match the background`。
- 換台詞：`replace the woman's line "…" with the line from Audio 1: "…". Adjust the performance subtly to match the new dialogue.`
- 加角色：`Add one person on the left wearing the same team uniform and moving in sync with the others.`
- 加特效層：`Add orange-yellow hand-drawn marks like Image 1 around the two people in Video 1. As they move closer, the marks multiply … When they kiss, introduce pink brushstrokes.`
- 局部風格化要明確作用範圍（`transform only the trees and cars into voxel; preserve buildings and pedestrians as photoreal`），否則整幅被重繪。
- 精細文字、精確 logo、要幀幀一致的群眾是弱項：一次一個改動、來源片段越短越好。
- 輸出比例跟來源。

六段式寫法：`<Video 1> is the source video for the target video edit.`、summary 前綴 `[video editing + audio reuse]`、`<Audio 2> is the synchronized audio track of <Video 1> and is reused` → `fully_copy`。

## 6. 續接與長片

- 官方任務型 `video continuation`：從來源結束狀態開始，保留方向與動作相位；新音訊延續原特徵（`audio reference`）除非直接複製。
- 社群鏈式流程：每段 10 s，取最後 2 s（48 幀 @24fps）當下一段上下文，並重新帶入角色參考；動作連續性改善，色偏與狀態變化仍會發生。
- >15 s 單鏡會崩：拆 15 s 段，尾幀接首幀或同方向運動 / 遮擋接。
- Hero Template：先做最重要的 clip，抽出有效節奏詞與光線句，後續 clip 只換主體場景。

## 7. 首尾幀（FL2VA）與循環

- 兩張圖必須同房間、同機位、同光；第二張最好是編輯第一張得到，不要分開生成。
- 描述**中間路徑**，不要描述兩張靜態圖：`first-frame state → observable intermediate changes → narrowing differences → last-frame state`；偏好單一 shot。
- 用途：產品開合（`Start frame: closed box. End frame: bottle upright beside the open box. Between them, hands lift the lid …`）、UI 轉場、情緒弧線、動物起飛落地。
- 循環：首尾同圖模型仍會補動作，尾幀常變；寫回到原姿勢的路徑，並接受可能要後製裁切。社群 seamless-loop prompt 會寫 `[LOCK] Render exactly as @image1. Do not alter …` + `[LOOP] A perfect cycle …`。
- L2VA：先建立合理的前狀態，再逐步收斂到尾幀；不要一開場就是尾幀然後靜止。

## 8. 真人照片（I2VA / 參考）

- 照片：清晰、正面或四分之三、單一主體、留動作空間；墨鏡、重陰影、極端角度會打壞口型。
- prompt 只寫表演與台詞，不寫外觀；代名詞、身份、場景必須與照片一致（寫 she 給男性照片，4 秒後會換人）。
- 只用自己或已同意者的照片。
