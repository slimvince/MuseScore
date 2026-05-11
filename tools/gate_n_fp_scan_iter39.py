#!/usr/bin/env python3
"""
gate_n_fp_scan_iter39.py — False-positive scan for Gate N (Major root-pos → Minor first-inversion).

Gate N structural pattern:
  - winner: quality=Major, bassIsRoot=True
  - alt: quality=Minor, bassPc == winner.bassPc
  - interval: (bassPc - alt.rootPc + 12) % 12 == 3  (bass is minor-third of alt = I3 inversion)
  - margin: winner.score - alt.score <= THRESHOLD

Genuine 6 targets (from enumerate_near_agree_iter38 DCML-confirmed):
  bwv123.6, bwv322, bwv337, bwv392, bwv417, bwv425

Anomalies excluded (negative margin, D not in F#m):
  bwv245.14, bwv335

Reports all matching regions split into GENUINE vs FP.
"""
import sys, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

_ROOT = Path('C:/s/MS')
_CORPUS = _ROOT / 'tools' / 'corpus'

GENUINE = {
    ('bwv123.6',  7,  2.0),
    ('bwv322',    1,  3.0),
    ('bwv337',    1,  2.0),
    ('bwv392',   11,  4.0),
    ('bwv417',    3,  2.0),
    ('bwv425',   22,  3.0),
}

THRESHOLD = 0.45  # starting generous; Gate I uses 0.45

def norm_quality(q):
    return q.lower() if q else ''

def scan(threshold):
    genuine = []
    fps = []

    for ours_path in sorted(_CORPUS.glob('*.ours.json')):
        stem = ours_path.stem.replace('.ours', '')
        data = json.loads(ours_path.read_text(encoding='utf-8'))
        for region in data.get('regions', []):
            winner_q    = region.get('quality', '')
            winner_bir  = region.get('bassIsRoot', False)
            winner_rpc  = region.get('rootPitchClass', -1)
            winner_bpc  = region.get('bassPitchClass', -1)
            winner_scr  = region.get('chordScore', 0.0)
            measure     = region.get('measureNumber', 0)
            beat        = region.get('beat', 0.0)

            if winner_q != 'Major' or not winner_bir:
                continue

            for alt in region.get('alternatives', []):
                alt_q   = alt.get('quality', '')
                alt_rpc = alt.get('rootPitchClass', -1)
                alt_bpc = alt.get('bassPitchClass', -1)
                alt_scr = alt.get('score', 0.0)

                if alt_q != 'Minor':
                    continue
                if alt_bpc != winner_bpc:
                    continue
                # (bassPc - altRootPc + 12) % 12 == 3 — minor-third inversion
                if (winner_bpc - alt_rpc + 12) % 12 != 3:
                    continue

                margin = winner_scr - alt_scr
                if margin > threshold:
                    continue

                case = {
                    'stem': stem, 'measure': measure, 'beat': beat,
                    'winner_rpc': winner_rpc, 'winner_bpc': winner_bpc,
                    'alt_rpc': alt_rpc, 'alt_bpc': alt_bpc,
                    'winner_scr': winner_scr, 'alt_scr': alt_scr,
                    'margin': margin,
                }
                key = (stem, measure, beat)
                if key in GENUINE:
                    genuine.append(case)
                else:
                    fps.append(case)
                break  # only check first matching alt per region

    return genuine, fps

genuine, fps = scan(THRESHOLD)

print(f'Gate N FP scan  (threshold={THRESHOLD})')
print(f'Pattern: winner=Major+bassIsRoot, alt=Minor, (bassPc-altRootPc)%12==3')
print()
print(f'GENUINE hits ({len(genuine)}/6):')
for c in genuine:
    print(f"  {c['stem']:<14} m{c['measure']:>3} b{c['beat']:>4.1f}  "
          f"wRpc={c['winner_rpc']:>2} bPc={c['winner_bpc']:>2} "
          f"aRpc={c['alt_rpc']:>2} margin={c['margin']:>+.3f}")
print()
print(f'FALSE POSITIVES ({len(fps)}):')
for c in fps:
    print(f"  {c['stem']:<14} m{c['measure']:>3} b{c['beat']:>4.1f}  "
          f"wRpc={c['winner_rpc']:>2} bPc={c['winner_bpc']:>2} "
          f"aRpc={c['alt_rpc']:>2} margin={c['margin']:>+.3f}")
if not fps:
    print('  (none)')
print()

# Also try tighter threshold
for thr in [0.30, 0.35]:
    g2, fp2 = scan(thr)
    print(f'At threshold={thr}: genuine={len(g2)}/6, FP={len(fp2)}')
