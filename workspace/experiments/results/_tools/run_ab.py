"""Submit one frozen A/B test to FreeVideo, blind-coded. Usage: python -I run_ab.py T1 [--only CODEIDX...]
Token is read from the FreeVideo token file and never printed. Videos go to _local/<T>/videos (gitignored)."""
import base64, json, pathlib, secrets, sys, time, urllib.request, urllib.error, hashlib, datetime
ROOT = pathlib.Path(__file__).resolve().parents[2]          # .../workspace/experiments
BASE = 'http://127.0.0.1:8189/freevideo/agent/v1'
TOKEN = pathlib.Path('E:/FreeVideo/agent/token').read_text().strip()
OPEN = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def call(method, path, body=None, raw=False):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(BASE + path if path.startswith('/') and not path.startswith('/freevideo') else 'http://127.0.0.1:8189' + path,
                                 data=data, method=method, headers={'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/json'})
    try:
        with OPEN.open(req, timeout=120) as r:
            b = r.read()
            return b if raw else json.loads(b)
    except urllib.error.HTTPError as e:
        return {'http_error': e.code, **json.loads(e.read() or b'{}')}

def upload(p):
    p = pathlib.Path(p)
    return call('POST', '/media', {'name': p.name, 'data_base64': base64.b64encode(p.read_bytes()).decode()})

def main(test, media_by_arm, extra_seeds=()):
    plan = json.load(open(ROOT / 'results' / test / 'plan.json', encoding='utf-8'))
    P = plan['params']; out = ROOT / '_local' / test; (out / 'videos').mkdir(parents=True, exist_ok=True)
    keyf = out / 'key.json'
    if keyf.exists(): key = json.load(open(keyf))
    else:
        key = {f'{a}{s}': {'arm': a, 'seed': s, 'code': secrets.token_hex(3)} for a in 'AB' for s in P['seeds']}
        json.dump(key, open(keyf, 'w'), indent=1)
    for a in 'AB':
        for sd in extra_seeds:
            key.setdefault(f'{a}{sd}', {'arm': a, 'seed': sd, 'code': secrets.token_hex(3)})
    json.dump(key, open(keyf, 'w'), indent=1)
    jobsf = out / 'jobs.json'
    jobs = json.load(open(jobsf)) if jobsf.exists() else {}
    order = sorted(key, key=lambda k: key[k]['code'])        # randomised submission order
    for k in order:
        e = key[k]; code = e['code']
        if jobs.get(code, {}).get('status') == 'succeeded': continue
        spec = {'prompt': plan['prompts'][e['arm']]['prompt'], 'seconds': P['seconds'], 'aspect': P['aspect'],
                'megapixels': P['megapixels'], 'quality': P['quality'], 'seed': e['seed'],
                'label': f'{test} {code}', 'ref': f'{test}-{code}-{datetime.datetime.now():%Y%m%d%H%M}'}
        if media_by_arm.get(e['arm']): spec['media'] = media_by_arm[e['arm']]
        pl = call('POST', '/plan', {k2: v for k2, v in spec.items() if k2 not in ('label', 'ref')})
        g = pl.get('geometry', {})
        if (g.get('width'), g.get('height')) != tuple(P['expected_width_height']) or g.get('frames') != P['expected_frames']:
            print('PLAN MISMATCH', test, code, g, pl.get('error')); sys.exit(2)
        job = call('POST', '/jobs', spec)
        job = job.get('job', job)
        if 'id' not in job: print('SUBMIT FAIL', code, job); sys.exit(3)
        t0 = time.time()
        while job['status'] not in ('succeeded', 'failed', 'cancelled', 'interrupted'):
            job = call('GET', '/jobs/' + job['id'] + '?wait=25')['job']
        rec = {'job': job['id'], 'status': job['status'], 'seconds_wall': round(time.time() - t0), 'geometry': g, 'spec_seed': e['seed']}
        if job['status'] == 'succeeded':
            vb = call('GET', job['result']['video']['url'], raw=True)
            (out / 'videos' / f'{code}.mp4').write_bytes(vb); rec['sha256'] = hashlib.sha256(vb).hexdigest()
        else: rec['error'] = job.get('error')
        jobs[code] = rec; json.dump(jobs, open(jobsf, 'w'), indent=1); print(code, rec['status'], rec['seconds_wall'], flush=True)
