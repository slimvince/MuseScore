# Iteration 2: Move temporal context into the shared pipeline

## ⚠ Critical behaviour rules for this session

- **Think, investigate, and REPORT before implementing each step.**
  Read the relevant code section, describe what you see and what you plan to change,
  then implement. If anything does not match what this document describes, STOP
  and report before proceeding.
- **Make only the changes listed in this document.** Do not refactor, improve,
  or simplify anything not explicitly listed here.
- **Do not retire `analyzeScore()`.** That is deferred to a separate iteration.
- **Do not touch `chordanalyzer.cpp` or `chordanalyzer.h`** (no scoring changes,
  no gate changes — those are Iteration 3).
- **Do not commit until all verification steps pass.** Then push as instructed.
- If the build fails or any test regresses, STOP immediately and report verbatim.

---

## Step 1 — Context loading (read ALL before touching any code)

1. `CLAUDE.md`
2. `STATUS.md` — top summary + 2026-05-04 and 2026-05-05 entries only
3. `ARCHITECTURE.md` — §2.10, §4.1c, §4.1d in full
4. `docs/unified_analysis_pipeline.md` — in full
5. `docs/prompts/iteration_plan_inversion_redesign.md` — in full

Then read these implementation files before changing anything:
6. The full `ChordTemporalExtensions` struct and `toExtensionsSnapshot()` function.
   (Iteration 1 report: defined in `harmonicrhythm.h` lines ~40–58. Find the exact
   path and read both in full.)
7. The `ChordTemporalContext` struct in `chordanalyzer.h` — confirm the four fields
   `nextRootPc`, `consecutiveBassStepwiseCount`, `recentRootPcs`, `regionMetricWeight`
   are present.
8. The §4.1c main loop in `notationharmonicrhythmbridge.cpp` — the full per-region
   block from the `findTemporalContext()` call through to the rolling-forward of
   `previousRootPc/Quality/BassPc`. Read every line.
9. The Pass 2 and Pass 2b sub-region loops in the same file — read in full.
10. The relevant section of `batch_analyze.cpp`'s `analyzeScore()` private function
    where the four new fields are currently computed (search for `consecutiveBassStepwiseCount`).

After reading, briefly confirm in your report that you found and understood each item.

---

## Step 2 — Verify current state before changing anything

Confirm:
A. `ChordTemporalExtensions` has exactly 5 fields: `previousRootPc`, `previousBassPc`,
   `previousQuality`, `bassIsStepwiseFromPrevious`, `bassIsStepwiseToNext`.
   The four new fields are NOT present.
B. `toExtensionsSnapshot()` copies exactly those 5 fields and nothing else.
C. The §4.1c main loop in `notationharmonicrhythmbridge.cpp` does NOT set
   `ctx.nextRootPc`, `ctx.consecutiveBassStepwiseCount`, `ctx.recentRootPcs`,
   or `ctx.regionMetricWeight`.
D. `batch_analyze.cpp` `analyzeScore()` DOES set all four fields (as per Iteration 1).
E. A function called `regionMetricWeightForBeatType` (or equivalent) exists in
   `batch_analyze.cpp`. Report its exact implementation.

Report findings for A–E. If anything differs from the above, report and STOP.

---

## Step 3 — Changes to make

Implement ONLY the following, in order. After each sub-step, report what you changed
before moving to the next.

### Sub-step 3a — Extend ChordTemporalExtensions

In the header file containing `ChordTemporalExtensions` (found in Step 1 item 6),
add four new fields to the struct:

```cpp
int nextRootPc = -1;                          ///< Root PC of next region; -1 = unknown.
int consecutiveBassStepwiseCount = 0;         ///< Consecutive stepwise bass moves ending here.
std::array<int, 3> recentRootPcs = {-1,-1,-1};///< Root PCs of 3 most recent regions.
double regionMetricWeight = 1.0;              ///< Metric weight [0,1]; 1 = downbeat.
```

Then update `toExtensionsSnapshot()` to copy all four new fields from the
`ChordTemporalContext` argument into the returned `ChordTemporalExtensions`.
The snapshot must mirror exactly what the context held at the time of the
`analyzeChord` call.

### Sub-step 3b — Add regionMetricWeightForBeatType helper

In `notationharmonicrhythmbridge.cpp`, add a file-local helper function that converts
a `BeatType` enum value to a normalised [0,1] weight — the same logic as
`batch_analyze.cpp`'s equivalent function. Use the exact same mapping so both paths
produce identical weights for the same beat type.

Do NOT copy this from batch_analyze.cpp into the bridge as a verbatim duplicate with
no shared definition. If a shared location (e.g. a composing-module utility header)
is available and appropriate, put it there and include it from both sites. If not,
implement it in the bridge and add:
```cpp
// TODO (ARCHITECTURE.md §2.10): duplicate of batch_analyze.cpp's
// regionMetricWeightForBeatType. Move to a shared composing-module utility.
```

### Sub-step 3c — Add rolling state before the §4.1c main loop

In `notationharmonicrhythmbridge.cpp`, immediately after the `findTemporalContext()`
call that seeds the initial context (the one at ~line 214 before the region loop),
add:

```cpp
int runningStepwiseCount = 0;
std::array<int, 3> recentRootsBuf = {-1, -1, -1};
```

### Sub-step 3d — Populate four fields per region, before analyzeChord

In the §4.1c per-region block, immediately before the main `analyzeChord` call,
add the following (in this order):

```cpp
// Temporal context — rolling signals
ctx.consecutiveBassStepwiseCount = runningStepwiseCount;
ctx.recentRootPcs = recentRootsBuf;
ctx.regionMetricWeight = regionMetricWeightForBeatType(
    safeBeatType(currentMeasure, regionStartSegment));
```

Then, in the existing look-ahead block that already computes `nextBassPc` (the block
around lines 243–262 that calls `collectRegionTones` for the next boundary), extend
it to also infer `nextRootPc`:

```cpp
// Already present: collect nextTones for the next region
// ADD: lightweight root inference from next region's tones
if (!nextTones.empty()) {
    const auto nextCandidates = chordAnalyzer->analyzeChord(
        nextTones, localKeyFifths, localKeyMode, nullptr, chordPrefs);
    if (!nextCandidates.empty()) {
        ctx.nextRootPc = nextCandidates[0].identity.rootPc;
    }
}
```

Use the same `chordPrefs` already in scope. Pass `nullptr` for context (no temporal
context for the look-ahead call itself — it is a lightweight root estimate only).

### Sub-step 3e — Update rolling state after analyzeChord

After the `analyzeChord` call and after the existing roll of
`ctx.previousRootPc/Quality/BassPc`, add:

```cpp
// Update rolling state for next region
if (ctx.bassIsStepwiseFromPrevious) {
    ++runningStepwiseCount;
} else {
    runningStepwiseCount = 0;
}
recentRootsBuf[2] = recentRootsBuf[1];
recentRootsBuf[1] = recentRootsBuf[0];
recentRootsBuf[0] = chosenResult.identity.rootPc;   // use the winner's rootPc
// Reset nextRootPc for next iteration
ctx.nextRootPc = -1;
```

Confirm the variable name for the winning result — it may be `chosenResult`,
`candidates.front()`, or similar. Use whatever name the existing code uses.

### Sub-step 3f — Handle Pass 2 and Pass 2b sub-region loops

The Pass 2 (onset sub-boundary) and Pass 2b (bass-movement sub-boundary) loops create
`subCtx` from the preceding region's result. For these sub-loops:

- Set `subCtx.consecutiveBassStepwiseCount` from the parent region's
  `temporalExtensions.consecutiveBassStepwiseCount` (carry forward)
- Set `subCtx.recentRootPcs` from the parent region's
  `temporalExtensions.recentRootPcs` (carry forward)
- Set `subCtx.regionMetricWeight` using `regionMetricWeightForBeatType` for the
  sub-region's start segment
- Leave `subCtx.nextRootPc = -1` (consistent with the current
  `subCtx.bassIsStepwiseToNext = false` treatment for sub-regions)

Add this TODO comment:
```cpp
// TODO: Sub-region temporal context carries parent state for rolling signals.
// For full fidelity, sub-regions should compute their own rolling counts and
// nextRootPc look-ahead. Deferred.
```

### Sub-step 3g — Remove duplicate computation from batch_analyze.cpp

In `batch_analyze.cpp`'s `analyzeScore()` private function, remove ONLY the four
lines that compute `consecutiveBassStepwiseCount`, `recentRootPcs`,
`regionMetricWeight`, and `nextRootPc` on `ctx`. Do not change anything else in
`analyzeScore()`. Do not retire `analyzeScore()` itself.

After removal, those four fields will be default-valued in the batch path (0, {-1,-1,-1},
1.0, -1). This is a temporary regression in batch-path quality that will be resolved
when `analyzeScore()` is retired in a later iteration. Add this comment:

```cpp
// NOTE: consecutiveBassStepwiseCount, recentRootPcs, regionMetricWeight, nextRootPc
// are no longer populated here. They are now computed in the shared bridge pipeline
// (notationharmonicrhythmbridge.cpp). analyzeScore() is a parallel legacy path
// pending retirement (see iteration_plan_inversion_redesign.md). Until retirement,
// these fields default to 0 / {-1,-1,-1} / 1.0 / -1 in the batch path.
// TODO (ARCHITECTURE.md §2.10): retire analyzeScore() and route batch mode through
// analyzeScoreNotationPrepared() to restore these fields in the batch path.
```

**Important:** After this sub-step, the four temporal context fields will be absent
from the batch corpus pipeline. The Iteration 3 gates will therefore NOT fire on batch
corpus runs until `analyzeScore()` is retired. This is expected and acceptable for
Iteration 2. The iteration plan accounts for this — Iteration 3 must verify that
gates fire correctly on the bridge paths.

---

## Step 4 — Build and test

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.

If any test regresses: STOP. Report verbatim. Do not attempt to fix.

---

## Step 5 — Corpus run (expect no change from Iteration 0 baseline)

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

The corpus numbers should be unchanged from the Iteration 0 baseline (119 genuine
BIR=true, 252 BIR=false) because no scoring or gate logic was changed in this
iteration — only context population was added. If numbers change unexpectedly, STOP
and report before proceeding.

---

## Step 6 — Verify all paths receive the new fields

Without making code changes, verify that the new temporal context fields flow through
to consumers. Add temporary diagnostic output or use the existing diagnostic structs
to confirm:

- A representative Bach chorale region in the bridge path now has non-default values
  for `temporalExtensions.consecutiveBassStepwiseCount`, `.recentRootPcs`,
  `.regionMetricWeight`. Report example values.
- `AnalyzedRegion.temporalExtensions.nextRootPc` is non-(-1) for at least some
  non-phrase-final regions.

If diagnostic output is not practical without invasive changes, report instead by
reading the code and confirming the data flow is wired correctly end-to-end.

---

## Step 7 — GitHub push

After clean build + 407/407 pass + no unexpected corpus changes:

```
cd C:\s\MS && git add -A && git commit -m "Temporal context: add 4 new fields to shared bridge pipeline" && git push
```

---

## Step 8 — Report

```
Context loading confirmed:         yes / issues: <list>
State verification (A–E):          all confirmed / differences: <list>
Changes made (per sub-step):
  3a ChordTemporalExtensions:      4 fields added; toExtensionsSnapshot updated
  3b regionMetricWeightForBeatType: added to bridge / shared location: <path>
  3c Rolling state vars:           added before §4.1c loop
  3d Per-region population:        nextRootPc, consecutiveCount, recentRoots,
                                   metricWeight all set before analyzeChord
  3e Rolling state update:         runningStepwiseCount + recentRootsBuf updated
  3f Sub-region loops:             handled with parent-carry + TODO
  3g batch_analyze.cpp:            4-field computation removed + NOTE comment
Build:                             pass / fail
Tests:                             407/407 pass / regressions: <list>
RealDiff:                          ≤ 4
Corpus preset:                     Baroque (confirm)
3-way genuine BIR=true:            119 (expected — no change)
3-way genuine BIR=false:           252 (expected — no change)
Path verification:
  Bridge path temporal fields:     populated (example: <region, values>)
  Batch path temporal fields:      absent (expected — noted in 3g comment)
GitHub push:                       done / commit hash
Unexpected findings:               none / <describe>
```
