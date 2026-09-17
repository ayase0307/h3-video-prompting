# h3-video-prompting

MiniMax H3（Hailuo 3）影片生成 prompt 的 Agent Skill。整理官方指南、官方飛書手冊（含 MiniMax 官方在評論區的回覆）、社群 prompt 庫與實測文章，重點放在**人物動作品質、節奏卡點、各種情境的寫法、失敗分診**。

An agent skill for writing MiniMax H3 / Hailuo 3 video prompts: motion quality, rhythm and beat-synced cuts, scenario playbooks (dialogue, UGC, MV, dance, fight, product, brand, UI, animals, anime, VFX, loops, editing…), and a symptom → fix triage table, compiled from the official guides, the official Feishu manual, community prompt libraries and creator reports.

## 安裝

```bash
# 本 skill
npx skills add ayase0307/h3-video-prompting

# 必要的官方排版 skill（欄位名、<d> 標籤、Ref2VA 六段式）
npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing
```

或手動：把整個資料夾放進 `~/.claude/skills/h3-video-prompting/`（Claude Code）或你的 agent 的 skills 目錄。

## 分工

- `h3-prompt-writing`（官方）：最終格式。
- `h3-video-prompting`（本 repo）：寫什麼、怎麼拆、哪些坑。先用本 skill 決定內容，再用官方 skill 排版。

## 內容

| 檔案 | 內容 |
|---|---|
| `SKILL.md` | 工作流程、情境索引、預算表、十條速查、本地 ComfyUI 注意事項、red flags |
| `references/scenarios-people.md` | 對白短劇、UGC、唱歌 MV、舞蹈、打鬥、跑酷、喜劇、情感特寫、懸疑偽紀實、vlog、POV/FPS、旁白數位人、真人照片動畫 |
| `references/scenarios-commercial.md` | 產品 hero、開箱示範、液體食物、品牌片、時尚美妝、logo 片頭、UI/遊戲選單、電商、工業機器人、建築旅遊 |
| `references/scenarios-world-and-styles.md` | 空鏡、自然、動物、車輛追逐、手機偽紀實、2D anime、3D 卡通、黏土紙藝、手繪實拍融合、動態圖形、變身 VFX、循環、角色設定板、綠幕重打光、混剪 |
| `references/motion-quality.md` | 動作弧線、重量動量、材質回應、手與物件、臉部表演、口型、舞蹈運動、慢動作、動畫風格規律、身份保持 |
| `references/action-choreography.md` | 動作寫成軌跡、順序連接詞、打鬥一拍公式、一鏡到底 vs 切鏡、動作遷移、不說話寫法 |
| `references/rhythm-and-pacing.md` | 時間軸、shot 最短長度、卡點觸發物、官方「律動」模板、唱歌節奏、速度形容詞、J/L-cut |
| `references/camera-and-transitions.md` | 官方 20 種運鏡、景別鏡頭角度、各類型預設鏡頭、切鏡、轉場寫成事件、手持感 |
| `references/audio-and-dialogue.md` | 三層音軌、對白預算、speaker 格式、表演方向、聲音參考、不說話、字幕、音效同步、配樂 |
| `references/references-and-editing.md` | 素材分工、動作/運鏡/表演遷移、兩段式、影片編輯、續接、首尾幀與循環、真人照片 |
| `references/prompt-formats.md` | 官方三欄 / 六段式 / 中文三段 / 社群區塊式，何時用哪種；平台參數地雷 |
| `references/failure-triage.md` | 36 種症狀 → 原因 → 修法；送出前 8 問；成本策略 |
| `references/example-fight-10s.md` | 一段完整的 10 秒打鬥改寫範例與決策說明 |
| `references/community-sources.md` | 所有來源與可信度 |

## 來源

官方：MiniMax-H3 GitHub / HF 指南、飛書使用手冊（45 個 goodcase + 官方回覆）、開放平台文件、Hailuo 知識庫。
社群：AI-KSK 導演台 compiler、penposs 框架、stimQQ 與 BeatAPI 的 prompt 庫（222 例）、aireiter 引用的 Reddit/X 實測、Kapwing、reAPI、atlascloud、Runware、fal.ai、videoai.me、ambienceai、debutify、virse 等。完整清單見 `references/community-sources.md`。

第三方 prompt 與文章的版權屬原作者；本 repo 只整理規則與寫法，範例為重寫。

## License

MIT
