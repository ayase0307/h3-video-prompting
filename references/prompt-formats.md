# 四種 prompt 格式：什麼時候用哪一種

| 格式 | 用在哪 | 特徵 |
|---|---|---|
| A. 官方三欄（Base） | 本地 ComfyUI / 開源權重 / 導演台；hosted API 要精確切點與 speaker 時 | `integrated_multimodal_description` + `overall_soundscape` + `non_diegetic_music`；I2VA/FL2VA/L2VA 前面加對齊句 |
| B. 官方六段（Ref2VA） | 任何有參考圖/影片/音檔的本地生成；hosted 多參考任務 | `subject_definitions / summary / retention_analysis / detailed_description / overall_soundscape / non_diegetic_music` |
| C. 官方中文三段 | 海螺 App / MiniMax Design / 開放平台自然語言（有 Context-IR 改寫） | 【參考素材說明】【核心創意】【畫面過程描述】 |
| D. 社群區塊式 | hosted API / 第三方平台自然語言 | `SCENE / SHOT BREAKDOWN / CAMERA / LIGHTING & PALETTE / AUDIO / AVOID`，開頭一行 `Duration | Aspect ratio | Style` |

規則：**本地沒有 Context-IR 改寫器，A/B 是硬需求。** hosted 端點會把 C/D 改寫成 A/B，但要精確控制 cut 時間、speaker、字幕、配樂時，直接寫 A/B 更穩（社群實測：寫了時間戳的 cut 誤差約 0.12 s；沒寫就一鏡靜止到底）。

A/B 的完整規則在官方 skill `h3-prompt-writing` 的 `references/base-en.txt` 與 `ref-en.txt`；本檔只列決策與差異。

## A. 官方三欄要點

- T2VA 沒有對齊句；I2VA：`For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.`；FL2VA/L2VA 用「How the reference pictures align with the target video — …」句，秒數兩位小數，對齊實際有效時長。
- `[Shot 1]` 不帶時間戳並先寫風格（`Live-action, cinematic` / `2D-animated` / `3D CG` / `claymation` / `watercolor` / `vintage film`）；之後 `[Shot N] At MM:SS.mmm,` 嚴格遞增。
- 純文字 300–700 英文字；有參考時縮短。
- 結尾兩欄不能省，沒有就 `N/A`。

## B. 六段式要點

- `<Subject N>` 是語義身份（誰），`<Picture N>` 是檔案（哪張圖）；同一角色多張圖合併成一個 Subject：`<Subject 1> is the same woman established by <Picture 1>, <Picture 2>, and <Picture 3>.`
- 圖只有當首幀/尾幀/關鍵幀/構圖錨/storyboard 時才獨立追蹤 Picture；只提供長相的圖寫進 Subject 定義即可。
- `summary` 開頭方括號任務型：`keyframe completion / reference generation / video editing / video continuation / audio reuse / audio reference`，可用 ` + ` 組合。
- `retention_analysis` 標記：視覺 `fully_preserved / partially_preserved / attribute_transfer / weak_reference`；音訊 `fully_copy / partially_copy / reference / weak_reference`。
- `detailed_description` 在 `[Shot 1]` 之前先用一兩句英文定風格；生成任務 350–500 英文字。
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

## 平台參數地雷（社群回報）

- 時長：官方 4–15 s；部分端點 T2V/I2V 只到 10 s，Ref2VA 到 15 s。寫 15 秒分鏡前先確認端點。
- 解析度：官方 768p 可升 1440p；部分端點只接受 2K。
- 比例：T2V 必須明確指定（16:9 / 4:3 / 1:1 / 3:4 / 9:16 / 21:9），I2V/Ref2VA 可 adaptive；首幀模式比例跟圖。
- 首/尾幀模式不能與參考素材混用。
- 參考：≤9 圖、≤3 影片（各 2–15 s、總 ≤15 s）、≤3 音檔（同上）、總 ≤12 檔；音檔不能單獨。
- prompt ≤7000 字元。
- 中文台詞本地不出聲：用 repo tokenizer，`<d>[Chinese] …</d>`，注意 shell 編碼。
