# Iteration 48: Harmonic boundary detection — audit and fix under-segmentation

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=21, BIR=false=128. Jazz hard stop: BIR=false ≤ 75.

---

## Background

`detectHarmonicBoundariesJaccard` divides a score into fixed quarter-note windows
and fires a boundary when Jaccard distance between consecutive pitch-class sets
≥ 0.6 (configurable via `ChordAnalyzerPreferences::harmonicBoundaryJaccardThreshold`).

When no boundary fires, the current window's pitch classes are merged into the
running "previous" set via bitwise OR (`prevBits = union`). This means accumulated
pitch classes from multiple windows without a boundary make it progressively harder
to detect new boundaries — a genuinely new chord shares only a few pitch classes
with a large accumulated set, so the Jaccard distance may stay below threshold.

A user audit of BWV 87/7 (096 Jesu, meine Freude) found that measure 3, beat 3
has no boundary even though the harmony clearly changes (e.g. Dm → G7). This is
likely caused by the running accumulation suppressing the boundary signal.

There are two implementations of this algorithm with a noted §2.10 TODO:
  - `src/notation/internal/notationcomposingbridgehelpers.cpp` (Studio display path)
  - `tools/batch_analyze.cpp` (corpus pipeline path — affects BIR metrics)

Both must be fixed identically.

Do NOT commit until Step 7 explicitly says to.

---

## Step 1 — Read both implementations in full

Read:
  `src/notation/internal/notationcomposingbridgehelpers.cpp`
    — find `detectHarmonicBoundariesJaccard`, read the function
  `tools/batch_analyze.cpp`
    — find the equivalent boundary detection logic

For each, report:
1. Exact line numbers of the boundary detection loop
2. Where `prevBits` is updated (the accumulation step)
3. Whether the two implementations are truly identical or have diverged
4. The exact variable name for the threshold and where it is read

Do NOT make any changes in this step.

---

## Step 2 — Diagnose: region count comparison

Compare region counts from our current corpus vs the music21 reference.
Music21 is not ground truth, but a systematic count difference signals
under-segmentation.

```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')

count_diffs = []
for ours_path in sorted(CORPUS.glob('*.ours.json')):
    stem = ours_path.stem.replace('.ours', '')
    m21_path = CORPUS / f'{stem}.music21.json'
    if not m21_path.exists():
        continue
    ours = json.loads(ours_path.read_text(encoding='utf-8'))
    m21  = json.loads(m21_path.read_text(encoding='utf-8'))
    n_ours = len(ours.get('regions', []))
    n_m21  = len(m21.get('regions', []))
    diff   = n_ours - n_m21
    count_diffs.append((stem, n_ours, n_m21, diff))

count_diffs.sort(key=lambda x: x[3])   # most under-segmented first

print('Most under-segmented (ours << music21):')
for stem, no, nm, d in count_diffs[:20]:
    print(f'  {stem:<20} ours={no:>3} m21={nm:>3} diff={d:>+4}')

print('\nMost over-segmented (ours >> music21):')
for stem, no, nm, d in reversed(count_diffs[-20:]):
    print(f'  {stem:<20} ours={no:>3} m21={nm:>3} diff={d:>+4}')

under = sum(1 for *_, d in count_diffs if d < -2)
over  = sum(1 for *_, d in count_diffs if d >  2)
exact = sum(1 for *_, d in count_diffs if abs(d) <= 2)
print(f'\nSummary: under-segmented (diff < -2): {under}')
print(f'         over-segmented  (diff >  2): {over}')
print(f'         close match     (|diff| <= 2): {exact}')
mean_diff = sum(d for *_, d in count_diffs) / len(count_diffs)
print(f'         mean diff: {mean_diff:+.2f}')
```

Report the distribution. If mean diff < −1 (we produce fewer regions than
music21 on average), under-segmentation is confirmed at corpus scale.

---

## Step 3 — Diagnose: inspect a specific under-segmented chorale

Pick the chorale with the largest negative diff from Step 2. For that chorale,
print both the music21 region list and our region list side by side, aligned by
measure/beat, to identify which boundaries we miss:

```python
import json
from pathlib import Path

# Replace with actual worst-case stem from Step 2
STEM = 'bwv??'  

CORPUS = Path('tools/corpus')
ours = json.loads((CORPUS / f'{STEM}.ours.json').read_text(encoding='utf-8'))
m21  = json.loads((CORPUS / f'{STEM}.music21.json').read_text(encoding='utf-8'))

print(f'music21 regions ({len(m21["regions"])}):')
for r in m21.get('regions', []):
    print(f'  m={r.get("measureNumber"):>3} b={r.get("beat"):.2f}  '
          f'quality={r.get("quality")!r}  rootPc={r.get("rootPitchClass")}')

print(f'\nours regions ({len(ours["regions"])}):')
for r in ours.get('regions', []):
    print(f'  m={r.get("measureNumber"):>3} b={r.get("beat"):.2f}  '
          f'quality={r.get("quality")!r}  rootPc={r.get("rootPitchClass")}')
```

Report: which measure/beat pairs appear in music21 but not in our output?
Are the missing boundaries at beat 2 (half-note changes), beat 3, or beat 4?
This tells us whether the issue is specific to certain beat positions.

---

## Step 4 — Test: threshold reduction

The current Jaccard threshold is 0.6. Test lower values to see how they affect
region counts and BIR metrics.

**4A — Batch_analyze threshold test**

Locate where the threshold is set or read in `tools/batch_analyze.cpp`. If it
is hardcoded, create a temporary version with threshold 0.50 and 0.45. Run on
the 5 most under-segmented chorales from Step 2:

```bash
# Example — adapt to actual code structure
./ninja_build_rel/batch_analyze.exe tools/corpus/bwvXX.xml \
    /tmp/bwvXX_t050.ours.json --preset Baroque --jaccard-threshold 0.50
```

If no CLI argument exists, document what change to the source would be needed.

Compare region counts with the current output and music21 reference.

**4B — Run full corpus with modified threshold**

If the threshold is accessible via `ChordAnalyzerPreferences` (which it is,
as `harmonicBoundaryJaccardThreshold`), check whether `run_bach_preset.py`
or the Baroque preset configuration can pass a lower value without changing
compiled code. If so, run:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir /tmp/corpus_t050 [--jaccard-threshold 0.50 if available]
cd C:\s\MS && python tools/analyze_inversion_errors.py \
    [--corpus-dir /tmp/corpus_t050]
```

Report BIR=true and BIR=false at threshold 0.50 and 0.45.

**Hard stop**: If BIR=false increases by more than 5 at any threshold,
do not lower the threshold — the over-segmentation is introducing regressions.

---

## Step 5 — Test: fix the running accumulation

The running-accumulation strategy (`prevBits = union`) compounds pitch-class
sets across windows. Test the alternative: compare each window only against
the immediately preceding window (no accumulation across non-boundary windows):

In the boundary detection loop, find the line:
```cpp
prevBits = uni;   // or: prevBits = prevBits | currentBits;
```

Change to:
```cpp
prevBits = currentBits;   // compare sequentially, no accumulation
```

Make this change in BOTH implementations (notationcomposingbridgehelpers.cpp
and batch_analyze.cpp). Build:

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Run region count comparison (Step 2 script) and BIR validation:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report:
- Mean region count diff vs music21 (should move toward 0)
- BIR=true and BIR=false (must not increase BIR=false by more than 5)
- Whether the specific boundaries missed in Step 3 are now detected

If both the accumulation fix AND a threshold reduction improve results, combine
them and test the combination.

---

## Step 6 — Run both test suites

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 and 53/53. Pipeline snapshot tests may fail if boundary
changes alter the 10-score output — verify the new boundaries are correct before
refreshing:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Only refresh goldens after confirming the new boundaries are genuine improvements,
not regressions.

---

## Step 7 — Jazz validation and commit (only if Steps 4–6 pass)

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz BIR=false must not exceed 75.

Restore Baroque afterward:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

If all pass, commit both implementation files with message:
```
Boundary detection: fix under-segmentation in detectHarmonicBoundariesJaccard

[Describe the specific change: threshold reduction / accumulation strategy /
both — fill in from actual implementation]

Previously, [describe old behaviour]. The running-accumulation strategy
(prevBits = union across non-boundary windows) caused the pitch-class set to
grow large enough that genuinely new chords shared enough pitch classes to
suppress the boundary signal.

[Describe fix and effect on region counts and BIR metrics]

Applied identically to notationcomposingbridgehelpers.cpp and batch_analyze.cpp.
Note: §2.10 TODO for consolidating both implementations remains open (Task #58).

BIR=true: N→N  BIR=false: N→N  Jazz BIR=false: N
Mean region count diff vs music21: N→N
```

Update `build_and_test.md` with new baselines.

---

## Step 8 — Report to Cowork

```
Step 1 — Implementation comparison:
  Implementations identical: [yes / diverged — describe]
  Accumulation line: [exact code, file, line N]
  Threshold variable: [name, location]

Step 2 — Region count diagnosis:
  Mean diff (ours − music21): [value]
  Under-segmented (diff < -2): N chorales
  Over-segmented  (diff >  2): N chorales
  Close match (|diff| ≤ 2): N chorales

Step 3 — Specific case:
  Worst-case chorale: [stem]
  Missed boundaries at: [list of m/b pairs]
  Pattern: [beat 2 / beat 3 / beat 4 / irregular]

Step 4 — Threshold test:
  Threshold 0.50: BIR=true=N  BIR=false=N  mean diff=N
  Threshold 0.45: BIR=true=N  BIR=false=N  mean diff=N

Step 5 — Accumulation fix:
  BIR=true: 21→N  BIR=false: 128→N
  Mean region count diff: [before] → [after]
  Missed boundaries now detected: [yes / partial / no]

Step 6 — Tests:
  composing_tests: N/407
  notation_tests: N/53
  Pipeline snapshot: [updated / no change needed / failed]

Step 7 — Jazz: BIR=false=N  (must be ≤ 75)

Committed: [yes — hash] / [not committed — reason]
Fix applied: [threshold only / accumulation only / both]
```
