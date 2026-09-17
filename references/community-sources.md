# 來源清單（2026-09-17 整理）

## 官方

- 官方 repo 與 skill：https://github.com/MiniMax-AI/MiniMax-H3（`skills/h3-prompt-writing` 已安裝到 `~/.claude/skills/h3-prompt-writing`，另有 8 個 style skill：3d-animation-short-generator、brand-promo-video-generator、co-op-game-intro-generator、handdrawn-live-video-generator、minimalist-product-ad-generator、music-video-subtitle-generator、paper-collage-explainer-generator、papercraft-stop-motion-explainer；後者需 MiniMax Hub agent，不可攜）
- 官方 prompt 指南（HF）：`docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md`、`docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md`
- MiniMax H3 使用手冊（飛書，含 45 個 goodcase、四、如何更好地使用 H3、評論區官方回覆）：https://vrfi1sk8a0.feishu.cn/wiki/FIWjwgL33ipnkekzk30crmKUnIh
- 開放平台：https://platform.minimax.io/docs/guides/video-generation 、 https://platform.minimax.io/docs/guides/video-prompt
- Hailuo 官方知識庫（節奏 / speed ramp）：https://hailuoai.video/pages/knowledge/prompting-pacing-brand-story-rhythm-ai 、 https://hailuoai.video/pages/knowledge/speed-ramping-director-mode-ai-video

## 社群 skill / repo

- AI-KSK 導演台 prompt compiler（含 camera-action-recipes、failure-repair-matrix、DIRECTOR_PROMPT_LOGIC_ZH）：https://github.com/AI-KSK/aiksk-minimax-h3-local-prompt
- penposs 泛化框架（六層控制、節奏、素材職責）：https://github.com/penposs/minimax-h3-video-prompt

## 社群整理文（含引用 Reddit / X 實測）

- aireiter：What Works, What Breaks（引用 @AIWarper、u/Powerful-Goal52 pull-out 修法、u/TheElectriking 20% 漏音樂、<d> vs 引號）：https://aireiter.com/blog/minimax-h3-prompt-review
- atlascloud：45 官方 prompt 逆向（六段結構、亂碼修法、This Is Fine 範例）：https://www.atlascloud.ai/blog/tips/minimax-h3-prompt-guide
- Kapwing：7 tips（動作寫成軌跡、分離主體/鏡頭/切鏡、失敗模式用分鏡設計解決）：https://www.kapwing.com/resources/how-to-prompt-minimax-h3-hailuo-3-0-a-guide-for-ai-video-creators/
- reAPI：一個主動作、一個運鏡、8 問自檢：https://reapi.ai/blog/minimax-h3-prompt-guide
- dreampixelforge：官方格式逐欄實測（cut 準時、台詞逐字）：https://www.dreampixelforge.com/blog/minimax-h3-prompts
- Runware：動作 / 運鏡 / 表演遷移：https://runware.ai/docs/models/minimax-h3/guides/motion-camera-performance
- videotoprompt：動作序列、解剖細節、物理回應：https://www.videotoprompt.app/posts/hailuo-h3-prompt-guide
- morphed：41 recipes（first/then/as、舞蹈寫法）：https://morphed.app/blog/hailuo-3-prompts
- audiencescience：對白 / 音效 / 音樂三層時間軸：https://www.audiencescience.com/prompting-audio-in-minimax-h3/
- minimax-h3.wiki 社群 wiki 與街舞 recipe：https://minimax-h3.wiki/guides/how-to-write-minimax-h3-prompts/
- fal.ai 44 範例：https://fal.ai/learn/devs/minimax-h3-prompting-guide
- arcloop anime：https://arcloop.ai/handbook/en-US/minimax-h3-anime-prompt-guide
- 老陳 AI 知識庫（中文）：https://www.cpengx.cn/video/h3-prompt.html

## 社群 prompt 庫（可看成片對照）

- stimQQ/stunning-minimax-h3-prompts：222 例（150 作者原文索引 + 72 重建 MIT），分類 animal/animation/camera/character/cinematic/dialogue/editing/product/vfx：https://github.com/stimQQ/stunning-minimax-h3-prompts
- BeatAPI/awesome-minimax-h3-prompts：含 aimikoda 角色板兩段式、KALDR 香水多參考、Y2K MV 等：https://github.com/BeatAPI/awesome-minimax-h3-prompts

## 情境專文

- ambienceai：真人照片動畫、對白預算（20 字/15 s、10 字/句、一 `<d>` 一句）、cut 誤差 0.12 s 實測：https://www.ambienceai.com/tutorials/minimax-h3-prompting-guide
- debutify：對白表演（意圖 > 情緒、聽者動作、停頓）：https://debutify.com/blog/make-ai-dialogue-scenes-natural-with-minimax-h3
- virse：motion transfer 滲漏與兩段式、聲音參考不是波形保留、續接 2 s 上下文：https://www.virse.ai/blog/minimax-h3-motion-transfer
- atlascloud lip-sync：音色參考要唸不同句子、參數地雷：https://www.atlascloud.ai/blog/tips/minimax-h3-lip-sync-and-audio
- videoai.me：UGC 模板、鏡頭語言、12 例：https://videoai.me/blog/minimax-h3-ugc-prompt-templates 、 https://videoai.me/blog/minimax-h3-camera-movement-prompts 、 https://videoai.me/blog/minimax-h3-prompt-examples
- minimax3.com：20 種官方運鏡整理：https://minimax3.com/tools/h3-camera-control
- minimaxh3.app：產品照轉廣告的保留清單：https://minimaxh3.app/posts/minimax-h3-product-ad
- Runware editing：編輯 = 改動 + 保留：https://runware.ai/docs/models/minimax-h3/guides/editing-video
- picsart：H3 vs H3 Max 分工、10 例：https://picsart.com/blog/minimax-prompting-guide/
- scenario.com：H3 Max 時間戳寫法、首尾幀範例：https://help.scenario.com/articles/1593651655-minimax-h3-the-essentials
- pixmind：短影音 hook 與六段骨架：https://www.pixmind.io/posts/minimax-h3-viral-video-guide

## Reddit 原串（本機無法直接抓，靠上列文章引用）

- r/StableDiffusion 1vuo078「the H3 dialog prompting guide sucks」
- 1vt2fea「prompting so that it will keep the full body」
- 1viui81「the H3 gibberish problem solved」
- 1veauqw「MiniMax H3 prompt guide」
- 1vhloyz「Walter White and the MiniMax H3 official prompting guide」

## 可信度

- 官方手冊與 HF 指南：格式與欄位規則以此為準。
- 官方評論區回覆（用户5333）：關於不說話、音效時間、字幕、光照負向詞，是第一手官方建議。
- 第三方平台文（reAPI / atlascloud / Kapwing 等）：多數與官方一致；限制數字（時長 5–10 vs 4–15、768p vs 2K）因平台而異，以你實際用的端點為準。
- Hailuo 知識庫的 Temporal Prompting 寫給 Hailuo 舊版自然語言入口；「形容詞優於數字」在 H3 自然語言模式仍適用，但 H3 結構化格式本身就支援時間戳。
