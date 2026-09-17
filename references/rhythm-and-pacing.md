# 節奏與卡點：讓 10 秒有拍子

來源：MiniMax 官方飛書手冊「大字幕 MV」與「手繪特效」完整 prompt；music-video-subtitle-generator 官方 style skill；brand-promo-video-generator beat 規劃；Hailuo 官方知識庫 Temporal Prompting；aireiter / reAPI / atlascloud 社群整理；Reddit r/StableDiffusion 回報（經 aireiter 引用）。

## 1. 時間軸是 prompt 的骨架

- 沒寫時間軸 = 一個動作被拉長到整段時長，第 7 秒模型沒事做。
- 官方 45 個範例裡最強的都在切時間：`[0s-3s] … [3s-6s] …` 或 `[Shot 2] At 00:03.000`。
- 本地/開源格式用 `[Shot N] At MM:SS.mmm`（嚴格遞增、落在時長內）；平台自然語言可用 `[0–3s]` 區塊。兩者都是「編輯大綱」，H3 對切點遵從度高，但不保證幀精確。
- 時間依資訊量分配，不平均分：例如 10 s → 0–3.3 建立 / 3.3–6.9 衝突 / 6.9–10 落點。
- 15 s 建議 3 段（0–5 / 5–10 / 10–15），每段一個動作一個運鏡；短片 5–6 s 只放一拍。

## 2. 每個 shot 的最短長度

- 社群最常見的結構失敗：「timestamps spaced too tightly」與「對白塞不進 shot」。
- 經驗值：非對白 shot ≥ 2 s；有台詞的 shot 長度 = 把台詞用預期語速唸出來的秒數 + 前後反應。12 個英文字約 5 秒。
- 一個 3 s shot 講一大段話，口型必壞（MiniMax 官方強調）。

## 3. 卡點要寫觸發物

「energetic editing」不可審查；「cut on the downbeat at 3.0 s」可以。

| 想要的效果 | 寫法 |
|---|---|
| 隨節拍硬切 | `每次 bass hit 觸發場景硬切或景別硬切` |
| 文字跟拍 | `每個 snare 時文字突然放大、抖動、掃描錯位` |
| 微顫 | `hi-hat roll 時字母邊緣高速細碎震動` |
| 重音壓屏 | `808 bass 砸下，"TWO FLY" 瞬間縱向壓縮後回彈` |
| 收尾 | `最後一拍所有場景碎片同步凍結，hard cut to black` |
| 無音樂的動作片 | `每次刀刃接觸的金屬聲當下切到下一個景別` |

MV skill 對應表：hi-hat roll → 微抖 / 跳幀；snare → 放大 / 硬切 / 肩膀下沉；808 bass hit → 低頻壓縮 / 拉伸 / 位移。切點落在 1/4 或 1/8 拍格。

## 4. 官方「律動」段落模板（大字幕 MV）

每個 shot 五行：場景 / 景別 / 人物 / 文字 / 律動，最後一行寫切法。

```text
Shot 2 — 中近景半身 / 牆面文字背景
- 場景：另一處牆面/海報牆近景（和 Shot 1 空間明顯不同）
- 景別：明顯拉到中近景半身
- 人物：Detective B 對鏡頭 rap，肩膀和頭部跟 hi-hat 點拍，身體輕微前傾
- 文字："CLUES" 巨大壓縮英文在人物身後，被頭髮/肩膀/服裝輪廓自然遮擋
- 律動：文字縱向拉伸如海報立起；每個 snare 時文字突然放大、抖動、掃描錯位
- 硬切
```

Final 段寫「禁止全身、禁止多人全景，只用近景/特寫」把景別鎖死，再寫「嘴型/下顎/呼吸/眉眼/手勢都精準卡住 vocal、snare、hi-hat roll、bass hit」。

## 5. 唱歌 / rap 的表演節奏

MiniMax 官方測試通過的寫法：

```text
女歌手微微前傾靠近復古銀色麥克風，眼神半垂，嘴角帶著一絲笑意，輕聲吟唱 neo soul 歌曲
"Baby, slow down, let the night hold us close. …"。雙手在 Rhodes 電鋼琴鍵上緩慢滑動，
肩膀隨慢拍輕輕搖擺。唱到 "honey on my soul" 時頭微微一偏，閉眼陶醉，尾音拖長。
```

要點：歌詞逐字給；把身體節奏綁到「慢拍」「某句歌詞時」；表演者要有「可見口型、下顎、呼吸、點頭、手部重音」跟隨 phrasing。

## 6. 速度：形容詞優於數字

- 模型不解讀「3 秒 pan」「5 mph」；解讀 `leisurely / steady / brisk / languid / explosive`。
- 一個主時間形容詞 + 一個運鏡動詞：`a leisurely crane up` 比 `crane up slowly` 穩。
- Contradiction Trap：同一 shot 不混 slow 與 rapid（「慢推鏡 + 快速流雲」會卡頓）。
- H3 開源格式的速度詞是 `at slow speed / at fast speed`，幅度是 `with small/large amplitude`。

## 7. 快節奏 ≠ 鏡頭亂動；慢節奏 ≠ 沒動作

- 快：更短的 shot、明確卡點、乾淨切換、一個 shot 一個視覺任務。
- 慢：緩慢推進、材質變化、眼神、聲音細節維持張力；慢 shot 背景動態元素要少。
- 品牌片節奏：2–3 個高能量峰 + 安靜煞車段；一個 beat 一個主動作，副層稍微延遲。

## 8. Hero Template：跨 clip 統一節奏

先生成最重要的 hero clip，抽出它有效的節奏詞（如 `languid tracking shot`），後續每個 clip 保留同樣的節奏詞只換主體與場景，避免拼接後「tonal whiplash」。

## 9. 多段拼接（>15 s）

MV skill 流程：鎖一條 master audio → 拆成 2–5 s 的 4–8 個 shot 對齊歌詞時間戳與鼓點 → 同場景用上一段尾幀當下一段首幀，硬切則同方向運動或遮擋接 → 剪輯時全部對回 beat grid，必要時 speed ramp。

## 10. 對白跨切點（J-cut / L-cut）

H3 支援，但要明寫哪一句跨了哪些 shot：

```text
一個畫外音響起說：Wake up Wake up。之後切鏡到一個中年婦女的近景，她是畫外音的主人，
她繼續說道：It's time to go to school!
```

開源格式在兩側加 `<scenetrans>` 並寫 `continues seamlessly across the cut`；被片尾截斷用 `<cutoff>`。
