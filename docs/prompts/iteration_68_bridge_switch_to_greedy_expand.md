# Iteration 68: Switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=5, BIR=false=125. Jazz BIR=false=12.
(Iter 67 committed dc52617762 — greedy-expand extracted to src/composing/analysis/harmony/harmonicsegmenter.h with HarmonicSegmenterCallbacks deviation; BIR=true=5, BIR=false=125 confirmed.)

**Prerequisite**: Iter 67 is committed (dc52617762). Push it before starting:
```bash
git push
```
Confirm `src/composing/analysis/harmony/harmonicsegmenter.h` exists and
`greedyExpandSegmentation()` accepts a `HarmonicSegmenterCallbacks` final parameter.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

The bridge path (`src/notation/internal/notationcomposingbridgehelpers.cpp`) is the
live user-facing chord analysis path — called per-keypress via `harmonicAnnotation`.
It currently uses `detectHarmonicBoundariesJaccard()` for segmentation. The batch
path has used greedy-expand since Iter 54 (commit `f92a4f1a3b`).

Unifying the bridge removes the last divergence between the two paths (§2.10
compliance). Expected effect: the two remaining Hypothesis A BIR=true cases
(bwv184.5 m=13 b=4.0 over-merge, bwv372 m=10 b=1.5 missing Bb) may resolve because
greedy-expand's boundary detection is structurally superior to Jaccard for these cases.

BIR=false may shift — the bridge change affects the live annotation path used by the
pipeline snapshot tests, so golden refresh is expected.

**Files changed in this iteration** (all pre-authorized per CLAUDE.md or explicitly
here):
- `src/notation/internal/notationcomposingbridgehelpers.cpp` — switch segmentation
- Pipeline snapshot goldens (`src/notation/tests/`) — refresh if needed

---

## Step 1 — Read the bridge segmentation call site

Read `src/notation/internal/notationcomposingbridgehelpers.cpp`.

Find:
1. Where `detectHarmonicBoundariesJaccard()` is called and what it returns
   (a sorted vector of Fraction boundary ticks).
2. How those ticks are consumed downstream (the loop that calls `collectRegionTones`
   + `analyzeChord` per region).
3. What context is available at the call site: Score*, tick range, excludeStaves,
   ChordAnalyzerPreferences, IChordAnalyzer*, keyFifths, keyMode.

Report this call-site structure in the Step 8 report so it is documented.

---

## Step 2 — Read harmonicsegmenter.h and bridge helpers before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.h` in full.

Note that CC deviated from the prompt's original signature in Iter 67: the
extracted `greedyExpandSegmentation()` takes a `HarmonicSegmenterCallbacks`
struct as a final parameter (instead of baking in `staffIsEligible` and
`collectRegionTones`). The actual signature is:

```cpp
std::vector<PlacedRegion>
greedyExpandSegmentation(const Score* score,
                         const Fraction& startTick,
                         const Fraction& endTick,
                         const std::set<size_t>& excludeStaves,
                         const analysis::ChordAnalyzerPreferences& prefs,
                         analysis::IChordAnalyzer* chordAnalyzer,
                         int globalKeyFifths,
                         analysis::KeySigMode globalKeyMode,
                         const HarmonicSegmenterCallbacks& callbacks);
```

The `HarmonicSegmenterCallbacks` struct requires:
- `staffIsEligible`: `std::function<bool(size_t staffIdx)>`
- `collectRegionTones`: `std::function<std::vector<analysis::ChordAnalysisTone>(int startTick, int endTick)>`

The bridge already has its own `collectRegionTones()` static function (line ~797)
and its own staff-eligibility logic. These become the callbacks. Read both before
writing the call site.

---

## Step 3 — Replace Jaccard with greedy-expand in the bridge

At the bridge call site identified in Step 1:

1. Include `src/composing/analysis/harmony/harmonicsegmenter.h`.
2. Construct the callbacks from the bridge's existing helpers and replace the
   `detectHarmonicBoundariesJaccard(...)` call with:
   ```cpp
   mu::composing::HarmonicSegmenterCallbacks segCallbacks;
   segCallbacks.staffIsEligible = [&](size_t staffIdx) -> bool {
       // mirror the bridge's existing staff-eligibility logic here
   };
   segCallbacks.collectRegionTones = [&](int startTick, int endTick)
       -> std::vector<mu::composing::analysis::ChordAnalysisTone> {
       return collectRegionTones(score, startTick, endTick, excludeStaves,
                                 chordPrefs);  // adjust args to match bridge signature
   };

   const auto placedRegions = mu::composing::greedyExpandSegmentation(
       score, startTick, endTick, excludeStaves,
       chordPrefs, chordAnalyzer, keyFifths, keyMode, segCallbacks);
   const auto boundaryTicks = mu::composing::placedRegionsToTicks(placedRegions);
   ```
   (`placedRegionsToTicks` gives the same sorted Fraction tick vector that Jaccard
   returned — the downstream consumption loop is unchanged.)

   Adjust lambda captures and argument lists to match the actual bridge signatures
   found in Step 1. Do not guess — read first.

3. Do NOT remove `detectHarmonicBoundariesJaccard()` from this file in this
   iteration — leave it in place (dead code is acceptable here; removal is a
   separate cleanup step). If removing it would cause a compile error elsewhere,
   leave it.

4. Do NOT change `collectRegionTones()`, the per-region `analyzeChord()` loop,
   or any other bridge logic — only the boundary-detection call changes.

---

## Step 4 — Build and run test suites

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 composing. Notation tests may have pipeline snapshot failures —
expected because the bridge output changes. Do NOT refresh goldens yet.

---

## Step 5 — Run Baroque corpus and BIR

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Record BIR=true and BIR=false. Check whether bwv184.5 m=13 b=4.0 and bwv372
m=10 b=1.5 (Hypothesis A cases) changed.

Hard stops:
- BIR=false increases > 10 above 125 — revert and report.
- BIR=true increases — revert immediately.

If BIR improves or holds: proceed to Jazz validation.

---

## Step 6 — Jazz validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz BIR=false hard stop: ≤75 (current 12). Restore Baroque after:

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
```

---

## Step 7 — Refresh pipeline snapshot goldens (if BIR acceptable)

If BIR=true did not increase and BIR=false is within tolerance:

```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

All pipeline snapshots must pass after golden refresh. If any fail after refresh,
the bridge change introduced an inconsistency — revert and report.

---

## Step 8 — Check bwv227.7 regression

The pre-existing `assert_bwv227_measure9_contains_e` regression (introduced by
the upstream merge, not by our code) should be noted but does not block this
iteration. Record whether it still fails or unexpectedly resolves.

---

## Step 9 — Commit

```bash
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/  # golden files
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Replace detectHarmonicBoundariesJaccard() in notationcomposingbridgehelpers.cpp
with greedyExpandSegmentation() from src/composing/analysis/harmony/harmonicsegmenter.h.
placedRegionsToTicks() provides the same Fraction-tick interface downstream.

Bridge and batch paths now use the same segmentation algorithm (§2.10 compliance).
detectHarmonicBoundariesJaccard() left in place (dead code) pending cleanup.

BIR=true: 5 → N  BIR=false: 125 → N  Jazz BIR=false: 12 → N
Pipeline snapshot goldens refreshed."

git push
```

---

## Step 10 — Report to Cowork

```
Bridge call site: [describe — what Jaccard returned, how ticks were consumed]

BIR after bridge switch:
  Baroque BIR=true: 5 → N
  Baroque BIR=false: 125 → N
  Jazz BIR=false: 12 → N

Hypothesis A cases:
  bwv184.5 m=13 b=4.0: [resolved / unchanged / changed but wrong]
  bwv372 m=10 b=1.5: [resolved / unchanged / changed but wrong]

bwv227.7 regression: [still fails / unexpectedly resolved]

Tests:
  composing: N/407
  notation: N/53
  pipeline_snapshot: N/N (goldens refreshed: [yes/no])

Committed: [yes — hash / not committed — reason]

Remaining BIR=true: N
```
