#!/usr/bin/env python3
"""Gate M diagnostic for Iteration 47"""

import json
from pathlib import Path

CORPUS = Path('C:\\s\\MS\\tools\\corpus')

GATE_M = [
    ('bwv187.7',  14, 2.0, 'bwv187.7'),
    ('bwv227.11', 10, 3.0, 'bwv227.11'),
    ('bwv278',     8, 2.0, 'bwv278'),
    ('bwv301',     2, 3.0, 'bwv301'),
    ('bwv302',     1, 4.0, 'bwv302'),
    ('bwv40.6',   14, 2.0, 'bwv40.6'),
    ('bwv85.6',    5, 1.0, 'bwv85.6'),
]

TEMPORAL = ['nextRootPc', 'previousRootPc', 'previousQuality',
            'previousBassPc', 'bassIsStepwiseFromPrevious',
            'bassIsStepwiseToNext', 'consecutiveBassStepwiseCount',
            'regionMetricWeight']

print('=' * 80)
print('STEP 4 — Gate M case details (margin=0.000)')
print('=' * 80)

print('Gate M cases (margin=0.000):')
for stem, meas, beat, label in GATE_M:
    fpath = CORPUS / f'{stem}.ours.json'
    try:
        data = json.loads(fpath.read_text(encoding='utf-8'))
    except Exception as e:
        print(f'ERROR reading {fpath}: {e}')
        continue

    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            print(f'\n{label}  m={meas} b={beat}')
            print(f'  winner: quality={r.get("quality")!r} '
                  f'rootPc={r.get("rootPitchClass")} '
                  f'bassPc={r.get("bassPitchClass")} '
                  f'bassIsRoot={r.get("bassIsRoot")} '
                  f'score={r.get("chordScore"):.4f}')
            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                print(f'  alt[{i}]: quality={a.get("quality")!r} '
                      f'rootPc={a.get("rootPitchClass")} '
                      f'bassPc={a.get("bassPitchClass")} '
                      f'bassIsRoot={a.get("bassIsRoot")} '
                      f'score={a.get("score"):.4f} margin={margin:.4f}')
            # Also print temporal fields
            for f in TEMPORAL:
                print(f'  {f}: {repr(r.get(f, "MISSING"))}')
            break

print('\n' + '=' * 80)
print('STEP 5 -- Gate M FP scan (exact tie <= 0.001)')
print('=' * 80)

GATE_M_GENUINE = {
    ('bwv187.7',  14, 2.0),
    ('bwv227.11', 10, 3.0),
    ('bwv278',     8, 2.0),
    ('bwv301',     2, 3.0),
    ('bwv302',     1, 4.0),
    ('bwv40.6',   14, 2.0),
    ('bwv85.6',    5, 1.0),
}

TIE_THRESHOLD = 0.001   # near-zero only

gate_m_matches = []
for fpath in sorted(CORPUS.glob('*.ours.json')):
    stem = fpath.stem.replace('.ours', '')
    try:
        data = json.loads(fpath.read_text(encoding='utf-8'))
    except:
        continue

    for r in data.get('regions', []):
        if r.get('quality') != 'Minor':
            continue
        if not r.get('bassIsRoot', False):
            continue
        wRootPc = r.get('rootPitchClass', -1)
        wBassPc = r.get('bassPitchClass', -1)
        wScore  = r.get('chordScore', 0.0)
        meas = r.get('measureNumber', -1)
        beat = r.get('beat', -1.0)

        for a in r.get('alternatives', []):
            if (a.get('quality') == 'Minor' and
                    a.get('rootPitchClass') == wRootPc and
                    a.get('bassPitchClass') != wBassPc):
                margin = wScore - a.get('score', 0.0)
                if abs(margin) <= TIE_THRESHOLD:
                    is_genuine = (stem, meas, beat) in GATE_M_GENUINE
                    gate_m_matches.append({
                        'stem': stem, 'meas': meas, 'beat': beat,
                        'wRootPc': wRootPc, 'wBassPc': wBassPc,
                        'altBassPc': a.get('bassPitchClass'),
                        'altBassIsRoot': a.get('bassIsRoot'),
                        'margin': margin,
                        'genuine': is_genuine,
                    })
                break

gm_genuine = [x for x in gate_m_matches if x['genuine']]
gm_fp      = [x for x in gate_m_matches if not x['genuine']]

print(f'\nGate M scan (exact tie <= 0.001):')
print(f'  Genuine: {len(gm_genuine)} / 7')
print(f'  FP: {len(gm_fp)}')
print('\nFP list:')
for x in gm_fp:
    print(f'  {x["stem"]:<20} m={x["meas"]:>3} b={x["beat"]:.1f} '
          f'wRoot={x["wRootPc"]} wBass={x["wBassPc"]} '
          f'altBass={x["altBassPc"]} margin={x["margin"]:.6f}')

print('\n' + '=' * 80)
print('Gate M diagnostic complete')
print('=' * 80)
