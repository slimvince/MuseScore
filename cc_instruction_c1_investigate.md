# CC Instruction — C1 investigation: Schumann tick 480 (viio7/V = C#°7)

**Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`

**Current state:** Branch `master`, HEAD `945a9e2f18`, **working tree clean.**
BIR baselines (lenient-OR): Baroque BIR=true=28, BIR=false=16; Jazz BIR=true=36,
BIR=false=10. Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).
Mismatch report: Jazz 3 RealDiff / 127 ConventionDiff; Standard 0 / 1.

---

## Background

C1 is a known deferred residual: the Schumann Kinderszenen score has a 240-tick C#°7
region at tick 480 (viio7/V — leading-tone dim7 resolving to the dominant) that is
absorbed by `absorbShortRegions` (the Phase-4 unconditional absorb swallowed it). Even
in the per-tick P4 analysis path, which does analyze down to individual ticks, the
rotation is wrong: `wDim` outputs G°7 instead of C#°7 because `nextRootPc` is not
plumbed into the P4 tickLocal path.

Two independent fixes are needed:
- **(a) Absorption exception:** prevent short leading-tone dim regions from being absorbed
  into their predecessor. Must be targeted — the Phase-4 unconditional-absorb policy
  exists because the old same-root-only policy tripled region count (10665 → 18502).
- **(b) nextRootPc in P4:** the P4 per-tick analysis path uses `wDim` to select the
  correct dim7 rotation, but only if it has `nextRootPc` in context. Verify whether it
  does, and if not, how to plumb it.

**This instruction is investigation only — no code changes.** Read the relevant code,
run batch dumps to understand the current behaviour, and produce a planning report.
Do not make any edits.

---

## Part A — Reproduce the current failure

Run the Schumann score through the batch analyzer to see the current region output:

```
cd C:\s\MS && ./ninja_build_rel/batch_analyze.exe \
  --input "src/notation/tests/data/Schumann_Kinderszenen_No._1_Of_Foreign_Lands_and_People.mscz" \
  --preset Baroque \
  --dump-regions notation \
  > /tmp/schumann_regions.txt 2>&1; echo "exit:$?"
head -80 /tmp/schumann_regions.txt; echo "exit:$?"
```

Find the region containing tick 480 and report:
- What region covers tick 480?
- What chord does the analyzer emit for that region?
- What region immediately follows it (tick/root/quality)?
- What is the output for the pipeline snapshot (the schumann_kinderszenen_n01 golden)?

Then look at the pipeline snapshot golden file to see what the expected output is:
```
grep -n "tick.*480\|\"480\"" \
  C:\s\MS\src\composing\tests\data\pipeline_snapshots\schumann_kinderszenen_n01*.json \
  2>/dev/null | head -20; echo "exit:$?"
```

(Adjust the path/glob to find the correct golden file if the above doesn't match.)

---

## Part B — Understand the absorption path for this region

Find `absorbShortRegions` in `regionanalyzer.cpp`. Read the function logic:

1. What is `kMinRegionTicks`? (The threshold below which a region is considered short.)
2. What conditions trigger absorption? (Is it purely tick-count-based, or are there
   quality/root checks?)
3. What does the absorbing region become? (Does the short region's tones merge, or is it
   discarded entirely?)

Then confirm: does the C#°7 region at tick 480 (length 240 ticks) meet the absorption
condition? Is its predecessor the region that absorbs it?

Report the precise absorption path for this specific case.

---

## Part C — Investigate the P4 tickLocal path for nextRootPc

Find the P4 per-tick analysis path in the codebase. P4 is the tick-level analysis pass
that produces per-tick chord labels from region-level results. It uses `wDim` to select
the correct dim7 rotation.

Answer these questions:

1. **Where is `nextRootPc` computed for the P4 path?** Does it come from the next
   region's root PC, from a lookahead computation, or is it not computed at all?
2. **Is `nextRootPc` populated in the `ChordTemporalContext` struct that P4 passes to
   `analyzeChord`?** Or is it left at its default (-1 = unknown)?
3. **Is `wDim` currently gated on `nextRootPc >= 0`?** If `nextRootPc == -1`, does `wDim`
   fire at all? (If not, the rotation ambiguity means P4 picks an arbitrary rotation.)

Check the P4 call sites in `regionanalyzer.cpp` and `notationharmonicrhythmbridge.cpp`
to see how the context is constructed before each `analyzeChord` call.

---

## Part D — Design proposals (based on A/B/C findings)

Once you have the facts from Parts A–C, propose concrete designs for each sub-task.
Do NOT implement — just describe the plan precisely enough that the implementation
instruction can be written from it.

### D1 — Absorption exception design

The targeted guard should preserve a short dim/half-dim region ONLY when both conditions
hold:
- The region is Diminished or HalfDiminished quality
- The next region's root PC is one semitone above the short region's root PC
  (`(nextRoot - shortRoot + 12) % 12 == 1`) — the leading-tone resolution pattern

Describe where in `absorbShortRegions` this exception should be inserted, and what
information (next region's rootPc) is available at that point. If `nextRegion.rootPc`
is not available in the absorb loop, describe how to thread it in.

Also: does the same exception need to apply in `notationharmonicrhythmbridge.cpp` or
only in `regionanalyzer.cpp`?

### D2 — nextRootPc plumbing design

If nextRootPc is not populated in the P4 context (confirmed in Part C):
- Describe the minimal change to populate it. Is the next region already available
  when P4 constructs the context?
- What is the concrete call site in `regionanalyzer.cpp` where the change belongs?

If nextRootPc IS already populated: confirm this and note that D2 may be a no-op
(the rotation issue is a different cause).

---

## Report back

1. Current batch output for tick 480 in the Schumann score (region, chord, length)
2. Precise absorption path: does the 240-tick region meet `kMinRegionTicks`? What absorbs it?
3. P4 nextRootPc status: populated or not? If not, does wDim fire or silently skip?
4. D1 absorption exception design (where + how)
5. D2 nextRootPc plumbing design (if needed)
6. Your assessment: are D1 and D2 independent fixes that can be applied in separate
   commits, or does D1 need to land before D2 has any observable effect?
