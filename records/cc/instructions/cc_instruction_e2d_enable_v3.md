# CC Instruction: E2d-enable v3

## Pre-reading

Read `C:\s\MS\STATUS.md` and `C:\s\MS\build_and_test.md` before starting.
Current HEAD: `37e8a711fc` (E3). All 11 pipeline snapshot tests pass.

---

## Background: why v2 failed

`suppressProgressionSignals` is gated in exactly five places in `chordanalyzer.cpp`.
The function layer re-adds signals 1–3 (rootContinuity, wSeq, wDim). It does NOT
replicate signals 4 and 5:

| Line | What is suppressed | v2 outcome |
|------|-------------------|------------|
| 3263 | results threshold + cap-of-3 | suppression returns 204 raw cells for the winning bass; function layer just trims to 3 without applying threshold |
| 3291 | diff-root append | alternatives lose the forced diff-root entry; Gate A gets a truncated candidate set |

And the function layer has a cross-bass silent-fail: it finds the global rescored winner
from the snapshot (all basses), then looks it up in `candidates[]` by `(tiePriority,
rootPc)`. `candidates[]` holds only the **suppression-mode winning bass's** 204 cells.
When a progression signal (rootContinuityBonus +0.40, wSeq +0.20) changes *which bass*
wins, the winner is absent from `candidates[]` → `winnerIdx < 0` → early return →
suppressed winner is kept silently.

Three specific failures from the investigation:

- **PRELUDE tick 7920**: rootContinuityBonus +0.40 from F♯m predecessor lifts the
  F♯7/C♯ slash reading (cross-bass, C♯ bass absent from suppressed `candidates[]`).
  Independent of the diff-root append (slash chord: rootPc ≠ bassPc, append never fires).

- **Mozart/Chopin missing alternatives**: diff-root append skipped → Gate A sees
  a truncated candidate set.

- **CHORALE 137 tick shift**: Pass 2/2b sub-region analysis was also suppressed in v2;
  the fragile Eø7/D♭ slash sub-region flips and merges into the adjacent Dm, erasing the
  tick-24000 boundary.

v3 fixes all three with four targeted changes.

---

## Changes required

### Part A — `src/composing/analysis/region/regionanalyzer.cpp`

**Enable `suppressProgressionSignals=true` and snapshot capture at Pass 1 only.**

In v2, suppression was enabled at all three `analyzeChord` call sites (Pass 1, Pass 2,
Pass 2b). Pass 2/2b sub-region suppression is what causes the CHORALE 137 cascade.
In v3, suppress ONLY at the Pass 1 site.

**Find the Pass 1 call site** — it is the main region-level `analyzeChord` call,
distinguished by having a non-null `&gateCtx` output arg and using the top-level region
prefs (not sub-region prefs inside a loop). The function layer is called with a real
snapshot pointer at this site in non-no-op mode.

At the Pass 1 call site only, make a local copy of prefs and set:
```cpp
auto pass1Prefs = prefs;
pass1Prefs.suppressProgressionSignals = true;
pass1Prefs.captureScoringSnapshot     = &snapshot;   // pre-declare ScoringSnapshot snapshot;
```

Then call `analyzeChord(..., pass1Prefs, &gateCtx)` and pass `&snapshot` to
`applyHarmonicFunction`.

**Do NOT modify** the Pass 2 or Pass 2b call sites — they remain in non-suppression mode
as before.

---

### Part B — `src/composing/analysis/chord/chordanalyzer.cpp`

**In suppression mode, return pre-built `ChordAnalysisResult` for ALL bass candidates,
not just the suppression-mode winning bass.**

**Locate** the result-building loop at approximately lines 3259–3272:

```cpp
std::vector<ChordAnalysisResult> results;
results.reserve(3);

for (const RawCandidate& rc : rawCandidates) {
    if (!prefs.suppressProgressionSignals) {
        if (results.size() >= 3) { break; }
        if (rc.score < threshold)  { break; }
    }
    results.push_back(buildResult(rc));
}
```

`rawCandidates` holds only the suppression-mode winning bass's sorted cells.

**Change:** In suppression mode, also iterate the other bass candidates and append their
pre-built results. The exact mechanism depends on how `rawCandidates` for other basses is
available at this point in the function — they may be stored in a per-bass staging vector
built during the bass competition loop, or accessible through an existing data structure.

**Whichever approach you use, the requirement is:**
- In suppression mode, `results` (= `candidates[]` returned to the caller) must contain
  pre-built `ChordAnalysisResult` objects for **every** `(bassPc, rootPc, tiePriority)`
  cell that is in `snapshot.cellsWithWDim` and `snapshot.cellsWithoutWDim`.
- Each entry must use the per-bass `buildResult` context (pcWeight, tpcForPc, bassTpc)
  appropriate for its bass PC — not the winning bass's context.
- The ordering does not matter (the function layer sorts by rescored score).
- In non-suppression mode, the result-building loop is **unchanged**.

**Practical implementation hint:** The most natural place to collect all-bass results is
inside the bass competition loop, right after each bass's `rawCandidates` is populated and
before moving to the next bass. In suppression mode, push those candidates into a
staging vector; after the loop assigns `rawCandidates` to the winner, append the other
basses' staged results and push them all into `results` (still without threshold/cap in
suppression mode).

**Expected size of suppressed `results`:** typically ≤4 basses × 12 roots × 17 templates
= ≤816 entries.

---

### Part C — `src/composing/analysis/function/harmonicfunctionlayer.cpp`

**Replace lines ~129–168** (the lookup + promote + trim block) with the corrected version.
**Keep lines 1–127 unchanged** — the `rescore` lambda and quality guard are already correct.

Replace the existing block beginning at `// ── Look up winner in candidates[] ──` with:

```cpp
    // ── Look up winner in candidates[] ─────────────────────────────────────
    //
    // candidates[] now contains pre-built results for ALL basses (Part B).
    // Match on (bassPc, rootPc, tiePriority) to survive cross-bass winner changes.
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
        // Should not happen with all-bass candidates[], but guard defensively.
        // Trim the over-sized suppressed results to 3 and return.
        if (candidates.size() > 3) { candidates.resize(3); }
        return;
    }

    // ── Compute rescored winner score and threshold ──────────────────────────
    //
    // rescore() does not include appliedBassBonus, so the de-inflated threshold
    // collapses to: threshold = winnerScore * kScoreThresholdRatio.
    auto [snw0, sw0] = rescore(*winnerCell);
    const double winnerScore = acceptWithWDim ? sw0 : snw0;

    const double threshold = winnerScore * kScoreThresholdRatio;

    // ── Collect winning-bass candidates, apply threshold + cap-of-3 ──────────
    //
    // Replicate analyzeChord lines 3262–3272 using rescored scores.
    const int winnerBassPc = winnerCell->bassPc;

    // Build (rescored score, index-in-candidates) pairs for the winning bass.
    std::vector<std::pair<double, int>> bassEntries;
    bassEntries.reserve(candidates.size());
    for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
        if (candidates[i].identity.bassPc != winnerBassPc) { continue; }
        // Find the corresponding snapshot cell to get the rescored score.
        // Match on (rootPc, tiePriority) within the winning-variant cells.
        double entryScore = -std::numeric_limits<double>::infinity();
        for (const auto& cell : winningCells) {
            if (cell.bassPc       != winnerBassPc)              { continue; }
            if (cell.rootPc       != candidates[i].identity.rootPc)       { continue; }
            if (cell.tiePriority  != candidates[i].identity.tiePriority)  { continue; }
            auto [snw, sw] = rescore(cell);
            entryScore = acceptWithWDim ? sw : snw;
            break;
        }
        if (entryScore >= threshold) {
            bassEntries.push_back({ entryScore, i });
        }
    }

    // Sort by rescored score descending, then tiePriority ascending (tie-break).
    std::sort(bassEntries.begin(), bassEntries.end(),
        [&](const std::pair<double,int>& a, const std::pair<double,int>& b) {
            if (a.first != b.first) return a.first > b.first;
            return candidates[a.second].identity.tiePriority
                 < candidates[b.second].identity.tiePriority;
        });

    // Cap to 3 (non-suppression cap from analyzeChord L3263-3265).
    if (bassEntries.size() > 3) { bassEntries.resize(3); }

    // ── Pass B — step bonuses ─────────────────────────────────────────────────
    //
    // Snapshot cells are captured pre-Pass-B.  Re-apply step bonuses on the
    // selected top-≤3 cells, matching the applyStepBonusGuard logic.
    // stepIn fires when the bass stepped to this chord from the previous region.
    // stepOut fires when the bass steps from this chord to the next region.
    //
    // Stepwise motion = interval of 1 or 2 semitones (mod 12).
    auto isStepwise = [](int fromPc, int toPc) -> bool {
        if (fromPc < 0 || toPc < 0) return false;
        const int d = ((toPc - fromPc) % 12 + 12) % 12;
        return d == 1 || d == 2 || d == 10 || d == 11;
    };
    const bool stepIn  = isStepwise(ctx.previousBassPc, winnerBassPc);
    const bool stepOut = isStepwise(winnerBassPc, ctx.nextBassPc);

    for (auto& [sc, idx] : bassEntries) {
        const auto& id = candidates[idx].identity;
        using Q = analysis::ChordQuality;
        // Root-position only; Power excluded.
        if (id.rootPc == id.bassPc && id.quality != Q::Power) {
            // m7-family guard: for Minor chords with 4 intervals (Min7),
            // the step bonus may not push score above kStepBudget above the
            // un-bonused score.  Find the cell to get intervalCount.
            bool isMin7 = false;
            for (const auto& cell : winningCells) {
                if (cell.bassPc      == id.bassPc
                    && cell.rootPc   == id.rootPc
                    && cell.tiePriority == id.tiePriority) {
                    isMin7 = (cell.quality == Q::Minor && cell.intervalCount == 4);
                    break;
                }
            }
            double bonus = 0.0;
            if (stepIn  && (!isMin7 || sc + kWStepIn  <= winnerScore + kStepBudget))
                bonus += kWStepIn;
            if (stepOut && (!isMin7 || sc + kWStepOut <= winnerScore + kStepBudget))
                bonus += kWStepOut;
            sc += bonus;
        }
    }

    // Re-sort after Pass B adjustments.
    std::sort(bassEntries.begin(), bassEntries.end(),
        [&](const std::pair<double,int>& a, const std::pair<double,int>& b) {
            if (a.first != b.first) return a.first > b.first;
            return candidates[a.second].identity.tiePriority
                 < candidates[b.second].identity.tiePriority;
        });

    // ── Diff-root append (replicate analyzeChord L3291–3312) ─────────────────
    //
    // If every entry in the top-≤3 shares the winner's rootPc, append the
    // highest-scored different-root candidate that clears the threshold,
    // provided the winner is root-position and inversionSuspicionMargin > 0.
    const int winnerRootPc = candidates[bassEntries[0].second].identity.rootPc;
    const bool winnerIsRootPos = (winnerRootPc == winnerBassPc);

    if (winnerIsRootPos && prefs->inversionSuspicionMargin > 0.0) {
        const bool hasDiffRoot = std::any_of(
            bassEntries.begin(), bassEntries.end(),
            [&](const std::pair<double,int>& e) {
                return candidates[e.second].identity.rootPc != winnerRootPc;
            });

        if (!hasDiffRoot) {
            // Scan all winning-bass candidates for best above-threshold diff-root.
            double bestDiffScore = -std::numeric_limits<double>::infinity();
            int    bestDiffIdx   = -1;
            for (int i = 0; i < static_cast<int>(candidates.size()); ++i) {
                if (candidates[i].identity.bassPc  != winnerBassPc) { continue; }
                if (candidates[i].identity.rootPc  == winnerRootPc) { continue; }
                // Get rescored score for this cell.
                double sc = -std::numeric_limits<double>::infinity();
                for (const auto& cell : winningCells) {
                    if (cell.bassPc     != winnerBassPc)                      { continue; }
                    if (cell.rootPc     != candidates[i].identity.rootPc)     { continue; }
                    if (cell.tiePriority!= candidates[i].identity.tiePriority){ continue; }
                    auto [snw, sw] = rescore(cell);
                    sc = acceptWithWDim ? sw : snw;
                    break;
                }
                if (sc >= threshold && sc > bestDiffScore) {
                    bestDiffScore = sc;
                    bestDiffIdx   = i;
                }
            }
            if (bestDiffIdx >= 0) {
                bassEntries.push_back({ bestDiffScore, bestDiffIdx });
            }
        }
    }

    // ── Rebuild candidates[] from selected entries ────────────────────────────
    std::vector<analysis::ChordAnalysisResult> newResults;
    newResults.reserve(bassEntries.size());
    for (const auto& [sc, idx] : bassEntries) {
        newResults.push_back(candidates[idx]);
        newResults.back().identity.score = sc;
    }

    candidates = std::move(newResults);
    chosenResult = candidates[0];
```

---

### Part D — `src/composing/analysis/function/harmonicfunctionlayer.h`

Add the threshold ratio constant alongside the existing bonus constants:

```cpp
inline constexpr double kScoreThresholdRatio = /* copy value from chordanalyzer.cpp */;
```

Find `kScoreThresholdRatio` in `chordanalyzer.cpp` (it is a `constexpr double` defined near
the top of the scoring constants block) and reproduce the same value here.

Also update the stale comment at `harmonicfunctionlayer.h:127–132` (the "INCLUDES the
rootContinuityBonus / E2c deducts" block on `ScoringCell::basisIndep`) to reflect that
in suppression-mode capture, `basisIndep` is **clean** (no rcb folded in), and the
function layer **adds** rcb before the cf×af multiply. This is documentation only — no
struct changes needed.

---

## Build and test sequence

```
# Build
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Composing tests
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp.txt 2>&1; echo "exit:$?"
tail -5 /tmp/comp.txt

# Notation tests (includes pipeline snapshot)
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/nota.txt 2>&1; echo "exit:$?"
tail -5 /tmp/nota.txt

# Pipeline snapshot tests — must be byte-identical, NO --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap.txt 2>&1; echo "exit:$?"
cat /tmp/snap.txt

# Mismatch report
cat C:\s\MS\src\composing\tests\chord_mismatch_report.txt | head -20
```

---

## Acceptance criteria

- All 11 pipeline snapshot tests pass **without `--update-goldens`** — byte-identical.
- `composing_tests.exe`: 407/407 (or current baseline) — no regressions.
- `notation_tests.exe`: 52/52 (or current baseline) — no regressions.
- Mismatch report: at or below current baseline (Baroque ≤25, Jazz ≤13).

---

## Hard stops — revert and report if any of these occur

1. Any pipeline snapshot test fails — even one.
2. Any composing or notation test that previously passed now fails.
3. Any BIR increase in Baroque or Jazz corpus.
4. `--update-goldens` is required to make snapshot tests pass — this means the
   function layer is producing different output than non-suppression mode and is
   **not** acceptable.

---

## Canary tests for the two mechanisms

**Mechanism (A) — cross-bass fix:**
- `bach_bwv806_prelude`: tick 7920 must still show F#7/C# (= V7/ii) in `implode` and
  `annotation` sections. This is the definitive cross-bass test.
- `chopin_bi105_op30_2`: zero diff-root 2-alt entries in the golden, so any remaining
  failure here is a pure cross-bass issue — the canary for (A) working independently of (B).

**Mechanism (B) — diff-root append fix:**
- `mozart_k279_1` tick 1920: `tickRegional.alternatives` must contain both D/minor
  and F/major (two entries). In v2 only D/minor appeared.
- `chopin_bi105_op30_1` tick 1920: same pattern (C/minor + Ab/major).

**Mechanism (cascade) — Pass 2/2b suppression removed:**
- `bach_chorale_137` tick 24000: must still show E/halfDiminished (Em7b5/Db),
  not D/minor. The tick must NOT shift.

---

## Notes

- Do not modify `docs/scoring_model.md` in this commit — no new scoring terms are added.
- Do not update any golden files.
- The only files that should change are:
  `src/composing/analysis/region/regionanalyzer.cpp`
  `src/composing/analysis/chord/chordanalyzer.cpp`
  `src/composing/analysis/function/harmonicfunctionlayer.cpp`
  `src/composing/analysis/function/harmonicfunctionlayer.h`
- If you discover that the all-bass candidate collection in Part B requires touching
  additional files (e.g., a helper header), that is acceptable — note it in your report.
- Commit only if all acceptance criteria are met. Commit message:
  `E2d-enable v3: function layer global-bass rebuild + diff-root append replication`
