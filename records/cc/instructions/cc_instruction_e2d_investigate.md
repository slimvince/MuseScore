# CC Instruction — E2d Investigation (read-only)

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 and §10.

**Current HEAD:** `20f992a5e7` (E2c-infra). Working tree clean.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**This is a READ-ONLY investigation. Make zero code changes. Report findings only.**

---

## Context

E2c Commit 2 failed because the function layer's rescore (signals re-applied,
no step bonus) diverges from the scorer's output in cases where Pass B
(step bonus) or cross-bass competition changes the winner. E2d must address
both blockers before the signal migration can be enabled.

Two specific blockers were identified from the E2c failure:

**Blocker 1 — Pass B not replicated.**  
The function layer adds `rootContinuityBonus`, `wSeqBonus`, `wDimBonus` to
pre-step-bonus scores, but does not add the step bonus (`wStepIn + wStepOut`).
When the step bonus is large (0.20–0.35) and flips the winner, the function
layer picks the wrong candidate.

**Blocker 2 — Cross-bass: winner not in `result.candidates`.**  
In suppression mode, `rawCandidates` contains only one bass's cells (the
suppressed-signal winning bass). When the true with-signals winner is on a
different bass, it is absent from `result.candidates` entirely and cannot
be promoted.

---

## Question 1 — `applyStepBonusGuard()` implementation

Read the full `applyStepBonusGuard()` function in `chordanalyzer.cpp`.

Report:
- Its exact signature and line number.
- What it does — specifically whether it reads `previousBassPc` and
  `nextBassPc` from a context object, from a lambda, or from some other
  source.
- The exact formula for `wStepIn` and `wStepOut` — what makes a bass step
  qualify, and what the bonus magnitudes are.
- The m7-family guard: what template quality or interval pattern triggers it,
  and how it gates the bonus.
- Whether `applyStepBonusGuard()` is a free function or takes lambda
  parameters. If it takes lambdas or function parameters, list them.
- Whether all the inputs it needs are available at the regionanalyzer.cpp
  call sites (i.e., could the function layer reconstruct them if it had the
  right context fields).

---

## Question 2 — `ChordTemporalContext` and bass tracking

Read the `ChordTemporalContext` struct definition in `chordanalyzer.h`.

Report:
- Full field list with types.
- Whether `previousBassPc` or `nextBassPc` (or equivalent) are present.
- Where `ChordTemporalContext` is advanced / updated in `regionanalyzer.cpp`
  (the `advanceTemporalContext()` call or equivalent). Does it update bass PCs?
- If `previousBassPc` is NOT in `ChordTemporalContext`, identify the nearest
  in-scope variable in `regionanalyzer.cpp` that holds the previous region's
  bass PC at the time `analyzeChord()` is called.

---

## Question 3 — Per-bass `std::move` and what is discarded

Read the joint-scoring outer loop (the `bi` loop over `bassCandidates`) in
`analyzeChord()`. Focus on the winner-selection step at the end of each `bi`
iteration.

Report:
- The exact lines of the `if (localBestWith > globalBestScoreWith)` block.
- Whether `perBassWith` is `std::move`d into `bestPerBassWith`, discarding
  non-winning basses' cells.
- How many per-bass arrays are live simultaneously during the loop (1 or all).
- Specifically: after the loop completes, how many `RawCandidate` cells
  survive into `rawCandidates` (one bass's full set, or all basses')?
- What the cost would be of keeping ALL basses' cells — i.e. what data
  structure change is needed and what is the memory / build-result-call
  overhead for the typical case (|bassCandidates| = 1–4, N_templates = 17).

---

## Question 4 — Can `buildResult` be called from outside `analyzeChord()`?

Read the `buildResult` lambda definition in `analyzeChord()`.

Report:
- What variables from the outer `analyzeChord()` scope it captures (list each
  one with type and purpose).
- Whether it could feasibly be extracted to a free function — i.e. could all
  its captures be passed as explicit parameters without being impractical?
- If not extractable, is there a smaller subset of its work that the function
  layer actually needs to redo (e.g., just correct `bassPc` and `bassTpc`
  on an existing `ChordAnalysisResult`)?

---

## Question 5 — Alternative: post-Pass-B score capture

Consider adding a second capture point in the snapshot: after `applyStepBonusGuard()`
runs on `perBassWith` and `perBassWithout`, capture the final `score` of each
`RawCandidate` as a `postStepScore` on the matching `ScoringCell`.

Report:
- Whether this is feasible given the current data structures — specifically,
  does each `RawCandidate` in `perBassWith/perBassWithout` correspond exactly
  to a `ScoringCell` by index (i.e., is cell `[bi * 12*N + rootPc*N + tplIdx]`
  the same as `perBassWith[rootPc*N + tplIdx]` for bass `bi`)?
- If correspondence is exact by index, the function layer could compute:
    `stepBonus = cell.postStepScore - cell.preStepScore`
  where `cell.preStepScore` is reconstructible from the current fields as:
    `(basisIndep + basisDep) * cf * af + wCompleteBonus`
  (since wSeq=0 and wDim=0 in suppression mode). Confirm this arithmetic
  is correct.
- Whether `postStepScore` for the NON-winning bass cells is captured (those
  are currently `std::move`d away) — i.e. does capturing `postStepScore`
  also require solving the cross-bass problem, or can it be done for the
  single surviving bass first?

---

## Question 6 — Context available at regionanalyzer.cpp call sites for Pass B

For the three call sites (Pass 1 ~L445, Pass 2 ~L647, Pass 2b ~L833), report
what information is available to reconstruct the step-bonus inputs:

- The previous region's bass PC (needed for `wStepInBonus`) — is it tracked
  in `temporalCtx`, in the region struct, or computed from `chosenResult` of
  the previous call?
- The next region's bass PC (needed for `wStepOutBonus`) — is a look-ahead
  possible at each call site, or is it not available until after this region
  is analyzed?
- Whether the `hasStructuralBass` flag (used inside `bassDependentContextualBonuses`
  which feeds `basisDep`) is per-region or per-call, and whether it is
  available outside `analyzeChord()`.

---

## Proposed implementation plan

Based on questions 1–6, answer: which of these three approaches is most
viable for E2d?

**Approach A — Replicate Pass B in function layer.**  
Extend `HarmonicFunctionContext` with `previousBassPc` / `nextBassPc`. Extract
or replicate `applyStepBonusGuard()` in `harmonicfunctionlayer.cpp`. The
function layer runs: rescore (signals applied) → Pass B → quality guard →
threshold → winner. For cross-bass: use the snapshot (which already covers all
basses' pre-step cells from D1) to run per-bass Pass B and find the true winner
across all basses. If the winner is on a different bass, fix the result.

**Approach B — Capture post-Pass-B score per cell.**  
Add `postStepScore` (a double) to `ScoringCell`. Populate it in a new D1.5
capture pass immediately after `applyStepBonusGuard()` runs on each bass's
`perBassWith/perBassWithout`. The function layer then computes:
  `trueScore = postStepScore + rcb*cf*af + wSeqBonus_new + wDimDelta_new`
where `postStepScore` already bakes in the (suppressed-signal) step bonus.
For cross-bass: same problem — non-winning basses' `postStepScore` values
are `std::move`d away and unavailable. Still need to solve cross-bass.

**Approach C — Capture all basses, run full rescore in function layer.**  
In suppression mode, keep all basses' `perBassWith`/`perBassWithout` arrays
(don't discard via `std::move`). Store them all in the snapshot or pass them
separately. The function layer iterates all basses, rescores with signals +
Pass B, runs the quality guard globally, and picks the true winner. Calls
`buildResult` for the winner if it is on a different bass than `rawCandidates`.

For each approach, state: estimated scope of change, whether it resolves
BOTH blockers cleanly, and any remaining risks.

---

## Report format

Answer each question with exact line numbers where relevant. For the proposed
plan, be concrete about which approach you recommend and flag any unresolved
risks. The E2d implementation instruction will be written from this report.

**Make zero code changes.**
