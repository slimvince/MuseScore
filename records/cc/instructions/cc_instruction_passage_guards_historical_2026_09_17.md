# CC INSTRUCTION — the three passage-protection checks become historical records (Alternative A1), 2026-09-17

**THE BASE.** Branch `master` at **`49c6364242772d34c08b046d5972d5748a4d0763`** (Commit 3 of the root records move,
pushed; `origin/master` equal — both read at the ref files by the writing side).

**THE RULING THIS EXECUTES.** User, 2026-09-17, on a surface delivered in its own turn and a choice question put in a
later one: **"I agree on A1."** Recorded at `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_three.md`
§1, which carries the surface's facts and the cost the user accepted. In short:

- `tools/audit/gen_claude_md_finer_archive.py`, `tools/audit/gen_post_split_archive.py` and
  `tools/audit/gen_claude_md_prune_backlog.py` leave the guard list and are recorded as HISTORICAL — reversing their
  three LIVE verdicts in `tools/audit/gen_guard_classification.py`, with the former verdict preserved (#12).
- Their artifacts stay on disk as committed. Nothing is deleted.
- **A1, not A2:** `gen_guard_classification.py` cannot regenerate today, because two guards the runner carries have no
  authored verdict (`tools/audit/gen_l0_l1_outgoing_population.py`, `tools/audit/gen_withheld_family_reading.py`). That
  STOP is **not** repaired here and no verdict is authored for either. `tools/audit/guard_classification.json` and
  `tools/audit/guard_state.json` are **not regenerated**.
- **The cost the user accepted:** nothing now fails on the day a later act archives one of the passages these three
  tools protected.

**The writing side does not touch this file, and lands nothing in the repository, while the batch runs (D-251).**

## THE ROUTE RULE

- **No shell command reads any file** — not `cat`, `head`, `tail`, `type`, `Get-Content` or any other, and not in the
  scratchpad. Read every capture with Read or Grep.
- Every capture: written to the scratchpad, given an identity with `git hash-object -w`, read with Read or Grep.
- Take a commit hash from the `git commit` command's own printed output (no `-q`, no redirect).
- **Add no command of your own.** Any guard refusal → STOP.
- Edit files with the Edit file tool only.

## TASK 0 — the state

**(a)** `git hash-object -w` on this dispatch. Record the identity. Every later read of this dispatch is
`git cat-file blob <that identity>`.

**(b)** `git rev-parse --abbrev-ref HEAD` and `git rev-parse HEAD`: `master` at
`49c6364242772d34c08b046d5972d5748a4d0763`, else STOP.

**(c)** `python tools/audit/changed_paths.py --staged`, captured: it must list **no path record**, else STOP.

**(d)** `python tools/audit/changed_paths.py`, captured. Compare with `git cat-file blob
5b26228cdf4e874c045e01ed352a2e27d8dc3d06` (the Task 0(d) capture of the Commit-3 run, per its report). **The only
differences allowed:**
- **gone** (committed in Commit 3): the records for `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_two.md`,
  `records/cc/instructions/cc_instruction_root_records_move_finish_commit_three_2026_09_17.md` and
  `records/cc/reports/cc_report_root_records_move_finish_commit_two_2026_09_17.md`;
- **new, untracked:** this dispatch, and `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_three.md`.
A difference only under `scratch_artifacts/` is reported, not a STOP. Anything else → STOP.

**(e)** `python tools/audit/gen_guard_state.py --check`, captured whole. Its output must equal
`git cat-file blob 9554b6f394edea834d0079aed50273f1957cd814` (counts line
`81 guard(s) run, 18 failing, 4 not run, 16 historical record(s)`), else STOP. This capture is the reference for
Task 2.

**(f)** Read whole: `records/cc/reports/cc_report_root_records_move_finish_commit_three_2026_09_17.md`, and handoff
entry 193 §1.

## TASK 1 — the edits

**(a) `tools/audit/gen_guard_state.py`, the `HISTORICAL` table.** Locate with Grep: pattern
`"tools/audit/decisions/gen_reads6_yield.py":` must match exactly once, and the next line that is exactly `}` closes
the table. **Insert immediately before that `}` line**, changing nothing else:

```python
    # ── THE THREE PASSAGE-PROTECTION CHECKS ───────────────────────────────────────────────────
    # RECLASSIFIED 2026-09-17 by `cc_instruction_passage_guards_historical_2026_09_17.md` Task 1, on the
    # user's ruling of 2026-09-17 (Alternative A1), recorded at
    # `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_three.md` §1. Each was classed LIVE,
    # and the reason is preserved at its verdict in `gen_guard_classification.py` (#12). ★ THE COST THE USER
    # ACCEPTED: nothing now fails on the day a later act archives one of the passages these checks held.
    "tools/audit/gen_claude_md_finer_archive.py":
        "HISTORICAL RECORD: the reading of the six `CLAUDE.md` passages settled at the seventh- and "
        "eighth-return sittings, a question its own record calls CLOSED. Its at-site test compares each "
        "passage's wording, read at a pinned commit, word for word with the live file, so it cannot tell an "
        "archiving act from a renamed path or an ordinary amendment; the 2026-09-17 root records move "
        "turned it red on renamed paths. The artifact stays on disk as committed (#12).",
    "tools/audit/gen_post_split_archive.py":
        "HISTORICAL RECORD: the one-off post-split archiving pass over the five governing files, which moved "
        "one resolved row and left the rest at site. Its at-site test compares the left-at-site passages' "
        "pinned wording word for word with the live files, so it fails on a renamed path or an ordinary "
        "amendment as surely as on an archiving act; the 2026-09-17 root records move turned it red on "
        "renamed paths. The artifact stays on disk as committed (#12).",
    "tools/audit/gen_claude_md_prune_backlog.py":
        "HISTORICAL RECORD: the one-off prune-at-amendment backlog pass of 2026-09-07, which read two "
        "candidates and moved neither. Its at-site test compares their pinned wording word for word with the "
        "live `CLAUDE.md`, so it fails on a renamed path or an ordinary amendment as surely as on an archiving "
        "act; the 2026-09-17 root records move turned it red on renamed paths. The artifact stays on disk as "
        "committed (#12).",
```

**(b) `tools/audit/gen_guard_classification.py`, the three verdicts.** Six single edits. **Before each, Grep the
old string: it must match exactly once, else STOP.**

1. Old: `        LIVE, "gen_claude_md_finer_archive.py, THE STOPS of its module docstring; `build()`, which "`
   New: the same line with `LIVE,` replaced by `POINT,` — nothing else on the line changes.
2. Old: `        "LIVE. Every one of its claims is re-answered against the tree AS IT STANDS on every run — "`
   New: two lines —
   `        "RECORDS A POINT-IN-TIME MEASUREMENT — reclassified 2026-09-17 on the user's ruling (Alternative A1, "`
   `        "handoff entry 193 §1). ★ THE FORMER VERDICT, PRESERVED (#12): LIVE. Every one of its claims is re-answered against the tree AS IT STANDS on every run — "`
3. Old: `        LIVE, "gen_post_split_archive.py, THE STOPS of its module docstring; `build()`, which "`
   New: the same line with `LIVE,` replaced by `POINT,`.
4. Old: `        "LIVE. Every one of its claims is re-answered against the tree AS IT STANDS on every run, "`
   New: two lines —
   `        "RECORDS A POINT-IN-TIME MEASUREMENT — reclassified 2026-09-17 on the user's ruling (Alternative A1, "`
   `        "handoff entry 193 §1). ★ THE FORMER VERDICT, PRESERVED (#12): LIVE. Every one of its claims is re-answered against the tree AS IT STANDS on every run, "`
5. Old: `        LIVE, "gen_claude_md_prune_backlog.py, THE STOPS of its module docstring; `candidates()`, "`
   New: the same line with `LIVE,` replaced by `POINT,`.
6. Old: `        "LIVE. Three of its four reconciliation directions are re-answered against the tree AS IT "`
   New: two lines —
   `        "RECORDS A POINT-IN-TIME MEASUREMENT — reclassified 2026-09-17 on the user's ruling (Alternative A1, "`
   `        "handoff entry 193 §1). ★ THE FORMER VERDICT, PRESERVED (#12): LIVE. Three of its four reconciliation directions are re-answered against the tree AS IT "`

No separate syntax check is run: Task 2(a) executes `gen_guard_state.py`, and Task 2(b) executes
`gen_guard_classification.py`, which imports it. A `SyntaxError` or import error in either run → STOP.

**(c) Restore the committed finer-archive artifact.** `git restore --source=HEAD --worktree --
tools/audit/claude_md_finer_archive.json`. The working-tree copy was rewritten by a write-mode run before the user's
ruling; the historical record is the committed one.

## TASK 2 — prove the effect before any commit

**(a)** `python tools/audit/gen_guard_state.py --check`, captured whole. Compare line by line with the Task 0(e)
capture. **The only differences allowed:**
- the three `[FAIL]` lines for the three tools of Task 1 are gone from the run listing;
- the three tools appear in the historical-record listing;
- the counts line reads, from Task 0(e)'s printed figures: runs 81 − 3, failing 18 − 3, not run 4, historical 16 + 3.
Any other difference — any other guard's verdict or output — → STOP, no commit.

**(b)** `python tools/audit/gen_guard_classification.py --check`, captured. It is expected to STOP with its
`no authored verdict` message naming **exactly** `tools/audit/gen_l0_l1_outgoing_population.py` and
`tools/audit/gen_withheld_family_reading.py`. Report the message verbatim. Any other message → STOP, no commit.

**(c)** `python tools/audit/changed_paths.py`, captured. Against Task 0(d)'s capture, the only new records are ` M` for
`tools/audit/gen_guard_state.py` and `tools/audit/gen_guard_classification.py`; the ` M` record for
`tools/audit/claude_md_finer_archive.json` is gone. Anything else → STOP.

**(d) Task commit, by explicit path only:** `tools/audit/gen_guard_state.py`; `tools/audit/gen_guard_classification.py`;
this dispatch; `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_three.md`. Check with
`changed_paths.py --staged` before committing: exactly those four. **Never** `docs/research_papers/BIBLIOGRAPHY.md`,
`docs/research_papers/README.md`, `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_eight.md`,
`tools/audit/guard_state.json`, `tools/audit/guard_classification.json`. Record the hash as the TASK COMMIT.

## TASK 3 — the report

Write with the Write file tool `records/cc/reports/cc_report_passage_guards_historical_2026_09_17.md` (Glob first; if
it exists → STOP). It carries Task 0, Task 1's six edits and the insertion as made, Task 2's captures and comparisons
with their blob identities, the classification STOP verbatim, and the task commit hash. Name members; state a total
only as a sum of named members or a figure a tool printed (D-431).

## TASK 4 — the close and the push

1. **The `STATUS.md` entry**, written first, at the top of the dated entries, in the file's pointer convention: names
   this dispatch, the three tools now historical, the ruling's record (entry 193 §1), that the classification record
   and `guard_state.json` were not regenerated and why, and points at this batch's report. Restates no figure.
2. **The forward bound — TWO moves in one act**, because the previous close skipped its own (its report and
   `STATUS.md` entry say why). Read `tools/audit/gen_status_batch_bound.py`'s docstring and its whole comment block
   above `PREVIOUS_AIMINGS`, including the 2026-09-07 catch-up precedent, before editing. `BASE_COMMIT` = the TASK
   COMMIT of Task 2(d). `ACT_DATE` = the day this runs. `DISPATCH` = this dispatch's file name, `TASK` = `"Task 4"`.
   Append every replaced aiming to `PREVIOUS_AIMINGS` (#12). Then, oldest first:
   - **Move 1:** `PREVIOUS_BATCH_DISPATCH = "cc_instruction_defense_share_authored_ends_2026_09_08.md"`,
     `MOVE_KIND = "catch-up"`, `--apply`.
   - **Move 2:** `PREVIOUS_BATCH_DISPATCH = "cc_instruction_root_records_move_finish_commit_three_2026_09_17.md"`,
     `MOVE_KIND = "ordinary"`, `--apply`.
   - Then `python tools/audit/gen_status_batch_bound.py --check` must exit 0.
   **If either move cannot be performed as the docstring and the precedent describe:** run
   `git restore --source=HEAD --worktree -- STATUS.md STATUS_ARCHIVE.md tools/audit/gen_status_batch_bound.py
   tools/audit/status_batch_bound.json`, write this batch's `STATUS.md` entry again exactly as in step 1 with one added
   sentence saying the bound was not performed and why, skip the bound, and report the tool's message verbatim. That is
   not a STOP.
3. `python tools/audit/gen_session_start_read_size.py`, then `python tools/audit/gen_defense_share.py`. Any STOP or
   FAIL printed → STOP, no commit.
4. `python tools/audit/gen_guard_state.py --check`, captured: every guard's result equal to Task 2(a)'s capture, else
   STOP (no commit, no push).
5. **Close commit, by explicit path only:** `STATUS.md`; `tools/audit/session_start_read_size.json`;
   `tools/audit/defense_share.json`; this batch's report; and **if the bound ran**, `STATUS_ARCHIVE.md`,
   `tools/audit/gen_status_batch_bound.py` and `tools/audit/status_batch_bound.json`. Never the five excluded paths of
   Task 2(d). Check with `changed_paths.py --staged` before committing.
6. `git diff <TASK COMMIT> <close commit>`: changes only in those paths; the two measurement artifacts only in values
   that follow from `STATUS.md` changing (and `STATUS_ARCHIVE.md`, if the bound ran); the report a whole-file addition.
   Otherwise → STOP, no push.

**Push:** `git push origin master`. Never `--force`. A failure is reported verbatim, with no retry by other options.

At the foot of the chat reply: the report's path, this dispatch's blob identity, the task commit and close commit
hashes, whether the bound ran, and the push result verbatim.

## DECLARED BY THE WRITING SIDE

- **Checked at the files this sitting:** both ref files read `49c6364242772d34c08b046d5972d5748a4d0763`; the Commit-3
  report whole; `gen_guard_state.py` — the `HISTORICAL` table's last entry and closing line, and that the runner
  skips a tool named there; `gen_guard_classification.py` — the three verdict lines quoted in Task 1(b) (each old
  string found once by Grep over a staged copy), the `POINT` constant, and `build()`'s first STOP for a tool with no
  verdict; that the two tools named in Task 2(b) are in the runner's list and have no verdict;
  `gen_status_batch_bound.py` — its docstring, that `--apply` and a plain run write `status_batch_bound.json`, and the
  names of its authored fields.
- **Relayed, not checked:** the capture identities `5b26228c…` and `9554b6f3…` and their contents, from the Commit-3
  report; that the four-line change leaves every other guard's output unchanged (Task 2(a) measures it).
- **No decisions-register entry is written by this batch.** Whether this reclassification owes one is not settled by
  the writing side and is carried at entry 193 as an open point; it is not this batch's to decide.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

Any Task 0 mismatch; any Grep of an old string not matching exactly once; any compile failure; any difference Task 2
does not allow; any excluded path staged; any guard refusal; **any instruction here found false at the objects.** On
any STOP: undo nothing; report the captures and every commit hash; stop.
