# Iteration 15: Eliminate `bestAlt` pointer — use `bestAltIdx` index throughout

## ⚠ Critical behaviour rules

- Pure refactoring — zero behaviour change.
- Build + all tests + corpus BIR numbers must match Iteration 14 baselines exactly.
- If anything deviates: STOP and report verbatim.

---

## Background

In `chordanalyzer.cpp`, the gate block holds two parallel variables for the
best clean alternative:

```cpp
const ChordAnalysisResult* bestAlt = nullptr;   // pointer into results[]
size_t bestAltIdx = 0;                           // index into results[]
```

`bestAlt` is a raw pointer into `results`, a `std::vector`. The FM2 fallback
(lines ~2021–2032) calls `results.push_back(buildResult(rc))`, which can
reallocate the vector and silently invalidate `bestAlt`. Today this is not a
live bug because `didEnharmonicFlip = true` is always set before any subsequent
`bestAlt` access. But the invariant is implicit and fragile — a future gate
added after FM2 that reads `bestAlt` without checking `didEnharmonicFlip` would
dereference garbage.

The fix: eliminate `bestAlt` entirely. `bestAltIdx` (a stable index) already
exists alongside it. Replace every `bestAlt->identity.X` with
`results[bestAltIdx].identity.X` and change the sentinel from `bestAlt == nullptr`
to `bestAltIdx < results.size()` (consistent with `halfDimAltIdx` already using
`results.size()` as its sentinel).

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=100, BIR=false=788

---

## Step 2 — Read and confirm current state

Read `src/composing/analysis/chord/chordanalyzer.cpp` around lines 1967–2144.
Confirm and report:

A. The exact line where `const ChordAnalysisResult* bestAlt = nullptr;` is declared.
B. The exact line where `size_t bestAltIdx = 0;` is declared.
C. Every line that reads `bestAlt->` — list all of them.
D. The exact line of `if (bestAlt != nullptr) {`.
E. Confirm `bestAltIdx` is set at the same point `bestAlt` is set (inside the
   search loop), and that no code sets `bestAltIdx` without also setting `bestAlt`.

Report before proceeding.

---

## Step 3 — Make the changes

All changes are in `src/composing/analysis/chord/chordanalyzer.cpp`.

### 3a — Change `bestAltIdx` sentinel

Change the declaration of `bestAltIdx` from:
```cpp
size_t bestAltIdx = 0;
```
To:
```cpp
size_t bestAltIdx = results.size();
```

### 3b — Remove `bestAlt` declaration

Remove the line:
```cpp
const ChordAnalysisResult* bestAlt = nullptr;
```

### 3c — Remove `bestAlt` assignment in search loop

In the search loop, the line:
```cpp
bestAlt = &alt;
```
(which appears alongside `bestAltIdx = i;`) — remove it entirely.

### 3d — Change the guard

Change:
```cpp
if (bestAlt != nullptr) {
```
To:
```cpp
if (bestAltIdx < results.size()) {
```

### 3e — Replace all `bestAlt->identity.X` with `results[bestAltIdx].identity.X`

For every occurrence of `bestAlt->identity.X` identified in Step 2C, replace it
with `results[bestAltIdx].identity.X` (substituting the actual field name `X`).

Do NOT change anything else — no logic, no reordering, no reformatting of
surrounding lines.

Report the exact lines changed for each of 3a–3e.

---

## Step 4 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected (must match exactly):
- Build: pass
- Composing tests: 407/407, RealDiff ≤ 4
- Notation tests: 53/53
- Pipeline snapshot tests: 11/11, no mismatches
- BIR=true: 100
- BIR=false: 788

Any deviation: STOP and report verbatim.

---

## Step 5 — Push

```
cd C:\s\MS && git add -A && git commit -m "Iter 15: eliminate bestAlt pointer, use bestAltIdx index (refactor, no behaviour change)" && git push
```

---

## Step 6 — Report

```
State (A–E confirmed):
  bestAlt declared at:      line N
  bestAltIdx declared at:   line N
  bestAlt-> occurrences:    lines N, N, N, ...
  if (bestAlt != nullptr):  line N
  bestAltIdx set with bestAlt: yes

Changes:
  3a bestAltIdx sentinel:   line N (was 0, now results.size())
  3b bestAlt removed:       line N
  3c bestAlt= removed:      line N
  3d guard changed:         line N
  3e replacements:          lines N, N, N, ...

Build:                    pass / fail
Composing tests:          407/407, RealDiff=N
Notation tests:           53/53
Pipeline snapshot tests:  11/11, no mismatches
BIR=true:                 100
BIR=false:                788
GitHub push:              done / commit hash
Unexpected findings:      none / <describe>
```
