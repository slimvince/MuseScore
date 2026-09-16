# CC Instruction — E2b: Expose scoring snapshot

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 and §10.

**Current state:** Branch `master`, HEAD `80a7adf32e`, working tree clean.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**This instruction introduces zero behavioral change.** The snapshot is populated
only when `prefs.captureScoringSnapshot != nullptr`. All existing call sites pass
nothing, so the hot path is unaffected. Every test must be identical before and after.

---

## Background

E2c will move the three progression signals (`rootContinuityBonus`, `w_seq`, `w_dim`)
out of `analyzeChord()` and into `applyHarmonicFunction()`. To preserve zero behavioral
change, the function layer must be able to redo bass selection, the `w_dim` dual-scoring
quality guard, and the threshold filter with any combination of those signals suppressed.

`ChordAnalysisResult` alone is too coarse: the threshold filter uses the bonus-inclusive
winner score, `rootContinuityBonus` is multiplied by `complexityFactor × augFactor`
(so simple subtraction from the final score is wrong), and the without-wDim variant's
data is discarded before `analyzeChord()` returns.

E2b adds an opt-in `ScoringSnapshot` that captures the full pre-step-bonus scoring
cube for both the with-wDim and without-wDim variants. E2c will consume it.

---

## Part A — Read before touching any file

In `chordanalyzer.cpp`, read the joint-scoring loop (~L2278–2447) closely. Report:

1. The exact variable names, at the point of `push_back` into `perBassWithout` and
   `perBassWith`, for the following quantities (the investigation confirmed these
   exist; find their names):
   - `basisIndepMatrix[rootPc][tplIdx]` (the full basisIndep value, including
     the `rootContinuityBonus` contribution)
   - `basisDep` (the bass-dependent delta, including `appliedBassBonus`)
   - `complexityFactorMatrix[rootPc][tplIdx]`
   - `augFactorMatrix[rootPc][tplIdx]`
   - `wCompleteBonus` (the `wCompleteBonus(...)` return value for this cell)
   - `wSeqBonus(candRootPc)` (the lambda return value; same for both variants)
   - `wDimDelta` (the wDimBonus lambda return value; 0 for the without-wDim cell)
   - `appliedBassBonus` (the bass-root bonus component, used for threshold
     de-inflation)
   - `bassCandidates[bi].pc` (the bass PC for the current outer loop index `bi`)

2. The exact line numbers of the two `push_back` calls (one for `perBassWithout`,
   one for `perBassWith`).

3. The exact line numbers of the post-variant-choice block (~L2436–2447) where
   `winnerIdx`, `acceptPostBonus`, and `rawCandidates` are finalised.

4. Where `distinctPcs` is first defined in `analyzeChord()`. Confirm it is in
   scope throughout the joint-scoring loop.

5. The current signature of `analyzeChord()` — specifically whether it is a member
   function with a `const` qualifier, and what the full parameter list looks like —
   to confirm that adding a field to `ChordAnalyzerPreferences` is the right way
   to pass the snapshot pointer (vs. an extra parameter).

---

## Part B — Add structs to `harmonicfunctionlayer.h`

Add the following inside `namespace mu::composing::function`, after the existing
bonus-function declarations:

```cpp
// -----------------------------------------------------------------------
// Scoring snapshot (E2b) — captured by analyzeChord() when
// prefs.captureScoringSnapshot is non-null. Consumed by applyHarmonicFunction()
// in E2c to redo joint scoring with progression signals suppressed.
// -----------------------------------------------------------------------

/// One (bass, root, template) scoring cell, pre-step-bonus.
/// E2c uses the decomposed fields to rebuild the score with any subset of
/// {rootContinuityBonus, w_seq, w_dim} suppressed and then re-runs Pass B.
struct ScoringCell {
    // Identifiers — locate the cell in the (bass, root, template) cube.
    int                    bassPc;
    int                    rootPc;
    int                    tiePriority;        ///< Template index; needed by E2c for
                                               ///< the Pass B m7-family guard look-up.
    analysis::ChordQuality quality;

    // Bass-independent pitch evidence (basisIndepMatrix[rootPc][tiePriority]).
    // INCLUDES the rootContinuityBonus contribution (if it fired for this rootPc).
    // E2c deducts:
    //   fn::rootContinuityBonus(rootPc, ctx.previousRootPc, prefs.rootContinuityBonus)
    // before re-multiplying, because that bonus is folded into basisIndep and
    // thus scaled by complexityFactor × augFactor (simple score subtraction is wrong).
    double basisIndep;

    double basisDep;            ///< Bass-dependent delta.
    double complexityFactor;    ///< complexityFactorMatrix[rootPc][tiePriority].
    double augFactor;           ///< augFactorMatrix[rootPc][tiePriority].

    // Additive terms (applied AFTER the cf × af multiplication).
    // Simple addition/subtraction by E2c is correct for all of these.
    double wCompleteBonus;      ///< 0 or kWComplete.
    double wSeqBonus;           ///< Identical across both cubes (neutral w.r.t. wDim).
    double wDimDelta;           ///< 0 in cellsWithoutWDim; ≥ 0 in cellsWithWDim.

    // Bass bonus, used for threshold de-inflation: threshold = (bestScore -
    // appliedBassBonus) * kScoreThresholdRatio. Must match what the scorer used.
    double appliedBassBonus;
};

/// Full per-region scoring snapshot. Populated inside analyzeChord() when
/// prefs.captureScoringSnapshot != nullptr. Contains nothing that is not
/// already computable from the analyzeChord() inputs; it exists only so E2c
/// does not have to re-run the full pitch scorer.
struct ScoringSnapshot {
    /// Scoring cubes for both the with-wDim and without-wDim variants.
    /// Layout: cells are stored in (bass, root, template) order — bass is the
    /// outer dimension (index bi), rootPc the middle (0..11), tiePriority the
    /// inner (0..N_templates-1). Total cells per cube:
    ///   bassCandidates.size() × 12 × N_templates  (typically ≤ 4 × 12 × 17 = 816).
    /// The two cubes share all fields except wDimDelta; they also share wSeqBonus
    /// (it is added before wDimDelta and is therefore identical in both variants).
    /// Pass B (step bonuses) is NOT reflected here — cells hold pre-step scores.
    /// E2c must re-run Pass B after re-scoring.
    std::vector<ScoringCell> cellsWithWDim;
    std::vector<ScoringCell> cellsWithoutWDim;

    /// Scorer's actual decisions (useful for E2c cross-check and debugging).
    int  chosenBassPc        { -1 };  ///< bassCandidates[winnerIdx].pc after quality guard
    bool acceptedWithWDim    { false }; ///< true iff the with-wDim variant was accepted
    int  winnerBassPcWith    { -1 };  ///< bass chosen by the with-wDim variant
    int  winnerBassPcWithout { -1 };  ///< bass chosen by the without-wDim variant

    /// Needed by E2c for w_seq / w_dim gate conditions.
    int  distinctPcs         { 0 };
};
```

---

## Part C — Add opt-in pointer to `ChordAnalyzerPreferences`

In `chordanalyzer.h`, find `ChordAnalyzerPreferences` (or `ChordAnalyzerPrefs`).
Add one field at the end:

```cpp
/// Set to a non-null pointer to receive a full scoring snapshot for E2c.
/// When null (default), no snapshot is allocated and the hot path is unchanged.
function::ScoringSnapshot* captureScoringSnapshot { nullptr };
```

This requires `#include "composing/analysis/function/harmonicfunctionlayer.h"` at
the top of `chordanalyzer.h` (or a forward declaration — use whichever the codebase
prefers for the other types already included there). If a forward declaration suffices,
use that to keep the header lean.

---

## Part D — Populate the snapshot in `analyzeChord()`

### D1 — Pre-step cells (Pass A capture)

Inside the joint-scoring loop, at the point where `perBassWithout` and `perBassWith`
are populated (identified in Part A), add a snapshot cell capture block gated on
`prefs.captureScoringSnapshot`:

```cpp
if (prefs.captureScoringSnapshot) {
    fn::ScoringCell cell;
    cell.bassPc          = bassCandidates[bi].pc;  // adjust variable name to match Part A
    cell.rootPc          = rootPc;
    cell.tiePriority     = tplIdx;                 // adjust if template loop variable differs
    cell.quality         = /* quality of this (rootPc, tplIdx) template */;
    cell.basisIndep      = basisIndepMatrix[rootPc][tplIdx];   // adjust to Part A names
    cell.basisDep        = /* basisDep local variable */;      // adjust to Part A names
    cell.complexityFactor = complexityFactorMatrix[rootPc][tplIdx];
    cell.augFactor        = augFactorMatrix[rootPc][tplIdx];
    cell.wCompleteBonus  = /* wCompleteBonus local / lambda result */;
    cell.wSeqBonus       = /* fn::wSeqBonus(...) lambda result */;
    cell.appliedBassBonus = /* appliedBassBonus local variable */;

    // Without-wDim cell: wDimDelta is always 0.
    cell.wDimDelta = 0.0;
    prefs.captureScoringSnapshot->cellsWithoutWDim.push_back(cell);

    // With-wDim cell: same except wDimDelta.
    cell.wDimDelta = wDimDelta;   // the wDimBonus lambda result; adjust variable name
    prefs.captureScoringSnapshot->cellsWithWDim.push_back(cell);
}
```

Place this block IMMEDIATELY BEFORE the existing `push_back` calls into
`perBassWithout` and `perBassWith`, so all local variables for this cell are
still in scope. Adjust every variable name to match what Part A found.

**Important:** The `quality` field should come from `templates[tplIdx].quality`
(or the equivalent in the current template-lookup code). Confirm Part A's read
gives you the template quality variable name.

### D2 — Final state capture (post-variant-choice)

After the variant-choice block (~L2436-2447), add:

```cpp
if (prefs.captureScoringSnapshot) {
    prefs.captureScoringSnapshot->distinctPcs        = distinctPcs;
    prefs.captureScoringSnapshot->acceptedWithWDim   = acceptPostBonus;
    // chosenBassPc is bassCandidates[winnerIdx].pc after the choice.
    // winnerBassPcWith / winnerBassPcWithout come from winnerIdxWith / winnerIdxWithout
    // tracked at L2305-2306 (from the E2 investigation). Adjust variable names.
    prefs.captureScoringSnapshot->chosenBassPc        = bassCandidates[winnerIdx].pc;
    prefs.captureScoringSnapshot->winnerBassPcWith    = bassCandidates[winnerIdxWith].pc;
    prefs.captureScoringSnapshot->winnerBassPcWithout = bassCandidates[winnerIdxWithout].pc;
}
```

Again, adjust all variable names to match what Part A found.

### D3 — Reserve capacity (performance)

At the start of `analyzeChord()`, after `bassCandidates` is fully constructed,
add a capacity reservation so snapshot population doesn't trigger repeated
reallocations:

```cpp
if (prefs.captureScoringSnapshot) {
    const int nCells = static_cast<int>(bassCandidates.size()) * 12 * static_cast<int>(templates.size());
    prefs.captureScoringSnapshot->cellsWithWDim.clear();
    prefs.captureScoringSnapshot->cellsWithoutWDim.clear();
    prefs.captureScoringSnapshot->cellsWithWDim.reserve(nCells);
    prefs.captureScoringSnapshot->cellsWithoutWDim.reserve(nCells);
}
```

---

## Part E — Build and verify zero behavioral change

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2b.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2b.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2b.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2b.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2b.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2b.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407, 52/52, 11/11 — byte-identical to baseline. If any count
changes at all, revert everything.**

Do NOT run BIR. The snapshot is opt-in and no caller sets the pointer; the scoring
path is unchanged.

---

## Part F — Commit

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.h \
  src/composing/analysis/function/harmonicfunctionlayer.cpp \
  src/composing/analysis/chord/chordanalyzer.h \
  src/composing/analysis/chord/chordanalyzer.cpp; echo "exit:$?"

cd C:\s\MS && git commit -m "E2b: expose scoring snapshot in analyzeChord() (opt-in)

Add ScoringCell / ScoringSnapshot structs to harmonicfunctionlayer.h.
Add prefs.captureScoringSnapshot pointer to ChordAnalyzerPreferences.

When non-null, analyzeChord() populates a pre-step-bonus scoring cube for
both the with-wDim and without-wDim variants (ScoringSnapshot::cellsWithWDim
and cellsWithoutWDim), covering all bassCandidates × 12 rootPcs × N templates.
Also records: distinctPcs, acceptedWithWDim, chosenBassPc, winnerBassPcWith/
Without.

All existing callers pass prefs without the new field (defaults to nullptr),
so the hot path is completely unchanged.

E2c will set prefs.captureScoringSnapshot and use it to redo joint scoring
with {rootContinuityBonus, w_seq, w_dim} suppressed in the scorer and applied
in applyHarmonicFunction() instead.

Zero behavioral change. All tests identical to HEAD 80a7adf32e."; echo "exit:$?"
```

---

## Report back

1. Exact variable names found in Part A (for each of the 9 quantities listed)
2. Line numbers of the two push_back calls and the post-variant-choice block
3. How the `ChordAnalyzerPreferences` include was handled (full include vs forward
   declaration); any include-order complications
4. Whether `quality` was read from the template array or from another in-scope variable
5. Test results — confirm byte-identical to baseline
6. Commit hash
7. Any deviation from the prescribed struct fields (report but do not change the
   struct design without flagging)
