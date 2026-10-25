# 運鏡手冊：17 式＋6 式 Loop Forge 鏡頭＋仙俠子彈時間（含 Colab 實測）

來源：老大的 H3 運鏡手冊（17 式）＋2026-10-25 Colab 兩輪實測（第 1 輪手冊原文 18 支：12 pass／5 partial／1 fail；第 2 輪改寫 11 支，全部找到可用寫法；第 3 輪 Loop Forge 配方 8 支，8/8 pass）。
第 3 輪配方來源：Loop Forge [loopforge0/minimaxh3-shots-skills](https://github.com/loopforge0/minimaxh3-shots-skills)（MIT），提示詞由其 build_prompt.py 產生，Ref2VA 單張角色參考圖。
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
| 9 | 滑動變焦 dolly zoom | ✅（第 3 輪） | 正向／反向兩種句型見下方「dolly zoom（第 3 輪驗證）」；不要再用這一行的舊寫法 | 第 1–2 輪舊寫法（只寫 zoom out while pushing in）會變推近＋分身或偏弱；第 3 輪 LF 句型兩方向都通過 |
| 10 | 急推 crash zoom | ✅ | Static medium shot, then at about 2.7s the camera crash-zooms in about 0.8 seconds to a close-up on the eyes and stops. | 連續急推，非跳切 |
| 11 | 手持晃動 shaky cam | ✅ | Handheld camera following SUBJECT through CROWD, constant jitter and drift in the frame. | 不用來掩蓋定格 |
| 12 | 追逐跟拍 chase | ✅ | The camera follows from behind as SUBJECT runs through SCENE, smooth continuous motion. | 無 |
| 13 | FPV 穿越機 | ✅（Turbo） | FPV drone flight at low altitude and high speed through SCENE, with obvious side-roll banking. | 無人物、無參考圖，走 Turbo |
| 14 | 視差橫移 parallax | ✅ | The camera trucks right with small amplitude at slow speed; the foreground pillars pass faster than the distant background; SUBJECT moves slowly. | 柱子可能完全遮住人物約 2 秒 |
| 15 | 過肩 OTS | 🟡 | Over-the-shoulder shot: blurred foreground shoulder of A (wearing OUTFIT, no jacket), B in focus speaking; the camera stays stable. | 會自行換服裝；對話者性別可能自動生成，要標 |
| 16 | 正反打 shot/reverse | ✅ | Two shots with a hard cut: shot 1 over A's shoulder at B; shot 2 over B's shoulder at A. | 過肩前景肩頭互換 |
| 17 | 子彈時間 bullet time | 🟡 | From the first frame everything is frozen mid-air (debris, hair, fabric). Only the camera moves: it trucks left while panning right, orbiting a full 360° around SUBJECT and ending back at the front. SCENE description required. | 原版髮絲仍飄；要「首幀即凍結」，補完整場景 |

仙俠子彈時間：身份優先於服裝——先寫「與 Picture 1 完全一致」、明寫髮長（短髮就寫短髮），再描述凍結元素（花瓣、衣擺、緞帶）。原版長髮換臉；改寫版 pass，花瓣大致定格、緞帶略變。

## 第 3 輪：dolly zoom 升為可用＋Loop Forge 6 式（2026-10-25 Colab）

### 第 3 輪共通要點
- **Omni 8 步就能出運鏡**（native、seed 42、euler+simple 實測）。Loop Forge 指出 4 步 turbo／Turbo LoRA 幾乎吃掉運鏡，建議 20 步；強運鏡不要用 4 步。
- **焦段名稱（24mm、85mm 等）無效**：不能當運鏡或景別的槓桿。景別要用文字寫出開場構圖（extreme wide、waist-up medium close-up、tight close-up）。
- **背景參考圖會讓運鏡幅度砍半**：只掛角色參考圖（臉、髮型、服裝），場景用文字寫。要鎖場景就得接受運鏡變小。
- 後端（Colab）秒數只收 **5/8/10/15**；yo-yo zoom 與三格分割必須 **8 秒**（5 秒放不下三段動作）。
- 運鏡寫成「TYPE＋AMPLITUDE＋SPEED」的動作句（with large amplitude at fast speed），不要只貼標籤；開場構圖要放在主角最大／最小的那一端（要結束在特寫就從遠景開；鎖主角的鏡頭開場即終景）。
- 不能要人「完全僵住」：會吃掉運鏡。主角寫 standing in place, breathing softly, blinking and shifting weight a little；dolly zoom 例外地要「站定不移步」。

### dolly zoom（第 3 輪驗證，✅ 可用）
要點順序：①先鎖主角大小與位置全程不變 ②面向鏡頭 ③站定不移步 ④才寫動詞對與背景變化 ⑤「Only the background transforms.」
- 背景要有**建物結構**（樓群、水塔、天線、圍籬、冷氣機一排），雪地森林這類低紋理背景會讓背景變化讀不出來。
- **開場即終景**（waist-up medium close-up），不要從遠景開，否則變成普通推近。
- **不要加背景參考圖**（運鏡砍半，這招沒有餘裕）。

正向（push in＋zoom out，背景退縮拉開；Vertigo 經典）：
```
Throughout the entire shot SUBJECT's size and position in frame stay exactly constant: he is framed identically in the last frame as in the first, neither closer nor further away, and never drifts from the centre of frame. He faces the camera squarely for the whole shot and never turns away from it. He stands rooted to one spot and does not step, lean or shift his weight. The camera pushes in while simultaneously zooming out at exactly the matching rate, so that the size of SUBJECT in frame is cancelled out entirely and does not change, while BACKGROUND_STRUCTURES behind him recede, shrink, and spread apart into much greater depth as the lens's focal length changes. Only the background transforms.
```
反向（pull out＋zoom in，背景壓近放大）：
```
...（前三句同上）... The camera pulls out while simultaneously zooming in at exactly the matching rate, so that the size of SUBJECT in frame is cancelled out entirely and does not change, while BACKGROUND_STRUCTURES behind him flatten, grow, and compress closer together as the lens's focal length changes. Only the background transforms.
```
實測：正向主角全程鎖住、水塔與樓群退縮拉開；反向主角鎖住、背景逐漸放大壓近（第 2 輪此方向失敗）。第 2 輪偏弱／失敗的原因是缺「鎖主角＋面向鏡頭＋站定」三句、背景缺結構。

### Loop Forge 6 式

| 運鏡 | 狀態 | 開場構圖 | 英文骨架 | 要點／風險 |
|---|---|---|---|---|
| snorricam（身綁鏡頭） | ✅（晃動偏溫和） | waist-up medium close-up，主角邊走 | SUBJECT walks steadily forward while the camera, fixed rigidly to him, holds his face locked dead-centre at exactly the same size and position throughout; the whole background lurches, sways and swings behind him with every stride. | 主角必須自己移動；表演寫 eyes locked forward, jaw tight, never once looking at the camera，不要加轉身；不要在器材欄寫 body rig（會被畫出來）；實測晃動感比預期溫和 |
| eyes-in（推進眼睛） | ✅ | waist-up medium close-up | The camera pushes in with large amplitude at slow speed toward his face and keeps going past it until his right eye, the iris and pupil filling the view fills the entire frame edge to edge. | 全身→中景→特寫→落在雙眼，連續無跳切；非人物主體要指定 DETAIL（如某個標記） |
| aerial pullback（高空後拉） | ✅ | waist-up medium close-up | The camera pulls out with large amplitude at fast speed while pedestalling up, rising and retreating until SUBJECT is a small lone figure far below and the whole LOCATION opens out around him. | 用 pull out（移動）不是 zoom out（只會平面放大）；LOCATION 寫主角所在的大場域 |
| super dolly in（超長推軌） | ✅（地理需注意） | extreme wide：looks straight down THE_SPACE, NEAR_OBJECTS rising close at the left and right edges of frame, SUBJECT small and distant at the far end | The camera pushes in with large amplitude at fast speed, charging the entire length of THE_SPACE toward him: NEAR_OBJECTS sweep outward past the edges of frame and out of shot as the camera passes them, FURTHER_OBJECTS rush by on both sides and GROUND streams underneath, and the move ends in a tight close-up with his face filling the frame. | **THE_SPACE 等空間槽位必須和主角所在地同一地點**，否則地理會怪（實測填夜市巷、主角在屋頂→夜市接屋頂）；一定要有近景左右兩物件掃出畫面，否則退化成急推 |
| yo-yo zoom（溜溜球變焦） | ✅（需 8 秒） | tight close-up fills the frame with his face | The camera begins in a tight close-up on his face, then zooms out, starting slowly and accelerating harder and harder as it goes until the whole view smears into motion blur and SUBJECT has fallen away into the far distance, a tiny figure PLACE. The camera holds there for about a second, then zooms back in with large amplitude at fast speed, snapping across the entire distance in a single instant to land tight on his face again exactly as it began. | **必須 8 秒**；加速要寫成加速；回程寫「單一瞬間跨越全程」；停留時間 H3 自己決定，別刪 hold 句（只會把空檔移到開頭），要精準就後製剪 |
| 三格分割畫面 split screen | ✅（需 8 秒，layout-only） | 自訂：三個等寬直格 | The frame is divided into three equal vertical panels side by side, separated by thin black gutters. The left panel holds SUBJECT, ACTION. Every panel is locked off and completely static; nothing pans, zooms or moves at any point. The three panels open one after another. The left panel plays from the very first frame, showing PANEL_1_ANGLE, while the centre and right panels are solid black. The centre panel stays solid black and then comes on, showing the same moment from PANEL_2_ANGLE. The right panel stays solid black longer than the centre one and comes on last, showing PANEL_3_ANGLE. For the remainder of the shot all three panels play together in perfect sync, the same continuous ACTION_SHORT at the same instant from three different angles. | **必須 8 秒**；只是版面效果，格內不運鏡；三格要同一瞬間同一動作的三個角度；只寫順序不寫秒數（H3 不照秒數，約 2.5 秒內全亮）；未亮的格每格都寫 solid black |

實測（第 3 輪，主角同一張參考圖）：snorricam 夜市巷臉鎖中央、背景晃動流過；eyes-in 連續推近落在眼睛；aerial pullback 特寫→全身→高空俯拍街區、主角縮成小點；super dolly in 從夜市上空推到屋頂主角近景（地理怪）；yo-yo zoom 特寫→急拉遠景→停留→急推回特寫、有動態模糊；三格分割依序亮格（側面→正面螢幕光→背影），最後三格同步打字。

## 場景意圖 → 運鏡選用指南

| 意圖／節點 | 首選 | 備選 | 禁用／慎用 |
|---|---|---|---|
| 開場建立 | 緩推、視差橫移 | 追逐跟拍遠景 | 急推 |
| 角色登場 | 揭示、仰搖 | 甩鏡落定 | 手持 |
| 緊張／不安 | 荷蘭角（固定斜角） | 手持晃動 | 對白 CU 上用強運鏡 |
| 揭露／發現 | 揭示、移焦 | 急推到眼睛 | 同段再加第二個強運鏡 |
| 震驚 | 急推、dolly zoom 正向 | eyes-in、失衡瞬間荷蘭角 | 連續重複同一運鏡 |
| 孤立／渺小 | 頂拍上升、aerial pullback | 高角度俯拍 | 近景手持 |
| 回憶／主觀 | POV | 移焦、eyes-in（進入內心） | 無 |
| 壓迫／被逼近 | dolly zoom 反向（背景壓近） | 急推 | 對白 CU |
| 失控／醉／恐慌 | snorricam | 手持晃動 | 站定不動的主角（snorricam 要主角自己移動） |
| 衝向目標／宿命感 | super dolly in | 急推 | 空間槽位與主角所在地不同 |
| 平行行動／多視角同一瞬間 | 三格分割畫面（8 秒） | 正反打 | 要精準時間點的揭示（時間不可控） |
| 對峙 | 正反打 | 過肩 | 三主體以上強運鏡 |
| 追逐／動作 | 追逐跟拍、FPV | 甩鏡轉場 | 子彈時間（凝滯破壞速度感） |
| 反轉／高潮 | 子彈時間、急推 | dolly zoom、yo-yo zoom | 同段多個強運鏡 |
| 仙俠大招定格 | 仙俠子彈時間 | 環繞 | 服裝描述壓過參考臉 |
| 對白 | 固定機位、正反打 | 過肩 | 任何強運鏡 |
| 日常 | 固定、緩推 | 視差橫移 | 子彈時間、甩鏡 |

不該用強運鏡：段首或鏡首接上一格、纏繞特寫、對白 CU、最大衝擊鏡、三主體以上、≤2 秒子鏡、拿手持掩蓋定格。

## 與 camera-and-transitions.md 對帳
- §2 官方 20 種運鏡不含子彈時間、dolly zoom、crash zoom、FPV、parallax、OTS、正反打；以本手冊為準。
- orbit 與 truck＋pan 並用：子彈時間用 truck left while panning right。
- §10 rack focus 已實測 ✅（原寫「H3 未實測」，以本手冊為準，仍算該鏡唯一鏡頭事件）。
- §2 對帳補充：dolly zoom 第 3 輪已驗證可用（以本手冊句型為準）；snorricam、eyes-in、aerial pullback、super dolly in、yo-yo zoom、三格分割為新增。
- 未測：緩推、後退跟拍、後拉、震屏，以及 2–3 秒子鏡版；LF 6 式只測過人物主體與預設方向（eyes-in 右眼）。
