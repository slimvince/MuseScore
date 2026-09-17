# CC Instruction: Phase D — re-analyze inline-merged arpeggio runs

## Pre-reading (mandatory)

Read in order:
1. `C:\s\MS\CLAUDE.md`
2. `C:\s\MS\STATUS.md` (header only — baselines and HEAD commit)
3. `C:\s\MS\build_and_test.md`
4. `C:\s\MS\docs\scoring_model.md` (you are touching the analyzeChord pipeline)
5. `C:\s\MS\docs\redesign_plan.md` Step 4 (Phase D section — read the FULL section,
   including both dead-end records and the "actual mechanism" subsection)

Note: `cc_instruction_phase_d_merger.md` is **superseded**. Ignore it entirely.
The short-region external merger was confirmed dead code in the Part A spot-check.

---

## What this is

A targeted modification to the `runPass1` lambda in `regionanalyzer.cpp`.

The Pass 1 loop already fuses adjacent arpeggio slices via the inline same-root-quality
merge (lines 510–518). The bug is that after fusing, `regions.back().chordResult` still
holds the first sub-slice's stale identity — the oracle was never re-run on the combined
tone set. This instruction adds that re-run.

**Constraint:** Change only `regionanalyzer.cpp`. No scoring changes, no gate changes,
no template additions, no other files. The entire fix lives inside the `runPass1` lambda
(or a private helper it calls).

---

## Background: what the existing merge does and what is missing

Inside the Pass 1 loop (lines 506–530):

```cpp
if (isContiguousWithPreviousRegion
    && regions.back().chordResult.identity.rootPc == chosenResult.identity.rootPc
    && regions.back().chordResult.identity.quality == chosenResult.identity.quality) {
    regions.back().endTick = regionEnd.ticks();
    mergeChordAnalysisTones(regions.back().tones, tones);   // ← tones are correct
    // ← chordResult.identity.rootPc is NEVER updated                     ← BUG
} else {
    // ... push new independent region ...
}
```

After the merge, `regions.back().tones` is the full duration-weighted aggregate. For
bwv102.7, the 720-tick aggregate `{C,D,Eb,G,Ab,Bb}` clearly picks AbMaj7 when the
oracle sees it without rcb interference. But the oracle is never called again.

The `advanceTemporalContext` call (line 473) runs BEFORE the merge check (line 506).
So by the time the merge fires for sub-slice 2, `temporalCtx.previousRootPc` is already
Eb (committed from sub-slice 1). Any re-analysis must use the context from BEFORE
sub-slice 1 was analyzed — the **run-opening context**.

---

## Implementation

### New local variables

Add immediately before the `for` loop (before line 390):

```cpp
// Phase D: track inline-merge runs for re-analysis.
// runOpeningCtx  — temporal context saved at the start of each new independent run
//                  (the state before sub-slice 1's analysis, so no rcb contamination).
// runMergeCount  — number of sub-slices merged into regions.back() since the last
//                  independent-region push. 0 means no merge is pending.
ChordTemporalContext runOpeningCtx = temporalCtx;
int runMergeCount = 0;
ChordTemporalContext ctxAtIterStart = temporalCtx;   // scratch, updated each iteration
```

### Save context at the top of each iteration

At the very top of the `for` loop body (before line 395, before `collectRegionTones`):

```cpp
ctxAtIterStart = temporalCtx;
```

This captures the predecessor fields (`previousRootPc`, `previousQuality`,
`previousBassPc`, `previousDistinctPcs`, `previousWinnerScore`,
`previousWinnerMargin`) before either per-region setup or `advanceTemporalContext`
modifies them.

### Track merges in the merge branch (line 510–518)

Inside the `if (isContiguousWithPreviousRegion && ...)` block, after the existing
`mergeChordAnalysisTones` call:

```cpp
runMergeCount++;
// runOpeningCtx is NOT updated here — it was set when this run started.
```

### Re-analyze at the else branch (line 519)

At the VERY START of the `else` block, before the `HarmonicRegion region;` creation:

```cpp
if (runMergeCount >= 1) {
    phaseDReanalyzeRun(regions, runOpeningCtx,
                       tones, localKeyFifths, localKeyMode,
                       chordAnalyzer, attemptPrefs, temporalCtx,
                       score, runningStepwiseCount, recentRootsBuf,
                       chosenResult);
    // After this call:
    // - regions.back().chordResult is corrected.
    // - temporalCtx is rebuilt from runOpeningCtx → advance(corrected) → advance(chosenResult).
    // - chosenResult is re-analyzed with the corrected predecessor context.
}
runOpeningCtx = ctxAtIterStart;
runMergeCount = 0;
```

### Re-analyze after the loop ends

After the closing `}` of the `for` loop (before `return regions;`, line 533):

```cpp
if (runMergeCount >= 1 && !regions.empty()) {
    // The final merged run was never closed by an 'else' branch.
    // Re-analyze it now. No subsequent region exists so we only fix the merged region
    // and update temporalCtx (it won't affect anything else, but keep it consistent).
    ChordTemporalContext dummyCtx = temporalCtx;
    ChordAnalysisResult dummyChosenResult;  // ignored — no subsequent region
    phaseDReanalyzeRun(regions, runOpeningCtx,
                       {}, localKeyFifths, localKeyMode,   // empty tones: no successor
                       chordAnalyzer, attemptPrefs, dummyCtx,
                       score, runningStepwiseCount, recentRootsBuf,
                       dummyChosenResult);
    // Note: temporalCtx here is not the dummyCtx; only update if it matters for callers.
}
```

(If `localKeyFifths`/`localKeyMode` are not in scope outside the loop, declare them
at a wider scope or pass the last-seen values. Adapt as needed to compile cleanly.)

---

## Helper function: `phaseDReanalyzeRun`

Add a `static` helper inside the anonymous namespace (or as a lambda inside
`runPass1`, whichever is cleaner). It has no counterpart in the existing API.

### Purpose

Given an already-merged region (`regions.back()` with correct combined tones but stale
identity) and the run-opening temporal context, re-run the full oracle pipeline on the
combined tones and update the region. Also fix `temporalCtx` and optionally re-analyze
the current/next slice (`chosenResult`) with the corrected predecessor.

### Inputs

| parameter | meaning |
|-----------|---------|
| `regions` | the `HarmonicRegion` vector; last entry is the merged run |
| `runOpeningCtx` | temporalCtx saved at the start of sub-slice 1 (predecessor fields correct) |
| `nextTones` | tones of the successor region (the current `else`-branch slice); may be empty for end-of-loop call |
| `keyFifths`, `keyMode` | key at the merged region (use `regions.back().keyModeResult`) |
| `chordAnalyzer` | the oracle |
| `prefs` | `attemptPrefs` |
| `temporalCtx` (in/out) | will be rebuilt to a consistent state after the call |
| `score`, `runningStepwiseCount`, `recentRootsBuf` | for `advanceTemporalContext` |
| `chosenResult` (in/out) | the current-slice result; if `nextTones` non-empty, re-analyzed with corrected predecessor |

### Algorithm

```
1. Build reCtx from runOpeningCtx:
   - Copy all predecessor fields as-is.
   - Recompute regionMetricWeight from regions.back().startTick (the merged region's
     start tick, NOT the current iteration's tick).  Use the same pattern as line 439–443.
   - Set nextRootPc from inferNextRootPc(chordAnalyzer, nextTones, keyFifths, keyMode)
     if nextTones is non-empty; otherwise leave as -1.
   - Set nextBassPc from bass tone of nextTones (first tone with isBass=true); or -1.
   - Set bassIsStepwiseToNext from mergedRegion's bassPc and nextTones' bassPc.
   - Set bassIsStepwiseFromPrevious from runOpeningCtx.previousBassPc and
     mergedRegion's bassPc (regions.back().chordResult.identity.bassPc).

2. Call oracle on merged region:
   PostScoringGateContext reGateCtx;
   auto reResults = chordAnalyzer->analyzeChord(
       regions.back().tones, keyFifths_from_mergedRegion, keyMode_from_mergedRegion,
       &reCtx, prefs, &reGateCtx);
   applyIter8691Pedal(reResults, reGateCtx, &reCtx, prefs);
   applyPostScoringGates(reResults, prefs, &reCtx, reGateCtx);
   if (reResults.empty()) return;  // safety: keep stale identity if oracle fails

3. Update merged region:
   regions.back().chordResult = reResults.front();
   regions.back().alternatives = {reResults.begin()+1, reResults.end()};
   regions.back().temporalExtensions = toExtensionsSnapshot(runOpeningCtx);
   // Update bassPc from merged tones (bassToneFromTones already ran during
   // the inline merge; just re-run to be safe):
   if (const auto* bt = bassToneFromTones(regions.back().tones)) {
       regions.back().chordResult.identity.bassPc = bt->pitch % 12;
       regions.back().chordResult.identity.bassTpc = bt->tpc;
   }

4. Rebuild temporalCtx after the corrected merged region:
   ChordTemporalContext ctxAfterMerge = runOpeningCtx;
   advanceTemporalContext(ctxAfterMerge, runningStepwiseCount, recentRootsBuf,
                          regions.back().chordResult.identity);
   // Also update the winner-score fields on ctxAfterMerge:
   {
       const int winRoot = regions.back().chordResult.identity.rootPc;
       ctxAfterMerge.previousWinnerRootPcWeight =
           (winRoot >= 0) ? reGateCtx.pcWeight[static_cast<size_t>(winRoot)] : 0.0;
       ctxAfterMerge.previousDistinctPcs = reGateCtx.distinctPcs;
       ctxAfterMerge.previousWinnerScore = reGateCtx.rawCandidates.empty()
           ? 0.0 : reGateCtx.rawCandidates[0].score;
       ctxAfterMerge.previousWinnerMargin = (reGateCtx.rawCandidates.size() >= 2)
           ? reGateCtx.rawCandidates[0].score - reGateCtx.rawCandidates[1].score
           : -1.0;
   }

5. If nextTones is non-empty, re-analyze the current (successor) slice:
   - Build nextCtx = ctxAfterMerge (the corrected predecessor context).
   - Populate nextCtx per-region fields (nextRootPc lookahead for the slice AFTER
     nextTones — i.e., two positions ahead; or just leave nextRootPc = -1 for
     simplicity since the current slice's nextRootPc was already set in the loop).
   - Actually: keep the per-region lookahead fields (nextRootPc, nextBassPc, 
     regionMetricWeight, bassIsStepwiseToNext) as they were already set in the
     loop body (lines 419-443) for the current iteration.  The predecessor fields
     are what changed.  So: copy ONLY the predecessor fields from ctxAfterMerge
     into a copy of the current iteration's temporalCtx state (which already has
     correct per-region fields).
   
   The cleanest approach:
   ChordTemporalContext reCurrentCtx = temporalCtx;  // has correct per-region fields
   reCurrentCtx.previousRootPc   = ctxAfterMerge.previousRootPc;
   reCurrentCtx.previousQuality  = ctxAfterMerge.previousQuality;
   reCurrentCtx.previousBassPc   = ctxAfterMerge.previousBassPc;
   reCurrentCtx.previousDistinctPcs       = ctxAfterMerge.previousDistinctPcs;
   reCurrentCtx.previousWinnerRootPcWeight = ctxAfterMerge.previousWinnerRootPcWeight;
   reCurrentCtx.previousWinnerScore       = ctxAfterMerge.previousWinnerScore;
   reCurrentCtx.previousWinnerMargin      = ctxAfterMerge.previousWinnerMargin;
   // Also copy the recentRootsBuf-related state if advanceTemporalContext updates it.
   
   PostScoringGateContext nextGateCtx;
   auto nextResults = chordAnalyzer->analyzeChord(
       nextTones, keyFifths, keyMode, &reCurrentCtx, prefs, &nextGateCtx);
   applyIter8691Pedal(nextResults, nextGateCtx, &reCurrentCtx, prefs);
   applyPostScoringGates(nextResults, prefs, &reCurrentCtx, nextGateCtx);
   if (!nextResults.empty()) {
       chosenResult = nextResults.front();  // caller uses this to push the new region
   }
   
   // Rebuild full temporalCtx after the current slice:
   temporalCtx = ctxAfterMerge;
   advanceTemporalContext(temporalCtx, runningStepwiseCount, recentRootsBuf,
                          chosenResult);
   {
       const int winRoot = chosenResult.identity.rootPc;
       temporalCtx.previousWinnerRootPcWeight =
           (winRoot >= 0) ? nextGateCtx.pcWeight[static_cast<size_t>(winRoot)] : 0.0;
       temporalCtx.previousDistinctPcs = nextGateCtx.distinctPcs;
       temporalCtx.previousWinnerScore = nextGateCtx.rawCandidates.empty()
           ? 0.0 : nextGateCtx.rawCandidates[0].score;
       temporalCtx.previousWinnerMargin = (nextGateCtx.rawCandidates.size() >= 2)
           ? nextGateCtx.rawCandidates[0].score - nextGateCtx.rawCandidates[1].score
           : -1.0;
   }
   
   // IMPORTANT: remove the next-region fields from temporalCtx that the loop
   // already set (they are correct since lines 419-443 ran for the current
   // iteration before we got to the else branch — leave them as-is unless
   // the re-analysis of the successor changes them, which it should not).

If nextTones is empty (end-of-loop call): only steps 1–4 are needed.
```

### Note on `recentRootsBuf` mutation

`advanceTemporalContext` modifies `recentRootsBuf` in place. When calling it twice
(once for the corrected merged region, once for the current slice), the buffer will
accumulate BOTH roots. This is correct — both roots entered the stream in sequence.
No special handling is needed.

---

## Scope of change

One function body modified: `runPass1` lambda in `regionanalyzer.cpp`.
One new static helper function added (in the same file, before `runPass1`).
No other files.

---

## Testing

### Build

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

### Both test suites

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/pdr_comp.txt 2>&1; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe  > /tmp/pdr_nota.txt 2>&1; echo "exit:$?"
head -15 /tmp/pdr_comp.txt
head -15 /tmp/pdr_nota.txt
```

Both must pass (416/416, 52/52 or current baselines from STATUS.md). If any test
fails, stop and report — do not proceed.

### Snapshot tests

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/pdr_snap.txt 2>&1; echo "exit:$?"
head -40 /tmp/pdr_snap.txt
```

For each drifting snapshot:
1. Show before/after chord identity at the changed tick(s)
2. Compare to DCML ground truth via `batch_analyze --preset Baroque` on that score
3. Classify: **improvement** (matches DCML), **neutral** (equally valid or alternatives
   only), **regression** (diverges from DCML)

Stop if ANY regression. Do not update goldens for regressions.

If all drifts are improvements or neutral:
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens > /tmp/pdr_goldens.txt 2>&1; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/pdr_snap2.txt 2>&1; echo "exit:$?"
head -5 /tmp/pdr_snap2.txt
```

### Corpus BIR — mandatory for both presets

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py; echo "exit:$?"
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py; echo "exit:$?"
```

**Hard stops:**
- Baroque BIR=false must not increase above 13
- Jazz BIR=false must not increase above 7

If either increases: stop and report. Do not commit.

### Manual verification — two Δ=+7a targets

After corpus run, check both BIR=false targets:

```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv102.7.xml" \
  --preset Baroque --dump-regions batch > /tmp/pdr_bwv102.json 2>&1; echo "exit:$?"
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv261.xml" \
  --preset Baroque --dump-regions batch > /tmp/pdr_bwv261.json 2>&1; echo "exit:$?"
```

For each, find the region(s) in the previously-failing arpeggio measure and report:
- Root pc and quality before and after
- DCML ground truth
- Whether the fix worked or a residual issue remains

Expected:
- bwv102.7: merged region should now output AbMaj7 (rootPc = 8)
- bwv261: report the margin; a 0.025 margin on the raw scores may still be indecisive
  and need Phase E — just document what happens

---

## Commit

If all tests pass, BIR does not regress, and both Δ=+7a targets are checked:

```
git add src/composing/analysis/region/regionanalyzer.cpp
git add src/notation/tests/pipeline_snapshot_tests/snapshots/  # if goldens updated
git commit -m "feat: Phase D — re-analyze inline-merged arpeggio runs on combined tone set (regionanalyzer.cpp)"
```

---

## Report format

Write findings to `C:\s\MS\cc_phase_d_reanalysis_report.md`.

Include:

### Part A — Implementation notes
Describe any deviations from the design above. In particular:
- Where exactly `phaseDReanalyzeRun` was placed (line range)
- Which fields of `ChordTemporalContext` were treated as "predecessor" vs "per-region"
  (the list above may not be exhaustive — note any additions)
- Whether the end-of-loop case was triggered on any corpus score
- Any compilation issues and how they were resolved

### Part B — Test results
composing N/N, notation N/N, snapshots N/N.
For each snapshot drift: tick, before/after chord, DCML ground truth, classification.

### Part C — BIR results
Baroque BIR=true/false before → after. Jazz BIR=true/false before → after.
If BIR improved (more =true), list which scores flipped from BIR=false → BIR=true.
If BIR regressed, do NOT commit — stop here.

### Part D — Δ=+7a manual verification
bwv102.7: merged region identity before → after; did it flip to AbMaj7?
bwv261: merged region identity before → after; margin; needs Phase E?

### Part E — Structural surprises
Any unexpected findings about which regions were re-analyzed (e.g., how many
inline-merged runs exist across the corpus beyond the known Δ=+7a cases, and
whether any of those are affected).
