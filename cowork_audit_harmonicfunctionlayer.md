# Cowork independent audit — harmonicfunctionlayer (competition + function) — to reconcile with CC

> Second-opinion pass from the committed-object source (HEAD) + the functional-residual investigation.

## Responsibility
`applyHarmonicFunction` — the **competition + function layer**: take the oracle's `ScoringSnapshot`, re-score
each cell with progression signals (resolution / inversion / root-continuity / w_seq / w_dim / step bonuses),
run the per-bass-group → global competition (with/without-w_dim variants + quality guard), select the
**WINNER** (root+quality), assign the **function/degree**. **This is where 95% of root errors live** (the
functional residual). ⚠ Arguably **multiple responsibilities**: winner-competition + temporal/progression
scoring + function assignment — a phase-2 decomposition flag.

## Correctness (vs the true chord/function)
1. **[correctness · chord-axis · the MAIN chord obligation] Wrong-winner selection.** 95.2% of root errors are
   functional = the competition picks the wrong root/quality among the oracle's ambiguous candidates
   (share-tone, inversion-vs-root). The investigation graded these largely **rule-reachable (B1)** — a better
   competition rule could fix them (distinct from the key-axis walls; these are hand-buildable).
2. **[correctness · structure] Heuristic accretion.** The progression signals are the accreted Iter-86/91/95/97
   bonuses, with/without-w_dim variants, a post-bonus quality guard, a surgical step guard. Each fixes specific
   cases; the **interaction is hard to reason about** (boiling-frog complexity) — a phase-2 "is this the right
   structure" candidate.
3. **[correctness · inherits] Function/degree assignment** inherits the key (`diatonicDegreeForRootPc`) → wrong
   degree if the key is wrong (key-axis errors propagate) and the S1 tonicization-vs-modulation labeling gap
   lives here/downstream.

## Completeness
4. **[completeness · chord-axis] Heuristic coverage gaps** — cases no bonus covers fall back to the vertical
   winner (functionally wrong); the rule-reachable residual (B1 ~26–55%) is the uncovered-rule space.
5. **[completeness] Phase split** (Segmentation vs Final) suppresses some signals — correctness depends on the
   phase being set right.

## ★ Phase-2 — the chord-axis vs key-axis contrast (the audit's structural verdict so far)
- **Chord axis:** oracle SOLID (~95%); obligations are at THIS competition layer and are **rule-reachable /
  hand-buildable** (better competition rules), plus the inherent symmetric-dim7/aug floor (reserved learned
  slice). The complexity risk is the heuristic accretion (structure), not a precision wall.
- **Key axis:** the obligation is a genuine precision WALL (cadence I→IV/I→V) + the relative-pair limit + the
  joint synthesis → calibration / learned, NOT hand-buildable rules.
- **So the two axes need different remedies:** chord-axis = competition-rule completion (+ the reserved slice);
  key-axis = upstream cadence precision + the constrained-joint soft combination + calibration.
- Decomposition flags: this layer's three jobs (competition / temporal scoring / function); the gate layer
  (next) is the post-scoring compensation it feeds (the deferred dissolution target).

## Reconciliation targets (for CC)
- Confirm the rule-reachable share of the functional residual at HEAD + characterize the top wrong-winner
  patterns (which competition rules are missing).
- Confirm/deny the multiple-responsibility decomposition (competition vs temporal-scoring vs function).
