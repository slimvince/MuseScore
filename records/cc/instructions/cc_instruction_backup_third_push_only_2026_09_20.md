# CC INSTRUCTION — push the third backup's task commit, and nothing else, 2026-09-20

**What this is.** The third backup's task commit `4d248dd096f0960021e622160a962d48476b8eb5` exists on
`master` on the user's disk and has not been pushed: the batch that made it stopped at its close's guard step
(`records/cc/reports/cc_report_backup_third_commit_and_push_2026_09_20.md` §8(b)). The user ruled on
2026-09-20 that the push is taken on its own, before the close is finished. **This dispatch pushes that
commit and does nothing else.** The close — the `STATUS.md` entry, the forward bound, the two measurement
artifacts and that report, all standing uncommitted in the working tree — is a LATER dispatch's work and is
not touched here beyond the one sentence Task 3 orders.

## THE ROUTE RULE

- **Make no commit. Stage nothing.** `git add`, in any form, is forbidden in this batch.
- Run **no guard set, no generator, no forward bound, no build, no test, no measurement**.
- **Add no command of your own.** Any guard refusal → STOP.
- Working-tree file content is read and written with the file tools, never through a shell (`D-253`).
- The ordinary session-start read still binds you (P-1, `D-230`).

## TASK 0 — the state, before anything is pushed

**(a)** `git rev-parse --abbrev-ref HEAD` must print `master`, else STOP.

**(b)** `git rev-parse HEAD` must print exactly

```
4d248dd096f0960021e622160a962d48476b8eb5
```

**Any other value → STOP.** Report the value printed and do nothing further. That value is THE TASK COMMIT,
and this dispatch pushes the branch only while the branch tip still is it.

**(c)** `git remote -v`. `origin` must be `https://github.com/slimvince/MuseScore` for **fetch** and for
**push**, and `upstream`'s push must be disabled, else STOP. *(Checked by the writing side at `.git/config`
on 2026-09-20: `origin` carries that one url and no separate push url; `upstream` carries
`pushurl = disabled`.)*

**(d)** `python tools/audit/changed_paths.py --staged`, captured. It must list **no path record** — the
previous batch staged nothing after its task commit. **Any staged record → STOP**, unstage nothing, and
report the capture whole.

## TASK 1 — the push

`git push origin master`. **Capture the whole output and report it verbatim.**

- Never `--force`, never `--force-with-lease`, never `upstream`, no other branch, no other refspec, no
  `--tags`.
- **If the push is rejected, or fails for any reason: report the output verbatim and STOP.** No pull, no
  fetch, no merge, no rebase, no retry with other options, and no second push.

## TASK 2 — the proof, at the object

`git rev-parse refs/remotes/origin/master` must print `4d248dd096f0960021e622160a962d48476b8eb5`. Report
what it prints. **A different value → report it and STOP** — the report's §3 then says so, and nothing else
is done. *(The writing side verifies this independently at `.git/refs/remotes/origin/master` with the file
tools.)*

## TASK 3 — the one sentence the push makes false in `STATUS.md`

`STATUS.md`'s topmost entry says of the previous batch that **nothing was pushed**. After Task 1 that
sentence is false about the state of the repository, and #10 forbids the record stating something false
about itself. **ONE edit, with the file tools, and only this one.**

**Find this text, which stands exactly once in the file:**

```
still open; nothing was undone.
```

**Replace it with exactly:**

```
still open; nothing was undone. ★ **AND THE TASK COMMIT WAS PUSHED AFTERWARDS, ON ITS OWN, BY `records/cc/instructions/cc_instruction_backup_third_push_only_2026_09_20.md`** — a dispatch that pushed and did nothing else, on the user's ruling of 2026-09-20 that the push is taken before the close is finished. The two sentences above stand as written of the batch they describe (#12), and **the close commit is still owed**: this file's entry, the forward bound, the two measurement artifacts and both batches' reports remain uncommitted.
```

Nothing else in `STATUS.md` changes: no entry is demoted, moved, archived or re-dated, the `Last updated: `
prefix stays where it is, and the forward bound is NOT run. **If that text is not found, or is found more
than once → STOP**, edit nothing, and report what was found.

## TASK 4 — the report

`records/cc/reports/cc_report_backup_third_push_only_2026_09_20.md`. **If it already exists → STOP.**
Short. It carries, in this order:

1. This dispatch's blob identity, from `git hash-object -- records/cc/instructions/cc_instruction_backup_third_push_only_2026_09_20.md`.
2. Task 0's four results, each as the command printed it.
3. Task 1's output **verbatim**, whole.
4. Task 2's value.
5. Task 3's edit: the text found, the text written, and that it stood exactly once.
6. What was not done: no commit, nothing staged, no guard set, no generator, no forward bound, no other
   edit to any file.

**This report is itself uncommitted**, as is the Task 3 edit — this batch makes no commit. The later close
dispatch commits both.

## THE FOOTPRINT

**Pushed:** the existing task commit, unchanged. **Edited:** `STATUS.md`, at the one site Task 3 names.
**Created:** this batch's report. **Nothing else** — no commit, no staging, no `src/` file, no build, no
test, no golden, no corpus, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement of the
analysis, no paper opened, no extract edited, no tool source edited, no open-items row created, flipped or
discarded, no decisions-register entry and no `D-NNN` allocated.

## DECLARED BY THE WRITING SIDE

- **Checked at the files on 2026-09-20, by the writing side, with the file tools:**
  - `.git/refs/heads/master` reads `4d248dd096f0960021e622160a962d48476b8eb5`;
  - `.git/refs/remotes/origin/master` reads `f6b9fadc58cdff4e97364abb1c70deda7213243c`, so the task commit
    is unpushed;
  - `.git/config`'s `origin` url, and `upstream`'s disabled push url;
  - `STATUS.md`'s topmost entry, and that Task 3's anchor text stands there exactly once;
  - the previous batch's report whole, and this dispatch's account of its §8(b).
- **Relayed, not checked by the writing side:** everything the previous batch's report states about its
  captures, its staged set and the contents of the task commit; and that the close's edits are uncommitted.
  No shell ran on either side.
- **A consequence of pushing, stated because a commit did not have it and a push does:** the task commit
  carries 168 records under `records/cc/` — the previous batch's report §7 states that count, and the
  writing side has not counted them itself — and the push publishes them at the `origin` fork. **Whether that
  fork is public was not established by the writing side.** The user ordered these files committed and
  pushed on 2026-09-16 and read the list before hand-over; this is recorded as a consequence, not reopened
  as a question.

## STOP CONDITIONS

- Any Task 0 mismatch: a branch other than `master`, a tip other than THE TASK COMMIT, a wrong or missing
  remote url, or any staged path record.
- The push rejected or failed, for any reason.
- `refs/remotes/origin/master` not equal to THE TASK COMMIT after the push.
- Task 3's anchor text absent, or present more than once.
- The report's path already in use.
- **Any instruction here found false at the objects.**

On any STOP: undo nothing, report every capture verbatim and every value printed, and stop.
