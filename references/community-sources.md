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
- Loop Forge h3-camera-shots（14 個具名鏡頭配方＋build_prompt.py，MIT）：https://github.com/loopforge0/minimaxh3-shots-skills 。2026-10-25 Colab 第 3 輪用其句型實測 8 支全過（dolly zoom 正反向、snorricam、eyes-in、aerial pullback、super dolly in、yo-yo zoom、三格分割），收錄於 `camera-moves-handbook.md`。MIT 授權，英文骨架改寫自其 shot line。

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

## 2026-10 研究批次（四支抖音 + Seedance/漫劇 GitHub + 中文社群）

| 來源 | 授權 | 用了什麼 | 可信度 |
|---|---|---|---|
| 抖音 1（7686479295782341938）電影感來自關係 | — | 關係、光線路徑、攝影機動機 | 方法主張；展示工具不是 H3；光線路徑已做本機先導 A/B（T3）沒測到好處，降為風格建議 |
| 抖音 2（7694988979074010404）分鏡表 | — | spec 卡欄位、角度慣例 | 方法主張；逐字稿逾時，只採影音摘要 |
| 抖音 3（7696840221446393126）混合媒介 | — | C9b 分層 | 方法主張；展示 Seedream 類工具；無 H3 實測 |
| 抖音 4（7686079109826465078）6 種運鏡 | — | camera §9 對照表（已 remap） | 方法主張；無 H3 實測 |
| alchaincyf/seedance-skill | MIT | 跳景別 >30°、運動放後段、焦段壓縮 | 僅別模型（作者白模自測） |
| zhouwei713/seedance-prompt | MIT | 設備缺陷、氛圍詞翻成現象 | 僅別模型，未附對照 |
| LearnPrompt/awesome-seedance | MIT | 低機位前景掠過、恐怖逐鏡升級 | 僅別模型（人工驗證案例） |
| songguoxs/seedance-prompt-skill | 無授權聲明 | 只借概念：前景遮擋 | 僅別模型 |
| chillzhuang/Kinema | AGPL-3.0 | 只借概念：停–爆–停、逆轉點換角度、讀數鏡 | 純理論 |
| MIKA6941/Comfy-H3-Director | 無授權 | 只借概念：match on action | 純理論（H3 專用，但無實測紀錄） |
| djyy1031/ai-comic-drama-director-skills | MIT | 固定、運鏡、切鏡三選一，運鏡鏈 | 純理論 |
| hailuoai.video 前景／背景深度文 | 第三方 | 金字塔細節 | 純理論 |
| mindstudio、fal Kling 3 | 第三方 | 焦點轉移 | 僅別模型 |

狀態：MiniMax-AI/MiniMax-H3 的 GitHub 到 2026-10-16 仍沒有有日期的 release，無法判斷規則是哪一版改的。
規則：無授權或 AGPL 的來源只轉寫概念，不收任何原句。本批沒有一條是 H3 實測。

## 音訊管線（audio-pipeline.md，2026-10-16）

| 來源 | 授權 | 採用 | 可信度 |
|---|---|---|---|
| MiniMax-AI/MiniMax-H3 `ref-en.txt` / `base-en.txt` / README | 官方 | `<Audio N>` 用法、audio reuse / reference、L2VA 定義、輸出規格 | 官方 |
| platform.minimax.io T2A v2 文件 | 官方 | speed / vol / pitch / emotion / `<#x#>` | 官方 |
| docs.comfy.org H3 partner 文件 | 官方轉述 | 聲畫同一次 forward、音訊需配圖或影片 | 官方轉述 |
| api.openverse.org、creativecommons.org 4.0 legalcode | 官方 | 端點、限額、授權與署名 | 官方＋實測 |
| LatentSync / MuseTalk / Wav2Lip repo | 各自授權 | 口型工具授權比較 | 官方 repo |
| virse.ai、Atlas Cloud、dev.to | 第三方 | 音色重新合成、voice crossover、文字描述聲線 | 社群單源 |
| ComfyUI issue 15283 | — | 大聲場景爆音 | 社群單源 |

## 光影配色（lighting-and-color.md，2026-10-16）

| 來源 | 授權 | 採用 | 可信度 |
|---|---|---|---|
| MiniMax-AI/MiniMax-H3 `ref-en.txt` / `base-en.txt` / README、platform.minimax.io video API | 官方 | 每鏡交代光線、風格句位置、參考上限 9/3/3/12、7000 字元、350–500 字 | 官方 |
| runware.ai editing-video 指南（作者標 MiniMax） | 第三方鏡像 | 日轉夜編輯範例 | 官方，經鏡像 |
| hailuoai.video lighting terms guide | 第三方 | 有效／避免光色詞 | 社群單源，內部經驗 |
| higgsfield.ai H3 指南 | 第三方 | 每個 shot 顏色寫得一模一樣 | 社群單源 |
| IC-Light、Qwen-Image-Edit Relight LoRA、FLUX Kontext 社群頁 | 各自授權 | 圖像端重打光寫法 | 社群單源，未實測 |
| en.wikipedia.org/wiki/Zone_System | CC BY-SA | 11 分區、概念對照 | 業界標準（無百分比） |
| lighting-color-palette-card（Seedance 教學影片蒸餾） | 自有 | 五層亮度、色卡錨點、重打光 | 自創方法，H3 未驗證 |
| colour-science `JND_CIE1976` 文件 | BSD | ΔE76≈2.3 | 社群 |

## 2026-10-20 研究批次（LoveUolanda 動作鏈方法論 + 英中社群掃描）

流程：Haiku 四路蒐集（英文社群、中文社群、journal 其他案例、官方 repo 差異）→ Opus 審核 → 整合。

### 主要來源

| 來源 | 授權 | 用了什麼 | 可信度 |
|---|---|---|---|
| LoveUolanda〈H3 古風舞蹈創作方法論〉X 長文，2026-10-19（x.com/LoveUolanda/status/2112373570055897528） | 原文亦收錄於 MIT repo `case-studies/2026-10-classical-wuxia-dance-13-segment/methodology.md`（Copyright (c) 2026 LoveRain1997，MIT）；本 skill 為中文轉寫與泛化，非逐字複製 | 動作鏈十要素、三層結構、運動質地、攝影機幾何、負向配正向、導演自檢 | **作者自述有成片（貼文影片），無 A/B、無量化**；貼文自述長片以 RunningHub OpenAPI 腳本化生成、本地 ffmpeg 拼接 |
| github.com/LoveRain1997/h3-prompt-journal（MIT） | MIT（Copyright (c) 2026 LoveRain1997；LICENSE 無排除文字條款） | 13 段武俠舞完整 prompt、sock-fan 狀態機、snap-lock 兩態相機、speed-contrast 動作數比、orbital 遮擋聯動 | prompt 完整公開；repo README 稱所有案例均實際生成、成片在作者 X 文章頁，但**成片未隨 repo 發布**（repo 內 mp4 多為來源樣片），我們沒看過成片；lamp 五章 p83/p84 README 未給比較結論，視為風格變奏而非對照 |

journal 內部互相矛盾處（連續環繞 vs 離散硬鎖、有無時間碼、單段精簡 vs 重複冗餘）已整理成條件對照，見 `camera-and-transitions.md` §12、`prompt-formats.md`「附：長自含式…」。

### 英文社群（Reddit 為主，2026-09 下旬～10 月）

全部是作者自述或留言建議，日期多為以貼文序號推算的近似值，**視為待測假說**：

- 一個 shot 一個具名運鏡（type + amplitude + speed），疊加運鏡會讓畫面變形（suno.bi、photogptai、LinkedIn 文；與現行規則一致，佐證不新增）。
- 連續長鏡/鏈式生成約第 3–4 次退化，一位作者把 30–45 秒當工作流上限、另一則留言稱約 45 秒後色彩衰退；用精確的最後一幀 PNG 接續（r/StableDiffusion 1wwh94x、1x43xyq、r/comfyui 1wqlv1u、1wyrp36）。
- Blender 假人運鏡渲染當 Ref2VA 運鏡參考可行，但要檢查接縫與身份漂移（r/comfyui 1wqybjk）；遮罩式動作參考有作者自述的 A/B 改善（r/StableDiffusion 1wruoq1）。
- 動漫來源影片會被加 3D 陰影、鏡頭漂移；留言建議用格線/十字覆蓋當固定錨（r/comfyui 1x8odqk，**未測**）。
- 複雜場景拆成兩個短 prompt 較穩（r/StableDiffusion 1wrdhbr）。
- 單句 prompt 做舞蹈：H3 比 Seedance 2.0 更守住身份，但漏掉運鏡、舞蹈提早結束（r/StableDiffusion 1wvsrhs）。

### 中文社群

2026-09-17 之後、有 H3 實測證據的新發現幾乎沒有；多為彙整與未驗證宣稱（覺醒AI知識庫 2026-09-23、X @GeekCatX 2026-09-27 反推 skill、B 站 BV1A2Hs6eE5p、GitHub flaqai/awesome-minimax-h3-video-prompts 與 AtlasCloudAI 中文庫）。小紅書、抖音、即刻、知乎原文抓不到。可用的只有：動作因果與關係（誰看見、誰被拍）要寫清楚；劇烈動作易溶解崩壞，建議分拍寫；換人時主體描述不足會丟身份。**均未驗證，未寫進規則，僅供參考。**

### 官方

MiniMax-AI/MiniMax-H3 自 2026-10-16 起沒有新 commit、release 或 tag（最後一次 push 為 2026-08-15）；平台文件的素材與字元上限與既有規則一致。issue #95（獨立參考音訊會多出對白、重複句）、#17（Ref2VA/FL2VA 多角色 voice 互相滲漏）是使用者回報，官方未回應，不當規則。官方頁另提文字生影片可在關鍵描述後加 `[pan]`、`[zoom]`、`[static]` 相機指令，效果未驗證，未收錄。

規則：無授權來源只轉寫概念；MIT 來源附授權聲明。本批沒有一條新規則通過 H3 對照實測。

### 使用者提供（2026-10-21）

- 「Photorealistic 15-Second Cinematic Video Script Generator」通用 system prompt（守富提供，作者不明，非 H3 專用）。吸收的概念：180 度線/畫面方向、因果五步、尺度參照、不瞬移、招牌技能保留、soundscape 遠近與三段衰減、配樂人聲與曲風、品牌不捏造、交付規則。皆為方法主張，未經 H3 A/B。衝突對照見 `prompt-formats.md` 附錄。
