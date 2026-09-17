# CC dispatch — EVALUATE the specification-reconstruction plan on its merits, under the neutral brief

> **Dispatch (Cowork, 2026-08-21). Written at a verified stop; nothing else is running and no
> dispatch was active when this was written.** Authority: `cowork_rulings_2026_08_21_evaluation_brief_sitting.md`
> (Rulings 1–4) — **which you do NOT read**; it is named here only so the record is checkable by
> a later reader, and it is excluded from your inputs by the boot list below.
>
> **★ THIS DISPATCH ORDERS AN EVALUATION, NOT THE WORK THE PLAN DESCRIBES.** Nothing in the plan is
> executed. No specification is written, no frame is built, no derivation is run. **The plan is NOT
> ratified and must not be treated as authority for anything — and neither is any verdict anyone
> has previously recorded about it.**
>
> **★ YOUR BRIEF IS `cowork_plan_evaluation_brief_2026_08_21.md`, READ WHOLE AND FIRST.** It is
> dispatched to you verbatim and to a second, independent evaluator verbatim; neither of you sees
> the other's answer. **A positive finding is a real finding. An all-negative return is an
> incomplete evaluation** (the brief, §4.2).
>
> **★ READ-FIRST BLOCK — AND A RULED DEPARTURE, STATED IN TERMS.** This dispatch departs from the
> standing clause *"Every dispatch's read-first block names the CURRENT HANDOVER BLOCK of
> `cowork_handoff.md`"* (`cowork_audit_protocol.md`, dispatch-protocol section). **You do NOT read
> `cowork_handoff.md` — any block — in this batch.** Ground, ruled by the user 2026-08-21 (Ruling 2
> of the sitting record named above): that block states a prior verdict on the object you are
> evaluating, which the brief's §2 requires you to be blind to; and the clause's own recorded
> ground — finding F58, a finding-number collision — is not engaged, because this batch allocates no
> finding number (the brief, §7). The departure reaches this one dispatch and amends nothing.
>
> **Your reads, in order, are the ones `cowork_evaluation_boot_list_2026_08_21.md` names, in the
> order it names them, and its DO-NOT-READ list binds you.** In summary and not in place of it:
> the brief; the object — the four plan versions v1, v2, v3, v4 in that order, then the curated
> boot-list draft; then `CLAUDE.md` in full, `DECISIONS.md` in full, the phase-definition surface,
> its sitting record (§6 above all), the method-directions record, and the derived gating answer
> narrowed to `gating_ids`; then the primary sources as your judgment requires. `STATUS.md` may be
> read; its newest entries carry no verdict on the plan. `BUILD_AND_TEST.md` is CONDITIONAL and the
> condition is not met. **`cowork_audit_protocol.md`'s dispatch-protocol section is read for the
> marked standing clauses** — they bind your report's form (citation, figures, self-check) and they
> carry no verdict on the plan.
>
> **The standing bars bind this batch whole:** no `src/` edit, no golden, no test changed, moved or
> run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis built,
> designed, scoped or run, no design, no repair, no mining, no document archived, moved or deleted
> AS A FILE, **no open-items row created, flipped or discarded**, **no specification text written or
> edited**, **no finding number allocated**. **Reading source code is permitted and expected.
> Running anything is not.** The lineage the brief's §1 asks you to read is the four plan FILES on
> disk, v1 to v4; **no git history is needed for it and none is read, and the commit LOG of the
> branch tip is not read** — see A1.

## Premise ledger

- **FACT** — the branch tip is `7d7a0e76f7`, parent `891bacc5d2`; `origin/master` stands at
  `891bacc5d2`. Read by the writing side at the live tree on 2026-08-21. **The tip commit's own
  subject line states a prior verdict on the plan; that is why A1 is checked by HASH and never by
  `git log`.**
- **FACT** — the fourteenth batch's invariants: `OPEN_ITEMS.md` at blob `6ae67d8603` and
  `tools/audit/nongating_apparatus_rows.json` at blob `5bb43d0b3a`, byte-identical at every commit
  of that batch, verified at the objects by the writing side. **Nothing this batch does may move
  either.**
- **FACT** — [[OI-179]] is in `gating_ids` on 2026-08-21; read at the staged artifact by the
  writing side.
- **ASSUMPTION A1 — the working tree you meet.** `git rev-parse HEAD` returns `7d7a0e76f7…` (compare
  the hash and nothing else; do not run `git log`). On disk and UNTRACKED: the brief, the boot list,
  `cowork_review_findings_prediction_2026_08_21.md` (sealed — do not open),
  `cowork_rulings_2026_08_21_evaluation_brief_sitting.md` (do not open), this dispatch, the four
  plan versions, `cowork_curated_boot_list_draft_2026_08_19.md`, `cc_instruction_plan_challenge.md`
  (do not open) — and the rest of the untracked population as the tree carries it: newly visible
  `cc_instruction_*.md`, `cc_*_report.md` and `cc_*_dossier.md` files and a scratch directory.
  `cowork_handoff.md` is MODIFIED against its blob (a new block and one heading marker); you do
  not open it. **Check ordered as the first act:** the hash comparison above, and that each file
  the boot list orders you to READ exists at its path. **The whole-tree enumeration is NOT ordered**
  — `git status` is measured to time out on this mount — so a tracked modification outside the
  named files is not a STOP here; it is reported if met. The F57 caveat applies to any byte
  comparison you make: the tree stores text in both line-ending conventions; compare through git
  or normalise first.

## Task 1 — the evaluation, as the brief orders it

Produce everything the brief's §4 and §5 require, in its form: every finding labelled MERIT or
CONFORMANCE and never both; KEPT / REPAIRED / DROPPED / MISSING / CANNOT ESTABLISH, each with cited
grounds; the counterfactual of §5 written separately and derived from the objective, not from the
plan. The brief's §3 puts the standing rules in scope: where a rule does not serve the objective,
say so with grounds and name the replacement — and establish the CURRENT generation of any rule you
rely on at its ruling record before relying on it.

**Registered expectation E1:** a report in the brief's §4/§5 shape, both polarities present, every
verdict cited `file:line` to a primary source, every figure by citation to a generated artifact,
every comparison carrying its uncertainty.

## Task 2 — the independence record

State, in the report, every file you opened; every file on the boot list's DO-NOT-READ list you
did not open; and, per the brief's §2 and the boot list's §2, any prior verdict on the plan you
met anywhere — where, and how much of it you saw before you stopped. **A report with no
independence record is incomplete.**

**Registered expectation E2:** the independence record present, and the four excluded files
recorded as unopened — or, where one was met, recorded as met with its extent.

## Task 3 — the report, and nothing else

One file, `cc_report_plan_evaluation.md`, carrying Tasks 1–2, the declared departures, and the
standing self-check over this session's own reading. **One commit, that file alone.** **The commit
subject carries NO verdict** — use exactly: `evaluation: the specification-reconstruction plan
evaluated under the neutral brief; report at cc_report_plan_evaluation.md`. *Why:* the second
evaluator is told the tip hash and takes no branch rule, but a later reader who runs `git log`
must not meet your verdict in a subject line, which is how the first review's verdict reached a
session that had not read the review.

**★ NO OTHER TREE CHANGE.** No `STATUS.md` entry, no close in `cowork_away_returns.md`, no handover
block, no chain table, no correction commit. **The report is both the deliverable and the record.**
**Do not push** — the writing side pushes after both evaluations have returned.

**Registered expectation E3:** exactly one commit on `7d7a0e76f7`, exactly one path, the guard set
unmoved because nothing this batch does touches it.

## What this batch does NOT do

- No specification text is written, derived, corrected or filed. The plan is not ratified.
- No frame is built, no document set derived, no history walked.
- No measurement tool is built, designed, scoped or run; no build, no test, no guard run.
- No finding number is allocated.
- No open-items row is created, flipped or discarded. [[OI-372]] and [[OI-374]] stay as found;
  [[OI-179]] stays OPEN and GATES.
- No pin, no candidacy, no census re-pin, no archiving, no push.
- Nothing in `docs/` or `ARCHITECTURE.md` is edited, however plainly wrong it is found to be — a
  finding is reported, never corrected here.

## The writing side's self-check over this dispatch (recorded, per the standing clause)

1. *Principles touched:* #17(b) — a prediction is registered and sealed before this runs; #19 —
   nothing previously asserted about the plan enters as established; #12 — nothing is deleted or
   rewritten; #24 — every comparison in the report must carry its uncertainty. Conforms.
2. *Conventions:* American English; no invented labels; music-theory words in their musical sense —
   *score* is not used in the numerical sense anywhere above; *measurement tool*, never the
   reserved word.
3. *Figures and premises:* no quantity is transcribed; the hashes are object names, not figures;
   the one count in the premise ledger (the gating answer) is cited to its artifact and field.
4. *File-tools rule:* the writing side's own departures are declared in the thirty-sixth handover
   block, not here; the executing side is bound by the rule as stated in `CLAUDE.md` Conventions.
5. *Uncertainty:* no comparison between measured quantities is asserted in this dispatch.

---

*Provenance: Cowork, 2026-08-21, written at branch tip `7d7a0e76f7` under Rulings 1–4 of the
2026-08-21 evaluation-brief sitting. The reserved-word conventions bind this dispatch, and the
vocabulary rule of 2026-08-17 binds every line of the report it orders — TOWARDS the ultimate
objective and TOWARDS the guiding principles.*
