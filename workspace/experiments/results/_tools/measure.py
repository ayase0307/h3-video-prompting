"""Objective metrics per coded clip. Usage: python measure.py T1  -> _local/<T>/metrics.csv + thumbs/<code>.jpg"""
import csv, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = sys.argv[1]; D = ROOT / '_local' / T; (D / 'thumbs').mkdir(exist_ok=True)

def ff(*a):
    return subprocess.run(['ffmpeg', '-hide_banner', '-nostats', *a], capture_output=True, text=True, encoding='utf-8', errors='replace').stderr

def cuts(mp4, thr):
    o = ff('-i', str(mp4), '-vf', f"select='gt(scene,{thr})',showinfo", '-f', 'null', '-')
    return [round(float(x), 2) for x in re.findall(r'pts_time:([0-9.]+)', o)]

def settle(mp4):
    o = ff('-sseof', '-1', '-i', str(mp4), '-vf', 'tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG', '-f', 'null', '-')
    v = [float(x) for x in re.findall(r'YAVG=([0-9.]+)', o)]
    return round(sum(v) / len(v), 3) if v else ''

rows = []
for mp4 in sorted((D / 'videos').glob('*.mp4')):
    c = mp4.stem
    ff('-y', '-i', str(mp4), '-vf', 'fps=2,scale=272:-2,tile=7x2', '-frames:v', '1', '-q:v', '4', str(D / 'thumbs' / f'{c}.jpg'))
    r = {'code': c, 'cuts_0.2': cuts(mp4, .2), 'cuts_0.3': cuts(mp4, .3), 'cuts_0.4': cuts(mp4, .4), 'end_residual_yavg': settle(mp4)}
    if T == 'T2':
        hit = [t for t in (2.2, 4.4) if any(abs(x - t) <= .25 for x in r['cuts_0.3'])]
        r['matched'] = len(hit); r['spurious'] = len([x for x in r['cuts_0.3'] if not any(abs(x - t) <= .25 for t in (2.2, 4.4))])
    rows.append(r)
keys = sorted({k for r in rows for k in r}, key=lambda k: (k != 'code', k))
with open(D / 'metrics.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, keys); w.writeheader(); w.writerows(rows)
print(open(D / 'metrics.csv', encoding='utf-8').read())
