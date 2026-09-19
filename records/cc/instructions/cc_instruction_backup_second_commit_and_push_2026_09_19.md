# CC INSTRUCTION — the second backup: commit and push fifteen named record files uncommitted at 5c95032de1, by explicit path, 2026-09-19

**THE BASE.** Branch `master` at **`5c95032de157aff105c2c2abefce2c87cbb95cab`** (the close commit of the
passage-guards batch, pushed; `origin/master` equal — both read at the ref files by the writing side on
2026-09-19).

**WHY THIS EXISTS.** Cowork sittings have landed second extracts, corrected first extracts and handoff entries
straight to disk, and no batch has committed them; three members of THE LIST (1, 13 and 14) were already modified
and uncommitted when the previous batch ran, as its report §2(d) records. **If the disk fails, they are lost.** The user
ordered on 2026-09-16 that such files be committed and pushed as a backup (*"we need to instruct CC to commit and
push all our extracts etc. Otherwise they will be lost if my disc crashes"*, recorded at
`records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_eight.md` §5, which also recommends this second
backup). **This batch is a backup and its own close, and nothing else: it commits the files THE LIST below names,
as they stand on disk; it writes its own report (Task 2); and it changes the content of no existing file except
the ones its close orders by name (Task 3: `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`
and the three generated artifacts named there).**

**The writing side does not touch this file, or any file on THE LIST, and lands nothing in the repository, while
the batch runs (D-251).**

## THE ROUTE RULE

- **No shell command reads any file** — not `cat`, `head`, `tail`, `type`, `Get-Content` or any other, and not in the
  scratchpad. Read every capture with Read or Grep.
- Every capture: written to the scratchpad, given an identity with `git hash-object -w`, read with Read or Grep.
- Take a commit hash from the `git commit` command's own printed output (no `-q`, no redirect). **One exception,
  ordered here so it is not a departure:** `git rev-parse HEAD` is run once immediately after the task commit
  (Task 1(d)) to expand its hash to forty characters, and once after the close commit (Task 3.6).
- **Add no command of your own.** Any guard refusal → STOP.
- Edit files with the Edit file tool only. **No file on THE LIST is edited, opened for editing, re-saved or
  normalised.** They are committed as they stand.

## THE LIST — the only paths this batch may stage at its task commit

Each line gives the path and **the size in bytes the writing side read on 2026-09-19** (at a folder listing or at a
staging result of the landed copy).

Handoff entries, under `records/cowork/handoff/`:
1. `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_eight.md` — **19822**
2. `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_four.md` — **9612**
3. `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_five.md` — **9423**
4. `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_six.md` — **14528**
5. `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_seven.md` — **19704**
6. `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_eight.md` — **29235**

First extracts, corrected at their own sites on the user's rulings, under `reading_pass/extracts/`:
7. `reading_pass/extracts/lafferty-mccallum-pereira-2001-conditional-random-fields-for-segmenting-and-labeling-sequence-data.md` — **65051**
8. `reading_pass/extracts/sha-pereira-2003-shallow-parsing-with-conditional-random-fields.md` — **26213**
9. `reading_pass/extracts/burgoyne-pugin-kereliuk-fujinaga-2007-a-cross-validated-study-of-modelling-strategies-for-automatic-chord-recognition-in-audio.md` — **54368**

Second extracts, under `reading_pass/extracts_second_pass/`:
10. `reading_pass/extracts_second_pass/lafferty-mccallum-pereira-2001-conditional-random-fields-probabilistic-models-for-segmenting-and-labeling-sequence-data.md` — **40212**
11. `reading_pass/extracts_second_pass/sha-pereira-2003-shallow-parsing-with-conditional-random-fields.md` — **42082**
12. `reading_pass/extracts_second_pass/burgoyne-pugin-kereliuk-fujinaga-2007-a-cross-validated-study-of-modelling-strategies-for-automatic-chord-recognition-in-audio.md` — **59210**

The two modified text files the first backup's exclusion left out (entry 188 §5), under `docs/research_papers/`:
13. `docs/research_papers/BIBLIOGRAPHY.md` — **18081**
14. `docs/research_papers/README.md` — **8382**

And this dispatch:
15. `records/cc/instructions/cc_instruction_backup_second_commit_and_push_2026_09_19.md` — no size is given for it.

**NEVER STAGED, at the task commit or at the close:** `tools/audit/claude_md_finer_archive.json`,
`tools/audit/guard_state.json`, `tools/audit/guard_classification.json`; anything under `src/`; any `.pdf`; anything
under `docs/research_papers/` other than members 13 and 14; and any path not named in this dispatch. **Open no file
under `docs/research_papers/` other than members 13 and 14, and open nothing under
`docs/research_papers/polyph9-release/`.**

## TASK 0 — the state

**(a)** `git hash-object -w` on this dispatch. Record the identity. Every later read of this dispatch is
`git cat-file blob <that identity>`.

**(b)** `git rev-parse --abbrev-ref HEAD` and `git rev-parse HEAD`: `master` at
`5c95032de157aff105c2c2abefce2c87cbb95cab`, else STOP. `git remote -v`: `origin` must be
`https://github.com/slimvince/MuseScore` for fetch and for push, else STOP.

**(c)** `python tools/audit/changed_paths.py --staged`, captured: it must list **no path record**, else STOP.

**(d)** `python tools/audit/changed_paths.py`, captured. **The writing side holds no reference capture for this
tree** (the previous batch's closing enumeration is in no file it could read), so the comparison is by shape:
- **Each member of THE LIST is looked up in the capture.** Expected, not required: members 1, 7, 8, 9, 13 and 14
  carry a modified record (` M`); members 2 to 6, 10 to 12 and 15 carry an untracked record (`??`). **A member
  whose record is of the other kind is reported and is still staged. A member with NO record in the capture is
  reported, Glob-checked for existence, and NOT staged** (a file that exists with no record is either already
  committed as it stands or ignored; it is reported either way and no command is added to tell which). **A member
  that does not exist on disk → STOP.**
- **THE STAGING SET** is the members of THE LIST that have a record in this capture. Name them in the report.
- Every ` M` record NOT on THE LIST is named in the report. `tools/audit/claude_md_finer_archive.json` is expected
  among them (the line-ending report measured by the previous batch) and is not a STOP. **A modified, deleted or
  renamed record under `src/` → STOP** (an untracked `??` record under `src/` is reported and is not a STOP).
- Every record under `records/cowork/handoff/`, `reading_pass/` or `records/cc/` that is NOT on THE LIST is named
  in the report and is **not staged**. Records elsewhere are not listed one by one; the capture's identity stands
  for them.

**(e)** `python tools/audit/gen_guard_state.py --check`, captured whole. The run exits 1 when the failing set is
not empty, as the previous batch's report records; that exit code is not a STOP. **This capture is the reference
for Task 3.4.** Report whether it hashes to `3cf63b086a2418290b1d4f179dc5f4e9804462a6` (the previous batch's closing
capture, per its report §5 item 4); **a different identity is reported and is not a STOP** — untracked record files
may be read by a guard, and the writing side has not established that none is.

**(f) The size check, by git object and not by a shell read.** For each member of THE STAGING SET except member
15: `git hash-object -w --no-filters <path>`, then `git cat-file -s <the identity it printed>`. **The size printed
must equal the figure on THE LIST. Any difference → STOP, stage nothing, and report every size found.** (The
figures are of the bytes on disk, which is what `--no-filters` hashes. **No member's line endings were measured by
the writing side.**)

**(g) The tail check, with the Read file tool.** For each member of THE STAGING SET except members 13, 14 and 15:
Read its closing lines (a Grep count of lines matching `^` over the file gives the line count; Read from five
lines before it). **The last non-empty line must be ordinary text. A file ending in NUL bytes, or an empty
file → STOP.** Report the last non-empty line's first 60 characters for each. (This is the truncated-write check the
first backup ran with a byte read; the Read tool is the sanctioned route.)

## TASK 1 — the task commit

**(a)** Stage **exactly** THE STAGING SET, by explicit path, one `git add -- <path>` per member or one command
naming them all. **Never `git add -A`, `git add .`, `git add -u` or any glob.** A line-ending warning printed by
`git add` is reported verbatim and is not a STOP.

**(b)** `python tools/audit/changed_paths.py --staged`, captured: **exactly the members of THE STAGING SET and
nothing else.** Anything else → `git restore --staged -- <every staged path>` and STOP.

**(c)** Commit with this message, verbatim (the standing `Co-Authored-By` trailer may follow it):

```
Second backup: named record files uncommitted at 5c95032de1 (user-ordered)

Commits, as they stand on disk, the handoff entries, corrected first extracts, second
extracts and the two research-paper index files uncommitted at 5c95032de1. No file
content changed by this commit.
Dispatch: records/cc/instructions/cc_instruction_backup_second_commit_and_push_2026_09_19.md
```

**(d)** Record the hash `git commit` printed, then `git rev-parse HEAD` once; the forty characters it prints must
begin with the printed hash, else STOP. That forty-character value is the **TASK COMMIT**.

## TASK 2 — the report

Write with the Write file tool `records/cc/reports/cc_report_backup_second_commit_and_push_2026_09_19.md` (Glob
first; if it exists → STOP). It carries: this dispatch's blob identity; Task 0(b) and (c); Task 0(d)'s capture
identity, THE STAGING SET by name, each member's record kind against the expected kind, every ` M` record not on
THE LIST, and every record under the three named directories not on THE LIST; Task 0(e)'s capture identity and
whether it equals the previous closing capture; every size from Task 0(f) against its figure; every tail line from
Task 0(g); Task 1(a)'s output including any warning verbatim; Task 1(b)'s capture; the task commit. Name members;
state a total only as a sum of named members or a figure a tool printed (D-431).

## TASK 3 — the close and the push

As the previous batch's close (`records/cc/instructions/cc_instruction_passage_guards_historical_2026_09_17.md`
Task 4, as run and described in `records/cc/reports/cc_report_passage_guards_historical_2026_09_17.md` §5), with
ONE forward-bound move, not two. Read that report's §5 before starting.

1. **The `STATUS.md` entry**, written first, at the top of the dated entries, in the file's pointer convention,
   taking the `Last updated: ` prefix, with the previous batch's entry demoted to a plain dated entry in the same
   edit (as that report's §5 item 1 describes). It names this dispatch; says that this batch is a backup commit of
   record files by explicit path, on the user's order of 2026-09-16 recorded at handoff entry 188 §5; says that no
   file content was changed by the task commit; and points at this batch's report. It restates no figure.
2. **The forward bound — ONE ordinary move.** Read `tools/audit/gen_status_batch_bound.py`'s docstring and its whole
   comment block above `PREVIOUS_AIMINGS` before editing. Re-aim: `BASE_COMMIT` = the TASK COMMIT (forty
   characters); `PREVIOUS_BATCH_DISPATCH = "cc_instruction_passage_guards_historical_resume_2026_09_17.md"` (the
   previous batch's `STATUS.md` entry names both that file and the original dispatch it resumed);
   `ACT_DATE` = the day this runs; `DISPATCH = "cc_instruction_backup_second_commit_and_push_2026_09_19.md"`;
   `TASK = "Task 3"`; `MOVE_KIND = "ordinary"`. Append the replaced aiming to `PREVIOUS_AIMINGS` (#12) and extend
   the authored comments as the tool's own conventions require. Then `--apply`, then
   `python tools/audit/gen_status_batch_bound.py --check` must exit 0.
   **If the move cannot be performed as the docstring and the precedent describe:** run
   `git restore --source=HEAD --worktree -- STATUS.md STATUS_ARCHIVE.md tools/audit/gen_status_batch_bound.py
   tools/audit/status_batch_bound.json`, write this batch's `STATUS.md` entry again exactly as in step 1 with one
   added sentence saying the bound was not performed and why, skip the bound, and report the tool's message
   verbatim. That is not a STOP.
3. `python tools/audit/gen_session_start_read_size.py`, then `python tools/audit/gen_defense_share.py`. Any STOP or
   FAIL printed → STOP, no commit.
4. `python tools/audit/gen_guard_state.py --check`, captured: every guard's result equal to Task 0(e)'s capture,
   else STOP (no commit, no push).
5. **Close commit, by explicit path only:** `STATUS.md`; `tools/audit/session_start_read_size.json`;
   `tools/audit/defense_share.json`; this batch's report; and **if the bound ran**, `STATUS_ARCHIVE.md`,
   `tools/audit/gen_status_batch_bound.py` and `tools/audit/status_batch_bound.json`. Check with
   `changed_paths.py --staged` before committing: exactly those. Message:
   `Close: second backup commit and push, 2026-09-19`.
6. `git rev-parse HEAD` once, for the close commit's forty characters. Then `git diff <TASK COMMIT> <close commit>`:
   changes only in the close commit's paths; the two measurement artifacts only in values that follow from
   `STATUS.md` changing (and `STATUS_ARCHIVE.md`, if the bound ran); the report a whole-file addition. Otherwise →
   STOP, no push.

**Push:** `git push origin master`. Never `--force`, never `--force-with-lease`, never to `upstream`, no other
branch. A failure is reported verbatim, with no pull, merge, rebase or retry by other options.

At the foot of the chat reply: the report's path, this dispatch's blob identity, THE STAGING SET by name, the task
commit and close commit hashes, whether the bound ran, and the push result verbatim.

## DECLARED BY THE WRITING SIDE

- **Checked at the files on 2026-09-19:** both ref files read `5c95032de157aff105c2c2abefce2c87cbb95cab`;
  `.git/HEAD` reads `ref: refs/heads/master`; `.git/config` names `origin` at
  `https://github.com/slimvince/MuseScore` and `upstream` with `pushurl = disabled`; `.gitignore` carries
  `docs/research_papers/**/*.pdf`; the sizes on THE LIST — members 1 to 5, 7, 8, 10, 11, 13 and 14 at folder
  listings, members 6, 9 and 12 at the staging results of their landed copies; members 6, 9 and 12 proved at content
  and at their last line after landing; `tools/audit/gen_status_batch_bound.py` at its authored constants (lines
  340–407: `BASE_COMMIT`, `PREVIOUS_BATCH_DISPATCH`, `ACT_DATE`, `DISPATCH`, `TASK`, `MOVE_KIND`) and at the line that
  selects entries by `PREVIOUS_BATCH_DISPATCH in line`; `STATUS.md` whole, whose newest entry names both the
  passage-guards dispatch and its resume; the previous batch's two dispatches and its report whole; the first
  backup's dispatch whole and its report at lines 1–108.
- **Relayed, not checked:** that the base is the passage-guards batch's close commit and that it was pushed
  (handoff entry 194 §0, which relays the push line from CC's chat reply; what the writing side checked is that
  both ref files carry that value); which members of THE LIST are tracked. The expectation at Task 0(d) rests on the first
  backup's report (every path under `reading_pass/` was then an addition) and on the previous batch's report §2(d)
  (members 1, 13 and 14 were ` M` records then, member 2 was not yet on disk). That handoff entries 189 to 193 are
  already committed is relayed from the handoff entries and from that report's §4(c) for entry 193; Task 0(d)
  reports any that are not. **What members 13 and 14's modifications contain was not read by the writing side.**
- **Not established:** whether any guard reads an untracked record file (Task 0(e) reports it); the line endings
  of every member (Task 0(f) measures bytes, and Task 1(a) reports any warning).
- **Not in this batch, named so the omission is not mistaken for a miss:** the CC report family, the root
  `cowork_*.md` documents, `tools/audit/derivation_exemplars/`, `Claude outputs/`, `Codex research inventory/`,
  `scratch_artifacts/`, `external resarch summary/`, `docs/research_papers/polyph9-release/` and the stray duplicate
  `reading_pass/extracts/lafferty-mccallum-pereira-2001-conditional-random-fields-for-segmenting-and-labeling-sequence-data-1.md`.
  **The writing side did not establish their present paths or tracked state** (the root records move of
  2026-09-17 ran after entry 188 was written). Entry 188 §5 recommended two of them for this backup — the CC report
  family and `tools/audit/derivation_exemplars/` — and they **remain owed to a later backup**; the same section
  holds the others back until the user says whether they belong in a public fork. Task 0(d)'s capture is what a
  later dispatch will be written from.
- **No decisions-register entry is written by this batch, and no open-items row is created, flipped or
  discarded.** The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

Any Task 0(b) or 0(c) mismatch; a member of THE LIST missing from disk; a changed record under `src/`; any size
different from its figure; any tail that is not ordinary text; any staged path outside THE STAGING SET; any guard
refusal; any Task 3 STOP; any push rejected; **any instruction here found false at the objects.** On any STOP: undo
nothing beyond the unstaging Task 1(b) orders; report the captures and every commit hash; stop.
