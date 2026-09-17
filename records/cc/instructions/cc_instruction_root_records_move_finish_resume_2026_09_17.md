# CC INSTRUCTION — resume the move finish from its Task 2 stop: skip the three passage-protection tools, commit, prove, close, push, 2026-09-17

**THE BASE.** Branch `master`, commit `5d24edb565b2e0e9efc92e082c163112bd97087f`, with the uncommitted working tree
that the third-issue run of `records/cc/instructions/cc_instruction_root_records_move_finish_2026_09_17.md` left when
it stopped in Task 2(a). **That dispatch is the base text of this one.** Read it from its pinned blob,
`git cat-file blob a16402ac47ed9f07de68629f299b65fd71eee51e` (the identity the third run recorded), never from the
working tree. Its route rule, its Task 2(d) allowed and barred kinds, its Task 3 and its Task 4 bind here **except
where this dispatch names a change.** Also read whole before Task 0: its third run's report,
`records/cc/reports/cc_report_root_records_move_finish_third_2026_09_17.md`.

**WHY THIS EXISTS.** The third run completed Task 1 and the first three write modes of Task 2, then stopped on the
fourth: `gen_claude_md_finer_archive.py` exits 1 because a reconciliation that counts ruled `CLAUDE.md` passages by
their exact wording at a pinned commit turned `false`; the previous batch had changed moved-file names inside those
passages to `records/…` paths. `gen_post_split_archive.py` and `gen_claude_md_prune_backlog.py` import the same
passages and count them the same way. **The user ruled on 2026-09-17 (Alternative A of the writing side's surface):
finish and push now, leave these three checks failing and reported, and settle the tools as a separate question after
the push.** No tool is changed and no passage is edited by this batch.

**The writing side does not touch this file while the batch runs (D-251).** **Do not undo the moves or any earlier
edit.**

**★ SECOND ISSUE.** The first run of this dispatch (blob `6e243168ba6c1b246f11ca4b7223df158ea1d5f8`) stopped at Task
2(c), before any commit; its report is `records/cc/reports/cc_report_root_records_move_finish_resume_2026_09_17.md`.
`gen_period_stratum_split.py --check` passed in the reference run and now fails. The tool reads
`tools/audit/specification_document_set.json`, which this line of work regenerated, and records that file's sha256
(line 409); with no argument it writes only `tools/audit/period_stratum_split.json` (lines 606–607). **That is the same
class as the six regenerated guards — an artifact made stale by a regenerated input — and not the class of the three
passage-protection checks the user ruled to leave failing.** So its write mode is added below as step 4, and its
artifact is proved under the base Task 2(d) kinds like the others. The writing side's defect: the guard lists named
only guards failing in the reference run and not those downstream of a regenerated artifact. **Start again from
Task 0.** Tasks 0(d), 2(a), 2(b), 2(c) and Task 3 are corrected below, former wordings kept.

**★ THIRD ISSUE.** The second issue's run (blob `de276440b3a2eb8392353019dd4b9f375a79c760`) ran all four write modes
and stopped at Task 2(b) on one unallowed new record,
`records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_two.md`, which the writing side landed while the
batch ran — **the writing side's defect**. Its report is
`records/cc/reports/cc_report_root_records_move_finish_resume_second_2026_09_17.md`. **That entry is a record file of
this line of work, the same class as entries 189–191, so it is allowed and Commit 2 adds it.** The writing side lands
nothing further in the repository while this batch runs. **Start again from Task 0.** Tasks 0(d), 2(b) and Task 3 are
corrected below, former wordings kept.

---

## TASK 0 — the resume state

**(a)** `git hash-object -w` on this dispatch. Record the identity.

**(b)** `git rev-parse --abbrev-ref HEAD` and `git rev-parse HEAD`: `master` at
`5d24edb565b2e0e9efc92e082c163112bd97087f`, else STOP.

**(c)** `python tools/audit/changed_paths.py --staged`, captured and given a blob identity: it must be
`4e959e003bbdd5b51e336ee669bd761eba00d7fc`, else STOP.

**(d)** `python tools/audit/changed_paths.py`, captured and given a blob identity. Compare with the third run's stop
capture, `git cat-file blob ba44a2c7eb0ee53a938a8e804c39bb60976ba56b` (the second-issue run, Task 2(b)). **The only
new record allowed** is an untracked record for that run's report
(`records/cc/reports/cc_report_root_records_move_finish_resume_second_2026_09_17.md`). *(Third issue. Second-issue
wording: "`git cat-file blob 654f881a31adf153ae8e4a5af7c0617e7e49dce5` (the first run of this dispatch, Task 2(b)).
The only new record allowed is an untracked record for that run's report
(`records/cc/reports/cc_report_root_records_move_finish_resume_2026_09_17.md`).")* A difference only under
`scratch_artifacts/` is reported, not a STOP. Anything else → STOP. *(Second issue. Former wording: "capture,
`git cat-file blob 4073a73b34614995f321edbf259a76bf3278140e`. The only new records allowed are untracked records for
the third run's report (…`finish_third_2026_09_17.md`) and this dispatch.")*

**Read every capture with Read or Grep. No shell command reads any file. Add no command of your own.**

---

## TASK 1 — not re-run

The base dispatch's Task 1 is done (third report §3). Do not repeat it. Its edits are proved in Task 3's content proof.

## TASK 2 — the remaining write modes

**(a)** The base dispatch's first three write modes are done (third report §4). **Do NOT run, in any mode other than
`--check`:** `gen_claude_md_finer_archive.py`, `gen_post_split_archive.py`, `gen_claude_md_prune_backlog.py`.
Run these three write modes, in this order, each followed by its own `--check`, under the base dispatch's Task 2(a)
rules (a STOP printed or a non-zero exit → STOP):
1. `python tools/audit/gen_session_start_read_size.py`
2. `python tools/audit/gen_defense_share.py`
3. `python tools/audit/gen_derivation_boot_pack.py` (never `--subject`)
4. `python tools/audit/gen_period_stratum_split.py` *(added in the second issue)*

**Steps 1–4 already ran in earlier runs of this dispatch and their artifacts are on disk. Run all four again anyway,
in order** *(third issue; second-issue wording: "Steps 1–3 already ran in the first run … Run them again anyway, in
order")*, so this
run's Task 2(b) and 2(c) rest on its own acts; a re-run that changes their artifacts again is reported, not a STOP,
provided their `--check` passes.

**(b)** `python tools/audit/changed_paths.py`, captured. Against Task 0(d), **no new record is allowed** — all four
artifacts are already modified in that capture. *(Third issue. Second-issue wording: "the only new changed record
allowed is `tools/audit/period_stratum_split.json`.")* *(Second issue. Former wording: "the only changed records allowed are
`tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json` and
`tools/audit/derivation_boot_pack.json`" — those three are already modified in the Task 0(d) capture.)*
**Any change under `tools/audit/derivation_boot_pack/` → STOP.** Anything else → STOP.

**(c)** `python tools/audit/gen_guard_state.py --check`, captured whole. Compare with the reference run,
`git cat-file blob d3774d3735639fcf8a604ee5d357a94933f2305f`, guard by guard:
- these six, which failed in the reference run, must now PASS: `gen_discard_records.py --check`,
  `gen_specification_document_set.py --check`, `gen_rulings_sort.py --check`, `gen_session_start_read_size.py --check`,
  `gen_defense_share.py --check`, `gen_derivation_boot_pack.py --check`; and `gen_period_stratum_split.py --check`
  must PASS *(second issue)*;
- these three stay FAILING, which is allowed: `gen_claude_md_finer_archive.py --check`, `gen_post_split_archive.py
  --check`, `gen_claude_md_prune_backlog.py --check`. Record each one's message; for the finer-archive tool, record
  which reconciliation lines print `False`;
- every other guard's result equals the reference run's.

Otherwise → STOP.

---

## TASK 3 — commit, prove, close, push (the base dispatch's Task 3, with these changes)

- **Commit 1** as in the base: the index as it stands, no `git add` before it, no `-a`.
- **Commit 2** as in the base, with two changes:
  - **Do NOT add `tools/audit/claude_md_finer_archive.json`.** Its working-tree copy was rewritten by the stopped
    write mode and records a `false` reconciliation; it stays uncommitted and unrestored. Confirm with
    `changed_paths.py --staged` before committing that it is not staged.
  - Add this dispatch, and every file Glob finds at
    `records/cc/reports/cc_report_root_records_move_finish*_2026_09_17.md` (all earlier runs' reports; this run's own
    report does not exist yet at Commit 2), **and `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_two.md`**
    *(third issue)*.
  The three pre-existing edits stay excluded exactly as the base says.
- **The content proof** as in the base. Task 2 artifacts are those regenerated in the third run and in Task 2(a) here
  (including `tools/audit/period_stratum_split.json`), plus `ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md`;
  the base Task 2(d) kinds apply to them.
- **The report (Task 4)** goes to `records/cc/reports/cc_report_root_records_move_finish_resume_third_2026_09_17.md`
  (Glob first; if it exists → STOP before writing). *(Third issue. Former paths: `…_finish_resume_2026_09_17.md` and
  `…_finish_resume_second_2026_09_17.md`, now earlier runs' reports, which Commit 2's pattern adds.)* It carries this batch's captures, identities, comparisons, Commits 1
  and 2 and the proof, and **a section naming the three failing checks, their messages, and the cause as the third
  report §0 derives it, labelled as derived and not measured per passage.**
- **Commit 3** as in the base, steps 1–6. The `STATUS.md` entry is a pointer to this report and to the base's reports
  and **names the three checks left failing by the user's ruling of 2026-09-17**, restating no figure (D-431). In step
  4 the guard results must equal Task 2(c)'s here.
- **Push** as in the base: `git push origin master`, never `--force`; a failure is reported verbatim.

At the foot of the chat reply: the report path, this dispatch's blob identity, the three commit hashes, the push
result.

---

## DECLARED BY THE WRITING SIDE

- **What this batch's orders move:** the three measurement artifacts of Task 2(a); the git object store; three commits
  and one push; `STATUS.md`, `STATUS_ARCHIVE.md` and `gen_status_batch_bound.py` through the forward bound; the two
  measurement artifacts again at the close; the new report. **No tool source other than the forward bound's re-aiming,
  no `CLAUDE.md` passage, no `src/` file.**
- **Checked at the files this sitting:** the third run's report whole; `gen_claude_md_finer_archive.py` at the
  reconciliation lines (461, 463) and its pin constants; `gen_post_split_archive.py` at its import of the finer-archive
  tool and its live-count checks (lines 441–444, 487, 504); `gen_claude_md_prune_backlog.py` at its import and its
  live-count checks (lines 487, 570); the base dispatch as landed (24,430 bytes).
- **Not established:** which of the four refused passages fail the count, and whether the post-split and prune-backlog
  checks fail on the same passages. Task 2(c) records the messages; nothing here depends on the per-passage answer.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

The base dispatch's, plus: running any of the three skipped tools in a write mode; adding
`tools/audit/claude_md_finer_archive.json` to any commit; a Task 0(d) or Task 2(b) difference outside what is allowed;
a Task 2(c) result other than the stated pattern; **any instruction here found false at the objects.** On any STOP: do
not undo anything; report the captures and any commit hashes; stop.
