# 範例：從 spec 卡到 H3 三欄 prompt（T2VA，10 s，4 shot，無配樂）

Brief：深夜小餐館，Mei 在等一個不會來的人。門鈴響了，進來的是外送員。角色不說話。

**Spec 卡（規劃用，不送出）**

| 欄 | Shot 1（0–2.5） | Shot 2（2.5–5.0） | Shot 3（5.0–7.5） | Shot 4（7.5–10.125） |
|---|---|---|---|---|
| 節拍目的 | 建立：等待 | 懷疑：時間流逝 | 揭露前：希望（能量峰） | 結果：落空（收） |
| 狀態變化  起→觸發→結果 | 手機亮 → 讀訊息 → 翻面蓋住 | 最後一縷熱氣 → 消失 → 她把杯子推向空位 | 門鈴 → 猛轉頭 → 半站起、撞桌 | 看見外送員 → 肩膀垮下 → 坐回 |
| 景別 | 遠景 | 特寫 | 中景 | 中遠景 |
| 角度 | 平視（隔窗，街上） | 高角度（俯看桌面） | 平視（櫃台後，方位轉約 90°） | 低角度（貼地） |
| 運鏡 | 推近，small/slow，停在窗框 | static | static（峰值 shot 鏡頭靜止） | 環繞 = truck left + pan right，small/slow，揭示門口 |
| 主體／視線 | Mei，視線向下看手機 | 物件：咖啡杯和空位 | Mei，視線看向門 | 門口的外送員；Mei 的視線落回手機 |
| 人物—環境關係 | 對面的空位和沒動過的咖啡 | 同左（主體化） | 門 | 外送員不是她等的人 |
| 景深層次（前景一物） | 玻璃上的失焦雨滴 | 畫面邊緣她失焦的手 | 失焦的鍍鉻紙巾架 | 失焦的深色桌腳 |
| 光線路徑 | 紅色霓虹 → 濕玻璃 → 只照她左臉 | 吊燈 → 桌面 → 碟子上一圈硬光 | 門外冷藍街光 → 地板 → 爬上她的臉 | 門縫的光變窄 → 消失 |
| 媒介 | 實拍單一媒介（不寫） | — | — | — |
| 聲音觸發 | 手機震一下 | 安靜 | 門鈴、雨聲變大、杯碟碰撞 | 腳步、紙袋、關門 |

**跨 shot 變化核對**（四軸：景別、角度、運鏡類型、主體／視線；相鄰至少 2 項不同，其中 ≥1 項是實質變化：景別跳 ≥2 級、角度或方位變 >30°，或主體換人／換物）

| 相鄰對 | 景別 | 角度 | 運鏡類型 | 主體／視線 | 不同項數 | 實質變化 |
|---|---|---|---|---|---|---|
| S1→S2 | 遠→特寫 ✔ | 平視→高角度 ✔ | 推近→static ✔ | Mei→杯子 ✔ | 4 | 景別跳 5 級；主體換物 |
| S2→S3 | 特寫→中 ✔ | 高角度→平視 ✔ | static→static ✘ | 杯子→Mei ✔ | 3 | 景別跳 2 級；方位轉約 90° |
| S3→S4 | 中→中遠 ✔（只跳 1 級） | 平視→低角度 ✔ | static→環繞 ✔ | Mei→外送員 ✔ | 4 | 角度 >30°；主體換人 |

能量曲線：S1 低 → S2 最低（靜止）→ S3 峰值（門鈴，鏡頭靜止，只讓她動）→ S4 收（慢環繞揭露，停在殘局）。

**壓縮紀錄（套用 動作 > 運鏡 > 光 > 媒介）**：
- 媒介欄整欄不寫，因為是實拍單一媒介。
- 字數 449，沒有超過 700，所以景深和光線都不砍，每個 shot 各保留一個前景子句和一句光。
- 關係欄壓成一個名詞片語 `an empty seat with an untouched cup of coffee`，只在 S1 出現一次。
- 每個 shot 留一句光線。
- 聲音不放進畫面欄，全部移到 `overall_soundscape`。

**H3 prompt**（`integrated_multimodal_description` 449 英文字、`overall_soundscape` 90 字，均以 `wc -w` 核對）

```text
integrated_multimodal_description: [Shot 1] Live-action, cinematic, night. A wide shot from the wet street looks through a rain-streaked diner window: out-of-focus raindrops on the glass sit in the foreground, Mei sits alone in a window booth in the middle ground, and the warm counter glows softly in the background. Mei is a woman in her late twenties with a short black bob, a mustard raincoat folded beside her; she stays silent throughout the video with her mouth naturally closed. Across from her is an empty seat with an untouched cup of coffee. Red neon from the diner sign outside passes through the wet glass and lights only the left side of her face. First her phone lights up on the table, then she reads it, as her thumb stops moving; finally she turns the phone face down and rests her hand on it. The camera pushes in with small amplitude at slow speed toward her through the glass, ending at the window frame.

[Shot 2] At 00:02.500, the shot cuts to a high-angle close-up looking down on the table: the untouched coffee cup on the empty side, her out-of-focus hand in the foreground at the edge of the frame. A single pendant lamp above the table throws a hard round pool of light onto the saucer. First a last thin thread of steam rises from the coffee, then it thins and disappears, as her fingers slide the cup a few centimeters toward the empty seat and let go. The camera holds a static shot.

[Shot 3] At 00:05.000, the shot cuts to an eye-level medium shot from behind the counter, Mei framed side-on in the middle ground, a blurred chrome napkin holder in the foreground. The door bell rings off-screen. First her head snaps toward the door, then she half rises from the booth, as her knee knocks the table and the cup rattles on its saucer. Cold blue street light spills through the opening door, runs across the floor, and climbs onto her face, replacing the red neon. The camera holds a static shot.

[Shot 4] At 00:07.500, the shot cuts to a low-angle medium-wide shot from near the floor beside the booth, a dark table leg out of focus in the foreground. The camera trucks left with small amplitude at slow speed while panning right to keep Mei centered, revealing the open doorway behind her: a delivery courier in a dripping yellow poncho holds a paper bag and looks around the room. Mei's shoulders drop, then she sinks back onto the seat, as her gaze falls to the face-down phone. The cold door light narrows to a thin strip and vanishes as the door swings shut behind the courier.

overall_soundscape: Steady rain taps on the window glass under a low refrigerator hum and the faint sizzle of a grill inside the diner. A single short phone vibration buzzes against the table in the first shot. The room goes quiet around the fading coffee. A bright brass door bell rings, the door opens and the rain is suddenly louder, the cup rattles on its saucer, the courier's wet footsteps and the rustle of a paper bag follow, then the door thuds shut and the rain drops back to a muffled patter.

non_diegetic_music: N/A
```

自檢結果：
- 切點 2.500、5.000、7.500，嚴格遞增，間距都是 2.5 s；最後一個 shot 是 2.625 s。
- `[Shot 1]` 沒有時間戳，shot 內沒有第二個 `At`。
- 每個 shot 剛好一個運鏡句。S4 的 truck + pan 是官方建議的環繞寫法，算一個運鏡。
- grep 環繞類詞為 0；全文沒有 music、score 等詞。
