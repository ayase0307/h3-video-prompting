"""T3: per-frame L* mean/std; T4: card->palette dE76 + meanLab. Usage: python measure_color.py T3|T4 (writes _local/<T>/color.csv)"""
import csv, pathlib, re, subprocess, sys, statistics
REPO = pathlib.Path(__file__).resolve().parents[4]; sys.path.insert(0, str(REPO / 'scripts'))
import color_qa
T = sys.argv[1]; D = REPO / 'workspace/experiments/_local' / T
CARD = '0B1118,1E2A38,3B5068,6B8299,E6F2FF'
rows = []
for mp4 in sorted((D / 'videos').glob('*.mp4')):
    r = {'code': mp4.stem}
    px = color_qa.pixels(str(mp4)); n = 160 * 90; Ls = []
    for i in range(0, len(px), n):
        fr = px[i:i + n]; Ls.append(statistics.fmean(color_qa.to_lab(p)[0] for p in fr[::7]))
    r['L_mean'] = round(statistics.fmean(Ls), 2); r['L_std'] = round(statistics.pstdev(Ls), 2)
    if T == 'T4':
        o = subprocess.run([sys.executable, '-I', str(REPO / 'scripts/color_qa.py'), str(mp4), '--ref', CARD], capture_output=True, text=True).stdout
        r['card_dE76'] = float(re.search(r'palette dE76 ([0-9.]+)', o).group(1))
        m = re.search(r'meanLab \(([^)]*)\)', o); r['meanLab'] = m.group(1)
    rows.append(r)
with open(D / 'color.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
print(open(D / 'color.csv', encoding='utf-8').read())
