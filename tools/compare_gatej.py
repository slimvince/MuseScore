"""Compare post-Gate-J corpus against baseline to list all improvements and regressions."""
from __future__ import annotations
import sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import compare_analyses as cmp
import dcml_parser as dcml

CORPUS_DIR = ROOT / 'tools' / 'corpus'
WIR_DIR    = ROOT / 'tools' / 'dcml' / 'when_in_rome'

with open(str(ROOT / 'tools' / 'bir_true_baseline.json')) as f:
    base_true = json.load(f)
with open(str(ROOT / 'tools' / 'bir_false_baseline.json')) as f:
    base_false = json.load(f)

ours_files = sorted(CORPUS_DIR.glob('*.ours.json'))
post_true  = {}
post_false = {}

for ours_path in ours_files:
    stem = ours_path.stem.replace('.ours', '')
    music21_path = CORPUS_DIR / f'{stem}.music21.json'
    if not music21_path.exists():
        continue
    try:
        _, ours_regions = cmp.load_analysis(ours_path)
        _, m21_regions  = cmp.load_analysis(music21_path)
    except Exception:
        continue
    if not ours_regions:
        continue
    aligned = cmp.align_regions(ours_regions, m21_regions)
    wir_path = dcml.find_wir_file(str(WIR_DIR), stem)
    wir_regions = []
    if wir_path:
        try:
            wir_regions = dcml.parse_rntxt_file(wir_path)
        except Exception:
            pass
    wir_aligned = cmp.align_dcml_regions(ours_regions, wir_regions) if wir_regions else [None]*len(ours_regions)
    for i, (our_r, their_r) in enumerate(aligned):
        result = cmp.classify(our_r, their_r)
        if result.category != 'chord_disagree':
            continue
        if not wir_regions or i >= len(wir_aligned):
            continue
        wir_r = wir_aligned[i]
        wir_pc = wir_r.root_pc if wir_r is not None else None
        cat = cmp.three_way_classify(our_r.root_pc, their_r.root_pc if their_r else None, wir_pc)
        if cat != 'music21_dcml_agree':
            continue
        key = f'{stem}|{our_r.measure_number}|{our_r.beat:.1f}'
        alts = [a.get('chordSymbol', '?') for a in (our_r.alternatives or [])[:2]]
        margin = getattr(our_r, 'chord_score_margin', '?')
        entry = {
            'stem': stem, 'm': our_r.measure_number, 'b': our_r.beat,
            'winner': our_r.chord_symbol, 'key': our_r.key,
            'margin': margin, 'alts': alts,
        }
        if our_r.bass_is_root:
            post_true[key] = entry
        else:
            post_false[key] = entry

print(f'Post Gate J: BIR=true={len(post_true)}, BIR=false={len(post_false)}')
print()

improved        = [k for k in base_true  if k not in post_true]
new_regressions = [k for k in post_false if k not in base_false]

print(f'=== BIR=true improvements (Gate J fired correctly): {len(improved)} ===')
for k in sorted(improved):
    e = base_true[k]
    # find what it became (alt it flipped to)
    if k in post_false:
        winner_now = post_false[k]['winner']
    else:
        winner_now = '(resolved)'
    alts_str = ', '.join(e['alts'][:2])
    print(f'  {e["stem"]:16s} m={e["m"]:3d} b={e["b"]}  winner={e["winner"]:15s}  alt=[{alts_str}]  '
          f'margin={e["margin"]}  key={e["key"]}  now={winner_now}')

print()
print(f'=== New BIR=false regressions (Gate J fired incorrectly): {len(new_regressions)} ===')
for k in sorted(new_regressions):
    e = post_false[k]
    # was it previously correct?
    if k in base_true:
        was = base_true[k]['winner']
    else:
        was = '(was correct)'
    alts_str = ', '.join(e['alts'][:2])
    print(f'  {e["stem"]:16s} m={e["m"]:3d} b={e["b"]}  winner={e["winner"]:15s}  alt=[{alts_str}]  '
          f'margin={e["margin"]}  key={e["key"]}')

print()
print(f'Net: +{len(improved)} improvements, -{len(new_regressions)} regressions')
