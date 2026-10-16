# agent.md — 進場規範

所有 agent（Claude、Codex、其他）進來修建前先讀完本檔，再讀 `memory.md`。

## 1. 開工前（依序）

1. `git pull --rebase origin main`（別的 agent 可能剛推過）
2. 讀 `workspace/memory.md`：現況、待辦、上一位留下的注意事項
3. 讀 `SKILL.md`（發布區入口，決定整個 skill 的結構與語氣）
4. 只讀你要改的那幾個 `references/*.md`，不要整包灌

## 2. 區域規則

- **發布區**（`SKILL.md`、`references/`、`assets/`、`README*.md`、`LICENSE`）：使用者安裝的內容。
- **工作區**（`workspace/`）：草稿、待辦、實驗、交接。
- 不確定的規則、沒在 H3 上驗證過的主張 → 先寫進 `workspace/drafts/` 或 `memory.md`，不要直接進發布區。

## 3. 晉升（工作區 → 發布區）

必須同時滿足：
- 有來源（官方文件、社群實測連結）或自己的 A/B 結果（記在 `workspace/experiments/`）
- 可信度標註清楚：官方 / 社群實測 / 方法主張（比照 `references/community-sources.md`）
- 沒和現有規則衝突；衝突就在 `memory.md` 記一筆決策並改掉舊規則
- 版面一致：`SKILL.md` 的情境索引、預算表、十條速查若受影響要同步改

## 4. 寫作約定（沿用現有風格）

- 參考文件用繁體中文；prompt 範例、欄位名、`<d>` 標籤保持英文
- 每條規則寫「怎麼做 + 為什麼 / 壞掉長怎樣」，不寫形容詞口號
- 新增 reference 檔：要在 `SKILL.md` 的索引與 `README.md` / `README.zh-TW.md` 的內容表各補一行
- 不複製第三方原文，只整理規則與重寫；來源寫進 `references/community-sources.md`
- 一次提交只做一件事

## 5. Commit / Push

- 格式：`<type>: <description>`，type ∈ feat / fix / refactor / docs / test / chore
- 發布區與工作區的變更**分開 commit**（方便回溯哪些是對外變更）
- 推送前：`git pull --rebase origin main`，有衝突就解完再推，**不 force push**
- 交接檔 `memory.md` 的更新與該次工作同 commit 或緊接一個 `docs:` commit
- 不 commit 暫存檔、生成的影片/圖片、金鑰

## 6. 收工清單

- [ ] 更新 `memory.md`：做了什麼、沒做完什麼、下一位該注意什麼
- [ ] 發布區若有改動：`SKILL.md` 索引與兩份 README 內容表一致
- [ ] `git status` 乾淨、已 push
- [ ] 沒有誤改別人正在做的檔案（先看 `memory.md` 的「進行中」欄）

## 7. 並行衝突

同時可能有別的 agent 在改。開工時在 `memory.md` 的「進行中」寫下你要動的檔案；收工時清掉。看到別人佔用的檔案就換別的做或在待辦留言，不要硬改。
