# Iteration 48b: Boundary detection — threshold reduction data point

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=21, BIR=false=128. Jazz hard stop: BIR=false ≤ 75.

Do NOT commit. Revert all changes after collecting data.

---

## Context

Iter 48 found:
- Accumulation fix alone (prevBits = currentBits) caused regression: BIR=true 21→24, BIR=false 128→139. Reverted.
- Step 4 (threshold reduction with original accumulation intact) was not completed.
- This iteration runs Step 4 as a data point only. No fix will be committed.

The accumulation strategy (`prevBits = union`) remains unchanged throughout this iteration.

---

## Step 1 — Locate threshold in both files

Confirm the exact location where `harmonicBoundaryJaccardThreshold` (or equivalent) is read or hardcoded in:
- `src/notation/internal/notationcomposingbridgehelpers.cpp`
- `tools/batch_analyze.cpp`

Check whether `run_bach_preset.py` or the Baroque preset JSON/config can pass a threshold value without changing compiled code. If yes, use that. If no, proceed to Step 2.

---

## Step 2 — Test threshold 0.50

In both files, change the Jaccard threshold from 0.6 to 0.50. Keep the accumulation strategy (`prevBits = union` / `previousBits = unionBits`) completely unchanged.

Build:
```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Run corpus and BIR check:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Record BIR=true and BIR=false.

---

## Step 3 — Test threshold 0.45

Change threshold to 0.45 in both files (accumulation still unchanged). Build and run corpus again.

Record BIR=true and BIR=false.

---

## Step 4 — Revert everything

Restore threshold to 0.60 in both files. Build once more to confirm baseline is restored:
```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Confirm BIR=true=21, BIR=false=128.

---

## Step 5 — Report to Cowork

```
Threshold 0.60 (baseline):  BIR=true=21  BIR=false=128
Threshold 0.50:             BIR=true=N   BIR=false=N
Threshold 0.45:             BIR=true=N   BIR=false=N

Baseline restored: [yes / no]

Interpretation: [threshold reduction helps / neutral / regression]
```

Do NOT commit anything. This is a data-collection step only.
