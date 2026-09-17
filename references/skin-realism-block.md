# H3 影片提示詞骨架（守富定版）

守富 2026-09-16 指示：之後所有影片提示詞一律參照此寫法，皮膚段完全比照，前兩段（鏡頭、光線）依場景情境改寫。

## 使用方式

三段結構，順序不可換：

1. `【鏡頭——<一句賣點形容>】` — 依場景改寫：機位／視角高度／景別／構圖框住範圍／是否晃動焦距／背景虛化內容／整體觀感。
2. `【光線——<色調形容>】` — 依場景改寫：光源性質（暖柔光／冷硬光…）、光從哪來、明暗過渡、有無硬陰影、補光方向、輪廓光、皮膚在該光下的呈色。
3. `【皮膚——通透白皙有真實肌理】` — **整段照抄，只微調光色字眼（例如冷光場景把「暖光」改成「冷光」、把「粉橘輪廓光」換成「銀藍輪廓光」），其餘一個字都不動。**

## 皮膚段（定版原文，照抄）

(visible skin pores:1.2), (natural skin micro-texture:1.1), (peach fuzz vellus hairs:1.0), (subsurface scattering:1.3), (fair luminous translucent skin:1.4), (natural skin radiance:1.2).
皮肤白皙通透、粉白粉白，有由内而外的自然光感和透光感。次表面散射让耳朵、鼻翼、脸颊边缘、肩头在暖光下微微透光，呈薄粉白色，像玉石温润。脸颊有自然粉意，鼻尖微泛红。毛孔细小可见但不粗大，大小疏密自然；脸颊边缘和鬓角极淡细绒毛在逆光下有金色绒光晕；上唇上方极细浅色绒毛；下眼睑薄皮肤透出淡青色；鼻翼两侧极淡红血丝和毛孔纹理；嘴唇有自然纵向唇纹，饱满粉嫩，微有光泽但不是唇釉假亮；自然少女眉有碎毛；睫毛根根分明自然纤长；脖颈白皙光滑无青筋凸起；胸口锁骨附近一颗极小的痣。远看白皙透亮，近看有细腻真实纹理。35mm Kodak Portra 400胶片，银盐颗粒细腻

### H3 散文版（去權重語法，H3 用這份）

photorealistic skin with visible pores and natural micro-texture; fine peach-fuzz vellus hairs along the cheek edge and hairline catching a golden rim light in backlight; subsurface scattering makes ears, nostrils, cheek edges and shoulders glow faintly translucent — a soft powder-pink, jade-like warmth. Cheeks carry a natural flush, nose tip slightly pink. Pores stay fine and small, never coarse, with natural spacing. Above the upper lip, very fine pale vellus hair; under-eye thin skin shows a faint blue undertone; faint capillaries and pore texture beside the nose; lips have real vertical lip lines, full and soft-pink with a slight natural sheen, never gloss-sticker shine; natural brows with stray hairs; lashes individually defined, long and natural; neck smooth and fair with no protruding veins; one tiny mole near the collarbone. Fair, luminous and translucent from a distance, fine and real up close. Shot on 35mm Kodak Portra 400 film, fine silver-halide grain.

## 為什麼不能直接用權重語法

H3 的 prompt 由 Qwen3-VL-32B 語言模型解析，不是 CLIP 標籤比對：`:1.2` 這種數字權重不被解析，會被當成雜訊稀釋描述力。權重語法要一律改寫成敘述句（「毛孔細小可見但不粗大」而不是 `(visible skin pores:1.2)`），詞彙本身照留。

## 已驗證搭配

皮膚感可與 fal MiniMax-H3-Realism-People-LoRA（trigger `r34l1sm`）並用；此骨架放在 prompt 主體，`r34l1sm` 仍置最開頭。
