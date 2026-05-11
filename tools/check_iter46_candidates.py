#!/usr/bin/env python3
"""
Step 5 diagnostic: Check if Augmented and HalfDiminished inversion candidates
now appear in results[] for target cases.
"""

import json
from pathlib import Path

# Target cases from iteration prompt
TYPEB_TARGETS = [
    # (stem, meas, beat, expected_alt_rootPc, expected_alt_quality)
    ('bwv288', 11, 1.0,  0, 'Augmented'),   # C+/E — correct root P4 below E
    ('bwv309', 12, 3.0, 10, 'Augmented'),   # Bb+/D — correct root P4 below D
    ('bwv331',  2, 1.0,  0, 'Augmented'),   # C+/E
]

CLUSTER_A_TARGETS = [
    ('bwv259',   8, 1.0,  1, 'HalfDiminished'),  # C#ø7/E (rootPc=1)
    ('bwv284',   3, 3.0,  9, 'HalfDiminished'),  # Aø7/C  (rootPc=9)
    ('bwv335',   8, 1.0,  1, 'HalfDiminished'),  # C#ø7/E
    ('bwv40.8', 10, 1.0,  0, 'HalfDiminished'),  # Cø7/Eb (rootPc=0)
    ('bwv407',   7, 4.0, 11, 'HalfDiminished'),  # Bø7/D  (rootPc=11)
    ('bwv90.5',  8, 2.0, 11, 'HalfDiminished'),  # Bø7/D
]

CORPUS = Path('tools/corpus')

def check_targets():
    found_count = {'TYPEB': 0, 'CLUSTER_A': 0}

    for category, targets in [('TYPEB', TYPEB_TARGETS), ('CLUSTER_A', CLUSTER_A_TARGETS)]:
        print(f"\n{'='*80}")
        print(f"{category} Targets:")
        print(f"{'='*80}")

        for stem, meas, beat, exp_rootPc, exp_qual in targets:
            fpath = CORPUS / f'{stem}.ours.json'
            if not fpath.exists():
                print(f'{stem}: FILE MISSING')
                continue

            data = json.loads(fpath.read_text(encoding='utf-8'))
            for r in data.get('regions', []):
                if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
                    found = False
                    for i, a in enumerate(r.get('alternatives', [])):
                        if (a.get('quality') == exp_qual and
                                a.get('rootPitchClass') == exp_rootPc):
                            margin = r.get('chordScore', 0) - a.get('score', 0)
                            print(f'FOUND  {stem} m{meas} b{beat}: {exp_qual} rootPc={exp_rootPc}'
                                  f' at alt[{i}] margin={margin:.4f} '
                                  f'winner={r.get("quality")} rootPc={r.get("rootPitchClass")}')
                            found = True
                            found_count[category] += 1
                            break
                    if not found:
                        winner_q = r.get('quality')
                        print(f'ABSENT {stem} m{meas} b{beat}: {exp_qual} rootPc={exp_rootPc}'
                              f' — winner={winner_q} rootPc={r.get("rootPitchClass")}')
                    break

    print(f"\n{'='*80}")
    print(f"Summary:")
    print(f"  TYPE-B targets FOUND: {found_count['TYPEB']}/3")
    print(f"  Cluster A targets FOUND: {found_count['CLUSTER_A']}/6")
    print(f"  Total FOUND: {found_count['TYPEB'] + found_count['CLUSTER_A']}/9")
    print(f"{'='*80}\n")

    return found_count

if __name__ == '__main__':
    check_targets()
