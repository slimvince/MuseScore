# CC REPORT — finishing the root records move: STOPPED at Task 1(a), before any edit or commit, 2026-09-17

**Dispatch executed:** `records/cc/instructions/cc_instruction_root_records_move_finish_2026_09_17.md`,
blob **`b5d6566eebf3553821291199d95cec2c67949491`**.

## 0. THE STOP — read this first

**The batch STOPPED at Task 1(a).** The set test found **35** entries, not the 43 the dispatch lists. The STOP rule
is: "If the set is not exactly the 43 identities listed above → STOP, naming the difference."

**The difference: eight entries.** Each of them does quote a moved file by its root name, and its home does now
carry that name as a `records/…` path. **But in each case the quoted passage no longer starts at the line the
entry cites.** So the name is not "at that place" when the home is read at the cited line, as Task 1(a) directs.

| Entry | Home file | Cited start line | Where the quoted passage starts now (Grep) | Where the moved name now sits |
|---|---|---|---|---|
| D-199 | `CLAUDE.md` | 1393 | 1432 | 1441 |
| D-249 | `CLAUDE.md` | 1781 | 1836 | 1837 |
| D-253 | `CLAUDE.md` | 1795 | 1850 | 1851 |
| D-254 | `CLAUDE.md` | 1838 | 1893 | 1894 |
| D-294 | `CLAUDE.md` | 937 | 976 | 977 |
| D-656 | `CLAUDE.md` | 1044 | 1083 | 1086, 1089 |
| D-660 | `CLAUDE.md` | 1561 | 1616 | 1617 |
| D-675 | `CLAUDE.md` | 1659 | 1714 | 1716 |

**This batch did not cause that drift.** The previous batch's `--verify` output (blob
`9cfcddcbc553da8f804aafe0748025ebdcf229e4`) already reports `LINE DRIFT` for other `CLAUDE.md` entries at these
same offsets: +39 lines in the gate-policy region (for example D-308: 923 → 962) and +55 lines in the conventions
region (for example D-200: 1751 → 1806). For these eight entries the drift was hidden, because a `verbatim NOT FOUND`
result is reported before the line is checked.

**Why finishing Task 1 under the other reading would STOP too.** Suppose "at that place" is read as "where the
quoted passage now sits". Then the set is exactly the 43, but Task 1(c)2 would STOP. The reason is in
`tools/audit/decisions/gen_cluster_dispositions.py`, `verify_backbone()`:
- when the quote is not found, it reports `MISS` and moves on (`continue`);
- when the quote **is** found, it finds the line the quote starts on and records a `LINE DRIFT` if that line differs
  from the cited one (`elif found != cited: drifted.append(...)`), printing
  `LINE DRIFT <id>: cited <home>, actually starts at line <n>`.

So once the eight quotes are corrected, `--verify` would print eight `LINE DRIFT` lines that do not appear in blob
`9cfcddcb…`. Task 1(c)2 says: "no `NOT FOUND` or other failure line may appear that is absent from blob
`9cfcddcb…`. Otherwise → STOP." The only way to avoid those eight lines would be to change each entry's `home` line
number, and Task 1(b) forbids that: "Nothing else in the field or the entry changes."

**This is stated as a derivation from the code, not a measurement.** No edit was made to run it, because the STOP
at 1(a) comes first.

**For the user to decide** (options only; no recommendation is made here):
- (a) allow the eight `LINE DRIFT` lines as new `--verify` lines, while the guard's result stays FAIL, as it is
  now;
- (b) also re-point those eight entries' `home` line numbers to the current start lines, a change beyond Task
  1(b)'s bar;
- (c) something else.

## 1. State at the stop

- **No file was edited, no generator was run in write mode, nothing was staged or committed, nothing was
  pushed.**
- `git rev-parse HEAD` → `5d24edb565b2e0e9efc92e082c163112bd97087f` (the base). There are no commit hashes to
  report.
- `python tools/audit/changed_paths.py --staged` → blob **`4e959e003bbdd5b51e336ee669bd761eba00d7fc`**
  (`978 changed path record(s) [staged]`). This is identical to Task 0(c).
- `python tools/audit/changed_paths.py` → blob **`deee986f478f1e2f9b37605a8971b57f8f1458e5`**
  (`1610 changed path record(s) [worktree]`). This is identical to Task 0(d). Writing this report adds one
  untracked file, which that capture predates.

## 2. TASK 0 — the state, re-captured

- **(a)** `git hash-object -w` on this dispatch → `b5d6566eebf3553821291199d95cec2c67949491`.
- **(b)** `git rev-parse --abbrev-ref HEAD` → `master`; `git rev-parse HEAD` →
  `5d24edb565b2e0e9efc92e082c163112bd97087f`. At the base.
- **(c)** `changed_paths.py --staged` → blob `4e959e003bbdd5b51e336ee669bd761eba00d7fc`. This equals the required
  identity.
- **(d)** `changed_paths.py` → blob `deee986f478f1e2f9b37605a8971b57f8f1458e5` (`1610 changed path record(s)`).
  The previous stop capture, blob `fd3a25f41083e97d29ea6a5da0f9ae3b9d7dba1b`, printed `1607 changed path
  record(s)`. It was compared by Grep over the two captures, by record class:
  - ` M` records: the same 60 lines, in the same positions (lines 1–37 and 1016–1038), in both captures.
  - `R` records: 978 in each capture. `RM` records: the same two in each —
    `cowork_handoff.md -> records/cowork/handoff/cowork_handoff.md` and
    `cowork_handoff_entry_one_hundred_and_eighty_eight.md -> records/cowork/handoff/…`.
  - `??` records: 572 now against 569 before. Records under `scratch_artifacts/` number 387 in both. The
    untracked records outside `scratch_artifacts/` are identical line for line, apart from three inserted
    records, which are exactly the three the dispatch allows:
    - `records/cc/instructions/cc_instruction_root_records_move_finish_2026_09_17.md` (new line 1046);
    - `records/cc/reports/cc_report_root_records_move_2026_09_17.md` (new line 1170);
    - `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_one.md` (new line 1220).
  - Bound: the 387 `scratch_artifacts/` records were compared by count only, not line by line. The dispatch
    makes a difference there reportable, not a STOP.
- **(e)** `python tools/audit/gen_guard_state.py --check` → exit 1, with the last line
  `81 guard(s) run, 24 failing, 4 not run, 16 historical record(s)`. The capture's blob is
  **`d3774d3735639fcf8a604ee5d357a94933f2305f`**, which is **the same blob** as the previous Task 5(b) capture.
  Every guard's result is therefore equal, and this capture is the reference run.

## 3. TASK 1(a) — how the set was established

- **The `NOT FOUND` lines.** Blob `9cfcddcb…` carries exactly 43 `verbatim NOT FOUND` lines, for these entries:
  - D-199, D-249, D-252, D-253, D-254, D-294, D-416;
  - D-640 to D-658;
  - D-660 to D-664;
  - D-666 to D-677.
- **The `verbatim` fields.** Each of those 43 entries was read in `tools/audit/decisions/backbone_decisions.json`.
  Each `verbatim` field names at least one moved file by its root name: a `cowork_rulings_*` or
  `cowork_ruling_*` record, a `cc_instruction_*` dispatch, a `cc_*` report, or a `cowork_handoff*` file.
- **The homes.** A Grep over each home file for moved-file names, with or without the `records/…` prefix, returns
  only prefixed forms. The results by home:
  - **`cowork_audit_protocol.md`: 25 entries, all passing.** D-252 (line 239), D-640 to D-655, D-657, D-658, D-661,
    D-663, and D-668 to D-673. For each, a Grep for the section's opening line finds it at the cited line, and the
    moved names sit inside the cited range as `records/…` paths.
  - **`docs/implementation_roadmap.md`: D-416 passes.** Line 28 is the quote's opening line, and line 33 carries
    `records/cowork/handoff/cowork_handoff.md`.
  - **`cowork_design_doc_template.md`: D-674 passes.** Line 120 is the quote's opening line, and line 125 carries
    `records/cowork/rulings/cowork_rulings_2026_08_11_fourteenth_stop.md`.
  - **`CLAUDE.md`: 8 entries pass.** D-651 (line 157), D-676 (388), D-662 (420), D-677 (448), D-664 (594),
    D-666 (616), D-667 (635) and D-652 (651) each start at the cited line and carry `records/…` paths inside the
    cited range.
  - **`CLAUDE.md`: 8 entries do not pass at the cited line.** These are the eight in the §0 table.
- **Total.** 25 + 1 + 1 + 8 = **35** pass; 8 do not; 35 + 8 = 43.

## 4. Not done

Everything after Task 1(a):
- Task 1(b) and (c): no `verbatim` edit and no regeneration;
- Task 2: no write mode was run;
- Task 3: Commits 1 to 3, the content proof, the `STATUS.md` entry, the forward bound, the two measurements and the
  push.

## 5. Declared departures and bounds

1. **Captures in the scratchpad.** `git hash-object -w` was run on seven scratchpad captures to give them the
   identities cited here. `git cat-file blob` was used to fetch the three previous captures the dispatch names.
2. **One Grep over-reached.** A Grep meant to list the `verbatim` and `home` lines of the register data ran over the
   whole file, because its file filter did not apply to a single-file path. The output was saved by the tool and not
   used.
3. **Tool code read.** `gen_cluster_dispositions.py` was read at `verify_backbone()`, lines 326–425. The dispatch
   lists that file as not read by the writing side; this batch read it only to decide how the STOP would present.
4. **Session-start read.** `STATUS.md`, `DECISIONS.md` in full, and the gating identities in
   `tools/audit/nongating_apparatus_rows.json` were read.
