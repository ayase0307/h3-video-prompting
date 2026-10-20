"""Copy shuffled contact sheets + brief to E:/MinimaxH3/_blind/<T> (outside repo). Usage: python blind_prep.py T3"""
import json, pathlib, random, shutil, sys
t = sys.argv[1]; E = pathlib.Path(__file__).resolve().parents[2]
p = json.load(open(E / f'results/{t}/plan.json', encoding='utf-8'))
d = pathlib.Path(f'E:/MinimaxH3/_blind/{t}'); d.mkdir(parents=True, exist_ok=True)
codes = [f.stem for f in (E / f'_local/{t}/thumbs').glob('*.jpg')]; random.shuffle(codes)
for i, c in enumerate(codes, 1): shutil.copy(E / f'_local/{t}/thumbs/{c}.jpg', d / f'clip{i}_{c}.jpg')
(d / 'brief.md').write_text('# Rater brief\n' + json.dumps(p['rater_brief'], ensure_ascii=False, indent=1) + '\n\n# Rubric\n' + json.dumps(p['rubric'], ensure_ascii=False, indent=1) +
  '\n\nEach clip is a contact sheet: 2 frames per second, left-to-right, top-to-bottom (7 per row), ~6.6 s. Output scores.csv in this folder: code,<rubric field names>,note.\n', encoding='utf-8')
print(t, len(codes))
