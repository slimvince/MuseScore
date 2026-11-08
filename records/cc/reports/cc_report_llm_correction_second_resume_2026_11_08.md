# CC report — the language-model correction, second resume (2026-11-08)

> **A CLAUDE CODE REPORT**, in the two-file form of Ruling 4 of
> `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`. It reports the execution of
> `records/cc/instructions/cc_instruction_llm_correction_second_resume_2026_11_08.md` (pinned at the blob
> `755e9b93da41af13a2703cdf4abdc0197c5eab06`, 66,387 bytes). **Documentation and record-keeping only; no algorithm
> changed.** The raw printouts are in the appendix beside it (named at the end of this file).

## 1. The ordered first read

- **My first tool call** was one Read of `records/cc/instructions/cc_instruction_llm_correction_second_resume_2026_11_08.md`
  and nothing else. It returned a partial view at the tool's page limit (lines 1–641 of 779); my second call read
  lines 642–779 of the same file, before anything else. **Declared.**
- **What reached me as injected context:** `CLAUDE.md` (the whole file as the harness injects it), the auto-memory
  index `MEMORY.md`, the git status snapshot and recent commits, and the commit attribution lines. Nothing else.
- **The eight-line check (Ruling 2 of the 2026-11-01 pruning record).** Each line was located by one search of
  `CLAUDE.md` at the tree with the file tools and compared with the injected copy. **All eight are identical, so the
  six-span read was not performed.**

  | # | Line at the tree | Text as read = as injected |
  |---|---|---|
  | 1 | 1 | `# Claude Code — Standing Instructions for This Repository` |
  | 2 | 3 | `## Guiding principles` |
  | 3 | 313 | `## The open-items register (user-directed, 2026-07-10; split into index + detail files, user-ratified 2026-07-26)` |
  | 4 | 488 | `## The decisions register (shape user-ratified 2026-07-28; content + living surface 2026-08-02)` |
  | 5 | 704 | `**Always read these two files at the start of every session:**` |
  | 6 | 1536 | `## Conventions` |
  | 7 | 1985 | `## The self-check after every coding exercise (user-directed, 2026-07-11)` |
  | 8 | 1994 | `memory of writing it. This applies to CC sessions and Cowork sessions alike.` (the last line carrying text) |

  During this check a PowerShell `Get-Item` size probe of `CLAUDE.md` was refused by the shell-read guard; nothing was
  read through it. **Declared.**
- **Then, in the dispatch's order:** `STATUS.md` whole; `DECISIONS.md` whole (two ranges, page limit);
  `BUILD_AND_TEST.md` whole; `gating_ids` at `tools/audit/nongating_apparatus_rows.json`; `cowork_audit_protocol.md`
  from `## The dispatch protocol these audits are commissioned and run under` (line 180) to its end (line 1606), in
  several ranges because of the page limit — its marked standing clauses bound this batch; the highest-numbered handoff
  entry on disk, **entry 585** (located by listing; no entry numbered above it), whole; the correction record whole;
  `tools/audit/gen_specification_document_set.py` at 153–164, 386–388, 422–432, 502–525, 551–572 and 786–807;
  `tools/audit/gen_l3_outgoing_population.py` at its `L3_KEYWORDS` list (lines 155–164).
- **Further reads, declared:** the set tool's lines 571–587 after the edit; `tools/audit/period_stratum_split.json`
  lines 2272–2277; `tools/audit/l3_outgoing_population.json` lines 20100–20117; `tools/audit/gen_status_batch_bound.py`
  at 2440–2489, 2690–2734, 2985–3024, 3270–3299 and 3940–3979 (to re-aim it), and a scratch copy of that tool at the
  start tip searched for its constants; `tools/audit/status_batch_bound.json` at `the_moved`; `STATUS.md` lines 7–18
  after the move; `.git/refs` files; the reading files at their four matched lines only;
  `records/cowork/handoff/cowork_away_returns.md` at its last section (Task 3(e)).
- **Capacity judgment.** The batch fitted in one session with no stop. No step was shortened on capacity grounds.

## 2. Task 0 — the records landed and pushed

- **0(a) the pin.** `git hash-object -w --no-filters` of the dispatch gave `755e9b93da41af13a2703cdf4abdc0197c5eab06`,
  `git cat-file -s` 66,387. It was re-hashed immediately before staging (equal), and the staged index entry carries that
  blob. **Declared departure (the P-2 route of `cowork_audit_protocol.md`):** the dispatch was read from the working
  tree before it was pinned, because the opening line named only the file; the blob was proved unmoved before staging.
- **0(b) the refs and the chain.** Both ref files at `257ad5bfc1915f63c1e0b7e54da5692e6003e64b`. `git cat-file -p`
  of the four named commits, one command each: `257ad5bf…` → parent `778c459b…` → parent `acbb2d7c…` → parent
  `d46a7b48…` → parent `4461d865fcb2c99ef20099487c0d4a4221456112`. **The chain holds.**
- **0(c) A1 and the landing set** (`python tools/audit/changed_paths.py`, 404 records). Tracked modifications: exactly
  the three of A1 (`docs/research_papers/BIBLIOGRAPHY.md`, `docs/research_papers/README.md`,
  `tools/audit/claude_md_finer_archive.json`). A1's two untracked items present: `docs/research_papers/polyph9-release/`
  and `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`. **Every untracked path under the five record
  folders is a path of the landing set, and every path of the landing set is untracked**: handoff entries 581, 582,
  583, 584 and 585; the resume report and its appendix; this dispatch — **eight paths**. Every other untracked path is
  under `scratch_artifacts/`, `Claude outputs/`, `Codex research inventory/` or `external resarch summary/` — taken as
  the standing population (observation 4). **A1 holds; no STOP.**
- **0(d) last bytes** (one scratch script, quoted whole in the appendix). Every landing file ends with a newline after
  a complete line and holds no zero byte. Sizes: entry 581 **8,243**, entry 582 **9,044**, entry 583 6,095, entry 584
  4,843, entry 585 5,909, the resume report **17,255**, its appendix **82,972**, the dispatch 66,387. The four the
  premise ledger states all match.
- **0(e) the commit.** Staged by explicit path; `changed_paths.py --staged` → **8**, equal to the landing set. Subject
  `record: handoff entries 581 to 585, the resume batch's report, with the second resume dispatch`. Commit
  `9a2b3c2d9a00f94ea2cf67f2dcf0832a3a65fbce` (**`<T0>`**), pushed; `.git/refs/remotes/origin/master` read equal.
- **0(f) the opening capture.** Header `STALE vs the run: guard_state.json does not re-derive`; tally **83 run,
  15 failing, 4 not run, 20 historical**. Failing set by name: `gen_phase3_gate_partition.py`,
  `gen_filing_convention_application.py`, `gen_specification_document_set.py`, `gen_artifact_inventory.py`,
  `gen_artifact_inventory_surface.py`, `gen_test_construction_evidence.py`, `gen_retirement_caller_check.py`,
  `decisions/apply_soft_discard.py`, `decisions/apply_residue_discard.py`, `gen_per_session_reading.py`,
  `gen_epoch_write_path.py`, `gen_recognizer_establishment_sort.py`, `decisions/gen_cluster_dispositions.py --verify`,
  `decisions/gen_home_classification.py`, `decisions/gen_phase1p_delegation_bar.py` — **exactly A2's fifteen**. Zero
  STOPs in the runner. The start tip's `tools/audit/guard_state.json` → `summary`, read at the object: run 83,
  passing 70, failing 13 (the thirteen standing reds, named in the appendix), not run 4, historical 20.
  `gen_guard_classification.py --check`: **exit 2**, STOP naming `gen_l0_l1_outgoing_population.py`,
  `gen_l2_withheld_documents.py`, `gen_l3_outgoing_population.py`, `gen_per_session_reading.py`,
  `gen_withheld_family_reading.py` — the five of the premise ledger.

**E0: met.**

## 3. Task 1 — the three grades; the set and split artifacts regenerated

- **1(a) the edit.** The two-line `old_string` (lines 571–572) occurred once. The fifteen lines were inserted as the
  dispatch gives them. **Proof:** line count 1,122 → 1,137 (+15, by a line-count search); `--numstat` in blob form
  (`f22c8923…` → `9c03a652…`) **`15 0`**; the new lines read back at 572–586 and `}` at 587; `ast.parse` passes.
  **Declared departure:** the dispatch's `python -c "…open('tools/audit/…')…"` was refused by the shell-read guard
  (a code string carrying a literal repository path, D-253). The same `ast.parse` was run over the file's git object
  (`git cat-file blob 9c03a652… | python -c "…sys.stdin…"`): **ast ok**.
- **1(b) the set artifact.** `--check` before: exit 1, `STALE: specification_document_set.json does not re-derive`
  (no STOP printed). The bare (writing) invocation, then `--check`: **exit 0**. The diff against the start tip's blob (`b28deb58…` →
  `ea8e05b8…`, numstat `46 4`) holds exactly:
  - the `counted` block: `targets_named_in_ARCHITECTURE.md` **68 → 71**; `namings_scanned` **199 → 202**;
    `bare-appended-citation` **17 → 18**; `provenance-attribution` **21 → 23** — the four lines removed are these four
    values;
  - three added records in the graded list, sorted by target, each carrying `target`, `form`, `admitted` false,
    `why_this_grade` (1(a)'s text verbatim), `decided_by` `rule_(i)_not_admitted`, one naming at `line` 8089 with the
    whole banner line as `line_text`, and `namings_counted` 1 — for `docs/llm_triage_design.md`
    (`bare-appended-citation`), `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md` and
    `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` (both `provenance-attribution`).

  **Tied:** every changed passage publishes one of the three new grades or the banner's namings of the three targets,
  or is one of the four counts they move. `targets_ADMITTED`, `members_total` and every member count did not move;
  **no member entered or left** (no member line is in the diff).
- **1(c) the split artifact.** `--check` before: exit 1, `FAIL: re-derivation differs from the committed artifact`.
  The bare (writing) invocation, then `--check`: **exit 0**. The diff (`7e6378d3…` → `d2c57a3d…`, numstat `1 1`): exactly one line, line
  2276, the `sha256` under `the_document_set` (read back at lines 2274–2276):
  `4a3e70df108120c6249582e0c0c5a88514805fe59a1f106772900b15ee1b0193` →
  `09f4db3f9b7326eaad56cd15e788a710898899dbaa43c9e8543a9cb15e286502`. The SHA-256 of the set artifact 1(b) wrote,
  computed over its blob `ea8e05b8…`: **`09f4db3f9b7326eaad56cd15e788a710898899dbaa43c9e8543a9cb15e286502` —
  equal.** **Declared departure:** computed over the blob piped into `python -c`, because the dispatch's literal-path
  form would meet the same guard denial as 1(a).
- **1(d) the commit.** Staged set proved, count **3**. Commit `1e563b8c9cb52dd1e6fff1039f9abe09be4f4682` (**`<T1>`**),
  pushed, `origin/master` read equal.
- **1(e) the capture after `<T1>`.** Same header; **83 run, 14 failing, 4 not run, 20 historical**. The one changed
  verdict: `gen_specification_document_set.py --check` **FAIL → PASS**. `gen_period_stratum_split.py --check` PASS at
  both. Failing set: exactly the fourteen. **No tool newly FAIL, so A2's rule did not fire and no regeneration commit
  was made.**

**E1: met.**

## 4. Task 2 — the reading files annotated (Ruling 1 items 5 and 6)

- `<ACT_DATE>` = **2026-11-08**. Each `old_string` was located by one exact-text search (one hit each, at 72468 and
  72557 in L2, 10142 in L0/L1 and 30466 in L3) and only the matched line was read before the edit.
- **Proof:** line counts unchanged — L2 78,957, L0/L1 16,404, L3 83,443. `--numstat` in blob form against `<T1>`:
  **L2 `2 2`, L0/L1 `1 1`, L3 `1 1`**. The changed lines in the diffs are at exactly 72468, 72557, 10142 and 30466, and a
  read-back search finds each annotation at those four line numbers and nowhere else in the three files.
- **The commit.** Staged set proved, count **3**. Commit `468aac14856d2cabf6cc5f9ee58678b7073d5c24` (**`<T2>`**), pushed,
  `origin/master` read equal.
- **2(d) the capture after `<T2>`.** Same header; **83 run, 14 failing**, and **no verdict differs** from 1(e).
  **No tool newly FAIL; no regeneration commit.**

**E2: met.**

## 5. Task 3 — the close

- **3(a) the `STATUS.md` entries.** Four entries written at the top, above the records landing's close entry: the
  close entry (with `Last updated: `, naming this dispatch), then Tasks 2, 1 and 0, each opening `Same dispatch`. In
  the same edit `Last updated: ` was removed from the records landing's close entry and nothing else of it changed. A
  read after the edit: **exactly one line carries `Last updated: `**. **The search** (case-insensitive, substring;
  every `L3_KEYWORDS` term plus *repeat* and *tie* — 28 terms, listed in the appendix): **one hit**, `phrase`, at line
  26 at that moment — inside *paraphrase*, in the paraphrase paragraph. **No hit in my entries.**
- **3(b) the forward bound.** The constants at the object `257ad5bf…:tools/audit/gen_status_batch_bound.py` **as
  found**: `BASE_COMMIT` `113b2ce680e527e81342d8f79d5acbad281334d7`, `PREVIOUS_BATCH_DISPATCH`
  `cc_instruction_boot_chain_landing_2026_11_02.md`, `DISPATCH` `cc_instruction_records_landing_2026_11_07.md`,
  `TASK` `Task 3`, `MOVE_KIND` `ordinary`, `ACT_DATE` 2026-11-07 — **equal to the relayed expectation**. **As set:**
  `BASE_COMMIT` `468aac14856d2cabf6cc5f9ee58678b7073d5c24` (`<T2>`; 2(d) made no regeneration commit);
  `PREVIOUS_BATCH_DISPATCH` `cc_instruction_records_landing_2026_11_07.md`; `DISPATCH`
  `cc_instruction_llm_correction_second_resume_2026_11_08.md`; `TASK` `Task 3` and `MOVE_KIND` `ordinary` (unchanged,
  so no comment was added, as at the batches before); `ACT_DATE` 2026-11-08; one row appended to `PREVIOUS_AIMINGS`.
  The head comments carry a new re-aiming paragraph and two re-statement lines, each former value named. **The
  `STATUS.md` blob at `BASE_COMMIT` equals its blob at the start tip** — `13bc8197c41680c3d15a72f7fe6fe1f2fc1f8744` at
  both, one `git rev-parse` per commit. `--apply`: *entries moved: 2, 1,307 characters; byte-present in the archive
  exactly once: True; absent from the must-read: True*. **`the_moved`**: the records landing's close entry
  (`line_at_base` 8, 999 characters, the declared adjustment applied) and its Task 0 `Same dispatch` entry
  (`line_at_base` 10, 308 characters). The two 2026-09-02 entries stayed. **The prediction held; no STOP.** The four
  archive checks, each in its own call: `gen_status_batch_bound.py --check`,
  `gen_governing_surface_split.py --check --pair STATUS.md`, `gen_status_residue_move.py --check`,
  `gen_status_archive_pass.py --check` — **all exit 0**.
- **3(c) the regenerations** (each checked first, in its own call; diffs in blob form against `<T2>`):

  | Artifact | Check before | Regenerated | Check after | What moved |
  |---|---|---|---|---|
  | `session_start_read_size.json` | exit 1 (STALE) | yes | exit 0 | the `STATUS.md` member 10,585 → 11,617; `total_characters` 236,984 → 238,016; the two comparisons built on the total (`to_total`, `change_in_characters`, `change_percent`: −130,137 / −35.45 → −129,105 / −35.17 and −59,848 / −20.16 → −58,816 / −19.81) |
  | `defense_share.json` | exit 1 (STALE) | yes | exit 0 | the whole-read denominator 236,984 → 238,016; the share 5.47 → 5.44 |
  | `l3_outgoing_population.json` | exit 1 (STALE) | yes | exit 0 | one value inside its `STATUS.md` residue record: the hit record's `line_number` 18 → 22 (the paraphrase paragraph's line after 3(a) and 3(b); the term `phrase`, the hit count 1, unchanged). **No member of either population, nor of `the_tabulation_population`, moved.** |
  | `l0_l1_outgoing_population.json` | exit 0 | no | — | — |
  | `derivation_boot_pack` manifest | exit 0 | no (not to be) | — | — |
  | `per_session_reading.json` (LAST) | exit 1 (STALE) | yes | exit 0 | see below |

  **`per_session_reading.json`** (numstat `44 30`), every changed passage accounted for:
  - the ordinary read: the `STATUS.md` member 10,585 → 11,617 (this batch's 3(a) and 3(b));
  - **the `DECISIONS.md` member 117,490 → 118,132 — a movement the dispatch did not name, reported by field.** Its
    cause was established at the objects. `DECISIONS.md` changed between the records landing's commit `113b2ce6…`
    and the start tip (`git diff --numstat` → `9 9`, the first stopped batch's supersession of D-440 to D-448). Its
    blob is `262c97c1…` at both the start tip and `<T2>`, so this batch did not change it. The artifact had been last
    made current at the records landing, so this is a stale input catching up, not this batch's act;
  - the ordinary read's total 236,342 → 238,016 (= +1,032 + 642), and every mirror of it (the share 5.48 → 5.44 and
    the `the_whole_ordinary_session_start_read` value);
  - **`the_reports_with_an_appendix_beside_them`**: `count` 7 → 9; two pairs added —
    `cc_report_llm_correction_2026_11_07.md` (12,837 + 21,746 characters) and
    `cc_report_llm_correction_resume_2026_11_07.md` (17,111 + 81,316); the two sums 241,593 → 271,541 and
    1,083,378 → 1,186,440, higher by exactly those characters (not the byte sizes of 0(d));
  - **the handoff population** 489 → 505 (+16: entries 570 to 585);
  - **`the_cowork_boot_chain`**, the three latest entries as the tool orders them: **581, 583, 582** (each
    `added_in_commit` `<T0>`, each `added_at_unix_time` 1794134795); 8,186 + 6,062 + 8,984 = 23,232 characters
    (was 22,382). **How the equal add-commit times were split:** entries 581 to 585 were all added at `<T0>`. The tool
    takes the three whose names sort last — *eighty_one*, *eighty_three*, *eighty_two* — and lists them in ascending
    name order. So the boot chain names 581, 582 and 583, not the numerically latest 583, 584 and 585. This is the
    carried name-order tie-break the dispatch lists, and it is **observation 2**;
  - the sums built over these (`without_the_injected_copy_of_CLAUDE_md` 672,856 → 675,380, `with_it` 842,038 →
    844,562, `under_ruling_2_of_2026_11_01` 736,597 → 739,121, the overall `characters` 972,160 → 974,684 — each
    +2,524 = 1,674 + 850).

  The dispatch and report populations did not move.
- **3(c′)** runs after this file and its appendix are final. Its output and diff are in the away-returns section, not
  here.

**E3: met for 3(a) to 3(c)** (every check 3(b) and 3(c) name is green at the tree; 3(f)'s close is in the away-returns
section; `guard_state.json` stays stale until Task 4).

## 6. Commits

| Task | Commit | Parent | Committed blobs |
|---|---|---|---|
| 0 | `9a2b3c2d9a00f94ea2cf67f2dcf0832a3a65fbce` | `257ad5bfc1915f63c1e0b7e54da5692e6003e64b` | 8 |
| 1 | `1e563b8c9cb52dd1e6fff1039f9abe09be4f4682` | `9a2b3c2d9a00f94ea2cf67f2dcf0832a3a65fbce` | 3 |
| 2 | `468aac14856d2cabf6cc5f9ee58678b7073d5c24` | `1e563b8c9cb52dd1e6fff1039f9abe09be4f4682` | 3 |

The close commit and the end-state commit are recorded in the away-returns section, because this file is final before
both.

## 7. Grades

- **E0, E1, E2: met. E3: met for what is on disk when this file is final** (above).
- **A1: holds** (0(c)); the five standing items untouched, unstaged, uncommitted.
- **A2: holds.** The opening capture failed exactly the fifteen with zero runner STOPs. 1(e) and 2(d) each changed
  exactly as predicted, or not at all. **No tool was newly red at 1(e) or 2(d)**, so A2's regenerate-or-carry rule
  never fired. Task 3's reds were the named ones plus `gen_l3_outgoing_population.py`, which the dispatch named as
  possible; all were regenerated green.
- **A3: holds** — no `src/` file, build, test, golden, corpus of scores or measurement of the analysis was touched.
- **A4 and A5:** graded at Task 4, against the name-status list.

## 8. Declared departures

1. The dispatch was read from the working tree before the pin (the P-2 route); proved unmoved before staging.
2. 1(a)'s `ast.parse` and 1(c)'s SHA-256 were run over git objects, because the dispatch's literal-path `python -c`
   forms are refused by the shell-read guard (D-253). The computation is the same; only the route to the bytes differs.
3. A `Get-Item` size probe of `CLAUDE.md` was refused by the guard during the eight-line check; nothing was read.
4. Line counts were taken with a line-count search through the file tools, not `wc`.
5. `DECISIONS.md` and `cowork_audit_protocol.md`'s dispatch-protocol section were read in several ranges because of
   the tool's page limit; each was read through to its end.

## 9. Observations met and not acted on

1. **`gen_l2_outgoing_population.py` is HISTORICAL in the guard runner.** A2 named it as possibly red at 2(d); it is
   not run, so it cannot be.
2. **The boot-chain three-latest pick** names entries 581, 582 and 583 — not 583, 584 and 585 — because the five
   entries share one add-commit time and the tie-break is by name order (3(c)). It is carried, and named again here
   because this batch's own landing produced it.
3. **The `DECISIONS.md` member movement in `per_session_reading.json`** was not predicted by the dispatch; its cause
   is established above (the first stopped batch's decisions-register change), not this batch's act.
4. **Untracked folders outside the five record folders** — `Claude outputs/`, `Codex research inventory/` and
   `external resarch summary/` — were taken as standing population. I did not check them against an earlier
   enumeration, and none of them was touched.
5. **Two of the dispatch's own commands are refused by the shell-read guard** (1(a)'s and 1(c)'s literal-path
   `python -c`). A later dispatch that orders such a check can name the git-object form directly.

## 10. Could this dispatch be executed without reading any earlier dispatch or report?

**Yes.** No step sent me to an earlier dispatch or report. Every value it relayed from them was either stated in the
dispatch or checkable at an object (the chain, the start tip's guard state, the forward-bound tool's constants, the
reading-file lines).

## 11. Tools carried red by this batch — questions for the writing side

**None.** No tool was newly red at 1(e) or 2(d), and every Task 3 red was regenerated green.

## 12. The tell

**No.** This batch produced the landing set, the edited set (the set tool and the three reading files), the set and
split artifacts, the artifacts 3(c) regenerated (`session_start_read_size.json`, `defense_share.json`,
`l3_outgoing_population.json`, `per_session_reading.json`), the Task 3 files (`STATUS.md`, `STATUS_ARCHIVE.md`,
`tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`), this report and its appendix, the
away-returns section, and the end state's guard artifact. Outside the repository there are only scratch files and loose
blob objects (from `git hash-object -w`). Nothing else.

## 13. Self-check (D-434)

1. **Guiding principles.** #6: one path per concern — the grades went into the set tool's one authored table, and no
   second home was made. #10 and #12: every annotated text was kept, no line was added to a reading file, and the moved
   `STATUS.md` entries are byte-present in the archive. #14: no behaviour change of the analysis. #15: every
   regenerated artifact was verified at its diff, field by field. #19: an unpredicted movement (`DECISIONS.md`) was
   established at the objects before it was reported as tied.
2. **Conventions.** American English; no invented labels; *measurement tool* rather than the reserved word; the
   musical words are not used in a non-musical sense in my own text (the dispatch's word for the equal add-commit
   times is quoted only as *tie-break*).
3. **Values and premises.** Every value in this report is copied from a generated artifact or a printout quoted whole
   in the appendix, as the dispatch orders the report to state them. Every premise is cited to its object.
4. **The file-tools rule.** Working-tree content was read with the file tools. The shell was used for git object
   queries by explicit hash, git's write acts (add, commit, push, `hash-object -w`) and the sanctioned scripts. Every
   guard refusal is declared above.
5. **Uncertainty.** No difference between measured quantities is asserted.

## 14. The appendix

`records/cc/reports/cc_report_llm_correction_second_resume_2026_11_08_appendix.md`, **95,734 bytes**, 43 sections.
It holds: the inline command transcripts of 0(a), 0(b), 0(e), 0(f), 1(a), 1(c), 1(d), 2, 3(a), 3(b) and 3(c); A1's
enumeration whole; 0(d)'s script and output; the opening capture whole and the classification STOP; the two scratch
scripts used for every blob diff and capture comparison, quoted whole; 1(b)'s and 1(c)'s three outputs and diffs each;
the capture after `<T1>` whole and its comparison; the three reading files' numstats and diffs; the capture after
`<T2>` whole and its comparison; 3(b)'s `--apply` and the four archive checks; every 3(c) check, write and diff; and the
assembler that built it, quoted whole.
