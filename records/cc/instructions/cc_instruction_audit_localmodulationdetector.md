# CC Instruction — LAYER AUDIT #2 (primary): localmodulationdetector.cpp (READ-ONLY)

> Second per-layer audit (`docs/layer_audit_plan.md`). **CC = primary auditor** (deep source + EMPIRICAL
> measurement); Cowork's independent note `cowork_audit_localmodulationdetector.md` reconciles against this.
> **READ-ONLY — findings only, NO code/behavior/inference change.** **North star: best = CORRECT inference —
> judge vs the DCML oracle, NOT a proxy gate.** Audit the layer IN ISOLATION (inputs assumed correct;
> interaction issues → phase-2). **Your fresh measurement is authoritative on the NUMBERS** — Cowork's
> figures below are `[prov]` (remembered from 4d-i), to be confirmed or corrected by your measurement (as the
> cadence-anchor "44%" became 27.6%).

## §1 — Scope
`src/composing/analysis/section/localmodulationdetector.{h,cpp}` (read). Read-only; you MAY build + run the
existing `--dump-modulation` diagnostic and/or a read-only probe (reuse `compare_rn`/`dcml_parser`; commit it
locally only if useful + production-byte-identical). No production edit.

## §2 — The audit (per plan §3) + Cowork's reconciliation targets
1. **Responsibility (contract).** State inputs/job/output. Confirm/deny it **consumes the shared cadence
   primitive** (`detectLocalModulations` calls both `detectAuthenticCadences` + `aggregateGlobalAnchor` over
   `CadenceRegionInput`, ~`:143-145`) → the decomposition flag.
2. **Correctness vs DCML (oracle) — MEASURE, don't recall.**
   - **Precision / recall of committed spans vs DCML modulations.** Cowork `[prov]`: **precision ~47% /
     recall ~33%** (4d-i). **Re-measure fresh** + report the real figures.
   - **★ The self-confirmation claim (load-bearing).** Cowork argues the CONFIRMATION gate (a cadence of the
     span's key resolving inside it) is **circularly satisfied by the SAME spurious cadence that seeded the
     span** (the I→IV "cadence to IV" both assigns the F regions AND confirms the F span) → the gate cannot
     filter the false positives. **Test it:** of the committed FALSE-positive spans (vs DCML), how many have
     an INDEPENDENT confirming cadence vs only the seeding one? If ~all FPs are self-confirmed, the claim
     holds; quantify.
   - **FP composition:** subdominant (V/V→V-anchored / I→IV) vs dominant vs foreign share, vs DCML.
   - **Inherited cadence wall:** confirm the FP roots trace to the cadence detector's I→IV / V/V→V over-reads
     (the corrected K1 mechanism — NOT "I→V", which is excluded).
3. **Completeness vs the case space.** Recall (above); authentic-cadence-confirmed-only (modulations signaled
   by half/plagal or by sustained scale-change without an authentic cadence → missed); relative-pair /
   partial-sig inheritance.
4. **Gaps → obligations**, tagged `[correctness]`/`[completeness]`, `[priority: key-axis]`, `[fix:
   structural / behavior-changing→deferred]`, genuine-error vs convention-floor.

## §3 — Deliver
`cc_audit_localmodulationdetector_report.md`: responsibility, the MEASURED precision/recall + FP composition
+ the self-confirmation quantification, completeness gaps, tagged obligations, and your empirical method
(corpus, oracle, probe). State explicitly which of Cowork's `[prov]` numbers you confirm vs correct. Read-only;
Cowork verifies the methodology at the committed object + reconciles; user ratifies.

## §4 — Stop conditions
- Any production/inference/behavior change → STOP. A probe that moves production output → STOP.
- Cross-layer issue → note for phase-2, don't chase. Uncertain → check vs the oracle; bucket
  convention-boundary + surface; never guess.
