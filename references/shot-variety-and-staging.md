# 不單調：跨 shot 變化、調度與送出前自檢

來源：
- 四支抖音參考：電影感來自關係、分鏡表、混合媒介、6 種運鏡。屬方法主張，展示工具不是 H3。
- Seedance 社群 skill：alchaincyf（MIT）、zhouwei713（MIT）、LearnPrompt（MIT）。只有 Seedance 經驗。
- 漫劇 pipeline：Kinema（AGPL）、Comfy-H3-Director（無授權）。只借概念。
- 中文社群教學、hailuoai.video 深度文。純理論。

**本頁規則大多沒有經過 H3 實測。** 唯一做過本機先導 A/B 的是 §6 光線路徑（結果：沒測到好處，已降為風格建議）。規則都設計成不破預算；其餘效果請依 §11 的方法自己 A/B 驗證。

## 1. 核心觀念

單調通常不是因為單一 shot 不夠熱鬧，而是相鄰 shot 長得太像。
解法放在 shot 和 shot 之間，不要在單一 shot 裡多堆運鏡、多堆動作。

預算不變：
- 每 shot 一個主動作、一個運鏡。
- 10 s 內 3–4 個 shot，每個 shot ≥2 s。
- 純文字 prompt 300–700 英文字（社群經驗值，官方無此數字）。

## 2. Spec 卡是規劃工具，不是 prompt

先用 `long-form-planning.md` §8 的 spec 卡把每個 shot 的欄位填滿，再壓成 prompt。

壓縮優先序：**動作 > 運鏡 > 光 > 媒介**。字數超標時從右邊開始砍。
- 「關係」和「景深」各縮成一個子句。
- 「媒介」只有混合媒介片才寫（C9b）。

## 3. 跨 shot 變化規則（主規則）

每個 shot 標出四軸：

| 軸 | 值 |
|---|---|
| 景別 | 遠 / 全 / 中遠 / 中 / 中近 / 特寫 / 大特寫（7 級） |
| 角度 | eye level / low / high / top down，加上方位（正面、側面、背後） |
| 運鏡類型 | static / push / pull / pan / tilt / truck / pedestal / zoom / track / POV / roll / shake / 環繞（= truck+pan） / 焦點轉移 |
| 主體／視線 | 這一鏡的主角是誰或什麼，看向哪裡 |

規則：
1. **相鄰 shot 在四軸中至少 2 項不同。**
2. **其中至少 1 項是實質變化**，三選一：
   - 景別跳 ≥2 級；
   - 角度或方位變 >30°；
   - 主體換人或換物。
   只是換距離、微調角度不算，那種情況用運鏡，不切（`camera-and-transitions.md` §5）。
3. 每次切鏡仍要帶新資訊：主體、空間、狀態、視角或時間。
4. 10 s 4 shot 裡至少 1 個是中遠景以上，用來交代誰在哪裡（讀數鏡）。
5. 不連續三個 shot 用同一運鏡類型；static 可以連兩個。

## 4. 每個 shot 都有可見的狀態變化

- 格式是「起 → 觸發 → 結果」，用 first / then / as 寫，不在 shot 中段插第二個 `At`：
  `First her phone lights up, then she reads it, as her thumb stops; finally she turns it face down.`
- 升級題材（恐怖、懸疑、壓迫）每個 shot 只加一個新變化，像階梯一樣往上，不要在一鏡裡全部爆出來。
- 切點可以用 match on action：前一個 shot 收在動作中段，下一個 shot 從同一個動作的後半開始。

## 5. 景深：每個 shot 一個層次

- 前景最具體、中景寫功能、背景只寫氣氛（金字塔細節）。三層都寫滿會變扁平。
- 前景只放一個物件：失焦的玻璃雨滴、枝葉、門框、路人。這個物件同時交代「從哪裡看」。
- 大氣介質（霧、塵、細雨）最多一種，同時兼任光線路徑的介質。
- 峰值或快速動作的 shot，鏡頭保持靜止，只讓主體動；快動作的模糊會吃掉深度線索。**這條只適用於劇情和情緒片**。打鬥、跑酷、車輛依各情境規則（例如 `example-fight-10s.md` 的 truck、camera §4 跑酷的 handheld tracking）。
- 主體不要小到看不見：要它做動作，至少用中遠景；臉部要穩，至少用中景。

## 6. 光：光線路徑（風格建議）

**本機先導實測（n=6, 0.5MP, t2va 6 s）**：路徑句 vs `cinematic lighting`，盲評 B 勝 1、平 5，觸發降級條款；評分員看不清臉（接觸表低解析），所以只能說「沒測到好處」，不是「有害」。原始紀錄在私有 repo，未公開。下面的寫法當風格選項用，不是必要規則。


- 寫法：光源 → 介質或路徑 → 受光面。
  `Red neon from the sign outside passes through the wet glass and lights only the left side of her face.`
- 光也可以是那一鏡的狀態變化：
  `Cold blue light spills through the opening door, runs across the floor, and climbs onto her face.`
- 想要指定光向時，路徑句比「cinematic lighting」具體；但本機實測兩者在畫面上沒量到差別，字數緊時可省。

## 7. 調度：關係、反應、揭露

- 人物和環境的關係用一個物件承載，例如對面的空位、沒動過的杯子、關著的門。全片只建立一次。
- 恐懼、驚訝、心痛可以拍旁人或主角的反應，不一定要拍事件本身。
- 正臉或關鍵物的揭露延後到峰值 shot。在那之前可以用背影、手部、側影。

## 8. 能量曲線

- 10 s 規劃一個峰值；15 s 最多兩個。rhythm §7 的品牌片是 2–3 個峰。
- 峰值前一個 shot 刻意降低動作強度，做「停 → 爆」。（峰值鏡頭靜止的建議只適用於劇情和情緒片，見 §5。）
- 相鄰 shot 的動作強度要有落差，大動接大靜。
- Shot 1 就要有狀態變化，不要放純空鏡。
- 收尾停在靜止的殘局，不收在動作中間。

## 9. 角度語意（慣例，不是公式）

| 角度 | 常見用途 |
|---|---|
| low angle | 支配、壓迫、英雄感 |
| high angle | 審視、脆弱、被掌控 |
| eye level | 對峙、拉鋸 |
| top down | 佈局 |

- 權力翻轉時，角度跟著翻轉：被壓的一方反擊時，從 high 換成 low。
- **俯拍是角度，不是運鏡。** 寫在景別句（`a high-angle wide shot`），運鏡另外選。
- 同一個 shot 只寫一個角度，不要「俯拍」和「平視」同時出現。

## 10. 送出前自檢（agent 逐條執行）

用 `P` 代表 prompt 文字檔，`D` 代表實際有效時長（例如 10 s 填 10.125）。

1. **shot 數**：`grep -o '\[Shot [0-9]*\]' P | wc -l`
   - 10 s 要得到 3–4；15 s 要得到 4–6。
2. **Shot 1 沒有時間戳**：`grep -c '\[Shot 1\] At' P`
   - 要得到 0。
3. **切點**：`grep -o 'At [0-9][0-9]:[0-9][0-9]\.[0-9]\{3\}' P`
   - 列出所有切點，數量必須等於 shot 數 − 1，超過就代表 shot 內插了 `At`，要改成 first/then。
   - 時間必須嚴格遞增。
   - 相鄰差 ≥ 2.000；第一個切點 ≥ 2.000；`D` 減最後一個切點 ≥ 2.000。
4. **沒有環繞類詞**：`grep -ciE 'orbit|\barc(s|ing)?\b|circles around|360-degree' P`
   - 要得到 0。需要環繞就寫成 `trucks left … while panning right`。
5. **每個 shot 剛好一個運鏡句**：把 prompt 依 `[Shot` 切開，每段用下面的式子計數，每段要剛好 1（truck 和 pan 寫在同一句時算 1）：
   `grep -oiE 'pushes in|pulls out|pans (left|right)|tilts (up|down)|trucks (left|right)|pedestals (up|down)|zooms (in|out)|tracks the|holds a static shot|point of view|rolls (clockwise|counterclockwise)|shakes (slightly|strongly)'`
6. **四軸表**：為每個 shot 填 {景別, 角度, 運鏡類型, 主體/視線}。
   - 相鄰 shot 不同項 ≥2。
   - 其中 ≥1 項符合 §3 的實質變化。
   - 任一對不合格就改角度或換主體，不要加運鏡。
7. **狀態變化**：每段都含 `then` 或 `as`（I2VA 的 Shot 1 也一樣）。
   - 沒有就補「起 → 觸發 → 結果」。
8. **光線路徑（選用，§6 已降為風格建議）**：想指定光向時，每段一個光源名詞（sun / lamp / neon / window light / street light / sky light …）和一個受光面。
   - 0 個可以不補；2 句以上就刪到 1 句。
   - **字數超標時此條降級**：只要求 Shot 1 和峰值 shot 有；其餘 shot 依 §2 壓縮優先序（動作 > 運鏡 > 光 > 媒介）可以省，不要為了補光句而超過字數上限。
8b. **景深層次**：每段都要命中 `foreground|in front of|out-of-focus`。
   - 0 次就補一個前景物子句。
   - **同 8，字數超標時降級**：只保留 Shot 1 和峰值 shot 的前景子句。15 s 6 shot、Ref2VA（350–500 字）幾乎一定要降級；先砍光與前景，絕不砍動作和運鏡。
9. **角度不矛盾**：同一段不能同時出現 `eye-level` 和 `high-angle`、`low-angle`、`top-down` 其中任一個。
10. **字數**：
    - T2VA：`wc -w` 只算 `integrated_multimodal_description`，要落在 300–700。
    - Ref2VA：只算 `detailed_description`，要落在 350–500（對白密集時以台詞時間優先）。
11. **結尾欄位**：`overall_soundscape` 和 `non_diegetic_music` 都要存在。
    - 若音樂是 `N/A`：`grep -ciE 'music|score|soundtrack|melody|bgm|配樂' P` 要只剩欄位名那 1 次。
12. **有參考素材時**：外觀形容詞（髮型、服裝）只出現在該角色第一次登場的 shot。
    - 用 grep 檢查這些詞的出現次數，要 ≤1，`subject_definitions` 不算。
13. **自我 A/B**：每次重抽只改一項，並記錄改了哪項、結果如何。

任何一條不過，先修 prompt 再送出；不要用增加時長或增加素材來解決。

## 11. 可信度與實測建議

| 規則 | 依據 | 建議驗證 |
|---|---|---|
| §3 跨 shot 四軸 | 剪輯慣例；Seedance 白模自測 | 同一 brief 生兩版（四軸全同 vs 合規），盲評單調感 |
| §5 前景一物 | 第三方文章 | 有前景物 vs 無前景物，各抽 3 次 |
| §6 光線路徑 | 抖音 1（方法主張） | 已測（T3，n=6, 0.5MP）：沒測到好處 → 降為風格建議；原始紀錄在私有 repo，未公開。0.98MP 或人工看臉的複驗未做 |
| 焦點轉移 | Seedance、Kling | H3 能不能做出來，是否被誤當成切鏡 |
| §8 峰值 shot 鏡頭靜止 | 純理論 | 峰值 shot 用 static vs 運鏡 |
| 動作鏈十要素（`action-choreography.md` §11） | LoveUolanda 方法論（舞蹈，有成片未對照）；籃球範例只經前向測試 | 同一個非舞蹈動作（如範例籃球過人）寫兩版：純動作名稱＋形容詞 vs 挑 2–3 項要素寫成受力/重心/慣性，各抽 3 次，比動作是否完成、是否糊成一團 **首次試跑（2026-10-20，單組、同 seed、各生成一次、i2va 9:16 10 秒）**：同一張持刀人物圖，舊寫法（形容詞＋「動態環繞」＋要配樂）生成一鏡到底、無切鏡，後 3.5 秒停在舉刀防禦姿勢仍有細微晃動、沒有收勢；新寫法（三 shot，受力/慣性/袖子延遲）切點落在 3.5 與 7.0 秒、斜斬弧光與水花都出現、結尾落定靜止。兩版同時也差字數、外貌描述與配樂，非單變量；一次樣本不構成證據。**單變量重做（T1，2026-10-20，n=3, 0.5MP, i2va 6 s）**：盲評兩臂全滿分（天花板），依判準為未定論，規則維持方法主張；B 尾 1 s 殘留動作 3/3 較低，只當描述性訊號。原始紀錄在私有 repo，未公開。 |
