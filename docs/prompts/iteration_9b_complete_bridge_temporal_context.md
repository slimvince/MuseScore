# Iteration 9B: Complete bridge temporal context + shared inferNextRootPc (§2.10 full retirement)

## ⚠ Critical behaviour rules

- **Read the exact lines described, confirm they match, then implement.**
- Make only the changes listed. Nothing else.
- Pipeline snapshot goldens may change — examine every changed score before updating.
- Do not commit until all tests pass and every golden change is verified correct.
- If the build fails or any test regresses, STOP and report verbatim.

---

## Background

After Iteration 9A, `isDiatonicStep()` lives in the composing module. After Iteration 8,
the batch path populates all 5 temporal context fields before every `analyzeChord()` call.

The bridge path (`analyzeHarmonicRhythm()` in `notationharmonicrhythmbridge.cpp`) has
most of the infrastructure already present in its region loop:

- The forward look-ahead block (collecting `nextTones`, computing `nextBassPc`,
  assigning `bassIsStepwiseToNext`) already exists.
- The assignments `temporalCtx.consecutiveBassStepwiseCount = runningStepwiseCount`
  and `temporalCtx.recentRootPcs = recentRootsBuf` already exist.
- `regionMetricWeight` is already computed and assigned.

What is MISSING:

1. The rolling state (`runningStepwiseCount`, `recentRootsBuf`) is **never updated**
   after each region — so both fields are always their initial values (0 and {-1,-1,-1}).
2. `nextRootPc` is **not extracted** from the look-ahead's `nextCandidates` result
   and not assigned to `temporalCtx`.
3. The lightweight `analyzeChord` call for `nextRootPc` is duplicated between batch
   and bridge — it should be a shared free function.

After this iteration:
- Bridge and batch produce identical `ChordTemporalContext` for every region.
- §2.10 technical debt is fully retired.
- `inferNextRootPc()` is the canonical shared helper for the look-ahead pattern.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=109, BIR=false=788

---

## Step 2 — Read and confirm current state

Read `src/notation/internal/notationharmonicrhythmbridge.cpp`, specifically the
`analyzeHarmonicRhythm()` function. Confirm and report the **exact line numbers** for:

A. Declaration of `runningStepwiseCount` and `recentRootsBuf` (initial values).
B. The forward look-ahead block — the `if (i + 1 < boundaryTicks.size())` block that
   collects `nextTones` and computes `nextBassPc`. Does it call `analyzeChord` on
   `nextTones`? If yes: does it extract `nextRootPc` and assign it to `temporalCtx`?
C. The lines that assign `temporalCtx.consecutiveBassStepwiseCount = runningStepwiseCount`
   and `temporalCtx.recentRootPcs = recentRootsBuf`.
D. The "advance previous" block after `analyzeChord()` — the lines that set
   `temporalCtx.previousRootPc`, `temporalCtx.previousQuality`,
   `temporalCtx.previousBassPc` for the next iteration.
E. Whether `runningStepwiseCount` and `recentRootsBuf` are updated anywhere after the
   analyzeChord call (expected: NOT found — this is the missing piece).
F. Whether there is a SECOND region-loop path in this file (an onset/subbound path
   around line 735 or later) that also processes regions and would need the same fixes.

Also read `tools/batch_analyze.cpp` look-ahead and rolling-state update blocks
(approximately lines 1716–1769) to confirm the exact update logic to mirror.

Report all line numbers (A–F) and the exact code of the "advance previous" block
before proceeding.

---

## Step 3 — Extract `inferNextRootPc` shared helper

In `src/composing/analysis/chord/chordanalyzer.h`, in the same namespace as
`isDiatonicStep()` (added in Iteration 9A), add immediately after `isDiatonicStep`:

```cpp
/// Lightweight root-PC inference for a neighbouring region.
/// Calls analyzeChord with nullptr context (no temporal signals) to avoid recursion.
/// Returns -1 if tones is empty or analyzeChord returns no candidates.
inline int inferNextRootPc(
    const IChordAnalyzer* analyzer,
    const std::vector<ChordAnalysisTone>& tones,
    int keySignatureFifths,
    KeySigMode keyMode,
    const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences)
{
    if (tones.empty()) return -1;
    const auto candidates = analyzer->analyzeChord(
        tones, keySignatureFifths, keyMode, nullptr, prefs);
    return candidates.empty() ? -1 : candidates[0].identity.rootPc;
}
```

Report the exact insertion line.

---

## Step 4 — Update batch_analyze.cpp to use the shared helper

In `tools/batch_analyze.cpp`, within the look-ahead block identified in Step 2,
replace the inline `analyzeChord` call that computes `nextRootPc` with a call to
`inferNextRootPc`. The logic should become:

```cpp
ctx.nextRootPc = inferNextRootPc(
    chordAnalyzer.get(), nextTones,
    localKey.keySignatureFifths, localKey.mode, chordPrefs);
```

(Adjust argument names to match actual variable names in the batch path.)

Remove the now-redundant inline `analyzeChord` call and the `nextCandidates` variable.

Report the exact lines changed.

---

## Step 5 — Three targeted changes to the bridge loop

All three changes are inside `analyzeHarmonicRhythm()` in
`src/notation/internal/notationharmonicrhythmbridge.cpp`.

### Change 1: Add `nextRootPc` to the bridge look-ahead block

In the forward look-ahead block (identified in Step 2B), after `nextTones` has been
collected and `nextBassPc` extracted:

If the block already calls `analyzeChord` on `nextTones` (producing `nextCandidates`
or similar): replace that call with `inferNextRootPc` and assign the result to
`temporalCtx.nextRootPc`.

If the block does NOT call `analyzeChord` on `nextTones`: add, after the
`nextBassPc` extraction, still inside the look-ahead `if` block:

```cpp
temporalCtx.nextRootPc = inferNextRootPc(
    chordAnalyzer.get(), nextTones, localKeyFifths, localKeyMode, prefs);
```

Add `temporalCtx.nextRootPc = -1;` immediately BEFORE the look-ahead `if` block
opens (to reset it at the start of each iteration, so the last region gets -1).

(Adjust variable names to match actual names in the bridge loop.)

### Change 2: Add rolling state updates after each region

Immediately after the "advance previous" block (identified in Step 2D — the lines
that update `temporalCtx.previousRootPc`, `previousQuality`, `previousBassPc`),
add the rolling state update that mirrors `batch_analyze.cpp`:

```cpp
// Update rolling state for the next region.
if (temporalCtx.bassIsStepwiseFromPrevious) {
    ++runningStepwiseCount;
} else {
    runningStepwiseCount = 0;
}
recentRootsBuf[2] = recentRootsBuf[1];
recentRootsBuf[1] = recentRootsBuf[0];
recentRootsBuf[0] = chosenResult.identity.rootPc;  // adjust to actual variable name
```

(Use the actual variable name for the chosen/final result's rootPc — this is whatever
the bridge uses after gate processing to represent the final chord for this region.)

### Change 3: If a second region-loop path exists (Step 2F)

If the file has a second region-processing loop (e.g. the onset/subbound path),
apply the same Changes 1 and 2 to that loop as well.

Report the exact line ranges of all changes made.

---

## Step 6 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

**Composing tests**: expect 407/407, RealDiff ≤ 4. Any regression: STOP.

**Notation tests**: expect 53/53. Any regression: STOP.

**Pipeline snapshot tests**: the bridge temporal context is now more complete, so
some golden files may change. Do NOT run `--update-goldens` yet.

If pipeline snapshot tests report mismatches:
1. Examine EVERY changed score individually.
2. For each change: identify the measure, the before/after chord symbols, and
   which temporal gate appears to have fired (based on the analysis context).
3. Verify each change is musicologically correct for the passage.
4. Report all changes before updating goldens.

If pipeline snapshot tests pass with no mismatches: report that too.

---

## Step 7 — Update pipeline snapshot goldens (if needed)

Only after verifying all golden changes are correct:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Confirm all tests pass after update.

---

## Step 8 — Corpus run

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected:
- BIR=true: ≤ 109 (may improve as temporal gates now fire on bridge path)
- BIR=false: ≤ 788

If BIR=false increases significantly (> 50): STOP and report before committing.
The bridge changes affect `analyzeChord` calls from the bridge path, not the batch
path, so the corpus numbers (which use batch) should be unchanged. If BIR=false
increases, investigate whether the bridge changes accidentally affected the batch path.

---

## Step 9 — Update baselines and push

Update `build_and_test.md`:
- Update BIR baselines if either changed.
- Remove the §2.10 technical debt note if still present.
- Update the attribution line to the commit hash from this iteration.

Update `STATUS.md` with a 2026-05-06 entry:
- §2.10 fully retired: bridge temporal context now complete
- `inferNextRootPc` extracted as shared helper
- Rolling state (`recentRootPcs`, `consecutiveBassStepwiseCount`) now maintained in bridge loop
- New BIR baselines
- Commit hash

```
cd C:\s\MS && git add -A && git commit -m "Iter 9B: complete bridge temporal context, extract inferNextRootPc (§2.10 full retirement)" && git push
```

---

## Step 10 — Report

```
State verification (A–F confirmed):
  runningStepwiseCount declared at:     line N
  recentRootsBuf declared at:           line N
  Look-ahead block:                     lines N–N
    analyzeChord on nextTones present:  yes / no
    nextRootPc assigned to ctx:         yes / no (was missing)
  consecutiveBassStepwiseCount assign:  line N
  recentRootPcs assign:                 line N
  Rolling state update (end of loop):   NOT found (confirmed missing)
  "Advance previous" block:             lines N–N
  Second loop path:                     yes (lines N–N) / no

Changes made:
  inferNextRootPc added to chordanalyzer.h: line N
  batch_analyze.cpp look-ahead updated:     lines N–N
  Bridge Change 1 (nextRootPc):             lines N–N
  Bridge Change 2 (rolling state update):   lines N–N
  Bridge Change 3 (second path, if any):    lines N–N / not applicable

Build:                    pass / fail
Composing tests:          407/407, RealDiff=N
Notation tests:           53/53
Pipeline snapshot tests (before update):  N/N pass / N mismatches
  Changed scores:         <list, or "none">
  Changes verified:       yes / n/a
Pipeline snapshot tests (after update):  N/N pass

Corpus:
  BIR=true:               N (was 109)
  BIR=false:              N (was 788)

build_and_test.md updated: yes
STATUS.md updated:         yes
GitHub push:               done / commit hash
Unexpected findings:       none / <describe>
```
