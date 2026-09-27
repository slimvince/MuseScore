# CC REPORT — THE L2 BRIEF LANDING (2026-09-27)

> Executes `records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md`, pinned at blob
> `8629059a304c29c269fd1ec5b1be5b5e1197ce1a` (29,597 bytes). Every task ran in order. **No STOP fired.**
> Captures and scripts were kept outside the repository working tree, in this session's scratchpad
> directory, written below as `scratchpad/…`
> (`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\4a91357d-7bb7-4d4b-972e-e158b106dfd2\scratchpad\`).
> The session-start reads were performed before the dispatch was acted on: the gating row identities,
> `STATUS.md` and the head of the `DECISIONS.md` index.

---

## 1. Task 0 — the start state, and the uncommitted records committed

**0(a) — the pin.** `git hash-object -w records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md`
→ `8629059a304c29c269fd1ec5b1be5b5e1197ce1a`; `git cat-file -s` → `29597`. The later
`git hash-object -w --no-filters` of the same path gave the same identity, and the committed index
entry carries it.

**0(b) — the refs**, read with the file tools:
`.git/refs/heads/master` = `84ab3a5c404bf9953a568df7c0c57022dba06f8f`;
`.git/refs/remotes/origin/master` = `84ab3a5c404bf9953a568df7c0c57022dba06f8f`. **They agree, at the
expected value.**

**0(c) — the working tree.** `python tools/audit/changed_paths.py`, exit 0, captured whole at
`scratchpad/cp0.txt` (402 records). The records other than the 387 untracked paths under
`scratch_artifacts/`, verbatim:

```
 M	records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	cowork_blind_session_brief_l2.md
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_four.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_three.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_two.md
??	records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md
…  (387 `??	scratch_artifacts/…` records, listed whole in the capture)
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
402 changed path record(s) [worktree]
```

**Nothing was staged**: every record's index column is blank (` M`) or untracked (`??`).

The last bytes of every text file 0(d) commits were read from its git object (`git cat-file -p <blob>`,
last 120 bytes, and the count of zero bytes in the last eight). **No file ends in a NUL byte, and every
one ends with a complete line and a newline.**

**0(d) — the commit of the interim carriers.** Each size by `git hash-object -w --no-filters` then
`git cat-file -s`:

| # | path | blob | size | stated |
|---|---|---|---|---|
| 1 | `records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md` | `8629059a304c29c269fd1ec5b1be5b5e1197ce1a` | 29597 | the 0(a) pin |
| 2 | `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md` | `b81b79a200a43b3c64eb7be6201fb2b2a7d48cb3` | 6212 | 6,212 ✓ |
| 3 | `records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md` | `b9a97269fbf327248fd69c8fb676204839dddcd3` | 6716 | 6,716 ✓ |
| 4 | `cowork_blind_session_brief_l2.md` | `686ca735ab550fadb81ac7a4719e24b1a204c32f` | 35582 | 35,582 ✓ |
| 5 | `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_two.md` | `bf0ea2afca3cbc6091478e9e85a13bddf8ce3cff` | 6552 | 6,552 ✓ |
| 5 | `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_three.md` | `5a2bdc1c20728d82a4413d35c10447b14487c30c` | 6627 | 6,627 ✓ |
| 6 | `records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md` | `791aaf6e76b9b67c48aa7bf0bd401a2c4c7e0c1c` | 71202 | 71,202 ✓ (reported modified) |
| 8 | `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_four.md` | `49766e0edededc561760a1716f039d1f6ea64a96` | 5713 | none stated; it exists |

**Item 7, `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_one.md`, was NOT
committed**: 0(c) does not report it, so it is tracked and unchanged.

**Held back and reported** (reported by the enumeration, named by no commit of this batch):
`tools/audit/claude_md_finer_archive.json` (B9), `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`
(untracked, present before this batch), and every other untracked path listed above.

The staged set, proved before committing (`git diff --cached --name-status`, then `git ls-files -s`
of the eight paths):

```
A	cowork_blind_session_brief_l2.md
A	records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md
M	records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_four.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_three.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_two.md
A	records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md
---
100644 686ca735ab550fadb81ac7a4719e24b1a204c32f 0	cowork_blind_session_brief_l2.md
100644 8629059a304c29c269fd1ec5b1be5b5e1197ce1a 0	records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md
100644 791aaf6e76b9b67c48aa7bf0bd401a2c4c7e0c1c 0	records/cc/reports/cc_report_l2_pack_build_second_half_2026_09_27.md
100644 49766e0edededc561760a1716f039d1f6ea64a96 0	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_four.md
100644 5a2bdc1c20728d82a4413d35c10447b14487c30c 0	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_three.md
100644 bf0ea2afca3cbc6091478e9e85a13bddf8ce3cff 0	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_two.md
100644 b9a97269fbf327248fd69c8fb676204839dddcd3 0	records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md
100644 b81b79a200a43b3c64eb7be6201fb2b2a7d48cb3 0	records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md
```

Exactly the eight paths, each at the blob measured above. **The commit:
`9378e95a7d620fca6ebd28119d4d1bb6483f9d66`** (parent `84ab3a5c404bf9953a568df7c0c57022dba06f8f`),
"Task 0: land the interim carriers of the 2026-09-27 leak-list and brief sittings", 8 files, 1497
insertions. Not pushed at that point.

**0(e) — THE OPENING GUARD CAPTURE**, taken after the commit: `python tools/audit/gen_guard_state.py`,
exit 0, captured at **`scratchpad/guard_open.txt`**. Every verdict, verbatim:

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
  [FAIL] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [PASS] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --check
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
79 guard(s) run, 13 failing, 4 not run, 19 historical record(s)
```

The previous batch's close capture read 12 failing; the thirteenth here is
`gen_evidence_pin_membership.py --check`, and its cause is established at 5(c): the two ruling records
Task 0 committed had not yet been read into that tool's artifact.

`python tools/audit/gen_guard_classification.py`, run separately after it
(`scratchpad/guardclass_open.txt`), exit 2, as expected (B8) — **carried, not chased**:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

## 2. Task 1 — the pack re-derives at the untouched tree

**(a)** `python tools/audit/gen_derivation_boot_pack.py --check`, exit 0, verbatim:

```
FROZEN SOURCES: 15 of 21 frozen pack file(s) would render at a different length from the sources as they stand today. NOT COMPARED; sets no exit code.
  - harmony-boundary/02_the_guiding_principles_and_the_conventions.md: the directory holds 59762 characters; today's sources would render 66702
  - harmony-boundary/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - harmony-boundary/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - harmony-boundary/05_the_ratified_design_intent.md: the directory holds 252572 characters; today's sources would render 252641
  - l0-l1/02_the_guiding_principles_and_the_conventions.md: the directory holds 61113 characters; today's sources would render 67476
  - l0-l1/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - l0-l1/04_the_dispatch_protocol.md: the directory holds 103431 characters; today's sources would render 108389
  - l0-l1/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
  - l0-l1/07_the_charter_the_layers_and_the_decisions.md: the directory holds 29031 characters; today's sources would render 33067
  - l0-l1/08_the_five_research_extracts.md: the directory holds 76722 characters; today's sources would render 99171
  - l0-l1/09_the_empirical_findings_ledger.md: the directory holds 50666 characters; today's sources would render 50963
  - scoring-model/02_the_guiding_principles_and_the_conventions.md: the directory holds 60536 characters; today's sources would render 67476
  - scoring-model/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - scoring-model/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - scoring-model/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
the derivation boot pack re-derives
  harmony-boundary: FROZEN — 7 file(s) at their recorded blobs
  l0-l1: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
exit:0
```

**Read as the expected result, and the reading is stated.** The dispatch's expected lines — `the
derivation boot pack re-derives`, three `FROZEN` lines, exit 0 — all appear. The `FROZEN SOURCES` block
before them is the tool's standing advisory, which "sets no exit code" and which
`cc_instruction_boot_pack_frozen_manifest_2026_09_20.md` requires to print on every `--check` run; it is
**line-for-line identical** to the block the previous batch recorded at its own Task 1(a)
(`cc_report_l2_pack_build_second_half_2026_09_27.md` §2). So it was not treated as an inherited STOP.

**(b)** `git hash-object tools/audit/gen_derivation_boot_pack.py` =
`9c3c78fcbd89dcf34f303881451610049cbdb6e9`; `git hash-object tools/audit/derivation_boot_pack.json` =
**`3fa7d30c67f63f3efd660dfd4f6c0e7dc3cf881a`** (Task 3(c)'s before-side).

## 3. Task 2 — Ruling 1 of the leak-list sitting, in the generator

Each OLD text was searched before replacement and occurred **exactly once** (lines 6034–6036, 6043,
6376, 6545–6550 and 6675–6676 of the untouched tool). Before 2(a) was applied it was checked that
`cross_reference_additions` has one caller only (line 6376), and that both the 2(c) and the 2(d) sites
lie inside `build_subject(subject, …)`, where `subject` is in scope; `FROZEN` is the module-level dict
at line 361.

**2(f) — the diff**, `git diff 9c3c78fcbd89dcf34f303881451610049cbdb6e9 13f87585a8d45cbf18d65a336969ca60cf20be39`,
verbatim (`scratchpad/t2_diff.txt`):

```diff
diff --git a/9c3c78fcbd89dcf34f303881451610049cbdb6e9 b/13f87585a8d45cbf18d65a336969ca60cf20be39
index 9c3c78fcbd..13f87585a8 100644
--- a/9c3c78fcbd89dcf34f303881451610049cbdb6e9
+++ b/13f87585a8d45cbf18d65a336969ca60cf20be39
@@ -6031,16 +6031,28 @@ def criterion_block(subject: str) -> tuple[str, dict]:
     )
 
 
+# ── the fields the cross-reference rule searches ───────────────────────────────────────────────
+# Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md`: for every
+# subject that is NOT FROZEN the rule searches only the fields member (5) renders besides the
+# identifier — `title`, `verbatim`, `plain`.  A FROZEN subject keeps the five-field search its pack
+# was built under, so that its manifest record — the record of what its session was given — does not
+# move; the same scoping as limb B's `extras_leaks` in `build_subject` (D-657).
+XREF_FIELDS_FROZEN = ("title", "verbatim", "plain", "rationale", "status_source")
+XREF_FIELDS = ("title", "verbatim", "plain")
+
+
 def cross_reference_additions(authored: set[str], docs: set[str],
-                              design_intent: list[dict], backbone: dict) -> list[dict]:
-    """Every DESIGN-INTENT entry that quotes or cross-references a withheld identity or document."""
+                              design_intent: list[dict], backbone: dict,
+                              searched: tuple[str, ...]) -> list[dict]:
+    """Every DESIGN-INTENT entry that quotes or cross-references a withheld identity or document,
+    in the fields `searched`."""
     adds = []
     for e in design_intent:
         eid = e["id"]
         if eid in authored:
             continue
         bb = backbone.get(eid, {})
-        fields = haystack(e, bb, ("title", "verbatim", "plain", "rationale", "status_source"))
+        fields = haystack(e, bb, searched)
         hits = []
         for field, value in fields.items():
             for other in sorted(authored):
@@ -6373,7 +6385,8 @@ def build_subject(subject: str, sort_entries: list[dict], backbone: dict) -> tup
     docs = set(authored.get("withheld_documents", {}))
 
     # ── the derived cross-reference additions ────────────────────────────────────────────────
-    adds = cross_reference_additions(authored_ids, docs, design_intent, backbone)
+    adds = cross_reference_additions(authored_ids, docs, design_intent, backbone,
+                                     XREF_FIELDS_FROZEN if subject in FROZEN else XREF_FIELDS)
     withheld_ids = authored_ids | {a["id"] for a in adds}
 
     # ── member (5): the cut, then the leak check ─────────────────────────────────────────────
@@ -6547,7 +6560,16 @@ def build_subject(subject: str, sort_entries: list[dict], backbone: dict) -> tup
                     "CROSS-REFERENCES a withheld identity or names a withheld document, added to "
                     "the withheld set by the derivation rather than by hand. The fields searched "
                     "include `rationale` and `status_source`, which the pack does not render — a "
-                    "cross-reference in either is still a route to the withheld material."),
+                    "cross-reference in either is still a route to the withheld material.")
+                if subject in FROZEN else (
+                    "Entries of the DESIGN-INTENT class whose own text QUOTES OR "
+                    "CROSS-REFERENCES a withheld identity or names a withheld document, added to "
+                    "the withheld set by the derivation rather than by hand. The fields searched "
+                    "are `title`, `verbatim` and `plain` — the fields member (5) renders besides "
+                    "the identifier (Ruling 1 of "
+                    "`cowork_rulings_2026_09_27_l2_leak_list_sitting.md`); `rationale` and "
+                    "`status_source`, which the pack does not render, are not searched for this "
+                    "subject."),
                 "★_the_bound": (
                     "ONE PASS, from the AUTHORED identities only. It is NOT transitive: an entry "
                     "that cross-references one of these additions rather than an authored "
@@ -6673,6 +6695,9 @@ def build() -> tuple[dict, dict[str, dict[str, str]], list[dict]]:
             "Ruling 1 of `cowork_rulings_2026_09_21_l2_extracts_member_cutting_sitting.md` — the "
             "`l2` extracts member cut per file by the text of each cut section's heading (limb A), "
             "with a derived leak check over the extras beside it (limb B).",
+            "Ruling 1 of `cowork_rulings_2026_09_27_l2_leak_list_sitting.md` — the cross-reference "
+            "rule searches only the fields member (5) renders, for every subject that is not "
+            "FROZEN.",
         ],
         "★_it_boots_no_session": (
             "Rendering the pack is not opening it. Nothing here derives a specification "
```

Exactly the five replacements and nothing else.

## 4. Task 3 — the render, and the proof that only what the ruling names moved

**3(a) — the render.** `python tools/audit/gen_derivation_boot_pack.py`, exit 0, verbatim:

```
wrote tools\audit\derivation_boot_pack.json
  harmony-boundary: design-intent 244 · candidates 75 · IN 16 / OUT 59 / UNPLACED 0
    withheld 33 (16 authored + 17 derived) · documents 1 · passages 2 · leaks 3
    rendered: 208 design-intent entries, 25 defect-type rows, 7 files
  l0-l1: design-intent 244 · candidates 0 · IN 0 / OUT 0 / UNPLACED 0
    withheld 0 (0 authored + 0 derived) · documents 0 · passages 0 · leaks 3
    rendered: 241 design-intent entries, 25 defect-type rows, 10 files
  l2: design-intent 244 · candidates 244 · IN 111 / OUT 133 / UNPLACED 0
    withheld 113 (111 authored + 2 derived) · documents 21 · passages 6 · leaks 2
    rendered: 129 design-intent entries, 25 defect-type rows, 10 files
  scoring-model: design-intent 244 · candidates 0 · IN 0 / OUT 0 / UNPLACED 0
    withheld 0 (0 authored + 0 derived) · documents 0 · passages 0 · leaks 3
    rendered: 241 design-intent entries, 25 defect-type rows, 7 files
```

**The `l2` line reads `IN 111 / OUT 133 / UNPLACED 0`, as required.** Before the render it was
confirmed at the tool that `write_all` skips every subject in `FROZEN` ("Nothing is written into a
spent subject's directory").

**3(b)** `--check`, exit 0, verbatim: the same sixteen-line `FROZEN SOURCES` block as Task 1(a), line
for line, then

```
the derivation boot pack re-derives
  harmony-boundary: FROZEN — 7 file(s) at their recorded blobs
  l0-l1: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
```

**3(c) — THE PROOF (D-657).** Script `scratchpad/t3c_proof.py`, not committed, verbatim:

```python
"""Task 3(c) proof (D-657): only what Ruling 1 of the leak-list sitting names moved."""
import json
import subprocess
import sys

REPO = r"C:\s\MS"
OLD_BLOB = "3fa7d30c67f63f3efd660dfd4f6c0e7dc3cf881a"  # Task 1(b)
NEW_PATH = REPO + r"\tools\audit\derivation_boot_pack.json"
ADDED = ("Ruling 1 of `cowork_rulings_2026_09_27_l2_leak_list_sitting.md` — the cross-reference "
         "rule searches only the fields member (5) renders, for every subject that is not "
         "FROZEN.")

old = json.loads(subprocess.run(["git", "-C", REPO, "show", OLD_BLOB], capture_output=True,
                                check=True).stdout.decode("utf-8"))
with open(NEW_PATH, encoding="utf-8") as fh:
    new = json.load(fh)

ok = True

# 1 — the three frozen subjects equal as parsed JSON
for s in ("harmony-boundary", "scoring-model", "l0-l1"):
    eq = old["subjects"][s] == new["subjects"][s]
    print(f"1. subjects[{s!r}] equal: {eq}")
    ok &= eq

# 2 — top-level keys and values
ko, kn = set(old), set(new)
print(f"2. top-level key sets equal: {ko == kn}")
ok &= ko == kn
for k in sorted(ko & kn):
    if old[k] == new[k]:
        continue
    if k == "the_rulings_it_executes":
        good = new[k] == old[k] + [ADDED]
        print(f"2. {k}: differs; new == old + [the one 2(e) string]: {good}")
        ok &= good
    elif k == "subjects":
        so, sn = set(old[k]), set(new[k])
        moved = sorted(s for s in so | sn if old[k].get(s) != new[k].get(s))
        good = so == sn and moved == ["l2"]
        print(f"2. subjects: differs; subject key sets equal: {so == sn}; subjects that differ: {moved}")
        ok &= good
    else:
        print(f"2. UNEXPECTED top-level difference at {k!r}")
        ok = False
for k in sorted(ko ^ kn):
    print(f"2. top-level key present in only one document: {k!r}")

# 3 — the l2 additions
adds = new["subjects"]["l2"]["THE_WITHHELD_FAMILY"]["derived_cross_reference_additions"]["additions"]
ids = sorted(a["id"] for a in adds)
print(f"3. new l2 additions: {ids}")
ok &= ids == ["D-406", "D-656"]
old_adds = old["subjects"]["l2"]["THE_WITHHELD_FAMILY"]["derived_cross_reference_additions"]["additions"]
print(f"   (old l2 additions, for the record: {len(old_adds)} entries)")

print("PROOF HOLDS" if ok else "PROOF FAILS")
sys.exit(0 if ok else 1)
```

Output, exit 0, verbatim:

```
1. subjects['harmony-boundary'] equal: True
1. subjects['scoring-model'] equal: True
1. subjects['l0-l1'] equal: True
2. top-level key sets equal: True
2. subjects: differs; subject key sets equal: True; subjects that differ: ['l2']
2. the_rulings_it_executes: differs; new == old + [the one 2(e) string]: True
3. new l2 additions: ['D-406', 'D-656']
   (old l2 additions, for the record: 91 entries)
PROOF HOLDS
```

**All three conditions hold**: the frozen subjects are equal as parsed JSON; the only top-level values
that differ are `the_rulings_it_executes` (the old list plus exactly the 2(e) string) and `subjects`
(differing only under `l2`); and the new `l2` additions are exactly `D-406` and `D-656`.

**3(d) — what moved in `l2`, read out of the two manifests and NOT reviewed** (the user's condition).
Script `scratchpad/t3d_read.py` (it prints the two `counted` objects and both `LEAKS.entries` lists;
first run failed on my script's own console encoding and was re-run with UTF-8 output). Verbatim:

```
BEFORE subjects.l2.counted:
{
  "design_intent_class": 244,
  "candidates": 244,
  "verdicts": {
    "IN": 111,
    "OUT": 133,
    "UNPLACED": 0
  },
  "withheld_identities_authored": 111,
  "withheld_identities_derived": 91,
  "withheld_identities_total": 202,
  "withheld_documents": 21,
  "withheld_passages": 6,
  "leaks": 0,
  "design_intent_entries_rendered": 42,
  "defect_type_rows_rendered": 25,
  "files_in_the_pack": 10,
  "extras_lines_with_a_leak_hit": 66
}
AFTER subjects.l2.counted:
{
  "design_intent_class": 244,
  "candidates": 244,
  "verdicts": {
    "IN": 111,
    "OUT": 133,
    "UNPLACED": 0
  },
  "withheld_identities_authored": 111,
  "withheld_identities_derived": 2,
  "withheld_identities_total": 113,
  "withheld_documents": 21,
  "withheld_passages": 6,
  "leaks": 2,
  "design_intent_entries_rendered": 129,
  "defect_type_rows_rendered": 25,
  "files_in_the_pack": 10,
  "extras_lines_with_a_leak_hit": 61
}
BEFORE subjects.l2.LEAKS keys: ['entries', '★_the_scope, stated because a scope that is not stated reads as total', '★_what_this_is']
BEFORE subjects.l2.LEAKS.entries:
[]
AFTER subjects.l2.LEAKS keys: ['entries', '★_the_scope, stated because a scope that is not stated reads as total', '★_what_this_is']
AFTER subjects.l2.LEAKS.entries:
[
  {
    "member": 5,
    "id": "D-296",
    "title": "READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits",
    "matched": [
      {
        "field": "verbatim",
        "kind": "a-docs-or-src-path",
        "matched": "src/notation"
      },
      {
        "field": "verbatim",
        "kind": "a-docs-or-src-path",
        "matched": "src/engraving"
      }
    ]
  },
  {
    "member": 5,
    "id": "D-440",
    "title": "The language-model integration is purpose-built and does not wait for the plugin-API reform",
    "matched": [
      {
        "field": "verbatim",
        "kind": "a-docs-or-src-path",
        "matched": "src/llm/"
      }
    ]
  }
]
```

**No per-entry review was performed on either.**

**3(e) — the `l2` pack directory.** Each file hashed with `git hash-object --no-filters` and compared
with its blob in `9378e95a7d…` (`git ls-tree -l`):

| file | bytes on disk | changed? |
|---|---|---|
| `00_READ_THIS_FIRST.md` | 3969 | no |
| `01_the_phase_definitions.md` | 18850 | no |
| `02_the_guiding_principles_and_the_conventions.md` | 65389 | no |
| `03_the_writing_standards.md` | 15205 | no |
| `04_the_dispatch_protocol.md` | 109056 | no |
| `05_the_ratified_design_intent.md` | 149034 (was 47646) | **yes**, blob `6599d64df806da4e3edb031fbb7f704dca1d2052` → `6ae0b1d8c9a830cfc3f2021f37460f05fad23547` |
| `06_the_defect_type_catalog.md` | 5968 | no |
| `07_the_charter_the_layers_and_the_decisions.md` | 33311 | no |
| `08_the_fifty_six_research_extracts.md` | 842350 | no |
| `09_the_empirical_findings_ledger.md` | 51543 | no |

**No file under the three frozen directories changed**: Task 6's enumeration reports no path under
`tools/audit/derivation_boot_pack/harmony-boundary/`, `…/scoring-model/` or `…/l0-l1/`.

## 5. Task 4 — the INPUT CONTRACT, cut, and the search whose hits go to the user

Before writing, the source passage was read at the file (`cowork_derived_specification_l0_l1_2026_09_03.md`
lines 184–189) and matched the dispatch's three NEEDLE pieces.

**4(a) — the cut copy.** Script `scratchpad/t4a_cut.py`, not committed, verbatim:

```python
"""Task 4(a): write the INPUT CONTRACT — the ratified L0/L1 specification with ONE named passage removed
(Ruling 1 of records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md)."""
import os
import subprocess
import sys

REPO = r"C:\s\MS"
SRC = os.path.join(REPO, "cowork_derived_specification_l0_l1_2026_09_03.md")
OUT_DIR = os.path.join(REPO, "tools", "audit", "derivation_exemplars", "l2")
OUT = os.path.join(OUT_DIR, "the_l0_l1_specification_the_input_contract.md")


def git_hash_object(path: str) -> str:
    return subprocess.run(["git", "-C", REPO, "hash-object", path], capture_output=True,
                          check=True).stdout.decode().strip()


# 1 — read as bytes, decode UTF-8; size and hash
with open(SRC, "rb") as fh:
    src_bytes = fh.read()
text = src_bytes.decode("utf-8")
print(f"1. source size in bytes: {len(src_bytes)}")
print(f"1. source git hash-object: {git_hash_object(SRC)}")

# 2 — the line ending
EOL = "\r\n" if "\r\n" in text else "\n"
print(f"2. EOL: {EOL!r}")

# 3 — the NEEDLE
NEEDLE = EOL.join([
    " The ratified L2 architecture's use of it as a fitted prior (D-528,",
    "  D-450) is in conflict with the charter's §8.6 and C-2, and that conflict is L2's to resolve at its",
    "  own derivation and surface — flagged, not decided.",
])

# 4 — exactly once, or STOP
count = text.count(NEEDLE)
print(f"4. NEEDLE occurrences: {count}")
if count != 1:
    print("STOP: the NEEDLE does not occur exactly once; nothing written.")
    sys.exit(2)

# 5 — remove it; print and confirm the line it sat on
cut = text.replace(NEEDLE, "", 1)
start = text.index(NEEDLE)
line_start = cut.rfind(EOL, 0, start) + len(EOL)
line_end = cut.find(EOL, start)
the_line = cut[line_start:line_end]
print(f"5. the line the NEEDLE sat on now reads: {the_line!r}")
expected_line = '  it as evidence about the music."*'
if the_line != expected_line:
    print(f"STOP: expected {expected_line!r}; nothing written.")
    sys.exit(2)
print("5. confirmed: matches the dispatch's verbatim line")

# 6 — the HEAD, joined by EOL, then one blank line
HEAD_LINES = [
    "> **THE INPUT CONTRACT — the ratified specification of L0 and L1, cut for the L2 deriving session.**",
    "> Below this block the ratified specification stands verbatim, except that passages stating the L2",
    "> layer's own ratified or current design have been removed where they stood, with no mark. Do not",
    "> try to reconstruct them, and do not treat a gap as a hint.",
]
HEAD = EOL.join(HEAD_LINES) + EOL + EOL
result = HEAD + cut

# 7 — write as UTF-8 bytes; establish (i), (ii), (iii)
os.makedirs(OUT_DIR, exist_ok=True)
out_bytes = result.encode("utf-8")
with open(OUT, "wb") as fh:
    fh.write(out_bytes)
with open(OUT, "rb") as fh:
    written = fh.read()
head_bytes = HEAD.encode("utf-8")
needle_bytes = NEEDLE.encode("utf-8")
assert src_bytes.count(needle_bytes) == 1
expected_body = src_bytes.replace(needle_bytes, b"", 1)
ok_i = written.startswith(head_bytes) and written[len(head_bytes):] == expected_body
print(f"7(i). result minus HEAD and its blank line == source minus NEEDLE, byte for byte: {ok_i}")
print(f"7(ii). result size in bytes: {len(written)}")
print(f"7(iii). result git hash-object: {git_hash_object(OUT)}")
sys.exit(0 if ok_i else 1)
```

Check (i) compares the written bytes with the source's raw bytes minus the NEEDLE's UTF-8 bytes, so it
does not merely repeat the text operation that produced the file. Output, exit 0, verbatim:

```
1. source size in bytes: 138808
1. source git hash-object: bbde68b96d64bd55346f1a14322bf0e2bc0e11a3
2. EOL: '\n'
4. NEEDLE occurrences: 1
5. the line the NEEDLE sat on now reads: '  it as evidence about the music."*'
5. confirmed: matches the dispatch's verbatim line
7(i). result minus HEAD and its blank line == source minus NEEDLE, byte for byte: True
7(ii). result size in bytes: 138946
7(iii). result git hash-object: a6d84e6ef3423f6bf09cb0acd7763d1b82346320
```

The directory `tools/audit/derivation_exemplars/l2/` was created by the script and holds that one file.

**4(b) — THE SEARCH OVER THE CUT COPY.** Script `scratchpad/t4b_search.py`, not committed, verbatim:

```python
"""Task 4(b): the search over the input contract. Its hits are REPORTED; nothing is cut or judged."""
import json
import re
from collections import Counter

REPO = r"C:\s\MS"
with open(REPO + r"\tools\audit\derivation_boot_pack.json", encoding="utf-8") as fh:
    manifest = json.load(fh)
with open(REPO + r"\tools\audit\derivation_exemplars\l2\the_l0_l1_specification_the_input_contract.md",
          "rb") as fh:
    text = fh.read().decode("utf-8")

fam = manifest["subjects"]["l2"]["THE_WITHHELD_FAMILY"]
ids = sorted({e["id"] for e in fam["identities"]}
             | {a["id"] for a in fam["derived_cross_reference_additions"]["additions"]})
docs = sorted(fam["documents"])
print(f"withheld identities searched: {len(ids)}; withheld documents searched: {len(docs)}")

id_res = [(i, re.compile(re.escape(i) + r"(?!\d)")) for i in ids]
PATH_LIKE = re.compile(r"\b(?:docs|src)/[A-Za-z0-9_./+-]+")
L2 = re.compile(r"\bL2\b")

counts = Counter()
lines = text.split("\n")
for n, raw in enumerate(lines, 1):
    line = raw[:-1] if raw.endswith("\r") else raw
    hits = []
    for i, rx in id_res:
        for m in rx.finditer(line):
            hits.append((1, m.group(0)))
    for d in docs:
        start = 0
        while (k := line.find(d, start)) != -1:
            hits.append((2, d))
            start = k + 1
    start = 0
    while (k := line.find("ARCHITECTURE.md", start)) != -1:
        hits.append((3, "ARCHITECTURE.md"))
        start = k + 1
    for m in PATH_LIKE.finditer(line):
        hits.append((3, m.group(0)))
    for m in L2.finditer(line):
        hits.append((4, m.group(0)))
    for kind, what in hits:
        counts[kind] += 1
        print(f"{n}\t{kind}\t{what}\t{line}")

print()
print("count per kind:")
for kind, label in ((1, "withheld identity"), (2, "withheld document"),
                    (3, "ARCHITECTURE.md or docs/src path"), (4, "the token L2")):
    print(f"  {kind} ({label}): {counts[kind]}")
print(f"  total: {sum(counts.values())}")
```

The `PATH_LIKE` pattern was confirmed identical to the tool's own (`gen_derivation_boot_pack.py`,
`PATH_LIKE = re.compile(r"\b(?:docs|src)/[A-Za-z0-9_./+-]+")`). A line with two hits of the same kind
is printed once per hit.

### THE CUT LIST'S RAW MATERIAL — for the user, not acted on

Every hit, verbatim (columns: line number in the cut copy, kind 1–4, what matched, the line):

```
withheld identities searched: 113; withheld documents searched: 21
1	4	L2	> **THE INPUT CONTRACT — the ratified specification of L0 and L1, cut for the L2 deriving session.**
2	4	L2	> Below this block the ratified specification stands verbatim, except that passages stating the L2
34	4	L2	- **The analysis** — the harmonic-analysis software. Its layers are named L0, L1, L2, L3 in the charter
86	4	L2	  Every cue and flag is published with its witnesses so that L2 can weigh it (§3.7).
107	4	L2	  local key` is L2's harmonic span, the charter's own name, bounded by harmony change; the grouping
141	4	L2	way to the next is L2's and is out of scope; where a statement depends on that, the dependency is its
289	4	L2	  statement supplies is carried at L0 by S-3, reached by L2 through its consumption of L0.
297	4	L2	    three-part root-pinning test is L2's decision and is RELOCATED there; its first part is S-14, and
305	4	L2	    L2's or L3's and RELOCATED there, the clauses being the L0/L1 half."*
350	4	L2	  a spelled context (S-9) and is carried forward for L2 as the charter's weak prior.
387	4	L2	  computation reads one of those. Not falsified by: L2 or L3 later admitting one of them through S-1.
403	4	L2	  notes, which is exactly the kind of thing L2 decides [RULED — charter, L2's question]. A layer that
403	4	L2	  notes, which is exactly the kind of thing L2 decides [RULED — charter, L2's question]. A layer that
429	4	L2	  key signature is replaced by a different one, all spelled pitches held fixed. Not falsified by: L2's
487	4	L2	  it does not exercise this) would yield one bar and one "bar" class; L2 would receive almost no metric
509	4	L2	  a voice assignment the record file does not carry. Not falsified by: L2 later deriving lines.
605	4	L2	  evidence L2 will want [CONJECTURE on L2's want].
605	4	L2	  evidence L2 will want [CONJECTURE on L2's want].
633	4	L2	  beginning on the upper note) — the harmony is still read on the principal at L1, and L2 receives
714	4	L2	  the interim treatment renders as a dyad; L2 sees an interval that never sounds together.
775	4	L2	  flag, so L2 can weigh it.
791	4	L2	  information for L2's weighing of the next change point and for L3's phrase reading, so it is
806	4	L2	and each ending, which slice would follow which on which pass), so that L2 can read across a repeat
836	4	L2	  impossible. The cost — very short slices in florid textures — is L2's to weigh, not L1's to
858	4	L2	  point; at L2 the harmonic boundary is decided jointly with the tonality and the chord over L1's
912	4	L2	  evidence and would decide that the harmony before the silence continues through it, which is L2's
916	4	L2	- *Premise.* Premise: L2 can consume an empty sounding set. False-negative path: a consumer that
917	4	L2	  divides by the set's size; a specification concern for L2, recorded.
934	4	L2	  entered and cut events keeps the span's edges honest (#12) and lets L2 know that the first slice's
966	4	L2	- *Premise.* The charter's; its false-negative path (a change point that L2 will always find
967	4	L2	  harmonically inert) is by design harmless — L2 may keep the harmony across it.
969	4	L2	  octave doubling's onset is not a change point. Not falsified by: L2 merging across it.
1026	4	L2	  ground truth would decide it — UNESTABLISHED; L1 publishes the class regardless, and L2's weighting
1040	4	L2	  L2's calibration"*.
1086	4	L2	- *Premise.* Premise: L2 can recover a hemiola from the notated class plus the notes. False-negative
1165	4	L2	  every change point (Ruling 47)"* — and relating them is L2's cadence-factor covariate and L3's
1176	4	L2	- *Premise.* Premise: L2 and L3 weigh the flags. Its false-negative path is none at L1.
1223	4	L2	- *Status.* Settled for L1 (OQ-1 answered for L1 at Ruling 70; Ruling 73), the remainder of OQ-1 L2's
1270	4	L2	  passing bass. The cue carries its witnesses and the slice's length, and the weighing is L2's. This
1283	4	L2	  with fitted weights, are *"L2's cadence factor … a consumer reading L1's cues and its own state"*.
1307	4	L2	  neighbour and the cue fails; the pack's C41 shape (evidence arrives after the moment). L2 can look
1317	4	L2	  structure"* being L2's choice not to consume it.
1337	4	L2	  and the cue becomes weaker. The published relaxation flag lets L2 weigh it.
1380	4	L2	  evidence, and its false-positive rate is L2's to learn.
1400	4	L2	- *Status.* Open on the measurement (OQ-10, L2's calibration); the stand-ins provisional under S-52
1414	4	L2	  under load, the measurement S-48 names owed to L2's calibration."* OQ-17 is marked ANSWERED at §4.
1431	4	L2	  (D-100). False-negative path: none; if it were dropped, L2 would compute it from the sounding set.
1505	4	L2	  and no chord able to move a change point"*; at L2 jointly with the tonality and the chord over L1's
1529	4	L2	**S-53. Nothing L1 publishes depends on anything L2 decides. Where a statement above would have
1530	4	L2	wanted L2's answer — which slice is the harmonic arrival (S-44), whether a lowest pitch is the
1533	4	L2	to L2. L1 is therefore computable in one forward pass over the working span, and the working span is
1535	4	L2	- *Defense.* The boundary contract: L1 → L2 forward only; *"L2 receives candidates and evidence, never
1535	4	L2	- *Defense.* The boundary contract: L1 → L2 forward only; *"L2 receives candidates and evidence, never
1542	4	L2	- *Falsifier.* CODE. Observable: L1's inputs. Decision rule: falsified if L1 reads any L2 output or any
1543	4	L2	  value not in L0 plus the span. Not falsified by: a caller passing a span computed by an earlier L2
1577	4	L2	  makes exhaustive; publishing the span keeps the information for L2, which may treat a pedalled
1579	1	D-207	  (D-207) — a different thing (a held tone in the harmony) from a pedal *mark* (a damper instruction);
1587	4	L2	  L2 see it.
1615	4	L2	  carried to L2's surface.
1672	1	D-501	  input; the ground D-501 and the L0 → L1 boundary contract (*"Nothing derived"*), neither naming a
1679	4	L2	  the measurement S-48 names owed to L2's calibration."* The ruling's own addendum records that the

count per kind:
  1 (withheld identity): 2
  2 (withheld document): 0
  3 (ARCHITECTURE.md or docs/src path): 0
  4 (the token L2): 59
  total: 61
```

Two things about the list that are facts rather than judgments, stated so the reader does not have to
find them: lines 1 and 2 are the HEAD the dispatch prescribed, not the specification's text; and the
identity hits are `D-207` (line 1579) and `D-501` (line 1672). **Nothing was removed, edited or judged.**

**4(c)** After both scripts ran, `git hash-object cowork_derived_specification_l0_l1_2026_09_03.md` =
`bbde68b96d64bd55346f1a14322bf0e2bc0e11a3` — **byte-identical to Task 4(a)1's hash** (B7). The
enumeration of Task 6 does not report the file.

## 6. Task 5 — the close

**5(a) — the `STATUS.md` entry**, written at the head of the dated entries, quoted whole:

> *Last updated: 2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md`. **★★ THE COWORK SIDE'S RECORDS AND THE DRAFT L2 BRIEF ARE COMMITTED**, the brief as it stands and not edited. ★ **RULING 1 OF `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md` IS CARRIED INTO THE BOOT-PACK GENERATOR**: for every subject that is not frozen, the cross-reference rule searches only the fields the pack renders besides the identifier; a frozen subject keeps the search its pack was built under. ★ **THE L2 PACK IS RE-RENDERED AND THE THREE FROZEN SUBJECTS WERE PROVED UNMOVED**, against the manifest at its pre-batch blob, with nothing written under their directories. ★ **THE INPUT CONTRACT IS WRITTEN** under Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md`: the ratified L0/L1 specification copied verbatim with ONE named passage cut, at `tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md`; the specification itself was read and not written. ★ **THE SEARCH OVER THE INPUT CONTRACT WAS RUN.** ★★ **WHAT THIS BATCH DID NOT DO: no session was booted, THE BRIEF WAS NOT RELEASED, and THE SEARCH'S HITS WERE NOT ACTED ON — they go to the user as the cut list's raw material**, together with what the re-render struck; no score or analysis file was copied, moved or edited. No open-items row created, flipped or discarded; no decisions-register identity allocated and no `D-NNN` created; no extract edited; no tool source edited but the boot-pack generator and the forward bound's authored aiming; no `src/` file, build, test, golden, score corpus or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_l2_brief_landing_2026_09_27.md` — and no figure is restated here (**D-431**).)*

**★ ONE CHANGE TO AN EXISTING LINE, DECLARED.** In the same edit, the second-half batch's entry beneath
lost its leading `Last updated: ` prefix. This is not an editorial rewrite: it is
`gen_status_batch_bound.py`'s own declared prefix adjustment, which the dispatch says is expected to fire
— `moved_entries()` strips that prefix from the base-commit text and requires the stripped form in the
live file exactly once. The previous batch declared the same act (its report §8). The entry it touched
then moved to the archive whole at 5(b), so **no rewritten sentence remains in `STATUS.md`**. This was
the last write to `STATUS.md` in this batch.

**5(b) — the forward bound.** Established first: `git ls-tree` of `STATUS.md` at
`84ab3a5c404bf9953a568df7c0c57022dba06f8f` and at `9378e95a7d620fca6ebd28119d4d1bb6483f9d66` both give
blob `d390a3103918b039489e1a5b08484d7cd18bc302`. The comment's claim that the close batch wrote no entry
of its own was checked at `git diff --numstat a84e237530… 84ab3a5c40… -- STATUS.md`: one line changed
(`1 1`), the second-half entry replacing the consolidation entry.

The aiming set: `BASE_COMMIT` = `9378e95a7d620fca6ebd28119d4d1bb6483f9d66`; `PREVIOUS_BATCH_DISPATCH`
= `cc_instruction_l2_pack_build_second_half_2026_09_27.md`; `DISPATCH` =
`cc_instruction_l2_brief_landing_2026_09_27.md`; `TASK` = `Task 5`; `ACT_DATE` = `2026-09-27` (the date
the move ran); `MOVE_KIND` = `ordinary`; `RULINGS` unchanged; one row appended to `PREVIOUS_AIMINGS` and
no row edited. Each former value is named in its comment.

The diff, `git diff 3a5ae0ed27e95f1926f0fb777e9b25e274e1b6dc c0a8fd4d1adf41cb338ca964520213cce2cdcd2c`,
verbatim (`scratchpad/bound_diff.txt`):

```diff
diff --git a/3a5ae0ed27e95f1926f0fb777e9b25e274e1b6dc b/c0a8fd4d1adf41cb338ca964520213cce2cdcd2c
index 3a5ae0ed27..c0a8fd4d1a 100644
--- a/3a5ae0ed27e95f1926f0fb777e9b25e274e1b6dc
+++ b/c0a8fd4d1adf41cb338ca964520213cce2cdcd2c
@@ -526,7 +526,33 @@ OUT = os.path.join(HERE, "status_batch_bound.json")
 # tool can identify them** — a declared state and not a STOP, unchanged by this act. **NO COUNT OF
 # THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431): the membership is DERIVED from the entries'
 # own text at the base commit.
-BASE_COMMIT = "a84e2375301973b48cb2a0cc5a0fb13e6ec41c24"
+# ★ RE-AIMED 2026-09-27 by `cc_instruction_l2_brief_landing_2026_09_27.md` Task 5, at its 5(b), and
+# ALL FIVE authored inputs moved together, `PREVIOUS_AIMINGS` being appended to rather than replaced
+# (#12). The aiming it replaces is the L2-pack-build second half's, which is ALREADY the last row of
+# `PREVIOUS_AIMINGS` — that batch recorded its own aiming in its own act — so it is not appended a
+# second time, and this batch's aiming is appended instead. `BASE_COMMIT` was
+# `a84e2375301973b48cb2a0cc5a0fb13e6ec41c24` and is now
+# `9378e95a7d620fca6ebd28119d4d1bb6483f9d66`: this batch's Task 0 commit, the interim carriers. Task 0
+# commits no `STATUS.md`, so that commit's `STATUS.md` object is the one both refs carried when this
+# batch opened (`84ab3a5c404bf9953a568df7c0c57022dba06f8f`, read at the two ref FILES with the file
+# tools, D-253) — the same blob at both commits, established at `git ls-tree` of each — and it carries
+# the second-half batch's entry at the head of the dated entries.
+#
+# ★★ THE THEN-PREVIOUS BATCH IS THE L2-PACK-BUILD SECOND HALF. `PREVIOUS_BATCH_DISPATCH` was
+# `cc_instruction_decision_rules_consolidation_2026_09_21.md` and now names
+# `cc_instruction_l2_pack_build_second_half_2026_09_27.md`, whose entry names it. That batch's CLOSE
+# (`cc_instruction_l2_pack_build_close_2026_09_27.md`) wrote no `STATUS.md` entry of its own — it
+# corrected the second-half entry in place — so it selects nothing and is not named; the same shape
+# the aiming above records for the consolidation batch's close.
+#
+# **THE DECLARED PREFIX ADJUSTMENT IS EXPECTED TO FIRE**, that entry carrying the `Last updated: `
+# prefix at the base commit, which is why this batch's own entry was written into `STATUS.md` BEFORE
+# `--apply` ran. `ACT_DATE` and the executing dispatch's date AGREE here, both being 2026-09-27.
+# **The second writing's two nameless 2026-09-02 entries remain in `STATUS.md` and no aiming of this
+# tool can identify them** — a declared state and not a STOP, unchanged by this act. **NO COUNT OF
+# THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431): the membership is DERIVED from the entries'
+# own text at the base commit.
+BASE_COMMIT = "9378e95a7d620fca6ebd28119d4d1bb6483f9d66"
 
 # The batch whose entries this aiming moves, named by its dispatch because that is what each of its
 # entries says of itself. On an ORDINARY move it is the THEN-PREVIOUS batch and Ruling 4's forward
@@ -536,7 +562,7 @@ BASE_COMMIT = "a84e2375301973b48cb2a0cc5a0fb13e6ec41c24"
 # 4's forward bound moves exactly these, in the act that writes this batch's own" until 2026-09-07,
 # correct while every aiming this tool had ever carried was an ordinary one; it is widened rather
 # than replaced, because the ordinary reading is still the one that governs an ordinary move — #12.)*
-PREVIOUS_BATCH_DISPATCH = "cc_instruction_decision_rules_consolidation_2026_09_21.md"
+PREVIOUS_BATCH_DISPATCH = "cc_instruction_l2_pack_build_second_half_2026_09_27.md"
 
 # ★ THE ACT DATE IS THE DAY THE MOVE RAN, NOT THE DAY THE DISPATCH WAS WRITTEN. This executing
 # dispatch is dated 2026-09-07 and this batch ran on 2026-09-07, so the two agree; the field is kept
@@ -548,9 +574,12 @@ PREVIOUS_BATCH_DISPATCH = "cc_instruction_decision_rules_consolidation_2026_09_2
 # the move happens now, and the header says so.)* *(`ACT_DATE` read "2026-09-21" and `DISPATCH`
 # `cc_instruction_decision_rules_consolidation_2026_09_21.md` while that batch was the executing act;
 # both are re-stated here for `cc_instruction_l2_pack_build_second_half_2026_09_27.md`, dated
+# 2026-09-27, whose move ran on 2026-09-27, so the two dates agree.)* *(`ACT_DATE` read "2026-09-27"
+# and `DISPATCH` `cc_instruction_l2_pack_build_second_half_2026_09_27.md` while that batch was the
+# executing act; both are re-stated here for `cc_instruction_l2_brief_landing_2026_09_27.md`, dated
 # 2026-09-27, whose move ran on 2026-09-27, so the two dates agree.)*
 ACT_DATE = "2026-09-27"
-DISPATCH = "cc_instruction_l2_pack_build_second_half_2026_09_27.md"
+DISPATCH = "cc_instruction_l2_brief_landing_2026_09_27.md"
 # TASK IS A CHOICE, DECLARED RATHER THAN IMPLIED. On an ORDINARY move the executing dispatch orders
 # the move and this batch's own `STATUS.md` entries in the same numbered task, so both halves of "the
 # same act that writes its own entries" sit inside it, and that task is what the archive header names.
@@ -595,8 +624,11 @@ DISPATCH = "cc_instruction_l2_pack_build_second_half_2026_09_27.md"
 # its 7(b) — inside its own Task 5, which that dispatch's §7 heading names in those words. It names
 # Task 10 while `cc_instruction_l2_pack_build_second_half_2026_09_27.md` is the executing act, that
 # dispatch ordering both halves of the close — this batch's own entry at its 12(a) and this move at
-# its 12(b) — inside its own Task 10, which that dispatch's §12 heading names in those words.)*
-TASK = "Task 10"
+# its 12(b) — inside its own Task 10, which that dispatch's §12 heading names in those words. It names
+# Task 5 while `cc_instruction_l2_brief_landing_2026_09_27.md` is the executing act, that dispatch
+# ordering both halves of the close — this batch's own entry at its 5(a) and this move at its 5(b) —
+# inside its own Task 5, which that dispatch's §7 heading names in those words.)*
+TASK = "Task 5"
 # ★ WHAT KIND OF MOVE THIS AIMING PERFORMS. Two values and no others.
 #   "ordinary"  — the move Ruling 4's forward clause describes: the then-previous batch's entries,
 #                 moved in the same act that writes this batch's own entries.
@@ -985,6 +1017,10 @@ PREVIOUS_AIMINGS = [
      "base_commit": "a84e2375301973b48cb2a0cc5a0fb13e6ec41c24",
      "the_then_previous_batch": "cc_instruction_decision_rules_consolidation_2026_09_21.md",
      "the_kind_of_move": "ordinary"},
+    {"executing_act": "cc_instruction_l2_brief_landing_2026_09_27.md, Task 5",
+     "base_commit": "9378e95a7d620fca6ebd28119d4d1bb6483f9d66",
+     "the_then_previous_batch": "cc_instruction_l2_pack_build_second_half_2026_09_27.md",
+     "the_kind_of_move": "ordinary"},
 ]
 
 HEADER_ORDINARY = (
```

No function was touched. `--apply`, exit 0, verbatim (it ran once; no STOP):

```
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 2,707 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

`--check`, exit 0, verbatim:

```
  entries moved: 1, 2,707 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**The entry actually moved, by name:** the second-half batch's entry,
`*2026-09-27 (CC — \`records/cc/instructions/cc_instruction_l2_pack_build_second_half_2026_09_27.md\`. **★★ THE L2 SUBJECT IS ADDED TO THE DERIVATION BOOT PACK AND ITS PACK IS RENDERED**…`
— the declared prefix adjustment applied. `STATUS_ARCHIVE.md`'s diff by blobs
(`160ece0f9274a0669bd2a52ec601a0cb08a4df78` → `131cd8d01514744febaeb674e27b653a29dd8840`) adds exactly
four lines at its end — the forward-bound header naming this dispatch and Task 5, a blank line, the moved
entry verbatim, a blank line — and removes none. **The two 2026-09-02 entries did not move and were not
moved by hand.** (A green `--check` is not read as proof the bound is met, `OPEN_ITEMS.md` OI-379; the
moved entry is named above.)

**5(c) — the regenerations**, all eight outputs verbatim, in the dispatch's order:

1. `python tools/audit/gen_evidence_pin_membership.py` — exit 0:
```
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 99
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
2. `python tools/audit/gen_evidence_pin_membership.py --check` — exit 0:
```
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 99
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
3. `python tools/audit/gen_l0_l1_outgoing_population.py` — exit 0:
```
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
```
4. `python tools/audit/gen_l0_l1_outgoing_population.py --check` — exit 0:
```
l0_l1_outgoing_population.json re-derives
```
5. `python tools/audit/gen_session_start_read_size.py` — exit 0:
```
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
    STATUS.md                                                                 11142
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 246304
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 246304 [ruled membership]  (-120817, -32.91%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 246304 [ruled membership]  (-50528, -17.02%)  <- CROSSES A REGIME BOUNDARY
```
6. `python tools/audit/gen_defense_share.py` — exit 0:
```
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
    of the whole session-start read (246304): 5.26%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```
7. `python tools/audit/gen_session_start_read_size.py --check` — exit 0: the first line reads
`the session-start read measurement re-derives`, followed by the same twenty-eight lines as output 5
from `  rule (a) points at …` through the second `CROSSES A REGIME BOUNDARY` line, identical (a `diff`
of the two captures differs only at line 1).
8. `python tools/audit/gen_defense_share.py --check` — exit 0: the first line reads
`the defense-share measurement re-derives`, followed by the same sixteen lines as output 6 from
`  row Why followed by …` through `  and the ends are AUTHORED (…).`, identical (a `diff` of the two
captures differs only at line 1).

**No `STOP:` line and no traceback from any of the four tools.** All four wrote their artifacts, and
each on-disk blob differs from its blob at `9378e95a7d…`.

**The members and entries changed**, by a recursive comparison of each artifact's parsed JSON on disk
against its blob at Task 0's commit (script `scratchpad/t5c_jdiff.py`), verbatim:

```
=== tools/audit/evidence_pin_membership.json: 3 difference(s)
  CHANGED $.counts.ruling_records_read
    old: 97
    new: 99
  ADDED $.ruling_records_read[]
    new: "records/cowork/rulings/cowork_rulings_2026_09_27_l2_brief_sitting.md"
  ADDED $.ruling_records_read[]
    new: "records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md"
=== tools/audit/l0_l1_outgoing_population.json: 2 difference(s)
  CHANGED $.the_term_search.counts.hits_per_term.release
    old: 73
    new: 74
  ADDED $.the_term_search.per_file.STATUS.md
    new: {"path": "STATUS.md", "inventory_class": "governing-documents", "is_a_named_member": false, "in_the_specification_document_set": false, "admitting_hit_count": 0, "recorded_hit_count": 1, "admitting_hits": [], "recorded_hits": [{"line_number": 8, "term": "release", "tier": "recorded", "line": "*Last updated: 2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md`. *… (2176 chars)
```

- **`evidence_pin_membership.json`: no member was added, removed or changed.** The two ruling records
  Task 0 committed entered the list of records read, and nothing else moved. The previous batch's
  finding stands as it was: the regeneration publishes no pinned-evidence member for the L2 reading
  document.
- **`l0_l1_outgoing_population.json`: no population entry was added, removed or changed.** One
  per-file record was added: `STATUS.md` now carries one *recorded* (not admitting) hit for the term
  `release`, at line 8. **That hit comes from this batch's own `STATUS.md` entry**, from its words "THE
  BRIEF WAS NOT RELEASED". Admitting hits for `STATUS.md`: 0. Resolved: nothing.

**5(d) — THE CLOSING GUARD CAPTURE**: `python tools/audit/gen_guard_state.py`, exit 0, captured at
**`scratchpad/guard_close.txt`**. A line-by-line `diff` of the opening and closing captures — the same
guards, in the same order — returns exactly:

```
59c59
<   [FAIL] tools/audit/gen_evidence_pin_membership.py --check
---
>   [PASS] tools/audit/gen_evidence_pin_membership.py --check
104c104
< 79 guard(s) run, 13 failing, 4 not run, 19 historical record(s)
---
> 79 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

**The guard that moved: `gen_evidence_pin_membership.py --check`, FAIL → PASS** (allowed), cleared by
5(c)'s regeneration. **No guard whose verdict was PASS at the opening carries any other verdict at the
close.** Every other verdict is identical, including `gen_derivation_boot_pack.py --check`,
`gen_status_batch_bound.py --check`, `gen_l0_l1_outgoing_population.py --check`,
`gen_session_start_read_size.py --check` and `gen_defense_share.py --check`, all PASS at both.

`python tools/audit/gen_guard_classification.py` (`scratchpad/guardclass_close.txt`), exit 2, as
expected (B8), carried and not chased — **byte-identical to the opening's** (`diff` exit 0):

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

## 7. Task 6 — the commit and the push

The enumeration before the batch commit (`python tools/audit/changed_paths.py`, exit 0,
`scratchpad/cp6.txt`, 407 records), every record other than the untracked paths already held back at
Task 0:

```
 M	STATUS.md
 M	STATUS_ARCHIVE.md
 M	tools/audit/claude_md_finer_archive.json
 M	tools/audit/defense_share.json
 M	tools/audit/derivation_boot_pack.json
 M	tools/audit/derivation_boot_pack/l2/05_the_ratified_design_intent.md
 M	tools/audit/evidence_pin_membership.json
 M	tools/audit/gen_derivation_boot_pack.py
 M	tools/audit/gen_status_batch_bound.py
 M	tools/audit/guard_state.json
 M	tools/audit/l0_l1_outgoing_population.json
 M	tools/audit/session_start_read_size.json
 M	tools/audit/status_batch_bound.json
??	tools/audit/derivation_exemplars/l2/
```

**Every modified path is inside the footprint assumption.** Nothing under the three frozen pack
directories appears. The guard set's own artifact reported modified is `tools/audit/guard_state.json`
(written by `gen_guard_state.py` at the captures). `tools/audit/claude_md_finer_archive.json` is held
back (B9); `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` and the other untracked paths
are held back.

**The batch commit** carries exactly these, each by its own path: `tools/audit/gen_derivation_boot_pack.py`;
`tools/audit/derivation_boot_pack.json`; `tools/audit/derivation_boot_pack/l2/05_the_ratified_design_intent.md`;
`tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md`; `STATUS.md`;
`STATUS_ARCHIVE.md`; `tools/audit/gen_status_batch_bound.py`; `tools/audit/status_batch_bound.json`;
`tools/audit/evidence_pin_membership.json`; `tools/audit/l0_l1_outgoing_population.json`;
`tools/audit/session_start_read_size.json`; `tools/audit/defense_share.json`; this report; and
`tools/audit/guard_state.json` — **14 paths.**

**The commits.** Task 0: `9378e95a7d620fca6ebd28119d4d1bb6483f9d66`. The batch commit is the commit
that carries this report, so its identity cannot be written inside it; it, the proof of its staged set
and the push result are reported in the session's closing message, and are readable at
`.git/refs/heads/master` and `.git/refs/remotes/origin/master`. This report is not edited after that
commit.

## 8. What I did NOT do

- No tool source edited but the two B1 names: `tools/audit/gen_derivation_boot_pack.py` (at exactly the
  five replacements) and `tools/audit/gen_status_batch_bound.py` (at its authored aiming inputs, their
  comments and one appended `PREVIOUS_AIMINGS` row; no function). Not
  `gen_withheld_family_reading.py`, not `gen_evidence_pin_membership.py`, not
  `gen_guard_classification.py`.
- No extract under `reading_pass/` edited.
- Nothing written, deleted, renamed or moved under `tools/audit/derivation_boot_pack/harmony-boundary/`,
  `…/scoring-model/` or `…/l0-l1/`.
- No governing document amended but `STATUS.md`: not `CLAUDE.md`, `FRAMEWORK.md`, `ARCHITECTURE.md`,
  `OPEN_ITEMS.md` or any ruling record.
- `cowork_derived_specification_l0_l1_2026_09_03.md` read and not written (4(c)); the draft brief
  `cowork_blind_session_brief_l2.md` committed as it stood and not edited.
- No score or analysis file copied, moved or edited; the seven exemplars the brief names stay where they
  are.
- No session booted; the brief not released.
- The search's hits not acted on: nothing removed, edited or judged.
- No per-entry review of what the re-render struck or returned to the pack.
- No open-items row created, flipped or discarded; no decisions-register identity allocated and no
  `D-NNN` touched.
- No `src/` file, build, test, golden, score corpus, nothing under `tools/corpus/`, `tools/robust_stop/`
  or `tools/dcml/`, no measurement of the analysis, no paper.
- The live consumer at `tools/audit/gen_withheld_family_reading.py` not repaired;
  `gen_guard_classification.py`'s STOP carried, not chased.
- `tools/audit/claude_md_finer_archive.json` not staged, not reverted, not investigated.

## 9. What goes to the user

- **The search's hits over the input contract** — §5, "THE CUT LIST'S RAW MATERIAL".
- **What the re-render struck at 3(d)** — the two member-(5) entries `D-296` and `D-440`, each
  matched on a source path in its `verbatim` field — read out and not reviewed.
- **The 5(c) changes**: in the pinned-evidence membership, no member changed (two ruling records read,
  nothing else); in the outgoing population, no entry changed, and one recorded (non-admitting) hit for
  `release` in `STATUS.md`, coming from this batch's own entry.
- **No STOP fired.** One reading is stated rather than silent: the standing `FROZEN SOURCES` advisory in
  the `--check` output was taken as part of the expected result, because it is identical to the
  previous batch's recorded baseline and sets no exit code (§2).
