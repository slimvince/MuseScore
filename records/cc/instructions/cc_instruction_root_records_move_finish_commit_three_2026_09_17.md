# CC INSTRUCTION — root records move: Commits 1 and 2 are made; do Commit 3 and the push, 2026-09-17

**THE BASE.** Branch `master` at **Commit 2, `54804de49ac593b532e804bcfb881366e3a018b5`** (parent Commit 1,
`447311137a934ab8e3f51e7abf8e18e7b8d2bd0e`). The run of
`records/cc/instructions/cc_instruction_root_records_move_finish_commit_two_2026_09_17.md` made Commit 2 and stopped at
its content proof. Its report is `records/cc/reports/cc_report_root_records_move_finish_commit_two_2026_09_17.md` —
**read it whole before Task 0.**

**The one open point of that proof is closed here.** Eleven entries of `tools/audit/specification_document_set.json`
changed position. The tool writes that array with `for target in sorted(GRADES):`
(`gen_specification_document_set.py` line 817, checked by the writing side), and the previous batch renamed those
eleven keys from root names to `records/…` paths. The report found each moved entry equal field by field once each path
is put back to its root name, with no entry added or dropped. **A re-sort that follows only from a key becoming its new
path is part of "a moved file's root name becoming its new path".** The writing side wrote that bar, so it settles it
rather than the user. **The content proof of Commit 2 therefore passes. Do not re-run it.**

**The text this dispatch continues.** Read from pinned blobs with `git cat-file blob`: the base dispatch
`a16402ac47ed9f07de68629f299b65fd71eee51e`, and the resume dispatch (third issue)
`bfb7846d337462ed4531f568a2edd38aab067b82`. Their route rule and their Commit 3 steps bind here except where this
dispatch names a change.

**The writing side does not touch this file, and lands nothing in the repository, while the batch runs (D-251).**
**Undo nothing.**

## THE ROUTE RULE, AS IT BITES HERE

- **No shell command reads any file** — not `cat`, `head`, `tail` or any other, and not in the scratchpad. Read every
  capture with Read or Grep.
- Take the commit hash from the `git commit` command's own printed output (no `-q`, no redirect).
- Add no command of your own. Any guard refusal → STOP.

## TASK 0 — the state

**(a)** `git hash-object -w` on this dispatch. Record the identity.

**(b)** `git rev-parse --abbrev-ref HEAD` and `git rev-parse HEAD`: `master` at
`54804de49ac593b532e804bcfb881366e3a018b5`, else STOP.

**(c)** `python tools/audit/changed_paths.py --staged`, captured, given a blob identity: must be
`2781d206447325730f78a7685285f43d32d31ece`, else STOP.

**(d)** `python tools/audit/changed_paths.py`, captured, given a blob identity. Compare with
`git cat-file blob af30f8f394ce42ee628bd95e301dcaec3537c7a8`. **The only new records allowed** are untracked records for
`records/cc/reports/cc_report_root_records_move_finish_commit_two_2026_09_17.md` and this dispatch, **and a ` M` record
for `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_two.md`** (committed in Commit 2, then updated
by the writing side before this dispatch was handed over). A difference only
under `scratch_artifacts/` is reported, not a STOP. Anything else → STOP.

**(e)** `python tools/audit/gen_guard_state.py --check`, captured whole. Every guard's result must equal
`git cat-file blob 9554b6f394edea834d0079aed50273f1957cd814`
(`81 guard(s) run, 18 failing, 4 not run, 16 historical record(s)`), else STOP.

## TASK 1 — the report, before Commit 3

Write with the Write file tool `records/cc/reports/cc_report_root_records_move_finish_commit_three_2026_09_17.md`
(Glob first; if it exists → STOP before writing). It carries Task 0, the three commit hashes known so far, and **a
section naming the three checks left failing by the user's ruling of 2026-09-17** (`gen_claude_md_finer_archive.py`,
`gen_post_split_archive.py`, `gen_claude_md_prune_backlog.py`), their messages and cause as the earlier reports record
them, labelled derived and not measured per passage. Name members; state a total only as a sum of named members or a
figure a tool printed (D-431).

## TASK 2 — Commit 3 and the push

The base dispatch's Commit 3 steps 1–6, as the resume dispatch changes them, with these specifics:

1. The `STATUS.md` entry points at this line's reports and names the three checks left failing by the user's ruling of
   2026-09-17, restating no figure.
2. The forward bound: `tools/audit/gen_status_batch_bound.py`, read its docstring first; `BASE_COMMIT` =
   `54804de49ac593b532e804bcfb881366e3a018b5`; this entry written first, `--apply` second. If it cannot be performed as
   described → keep the entry, skip the bound, report why.
3. `python tools/audit/gen_session_start_read_size.py`, then `python tools/audit/gen_defense_share.py`.
4. `python tools/audit/gen_guard_state.py --check`, captured: every guard's result equal to Task 0(e), else STOP (no
   Commit 3, no push).
5. **Commit 3, by explicit path only:** `STATUS.md`; `STATUS_ARCHIVE.md` and `tools/audit/gen_status_batch_bound.py` if
   the bound ran; `tools/audit/session_start_read_size.json`; `tools/audit/defense_share.json`; this batch's report;
   `records/cc/reports/cc_report_root_records_move_finish_commit_two_2026_09_17.md`; this dispatch;
   `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_two.md`. **Never** the four
   excluded paths (`docs/research_papers/BIBLIOGRAPHY.md`, `docs/research_papers/README.md`,
   `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_eight.md`,
   `tools/audit/claude_md_finer_archive.json`). Check with `changed_paths.py --staged` before committing.
6. `git diff 54804de49ac593b532e804bcfb881366e3a018b5 <Commit 3 hash>`: changes only in those paths; the two measurement
   artifacts only in the base Task 2(d) kinds; the three new record files whole-file additions; entry 192 a record file of this line (its content is not
   proved). Otherwise → STOP, no push.

**Push:** `git push origin master`. Never `--force`. A failure is reported verbatim, with no retry by other options.

At the foot of the chat reply: this report's path, this dispatch's blob identity, the three commit hashes, the push
result.

## DECLARED BY THE WRITING SIDE

- **Checked at the files this sitting:** the commit-two report whole; `.git/refs/heads/master` reads
  `54804de49ac593b532e804bcfb881366e3a018b5`; `gen_specification_document_set.py` line 817.
- **Relayed, not checked:** the capture blob identities and the field-by-field equality of the eleven entries, from the
  commit-two report.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

Those of the base and resume dispatches, plus any Task 0 mismatch, any excluded path staged, and **any instruction
here found false at the objects.** On any STOP: undo nothing; report the captures and every commit hash; stop.
