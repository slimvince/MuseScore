# Iteration 56: Re-characterize genuine-14, fixed-7, and regressed-4

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=14, BIR=false=132. Jazz BIR=false=12.

Build fresh before every BIR measurement. Verify binary is newer than source.

Do NOT change any source code. Diagnostic and reporting only.

---

## Background

Iter 54 moved BIR=true from 21 to 14 (−7 fixed by better segmentation) and
BIR=false from 128 to 132 (+4 regressions). Before planning Round 3 or any
further gate work, we need to understand:

1. Which 7 genuine-21 cases were fixed (no longer errors)?
2. Which 4 new cases appeared in BIR=false (regressions)?
3. What do the remaining 14 genuine cases look like?

This characterisation drives all subsequent work.

---

## Step 1 — Confirm corpus is current

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Must show BIR=true=14, BIR=false=132. If not, regenerate:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

---

## Step 2 — Extract current genuine-14

Adapt the existing `tools/diag_genuine32_characterize.py` (or equivalent
characterization script) to extract the current three-way genuine error set.
Run it and save output to `tools/iter54_genuine14_characterization.txt`.

The script must print for each genuine case:
- stem, measureNumber, beat
- winner: rootPitchClass, quality, bassPitchClass, bassIsRoot, chordScore
- reference rootPc (from music21/DCML agreement)
- top 3 alternatives with rootPitchClass, quality, score, margin

---

## Step 3 — Identify fixed-7 (cases in genuine-21 not in genuine-14)

Compare against the known genuine-21 list from
`tools/iter46_genuine21_characterization.txt` (or the documented 21 cases
from Iter 47). Identify which cases are now absent from genuine-14.

For each fixed case, determine HOW it was fixed:
- Did a new boundary from greedy segmentation split a region so the correct
  pitch-class set is now scored? (boundary fix)
- Or did a merged region now include more pitch classes that helped the scorer?
  (merge fix)

To diagnose: for each fixed case, print the regions in the vicinity from the
current corpus JSON and compare to what the Jaccard segmentation would have
produced. Since we no longer have the Jaccard corpus (it was overwritten),
reconstruct from the characterization file: the Jaccard region spanned a
certain measure/beat range; does the greedy output have a different boundary
near that case?

```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')
FIXED_CASES = [
    # Fill in from comparison of genuine-21 vs genuine-14
    # ('stem', measureNumber, beat),
]

for stem, meas, beat in FIXED_CASES:
    fpath = CORPUS / f'{stem}.ours.json'
    data = json.loads(fpath.read_text(encoding='utf-8'))
    print(f'\n=== FIXED: {stem} m={meas} b={beat} ===')
    # Print the 3 regions surrounding the formerly-erroneous position
    for r in data.get('regions', []):
        if abs(r.get('measureNumber', 0) - meas) <= 1:
            print(f"  m={r['measureNumber']} b={r['beat']:.2f} "
                  f"root={r['rootPitchClass']} qual={r['quality']!r} "
                  f"bass={r['bassPitchClass']} bassIsRoot={r['bassIsRoot']} "
                  f"score={r['chordScore']:.4f}")
```

---

## Step 4 — Identify regressed-4 (new cases in BIR=false)

Extract the full BIR=false error list from `analyze_inversion_errors.py`.
If the script does not output individual cases, modify it or run a separate
scan:

```python
import json
from pathlib import Path

# Load music21 and DCML reference data — adapt paths to actual locations
# used by analyze_inversion_errors.py
CORPUS = Path('tools/corpus')

# This script must match the logic in analyze_inversion_errors.py:
# Three-way agree: music21 rootPc == DCML rootPc != our rootPc
# bassIsRoot=false cases = BIR=false

# Print all current BIR=false cases with stem/meas/beat
# Compare against the known BIR=false=128 list to find the 4 new ones

# Known previous BIR=false cases should be inferrable from:
# - The genuine-21 characterization (those were BIR=true)
# - Everything else in BIR=false=128 was already there

# Simplest approach: run analyze_inversion_errors.py with --verbose or
# equivalent flag, capture all cases, filter for bassIsRoot=false.
# If no --verbose flag exists, read the script and add minimal output.
```

For each of the 4 regressed cases print:
- stem, measureNumber, beat
- Our current output: rootPitchClass, quality, bassPitchClass, bassIsRoot
- Music21 + DCML agreed rootPc
- The 3 regions in the vicinity — did a new greedy boundary create a spurious
  short region that confused the scorer?

---

## Step 5 — Characterize genuine-14 by cluster

Group the 14 remaining genuine cases by pattern. Use the same cluster
categories as the genuine-21 characterization:
- Gate M cluster (Minor→Diminished/HalfDim, previously 7 cases)
- Cluster A (Minor6→HalfDim inversion, previously 7 cases)
- Power/Suspended (previously 4 cases)
- Edge cases
- Any new cluster introduced by the segmentation change

For each cluster report:
- How many cases remain
- Whether the blocking reason from genuine-21 still applies
- Whether the greedy segmentation changes anything about the candidate pool
  (run the alt-presence check for Cluster A cases — is the HalfDim alt still
  absent from results[]?)

---

## Step 6 — Save characterization

Save full output to `tools/iter54_genuine14_characterization.txt` and
`tools/iter54_regression4_characterization.txt`.

---

## Step 7 — Report to Cowork

```
Step 1 — Corpus confirmed: BIR=true=14  BIR=false=132

Fixed-7 (were in genuine-21, now correct):
  [For each: stem m=N b=N — reason: boundary fix / merge fix]

Regressed-4 (new in BIR=false):
  [For each: stem m=N b=N — our output root=N qual=Q,
   agreed root=N — apparent cause]

Genuine-14 clusters:
  Gate M:          N cases (was 7) — blocking reason still applies: [yes/no]
  Cluster A:       N cases (was 7) — HalfDim alt still absent: [yes/no]
  Power/Suspended: N cases (was 4)
  Other/new:       N cases
  [describe any new patterns]

Actionable next steps:
  [regressions: fixable by parameter tuning / gate / investigation needed]
  [genuine-14: any new viable gates identified?]

Files saved:
  tools/iter54_genuine14_characterization.txt: [yes]
  tools/iter54_regression4_characterization.txt: [yes]
```
