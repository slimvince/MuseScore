# Iteration 9C: Extract `advanceTemporalContext()` to composing module (§2.10 one-implementation)

## ⚠ Critical behaviour rules

- **Read first, report exact lines, then implement.**
- Pure refactoring — zero behaviour change. Tests and corpus numbers must be identical.
- Do not commit until everything matches post-9B baselines exactly.
- If anything deviates, STOP and report verbatim.

---

## Background

After Iteration 9A (`isDiatonicStep`) and 9B (`inferNextRootPc`), the temporal context
computation still has one remaining duplication: the end-of-loop "advance" logic that
updates rolling state and previous fields after each region is analyzed.

Both `tools/batch_analyze.cpp` (`analyzeScore()`) and
`src/notation/internal/notationharmonicrhythmbridge.cpp` (`analyzeHarmonicRhythm()`)
contain identical inline logic:

```
1. Increment or reset runningStepwiseCount based on bassIsStepwiseFromPrevious
2. Shift recentRootsBuf left and insert the chosen result's rootPc at [0]
3. Assign ctx.consecutiveBassStepwiseCount = runningStepwiseCount
4. Assign ctx.recentRootPcs = recentRootsBuf
5. Assign ctx.previousRootPc / previousBassPc / previousQuality from chosen result
```

This iteration extracts that logic into a single `advanceTemporalContext()` free function
in `src/composing/analysis/chord/chordanalyzer.h`, alongside `isDiatonicStep` and
`inferNextRootPc`. Both loops call it instead of containing the inline logic.

After this change, any future modification to how rolling state or previous fields are
updated requires a change in exactly one place.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=109, BIR=false=788

---

## Step 2 — Read and confirm current state

Read the end-of-loop sections in both files. Confirm and report exact line numbers for:

**In `tools/batch_analyze.cpp`:**
A. The block that updates `runningStepwiseCount` (increment or reset based on `ctx.bassIsStepwiseFromPrevious`)
B. The block that shifts `recentRootsBuf` and inserts new rootPc
C. The block that assigns `ctx.consecutiveBassStepwiseCount` and `ctx.recentRootPcs`
D. The block that assigns `ctx.previousRootPc`, `ctx.previousBassPc`, `ctx.previousQuality`
E. What variable holds the chosen/final result for this region (e.g. `candidates[0]`)

**In `src/notation/internal/notationharmonicrhythmbridge.cpp`:**
F. The corresponding blocks (A–D equivalent) in the bridge loop
G. What variable holds the chosen/final result (e.g. `chosenResult`, `results[0]`)
H. Is the ordering of these updates identical to the batch path (same sequence of steps)?

**In `src/composing/analysis/chord/chordanalyzer.h`:**
I. What is the name and structure of the type that holds `rootPc`, `bassPc`, and
   `quality` for a single chord result's identity? (e.g. `ChordIdentity`)
   Confirm it is already visible from code in both batch_analyze.cpp and
   notationharmonicrhythmbridge.cpp (via existing includes).

Report all of the above before proceeding.

---

## Step 3 — Add `advanceTemporalContext()` to chordanalyzer.h

In `src/composing/analysis/chord/chordanalyzer.h`, immediately after `inferNextRootPc`
(added in Iteration 9B), add:

```cpp
/// Advances the temporal context and rolling state after a region has been analyzed.
/// Call once per region, after analyzeChord() has been called and the final result
/// chosen. Updates: rolling stepwise count, recent-roots window, and previous-chord
/// fields. After returning, ctx is ready for the next region's analyzeChord() call
/// (except for bassIsStepwiseFromPrevious / bassIsStepwiseToNext / nextRootPc which
/// depend on the next region's tones and must be set separately).
inline void advanceTemporalContext(
    ChordTemporalContext& ctx,
    int& runningStepwiseCount,
    std::array<int, 3>& recentRootsBuf,
    int chosenRootPc,
    int chosenBassPc,
    ChordQuality chosenQuality) noexcept
{
    // Rolling stepwise count.
    if (ctx.bassIsStepwiseFromPrevious) {
        ++runningStepwiseCount;
    } else {
        runningStepwiseCount = 0;
    }

    // Recent-roots window (most-recent first).
    recentRootsBuf[2] = recentRootsBuf[1];
    recentRootsBuf[1] = recentRootsBuf[0];
    recentRootsBuf[0] = chosenRootPc;

    // Pre-populate rolling fields for the next call to analyzeChord.
    ctx.consecutiveBassStepwiseCount = runningStepwiseCount;
    ctx.recentRootPcs                = recentRootsBuf;

    // Advance previous-chord fields.
    ctx.previousRootPc  = chosenRootPc;
    ctx.previousBassPc  = chosenBassPc;
    ctx.previousQuality = chosenQuality;
}
```

If the codebase uses a `ChordIdentity` (or equivalent named struct) that bundles
`rootPc`, `bassPc`, and `quality` — and this type is already visible in both consumer
files — add an overload that takes it instead:

```cpp
inline void advanceTemporalContext(
    ChordTemporalContext& ctx,
    int& runningStepwiseCount,
    std::array<int, 3>& recentRootsBuf,
    const ChordIdentity& chosen) noexcept
{
    advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf,
                           chosen.rootPc, chosen.bassPc, chosen.quality);
}
```

Report the exact insertion line(s).

---

## Step 4 — Replace inline logic in batch_analyze.cpp

In `tools/batch_analyze.cpp`, in the `analyzeScore()` loop, replace the entire
inline advance block (items A–D from Step 2) with a single call:

```cpp
advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf,
                       <chosen>.identity.rootPc,
                       <chosen>.identity.bassPc,
                       <chosen>.identity.quality);
```

Or, using the identity overload if added:

```cpp
advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf,
                       <chosen>.identity);
```

(Replace `<chosen>` with the actual variable name identified in Step 2E.)

Verify the replaced block covered EXACTLY items A–D — no more, no less.
Report the exact lines removed and the single replacement line added.

---

## Step 5 — Replace inline logic in notationharmonicrhythmbridge.cpp

In `src/notation/internal/notationharmonicrhythmbridge.cpp`, in `analyzeHarmonicRhythm()`,
replace the entire inline advance block (items F–H from Step 2) with the same call
pattern as Step 4, using the variable identified in Step 2G.

Report the exact lines removed and the single replacement line added.

---

## Step 6 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected (must match exactly — pure refactoring):
- Composing tests: 407/407, RealDiff ≤ 4
- Notation tests: 53/53
- Pipeline snapshot tests: 11/11, no golden mismatches
- BIR=true: 109
- BIR=false: 788

Any deviation = STOP and report verbatim.

---

## Step 7 — Push

```
cd C:\s\MS && git add -A && git commit -m "Iter 9C: extract advanceTemporalContext to composing module (§2.10 one-implementation)" && git push
```

---

## Step 8 — Report

```
State (A–I confirmed):
  batch advance block:       lines N–N (N lines)
  bridge advance block:      lines N–N (N lines)
  Blocks identical in logic: yes / differences: <list>
  ChordIdentity type:        <name> / not found (used individual fields)

Changes:
  advanceTemporalContext added to chordanalyzer.h: lines N–N
  Identity overload added:   yes / no
  batch_analyze.cpp:         lines N–N removed → line N (single call)
  notationharmonicrhythmbridge.cpp: lines N–N removed → line N (single call)

Build:                    pass / fail
Composing tests:          407/407, RealDiff=N
Notation tests:           53/53
Pipeline snapshot tests:  11/11, no mismatches
BIR=true:                 109
BIR=false:                788
GitHub push:              done / commit hash
Unexpected findings:      none / <describe>
```
