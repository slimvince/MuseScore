#!/usr/bin/env python3
"""Reconcile the 25 characterization items against actual three-way BIR=true count."""

import json
from pathlib import Path

CORPUS = Path('tools/corpus')
characterization_items = [
    ('bwv110.7', 2, 2.0),
    ('bwv184.5', 10, 3.0),
    ('bwv184.5', 13, 4.0),
    ('bwv187.7', 14, 2.0),
    ('bwv227.1', 11, 3.0),
    ('bwv227.11', 10, 3.0),
    ('bwv244.40', 8, 2.0),
    ('bwv259', 8, 1.0),
    ('bwv278', 8, 2.0),
    ('bwv293', 5, 3.0),
    ('bwv301', 2, 3.0),
    ('bwv302', 1, 4.0),
    ('bwv322', 15, 1.0),
    ('bwv335', 8, 1.0),
    ('bwv361', 5, 4.0),
    ('bwv40.6', 14, 2.0),
    ('bwv407', 7, 4.0),
    ('bwv43.11', 3, 2.0),
    ('bwv65.7', 8, 3.0),
    ('bwv78.7', 16, 1.0),
    ('bwv84.5', 5, 1.0),
    ('bwv85.6', 5, 1.0),
    ('bwv90.5', 8, 2.0),
    ('bwv90.5', 12, 2.0),
    ('bwv96.6', 2, 1.0),
]

# Check which characterization items are actually three-way genuine BIR=true
actual_three_way = []
non_three_way = []

for stem, m, b in characterization_items:
    fpath = CORPUS / f'{stem}.ours.json'
    try:
        data = json.loads(fpath.read_text(encoding='utf-8'))
        for r in data.get('regions', []):
            if r['measureNumber'] == m and abs(r['beat'] - b) < 0.15:
                # Check if this is three-way (has m21 and DCML info)
                m21_chord = r.get('m21_chord')
                dcml_chord = r.get('dcml_chord')
                ours_bassIsRoot = r.get('bassIsRoot')
                ours_quality = r.get('quality')
                ours_root = r.get('rootPitchClass')
                ours_bass = r.get('bassPitchClass')

                # Three-way means all three have values
                is_three_way = bool(m21_chord and dcml_chord)

                if is_three_way and ours_bassIsRoot == True:
                    actual_three_way.append({
                        'stem': stem, 'm': m, 'b': b,
                        'quality': ours_quality,
                        'root': ours_root,
                        'bass': ours_bass,
                        'bassIsRoot': ours_bassIsRoot,
                        'm21': m21_chord,
                        'dcml': dcml_chord,
                    })
                else:
                    status = []
                    if not is_three_way:
                        status.append('NOT-THREE-WAY')
                    if ours_bassIsRoot == False:
                        status.append('BIR=FALSE')
                    non_three_way.append({
                        'stem': stem, 'm': m, 'b': b,
                        'status': ', '.join(status) or 'OTHER',
                        'bassIsRoot': ours_bassIsRoot,
                        'has_m21': bool(m21_chord),
                        'has_dcml': bool(dcml_chord),
                    })
                break
    except Exception as e:
        non_three_way.append({
            'stem': stem, 'm': m, 'b': b,
            'status': f'ERROR: {e}',
        })

print(f"Characterization script total: {len(characterization_items)}")
print(f"Three-way genuine BIR=true: {len(actual_three_way)}")
print(f"Non-three-way or BIR=false: {len(non_three_way)}")
print()

if non_three_way:
    print("=" * 80)
    print(f"DISCREPANCY: 4 cases in characterization are NOT three-way genuine BIR=true")
    print("=" * 80)
    for i, case in enumerate(non_three_way, 1):
        print(f"\n{i}. {case['stem']:12s} m{case['m']:2d} b{case['b']:.1f}")
        print(f"   Status: {case['status']}")
        if 'bassIsRoot' in case:
            print(f"   bassIsRoot: {case['bassIsRoot']}")
        if 'has_m21' in case:
            print(f"   Has m21: {case['has_m21']}, Has DCML: {case['has_dcml']}")
