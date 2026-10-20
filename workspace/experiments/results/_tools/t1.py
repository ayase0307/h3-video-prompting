import sys, run_ab
r = run_ab.upload(run_ab.ROOT / '_local/chars/t1_first_frame.png'); print(r, flush=True)
f = r.get('file') or r.get('path') or r.get('name')
run_ab.main('T1', {'A': {'first': f}, 'B': {'first': f}})
