# 範例：10 秒屋頂打鬥（T2VA，無配樂，卡點靠音效）

Brief：10 s、16:9、實拍電影感。女劍客在雨夜屋頂對兩名蒙面刺客。要有節奏、切點落在拍子上、一個慢動作格擋、快速收尾踢人下樓。無配樂，角色不說話。

## 預算決定

- 10 s → 4 個 shot（2.5 / 2.5 / 2.5 / 2.5 左右，依資訊量微調），每個 shot 一拍。
- 沒有音樂，「拍子」= 每次金屬接觸聲；在 Shot 1 就宣告規則。
- 慢動作獨立成 Shot 3，該 shot 把大雨降成細雨、拿掉背景霓虹閃爍。
- 三個角色：一次只讓一個刺客行動。
- 不說話：開頭正向宣告，全片給她持續動作，不寫「看鏡頭」。

## Prompt

```text
integrated_multimodal_description: [Shot 1] Live-action, cinematic, a medium-wide shot frames a rain-soaked rooftop at night, one floodlight from frame-left, puddles reflecting a still skyline. A female swordswoman in a fitted black jacket with dark hair tied back stands center, straight sword held low in her right hand; she stays silent throughout the video with her mouth naturally closed. Masked assassin A crouches frame-left with a curved knife, assassin B stands frame-right, holding position. Every cut in this video lands exactly on a blade-contact sound. First assassin A lunges forward with the knife aimed at her ribs, then she steps back with her left foot and swings the blade across her body, as steel meets steel with a sharp ring and A is knocked one step back. The camera holds a static shot.

[Shot 2] At 00:02.500, on that ring the shot cuts to a medium two-shot from behind her right shoulder: A recovers frame-left; B sprints in from frame-right and hurls his knife straight at her face. The camera trucks right with small amplitude at fast speed to keep both bodies in frame, ending as the knife leaves his hand.

[Shot 3] At 00:05.000, the shot cuts to a close-up in slow motion: light drizzle, no wind, the background reduced to a dark flat wall. The thrown knife spins toward the lens; her blade rises from below the frame and deflects it with a bright metallic flash, and the knife tumbles out of frame upward. The camera holds a static shot. Only the drizzle and the single slowed metallic contact are audible.

[Shot 4] At 00:07.500, on that contact the shot cuts back to real time, a wide profile shot along the rooftop ledge: B, now unarmed, rushes her from frame-right; first she steps inside his reach and plants her left foot, then drives a spinning back kick into his chest, as he is launched backward over the ledge and drops out of frame. The camera trucks left with small amplitude at fast speed following the kick, then holds as she lowers the sword and looks down over the edge, breathing steadily, mouth closed.

overall_soundscape: Steady rain drums on the rooftop and metal vents with a low wind under it. Boots splash in puddles and wet fabric snaps with each movement. Two sharp blade-contact rings mark the first parry and the deflection, the deflection stretched and low during the slow-motion shot, followed by a heavy kick impact, a short fading yell as the assassin falls, and her controlled breathing at the end.

non_diegetic_music: N/A
```

## 為什麼這樣寫

| 決定 | 對應規則 |
|---|---|
| 4 個 shot、最短 2.5 s | shot ≥ 2 s；10 s 內 3–4 個 |
| 每個 shot 只有一個刺客動作 | 一拍 = 建立→攻擊→接觸→反應 |
| 「Every cut lands on a blade-contact sound」 | 卡點寫觸發物 |
| Shot 3 drizzle + flat wall | 慢動作降熵 |
| 「on that ring / on that contact the shot cuts」 | cut 綁事件，不綁「energetic」 |
| 開頭「stays silent … mouth naturally closed」+ 全片都在動 | 官方不說話寫法 |
| 音效在動作旁寫一次、soundscape 依序再述 | 官方音效建議 |
| N/A 且全文無音樂情緒詞 | 防漏音樂 |
