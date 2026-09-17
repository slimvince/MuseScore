# CC INSTRUCTION — check the reference map report against the repository, 2026-09-17 (READ-ONLY, one new tool)

**THE BASE.** The current commit should be `5d24edb565b2e0e9efc92e082c163112bd97087f` on branch `master`.
**Check this first (Task 0).**

**WHY THIS EXISTS.** The previous batch wrote
`records/cc/reports/cc_report_root_records_reference_map_2026_09_16.md` (the map of every reference to the root
record files, before they are moved). The move dispatch will be written from it. The report is 11,423 lines, and
the previous writing session ran out of room reading it, so on the user's ruling of 2026-09-17 the writing side
reads its prose and judgement sections itself and **this batch checks its long listings mechanically, with a
tool whose output can be re-run**. The writing side may not do this itself: `CLAUDE.md` Conventions bars it from
reading working-tree files through a shell or interpreter (D-253).

**This batch changes no existing file.** It writes one new tool, one generated output and one report.

**The writing side does not touch this file, or the report it checks, while the batch runs.**

---

## THE ROUTE RULE

Read with the file tools (Glob, Grep, Read) when you read by hand. **Apart from git, the new tool is the only code that reads files**,
and it runs as `python tools/audit/check_reference_map.py …`. No other interpreter code, no shell text utility on any
file, no redirection from a file. Git commands: those in Task 0, and the `git ls-files` / `git cat-file` calls the
tool itself makes. **Never open, list or search anything under `docs/research_papers/polyph9-release/`,
`scratch_artifacts/`, `external resarch summary/`, `Claude outputs/`, `Codex research inventory/` or `.git/`** — the
tool excludes them too. **If a guard refuses anything, STOP and report the refusal text verbatim.**

If the repository's own rules require a new tool under `tools/audit/` to be enrolled or registered anywhere, do what
those rules say and name, in the report, the rule you followed and where you read it. **If you cannot establish what
they require, STOP before running the tool.**

---

## TASK 0 — start state, pinning

**(a)** `git hash-object -w` on this dispatch and on the report being checked. Record both identities. The tool reads
the report **from its blob** (`git cat-file blob <identity>`), never from the working tree.

**(b)** `git rev-parse --abbrev-ref HEAD`, `git rev-parse HEAD`. **Not `master` at the base → STOP.**

---

## TASK 1 — write the tool

Write `tools/audit/check_reference_map.py`. It takes the report's blob identity as an argument, reads the working tree
for everything else, applies the exclusions above at every walk, and writes `tools/audit/reference_map_check.json`.
Its docstring states what it checks, what it does not, and that a line it cannot parse is **published as unchecked,
never skipped**. It checks five things. Every mismatch is published whole, with the report's line number.

1. **§2(b).5, the hit lines.** The block between the heading `### 2(b).5 Every hit line, verbatim, in Grep's order`
   and its closing `~~~~`. Each line is `path:line:content`. Check that the named file's line equals `content`
   exactly. Then walk the repository independently with the same regular expression
   (`cowork_|cc_instruction|cc_report|cc_\*|listdir|glob\(|iterdir|scandir`) over the same file types
   (`*.py *.mjs *.js *.sh *.ps1 *.bat *.cmake`) and publish the difference **in both directions**: hits the report
   lists that the walk does not find, and hits the walk finds that the report does not list.
2. **§2(b).1 and §2(b).2, the deciding lines.** Each quoted item of the form ``NNN: `code` `` or
   ``NNN–MMM: `code` ``. Check that the code occurs at that line, or inside that range, in the file the entry names.
   `...` and `…` inside a quote match any text. Where the file cannot be resolved to exactly one path, or the item
   cannot be parsed, publish it as unchecked with the reason.
3. **Task 2(a), the counts.** For each of the six expressions, recompute every listed file's figure **twice**: as
   matching lines and as individual matches. Publish, per file, which of the two the report's figure equals, or
   neither. Publish files the walk finds with a match that the report does not list, and the reverse.
4. **Task 1, the root lists and their T/U marks.** Recompute each list from a listing of the repository root alone,
   and each mark from `git ls-files` (at most forty literal names per call). Publish every difference.
5. **§2(c), coverage.** Take every file whose text matches `(cc|cowork)_[A-Za-z0-9_]+\.md` under the exclusions.
   Check that each is classified exactly once in §2(c), or falls in the population §2(c).1 covers in one statement.
   Publish files classified twice, files not classified, and classified files that no longer match.

**Differences caused by later changes.** The report was written on 2026-09-16; files have been added and changed
since (for example `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_nine.md`). For every
difference in checks 1, 3, 4 and 5, publish whether the file's modification time is later than the report's. **Do not
decide** whether a difference is a defect of the report; publish it.

**What the tool does not check, stated in its docstring and in the output:** whether any verdict (i)–(iv) or any class
in §2(c) is right. Those are judgements; the writing side reads them.

---

## TASK 2 — run it and write the report

Run the tool once. Then write, **with the Write file tool**,
`records/cc/reports/cc_report_reference_map_check_2026_09_17.md`, carrying: the Task 0 identities and answers; the
enrolment rule you followed, or that none was required and where you read that; the exact command; and, for each of
the five checks, **every mismatch and every unchecked item named**, copied from the output. A total may be stated
only as a sum of named members, or as a figure the output itself carries, cited to its field (D-431). **Do not
interpret a mismatch; name it.**

**Do not commit, stage or push anything.** At the foot of your chat reply, give the report's path, the output's path
and the Task 0 identities.

---

## DECLARED BY THE WRITING SIDE

- **What this batch's orders move:** the git object store (two pinned blobs) and three new files —
  `tools/audit/check_reference_map.py`, `tools/audit/reference_map_check.json` and the report. Plus any enrolment
  edit the repository's rules require for a new tool, which you name in the report. **No other existing file is
  edited, moved, staged or deleted.**
- No `STATUS.md` entry, no other generator, no guard-set run, no build. The three new files are committed by the
  later move dispatch, not by this batch.
- The ordinary session-start read still binds you (P-1, D-230).
- The writing side's own check before release: every path and heading named here was read at the staged copy of the
  report or the previous dispatch this sitting; the enrolment requirement was **not** read by the writing side, which
  is why Task 1 orders you to establish it.

## STOP CONDITIONS

- Task 0(b) not at the base.
- Any guard refusal.
- The enrolment requirement for a new tool cannot be established.
- **Any instruction here found false at the objects.**

## WHAT THIS BATCH MAY NOT DO

Edit, move, stage, commit, push or delete any file beyond the three it writes and a required enrolment; open, list or
search the excluded locations; run any other generator, guard or build; correct the report being checked.
