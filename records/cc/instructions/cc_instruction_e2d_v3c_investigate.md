# CC Instruction: E2d v3c — Investigation (read-only, no code changes)

## Pre-reading

Read `C:\s\MS\STATUS.md` and `C:\s\MS\build_and_test.md` before starting.
Current HEAD: `0ab219d4c5` (Phase 1 / E2d-prereq). All tests pass.
This instruction is **read-only**. Do not modify any source file.

---

## Background

Phase 2 (E2d-enable v3b) revealed a fourth consistency gap:
`applyPostScoringGates` receives a `PostScoringGateContext` that was frozen inside
`analyzeChord` during the SUPPRESSED scoring pass. After `applyHarmonicFunction`
changes the winner (new bassPc, signal-inclusive scores), the gates still see stale
`rawCandidates`, `threshold`, and `bassPc`. At mozart_k280_1 tick 3840, the
inversion-bias correction (chordanalyzer.cpp ~L1912) should de-inflate the Dm
bass-root score and promote F6 (as HEAD does), but with suppression-frozen gateCtx
it doesn't.

v3c will fix this by rebuilding the relevant gateCtx fields from inside (or
immediately after) `applyHarmonicFunction`. Before writing v3c, I need exact
answers to the five questions below.

---

## Question 1 — Inversion-bias correction: exact gate mechanics at tick 3840

Trace the inversion-bias correction / Sub-9a block in `applyPostScoringGates`
(starting at ~L1912 in `chordanalyzer.cpp`) for mozart_k280_1 tick 3840.

Report:
- The exact entry condition(s): what must be true for the correction to fire?
- Which `PostScoringGateContext` fields it reads and what their values are in
  the current HEAD binary for this tick (use batch_analyze or add a temporary
  log if needed).
- The precise comparison / computation that determines whether to promote F6
  over Dm (what score, what threshold, what ratio, what bass bonus is involved).
- Why Phase 2's suppressed gateCtx causes the comparison to fail.

---

## Question 2 — Complete gateCtx field audit for all gates

Read the full body of `applyPostScoringGates` (all gates). For each gate, list
which `PostScoringGateContext` fields it reads (a table is fine):

| Gate | Fields read from gateCtx |
|------|--------------------------|
| Gate J / inversion-bias | … |
| Gate A | … |
| Sub-9a | … |
| … | … |

The goal is to identify the **minimum set of gateCtx fields** that must be rebuilt
to signal-inclusive values for all gates to produce byte-identical output.

---

## Question 3 — Non-winning-bass rawCandidates usage

Does any gate read `gateCtx.rawCandidates` looking for entries whose
`rootPc != winnerBassPc` (i.e., candidates from a different bass than the winner)?

If yes: identify the gate and what it does with those entries.
If no: confirm that rebuilding only the winning-bass's rawCandidates is sufficient.

---

## Question 4 — Rebuilding rawCandidates from the snapshot

After `applyHarmonicFunction` finishes its Phase 2 algorithm (final scores computed,
winning bass known), it has available:
- `winningCells` (the selected variant of the snapshot — all basses)
- `finalScores` map (cell pointer → post-step, signal-inclusive score)
- `winnerCell` with `bassPc`, `rootPc`, `tiePriority`, `appliedBassBonus`
- `threshold` = `(winnerScore - winnerCell->appliedBassBonus) * kScoreThresholdRatio`

`RawCandidate` has fields: `score`, `appliedBassBonus`, `rootPc`, `quality`,
`tiePriority`, `wDimDelta`. All of these are available from `ScoringCell` +
`finalScores`.

**Question:** Can the function layer reconstruct a `std::vector<RawCandidate>`
for the winning bass from these inputs alone? Specifically:
- Is every field of `RawCandidate` directly available (or trivially derivable)
  from a `ScoringCell` + `finalScores`?
- Is there any field of `RawCandidate` that is NOT in `ScoringCell` and would
  require data not available to the function layer?
- Is the `RawCandidate::wDimDelta` field the same as `ScoringCell::wDimDelta`?
  (Check both struct definitions.)

If there are gaps, identify them precisely.

---

## Question 5 — pcWeight and tpcForPc in gates

Does any gate in `applyPostScoringGates` read `gateCtx.pcWeight` or `gateCtx.tpcForPc`
in a way that is bass-dependent — i.e., would the gate produce a different result if
the winning bass changed (same pcWeight/tpcForPc values, different bassPc)?

These fields represent the sounding chord's pitch-class weights and TPC resolution;
they are computed from the input tones and do not change when the function layer
changes the bass. Confirming they are bass-independent would mean we do NOT need to
rebuild them — only `rawCandidates`, `threshold`, `bassPc`, and `bassTpc` need updating.

---

## Output

Write findings to `C:\s\MS\cc_e2d_v3c_investigation_report.md`.

Structure:
```
# E2d v3c Investigation Report

## Q1 — Inversion-bias correction mechanics
…

## Q2 — gateCtx field audit
…

## Q3 — Non-winning-bass rawCandidates usage
…

## Q4 — rawCandidates rebuild feasibility
…

## Q5 — pcWeight / tpcForPc bass-dependence
…

## Summary: minimum rebuild required for v3c
List the minimum set of gateCtx fields that applyHarmonicFunction (or a new
post-function-layer step) must update to signal-inclusive values.
```

No code changes. No commits. Report only.
