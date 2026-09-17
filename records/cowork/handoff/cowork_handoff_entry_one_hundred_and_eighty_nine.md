# Cowork handoff entry 189 — 2026-09-16 (short entry, written after a context compaction)

## 0. Read this first

This session's context was **compacted automatically** during its last act. The exact text of the conversation up
to that point was lost; only a summary survived. This entry therefore separates two grades of fact:

- **[checked]** — opened at the file, or re-staged and measured, **after** the compaction.
- **[summary]** — carried by the compaction summary only; **not re-verified**. Reopen the named object before
  relying on it.

Two degradation tells were recorded against this session: reading past the capacity point instead of handing over,
and stating counts in chat from the summary instead of from the report. Neither figure is carried into this entry.

**Filed at `records/cowork/handoff/`**, the first file there, because the user ruled that record files cannot stay
in the repository root (quoted in the reference-map dispatch, lines 6–7). The layout it sits in is **proposed, not
ratified** (§3).

## 1. Boot order for the next session

1. The session-start read as `cowork_handoff_entry_one_hundred_and_eighty_eight.md` (root) orders it in its Boot block.
2. This entry, whole.
3. **Re-read whole** the latest dispatch:
   `records/cc/instructions/cc_instruction_root_records_reference_map_2026_09_16.md` (7,036 bytes).
4. **Re-read CC's entire answer to it:**
   - its report, `records/cc/reports/cc_report_root_records_reference_map_2026_09_16.md` — 11,423 lines, about
     800 KB. The Read tool refuses chunks over 25,000 tokens; chunks of roughly 330–450 lines fitted in this session.
     **Plan capacity around this read:** it is what exhausted this session.
   - CC's **chat reply** to that batch. It is **not on disk**; ask the user to paste it again.
5. Only then write anything.

## 2. State at close [checked]

- `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both read `5d24edb565b2e0e9efc92e082c163112bd97087f`
  — unmoved from the 188th entry's figure.
- The second backup the 188th entry's §5 recommends is **still undone**. Nothing was committed or pushed this session.
- Files this session landed, each re-staged after the compaction and matching its proven size:

| Path | Bytes | Run status |
|---|---|---|
| `cc_instruction_second_backup_commit_and_push_2026_09_16.md` (root) | 11,568 | CC stopped [summary] |
| `cc_instruction_second_backup_rerun_2026_09_16.md` (root) | 10,964 | CC stopped [summary] |
| `cc_instruction_second_backup_rerun_two_2026_09_16.md` (root) | 11,941 | never run [summary] |
| `records/cc/instructions/cc_instruction_root_records_reference_map_2026_09_16.md` | 7,036 | ran, no stop [summary] |

- CC's reports on the two stopped backup batches sit at the root, uncommitted:
  `cc_report_second_backup_commit_and_push_2026_09_16.md`, `cc_report_second_backup_rerun_2026_09_16.md`.
  Their stop reasons (a file-type check that did not list `.mscx`; a byte read and an `awk` read refused by the
  shell-read guard) are [summary] — reopen the reports.
- **Why the backup was paused:** the user asked why the root holds so many record files, and ruled they cannot stay
  there. The plan became: move them, fix references, then commit and push — which is also the backup.

## 3. The proposed layout [checked — from the map dispatch, lines 9–17]

```
records/
  cowork/
    handoff/        cowork_handoff_entry_*.md, cowork_handoff.md, cowork_handoff_archive.md
    rulings/        cowork_rulings_*.md, cowork_ruling_*.md
  cc/
    instructions/   cc_instruction_*.md
    reports/        every other root cc_*.md
```

Other root `cowork_*.md` files are outside the move. **Not ratified by the user.**

## 4. Findings confirmed at the files after the compaction [checked]

1. **`tools/audit/gen_rulings_sort.py`** writes root paths to two rulings records into its constants — line 111
   `ROOT / "cowork_rulings_2026_08_16_preparation_return.md"`, line 118
   `ROOT / "cowork_rulings_2026_08_17_rulings_sort_sitting.md"` — and its docstring states that a sentence it cannot
   locate STOPS it (line 235). Moving the rulings breaks it unless its paths change.
2. **`tools/audit/decisions/gen_decision_harvest.py`** globs the root: line 152 `md_glob("", "cowork_*.md", …)`,
   line 166 `md_glob("", "cc_*.md")`. After a move those globs would return nothing, with no stop.
3. **`tools/audit/gen_artifact_inventory.py`** classifies files by root-name prefix (lines 246–270) and its docstring
   states an unclassified file is a STOP (lines 31–32).
4. **The layout misses three rulings prefixes.** The same tool (lines 246–249) counts five prefixes as rulings
   records: `cowork_rulings_`, `cowork_ruling_`, `cowork_owner_rulings_`, `cowork_pending_rulings_`,
   `cowork_document_route_rulings_`. §3 covers the first two only. It also names `cowork_away_returns.md` and the
   `cowork_instruction_` prefix beside `cowork_handoff.md` (lines 251–255).
5. **`.gitignore` line 116** is `/cc_e2d_*.md` — anchored at the root, so it stops covering those untracked reports
   once they move. Line 121 `tools/cc_*` is a separate rule on `tools/`.
6. **CC's report, lines 10318–11423** (read after the compaction): `decisions/group_*.md` GENERATED by
   `gen_decisions_register.py`; every `open_items/OI-*.md` marked UNDECIDED on one shared ground (line 10335);
   `tools/` non-code classifications; the CODE listing; the Declared section. CC's declared departures (line
   11409–11418): Glob calls without the exclusions; one `grep -v` pipe; `--error-unmatch`; brace globs with a slash
   that did not filter, the affected files then reopened one by one. CC used helper sessions for Task 2(b) (line 11408).
   Two READMEs it marked UNDECIDED were not opened by CC (lines 10897, 10970).

## 5. Carried by the summary only — reopen before use [summary]

- The report's §2(b).1 grouping of tools (hard-coded root paths; root scans; prefix logic; name dependencies;
  pinned-commit reads) and any count of tools in each group.
- The §2(c) LIVE list, including `cowork_handoff.md` classed LIVE as the one exception inside the move population.
- The population sizes in the report's Task 1.
- `pipeline_snapshot_tests.cpp` writing a `cc_instruction_…` name as a label; `jointembeddedartifacts.cpp` lines
  50/113/119/128 content not established by CC.

## 6. Open for the user, one per turn, as full surfaces

1. **How to treat tools that point at the root** — one-off historical tools whose outputs are committed: edit their
   paths, or leave them as records of acts done (and accept they no longer run). Open the report's §2(b) first.
2. The three missed rulings prefixes (§4 item 4), `cowork_away_returns.md` and `cowork_instruction_*`: in the move
   or not.
3. Ratify the §3 layout.
4. Carried from the 188th entry §5: `Claude outputs/` and `Codex research inventory/`; the `.mscx` byte-stability
   question in `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md` §8.

Then: write the move, reference-fix, regenerate, commit and push dispatch from the re-read map.

## 7. This session's standing instructions from the user (the next session receives its own)

No shell in the container or on the device; no listing of the repository root; `docs/research_papers/polyph9-release/`
closed; row 18's Table 3 cell not reopened; decision surfaces in plain text, choice question in a separate later
turn, one decision per turn, no popup; CC's output read in full and verified at the files.
