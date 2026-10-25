# 每個 [Shot N] 寫滿五小節（Camera／Motion／Performance／Light／Sound）

> 適用範圍：一般可用，不設硬條件；agent 先自由寫，超過建議字數時由使用者決定（見「字數與字元上限」）。證據有限：T8 是 t2va、15 s、非盲評的先導；EP01 是 Ref2VA 短段（8–9 s）的主觀實戰案例。兩者都沒有 A/B 對照，Ref2VA 下的效果待 A/B。原始實驗紀錄在私有 repo，未公開。
>
> 可信度：**[實戰]** 守富 2026-10-21《我修的是遺忘課》EP01（12 段、35 鏡、Ref2VA 六段式、本地 FreeVideo）主觀評估效果不錯；**尚未做 A/B 對照**，字數放寬對臉部一致性的影響待驗證（見文末「待驗證」）。

## 為什麼

`[Shot N]` 只寫一句動作時，H3 會自己補運鏡落點、表演與光，常補成平均值（表情僵、光平、聲音空）。把每個 shot 拆成固定五小節，等於逐鏡交一張完整的規格卡，也讓審稿時一眼看出哪一軸漏寫。

## 一行的組成（順序固定，整鏡一行不換行）

```text
[Shot N] At MM:SS.mmm, the shot cuts to a <景別> (<焦距>, <物距>) of <主體>, as the camera <官方運鏡詞>. Camera: …  Motion: …  Performance: …  Light: …  Sound: …  <台詞：<d>…</d>／外部 TTS 說明／Lips stay closed.>
```

頭句（景別、焦距物距、主體、唯一的官方運鏡詞）照官方排版；五小節接在後面；台詞 `<d>` 放最後。

## 五小節寫什麼

| 小節 | 內容 | 句型提示 |
|---|---|---|
| **① Camera** | 焦距＋物距＋機位高度／方位；運鏡幅度、速度、時長；起幅與落幅（主體在畫左畫右、落在哪條三分線）。固定鏡寫 `locked off for 2.0 s`。 | `85mm from three metres at his kneeling eye height, moving slowly closer by about ten percent over 3.5 s, from a loose close-up to a tight one; …` |
| **② Motion** | 起始狀態 → 施力點／方向／速度 → 支撐、重心、慣性 → 結束狀態；每鏡仍只 1 個主動作。 | `First …, then …, as …, finally …` |
| **③ Performance** | 眉、眼、嘴、肩、呼吸的微變化與情緒轉折；寫可見的變化，不寫情緒清單；聽者也要演。無臉鏡改寫手、背、姿態的表演。 | `Red-rimmed eyes that stay dry; a short breath through the nose between the two sentences; …` |
| **④ Light** | 光源方向＋色溫；材質對光；水面、紙、布、灰塵、濕石板等環境回應；跨鏡光源一致。 | `Cool top light slides down his face as he rises, catching the wet strands at his temple; …` |
| **⑤ Sound** | 鏡內音效的秒數（`at about 0.8 s`）、環境音；有台詞寫起口時間；外部 TTS 鏡寫明說話者嘴不入畫（`her mouth out of frame behind her head`），但不要寫 speaks／says 這類說話動詞（沒有 `<d>` 時 H3 會自編亂語）。 | `The clay base grates on stone at about 0.8 s; he speaks about 0.3 s after the bowl stops.` |

## 硬規則（五小節內也要守）

- 運鏡詞只出現在頭句：五小節內不寫第二個運鏡動詞（push／pan／tilt／zoom／truck／dolly／pedestal／track）、不寫 `the camera`、不寫 orbit／arc／360。
- 不重述參考圖外觀（髮型、五官、服裝只在 `subject_definitions`）。
- 不寫 `cinematic／epic／dynamic／volumetric`、`looks at the camera`。
- 收尾不要寫靜止（`comes to rest／settles`），停在動作過程中（`holds there`、`stays suspended`），避免被定格吃掉。
- 無配樂段 `non_diegetic_music: N/A`，全文不出現 music／score 等字。
- 一個 `<d>` 一句；每段影格仍守 17k+5。
- 非寫實風格不加皮膚段，也不寫 bokeh／depth of field 等鏡頭語彙。

## 字數與字元上限

- 寫五小節時，`detailed_description` 會超過 350–500 英文字建議值；EP01 實測每段 430–940、T8 為 519–636。**≤700 是未實測的建議值**（沿用純文字 300–700 預算），不是硬規則。

### 流程：agent 先寫、說明、使用者決策

1. **先自由寫完整版**，不預先砍字。
2. 數英文字數與字元數。
3. 超過 700 英文字時，向使用者報告：實際字數；若要照技能壓縮，**預計犧牲哪些內容**（照下面的壓縮順序逐項列出具體要刪什麼，以及鏡內小節是否會被動到）；保留完整版的風險（文字跟參考圖搶臉、後段細節被忽略，皆未驗證）。
4. 由使用者選：**照技能壓縮／放行完整版／折衷**。使用者沒回覆前，不擅自壓縮，也不擅自送出。
5. 例外：送件端硬上限（hosted API 7000 字元）不能放行，超過只能壓縮或拆段。

壓縮順序（先壓縮其他欄位，**不刪鏡內小節**）：
  1. `retention_analysis` 連戲錨只留 axis＋blocking；
  2. `retention_analysis` 逐鏡裁切說明只留「誰露臉」一句；
  3. 次要角色去服裝描述尾巴；
  4. `subject_definitions` 主角外觀改短稱；
  5. 場景圖描述只留首子句。
  仍超限就交給人決定（拆段，或本地無上限時照送）。

## 範例（Ref2VA，2 張參考圖，懸疑對白特寫）

```text
[Shot 1] The scene opens with <Picture 1> as a scene/style reference for spatial guidance: Close-up (85mm, 3m) of <Subject 1>, as the camera dollies in. Camera: 85mm from three metres at his kneeling eye height, moving slowly closer by about ten percent over 3.5 s, from a loose close-up to a tight one; he holds three-quarter profile facing frame left, his eyes ending on the upper third line. Motion: First his forehead lifts off the bowl rim, then his spine straightens vertebra by vertebra and his chin rises to meet her eyes off-screen left, as the white ring mark on his right wrist flashes past the bottom edge, finally he slows the last three syllables and holds his jaw still. Performance: Red-rimmed eyes that stay dry, cracked lips, each word set down separately; a short breath through the nose between the two sentences; after the last word his gaze does not retreat. Light: The ceiling light behind his shoulder drifts slowly; cool light slides down his face as he rises, catching the wet strands at his temple and the damp edge of his collar. Sound: Water drips from his soaked cuffs; he begins at about 0.2 s and slows on the final three words. <Subject 1> (S1) says: <d>[Chinese] 再刪一次，她便只剩不存在。</d>, then after a short pause <Subject 1> (S1) continues: <d>[Chinese] 我不刪。</d>.
```

## 送出前自檢

- 每個 `[Shot N]` 五個標籤都在、順序正確。
- 五小節內沒有第二個運鏡詞、沒有外觀重述。
- 全文字元 ≤ 送件端上限。

## 待驗證

- 五小節版 vs 舊版一句式：同 seed A/B，比較表演自然度、臉部一致性（文字變長是否與參考圖搶臉）。
- 字數上限：超過 500、700 英文字後是否開始出現細節被忽略或混臉；實測後再決定 ≤700 要保留、調整還是拿掉。
- 本檔的「使用者決策」流程是暫行做法，實測有結論後改成明確門檻或預設值。
