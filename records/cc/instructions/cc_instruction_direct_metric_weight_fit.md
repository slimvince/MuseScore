# CC instruction — the direct-metric weight search (the ratified fallback; the weight stage, second attempt)

> **The ruling is IN (user, 2026-07-19): ★R = M2. This file is DISPATCHED.**
>
> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header + 2026-07-19
> entries), `C:\s\MS\BUILD_AND_TEST.md`, `cowork_prefit_gates.md` (the held-out and capacity
> protocols bind; the weight cap is ≤ 14 as amended), the §5a staged-fitting decision in
> `cowork_joint_estimator_architecture.md` (item (d) — the fallback this dispatch executes), the
> **OI-187 row** (the refuted likelihood-objective premise this responds to), and your weight-fit
> record (`aef4540c0d`).
>
> **Current state:** branch `master`, HEAD `aef4540c0d` (verify). One Cowork-authored uncommitted
> doc edit rides YOUR commit: `cowork_handoff.md`. **PYTHON-ONLY; instrument layer only; no
> `src/`, no build, no golden, no re-baseline. THE FIREWALL FOR THIS FIT EVENT, stated precisely:
> the DECLARED search objective (★R below, a training-fold error quantity) is lawfully consulted
> by the optimizer on TRAINING folds — that is the ratified fallback's defining property; each
> held-out fold is evaluated EXACTLY ONCE by the per-fold selected optimum (selected on the
> TRAINING objective, never on held-out); no other accuracy figure is consulted anywhere,
> grep-proven.** Pinned instruments import-only. No adoption proposed; results return for review.

**Dispatch author:** Cowork, 2026-07-19, at the user's direction — the user-ruled option 1 after
the likelihood fit's STOP: the ratified direct-metric fallback (the published minimum-error-rate
protocol: few weights, direct error minimization, random-restart stability, bootstrap intervals).

## ★R — the scalar the search minimizes (user ruling required)

The metric has axes; a search needs one number. Options presented to the user: **M1** = the
duration-weighted ROOT disagreement alone (the robust unit's governing respect; but root is
already in band — searching on it forfeits the key-axis purpose of the weight stage); **M2** = the
equal-weighted SUM of duration-weighted ROOT disagreement and KEY-vs-LOCAL disagreement (the two
primary axes: the governing respect plus the architecture's target; equal weighting is the
no-information choice; Roman numeral and key-home tracked beside); **M3** = KEY-vs-LOCAL alone
(maximal pressure on the target axis; risks trading root away — the hard-stop axis — for key).
**RULING: M2 (user, 2026-07-19)** — the equal-weighted sum of duration-weighted root disagreement
and key-vs-local disagreement, computed on training folds; Roman numeral and key-home tracked
beside, never inside the objective.

## Task 1 — the search (per the published protocol; per training-fold complement)

For each of the 5 training-fold complements: minimize the ★R objective over the 13-weight vector.
- **Bounds, declared:** each weight in [0, 5]. Non-negativity is theory-grounded — every factor is
  a log-probability of the generative form, so a negative weight would assert the counted table
  actively misleads; if the search PINS a weight at 0 (the metric rejecting a factor) or presses a
  bound, that is a reported finding, not a search freedom to widen.
- **No regularization penalty** (the published protocol at this scale uses none; the capacity
  protection is 13 weights against ~100,000 tokens, the held-out gate, and the bounds).
- **Starts:** 21 per fold — identity weights, the likelihood-fit weights (both named), and 19
  seeded-random starts (seeds recorded). **Selection:** the best TRAINING objective. **Stability
  report:** the spread of the converged optima's training objectives AND their held-out results
  per fold (the published protocol's substitute for a convexity proof) — a wide spread is a
  prominently-reported finding.
- Search method (coordinate line search or a simplex method): your choice, named and reported;
  deterministic given the recorded seeds; byte-reproducible.

## Task 2 — evaluation, against these written predictions (Cowork, #17b)

Held-out once per fold; pooled CV figures with piece-level bootstrap 95 % intervals; beside them:
the identity arm (CV 74.68 / 53.20 / 72.70 / 60.08), the likelihood-fit arm, and the committed
current-system baselines. **Predictions for the direct-search arm (CV, pooled):** key-local
**74–82** (must not sit below identity beyond the interval — the search starts AT identity);
key-home **57–68**; root **72–77** (the hard-stop axis must not degrade beyond the interval);
Roman numeral **59–66**. A band miss is a STOP-for-review (this is a fit event, not an
exploration). Also report: the selected weights per fold and pooled (with plain-language reading —
which evidence types the metric strengthened or discounted); whether the cadence features earned
non-zero weight (the OI-190 watch — the leading-tone feature's sign instability under the
likelihood objective); the three sensitive cases re-decoded (the bwv352 pair, the bwv10.7
merge-versus-split, the deceptive cadence); the modulation-rate check (key changes per piece vs
the ground truth's — the OI-187 mechanism must NOT reappear); the prune cost on the 12-piece
sample at the selected weights; timings.

## Commit

**One commit:** `tools: the direct-metric weight search (the ratified fallback) — CV headline + stability record` —
the search code, the artifacts (per fold + pooled + all-326 publishable variant reported beside,
provenance-stamped with the ★R ruling), this file (force-add), the riding Cowork doc edit. Push
**origin only**. Update the OI-187 row's status with the outcome in the same commit.

## Self-check before reporting (standing rule)

Diff scope proven; the firewall as stated grep-proven (the objective computation is confined to
training folds; the held-out evaluation path is called once per fold and writes only the report
artifacts); all figures generated; fold provenance on every number. **Report:** the headline
table (direct-search vs identity vs likelihood vs current); the stability record; the weight
reading; the prediction verdicts; the sensitive cases; the modulation-rate check; anomalies — a
surprise at a fit event is a STOP-for-review, never built around.
