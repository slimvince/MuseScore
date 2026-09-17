# The sitting's landing — report (CC, 2026-09-01)

**Dispatch:** `cc_instruction_sitting_landing_2026_09_01.md`.
**Outcome:** one commit exists, `e02d982c158d1899da67c5acf1d73478edc6df0b`, carrying exactly the
paths §2 names that Task 1 found. The deliberate exclusion held. Nothing was pushed, amended,
squashed, rebased or tagged. **No file's content was changed by this batch.**

**★ §0's FLAGGED CLAIM IS ANSWERED, AND IT WAS FALSE.** The writing side told the user the ruling
record *"has never landed in git."* **It is tracked, and an earlier state of it is in HEAD's tree.**
What had not landed is the sitting's additions to it. The establishment is at the git objects, §1
below.

---

## 0. Boot — what was read, and the one conditional read whose condition was not met

Performed before any other act, and not treated as waived by the opening instruction naming one file
(the ratified 2026-08-29 rule, P-1).

- `CLAUDE.md` — whole.
- `DECISIONS.md` — whole (the INDEX, all groups A…U and the provenance block).
- `STATUS.md` — whole.
- The derived gating answer — `tools/audit/nongating_apparatus_rows.json` →
  `★_the_live_gating_answer`, read at the artifact. No stage is opened by this batch, so no gating
  identity is consumed by any act below.
- `cowork_rulings_2026_08_31_decision_surface_sitting.md` — whole (the principal object landed).
- `cc_instruction_sitting_landing_2026_09_01.md` — whole.
- The branch and commit rules: `CLAUDE.md` Conventions, and the dispatch protocol
  (`cowork_audit_protocol.md`) at the clauses that bear on committing — including the
  interim-carrier clause that is this landing's own authority.

**`BUILD_AND_TEST.md` — NOT read, condition not met, and the condition was CHECKED rather than
assumed.** Its condition is a session that builds, tests, or runs a measurement tool *whose command
lives there*. This batch built nothing and tested nothing. It did run one Python tool —
`tools/audit/changed_paths.py`, the substitute the standing shell-read guard itself names — and
`BUILD_AND_TEST.md` was searched for that tool: **no occurrence.** Its command does not live there,
so the condition stays unmet.

### Task 0 — the pins

Every file §0 names, pinned with `git hash-object -w` before it was relied on. **No read disagreed
with its pin.**

| file | blob |
|---|---|
| `CLAUDE.md` | `e012d3f2adc10e4557bf422236f0d50014559568` |
| `DECISIONS.md` | `238cff78e61d4ff4cd8e5a41dc17f6fab4ab7d59` |
| `STATUS.md` | `a9163ead8ade542c67cde43bf611e30477e0459b` |
| `BUILD_AND_TEST.md` | `42df316140c8bf178b620b461b84fadacb976299` |
| `tools/audit/nongating_apparatus_rows.json` | `a2ca9f64783d45a50bd3fb299d46afe46b9fe678` |
| `cowork_rulings_2026_08_31_decision_surface_sitting.md` | `78b4154e86bfc6d971de50042cd7be53332748fc` |
| `cc_instruction_sitting_landing_2026_09_01.md` | `da3239fbe9bacaedc1643ec2dda380108fabf099` |

---

## 1. Task 1 — the true state, established before anything rested on it

### 1.1 The shell-read guard refused, and the substitute it names was used

`git status --porcelain` was **refused by the standing guard**, which named its own substitute:

> `git status` is not trusted for what is current — `CLAUDE.md` Conventions, register entry D-253.
> The sanctioned way to enumerate which paths changed is `python tools/audit/changed_paths.py`
> (`--staged`, or `--commit <hash>`), which reports paths and status codes and cannot return file
> content.

That substitute produced every enumeration in this report. **Saying so is the dispatch's own
instruction**, and three preceding batches met the same refusal.

### 1.2 The full changed-path enumeration at Task 1 — reported whole

`python tools/audit/changed_paths.py`, run before any staging act. **874 records: 4
tracked-and-modified (` M `), 870 untracked (`??`).** An untracked *directory* record stands for
everything beneath it — that is the tool's own reporting shape, and it matters for the arithmetic in
§4.3.

```
 M	FRAMEWORK.md
 M	cowork_rulings_2026_08_31_decision_surface_sitting.md
 M	tools/audit/derivation_boot_pack.json
 M	tools/audit/gen_derivation_boot_pack.py
??	cc_L6_corpus_oracle_report.md
??	cc_absent_root_investigation.md
??	cc_anchor_design_dossier.md
??	cc_anchor_recompute_report.md
??	cc_anchor_redesign_dossier.md
??	cc_approval_styletag_swap_commit.md
??	cc_architecture_opinion.md
??	cc_artifact_inventory_report.md
??	cc_audit_cadencekeyanchor_report.md
??	cc_audit_chordanalyzer_oracle_report.md
??	cc_audit_harmonicfunctionlayer_report.md
??	cc_audit_jointkeydecision_report.md
??	cc_audit_keymodeanalyzer_report.md
??	cc_audit_localmodulationdetector_report.md
??	cc_b2_subdominant_guard_report.md
??	cc_b_guard_scoping_dossier.md
??	cc_backfill_engravingbridge_report.md
??	cc_backfill_formatter_report.md
??	cc_backfill_l3_keymode_report.md
??	cc_backfill_l4_oracle_report.md
??	cc_baseline_reconciliation_report.md
??	cc_batch_analyze_restore_report.md
??	cc_batch_analyze_unification_report.md
??	cc_bridge_lookahead_report.md
??	cc_bwv301_diagnostic_report.md
??	cc_clang_branch_coverage_report.md
??	cc_consumer_build_report.md
??	cc_corpus_hygiene_report.md
??	cc_corpus_hygiene_report_corelli.md
??	cc_corpus_wave1_report.md
??	cc_deltaseven_7a_diagnostic_report.md
??	cc_deltaseven_phase_e_diagnostic_report.md
??	cc_deltaseven_predecessor_report.md
??	cc_doc_recovery_report.md
??	cc_doctruth_gate_sync_report.md
??	cc_e0doubleprime_report.md
??	cc_e0prime_report.md
??	cc_e3_investigation_report.md
??	cc_engage_u1_uncap_report.md
??	cc_exemplar_decode_report_2026_09_01.md
??	cc_extension_build_report.md
??	cc_foundations_verification_report.md
??	cc_framework_9_0_correction_report.md
??	cc_gate_r_report.md
??	cc_gate_r_verify_report.md
??	cc_instruction_L5_close_commit.md
??	cc_instruction_L6_corpus_oracle_check.md
??	cc_instruction_a8_metric_rebaseline_measure.md
??	cc_instruction_absent_root_guard.md
??	cc_instruction_absent_root_investigate.md
??	cc_instruction_adoption_commit.md
??	cc_instruction_anchor_design_investigation.md
??	cc_instruction_anchor_recompute_impl.md
??	cc_instruction_anchor_redesign_investigation.md
??	cc_instruction_architecture_opinion.md
??	cc_instruction_audit_cadencekeyanchor.md
??	cc_instruction_audit_chordanalyzer_oracle.md
??	cc_instruction_audit_harmonicfunctionlayer.md
??	cc_instruction_audit_jointkeydecision.md
??	cc_instruction_audit_keymodeanalyzer.md
??	cc_instruction_audit_localmodulationdetector.md
??	cc_instruction_away_batch.md
??	cc_instruction_b2_aug7.md
??	cc_instruction_b2_final.md
??	cc_instruction_b2_guardfix.md
??	cc_instruction_b2_retry.md
??	cc_instruction_b2_subdominant_guard_build.md
??	cc_instruction_b3.md
??	cc_instruction_b_dominant_subdominant_guard_scoping.md
??	cc_instruction_backfill_engravingbridge.md
??	cc_instruction_backfill_formatter.md
??	cc_instruction_backfill_l3_keymode.md
??	cc_instruction_backfill_l4_oracle_gates.md
??	cc_instruction_backup_batch2.md
??	cc_instruction_backup_cowork_docs.md
??	cc_instruction_baseline_reconciliation.md
??	cc_instruction_batch_analyze_restore.md
??	cc_instruction_batch_analyze_unification_audit.md
??	cc_instruction_boot_pack_regeneration.md
??	cc_instruction_bridge_anchor_investigation.md
??	cc_instruction_bridge_lookahead.md
??	cc_instruction_bwv301_diagnostic.md
??	cc_instruction_c1_investigate.md
??	cc_instruction_cadence_key_investigation.md
??	cc_instruction_cadence_precision_investigation.md
??	cc_instruction_carryfix2_resolver_identity.md
??	cc_instruction_carryfix_dl5a_e0prime.md
??	cc_instruction_carryfix_task2_addendum.md
??	cc_instruction_clang_branch_coverage.md
??	cc_instruction_classifier_fix.md
??	cc_instruction_commit_cadence_instrument.md
??	cc_instruction_commit_docs.md
??	cc_instruction_commit_exploration_mode.md
??	cc_instruction_commit_idiom_work.md
??	cc_instruction_commit_reads3.md
??	cc_instruction_consumer_build.md
??	cc_instruction_consumer_build_addendum.md
??	cc_instruction_convert_curated_scores.md
??	cc_instruction_corpus_clone.md
??	cc_instruction_corpus_hygiene.md
??	cc_instruction_corpus_hygiene_corelli.md
??	cc_instruction_corpus_hygiene_record.md
??	cc_instruction_corpus_wave1_dlc_onboarding.md
??	cc_instruction_corpus_wave2_axis2_beds.md
??	cc_instruction_dcml_parser_applied_root_fix.md
??	cc_instruction_decision_enumeration_wave.md
??	cc_instruction_decoder_work_counts.md
??	cc_instruction_deltaseven_7a_diagnostic.md
??	cc_instruction_deltaseven_phase_e_diagnostic.md
??	cc_instruction_deltaseven_predecessor_diagnostic.md
??	cc_instruction_doc_governance_commit.md
??	cc_instruction_doc_pass_caps_and_gates.md
??	cc_instruction_doc_recovery.md
??	cc_instruction_doc_sync_layer1.md
??	cc_instruction_doctruth_gate_sync.md
??	cc_instruction_e0_addendum_carry_cap.md
??	cc_instruction_e0_fullspine_measure.md
??	cc_instruction_e1.md
??	cc_instruction_e2_investigate.md
??	cc_instruction_e2a.md
??	cc_instruction_e2b.md
??	cc_instruction_e2b_fixup.md
??	cc_instruction_e2b_investigate.md
??	cc_instruction_e2b_review.md
??	cc_instruction_e2c.md
??	cc_instruction_e2c_investigate.md
??	cc_instruction_e2d.md
??	cc_instruction_e2d_architecture_review.md
??	cc_instruction_e2d_cleanup.md
??	cc_instruction_e2d_enable.md
??	cc_instruction_e2d_enable_v2.md
??	cc_instruction_e2d_enable_v2_investigate.md
??	cc_instruction_e2d_enable_v3.md
??	cc_instruction_e2d_enable_v3b.md
??	cc_instruction_e2d_investigate.md
??	cc_instruction_e2d_investigate2.md
??	cc_instruction_e2d_v3c_investigate.md
??	cc_instruction_e3.md
??	cc_instruction_e3_investigate.md
??	cc_instruction_engage_u1_uncap.md
??	cc_instruction_equivalence_harness.md
??	cc_instruction_evidence_sizing.md
??	cc_instruction_exemplar_decode_2026_09_01.md
??	cc_instruction_extension_build.md
??	cc_instruction_fetch_more_scores.md
??	cc_instruction_foundation_stage0.md
??	cc_instruction_foundation_stage2a.md
??	cc_instruction_foundation_stage3a.md
??	cc_instruction_foundation_stage3b.md
??	cc_instruction_foundations_verification.md
??	cc_instruction_framework_9_0_correction_2026_08_31.md
??	cc_instruction_functional_residual_investigation.md
??	cc_instruction_gap_analysis_spec_vs_impl.md
??	cc_instruction_gate_default_measure.md
??	cc_instruction_gate_r_verify_and_commit.md
??	cc_instruction_gate_rebaseline_verify.md
??	cc_instruction_grammar_completion.md
??	cc_instruction_housekeeping_e2d.md
??	cc_instruction_housekeeping_e2d_pass2.md
??	cc_instruction_invisible_notes_establishment_2026_09_01.md
??	cc_instruction_j_key_i.md
??	cc_instruction_j_key_ii.md
??	cc_instruction_j_key_ii_redux.md
??	cc_instruction_j_key_iii_integration_investigation.md
??	cc_instruction_j_key_iii_step2_wiring.md
??	cc_instruction_j_key_iii_step3_land.md
??	cc_instruction_j_key_iii_step3c_dormant_commit.md
??	cc_instruction_j_key_iii_step3d_push_then_B.md
??	cc_instruction_jazz_nondeterminism.md
??	cc_instruction_joint_architecture_investigation.md
??	cc_instruction_joint_table_codegen.md
??	cc_instruction_key_emission_headroom.md
??	cc_instruction_keyregression_diagnosis.md
??	cc_instruction_l0l1_boot_pack_2026_08_31.md
??	cc_instruction_l0l1_boot_pack_second_2026_08_31.md
??	cc_instruction_l0l1_exemplar_selection_2026_08_31.md
??	cc_instruction_l1l3_delta_check_resync.md
??	cc_instruction_l1l3_spec_sync.md
??	cc_instruction_l1l4_review_tidy.md
??	cc_instruction_l3_keyalt_forwardcarry.md
??	cc_instruction_l6_dormant_build.md
??	cc_instruction_layer1_audit.md
??	cc_instruction_layer1_coverage.md
??	cc_instruction_layer1_implementation.md
??	cc_instruction_layer1_phase1a_build.md
??	cc_instruction_layer2_audit.md
??	cc_instruction_layer2_corpus_validation.md
??	cc_instruction_layer2_implementation.md
??	cc_instruction_layer2_phase2_build.md
??	cc_instruction_layer3_characterization_scaffold.md
??	cc_instruction_layer3_decoder_audit.md
??	cc_instruction_layer3_decoder_build.md
??	cc_instruction_layer3_decoder_followup.md
??	cc_instruction_layer3_docsync_commit.md
??	cc_instruction_layer3_error_decomposition.md
??	cc_instruction_layer3_incrementA_indexing.md
??	cc_instruction_layer3_incrementB_groundtruth.md
??	cc_instruction_layer3_jazz_churn_investigation.md
??	cc_instruction_layer3_keymode_audit.md
??	cc_instruction_layer3_phase3_build.md
??	cc_instruction_layer3_sweep.md
??	cc_instruction_layer3_tpc_keymeasure.md
??	cc_instruction_layer3_wiring.md
??	cc_instruction_layer3_wiring_code.md
??	cc_instruction_layer3_wiring_commit.md
??	cc_instruction_layer4_audit.md
??	cc_instruction_layer4_b_fairkey.md
??	cc_instruction_layer4_build_increment_a.md
??	cc_instruction_layer4_build_increment_b.md
??	cc_instruction_layer4_residual_decomposition.md
??	cc_instruction_measurement_pipeline_audit.md
??	cc_instruction_metric_build.md
??	cc_instruction_metric_build_l0l1.md
??	cc_instruction_metric_decomposition.md
??	cc_instruction_metric_design_investigation.md
??	cc_instruction_metric_first_investigation.md
??	cc_instruction_metric_rebaseline_batch.md
??	cc_instruction_modulation_keypath_scoping.md
??	cc_instruction_mscz_container_establishment_2026_09_01.md
??	cc_instruction_notation_consumption_audit.md
??	cc_instruction_notation_seams_2.md
??	cc_instruction_oi274_second_half.md
??	cc_instruction_open_items_split.md
??	cc_instruction_partition2_archives.md
??	cc_instruction_phase1h_full_reads.md
??	cc_instruction_phase1i_reads_and_delivery.md
??	cc_instruction_phase2_architecture_support.md
??	cc_instruction_phase5_kmasks_complete.md
??	cc_instruction_phase5_kmasks_derive.md
??	cc_instruction_phase5b_step0_investigate.md
??	cc_instruction_phase5b_step1_g1.md
??	cc_instruction_phase5b_step2_g2.md
??	cc_instruction_phase5b_step2final_o2_inherit.md
??	cc_instruction_phase5b_step3_g6.md
??	cc_instruction_phase5b_step4_g4_spellingpin.md
??	cc_instruction_phase5b_stepM_measure.md
??	cc_instruction_phase5c_L5_close_review.md
??	cc_instruction_phase5c_step1.md
??	cc_instruction_phase5c_step2.md
??	cc_instruction_phase5c_step2_amend.md
??	cc_instruction_phase5c_step2_resolution.md
??	cc_instruction_phase5c_step3.md
??	cc_instruction_phase5c_step4.md
??	cc_instruction_phase5c_step5.md
??	cc_instruction_phase5c_step5_followup.md
??	cc_instruction_phase5c_step6.md
??	cc_instruction_phase5c_stepM.md
??	cc_instruction_phase5c_stepM_consolidate.md
??	cc_instruction_phase5c_stepM_followup.md
??	cc_instruction_phase_d_investigation.md
??	cc_instruction_phase_d_merger.md
??	cc_instruction_phase_d_reanalysis.md
??	cc_instruction_phase_e_commit_unification.md
??	cc_instruction_phase_e_exploration_mode.md
??	cc_instruction_phase_e_predecessor_survey.md
??	cc_instruction_phase_e_rcb_bass_chord_tone_gate.md
??	cc_instruction_phrase_boundary_build.md
??	cc_instruction_precision_headroom_investigation.md
??	cc_instruction_push_bi_checkpoint.md
??	cc_instruction_push_doc_sync.md
??	cc_instruction_push_layer1_checkpoint.md
??	cc_instruction_push_layer2.md
??	cc_instruction_push_layer2_validation.md
??	cc_instruction_push_layer3_incrementA.md
??	cc_instruction_push_layer3_incrementB.md
??	cc_instruction_redesign_segregation.md
??	cc_instruction_redesign_step1_free_wiring.md
??	cc_instruction_redesign_step2_predecessor_confidence.md
??	cc_instruction_refactor1_chordanalyzer_split_design.md
??	cc_instruction_refactor1_split_build.md
??	cc_instruction_refactor_harmonicsegmenter_split.md
??	cc_instruction_refactor_keymodeanalyzer_split.md
??	cc_instruction_refactor_keyresolver_split.md
??	cc_instruction_refactor_regiontonecollector_split.md
??	cc_instruction_refactor_sectionanalyzer_split.md
??	cc_instruction_repair_direction_enumeration.md
??	cc_instruction_repair_index_verify_b2.md
??	cc_instruction_rerun_discovery.md
??	cc_instruction_revert_absent_root_guard.md
??	cc_instruction_roadmap_sync.md
??	cc_instruction_run_discovery.md
??	cc_instruction_scoring_doc.md
??	cc_instruction_sitting_landing_2026_09_01.md
??	cc_instruction_slot_sweep_2026_09_01.md
??	cc_instruction_spec_impl_delta_L1L4.md
??	cc_instruction_stage0_followup.md
??	cc_instruction_stage0_hygiene.md
??	cc_instruction_stage1a_functionlayer_tests.md
??	cc_instruction_stage1b_gate_tests.md
??	cc_instruction_stage1c_segmentation_key_tests.md
??	cc_instruction_stage1d_metric_script_tests.md
??	cc_instruction_stage2_1_phase4c_move.md
??	cc_instruction_stage2_2_ab_exploration.md
??	cc_instruction_stage2_2a_corpus_hardening.md
??	cc_instruction_stage2_2ii_ship_package.md
??	cc_instruction_stage2_3_addendum.md
??	cc_instruction_stage2_3_diagnose_production_view.md
??	cc_instruction_stage2_4_divergence_decisions.md
??	cc_instruction_stage2_4_ratification.md
??	cc_instruction_stage2_5_p3_profile.md
??	cc_instruction_stage3_1_beam1_decoder.md
??	cc_instruction_stage3_1b_approval.md
??	cc_instruction_stage3_1b_decode_once.md
??	cc_instruction_stage3_1b_revision.md
??	cc_instruction_stage3_2_design.md
??	cc_instruction_stage3_3_gater_decision.md
??	cc_instruction_stage3_3_signal_migration.md
??	cc_instruction_stage3_4i_gate_retirement_dossier.md
??	cc_instruction_stage3_4ii_c1_removal.md
??	cc_instruction_stage3_decoder_design.md
??	cc_instruction_stage4_design.md
??	cc_instruction_stage4a_commit_and_stage4b_scoping.md
??	cc_instruction_stage4a_declared_mode_import_fix.md
??	cc_instruction_stage4b_i_commit.md
??	cc_instruction_stage4b_i_demote_and_measure.md
??	cc_instruction_stage4b_ii_strengthen.md
??	cc_instruction_stage4c_i_cadence_detector_measure.md
??	cc_instruction_stage4c_iii_refine_detection.md
??	cc_instruction_stage4d_i_modulation_detector_measure.md
??	cc_instruction_stage5_phase3.md
??	cc_instruction_stage6_tonic_i_labeler_measure.md
??	cc_instruction_step1_pc_primitive_extraction.md
??	cc_instruction_step2_merge_predicate_dedup.md
??	cc_instruction_step3_key_investigation.md
??	cc_instruction_stepback.md
??	cc_instruction_styletag_swap.md
??	cc_instruction_term_grounding_inventory.md
??	cc_instruction_test_backfill.md
??	cc_instruction_tonicization_modulation_metric_check.md
??	cc_instruction_tpc_capability_build.md
??	cc_instruction_tree_repair_and_coverage.md
??	cc_instruction_tsv_oracle_addendum.md
??	cc_instruction_tsv_oracle_infrastructure.md
??	cc_instruction_types_header_build.md
??	cc_instruction_types_header_investigation.md
??	cc_instruction_uncertain_resolver_measurement.md
??	cc_instruction_union_branch_coverage.md
??	cc_instruction_vl_idiom_discovery.md
??	cc_instruction_vocabulary_build.md
??	cc_invisible_notes_establishment_report_2026_09_01.md
??	cc_j_key_i_report.md
??	cc_j_key_ii_redux_report.md
??	cc_j_key_ii_report.md
??	cc_j_key_iii_integration_dossier.md
??	cc_j_key_iii_step2_report.md
??	cc_j_key_iii_step3_report.md
??	cc_jazz_nondeterminism_report.md
??	cc_joint_architecture_dossier.md
??	cc_kmasks_complete_report.md
??	cc_kmasks_derive_report.md
??	cc_l0l1_boot_pack_report.md
??	cc_l0l1_boot_pack_second_report.md
??	cc_l0l1_exemplar_selection_report.md
??	cc_l1l3_delta_check_resync_report.md
??	cc_l1l3_spec_sync_report.md
??	cc_l1l4_review_report.md
??	cc_l3_keyalt_forwardcarry_report.md
??	cc_l6_build_report.md
??	cc_label_table_fit_report.md
??	cc_layer1_audit_dossier.md
??	cc_layer1_doc_sync_report.md
??	cc_layer1_phase1a_report.md
??	cc_layer2_corpus_validation_report.md
??	cc_layer2_phase2_report.md
??	cc_layer3_characterization_report.md
??	cc_layer3_decoder_audit_dossier.md
??	cc_layer3_decoder_build_report.md
??	cc_layer3_incrementA_report.md
??	cc_layer3_incrementB_report.md
??	cc_layer3_keymode_audit_dossier.md
??	cc_layer3_phase3_report.md
??	cc_layer3_wiring_design_dossier.md
??	cc_layer4_audit_dossier.md
??	cc_layer4_build_a_report.md
??	cc_layer4_build_b_fairkey_report.md
??	cc_layer4_build_b_report.md
??	cc_layer4_residual_decomposition_report.md
??	cc_measurement_pipeline_audit.md
??	cc_metric_build_l0l1_report.md
??	cc_metric_build_report.md
??	cc_metric_decomposition_report.md
??	cc_metric_first_dossier.md
??	cc_metric_round2_report.md
??	cc_metric_round3_report.md
??	cc_modulation_keypath_scoping_dossier.md
??	cc_mscz_container_establishment_report.md
??	cc_notation_consumption_audit_report.md
??	cc_phase2_architecture_support_report.md
??	cc_phase5b_step0_report.md
??	cc_phase5b_step1_report.md
??	cc_phase5b_step2_report.md
??	cc_phase5b_step2final_report.md
??	cc_phase5b_step3_report.md
??	cc_phase5b_step4_report.md
??	cc_phase5b_stepM_measure_report.md
??	cc_phase5c_L5_close_review.md
??	cc_phase5c_step0_report.md
??	cc_phase5c_step1_report.md
??	cc_phase5c_step2_amendment.md
??	cc_phase5c_step2_report.md
??	cc_phase5c_step3_report.md
??	cc_phase5c_step4_report.md
??	cc_phase5c_step5_followup_report.md
??	cc_phase5c_step5_report.md
??	cc_phase5c_step6_report.md
??	cc_phase5c_stepM_followup_report.md
??	cc_phase5c_stepM_report.md
??	cc_phase_d_investigation_report.md
??	cc_phase_e_commit_unification_report.md
??	cc_phase_e_exploration_mode_report.md
??	cc_phase_e_predecessor_survey_report.md
??	cc_phrase_boundary_build_report.md
??	cc_precision_headroom_dossier.md
??	cc_refactor_harmonicsegmenter_report.md
??	cc_refactor_keymodeanalyzer_report.md
??	cc_refactor_keyresolver_report.md
??	cc_refactor_regiontonecollector_report.md
??	cc_refactor_sectionanalyzer_report.md
??	cc_secondary_dominant_refit_report.md
??	cc_slot_sweep_report_2026_09_01.md
??	cc_spec_impl_delta_L1L4_report.md
??	cc_stage0_report.md
??	cc_stage1a_report.md
??	cc_stage1b_report.md
??	cc_stage1c_report.md
??	cc_stage1d_report.md
??	cc_stage2_1_report.md
??	cc_stage2_2a_report.md
??	cc_stage2_2ii_report.md
??	cc_stage2_3_report.md
??	cc_stage2_4_report.md
??	cc_stage2_5_report.md
??	cc_stage2a_wip_triage_report.md
??	cc_stage3_1_report.md
??	cc_stage3_1b_report.md
??	cc_stage3_2_design_report.md
??	cc_stage3_3_report.md
??	cc_stage3_4i_dossier.md
??	cc_stage3_4ii_report.md
??	cc_stage3_design_report.md
??	cc_stage3a_notation_triage_report.md
??	cc_stage4_design_report.md
??	cc_stage4b_i_report.md
??	cc_stage4b_ii_report.md
??	cc_stage4b_scoping_dossier.md
??	cc_stage4c_i_report.md
??	cc_stage4c_iii_report.md
??	cc_stage4d_i_report.md
??	cc_stage6_tonic_i_report.md
??	cc_step1_pc_primitive_report.md
??	cc_step2_merge_predicate_report.md
??	cc_stepback_report.md
??	cc_styletag_swap_report.md
??	cc_test_backfill_report.md
??	cc_tpc_capability_build_report.md
??	cc_tpc_capability_verify_report.md
??	cc_tree_repair_and_coverage_report.md
??	cc_tsv_oracle_report.md
??	cc_types_header_build_report.md
??	cc_types_header_investigation_report.md
??	cc_union_branch_coverage_report.md
??	cc_vocabulary_build_report.md
??	cowork_blind_session_brief_l0_l1.md
??	cowork_handoff_entry_eighty_seven.md
??	cowork_handoff_entry_eighty_six.md
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	reading_pass/candidacy_upgrades.md
??	reading_pass/extracts/bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md
??	reading_pass/extracts/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md
??	reading_pass/extracts/pardo-birmingham-2002-algorithms-for-chordal-analysis.md
??	reading_pass/extracts/sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md
??	reading_pass/extracts/temperley-sleator-1999-modeling-meter-and-harmony.md
??	reading_pass/object_reads/
??	reading_pass/remedial_commission_session_record_2026_08_31.md
??	scratch_artifacts/baseline_composing.txt
??	scratch_artifacts/baseline_notation.txt
??	scratch_artifacts/baseline_snapshot.txt
??	scratch_artifacts/baseline_table.md
??	scratch_artifacts/batch_analyze.both.bak
??	scratch_artifacts/batchreg.log
??	scratch_artifacts/bir_after_baroque.txt
??	scratch_artifacts/bir_after_default.txt
??	scratch_artifacts/bir_after_jazz.txt
??	scratch_artifacts/bir_baroque.log
??	scratch_artifacts/bir_baroque.txt
??	scratch_artifacts/bir_default.log
??	scratch_artifacts/bir_default.txt
??	scratch_artifacts/bir_jazz.log
??	scratch_artifacts/bir_jazz.txt
??	scratch_artifacts/build_backfill.txt
??	scratch_artifacts/build_backfill2.txt
??	scratch_artifacts/build_backfill2_err.txt
??	scratch_artifacts/build_backfill_err.txt
??	scratch_artifacts/build_dbg.log
??	scratch_artifacts/build_final.log
??	scratch_artifacts/build_g1.log
??	scratch_artifacts/build_g2.log
??	scratch_artifacts/build_g2b.log
??	scratch_artifacts/build_iso.log
??	scratch_artifacts/build_out.txt
??	scratch_artifacts/build_revert.log
??	scratch_artifacts/build_revert_err.log
??	scratch_artifacts/build_step1.log
??	scratch_artifacts/build_step1b.log
??	scratch_artifacts/build_step1c.log
??	scratch_artifacts/build_step2.log
??	scratch_artifacts/build_stepM.log
??	scratch_artifacts/build_stepM2.log
??	scratch_artifacts/build_stepM_err.log
??	scratch_artifacts/build_task1.log
??	scratch_artifacts/build_task2.log
??	scratch_artifacts/c5_guardhelp.txt
??	scratch_artifacts/c5_p1w.txt
??	scratch_artifacts/c5_triage.txt
??	scratch_artifacts/c5_triage2.txt
??	scratch_artifacts/c8_bar.txt
??	scratch_artifacts/c8_bar2.txt
??	scratch_artifacts/c8_build.log
??	scratch_artifacts/c8_class.txt
??	scratch_artifacts/c8_classchk.txt
??	scratch_artifacts/c8_ct.txt
??	scratch_artifacts/c8_disp.txt
??	scratch_artifacts/c8_dispv.txt
??	scratch_artifacts/c8_gc_t0.txt
??	scratch_artifacts/c8_gc_t1.txt
??	scratch_artifacts/c8_gc_t2.txt
??	scratch_artifacts/c8_gc_t4.txt
??	scratch_artifacts/c8_gc_t4b.txt
??	scratch_artifacts/c8_gp.txt
??	scratch_artifacts/c8_guard_final.txt
??	scratch_artifacts/c8_guard_final2.txt
??	scratch_artifacts/c8_guard_start.txt
??	scratch_artifacts/c8_guard_t0.txt
??	scratch_artifacts/c8_guard_t0b.txt
??	scratch_artifacts/c8_guard_t0c.txt
??	scratch_artifacts/c8_guard_t1.txt
??	scratch_artifacts/c8_guard_t1b.txt
??	scratch_artifacts/c8_guard_t1c.txt
??	scratch_artifacts/c8_guard_t2.txt
??	scratch_artifacts/c8_guard_t2b.txt
??	scratch_artifacts/c8_guard_t4.txt
??	scratch_artifacts/c8_guard_t4b.txt
??	scratch_artifacts/c8_guard_t4c.txt
??	scratch_artifacts/c8_guardclass_start.txt
??	scratch_artifacts/c8_inv.txt
??	scratch_artifacts/c8_lint.txt
??	scratch_artifacts/c8_nt.txt
??	scratch_artifacts/c8_oi357_a.txt
??	scratch_artifacts/c8_oi357_b.txt
??	scratch_artifacts/c8_oi357_c.txt
??	scratch_artifacts/c8_ps.txt
??	scratch_artifacts/c8_r1.txt
??	scratch_artifacts/c8_r12.txt
??	scratch_artifacts/c8_reaim.txt
??	scratch_artifacts/c8_reaimhelp.txt
??	scratch_artifacts/c8_reg.txt
??	scratch_artifacts/c8_regchk.txt
??	scratch_artifacts/c8_routes.txt
??	scratch_artifacts/c8_split.txt
??	scratch_artifacts/c8_sweep.txt
??	scratch_artifacts/c8_sweep2.txt
??	scratch_artifacts/c8_sweep3.txt
??	scratch_artifacts/c8_sweep4.txt
??	scratch_artifacts/c8_sweep5.txt
??	scratch_artifacts/c8_sweep6.txt
??	scratch_artifacts/c8_sweep_list.txt
??	scratch_artifacts/c8_t1_bar.txt
??	scratch_artifacts/c8_t1_bar2.txt
??	scratch_artifacts/c8_t1_blk.txt
??	scratch_artifacts/c8_t1_class.txt
??	scratch_artifacts/c8_t1_class2.txt
??	scratch_artifacts/c8_t1_class3.txt
??	scratch_artifacts/c8_t1_disp.txt
??	scratch_artifacts/c8_t1_disp2.txt
??	scratch_artifacts/c8_t1_fl.txt
??	scratch_artifacts/c8_t1_inv.txt
??	scratch_artifacts/c8_t1_outd.txt
??	scratch_artifacts/c8_t1_reaim.txt
??	scratch_artifacts/c8_t1_reg.txt
??	scratch_artifacts/c8_t1_reg2.txt
??	scratch_artifacts/c8_t1_routes.txt
??	scratch_artifacts/c8_t1_routes2.txt
??	scratch_artifacts/c8_t1_routes3.txt
??	scratch_artifacts/c8_t1_routes4.txt
??	scratch_artifacts/c8_t2_blk.txt
??	scratch_artifacts/c8_t2_class.txt
??	scratch_artifacts/c8_t2_class2.txt
??	scratch_artifacts/c8_t2_class3.txt
??	scratch_artifacts/c8_t2_class4.txt
??	scratch_artifacts/c8_t2_class5.txt
??	scratch_artifacts/c8_t2_disp.txt
??	scratch_artifacts/c8_t2_fl.txt
??	scratch_artifacts/c8_t2_inv.txt
??	scratch_artifacts/c8_t2_outd.txt
??	scratch_artifacts/c8_t2_r1.txt
??	scratch_artifacts/c8_t2_reaim.txt
??	scratch_artifacts/c8_t2_reg.txt
??	scratch_artifacts/c8_t2_routes.txt
??	scratch_artifacts/c8_t4_blk.txt
??	scratch_artifacts/c8_t4_cp.txt
??	scratch_artifacts/c8_t4_cp2.txt
??	scratch_artifacts/c8_t4_cp3.txt
??	scratch_artifacts/c8_t4_cphelp.txt
??	scratch_artifacts/c8_t4_fl.txt
??	scratch_artifacts/c8_t4_fl2.txt
??	scratch_artifacts/c8_t4_inv.txt
??	scratch_artifacts/c8_t4_inv2.txt
??	scratch_artifacts/c8_t4_ng.txt
??	scratch_artifacts/c8_t4_ng2.txt
??	scratch_artifacts/c8_t4_p1w.txt
??	scratch_artifacts/c8_t4_p1w2.txt
??	scratch_artifacts/c8_t4_p1w3.txt
??	scratch_artifacts/c8_t4_r1.txt
??	scratch_artifacts/c8_t4_routes.txt
??	scratch_artifacts/c8_triage.txt
??	scratch_artifacts/c8_triage2.txt
??	scratch_artifacts/c9_changed.txt
??	scratch_artifacts/c9_class.txt
??	scratch_artifacts/c9_classchk.txt
??	scratch_artifacts/c9_guard_start.txt
??	scratch_artifacts/c9_guards1.txt
??	scratch_artifacts/c9_guards2.txt
??	scratch_artifacts/c9_p1w.txt
??	scratch_artifacts/c9_r1.txt
??	scratch_artifacts/c9_reaim.txt
??	scratch_artifacts/c9_regen1.txt
??	scratch_artifacts/c9_regen2.txt
??	scratch_artifacts/c9_regen3.txt
??	scratch_artifacts/c9_routes.txt
??	scratch_artifacts/c9_shellguard_1.txt
??	scratch_artifacts/c9_shellguard_rep.txt
??	scratch_artifacts/c9_split.txt
??	scratch_artifacts/c9_verify1.txt
??	scratch_artifacts/c9_verify2.txt
??	scratch_artifacts/cadence_tests.txt
??	scratch_artifacts/cc_collect.txt
??	scratch_artifacts/ccc_collect2.txt
??	scratch_artifacts/ccc_log.txt
??	scratch_artifacts/ccc_notation.txt
??	scratch_artifacts/ccc_path.txt
??	scratch_artifacts/char_baroque.txt
??	scratch_artifacts/char_baroque_l5m.txt
??	scratch_artifacts/char_default.txt
??	scratch_artifacts/char_default_l5m.txt
??	scratch_artifacts/char_jazz.txt
??	scratch_artifacts/char_jazz_l5m.txt
??	scratch_artifacts/claude_baroque.txt
??	scratch_artifacts/claude_baroque_sorted.txt
??	scratch_artifacts/claude_default.txt
??	scratch_artifacts/claude_default_sorted.txt
??	scratch_artifacts/claude_jazz.txt
??	scratch_artifacts/claude_jazz_sorted.txt
??	scratch_artifacts/clone_algomusdata.txt
??	scratch_artifacts/clone_asap.txt
??	scratch_artifacts/clone_batch1.log
??	scratch_artifacts/clone_batch2.log
??	scratch_artifacts/clone_batch3.log
??	scratch_artifacts/clone_batik.log
??	scratch_artifacts/clone_bcfb.txt
??	scratch_artifacts/clone_cocopops.txt
??	scratch_artifacts/clone_figbass.txt
??	scratch_artifacts/clone_lieder.txt
??	scratch_artifacts/clone_mcma.log
??	scratch_artifacts/clone_mikrokosmos.log
??	scratch_artifacts/clone_openewld.txt
??	scratch_artifacts/clone_piano_svsep.log
??	scratch_artifacts/clone_protovoice.txt
??	scratch_artifacts/clone_schenker41.txt
??	scratch_artifacts/clone_sq.txt
??	scratch_artifacts/clone_vocsep.log
??	scratch_artifacts/cmp_manifest_sha.py
??	scratch_artifacts/commit1_msg.txt
??	scratch_artifacts/commit1_out.txt
??	scratch_artifacts/commit2_msg.txt
??	scratch_artifacts/commit2_out.txt
??	scratch_artifacts/commit_msg_step2.txt
??	scratch_artifacts/comp_run.txt
??	scratch_artifacts/comp_run2.txt
??	scratch_artifacts/comp_run3.txt
??	scratch_artifacts/comp_run4.txt
??	scratch_artifacts/comp_step1.txt
??	scratch_artifacts/comp_step1c.txt
??	scratch_artifacts/composing.cobertura.xml
??	scratch_artifacts/composing_final_out.txt
??	scratch_artifacts/composing_full.txt
??	scratch_artifacts/composing_new_out.txt
??	scratch_artifacts/composing_test.log
??	scratch_artifacts/composing_test2.log
??	scratch_artifacts/composing_tests_out.txt
??	scratch_artifacts/corpus_decode_chord_g1/
??	scratch_artifacts/corpus_decode_chord_g2/
??	scratch_artifacts/corpus_decode_chord_g2iso/
??	scratch_artifacts/corpus_decode_chord_g6/
??	scratch_artifacts/corpus_decode_chord_step2final_A/
??	scratch_artifacts/corpus_decode_chord_step2final_B/
??	scratch_artifacts/corpus_decode_chord_stepM/
??	scratch_artifacts/corpus_ours_check/
??	scratch_artifacts/corpus_ours_check_g2/
??	scratch_artifacts/cov_after.log
??	scratch_artifacts/cov_after2.log
??	scratch_artifacts/cov_final.log
??	scratch_artifacts/cov_final2.log
??	scratch_artifacts/coverage/
??	scratch_artifacts/coverage_merged.txt
??	scratch_artifacts/coverage_report.txt
??	scratch_artifacts/curation_worksheet.txt
??	scratch_artifacts/decode_baroque_step0.log
??	scratch_artifacts/decode_default_step0.log
??	scratch_artifacts/decode_g1_baroque.log
??	scratch_artifacts/decode_g1_baroque2.log
??	scratch_artifacts/decode_g1_default2.log
??	scratch_artifacts/decode_g1_driver.py
??	scratch_artifacts/decode_g2_baroque.log
??	scratch_artifacts/decode_g2_default.log
??	scratch_artifacts/decode_g2iso.log
??	scratch_artifacts/decode_step0_run.log
??	scratch_artifacts/decode_stepM_baroque.log
??	scratch_artifacts/decode_stepM_default.log
??	scratch_artifacts/decompose_g1_after.log
??	scratch_artifacts/decompose_g1_before.log
??	scratch_artifacts/decompose_g2_after.log
??	scratch_artifacts/decompose_g2_before.log
??	scratch_artifacts/decompose_g2iso.log
??	scratch_artifacts/decompose_step0.log
??	scratch_artifacts/dlc_baseline_run.log
??	scratch_artifacts/dlc_pins.json
??	scratch_artifacts/driver_smoke.err
??	scratch_artifacts/e0dp_cap_decomp.py
??	scratch_artifacts/e0prime_grader.log
??	scratch_artifacts/e0prime_supp.log
??	scratch_artifacts/e0prime_supp.py
??	scratch_artifacts/filter_hunks.py
??	scratch_artifacts/fs_regen_baroque.log
??	scratch_artifacts/fs_regen_default.log
??	scratch_artifacts/fs_regen_driver.log
??	scratch_artifacts/fs_regen_jazz.log
??	scratch_artifacts/g1_composing.log
??	scratch_artifacts/g1_decode_tests.log
??	scratch_artifacts/g1_notation.log
??	scratch_artifacts/g1_one_decode.err
??	scratch_artifacts/g1_one_decode.json
??	scratch_artifacts/g1_snapshots.log
??	scratch_artifacts/g2_composing.log
??	scratch_artifacts/g2_decode_tests.log
??	scratch_artifacts/g2_notation.log
??	scratch_artifacts/g2_snap.log
??	scratch_artifacts/gate_after_baroque.txt
??	scratch_artifacts/gate_after_default.txt
??	scratch_artifacts/gate_after_jazz.txt
??	scratch_artifacts/gate_baroque.txt
??	scratch_artifacts/gate_before_baroque.txt
??	scratch_artifacts/gate_before_default.txt
??	scratch_artifacts/gate_before_jazz.txt
??	scratch_artifacts/gate_check.py
??	scratch_artifacts/gate_setdiff.py
??	scratch_artifacts/grade_g1_after.log
??	scratch_artifacts/grade_g1_before.log
??	scratch_artifacts/grade_g2_after.log
??	scratch_artifacts/grade_g2_before.log
??	scratch_artifacts/grade_g2iso.log
??	scratch_artifacts/grade_step0.log
??	scratch_artifacts/guitarset_curl_err.txt
??	scratch_artifacts/guitarset_dl_err.txt
??	scratch_artifacts/guitarset_zenodo.json
??	scratch_artifacts/harvest_final.txt
??	scratch_artifacts/harvest_final2.txt
??	scratch_artifacts/harvest_final3.txt
??	scratch_artifacts/harvest_run1.txt
??	scratch_artifacts/harvest_run2.txt
??	scratch_artifacts/harvest_run3.txt
??	scratch_artifacts/hd_LIST.txt
??	scratch_artifacts/hd_branch.txt
??	scratch_artifacts/hd_dl.txt
??	scratch_artifacts/hd_err.txt
??	scratch_artifacts/hd_lists.json
??	scratch_artifacts/hd_repo.json
??	scratch_artifacts/hd_repos.txt
??	scratch_artifacts/hd_repos_final.txt
??	scratch_artifacts/hd_root.json
??	scratch_artifacts/hd_tree.json
??	scratch_artifacts/humdrum_data_closure_71repos.txt
??	scratch_artifacts/humdrum_gitmodules.txt
??	scratch_artifacts/humdrum_gitmodules2.txt
??	scratch_artifacts/keyparse_probe.log
??	scratch_artifacts/l4.err
??	scratch_artifacts/l4.patch
??	scratch_artifacts/l5.err
??	scratch_artifacts/l5.patch
??	scratch_artifacts/l5_smoke.err
??	scratch_artifacts/l5_smoke.json
??	scratch_artifacts/line_hits.py
??	scratch_artifacts/ninja_direct.txt
??	scratch_artifacts/notation.cobertura.xml
??	scratch_artifacts/notation_after.txt
??	scratch_artifacts/notation_final.txt
??	scratch_artifacts/notation_full.txt
??	scratch_artifacts/notation_run.txt
??	scratch_artifacts/notation_step1.txt
??	scratch_artifacts/notation_test.log
??	scratch_artifacts/notation_test2.log
??	scratch_artifacts/notation_tests_out.txt
??	scratch_artifacts/oi357_production_arm/
??	scratch_artifacts/oi357_production_arm_legacy_control/
??	scratch_artifacts/ours_A/
??	scratch_artifacts/ours_B/
??	scratch_artifacts/ours_check_baroque.log
??	scratch_artifacts/parse_cov.py
??	scratch_artifacts/parse_merge.py
??	scratch_artifacts/pdmx_inspect.py
??	scratch_artifacts/pipeline_snapshot_tests_out.txt
??	scratch_artifacts/quote_verify.txt
??	scratch_artifacts/quote_verify2.txt
??	scratch_artifacts/reg_A.json
??	scratch_artifacts/reg_B.json
??	scratch_artifacts/reg_pre_acq.json
??	scratch_artifacts/reg_run1.json
??	scratch_artifacts/reg_run1.txt
??	scratch_artifacts/reg_run2.txt
??	scratch_artifacts/regen_baroque.log
??	scratch_artifacts/regen_baroque_l5.log
??	scratch_artifacts/regen_default.log
??	scratch_artifacts/regen_default_l5.log
??	scratch_artifacts/regen_driver.log
??	scratch_artifacts/regen_g2_baroque.log
??	scratch_artifacts/regen_jazz.log
??	scratch_artifacts/regen_jazz_l5.log
??	scratch_artifacts/rel_tests.txt
??	scratch_artifacts/repro30.txt
??	scratch_artifacts/repro_block.txt
??	scratch_artifacts/repro_check/
??	scratch_artifacts/s5_2b_task1_tables.txt
??	scratch_artifacts/set_baroque.txt
??	scratch_artifacts/set_default.txt
??	scratch_artifacts/set_jazz.txt
??	scratch_artifacts/setdiff.py
??	scratch_artifacts/sm_comp.txt
??	scratch_artifacts/sm_notation.txt
??	scratch_artifacts/sm_snap.txt
??	scratch_artifacts/smoke.err
??	scratch_artifacts/smoke.json
??	scratch_artifacts/smoke_and_cadence.py
??	scratch_artifacts/snap_after.txt
??	scratch_artifacts/snap_final.txt
??	scratch_artifacts/snap_full.txt
??	scratch_artifacts/snap_run.txt
??	scratch_artifacts/snap_step1.txt
??	scratch_artifacts/snap_test.log
??	scratch_artifacts/snap_test2.log
??	scratch_artifacts/snapshot_full.txt
??	scratch_artifacts/stepM_analysis_all.txt
??	scratch_artifacts/stepM_analysis_test.txt
??	scratch_artifacts/stepM_analyze.py
??	scratch_artifacts/stepM_l5_measure.txt
??	scratch_artifacts/taskB_run.sh
??	scratch_artifacts/u1_byteid/
??	scratch_artifacts/u1_composing_tests.txt
??	scratch_artifacts/u1_pipeline_snap.txt
??	scratch_artifacts/v2_composing.txt
??	scratch_artifacts/v2_notation.txt
??	scratch_artifacts/v2_snap.txt
??	scratch_artifacts/wjd_curl_err.txt
??	tools/audit/derivation_boot_pack/l0-l1/
??	tools/audit/derivation_exemplars/
??	tools/audit/gen_l0l1_exemplar_selection.py
??	tools/audit/gen_score_tags.py
??	tools/audit/l0l1_boot_pack_extension.json
??	tools/audit/l0l1_boot_pack_freeze_and_render.json
??	tools/audit/l0l1_exemplar_selection.json
??	tools/audit/score_tags_l0l1_sweep.json
874 changed path record(s) [worktree]
```

### 1.3 The ruling record IS TRACKED — §0's flagged claim answered

**Established at the git objects, not inherited.**

| what | value |
|---|---|
| HEAD at Task 1 | `f54995c092585f508c4ce572a6a4f553c033da3c` (agrees with the session-start snapshot) |
| the path's blob in HEAD's tree | `d02c571a1d811e6fe3457c9cf4c5917bd248a5c6` |
| size of the committed blob | 16,630 bytes |
| the working copy, pinned at Task 0 | `78b4154e86bfc6d971de50042cd7be53332748fc`, 185,646 bytes |
| divergence, `git diff --numstat` blob→blob | **2,083 lines added, 0 removed** |

**So the writing side's claim was false in the direction it flagged.** The record is tracked; an
earlier state of it is in HEAD's tree; the divergence is a **pure append** — nothing that had landed
was rewritten or removed. What had not landed is this sitting's additions. Both blob identifiers are
given so every value above is re-derivable at the objects rather than taken from this report
(**D-663**).

*The three preceding batches' enumerations, which listed the path as ` M `, were right, and the
prose claim was the thing that was wrong.*

### 1.4 The branch state, and what the rules require

- **Current branch: `master`**, read at the ref and agreeing with the session-start snapshot.
- **`CLAUDE.md` states no branch rule at all.** Its only commit rule is the Convention *"Commit only
  when explicitly asked"* — satisfied: this dispatch orders the commit in terms (§3).
- **The dispatch protocol (`cowork_audit_protocol.md`) states no branch rule either.** What it does
  state, and what this batch is executing, is the interim-carrier clause: *"A sitting record is an
  interim carrier: it is written in the turn its ruling is given and lands in git at the next
  dispatch's Task 0."* That clause also records, at its own text, that **D-230's verbatim is the
  decisions register's rule (c) and says nothing about a sitting record** — so the authority for
  this landing is that clause, and citing D-230 alone would be the shape **D-643** forbids.
- **Nothing forbids committing where I stand. No STOP.**
- **The `"held for Cowork"` convention does NOT apply** — this dispatch does not use that word and
  orders the commit directly.

**One difference reported, as §0.3 requires.** My own generic harness guidance carries a default
*"if on the default branch, branch first."* That is not `CLAUDE.md` and not the dispatch protocol.
The dispatch forbids creating, switching or rebasing anything on my own judgment, the repository's
own established practice is that these landing commits go on `master`, and §0.3 makes the
repository's rules and this document govern. **I committed on `master` and created no branch.**

### 1.5 Whether `cc_instruction_*.md` and `cc_*report*.md` are committed material — the convention is SILENT, and it is committed anyway under §2

Established at the surfaces the dispatch names, not inferred from older ones existing in history:

- **`CLAUDE.md`: silent.** It cites many `cc_*` files as provenance and never says whether they are
  committed material.
- **The dispatch protocol: silent on committing them.** Its rule *"One side writes the instruction
  files and the other executes them"* fixes authorship, not tracking.
- **`.gitignore` is the only surface that speaks, and it speaks by exclusion.** Under the heading
  *"Working-process instruction and report files (CC / Cowork session artifacts)"* it ignores
  exactly three narrow patterns — `/cc_e2d_*.md`, `ai-assistant/CC_INSTRUCTION_*.md`, and
  `tools/cc_*`. **Root-level `cc_instruction_*.md` and `cc_*report*.md` are not ignored.** That is
  evidence they are *not excluded*; it is not a positive rule that they are committed.
- `DECISIONS.md`'s scope block names *"the cc_* session reports"* among what it did not read in
  full, treating them as repository material — again a treatment, not a rule.

**Verdict: the convention is SILENT. Per §1's own instruction I committed them anyway under §2's
list, and the silence is flagged here.**

---

## 2. Task 2 — the commit set, listed individually, and the two things §2 does not reach

### 2.1 What §2 names, what Task 1 found, and what was committed — 29 paths

Every path below was found by Task 1 and is in the commit. **No path in §2's list was missing.**

**The record and the tool it produced (2)**

1. `cowork_rulings_2026_08_31_decision_surface_sitting.md` — modified
2. `cowork_blind_session_brief_l0_l1.md` — new (it appeared untracked, one of the two shapes §7
   allowed for)

**The governing document corrected under a ruling, and the pack machinery (13)**

3. `FRAMEWORK.md` — modified
4. `tools/audit/gen_derivation_boot_pack.py` — modified
5. `tools/audit/derivation_boot_pack.json` — modified
6. `tools/audit/derivation_boot_pack/l0-l1/00_READ_THIS_FIRST.md` — new
7. `tools/audit/derivation_boot_pack/l0-l1/01_the_phase_definitions.md` — new
8. `tools/audit/derivation_boot_pack/l0-l1/02_the_guiding_principles_and_the_conventions.md` — new
9. `tools/audit/derivation_boot_pack/l0-l1/03_the_writing_standards.md` — new
10. `tools/audit/derivation_boot_pack/l0-l1/04_the_dispatch_protocol.md` — new
11. `tools/audit/derivation_boot_pack/l0-l1/05_the_ratified_design_intent.md` — new
12. `tools/audit/derivation_boot_pack/l0-l1/06_the_defect_type_catalog.md` — new
13. `tools/audit/derivation_boot_pack/l0-l1/07_the_charter_the_layers_and_the_decisions.md` — new
14. `tools/audit/derivation_boot_pack/l0-l1/08_the_five_research_extracts.md` — new
15. `tools/audit/derivation_boot_pack/l0-l1/09_the_empirical_findings_ledger.md` — new

*The ten pack members are everything under `…/l0-l1/`, listed at the directory rather than taken on
the writing side's count. The sibling packs `harmony-boundary/` and `scoring-model/` were already
tracked and unmodified and are untouched.*

**The score-tag tool and its table (2)** — §2's "score-tag instrument"; named here as a measurement
tool, the reserved-word convention applying to what is written for the user

16. `tools/audit/gen_score_tags.py` — new
17. `tools/audit/score_tags_l0l1_sweep.json` — new

**This sitting's dispatches (9)** — every file matching `cc_instruction_*_2026_08_31.md` or
`cc_instruction_*_2026_09_01.md` that Task 1 found uncommitted

18. `cc_instruction_l0l1_exemplar_selection_2026_08_31.md`
19. `cc_instruction_l0l1_boot_pack_2026_08_31.md`
20. `cc_instruction_l0l1_boot_pack_second_2026_08_31.md`
21. `cc_instruction_framework_9_0_correction_2026_08_31.md`
22. `cc_instruction_mscz_container_establishment_2026_09_01.md`
23. `cc_instruction_exemplar_decode_2026_09_01.md`
24. `cc_instruction_slot_sweep_2026_09_01.md`
25. `cc_instruction_invisible_notes_establishment_2026_09_01.md`
26. `cc_instruction_sitting_landing_2026_09_01.md` — this batch's own dispatch, which the glob reaches

**The matching dated reports (3)**

27. `cc_exemplar_decode_report_2026_09_01.md`
28. `cc_slot_sweep_report_2026_09_01.md`
29. `cc_invisible_notes_establishment_report_2026_09_01.md`

**Four further files match §2's globs but were ALREADY IN THE TREE, unmodified, so there was nothing
to commit.** Established at the objects (their blobs resolve in the new commit's tree), not inferred
from their absence from the changed-path enumeration:

| file | blob in the tree |
|---|---|
| `cc_instruction_reading_pass_landing_2026_08_31.md` | `cb51384fea5c5aebf51a9e57eb303610b7f9c737` |
| `cc_instruction_reading_pass_landing_second_2026_08_31.md` | `a06bfc2a392267428f0b1182d67035b2ff0b14cc` |
| `cc_report_reading_pass_landing_2026_08_31.md` | `417f1b5f88b263e5337d6d1c5d44d04e821c12fc` |
| `cc_report_reading_pass_landing_second_2026_08_31.md` | `56306eb58c693704a30abb47f66ec4af1731845f` |

### 2.2 ★ AN AMBIGUITY IN §2 THAT CHANGES WHAT LANDS — FIVE OF THIS SITTING'S REPORTS ARE NOT REACHED BY §2'S OWN PATTERN, AND ARE NOT COMMITTED

**§2 states its population in prose and then enumerates it by pattern, and the two do not agree.**
The prose is *"This sitting's dispatches and their reports"*; the pattern is
`cc_*report*_2026_08_31.md` / `cc_*report*_2026_09_01.md`, which requires the date in the file name.
**Five of this sitting's reports carry no date in their names, so the pattern does not reach them,
although the dispatches they answer ARE in §2 and ARE committed:**

- `cc_l0l1_exemplar_selection_report.md` — the report of committed dispatch (18)
- `cc_l0l1_boot_pack_report.md` — the report of committed dispatch (19)
- `cc_l0l1_boot_pack_second_report.md` — the report of committed dispatch (20)
- `cc_framework_9_0_correction_report.md` — the report of committed dispatch (21)
- `cc_mscz_container_establishment_report.md` — the report of committed dispatch (22)

**They are NOT in the commit, and they remain untracked on disk, unchanged.**

**Why the strict reading was taken.** §6 makes *a path in the commit that §2 does not name* a
**STOP**, and makes a §2 path Task 1 does not find *reported, not hunted for* — the two directions
are treated asymmetrically on purpose. Under the pattern, §2 does not name these five; under the
prose, it arguably does. Committing them on the generous reading risks an explicit STOP and is not
undoable by a report; leaving them risks nothing but a second act, and they sit on disk exactly
where the deriving session can read them. **So the reversible branch was taken and the question is
returned to the writing side rather than resolved by my judgment.**

**This is DT-26's shape — scope-assumed enumeration.** A pattern complete inside its own match set,
read as answering a population the prose states more widely; the failure is silent by construction,
because a pattern cannot report what it never matched. It was caught by DT-26's own prescribed
detection: running the same pattern tree-wide and reading the remainder file by file. **One act
closes it: a line from the writing side naming these five, or naming the wider reading.**

### 2.3 ★ THE ONE DELIBERATE EXCLUSION, AND ITS REASON — VERIFIED AT THE OBJECT, NOT INHERITED

**NOT committed, on purpose, and still untracked on disk:**

- `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`
- `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md`

**The ground was re-read at `.gitattributes` rather than taken from the dispatch.** Line 2 carries
`*  text=auto`; **there is no `*.mscx` rule**; and the file's own comment at lines 18–19 says in
terms that *".mscx is uncompressed XML and is left under text=auto by design — only the committed
.mscz set needs this."* Committing the exemplar under that rule would put a CRLF checkout between
the score and its own provenance record's byte-identity claim — **the OI-195 / OI-34
line-ending-normalisation class that `.gitattributes` names in its own words.**

**Whether `.gitattributes` should gain a rule for committed `.mscx` exemplars is OWED TO THE USER.
This batch did not answer it, did not edit `.gitattributes`, and added no ignore rule.** The two
files stay untracked on disk, where the deriving session reads them exactly as they stand.

**This is a thing left undone on purpose, not an oversight.**

---

## 3. Task 3 — the commit

**`e02d982c158d1899da67c5acf1d73478edc6df0b`**, parent `f54995c092585f508c4ce572a6a4f553c033da3c`
— the same HEAD Task 1 established, so nothing was rebased under it.

- **One commit.** Nothing amended, squashed, rebased, force-pushed or tagged.
- **NOT PUSHED**, as ordered. Neither `CLAUDE.md` nor the dispatch protocol makes a push a condition
  of a commit counting as landed, so no STOP arises on that limb.
- The message names what landed and under what authority, names the exclusion and its reason, and
  **carries no value of this project's own measurement** (#17f, **D-431**) — no count of rulings, no
  byte size, no score value.
- Message shape follows the repository's own established form, checked at two prior commit objects
  by explicit hash, including the `Co-Authored-By` trailer.

---

## 4. Task 4 — proof of what landed

### 4.1 The commit's own path list, taken from git

`python tools/audit/changed_paths.py --commit e02d982c158d1899da67c5acf1d73478edc6df0b`:

```
M	FRAMEWORK.md
A	cc_exemplar_decode_report_2026_09_01.md
A	cc_instruction_exemplar_decode_2026_09_01.md
A	cc_instruction_framework_9_0_correction_2026_08_31.md
A	cc_instruction_invisible_notes_establishment_2026_09_01.md
A	cc_instruction_l0l1_boot_pack_2026_08_31.md
A	cc_instruction_l0l1_boot_pack_second_2026_08_31.md
A	cc_instruction_l0l1_exemplar_selection_2026_08_31.md
A	cc_instruction_mscz_container_establishment_2026_09_01.md
A	cc_instruction_sitting_landing_2026_09_01.md
A	cc_instruction_slot_sweep_2026_09_01.md
A	cc_invisible_notes_establishment_report_2026_09_01.md
A	cc_slot_sweep_report_2026_09_01.md
A	cowork_blind_session_brief_l0_l1.md
M	cowork_rulings_2026_08_31_decision_surface_sitting.md
M	tools/audit/derivation_boot_pack.json
A	tools/audit/derivation_boot_pack/l0-l1/00_READ_THIS_FIRST.md
A	tools/audit/derivation_boot_pack/l0-l1/01_the_phase_definitions.md
A	tools/audit/derivation_boot_pack/l0-l1/02_the_guiding_principles_and_the_conventions.md
A	tools/audit/derivation_boot_pack/l0-l1/03_the_writing_standards.md
A	tools/audit/derivation_boot_pack/l0-l1/04_the_dispatch_protocol.md
A	tools/audit/derivation_boot_pack/l0-l1/05_the_ratified_design_intent.md
A	tools/audit/derivation_boot_pack/l0-l1/06_the_defect_type_catalog.md
A	tools/audit/derivation_boot_pack/l0-l1/07_the_charter_the_layers_and_the_decisions.md
A	tools/audit/derivation_boot_pack/l0-l1/08_the_five_research_extracts.md
A	tools/audit/derivation_boot_pack/l0-l1/09_the_empirical_findings_ledger.md
M	tools/audit/gen_derivation_boot_pack.py
A	tools/audit/gen_score_tags.py
A	tools/audit/score_tags_l0l1_sweep.json
29 changed path record(s) [commit]
```

**Both directions checked.** Every one of §2's paths that Task 1 found is in the list (§2.1's
numbered 1–29 map onto it one-for-one). **No path outside §2 is in it** — the commit list is
byte-identical to the staged list I verified before committing, and every entry is named at §2.
**No STOP.**

### 4.2 The two excluded files — still untracked, still on disk, unchanged

| file | fingerprint at Task 1 | after the commit |
|---|---|---|
| `…/l0-l1/bwv1049_03_presto.mscx` | `1cc6dd4c4d97ffd56bac202456137b7b8ba7adee` | **identical** |
| `…/l0-l1/bwv1049_03_presto.provenance.md` | `048e3613a08e104bcfeba552d8618ed3723aaf77` | **identical** |

Untracked state confirmed at git: `git ls-files --error-unmatch` on the score returns *"did not
match any file(s) known to git."*

**Substitution declared, as §1's guard clause requires.** §4 asks for size and `sha256`. Taking
either through a shell means reading working-tree content through a shell, which the standing guard
governs in every dialect — and the guard already refused this batch once. The substitute used is
`git hash-object --no-filters` (no `-w`, so no object was written): **a git blob identifier is
sha1 over the byte length and the bytes together**, so identity of the fingerprint proves identity
of both the size and the content. It is strictly stronger than the pair asked for, and it is a git
object operation rather than a shell content read.

### 4.3 The changed-path enumeration re-run, and what remains uncommitted

`python tools/audit/changed_paths.py` after the commit: **854 records, and NOT ONE of them is
tracked-and-modified** — every ` M ` record of §1.2 is now in the commit.

**The arithmetic reconciles exactly, which is the check that §1.2's listing is faithful:**
874 (before) − 854 (after) = **20 records cleared** = the 4 ` M ` records, plus 16 untracked records
(15 individual files, plus the single directory record `tools/audit/derivation_boot_pack/l0-l1/`
that stood for all ten pack members). 4 + 15 + 10 = the 29 paths in the commit.

**What remains uncommitted, and why:**

1. **The deliberate exclusion** — `tools/audit/derivation_exemplars/` (the score and its provenance
   record). §2.3. Left on purpose; the `.gitattributes` question is the user's.
2. **This batch's own report** — the file you are reading. Created after the commit, as §7 provides.
3. **The five sitting reports §2's pattern does not reach** — §2.2. Returned to the writing side.
4. **Four further L0+L1 sitting artifacts under `tools/audit/` that Task 1 found and §2 does not
   name.** Reported, not hunted for and not committed:
   - `tools/audit/gen_l0l1_exemplar_selection.py`
   - `tools/audit/l0l1_exemplar_selection.json`
   - `tools/audit/l0l1_boot_pack_extension.json`
   - `tools/audit/l0l1_boot_pack_freeze_and_render.json`
5. **The two staged handoff entries** `cowork_handoff_entry_eighty_six.md` and
   `cowork_handoff_entry_eighty_seven.md` — the ones the preceding batch landed as files instead of
   a prepend. §2 does not name them; they stay staged on disk, as that batch left them.
6. **The `reading_pass/` files** (the extracts, `candidacy_upgrades.md`, `object_reads/`, the
   remedial commission record) — not named by §2.
7. **The long pre-existing residue** — the older `cc_*` dispatches and reports, and the whole
   `scratch_artifacts/` tree. Pre-existing, untouched, and outside this batch's subject.
8. **Two third-party research-paper binaries under `external resarch summary/`.** Flagged, not
   acted on: the ignore rule widened on 2026-08-31 reads `docs/research_papers/**/*.pdf` and **does
   not reach this differently-named top-level folder**, so two paper binaries sit untracked in a
   public fork's tree outside the rule that exists to keep them out of it. Nothing has been tracked,
   so nothing has leaked; but the protection here is the absence of an `add`, not a rule. **This
   batch adds no ignore rule** (§7 forbids it) and states the finding for the user.

---

## 5. STOPs

**No STOP was met.**

- No read disagreed with its pin.
- `CLAUDE.md`'s rules do not forbid a commit where I stand — they state no branch rule at all.
- No path in the commit is unnamed by §2.
- Neither excluded file is in the commit, and neither moved on disk.
- No act was taken outside §7.

**Two things met that §6 classes as reported rather than resolved, and both are reported above:**
the shell-read guard's refusal of `git status --porcelain` (§1.1), and the record turning out to be
tracked (§1.3).

**One thing §6 does not anticipate, reported and left for the user:** the gap between §2's prose and
§2's own pattern (§2.2).

**The §7 tracked-modification assumption held exactly.** The four tracked-and-modified paths the
three preceding batches established were the only four found — `FRAMEWORK.md`, the ruling record,
`tools/audit/derivation_boot_pack.json`, `tools/audit/gen_derivation_boot_pack.py` — and
`cowork_blind_session_brief_l0_l1.md` appeared untracked, one of the two shapes §7 allowed for.
**No other tracked modification exists, so no pre-commit STOP arose.**

---

## 6. The standing self-check

Run on the work actually on disk, before this report was written.

- **No file's content was changed by this batch.** There is no content difference to re-read: every
  path in the commit carries the bytes an earlier ruled batch left, and no editor was run on any
  repository file. The acts were git-object pins, one staging, one commit, and this report.
- **#6, one path per concern** — nothing duplicated; the enumerations all come from the one
  sanctioned tool.
- **#12, no information loss** — nothing deleted, nothing overwritten; the excluded files and every
  unnamed path stay on disk, proven unchanged where it matters.
- **#17f / D-431** — no value of this project's own measurement is in the commit message. The values
  in this report are the ones §1 and §4 order reported, and each is published beside the object
  identifier it is re-derivable from (**D-663**).
- **#19** — nothing here is presented as established by not having failed: the ruling record's
  tracked state, the four already-tracked files, the exemplar's untracked state and the
  `.gitattributes` ground were each read at an object or at git.
- **Conventions** — American English; the register named in full as *the open-items register*;
  §2's "score-tag instrument" rendered for the user as the score-tag **measurement tool**, the word
  *instrument* being reserved for a violin; *score* used only of music.
- **`DEFECT_TYPES.md`** — the one catalogued type this batch actually met is **DT-26**
  (scope-assumed enumeration), at §2.2, detected by DT-26's own prescribed method and reported
  rather than papered over. No new defect type is proposed and no catalog entry is added: §7
  forbids it.
- **Footprint (§7)** — one commit and this report. No build, no test, no golden, no measurement of
  the analysis; nothing under `tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; no pack
  rendered and neither frozen pack opened; no open-items row created, flipped or discarded; no
  decisions-register entry and no `D-NNN`; no score staged, edited, renamed, moved, converted or
  re-saved; `tools/snapshot_sources_manifest.json` and the eleven snapshot sources untouched; no
  governing document amended; `.gitattributes` untouched; nothing pushed.
- **The three things §7 forbids repairing in passing were left exactly as they stand:** the
  manifest's `rendered_from` line for pack member (7), the inherited bare uses of *bar* and
  *register* belonging to the scoped terminology pass (**OI-229**), and the `.gitattributes`
  question.

---

## 7. Done

- The true tracked state of the ruling record is established and reported, and §0's flagged claim is
  **answered: it was false** — the record is tracked, and this commit carries the sitting's
  additions rather than its first landing.
- The branch and commit rules were read whole and obeyed; the one difference against my own generic
  harness default is reported at §1.4.
- **One commit exists** carrying exactly §2's found paths, proven both ways from git.
- The exclusion is reported with its reason, verified at `.gitattributes` rather than inherited.
- The post-commit enumeration is given, and reconciles arithmetically with the pre-commit one.
- **One question is returned to the writing side:** the five sitting reports §2's own pattern does
  not reach (§2.2).

*Provenance: CC, 2026-09-01, executing `cc_instruction_sitting_landing_2026_09_01.md`. Every
enumeration in this report is the output of `tools/audit/changed_paths.py`, the substitute the
standing shell-read guard names. Every value about a blob is re-derivable at the object identifier
published beside it. No value of this project's own measurement is transcribed (#17f, D-431).*
