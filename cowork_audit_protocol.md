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

**★ THE RUBRIC FOR AN INFORMATION-LOSS SWEEP, AND ITS FOURTH VERDICT (user-ratified 2026-07-06;
written here 2026-08-09).** Where the sweep's subject is information the analysis produces,
**information not yet consumed is NOT automatically a defect**, and every site takes one of four
verdicts: **PRESERVED, awaiting a future or dormant consumer** — intact and carried, simply not read
yet because the consumer is not built; **LOST** — destroyed, overwritten, collapsed or dropped so
that no consumer, present or architecture-intended, can recover it; **SHOULD-ALREADY** — preserved
and available, but a consumer that exists today and ought to be reading it is not given it; and
**UNCLEAR — consumer status ambiguous**, which is **recorded for the user's adjudication and never
guessed**. *Why the first clause:* without it a proactive sweep manufactures findings, because every
correctly forward-provisioned fact reads as waste. *Why the fourth verdict:* it is what keeps the
rule honest in the other direction — #1 forbids guessing, so an ambiguous consumer status is written
down as ambiguous rather than resolved by the auditor. It is this section's closed-verdict-set rule
applied to one sweep's subject, and the escape it forbids is the same one.

**★ AND A VERDICT MAY BE *KEEP, DEFERRED* ONLY WHILE THE THING KEPT STAYS CHARACTERIZED EXACTLY
(user-ratified 2026-07-06; written here 2026-08-09).** Where a known loss is deliberately left in
place because the work that will close it is a planned later step, the disposition holds **only
while its exact shape stays written down** — what is stale, under what circumstances, and what is
not recomputed — and **the moment the behaviour drifts so that the loss is no longer precisely that,
the decision to keep it is re-adjudicated.** *Why:* stated with the ruling in the user's own words —
*keep as long as we know exactly what it is* — and the standing characterization is written out
beside the disposition so the condition is checkable rather than asserted. It is what separates a
deferral from an unexamined defect: a deferral names its future owner AND its exact form, so a later
reader can tell whether what stands is still the thing that was ruled on. **This bounds a
DISPOSITION, not a fix** — nothing here authorizes closing the loss, and the queue that owns the fix
is unaffected.

## P3 — Audit the negative space (spec→code, not only code→intuition)

Reading code and asking "does this look fine?" finds only what priors recognize. The second
direction is mandatory: from the layer's CONTRACT (architecture docs, the layer's declared
outputs), enumerate what the layer SHOULD handle and publish, then check each expectation
against the code. Absences (an unpublished fact, an unhandled case, a consumer that should
exist and doesn't) are findable only in this direction — the siloed-facts class was exactly
this.

**★ POINTER — THE METHOD BY WHICH A GAP THIS DIRECTION FINDS IS CLASSIFIED AND ADJUDICATED (written
2026-08-12).** How a specification-versus-code gap is CLASSIFIED, and what may ADJUDICATE it, is at
`cowork_spec_code_audit_adjudication_method.md` — a **Cowork reading surface for phase 2, NOT
ratified, NOT a specification and NOT an authorization**. A pointer, never a copy (#6): none of that
file's content is restated here, and it commissions no audit and licenses no probe. *(It sits at the
section's end rather than inside the text above because that text is quoted whole as a
decisions-register entry's verbatim, and an insertion into it would put 2026-08-12 words inside a
decision ruled 2026-07-10 — the placement error the preceding batch's own R3 pointer made and
corrected.)*

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

### Every dispatch's read-first block names the CURRENT HANDOVER BLOCK of `cowork_handoff.md`

**Ruled by the user, 2026-08-17 — limb (c) of Ruling 2 of
`cowork_rulings_2026_08_17_ninth_return.md`; written here 2026-08-18 by
`cc_instruction_preparation_tenth.md` Task 3.** **Every dispatch's read-first block names the
current handover block of `cowork_handoff.md`.** It is a rule about how a dispatch is WRITTEN, so
it binds the writing side, and it stands beside the self-sufficiency rule above rather than inside
it: an instruction can be self-sufficient about the work it orders and still send the executing
session in without the one thing both sides share.

**THE GROUND IS FINDING F58, and it is stated because the rule is unreadable without it.** Both
sides record findings in ONE shared numbered series, and there is no single place where the next
free number is allocated: each side takes the next number after the highest it knows about. The
current handover block is where the writing side announces its own additions to that series, so a
session that has not read it cannot know where the series stands. **The measured instance:** the
writing side numbered two findings F52 and F53 in one handover block; the executing session, which
knew the series stood at F51, numbered from F52 — and **F52 was double-booked across two different
findings.**

**THE SHARPER HALF, and the reason the remedy is a read rather than a numbering convention.** The
dispatch that produced the collision named `cowork_handoff.md` three times — as something to
commit, as the subject of an assumption's check, and as a place to WRITE two corrections — and
never once as something to READ. **So the executing side was routed to write into the file that
carried the number assignment, three blocks below where the assignment was made, without ever being
routed to read it.** **The lesson, in its general form: a dispatch that orders a write into a
document must also order the read of it.**

*What this rule does not do:* it fixes no numbering scheme, allocates no number, and grades no
finding. It names one file and one block, and the allocation follows from both sides having read
the same thing.

### A ruling record taken from a GENERATED DOCUMENT names the commit it was ruled at

**Ruled by the user, 2026-08-18 — the forward clause of Ruling 1 of
`cowork_rulings_2026_08_18_tenth_return.md`; written here by
`cc_instruction_preparation_eleventh_amended.md` Task 2.** **A ruling record whose sitting was held
over a GENERATED document names, in that record, the commit the document was ruled at.** It is a rule
about how a ruling record is WRITTEN, so it binds the writing side, and it stands beside the
read-first clause above for the same reason: both are about what a document must carry so that a
later mechanism can do its work without guessing.

**THE GROUND IS FINDING F60.** A generated document is rewritten whenever the data it is generated
from moves, so the document a ruling was actually taken over survives only at the commit that carried
it. The rule that protects it — a generated document put to the user for a ruling joins the pinned
kind, and its generator thereafter reads its inputs at the git objects of the commit the ruling names
— needs that commit to be findable. **The measured instance:** of five members reached by the
document route, exactly ONE carried the commit in its record; the other four named the document and
no commit at all, so the rule could not be applied to any of them without either amending the rule or
amending the records.

**THE GENERAL FORM, which is what outlives the instance:** *a rule whose operative clause names a
field the records do not carry cannot be applied without amending either the rule or the records.*
Amending the rule leaves a second resolution mechanism standing for every future member, which is
what #6 exists against; amending the records closes it, and the rule then needs nothing further.

*What this rule does not do:* it pins nothing, resolves no member and grades no ruling. It says what
a ruling record carries; whether any particular generator is pinned is that member's own question.

### Where the ruled rendering and the committed document have SEPARATED, the ruling record names the BLOB and the member stays unpinned

**Ruled by the user, 2026-08-19 — the forward clause of Ruling 1 of
`cowork_rulings_2026_08_19_eleventh_return.md`, ruled AS A CLASS; written here by
`cc_instruction_preparation_twelfth.md` Task 2.** **WHERE A GENERATED DOCUMENT'S COMMITTED CONTENT
HAS SEPARATED FROM THE RENDERING A RULING WAS TAKEN OVER, THE RULING RECORD NAMES THE BLOB OF THE
RULED RENDERING AND THE MEMBER IS RECORDED NOT PINNED WITH ITS REASON.** It stands beside the clause
immediately above because that clause says a ruling record names the COMMIT, and this says what the
same record carries once the commit alone no longer reaches the rendering. **It reaches only the
separated case:** where the ruled rendering and the committed document are still ONE document, a pin
also buys per-run enforcement and continues to be taken exactly as the rule that orders it says.

**THE GROUND IS FINDING F76.** A pin taken after the ruled rendering has already been rewritten
cannot both fix its inputs and pass its own check. **The measured instance:** of four members
re-derived at the git objects under the landing-commit bound, two could not be pinned although both
commits were established. On one, the committed document had drifted from the ruled rendering
through a later act of the same arc, so fixing the generator's input routes at the ruled commit
would render a document that is not the committed one. On the other the pin is not constructible at
all — an input the generator now reads did not exist at that commit — and the drift there IS the
sitting's own executing act, so reverting it would destroy the record of what was RULED.

**THE GENERAL FORM, which is what outlives the instance:** *the pin protects TWO things that are
normally one rendering — the evidence of what was PUT and the record of what was RULED — and once a
post-ruling regeneration has separated them, no single commit holds both.*

**WHY NAMING THE OBJECT ANSWERS IT.** The pin was only ever a means; its end is that a later reader
can obtain the rendering the user ruled from, and git already provides that end exactly and
self-verifyingly, provided the record names the object. **#12** is met in the shape this project
already uses everywhere else — the former rendering stands in git at the commits that carried it —
and **#19** more strictly than a pin meets it, a blob being content-addressed and self-verifying
where a pin's guarantee is only as good as the check that enforces it. **THE COST THE USER ACCEPTED,
recorded because an accepted cost is not a discharged one:** a pin re-proves the evidence on every
run, and a named blob is proved only when a reader goes and looks. It is bounded by the fact that a
blob cannot silently rot — git either produces that object or errors loudly, the same self-verifying
property **D-253** already rests on.

*What this rule does not do:* it unpins nothing and re-takes no pin — a member already carrying one
is untouched — and it authorizes no restore, no overwrite and no regeneration of any document.

### A dispatch's DECLARED START STATE is stated at the tree the dispatch will meet, including the reds its own inputs cause

**Ruled by the user, 2026-08-18 — the standing clause riding Ruling 1 of
`cowork_rulings_2026_08_18_eleventh_stop.md`; written here by
`cc_instruction_preparation_eleventh_amended.md` Task 2.** **A dispatch's declared start state is
stated at the tree the dispatch will actually meet, INCLUDING the reds the dispatch's own inputs
cause, EACH NAMED WITH ITS CAUSE.** It is a rule about how a dispatch is WRITTEN, so it binds the
writing side, and it stands beside the read-first clause above rather than inside it: a dispatch can
name the right handover block and still declare a start state it could not have had.

**THE GROUND IS FINDING F67.** A dispatch commonly lands its own authority — the sitting record it
executes, the dispatch itself, the report that preceded it — and those files sit on disk, untracked,
before the executing session boots. **A derivation whose population is the FILE SYSTEM rather than
the git index is therefore already moved by them.** **The measured instance:** a dispatch declared
the previous batch's proven end state as its start state; the executing session measured a SECOND
red before its first edit, because the membership derivation it was told to bind at lists the
repository root on the file system and two of the dispatch's own untracked inputs were root-level
ruling records. The dispatch's own words made that a STOP-and-report, and the batch returned with
nothing executed.

**THE GENERAL FORM, which is what outlives the instance:** *where a derivation's population is the
file system rather than the index, an untracked file is already inside it — so any state declared
"the previous batch's proven end state" is false for every such derivation the moment the next
dispatch's own inputs are written.*

**THE TWO ALTERNATIVES DECLINED are recorded because an excluded alternative is evidence about the
choice.** Deriving the population from the git index instead was declined: the artifact would then
report fewer ruling records than sit on disk, so a measurement whose subject is the evidence a ruling
was taken from would stop counting a ruling record that exists and was ruled from — #12's own
direction of loss. Exempting the check was declined as #19's silent-failure direction: a standing
exemption teaches sessions that a red on that tool means nothing, and removes the one mechanism that
caught the false premise.

*What this rule does not do:* it changes no measurement tool, exempts no check, and authorizes no
session to work around a red. It says what the DECLARATION must contain.

### Where a derivation reaches its inputs by MORE THAN ONE ROUTE, a prediction about its output is taken from EVERY route

**Ruled by the user, 2026-08-19 — the second clause of Ruling 2 of
`cowork_rulings_2026_08_19_eleventh_return.md`; written here by
`cc_instruction_preparation_twelfth.md` Task 2.** **WHERE A DERIVATION REACHES ITS INPUTS BY MORE
THAN ONE ROUTE, A PREDICTION ABOUT ITS OUTPUT IS TAKEN FROM EVERY ROUTE.** **It stands beside the
declared-start-state clause immediately above because it is the second half of the same lesson:**
that clause says a dispatch declares the reds its own inputs cause, and this says that where the
dispatch also predicts WHAT those inputs will change, the prediction is taken from every route by
which they reach the derivation.

**THE GROUND IS FINDING F75.** A dispatch predicted a regenerated artifact's whole difference as a
count and two added names. **The measured instance:** the difference carried a third hunk as well,
additive, arriving by the derivation's OTHER route — a scan of a ruling record's entire text for a
measurement tool the record names as fixed to a commit, where the predicted route was the population
of ruling records themselves. The route the dispatch predicted from was the one whose cause it
already knew.

**THE GENERAL FORM, which is what outlives the instance:** *a prediction drawn from the route whose
cause is known reads as complete when it is not.*

*What this rule does not do:* it changes no derivation, adds no check and grades no difference. It
says what a prediction about a derived artifact's difference must cover before it is stated.

### A check on a derived artifact's difference bars the MOVEMENT of a value, not the ADDITION of a derived cross-reference the ordered act causes

**Ruled by the user, 2026-08-19 — the sharpened bar of Ruling 2 of
`cowork_rulings_2026_08_19_eleventh_return.md`; written here by
`cc_instruction_preparation_twelfth.md` Task 2.** **A CHECK ON A DERIVED ARTIFACT'S DIFFERENCE BARS
THE MOVEMENT OF AN EXISTING VALUE, AND DOES NOT BAR THE ADDITION OF A DERIVED CROSS-REFERENCE WHOSE
CAUSE IS THE ACT THE DISPATCH ITSELF ORDERS.** It stands beside the two clauses above because all
three govern the same moment: a dispatch's ordered check over an artifact its own act regenerates.

**THE GROUND IS THE MEASURED EPISODE THAT FORCED IT.** A dispatch's ordered check listed the kinds of
thing a bookkeeping regeneration may not move, and stated its own purpose in terms — *the
regeneration is a bookkeeping act and may not move a verdict*. The regeneration added ONE field
cross-referencing a ruling record the same dispatch had just landed, and moved no member, no route,
no document, no pin constant, no state and no count: **the stated purpose was met in full.** Read
strictly, the added field named one of the listed kinds in a second place, so a session could have
STOPPED — and that reading would have returned a second consecutive batch with nothing executed, over
an additive cross-reference produced by the very act the dispatch ordered.

**THE GENERAL FORM, which is what outlives the instance:** *enforcing a bar past its own stated
purpose is how a STOP becomes ritual rather than a guard.* The narrowing is stated in those terms —
**added, derived, and caused by the ordered act** — rather than left as discretion, because a STOP
condition exists precisely to remove a judgment from the executing side, which is **D-251**'s own
shape.

**THE ALTERNATIVE DECLINED, recorded because an excluded alternative is evidence about the choice:**
leaving the bar as written and judging each case was declined as the *"stable enough to be cited"*
failure the record already names and **D-639**'s own worked example — a criterion that reads as
mechanical and resolves case by case.

*What this rule does not do:* it widens no check, exempts no artifact and admits no movement of a
value. An addition still enters the report, with its cause established at the record's own text.

### A SITTING RECORD is an interim carrier, and the commit that lands it bounds when the sitting was held

**Ruled by the user, 2026-08-18 — the forward clause of Ruling 3 of
`cowork_rulings_2026_08_18_eleventh_stop.md`; written here by
`cc_instruction_preparation_eleventh_amended.md` Task 2.** **A sitting record is an interim carrier:
it is written in the turn its ruling is given and lands in git at the next dispatch's Task 0 — so THE
COMMIT THAT LANDS IT BOUNDS WHEN THE SITTING WAS HELD.** This writes down a practice the record has
followed throughout and had never stated. **It is what a dated correction under the clause two above
may cite for its bound**, and it binds both sides.

**THE GROUND IS FINDING F72.** A derivation that must locate the rendering a user actually ruled from
needs an upper bound on when the sitting was held, and the record supplies one that is finer than the
date: the sitting record's own landing commit. That bound was proposed with **D-230** cited as its
authority. **D-230's verbatim text is the decisions register's rule (c)** — *"a new ratification,
shelving or falsification gets its register entry (data + regenerated files) IN the commit that
records it"* — and it says nothing about a sitting record, an interim carrier or a dispatch's Task 0;
no entry in that register's INDEX states the practice either. **The practice is real, uniform across
the arc and derivable per member at the git objects; what was missing was a rule the record carries.**

**WHY THE BOUND MATTERS RATHER THAN THE DATE, measured on the member that forced it.** Four commits
touched one ratification surface on its sitting's own day. A date-granularity reading selects the
last of them — which lands after the sitting record reached git AND after the sitting's own executing
act — so it pins a POST-RULING rendering and records it as the evidence of what was PUT. That is the
precise defect the pinning rule exists against, arriving on the exact member that rule's own ground
names as its reason for adding a date bound at all. **The bound fails on its founding case; the
landing commit does not.**

**THE GENERAL FORM, which is what outlives the instance:** *a practice every session follows and
every record cites is not thereby a rule, and a claim invoking a ruling as its authority must be
checkable at that ruling's own text* (**D-643**).

*What this rule does not do:* it dates no sitting by itself, pins nothing, and replaces no per-member
derivation — the landing commit is derived per member at the git objects, and the derivation is
published with the pin it supports.

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

### A published CHARACTER FIGURE names the tool that produced it

**Ruled by the user, 2026-08-18 — the standing clause riding Ruling 3 of
`cowork_rulings_2026_08_18_tenth_return.md`; written here by
`cc_instruction_preparation_eleventh_amended.md` Task 2.** **A character figure published anywhere in
the record — the size of a read, of a file, of a span — NAMES THE TOOL THAT PRODUCED IT.** It stands
beside the rule immediately above because **it is that rule's own missing half: the rule above says
where a figure comes FROM, and this says that a reader must be able to SEE where it came from.**

**THE GROUND IS FINDING F66.** A figure whose producer is not named cannot be reproduced, cannot be
challenged, and cannot be told apart from a hand measurement — and a hand measurement is admissible
as evidence for a ruling, never as the record's published statement of a quantity. **The measured
instance:** a session-start-read size and a reduction percentage derived from it were published in a
handover block's opening sentence, at the top of the entry point, one turn after the measurement they
rest on was taken by hand. When a generator was later built for the same quantity it reproduced
neither figure; the total was low by 6,908 characters and the whole gap was one term.

**THE GENERAL FORM, which is what outlives the instance:** *a figure that becomes a headline is
checked at a generator before it becomes one.*

*What this rule does not do:* it forbids no measurement and withdraws no figure. It says that a
published one carries its producer's name, which is what makes the rule above checkable rather than
merely obeyed.

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

### An ENUMERATING PATTERN whose reach has never been measured may STATE its bound on its own artifact instead of owing a detection measurement — and the test is whether an ANALYSIS DECISION consumes it

**Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_fourteenth_stop.md`, Ruling 60, taking
the proposed decision of Ruling 59 of `cowork_rulings_2026_08_11_thirteenth_stop.md`). It belongs
beside the two sections above for the reason the second gives for its own siting: those say what a
MECHANISM is worth unmeasured and what a COMPLETENESS CLAIM is worth unmeasured, and this says which
of the two an ENUMERATING PATTERN is — a search expression run over text to locate every instance of
a class.

**THE RULE.** Where such a pattern's reach against the text it scans has never been measured, the
limit may be **STATED ON THE PATTERN'S OWN ARTIFACT** — marked advisory, with its empty verdict
recorded as bounding nothing — **instead of a detection measurement being owed**. **THE TEST FOR
WHICH IT IS: does an ANALYSIS DECISION CONSUME the enumeration?** Where one does, the measurement is
owed exactly as the three conditions above require and the bound is no substitute for it. Where none
does, the bound is the whole of what is owed.

**The bound is not a weaker measurement, and the difference is what makes the rule safe.** A stated
bound claims nothing about coverage: it records that the pattern's misses are unknown, so an empty
run is evidence of nothing and may not be cited as one. What it removes is the standing debt, not
the ignorance.

*Why it is a rule rather than one pattern's treatment:* as the record stood without it, **D-436**'s
detection-rate condition and **D-661**'s completeness rule together left every unmeasured pattern
owing a measurement that nothing would ever spend the effort on, and none was ever written off — so
the register carried the obligation and never its limit, and an obligation that cannot end is one
that never closes. The clause concentrates establishment effort where #19 actually buys something:
on the measurement chain that feeds inference. **The test is applied PER ENUMERATION and is not
inherited** — a pattern whose output no analysis decision reads is bounded, and its neighbour whose
output one does read is measured, however alike the two patterns look.

*The instance it was ruled at, and what that instance shows:* a comment sweep reported its class
empty at HEAD while an instance of the class stood in a file the correcting act had touched, and the
enumeration's reach had never been measured. Nothing in the analysis consumes a comment sweep — its
output is read by sessions maintaining the record — so the ruling stated the bound on that
artifact and declined to seed the measurement. **The excluded alternative is recorded:** owing the
measurement, which is the reading the record already carried and which had produced no measurement
in any of the waves that met the pattern.

### A RECOGNIZER OVER A POPULATION states, at its own artifact, whether an INDEPENDENTLY-KNOWN population exists to reconcile against — and where none does, it publishes its output as a LOWER BOUND with its reach declared UNMEASURED, never as a census

**Ruled by the user, 2026-08-19 — the forward clause of Ruling 1 of
`cowork_rulings_2026_08_19_twelfth_return.md`, ruled AS A CLASS; written here by
`cc_instruction_preparation_thirteenth.md` Task 1.** **A RECOGNIZER OVER A POPULATION STATES, AT ITS
OWN ARTIFACT, WHETHER AN INDEPENDENTLY-KNOWN POPULATION EXISTS TO RECONCILE AGAINST — AND WHERE NONE
DOES, IT PUBLISHES ITS OUTPUT AS A LOWER BOUND WITH ITS REACH DECLARED UNMEASURED, NEVER AS A
CENSUS.**

**IT STANDS BESIDE THE THREE SECTIONS ABOVE, and the siting is the one those sections use of
themselves.** They say what a MECHANISM is worth unmeasured, what a COMPLETENESS CLAIM is worth
unmeasured, and what an ENUMERATING PATTERN is worth unmeasured. **This says what a RECOGNIZER OVER
A POPULATION is worth unmeasured, and it supplies the test the first of those three leaves open:**
the completeness rule immediately above demands a measured miss rate against a seed, and this says
what is owed where the record holds no second enumeration to measure a miss rate against.

**THE TEST, AND IT IS MECHANICAL RATHER THAN A MATTER OF TASTE: DOES SOMETHING OTHER THAN THIS
RECOGNIZER ENUMERATE THE POPULATION IT CLAIMS TO DESCRIBE?** Where something does, the recognizer is
**established** by both-ways reconciliation against it. Where nothing does, **the recognizer's output
IS the population, no seed set can establish it**, and the honest publication is a floor.

**THE GROUND IS FINDING F84, MEASURED RATHER THAN ARGUED.** A recognizer written from its known
instances recognises its known instances. **The measured instance:** a derivation over the tools' own
syntax trees was first written from the two members the record already establishes, and it reproduced
both — while missing three real idioms the same population uses. Published as written it would have
named three members instead of seven and read as complete, and every miss was found only by seeking
candidates the recognizer did NOT return. **A seed set therefore proves that a recognizer is not
broken and says nothing about what it covers**, which is precisely the *merely unfalsified* that
**#19** exists against.

**THE TEST IT RESTS ON IS FINDING F87**, which is what says WHICH recognizers F84 reaches, and it is
not seeds-versus-none. **Measured on three.** The derived gating answer a session reads at boot
reconciles both ways against the parsed INDEX, with a halt on any row it cannot place, and the INDEX
is enumerated by something other than that recognizer — **established, and F84 does not reach it**.
The epoch-pinned write-path enumeration has no external population, so its both-ways check runs
against an authored set the same session completed and catches only future drift, as its own artifact
concedes. The evidence-pin membership is **MIXED** — established on its population, which is an
external file-system enumeration, and unestablished on its classification, which is recognizers over
record text.

**THE TWO GENERAL FORMS, which are what outlive the instances:** *a recognizer's reach is measured by
the instances it FAILS to find, never by the ones it does*; and *establishment needs a SECOND,
INDEPENDENT enumeration of the same population.*

**★ THE BOUND, STATED HERE BECAUSE A READER WILL OTHERWISE TAKE THE CLAUSE FOR A SWEEP: IT BINDS A
RECOGNIZER WRITTEN OR TOUCHED FROM HERE. EXISTING RECOGNIZERS' OWN ARTIFACTS ARE NOT RETRO-FITTED
WITH THE STATEMENT.** The read-only sort ordered with this ruling carries the per-recognizer verdict,
so the information has ONE home (**#6**), and retro-fitting a population under the standing mechanism
freeze would be tool work that blocks nothing — the freeze's own test.

**THE COST THE USER ACCEPTED, recorded because an accepted cost is not a discharged one:** this
clause **CLASSIFIES** exposure and does not **MEASURE** it. A recognizer on the
no-external-population side is known to be a lower bound and is **not** known by how much. The
UNMEASURED declaration is what keeps that residual visible rather than closing it.

*What this rule does not do:* it edits, widens or acts on no recognizer, orders no re-establishment
pass, and grades no existing artifact. It says what a recognizer's own artifact must state about
itself, and nothing else.

### A maintenance act ESTABLISHES THE CAUSE before it touches the mechanism — and a cause that resists establishment is a STOP, with no fix taken on a named-but-unasserted candidate

**Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_eleventh_stop.md`, Ruling 52, taking
Ruling 50 of `cowork_rulings_2026_08_11_tenth_stop.md`). The two sections above say what a MECHANISM
is worth unmeasured and what a COMPLETENESS CLAIM is worth unmeasured. This says what an ACT owes
before it changes a mechanism at all, and it is sited here so that a reader meeting the fix order in
the guard-family rules below meets the diagnosis order first.

**THE ORDER, and the STOP is the half that binds.** Where a mechanism is failing, the maintenance
act that would repair it **establishes the cause AT THE OBJECTS first — before one line of the
mechanism moves.** Only with the cause established does the fix follow, under whatever order that
mechanism's own family discipline fixes for it. **A cause that resists establishment is a STOP back
to the user, and NO FIX IS TAKEN ON AN UNVERIFIED CANDIDATE** — not even one the record has already
named, and not even one that turns out to be right.

*Why the STOP is stated rather than left to #19:* **a named-but-unasserted candidate looks like a
diagnosis.** A row that names a plausible cause and honestly declines to assert it reads, one wave
later, as though the cause were known — so the fix gets taken on it, the mechanism changes, and the
symptom disappearing is then read as confirmation. That is the merely-unfalsified trust #19 refuses,
arriving by the one route that looks like diligence. The register carries the FIX half's order for
this family — corpus rows first, both rates re-measured on the same extended corpus, the revert
condition governing — and none of those entries says that the cause must be established first, or
what happens when it cannot be.

*The evidence that it earns its place, from the act that produced it:* the diagnosis was taken with
**no change to the tool at all** — the module was loaded twice from its own file by an ordinary
import from outside the repository, once under each spelling of the drive letter in that path, each
load applying the same equality test the mechanism applies to its own artifact. The row's own closing
clause had declined that diagnosis on the ground that it *"is a change to the tool"*, and it did not
have to be. **The general form is worth carrying: a tool can be DIAGNOSED without being EDITED, so
declining a diagnosis because it would edit the tool is a conclusion that deserves checking before it
is accepted.**

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

> **★ THE MANDATORY-ROW CLAUSE ABOVE IS SUPERSEDED FOR ONE CLASS — the findings the WORTH TEST
> DISCARDS (user-ruled 2026-08-11; the ruling record is
> `cowork_rulings_2026_08_11_sixteenth_stop.md`, Ruling 68).** The NO branch's *"The row is written,
> and the row is the whole of what is owed"*, and the closing paragraph's *"the row is mandatory"*,
> **no longer hold for a finding that fails the worth test principle #10 now carries**: such a
> finding is **recorded as DISCARDED and is not rowed**. **The test itself, what a discard record
> carries, and the two carve-outs are NOT restated here (#6)** — their one home is `CLAUDE.md`
> principle #10 (register entry **D-174**, whose verbatim is re-taken there).
>
> **R3 IS OTHERWISE UNTOUCHED, and the halves that stand are the ones a reader is most likely to
> think moved.** It still decides whether a finding is SURFACED or rowed; **D-438**'s test is still
> the sorting, unchanged; and **the #19 exception above is reinforced rather than weakened** — an
> establishment obligation is never discarded, whatever its subject, so it is rowed and surfaced
> exactly as before. What the supersession removes is the obligation to row a finding bearing on
> neither of the worth test's two consequences; it removes nothing from the YES branch, and the
> open-items register's rule (c) governs every finding that IS rowed exactly as before.
>
> *Why it is recorded here rather than only at the principle:* R3's own text states the mandatory
> row twice, in the NO branch and again in its closing *What it is NOT* paragraph, and a reader
> arriving at either would otherwise meet a demand the record no longer makes (#10). *Why it is
> placed at the section's end rather than beside the clause it supersedes:* the section is quoted
> whole as this decision's verbatim, and an amendment inserted into it would put 2026-08-11 text
> inside a decision ruled 2026-08-04 — so it takes the form the overtaking block at the end of the
> ordering-rule section below already uses.

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

### A homing act tests a section in a FIXED ORDER — pointer move first, kind half before any write — and a findings-recording owner means HELD, never written by stretch

**Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_tenth_stop.md`, Ruling 49, taking the
upgrade reading of Ruling 40 of `cowork_rulings_2026_08_09_eighth_stop.md`). Same family as the two
forms above, and the one they leave out: those say HOW to write a decision into a section that will
not take the plain form, and this says **in what order a homing act tests a section at all, and what
happens when the test fails.**

**THE ORDER, and it is an order rather than a set of considerations.**

1. **Where the owning section ALREADY STATES the entry's rule, the pointer moves and nothing is
   written.** The entry's home field moves to that section, its verbatim re-taken from that section's
   own text, every former field preserved (#12), zero text movement. **This step is tried FIRST and
   for every entry**, because a write that was not needed is a second statement of a homed rule (#6).
2. **Else, where the owning section STATES RULES, the rule is written there in that section's own
   voice**, with its defense, under whatever licence the act carries.
3. **Where the owning section RECORDS FINDINGS, the entry is HELD, with its row named.** Adding a
   rule-stating block to a findings table is a document-structure act, and it is reserved to the
   user.

**THE KIND HALF IS JUDGED PER SECTION AND BEFORE ANY WRITE**, with its evidence written down rather
than asserted — form first, kind second and last, which is the register's own precedence. **An entry
fitting none of the three steps is a STOP back to the user, never a judgment.**

*Why the order is load-bearing and not a description of good practice:* each step exists against a
different failure. Step 1 first, because the cheapest correct act is the one that moves no text, and
a session that starts at step 2 writes a rule that was already written. The kind half BEFORE the
write, because a section judged after the fact is judged by a reader who has already written into
it. And step 3 rather than a widened step 2, because the temptation at a findings table is exactly
to argue the table into a rule-stating section — the stretch that makes a mechanical test a matter
of taste.

*The evidence that it earns its place:* applied over one document's whole set, **step 1 closed
nothing**, with two near-misses recorded as checked-and-declined — a citation of a ratification by
date while stating something else, and a sentence stating a decision's FACT but not its CONSEQUENCE —
either of which a looser reading would have taken. **Step 3 then fired for four entries that turned
out not to be one shape**, and the user's own rulings on all four confirmed the STOP rather than
relaxing it: three needed no home at all, and the fourth closed by a write only because the user
MADE the general rule a session may not compose. A procedure whose STOP is confirmed by every case
it stopped on is not a formality.

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

### A task that CANNOT BE STOPPED PARTWAY is dispatched FIRST, with nothing large in front of it — and the ordering is RULED, never left to a preference

**Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_eleventh_stop.md`, Ruling 52, taking
Ruling 51 of `cowork_rulings_2026_08_11_tenth_stop.md`). Every other rule in this block says what a
dispatch may contain or how an act inside one is performed. This says in what ORDER the tasks of a
dispatch are placed, and it exists because two rules the project already runs on collide and nothing
said which wins.

**THE TWO RULES THAT COLLIDE.** One kind of task must be published over its WHOLE derived population
or not at all — a derivation covering some of its population reads as covering the class, which is
the cap nobody sees. The other kind, a per-entry pass, may be stopped at any member boundary,
because each completed member is whole in itself. **So the second kind can always absorb whatever
capacity is left and the first kind never can.**

**THE RULE.** Where a dispatch carries a task that cannot be stopped partway, **that task is placed
FIRST, with nothing large in front of it**, and the placement is recorded as a RULING rather than as
the dispatch-writer's preference.

*Why a ruling rather than a preference, which is the clause that binds:* a preference does not
survive one more capacity squeeze. The structural point is that such a task is **small in COUNT and
large in READING**, so every honest estimate of it looks cheap while every attempt at it loses to
work that can stop at a boundary — and each individual refusal is CORRECT on its own terms, which is
what makes the pattern invisible from inside any one dispatch.

*The evidence, measured rather than argued:* one such task was declined by **seven consecutive
dispatches**, every refusal right on its own terms and for the same reason each time. Dispatched
first under this rule, with nothing large in front of it, it closed WHOLE in one act — and turned up
a finding nobody was looking for while deriving its own population. **The ordering was the whole
difference, and nothing about the task had changed.**

**Siting note, recorded rather than smoothed over.** The proposed home named this block *beside the
two rules it arbitrates between*. Those two are not subsections of this block, or of any governing
surface: they live in dispatch prose and in session records, which is itself one reason nothing ever
stated what happens when they meet. The entry is therefore sited in the block the ruling names, at
its end, and the two rules are stated above in the terms this rule needs them in — not homed here,
because homing them is a separate act nobody has ruled.

> **★ THE CLOSING CLAUSE ABOVE IS OVERTAKEN, AND THE FORMER WORDING STANDS (#12; corrected
> 2026-08-11 on the user's Ruling 55 of `cowork_rulings_2026_08_11_twelfth_stop.md`).** *"Homing them
> is a separate act nobody has ruled"* was true when it was written and is no longer: the user ruled
> that act one stop later, and **both rules are now homed in the two subsections immediately below**,
> in this block's own voice. Nothing in the rule above moves; what changes is that the two rules it
> arbitrates between are governed text rather than dispatch prose, which is what made the arbitration
> readable only through this entry.

### A derivation, a measurement or a sizing over a derived population is published WHOLE or not at all — and a subset is published only under a scope that NAMES its members

**Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_twelfth_stop.md`, Ruling 55), which
homes a rule this project had been running on since the fourth return continuation without any
governing surface stating it. The rule above arbitrates between this rule and the one below; until
this act neither of the two was written anywhere a session would find them.

**THE RULE, in two halves.** **(a)** Where a task's deliverable is ONE derivation, ONE measurement or
ONE sizing over a DERIVED population, it is published over the whole of that population or it is not
opened at all. **(b)** Where a subset is nonetheless published — because the whole is not reachable
and the finding is worth having — it is published **under a scope that names its members
individually**, in the same surface that carries it, so that no reader can take it for the whole.

*Why (a) is a rule and not a preference:* a derivation covering some of its population **reads as
covering the class**. The failure is silent by construction — the surface looks complete, every
value in it is correct, and nothing in it says what was left out — so the reader is not merely
under-informed, they are informed wrongly and have no way to notice. That is the defect this
project's establishment rules exist against, and it is why *opened and left part-done* is worse than
*not opened*, which reverses the ordinary presumption about partial progress.

*Why (b) rather than a flat prohibition:* a subset whose members are NAMED cannot be mistaken for the
whole, so the silent half of the failure is removed and the finding is kept. The two published
subsets on the record are exactly this shape — a sizing delivered over the rows one batch had read,
with those rows named one by one and the shortfall stated in the heading that carried them.

*The evidence, measured rather than argued:* one derivation was declined by seven consecutive
dispatches, each refusal citing this rule and each correct on its own terms; when it finally ran
under the ordering rule above it closed whole in one act. **A rule that produces seven correct
refusals in a row is doing its job**, and the cost of those refusals is what the ordering rule exists
to pay rather than an argument against this one.

**What it does NOT reach.** A per-entry pass, which is the subject of the rule immediately below: its
members are complete in themselves, so stopping inside one publishes nothing partial. And a
deliberately bounded population — a derivation whose OWN declared scope is a subset — is not a
partial publication of a larger one, provided the boundary is declared where the artifact is read.

### A PER-ENTRY PASS may be stopped at any member boundary, and the stop is RECORDED — what was done, what was not, and that the remainder is untouched rather than partly worked

**Ruled by the user, 2026-08-11** (`cowork_rulings_2026_08_11_twelfth_stop.md`, Ruling 55), the
second of the two rules the ordering rule above arbitrates between, and homed in the same act for the
same reason: it governed every batch of this arc from dispatch prose alone.

**THE RULE.** A task whose deliverable is a per-entry, per-row or per-site PASS may be stopped at any
**member boundary** — on capacity, or because a later task binds harder — and the stop is not a
failure. **Three things are recorded when it happens:** which members were completed, that the
remainder is UNTOUCHED rather than partly worked, and that nothing is left half-edited. A stop
recorded that way is a result; a stop that is silent is the defect the rule above names.

*Why the allowance is safe here and nowhere else:* each completed member is **whole in itself**. A
homed entry, a corrected row, a re-aimed anchor — each stands alone and is not made wrong by the next
one never happening, so a stopped pass publishes nothing that reads as more than it is. That is
exactly the property a derivation over a population does not have, which is why the two rules are
different rules rather than one.

*Why the recording clause is the load-bearing half:* an unrecorded stop turns a per-entry pass into
the very thing the rule above forbids — a reader meets a list of completed members and cannot tell a
finished pass from an interrupted one. **The remainder is therefore derived fresh by the continuing
session and never carried from the stopping session's account of it**, which is the standing form this
arc has used at every such stop.

**What it does NOT license.** Leaving a member half-edited; a stop inside a task the rule above
governs; and a stop presented as completion. Nor does it decide WHICH task stops — that is the
ordering rule above, which places the unstoppable task first precisely so that the stoppable one is
what absorbs the shortfall.
