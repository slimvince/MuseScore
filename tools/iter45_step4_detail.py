"""
Iteration 45 Step 4 — Cluster B Power/Sus2 characterization (detailed music21 reporting)
Runs exactly as specified: winner quality, alt quality strings, margins from .ours.json,
and what music21 reports from .music21.json files.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "tools" / "corpus"

CLUSTER_B = [
    ('bwv227.1', 11, 3.0),
    ('bwv43.11', 3, 2.0),
    ('bwv361', 5, 4.0),
]

print("=" * 100)
print("STEP 4 — Cluster B: Power/Sus2 Characterization")
print("=" * 100)
print()

for stem, meas, beat in CLUSTER_B:
    ours_path = CORPUS_DIR / f"{stem}.ours.json"
    m21_path = CORPUS_DIR / f"{stem}.music21.json"

    print("-" * 100)
    print(f"{stem}  m={meas} b={beat}")
    print("-" * 100)

    # Our analysis
    if not ours_path.exists():
        print(f"ERROR: {ours_path} not found")
        continue

    ours_data = json.loads(ours_path.read_text(encoding='utf-8'))
    ours_region = None

    for r in ours_data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            ours_region = r
            break

    if not ours_region:
        print(f"No region found in our analysis at m={meas} b={beat}")
    else:
        print(f"\nOUR ANALYSIS (.ours.json):")
        print(f"  Winner:")
        print(f"    quality={ours_region.get('quality')!r}")
        print(f"    rootPc={ours_region.get('rootPitchClass')}")
        print(f"    bassPc={ours_region.get('bassPitchClass')}")
        print(f"    bassIsRoot={ours_region.get('bassIsRoot')}")
        print(f"    score={ours_region.get('chordScore'):.4f}")

        alts = ours_region.get('alternatives', [])
        print(f"\n  Alternatives ({len(alts)} total):")
        for i, a in enumerate(alts):
            margin = ours_region.get('chordScore', 0.0) - a.get('score', 0.0)
            print(f"    alt[{i}]:")
            print(f"      quality={a.get('quality')!r}")
            print(f"      rootPc={a.get('rootPitchClass')}")
            print(f"      bassPc={a.get('bassPitchClass')}")
            print(f"      bassIsRoot={a.get('bassIsRoot')}")
            print(f"      score={a.get('score'):.4f}")
            print(f"      margin={margin:.4f}")

    # Music21 reference
    print(f"\nMUSIC21 REFERENCE (.music21.json):")
    if not m21_path.exists():
        print(f"  File not found: {m21_path}")
    else:
        m21_data = json.loads(m21_path.read_text(encoding='utf-8'))
        m21_region = None

        for r in m21_data.get('regions', []):
            if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
                m21_region = r
                break

        if not m21_region:
            print(f"  No region found at m={meas} b={beat}")
            # Show what regions exist nearby
            print(f"  Regions near m={meas} in music21:")
            nearby_count = 0
            for r in m21_data.get('regions', []):
                if r['measureNumber'] == meas:
                    nearby_count += 1
                    print(f"    m={r['measureNumber']} b={r['beat']:.1f}: "
                          f"quality={r.get('quality')!r} rootPc={r.get('rootPitchClass')}")
            if nearby_count == 0:
                print(f"    (no regions in m={meas})")
        else:
            print(f"  Region found at m={meas} b={beat}:")
            print(f"    quality={m21_region.get('quality')!r}")
            print(f"    rootPc={m21_region.get('rootPitchClass')}")
            print(f"    bassPc={m21_region.get('bassPitchClass')}")
            print(f"    bassIsRoot={m21_region.get('bassIsRoot')}")

    print()

print("=" * 100)
print("CLUSTER B SUMMARY")
print("=" * 100)
print()

# Collect all qualities
all_winner_qualities = set()
all_alt_qualities = set()
all_margins = []

for stem, meas, beat in CLUSTER_B:
    ours_path = CORPUS_DIR / f"{stem}.ours.json"
    if not ours_path.exists():
        continue

    ours_data = json.loads(ours_path.read_text(encoding='utf-8'))
    for r in ours_data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            all_winner_qualities.add(r.get('quality'))
            for a in r.get('alternatives', []):
                all_alt_qualities.add(a.get('quality'))
                margin = r.get('chordScore', 0.0) - a.get('score', 0.0)
                all_margins.append(margin)
            break

print(f"Winner quality string(s): {sorted(all_winner_qualities)}")
print(f"Alt quality strings: {sorted(all_alt_qualities)}")
print(f"Margin range: min={min(all_margins):.4f}, max={max(all_margins):.4f}")
print(f"All margins: {sorted(all_margins)}")
print()
print("Pattern analysis:")
if len(all_winner_qualities) == 1:
    print(f"  Winner quality is CONSISTENT: {list(all_winner_qualities)[0]!r}")
else:
    print(f"  Winner quality is VARIED: {all_winner_qualities}")
print(f"  Alt qualities are: {all_alt_qualities}")
print(f"  Tightest margin: {min(all_margins):.4f}")
