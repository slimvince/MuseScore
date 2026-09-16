# CC INSTRUCTION — commit and push the uncommitted reading-pass and Cowork record files, 2026-09-16

**THE BASE.** The current commit should be `0f69cc6b79610c962a8400cdaba3dfc12facfe55` on branch `master`.
**Check this first (Task 0(b)).**

**WHY THIS EXISTS, IN ONE PARAGRAPH.** Since that commit, Cowork sittings have written paper extracts,
second extracts, handoff entries, ruling records and edits to the reading-pass progress record straight
to disk, and no batch has committed them. **If the disk fails, they are lost.** The user ordered on
2026-09-16 that they be committed and pushed to the remote as a backup. **This batch is a backup and
nothing else: it commits files as they stand on disk, and it changes the content of no file except the
report it writes.**

**WHAT THE WRITING SIDE CHECKED BEFORE WRITING THIS, AT THE OBJECTS.** `.git/HEAD` reads
`ref: refs/heads/master`. `.git/refs/heads/master` reads the commit above. `.git/config` names remote
`origin` at `https://github.com/slimvince/MuseScore`, with `master` tracking `origin/master`, and a
remote `upstream` whose `pushurl = disabled`. `.gitignore` carries `docs/research_papers/**/*.pdf`
under the comment *"Research-paper library binaries: git home is the private repo
(slimvince/research-papers), never this public fork."* **The writing side ran no git command; nothing
about which paths are tracked, modified or untracked is known to it.** That is why Task 0 measures it.

**The writing side does not touch this file, or any file this batch commits, while the batch runs.**

---

## PREMISES — DECLARED UNESTABLISHED; check each and report either way

1. The current commit is the one above, on `master`. **Not so → STOP.**
2. `origin` is `https://github.com/slimvince/MuseScore`. **Not so → STOP.**
3. **The shape expected** (a shape, not a count): the changed and untracked paths lie mainly under the
   ALLOWED SET below. Paths outside it may exist; they are **reported, not committed, and not a STOP**
   unless a STOP condition below names them.
4. `reading_pass/` already has tracked files at the current commit (so its content has been published
   to `origin` before). **Check with `git ls-files reading_pass`** (the first few lines suffice). If
   `reading_pass/` has NO tracked file at all → **STOP before committing anything, and report**,
   because the commit would be that directory's first publication to a public repository, and that is
   the user's call, not this batch's.

---

## THE ALLOWED SET — the only paths this batch may stage

- At the repository root: files matching `cowork_*.md`, `cc_instruction_*.md` and `cc_report_*.md`.
- Everything under `reading_pass/`.
- Everything under `ratification_surfaces/`.

**Never stage anything under `docs/research_papers/`**, whatever its extension, and do not open any file
there. **Never stage anything under `src/`, `tools/`, `decisions/` or `open_items/`**, and never
`CLAUDE.md`, `DECISIONS.md`, `STATUS.md`, `ARCHITECTURE.md`, `OPEN_ITEMS.md` or `BUILD_AND_TEST.md`.
If any of those shows a change, **report its path and change type only.**

---

## TASK 0 — the start state, and pinning

**(a)** Pin this dispatch: `git hash-object -w cc_instruction_backup_commit_and_push_2026_09_16.md`.
Record the blob identity in the report, and take every later read of this dispatch from
`git cat-file blob <that identity>`.

**(b)** Answer premises 1 and 2 with `git rev-parse --abbrev-ref HEAD`, `git rev-parse HEAD` and
`git remote -v`.

**(c)** Enumerate: `git status --porcelain=v1 --untracked-files=all`. **Keep the whole output for the
report; write it to no file.** Split every path into three lists: **inside the ALLOWED SET**,
**outside it**, and **deleted or renamed** (any `D` or `R` entry).

**(d)** Answer premise 4.

**(e)** **Corruption check** on every path in the ALLOWED-SET list: the file must be non-empty and must
contain no NUL byte (in PowerShell, for example, `([System.IO.File]::ReadAllBytes($p) -contains 0)` must
be `False`; any equivalent that reads the bytes is fine). **Any NUL byte or any empty file →
STOP and report the paths.** Also report every file larger than 5 MB in that list; **any file larger
than 50 MB → STOP.**

**(f)** **Size check on the three files the last Cowork sitting landed.** The expected size of each, in bytes, is:
- `reading_pass/extracts/och-2003-minimum-error-rate-training-in-statistical-machine-translation.md` — **53513**
- `reading_pass/extracts_second_pass/och-2003-minimum-error-rate-training-in-statistical-machine-translation.md` — **50903**
- `cowork_handoff_entry_one_hundred_and_eighty_eight.md` — **12349**

**A different size is not a STOP** (the device bridge that wrote them has been seen to land stale bytes).
**Report each size found against the figure above.**

---

## TASK 1 — commit

**(a)** Stage **exactly** the ALLOWED-SET list from Task 0(c), by explicit path, **modified and untracked
alike**. **Do not use `git add -A`, `git add .` or any glob that reaches outside the list.** Do not stage
deletions or renames; report them.

**(b)** Before committing, run `git diff --cached --name-status` and check that every staged path is in
the ALLOWED-SET list and nothing else is staged. **Any path outside it → unstage everything and STOP.**

**(c)** Commit **verbatim — edit, reformat, re-wrap and normalise nothing**, with this message:

```
Back up uncommitted reading-pass and Cowork record files (user-ordered, 2026-09-16)

Commits, as they stand on disk, the paper extracts, second extracts, handoff entries,
ruling records and reading-pass edits uncommitted at 0f69cc6b. No file content changed.
Dispatch: cc_instruction_backup_commit_and_push_2026_09_16.md
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

**(a)** Write `cc_report_backup_commit_and_push_2026_09_16.md` with:
- the pinned blob identity;
- premises 1 to 4, each answered;
- the whole Task 0(c) enumeration, in its three lists, **every path named**;
- the corruption check result, and the three sizes from Task 0(f) against their figures;
- the commit identity and the `git diff --cached --name-status` output from Task 1(b);
- the push result, and the two identities from Task 2.

**Assert no count of your own acts anywhere in it; name the members.**

**(b)** Commit that report alone (message: `Report: backup commit and push, 2026-09-16`), then
`git push origin master` under the same rules as Task 2, and record the new `HEAD` and `origin/master`
at the foot of your chat reply (not in the committed report, which cannot contain its own commit).

---

## DECLARED BY THE WRITING SIDE, SO THE BATCH IS NOT CAUGHT BETWEEN TWO INSTRUCTIONS

- **No `STATUS.md` entry, no forward-bound re-aiming and no regeneration of any `tools/audit/` artifact
  is ordered.** This batch changes the content of no file except its own report. The report and the
  commit are its record. If you judge that a standing rule you read at session start still requires a
  `STATUS.md` entry, **STOP and report the rule by name and file location rather than writing one.**
- **No guard set is run.** Nothing measured moves, because no file content changes.
- The ordinary session-start read still binds you (P-1, D-230).

---

## STOP CONDITIONS

- Premise 1, 2 or 4 fails.
- Any NUL byte, any empty file, or any file over 50 MB in the ALLOWED-SET list.
- Any staged path outside the ALLOWED-SET list at Task 1(b).
- Any push rejected.
- **Any instruction here found false at the objects.** A premise that does not hold is a STOP and a
  report, never something to work around.

## WHAT THIS BATCH MAY NOT DO

It may not edit the content of any file except its own report, and may not delete any file. It may not stage anything outside the ALLOWED SET, open any file
under `docs/research_papers/`, create, flip or discard any open-items row, write any decisions-register
entry, touch `src/`, build, test, or measure anything. **It may not force-push, pull, merge or rebase.**
