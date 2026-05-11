# Iteration 45: Cluster A diagnostic — Minor6 → HalfDim7 first-inversion (Gate Q)

## Standing rule — no symbol inference

**No chord symbol string parsing of any kind. No Roman numeral inference.
Use only structured fields (quality, rootPc, bassPc, bassIsRoot, score, extensions).**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=32, BIR=false=177.

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.

---

## Background

Iter 45 follows the genuine-32 re-characterization (tools/diag_genuine32_characterize.py).
17 UNCHARACTERIZED cases were identified. Cluster A (6 cases) is the highest-leverage
target: our winner is a Minor6 chord in root-position (bassIsRoot=true), and the
correct ground-truth reading is a HalfDiminished7 chord in first inversion at the
same bass note.

This is a well-known pitch-class identity:
  Xm6 = Yø7/X   where Y.rootPc = (X.rootPc − 3 + 12) % 12

Example: Dm6 {D, F, A, B} = Bø7/D {B, D, F, A}. The same four pitch classes;
our analyzer picks root D (bassIsRoot=true), the correct reading picks root B
(Bø7 in first inversion at bass D, bassIsRoot=false).

Cluster A cases (from diag_genuine32_characterize.py):
  bwv259  m8  b1: Em6  → ?/E    margin 0.38
  bwv284  m3  b3: Cm6  → ?/C    margin 0.06
  bwv335  m8  b1: Em6  → C#m7/E margin 0.62
  bwv40.8 m10 b1: Ebm6 → ?/Eb   margin 0.11
  bwv407  m7  b4: Dm6  → Bm7b5/D margin 0.00
  bwv90.5 m8  b2: Dm6  → ?/D    margin 0.23

---

## Step 0 — Coverage discrepancy check (brief)

Two anomalies were found in the genuine-32 coverage vs known gate sets.
Check both before the main diagnostic.

**A — Gate M: bwv423 absent**

bwv423 was in the genuine-8 Gate M set (Minor→Diminished). It is no longer in
genuine-32. Determine why:

```python
import json
from pathlib import Path

fpath = Path('tools/corpus/bwv423.ours.json')
m21path = Path('tools/corpus/bwv423.music21.json')

data = json.loads(fpath.read_text(encoding='utf-8'))
m21 = json.loads(m21path.read_text(encoding='utf-8'))

# Gate M target was at m=9 b=2.0
for r in data.get('regions', []):
    if r['measureNumber'] == 9 and abs(r['beat'] - 2.0) < 0.15:
        print("ours: quality=%s rootPc=%s bassPc=%s bassIsRoot=%s"
              % (r.get('quality'), r.get('rootPitchClass'),
                 r.get('bassPitchClass'), r.get('bassIsRoot')))
        break

for r in m21.get('regions', []):
    if r['measureNumber'] == 9 and abs(r['beat'] - 2.0) < 0.15:
        print("m21: quality=%s rootPc=%s"
              % (r.get('quality'), r.get('rootPitchClass')))
        break
```

Report: did bwv423 m9 b2 exit the genuine set because (a) our output now matches
music21, (b) music21/DCML now disagree with each other, or (c) the region no
longer exists at that position?

**B — Gate N: only bwv322 remains of 6**

Gate N genuine set was: bwv123.6, bwv322, bwv337, bwv392, bwv417, bwv425.
Only bwv322 appears in genuine-32 now. For each of the 5 absent cases, print
what our analyzer currently outputs at the Gate N target region:

```python
GATE_N = [
    ('tools/corpus/bwv123.6.ours.json',  7, 2.0),
    ('tools/corpus/bwv337.ours.json',    1, 2.0),
    ('tools/corpus/bwv392.ours.json',   11, 4.0),
    ('tools/corpus/bwv417.ours.json',    3, 2.0),
    ('tools/corpus/bwv425.ours.json',   22, 3.0),
]

for fpath, meas, beat in GATE_N:
    stem = Path(fpath).stem.replace('.ours', '')
    data = json.loads(Path(fpath).read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            print(f"{stem} m{meas} b{beat}: quality={r.get('quality')} "
                  f"rootPc={r.get('rootPitchClass')} bassPc={r.get('bassPitchClass')} "
                  f"bassIsRoot={r.get('bassIsRoot')}")
            break
```

Report: for each absent case, is the region now BIR=false (our analyzer already
inverted it), or does it match music21, or is it DCML-disagree?

This step determines whether Gate N has genuinely shrunk to 1 real case.

---

## Step 1 — Confirm quality strings and pitch-class equivalence

For each of the 6 Cluster A cases, print the winner and ALL alternatives.
Confirm:
1. The exact quality string for the Minor6 winner (e.g., "Minor6", "MinorSixth", "Addeds6")
2. The exact quality string for the half-dim alt (e.g., "HalfDiminished7",
   "HalfDiminishedSeventh", "Minor7b5")
3. That alt.rootPc == (winner.rootPc − 3 + 12) % 12 (the minor-third-below root)
4. That alt.bassPc == winner.bassPc
5. Whether the alt also has bassIsRoot == False

```python
import json
from pathlib import Path

TARGETS = [
    ('tools/corpus/bwv259.ours.json',   8, 1.0, 'bwv259'),
    ('tools/corpus/bwv284.ours.json',   3, 3.0, 'bwv284'),
    ('tools/corpus/bwv335.ours.json',   8, 1.0, 'bwv335'),
    ('tools/corpus/bwv40.8.ours.json', 10, 1.0, 'bwv40.8'),
    ('tools/corpus/bwv407.ours.json',   7, 4.0, 'bwv407'),
    ('tools/corpus/bwv90.5.ours.json',  8, 2.0, 'bwv90.5'),
]

for fpath, meas, beat, label in TARGETS:
    data = json.loads(Path(fpath).read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            wRootPc = r.get('rootPitchClass', -1)
            wBassPc = r.get('bassPitchClass', -1)
            target_rootPc = (wRootPc - 3 + 12) % 12

            print(f"\n{label}  m={meas} b={beat}")
            print(f"  winner: quality={r.get('quality')!r} rootPc={wRootPc} "
                  f"bassPc={wBassPc} bassIsRoot={r.get('bassIsRoot')} "
                  f"score={r.get('chordScore'):.4f}")
            print(f"  (target alt: rootPc={target_rootPc} bassPc={wBassPc} "
                  f"bassIsRoot=False)")

            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                flag = ""
                if (a.get('rootPitchClass') == target_rootPc and
                        a.get('bassPitchClass') == wBassPc):
                    flag = "  ← CLUSTER-A CANDIDATE"
                print(f"  alt[{i}]: quality={a.get('quality')!r} "
                      f"rootPc={a.get('rootPitchClass')} "
                      f"bassPc={a.get('bassPitchClass')} "
                      f"bassIsRoot={a.get('bassIsRoot')} "
                      f"score={a.get('score'):.4f} "
                      f"margin={margin:.4f}{flag}")
            break
```

Report:
- Exact quality strings (winner and alt)
- How many of the 6 cases have the expected alt (rootPc−3, same bass) in results[]?
- For those that do: is the alt quality consistently HalfDiminished (or similar)?
- For those that don't: what is the alt quality at the target rootPc?

If fewer than 4 of the 6 have the correct alt in results[]: STOP. The pattern
may not be gate-addressable (same candidate-generation issue as Gate P).

---

## Step 2 — Full Baroque corpus scan (Cluster A pattern)

Using the exact quality strings confirmed in Step 1, scan all `.ours.json` files
for the Cluster A pattern:
  winner.quality == [Minor6_quality] AND winner.bassIsRoot == True
  alt.quality == [HalfDim7_quality] AND alt.bassPc == winner.bassPc
  alt.rootPc == (winner.rootPc − 3 + 12) % 12
  margin ≤ 0.65 (generous initial threshold — calibrate tighter after seeing FP count)

```python
import json
from pathlib import Path

CORPUS_DIR = Path('tools/corpus')

# Fill in from Step 1:
WINNER_QUALITY = "???"        # exact string from Step 1
ALT_QUALITY    = "???"        # exact string from Step 1

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

print(f"Cluster A scan (threshold ≤ {THRESHOLD}):")
print(f"  Genuine found: {len(genuine_found)} / {len(GENUINE)}")
print(f"  False positives: {len(fp_list)}")
print("\nFalse positives:")
for x in fp_list:
    print(f"  {x['stem']:<20} m={x['meas']:>3} b={x['beat']:.1f}  "
          f"wRoot={x['wRootPc']} wBass={x['wBassPc']} "
          f"altRoot={x['altRootPc']} margin={x['margin']:.4f}")

# Tighter thresholds
for t in [0.50, 0.40, 0.30]:
    fp_t = [x for x in fp_list if x['margin'] <= t]
    gen_t = [x for x in genuine_found if x['margin'] <= t]
    print(f"\nAt threshold ≤ {t}: genuine={len(gen_t)} FP={len(fp_t)}")
```

Report:
- Genuine found at each threshold
- FP count at each threshold
- Full FP list with raw values
- Whether a threshold exists where genuine ≥ 4 AND FP ≤ 2

If FP > 3 at all thresholds: STOP. Do not proceed to Jazz scan.

---

## Step 3 — Temporal context for Cluster A matches (if Step 2 FP ≤ 3)

For each match from Step 2 (genuine AND FP), print the temporal context:

```python
TEMPORAL = ['nextRootPc', 'previousRootPc', 'previousQuality',
            'previousBassPc', 'bassIsStepwiseFromPrevious',
            'bassIsStepwiseToNext', 'consecutiveBassStepwiseCount',
            'regionMetricWeight']

print("\nTemporal context for Cluster A matches:")
for x in matches:
    fpath = CORPUS_DIR / f"{x['stem']}.ours.json"
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == x['meas'] and abs(r['beat'] - x['beat']) < 0.15:
            label = "GENUINE" if x['genuine'] else "FP"
            print(f"\n{label}  {x['stem']} m={x['meas']} b={x['beat']:.1f}  margin={x['margin']:.4f}")
            for f in TEMPORAL:
                print(f"  {f}: {repr(r.get(f, 'MISSING'))}")
            break
```

Report any temporal signals that differ between genuine and FP groups.

---

## Step 4 — Cluster B: Power/Sus2 characterization (brief)

For each of the 3 Cluster B cases, print winner + all alternatives:

```python
CLUSTER_B = [
    ('tools/corpus/bwv227.1.ours.json', 11, 3.0, 'bwv227.1'),
    ('tools/corpus/bwv43.11.ours.json',  3, 2.0, 'bwv43.11'),
    ('tools/corpus/bwv361.ours.json',    5, 4.0, 'bwv361'),
]

for fpath, meas, beat, label in CLUSTER_B:
    data = json.loads(Path(fpath).read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            print(f"\n{label}  m={meas} b={beat}")
            print(f"  winner: quality={r.get('quality')!r} rootPc={r.get('rootPitchClass')} "
                  f"bassPc={r.get('bassPitchClass')} bassIsRoot={r.get('bassIsRoot')} "
                  f"score={r.get('chordScore'):.4f}")
            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                print(f"  alt[{i}]: quality={a.get('quality')!r} "
                      f"rootPc={a.get('rootPitchClass')} "
                      f"bassPc={a.get('bassPitchClass')} "
                      f"bassIsRoot={a.get('bassIsRoot')} "
                      f"score={a.get('score'):.4f} margin={margin:.4f}")
            break
```

Report: exact quality strings for winner (Power/Sus) and alts. Are the alts
always Sus2/Sus4 at the same bass? Do all 3 have the same structural pattern?
What is the music21 ground-truth quality for each (from `.music21.json`)?

---

## Step 5 — Report to Cowork

```
Step 0 — Coverage discrepancies:
  bwv423 Gate M: [exited because — describe]
  Gate N remaining genuine: [1 / how many of 5 absent are now correct]

Step 1 — Cluster A quality strings and alt presence:
  Winner quality string: "[exact]"
  Alt quality string: "[exact]"
  Cases with correct alt in results[]: N / 6
  Alt.bassIsRoot: [consistently False / other]
  Any cases missing the alt: [list]

Step 2 — Baroque Cluster A scan:
  At threshold ≤ 0.65: genuine=N  FP=N
  At threshold ≤ 0.50: genuine=N  FP=N
  At threshold ≤ 0.40: genuine=N  FP=N
  At threshold ≤ 0.30: genuine=N  FP=N
  Best threshold (genuine ≥ 4, FP ≤ 2): [N or "none found"]
  [FP list with raw fields]

Step 3 — Temporal context:
  Signals separating genuine from FP: [describe or "none"]

Step 4 — Cluster B characterization:
  Winner quality string(s): "[exact]"
  Alt quality string(s): "[exact]"
  Pattern: [consistent / varied]
  music21 ground-truth qualities: [list]

Gate Q viability verdict:
  [VIABLE — threshold=N, temporal guard needed/not needed]
  [BLOCKED — reason]
Gate R (Cluster B) viability hint:
  [Promising / needs more investigation / blocked]
```

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.
