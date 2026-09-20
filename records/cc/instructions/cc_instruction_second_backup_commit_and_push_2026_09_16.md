# CC INSTRUCTION — the second backup: commit and push what the first backup left out, 2026-09-16

**THE BASE.** The current commit should be `5d24edb565b2e0e9efc92e082c163112bd97087f` on branch `master`,
and `origin/master` should be the same commit. **Check this first (Task 0(b)).**

**WHY THIS EXISTS, IN ONE PARAGRAPH.** Earlier today `cc_instruction_backup_commit_and_push_2026_09_16.md`
committed and pushed the uncommitted reading-pass and Cowork record files as a backup against a disk
failure, and `cc_report_backup_commit_and_push_2026_09_16.md` records the run. **That dispatch's
ALLOWED SET was defective in two places, and this batch repairs the omission.** (1) Its root pattern
`cc_report_*.md` matched none of CC's session reports (by that report's own account); those reports are named `cc_<subject>_report.md`,
`cc_<subject>_dossier.md` and similar — the report says so under *"Premise 3"*, and names them in its
*"List 2 — outside the ALLOWED SET"*. (2) Its bar on everything under `docs/research_papers/` also left
out the two tracked text files that List 2 reports as modified there, `BIBLIOGRAPHY.md` and `README.md`.
**This batch is a backup and nothing else: it commits files as they stand on disk, and it changes the
content of no file except the report it writes.**

**WHAT THE WRITING SIDE CHECKED BEFORE WRITING THIS, AT THE OBJECTS.** `.git/HEAD` reads
`ref: refs/heads/master`. `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both read the
commit above. `.git/config` names remote `origin` at `https://github.com/slimvince/MuseScore`, `master`
tracking `origin/master`, and remote `upstream` with `pushurl = disabled`. `.gitignore` carries
`docs/research_papers/**/*.pdf`. `tools/audit/changed_paths.py` exists and offers the working-tree
enumeration (no flag) and `--staged`. **The writing side ran no git command and no shell command;
which paths are tracked, modified or untracked NOW is not known to it** — List 2 of the previous report
is a relay from before that report's own commit, and files have been written since. That is why
Task 0 measures it.

**The writing side does not touch this file, or any file this batch commits, while the batch runs.**

---

## PREMISES — DECLARED UNESTABLISHED; check each and report either way

1. The current commit is the one above, on `master`. **Not so → STOP.**
2. `origin` is `https://github.com/slimvince/MuseScore`, and `origin/master` equals the current commit.
   **`origin` differs → STOP. `origin/master` differs → report it; the push rules in Task 2 govern.**
3. **The shape expected** (a shape, not a count): the changed and untracked paths inside the ALLOWED SET
   below are mainly root `cc_*.md` session reports, the two `docs/research_papers/` text files, the
   members of `tools/audit/derivation_exemplars/`, and `cowork_handoff_entry_one_hundred_and_eighty_eight.md`
   (modified since the first backup). Other paths may exist; outside the set they are **reported, not
   committed, and not a STOP**.

---

## THE ALLOWED SET — the only paths this batch may stage

- At the repository root: files matching `cowork_*.md` and `cc_*.md` (this reaches `cc_instruction_*`,
  `cc_report_*` and every `cc_<subject>_*.md` alike).
- Everything under `reading_pass/` and under `ratification_surfaces/` (the first backup's set, repeated
  so anything written since is caught).
- Exactly two files under `docs/research_papers/`: `docs/research_papers/BIBLIOGRAPHY.md` and
  `docs/research_papers/README.md`.
- Everything under `tools/audit/derivation_exemplars/`, **subject to the file-type STOP in Task 0(d)**.

**HELD BACK — never stage, open, list or search:** anything under `docs/research_papers/polyph9-release/`;
any other path under `docs/research_papers/`; `external resarch summary/` (the spelling is the
directory's own); `scratch_artifacts/`. **Never stage** anything under `Claude outputs/` or
`Codex research inventory/` — **those two stand with the user**, and Task 0(e) reports their member paths
only. **Never stage** anything under `src/`, `decisions/`, `open_items/`, or under `tools/` outside
`tools/audit/derivation_exemplars/`, and never `CLAUDE.md`, `DECISIONS.md`, `STATUS.md`,
`ARCHITECTURE.md`, `OPEN_ITEMS.md` or `BUILD_AND_TEST.md`. If any of those shows a change, **report its
path and change type only.**

---

## TASK 0 — the start state, and pinning

**(a)** Pin this dispatch: `git hash-object -w cc_instruction_second_backup_commit_and_push_2026_09_16.md`.
Record the blob identity in the report, and take every later read of this dispatch from
`git cat-file blob <that identity>`.

**(b)** Answer premises 1 and 2 with `git rev-parse --abbrev-ref HEAD`, `git rev-parse HEAD`,
`git rev-parse origin/master` and `git remote -v`.

**(c)** Enumerate with the sanctioned tool, **`python tools/audit/changed_paths.py`** (no flag; **do not
pass `--json`**, which writes a file), not with `git status` (the previous run's shell-read guard refused
that, citing D-253). The tool reports an untracked DIRECTORY as one record. **For every such record that
lies inside the ALLOWED SET, enumerate its members with the Glob file tool.** Split every path into three
lists: **inside the ALLOWED SET**, **outside it**, and **deleted or renamed** (any `D` or `R` code). Keep
the enumeration for the report; if you must hold it in a file, use a session scratchpad outside
`C:\s\MS`, as the previous run did, and say so.

**(d)** **File-type STOP for `tools/audit/derivation_exemplars/`.** Name every member. **If any member's
extension is not one of `.md`, `.json`, `.py`, `.txt`, `.csv` → STOP before staging anything, and report
every member with its extension.** The reason: no member of this directory was opened by the writing side
in this sitting, and the push goes to a public repository.

**(e)** **Report, do not stage:** the member paths of `Claude outputs/` and `Codex research inventory/`,
by Glob, **without opening any file**. These are facts for a decision the user has not yet taken.

**(f)** **Corruption check** on every path in the ALLOWED-SET list, as the previous run did it and
declared it (its deviation (3)): each file non-empty and containing no NUL byte, read as bytes, and after
staging each staged blob's size read from the object store by hash and compared against the byte count
read from disk. **Any NUL byte, any empty file, or any size mismatch → unstage everything if anything is staged, STOP,
and report the paths.**
Report every file larger than 5 MB; **any file larger than 50 MB → STOP.** *(The byte read is ordered
here by the writing side, with the by-hash cross-check beside it, so it is not a deviation you need to
declare; the D-253 hazard it touches — a stale mount — is what the cross-check measures. If a guard refuses the byte read, STOP and report the refusal text.)*

**(g)** **Size check** on the file the writing side proved at a staging call this sitting:
`cowork_handoff_entry_one_hundred_and_eighty_eight.md` — **19822** bytes. **A different size is not a
STOP** (the device bridge has been seen to land stale bytes). **Report the size found against it.**

---

## TASK 1 — commit

**(a)** Stage **exactly** the ALLOWED-SET list from Task 0(c), by explicit path, **modified and untracked
alike**. **Do not use `git add -A`, `git add .` or any glob that reaches outside the list.** Do not stage
deletions or renames; report them.

**(b)** Before committing, run `python tools/audit/changed_paths.py --staged` and compare the staged set
against the ALLOWED-SET list **as a set, in both directions**. **Any staged path outside the list, or any
list path not staged → unstage everything and STOP.**

**(c)** Commit **verbatim — edit, reformat, re-wrap and normalise nothing** — with this message, followed
by the standing attribution trailer:

```
Second backup: CC session reports, research-paper text files, derivation exemplars (user-ordered, 2026-09-16)

Commits, as they stand on disk, the files the first backup's ALLOWED SET left out:
root cc_*.md session reports, docs/research_papers/BIBLIOGRAPHY.md and README.md,
tools/audit/derivation_exemplars/, and Cowork record files changed since 5d24edb5.
No file content changed. Dispatch: cc_instruction_second_backup_commit_and_push_2026_09_16.md
```

---

## TASK 2 — push

`git push origin master`. **Never `--force`, never `--force-with-lease`, never push to `upstream`, and
push no other branch.** If the push is rejected for any reason (authentication, network,
non-fast-forward): **STOP. Do not pull, merge, rebase or retry with force.** Report the exact error text.

After a successful push, record `git rev-parse HEAD` and `git rev-parse origin/master`; they must be
equal. **Not equal → report.**

---

## TASK 3 — the report, committed and pushed

**(a)** Write `cc_report_second_backup_commit_and_push_2026_09_16.md` with:
- the pinned blob identity;
- premises 1 to 3, each answered;
- the whole Task 0(c) enumeration in its three lists, **every path named**, and Task 0(d)'s and 0(e)'s
  member lists;
- the corruption check result, and the size from Task 0(g) against its figure;
- the commit identity and the `--staged` output from Task 1(b);
- the push result, and the two identities from Task 2.

**Assert no count of your own acts anywhere in it; name the members.**

**(b)** Commit that report alone (message: `Report: second backup commit and push, 2026-09-16`, with the
attribution trailer), then `git push origin master` under the same rules as Task 2, and record the new
`HEAD` and `origin/master` at the foot of your chat reply (not in the committed report, which cannot
contain its own commit).

---

## DECLARED BY THE WRITING SIDE, SO THE BATCH IS NOT CAUGHT BETWEEN TWO INSTRUCTIONS

- **What this batch's own orders move:** the git index and history (two commits), `origin/master` (two
  pushes), the git object store (the pinned blob), and one new file, its own report. **No existing file's
  content is edited.**
- **No `STATUS.md` entry, no forward-bound re-aiming and no regeneration of any `tools/audit/` artifact is
  ordered.** The previous report already named the two rules that could require an entry (under
  *"The `STATUS.md` question, reported and not acted on"*), and that question stands with the user. **If
  you judge the same or another rule requires one, name it in the report; do not write an entry, and it
  is not a STOP.**
- **No guard set is run.** No file content changes.
- The ordinary session-start read still binds you (P-1, D-230).

---

## STOP CONDITIONS

- Premise 1 fails, or `origin` is not the URL in premise 2.
- A `tools/audit/derivation_exemplars/` member with an extension outside the list in Task 0(d).
- Any NUL byte, empty file, size mismatch, or file over 50 MB in the ALLOWED-SET list, or a refused byte
  read at Task 0(f).
- Any staged path outside the ALLOWED-SET list, or any list path not staged, at Task 1(b).
- Any push rejected.
- **Any instruction here found false at the objects.** A premise that does not hold is a STOP and a
  report, never something to work around.

## WHAT THIS BATCH MAY NOT DO

It may not edit the content of any file except its own report, and may not delete any file. It may not
stage anything outside the ALLOWED SET, or open, list, stage or search anything under
`docs/research_papers/polyph9-release/`. It may not create, flip or discard any open-items row, write any
decisions-register entry, touch `src/`, build, test, or measure anything. **It may not force-push, pull,
merge or rebase.**
