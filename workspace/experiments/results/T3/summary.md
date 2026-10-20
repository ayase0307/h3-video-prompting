# T3 結果（光線路徑句 vs `cinematic lighting`；0.5MP / medium / 6s / t2va 16:9，seed 1001–1003，各臂 3 支）

單變量：A＝`cinematic lighting` 類泛稱；B＝路徑句（光從哪來、落在哪）。去盲對照見 `key.json`。

| seed | A 盲評 composite（0–7） | B composite | L* std A / B（閃爍代理） |
|---|---|---|---|
| 1001 | 7 | 7 | 2.40 / 1.97 |
| 1002 | 6（key_direction 方向稍飄） | 7 | 1.69 / 2.04 |
| 1003 | 7 | 7 | 0.61 / 0.60 |

- 切點：6 支皆 0 切。
- B 只在 seed 1002 勝（A 的光向被評為「稍飄」），其餘兩 seed 打平；appeal 全 3、exposure 全 1（評分員皆說「臉偏暗看不清」）。
- L* std：B 未比 A 高出 1.0 以上，沒有閃爍退化。
- 判定（依 plan.json `decision`）：1 勝 2 平 ≠ 「3/3 或 2/3＋平手」→ promote 不成立。原稿判為「未定論」，**審查更正**：`demote` 條款是「A ≥ B 在 ≥2/3 seed」，平手算 A ≥ B，seed 1001、1003 已滿足，n=3 時就該觸發降級；補跑的 1004–1006 與此一致，不是補跑才觸發。
- 限制：評分員自述臉部看不清，exposure 無鑑別力；接觸表 2fps 低解析；n=3。

## 補跑 seed 1004–1006（依 plan 的 inconclusive 規則；`scores_extra.csv`，composite＝artifact+key_direction+motivated+exposure 加總）

| seed | A | B | L* std A / B |
|---|---|---|---|
| 1004 | 7 | 7 | 1.72 / 1.93 |
| 1005 | 6（抬手輪廓糊） | 6（光向不穩） | 1.19 / 0.89 |
| 1006 | 7 | 7 | 2.20 / 2.70 |

- 六個 seed 合計：B 勝 1、平 5、A 勝 0；L* std 差皆 <1.0。
- 判定（plan `decision`）：未達 B 勝 3/3 或 2/3＋平，且 A ≥ B 在 5/6 seed（只有 1002 是 B 勝） → 依 demote 條款，**路徑句不得標為已驗證技巧，降級為風格建議**（不是「有害」，是「在本機 0.5MP 下沒測到好處」）。
- 限制：評分員多數回報「臉偏暗看不清」，exposure 全部 1 分（無鑑別力）；接觸表每幀約 272×154，key_direction 幾乎量不出差別，所以降級的意思是「這個評分員量不到好處」，不是「確定沒好處」；兩臂畫面都偏暗（L* 均值 16–25）；兩臂字數與場景物件相同，差異只在光線句；n=6。
