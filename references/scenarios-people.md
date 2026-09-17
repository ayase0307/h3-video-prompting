# 情境庫 A：人物、表演、動作

每個情境：優先順序 → 必寫 → 範本片段 → 坑。格式照 `prompt-formats.md` 選；動作細節見 `motion-quality.md`。

## A1. 兩人對白 / 短劇

優先：逐字台詞 → speaker 穩定 → 反應時序 → 簡單鏡頭。
必寫：每人一個穩定稱呼與 (S1)/(S2)；台詞緊貼該角色的動作；聽者的反應動作；停頓；正反打或固定雙人鏡；環境聲基線；配樂 N/A 或只在結尾進。
```text
[Shot 1] Live-action, cinematic, a medium two-shot frames Maya and Daniel across a café table by the window. Maya, holding a folded letter in both hands and avoiding eye contact, in a controlled voice hiding anxiety (S1) asks: <d>[English] Did you read it?</d> Daniel watches her without speaking.
[Shot 2] At 00:04.000, the shot cuts to a close-up of Daniel. He looks down at the letter, takes a slow breath, and in a low, calm, certain voice (S2) replies: <d>[English] I didn't have to.</d> Maya's hands stop moving as he speaks.
[Shot 3] At 00:07.000, the shot cuts to a close-up of Maya. She holds his gaze, says nothing, and slowly places the letter on the table.
overall_soundscape: Soft café room tone with distant indistinct voices and occasional dish sounds; paper slides against wood at the end.
non_diegetic_music: No music during the conversation; one restrained piano note enters after the letter touches the table and fades.
```
坑：台詞超過 shot 長度；兩句放一個 `<d>`；長台詞配快速切鏡；沒給聽者動作變成兩段獨白；豎版短劇用 MCU/CU 為主。

## A2. UGC 口播 / talking head

優先：不像廣告 → 一句有細節的台詞 → 手持微晃 → 無音樂。
必寫：`handheld medium close-up with a small amount of natural sway`；單一窗光；`room tone only, no music`；台詞是人會對朋友說的話（`Nobody warned me about the purge week.`）；產品晚點入鏡（第二拍才舉起）。
```text
A woman in her late twenties sits cross-legged on a bed in a sunlit bedroom, holding a small pink skincare tube toward the camera. She looks straight into the lens and says, "Nobody warned me about the purge week." Handheld medium close-up with a small amount of natural sway, soft window light from the left, clean natural colour. Room tone only, no music. Vertical framing.
```
坑：完美構圖、多向打光、品牌語（clinically proven）、配樂、開頭就舉產品；五秒塞四句話。
批次：模板固定，只換台詞，5 秒 480p 先測，存活者再 768p。

## A3. 唱歌 / rap / MV 表演

優先：歌詞逐字 → 口型與呼吸跟 phrasing → 鼓點綁動作與文字 → 近景為主。
必寫：歌詞在引號或 `<d>` 內；`肩膀隨慢拍輕輕搖擺`、`唱到 "…" 時頭微微一偏`；卡點觸發物（bass hit 硬切、snare 文字放大、hi-hat 微抖）；`禁止全身、禁止多人全景`（官方 MV 例）。
範本見 `rhythm-and-pacing.md` §4–5。
坑：歌詞不給就變亂語；全身景別讓口型不可讀；文字沒逐字打出會變噪音。

## A4. 舞蹈 / 動作遷移

優先：全身可讀 → 身體序列 → 鏡頭環繞 vs 舞者自轉分清 → 節拍。
必寫（有參考）：`Use Video 1 strictly for the street-dance movement and timing. Use Images 1 and 2 for identity, appearance, and wardrobe.`；（無參考）：身體序列 `weight drops onto the left knee, then the torso spirals open`。
坑：所有素材都拿來參考所有屬性 → 臉、衣、動作混血；跨體型遷移漂；參考影片音軌滲入。

## A5. 打鬥 / 對抗

優先：接觸幾何清楚 → 一 shot 一拍 → 鏡頭比身體簡單 → 切點對衝擊。
必寫：雙方畫面位置與朝向；攻擊肢體/武器與方向；接觸/格擋；反應/恢復；一個運鏡；每次 cut 落在接觸聲。
完整範例：`example-fight-10s.md`。
坑：多個同時攻擊；3 個以上重要角色；慢動作段還有大雨；「dynamic」沒有物理描述。
魔法 / 元素對戰：先寫身體動作，再寫元素軌跡（`sweeping trails of translucent blue water from their arms`），最後寫碰撞後果（`shockwave of grey smoke and airborne stone debris pushes the characters to the frame edges`）。

## A6. 跑酷 / 極限運動 / 追逐

優先：每段一個動作 → 鏡頭跟動量 → 切點對落地 → 環境回應。
```text
0-4s — Vault over a metal barricade in a narrow alley, then a leap over a concrete parapet against clear sky. Low tracking angle.
4-8s — He jumps toward the camera down tiled stairs. Cuts to a high angle as he drops from a ledge to a lower rooftop.
12-15s — Lands in a balanced crouch on the parapet edge, safety-rolls onto the roof; the camera pulls back to a high wide revealing the skyline.
CAMERA: handheld tracking following his momentum; cuts match the physical impact of each landing.
AUDIO: wind whoosh, heavy landing thuds, sneaker squeaks, clothing rustle.
AVOID: slow motion, static tripod shots.
```
坑：一段塞三個技巧；鏡頭比人還忙。

## A7. 喜劇 / 反應戲 / slapstick

優先：setup → pause → reaction → payoff 的時序。
必寫：反應前的停頓；鏡頭固定或簡單，讓時序讀得出；音效點到為止；動畫風格用荷蘭角、squash/stretch；結尾一個「殘局」wide static 定格（官方 janitor 例：`mall corridor completely trashed`）。
坑：SFX 太多蓋過笑點；鏡頭亂動讓 timing 消失。

## A8. 情感特寫 / 浪漫

優先：微動作與視線。
必寫：小幅度動作（呼吸、眨眼、手指）、光的方向與材質（`warm low light, condensation on the crystal tumbler`）、聲音細節（`ice tapping crystal, controlled breathing`）；一個運鏡或 static；臉部朝向與遮蔽（官方 red-dress 例：女方臉大多不入鏡，只給頸肩手）。
坑：場景切換過多；情緒詞堆疊。

## A9. 懸疑 / 恐怖 / 偽紀實

優先：資訊保留與聲音舞台。
必寫：負空間、慢速揭露、具體的畫外聲（`slow footsteps echo from inside the tunnel`）、手持一手拍的缺陷感（`delayed autofocus, exposure fluctuation, coarse noise in shadows`）；明說「不要」（`no giant eyes, split mouths, fangs, lunges, sudden black frames, jump scares`）如果要溫和版。
坑：「scary atmosphere」沒有可見可聽線索；恐怖元素憑空出現。

## A10. 紀實 / 觀察式 / vlog

優先：可信行為與環境連續。
必寫：拍攝者身份（路人手機、一手拍）、設備感（`realistic smartphone compression, limited stabilization, occasional autofocus adjustment`）、不完美構圖、環境聲真實、`completely serious, unscripted documentary feeling`（官方 giant koi 例）。
坑：加了電影感光影與配樂就破功。

## A11. POV / 第一人稱 / FPS

優先：鏡頭與身體的關係。
必寫：`first-person, eye level, handheld`；可見的手/武器只在需要時；`subtle player-driven sway while moving, small checks left and right, light recoil when firing`；不切第三人稱除非刻意 cut；HUD 文字要逐字。
坑：頭部動作不合理；HUD 文字寫「HUD elements」變亂碼。

## A12. 旁白型解說 / 數位人

優先：旁白節奏 → 畫面支撐當前論點 → 口型或閉嘴明確。
必寫：旁白 `says in an off-screen voiceover … while lips remain closed`；畫面內人物若不說話用 §不說話寫法；數位人用 `<Audio N>` 當音色參考 + 穩定 (S1)，不自動複製原句；動作克制。
坑：旁白被畫面內角色「唸出來」；把旁白文字又打成字幕。

## A13. 真人照片動起來（I2VA）

優先：照片與 prompt 一致 → 只寫表演與台詞。
```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, a medium close-up holds on the woman from the photo at her desk. She looks up from the laptop, breaks into a warm smile, and with a confident, easy voice (S1) says: <d>[English] We just shipped the feature you have all been asking for.</d> She closes the laptop and leans back, holding the frame to the end.
overall_soundscape: Quiet office ambience with a laptop lid closing and a chair creaking softly.
non_diegetic_music: N/A
```
坑：代名詞或職業與照片不符會中途換人；描述第二個人就會多出一個人。
