# Iteration 17: Diagnostic — why only 9 of 28 Gate G-E cases fired

## ⚠ Critical behaviour rules

- Read-only investigation. Zero code changes. Zero commits.
- Write and run Python scripts inline (do not save to repo).

---

## Background

Iteration 12 fixed 9 of the 48 MinorAdd6 BIR=true errors (BIR=true: 109→100).
The Iteration 10 diagnostic predicted 28 fixes (7 viiø7 + 21 iiø7). Gate G-E
fires when `altRoot == (keyTonicPc+11)%12 || altRoot == (keyTonicPc+2)%12`.

CC's Iteration 12 report noted: "29 HalfDiminished top-alternative entries
remaining in the BIR=true pool suggest the alt IS reaching results[] in those
cases, but the key-context condition is not matching."

The likely cause: the Iteration 10 diagnostic computed keyTonicPc from static
fields in the corpus JSON, but the runtime `keyTonicPc` in `analyzeChord` is
computed from `keySignatureFifths` and `keyMode` as resolved by the per-region
local key detection. These may differ — especially mid-piece where a modulation
has been detected, or where the mode is HarmonicMinor vs. Aeolian.

This iteration finds the truth.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=100, BIR=false=788

---

## Step 2 — Regenerate corpus

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Confirm BIR=true=100 and BIR=false=788. If either differs, STOP and report.

---

## Step 3 — Inspect a single JSON to map available fields

Write and run a Python script (do not save) that opens ONE corpus JSON that
contains MinorAdd6 errors and prints the full structure of ONE such region,
including every key-related field present at any level (score, region, winner,
alternatives). This determines what key information is actually stored.

```python
import json, glob, os

corpus_dir = r'C:\s\MS\tools\corpus'
for f in sorted(glob.glob(os.path.join(corpus_dir, '*.json'))):
    data = json.load(open(f, encoding='utf-8'))
    for region in data.get('regions', []):
        w = region.get('winner', {})
        alts = region.get('alternatives', [])
        if (w.get('quality') == 'MinorAdd6'
                and region.get('bassIsRoot') is True
                and region.get('referenceIsRoot') is False):
            print('=== Sample MinorAdd6 BIR=true region ===')
            print(json.dumps(region, indent=2))
            import sys; sys.exit(0)
```

Report the full JSON of that one region. In particular, identify:
- What key fields exist (e.g. `keyFifths`, `keySignatureFifths`, `keyMode`,
  `tonicPc`, `keyTonicPc`, or similar)
- Whether any field stores the actual tonic pitch class used at analysis time
- Whether the winner and/or alternatives carry key context

---

## Step 4 — Full breakdown of remaining 39 MinorAdd6 errors

Using what you learned in Step 3 about the available key fields, write and run
a Python script (do not save) that:

1. Iterates all corpus JSONs
2. Collects every MinorAdd6 BIR=true error (bassIsRoot=True, referenceIsRoot=False,
   winner quality=MinorAdd6)
3. For each, extracts:
   - Score filename and measure
   - `winnerRootPc` (winner's root pitch class, 0–11)
   - `halfDimAltRootPc` (root of the HalfDiminished alternative, if present)
   - `keyTonicPc` as stored in the JSON (whichever field carries it)
   - `interval` = `(halfDimAltRootPc - keyTonicPc + 12) % 12`  ← what the
     runtime gate compares against 11 and 2
4. Groups by interval and reports counts
5. Also reports cases where no HalfDim alt is found in the alternatives list

```python
import json, glob, os
from collections import Counter, defaultdict

corpus_dir = r'C:\s\MS\tools\corpus'

# Adjust these field names based on what Step 3 reveals:
KEY_TONIC_FIELD = 'keyTonicPc'   # ← update if the field has a different name
QUALITY_FIELD   = 'quality'

results_by_interval = Counter()
no_halfdim_alt = []
cases = []

for f in sorted(glob.glob(os.path.join(corpus_dir, '*.json'))):
    data = json.load(open(f, encoding='utf-8'))
    fname = os.path.basename(f)
    for region in data.get('regions', []):
        w = region.get('winner', {})
        if (w.get(QUALITY_FIELD) != 'MinorAdd6'
                or region.get('bassIsRoot') is not True
                or region.get('referenceIsRoot') is not False):
            continue
        alts = region.get('alternatives', [])
        halfdim = next(
            (a for a in alts if a.get(QUALITY_FIELD) == 'HalfDiminished'),
            None)
        if halfdim is None:
            no_halfdim_alt.append({'file': fname, 'measure': region.get('measure')})
            continue
        # Try to get tonicPc — adjust field name from Step 3
        tonic = (w.get(KEY_TONIC_FIELD)
                 or region.get(KEY_TONIC_FIELD)
                 or region.get('keyTonicPc')
                 or region.get('tonicPc'))
        if tonic is None:
            print(f"WARNING: no tonic field found in {fname} m{region.get('measure')}")
            continue
        alt_root = halfdim.get('rootPc')
        interval = (alt_root - tonic + 12) % 12
        results_by_interval[interval] += 1
        cases.append({
            'file': fname,
            'measure': region.get('measure'),
            'winnerRootPc': w.get('rootPc'),
            'altRootPc': alt_root,
            'keyTonicPc': tonic,
            'interval': interval,
        })

print(f"\nTotal MinorAdd6 BIR=true errors: {len(cases) + len(no_halfdim_alt)}")
print(f"  With HalfDim alt in results[]: {len(cases)}")
print(f"  Without HalfDim alt:           {len(no_halfdim_alt)}")
print(f"\nInterval breakdown (altRoot - keyTonicPc) % 12:")
for interval, count in sorted(results_by_interval.items()):
    label = {11: 'viiø7 (leading tone)', 2: 'iiø7 (supertonic)',
             0: 'I (tonic)', 4: 'III', 5: 'IV', 7: 'V', 9: 'VI'}.get(interval, '?')
    print(f"  +{interval:2d} ({label}): {count}")
print(f"\nNo-HalfDim cases: {len(no_halfdim_alt)}")
for c in no_halfdim_alt[:10]:
    print(f"  {c['file']} m{c['measure']}")
```

If the key tonic field name from Step 3 differs from `keyTonicPc`, update the
script accordingly before running.

---

## Step 5 — Inspect specific cases for the dominant non-11/non-2 interval

For the interval group with the most cases (other than 11 and 2), print 5
representative examples showing: score, measure, winner symbol, alt symbol,
key signature, and the stored keyTonicPc.

Also: for the iiø7 cases (interval=2) — confirm how many there are. The Iteration
10 diagnostic predicted 21 but only some portion of those fired. If interval=2
cases appear in the remaining 39, it means the stored `keyTonicPc` in the JSON
differs from what `analyzeChord` received at runtime. Confirm or refute this.

---

## Step 6 — Report

```
Corpus regenerated:        BIR=true=N, BIR=false=N

Key field found in JSON:   <field name and location — winner, region, or score level>
Tonic field is runtime or post-hoc: <describe — is this the value passed to analyzeChord?>

MinorAdd6 BIR=true total:  N (confirm = 39)
  With HalfDim alt:        N
  Without HalfDim alt:     N

Interval breakdown (altRoot - keyTonicPc) % 12:
  +11 (viiø7):  N  ← Gate G-E already fires on these
  +2  (iiø7):   N  ← Gate G-E already fires on these
  +X  (?):      N  ← dominant remaining group
  +Y  (?):      N
  ...

Interval=2 cases still present: N
  If > 0: this confirms keyTonicPc in JSON ≠ runtime value for those cases.

Dominant non-11/non-2 interval:  +N (N cases) — scale degree: <describe>
  Example: <score> m<N>, winner <symbol>, alt <symbol>, keyTonicPc=<N>

Most actionable finding:   <which interval group is largest and musically unambiguous?>
Unexpected findings:       none / <describe>
```
