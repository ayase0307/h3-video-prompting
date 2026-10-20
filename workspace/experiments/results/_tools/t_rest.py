import run_ab
for t in ('T2', 'T3', 'T4'):
    run_ab.main(t, {})
C = run_ab.ROOT / '_local/chars'
ff = run_ab.upload(C / 't6_first_frame.png')['file']
face = run_ab.upload(C / 't6_face_cell.png')['file']
body = run_ab.upload(C / 't6_fullbody_cell.png')['file']
run_ab.main('T6', {'A': {'first': ff}, 'B': {'references': [{'file': face}, {'file': body}]}})
