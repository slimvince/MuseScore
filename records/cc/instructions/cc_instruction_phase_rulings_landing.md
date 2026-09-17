# CC dispatch — land the phase-definition sitting's records and the eighteenth handoff block, and perform the ruled D-231 rephrasing in `CLAUDE.md`

> **Dispatch (Cowork, 2026-08-15).** Executes the rulings of
> `cowork_rulings_2026_08_15_phase_definition_sitting.md` — above all its §4 (D-231 rephrased in
> place, Alternative A). Written at a verified STOP; nothing else is running.
> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
> `C:\s\MS\BUILD_AND_TEST.md`. **Then read, in full:** the sitting's ruling record named above;
> `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`; and `cowork_handoff.md`'s
> EIGHTEENTH entry block (the current entry point — uncommitted on disk, which Task 0 lands).
> The standing bars bind this batch whole: **no `src/` edit, no golden, no test changed, moved or
> run, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the analysis, no
> design, no repair, no derivation, no decisions-register entry** (the filtering ruling stands),
> **no open-items row created, flipped or discarded.** This batch does NOT open the preparation
> phase: no register filter, no rulings sort, no findings ledger, no boot list, no pruning act,
> no caller-check, and none of the newly visible or still-ignored files is landed.
>
> **Commit-and-push per task. Run the FULL guard set BEFORE the first edit and again at the end;
> record both states.** The expected start state is the previous batch's end state — 48 run,
> 47 passing, ONE failing ([[OI-372]]'s tool), zero STOPs, and NO stale report — **a different
> start state is a STOP-and-report.** Verify every commit after the fact at the object
> (`git diff-tree --no-commit-id --name-only -r <sha>`) and record the SHAs in the close. The
> reserved-word conventions and the ruled vocabulary replacements (the sitting record §1:
> *a changed passage*, *the current commit*, *untrusted source*) bind all new prose.

## Ruling ledger (what this batch may rest on — quoted at the record, not paraphrased)

- **Sitting record §4 (Decision 2, the user's "A"):** the D-231 Conventions entry in `CLAUDE.md`
  is *"REWRITTEN IN PLACE to state the ruled six-phase structure, pointing at the ruled
  definitions as their one home (#6), with the former wording preserved in place (#12)"*; the
  truth half is *"REPLACED by the opposite rule, stated plainly where every session reads: a
  disagreement between specification and code is evidence, reserved for the audit; no document
  is corrected on the ground that the code says otherwise"*; and *"the edit itself … lands by
  dispatch under the ordinary discipline, with this record as its authority."* This dispatch is
  that discharge.
- **Sitting record §2 (Decision 1):** the six phases — preparation → pilot → framework → detail
  specifications → measurement design → audit — with the fix plan after the audit unchanged.
- **Sitting record §3:** every phase closes with a recorded retrospective.
- **Sitting record §8:** the next acts are exactly this batch's two: the Task-0 landing and the
  D-231 edit. Nothing further is authorized by it.
- **The eighteenth handoff block, of itself:** *"THIS BLOCK IS UNCOMMITTED AT ITS OWN CLOSE —
  the next batch's FIRST task lands it, the Task-0 pattern, naming this file explicitly."*

## Premise ledger

- **FACT** — both ignore rules over the dispatch family are removed: `/cc_*.md` at the
  ruled-inventory-landing batch and `/cc_instruction_*.md` at commit `e1a313925e` (verified at
  the objects by the previous batch's report §1, its close, and the one-line numstat). So this
  file is staged WITHOUT any override — the first dispatch ever landed plainly.
- **FACT** — the previous batch's end state: 48 guards run, 47 passing, one failing
  ([[OI-372]]'s tool), zero STOPs, no stale report (`cc_report_batch_return_rulings.md` §3.a/§4;
  the close in `cowork_away_returns.md`).
- **ASSUMPTION A1** — `cowork_handoff.md`'s on-disk state differs from its committed blob ONLY
  by the eighteenth entry block (written at the previous writing-side close). **Check ordered
  (Task 0 step 1): diff the working file against the committed blob; any difference outside
  that one block is a STOP-and-report, never a guess.**
- **ASSUMPTION A2** — the D-231 entry in `CLAUDE.md` is the Conventions bullet opening
  **"ISSUE-EXHAUSTION AND SPECIFICATION COMPLETION BEFORE ANY FIX DESIGN (user-directed,
  2026-08-02…"**, and it is the ONE home of the three-phase text (the sentence *"the
  specification text is corrected wherever it states something false at HEAD"* occurs inside it
  and, outside quotations of it, nowhere else in the file). **Check ordered (Task 1 step 1):
  read the entry in full with the file tools and search the file for that sentence before
  editing; a second live (non-quoting) occurrence is a STOP-and-report.**
- **ASSUMPTION A3** — the three writing-side files named in Task 0 exist on disk exactly as the
  writing side committed them this session (two new, one under `ratification_surfaces/`).
  **Check: the sanctioned changed-path enumeration shows them untracked/modified as named; a
  missing path is a STOP-and-report.**

## Task 0 — land the writing-side records and the eighteenth handoff block

1. **A1's check first** (diff `cowork_handoff.md` against its committed blob).
2. Commit, in ONE commit whose message names its own act, exactly these FOUR paths and no fifth:
   1. `cowork_handoff.md` (the eighteenth block lands — named explicitly, the Task-0 pattern)
   2. `cowork_rulings_2026_08_15_phase_definition_sitting.md` (new)
   3. `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` (new)
   4. `cc_instruction_phase_rulings_landing.md` (this file — staged plainly, no override)
3. Verify at the index through the sanctioned enumeration before the commit and at the object
   after it. Push.

**Registered expectation E0:** `git diff-tree` on the Task 0 commit lists exactly 4 paths, and
no staging override of any kind was needed.

## Task 1 — the D-231 rephrasing in `CLAUDE.md` (sitting record §4)

1. **A2's check first.** Read the whole D-231 Conventions entry with the file tools; search the
   file for the truth-half sentence.
2. **The edit is a PURE INSERTION — nothing is deleted, nothing below is reworded.** Insert, at
   the head of that entry (immediately after its opening bold heading sentence ends, before the
   "Three phases, strictly ordered" text begins), the following block VERBATIM:

   > **★ THE THREE-PHASE STRUCTURE BELOW IS SUPERSEDED AND ITS TRUTH HALF IS REPLACED
   > (user-ruled 2026-08-15; the ruling record is
   > `cowork_rulings_2026_08_15_phase_definition_sitting.md`; the ruled definitions' ONE home is
   > `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §3 — a pointer, never
   > a copy, #6).** The governing structure is now SIX PHASES — preparation → the pilot (on
   > `docs/scoring_model.md`) → the framework → the detail specifications → measurement design →
   > the audit — with the fix plan after the audit unchanged: #8's three-clause gate and the
   > one-prioritized-fix-plan rule stand exactly as below. Every phase closes with a recorded
   > retrospective (lessons of any kind, with evidence, routed to their homes; amendments only by
   > the user's ratification). **The rule that replaces the truth half, stated here because it
   > must bind even a session that reads nothing else: A DISAGREEMENT BETWEEN SPECIFICATION AND
   > CODE IS EVIDENCE, RESERVED FOR THE AUDIT; NO DOCUMENT IS CORRECTED ON THE GROUND THAT THE
   > CODE SAYS OTHERWISE.** The COMPLETE half survives as a property, not a program: the
   > detail-specification phase derives specifications that are born complete — every decision in
   > its owning specification, with its defense. **The former three-phase text below is PRESERVED
   > IN PLACE (#12) and is no longer the governing structure.** Its embedded sub-rulings keep
   > their own recorded standing and none is edited by this supersession: old phase 2's
   > exhaustion duty (measured coverage, every channel enumerated, the bounded trust statement)
   > is inherited by the audit phase; old phase 3 and its family-gate qualification are the
   > unchanged fix-plan territory; a sub-ruling whose subject was the superseded truth half
   > (D-639's reach test) loses its subject with it, its record untouched and its register
   > standing settled at the register's own discharge, not here. The abbreviation HEAD in the
   > preserved text below is read under the ruled vocabulary: the current commit of everything,
   > never the code alone.

3. Nothing else in `CLAUDE.md` moves. Run the full guard set. **If a check reports an anchor
   drift caused solely by this insertion, remap per the drift report's own per-citation practice
   and say so in the close; any other new red is a STOP-and-report.**
4. Commit as ONE commit naming its own act and citing the sitting record §4 — `CLAUDE.md` as
   the only path unless step 3's sanctioned remap touched a generated anchor artifact, in which
   case that artifact rides the same commit and the close names it. Push. Verify at the object.

**Registered expectation E1:** the commit's diff to `CLAUDE.md` is insertion-only — zero
deletions (the branch-one-banner precedent: a pure insertion is provable at the numstat) — and
afterwards the truth-half sentence still occurs in the file ONLY inside the preserved text and
its quotations, with the superseding block standing above it.

## Task 2 — the close

One `STATUS.md` pointer entry per task and nothing else in that file. The FULL close appended to
`cowork_away_returns.md` — both guard-set states, every SHA, every expectation graded, every
problem declared. The report file `cc_report_phase_rulings_landing.md`, an ordinary tracked
file. Commit, push, verify at the object.

**Registered expectation E2:** the end-state guard run reports 48 run, 47 passing, one failing
([[OI-372]]'s tool), zero STOPs, and the committed `guard_state.json` re-derives (no stale
report) — the batch introduces no red and works none around.

## What this batch does NOT do

- **No preparation-phase act:** no register filter, no rulings sort, no findings ledger, no
  fact-gate, no curated boot list, no pruning, no caller-check, no archiving, no mining.
- **No file landed beyond Task 0's four** — the 284 newly visible instruction files and the
  remaining ignored files stay unlanded, riding their ruled fates.
- **No open-items row touched; no decisions-register entry written** (the filtering ruling
  stands — the register's supersession records land at its own discharge).
- **No `src/` edit, no golden, no test, nothing under `tools/corpus/` or `tools/robust_stop/`,
  no measurement, no design, no repair, no derivation, no pilot.**
- **No edit to any guard or generator** (Task 1 step 3's sanctioned remap of a generated anchor
  artifact, if needed, is the one bounded exception and is declared in the close).
- **[[OI-372]] and [[OI-374]] stay exactly as found. [[OI-179]] stays OPEN and GATES.**
