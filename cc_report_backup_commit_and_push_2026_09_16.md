# CC REPORT — backup commit and push, 2026-09-16

**Dispatch:** `cc_instruction_backup_commit_and_push_2026_09_16.md`.
**What this batch did:** it committed, as they stood on disk, the uncommitted files inside the
dispatch's ALLOWED SET, and pushed them to `origin`. It changed the content of no file except
this report. It decided nothing, ruled nothing, opened no paper, moved no measured value, created,
flipped or discarded no open-items row, wrote no decisions-register entry, touched no `src/` file,
no build, no test, no golden and no corpus, and edited no governing document.

---

## The pinned dispatch

`git hash-object -w cc_instruction_backup_commit_and_push_2026_09_16.md` →
**`fe4d4e1fc57da687ee06e0254055e6eb4b934dfd`**. Every later read of the dispatch was taken from
that blob identity.

---

## The premises, each answered

**Premise 1 — the current commit is `0f69cc6b79610c962a8400cdaba3dfc12facfe55` on `master`.**
**HOLDS.** `git rev-parse --abbrev-ref HEAD` → `master`; `git rev-parse HEAD` →
`0f69cc6b79610c962a8400cdaba3dfc12facfe55`.

**Premise 2 — `origin` is `https://github.com/slimvince/MuseScore`.** **HOLDS.** `git remote -v`
reports `origin` at that URL for fetch and for push, and `upstream` at
`https://github.com/musescore/MuseScore.git` for fetch with `disabled` for push. Nothing was
pushed to `upstream`.

**Premise 3 — the changed and untracked paths lie mainly under the ALLOWED SET.** **HOLDS as a
shape, with one qualification the dispatch's own wording produces and which is reported rather
than worked around.** The ALLOWED SET's third root pattern is `cc_report_*.md` — files whose name
BEGINS with `cc_report_`. The repository root carries a large family of untracked session reports
and dossiers named `cc_<subject>_report.md`, `cc_<subject>_dossier.md` and
`cc_<subject>_investigation.md`. **None of those begins with `cc_report_`, so none matches, and
every one of them is in the outside list below and was not committed.** This reading is consistent
with the dispatch's own statement of purpose, which names paper extracts, second extracts, handoff
entries, ruling records and reading-pass edits — the files those reports are not. The only path
matching `cc_report_*.md` at this tree is this report itself, written after the backup commit.

**Premise 4 — `reading_pass/` already has tracked files at the current commit.** **HOLDS.**
`git ls-files reading_pass` reports tracked files, among them `reading_pass/additions.md`,
`reading_pass/continuation.md` and the `reading_pass/cross_checks/` extracts. The directory's
content has therefore been published to `origin` before, and this commit is not its first
publication. No STOP.

---

## Deviations from the dispatch's letter, declared

Each of these is a departure from a literal instruction, taken because a standing rule of
`CLAUDE.md` forbade the literal act or because no tool answers the question the literal act asks.
None of them changes what was committed.

**(1) `git status --porcelain=v1 --untracked-files=all` was REFUSED, and the sanctioned
enumeration was used instead.** The project's shell-read guard denied the command, citing
`CLAUDE.md` Conventions and register entry **D-253**, and named `tools/audit/changed_paths.py` as
the sanctioned way to answer *which paths changed*. That tool enumerates at git's
`--untracked-files=normal`, which **collapses an untracked DIRECTORY into one record** — a
coverage limit the tool states in its own docstring, kept because `=all` expands one scratch
directory in this repository into output large enough to be its own failure under `CLAUDE.md`'s
bash Rule 2. **The consequence for this batch is bounded and was closed:** exactly one collapsed
untracked directory falls inside the ALLOWED SET, `reading_pass/object_reads/`, and its members
were enumerated with the **Glob** file tool — the sanctioned route — so **no allowed-set member is
unnamed below**. Collapsed directories OUTSIDE the set are named as directories and their members
are not listed; nothing was committed from any of them.

**(2) The enumeration was written to a session scratchpad file outside the repository.** The
dispatch says to keep the whole output for the report and write it to no file. **No repository
file was written**, and the enumeration appears in full below. The scratchpad lies outside
`C:\s\MS`, is session-local, and is no part of the record. Without it the enumeration could not be
partitioned without a single shell call producing output large enough to trip bash Rule 2.

**(3) The corruption check read working-tree bytes through PowerShell, and the verdict does not
rest on that read alone.** Task 0(e) asks whether each file is non-empty and free of NUL bytes;
`CLAUDE.md`'s file-tools convention sends local file content through Read / Grep / Glob, and none
of those answers a NUL-byte question over hundreds of files. The dispatch names the byte read
itself (`[System.IO.File]::ReadAllBytes($p) -contains 0`). **The letter-deviation is therefore
declared rather than hidden, and the hazard that convention exists against — a stale mount
returning silently-wrong content — was measured rather than assumed:** after staging, every
staged blob's size was read from the object store BY HASH, which is the content-addressed,
self-verifying route the convention explicitly exempts, and compared against the byte count read
from disk. **The two agree for every file in the allowed-set list, with no mismatch.** Had the
mount been stale, the two would have disagreed.

**(4) Task 1(b) used the sanctioned equivalent of `git diff --cached --name-status`.** The same
guard governs that command; `python tools/audit/changed_paths.py --staged` reports the staged
paths with their status codes and cannot return file content. Its output is reproduced below.

**(5) The commit message carries the standing attribution trailer in addition to the dispatch's
text.** The dispatch's message is committed verbatim — nothing edited, reformatted, re-wrapped or
normalised — and the `Co-Authored-By` trailer follows it, which every commit in this repository's
recent history carries.

**(6) The push published more than this batch's commit, and that is a fact about the remote rather
than about this batch.** `origin/master` stood at `d2ebe3cc98`, behind the local `master`, so the
push also published the commits that were already made and unpushed. They are named under Task 2.

---

## Task 0(c) — the enumeration, in three lists

### List 1 — inside the ALLOWED SET

These are the paths staged and committed. All are untracked additions; none was a modification of
a tracked file. `reading_pass/object_reads/` is expanded to its members.

```
cc_instruction_L5_close_commit.md
cc_instruction_L6_corpus_oracle_check.md
cc_instruction_a8_metric_rebaseline_measure.md
cc_instruction_absent_root_guard.md
cc_instruction_absent_root_investigate.md
cc_instruction_adoption_commit.md
cc_instruction_anchor_design_investigation.md
cc_instruction_anchor_recompute_impl.md
cc_instruction_anchor_redesign_investigation.md
cc_instruction_architecture_opinion.md
cc_instruction_audit_cadencekeyanchor.md
cc_instruction_audit_chordanalyzer_oracle.md
cc_instruction_audit_harmonicfunctionlayer.md
cc_instruction_audit_jointkeydecision.md
cc_instruction_audit_keymodeanalyzer.md
cc_instruction_audit_localmodulationdetector.md
cc_instruction_away_batch.md
cc_instruction_b2_aug7.md
cc_instruction_b2_final.md
cc_instruction_b2_guardfix.md
cc_instruction_b2_retry.md
cc_instruction_b2_subdominant_guard_build.md
cc_instruction_b3.md
cc_instruction_b_dominant_subdominant_guard_scoping.md
cc_instruction_backfill_engravingbridge.md
cc_instruction_backfill_formatter.md
cc_instruction_backfill_l3_keymode.md
cc_instruction_backfill_l4_oracle_gates.md
cc_instruction_backup_batch2.md
cc_instruction_backup_commit_and_push_2026_09_16.md
cc_instruction_backup_cowork_docs.md
cc_instruction_baseline_reconciliation.md
cc_instruction_batch_analyze_restore.md
cc_instruction_batch_analyze_unification_audit.md
cc_instruction_boot_pack_regeneration.md
cc_instruction_bridge_anchor_investigation.md
cc_instruction_bridge_lookahead.md
cc_instruction_bwv301_diagnostic.md
cc_instruction_c1_investigate.md
cc_instruction_cadence_key_investigation.md
cc_instruction_cadence_precision_investigation.md
cc_instruction_carryfix2_resolver_identity.md
cc_instruction_carryfix_dl5a_e0prime.md
cc_instruction_carryfix_task2_addendum.md
cc_instruction_clang_branch_coverage.md
cc_instruction_classifier_fix.md
cc_instruction_commit_cadence_instrument.md
cc_instruction_commit_docs.md
cc_instruction_commit_exploration_mode.md
cc_instruction_commit_idiom_work.md
cc_instruction_commit_reads3.md
cc_instruction_consumer_build.md
cc_instruction_consumer_build_addendum.md
cc_instruction_convert_curated_scores.md
cc_instruction_corpus_clone.md
cc_instruction_corpus_hygiene.md
cc_instruction_corpus_hygiene_corelli.md
cc_instruction_corpus_hygiene_record.md
cc_instruction_corpus_wave1_dlc_onboarding.md
cc_instruction_corpus_wave2_axis2_beds.md
cc_instruction_dcml_parser_applied_root_fix.md
cc_instruction_decision_enumeration_wave.md
cc_instruction_decoder_work_counts.md
cc_instruction_deltaseven_7a_diagnostic.md
cc_instruction_deltaseven_phase_e_diagnostic.md
cc_instruction_deltaseven_predecessor_diagnostic.md
cc_instruction_doc_governance_commit.md
cc_instruction_doc_pass_caps_and_gates.md
cc_instruction_doc_recovery.md
cc_instruction_doc_sync_layer1.md
cc_instruction_doctruth_gate_sync.md
cc_instruction_e0_addendum_carry_cap.md
cc_instruction_e0_fullspine_measure.md
cc_instruction_e1.md
cc_instruction_e2_investigate.md
cc_instruction_e2a.md
cc_instruction_e2b.md
cc_instruction_e2b_fixup.md
cc_instruction_e2b_investigate.md
cc_instruction_e2b_review.md
cc_instruction_e2c.md
cc_instruction_e2c_investigate.md
cc_instruction_e2d.md
cc_instruction_e2d_architecture_review.md
cc_instruction_e2d_cleanup.md
cc_instruction_e2d_enable.md
cc_instruction_e2d_enable_v2.md
cc_instruction_e2d_enable_v2_investigate.md
cc_instruction_e2d_enable_v3.md
cc_instruction_e2d_enable_v3b.md
cc_instruction_e2d_investigate.md
cc_instruction_e2d_investigate2.md
cc_instruction_e2d_v3c_investigate.md
cc_instruction_e3.md
cc_instruction_e3_investigate.md
cc_instruction_engage_u1_uncap.md
cc_instruction_equivalence_harness.md
cc_instruction_evidence_sizing.md
cc_instruction_extension_build.md
cc_instruction_fetch_more_scores.md
cc_instruction_foundation_stage0.md
cc_instruction_foundation_stage2a.md
cc_instruction_foundation_stage3a.md
cc_instruction_foundation_stage3b.md
cc_instruction_foundations_verification.md
cc_instruction_functional_residual_investigation.md
cc_instruction_gap_analysis_spec_vs_impl.md
cc_instruction_gate_default_measure.md
cc_instruction_gate_r_verify_and_commit.md
cc_instruction_gate_rebaseline_verify.md
cc_instruction_grammar_completion.md
cc_instruction_handoff_prepend_2026_09_01.md
cc_instruction_housekeeping_e2d.md
cc_instruction_housekeeping_e2d_pass2.md
cc_instruction_j_key_i.md
cc_instruction_j_key_ii.md
cc_instruction_j_key_ii_redux.md
cc_instruction_j_key_iii_integration_investigation.md
cc_instruction_j_key_iii_step2_wiring.md
cc_instruction_j_key_iii_step3_land.md
cc_instruction_j_key_iii_step3c_dormant_commit.md
cc_instruction_j_key_iii_step3d_push_then_B.md
cc_instruction_jazz_nondeterminism.md
cc_instruction_joint_architecture_investigation.md
cc_instruction_joint_table_codegen.md
cc_instruction_key_emission_headroom.md
cc_instruction_keyregression_diagnosis.md
cc_instruction_l1l3_delta_check_resync.md
cc_instruction_l1l3_spec_sync.md
cc_instruction_l1l4_review_tidy.md
cc_instruction_l3_keyalt_forwardcarry.md
cc_instruction_l6_dormant_build.md
cc_instruction_layer1_audit.md
cc_instruction_layer1_coverage.md
cc_instruction_layer1_implementation.md
cc_instruction_layer1_phase1a_build.md
cc_instruction_layer2_audit.md
cc_instruction_layer2_corpus_validation.md
cc_instruction_layer2_implementation.md
cc_instruction_layer2_phase2_build.md
cc_instruction_layer3_characterization_scaffold.md
cc_instruction_layer3_decoder_audit.md
cc_instruction_layer3_decoder_build.md
cc_instruction_layer3_decoder_followup.md
cc_instruction_layer3_docsync_commit.md
cc_instruction_layer3_error_decomposition.md
cc_instruction_layer3_incrementA_indexing.md
cc_instruction_layer3_incrementB_groundtruth.md
cc_instruction_layer3_jazz_churn_investigation.md
cc_instruction_layer3_keymode_audit.md
cc_instruction_layer3_phase3_build.md
cc_instruction_layer3_sweep.md
cc_instruction_layer3_tpc_keymeasure.md
cc_instruction_layer3_wiring.md
cc_instruction_layer3_wiring_code.md
cc_instruction_layer3_wiring_commit.md
cc_instruction_layer4_audit.md
cc_instruction_layer4_b_fairkey.md
cc_instruction_layer4_build_increment_a.md
cc_instruction_layer4_build_increment_b.md
cc_instruction_layer4_residual_decomposition.md
cc_instruction_measurement_pipeline_audit.md
cc_instruction_metric_build.md
cc_instruction_metric_build_l0l1.md
cc_instruction_metric_decomposition.md
cc_instruction_metric_design_investigation.md
cc_instruction_metric_first_investigation.md
cc_instruction_metric_rebaseline_batch.md
cc_instruction_modulation_keypath_scoping.md
cc_instruction_notation_consumption_audit.md
cc_instruction_notation_seams_2.md
cc_instruction_oi274_second_half.md
cc_instruction_open_items_split.md
cc_instruction_partition2_archives.md
cc_instruction_phase1h_full_reads.md
cc_instruction_phase1i_reads_and_delivery.md
cc_instruction_phase2_architecture_support.md
cc_instruction_phase5_kmasks_complete.md
cc_instruction_phase5_kmasks_derive.md
cc_instruction_phase5b_step0_investigate.md
cc_instruction_phase5b_step1_g1.md
cc_instruction_phase5b_step2_g2.md
cc_instruction_phase5b_step2final_o2_inherit.md
cc_instruction_phase5b_step3_g6.md
cc_instruction_phase5b_step4_g4_spellingpin.md
cc_instruction_phase5b_stepM_measure.md
cc_instruction_phase5c_L5_close_review.md
cc_instruction_phase5c_step1.md
cc_instruction_phase5c_step2.md
cc_instruction_phase5c_step2_amend.md
cc_instruction_phase5c_step2_resolution.md
cc_instruction_phase5c_step3.md
cc_instruction_phase5c_step4.md
cc_instruction_phase5c_step5.md
cc_instruction_phase5c_step5_followup.md
cc_instruction_phase5c_step6.md
cc_instruction_phase5c_stepM.md
cc_instruction_phase5c_stepM_consolidate.md
cc_instruction_phase5c_stepM_followup.md
cc_instruction_phase_d_investigation.md
cc_instruction_phase_d_merger.md
cc_instruction_phase_d_reanalysis.md
cc_instruction_phase_e_commit_unification.md
cc_instruction_phase_e_exploration_mode.md
cc_instruction_phase_e_predecessor_survey.md
cc_instruction_phase_e_rcb_bass_chord_tone_gate.md
cc_instruction_phrase_boundary_build.md
cc_instruction_precision_headroom_investigation.md
cc_instruction_push_bi_checkpoint.md
cc_instruction_push_doc_sync.md
cc_instruction_push_layer1_checkpoint.md
cc_instruction_push_layer2.md
cc_instruction_push_layer2_validation.md
cc_instruction_push_layer3_incrementA.md
cc_instruction_push_layer3_incrementB.md
cc_instruction_redesign_segregation.md
cc_instruction_redesign_step1_free_wiring.md
cc_instruction_redesign_step2_predecessor_confidence.md
cc_instruction_refactor1_chordanalyzer_split_design.md
cc_instruction_refactor1_split_build.md
cc_instruction_refactor_harmonicsegmenter_split.md
cc_instruction_refactor_keymodeanalyzer_split.md
cc_instruction_refactor_keyresolver_split.md
cc_instruction_refactor_regiontonecollector_split.md
cc_instruction_refactor_sectionanalyzer_split.md
cc_instruction_repair_direction_enumeration.md
cc_instruction_repair_index_verify_b2.md
cc_instruction_rerun_discovery.md
cc_instruction_revert_absent_root_guard.md
cc_instruction_roadmap_sync.md
cc_instruction_run_discovery.md
cc_instruction_scoring_doc.md
cc_instruction_sitting_landing_second_2026_09_01.md
cc_instruction_spec_impl_delta_L1L4.md
cc_instruction_stage0_followup.md
cc_instruction_stage0_hygiene.md
cc_instruction_stage1a_functionlayer_tests.md
cc_instruction_stage1b_gate_tests.md
cc_instruction_stage1c_segmentation_key_tests.md
cc_instruction_stage1d_metric_script_tests.md
cc_instruction_stage2_1_phase4c_move.md
cc_instruction_stage2_2_ab_exploration.md
cc_instruction_stage2_2a_corpus_hardening.md
cc_instruction_stage2_2ii_ship_package.md
cc_instruction_stage2_3_addendum.md
cc_instruction_stage2_3_diagnose_production_view.md
cc_instruction_stage2_4_divergence_decisions.md
cc_instruction_stage2_4_ratification.md
cc_instruction_stage2_5_p3_profile.md
cc_instruction_stage3_1_beam1_decoder.md
cc_instruction_stage3_1b_approval.md
cc_instruction_stage3_1b_decode_once.md
cc_instruction_stage3_1b_revision.md
cc_instruction_stage3_2_design.md
cc_instruction_stage3_3_gater_decision.md
cc_instruction_stage3_3_signal_migration.md
cc_instruction_stage3_4i_gate_retirement_dossier.md
cc_instruction_stage3_4ii_c1_removal.md
cc_instruction_stage3_decoder_design.md
cc_instruction_stage4_design.md
cc_instruction_stage4a_commit_and_stage4b_scoping.md
cc_instruction_stage4a_declared_mode_import_fix.md
cc_instruction_stage4b_i_commit.md
cc_instruction_stage4b_i_demote_and_measure.md
cc_instruction_stage4b_ii_strengthen.md
cc_instruction_stage4c_i_cadence_detector_measure.md
cc_instruction_stage4c_iii_refine_detection.md
cc_instruction_stage4d_i_modulation_detector_measure.md
cc_instruction_stage5_phase3.md
cc_instruction_stage6_tonic_i_labeler_measure.md
cc_instruction_step1_pc_primitive_extraction.md
cc_instruction_step2_merge_predicate_dedup.md
cc_instruction_step3_key_investigation.md
cc_instruction_stepback.md
cc_instruction_styletag_swap.md
cc_instruction_term_grounding_inventory.md
cc_instruction_test_backfill.md
cc_instruction_tonicization_modulation_metric_check.md
cc_instruction_tpc_capability_build.md
cc_instruction_tree_repair_and_coverage.md
cc_instruction_tsv_oracle_addendum.md
cc_instruction_tsv_oracle_infrastructure.md
cc_instruction_types_header_build.md
cc_instruction_types_header_investigation.md
cc_instruction_uncertain_resolver_measurement.md
cc_instruction_union_branch_coverage.md
cc_instruction_vl_idiom_discovery.md
cc_instruction_vocabulary_build.md
cowork_handoff_entry_one_hundred_and_eighteen.md
cowork_handoff_entry_one_hundred_and_eighty.md
cowork_handoff_entry_one_hundred_and_eighty_eight.md
cowork_handoff_entry_one_hundred_and_eighty_five.md
cowork_handoff_entry_one_hundred_and_eighty_four.md
cowork_handoff_entry_one_hundred_and_eighty_one.md
cowork_handoff_entry_one_hundred_and_eighty_seven.md
cowork_handoff_entry_one_hundred_and_eighty_six.md
cowork_handoff_entry_one_hundred_and_eighty_three.md
cowork_handoff_entry_one_hundred_and_eighty_two-1.md
cowork_handoff_entry_one_hundred_and_eighty_two.md
cowork_handoff_entry_one_hundred_and_eleven.md
cowork_handoff_entry_one_hundred_and_fifteen.md
cowork_handoff_entry_one_hundred_and_fifty_eight.md
cowork_handoff_entry_one_hundred_and_fifty_five.md
cowork_handoff_entry_one_hundred_and_fifty_four.md
cowork_handoff_entry_one_hundred_and_fifty_nine.md
cowork_handoff_entry_one_hundred_and_fifty_one.md
cowork_handoff_entry_one_hundred_and_fifty_seven.md
cowork_handoff_entry_one_hundred_and_fifty_six.md
cowork_handoff_entry_one_hundred_and_fifty_three.md
cowork_handoff_entry_one_hundred_and_fifty_two.md
cowork_handoff_entry_one_hundred_and_forty.md
cowork_handoff_entry_one_hundred_and_forty_five.md
cowork_handoff_entry_one_hundred_and_forty_four.md
cowork_handoff_entry_one_hundred_and_forty_one.md
cowork_handoff_entry_one_hundred_and_forty_six.md
cowork_handoff_entry_one_hundred_and_forty_three.md
cowork_handoff_entry_one_hundred_and_forty_two.md
cowork_handoff_entry_one_hundred_and_fourteen.md
cowork_handoff_entry_one_hundred_and_nine.md
cowork_handoff_entry_one_hundred_and_nineteen.md
cowork_handoff_entry_one_hundred_and_seventeen.md
cowork_handoff_entry_one_hundred_and_seventy.md
cowork_handoff_entry_one_hundred_and_seventy_eight.md
cowork_handoff_entry_one_hundred_and_seventy_five.md
cowork_handoff_entry_one_hundred_and_seventy_four.md
cowork_handoff_entry_one_hundred_and_seventy_nine.md
cowork_handoff_entry_one_hundred_and_seventy_one.md
cowork_handoff_entry_one_hundred_and_seventy_seven.md
cowork_handoff_entry_one_hundred_and_seventy_six.md
cowork_handoff_entry_one_hundred_and_seventy_three.md
cowork_handoff_entry_one_hundred_and_seventy_two.md
cowork_handoff_entry_one_hundred_and_sixteen.md
cowork_handoff_entry_one_hundred_and_sixty.md
cowork_handoff_entry_one_hundred_and_sixty_eight.md
cowork_handoff_entry_one_hundred_and_sixty_five.md
cowork_handoff_entry_one_hundred_and_sixty_four.md
cowork_handoff_entry_one_hundred_and_sixty_nine.md
cowork_handoff_entry_one_hundred_and_sixty_one.md
cowork_handoff_entry_one_hundred_and_sixty_seven.md
cowork_handoff_entry_one_hundred_and_sixty_six.md
cowork_handoff_entry_one_hundred_and_sixty_three.md
cowork_handoff_entry_one_hundred_and_sixty_two.md
cowork_handoff_entry_one_hundred_and_ten.md
cowork_handoff_entry_one_hundred_and_thirteen.md
cowork_handoff_entry_one_hundred_and_thirty.md
cowork_handoff_entry_one_hundred_and_thirty_eight.md
cowork_handoff_entry_one_hundred_and_thirty_five.md
cowork_handoff_entry_one_hundred_and_thirty_four.md
cowork_handoff_entry_one_hundred_and_thirty_nine.md
cowork_handoff_entry_one_hundred_and_thirty_one.md
cowork_handoff_entry_one_hundred_and_thirty_seven.md
cowork_handoff_entry_one_hundred_and_thirty_six.md
cowork_handoff_entry_one_hundred_and_thirty_three.md
cowork_handoff_entry_one_hundred_and_thirty_two.md
cowork_handoff_entry_one_hundred_and_twelve.md
cowork_handoff_entry_one_hundred_and_twenty.md
cowork_handoff_entry_one_hundred_and_twenty_eight.md
cowork_handoff_entry_one_hundred_and_twenty_five.md
cowork_handoff_entry_one_hundred_and_twenty_four.md
cowork_handoff_entry_one_hundred_and_twenty_nine.md
cowork_handoff_entry_one_hundred_and_twenty_one.md
cowork_handoff_entry_one_hundred_and_twenty_seven.md
cowork_handoff_entry_one_hundred_and_twenty_six.md
cowork_handoff_entry_one_hundred_and_twenty_three.md
cowork_handoff_entry_one_hundred_and_twenty_two.md
cowork_l2_boot_list_surface_2026_09_05.md
cowork_l2_first_pass_extracts_derivation_2026_09_05.md
cowork_l2_score_set_read_2026_09_05.md
cowork_l2_task_b_slice_derivation_2026_09_05.md
cowork_rulings_2026_09_05_l2_boot_list_sitting.md
cowork_rulings_2026_09_11_satellite_arc_close.md
reading_pass/candidacy_upgrades.md
reading_pass/extracts/bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md
reading_pass/extracts/burgoyne-pugin-kereliuk-fujinaga-2007-a-cross-validated-study-of-modelling-strategies-for-automatic-chord-recognition-in-audio.md
reading_pass/extracts/catteau-martens-leman-2006-model-based-approach-to-scale-and-chord-estimation.md
reading_pass/extracts/chen-su-2018-functional-harmony-recognition-of-symbolic-music-data-with-multi-task-rnn.md
reading_pass/extracts/chen-su-2019-harmony-transformer-incorporating-chord-segmentation-into-harmony-recognition.md
reading_pass/extracts/chen-su-2021-attend-to-chords-improving-harmonic-analysis-of-symbolic-music.md
reading_pass/extracts/chew-2002-spiral-array-algorithm-for-determining-key-boundaries.md
reading_pass/extracts/conditschultz-ju-fujinaga-2018-a-flexible-approach-to-automated-harmonic-analysis.md
reading_pass/extracts/declercq-2015-a-model-for-scale-degree-reinterpretation.md
reading_pass/extracts/feisthauer-bigo-giraud-leve-2020-estimating-keys-and-modulations-in-musical-pieces.md
reading_pass/extracts/granrothwilding-2013-harmonic-analysis-of-music-using-combinatory-categorial-grammar.md
reading_pass/extracts/granrothwilding-steedman-2012-statistical-parsing-for-harmonic-analysis-of-jazz-chord-sequences.md
reading_pass/extracts/harasim-rohrmeier-odonnell-2018-a-generalized-parsing-framework-for-generative-models-of-harmonic-syntax.md
reading_pass/extracts/illescas-rizo-inesta-2007-harmonic-melodic-and-functional-automatic-analysis.md
reading_pass/extracts/jacoby-tishby-tymoczko-2015-an-information-theoretic-approach-to-chord-categorization-and-functional-harmony.md
reading_pass/extracts/ju-conditschultz-arthur-fujinaga-2017-non-chord-tone-identification-using-deep-neural-networks.md
reading_pass/extracts/ju-howes-mckay-conditschultz-calvozaragoza-fujinaga-2019-an-interactive-workflow-for-generating-chord-labels.md
reading_pass/extracts/karystinaios-hentschel-neuwirth-widmer-2025-analysisgnn-unified-music-analysis.md
reading_pass/extracts/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md
reading_pass/extracts/karystinaios-widmer-2023-roman-numeral-analysis-with-graph-neural-networks.md
reading_pass/extracts/korzeniowski-widmer-2018-improved-chord-recognition-by-combining-duration-and-harmonic-language-models.md
reading_pass/extracts/lafferty-mccallum-pereira-2001-conditional-random-fields-for-segmenting-and-labeling-sequence-data-1.md
reading_pass/extracts/lafferty-mccallum-pereira-2001-conditional-random-fields-for-segmenting-and-labeling-sequence-data.md
reading_pass/extracts/masada-bunescu-2019-chord-recognition-in-symbolic-music-a-segmental-crf-model.md
reading_pass/extracts/micchi-gotham-giraud-2020-not-all-roads-lead-to-rome-pitch-representation-and-model-architecture.md
reading_pass/extracts/napoleslopez-gotham-fujinaga-2021-augmentednet-roman-numeral-analysis-network.md
reading_pass/extracts/ng-jordan-2001-on-discriminative-vs-generative-classifiers.md
reading_pass/extracts/ni-mcvicar-santosrodriguez-debie-2011-end-to-end-machine-learning-system-harmonic-analysis.md
reading_pass/extracts/noland-sandler-2006-key-estimation-using-a-hidden-markov-model.md
reading_pass/extracts/och-2003-minimum-error-rate-training-in-statistical-machine-translation.md
reading_pass/extracts/pardo-birmingham-2002-algorithms-for-chordal-analysis.md
reading_pass/extracts/raphael-stoddard-2003-harmonic-analysis-with-probabilistic-graphical-models.md
reading_pass/extracts/rocher-robine-hanna-oudre-2010-concurrent-estimation-of-chords-and-keys.md
reading_pass/extracts/rohrmeier-2006-towards-modelling-harmonic-movement-in-music.md
reading_pass/extracts/rohrmeier-2011-towards-a-generative-syntax-of-tonal-harmony.md
reading_pass/extracts/sailor-2024-rnbert-fine-tuning-a-masked-language-model-for-roman-numeral-analysis.md
reading_pass/extracts/sarawagi-cohen-2004-semi-markov-conditional-random-fields.md
reading_pass/extracts/sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md
reading_pass/extracts/sha-pereira-2003-shallow-parsing-with-conditional-random-fields.md
reading_pass/extracts/sheh-ellis-2003-chord-segmentation-and-recognition-using-em-trained-hidden-markov-models.md
reading_pass/extracts/sutton-mccallum-2006-an-introduction-to-conditional-random-fields-for-relational-learning.md
reading_pass/extracts/temperley-2002-a-bayesian-approach-to-key-finding.md
reading_pass/extracts/temperley-2009-unified-probabilistic-model-polyphonic-music-analysis.md
reading_pass/extracts/temperley-sleator-1999-modeling-meter-and-harmony.md
reading_pass/extracts/tsushima-nakamura-itoyama-yoshii-2017-arxiv-generative-statistical-models-with-self-emergent-grammar-of-chord-sequences.md
reading_pass/extracts/wu-nakamura-yoshii-2020-variational-autoencoder-for-joint-chord-and-key-estimation.md
reading_pass/extracts/yang-cwitkowitz-duan-2023-harmonic-analysis-with-neural-semi-crf.md
reading_pass/extracts_second_pass/catteau-martens-leman-2006-model-based-approach-to-scale-and-chord-estimation.md
reading_pass/extracts_second_pass/chen-su-2018-functional-harmony-recognition-of-symbolic-music-data-with-multi-task-rnn.md
reading_pass/extracts_second_pass/feisthauer-bigo-giraud-leve-2020-estimating-keys-and-modulations-in-musical-pieces.md
reading_pass/extracts_second_pass/karystinaios-hentschel-neuwirth-widmer-2025-analysisgnn-unified-music-analysis.md
reading_pass/extracts_second_pass/karystinaios-widmer-2023-roman-numeral-analysis-with-graph-neural-networks-onset-wise-predictions.md
reading_pass/extracts_second_pass/korzeniowski-widmer-2018-improved-chord-recognition-by-combining-duration-and-harmonic-language-models.md
reading_pass/extracts_second_pass/masada-bunescu-2019-chord-recognition-in-symbolic-music-a-segmental-crf-model.md
reading_pass/extracts_second_pass/micchi-gotham-giraud-2020-not-all-roads-lead-to-rome-pitch-representation-and-model-architecture.md
reading_pass/extracts_second_pass/napoleslopez-gotham-fujinaga-2021-augmentednet-roman-numeral-analysis-network.md
reading_pass/extracts_second_pass/noland-sandler-2006-key-estimation-using-a-hidden-markov-model.md
reading_pass/extracts_second_pass/och-2003-minimum-error-rate-training-in-statistical-machine-translation.md
reading_pass/extracts_second_pass/raphael-stoddard-2003-harmonic-analysis-with-probabilistic-graphical-models.md
reading_pass/extracts_second_pass/rocher-robine-hanna-oudre-2010-concurrent-estimation-of-chords-and-keys.md
reading_pass/extracts_second_pass/sailor-2024-rnbert-fine-tuning-a-masked-language-model-for-roman-numeral-analysis.md
reading_pass/extracts_second_pass/sarawagi-cohen-2004-semi-markov-conditional-random-fields.md
reading_pass/extracts_second_pass/sheh-ellis-2003-chord-segmentation-and-recognition-using-em-trained-hidden-markov-models.md
reading_pass/extracts_second_pass/temperley-2002-a-bayesian-approach-to-key-finding.md
reading_pass/extracts_second_pass/temperley-2009-unified-probabilistic-model-for-polyphonic-music-analysis.md
reading_pass/extracts_second_pass/yang-cwitkowitz-duan-2023-harmonic-analysis-with-neural-semi-crf.md
reading_pass/l2_slice_reading_progress.md
reading_pass/l2_slice_reading_progress_companion.md
reading_pass/object_reads/derived_row_set.md
reading_pass/object_reads/stop_task_a_method_2026_08_31.md
reading_pass/object_reads/row1_mcleod-rohrmeier-2021-modular-harmonic-analysis.md
reading_pass/object_reads/row2_mcleod-rohrmeier-2024-chord-tone-alterations-suspensions.md
reading_pass/object_reads/stop_row2_dpd_defusal_2026_08_31.md
reading_pass/object_reads/row5_dehaas-magalhaes-wiering-veltkamp-harmtrace.md
reading_pass/object_reads/row17_sapp-2005-visual-hierarchical-key-analysis.md
reading_pass/object_reads/row18_viaccoz-harasim-moss-rohrmeier-wavescapes.md
reading_pass/object_reads/row21_humphrey-bello-2015-four-timely-insights.md
reading_pass/object_reads/row3_hentschel-moss-mcleod-neuwirth-rohrmeier-unified-chord-model.md
reading_pass/object_reads/task_a_consolidated_2026_08_31.md
reading_pass/remedial_commission_session_record_2026_08_31.md
```

### List 2 — outside the ALLOWED SET — reported, NOT committed

Each line carries git's two-character status code and the path. A path ending in `/` is an
untracked directory git reported as one record; its members are not listed and none was committed.

**The three paths under `docs/research_papers/` are reported by path and change type only, as the
dispatch requires, and no file under that directory was opened or staged:**
`docs/research_papers/BIBLIOGRAPHY.md` — modified in the working tree, not staged;
`docs/research_papers/README.md` — modified in the working tree, not staged;
`docs/research_papers/polyph9-release/` — an untracked directory.

Nothing under `src/`, `decisions/` or `open_items/` shows a change, and neither `CLAUDE.md`,
`DECISIONS.md`, `STATUS.md`, `ARCHITECTURE.md`, `OPEN_ITEMS.md` nor `BUILD_AND_TEST.md` shows one.
Under `tools/` the enumeration reports one path, `tools/audit/derivation_exemplars/`, an untracked
directory, which was not staged.

```
 M	docs/research_papers/BIBLIOGRAPHY.md
 M	docs/research_papers/README.md
??	Claude outputs/
??	Codex research inventory/
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
??	cc_extension_build_report.md
??	cc_foundations_verification_report.md
??	cc_gate_r_report.md
??	cc_gate_r_verify_report.md
??	cc_handoff_prepend_report_2026_09_01.md
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
??	cc_sitting_landing_second_report_2026_09_01.md
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
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
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
??	tools/audit/derivation_exemplars/
```

### List 3 — deleted or renamed

**Empty.** No record in the enumeration carries a `D` or an `R` in either status position, so no
deletion and no rename was staged, and none is reported.

---

## Task 0(e) — the corruption check

Every path in List 1 was read as bytes. **No file is empty. No file contains a NUL byte. No file
exceeds 5 MB, and therefore none exceeds 50 MB.** Every path in the list exists as a file — none
was missing. **No STOP condition fired.**

The cross-check described under deviation (3): every staged blob's size, taken from the object
store by hash, equals the byte count read from disk, for every member of the list, with no
mismatch.

## Task 0(f) — the three sizes against their expected values

| Path | Expected | Found | Verdict |
|---|---|---|---|
| `reading_pass/extracts/och-2003-minimum-error-rate-training-in-statistical-machine-translation.md` | 53513 | 53513 | matches |
| `reading_pass/extracts_second_pass/och-2003-minimum-error-rate-training-in-statistical-machine-translation.md` | 50903 | 50903 | matches |
| `cowork_handoff_entry_one_hundred_and_eighty_eight.md` | 12349 | 12349 | matches |

All three match the dispatch's expected value exactly. The device bridge the dispatch warns about
did not land stale bytes for any of them.

---

## Task 1 — staging and the commit

**(a)** The paths of List 1 were staged by explicit path, through a NUL-separated pathspec file
(`git add --pathspec-from-file=… --pathspec-file-nul`). **`git add -A`, `git add .` and every
glob were avoided.** No deletion and no rename was staged, there being none.

**(b)** The staged enumeration was compared against List 1 as a SET, in both directions:
**no staged path lies outside the ALLOWED SET, and no member of the ALLOWED SET is unstaged.**
Every staged record carries status `A`. The enumeration follows.

```
A	cc_instruction_L5_close_commit.md
A	cc_instruction_L6_corpus_oracle_check.md
A	cc_instruction_a8_metric_rebaseline_measure.md
A	cc_instruction_absent_root_guard.md
A	cc_instruction_absent_root_investigate.md
A	cc_instruction_adoption_commit.md
A	cc_instruction_anchor_design_investigation.md
A	cc_instruction_anchor_recompute_impl.md
A	cc_instruction_anchor_redesign_investigation.md
A	cc_instruction_architecture_opinion.md
A	cc_instruction_audit_cadencekeyanchor.md
A	cc_instruction_audit_chordanalyzer_oracle.md
A	cc_instruction_audit_harmonicfunctionlayer.md
A	cc_instruction_audit_jointkeydecision.md
A	cc_instruction_audit_keymodeanalyzer.md
A	cc_instruction_audit_localmodulationdetector.md
A	cc_instruction_away_batch.md
A	cc_instruction_b2_aug7.md
A	cc_instruction_b2_final.md
A	cc_instruction_b2_guardfix.md
A	cc_instruction_b2_retry.md
A	cc_instruction_b2_subdominant_guard_build.md
A	cc_instruction_b3.md
A	cc_instruction_b_dominant_subdominant_guard_scoping.md
A	cc_instruction_backfill_engravingbridge.md
A	cc_instruction_backfill_formatter.md
A	cc_instruction_backfill_l3_keymode.md
A	cc_instruction_backfill_l4_oracle_gates.md
A	cc_instruction_backup_batch2.md
A	cc_instruction_backup_commit_and_push_2026_09_16.md
A	cc_instruction_backup_cowork_docs.md
A	cc_instruction_baseline_reconciliation.md
A	cc_instruction_batch_analyze_restore.md
A	cc_instruction_batch_analyze_unification_audit.md
A	cc_instruction_boot_pack_regeneration.md
A	cc_instruction_bridge_anchor_investigation.md
A	cc_instruction_bridge_lookahead.md
A	cc_instruction_bwv301_diagnostic.md
A	cc_instruction_c1_investigate.md
A	cc_instruction_cadence_key_investigation.md
A	cc_instruction_cadence_precision_investigation.md
A	cc_instruction_carryfix2_resolver_identity.md
A	cc_instruction_carryfix_dl5a_e0prime.md
A	cc_instruction_carryfix_task2_addendum.md
A	cc_instruction_clang_branch_coverage.md
A	cc_instruction_classifier_fix.md
A	cc_instruction_commit_cadence_instrument.md
A	cc_instruction_commit_docs.md
A	cc_instruction_commit_exploration_mode.md
A	cc_instruction_commit_idiom_work.md
A	cc_instruction_commit_reads3.md
A	cc_instruction_consumer_build.md
A	cc_instruction_consumer_build_addendum.md
A	cc_instruction_convert_curated_scores.md
A	cc_instruction_corpus_clone.md
A	cc_instruction_corpus_hygiene.md
A	cc_instruction_corpus_hygiene_corelli.md
A	cc_instruction_corpus_hygiene_record.md
A	cc_instruction_corpus_wave1_dlc_onboarding.md
A	cc_instruction_corpus_wave2_axis2_beds.md
A	cc_instruction_dcml_parser_applied_root_fix.md
A	cc_instruction_decision_enumeration_wave.md
A	cc_instruction_decoder_work_counts.md
A	cc_instruction_deltaseven_7a_diagnostic.md
A	cc_instruction_deltaseven_phase_e_diagnostic.md
A	cc_instruction_deltaseven_predecessor_diagnostic.md
A	cc_instruction_doc_governance_commit.md
A	cc_instruction_doc_pass_caps_and_gates.md
A	cc_instruction_doc_recovery.md
A	cc_instruction_doc_sync_layer1.md
A	cc_instruction_doctruth_gate_sync.md
A	cc_instruction_e0_addendum_carry_cap.md
A	cc_instruction_e0_fullspine_measure.md
A	cc_instruction_e1.md
A	cc_instruction_e2_investigate.md
A	cc_instruction_e2a.md
A	cc_instruction_e2b.md
A	cc_instruction_e2b_fixup.md
A	cc_instruction_e2b_investigate.md
A	cc_instruction_e2b_review.md
A	cc_instruction_e2c.md
A	cc_instruction_e2c_investigate.md
A	cc_instruction_e2d.md
A	cc_instruction_e2d_architecture_review.md
A	cc_instruction_e2d_cleanup.md
A	cc_instruction_e2d_enable.md
A	cc_instruction_e2d_enable_v2.md
A	cc_instruction_e2d_enable_v2_investigate.md
A	cc_instruction_e2d_enable_v3.md
A	cc_instruction_e2d_enable_v3b.md
A	cc_instruction_e2d_investigate.md
A	cc_instruction_e2d_investigate2.md
A	cc_instruction_e2d_v3c_investigate.md
A	cc_instruction_e3.md
A	cc_instruction_e3_investigate.md
A	cc_instruction_engage_u1_uncap.md
A	cc_instruction_equivalence_harness.md
A	cc_instruction_evidence_sizing.md
A	cc_instruction_extension_build.md
A	cc_instruction_fetch_more_scores.md
A	cc_instruction_foundation_stage0.md
A	cc_instruction_foundation_stage2a.md
A	cc_instruction_foundation_stage3a.md
A	cc_instruction_foundation_stage3b.md
A	cc_instruction_foundations_verification.md
A	cc_instruction_functional_residual_investigation.md
A	cc_instruction_gap_analysis_spec_vs_impl.md
A	cc_instruction_gate_default_measure.md
A	cc_instruction_gate_r_verify_and_commit.md
A	cc_instruction_gate_rebaseline_verify.md
A	cc_instruction_grammar_completion.md
A	cc_instruction_handoff_prepend_2026_09_01.md
A	cc_instruction_housekeeping_e2d.md
A	cc_instruction_housekeeping_e2d_pass2.md
A	cc_instruction_j_key_i.md
A	cc_instruction_j_key_ii.md
A	cc_instruction_j_key_ii_redux.md
A	cc_instruction_j_key_iii_integration_investigation.md
A	cc_instruction_j_key_iii_step2_wiring.md
A	cc_instruction_j_key_iii_step3_land.md
A	cc_instruction_j_key_iii_step3c_dormant_commit.md
A	cc_instruction_j_key_iii_step3d_push_then_B.md
A	cc_instruction_jazz_nondeterminism.md
A	cc_instruction_joint_architecture_investigation.md
A	cc_instruction_joint_table_codegen.md
A	cc_instruction_key_emission_headroom.md
A	cc_instruction_keyregression_diagnosis.md
A	cc_instruction_l1l3_delta_check_resync.md
A	cc_instruction_l1l3_spec_sync.md
A	cc_instruction_l1l4_review_tidy.md
A	cc_instruction_l3_keyalt_forwardcarry.md
A	cc_instruction_l6_dormant_build.md
A	cc_instruction_layer1_audit.md
A	cc_instruction_layer1_coverage.md
A	cc_instruction_layer1_implementation.md
A	cc_instruction_layer1_phase1a_build.md
A	cc_instruction_layer2_audit.md
A	cc_instruction_layer2_corpus_validation.md
A	cc_instruction_layer2_implementation.md
A	cc_instruction_layer2_phase2_build.md
A	cc_instruction_layer3_characterization_scaffold.md
A	cc_instruction_layer3_decoder_audit.md
A	cc_instruction_layer3_decoder_build.md
A	cc_instruction_layer3_decoder_followup.md
A	cc_instruction_layer3_docsync_commit.md
A	cc_instruction_layer3_error_decomposition.md
A	cc_instruction_layer3_incrementA_indexing.md
A	cc_instruction_layer3_incrementB_groundtruth.md
A	cc_instruction_layer3_jazz_churn_investigation.md
A	cc_instruction_layer3_keymode_audit.md
A	cc_instruction_layer3_phase3_build.md
A	cc_instruction_layer3_sweep.md
A	cc_instruction_layer3_tpc_keymeasure.md
A	cc_instruction_layer3_wiring.md
A	cc_instruction_layer3_wiring_code.md
A	cc_instruction_layer3_wiring_commit.md
A	cc_instruction_layer4_audit.md
A	cc_instruction_layer4_b_fairkey.md
A	cc_instruction_layer4_build_increment_a.md
A	cc_instruction_layer4_build_increment_b.md
A	cc_instruction_layer4_residual_decomposition.md
A	cc_instruction_measurement_pipeline_audit.md
A	cc_instruction_metric_build.md
A	cc_instruction_metric_build_l0l1.md
A	cc_instruction_metric_decomposition.md
A	cc_instruction_metric_design_investigation.md
A	cc_instruction_metric_first_investigation.md
A	cc_instruction_metric_rebaseline_batch.md
A	cc_instruction_modulation_keypath_scoping.md
A	cc_instruction_notation_consumption_audit.md
A	cc_instruction_notation_seams_2.md
A	cc_instruction_oi274_second_half.md
A	cc_instruction_open_items_split.md
A	cc_instruction_partition2_archives.md
A	cc_instruction_phase1h_full_reads.md
A	cc_instruction_phase1i_reads_and_delivery.md
A	cc_instruction_phase2_architecture_support.md
A	cc_instruction_phase5_kmasks_complete.md
A	cc_instruction_phase5_kmasks_derive.md
A	cc_instruction_phase5b_step0_investigate.md
A	cc_instruction_phase5b_step1_g1.md
A	cc_instruction_phase5b_step2_g2.md
A	cc_instruction_phase5b_step2final_o2_inherit.md
A	cc_instruction_phase5b_step3_g6.md
A	cc_instruction_phase5b_step4_g4_spellingpin.md
A	cc_instruction_phase5b_stepM_measure.md
A	cc_instruction_phase5c_L5_close_review.md
A	cc_instruction_phase5c_step1.md
A	cc_instruction_phase5c_step2.md
A	cc_instruction_phase5c_step2_amend.md
A	cc_instruction_phase5c_step2_resolution.md
A	cc_instruction_phase5c_step3.md
A	cc_instruction_phase5c_step4.md
A	cc_instruction_phase5c_step5.md
A	cc_instruction_phase5c_step5_followup.md
A	cc_instruction_phase5c_step6.md
A	cc_instruction_phase5c_stepM.md
A	cc_instruction_phase5c_stepM_consolidate.md
A	cc_instruction_phase5c_stepM_followup.md
A	cc_instruction_phase_d_investigation.md
A	cc_instruction_phase_d_merger.md
A	cc_instruction_phase_d_reanalysis.md
A	cc_instruction_phase_e_commit_unification.md
A	cc_instruction_phase_e_exploration_mode.md
A	cc_instruction_phase_e_predecessor_survey.md
A	cc_instruction_phase_e_rcb_bass_chord_tone_gate.md
A	cc_instruction_phrase_boundary_build.md
A	cc_instruction_precision_headroom_investigation.md
A	cc_instruction_push_bi_checkpoint.md
A	cc_instruction_push_doc_sync.md
A	cc_instruction_push_layer1_checkpoint.md
A	cc_instruction_push_layer2.md
A	cc_instruction_push_layer2_validation.md
A	cc_instruction_push_layer3_incrementA.md
A	cc_instruction_push_layer3_incrementB.md
A	cc_instruction_redesign_segregation.md
A	cc_instruction_redesign_step1_free_wiring.md
A	cc_instruction_redesign_step2_predecessor_confidence.md
A	cc_instruction_refactor1_chordanalyzer_split_design.md
A	cc_instruction_refactor1_split_build.md
A	cc_instruction_refactor_harmonicsegmenter_split.md
A	cc_instruction_refactor_keymodeanalyzer_split.md
A	cc_instruction_refactor_keyresolver_split.md
A	cc_instruction_refactor_regiontonecollector_split.md
A	cc_instruction_refactor_sectionanalyzer_split.md
A	cc_instruction_repair_direction_enumeration.md
A	cc_instruction_repair_index_verify_b2.md
A	cc_instruction_rerun_discovery.md
A	cc_instruction_revert_absent_root_guard.md
A	cc_instruction_roadmap_sync.md
A	cc_instruction_run_discovery.md
A	cc_instruction_scoring_doc.md
A	cc_instruction_sitting_landing_second_2026_09_01.md
A	cc_instruction_spec_impl_delta_L1L4.md
A	cc_instruction_stage0_followup.md
A	cc_instruction_stage0_hygiene.md
A	cc_instruction_stage1a_functionlayer_tests.md
A	cc_instruction_stage1b_gate_tests.md
A	cc_instruction_stage1c_segmentation_key_tests.md
A	cc_instruction_stage1d_metric_script_tests.md
A	cc_instruction_stage2_1_phase4c_move.md
A	cc_instruction_stage2_2_ab_exploration.md
A	cc_instruction_stage2_2a_corpus_hardening.md
A	cc_instruction_stage2_2ii_ship_package.md
A	cc_instruction_stage2_3_addendum.md
A	cc_instruction_stage2_3_diagnose_production_view.md
A	cc_instruction_stage2_4_divergence_decisions.md
A	cc_instruction_stage2_4_ratification.md
A	cc_instruction_stage2_5_p3_profile.md
A	cc_instruction_stage3_1_beam1_decoder.md
A	cc_instruction_stage3_1b_approval.md
A	cc_instruction_stage3_1b_decode_once.md
A	cc_instruction_stage3_1b_revision.md
A	cc_instruction_stage3_2_design.md
A	cc_instruction_stage3_3_gater_decision.md
A	cc_instruction_stage3_3_signal_migration.md
A	cc_instruction_stage3_4i_gate_retirement_dossier.md
A	cc_instruction_stage3_4ii_c1_removal.md
A	cc_instruction_stage3_decoder_design.md
A	cc_instruction_stage4_design.md
A	cc_instruction_stage4a_commit_and_stage4b_scoping.md
A	cc_instruction_stage4a_declared_mode_import_fix.md
A	cc_instruction_stage4b_i_commit.md
A	cc_instruction_stage4b_i_demote_and_measure.md
A	cc_instruction_stage4b_ii_strengthen.md
A	cc_instruction_stage4c_i_cadence_detector_measure.md
A	cc_instruction_stage4c_iii_refine_detection.md
A	cc_instruction_stage4d_i_modulation_detector_measure.md
A	cc_instruction_stage5_phase3.md
A	cc_instruction_stage6_tonic_i_labeler_measure.md
A	cc_instruction_step1_pc_primitive_extraction.md
A	cc_instruction_step2_merge_predicate_dedup.md
A	cc_instruction_step3_key_investigation.md
A	cc_instruction_stepback.md
A	cc_instruction_styletag_swap.md
A	cc_instruction_term_grounding_inventory.md
A	cc_instruction_test_backfill.md
A	cc_instruction_tonicization_modulation_metric_check.md
A	cc_instruction_tpc_capability_build.md
A	cc_instruction_tree_repair_and_coverage.md
A	cc_instruction_tsv_oracle_addendum.md
A	cc_instruction_tsv_oracle_infrastructure.md
A	cc_instruction_types_header_build.md
A	cc_instruction_types_header_investigation.md
A	cc_instruction_uncertain_resolver_measurement.md
A	cc_instruction_union_branch_coverage.md
A	cc_instruction_vl_idiom_discovery.md
A	cc_instruction_vocabulary_build.md
A	cowork_handoff_entry_one_hundred_and_eighteen.md
A	cowork_handoff_entry_one_hundred_and_eighty.md
A	cowork_handoff_entry_one_hundred_and_eighty_eight.md
A	cowork_handoff_entry_one_hundred_and_eighty_five.md
A	cowork_handoff_entry_one_hundred_and_eighty_four.md
A	cowork_handoff_entry_one_hundred_and_eighty_one.md
A	cowork_handoff_entry_one_hundred_and_eighty_seven.md
A	cowork_handoff_entry_one_hundred_and_eighty_six.md
A	cowork_handoff_entry_one_hundred_and_eighty_three.md
A	cowork_handoff_entry_one_hundred_and_eighty_two-1.md
A	cowork_handoff_entry_one_hundred_and_eighty_two.md
A	cowork_handoff_entry_one_hundred_and_eleven.md
A	cowork_handoff_entry_one_hundred_and_fifteen.md
A	cowork_handoff_entry_one_hundred_and_fifty_eight.md
A	cowork_handoff_entry_one_hundred_and_fifty_five.md
A	cowork_handoff_entry_one_hundred_and_fifty_four.md
A	cowork_handoff_entry_one_hundred_and_fifty_nine.md
A	cowork_handoff_entry_one_hundred_and_fifty_one.md
A	cowork_handoff_entry_one_hundred_and_fifty_seven.md
A	cowork_handoff_entry_one_hundred_and_fifty_six.md
A	cowork_handoff_entry_one_hundred_and_fifty_three.md
A	cowork_handoff_entry_one_hundred_and_fifty_two.md
A	cowork_handoff_entry_one_hundred_and_forty.md
A	cowork_handoff_entry_one_hundred_and_forty_five.md
A	cowork_handoff_entry_one_hundred_and_forty_four.md
A	cowork_handoff_entry_one_hundred_and_forty_one.md
A	cowork_handoff_entry_one_hundred_and_forty_six.md
A	cowork_handoff_entry_one_hundred_and_forty_three.md
A	cowork_handoff_entry_one_hundred_and_forty_two.md
A	cowork_handoff_entry_one_hundred_and_fourteen.md
A	cowork_handoff_entry_one_hundred_and_nine.md
A	cowork_handoff_entry_one_hundred_and_nineteen.md
A	cowork_handoff_entry_one_hundred_and_seventeen.md
A	cowork_handoff_entry_one_hundred_and_seventy.md
A	cowork_handoff_entry_one_hundred_and_seventy_eight.md
A	cowork_handoff_entry_one_hundred_and_seventy_five.md
A	cowork_handoff_entry_one_hundred_and_seventy_four.md
A	cowork_handoff_entry_one_hundred_and_seventy_nine.md
A	cowork_handoff_entry_one_hundred_and_seventy_one.md
A	cowork_handoff_entry_one_hundred_and_seventy_seven.md
A	cowork_handoff_entry_one_hundred_and_seventy_six.md
A	cowork_handoff_entry_one_hundred_and_seventy_three.md
A	cowork_handoff_entry_one_hundred_and_seventy_two.md
A	cowork_handoff_entry_one_hundred_and_sixteen.md
A	cowork_handoff_entry_one_hundred_and_sixty.md
A	cowork_handoff_entry_one_hundred_and_sixty_eight.md
A	cowork_handoff_entry_one_hundred_and_sixty_five.md
A	cowork_handoff_entry_one_hundred_and_sixty_four.md
A	cowork_handoff_entry_one_hundred_and_sixty_nine.md
A	cowork_handoff_entry_one_hundred_and_sixty_one.md
A	cowork_handoff_entry_one_hundred_and_sixty_seven.md
A	cowork_handoff_entry_one_hundred_and_sixty_six.md
A	cowork_handoff_entry_one_hundred_and_sixty_three.md
A	cowork_handoff_entry_one_hundred_and_sixty_two.md
A	cowork_handoff_entry_one_hundred_and_ten.md
A	cowork_handoff_entry_one_hundred_and_thirteen.md
A	cowork_handoff_entry_one_hundred_and_thirty.md
A	cowork_handoff_entry_one_hundred_and_thirty_eight.md
A	cowork_handoff_entry_one_hundred_and_thirty_five.md
A	cowork_handoff_entry_one_hundred_and_thirty_four.md
A	cowork_handoff_entry_one_hundred_and_thirty_nine.md
A	cowork_handoff_entry_one_hundred_and_thirty_one.md
A	cowork_handoff_entry_one_hundred_and_thirty_seven.md
A	cowork_handoff_entry_one_hundred_and_thirty_six.md
A	cowork_handoff_entry_one_hundred_and_thirty_three.md
A	cowork_handoff_entry_one_hundred_and_thirty_two.md
A	cowork_handoff_entry_one_hundred_and_twelve.md
A	cowork_handoff_entry_one_hundred_and_twenty.md
A	cowork_handoff_entry_one_hundred_and_twenty_eight.md
A	cowork_handoff_entry_one_hundred_and_twenty_five.md
A	cowork_handoff_entry_one_hundred_and_twenty_four.md
A	cowork_handoff_entry_one_hundred_and_twenty_nine.md
A	cowork_handoff_entry_one_hundred_and_twenty_one.md
A	cowork_handoff_entry_one_hundred_and_twenty_seven.md
A	cowork_handoff_entry_one_hundred_and_twenty_six.md
A	cowork_handoff_entry_one_hundred_and_twenty_three.md
A	cowork_handoff_entry_one_hundred_and_twenty_two.md
A	cowork_l2_boot_list_surface_2026_09_05.md
A	cowork_l2_first_pass_extracts_derivation_2026_09_05.md
A	cowork_l2_score_set_read_2026_09_05.md
A	cowork_l2_task_b_slice_derivation_2026_09_05.md
A	cowork_rulings_2026_09_05_l2_boot_list_sitting.md
A	cowork_rulings_2026_09_11_satellite_arc_close.md
A	reading_pass/candidacy_upgrades.md
A	reading_pass/extracts/bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md
A	reading_pass/extracts/burgoyne-pugin-kereliuk-fujinaga-2007-a-cross-validated-study-of-modelling-strategies-for-automatic-chord-recognition-in-audio.md
A	reading_pass/extracts/catteau-martens-leman-2006-model-based-approach-to-scale-and-chord-estimation.md
A	reading_pass/extracts/chen-su-2018-functional-harmony-recognition-of-symbolic-music-data-with-multi-task-rnn.md
A	reading_pass/extracts/chen-su-2019-harmony-transformer-incorporating-chord-segmentation-into-harmony-recognition.md
A	reading_pass/extracts/chen-su-2021-attend-to-chords-improving-harmonic-analysis-of-symbolic-music.md
A	reading_pass/extracts/chew-2002-spiral-array-algorithm-for-determining-key-boundaries.md
A	reading_pass/extracts/conditschultz-ju-fujinaga-2018-a-flexible-approach-to-automated-harmonic-analysis.md
A	reading_pass/extracts/declercq-2015-a-model-for-scale-degree-reinterpretation.md
A	reading_pass/extracts/feisthauer-bigo-giraud-leve-2020-estimating-keys-and-modulations-in-musical-pieces.md
A	reading_pass/extracts/granrothwilding-2013-harmonic-analysis-of-music-using-combinatory-categorial-grammar.md
A	reading_pass/extracts/granrothwilding-steedman-2012-statistical-parsing-for-harmonic-analysis-of-jazz-chord-sequences.md
A	reading_pass/extracts/harasim-rohrmeier-odonnell-2018-a-generalized-parsing-framework-for-generative-models-of-harmonic-syntax.md
A	reading_pass/extracts/illescas-rizo-inesta-2007-harmonic-melodic-and-functional-automatic-analysis.md
A	reading_pass/extracts/jacoby-tishby-tymoczko-2015-an-information-theoretic-approach-to-chord-categorization-and-functional-harmony.md
A	reading_pass/extracts/ju-conditschultz-arthur-fujinaga-2017-non-chord-tone-identification-using-deep-neural-networks.md
A	reading_pass/extracts/ju-howes-mckay-conditschultz-calvozaragoza-fujinaga-2019-an-interactive-workflow-for-generating-chord-labels.md
A	reading_pass/extracts/karystinaios-hentschel-neuwirth-widmer-2025-analysisgnn-unified-music-analysis.md
A	reading_pass/extracts/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md
A	reading_pass/extracts/karystinaios-widmer-2023-roman-numeral-analysis-with-graph-neural-networks.md
A	reading_pass/extracts/korzeniowski-widmer-2018-improved-chord-recognition-by-combining-duration-and-harmonic-language-models.md
A	reading_pass/extracts/lafferty-mccallum-pereira-2001-conditional-random-fields-for-segmenting-and-labeling-sequence-data-1.md
A	reading_pass/extracts/lafferty-mccallum-pereira-2001-conditional-random-fields-for-segmenting-and-labeling-sequence-data.md
A	reading_pass/extracts/masada-bunescu-2019-chord-recognition-in-symbolic-music-a-segmental-crf-model.md
A	reading_pass/extracts/micchi-gotham-giraud-2020-not-all-roads-lead-to-rome-pitch-representation-and-model-architecture.md
A	reading_pass/extracts/napoleslopez-gotham-fujinaga-2021-augmentednet-roman-numeral-analysis-network.md
A	reading_pass/extracts/ng-jordan-2001-on-discriminative-vs-generative-classifiers.md
A	reading_pass/extracts/ni-mcvicar-santosrodriguez-debie-2011-end-to-end-machine-learning-system-harmonic-analysis.md
A	reading_pass/extracts/noland-sandler-2006-key-estimation-using-a-hidden-markov-model.md
A	reading_pass/extracts/och-2003-minimum-error-rate-training-in-statistical-machine-translation.md
A	reading_pass/extracts/pardo-birmingham-2002-algorithms-for-chordal-analysis.md
A	reading_pass/extracts/raphael-stoddard-2003-harmonic-analysis-with-probabilistic-graphical-models.md
A	reading_pass/extracts/rocher-robine-hanna-oudre-2010-concurrent-estimation-of-chords-and-keys.md
A	reading_pass/extracts/rohrmeier-2006-towards-modelling-harmonic-movement-in-music.md
A	reading_pass/extracts/rohrmeier-2011-towards-a-generative-syntax-of-tonal-harmony.md
A	reading_pass/extracts/sailor-2024-rnbert-fine-tuning-a-masked-language-model-for-roman-numeral-analysis.md
A	reading_pass/extracts/sarawagi-cohen-2004-semi-markov-conditional-random-fields.md
A	reading_pass/extracts/sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md
A	reading_pass/extracts/sha-pereira-2003-shallow-parsing-with-conditional-random-fields.md
A	reading_pass/extracts/sheh-ellis-2003-chord-segmentation-and-recognition-using-em-trained-hidden-markov-models.md
A	reading_pass/extracts/sutton-mccallum-2006-an-introduction-to-conditional-random-fields-for-relational-learning.md
A	reading_pass/extracts/temperley-2002-a-bayesian-approach-to-key-finding.md
A	reading_pass/extracts/temperley-2009-unified-probabilistic-model-polyphonic-music-analysis.md
A	reading_pass/extracts/temperley-sleator-1999-modeling-meter-and-harmony.md
A	reading_pass/extracts/tsushima-nakamura-itoyama-yoshii-2017-arxiv-generative-statistical-models-with-self-emergent-grammar-of-chord-sequences.md
A	reading_pass/extracts/wu-nakamura-yoshii-2020-variational-autoencoder-for-joint-chord-and-key-estimation.md
A	reading_pass/extracts/yang-cwitkowitz-duan-2023-harmonic-analysis-with-neural-semi-crf.md
A	reading_pass/extracts_second_pass/catteau-martens-leman-2006-model-based-approach-to-scale-and-chord-estimation.md
A	reading_pass/extracts_second_pass/chen-su-2018-functional-harmony-recognition-of-symbolic-music-data-with-multi-task-rnn.md
A	reading_pass/extracts_second_pass/feisthauer-bigo-giraud-leve-2020-estimating-keys-and-modulations-in-musical-pieces.md
A	reading_pass/extracts_second_pass/karystinaios-hentschel-neuwirth-widmer-2025-analysisgnn-unified-music-analysis.md
A	reading_pass/extracts_second_pass/karystinaios-widmer-2023-roman-numeral-analysis-with-graph-neural-networks-onset-wise-predictions.md
A	reading_pass/extracts_second_pass/korzeniowski-widmer-2018-improved-chord-recognition-by-combining-duration-and-harmonic-language-models.md
A	reading_pass/extracts_second_pass/masada-bunescu-2019-chord-recognition-in-symbolic-music-a-segmental-crf-model.md
A	reading_pass/extracts_second_pass/micchi-gotham-giraud-2020-not-all-roads-lead-to-rome-pitch-representation-and-model-architecture.md
A	reading_pass/extracts_second_pass/napoleslopez-gotham-fujinaga-2021-augmentednet-roman-numeral-analysis-network.md
A	reading_pass/extracts_second_pass/noland-sandler-2006-key-estimation-using-a-hidden-markov-model.md
A	reading_pass/extracts_second_pass/och-2003-minimum-error-rate-training-in-statistical-machine-translation.md
A	reading_pass/extracts_second_pass/raphael-stoddard-2003-harmonic-analysis-with-probabilistic-graphical-models.md
A	reading_pass/extracts_second_pass/rocher-robine-hanna-oudre-2010-concurrent-estimation-of-chords-and-keys.md
A	reading_pass/extracts_second_pass/sailor-2024-rnbert-fine-tuning-a-masked-language-model-for-roman-numeral-analysis.md
A	reading_pass/extracts_second_pass/sarawagi-cohen-2004-semi-markov-conditional-random-fields.md
A	reading_pass/extracts_second_pass/sheh-ellis-2003-chord-segmentation-and-recognition-using-em-trained-hidden-markov-models.md
A	reading_pass/extracts_second_pass/temperley-2002-a-bayesian-approach-to-key-finding.md
A	reading_pass/extracts_second_pass/temperley-2009-unified-probabilistic-model-for-polyphonic-music-analysis.md
A	reading_pass/extracts_second_pass/yang-cwitkowitz-duan-2023-harmonic-analysis-with-neural-semi-crf.md
A	reading_pass/l2_slice_reading_progress.md
A	reading_pass/l2_slice_reading_progress_companion.md
A	reading_pass/object_reads/derived_row_set.md
A	reading_pass/object_reads/row17_sapp-2005-visual-hierarchical-key-analysis.md
A	reading_pass/object_reads/row18_viaccoz-harasim-moss-rohrmeier-wavescapes.md
A	reading_pass/object_reads/row1_mcleod-rohrmeier-2021-modular-harmonic-analysis.md
A	reading_pass/object_reads/row21_humphrey-bello-2015-four-timely-insights.md
A	reading_pass/object_reads/row2_mcleod-rohrmeier-2024-chord-tone-alterations-suspensions.md
A	reading_pass/object_reads/row3_hentschel-moss-mcleod-neuwirth-rohrmeier-unified-chord-model.md
A	reading_pass/object_reads/row5_dehaas-magalhaes-wiering-veltkamp-harmtrace.md
A	reading_pass/object_reads/stop_row2_dpd_defusal_2026_08_31.md
A	reading_pass/object_reads/stop_task_a_method_2026_08_31.md
A	reading_pass/object_reads/task_a_consolidated_2026_08_31.md
A	reading_pass/remedial_commission_session_record_2026_08_31.md
```

**(c)** Committed verbatim with the dispatch's message.

**Commit identity: `d7bb4720036ac7356c8d5a2b17d161c12e558f80`.**

---

## Task 2 — the push

`git push origin master` **succeeded**, reporting `d2ebe3cc98..d7bb472003  master -> master`.
It was run without `--force` and without `--force-with-lease`; `upstream` was not pushed to; no
other branch was pushed. No pull, merge or rebase was performed.

After the push:

- `git rev-parse HEAD` → `d7bb4720036ac7356c8d5a2b17d161c12e558f80`
- `git rev-parse origin/master` → `d7bb4720036ac7356c8d5a2b17d161c12e558f80`

**The two are equal.**

Because `origin/master` stood at `d2ebe3cc98`, this push also published the commits below, which
were made before this batch and had not reached the remote. They are named rather than counted:

- `0f69cc6b79610c962a8400cdaba3dfc12facfe55` — close: the authored-ends batch — entries, the forward bound, the ordered regeneration
- `e6fa18961a097ab2b2c7afa2affe57aeeed630bf` — measure: the marked-clause ends become AUTHORED, and the spent dispatch is re-bannered
- `fc88d1c41ab03f13558a7a3e7de0bf211059d52b` — track: the fourth sitting's records, the authored ends pass, and this dispatch
- `cdd7ff4aca948156291725c76535bedfd84d9be5` — close: the defense-share sizing batch — STATUS.md covering both commits, the forward bound once
- `38e8d81ab7e867e282117e9110fd8cf105a74833` — measure: the defense share of the session-start read, with the span coordinates made reachable
- `02b816b86376b4b48152485a0592223b31484229` — track: the third issue, the second issue's report, and the two handoff entries
- `45a0527b90e895bee735cf9aa57c4d8e2a640478` — track: the defense-satellite sitting's records, the first issue's stop, and this dispatch

---

## The `STATUS.md` question, reported and not acted on

The dispatch declares that no `STATUS.md` entry, no forward-bound re-aiming and no regeneration of
any `tools/audit/` artifact is ordered, and directs that a standing rule judged to require an
entry be **reported by name and file location rather than acted on**. Two such rules were read at
session start and are named here; **neither was acted on, and no `STATUS.md` entry was written.**

- **`STATUS.md`'s own opening banner**, at `C:\s\MS\STATUS.md`, first block: *"Living document.
  Claude Code reads this at the start of every session. Update this as the last act when anything
  changes."* Commits landed, so something changed.
- **The forward bound — Ruling 4 of `cowork_rulings_2026_08_17_governing_surface_split.md`**,
  pointed at from `STATUS.md`'s own archive paragraphs: an entry is superseded the moment a later
  batch's close exists, this file keeps only the latest batch's entries, and every future close
  moves the then-previous batch's entries in the same act that writes its own.

Whether a backup commit that changes no file's content is a *batch close* in the sense those rules
govern is not settled by this report, and this batch did not settle it by acting.

---

## The standing self-check

The diff of this batch was re-read against the guiding principles, the conventions and the gate
policy before reporting. What it found, and what was done:

- **The reserved-word convention** (`CLAUDE.md` Conventions, D-113): this report uses *measurement
  tool*, *check* and *script* and never *instrument*; *size* and *value* rather than bare *figure*;
  and the bare words *score*, *key* and *measure* appear nowhere in a non-musical sense.
- **No count of this batch's own acts is asserted anywhere above.** Every list names its members.
  Where the dispatch itself states an expected size, that value is quoted as the dispatch's, and
  the value found is stated beside it.
- **Three letter-deviations and one scope reading were found in the work as run and are declared
  above rather than left silent** — the refused enumeration command, the scratchpad file, the
  working-tree byte read, and the `cc_report_*.md` pattern matching none of the existing session
  reports.
- **One defect in this report's own first writing was found and corrected before reporting:** the
  generating script was read by PowerShell 5.1 in the system ANSI code page, so every em-dash
  landed as mojibake. The prose is now held in UTF-8 fragments read with an explicit encoding, and
  the file was re-read at the object to confirm the characters are right.
- **No violation was found that could not be declared**, and no `OPEN_ITEMS.md` row was created,
  the dispatch barring one.
