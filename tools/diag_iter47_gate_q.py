#!/usr/bin/env python3
"""Gate Q diagnostic for Iteration 47"""

import json
from pathlib import Path

CORPUS = Path('C:\\s\\MS\\tools\\corpus')

CLUSTER_A = [
    ('bwv259',  8, 1.0, 'bwv259'),
    ('bwv335',  8, 1.0, 'bwv335'),
    ('bwv78.7', 16, 1.0, 'bwv78.7'),
    ('bwv84.5',  5, 1.0, 'bwv84.5'),
    ('bwv90.5',  8, 2.0, 'bwv90.5-a'),
    ('bwv90.5', 12, 2.0, 'bwv90.5-b'),
    ('bwv96.6',  2, 1.0, 'bwv96.6'),
]

print('=' * 80)
print('STEP 1 — Quality strings and alt presence for Gate Q cases')
print('=' * 80)

winner_qualities = set()
alt_qualities = set()
alts_in_results = 0

for stem, meas, beat, label in CLUSTER_A:
    fpath = CORPUS / f'{stem}.ours.json'
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            wRootPc = r.get('rootPitchClass', -1)
            wBassPc = r.get('bassPitchClass', -1)
            target_rootPc = (wRootPc - 3 + 12) % 12
            print(f'\n{label}  m={meas} b={beat}')
            print(f'  winner: quality={r.get("quality")!r} rootPc={wRootPc} '
                  f'bassPc={wBassPc} bassIsRoot={r.get("bassIsRoot")} '
                  f'score={r.get("chordScore"):.4f}')
            print(f'  (target alt: HalfDim rootPc={target_rootPc} bassPc={wBassPc})')

            winner_qualities.add(r.get("quality"))

            found_target = False
            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                flag = ''
                if (a.get('rootPitchClass') == target_rootPc and
                        a.get('bassPitchClass') == wBassPc):
                    flag = '  <- GATE Q TARGET'
                    alt_qualities.add(a.get("quality"))
                    found_target = True
                print(f'  alt[{i}]: quality={a.get("quality")!r} '
                      f'rootPc={a.get("rootPitchClass")} '
                      f'bassPc={a.get("bassPitchClass")} '
                      f'bassIsRoot={a.get("bassIsRoot")} '
                      f'score={a.get("score"):.4f} margin={margin:.4f}{flag}')
            if found_target:
                alts_in_results += 1
            break

print('\n' + '=' * 80)
print('STEP 1 SUMMARY')
print('=' * 80)
print(f'Winner quality strings: {sorted(winner_qualities)}')
print(f'HalfDim quality strings: {sorted(alt_qualities)}')
print(f'Cases with HalfDim alt in results[]: {alts_in_results} / 7')
print(f'Alt.bassIsRoot consistency: check details above')

# STEP 2 — FP scan for Gate Q
print('\n' + '=' * 80)
print('STEP 2 — Full Baroque corpus FP scan for Gate Q')
print('=' * 80)

WINNER_QUALITY = list(winner_qualities)[0] if winner_qualities else None
ALT_QUALITY = list(alt_qualities)[0] if alt_qualities else None

print(f'Using WINNER_QUALITY={WINNER_QUALITY!r}, ALT_QUALITY={ALT_QUALITY!r}')

GENUINE = {
    ('bwv259',  8, 1.0),
    ('bwv335',  8, 1.0),
    ('bwv78.7', 16, 1.0),
    ('bwv84.5',  5, 1.0),
    ('bwv90.5',  8, 2.0),
    ('bwv90.5', 12, 2.0),
    ('bwv96.6',  2, 1.0),
}

matches = []
for fpath in sorted(CORPUS.glob('*.ours.json')):
    stem = fpath.stem.replace('.ours', '')
    try:
        data = json.loads(fpath.read_text(encoding='utf-8'))
    except Exception as e:
        print(f'Warning: failed to read {fpath}: {e}')
        continue

    for r in data.get('regions', []):
        if r.get('quality') != WINNER_QUALITY:
            continue
        if not r.get('bassIsRoot', False):
            continue
        wRootPc = r.get('rootPitchClass', -1)
        wBassPc = r.get('bassPitchClass', -1)
        wScore  = r.get('chordScore', 0.0)
        target  = (wRootPc - 3 + 12) % 12
        meas = r.get('measureNumber', -1)
        beat = r.get('beat', -1.0)

        for a in r.get('alternatives', []):
            if (a.get('quality') == ALT_QUALITY and
                    a.get('bassPitchClass') == wBassPc and
                    a.get('rootPitchClass') == target):
                margin = wScore - a.get('score', 0.0)
                if margin <= 0.50:
                    is_genuine = (stem, meas, beat) in GENUINE
                    matches.append({
                        'stem': stem, 'meas': meas, 'beat': beat,
                        'wRootPc': wRootPc, 'wBassPc': wBassPc,
                        'margin': margin, 'genuine': is_genuine,
                    })
                break

genuine_found = [x for x in matches if x['genuine']]
fp_list       = [x for x in matches if not x['genuine']]

print(f'\nGate Q scan (<= 0.50):')
print(f'  Genuine: {len(genuine_found)} / {len(GENUINE)}')
print(f'  FP: {len(fp_list)}')
print('\nFP list:')
for x in fp_list:
    print(f'  {x["stem"]:<20} m={x["meas"]:>3} b={x["beat"]:.1f} '
          f'margin={x["margin"]:.4f}')

thresholds = [0.35, 0.20, 0.10]
best_threshold = None
for t in thresholds:
    fp_t  = [x for x in fp_list       if x['margin'] <= t]
    gen_t = [x for x in genuine_found if x['margin'] <= t]
    print(f'\nAt <= {t}: genuine={len(gen_t)} FP={len(fp_t)}')
    if len(gen_t) >= 5 and len(fp_t) <= 2:
        if best_threshold is None:
            best_threshold = t

print(f'\nBest threshold (genuine >= 5, FP <= 2): {best_threshold or "none"}')

# STEP 3 — Temporal context
print('\n' + '=' * 80)
print('STEP 3 — Temporal context for Gate Q matches')
print('=' * 80)

TEMPORAL = ['nextRootPc', 'previousRootPc', 'previousQuality',
            'previousBassPc', 'bassIsStepwiseFromPrevious',
            'bassIsStepwiseToNext', 'consecutiveBassStepwiseCount',
            'regionMetricWeight']

print('\nTemporal context — Gate Q matches:')
for x in matches:
    fpath = CORPUS / f'{x["stem"]}.ours.json'
    try:
        data = json.loads(fpath.read_text(encoding='utf-8'))
    except:
        continue

    for r in data.get('regions', []):
        if r['measureNumber'] == x['meas'] and abs(r['beat'] - x['beat']) < 0.15:
            label = 'GENUINE' if x['genuine'] else 'FP'
            print(f'\n{label}  {x["stem"]} m={x["meas"]} b={x["beat"]:.1f}  '
                  f'margin={x["margin"]:.4f}')
            for f in TEMPORAL:
                print(f'  {f}: {repr(r.get(f, "MISSING"))}')
            break

print('\n' + '=' * 80)
print('STEP 3 — Temporal analysis complete')
print('=' * 80)
