# CC Instruction — LAYER AUDIT #1 (primary): cadencekeyanchor.cpp (READ-ONLY)

> **First per-layer audit** of the combined audit plan (`docs/layer_audit_plan.md`). **CC = primary auditor**
> (deep source + data-flow + EMPIRICAL probe); Cowork does the independent second-opinion in parallel.
> **READ-ONLY — findings only, NO code/behavior/inference change.** **North star: best = CORRECT inference**
> — judge correctness/completeness against the **DCML / music21 ground-truth oracle**, NOT a proxy gate (BIR/
> rn_agree). Audit this layer IN ISOLATION (inputs assumed correct, consumers ignored; interaction issues are
> phase-2 — note + move on).

---

## §1 — Scope
`src/composing/analysis/section/cadencekeyanchor.{h,cpp}` (read). Read-only. You MAY build + run the existing
diagnostics (`batch_analyze --dump-cadence-anchor` / `--dump-modulation`) and/or write a read-only probe to
measure this layer against the oracle — a probe is a diagnostic (commit it locally only if useful, and it
must be production-byte-identical; Cowork verifies at the committed object). **No production edit.**

## §2 — The audit (per plan §3)
1. **Responsibility (the contract).** State in one sentence: its inputs, its single job, its output. **Flag
   if it has >1 responsibility** (e.g. cadence *detection* vs global-key *aggregation* — is that one job or
   two? note for phase-2, don't resolve).
2. **Correctness vs the TRUE analysis (oracle, not the gate).** Trace the logic AND empirically measure: of
   the cadences it detects and the global key anchor it emits, how many are **correct vs DCML** (the true
   cadences / the DCML global key)? **Quantify the error rate** and characterize WHAT is wrong — e.g. the
   `detectAuthenticCadences` leading-tone test (`a.rootPc+4` = the dominant's major third, present in any
   major triad) firing on plain **I→IV / I→V** as spurious "cadences to IV/V" (the known blind spot — confirm
   + quantify it against the oracle). Distinguish genuine error from convention-boundary ambiguity.
3. **Completeness vs the case space (correctly).** Enumerate the cadence-type space (PAC / IAC / half /
   deceptive / plagal / phrygian-half / …) and the key-relationship space (major↔minor relative pair;
   modulation; partial/modal signatures). For each: does the layer detect/anchor it **correctly**, or
   mis-handle / omit it? Test coverage against the oracle. Pin every mis-handled or omitted case (this is
   where most obligations live — e.g. authentic-only detection missing half/deceptive; piece-global anchor
   not handling modulation; windowed-anchor instability).
4. **Gaps → obligations.** List each, tagged: `[correctness]`/`[completeness]`; `[priority: key-axis]`;
   `[fix: structural / behavior-changing→deferred]`; + whether it's genuine-error or convention-floor.

## §3 — Deliver
Write `cc_audit_cadencekeyanchor_report.md`: the responsibility statement, the correctness measurement (vs
oracle, quantified + characterized), the enumerated completeness coverage + gaps, and the tagged obligation
list. State your empirical method (corpus, oracle, probe) so Cowork can reconcile. If you committed a probe,
report its hash. **Read-only — no production change; Cowork independently audits the same layer at the
committed object and reconciles.**

## §4 — Stop conditions
- Any production / inference / behavior change (this is a read-only audit) → STOP.
- A probe that moves production output (`.ours.json` / BIR / snapshots) → STOP (it's not a clean diagnostic).
- An interaction/cross-layer issue → NOTE it for phase-2, do not chase it (audit this layer in isolation).
- Uncertain whether something is wrong → check against the oracle; if still unclear, bucket as
  convention-boundary and surface — never guess.
