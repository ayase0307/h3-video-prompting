# 範例：Seedance 時間碼 + @圖片N 轉 H3 Ref2VA 六段式

**Seedance 原文**（本審查自寫的示範，不取自任何來源）：

```text
@圖片1 為首幀，@圖片2 為女主角形象。10 秒，16:9，電影感。
0-3秒：鏡頭環繞天台上的女生，她慢慢轉身望向城市，風吹起頭髮，鏡頭同時推近到她的臉。
3-5秒：俯拍，她走向欄杆，鏡頭升高。
5-8秒：特寫她的手抓緊欄杆，焦點轉到遠處城市。
8-10秒：鏡頭拉遠成全景，城市燈光一盞盞亮起，配樂漸強。
```

**轉換步驟和診斷**

| 原文 | 問題 | H3 處理 |
|---|---|---|
| `0-3秒` | 寫成區間 | 改成 `[Shot 1]`，不寫時間戳 |
| `3-5秒`、`5-8秒`、`8-10秒` | 寫成區間 | 只取起點：`[Shot 2] At 00:03.000`、`[Shot 3] At 00:05.000`、`[Shot 4] At 00:08.000`。每段都 ≥2 s，最後一段 2.125 s |
| @圖片1 首幀 | 當畫面錨點用 | 獨立成 `<Picture 1>`，寫 `the shot begins from <Picture 1>`；summary 前綴加 `keyframe completion` |
| @圖片2 角色形象 | 只提供外觀 | 依 ref-en §2.2，不獨立成 Picture 行，寫進 `<Subject 1> is … in <Picture 2>`；前綴加 `reference generation` |
| Shot 1：環繞 + 推近 | 兩個運鏡 | 只留環繞，改成 truck left + pan right；推近刪掉，「靠近她」改由 Shot 3 特寫交付 |
| Shot 2：俯拍 + 升高 | 俯拍不是運鏡 | 俯拍寫成 `high-angle wide shot`（角度），升高寫成 `pedestals up`（唯一運鏡） |
| Shot 3：焦點轉移 | 算鏡頭事件 | 鏡身 static，焦點轉移就是該 shot 唯一的鏡頭事件（H3 未實測，失敗就刪掉，只留 static） |
| Shot 4：配樂漸強 | 寫在畫面裡 | 移到 `non_diegetic_music`，寫進場時間 |
| 中文 | — | 英文改寫；`detailed_description` 依官方 350–500 字，不套純文字的 300–700 |

**跨 shot 變化核對**

| 相鄰對 | 景別 | 角度 | 運鏡 | 主體／視線 | 實質變化 |
|---|---|---|---|---|---|
| S1→S2 | 中→遠 | 平視→高角度 | 環繞→升高 | 同一人（轉身→走路） | 角度 >30° |
| S2→S3 | 遠→特寫 | 高角度→平視 | 升高→static＋焦點 | 人→手 | 景別跳 ≥2 級 |
| S3→S4 | 特寫→遠 | 平視（背後） | static→拉遠 | 手→人加城市 | 景別跳 ≥2 級 |

**H3 prompt**（`detailed_description` 407 英文字，`wc -w` 核對）

```text
subject_definitions:
<Subject 1> is the young woman in <Picture 2>, with shoulder-length black hair, a long beige trench coat, and white sneakers.
<Picture 1> is the first frame of [Shot 1], showing <Subject 1> standing on a concrete rooftop at dusk with her back to the camera, a metal railing and the city skyline beyond her.

summary:
[keyframe completion + reference generation] The target video begins from <Picture 1> and follows <Subject 1> on a city rooftop at dusk across four shots: she turns toward the skyline, walks to the railing, grips it as the focus moves to the distant towers, and is left small in a wide frame as the city lights switch on. <Picture 2> provides the identity and wardrobe of <Subject 1>.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3], [Shot 4]): fully_preserved - the face, shoulder-length black hair, long beige trench coat, and white sneakers from <Picture 2> are retained.
<Picture 1> ([Shot 1] first frame): fully_preserved - the rooftop layout, railing position, skyline, and dusk light are retained as the opening frame.

detailed_description:
The target video is live-action and cinematic, with cool dusk light and a slightly desaturated palette.
[Shot 1] The shot begins from <Picture 1>: a medium shot on a concrete rooftop at dusk. <Subject 1>, the young woman with shoulder-length black hair in a long beige trench coat, stands near the center with her back to the camera, a metal railing and the city skyline beyond her. She stays silent throughout the video with her mouth naturally closed. The last orange light from the low sun behind the towers rims her hair and shoulders. First she turns slowly to her right toward the skyline, then the wind lifts her hair and the hem of her coat, as her face settles in profile. The camera trucks left with small amplitude at slow speed while panning right to keep her centered, moving around her as a railing post slides past out of focus in the foreground, until the skyline opens up behind her profile.
[Shot 2] At 00:03.000, the shot cuts to a high-angle wide shot looking down on the rooftop past the out-of-focus edge of a ventilation unit in the foreground: first <Subject 1> walks four steps from the center toward the railing, then stops one pace short of it, as the low sun ahead of her stretches her long shadow back across the concrete toward the camera. The camera pedestals up with small amplitude at slow speed, revealing the rooftop ventilation units and the street far below.
[Shot 3] At 00:05.000, the shot cuts to an eye-level close-up of <Subject 1>'s right hand on the cold metal railing, the city lights soft and blurred in the background. Cool sky light from above catches the top edge of the railing and her knuckles. First her fingers tighten around the bar until the knuckles pale, then the focus shifts from her hand to the distant towers, as her hand softens into a blur in the foreground. The camera holds a static shot.
[Shot 4] At 00:08.000, the shot cuts to a wide shot from behind <Subject 1> at the railing, the dark edge of a ventilation unit out of focus in the foreground. The camera pulls out with large amplitude at slow speed, leaving her small at the lower center of the frame, as the windows of the city light up block by block from left to right and the last orange band on the horizon fades to blue.

overall_soundscape:
Steady wind sweeps across the rooftop over distant traffic and a faint siren far below. Her coat fabric flaps once as she turns. Four soft footsteps land on the concrete. A light metallic creak sounds as her hand tightens on the railing. At the end the wind settles and the low hum of the city rises slightly.

non_diegetic_music:
A sparse piano-and-strings cue enters softly at 00:08.000 and swells gently until the end of the video.
```

說明：
- 本地 ComfyUI 的接法：`ref_image_0` 對 `<Picture 1>`（首幀），`ref_image_1` 對 `<Picture 2>`（角色）。
- hosted 端點有些不允許「首尾幀模式」和參考素材混用（prompt-formats 地雷段）。這時改成兩張都當參考：拿掉 `keyframe completion`，`<Picture 1>` 改當構圖錨點，寫 `the shot's keyframe corresponds to <Picture 1>`。是否被接受，要看端點。
