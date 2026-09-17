# CC Instruction — E2b fixup: complete harmonicfunctionlayer.h

**Context:** Cowork made partial E2b changes that cannot be built. The following
files are already correct — do NOT touch them:

- `src/composing/analysis/chord/chordanalyzer.h` — forward declaration at L38-40,
  `captureScoringSnapshot` field at L488. Correct.
- `src/composing/analysis/chord/chordanalyzer.cpp` — D3 (capacity reserve at
  ~L2279), D1 (cell capture block in joint-scoring loop), D2 (final-state capture
  after variant-choice block). Correct.

**The only broken file:** `src/composing/analysis/function/harmonicfunctionlayer.h`

---

## What went wrong

The file currently ends at 87 lines. The last line is:

```
// -----------------
```

This is a truncated `// -----...-----` divider. The `ScoringCell` and
`ScoringSnapshot` struct definitions were never written. The `#include <vector>`
at L37 was added (needed by the structs' `std::vector` fields) but the structs
themselves are missing.

**Verify first:**

```bash
wc -l /sessions/eloquent-confident-einstein/mnt/MS/src/composing/analysis/function/harmonicfunctionlayer.h; echo "exit:$?"
tail -5 /sessions/eloquent-confident-einstein/mnt/MS/src/composing/analysis/function/harmonicfunctionlayer.h; echo "exit:$?"
```

Confirm the file is 87 lines and ends with `// -----------------`.

---

## What to do

### Step 1 — Fix the truncated comment and add the structs

The file currently ends (line 87) with `// -----------------` which is a broken
divider. The closing `} // namespace` brace is also missing.

Replace the final two lines (the broken divider + whatever follows, which is
nothing — check that line 86 is the closing `};` of `wDimBonus`) and append the
complete structs block and the closing namespace brace.

Read lines 80-87 first to confirm the exact ending, then apply this edit:

Replace the broken trailing line(s) so the file ends correctly:

```
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
    double wDimDelta;           ///< 0 in cellsWithoutWDim; >= 0 in cellsWithWDim.

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
    ///   bassCandidates.size() * 12 * N_templates  (typically <= 4 * 12 * 17 = 816).
    /// The two cubes share all fields except wDimDelta; they also share wSeqBonus
    /// (it is added before wDimDelta and is therefore identical in both variants).
    /// Pass B (step bonuses) is NOT reflected here -- cells hold pre-step scores.
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

} // namespace mu::composing::function
```

The key mechanics:
- Line 87 (`// -----------------`) must be REPLACED (not appended-to) — delete it
  and write the full block above in its place.
- The closing `} // namespace mu::composing::function` brace is currently absent
  from the file — it must be present at the end.
- Do NOT add a second `} // namespace` if the file already has one — read first.

Read lines 82-87 of the current file, then apply the edit.

---

### Step 2 — Build

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

---

### Step 3 — Run all three test suites

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2b.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2b.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2b.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2b.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2b.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2b.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407, 52/52, 11/11 — byte-identical to HEAD 80a7adf32e.**
If any count changes, revert everything (`git checkout -- .`) and report.

---

### Step 4 — Commit

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.h \
  src/composing/analysis/chord/chordanalyzer.h \
  src/composing/analysis/chord/chordanalyzer.cpp; echo "exit:$?"

cd C:\s\MS && git commit -m "E2b: expose scoring snapshot in analyzeChord() (opt-in)

Add ScoringCell / ScoringSnapshot structs to harmonicfunctionlayer.h.
Add prefs.captureScoringSnapshot pointer to ChordAnalyzerPreferences.

When non-null, analyzeChord() populates a pre-step-bonus scoring cube for
both the with-wDim and without-wDim variants (ScoringSnapshot::cellsWithWDim
and cellsWithoutWDim), covering all bassCandidates x 12 rootPcs x N templates.
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

1. Confirm harmonicfunctionlayer.h now has both structs and the closing namespace brace
2. Test results (407/407, 52/52, 11/11)
3. Commit hash
4. Confirm harmonicfunctionlayer.cpp was NOT modified (no changes needed there)
