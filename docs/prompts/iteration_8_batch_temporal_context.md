# Iteration 8: Wire temporal context into batch_analyze (§2.10 partial retirement)

## ⚠ Critical behaviour rules

- **Think, investigate, and REPORT before implementing.**
  Read the exact lines described, confirm they match, then implement.
- Make only the changes listed. Nothing else.
- Do not commit until all tests pass AND the corpus has been regenerated.
- If the build fails or any test regresses, STOP and report verbatim.

---

## Background

`analyzeScore()` in `batch_analyze.cpp` already declares and maintains the rolling
state variables needed for temporal context (`runningStepwiseCount`,
`recentRootsBuf`), already computes `bassIsStepwiseFromPrevious` and
`bassIsStepwiseToNext`, and already collects next-region tones for the look-ahead.
But the NOTE comment added in Iteration 2 (around line 1701) intentionally leaves
`consecutiveBassStepwiseCount`, `recentRootPcs`, and `nextRootPc` unset in `ctx`
before the `analyzeChord()` call.

This iteration wires those three fields in. After this change, every temporal gate
(B/C/D/G-B/G-C/G-D/E/F/H-B/H-C/H-D) fires in the batch path exactly as it does
in the bridge path, making all corpus measurements accurate.

`regionMetricWeight` is intentionally left at its default (1.0) — no gate uses it.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — current baselines (BIR=true=109, BIR=false=788)

---

## Step 2 — Read and confirm current state

Read `tools/batch_analyze.cpp` from the start of the `analyzeScore()` main loop
through the `analyzeChord()` call and the rolling-state update block. Confirm:

A. `runningStepwiseCount` and `recentRootsBuf` are declared before the loop
   and updated inside it — but `ctx.consecutiveBassStepwiseCount` and
   `ctx.recentRootPcs` are NEVER assigned from them.
B. The nextTones look-ahead block collects `nextBassPc` and sets
   `ctx.bassIsStepwiseToNext`, but does NOT compute `ctx.nextRootPc`.
C. `ctx.nextRootPc` stays at its default (-1) throughout the loop.
D. The NOTE comment (around line 1701) explicitly documents this as intentional.
E. `chordAnalyzer` is already in scope at the look-ahead block (it is used for
   the main `analyzeChord()` call immediately after).

Report the exact line numbers for each item before proceeding.

---

## Step 3 — Three targeted changes

### Change 1: assign `consecutiveBassStepwiseCount` and `recentRootPcs` to ctx

Immediately before the `auto candidates = chordAnalyzer->analyzeChord(...)` line,
add two assignments:

```cpp
        ctx.consecutiveBassStepwiseCount = runningStepwiseCount;
        ctx.recentRootPcs                = recentRootsBuf;
```

These two lines replace the "not populated" state described in the NOTE comment.

### Change 2: compute `ctx.nextRootPc` inside the existing look-ahead block

The look-ahead block already collects `nextTones` and extracts `nextBassPc`.
Extend it to also compute `ctx.nextRootPc` via a lightweight `analyzeChord`
call on `nextTones` with `nullptr` context — exactly as the bridge does:

Find the line `ctx.bassIsStepwiseToNext = ...` (currently just after the
look-ahead block closes). Before that line, still inside the
`if (boundaryIndex + 1 < boundaryTicks.size())` block, add:

```cpp
            // nextRootPc: lightweight analyzeChord on next region (no context — avoids recursion).
            if (!nextTones.empty()) {
                const auto nextCandidates = chordAnalyzer->analyzeChord(
                    nextTones, localKey.keySignatureFifths, localKey.mode,
                    nullptr, chordPrefs);
                ctx.nextRootPc = nextCandidates.empty()
                                 ? -1 : nextCandidates[0].identity.rootPc;
            } else {
                ctx.nextRootPc = -1;
            }
```

Also add `ctx.nextRootPc = -1;` immediately before the
`if (boundaryIndex + 1 < boundaryTicks.size())` block opens, so the field is
reset at the start of each iteration (in case the look-ahead block is skipped
for the last region).

### Change 3: update the NOTE comment

Remove the NOTE/TODO comment block that says the four fields "are no longer
populated here" (around lines 1701–1707). Replace it with a brief accurate comment:

```cpp
        // Temporal context is now fully populated before analyzeChord():
        //   bassIsStepwiseFromPrevious, bassIsStepwiseToNext — computed above
        //   consecutiveBassStepwiseCount, recentRootPcs — assigned below
        //   nextRootPc — computed in look-ahead block below
        //   regionMetricWeight — left at default 1.0 (no gate uses it)
        // §2.10: analyzeScore() and the bridge now use identical temporal signals.
```

After making all three changes, report the exact line ranges modified.

---

## Step 4 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

**Composing tests** (catalog-based, always have context): expect 407/407,
RealDiff ≤ 4. If any regression: STOP.

**Notation tests**: expect 53/53. If any regression: STOP.

**Pipeline snapshot tests**: the bridge path is unchanged — expect 11/11 pass,
no golden mismatches. If any failure: STOP and report.

---

## Step 5 — Regenerate corpus and record new baselines

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

(Use the regeneration command from `build_and_test.md`. If the command differs,
use whatever `build_and_test.md` specifies.)

Record the new BIR=true and BIR=false numbers. Expect:
- BIR=true: should improve from 109 (temporal gates now fire in batch)
- BIR=false: should stay flat or improve (gates are context-gated and were
  already verified safe in Iterations 3–7)

If BIR=false increases significantly (> 50): STOP and report before updating
any baselines. A large BIR=false increase would mean a temporal gate is firing
aggressively on correct root-position chords.

---

## Step 6 — Update baselines

Update `build_and_test.md`:
- Replace BIR=true baseline with the new number
- Replace BIR=false ceiling with the new number (if it changed)
- Update the attribution line to commit hash from this iteration
- Remove the note about "temporal gates not measurable in batch" — they now are

Update `STATUS.md` with a 2026-05-06 entry documenting:
- §2.10 partial retirement: batch temporal context now fully populated
- New BIR=true and BIR=false baselines
- Commit hash

---

## Step 7 — Push

```
cd C:\s\MS && git add -A && git commit -m "Iter 8: wire temporal context into batch (§2.10 partial retirement)" && git push
```

---

## Step 8 — Report

```
State verification (A–E):          all confirmed / differences: <list>
  runningStepwiseCount declared at: line N
  recentRootsBuf declared at:       line N
  ctx.consecutiveBassStepwiseCount never assigned: confirmed at line N
  ctx.recentRootPcs never assigned: confirmed at line N
  ctx.nextRootPc stays -1:         confirmed at line N
  chordAnalyzer in scope:          yes

Changes made:
  Change 1 (consecutiveBassStepwiseCount + recentRootPcs): lines N–N
  Change 2 (nextRootPc look-ahead): lines N–N
  Change 3 (comment update): lines N–N

Build:                             pass / fail
Composing tests:                   407/407 pass, RealDiff=N
Notation tests:                    53/53 pass
Pipeline snapshot tests:           11/11 pass

New corpus baselines:
  BIR=true:                        N (was 109, improvement: N)
  BIR=false:                       N (was 788)
  Change in BIR=false:             N (positive = regression; negative = improvement)

Breakdown of BIR=true improvement (if measurable):
  Enharmonic-pair errors:          before N / after N
  Non-enharmonic errors:           before N / after N

build_and_test.md updated:         yes
STATUS.md updated:                 yes
GitHub push:                       done / commit hash
Unexpected findings:               none / <describe>
```
