# CC DISPATCH — ENUMERATE, DRAW, SEAL AND COMMIT THE PLACEMENT SAMPLE

*Written by the Cowork writing side, 2026-08-27, against tip
`0e7186a961f50b32e0552483b289b11069f1319a`. Executes Rulings 1, 2 and 3 of
`cowork_rulings_2026_08_27_placement_sample_sitting.md`. This batch performs NO ratification, orders
NO register entry, MAKES NO ADMISSION, and **DOES NOT RUN THE PLACEMENT TEST** — the frame it would
be run against does not exist yet.*

---

## 0. What this batch is, and the one property that governs every instruction below

The framework phase's third act is a **placement test**: statements taken from outside the frame
are each placed into the finished frame, and every statement that fits nowhere is a finding about
the frame. **You will run that test later, in a different dispatch.** This batch produces the set of
statements you will be given — the **placement sample** — and closes it.

**★ THE PROPERTY THAT GOVERNS EVERYTHING: YOU ARE NOT PERMITTED TO CHOOSE WHAT GOES INTO THIS
SAMPLE.** Ruling 1 of 2026-08-26 made you the side that runs the placement test. If you also chose
the sample, the side being tested would be picking its own examination questions. So the selection
rule is written out below **by the writing side, before any count was known**, and it is
deterministic: given the enumeration, exactly one sample follows. **Where the rule does not decide
something, you STOP and report. You never decide it.**

**The seal.** The drawn set must be closed before the frame's author begins. Committing the file is
the seal — an object at a named tip with a date that cannot be re-argued.

---

## Task 0 — start state and landings

**(a)** Read `.git/refs/heads/master` with the file tool. It must read
`0e7186a961f50b32e0552483b289b11069f1319a`. **If it does not, STOP and report.** Name the side
measured wherever you state a hash.

**(b) Do NOT run `git status`** (D-253). Run `python tools/audit/changed_paths.py`; record the
population; commit none of the standing untracked population beyond what (c) names.

**(c) Land, in one commit**, these seven paths:

- `cowork_handoff.md` — **TRACKED-MODIFIED.** It carries the sixty-eighth entry from 2026-08-26 and
  a sixty-ninth entry added 2026-08-27, **additions only, prepended, no earlier entry reworded**.
  **Establish that before committing:** compare the working tree against the blob at the tip and
  report what differs.
- `cowork_framework_phase_opening_surface_2026_08_26.md` — untracked
- `cowork_rulings_2026_08_26_framework_opening_sitting.md` — untracked
- `cowork_literature_reachability_2026_08_26.md` — untracked
- `cowork_placement_sample_surface_2026_08_27.md` — untracked
- `cowork_rulings_2026_08_27_placement_sample_sitting.md` — untracked
- this dispatch

Then `python tools/audit/gen_evidence_pin_membership.py`.

---

## Task 1 — establish each stratum's population at its object, and quote what you rely on

The sample is drawn from **eight strata**, ruled at `cowork_rulings_2026_08_26_framework_opening_sitting.md`
§3 and standing at `cowork_specification_reconstruction_plan_successor_2026_08_21.md` §6.2:

1. ruling records
2. decision surfaces
3. dossiers
4. the **DEFERRED** entries of the decisions register
5. the evidence inventory
6. the declared dormancies
7. every current document heading
8. every heading ever deleted from the document set

**For each stratum, before enumerating anything, establish what it denotes at the objects and quote
the text you rely on.** Name the defining object — a directory, a generated membership artifact, a
register field, a filename convention. The writing side has deliberately not guessed at these:
naming them from a dispatch rather than from the repository is how this project has previously
written an instruction too narrow.

**The enumeration unit, which IS declared here because it is a selection choice and therefore not
yours:**

| Stratum | One item is |
|---|---|
| 1 ruling records | one numbered ruling in a ruling record |
| 2 decision surfaces | one numbered decision in a decision surface |
| 3 dossiers | one claim or finding entry in a dossier |
| 4 deferred register entries | one register entry whose status is DEFERRED |
| 5 evidence inventory | one inventory row |
| 6 declared dormancies | one declared dormancy |
| 7 current headings | one markdown heading in a current member of the document set |
| 8 deleted headings | one markdown heading present in an earlier commit of a document-set member and absent at the tip |

**★ STOP CONDITION, PER STRATUM AND NOT FOR THE WHOLE BATCH.** If a stratum's membership is **not
determinable from a named object** — there is no defining artifact, or two candidate objects
disagree — **do not invent a definition and do not pick between them.** Record that stratum as
**STOPPED**, with what you found and what is missing, and carry on with the others.

**A stratum that enumerates to ZERO is not a stop.** Record `N = 0` and say so in terms. An empty
stratum is a finding about this project's records, and it must be visible rather than absent.

---

## Task 2 — apply the selection rule exactly as written

### 2.1 The ordering — deterministic, and no other ordering is permitted

Within each stratum, order the enumerated items by this tuple, ascending:

1. the repository-relative path of the file the item is found in, by byte order;
2. then the line number at which the item begins;
3. then, **for stratum 8 only**, the hash of the commit that deleted the heading, lexicographically.

**Do not order by importance, recency, topic, length or interest.** If two items tie on all three
keys, STOP and report — that means the enumeration unit is ambiguous and the writing side must fix
it, not you.

### 2.2 The threshold and the take

Let `N` be a stratum's enumerated count and `T = 25`.

- **If `N ≤ T`: the stratum goes in WHOLE.** Census, no sampling, no uncertainty range needed.
- **If `N > T`: the stratum contributes exactly `T = 25` items**, taken systematically from the
  ordering of §2.1: let `k = floor(N / T)`; take the items at 1-indexed ordered positions
  `1, 1+k, 1+2k, …, 1+24k`.

**★ `T = 25` IS DECLARED, NOT DERIVED, AND YOU MUST WRITE IT DOWN THAT WAY WHEREVER IT APPEARS.** No
measurement in this project supports it. Its stated ground: the predecessors' whole placement test
placed sixty statements across all sources, so twenty-five per stratum gives each stratum on its own
more than a third of what the entire test formerly had, and caps this one at two hundred items
across eight strata. Ruling 2 of 2026-08-27 requires the threshold and take-rate be declared before
the counts are known; they were. **A successor citing 25 as a measured figure has misread it.**

**The cap is why there is no unpayable-take case.** A stratum of forty and a stratum of ten thousand
both contribute twenty-five. What a very large stratum costs instead is a **wide uncertainty range**
on its proportion, and that range — required by Ruling 3 of 2026-08-26 — is reported, never glossed.

---

## Task 3 — write the sealed sample

**Path: `cowork_placement_sample_sealed_2026_08_27.md` at the repository root.** Chosen by the
writing side on the existing root convention for `cowork_*` records; it is not ruled and the user
may rename it in one line.

**★ THE BANNER MUST CARRY, IN THIS ORDER AND WHERE IT CANNOT BE MISSED:**

1. **DO NOT READ IF YOU ARE AUTHORING THE FRAME.** This file is withheld from the frame's author,
   alongside the code. Ruling 3 of 2026-08-27.
2. That this is the **sealed** placement sample, drawn at tip
   `0e7186a961f50b32e0552483b289b11069f1319a`, and that it is closed.
3. That `T = 25` is **declared, not derived**.
4. **Any STOPPED stratum, named**, with what was missing — and that **the frame is not authored
   until the user has ruled on every stopped stratum.** That gate is Ruling 3 of 2026-08-26 read
   plainly: a sample missing a stratum nobody ruled on is not sealed, it is incomplete.

**Per stratum, the body carries:** the defining object and the quoted text establishing it; `N`;
whether it was a census or a take; `k` where one applied; and the drawn items — each with its
**verbatim text** and its `path:line` provenance. A statement that must be interpreted before it can
be placed is not a statement; if an item cannot be rendered verbatim, record it and say so rather
than paraphrasing it into shape.

**What this file does NOT carry:** any judgement about whether an item is placeable, any grouping by
topic, any commentary on the frame, any ranking. It is a list.

---

## Task 4 — the root-population hazard, checked BEFORE the sealed file is written

`gen_filing_convention_application.py` derives its candidate population over the repository root's
`*.md` files, and it is the guard behind the one standing DECISION red, `[[OI-372]]`, whose
candidate list is currently exactly three. **This batch adds root-level `.md` files, so it can in
principle widen a red it is forbidden to cure.**

**Read that tool's candidate derivation and report, before writing the sealed file, whether
`cowork_placement_sample_sealed_2026_08_27.md` and this batch's report will enter it.** Then run the
sweep with both on disk and report the candidate list.

**If the list widens: report it prominently, do NOT classify it, do NOT cure it, and do NOT
regenerate the guard.** The batch still completes — the sealed sample is the deliverable — but the
widening is a consequence the writing side must see.

**★ AND DO NOT SHAPE EITHER FILE TO STAY OUT OF THAT POPULATION.** A previous report's absence from
the candidate list was engineered by keeping hashes out of its tail, which silently voided every
*"the list did not widen"* result taken from it. Write both files as their content requires and let
the guard say what it says.

---

## Task 5 — `STATUS.md`, the forward bound, the sweep, the report, the commit

**(a)** One **POINTER** entry in `STATUS.md` (OI-222 remedy; **D-431**: no count, no identity, no
rendered value). **Write it BEFORE running the forward-bound tool** — the reverse order makes the
tool's occurrence test find zero and STOP.

**(b)** Re-aim `tools/audit/gen_status_batch_bound.py` — the **five** aiming constants, and
**append** the outgoing aiming to `PREVIOUS_AIMINGS` rather than overwriting it (#12); both are
inside the named carve-out. Read the tool's own parser for the flag; report the exact command line
and the values set. **`TASK` is a choice — declare which task number you used and why.**

**(c) The sweep**, as ruled: `gen_guard_state.py`, then `gen_guard_classification.py`, in that
order. Three reds are standing and are **not yours to cure**: `[[OI-372]]`'s guard,
`apply_soft_discard.py --check`, `apply_residue_discard.py --check`. A staleness red caused by this
batch's own writes is cured under the standing sweep rule. **For any other red: if you cannot tell
whether it is a decision red or a regeneration red, treat it as a DECISION red and STOP.**

**(d)** Write `cc_report_placement_sample.md` at the root, then commit. State separately: the Task
0(c) establishment of the modified handoff; **for each of the eight strata, its defining object with
your quotation, its `N`, census-or-take, and `k`**; every STOPPED stratum; whether the root
population widened; every path written; and **every departure and every instruction you could not
obey.**

---

## §6 THE FENCE

Writes permitted at **exactly** these paths:

- `cowork_placement_sample_sealed_2026_08_27.md` — new
- `cc_report_placement_sample.md` — new
- `STATUS.md` — one pointer entry
- `tools/audit/gen_status_batch_bound.py` — the five aiming constants and the appended row, carve-out
- the seven Task 0(c) landings and `tools/audit/evidence_pin_membership.json`
- **any file a tool this dispatch orders you to run writes as its own output.** Name each in the report.

**Explicitly forbidden.** **No frame text authored, no part of the frame written, no statement
placed, no judgement about placeability recorded** — the placement test is a later dispatch and this
one has no frame to run it against. No `CLAUDE.md`, `ARCHITECTURE.md` or `DECISIONS.md` edit. **No
register entry** — this batch performs no ratification, so rule (c) is not engaged and the two
mutually unsatisfiable discard-act checks stay out of its path. *(That is again a batch shaped to
route around the register blocker rather than to cure it. It is recorded here, not hidden; curing it
is a decision act that has never been put to the user.)* No item added to, removed from or reordered
in the sample except by the rule at Task 2. No existing ruling record, surface, dossier, register
entry or inventory row edited — **you are reading these, not maintaining them.** No `src/` change,
no test changed, moved or run, no golden. Nothing under `tools/corpus/` or `tools/robust_stop/`. No
open-items row created, flipped or discarded. No finding number allocated. Neither blind output
opened. Neither pack, the generator, the manifest or any withheld family touched. No other `.py`
source edited. Do not cure the two discard-act checks; do not regenerate `[[OI-372]]`.

**★ THE STANDING CLAUSE.** **If obeying any instruction here would require a write outside this
fence, STOP and report the conflict. Do not choose a route, do not widen the fence, and do not
substitute a weaker form of the instruction to stay inside it.** Stopping and reporting is the
correct outcome.
