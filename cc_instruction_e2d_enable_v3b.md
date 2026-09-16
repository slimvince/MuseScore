# CC Instruction: E2d-enable v3b

## Pre-reading

Read `C:\s\MS\STATUS.md` and `C:\s\MS\build_and_test.md` before starting.
Current HEAD: `37e8a711fc` (E3). All 11 pipeline snapshot tests pass.

---

## Why v3 was insufficient — all four issues

The design review before writing this instruction (informed by your v3 investigation) found
four problems with the original v3 spec:

1. **Blocking (Iter 86/91/pedal):** Iter 86 (bass-b7 promotion, L3337–3359),
   Iter 91 (bass-as-root promotion, L3361–3400), and pedal detection (L3402–3487)
   run inside `analyzeChord()` BEFORE `applyHarmonicFunction()` runs.
   In suppression mode they stamp the suppressed-signal winner, not the real one.
   This is the same "Mode C reversion" bug E3 fixed for gates — it was never extended
   to these three tail passes. MUST be extracted first.

2. **Threshold formula wrong:** `basisDep` folds in `appliedBassBonus` via
   `bassDependentContextualBonuses()` (L3102). So `rescore()` output already includes
   `appliedBassBonus`. Correct formula:
   `threshold = (winnerRescore - winnerCell->appliedBassBonus) * kScoreThresholdRatio`
   (mirrors `analyzeChord` L3242–3245 exactly).

3. **Pass B guard wrong:** The v3 instruction used a simplified `isMin7` check.
   The real guard is `applyStepBonusGuard` (L3045–3083) which blocks the step bonus
   when a **competitor at `(bassPc - 3) % 12`** is Dim/HalfDim/MinorSeventh and
   `competitor.score ≥ cand.score - kStepBudget`. Must be replicated faithfully.

4. **Winner selection order wrong:** `analyzeChord` selects the global winner from
   post-Pass-B scores (L3158–3200). The function layer must do the same: apply the
   step bonus guard first, THEN pick the winner.

This instruction is split into two phases. Phase 1 is a self-contained prerequisite
commit; Phase 2 is the actual E2d-enable. Build and run all tests after Phase 1 before
proceeding to Phase 2.

---

## Phase 1: Extract Iter 86 / Iter 91 / Pedal to run after applyHarmonicFunction

**Mirror the E3 gate-extraction pattern exactly.** After this phase, non-suppression
behaviour must be byte-identical to HEAD.

### 1-A. What needs to move

Remove the three blocks from `analyzeChord()`:
- **Iter 86** — lines 3337–3359
- **Iter 91** — lines 3361–3400
- **Pedal detection** — lines 3402–3487

These blocks must run AFTER `applyHarmonicFunction()` and BEFORE
`applyPostScoringGates()` at every production call site (regionanalyzer.cpp, and
any other callers that invoke the full pipeline). The test helper `analyzeWithGates()`
must also call them.

### 1-B. Data each block needs

All three blocks currently read local variables from `analyzeChord()`. The already-
populated `PostScoringGateContext` (`gateCtxOut`) holds most of them. Add whatever
is missing:

| Block | Required locals | Already in gateCtxOut? |
|-------|----------------|------------------------|
| Iter 86 | `results`, `bassPc`, `pcWeight`, `prefs.extensionThreshold` | bassPc ✓; `pcWeight` **add it** |
| Iter 91 | `results`, `bassPc`, `context->nextRootPc`, `rawCandidates`, `buildChordResult(rc)` | bassPc ✓; rawCandidates ✓; context comes from regionanalyzer; `buildChordResult` needs to be callable |
| Pedal | `results`, `bassPc`, `tones`, `keySignatureFifths`, `keyMode`, `prefs` | bassPc ✓; `tones`, `keySignatureFifths`, `keyMode` **add them**; prefs is passed separately |

Concretely, add to `PostScoringGateContext` (in the header where it is declared):
```cpp
std::array<double, 12>          pcWeight{};    // for Iter 86
std::vector<ChordAnalysisTone>  tones;         // for pedal
int                             keySigFifths = 0;  // for pedal
KeySigMode                      keySigMode   = KeySigMode::Major;  // for pedal
```

And populate them in `analyzeChord()` inside the existing `if (gateCtxOut)` block
(L3318–3329), in the same pattern as the existing fields.

For Iter 91's `buildChordResult(rc)`: expose `buildChordResult` as a free function
in `chordanalyzer.h` (it is already at namespace scope in `chordanalyzer.cpp`) and
declare the `BuildChordResultContext` struct in the header too. Iter 91's extracted
code can then call it directly with the gateCtxOut fields.

### 1-C. New free function: `applyIter8691Pedal`

Create in `chordanalyzer.cpp` (and declare in `chordanalyzer.h`):

```cpp
void applyIter8691Pedal(
    std::vector<ChordAnalysisResult>&  results,
    ChordAnalysisResult&               chosenResult,
    const PostScoringGateContext&      gateCtx,
    const ChordTemporalContext*        temporalCtx,   // for Iter 91 nextRootPc
    const ChordAnalyzerPreferences&    prefs);
```

Move the three blocks verbatim into this function, substituting local variable
references with the corresponding `gateCtx.*` field or parameter. The body ends with:
```cpp
if (!results.empty()) chosenResult = results.front();
```

### 1-D. Call sites

In `regionanalyzer.cpp`, at every site that currently does:
```cpp
auto results = analyzeChord(..., &gateCtx);
applyHarmonicFunction(results, chosen, ctx, snapshot, prefs);
applyPostScoringGates(results, chosen, ..., gateCtx);
```

Insert the new call:
```cpp
auto results = analyzeChord(..., &gateCtx);
applyHarmonicFunction(results, chosen, ctx, snapshot, prefs);
applyIter8691Pedal(results, chosen, gateCtx, temporalCtx, prefs);   // NEW
applyPostScoringGates(results, chosen, ..., gateCtx);
```

Do the same in any other caller (harmonicsegmenter.cpp, bridge callers,
`analyzeWithGates()` test helper).

### 1-E. Phase 1 verification

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe   > /tmp/comp1.txt 2>&1; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe    > /tmp/nota1.txt 2>&1; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap1.txt 2>&1; echo "exit:$?"
tail -5 /tmp/comp1.txt /tmp/nota1.txt /tmp/snap1.txt
```

All tests must pass byte-identically, without `--update-goldens`.
If any test fails, revert Phase 1 and report — do NOT proceed to Phase 2.

Commit message: `E2d-prereq: extract Iter 86/91/pedal to run after applyHarmonicFunction`

---

## Phase 2: E2d-enable (suppression on, corrected function layer)

Proceed only after Phase 1 is committed and all tests pass.

### Part A — `src/composing/analysis/region/regionanalyzer.cpp`

Enable `suppressProgressionSignals=true` and snapshot capture at **Pass 1 only**.
Do NOT touch Pass 2 or Pass 2b call sites.

At the Pass 1 site only:
```cpp
ScoringSnapshot snapshot;
auto pass1Prefs = prefs;
pass1Prefs.suppressProgressionSignals = true;
pass1Prefs.captureScoringSnapshot     = &snapshot;
// Use pass1Prefs for the Pass 1 analyzeChord call.
// Pass &snapshot to applyHarmonicFunction.
```

The snapshot must be passed to `applyHarmonicFunction` at this site. All other
call sites remain unchanged.

### Part B — `src/composing/analysis/chord/chordanalyzer.cpp`

In suppression mode, return pre-built `ChordAnalysisResult` for ALL bass candidates
(not just the suppression-mode winning bass).

In the result-building loop at L3262–3272:
```cpp
for (const RawCandidate& rc : rawCandidates) {
    if (!prefs.suppressProgressionSignals) {
        if (results.size() >= 3) { break; }
        if (rc.score < threshold) { break; }
    }
    results.push_back(buildResult(rc));
}
```

`rawCandidates` at this point holds ONLY the winning-bass's cells. The other basses'
rawCandidates were discarded after the competition loop (L3085–3220).

**Approach:** During the per-bass competition loop (L3085–3181), in suppression mode
collect a staging vector of pre-built results for every bass. After the competition
selects the winning bass, append all staged results (all basses) to `results` in
suppression mode.

Concretely, before the competition loop:
```cpp
std::vector<ChordAnalysisResult> allBassResultsForSuppression;
```

At the end of each bass `bi` iteration (after `applyStepBonusGuard` and before
moving to `bi+1`), if `prefs.suppressProgressionSignals`:
```cpp
// Capture all cells for this bass using its local buildResult context.
const auto& src = acceptPostBonus ? perBassWith : perBassWithout;
for (const auto& rc : src) {
    allBassResultsForSuppression.push_back(buildResult(rc));
}
```

Then in the suppression-mode path of the result-building loop, replace the contents
of `results` with `allBassResultsForSuppression` (no threshold, no cap — the function
layer does that):
```cpp
for (const RawCandidate& rc : rawCandidates) {
    if (!prefs.suppressProgressionSignals) {
        if (results.size() >= 3) { break; }
        if (rc.score < threshold) { break; }
    }
    results.push_back(buildResult(rc));
}
if (prefs.suppressProgressionSignals) {
    results = std::move(allBassResultsForSuppression);
}
```

**Important:** `buildResult` inside the per-bass loop uses `bassPc`/`bassTpc`/
`pcWeight`/`tpcForPc` which are in flux during the competition. You must snapshot the
per-bass context at capture time (e.g. capture `bassCandidates[bi].pc` as local
`thisBassPC` and pass it to `BuildChordResultContext` explicitly). The winning-bass
context is committed only at L3201–3207; capture each bass's context before the
`bi` loop advances.

**Expected size of suppressed `results`:** ≤4 basses × 12 roots × 17 templates = ≤816.

### Part C — `src/composing/analysis/function/harmonicfunctionlayer.cpp`

Replace lines 114–169 (from `// ── Find the global winner cell ──` to the end of
the function body, before the closing `}`) with the corrected algorithm below.
Keep lines 1–113 unchanged (early-return guards, `rescore` lambda, quality guard).

The corrected algorithm has six steps:

**Step 1 — Per-bass rescoring with step bonus guard.**

Replicate `applyStepBonusGuard` (L3045–3083 in `chordanalyzer.cpp`) for each bassPc
group. `applyStepBonusGuard` operates on a `vector<RawCandidate>` but here we work
with `ScoringCell`. The logic is equivalent:

```cpp
// Locally mirror the step-bonus constants and stepwise helpers.
// (These will be deduplicated to a shared header in the follow-on cleanup.)
auto isStepwise = [](int from, int to) -> bool {
    if (from < 0 || to < 0) return false;
    const int d = ((to - from) % 12 + 12) % 12;
    return d == 1 || d == 2 || d == 10 || d == 11;
};
const bool stepInGlobal  = isStepwise(ctx.previousBassPc, /* TBD — set per-bass */0);
// We apply step bonus per-bass below.

// Group cells by bassPc; compute post-step score for each.
// Use a map from cell pointer → final score (including step bonus).
std::unordered_map<const ScoringCell*, double> finalScores;
finalScores.reserve(winningCells.size());

// First pass: compute rescore (pre-step) for every cell.
std::unordered_map<const ScoringCell*, double> preStepScores;
preStepScores.reserve(winningCells.size());
for (const auto& cell : winningCells) {
    auto [snw, sw] = rescore(cell);
    preStepScores[&cell] = acceptWithWDim ? sw : snw;
}

// Second pass: apply step bonus guard within each bassPc group.
// Gather unique bass PCs.
std::set<int> allBassPcs;
for (const auto& cell : winningCells) { allBassPcs.insert(cell.bassPc); }

for (int bp : allBassPcs) {
    const bool stepIn  = isStepwise(ctx.previousBassPc, bp);
    const bool stepOut = isStepwise(bp, ctx.nextBassPc);
    if (!stepIn && !stepOut) {
        // No step bonus possible for this bass; finalScores = preStepScores.
        for (const auto& cell : winningCells) {
            if (cell.bassPc == bp)
                finalScores[&cell] = preStepScores[&cell];
        }
        continue;
    }

    // kStepBudget = kWStepIn + kWStepOut + 0.01  (same constant as analyzeChord).
    // Find wStepIn / wStepOut by looking at definitions of wStepInBonus /
    // wStepOutBonus in chordanalyzer.cpp and replicating the return value.
    const double kStepBudget = kWStepIn + kWStepOut + 0.01;
    const int compRootPc = (bp - 3 + 12) % 12;

    // Check if there is a blocking competitor (Dim/HalfDim/Min7 at compRootPc
    // whose pre-step score is within kStepBudget of the candidate).
    for (const auto& cell : winningCells) {
        if (cell.bassPc != bp) continue;
        double score = preStepScores[&cell];

        using Q = analysis::ChordQuality;
        if (cell.rootPc == bp /* root-position */
            && cell.quality != Q::Power) {
            // Check for blocking competitor.
            bool blocked = false;
            for (const auto& other : winningCells) {
                if (other.bassPc != bp)                  { continue; }
                if (other.rootPc != compRootPc)          { continue; }
                const bool isMin7 = (other.quality == Q::Minor)
                                    && (other.intervalCount == 4);
                const bool relevantQuality =
                    (other.quality == Q::HalfDiminished)
                    || (other.quality == Q::Diminished)
                    || isMin7;
                if (!relevantQuality) { continue; }
                if (preStepScores.at(&other) >= score - kStepBudget) {
                    blocked = true;
                    break;
                }
            }
            if (!blocked) {
                score += (stepIn  ? kWStepIn  : 0.0)
                       + (stepOut ? kWStepOut : 0.0);
            }
        }
        finalScores[&cell] = score;
    }
}
```

**Important:** `kWStepIn`, `kWStepOut` are defined in `chordanalyzer.cpp`. Expose them
as `inline constexpr double` in `chordanalyzer.h` (or in a shared scoring-constants
header) so the function layer can use them. Do NOT hardcode numeric values.

**Step 2 — Select global winner from finalScores.**

```cpp
const ScoringCell* winnerCell  = nullptr;
double             winnerScore = -std::numeric_limits<double>::infinity();
for (const auto& cell : winningCells) {
    const double s = finalScores.at(&cell);
    if (s > winnerScore) { winnerScore = s; winnerCell = &cell; }
}
if (!winnerCell) return;
```

**Step 3 — Look up winner in candidates[] by (bassPc, rootPc, tiePriority).**

```cpp
int winnerIdx = -1;
for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
    const auto& id = candidates[i].identity;
    if (id.bassPc      == winnerCell->bassPc
        && id.rootPc   == winnerCell->rootPc
        && id.tiePriority == winnerCell->tiePriority) {
        winnerIdx = i;
        break;
    }
}
if (winnerIdx < 0) {
    // Defensive: should not happen with all-bass candidates[] from Part B.
    if (candidates.size() > 3) candidates.resize(3);
    return;
}
```

**Step 4 — Apply threshold + cap-of-3 on winning-bass cells.**

```cpp
// Threshold: de-inflate by winnerCell->appliedBassBonus (included in winnerScore
// via basisDep, so we subtract it back out — mirrors analyzeChord L3242-3245).
const double threshold =
    (winnerScore - winnerCell->appliedBassBonus) * kScoreThresholdRatio;

const int winnerBassPc = winnerCell->bassPc;

// Collect (finalScore, candidateIndex) for all winning-bass entries above threshold.
std::vector<std::pair<double, int>> bassEntries;
bassEntries.reserve(candidates.size());
for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
    if (candidates[i].identity.bassPc != winnerBassPc) continue;
    // Find the matching cell in winningCells to get the finalScore.
    double sc = -std::numeric_limits<double>::infinity();
    for (const auto& cell : winningCells) {
        if (cell.bassPc      != winnerBassPc)                      continue;
        if (cell.rootPc      != candidates[i].identity.rootPc)     continue;
        if (cell.tiePriority != candidates[i].identity.tiePriority) continue;
        sc = finalScores.at(&cell);
        break;
    }
    if (sc >= threshold) {
        bassEntries.push_back({ sc, i });
    }
}

// Sort by finalScore descending, tiePriority ascending as tiebreaker.
std::sort(bassEntries.begin(), bassEntries.end(),
    [&](const std::pair<double,int>& a, const std::pair<double,int>& b) {
        if (a.first != b.first) return a.first > b.first;
        return candidates[a.second].identity.tiePriority
             < candidates[b.second].identity.tiePriority;
    });

if (bassEntries.size() > 3) bassEntries.resize(3);
```

**Step 5 — Diff-root append (replicate analyzeChord L3291–3312).**

```cpp
// Only fires when winner is root-position and no diff-root is already present.
const int winnerRootPc = candidates[bassEntries[0].second].identity.rootPc;

if (winnerRootPc == winnerBassPc
    && prefs->inversionSuspicionMargin > 0.0)
{
    const bool hasDiffRoot = std::any_of(
        bassEntries.begin(), bassEntries.end(),
        [&](const std::pair<double,int>& e) {
            return candidates[e.second].identity.rootPc != winnerRootPc;
        });

    if (!hasDiffRoot) {
        double bestDiffSc  = -std::numeric_limits<double>::infinity();
        int    bestDiffIdx = -1;
        for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
            if (candidates[i].identity.bassPc  != winnerBassPc) continue;
            if (candidates[i].identity.rootPc  == winnerRootPc) continue;
            double sc = -std::numeric_limits<double>::infinity();
            for (const auto& cell : winningCells) {
                if (cell.bassPc      != winnerBassPc)                      continue;
                if (cell.rootPc      != candidates[i].identity.rootPc)     continue;
                if (cell.tiePriority != candidates[i].identity.tiePriority) continue;
                sc = finalScores.at(&cell);
                break;
            }
            if (sc >= threshold && sc > bestDiffSc) {
                bestDiffSc  = sc;
                bestDiffIdx = i;
            }
        }
        if (bestDiffIdx >= 0) {
            bassEntries.push_back({ bestDiffSc, bestDiffIdx });
        }
    }
}
```

**Step 6 — Rebuild candidates[] and chosenResult.**

```cpp
std::vector<analysis::ChordAnalysisResult> newCandidates;
newCandidates.reserve(bassEntries.size());
for (const auto& [sc, idx] : bassEntries) {
    newCandidates.push_back(candidates[idx]);
    newCandidates.back().identity.score = sc;
}
candidates    = std::move(newCandidates);
chosenResult  = candidates[0];
```

### Part D — `src/composing/analysis/function/harmonicfunctionlayer.h`

Add `kScoreThresholdRatio` alongside the existing bonus constants (copy value from
`chordanalyzer.cpp`). Also expose `kWStepIn` and `kWStepOut` in `chordanalyzer.h`
if they are not already (the function layer needs them for the step bonus guard).

Fix the stale `basisIndep` comment (L127–132): update it to note that in
suppression-mode capture `basisIndep` is clean (no rcb), and `appliedBassBonus` IS
included in `basisDep` via `bassDependentContextualBonuses`.

---

## Build and test sequence

```
# Phase 2 build
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Composing tests
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp2.txt 2>&1; echo "exit:$?"
tail -5 /tmp/comp2.txt

# Notation tests
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/nota2.txt 2>&1; echo "exit:$?"
tail -5 /tmp/nota2.txt

# Pipeline snapshot — byte-identical, NO --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap2.txt 2>&1; echo "exit:$?"
cat /tmp/snap2.txt

# Mismatch report
head -20 C:\s\MS\src\composing\tests\chord_mismatch_report.txt
```

---

## Acceptance criteria

- Phase 1: all tests pass byte-identically before proceeding to Phase 2.
- Phase 2: all 11 pipeline snapshot tests pass without `--update-goldens`.
- composing_tests.exe: 407/407 (current baseline), no regressions.
- notation_tests.exe: 52/52 (current baseline), no regressions.
- Mismatch: Baroque ≤25, Jazz ≤13 (current baselines).

---

## Hard stops — revert and report

1. Phase 1 changes behavior at all: any test difference → revert Phase 1.
2. Phase 2: any pipeline snapshot fails → revert Phase 2, keep Phase 1.
3. Phase 2: `--update-goldens` needed → not acceptable; revert Phase 2.
4. Any BIR increase in either preset → revert Phase 2.

---

## Canary tests

**Cross-bass (mechanism A):**
- `bach_bwv806_prelude` tick 7920: F#7/C# (V7/ii) in `implode` and `annotation`.
- `chopin_bi105_op30_2`: no diff-root 2-alt regions, so any failure = pure cross-bass.

**Diff-root append (mechanism B):**
- `mozart_k279_1` tick 1920: `alternatives` = [D/minor, F/major] (two entries).
- `chopin_bi105_op30_1` tick 1920: [C/minor, Ab/major].

**Pass 2/2b cascade fix:**
- `bach_chorale_137` tick 24000: E/halfDiminished (NOT D/minor), tick must NOT shift.

**Iter 86/91/pedal (Phase 1 validation):**
- All 10 pipeline scores must produce identical output before and after Phase 1.

---

## Files authorized to change

Phase 1:
- `src/composing/analysis/chord/chordanalyzer.cpp`
- `src/composing/analysis/chord/chordanalyzer.h`
- `src/composing/analysis/region/regionanalyzer.cpp`
- (and any other caller sites for `applyIter8691Pedal`)

Phase 2:
- `src/composing/analysis/region/regionanalyzer.cpp`
- `src/composing/analysis/chord/chordanalyzer.cpp`
- `src/composing/analysis/function/harmonicfunctionlayer.cpp`
- `src/composing/analysis/function/harmonicfunctionlayer.h`
- `src/composing/analysis/chord/chordanalyzer.h` (if kWStepIn/kWStepOut not already exposed)

Do not modify `docs/scoring_model.md` in either commit.
Do not update golden files.

## Commit messages

Phase 1: `E2d-prereq: extract Iter 86/91/pedal to run after applyHarmonicFunction`
Phase 2: `E2d-enable v3b: global-bass rebuild, correct threshold, faithful Pass B guard`
