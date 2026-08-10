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

### A DIRECTION with its artifact named is not a transcribed value

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_fifth_stop.md`, Ruling 35(c)). A
reading of the rule immediately above, recorded against it so that a session meeting the
prohibition meets the clause that says what it still permits. **A DIRECTION — *fewer than half*,
*the large majority*, *markedly better* — stated with the generated artifact CITED BESIDE IT is not
a transcribed value, and is what the rule above asks for.**

*Why the reading has to be written down:* the prohibition exists so that a quantity cannot enter
prose and then go stale while the artifact moves. A direction with its artifact named leaves the
value in the artifact and still tells a reader what was found. Without this clause the safe reading
of the prohibition is that ANY characterization of a result is forbidden — which would make a
finding unreportable, and sessions have repeatedly had to guess at where the line falls.

**What the clause does NOT admit.** It does not admit restating the value itself, in digits or in
words; the artifact and the field remain the only place a quantity is read. And it does not relax
**#24**: a DIFFERENCE asserted between two measured quantities still carries its uncertainty, or is
not asserted — a direction is a statement about one result, not a licence for an unqualified
comparison.

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

### "Complete" means complete relative to a NAMED DERIVATION, whose measured miss rate against the record is part of its name

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_fifth_stop.md`, Ruling 31; restated as
the standing statement by Ruling 37 of `cowork_rulings_2026_08_09_sixth_stop.md` when the derivation
it licensed came back negative). It belongs beside the three measured conditions above because it is
the same rule one level out: those say what a MECHANISM is worth unmeasured, and this says what a
COMPLETENESS CLAIM is worth unmeasured.

**A hand-made inventory's completeness is not known, and it becomes checkable BY DERIVATION.** The
candidate population is DERIVED from named surfaces; the existing hand-made list is demoted to
**SEED VERDICTS** rather than standing as the population; every derived candidate carries an
AUTHORED verdict; **an unclassified candidate is a STOP**; and the derivation is RE-DERIVED as the
tree grows. *Complete* thereafter means complete **relative to that named derivation** and to
nothing wider.

**AND THE DERIVATION IS MEASURED AGAINST THE SEED, WITH WHAT IT MISSES PUBLISHED AS PART OF ITS
NAME.** A derivation that misses a word the record already holds cannot be trusted to have found the
ones the record does not — so the miss rate against the seed is not a footnote to the claim, it is a
term of it. Where a derivation is not SOUND (it misses known positives) or not BOUNDED (it proposes
a population no session can rule on), that is REPORTED and the population stays advisory. **Nothing
is narrowed until the misses disappear:** fitting the derivation to the cases that motivated it is
the defect the catalog names DT-2.

*Why it is a standing rule rather than one pass's finding:* it is **#19** applied to a completeness
claim. An inventory trusted because nobody has found a gap in it is exactly the thing merely
unfalsified, and the register states the test nowhere else.

**What it does not authorize.** No rename, no guard, no fix to the analysis, no design and no
inference change. Adoption of a derived population as a diff-time check remains conditional on
MEASURED clean separation, which is the third of the conditions above.

### When a shell-read policy cannot decide, it DENIES — and the ceiling it cannot see is published in the measured rate

**Ruled by the user, 2026-08-08** (`cowork_ruling_guard_family_2026_08_08.md`, clauses 4 and 2).
Two standing statements about the guard that enforces the working-tree-read rule, both of which
bind beyond the act that introduced them.

**DENY ON INDETERMINATE, adopted as standing policy.** Where the guard cannot decide whether a
command reads working-tree content — the ruling's own case is a shell variable it has not
expanded — it DENIES. *Why, in the ruling's own asymmetry:* **a false deny costs a retry through
the file tools; a false admit costs an unverified read through the very mount whose measured
stale-content failure created the working-tree-read rule.** The two errors are not the same size,
so the policy is a consequence of that difference rather than a preference between them.

**AND THE POLICY'S CEILING IS PUBLISHED IN THE MEASURED RATE RATHER THAN LEFT SILENT.** Interpreter
code — a `python -c` or `perl -e` code string, or a heredoc body fed to one — is decided by policy
and not by a model of the language: a code string carrying a LITERAL path this repository holds is
denied, and anything else is admitted. **A code string that COMPUTES its path carries no literal
for any policy to see, and is therefore admitted**; that residual is carried as a row of the
establishment corpus, so the published deny rate REPORTS it. *Why the ceiling must be published
rather than merely known:* the guard cannot parse interpreter code, and a policy behaving as though
it could would be a structural proxy standing in for a behavioral quantity, unvalidated — which
principle #17(d) forbids — while a rate measured over a corpus that excludes the shape the guard
cannot see bounds less than it appears to (#19). **A session that does not know the ceiling reads
the published rate as covering more than it does.**

**What this does not authorize.** No fix to the analysis, no design, no inference change, and no
further widening of the guard: a widening is a mechanism change, which stays the user's.

### Moving an authored judgment WHOLE into a retired block is MAINTENANCE, not a mechanism change

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_return.md`, Ruling 4(b)). A generated
pass whose inputs are partly AUTHORED — a per-document judgment, a per-entry verdict, a per-row
classification — STOPS when one of those inputs names something the tree no longer has. **Moving
that judgment WHOLE into the pass's own retired block, with the reason it retired and with nothing
deleted (#12), is AUTHORED-INPUT MAINTENANCE, and a session performs it. It is not a mechanism
change**, so the reservation stated immediately above — that a mechanism's fate is decided by the
user — is not engaged by it.

**Where the line falls, stated so it is mechanical rather than a matter of taste.** What is admitted
is a judgment FOLLOWING ITS SUBJECT: the subject left the pass's population, and the judgment goes
with it, unaltered, into the record of what the pass once judged. What is NOT admitted is
re-deciding that judgment, deleting it, authoring a new judgment for a subject the pass's own cut
did not reach, or changing the rule by which judgments are made — each of those is a mechanism
change. A retired judgment is protected in the other direction too: resurrecting one without
re-reading it STOPS the pass, so retirement is not a quiet way of dropping an authored input.

*Why it needs stating:* the two acts look alike at the diff, and a session that cannot tell them
apart either returns to the user on every stale authored input or edits mechanisms under the cover
of maintenance. It is recorded because the same shape recurred repeatedly across consecutive
batches, each time as a pass REFUSING TO RUN rather than as a defect a reader happened to notice —
which is those passes' own STOPs working.

### A mechanism change is decided over its WHOLE population BOTH WAYS before it is applied, and only the members the defect's own shape names may move

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_fourth_stop.md`, Ruling 25). The two
rules above bound the mechanism question from either side — how a mechanism is JUDGED once it
exists, and when the mechanism-change reservation is ENGAGED at all. This states what a mechanism
CHANGE owes BEFORE it is applied.

**THE CONDITION.** Every member of the population is decided under **BOTH** rules — the one live at
HEAD and the proposed one — before and after. **Only the members the defect's own shape names may
move. ANY OTHER MOVEMENT IS A STOP back to the user**, and the change is not applied.

**THE CONSTRUCTION, which is not a detail.** The table **implements both rules itself** rather than
reporting a diff of the result. That is the only construction that can SHOW a movement rather than
assert one: a diff of outputs says that something changed, while two independent decisions per
member say which rule moved it and in which direction. *(The second pass performed under this
condition added one thing to the form and it is recorded here because it decides whether the record
survives: the BEFORE half is read from a git object by explicit hash, never from the working tree.
A pass that takes its baseline from the tree can be run exactly once — the second run reports the
tree it has itself already changed — and one such record was overwritten by an accidental
invocation before the change was made. See `cowork_away_returns.md`, the fifth continuation's Task 1
log.)*

*Why the condition binds rather than merely advising:* it has already killed a ruled remedy. Applied
at the case that produced it, the both-ways table established that the proposed correction **fixed
one member of its population and broke two** — and a forward-only application would have reported
the fix and nothing else. It then did the same job a second time, in the other direction: the
re-reading of one member REFUTED the previous pass's account of it, which made the refuted remedy
worse than it had been recorded to be rather than better.

**What it does not authorize.** No mechanism change is authorized by this rule — whether a mechanism
changes at all stays the user's, as the reservation above states. This says what the evidence must
look like before the question is put.

### A generated record that must outlive its own writer is FROZEN at an established snapshot, and the freeze is a hash STOP

**Ruled by the user, 2026-08-08** (`cowork_rulings_2026_08_08_pre_away.md`, Ruling 1). **Where a
generated artifact RECORDS WHAT A PASS FOUND and the tool that writes it must go on running, the
artifact is declared HISTORICAL and frozen at an ESTABLISHED SNAPSHOT; the writer then runs at HEAD;
and the freeze is enforced by a STOP on the snapshot's own bytes.** The writing tool carries one
frozen CLASS EPOCH per completed pass on the same construction, so no value an earlier pass recorded
is overwritten by a later one (#12).

**Why the RECORD is frozen rather than the WRITER held.** The hazard is that a later wave regenerates
the record and the pass's findings go with it. The remedy previously in use was to HOLD the writer,
which stops a live derivation for as long as the record must survive — and which did not work: the
held run was performed by more than one later wave, and what preserved the record was the snapshot,
not the hold. The ruling's own words for the remedy are that the hazard is *"discharged by freezing
rather than by holding the writer forever"* — the epoch treatment a tool already applies to its own
fields, applied one level up, to the artifact.

**What makes the freeze a mechanism rather than a convention.** The snapshot's bytes are hashed and
re-checked on every run of the writing tool, so a regeneration over the record STOPS instead of
succeeding quietly. A promise in prose is exactly what #19 refuses to treat as established. The tool
that performs the freeze states the whole arrangement in its own docstring, which is what the
register points at rather than a second copy of the rule (#6).

**What it does not authorize.** No fix to the analysis, no design and no inference change. It says
how a record-bearing generated artifact is kept, and nothing else.

### A finding that bears on the analysis is SURFACED whatever its size; an apparatus finding is ROWED AND LEFT

**Ruled by the user, 2026-08-04** (dispatch `cc_instruction_commit_and_finish_line.md`, R3). Every
finding a session makes is sorted by **D-438's own test**, and by nothing else: *does the finding's
subject bear on the analysis, on the analysis's inputs, or on an instrument a measurement depends
on?*

- **If YES — it is SURFACED to the user for decision, WHATEVER ITS SIZE.** Not held for a later
  wave, not absorbed into the middle of a report, and never left as a row on the ground that it
  looked small. Size is not one of the test's terms.
- **If NO — it is ROWED AND LEFT: no wave, no dispatch, no surface.** The row is written, and the
  row is the whole of what is owed.

**★ THE EXCEPTION, STATED PLAINLY: AN ESTABLISHMENT OBLIGATION (#19) ALWAYS GATES, AND IS THEREFORE
ALWAYS SURFACED, WHATEVER ITS SUBJECT** — including one whose subject is this project's own
apparatus. R3 does not weaken that clause and does not touch it. The reason is the one
`CLAUDE.md`'s non-gating declaration already gives in the same words: backgrounding an
establishment obligation is how it never happens, and #19 exists because a thing merely unfalsified
is not established.

**What this ADDS to D-438, which it does not amend.** D-438 declares that a row whose subject is
this project's own tracking and documentation apparatus **gates nothing**. What D-438 does not say
is what such a row is then OWED. R3 answers on both sides — the duty to surface on the one, and,
the operative half, **the prohibition on spending a wave on the other.** Without it, "gates
nothing" had come to mean "still gets a wave, just not a blocking one", which is the same work at a
lower priority rather than less work.

*Why, in the user's own ground for the ruling:* **the apparatus is now large enough to generate its
own defect stream indefinitely, and treating each defect as owed is what produced a six-wave
backlog** — the state `OPEN_ITEMS.md` **OI-337** records — **while the findings that bear on the
objective came from reads and probes, not from apparatus repair.** That ground is the user's and is
recorded as the user's; this section derives no measurement of its own for it, and a later session
must not cite it as one. What it does have beside it is the record each wave left: the read waves'
yields are in their own artifacts (`tools/audit/decisions/reads<n>_yield.json`), and no value from
any of them is restated here (**D-431**).

**How it composes with the finish line.** R2 of the same ruling makes the derived finish line the
SCOPE — `tools/audit/phase1_finish_line.json`, regenerated by
`tools/audit/gen_phase1_finish_line.py`. R3 governs what happens to a finding made while an item on
that list is worked: it decides whether the finding is surfaced or rowed, and it never adds the
finding to the list. **Adding an item to the finish line is a user ruling**, which is what keeps a
scope from growing by the same mechanism this rule exists to stop.

**What it is NOT.** It is not permission to leave an apparatus defect undocumented — the row is
mandatory, and the open-items register's rule (c) still requires the row and its detail file in the
commit that records the discovery. It is not a claim that apparatus defects are harmless. And it
does not decide what PHASE 1 OWES: D-231's clause and D-639 decide that, and D-639 says in terms
that what a stage waits on and what phase 1 owes are different tests with different subjects.

### A session may AUTHOR an establishment; its verdicts clear no guard until the reviewed set is applied

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_third_stop.md`, Ruling 18). The block
immediately above says WHEN an establishment obligation starts gating. This says how it STOPS.
**A session is licensed to perform an owed establishment and to author its verdicts — by the
originating pass's own method and by no invented one (#6, #16) — and those verdicts CLEAR NO GUARD
when they are written.** They are delivered as a ratification-surface reading file; the standing
check goes on failing, deliberately, across the authoring session; and it clears only when the
REVIEWED set is applied, in a commit that cites the user's ruling on it. **Authoring and clearing
are two acts by two parties, and a session performs only the first.**

*Why the separation rather than a licence to author and apply in one act:* the objection this
answers was never that the work is hard. It is that **verdicts written in order to clear a guard are
the weakest establishment there is** — the session's own unreviewed judgment discharging the
session's own obligation, which is what #14 and #19 exist against. The remedy is structural rather
than exhortative: nothing self-ratifies, because at the moment of writing there is nothing the
verdicts could ratify. It also costs the user nothing to disagree, since a verdict the user rejects
is one line in a reading file rather than an edit that has to be unwritten.

**What it does not authorize.** It does not weaken the always-gates clause above, it does not permit
a verdict authored outside the originating pass's method — a session meeting a case that method does
not cover states the gap rather than substituting a method of its own — and it moves no status that
the reviewed application does not move. No fix to the analysis, no design, no inference change.

### Criterion C1 reaches every decision whose content is LIVE — a superseded entry's obligation moves to its successor

**Ruled by the user, 2026-08-04** (dispatch `cc_instruction_c1_ruling_and_item1c.md`, §0a R1).
**Criterion C1 — D-231's phase-1 obligation that every recorded decision is written into its owning
specification — reaches every decision whose content is LIVE.** A superseded decision's live content
lives in its **successor**; C1 is satisfied for that content **when the successor is homed**, and the
superseded entry itself is recorded in the register, which D-231 makes the status ledger for
supersession. **Where the successor is NOT homed, C1 is defeated and the owed act is homing the
SUCCESSOR — not the superseded entry.**

**The basis, at D-231's own clause.** The clause assigns two things to two places in one sentence:
*"the decisions register remains the status ledger (supersession, shelving, the same-commit rule),
never the conformance reference"*. Supersession and shelving are named there as two distinct things
the register is the ledger OF, and conformance is assigned to the specifications — so a superseded
decision is not something conformance is measured against. The clause is quoted **entire**, derived
at HEAD, at `tools/audit/phase1_completion_inventory.json` → `the_requirement.phase_1_verbatim`,
which is what the rule immediately below requires of a citation like this one.

**★ THE BASIS PREVIOUSLY CLAIMED IS WITHDRAWN, AND THE WITHDRAWAL IS PART OF THE RULING.** The
preceding dispatch (`cc_instruction_finish_line_item1b.md`) presented this ruling as an APPLICATION
of `OPEN_ITEMS.md` OI-272's per-kind home scheme to the superseded kind, and declared that reading as
an assumption with an instruction to STOP rather than stretch the scheme. The check came back
negative and **the reading is withdrawn**: the scheme partitions by what a decision IS rather than by
what its STATUS is, and applied at its own text it routes the affected entries the OPPOSITE way. The
four grounds that refuted it live at `open_items/OI-340.md` and are not restated here (#6) — a wrong
basis retracted is evidence (#12), and the row that produced the refutation is where that evidence
belongs.

**Where it is applied, and what it does not authorize.** The ruling is recorded against criterion C1
itself — `tools/audit/phase1_completion_inventory.json` → `the_requirement.criteria` → C1 — and
applied per entry over finish-line item 1's no-home class at
`tools/audit/decisions/r1_superseded_reach.json`; no verdict or count is restated here (**D-431**).
It authorizes no fix to the analysis, no design, no inference change, and no re-classification of any
entry's home class. It decides which entries criterion C1 reaches, and nothing else.

### A claim that invokes a ruling AS AN APPLICATION quotes that ruling in full, not the branch that supports the claim

**Ruled by the user, 2026-08-04** (dispatch `cc_instruction_c1_ruling_and_item1c.md`, §0a R2). **A
claim that invokes a ruling as an application of it must QUOTE THAT RULING IN FULL, not the branch of
it that supports the claim.**

*Why, at the instance that produced the ruling:* the withdrawn reading above cited OI-272's class
about shelvings, falsifications and dead ends — and **never put class 1 on the page.** Class 1 is the
branch that decided the case the other way: the entries at issue are, by kind, standing constraints,
so class 1 claims them, and class 1 prescribes homing them into the owning specification — the very
act the invoking ruling exists to forbid. Quoting the helpful branch is not a weaker citation of a
ruling; it is a citation of a different ruling, and the reader cannot see that it is one. *(The
scheme itself is quoted in full — all four of its classes — at `open_items/OI-340.md`, so this
paragraph's account of it is checkable at a primary source rather than taken from here, which is what
the rule it states would require of it.)*

**How it composes with D-431, which it does not amend.** D-431 requires a premise to be cited to the
primary source it can be checked at. This rule governs what the citation must then CARRY: the whole
of the ruling, including the parts that cut against the claim being made. **A citation that is
correctly sourced and selectively quoted satisfies D-431 and fails this one** — which is why it needs
stating separately rather than being read into D-431.

**Both sides are bound**, the writing side's dispatches and the executing side's reports alike, on
the same ground D-431 gives: a dispatch's premise becomes the next session's starting assumption.

### Where a superseded decision's content is a REMOVAL, the specification states the current behaviour and records the removal as a tried-and-closed line

**Ruled by the user, 2026-08-04** (dispatch `cc_instruction_guard_fix_and_item1d.md`, §0a R2).
**Where a superseded decision's content is a REMOVAL, the owning specification STATES THE CURRENT
BEHAVIOUR and RECORDS THE REMOVAL AS A TRIED-AND-CLOSED LINE; the register holds the status.**

**This is PRECEDENT, not a new rule.** It is what was already done at `ARCHITECTURE.md` §5.2 for the
declared-mode piece-start shortcut (`OPEN_ITEMS.md` OI-315, register entry **D-058**), and the ruling
names that act as its own source. The precedent is quoted **in full**, located by its own anchors and
re-read from `ARCHITECTURE.md` on every run, at `tools/audit/phase1_completion_inventory.json` →
`the_requirement.criteria` → C1 → the removal block; it is deliberately not restated here (#6), and a
rewording of it STOPS the derivation rather than leaving a stale account of it standing.

**What the precedent shows, and why it answers a question D-642 leaves open.** D-642 moves a
superseded entry's obligation to its **successor**. A removal has no successor: nothing later states
the rule, because the rule is that the mechanism is gone. Read without this ruling, such an entry
falls through — the register records it superseded, no specification carries it, and criterion C1 has
no closing act to name. The precedent supplies one, and it is two acts rather than one: the
specification is made TRUE about HEAD (there the specification had gone on asserting the removed
mechanism in the present tense, which is exactly D-231's doc-sync half), and the removal is recorded
where a later reader will meet it before retrying it. **Neither half alone is sufficient** — stating
the current behaviour without the tried-and-closed line loses the information that the alternative
was tried (#12), and recording the closed line without correcting the text leaves the specification
misdescribing the code.

**What it does not authorize.** No fix to the analysis, no design, no inference change, and no
re-classification of any entry's home class. It says what the owning specification owes for one shape
of entry, and nothing else.

### Where the implementation CONTRADICTS the decision being homed, the shelving is written in AS a shelving, the contradiction stated beside it, and the questions POINTED at their rows

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_return.md`, Ruling 5). Same family as
the two rules above: a FORM for writing a decision into a specification when the plain form would
state something false. **Where the record says a later build specified the opposite of the decision
being homed, the decision is written into its owning section AS WHAT IT IS — a shelving as a
shelving, a deferral as a deferral — the later build's contradiction is stated BESIDE it in a marked
block, and the two questions that would need a judgment (does the implementation conform, and what
should the rule now be) are POINTED at the rows that own them. NO VERDICT IS TAKEN either way.**

**The pre-act check the form carries.** The receiving section must STATE RULES rather than record
findings — the register's own kind test for a home — read before any home text is written. A
findings-recording section is a STOP back to the user, not a home to be argued into one.

*Why the form exists:* without it, a decision the implementation contradicts cannot be homed at all.
Writing it plainly states a rule the code does not follow; omitting it leaves the decision with no
home and criterion C1 with no closing act; and deciding which of the two is right is a judgment about
the analysis that a filing act may not take. The form lets the record become COMPLETE without
becoming untrue — **both facts visible, neither adjudicated** — which is exactly the split D-231's
own phase 1 draws between making the specifications complete and true, and fixing what they then
expose. It is now a twice-ruled, named pattern rather than a one-off treatment.

### Two same-dated texts are compared VERBATIM before either is retired into the other; where they bind different acts they are homed SIDE BY SIDE

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_return.md`, Ruling 7, and
`cowork_rulings_2026_08_09_second_stop.md`, Ruling 11 — one method, recorded as one rule because the
test and the remedy are useless apart). Same family as the form above.

**THE CONDITION.** Before a recorded decision is treated as ONE DECISION RECORDED TWICE and retired
into a text that appears to duplicate it, **the two texts are compared VERBATIM, at their sources,
and any BINDING difference is a STOP back to the user.** Sharing a date, an argument, a source and a
vocabulary is not the test; what the two texts FORBID is.

**THE REMEDY, where the condition fires.** They are two decisions, and they are homed **SIDE BY SIDE
in the same section, each cross-referencing the other**, with the more specific prohibition carried
in the words it was recorded in — never merged into one widened text. *Why side by side rather than
merged:* #6 forbids two homes for ONE rule, and two texts that bind different acts are demonstrably
two rules, so #6 does not demand the merge; while the merge itself would edit an already-ruled text
(#14) and risks paraphrasing away the narrower prohibition, which is a loss under #12.

*Why the pair is recorded rather than left to a reader's judgment:* applied at the case that produced
it, the comparison STOPPED a collapse that would have lost the more specific and more easily violated
of two prohibitions — a session could have obeyed the surviving text in full while breaching the one
about to be retired into it. Without the condition in the record, the next session meeting two
same-dated texts has only the temptation to tidy them into one; without the remedy beside it, a
session that runs the test correctly is left with a STOP and no form to write the answer in.

### Where the record does not settle the question, the surface that returns it to the user gathers FACTS and makes NO recommendation

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_fourth_stop.md`, Ruling 27), on the
user's own instruction, quoted in the ruling verbatim: *"follow the rule: fact based decisions or
exploration to gather facts are allowed, not decided on unsure/fabulated/misremembered facts."* The
third member of the family above, and the case those two do not cover: not *the plain form would
state something false*, but *the record does not answer the question at all*.

**THE FORM.** Where a question the session cannot settle has to go back to the user, the surface it
goes back on carries: **every claim CITED AT ITS SOURCE and read in place; the records concerned
READ WHOLE; anything the record does not settle marked UNSETTLED rather than filled — and NO
RECOMMENDATION AT ALL.**

**The last clause is the load-bearing one, and it is the one a session will be tempted to break.** A
fact-gathering pass that ends in a recommendation has decided the question it was sent to inform:
the user then rules on the session's reading rather than on the facts, which is the outcome the
instruction above exists against. Marking an item UNSETTLED is likewise an ANSWER and not a
shortfall — *the record does not address this* is what a reader needs in order to rule, and filling
it from the most plausible reading is the invention the never-work-from-memory rule forbids.

*Why the form earns its place:* applied at the case that produced it, gathering the facts settled
more than the question asked — and it LOCATED a conflict between two records that nobody had put
side by side, with two readings visible and neither chosen. A pass permitted to recommend would
have chosen one, and the conflict would have been resolved by a session's reading of intent rather
than by the user on facts.

### A correction that reconciles a specification to the arm that SHIPS carries the behavioural non-equivalence visibly, as unmeasured

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_second_stop.md`, Ruling 15). The
doc-sync case of the same family. **Where a specification names one implementation as a rule's
precondition and the arm that ships meets that precondition by a DIFFERENT design, the correction
states the requirement rather than the implementation, names the design on each arm — and MUST CARRY
THE RECORDED BEHAVIOURAL DIFFERENCE BETWEEN THE TWO ARMS VISIBLY, stated as UNMEASURED (#24). It may
not word the difference away as equivalence, and it may not claim either arm's output is the better
one.**

*Why the clause is needed on top of the correction itself:* an arm-reconciling correction invites
exactly one failure — it reads as *the two are the same*, and a real, unmeasured behavioural
difference disappears into a tidy sentence. That loses information the record held (#12) and asserts
an equivalence nobody measured (#24), on the surface a later design will treat as the compliance
reference. The instance that produced the ruling had that shape precisely: two mechanisms meet one
requirement, one erasing a condition unconditionally and the other only making it expensive, with no
comparison of the two outputs taken.

### A homing dispatch may edit three further files, and the license is scoped to homing acts alone

**Ruled by the user, 2026-08-07** (dispatch `cc_instruction_five_rulings.md`, §0a R1). **The edit
surface a HOMING dispatch may touch is widened to `docs/scoring_model.md`, `CLAUDE.md` and
`BUILD_AND_TEST.md`, SCOPED TO HOMING ACTS ONLY** — writing a register entry's decision into its
owning specification, in that section's own voice, with its defense, and with the entry's former
home, its former class and its former verbatim preserved (#12). **The license does not extend to any
other edit of those three files.**

**What the license is a license FOR.** Criterion C1 — D-231's phase-1 obligation that every recorded
decision is written into its owning specification — names an owning specification per entry, and for
part of finish-line item 1 that specification is a section of one of these three files. Until this
ruling a session could identify the owed act and not perform it, because the file lay outside the
standing authorization, which names `src/composing/`, `notationaccessibility.cpp` and
`ARCHITECTURE.md` and no other document. The widening removes that obstruction and removes nothing
else: a homing act writes a decision the register already holds into the section that owns its
subject, and every other edit of these files remains outside what a dispatch may take.

**The context the ruling was taken on, and the half it deliberately does not reach.** The blocker for
item 1's re-home class is partitioned at `tools/audit/decisions/item1_rehome_blocker.json`, derived
per entry from each row's own recorded reason. **Edit-surface licensing is the MINORITY** of that
class; the majority record an owner the record itself calls not determinate, and a widening moves
none of them. **That half is untouched by this ruling and returns to the user per entry.** No
population, identifier or count is restated here (**D-431**) — the artifact carries them.

**What it does not authorize.** No fix to the analysis, no design, no inference change, no
re-classification of any entry's home class, and no edit of these three files for any purpose other
than a homing act. **The dispatch that records the license performs no homing under it**: the ruling
and its first exercise are deliberately separate acts, so that what the license permits is on the
record before anything is written under it.

### Where a licence's letter leaves a known falsity standing in the file it licensed, the session CORRECTS it and REPORTS the widening in the same act

**Ruled by the user, 2026-08-09** (`cowork_rulings_2026_08_09_third_stop.md`, Ruling 17). The
subsection above states the SCOPE of a licence. This states the one case that scope does not cover.
**Where performing a one-edit licence to the letter would leave, in the very file being corrected, a
second instance of the same falsity made false by the same act, the session CORRECTS THAT INSTANCE
TOO AND REPORTS THE WIDENING IN THE SAME ACT — naming what it did, why the licence's heading-level
subject covers it, and what the one edit would be if the narrower scope was meant.**

**The half that keeps this from becoming a precedent, and it is the half worth the care.** A widening
that is REPORTED is reviewable; a widening that is SILENT is not, and would not have been accepted.
**The one-edit licensing discipline's narrow-letter default is UNCHANGED for every future licence.**
This rule does not say a session may read a licence past its letter; it says what a session OWES when
the letter leaves a known falsity in place — correct it and report it, and do not thereafter treat
the licence as having been wider.

*Why the correction rather than the letter:* leaving the second instance would ship a statement that
is false at HEAD, in the very file being edited because its account of itself was false, which the
doc-sync half of phase 1 does not admit. The excluded alternative is recorded with the ruling —
reverting the second correction, which would knowingly re-insert a false statement in order to make a
process point.
