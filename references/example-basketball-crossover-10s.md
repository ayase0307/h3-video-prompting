# 範例：非舞蹈動作（街頭籃球過人上籃）10 秒 T2VA

用途：示範動作鏈（`action-choreography.md` §11）怎麼轉到一般人體動作，而且守住字數與「每 shot 一個主動作」。**這支 prompt 是前向測試產物，沒有送進 H3 生成過，效果未驗證。** 格式：社群區塊式（`prompt-formats.md` D），hosted 自然語言端點；本地 ComfyUI 要改成官方格式。

## Prompt（約 320 英文字）

```text
Duration: 10 seconds | Aspect ratio: 16:9 | Style: Live-action, cinematic street basketball, natural late-afternoon light

SCENE
An outdoor half-court on cracked grey asphalt with a chain-link fence behind it. A young male player in a black sleeveless jersey and white shorts, short dark hair, faces one defender in a grey hoodie. Low sun from the left stretches long shadows across the court. The orange ball is the only bright object. Both players breathe visibly and keep their weight shifting between their feet throughout.

SHOT BREAKDOWN
0-3.5s — Medium wide, eye level, from the side. The attacker dribbles toward the defender, knees bent, ball bouncing low. His weight drops onto his left foot as the defender steps in to cut him off. Then he crosses the ball low from right hand to left hand in front of his knees, the ball slapping his palms, his shoulders swinging with it, and he plants his right foot to change direction. The camera trucks left with small amplitude at slow speed to keep both bodies in frame.

3.5-7s — Close-up, low angle, camera near the ground beside the court line. As the attacker drives past the defender, who stumbles back one step, he pushes off his planted foot, rises, and extends his right arm to lay the ball softly off the backboard. As he leaves the ground, the hoodie flares behind him and dust lifts from the asphalt at takeoff. The camera pushes in with small amplitude at fast speed toward his rising hand.

7-10s — Wide, high angle from behind the fence. The ball drops through the net with a clean snap. Then the attacker lands on both feet, absorbs the impact with bent knees, straightens, and turns to look back at the defender with a short breath. The camera pulls out with small amplitude at slow speed to reveal the full court and the fence, and holds the final composition.

AUDIO: dribble thumps on asphalt, sneaker squeak on the plant, palm slap on the crossover, net snap, one breath. No music.

AVOID: slow motion, static tripod shots, extra players, warped hands, text or watermarks.
```

## 用了十要素的哪幾項

| 要素 | 在 prompt 裡的位置 |
|---|---|
| 1 起始受力 | 重心壓左腳、膝蓋彎曲 |
| 2 進入路徑與支撐點 | 低手交叉、右腳站定換向 |
| 3 重心與軸線 | 肩膀隨球擺動 |
| 5 峰值 | 掌拍球聲＝交叉換手的峰值 |
| 6 慣性 | 落地屈膝吸收 |
| 8 物件／服裝物理 | 球拍手掌、連帽衫外擴、起跳揚塵 |
| 9 攝影機幾何 | 貼地靠球場線、欄杆後高角度 |
| 10 觸發條件 | 沒有音樂，改用腳步聲與掌拍聲 |

沒用的：微動作層（眼神、手指）因為字數壓力略過，符合 §11「只挑 2–3 項最容易出錯的」的預算。

## 檢查結果與已知弱點

- 3 個 shot、每個 3–3.5 秒、各一個運鏡（truck left / push in / pull out）。
- 「一個主動作」：shot 2 的 蹬地 → 騰空 → 出手 是一條上籃弧線（見 `action-choreography.md` §3）。測試員自己數成 7 個子動作，這是邊界值；若實際生成糊成一團，把 shot 2 拆成蹬地起跳與出手兩個 shot。
- 光源（low sun）與前景物只寫在 SCENE 段，沒有逐 shot 重複；若要嚴格過 `shot-variety-and-staging.md` §10.8／§10.8b，每個 shot 再補一句（約增加 40–60 字，仍在 700 字內）。
- `AVOID` 的 `text or watermarks` 與「不要寫不要字幕」有張力；格式 D 的官方範例本身就有這個欄位，故保留。
