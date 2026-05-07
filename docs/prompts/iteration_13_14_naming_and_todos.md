# Iterations 13 + 14: Naming fix + §2.10 TODO comments

## ⚠ Critical behaviour rules

- Pure text changes — zero behaviour change.
- Build + all tests must be identical to Iteration 12 baselines.
- If the build fails or any test regresses: STOP and report verbatim.

---

## Background

Two small housekeeping changes identified in the comprehensive code audit:

**Iter 13** — Variable `gSupersonicPc` (chordanalyzer.cpp line 2177) is a typo.
"Supersonic" means faster than sound. The intended term is "supertonic" (2nd scale
degree). The computation `(keyTonicPc + 2) % 12` is musically correct; only the
name is wrong.

**Iter 14** — ARCHITECTURE.md §2.10 rule 4 states: "Any mirrored code must be
marked with a TODO comment referencing this rule." The batch_analyze.cpp version
of the duplicated helpers has a block comment at lines 399–442 acknowledging §2.10.
The bridge side (`notationcomposingbridgehelpers.cpp`) does NOT have equivalent
comments on `collectRegionTones` or `detectHarmonicBoundariesJaccard`, violating
this rule. `regionMetricWeightForBeatType` in `notationcomposingbridgehelpers.h`
is already correctly marked.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=100, BIR=false=788

---

## Step 2 — Iter 13: Rename `gSupersonicPc` → `gSupertonicPc`

In `src/composing/analysis/chord/chordanalyzer.cpp`, line 2177:

Change:
```cpp
                const int gSupersonicPc   = (keyTonicPc + 2) % 12;
```
To:
```cpp
                const int gSupertonicPc   = (keyTonicPc + 2) % 12;
```

Also update the single use of `gSupersonicPc` on line 2180:
```cpp
                        || results[halfDimAltIdx].identity.rootPc == gSupersonicPc)) {
```
To:
```cpp
                        || results[halfDimAltIdx].identity.rootPc == gSupertonicPc)) {
```

Report the exact lines changed.

---

## Step 3 — Iter 14: Add §2.10 TODO comments in bridge helpers

In `src/notation/internal/notationcomposingbridgehelpers.cpp`, immediately before
the `collectRegionTones` function definition (currently at approximately line 796),
add:

```cpp
// TODO (ARCHITECTURE.md §2.10 / §4.1c): duplicate of batch_analyze.cpp's
// collectRegionTones(). Move to src/composing/ with a note-provider interface
// so bridge and batch_analyze call one implementation.
```

In the same file, find `detectHarmonicBoundariesJaccard` (search for the function
definition, not calls to it). Immediately before its definition, add:

```cpp
// TODO (ARCHITECTURE.md §2.10 / §4.1c): duplicate of batch_analyze.cpp's
// detectHarmonicBoundariesJaccard(). Move to src/composing/ with a note-provider
// interface so bridge and batch_analyze call one implementation.
```

Report the exact lines inserted for each.

---

## Step 4 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Expected (must match exactly):
- Build: pass
- Composing tests: 407/407, RealDiff ≤ 4
- Notation tests: 53/53
- Pipeline snapshot tests: 11/11, no mismatches

Any deviation: STOP and report verbatim.

---

## Step 5 — Push

```
cd C:\s\MS && git add -A && git commit -m "Iter 13+14: rename gSupersonicPc→gSupertonicPc; add §2.10 TODOs to bridge helpers" && git push
```

---

## Step 6 — Report

```
Changes:
  gSupersonicPc renamed at:              lines N, N
  collectRegionTones TODO inserted at:   line N
  detectHarmonicBoundariesJaccard TODO:  line N

Build:                    pass / fail
Composing tests:          407/407, RealDiff=N
Notation tests:           53/53
Pipeline snapshot tests:  11/11, no mismatches
GitHub push:              done / commit hash
Unexpected findings:      none / <describe>
```
