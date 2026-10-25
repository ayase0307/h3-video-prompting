# 運鏡手冊：17 式＋仙俠子彈時間（含 Colab 實測）

來源：老大的 H3 運鏡手冊（17 式）＋2026-10-25 Colab 兩輪實測（第 1 輪手冊原文 18 支：12 pass／5 partial／1 fail；第 2 輪改寫 11 支，全部找到可用寫法）。
驗證狀態：✅ 實測通過、🟡 需用改寫版、🧪 實驗性（效果弱）、⚪ 未實測。

## 共通規則（每式都適用）
- 每個 shot 一個強運鏡；同一段最多 1–2 個強運鏡。對白 CU、最大衝擊鏡、≤2 秒子鏡、三主體以上、纏繞特寫不用強運鏡。
- 必須帶完整場景段。手冊原版沒寫場景時，參考圖灰底會滲進畫面（cm04、cm09、cm10 實測）。「只鎖人物（臉、髮型、服裝），不參考背景」。
- 「全程維持」類（固定斜角、純垂直上升、俯搖）模型會演成漸變運動：寫「from the first frame, held throughout」，並加禁止反向動作的句子。
- 後端秒數只收 5/8/10/15（Colab）；Omni 必須有參考圖，無參考圖的運鏡（FPV）改走 Turbo。家機 FreeVideo 幀數 17n+5、無此限制。
- Colab 的時間點結論套在 2–3 秒子鏡時，可信度降半級。
- 過肩、仙俠換裝：重申參考服裝，服裝描述不得壓過參考臉。

## 17 式

| # | 運鏡 | 狀態 | 英文骨架（把 SUBJECT／SCENE 換成實際內容） | 風險 |
|---|---|---|---|---|
| 1 | 甩鏡 whip pan | ✅ | Start framed on SCENE_A. The camera whips right at very high speed with strong horizontal motion blur, landing on SUBJECT in a medium shot and holding steady there until the end. | 落點要寫清楚並停住 |
| 2 | 荷蘭角 dutch angle | 🟡 | 固定斜角：Shot as a canted frame from the first frame: every vertical line leans 30° to the left, like a crooked printed photo; the camera stays static and the tilt is held throughout. 失衡瞬間版：The frame starts level, then snaps in a 0.5-second fast roll into a tilted angle and locks there. | 只寫 tilt 角度會被忽略；原版會演成漸變 roll；服裝可能變色，重申服裝 |
| 3 | 移焦 rack focus | ✅ | The camera holds a static shot. Focus starts on FOREGROUND_OBJECT near the lens, then shifts a short distance back to SUBJECT's face as the object melts into soft bokeh. | 起點終點都要是可指認物件；算該鏡唯一鏡頭事件 |
| 4 | 揭示 reveal | ✅（需場景） | A foreground element (e.g. a pillar) blocks the lens from SUBJECT. The camera trucks slowly left, locked in one direction; the element slides out and SUBJECT comes into sharp focus on the right of frame. | 沒場景會灰底 |
| 5 | 第一人稱 POV | ✅ | First-person view: the camera pushes open the door and walks toward SUBJECT, with slight natural handheld sway; SUBJECT looks up into the lens. | 鏡頭人物不入鏡，不掛其參考圖 |
| 6 | 頂拍上升 top-down | 🟡 | The camera points straight down for the whole shot, the horizon never appears. The camera pedestals up vertically; SUBJECT at the center circle shrinks as the whole court lines unfold. | 原版會變前傾俯仰；人物會變很小 |
| 7 | 仰搖 tilt up | ✅ | The camera tilts up from SUBJECT to the TOP_OBJECT and stops there. | 人物會出畫（預期） |
| 8 | 高角度俯拍 high angle | 🟡 | High-angle shot looking down on SUBJECT, then the camera tilts down to LANDING_OBJECT on the ground. | 俯搖要給落點物件；人物會低頭看不到臉 |
| 9 | 滑動變焦 dolly zoom | 🧪 | The camera zooms out while pushing in, SUBJECT's face stays the same size while the corridor behind stretches deeper (vertigo effect). | pull out＋zoom in 無效；效果偏弱；原版會變推近＋分身。不保證，可降級 push-in |
| 10 | 急推 crash zoom | ✅ | Static medium shot, then at about 2.7s the camera crash-zooms in about 0.8 seconds to a close-up on the eyes and stops. | 連續急推，非跳切 |
| 11 | 手持晃動 shaky cam | ✅ | Handheld camera following SUBJECT through CROWD, constant jitter and drift in the frame. | 不用來掩蓋定格 |
| 12 | 追逐跟拍 chase | ✅ | The camera follows from behind as SUBJECT runs through SCENE, smooth continuous motion. | 無 |
| 13 | FPV 穿越機 | ✅（Turbo） | FPV drone flight at low altitude and high speed through SCENE, with obvious side-roll banking. | 無人物、無參考圖，走 Turbo |
| 14 | 視差橫移 parallax | ✅ | The camera trucks right with small amplitude at slow speed; the foreground pillars pass faster than the distant background; SUBJECT moves slowly. | 柱子可能完全遮住人物約 2 秒 |
| 15 | 過肩 OTS | 🟡 | Over-the-shoulder shot: blurred foreground shoulder of A (wearing OUTFIT, no jacket), B in focus speaking; the camera stays stable. | 會自行換服裝；對話者性別可能自動生成，要標 |
| 16 | 正反打 shot/reverse | ✅ | Two shots with a hard cut: shot 1 over A's shoulder at B; shot 2 over B's shoulder at A. | 過肩前景肩頭互換 |
| 17 | 子彈時間 bullet time | 🟡 | From the first frame everything is frozen mid-air (debris, hair, fabric). Only the camera moves: it trucks left while panning right, orbiting a full 360° around SUBJECT and ending back at the front. SCENE description required. | 原版髮絲仍飄；要「首幀即凍結」，補完整場景 |

仙俠子彈時間：身份優先於服裝——先寫「與 Picture 1 完全一致」、明寫髮長（短髮就寫短髮），再描述凍結元素（花瓣、衣擺、緞帶）。原版長髮換臉；改寫版 pass，花瓣大致定格、緞帶略變。

## 場景意圖 → 運鏡選用指南

| 意圖／節點 | 首選 | 備選 | 禁用／慎用 |
|---|---|---|---|
| 開場建立 | 緩推、視差橫移 | 追逐跟拍遠景 | 急推 |
| 角色登場 | 揭示、仰搖 | 甩鏡落定 | 手持 |
| 緊張／不安 | 荷蘭角（固定斜角） | 手持晃動 | 對白 CU 上用強運鏡 |
| 揭露／發現 | 揭示、移焦 | 急推到眼睛 | 同段再加第二個強運鏡 |
| 震驚 | 急推 | 失衡瞬間荷蘭角 | 連續重複同一運鏡 |
| 孤立／渺小 | 頂拍上升 | 高角度俯拍 | 近景手持 |
| 回憶／主觀 | POV | 移焦 | 無 |
| 對峙 | 正反打 | 過肩 | 三主體以上強運鏡 |
| 追逐／動作 | 追逐跟拍、FPV | 甩鏡轉場 | 子彈時間（凝滯破壞速度感） |
| 反轉／高潮 | 子彈時間、急推 | 滑動變焦（實驗） | 同段多個強運鏡 |
| 仙俠大招定格 | 仙俠子彈時間 | 環繞 | 服裝描述壓過參考臉 |
| 對白 | 固定機位、正反打 | 過肩 | 任何強運鏡 |
| 日常 | 固定、緩推 | 視差橫移 | 子彈時間、甩鏡 |

不該用強運鏡：段首或鏡首接上一格、纏繞特寫、對白 CU、最大衝擊鏡、三主體以上、≤2 秒子鏡、拿手持掩蓋定格。

## 與 camera-and-transitions.md 對帳
- §2 官方 20 種運鏡不含子彈時間、dolly zoom、crash zoom、FPV、parallax、OTS、正反打；以本手冊為準。
- orbit 與 truck＋pan 並用：子彈時間用 truck left while panning right。
- §10 rack focus 已實測 ✅（原寫「H3 未實測」，以本手冊為準，仍算該鏡唯一鏡頭事件）。
- 未測：緩推、後退跟拍、後拉、震屏，以及 2–3 秒子鏡版。
