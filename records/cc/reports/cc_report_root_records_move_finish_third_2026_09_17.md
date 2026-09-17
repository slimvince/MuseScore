# CC REPORT — finishing the root records move, third issue: Task 1 done; STOPPED at Task 2(a) on a write mode exiting non-zero, before any commit, 2026-09-17

**Dispatch executed:** `records/cc/instructions/cc_instruction_root_records_move_finish_2026_09_17.md` (third issue),
blob **`a16402ac47ed9f07de68629f299b65fd71eee51e`**.

## 0. THE STOP — read this first

**The batch STOPPED at Task 2(a), on the fourth of the nine write modes.** The dispatch says: "A write mode that
prints a STOP or exits non-zero → STOP." `python tools/audit/gen_claude_md_finer_archive.py` (no argument) exited
**1**. Its whole output (blob `00ccfa9bf66b7417d6d7c0a2e859d0b97d8713aa`):

```
wrote tools\audit\claude_md_finer_archive.json
  ruled to archive: 2, moved 0, left at site by the reading 2; refused by the ruling 4
  characters moved: 0
  moved spans byte-present in the companion exactly once  True
  moved spans absent from the must-read                   True
  every flagged span still at site exactly once           True
  no flagged span in the companion                        True
  every REFUSED span still at site exactly once           False
  no REFUSED span in the companion                        True
  moved + kept accounts for the base blob                 True
```

The `--check` that followed also exited 1 and printed the same seven lines (blob
`f61de75e82d49c8911da5c5a4c1db67c991d9461`). It printed no `FAIL: … does not re-derive` line, so the artifact the
write mode had just written re-derives. The exit code comes from `main`'s last line:
`return 0 if ok else 1`, where `ok` requires every reconciliation boolean to be true.

**This is also a kind Task 2(d) bars:** "a boolean that was `true` becoming `false`". In
`tools/audit/claude_md_finer_archive.json` the field
`reconciliation.every_span_the_ruling_REFUSED_is_still_present_at_site_exactly_once` is now `false`.

**The write mode wrote its artifact before it returned 1.** `tools/audit/claude_md_finer_archive.json` is
therefore modified in the working tree (stop capture line 1020). It was not undone, as the dispatch orders.

### The cause — derived from the tool and the artifact, not measured

- The tool computes the flag at `gen_claude_md_finer_archive.py` line 463:
  `refused_at_site = all(live.count(r["_text"]) == 1 for r in p["refused"])`. Each refused span's text is read
  from the git object at the pinned commit (docstring: "every span's TEXT, from the git OBJECT at the pinned
  commit, matched verbatim in the live file"), and it is counted in the live `CLAUDE.md`.
- The artifact's `the_refused_by_the_ruling` block shows the opening of each of the four refused spans. Three of
  those openings quote a moved file by its root name:
  - span at pin lines 344–374: `` `cowork_rulings_2026_08_11_fifte…`` (the opening is cut at that point in the
    artifact);
  - span at pin lines 796–816: `` `cc_oi168_fix_report.md` ``;
  - span at pin lines 1008–1044: `` `cc_a8_rebaseline_measure_report.md` ``.
- The previous batch's Task 4 changed every such root name in `CLAUDE.md` to its `records/…` path. So the pinned
  text of at least those three spans no longer occurs verbatim in the live file, and the count is 0.
- **Not established:** whether the fourth refused span (pin lines 1750–1772) also fails, and which of the four
  make `all(...)` false. The per-span counts were not computed, because that would need a command this dispatch
  does not name.

This is the same shape as the dispatch's own reason for existing: a guard that compares pinned text with the live
file cannot pass once the live file's names became paths. It differs in one way. This tool does not publish a
size that Task 2(d) can let move. It publishes a **true/false reconciliation**, and it fails its own write mode.

### For the user to decide (options only, no recommendation)

- (a) Allow this one boolean to be `false`, and a non-zero exit, for `gen_claude_md_finer_archive.py`, and let
  the batch continue. The tool's own record would then state that ruled-refused spans are absent from the site,
  which is false in substance: the spans are still at the site, with paths in place of names.
- (b) Change the tool, or its pinned inputs, so that it compares the refused spans with the name-to-path mapping
  applied. That is a tool change beyond this dispatch's licence.
- (c) Something else, for example restoring the root names inside the refused spans in `CLAUDE.md` (the previous
  dispatch's class rules would have to allow that).

**Not yet run, and not predicted:** the write modes of `gen_post_split_archive.py` and
`gen_claude_md_prune_backlog.py`. Both import this tool's settled spans (`import gen_claude_md_finer_archive as
ruled_spans`) and read pinned `CLAUDE.md` text. Whether they fail the same way was not measured.

## 1. State at the stop

- **No commit was made and nothing was pushed.** `git rev-parse HEAD` → `5d24edb565b2e0e9efc92e082c163112bd97087f`.
  Commits 1, 2 and 3 do not exist, so there are no commit hashes to report.
- **Staged:** `python tools/audit/changed_paths.py --staged` → `978 changed path record(s) [staged]`, blob
  **`4e959e003bbdd5b51e336ee669bd761eba00d7fc`**. This is unchanged from Task 0(c).
- **Working tree:** `python tools/audit/changed_paths.py` → `1619 changed path record(s) [worktree]`, blob
  **`4073a73b34614995f321edbf259a76bf3278140e`**. Against the Task 1 state (1614, blob
  `877025ef83e0a35ae2e20528b4ce07ab2f3121e9`), the new ` M` records are these five, all of them artifacts in Task
  2's third column:
  - `ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md`
  - `tools/audit/claude_md_finer_archive.json`
  - `tools/audit/discard_records.json`
  - `tools/audit/rulings_sort_classification.json`
  - `tools/audit/specification_document_set.json`

  1614 + 5 = 1619. Writing this report adds one more untracked file, which that capture predates.
- **Not run:** Task 2(a) write modes 5–9, Task 2(b) and (c), and all of Task 3 (the commits, the content proof,
  the `STATUS.md` entry, the forward bound, the two re-measurements and the push).

## 2. TASK 0 — the state, re-captured

- **(a)** `git hash-object -w` on the dispatch → `a16402ac47ed9f07de68629f299b65fd71eee51e`. Git warned that LF will
  be replaced by CRLF.
- **(b)** `git rev-parse --abbrev-ref HEAD` → `master`; `git rev-parse HEAD` →
  `5d24edb565b2e0e9efc92e082c163112bd97087f`. At the base.
- **(c)** `changed_paths.py --staged` → blob `4e959e003bbdd5b51e336ee669bd761eba00d7fc`, the required identity.
- **(d)** `changed_paths.py` → `1612 changed path record(s)`, blob `156a000493907577ec05d8203a0c9b5992d94d96`. It was
  compared with the previous stop capture (blob `fd3a25f4…`, `1607 changed path record(s)`) by Grep, record class
  by record class:
  - **Non-rename tracked records** (` M` and `RM`): the same 60 lines at the same line numbers (1–37, 811, 835,
    1016–1038) in both captures.
  - **`R` records:** 978 in each capture, at the same line range. Compared by count and position only. The
    staged capture, which lists the same renames, is byte-identical.
  - **Untracked records under `scratch_artifacts/`:** 387 in each. Compared by count only.
  - **Other untracked records:** identical line for line, except for five inserted records, all on the allowed
    list:
    - `records/cc/instructions/cc_instruction_root_records_move_finish_2026_09_17.md` (line 1046);
    - `records/cc/reports/cc_report_root_records_move_2026_09_17.md` (line 1170);
    - `records/cc/reports/cc_report_root_records_move_finish_2026_09_17.md` (line 1171);
    - `records/cc/reports/cc_report_root_records_move_finish_second_2026_09_17.md` (line 1172);
    - `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_one.md` (line 1222).

  1607 + 5 = 1612. There was no STOP.
- **(e)** `python tools/audit/gen_guard_state.py --check` → exit 1, blob
  **`d3774d3735639fcf8a604ee5d357a94933f2305f`**. That is **the same blob** as the previous Task 5(b) capture, so
  every guard's result is equal. Its last line is `81 guard(s) run, 24 failing, 4 not run, 16 historical
  record(s)`, and its first line is `STALE vs the run: guard_state.json does not re-derive`. This capture is the
  reference run.

## 3. TASK 1 — the 43 quotes

### (a) The set

- **The failing lines.** Blob `9cfcddcb…` carries exactly 43 `verbatim NOT FOUND` lines, for the dispatch's 43
  identities.
- **The `verbatim` fields.** A Grep of `backbone_decisions.json` for moved-family names not preceded by `/` found
  hits on each of the 43 entries' `verbatim` lines (lines 3681, 4180, 4267, 4296, 4326, 5706, 8749, and
  13929–14630). The 26 distinct names are listed in (b). One Glob confirmed all 26 exist under `records/`.
  D-252's `` `cc_instruction_*.md` `` is a pattern, not a moved file, and was left alone.
- **The homes.** A Grep over the four home files (`CLAUDE.md`, `cowork_audit_protocol.md`,
  `cowork_design_doc_template.md`, `docs/implementation_roadmap.md`) for the same names not preceded by `/`
  returned **no match**. So each home carries these names only as `records/…` paths.
- **Where each quoted passage starts.** Each opening line was located by Grep, and each path line was checked to
  fall inside the passage:
  - `cowork_audit_protocol.md`, **25 entries**, each opening at its cited line: D-252 (239, path at 242), D-640
    (612), D-641 (1015), D-642 (1117), D-643 (1154), D-644 (1181), D-645 (1354), D-646 (987), D-647 (896), D-648
    (926), D-649 (1212), D-650 (1236), D-653 (1334), D-654 (1387), D-655 (1091), D-657 (952), D-658 (1306), D-661
    (729), D-663 (590), D-668 (1263), D-669 (863), D-670 (1411), D-671 (1458), D-672 (1496), D-673 (762). The
    paths sit on the line after each heading, or two lines after.
  - `docs/implementation_roadmap.md`: **D-416**, opening at 28, path at 33.
  - `cowork_design_doc_template.md`: **D-674**, opening at 120, path at 125.
  - `CLAUDE.md`, **16 entries**:
    - eight opening at their cited line: D-651 (157, path 158), D-676 (388, 389), D-662 (420, 421), D-677 (448,
      450), D-664 (594, 596), D-666 (616, 617–618), D-667 (635, 636–637), D-652 (651, 652);
    - eight opening elsewhere: D-199 (1432, path 1441), D-249 (1836, 1837), D-253 (1850, 1851), D-254 (1893,
      1894), D-294 (976, 977), D-656 (1083, 1086 and 1089), D-660 (1616, 1617), D-675 (1714, 1716).
- **Total:** 25 + 1 + 1 + 16 = **43**, exactly the dispatch's list. There was no STOP.

### (b) The edits

All edits are in `tools/audit/decisions/backbone_decisions.json`, inside `verbatim` fields only. There were
**44 Edit calls**: one per changed passage, and D-642 has two passages far apart. Each edit put a folder prefix
before a root name and changed nothing else. **Before → after**, as the root name and the prefix it gained:

| Entry | Root name(s) in the quote | Prefix added |
|---|---|---|
| D-199 | `cc_key_emission_headroom_dossier.md` | `records/cc/reports/` |
| D-249, D-252, D-253, D-254, D-416 | `cowork_handoff.md` | `records/cowork/handoff/` |
| D-294 | `cowork_handoff_archive.md` | `records/cowork/handoff/` |
| D-640 | `cc_instruction_phase1_delegations_and_corrections.md` | `records/cc/instructions/` |
| D-641 | `cc_instruction_commit_and_finish_line.md` | `records/cc/instructions/` |
| D-642 | `cc_instruction_c1_ruling_and_item1c.md`; `cc_instruction_finish_line_item1b.md` (two edits) | `records/cc/instructions/` |
| D-643 | `cc_instruction_c1_ruling_and_item1c.md` | `records/cc/instructions/` |
| D-644 | `cc_instruction_guard_fix_and_item1d.md` | `records/cc/instructions/` |
| D-645 | `cc_instruction_five_rulings.md` | `records/cc/instructions/` |
| D-646 | `cowork_rulings_2026_08_08_pre_away.md` | `records/cowork/rulings/` |
| D-647 | `cowork_ruling_guard_family_2026_08_08.md` | `records/cowork/rulings/` |
| D-648, D-649, D-651 | `cowork_rulings_2026_08_09_return.md` | `records/cowork/rulings/` |
| D-650 | `cowork_rulings_2026_08_09_return.md`, `cowork_rulings_2026_08_09_second_stop.md` | `records/cowork/rulings/` |
| D-652, D-653 | `cowork_rulings_2026_08_09_second_stop.md` | `records/cowork/rulings/` |
| D-654, D-655 | `cowork_rulings_2026_08_09_third_stop.md` | `records/cowork/rulings/` |
| D-656 | `cowork_rulings_2026_08_09_second_stop.md`, `cowork_rulings_2026_08_09_fourth_stop.md` | `records/cowork/rulings/` |
| D-657, D-658 | `cowork_rulings_2026_08_09_fourth_stop.md` | `records/cowork/rulings/` |
| D-660, D-662, D-663 | `cowork_rulings_2026_08_09_fifth_stop.md` | `records/cowork/rulings/` |
| D-661 | `cowork_rulings_2026_08_09_fifth_stop.md`, `cowork_rulings_2026_08_09_sixth_stop.md` | `records/cowork/rulings/` |
| D-664 | `cowork_rulings_2026_08_09_sixth_stop.md` | `records/cowork/rulings/` |
| D-666, D-667 | `cowork_rulings_2026_08_11_tenth_stop.md`, `cowork_rulings_2026_08_09_ninth_stop.md` | `records/cowork/rulings/` |
| D-668 | `cowork_rulings_2026_08_11_tenth_stop.md`, `cowork_rulings_2026_08_09_eighth_stop.md` | `records/cowork/rulings/` |
| D-669, D-670 | `cowork_rulings_2026_08_11_eleventh_stop.md`, `cowork_rulings_2026_08_11_tenth_stop.md` | `records/cowork/rulings/` |
| D-671, D-672 | `cowork_rulings_2026_08_11_twelfth_stop.md` | `records/cowork/rulings/` |
| D-673 | `cowork_rulings_2026_08_11_fourteenth_stop.md`, `cowork_rulings_2026_08_11_thirteenth_stop.md` | `records/cowork/rulings/` |
| D-674 | `cowork_rulings_2026_08_11_fourteenth_stop.md` | `records/cowork/rulings/` |
| D-675, D-676 | `cowork_rulings_2026_08_11_fifteenth_stop.md` | `records/cowork/rulings/` |
| D-677 | `cowork_rulings_2026_08_13_seventeenth_stop.md` | `records/cowork/rulings/` |

**Check after the edits.** The same Grep, restricted to lines containing `"verbatim":`, now hits 8 lines: 14684,
18225, 18333, 18387, 18441, 18495, 19345 and 20357. **None of them is one of the 43 lines.** Their entries were
not in the `NOT FOUND` list, and they were not touched. No cited line number was changed.

### (c) Regeneration and checks

1. `gen_decisions_register.py` → `wrote 20 files: DECISIONS.md (the index, 861 lines) + 19 group files under
   decisions/ (477 decisions)` (blob `cb789fc6…`, the same blob as the previous batch's generate capture). Its
   `--check` → `the register matches the data (20 files: the index + 19 group files)` (blob `574a9d24…`, the same
   blob as before). Both exited 0.
2. `gen_cluster_dispositions.py --verify` → exit 1 (blob `a1b18675b426d504c273425971a8f569bbc5d0b8`):
   - `verbatim quotes found at their cited home: 477/477` (before: 434/477);
   - `cited line numbers correct: 436/471` (before: 401/428);
   - **no `MISS` line**;
   - 35 `LINE DRIFT` lines: the 27 of blob `9cfcddcb…`, unchanged, plus exactly the eight allowed, each at the
     start line the first run's report gives: D-199 → 1432, D-249 → 1836, D-253 → 1850, D-254 → 1893,
     D-294 → 976, D-656 → 1083, D-660 → 1616, D-675 → 1714;
   - no `DANGLING` or `FIELD SHAPE` line; `cross-references resolving: ALL`.

   **The arithmetic:**
   - quotes found: 434 + 43 = 477;
   - lines checked: 477 found − 6 cited to a file with no line number = 471 (before: 434 − 6 = 428);
   - lines correct: 401 + 43 − 8 = 436;
   - drifts: 471 − 436 = 35 = 27 + 8.
3. `gen_cluster_dispositions.py --check` → `OVERALL PASS` (blob `04acff01…`). `--producible` → `OVERALL PASS`
   (blob `1f0f046c…`). Its write mode was not run.
4. **The Task 1 state:** `changed_paths.py` → `1614 changed path record(s)`, blob
   `877025ef83e0a35ae2e20528b4ce07ab2f3121e9`. Against Task 0(d), the new ` M` records are `decisions/group_I.md`
   (D-416) and `decisions/group_K.md` (D-674). Both are Task 1 files. 1612 + 2 = 1614.

## 4. TASK 2 — as far as it ran

**Reading before running.** For all nine tools, the docstring and `main` were read, together with the `OUT`
constant. Nothing read contradicted the table:
- `gen_claude_md_finer_archive.py`, `gen_post_split_archive.py` and `gen_claude_md_prune_backlog.py` call
  `apply_move()` only under `--apply`.
- The prune-backlog tool's second path, `FRESH_COARSE`, is only read.
- In `gen_derivation_boot_pack.py`, `build` loops over `WITHHELD` (lines 601–733: `harmony-boundary`,
  `scoring-model`, `l0-l1`), and `FROZEN` (lines 334–410) names the same three. `write_all` skips every frozen
  subject, so a plain run writes only the manifest.
- `gen_rulings_sort.py` writes the artifact and the surface.

**Runs, in the table's order**, each write mode followed by its `--check`:

| # | Command | Exit | Output (blob) |
|---|---|---|---|
| 1 | `gen_discard_records.py` | 0 | `wrote tools\audit\discard_records.json`; entered 2, conforming 2, not conforming 0; retired 1 — OI-373 (`781a1d6f…`) |
| 1 | `… --check` | 0 | `the discard records re-derive from the record` (`4eec2b8c…`) |
| 2 | `gen_specification_document_set.py` | 0 | `wrote tools\audit\specification_document_set.json`; targets named 68; namings 199; admitted 25; members 26; with no file 0; seed misses 5 of 25 (`2403def1…`) |
| 2 | `… --check` | 0 | `the specification document set re-derives` (`9ffbd307…`) |
| 3 | `gen_rulings_sort.py` | 0 | wrote both files; DESIGN-INTENT 244, IMPLEMENTATION-MANAGEMENT 167, NEEDS-THE-USER 0 (`de908534…`) |
| 3 | `… --check` | 0 | `the rulings sort re-derives` (`1db06e84…`) |
| 4 | `gen_claude_md_finer_archive.py` | **1** | see §0 (`00ccfa9b…`) — **STOP** |
| 4 | `… --check` | 1 | see §0 (`f61de75e…`) |

**Not run:** tools 5–9 (`gen_post_split_archive.py`, `gen_claude_md_prune_backlog.py`,
`gen_session_start_read_size.py`, `gen_defense_share.py`, `gen_derivation_boot_pack.py`), and Task 2(b) and (c).
The content of the four rewrites that did happen has not been proved, because Task 3's proof never ran.

## 5. Declared departures and bounds

1. **Session-start read:** `STATUS.md` whole; `DECISIONS.md` whole, in three pieces; the `gating_ids` list in
   `tools/audit/nongating_apparatus_rows.json`. Read whole before Task 0: the previous report, the previous
   dispatch, and both earlier stop reports of this dispatch.
2. **Captures in the scratchpad.** Every capture was written there and given a blob identity with
   `git hash-object -w`. Three earlier captures were fetched with `git cat-file blob`. Every capture was read with
   Read or Grep only.
3. **A shell variable in commands.** Several commands set `S` to the scratchpad path and redirected output to
   `$S/…`. No shell command read any file through it, and no guard refused anything.
4. **One Grep ran over the whole register data file** (every `"verbatim"` and `"home"` line). Its output was
   saved by the tool, and only the 43 lines were used.
5. **The cause in §0 was read from `gen_claude_md_finer_archive.py`** (a search for `refused`) and from the
   artifact the write mode had just written. The dispatch does not name this reading; it is read-only and only
   supports the report.
6. **Commit and push:** none. Nothing has left the machine.
