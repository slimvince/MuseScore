"""
Iteration 45 Cluster A diagnostic — Minor6 → HalfDim7 first-inversion (Gate Q)
Executes Steps 0–4 of the diagnostic protocol.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = ROOT / "tools" / "corpus"

print("=" * 100)
print("STEP 0 — Coverage Discrepancy Check")
print("=" * 100)

# Step 0A — bwv423 Gate M absence
print("\nStep 0A — bwv423 (Gate M target: m9 b2.0)")
fpath = CORPUS_DIR / "bwv423.ours.json"
m21path = CORPUS_DIR / "bwv423.music21.json"

data = json.loads(fpath.read_text(encoding='utf-8'))
m21 = json.loads(m21path.read_text(encoding='utf-8'))

found_ours = False
found_m21 = False

for r in data.get('regions', []):
    if r['measureNumber'] == 9 and abs(r['beat'] - 2.0) < 0.15:
        print(f"  ours: quality={r.get('quality')!r} rootPc={r.get('rootPitchClass')} "
              f"bassPc={r.get('bassPitchClass')} bassIsRoot={r.get('bassIsRoot')}")
        found_ours = True
        break

if not found_ours:
    print("  ours: NO REGION FOUND at m9 b2.0")

for r in m21.get('regions', []):
    if r['measureNumber'] == 9 and abs(r['beat'] - 2.0) < 0.15:
        print(f"  m21: quality={r.get('quality')!r} rootPc={r.get('rootPitchClass')}")
        found_m21 = True
        break

if not found_m21:
    print("  m21: NO REGION FOUND at m9 b2.0")

# Step 0B — Gate N absent cases
print("\nStep 0B — Gate N absent cases (checking 5 of 6 listed members)")
GATE_N = [
    ('tools/corpus/bwv123.6.ours.json',  7, 2.0),
    ('tools/corpus/bwv337.ours.json',    1, 2.0),
    ('tools/corpus/bwv392.ours.json',   11, 4.0),
    ('tools/corpus/bwv417.ours.json',    3, 2.0),
    ('tools/corpus/bwv425.ours.json',   22, 3.0),
]

for fpath, meas, beat in GATE_N:
    full_path = ROOT / fpath
    if not full_path.exists():
        stem = Path(fpath).stem.replace('.ours', '')
        print(f"  {stem}: FILE NOT FOUND")
        continue

    stem = Path(fpath).stem.replace('.ours', '')
    data = json.loads(full_path.read_text(encoding='utf-8'))
    found = False
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            print(f"  {stem:<12} m{meas} b{beat}: quality={r.get('quality')!r} "
                  f"rootPc={r.get('rootPitchClass')} bassPc={r.get('bassPitchClass')} "
                  f"bassIsRoot={r.get('bassIsRoot')}")
            found = True
            break

    if not found:
        print(f"  {stem:<12} m{meas} b{beat}: NO REGION FOUND")

print("\n" + "=" * 100)
print("STEP 1 — Confirm Quality Strings and Pitch-Class Equivalence")
print("=" * 100)

TARGETS = [
    ('tools/corpus/bwv259.ours.json',   8, 1.0, 'bwv259'),
    ('tools/corpus/bwv284.ours.json',   3, 3.0, 'bwv284'),
    ('tools/corpus/bwv335.ours.json',   8, 1.0, 'bwv335'),
    ('tools/corpus/bwv40.8.ours.json', 10, 1.0, 'bwv40.8'),
    ('tools/corpus/bwv407.ours.json',   7, 4.0, 'bwv407'),
    ('tools/corpus/bwv90.5.ours.json',  8, 2.0, 'bwv90.5'),
]

winner_qualities = set()
alt_qualities = set()
correct_alts_count = 0

for fpath, meas, beat, label in TARGETS:
    full_path = ROOT / fpath
    data = json.loads(full_path.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            wRootPc = r.get('rootPitchClass', -1)
            wBassPc = r.get('bassPitchClass', -1)
            target_rootPc = (wRootPc - 3 + 12) % 12
            winner_qualities.add(r.get('quality'))

            print(f"\n{label:<12} m={meas} b={beat}")
            print(f"  winner: quality={r.get('quality')!r} rootPc={wRootPc} "
                  f"bassPc={wBassPc} bassIsRoot={r.get('bassIsRoot')} "
                  f"score={r.get('chordScore'):.4f}")
            print(f"  (target alt: rootPc={target_rootPc} bassPc={wBassPc} bassIsRoot=False)")

            has_correct_alt = False
            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                flag = ""
                if (a.get('rootPitchClass') == target_rootPc and
                        a.get('bassPitchClass') == wBassPc):
                    flag = "  <-- CLUSTER-A CANDIDATE"
                    alt_qualities.add(a.get('quality'))
                    has_correct_alt = True
                print(f"  alt[{i}]: quality={a.get('quality')!r} "
                      f"rootPc={a.get('rootPitchClass')} "
                      f"bassPc={a.get('bassPitchClass')} "
                      f"bassIsRoot={a.get('bassIsRoot')} "
                      f"score={a.get('score'):.4f} "
                      f"margin={margin:.4f}{flag}")

            if has_correct_alt:
                correct_alts_count += 1
            break

print(f"\n--- Step 1 Summary ---")
print(f"Winner quality string(s): {sorted(winner_qualities)}")
print(f"Alt quality string(s): {sorted(alt_qualities)}")
print(f"Cases with correct alt in results[]: {correct_alts_count} / 6")

if correct_alts_count < 4:
    print(f"\n*** STOP *** Fewer than 4 of 6 cases have correct alt. Pattern may not be gate-addressable.")
    exit(0)

print("\n" + "=" * 100)
print("STEP 2 — Full Baroque Corpus Scan (Cluster A Pattern)")
print("=" * 100)

# Get exact quality strings
WINNER_QUALITY = list(winner_qualities)[0] if len(winner_qualities) == 1 else None
ALT_QUALITY    = list(alt_qualities)[0] if len(alt_qualities) == 1 else None

if not WINNER_QUALITY or not ALT_QUALITY:
    print(f"\nError: Multiple quality strings or missing. Winner={winner_qualities}, Alt={alt_qualities}")
    print("Using first found:")
    WINNER_QUALITY = sorted(winner_qualities)[0]
    ALT_QUALITY = sorted(alt_qualities)[0]

print(f"\nScanning with: WINNER_QUALITY={WINNER_QUALITY!r}, ALT_QUALITY={ALT_QUALITY!r}")

GENUINE = {
    ('bwv259',  8, 1.0),
    ('bwv284',  3, 3.0),
    ('bwv335',  8, 1.0),
    ('bwv40.8', 10, 1.0),
    ('bwv407',  7, 4.0),
    ('bwv90.5', 8, 2.0),
}

THRESHOLD = 0.65
matches = []

for fpath in sorted(CORPUS_DIR.glob('*.ours.json')):
    stem = fpath.stem.replace('.ours', '')
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r.get('quality') != WINNER_QUALITY:
            continue
        if not r.get('bassIsRoot', False):
            continue
        wRootPc = r.get('rootPitchClass', -1)
        wBassPc = r.get('bassPitchClass', -1)
        wScore  = r.get('chordScore', 0.0)
        target_rootPc = (wRootPc - 3 + 12) % 12
        meas = r.get('measureNumber', -1)
        beat = r.get('beat', -1.0)

        for a in r.get('alternatives', []):
            if (a.get('quality') == ALT_QUALITY and
                    a.get('bassPitchClass') == wBassPc and
                    a.get('rootPitchClass') == target_rootPc):
                margin = wScore - a.get('score', 0.0)
                if margin <= THRESHOLD:
                    is_genuine = (stem, meas, beat) in GENUINE
                    matches.append({
                        'stem': stem, 'meas': meas, 'beat': beat,
                        'wRootPc': wRootPc, 'wBassPc': wBassPc,
                        'altRootPc': target_rootPc,
                        'margin': margin,
                        'genuine': is_genuine,
                    })
                break

genuine_found = [x for x in matches if x['genuine']]
fp_list       = [x for x in matches if not x['genuine']]

print(f"\nCluster A scan (threshold ≤ {THRESHOLD}):")
print(f"  Genuine found: {len(genuine_found)} / {len(GENUINE)}")
print(f"  False positives: {len(fp_list)}")

print("\nFalse positives:")
if fp_list:
    for x in fp_list:
        print(f"  {x['stem']:<20} m={x['meas']:>3} b={x['beat']:>4.1f}  "
              f"wRoot={x['wRootPc']} wBass={x['wBassPc']} "
              f"altRoot={x['altRootPc']} margin={x['margin']:.4f}")
else:
    print("  (none)")

# Tighter thresholds
print("\nThreshold analysis:")
for t in [0.65, 0.50, 0.40, 0.30]:
    fp_t = [x for x in fp_list if x['margin'] <= t]
    gen_t = [x for x in genuine_found if x['margin'] <= t]
    print(f"  At threshold ≤ {t:4.2f}: genuine={len(gen_t)} FP={len(fp_t)}")

best_threshold = None
for t in [0.65, 0.50, 0.40, 0.30, 0.20, 0.10]:
    gen_t = [x for x in genuine_found if x['margin'] <= t]
    fp_t = [x for x in fp_list if x['margin'] <= t]
    if len(gen_t) >= 4 and len(fp_t) <= 2:
        best_threshold = t
        break

print(f"\nBest threshold (genuine ≥ 4, FP ≤ 2): {best_threshold}")

if len(fp_list) > 3:
    print(f"\n*** FP > 3 at threshold 0.65. Do not proceed to Jazz scan. ***")
    exit(0)

print("\n" + "=" * 100)
print("STEP 3 — Temporal Context for Cluster A Matches")
print("=" * 100)

TEMPORAL = ['nextRootPc', 'previousRootPc', 'previousQuality',
            'previousBassPc', 'bassIsStepwiseFromPrevious',
            'bassIsStepwiseToNext', 'consecutiveBassStepwiseCount',
            'regionMetricWeight']

print(f"\nTemporal context for all {len(matches)} Cluster A matches:")
for x in matches:
    fpath = CORPUS_DIR / f"{x['stem']}.ours.json"
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == x['meas'] and abs(r['beat'] - x['beat']) < 0.15:
            label = "GENUINE" if x['genuine'] else "FP"
            print(f"\n{label}  {x['stem']} m={x['meas']} b={x['beat']:.1f}  margin={x['margin']:.4f}")
            for f in TEMPORAL:
                val = r.get(f, 'MISSING')
                print(f"  {f:<35} {repr(val)}")
            break

print("\n" + "=" * 100)
print("STEP 4 — Cluster B Characterization (Power/Sus2)")
print("=" * 100)

CLUSTER_B = [
    ('tools/corpus/bwv227.1.ours.json', 11, 3.0, 'bwv227.1'),
    ('tools/corpus/bwv43.11.ours.json',  3, 2.0, 'bwv43.11'),
    ('tools/corpus/bwv361.ours.json',    5, 4.0, 'bwv361'),
]

b_winner_qualities = set()
b_alt_qualities = set()

for fpath, meas, beat, label in CLUSTER_B:
    full_path = ROOT / fpath
    if not full_path.exists():
        print(f"\n{label}: FILE NOT FOUND")
        continue

    data = json.loads(full_path.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            b_winner_qualities.add(r.get('quality'))
            print(f"\n{label}  m={meas} b={beat}")
            print(f"  winner: quality={r.get('quality')!r} rootPc={r.get('rootPitchClass')} "
                  f"bassPc={r.get('bassPitchClass')} bassIsRoot={r.get('bassIsRoot')} "
                  f"score={r.get('chordScore'):.4f}")
            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                b_alt_qualities.add(a.get('quality'))
                print(f"  alt[{i}]: quality={a.get('quality')!r} "
                      f"rootPc={a.get('rootPitchClass')} "
                      f"bassPc={a.get('bassPitchClass')} "
                      f"bassIsRoot={a.get('bassIsRoot')} "
                      f"score={a.get('score'):.4f} margin={margin:.4f}")
            break

print(f"\n--- Step 4 Summary ---")
print(f"Cluster B winner quality string(s): {sorted(b_winner_qualities)}")
print(f"Cluster B alt quality string(s): {sorted(b_alt_qualities)}")

print("\n" + "=" * 100)
print("DIAGNOSTIC COMPLETE")
print("=" * 100)
