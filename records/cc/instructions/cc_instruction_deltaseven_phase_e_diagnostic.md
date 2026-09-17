# CC Instruction: Δ=+7b Phase E diagnostic

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), `C:\s\MS\build_and_test.md`,
`C:\s\MS\docs\scoring_model.md` (§4, §11), and `C:\s\MS\docs\redesign_plan.md`
before starting.

**Read-and-diagnose only. No code changes. No commits.**

---

## Background

The three Δ=+7b cases (bwv245.28, bwv296, bwv320) share a mechanism: the oracle
produces a near-tie (~1.92 vs ~1.92) between two candidates in the failing region,
and `rootContinuityBonus` (+0.40) breaks the tie toward the predecessor's root — which
happens to be wrong for the current region.

The predecessor is CORRECT and confident (pcWeight 0.60–0.82). So scaling by
predecessor confidence cannot help (predecessor is not the problem).

Phase E needs a signal that says "despite the near-tie, this is a chord change, not
a continuation." Before designing anything, we need the full scoring picture for these
three regions: what the two near-tie candidates are, whether existing context signals
(`wSeqBonus`, `previousQuality`, `consecutiveBassStepwiseCount`, `nextRootPc`) already
favour the correct candidate, and whether the mozart_k280-1 control behaves differently
on those same signals.

---

## Step 1 — Identify failing region details from mismatch report

Read `src/composing/tests/chord_mismatch_report.txt`.

For each of bwv245.28, bwv296, bwv320, find the failing region entry and record:
- Tick range (startTick, endTick)
- Our winning rootPc and quality
- DCML expected rootPc and quality
- The BIR=false label

Also look up the mozart_k280-1 control region(s) where `rootContinuityBonus` fires
correctly (measures 9 and/or 12, IV region). Record their tick ranges.

---

## Step 2 — Full scoring dump via temporary debug print

Add a temporary debug print in `harmonicfunctionlayer.cpp`, at the TOP of the Pass A
loop (just before the `rootContinuityBonus` call, approximately L206), that fires only
for the target regions.

The print should emit, for EVERY candidate in the failing region:

```cpp
// TEMPORARY DIAGNOSTIC — remove before reporting
if (/* tick-gate for target regions */) {
    const double rcb = rootContinuityBonus(cell.rootPc, ctx.previousRootPc,
                                           prefs.rootContinuityBonus);
    const double wseq = wSeqBonus(cell.rootPc, ctx.nextRootPc, snapshot.distinctPcs,
                                  snapshot.jointScoringEnabled, prefs.explorationMode);
    const double rawScore = (cell.basisIndep + cell.basisDep)
                             * cell.complexityFactor * cell.augFactor
                             + cell.wCompleteBonus;
    qDebug("[PEd] tick=%d bass=%d root=%d qual=%d "
           "raw=%.4f rcb=%.4f wseq=%.4f total=%.4f "
           "prevRoot=%d prevQual=%d nextRoot=%d "
           "stepwise=%d metricW=%.3f distinctPcs=%d",
           /* tick */, cell.bassPc, cell.rootPc, static_cast<int>(cell.quality),
           rawScore, rcb, wseq, rawScore + rcb + wseq,
           ctx.previousRootPc, static_cast<int>(ctx.previousQuality), ctx.nextRootPc,
           ctx.consecutiveBassStepwiseCount, ctx.regionMetricWeight,
           snapshot.distinctPcs);
}
```

Gate on the failing-region startTicks found in Step 1, plus the mozart control tick(s).

**Finding the tick variable:** `applyHarmonicFunction` does not directly receive a tick
parameter. The snapshot may not carry it either. If tick is unavailable inside
`harmonicfunctionlayer.cpp`, fall back to gating on `ctx.previousRootPc` matching the
predecessor's known rootPc AND `snapshot.distinctPcs` matching the known value for that
region. Use a compound condition:

```cpp
// Gate example if tick unavailable:
const bool isTarget =
    (ctx.previousRootPc == <pred_rootPc_bwv245> && snapshot.distinctPcs == <N>)
    || (ctx.previousRootPc == <pred_rootPc_bwv296> && snapshot.distinctPcs == <N>)
    // ... etc
```

Check whether `snapshot` or `gateCtx` carries a tick or region identifier before
falling back to this.

Build, run batch_analyze per score (redirect to file):

```
cd C:\s\MS
ninja_build_rel/batch_analyze.exe <bwv245.28_path> > /tmp/ped_245.txt 2>&1; echo "exit:$?"
grep "\[PEd\]" /tmp/ped_245.txt
# repeat for bwv296, bwv320, and mozart_k280_1
```

---

## Step 3 — Remove debug print and report

Remove the temporary print. Confirm working tree clean (regionanalyzer.cpp byte-identical
to HEAD, only the print removal in harmonicfunctionlayer.cpp — already reverted).

Write findings to `C:\s\MS\cc_deltaseven_phase_e_diagnostic_report.md`.

---

## What to report

**Table 1 — Full candidate scores for each failing region**

For each of the three Δ=+7b regions, list ALL candidates that appear in the dump:

| Score | Tick | BassPc | RootPc | Quality | Raw | rcb | wSeq | Total |
|---|---|---|---|---|---|---|---|---|

Mark which candidate is:
- Our current winner (highest Total after all bonuses in this print)
- The DCML-expected chord
- The predecessor-continuation candidate (rootPc == ctx.previousRootPc)

**Table 2 — Context values at each failing region**

| Score | previousRootPc | previousQuality | nextRootPc | consecutiveBassStepwiseCount | regionMetricWeight | distinctPcs |
|---|---|---|---|---|---|---|

**Table 3 — Mozart control (for comparison)**

Same tables for the mozart_k280-1 IV region(s) where `rootContinuityBonus` fires
correctly.

**Assessment — answer these questions:**

1. Is the near-tie BEFORE rootContinuityBonus (raw ≈ raw) or does something else
   also contribute (e.g., wSeqBonus already favouring the wrong candidate)?

2. Does `wSeqBonus` fire for either candidate in the failing regions? If so, which?
   Does the DCML-correct candidate have a V→I relationship with `nextRootPc`?

3. What is `consecutiveBassStepwiseCount` at the failing regions vs. mozart?
   Could a gate on `consecutiveBassStepwiseCount > 0` → reduced `rootContinuityBonus`
   break the tie correctly without regressing mozart?

4. What is `previousQuality` at the failing regions? Does it suggest a specific
   resolution target (e.g., minor predecessor → dominant or tonic resolution)?

5. What is `nextRootPc` and is it consistent with the DCML-expected chord?
   (E.g., if DCML current = A and nextRootPc = D, that's a V→I relationship.)

6. Do the three failing regions share any pattern in the context signals that
   cleanly separates them from the mozart control?

7. Surface any structural surprise not anticipated above.
