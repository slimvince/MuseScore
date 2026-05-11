#!/usr/bin/env python3
"""Step 3 — Inspect worst-case under-segmented chorale"""

import json
from pathlib import Path

STEM = 'bwv328'
CORPUS = Path('C:\\s\\MS\\tools\\corpus')

ours = json.loads((CORPUS / f'{STEM}.ours.json').read_text(encoding='utf-8'))
m21  = json.loads((CORPUS / f'{STEM}.music21.json').read_text(encoding='utf-8'))

print(f'music21 regions ({len(m21["regions"])}):')
for r in m21.get('regions', []):
    print(f'  m={r.get("measureNumber"):>3} b={r.get("beat"):.2f}  '
          f'quality={r.get("quality")!r}  rootPc={r.get("rootPitchClass")}')

print(f'\nours regions ({len(ours["regions"])}):')
for r in ours.get('regions', []):
    print(f'  m={r.get("measureNumber"):>3} b={r.get("beat"):.2f}  '
          f'quality={r.get("quality")!r}  rootPc={r.get("rootPitchClass")}')

# Find missing boundaries
print(f'\nMissing boundaries (in music21 but not in ours):')
ours_set = set()
for r in ours.get('regions', []):
    m = r.get('measureNumber')
    b = round(r.get('beat', 0.0), 2)
    ours_set.add((m, b))

missing = []
for r in m21.get('regions', []):
    m = r.get('measureNumber')
    b = round(r.get('beat', 0.0), 2)
    if (m, b) not in ours_set:
        missing.append((m, b, r.get('quality'), r.get('rootPitchClass')))

print(f'Total missing: {len(missing)}')
for m, b, q, pc in missing[:30]:
    print(f'  m={m:>3} b={b:.2f}  quality={q!r}  rootPc={pc}')

if len(missing) > 30:
    print(f'  ... and {len(missing) - 30} more')

# Analyze beat pattern
beat_pattern = {}
for m, b, q, pc in missing:
    beat_pattern[b] = beat_pattern.get(b, 0) + 1

print(f'\nMissing boundaries by beat position:')
for beat in sorted(beat_pattern.keys()):
    print(f'  Beat {beat}: {beat_pattern[beat]} missing')
