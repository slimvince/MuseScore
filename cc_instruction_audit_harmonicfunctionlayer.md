# CC Instruction — LAYER AUDIT #6 (primary): harmonicfunctionlayer.cpp (competition + function) — READ-ONLY

> Sixth per-layer audit (`docs/layer_audit_plan.md`) — the CHORD-AXIS obligation layer (the oracle audit #5
> proved ~91% of root errors land HERE, downstream). **CC = primary auditor**; Cowork's note
> `cowork_audit_harmonicfunctionlayer.md` + the map's C1 reconcile. **READ-ONLY — findings only, NO
> code/behavior/inference change.** **North star: best = CORRECT inference vs the DCML/music21 oracle.**
> **Your fresh measurement is authoritative on the NUMBERS.**

## §1 — Scope
`src/composing/analysis/function/harmonicfunctionlayer.cpp` (`applyHarmonicFunction` — the competition over
the `ScoringSnapshot` + the migrated progression bonuses + winner selection + function/degree). Read-only;
you MAY run the corpus + a read-only probe (reuse `compare_rn`/`dcml_parser`/`music21`). No production edit.

## §2 — The audit (per plan §3) + reconciliation targets (MEASURE vs the oracle)
1. **Responsibility.** Competition (per-bass-group → global winner, with/without-w_dim + quality guard) +
   temporal/progression re-scoring (resolution/inversion/rootContinuity/w_seq/w_dim/step) + function/degree.
   **Confirm/deny the MULTIPLE-responsibility flag (S3):** is this one layer or three (competition vs
   temporal-scoring vs function)? — a phase-2 decomposition call (STRUCTURAL, fix-first per the sequencing gate).
2. **Correctness — the rule-reachable functional residual (the chord-axis obligation), MEASURE:**
   - **The wrong-winner rate + the rule-reachable share.** Of the **91% functional** root errors (audit #5),
     how many are **rule-reachable** (a better competition rule would fix them) vs defensible-ambiguity/floor?
     Cowork `[prov ≈ 26–55% rule-reachable]` (functional-residual B1, strict→generous). Re-measure + report.
   - **Characterize the TOP wrong-winner patterns** — which competition rules are missing (share-tone
     viio↔V7, inversion-vs-root, applied-dominant, …)? This is the actionable chord-axis obligation list.
   - **Heuristic-accretion risk:** note the Iter-*-bonus / with-without-variant / guard complexity (a
     structural-quality concern), but the obligation is the missing rules, not a rewrite.
3. **Completeness:** heuristic coverage gaps (cases no bonus covers → the vertical winner stands wrong); the
   phase split (Segmentation vs Final).
4. **Gaps → obligations**, tagged STRUCTURAL ("wrong place" — the 3-responsibility split, fix-first) vs
   CORRECTNESS ("right place, wrong output" — the missing competition rules, the inference track). Per the
   sequencing gate, keep these two cleanly separated.

## §3 — Deliver
`cc_audit_harmonicfunctionlayer_report.md`: responsibility (+ the 1-vs-3 decomposition call), the MEASURED
rule-reachable share + the top wrong-winner patterns, completeness, tagged obligations (STRUCTURAL vs
CORRECTNESS), empirical method. State which `[prov]` you confirm vs correct. Read-only; Cowork verifies +
reconciles; user ratifies.

## §4 — Stop conditions
- Any production/inference/behavior change → STOP. A probe that moves production output → STOP.
- Cross-layer issue → phase-2 note. Uncertain → check vs oracle; bucket convention-boundary + surface; never
  guess.
