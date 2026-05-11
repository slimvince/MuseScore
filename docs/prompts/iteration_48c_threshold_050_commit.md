# Iteration 48c: Commit Jaccard threshold 0.50 as final baseline for deprecated algorithm

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=21, BIR=false=128. Jazz hard stop: BIR=false ≤ 75.

---

## Context

Iter 48b found that threshold 0.50 (with original accumulation strategy intact) may
improve BIR=false from 128 to 124 with no regression in BIR=true. The result was
from a session with corpus hygiene issues and cannot be fully trusted.

This iteration performs one clean, disciplined verification and commits if it passes.
The current detectHarmonicBoundariesJaccard algorithm is deprecated and will be
replaced (Task #62). This threshold change establishes the best achievable quality
floor for the current algorithm — a reference point against which the new algorithm
will be benchmarked.

---

## Step 1 — Clean build from committed state

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Regenerate and confirm baseline:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=21, BIR=false=128. Stop if this does not match.

---

## Step 2 — Apply threshold 0.50

Change the Jaccard threshold from 0.60 to 0.50 in BOTH locations:
- `src/notation/internal/notationcomposingbridgehelpers.cpp` (line ~208 or wherever
  `harmonicBoundaryJaccardThreshold` is read or the literal 0.6 appears in the
  boundary detection function)
- `tools/batch_analyze.cpp` (wherever the threshold is set or read)

Do NOT change the accumulation strategy. Do NOT change anything else.

Add a comment at each change site:
```cpp
// Threshold lowered from 0.60 to 0.50 (Iter 48c).
// detectHarmonicBoundariesJaccard is deprecated (Task #62 — replacement planned).
// 0.50 is the best achievable parameter for this algorithm; kept as quality baseline.
```

---

## Step 3 — Build and Baroque validation

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=21, BIR=false ≤ 128 (hoping for 124).
Hard stop: if BIR=false > 128 or BIR=true > 21, revert and close this iteration.

---

## Step 4 — Test suites

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 and 53/53.

If pipeline_snapshot_tests fail (boundary changes alter output):
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Only refresh goldens if the changed boundaries are genuine improvements.

---

## Step 5 — Jazz validation

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz BIR=false must not exceed 75. Hard stop if it does — revert and close.

Restore Baroque corpus after Jazz run:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 6 — Commit (only if Steps 1–5 all pass)

```
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add tools/batch_analyze.cpp
git commit -m "Boundary detection: lower Jaccard threshold 0.60 → 0.50

Reduces BIR=false from 128 to N with no regression in BIR=true (21→21).

0.50 is the best achievable threshold for the running-accumulation strategy.
detectHarmonicBoundariesJaccard is deprecated (Task #62 — replacement
architecture planned). This change establishes the algorithm's quality
ceiling as a benchmark for the replacement.

BIR=true: 21→21  BIR=false: 128→N  Jazz BIR=false: N"
```

Update `build_and_test.md` with new baselines.

---

## Step 7 — Report to Cowork

```
Step 1 — Baseline confirmed: BIR=true=21  BIR=false=128  [yes/no]

Step 3 — Baroque at 0.50:
  BIR=true: 21→N
  BIR=false: 128→N

Step 4 — Tests:
  composing_tests: N/407
  notation_tests: N/53
  Pipeline snapshot: [updated / no change / failed]

Step 5 — Jazz BIR=false: N  (must be ≤ 75)

Committed: [yes — hash] / [not committed — reason]
```
