# memory.md — 跨 agent 交接記憶

每次收工更新。最新的在上面。

## 現況（2026-10-16 初始化）

- repo：https://github.com/ayase0307/h3-video-prompting（main，MIT）
- 本機：`E:\MinimaxH3\h3-video-prompting`
- 性質：MiniMax H3 / 海螺 3 的影片提示詞 Agent Skill；依賴官方 `h3-prompt-writing` 負責最終排版
- 發布區 25 個檔：`SKILL.md`、`references/`（18 份）、`assets/`（2 圖）、中英 README、LICENSE
- 最後一個 commit：`a15f18b` Fix self-check light/foreground rules under word budget; widen SKILL triggers
- 誠實的限制：跨 shot 變化規則、spec 卡、光線路徑等是方法主張，尚未在 H3 驗證（見 `references/shot-variety-and-staging.md` §11）

## 進行中（動檔案前先看、收工清掉）

（無）

## 待辦

- [ ] 音訊規則散在 10+ 份文件，考慮在 `audio-and-dialogue.md` 加一張「去哪找什麼」索引（尚未動工）
- [ ] 跑 `shot-variety-and-staging.md` §11 的 A/B 測試並把結果記到 `workspace/experiments/`

## 決策紀錄

- 2026-10-16：工作區 / 發布區用 `workspace/` 資料夾切開；草稿先進工作區，驗證後晉升（見 `agent.md` §3）
- 2026-10-16：`workspace/` 不被 `SKILL.md` 引用；`npx skills add` 仍會帶入整個 repo，暫時接受

## 已知坑

- claude-mem 觀察器憑證失效（2026-10-14 起），不能靠它存記憶；交接只靠本檔
- 這個資料夾沒有 CLAUDE.md；規範以 `workspace/agent.md` 為準
