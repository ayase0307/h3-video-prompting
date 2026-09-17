# 聲音與對白

來源：官方 base-en.txt 4.4/4.6/4.7；官方飛書手冊評論區回覆；ambienceai 對白預算實測；debutify 對白表演；audiencescience 三層時間軸；atlascloud lip-sync 實測；virse 聲音參考限制；AI-KSK dialogue-audio-recipes；aireiter 引用的 Reddit 回報。

## 1. 三層音軌各歸其位

| 層 | 寫在哪 | 內容 |
|---|---|---|
| 對白 / 唱歌 / 角色聽得到的音樂 | `integrated_multimodal_description`（或 `detailed_description`）動作旁 | 說話者 + 語氣 + `<d>[Language] 原文</d>` |
| 環境聲、動作音效、非語言人聲 | `overall_soundscape`（1–4 句） | 風雨車流、腳步布料撞擊、呼吸笑聲喘息 |
| 觀眾才聽得到的配樂 | `non_diegetic_music`（1–3 句） | 樂器、速度、節奏、動態變化；不寫情緒詞 |

- 收音機 / 手機 / 現場樂器的音樂是 diegetic，寫在描述裡，不是配樂欄。
- 音效寫兩次：動作旁一次，`overall_soundscape` 依事件順序再述一次（官方回覆）。
- 音量用相對混音描述（`well under the voice`、`voice clear and centered above the ambience`），不寫百分比或 dB。
- 配樂進出：「某事件前無音樂 → 事件時進入 → 某事件後完全停止」。範例：`Use no music during the conversation. After the final line, introduce one restrained piano note and let it fade.`
- 靜音要明說：`non_diegetic_music: N/A`；環境聲全靜才寫 `overall_soundscape: N/A`。

## 2. 對白預算（ambienceai 實測）

- 15 秒約 20 個英文字；每句約 10 字；一個 `<d>` 只放一個句子，兩句就拆兩個 `<d>`。
- 12 個英文字約 5 秒。先用預期語速唸一遍，再加前後反應時間；猶豫的角色要多 1–2 秒。
- 一個 3 秒 shot 講一大段話，口型必壞（官方）。
- 短片只做一個交換：一問一答、一句陳述一個反應、一次反駁一個停頓、一個揭露接沉默。
- 寫口語不寫書面：`Going to the station tonight? I don't think that's a good idea.`

## 3. 說話者與台詞格式

- 說話者 ID `(S1)`、`(S2)`，合唱 `(S1,S2)`，全篇不換號；不出聲的角色沒有 ID。
- 第一次出現給足身份：年齡、性別、畫內/畫外、音高、音色、語速、口音。這些**全放在 `<d>` 外面**；`<d>` 裡只有語言標籤和逐字台詞。
- 畫內說話寫 `visible on screen and says`；畫外音寫 `says in an off-screen voiceover` 並緊接 `while his lips remain completely closed`。
- 跨切點：兩側加 `<scenetrans>` 並寫 `continues seamlessly across the cut`；被結尾截斷用 `<cutoff>`。
- 對白跨 shot 的官方例：`一個畫外音響起說：Wake up Wake up。之後切鏡到一個中年婦女的近景，她是畫外音的主人，她繼續說道：It's time to go to school!`
- `<d>` 出現亂語或多餘人聲 → 同一句改純引號重試，不重寫整段（社群回報 `<d>` 路徑偶爾不穩）。

## 4. 表演方向：意圖 > 情緒

- `Daniel tries to sound casual, but hesitates before replying, "No. Of course not."`
- 每句 2–3 個相關線索：`quiet and measured`、`low and restrained`、`breathless after running`、`firm without shouting`、`warm and reassuring`。
- 重音：`placing subtle emphasis on "wait"`。
- 停頓與輪替：`Maya remains silent for one second. She studies his expression before replying`。
- 聽者要有反應動作（看見對白指南 motion-quality.md §5）。
- 對白時鏡頭少動、臉保持可見；重要台詞不要配快速切鏡或大運鏡。

## 5. 聲音參考（Ref2VA `<Audio N>`）

- `<Audio 1>` 是音色/語氣參考時，台詞來自 prompt，**參考音檔要唸不同的句子**，否則模型會直接複製音軌。
- 明寫角色：`<Audio 1> is the voice-timbre reference for <Subject 1> (S1). Reference the timbre only; do not reuse its words.`
- 聲音參考不是波形保留：語句會被重新合成；0.1 秒的時序差就可能掉字。對白必須逐字精確時，把原音當獨立資產後製。
- 參考影片自帶音軌會滲入（女聲笑套到男角色）；換匹配的參考或在 Sound 句明寫。
- 限制：音檔 ≤3 段、每段 2–15 s、總長 ≤15 s；音檔不能單獨當參考，至少配一張圖或一段影片。
- 系列作品：同一個聲音參考用到底，換聲音比換任何變數都更破壞連續性。

## 6. 不說話、不亂語（官方回覆整理）

正向：`人物全程保持安靜，嘴巴自然閉合，沒有說話或對話，面部只有輕微自然表情。`
負向補充：無對白、無人聲、無念白、無口型變化、無自言自語。
避免：對著鏡頭、交談、講述、激動表達、嘴唇微動；少用引號和台詞格式。
給持續動作：專注觀察、低頭閱讀、轉身行走；「站著看鏡頭」最容易自行補說話。
特寫仍不穩：側臉、背影、中遠景。

## 7. 字幕與畫面文字

- 官方建議**不要**在 prompt 寫「不要字幕」（可能反而觸發）；改用不含文字的畫面描述，並減少台詞字數。字幕仍出現 → 後製裁掉。
- 要可讀的字：逐字打出來加引號 + `do not misspell, do not add other text`；品牌字用圖片參考或後製疊字。
- 沒打出來的字（「HUD elements」）會變成字形噪音。

## 8. 音效與動作同步

- 每個音效緊貼它的視覺原因：`[6.2s] She pulls the tab open. A sharp metallic click occurs first, followed immediately by a short carbonation fizz.`
- 大聲的 beat 不要同時放台詞：先講完再進打擊樂或車輛音效。
- 音效時序漂 → 減少音效數量或簡化場景，不要加更多描述。
- 慢動作 shot 的聲音也要拉長：`the contact stretches into a low, drawn-out scrape`。
- 環境聲先給基線（room tone），再疊事件；背景人聲要 `indistinct, no background words clearly audible`。

## 9. 配樂寫法

```text
non_diegetic_music: A trap beat at a half-time feel around 140 BPM with deep sliding
808 bass hits, sharp snare on the backbeat, and rapid hi-hat rolls, starting at full
volume from the first frame. During the slow-motion shot the drums drop out to a single
sustained 808 note, then the full kit returns on the windmill and ends on one final hit.
```

- 樂器 + 速度 + 進入/高潮/停止時間點；官方片頭範例：`first 2 s low frequencies and hi-hat; low drums at 3 s; jazz-bass at 6 s; sax riff at 10 s; freeze the last 2 s on a tense chord`。
- 不模仿現有旋律：`do not imitate an existing melody`。
- UGC / 對白戲預設無音樂；一有配樂就像廣告。
