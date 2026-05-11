"""
Iteration 45 Step 4 — Cluster B characterization (Power/Sus2)
Prints winner and alternatives for 3 Cluster B cases.
Also includes music21 ground-truth quality from .music21.json files.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "tools" / "corpus"

CLUSTER_B = [
    ('tools/corpus/bwv227.1.ours.json', 11, 3.0, 'bwv227.1'),
    ('tools/corpus/bwv43.11.ours.json',  3, 2.0, 'bwv43.11'),
    ('tools/corpus/bwv361.ours.json',    5, 4.0, 'bwv361'),
]

print("=" * 100)
print("STEP 4 — Cluster B Characterization (Power/Sus2)")
print("=" * 100)

winner_qualities = set()
alt_qualities = set()

for fpath, meas, beat, label in CLUSTER_B:
    full_path = ROOT / fpath
    m21_path = CORPUS_DIR / f"{label}.music21.json"

    if not full_path.exists():
        print(f"\n{label}: FILE NOT FOUND")
        continue

    data = json.loads(full_path.read_text(encoding='utf-8'))
    found = False

    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            winner_qualities.add(r.get('quality'))
            print(f"\n{label}  m={meas} b={beat}")
            print(f"  winner: quality={r.get('quality')!r} rootPc={r.get('rootPitchClass')} "
                  f"bassPc={r.get('bassPitchClass')} bassIsRoot={r.get('bassIsRoot')} "
                  f"score={r.get('chordScore'):.4f}")

            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                alt_qualities.add(a.get('quality'))
                print(f"  alt[{i}]: quality={a.get('quality')!r} "
                      f"rootPc={a.get('rootPitchClass')} "
                      f"bassPc={a.get('bassPitchClass')} "
                      f"bassIsRoot={a.get('bassIsRoot')} "
                      f"score={a.get('score'):.4f} margin={margin:.4f}")

            # Check music21 ground truth
            m21_quality = None
            if m21_path.exists():
                m21_data = json.loads(m21_path.read_text(encoding='utf-8'))
                for m21_r in m21_data.get('regions', []):
                    if m21_r['measureNumber'] == meas and abs(m21_r['beat'] - beat) < 0.15:
                        m21_quality = m21_r.get('quality')
                        break

            if m21_quality is not None:
                print(f"  music21 ground-truth quality: {m21_quality!r}")
            else:
                print(f"  music21 ground-truth: NOT FOUND at this location")

            found = True
            break

    if not found:
        print(f"\n{label}  m={meas} b={beat}: NO REGION FOUND in our analysis")
        if m21_path.exists():
            print(f"  (checking music21 for context...)")
            m21_data = json.loads(m21_path.read_text(encoding='utf-8'))
            for m21_r in m21_data.get('regions', []):
                if m21_r['measureNumber'] == meas and abs(m21_r['beat'] - beat) < 0.15:
                    print(f"    m21 at this location: quality={m21_r.get('quality')!r} rootPc={m21_r.get('rootPitchClass')}")

print("\n" + "=" * 100)
print("CLUSTER B SUMMARY")
print("=" * 100)
print(f"Winner quality string(s): {sorted(winner_qualities)}")
print(f"Alt quality string(s): {sorted(alt_qualities)}")
print()

# Analyze pattern consistency
print("Pattern analysis:")
if len(winner_qualities) == 1:
    print(f"  Winner quality: CONSISTENT (all {list(winner_qualities)[0]!r})")
else:
    print(f"  Winner quality: VARIED {winner_qualities}")

if len(alt_qualities) <= 2:
    print(f"  Alt quality: Relatively consistent {sorted(alt_qualities)}")
else:
    print(f"  Alt quality: VARIED {sorted(alt_qualities)}")
