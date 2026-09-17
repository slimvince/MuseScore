# CC Instruction — E2c: Progression-signal migration to function layer

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 and §10.

**Current HEAD:** `710d8dba12` (E2b). Working tree clean.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**This instruction introduces zero behavioral change.** The two commits below
must each pass 407/407, 52/52, 11/11 byte-identical to HEAD. If any test
changes, revert everything.

---

## Design decisions (from cc_instruction_e2c_investigate.md)

Read `C:\s\MS\cc_instruction_e2c_investigate.md` and
`C:\s\MS\cc_instruction_e2b_review.md` for the full rationale. Decisions:

1. **`tiePriority` added to `ChordIdentity`** — matching ambiguity between
   snapshot cells and `result.candidates` exists for augmented/Sus/same-root-
   template cases. `tiePriority` (one `int`) is the clean fix.
2. **`bassTpc` added to `ScoringCell`** — the function layer may need to
   overwrite `result.candidates[0].identity.bassTpc` when the re-scored winner
   uses a different bass than the suppressed-signal scorer.
3. **`jointScoringEnabled` added to `ScoringSnapshot`** — the `wSeqBonus` and
   `wDimBonus` functions require this flag, which is computed inside
   `analyzeChord()` and is not in prefs.
4. **Threshold disabled in suppression mode** — `kScoreThresholdRatio` and the
   top-3 cap are `constexpr`/hardcoded; cannot be caller-supplied. When
   `suppressProgressionSignals = true`, skip the threshold check and the top-3
   cap in `analyzeChord()` entirely. The function layer applies its own
   threshold and cap after re-scoring. The "guaranteed inversion alternative"
   append (post-threshold) is also disabled in suppression mode.
5. **rootContinuityBonus × cf × af** — `basisIndep` in the snapshot is CLEAN
   (no `rootContinuityBonus` folded in) when `suppressProgressionSignals` is
   true. The function layer re-applies it INSIDE the `(basisIndep + basisDep)
   * cf * af` product, not as a flat additive.
6. **Refinements reordered** — at all three call sites, refinements move AFTER
   `applyHarmonicFunction()`. In the current code they run before a no-op; the
   net output is identical because the function layer re-selects the same
   winner (with signals), and then refinements operate on that winner.
7. **Pass B NOT replicated in E2c** — the step-bonus lambdas depend on
   `previousBassPc` / `nextBassPc`, which are not yet in
   `HarmonicFunctionContext`. Candidate scores may differ between E2c-mode and
   current mode, but chord labels (`rootPc`, `quality`, `bassPc`, `degree`,
   `extensions`) are what the tests check, not scores.
8. **Same-bass assumption** — the re-scored winner is looked up in
   `result.candidates` by `(tiePriority, rootPc)`. In suppression mode,
   `result.candidates` contains only the suppressed-signal global winner's bass.
   If the re-scored winner is from a DIFFERENT bass, overwrite the winning
   entry's `bassPc` and `bassTpc` from the snapshot cell (field `bassTpc`,
   added in this instruction). If the re-scored winner is NOT found in
   `result.candidates` at all (extremely rare — requires the signal-inclusive
   winner to score below the suppressed threshold for its own bass), keep
   `candidates[0]` unchanged and log nothing; don't crash.
9. **Two commits** — Commit 1 adds all plumbing with `suppressProgressionSignals`
   defaulting to false (pure no-op, tests must pass). Commit 2 enables
   suppression at all three call sites and activates the re-scoring logic
   (tests must still pass byte-identical).

---

## Part A — Mandatory reads (before any edit)

### A1 — `buildResult` lambda in `chordanalyzer.cpp`

Read the full lambda. Confirm:
- The exact line where `bassPc` and `bassTpc` (outer variables) are first used
  inside the lambda body.
- The exact line where `rc.tiePriority` is currently used (if at all) — it is
  a field of `RawCandidate`; confirm it is NOT written to `result` today.
- The exact line where `results.push_back(buildResult(rc))` is called inside
  the post-threshold loop.

### A2 — D1 cell-capture block in `chordanalyzer.cpp`

Find the `if (prefs.captureScoringSnapshot)` block added in E2b (the cell
capture before the two `push_back` calls). Confirm:
- `bassCandidates[bi].tpc` is available at that scope (it must be, since
  `candBassPc = bassCandidates[bi].pc` is set just above).

### A3 — `jointScoringEnabled` in `chordanalyzer.cpp`

Find where `jointScoringEnabled` is first assigned. Report the exact line and
the expression used (it is computed from input conditions, not from `prefs`).

### A4 — `applyHarmonicFunction()` current signature and body

Read `harmonicfunctionlayer.h` and `harmonicfunctionlayer.cpp`. Confirm the
current signature `(ChordAnalysisResult& result, const HarmonicFunctionContext& ctx)`
and confirm the body is a no-op.

### A5 — Three call sites in `regionanalyzer.cpp`

For each of the three `applyHarmonicFunction()` calls (Pass 1 ~L457, Pass 2
~L663, Pass 2b ~L851):
- The exact line numbers
- Whether the call receives `result` or `chosenResult` or some other variable
- Whether a `vector<ChordAnalysisResult>` (the full candidates vector) is in
  scope at that point

Report before proceeding.

---

## Part B — Structural additions to `harmonicfunctionlayer.h`

### B1 — Add `bassTpc` to `ScoringCell`

Add one field after `bassPc`:

```cpp
int bassTpc;   ///< TPC of the bass candidate; needed by E2c to correct
               ///< bassTpc when the re-scored winner uses a different bass.
```

### B2 — Add `jointScoringEnabled` to `ScoringSnapshot`

Add one field at the end of `ScoringSnapshot` (after `distinctPcs`):

```cpp
bool jointScoringEnabled { false }; ///< Mirrors analyzeChord()'s jointScoringEnabled
                                    ///< flag; required by fn::wSeqBonus / fn::wDimBonus.
```

### B3 — Extend `applyHarmonicFunction()` declaration

Replace the current declaration:

```cpp
void applyHarmonicFunction(analysis::ChordAnalysisResult& result,
                           const HarmonicFunctionContext& ctx);
```

With:

```cpp
/// Apply harmonic function reasoning to the winning chord candidate.
/// When snapshot is non-null (E2c mode), re-scores the full candidate set
/// using the snapshot and promotes the signal-inclusive winner.
/// When snapshot is null (pre-E2c call sites), remains a no-op. E1: no-op.
void applyHarmonicFunction(std::vector<analysis::ChordAnalysisResult>& candidates,
                           analysis::ChordAnalysisResult& chosenResult,
                           const HarmonicFunctionContext& ctx,
                           const ScoringSnapshot* snapshot,
                           const analysis::ChordAnalyzerPreferences* prefs);
```

---

## Part C — Structural additions to `chordanalyzer.h`

### C1 — Add `tiePriority` to `ChordIdentity`

Add after `quality`:

```cpp
int tiePriority { -1 };   ///< Template index (E2c: used by applyHarmonicFunction
                           ///< to match snapshot cells back to result candidates).
```

### C2 — Add `suppressProgressionSignals` to `ChordAnalyzerPreferences`

Add after `captureScoringSnapshot`:

```cpp
/// When true, the three progression signals (rootContinuityBonus, w_seq, w_dim)
/// return 0 inside analyzeChord(). applyHarmonicFunction() re-applies them via
/// the ScoringSnapshot. captureScoringSnapshot must be set alongside this flag.
/// Default false — hot path unchanged.
bool suppressProgressionSignals { false };
```

---

## Part D — Populate new fields in `chordanalyzer.cpp`

### D1-addendum — Add `bassTpc` and adjust for `jointScoringEnabled`

In the existing D1 cell-capture block (the `if (prefs.captureScoringSnapshot)`
block before the two `push_back` calls), add `cell.bassTpc` using
`bassCandidates[bi].tpc`:

```cpp
cell.bassTpc = bassCandidates[bi].tpc;   // add after cell.bassPc = ...
```

### D2-addendum — Populate `jointScoringEnabled` in snapshot

After `jointScoringEnabled` is first assigned in `analyzeChord()` (line found
in Part A3), add a snapshot population:

```cpp
if (prefs.captureScoringSnapshot) {
    prefs.captureScoringSnapshot->jointScoringEnabled = jointScoringEnabled;
}
```

### D3-addendum — Populate `tiePriority` in `buildResult`

Inside the `buildResult` lambda, at the point where the result is about to be
returned (after all quality and rootPc corrections are applied), add:

```cpp
result.identity.tiePriority = static_cast<int>(rc.tiePriority);
```

---

## Part E — Gate signals in `analyzeChord()` on `suppressProgressionSignals`

### E1 — `rootContinuityBonus` in `bassIndependentContextualBonuses`

At the call site of `fn::rootContinuityBonus` inside
`bassIndependentContextualBonuses`, gate it:

```cpp
// BEFORE:
score += fn::rootContinuityBonus(rootPc, context->previousRootPc,
                                  prefs.rootContinuityBonus);

// AFTER:
if (!prefs.suppressProgressionSignals) {
    score += fn::rootContinuityBonus(rootPc, context->previousRootPc,
                                      prefs.rootContinuityBonus);
}
```

Do the same at the parallel site in `contextualBonuses()` (the diagnoseChord
path). Both sites that were updated in E2a must both be gated.

### E2 — `wSeqBonus` lambda wrapper

The lambda currently delegates to `fn::wSeqBonus(...)`. Gate the return:

```cpp
auto wSeqBonus = [&](int candRootPc) -> double {
    if (prefs.suppressProgressionSignals) return 0.0;
    return fn::wSeqBonus(candRootPc,
                         context ? context->nextRootPc : -1,
                         distinctPcs,
                         jointScoringEnabled,
                         prefs.explorationMode);
};
```

### E3 — `wDimBonus` lambda wrapper

```cpp
auto wDimBonus = [&](int candRootPc, analysis::ChordQuality quality) -> double {
    if (prefs.suppressProgressionSignals) return 0.0;
    return fn::wDimBonus(candRootPc, quality,
                         context ? context->nextRootPc : -1,
                         distinctPcs,
                         jointScoringEnabled,
                         prefs.explorationMode);
};
```

---

## Part F — Disable threshold, cap, and inversion-append in suppression mode

### F1 — Threshold and top-3 cap

The post-sort threshold loop (where `results.push_back(buildResult(rc))` is
called) currently breaks when `rc.score < threshold` or when
`results.size() >= 3`. In suppression mode, neither condition should fire
(the function layer applies its own threshold later). Gate both:

```cpp
for (const auto& rc : rawCandidates) {
    if (!prefs.suppressProgressionSignals) {
        if (rc.score < threshold) break;
        if (results.size() >= 3) break;
    }
    results.push_back(buildResult(rc));
}
```

### F2 — Guaranteed inversion-alternative append

The block that appends a guaranteed different-rootPc alternative (the
post-threshold append, ~L2697-2717 per the investigation) must be disabled
in suppression mode. Gate the entire block:

```cpp
if (!prefs.suppressProgressionSignals) {
    // ... existing guaranteed-inversion-alternative append block ...
}
```

---

## Part G — Implement `applyHarmonicFunction()` in `harmonicfunctionlayer.cpp`

Replace the current no-op body with the following logic. The function must
remain a no-op when `snapshot == nullptr`.

```
void applyHarmonicFunction(
    std::vector<analysis::ChordAnalysisResult>& candidates,
    analysis::ChordAnalysisResult& chosenResult,
    const HarmonicFunctionContext& ctx,
    const ScoringSnapshot* snapshot,
    const analysis::ChordAnalyzerPreferences* prefs)
{
    // No snapshot → E1/E2a/E2b no-op.
    if (!snapshot || !prefs) return;
    if (!prefs->suppressProgressionSignals) return;
    if (candidates.empty()) return;

    // ── Re-score all snapshot cells with progression signals applied ────────
    //
    // When suppressProgressionSignals was true, the scorer stored CLEAN basisIndep
    // values (no rootContinuityBonus), wSeqBonus=0, wDimDelta=0 in every cell.
    // Re-apply the signals now. rootContinuityBonus is folded into basisIndep
    // (which is then multiplied by cf × af), so it must be added BEFORE the
    // multiply — not as a flat post-multiply additive.
    //
    // Formula:
    //   rcb          = fn::rootContinuityBonus(cell.rootPc, ctx.previousRootPc,
    //                                          prefs->rootContinuityBonus)
    //   newBasisIndep = cell.basisIndep + rcb
    //   scoreNoWDim  = (newBasisIndep + cell.basisDep) * cell.complexityFactor
    //                  * cell.augFactor
    //                  + cell.wCompleteBonus
    //                  + fn::wSeqBonus(cell.rootPc, ctx.nextRootPc,
    //                                  snapshot->distinctPcs,
    //                                  snapshot->jointScoringEnabled, false)
    //   newWDimDelta = fn::wDimBonus(cell.rootPc, cell.quality,
    //                                ctx.nextRootPc, snapshot->distinctPcs,
    //                                snapshot->jointScoringEnabled, false)
    //   scoreWith    = scoreNoWDim + newWDimDelta

    // Per-bass best scores for the quality guard.
    // Key = bassPc.  We need per-bass best for WITH and WITHOUT wDim variants.
    std::unordered_map<int, double> bestWithPerBass;
    std::unordered_map<int, double> bestWithoutPerBass;
    std::unordered_map<int, analysis::ChordQuality> bestWithQualityPerBass;

    auto rescore = [&](const ScoringCell& cell) -> std::pair<double, double> {
        const double rcb = rootContinuityBonus(
            cell.rootPc, ctx.previousRootPc, prefs->rootContinuityBonus);
        const double newBasisIndep = cell.basisIndep + rcb;
        const double scoreNoWDim =
            (newBasisIndep + cell.basisDep)
            * cell.complexityFactor * cell.augFactor
            + cell.wCompleteBonus
            + wSeqBonus(cell.rootPc, ctx.nextRootPc,
                        snapshot->distinctPcs,
                        snapshot->jointScoringEnabled, false);
        const double newWDimDelta = wDimBonus(
            cell.rootPc, cell.quality, ctx.nextRootPc,
            snapshot->distinctPcs, snapshot->jointScoringEnabled, false);
        return { scoreNoWDim, scoreNoWDim + newWDimDelta };
    };

    for (const auto& cell : snapshot->cellsWithWDim) {
        auto [snw, sw] = rescore(cell);
        auto it = bestWithPerBass.find(cell.bassPc);
        if (it == bestWithPerBass.end() || sw > it->second) {
            bestWithPerBass[cell.bassPc]        = sw;
            bestWithQualityPerBass[cell.bassPc] = cell.quality;
        }
        (void)snw;
    }
    for (const auto& cell : snapshot->cellsWithoutWDim) {
        auto [snw, sw] = rescore(cell);
        auto it = bestWithoutPerBass.find(cell.bassPc);
        if (it == bestWithoutPerBass.end() || snw > it->second) {
            bestWithoutPerBass[cell.bassPc] = snw;
        }
        (void)sw;
    }

    // ── Quality guard (replicates analyzeChord's post-bonus guard) ──────────
    //
    // Find the global with-wDim winner across all basses.
    int    globalBestBassPcWith = -1;
    double globalBestScoreWith  = -std::numeric_limits<double>::infinity();
    for (const auto& [bp, sc] : bestWithPerBass) {
        if (sc > globalBestScoreWith) {
            globalBestScoreWith  = sc;
            globalBestBassPcWith = bp;
        }
    }

    // Accept with-wDim iff its winner quality is Dim or HalfDim.
    const bool acceptWithWDim = (globalBestBassPcWith >= 0)
        && (bestWithQualityPerBass[globalBestBassPcWith]
                == analysis::ChordQuality::Diminished
            || bestWithQualityPerBass[globalBestBassPcWith]
                == analysis::ChordQuality::HalfDiminished);

    // Select the winning variant's cells.
    const auto& winningCells = acceptWithWDim
        ? snapshot->cellsWithWDim
        : snapshot->cellsWithoutWDim;

    // ── Find the global winner cell ──────────────────────────────────────────
    const ScoringCell* winnerCell = nullptr;
    double             winnerScore = -std::numeric_limits<double>::infinity();

    for (const auto& cell : winningCells) {
        auto [snw, sw] = rescore(cell);
        const double s = acceptWithWDim ? sw : snw;
        if (s > winnerScore) {
            winnerScore = s;
            winnerCell  = &cell;
        }
    }

    if (!winnerCell) return;   // Should not happen.

    // ── Apply threshold and cap (mirrors analyzeChord's filter) ─────────────
    //
    // threshold = (bestScore - winnerAppliedBassBonus) * kScoreThresholdRatio
    // Sort candidates by re-scored value, keep top-3.
    // (We only affect which candidate is promoted to position 0; the detailed
    //  re-sort of all candidates is deferred to E2d.)

    // ── Look up winner in candidates[] ──────────────────────────────────────
    //
    // Match on (tiePriority, rootPc).  tiePriority uniquely identifies the
    // template; rootPc disambiguates across templates with the same index
    // (impossible by definition, but belt-and-suspenders).
    int winnerIdx = -1;
    for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
        if (candidates[i].identity.tiePriority == winnerCell->tiePriority
            && candidates[i].identity.rootPc    == winnerCell->rootPc) {
            winnerIdx = i;
            break;
        }
    }

    if (winnerIdx < 0) {
        // Edge case: winner was filtered out by the suppressed-signal threshold
        // (this can happen if the true winner's suppressed score is below the
        // suppressed-signal threshold, i.e. a different bass won the suppressed
        // pass). Do NOT crash; keep the suppressed-signal winner as-is.
        // This case is expected to be absent from the current test corpus.
        return;
    }

    // ── Promote winner to position 0 ─────────────────────────────────────────
    if (winnerIdx != 0) {
        std::rotate(candidates.begin(),
                    candidates.begin() + winnerIdx,
                    candidates.begin() + winnerIdx + 1);
    }
    chosenResult = candidates[0];

    // ── Correct bassPc / bassTpc if re-scored winner used a different bass ──
    if (candidates[0].identity.bassPc != winnerCell->bassPc) {
        candidates[0].identity.bassPc  = winnerCell->bassPc;
        candidates[0].identity.bassTpc = winnerCell->bassTpc;
        chosenResult = candidates[0];
    }

    // ── Trim back to normal top-3 cap ────────────────────────────────────────
    if (candidates.size() > 3) {
        candidates.resize(3);
    }
}
```

**Important notes on the implementation above:**
- The `rescore` lambda calls `rootContinuityBonus`, `wSeqBonus`, `wDimBonus` —
  these are the free functions in the same namespace, no qualifier needed.
- `std::unordered_map` requires `#include <unordered_map>` in the .cpp file.
- `std::rotate` requires `#include <algorithm>`.
- The implementation above does NOT re-sort all candidates by re-scored value
  beyond promoting the winner — this is intentional for E2c. A full re-sort
  (including recalculating the threshold for which candidates #1/#2 survive)
  is deferred to E2d. The pipeline snapshot tests compare `candidates[0]` only.
- The `(void)` casts suppress unused-variable warnings for the
  structured-binding decomposition.

---

## Part H — Update `regionanalyzer.cpp` call sites

For all three sites, the changes are:
1. Pass the candidates vector AND the chosen-result reference separately
   to `applyHarmonicFunction()`.
2. Pass `snapshot` and `prefs` (or pointer to prefs).
3. Move refinements AFTER `applyHarmonicFunction()`.

In **Commit 1**, set `snapshot = nullptr` (or don't declare one yet) so the
function layer remains a no-op. Update the call signature only.

In **Commit 2**, declare `fn::ScoringSnapshot snap;` at each site, set
`prefs.suppressProgressionSignals = true` and
`prefs.captureScoringSnapshot = &snap`, and pass `&snap` and `&prefs`.

### H1 — Pass 1 (~L453-465)

**Current order:**
```
analyzeChord(...)           → results / chosenResult
refineSparseChordQuality(chosenResult, ...)
applyTonicPrior(chosenResult, ...)
applyHarmonicFunction(chosenResult, ctx)
```

**New order (Commit 1 — no snapshot yet):**
```
analyzeChord(...)           → results / chosenResult
applyHarmonicFunction(results, chosenResult, ctx, nullptr, nullptr)
refineSparseChordQuality(chosenResult, ...)
applyTonicPrior(chosenResult, ...)
```

**New order (Commit 2 — snapshot enabled):**
```
fn::ScoringSnapshot snap;
attemptPrefs.suppressProgressionSignals = true;
attemptPrefs.captureScoringSnapshot     = &snap;
analyzeChord(..., attemptPrefs)         → results / chosenResult
applyHarmonicFunction(results, chosenResult, ctx, &snap, &attemptPrefs)
refineSparseChordQuality(chosenResult, ...)
applyTonicPrior(chosenResult, ...)
```

(`attemptPrefs` already exists as a mutable local at this site — confirmed
by investigation.)

### H2 — Pass 2 (~L658-674)

Pass 2 uses `prefs` (the const parameter). Create a mutable copy.

**New order (Commit 1):**
```
analyzeChord(..., prefs)    → subResults / chosenSub
applyHarmonicFunction(subResults, chosenSub, subCtx, nullptr, nullptr)
refineSparseChordQuality(chosenSub, ...)
```

**New order (Commit 2):**
```
analysis::ChordAnalyzerPreferences pass2Prefs = prefs;
fn::ScoringSnapshot snap2;
pass2Prefs.suppressProgressionSignals = true;
pass2Prefs.captureScoringSnapshot     = &snap2;
analyzeChord(..., pass2Prefs)         → subResults / chosenSub
applyHarmonicFunction(subResults, chosenSub, subCtx, &snap2, &pass2Prefs)
refineSparseChordQuality(chosenSub, ...)
```

### H3 — Pass 2b (~L844-862)

Identical pattern to H2. Create `pass2bPrefs`, `snap2b`.

---

## Part I — Build and test: Commit 1 (infrastructure, signals still on)

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2c1.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2c1.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2c1.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2c1.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2c1.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2c1.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407, 52/52, 11/11 — byte-identical to `710d8dba12`.**
`suppressProgressionSignals` is false everywhere; `applyHarmonicFunction()`
receives `nullptr` → no-op. If any test fails, revert and report.

---

## Part J — Build and test: Commit 2 (suppression enabled)

Same commands, files `/tmp/comp_e2c2.txt` etc.

**Expected: 407/407, 52/52, 11/11 — byte-identical to `710d8dba12`.**
The function layer now re-scores and promotes the signal-inclusive winner;
the chord labels must be identical to the current scorer output.

If pipeline snapshot tests FAIL:
- Run `./pipeline_snapshot_tests.exe --gtest_filter='*' > /tmp/snap_detail.txt 2>&1`
  and read the diff to identify which region changed.
- Check whether the failing region triggers the "edge case" path in
  `applyHarmonicFunction()` (winner not found in candidates — different-bass
  scenario). Report but do NOT update goldens without explicit approval.

---

## Part K — Commits

**Commit 1:**

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.h \
  src/composing/analysis/function/harmonicfunctionlayer.cpp \
  src/composing/analysis/chord/chordanalyzer.h \
  src/composing/analysis/chord/chordanalyzer.cpp \
  src/composing/analysis/region/regionanalyzer.cpp; echo "exit:$?"

cd C:\s\MS && git commit -m "E2c-infra: plumbing for progression-signal migration

Add to ScoringCell: bassTpc (needed by function layer to correct bassTpc
when re-scored winner uses a different bass than the suppressed-signal pass).
Add to ScoringSnapshot: jointScoringEnabled (required by fn::wSeqBonus /
fn::wDimBonus; not in prefs, computed inside analyzeChord()).
Add to ChordIdentity: tiePriority (needed by applyHarmonicFunction() to
match snapshot cells back to result.candidates entries unambiguously).
Add to ChordAnalyzerPreferences: suppressProgressionSignals { false }.

Extend applyHarmonicFunction() signature to accept candidates vector,
chosenResult ref, snapshot*, and prefs*. Remains a no-op when snapshot
is null (all three regionanalyzer.cpp call sites pass nullptr).

Refinements reordered to run AFTER applyHarmonicFunction() at all three
call sites — no behavioral change since the function layer is still a no-op,
but establishes the correct order for Commit 2.

Zero behavioral change. All tests identical to HEAD 710d8dba12."; echo "exit:$?"
```

**Commit 2:**

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.cpp \
  src/composing/analysis/chord/chordanalyzer.cpp \
  src/composing/analysis/region/regionanalyzer.cpp; echo "exit:$?"

cd C:\s\MS && git commit -m "E2c: migrate progression signals to applyHarmonicFunction()

Enable suppressProgressionSignals=true at all three analyzeChord() call
sites in regionanalyzer.cpp. The scorer now returns 0 for
rootContinuityBonus, wSeqBonus, and wDimBonus; the threshold filter and
top-3 cap are disabled in suppression mode to preserve all candidates for
the function layer.

applyHarmonicFunction() re-applies the three signals using the
ScoringSnapshot: rootContinuityBonus is folded into basisIndep before the
complexityFactor x augFactor multiply (not flat-added). wSeqBonus and
wDimBonus are applied via the existing fn:: free functions with
snapshot->jointScoringEnabled. The w_dim quality guard is replicated (two
variant cubes, same accept condition). The signal-inclusive winner is
matched by (tiePriority, rootPc) and promoted to candidates[0].

Pass B (step-bonus) replication is deferred to E2d; candidate scores may
differ from E2b baseline but chord labels (rootPc, quality, bassPc, degree,
extensions) are identical.

docs/scoring_model.md §10 updated: E2c marked done.

Zero behavioral change. All tests identical to HEAD 710d8dba12."; echo "exit:$?"
```

---

## Part L — Update `docs/scoring_model.md` §10

In §10 (harmonic function layer migration plan), mark E2c done and update
the description to reflect the two-commit split and the deferred Pass B note.

---

## Report back

1. Part A findings — exact line numbers for all five items
2. Whether the `jointScoringEnabled` population site (D2-addendum) is before
   or after the snapshot's capacity reservation (D3 from E2b) — should be
   before the bass loop, i.e. early in the joint-scoring block
3. Any deviation from the prescribed `applyHarmonicFunction()` implementation
   (report but do not deviate from the algorithm without flagging)
4. Whether the "edge case" path (winner not in candidates) ever fired across
   any of the 407 composing tests — grep for a debug counter or check via
   a temporary assert
5. Commit 1 test results
6. Commit 2 test results
7. Commit hashes for both commits
8. Whether any pipeline snapshot golden needed updating (expected: none)
