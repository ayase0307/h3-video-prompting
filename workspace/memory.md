# memory.md — 跨 agent 交接記憶

每次收工更新。最新的在上面。

## 現況（2026-10-20 更新：先導 A/B T1/T2/T3/T4/T6 已跑完並審查）

- 先導 A/B（0.5MP/medium/6s，n=3，T3 n=6，Haiku 盲評 2fps 接觸表）結果已寫進發布區規則旁的證據標註；總表見 `workspace/experiments/ab-master-plan.md` §結果
- 證據等級一律是「本機先導實測（n=3, 0.5MP）」，不是官方

## 初始化紀錄（2026-10-16）

- repo：https://github.com/ayase0307/h3-video-prompting（main，MIT）
- 本機：`E:\MinimaxH3\h3-video-prompting`
- 性質：MiniMax H3 / 海螺 3 的影片提示詞 Agent Skill；依賴官方 `h3-prompt-writing` 負責最終排版
- 發布區 25 個檔：`SKILL.md`、`references/`（18 份）、`assets/`（2 圖）、中英 README、LICENSE
- 最後一個 commit：`a15f18b` Fix self-check light/foreground rules under word budget; widen SKILL triggers
- 誠實的限制：跨 shot 變化規則、spec 卡等仍是方法主張；光線路徑已測、降為風格建議（見 `references/shot-variety-and-staging.md` §11）

## 進行中（動檔案前先看、收工清掉）

- （無）

## 待辦

- [x] 音訊規則索引已加在 `references/audio-and-dialogue.md` 開頭（2026-10-16）
- [ ] 跑 `workspace/experiments/audio-ab-tests.md` 的 6 項 A/B，驗證後把 `audio-pipeline.md` 的 [推測] 升級
- [ ] 飛書手冊需登入未取得；有權限的 agent 補查聲音／情緒／音色一致的說法
- [ ] 用 `four-dimensional-voice-acting` 的 `voice_distiller.py` 產出 MiniMax T2A 參數的轉換腳本（目前只有對照表，在 `audio-pipeline.md` §B）
- [x] 先導 A/B T1/T2/T3/T4/T6 跑完並審查（2026-10-20）
- [ ] T5（跨段光色重述）、T7（字數預算，10 s）尚未凍結與執行
- [ ] 勝出/維持的規則（T2、T4、T6）用 0.98MP 各複驗 1 輪；T3 的降級也可在 0.98MP 或人工看臉複驗
- [ ] T1 換更難的動作（兩段連續動作或有接觸的動作）重做，避開盲評天花板
- [ ] T6 加一臂「i2va 首幀＝臉部特寫」，分離「多一張特寫」與「Ref2VA 路線」
- [ ] 盲評接觸表解析度太低（每幀寬 272px），下批改用較大的單幀或裁臉
- [ ] 其餘 `shot-variety-and-staging.md` §11 項目（§3 四軸、§5 前景、焦點轉移、§8 峰值靜止）仍未測

## 決策紀錄

- 2026-10-21：吸收守富提供的「寫實 15 秒電影腳本」system prompt：新增 180 度線、因果五步/尺度/不瞬移/招牌技能（action-choreography §16）、soundscape 遠近與三段衰減、配樂人聲與曲風、品牌不捏造、SKILL 交付規則；全標方法主張。不採用：一律六段、`[Shot N] — Title (區間)`、風格當 Subject、每 shot 五小節段落、渲染詞堆疊（對照表在 prompt-formats.md 附錄）。待測：180 度線與因果五步可排 A/B

- 2026-10-20：T1 動作鏈（action-choreography §11）：盲評兩臂全滿分（天花板），composite 3/3 平手 → 未定論，規則維持方法主張；殘留動作 B 3/3 較低僅描述。原 summary 誤判為晉升，已更正
- 2026-10-20：T2 時間戳切點（prompt-formats.md）：B 6/6 命中、平均誤差 0.045 s、A 2/6 → 晉升「本機先導實測」；「不寫時間戳就一鏡到底」在含 `the shot cuts to` 時不成立。證據不適用 shot-variety §3 四軸
- 2026-10-20：T3 光線路徑（shot-variety §6、lighting-and-color §A）：6 seed B 勝 1 平 5，A ≥ B 5/6 → 降級為風格建議；§10 自檢 #8 改選用。原 summary「6/6」「n=3 未定論」已更正
- 2026-10-20：T4 HEX vs 色名（lighting-and-color）：兩平一色名略近、無 HEX 勝 → 維持「色名＋物體，不寫 HEX」，標本機先導實測；兩臂離色卡都很遠
- 2026-10-20：T6 角色一致（action-choreography §10）：臉部一致 Ref2VA＋臉部特寫 3/3 勝 → 晉升為「要鎖臉時給臉部特寫參考」；混淆：多一張特寫、評分基準即特寫、服裝 ΔE 反向

- 2026-10-16：光影配色整合：新增 `references/lighting-and-color.md` 與 `scripts/color_qa.py`。HEX 色表不進主規則（H3 無證據），五層亮度與色卡標為自創；聲畫協同配對不採用；「300–700 英文字」降級為社群經驗值
- 2026-10-16：日轉夜編輯範例出自 Runware 頁面，不在官方 GitHub；綠幕兩句引文出處待核（疑飛書手冊）

- 2026-10-16：音訊研究整合：新增 `references/audio-pipeline.md`。流程為 5 位 Haiku 調研、Opus 審查補查。H3 無情緒控制欄位，所以四維配音法只在 H3 內當文字描述（有效性未驗證），細控併入外部 TTS（MiniMax T2A）；環境音不可靠時走 Openverse（`license=cc0,by`，不用 category 篩選）
- 2026-10-16：H3 輸出為單軌混音，「靜音環境聲留對白」不可行；決策拆成三路（見 `audio-pipeline.md` §D）
- 2026-10-16：L2VA ＝ FL2VA 的只給尾幀模式，不是音訊驅動口型；鎖音色只能走 Ref2VA

- 2026-10-16：工作區 / 發布區用 `workspace/` 資料夾切開；草稿先進工作區，驗證後晉升（見 `agent.md` §3）
- 2026-10-16：`workspace/` 不被 `SKILL.md` 引用；`npx skills add` 仍會帶入整個 repo，暫時接受

- [ ] 跑 `workspace/experiments/lighting-ab-tests.md` 的 7 項 A/B（HEX vs 色名、色卡、重打光、重述）
- [ ] 有飛書權限的 agent 核對綠幕兩句引文出處

## 已知坑

- claude-mem 觀察器憑證失效（2026-10-14 起），不能靠它存記憶；交接只靠本檔
- 這個資料夾沒有 CLAUDE.md；規範以 `workspace/agent.md` 為準

- 2026-10-21 T8（五小節 vs 散文，15 s×3 場景，seed 2001）完成，結果在 `results/T8/`；待辦：盲評＋≥3 seed＋「散文補光線/連戲句」對照臂，才能決定是否預設五小節。15 s/0.5MP/medium 每支約 23–27 分鐘。
