# CC Instruction — LAYER AUDIT #3 (primary): jointkeydecision.cpp (READ-ONLY)

> Third per-layer audit (`docs/layer_audit_plan.md`). **CC = primary auditor** (empirical measurement);
> Cowork's independent note `cowork_audit_jointkeydecision.md` reconciles. **READ-ONLY — findings only, NO
> code/behavior/inference change.** **North star: best = CORRECT inference vs the DCML oracle, not a proxy
> gate.** **Your fresh measurement is authoritative on the NUMBERS** — Cowork's figures are `[prov]`
> (Cowork-verified during J-key-i/ii/iii but not re-measured this session), to be confirmed or corrected.
> The producer is the J-key-i strong-signature-backbone (the dormant commit restored it); audit THAT state.

## §1 — Scope
`src/composing/analysis/section/jointkeydecision.{h,cpp}` (read). Read-only; you MAY run the committed
`--dump-joint-key` diagnostic + `cc_j_key_i_measure.py` (the established instruments) to re-measure. No
production edit; the dormant flag stays OFF (byte-identical).

## §2 — The audit (per plan §3) + Cowork's reconciliation targets (MEASURE, don't recall)
1. **Responsibility (contract).** The constrained-joint key decision (dormant): combine soft evidence
   (scorer candidates + cadence anchor + modulation spans + bass + declared hint) over a global key-path
   Viterbi (+ scoped joint), home-pair-pinned. Confirm it is the SYNTHESIS layer (consumes the other
   key-axis layers).
2. **Correctness / decision quality vs DCML — re-measure:**
   - **The soft re-rank WIN.** `[prov ≈ +3.80/+3.50/+12.24 pp; S2 −140/−96/−1706]` vs production. Re-measure
     on the committed instruments; report the real figures.
   - **The home-fifths HARD pin unsafe rate.** `[prov ≈ 17% / 56 stems]` (partial-sig structurally
     unrepresentable). Re-measure.
   - **★ The scoped JOINT is INERT (the load-bearing architecture claim).** `[prov ≈ +0.04/−0.14/−0.06 pp]`
     (joint − soft). **Re-measure the joint−soft increment.** If it is ~0, the WIN is the SOFT broad-evidence
     integration, NOT the joint search → confirms the META-PRINCIPLE (precision lives in evidence breadth +
     calibration, not search). This determines whether the constrained-joint *combination* is the key-axis
     lever — the single most decision-relevant number for the eventual fix.
3. **Completeness:** the home-pair lattice excludes non-signature keys (partial-sig); inherits the cadence/
   modulation imprecision (K1) + the scorer's relative-pair limit (K2).
4. **Gaps → obligations**, tagged. Confirm the convergence: K1 (cadence precision) feeds it; K2 (relative-
   pair) is what the soft combination must overcome; the home-pin demotion was measured not-separably-safe.

## §3 — Deliver
`cc_audit_jointkeydecision_report.md`: responsibility, the MEASURED win / unsafe-rate / joint−soft
increment, completeness, tagged obligations, empirical method. State which `[prov]` numbers you confirm vs
correct. Read-only; Cowork verifies methodology at the committed object + reconciles; user ratifies.

## §4 — Stop conditions
- Any production/inference/behavior change → STOP. A probe/regen that moves production output → STOP.
- Cross-layer issue → note for phase-2. Uncertain → check vs the oracle; bucket convention-boundary +
  surface; never guess.
