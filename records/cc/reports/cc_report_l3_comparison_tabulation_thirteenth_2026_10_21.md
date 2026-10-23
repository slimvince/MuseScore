# CC report — the L3 comparison continued at position 35: position 35 tabulated, proposals only — NOTHING DECIDED, NO ALGORITHM CHANGE, NO DECISIONS-REGISTER ENTRY

*Executing `records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md` (pinned at Task 0
to blob `40e64cd2f3afed810bc2917ec86f35df5f1dc20e`, 173,407 bytes). Written 2026-10-21 to 2026-10-23 by Claude Code. This report
decides nothing: every disposition in the reading file is a proposal for the user's later ruling, and no recommendation
is made here about any disposition, any difference, any open question, the derivation or the method.*

**★ TWO INTERRUPTIONS ARE ON THE SESSION'S RECORD, AND NEITHER FELL INSIDE A COMMITTED ACT.** (1) **A pause** fell
while this report's template was being checked against the files, before it was assembled; the user's *"resume"*
continued the same context, which was not summarized by it, and the session's date moved from 2026-10-21 to 2026-10-23
across it — the forward bound's move, its `--apply` and every 2(c) regeneration ran on 2026-10-21, before the pause.
(2) **The session's context was summarized once**, at Task 2(b): after the five edits that re-aimed `tools/audit/gen_status_batch_bound.py` and before
its `--apply` ran. The Task 0 commit, the member commit with its three checks, and the `STATUS.md` entries of 2(a) were
all made before the summary; the forward bound's `--apply` and `--check`, the 2(c) regenerations, this report, the close
section and the end state were made after it. **What this report states of the work before the summary is taken from
the session's own transcript** — rendered by the scratch script `t2_dedupe.py` (§7), which prints each tool call once
with its input and its result — **and from the scratch files, never from the summary's wording.** The capacity-judgment
file was written before the summary, so its sentence *"This session's context has not been summarized"* was true when
it was written.

## The member done and not done

- **Done:** position **35** — `docs/scoring_model.md`, *the passages of the document* — §6.35 of the reading file, in its
  own commit (§2).
- **The stop:** at the member boundary after position 35, **under this dispatch's 1(g)** — *"Position 35 ALONE: after
  its commit, STOP at that member boundary and go to Task 2, whatever capacity remains"* — and **not** by a capacity
  judgment.
- **Not done:** positions 36 to 57, **UNTOUCHED** — not read for tabulation, not quoted, not counted and not placed
  (**D-672**). §0 of the reading file says so.
- **The next writing resumes at position 36.**
- §7, §8, §9 and §14's relay stay NOT YET WRITTEN; position 57 is not done.

**The capacity judgment, as 1(h) orders it — written to its file in the session's scratch folder, outside the
repository, with the file tools, BEFORE the member's lines were opened at the document, and quoted here whole.** The
transcript shows the write of `capacity_judgment_35.txt` at its call 114; the first act that read any line of the
member at the document — the ranges check, which compares each range's two line texts with the lines at its locators —
is call 130, and the member's lines were first read whole at call 138 (`m35_dump.txt`). Calls 115 and 116 between them
read the four blobs' identities and copied them into scratch files; neither printed a line of the document. The judgment
was *"I can finish this member whole"*, and the member was finished whole; the first-member rule did not fire.

*`capacity_judgment_35.txt`:*

```
Capacity judgment before position 35, written before any line of the member was opened at the document.

Position: 35 — docs/scoring_model.md, "the passages of the document".
At the artifact (tools/audit/l3_outgoing_population.json, read at its entry): lines 480, bytes 45,088, ranges 42,
item_3_hit_lines_inside 93, item_4_identities_inside empty.

Judgment: I can finish this member whole. It has fewer lines than position 21 (495), which a fresh session finished
whole, and about a fifth more bytes; its forty-two ranges hold three whole tables, two quotation-block ranges, one
range opening with a heading line and one former wording, each named by the dispatch, and no fenced block. This
session has done its ordered reads and Task 0, and its context has not been summarized. The member's rows, its updates
to sections 0 and 10 to 13 and the three checks before the commit fit in what remains, with room for the close, the
report and the end state. It is the batch's only member (the dispatch's 1(g)); after it the batch stops and goes to
Task 2.
```

**The next member's size, as 1(h) asks of a stop.** Position 36 is **361 lines and 39,176 bytes** at the artifact, with
82 item-3 hit lines, and its `item_4_identities_inside` is not empty. Position 35, which this session finished whole, is
480 lines and 45,088 bytes there, so position 36 is smaller on both sizes. Its size gives no reason to doubt that a fresh
session can finish it whole. What the next dispatch already names of it — a passage member of a withheld document,
carrying WITHHELD homes in its entry and SEEN homes in its document, whose ranges, nearest headings, homes and cut no
batch has yet read — is a matter of its marks and readings, not of its size.

## 0. The ordered first read

The opening instruction named only this dispatch, so the session's **first tool call was ONE read: the dispatch's first
page** (its lines 1 to 560, the reading tool's first page), to learn the order — the standing fallback the dispatch
names, declared. Nothing else was read in that call. Before any tool call, `CLAUDE.md`, the auto-memory index and a
git status snapshot reached the context at boot as injected context (§6, departure 2). The order, as the transcript's
calls record it (§7, `t2_dedupe.py`, call numbers in brackets):

1. `cowork_blind_derivation_l3_2026_10_17.md`: its heading list by a search [2]; then **§5, §6 and §7** in one read,
   from its line 1269 to the end [3]; then the whole file from line 1 in three reads (1 to 520, 520 to 969, 969 to 1268)
   [4, 5, 6]. **§5 first, then §6, then §7, then whole.**
2. **The derivation's counts, taken AT this read** by two searches made immediately after the whole read and before
   anything else was opened: `^\*\*L3-S\d+\. ` counted **42** [7], and `^- \*\*OQ-L3-\d+` counted **14** [8]. The
   session's message then read *"The counts are 42 statements and 14 open questions, which match the manifest. Next
   I'll read the rest of the dispatch."* They agree with the manifest; no STOP.
3. The remainder of this dispatch, whole (its lines 561 to the end, three reads) [9, 10, 11].
4. **(1)** `CLAUDE.md` injected at boot (declared; not re-read through a tool); `STATUS.md` whole [12]; rule (a)'s
   `gating_ids` at `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` [13, 14, 16];
   `DECISIONS.md` whole (three reads) [15, 17, 18]; `BUILD_AND_TEST.md` — the condition met, this batch runs the guard
   set — located by two searches and read whole [19, 20, 21].
5. **(2)** `cowork_audit_protocol.md`'s dispatch-protocol section, in full (from its line 180, two reads) [22, 23, 24].
6. **(3)** The two L3 rulings whole [25, 26]; the L2 named-documents ruling whole [27]; the comparison-design sitting
   whole [28]; §3am and §3an of the 2026-08-31 decision-surface sitting, located by a search [29, 30].
7. **(4)** The phase definition's §0 and §3.4 [31, 33, 34].
8. **(5)** `FRAMEWORK.md` §5, from `### L0 — The notated record.` through the end of `### The boundary contracts` [32,
   35].
9. **(6)** The brief's §2, §4 and §7 [36, 37, 38].
10. **(7)** `tools/audit/derivation_boot_pack.json` → `subjects` → `l3` → `counted`, `THE_WITHHELD_FAMILY` and `LEAKS`
    (read; not regenerated) [39, 40, 41].
11. **(8)** Entry 437 whole, its existence checked first by a file search [42, 44]; the previous report whole (three
    reads) [43, 45, 46, 47]; the previous dispatch whole (three reads) [48, 49, 50].
12. **(9)** `tools/audit/l3_outgoing_population.json` → the passage rule, the order, `item_2_listed_not_compared_whole`,
    `the_named_documents_derivation` and the members' entries, located by a search [51] and read at its lines 33025 to
    33064 [52], 35060 to 35229 [53] and 34812 to 35061 [55], with a search for position 35's document between [54].
    **The read at 35060 to 35229 took in the end of position 35's entry and position 36's entry with its ranges, where
    only position 36's `lines` and `bytes` were ordered** (§6, departure 3).
13. **(10)** The reading file at the portions the dispatch names, at that time's line numbers: its heading structure
    [56]; the banner and §0 to the paragraph under `## 6.` stating the two reading rules (lines 1 to 373, whole) [57];
    **§6.28 at three portions — 33842 to 34171, 34515 to 34644 and 34840 to 35085 — with searches locating its DIFFERS
    rows** [58 to 63]; **§6.10's manifest header** (14322 to 14441) [64]; **Row 1.15**, located by a search [65, 66];
    **§6.27's manifest header** (33613 to 33721) [67, 68]; **§6.21's manifest header** (27044 to 27373) [69]; **§6.23's
    manifest header** (32100 to 32259) [70]; a search for *blockquote-marker reading* [71]; and **§10 to §16 at
    36318 to 36447, 36630 to 36791, 37792 to 37961 and 38612 to the end**, with searches locating each charter block's
    end and each member block's head [72 to 78]. **Not read as ordered: §6.28 whole (its lines 34172 to 34514 and 34645
    to 34839 were not read), the manifest headers of §6.7, §6.15, §6.16 and §6.19, and §10 to §12 whole** — §6, departure
    4. The member's §10, §11 and §12 entries were written at those sections' ends, and the recheck script compares all
    three sections with the member's rows in both directions (§2).
14. **(11)** Not read — positions 56 and 57 were not reached.
15. **(12)** The outgoing text was opened as Task 1 orders — the member's lines inside its published ranges, read from a
    scratch copy of `docs/scoring_model.md`'s blob at the Task 0 commit (§2).

## 1. Task 0 — the pin, the refs, A1, the last bytes, the commit, the opening capture, the two blobs

**0(a) — the pin.** `git hash-object -w` of this dispatch [84]:

```
warning: in the working copy of 'records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md', LF will be replaced by CRLF the next time Git touches it
40e64cd2f3afed810bc2917ec86f35df5f1dc20e
exit:0
```

then `git cat-file -s` of that blob, `git hash-object -w --no-filters` of entry 437 and of this dispatch [87]:

```
173407
exit:0
d63c5c1befbb8a93532b6313bd366bde383e0e86
exit:0
40e64cd2f3afed810bc2917ec86f35df5f1dc20e
exit:0
```

**0(b) — the refs**, read with the file tools [85, 86]: `.git/refs/heads/master` and `.git/refs/remotes/origin/master`
both named `06b17b46d480bbbd2d7fd0ebe67fe57270d627be`, as the FACT relays. **The chain**, one `git show --stat` per
commit, each hash written literally in its own command and redirected to its own scratch file [88], the eleven files then
read with the file tools [89 to 99]:

```
commit 06b17b46d480bbbd2d7fd0ebe67fe57270d627be
parent 75bbfa9326db01819b7036f660b71bc1c388365b
subject End state: the L3 comparison continued from position 27 - guard run at the close tree, the A2 regenerations already met inside the close


 records/cowork/handoff/cowork_away_returns.md | 71 +++++++++++++++++++++++++++
 tools/audit/guard_state.json                  | 12 ++---
 2 files changed, 77 insertions(+), 6 deletions(-)
commit 75bbfa9326db01819b7036f660b71bc1c388365b
parent f85ed74066f8e73682a9d853013be68978de95be
subject Close: the L3 comparison continued from position 27, under its dispatch


 STATUS.md                                          |    6 +-
 STATUS_ARCHIVE.md                                  |    8 +
 ..._l3_comparison_tabulation_twelfth_2026_10_20.md | 2490 ++++++++++++++++++++
 records/cowork/handoff/cowork_away_returns.md      |   82 +
 tools/audit/defense_share.json                     |    2 +-
 tools/audit/gen_status_batch_bound.py              |   54 +-
 tools/audit/session_start_read_size.json           |   16 +-
 tools/audit/status_batch_bound.json                |   32 +-
 8 files changed, 2661 insertions(+), 29 deletions(-)
commit f85ed74066f8e73682a9d853013be68978de95be
parent c305fc0273ce4aa3cebc18e7fcdfe649482e5a5a
subject comparison L3: member 34 tabulated - 0 outgoing statements placed, proposals only


 .../cowork_comparison_l3_reading.md                | 142 +++++++++++++++++++--
 1 file changed, 131 insertions(+), 11 deletions(-)
commit c305fc0273ce4aa3cebc18e7fcdfe649482e5a5a
parent b836986f940e8a07053a5662b16ace2e97fb69e4
subject comparison L3: member 33 tabulated - 0 outgoing statements placed, proposals only


 .../cowork_comparison_l3_reading.md                | 147 +++++++++++++++++++--
 1 file changed, 138 insertions(+), 9 deletions(-)
commit b836986f940e8a07053a5662b16ace2e97fb69e4
parent 8f025665927fa312f84554eb1dec647967890f4d
subject comparison L3: member 32 tabulated - 1 outgoing statements placed, proposals only


 .../cowork_comparison_l3_reading.md                | 170 +++++++++++++++++++--
 1 file changed, 156 insertions(+), 14 deletions(-)
commit 8f025665927fa312f84554eb1dec647967890f4d
parent 917d2f6c5fe35dfc7fa02a1a45697eed81783c59
subject comparison L3: member 31 tabulated - 20 outgoing statements placed, proposals only


 .../cowork_comparison_l3_reading.md                | 463 ++++++++++++++++++++-
 1 file changed, 450 insertions(+), 13 deletions(-)
commit 917d2f6c5fe35dfc7fa02a1a45697eed81783c59
parent 777e6d5ebb0c68998e2df868dddc516d15e9aa87
subject comparison L3: member 30 tabulated - 8 outgoing statements placed, proposals only


 .../cowork_comparison_l3_reading.md                | 295 ++++++++++++++++++++-
 1 file changed, 281 insertions(+), 14 deletions(-)
commit 777e6d5ebb0c68998e2df868dddc516d15e9aa87
parent f9ba0d9c93c0b3d2f2760267c97911495ea8c625
subject comparison L3: member 29 tabulated - 7 outgoing statements placed, proposals only


 .../cowork_comparison_l3_reading.md                | 251 ++++++++++++++++++++-
 1 file changed, 239 insertions(+), 12 deletions(-)
commit f9ba0d9c93c0b3d2f2760267c97911495ea8c625
parent 800fe2662a374f4206c14612a0f2a86c09adf801
subject comparison L3: member 28 tabulated - 72 outgoing statements placed, proposals only


 .../cowork_comparison_l3_reading.md                | 1389 +++++++++++++++++++-
 1 file changed, 1376 insertions(+), 13 deletions(-)
commit 800fe2662a374f4206c14612a0f2a86c09adf801
parent 532971b19d1bc0cae2471c75d1785763811a665c
subject comparison L3: member 27 tabulated - 4 outgoing statements placed, proposals only


 .../cowork_comparison_l3_reading.md                | 274 ++++++++++++++++++++-
 1 file changed, 261 insertions(+), 13 deletions(-)
commit 532971b19d1bc0cae2471c75d1785763811a665c
parent 95bdd1357f75ab3cb09530a7a5ba2ad0379c819d
subject record: entry 436 and the twelfth l3 comparison tabulation dispatch


 ..._l3_comparison_tabulation_twelfth_2026_10_20.md | 1522 ++++++++++++++++++++
 ...rk_handoff_entry_four_hundred_and_thirty_six.md |  105 ++
 2 files changed, 1627 insertions(+)
```

The chain agrees with the FACT: `06b17b46…` (the previous batch's end state) ← `75bbfa93…` (its close) ← its eight
member commits ← its Task 0 commit `532971b1…` ← `95bdd135…`.

**0(c) — A1's check.** `python tools/audit/changed_paths.py` into a scratch file (exit 0) [100], searched there with the
file tools [101]:

```
1: M	tools/audit/claude_md_finer_archive.json
2:??	Claude outputs/
3:??	Codex research inventory/
4:??	docs/research_papers/polyph9-release/
5:??	external resarch summary/Computational Music Theory and Its.pdf
6:??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
7:??	records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md
8:??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_seven.md
396:??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
397:396 changed path record(s) [worktree]
```

Per named untracked path, and per tracked input this batch edits by `git diff --stat` against `06b17b46…` written
literally [102]:

```
records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md
exit:0
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_seven.md
exit:0
== STATUS.md
exit:0
== STATUS_ARCHIVE.md
exit:0
== tools/audit/gen_status_batch_bound.py
exit:0
== tools/audit/status_batch_bound.json
exit:0
== ratification_surfaces/cowork_comparison_l3_reading.md
exit:0
== records/cowork/handoff/cowork_away_returns.md
exit:0
```

**A1 HOLDS BY CONTENT:** one tracked modification, `tools/audit/claude_md_finer_archive.json`, carried; the two untracked
paths Task 0 lands; the standing untracked population as declared, every other line under `scratch_artifacts/`; every
per-path diff empty. No further handoff entry or ruling record appeared during the run.

**0(d) — the last bytes**, by `t0_lastbytes.py` with this batch's two paths and blobs [104]:

```
== records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md
   blob 40e64cd2f3afed810bc2917ec86f35df5f1dc20e  size 173407
   zero bytes: 0
   ends with a newline: True
   last non-empty line: and is recorded at the end of this file"* and is true as it stands. Nothing else was found to correct.
   last 70 bytes: b's file"* and is true as it stands. Nothing else was found to correct.\n'
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_seven.md
   blob d63c5c1befbb8a93532b6313bd366bde383e0e86  size 8608
   zero bytes: 0
   ends with a newline: True
   last non-empty line: instruction; "continue"; "continue".*
   last 70 bytes: b'. The user\'s words: the opening\ninstruction; "continue"; "continue".*\n'
exit:0
```

Both files whole, no zero byte; **entry 437 is 8,608 bytes**.

**0(e) — the commit.** The pin re-proved immediately before staging, the two paths staged by explicit path, the staged
set proved [105]:

```
40e64cd2f3afed810bc2917ec86f35df5f1dc20e
exit:0
warning: in the working copy of 'records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_seven.md', LF will be replaced by CRLF the next time Git touches it
exit:0
A	records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_seven.md
2 changed path record(s) [staged]
exit:0
```

The commit, then its identity by a branch-tip read (§6, departure 7) [106]:

```
exit:0
d1b3a26f577c8034b56ac909de3946564cffe243 06b17b46d480bbbd2d7fd0ebe67fe57270d627be record: entry 437 and the thirteenth l3 comparison tabulation dispatch
exit:0
```

Verified at the commit's own object and pushed [107]:

```
d1b3a26f577c8034b56ac909de3946564cffe243 06b17b46d480bbbd2d7fd0ebe67fe57270d627be
record: entry 437 and the thirteenth l3 comparison tabulation dispatch

 ..._comparison_tabulation_thirteenth_2026_10_21.md | 1685 ++++++++++++++++++++
 ..._handoff_entry_four_hundred_and_thirty_seven.md |   98 ++
 2 files changed, 1783 insertions(+)
exit:0
40e64cd2f3afed810bc2917ec86f35df5f1dc20e
d63c5c1befbb8a93532b6313bd366bde383e0e86
exit:0
To https://github.com/slimvince/MuseScore
   06b17b46d4..d1b3a26f57  master -> master
exit:0
```

The push line: **`06b17b46d4..d1b3a26f57  master -> master`**. `.git/refs/remotes/origin/master`, read with the file
tools [108], named `d1b3a26f577c8034b56ac909de3946564cffe243`.

**0(f) — the opening guard capture**, `python tools/audit/gen_guard_state.py --check` (the read-only operating mode,
named) into a scratch file, exit 0 [109], whole:

```
the guard state re-derives
  [PASS] tools/audit/register_lint.py 
  [PASS] tools/audit/index_status_lint.py --check
  [PASS] tools/audit/gen_arm_comment_sweep.py --check
  [PASS] tools/audit/local_patches_check.py 
  [PASS] tools/audit/local_patches_check.py --establish --check
  [PASS] tools/audit/guard_armed_check.py 
  [PASS] tools/audit/process_check.py --establish --check
  [PASS] tools/audit/shell_read_guard.py --establish --check
  [PASS] tools/audit/output_encoding.py --establish --check
  [PASS] tools/audit/changed_paths.py --establish
  [PASS] tools/audit/claude_md_rule_triage.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --check
  [PASS] tools/audit/corpus_arm_stamp.py --establish --check
  [PASS] tools/audit/instrument_arm_declaration_effect.py --check
  [FAIL] tools/audit/gen_phase3_gate_partition.py --check
  [PASS] tools/audit/gen_nongating_apparatus_rows.py --check
  [PASS] tools/audit/gen_discard_records.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach.py --check
  [PASS] tools/audit/decisions/gen_true_half_reach_rows.py --check
  [PASS] tools/audit/gen_gating_row_sizing.py --check
  [FAIL] tools/audit/gen_filing_convention_application.py --check
  [PASS] tools/audit/decisions/gen_phase1q_snapshot_establishment.py --check
  [PASS] tools/audit/gen_period_stratum_split.py --check
  [PASS] tools/audit/gen_july_screen.py --check
  [PASS] tools/audit/gen_specification_document_set.py --check
  [PASS] tools/audit/gen_l0_l1_outgoing_population.py --check
  [PASS] tools/audit/gen_withheld_family_reading.py --subject l2 --check
  [PASS] tools/audit/gen_withheld_family_reading.py --subject l3 --check
  [FAIL] tools/audit/gen_artifact_inventory.py --check
  [FAIL] tools/audit/gen_artifact_inventory_surface.py --check
  [PASS] tools/audit/gen_status_archive_pass.py --check
  [PASS] tools/audit/gen_doc_change_candidates.py --check
  [FAIL] tools/audit/gen_test_construction_evidence.py --check
  [PASS] tools/audit/gen_decisions_filter.py --check
  [FAIL] tools/audit/gen_retirement_caller_check.py --check
  [PASS] tools/audit/gen_deciding_act_recovery.py --check
  [PASS] tools/audit/gen_rulings_sort.py --check
  [PASS] tools/audit/gen_sole_carrier_subclass.py --check
  [PASS] tools/audit/gen_ratified_document_check.py --check
  [FAIL] tools/audit/decisions/apply_soft_discard.py --check
  [FAIL] tools/audit/decisions/apply_residue_discard.py --check
  [PASS] tools/audit/gen_framework_untrusted_candidates.py --check
  [PASS] tools/audit/gen_phase1_gate_readers.py --check
  [PASS] tools/audit/gen_discard_reach_split.py --check
  [PASS] tools/audit/decisions/gen_retired_subject_moves.py --check
  [PASS] tools/audit/gen_census_movement_classification.py --check
  [PASS] tools/audit/gen_governing_surface_spans.py --check
  [PASS] tools/audit/gen_governing_surface_readers.py --check
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair CLAUDE.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair OPEN_ITEMS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair DECISIONS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair STATUS.md
  [PASS] tools/audit/gen_governing_surface_split.py --check --pair BUILD_AND_TEST.md
  [PASS] tools/audit/gen_status_batch_bound.py --check
  [PASS] tools/audit/gen_status_residue_move.py --check
  [PASS] tools/audit/gen_retirement_census_movement.py --check
  [PASS] tools/audit/gen_claude_md_finer_spans.py --check
  [PASS] tools/audit/gen_claude_md_finer_surface.py --check
  [PASS] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [PASS] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --subject l3 --check
  [PASS] tools/audit/gen_l3_outgoing_population.py --check
  [PASS] tools/audit/decisions/gen_decisions_register.py --check
  [FAIL] tools/audit/decisions/gen_cluster_dispositions.py --verify
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --producible
  [FAIL] tools/audit/decisions/gen_home_classification.py --check
  [FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
  [PASS] tools/audit/decisions/gen_reads5_repack.py --check
  [PASS] tools/audit/decisions/gen_decision_clusters.py --check
  [PASS] tools/audit/decisions/gen_phase1w_legacy_verification.py --check
  [PASS] tools/audit/decisions/reaim_home_anchors.py --check
  [PASS] tools/audit/decisions/gen_live_prohibition_pointers.py --check
  [PASS] tools/audit/gen_claude_md_growth.py --check
  [PASS] tools/audit/prune_at_amendment_lint.py --check
  [PASS] tools/open_items_split_check.py 
  [PASS] tools/notation_seams/gen_callpath_facts.py --check
  [NOT RUN] tools/audit/gen_ratification_surface_set.py
  [NOT RUN] tools/audit/reaim_ratification_surface_paths.py
  [NOT RUN] tools/audit/decisions/gen_verbatim_subject_consistency.py
  [NOT RUN] tools/audit/gen_reserved_word_scanner.py
  [HISTORICAL] tools/audit/gen_phase1_completion_inventory.py
  [HISTORICAL] tools/audit/gen_phase1_finish_line.py
  [HISTORICAL] tools/audit/decisions/gen_outstanding_delegations.py
  [HISTORICAL] tools/audit/gen_claude_md_finer_archive.py
  [HISTORICAL] tools/audit/gen_post_split_archive.py
  [HISTORICAL] tools/audit/gen_l2_outgoing_population.py
  [HISTORICAL] tools/audit/decisions/gen_phase1n_reading_regime.py
  [HISTORICAL] tools/audit/decisions/gen_reads5_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads6_yield.py
  [HISTORICAL] tools/audit/decisions/gen_phase1m_measurements.py
  [HISTORICAL] tools/audit/decisions/gen_phase1g_triage.py
  [HISTORICAL] tools/audit/decisions/gen_reads1_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads2_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads3_yield.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_yield.py
  [HISTORICAL] tools/audit/decisions/gen_finish_line_item1_routes.py
  [HISTORICAL] tools/audit/decisions/gen_item1_rehome_blocker.py
  [HISTORICAL] tools/audit/decisions/gen_r1_superseded_reach.py
  [HISTORICAL] tools/audit/decisions/gen_reads4_oi326_application.py
  [HISTORICAL] tools/audit/gen_claude_md_prune_backlog.py
82 guard(s) run, 13 failing, 4 not run, 20 historical record(s)
```

**A2 HOLDS:** the header *"the guard state re-derives"* — the header the previous ten batches met; run 82; **exactly the
thirteen FAIL** (`gen_phase3_gate_partition.py`, `gen_filing_convention_application.py`, `gen_artifact_inventory.py`,
`gen_artifact_inventory_surface.py`, `gen_test_construction_evidence.py`, `gen_retirement_caller_check.py`,
`apply_soft_discard.py`, `apply_residue_discard.py`, `gen_epoch_write_path.py`, `gen_recognizer_establishment_sort.py`,
`gen_cluster_dispositions.py --verify`, `gen_home_classification.py`, `gen_phase1p_delegation_bar.py`); four NOT RUN,
twenty HISTORICAL; `gen_evidence_pin_membership.py --check` PASS; zero STOPs. The object's own summary, read from a
scratch copy of `06b17b46…:tools/audit/guard_state.json` [111, 113]:

```
1616:    "run": 82,
1617:    "passing": 69,
1618:    "failing": 13,
1699:    "not_run": 4,
1700:    "historical_records": 20
```

and `python tools/audit/gen_guard_classification.py --check` (exit 2 [111]), its output read from its scratch file
[112]:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_withheld_family_reading.py']
```

The STOP names exactly the four tools of the FACT.

**0(g) — the two blobs**, `git hash-object` of the derivation and the brief, then `git cat-file -s` of the two named
blobs — call 111's whole output:

```
exit:0
exit:2
c01793f98c51e0267fb0dc7487613ac477cc1fbb
6abb53333fd248ee15a983c6ece4cbfe38a376a0
exit:0
127533
39251
exit:0
```

(The call's first two lines are the copy of the guard artifact, exit 0, and the classification check, exit 2.) Both
blobs equal the FACT's, and their sizes, 127,533 and 39,251 bytes.

**E0 — MET**: the two named paths in one commit; `origin/master` at the commit; the pin proved before staging; A1
reported with its enumeration; the opening capture against A2; the two blobs verified.

## 2. Task 1 — the tabulation, position 35

**The objects the member was read from**, taken at the Task 0 commit by explicit hash (`git rev-parse
d1b3a26f577c8034b56ac909de3946564cffe243:<path>` for `docs/scoring_model.md`, the reading file, the population artifact
and the decisions register's data file, in that order), then `git hash-object` of the working `docs/scoring_model.md` and
reading file [115]:

```
8410b00ef422769533abb967852357d0f17f86e6
d1f5140019f7d68613cac037acb598c4ce913661
13d1750be95ecdcf408405ff7d6f67bba8db1dfe
9f34b0cab42c2fc69d3af8613ac3e0a9237d6b03
exit:0
8410b00ef422769533abb967852357d0f17f86e6
d1f5140019f7d68613cac037acb598c4ce913661
exit:0
```

The working `docs/scoring_model.md` and reading file are those blobs. The four blobs were copied into scratch files by
`git cat-file blob` (exit 0 each) [116], and the previous batch's scripts were repointed at those copies (§7).

**How the scripts took the member's text (1(g)).** The member's text is the lines inside its forty-two published ranges,
read from the scratch copy of `docs/scoring_model.md`'s blob `8410b00e…` at the Task 0 commit, joined as the scripts
join them, with the `> ` mask at line starts left in place — **and the mask acted on thirty-two lines**, *"marker lines
masked: 32"* below: **the twelve lines of range 2 and the twenty lines of range 3**, every one of which opens with the
quotation-block marker or is that marker alone, as the ranges check counts them per range. **The member text is also
taken a second way, with the one hyphen at a line end joined to the next line**, and a quotation is accepted if it is
found in either form: the join is at line 862, inside the compound *guaranteed-inversion-alternative*, quoted at Row
35.95. **Every quotation of an outgoing statement was found in those lines** (*"quotations not found verbatim: 0"*), so
no quotation needed the fallback of a sentence checked against the document's text beyond a range.

### The commit

| Member | Commit | Subject | Push line | Reading file's blob at the commit |
|---|---|---|---|---|
| 35 | `5d9f356a0e5f7d11ae5e63a270d7be1537aaac37` | `comparison L3: member 35 tabulated - 197 outgoing statements placed, proposals only` | `d1b3a26f57..5d9f356a0e  master -> master` | `fff5cd075c4c218eb1e86a4e567f25b83eec67c5` |

The edited reading file written as a blob before the checks ran [215]:

```
warning: in the working copy of 'ratification_surfaces/cowork_comparison_l3_reading.md', LF will be replaced by CRLF the next time Git touches it
fff5cd075c4c218eb1e86a4e567f25b83eec67c5
exit:0
```

the three checks run on that blob's scratch copy [216]:

```
exit:0
done 35 1 42 ranges
exit:0
```

then the blob re-proved, the reading file staged by explicit path and the staged set proved [221]:

```
fff5cd075c4c218eb1e86a4e567f25b83eec67c5
exit:0
warning: in the working copy of 'ratification_surfaces/cowork_comparison_l3_reading.md', LF will be replaced by CRLF the next time Git touches it
exit:0
M	ratification_surfaces/cowork_comparison_l3_reading.md
1 changed path record(s) [staged]
exit:0
```

the commit and its identity by a branch-tip read [222]:

```
exit:0
5d9f356a0e5f7d11ae5e63a270d7be1537aaac37 d1b3a26f577c8034b56ac909de3946564cffe243 comparison L3: member 35 tabulated - 197 outgoing statements placed, proposals only
exit:0
```

verified at its own object, its reading-file blob read, and pushed [223]:

```
5d9f356a0e5f7d11ae5e63a270d7be1537aaac37 d1b3a26f577c8034b56ac909de3946564cffe243
comparison L3: member 35 tabulated - 197 outgoing statements placed, proposals only

 .../cowork_comparison_l3_reading.md                | 3563 +++++++++++++++++++-
 1 file changed, 3548 insertions(+), 15 deletions(-)
exit:0
fff5cd075c4c218eb1e86a4e567f25b83eec67c5
exit:0
To https://github.com/slimvince/MuseScore
   d1b3a26f57..5d9f356a0e  master -> master
exit:0
```

`.git/refs/remotes/origin/master`, read with the file tools after the push [224], named
`5d9f356a0e5f7d11ae5e63a270d7be1537aaac37`. The member commit also carried the one banner edit and the §0 clause on the
previous batch's stop.

**How the member's text reached the reading file.** The manifest header, the 174 rows, the *not a statement* list and the
foot were generated by scratch scripts (`gen35_lib.py`, `gen35_rows_a.py`, `gen35_rows_b.py`, `gen35.py`, `gen35_head.py`)
from the row specifications, each quotation taken by the script from the blob's own lines at its locator; `splice35.py`
inserted the new subsection before §7 and the member's §11 block before §12 in a scratch copy of the reading file's
member-34 blob; the member and word checks ran on that scratch copy first (outputs `m35_member0.txt` and
`m35_words0.txt`); the copy was put into the repository with `cp` [201] (§6, departure 5); and the banner, §0, §10, §12
and §13 edits were then made with the file tools' Edit [203 to 214]. The three checks above ran on the result.

**What the checks and the generator found and corrected before the commit, each corrected at the row specifications or
the generator and the checks run again:** two quotations whose start or end the generator did not find at the
locator — Row 35.98's sentence starts on line 870, so its locator became lines 870–871, and Row 35.165's end string
lies inside a code span, so it became the span's end; three wrapping faults of the generator — a code span broken
across a line, the charter name broken across a line in the manifest, and **the charter name separated from
*RELOCATED — to*, which made the member check stop with an IndexError at its first run** (call 195, exit 1, output
`m35_member0.txt` before the fix); Row 35.137's AGREES remark, which overstated L3-S38 and was corrected to *the
committed chord is left alone and not revised*; and a §10 parenthetical naming Rows 35.121 to 35.144 as lying in homes,
corrected to *"Eight of them — all but Rows 35.8 and 35.30 — lie in homes…"*.

### Position 35 — `docs/scoring_model.md`, the passages of the document

Forty-two ranges over the whole document — its section is the document itself, lines 1 to 1755, the label naming no
heading — three of them tables (ranges 17, 19 and 25), two of them quotation-block paragraphs (ranges 2 and 3), one
opening with a heading line (range 29, *7. Inversion correction*) and one holding a preserved former wording (range
28); **no fenced block inside a range**. **No other member of the artifact is cut from this document**, so nothing is
excluded from the cut. **One hundred and seventy-four rows carrying one hundred and ninety-seven statements**: eighteen
RELOCATED (seventeen to *L2 — The tonal reading. The one entangled decision.* and one, Row 35.151, to *the measurement
of the analysis*), one hundred and fifty-three QUARANTINED and twenty-six HISTORICAL; **three AGREES** (Rows 35.90 (ii)
and 35.126 with L3-S4, Row 35.137 (i) with L3-S38), **one DIFFERS** (Row 35.154, from L3-S38, its one-sentence difference
in both texts' words at §12, nothing chosen) and one hundred and ninety-three THE DERIVATION IS SILENT. Sixty-four items
are listed under *not a statement*, the three table header rows among them, each quoted at its opening. **Thirteen homes
of the decisions register's data file lie inside the ranges**, twelve in its `decisions` list and one RETIRED entry,
D-216, each named at its rows with its INDEX status relayed as a fact and carrying no mark; **thirty homes lie in the
cut**, each named at the manifest header. **No WITHHELD home** (the artifact's `item_4_identities_inside` is empty) **and
no SEEN home** (D-510, a SEEN identity, is homed in the cut). The manifest header states **eight placements for
challenge, (a) to (h)**, each with its alternative where one was weighed, and **one departure from the former-wording
precedent at one sentence** (Row 35.119), stated for challenge with its alternative.

**The ranges check:**

*`m35_ranges.txt`:*

```
document: docs/scoring_model.md | lines in the split: 1756 | ends with a newline: True
kind: items 3 and 4 — passages of a specification-set member | label: the passages of the document | lines 480 | bytes 45088 | hits 93 | item-4 []
range 1 28-31 first matches: True  last matches: True  marker lines: 0  of 4
range 2 33-44 first matches: True  last matches: True  marker lines: 12  of 12
range 3 74-93 first matches: True  last matches: True  marker lines: 20  of 20
range 4 101-128 first matches: True  last matches: True  marker lines: 0  of 28
range 5 135-151 first matches: True  last matches: True  marker lines: 0  of 17
range 6 398-403 first matches: True  last matches: True  marker lines: 0  of 6
range 7 416-431 first matches: True  last matches: True  marker lines: 0  of 16
range 8 440-454 first matches: True  last matches: True  marker lines: 0  of 15
range 9 456-476 first matches: True  last matches: True  marker lines: 0  of 21
range 10 478-490 first matches: True  last matches: True  marker lines: 0  of 13
range 11 503-509 first matches: True  last matches: True  marker lines: 0  of 7
range 12 511-517 first matches: True  last matches: True  marker lines: 0  of 7
range 13 544-547 first matches: True  last matches: True  marker lines: 0  of 4
range 14 549-559 first matches: True  last matches: True  marker lines: 0  of 11
range 15 594-600 first matches: True  last matches: True  marker lines: 0  of 7
range 16 624-627 first matches: True  last matches: True  marker lines: 0  of 4
range 17 717-738 first matches: True  last matches: True  marker lines: 0  of 22
range 18 740-754 first matches: True  last matches: True  marker lines: 0  of 15
range 19 773-786 first matches: True  last matches: True  marker lines: 0  of 14
range 20 823-829 first matches: True  last matches: True  marker lines: 0  of 7
range 21 831-841 first matches: True  last matches: True  marker lines: 0  of 11
range 22 862-865 first matches: True  last matches: True  marker lines: 0  of 4
range 23 867-872 first matches: True  last matches: True  marker lines: 0  of 6
range 24 891-898 first matches: True  last matches: True  marker lines: 0  of 8
range 25 977-986 first matches: True  last matches: True  marker lines: 0  of 10
range 26 995-1002 first matches: True  last matches: True  marker lines: 0  of 8
range 27 1033-1046 first matches: True  last matches: True  marker lines: 0  of 14
range 28 1048-1063 first matches: True  last matches: True  marker lines: 0  of 16
range 29 1085-1089 first matches: True  last matches: True  marker lines: 0  of 5
range 30 1137-1139 first matches: True  last matches: True  marker lines: 0  of 3
range 31 1141-1144 first matches: True  last matches: True  marker lines: 0  of 4
range 32 1177-1178 first matches: True  last matches: True  marker lines: 0  of 2
range 33 1276-1312 first matches: True  last matches: True  marker lines: 0  of 37
range 34 1413-1439 first matches: True  last matches: True  marker lines: 0  of 27
range 35 1466-1473 first matches: True  last matches: True  marker lines: 0  of 8
range 36 1526-1530 first matches: True  last matches: True  marker lines: 0  of 5
range 37 1552-1556 first matches: True  last matches: True  marker lines: 0  of 5
range 38 1582-1583 first matches: True  last matches: True  marker lines: 0  of 2
range 39 1602-1611 first matches: True  last matches: True  marker lines: 0  of 10
range 40 1616-1630 first matches: True  last matches: True  marker lines: 0  of 15
range 41 1691-1709 first matches: True  last matches: True  marker lines: 0  of 19
range 42 1713-1723 first matches: True  last matches: True  marker lines: 0  of 11
ranges: 42  all 2x42 boundary texts match: True
lines in ranges: 480  bytes (each line with its newline): 45088
section: the whole document, lines 1 to 1755 (its last line '`analyzeChord()`.*')
lines of the section outside every range: 1275 (241 blank, 1034 not blank)
cut spans: 1-27 32 45-73 94-100 129-134 152-397 404-415 432-439 455 477 491-502 510 518-543 548 560-593 601-623 628-716 739 755-772 787-822 830 842-861 866 873-890 899-976 987-994 1003-1032 1047 1064-1084 1090-1136 1140 1145-1176 1179-1275 1313-1412 1440-1465 1474-1525 1531-1551 1557-1581 1584-1601 1612-1615 1631-1690 1710-1712 1724-1755
headings in the cut:
  1: # Chord Analyzer Scoring Model
  72: ## 1. Overview
  133: ### Scoring constants are readable from an optional override file (Stage-5 fitter)
  155: ## 2. Templates
  205: ## 3. Score matrix structure
  263: ### Floating-point tie policy
  297: ## 4. Bonus and penalty terms
  299: ### `dim7CharacteristicBonus` — `kDim7CharacteristicBonus = 0.75`
  387: ### `rootContinuityBonus` — `prefs.rootContinuityBonus = 0.40`
  405: ### Gate R — rcb bass-chord-tone guard
  533: ### `w_complete` — `kWComplete = 0.50`
  561: ### `w_stepIn` / `w_stepOut` — `kWStepIn` per-carrier (Baroque/Default **0.125**, Jazz/others 0.10); `kWStepOut = 0.10`
  610: ### `w_seq` — `kWSeq = 0.20`
  629: ### `w_dim` — `kWDim = 0.15`
  658: ### B2 aug7 guard
  674: ### `ScoringPhase` (ChordAnalyzerPreferences::scoringPhase)
  715: ### Other terms (briefly)
  756: ### The registered scoring constants this document does not table above
  795: ## 5. Joint (bass, root, template) scoring
  860: ## 6. Post-scoring gates (A–L)
  905: ### §6a. The unified promotion primitive `promoteToWinner()`
  1100: ### Pre-sort capture: `originalWinnerRootPc`
  1129: ## 8. Known constraints and dead ends
  1267: ### The fine-grain function override — falsified, its repair refuted, its principled restriction un-computable, and a redesign recommended but NOT adopted
  1314: ### Bass-as-root promotion — SHELVED WITH EVIDENCE, and the cascade the attempt exposed
  1348: ### The quality-overwrite information loss is TOLERATED until the gate-dissolution step — tolerated is not forgotten
  1367: ### Four measured dead ends of the segmentation-and-root path — do not retry any of them
  1401: ### Four archive-only dead ends of the chord-scoring path — do not retry any of them
  1441: ### The validation basis of every hand-set scoring magnitude on this surface is retroactively VOID
  1459: ## 9. How to add a new template safely (checklist)
  1540: ## 10. Harmonic function layer
  1597: ## 11. Scoring oracle vs competition pipeline (E2d redesign)
headings inside the ranges:
  1085: ## 7. Inversion correction
```

**The inside control and the homes walk:**

*`m35_inside.txt`:*

```
member 35 document: docs/scoring_model.md
members of the artifact with that document: [35]
docs/scoring_model.md members other than 35: 0; their ranges overlapping 1 1755: 0
```

*`m35_homes.txt`:*

```
D-215 | docs/scoring_model.md:1137 | live | /decisions | range [(1137, 1139)] | wholly inside a range: True
D-221 | docs/scoring_model.md:1177-1178 | live | /decisions | range [(1177, 1178)] | wholly inside a range: True
D-299 | docs/scoring_model.md:1413-1417 | live | /decisions | range [(1413, 1439)] | wholly inside a range: True
D-300 | docs/scoring_model.md:1418-1424 | deferred | /decisions | range [(1413, 1439)] | wholly inside a range: True
D-301 | docs/scoring_model.md:1425-1430 | deferred | /decisions | range [(1413, 1439)] | wholly inside a range: True
D-302 | docs/scoring_model.md:1431-1439 | live | /decisions | range [(1413, 1439)] | wholly inside a range: True
D-327 | docs/scoring_model.md:478-490 | live | /decisions | range [(478, 490)] | wholly inside a range: True
D-490 | docs/scoring_model.md:1276-1284 | live | /decisions | range [(1276, 1312)] | wholly inside a range: True
D-491 | docs/scoring_model.md:1285-1292 | live | /decisions | range [(1276, 1312)] | wholly inside a range: True
D-492 | docs/scoring_model.md:1302-1312 | live | /decisions | range [(1276, 1312)] | wholly inside a range: True
D-493 | docs/scoring_model.md:1293-1301 | live | /decisions | range [(1276, 1312)] | wholly inside a range: True
D-537 | docs/scoring_model.md:549-559 | live | /decisions | range [(549, 559)] | wholly inside a range: True
D-216 | docs/scoring_model.md:1141 | live | /retired_entries/entries/the_entry | range [(1141, 1144)] | wholly inside a range: True
homes naming docs/scoring_model.md with a line number: 43
identities overlapping the 42 ranges given: 13
```

*`m35_homes_cut.txt`:*

```
D-220 | docs/scoring_model.md:1169-1170 | live | /decisions | range [(1145, 1176)] | wholly inside a range: True
D-222 | docs/scoring_model.md:1180-1182 | live | /decisions | range [(1179, 1275)] | wholly inside a range: True
D-223 | docs/scoring_model.md:1184-1186 | live | /decisions | range [(1179, 1275)] | wholly inside a range: True
D-224 | docs/scoring_model.md:1188-1191 | live | /decisions | range [(1179, 1275)] | wholly inside a range: True
D-317 | docs/scoring_model.md:1375-1381 | live | /decisions | range [(1313, 1412)] | wholly inside a range: True
D-318 | docs/scoring_model.md:1382-1385 | live | /decisions | range [(1313, 1412)] | wholly inside a range: True
D-319 | docs/scoring_model.md:1386-1392 | live | /decisions | range [(1313, 1412)] | wholly inside a range: True
D-320 | docs/scoring_model.md:1393-1399 | live | /decisions | range [(1313, 1412)] | wholly inside a range: True
D-321 | docs/scoring_model.md:265-278 | live | /decisions | range [(152, 397)] | wholly inside a range: True
D-322 | docs/scoring_model.md:286-291 | live | /decisions | range [(152, 397)] | wholly inside a range: True
D-323 | docs/scoring_model.md:356-360 | live | /decisions | range [(152, 397)] | wholly inside a range: True
D-324 | docs/scoring_model.md:1026-1027 | live | /decisions | range [(1003, 1032)] | wholly inside a range: True
D-325 | docs/scoring_model.md:1198-1205 | live | /decisions | range [(1179, 1275)] | wholly inside a range: True
D-328 | docs/scoring_model.md:1207-1216 | live | /decisions | range [(1179, 1275)] | wholly inside a range: True
D-423 | docs/scoring_model.md:1218-1225 | live | /decisions | range [(1179, 1275)] | wholly inside a range: True
D-463 | docs/scoring_model.md:1227-1235 | live | /decisions | range [(1179, 1275)] | wholly inside a range: True
D-465 | docs/scoring_model.md:1238-1250 | live | /decisions | range [(1179, 1275)] | wholly inside a range: True
D-510 | docs/scoring_model.md:936-946 | live | /decisions | range [(899, 976)] | wholly inside a range: True
D-511 | docs/scoring_model.md:947-953 | live | /decisions | range [(899, 976)] | wholly inside a range: True
D-512 | docs/scoring_model.md:954-965 | live | /decisions | range [(899, 976)] | wholly inside a range: True
D-536 | docs/scoring_model.md:843-856 | live | /decisions | range [(842, 861)] | wholly inside a range: True
D-580 | docs/scoring_model.md:1252-1265 | deferred | /decisions | range [(1179, 1275)] | wholly inside a range: True
D-600 | docs/scoring_model.md:1355-1365 | live | /decisions | range [(1313, 1412)] | wholly inside a range: True
D-214 | docs/scoring_model.md:1134 | live | /retired_entries/entries/the_entry | range [(1090, 1136)] | wholly inside a range: True
D-217 | docs/scoring_model.md:1147 | live | /retired_entries/entries/the_entry | range [(1145, 1176)] | wholly inside a range: True
D-218 | docs/scoring_model.md:1154 | live | /retired_entries/entries/the_entry | range [(1145, 1176)] | wholly inside a range: True
D-219 | docs/scoring_model.md:1162 | live | /retired_entries/entries/the_entry | range [(1145, 1176)] | wholly inside a range: True
D-594 | docs/scoring_model.md:1321-1335 | shelved-with-evidence | /retired_entries/entries/the_entry | range [(1313, 1412)] | wholly inside a range: True
D-595 | docs/scoring_model.md:1336-1346 | live | /retired_entries/entries/the_entry | range [(1313, 1412)] | wholly inside a range: True
D-615 | docs/scoring_model.md:1447-1455 | live | /retired_entries/entries/the_entry | range [(1440, 1465)] | wholly inside a range: True
homes naming docs/scoring_model.md with a line number: 43
identities overlapping the 43 ranges given: 30
```

**The three checks** on the committed blob:

*`m35_member1.txt`:*

```
   join at a line ending: 's populated and the optional guaranteed-'
member lines taken: 480  marker lines masked: 32
hyphen-at-line-end joins in the member: 1
rows parsed: 174  contiguous 1..n: True
rows: 174  statements (claims): 197  claims-per-row histogram: {1: 152, 2: 21, 3: 1}
ADOPTED — carried 0: 
ADOPTED — proposed 0: 
RELOCATED 18: 35.8, 35.30, 35.41 (i), 35.46, 35.90 (ii), 35.97, 35.98, 35.121, 35.123 (ii), 35.126, 35.134 (i), 35.139, 35.140, 35.141, 35.142, 35.143, 35.144, 35.151
QUARANTINED 153: 35.1, 35.2 (ii), 35.3 (ii), 35.4, 35.5, 35.6 (i), 35.6 (ii), 35.7 (i), 35.7 (iii), 35.9 (i), 35.9 (ii), 35.10, 35.11, 35.12, 35.13, 35.14, 35.15, 35.16, 35.17, 35.18, 35.19, 35.21, 35.22, 35.23, 35.24, 35.25, 35.26, 35.27 (i), 35.28 (ii), 35.29, 35.31, 35.32, 35.33, 35.34, 35.35 (i), 35.36, 35.37, 35.38, 35.40 (ii), 35.41 (ii), 35.42, 35.43, 35.44, 35.45, 35.47, 35.48, 35.49, 35.50, 35.51 (i), 35.51 (ii), 35.52, 35.53 (i), 35.54, 35.55, 35.56, 35.57, 35.58, 35.59, 35.60, 35.61, 35.62, 35.63, 35.64, 35.65, 35.66, 35.67, 35.68, 35.69, 35.70, 35.71, 35.72, 35.73, 35.75, 35.76, 35.77, 35.78, 35.79, 35.80, 35.81, 35.82, 35.83, 35.84, 35.85, 35.86, 35.87, 35.88, 35.89, 35.90 (i), 35.91, 35.92, 35.93, 35.94, 35.95, 35.96, 35.99, 35.100, 35.101, 35.102 (i), 35.103, 35.104 (i), 35.105, 35.106, 35.107, 35.108, 35.114, 35.115, 35.116 (i), 35.116 (ii), 35.117, 35.119, 35.120, 35.122 (ii), 35.123 (i), 35.124, 35.125, 35.127, 35.128, 35.129, 35.130, 35.131, 35.132, 35.133, 35.134 (ii), 35.135, 35.137 (ii), 35.138, 35.145, 35.146, 35.147, 35.148, 35.149, 35.150, 35.152, 35.153 (i), 35.154, 35.156, 35.157, 35.158, 35.159, 35.160, 35.161, 35.162, 35.163, 35.164, 35.165, 35.166, 35.167, 35.168, 35.169 (ii), 35.170, 35.171, 35.172, 35.173
DISCARDED 0: 
HISTORICAL 26: 35.2 (i), 35.3 (i), 35.7 (ii), 35.20, 35.27 (ii), 35.28 (i), 35.35 (ii), 35.39, 35.40 (i), 35.53 (ii), 35.74, 35.102 (ii), 35.104 (ii), 35.109, 35.110, 35.111, 35.112, 35.113, 35.118, 35.122 (i), 35.136, 35.137 (i), 35.153 (ii), 35.155, 35.169 (i), 35.174
UNPLACED 0: 
  RELOCATED to L2 — The tonal reading. The one entangled decision. (17): 35.8, 35.30, 35.41 (i), 35.46, 35.90 (ii), 35.97, 35.98, 35.121, 35.123 (ii), 35.126, 35.134 (i), 35.139, 35.140, 35.141, 35.142, 35.143, 35.144
  RELOCATED to the measurement of the analysis (1): 35.151
verdict AGREES: 3
verdict DIFFERS: 1
verdict THE DERIVATION IS SILENT: 193
AGREES at: 35.90 (ii), 35.126, 35.137 (i)
DIFFERS at: 35.154
quotations not found verbatim: 0
row lines opening with a list or heading marker: 0
```

*`m35_recheck1.txt`:*

```
(a) 6.1-6.34 span identical: True  lengths 1821667 1821667
    foot ADOPTED — carried: stated 0, listed 0
    foot ADOPTED — proposed: stated 0, listed 0
    foot RELOCATED: stated 18, listed 18
    foot QUARANTINED: stated 153, listed 153
    foot DISCARDED: stated 0, listed 0
    foot HISTORICAL: stated 26, listed 26
    foot UNPLACED: stated 0, listed 0
(b) section 10 vs RELOCATED: missing []  extra []
    section 11 vs QUARANTINED: missing []  extra []  entries 153
    section 12 proposals vs ADOPTED -- proposed: missing []  extra []
    section 12 DIFFERS lines vs the foot's DIFFERS: missing []  extra []  lines 1
(c) placeholders left: 0
(d) changed: # The COMPARISON — L3: the derived statements against the outgoing tex
(d) changed: ## 0. Progress — which members are done, and where this stops
(d) changed: ## 6. The tabulation, in the published order
(d) changed: ## 10. The TRANSFER LIST — every RELOCATED row, by target charter
(d) changed: ## 11. The AUDIT QUESTIONS — every QUARANTINED row
(d) changed: ## 12. The PROPOSALS — every ADOPTED — proposed row and every DIFFERS,
(d) changed: ## 13. The distribution so far, counted at this file's own rows
```

*`m35_words1.txt`:*

```
not-a-statement items checked: 64  openings not found: 0
== score: 27
    rride file (Stage-5 fitter)*; *2. Templates*; *3. Score matrix > structure* with *Floating-poin
    rries a claim of its own — range 4's *compute a > score using:* (Row 35.10), range 7's *Zero th
    ot, template and bass candidate given a candidate score.** *Outgoing statement.* — the secti
    uestion:* does the legacy scorer give a candidate score to every combination of root, template
    .11 — the bass-independent base of that candidate score.** *Outgoing statement.* — the same
    ter the bass-independent portion of the candidate score at the current commit? --- **Row 35.1
    enter the bass-dependent portion of the candidate score at the current commit? --- **Row 35.1
    n:* do these five joint terms enter the candidate score at the current commit, and at which sta
    --- **Row 35.14 — candidates ranked by candidate score, then by template, then by root.** *Ou
    he legacy scorer rank its candidates by candidate score, then by the template's order for equal
    elow the bass within of the unbonused candidate score, at the current commit, and is it reach
    readings span identical PCs (e.g. Bb6 = Gm7/Bb); score cannot reliably distinguish in bass-hea
    aise that half-diminished alternative's candidate score by after the deduction and before the
    **Row 35.161 — every cell re-given its candidate score with three progression terms.** *Outgo
    pipeline add , and to every cell's candidate score, the first before the multiply, at the
    ose as winner the cell with the highest candidate score across all basses at the current commit
    ine set its threshold from the winner's candidate score less its bass bonus, by , at the curre
    urrent commit? --- **Row 35.172 — the candidate score reconstructed in the same arithmetic po
    w 35.10 — does the legacy scorer give a candidate score to every combination of root, template
    ter the bass-independent portion of the candidate score at the current commit? - Row 35.12 — wh
    enter the bass-dependent portion of the candidate score at the current commit? - Row 35.13 — do
    3 — do these five joint terms enter the candidate score at the current commit, and at which sta
    he legacy scorer rank its candidates by candidate score, then by the template's order for equal
    aise that half-diminished alternative's candidate score by - Row 35.115 — does the bass-root re
    pipeline add , and to every cell's candidate score, the - Row 35.162 — does the pipeline a
    ose as winner the cell with the highest candidate score across all basses at the - Row 35.165 —
    ine set its threshold from the winner's candidate score less its bass bonus, by - Row 35.166 —
== scores: 5
    ing to how a chord identifier forms its candidate scores. (b) **The bass a candidate reading tak
    then by the template's order for equal candidate scores, then by root, at the current commit?
    **Row 35.96 — the ranking changed, the candidate scores untouched.** *Outgoing statement.* —
    the gates reorder alone, leaving the candidate scores in unchanged, at the current commit?
    the gates reorder alone, leaving the candidate scores in unchanged, at the - Row 35.99 — do
== scoring: 55
    before range 1; the headings *1. Overview* and > *Scoring constants are readable from an optional
    se)*, *Other terms (briefly)* and *The registered scoring constants this document > does not tabl
    t fall under it; *5. Joint (bass, root, template) scoring*; *6. > Post-scoring gates (A–L)* with
    Joint (bass, root, template) scoring*; *6. > Post-scoring gates (A–L)* with *§6a. The unified pro
    hem*, > *Four archive-only dead ends of the chord-scoring path — do not retry any of them* outsid
    34, and *The > validation basis of every hand-set scoring magnitude on this surface is retroactiv
    (checklist)*; *10. Harmonic function layer*; *11. Scoring oracle vs competition pipeline (E2d > r
    ce after it stating its claim in full —, * — the scoring oracle.* > and *Oracle temporal-signal
    on bonuses; the gates applied after the candidate scoring, the rule on what they may read, their
    > change to the chord decision and its candidate scoring may attempt** — §8's constraints and de
    the rules on the chord decision and its candidate scoring; their grounds, listed under the second
    .* — under the document's title *Chord Analyzer Scoring Model*, the quotation-block paragraph l
    e movement alone, with no change to the candidate scoring or to the inference; (ii) each of the f
    a change to the chord decision and its candidate scoring may attempt, as §6.21 placed the rules
    the rules on the chord decision and its candidate scoring. --- **Row 35.9 — tone collection: a
    Row 35.18 — the gates applied after the candidate scoring, listed.** *Outgoing statement.* — t
    tes the legacy scorer applies after its candidate scoring at the current commit? --- **Row 35.1
    ent.* — the section *1. Overview*, sub-section *Scoring constants are readable from an optional
    n what a change to the chord decision's candidate scoring may attempt, as §6.21 placed the rules
    the rules on the chord decision and its candidate scoring. --- **Row 35.31 — Gate R's predicate
    a ratified rule of the chord decision's candidate scoring, as §6.21 placed such rules. (ii) **QUA
    ow a correction of the chord decision's candidate scoring is conditioned, as §6.21 placed the rul
    the rules on the chord decision and its candidate scoring. *The decisions register at this row.*
    s and penalty terms*, sub-section *The registered scoring constants this document does not table
    — the section *5. Joint (bass, root, template) scoring*, the paragraph led * * (locator: lines
    * *Outgoing statement.* — the section *6. Post-scoring gates (A–L)*, its opening paragraph (lo
    -- **Row 35.97 — a gate or rule of the candidate scoring reading structured fields only.** *Out
    * *Outgoing statement.* — the section *6. Post-scoring gates (A–L)*, the paragraph led *★ POIN
    * — a rule on what the chord decision's candidate scoring may read, as §6.21 placed the rules on
    the rules on the chord decision and its candidate scoring. --- **Row 35.98 — the rule binding e
    * *Outgoing statement.* — the section *6. Post-scoring gates (A–L)*, the paragraph led *Outer
    * *Outgoing statement.* — the section *6. Post-scoring gates (A–L)*, sub-section *§6a. The uni
    * *Outgoing statement.* — the section *6. Post-scoring gates (A–L)*, sub-section *§6a. The uni
    ing statement.* Option B — the section *6. Post-scoring gates (A–L)*, sub-section *§6a. The uni
    — a closed line of the chord decision's candidate scoring, not to be retried, as §6.21 placed the
    the rules on the chord decision and its candidate scoring. *The decisions register at this row.*
    traint on changing the chord decision's candidate scoring: none of the four is to be removed. *T
    section *Four archive-only dead ends of the chord-scoring path — do not retry any of them*, its f
    — a closed line of the chord decision's candidate scoring, not to be retried, as §6.21 placed the
    the rules on the chord decision and its candidate scoring. *The decisions register at this row.*
    section *Four archive-only dead ends of the chord-scoring path — do not retry any of them*, its s
    — a closed line of the chord decision's candidate scoring, not to be retried, as §6.21 placed the
    the rules on the chord decision and its candidate scoring. *The decisions register at this row.*
    section *Four archive-only dead ends of the chord-scoring path — do not retry any of them*, its t
    — a closed line of the chord decision's candidate scoring, not to be retried, as §6.21 placed the
    the rules on the chord decision and its candidate scoring. *The decisions register at this row.*
    section *Four archive-only dead ends of the chord-scoring path — do not retry any of them*, its f
    — a closed line of the chord decision's candidate scoring, not to be retried, as §6.21 placed the
    the rules on the chord decision and its candidate scoring. *The decisions register at this row.*
    de.** *Outgoing statement.* — the section *11. Scoring oracle vs competition pipeline (E2d red
    eline (E2d redesign)*, the paragraph led * — the scoring oracle.* (locator: lines 1602–1603). *
    ms.** *Outgoing statement.* — the section *11. Scoring oracle vs competition pipeline (E2d red
    ne.** *Outgoing statement.* — the section *11. Scoring oracle vs competition pipeline (E2d red
    5.98 — every gate and every term of the candidate scoring reading structured fields only, no - Ro
    tes the legacy scorer applies after its candidate scoring at the current commit? - Row 35.19 — do
== key: 10
    *Row 35.53 — the diatonic-root bonus, reading the key signature's collection; its fix at OI-1
    onus is awarded where the root is a member of the key signature's diatonic collection, the te
    Audit question:* does test the root against the key signature's diatonic collection, readin
    arrying no mark. --- **Row 35.134 — the coupled key-and-chord minority the principled form;
    restricting the override to the genuinely coupled key-and-chord minority is the principled fo
    g no mark. --- **Row 35.135 — the blocker a per-key re-decode of the chord, still owed.**
    echanism leave the chord unchanged, and is no per-key re-decode of the chord built, at the cu
    riction of the fine-grain override to the coupled key-and-chord minority as its principled -
    Row 35.53 (i) — does test the root against the key signature's diatonic collection, readin
    echanism leave the chord unchanged, and is no per-key re-decode of the chord - Row 35.137 (ii
== note: 8
    ier's purpose; read as a statement about the bass note L3's chord > symbol publishes, it would
    e, travel > with them. (d) **That a sparse lowest note in an upper register is no bass** (Rows
    eligibility flags; a sparse upper-register lowest note no bass.** *Outgoing statement.* bass
    L3-S4: **AGREES** — both say the lowest sounding note need not be the bass. The derivation's
    — a rule of the chord decision on which sounding note counts as the bass, as Row 22.59 placed
    L3-S4: **AGREES** — both say the lowest sounding note need not be the bass. The derivation's
    — a rule of the chord decision on which sounding note counts as the bass, as Row 35.90 (ii).
    he - Rows 35.90 (ii) and 35.126 — a sparse lowest note in an upper register no bass voice, ear
== notes: 2
    sion bonuses still respect it; (ii) sparse lowest notes in an upper register are not real bass
    --- **Row 35.126 — sparse upper-register lowest notes earning no inversion bonus.** *Outgoin
== flat: 4
    ? --- **Row 35.79 — the extension weight at the flat thirteenth.** *Outgoing statement.*
    --- **Row 35.81 — the factor for a third spelled flat over a Sus4 reading.** *Outgoing state
    e the extension factor where the third is spelled flat, as the row says, at the current commit
    e the extension factor where the third is spelled flat, as the row says, - Row 35.82 — does
== register: 98
    is empty. > **Thirteen decisions of the decisions register's data file are homed inside this membe
    lying wholly inside one range: in the decisions > register's list, **D-327** at 478–490 (range 10,
    whole); > and **one RETIRED entry** the decisions register's INDEX does not show, **D-216** at 114
    by this session at D-216's record). The decisions register's INDEX records **D-215** and > **D-221
    t D-215, D-221 and D-537 — facts of the decisions register, relayed and moving no disposition. > *
    ere, and therefore in no member: in the decisions register's list, **D-321** at 265–278, **D-322**
    from ranges 2 and 3 drops it**, as the decisions register's own convention > drops it from a verb
    them. (d) **That a sparse lowest note in an upper register is no bass** (Rows 35.90 (ii) and 35.12
    rom Gate R at the current commit? *The decisions register at this row.* The quoted statement lies
    D-327** (lines 478–490), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    ified 2026-08-02 · user — a fact of the decisions register, relayed, moving no disposition and car
    question:* the same as Row 35.5. *The decisions register at this row.* The quoted statement lies
    D-327** (lines 478–490), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    ified 2026-08-02 · user — a fact of the decisions register, relayed, moving no disposition and car
    rd sounds, at the current commit? *The decisions register at this row.* The quoted statement lies
    D-327** (lines 478–490), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    ified 2026-08-02 · user — a fact of the decisions register, relayed, moving no disposition and car
    cision and its candidate scoring. *The decisions register at this row.* The quoted statement lies
    D-537** (lines 549–559), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    LEGACY-marked, group G — a fact of the decisions register, relayed, moving no disposition and car
    threshold, at the current commit? *The decisions register at this row.* The quoted statement lies
    D-537** (lines 549–559), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    LEGACY-marked, group G — a fact of the decisions register, relayed, moving no disposition and car
    question:* the same as Row 35.47. *The decisions register at this row.* The quoted statement lies
    D-537** (lines 549–559), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    LEGACY-marked, group G — a fact of the decisions register, relayed, moving no disposition and car
    mbined into the eligibility flags; a sparse upper-register lowest note no bass.** *Outgoing state
    respect it; (ii) sparse lowest notes in an upper register are not real bass voices and must not t
    cision and its candidate scoring. *The decisions register at this row.* The quoted statement lies
    f **D-215** (line 1137), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    LEGACY-marked, group U — a fact of the decisions register, relayed, moving no disposition and car
    one of the four is to be removed. *The decisions register at this row.* The quoted statement lies
    D **D-216** (line 1141), * *, which the decisions register's INDEX does not show: its data file ke
    red record carries, * * — a fact of the decisions register's data file, relayed, moving no disposi
    on bonuses at the current commit? *The decisions register at this row.* The quoted statement lies
    221** (lines 1177–1178), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    LEGACY-marked, group U — a fact of the decisions register, relayed, moving no disposition and car
    rrying no mark. --- **Row 35.126 — sparse upper-register lowest notes earning no inversion bonus
    s as the bass, as Row 35.90 (ii). *The decisions register at this row.* The quoted statement lies
    221** (lines 1177–1178), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    LEGACY-marked, group U — a fact of the decisions register, relayed, moving no disposition and car
    -positive, and does it reproduce? *The decisions register at this row.* The quoted statement lies
    490** (lines 1276–1284), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    27, for the two quantities named. *The decisions register at this row.* The quoted statement lies
    490** (lines 1276–1284), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    .127, for the best setting found. *The decisions register at this row.* The quoted statement lies
    490** (lines 1276–1284), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    ied, and does its harm reproduce? *The decisions register at this row.* The quoted statement lies
    491** (lines 1285–1292), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    uestion:* the same as Row 35.130. *The decisions register at this row.* The quoted statement lies
    491** (lines 1285–1292), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    , for the prediction of the root. *The decisions register at this row.* The quoted statement lies
    491** (lines 1285–1292), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    ed nowhere at the current commit? *The decisions register at this row.* The quoted statement lies
    493** (lines 1293–1301), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    uestion:* the same as Row 35.133. *The decisions register at this row.* The quoted statement lies
    493** (lines 1293–1301), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    ord built, at the current commit? *The decisions register at this row.* The quoted statement lies
    493** (lines 1293–1301), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    dation, recorded and not adopted. *The decisions register at this row.* The quoted statement lies
    492** (lines 1302–1312), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    the pass, and does it reproduce? *The decisions register at this row.* The quoted statement lies
    492** (lines 1302–1312), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    e same as Rows 35.127 and 35.130. *The decisions register at this row.* The quoted statement lies
    492** (lines 1302–1312), * *, which the decisions register's INDEX records as LIVE, group H, entry
    ified 2026-08-04 · user — a fact of the decisions register, relayed, moving no disposition and car
    cision and its candidate scoring. *The decisions register at this row.* The quoted statement lies
    299** (lines 1413–1417), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    ified 2026-08-02 · user — a fact of the decisions register, relayed, moving no disposition and car
    same closed line, stated in full. *The decisions register at this row.* The quoted statement lies
    299** (lines 1413–1417), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    ified 2026-08-02 · user — a fact of the decisions register, relayed, moving no disposition and car
    cision and its candidate scoring. *The decisions register at this row.* The quoted statement lies
    300** (lines 1418–1424), * *, which the decisions register's INDEX records as DEFERRED and LEGACY-
    ified 2026-08-02 · user — a fact of the decisions register, relayed, moving no disposition and car
    cision and its candidate scoring. *The decisions register at this row.* The quoted statement lies
    301** (lines 1425–1430), * *, which the decisions register's INDEX records as DEFERRED and LEGACY-
    ified 2026-08-02 · user — a fact of the decisions register, relayed, moving no disposition and car
    cision and its candidate scoring. *The decisions register at this row.* The quoted statement lies
    302** (lines 1431–1439), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    ified 2026-08-02 · user — a fact of the decisions register, relayed, moving no disposition and car
    same closed line, stated in full. *The decisions register at this row.* The quoted statement lies
    302** (lines 1431–1439), * *, which the decisions register's INDEX records as LIVE and LEGACY-mark
    ified 2026-08-02 · user — a fact of the decisions register, relayed, moving no disposition and car
    ot withheld, carrying no mark**: of the decisions register's list, D-327 at Rows 35.41 to 35.43,
    ws 35.8 and 35.30 — lie in homes of the decisions register's data file named at their - Rows 35.41
    ii) and 35.126 — a sparse lowest note in an upper register no bass voice, earning no inversion bon
== tie: 1
    3. Score matrix > structure* with *Floating-point tie policy*; under *4. Bonus and penalty te
== scale: 1
    collection, the term reading no tonic and no mode scale and sharing that test with ; (ii) it w
== mode: 2
    onic collection, the term reading no tonic and no mode scale and sharing that test with ; (ii
    re's diatonic collection, reading no tonic and no mode, at the current commit? (ii) **HISTORIC
== interval: 5
    *Row 35.38 — the template-tone test read from the interval bitmasks.** *Outgoing statement.* —
    TINED.** *Audit question:* does test the bass's interval above the root against a table derive
    it question:* does weight the extension at that interval in at the current commit? --- **Row
    d condition. - Row 35.38 — does test the bass's interval above the root against a table derive
    - Row 35.79 — does weight the extension at that interval in at the current - Row 35.80 — does
```

**Read by hand, every word the scan reports.** *score* and *scores*: each is *candidate score* or *candidate scores*,
or inside a title or quotation of the member that the mask did not reach — the document's title *Chord Analyzer Scoring
Model*, its heading *3. Score matrix structure*, the range-4 lead *compute a score using:*, and the member's own
table-row words *score cannot reliably distinguish*, inside Row 35.102's long quotation (line 38215 of the reading
file), confirmed there at the blob; *scoring*: *candidate scoring*, or inside the document's headings (*Scoring
constants are readable from an optional override file*, *5. Joint (bass, root, template) scoring*, *6. Post-scoring gates
(A–L)*, *Four archive-only dead ends of the chord-scoring path*, *11. Scoring oracle vs competition pipeline*) and its
lead *— the scoring oracle.*; *key*: the key signature's diatonic collection, and *key-and-chord* — the tonal sense;
*note* and *notes*: the lowest sounding note, a pitch event; *flat*: the flat thirteenth and a third spelled flat, the
accidental; *register*: *the decisions register* in full, or *upper register*, the pitch sense; *tie*: the document's
heading *Floating-point tie policy*; *scale* and *mode*: *mode scale* and *mode*, the musical senses; *interval*: the
pitch interval (*interval bitmasks*, *the bass's interval above the root*). **No slip of this session's wording was
found by the scan at the committed blob**; the pre-copy run (`m35_words0.txt`) reported the same words at fewer lines,
the difference being the banner, §0, §10, §12 and §13 edits made after the copy.

## 3. Task 2 — the close

**2(a) — the `STATUS.md` entries, first.** Three entries at the top, written with the file tools' Edit [225]: the close
entry, naming this dispatch by its file name and carrying the moved `Last updated: ` prefix, then the entries for Task 1
and Task 0, each saying `Same dispatch`, all three pointers to this report with no count restated. The prefix was removed
from the twelfth tabulation batch's close entry; no other existing sentence was rewritten or removed. **A case-insensitive
substring search of `STATUS.md` for all 26 ruled terms, run after the entries were written, hit one line only** [226]:

```
26:phrase
```

— the standing *ARCHIVED 2026-08-17, THE SECOND ACT* paragraph, where `phrase` matches inside *paraphrase*, at line 26
before the move. Run again after the move [266], and that line confirmed [267]:

```
20:phrase
```

```
20:paraphrase
```

the same line, at line 20. No entry was corrected after the move: each says only what the scratch files and the objects
show of this batch.

**2(b) — the forward bound.** Read at the object `06b17b46…:tools/audit/gen_status_batch_bound.py`, redirected to a
scratch file outside the repository and read there at its authored-aiming region (the five constants with their head
comments and the end of `PREVIOUS_AIMINGS`, located by a search) [227 to 233]; the object's blob and the working copy's:

```
exit:0
9e716cc9acff3457a6f9ca4876c208d0198ddaeb
9e716cc9acff3457a6f9ca4876c208d0198ddaeb
exit:0
```

`BASE_COMMIT` is the member commit of Task 1, `5d9f356a…`, this batch's last task commit before the close; its
`STATUS.md` object is the boot one — `git rev-parse <commit>:STATUS.md` for `06b17b46…`, `d1b3a26f…` and `5d9f356a…`, in
that order, then the previous close commit's subject [234]:

```
dba6f051cf8716454836f3efb1fbb2a7fe4db0a3
dba6f051cf8716454836f3efb1fbb2a7fe4db0a3
dba6f051cf8716454836f3efb1fbb2a7fe4db0a3
exit:0
75bbfa9326db01819b7036f660b71bc1c388365b Close: the L3 comparison continued from position 27, under its dispatch
exit:0
```

**All five authored constants were aimed** [235 to 239]: `BASE_COMMIT` to `5d9f356a0e5f7d11ae5e63a270d7be1537aaac37`,
`PREVIOUS_BATCH_DISPATCH` to `cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md`, `ACT_DATE` to `2026-10-21`
(the day the move ran, which is this dispatch's date too), `DISPATCH` to this dispatch's file name, `TASK` kept at
`Task 2`; `MOVE_KIND` stays `ordinary`. This batch's aiming is appended to `PREVIOUS_AIMINGS`; the twelfth batch's aiming
was already the last row and was not appended twice. The head comments name every former value; no function and no
existing row was touched.

`python tools/audit/gen_status_batch_bound.py --apply` and `--check`, each into a scratch file [241]:

```
apply exit:0
check exit:0
```

the `--apply` output, whole:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 3, 2,953 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

and the `--check` output, whole:

```
  entries moved: 3, 2,953 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**The prediction HELD, read at the artifact rather than at the green `--check` (OI-379).**
`tools/audit/status_batch_bound.json` → `the_moved` [244]:

```
662: "the_moved": [
663-  {
664-   "line_at_base": 8,
665-   "characters": 1819,
666-   "sha256": "8e932ed3300146d28d1910a1d5962d1c56e2697aa15f66c4683f018c1d454e51",
667-   "membership": "names the dispatch",
668-   "the_one_declared_adjustment_applied": true,
669-   "opening": "*2026-10-20 (CC — `records/cc/instructions/cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md`, Task 2, the close. **★★ THE L3 COMPARISON C"
670-  },
671-  {
672-   "line_at_base": 10,
673-   "characters": 740,
674-   "sha256": "a81b49a29e4160b3def59aeca521e5df8a69277a02f1aaf219d29d14a0fa2e39",
675-   "membership": "says `Same dispatch`, in the run below the entry that names it",
676-   "the_one_declared_adjustment_applied": false,
677-   "opening": "*2026-10-20 (CC — Same dispatch, Task 1. **THE L3 COMPARISON CONTINUED: POSITIONS 27 TO 34 TABULATED**: a capacity judgment written to a file outside "
678-  },
679-  {
680-   "line_at_base": 12,
681-   "characters": 394,
682-   "sha256": "7ca5fddd52a36fdffcf03e5b457b9c3b2697140605b1e7f6f066e35ae0c01916",
683-   "membership": "says `Same dispatch`, in the run below the entry that names it",
684-   "the_one_declared_adjustment_applied": false,
685-   "opening": "*2026-10-20 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRY 436 ARE LANDED**, as they stood: each checked at its last bytes at its blob"
686-  }
687- ],
688- "reconciliation": {
689-  "every_moved_entry_is_byte_present_in_STATUS_ARCHIVE_md_exactly_once": true,
690-  "every_moved_entry_is_absent_from_STATUS_md": true,
691-  "what_that_proves_together": "Nothing left the must-read that is not in the archive, and each entry was MOVED rather than copied. Both are byte comparisons against the file at HEAD and against the git object at the base commit named by explicit hash — never against the memory of performing the move (#15).",
692:  "★_why_the_moved_set_is_read_from_a_git_object": "The set is a statement about the file as it stood when the act ran. Reading it from the base commit's own object makes this check re-derive forever as later batches legitimately append their own entries — the OI-344 shape avoided by construction, on the precedent gen_status_archive_pass.py sets (D-646)."
693- }
694-}
```

— exactly the twelfth tabulation batch's three entries: its close entry (membership *names the dispatch*; the declared
prefix adjustment applied to it), its Task 1 entry and its Task 0 entry. The head of `STATUS.md` after the move, each
entry's opening:

```
8:*Last updated: 2026-10-21 (CC — `records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md`, Task 2, the close. **★★ THE L3 COMPA
10:*2026-10-21 (CC — Same dispatch, Task 1. **THE L3 COMPARISON CONTINUED: POSITION 35 TABULATED**: a capacity judgment written to a file outside the
12:*2026-10-21 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRY 437 ARE LANDED**, as they stood: each checked at its last bytes at its 
14:*2026-09-02 (CC — **★★ THE L0/L1 COMPARISON IS OPEN AND SEVEN OF ITS TWENTY-NINE DOCUMENTS ARE TABULATED; THE READING FILE EXISTS.** `ratification
16:*2026-09-02 (CC — Same dispatch, Tasks 0 and 1. **★★ RULING 33's CUT IS APPLIED AND THE SIZE STOP THAT ENDED THE PREVIOUS BATCH DOES NOT FIRE.** `
```

The two 2026-09-02 entries stay in `STATUS.md`, directly below this batch's three; no STOP.

**2(c) — the regenerations and the checks.** The six checks, after the move, each into its own scratch file [247]:

```
gen_evidence_pin_membership exit:0
gen_l0_l1_outgoing_population exit:0
gen_defense_share exit:1
gen_l3_outgoing_population exit:0
gen_session_start_read_size exit:1
gen_status_batch_bound exit:0
exit:0
```

```
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 169
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
```

```
l0_l1_outgoing_population.json re-derives
```

```
STALE vs the measurement: defense_share.json does not re-derive
```

```
l3_outgoing_population.json re-derives
```

```
STALE vs the measurement: session_start_read_size.json does not re-derive
```

```
  entries moved: 3, 2,953 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

Red exactly as A2 provides for: `gen_defense_share.py` and `gen_session_start_read_size.py`. **The L3 and L0/L1
population checks stayed green and were not regenerated**; the evidence pin stayed green. `gen_defense_share.py` written,
then `--check`; then, **last, after the final edit to `STATUS.md`**, `gen_session_start_read_size.py` written, then
`--check` [253]:

```
defense regen exit:0
defense check exit:0
ssrs regen exit:0
ssrs check exit:0
```

`gen_defense_share.py`, written:

```
wrote tools/audit/defense_share.json
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   41071  ( 8.45%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (105876): 12.24%
    of the whole session-start read (248690): 5.21%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

and its `--check`:

```
the defense-share measurement re-derives
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   41071  ( 8.45%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (105876): 12.24%
    of the whole session-start read (248690): 5.21%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

`gen_session_start_read_size.py`, written:

```
wrote tools/audit/session_start_read_size.json
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              41071
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 169617, the six session-start spans 105876, overstated by 63741
    CLAUDE.md                                                                105876
    STATUS.md                                                                 12261
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 248690
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 248690 [ruled membership]  (-118431, -32.26%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 248690 [ruled membership]  (-48142, -16.22%)  <- CROSSES A REGIME BOUNDARY
```

and its `--check`:

```
the session-start read measurement re-derives
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              41071
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 169617, the six session-start spans 105876, overstated by 63741
    CLAUDE.md                                                                105876
    STATUS.md                                                                 12261
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 248690
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 248690 [ruled membership]  (-118431, -32.26%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 248690 [ruled membership]  (-48142, -16.22%)  <- CROSSES A REGIME BOUNDARY
```

The six checks again, all green, followed by each moved artifact's blob at `06b17b46…` and its new blob written by `git
hash-object -w` [258]:

```
gen_evidence_pin_membership exit:0
gen_l0_l1_outgoing_population exit:0
gen_defense_share exit:0
gen_l3_outgoing_population exit:0
gen_session_start_read_size exit:0
gen_status_batch_bound exit:0
warning: in the working copy of 'tools/audit/defense_share.json', LF will be replaced by CRLF the next time Git touches it
tools/audit/defense_share.json old e83d529f335ca8205e56952ca1100185880e5836 new 6faf22b4a872c9cc323d8535b02a751f4853422b
warning: in the working copy of 'tools/audit/session_start_read_size.json', LF will be replaced by CRLF the next time Git touches it
tools/audit/session_start_read_size.json old f5ac583bde572eeaf8b3954864902fa3c0cba140 new 2d149c7f3b57722a3296d551f8db92bc36ef29ad
warning: in the working copy of 'tools/audit/status_batch_bound.json', LF will be replaced by CRLF the next time Git touches it
tools/audit/status_batch_bound.json old 49648372bf9e94defb7e5bbe22c11fb867f5257d new 430460f96a5b29f1cefaa5d4ca372c53585e6cbc
exit:0
```

**What moved, at the blob diff against `06b17b46…` by explicit hash** — `git diff <blob at 06b17b46> <new blob>`, both
hashes written literally, each into a scratch file [259], read with the file tools [260 to 262]:

`tools/audit/defense_share.json` — the whole-read denominator only:

```
diff --git a/e83d529f335ca8205e56952ca1100185880e5836 b/6faf22b4a872c9cc323d8535b02a751f4853422b
index e83d529f33..6faf22b4a8 100644
--- a/e83d529f335ca8205e56952ca1100185880e5836
+++ b/6faf22b4a872c9cc323d8535b02a751f4853422b
@@ -77,7 +77,7 @@
  ],
  "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
   "the_six_session_start_spans": 105876,
-  "the_whole_ordinary_session_start_read": 248661,
+  "the_whole_ordinary_session_start_read": 248690,
   "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked defense; the second says how much of the WHOLE boot it is. A share quoted against one of them is not the share against the other."
  },
  "per_span": [
```

`tools/audit/session_start_read_size.json` — `STATUS.md`'s member and the totals derived from it:

```
diff --git a/f5ac583bde572eeaf8b3954864902fa3c0cba140 b/2d149c7f3b57722a3296d551f8db92bc36ef29ad
index f5ac583bde..2d149c7f3b 100644
--- a/f5ac583bde572eeaf8b3954864902fa3c0cba140
+++ b/2d149c7f3b57722a3296d551f8db92bc36ef29ad
@@ -176,11 +176,11 @@
   },
   "characters_per_member": {
    "CLAUDE.md": 105876,
-   "STATUS.md": 12232,
+   "STATUS.md": 12261,
    "DECISIONS.md": 127727,
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
   },
-  "total_characters": 248661,
+  "total_characters": 248690,
   "further_spans_of_the_same_artifact_NOT_counted_into_the_read": {
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows": {
     "characters": 62498,
@@ -276,10 +276,10 @@
    "from_commit": "1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
    "from_total": 367121,
    "from_regime": "whole-file practice",
-   "to_total": 248661,
+   "to_total": 248690,
    "to_regime": "ruled membership",
-   "change_in_characters": -118460,
-   "change_percent": -32.27,
+   "change_in_characters": -118431,
+   "change_percent": -32.26,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   },
@@ -287,10 +287,10 @@
    "from_commit": "594074e1e1900079e449d2b79a38920d21bca6e6",
    "from_total": 296832,
    "from_regime": "whole-file practice",
-   "to_total": 248661,
+   "to_total": 248690,
    "to_regime": "ruled membership",
-   "change_in_characters": -48171,
-   "change_percent": -16.23,
+   "change_in_characters": -48142,
+   "change_percent": -16.22,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   }
```

`tools/audit/status_batch_bound.json` — the aiming and the moved entries:

```
diff --git a/49648372bf9e94defb7e5bbe22c11fb867f5257d b/430460f96a5b29f1cefaa5d4ca372c53585e6cbc
index 49648372bf..430460f96a 100644
--- a/49648372bf9e94defb7e5bbe22c11fb867f5257d
+++ b/430460f96a5b29f1cefaa5d4ca372c53585e6cbc
@@ -1,7 +1,7 @@
 {
  "what_this_is": "RULING 4's FORWARD BOUND, applied at one batch close: which of the then-previous batch's STATUS.md entries moved to the archive, and the mechanical proof that nothing was lost or altered in transit (#12). Every figure here is computed; none is transcribed (D-431).",
  "generated_by": "tools/audit/gen_status_batch_bound.py",
- "dispatch": "cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md, Task 2",
+ "dispatch": "cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md, Task 2",
  "★_every_previous_aiming_of_this_tool_kept_rather_than_replaced": [
   {
    "executing_act": "cc_instruction_preparation_sixth.md, Task 1",
@@ -645,38 +645,44 @@
    "base_commit": "f85ed74066f8e73682a9d853013be68978de95be",
    "the_then_previous_batch": "cc_instruction_l3_comparison_tabulation_eleventh_2026_10_20.md",
    "the_kind_of_move": "ordinary"
+  },
+  {
+   "executing_act": "cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md, Task 2",
+   "base_commit": "5d9f356a0e5f7d11ae5e63a270d7be1537aaac37",
+   "the_then_previous_batch": "cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md",
+   "the_kind_of_move": "ordinary"
   }
  ],
  "the_ruling": "Ruling 4 of cowork_rulings_2026_08_17_governing_surface_split.md: an entry is SUPERSEDED the moment a later batch's close exists; the site keeps only the latest batch's entries, and every future batch close moves the then-previous batch's entries in the same act that writes its own.",
- "base_commit": "f85ed74066f8e73682a9d853013be68978de95be",
- "the_then_previous_batch": "cc_instruction_l3_comparison_tabulation_eleventh_2026_10_20.md",
+ "base_commit": "5d9f356a0e5f7d11ae5e63a270d7be1537aaac37",
+ "the_then_previous_batch": "cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md",
  "the_kind_of_move": "ordinary",
  "entries_moved": 3,
- "characters_moved": 3013,
+ "characters_moved": 2953,
  "the_moved": [
   {
    "line_at_base": 8,
-   "characters": 1880,
-   "sha256": "e9c6aee2fcf82054b8868add7b25c0f47a4f359c5c366bea51ac88b7344b2389",
+   "characters": 1819,
+   "sha256": "8e932ed3300146d28d1910a1d5962d1c56e2697aa15f66c4683f018c1d454e51",
    "membership": "names the dispatch",
    "the_one_declared_adjustment_applied": true,
-   "opening": "*2026-10-20 (CC — `records/cc/instructions/cc_instruction_l3_comparison_tabulation_eleventh_2026_10_20.md`, Task 2, the close. **★★ THE L3 COMPARISON "
+   "opening": "*2026-10-20 (CC — `records/cc/instructions/cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md`, Task 2, the close. **★★ THE L3 COMPARISON C"
   },
   {
    "line_at_base": 10,
-   "characters": 738,
-   "sha256": "c58711360ce123eff81beeee711dc9a2cf529aa7712e60f1f6a49459ba2a3921",
+   "characters": 740,
+   "sha256": "a81b49a29e4160b3def59aeca521e5df8a69277a02f1aaf219d29d14a0fa2e39",
    "membership": "says `Same dispatch`, in the run below the entry that names it",
    "the_one_declared_adjustment_applied": false,
-   "opening": "*2026-10-20 (CC — Same dispatch, Task 1. **THE L3 COMPARISON CONTINUED: POSITIONS 23 TO 26 TABULATED**: no capacity judgment written as a message befo"
+   "opening": "*2026-10-20 (CC — Same dispatch, Task 1. **THE L3 COMPARISON CONTINUED: POSITIONS 27 TO 34 TABULATED**: a capacity judgment written to a file outside "
   },
   {
    "line_at_base": 12,
-   "characters": 395,
-   "sha256": "c59a2e32ed57fe090c43a05972b5705e9ae854720592e4ee87c301937078ad3a",
+   "characters": 394,
+   "sha256": "7ca5fddd52a36fdffcf03e5b457b9c3b2697140605b1e7f6f066e35ae0c01916",
    "membership": "says `Same dispatch`, in the run below the entry that names it",
    "the_one_declared_adjustment_applied": false,
-   "opening": "*2026-10-20 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRY 435 ARE LANDED**, as they stood: each checked at its last bytes at its blob"
+   "opening": "*2026-10-20 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRY 436 ARE LANDED**, as they stood: each checked at its last bytes at its blob"
   }
  ],
  "reconciliation": {
```

**No member of either population, no item-4 passage and no member of `the_tabulation_population` moved**: neither
population artifact moved at all, and the L3 population's one `STATUS.md` residue hit record did not move line, its
check green throughout. The tracked modifications at the close, before staging (`changed_paths.py` into a scratch file,
searched there):

```
 M	STATUS.md
 M	STATUS_ARCHIVE.md
 M	tools/audit/claude_md_finer_archive.json
 M	tools/audit/defense_share.json
 M	tools/audit/gen_status_batch_bound.py
 M	tools/audit/session_start_read_size.json
 M	tools/audit/status_batch_bound.json
```

— the six close paths and the carried `tools/audit/claude_md_finer_archive.json`, which is held back.

**2(d) — this report. 2(e) — the close section** appended to `records/cowork/handoff/cowork_away_returns.md`. **2(f) —
the close commit** by explicit path, the staged set proved, its identity and push line in the git log and in the close
section's end-state portion.

**E1 — MET for position 35**: its manifest; every outgoing statement with exactly one disposition, none UNPLACED; the one
DIFFERS with its one-sentence difference and nothing chosen; no mark at position 35, and every home inside its ranges
named beside its rows; the transfer list, audit questions and proposals gathered, checked both ways; §0 true of the file,
the previous batch's stop stated as its own clause in the true words 1(f) gives; the capacity-judgment file written before
the member was opened and quoted whole above; no member beyond position 35; no recommendation anywhere; A5 intact at the
member commit, §6.1 to §6.34 included (recheck (a)).

**E2 — MET at the close tree as far as the close can show it**: every `--check` A2 names green; the failing set's proof
at the full guard run is Task 3's, recorded by its own commit.

## 4. A1 to A5, graded

- **A1 — HELD, BY CONTENT** (§1, 0(c)). During the run no further handoff entry or ruling record appeared.
- **A2 — HELD.** At the opening capture: the thirteen FAIL and nothing else, zero STOPs, run 82, the evidence pin green,
  the header *"the guard state re-derives"*. At the close: the two reds A2 names for this batch's `STATUS.md` acts, each
  regenerated; the L3 and L0/L1 populations green throughout, the L3 population's `STATUS.md` residue record not moved.
  The end state is recorded by its own commit.
- **A3 — HELD.** `gen_l2_outgoing_population.py` was not run in any operating mode, and its artifact was not touched.
- **A4 — HELD.** No tool added or enrolled; `gen_guard_state.py` and `gen_l3_outgoing_population.py` not edited; one
  tool source touched, `gen_status_batch_bound.py`'s authored aiming and its head comments.
- **A5 — HELD at the member commit** (§6.1 to §6.34 identical, recheck (a): *"(a) 6.1-6.34 span identical: True"*), and
  verified at the objects after the last commit by the end-state portion of the close section (Task 3).

## 5. Findings of the run, and observations recorded and not acted on

**No finding of the comparison apparatus.** The member's document exists at its path; **every one of its eighty-four
range line texts matches the line at its locator** — the first character-by-character comparison of them, as the
dispatch's Findings section says (*"all 2x42 boundary texts match: True"*); the outgoing text parsed into statements;
and every derived statement carries its six fields. **No finding under 1(h)**: the judgment did not fall short of the
whole member.

**One fact of the premise ledger found incomplete at the object, surfaced here and not absorbed.** The dispatch states
twice that *"the document's fences stand at lines 333 to 335, 1091 to 1094, 1104 to 1109 and 1568 to 1573, all in the
cut"* and speaks of *"the four fenced blocks"*. **The document has FIVE fenced blocks**: a search for lines opening with
three backticks in the blob `8410b00e…` finds ten fence lines, at 227, 230, 333, 335, 1091, 1094, 1104, 1109, 1568 and
1573, so the fifth block is lines 227 to 230, under *2. Templates*. **All five lie in the cut**, so the fact the
tabulation rests on — no fenced block inside a range — holds, and no row moves; §6.35's manifest header names the five.
It is recorded because a fact relayed as established was not complete (#3), and the writing side's search is where the
difference lies; nothing here says why.

**Observations, recorded for the writing side and not acted on:**

1. **The placements and readings stated for challenge** at §6.35's manifest header — the eight placements (a) to (h),
   and the one departure from the former-wording precedent at Row 35.119 — each with its alternative.
2. **The passage rule's cut at position 35 is recorded, not repaired**: the document's lines in no range, as spans, with
   the headings among them and every home of the decisions register's data file that lies there, LIVE, DEFERRED or
   RETIRED, named at the manifest header; the homes walk above prints them.
3. **Reserved words in earlier members' text** stand as the dispatch carries them — §6.1 to §6.34 are frozen.
4. **The classification tool's message still names four tools without an authored verdict**, unchanged.
5. **Position 36's size**, stated at the head of this report for the next dispatch.

## 6. Declared departures

1. **The derivation's heading search came before its §5 was read** [2] — a read of the derivation itself, so nothing else
   was read before the derivation; the first tool call was the dispatch's first page alone, as ordered.
2. **Injected context at boot**: `CLAUDE.md`, the auto-memory index and a git status snapshot reached the context before
   any tool call. **`CLAUDE.md` was not re-read through a tool**; its six session-start spans were in the injected text.
3. **Position 36's entry with its ranges came back in one read** at item (9) [53], where only its `lines` and `bytes`
   were ordered. Nothing of position 36 was quoted, counted or placed. At the close, searches of the scratch copy of the
   artifact read position 36's entry head (its position, hit count and first withheld identities) and the `lines` and
   `bytes` of every member, to check the sizes stated at the head of this report.
4. **Item (10) was not read in full**: §6.28 at three portions rather than whole (its lines 34172 to 34514 and 34645 to
   34839 not read); the manifest headers of §6.7, §6.15, §6.16 and §6.19 not read — a search for *blockquote-marker
   reading* located that reading's statements instead; and §10 to §12 not read whole (§0, item 13). The member's §10,
   §11 and §12 entries were written at those sections' ends and checked by the recheck script against the member's rows
   in both directions.
5. **The reading file's new content was written into the repository by `cp`** [201] from the scratch splice, where a
   file-tool write is the practice; the smaller edits that followed were made with the file tools' Edit [203 to 214]. The
   copied file was then written as a blob and every check ran on that blob's scratch copy.
6. **The session's context was summarized once**, after the forward bound's five edits and before its `--apply`. What this
   report states of the work before the summary is taken from the transcript and the scratch files (§7). **And a pause**
   fell before this report was assembled, the user's *"resume"* continuing the same context; the close commit and the
   end state are therefore dated 2026-10-23, while every `STATUS.md` entry and the forward bound's `ACT_DATE` carry
   2026-10-21, the day those acts ran.
7. **A branch-tip read after each commit** (`git log -1`) to learn the new commit's identifier, verified each time at the
   commit's own object and at the ref file.
8. **Shell loops over named PATHS** (0(c)'s per-path checks) **and over tool NAMES** (2(c)'s checks), each hash inside
   them written literally; **shell variables naming the scratch folder** (`S=…`, `P=…`) **and the member's range and cut
   lists** (`R35=…`, `C35=…`), never holding a hash.
9. **One shell command was refused by the read guard** at 2(b) [240]: it chained a `wc` of two scratch files named
   through a shell variable onto the `--apply` and `--check`; the guard stopped the whole command before anything ran, and
   it was run again without the `wc` [241], the outputs read with the file tools.
10. **Scratch scripts run with `python -I -X utf8`**, outside the repository, edited with the file tools; `t2_dedupe.py`
    reads the session's own transcript file, which lies outside the repository.
11. **The co-author trailer** as a second paragraph of each commit message, the subject line exactly the ordered one.
12. **Every change made to the scratch scripts, those for a document other than `ARCHITECTURE.md` named first** (§7).
13. **This report was assembled by a scratch script** (`t2_report.py`) that splices the scratch files and the
    transcript's tool results into it verbatim, then copied into the repository with `cp`; it was read back with the
    file tools before staging.

## 7. The scripts, and the limits they met

All in the session's scratch folder, outside the repository, reading git objects only through scratch copies taken by
explicit hash. **The previous batch's scripts, copied from its session folder and changed for `docs/scoring_model.md`:**

- `t1_ranges.py` — repointed at the population artifact's copy `l3pop_13d1750b.json` and at the document's copy
  `sm_8410b00e.md` through a map from document path to copy, `ARCHITECTURE.md` not read; it prints the document's line
  count and whether it ends with a newline; and **for the label *the passages of the document* it takes the whole
  document as the section**, lines 1 to the last, the empty string after the last line break not counted as a line.
- `t1_inside.py` — **rewritten**: for a member made of a whole document's passages it lists every other member of the
  artifact whose document is the same, with their ranges overlapping the given lines, where the earlier form listed
  `ARCHITECTURE.md` members overlapping a section.
- `t1_homes.py` — repointed at the decisions data file's copy `backbone_9f34b0ca.json`, which it walks for any document
  path given; unchanged otherwise.
- `t1_dump.py` — repointed at the two copies through the same document map.
- `t1_manifest_ranges.py` — repointed at the artifact's copy.
- `t1_member.py` — repointed at `sm_8410b00e.md`, and **the member text is also taken with every hyphen at a line end
  joined to the next line, a quotation accepted if found in either form**, each join printed.
- `t1_words.py` — repointed at `sm_8410b00e.md`, and **the member text it masks quotations against has the `> ` marker
  removed at each line start**, as `t1_member.py` masks it.
- `run_checks_m.py` — its scratch-folder path changed. `t1_recheck.py` — unchanged.
- `t0_lastbytes.py` — its two paths and blobs replaced.

**New this batch:** `gen35_lib.py` (the quotation taker — each quotation taken from the blob's own lines at its locator,
the marker dropped, indentation stripped, the hyphen joined and spaces collapsed, a whole table row taken as one unit —
and the line wrapper, which keeps protected phrases and code spans of up to forty characters whole and avoids a line
opening with a list or heading marker), `gen35_rows_a.py` and `gen35_rows_b.py` (the row specifications), `gen35.py` and
`gen35_head.py` (the rows, the *not a statement* list, the §11 block, the distribution, the manifest header and the
foot), `splice35.py` (the splice into the scratch copy of the reading file); at the close, `t2_dedupe.py` (the transcript
rendered once per tool call, by its identifier, with input and result — the transcript file holds some assistant
messages twice, so the earlier rendering scripts `t2_extract.py` and `t2_calls.py`, copied from the previous batch and
run first, printed those calls twice) and `t2_report.py` (this report's verbatim blocks spliced in). `t3_span.py` and
`t3_compare.py` are used at the end state, as the previous batch's.

**The limits met, recorded as the previous reports recorded theirs:**

- **The word check's quotation mask has a line limit**: at Row 35.102 the member's own words *score cannot reliably
  distinguish*, inside a quotation running over several lines, were reported as if they were this session's; read by
  hand at the blob, they are the member's.
- **The table-header limit did not bite**: each of the three table header rows was listed with the row itself quoted as
  the item's opening, and the word check found every opening (*"openings not found: 0"*).
- **The fenced-block limit had no instance**: no range holds a fenced block.
- **The member check stopped once on a charter name it could not parse** (the generator's wrapping fault named at §2),
  and ran clean after the generator was corrected.
- **The quoted words of derived statements inside the *difference* sentence** — the one at Row 35.154 — and inside the
  AGREES remarks are not checked by the script and were held to the derivation's lines by hand.

## 8. What this batch did not do

No decision on any disposition, difference, open question, the derivation or the method; no verdict on the deriving
session's independence; no session booted; no measurement of the analysis built or run. No edit to the derivation, the
brief, the pack or its artifact, the two input-contract files, the L0/L1 or the L2 reading file, any outgoing text
(`docs/scoring_model.md` above all, and `ARCHITECTURE.md`), any governing document other than `STATUS.md` and
`STATUS_ARCHIVE.md`, any source of the decisions register, or §6.1 to §6.34 of the reading file. No tool source touched
but `gen_status_batch_bound.py`'s authored aiming; no guard enrolment; no freeze of the L3 pack; no member split by
hand; `gen_l2_outgoing_population.py` never run; `gen_l3_outgoing_population.py` run in `--check` operating mode only.
No finding number, no open-items row, no `src/` change, no golden, no test, nothing under `tools/corpus/`,
`tools/robust_stop/` or `tools/dcml/`, no decisions-register entry and no `D-NNN`. No residue file or LISTED item-2
document dispositioned; no ruling taken; nothing put to the user. No repair of the passage rule's cuts; no correction of
the previous report. No member beyond position 35.

## 9. The plan's tell, in one sentence

**This batch produced nothing other than the landed records, the reading file's new member subsection with its updates
to §0 and §10 to §13 (and the one banner edit and the §0 clause on the previous batch's stop), the Task 2 files and this
report — and, outside the repository, the capacity-judgment file, the scratch scripts and their outputs.**

## 10. Self-check (D-434) — the standing check over this batch's own work

The diff of every touched file was read against the principles, the conventions and the gate and threshold policies:

- **#1, #12, #15** — every quotation of an outgoing statement checked at the objects against the member's text, every
  disposition tallied against its foot, coverage of §10 to §12 checked both ways; the readings stated for challenge are
  recorded at the manifest header rather than dropped.
- **#3, #13** — the one fact of the premise ledger found incomplete (the fifth fenced block) is surfaced at §5 and not
  absorbed; it moves no row, so it is not a STOP of the tabulation.
- **#6, #10, D-431** — no count restated in `STATUS.md` or in the close section; the member's counts live at its manifest
  header and at §13, and this report repeats them in its member paragraph and inside the outputs the dispatch orders
  verbatim.
- **#19** — the forward bound's move was proved at its artifact (`the_moved`), not at its green `--check`.
- **The reserved-word convention** — this session's wording scanned at the member with the quotations masked, every word
  the scan reports read by hand; the `STATUS.md` entries searched for the 26 ruled terms, with the one standing hit.
- **Never work from memory** — the work before the summary is reported from the transcript and the scratch files, and the
  readings stated for challenge from the committed blob's manifest header, not from the summary.
- **The self-check after every coding exercise** — the scratch scripts touched no repository file but the reading file's
  copy and this report's; the reading file's diff at the member commit was checked by the three checks above;
  `gen_status_batch_bound.py`'s diff touches only its authored aiming and head comments.
