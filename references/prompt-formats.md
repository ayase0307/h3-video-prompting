# 四種 prompt 格式：什麼時候用哪一種

| 格式 | 用在哪 | 特徵 |
|---|---|---|
| A. 官方三欄（Base） | 本地 ComfyUI / 開源權重 / 導演台；hosted API 要精確切點與 speaker 時 | `integrated_multimodal_description` + `overall_soundscape` + `non_diegetic_music`；I2VA/FL2VA/L2VA 前面加對齊句 |
| B. 官方六段（Ref2VA） | 任何有參考圖/影片/音檔的本地生成；hosted 多參考任務 | `subject_definitions / summary / retention_analysis / detailed_description / overall_soundscape / non_diegetic_music` |
| C. 官方中文三段 | 海螺 App / MiniMax Design / 開放平台自然語言（有 Context-IR 改寫） | 【參考素材說明】【核心創意】【畫面過程描述】 |
| D. 社群區塊式 | hosted API / 第三方平台自然語言 | `SCENE / SHOT BREAKDOWN / CAMERA / LIGHTING & PALETTE / AUDIO / AVOID`，開頭一行 `Duration | Aspect ratio | Style` |

規則：**本地沒有 Context-IR 改寫器，A/B 是硬需求。** hosted 端點會把 C/D 改寫成 A/B，但要精確控制 cut 時間、speaker、字幕、配樂時，直接寫 A/B 更穩（社群實測：寫了時間戳的 cut 誤差約 0.12 s；沒寫就一鏡靜止到底）。**本機先導實測（n=3, 0.5MP, t2va 6 s）**：`[Shot n] At` 時間戳 6/6 切點落在 ±0.25 s 內（平均誤差 0.045 s、無多餘切點）；同樣三個 shot 寫成含 `the shot cuts to` 的散文、不加時間戳，H3 每支仍切 2 次，但只有 2/6 落在目標附近——所以「沒寫就一鏡靜止到底」在有切鏡字眼時不成立，完全不寫切鏡字眼的情況沒測。原始紀錄在私有 repo，未公開。

A/B 的完整規則在官方 skill `h3-prompt-writing` 的 `references/base-en.txt` 與 `ref-en.txt`；本檔只列決策與差異。

## A. 官方三欄要點

- T2VA 沒有對齊句；I2VA：`For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.`；FL2VA/L2VA 用「How the reference pictures align with the target video — …」句，秒數兩位小數，對齊實際有效時長。
- `[Shot 1]` 不帶時間戳並先寫風格（`Live-action, cinematic` / `2D-animated` / `3D CG` / `claymation` / `watercolor` / `vintage film`）；之後 `[Shot N] At MM:SS.mmm,` 嚴格遞增。
- 純文字 300–700 英文字（社群經驗值，官方無此數字）；有參考時縮短。
- 結尾兩欄不能省，沒有就 `N/A`。

## B. 六段式要點

- `<Subject N>` 是語義身份（誰），`<Picture N>` 是檔案（哪張圖）；同一角色多張圖合併成一個 Subject：`<Subject 1> is the same woman established by <Picture 1>, <Picture 2>, and <Picture 3>.`
- 圖只有當首幀/尾幀/關鍵幀/構圖錨/storyboard 時才獨立追蹤 Picture；只提供長相的圖寫進 Subject 定義即可。
- Subject 不只人：會跨 shot 重複出現、需要保持一致的道具或場景也可以給一個 Subject（例：`<Subject 2> is the rain-soaked night market alley …`），寫空間配置、材質、天氣、它會怎麼回應動作。簡單場景不要硬湊 Subject。〔方法主張：守富提供的 15 秒腳本 system prompt，H3 未 A/B〕
- `summary` 開頭方括號任務型：`keyframe completion / reference generation / video editing / video continuation / audio reuse / audio reference`，可用 ` + ` 組合。
- `retention_analysis` 標記：視覺 `fully_preserved / partially_preserved / attribute_transfer / weak_reference`；音訊 `fully_copy / partially_copy / reference / weak_reference`。
- `detailed_description` 在 `[Shot 1]` 之前先用一兩句英文定風格；生成任務 350–500 英文字。每個 `[Shot N]` 寫五小節時會變長（實測 430–940 字；T8 為 519–636）；≤700 是未實測的建議值，超過時由使用者決定放行或壓縮，送件端字元上限不可超，見 `shot-five-part.md`。
- 本地 ComfyUI Ref2VA 節點：`ref_image_0` → `<Picture 1>`，`ref_image_1` → `<Picture 2>`，保留英文與尖括號，不寫欄位全名。

## C. 官方中文三段（海螺 / Design / API 自然語言）

```text
【參考素材說明】@圖片1 提供人物形象（鎖臉），@視頻1 提供動作參考，@音頻1 提供節奏/情緒參考。只參考指定維度，不直接複製參考圖。
【核心創意】一句話：主體 + 地點 + 事件 + 題材/風格 + 特殊運鏡（航拍/一鏡到底/慢動作）+ 切鏡風格（普通切/疊化/卡點切/快切）。
【畫面過程描述】按時間段或 Shot 分段；每段：景別 + 內容 + 運鏡 + 動作 + 台詞 + 音效；最後寫「不想要」。
非敘事性音樂：N/A
```

- 沒上傳素材就整段跳過【參考素材說明】。
- 素材用途詞：人物參考 / 物體參考 / 場景參考 / 關鍵幀 / 音色參考 / 故事版 / 風格參考 / 構圖參考 / 音頻復用 / 音頻部分復用 / 動作參考 / 運鏡參考 / 視頻編輯。
- 音頻復用要保留歌詞或台詞時，強烈建議補逐字文本：`@音頻1 作為音頻復刻素材，具體歌詞是：「…」`。
- 官方「容易踩的坑」表：只寫一段話沒分段、素材沒說用途、想用音樂又說不要 BGM、想一鏡到底卻寫很多分鏡、想要臉一致卻沒傳圖、prompt 太短。

## D. 社群區塊式（222 例 prompt 庫共同結構）

```text
Duration: 15 seconds | Aspect ratio: 16:9 | Style: Handheld action sports parkour videography

SCENE
<主體外觀、場景固定元素、畫面內文字原文>

SHOT BREAKDOWN
0-4s — <一個動作 + 景別/角度>
4-8s — <一個動作；「Cuts to …」寫切鏡>
8-12s — …
12-15s — <落點 / 定格>

CAMERA
<一句：鏡頭種類、跟隨方式、切點對什麼>

LIGHTING & PALETTE
<光的方向與硬度、時間、3–5 個主色>

AUDIO
<環境聲 / 動作音 / 對白 / 配樂各一句，或 No music>

AVOID
<3–6 個高機率、高損失的錯誤>
```

- `AVOID` 只放真正會毀片的東西（`slow motion, static tripod shots, text, watermarks, changing text spelling`），不列 20 條。
- 官方自然語言範例會在開頭寫「15s, 16:9」和整體風格句，再分段。

## 附：長自含式 hosted prompt（音樂驅動分段案例）與本 skill 規則的衝突對照

來源：LoveUolanda 13 段案例（貼文自述用 RunningHub 端點；作者稱有成片，我們沒看過，無 A/B）。他的 prompt 是分節的英文散文（段首權限 → 動作規則 → 局部時間軸 → 節拍網格 → 連續性檢查），不是 `[Shot N]` 格式。以下逐條說明和本 skill 其他規則的衝突，**依端點選用，不要合併**：

| 他的做法 | 本 skill 規則 | 怎麼取捨 |
|---|---|---|
| 單段約 5.9–6.8 千字元（890–1030 英文字） | 純文字 300–700 字；hosted API 上限 7000 字元 | 他的 13 段全在上限內，最長一段只差約 240 字元；journal 其他案例有 20–30 KB 的，**會超過**。先確認端點上限。本地 ComfyUI 與有參考素材時仍照 300–700 字，只寫新變化 |
| 10.3–13.6 秒內 5–8 個動作窗（0.02–3.4 秒，約六成落在 1.3–2.7 秒），但明寫硬切每段僅約 0–3 次 | 10 秒 3–4 shot；每 shot ≥ 2 秒、一個主動作 | 衝突在「窗」短於 2 秒，不在 shot 數；許多窗是「流入下一動作」而非切鏡。屬音樂剪輯例外，無音樂時照預算表；若成片糊成一團，砍到 3–4 個窗 |
| 寫 `Do not generate visible text or subtitles` | 官方回覆：不要在 prompt 裡寫「不要字幕」（提到反而召喚） | 沒有 A/B 證明他的寫法有效。本 skill 維持預設不寫；若真的出現字幕，照 `audio-and-dialogue.md` §7：減少台詞、改寫成不含文字的畫面描述，仍出現就後製裁掉 |
| 毫秒級節拍網格 | 自然語言模式用形容詞，不用數字 | 時間戳本來就受支援，但精度 0.1 秒已夠（見 `rhythm-and-pacing.md` §11） |
| 自由散文分節 | 本地 ComfyUI/導演台必須 `[Shot N] At MM:SS.mmm` 官方格式 | 本地用官方格式；hosted/自然語言端點可用分節散文 |
| 每段都重複身份與相機紀律 | 有參考圖時文字縮短、只寫新變化 | 自含式分段必須重複（每段獨立生成）；單段內不要重複 |
| 大量 `Do not` 禁令 | 負向要配正向替代 | 他的案例多數每條禁令都配了正向狀態定義；照 `motion-quality.md` §13 |

可信度標示：該作者提供完整 prompt 與（自述的）成片，但成片未隨 repo 發布，沒有同題 A/B 對照，也沒有量化評估；每條主張都視為「有人用過、看起來可行」，不是「已證實更好」。

## 平台參數地雷（社群回報）

- 時長：官方 4–15 s；部分端點 T2V/I2V 只到 10 s，Ref2VA 到 15 s。寫 15 秒分鏡前先確認端點。
- 解析度：官方 768p 可升 1440p；部分端點只接受 2K。
- 比例：T2V 必須明確指定（16:9 / 4:3 / 1:1 / 3:4 / 9:16 / 21:9），I2V/Ref2VA 可 adaptive；首幀模式比例跟圖。
- 首/尾幀模式不能與參考素材混用。
- 參考：≤9 圖、≤3 影片（各 2–15 s、總 ≤15 s）、≤3 音檔（同上）、總 ≤12 檔；音檔不能單獨。
- prompt ≤7000 字元。
- 中文台詞本地不出聲：用 repo tokenizer，`<d>[Chinese] …</d>`，注意 shell 編碼。

## 附：「寫實 15 秒電影腳本產生器」system prompt 與本 skill 的對照（2026-10-21）

來源：守富提供的通用 system prompt（六段輸出、每 shot 五小節、攝影/動作/聲音/負向/輸出規則共 12 節）。作者與成片不明，沒有 H3 A/B；被吸收的部分標 〔方法主張：守富提供的 15 秒腳本 system prompt，H3 未 A/B〕。**不採用的部分與原因**：

| 他的做法 | 本 skill 規則 | 取捨 |
|---|---|---|
| 一律輸出六段（含 `retention_analysis`） | 六段是 Ref2VA 格式；T2VA/I2VA/FL2VA 用官方三欄 | 不採用「一律六段」。沒參考素材時 `retention_analysis` 沒有東西可保留，照 §A 三欄 |
| `[Shot 1] — Title (00:00–00:02)` 標題＋區間 | `[Shot 1]` 不帶時間戳、之後 `[Shot N] At MM:SS.mmm`（本機實測切點 6/6 命中） | 不採用。標題字可能被當成畫面文字；區間格式未測 |
| `retention_analysis` 寫 `appears in [Shot 1] through [Shot N]: fully_preserved — …` | 官方標記同為 `fully_preserved / partially_preserved / attribute_transfer / weak_reference` | 標記一致，已涵蓋；「出現在哪幾個 shot」可當補充說明，不改官方句型 |
| `<Subject 3>` = 視覺風格 | 風格寫在 `detailed_description` 開頭一兩句與 `[Shot 1]` | 不採用把風格當 Subject（Subject 是「誰／什麼」的身份） |
| 每 shot 固定五小節（Camera / Visual Action / Environmental Interaction / Lighting / Transition） | Ref2VA `detailed_description` 350–500 英文字、純文字 300–700 | **可用，不設硬條件**（本機先導 T8，n=1×3 場景，非盲評）：agent 先自由寫，超過建議字數再請使用者決定；T8 在 15 s、≤5 shot、t2va 下可直接寫五個標籤小節；Ref2VA 短段（EP01，8–9 s）有實戰案例、待 A/B（實測 519–636 字，標籤字沒被畫進畫面，切點與劇情拍和散文平手）；B 勝在它逼你寫的光線/時段與連戲句（散文版沒寫光 → 夜景變白天、花瓣末鏡消失）。使用者選擇壓縮時（>5 shot 或有參考要縮字），改用散文但五項當檢查表且**光線與連戲兩項必寫**。原始紀錄在私有 repo，未公開 |
| 預設 15 秒 | 部分端點 T2V/I2V 只到 10 s；15 s ＝ 362 幀；15 s 內 4–6 shot | 保留「使用者沒說就 15 s」，但先確認端點與幀網格 |
| 長串渲染詞（global illumination、PBR、subsurface、anamorphic…） | 守富皮膚段；H3 由 Qwen3-VL 解析，形容詞不等於物理描述 | 他自己也說「選擇性使用」；只留跟畫面有關的（光的方向、鏡頭焦段），不堆 |
| 負向限制寫進各段、含「無字幕、無浮水印」 | 負向配正向；官方說不要寫「不要字幕」 | 「只列相關的」已涵蓋（格式 D `AVOID`、`motion-quality.md` §13）；字幕仍照 `audio-and-dialogue.md` §7 |
| 動作以 15 秒填滿多段 escalation | 10 s 3–4 shot、15 s 4–6 shot，每 shot 一個主動作 | escalation 結構採用（能量曲線，`shot-variety-and-staging.md` §8），數量照預算表 |
