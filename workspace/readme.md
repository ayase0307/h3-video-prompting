# workspace/ — 工作區

這個資料夾是**多個 agent 輪流進場**的工作區，不是發布內容。

## 工作區 vs 發布區

| 區 | 路徑 | 用途 | 誰能改 |
|---|---|---|---|
| 發布區 | `SKILL.md`、`references/`、`assets/`、`README.md`、`README.zh-TW.md`、`LICENSE` | 使用者安裝到的 skill 本體 | 只在「晉升」時改（見 `agent.md` §晉升） |
| 工作區 | `workspace/` | 交接、待辦、草稿、實驗紀錄、待驗證的規則 | 每個 agent 隨時可改 |

原則：**草稿與未驗證的主張先進 `workspace/`，驗證過才晉升到發布區。**

## 檔案

- `agent.md` — 進場規範：開工前讀什麼、怎麼改、怎麼 commit/push、收工清單
- `memory.md` — 跨 agent 交接記憶：現況、待辦、決策、已知坑（每次收工更新）
- `readme.md` — 本檔
- `drafts/` — 草稿（需要時才建）
- `experiments/` — A/B 測試紀錄（需要時才建）

## 注意

`npx skills add ayase0307/h3-video-prompting` 會抓整個 repo，因此 `workspace/` 也會被帶進使用者的 skills 目錄。
`SKILL.md` 不引用 `workspace/`，所以不影響 skill 行為；若日後在意體積，再改用發布分支。
