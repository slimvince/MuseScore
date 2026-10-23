# CC report — the L3 comparison continued at position 36: position 36 tabulated, proposals only — NOTHING DECIDED, NO ALGORITHM CHANGE, NO DECISIONS-REGISTER ENTRY

*Executing `records/cc/instructions/cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md` (pinned at Task 0
to blob `596fb568bdcecec465b48e1ee46beadd430fa6aa`, 187,338 bytes). Written 2026-10-23 by Claude Code. This report
decides nothing: every disposition in the reading file is a proposal for the user's later ruling, and no recommendation
is made here about any disposition, any difference, any open question, the derivation or the method.*

**★ THE SESSION'S CONTEXT WAS SUMMARIZED ONCE, INSIDE TASK 1, AND NO COMMITTED ACT FELL ACROSS IT.** The summary fell
between the session's calls 178 and 179 (the call numbers of the scratch script `t2_dedupe.py`, §7): after the first
half of position 36's rows had been written to scratch files and before the second half was. The Task 0 commit, the
opening capture, the capacity-judgment file and every Task 1 input check were made before it; the second half of the
rows, the member's manifest header and foot, the splice, the three checks, the member commit and all of Task 2 were made
after it. **What this report states of the work before the summary is taken from the session's own transcript** —
rendered by `t2_dedupe.py`, which prints each tool call once with its input and its result — **and from the scratch
files, never from the summary's wording.** The capacity-judgment file was written before the summary, so its sentence
*"its context has not been summarized"* was true when it was written.

## The member done and not done

- **Done:** position **36** — `cowork_phrase_boundary_design.md`, *the passages of the document* — §6.36 of the reading
  file, in its own commit (§2).
- **The stop:** at the member boundary after position 36, **under this dispatch's 1(g)** — position 36 alone, then Task
  2 — and **not** by a capacity judgment.
- **Not done:** positions 37 to 57, **UNTOUCHED** — not read for tabulation, not quoted, not counted and not placed
  (**D-672**). §0 of the reading file says so.
- **The next writing resumes at position 37.**
- §7, §8, §9 and §14's relay stay NOT YET WRITTEN; position 57 is not done.

**The capacity judgment, as 1(h) orders it — written to its file in the session's scratch folder, outside the
repository, with the file tools, BEFORE the member's lines were opened at the document, and quoted here whole.** The
transcript shows the write of `capacity_judgment_36.txt` at its call 135; the first act that read any line of the member
at the document — the ranges check, which compares each range's two line texts with the lines at its locators — is call
141, and the member's lines were first read whole at call 162 (`m36_dump.txt`). Calls 136 and 137 between them read four
blobs' identities and copied them into scratch files; neither printed a line of the document. The judgment was *"I can
finish this member whole"*, and the member was finished whole; the first-member rule did not fire.

*`capacity_judgment_36.txt`:*

```
Capacity judgment before position 36, written before any line of the member was opened at the document.

Position: 36 — cowork_phrase_boundary_design.md, "the passages of the document".
At the artifact (tools/audit/l3_outgoing_population.json, read at its entry): lines 361, bytes 39,176, ranges 22,
item_3_hit_lines_inside 82, item_4_identities_inside seven (D-476, D-477, D-478, D-479, D-480, D-481, D-485).

Judgment: I can finish this member whole. It is smaller on both sizes than position 35 (480 lines, 45,088 bytes),
which a fresh session finished whole; its twenty-two ranges hold one quotation-block banner, one terms table, one
glossary, fourteen ranges opening with a heading line and no fenced block, each named by the dispatch, and seven
WITHHELD homes and two SEEN homes whose rows must carry their marks. This session has done its ordered reads and
Task 0, and its context has not been summarized. The member's rows, its updates to sections 0 and 10 to 13 and the
three checks before the commit fit in what remains, with room for the close, the report and the end state. It is the
batch's only member (the dispatch's 1(g)); after it the batch stops and goes to Task 2.
```

**The next member's size, as 1(h) asks of a stop.** Position 37 is **472 lines and 47,074 bytes** at the artifact, as
the dispatch states it and as this session's read of the artifact at call 59 showed it (§6, departure 2), with
twenty-one ranges and its `item_4_identities_inside` empty. That is larger in bytes than any passage member done so far
— position 35's 45,088 was the largest — and smaller in lines than position 35's 480. **Position 36 is the measured
case that bears on it:** at 39,176 bytes it was finished whole, but this session's context was summarized once during
it (above), which no earlier report of a member this size records. So the next member's size gives **some reason to
doubt** that a fresh session finishes it whole without a summary of its context; it gives no reason to judge it cannot
be finished whole. The judgment is the next session's, under its own 1(h).

## 0. The ordered first read

The opening instruction named only this dispatch. **The session's first tool calls were THREE reads made together:
the dispatch's first page (its lines 1 to 552), `STATUS.md` whole and `DECISIONS.md` (its lines 1 to 362)** [1, 2, 3] —
against the ordered first read, which puts the derivation first after the dispatch's first page (§6, departure 1).
Before any tool call, `CLAUDE.md`, the auto-memory index and a git status snapshot reached the context at boot as
injected context. The order thereafter, as the transcript records it (call numbers in brackets):

1. `cowork_blind_derivation_l3_2026_10_17.md`: its heading list by a search [4]; then **§5, §6 and §7** in one read,
   from its line 1269 to the end [5]; then the whole file from line 1 in three reads (1 to 520, 520 to 919, 919 to
   1268) [6, 7, 8]. **§5 first, then §6, then §7, then whole.**
2. **The derivation's counts, taken AT this read** by two searches made immediately after the whole read and before
   anything else was opened: `^\*\*L3-S\d+\. ` counted **42** [9], and `^- \*\*OQ-L3-\d+ ` counted **14** [10]. They
   agree with the reading file's manifest; no STOP.
3. The remainder of this dispatch, whole (its lines 553 to the end, three reads) [11, 12, 13].
4. **(1)** `CLAUDE.md` injected at boot; `STATUS.md` whole [2]; `DECISIONS.md` whole [3, 15, 16] (call 14, a read of
   500 lines from line 363, returned nothing usable and was redone as two reads of 250); rule (a)'s `gating_ids` at
   `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`, located by a search and read [17, 20, 21];
   `BUILD_AND_TEST.md` — the condition met, this batch runs the guard set — located by two searches and read whole
   [18, 19, 22].
5. **(2)** `cowork_audit_protocol.md` from its line 180 to the end, three reads [23 to 26].
6. **(3)** The two L3 rulings whole [27, 28]; the L2 named-documents ruling whole [29]; the comparison-design sitting
   whole [30]; §3am to §3ao of the 2026-08-31 decision-surface sitting, located by a search [31, 32].
7. **(4)** The phase definition's §0 and §3.4 [33, 34, 35].
8. **(5)** `FRAMEWORK.md` §5, located by a search and read [36, 37].
9. **(6)** The brief's §2, §4 and §7 [38, 39, 40].
10. **(7)** `tools/audit/derivation_boot_pack.json` → `subjects` → `l3` → `counted`, `THE_WITHHELD_FAMILY` and `LEAKS`
    (read; not regenerated) [41 to 44].
11. **(8)** Entries 438 and 439, located by a file search [45, 55, 56]; the previous dispatch whole (four reads) [46 to
    50]; the previous report whole (four reads) [51 to 54].
12. **(9)** `tools/audit/l3_outgoing_population.json` → the passage rule, the order, `item_2_listed_not_compared_whole`,
    `the_named_documents_derivation` and the members' entries, located by a search [57] and read at its lines 33025
    to 33064 [58], 35060 to 35399 [59] and 32755 to 32884 [60]. **The read at 35060 took in position 37's entry with
    its ranges, where only its `lines` and `bytes` were ordered** (§6, departure 2).
13. **(10)** The reading file at the portions the dispatch names: its heading structure [61]; the banner and §0 to the
    paragraph under `## 6.` stating the two reading rules [62, 63]; §6.35's manifest header and its first rows [64, 65,
    66]; the marked title lines of Rows 2.8, 2.9, 2.16, 7.226 to 7.229 and 20.45 to 20.49, located by a search [67,
    68, 69]; the precedent rows 1(a)'s point (b) names, located by a search and read at their blocks [70 to 79, 95];
    §6.10's manifest header [80]; three further precedent blocks [81 to 85]; §6.21's manifest header [86]; **§10 to §13
    at their member-35 ends, with searches locating each charter block's end and each member block's head** [87 to
    94]; and the heading-line and blockquote-marker readings, located by a search [96, 97, 98]. **Not read as
    ordered:** §11 and §12 whole (only their member-35 ends and the blocks of members 19, 20, 34 and 35 were read), and
    the manifest headers of §6.16 and §6.7 — §6, departure 4. The member's §10, §11 and §12 entries were written at
    those sections' ends, and the recheck script compares all three with the member's rows in both directions (§2).
14. **(11)** Not read — positions 56 and 57 were not reached.
15. **(12)** The outgoing text was opened as Task 1 orders — the member's lines inside its published ranges, read from a
    scratch copy of `cowork_phrase_boundary_design.md`'s blob at the Task 0 commit (§2); this session also read the
    document's cut lines from that copy (§2).

## 1. Task 0 — the pin, the refs, A1, the last bytes, the commit, the opening capture, the two blobs

**0(a) — the pin.** `git hash-object -w` of this dispatch [102]:

```
warning: in the working copy of 'records/cc/instructions/cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md', LF will be replaced by CRLF the next time Git touches it
596fb568bdcecec465b48e1ee46beadd430fa6aa
exit:0
```

then `git cat-file -s` of that blob, `git hash-object -w --no-filters` of entry 438 and of this dispatch [103]:

```
187338
exit:0
40d14a973645d8328a9494049296a0261afeab12
exit:0
596fb568bdcecec465b48e1ee46beadd430fa6aa
exit:0
```

**Proved unmoved immediately before staging** [126]: `596fb568bdcecec465b48e1ee46beadd430fa6aa`, the same blob.

**0(b) — the refs**, read with the file tools [104, 105]: `.git/refs/heads/master` and `.git/refs/remotes/origin/master`
each `619fb8ef679b9dd811a18dd57ecffd27100c8e2c`, as the FACT names. The chain, five commands, each hash written
literally [106 to 110], each into a scratch file read with the file tools:

```
commit 619fb8ef679b9dd811a18dd57ecffd27100c8e2c
parent 1efab7f6215e8eafdbfadd854d3930c57f51c95d
subject End state: the L3 comparison continued at position 35 - guard run at the close tree, the A2 regenerations already met inside the close

 records/cowork/handoff/cowork_away_returns.md | 73 +++++++++++++++++++++++++++
 tools/audit/guard_state.json                  | 12 ++---
 2 files changed, 79 insertions(+), 6 deletions(-)
```

```
commit 1efab7f6215e8eafdbfadd854d3930c57f51c95d
parent 5d9f356a0e5f7d11ae5e63a270d7be1537aaac37
subject Close: the L3 comparison continued at position 35, under its dispatch

 STATUS.md                                          |    6 +-
 STATUS_ARCHIVE.md                                  |    8 +
 ..._comparison_tabulation_thirteenth_2026_10_21.md | 1757 ++++++++++++++++++++
 records/cowork/handoff/cowork_away_returns.md      |   78 +
 tools/audit/defense_share.json                     |    2 +-
 tools/audit/gen_status_batch_bound.py              |   55 +-
 tools/audit/session_start_read_size.json           |   16 +-
 tools/audit/status_batch_bound.json                |   32 +-
 8 files changed, 1924 insertions(+), 30 deletions(-)
```

```
commit 5d9f356a0e5f7d11ae5e63a270d7be1537aaac37
parent d1b3a26f577c8034b56ac909de3946564cffe243
subject comparison L3: member 35 tabulated - 197 outgoing statements placed, proposals only

 .../cowork_comparison_l3_reading.md                | 3563 +++++++++++++++++++-
 1 file changed, 3548 insertions(+), 15 deletions(-)
```

```
commit d1b3a26f577c8034b56ac909de3946564cffe243
parent 06b17b46d480bbbd2d7fd0ebe67fe57270d627be
subject record: entry 437 and the thirteenth l3 comparison tabulation dispatch

 ..._comparison_tabulation_thirteenth_2026_10_21.md | 1685 ++++++++++++++++++++
 ..._handoff_entry_four_hundred_and_thirty_seven.md |   98 ++
 2 files changed, 1783 insertions(+)
```

```
commit 06b17b46d480bbbd2d7fd0ebe67fe57270d627be
parent 75bbfa9326db01819b7036f660b71bc1c388365b
subject End state: the L3 comparison continued from position 27 - guard run at the close tree, the A2 regenerations already met inside the close

 records/cowork/handoff/cowork_away_returns.md | 71 +++++++++++++++++++++++++++
 tools/audit/guard_state.json                  | 12 ++---
 2 files changed, 77 insertions(+), 6 deletions(-)
```

The chain is the one the FACT relays: the previous batch's four commits — its Task 0, its member commit, its close and
its end state — above the twelfth batch's end state.

**0(c) — A1's check.** `python tools/audit/changed_paths.py` over the whole tracked population [116], into a scratch
file read with the file tools; its tracked and repository-level lines, and its count line (the 385 lines under
`scratch_artifacts/` between them are not reproduced here, every one of them `??` and under that folder):

```
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_eight.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_nine.md
...
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
397 changed path record(s) [worktree]
```

Per named untracked path, `git ls-files --others --exclude-standard`, and per tracked input this batch edits, `git diff
--stat 619fb8ef… -- <path>` [121]:

```
records/cc/instructions/cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md
exit:0
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_eight.md
exit:0
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_nine.md
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

**A1 holds:** exactly one tracked modification, `tools/audit/claude_md_finer_archive.json`, carried; the two paths
Task 0 lands; entry 439, untracked and NOT landed, as A1 names it; the standing untracked population; every edited
input empty against `619fb8ef…`. No other untracked path under `records/`, `reading_pass/` or `ratification_surfaces/`
or at the repository's top level.

**0(d) — the last bytes**, by `t0_lastbytes.py` (§7) at each blob [124]:

```
== records/cc/instructions/cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md
   blob 596fb568bdcecec465b48e1ee46beadd430fa6aa  size 187338
   zero bytes: 0
   ends with a newline: True
   last non-empty line: a commit set or an algorithm; none is a question for the user. **Banner set to RELEASED.**
   last 70 bytes: b'gorithm; none is a question for the user. **Banner set to RELEASED.**\n'
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_eight.md
   blob 40d14a973645d8328a9494049296a0261afeab12  size 7585
   zero bytes: 0
   ends with a newline: True
   last non-empty line: instruction; "continue".*
   last 70 bytes: b'on entry 437. The user\'s words: the opening\ninstruction; "continue".*\n'
```

Entry 438 exists, 7,585 bytes; neither file is broken off, neither carries a zero byte.

**0(e) — the commit.** Staged by explicit path, the staged set proved [126]:

```
596fb568bdcecec465b48e1ee46beadd430fa6aa
exit:0
warning: in the working copy of 'records/cc/instructions/cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_eight.md', LF will be replaced by CRLF the next time Git touches it
exit:0
A	records/cc/instructions/cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_thirty_eight.md
2 changed path record(s) [staged]
exit:0
```

The commit [127]:

```
exit:0
69e0afc218c62ae19847f4dd820b7118cdefd573 619fb8ef679b9dd811a18dd57ecffd27100c8e2c record: entry 438 and the fourteenth l3 comparison tabulation dispatch
exit:0
```

Its stat, the two blobs at it, and the push [128]:

```
69e0afc218c62ae19847f4dd820b7118cdefd573 619fb8ef679b9dd811a18dd57ecffd27100c8e2c
record: entry 438 and the fourteenth l3 comparison tabulation dispatch

 ..._comparison_tabulation_fourteenth_2026_10_23.md | 1800 ++++++++++++++++++++
 ..._handoff_entry_four_hundred_and_thirty_eight.md |   89 +
 2 files changed, 1889 insertions(+)
exit:0
596fb568bdcecec465b48e1ee46beadd430fa6aa
40d14a973645d8328a9494049296a0261afeab12
exit:0
To https://github.com/slimvince/MuseScore
   619fb8ef67..69e0afc218  master -> master
exit:0
```

`.git/refs/remotes/origin/master` read with the file tools [129]: `69e0afc218c62ae19847f4dd820b7118cdefd573`.

**0(f) — the opening capture**, `python tools/audit/gen_guard_state.py --check` (the read-only operating mode, named)
[130], exit 0, every verdict:

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

**Against A2:** the header met is *"the guard state re-derives"* (exit 0); the thirteen FAIL lines are exactly the
thirteen the FACT names; `gen_evidence_pin_membership.py --check` and `gen_l3_outgoing_population.py --check` PASS;
run 82; zero STOPs. The committed artifact at `619fb8ef…`, read from its object into a scratch file [132, 134]: `run`
82, `passing` 69, `failing` 13, `not_run` 4, `historical_records` 20. **`gen_guard_classification.py --check`** [132],
exit 2, the STOP naming exactly the four tools of the FACT:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_withheld_family_reading.py']
```

**0(g) — the two blobs** [132]: `git hash-object` of the derivation and of the brief, and `git cat-file -s` of each blob:

```
c01793f98c51e0267fb0dc7487613ac477cc1fbb
6abb53333fd248ee15a983c6ece4cbfe38a376a0
exit:0
127533
39251
exit:0
```

— the blobs and sizes A5's first line names.

**E0 — MET:** the two named paths in one commit; `origin/master` at it; the pin proved; A1 reported with its
enumeration; the opening capture against A2; the two blobs verified.

## 2. Task 1 — the tabulation, position 36

### The inputs, at their objects

The four objects at the Task 0 commit, and the two working copies [136]:

```
3413a9edd47d231db37c7dadfa196ee6089d6c28
fff5cd075c4c218eb1e86a4e567f25b83eec67c5
13d1750be95ecdcf408405ff7d6f67bba8db1dfe
9f34b0cab42c2fc69d3af8613ac3e0a9237d6b03
exit:0
3413a9edd47d231db37c7dadfa196ee6089d6c28
fff5cd075c4c218eb1e86a4e567f25b83eec67c5
exit:0
```

— `cowork_phrase_boundary_design.md`, the reading file, `tools/audit/l3_outgoing_population.json` and
`tools/audit/decisions/backbone_decisions.json`, in that order. Each blob was copied to a scratch file by explicit hash
[137], and every script below reads those copies (`pb_3413a9ed.md`, `rf_fff5cd07.md`, `l3pop_13d1750b.json`,
`backbone_9f34b0ca.json`).

**The ranges check** (`t1_ranges.py 36`) [141], whole:

```
document: cowork_phrase_boundary_design.md | lines in the split: 414 | ends with a newline: True
kind: items 3 and 4 — passages of a specification-set member | label: the passages of the document | lines 361 | bytes 39176 | hits 82 | item-4 [{'identity': 'D-476', 'home_as_cited': 'cowork_phrase_boundary_design.md:250-253'}, {'identity': 'D-477', 'home_as_cited': 'cowork_phrase_boundary_design.md:64-69'}, {'identity': 'D-478', 'home_as_cited': 'cowork_phrase_boundary_design.md:260-265'}, {'identity': 'D-479', 'home_as_cited': 'cowork_phrase_boundary_design.md:266-272'}, {'identity': 'D-480', 'home_as_cited': 'cowork_phrase_boundary_design.md:303-309'}, {'identity': 'D-481', 'home_as_cited': 'cowork_phrase_boundary_design.md:188-193'}, {'identity': 'D-485', 'home_as_cited': 'cowork_phrase_boundary_design.md:205-218'}]
range 1 1-21 first matches: True  last matches: True  marker lines: 19  of 21
range 2 37-46 first matches: True  last matches: True  marker lines: 0  of 10
range 3 48-61 first matches: True  last matches: True  marker lines: 0  of 14
range 4 63-94 first matches: True  last matches: True  marker lines: 0  of 32
range 5 96-105 first matches: True  last matches: True  marker lines: 0  of 10
range 6 107-110 first matches: True  last matches: True  marker lines: 0  of 4
range 7 112-113 first matches: True  last matches: True  marker lines: 0  of 2
range 8 126-134 first matches: True  last matches: True  marker lines: 0  of 9
range 9 136-139 first matches: True  last matches: True  marker lines: 0  of 4
range 10 141-164 first matches: True  last matches: True  marker lines: 0  of 24
range 11 172-180 first matches: True  last matches: True  marker lines: 0  of 9
range 12 182-185 first matches: True  last matches: True  marker lines: 0  of 4
range 13 187-203 first matches: True  last matches: True  marker lines: 0  of 17
range 14 205-218 first matches: True  last matches: True  marker lines: 0  of 14
range 15 220-228 first matches: True  last matches: True  marker lines: 0  of 9
range 16 230-247 first matches: True  last matches: True  marker lines: 0  of 18
range 17 249-275 first matches: True  last matches: True  marker lines: 0  of 27
range 18 277-291 first matches: True  last matches: True  marker lines: 0  of 15
range 19 293-309 first matches: True  last matches: True  marker lines: 0  of 17
range 20 311-357 first matches: True  last matches: True  marker lines: 0  of 47
range 21 359-368 first matches: True  last matches: True  marker lines: 0  of 10
range 22 370-413 first matches: True  last matches: True  marker lines: 0  of 44
ranges: 22  all 2x22 boundary texts match: True
lines in ranges: 361  bytes (each line with its newline): 39176
section: the whole document, lines 1 to 413 (its last line '     built until the inference phase opens; validate on a non-chorale corpus (§8).')
lines of the section outside every range: 52 (26 blank, 26 not blank)
cut spans: 22-36 47 62 95 106 111 114-125 135 140 165-171 181 186 204 219 229 248 276 292 310 358 369
headings in the cut:
  33: ## 0. Terms (read first — nothing below uses a term before its row)
  115: ## 4. The model (the rules)
  119: ### 4.1 The surface-cue core (a local-change boundary-strength model)
  166: ### 4.3 Per-voice cues, aggregated to the texture (polyphony)
headings inside the ranges:
  1: # Phrase-boundary primitive (Architectural Layer 1.5) — Architecture & Design
  48: ## 1. Purpose
  63: ## 2. Constraints
  96: ## 3. Context & scope (external view)
  141: ### 4.2 The deterministic notated-marker spikes
  187: ### 4.4 Peak-picking
  220: ### 4.5 Explicitly excluded
  230: ## 5. Runtime view (scenarios)
  249: ## 6. Architecture decisions (with the alternatives weighed)
  277: ## 7. Quality & testing
  293: ## 8. Risks & technical debt
  311: ## 9. Glossary
  359: ## 10. Background: what this replaces, and the as-built map (not needed to understand the primitive)
  370: ## 11. Open items
fence lines in the document: []
marker lines in the document: 3-21 23-31
lines ending in a hyphen: [(231, True, '/long-note gives a strong gap-'), (239, True, 'e (low-weighted, noisy) pitch-')]
```

All forty-four line texts match; the cut is the dispatch's span for span; no fenced block; the marker at lines 3 to 21
and 23 to 31 only; two hyphen line ends, both in range 16.

**The inside control and the two walks of the decisions register's data file** [156]:

```
member 36 document: cowork_phrase_boundary_design.md
members of the artifact with that document: [36]
cowork_phrase_boundary_design.md members other than 36: 0; their ranges overlapping 1 413: 0
```

```
D-476 | cowork_phrase_boundary_design.md:250-253 | live | /decisions | range [(249, 275)] | wholly inside a range: True
D-477 | cowork_phrase_boundary_design.md:64-69 | live | /decisions | range [(63, 94)] | wholly inside a range: True
D-478 | cowork_phrase_boundary_design.md:260-265 | live | /decisions | range [(249, 275)] | wholly inside a range: True
D-479 | cowork_phrase_boundary_design.md:266-272 | live | /decisions | range [(249, 275)] | wholly inside a range: True
D-480 | cowork_phrase_boundary_design.md:303-309 | live | /decisions | range [(293, 309)] | wholly inside a range: True
D-481 | cowork_phrase_boundary_design.md:188-193 | live | /decisions | range [(187, 203)] | wholly inside a range: True
D-482 | cowork_phrase_boundary_design.md:254-256 | live | /decisions | range [(249, 275)] | wholly inside a range: True
D-483 | cowork_phrase_boundary_design.md:281-285 | live | /decisions | range [(277, 291)] | wholly inside a range: True
D-484 | cowork_phrase_boundary_design.md:83-94 | live | /decisions | range [(63, 94)] | wholly inside a range: True
D-485 | cowork_phrase_boundary_design.md:205-218 | live | /decisions | range [(205, 218)] | wholly inside a range: True
homes naming cowork_phrase_boundary_design.md with a line number: 10
identities overlapping the 22 ranges given: 10
```

and over the twenty-one cut spans:

```
homes naming cowork_phrase_boundary_design.md with a line number: 10
identities overlapping the 21 ranges given: 0
```

**As predicted:** exactly the ten the dispatch names inside the ranges, none in the cut. The decisions register's INDEX
rows for D-476 to D-485, read with a search [181]: all ten LIVE, ratified `2026-08-04 · user`, each homed at a section
of `cowork_phrase_boundary_design.md`; their group, read at the INDEX's group headings [205], is H.

### The rows, how they were written, and the three checks before the commit

The member's lines were read whole from the scratch copy [162, 183, 190], and the rows written as Python data in
`gen36_rows_a.py` and `gen36_rows_b.py`, every quotation taken from the copy by its line range and its first and last
words and never retyped (`gen36_lib.py`, §7). The words of the derived statements L3-S8, L3-S9, L3-S10, L3-S12,
L3-S14, L3-S16, L3-S33, L3-S38 and L3-S42 quoted in the rows were checked against the derivation after the context
summary [193]; the others quoted (L3-S15, L3-S23, L3-S32, L3-S39, L3-S40 and L3-S41) were written into the rows before
it, from the derivation's whole read, and were not re-checked after it. The
generator's output after the last change [326, its first step]:

```
rows 157 statements 237 hist {1: 90, 3: 13, 2: 54} not a statement 42
```

**The marks were checked two ways.** (1) The generator prints every row that carries a mark and every row that carries
the decisions register's remark without one; that list was compared by hand with the ten homes' line ranges and the
rows' locators: the twenty WITHHELD rows and the eight SEEN rows are exactly the rows whose quotations lie inside the
nine homes, and D-483's three rows carry the remark and no mark. (2) **Each WITHHELD row's quotation was held to its home's
verbatim span** at the artifact's item-4 record by `t1_held36.py` (§7) [235]:

```
item-4 records for the document: D-476 x1, D-477 x1, D-478 x1, D-479 x1, D-480 x1, D-481 x1, D-485 x1
36.17 D-477 held: True
36.18 D-477 held: True
36.19 D-477 held: True
36.60 D-481 held: True
36.66 D-485 held: True
36.67 D-485 held: True
36.68 D-485 held: True
36.69 D-485 held: True
36.70 D-485 held: True
36.71 D-485 held: True
36.85 D-476 held: True
36.86 D-476 held: True
36.91 D-478 held: True
36.92 D-478 held: True
36.93 D-478 held: True
36.94 D-479 held: True
36.95 D-479 held: True
36.96 D-479 held: True
36.111 D-480 held: True
36.112 D-480 held: True
rows not held: 0
```

The SEEN homes have no verbatim span at the artifact (they are not item-4 identities), so the SEEN rows' quotations
were held to the document by the member check below, as every quotation is.

**The three checks**, run by `run_checks_m.py` over the old reading file (`rf_fff5cd07.md`) and the new one
(`reading_new.md`): three runs. **The first** [291] reported, at the recheck, twelve bare row numbers in §10's
parentheses (a number standing without the claim label the RELOCATED list carries — *Row 36.17* for *Row 36.17 (i)*)
and one label of the foot's DIFFERS list wrapped onto the next line (*36.91* / *(i)*); its word scan showed this
session's own wording using *measure*, *part* (*takes part in*, *its part (a)*), *rest* (*the mark saying the rest*) and
*score* (as a verb, in Row 36.102's title) outside their musical sense. All were corrected in the scratch files and the
generator re-run: §10's parentheses now name each claim with its label, the foot's lists keep a number and its label on
one line, and the wording is *strength*, *included in*, *enters no override frame*, *its clause (a)*, *recording what
the session was not shown* and *to yield*. Row 36.156's audit question, which had read *"the same as Row 36.68."*, was
rewritten as a question of its own. **The second** [319] reported the Row 36.102 title alone; **the third** [326],
over the copy that was committed, reported nothing. Its member check, whole:

```
   join at a line ending: 'voice-rest/long-note gives a strong gap-'
   join at a line ending: 'es only the (low-weighted, noisy) pitch-'
member lines taken: 361  marker lines masked: 19
hyphen-at-line-end joins in the member: 2
rows parsed: 157  contiguous 1..n: True
rows: 157  statements (claims): 237  claims-per-row histogram: {1: 90, 3: 13, 2: 54}
```

then each disposition's statement list (identical to the foot's distribution table in the committed file), each
charter's relocated list, the verdict counts and the AGREES and DIFFERS lists, and:

```
quotations not found verbatim: 0
row lines opening with a list or heading marker: 0
```

Its recheck, whole:

```
(a) 6.1-6.35 span identical: True  lengths 1995526 1995526
    foot ADOPTED — carried: stated 26, listed 26
    foot ADOPTED — proposed: stated 3, listed 3
    foot RELOCATED: stated 125, listed 125
    foot QUARANTINED: stated 21, listed 21
    foot DISCARDED: stated 0, listed 0
    foot HISTORICAL: stated 18, listed 18
    foot UNPLACED: stated 44, listed 44
(b) section 10 vs RELOCATED: missing []  extra []
    section 11 vs QUARANTINED: missing []  extra []  entries 21
    section 12 proposals vs ADOPTED -- proposed: missing []  extra []
    section 12 DIFFERS lines vs the foot's DIFFERS: missing []  extra []  lines 47
(c) placeholders left: 0
(d) changed: # The COMPARISON — L3: the derived statements against the outgoing tex
(d) changed: ## 0. Progress — which members are done, and where this stops
(d) changed: ## 6. The tabulation, in the published order
(d) changed: ## 10. The TRANSFER LIST — every RELOCATED row, by target charter
(d) changed: ## 11. The AUDIT QUESTIONS — every QUARANTINED row
(d) changed: ## 12. The PROPOSALS — every ADOPTED — proposed row and every DIFFERS,
(d) changed: ## 13. The distribution so far, counted at this file's own rows
```

Its word scan: all forty-two *not a statement* openings found; every remaining hit of a reserved word, read by hand, is
inside a quotation of the member, inside the decisions register's name, or in its musical sense (*score* as the piece,
*key* as the tonality or the key signature, *bar*, *note*, *rest*, *part* in *per-part*, *interval* as a pitch
interval, *instrument*, *dynamic*).

### The commit

The copy placed in the working tree and its blob [330]:

```
exit:0
warning: in the working copy of 'ratification_surfaces/cowork_comparison_l3_reading.md', LF will be replaced by CRLF the next time Git touches it
b8763e6c1a0b8367afc71f0ba7086be359585911
exit:0
b8763e6c1a0b8367afc71f0ba7086be359585911
exit:0
```

— the working file's blob equals the checked scratch copy's. Staged and proved [332]:

```
M	ratification_surfaces/cowork_comparison_l3_reading.md
1 changed path record(s) [staged]
```

Committed [334] with the subject `comparison L3: member 36 tabulated - 237 outgoing statements placed, proposals
only`; `git log -1` [335]: `8f0baf80f15bdd7fccbbdab4f3d5e050bf282ab2`. At the commit, and the push [337]:

```
100644 blob b8763e6c1a0b8367afc71f0ba7086be359585911	ratification_surfaces/cowork_comparison_l3_reading.md
exit:0
8f0baf80f15bdd7fccbbdab4f3d5e050bf282ab2 69e0afc218c62ae19847f4dd820b7118cdefd573

 .../cowork_comparison_l3_reading.md                | 3656 +++++++++++++++++++-
 1 file changed, 3639 insertions(+), 17 deletions(-)
exit:0
To https://github.com/slimvince/MuseScore
   69e0afc218..8f0baf80f1  master -> master
exit:0
```

`.git/refs/remotes/origin/master`, read with the file tools: `8f0baf80f15bdd7fccbbdab4f3d5e050bf282ab2`.

### What the member's subsection carries

§6.36 carries the manifest header the dispatch's 1(f) lists — the ranges with their texts, the cut and what it holds,
the walks of the homes, the reading rules with the member's instances (the blockquote-marker reading at range 1's lines
3 to 21 only; the fenced-block reading with no instance; the heading-line reading at fourteen ranges; the glossary
reading at range 20 and range 2's terms table read under it, its header row listed with its separator line; the
quotation join at lines 231 and 239; range 13's superseded phrase listed as provenance; range 1's revision record), and
a paragraph on what the member is and how its subjects were placed, **including how the split DP-I records was weighed
between the notated evidence and the phrase reading, and the precedents 1(a)'s point (b) names**, with four placements
stated for challenge, each with its alternative. Then the 157 rows, and the foot's five sections. **The counts are
stated there and at §13, and nowhere else** — this report does not restate them beyond the check outputs quoted above.
§0, the banner, §10, §11, §12 and §13 were updated in the same commit; §0's clause on the previous batch's stop reads,
in the words 1(f) gives: *"position 35 was tabulated under
`records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md`, which stopped at the member
boundary after position 35 under its own limit on the batch, and not by a capacity judgment; position 36 was tabulated
under `records/cc/instructions/cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md`."*

**E1 — MET:** the manifest; every outgoing statement with exactly one disposition or UNPLACED with what was read;
every DIFFERS with its one-sentence difference and nothing chosen; every row inside the seven WITHHELD homes marked
WITHHELD with its identity, every row inside D-482's and D-484's homes marked SEEN, no other row marked, D-483's home
named beside its rows; the transfer list, audit questions and proposals gathered; §0 true of the file with the previous
batch's stop in 1(f)'s words; the capacity file written before the member was opened and quoted above; no member beyond
position 36; no recommendation anywhere; §6.1 to §6.35 identical (the recheck's (a), and A5 at §4).

## 3. Task 2 — the close

**2(a) — the `STATUS.md` entries, first.** Three entries at the top, written with the file tools' Edit: the close
entry, naming this dispatch by its file name and carrying the moved `Last updated: ` prefix, then the entries for Task 1
and Task 0, each saying `Same dispatch`, all three pointers to this report with no count restated. The prefix was
removed from the thirteenth tabulation batch's close entry; no other existing sentence was rewritten or removed. **A
case-insensitive substring search of `STATUS.md` for all 26 ruled terms, run after the entries were written, hit one
line only**:

```
26:phrase
```

— the standing *ARCHIVED 2026-08-17, THE SECOND ACT* paragraph, where `phrase` matches inside *paraphrase*, at line 26
before the move. Run again after the move, the same line, at line 20:

```
20:phrase
```

No entry was corrected after the move.

**2(b) — the forward bound.** Read at the object `619fb8ef…:tools/audit/gen_status_batch_bound.py`, redirected to a
scratch file outside the repository and read there at its authored-aiming region (the five constants with their head
comments, `PREVIOUS_AIMINGS` whole, and the move's functions); the object's blob and the working copy's, then the
`STATUS.md` blob at `619fb8ef…`, at the Task 0 commit and at the member commit [346]:

```
exit:0
f232be5e51d5c2f9120986a7213657abe85d041d
f232be5e51d5c2f9120986a7213657abe85d041d
exit:0
32823dcb36a3507267bab376c1b11a023e079abf
32823dcb36a3507267bab376c1b11a023e079abf
32823dcb36a3507267bab376c1b11a023e079abf
exit:0
```

**All five authored constants were aimed:** `BASE_COMMIT` to `8f0baf80f15bdd7fccbbdab4f3d5e050bf282ab2` (the member
commit, this batch's last task commit before the close; its `STATUS.md` blob equals the one at `619fb8ef…`, above),
`PREVIOUS_BATCH_DISPATCH` to `cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md`, `ACT_DATE` to
`2026-10-23` (the day the move ran, which is this dispatch's date too), `DISPATCH` to this dispatch's file name, `TASK`
kept at `Task 2`; `MOVE_KIND` stays `ordinary`. This batch's aiming is appended to `PREVIOUS_AIMINGS`; the thirteenth
batch's aiming was already the last row and was not appended twice. The head comments name every former value; no
function and no existing row was touched.

`--apply` and `--check`, each into a scratch file [357]:

```
apply exit:0
check exit:0
```

the `--apply` output, whole:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 3, 2,982 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

and the `--check` output, whole:

```
  entries moved: 3, 2,982 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**The prediction HELD, read at the artifact rather than at the green `--check` (OI-379).**
`tools/audit/status_batch_bound.json` → `the_moved`:

```
668: "the_moved": [
669-  {
670-   "line_at_base": 8,
671-   "characters": 1914,
672-   "sha256": "ccc6d888f012460f17cb1a3f39c4150cf389da3aeff1062658940067df4373cf",
673-   "membership": "names the dispatch",
674-   "the_one_declared_adjustment_applied": true,
675-   "opening": "*2026-10-21 (CC — `records/cc/instructions/cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md`, Task 2, the close. **★★ THE L3 COMPARISO"
676-  },
677-  {
678-   "line_at_base": 10,
679-   "characters": 671,
680-   "sha256": "76028f12de358867e8f49d4e397d5b8d53f710ffb7519a41d6bea97aa94c3678",
681-   "membership": "says `Same dispatch`, in the run below the entry that names it",
682-   "the_one_declared_adjustment_applied": false,
683-   "opening": "*2026-10-21 (CC — Same dispatch, Task 1. **THE L3 COMPARISON CONTINUED: POSITION 35 TABULATED**: a capacity judgment written to a file outside the rep"
684-  },
685-  {
686-   "line_at_base": 12,
687-   "characters": 397,
688-   "sha256": "7eb63d65089953e87053ed466892833235f93ba4c60a8dcb30ea9d71fa272662",
689-   "membership": "says `Same dispatch`, in the run below the entry that names it",
690-   "the_one_declared_adjustment_applied": false,
691-   "opening": "*2026-10-21 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRY 437 ARE LANDED**, as they stood: each checked at its last bytes at its blob"
692-  }
693- ],
```

— exactly the thirteenth tabulation batch's three entries: its close entry (membership *names the dispatch*; the
declared prefix adjustment applied to it), its Task 1 entry and its Task 0 entry. After the move `STATUS.md` carries
this batch's three entries at lines 8, 10 and 12 and the two 2026-09-02 entries at lines 14 and 16; no STOP.

**2(c) — the regenerations and the checks.** The six checks, after the move, each into its own scratch file [363]:

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
  entries moved: 3, 2,982 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

Red exactly as A2 provides for: `gen_defense_share.py` and `gen_session_start_read_size.py`. **The L3 and L0/L1
population checks stayed green and were not regenerated** — the residue hit record did not move — and the evidence pin
stayed green. `gen_defense_share.py` written, then `--check`; then, **last, after the final edit to `STATUS.md`**,
`gen_session_start_read_size.py` written, then `--check` [369]:

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
    of the whole session-start read (248868): 5.21%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

and its `--check`, the same lines under the header *"the defense-share measurement re-derives"*.

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
    STATUS.md                                                                 12439
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 248868
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 248868 [ruled membership]  (-118253, -32.21%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 248868 [ruled membership]  (-47964, -16.16%)  <- CROSSES A REGIME BOUNDARY
```

and its `--check`, the same lines under the header *"the session-start read measurement re-derives"*.

**What moved, at the blob diff against the blob at `619fb8ef…`, by explicit hash** [374, 376]:
`tools/audit/defense_share.json` (`6faf22b4…` → `88f76f9e…`):

```
@@ -80 +80 @@
-  "the_whole_ordinary_session_start_read": 248690,
+  "the_whole_ordinary_session_start_read": 248868,
```

`tools/audit/session_start_read_size.json` (`2d149c7f…` → `6973c2da…`):

```
@@ -179 +179 @@
-   "STATUS.md": 12261,
+   "STATUS.md": 12439,
@@ -183 +183 @@
-  "total_characters": 248690,
+  "total_characters": 248868,
@@ -279 +279 @@
-   "to_total": 248690,
+   "to_total": 248868,
@@ -281,2 +281,2 @@
-   "change_in_characters": -118431,
-   "change_percent": -32.26,
+   "change_in_characters": -118253,
+   "change_percent": -32.21,
@@ -290 +290 @@
-   "to_total": 248690,
+   "to_total": 248868,
@@ -292,2 +292,2 @@
-   "change_in_characters": -48142,
-   "change_percent": -16.22,
+   "change_in_characters": -47964,
+   "change_percent": -16.16,
```

— both moved only by `STATUS.md`'s size. `tools/audit/status_batch_bound.json` (`430460f9…` → `601b2dde…`, 19 lines
in, 13 out): the aiming's fields, this batch's row in the record of aimings, and `the_moved` above. **No member of
either population, no item-4 passage and no member of `the_tabulation_population` moved** — the two population
checks stayed green.

**2(d) — this report.** **2(e)** — the close section appended to `records/cowork/handoff/cowork_away_returns.md`.
**2(f)** — the close commit, its staged set proved; its outputs are in that close section and the git log.

**E2 — expected MET at the close tree:** every `--check` A2 names green after the regenerations above; the failing set
is the end state's to measure (Task 3).

## 4. A1 to A5, graded

- **A1 — HELD**, established by the enumeration at 0(c).
- **A2 — HELD:** the opening capture as predicted; the reds of Task 2 exactly the two provided for, both regenerated
  green; the L3 and L0/L1 population checks green throughout; no STOP.
- **A3 — HELD:** `tools/audit/gen_l2_outgoing_population.py` was not run in any operating mode and its artifact was not
  touched; it appears in the capture's HISTORICAL list.
- **A4 — HELD:** no tool added or enrolled; exactly one tool source touched, `tools/audit/gen_status_batch_bound.py`'s
  authored aiming; population 82.
- **A5 — to be verified at the objects after the last commit**, by `git diff --name-status 619fb8ef… <close>` and the
  §6.1 to §6.35 span comparison, in the end-state section of `records/cowork/handoff/cowork_away_returns.md` (Task 3).
  Inside Task 1 the recheck already compared the §6.1 to §6.35 span of the committed copy with the old blob's, identical.

## 5. Findings of the run, and observations recorded and not acted on

- **No finding of the run under 1(h) or the Findings section**: every range matched, the document exists at its path,
  every statement parsed, and no derived statement lacked its fields.
- **Observation, not acted on — the size of position 36 relative to this session's context.** The member was finished
  whole, but the session's context was summarized once during it. The capacity judgment did not anticipate that, and a
  later dispatch may wish to weigh it for position 37 (above).

## 6. Declared departures

1. **The first tool calls were three reads made together** — the dispatch's first page, `STATUS.md` whole and
   `DECISIONS.md` from line 1 [1, 2, 3] — where the ordered first read puts the derivation immediately after the
   dispatch's first page. Nothing of the derivation had been read before them; the derivation's §5, §6 and §7 were then
   read first and its counts taken at that read.
2. **Position 37's entry at the artifact, with its ranges, came back in the read at line 35060** [59], where only its
   `lines` and `bytes` were ordered. Nothing of it was quoted, counted or placed; its sizes are used once, above.
   **Entry 439** — the checking sitting's entry, untracked and not landed — was also read whole [56], beside entry 438
   [55]; the dispatch orders entry 438's read only. Nothing of entry 439 was acted on.
3. **One search was refused by the search tool** — a pattern with a look-around [117] — and rewritten without it [118].
4. **Not read as ordered:** §11 and §12 of the reading file whole, and the manifest headers of §6.7 and §6.16 (item 13
   of §0 above). The recheck compares §10, §11 and §12 with the member's rows in both directions.
5. **A read was chained onto an act in four shell calls:** the Task 0 `git add` followed by `changed_paths.py
   --staged` [126]; the Task 0 commit followed by `git log -1` [127]; the copy of the reading file into the working
   tree followed by the two `git hash-object` calls [330]; and the member's `git add` followed by `changed_paths.py
   --staged` [332]. Each output is quoted above. (The two pushes [128, 337] were preceded, not followed, by their reads
   in the same call, and each push was verified at the ref file with the file tools.)
6. **The reading file was placed in the working tree with `cp`** [330], from the checked scratch copy, rather than
   written with the file tools; the blob of the working file was proved equal to the scratch copy's in the same call.
7. **The scratch scripts were copied into this session's scratch folder with `mkdir -p` and `cp`** [101] from the
   previous batch's scratch folder, before any repository file was read for Task 0.
8. **The context summary** (the head of this report) — not an act of the session, but a condition of the run: the
   capacity-judgment file's sentence on it was true when written and is not true of the whole member.
9. **The marks were checked by hand against the generator's list of marked rows**, and the WITHHELD rows' quotations
   by a script; no script compares the SEEN rows with their homes' spans, the artifact carrying none for them.

## 7. The scripts, and the limits they met

All in the session's scratch folder, outside the repository. **Repointed from the previous batch's** (scratch folder
and document names only, unless stated): `t0_lastbytes.py` (this batch's two paths and blobs); `t1_ranges.py` (the
document map to `pb_3413a9ed.md`, and three outputs added — fence lines, marker-line spans and hyphen-ending lines);
`t1_words.py`; `t1_inside.py`; `t1_dump.py`; `t1_member.py`; `t1_homes.py`; `t1_manifest_ranges.py`;
`run_checks_m.py`. **Unchanged:** `t1_recheck.py`, `t2_dedupe.py`. **New:** `gen36_lib.py` (the quotation and wrapping
helpers, adapted from `gen35_lib.py`: the blockquote marker dropped, the quotation join, the protection of charter names
and verdict tokens against wrapping, and the hazard test that keeps a wrapped line from opening with a list or table
marker); `gen36_rows_a.py` and `gen36_rows_b.py` (the rows, as data); `gen36.py` (assembles the rows, the *not a
statement* list, §11's block and the distribution; adds over `gen35.py` the axis foot's statement lists and **§12's
DIFFERS lines, generated from each row's own difference sentence**); `gen36_head.py` (the manifest header and foot;
keeps a row number and its label on one line in the foot's lists); `splice36.py`, `resplice36.py` and
`splice36_s12.py` (insert the subsection, §11's block and §12's block into the scratch copy of the reading file;
`resplice36.py` replaces the subsection and §11's block after a regeneration, leaving the hand edits to §0, the banner,
§10 and §13 in place); `t1_held36.py` (holds each WITHHELD row's quotation to the item-4 span); `t1_rel36.py` (lists
the RELOCATED statements for writing §10 by hand); `t2_calls36.py` (lists the shell calls from the transcript).
**Limits met:** the member check's first and second runs (above); the generator's first run of §12's lines took a
claim label inside a sentence as a segment boundary, corrected by requiring a capital after the label; the WITHHELD
check's first run missed four rows whose mark wrapped onto the next line, corrected by flattening the row before
matching.

## 8. What this batch did not do

No decision on any disposition, any difference, any open question, the derivation or the method; no recommendation; no
disposition applied; no outgoing text edited — `cowork_phrase_boundary_design.md`, `docs/scoring_model.md` and
`ARCHITECTURE.md` among them; the derivation, the brief, the pack and the input-contract files unedited; no session
booted; no measurement of the analysis; no `src/` file, build, test or golden; nothing under `tools/corpus/`,
`tools/robust_stop/` or `tools/dcml/`; no open-items row created, flipped or discarded; no decisions-register entry and
no `D-NNN`; no tool source touched but the forward bound's authored aiming; §6.1 to §6.35 untouched; no member split by
hand; positions 37 to 57 untouched.

## 9. The plan's tell, in one sentence

This batch produced nothing beyond the landed records, the reading file's §6.36 with its updates to §0 and §10 to §13
(and the one banner edit and the §0 clause on the previous batch's stop), the Task 2 files and this report — and,
outside the repository, the scratch files.

## 10. Self-check (D-434) — the standing check over this batch's own work

The diff of every file this batch touched was read against the principles, the conventions and the dispatch: the
reading file through the member's three checks (§2), whose recheck names every section the commit changed and compares
§10 to §12 with the rows in both directions, and its §0 and §13 at the sites edited; `STATUS.md` after the move, its
search for the 26 ruled terms run twice; `tools/audit/gen_status_batch_bound.py` at its five edits, each naming the
former value; the regenerated artifacts at their blob diffs. **#10, #12** — every superseded value in the tool's head
comments kept; the moved entries byte-present in the archive. **#15** — the reconciliation read at the artifact's
`the_moved`, not at the green check. **#17f / D-431** — no count restated in `STATUS.md`. **The reserved words** — the
word scan read by hand, and five of this session's own slips corrected before the commit (§2). **No violation was found
that is not declared in §6.**
