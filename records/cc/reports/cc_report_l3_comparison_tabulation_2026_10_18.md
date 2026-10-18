# CC report — the L3 tabulation population published in its order, and the L3 comparison opened: positions 1 to 6 tabulated, proposals only — NOTHING DECIDED, NO ALGORITHM CHANGE, NO REGISTER ENTRY

Executed by Claude Code under `records/cc/instructions/cc_instruction_l3_comparison_tabulation_2026_10_18.md`, pinned at
Task 0 to blob `db7afc92d1dbd4e7b76a297ed1c1c6070a839f64` (99,737 bytes at the object). Task 2 stopped at a member
boundary, by this session's capacity judgment, after position 6; Tasks 0, 1 and 3 ran whole. This report decides nothing
and recommends nothing. No figure from the population artifact or the reading file is restated in prose (**D-431**):
the values below are the tools' own printed output and the diffs, quoted verbatim, and the artifacts are pointed at by
field.

## The members done and not done

- **Done: positions 1 to 6** — the six `ARCHITECTURE.md` places of the 2026-10-17 ruling's item 1: the sections *Layer
  4 — the per-slice chord-symbol decoder*, *Layer 5 — the function/cadence layer* and *Layer 6 — the grouping layer*,
  section *4.3 ChordSymbolFormatter* (its two subsections included), section *4.3b HarmonicRhythm*, and the passage
  *Harmonic rhythm detection* inside §11.5. Each is tabulated whole in its own commit, every statement under exactly one
  proposed disposition, the arithmetic closing at each member's foot and in §13.
- **Not done: positions 7 to 57** — UNTOUCHED: not read for tabulation, not quoted, not counted and not placed (**D-672**).
  **The next dispatch resumes at position 7**, `cowork_layer5_function_design.md`, whole.
- **The capacity judgment, stated before position 7 was opened, as 2(g) orders.** Position 7 is the largest WHOLE
  member; its size is at `tools/audit/l3_outgoing_population.json` → `the_tabulation_population` → `the_members` →
  position 7 → `bytes`. Reading it whole, and placing every one of its statements with its WITHHELD home (D-336) and its
  SEEN home (D-335), would have taken a large share of what remained of this session's context. With Task 3's close and
  Task 4's end-state run still to perform, I judged it not finishable whole, so it was not opened. No partly worked member
  was committed.
- **§0 of the reading file is true of the file**: it marks positions 1 to 6 DONE and 7 to 57 NOT YET TABULATED, and states
  that a member so marked is untouched. §7, §8, §9 and §14 are headed NOT YET WRITTEN, as 2(e) and 2(f) order.

## 1. Task 0 — the pin, the refs, A1, the last bytes, the commit, the opening capture

**0(a) — the pin.** `git hash-object -w` of the dispatch printed `db7afc92d1dbd4e7b76a297ed1c1c6070a839f64` under the
default filters and under `--no-filters`; `git cat-file -s` printed `99737`. The dispatch was re-hashed immediately
before staging and returned the same blob, and the committed blob is the same (verified below).

**0(b) — the refs and the chain.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both read
`6e127d7a94d4e3f4dbdd7858bd39fef54992b712` (file tools), as the premise ledger states. `git show --stat` of the chain, as
printed:

```
commit 6e127d7a94d4e3f4dbdd7858bd39fef54992b712
parent affc956bc169dcdc5746603a2d8c9883d2a9f905
subject End state: the L3 outgoing population — guard run at the close tree, the A2 regenerations already met inside the close

 records/cowork/handoff/cowork_away_returns.md | 37 +++++++++++++++++++++++++++
 tools/audit/guard_state.json                  | 34 ++++++++++++++++--------
 2 files changed, 61 insertions(+), 10 deletions(-)
commit affc956bc169dcdc5746603a2d8c9883d2a9f905
parent a4604507486c392b63882e4446a41fdf80ef7e65
subject Close: the L3 outgoing population, under its dispatch

 STATUS.md                                          |   6 +-
 STATUS_ARCHIVE.md                                  |   8 +
 .../cc_report_l3_outgoing_population_2026_10_18.md | 794 +++++++++++++++++++++
 records/cowork/handoff/cowork_away_returns.md      |  48 ++
 tools/audit/defense_share.json                     |   4 +-
 tools/audit/evidence_pin_membership.json           |   3 +-
 tools/audit/gen_status_batch_bound.py              |  53 +-
 tools/audit/session_start_read_size.json           |  16 +-
 tools/audit/status_batch_bound.json                |  36 +-
 9 files changed, 939 insertions(+), 29 deletions(-)
commit a4604507486c392b63882e4446a41fdf80ef7e65
parent 50df6b5feaa36fbc5347b2f59818ff97898a4150
subject audit: the l3 outgoing population derived and measured under the rulings of 2026-10-17 and 2026-10-18 (nothing tabulated)

 tools/audit/gen_guard_state.py            |    18 +
 tools/audit/gen_l3_outgoing_population.py |   663 +
 tools/audit/l3_outgoing_population.json   | 33070 ++++++++++++++++++++++++++++
 3 files changed, 33751 insertions(+)
commit 50df6b5feaa36fbc5347b2f59818ff97898a4150
parent 986b9663085c4ab21c6a4d3f3957b3fbe9d45b23
subject record: the l3 keyword-list ruling, entries 423-424 and the l3 outgoing-population dispatch

 ...nstruction_l3_outgoing_population_2026_10_18.md | 1279 ++++++++++++++++++++
 ...k_handoff_entry_four_hundred_and_twenty_four.md |   73 ++
 ..._handoff_entry_four_hundred_and_twenty_three.md |   73 ++
 ...k_rulings_2026_10_18_l3_keyword_list_sitting.md |  102 ++
 4 files changed, 1527 insertions(+)
commit 986b9663085c4ab21c6a4d3f3957b3fbe9d45b23
parent 49a3ce5813981324011897d6a6a7119eb6d8642d
subject End state: the L3 keyword count — guard run at the close tree, the A2 regenerations already met inside the close

 records/cowork/handoff/cowork_away_returns.md | 33 +++++++++++++++++++++++++++
 tools/audit/guard_state.json                  | 14 ++++++------
 2 files changed, 40 insertions(+), 7 deletions(-)
```

The chain is the premise ledger's: four commits on `986b9663…`, linear. **The guard summary at the object**
(`6e127d7a…:tools/audit/guard_state.json` → `summary`, read whole at that block): run 82, passing 69, failing 13, the
thirteen named in the premise ledger, `not_run` 4, `historical_records` 20 — the FACT holds at the object.

**0(c) — A1.** `python tools/audit/changed_paths.py` (exit 0) listed exactly ONE tracked modification,
`tools/audit/claude_md_finer_archive.json`, whose `git hash-object` equals the tip's blob
(`1df4f20771b6782cbb965c293db4d445bc7ec892`, both — line endings only; left untouched, never staged); two untracked
paths under `records/` — this dispatch and `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_five.md`;
and the standing untracked population (`Claude outputs/`, `Codex research inventory/`, `docs/research_papers/polyph9-release/`,
the two files under `external resarch summary/`, everything under `scratch_artifacts/`,
`tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`); 396 records in all. Nothing else under `records/`,
`reading_pass/` or `ratification_surfaces/`, and nothing else at the root. Per landing path,
`git ls-files --others --exclude-standard -- <path>` printed the path (exit 0 each). Per tracked input this batch edits,
`git diff --stat 6e127d7a94d4e3f4dbdd7858bd39fef54992b712 -- <path>` printed nothing (exit 0 each) for `STATUS.md`,
`STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`,
`tools/audit/gen_l3_outgoing_population.py`, `tools/audit/l3_outgoing_population.json` and
`records/cowork/handoff/cowork_away_returns.md`.

**0(d) — the last bytes**, measured at the objects only (the script is §7's), whole:

```
== records/cc/instructions/cc_instruction_l3_comparison_tabulation_2026_10_18.md
   blob db7afc92d1dbd4e7b76a297ed1c1c6070a839f64  size 99737
   zero bytes: 0
   ends with a newline: True
   last line: no bar added.
   last 70 bytes: b'd (correction 4); no task was widened by this check and\nno bar added.\n'
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_five.md
   blob 357da38fbbbbd7e81b9d5179db0826aa841cf817  size 7056
   zero bytes: 0
   ends with a newline: True
   last line: instruction; "continue"; "continue"; "continue".*
   last 70 bytes: b' words: the opening\ninstruction; "continue"; "continue"; "continue".*\n'
```

**Entry 425 exists, 7,056 bytes at the object**; both files end with a whole line, no zero byte.

**0(e) — the commit.** Staged by explicit path; `changed_paths.py --staged` showed exactly the two `A` records. Commit
`b11054f27831c242a6e82f45e2503d93058a7f9e`, subject `record: entry 425 and the l3 comparison tabulation dispatch`.
Verified at the object: `changed_paths.py --commit` lists the two paths as added; its parent is `6e127d7a…`; `git
rev-parse b11054f2…:<path>` returns `db7afc92…` and `357da38f…`, the blobs measured. The push printed
`6e127d7a94..b11054f278  master -> master`, and `.git/refs/remotes/origin/master` then named `b11054f2…`.

**0(f) — the opening capture**, after the commit: `python tools/audit/gen_guard_state.py --check` (exit 0), whole:

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

**A2 HELD AT THE START, exactly:** run 82; failing exactly the thirteen of the premise ledger and nothing else;
`gen_evidence_pin_membership.py --check` green, as A2 expected; no STOP in the runner.

`python tools/audit/gen_guard_classification.py --check` (exit 2), whole:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_withheld_family_reading.py']
```

— exactly the four names of the FACT; no fifth. Carried, not chased.

**E0 — MET.** The pin proved; the two named paths in one commit, `b11054f2…`; `origin/master` at it; A1 reported with
its enumeration and held; the opening capture as A2 predicted.

## 2. Task 1 — the tabulation population, published by the tool

**1(a) — the six edits**, made with the file-editing tool, in the dispatch's order. The diff against the boot tip,
`git diff -U0 6e127d7a94d4e3f4dbdd7858bd39fef54992b712 -- tools/audit/gen_l3_outgoing_population.py`, whole:

```
diff --git a/tools/audit/gen_l3_outgoing_population.py b/tools/audit/gen_l3_outgoing_population.py
index c5b2bb2baf..f3bcf0699a 100644
--- a/tools/audit/gen_l3_outgoing_population.py
+++ b/tools/audit/gen_l3_outgoing_population.py
@@ -45,0 +46,6 @@ WHAT IT DOES, AND NOTHING ELSE.  Every numbered item is a key of the artifact.
+  6. `the_tabulation_population` -- the population cut into the MEMBERS the comparison tabulates,
+     in its order, under the named-documents derivation of the tabulation dispatch and
+     THE_PASSAGE_RULE (the L2 comparison's, imported); with three further STOPs: item 2's derived
+     names differing from the derivation's two lists, a specification-set member among them not
+     graded WHOLE, and a hit line or an item-4 home not lying in exactly one member.
+
@@ -67 +73 @@ THE STOPS, each ending the run with `STOP: <reason>` and exit 2 -- never a trace
-WHAT IT DOES NOT DO.  It takes no disposition, orders no tabulation, fixes no tabulation unit,
+WHAT IT DOES NOT DO.  It takes no disposition, fixes no tabulation unit,
@@ -69,2 +75,2 @@ grades nothing, compares nothing, and edits no outgoing text.  It does not open
-derivation, its brief, or the boot pack's directory.  THE TABULATION IS THE NEXT DISPATCH'S, written
-after the writing side has read `the_measured_size`.
+derivation, its brief, or the boot pack's directory.  THE TABULATION'S ORDER IS PUBLISHED HERE; ITS
+UNIT IS THE TABULATING DISPATCH'S.
@@ -106,0 +113,3 @@ from gen_l2_outgoing_population import (         # noqa: E402  (path set above)
+    TOP_LEVEL,
+    block_around,
+    fence_ranges,
@@ -108,0 +118 @@ from gen_l2_outgoing_population import (         # noqa: E402  (path set above)
+    merge_ranges,
@@ -110,0 +121 @@ from gen_l2_outgoing_population import (         # noqa: E402  (path set above)
+    subtract_spans,
@@ -186,3 +197,67 @@ SIZE_STOP_STATEMENT = (
-    "THIS BATCH TABULATES NOTHING.  The size stop is that the batch ends here; the tabulation's "
-    "unit, order and batching, and which of item 2's documents are compared whole, are written by "
-    "the next dispatch after the writing side has read this block."
+    "THE TABULATION RUNS IN THE ORDER OF `the_tabulation_population`, ONE MEMBER PER COMMIT, AND "
+    "MAY STOP AT ANY MEMBER BOUNDARY (D-672).  Its unit, the outgoing statement, is fixed by the "
+    "dispatch that tabulates, not by this tool."
+)
+
+# --------------------------------------------------------------------------------------------
+# THE NAMED-DOCUMENTS DERIVATION -- which of item 2's documents are compared WHOLE.  Not a ruling:
+# the 2026-10-17 ruling (item 2) says the named documents are graded afterwards AS THE L2
+# NAMED-DOCUMENTS RULING GRADED L2's, a question put to the user only where the measurement raises
+# one.  The writing side applied that ruling's three classes to the twelve derived names on
+# 2026-10-18 and found every name already placed by them (the tabulation dispatch records the
+# derivation); the user may overrule it.  AUTHORED from that derivation; the union must equal
+# item 2's derived names EXACTLY, in both directions, and every specification-set member among
+# them must be WHOLE, or the run STOPs -- so a name entering or leaving the six spans halts it.
+# --------------------------------------------------------------------------------------------
+THE_NAMED_DOCUMENTS_DERIVATION = {
+    "derived_by": "records/cc/instructions/cc_instruction_l3_comparison_tabulation_2026_10_18.md, "
+                  "the section THE NAMED-DOCUMENTS DERIVATION, applying the classes of "
+                  "records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md §1 "
+                  "under item 2 of the 2026-10-17 ruling",
+    "what_it_is": "a derivation by the writing side, not a ruling; no question was raised that the "
+                  "record does not answer, so none was put to the user",
+    "executed_by": "records/cc/instructions/cc_instruction_l3_comparison_tabulation_2026_10_18.md, "
+                   "Task 1",
+}
+
+ITEM_2_WHOLE = [
+    "cowork_layer4_chordsymbol_design.md",
+    "cowork_layer5_engagement_design.md",
+    "cowork_layer5_function_design.md",
+    "cowork_layer6_grouping_design.md",
+    "cowork_engage_arc_plan.md",
+    "cowork_l1l4_review_charter.md",
+    "cowork_phase5b_l4_build_plan.md",
+    "docs/nct_detection_design.md",
+]
+
+ITEM_2_LISTED_NOT_WHOLE = [
+    "CLAUDE.md",
+    "OPEN_ITEMS.md",
+    "records/cc/reports/cc_tonicization_modulation_metric_dossier.md",
+    "records/cowork/rulings/cowork_rulings_2026_08_09_second_stop.md",
+]
+
+THE_PASSAGE_RULE = (
+    "A passage is the block of lines holding one item-3 hit line, or spanning one item-4 home: "
+    "(a) a line inside a fenced code block takes the whole block, fence lines included; (b) any "
+    "other line takes the maximal run of consecutive non-blank lines around it, stopping at a blank "
+    "line or a fence line; (c) where that run is one heading line standing alone, it takes the "
+    "heading together with the block that follows it (blank lines skipped), unless the next "
+    "non-blank line is a heading or a fence.  An item-4 home spanning lines a..b takes the block "
+    "around a through the block around b.  Overlapping or touching passages of one document merge.  "
+    "In ARCHITECTURE.md every line inside the six item-1 spans is removed from the passages (those "
+    "spans are tabulated whole), and the passages are grouped by the nearest top-level `## ` heading "
+    "at or before them, the lines before the first such heading forming the opening block.  The "
+    "rule and the four functions that implement it are the L2 comparison's, imported from "
+    "gen_l2_outgoing_population and not copied."
+)
+
+THE_ORDER = (
+    "1-6: the six item-1 places, in ARCHITECTURE.md's order.  Then the eight WHOLE item-2 "
+    "documents: the specification-set members first, then the others; within each group by "
+    "descending count of distinct item-3 hit lines, ties by path.  Then ARCHITECTURE.md's passages, "
+    "one member per top-level `## ` section, in the file's order.  Then every other document "
+    "carrying passages: the specification-set members by descending count of their distinct item-3 "
+    "hit lines, ties by path; then the documents reached by item 4 alone, by path.  Last: the two "
+    "transfer inputs, the L0/L1 comparison's section 10 span and then the L2 comparison's."
@@ -438,0 +514,160 @@ def derive():
+    # ---- THE TABULATION POPULATION (the named-documents derivation; THE_PASSAGE_RULE; THE_ORDER) --
… (the 160 added lines of edit 3, the dispatch's block verbatim; the whole diff is reproducible by the command above
   at the Task 1 commit, and the block was read line for line against the dispatch before the commit) …
@@ -476,0 +712,11 @@ def derive():
+        "the_tabulation_population": {
+            "members": len(members),
+            "members_by_kind": {k: sum(1 for m in members if m["kind"] == k)
+                                for k in sorted({m["kind"] for m in members})},
+            "lines_by_kind": {k: sum(m["lines"] for m in members if m["kind"] == k)
+                              for k in sorted({m["kind"] for m in members})},
+            "bytes_by_kind": {k: sum(m["bytes"] for m in members if m["kind"] == k)
+                              for k in sorted({m["kind"] for m in members})},
+            "lines_total": sum(m["lines"] for m in members),
+            "bytes_total": sum(m["bytes"] for m in members),
+        },
@@ -485 +731,2 @@ def derive():
-        "LINES; the passages cut around them are the next dispatch's."
+        "LINES; the passages cut around them are at `the_tabulation_population` under "
+        "`the_passage_rule`."
@@ -494,2 +741,3 @@ def derive():
-            "ruling's four items, and states how large each is.  It takes no disposition, orders "
-            "no tabulation and grades nothing."
+            "ruling's four items, and states how large each is; `the_tabulation_population` cuts "
+            "it into the members the comparison tabulates, in their order.  It takes no "
+            "disposition and grades nothing."
@@ -499,2 +747,3 @@ def derive():
-            "it orders no tabulation and fixes no tabulation unit; it grades none of item 2's "
-            "documents whole or listed; it edits no outgoing text; and it does not open the blind "
+            "it fixes no tabulation unit; which of item 2's documents are compared whole it "
+            "carries as the writing side's derivation, not as a ruling; it edits no outgoing "
+            "text; and it does not open the blind "
@@ -510 +759,2 @@ def derive():
-            "`norm`, `MD_NAME`, `HOME_SHAPE` and `THE_RESIDUE_STATEMENT` from "
+            "`norm`, `MD_NAME`, `HOME_SHAPE`, `THE_RESIDUE_STATEMENT`, `TOP_LEVEL`, `fence_ranges`, "
+            "`block_around`, `merge_ranges` and `subtract_spans` from "
@@ -528 +778 @@ def derive():
-                "is a later question (the 2026-10-17 ruling, item 2)."
+                "is graded at `the_tabulation_population` under `the_named_documents_derivation`."
@@ -616,0 +867,16 @@ def derive():
+        "the_named_documents_derivation": THE_NAMED_DOCUMENTS_DERIVATION,
+        "the_tabulation_population": {
+            "★_what_this_is": (
+                "The outgoing population cut into the MEMBERS the comparison tabulates, in the "
+                "order it tabulates them, under the rulings of 2026-10-17 (Option B) and 2026-10-18 "
+                "(Option B), the named-documents derivation and the passage rule below.  Every "
+                "item-3 hit line of every specification-set member lies in exactly one member, and "
+                "every one of the 22 item-4 homes lies wholly in exactly one member; either failing "
+                "is a STOP, so this sentence records checks that passed.  It takes no disposition "
+                "and grades nothing."
+            ),
+            "the_passage_rule": THE_PASSAGE_RULE,
+            "the_order": THE_ORDER,
+            "item_2_listed_not_compared_whole": listed,
+            "the_members": members,
+        },
@@ -657,0 +924,3 @@ def main():
+    tp = size["the_tabulation_population"]
+    print("tabulation population: %d members, %d lines, %d bytes"
+          % (tp["members"], tp["lines_total"], tp["bytes_total"]))
```

**A declared shortening, stated rather than hidden.** The diff above is whole except the 160 added lines of edit 3,
which are the dispatch's 1(a) edit-3 block verbatim. They are elided to keep this report readable, and anyone can recover
them by running the stated command at the Task 1 commit. The scratch copy of the full diff was read whole before the commit.

**1(b) — the synthetic checks**, through the amended module's names (the script is §7's), whole:

```
HELD    fence_ranges(lines) == [(6, 8)]  (got [(6, 8)])
HELD    block_around(lines, 4, [(6, 8)]) == (3, 4)  (got (3, 4))
HELD    block_around(lines, 7, [(6, 8)]) == (6, 8)  (got (6, 8))
HELD    block_around(lines, 1, [(6, 8)]) == (1, 4)  (got (1, 4))
HELD    block_around(lines, 9, [(6, 8)]) == (9, 9)  (got (9, 9))
HELD    merge_ranges([(5, 7), (1, 2), (3, 3), (9, 9)]) == [(1, 3), (5, 7), (9, 9)]  (got [(1, 3), (5, 7), (9, 9)])
HELD    subtract_spans([(1, 10)], [(4, 5), (8, 8)]) == [(1, 3), (6, 7), (9, 10)]  (got [(1, 3), (6, 7), (9, 10)])
ALL SEVEN HELD
```

The import resolves; no function was edited.

**1(c) — the run and the check.** `python tools/audit/gen_l3_outgoing_population.py` — **exit 0**, whole:

```
item 1: #### Layer 4 — the per-slice chord-symbol decoder — 140 lines
item 1: #### Layer 5 — the function/cadence layer — 117 lines
item 1: #### Layer 6 — the grouping layer — 65 lines
item 1: ### 4.3 ChordSymbolFormatter — 115 lines
item 1: ### 4.3b HarmonicRhythm — 81 lines
item 1: #### Harmonic rhythm detection — 20 lines
item 2: 12 distinct names, 12 resolve (844831 bytes), 4 in the specification set
item 3: 26 in-set files with a hit, 1364 distinct hit lines over them (ARCHITECTURE.md inside the six spans: 83, outside: 355); residue files: 150
item 4: in a specification-set member — 10
item 4: in an item-2 document that resolves — 9
item 4: inside item 1 — 3
transfer span: ratification_surfaces/cowork_comparison_l0_l1_reading.md — 287 lines
transfer span: ratification_surfaces/cowork_comparison_l2_reading.md — 948 lines
tabulation population: 57 members, 11276 lines, 1075960 bytes
wrote C:\s\MS\tools\audit\l3_outgoing_population.json
```

`--check` — **exit 0**: `l3_outgoing_population.json re-derives`. No `STOP:` line and no traceback on either run.

**The unchanged-part property**, measured between the committed artifact's blob
(`6e127d7a…:tools/audit/l3_outgoing_population.json` = `92ef966cb03caca4be8288522c423b20ac1aceb5`) and the new one written
into the object store (`13d1750be95ecdcf408405ff7d6f67bba8db1dfe`), both read from the object store and compared
recursively by key path (the script is §7's), whole:

```
key paths of the old artifact MISSING from the new: 0
key paths whose value CHANGED: 6
    ★_what_this_artifact_is
    ★_what_it_does_not_do
    one_path_per_concern
    item_2_the_documents_the_sections_name -> no_grading_of_form
    item_3_the_term_search -> the_reach_stated
    the_measured_size -> ★_the_size_stop
key paths ADDED in the new (topmost added keys only): 3
    the_measured_size -> the_tabulation_population
    the_named_documents_derivation
    the_tabulation_population
item_3_the_term_search -> the_population identical: True
item_3_the_term_search -> the_residue_for_the_mining_map identical: True
item_4_the_decision_passages -> the_passages identical: True
```

**The property holds exactly as the dispatch states it**: exactly the six strings changed; exactly the three key paths
added; the population, the residue and the passages identical.

**1(d) — the published order, read at the new artifact's `the_tabulation_population` → `the_members`, checked against
the dispatch:** positions 1 to 6 are the six item-1 places in `ARCHITECTURE.md`'s order (Layer 4, Layer 5, Layer 6,
§4.3, §4.3b, the harmonic-rhythm passage); positions 7 to 14 are the eight WHOLE documents, the four
specification-set members first; the last two are the two transfer inputs, the L0/L1 file's span and then the L2 file's;
between them come `ARCHITECTURE.md`'s passage members in the file's order, then the specification-set members carrying
passages. There is **no member of kind `item 4 — passages reached by item 4 alone`**. The guide held: the
`item_4_identities_inside` lists sum to the full withheld set; D-022 and D-605 sit inside `ARCHITECTURE.md` passage
members; the `cowork_phrase_boundary_design.md` member carries seven identities and `cowork_joint_estimator_architecture.md`
one. **The member count, lines and bytes are at `the_measured_size` → `the_tabulation_population`**, and the tool's
printed line above shows them; neither is restated in prose.

**1(e) — the commit.** `changed_paths.py` before staging showed the two Task 1 modifications and A1's one; staged by
explicit path, `--staged` showed exactly the two. Commit `966786b80bf5c971f74d6c98dcfcd849cf01b3c3`, subject
`audit: the l3 tabulation population published in its order under the named-documents derivation and the passage rule,
nothing tabulated yet`; verified at the object (`changed_paths.py --commit`: `M` the two paths; parent `b11054f2…`;
the tool's blob `f3bcf0699ae7559c4ec466ac6fbff0829bc88cb5` and the artifact's `13d1750b…`, each equal to `git
hash-object` of the written file). The push printed `b11054f278..966786b80b  master -> master`; `origin/master` then
named `966786b8…`.

**E1 — MET.** The six edits present (the diff); the synthetic checks held; the tool and its `--check` exit 0 with no
`STOP:` line; the unchanged-part property proved; the order checked against 1(d); the member count, lines and bytes at
the artifact, cited and not restated.

## 3. Task 2 — the reading file

`ratification_surfaces/cowork_comparison_l3_reading.md`, on the L2 reading file's section shape: §0 to §5 written in
the skeleton; §6 one subsection per tabulated member, each with its manifest header, its rows, its *not a statement* list,
its arithmetic, its distribution and its marks; §10 to §13 updated in each member's commit; §7, §8, §9 and §14 headed NOT
YET WRITTEN; §15 NOTHING; §16 what the file does not do.

| Commit | Parent | Subject (exactly) |
|---|---|---|
| `13380cf1603132da5780abe86ba1169797e75d49` | `966786b8…` | comparison L3: the reading file opened, its population, unit and vocabulary stated, nothing tabulated |
| `69b3c439c1ab918e0a5b57be4ea11af2bc77bb35` | `13380cf1…` | comparison L3: member 1 tabulated - 43 outgoing statements placed, proposals only |
| `480d4ab090be13c6dc71714086d0587cd0fa59ea` | `69b3c439…` | comparison L3: member 2 tabulated - 34 outgoing statements placed, proposals only |
| `2b49b0e87004aa371f4bff8b792c16d59aed5f36` | `480d4ab0…` | comparison L3: member 3 tabulated - 21 outgoing statements placed, proposals only |
| `35a98b2c0ad1510b3259eb504b774d0c803dc722` | `2b49b0e8…` | comparison L3: member 4 tabulated - 34 outgoing statements placed, proposals only |
| `fb20eded3686934d0ca02d51b540b99ce4e28aca` | `35a98b2c…` | comparison L3: member 5 tabulated - 19 outgoing statements placed, proposals only |
| `1dc893cfdc43f35a1ec7a9711f5a27b9c843d57c` | `fb20eded…` | comparison L3: member 6 tabulated - 10 outgoing statements placed, proposals only |

*(The integers in the subjects are the dispatch's ordered `<n>` — each member's statement count from its own manifest
header — and the subjects carry them as 2(g) orders.)* Each commit carries the one path; each was verified at the object
(`changed_paths.py --commit`) and each push verified at `.git/refs/remotes/origin/master` with the file tools.

**How the marks were placed.** WITHHELD at the rows inside the item-4 homes the artifact names for members 2 and 3; the
homes of the SEEN identities were located at `tools/audit/decisions/backbone_decisions.json`, read from the committed blob
(the script is §7's); none of them lies in positions 1 to 6, and two of them (D-503, D-510) lie inside no member at all,
which §5 of the reading file records. L3-S4's §6 item 2 flag is carried at the one row that names L3-S4 (Row 4.23).

**E2 — MET for positions 1 to 6.** Each done member has its manifest; every outgoing statement has exactly one
disposition, or UNPLACED with what was read; every DIFFERS states its difference in both texts' own words and chooses
nothing; the marks are placed where they apply; the transfer list (§10), the audit questions (§11) and the proposals
(§12) are gathered; §0 is true of the file; no recommendation appears anywhere; A5 is verified at the objects in the
end-state portion of the close.

## 4. Task 3 — the close

**3(a) — the `STATUS.md` entries, first.** Four entries at the top: the close entry, which names this dispatch by its
file name and carries the moved `Last updated: ` prefix, then the entries for Task 2, Task 1 and Task 0, each saying
`Same dispatch`. All four are pointers to this report, with no figure restated. The prefix was removed from the
outgoing-population batch's close entry, and no other existing sentence was rewritten or removed. **None of the 26
ruled terms appears in the four entries.** A case-insensitive substring search of `STATUS.md` for all 26, run after the
entries were written, hit one line only: the standing *ARCHIVED 2026-08-17, THE SECOND ACT* paragraph, where `phrase`
matches inside *paraphrase*. **A finding, recorded rather than absorbed:** 3(a) suggests the wording *"the read-off
facts"*, and `read-off` is one of the 26 ruled terms. Writing it would have added a `STATUS.md` hit and moved the
population tool's `--check` beyond the one line move A2 names. So the entries use "the L3 comparison" and "the ruled
term list" only. This was the last write to `STATUS.md` in this batch.

**3(b) — the forward bound.** Read whole at the object `6e127d7a…:tools/audit/gen_status_batch_bound.py` (redirected to a
scratch file outside the repository and read there with the file tools); the working copy diffed empty against it at
boot. `BASE_COMMIT` is the last member commit of Task 2, `1dc893cf…`; its `STATUS.md` object is
`78068919b71a56a2e8340e9cef71c2a13478afb9`, the same blob at `6e127d7a…`, `b11054f2…`, `966786b8…`, `13380cf1…` and
`1dc893cf…` (established at `git rev-parse` of each). The re-aiming diff against `1dc893cf…`, whole:

```
diff --git a/tools/audit/gen_status_batch_bound.py b/tools/audit/gen_status_batch_bound.py
index 4ec072f48f..d6c087c612 100644
--- a/tools/audit/gen_status_batch_bound.py
+++ b/tools/audit/gen_status_batch_bound.py
@@ -1392 +1392,32 @@ OUT = os.path.join(HERE, "status_batch_bound.json")
-BASE_COMMIT = "a4604507486c392b63882e4446a41fdf80ef7e65"
+# ★ RE-AIMED 2026-10-18 by `cc_instruction_l3_comparison_tabulation_2026_10_18.md` Task 3, at its 3(b),
… (the 30 comment lines of the re-aiming block, stating the former value, the base commit's STATUS.md blob, the
   then-previous batch, the prefix adjustment and the nameless 2026-09-02 entries, on the shape every earlier block
   uses) …
+BASE_COMMIT = "1dc893cfdc43f35a1ec7a9711f5a27b9c843d57c"
@@ -1507 +1538,4 @@ BASE_COMMIT = "a4604507486c392b63882e4446a41fdf80ef7e65"
-PREVIOUS_BATCH_DISPATCH = "cc_instruction_l3_keyword_count_2026_10_17.md"
+# *(`PREVIOUS_BATCH_DISPATCH` read "cc_instruction_l3_keyword_count_2026_10_17.md" while
+# `cc_instruction_l3_outgoing_population_2026_10_18.md` was the executing act; it is re-stated here for
+# `cc_instruction_l3_comparison_tabulation_2026_10_18.md`, whose then-previous batch is that one.)*
+PREVIOUS_BATCH_DISPATCH = "cc_instruction_l3_outgoing_population_2026_10_18.md"
@@ -1638,0 +1673,4 @@ PREVIOUS_BATCH_DISPATCH = "cc_instruction_l3_keyword_count_2026_10_17.md"
+# *(`ACT_DATE` read "2026-10-18" and `DISPATCH` `cc_instruction_l3_outgoing_population_2026_10_18.md`
+# while that batch was the executing act; both are re-stated here for
+# `cc_instruction_l3_comparison_tabulation_2026_10_18.md`, dated 2026-10-18, whose move ran on
+# 2026-10-18, so the two dates agree and `ACT_DATE` keeps its value.)*
@@ -1640 +1678 @@ ACT_DATE = "2026-10-18"
-DISPATCH = "cc_instruction_l3_outgoing_population_2026_10_18.md"
+DISPATCH = "cc_instruction_l3_comparison_tabulation_2026_10_18.md"
@@ -1793,2 +1831,5 @@ DISPATCH = "cc_instruction_l3_outgoing_population_2026_10_18.md"
-# names in those words.)*
-TASK = "Task 2"
+# names in those words. It names Task 3 while `cc_instruction_l3_comparison_tabulation_2026_10_18.md`
+# is the executing act, that dispatch ordering both halves of the close — this batch's own entries at
+# its 3(a) and this move at its 3(b) — inside its own Task 3, which that dispatch's heading *"Task 3 —
+# the close"* names in those words.)*
+TASK = "Task 3"
@@ -2310,0 +2352,4 @@ PREVIOUS_AIMINGS = [
+    {"executing_act": "cc_instruction_l3_comparison_tabulation_2026_10_18.md, Task 3",
+     "base_commit": "1dc893cfdc43f35a1ec7a9711f5a27b9c843d57c",
+     "the_then_previous_batch": "cc_instruction_l3_outgoing_population_2026_10_18.md",
+     "the_kind_of_move": "ordinary"},
```

*(The 30 comment lines are elided here as the edit-3 block is above; the command reproduces them.)* `MOVE_KIND` stays
`ordinary`; the outgoing population's aiming was already the last row and was not appended twice. No function and no
existing row was touched.

`python tools/audit/gen_status_batch_bound.py --apply` (exit 0), whole:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 3, 2,820 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

and `--check` (exit 0), whole:

```
  entries moved: 3, 2,820 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**The prediction HELD, read at the artifact rather than at the green `--check` (OI-379).**
`tools/audit/status_batch_bound.json` → `the_moved` names, by their openings, exactly the outgoing-population batch's
three entries:

- its close entry, the one naming `cc_instruction_l3_outgoing_population_2026_10_18.md` as Task 2, the close. Its
  membership is *names the dispatch*, and the one declared prefix adjustment was applied to it.
- its Task 1 entry, *THE L3 OUTGOING POPULATION DERIVED AND MEASURED*.
- its Task 0 entry, *THIS DISPATCH, THE L3 KEYWORD-LIST RULING RECORD AND HANDOFF ENTRIES 423 AND 424 ARE LANDED*.

The membership of the last two is *says `Same dispatch`*. The two 2026-09-02 entries stayed in `STATUS.md` and were not
moved by hand.

**3(c) — the regenerations.** After (a) and (b), each `--check` A2 names, whole:

```
== gen_evidence_pin_membership.py
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
exit:0
== gen_l0_l1_outgoing_population.py
l0_l1_outgoing_population.json re-derives
exit:0
== gen_defense_share.py
STALE vs the measurement: defense_share.json does not re-derive
exit:1
== gen_l3_outgoing_population.py
STALE vs the derivation: l3_outgoing_population.json does not re-derive
exit:1
== gen_session_start_read_size.py
STALE vs the measurement: session_start_read_size.json does not re-derive
exit:1
```

The evidence-pin membership stayed green, since no ruling record landed, and the L0/L1 population stayed green; neither
was regenerated. The three reds are A2's, caused by this batch's `STATUS.md` acts. Each was regenerated, the read size
last after the final `STATUS.md` edit, and each `--check` was re-run: **all three exit 0**, re-deriving (the tools'
output is in the scratch log and quoted in the end-state portion's verdicts). What each changed, between the Task 1
commit's blob and the regenerated blob written into the object store:

```
diff --git a/35705d0d4f4ba09a4122d30ca4ccfe0be40208a9 b/ecd0557264e3747b92c5a1ce68b09e2dbdebaa6a
@@ -80 +80 @@
-  "the_whole_ordinary_session_start_read": 248528,
+  "the_whole_ordinary_session_start_read": 248739,
diff --git a/13d1750be95ecdcf408405ff7d6f67bba8db1dfe b/e367d718f75e48cba3518e9f3777fc2516ac339f
@@ -20126 +20126 @@
-       "line_number": 20,
+       "line_number": 22,
diff --git a/398ecab8f7ca63f413e48f2501a359688f9dd9eb b/d7bbb42e39478de2e0ece7416c262a3a46faf83b
@@ -179 +179 @@
-   "STATUS.md": 12099,
+   "STATUS.md": 12310,
@@ -183 +183 @@
-  "total_characters": 248528,
+  "total_characters": 248739,
@@ -279 +279 @@
-   "to_total": 248528,
+   "to_total": 248739,
@@ -281,2 +281,2 @@
-   "change_in_characters": -118593,
-   "change_percent": -32.3,
+   "change_in_characters": -118382,
+   "change_percent": -32.25,
@@ -290 +290 @@
-   "to_total": 248528,
+   "to_total": 248739,
@@ -292,2 +292,2 @@
-   "change_in_characters": -48304,
-   "change_percent": -16.27,
+   "change_in_characters": -48093,
+   "change_percent": -16.2,
```

- **`tools/audit/l3_outgoing_population.json`** — **one residue hit record moved line, named:** `STATUS.md`'s record at
  `item_3_the_term_search` → `the_residue_for_the_mining_map` → `files` → `STATUS.md` → `hit_records`, the *paraphrase*
  line of the *ARCHIVED 2026-08-17, THE SECOND ACT* paragraph. It moved two lines, because four entries came in and three
  went out. **No member of `the_population`, no item-4 passage and no member of `the_tabulation_population` moved.**
- **`tools/audit/defense_share.json`** — the whole-read denominator only.
- **`tools/audit/session_start_read_size.json`** — `STATUS.md`'s size and the totals and comparisons computed from it.

**E3 — derived from the declared start state plus this batch's footprint (P-3):** at the tree carrying the close, every
`--check` A2 names is green, and the failing set is exactly the thirteen. The end-state run confirms it, and the close
section's end-state portion records that run.

## 5. A1 to A5, graded

- **A1 — HELD, BY CONTENT** (§1, 0(c)). During the run no further handoff entry or ruling record appeared. The
  enumeration after the close's acts shows the close's eight paths as modifications and A1's one, and nothing else
  tracked.
- **A2 — HELD AT THE START** (§1, 0(f)), and **at the close** every red it names was met and regenerated or stayed green
  (§4, 3(c)). The end prediction is carried by the end-state run.
- **A3 — HELD.** `tools/audit/gen_l2_outgoing_population.py` was not run in any operating mode. It was imported by the
  amended tool, which executes its module level and never its `derive()`. Its artifact was not touched. It is verified at
  the objects in the end-state portion.
- **A4 — HELD.** No tool was added and none enrolled. `tools/audit/gen_guard_state.py` was not edited. Exactly two tool
  sources were touched: `tools/audit/gen_l3_outgoing_population.py` (Task 1) and the authored aiming of
  `tools/audit/gen_status_batch_bound.py` (Task 3).
- **A5** — verified at the objects after the last commit, in the end-state portion of the close
  (`git diff --name-status 6e127d7a… <close>`).

## 6. Declared departures

1. **The ordered first read was not the very first read.** To learn the order I had to read the dispatch's first page,
   which carries its own outgoing-text framing (the ruling ledger and `FRAMEWORK.md` §5's L3 block quoted). **In the
   same parallel call I also read `STATUS.md` before the derivation.** The derivation was then read §5, then §6, then §7,
   then whole, before any other read of this session. `STATUS.md`'s content carries no L3 outgoing text. The breach is
   stated rather than argued away; Ruling 2's ordering was not met for that one file.
2. **The dispatch was read from the working tree before it was pinned.** This is standing clause P-2's fallback route,
   since the opening line named only the file. It was pinned at Task 0 and proved unmoved before staging.
3. **One shell command in 0(b) carried commit hashes in a loop variable** (`for c in …; do git show --stat … $c`),
   where the dispatch says to write every hash literally. The guard admitted it. Every later command named its hashes
   literally, except the Task 2 commit verification, which iterated the same way over seven literal hashes.
4. **One interpreter command was denied by the guard**: a `python -c` naming `tools/audit/derivation_boot_pack.json`.
   It read nothing. The pack was then read with the file tools.
5. **`BUILD_AND_TEST.md` was read at its Git Bash section and its headings, and searched for the guard commands.** It was
   not read whole. The conditional read's purpose — the commands this batch runs — is carried by the dispatch itself.
6. **The model reading file was read slightly beyond the ordered extent**: member 1's foot (its arithmetic and marks
   blocks), to follow the shape of a member's close.
7. **`records/cowork/handoff/cowork_away_returns.md` was read at the previous batch's two appended portions**, at the
   objects `affc956b…` and `6e127d7a…`, because Task 3(e) writes into that file and the shape is that batch's.
8. **Scratch scripts were run with `python -I`.** One of them first failed on its own output encoding (a `★` in a key
   path under the cp1252 console) and was re-run with UTF-8 output; it reads only blobs and writes nothing.
9. **Each commit message carries one trailer line after the ordered subject**, the co-author attribution this session's
   instructions require, as a second paragraph. The subject lines are exactly the ordered ones.
10. **Two diffs are shown in this report with a declared elision** (the edit-3 block and the forward bound's 30 comment
    lines). Each is reproducible by the command stated with it.
11. **Task 2 stopped at the member boundary after position 6** by the capacity judgment stated at the head of this
    report. That is the dispatch's own provision, recorded here as well as in §0 of the reading file.

## 7. The scripts, whole

The Task 0(d) script, `t0_lastbytes.py`:

```python
"""Task 0(d): measure each landed file at its git OBJECT -- size, zero bytes, last 70 bytes, last line."""
import subprocess

REPO = r"C:\s\MS"
BLOBS = [
    ("records/cc/instructions/cc_instruction_l3_comparison_tabulation_2026_10_18.md",
     "db7afc92d1dbd4e7b76a297ed1c1c6070a839f64"),
    ("records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_five.md",
     "357da38fbbbbd7e81b9d5179db0826aa841cf817"),
]
for path, blob in BLOBS:
    data = subprocess.run(["git", "cat-file", "blob", blob], cwd=REPO,
                          capture_output=True, check=True).stdout
    text = data.decode("utf-8")
    lines = text.split("\n")
    last = lines[-2] if text.endswith("\n") else lines[-1]
    print("==", path)
    print("   blob", blob, " size", len(data))
    print("   zero bytes:", data.count(b"\x00"))
    print("   ends with a newline:", text.endswith("\n"))
    print("   last line:", last)
    print("   last 70 bytes:", data[-70:])
```

The Task 1(b) script, `t1b_synthetic.py`:

```python
"""Task 1(b): the four imported functions on synthetic lines, through the AMENDED module's names.
Reads no repository file beyond importing the tools; writes nothing."""
import sys

sys.path.insert(0, r"C:\s\MS\tools\audit")
from gen_l3_outgoing_population import fence_ranges, block_around, merge_ranges, subtract_spans

lines = ["# H", "", "a", "b", "", "```", "x", "```", "c"]
checks = [
    ("fence_ranges(lines)", fence_ranges(lines), [(6, 8)]),
    ("block_around(lines, 4, [(6, 8)])", block_around(lines, 4, [(6, 8)]), (3, 4)),
    ("block_around(lines, 7, [(6, 8)])", block_around(lines, 7, [(6, 8)]), (6, 8)),
    ("block_around(lines, 1, [(6, 8)])", block_around(lines, 1, [(6, 8)]), (1, 4)),
    ("block_around(lines, 9, [(6, 8)])", block_around(lines, 9, [(6, 8)]), (9, 9)),
    ("merge_ranges([(5, 7), (1, 2), (3, 3), (9, 9)])",
     merge_ranges([(5, 7), (1, 2), (3, 3), (9, 9)]), [(1, 3), (5, 7), (9, 9)]),
    ("subtract_spans([(1, 10)], [(4, 5), (8, 8)])",
     subtract_spans([(1, 10)], [(4, 5), (8, 8)]), [(1, 3), (6, 7), (9, 10)]),
]
ok_all = True
for expr, got, want in checks:
    ok = got == want
    ok_all = ok_all and ok
    print("%s  %s == %r  (got %r)" % ("HELD  " if ok else "FAILED", expr, want, got))
print("ALL SEVEN HELD" if ok_all else "NOT ALL HELD")
sys.exit(0 if ok_all else 1)
```

The Task 1(c) comparison script, `t1c_compare.py`:

```python
"""Task 1(c): compare the committed artifact blob with the new one, recursively, by key path.
Both are read from the object store by explicit blob hash.  Writes nothing."""
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

REPO = r"C:\s\MS"
OLD = "92ef966cb03caca4be8288522c423b20ac1aceb5"
NEW = "13d1750be95ecdcf408405ff7d6f67bba8db1dfe"


def load(blob):
    data = subprocess.run(["git", "cat-file", "blob", blob], cwd=REPO,
                          capture_output=True, check=True).stdout
    return json.loads(data.decode("utf-8"))


old, new = load(OLD), load(NEW)
changed, missing, added = [], [], []


def walk(o, n, path):
    if isinstance(o, dict) and isinstance(n, dict):
        for k in o:
            if k not in n:
                missing.append(path + (k,))
            else:
                walk(o[k], n[k], path + (k,))
        for k in n:
            if k not in o:
                added.append(path + (k,))
        return
    if o != n:
        changed.append(path)


walk(old, new, ())
fmt = lambda p: " -> ".join(p)
print("key paths of the old artifact MISSING from the new:", len(missing))
for p in missing:
    print("   ", fmt(p))
print("key paths whose value CHANGED:", len(changed))
for p in changed:
    print("   ", fmt(p))
print("key paths ADDED in the new (topmost added keys only):", len(added))
for p in added:
    print("   ", fmt(p))
for key in ("the_population", "the_residue_for_the_mining_map"):
    same = json.dumps(old["item_3_the_term_search"][key], ensure_ascii=False, sort_keys=True) == \
        json.dumps(new["item_3_the_term_search"][key], ensure_ascii=False, sort_keys=True)
    print("item_3_the_term_search ->", key, "identical:", same)
same = json.dumps(old["item_4_the_decision_passages"]["the_passages"], ensure_ascii=False,
                  sort_keys=True) == json.dumps(new["item_4_the_decision_passages"]["the_passages"],
                                                ensure_ascii=False, sort_keys=True)
print("item_4_the_decision_passages -> the_passages identical:", same)
```

The Task 1(d) order script, `t1d_order.py`, printed each member's position, kind, document, label, line and byte sizes,
range count, item-3 hit lines and item-4 identities from the new artifact's blob `13d1750b…`, and the measured-size
block. Its output is the artifact's own `the_members` and `the_measured_size` → `the_tabulation_population`, which are
pointed at and not restated (**D-431**).

The Task 2(c) SEEN-homes script, `t2_seen_homes.py`, read `tools/audit/decisions/backbone_decisions.json` and the new
artifact from the commit `966786b8…` (`git show <commit>:<path>`). For each of D-482, D-484, D-335, D-406 and D-502 to
D-510 it tested the home against every member's ranges. Its result is written into §5 of the reading file: D-482 and
D-484 in member 36, D-335 in member 7, D-406 in member 46, D-502 and D-504 to D-509 in member 44, and D-503 and D-510 in
no member.

## 8. Observations, recorded and not acted on

1. **The finding of §4, 3(a)**: the dispatch's suggested `STATUS.md` wording *"the read-off facts"* carries the ruled term
   `read-off`. It was not used.
2. **For position 10 (`cowork_layer4_chordsymbol_design.md`), the member's `bytes` and the same file's `bytes` at
   `the_distinct_names` differ by its line count.** The member's size is computed over lines joined by a line feed; the
   distinct-names size is the file's size on disk, whose working copy carries carriage-return line feeds. This is a
   difference of counting convention, not of content. Nothing was acted on.
3. **Position 34 (`ARCHITECTURE.md` passages under *Appendix B*) is a few lines carrying a large byte count** at the
   artifact. One very long line explains it, and nothing was acted on.
4. **A substantial share of positions 1 to 6 places UNPLACED** where a rule on L3's own subject differs from a derived
   statement. The share is countable at §13. The file states the reason at each such row: choosing ADOPTED — proposed
   there would choose between the texts. This records how the honest default was applied, not a verdict.
5. **The classification tool's message is unchanged**, still naming the four tools without an authored verdict.
   Authoring one is not this batch's act.

## 9. What this batch did not do

Nothing was decided, and no disposition was applied anywhere. Every placement in the reading file is a proposal. No
outgoing text was edited. The derivation, the brief, the pack directory, the pack's artifact, the two input-contract
files, and the L0/L1 and L2 reading files were not edited. No session was booted, and no measurement of the analysis was
built, designed, scoped or run. No tool source was touched beyond the two A4 names. `gen_l2_outgoing_population.py` was
imported and never run, and its artifact is untouched. No open-items row was created, flipped or discarded. No
decisions-register entry and no `D-NNN` were allocated, and nothing was written into the suspension file. No ruling was
taken, nothing was put to the user, and no recommendation was made about the derivation, the method or any open question.
The five ★ questions (OQ-L3-2, 3, 6, 8 and 10) were not put. No `src/` file, build, test, golden, corpus of scores or
anything under `tools/corpus/`, `tools/robust_stop/` or `tools/dcml/` was touched. No residue file and none of the four
LISTED item-2 documents was dispositioned.

## 10. The plan's tell, in one sentence

This batch produced nothing other than the two landed records, the amended population tool and its artifact, the reading
file, the close's files (`STATUS.md`, `STATUS_ARCHIVE.md`, the re-aimed forward bound and its artifact, and the three
regenerated artifacts) and this report.

## 11. Self-check (D-434) — the standing check over this batch's own work

1. **The guiding principles.** #6 — the passage rule's four functions and `TOP_LEVEL` are imported, not copied, and the
   one re-authored block (edit 3) is the dispatch's declared copy. #12 — every hit line and every item-4 home lies in
   exactly one member, proved by the tool's STOP; the residue and the four LISTED names stay published; UNPLACED and
   SILENT stand beside ADOPTED; the forward bound moved its entries byte-faithfully. #19 — the reading file establishes
   nothing, and every row can be re-placed at the two quoted texts. #24 — no difference between two measured quantities
   is asserted. #13 — no surprise was built around: the denied interpreter read was rerouted, the scratch script's
   encoding failure was fixed in the script and not in a tool, and the ruled-term clash in 3(a) is reported.
2. **The conventions.** American English. The disposition words are the phase definition's and the verdict words the
   comparison-design sitting's; the charter names are `FRAMEWORK.md` §5's. *Score* is the music only, *key* tonality
   only, *bar* the metric unit, *note* a pitch event, *measurement* the gauging sense, and a quantity is a *value* or a
   *count*. No numeric grade appears in the reading file. The ruled terms appear in `STATUS.md`'s new entries nowhere.
3. **The figures-and-premises rule (D-431).** No value from the population artifact or the reading file is restated in
   prose. The tools' printed output and the diffs are quoted verbatim. Every premise was checked at its object: the ref
   files, the blobs, `git rev-parse`, the artifacts and the register's data file.
4. **The file-tools rule (D-253).** Working-tree content was read with the file tools. The shell ran git object queries
   by explicit hash, `git add`, `commit` and `push` by explicit path, the sanctioned tools, and scratch scripts outside
   the repository reading blobs. Each command carried `; echo "exit:$?"` and redirected its output to the scratch folder.
5. **Uncertainty on any comparison (#24).** None is asserted.

**The diffs of every touched file were re-read before this report was written:** the tool against the dispatch's six
edits; the artifact by the key-path comparison; the reading file member by member, its row counts grepped against the
manifests and every quotation checked against the text it quotes; `STATUS.md` (four entries and the moved prefix);
`STATUS_ARCHIVE.md` (the archive header and the three moved entries); the forward-bound aiming; and the three
regenerated artifacts (the moves A2 names only). Three slips were found and corrected before their commits:

- a bracketed alteration inside a quotation;
- two derivation quotations joined as if they were one;
- the §6 item 2 flag missing at the one row that names L3-S4.

No violation remains that I know of.

*Provenance: CC, 2026-10-18, at boot tip `6e127d7a94d4e3f4dbdd7858bd39fef54992b712`, under
`cc_instruction_l3_comparison_tabulation_2026_10_18.md`. Every commit identifier here was read from the commit's own
object, and `origin/master` at its ref file after each push; the guard verdicts are this batch's own runs.*
