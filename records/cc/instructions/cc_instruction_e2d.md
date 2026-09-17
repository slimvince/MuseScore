# CC Instruction — E2d: Enable progression-signal suppression (Pass B + cross-bass)

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 and §10.

**Current HEAD:** `20f992a5e7` (E2c-infra). Working tree clean.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**This instruction introduces zero behavioral change.** Two commits; each
must pass 407/407, 52/52, 11/11 byte-identical to HEAD. Revert if any test
changes.

---

## Context — why E2c Commit 2 failed

Read `C:\s\MS\cc_instruction_e2c.md` and `C:\s\MS\cc_instruction_e2d_investigate.md`
for full background. Two blockers:

**Blocker 1 — Pass B not replicated.**  
`applyStepBonusGuard()` adds ±0.10+0.10 = 0.20 max per candidate (root-position,
stepwise-bass-motion). This is large enough to flip the winner. The function layer
must replicate it after rescoring.

**Blocker 2 — Cross-bass winner absent from candidates[].**  
In suppression mode, candidates[] contains only one bass's cells (threshold is
already disabled → all 12×17=204 entries survive, but from one bass only). The
snapshot covers ALL basses from D1. When the signal-inclusive winner is from a
different bass, candidates[] has a cell with the same (tiePriority, rootPc) but
the wrong bassPc. The function layer must patch bassPc/bassTpc from the snapshot
cell. No chordanalyzer.cpp changes are needed; the patch already exists in the
E2c function-layer code.

---

## Design decisions

1. **`intervalCount` added to `ScoringCell`** — the m7-family guard checks
   `quality == Minor && intervals.size() == 4`. The function layer has no
   access to the templates array. Adding `intervalCount` (one int, populated
   from `templates[tplIdx].intervals.size()` in the D1 block) avoids
   hardcoding `tiePriority == 5` and remains correct if templates are added.

2. **Two-variant Pass B** — in suppression mode `wDimDelta = 0` in the
   snapshot, but the function layer re-introduces wDim when rescoring. The
   rescored `scoreWithWDim` and `scoreWithoutWDim` diverge for Dim/HalfDim
   cells. The m7-family guard comparison (`other.score >= cand.score - kStepBudget`)
   uses variant-specific scores. Pass B must therefore run separately for
   the with-wDim and without-wDim rescored variants — same logic, different
   score arrays.

3. **Pass B gate: `snapshot->jointScoringEnabled`** — same gate used by
   `wSeqBonus`/`wDimBonus`. When false, step bonus is 0.

4. **Pass B constants defined in function layer** — add `kWStepIn = 0.10`,
   `kWStepOut = 0.10`, `kStepBudget = kWStepIn + kWStepOut + 0.01` to
   `harmonicfunctionlayer.h` alongside existing `kWSeq`/`kWDim`.

5. **Iteration order** — `applyStepBonusGuard()` iterates perBass in
   (rootPc, tplIdx) row-major order (the push_back order in the inner loop).
   Snapshot cells within a bass group are in the same order. Iterate in that
   order to match the original.

6. **Cross-bass bassPc patch** — the function layer already has this code
   (from E2c). The fix for Blocker 2 is just ensuring it's reached — which
   it will be once Pass B (Blocker 1) is fixed.

7. **Two commits** — Commit 1: `intervalCount` + `HarmonicFunctionContext`
   extension + call-site wiring (suppressProgressionSignals still false →
   no-op). Commit 2: Pass B implementation + enable suppression.

---

## Part A — Mandatory reads before editing

### A1 — `applyStepBonusGuard` lambda body

Read `chordanalyzer.cpp` lines 2330–2368. Confirm:
- Exact field name for template intervals (used in `isMin7` check) —
  e.g. `tpl.intervals.size()` or `tpl.pcOffsets.size()`. Report the name.
- The exact expression for `compRootPc` — should be `(candBassPc - 3 + 12) % 12`.
- Whether `other.score` in the guard comparison refers to the current
  (already-potentially-modified) score in perBass, or a snapshot of the
  score before the loop started. (It uses the live value — confirm.)

### A2 — D1 cell-capture block

Confirm that `templates[tplIdx]` is in scope at the D1 block and that the
intervals field identified in A1 is accessible there.

### A3 — `applyHarmonicFunction()` current body

Read `harmonicfunctionlayer.cpp` in full. Confirm the current rescore logic,
the quality-guard loop, the winner lookup by (tiePriority, rootPc), and the
bassPc/bassTpc patch are all present from E2c. Identify the exact line where
the function returns early when `winnerIdx < 0`.

---

## Part B — Add `intervalCount` to `ScoringCell`

In `harmonicfunctionlayer.h`, inside `ScoringCell`, add after `quality`:

```cpp
int intervalCount { 0 };   ///< Number of intervals in the template
                            ///< (templates[tiePriority].intervals.size()).
                            ///< Used by E2d Pass B m7-family guard:
                            ///< isMin7 ≡ quality==Minor && intervalCount==4.
```

In the D1 cell-capture block in `chordanalyzer.cpp`, add after the quality
assignment:

```cpp
cell.intervalCount = static_cast<int>(tpl.<INTERVALS_FIELD>.size());
// Replace <INTERVALS_FIELD> with the name confirmed in Part A1.
```

---

## Part C — Extend `HarmonicFunctionContext`

In `harmonicfunctionlayer.h`, add to `HarmonicFunctionContext`:

```cpp
int previousBassPc { -1 };  ///< Bass PC of the preceding region (-1 = unknown).
                             ///< Required by E2d Pass B (wStepInBonus gate).
int nextBassPc     { -1 };  ///< Bass PC of the following region (-1 = unknown).
                             ///< Required by E2d Pass B (wStepOutBonus gate).
```

---

## Part D — Populate new context fields at all three call sites

In `regionanalyzer.cpp`, at each of the three `applyHarmonicFunction()` calls:

**Pass 1 (~L445 block):** `temporalCtx` has both fields (confirmed in
investigation). Add before the `applyHarmonicFunction()` call:

```cpp
fnCtx.previousBassPc = temporalCtx.previousBassPc;
fnCtx.nextBassPc     = temporalCtx.nextBassPc;
```

(The local `fnCtx` variable — or whatever the `HarmonicFunctionContext` local
is named — was established in E1. Find its exact name first.)

**Pass 2 and Pass 2b (~L649 and ~L837 blocks):** same pattern, using `subCtx`
instead of `temporalCtx`.

---

## Part E — Define step-bonus constants in `harmonicfunctionlayer.h`

After the existing `kWSeq` and `kWDim` constants, add:

```cpp
inline constexpr double kWStepIn   = 0.10;  ///< Stepwise-bass step-in bonus (E2d)
inline constexpr double kWStepOut  = 0.10;  ///< Stepwise-bass step-out bonus (E2d)
inline constexpr double kStepBudget = kWStepIn + kWStepOut + 0.01;  ///< Guard tolerance
```

---

## Part F — Build and test: Commit 1 (infra, suppression still off)

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2d1.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2d1.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2d1.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2d1.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2d1.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2d1.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407, 52/52, 11/11. `suppressProgressionSignals` is still
false everywhere; function layer still receives null snapshot → no-op.**
If any test fails, revert and report.

---

## Part G — Implement Pass B in `applyHarmonicFunction()` (Commit 2)

Replace the current rescore section in `applyHarmonicFunction()` in
`harmonicfunctionlayer.cpp`. The new implementation adds a Pass B simulation
after the per-cell rescore and before the quality guard.

```cpp
void applyHarmonicFunction(
    std::vector<analysis::ChordAnalysisResult>& candidates,
    analysis::ChordAnalysisResult& chosenResult,
    const HarmonicFunctionContext& ctx,
    const ScoringSnapshot* snapshot,
    const analysis::ChordAnalyzerPreferences* prefs)
{
    if (!snapshot || !prefs) return;
    if (!prefs->suppressProgressionSignals) return;
    if (candidates.empty()) return;

    // ── Step 1: Rescore all cells with signals re-applied ───────────────────
    //
    // Cells come from snapshot->cellsWithWDim and snapshot->cellsWithoutWDim.
    // They are in (bi, rootPc, tplIdx) order — cells from the same bass are
    // contiguous within each outer bi-block. Both vectors are the same length
    // and correspond index-by-index (same cell, different wDimDelta).
    //
    // In suppression mode, all snapshot cells have:
    //   cell.wDimDelta == 0  (wDimBonus returned 0)
    //   cell.wSeqBonus == 0  (wSeqBonus returned 0)
    //   cell.basisIndep      (clean, no rootContinuityBonus)
    //
    // Re-score formula:
    //   rcb          = fn::rootContinuityBonus(rootPc, ctx.previousRootPc,
    //                                          prefs->rootContinuityBonus)
    //   newBI        = cell.basisIndep + rcb        // rcb INSIDE the multiply
    //   baseScore    = (newBI + cell.basisDep) * cell.complexityFactor
    //                  * cell.augFactor + cell.wCompleteBonus
    //   newWSeq      = fn::wSeqBonus(cell.rootPc, ctx.nextRootPc,
    //                                snapshot->distinctPcs,
    //                                snapshot->jointScoringEnabled, false)
    //   newWDim      = fn::wDimBonus(cell.rootPc, cell.quality,
    //                                ctx.nextRootPc, snapshot->distinctPcs,
    //                                snapshot->jointScoringEnabled, false)
    //   scoreWithout = baseScore + newWSeq
    //   scoreWith    = scoreWithout + newWDim

    const std::size_t N = snapshot->cellsWithWDim.size();
    std::vector<double> scoreWith(N), scoreWithout(N);

    for (std::size_t i = 0; i < N; ++i) {
        const ScoringCell& cw  = snapshot->cellsWithWDim[i];
        const double rcb = rootContinuityBonus(
            cw.rootPc, ctx.previousRootPc, prefs->rootContinuityBonus);
        const double newBI = cw.basisIndep + rcb;
        const double base  = (newBI + cw.basisDep)
                             * cw.complexityFactor * cw.augFactor
                             + cw.wCompleteBonus;
        const double newWSeq = wSeqBonus(cw.rootPc, ctx.nextRootPc,
                                          snapshot->distinctPcs,
                                          snapshot->jointScoringEnabled, false);
        const double newWDim = wDimBonus(cw.rootPc, cw.quality,
                                          ctx.nextRootPc, snapshot->distinctPcs,
                                          snapshot->jointScoringEnabled, false);
        scoreWithout[i] = base + newWSeq;
        scoreWith[i]    = scoreWithout[i] + newWDim;
    }

    // ── Step 2: Pass B simulation ────────────────────────────────────────────
    //
    // Replicate applyStepBonusGuard() per bass group, for BOTH score variants
    // independently. Cells within a bass group are already in (rootPc, tplIdx)
    // row-major order — same iteration order as the original lambda.
    //
    // Gate: jointScoringEnabled && ctx.previousBassPc or nextBassPc valid.
    // Bonus: kWStepIn (step-in from prev bass), kWStepOut (step-out to next bass).
    // Guard: compRootPc = (bassPc - 3 + 12) % 12;
    //        blocked if any OTHER cell in the same bass group has
    //          other.rootPc == compRootPc
    //          && (Dim || HalfDim || (Minor && intervalCount == 4))
    //          && otherScore >= candScore - kStepBudget
    // Note: guard comparison uses the LIVE score (which may already include a
    // previously-applied step bonus for an earlier candidate in the group).
    // This matches the original lambda's in-place modification of perBass.

    if (snapshot->jointScoringEnabled) {
        auto runPassB = [&](std::vector<double>& scores) {
            // Find all distinct bassPcs and the index ranges for each.
            // Snapshot is in (bi, rootPc, tplIdx) order; adjacent cells with the
            // same bassPc form a contiguous block for each bi.
            // We iterate ALL indices and check cell.bassPc — same result.
            for (std::size_t ci = 0; ci < N; ++ci) {
                const ScoringCell& cand = snapshot->cellsWithWDim[ci];
                if (cand.rootPc != cand.bassPc) continue;   // root-position only
                if (cand.quality == analysis::ChordQuality::Power) continue;

                // Step-in: previous bass approaches this bass stepwise.
                double stepIn = 0.0;
                if (ctx.previousBassPc >= 0 && ctx.previousBassPc != cand.bassPc) {
                    const int d = ((cand.bassPc - ctx.previousBassPc) % 12 + 12) % 12;
                    if (d == 1 || d == 2 || d == 10 || d == 11) stepIn = kWStepIn;
                }
                // Step-out: this bass approaches next bass stepwise.
                double stepOut = 0.0;
                if (ctx.nextBassPc >= 0) {
                    const int d = ((ctx.nextBassPc - cand.bassPc) % 12 + 12) % 12;
                    if (d == 1 || d == 2 || d == 10 || d == 11) stepOut = kWStepOut;
                }
                if (stepIn + stepOut == 0.0) continue;

                // m7-family guard.
                const int compRoot = ((cand.bassPc - 3) % 12 + 12) % 12;
                bool blocked = false;
                for (std::size_t oi = 0; oi < N && !blocked; ++oi) {
                    const ScoringCell& other = snapshot->cellsWithWDim[oi];
                    if (other.bassPc != cand.bassPc) continue;
                    if (other.rootPc != compRoot) continue;
                    if (other.quality != analysis::ChordQuality::Diminished
                     && other.quality != analysis::ChordQuality::HalfDiminished
                     && !(other.quality == analysis::ChordQuality::Minor
                          && other.intervalCount == 4)) continue;
                    if (scores[oi] >= scores[ci] - kStepBudget) blocked = true;
                }
                if (!blocked) scores[ci] += stepIn + stepOut;
            }
        };

        runPassB(scoreWith);
        runPassB(scoreWithout);
    }

    // ── Step 3: Per-bass quality guard ───────────────────────────────────────
    //
    // For each bass, find the best score in each variant. Then globally,
    // find the with-wDim winner; if its quality is Dim/HalfDim, accept
    // with-wDim; otherwise fall back to without-wDim.
    // This replicates the post-bonus quality guard in analyzeChord().

    std::unordered_map<int, double> bestWith, bestWithout;
    std::unordered_map<int, analysis::ChordQuality> bestWithQuality;

    for (std::size_t i = 0; i < N; ++i) {
        const int bp = snapshot->cellsWithWDim[i].bassPc;
        if (bestWith.find(bp) == bestWith.end() || scoreWith[i] > bestWith[bp]) {
            bestWith[bp] = scoreWith[i];
            bestWithQuality[bp] = snapshot->cellsWithWDim[i].quality;
        }
        if (bestWithout.find(bp) == bestWithout.end()
            || scoreWithout[i] > bestWithout[bp]) {
            bestWithout[bp] = scoreWithout[i];
        }
    }

    // Global with-wDim winner.
    int    globalBpWith = -1;
    double globalBestWith = -std::numeric_limits<double>::infinity();
    for (const auto& [bp, sc] : bestWith) {
        if (sc > globalBestWith) { globalBestWith = sc; globalBpWith = bp; }
    }
    const bool acceptWithWDim = (globalBpWith >= 0)
        && (bestWithQuality[globalBpWith] == analysis::ChordQuality::Diminished
         || bestWithQuality[globalBpWith] == analysis::ChordQuality::HalfDiminished);

    // ── Step 4: Find global winner cell ──────────────────────────────────────
    const std::vector<double>& winScores = acceptWithWDim ? scoreWith : scoreWithout;
    std::size_t winnerCellIdx = 0;
    double winnerScore = -std::numeric_limits<double>::infinity();
    for (std::size_t i = 0; i < N; ++i) {
        if (winScores[i] > winnerScore) {
            winnerScore    = winScores[i];
            winnerCellIdx  = i;
        }
    }
    const ScoringCell& winnerCell = snapshot->cellsWithWDim[winnerCellIdx];

    // ── Step 5: Promote winner in candidates[] ────────────────────────────────
    //
    // Match by (tiePriority, rootPc). In suppression mode, threshold is
    // disabled → all 12×17 cells for the suppressed-signal winning bass are
    // in candidates[]. Any (tiePriority, rootPc) pair therefore exists.
    // If the winner is on a different bass, the match will find the same
    // (tiePriority, rootPc) entry with the wrong bassPc; patch it below.
    int winnerIdx = -1;
    for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
        if (candidates[i].identity.tiePriority == winnerCell.tiePriority
            && candidates[i].identity.rootPc    == winnerCell.rootPc) {
            winnerIdx = i; break;
        }
    }
    if (winnerIdx < 0) {
        // Should not occur in suppression mode (all cells present). If it does,
        // keep the suppressed-signal winner unchanged rather than crash.
        return;
    }

    if (winnerIdx != 0) {
        std::rotate(candidates.begin(),
                    candidates.begin() + winnerIdx,
                    candidates.begin() + winnerIdx + 1);
    }

    // Patch bassPc / bassTpc if winner is from a different bass.
    if (candidates[0].identity.bassPc != winnerCell.bassPc) {
        candidates[0].identity.bassPc  = winnerCell.bassPc;
        candidates[0].identity.bassTpc = winnerCell.bassTpc;
    }

    chosenResult = candidates[0];

    // Trim back to normal top-3 cap.
    if (candidates.size() > 3) candidates.resize(3);
}
```

**Required headers in `harmonicfunctionlayer.cpp`** (add if not present):
`#include <algorithm>` (for `std::rotate`), `#include <unordered_map>`,
`#include <limits>` (for `std::numeric_limits`).

**Note on `runPassB` closure**: the lambda captures `N`, `snapshot`, `ctx`,
and `kWStepIn/kWStepOut/kStepBudget` (which are inline constexpr in the
namespace — no capture needed for those; capture `N`, `snapshot`, `ctx` by
reference). If the compiler complains about `kStepBudget` inside the lambda,
copy it to a local variable before the lambda.

---

## Part H — Enable `suppressProgressionSignals` at all three call sites

This is the same change that was attempted and reverted in E2c Commit 2.
Now that Pass B is implemented, it should produce byte-identical results.

At each of the three call sites in `regionanalyzer.cpp`, set:

```cpp
<prefs_copy>.suppressProgressionSignals = true;
<prefs_copy>.captureScoringSnapshot     = &<snap>;
```

Where `<prefs_copy>` is the mutable prefs copy established at each site
(Pass 1 uses `attemptPrefs`, Pass 2 and 2b use copies created in E2c).
And `<snap>` is the `fn::ScoringSnapshot` local declared at each site.

(These locals were set up in E2c Commit 1 but left with
`suppressProgressionSignals = false`. Now set it to `true`.)

---

## Part I — Build and test: Commit 2 (Pass B + suppression enabled)

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2d2.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2d2.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2d2.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2d2.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2d2.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2d2.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407, 52/52, 11/11 — byte-identical to `20f992a5e7`.**

If pipeline snapshot tests fail again:
- Run `./pipeline_snapshot_tests.exe --gtest_filter='Snapshot*' > /tmp/snap_detail.txt 2>&1`
  and read the failing region's expected vs actual.
- Check: is the failing case a root-position candidate with stepwise bass? If
  so, the Pass B simulation order may differ from the original.
- Check: is the `winnerIdx < 0` guard firing (cross-bass miss)? Add a
  temporary counter: `if (winnerIdx < 0) { ++misses; }` and report the count.
- Do NOT update goldens. Report and revert everything.

---

## Part J — Commits

**Commit 1:**

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.h \
  src/composing/analysis/chord/chordanalyzer.cpp \
  src/composing/analysis/region/regionanalyzer.cpp; echo "exit:$?"

cd C:\s\MS && git commit -m "E2d-infra: intervalCount, bass-context extension, step-bonus constants

Add ScoringCell::intervalCount (templates[tplIdx].intervals.size()) for
the Pass B m7-family guard in applyHarmonicFunction(). Populated in the
D1 cell-capture block.

Extend HarmonicFunctionContext with previousBassPc and nextBassPc.
Populated from temporalCtx/subCtx at all three regionanalyzer.cpp call sites.

Add kWStepIn, kWStepOut, kStepBudget constants to harmonicfunctionlayer.h.

suppressProgressionSignals still false everywhere. Zero behavioral change.
All tests identical to HEAD 20f992a5e7."; echo "exit:$?"
```

**Commit 2:**

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.cpp \
  src/composing/analysis/region/regionanalyzer.cpp; echo "exit:$?"

cd C:\s\MS && git commit -m "E2d: enable progression-signal suppression with Pass B replication

applyHarmonicFunction() now replicates applyStepBonusGuard() after
rescoring snapshot cells with signals re-applied. Two independent Pass B
runs (with-wDim and without-wDim score variants) precede the quality guard,
matching the original per-variant simulation in analyzeChord().

suppressProgressionSignals=true enabled at all three regionanalyzer.cpp
call sites. The scorer runs without rootContinuityBonus, wSeqBonus, and
wDimBonus; the function layer re-applies all three plus the step bonus.

Cross-bass promotion: if the signal-inclusive winner is on a different bass
than the suppressed-signal scorer, bassPc and bassTpc are patched from the
snapshot cell (threshold disabled in suppression mode ensures all 204 cells
per bass are present in candidates[]).

docs/scoring_model.md §10 updated: E2c and E2d marked done.

Zero behavioral change. All tests identical to HEAD 20f992a5e7."; echo "exit:$?"
```

---

## Part K — Update `docs/scoring_model.md` §10

Mark E2c (infra) and E2d (enable) done. Note the Pass B replication and the
two-variant approach. Note that E2c-enable (original Commit 2) failed because
Pass B was not replicated and is now replaced by E2d.

---

## Report back

1. Part A1 findings — exact field name for template intervals
2. Whether `runPassB` required any deviation from the prescribed implementation
3. Whether the `winnerIdx < 0` guard ever fired across the 407 composing tests
   (add a temporary assert or counter in Commit 2 to verify)
4. Commit 1 test results and hash
5. Commit 2 test results and hash
6. Whether any pipeline snapshot golden needed updating (expected: none)
7. Any unexpected divergence in the pipeline snapshot tests (if Commit 2 fails)
