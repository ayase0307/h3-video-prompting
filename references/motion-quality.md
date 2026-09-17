# 動作品質：讓身體有重量、材質會回應、表情有意圖

來源：官方 3d-animation-short-generator shot-table-spec（squash/stretch、anticipation、overshoot、follow-through）、videotoprompt、morphed、Kapwing、debutify 對白表演、ambienceai 真人照片動畫、virse motion transfer、Hailuo 知識庫 speed ramp、stimQQ/BeatAPI 社群 prompt 庫。

## 1. 動作弧線：起手 → 執行 → 接觸 → 收勢

真人或動畫都一樣，一個「動作」有四段。只寫中間那段，模型會自己補前後，常補錯。

| 段 | 寫什麼 | 範例 |
|---|---|---|
| 起手 anticipation | 重心轉移、蓄力、視線先到 | `she plants her left foot and drops her weight before the swing` |
| 執行 commitment | 肢體路徑、方向、速度形容詞 | `the right arm sweeps across her body at explosive speed` |
| 接觸 impact | 碰到什麼、反作用 | `the flat of the blade meets the knife with a sharp ring; her wrist absorbs the shock` |
| 收勢 settle / follow-through | 多餘動量怎麼消、回到什麼姿勢 | `the momentum carries her half a step forward before she resets her stance` |

品牌片 skill 的 motion intent 詞：`setup, anticipation, commitment, impact, brake, settle`。動畫 skill 的表演詞：`squash-and-stretch, anticipation, overshoot, follow-through, overlap, arcs, clear silhouette`。

## 2. 重量與動量

- 寫重心：`weight drops onto the left knee`、`leans into the wind`、`shifts his weight forward, then jumps`。
- 寫慣性：`lands with bent knees, rolls over one shoulder, and rises into a sprint without pausing`。
- 車輛與載具：`real weight in the lean`、`tires smoking`、`sparks off the footpeg`、`continuous forward velocity throughout`；轉向要寫 `drifts through the final bend` 而不是「帥氣過彎」。
- 動物：寫步態與腳的觸地順序 `steps cautiously onto a wet rock, shifts its weight forward, then jumps; its paws displace moss on landing`。

## 3. 環境與材質要「回應」動作

Hailuo 系列對水、布、髮、粒子、衝擊特別強。每個主動作配一個環境反應，寫因果不寫形容詞。

| 材質 | 可寫的回應 |
|---|---|
| 水 / 液體 | `water sheets down the faceted sides and splits at each edge`、`a shallow pool forms and spreads outward`、`condensation streaks down the glass` |
| 布料 | `the jacket rides up`、`coat and scarf stream behind him`、`heavy wool snaps once as it is shaken open, then rustles as it settles` |
| 頭髮 | `wind lifts her hair once`、`a strand shifts near her temple` |
| 粒子 | `dust lifts where the foot pivots`、`fine sand curls around his boots with each step`、`powder drifts down through the frame` |
| 光 | `a narrow highlight travels across the brushed metal`、`highlights travel across the surface as it turns` |
| 硬物 | `the chocolate bar snaps cleanly along a scored line, fine crumbs fall`、`the glass tips, falls, and cracks spread as fragments slide outward` |

不要堆疊無關的效果來「顯得細」。一個主動作 + 一到兩個回應。

## 4. 手與物件互動

最容易壞的地方。規則：**哪隻手、握哪裡、動到哪、放哪裡**。

```text
✅ She reaches forward with her right hand, grips the bottle around the upper third,
   lifts it to chest height, and rotates it until the label faces camera.
✅ Two hands hold a dark chocolate bar over a slate board. First the bar is flexed,
   then it snaps cleanly along a scored line.
❌ she picks up the bottle / she opens the box
```

- 精細手指動作（穿針、打字、彈琴）是弱項：改成中景 + 短時間，或用參考影片遷移。
- 產品在手上：`preserve hands/product contact`、`the hand tilts the product slightly toward the light while keeping the label square to camera`。
- 不要讓產品做變形動作（拆解、擠壓）除非那是賣點，並要求「部件對齊、數量守恆、最終復位」。

## 5. 臉部表演：寫意圖，不寫情緒清單

- 「nervous」不如「試圖掩飾緊張」：`Daniel tries to sound casual, but hesitates before replying`。
- 一句話配 2–3 個相關線索，不要五種情緒疊在一起。
- 微表情用具體動作：`a brief eyebrow lift`、`eyes drop, then meet the camera again`、`stops stirring and looks up slowly`、`a small nod`、`starts to answer, then stops`。
- 聽的人也要演：`holding or breaking eye contact, a quiet breath, tightening a grip, shifting in the chair`。
- 靜止也是表演：緊張戲少動作比大動作可信。
- 真人照片動畫（I2VA）：prompt 只寫表演與台詞，不重述外觀；代名詞、角色、場景必須和照片一致，寫錯性別會在中途換人。

## 6. 口型與說話品質

- 說話時鏡頭少動：`locked camera, no head turns while speaking`。
- 防橡皮嘴：`realistic lip articulation, no exaggerated mouth opening`。
- 說完要收：`exactly as his voice stops, his lips settle closed and he exhales through his nose`。
- 每個 shot 都要有事做，尤其最後一個；對白會擠在 shot 開頭，最後一個 shot 沒動作就變 dead air。
- 唱歌 / rap：`visible lip shapes, jaw motion, breath, facial accents, nods, and hand accents following phrasing`。

## 7. 舞蹈與運動：寫身體序列，不寫風格標籤

```text
❌ contemporary dance / breakdance
✅ First the weight drops onto the left knee, then the torso spirals open, as one arm
   extends and the fabric trails behind the movement.
✅ He drops into a windmill: first the shoulder makes contact, then the legs sweep
   through in a full rotation, as the jacket rides up and water sprays from the surface.
```

- 四肢要看得到：全身動作用全身景別。
- 分清「鏡頭環繞」和「舞者自轉」。
- 卡點：有音樂就綁鼓點，沒音樂就綁腳步、觸地、呼吸。
- 極限運動 / 跑酷：每個時間段一個動作（vault → leap → drop → roll），鏡頭「跟著動量」，切點對齊落地衝擊。

## 8. 慢動作與速度變化

- 慢動作獨立 shot，背景降熵（大雨→細雨、狂風→微風、拿掉人群）。
- 慢動作 shot 內的聲音也要慢：`the rain and metal contact stretch into a low, drawn-out scrape`。
- 一個 shot 內不寫「先慢後快」；真正的 speed ramp 用兩次生成 + 剪輯 optical flow。
- 高速用有方向感的詞：`streaking, motion blur, dynamic thrust`；低速用 `leisurely, languid, steady`。

## 9. 動畫風格的動作規律

| 風格 | 動作要求 | 禁止 |
|---|---|---|
| 3D 卡通 / Pixar 風 | 誇張彈性：squash/stretch、anticipation、overshoot、快速換 pose、清楚剪影；荷蘭角用在追逐/失衡/驚訝 | 寫實肌肉感 |
| 2D anime | 一個 shot 一個 held beat；描述繪製方式 `flat cel shading, two-tone shadows, clean dark linework, limited animation timing`；光用 2D 畫法 `warm side light, hard shadow edge` | `volumetric god rays, shallow depth of field`（會拉向 3D） |
| 黏土 / 定格 | 手指痕、霧面、微縮景深；關節動作有限；stop-motion stepping 不是流體動作 | 流暢寫實動作 |
| 紙藝 / 拼貼 | 層次紙邊、切痕、翻折；動作是放置、撕、滑、疊 | 3D 立體感 |
| 手繪 + 實拍融合 | 說清哪層是實拍、哪層是線條；線條要和實體表面互動（貼指尖、繞扶手、沿座椅縫） | 恐怖化、撲咬、憑空切鏡 |
| 像素 / voxel | 物理仍要正確，保留真實環境的陰影與透光 | 全畫面被重繪 |

## 10. 身份與臉在動作中不掉

- 臉越小越難保持；廣角建立空間，關鍵情緒拍轉中景/特寫，或「wide shots use back view / rear three-quarter; never a distant frontal face」（官方 xianxia 範例）。
- 有參考圖時，全局宣告一次不變量，分鏡內只寫新變化；每個 shot 重述外觀會讓文字與圖片互搶。
- 快速動作讓幾何解析變差；臉部要清楚的 beat 不要同時是最快的 beat。
- 多角色：每個角色一個穩定稱呼（名字或「the man in the grey henley」），全篇不換說法。
