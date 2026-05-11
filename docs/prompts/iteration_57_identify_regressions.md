# Iteration 57: Identify the 4 BIR=false regressions + establish enumeration practice

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=14, BIR=false=132. Jazz BIR=false=12.

Build fresh before every BIR measurement. Verify binary is newer than source.

Do NOT change any source code. Diagnostic and documentation only.

---

## Background

Iter 54 introduced +4 BIR=false regressions when switching to greedy-expand
segmentation. The prior BIR=false=128 cases were never enumerated, so the 4
new cases cannot be identified by diffing. This iteration:

1. Rebuilds the pre-Iter-54 Jaccard binary from commit 5df8421114 to enumerate
   the 128 BIR=false cases into a temporary corpus.
2. Diffs that list against `tools/iter54_bir_false_enumeration.txt` (current 132)
   to identify the 4 regressions.
3. Characterises each regression.
4. Establishes BIR=false enumeration as a standing practice in build_and_test.md.

The current working tree is NOT modified. All git operations use a detached HEAD
for the old build and then return to the current HEAD.

---

## Step 1 — Enumerate BIR=false=128 from pre-Iter-54 binary

```bash
# Save current HEAD hash for return
CURRENT_HEAD=$(git rev-parse HEAD)
echo "Current HEAD: $CURRENT_HEAD"

# Check out last Jaccard commit (pre-Iter-54, Iter 36 recovery)
git checkout 5df8421114

# Build the Jaccard binary
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Regenerate corpus into a SEPARATE directory (do NOT overwrite tools/corpus/)
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir /tmp/corpus_jaccard128

# Confirm BIR=false=128 with Jaccard corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py \
    --corpus-dir /tmp/corpus_jaccard128
```

Expected: BIR=true=21, BIR=false=128. Stop if this does not match —
report the discrepancy before proceeding.

---

## Step 2 — Enumerate the 128 BIR=false cases

Using `tools/diag_iter54_bir_false_enumerate.py` (or equivalent), enumerate
all 128 BIR=false cases from /tmp/corpus_jaccard128 to a file:

```bash
cd C:\s\MS && python tools/diag_iter54_bir_false_enumerate.py \
    --corpus-dir /tmp/corpus_jaccard128 \
    > tools/birfalse_baseline_iter46_jaccard.txt
```

If the script does not support --corpus-dir, adapt it to accept a corpus path
argument. Save as `tools/birfalse_baseline_iter46_jaccard.txt`.

Format per case (must match iter54_bir_false_enumeration.txt for easy diffing):
```
stem  measureNumber  beat  ourRootPc  ourQuality  agreedRootPc
```

---

## Step 3 — Return to current HEAD

```bash
git checkout $CURRENT_HEAD

# Rebuild current (greedy) binary
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Regenerate Baroque corpus from current binary
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus

# Confirm current baselines restored
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=14, BIR=false=132. Stop if this does not match.

---

## Step 4 — Diff to find the 4 regressions

```python
from pathlib import Path

def parse_enumeration(path):
    cases = {}
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split()
        if len(parts) >= 3:
            key = (parts[0], int(parts[1]), float(parts[2]))
            cases[key] = parts
    return cases

jaccard = parse_enumeration('tools/birfalse_baseline_iter46_jaccard.txt')
greedy  = parse_enumeration('tools/iter54_bir_false_enumeration.txt')

regressions = {k: v for k, v in greedy.items()  if k not in jaccard}
fixed       = {k: v for k, v in jaccard.items() if k not in greedy}

print(f'Regressions (in greedy-132, not in jaccard-128): {len(regressions)}')
for k, v in sorted(regressions.items()):
    print(f'  {v}')

print(f'\nFixed (in jaccard-128, not in greedy-132): {len(fixed)}')
for k, v in sorted(fixed.items()):
    print(f'  {v}')
```

Expected: 4 regressions, ~0 fixed in BIR=false (the BIR=false fixes would show
as BIR=true→correct, not BIR=false→absent). If the diff produces a different
count, report the discrepancy.

Note: the diff key uses (stem, measureNumber, beat). If greedy created a new
boundary that moved a region from beat X to beat X±ε, the key may not match
despite being the same underlying error. In that case, do a fuzzy match
(|beat_a - beat_b| < 0.1) and note any near-misses.

---

## Step 5 — Characterise each regression

For each of the 4 regressions, print the full region detail from the current
greedy corpus:

```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')
REGRESSIONS = [
    # Fill from Step 4 output
    # ('stem', measureNumber, beat),
]

for stem, meas, beat in REGRESSIONS:
    fpath = CORPUS / f'{stem}.ours.json'
    data = json.loads(fpath.read_text(encoding='utf-8'))
    print(f'\n=== REGRESSION: {stem} m={meas} b={beat:.2f} ===')
    for r in data.get('regions', []):
        if abs(r.get('measureNumber', 0) - meas) <= 1:
            print(f"  m={r['measureNumber']} b={r['beat']:.2f}  "
                  f"root={r.get('rootPitchClass')} qual={r.get('quality')!r}  "
                  f"bass={r.get('bassPitchClass')} bassIsRoot={r.get('bassIsRoot')}  "
                  f"score={r.get('chordScore', 0):.4f}  "
                  f"pcMask={r.get('pitchClassSet')}")
            for i, a in enumerate(r.get('alternatives', [])[:3]):
                print(f"    alt[{i}]: root={a.get('rootPitchClass')} "
                      f"qual={a.get('quality')!r} score={a.get('score', 0):.4f}")
```

For each regression, determine:
- Is this a new greedy-created boundary that split a previously-correct region,
  producing a short region with a misleading pitch-class set?
- Or is this a pre-existing scoring weakness now exposed by a different boundary?
- Is it fixable by a Round 3 merge, a minimum-duration guard, or a gate?

---

## Step 6 — Save enumeration files and update build_and_test.md

Save `tools/birfalse_baseline_iter46_jaccard.txt` to the repository.

Update `build_and_test.md` to add a standing practice section:

```
## Standing practice: BIR=false enumeration

At every baseline update, run the enumeration script and commit the output:
  python tools/diag_iter54_bir_false_enumerate.py > tools/birfalse_baseline_ITERNN.txt
  git add tools/birfalse_baseline_ITERNN.txt

This enables clean diffs between baselines to identify regressions and fixes.
Current enumeration files:
  tools/birfalse_baseline_iter46_jaccard.txt — 128 cases (Iter 46/Jaccard, commit 5df8421114)
  tools/iter54_bir_false_enumeration.txt     — 132 cases (Iter 54/greedy, commit 7a006cf14f)
```

---

## Step 7 — Commit

```
git add tools/birfalse_baseline_iter46_jaccard.txt
git add build_and_test.md
git commit -m "Iter 57: add Jaccard BIR=false=128 enumeration baseline + enumeration practice

Enumerates all 128 BIR=false cases from the last Jaccard commit (5df8421114)
to enable clean diff against the greedy baseline (132 cases, 7a006cf14f).

Establishes standing practice: enumerate BIR=false at every baseline update."
```

---

## Step 8 — Report to Cowork

```
Step 1 — Jaccard build confirmed: BIR=true=21  BIR=false=128  [yes/no]

Step 3 — Current baselines confirmed: BIR=true=14  BIR=false=132  [yes/no]

Step 4 — Diff results:
  Regressions identified: N (expected 4)
  Fixed in BIR=false: N
  [List regressions: stem m=N b=N]

Step 5 — Regression characterisation:
  [For each: stem m=N b=N
   Cause: [greedy boundary split / pre-existing scoring / other]
   Fixable by: [Round 3 merge / duration guard / gate / unknown]]

Step 6 — Files saved:
  tools/birfalse_baseline_iter46_jaccard.txt: [yes]
  build_and_test.md updated: [yes]

Committed: [yes — hash] / [not committed — reason]
```
