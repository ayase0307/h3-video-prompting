---
name: h3-video-prompting
description: Use when writing, reviewing, or fixing a MiniMax H3 / Hailuo 3 (H3, Hailuo 03, H3 Max) video prompt in any mode (T2VA, I2VA, FL2VA, L2VA, Ref2VA, video editing, ComfyUI local, hosted API), for any scenario - dialogue and short drama, UGC talking head, singing and MV, dance, fight, parkour, chase and vehicles, product and e-commerce, brand film, logo sting, UI and game, animals, nature B-roll, anime, 3D cartoon, clay and paper, hand-drawn fusion, motion graphics, VFX transformation, loops, motion transfer, relighting - or when a generated clip came back static, mushy, over-choreographed, speaking gibberish, with unwanted music or subtitles, garbled text, or drifting identity.
---

# H3 Video Prompting（動作 × 節奏 × 情境 × 社群實戰）

**REQUIRED SUB-SKILL:** `h3-prompt-writing`（官方）負責最終排版：欄位名、`[Shot N] At MM:SS.mmm`、`<d>` 標籤、`<Picture N>` 對齊句、Ref2VA 六段式。本 skill 負責「寫什麼」與「怎麼不踩坑」。先用本 skill 決定內容，再用官方 skill 排版。

核心原則：**H3 prompt 是隨時間變化的規格，不是畫面描述。** 每句話對應看得到或聽得到的事件，並說清楚在第幾秒。

## 工作流程

1. **選格式**：本地 ComfyUI / 導演台 → 官方三欄或六段式；海螺 / Design / hosted 自然語言 → 中文三段或社群區塊式。決策表：`references/prompt-formats.md`。
2. **選情境**：從下表找最接近的一到兩個，讀那一節的「優先順序 / 必寫 / 坑」。
3. **先寫動作鏈，再寫鏡頭，再寫聲音，最後排版**（AI-KSK 口訣）。素材有的話先分工。
4. **預算檢查**（下表），超標就砍動作或拆成多次生成。
5. 送出前對照 `references/failure-triage.md` 的症狀表與 8 問。

## 情境索引

| 你要做的 | 讀 |
|---|---|
| 兩人對白、短劇、UGC 口播、唱歌 rap、舞蹈、打鬥、跑酷追逐、喜劇、情感特寫、懸疑偽紀實、vlog、POV/FPS、旁白數位人、真人照片動起來 | `references/scenarios-people.md` |
| 產品 hero、開箱示範、液體食物、品牌片、時尚美妝、logo 片頭字卡、UI/網頁/遊戲選單、電商在手、工業機器人、建築旅遊 | `references/scenarios-commercial.md` |
| 空鏡 B-roll、自然天氣、動物、車輛追逐空拍、手機偽紀實、2D anime、3D 卡通、黏土紙藝、手繪實拍融合、動態圖形、變身 VFX、無縫循環、角色設定板、綠幕重打光、多素材混剪 | `references/scenarios-world-and-styles.md` |

橫向主題：
- 動作品質（重量、材質回應、手、表情、口型、慢動作、動畫風格規律）：`references/motion-quality.md`
- 動作拆解與打鬥一拍公式：`references/action-choreography.md`
- 節奏、卡點、時間軸、速度形容詞：`references/rhythm-and-pacing.md`
- 鏡頭 20 種官方詞、景別鏡頭角度、轉場寫成事件：`references/camera-and-transitions.md`
- 對白預算、speaker、聲音參考、配樂進出、不說話寫法、字幕：`references/audio-and-dialogue.md`
- 素材分工、動作/運鏡/表演遷移、影片編輯、續接、首尾幀與循環：`references/references-and-editing.md`
- 完整改寫範例：`references/example-fight-10s.md`

## 預算表（社群實測上限）

| 項目 | 上限 | 超過會怎樣 |
|---|---|---|
| 每個 shot 主動作 | 1 個（含起手→接觸→收勢） | 動作被壓縮、糊成一團 |
| 每個 shot 長度 | ≥ 2 s；對白 shot = 台詞朗讀秒數 + 反應 | timestamp 太密是最常見結構失敗 |
| 10 s 內 shot 數 | 3–4；15 s 內 4–6 | 幻燈片感、動作沒做完 |
| 每個 shot 運鏡 | 1 個（motion type + amplitude + speed + 落點） | 鏡頭亂飄或幾乎不動 |
| 對白 | 15 s 約 20 英文字；每句約 10 字；一個 `<d>` 一句 | 語速趕、口型壞、亂語 |
| 重要角色 | ≤ 3 | 身份漂移、錯人說話 |
| 慢動作 | 獨立 shot，背景動態元素減到最少 | 抖動、閃爍 |
| 純文字 prompt | 300–700 英文字 | 太短 = 沒東西可參考 |
| 有參考素材時 | 字數要縮，只寫新變化 | 文字跟圖片互搶，臉會變 |
| 參考檔 | ≤9 圖 / ≤3 影片 / ≤3 音檔 / 總 ≤12；影片音檔各 2–15 s、總 ≤15 s；音檔不能單獨 | 被拒或被忽略 |

## 十條速查

1. 動作寫軌跡：起始狀態 → 哪隻手/哪個方向/多快 → 結束狀態。
2. `first / then / as / finally` 鎖順序；沒連接詞 H3 當同時發生。
3. 每個素材一個職責，並寫它不負責什麼。
4. 卡點寫觸發物（bass hit、刀刃接觸聲、落地），不寫 energetic。
5. 運鏡用官方詞 + 落點，寫在動作句裡；環繞寫 `truck left + pan right`。
6. 速度用形容詞；同一 shot 不混 slow 與 rapid；慢動作獨立降熵。
7. 聲音三層各歸其位；音效寫兩次；配樂寫進出時間；不要就 `non_diegetic_music: N/A` 且全文無音樂情緒詞。
8. 不說話用正向句 + 持續動作；不寫「看鏡頭」；不要在 prompt 裡寫「不要字幕」。
9. 要可讀的字逐字打出加引號；沒打的字會變噪音。
10. 一鏡到底就沒有 `[Shot 2]`；切鏡每次帶新資訊；轉場寫成事件。

## 本地 ComfyUI / 導演台

- 沒有 Context-IR 改寫器：官方格式是硬需求。
- `ref_image_0` → `<Picture 1>`，`ref_image_1` → `<Picture 2>`；保留英文與尖括號。
- 中文台詞不出聲：repo tokenizer + `<d>[Chinese] …</d>` + 檢查 shell 編碼。
- 三張圖敘事：先 `<Subject 1>` 合併同一角色，Picture 只當關鍵幀；每次切鏡留一個可觀察的連續載體（動作、視線、道具接觸、動量、聲音）。
- 時間點對齊實際有效時長（幀數 snap 後以實際為準）。

## Red flags：看到就停下重寫

- 兩個 shot 差不到 2 秒；一個 shot 三個以上動作
- `cinematic / epic / dynamic / high quality` 沒有物理描述
- 慢動作 shot 裡有大雨、飛葉、群眾
- 寫了 orbit / 環繞；一個 shot 兩個運鏡
- 上傳素材沒寫職責；或每個 shot 重述參考圖外觀
- 同時要一鏡到底和切鏡；同時要配樂和不要 BGM
- 台詞兩句塞一個 `<d>`；3 秒 shot 講一段話
- 代名詞或場景跟照片不符（會中途換人）
- 「HUD elements」「some labels」沒逐字打出

來源與可信度：`references/community-sources.md`。
