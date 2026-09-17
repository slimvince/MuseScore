# CC REPORT — root records move, Commit 3 and the push, 2026-09-17

**Dispatch executed:** `records/cc/instructions/cc_instruction_root_records_move_finish_commit_three_2026_09_17.md`,
blob **`6b9deb62b91320f4d47220f55123590ae2edd4e9`**.
**Base dispatch read from its pinned blob:** `a16402ac47ed9f07de68629f299b65fd71eee51e`.
**Resume dispatch (third issue) read from its pinned blob:** `bfb7846d337462ed4531f568a2edd38aab067b82`.
**Report of the previous run, read whole before Task 0:**
`records/cc/reports/cc_report_root_records_move_finish_commit_two_2026_09_17.md`.

This report was written before Commit 3, as the dispatch orders. Commit 3's steps, its hash and the push result are
given in the chat reply, as the base dispatch's Task 4 orders.

| Commit | Hash | Source of the hash |
|---|---|---|
| Commit 1 (the 978 renames) | `447311137a934ab8e3f51e7abf8e18e7b8d2bd0e` | given by this dispatch as the parent of Commit 2 |
| Commit 2 (references, quotes, regeneration, record files) | `54804de49ac593b532e804bcfb881366e3a018b5` | `git rev-parse HEAD` at Task 0(b); the commit-two report records the command's printed `[master 54804de49a]` |
| Commit 3 | not yet made when this report was written | — |

**The one open point of the Commit 2 content proof** (the eleven reordered entries of
`tools/audit/specification_document_set.json`) is closed by this dispatch, on the writing side's reading of its own
bar. The proof was not re-run, as the dispatch orders.

## 1. TASK 0 — the state

- **(a)** `git hash-object -w` on this dispatch → `6b9deb62b91320f4d47220f55123590ae2edd4e9`. Git warned that LF will
  be replaced by CRLF.
- **(b)** `git rev-parse --abbrev-ref HEAD` → `master`; `git rev-parse HEAD` →
  `54804de49ac593b532e804bcfb881366e3a018b5`. As required.
- **(c)** `changed_paths.py --staged` → blob `2781d206447325730f78a7685285f43d32d31ece`, the required identity.
- **(d)** `changed_paths.py` → `567 changed path record(s) [worktree]`, blob
  `5b26228cdf4e874c045e01ed352a2e27d8dc3d06`. Compared, read in full with Read, with
  `git cat-file blob af30f8f394ce42ee628bd95e301dcaec3537c7a8` (`564 changed path record(s) [worktree]`):
  - new lines 1–3 equal old lines 1–3;
  - **new line 4, allowed:** ` M records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_two.md`;
  - new lines 5–10 equal old lines 4–9;
  - **new line 11, allowed:**
    `?? records/cc/instructions/cc_instruction_root_records_move_finish_commit_three_2026_09_17.md` (this dispatch);
  - new lines 12–132 equal old lines 10–130;
  - **new line 133, allowed:**
    `?? records/cc/reports/cc_report_root_records_move_finish_commit_two_2026_09_17.md`;
  - new lines 134–567 equal old lines 131–564; nothing under `scratch_artifacts/` differs.

  564 + 3 = 567. No STOP.
- **(e)** `gen_guard_state.py --check` → exit 1, blob **`9554b6f394edea834d0079aed50273f1957cd814`**, the same blob the
  dispatch names. The two outputs are byte-identical, so every guard's result is equal. Its counts line reads
  `81 guard(s) run, 18 failing, 4 not run, 16 historical record(s)`. No STOP. This capture is the reference for
  Commit 3's step 4.

## 2. The three checks left failing by the user's ruling of 2026-09-17

The user ruled on 2026-09-17 (Alternative A of the writing side's surface, as the resume dispatch records it) to finish
and push now, leave these three checks failing and reported, and settle the tools as a separate question after the
push. This batch did not run any of the three in any mode other than inside `gen_guard_state.py --check`. In the
Task 0(e) capture they are:

- `[FAIL] tools/audit/gen_claude_md_finer_archive.py --check` (line 59);
- `[FAIL] tools/audit/gen_post_split_archive.py --check` (line 60);
- `[FAIL] tools/audit/gen_claude_md_prune_backlog.py --check` (line 79).

**Their messages**, as the resume dispatch's third run recorded them from separate `--check` runs
(`records/cc/reports/cc_report_root_records_move_finish_resume_third_2026_09_17.md` §5). They were not re-run
separately here; the guard runner does not print them.

- **`gen_claude_md_finer_archive.py --check`** (blob `f61de75e82d49c8911da5c5a4c1db67c991d9461`): of its seven
  reconciliation lines, only `every REFUSED span still at site exactly once           False` prints `False`. Its first
  line is `ruled to archive: 2, moved 0, left at site by the reading 2; refused by the ruling 4`.
- **`gen_post_split_archive.py --check`** (blob `e4d3e573de55fa725ed15d8de14a76899ff91ba6`):
  `FAIL: the post-split archiving record does not re-derive: tools\audit\post_split_archive.json`
- **`gen_claude_md_prune_backlog.py --check`** (blob `845cc32d0cf27e8ce1da9041e99dc8a112b59d7e`):
  `FAIL: the prune-at-amendment backlog record does not re-derive: tools\audit\claude_md_prune_backlog.json`

**The cause, as the earlier reports derive it. It is DERIVED and was NOT MEASURED passage by passage.**

- The finer-archive tool reads each refused `CLAUDE.md` passage's exact wording from the git object at a pinned
  commit, and counts that wording in the live `CLAUDE.md` (the `refused_at_site` test).
- The earlier batch of this line of work changed moved-file root names inside those passages to `records/…` paths,
  so the pinned wording no longer occurs verbatim.
- The post-split and prune-backlog tools import the finer-archive tool's settled spans and read pinned `CLAUDE.md`
  text. **Whether their failures come from the same passages was not established.**

`tools/audit/claude_md_finer_archive.json` stays modified and uncommitted in the working tree, as the resume
dispatch orders.

## 3. What Commit 3 is ordered to carry

By explicit path only: `STATUS.md`; `STATUS_ARCHIVE.md` and `tools/audit/gen_status_batch_bound.py` if the forward
bound runs; `tools/audit/session_start_read_size.json`; `tools/audit/defense_share.json`; this report;
`records/cc/reports/cc_report_root_records_move_finish_commit_two_2026_09_17.md`; this dispatch;
`records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_two.md`. Never the four excluded paths
(`docs/research_papers/BIBLIOGRAPHY.md`, `docs/research_papers/README.md`,
`records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_eight.md`,
`tools/audit/claude_md_finer_archive.json`).

## 4. Declared departures and bounds

1. **Session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in three pieces; the `gating_ids` list in
   `tools/audit/nongating_apparatus_rows.json`. Read whole before Task 0: this dispatch, both pinned dispatches
   (fetched with `git cat-file blob` into the scratchpad), the commit-two report, and the resume dispatch's third-run
   report (for the three checks' messages).
2. **Captures.** Every capture was written to the scratchpad, given a blob identity with `git hash-object -w`, and
   read with Read or Grep only. One reference capture (`af30f8f3…`) was fetched with `git cat-file blob`. Commands set
   a shell variable `S` to the scratchpad path. No shell command read a file. No guard refused anything.
3. **Entry 192's content is not proved**, as the dispatch states.
