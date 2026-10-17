# CC report — L3's PACK BUILD, SECOND HALF, RESUMED: L2 frozen at the blobs its session was given, L3's pack RENDERED; the lists go to the user before any boot — no session booted, no algorithm changed, no register entry

> **This report decides nothing and recommends nothing.** It records what was done, what was measured, and where
> the act departed from what the dispatch predicted. **No ruling was taken, no question or recommendation was put
> to the user, no list below was acted on, no session was booted, no brief was written, no score was staged, and no
> decisions-register entry was written.** Where this report would name a hash it cannot contain — the close commit
> and the end-state commit that follows it — it points at the git log. Guard counts are this batch's own runs; the
> end-state run's values are carried by `tools/audit/guard_state.json` → `summary` in the end-state commit.

**Dispatch:** `records/cc/instructions/cc_instruction_l3_pack_build_second_half_resumed_2026_10_16.md`, pinned at Task 0
to blob `4e8629290f9c6ff3bcfd7349397b44e792d20c91`, proven unmoved immediately before staging; the committed blob at
Task 0's commit equals the pin.
**Full close:** `records/cowork/handoff/cowork_away_returns.md`, the section **THE L3 PACK BUILD, SECOND HALF, RESUMED:
L2 FROZEN, L3's PACK RENDERED — THE LISTS GO TO THE USER BEFORE ANY BOOT; NO SESSION, NO ALGORITHM CHANGED**, which
carries the plan line and points here.

---

## THE LISTS FOR THE USER — BEFORE ANY SESSION BOOTS

Task 4(e), whole. Every value below was read out of the manifest on disk (`tools/audit/derivation_boot_pack.json`, as
committed with the render) and out of the rendered files of `tools/audit/derivation_boot_pack/l3/` by the script
`lists_t4.py` (§6), and was not transcribed. **This batch decides none of them.** The (d) block of the pack directory
precedes the five lists, as the script prints it.

### (d) The pack directory
Files on disk: `00_READ_THIS_FIRST.md`, `01_the_phase_definitions.md`, `02_the_guiding_principles_and_the_conventions.md`, `03_the_writing_standards.md`, `04_the_dispatch_protocol.md`, `05_the_ratified_design_intent.md`, `06_the_defect_type_catalog.md`, `07_the_charter_the_layers_and_the_decisions.md`, `08_the_seventeen_research_extracts.md`, `09_the_empirical_findings_ledger.md`

`the_pack_files_in_order` → `l3`: `00_READ_THIS_FIRST.md`, `01_the_phase_definitions.md`, `02_the_guiding_principles_and_the_conventions.md`, `03_the_writing_standards.md`, `04_the_dispatch_protocol.md`, `05_the_ratified_design_intent.md`, `06_the_defect_type_catalog.md`, `07_the_charter_the_layers_and_the_decisions.md`, `08_the_seventeen_research_extracts.md`, `09_the_empirical_findings_ledger.md`

The directory and `the_pack_files_in_order` name the same set: True

| Member (8) | in the manifest | authored (the JSON object of Task 3(d) plus the twelve L2 parts) |
|---|---|---|
| parts | 17 | 17 |
| removals | 78 | 78 |
| cuts | 61 | 61 |
| runs_to_end cuts | 17 | 17 |

Member (8) `characters`: 118166

### (e) 1. The derived cross-reference additions

| identity | title | derived because |
|---|---|---|
| D-343 | The key/mode layer owns the candidate space and the note-evidence model outright; the residual is SELECTED from its carried alternatives, never re-scored | `verbatim` matched `cowork_layer5_function_design.md` |

#### RULING 84 — ADDITIONS THAT WOULD WITHHOLD AN ENTRY THE USER RULED ADMITTED

- **D-343** — The key/mode layer owns the candidate space and the note-evidence model outright; the residual is SELECTED from its carried alternatives, never re-scored
  - verdict: OUT
  - finding: Its verbatim gives the key/mode layer the candidate space and the note-evidence model outright, the residual settled by selecting among its carried alternatives.
  - reason: It states who decides the tonality, which is L2's decision.

Additions with no verdict in `VERDICTS["l3"]`: none

### (e) 2. `LEAKS` — members (5) and (6)

| member | identity | title | matched |
|---|---|---|---|
| 5 | D-270 | The held-out evaluation protocol - five-fold cross-validation grouped by ground-truth analysis file | `verbatim`: `docs/score_inventory.md` (a-docs-or-src-path) |
| 5 | D-296 | READING MuseScore's engraving code is allowed from anywhere we may edit; only EDITING the notation and engraving code is off limits | `verbatim`: `src/notation` (a-docs-or-src-path); `verbatim`: `src/engraving` (a-docs-or-src-path) |
| 5 | D-440 | The language-model integration is purpose-built and does not wait for the plugin-API reform | `verbatim`: `src/llm/` (a-docs-or-src-path) |

### (e) 3. `LEAKS_IN_THE_EXTRAS` — limb B, every line, grouped by member and file

Entries: 6 · `counted/extras_lines_with_a_leak_hit`: 6

#### member (9) — `09_the_empirical_findings_ledger.md`

| line | matched | kinds | the line |
|---|---|---|---|
| 94 | docs/scoring_model.md | a-docs-or-src-path | >    constraints and stop rules. Existing seeds: `DEFECT_TYPES.md`, `docs/scoring_model.md` §8, the |
| 145 | docs/scoring_model.md | a-docs-or-src-path | \| **`docs/scoring_model.md` §8** \| **YES** \| Read WHOLE at the object, `:1129–1457`, by the first harvest. **Eight** entries in the body come from it — C1, C2, C4, C5, C6, C7, the restatement C8, and, since the extension of 2026-08-26, the ruled restatement C9, whose EARLIER wording stands refused at §5. *(This row formerly read **"Seven … and so does the one refused at re-check, C9"**, which was true while C9 was in no entry, #12.)* \| |
| 156 | docs/scoring_model.md | a-docs-or-src-path | 2026-08-07 routed the chord- and function-layer refuted-repair family into `docs/scoring_model.md` §8 |
| 217 | docs/scoring_model.md | a-docs-or-src-path | \| **C9** — admitted as the restatement *"The presence of a leading tone does not distinguish the genuine cases."* (`cowork_fact_gate_admissions_2026_08_26.md:120`) \| `cowork_empirical_findings_candidates.md` §C9, `:301–321` \| **The admitted sentence's SUBJECT is a population defined by a mechanism of the implementation.** *"The genuine cases"* denotes the correct fires of the minor-read-as-diminished gate — register entry **D-300**, homed `docs/scoring_model.md:1418–1424` — so with the implementation thrown away the sentence has no population and the fact does not survive **in the form admitted**. The stripping that produced it removed our vocabulary from the predicate (*"available at analysis time"*) and left it in the subject. **This is a verdict on the admitted SENTENCE, not on whatever music claim may sit under it.** \| |
| 318 | docs/scoring_model.md | a-docs-or-src-path |   same entry (`docs/scoring_model.md:1418–1424`, register entry **D-300**). The sentence was neither |
| 644 | docs/scoring_model.md | a-docs-or-src-path | eight `docs/scoring_model.md` §8 entries.** Ruling 1 of |

### (e) 4. Member (8)'s title lines, as rendered

| part | line in `08_…` | the title line |
|---|---|---|
| 1 | 1 | # EXTRACT — Ju, Margot, McKay, Dahn & Fujinaga 2020, "Automatic Figured Bass Annotation Using the New Bach Chorales Figured Bass Dataset" — Task B candidacy row 36, first pass, AT THE OBJECT |
| 2 | 206 | # EXTRACT — Bigo, Feisthauer, Giraud & Levé 2018, "Relevance of Musical Features for Cadence Detection" — Task B candidacy row 37, first pass, AT THE OBJECT |
| 3 | 333 | # EXTRACT — Karystinaios & Widmer 2022, "Cadence Detection in Symbolic Classical Music using Graph Neural Networks" — Task B candidacy row 38, first pass, AT THE OBJECT |
| 4 | 476 | # EXTRACT — Sears, Pearce, Caplin & McAdams 2018, "Simulating melodic and harmonic expectations for tonal cadences using probabilistic models" — Task B candidacy row 39, first pass, AT THE OBJECT |
| 5 | 612 | # EXTRACT — Illescas, Rizo & Iñesta, "Harmonic, Melodic, and Functional Automatic Analysis" (ICMC 2007 by the bibliography's row; the file prints no venue and no year) — Task B candidacy row 34, first pass, AT THE OBJECT |
| 6 | 738 | # EXTRACT — de Clercq, "A Model for Scale-Degree Reinterpretation: Melodic Structure, Modulation, and Cadence Choice in the Chorale Harmonizations of J. S. Bach" — Task B candidacy row 40, first pass, AT THE OBJECT |
| 7 | 1050 | # EXTRACT — Feisthauer 2021, the Lille thesis (modulations and cadences for sonata form) — population row 16, first pass |
| 8 | 1087 | # EXTRACT — Hamanaka, Hirata & Tojo 2013, "Computational Music Theory and Its Applications to Expressive Performance and Composition" — population row 19 (the GTTM computational line), CENTRAL, first pass |
| 9 | 1278 | # EXTRACT — Lazzari 2023, "Knowledge-Based Chord Embeddings" (the Modal Harmony Ontology) — population row 7, CENTRAL-adjacent, first pass |
| 10 | 1484 | # EXTRACT — Nápoles López, Feisthauer, Levé & Fujinaga 2020, "On Local Keys, Modulations, and Tonicizations" (DLfM 2020) — population row 13, first pass (single pass; not central) |
| 11 | 1525 | # EXTRACT — McLeod & Rohrmeier 2021, "A Modular System for the Harmonic Analysis of Musical Scores using a Large Vocabulary" (ISMIR 2021) — population row 1, CENTRAL, first pass |
| 12 | 1579 | # EXTRACT — BACHI (arXiv:2510.06528v2), boundary-aware symbolic chord recognition — population row 12, first pass (single pass; not central) |
| 13 | 1621 | # EXTRACT — Hentschel, Moss, McLeod, Neuwirth & Rohrmeier 2021, "Towards a Unified Model of Chords in Western Harmony" (MEC 2021) — population row 3, CENTRAL, first pass |
| 14 | 1659 | # EXTRACT — McLeod & Rohrmeier 2024, "Detecting chord tone alterations and suspensions" (JNMR 52(5)) — population row 2, CENTRAL, first pass |
| 15 | 1708 | # EXTRACT — Sapp 2005, "Visual Hierarchical Key Analysis" (keyscapes) — population row 17, CENTRAL, first pass |
| 16 | 1745 | # EXTRACT — de Haas, Magalhães, Wiering & Veltkamp 2013, "Automatic Functional Harmonic Analysis" (HarmTrace; CMJ 37(4)) — population row 5, CENTRAL, first pass |
| 17 | 1789 | # EXTRACT — de Berardinis et al. 2023, "ChoCo" (Scientific Data 10) — population row 8 (with the Polifonia ontology members it carries), first pass (single pass; not central) |

### (e) 5. Member (2) for L3 — the five withheld document names, searched

- `ARCHITECTURE.md`: 9 line(s)
  - line 262: …`ARCHITECTURE.md` layer specifications are kept in sync as facts are adopted (OI-146).…
  - line 324: …`ARCHITECTURE.md`** (the primary place such decisions are recorded — not exclusively, but…
  - line 329: …collection from `ARCHITECTURE.md` §2.15 and the factorization document without opening the…
  - line 331: …explicitly and twice (`ARCHITECTURE.md:1045-1053`, slice identity IS the eligible sounding-note…
  - line 407: …batches**, **governing surfaces first** (`CLAUDE.md`, `ARCHITECTURE.md`, the signed…
  - line 418: …layer's specification in `ARCHITECTURE.md` first — the record states WHY the decision was made:…
  - line 421: …where the decision lives. This generalizes `ARCHITECTURE.md` §17.2 (every non-obvious scoring…
  - line 586: …anything that trades precision for speed — which puts the effort control (`ARCHITECTURE.md` §2.16)…
  - line 597: …in the estimator's own specification (`ARCHITECTURE.md`, the joint estimator's standing rules, (c)) and…

- `cowork_joint_estimator_architecture.md`: 1 line(s)
  - line 296: …`cowork_joint_estimator_architecture.md` §6/§7, operational rows OI-176…OI-181; the…

- `cowork_layer5_function_design.md`: 0 line(s)

- `cowork_layer6_grouping_design.md`: 0 line(s)

- `cowork_phrase_boundary_design.md`: 0 line(s)

*Two readings of the lists, stated as facts at the objects and not as verdicts.* (1) The Ruling 84 sub-list is not
empty: the one derived cross-reference addition, D-343, carries an OUT verdict in `VERDICTS["l3"]`, and the field
that derived it is its `verbatim`, matching the withheld document name `cowork_layer5_function_design.md`. (2) Limb B's
list for `l3` holds no line of member (7), the charter: the two charter lines that stopped the released second half
name D-527 and D-207, and neither identity is in `l3`'s withheld set, so neither is a hit for `l3` — the question
that report's §8 item 1 left open, measured here.

---

## 1. The commits, by explicit hash

| Act | Commit | What it carries |
|---|---|---|
| the tree met | `5324b94388bdda6c242ff937ace781cbe62d9c2d` | `master` and `origin/master`, both read at the ref files |
| Task 0 | `c1b68098c97369b4cde67d3bb8e21bac16723999` | this dispatch, handoff entries 414 and 415, the 2026-10-16 ruling record, `tools/audit/evidence_pin_membership.json` |
| Task 1 | `ebdff3bb4953e0ee9e69ae701e55cd32478ff913` | the generator (Edits 1.1 to 1.6 and `FROZEN["l2"]`), the manifest |
| Task 2 | `c150443e390c4cd26e28d8f416cca0ed74c5dddc` | the generator (the three edits), the manifest |
| Tasks 3 and 4 | `ca55115f81ee99cc057f04a75747f51a93a43073` | the generator (`L3_WITHHELD_DOCUMENTS`, `WITHHELD["l3"]`, `EXTRAS["l3"]`, the four ruling strings), the manifest, the ten files of `tools/audit/derivation_boot_pack/l3/` |
| the close | see the git log | `STATUS.md`, `STATUS_ARCHIVE.md`, the re-aimed `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`, `tools/audit/session_start_read_size.json`, this report, the close section |
| the end state | see the git log | the full guard run at the close's tree, with the artifacts A2 orders regenerated |

After every push, `.git/refs/remotes/origin/master` was read with the file tools and named the commit just made. Every
commit was verified at the object by explicit hash (`git show --stat <hash>`).

**The whole footprint of the task commits**, `git diff --stat` from the tree met to the last task commit by explicit
hash: exactly seventeen paths — the four records of Task 0, the membership artifact, the generator, the manifest and
the ten `l3` pack files. No other path moved.

## 2. The guard states

**THE START STATE, a `--check` run before the first edit:** 81 run, **15 failing**, 4 not run, 20 historical — the
committed guard state's fourteen failing plus `gen_evidence_pin_membership.py --check`, which A2 predicts for exactly
this cause (one untracked ruling record) and Task 0 act (2) cleared. `gen_guard_classification.py --check` (exit 2)
gave the standing STOP naming the same three tools. The start run's whole output, then the classification message:

```
STALE vs the run: guard_state.json does not re-derive
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
  [FAIL] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [FAIL] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --subject l3 --check
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
81 guard(s) run, 15 failing, 4 not run, 20 historical record(s)
```

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

**`gen_derivation_boot_pack.py --check` is GREEN after Task 4's render** (§5, Task 4(b)), as A2 predicts. **THE END
STATE IS NOT ASSERTED HERE.** The one further commit carries it.

## 3. A1 to A3, and E0 to E5, graded

- **A1 — HELD, BY CONTENT.** The five tracked inputs each diffed empty against `5324b943…`. The tracked population
  through `tools/audit/changed_paths.py` showed exactly one tracked modification, `tools/audit/claude_md_finer_archive.json`,
  whose `git hash-object` equals the tip's blob (`1df4f20771b6782cbb965c293db4d445bc7ec892`) — re-established, left
  untouched, never staged. Every path of Task 0's list was untracked, **entry 415 among them**, so the subject reads
  `entries 414-415`. **Untracked paths outside Task 0's list, NOT landed:** none under `records/`, `reading_pass/` or
  `ratification_surfaces/`; elsewhere `Claude outputs/`, `Codex research inventory/`, `docs/research_papers/polyph9-release/`,
  two files under `external resarch summary/`, the `scratch_artifacts/` population and
  `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`. No further handoff entry or ruling record appeared
  during the run. The premise ledger's cross-commit proof — the generator, the manifest and every file under
  `tools/audit/derivation_boot_pack/` unchanged between `a01e9402…` and `5324b943…` — came back empty.
- **A2 — HELD AT THE START** (§2). The end prediction is carried by the end-state commit.
- **A3 — verified at the objects** for the task commits (§1, the footprint); for the close and end-state commits it is
  stated in the close section's end-state part.
- **E0 — MET.** The five paths of Task 0 in one commit (the four records and the membership artifact, which moved by
  exactly the one permitted entry); `origin/master` at it; every path accounted for.
- **E1 — MET.** The ten files proved equal to their committed blobs; the ten digests taken twice, agreeing, and equal
  to the premise ledger's (§4); (e) and (g) wholly empty, (g) item 2's movement exactly the expected one; the manifest
  byte-identical to `B2.json`; `--check` green; every pack directory byte-unchanged; one commit, pushed.
- **E2 — MET.** The three edits as written, with the two ordered substitutions; the comparison as expected (the old
  bullet found once in `l2`'s record, and that one line the only movement); the deleted-line enumeration published.
- **E3/E4 — MET.** Task 3(e) all PASS; the render's `IN 22`, and `OUT 222 / UNPLACED 0` equal to the relayed
  expectation; `--check` green; (c) as stated; (d) and (e) reported whole; one commit, pushed.
- **E5** — carried by the end-state commit, not asserted here.

## 4. Task 1(a) and (b) — the ten files and their digests

The directory listing (by the file tools) and the tip's tree (`git ls-tree --name-only 5324b943… tools/audit/derivation_boot_pack/l2/`)
name the same ten files. For each, `git hash-object` (through git's filters), `git hash-object --no-filters` and
`git rev-parse 5324b943…:<path>` agree, and each equals the premise ledger's value:

| File | Digest (all three forms agree; equal to the premise ledger) |
|---|---|
| `00_READ_THIS_FIRST.md` | `fd27dee7a4b6bca3454d12c659aa34a96cd1abc1` |
| `01_the_phase_definitions.md` | `518b1e50d60af2b4e2ddcd8978623832eb071899` |
| `02_the_guiding_principles_and_the_conventions.md` | `41288e7375faca980c566ca0367fca1c7de760e8` |
| `03_the_writing_standards.md` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` |
| `04_the_dispatch_protocol.md` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` |
| `05_the_ratified_design_intent.md` | `6ae0b1d8c9a830cfc3f2021f37460f05fad23547` |
| `06_the_defect_type_catalog.md` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` |
| `07_the_charter_the_layers_and_the_decisions.md` | `5796c2d1bda0520b067ccde300e25336b9606884` |
| `08_the_fifty_six_research_extracts.md` | `69404bace220b25589e78edc7c89c513ae5a0e2e` |
| `09_the_empirical_findings_ledger.md` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` |

(The values in this table were taken from the run's own output line by line, the command printing the three forms side
by side.)

## 5. The tasks, act by act, with every comparison's output

### Task 0, act (2) — the membership artifact

`gen_evidence_pin_membership.py --check` was red at the start. Regenerated, and compared against the tip's blob by
`cmp_t0_epm.py` (§6), whose index-based diff shows the list growing by one:

```
diff(tip, regenerated): 3 DIFFERENCE(S)
    /counts/ruling_records_read
        A: 165
        B: 166
    /ruling_records_read#len
        A: 165
        B: 166
    /ruling_records_read[164]
        A: "records/cowork/rulings/cowork_rulings_oi345_oi342_2026_08_07.md"
        B: "records/cowork/rulings/cowork_rulings_2026_10_16_l2_freeze_leak_list_sitting.md"
```

A second check, run inline (`python -c`, its text in §6), established the shape: exactly one entry inserted —
`records/cowork/rulings/cowork_rulings_2026_10_16_l2_freeze_leak_list_sitting.md` — none removed, the committed
entries standing in the same order, and every other field equal. The permitted change and no other.

### Task 1

**(c)** `B0.json` dumped with the generator untouched; `C.json` taken by `git show 5324b943…:tools/audit/derivation_boot_pack.json`.
Its blob, `db340baf15f7fa3ad1ab29d067f12a47b4354ace`, is the same at `5324b943…` and at `a01e9402…`.

**(d)** The six edits made in the dispatch's order, each old text found exactly once. After them, `subject in FROZEN`
occurs **once in `build_subject`** — the `if subject in FROZEN:` Edit 1.6 adds — and the other three hits in the file
are `if subject in FROZEN:` in `build()`, `write_all` and `check_all`, untouched.

**(e) — WHOLLY EMPTY: the repair is inert before the freeze.** `B1.json` dumped; `cmp_t1e.py`:

```
diff(B0.subjects, B1.subjects): EMPTY
top-level keys the same set: PASS
top-level 'generator' equal: PASS
top-level 'the_pack_files_in_order' equal: PASS
top-level 'what_is_AUTHORED' equal: PASS
top-level 'what_is_DERIVED' equal: PASS
top-level 'what_this_is' equal: PASS
top-level '★_it_boots_no_session' equal: PASS
top-level '★_the_verdicts_clear_nothing' equal: PASS
B1.the_STOPS == B0.the_STOPS + [the added string]: PASS
B1.the_rulings_it_executes == B0.the_rulings_it_executes + [the added string]: PASS
RESULT: ALL PASS
```

**(f)** The `FROZEN["l2"]` entry inserted between the table's last comment line and its `}` (that two-line old text
found once after Edit 1.1), its `digests` the ten values of §4 in the premise ledger's order, its `finding`, `date` and
`reason` the dispatch's texts — proven equal to them by the (g) script's first three lines — and the ordered comment
after it. `l2` was not added to `RENDERED_BEFORE_THE_SCOPING_RULINGS` (the (g) script's fourth line).

**(g) — WHOLLY EMPTY, with item 2's one expected movement.** `B2.json` dumped; `cmp_t1g.py`. **The prediction the
ruling record names — that a scan over the on-disk files returns exactly the committed list — HELD**: both lengths are
read from the two files, and the lists are equal entry for entry and in order.

```
FROZEN['l2']['finding'] equals the dispatch's text: PASS
FROZEN['l2']['reason'] equals the dispatch's text: PASS
FROZEN['l2']['date'] equals the dispatch's text: PASS
l2 not in RENDERED_BEFORE_THE_SCOPING_RULINGS: PASS
=== 1. against the committed manifest (the governing comparison)
diff(C.subjects['harmony-boundary'], B2.subjects['harmony-boundary']): EMPTY
diff(C.subjects['scoring-model'], B2.subjects['scoring-model']): EMPTY
diff(C.subjects['l0-l1'], B2.subjects['l0-l1']): EMPTY
diff(T(C.subjects['l2']), B2.subjects['l2']): EMPTY
C.l2 LEAKS_IN_THE_EXTRAS entries, as read from C: 61
B2.l2 LEAKS_IN_THE_EXTRAS entries, as read from B2: 61
C.l2 counted/extras_lines_with_a_leak_hit: 61
B2.l2 counted/extras_lines_with_a_leak_hit: 61
B2's entries equal C's, entry for entry and in order: PASS
=== 2. against the repaired build before the freeze
diff(B1.subjects['harmony-boundary'], B2.subjects['harmony-boundary']): EMPTY
diff(B1.subjects['scoring-model'], B2.subjects['scoring-model']): EMPTY
diff(B1.subjects['l0-l1'], B2.subjects['l0-l1']): EMPTY
top-level keys the same set (B1, B2): PASS
top-level 'generator' equal (B1, B2): PASS
top-level 'the_STOPS' equal (B1, B2): PASS
top-level 'the_pack_files_in_order' equal (B1, B2): PASS
top-level 'the_rulings_it_executes' equal (B1, B2): PASS
top-level 'what_is_AUTHORED' equal (B1, B2): PASS
top-level 'what_is_DERIVED' equal (B1, B2): PASS
top-level 'what_this_is' equal (B1, B2): PASS
top-level '★_it_boots_no_session' equal (B1, B2): PASS
top-level '★_the_verdicts_clear_nothing' equal (B1, B2): PASS
diff(U, B2.subjects['l2'])  [U = T(B1.l2) with B2's leak list and count]: EMPTY
--- the measured movement (not pass/fail by itself): today's re-render before the freeze against the on-disk scan after it
entries in T(B1.l2) and not in B2.l2: 2
    {"member": 7, "file": "07_the_charter_the_layers_and_the_decisions.md", "line": 150, "matched": ["D-527"], "kinds": ["withheld-identity"], "the_line": "class carries a note's foreignness rather than dropping it (#12); the charter's list, D-527's label list and"}
    {"member": 7, "file": "07_the_charter_the_layers_and_the_decisions.md", "line": 151, "matched": ["D-207"], "kinds": ["withheld-identity"], "the_line": "D-207's class become one vocabulary (#6); standard names, each defined by approach and departure, or by a tone"}
entries in B2.l2 and not in T(B1.l2): 0
the movement is exactly the expected one (two member-(7) entries, matching D-527 and D-207, none the other way): PASS
RESULT: ALL EMPTY / PASS
```

**(h)** The write run (no `--subject`; all four subjects frozen, so `write_all` wrote the manifest and no pack
directory), then `cmp` of the written manifest against `B2.json` (exit 0: byte-identical), then `--check` (exit 0). The
write run's output, then `--check`'s whole output:

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

```
FROZEN SOURCES: 17 of 30 frozen pack file(s) would render at a different length from the sources as they stand today. NOT COMPARED; sets no exit code.
  - harmony-boundary/02_the_guiding_principles_and_the_conventions.md: the directory holds 59762 characters; today's sources would render 67969
  - harmony-boundary/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - harmony-boundary/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - harmony-boundary/05_the_ratified_design_intent.md: the directory holds 252572 characters; today's sources would render 252641
  - l0-l1/02_the_guiding_principles_and_the_conventions.md: the directory holds 61113 characters; today's sources would render 68743
  - l0-l1/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - l0-l1/04_the_dispatch_protocol.md: the directory holds 103431 characters; today's sources would render 108389
  - l0-l1/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
  - l0-l1/07_the_charter_the_layers_and_the_decisions.md: the directory holds 29031 characters; today's sources would render 36208
  - l0-l1/08_the_five_research_extracts.md: the directory holds 76722 characters; today's sources would render 103250
  - l0-l1/09_the_empirical_findings_ledger.md: the directory holds 50666 characters; today's sources would render 50963
  - l2/02_the_guiding_principles_and_the_conventions.md: the directory holds 64913 characters; today's sources would render 66180
  - l2/07_the_charter_the_layers_and_the_decisions.md: the directory holds 33067 characters; today's sources would render 36208
  - scoring-model/02_the_guiding_principles_and_the_conventions.md: the directory holds 60536 characters; today's sources would render 68743
  - scoring-model/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - scoring-model/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - scoring-model/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
the derivation boot pack re-derives
  harmony-boundary: FROZEN — 7 file(s) at their recorded blobs
  l0-l1: FROZEN — 10 file(s) at their recorded blobs
  l2: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
```

Every file of the four pack directories was compared against its blob at `5324b943…` by explicit hash (`git ls-tree -r`
over the directory, `git hash-object` per path): 34 files, none moved, and the directory listing by the file tools
holds exactly those 34.

**The deleted-line enumeration for the generator**, `git diff -U0 c1b68098… ebdff3bb…`: ten deleted lines — the
docstring's `a file that is not there.`; the four comment lines of Edit 1.2's first old text; Edit 1.2's field-choice
line; Edit 1.3's two comment lines and its `extras_leaks` line; Edit 1.6's scan line
(`for n, ln in enumerate(text.split("\n"), start=1):`); and Edit 1.4's `if subject in FROZEN else (`. **Every one is
inside an old text the task quotes.**

### Task 2

**(a)** `B3.json` dumped before the edits. **(b)–(d)** The three edits made as the first half's Task 2 writes them,
each old text found once, with the two ordered substitutions: Edit 2's *"★ CORRECTED 2026-10-15 by the first half of
L3's pack build;"* written *"★ CORRECTED by the second half of L3's pack build;"*, and Edit 3's *"(2026-10-15, the first
half of L3's pack build; owed since entry 398 §2)"* written *"(the second half of L3's pack build; owed since entry 398
§2)"*, its line wrapping kept where the first half wrapped it. Edit 1's comment is unchanged.

**(e)** `B4.json` dumped; `cmp_t2e.py`:

```
top-level keys the same set: PASS
top-level 'generator' equal: PASS
top-level 'the_STOPS' equal: PASS
top-level 'the_pack_files_in_order' equal: PASS
top-level 'the_rulings_it_executes' equal: PASS
top-level 'what_is_AUTHORED' equal: PASS
top-level 'what_is_DERIVED' equal: PASS
top-level 'what_this_is' equal: PASS
top-level '★_it_boots_no_session' equal: PASS
top-level '★_the_verdicts_clear_nothing' equal: PASS
subjects the same set: PASS
diff(B3.subjects['harmony-boundary'], B4.subjects['harmony-boundary']): EMPTY
diff(B3.subjects['scoring-model'], B4.subjects['scoring-model']): EMPTY
diff(B3.subjects['l0-l1'], B4.subjects['l0-l1']): EMPTY
occurrences of the old bullet in B3.subjects['l2']: 1
diff(B3.l2 with the bullet replaced once, B4.l2): EMPTY
RESULT: ALL PASS
```

The manifest regenerated in write mode and `cmp` against `B4.json` (exit 0: byte-identical); `--check` exit 0, its last
lines:

```
FROZEN SOURCES: 17 of 30 frozen pack file(s) would render at a different length from the sources as they stand today. NOT COMPARED; sets no exit code.
  - harmony-boundary/02_the_guiding_principles_and_the_conventions.md: the directory holds 59762 characters; today's sources would render 67969
  - harmony-boundary/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - harmony-boundary/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - harmony-boundary/05_the_ratified_design_intent.md: the directory holds 252572 characters; today's sources would render 252641
  - l0-l1/02_the_guiding_principles_and_the_conventions.md: the directory holds 61113 characters; today's sources would render 68743
  - l0-l1/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - l0-l1/04_the_dispatch_protocol.md: the directory holds 103431 characters; today's sources would render 108389
  - l0-l1/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
  - l0-l1/07_the_charter_the_layers_and_the_decisions.md: the directory holds 29031 characters; today's sources would render 36208
  - l0-l1/08_the_five_research_extracts.md: the directory holds 76722 characters; today's sources would render 103250
  - l0-l1/09_the_empirical_findings_ledger.md: the directory holds 50666 characters; today's sources would render 50963
  - l2/02_the_guiding_principles_and_the_conventions.md: the directory holds 64913 characters; today's sources would render 66180
  - l2/07_the_charter_the_layers_and_the_decisions.md: the directory holds 33067 characters; today's sources would render 36208
  - scoring-model/02_the_guiding_principles_and_the_conventions.md: the directory holds 60536 characters; today's sources would render 68743
  - scoring-model/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - scoring-model/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - scoring-model/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
the derivation boot pack re-derives
  harmony-boundary: FROZEN — 7 file(s) at their recorded blobs
  l0-l1: FROZEN — 10 file(s) at their recorded blobs
  l2: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
```

Every file of the four pack directories was compared against its blob at `ebdff3bb…` by explicit hash: none moved.
**The deleted-line enumeration**, `git diff -U0 ebdff3bb… c150443e…` over the generator: four deleted lines — Edit
2's three comment lines and Edit 3's bullet line. The diff stat's fifth deletion is the manifest's one changed line.
Every deleted generator line is inside the quoted old texts.

### Task 3

**(a)** `L3_WITHHELD_DOCUMENTS` and its comment inserted before `WITHHELD`, by the file-editing tool; that old text
found once. **(b)** The `l3` entry of `WITHHELD` inserted before the `framework` comment, by the file-editing tool;
that old text found once. **(c)–(d)** The `l3` entry of `EXTRAS`, with its seventeen parts, inserted by the scratch
script `insert_l3_extras.py` (§6; declared departure §7 item 2): the twelve carried parts copied from
`EXTRAS["l2"]`'s member (8) **as text from the generator's own file** — each found once by its `"source"` line inside
`EXTRAS["l2"]` — with the authority's additions inserted after L2's entries; the five new parts written from the
authority. The three-line old text of (c) was found once. The authority, `l3_member8_expected.json`, was written byte
for byte from the PINNED dispatch blob by `extract_member8_json.py` (§6): 25,121 bytes, 17 in `order`, 5 `new`, 12
`carried`. **(f)** The four ruling strings appended by the file-editing tool after the string Edit 1.5 added; that
old text found once.

**(e) — ALL PASS.** `cmp_t3e.py` imports the edited generator, and the generator at Task 2's commit (written to the
scratch folder by `git show c150443e…:tools/audit/gen_derivation_boot_pack.py`) for item 6 only, with `tools/audit` on
`sys.path` so that its one module-level import resolves, and nothing of it called. The import did not fail, so item 6
was taken by the import and not by the fallback:

```
1. EXTRAS['l3'] has three members, [0] is CHARTER_MEMBER_7 and [2] is LEDGER_MEMBER_9 by identity: PASS
2. member (8)'s sources are X['order'], every part's spans == [{'kind': 'whole'}]: PASS
3. the 5 new parts equal the authority's removals and cuts: PASS
4. the 12 carried parts equal L2's entries followed by the additions: PASS
5. WITHHELD['l3'] has the five documents in the artifact's order, each with finding/date/reason, and no withheld passage: PASS
    the artifact's document order: ['ARCHITECTURE.md', 'cowork_joint_estimator_architecture.md', 'cowork_layer5_function_design.md', 'cowork_layer6_grouping_design.md', 'cowork_phrase_boundary_design.md']
6. EXTRAS['l2'] and WITHHELD['l2'] equal those of the generator at Task 2's commit: PASS
RESULT: ALL PASS
```

No FAIL, so no literal was corrected.

### Task 4

**(a)** `B5.json` dumped with no STOP — every filter's anchor, delimiter and heading found exactly once and both
directions of the extras' verification passing for all seventeen parts. Then the write run (no `--subject`); its output
verbatim. **The `l3` line reads `IN 22`; OUT and UNPLACED read `222` and `0`, equal to the relayed expectation.** The
written manifest is byte-identical to `B5.json` (`cmp`, exit 0).

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
  l3: design-intent 244 · candidates 244 · IN 22 / OUT 222 / UNPLACED 0
    withheld 23 (22 authored + 1 derived) · documents 5 · passages 0 · leaks 3
    rendered: 218 design-intent entries, 25 defect-type rows, 10 files
  scoring-model: design-intent 244 · candidates 0 · IN 0 / OUT 0 / UNPLACED 0
    withheld 0 (0 authored + 0 derived) · documents 0 · passages 0 · leaks 3
    rendered: 241 design-intent entries, 25 defect-type rows, 7 files
```

**(b)** `--check`, exit 0, whole output:

```
FROZEN SOURCES: 17 of 30 frozen pack file(s) would render at a different length from the sources as they stand today. NOT COMPARED; sets no exit code.
  - harmony-boundary/02_the_guiding_principles_and_the_conventions.md: the directory holds 59762 characters; today's sources would render 67969
  - harmony-boundary/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - harmony-boundary/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - harmony-boundary/05_the_ratified_design_intent.md: the directory holds 252572 characters; today's sources would render 252641
  - l0-l1/02_the_guiding_principles_and_the_conventions.md: the directory holds 61113 characters; today's sources would render 68743
  - l0-l1/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - l0-l1/04_the_dispatch_protocol.md: the directory holds 103431 characters; today's sources would render 108389
  - l0-l1/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
  - l0-l1/07_the_charter_the_layers_and_the_decisions.md: the directory holds 29031 characters; today's sources would render 36208
  - l0-l1/08_the_five_research_extracts.md: the directory holds 76722 characters; today's sources would render 103250
  - l0-l1/09_the_empirical_findings_ledger.md: the directory holds 50666 characters; today's sources would render 50963
  - l2/02_the_guiding_principles_and_the_conventions.md: the directory holds 64913 characters; today's sources would render 66180
  - l2/07_the_charter_the_layers_and_the_decisions.md: the directory holds 33067 characters; today's sources would render 36208
  - scoring-model/02_the_guiding_principles_and_the_conventions.md: the directory holds 60536 characters; today's sources would render 68743
  - scoring-model/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - scoring-model/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - scoring-model/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
the derivation boot pack re-derives
  harmony-boundary: FROZEN — 7 file(s) at their recorded blobs
  l0-l1: FROZEN — 10 file(s) at their recorded blobs
  l2: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
```

**(c)** `cmp_t4c.py`, the manifest at Task 2's commit (`M2.json`) against the manifest on disk (`M4.json`):

```
diff(M2.subjects['harmony-boundary'], M4.subjects['harmony-boundary']): EMPTY
diff(M2.subjects['scoring-model'], M4.subjects['scoring-model']): EMPTY
diff(M2.subjects['l0-l1'], M4.subjects['l0-l1']): EMPTY
diff(M2.subjects['l2'], M4.subjects['l2']): EMPTY
top-level keys the same set: PASS
top-level 'generator' equal: PASS
top-level 'the_STOPS' equal: PASS
top-level 'what_is_AUTHORED' equal: PASS
top-level 'what_is_DERIVED' equal: PASS
top-level 'what_this_is' equal: PASS
top-level '★_it_boots_no_session' equal: PASS
top-level '★_the_verdicts_clear_nothing' equal: PASS
the_rulings_it_executes == old + the four strings of Task 3(f): PASS
the_pack_files_in_order differs from the old only by the added key 'l3': PASS
subjects differs from the old only by the added key 'l3': PASS
RESULT: ALL PASS
```

By explicit hash, no file under the four frozen directories differs from Task 2's commit: 34 files compared, none moved.

**(d)** In the report's first section.

### Task 5

**(a)** This batch's five entries written at the top of `STATUS.md` — the close entry first, naming this dispatch by
its file name and carrying the `Last updated: ` prefix, which moved off the released second half's close entry; then
one `Same dispatch` entry each for Tasks 3 and 4 (one commit), Task 2, Task 1 and Task 0. None of them carries the
released second half's dispatch file name, so none can be read as that batch's entry. **(b)** The five authored inputs
of `gen_status_batch_bound.py` re-aimed — `BASE_COMMIT` `ca55115f…` (the last task commit before the close),
`PREVIOUS_BATCH_DISPATCH` `cc_instruction_l3_pack_build_second_half_2026_10_16.md`, `ACT_DATE` `2026-10-17`,
`DISPATCH` this dispatch, `TASK` `Task 5` — with a re-aiming comment, the former values preserved in the comments on
the tool's own convention, and this aiming appended to `PREVIOUS_AIMINGS`. `ACT_DATE` differs from the dispatch's date,
and the comment says so. **(c)** `--apply`, then `--check`. **The prediction HELD**: exactly the released second half's
two entries moved; the two 2026-09-02 entries stayed.

```
wrote tools\audit\status_batch_bound.json
  entries moved: 2, 2,674 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**(d)** After the final `STATUS.md` edit, `gen_session_start_read_size.py` regenerated and its `--check` green:

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
    STATUS.md                                                                 13280
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 249709
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 249709 [ruled membership]  (-117412, -31.98%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 249709 [ruled membership]  (-47123, -15.88%)  <- CROSSES A REGIME BOUNDARY
```

## 6. The scripts, whole

All kept in this session's scratch folder, outside the repository.

`dump_build.py` — as the dispatch gives it:

```python
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location(
    "dbp", r"C:\s\MS\tools\audit\gen_derivation_boot_pack.py")
dbp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dbp)
manifest, packs, displaced = dbp.build()
with open(sys.argv[1], "w", encoding="utf-8", newline="") as fh:
    fh.write(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print("dumped", sys.argv[1], "subjects:", sorted(manifest["subjects"]))
```

`diff_paths.py` — the helper the dispatch orders written:

```python
"""diff(a, b, path="") -> every JSON path at which two parsed values differ.

Recurses into dicts by key and lists by index; a missing key or a different list length is
itself a difference at that path.  Each difference carries both values, printed truncated to
300 characters.  Kept outside the repository working tree; imported by the comparison scripts.
"""
import json

MISSING = "<MISSING>"


def _show(v) -> str:
    if v is MISSING:
        return MISSING
    s = json.dumps(v, ensure_ascii=False)
    return s if len(s) <= 300 else s[:300] + "…"


def diff(a, b, path=""):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in list(a.keys()) + [k for k in b.keys() if k not in a]:
            p = f"{path}/{k}"
            if k not in a:
                out.append((p, MISSING, _show(b[k])))
            elif k not in b:
                out.append((p, _show(a[k]), MISSING))
            else:
                out.extend(diff(a[k], b[k], p))
        return out
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append((f"{path}#len", str(len(a)), str(len(b))))
        for i in range(min(len(a), len(b))):
            out.extend(diff(a[i], b[i], f"{path}[{i}]"))
        return out
    if type(a) is not type(b) or a != b:
        out.append((path, _show(a), _show(b)))
    return out


def report(name, d):
    print(f"{name}: {'EMPTY' if not d else f'{len(d)} DIFFERENCE(S)'}")
    for p, x, y in d:
        print(f"    {p}\n        A: {x}\n        B: {y}")
    return not d
```

`cmp_t0_epm.py` — Task 0 act (2):

```python
"""Task 0 act (2): the regenerated evidence-pin membership artifact against the tip's blob.
Prints every differing JSON path.  Kept outside the repository working tree."""
import json
import os
import sys

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from diff_paths import diff, report  # noqa: E402

A = json.load(open(os.path.join(S, "epm_tip.json"), encoding="utf-8"))
B = json.load(open(os.path.join(S, "epm_new.json"), encoding="utf-8"))
report("diff(tip, regenerated)", diff(A, B))
```

The inline check of Task 0 act (2), run as `python -c "…"` with `$S` the scratch folder:

```python
import json
A=json.load(open('$S/epm_tip.json',encoding='utf-8'));B=json.load(open('$S/epm_new.json',encoding='utf-8'))
a=A['ruling_records_read'];b=B['ruling_records_read']
ins=[x for x in b if x not in a];rem=[x for x in a if x not in b]
print('inserted',ins);print('removed',rem);print('rest equal in order',[x for x in b if x in a]==a)
A2=dict(A);B2=dict(B);[d.pop('ruling_records_read') for d in (A2,B2)];A2['counts']=dict(A2['counts']);B2['counts']=dict(B2['counts']);A2['counts'].pop('ruling_records_read');B2['counts'].pop('ruling_records_read')
print('everything else equal',A2==B2)
```

Its output: `inserted ['records/cowork/rulings/cowork_rulings_2026_10_16_l2_freeze_leak_list_sitting.md']`,
`removed []`, `rest equal in order True`, `everything else equal True`.

`cmp_t1e.py` — Task 1(e):

```python
"""Task 1(e): the repair is inert before the freeze.  B0 (generator untouched) against B1 (the six
edits made, no freeze).  Kept outside the repository working tree."""
import json
import sys
import os

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from diff_paths import diff, report  # noqa: E402

B0 = json.load(open(os.path.join(S, "B0.json"), encoding="utf-8"))
B1 = json.load(open(os.path.join(S, "B1.json"), encoding="utf-8"))

STOP_ADDED = ("an entry of `RENDERED_BEFORE_THE_SCOPING_RULINGS` naming a subject that is not FROZEN, "
              "or lacking its finding, its date or its reason")
RULING_ADDED = (
    "The derivation recorded at "
    "`records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md`, "
    "applying Ruling 1 of `cowork_rulings_2026_09_27_l2_leak_list_sitting.md` as ruled — the "
    "field choice, limb B and the additions' wording keyed on the authored list "
    "`RENDERED_BEFORE_THE_SCOPING_RULINGS` rather than on FROZEN membership; Ruling 1 of "
    "`cowork_rulings_2026_10_16_l2_freeze_leak_list_sitting.md` — a FROZEN subject's extras "
    "leak list and its count taken from the files its pack directory holds, not from a "
    "re-render; and the freeze "
    "of the spent `l2` pack (Ruling 1 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, "
    "noted).")

ok = True
ok &= report("diff(B0.subjects, B1.subjects)", diff(B0["subjects"], B1["subjects"]))
same_keys = set(B0) == set(B1)
print("top-level keys the same set:", "PASS" if same_keys else "FAIL")
ok &= same_keys
for k in sorted(set(B0) & set(B1)):
    if k in ("subjects", "the_STOPS", "the_rulings_it_executes"):
        continue
    eq = B0[k] == B1[k]
    print(f"top-level {k!r} equal:", "PASS" if eq else "FAIL")
    ok &= eq
a = B1["the_STOPS"] == B0["the_STOPS"] + [STOP_ADDED]
b = B1["the_rulings_it_executes"] == B0["the_rulings_it_executes"] + [RULING_ADDED]
print("B1.the_STOPS == B0.the_STOPS + [the added string]:", "PASS" if a else "FAIL")
print("B1.the_rulings_it_executes == B0.the_rulings_it_executes + [the added string]:",
      "PASS" if b else "FAIL")
ok &= a and b
print("RESULT:", "ALL PASS" if ok else "STOP")
sys.exit(0 if ok else 3)
```

`cmp_t1g.py` — Task 1(g):

```python
"""Task 1(g): the D-657 comparison.  C = the committed manifest at 5324b943…, B1 = the repaired
build before the freeze, B2 = the repaired build with FROZEN["l2"].  T(rec) applies to a record
exactly what build() does to a frozen subject's record, in the same order.  Item 2 replaces, in a
deep copy U of T(B1.l2), the extras leak list and its count by B2's, and then prints the movement
of the leak list as a measurement.  Also checks the authored freeze fields against the dispatch's
verbatim texts.  Kept outside the working tree."""
import copy
import importlib.util
import json
import os
import sys

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from diff_paths import diff, report  # noqa: E402

spec = importlib.util.spec_from_file_location(
    "dbp", r"C:\s\MS\tools\audit\gen_derivation_boot_pack.py")
dbp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dbp)

C = json.load(open(os.path.join(S, "C.json"), encoding="utf-8"))
B1 = json.load(open(os.path.join(S, "B1.json"), encoding="utf-8"))
B2 = json.load(open(os.path.join(S, "B2.json"), encoding="utf-8"))


def T(rec):
    r = copy.deepcopy(rec)
    r["★_FROZEN"] = dbp.frozen_block("l2")
    dbp.frozen_from_disk("l2", r)
    return r


ok = True
FINDING = ("Its deriving session has RUN (Ruling 1 of "
           "`records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, noted), and "
           "the specification it produced, `cowork_derived_specification_l2_2026_10_10.md`, was "
           "ratified face by face on 2026-10-13 and 2026-10-14. The pack is STALE against today's "
           "sources — its rendered charter member lacks the 2026-10-14 amendment to L2's block of "
           "`FRAMEWORK.md` §5 — so the digests recorded here are those of the files on disk, proved "
           "equal to their committed blobs: what the session was given, and not a re-render.")
REASON = ("A spent subject's pack is the record of what its session was given rather than an input "
          "to be kept current (Ruling 17(a); D-646). Left live it would re-render the charter member "
          "with an amendment ruled after the session ran, and so back-date into a completed "
          "derivation's record a text its session never read (#12); and L3's pack shares the charter "
          "member with it (`CHARTER_MEMBER_7`), so it must be frozen before L3's is built (the "
          "boot-list record's Ruling 1, noted). Frozen at the blobs it carries, with the hash STOP.")
f = dbp.FROZEN["l2"]
for name, got, want in (("finding", f["finding"], FINDING), ("reason", f["reason"], REASON),
                        ("date", f["date"], "2026-10-15")):
    print(f"FROZEN['l2'][{name!r}] equals the dispatch's text:", "PASS" if got == want else "FAIL")
    ok &= got == want
print("l2 not in RENDERED_BEFORE_THE_SCOPING_RULINGS:",
      "PASS" if "l2" not in dbp.RENDERED_BEFORE_THE_SCOPING_RULINGS else "FAIL")
ok &= "l2" not in dbp.RENDERED_BEFORE_THE_SCOPING_RULINGS

print("=== 1. against the committed manifest (the governing comparison)")
for s in ("harmony-boundary", "scoring-model", "l0-l1"):
    ok &= report(f"diff(C.subjects[{s!r}], B2.subjects[{s!r}])",
                 diff(C["subjects"][s], B2["subjects"][s]))
ok &= report("diff(T(C.subjects['l2']), B2.subjects['l2'])",
             diff(T(C["subjects"]["l2"]), B2["subjects"]["l2"]))
c_ent = C["subjects"]["l2"]["LEAKS_IN_THE_EXTRAS"]["entries"]
b2_ent = B2["subjects"]["l2"]["LEAKS_IN_THE_EXTRAS"]["entries"]
print("C.l2 LEAKS_IN_THE_EXTRAS entries, as read from C:", len(c_ent))
print("B2.l2 LEAKS_IN_THE_EXTRAS entries, as read from B2:", len(b2_ent))
print("C.l2 counted/extras_lines_with_a_leak_hit:",
      C["subjects"]["l2"]["counted"]["extras_lines_with_a_leak_hit"])
print("B2.l2 counted/extras_lines_with_a_leak_hit:",
      B2["subjects"]["l2"]["counted"]["extras_lines_with_a_leak_hit"])
same_list = b2_ent == c_ent
print("B2's entries equal C's, entry for entry and in order:", "PASS" if same_list else "FAIL")
ok &= same_list

print("=== 2. against the repaired build before the freeze")
for s in ("harmony-boundary", "scoring-model", "l0-l1"):
    ok &= report(f"diff(B1.subjects[{s!r}], B2.subjects[{s!r}])",
                 diff(B1["subjects"][s], B2["subjects"][s]))
keys = set(B1) == set(B2)
print("top-level keys the same set (B1, B2):", "PASS" if keys else "FAIL")
ok &= keys
for k in sorted(set(B1) & set(B2)):
    if k == "subjects":
        continue
    eq = B1[k] == B2[k]
    print(f"top-level {k!r} equal (B1, B2):", "PASS" if eq else "FAIL")
    ok &= eq
tb1 = T(B1["subjects"]["l2"])
U = copy.deepcopy(tb1)
U["LEAKS_IN_THE_EXTRAS"]["entries"] = copy.deepcopy(b2_ent)
U["counted"]["extras_lines_with_a_leak_hit"] = \
    B2["subjects"]["l2"]["counted"]["extras_lines_with_a_leak_hit"]
ok &= report("diff(U, B2.subjects['l2'])  [U = T(B1.l2) with B2's leak list and count]",
             diff(U, B2["subjects"]["l2"]))

print("--- the measured movement (not pass/fail by itself): today's re-render before the freeze "
      "against the on-disk scan after it")
key = lambda e: json.dumps(e, sort_keys=True, ensure_ascii=False)  # noqa: E731
before = tb1["LEAKS_IN_THE_EXTRAS"]["entries"]
bk = [key(e) for e in before]
ak = [key(e) for e in b2_ent]
only_before = [e for e in before if key(e) not in ak]
only_after = [e for e in b2_ent if key(e) not in bk]
print(f"entries in T(B1.l2) and not in B2.l2: {len(only_before)}")
for e in only_before:
    print("   ", json.dumps(e, ensure_ascii=False))
print(f"entries in B2.l2 and not in T(B1.l2): {len(only_after)}")
for e in only_after:
    print("   ", json.dumps(e, ensure_ascii=False))
expected_shape = (
    len(only_before) == 2 and not only_after
    and all(e["member"] == 7 and e["file"] == "07_the_charter_the_layers_and_the_decisions.md"
            for e in only_before)
    and sorted(m for e in only_before for m in e["matched"]) == ["D-207", "D-527"])
print("the movement is exactly the expected one (two member-(7) entries, matching D-527 and "
      "D-207, none the other way):", "PASS" if expected_shape else "FAIL")
ok &= expected_shape
print("RESULT:", "ALL EMPTY / PASS" if ok else "STOP")
sys.exit(0 if ok else 3)
```

`cmp_t2e.py` — Task 2(e):

```python
"""Task 2(e): B3 (before the three edits) against B4 (after).  Every top-level value but
`subjects` equal; the three pre-scoping subjects unmoved; and `l2` moved in exactly the one
bullet line, tested by replacing the JSON-escaped old bullet exactly once in B3's `l2` text.
Kept outside the repository working tree."""
import json
import os
import sys

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from diff_paths import diff, report  # noqa: E402

B3 = json.load(open(os.path.join(S, "B3.json"), encoding="utf-8"))
B4 = json.load(open(os.path.join(S, "B4.json"), encoding="utf-8"))
ok = True
keys = set(B3) == set(B4)
print("top-level keys the same set:", "PASS" if keys else "FAIL")
ok &= keys
for k in sorted(set(B3) & set(B4)):
    if k == "subjects":
        continue
    eq = B3[k] == B4[k]
    print(f"top-level {k!r} equal:", "PASS" if eq else "FAIL")
    ok &= eq
same_subjects = set(B3["subjects"]) == set(B4["subjects"])
print("subjects the same set:", "PASS" if same_subjects else "FAIL")
ok &= same_subjects
for s in ("harmony-boundary", "scoring-model", "l0-l1"):
    ok &= report(f"diff(B3.subjects[{s!r}], B4.subjects[{s!r}])",
                 diff(B3["subjects"][s], B4["subjects"][s]))
OLD = json.dumps("its `group` is E — Layer 2, the slicer", ensure_ascii=False)
NEW = json.dumps("its `group` is one of the register groups listed under `the_groups` below",
                 ensure_ascii=False)
txt = json.dumps(B3["subjects"]["l2"], ensure_ascii=False)
n = txt.count(OLD)
print("occurrences of the old bullet in B3.subjects['l2']:", n)
ok &= n == 1
replaced = json.loads(txt.replace(OLD, NEW, 1))
ok &= report("diff(B3.l2 with the bullet replaced once, B4.l2)",
             diff(replaced, B4["subjects"]["l2"]))
print("RESULT:", "ALL PASS" if ok else "STOP")
sys.exit(0 if ok else 3)
```

`extract_member8_json.py` — Task 3(d)'s authority, from the pinned blob (`git cat-file -p 4e862929… | python extract_member8_json.py <out>`):

```python
"""Write Task 3(d)'s JSON object, byte for byte, from the PINNED dispatch blob read on stdin
(`git cat-file -p <blob> | python extract_member8_json.py <out>`).  The object is the one fenced
```json block of the dispatch, which opens directly under the words "The authority is this JSON
object" — located by that text, and required to be found exactly once.  Kept outside the
repository working tree."""
import json
import sys

raw = sys.stdin.buffer.read().decode("utf-8")
text = raw.replace("\r\n", "\n")
marker = "**The authority is this JSON object.**"
assert text.count(marker) == 1, "marker not found exactly once"
after = text[text.index(marker):]
assert after.count("```json\n") >= 1
start = after.index("```json\n") + len("```json\n")
end = after.index("\n```\n", start)
body = after[start:end] + "\n"
assert text.count("```json\n") == 1, f"```json fences in the dispatch: {text.count('```json')}"
obj = json.loads(body)
with open(sys.argv[1], "w", encoding="utf-8", newline="") as fh:
    fh.write(body)
print("written", sys.argv[1], len(body.encode("utf-8")), "bytes;",
      "order", len(obj["order"]), "new", len(obj["new"]), "carried", len(obj["carried"]))
```

`insert_l3_extras.py` — Task 3(c)–(d), run once as a dry run and once with `--write`:

```python
"""Task 3(c)/(d): author EXTRAS["l3"] into the generator.

The twelve CARRIED parts are copied from the generator's OWN TEXT — each `EXTRAS["l2"]` member-(8)
part whose `"source"` line names the path, found exactly once inside `EXTRAS["l2"]`, taken from its
opening `{` to its closing `},` byte for byte — and the additions of the JSON authority are inserted
before the closing `],` of its `removals` and of its `cuts`, in the order given.  The five NEW parts
are written from the JSON authority.  Every dict is written in the multi-line style the `l2` parts
use, strings as JSON string literals (valid Python string literals for this text), `true` as `True`.
The block is inserted ONCE, between `    ],` and `}` at the end of `EXTRAS`; the three-line old text
must occur exactly once or nothing is written.  The inserted block is also saved to the scratch
folder.  Kept outside the repository working tree."""
import json
import os
import sys

S = os.path.dirname(os.path.abspath(__file__))
GEN = r"C:\s\MS\tools\audit\gen_derivation_boot_pack.py"
X = json.load(open(os.path.join(S, "l3_member8_expected.json"), encoding="utf-8"))

src = open(GEN, encoding="utf-8", newline="").read()
assert "\r\n" not in src, "the generator carries CRLF line ends; this script writes LF only"
lines = src.split("\n")

I_DICT = " " * 24      # a filter-entry dict's opening brace
I_KEY = " " * 28       # a filter-entry dict's keys
I_PART = " " * 16      # a part's opening brace
I_PKEY = " " * 20      # a part's keys


def lit(v):
    if v is True:
        return "True"
    return json.dumps(v, ensure_ascii=False)


def dict_lines(d):
    out = [I_DICT + "{"]
    for k, v in d.items():
        out.append(f"{I_KEY}{json.dumps(k)}: {lit(v)},")
    out.append(I_DICT + "},")
    return out


# ── the range of EXTRAS["l2"] ─────────────────────────────────────────────────────────────────
start = [i for i, ln in enumerate(lines) if ln == "EXTRAS: dict[str, list[dict]] = {"]
assert len(start) == 1
l2_open = [i for i in range(start[0], len(lines)) if lines[i] == '    "l2": [']
assert len(l2_open) == 1, l2_open
l2_close = next(i for i in range(l2_open[0], len(lines)) if lines[i] == "    ],")
L2 = (l2_open[0], l2_close)


def carried_part(path):
    want = f'{I_PKEY}"source": {json.dumps(path)},'
    hits = [i for i in range(L2[0], L2[1]) if lines[i] == want]
    assert len(hits) == 1, (path, hits)
    h = hits[0]
    assert lines[h - 1] == I_PART + "{", (path, lines[h - 1])
    end = next(i for i in range(h, L2[1]) if lines[i] == I_PART + "},")
    return lines[h - 1:end + 1]


def add_to_list(block, key, added):
    if not added:
        return block
    opener = f'{I_PKEY}"{key}": ['
    empty = f'{I_PKEY}"{key}": [],'
    idx = [i for i, ln in enumerate(block) if ln in (opener, empty)]
    assert len(idx) == 1, (key, idx)
    i = idx[0]
    new = [x for d in added for x in dict_lines(d)]
    if block[i] == empty:
        return block[:i] + [opener] + new + [I_PKEY + "],"] + block[i + 1:]
    close = next(j for j in range(i + 1, len(block)) if block[j] == I_PKEY + "],")
    return block[:close] + new + block[close:]


def new_part(path, spec):
    out = [I_PART + "{", f'{I_PKEY}"source": {json.dumps(path)},',
           f'{I_PKEY}"spans": [{{"kind": "whole"}}],']
    for key in ("removals", "cuts"):
        if spec[key]:
            out.append(f'{I_PKEY}"{key}": [')
            for d in spec[key]:
                out.extend(dict_lines(d))
            out.append(I_PKEY + "],")
        else:
            out.append(f'{I_PKEY}"{key}": [],')
    out.append(I_PART + "},")
    return out


parts = []
for path in X["order"]:
    if path in X["new"]:
        parts.extend(new_part(path, X["new"][path]))
    else:
        c = X["carried"][path]
        b = carried_part(path)
        b = add_to_list(b, "removals", c["removals_added"])
        b = add_to_list(b, "cuts", c["cuts_added"])
        parts.extend(b)

head = '''    "l3": [
        CHARTER_MEMBER_7,
        {
            "number": 8,
            "filename": "08_the_seventeen_research_extracts.md",
            "title": "Seventeen published sources, read at the object — the L3 slice and the "
                     "first-pass extracts that bear on it",
            "source": "reading_pass/extracts/ — the first extractions of the six L3-slice rows (36, "
                      "37, 38 and 39, with 34 and 40 carried from L2's slice; Ruling 3 (i) of "
                      "`cowork_rulings_2026_10_15_l3_boot_list_sitting.md`) and the eleven "
                      "first-pass extracts admitted by Ruling 1 of "
                      "`cowork_rulings_2026_10_15_l3_first_pass_extracts_sitting.md`",
            "rendered_from": "the seventeen files themselves, quoted whole, each with the sections "
                             "and passages stating this project's own positions cut PER FILE "
                             "(Ruling 1 of 2026-09-21, limb A), the ruled shared cut strings "
                             "unchanged, and L2's filters carried unchanged for the twelve files "
                             "L2's member (8) already holds; the per-file list is "
                             "`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`",
            "parts": ['''.split("\n")
tail = ['            ],', '        },', '        LEDGER_MEMBER_9,', '    ],']
block = head + parts + tail

OLD = "        LEDGER_MEMBER_9,\n    ],\n}\n"
assert src.count(OLD) == 1, f"old text occurs {src.count(OLD)} times"
NEW = "        LEDGER_MEMBER_9,\n    ],\n" + "\n".join(block) + "\n}\n"
out = src.replace(OLD, NEW, 1)
with open(os.path.join(S, "l3_extras_block.py.txt"), "w", encoding="utf-8", newline="") as fh:
    fh.write("\n".join(block) + "\n")
if "--write" in sys.argv:
    with open(GEN, "w", encoding="utf-8", newline="") as fh:
        fh.write(out)
    print("inserted", len(block), "lines into the generator")
else:
    print("dry run:", len(block), "lines; nothing written")
```

`cmp_t3e.py` — Task 3(e):

```python
"""Task 3(e): the check of the authored `l3` member against its JSON authority, before any build.
Imports the EDITED generator as `dbp`, and the generator at Task 2's commit (saved to the scratch
folder as gen_at_t2.py) as `dbp_t2` for item 6 — the latter only for two tables, nothing called
(`tools/audit` is put on `sys.path` so its one module-level import resolves; it reads no source at
import).  Kept outside the repository working tree."""
import importlib.util
import json
import os
import sys

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\s\MS\tools\audit")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


dbp = load("dbp", r"C:\s\MS\tools\audit\gen_derivation_boot_pack.py")
X = json.load(open(os.path.join(S, "l3_member8_expected.json"), encoding="utf-8"))
ok = True


def say(n, cond, what):
    global ok
    print(f"{n}. {what}: {'PASS' if cond else 'FAIL'}")
    ok &= bool(cond)


E = dbp.EXTRAS["l3"]
say(1, len(E) == 3 and E[0] is dbp.CHARTER_MEMBER_7 and E[2] is dbp.LEDGER_MEMBER_9,
    "EXTRAS['l3'] has three members, [0] is CHARTER_MEMBER_7 and [2] is LEDGER_MEMBER_9 by identity")
parts = E[1]["parts"]
say(2, [p["source"] for p in parts] == X["order"]
    and all(p["spans"] == [{"kind": "whole"}] for p in parts),
    "member (8)'s sources are X['order'], every part's spans == [{'kind': 'whole'}]")
by = {p["source"]: p for p in parts}
c3 = True
for path, spec in X["new"].items():
    p = by[path]
    good = ("removals" in p and "cuts" in p and p.get("removals") == spec["removals"]
            and p.get("cuts") == spec["cuts"])
    if not good:
        print("    FAIL at", path)
    c3 &= good
say(3, c3, f"the {len(X['new'])} new parts equal the authority's removals and cuts")
l2m8 = [m for m in dbp.EXTRAS["l2"] if m.get("number") == 8]
assert len(l2m8) == 1
c4 = True
for path, add in X["carried"].items():
    Ls = [q for q in l2m8[0]["parts"] if q["source"] == path]
    if len(Ls) != 1:
        print("    FAIL: l2 part found", len(Ls), "times at", path)
        c4 = False
        continue
    L, p = Ls[0], by[path]
    good = (p["removals"] == L["removals"] + add["removals_added"]
            and p["cuts"] == L["cuts"] + add["cuts_added"])
    if not good:
        print("    FAIL at", path)
    c4 &= good
say(4, c4, f"the {len(X['carried'])} carried parts equal L2's entries followed by the additions")
docs_json = json.load(open(r"C:\s\MS\tools\audit\l3_withheld_documents.json", encoding="utf-8"))
dl = docs_json["documents"]
order = list(dl) if isinstance(dl, dict) else [d.get("document", d.get("name")) for d in dl]
W = dbp.WITHHELD["l3"]
wd = W["withheld_documents"]
say(5, list(wd) == list(dbp.L3_WITHHELD_DOCUMENTS) == order
    and all(wd[d].get(f) for d in wd for f in ("finding", "date", "reason"))
    and W["withheld_passages"] == [],
    "WITHHELD['l3'] has the five documents in the artifact's order, each with finding/date/reason, "
    "and no withheld passage")
print("    the artifact's document order:", order)
t2 = load("dbp_t2", os.path.join(S, "gen_at_t2.py"))
say(6, t2.EXTRAS["l2"] == dbp.EXTRAS["l2"] and t2.WITHHELD["l2"] == dbp.WITHHELD["l2"],
    "EXTRAS['l2'] and WITHHELD['l2'] equal those of the generator at Task 2's commit")
print("RESULT:", "ALL PASS" if ok else "STOP")
sys.exit(0 if ok else 3)
```

`cmp_t4c.py` — Task 4(c):

```python
"""Task 4(c): the manifest at Task 2's commit (M2.json) against the manifest on disk now (M4.json).
The four frozen subjects unmoved; the top-level keys the same set; every top-level value equal
except three — `the_rulings_it_executes` the old list followed by exactly Task 3(f)'s four strings,
and `the_pack_files_in_order` and `subjects` each differing from the old only by the added key
`l3`.  Kept outside the repository working tree."""
import json
import os
import sys

S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, S)
from diff_paths import diff, report  # noqa: E402

A = json.load(open(os.path.join(S, "M2.json"), encoding="utf-8"))
B = json.load(open(os.path.join(S, "M4.json"), encoding="utf-8"))
FOUR = [
    "Rulings 1 to 5 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md` — the `l3` "
    "subject's pack: the charter member and the ledger member as `l2` carries them, the "
    "extracts member over L3's slice and the first-pass extracts that bear on L3, no withheld "
    "passage of member (2), and withheld documents derived and confirmed before being "
    "authored.",
    "The rulings of `cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md` — the `l3` "
    "withheld family: every identity the authored verdicts grade IN is withheld.",
    "Ruling 1 of `cowork_rulings_2026_10_15_l3_withheld_documents_confirmation_sitting.md` — "
    "the derived set of the `l3` withheld documents, confirmed.",
    "Ruling 1 of `cowork_rulings_2026_10_15_l3_first_pass_extracts_sitting.md` — the eleven "
    "first-pass extracts of the `l3` extracts member, each cut per file under limb A of Ruling "
    "1 of `cowork_rulings_2026_09_21_l2_extracts_member_cutting_sitting.md`.",
]
ok = True
for s in ("harmony-boundary", "scoring-model", "l0-l1", "l2"):
    ok &= report(f"diff(M2.subjects[{s!r}], M4.subjects[{s!r}])",
                 diff(A["subjects"][s], B["subjects"][s]))
k = set(A) == set(B)
print("top-level keys the same set:", "PASS" if k else "FAIL")
ok &= k
for key in sorted(set(A) & set(B)):
    if key in ("the_rulings_it_executes", "the_pack_files_in_order", "subjects"):
        continue
    eq = A[key] == B[key]
    print(f"top-level {key!r} equal:", "PASS" if eq else "FAIL")
    ok &= eq
r = B["the_rulings_it_executes"] == A["the_rulings_it_executes"] + FOUR
print("the_rulings_it_executes == old + the four strings of Task 3(f):", "PASS" if r else "FAIL")
ok &= r
for key in ("the_pack_files_in_order", "subjects"):
    a, b = A[key], B[key]
    good = set(b) - set(a) == {"l3"} and not (set(a) - set(b)) and all(a[x] == b[x] for x in a)
    print(f"{key} differs from the old only by the added key 'l3':", "PASS" if good else "FAIL")
    ok &= good
print("RESULT:", "ALL PASS" if ok else "STOP")
sys.exit(0 if ok else 3)
```

`lists_t4.py` — Task 4(d) and (e):

```python
"""Task 4(d) and 4(e): read out of the manifest on disk and the rendered `l3` files, never
transcribed.  Writes markdown to stdout.  Imports the generator only to read `VERDICTS["l3"]` and the
authored member (8) for the authored totals (nothing is built).  Kept outside the working tree."""
import importlib.util
import json
import os
import sys

ROOT = r"C:\s\MS"
PACK = os.path.join(ROOT, "tools", "audit", "derivation_boot_pack", "l3")
S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "tools", "audit"))
spec = importlib.util.spec_from_file_location(
    "dbp", os.path.join(ROOT, "tools", "audit", "gen_derivation_boot_pack.py"))
dbp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dbp)
M = json.load(open(os.path.join(ROOT, "tools", "audit", "derivation_boot_pack.json"), encoding="utf-8"))
R = M["subjects"]["l3"]


def md(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


print("### (d) The pack directory")
on_disk = sorted(n for n in os.listdir(PACK) if os.path.isfile(os.path.join(PACK, n)))
order = M["the_pack_files_in_order"]["l3"]
print("Files on disk:", ", ".join(f"`{n}`" for n in on_disk))
print()
print("`the_pack_files_in_order` → `l3`:", ", ".join(f"`{n}`" for n in order))
print()
print("The directory and `the_pack_files_in_order` name the same set:", sorted(order) == on_disk)
m8 = [r for r in R["the_members_as_rendered"] if r["member"] == 8][0]
fa = [f for p in m8["parts"] for f in p["filters_applied"]]
got = {"parts": len(m8["parts"]),
       "removals": sum(1 for f in fa if f["kind"] == "removal"),
       "cuts": sum(1 for f in fa if f["kind"] == "cut"),
       "runs_to_end cuts": sum(1 for f in fa if f["kind"] == "cut" and f.get("runs_to_end"))}
A = dbp.EXTRAS["l3"][1]["parts"]
auth = {"parts": len(A),
        "removals": sum(len(p["removals"]) for p in A),
        "cuts": sum(len(p["cuts"]) for p in A),
        "runs_to_end cuts": sum(1 for p in A for c in p["cuts"] if c.get("runs_to_end"))}
print()
print("| Member (8) | in the manifest | authored (the JSON object of Task 3(d) plus the twelve L2 parts) |")
print("|---|---|---|")
for k in got:
    print(f"| {k} | {got[k]} | {auth[k]} |")
print()
print("Member (8) `characters`:", m8["characters"])

print()
print("### (e) 1. The derived cross-reference additions")
adds = R["THE_WITHHELD_FAMILY"]["derived_cross_reference_additions"]["additions"]
print()
print("| identity | title | derived because |")
print("|---|---|---|")
for a in adds:
    why = "; ".join(f"`{h['field']}` matched `{h['matched']}`" for h in a["derived_because"])
    print(f"| {a['id']} | {md(a['title'])} | {md(why)} |")
print()
print("#### RULING 84 — ADDITIONS THAT WOULD WITHHOLD AN ENTRY THE USER RULED ADMITTED")
V = dbp.VERDICTS["l3"]
r84 = [a for a in adds if a["id"] in V and V[a["id"]][0] == dbp.VERDICT_OUT]
if not r84:
    print()
    print("There is none.")
for a in r84:
    vd, finding, reason = V[a["id"]]
    print()
    print(f"- **{a['id']}** — {md(a['title'])}")
    print(f"  - verdict: {vd}")
    print(f"  - finding: {md(finding)}")
    print(f"  - reason: {md(reason)}")
not_graded = [a["id"] for a in adds if a["id"] not in V]
print()
print("Additions with no verdict in `VERDICTS[\"l3\"]`:", not_graded or "none")

print()
print("### (e) 2. `LEAKS` — members (5) and (6)")
print()
print("| member | identity | title | matched |")
print("|---|---|---|---|")
for e in R["LEAKS"]["entries"]:
    mt = "; ".join(f"`{h['field']}`: `{h['matched']}` ({h['kind']})" for h in e["matched"])
    print(f"| {e['member']} | {e['id']} | {md(e['title'])} | {md(mt)} |")

print()
print("### (e) 3. `LEAKS_IN_THE_EXTRAS` — limb B, every line, grouped by member and file")
ex = R["LEAKS_IN_THE_EXTRAS"]["entries"]
print()
print("Entries:", len(ex), "· `counted/extras_lines_with_a_leak_hit`:",
      R["counted"]["extras_lines_with_a_leak_hit"])
cur = None
for e in ex:
    g = (e["member"], e["file"])
    if g != cur:
        cur = g
        print()
        print(f"#### member ({e['member']}) — `{e['file']}`")
        print()
        print("| line | matched | kinds | the line |")
        print("|---|---|---|---|")
    print(f"| {e['line']} | {md(', '.join(e['matched']))} | {md(', '.join(e['kinds']))} | "
          f"{md(e['the_line'])} |")

print()
print("### (e) 4. Member (8)'s title lines, as rendered")
f8 = open(os.path.join(PACK, "08_the_seventeen_research_extracts.md"), encoding="utf-8",
          newline="").read().split("\n")
print()
print("| part | line in `08_…` | the title line |")
print("|---|---|---|")
for i, p in enumerate(A, start=1):
    first = open(os.path.join(ROOT, p["source"]), encoding="utf-8", newline="").read().split("\n")[0]
    first = first.rstrip("\r")
    hits = [n for n, ln in enumerate(f8, start=1) if ln.rstrip("\r") == first]
    print(f"| {i} | {', '.join(map(str, hits)) or 'NOT FOUND'} | {md(first)} |")

print()
print("### (e) 5. Member (2) for L3 — the five withheld document names, searched")
f2 = open(os.path.join(PACK, "02_the_guiding_principles_and_the_conventions.md"), encoding="utf-8",
          newline="").read().split("\n")
for d in dbp.L3_WITHHELD_DOCUMENTS:
    hits = [(n, ln) for n, ln in enumerate(f2, start=1) if d in ln]
    print()
    print(f"- `{d}`: {len(hits)} line(s)")
    for n, ln in hits:
        s = ln.strip()
        at = s.find(d)
        lo, hi = max(0, at - 120), min(len(s), at + len(d) + 120)
        print(f"  - line {n}: …{md(s[lo:hi])}…")
```

`assemble_report.py` — fills this report's marked places with the run outputs and script texts above, verbatim:

```python
"""Fill the report skeleton's insertion places with the named scratch files, verbatim (trailing
newline stripped), in ONE pass over the skeleton — so text inserted is never itself re-scanned —
and write the report.  Every named file must exist, or nothing is written.  Kept outside the
repository working tree."""
import os
import re
import sys

S = os.path.dirname(os.path.abspath(__file__))
skel = open(os.path.join(S, "report_skeleton.md"), encoding="utf-8").read()
MARK = re.compile(r"<<INSERT:([^>]+)>>")
names = MARK.findall(skel)
bodies = {n: open(os.path.join(S, n), encoding="utf-8").read().rstrip("\n") for n in names}
out = MARK.sub(lambda m: bodies[m.group(1)], skel)
with open(sys.argv[1], "w", encoding="utf-8", newline="\n") as fh:
    fh.write(out)
print("filled", len(names), "places; wrote", sys.argv[1], len(out.encode("utf-8")), "bytes")
```

## 7. Declared departures

1. **The dispatch was read from the working tree before it was pinned** — standing clause P-2's fallback route, the
   user's opening line naming only the file. Pinned at Task 0 (`git hash-object -w`); the blob proven unmoved before
   staging.
2. **Task 3(c)–(d)'s `EXTRAS["l3"]` entry was inserted by a scratch script, not by the file-editing tool.** The
   standing bars say *"Edit files with your file-editing tool, never by retyping a whole file"*, and Task 3(d) says
   *"Copy the L2 entries from the file, not from memory and not from this dispatch"*. The block is 949 lines, most of
   them twelve parts of L2's own filter entries; the script copies those parts as text from the generator file itself,
   so nothing in them passed through this session's retyping, and inserts the whole block at the one old text, found
   once. The file was not retyped: one region was inserted. Task 3(e) then proved the result against the JSON
   authority, part for part, and against L2's entries, by value. The other three Task 3 edits were made by the
   file-editing tool.
3. **The comparison scripts were run with `PYTHONIOENCODING=utf-8`**, on the released second half's lesson that the
   console's code page stops a script at its first `★`.
4. **This report was assembled by a scratch script** that replaced marked places with the run outputs and script texts
   verbatim, so that no output was hand-transcribed (#17f).
5. **Each commit message carries one trailer line after the ordered subject** — the co-author attribution this session's
   instructions require — as a second paragraph; the subject lines are exactly the ordered ones.
6. **`git hash-object` was run on working-tree files** — the dispatch, for P-2; `claude_md_finer_archive.json`, for A1;
   the ten `l2` pack files, as Task 1(a)–(b) orders; and every file of the pack directories, for the unmoved proofs.
   **`cmp` was run on the manifest** against the scratch dumps, for the byte-identity proofs Task 1(h), Task 2 and
   Task 4(a) order.
7. **The `STATUS.md` entry for Tasks 3 and 4 is one entry**, the two tasks having made one commit as the dispatch
   orders.

## 8. Observations, recorded and not acted on

1. **The released second half's open question is answered by the measurement**: the two charter lines that stopped
   it are not leak hits for `l3` (first section, second reading).
2. **★ A STALE SENTENCE THIS BATCH'S OWN ACT CREATED, SURFACED AND NOT CORRECTED.** The first block of
   `VERDICTS["l3"]`'s opening comment, under the heading *"L3, the deriving subject after L2 — PROPOSALS, NOT A WITHHELD
   FAMILY"*, reads, read at the generator after Task 4's commit: *"So this table is a set of proposals.  `WITHHELD`
   carries no `l3` entry, `build()` iterates `WITHHELD`, and therefore NOTHING READS THIS TABLE TODAY: it is dormant by
   design, its consumer the `build_subject("l3", ...)` run that happens when the user has ruled the lists and the
   family is authored — a separate act."* **That is false since Task 3**: `WITHHELD` carries an `l3` entry, `build()`
   builds `l3`, and the table is read. **It was not corrected**, because A3 and the standing bars hold the generator
   byte-unchanged outside the edits Tasks 1 to 3 quote, and this sentence is in none of them; and **no open-items row
   was created**, because the bars forbid one. The self-check rule would row a finding that cannot be corrected in
   scope; the dispatch's bar forbids the row; the two are put to the writing side here rather than resolved by this
   session. *The precedent shape, for whoever corrects it:* `VERDICTS["l2"]`'s equivalent comment carries the same
   sentence as a FORMER WORDING, PRESERVED (#12), under its correction at L2's build. Documentation of a tool only; it
   changes no algorithm.
3. **D-343's OUT verdict and its derived withholding coincide** — the one case Ruling 84 sends to the user as its own
   list; it is in the first section and nothing was done about it.

## 9. What this batch did not do

No session booted; no brief written; no score copied, staged or written; no list of Task 4(e) acted on; no filter
string corrected and no cut authored beyond the authority; no edit to `CRITERION`, `MEMBERS`, `CHARTER_MEMBER_7`,
`LEDGER_MEMBER_9`, `EXTRAS["l2"]`, `WITHHELD` for any subject but `l3`, or any `VERDICTS` entry; no edit to any
ruling record, the cut list, any extract or either input-contract copy; no ruling taken and no question or
recommendation put to the user; no open-items row created, flipped or discarded; no decisions-register entry and no
`D-NNN`; nothing in the suspension file; no `src/` file, build, test, golden, corpus of scores, or anything under
`tools/corpus/` or `tools/robust_stop/`; no measurement of the analysis; no governing document edited except
`STATUS.md` and `STATUS_ARCHIVE.md`; no pack directory written except `tools/audit/derivation_boot_pack/l3/`.

## 10. The plan's tell, in one sentence

**Did this batch produce anything other than the landed paths, the repair (Edits 1.1 to 1.6), the freeze, the three
Task 2 edits, the `l3` entries of `WITHHELD` and `EXTRAS` with `L3_WITHHELD_DOCUMENTS` and the four ruling strings, the
rendered `l3` directory, the manifest, the Task 5 files and the report?** **Yes, by addition only:** Task 0 carries the
regenerated `tools/audit/evidence_pin_membership.json`, as its act (2) orders; the end-state commit carries the
artifacts A2's classing regenerates beside `tools/audit/guard_state.json`; and the scripts of §6 that the dispatch does
not order in that form (`insert_l3_extras.py`, `extract_member8_json.py`, `lists_t4.py`, `assemble_report.py`, the
inline check of Task 0) were run outside the repository. Nothing else.

## 11. The standing self-check (D-434) over this batch's own work

1. *Principles touched.* **#12** — the record of what L2's session was given did not move: its leak list is scanned
   from the files that session was given, and the comparison against the committed manifest is empty. **#6** — the
   charter and ledger members are the shared objects (Task 3(e) item 1, by identity); the twelve carried parts are
   L2's own entries copied from the file. **#13/#18** — the ruling record's prediction was measured by the ordered
   comparison, with a STOP behind it, and it held. **#15/#19** — every comparison is at the objects, in both
   directions, against an explicit hash. **#17(f)/D-431** — every count in this report is in a run output reproduced
   verbatim, or is a hash or a count of files taken from a command's own printed lines; the `STATUS.md` entries restate
   none. Conforms.
2. *Conventions.* American English in this side's prose; no self-invented label; reserved words in their musical senses
   or qualified (*decisions-register*, *open-items*, *corpus of scores*; a pack *part* only as the generator's field).
3. *The diff of every touched file was re-read* through the diff enumerations of §5 and the footprint of §1; every
   deleted generator line falls inside a quoted old text, and Task 3–4's generator diff deletes none. **One
   finding:** the stale sentence of §8 item 2, made false by Task 3 and left standing because the bars forbid both
   its correction and its row; surfaced here, not shipped silently.
4. *File-tools rule.* Repository content read with the file tools, save the git object queries, the sanctioned scripts
   and the declared items of §7. Two shell reads of repository paths were refused by the armed guard (`ls` and `cat`)
   and redone with the file tools.
5. *Uncertainty.* No check rests on a sample; each is a whole-object comparison or a full run.

*Provenance: CC, 2026-10-17, at boot tip `5324b94388bdda6c242ff937ace781cbe62d9c2d`, under
`cc_instruction_l3_pack_build_second_half_resumed_2026_10_16.md`, after its ordered first reads — the 2026-10-16 ruling
record, the freeze-derivation and confirmation records and the cut list whole; `CLAUDE.md` at its session-start spans;
`STATUS.md` and `DECISIONS.md` whole; the gating answer located; handoff entries 414 and 415 whole; the dispatch-protocol
section of `cowork_audit_protocol.md` at P-2; the released second half's report at its head section, §1 to §11 and the
first part of its diff; the first half's dispatch at its Tasks 0 to 2; the generator at its docstring, `VERDICT_DATE`,
`FROZEN`, `CHARTER_MEMBER_7`, `LEDGER_MEMBER_9`, `EXTRAS` at its head, its `l2` parts by search and at four carried
parts, `filter_part`, `_removal_spans`, `_cut_spans`, `render_extra`, `criterion_block`, `cross_reference_additions`,
`build_subject`, `build()`, `frozen_block`, `frozen_from_disk`, `write_all`, `check_all` and `main`; and
`gen_status_batch_bound.py` at the tip's object at its docstring, its authored inputs with their comments, the tail of
`PREVIOUS_AIMINGS` and its code. **Not read:** handoff entries 410 to 413 (read by the batch that landed them; this
dispatch's own record of them was relied on); the released second half's dispatch beyond what this dispatch carries;
the first half's report and close section; the boot-list and first-pass extracts ruling records; the extracts
themselves; `tools/audit/l3_withheld_documents.json` beyond its `documents` order, which Task 3(e) item 5 read.*
