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
- 判定（依 plan.json `decision`）：1 勝 2 平 ≠ 「3/3 或 2/3＋平手」→ **未定論**，plan 要求補 seed 1004–1006。路徑句規則**不升級**，維持方法主張。
- 限制：評分員自述臉部看不清，exposure 無鑑別力；接觸表 2fps 低解析；n=3。
