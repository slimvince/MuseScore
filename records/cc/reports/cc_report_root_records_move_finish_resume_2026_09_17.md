# CC REPORT — resuming the root records move finish: Task 2(a) and (b) done; STOPPED at Task 2(c) on one guard outside the stated pattern, before any commit, 2026-09-17

**Dispatch executed:** `records/cc/instructions/cc_instruction_root_records_move_finish_resume_2026_09_17.md`,
blob **`6e243168ba6c1b246f11ca4b7223df158ea1d5f8`**.
**Base dispatch read from its pinned blob:** `a16402ac47ed9f07de68629f299b65fd71eee51e`.

## 0. THE STOP — read this first

**The batch STOPPED at Task 2(c).** The dispatch says that every guard other than the six named to pass and the
three named to stay failing must give the same result as the reference run (`d3774d37…`), "Otherwise → STOP."

**One guard does not:**

| Guard | Reference run (`d3774d37…`, line 24) | This run (`a3e3dc9d…`, line 24) |
|---|---|---|
| `tools/audit/gen_period_stratum_split.py --check` | `[PASS]` | **`[FAIL]`** |

Every other guard matches the stated pattern (§3(c)). The counts line agrees with this: the reference run prints
`81 guard(s) run, 24 failing, 4 not run, 16 historical record(s)`, and this run prints `81 guard(s) run, 19 failing,
4 not run, 16 historical record(s)`. 24 − 6 (now passing) + 1 (`gen_period_stratum_split.py`) = 19.

### The likely cause — derived from the tool's source, not measured

- `gen_period_stratum_split.py` reads `tools/audit/specification_document_set.json` (constant `IN_DOCSET`, line
  136; read at line 311, where it also builds the `member_of` table from `the_document_set`).
- It writes that input's **sha256** into its own artifact (line 409: `"sha256": sha256_of(IN_DOCSET)`).
- Its `--check` (lines 597–605) compares the re-derived text with `tools/audit/period_stratum_split.json` byte for
  byte.
- The third run's Task 2(a) write mode 2 (`gen_specification_document_set.py`) rewrote
  `specification_document_set.json` (third report §4). The recorded sha256 can therefore no longer match. The
  `member_of` table could also change if member paths changed.
- **Not established:** which fields of the re-derived `period_stratum_split.json` differ, or whether anything besides
  the digest differs. Finding out would take a command neither dispatch names. The tool was not run on its own, and
  its write mode was not run.
- **When the failure started is not isolated.** The reference run was captured at the third run's Task 0(e), before
  its Task 1. No guard set was run between that point and this Task 2(c). The candidates are: Task 1's edits, the
  third run's four write modes, and this run's three.

**Why the dispatch did not foresee this, as far as the objects show:** its Task 2(c) list and the base dispatch's
Task 2 list name only the nine guards that were failing in the reference run. `gen_period_stratum_split.py` was
passing then, and it depends on an artifact this line of work regenerates. This is a guard that started failing,
not one that was failing already.

### For the user to decide (options only, no recommendation)

- (a) Let `gen_period_stratum_split.py --check` also stay failing, like the three archive tools, and continue with
  Task 3.
- (b) Allow its write mode (no argument; it writes only `tools/audit/period_stratum_split.json`, lines 606–607) to be
  run, with its artifact added to the Task 2(d) kinds (a digest of a regenerated file). Whether its re-derived
  content changes only the digest has not been checked.
- (c) Something else.

## 1. State at the stop

- **No commit was made and nothing was pushed.** `git rev-parse HEAD` → `5d24edb565b2e0e9efc92e082c163112bd97087f`.
  Commits 1, 2 and 3 do not exist.
- **Staged:** `python tools/audit/changed_paths.py --staged` → blob **`4e959e003bbdd5b51e336ee669bd761eba00d7fc`**,
  unchanged from Task 0(c).
- **Working tree:** `python tools/audit/changed_paths.py` → `1624 changed path record(s) [worktree]`, blob
  **`654f881a31adf153ae8e4a5af7c0617e7e49dce5`** (the Task 2(b) capture). Writing this report adds one more untracked
  file, which that capture does not include.
- `tools/audit/claude_md_finer_archive.json` stays modified in the working tree. It was not staged and not restored.
- **Not run:** Task 3 (the commits, the content proof, the `STATUS.md` entry, the forward bound, the two
  re-measurements, the push).

## 2. TASK 0 — the resume state

- **(a)** `git hash-object -w` on this dispatch → `6e243168ba6c1b246f11ca4b7223df158ea1d5f8`. Git warned that LF will
  be replaced by CRLF.
- **(b)** `git rev-parse --abbrev-ref HEAD` → `master`; `git rev-parse HEAD` →
  `5d24edb565b2e0e9efc92e082c163112bd97087f`. At the base.
- **(c)** `changed_paths.py --staged` → blob `4e959e003bbdd5b51e336ee669bd761eba00d7fc`, the required identity.
- **(d)** `changed_paths.py` → `1621 changed path record(s) [worktree]`, blob
  `791d9f830c8d2b89ea560e66ffadf61bc34c43df`. It was compared with the third run's stop capture (blob
  `4073a73b…`, `1619 changed path record(s)`) using Grep:
  - **Records that are not `R` and not under `scratch_artifacts/`:** identical line for line, except for two
    inserted untracked records, both allowed:
    - `records/cc/instructions/cc_instruction_root_records_move_finish_resume_2026_09_17.md` (line 1054);
    - `records/cc/reports/cc_report_root_records_move_finish_third_2026_09_17.md` (line 1181).
  - **Records starting with `R`** (the 976 `R` plus the 2 `RM`): 978 in each capture, at lines 41–1018 in both
    (both insertions come after that range). Compared by count and position, as in the third run. The staged
    capture, which lists the same renames, is byte-identical to the one required.
  - **Records under `scratch_artifacts/`:** 387 in each. Compared by count only.

  1619 + 2 = 1621. There was no STOP.

## 3. TASK 2 — the remaining write modes

### (a) The three write modes

Before running them, the `main` function and `OUT` constant of each tool were read:
- `gen_session_start_read_size.py`: `main` at 752; `OUT` = `session_start_read_size.json` (line 119); with no
  argument it writes `OUT`.
- `gen_defense_share.py`: `main` at 673; `OUT` = `defense_share.json` (line 116); with no argument it writes `OUT`.
- `gen_derivation_boot_pack.py`: `main` at 4083; `OUT` = `derivation_boot_pack.json` (line 201); with no argument it
  calls `write_all(manifest, packs, None)`. `--subject` was not used.

Nothing read contradicted the base dispatch's table.

| # | Command | Exit | Output (blob) |
|---|---|---|---|
| 1 | `python tools/audit/gen_session_start_read_size.py` | 0 | `wrote tools/audit/session_start_read_size.json` (`bcdae0e0…`) |
| 1 | `… --check` | 0 | `the session-start read measurement re-derives` (`72e19521…`) |
| 2 | `python tools/audit/gen_defense_share.py` | 0 | `wrote tools/audit/defense_share.json` (`72c3ec93…`) |
| 2 | `… --check` | 0 | `the defense-share measurement re-derives` (`80e1fc5b…`) |
| 3 | `python tools/audit/gen_derivation_boot_pack.py` | 0 | `wrote tools\audit\derivation_boot_pack.json`; three subjects listed (`a26a029e…`) |
| 3 | `… --check` | 0 | `the derivation boot pack re-derives`; `harmony-boundary`, `l0-l1` and `scoring-model` each `FROZEN — … file(s) at their recorded blobs` (`f4accd66…`) |

No output printed `STOP`. The finer-archive, post-split and prune-backlog tools were **not** run in any write mode.

### (b) Nothing else written

`changed_paths.py` → `1624 changed path record(s) [worktree]`, blob `654f881a31adf153ae8e4a5af7c0617e7e49dce5`.
Against Task 0(d), compared with Grep:
- **Three new ` M` records**, which are exactly the three allowed:
  - `tools/audit/defense_share.json` (line 1028);
  - `tools/audit/derivation_boot_pack.json` (line 1029);
  - `tools/audit/session_start_read_size.json` (line 1046).
- **Nothing under `tools/audit/derivation_boot_pack/`.** A Grep for that string matches no record.
- **Everything else is unchanged, only shifted in position.** Lines 1–40 and 814, 838 match. Every other
  non-`R`, non-`scratch_artifacts/` record matches, moved down by the three inserted lines (for example this
  dispatch 1054 → 1057, the third report 1181 → 1184, `tools/audit/reference_map_check.json` 1621 → 1624). The
  `R` records (978) and the `scratch_artifacts/` records (387) keep their counts.

1621 + 3 = 1624. There was no STOP.

### (c) The guard set — the STOP

`python tools/audit/gen_guard_state.py --check` → exit 1, blob **`a3e3dc9dbfa5285c2de00cfcb3e0efa5cb5c16aa`**.
Compared guard by guard with the reference run (`git cat-file blob d3774d37…`). Both files list the guards in the
same order, at lines 2–102:

- **The six that had to pass now pass:** `gen_discard_records.py --check` (line 18), `gen_specification_document_set.py
  --check` (26), `gen_rulings_sort.py --check` (37), `gen_session_start_read_size.py --check` (62),
  `gen_defense_share.py --check` (63), `gen_derivation_boot_pack.py --check` (65). Each was `[FAIL]` in the reference
  run.
- **The three allowed to fail still fail:** `gen_claude_md_finer_archive.py --check` (59),
  `gen_post_split_archive.py --check` (60), `gen_claude_md_prune_backlog.py --check` (79). Their messages are in §4.
- **One other guard differs:** `gen_period_stratum_split.py --check` (24), `[PASS]` → `[FAIL]`. **This is the STOP**
  (§0).
- **Every other line is equal.** That includes line 1 (`STALE vs the run: guard_state.json does not re-derive`),
  the four `[NOT RUN]` lines and the sixteen `[HISTORICAL]` lines.

## 4. The three checks left failing by the user's ruling of 2026-09-17

Each one's `--check` was run on its own, the only mode the dispatch permits for these tools, so its message could be
recorded. The guard runner does not print the messages. All three exited 1.

- **`gen_claude_md_finer_archive.py --check`** (blob `f61de75e82d49c8911da5c5a4c1db67c991d9461`, **the same blob**
  as the third run's capture of this check). It prints seven reconciliation lines. **Only one prints `False`:**
  `every REFUSED span still at site exactly once           False`. The other six print `True`: moved spans
  byte-present in the companion exactly once; moved spans absent from the must-read; every flagged span still at site
  exactly once; no flagged span in the companion; no REFUSED span in the companion; moved + kept accounts for the base
  blob. It prints no `does not re-derive` line.
- **`gen_post_split_archive.py --check`** (blob `e4d3e573de55fa725ed15d8de14a76899ff91ba6`):
  `FAIL: the post-split archiving record does not re-derive: tools\audit\post_split_archive.json`
- **`gen_claude_md_prune_backlog.py --check`** (blob `845cc32d0cf27e8ce1da9041e99dc8a112b59d7e`):
  `FAIL: the prune-at-amendment backlog record does not re-derive: tools\audit\claude_md_prune_backlog.json`

**The cause, as the third report §0 derives it. This is derived and was not measured passage by passage.** The
finer-archive tool counts each refused `CLAUDE.md` passage by its exact wording, read from the git object at a pinned
commit, in the live `CLAUDE.md` (`refused_at_site = all(live.count(r["_text"]) == 1 …)`, line 463). The previous
batch changed moved-file root names inside those passages to `records/…` paths, so the pinned wording no longer
occurs verbatim. At least three of the four refused passages quote a moved file by its root name. The post-split and
prune-backlog tools import the finer-archive tool's settled spans and read pinned `CLAUDE.md` text, according to the
third report §0 and this dispatch's own declaration. **Whether their failures come from the same passages was not
established.** Their messages say only that their records do not re-derive.

## 5. Declared departures and bounds

1. **Session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in three pieces; the `gating_ids` list in
   `tools/audit/nongating_apparatus_rows.json`. Read whole before Task 0: this dispatch, the base dispatch from its
   pinned blob, and the third run's report.
2. **Captures in the scratchpad.** Every capture was written there and given a blob identity with
   `git hash-object -w`. Two earlier captures (`4073a73b…`, `d3774d37…`) and the base dispatch were fetched with
   `git cat-file blob`. Every capture was read with Read or Grep only. Commands set a shell variable `S` to the
   scratchpad path; no shell command read a file through it. No guard refused anything.
3. **The three separate `--check` runs in §4** are not named as separate commands in the dispatch. They were run
   because Task 2(c) orders the messages to be recorded and the guard runner does not print them. They are check
   modes only, the only mode the dispatch permits for these tools.
4. **The cause in §0 was read from `gen_period_stratum_split.py`**: its docstring, its constants, its `main`, and a
   search for `IN_DOCSET`. This reading is not named in the dispatch. It is read-only and only supports the report.
   The tool itself was not run beyond its place in the guard set.
5. **Commit and push:** none. Nothing has left the machine.
