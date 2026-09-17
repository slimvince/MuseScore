# CC Instruction — E2d-enable v2: Enable progression-signal suppression

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 and §10.

**Current HEAD:** `37e8a711fc` (E3). Working tree clean.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**One commit. All tests must be byte-identical to HEAD `37e8a711fc`.
Do NOT update goldens under any circumstances. If snapshot tests fail,
stop and report.**

---

## Context

E3 extracted gates A–L from `analyzeChord()` into `applyPostScoringGates()`,
which regionanalyzer.cpp now calls AFTER `applyHarmonicFunction()`. The
execution order at every production call site is now:

```
analyzeChord(..., &gateCtx)         → pre-gate results + gate context
applyHarmonicFunction(...)          → currently a no-op (snapshot=nullptr)
applyPostScoringGates(..., gateCtx) → gates run on the function-layer winner
chosenResult = results.front()
```

With E2d-enable active, `suppressProgressionSignals=true` causes
`analyzeChord()` to score without progression signals (all signal lambdas
return 0, threshold disabled → all 204 cells per bass are returned
pre-gate). `applyHarmonicFunction()` then rescores with signals applied,
promotes the signal-inclusive winner to `results[0]`, and
`applyPostScoringGates()` runs the same gate logic on that winner. Because
the gates run on the same pre-gate winner as the non-suppression path, the
output is byte-identical.

**Two things need to change:**

1. **`applyHarmonicFunction()` is missing Pass B.** The current body has a
   rescore loop and per-bass quality guard but no step-bonus simulation. The
   step bonus (±0.10 in/out) is large enough to flip the winner; without
   replicating it the function layer picks the wrong winner.

2. **Three call sites still pass `nullptr, nullptr` for snapshot/prefs.**
   `suppressProgressionSignals` is still false at all sites.

**No other files change.** `chordanalyzer.cpp`, `applyPostScoringGates()`,
and all test files are untouched.

---

## Part A — Confirm current state

Read `src/composing/analysis/function/harmonicfunctionlayer.cpp` in full.
Confirm:
- The function body is present (not just `return;`) but has NO Pass B
  step-bonus simulation.
- The current structure uses per-bass score maps (`bestWithPerBass` etc.)
  rather than per-cell score arrays.
- A final `candidates.resize(3)` trim is present.
- `kWStepIn`, `kWStepOut`, `kStepBudget` are already defined in
  `harmonicfunctionlayer.h`.
- `HarmonicFunctionContext` already has `previousBassPc` and `nextBassPc`.

Read `src/composing/analysis/region/regionanalyzer.cpp`:
- Pass 1 (~L370–470): note where `attemptPrefs` is declared (it is a
  `ChordAnalyzerPreferences` copy declared at the top of the `runPass1`
  lambda, outside the per-region loop) and that
  `applyHarmonicFunction(..., nullptr, nullptr)` is at ~L463.
- Pass 2 (~L655–690) and Pass 2b (~L855–885): `analyzeChord()` uses `prefs`
  (const ref); `applyHarmonicFunction(..., nullptr, nullptr)` is present at
  both sites.

---

## Part B — Replace `applyHarmonicFunction()` body

Replace the **entire function body** of `applyHarmonicFunction()` in
`harmonicfunctionlayer.cpp` with the following. This restructures from
per-bass maps to per-cell score arrays (required for Pass B), adds Pass B,
and sorts the tail by rescored score so `applyPostScoringGates()` sees the
same alternative ordering as the non-suppression path.

```cpp
void applyHarmonicFunction(std::vector<analysis::ChordAnalysisResult>& candidates,
                           analysis::ChordAnalysisResult& chosenResult,
                           const HarmonicFunctionContext& ctx,
                           const ScoringSnapshot* snapshot,
                           const analysis::ChordAnalyzerPreferences* prefs)
{
    if (!snapshot || !prefs) return;
    if (!prefs->suppressProgressionSignals) return;
    if (candidates.empty()) return;

    // ── Step 1: Rescore all snapshot cells with progression signals applied ──
    //
    // In suppression mode the scorer stored CLEAN basisIndep values (no
    // rootContinuityBonus), wSeqBonus=0, wDimDelta=0. Re-apply signals now.
    // rootContinuityBonus must be folded inside basisIndep (before the cf×af
    // multiply) — not added as a flat post-multiply term.
    //
    // Both cubes (cellsWithWDim, cellsWithoutWDim) have the same length N and
    // correspond index-by-index (same cell, different wDimDelta).  Only
    // cellsWithWDim is needed for identity (bassPc, rootPc, tiePriority,
    // quality, intervalCount); the scoreWithout variant uses the without-wDim
    // scoring for the quality guard.

    const std::size_t N = snapshot->cellsWithWDim.size();
    std::vector<double> scoreWith(N), scoreWithout(N);

    for (std::size_t i = 0; i < N; ++i) {
        const ScoringCell& cw = snapshot->cellsWithWDim[i];
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
    // Replicates applyStepBonusGuard() per bass group, for BOTH score variants
    // independently.  Cells within each bass group are in (rootPc, tplIdx)
    // row-major order — same iteration order as the original lambda.
    //
    // Gate: jointScoringEnabled (same as original).
    // Bonus: kWStepIn (step-in from prev bass), kWStepOut (step-out to next).
    // Root-position only; Power excluded.
    // m7-family guard (compRootPc = (bassPc-3+12)%12): blocked when any other
    // cell in the same bass group has rootPc==compRootPc, quality in
    // {Dim, HalfDim, Minor+4-intervals}, and score >= cand_score - kStepBudget.
    // Guard comparison uses the LIVE score (modified in-place by earlier
    // iterations) — matches the original lambda's in-place behaviour.

    if (snapshot->jointScoringEnabled) {
        auto runPassB = [&](std::vector<double>& scores) {
            for (std::size_t ci = 0; ci < N; ++ci) {
                const ScoringCell& cand = snapshot->cellsWithWDim[ci];
                if (cand.rootPc != cand.bassPc) continue;    // root-position only
                if (cand.quality == analysis::ChordQuality::Power) continue;

                double stepIn = 0.0;
                if (ctx.previousBassPc >= 0 && ctx.previousBassPc != cand.bassPc) {
                    const int d = ((cand.bassPc - ctx.previousBassPc) % 12 + 12) % 12;
                    if (d == 1 || d == 2 || d == 10 || d == 11) stepIn = kWStepIn;
                }
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
                    if (other.rootPc != compRoot)    continue;
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
    // Replicates analyzeChord()'s post-bonus guard: accept the with-wDim
    // variant only when its per-bass winner has Dim or HalfDim quality.

    std::unordered_map<int, double>                      bestWith, bestWithout;
    std::unordered_map<int, analysis::ChordQuality>      bestWithQuality;

    for (std::size_t i = 0; i < N; ++i) {
        const int bp = snapshot->cellsWithWDim[i].bassPc;
        if (bestWith.find(bp) == bestWith.end() || scoreWith[i] > bestWith[bp]) {
            bestWith[bp]        = scoreWith[i];
            bestWithQuality[bp] = snapshot->cellsWithWDim[i].quality;
        }
        if (bestWithout.find(bp) == bestWithout.end()
            || scoreWithout[i] > bestWithout[bp]) {
            bestWithout[bp] = scoreWithout[i];
        }
    }

    int    globalBpWith   = -1;
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
    double      winnerScore   = -std::numeric_limits<double>::infinity();
    for (std::size_t i = 0; i < N; ++i) {
        if (winScores[i] > winnerScore) {
            winnerScore   = winScores[i];
            winnerCellIdx = i;
        }
    }
    const ScoringCell& winnerCell = snapshot->cellsWithWDim[winnerCellIdx];

    // ── Step 5: Promote winner in candidates[] ────────────────────────────────
    //
    // Match by (tiePriority, rootPc).  In suppression mode the threshold is
    // disabled — all 204 cells for the suppressed-signal winning bass are in
    // candidates[].  Any (tiePriority, rootPc) pair therefore exists.
    int winnerIdx = -1;
    for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
        if (candidates[i].identity.tiePriority == winnerCell.tiePriority
            && candidates[i].identity.rootPc    == winnerCell.rootPc) {
            winnerIdx = i;
            break;
        }
    }
    if (winnerIdx < 0) {
        // Should not occur. Keep suppressed-signal winner rather than crash.
        return;
    }

    if (winnerIdx != 0) {
        std::rotate(candidates.begin(),
                    candidates.begin() + winnerIdx,
                    candidates.begin() + winnerIdx + 1);
    }

    // Patch bassPc / bassTpc if the signal-inclusive winner is on a different bass.
    if (candidates[0].identity.bassPc != winnerCell.bassPc) {
        candidates[0].identity.bassPc  = winnerCell.bassPc;
        candidates[0].identity.bassTpc = winnerCell.bassTpc;
    }
    chosenResult = candidates[0];

    // ── Step 6: Sort tail by rescored score, then trim to top-3 ──────────────
    //
    // After rotation, candidates[1..] are still in suppressed-signal order.
    // Re-sort them by signal-inclusive score so applyPostScoringGates() sees
    // the same alternative ordering it would see in the non-suppression path.
    // This is required for byte-identical gate behaviour (Gate A-F examine
    // candidates[1] for inversion candidates).

    auto rescoredScore = [&](const analysis::ChordAnalysisResult& r) -> double {
        // Look up the cell's rescored signal-inclusive score.
        for (std::size_t i = 0; i < N; ++i) {
            const ScoringCell& sc = snapshot->cellsWithWDim[i];
            if (sc.tiePriority == r.identity.tiePriority
                && sc.rootPc   == r.identity.rootPc) {
                return winScores[i];
            }
        }
        return -std::numeric_limits<double>::infinity();
    };

    if (candidates.size() > 1) {
        std::sort(candidates.begin() + 1, candidates.end(),
                  [&](const auto& a, const auto& b) {
                      return rescoredScore(a) > rescoredScore(b);
                  });
    }
    if (candidates.size() > 3) {
        candidates.resize(3);
    }
}
```

**Note on the `rescoredScore` lambda:** the linear scan is O(N) per candidate
tail entry but only for the ≤2 tail entries after trimming to 3. N is at most
~816 cells (4 basses × 12 roots × 17 templates). If this shows up in a
profiler it can be replaced with an `unordered_map` lookup, but for now
clarity is preferred.

**Required headers:** `<algorithm>`, `<limits>`, `<unordered_map>` — all
already included in the current `harmonicfunctionlayer.cpp`.

---

## Part C — Enable suppression at 3 call sites in `regionanalyzer.cpp`

For each call site the pattern is:
1. Declare a `fn::ScoringSnapshot snap;` per-region (inside the loop, before
   `analyzeChord()`).
2. Set `captureScoringSnapshot = &snap` on the prefs before `analyzeChord()`.
3. Set `suppressProgressionSignals = true` on the prefs.
4. Change `applyHarmonicFunction(..., nullptr, nullptr)` to
   `applyHarmonicFunction(..., &snap, &<prefs>)`.

### Pass 1 (~L370, inside `runPass1` lambda)

`attemptPrefs` is the mutable prefs copy. Add `suppressProgressionSignals`
once at the lambda's top (after the existing `minDistinctPcsForCandidate`
line):

```cpp
attemptPrefs.suppressProgressionSignals = true;
```

Inside the per-region loop, just before the `analyzeChord()` call:

```cpp
function::ScoringSnapshot snap;
attemptPrefs.captureScoringSnapshot = &snap;
```

(The snap must be declared per-iteration so each call gets a fresh object;
`captureScoringSnapshot` is updated each iteration to point to it.)

Change the `applyHarmonicFunction` call:
```cpp
// Before:
function::applyHarmonicFunction(results, chosenResult, fnCtx,
                                nullptr, nullptr);
// After:
function::applyHarmonicFunction(results, chosenResult, fnCtx,
                                &snap, &attemptPrefs);
```

### Pass 2 (~L655, inside Pass 2 sub-region loop)

`prefs` is const. Introduce a mutable copy per-iteration at the top of the
sub-region loop body, before `analyzeChord()`:

```cpp
analysis::ChordAnalyzerPreferences subPrefs = prefs;
subPrefs.suppressProgressionSignals = true;
function::ScoringSnapshot subSnap;
subPrefs.captureScoringSnapshot = &subSnap;
```

Change the three affected calls:
```cpp
// analyzeChord: change prefs → subPrefs
auto subResults = chordAnalyzer->analyzeChord(
    subTones, subKeyFifths, subKeyMode, &subCtx, subPrefs, &subGateCtx);

// applyHarmonicFunction: change nullptr, nullptr → &subSnap, &subPrefs
function::applyHarmonicFunction(subResults, chosenSub, fnCtx,
                                &subSnap, &subPrefs);

// applyPostScoringGates: change prefs → subPrefs
analysis::applyPostScoringGates(subResults, subPrefs, &subCtx, subGateCtx);
```

### Pass 2b (~L855, inside Pass 2b sub-region loop)

Identical pattern to Pass 2. Use `subPrefs2b` (or `subPrefs` — pick a name
that doesn't clash with Pass 2's local if they're in the same scope).
Verify the exact variable names by reading the code.

---

## Part D — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2de.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2de.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2de.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2de.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2de.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2de.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407, 52/52, 11/11 byte-identical to `37e8a711fc`.**

**If composing or notation tests fail: revert all changes and report.
Do not proceed.**

**If snapshot tests fail:**

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_detail.txt 2>&1; echo "exit:$?"
grep -A 40 "FAILED\|Expected\|Actual" /tmp/snap_detail.txt | head -150; echo "exit:$?"
```

For EACH failing test, report:
- Test name
- Expected `candidates[0]`: rootPc, quality, bassPc, score
- Actual `candidates[0]`: rootPc, quality, bassPc, score
- Whether `candidates[0]` is identical between expected and actual

**If candidates[0] differs in ANY test:** do NOT update goldens, revert
all changes, and report the full diff. The root cause must be understood
before proceeding.

**If candidates[0] is identical in all failing tests** (only alternatives
[1]/[2] differ): report which tests and the diff, then stop and ask before
updating goldens.

---

## Part E — Update `docs/scoring_model.md` §10

Mark E2d done. Add a note that:
- Pass B is replicated in `applyHarmonicFunction()` via per-cell score arrays
  (required because Pass B modifies scores in-place and the guard reads live
  scores).
- Two-variant Pass B (with-wDim / without-wDim) runs independently to match
  `analyzeChord()`'s quality guard.
- Tail candidates are sorted by signal-inclusive rescored score before
  trimming so `applyPostScoringGates()` sees the correct alternative ordering.

---

## Part F — Commit

Only if all three test suites pass byte-identical:

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.cpp \
  src/composing/analysis/region/regionanalyzer.cpp \
  docs/scoring_model.md; echo "exit:$?"

cd C:\s\MS && git commit -m "E2d-enable: progression-signal suppression with Pass B replication

applyHarmonicFunction() restructured from per-bass maps to per-cell score
arrays, enabling two-variant Pass B simulation (scoreWith / scoreWithout)
that replicates applyStepBonusGuard(). The step bonus is applied in-place
so the m7-family guard comparison uses live (already-modified) scores,
matching the original lambda behaviour.

suppressProgressionSignals=true enabled at all three regionanalyzer.cpp
call sites (Pass 1 / Pass 2 / Pass 2b). analyzeChord() runs in suppression
mode (no progression signals, threshold disabled); the function layer
rescores with signals and promotes the signal-inclusive winner; then the
extracted applyPostScoringGates() runs on that winner.

Tail candidates are sorted by signal-inclusive rescored score before
trimming to top-3, so applyPostScoringGates() sees the same alternative
ordering as the non-suppression path.

Zero behavioral change. All tests byte-identical to HEAD 37e8a711fc:
407/407 composing, 52/52 notation, 11/11 snapshot.

docs/scoring_model.md §10 updated: E2d marked done."; echo "exit:$?"
```

---

## After this commit

Hand `C:\s\MS\cc_instruction_e2d_cleanup.md` to CC. That instruction
extracts `applyStepBonus()` into a shared free function to eliminate the
Pass B code duplication between `chordanalyzer.cpp` and
`harmonicfunctionlayer.cpp`.

---

## Report back

1. Composing and notation test results
2. Did all 11 snapshot tests pass byte-identical?
3. If any snapshot test failed: rootPc/quality/bassPc of expected vs actual
   candidates[0] for each failing test
4. Commit hash
5. Any deviation from the specified implementation (e.g. different variable
   names at the Pass 2b site, name clash requiring renaming)
