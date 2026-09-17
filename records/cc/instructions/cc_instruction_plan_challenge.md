# CC dispatch — CHALLENGE the specification-reconstruction plan; refute it, do not assess it

> **Dispatch (Cowork, 2026-08-19). Written at a verified stop; nothing else is running and no dispatch
> was active when this was written.**
>
> **★ THIS DISPATCH ORDERS A REVIEW, NOT THE WORK THE PLAN DESCRIBES.** Nothing in the plan is
> executed. No specification is written, no frame is built, no derivation is run. **The plan is NOT
> ratified and must not be treated as authority for anything.**
>
> **★ THE BRIEF IS TO REFUTE.** The plan's §15 states ten load-bearing assumptions, each with what
> would refute it. **A report concluding that the plan looks sound is a FAILED report.** Where an
> assumption survives, the report states **what was checked** that could have refuted it and did not —
> a survival with no attempted refutation behind it is not a survival.
>
> **★ READ FIRST.** **(1)** `CLAUDE.md` and `STATUS.md` as they now stand, in full. **(2)**
> `DECISIONS.md` — unconditional. **(3)** `BUILD_AND_TEST.md` — CONDITIONAL, and **this batch does NOT
> meet the condition**: it runs no build, no test and no measurement tool. **(4) DO NOT READ THE WHOLE
> OPEN-ITEMS INDEX.** Rule (a) reads the derived gating answer narrowed to its identity list.
> **(5)** `cowork_handoff.md`, **its current (THIRTY-THIRD) block**. **(6)**
> `cowork_audit_protocol.md`'s dispatch-protocol section — read the sections carrying the membership
> marker; the number is retired and is not restated here.
>
> **Then, in full: `cowork_specification_reconstruction_plan_v4_2026_08_19.md`** — the subject of this
> dispatch, on disk and untracked. Its §15 is the whole of Task 1.
>
> **The standing bars bind this batch whole:** no `src/` edit, no golden, no test changed, moved or
> run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis built,
> designed, scoped or run, no design, no repair, no mining, no document archived, moved or deleted AS A
> FILE, **no open-items row created, flipped or discarded**, and **no specification text written or
> edited**. **Reading source code is permitted and expected. Running anything is not.**

## Premise ledger

- **FACT** — the fourteenth batch is complete and pushed; the terminus is `891bacc5d2`, verified at the
  objects by the writing side, every parent confirmed and every path count read from the object.
- **FACT** — `OPEN_ITEMS.md` (`6ae67d8603`) and `tools/audit/nongating_apparatus_rows.json`
  (`5bb43d0b3a`) are byte-identical at every commit of that batch. **Nothing this batch does may move
  either.**
- **FACT, measured by the writing side** — no artifact under `tools/audit/` takes the provenance of
  `ARCHITECTURE.md` or `docs/scoring_model.md` as its subject.
- **ASSUMPTION A1** — the working tree carries the four untracked plan and boot-list files this
  sitting wrote and no tracked modification. **Check ordered as the first act, at content-addressed
  objects, under the F57 caveat.** A tracked modification at any path is a STOP-and-report.

## Task 1 — REFUTE the ten assumptions of the plan's §15

For **each** of L1 through L10, return one of exactly three verdicts, and no fourth:

- **REFUTED** — with the evidence, cited to the object, the file or the code site that refutes it.
- **SURVIVES** — with **what was checked that could have refuted it and did not.** A bare "seems fine"
  is not a verdict and is reported as CANNOT DECIDE.
- **CANNOT DECIDE** — with what would be needed to decide, and why it was not available.

**Two of the ten are worth disproportionate effort and are named so they are not levelled with the
rest:**

**L2** — that a specification statement can carry a code-falsifiable condition. If it falls, every
statement the programme would produce is undeltaable and the work is wasted at its last step. **Task 2
supplies the material.**

**L3** — that the problem is separable per section at all. The production layer is a **joint** estimator
precisely because key and chord are mutually determining. **Read the joint estimator's standing rules in
`ARCHITECTURE.md` and answer at the text: can those rules be stated as independent per-section statements
without loss?** If they cannot, the plan's unit of work is wrong and that is the largest possible return
of this dispatch.

**Registered expectation E1:** ten verdicts, one per assumption, each from the closed set of three, each
carrying either its refuting evidence or what was checked; L2 and L3 answered at the code and at the
text rather than by argument.

## Task 2 — judge the statement format from the DELTA side

Below are **five statements written by Cowork purely as format probes.** They are **NOT proposed
specification content**, they are **not ratified**, and nothing may be implemented, corrected or filed
from them. They exist to test one question: **is field five sufficient?**

> **S1 — boundary rule.** *Statement:* a harmony boundary is placed at every onset introducing a pitch
> class outside the currently committed harmony, unless that pitch class is metrically weak and resolves
> by step within the same beat. *Defense:* non-chord-tone treatment in common-practice theory; the
> metric-weakness clause is owed a measurement. *Source class:* derived. *Status:* open. *Falsified in
> code by:* the boundary-proposal site tests neither metric weight nor stepwise resolution.
>
> **S2 — knowledge item.** *Statement:* the analysis consults a store of common progressions of the
> target repertoire, and that store is data rather than code. *Defense:* corpus-derived progression
> frequency is measurable and is not a design choice. *Source class:* derived. *Status:* open.
> *Falsified in code by:* no such store is read at analysis time, or it exists only as literals in source.
>
> **S3 — enablement constraint.** *Statement:* every derived harmonic fact is published on its producing
> layer's output surface even where no consumer reads it, carrying its establishment status. *Defense:*
> the fact-publication corollary of `CLAUDE.md`, ratified 2026-07-10 and amended 2026-07-12. *Source
> class:* salvaged. *Status:* settled. *Falsified in code by:* a derived fact exists that no layer surface
> publishes, or one published without a status field.
>
> **S4 — numeric threshold.** *Statement:* a chord candidate is admitted to scoring only when at least
> three of its chord tones sound. *Defense:* **none — this is a bare value and is marked UNSUPPORTED.**
> *Source class:* derived. *Status:* open. *Falsified in code by:* the admission test uses a different
> count, or none.
>
> **S5 — abstention rule.** *Statement:* where two readings differ in root and their scores lie within
> the measured noise, the analysis abstains on the root axis rather than committing. *Defense:* correct
> abstention is a right outcome and the hard stop is abstain-aware. *Source class:* derived. *Status:*
> open. *Falsified in code by:* there is no abstention path on the root axis at all.

**For each of the five, answer:** could you return **conforms / diverges / not implemented / present in
code but in no statement** from field five **alone, without interpretation**? Where the answer is no,
say **what field five would have to carry instead**.

**Registered expectation E2:** a per-statement verdict on field five's sufficiency, and — where any fails
— a concrete replacement form, proposed from the delta side by the party that would run the delta.

## Task 3 — judge the feasibility of A4, A5 and the budget

**Do not run them.** Judge whether they can be run, and at what cost.

1. **Can you enumerate the decisions the implementation actually makes**, as a population a frame can be
   reconciled against both ways? Say how, and what it would cost.
2. **Can you enumerate the fields of the ground-truth annotation schema** from the corpus data?
3. **Can you cluster the failing runs by which decision they turn on** — and, bearing on **L4**, what
   share would you expect to be multi-causal and therefore unattributable to one section?
4. **Is A5's sample of 60 statements the right size** to detect a missing axis, and is the STOP threshold
   of more than ten unplaceable defensible or arbitrary?
5. **Is the Phase-A budget of three working sessions realistic**, given A3 walks the deletion history of
   every document in the A1 set? This is **L8**'s own subject; answer it with a measurement of that
   history if one is cheaply available, and say so if it is not.
6. **Are the plan's eleven guardrails checkable from the executing side**, and which of them would you be
   unable to comply with or to detect a breach of?

**Registered expectation E3:** six answers, each stating whether the thing is feasible, at what cost, and
what would make it infeasible.

## Task 4 — the report, and nothing else

One file, `cc_report_plan_challenge.md`, carrying Tasks 1–3, the declared departures, and the standing
self-check over this session's own reading. **One commit, that file alone.**

**★ NO OTHER TREE CHANGE.** No `STATUS.md` entry, no close in `cowork_away_returns.md`, no handover block,
no chain table, no correction commit about a correction. **The report is both the deliverable and the
record** — the plan's guardrail 8 applied to the dispatch that challenges it.

**Registered expectation E4:** exactly one commit, exactly one path, and the guard set unmoved because
nothing this batch does touches it.

## What this batch does NOT do

- **No specification text is written, derived, corrected or filed.** The plan is not ratified.
- **No frame is built**, no document set derived, no section enumerated, no history walked except where
  Task 3.5 needs one cheap measurement of its size.
- **No measurement tool is built, designed, scoped or run**; no build, no test, no guard run.
- **No finding number is allocated** — findings from this review belong in the report, and the writing
  side numbers anything that deserves it at the return sitting.
- **No open-items row is created, flipped or discarded.** [[OI-372]] and [[OI-374]] stay exactly as
  found; [[OI-179]] stays OPEN and GATES.
- **No pin is taken**, no candidacy acted on, no census re-pin, no archiving.
- **Nothing in `docs/` or `ARCHITECTURE.md` is edited**, however plainly wrong it is found to be —
  a finding is reported, never corrected here.

---

*Provenance: Cowork, 2026-08-19, written at branch tip `891bacc5d2`. The subject plan and its three
withdrawn predecessors are on disk and untracked. The reserved-word conventions bind this dispatch, and
the vocabulary rule of 2026-08-17 binds every line of the report it orders — TOWARDS the ultimate
objective and TOWARDS the guiding principles.*
