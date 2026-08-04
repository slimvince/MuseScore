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

## P10 — Verification is organised BY LAYER: a layer is audited once its pieces are in place (user-recorded standing method, 2026-06-14)

Auditing is not something done to each change in isolation. When a layer's pieces are built, that layer is
audited as a whole, and the work moves on only then. This is the verification model for the back half of the
programme, and it is what P9's dependency-ordered partition and P8's two runs are the method OF: P10 says
*when* an audit is owed, P8/P9 say *how* it is run and over what. *Why:* a user-recorded standing method —
the alternative, verifying per change, was what left the module with a coverage figure nobody could state.
It was realised as the dependency-ordered per-layer certification plan (`OPEN_ITEMS.md` OI-84, complete
2026-07-12), which is the same rule applied end to end. Ratified by the user 2026-06-14; homed here
2026-08-02 from `cowork_handoff_archive.md` (`OPEN_ITEMS.md` OI-272), a surface two governing documents
declare outside the session-start read.

## The one-line summary

Bias picks queries; so remove queries — machine-generated total inventory (P1), fixed rubric
(P2), both directions (P3), measured behavior (P4), blinded redundancy (P5), a measured error
rate instead of a completeness claim (P6) — and then run the known-problem signatures anyway,
blind pass first, catalog pass second (P7/P8), so new types and known instances are BOTH
caught.

*Cowork, session 36. First application: the L1/L2 certification audit (OI-84). The protocol
is itself subject to #16: each audit stamps the inventory-generation script + corpus hash it
ran under, so a certification is reproducible.*

---

## The dispatch protocol these audits are commissioned and run under

**Homed here 2026-08-02 (`OPEN_ITEMS.md` OI-266; register entries D-250, D-251, D-252).** Every
audit above is commissioned as a written instruction to a working session and executed by that
session; P5's withheld-finding rule and P8's blind-pass-first ordering are already rules about how
that instruction is *written* and *sequenced*. The three rules below are the rest of that protocol.
They stood for months recorded only in `cowork_handoff.md`, which is a place for tracking a
handover, not a home for a standing rule — the finding that produced this section. **Their scope is
wider than this document's audits**: they govern every dispatch, and this document is their home
because it is where the project's dispatch-construction rules already live.

### One side writes the instruction files and the other executes them, never the reverse

**Cowork writes instruction files. CC executes them. Never the other way around.** When the user
says "go", "execute", or names an increment, the response is that the instruction is ready at its
`cc_instruction_*.md` path and should be given to the executing session. The planning side **may**
read source files via the file tools, write `.md` instruction files, and update `cowork_handoff.md`
and `STATUS.md` after a report lands. It **must not** edit anything under `src/`, run builds, or
spawn agents that run build commands or modify `src/`. *Why:* violating this rule has broken the
codebase twice, at the E1 and E2b increments — the evidence is stated with the rule itself.

### Dispatches are written only when they are next; a parked instruction is revalidated first

**Do not write instructions ahead of need.** At most **one** instruction is dispatched or being
executed at a time. The next instruction is written only once its predecessor's report is ratified
and it is actually the next dispatch — never speculatively. Upcoming work is recorded as **plan
lines** (the roadmap, the `STATUS.md` "next" entry), not as pre-written instruction files. Any
instruction file that exists but is not the active dispatch carries a **`⏸ PARKED` banner** and must
be revalidated against the then-current `STATUS.md` and HEAD immediately before dispatch, receiving
a dated dispatch note; an executing session must not run a parked instruction without that note.
*Why:* the three failure modes are stated with the rule — a pre-written instruction goes stale as
its premises change under it, risks being skipped, and risks out-of-order execution.

### A running dispatch is never interrupted or steered mid-flight

**No mid-flight steering (user, 2026-07-05):** a running session is never interrupted or relayed to.
Every instruction must therefore be **self-sufficient** — every foreseeable fork is carried inside
it as a stop or branch rule, and anything not covered waits for the report and is ruled at
verification. The only mid-run channel is the one the executing session itself opens, its own STOP
question, answered when it asks. *Why:* the evidence is stated with the rule — interruptions have
several times proven disastrous.

### A figure enters a dispatch or a report by CITATION to a generated artifact, never by transcription

**Ruled by the user, 2026-08-03.** A quantity may not be copied into a dispatch or into a session
report as a literal value. It is named as **an artifact and a field** — *`tools/audit/decisions/
phase1m_measurements.json` → `task6_reading_yield.owed_a_full_read`* — and the reader takes the value
from the artifact. The same holds for a **premise**: a claim of fact about the code, the corpus or
the record is cited to the primary source it can be checked at, never carried across from a surface
that merely repeats it.

This is `CLAUDE.md` principle **#17(f)** — *no hand-transcribed measurement numbers; figures enter
docs only via generated artifacts* — applied where it was being ignored. #17(f) was written for
DOCUMENTS and was honored there: the decisions register, the disposition manifest and the phase
measurement artifacts are all generated. Dispatches and session reports were treated as outside it,
on the unstated ground that they are working correspondence rather than record. They are not outside
it: a dispatch's premise becomes the next session's starting assumption, and a report's figure
becomes the next report's baseline. **Both sides are bound — the writing side's dispatches and the
executing side's reports alike.**

*Why:* measured, over the three waves that ran under this protocol before the ruling. Each instance
is a value or a premise taken from a secondary surface rather than a primary one, and each was caught
by a dispatch's own ordered check rather than by the writer's reading:

1. **A dispatch premise refuted at the commit.** The phase-1l dispatch held one half of the
   two-deferred-refactors mandate to be owed against retiring code; the file split it names had been
   delivered on 2026-06-17, and five later records — two of them user-ratified surfaces — still called
   it parked. `OPEN_ITEMS.md` OI-286.
2. **A dispatch premise refuted at the control flow.** The phase-1m dispatch held the post-hoc gate
   layer reachable on the live notation arm through the tick-local fallback; the record arm returns
   above that fallback whenever the record flag is set, which is its default. `OPEN_ITEMS.md` OI-288.
3. **A coverage count that rode forward unchecked for three waves.** "38 of 143 read" was 34 by its
   own stated basis; the difference was carried into 39 and then 40 before the partition was derived
   mechanically and came out at 36 read / 41 excluded / 66 owed. The `OPEN_ITEMS.md` OI-207 note of
   2026-08-03, §0.
4. **Three rank correlations reported with no generator behind them.** The proxy figures in that same
   note were computed outside `gen_phase1m_measurements.py` — the tool contains no correlation code —
   so a second recomputation returned a different value for the strongest of the three, and the
   difference could not be attributed because neither computation was reproducible.
5. **A total transcribed from an artifact that then moved inside the same wave.** The same note states
   a yield of 157 entries over the documents read in full; the committed artifact's
   `task6_reading_yield.yield_total_entries_homed_in_read_documents` reads 160, because three register
   entries homed in an already-read document were added after the sentence was written. `--check`
   passes, so the artifact is current and the sentence is not.

Instances 1 and 2 are the reason the rule covers premises and not only numbers: a wrong premise costs
a whole task, where a wrong figure costs a sentence. Instances 3 to 5 are the reason it covers reports
and not only dispatches: every one of them originated in a report's own prose and was inherited by the
next dispatch as fact. `OPEN_ITEMS.md` **OI-283** is the register-side instance of the same shape — a
hand-typed coverage claim inside a generated file — and its remedy is now one instance of this general
rule rather than a one-off.

### A count of OUTSTANDING work is DERIVED from state, never taken from the membership of a list of asks

**Ruled by the user, 2026-08-04** (dispatch `cc_instruction_phase1_delegations_and_corrections.md`,
R4). A figure reporting how much of something is still owed is computed from the CURRENT STATE of
each candidate, at HEAD. It is **never** taken from the length of a list that records what was asked
for, and never from an authored disposition field written beside the row when the ask was made.
**A list of asks carries no state**, and #12 keeps a satisfied ask in it rather than deleting it — so
its membership counts asks EVER MADE, which is a different quantity and is always the larger one.

*Why:* measured at the instance that produced the ruling. The OI-293 / OI-327 **write list** — the
homes the record means to keep, each awaiting a delegation only the user may write — was read two
ways at once, and both were wrong in the same direction:

1. **The count was the list's length.** `tools/audit/gen_phase1_completion_inventory.py` reported
   `documents_awaiting_a_delegation_only_the_user_may_write` as `len(write_list)`, inside the artifact
   a phase-1 completion statement would rest on. Derived at HEAD from the delegation grades and the
   home data, the figure is a small fraction of it — and the derivation additionally names a document
   the write list never carried, so the list was wrong in both directions at once about WHICH
   documents are outstanding.
2. **The per-row state was an authored field, and a second one was appended beside it.** Each row
   carries a `disposition_2026_08_04`; read wave 6 then answered two of those rows in a NEW field,
   `disposition_2026_08_04_wave6`. The reader read only the first and published *"NOT WRITTEN —
   WITHHELD"* for a document the user had since delegated to, and for one the user had ruled is not a
   delegation target at all.

**The remedy is not a status field on the list** — that is the same authored-field hazard a third
time. The list keeps its role as the record of what was asked for, with each draft wording and each
reason (#12), and **states in its own data that its membership is not a count of outstanding work**;
the STATE is derived, at `tools/audit/decisions/outstanding_delegations.json`. This is the general
form of the same shape `OPEN_ITEMS.md` **OI-283** and the figures rule above already carry: a
recorded finding that is never marked discharged becomes a count of work that is no longer owed.
Tracked at `OPEN_ITEMS.md` **OI-335**.

### The writing side runs the standing self-check too, before a dispatch is released

**Ruled by the user, 2026-08-03.** `CLAUDE.md`'s standing self-check already binds both sides in its
own words — *"code, scripts, instruments, and document edits alike — and BEFORE reporting the work
done… The check is of the work actually on disk, not of the intention"*. It has been observed on the
EXECUTING side and not on the WRITING side. It is therefore stated here, where the rules about how a
dispatch is written live: **before a dispatch or a decision surface is released, the writing side
runs the standing self-check over it and RECORDS the output.** Releasing without that record is the
same defect as shipping a diff unchecked.

**The mechanism, so this is more than a habit.** Every dispatch and every session report carries a
**self-check section**, and its ABSENCE is a failure the process check reports
(`tools/audit/process_check.py`). The checklist the section answers, item by item:

1. **The guiding principles** — which of #1–#24 the work touches, and whether it conforms.
2. **The conventions** — American English; no self-invented labels, abbreviations or numbering; the
   music-theory words used only in their musical sense, every non-musical use qualified.
3. **The figures-and-premises rule** — every quantity named as an artifact and a field, every premise
   cited to the primary source it can be checked at (**D-431** above).
4. **The file-tools rule** — working-tree content read with the file tools; shell only for read-only
   git object queries by explicit hash and for the sanctioned scripts (`CLAUDE.md` Conventions).
5. **Uncertainty on any comparison** — a difference asserted between two measured quantities carries
   its uncertainty, or is not asserted (**#24**).

*Why:* measured, on this protocol's own output, and each instance is cited to the row or artifact
that records it rather than restated here — **(a)** a dispatch premise about a delivered refactor,
refuted at the commit (`OPEN_ITEMS.md` OI-286); **(b)** a dispatch premise about a live code path,
refuted at the control flow (OI-288); **(c)** a retirement-map citation corrected inside that same
row's own text; **(d)** a criterion released at document granularity when its own evidence was at
section granularity (OI-281); **(e)** a ratified-marker count estimated rather than derived
(`STATUS.md`, the phase-1l entry); **(f)** a LEGACY-mark set size that three surfaces of record state
differently (OI-289); **(g)** a reading-coverage count carried forward for three waves
(`tools/audit/decisions/phase1m_measurements.json` → `task6_reading_yield`); and **(h)** a comparison
between three proxies asserted without its uncertainty, against #24
(`tools/audit/decisions/phase1n_reading_regime.json` → `proxy.ordering_decision`). Every one of the
eight was found by the EXECUTING side, running the check the writing side had not.

### The three measured conditions a mechanism is judged on — and who decides when one fails

**Ruled by the user, 2026-08-03; AMENDED by the user the same day (the eleventh ruling set).** A
mechanism built to enforce one of these rules is judged on three conditions: **it runs
automatically with no human step, it has a measured detection rate against known instances of the
failure it is for, and it has a measured false-positive rate at or near zero on legitimate work.**
All three are measurable and none is judged. **A mechanism that fails any of them is REPORTED —
with the condition it fails, the measurement that shows it, and the reason that condition exists.
It is NOT removed automatically: keeping it or removing it is the user's ruling.** The reasons the
conditions exist are unchanged, and they are what the report must carry: one needing a human step
is a reminder, one with no measured detection rate is unestablished (#19), and **one that fires on
legitimate work gets switched off, which is worse than having none.**

**What the amendment changed, and what it did not.** The three conditions are untouched; so is the
requirement that each be measured rather than judged. What changed is the CONSEQUENCE. The rule as
first stated made failure self-executing — a mechanism failing a condition "is not kept" — which
puts a removal decision inside a measurement. The two are different acts: measuring is the
session's, deciding what a failing measurement means is the user's. The criterion now **informs**
that decision instead of pre-empting it. *Why the change is not a weakening:* nothing is trusted
that was not trusted before — a mechanism failing the detection-rate condition is still
unestablished under #19 and still may not be put under load; what it may no longer do is disappear
without a ruling, which would destroy the measurement's own evidence (#12) and hide the failure
from the person whose rule the mechanism enforces.

**The test this replaces, and why it was withdrawn.** The preceding rule — stated by the planning
side in the phase-1p dispatch (§6.4) — was *a mechanism must retire the prose it replaces, or it
is apparatus growth.* The user withdrew it on 2026-08-03 because it is a **structural proxy
standing in for a behavioral quantity, and an unvalidated one** — principle #17(d), which forbids
exactly that substitution. What is at stake is whether the running burden or the failure rate
falls; prose retirement measures neither. A rule may legitimately need stating for a human reader
**and** be enforced by a machine — that is not the duplication #6 forbids, as this register
demonstrates, being a generated surface whose source of record is a separate data file.

**The two mechanisms built under the withdrawn test are KEPT under this one**, and their
establishment artifacts are where their figures live rather than being restated here:
`tools/audit/process_check.py` (`tools/audit/process_check_establishment.json`) and
`tools/audit/shell_read_guard.py` (`tools/audit/shell_read_guard_establishment.json`). Neither
retires any prose, which is why they failed the withdrawn test and is not a defect under this one.
The guard's third condition is met only while it is ARMED; until it is, that is recorded as an
expected-failing check rather than as coverage (`OPEN_ITEMS.md` OI-292).
