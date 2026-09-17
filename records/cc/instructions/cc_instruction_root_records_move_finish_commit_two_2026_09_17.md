# CC INSTRUCTION — root records move: Commit 1 is made; do Commit 2, the content proof, Commit 3 and the push, 2026-09-17

**THE BASE.** Branch `master` at **Commit 1, `447311137a934ab8e3f51e7abf8e18e7b8d2bd0e`**, with an uncommitted working
tree. The third-issue run of `records/cc/instructions/cc_instruction_root_records_move_finish_resume_2026_09_17.md`
made Commit 1 and stopped before Commit 2 on a guard refusal of a `cat` it added. Its report is
`records/cc/reports/cc_report_root_records_move_finish_resume_third_2026_09_17.md` — **read it whole before Task 0.**

**The text this dispatch continues.** Read both from their pinned blobs with `git cat-file blob`, never from the
working tree:
- the base dispatch, blob `a16402ac47ed9f07de68629f299b65fd71eee51e`;
- the resume dispatch, third issue, blob `bfb7846d337462ed4531f568a2edd38aab067b82`.

**Their route rule, their Task 3 (as the resume dispatch changes it) and their report rules bind here, except where
this dispatch names a change.** Tasks 0, 1 and 2 of both are DONE and are not repeated.

**The writing side does not touch this file, and lands nothing in the repository, while the batch runs (D-251).**
**Do not undo Commit 1 or any edit.**

---

## THE ROUTE RULE, AS IT BITES HERE

- **No shell command reads any file** — not `cat`, `head`, `tail`, or any other, and not in the scratchpad. Three runs of
  this line stopped on a guard refusal of a shell read the executing session added (`git diff --no-index`, `tail`,
  `cat`). **Read every capture with Read or Grep.**
- **Take each commit hash from the `git commit` command's own printed output.** Do not use `-q`; do not redirect the
  commit command's output to a file.
- **Add no command of your own.** Any guard refusal → STOP.

---

## TASK 0 — the state

**(a)** `git hash-object -w` on this dispatch. Record the identity.

**(b)** `git rev-parse --abbrev-ref HEAD` and `git rev-parse HEAD`: `master` at
`447311137a934ab8e3f51e7abf8e18e7b8d2bd0e`, else STOP.

**(c)** `python tools/audit/changed_paths.py --staged`, captured, given a blob identity: must be
`2781d206447325730f78a7685285f43d32d31ece` (nothing staged), else STOP.

**(d)** `python tools/audit/changed_paths.py`, captured, given a blob identity. Compare with
`git cat-file blob 8b74133be982d3084a8943a5aa6507ad0949ba68` (the stop capture). **The only new records allowed** are
untracked records for the stop report named above and for this dispatch. A difference only under `scratch_artifacts/`
is reported, not a STOP. Anything else → STOP.

**(e)** `python tools/audit/gen_guard_state.py --check`, captured whole. Compare guard by guard with the third-issue
run's Task 2(c) capture, `git cat-file blob 9554b6f394edea834d0079aed50273f1957cd814`
(`81 guard(s) run, 18 failing, 4 not run, 16 historical record(s)`). **Every guard's result must be equal**, else STOP.
Call this **the Task 2(c) reference** for Commit 3's step 4.

---

## TASK 3 — Commit 2, the proof, Commit 3, the push

Exactly the resume dispatch's Task 3 (third issue), with these changes:

- **Commit 1 is done.** Skip it.
- **Commit 2 adds, by explicit path only:**
  - every path `changed_paths.py` shows modified in the working tree, **except:**
    `docs/research_papers/BIBLIOGRAPHY.md`, `docs/research_papers/README.md`,
    `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_eight.md` (it now shows ` M`; its rename is
    already in Commit 1, and its working-tree edit is not this line of work), and
    `tools/audit/claude_md_finer_archive.json` (the user's ruling of 2026-09-17);
  - the base dispatch's named record files, `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_two.md`,
    the base dispatch, the resume dispatch, **this dispatch**, and every file Glob finds at
    `records/cc/reports/cc_report_root_records_move_finish*_2026_09_17.md` (this run's own report does not exist yet).

  Before committing, `changed_paths.py --staged`, captured and read with Grep: none of the four excluded paths staged.
- **The content proof** is `git diff 447311137a934ab8e3f51e7abf8e18e7b8d2bd0e <Commit 2 hash>`, checked as the base and
  resume dispatches order. In addition, for `records/cowork/handoff/cowork_handoff.md` (a rename in Commit 1 whose edits
  land in Commit 2): every changed line equals its old line once each new path is replaced by its root name.
- **The report (Task 4)** goes to `records/cc/reports/cc_report_root_records_move_finish_commit_two_2026_09_17.md`
  (Glob first; if it exists → STOP before writing). It carries this batch's Task 0, Commit 2, the proof, and Commit 1's
  hash as given here.
- **Commit 3** as the resume dispatch orders; its step 4 guard results must equal Task 0(e) here.
- **Push:** `git push origin master`. Never `--force`. A failure is reported verbatim, with no retry by other options.

At the foot of the chat reply: the report path, this dispatch's blob identity, the Commit 1, 2 and 3 hashes, the push
result.

---

## DECLARED BY THE WRITING SIDE

- **Checked at the files this sitting:** the stop report whole; `.git/refs/heads/master` reads
  `447311137a934ab8e3f51e7abf8e18e7b8d2bd0e`.
- **Relayed, not checked:** the blob identities of the captures and of the two pinned dispatches, and the stop state
  counts, all from the stop report.
- **What this batch's orders move:** two commits and one push; `STATUS.md`, `STATUS_ARCHIVE.md`,
  `gen_status_batch_bound.py` and the two measurement artifacts through Commit 3's steps; the new report. No tool
  source other than the forward bound's re-aiming, no `CLAUDE.md` passage, no `src/` file.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

Those of the base and resume dispatches, plus: any Task 0 mismatch; any excluded path staged; **any instruction here
found false at the objects.** On any STOP: undo nothing; report the two captures and every commit hash; stop.
