# CC REPORT — the defense-share sizing, 2026-09-08 — ★★ **STOPPED AT TASK 0(a). NOTHING WAS COMMITTED, NO TOOL WAS BUILT, NO GUARD WAS RUN.**

**WHAT THIS IS.** The report `cc_instruction_defense_share_sizing_2026_09_08.md` Task 2(e) orders,
written early because the dispatch's FIRST task hit a declared STOP condition and its own words are
*report it and do not proceed*.

**THE ONE-LINE ANSWER.** The tree carries a tracked modification —
`cowork_handoff_entry_one_hundred_and_forty_seven.md` — where Task 0(a) expects none. Two of the
dispatch's own STOP conditions fire on the same fact. **Task 0(b), Task 0(c), Task 1 and Task 2 were
not begun.** The two premises the dispatch declared unestablished were checked anyway, because it
orders their answers *either way*, and both are answered below.

---

## 1. THE STOP, AND THE EVIDENCE FOR IT

**The dispatch's words, verbatim, at Task 0(a):** *"**Expected: zero tracked modifications**, with the
untracked files of (c) present among the untracked records. **A tracked modification is a STOP —
report it and do not proceed.**"* Its STOP-conditions list repeats it as *"Any tracked modification at
Task 0(a)"*, and adds *"Any instruction here that you find to be false at the objects. **A premise of
this dispatch that does not hold is a STOP and a report, never something to work around.**"*

**What was run.** The sanctioned enumeration, over the whole tracked population, recorded as ordered
at `tools/audit/changed_paths_defense_sizing_task0.json` (`tools/audit/changed_paths.py`, working-tree
enumeration; no value is transcribed here — **D-431**).

**What it found.** Every record but one carries the untracked code. **Exactly one record is a tracked
modification, and it is named rather than counted:**

| Path | Code |
|---|---|
| `cowork_handoff_entry_one_hundred_and_forty_seven.md` | ` M` — index matches HEAD, working tree differs |

**The finding was established at the object and not left at the enumeration.** The committed text was
fetched from the git object at the base tip the dispatch declares —
`d2ebe3cc98a33affdb5ffa2b8faf993bff6f0a71` — and both texts were read whole with the file tools. They
differ, and the difference is substantive rather than a whitespace or line-ending artifact.

**What the difference is, stated so the reading side need not re-derive it.** The working-tree copy is
the same entry brought current after the preceding batch returned. Against the committed copy it
carries: a rewritten opening banner (*"A BATCH IS OUT … IT WILL HAVE MOVED BY THE TIME YOU BOOT"*
becomes *"NOTHING IS RUNNING … THE TIP IS `d2ebe3cc98…`"*); a rewritten size sentence; a new section
**"THE BATCH'S RETURN, VERIFIED AT THE OBJECTS"**; a new owed-work bullet recording that
`cowork_memory_pointer_cut_2026_09_07.md` is on disk but untracked and that a later batch should track
it; an amended *"THE NEXT COWORK ACT"* bullet; changed inherited-state bullets (the tip, the gating
answer's identities); a rewritten *"THE VERIFIED STOP"* paragraph; **a new declared departure (xiii)**
which states the amendment in its own words — *"THIS ENTRY WAS AMENDED AFTER THE BATCH RETURNED,
INSIDE THE SAME SITTING"*; a rewritten cadence step 1; and an extended watch line.

**So the modification is explained, and it is still a STOP.** The dispatch fixes the expectation at
ZERO tracked modifications without qualification, and it carves out exactly one case — *"If the
enumeration at (a) shows a file of this list already tracked **and unmodified**, that file is simply
dropped from the commit"* — which does not reach this file on either limb: it is not a member of Task
0(c)'s list, and it is modified. **Nothing here is corrected, and no judgment is offered on whether
the amendment should have happened.** The fact is reported.

**Why the second STOP condition fires too.** The dispatch's premise 6 states that four of the five
Task 0(c) files *"were written this sitting"* and says nothing about entry 147 having been amended in
the same sitting — while that entry's own departure (xiii) records the amendment. The expectation of
zero tracked modifications is therefore false at the objects, which the dispatch itself classes a STOP
rather than something to work around.

---

## 2. THE TWO DECLARED-UNESTABLISHED PREMISES — BOTH ANSWERED, AS ORDERED

The dispatch says of both: **"CHECK EACH AND REPORT THE ANSWER EITHER WAY. DO NOT ASSUME."** Both were
checked before the STOP was written, because the answers are owed whatever happens to the tasks.

### Premise (5) — must a new tool be enrolled in the guard runner's authored invocation list?

**ANSWER: YES, IT MUST — and the ground is read at the guard runner's own source, which this side
opened in full.** `tools/audit/gen_guard_state.py`:

- `candidates()` walks every `*.py` under `tools/audit/` and admits any whose source matches the
  module-level pattern `--(check|verify|establish)\b`. A tool built to Task 1's specification carries a
  `--check`, so it **enters that derived population by construction**.
- `main()` computes `unclassified = sorted(p for p in derived if p not in authored_paths)`, where
  `authored_paths` is drawn from the `AUTHORED` table.
- A non-empty `unclassified` prints `STOP: derived candidate(s) with no authored invocation` and
  **returns 1**. The artifact's own field says it in terms: *"a derived candidate with no authored
  invocation. NON-EMPTY IS A STOP: a guard exists that this run did not cover."*
- The docstring states the same rule as the tool's reason for existing: *"a DERIVED candidate with no
  authored invocation is UNCLASSIFIED -- a new guard cannot be silently left unrun."*

**AND THERE IS A SECOND ENROLMENT THE DISPATCH DOES NOT NAME, WHICH THIS SIDE FOUND BY READING AND
REPORTS RATHER THAN ABSORBING.** `tools/audit/gen_guard_classification.py` derives its population from
`gen_guard_state.AUTHORED` and declares as the first of its three STOPs: *"a tool in the guard-state
population with NO authored verdict is a STOP."* So enrolling a tool in the invocation list without
authoring its classification verdict in the same act would move the STOP from one check to the other
rather than clearing it. **The established practice in the record is to do both in the act that creates
the tool**, and the `AUTHORED` table's own comments say so repeatedly — for example, of the two tools
added on 2026-08-15: *"each classified in the same act at `gen_guard_classification.py` — which STOPs
if the two tables disagree (#6)"*.

**Consequence for a later batch, stated and not acted on:** building
`tools/audit/gen_defense_share.py` requires, in the same commit, an `AUTHORED` entry in
`gen_guard_state.py` and a `VERDICTS` entry in `gen_guard_classification.py`. **Neither was written
here**, because the tool was not built.

### Premise (6) — are the five files of Task 0(c) untracked at this tree?

**ANSWER: YES, ALL FIVE ARE UNTRACKED — established with the sanctioned enumeration tool as ordered,
not taken from the dispatch.** Each appears in
`tools/audit/changed_paths_defense_sizing_task0.json` with the untracked code:

| Path | Present as |
|---|---|
| `cowork_claude_md_live_rule_classification_2026_09_08.md` | untracked |
| `ratification_surfaces/cowork_pruning_and_satellites_surface_2026_09_08.md` | untracked |
| `cowork_rulings_2026_09_08_defense_satellite_sitting.md` | untracked |
| `cowork_handoff_entry_one_hundred_and_forty_eight.md` | untracked |
| `cowork_memory_pointer_cut_2026_09_07.md` | untracked |

**The fifth is the one the dispatch declared RELAYED and unchecked by the writing side, and the relay
holds.** The file inside `ratification_surfaces/` appears as its own record rather than being collapsed
into a directory record, so the enumeration's stated directory-collapse limit does not bear on this
answer.

---

## 3. WHAT WAS DONE, AND WHAT WAS NOT

| Ordered act | State |
|---|---|
| Task 0(a) — the enumeration, recorded at its named path | **DONE.** It is what produced the STOP. |
| Task 0(b) — run the full guard set and record its state | **NOT DONE.** Running it is proceeding. |
| Task 0(c) — commit the five files in one commit | **NOT DONE. Nothing was committed.** |
| Task 1 — build `tools/audit/gen_defense_share.py` and publish `defense_share.json` | **NOT DONE.** No tool written, no artifact written, no marker located, no span imported. |
| Task 2(a) — this batch's `STATUS.md` entries | **NOT DONE.** `STATUS.md` is untouched. |
| Task 2(b) — the forward bound on `STATUS.md` | **NOT DONE.** |
| Task 2(c) — regenerate `tools/audit/session_start_read_size.json` | **NOT DONE.** |
| Task 2(d) — the standing self-check | **DONE**, over what this batch actually touched — §5 below. |
| Task 2(e) — this report | **DONE**, as a STOP report. |

**Nothing on the dispatch's own prohibition list was touched.** No edit to `CLAUDE.md`, `DECISIONS.md`,
`ARCHITECTURE.md`, `OPEN_ITEMS.md` or any ruling record. No satellite file. No text moved. No
open-items row created, flipped or discarded. No decisions-register entry, no `D-NNN`, no finding
number. No `src/` change, no build, no test, no golden, no corpus, nothing under `tools/robust_stop/`
or `tools/corpus/`. No paper opened, no extract, no sweep, no verdict moved, no gate lifted.

**What this batch added to the tree, both untracked and uncommitted:**

- `tools/audit/changed_paths_defense_sizing_task0.json` — the ordered Task 0(a) artifact.
- `cc_report_defense_share_sizing_2026_09_08.md` — this file.

---

## 4. EVERY READING TAKEN THAT THE DISPATCH DID NOT ORDER

- **The ordinary session-start read was performed in full before anything else**, on the standing
  convention that a single-file opening instruction is not an exemption from it (**D-230**, P-1):
  `CLAUDE.md` at its six session-start spans, arriving whole in this session's context blocks;
  `STATUS.md` whole; `DECISIONS.md` whole, in three reads with no gap; and the derived gating answer
  at `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`, its header block and
  all of its gating identities.
- **`BUILD_AND_TEST.md` was NOT read, and the ground is stated rather than assumed.** Its read is
  conditional on a session that builds, tests, or runs a measurement tool *whose command lives there*.
  This session builds nothing and tests nothing, and that file was searched for every tool this batch
  would have run — the only one it carries is `tools/audit/corpus_arm_stamp.py`, which is not among
  them. The condition is not met.
- **`tools/audit/changed_paths.py` was read in full** before it was run, so that what the enumeration
  can and cannot see was known rather than trusted — in particular its stated limits: it reports what
  git reports, an ignored path is invisible to it, and an untracked DIRECTORY collapses to one record.
- **`tools/audit/gen_guard_state.py` was read in full**, and
  `tools/audit/gen_guard_classification.py` down to and including its three declared STOPs and the
  first block of its authored verdicts — the readings premise (5) required.
- **Both texts of the modified handoff entry were read whole**, the committed one from the git object
  at the declared base tip and the working-tree one with the file tools, so that §1's account of the
  difference is a reading of the objects and not an inference from the status code.

**One declared bound on §1.** The comparison of the two texts was made by reading both whole, not by a
mechanical difference: a small wording change inside an otherwise-unchanged paragraph could have
escaped it. **What is established is that the file is modified and that the amendment its own
departure (xiii) declares is present in the working tree; the enumeration of changed passages is a
reading and is offered as one.**

---

## 5. THE STANDING SELF-CHECK

Performed on what is actually on disk from this batch, against the guiding principles, the
conventions, the gate and threshold policies, and `DEFECT_TYPES.md`.

- **No violation found, and no correction was needed.** The two files this batch wrote are a generated
  artifact produced by a committed tool and this report.
- **#13 and the STOP conventions** are satisfied by stopping rather than working around: the dispatch
  named this exact condition and it is honoured literally.
- **D-431** — no value is transcribed. The one record that matters is named by its identity, and the
  enumeration is cited to its artifact.
- **D-253** — every working-tree read went through the file tools. The one shell use was a
  content-addressed git object query by explicit hash. **The shell-read guard fired once and was
  obeyed**: a first attempt bundled a working-tree size read into the same command, the guard denied
  it naming D-253, and the command was re-issued with that half removed rather than worked around.
- **The reserved-word convention** was applied to this report's own new text: *measurement* not the
  gauging sense of the bare noun, *measurement tool* and *check* rather than the violin word, the two
  registers named in full, and *file name* rather than the note-stem word.
- **#19** — nothing here is claimed established that was not positively checked. Premise (5) is
  answered from the runner's own source, premise (6) from the sanctioned tool, and §4's bound is
  declared rather than left implicit.

---

## 6. WHAT THE READING SIDE IS OWED, AND WHAT IT IS NOT

**Owed:** a decision on the tracked modification. The dispatch cannot be resumed as written while the
expectation at Task 0(a) is false, and this side may not choose between the available routes — commit
the amended entry alongside the five, exclude it, or re-issue the dispatch with the expectation
restated. **That is the reading side's act, not this one's.**

**Not owed, and explicitly not claimed:** that the amendment to entry 147 was wrong; that the five
Task 0(c) files should or should not be committed; anything about the size of the defense material,
which is the measurement this batch exists for and **was not taken**; and anything about the guard
set's state, which was not run.

*Provenance: `cc_instruction_defense_share_sizing_2026_09_08.md`, base tip
`d2ebe3cc98a33affdb5ffa2b8faf993bff6f0a71`. No commit was made by this batch.*
