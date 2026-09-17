# CC Instruction: Phase E — Eliminate explorationMode dual-path

## Context

This is Phase E Step 5 architectural work, continuing from `1bfc64d18c`.
See `docs/redesign_plan.md` Step 5 and `COWORK_HANDOFF.md` "Architecture direction."

**Goal:** Remove the `explorationMode` flag from all bonus-function signatures and from
`ChordAnalyzerPreferences`. The flag currently creates a hidden dual-path inside the
competition pipeline: five separate functions each check it and suppress themselves.
After this change, the bonus functions are stateless and pure; the control point lives
in one place.

**Constraint:** Byte-identical output on all tests and both corpora. No new scoring
logic. No behaviour changes.

---

## What explorationMode currently does

`explorationMode = true` is set by `harmonicsegmenter.cpp` at two sites (lines ~347
and ~704) before calling `analyzeChord`. It flows through `ChordAnalyzerPreferences`
to `applyHarmonicFunction`, where it suppresses five things:

| Function / gate | Effect when explorationMode=true |
|---|---|
| `wSeqBonus` | Returns 0.0 always |
| `wDimBonus` | Returns 0.0 always |
| `wStepInBonus` | Returns 0.0 always |
| `wStepOutBonus` | Returns 0.0 always |
| `gateRZeroesRootContinuity` | Returns false always (Gate R never fires) |

`rootContinuityBonus` is deliberately NOT suppressed — segmentation depends on it.

---

## Task 1 — Read the current code (mandatory before touching anything)

```
sed -n '340,360p' C:/s/MS/src/composing/analysis/harmony/harmonicsegmenter.cpp
sed -n '695,710p' C:/s/MS/src/composing/analysis/harmony/harmonicsegmenter.cpp
sed -n '470,480p' C:/s/MS/src/composing/analysis/chord/chordanalyzer.h
sed -n '44,96p'   C:/s/MS/src/composing/analysis/function/harmonicfunctionlayer.cpp
sed -n '140,150p' C:/s/MS/src/composing/analysis/function/harmonicfunctionlayer.cpp
sed -n '260,310p' C:/s/MS/src/composing/analysis/function/harmonicfunctionlayer.cpp
sed -n '120,148p' C:/s/MS/src/composing/analysis/function/harmonicfunctionlayer.h
sed -n '220,235p' C:/s/MS/src/composing/analysis/function/harmonicfunctionlayer.h
sed -n '2960,2975p' C:/s/MS/src/composing/analysis/chord/chordanalyzer.cpp
```

Confirm:
1. The two `harmonicsegmenter.cpp` sites match the description above.
2. The five functions/gates all check `explorationMode` exactly as described.
3. `applyHarmonicFunction` at line ~2968 of `chordanalyzer.cpp` is the sole call site
   that routes through `prefs` into the pipeline.
4. No other call sites for those bonus functions exist outside `harmonicfunctionlayer.cpp`
   and the unit tests in `gater_tests.cpp`.

Report any discrepancies before proceeding.

---

## Task 2 — Design: replace the flag with a ScoringPhase

Instead of `explorationMode` scattered across 5 function signatures, introduce a
single `ScoringPhase` enum in `harmonicfunctionlayer.h`:

```cpp
enum class ScoringPhase : uint8_t {
    Segmentation, ///< Boundary exploration — progression signals suppressed; rcb active.
    Final         ///< Per-region final scoring — all signals active.
};
```

The phase is passed as a single new parameter to `applyHarmonicFunction`. All five
bonus functions and `gateRZeroesRootContinuity` lose their `explorationMode` parameter
entirely — they become stateless. Inside `applyHarmonicFunction`, the phase is checked
once at the entry point of Pass A (before the per-cell loop), and when phase is
`Segmentation` the four bonuses are simply not called and Gate R is skipped.

Exact changes:

### `harmonicfunctionlayer.h`
1. Add the `ScoringPhase` enum (before the free-function declarations).
2. Remove `explorationMode` from the signatures of `wSeqBonus`, `wDimBonus`,
   `wStepInBonus`, `wStepOutBonus`, `gateRZeroesRootContinuity`.
3. Add `ScoringPhase phase = ScoringPhase::Final` as the last parameter of
   `applyHarmonicFunction`.

### `harmonicfunctionlayer.cpp`
1. Remove `explorationMode` from the implementations of the five functions.
   Replace the `if (!jointScoringEnabled || explorationMode)` guards with just
   `if (!jointScoringEnabled)` (the `explorationMode` arm is gone).
   Replace the `return rcb > 0.0 && !explorationMode && ...` with
   `return rcb > 0.0 && ...` (the `!explorationMode` arm is gone).
2. In `applyHarmonicFunction`, add a phase check at the top of the Pass A per-cell
   loop:
   ```cpp
   const bool applyProgressionSignals = (phase == ScoringPhase::Final);
   ```
   Then gate the four bonus calls and the Gate R check on `applyProgressionSignals`:
   ```cpp
   if (gateRZeroesRootContinuity(cell, rcb) && applyProgressionSignals) {
       rcb = 0.0;
   }
   // ...
   scoreNoWDim += applyProgressionSignals
       ? wSeqBonus(cell.rootPc, ctx.nextRootPc, snapshot.distinctPcs,
                   snapshot.jointScoringEnabled)
       : 0.0;
   const double wDimDelta = applyProgressionSignals
       ? wDimBonus(cell.rootPc, cell.quality, ctx.nextRootPc, snapshot.distinctPcs,
                   snapshot.jointScoringEnabled)
       : 0.0;
   ```
   And in Pass B (step-bonus guard):
   ```cpp
   if (applyProgressionSignals) {
       applyStepBonusGuard(perBassWith, ...);
       applyStepBonusGuard(perBassWithout, ...);
   }
   ```
   **Check whether Pass B's step bonuses are also gated via explorationMode or only
   via jointScoringEnabled.** If they are already gated purely by jointScoringEnabled
   (i.e., explorationMode only affects them indirectly through the wStep functions
   which check it), confirm this and document. Do not suppress Pass B separately if
   it is already handled.

### `chordanalyzer.cpp`
At the `fn::applyHarmonicFunction(snapshot, fnCtx, prefs, results, chosenResult, gateCtxOut)`
call site (~line 2968), pass the phase directly from `prefs`:
```cpp
fn::applyHarmonicFunction(snapshot, fnCtx, prefs, results, chosenResult, gateCtxOut,
                          prefs.scoringPhase);
```
(`prefs.scoringPhase` replaces the old `prefs.explorationMode` bool — no translation needed.)

### `chordanalyzer.h`
Remove `bool explorationMode = false;` from `ChordAnalyzerPreferences`.
Update the doc-comment for that struct.

### `chordanalyzer.h`
Remove `bool explorationMode = false;` from `ChordAnalyzerPreferences`. Replace it with:
```cpp
fn::ScoringPhase scoringPhase = fn::ScoringPhase::Final;
```
Update the doc-comment to explain:
"Set to `fn::ScoringPhase::Segmentation` for boundary-exploration calls (suppresses
progression signals; rcb remains active). Default `fn::ScoringPhase::Final` for all
per-region analysis calls."

Note: `fn::ScoringPhase` is now defined in `harmonicfunctionlayer.h`, so
`chordanalyzer.h` must `#include` that header (check whether it already does — it
likely does via the existing `fn::applyHarmonicFunction` declaration dependency).

### `harmonicsegmenter.cpp`
At the two sites (~347 and ~704), replace `explorationMode = true` with
`scoringPhase = fn::ScoringPhase::Segmentation`. All other prefs fields stay untouched.

Summary of the full replacement:
```cpp
// Before:
explorePrefs.explorationMode = true;

// After:
explorePrefs.scoringPhase = fn::ScoringPhase::Segmentation;
```

(And the same for `sparsePrefs` at site 2.)

---

## Task 3 — Update the unit tests

`gater_tests.cpp` tests `gateRZeroesRootContinuity` with `explorationMode` as a
direct parameter. Remove that parameter from the calls; the test for "Gate R does
NOT fire in exploration mode" (Branch 4) should be deleted or converted to test
the `ScoringPhase::Segmentation` path via `applyHarmonicFunction` instead.

Read the test file first to understand the exact shape of the four branch tests:
```
cat C:/s/MS/src/composing/tests/gater_tests.cpp
```

The core invariant being tested (Gate R fires correctly on the right conditions) must
be preserved. Adapt the test, do not simply delete it.

---

## Task 4 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/phase_e_expl_compose.txt 2>&1; echo "exit:$?"
head -20 /tmp/phase_e_expl_compose.txt
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/phase_e_expl_notation.txt 2>&1; echo "exit:$?"
head -20 /tmp/phase_e_expl_notation.txt
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/phase_e_expl_snap.txt 2>&1; echo "exit:$?"
tail -20 /tmp/phase_e_expl_snap.txt
```

Expected: **416/416 · 52/52 · 11/11, zero snapshot diffs**.

---

## Task 5 — Corpus spot-check

```
cd C:\s\MS && python tools/characterise_bir_false.py > /tmp/bir_expl.txt 2>&1; echo "exit:$?"
cat /tmp/bir_expl.txt
```

BIR=false must not increase: Baroque ≤ 13, Jazz ≤ 7.

---

## Report format

Write findings to `C:\s\MS\cc_phase_e_exploration_mode_report.md`.

**Section 1 — Survey confirmation:** Confirm the five function signatures match the
description. Note exact line numbers. Report any discrepancy immediately.

**Section 2 — Pass B check:** Does `applyStepBonusGuard` need explicit
`applyProgressionSignals` gating, or is it already handled by `jointScoringEnabled`
inside `wStepInBonus`/`wStepOutBonus`? Explain.

**Section 3 — Implementation diff:** Show before/after for each changed site (10-line
context). List all files touched.

**Section 4 — Test results:** composing / notation / snapshot counts. Show any diffs.

**Section 5 — BIR:** Baroque and Jazz BIR=false after the change.

**Section 6 — Commit recommendation:** Propose a commit message. Do not commit until
Cowork confirms.
