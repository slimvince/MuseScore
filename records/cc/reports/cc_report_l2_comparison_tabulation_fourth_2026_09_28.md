# CC REPORT — THE L2 COMPARISON, FIFTH BATCH: THE TABULATION CONTINUED FROM POSITION 9 — POSITIONS 9 TO 16 TABULATED WHOLE, THE REMAINDER UNTOUCHED (2026-09-28)

> **Executes** `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md`, pinned
> at blob `ec0b9e591f242cbc760a2949712d51a2d8b82090`. **No task STOPped.** The tabulation tabulated
> **positions 9 to 16**, each whole and each in its own commit. It stopped at the member boundary after
> position 16, under the dispatch's capacity judgment (Task 1(h)) and its batching rule (Task 1(g), D-672).
> The stop is recorded here and in the reading file's §0. **This report decides nothing**: it relays what
> was run and what was written, and it makes no recommendation about the derivation, the method, any
> disposition or any open question. Every output is quoted verbatim from the run. **No count the population
> tool produces, and no count of the reading file's rows, is restated in prose (D-431).** The member sizes
> are at `tools/audit/l2_outgoing_population.json` → `the_tabulation_population` → `the_members`. The row
> arithmetic is at the feet of the reading file's §6.9 to §6.16 and at its §13. The one exception the
> dispatch orders is the capacity judgment of Task 1(h), which states each member's `lines` and `bytes` as
> read at the artifact. Commit subjects are quoted as git prints them.

---

## 0. The ordered first read

The session's opening instruction named only this dispatch, so **the dispatch file was the first file
read**, to learn what to do. *(`CLAUDE.md` and the auto-memory index reached the session's context at boot
as injected context, before any tool call.)* The first read after the dispatch was
`cowork_blind_derivation_l2_2026_09_27.md`: its heading lines were located, then it was read from its `## 5.`
heading to its end — §5, then §6, then §7 — and then **the whole file** from its first line, in consecutive
portions. This came before any read of `STATUS.md`, `DECISIONS.md` or anything else (Ruling 2 of the
comparison-design sitting). This is declared at §5, item 1.

Then, in the dispatch's order:

- (1) `CLAUDE.md` at its six session-start spans, which were in context at boot. Then `STATUS.md`,
  `DECISIONS.md` whole, and `BUILD_AND_TEST.md` whole, its condition being met because this batch runs the
  guard set. Then the gating answer at `tools/audit/nongating_apparatus_rows.json` →
  `★_the_live_gating_answer` → `gating_ids`.
- (2) `cowork_audit_protocol.md`'s dispatch-protocol section.
- (3) The two rulings of 2026-09-27 and the comparison-design sitting, whole.
- (4) The phase definition, §0 and §3.4.
- (5) `FRAMEWORK.md` §5.
- (6) The brief's §2, §4 and §7.
- (7) The pack's L2 `counted`, `THE_WITHHELD_FAMILY` (`identities`, `documents`, `passages`) and `LEAKS`,
  read and not regenerated.
- (8) The current handover block, `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md`,
  which this batch lands.
- (9) The artifact's `the_passage_rule`, `the_order` and `the_members` from position 9 onward.
- (10) The reading file's banner and §0 to §5, the paragraph under `## 6.` that states the two reading rules,
  the first row blocks of §6.1, §6.8's foot and §10 to §16.

**Not read, as the dispatch orders:** the L0/L1 reading file's §10, since position 62 was not reached. The
outgoing texts were opened member by member, as Task 1 orders, each at its blob by explicit hash.

---

## 1. Task 0 — the records landed, and pushed

**0(a) — the pin.** `git hash-object -w` over the dispatch, and its size at the object:

```
$ git hash-object -w records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md
warning: in the working copy of 'records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md', LF will be replaced by CRLF the next time Git touches it
ec0b9e591f242cbc760a2949712d51a2d8b82090
exit:0
$ git cat-file -s ec0b9e591f242cbc760a2949712d51a2d8b82090
64854
exit:0
```

Proved unmoved immediately before staging (the first line of the 0(e) output below is the same hash).

**0(b) — the refs**, read with the file tools: `.git/refs/heads/master` and `.git/refs/remotes/origin/master`
each read `29d086b3482f29ccf6863549650d1e12dce89c94`, equal to the FACT. *(They were first printed by a shell
`cat` in the same command as the size above; that is declared at §5, item 4.)* The chain, by explicit hash:

```
commit 29d086b3482f29ccf6863549650d1e12dce89c94
parent a22d8a41affe6182e0abed22c2e60af336cc25ae
subject Close: the L2 tabulation continued from position 6, under its dispatch

 STATUS.md                                          |   2 +-
 STATUS_ARCHIVE.md                                  |   4 +
 ...rt_l2_comparison_tabulation_third_2026_09_27.md | 852 +++++++++++++++++++++
 tools/audit/defense_share.json                     |   2 +-
 tools/audit/gen_status_batch_bound.py              |  51 +-
 tools/audit/guard_state.json                       |  12 +-
 tools/audit/l2_outgoing_population.json            |   2 +-
 tools/audit/session_start_read_size.json           |  16 +-
 tools/audit/status_batch_bound.json                |  20 +-
 9 files changed, 932 insertions(+), 29 deletions(-)
---
commit a22d8a41affe6182e0abed22c2e60af336cc25ae
parent 413c0adba12c479968f1e9d8c4fb9ddebfe8f81d
subject comparison L2: member 8 tabulated - 212 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 2673 +++++++++++++++++++-
 1 file changed, 2659 insertions(+), 14 deletions(-)
---
commit 413c0adba12c479968f1e9d8c4fb9ddebfe8f81d
parent ba275ceb82f294cde6a2ab2a82d48fce1dc2624d
subject comparison L2: member 7 tabulated - 224 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 2538 +++++++++++++++++++-
 1 file changed, 2524 insertions(+), 14 deletions(-)
---
commit ba275ceb82f294cde6a2ab2a82d48fce1dc2624d
parent 0ee62fc2eba2635c857047c000d6724349db55b1
subject comparison L2: member 6 tabulated - 272 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 3029 +++++++++++++++++++-
 1 file changed, 3013 insertions(+), 16 deletions(-)
---
commit 0ee62fc2eba2635c857047c000d6724349db55b1
parent 3158c3c24c031505f55ad19190a09d766614fd75
subject record: entry 264 and the third L2 tabulation dispatch

 ...on_l2_comparison_tabulation_third_2026_09_27.md | 700 +++++++++++++++++++++
 ...ork_handoff_entry_two_hundred_and_sixty_four.md |  86 +++
 2 files changed, 786 insertions(+)
---
exit:0
```

The chain is the one the FACT relays: the tip `29d086b3…` is the third batch's close, its parent is member 8
`a22d8a41…`, then member 7 `413c0adb…`, member 6 `ba275ceb…` and Task 0 `0ee62fc2…`.

**0(c) — A1's check.** `python tools/audit/changed_paths.py` over the whole tracked population, written to a
scratch file and read with the file tools. Its first eight lines, and its last line:

```
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md
…
396 changed path record(s) [worktree]
```

Every line between them is under `scratch_artifacts/`, except the one before the last line,
`??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`. So the enumeration shows **exactly one
tracked modification**, `tools/audit/claude_md_finer_archive.json`, the **two untracked landing paths**, and
the standing untracked population, as A1 declares. The two landing paths, and nothing staged, by explicit
hash:

```
$ git ls-files --others --exclude-standard -- records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md
records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md
records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md
exit:0
$ git write-tree; git rev-parse 29d086b3482f29ccf6863549650d1e12dce89c94^{tree}
364818947e8f9717c4cfe1ffcc4bd41513190cd5
364818947e8f9717c4cfe1ffcc4bd41513190cd5
exit:0
```

**0(d) — the last-bytes check**, per landed file at its blob:

```
$ git hash-object -w --no-filters records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md; git hash-object -w --no-filters records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md
ec0b9e591f242cbc760a2949712d51a2d8b82090
45515b9cca907b807f6381157d6fcd7133ebeb29
exit:0
$ python <scratch>/lastbytes.py ec0b9e591f242cbc760a2949712d51a2d8b82090 45515b9cca907b807f6381157d6fcd7133ebeb29
== ec0b9e591f242cbc760a2949712d51a2d8b82090 size 64854 zero bytes 0
b'. TOWARDS the ultimate objective and TOWARDS the guiding principles.*\n'
== 45515b9cca907b807f6381157d6fcd7133ebeb29 size 5924 zero bytes 0
b'ce: Cowork, 2026-09-28 (Stockholm), the sitting booted on entry 264.*\n'
exit:0
```

Each file ends in a complete line and neither carries a zero byte. *(A first attempt with a shell `tail` was
denied by the guard; §5, item 5.)*

**0(e) — the commit.**

```
$ git hash-object records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md && git add -- records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md && git diff --cached --name-status 29d086b3482f29ccf6863549650d1e12dce89c94
ec0b9e591f242cbc760a2949712d51a2d8b82090
warning: in the working copy of 'records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md', LF will be replaced by CRLF the next time Git touches it
A	records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md
exit:0
$ git commit -m 'record: entry 265 and the fourth L2 tabulation dispatch' -m 'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>' && git push origin master 2>&1 | tail -3
[master 849a5fbc7b] record: entry 265 and the fourth L2 tabulation dispatch
 2 files changed, 857 insertions(+)
 create mode 100644 records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md
 create mode 100644 records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md
To https://github.com/slimvince/MuseScore
   29d086b348..849a5fbc7b  master -> master
exit:0
$ git show --stat --format='commit %H%nparent %P%nsubject %s' 849a5fbc7b | head -8; git rev-parse 849a5fbc7b:records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md 849a5fbc7b:records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md
commit 849a5fbc7b669050da134cc739f7b224932061f2
parent 29d086b3482f29ccf6863549650d1e12dce89c94
subject record: entry 265 and the fourth L2 tabulation dispatch

 ...n_l2_comparison_tabulation_fourth_2026_09_28.md | 779 +++++++++++++++++++++
 ...ork_handoff_entry_two_hundred_and_sixty_five.md |  78 +++
 2 files changed, 857 insertions(+)
ec0b9e591f242cbc760a2949712d51a2d8b82090
45515b9cca907b807f6381157d6fcd7133ebeb29
exit:0
```

Both refs then read `849a5fbc7b669050da134cc739f7b224932061f2` at their files, read with the file tools.

**0(f) — the opening guard capture.** The environment, recorded so 2(d) could run under the same one:

```
PYTHONIOENCODING=[unset] PYTHONUTF8=[unset]
Python 3.14.3
/c/s/MS/.venv/Scripts/python
shell: 5.2.37(1)-release
exit:0
```

`python tools/audit/gen_guard_state.py` — the invocation without a flag, which writes the artifact — with its
output saved to a scratch file outside the repository. Every verdict, verbatim:

```
wrote tools\audit\guard_state.json
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
  [PASS] tools/audit/gen_l2_outgoing_population.py --check
  [PASS] tools/audit/decisions/gen_decisions_register.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --verify
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
80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

Against A2: exactly the twelve FAIL verdicts the FACT names, and no thirteenth. The written artifact was then
compared with the committed object, by explicit hash:

```
opening blob 25ce197f6e6641818ce1d5a5e36d5d6264a4eedb
{'run': 80, 'passing': 68, 'failing': 12, 'not_run': 4, 'historical_records': 19}
FAIL tools/audit/gen_phase3_gate_partition.py --check
FAIL tools/audit/gen_filing_convention_application.py --check
FAIL tools/audit/gen_artifact_inventory.py --check
FAIL tools/audit/gen_artifact_inventory_surface.py --check
FAIL tools/audit/gen_test_construction_evidence.py --check
FAIL tools/audit/gen_retirement_caller_check.py --check
FAIL tools/audit/decisions/apply_soft_discard.py --check
FAIL tools/audit/decisions/apply_residue_discard.py --check
FAIL tools/audit/gen_epoch_write_path.py --check
FAIL tools/audit/gen_recognizer_establishment_sort.py --check
FAIL tools/audit/decisions/gen_home_classification.py --check
FAIL tools/audit/decisions/gen_phase1p_delegation_bar.py --check
verdict differences: []
not_run equal: True
historical equal: True
exit:0
```

The opening capture's blob `25ce197f…` equals the object at `29d086b3…` and at `849a5fbc…`, so the working
copy did not move at the opening. `python tools/audit/gen_guard_classification.py` exited 2:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

Exactly the four tools of the FACT, and no fifth.

**0(g) — the two blobs**, verified before Task 1 opened, at `849a5fbc…`, at `29d086b3…` and in the working
tree, with their sizes:

```
d78ac530992860d38d1f605a77a2961d5440a2f6
c5ff83dcad2107ac8c05ead21724cbab0d9471fd
d78ac530992860d38d1f605a77a2961d5440a2f6
c5ff83dcad2107ac8c05ead21724cbab0d9471fd
d78ac530992860d38d1f605a77a2961d5440a2f6
c5ff83dcad2107ac8c05ead21724cbab0d9471fd
125549
35952
25ce197f6e6641818ce1d5a5e36d5d6264a4eedb
exit:0
```

All three places agree with the FACT. *(The last line is `guard_state.json` at `849a5fbc…`.)*

**E0 — MET.** Two paths in one commit; `origin/master` at the commit; the pin proved; A1 reported with its
enumeration; the opening capture held against A2; the two blobs verified.

---

## 2. Task 1 — the tabulation, continued

### 2.1 The capacity judgments (1(h))

| Position | Document | `lines` | `bytes` | Judgment |
|---|---|---|---|---|
| 9 | `cowork_stage5_fitter_design.md`, whole | 1545 | 147929 | finishable whole, read in consecutive portions and drafted to scratch as 1(h) permits; opened and finished |
| 10 | `cowork_joint_estimator_factorization.md`, whole | 214 | 18449 | finishable whole; opened and finished |
| 11 | `cowork_score_census.md`, whole | 355 | 42049 | finishable whole; opened and finished |
| 12 | `cowork_prefit_gates.md`, whole | 204 | 16186 | finishable whole; opened and finished |
| 13 | `docs/nct_detection_design.md`, whole | 219 | 10148 | finishable whole; opened and finished |
| 14 | `cowork_phase5b_l4_build_plan.md`, whole | 84 | 7421 | finishable whole; opened and finished |
| 15 | `cowork_engage_arc_plan.md`, whole | 185 | 16074 | finishable whole; opened and finished |
| 16 | `cowork_l1l4_review_charter.md`, whole | 52 | 4286 | finishable whole; opened and finished |
| 17 | `ARCHITECTURE.md` passages — the opening block, above the first `## ` heading | 256 | 27814 | **judged not finishable whole in the context that remained, with the close still to run; NOT opened** |

Each size was read at the artifact before the member was opened. For positions 11 to 17 the judgment was
stated in the session before the member was opened; for positions 9 and 10 it was made on the sizes read at
the artifact but not written out at the time, which is declared at §5, item 8. **The first-member rule did
not fire**: position 9 was opened and finished whole. The position-17 judgment is this session's: position
17 is the first *passage* member this batch would have met, with six published ranges and four WITHHELD
identities; this session's context had already been compacted once; and the whole close was still to run.

### 2.2 The members, as written

Each member is a subsection §6.M of the reading file, after a `---` separator line, in the shape §6.1 to
§6.8 use. It has a manifest header, the rows, and the five foot sections. For positions 13 to 16 the
manifest carries the named-documents ruling's §2 account of what the document is, quoted from
`records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md` §2. Each member's commit
updated §0 (its row to **DONE**, the "Done" list, and the stop paragraph), §10 (its RELOCATED rows by target
charter, and the closing remark at §10's foot), §11, §12, §13 with its two arithmetic checks, and the §16
progress clause. The one banner insertion was made in the member-9 commit, and nowhere else. **WITHHELD
marks** were made at positions 10 (D-565), 12 (D-270 and D-271) and 15 (D-278), each from the artifact's
`item_4_identities_inside`. At position 12 one boundary case is marked and says so at the row: the sentence
that opens a line before D-271's home and carries that home's first claim, marked as Row 7.76 was. **No SEEN
home lies in positions 9 to 16**: none of the eight identities 1(c) names is in any of those members'
`item_4_identities_inside`, and each member's foot says so.

**The range check the Findings section orders**, run at each member's blob against the artifact's
`first_line_text` and `last_line_text`:

```
9 cowork_stage5_fitter_design.md lines 1-1545 file lines 1545 artifact lines 1545 crlf False first True last True
10 cowork_joint_estimator_factorization.md lines 1-214 file lines 214 artifact lines 214 crlf False first True last True
11 cowork_score_census.md lines 1-355 file lines 355 artifact lines 355 crlf False first True last True
12 cowork_prefit_gates.md lines 1-204 file lines 204 artifact lines 204 crlf False first True last True
13 docs/nct_detection_design.md lines 1-219 file lines 219 artifact lines 219 crlf False first True last True
14 cowork_phase5b_l4_build_plan.md lines 1-84 file lines 84 artifact lines 84 crlf False first True last True
15 cowork_engage_arc_plan.md lines 1-185 file lines 185 artifact lines 185 crlf False first True last True
16 cowork_l1l4_review_charter.md lines 1-52 file lines 52 artifact lines 52 crlf False first True last True
```

Every range matches. No blob is stored with CRLF line ends, so no carriage return had to be set aside.

### 2.3 How the rows were checked before each commit (1(g))

Each member was drafted in scratch and checked there before any commit. The five checks:

- **The quotation check** (`gen_check.py`, and its member-9 predecessor): every quoted outgoing statement and
  every *not a statement* quotation compared with the member's text at the blob (whitespace collapsed,
  emphasis marks stripped, block-quote prefixes removed). Every short quotation in an axis or difference
  sentence was compared against both texts. A coverage pass then replaced every quotation in the normalized
  member text and listed what was left. **From position 11 on, every quotation was cut by a scratch
  generator directly from the member's lines at the blob**, from a start and an end phrase, rather than
  typed. So the quotation check there tests the cut. Each member's §12 entries were checked against both
  texts, and the derived statement each is attributed to (`gen_secquotes.py`, `m10_attrib.py`). Result at
  every member: `problems: []` (position 9: `problems: 0`), with the uncovered fragments being headings,
  table header rows, table pipes and list markers only.
- **The count check**: the claims, dispositions and verdicts counted from the member text itself, every
  claim reconciled to exactly one disposition and at least one verdict, and every row naming a derived
  statement that §6.3 names as NEAREST checked to say so (`gen_nearest.py`). The foot's arithmetic and §13
  were generated from that count (`gen_build.py`).
- **The build check** (`gen_buildcheck.py`, and its member-9 predecessor): the member inserted into the
  committed reading file at the member's parent commit, in scratch. Its first lines at each member, verbatim:

```
span 6.1-6.8 identical: True 7d67218d09801ade 911227
span 6.1-6.9 identical: True e465bdb95e268b1f 1232649
span 6.1-6.10 identical: True 00f64c7fb33c7c55 1294420
span 6.1-6.11 identical: True 374113dee6e7a542 1377913
span 6.1-6.12 identical: True 06ef3f118c718005 1427323
span 6.1-6.13 identical: True d833d331fc1d83e6 1465048
span 6.1-6.14 identical: True 0eb046e88699808e 1494070
span 6.1-6.15 identical: True 74076418067041ba 1533722
```

  each followed by `§10 exact: True missing: [] extra: []` and the same line for §11, §12 proposals and §12
  differs. The diff outside the member touched only the ordered updates, plus one blank line at the member
  boundary that the line alignment reports as an insertion. That line was checked at the file each time: one
  blank line before `## 7.`, as the structure requires.
- **The word scan** (`p9_wordscan.py`): the member's own prose, quotations removed, scanned for British
  spellings and the reserved words. Each non-musical use found was rephrased before the commit. At position 11
  that was *licence* (to *license*) and *part* in the sense of portion. At position 13 it was *part* in that
  sense, three times. At position 15 it was *programme*, *beat* in the sense of outperform, and *scale* in a
  title of this session's. Every remaining hit was read and is a musical use, or a word inside a quotation or
  a document heading.
- **The consistency check**: every *"travelling with Row M.n"* checked to point at a row of the same
  disposition, and every *"as at Row M.n"* at a row carrying the same derived statement and verdict. This was
  done at the committed reading file for every earlier-member target (`rowdisp.py`, `m10_xcheck.py`), and by
  construction for targets inside the member.

### 2.4 The commits

```
ea12cd4dbc3ad4a024d4173743712c70b1622822 ca68dc789fcadea1b30ac8900f8293c937684ef3
    comparison L2: member 16 tabulated - 10 outgoing statements placed, proposals only
ca68dc789fcadea1b30ac8900f8293c937684ef3 7fe4056579511db3e4a5e3eb302ea300a71c5264
    comparison L2: member 15 tabulated - 45 outgoing statements placed, proposals only
7fe4056579511db3e4a5e3eb302ea300a71c5264 bd9a6c342f42f10db615727e67917e0906a8abd9
    comparison L2: member 14 tabulated - 47 outgoing statements placed, proposals only
bd9a6c342f42f10db615727e67917e0906a8abd9 d4cdd4ca596d05712187d19b2ccd990902cd5019
    comparison L2: member 13 tabulated - 50 outgoing statements placed, proposals only
d4cdd4ca596d05712187d19b2ccd990902cd5019 e955805d086db85dc4845dad823db660bb734d08
    comparison L2: member 12 tabulated - 71 outgoing statements placed, proposals only
e955805d086db85dc4845dad823db660bb734d08 02688fedd7eb464ba32c4ca75ab0cce30b01204d
    comparison L2: member 11 tabulated - 104 outgoing statements placed, proposals only
02688fedd7eb464ba32c4ca75ab0cce30b01204d 9dbbcc05a3cba713643dfe14a350983af72e77ec
    comparison L2: member 10 tabulated - 96 outgoing statements placed, proposals only
9dbbcc05a3cba713643dfe14a350983af72e77ec 849a5fbc7b669050da134cc739f7b224932061f2
    comparison L2: member 9 tabulated - 471 outgoing statements placed, proposals only
849a5fbc7b669050da134cc739f7b224932061f2 29d086b3482f29ccf6863549650d1e12dce89c94
    record: entry 265 and the fourth L2 tabulation dispatch
exit:0
```

Each member commit carries one path, the reading file, and was pushed at once. After each push,
`.git/refs/remotes/origin/master` was read with the file tools and equaled the new commit.

### 2.5 §6.1 to §6.8 proven untouched (A5)

The span from `### 6.1 — ` up to the line before `## 7.` in the blob at `29d086b3…`, against the span from
`### 6.1 — ` up to the separator before `### 6.9 — ` in the last member commit's blob, each extracted to
scratch outside the repository:

```
span 6.1-6.8 at 29d086b3: 926173 7d67218d09801ade301d4ec20e1a57b349d2e1e50e11bc39f79b58dd9d205769
span 6.1-6.8 at ea12cd4d: 926173 7d67218d09801ade301d4ec20e1a57b349d2e1e50e11bc39f79b58dd9d205769
identical: True
exit:0
```

### 2.6 The readings applied, and the case they could not decide

The two reading rules at the head of the reading file's §6 were applied unchanged at every member, as were
the second batch's three further readings and the third batch's further readings. **The readings this batch
took for the kinds of text it met are stated in each member's manifest, and none is ruled:**

- **At position 11, the census**:
  - a statement of what a corpus holds, of the role a corpus or a ground-truth class plays for a measurement
    or a fit, or of a rule governing what the measurement may use or trust, is RELOCATED to *the measurement
    of the analysis*;
  - an acquisition, an onboarding, an enumeration state, a ratified expansion or a plan is HISTORICAL;
  - a rule of how the project searches for, records and tracks corpora, and the census's account of its own
    reach, is listed under *not a statement* as a rule of the development process, following the example of
    member 10, which listed one;
  - a statement about a product tool outside the analysis is listed under *not a statement*.
- **At position 12, the pre-fit gates**, the precedents set by earlier members are named in the manifest:
  - the cross-validation protocol and the capacity budget travel with Rows 1.6(i) and 1.7;
  - tables counted once and frozen travel UNPLACED with Row 1.45;
  - the scope of the fitted values travels QUARANTINED with Row 1.28;
  - the protocol for the one adoption event is HISTORICAL, as Rows 9.107 and 9.189 were;
  - the dual path's sanction terms and retirement map are HISTORICAL.
- **At positions 13 to 16, the four smaller documents**, three readings apply:
  - a description of the implementation of the document's date is QUARANTINED, and its axis reads THE
    DERIVATION IS SILENT with the remark that the derivation states what L2 decides, not what an
    implementation did. The one exception is Row 14.17(ii), where a derived statement contradicts a mechanism
    the text records as built to a specification; there a DIFFERS stands beside the QUARANTINED, as Row 7.14
    carries one;
  - a rule of the order of work, of a review's process or of a development method is listed under *not a
    statement*;
  - an estimate, a step, a stage, an entry gate's item or a legacy work program is HISTORICAL.

**The one case the readings could not decide is Row 9.30** (the glossary's five harmonic-progression
idioms), with the rows that travel with it. It is a style taxonomy ratified from a measurement over corpora.
It describes no mechanism of the implementation, records no event of L2's build, belongs to none of
`FRAMEWORK.md` §5's charters, and the derivation names no style axis. It is placed UNPLACED with what was read.
Every other UNPLACED row in positions 9 to 16 is placed so for the reason its own row states.

### 2.7 The members done and not done

**Done: positions 9 to 16, each whole, each in its own commit** (§2.4). **Not done: positions 17 to 62**,
untouched: not read for tabulation, not quoted, not counted and not placed. **The next writing resumes at
position 17**, `ARCHITECTURE.md` passages — the opening block, above the first `## ` heading. The reading
file's §0 says the same. §7, §8, §9 and §14 stay NOT YET WRITTEN.

### 2.8 The next member's size, looked at as 1(h) orders

Position 17 is 256 lines and 27814 bytes at the artifact, with six ranges and four WITHHELD identities
(D-001, D-003, D-005, D-010). Smaller members were finished whole in this batch, and larger ones too: position
9 is larger by line and by byte, and position 11 by line and by byte. **Its size gives no reason to doubt that
a fresh session can finish it whole.** The stop here is this session's capacity judgment, not a judgment
about position 17. *(For planning only: among the passage members from position 17 onward, position 23 —
`ARCHITECTURE.md` §4 — stands at 817 lines, 58356 bytes and 100 ranges at the artifact, larger by range count
than anything tabulated so far, while smaller by byte than position 9.)*

**E1 — MET, with the timing departure of §5, item 8.**

- For every member done:
  - its manifest;
  - every outgoing statement with exactly one disposition, or UNPLACED with what was read;
  - every DIFFERS with its one-sentence difference and nothing chosen;
  - the marks of 1(c) where they apply;
  - the transfer list, audit questions and proposals gathered.
- §0 and the §16 progress clause are true of the file.
- The capacity judgment is stated for every member.
- There is no recommendation anywhere.
- A5 is intact, §6.1 to §6.8 included.

---

## 3. Task 2 — the close

**2(a) — the `STATUS.md` entry**, written first. It is one pointer entry at the top, naming this dispatch by
file name, with the `Last updated: ` prefix moved to it from the third batch's entry. It names positions 9 to
16 by position and document, restates no count, says every disposition is a proposal and nothing is applied,
and says where and why the batch stopped. It also says that one inconsistency is reported here and left at
its site (§6), and it points at this report.

**2(b) — the forward bound.** `STATUS.md`'s object at this batch's Task 0 commit, at `29d086b3…` and at the
last member commit, by explicit hash:

```
$ git rev-parse 849a5fbc7b669050da134cc739f7b224932061f2:STATUS.md 29d086b3482f29ccf6863549650d1e12dce89c94:STATUS.md ea12cd4dbc3ad4a024d4173743712c70b1622822:STATUS.md
565d8a849ce2252d9cbfc1b38feca7d4ae6d5cb5
565d8a849ce2252d9cbfc1b38feca7d4ae6d5cb5
565d8a849ce2252d9cbfc1b38feca7d4ae6d5cb5
exit:0
```

The same blob at all three. `tools/audit/gen_status_batch_bound.py` was then re-aimed, all five authored
constants together:

| Constant | Was | Now |
|---|---|---|
| `BASE_COMMIT` | `0ee62fc2eba2635c857047c000d6724349db55b1` | `849a5fbc7b669050da134cc739f7b224932061f2` |
| `PREVIOUS_BATCH_DISPATCH` | `cc_instruction_l2_comparison_tabulation_second_2026_09_27.md` | `cc_instruction_l2_comparison_tabulation_third_2026_09_27.md` |
| `ACT_DATE` | `2026-09-27` | `2026-09-28` |
| `DISPATCH` | `cc_instruction_l2_comparison_tabulation_third_2026_09_27.md` | `cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md` |
| `TASK` | `"Task 2"` | `"Task 2"` |

`MOVE_KIND` stays `"ordinary"` and `RULINGS` is unchanged. This batch's aiming is appended to
`PREVIOUS_AIMINGS`; the third batch's aiming was already its last row and was not appended twice. The head
comments are amended the way the previous batches amended them, each field's former value named in its
comment (#12). Then:

```
$ python tools/audit/gen_status_batch_bound.py --apply
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 2,113 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
exit:0
$ python tools/audit/gen_status_batch_bound.py --check
  entries moved: 1, 2,113 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
exit:0
```

**The entry that moved**, read at the files: the third batch's entry, the one naming
`records/cc/instructions/cc_instruction_l2_comparison_tabulation_third_2026_09_27.md`. It is now absent from
`STATUS.md` and present once in `STATUS_ARCHIVE.md`, under a header naming this dispatch's Task 2. The two
2026-09-02 entries stayed in `STATUS.md`. **The prediction held**: exactly that one entry moved, and there was
no STOP.

**2(c) — the regenerations**, each then `--check`. Every write and every check exited 0. The outputs,
verbatim:

```
$ python tools/audit/gen_evidence_pin_membership.py
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 102
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
$ python tools/audit/gen_evidence_pin_membership.py --check
the evidence pin's class membership re-derives
  (the same eight lines as above)
$ python tools/audit/gen_l0_l1_outgoing_population.py
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
$ python tools/audit/gen_l0_l1_outgoing_population.py --check
l0_l1_outgoing_population.json re-derives
$ python tools/audit/gen_l2_outgoing_population.py
item 1: ## The joint estimator — the standing rules of the production inference layer — 286 lines
item 1: #### Layer 3 — key/mode is the sequence decoder — 207 lines
item 1: #### Layer 4 — the per-slice chord-symbol decoder — 140 lines
item 1: #### Layer 5 — the function/cadence layer — 117 lines
item 2: 20 distinct names, 20 resolve (1123671 bytes), 8 in the specification set
item 3: 26 in-set files with a hit, 2664 distinct hit lines over them (ARCHITECTURE.md inside the four spans: 87, outside: 683); residue files: 168
item 4: in a specification-set member — 56
item 4: in an item-2 document that resolves — 28
item 4: inside item 1 — 19
item 4: reached by item 4 alone — 8
transfer span: 287 lines
tabulation population: 62 members, 14232 lines, 1317940 bytes
wrote C:\s\MS\tools\audit\l2_outgoing_population.json
$ python tools/audit/gen_l2_outgoing_population.py --check
l2_outgoing_population.json re-derives
$ python tools/audit/gen_defense_share.py
wrote tools/audit/defense_share.json
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   39804  ( 8.72%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (104609): 12.39%
    of the whole session-start read (247092): 5.24%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
$ python tools/audit/gen_defense_share.py --check
the defense-share measurement re-derives
  (the same fifteen lines as above)
$ python tools/audit/gen_session_start_read_size.py        # LAST, after the final edit to STATUS.md
wrote tools/audit/session_start_read_size.json
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              39804
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 168350, the six session-start spans 104609, overstated by 63741
    CLAUDE.md                                                                104609
    STATUS.md                                                                 11930
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 247092
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 247092 [ruled membership]  (-120029, -32.69%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 247092 [ruled membership]  (-49740, -16.76%)  <- CROSSES A REGIME BOUNDARY
$ python tools/audit/gen_session_start_read_size.py --check
the session-start read measurement re-derives
  (the same twenty-seven lines as above)
```

*(For the evidence pin, the defense share and the read size, the `--check` output is the write output with
its first line replaced by the re-derives line; where this report writes "the same … lines as above", that
was established by comparing the two scratch files. The two population tools' checks print the one line
shown. These are the outputs of the third pass of 2(c), run after the corrections to `STATUS.md` declared at
§5, item 10; the earlier passes differed from them only in the values `STATUS.md`'s size moves.)*

**The line-by-line comparison against A3**, each artifact between its blob at the last member commit
`ea12cd4d…` and the new working copy, extracted in scratch:

```
===== tools/audit/evidence_pin_membership.json | bytes 21731 -> 21731 | byte-identical: True | lines 376 -> 376
===== tools/audit/l0_l1_outgoing_population.json | bytes 1017399 -> 1017399 | byte-identical: True | lines 23189 -> 23189
===== tools/audit/l2_outgoing_population.json | bytes 3857098 -> 3857640 | byte-identical: False | lines 77721 -> 77721
  replace old 40141-40141 new 40141-40141
    -        "line": "*Last updated: 2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_third_2026_09_27.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 6: POSITIONS 6, 7 AND 8 — `cowork_layer4_chordsy
    +        "line": "*Last updated: 2026-09-28 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 9: POSITIONS 9 TO 16 — `cowork_stage5_fitter_de
===== tools/audit/defense_share.json | bytes 33229 -> 33229 | byte-identical: False | lines 618 -> 618
  replace old 80-80 new 80-80
    -   "the_whole_ordinary_session_start_read": 246552,
    +   "the_whole_ordinary_session_start_read": 247092,
  replace old 145-145 new 145-145
    -   "share_of_the_whole_ordinary_session_start_read": 5.26
    +   "share_of_the_whole_ordinary_session_start_read": 5.24
===== tools/audit/session_start_read_size.json | bytes 18864 -> 18864 | byte-identical: False | lines 305 -> 305
  replace old 179-179 new 179-179
    -    "STATUS.md": 11390,
    +    "STATUS.md": 11930,
  replace old 183-183 new 183-183
    -   "total_characters": 246552,
    +   "total_characters": 247092,
  replace old 279-279 new 279-279
    -    "to_total": 246552,
    +    "to_total": 247092,
  replace old 281-282 new 281-282
    -    "change_in_characters": -120569,
    -    "change_percent": -32.84,
    +    "change_in_characters": -120029,
    +    "change_percent": -32.69,
  replace old 290-290 new 290-290
    -    "to_total": 246552,
    +    "to_total": 247092,
  replace old 292-293 new 292-293
    -    "change_in_characters": -50280,
    -    "change_percent": -16.94,
    +    "change_in_characters": -49740,
    +    "change_percent": -16.76,
```

**Named against A3.**

- `evidence_pin_membership.json` and `l0_l1_outgoing_population.json` did not move.
- `l2_outgoing_population.json` moved in one line. That line is the residue record of `STATUS.md` (the record
  opening `"STATUS.md": {` → `"path": "STATUS.md"`), hit record at `line_number` 8: the new entry line
  replaced the third batch's.
- No member of the outgoing population or of the tabulation population moved, and no file entered or left the
  population or the residue.
- `defense_share.json` and `session_start_read_size.json` moved only in what `STATUS.md`'s new size moves.
- `status_batch_bound.json` is the forward bound's own artifact, written by `--apply`.

**No STOP.**

**2(d) — the closing guard capture**, under the environment 0(f) recorded:

```
$ echo "PYTHONIOENCODING=[${PYTHONIOENCODING:-unset}]"; python tools/audit/gen_guard_state.py > <scratch>/guard_close3.txt 2>&1
PYTHONIOENCODING=[unset]
exit:0
$ python <scratch>/guard_cmp3.py
opening lines 105 closing lines 105 identical: True
last line closing: 80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
classification: STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
exit:0
```

**The two captures are identical line for line**, so they are identical verdict for verdict: every PASS still
PASS, the same twelve FAIL, the NOT RUN and HISTORICAL lines identical, and population 80. The rewritten
`guard_state.json` moved against its blob at the last member commit only in three passing guards' captured
standard output, each following `STATUS.md`'s move:

```
summary equal: True
top-level keys equal: True
run keys equal: True
run differs: ('tools/audit/gen_defense_share.py', '--check') fields: ['stdout'] | verdict PASS -> PASS
     - ['the defense-share measurement re-derives', '  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)', '  row Evidence followed by a colon                         
     + ['the defense-share measurement re-derives', '  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)', '  row Evidence followed by a colon                         
run differs: ('tools/audit/gen_session_start_read_size.py', '--check') fields: ['stdout'] | verdict PASS -> PASS
     - ['the session-start read measurement re-derives', '  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids', '  CLAUDE.md is read under the regime: rul
     + ['the session-start read measurement re-derives', '  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids', '  CLAUDE.md is read under the regime: rul
run differs: ('tools/audit/gen_status_batch_bound.py', '--check') fields: ['stdout'] | verdict PASS -> PASS
     - ['  entries moved: 1, 2,033 characters', '  byte-present in the archive exactly once: True', '  absent from the must-read:                True']
     + ['  entries moved: 1, 2,113 characters', '  byte-present in the archive exactly once: True', '  absent from the must-read:                True']
```

*(The comparison script prints each differing stdout field's first 200 characters, which is why the first two
pairs look alike: the lists differ further along, in the values `STATUS.md`'s new size moves, as 2(c)'s
comparison of the two artifacts shows.)*

Then:

```
$ python tools/audit/gen_guard_classification.py
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
exit:2
```

Exactly the four tools of the FACT, unchanged.

**E2 — MET.** At the tree carrying the close: population 80; zero STOPs in the runner; the failing set exactly
the twelve named, and no other; the classification STOP unchanged.

---

## 4. The assumptions, graded

- **A1 — HOLDS**, established by the enumeration at 0(c). There was exactly one tracked modification,
  `tools/audit/claude_md_finer_archive.json`, carried and not chased, and exactly the two untracked landing
  paths, within the standing untracked population. Nothing was staged. Before the close was staged,
  `python tools/audit/changed_paths.py` listed exactly the eight close files Task 3 names (`STATUS.md`,
  `STATUS_ARCHIVE.md`, `tools/audit/defense_share.json`, `tools/audit/gen_status_batch_bound.py`,
  `tools/audit/guard_state.json`, `tools/audit/l2_outgoing_population.json`,
  `tools/audit/session_start_read_size.json`, `tools/audit/status_batch_bound.json`), plus that standing
  modification and the standing untracked population, which this report then joins.
- **A2 — HOLDS**: exactly the twelve at the opening capture, and no thirteenth.
  `gen_evidence_pin_membership.py --check` PASSED, as predicted.
- **A3 — HOLDS**: see 2(c).
- **A4 — HOLDS.** No tool was added and none enrolled. Exactly one tool source was touched,
  `tools/audit/gen_status_batch_bound.py`'s authored aiming. `gen_l2_outgoing_population.py` and
  `gen_guard_state.py` were not edited. Population 80 throughout.
- **A5 — HOLDS**, verified at the objects:
  - the batch's whole footprint from `29d086b3…` to the last member commit, by explicit hash:

```
$ git diff --name-status 29d086b3482f29ccf6863549650d1e12dce89c94 ea12cd4dbc3ad4a024d4173743712c70b1622822
M	ratification_surfaces/cowork_comparison_l2_reading.md
A	records/cc/instructions/cc_instruction_l2_comparison_tabulation_fourth_2026_09_28.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_five.md
exit:0
```

  - every object A5 names, at `29d086b3…` and at `ea12cd4d…`: `SAME` at each, among them the derivation
    `d78ac530…`, the brief `c5ff83dc…`, the pack directory `tools/audit/derivation_boot_pack/l2` tree
    `dae537fe…`, `tools/audit/derivation_boot_pack.json` blob `db340baf…`, the input contract `bbde68b9…`,
    the L0/L1 reading file `f3edcfe8…`, the five tools A5 names, `CLAUDE.md`, `ARCHITECTURE.md`,
    `DECISIONS.md`, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`, `FRAMEWORK.md`, the `decisions` and `open_items`
    trees and `tools/audit/decisions/backbone_decisions.json`;
  - no outgoing text of the tabulation population lies in the footprint above;
  - **§6.1 to §6.8 of the reading file are byte-identical**, as shown at §2.5;
  - the close commit adds only the files Task 3 names, proved at its staging. The re-check of A5 at the close
    commit itself is reported in the session's closing message, since that hash cannot be in this file.

---

## 5. Declared departures

1. **The dispatch file was read before the derivation.** The user's opening line named only the dispatch,
   so it had to be read first to learn the ordered first read. The derivation was then the first read of
   anything else (§0).
2. **The pin was taken after the dispatch was read from the working tree**, which is the declared-departure
   route of the standing clause (P-2). The blob was proved unmoved at staging (`ec0b9e59…`).
3. **A shell `wc -c` over repository paths was attempted once, early in the session, and the guard denied
   it.** Nothing ran. The sizes it would have printed were taken with the file tools and at the artifact.
4. **The refs were printed once by a shell `cat`** of `.git/refs/heads/master` and
   `.git/refs/remotes/origin/master`, in the same command as the pin's `git cat-file -s`. That is a
   working-tree read through the shell, which D-253 excludes, and the guard did not deny it. The refs were
   re-read at once with the file tools, which agree, and the file-tools reading is the one relied on (0(b)).
5. **The last-bytes check was first attempted with a shell `tail` pipeline, which the guard denied.** It was
   re-run as a scratch script reading the two git objects (0(d)).
6. **Each member was placed by building the extended reading file in scratch and copying it into place**, as
   the third batch did. Each build started from the reading file's committed blob at the member's parent
   commit, read by `git show` at the explicit hash. Before staging, the copied file's content was proved
   equal to the scratch build's.
7. **Every commit message carries the exact subject the dispatch gives**, followed by a short body (the
   position, the document and the dispatch task) and a co-author trailer. The subject line itself is
   verbatim.
8. **The capacity judgments for positions 9 and 10 were made on their sizes read at the artifact before each
   was opened, but were not written out in a visible message at the time.** They are stated at §2.1. The
   judgments for positions 11 to 17 were stated in the session before each member was opened.
9. **This session's context was compacted once, during position 10's drafting.** Afterward the work continued
   from the scratch drafts and the committed objects. The Task 0 outputs quoted at §1 were recovered from the
   session's own transcript by a scratch script, and are the outputs as they were printed then; they were not
   re-run. The quotation, build and consistency checks of every member after the compaction ran on the
   objects, not on memory of them.
10. **The 2(c) regenerations and the 2(d) closing capture were run three times.** Word scans of this report
    and of `STATUS.md` found that this session's `STATUS.md` entry used three reserved words in a non-musical
    sense: *note* ("the named-documents ruling's note"), and, in wording carried over from the third batch's
    entry, a bare *register* ("boot pack or register") and *figure* in the sense of a number ("no figure is
    restated"). They were changed to *account*, *decisions register* and *count*, in two rounds. After each
    round, `gen_status_batch_bound.py --check` was re-run and printed the same three lines, and then the five
    regenerations, the line-by-line comparison, the closing capture and the classification were all run
    again, in the same order and environment. The third pass is the one reported and committed. It differs
    from the earlier passes only in the values `STATUS.md`'s size moves: the read size's `STATUS.md` value
    and totals, and the defense share's denominator. Every pass's capture was identical to the opening one,
    line for line, and every pass's classification STOP named the four tools.

*Operational remarks, not departures.*

- The armed guard denied the commands of items 3 and 5. None was worked around; each was re-run in the
  sanctioned form.
- Three scratch patch scripts aborted on their own assertions before writing anything, and the same edits
  were made with the editor.
- At position 13, rows given only a start phrase first ran to the end of their line range. The coverage and
  quotation checks caught this before any commit, and the generator was corrected.

---

## 6. Findings of the run

**No finding number is allocated, and no apparatus defect was met.** Every member range matched the file
(§2.2), every outgoing text parsed into statements, and every derived statement carries its six fields. **No
1(h) finding arises**, since position 9 was finished whole.

**One inconsistency in this batch's own committed rows is written up here and left at its site**, the rule
for §6.1 to §6.8 being applied to the batch's own committed members, which the build check proves unchanged
at every later commit:

- **Rows 11.67 and 11.70(ii)** place, as RELOCATED to *the measurement of the analysis*:
  - that the fitter's design declares its data pool per license class before fitting;
  - that the fitter's split between objective and validation states which sources feed which.
- **Row 1.23 places the same content** — *"The fitting design states its objective-source and its
  validation-source split explicitly"* — as **ADOPTED — proposed**, with the proposal that L2's fit record
  state, for every fitted value, which pool fitted it and which pool validated it.
- Under the third batch's cross-member reading, a later statement of the same content would travel with Row
  1.23.
- It was noticed while member 12 was being prepared, after member 11 had been committed. It was not
  corrected, because a committed member is not re-opened.
- The user places the rows. Nothing about which placement is right is decided here.

---

## 7. What this batch did NOT do

- **No disposition applied anywhere.** Every disposition in the reading file is a proposal. No outgoing
  text, derivation, brief, boot pack, pack artifact, input contract, L0/L1 reading file or source of the
  decisions register was edited.
- **No decision** on any disposition, difference, open question, the derivation or the method. **No verdict**
  on the deriving session's independence. **No recommendation** in the reading file, this report or any
  commit message. **The five questions the derivation marks for the user (OQ-L2-2, 4, 5, 8, 16) are not
  put.**
- **No session booted, and no subagent spawned.** No measurement of the analysis was built, designed, scoped
  or run.
- **No tool source touched but the forward bound's authored aiming.** No guard enrollment, and no freeze of
  the L2 pack.
- **No open-items row created, flipped or discarded; no decisions-register identity.** No `src/` change,
  golden or test, and nothing under `tools/corpus/`, `tools/robust_stop/` or `tools/dcml/`.
- **No disposition of any residue file or of any of the eight LISTED item-2 documents.**
- **§6.1 to §6.8 were not re-opened, re-tabulated, re-numbered or corrected**, and neither were this batch's
  own committed members.
- **Positions 17 to 62 were not tabulated**, and are untouched. **No member was split by hand, and no
  smaller member was taken out of order.**

**The plan's tell, in one sentence:** the batch produced nothing in the repository other than the landed
records, the reading file's eight new member subsections with their updates to §0, §10 to §13 and the §16
progress clause and the one banner edit, the Task 2 files and this report. Outside the repository it produced
only scratch files: the member drafts and generators, the counting, quotation-checking, build-verifying and
consistency scripts, the guard and regeneration captures, the extracted comparison spans and the transcript
extracts. It also produced the loose git blob objects that `git hash-object -w` wrote for the ordered checks.

---

## 8. Self-check — the standing clause, run over the work on disk

1. **Principles.**
   - **#19**: the reading file establishes nothing and says so. Every row carries both texts' words and can
     be re-placed at the texts.
   - **#6**: the population's cut is the tool's, and no member was split by hand.
   - **#12**: the earlier batches' stops stay as their own sentences in §0, and UNPLACED, SILENT and every
     DIFFERS are kept. The inconsistency of §6 is recorded, not overwritten.
   - **#13**: the capacity judgment was stated for every member. The stop is a recorded member-boundary stop,
     not a partly worked member.
   - **#17(f)/D-431**: no artifact count is restated in the reading file or in this report's prose, save the
     1(h) sizes the dispatch orders. The tools' printouts and the commit subjects are quoted verbatim.
   - **#24**: no difference between measured quantities is asserted.
2. **Conventions.** This session's prose is in American English: British spellings in authored prose were
   corrected, and left where they sit inside quotations. The reserved words were checked by a scan of each
   member's own prose, with quotations removed, and the non-musical uses found were rephrased before each
   commit (§2.3). No invented label is left undefined.
3. **Values and premises.** Every quantity in this report is one of: a tool's verbatim printout, a git
   object identity, a pointer to an artifact field or to the reading file's feet and §13, or a 1(h) size read
   at the artifact. The premises were checked at their objects: the refs, the chain, the guard object, the
   two blobs, the pack, `STATUS.md`'s blob at the three commits and the §6.1 to §6.8 span.
4. **File-tools rule.** Working-tree content was read with the file tools, save the one `cat` of the refs
   declared at §5, item 4. The shell ran git object queries by explicit hash, the sanctioned scripts, and
   scratch scripts reading scratch files and git objects. The commands the guard denied were re-run in the
   sanctioned form.
5. **Uncertainty.** No comparison of measured quantities is made.

*Provenance: Claude Code, 2026-09-28, executing the dispatch above from its pinned blob. The close commit
carries this file, so its own hash, the pushed branch and `origin/master` after the push are reported in
the session's closing message and are at the git log.*
