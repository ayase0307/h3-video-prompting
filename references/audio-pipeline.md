# 聲音一次到位與配音後製

來源：官方 MiniMax-H3 repo `skills/h3-prompt-writing/references/{base-en,ref-en}.txt` 與 README；MiniMax 開放平台 T2A 文件；ComfyUI partner 文件；Openverse API 與 Creative Commons 授權原文；LatentSync / MuseTalk / Wav2Lip repo；virse、Atlas Cloud（社群，單源）。2026-10-16 由 Haiku 調研、Opus 審查並補查。

等級標註：**[官方]** 官方文件原文、**[實測]** 本次實際呼叫或執行、**[社群單源]** 單一第三方、**[推測]** 未驗證。[推測] 不得當成保證寫進 prompt；A/B 步驟在文末。

先記住兩個硬事實：
- H3 的聲音與畫面在同一次 forward 生成，輸出是 **單一 32 kHz 立體聲混音軌，沒有分軌，也沒有關閉音訊的參數** [官方]。
- **L2VA 不是音訊驅動口型**：它是 FL2VA checkpoint 的「只給尾幀」模式，輸入只有文字與圖，吃不到 `<Audio>` / `<Video>` [官方 base-en §3.3]。

## A. 一次生成聲畫（不靠後期）

| 規則 | 為什麼 / 壞掉長怎樣 |
|---|---|
| 要跨片段鎖角色音色，走 **Ref2VA**，不要走 FL2VA / L2VA 尾幀串接 | FL2VA / L2VA 只吃圖，每段重新抽聲音，S1 的嗓音逐段漂 [官方，推論] |
| 音色母帶從首段剪：2–15 s、單人、無配樂、少回聲的台詞，存成固定素材，之後每段都當 `<Audio 1>` | 混到 BGM 或第二人聲，音色會串到別的角色 [社群單源 dev.to] |
| `<Audio N>` 可以是獨立音檔，也可以是參考影片的同步音軌 | [官方 ref-en §2.4–2.5]；用途含音色、對白、BGM、續接 |
| 續接寫任務型 `[video continuation + audio reference]`；要保留原音寫 `audio reuse` | [官方 ref-en §3] |
| 只參考音色時，不帶入原對白；要原音照搬（`audio reuse`）時，`<d>` 逐字照抄原話 | [官方 ref-en §5.4] |
| 系列作品全程同一份母帶，不中途換 | 換聲音比換任何變數都更破壞連續性 |

範例（續接且鎖音色）：

```text
[video continuation + audio reference]
<Video 1> is the source video to continue. <Audio 1> is the synchronized audio track
of <Video 1>; it is the voice-timbre reference for <Subject 1> (S1). Reference the
timbre only; do not reuse its words.
```

**未驗證**：用首段音軌鎖音色的實際成功率。官方只保證「音色與語氣參考」，不保證跨片段一致；virse 回報參考音會被重新合成，並出現 voice crossover（聲音串到別人身上）[社群單源]。結論前先跑文末 A/B 1、2。

H3 自己也支援「保留原 BGM、換一段音色重說新台詞並對口型」：任務型寫 `[video editing + audio reference + audio reuse]`（官方 README 範例）。需要換台詞時先試這個，實際對嘴品質未驗證。

## B. 情緒與表演：H3 內能做的 vs 必須外部配音

**H3 內**：沒有任何情緒、語速、停頓、音高的欄位或標籤 [官方]。情緒只能寫成文字，放在 `<d>` **外面**；`<d>` 裡只有語言標籤與逐字台詞。社群單次測試顯示文字描述聲線（如 `calm, low, magnetic male voice`）有效 [社群單源 Atlas Cloud，無 A/B]；「四維描述有效」查無對照實驗 [推測]。

四維寫法（沿用 `four-dimensional-voice-acting` 的拆法）：

| 維度 | H3 內怎麼寫 | 可信度 |
|---|---|---|
| 音量與聲線 | `voice low and tight through clenched teeth` | 單源有效 |
| 語速 | `speaking slowly` / `rapid, breathless` | 官方要求 speaker 首次出現寫 speaking rate |
| 停頓 | 寫成動作事件：`pauses one second before the last word` | 見 audio-and-dialogue §4 |
| 句尾語調 | 只寫 `the line ends falling and flat`，**不保證照做** | 推測 |

```text
(S1), a man in his forties, voice low and tight through clenched teeth, speaking
slowly, pauses one second before the last word, says: <d>[English] Get out.</d>
```

- 每句 1–2 個聲帶狀態詞；疊太多「沙啞、發顫、撕裂」會變雜訊（四維配音法的 limitations）。
- 標點要和語調一致：要句尾下沉就用句號，不要連用感嘆號；英文與日文的重音／音拍規則不同，不可把中文的「牙縫擠字」直接翻成別語言。
- 細到「句尾曲線、秒級停頓」的控制，H3 做不到 → 走外部配音（見 C 與下表）。

**外部配音對照：四維 → MiniMax T2A v2** [官方 platform.minimax.io/docs/api-reference/speech-t2a-http]

| 四維 | T2A 參數 | 範圍與限制 |
|---|---|---|
| 音量聲線 | `vol`、`emotion` | vol (0,10]；emotion 九種：happy / sad / angry / fearful / disgusted / surprised / calm / fluent / whisper。`fluent`、`whisper` 僅 speech-2.6 系列，2.8 不支援 whisper |
| 語速 | `speed` | [0.5, 2]；四維配音法建議最慢不低於 −20～−25%，用停頓代替全局慢速 |
| 停頓 | 文字內 `<#x#>` | x = 0.01–99.99 秒，**不可連用** |
| 音高 | `pitch` | 整數 [−12, 12]，**整句一個值** |
| 句尾語調 | **無參數** | 用標點（`？` `……`）近似，或多抽幾版挑，或後製做 pitch envelope |
| 語氣詞 | `(laughs)` `(sighs)` `(breath)` | 僅 speech-2.8 |

## C. 必須配音時：避開口型

原則：**H3 音畫同批生成，事後換聲音就失去對位**，所以要換聲音的鏡頭，畫面就不能有「正在說話的嘴」。

1. 先定配音時長，再反推 shot 長度（H3 單段 5–15 秒；12 個英文字約 5 秒）。「先出畫面再配」查無可靠流程。
2. 適合外部配音的鏡頭：
   - **畫外旁白**：`says in an off-screen voiceover while lips remain completely closed`。
   - **內心戲 / 系統音 / 電話另一端**：畫面給持續動作（低頭讀信、轉身走），不給正臉說話。
   - **背影、遠景、遮擋嘴部、cutaway 反應鏡頭**：對白期間畫面切去聽者或物件。
   - 不說話寫法見 audio-and-dialogue §6；「站著看鏡頭」最容易自行補說話。
3. 一定要有正臉口型又要換台詞：
   - 先試 H3 自己的 `[video editing + audio reference + audio reuse]`（A 節）。
   - 外部口型工具：**LatentSync 1.5**（程式 Apache-2.0，需 8 GB VRAM；1.6 權重是 openrail++ 有使用限制，需 18 GB）、**MuseTalk**（程式與權重 MIT，其相依模型各有授權）、Sync.so（付費，能辨識畫外說話者，只對畫內人臉做口型）。**Wav2Lip 開源版禁止商用，不要用於交付。** [官方 repo LICENSE / README]
4. 要把外部配音疊上去：`-an` 丟掉原生整軌，聲場自己重建（見 D）；不要只靜音環境聲，因為對白在同一軌 [官方]。

## D. 後製音效：何時改用外部音效

**H3 原生音效何時不可靠** [社群，單源；穩定類別查無實測]：大聲場景（爆炸、撞擊、人群）易失真爆音（ComfyUI issue 15283，與取樣器有關）、時序漂移、背景人聲亂語、無預期配樂。需要對位的 foley（開門、腳步）、需響度控制或指定配樂時，也不要賭原生。

因為輸出是單軌，決策分三路：

| 情況 | 做法 |
|---|---|
| 要留原生對白 | **不要靜音**。提示詞把 `overall_soundscape` 壓到只剩 room tone，再用 `amix` 往上疊外部音效 |
| 對白也改外部配音（C 節） | 整軌 `-an` 丟掉，聲場全部重建 |
| 環境聲壞了又要留對白 | 先做人聲分離（demucs、MossFormer 類），再疊音效；會殘留瑕疵 [推測] |

`soundscape: N/A` 並不保證靜音；失敗分診表記錄的 20% 漏出是指**配樂**寫了 `N/A` 仍出現音樂，不是環境聲。

### Openverse 取得音效 [官方文件 + 實測]

- 端點 `GET https://api.openverse.org/v1/audio/`，匿名可用；限額 **20 次/分鐘、200 次/天**；匿名 `page_size ≤ 20`。註冊 OAuth2 為選用。
- 篩選：`license=cc0,by`（只要這兩種）、`source=freesound`、`length=short`、`q=`關鍵字。**不要用 `category=sound_effect`**：實測回 0 筆，原因是 freesound 條目的 category 欄位多半沒填（None）。
- 相關度偏寬（`door close` 會回車門、`city ambience` 會回滑板），要多給關鍵字並人工聽過。
- 下載網址是 freesound 的 **mp3 preview**（44.1 kHz 立體聲），不是原始 WAV。
- 每筆回傳的 `attribution` 字串可直接當署名文字。

授權（Creative Commons 4.0 原文）：

| 授權 | 能不能用 | 要做什麼 |
|---|---|---|
| CC0 / PDM | 可 | 不強制標示，仍建議保留來源記錄 |
| CC BY | 可 | 署名、標授權、註明有修改 |
| CC BY-SA | **避開** | 錄音與影像時間同步即構成 Adapted Material，整支影片得以 BY-SA 釋出 |
| NC / ND / sampling+ | **避開** | `license_type=commercial,modification` 會放進 by-sa 與 sampling+，所以改用 `license=cc0,by` 明確指定 |

每個用過的音效記一列：`title, creator, license, attribution, source_url, modifications`（修改欄寫 trimmed / −6 dB / mixed），片尾或說明欄貼 `attribution` 字串。

### ffmpeg 疊音效與響度

```bash
ffmpeg -i video.mp4 -i sfx.mp3 -filter_complex \
"[1:a]adelay=2000:all=1,volume=0.8[sfx];[0:a][sfx]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]" \
-map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 out.mp4
```

- `adelay=2000:all=1`：SFX 延後 2 秒進入（`2000|2000` 只對雙聲道有效）。
- `amix normalize=0`：不自動降音量；`duration=first` 以影片長度為準。
- `loudnorm` 預設輸出 192 kHz，所以要補 `-ar 48000`；混完用 `ffprobe` 驗輸出取樣率。單次 loudnorm 約有 ±0.5 LU 誤差，正式交付跑兩次。
- 要壓低背景讓對白清楚：用 `sidechaincompress`（指令可跑，實際壓降量沒量測）。
- 原版指令只用合成測試音在本機跑通，修正版（`:all=1`、`-ar 48000`）未重跑，用前先試一次。

## 仍未驗證（需要在自己機器上做 A/B）

原始紀錄在私有 repo，未公開。飛書手冊需要登入，未取得，不能排除其中有其他說法。
