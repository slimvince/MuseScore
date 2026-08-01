# The Certification-Audit Protocol — Minimizing Known-Suspect Bias

> **Cowork, 2026-07-10 (session 36), user-directed:** the protocol every EG-7 layer audit
> (L1→L2→L3→L4→L5+instruments, OI-84) must follow. Rationale: the session-36 sweeps were
> SEARCH-driven — the auditor's priors chose the queries, so the priors chose the coverage
> (proof: PC-1's unadmitted premise was invisible to every sweep and surfaced only when a
> measurement contradicted it). Bias is not removed by effort; it is removed by making the
> audit a TOTAL FUNCTION over a MACHINE-GENERATED domain, then establishing the audit itself
> as an instrument (#19). One protocol, reused by every layer audit (#6).

## P1 — Enumerate-then-classify; never search

The audit scope is generated MECHANICALLY from the code, not chosen by anyone: the complete
list of (a) functions, (b) numeric literals, (c) struct fields on cross-layer surfaces,
(d) cross-layer calls, (e) branches, for the layer under audit — produced by script (the
#17(f) generated-artifact rule applied to audit SCOPE: no hand-chosen inventory). The
auditor's output is a **disposition for EVERY row** — findings are not "reported", rows are
exhausted. An item cannot be silently skipped because every item demands a verdict.

## P2 — A closed verdict set with no silent escape

Every row gets a verdict from a fixed rubric — premises: FACT / THEORY / ASSUMPTION;
derived facts: PUBLISHED / SILOED / TRAPPED / DUPLICATED; code: RETIRES(R1–R9) / SURVIVES;
constants: ESTABLISHED / UNFIT / DEAD — and **"no issue" is itself a recorded claim with a
stated reason**, auditable later. The rubric's questions are the same for every row (what
does it assume? what does it publish? who consumes it? what happens at its edge cases?), so
the auditor does not get to choose the questions per item — choosing questions is where
priors leak in.

## P3 — Audit the negative space (spec→code, not only code→intuition)

Reading code and asking "does this look fine?" finds only what priors recognize. The second
direction is mandatory: from the layer's CONTRACT (architecture docs, the layer's declared
outputs), enumerate what the layer SHOULD handle and publish, then check each expectation
against the code. Absences (an unpublished fact, an unhandled case, a consumer that should
exist and doesn't) are findable only in this direction — the siloed-facts class was exactly
this.

## P4 — Behavioral characterization, not just reading (the PC-1 lesson)

For every mechanism/branch in the inventory: measure its FIRE RATE on the pinned corpus with
a cheap read-only counter (the O-10 liveness idea generalized to every branch of the audited
layer). A mechanism that never fires, always fires, or fires wildly off its designed
population is surfaced MECHANICALLY, no suspicion required — this is the only method in the
set that would have caught PC-1 before EG-2 did. Reading answers "what does it claim?";
counting answers "what does it do?"; the audit requires both columns per row.

## P5 — A blinded second pass, adversarial by construction

The primary auditor receives the inventory + rubric and NO list of suspects (the instruction
must not name prior findings for the layer). A SECOND, independent pass (fresh session or
agent, no access to the first pass's dispositions) audits a stratified sample of the same
rows; its dispositions are then diffed against the first pass. Its explicit mission is to
find what the first pass missed — it is rewarded by disagreement, not agreement.

**A WITHHELD FINDING NEVER ENTERS A MANDATORY SESSION-START READ (user-ratified 2026-07-28).**
When a pass is run blind — a finding deliberately kept from the auditor so that whether they
rediscover it measures the audit's power — that finding must not appear in any document the
auditor is *required* to open, and must not be delivered inline in the dispatch body. `STATUS.md`
carries a POINTER; the withheld content lives in a separate artifact opened only after the freeze
commit. Before a blind pass is dispatched, every required read and the dispatch body are
cross-checked against every withholding requirement. *Why:* measured failure — on the OI-199
pass-1 blinding, the mandatory `STATUS.md` read carried the full text of all three sealed findings
with line citations, and the dispatch delivered them inline as well; the reconciliation could then
no longer report blind recall, only that the artifacts point at each mechanism on their merits.
The same shape had already occurred once (the OI-89 instance), which is why the remedy is stated
as a standing rule rather than a per-dispatch precaution. Tracked at `OPEN_ITEMS.md` OI-222.

## P6 — Establish the audit itself (#19): a measured residual-error rate

Randomly sample N rows (random, not "interesting" — neutral processing order throughout, so
attention fatigue lands on random rows rather than systematically on the unglamorous tail);
deep-verify their dispositions at objects (#15). The disagreement rate is the audit's
measured error estimate — **the audit's completeness is then a NUMBER, not a claim.** An
audit with an unmeasured error rate is an unestablished instrument and does not certify a
layer (EG-7 gate not satisfied). Disagreements found in P5/P6 are #13 STOPs for the audit:
diagnosed (which protocol step let the miss through?) before certification.

## P7 — The defect-type catalog (the value of known problems, kept)

Removing queries (P1) also removes the diagnostic value of every pathology already paid for —
a generic rubric can under-recognize an INSTANCE that a targeted signature catches instantly.
So known problem TYPES live in **`DEFECT_TYPES.md`** — the living catalog, one entry per type
with its detection signature, **mechanical wherever possible** (value-copied constants,
dangling anchors, never-fires branches, raw-DOM calls outside L1 are all scriptable). Standing
rule: every newly discovered problem type gets a catalog entry in the same commit (the
OPEN_ITEMS rule, applied to types).

## P8 — TWO RUNS, in this order (user-directed, 2026-07-10)

1. **Pass 1 — BLIND enumerative** (P1–P4, no suspects named, catalog withheld): finds new
   types without anchoring. Types discovered here are PROMOTED into the catalog immediately.
2. **Pass 2 — SIGNATURE sweep** with the FULL catalog (known types + pass-1 promotions):
   every catalog row applied across the whole layer — mechanical signatures as scripts over
   all rows, review signatures row-by-row against the P1 inventory.
The order matters: blind-first prevents the catalog from anchoring enumeration (which would
re-import the bias P1 removed); signatures suffer no anchoring, so they run second at full
strength. Pass-1-vs-pass-2 disagreements feed the P6 error estimate. Certification requires
BOTH passes complete.

## P9 — Scope: code that is about to be deleted gets NO audit (user-corrected 2026-07-10)

Applied BEFORE P1's enumeration. The module is partitioned against the retirement map: **code that
retires gets no audit at all** — the only thing owed to it is the #12 no-information-loss check at
the moment of deletion (does anything it knew go unrecorded?). The surviving stack is then audited
exhaustively, layer by layer, in dependency order, which is the plan P1–P8 describes. *Why:* the
alternative form — audit whatever a session happens to touch — was put to the user and REJECTED as
risky: touching one per cent of the module would audit one per cent while new work built on the
unaudited remainder, itself a #18 violation (an unverified premise carrying load) across the whole
architecture. Recorded at `OPEN_ITEMS.md` OI-84, corrected 2026-07-10 at the user's challenge.

**The rule's own boundary, ruled by the user 2026-07-28:** it does NOT shield the joint estimator
module. That module is production on both the batch and the notation surface and is not retiring, so
the retiring-code exemption does not reach it — which is why the OI-199 review was pulled forward
onto it rather than deferred behind the retirement map.

## The one-line summary

Bias picks queries; so remove queries — machine-generated total inventory (P1), fixed rubric
(P2), both directions (P3), measured behavior (P4), blinded redundancy (P5), a measured error
rate instead of a completeness claim (P6) — and then run the known-problem signatures anyway,
blind pass first, catalog pass second (P7/P8), so new types and known instances are BOTH
caught.

*Cowork, session 36. First application: the L1/L2 certification audit (OI-84). The protocol
is itself subject to #16: each audit stamps the inventory-generation script + corpus hash it
ran under, so a certification is reproducible.*
