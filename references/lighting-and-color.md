# 光影配色與跨鏡頭色彩一致

來源：官方 MiniMax-H3 repo（`skills/h3-prompt-writing/references/{base-en,ref-en}.txt`、README）、MiniMax 平台 API 文件、Runware editing-video 指南（頁面標作者 MiniMax）、Hailuo Field Notes、Higgsfield H3 指南、IC-Light / Qwen-Image-Edit / FLUX Kontext 社群做法、Zone System、`lighting-color-palette-card`（Seedance 教學影片蒸餾，方法為創作者自創）。2026-10-16 由 Haiku 調研、Opus 審查並補查。

等級：**[官方]**、**[官方，經鏡像]**（出處為 MiniMax 作者的第三方頁面）、**[實測]**、**[社群單源]**、**[自創]**（來源方法，無外部依據）、**[推測]**。[自創] 與 [推測] 不得當保證。A/B 清單見 `workspace/experiments/lighting-ab-tests.md`。

先記住：
- 官方 repo 的 skills 全部查不到 HEX、Kelvin、palette 表 [官方]。H3 文字端是 Qwen3-VL，「HEX 能鎖色」在 H3 上沒有任何證據。
- 官方只要求：每個 shot 交代 environment and lighting（ref-en §1）、I2VA 的顏色要保持一致、FL2VA 要描述光線變化 [官方]。

## A. 光色寫法

| 規則 | 為什麼 / 壞掉長怎樣 |
|---|---|
| 每個 shot 一句光線路徑：**光源 → 介質 → 受光面**；顏色用「色名＋實際物體」，不用 HEX 表 | 官方要求每鏡交代光線；只寫 `cinematic lighting` 沒有路徑，曝光由模型亂決定 [官方＋方法] |
| 風格與色板在片頭一到兩句英文定下：三欄格式在 `[Shot 1]` 開頭；Ref2VA 六段式的風格句寫在 `[Shot 1]` **之前** | [官方 ref-en §5.2] |
| 避開 `bright`、`well-lit`、`high quality`、`flat lighting`；`Rembrandt`、`chiaroscuro` 也要謹慎 | Hailuo Field Notes 列為避免或謹慎；該頁自稱內部經驗，非實驗 [社群單源] |
| 可用詞：45° / 90° side light、rim / back light、soft box、hard light、diffuse、golden rim light | 同上 [社群單源] |
| 點綴色必須寫範圍：`only lights the nearby rubble` | 不寫範圍會擴散成全屏光污染（創作者經驗） [自創] |

範例（光線路徑＋色名綁物體）：

```text
Cold steel-blue dusk light from the broken skyline rakes across the left side of his
armor; the alley walls fall into deep navy-black shadow that keeps brick texture; only
the blade edge flashes ice-white.
```

**五層亮度的 H3 版 [自創]**：最暗、陰影、中間調、遠景霧、最高光，各綁一個物體；最高光只給一兩個小物件。來源卡片的百分比（0–8 / 10–25 / 30–50 / 55–75 / 85–98%，最高光 <3% 面積）**不是業界標準**：Zone System 有 11 個分區，原文沒有百分比或 IRE 對應；唯有「最深暗部要留紋理、最高光無紋理」的概念與 Zone 吻合。實測卡片 5 個 HEX 換成 L* 約 7 / 22 / 43 / 63 / 90，剛好落在宣稱區間，所以「亮度 %」可讀成 L*，但這只是內部自洽。

```text
near-black navy only in the coat folds and gaps between rubble; slate blue-grey shadow
on the buildings; steel-blue midtones on the armor; smoky blue-grey haze in the far
distance; ice-white highlights only on the blade edge and eye catchlights.
```

- 套冷色板時，`skin-realism-block.md` 散文版的光色詞要同步換掉（golden rim → silver-blue rim；暖粉、玉質暖調 → 冷光下的呈色），否則兩段光色互相打架。
- 字數：**「純文字 300–700 英文字」沒有官方出處**，只是社群經驗值。有出處的只有：平台 API 上限 7000 **字元**（hosted）、Ref2VA 生成任務 `detailed_description` 350–500 英文字 [官方 ref-en]。Seedance 教學的「5000 字手戳提示詞」與「風格 25 / 角色 25 / 鏡頭 20 / 動作 30」比例不移植，查無可靠來源 [自創]；光色段寫一句光線路徑加一句全域配色就夠。

## B. 跨鏡頭色彩一致

| 規則 | 為什麼 |
|---|---|
| 把不變量（色名＋主光方向）寫成**一句全域光色句**，每段生成**逐字重用** | 每段換說法，冷暖就會漂。Higgsfield 也建議顏色在每個 shot 寫得一模一樣 [社群單源] |
| 同一段內不要每個 shot 重述外觀；後續 shot 不重新定義 label | 重述外觀會讓臉變，也違反 ref-en §5.3 [官方] |
| 續接：首幀用上一段尾幀，並寫 `Lighting direction and colour temperature continue unchanged from <Picture 1>.` | [推測]，未實測 |
| 場景資產先出同一光況的場景圖再生成 | 官方 3D skill 的 scene card 要列 key light states（day / night） [官方] |

範例：`The target video is cinematic live-action with a low-saturation cold steel-blue palette; key light from camera-left, same in every shot.`

查無：固定 seed、步數與色偏的關係；曝光自動調整是不是成因；H3 官方的色彩一致專用建議。

## C. 角色重打光與防貼紙

白底影棚光的三視圖直接放進暗場景，人會像貼紙：光向、色溫、顆粒、動態模糊不一致，又缺接觸陰影 [社群]。

**圖像端（生圖階段先把角色打成場景光）**，皆 [社群單源]、未實測：

```text
Relight the character with a warm tungsten key from above-left and cool blue fill;
preserve face, costume, skin tone, pose and framing exactly.
```

- IC-Light 吃前景圖加文字或背景圖；預設去背器 RMBG 1.4 **不可商用**，商用要換 BiRefNet。
- Qwen-Image-Edit 搭 Relight LoRA、FLUX Kontext：先講光型，再補色溫、方向、強度；必須寫保身份子句；一次只改一件事。大幅打光時身份與膚色可能漂，無量化比較。
- Nano Banana、GPT Image：查無官方重打光範例。

**影片端 H3 編輯**（出處：Runware editing-video 指南，頁面標 MiniMax 作者、2026-07-30 [官方，經鏡像]；**官方 GitHub repo 查無此範例**）：

```text
In Video 1, change the lighting from bright day to night: a deep blue sky, a warm lamppost
glow across the bench, and soft moonlight on the grass. Keep the bench, the tree, and the
camera drift exactly the same. Sound: soft night crickets.
```

六段式寫法 [推導]：retention 標 `<Video 1> partially_preserved - geometry and camera kept, lighting changed to night`。

**防貼紙**：寫接觸陰影與受光方向一致，例如 `his shadow falls on the wet floor toward camera-right, matching the lamp`；背景光向與角色主光同側 [社群]。綠衣角色避免用綠幕，改藍幕。

**Ref2VA 分工 [推測]**：`Video 1 keeps the character's identity and costume; Image 2 sets light direction and colour temperature only.` 官方沒有明文「三視圖管身份、場景圖管光」。

## D. 色卡參考圖 [自創，H3 上未驗證]

- 官方：只用來定義角色、場景、服裝、風格的素材**不建獨立 `<Picture N>`**；風格參考只保留大致相似，不逐像素複製（`weak_reference`）[官方 ref-en]。
- 色卡**照樣佔一個上傳名額**：參考上限 ≤9 圖、≤3 影片、≤3 音檔、總 ≤12 [官方 README、平台 API]。第三方寫的「最多 5 張」是該平台自己的限制。
- 寫法 [推測，依 ref-en 推導]：

```text
<Subject 4> is the overall colour palette defined by <Picture 4>, a five-swatch card; it
controls colour only and is never shown as an object.
```

retention 標 `weak_reference`，summary 用 `reference generation`。
- 色卡被畫進畫面（出現色條、色塊、招牌）的風險在 H3 上查無回報；上面那句「never shown as an object」是防呆，效果未驗證。
- 槽位不夠時，先把色溫烘進角色圖，把色卡拿掉。

## E. 後期統一與色彩 QA

生成端壓不住時，用後期統一。先統一亮度，再匹配色彩（DaVinci 的 Shot Match 也只匹配色彩，不匹配亮度）。

```bash
ffmpeg -i in.mp4 -vf "colorbalance=rm=-0.15:bm=0.15:rh=-0.08:bh=0.08" -c:a copy out.mp4
ffmpeg -i in.mp4 -vf "lut3d=file=grade.cube" -c:a copy out.mp4
```

量測用 `scripts/color_qa.py`（只用標準庫，需要 ffmpeg）：

```bash
python -I scripts/color_qa.py shotA.mp4 shotB.mp4 --ref 0B1118,1E2A38,3B5068,6B8299,E6F2FF
```

輸出每個輸入的平均 Lab 與 5 色主色，兩兩的平均色 ΔE76 與主色 palette ΔE76，`--ref` 會再給「色卡對主色」的距離。影片以 2 fps 取樣。

- 實測（hero.jpg）：colorbalance 暖偏後平均色 ΔE76 為 9.87，反向校回 0.70；palette 距離有約 2 的量化噪音 [實測]。
- ΔE 約 1 以下通常不可察覺，ΔE76 約 2.3 常被引為可察覺差（colour 文件；Mahy 1994 原文查無）[社群]。**ΔE76 與 ΔE2000 數值不可互換**；腳本只做 ΔE76。
- 門檻 **平均色 ΔE76 ≤ 3 只用在續接接點或同機位重生成** [推測]；不同鏡頭內容本來就不同，平均色差 20 以上是正常的，跨鏡頭只看「對色卡的 palette 距離」的相對趨勢。
- 這個量測很粗：灰色鉛筆分鏡對冷鋼卡的距離反而比真實 hero 圖小。只拿來比較同一流程的前後，不拿來判斷好壞。
- 未驗證：H3 輸出（bt709 標記）經 ffmpeg 轉 sRGB 的色彩矩陣是否準確。

## 不採用

- 卡片的**聲畫協同**（冷鋼夜黑 → 壓抑憤怒配音）：沒有依據，且和官方規則衝突（配樂只寫樂器、速度、力度，不寫情緒詞；speaker 要寫 pitch、timbre、rate）。
- HEX 色表進主規則：沒有 H3 證據，只放 A/B 測試。

## 出處待核

- `references-and-editing.md` §5 與 `scenarios-world-and-styles.md` C14 的綠幕引文，在 Runware 頁面與官方 repo 都查不到，疑出自需登入的飛書手冊，標為「出處待核」。
