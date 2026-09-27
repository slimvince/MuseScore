# CC REPORT — THE L2 COMPARISON, SECOND BATCH: THE TABULATION POPULATION PUBLISHED IN ITS ORDER, AND THE TABULATION OPENED — POSITIONS 1 TO 4 TABULATED, THE REST UNTOUCHED (2026-09-27)

> **Executes** `records/cc/instructions/cc_instruction_l2_comparison_tabulation_2026_09_27.md`, pinned at
> blob `0e21f61857ae7a2e286b576549d42ac6cc3c7d95`. **No task STOPped.** The tabulation stopped at the
> member boundary after position 4 under the dispatch's own context rule (Task 2(g), D-672), and that stop
> is recorded here and in the reading file's §0. **This report decides nothing**: it relays what was run
> and what was written, and it makes no recommendation about the derivation, the method, any disposition
> or any open question. Every output is quoted verbatim from the run. **No count the population tool
> produces, and no count of the reading file's rows, is restated in prose (D-431)** — the sizes are at
> `tools/audit/l2_outgoing_population.json` → `the_measured_size` → `the_tabulation_population`, and the
> row arithmetic is at the reading file's §13.

---

## 0. The ordered first read

The first file this session read was `cowork_blind_derivation_l2_2026_09_27.md` — **§5, then §6, then
§7, then the whole file** — before `CLAUDE.md`'s session-start spans were acted on and before any other
read (Ruling 2 of the comparison-design sitting). *(`CLAUDE.md`'s contents reached the session's context
at boot as injected context, before any tool call; no read of it was made by this session before the
derivation was read whole.)* The derivation's own counts were taken at its structure by this session:
**49 statements, 18 open questions, 5 marked ★** — the counts of record for this comparison, stated in
the reading file's manifest.

Then, in the dispatch's order: `CLAUDE.md` at its six session-start spans (in context); `STATUS.md`;
`DECISIONS.md` whole; `BUILD_AND_TEST.md` (the condition is met — this batch runs the guard set; its
opening section and the build-script section were read, and it names no guard-runner command); the
gating answer at `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` →
`gating_ids`; `cowork_audit_protocol.md`'s dispatch-protocol section in full; the two rulings of
2026-09-27 whole; the comparison-design sitting whole; Rulings 32 and 33 (§3am, §3an); the phase
definition §0 and §3.4; `FRAMEWORK.md` §5 from `### L0` through `### The boundary contracts`; the
brief's §2, §4 and §7; the pack's L2 `counted`, `THE_WITHHELD_FAMILY` and `LEAKS` (read, not
regenerated); the previous dispatch and report whole; `tools/audit/gen_l2_outgoing_population.py`
whole; the artifact's `the_measured_size` and `the_distinct_names`; the L0/L1 reading file's §0 to §5,
the first three row blocks of §6.1, its foot arithmetic, §10 and §14; and the current handover block,
`records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_two.md` (the standing clause that a
dispatch's read-first block names it).

**The pack's counted block, read at the file:** 113 withheld identities, 21 withheld documents, 6
withheld passages, 2 leaks — as the dispatch's FACT states. **The twenty names at
`the_distinct_names` are the twelve WHOLE and eight LISTED of ruling (2)**, checked name by name.

---

## 1. Task 0 — the records landed, and pushed

**0(a) — the pin.**

```
$ git hash-object -w records/cc/instructions/cc_instruction_l2_comparison_tabulation_2026_09_27.md
0e21f61857ae7a2e286b576549d42ac6cc3c7d95
68054
```

The blob was proved unmoved at staging (the staged identity at 0(e) below is the same `0e21f618…`).

**0(b) — the refs, read with the file tools.** Both read `6f77e0d2b5b14a8043212bf6f19b06a0b7ed4b04`, as
the FACT states. **The chain, read at the objects by explicit hash:**

```
commit 6f77e0d2b5b14a8043212bf6f19b06a0b7ed4b04
parent fdfc774bca215441b7671c4a0c1e1aa1afcc324d
subject Close: the L2 outgoing population measured, under its dispatch
 STATUS.md | 2 +-  STATUS_ARCHIVE.md | 4 +  .../cc_report_l2_outgoing_population_2026_09_27.md | 702 +
 tools/audit/defense_share.json | 4 +-  tools/audit/evidence_pin_membership.json | 3 +-
 tools/audit/gen_status_batch_bound.py | 49 +-  tools/audit/guard_state.json | 34 +-
 tools/audit/l0_l1_outgoing_population.json | 19 +-  tools/audit/l2_outgoing_population.json | 12 +-
 tools/audit/session_start_read_size.json | 16 +-  tools/audit/status_batch_bound.json | 20 +-
 11 files changed, 804 insertions(+), 61 deletions(-)
commit fdfc774bca215441b7671c4a0c1e1aa1afcc324d
parent c8a1a8502373abddcf7961e35cad6f12353c4d8b
subject the L2 outgoing population derived and measured under the ruling of 2026-09-27: four items, residue published, nothing tabulated
 tools/audit/gen_guard_state.py | 15 +  tools/audit/gen_l2_outgoing_population.py | 635 +
 tools/audit/l2_outgoing_population.json | 72270 +
 3 files changed, 72920 insertions(+)
commit c8a1a8502373abddcf7961e35cad6f12353c4d8b
parent 1fb7f5189a44eb927049694faf137ea01ef528ac
subject record: the L2 outgoing-population ruling (Option B), entries 259 to 261 and the population dispatch
 5 files changed, 823 insertions(+)
commit 1fb7f5189a44eb927049694faf137ea01ef528ac
parent 19673e24f17384d205ef7f3503a1c2ebf8f9a11e
subject Close: the L2 blind derivation committed, under its dispatch
 9 files changed, 793 insertions(+), 30 deletions(-)
```

*(The per-file stat lines are joined here for length; the commits, parents, subjects and totals are as
printed.)* The chain matches the previous report's Task 0 and Task 1 commits and the close's subject.

**0(c) — A1's check.** `python tools/audit/changed_paths.py`, exit 0; every record other than the
untracked paths under `scratch_artifacts/`, verbatim:

```
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_l2_comparison_tabulation_2026_09_27.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_two.md
??	records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
397 changed path record(s) [worktree]
```

Per named path, `git ls-files --others --exclude-standard -- <path>` returned each of the three paths
(untracked). **Nothing was staged**: the index's tree (`git write-tree`) equalled the tip's tree
`dc35da6145a31e0d249b55c4575753fd0ad74c5c`.

**0(d) — the last-bytes check**, at each blob:

```
records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md 71732bdaf7e4331826497e32eb27a4d8d79cccf5 9441
b' "B, but why not first have a look at the \'four\nsmaller documents\'?"*\n' 0
records/cc/instructions/cc_instruction_l2_comparison_tabulation_2026_09_27.md 0e21f61857ae7a2e286b576549d42ac6cc3c7d95 68054
b'. TOWARDS the ultimate objective and TOWARDS the guiding principles.*\n' 0
records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_two.md 38b8450d2cbfdf1fef108bb19ae1bdf286e04921 4745
b'ce: Cowork, 2026-09-27 (Stockholm), the sitting booted on entry 261.*\n' 0
```

No zero byte and no final line broken off mid-word; the ruling record is at the stated 9,441 bytes;
entry 262 at the size shown (no size was stated for it).

**0(e) — the commit.** The staged set proved against the tip's tree, by explicit hash:

```
:000000 100644 0000000000000000000000000000000000000000 0e21f61857ae7a2e286b576549d42ac6cc3c7d95 A	records/cc/instructions/cc_instruction_l2_comparison_tabulation_2026_09_27.md
:000000 100644 0000000000000000000000000000000000000000 38b8450d2cbfdf1fef108bb19ae1bdf286e04921 A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_two.md
:000000 100644 0000000000000000000000000000000000000000 71732bdaf7e4331826497e32eb27a4d8d79cccf5 A	records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md
```

**Commit `9084a5f806cc1745bd7b19be53124f41ffa2e4d8`** — `record: the L2 named-documents ruling (Option
B), entry 262 and the L2 tabulation dispatch`. Pushed; `.git/refs/remotes/origin/master` read
`9084a5f806cc1745bd7b19be53124f41ffa2e4d8`.

**0(f) — the opening guard capture**, after the commit, `python tools/audit/gen_guard_state.py` (write
mode), exit 0, saved outside the repository at
`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\fa31c1c9-3cdd-4d9d-b7b3-6aaa71fac0ce\scratchpad\guard_open.txt`.
Every verdict, verbatim:

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
80 guard(s) run, 13 failing, 4 not run, 19 historical record(s)
```

**Against A2: holds exactly** — the twelve named reds plus `gen_evidence_pin_membership.py --check`,
zero STOPs in the runner. **The figure of record, read at the object**
`6f77e0d2…:tools/audit/guard_state.json` → `summary`: run 80, passing 68, failing 12, the twelve named
failing tools, not_run 4, historical_records 19 — as the FACT states.

**The guard classification**, `python tools/audit/gen_guard_classification.py`, exit 2, against the FACT
— exactly the four names, no fifth:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

**E0: MET.** Three paths in one commit; `origin/master` at the commit; the pin proved; A1 established by
the enumeration; the opening capture as A2 predicts.

---

## 2. Task 1 — the tabulation population, published by the tool

**1(a) — the six edits**, made to `tools/audit/gen_l2_outgoing_population.py` and to nothing else in
`tools/`: edit 1 (the named-documents constants, the passage rule, the order, and the new
`SIZE_STOP_STATEMENT`); edit 2 (the four pure functions after `norm`); edit 3 (the tabulation-population
block before the measured size); edit 4 (the size key and the two artifact keys); edit 5 (the reach
sentence); edit 6 (the docstring item 6, the docstring sentence, and the printout). Each was inserted
verbatim at the anchor the dispatch quotes. The source moved from blob
`173d14d51167c9a654be84b35d021ac6cdad3849` to `0330401941973d1b477f4b33626a0b55e21a2676`
(`git diff --stat`: 331 insertions, 7 deletions).

**1(b) — the synthetic checks**, from a scratch script outside the repository importing the four
functions, verbatim:

```
PASS  fence_ranges(lines) -> [(6, 8)] (expected [(6, 8)])
PASS  block_around(lines, 4, [(6, 8)]) -> (3, 4) (expected (3, 4))
PASS  block_around(lines, 7, [(6, 8)]) -> (6, 8) (expected (6, 8))
PASS  block_around(lines, 1, [(6, 8)]) -> (1, 4) (expected (1, 4))
PASS  block_around(lines, 9, [(6, 8)]) -> (9, 9) (expected (9, 9))
PASS  merge_ranges([(5, 7), (1, 2), (3, 3), (9, 9)]) -> [(1, 3), (5, 7), (9, 9)] (expected [(1, 3), (5, 7), (9, 9)])
PASS  subtract_spans([(1, 10)], [(4, 5), (8, 8)]) -> [(1, 3), (6, 7), (9, 10)] (expected [(1, 3), (6, 7), (9, 10)])
failed: 0
```

**1(c) — the run, the check, and the unchanged part.**

```
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
exit:0
$ python tools/audit/gen_l2_outgoing_population.py --check
l2_outgoing_population.json re-derives
exit:0
```

No `STOP:` line and no traceback — so every item-3 hit line and every item-4 home was proven to lie in
exactly one member, and item 2's derived names equal the named-documents ruling's two lists.

**The unchanged-part property**, compared recursively between the committed artifact at
`6f77e0d2…:tools/audit/l2_outgoing_population.json` (blob `cf091c01059e3a5236067dcd0a15f6426f805ae8`)
and the new one written into the object store (blob `ddc45c24a658fd1d248b0214f3158a889eacb444`), both
read from `git show <blob>` into scratch files and loaded with `json`:

```
key paths CHANGED in value: 2
  item_3_the_term_search -> the_reach_stated
  the_measured_size -> ★_the_size_stop
key paths REMOVED: 0
key paths ADDED (top of each added subtree): 3
  the_measured_size -> the_tabulation_population
  the_named_documents_ruling
  the_tabulation_population
PROPERTY HOLDS
```

**As measured:** exactly the two named paths changed, carrying the edit-5 and edit-1 texts; nothing was
removed; and the only additions are the three named key paths with everything beneath them.

**1(d) — the commit.** Staged set proved: `M tools/audit/gen_l2_outgoing_population.py`, `M
tools/audit/l2_outgoing_population.json`. **Commit `85817dec62e1aa7037789dc583c2ff2bf3003989`** — `the L2
tabulation population published in its order under the named-documents ruling and the passage rule,
nothing tabulated yet`. Pushed; `origin/master` read `85817dec…` at the ref file.

**E1: MET.** The six edits present; the synthetic checks passed; the tool and its `--check` exit 0 with
no `STOP:` line; the unchanged-part property proven; the member count, lines and bytes are at the artifact
(`the_measured_size` → `the_tabulation_population`), cited here and not restated in prose.

---

## 3. Task 2 — the tabulation

**The reading file** is `ratification_surfaces/cowork_comparison_l2_reading.md`, following the L0/L1
reading file section for section (§0 progress, §1 words, §2 the subject from scratch, §3 the population
named to the artifact with the eight LISTED names and the residue named as not tabulated, §4 the unit as
2(a) states it, §5 the closed vocabulary and the two narrow marks, §6 the tabulation, §7 to §9 and §14
NOT YET WRITTEN, §10 to §13 the gathers, §15 NOTHING, §16 what it does not do).

**The commits, one per member, each pushed with `origin/master` read equal at the ref file:**

| Act | Commit |
|---|---|
| The skeleton — `comparison L2: the reading file opened, its population, unit and vocabulary stated, nothing tabulated` | `03b3d445dee5522f46acd2e4cd01ecf069788322` |
| Member 1 | `d3da65ea8c123f101ab49a121d8f92d0672b32a0` |
| Member 2 | `c3e40487b9e44aad166bc32ad5ec1f3ac30eee54` |
| Member 3 | `0dca4e8a1ee13da9d6eb250610e9824e2c38a2f0` |
| Member 4 | `9d96782d360782d2a50fa2b166045cfd1e7d1e0a` |

Each member commit's subject carries the member's statement count from its manifest header, as 2(g)
orders; the counts, the per-member distributions and the running totals with their arithmetic check are
at the reading file's §13 and are not restated here.

**The members done and not done.** **DONE: positions 1 to 4** — the four `ARCHITECTURE.md` sections of
the ruling's item 1, each read whole and tabulated whole. **NOT DONE: positions 5 to 62** — UNTOUCHED:
not read for tabulation, not quoted, not counted and not placed; **nothing is partly worked**. The next
writing resumes at **position 5**, `cowork_layer5_function_design.md`, whole. **Why the stop fell there
(D-672, the dispatch's Task 2(g)):** over positions 1 to 4 this session caught, on re-reading its own rows
before each commit, several quotations attributed to the wrong field of a derived statement (a phrase from
the derivation's terms table attributed to L2-S2; a phrase from L2-S20's premise attributed to L2-S22; the
contamination flag attributed to §6.3 rather than to L2-S17's own defense), all corrected before their
member was committed — the dispatch's tell *"a row whose quoted words you did not read at the file"*
approaching — and position 5 is a whole document of several hundred lines. The stop and the resume point
are recorded in the reading file's §0.

**Two reading rules this session applied, authored and stated at the head of the reading file's §6 so the
user can challenge them at one place:** (1) section headings are titles and are neither statements nor
*not a statement* items; (2) a sentence introduced as the defense of the rule before it (*Why:*) is listed
under *not a statement* as a defense, unless it states a separate rule of its own. Both are this session's
readings of 2(a)'s unit; neither is ruled.

**The marks.** WITHHELD is marked only where a statement lies inside one of the homes the artifact's
`item_4_identities_inside` names for its member, and every AGREES on a WITHHELD row is listed at its
member's foot. **No SEEN home lies in positions 1 to 4.** Rows naming a derived statement §6.3 names as
NEAREST say so, and each member's foot lists them. The wider check the dispatch names is **not made**,
and the reading file's §5 and §14 say so.

**E2: MET for positions 1 to 4.** Each has its manifest; every outgoing statement carries exactly one
disposition or UNPLACED with what was read; every DIFFERS carries its one-sentence difference in both
texts' words and nothing chosen; the marks applied where they apply; the transfer list, audit questions
and proposals gathered at §10, §11 and §12; §0 true of the file; no recommendation anywhere; A5 intact
(below).

---

## 4. Task 3 — the close

**3(a) — the `STATUS.md` entry**, written first, at the top, taking the `Last updated: ` prefix from the
previous batch's entry, quoted whole:

> *Last updated: 2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_2026_09_27.md`. **★★ THE L2 COMPARISON'S TABULATION POPULATION IS PUBLISHED IN ITS ORDER, AND THE TABULATION IS OPEN: THE FOUR NAMED `ARCHITECTURE.md` SECTIONS ARE TABULATED, AND THE REST IS UNTOUCHED.** ★ **THE RECORDS ARE COMMITTED** — the user's named-documents ruling of 2026-09-27, Option B, at `records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md`, with `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_two.md` and this dispatch, each checked at its blob for a complete final line before it was staged. ★ **THE POPULATION TOOL `tools/audit/gen_l2_outgoing_population.py` NOW ALSO PUBLISHES THE TABULATION POPULATION** — the outgoing population cut into members, in the order the comparison tabulates them, under the named-documents ruling (which of the documents the four sections name are compared whole, and which are listed and not compared whole) and a stated passage rule — at `tools/audit/l2_outgoing_population.json` → `the_tabulation_population`, its four new helper functions checked on synthetic lines before any run, every hit line and every decision's home proven by STOP to lie in exactly one member, and every value the artifact held before shown unchanged except the two strings the dispatch named. ★ **THE READING FILE `ratification_surfaces/cowork_comparison_l2_reading.md` IS OPEN**, the blind derivation having been read whole before anything else this session read: **positions 1 to 4 — the four named `ARCHITECTURE.md` sections — are tabulated, one member per commit, every outgoing statement placed under exactly one proposed disposition beside the current-text axis; the writing STOPPED AT THE MEMBER BOUNDARY after position 4 under the dispatch's context rule, and positions 5 onward are UNTOUCHED, not partly worked (D-672)**; the file's own §0 says where the next writing resumes. ★★ **EVERY DISPOSITION IS A PROPOSAL AND NOTHING IS APPLIED**: no outgoing text, derivation, brief, boot pack or register was edited; the five questions the derivation marks for the user are not put; no recommendation is made anywhere. No session booted; no open-items row created, flipped or discarded; no decisions-register identity allocated; no tool source edited but the population tool and the forward bound's authored aiming; no governing document amended but this file; no `src/` file, build, test, golden, score corpus or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_l2_comparison_tabulation_2026_09_27.md` — and no figure is restated here (**D-431**).)*

No existing sentence of `STATUS.md` was rewritten or removed; the prefix moved from the previous batch's
entry to this one, the forward bound's declared adjustment.

**3(b) — the forward bound.** `STATUS.md`'s object was checked at both commits first: `git ls-tree` gives
blob `5a1fb2396e8049dc3d592844244e626b0fd06df8` at `9084a5f8…` (Task 0) and at `6f77e0d2…` (the refs at
0(b)) — the same object. **The aiming set:** `BASE_COMMIT` `9084a5f806cc1745bd7b19be53124f41ffa2e4d8`;
`PREVIOUS_BATCH_DISPATCH` `cc_instruction_l2_outgoing_population_2026_09_27.md`; `ACT_DATE`
`2026-09-27`; `DISPATCH` `cc_instruction_l2_comparison_tabulation_2026_09_27.md`; `TASK` `"Task 3"`;
`MOVE_KIND` `"ordinary"` unchanged; `RULINGS` unchanged; one row appended to `PREVIOUS_AIMINGS` (the
previous batch's aiming was already its last row and was not appended again); each field's former value
named in its comment (#12). Source blob `e401642b2dc263128b74ba7b64ecd01d5f729495` →
`96b0b0abae5563efbfb3a246bda216de153efe87` (`git diff --numstat`: 44 added, 5 removed).

```
$ python tools/audit/gen_status_batch_bound.py --apply
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 2,387 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
exit:0
$ python tools/audit/gen_status_batch_bound.py --check
  entries moved: 1, 2,387 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
exit:0
```

**The entry that moved, by name** (OI-379 — a green `--check` is not the proof): the L2
outgoing-population batch's entry — `status_batch_bound.json` records its opening as `*2026-09-27 (CC —
`records/cc/instructions/cc_instruction_l2_outgoing_population_2026_09_27.md`. **★★ THE L2 COMPARISON'S
OUTGOING POPULATION IS DERIV`, membership `names the dispatch`, `the_one_declared_adjustment_applied:
true`. **The prediction held**: exactly the previous batch's one entry moved; **the two 2026-09-02
entries stayed** (both still open with `*2026-09-02 (CC` in `STATUS.md`) and were not moved by hand; no
STOP. `STATUS_ARCHIVE.md` gained and only gained lines (blob `3e5b63b6bec9bb6e4fb192ff7062854367bf3d17` →
`9fd84ba0620fe88f75d9bc49644009f5ea213efe`: four lines added, none removed).

**3(c) — the regenerations, each then `--check`, all exit 0, no `STOP:` line and no traceback**, in the
order the dispatch gives, `gen_session_start_read_size.py` last after the final edit to `STATUS.md`:

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
exit:0
$ python tools/audit/gen_evidence_pin_membership.py --check
the evidence pin's class membership re-derives
  (the same seven member lines as above)
exit:0
$ python tools/audit/gen_l0_l1_outgoing_population.py
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
exit:0
$ python tools/audit/gen_l0_l1_outgoing_population.py --check
l0_l1_outgoing_population.json re-derives
exit:0
$ python tools/audit/gen_l2_outgoing_population.py
  (the same printout as at 1(c), line for line)
exit:0
$ python tools/audit/gen_l2_outgoing_population.py --check
l2_outgoing_population.json re-derives
exit:0
$ python tools/audit/gen_defense_share.py
wrote tools/audit/defense_share.json
  ...
    of the whole session-start read (247141): 5.24%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
exit:0
$ python tools/audit/gen_defense_share.py --check
the defense-share measurement re-derives
exit:0
$ python tools/audit/gen_session_start_read_size.py
wrote tools/audit/session_start_read_size.json
  ...
    STATUS.md                                                                 11979
  total at the tree 247141
exit:0
$ python tools/audit/gen_session_start_read_size.py --check
the session-start read measurement re-derives
exit:0
```

*(Where a line reads "the same … as above" or "...", the omitted lines are identical to the lines shown
or are the unchanged per-span and per-row lines the previous report prints in full; the full capture is
at the scratch file `regen.txt` beside the guard captures.)*

**What moved, each artifact diffed recursively between its committed blob at `9d96782d…` and the new
blob:**

- **`tools/audit/evidence_pin_membership.json`** (`32e9d7534febcc2e0b1438c277c52262759b9dbf` →
  `54f774d82a2d2e5a9ec99b13666bd83d63ac5257`): **exactly one ruling record read added** —
  `records/cowork/rulings/cowork_rulings_2026_09_27_l2_named_documents_sitting.md`, with `counts` →
  `ruling_records_read` moving with it; **no member moved**. **A3 HOLDS.**
- **`tools/audit/l0_l1_outgoing_population.json`**: **did not move** (same blob
  `e310fb57ac53f9a06f8a9295d70c17ec143e3ce3`).
- **`tools/audit/l2_outgoing_population.json`** (`ddc45c24a658fd1d248b0214f3158a889eacb444` →
  `bd1543118d5bd2e82dd873fa75976477a3ed89a5`): **in the `STATUS.md` RESIDUE record, one hit record
  ADDED** — the term `boundary`, on this batch's new `STATUS.md` entry line (*"THE MEMBER BOUNDARY"*) —
  with that record's `hit_lines_distinct`, `hits` and `hits_per_term` → `boundary` moving with it.
  `STATUS.md` is a residue file, not a member: **no member of the outgoing population or of the
  tabulation population moved**, and no file entered or left the population or the residue. This is the
  movement the dispatch names as expected on a moved `STATUS.md` line.
- **`tools/audit/defense_share.json`** and **`tools/audit/session_start_read_size.json`**: moved only in
  the denominators and totals that `STATUS.md`'s new size moves (the `STATUS.md` per-member characters,
  the session-start total, the two movement rows, and the share of the whole read).
- **`tools/audit/status_batch_bound.json`**: rewritten by the forward bound's `--apply`, as 3(b)
  reports.

**3(d) — the closing guard capture**, write mode, exit 0, saved at
`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\fa31c1c9-3cdd-4d9d-b7b3-6aaa71fac0ce\scratchpad\guard_close.txt`.
**Verdict by verdict against 0(f)**, the whole difference between the two captures (a `diff` of the two
scratch files):

```
59c59
<   [FAIL] tools/audit/gen_evidence_pin_membership.py --check
---
>   [PASS] tools/audit/gen_evidence_pin_membership.py --check
105c105
< 80 guard(s) run, 13 failing, 4 not run, 19 historical record(s)
---
> 80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

**THE CONDITION HOLDS**: every PASS still PASS; `gen_evidence_pin_membership.py --check` moved FAIL →
PASS; every other FAIL the same set; the NOT RUN and HISTORICAL lines identical; population 80. **The
guard classification**, exit 2, naming exactly the four tools of the FACT:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

**E3: MET** — derived from the declared start state plus this batch's footprint: at the tree carrying the
close, population 80; zero STOPs in the runner; the failing set exactly the twelve named, plus none; the
classification STOP unchanged.

---

## 5. The assumptions, graded

- **A1 — HOLDS**, established by the enumeration at 0(c): exactly one tracked modification
  (`tools/audit/claude_md_finer_archive.json`, carried and not chased) and the three untracked landed
  paths; nothing staged.
- **A2 — HOLDS**: thirteen failing at the opening capture — the twelve plus the membership check — zero
  STOPs in the runner; the membership check cleared at 3(c).
- **A3 — HOLDS**: the membership artifact moved by exactly one ruling record read, ruling (2)'s, and no
  member moved.
- **A4 — HOLDS**: no tool added and none enrolled; exactly two tool sources touched,
  `tools/audit/gen_l2_outgoing_population.py` (Task 1) and `tools/audit/gen_status_batch_bound.py`'s
  authored aiming (Task 3); `tools/audit/gen_guard_state.py` not edited; population 80 throughout.
- **A5 — HOLDS**, verified at the objects: `git diff --name-status 6f77e0d2… 9d96782d…` lists only the
  three landed records, the reading file, the population tool and its artifact; the close commit adds only
  the files Task 4 names. The derivation and the brief are at blobs
  `d78ac530992860d38d1f605a77a2961d5440a2f6` (125,549 bytes) and
  `c5ff83dcad2107ac8c05ead21724cbab0d9471fd` (35,952 bytes) at `6f77e0d2…`, at `9d96782d…` and in the
  working tree — the relayed blobs exactly. Nothing under `tools/audit/derivation_boot_pack/l2/`,
  `tools/audit/derivation_boot_pack.json`, the input contract, the L0/L1 reading file, any outgoing text,
  the three named tools, any governing document other than `STATUS.md` and `STATUS_ARCHIVE.md`, or any
  register source appears in the batch's footprint. The close commit's own staged set is proved at Task 4
  and named in the closing message.

---

## 6. Declared departures

1. **The pin was taken after the dispatch was read from the working tree** — the declared-departure
   route of the standing clause (P-2): the session opened the dispatch with the file tools before pinning
   it, pinned it at 0(a), and proved the blob unmoved at staging (0(e) stages `0e21f618…`).
2. **The derivation's and the brief's blobs were verified at the object AFTER Task 2, not before it** —
   the dispatch orders the check *"before Task 2 opens"*, and it was taken at the close instead. Both
   match the relayed blobs at the batch's opening tip, at the latest commit and in the working tree (§5,
   A5), so the file read first is the blob of record; the order is departed from and is declared here.
3. **"Nothing staged" was checked by comparing the index's tree with the tip's tree** (`git write-tree`
   against `6f77e0d2…^{tree}`), not by a `git diff --cached`, which names no explicit hash.
4. **Every commit message carries the exact subject the dispatch gives, followed by a co-author trailer
   line** in the message body; the subject line itself is verbatim.
5. **The two reading rules at the head of the reading file's §6** — headings not counted; defenses listed
   as *not a statement* — are this session's readings of the unit, stated where the user can challenge
   them, not ruled.

Operational notes, not departures: a scratch comparison script failed once on console encoding and was
re-run with UTF-8 output (the artifact was not the cause); the armed shell-read guard denied one
`git diff` whose blob hashes were held in shell variables (deny on indeterminate, by policy), and the
diff was re-run with the literal hashes.

---

## 7. What this batch did NOT do

- **No disposition applied anywhere**; every disposition in the reading file is a proposal; no outgoing
  text, derivation, brief, boot pack, pack artifact, input contract, L0/L1 reading file or register source
  was edited.
- **No decision** on any disposition, difference, open question, the derivation or the method; **no
  verdict** on the deriving session's independence; **no recommendation** in the reading file, this
  report or any commit message. **The five questions the derivation marks for the user (OQ-L2-2, 4, 5, 8,
  16) are not put**; they will be listed ungraded at the reading file's §8, which stays NOT YET WRITTEN.
- **No session booted; no measurement of the analysis built, designed, scoped or run.**
- **No tool source touched but the two A4 names; no guard enrolment; no freeze of the L2 pack.**
- **No open-items row created, flipped or discarded; no decisions-register identity; no `src/` change,
  golden or test; nothing under `tools/corpus/`, `tools/robust_stop/` or `tools/dcml/`.**
- **No disposition of any residue file or of any of the eight LISTED item-2 documents.**
- **Positions 5 to 62 were not tabulated**, and are untouched.

**The plan's tell, in one sentence:** apart from the landed records, the amended tool and its artifact,
the reading file, the Task 3 files and this report, the batch produced nothing in the repository — only
scratch files outside it (the guard captures, the regeneration capture, the path enumerations and three
comparison scripts) and the loose git blob objects written by `git hash-object -w` for the ordered checks.

---

## 8. The self-check, run over the work on disk (the standing clause)

1. **Principles.** **#19** — the reading file establishes nothing and says so (§16); every row carries both
   texts' words, re-placeable at the texts. **#6** — the passage cut lives in the one tool that owns the
   population, its helpers reused. **#12** — the eight LISTED names and the residue are named in §3 and
   stay on the artifact; UNPLACED, SILENT and every DIFFERS are kept; the stop records the untouched
   remainder. **#13** — the synthetic checks ran before the tool; no STOP fired; the order departure (§6
   item 2) is surfaced rather than absorbed. **#17(f)/D-431** — no artifact count is restated in the
   reading file or this report's prose; the tool's printouts are quoted verbatim and pointed at. **#24** —
   no difference between measured quantities is asserted.
2. **Conventions.** American English in this session's prose (British spellings found in the reading file
   during self-review — *neighbours*, *neighbourhood*, *labelled* — were corrected in authored prose and
   left where they sit inside quotations); reserved words checked by search over the reading file after
   each member, and the non-musical uses found (*register*, *part*, *figure*, *measure*, *bar* in the
   prohibiting sense) were corrected before each commit; no invented label left undefined — *member*,
   *passage*, *WITHHELD*, *SEEN* are defined at the file's §1 and §5.
3. **Figures and premises.** Every quantity in this report is a tool's verbatim printout, a git object
   identity, or a pointer to an artifact field or to the reading file's §13; the premises were checked at
   their objects (the refs, the chain, the guard object, the two blobs).
4. **File-tools rule.** Working-tree content was read with the file tools; the shell ran git object
   queries by explicit hash and the sanctioned scripts; the one variable-held `git diff` the guard denied
   was re-run with literal hashes.
5. **Uncertainty.** No comparison of measured quantities is made.

*Provenance: Claude Code, 2026-09-27, executing the dispatch above from its pinned blob. The close
commit carries this file, so its own hash, the pushed branch and `origin/master` after the push are
reported in the session's closing message and are at the git log.*
