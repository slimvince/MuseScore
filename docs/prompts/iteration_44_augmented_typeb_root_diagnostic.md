# Iteration 44: Augmented TYPE-B root correction — diagnostic

## Standing rule — no symbol inference

**No chord symbol string parsing of any kind. No Roman numeral inference.
Use only structured fields (quality, rootPc, bassPc, bassIsRoot, score, extensions).**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=32, BIR=false=177.

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.

---

## Background

Gate O (Iter 42) was reverted. It tried to fix bwv288 m11, bwv309 m12, bwv331 m2
by switching from Augmented (root-position) to MinorMajor7 (2nd inversion).
The fix was wrong: the ground truth (music21 + DCML) labels these regions as a
**different Augmented root**, not MinMaj7.

The key insight is that Augmented triads are fully symmetric under major-third
transposition. The pitch-class set {E, G#, C} can be analysed as:

  - E+  (rootPc=4):  bass=E is the root      → bassIsRoot=true (root-position)
  - C+  (rootPc=0):  bass=E is the M3        → bassIsRoot=false (1st inversion)
  - Ab+ (rootPc=8):  bass=E is the A5        → bassIsRoot=false (2nd inversion)

In all 3 known cases the observed pattern is:

  winner:  Augmented, rootPc=X,         bassPc=X  (bassIsRoot=true)
  correct: Augmented, rootPc=(X-4)%12,  bassPc=X  (bassIsRoot=false — 1st inv)

  bwv288 m11 b1: winner E+ (root=4, bass=4) → correct C+/E (root=0, bass=4)
  bwv309 m12 b3: winner D+ (root=2, bass=2) → correct Bb+/D (root=10, bass=2)
  bwv331 m2  b1: winner E+ (root=4, bass=4) → correct C+/E (root=0, bass=4)
                 NOTE: bwv331 three-way status uncertain (Step 0 below)

This is a **TYPE-B error**: correct quality (Augmented), correct pitch classes,
wrong enharmonic root — choosing the root-position reading when the 1st-inversion
reading is correct. It is also an inversion error: we say bassIsRoot=true when
the correct reading has bassIsRoot=false.

This is distinct from Gate K (which corrects bassIsRoot=false→true for Augmented
I4 patterns) and Gate L (which prefers Major over Augmented when roots match).

---

## Step 0 — Verify bwv331 three-way status

Gate O arithmetic: BIR=true 32→29 (−3 cases left BIR=true), BIR=false 177→179
(+2 regressions). One of the 3 fired cases did NOT add to BIR=false — suggesting
it was not a music21 mismatch in the first place after the switch, which implies
bwv331 may not be a genuine three-way error.

Do the following three checks for bwv331 m2 b1:

**A — music21.json reference:**
```python
import json
data = json.load(open('tools/corpus/bwv331.music21.json'))
for r in data.get('regions', []):
    if r['measureNumber'] == 2 and abs(r['beat'] - 1.0) < 0.15:
        print("music21 m2 b1:", r)
        break
```

**B — Our current output (ours.json):**
```python
data = json.load(open('tools/corpus/bwv331.ours.json'))
for r in data.get('regions', []):
    if r['measureNumber'] == 2 and abs(r['beat'] - 1.0) < 0.15:
        print("ours m2 b1: quality=%s rootPc=%s bassPc=%s bassIsRoot=%s score=%s"
              % (r.get('quality'), r.get('rootPitchClass'), r.get('bassPitchClass'),
                 r.get('bassIsRoot'), r.get('chordScore')))
        for i, a in enumerate(r.get('alternatives', [])):
            print("  alt[%d]: quality=%s rootPc=%s bassPc=%s bassIsRoot=%s score=%s"
                  % (i, a.get('quality'), a.get('rootPitchClass'),
                     a.get('bassPitchClass'), a.get('bassIsRoot'), a.get('score')))
        break
```

**C — DCML annotation lookup:**
Search `tools/dcml/` for any annotation files (`.tsv`, `.csv`, `.json`) that
correspond to bwv331. Given the BWV→DCML ordinal mismatch discovered in Iter 43,
do a text search for "331" or the chorale title "Nun lob, mein Seel" across the
DCML directory structure.

```bash
grep -r "331\|Nun lob" tools/dcml/ --include="*.tsv" --include="*.csv" \
    -l 2>/dev/null | head -20
```

Report:
- Does music21.json agree or disagree with our E+ winner at m2 b1?
- What rootPc does music21 assign?
- Can DCML annotation be located? If yes, what does it say?
- Is bwv331 m2 b1 in the BIR=true mismatch set (i.e. does
  analyze_inversion_errors.py count it)?

If bwv331 is NOT a genuine three-way error, note it for removal from the
genuine-32 set.

---

## Step 1 — Confirm TYPE-B alternative exists in corpus JSON

For each of the 2 confirmed cases (bwv288, bwv309), print winner + ALL
alternatives, specifically looking for an Augmented alt with:
  alt.rootPc == (winner.rootPc - 4 + 12) % 12
  alt.bassPc == winner.bassPc
  alt.quality == "Augmented"  (or the exact Augmented quality string)

Also print whether alt.bassIsRoot == false for that candidate.

```python
import json

TARGETS = [
    ('tools/corpus/bwv288.ours.json',  11, 1.0, 'bwv288'),
    ('tools/corpus/bwv309.ours.json',  12, 3.0, 'bwv309'),
]

for fpath, meas, beat, label in TARGETS:
    data = json.load(open(fpath))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            wRootPc = r.get('rootPitchClass', -1)
            wBassPc = r.get('bassPitchClass', -1)
            typeb_rootPc = (wRootPc - 4 + 12) % 12

            print(f"\n{label}  m={meas} b={beat}")
            print(f"  winner: quality={r.get('quality')} rootPc={wRootPc} "
                  f"bassPc={wBassPc} bassIsRoot={r.get('bassIsRoot')} "
                  f"score={r.get('chordScore'):.4f}")
            print(f"  (looking for TYPE-B alt: Augmented rootPc={typeb_rootPc} "
                  f"bassPc={wBassPc} bassIsRoot=False)")

            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                flag = ""
                if (a.get('quality') == r.get('quality') and
                        a.get('bassPitchClass') == wBassPc and
                        a.get('rootPitchClass') == typeb_rootPc):
                    flag = "  ← TYPE-B CANDIDATE"
                print(f"  alt[{i}]: quality={a.get('quality')} "
                      f"rootPc={a.get('rootPitchClass')} "
                      f"bassPc={a.get('bassPitchClass')} "
                      f"bassIsRoot={a.get('bassIsRoot')} "
                      f"score={a.get('score'):.4f} margin={margin:.4f}{flag}")
            break
```

Report:
- Does the TYPE-B alternative exist in results[] for each case?
- What is the margin (winner.score − alt.score)?
- What rank is the alt in the results list (index 0 = winner, 1 = 1st runner-up)?
- Is alt.bassIsRoot consistently False?

If no TYPE-B alternative exists in either case: STOP. The gate is not viable
(the correct reading is not in the candidate set).

---

## Step 2 — Full Baroque corpus scan (TYPE-B: −4 direction)

Scan all `.ours.json` files in `tools/corpus/` for regions matching the TYPE-B
pattern (winner root-pos Augmented, alt 1st-inversion Augmented one major-third
lower, same bass):

```python
import json, os
from pathlib import Path

CORPUS_DIR = Path('tools/corpus')
# Genuine cases confirmed after Step 0
GENUINE = {
    ('bwv288', 11, 1.0),
    ('bwv309', 12, 3.0),
    # bwv331 included tentatively pending Step 0 verification
    ('bwv331',  2, 1.0),
}

THRESHOLD = 0.50
results_typeb = []

for fpath in sorted(CORPUS_DIR.glob('*.ours.json')):
    stem = fpath.stem.replace('.ours', '')
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r.get('quality') != 'Augmented':
            continue
        if not r.get('bassIsRoot', False):
            continue

        wRootPc = r.get('rootPitchClass', -1)
        wBassPc = r.get('bassPitchClass', -1)
        wScore  = r.get('chordScore', 0.0)
        typeb_rootPc = (wRootPc - 4 + 12) % 12
        meas = r.get('measureNumber', -1)
        beat = r.get('beat', -1.0)

        for a in r.get('alternatives', []):
            if (a.get('quality') == 'Augmented' and
                    a.get('bassPitchClass') == wBassPc and
                    a.get('rootPitchClass') == typeb_rootPc):
                margin = wScore - a.get('score', 0.0)
                if margin <= THRESHOLD:
                    is_genuine = (stem, meas, beat) in GENUINE
                    results_typeb.append({
                        'stem': stem, 'meas': meas, 'beat': beat,
                        'wRootPc': wRootPc, 'wBassPc': wBassPc,
                        'altRootPc': typeb_rootPc,
                        'altBassIsRoot': a.get('bassIsRoot'),
                        'margin': margin,
                        'genuine': is_genuine,
                    })
                break  # only first matching alt per region

genuine_found = [x for x in results_typeb if x['genuine']]
fp_list       = [x for x in results_typeb if not x['genuine']]

print(f"\nTYPE-B scan (threshold ≤ {THRESHOLD}):")
print(f"  Genuine found: {len(genuine_found)} / {len(GENUINE)}")
print(f"  False positives: {len(fp_list)}")
print("\nFalse positives:")
for x in fp_list:
    print(f"  {x['stem']:<20} m={x['meas']:>3} b={x['beat']:.1f}  "
          f"wRoot={x['wRootPc']} wBass={x['wBassPc']} "
          f"altRoot={x['altRootPc']} altBassIsRoot={x['altBassIsRoot']} "
          f"margin={x['margin']:.4f}")

# Tighter threshold
THRESHOLD2 = 0.30
fp2 = [x for x in results_typeb if not x['genuine'] and x['margin'] <= THRESHOLD2]
print(f"\nAt tighter threshold ≤ {THRESHOLD2}: FP={len(fp2)}")
```

Report:
- How many genuine cases found at ≤ 0.50?
- How many FPs at ≤ 0.50 and ≤ 0.30?
- Full FP list with raw field values
- Is alt.bassIsRoot consistently False in all matches?

If FP count > 3 at both thresholds: STOP. Do not proceed to Step 4.

---

## Step 3 — Also scan the +4 direction (secondary check)

The third Augmented root possibility is alt.rootPc = (winner.rootPc + 4) % 12,
which would place the bass note as the augmented 5th of the chord (2nd inversion).
Run the same scan with this direction and report the hit count. This is
informational only — do not mix with the Step 2 results.

```python
THRESHOLD = 0.50
results_plus4 = []

for fpath in sorted(CORPUS_DIR.glob('*.ours.json')):
    stem = fpath.stem.replace('.ours', '')
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r.get('quality') != 'Augmented' or not r.get('bassIsRoot', False):
            continue
        wRootPc = r.get('rootPitchClass', -1)
        wBassPc = r.get('bassPitchClass', -1)
        wScore  = r.get('chordScore', 0.0)
        plus4_rootPc = (wRootPc + 4) % 12
        meas = r.get('measureNumber', -1)
        beat = r.get('beat', -1.0)

        for a in r.get('alternatives', []):
            if (a.get('quality') == 'Augmented' and
                    a.get('bassPitchClass') == wBassPc and
                    a.get('rootPitchClass') == plus4_rootPc):
                margin = wScore - a.get('score', 0.0)
                if margin <= THRESHOLD:
                    results_plus4.append({
                        'stem': stem, 'meas': meas, 'beat': beat,
                        'wRootPc': wRootPc, 'altRootPc': plus4_rootPc,
                        'margin': margin,
                    })
                break

print(f"\n+4 direction scan: {len(results_plus4)} matches at ≤ {THRESHOLD}")
for x in results_plus4:
    print(f"  {x['stem']:<20} m={x['meas']:>3} b={x['beat']:.1f}  "
          f"wRoot={x['wRootPc']} altRoot={x['altRootPc']} margin={x['margin']:.4f}")
```

---

## Step 4 — Temporal context for genuine vs FP cases (if Step 2 FP ≤ 3)

For each match from Step 2 (genuine AND FP), print the temporal context fields
that were added in Iter 41:

```python
TEMPORAL = ['nextRootPc', 'previousRootPc', 'previousQuality',
            'previousBassPc', 'bassIsStepwiseFromPrevious',
            'bassIsStepwiseToNext', 'consecutiveBassStepwiseCount',
            'regionMetricWeight']

print("\nTemporal context for TYPE-B matches:")
for x in results_typeb:
    fpath = CORPUS_DIR / f"{x['stem']}.ours.json"
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == x['meas'] and abs(r['beat'] - x['beat']) < 0.15:
            label = "GENUINE" if x['genuine'] else "FP"
            print(f"\n{label}  {x['stem']} m={x['meas']} b={x['beat']:.1f}")
            for f in TEMPORAL:
                print(f"  {f}: {repr(r.get(f, 'MISSING'))}")
            break
```

Report:
- Do any temporal fields cleanly separate genuine from FP?
- In particular: bassIsStepwiseToNext, regionMetricWeight, nextRootPc

---

## Step 5 — Jazz scan (only if Baroque FP ≤ 3 at some threshold)

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
```

Re-run Step 2 scan on the Jazz corpus at whichever threshold passed Baroque.
Report Jazz FP count.

Restore Baroque corpus afterward:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 6 — Report to Cowork

```
Step 0 — bwv331 three-way status:
  music21 m2 b1 rootPc: [value]
  DCML annotation found: [yes — rootPc=N / no]
  bwv331 m2 in BIR=true mismatch set: [yes / no]
  Verdict: [keep in genuine-32 / REMOVE from genuine-32]

Step 1 — TYPE-B alt exists in corpus JSON:
  bwv288 m11 b1: [yes — margin=N, alt rank=N / no]
  bwv309 m12 b3: [yes — margin=N, alt rank=N / no]
  alt.bassIsRoot: [consistently False / other]

Step 2 — Baroque TYPE-B scan (−4 direction, threshold ≤ 0.50):
  Genuine found: N / 3 (or 2 if bwv331 removed)
  FP count at ≤ 0.50: N
  FP count at ≤ 0.30: N
  [FP list with raw fields]

Step 3 — +4 direction scan:
  Matches: N  [list or "none"]

Step 4 — Temporal context:
  Fields that differ between genuine and FP: [list or "none"]
  Best candidate signal: [describe or "none found"]

Step 5 — Jazz scan (if reached):
  Threshold used: [0.50 / 0.30]
  Jazz FP count: N
  Jazz FP list: [list or "none"]

Viability verdict:
  Gate P (TYPE-B Augmented root correction): [VIABLE / BLOCKED — reason]
  Recommended threshold: [N]
  Temporal guard needed: [yes — describe / no]
```

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.
