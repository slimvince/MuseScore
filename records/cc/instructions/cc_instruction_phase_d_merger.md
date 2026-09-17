# CC Instruction: Phase D — arpeggio micro-region merger

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header),
`C:\s\MS\build_and_test.md`, and `C:\s\MS\docs\redesign_plan.md`
Step 4 (Phase D section, including the dead-end and window-boundary-decision
subsections). Do not skip these; the design context is essential.

---

## What this is

A new pass in `regionanalyzer.cpp` that aggregates consecutive short-duration,
sparse-tone greedy-expand regions into a single analysis window before their
chord identities cascade into the temporal context.

This is Phase D of the redesign. It fixes the Δ=+7a failure class (bwv102.7
AbMaj7, bwv261 F#7) by ensuring arpeggiated harmonies are heard as a unit by
the oracle. It is NOT a BIR-improvement exercise. Some BIR improvement may
follow as a side effect; the success criterion is the architecture.

**Constraint: change only `regionanalyzer.cpp` and its private helpers.** Do not
touch `chordanalyzer.cpp`, `harmonicfunctionlayer.cpp`, `regiontonecollector.cpp`,
gate thresholds, templates, or scoring terms.

---

## Background

The greedy-expand (Pass 1 boundary detection in `regionanalyzer.cpp`) creates a
new region boundary every time the set of simultaneously sounding notes changes.
An arpeggiated chord — say AbMaj7 cycling through C→Eb→G→Ab — produces one
240-tick region per arpeggio step. In each step the tone set is partial: the DCML
root hasn't attacked yet. The oracle correctly identifies a chord from the
incomplete evidence (Eb major, say), commits that identity, and
`rootContinuityBonus` carries the wrong root forward into the slice where the DCML
root finally sounds and would otherwise win cleanly.

The investigation (`cc_phase_d_investigation_report.md`) confirmed:
- The DCML root is in a FUTURE arpeggio position — it cannot be reached by any
  backward-walk fix
- The 240-tick micro-regions come from the initial greedy-expand (Pass 1 boundary
  detection), not from `detectBassMovementSubBoundaries` (Pass 2b, which has
  `minGapTicks = 960` specifically to avoid these)
- Merging the full arpeggio span's tones produces the correct chord for bwv102.7:
  `{Eb:720, G:720, Ab:480, C:480, D:240, Bb:240}` → oracle picks AbMaj7
- bwv261 has a 0.025 raw-score margin even with full aggregation and will need
  Phase E for a decisive fix; aggregation is still a prerequisite

---

## Architecture of the insertion point

Pass 1 (lines ~390–531, `runPass1` lambda) creates `HarmonicRegion` objects with:
- `chordResult` — oracle output including `applyIter8691Pedal` + `applyPostScoringGates`
- `tones` — the raw tone vector from `collectRegionTones`, stored in the region
- `temporalExtensions` — snapshot of the temporal context at commit time

After Pass 1, the `regions` vector holds these fully-analyzed regions. Pass 2 then
merges adjacent regions that share the same root and quality (the inline
same-chord-consecutive merge at lines ~510–514 already uses `mergeChordAnalysisTones`).

**The Phase D pass inserts between Pass 1 and Pass 2.** At that point:
- Every `HarmonicRegion` has a populated `tones` vector — no extra
  `collectRegionTones` call is needed
- `mergeChordAnalysisTones` already exists and is already used in the same file
- The merged region needs one fresh oracle call on the aggregated tone set

---

## Part A — Corpus spot-check (read-only, no build)

Before writing any code, run a quick spot-check to verify the merger trigger
conditions don't have unexpected false positives in the corpus.

Using the existing batch-analysis output in `tools/corpus/*.ours.json`, or by
running `--dump-regions batch` on a sample of 10–15 scores, answer:

1. How many short-run candidates (runs of N≥2 adjacent regions each shorter than
   480 ticks) exist in the 13 BIR=false scores? List them with tick ranges.
2. For the non-Δ=+7a candidates: are their tone sets sparse (distinctPcs ≤ 2)
   or richer? The distinctPcs guard should exclude genuine brief chords with 3+
   distinct pitch classes.
3. For the two known Δ=+7a scores: confirm the arpeggio micro-regions appear as
   expected (N≥2 consecutive, each < 480 ticks, each with distinctPcs ≤ 2).

To compute distinctPcs for a region from the dump output: count distinct
`rootPc` values present across the `collected_notes` of each region (use
`--diagnose-measures` for detail) or approximate from the JSON chord output.

Report the spot-check findings before proceeding to Part B. If any non-arpeggio
score has runs of N≥2 consecutive short regions with distinctPcs ≤ 2, flag it —
the distinctPcs threshold may need lowering to 1 for that corpus.

---

## Part B — Implementation

If the spot-check confirms no unexpected false positives, implement the merger
pass. If unexpected cases exist, stop and report.

### New function: `mergeArpeggioMicroRegions`

Add a new static function to `regionanalyzer.cpp` immediately before the main
`analyzeRegion` function body. Signature:

```cpp
// Phase D — merge runs of consecutive sparse short regions into a single
// analysis window before chord identities enter the temporal-context stream.
// A run is: N >= kPhaseD_MinRunLength adjacent regions each with duration
// < kPhaseD_MinHarmonicTicks AND distinctPcs <= kPhaseD_MaxSparsePcs.
// The merged region is re-analyzed on the aggregated tone set so the oracle
// sees the full arpeggio harmony.
static void mergeArpeggioMicroRegions(
    std::vector<HarmonicRegion>& regions,
    const Score* score,
    const ChordAnalyzerPreferences& prefs,
    const std::shared_ptr<IChordAnalyzer>& chordAnalyzer,
    const std::set<std::size_t>& excludeStaves);
```

Constants (add as `static constexpr` in the file, near the other kPass2b/kMin
constants):
```cpp
static constexpr int    kPhaseD_MinHarmonicTicks = 480;  // 1 quarter note
static constexpr int    kPhaseD_MaxSparsePcs      = 2;   // ≤ 2 distinct PCs = arpeggio slice
static constexpr size_t kPhaseD_MinRunLength      = 2;   // require ≥ 2 consecutive short regions
```

### Algorithm

```
i = 0
while i < regions.size():
    dur = regions[i].endTick - regions[i].startTick
    dpcs = distinctPcCount(regions[i].tones)  // count distinct pitch % 12
    if dur >= kPhaseD_MinHarmonicTicks OR dpcs > kPhaseD_MaxSparsePcs:
        i++; continue
    // Start of a candidate run
    j = i + 1
    while j < regions.size():
        dur_j = regions[j].endTick - regions[j].startTick
        dpcs_j = distinctPcCount(regions[j].tones)
        adjacent = (regions[j].startTick == regions[j-1].endTick)
        if NOT adjacent OR dur_j >= kPhaseD_MinHarmonicTicks OR dpcs_j > kPhaseD_MaxSparsePcs:
            break
        j++
    run_length = j - i
    if run_length < kPhaseD_MinRunLength:
        i++; continue
    // Merge regions[i..j-1] into one
    merge_and_reanalyze(regions, i, j, ...)
    // After merge, regions[i] is the new combined region; regions[i+1..j-1] removed
    // Do NOT advance i — the merged region might itself be short and part of a longer run
    // (conservative: advance i to skip the merged region)
    i++
```

### Merge and re-analyse

For the run `regions[i..j-1]`:

1. **Aggregate tone set:** start with `regions[i].tones`, then call
   `mergeChordAnalysisTones(combined_tones, regions[k].tones)` for k = i+1..j-1.
   This function already exists in the file and handles duration-weighted tone merging.

2. **Temporal context:** use `regions[i].temporalExtensions` for predecessor
   context (the merged span's predecessor is the region BEFORE the run, not an
   arpeggio step). Reconstruct a `ChordTemporalContext` from `temporalExtensions`:
   - `previousRootPc = regions[i].temporalExtensions.previousRootPc`
   - `previousQuality = regions[i].temporalExtensions.previousQuality`
   - `previousBassPc = regions[i].temporalExtensions.previousBassPc`
   - For `nextRootPc`: cold-analyze `regions[j].tones` (the successor) using
     `inferNextRootPc(chordAnalyzer.get(), regions[j].tones, ...)` if j is in
     range; otherwise leave at -1. Look at how Pass 1's lookahead works (lines
     ~421-432) for the exact pattern.
   - Set `regionMetricWeight` from the score's beat type at
     `regions[i].startTick` (same pattern as Pass 2b).

3. **Re-analyze:** call the same pipeline used everywhere:
   ```cpp
   PostScoringGateContext gateCtx;
   auto results = chordAnalyzer->analyzeChord(
       combined_tones, keyFifths, keyMode, &mergedCtx, prefs, &gateCtx);
   applyIter8691Pedal(results, gateCtx, &mergedCtx, prefs);
   applyPostScoringGates(results, prefs, &mergedCtx, gateCtx);
   ```
   For `keyFifths` and `keyMode`: use `regions[i].keyModeResult`.

4. **Create merged region:** replace `regions[i]` with the new region spanning
   `[regions[i].startTick, regions[j-1].endTick]`. Set `tones = combined_tones`,
   `chordResult = results.front()`, `alternatives = rest of results`,
   `keyModeResult = regions[i].keyModeResult`, `hasAnalyzedChord = true`.
   Erase `regions[i+1..j-1]`.

### Call site

In the main `analyzeRegion` body (or equivalent orchestration function), call
`mergeArpeggioMicroRegions` immediately after Pass 1 returns and before the
existing same-root-quality collapse merge (Pass 2). Look for the comment
`// ── Pass 2 ──` or similar and insert just before it:

```cpp
if (!regions.empty()) {
    mergeArpeggioMicroRegions(regions, score, prefs, chordAnalyzer, excludeStaves);
}
```

---

## Testing

### Run both test suites and snapshots

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/pd_comp.txt 2>&1; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/pd_nota.txt 2>&1; echo "exit:$?"
head -10 /tmp/pd_comp.txt
head -10 /tmp/pd_nota.txt
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/pd_snap.txt 2>&1; echo "exit:$?"
head -30 /tmp/pd_snap.txt
```

### Snapshot drifts

For each drifting snapshot:
1. Show the before/after chord identity at the changed tick(s)
2. Look up DCML ground truth via `batch_analyze --preset Baroque` on the score
3. Classify: **improvement** (matches DCML), **neutral** (alternatives only or
   equally valid), **regression** (diverges from DCML)

Stop if any regression. Do not update goldens for regressions.

If all drifts are improvements or neutral, update goldens:
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens > /tmp/pd_goldens.txt 2>&1; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/pd_snap2.txt 2>&1; echo "exit:$?"
head -5 /tmp/pd_snap2.txt
```

### Corpus run and BIR check

After all tests pass:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py; echo "exit:$?"
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/characterise_bir_false.py; echo "exit:$?"
```

Hard stops:
- Baroque BIR=false must not increase above 13
- Jazz BIR=false must not increase above 7

If either increases, stop and report — do not commit.

### Manual verification for the two Δ=+7a targets

```
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv102.7.xml" \
  --preset Baroque --diagnose-measures N > /tmp/pd_bwv102.json 2>&1; echo "exit:$?"
/c/s/MS/ninja_build_rel/batch_analyze.exe "C:/s/MS/tools/corpus/bwv261.xml" \
  --preset Baroque --diagnose-measures N > /tmp/pd_bwv261.json 2>&1; echo "exit:$?"
```

(Use the measure numbers identified in the spot-check.) Confirm:
- bwv102.7: the merged region now outputs AbMaj7 (root Ab = pc 8)
- bwv261: report what the merged region outputs and its margin; a decisive fix
  may require Phase E

---

## Commit

If all tests pass, BIR does not regress, and manual verification confirms the
merger fires correctly:

```
git add src/composing/analysis/region/regionanalyzer.cpp
git add src/notation/tests/pipeline_snapshot_tests/snapshots/  # if goldens updated
git commit -m "feat: Phase D — merge arpeggio micro-regions before chord analysis (regionanalyzer.cpp)"
```

---

## Report format

Write findings to `C:\s\MS\cc_phase_d_merger_report.md`.

Include:

### Part A — Spot-check results
For each run candidate found in the BIR=false scores: tick range, N, duration
per region, distinctPcs per region. For the Δ=+7a targets: confirm they appear
as expected. For any unexpected candidates: flag them and state whether the
distinctPcs guard excluded them.

### Part B — Architecture confirmation
Confirm the insertion point (line number range where the call was inserted).
Note any deviation from the algorithm above and why.

### Part C — Test results
composing N/N, notation N/N, snapshots N/N.
For each snapshot drift: tick, before/after, DCML ground truth, classification.

### Part D — BIR results
Baroque BIR=true/false before and after. Jazz BIR=true/false before and after.
Any regressions (if none, state explicitly).

### Part E — Δ=+7a manual verification
bwv102.7: chord identity of merged region, before/after.
bwv261: chord identity of merged region, margin, whether it needs Phase E.

### Part F — Structural surprises
Any deviations from the design, judgment calls, edge cases encountered.
