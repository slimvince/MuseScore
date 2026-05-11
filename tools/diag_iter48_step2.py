#!/usr/bin/env python3
"""Step 2 — Region count comparison (Iteration 48)"""

import json
from pathlib import Path

CORPUS = Path('C:\\s\\MS\\tools\\corpus')

count_diffs = []
for ours_path in sorted(CORPUS.glob('*.ours.json')):
    stem = ours_path.stem.replace('.ours', '')
    m21_path = CORPUS / f'{stem}.music21.json'
    if not m21_path.exists():
        continue
    try:
        ours = json.loads(ours_path.read_text(encoding='utf-8'))
        m21  = json.loads(m21_path.read_text(encoding='utf-8'))
    except:
        continue

    n_ours = len(ours.get('regions', []))
    n_m21  = len(m21.get('regions', []))
    diff   = n_ours - n_m21
    count_diffs.append((stem, n_ours, n_m21, diff))

count_diffs.sort(key=lambda x: x[3])   # most under-segmented first

print('Most under-segmented (ours << music21):')
for stem, no, nm, d in count_diffs[:20]:
    print(f'  {stem:<20} ours={no:>3} m21={nm:>3} diff={d:>+4}')

print('\nMost over-segmented (ours >> music21):')
for stem, no, nm, d in reversed(count_diffs[-20:]):
    print(f'  {stem:<20} ours={no:>3} m21={nm:>3} diff={d:>+4}')

under = sum(1 for *_, d in count_diffs if d < -2)
over  = sum(1 for *_, d in count_diffs if d >  2)
exact = sum(1 for *_, d in count_diffs if abs(d) <= 2)
print(f'\nSummary: under-segmented (diff < -2): {under}')
print(f'         over-segmented  (diff >  2): {over}')
print(f'         close match     (|diff| <= 2): {exact}')
mean_diff = sum(d for *_, d in count_diffs) / len(count_diffs) if count_diffs else 0.0
print(f'         mean diff: {mean_diff:+.2f}')
