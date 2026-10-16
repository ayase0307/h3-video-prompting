# 音訊 A/B 測試清單

來源：2026-10-16 Opus 審查。每項固定 seed、各抽 3 次，結果記回本檔，驗證後才能把 `references/audio-pipeline.md` 的 [推測] 升級。

| # | 問題 | 比較 | 怎麼量 | 結果 |
|---|---|---|---|---|
| 1 | 首段音軌能鎖音色嗎 | S1 同一句台詞：(A) 不加 `<Audio>` vs (B) 加首段剪出的 `<Audio 1>` | 盲聽評分，或用 resemblyzer 算 speaker embedding 餘弦相似度 | 未做 |
| 2 | 續接哪個聲音斷點小 | 同一段尾巴：(A) FL2VA 尾幀接續 vs (B) Ref2VA `[video continuation + audio reference]` | 聽音色與環境聲斷點 | 未做 |
| 3 | 四維描述有沒有用 | 同一句台詞：(A) `angrily` vs (B) 四維物理描述 | 量 RMS 音量、語速（字/秒）、停頓長度 | 未做 |
| 4 | H3 能換台詞並對嘴嗎 | `[video editing + audio reference + audio reuse]` vs LatentSync 1.5 | 口型準度、音色 | 未做 |
| 5 | soundscape 壓到 room tone 再疊音效 | 提示詞只留 room tone，疊外部音效 | 聽是否殘留事件聲 | 未做 |
| 6 | ffmpeg 修正版指令 | `adelay=...:all=1` 與 `-ar 48000` | `ffprobe` 驗取樣率、onset 時間 | 未做 |
