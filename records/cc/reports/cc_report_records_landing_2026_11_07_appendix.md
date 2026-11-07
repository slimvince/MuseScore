# Appendix — the raw printouts of the records landing of 2026-11-07

Beside `records/cc/reports/cc_report_records_landing_2026_11_07.md`, under Ruling 4 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`. Every block below is a printout copied verbatim from the scratch file the command wrote, under a heading naming the command and the step. Nothing here is needed to read the report proper. The scratch scripts ran outside the repository with `python -I`; the 3(c′) run and Task 4's capture are not here — they are in this batch's section of `records/cowork/handoff/cowork_away_returns.md`.

## Start state, before Task 0 — `python tools/audit/gen_per_session_reading.py --check` (exit 2)

~~~~
STOP: a member of a derived population has no add-commit: records/cowork/handoff/cowork_handoff_entry_five_hundred.md
~~~~

## Start state, before Task 0 — `python tools/audit/gen_evidence_pin_membership.py --check` (exit 1)

~~~~
STALE vs the derivation: evidence_pin_membership.json does not re-derive
~~~~

## 0(c) / A1 — `python tools/audit/changed_paths.py` (exit 0), whole

~~~~
 M	docs/research_papers/BIBLIOGRAPHY.md
 M	docs/research_papers/README.md
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	ratification_surfaces/cowork_l3_cadence_type_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_catalog_further_rows_surface_2026_11_06.md
??	ratification_surfaces/cowork_l3_catalog_idiom_tags_part1_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_catalog_idiom_tags_part2_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_catalog_key_surface_2026_11_06.md
??	ratification_surfaces/cowork_l3_catalog_lead_rows_surface_2026_11_06.md
??	ratification_surfaces/cowork_l3_catalog_pairwise_grammar_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_catalog_recognition_part1_surface_2026_11_06.md
??	ratification_surfaces/cowork_l3_catalog_recognition_part2_surface_2026_11_06.md
??	ratification_surfaces/cowork_l3_catalog_substitution_part1_surface_2026_11_06.md
??	ratification_surfaces/cowork_l3_catalog_substitution_part2_surface_2026_11_06.md
??	ratification_surfaces/cowork_l3_catalog_suggestion_tool_and_cadential_entries_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_code_interfaces_family_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_decomposition_rules_family_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_display_family_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_fit_and_rest_second_cut_surface_2026_11_04.md
??	ratification_surfaces/cowork_l3_fit_and_rest_surface_2026_11_04.md
??	ratification_surfaces/cowork_l3_fit_and_rest_third_cut_surface_2026_11_04.md
??	ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_modal_counts_family_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_presets_scope_family_surface_2026_11_07.md
??	ratification_surfaces/cowork_l3_s38_eighth_cut_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_s38_fifth_cut_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_s38_first_cut_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_s38_fourth_cut_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_s38_ratification_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_s38_second_cut_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_s38_seventh_cut_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_s38_sixth_cut_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_s38_third_cut_surface_2026_11_03.md
??	ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md
??	ratification_surfaces/cowork_l3_tier3_display_surface_2026_11_04.md
??	ratification_surfaces/cowork_l3_tier3_literature_facts_surface_2026_11_04.md
??	ratification_surfaces/cowork_l3_tier3_span_kinds_surface_2026_11_04.md
??	ratification_surfaces/cowork_l3_unplaced_families_2026_11_06.md
??	ratification_surfaces/cowork_l3_unplaced_inventory_2026_11_04.md
??	ratification_surfaces/cowork_llm_correction_scope_2026_11_07.md
??	records/cc/instructions/cc_instruction_records_landing_2026_11_07.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eight.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eighteen.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eleven.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifteen.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_eight.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_five.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_four.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_nine.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_one.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_seven.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_six.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_three.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_two.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_five.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_eight.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_five.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_four.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_nine.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_one.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_seven.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_six.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_three.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_two.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_four.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fourteen.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_nine.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_nineteen.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_one.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seven.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventeen.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_six.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixteen.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_eight.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_five.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_four.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_nine.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_one.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_seven.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_six.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_three.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_two.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_ten.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirteen.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_eight.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_five.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_four.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_nine.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_one.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_seven.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_six.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_three.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_two.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_three.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twelve.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_eight.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_five.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_four.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_nine.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_one.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_seven.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_six.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_three.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_two.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_two.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_eight.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_five.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_four.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_nine.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_one.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_seven.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_six.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_three.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_two.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_eight.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_five.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_four.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_nine.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_one.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_seven.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_six.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_three.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_two.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_nine.md
??	records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_02_l3_route_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_vocabulary_point_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_key_areas_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_03_research_registry_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_04_l3_literature_facts_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_key_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_l3_code_interfaces_family_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_l3_display_family_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_l3_modal_counts_family_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md
??	records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md
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
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
571 changed path record(s) [worktree]
~~~~

## 0(c) — the count script, quoted whole: `landing_set_check.py`

~~~~
"""0(c): prove the landing set against changed_paths.py's enumeration.

Reads the enumeration saved by `python tools/audit/changed_paths.py` (argv[1]),
maps each untracked handoff-entry name to its number, compares the rulings and
ratification-document populations with the dispatch's lists name by name, and
writes the landing set (one path per line) to argv[2].
"""
import sys

ENUM, OUT = sys.argv[1], sys.argv[2]

UNITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
         "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
         "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
         "nineteen": 19}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90}


def words_to_int(s):
    parts = s.split("_")
    if len(parts) < 2 or parts[1] != "hundred" or parts[0] not in UNITS:
        raise ValueError("unparsed: " + s)
    n = UNITS[parts[0]] * 100
    rest = parts[2:]
    if not rest:
        return n
    if rest[0] != "and":
        raise ValueError("unparsed: " + s)
    rest = rest[1:]
    if len(rest) == 1:
        w = rest[0]
        if w in UNITS:
            return n + UNITS[w]
        if w in TENS:
            return n + TENS[w]
        raise ValueError("unparsed: " + s)
    if len(rest) == 2 and rest[0] in TENS and rest[1] in UNITS and UNITS[rest[1]] < 10:
        return n + TENS[rest[0]] + UNITS[rest[1]]
    raise ValueError("unparsed: " + s)


RULINGS = """cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md
cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md
cowork_rulings_2026_11_02_l3_phrase_units_sitting.md
cowork_rulings_2026_11_02_l3_route_sitting.md
cowork_rulings_2026_11_03_l3_boundaries_sitting.md
cowork_rulings_2026_11_03_l3_cadence_features_sitting.md
cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md
cowork_rulings_2026_11_03_l3_cadence_type_sitting.md
cowork_rulings_2026_11_03_l3_cadence_vocabulary_point_sitting.md
cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md
cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md
cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md
cowork_rulings_2026_11_03_l3_figured_bass_sitting.md
cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md
cowork_rulings_2026_11_03_l3_key_areas_sitting.md
cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md
cowork_rulings_2026_11_03_l3_pivot_label_sitting.md
cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md
cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md
cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md
cowork_rulings_2026_11_03_l3_sections_sitting.md
cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md
cowork_rulings_2026_11_03_research_registry_sitting.md
cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md
cowork_rulings_2026_11_04_l3_display_sitting.md
cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md
cowork_rulings_2026_11_04_l3_literature_facts_sitting.md
cowork_rulings_2026_11_04_l3_span_kinds_sitting.md
cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md
cowork_rulings_2026_11_06_l3_catalog_key_sitting.md
cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md
cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md
cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md
cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md
cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md
cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md
cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting.md
cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md
cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md
cowork_rulings_2026_11_07_l3_code_interfaces_family_sitting.md
cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md
cowork_rulings_2026_11_07_l3_display_family_sitting.md
cowork_rulings_2026_11_07_l3_modal_counts_family_sitting.md
cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md
cowork_rulings_2026_11_07_llm_correction_sitting.md
cowork_rulings_2026_11_07_llm_test_only_sitting.md""".split()

SURFACES = """cowork_l3_cadence_type_surface_2026_11_03.md
cowork_l3_catalog_further_rows_surface_2026_11_06.md
cowork_l3_catalog_idiom_tags_part1_surface_2026_11_07.md
cowork_l3_catalog_idiom_tags_part2_surface_2026_11_07.md
cowork_l3_catalog_key_surface_2026_11_06.md
cowork_l3_catalog_lead_rows_surface_2026_11_06.md
cowork_l3_catalog_pairwise_grammar_surface_2026_11_07.md
cowork_l3_catalog_recognition_part1_surface_2026_11_06.md
cowork_l3_catalog_recognition_part2_surface_2026_11_06.md
cowork_l3_catalog_substitution_part1_surface_2026_11_06.md
cowork_l3_catalog_substitution_part2_surface_2026_11_06.md
cowork_l3_catalog_suggestion_tool_and_cadential_entries_surface_2026_11_07.md
cowork_l3_code_interfaces_family_surface_2026_11_07.md
cowork_l3_decomposition_rules_family_surface_2026_11_07.md
cowork_l3_display_family_surface_2026_11_07.md
cowork_l3_fit_and_rest_surface_2026_11_04.md
cowork_l3_fit_and_rest_second_cut_surface_2026_11_04.md
cowork_l3_fit_and_rest_third_cut_surface_2026_11_04.md
cowork_l3_language_model_family_surface_2026_11_07.md
cowork_l3_modal_counts_family_surface_2026_11_07.md
cowork_l3_presets_scope_family_surface_2026_11_07.md
cowork_l3_s38_first_cut_surface_2026_11_03.md
cowork_l3_s38_second_cut_surface_2026_11_03.md
cowork_l3_s38_third_cut_surface_2026_11_03.md
cowork_l3_s38_fourth_cut_surface_2026_11_03.md
cowork_l3_s38_fifth_cut_surface_2026_11_03.md
cowork_l3_s38_sixth_cut_surface_2026_11_03.md
cowork_l3_s38_seventh_cut_surface_2026_11_03.md
cowork_l3_s38_eighth_cut_surface_2026_11_03.md
cowork_l3_s38_ratification_surface_2026_11_03.md
cowork_l3_tier3_architecture_rules_surface_2026_11_04.md
cowork_l3_tier3_display_surface_2026_11_04.md
cowork_l3_tier3_literature_facts_surface_2026_11_04.md
cowork_l3_tier3_span_kinds_surface_2026_11_04.md
cowork_l3_unplaced_families_2026_11_06.md
cowork_l3_unplaced_inventory_2026_11_04.md
cowork_llm_correction_scope_2026_11_07.md""".split()

DISPATCH = "records/cc/instructions/cc_instruction_records_landing_2026_11_07.md"
HO = "records/cowork/handoff/"
RU = "records/cowork/rulings/"
RS = "ratification_surfaces/"
FOLDERS = (HO, RU, RS, "records/cc/instructions/")

modified, untracked = [], []
with open(ENUM, encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        if "\t" not in line:
            continue
        status, path = line.split("\t", 1)
        if status.strip() == "??":
            untracked.append(path)
        else:
            modified.append((status.strip(), path))

print("tracked modifications (%d):" % len(modified))
for s, p in modified:
    print("  %s %s" % (s, p))

ok = True
# (i) handoff entries
nums = {}
for p in untracked:
    if p.startswith(HO + "cowork_handoff_entry_") and p.endswith(".md"):
        w = p[len(HO + "cowork_handoff_entry_"):-3]
        n = words_to_int(w)
        if n in nums:
            print("DUPLICATE number %d: %s and %s" % (n, nums[n], p)); ok = False
        nums[n] = p
got = sorted(nums)
print("handoff entries untracked: %d, numbers %d..%d" % (len(got), got[0], got[-1]))
expected_a = list(range(479, 569))
expected_b = list(range(479, 570))
if got == expected_b:
    print("handoff numbers: EXACTLY 479..569, each once (91)")
elif got == expected_a:
    print("handoff numbers: EXACTLY 479..568, each once (90)")
else:
    print("handoff numbers: MISMATCH missing=%s extra=%s" % (
        sorted(set(expected_b) - set(got)), sorted(set(got) - set(expected_b)))); ok = False

# (ii) rulings
ru_untracked = sorted(p[len(RU):] for p in untracked if p.startswith(RU))
print("ruling records listed: %d (distinct %d); untracked in folder: %d" % (
    len(RULINGS), len(set(RULINGS)), len(ru_untracked)))
miss = sorted(set(RULINGS) - set(ru_untracked)); extra = sorted(set(ru_untracked) - set(RULINGS))
print("  listed-not-untracked: %s" % miss); print("  untracked-not-listed: %s" % extra)
ok = ok and not miss and not extra and len(set(RULINGS)) == 46

# (iii) surfaces
rs_untracked = sorted(p[len(RS):] for p in untracked if p.startswith(RS))
print("ratification documents listed: %d (distinct %d); untracked in folder: %d" % (
    len(SURFACES), len(set(SURFACES)), len(rs_untracked)))
miss = sorted(set(SURFACES) - set(rs_untracked)); extra = sorted(set(rs_untracked) - set(SURFACES))
print("  listed-not-untracked: %s" % miss); print("  untracked-not-listed: %s" % extra)
ok = ok and not miss and not extra and len(set(SURFACES)) == 37

# (iv) dispatch, and the cc instructions folder
ci_untracked = sorted(p for p in untracked if p.startswith("records/cc/instructions/"))
print("records/cc/instructions untracked: %s" % ci_untracked)
ok = ok and ci_untracked == [DISPATCH]

# any untracked path in the four folders outside the landing set
landing = [nums[n] for n in got] + [RU + r for r in sorted(RULINGS)] + \
          [RS + s for s in sorted(SURFACES)] + [DISPATCH]
lset = set(landing)
stray = [p for p in untracked if p.startswith(FOLDERS) and p not in lset]
print("untracked in the four folders outside the landing set: %s" % stray)
ok = ok and not stray
others = [p for p in untracked if not p.startswith(FOLDERS)]
print("other untracked paths (standing population, not landed): %d" % len(others))
print("landing set size: %d" % len(landing))
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    for p in landing:
        f.write(p + "\n")
print("RESULT: %s" % ("PASS" if ok else "FAIL"))
~~~~

## 0(c) — `python -I landing_set_check.py a1_enumeration.txt landing_paths.txt` (exit 0), output

~~~~
tracked modifications (3):
  M docs/research_papers/BIBLIOGRAPHY.md
  M docs/research_papers/README.md
  M tools/audit/claude_md_finer_archive.json
handoff entries untracked: 91, numbers 479..569
handoff numbers: EXACTLY 479..569, each once (91)
ruling records listed: 46 (distinct 46); untracked in folder: 46
  listed-not-untracked: []
  untracked-not-listed: []
ratification documents listed: 37 (distinct 37); untracked in folder: 37
  listed-not-untracked: []
  untracked-not-listed: []
records/cc/instructions untracked: ['records/cc/instructions/cc_instruction_records_landing_2026_11_07.md']
untracked in the four folders outside the landing set: []
other untracked paths (standing population, not landed): 393
landing set size: 175
RESULT: PASS
~~~~

## 0(d) — the last-bytes script, quoted whole: `last_bytes_check.py`

~~~~
"""0(d): each landing file's blob, written --no-filters; size, last 70 bytes, zero-byte count.

argv[1] = repository root; argv[2] = file of landing paths (one per line).
Each blob is written with `git hash-object -w --no-filters` and then read back
from the object store with `git cat-file blob <hash>`; nothing is read from the
working tree by this script except through git's own hash-object.
"""
import subprocess
import sys

ROOT, LIST = sys.argv[1], sys.argv[2]
paths = [l.rstrip("\n") for l in open(LIST, encoding="utf-8") if l.strip()]
bad = []
for p in paths:
    h = subprocess.run(["git", "hash-object", "-w", "--no-filters", p], cwd=ROOT,
                       capture_output=True, text=True, check=True).stdout.strip()
    data = subprocess.run(["git", "cat-file", "blob", h], cwd=ROOT,
                          capture_output=True, check=True).stdout
    size = len(data)
    zeros = data.count(b"\x00")
    tail = data[-70:]
    ends_nl = data.endswith(b"\n")
    # the final line (before the closing newline) must be a complete line
    last_line = data.rstrip(b"\n").rsplit(b"\n", 1)[-1]
    status = "OK"
    if zeros or not ends_nl:
        status = "FAIL"
        bad.append(p)
    print("%s\t%s\t%d\tzeros=%d\tends_newline=%s\t%s" % (status, h, size, zeros, ends_nl, p))
    print("    last70=%r" % tail)
    print("    last_line_tail=%r" % last_line[-70:])
print("files: %d; failing: %d %s" % (len(paths), len(bad), bad))
~~~~

## 0(d) — `python -I last_bytes_check.py /c/s/MS landing_paths.txt` (exit 0), output: every file's blob, size, zero-byte count, last 70 bytes and final-line tail

~~~~
OK	a4f7f07df5e34374868dc6aadb39c09b3255d5fd	5787	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_nine.md
    last70=b'78. The user\'s words: the opening instruction;\n"narrow"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue".*'
OK	3567fa7cb5718de81251630fc676a02f8c98252d	5755	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty.md
    last70=b'rds: the opening instruction;\n"narrow"; "continue"; "continue"; "A".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue"; "A".*'
OK	67f2e6c2875e2ef6df777cdbc2000820ae1c4ab6	7686	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_one.md
    last70=b'words: the opening instruction;\n"full read"; "continue"; "continue".*\n'
    last_line_tail=b'"full read"; "continue"; "continue".*'
OK	9c85ebb8c8beacc9bb09d102da99b71a85d0d07a	5037	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_two.md
    last70=b'ruction;\n"narrowed"; "continue"; "continue"; "A"; "continue"; "yes".*\n'
    last_line_tail=b'"narrowed"; "continue"; "continue"; "A"; "continue"; "yes".*'
OK	3a42443b2529769c15a642ba22604ae3a793d84d	5221	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_three.md
    last70=b'l read"; "continue"; "continue"; "continue"; "A"; "yes"; "continue".*\n'
    last_line_tail=b'll read"; "continue"; "continue"; "continue"; "A"; "yes"; "continue".*'
OK	3a23a6766e0e5726eb21e06f5413e103ecebf807	5450	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_four.md
    last70=b'ruction;\n"continue"; "continue"; "continue"; "A"; "yes"; "continue".*\n'
    last_line_tail=b'"continue"; "continue"; "continue"; "A"; "yes"; "continue".*'
OK	71d9de733e0fd9efac956fb227f2ab14da94f8bb	6124	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_five.md
    last70=b'inue"; "continue"; "continue"; "yes"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'tinue"; "continue"; "continue"; "yes"; "continue"; "yes"; "continue".*'
OK	1c5d5e573d1156869ce417d1f7a2230955b787e5	5966	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_six.md
    last70=b' words: the opening instruction;\n"continue"; "continue"; "continue".*\n'
    last_line_tail=b'"continue"; "continue"; "continue".*'
OK	c51893874a2d1023d76812aa04d65376e6cdab2f	5569	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_seven.md
    last70=b'"; "A"; "continue"; "None principal"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'e"; "A"; "continue"; "None principal"; "continue"; "yes"; "continue".*'
OK	58e608815b9e7cedb72593edf6924e1e393fd0d3	5710	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_eight.md
    last70=b'ng instruction;\n"continue"; "continue"; "yes, ratified"; "continue".*\n'
    last_line_tail=b'"continue"; "continue"; "yes, ratified"; "continue".*'
OK	9a77a2a32ae10d309c79f71a58968a539774067d	5263	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_nine.md
    last70=b' words: the opening instruction;\n"continue"; "ratified"; "continue".*\n'
    last_line_tail=b'"continue"; "ratified"; "continue".*'
OK	6be1cdb039d690524be0db50856268f373646ec9	5608	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety.md
    last70=b' words: the opening instruction;\n"continue"; "continue"; "ratified".*\n'
    last_line_tail=b'"continue"; "continue"; "ratified".*'
OK	b511491bb1d01d998abdb817d4f1b6cbc1ff1499	5604	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_one.md
    last70=b'on entry 490. The user\'s words: the opening instruction;\n"continue".*\n'
    last_line_tail=b'"continue".*'
OK	7dd5715c2e8bd7ddc9beeec3a4e9d8e37389d662	8039	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_two.md
    last70=b'; "Continue (and I assume the BIBLIOGRAPHY.md needs to be updated)".*\n'
    last_line_tail=b'"; "Continue (and I assume the BIBLIOGRAPHY.md needs to be updated)".*'
OK	8a9f8fa068a3bf1f75b9fe07ea0b659f20c43a41	8682	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_three.md
    last70=b' the registry; "continue"; "continue"; "D"; the registry\'s location.*\n'
    last_line_tail=b'n the registry; "continue"; "continue"; "D"; the registry\'s location.*'
OK	c62540f665e97af402848f3e8d9946c30f423c3c	6577	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_four.md
    last70=b'on entry 493. The user\'s words: the opening instruction;\n"continue".*\n'
    last_line_tail=b'"continue".*'
OK	e3c096489c057f67d1edc6e54e7586599ba37e7f	8081	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_five.md
    last70=b'can read\nother languages than japanese? Fix it!"; "yes"; "continue".*\n'
    last_line_tail=b'other languages than japanese? Fix it!"; "yes"; "continue".*'
OK	cd953083d1507b1adadeaf1d2fcf16abe5bc1f19	6856	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_six.md
    last70=b'y 495. The user\'s words: the opening instruction;\n"yes"; "yes"; "A".*\n'
    last_line_tail=b'"yes"; "yes"; "A".*'
OK	2b247c5e93b79b49dd538005c5dbf080fbcbced8	6129	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_seven.md
    last70=b';\n"yes"; "continue"; "continue"; "continue"; "ratified"; "continue".*\n'
    last_line_tail=b'"yes"; "continue"; "continue"; "continue"; "ratified"; "continue".*'
OK	bf204e2e5b7b51d10549ab8fa8e8a57c782d284a	6006	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_eight.md
    last70=b'uestion on the local PDF; "continue"; "continue";\n"yes"; "yes"; "A".*\n'
    last_line_tail=b'"yes"; "yes"; "A".*'
OK	120b0e88595ea039a59f3e9d8114aa31c2f67b27	6346	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_nine.md
    last70=b'; "yes"; "continue"; "continue"; "continue"; "yes"; "continue"; "A".*\n'
    last_line_tail=b'"; "yes"; "continue"; "continue"; "continue"; "yes"; "continue"; "A".*'
OK	44c4cbd7205384c5bd88e5c20bb4763d8463ca02	6229	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred.md
    last70=b'inue"; "yes"; "continue"; "continue"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'tinue"; "yes"; "continue"; "continue"; "continue"; "yes"; "continue".*'
OK	190d0ed8faf989353ec194f5135f7109e15bdee6	6035	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_one.md
    last70=b'"; "continue"; "B"; "continue"; "continue"; "continue"; "confirmed".*\n'
    last_line_tail=b'e"; "continue"; "B"; "continue"; "continue"; "continue"; "confirmed".*'
OK	b1a0550f70e156252711520a76f71bf08f701d2c	5356	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_two.md
    last70=b'ough this far"; "continue"; "continue"; "A (narrowly?)"; "continue".*\n'
    last_line_tail=b'nough this far"; "continue"; "continue"; "A (narrowly?)"; "continue".*'
OK	e46a1d077024bfb5b8eabbe72d3c1a137d32ec11	5949	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_three.md
    last70=b' the publish everything principle)."; "continue"; "yes";\n"continue".*\n'
    last_line_tail=b'"continue".*'
OK	f3b5734d85909dea4cd7df59762d084dae5ae7a9	5723	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_four.md
    last70=b'rrow"; "continue"; "continue"; "yes"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'arrow"; "continue"; "continue"; "yes"; "continue"; "yes"; "continue".*'
OK	3efa2b299227698616166a2cd503357c785b805a	8542	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_five.md
    last70=b'04. The user\'s words: the opening instruction;\n"narrow"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue".*'
OK	d952f2597dc42a77524a38d956945e8668b53e27	5709	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_six.md
    last70=b'\'s words: the opening instruction;\n"narrow"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue".*'
OK	2e5d74de7f3b94b71079938276b3c7bb94146b83	6980	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seven.md
    last70=b'ning instruction;\n"narrow"; "continue"; "a"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "a"; "continue"; "continue".*'
OK	b9b7e1e1d16a0b9bcdb18e8bdc2deaef35bbd1a7	5815	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eight.md
    last70=b'\'s words: the opening instruction;\n"narrow"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue".*'
OK	83358e1a083c9f0462fc49be21097e58d9e77ebd	5796	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_nine.md
    last70=b'tion;\n"narrow"; "continue"; "A"; "continue"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "A"; "continue"; "continue"; "continue".*'
OK	565097fd203ee0450dbe95c40441f593d471c80a	5930	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_ten.md
    last70=b'ruction;\n"continue"; "continue"; "continue"; "continue"; "continue".*\n'
    last_line_tail=b'"continue"; "continue"; "continue"; "continue"; "continue".*'
OK	20e22ba17e33289838eb4150b275efd2bc3924e7	5810	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eleven.md
    last70=b'e opening instruction;\n"narrow"; "continue"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue"; "continue".*'
OK	7fd40b066ec1f20182461ed232a97cfbd3d79c1c	5693	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twelve.md
    last70=b'truction;\n"narrow as last time"; "continue"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow as last time"; "continue"; "continue"; "continue".*'
OK	34cf14dd72b2700c396ae67bf76efda64add346d	6083	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirteen.md
    last70=b'instruction;\n"narrow as BEFORE"; "continue"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow as BEFORE"; "continue"; "continue"; "continue".*'
OK	0166ea38d4dc492759b76faf77129c93b406e269	5874	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fourteen.md
    last70=b'\'s words: the opening instruction;\n"narrow"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue".*'
OK	07f20e09d5a43e6c859d64a1d6ed365f7a9b3a9b	4793	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifteen.md
    last70=b'instruction;\n"narrowest"; "continue"; "continue"; "continue"; "yes".*\n'
    last_line_tail=b'"narrowest"; "continue"; "continue"; "continue"; "yes".*'
OK	e5d5c49067e869833fc1219e8bd5f2936d7e477b	7174	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixteen.md
    last70=b' opening instruction;\n"narrow"; "contionue"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "contionue"; "continue"; "continue".*'
OK	1643a90a39a65e788e6a33f5ca18506fbdb5540b	6063	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventeen.md
    last70=b' words: the opening instruction;\n"narrowed"; "continue"; "continue".*\n'
    last_line_tail=b'"narrowed"; "continue"; "continue".*'
OK	2b593016ddfceab364b62acc0a15715af3cdccf5	5476	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eighteen.md
    last70=b'struction;\n"narrow"; "continue"; "continue"; "ratified"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue"; "ratified"; "continue".*'
OK	60c671d7de67767b3ea3f0f801b7629c8ae71715	5383	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_nineteen.md
    last70=b'ng instruction;\n"narrow"; "continue"; "continue"; "continue"; "yes".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue"; "continue"; "yes".*'
OK	06e9c16451f2004bbf02ff5b07bc8477d09ddae2	5787	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty.md
    last70=b'on;\n"narrowed"; "continue"; "continue"; "ratify a to c"; "continue".*\n'
    last_line_tail=b'"narrowed"; "continue"; "continue"; "ratify a to c"; "continue".*'
OK	f710baa949f4f6e93dd6eeed6c3622e48e4a14c3	5676	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_one.md
    last70=b'ing instruction;\n"narrowed"; "continue"; "continue"; "yes"; "agree".*\n'
    last_line_tail=b'"narrowed"; "continue"; "continue"; "yes"; "agree".*'
OK	57b697a7d431a2b352e73e55718099351352d561	6354	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_two.md
    last70=b'ng instruction;\n"narrow"; "continue"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue"; "yes"; "continue".*'
OK	5c332a8f6b30675016646b768b928a73d9965b04	6884	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_three.md
    last70=b'e opening instruction;\n"narrow"; "continue"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue"; "continue".*'
OK	134c86d3592e62faec2a6149e51f256faf91d38f	6424	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_four.md
    last70=b'23. The user\'s words: the opening instruction;\n"narrow"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue".*'
OK	10a5e01090fd91121d0424d762de7815dc72072e	6455	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_five.md
    last70=b'4. The user\'s words: the opening instruction;\n"shorter"; "continue".*\n'
    last_line_tail=b'"shorter"; "continue".*'
OK	a4d191e00e498b01c13e6e3452c4c2be242a1d7d	6169	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_six.md
    last70=b'5. The user\'s words: the opening instruction;\n"shorter"; "continue".*\n'
    last_line_tail=b'"shorter"; "continue".*'
OK	b3d273188b7b3b0f2eff6ca4fe424c8a4c101235	6029	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_seven.md
    last70=b'\'s words: the opening instruction;\n"narrow"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue".*'
OK	f51015ee33aa5915f0ee271a77a73dcb6e386f18	6229	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_eight.md
    last70=b'27. The user\'s words: the opening instruction;\n"narrow"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue".*'
OK	4dddae06945c094fcac8f914eb76ec8b7d849d4c	6017	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_nine.md
    last70=b'\'s words: the opening instruction;\n"narrow"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue".*'
OK	1f62dfa7d4c7a6fb068f9c71d3db01c6c29771ae	5192	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty.md
    last70=b'\'s words: the opening instruction;\n"narrow"; "continue"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue".*'
OK	eb26511d2cf3e801b803b177d1717a44d00bcd9d	4746	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_one.md
    last70=b'30. The user\'s words: the opening instruction;\n"narrow"; "continue".*\n'
    last_line_tail=b'"narrow"; "continue".*'
OK	bd2006fc7c90ef74f1c347ea8de8a5c5e6d109cc	4781	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_two.md
    last70=b'31. The user\'s words: the opening\ninstruction; "narrow"; "continue".*\n'
    last_line_tail=b'instruction; "narrow"; "continue".*'
OK	5116c143a4f1b28165cbb259afeb6ac6ccb41db7	5593	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_three.md
    last70=b' 532. The user\'s words: the opening\ninstruction; "narroe"; "resume".*\n'
    last_line_tail=b'instruction; "narroe"; "resume".*'
OK	cdbafc2afb616c3aa752b1f0b3f1e2c7a2c11af0	5490	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_four.md
    last70=b'33. The user\'s words: the opening\ninstruction; "narrow"; "continue".*\n'
    last_line_tail=b'instruction; "narrow"; "continue".*'
OK	ed2dfa73ea2db02547124ba89c59091aaccc4678	5007	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_five.md
    last70=b'34. The user\'s words: the opening\ninstruction; "narrow"; "continue".*\n'
    last_line_tail=b'instruction; "narrow"; "continue".*'
OK	7477d799f28cfe51c3ca43ff035852b2be4d7add	5760	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_six.md
    last70=b'5. The user\'s words: the opening\ninstruction; "shorten"; "continue".*\n'
    last_line_tail=b'instruction; "shorten"; "continue".*'
OK	a1ebda18a906bcc458534c9781063d09cd81a6c4	5597	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_seven.md
    last70=b'6. The user\'s words: the opening\ninstruction; "shorten"; "continue".*\n'
    last_line_tail=b'instruction; "shorten"; "continue".*'
OK	edc7e7dcefc66b494287d7f31bc4b88478baf93d	6306	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_eight.md
    last70=b'words: the opening\ninstruction; "shortened"; "continue"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue".*'
OK	6323bc24d6d7442b0acb8460967a36b678eade5a	7015	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_nine.md
    last70=b'rface\'s \xc2\xa78; "continue"; the three points quoted at \xc2\xa79;\n"continue".*\n'
    last_line_tail=b'"continue".*'
OK	adb7a8f124a6929b753179d588e14b1e8ba3e80c	6196	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty.md
    last70=b' 539. The user\'s words: the opening\ninstruction; "full"; "continue".*\n'
    last_line_tail=b'instruction; "full"; "continue".*'
OK	a6d549be44cfd2aac76b57fee199dfeeb99d664c	6810	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_one.md
    last70=b'tion; "shortened"; "continue"; "continue"; "yes"; "yes"; "continue".*\n'
    last_line_tail=b'ction; "shortened"; "continue"; "continue"; "yes"; "yes"; "continue".*'
OK	6e49120e8a475f9a0758abab80c7dfbd8e8937f6	6052	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_two.md
    last70=b'he opening\ninstruction; "shortened" (twice); "continue"; "continue".*\n'
    last_line_tail=b'instruction; "shortened" (twice); "continue"; "continue".*'
OK	a49f2210ec0d44b8272ff2cbc3ca8d53735a6f9d	5795	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_three.md
    last70=b'words: the opening\ninstruction; "shortened"; "ratified"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "ratified"; "continue".*'
OK	ee4454abbdc8d670ab4ab2fd5fad2c9ec04a9ff7	6825	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_four.md
    last70=b' "shortened"; "continue"; "continue"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'; "shortened"; "continue"; "continue"; "continue"; "yes"; "continue".*'
OK	b16c206ddc4413275b023ed2ddf0d5e442bcbd5e	6793	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_five.md
    last70=b'ing\ninstruction; "short"; "continue"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'instruction; "short"; "continue"; "continue"; "yes"; "continue".*'
OK	4e4d8ce6e81889a4b8a0dc73783ba456e3d01b01	6974	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_six.md
    last70=b' "shortened"; "continue"; "continue"; "yes"; "continue"; "continue".*\n'
    last_line_tail=b'; "shortened"; "continue"; "continue"; "yes"; "continue"; "continue".*'
OK	1f6bf1618a9513be147826fb5fffa269bba2760b	8341	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_seven.md
    last70=b'er\'s words: the opening\ninstruction; "full"; "continue"; "continue".*\n'
    last_line_tail=b'instruction; "full"; "continue"; "continue".*'
OK	9ca3c0561f9cf57e713a63ffb8153ff1a09959e9	7226	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_eight.md
    last70=b'; "continue"; "continue"; "continue"; "yes"; "continue"; "continue".*\n'
    last_line_tail=b'"; "continue"; "continue"; "continue"; "yes"; "continue"; "continue".*'
OK	99eb835ca96d5087967d8a5d9645bf82fb369f8c	6938	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_nine.md
    last70=b'instruction; "shortened"; "continue"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue"; "yes"; "continue".*'
OK	834d77250bf67d488ae5338bde65f1061fcf6d08	7698	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty.md
    last70=b'rds: the opening\ninstruction; "shortened"; "start test"; "Continue".*\n'
    last_line_tail=b'instruction; "shortened"; "start test"; "Continue".*'
OK	8f43272e238f3e771c49de6ea04137a93d9b7765	5607	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_one.md
    last70=b'rterned"; "continue"; "continue"; the thought on labels; "ratified".*\n'
    last_line_tail=b'orterned"; "continue"; "continue"; the thought on labels; "ratified".*'
OK	b4abe953ce8cbfb3f3c19b53c2810cc21e8c17f2	5495	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_two.md
    last70=b'instruction; "shortened"; "continue"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue"; "yes"; "continue".*'
OK	fe213e6f1599ee422f3ad981e9b6890c37c7164a	6428	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_three.md
    last70=b' "shortened"; "continue"; "continue"; "continue"; "yes"; "continue".*\n'
    last_line_tail=b'; "shortened"; "continue"; "continue"; "continue"; "yes"; "continue".*'
OK	76777103dc97552519cf628ca49e91d6a12a3d4f	6213	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_four.md
    last70=b'uction; "shortened"; "continue"; "continue"; "continue"; "continue".*\n'
    last_line_tail=b'ruction; "shortened"; "continue"; "continue"; "continue"; "continue".*'
OK	20ccb1a81fc2d23660a85b3e0fa8693ea04e5cac	5836	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_five.md
    last70=b'pening\ninstruction; "shortened"; "continue"; "C"; "yes"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "C"; "yes"; "continue".*'
OK	d62f5220fe8b687d65f6a912f127e88bde055a92	5859	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_six.md
    last70=b'instruction; "shortened"; "continue"; "continue"; "continue"; "yes".*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue"; "continue"; "yes".*'
OK	96f7e12f92d1d67fb6cae7de72e5d83a27b72941	5924	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_seven.md
    last70=b'pening\ninstruction; "shortened"; "continue"; "continue"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue"; "continue".*'
OK	2aa57cddcfab8e222380af7bc73c58b8a15bd77a	5314	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_eight.md
    last70=b'pening\ninstruction; "Shortened"; "continue"; "A"; "yes"; "continue".*\n'
    last_line_tail=b'instruction; "Shortened"; "continue"; "A"; "yes"; "continue".*'
OK	b85114440a56e9858b2548cc7f1f7338caf6a260	6059	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_nine.md
    last70=b'; "continue"; "continue"; "continue"; "Continue"; "Yes"; "Continue".*\n'
    last_line_tail=b'"; "continue"; "continue"; "continue"; "Continue"; "Yes"; "Continue".*'
OK	2631454730a54151c84c9552bb578e3e591542a9	5925	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty.md
    last70=b'pening\ninstruction; "shortened"; "continue"; "continue"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue"; "continue".*'
OK	511a43d573bfe42d0ea18a99db42e8f0c0d9d0f0	5896	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_one.md
    last70=b'he opening\ninstruction; "shortened"; "continueo"; "yes"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "continueo"; "yes"; "continue".*'
OK	a409988c168f0539dba62ed0e293f6974e07195e	6311	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_two.md
    last70=b'words: the opening\ninstruction; "shortened"; "continue"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue".*'
OK	f7b8e22088fee80bcb4198f7607c8002a02b1d29	7014	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_three.md
    last70=b' instruction quoted in the language-model ruling record; "continue".*\n'
    last_line_tail=b'e instruction quoted in the language-model ruling record; "continue".*'
OK	ab8e0efb5c518f8ffffb778869d3c47fca6c2c67	7473	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_four.md
    last70=b'er\'s words: the opening instruction;\n"shortened"; "continue"; "yes".*\n'
    last_line_tail=b'"shortened"; "continue"; "yes".*'
OK	b59663a7a69679e80f53ea8d06a5ada8bbf9253a	4991	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_five.md
    last70=b' The user\'s words: the opening instruction;\n"shortened"; "CONTINUE".*\n'
    last_line_tail=b'"shortened"; "CONTINUE".*'
OK	cecfd1e7c5f72dce4c21a1585817c9bfb550a88e	4552	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_six.md
    last70=b' The user\'s words: the opening instruction;\n"shortened"; "continue".*\n'
    last_line_tail=b'"shortened"; "continue".*'
OK	82dd84d677bfb625dc14685ac7bc6f029921f45c	5198	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_seven.md
    last70=b'pening instruction;\n"shortened"; "continue"; "continue"; "ratified".*\n'
    last_line_tail=b'"shortened"; "continue"; "continue"; "ratified".*'
OK	3971f5bea8d2eea23332380bb9abe9cf41f251e6	6874	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_eight.md
    last70=b' 567. The user\'s words: the opening instruction;\n"shortened"; "yes".*\n'
    last_line_tail=b'"shortened"; "yes".*'
OK	815b3b4b911076534d5be0d4abba560e0763d6c1	6642	zeros=0	ends_newline=True	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_nine.md
    last70=b'the opening instruction;\n"shortened"; "ok"; "run check"; "continue".*\n'
    last_line_tail=b'"shortened"; "ok"; "run check"; "continue".*'
OK	c3c29e8fd66022ad075fdccc8c52747d5a23f502	12277	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md
    last70=b'opening instruction; "continue"; "continue";\n"continue"; "A"; "yes".*\n'
    last_line_tail=b'"continue"; "A"; "yes".*'
OK	64ea3e43b46eadda1f07066d7a862f504281a3d4	12321	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md
    last70=b'ruction; "narrowed"; "continue";\n"continue"; "A"; "continue"; "yes".*\n'
    last_line_tail=b'"continue"; "A"; "continue"; "yes".*'
OK	a7e168d1b65b1ecaabc4fb40423fd1f82170a3b0	12428	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md
    last70=b'uction; "full read"; "continue";\n"continue"; "continue"; "A"; "yes".*\n'
    last_line_tail=b'"continue"; "continue"; "A"; "yes".*'
OK	ae3ec114f21d42f4aca7be8e1b395c2ac3261a25	9951	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_02_l3_route_sitting.md
    last70=b'rds: the opening instruction; "narrow"; "continue";\n"continue"; "A".*\n'
    last_line_tail=b'"continue"; "A".*'
OK	1f937e0f1da92c436a24ff86f389480bbdb766c4	12069	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md
    last70=b'ue" (Question (a) put); "yes"; "continue" (Question (b) put);\n"yes".*\n'
    last_line_tail=b'"yes".*'
OK	c0e1b49bc4b6d598d646b18c15dd70dfd9dc7813	12603	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md
    last70=b'ction; "continue"; "continue";\n"continue"; "yes"; "continue"; "yes".*\n'
    last_line_tail=b'"continue"; "yes"; "continue"; "yes".*'
OK	79e5e2e5552b7fe61294449cee961aace85151f3	7292	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md
    last70=b's: the opening instruction; "continue"; "continue"; "yes,\nratified".*\n'
    last_line_tail=b'ratified".*'
OK	d38ef735c0f4b9e98c94a0b9c428b1ec396a46ea	9376	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md
    last70=b'"; "continue"; "A"; "continue"; "None\nprincipal"; "continue"; "yes".*\n'
    last_line_tail=b'principal"; "continue"; "yes".*'
OK	fb274b225381dfb9dd3beb014bb11ed7e87428b6	6388	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_vocabulary_point_sitting.md
    last70=b' words: the opening instruction; "continue"; "continue";\n"ratified".*\n'
    last_line_tail=b'"ratified".*'
OK	b76f0f4dcffc691f56ed2a4fef9716923abc2482	6575	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md
    last70=b'. The user\'s words: the opening instruction; "continue"; "ratified".*\n'
    last_line_tail=b'). The user\'s words: the opening instruction; "continue"; "ratified".*'
OK	76f4a96b283343d06ed275fc732549f306181af8	11895	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md
    last70=b' "continue" (the check); "continue" (the question put); "confirmed".*\n'
    last_line_tail=b'; "continue" (the check); "continue" (the question put); "confirmed".*'
OK	be9fd6e59f2ae3f5eb173db058591d2042c34b79	8964	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md
    last70=b'face); "continue" (the check); "continue" (the question put); "yes".*\n'
    last_line_tail=b'rface); "continue" (the check); "continue" (the question put); "yes".*'
OK	42037bece11d892ac308f53c1d3d439d4ba930b9	10846	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md
    last70=b'urface); "continue" (the check); "continue" (the question put); "B".*\n'
    last_line_tail=b'surface); "continue" (the check); "continue" (the question put); "B".*'
OK	4cf648e04b348428bafa58c51058d2fa1e5ddb54	10955	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md
    last70=b'ntinue" (the check); "continue" (the question put); "A (narrowly?)".*\n'
    last_line_tail=b'ontinue" (the check); "continue" (the question put); "A (narrowly?)".*'
OK	41cdbef37a391a2227325be07fbc82a90fc97276	11601	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_key_areas_sitting.md
    last70=b'" (the check); "continue" (K1 put); "yes"; "continue" (K2 put); "A".*\n'
    last_line_tail=b'e" (the check); "continue" (K1 put); "yes"; "continue" (K2 put); "A".*'
OK	a6b6434b8651c3da8184b79cd8782c1d7fadf2be	13203	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md
    last70=b'publish everything\nprinciple)."; "continue" (Question 2 put); "yes".*\n'
    last_line_tail=b'principle)."; "continue" (Question 2 put); "yes".*'
OK	419bdd3f6c0d4eb1e66c194e50a9a083fb1f8843	10502	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md
    last70=b'face); "continue" (the check); "continue" (the question put); "yes".*\n'
    last_line_tail=b'rface); "continue" (the check); "continue" (the question put); "yes".*'
OK	55db2021c5d40ae489f0b05f93cc588f0c9396d3	6889	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md
    last70=b'ening\ninstruction; "narrow"; "continue"; "a" (Ruling 1); "continue".*\n'
    last_line_tail=b'instruction; "narrow"; "continue"; "a" (Ruling 1); "continue".*'
OK	643a81f3e8480c5a6fdeed12e2020746d24672ec	5897	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md
    last70=b'; "narrowest"; "continue"; "continue"; "continue"; "yes" (Ruling 1).*\n'
    last_line_tail=b'n; "narrowest"; "continue"; "continue"; "continue"; "yes" (Ruling 1).*'
OK	22f1a005f98c07fe188b77f3302dbf665cbf5ce7	7391	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md
    last70=b'rder: the opening\ninstruction; "narrow"; "continue"; "A" (Ruling 1).*\n'
    last_line_tail=b'instruction; "narrow"; "continue"; "A" (Ruling 1).*'
OK	f532025cafad1eab87ede1202921b186482c2f2e	20068	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md
    last70=b'rm is there\nin exposing such names?"; "continue"; "continue"; "yes".*\n'
    last_line_tail=b'in exposing such names?"; "continue"; "continue"; "yes".*'
OK	f475002114f81ad7a06522ed7cc248512b263f8f	10763	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md
    last70=b' instruction; "yes"; "continue";\n"continue"; "continue"; "ratified".*\n'
    last_line_tail=b'"continue"; "continue"; "ratified".*'
OK	44e74333c0ffbb7af1fc29f4419e2aa4a0783707	8927	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_03_research_registry_sitting.md
    last70=b'ot a ruling; restated); "D"; the registry\'s location, quoted in \xc2\xa71.*\n'
    last_line_tail=b'not a ruling; restated); "D"; the registry\'s location, quoted in \xc2\xa71.*'
OK	30aa85c7f982e0cc32f5e5846ae3ed891031f38f	7799	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md
    last70=b'owed"; "continue" (the check); "continue" (the question put); "yes".*\n'
    last_line_tail=b'rowed"; "continue" (the check); "continue" (the question put); "yes".*'
OK	7c083ce6ec7572c40464572bcf9d03e673ac3036	6101	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md
    last70=b'inue"; "continue" (the check); "continue" (the question put); "yes".*\n'
    last_line_tail=b'tinue"; "continue" (the check); "continue" (the question put); "yes".*'
OK	0f378545e156e73b5729d63e59045a947884bd3f	6293	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md
    last70=b'e opening instruction;\n"narrow"; "continue"; "continue"; "ratified".*\n'
    last_line_tail=b'"narrow"; "continue"; "continue"; "ratified".*'
OK	35f1696083ea9887f7c794b706ce2a70d076149c	6707	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_04_l3_literature_facts_sitting.md
    last70=b'rrow"; "continue" (the check); "continue" (the question put); "yes".*\n'
    last_line_tail=b'arrow"; "continue" (the check); "continue" (the question put); "yes".*'
OK	898e2dc278a251d26c434be2fcac466bee684aeb	6011	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md
    last70=b'ntinue" (the check); "continue" (the question put); "ratify a to c".*\n'
    last_line_tail=b'ontinue" (the check); "continue" (the question put); "ratify a to c".*'
OK	cd71cda104fda65f2a111742b50dc480154e7f85	8151	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md
    last70=b'tinue" (the check); "continue" (the question put); "yes" (Ruling 1).*\n'
    last_line_tail=b'ntinue" (the check); "continue" (the question put); "yes" (Ruling 1).*'
OK	78d1f65bc7bd6f12b925e64d005461e918bb8ac0	8881	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_key_sitting.md
    last70=b'tinue" (the first question put); "yes" (Ruling 1); "yes"\n(Ruling 2).*\n'
    last_line_tail=b'(Ruling 2).*'
OK	8a7d8b3b2f7f943ea68db80c65eb5d454e14c64f	5819	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md
    last70=b' words: the opening\ninstruction; "shortened"; "ratified" (Ruling 1).*\n'
    last_line_tail=b'instruction; "shortened"; "ratified" (Ruling 1).*'
OK	04cab0e5955e8b627f9e1719f6ee20012714bf76	7479	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md
    last70=b'tinue" (the check); "continue" (the question put); "yes" (Ruling 1).*\n'
    last_line_tail=b'ntinue" (the check); "continue" (the question put); "yes" (Ruling 1).*'
OK	95b0ac7bf07a8d5df9a0734b416b5ed1e4e1be61	8008	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md
    last70=b'tinue" (the check); "continue" (the question put); "yes" (Ruling 1).*\n'
    last_line_tail=b'ntinue" (the check); "continue" (the question put); "yes" (Ruling 1).*'
OK	d34e404d5c6bb9cfed87ff4e4709d3ce80bd0ddf	6881	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md
    last70=b'tinue" (the check); "continue" (the question put); "yes" (Ruling 1).*\n'
    last_line_tail=b'ntinue" (the check); "continue" (the question put); "yes" (Ruling 1).*'
OK	80539b387836b9b30fb75955a488011b771d72c0	6651	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md
    last70=b'tinue" (the check); "continue" (the question put); "yes" (Ruling 1).*\n'
    last_line_tail=b'ntinue" (the check); "continue" (the question put); "yes" (Ruling 1).*'
OK	4aa210c7eadfa68e54e58d36cc38e893274c690e	9010	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md
    last70=b'e question put); the thought on labels (\xc2\xa72);\n"ratified" (Ruling 1).*\n'
    last_line_tail=b'"ratified" (Ruling 1).*'
OK	6302aba69e770e1e4b1508cb0853dd02eb878d19	6479	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting.md
    last70=b'tinue" (the check); "continue" (the question put); "yes" (Ruling 1).*\n'
    last_line_tail=b'ntinue" (the check); "continue" (the question put); "yes" (Ruling 1).*'
OK	da3fc633cf60c7646e4ea81f1c489be36bf7d3e8	8180	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md
    last70=b'tinue" (the check); "continue" (the question put); "yes" (Ruling 1).*\n'
    last_line_tail=b'ntinue" (the check); "continue" (the question put); "yes" (Ruling 1).*'
OK	fa1f136b9d2f504db681d7a91620e9d5dccc8fbd	9543	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md
    last70=b'ntinue" (the choice question put); "C" (Ruling 1); "yes" (Ruling 2).*\n'
    last_line_tail=b'ontinue" (the choice question put); "C" (Ruling 1); "yes" (Ruling 2).*'
OK	1cc70068ebaf6cbd78ca93752f3292ad68ec8e9b	8381	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_l3_code_interfaces_family_sitting.md
    last70=b'words: the opening\ninstruction; "Shortened"; "continue"; "A"; "yes".*\n'
    last_line_tail=b'instruction; "Shortened"; "continue"; "A"; "yes".*'
OK	728a46d07ea9415f8f6bcda88018c2df67dd8e10	6316	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md
    last70=b'ortened"; "continueo" (read as "continue": the question put); "yes".*\n'
    last_line_tail=b'hortened"; "continueo" (read as "continue": the question put); "yes".*'
OK	ece876373bccafdecdf614767086c50151fcd08f	6063	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_l3_display_family_sitting.md
    last70=b'inue"; "continue" (the check); "continue" (the question put); "yes".*\n'
    last_line_tail=b'tinue"; "continue" (the check); "continue" (the question put); "yes".*'
OK	2456059642a52fb862fa1a17f6294ca14874712f	6592	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_l3_modal_counts_family_sitting.md
    last70=b' "Shortened"; "continue"; "continue"; "continue"; "Continue"; "Yes".*\n'
    last_line_tail=b'; "Shortened"; "continue"; "continue"; "continue"; "Continue"; "Yes".*'
OK	db73fb9b867115d518d07dfe0228697fa7aa0073	7264	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md
    last70=b' 562. The user\'s words: the opening\ninstruction; "shortened"; "yes".*\n'
    last_line_tail=b'instruction; "shortened"; "yes".*'
OK	97f065550defe443804afef2f1ca78495c5a0384	5001	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md
    last70=b'pening instruction;\n"shortened"; "continue"; "continue"; "ratified".*\n'
    last_line_tail=b'"shortened"; "continue"; "continue"; "ratified".*'
OK	e223a16d4a4d5d6de8ce079b12f8b319de6b6315	5626	zeros=0	ends_newline=True	records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md
    last70=b'; the three statements\nquoted in \xc2\xa71; the instruction quoted in \xc2\xa72.*\n'
    last_line_tail=b'quoted in \xc2\xa71; the instruction quoted in \xc2\xa72.*'
OK	8c5c62fa1d156618346b0bbf953d9f337e2dc0b9	13509	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_cadence_type_surface_2026_11_03.md
    last70=b' words: the opening instruction; "continue"; "continue";\n"continue".*\n'
    last_line_tail=b'"continue".*'
OK	ebf35d2fcad55e70ccf7db4b2a8f771650fb34a7	29862	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_further_rows_surface_2026_11_06.md
    last70=b'words: the opening\ninstruction; "shortened"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "shortened"; "continue" (the check).*'
OK	64aea070948ecb6a5f8ca89b69e776240ee2f312	28531	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_idiom_tags_part1_surface_2026_11_07.md
    last70=b'ords: the opening\ninstruction; "shorterned"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "shorterned"; "continue" (the check).*'
OK	2e575071650f9541bf4043f5e98b96c4246d5180	17836	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_idiom_tags_part2_surface_2026_11_07.md
    last70=b'words: the opening\ninstruction; "shortened"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "shortened"; "continue" (the check).*'
OK	a8b6b0405c1febabfd15fb01a1ecd3cb641a4290	50124	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_key_surface_2026_11_06.md
    last70=b' the user\'s words:\nthe opening instruction; "shortened"; "continue".*\n'
    last_line_tail=b'the opening instruction; "shortened"; "continue".*'
OK	d6fc2a0bd0c237d4c6cc2a1e20862fbd261a0a7c	19124	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_lead_rows_surface_2026_11_06.md
    last70=b'rds: the opening\ninstruction; "shortened" (twice); "continue" (\xc2\xa76).*\n'
    last_line_tail=b'instruction; "shortened" (twice); "continue" (\xc2\xa76).*'
OK	8ea43343a09b85e8f7e354daed4802d22a99a8f4	22016	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_pairwise_grammar_surface_2026_11_07.md
    last70=b'pening\ninstruction; "shortened"; "continue"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue" (the check).*'
OK	54f9556f0769d8a5bb29d6fb78654bfbb060e968	25432	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_recognition_part1_surface_2026_11_06.md
    last70=b'pening\ninstruction; "shortened"; "continue"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue" (the check).*'
OK	ecce70fc92c2578b0bb25ec099492dfcd90b0e69	29314	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_recognition_part2_surface_2026_11_06.md
    last70=b'r\'s words: the opening\ninstruction; "short"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "short"; "continue" (the check).*'
OK	974dbe6b7d6185afb3c0756b70644920e7c8ef7f	24818	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_substitution_part1_surface_2026_11_06.md
    last70=b'pening\ninstruction; "shortened"; "continue"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue" (the check).*'
OK	e6752c3697d23e46ffa4988c67774285d7dfe7f9	21048	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_substitution_part2_surface_2026_11_06.md
    last70=b'words: the opening\ninstruction; "shortened"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "shortened"; "continue" (the check).*'
OK	fcda2d2c4e947dfc1974c3b5a03240bf92cea25a	17952	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_catalog_suggestion_tool_and_cadential_entries_surface_2026_11_07.md
    last70=b'words: the opening\ninstruction; "shortened"; "continue"; "continue".*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue".*'
OK	768d1cdc569186fa49607617612792a334e98aa2	32931	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_code_interfaces_family_surface_2026_11_07.md
    last70=b'pening\ninstruction; "shortened"; "continue"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue" (the check).*'
OK	9b55672fad278f0be1353a15f68bee4879967c2d	27650	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_decomposition_rules_family_surface_2026_11_07.md
    last70=b'n entry 560; the user\'s words: the\nopening instruction; "shortened".*\n'
    last_line_tail=b'opening instruction; "shortened".*'
OK	14e99a2da8af9d64bc18df75150260632e872447	20954	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_display_family_surface_2026_11_07.md
    last70=b'pening\ninstruction; "shortened"; "continue"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "shortened"; "continue"; "continue" (the check).*'
OK	697c636860507451d8631b912bae1850269c0b38	12417	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_fit_and_rest_second_cut_surface_2026_11_04.md
    last70=b' words: the opening instruction;\n"narrowed"; "continue" (the check).*\n'
    last_line_tail=b'"narrowed"; "continue" (the check).*'
OK	694fa21cb79f211bfef73e76687c41f2026cbf1f	16617	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_fit_and_rest_surface_2026_11_04.md
    last70=b'h hits in the face ratification records and the phrase-units record.*\n'
    last_line_tail=b'ch hits in the face ratification records and the phrase-units record.*'
OK	266976e42cff65f5b2c66efdadeb1ca51d3a3d74	13833	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_fit_and_rest_third_cut_surface_2026_11_04.md
    last70=b'\'s words: the opening instruction;\n"narrow"; "continue" (the check).*\n'
    last_line_tail=b'"narrow"; "continue" (the check).*'
OK	ccfc164cf7fba596ec3673cc735f6e6225aecde2	12389	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md
    last70=b' instruction;\n"shortened"; "yes" (family 6); "continue"; "continue".*\n'
    last_line_tail=b'"shortened"; "yes" (family 6); "continue"; "continue".*'
OK	847aa0ea5d622699627197ac2cee414977bff3dc	22551	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_modal_counts_family_surface_2026_11_07.md
    last70=b'words: the opening instruction;\n"Shortened"; "continue"; "continue".*\n'
    last_line_tail=b'"Shortened"; "continue"; "continue".*'
OK	466d97735b2e9f9f237dc5e22d05abfcda82cd44	25171	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_presets_scope_family_surface_2026_11_07.md
    last70=b'tion;\n"shortened"; "continue" (the surface); "continue" (the check).*\n'
    last_line_tail=b'"shortened"; "continue" (the surface); "continue" (the check).*'
OK	32ef5b5d684ebef6f5eff0a996a174ac12fb03f2	12670	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_s38_eighth_cut_surface_2026_11_03.md
    last70=b'\'s words: the opening instruction;\n"narrow"; "continue" (the check).*\n'
    last_line_tail=b'"narrow"; "continue" (the check).*'
OK	a7707aa72ca36647995f559e94a44de57289715e	13555	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_s38_fifth_cut_surface_2026_11_03.md
    last70=b'nstruction;\n"narrow"; "continue" (this cut); "continue" (the check).*\n'
    last_line_tail=b'"narrow"; "continue" (this cut); "continue" (the check).*'
OK	ab863286b624af613cf75e1897ebbb430db2f1ff	22076	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_s38_first_cut_surface_2026_11_03.md
    last70=b'rds: the opening instruction; "narrow"; "continue"; "a"; "continue".*\n'
    last_line_tail=b'ords: the opening instruction; "narrow"; "continue"; "a"; "continue".*'
OK	4eaca060276f99cd0c3f61ebce80335cdead3d72	11547	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_s38_fourth_cut_surface_2026_11_03.md
    last70=b'ontinue"; "continue"; "continue" (this cut); "continue" (the check).*\n'
    last_line_tail=b'continue"; "continue"; "continue" (this cut); "continue" (the check).*'
OK	49c66dde554040d80d7f9430a6f729b18aeb3562	11858	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_s38_ratification_surface_2026_11_03.md
    last70=b'pening\ninstruction; "narrowest"; "continue"; "continue" (the check).*\n'
    last_line_tail=b'instruction; "narrowest"; "continue"; "continue" (the check).*'
OK	968aa4f18b0c1e5adf3ca11bef91f350a33976cc	13403	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_s38_second_cut_surface_2026_11_03.md
    last70=b'd on\nentry 508; the user\'s words: the opening instruction; "narrow".*\n'
    last_line_tail=b'entry 508; the user\'s words: the opening instruction; "narrow".*'
OK	971b5b83a6b054e01372e81b6c6a518ebe2e27cb	18088	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_s38_seventh_cut_surface_2026_11_03.md
    last70=b';\n"narrow as BEFORE"; "continue" (this cut); "continue" (the check).*\n'
    last_line_tail=b'"narrow as BEFORE"; "continue" (this cut); "continue" (the check).*'
OK	e4e4a8434bd47f735a9b7aa8dba4d03e72ce38b5	17546	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_s38_sixth_cut_surface_2026_11_03.md
    last70=b'narrow as last time"; "continue" (this cut); "continue" (the check).*\n'
    last_line_tail=b'"narrow as last time"; "continue" (this cut); "continue" (the check).*'
OK	eeaa9e530af8da2dcd6b67245aefc85fe9601770	12711	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_s38_third_cut_surface_2026_11_03.md
    last70=b'ow"; "continue"; "A"; "continue" (this cut); "continue" (the check).*\n'
    last_line_tail=b'row"; "continue"; "A"; "continue" (this cut); "continue" (the check).*'
OK	8da8774dd496fae773424e719437a4d1d23c6dc5	26148	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md
    last70=b' words: the opening instruction;\n"narrowed"; "continue" (the check).*\n'
    last_line_tail=b'"narrowed"; "continue" (the check).*'
OK	d44f9ecc7ff9eb39f4e73caf8f360415b699044f	21522	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_tier3_display_surface_2026_11_04.md
    last70=b'e opening instruction;\n"narrow"; "continue"; "continue" (the check).*\n'
    last_line_tail=b'"narrow"; "continue"; "continue" (the check).*'
OK	f1cec9c8504a13308c5bed58c58738d4ae39248f	19361	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_tier3_literature_facts_surface_2026_11_04.md
    last70=b'\'s words: the opening instruction;\n"narrow"; "continue" (the check).*\n'
    last_line_tail=b'"narrow"; "continue" (the check).*'
OK	58932ec407fa641517ff46346ad18ba8cfcba006	21940	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_tier3_span_kinds_surface_2026_11_04.md
    last70=b' words: the opening instruction;\n"narrowed"; "continue" (the check).*\n'
    last_line_tail=b'"narrowed"; "continue" (the check).*'
OK	d813f034b12c17a43c377b0c5bad7cd046267af1	12488	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_unplaced_families_2026_11_06.md
    last70=b'6. The user\'s words: the opening\ninstruction; "shorten"; "continue".*\n'
    last_line_tail=b'instruction; "shorten"; "continue".*'
OK	a9bbee14edb476731f06e0c928dee1f363dd700d	166333	zeros=0	ends_newline=True	ratification_surfaces/cowork_l3_unplaced_inventory_2026_11_04.md
    last70=b' on entry 535; the user\'s words: the opening\ninstruction; "shorten".*\n'
    last_line_tail=b'instruction; "shorten".*'
OK	c969f9d9cb85a0310dbfdaf8317b84f74e6e8fe4	38702	zeros=0	ends_newline=True	ratification_surfaces/cowork_llm_correction_scope_2026_11_07.md
    last70=b' the user\'s words: the opening instruction; "shortened"; "continue".*\n'
    last_line_tail=b'; the user\'s words: the opening instruction; "shortened"; "continue".*'
OK	78e4498da26365b7f83936f9125f5f9363cf1ce7	46747	zeros=0	ends_newline=True	records/cc/instructions/cc_instruction_records_landing_2026_11_07.md
    last70=b"No step, prediction or stop\nchanged but items 1, 2 and 6's wording.**\n"
    last_line_tail=b"changed but items 1, 2 and 6's wording.**"
files: 175; failing: 0 []
~~~~

## 0(e) — `python tools/audit/gen_evidence_pin_membership.py --check` before (exit 1)

~~~~
STALE vs the derivation: evidence_pin_membership.json does not re-derive
~~~~

## 0(e) — `python tools/audit/gen_evidence_pin_membership.py` (write, exit 0)

~~~~
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 218
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
~~~~

## 0(e) — `python tools/audit/gen_evidence_pin_membership.py --check` after (exit 0)

~~~~
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 218
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
~~~~

## 0(e) — `git diff c9aa4e8563dd7c8ef03780c8bf562e324e5c4db7 b0c4673afcbb1eb6bfcef132bf5f7491f2064404` (the artifact's blob at the start tip against the new blob)

~~~~
diff --git a/c9aa4e8563dd7c8ef03780c8bf562e324e5c4db7 b/b0c4673afcbb1eb6bfcef132bf5f7491f2064404
index c9aa4e8563..b0c4673afc 100644
--- a/c9aa4e8563dd7c8ef03780c8bf562e324e5c4db7
+++ b/b0c4673afcbb1eb6bfcef132bf5f7491f2064404
@@ -17,7 +17,7 @@
  },
  "counts": {
   "generated_ratification_documents": 7,
-  "ruling_records_read": 172,
+  "ruling_records_read": 218,
   "members": 7,
   "members_pinned": 5,
   "members_unresolved": 0,
@@ -313,6 +313,52 @@
   "records/cowork/rulings/cowork_rulings_2026_10_26_l3_position_57_sitting.md",
   "records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md",
   "records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_02_l3_route_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_vocabulary_point_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_key_areas_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_03_research_registry_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_04_l3_literature_facts_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_key_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_l3_code_interfaces_family_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_l3_display_family_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_l3_modal_counts_family_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md",
   "records/cowork/rulings/cowork_rulings_oi345_oi342_2026_08_07.md"
  ],
  "named_in_a_ruling_record_but_not_generated": {
~~~~

## 0(e) — the pathspec file fed to `git add --pathspec-from-file`, quoted whole

~~~~
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_nine.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_one.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_two.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_three.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_four.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_five.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_six.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_seven.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_eight.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_nine.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_one.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_two.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_three.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_four.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_five.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_six.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_seven.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_eight.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_nine.md
records/cowork/handoff/cowork_handoff_entry_five_hundred.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_one.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_two.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_three.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_four.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_five.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_six.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seven.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eight.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_nine.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_ten.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eleven.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twelve.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirteen.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fourteen.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifteen.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixteen.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventeen.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eighteen.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_nineteen.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_one.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_two.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_three.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_four.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_five.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_six.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_seven.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_eight.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_nine.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_one.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_two.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_three.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_four.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_five.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_six.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_seven.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_eight.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_nine.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_one.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_two.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_three.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_four.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_five.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_six.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_seven.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_eight.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_nine.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_one.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_two.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_three.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_four.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_five.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_six.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_seven.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_eight.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_nine.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_one.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_two.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_three.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_four.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_five.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_six.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_seven.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_eight.md
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_nine.md
records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_02_l3_route_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_vocabulary_point_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_key_areas_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_03_research_registry_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_04_l3_literature_facts_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_key_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_l3_code_interfaces_family_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_l3_display_family_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_l3_modal_counts_family_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md
ratification_surfaces/cowork_l3_cadence_type_surface_2026_11_03.md
ratification_surfaces/cowork_l3_catalog_further_rows_surface_2026_11_06.md
ratification_surfaces/cowork_l3_catalog_idiom_tags_part1_surface_2026_11_07.md
ratification_surfaces/cowork_l3_catalog_idiom_tags_part2_surface_2026_11_07.md
ratification_surfaces/cowork_l3_catalog_key_surface_2026_11_06.md
ratification_surfaces/cowork_l3_catalog_lead_rows_surface_2026_11_06.md
ratification_surfaces/cowork_l3_catalog_pairwise_grammar_surface_2026_11_07.md
ratification_surfaces/cowork_l3_catalog_recognition_part1_surface_2026_11_06.md
ratification_surfaces/cowork_l3_catalog_recognition_part2_surface_2026_11_06.md
ratification_surfaces/cowork_l3_catalog_substitution_part1_surface_2026_11_06.md
ratification_surfaces/cowork_l3_catalog_substitution_part2_surface_2026_11_06.md
ratification_surfaces/cowork_l3_catalog_suggestion_tool_and_cadential_entries_surface_2026_11_07.md
ratification_surfaces/cowork_l3_code_interfaces_family_surface_2026_11_07.md
ratification_surfaces/cowork_l3_decomposition_rules_family_surface_2026_11_07.md
ratification_surfaces/cowork_l3_display_family_surface_2026_11_07.md
ratification_surfaces/cowork_l3_fit_and_rest_second_cut_surface_2026_11_04.md
ratification_surfaces/cowork_l3_fit_and_rest_surface_2026_11_04.md
ratification_surfaces/cowork_l3_fit_and_rest_third_cut_surface_2026_11_04.md
ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md
ratification_surfaces/cowork_l3_modal_counts_family_surface_2026_11_07.md
ratification_surfaces/cowork_l3_presets_scope_family_surface_2026_11_07.md
ratification_surfaces/cowork_l3_s38_eighth_cut_surface_2026_11_03.md
ratification_surfaces/cowork_l3_s38_fifth_cut_surface_2026_11_03.md
ratification_surfaces/cowork_l3_s38_first_cut_surface_2026_11_03.md
ratification_surfaces/cowork_l3_s38_fourth_cut_surface_2026_11_03.md
ratification_surfaces/cowork_l3_s38_ratification_surface_2026_11_03.md
ratification_surfaces/cowork_l3_s38_second_cut_surface_2026_11_03.md
ratification_surfaces/cowork_l3_s38_seventh_cut_surface_2026_11_03.md
ratification_surfaces/cowork_l3_s38_sixth_cut_surface_2026_11_03.md
ratification_surfaces/cowork_l3_s38_third_cut_surface_2026_11_03.md
ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md
ratification_surfaces/cowork_l3_tier3_display_surface_2026_11_04.md
ratification_surfaces/cowork_l3_tier3_literature_facts_surface_2026_11_04.md
ratification_surfaces/cowork_l3_tier3_span_kinds_surface_2026_11_04.md
ratification_surfaces/cowork_l3_unplaced_families_2026_11_06.md
ratification_surfaces/cowork_l3_unplaced_inventory_2026_11_04.md
ratification_surfaces/cowork_llm_correction_scope_2026_11_07.md
records/cc/instructions/cc_instruction_records_landing_2026_11_07.md
tools/audit/evidence_pin_membership.json
~~~~

## 0(e) — `python tools/audit/changed_paths.py --staged` (exit 0), whole

~~~~
A	ratification_surfaces/cowork_l3_cadence_type_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_catalog_further_rows_surface_2026_11_06.md
A	ratification_surfaces/cowork_l3_catalog_idiom_tags_part1_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_catalog_idiom_tags_part2_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_catalog_key_surface_2026_11_06.md
A	ratification_surfaces/cowork_l3_catalog_lead_rows_surface_2026_11_06.md
A	ratification_surfaces/cowork_l3_catalog_pairwise_grammar_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_catalog_recognition_part1_surface_2026_11_06.md
A	ratification_surfaces/cowork_l3_catalog_recognition_part2_surface_2026_11_06.md
A	ratification_surfaces/cowork_l3_catalog_substitution_part1_surface_2026_11_06.md
A	ratification_surfaces/cowork_l3_catalog_substitution_part2_surface_2026_11_06.md
A	ratification_surfaces/cowork_l3_catalog_suggestion_tool_and_cadential_entries_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_code_interfaces_family_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_decomposition_rules_family_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_display_family_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_fit_and_rest_second_cut_surface_2026_11_04.md
A	ratification_surfaces/cowork_l3_fit_and_rest_surface_2026_11_04.md
A	ratification_surfaces/cowork_l3_fit_and_rest_third_cut_surface_2026_11_04.md
A	ratification_surfaces/cowork_l3_language_model_family_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_modal_counts_family_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_presets_scope_family_surface_2026_11_07.md
A	ratification_surfaces/cowork_l3_s38_eighth_cut_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_s38_fifth_cut_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_s38_first_cut_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_s38_fourth_cut_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_s38_ratification_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_s38_second_cut_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_s38_seventh_cut_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_s38_sixth_cut_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_s38_third_cut_surface_2026_11_03.md
A	ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md
A	ratification_surfaces/cowork_l3_tier3_display_surface_2026_11_04.md
A	ratification_surfaces/cowork_l3_tier3_literature_facts_surface_2026_11_04.md
A	ratification_surfaces/cowork_l3_tier3_span_kinds_surface_2026_11_04.md
A	ratification_surfaces/cowork_l3_unplaced_families_2026_11_06.md
A	ratification_surfaces/cowork_l3_unplaced_inventory_2026_11_04.md
A	ratification_surfaces/cowork_llm_correction_scope_2026_11_07.md
A	records/cc/instructions/cc_instruction_records_landing_2026_11_07.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eight.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eighteen.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eleven.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifteen.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_eight.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_five.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_four.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_nine.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_one.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_seven.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_six.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_three.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fifty_two.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_five.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_eight.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_five.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_four.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_nine.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_one.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_seven.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_six.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_three.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_forty_two.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_four.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_fourteen.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_nine.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_nineteen.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_one.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seven.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventeen.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_six.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixteen.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_eight.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_five.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_four.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_nine.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_one.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_seven.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_six.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_three.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_sixty_two.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_ten.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirteen.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_eight.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_five.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_four.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_nine.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_one.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_seven.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_six.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_three.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_thirty_two.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_three.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twelve.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_eight.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_five.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_four.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_nine.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_one.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_seven.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_six.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_three.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_twenty_two.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_two.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_eight.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_five.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_four.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_nine.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_one.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_seven.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_six.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_three.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eighty_two.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_eight.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_five.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_four.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_nine.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_one.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_seven.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_six.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_three.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ninety_two.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_nine.md
A	records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_02_l3_route_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_vocabulary_point_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_key_areas_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_first_cut_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_second_cut_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_03_research_registry_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_04_l3_literature_facts_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_further_rows_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_key_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_lead_rows_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part1_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_recognition_part2_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part1_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_06_l3_catalog_substitution_part2_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part1_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_idiom_tags_part2_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_pairwise_grammar_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_l3_catalog_suggestion_tool_and_cadential_entries_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_l3_code_interfaces_family_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_l3_decomposition_rules_family_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_l3_display_family_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_l3_modal_counts_family_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_l3_presets_scope_family_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md
A	records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md
M	tools/audit/evidence_pin_membership.json
176 changed path record(s) [staged]
~~~~

## 0(e) — `git push origin master` (exit 0)

~~~~
To https://github.com/slimvince/MuseScore
   864deb43c5..113b2ce680  master -> master
~~~~

## 0(f) — the opening capture: `python tools/audit/gen_guard_state.py --check` (exit 1), whole

~~~~
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
  [PASS] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_per_session_reading.py --check
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
83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
~~~~

## 0(f) — `python tools/audit/gen_guard_classification.py --check` (exit 2)

~~~~
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_per_session_reading.py', 'tools/audit/gen_withheld_family_reading.py']
~~~~

## 3(b) — `python tools/audit/gen_status_batch_bound.py --apply` (exit 0)

~~~~
wrote tools\audit\status_batch_bound.json
  entries moved: 3, 1,867 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
~~~~

## 3(b) — `python tools/audit/gen_status_batch_bound.py --check` (exit 0)

~~~~
  entries moved: 3, 1,867 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
~~~~

## 3(b) — `python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md` (exit 0)

~~~~
  STATUS.md / STATUS_ARCHIVE.md: moved 131 span(s), 457,949 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
~~~~

## 3(b) — `python tools/audit/gen_status_residue_move.py --check` (exit 0)

~~~~
  candidates: 17, moved 16, left at site by the reading 1
  characters moved: 46,105
  byte-present in the companion exactly once: True
  absent from the must-read:                  True
  every flagged entry still at site:          True
~~~~

## 3(b) — `python tools/audit/gen_status_archive_pass.py --check` (exit 0)

~~~~
  dated entries moved: 52
  at the pass commit, the live file was exactly base-minus-range: True
  the moved block is verbatim in the archive at HEAD:             True
  the moved block is absent from the live file at HEAD:           True
~~~~

## 3(c)1 — `python tools/audit/gen_evidence_pin_membership.py --check` (exit 0)

~~~~
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 218
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
~~~~

## 3(c)2 — `python tools/audit/gen_session_start_read_size.py --check` before (exit 1)

~~~~
STALE vs the measurement: session_start_read_size.json does not re-derive
~~~~

## 3(c)2 — `python tools/audit/gen_session_start_read_size.py` (write, exit 0)

~~~~
wrote tools/audit/session_start_read_size.json
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              40636
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 169182, the six session-start spans 105441, overstated by 63741
    CLAUDE.md                                                                105441
    STATUS.md                                                                 10585
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 236342
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 236342 [ruled membership]  (-130779, -35.62%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 236342 [ruled membership]  (-60490, -20.38%)  <- CROSSES A REGIME BOUNDARY
~~~~

## 3(c)2 — `python tools/audit/gen_session_start_read_size.py --check` after (exit 0)

~~~~
the session-start read measurement re-derives
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              40636
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 169182, the six session-start spans 105441, overstated by 63741
    CLAUDE.md                                                                105441
    STATUS.md                                                                 10585
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 236342
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 236342 [ruled membership]  (-130779, -35.62%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 236342 [ruled membership]  (-60490, -20.38%)  <- CROSSES A REGIME BOUNDARY
~~~~

## 3(c)2 — `python tools/audit/gen_defense_share.py --check` before (exit 1)

~~~~
STALE vs the measurement: defense_share.json does not re-derive
~~~~

## 3(c)2 — `python tools/audit/gen_defense_share.py` (write, exit 0)

~~~~
wrote tools/audit/defense_share.json
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   40636  ( 8.54%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (105441): 12.29%
    of the whole session-start read (236342): 5.48%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
~~~~

## 3(c)2 — `python tools/audit/gen_defense_share.py --check` after (exit 0)

~~~~
the defense-share measurement re-derives
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   40636  ( 8.54%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (105441): 12.29%
    of the whole session-start read (236342): 5.48%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
~~~~

## 3(c)3 — `python tools/audit/gen_l3_outgoing_population.py --check` before (exit 1)

~~~~
STALE vs the derivation: l3_outgoing_population.json does not re-derive
~~~~

## 3(c)3 — `python tools/audit/gen_l3_outgoing_population.py` (write, exit 0)

~~~~
item 1: #### Layer 4 — the per-slice chord-symbol decoder — 140 lines
item 1: #### Layer 5 — the function/cadence layer — 117 lines
item 1: #### Layer 6 — the grouping layer — 65 lines
item 1: ### 4.3 ChordSymbolFormatter — 115 lines
item 1: ### 4.3b HarmonicRhythm — 81 lines
item 1: #### Harmonic rhythm detection — 20 lines
item 2: 12 distinct names, 12 resolve (844399 bytes), 4 in the specification set
item 3: 26 in-set files with a hit, 1364 distinct hit lines over them (ARCHITECTURE.md inside the six spans: 83, outside: 355); residue files: 150
item 4: in a specification-set member — 10
item 4: in an item-2 document that resolves — 9
item 4: inside item 1 — 3
transfer span: ratification_surfaces/cowork_comparison_l0_l1_reading.md — 287 lines
transfer span: ratification_surfaces/cowork_comparison_l2_reading.md — 948 lines
tabulation population: 57 members, 11276 lines, 1075960 bytes
wrote C:\s\MS\tools\audit\l3_outgoing_population.json
~~~~

## 3(c)3 — `python tools/audit/gen_l3_outgoing_population.py --check` after (exit 0)

~~~~
l3_outgoing_population.json re-derives
~~~~

## 3(c)3 — `python tools/audit/gen_l0_l1_outgoing_population.py --check` (exit 0; not regenerated)

~~~~
l0_l1_outgoing_population.json re-derives
~~~~

## 3(c)4 — `python tools/audit/gen_derivation_boot_pack.py --check` (exit 0; not regenerated)

~~~~
FROZEN SOURCES: 18 of 39 frozen pack file(s) would render at a different length from the sources as they stand today. NOT COMPARED; sets no exit code.
  - harmony-boundary/02_the_guiding_principles_and_the_conventions.md: the directory holds 59762 characters; today's sources would render 67534
  - harmony-boundary/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - harmony-boundary/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - harmony-boundary/05_the_ratified_design_intent.md: the directory holds 252572 characters; today's sources would render 252641
  - l0-l1/02_the_guiding_principles_and_the_conventions.md: the directory holds 61113 characters; today's sources would render 68308
  - l0-l1/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - l0-l1/04_the_dispatch_protocol.md: the directory holds 103431 characters; today's sources would render 108389
  - l0-l1/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
  - l0-l1/07_the_charter_the_layers_and_the_decisions.md: the directory holds 29031 characters; today's sources would render 36208
  - l0-l1/08_the_five_research_extracts.md: the directory holds 76722 characters; today's sources would render 103250
  - l0-l1/09_the_empirical_findings_ledger.md: the directory holds 50666 characters; today's sources would render 50963
  - l2/02_the_guiding_principles_and_the_conventions.md: the directory holds 64913 characters; today's sources would render 65745
  - l2/07_the_charter_the_layers_and_the_decisions.md: the directory holds 33067 characters; today's sources would render 36208
  - l3/02_the_guiding_principles_and_the_conventions.md: the directory holds 68743 characters; today's sources would render 68308
  - scoring-model/02_the_guiding_principles_and_the_conventions.md: the directory holds 60536 characters; today's sources would render 68308
  - scoring-model/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - scoring-model/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - scoring-model/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
the derivation boot pack re-derives
  harmony-boundary: FROZEN — 7 file(s) at their recorded blobs
  l0-l1: FROZEN — 10 file(s) at their recorded blobs
  l2: FROZEN — 10 file(s) at their recorded blobs
  l3: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
~~~~

## 3(c)5 — `python tools/audit/gen_per_session_reading.py --check` before (exit 1)

~~~~
STALE vs the measurement: per_session_reading.json does not re-derive
~~~~

## 3(c)5 — `python tools/audit/gen_per_session_reading.py` (write, exit 0)

~~~~
wrote tools/audit/per_session_reading.json
  the ordinary session-start read (imported) 236342
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  invariant share: dispatches 32.35 %, reports 19.00 %
  reports with an appendix beside them 6: reports proper 218252, appendices 887153 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 672856
  Cowork, per sitting, in the shape of the sitting of entry 461: 972160
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
~~~~

## 3(c)5 — `python tools/audit/gen_per_session_reading.py --check` after (exit 0)

~~~~
the per-session reading measurement re-derives
  the ordinary session-start read (imported) 236342
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  invariant share: dispatches 32.35 %, reports 19.00 %
  reports with an appendix beside them 6: reports proper 218252, appendices 887153 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 672856
  Cowork, per sitting, in the shape of the sitting of entry 461: 972160
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
~~~~

## 3(c) — `python tools/audit/changed_paths.py` after the regenerations (exit 0), whole

~~~~
 M	STATUS.md
 M	STATUS_ARCHIVE.md
 M	docs/research_papers/BIBLIOGRAPHY.md
 M	docs/research_papers/README.md
 M	tools/audit/claude_md_finer_archive.json
 M	tools/audit/defense_share.json
 M	tools/audit/gen_status_batch_bound.py
 M	tools/audit/l3_outgoing_population.json
 M	tools/audit/per_session_reading.json
 M	tools/audit/session_start_read_size.json
 M	tools/audit/status_batch_bound.json
??	Claude outputs/
??	Codex research inventory/
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
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
404 changed path record(s) [worktree]
~~~~

## 3(c) — the diff script, quoted whole: `artifact_diffs.py` (as run; the first run stopped on a console-encoding error before any diff printed, and `sys.stdout.reconfigure` was added)

~~~~
"""3(c): diff each moved artifact against its blob at a named commit, between explicit blob hashes.

argv[1] = repository root; argv[2] = base commit; argv[3:] = artifact paths.
For each path: the base blob is `git rev-parse <base>:<path>`, the new blob is written with
`git hash-object -w <path>`, and `git diff <base-blob> <new-blob>` is printed whole.
"""
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT, BASE, PATHS = sys.argv[1], sys.argv[2], sys.argv[3:]


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", check=True).stdout


for p in PATHS:
    old = git("rev-parse", "%s:%s" % (BASE, p)).strip()
    new = git("hash-object", "-w", p).strip()
    print("=" * 100)
    print("ARTIFACT %s" % p)
    print("  base %s  blob %s" % (BASE, old))
    print("  new          blob %s" % new)
    if old == new:
        print("  IDENTICAL")
        continue
    print(git("diff", old, new))
~~~~

## 3(c) — `python -I artifact_diffs.py /c/s/MS 864deb43c5dae6415a8c8b9e98901e7b2c2a96ae tools/audit/session_start_read_size.json tools/audit/defense_share.json tools/audit/l3_outgoing_population.json tools/audit/per_session_reading.json tools/audit/status_batch_bound.json` (exit 0), whole

~~~~
====================================================================================================
ARTIFACT tools/audit/session_start_read_size.json
  base 864deb43c5dae6415a8c8b9e98901e7b2c2a96ae  blob 1bb887339a5a10ec35a363927f482b58aaa5eb5b
  new          blob 8de5f6db64f100e7b8817ef56ef075ed43d100f0
diff --git a/1bb887339a5a10ec35a363927f482b58aaa5eb5b b/8de5f6db64f100e7b8817ef56ef075ed43d100f0
index 1bb887339a..8de5f6db64 100644
--- a/1bb887339a5a10ec35a363927f482b58aaa5eb5b
+++ b/8de5f6db64f100e7b8817ef56ef075ed43d100f0
@@ -176,11 +176,11 @@
   },
   "characters_per_member": {
    "CLAUDE.md": 105441,
-   "STATUS.md": 11146,
+   "STATUS.md": 10585,
    "DECISIONS.md": 117490,
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
   },
-  "total_characters": 236903,
+  "total_characters": 236342,
   "further_spans_of_the_same_artifact_NOT_counted_into_the_read": {
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows": {
     "characters": 62498,
@@ -276,10 +276,10 @@
    "from_commit": "1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
    "from_total": 367121,
    "from_regime": "whole-file practice",
-   "to_total": 236903,
+   "to_total": 236342,
    "to_regime": "ruled membership",
-   "change_in_characters": -130218,
-   "change_percent": -35.47,
+   "change_in_characters": -130779,
+   "change_percent": -35.62,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   },
@@ -287,10 +287,10 @@
    "from_commit": "594074e1e1900079e449d2b79a38920d21bca6e6",
    "from_total": 296832,
    "from_regime": "whole-file practice",
-   "to_total": 236903,
+   "to_total": 236342,
    "to_regime": "ruled membership",
-   "change_in_characters": -59929,
-   "change_percent": -20.19,
+   "change_in_characters": -60490,
+   "change_percent": -20.38,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   }

====================================================================================================
ARTIFACT tools/audit/defense_share.json
  base 864deb43c5dae6415a8c8b9e98901e7b2c2a96ae  blob 2ad87e2668e5688af2d286806181d9c91d81ef58
  new          blob 507c7e68103b16ec06bdeb849b0c247fe23a2d03
diff --git a/2ad87e2668e5688af2d286806181d9c91d81ef58 b/507c7e68103b16ec06bdeb849b0c247fe23a2d03
index 2ad87e2668..507c7e6810 100644
--- a/2ad87e2668e5688af2d286806181d9c91d81ef58
+++ b/507c7e68103b16ec06bdeb849b0c247fe23a2d03
@@ -77,7 +77,7 @@
  ],
  "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
   "the_six_session_start_spans": 105441,
-  "the_whole_ordinary_session_start_read": 236903,
+  "the_whole_ordinary_session_start_read": 236342,
   "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked defense; the second says how much of the WHOLE boot it is. A share quoted against one of them is not the share against the other."
  },
  "per_span": [
@@ -142,7 +142,7 @@
   "characters_had_every_clause_been_closed_at_the_next_marked_clause": 51684,
   "characters_had_every_clause_run_to_its_paragraph_end": 160906,
   "share_of_the_six_session_start_spans": 12.29,
-  "share_of_the_whole_ordinary_session_start_read": 5.47
+  "share_of_the_whole_ordinary_session_start_read": 5.48
  },
  "every_clause_published_so_the_tables_reach_is_inspectable_rather_than_asserted": [
   {

====================================================================================================
ARTIFACT tools/audit/l3_outgoing_population.json
  base 864deb43c5dae6415a8c8b9e98901e7b2c2a96ae  blob b196fe6e8c6d19cdf48c7a9af3c0bca38570b137
  new          blob 71a559216988dbc17f459a2b9e8e432c451f2a85
diff --git a/b196fe6e8c6d19cdf48c7a9af3c0bca38570b137 b/71a559216988dbc17f459a2b9e8e432c451f2a85
index b196fe6e8c..71a5592169 100644
--- a/b196fe6e8c6d19cdf48c7a9af3c0bca38570b137
+++ b/71a559216988dbc17f459a2b9e8e432c451f2a85
@@ -20111,7 +20111,7 @@
      "the_statement": "hit, outside the specification document set, not dispositioned by this comparison; reachable by the mining map",
      "hit_records": [
       {
-       "line_number": 20,
+       "line_number": 18,
        "term": "phrase",
        "tier": "admitting",
        "line": "*★ ARCHIVED 2026-08-17, THE SECOND ACT — the dated entries that PREDATE (or paraphrase) the OI-222 pointer convention fell to `operative-rule-text` in the pinned measurement and stayed when the block above was cleared. They were READ one by one and moved verbatim to `STATUS_ARCHIVE.md` by `records/cc/instructions/cc_instruction_preparation_seventh.md` Task 1, under Ruling 3 of `records/cowork/rulings/cowork_rulings_2026_08_17_sixth_return.md`, which brings them under Ruling 4's own line. **One candidate did NOT move and is flagged:** the navigational paragraph at the foot of this file is not a completed batch's dated record but a live pointer to the archive and to the gate policy, so the read-before-move safeguard left it at site. The per-entry reconciliation is re-derived by `tools/audit/gen_status_residue_move.py --check`.*"

====================================================================================================
ARTIFACT tools/audit/per_session_reading.json
  base 864deb43c5dae6415a8c8b9e98901e7b2c2a96ae  blob 1388622e18fbce34416420b790215548d53c3cbb
  new          blob 63f2a0756c2c7e7703ac478ce01125c29c88734f
diff --git a/1388622e18fbce34416420b790215548d53c3cbb b/63f2a0756c2c7e7703ac478ce01125c29c88734f
index 1388622e18..63f2a0756c 100644
--- a/1388622e18fbce34416420b790215548d53c3cbb
+++ b/63f2a0756c2c7e7703ac478ce01125c29c88734f
@@ -15,11 +15,11 @@
    "its_one_home": "`tools/audit/session_start_read_size.json`, written by `tools/audit/gen_session_start_read_size.py`; what stands here is that tool's own `measure` called at the tree, and its total is checked against that artifact on every run",
    "characters_per_member": {
     "CLAUDE.md": 105441,
-    "STATUS.md": 11146,
+    "STATUS.md": 10585,
     "DECISIONS.md": 117490,
     "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
    },
-   "total_characters": 236903,
+   "total_characters": 236342,
    "the_reading_of_claude_md": {
     "regime": "ruled membership",
     "characters": 105441
@@ -1352,28 +1352,28 @@
      "the_writing_sides_read": "unwritten practice"
     },
     "the_record_that_mandates_it": "the standing clause `Every dispatch's read-first block names the CURRENT HANDOVER BLOCK`, which this repository carries as numbered entry files; the writing side's three is its own practice",
-    "the_population_count": 398,
+    "the_population_count": 489,
     "the_three": [
      {
-      "name": "cowork_handoff_entry_four_hundred_and_seventy_six.md",
-      "added_in_commit": "dd06b5fea97a0f7e1fee4ffa35b7aebdc704ebd5",
-      "added_at_unix_time": 1793616911,
-      "characters": 8572
+      "name": "cowork_handoff_entry_four_hundred_and_ninety_three.md",
+      "added_in_commit": "113b2ce680e527e81342d8f79d5acbad281334d7",
+      "added_at_unix_time": 1794074726,
+      "characters": 8650
      },
      {
-      "name": "cowork_handoff_entry_four_hundred_and_seventy_eight.md",
-      "added_in_commit": "60d9048cda3b0a33b216e3a4e468b29dbe5d14d8",
-      "added_at_unix_time": 1793626075,
-      "characters": 6606
+      "name": "cowork_handoff_entry_four_hundred_and_ninety_two.md",
+      "added_in_commit": "113b2ce680e527e81342d8f79d5acbad281334d7",
+      "added_at_unix_time": 1794074726,
+      "characters": 7994
      },
      {
-      "name": "cowork_handoff_entry_four_hundred_and_seventy_seven.md",
-      "added_in_commit": "60d9048cda3b0a33b216e3a4e468b29dbe5d14d8",
-      "added_at_unix_time": 1793626075,
-      "characters": 8234
+      "name": "cowork_handoff_entry_four_hundred_and_seventy_nine.md",
+      "added_in_commit": "113b2ce680e527e81342d8f79d5acbad281334d7",
+      "added_at_unix_time": 1794074726,
+      "characters": 5738
      }
     ],
-    "characters": 23412
+    "characters": 22382
    }
   ],
   "totals_by_side": {
@@ -1381,7 +1381,7 @@
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 236903
+      "characters": 236342
      },
      {
       "member": "BUILD_AND_TEST.md",
@@ -1401,13 +1401,13 @@
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 23412
+      "characters": 22382
      }
     ],
-    "without_the_injected_copy_of_CLAUDE_md": 674447,
-    "with_it": 843629,
+    "without_the_injected_copy_of_CLAUDE_md": 672856,
+    "with_it": 842038,
     "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, 169182 characters",
-    "under_ruling_2_of_2026_11_01": 738188,
+    "under_ruling_2_of_2026_11_01": 736597,
     "how_ruling_2_moves_it": "Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`: the injected copy is the read of the six spans, so their file-tool read (105441 characters) leaves the sum and the injected copy stays; the eight-line check's own reads are not sized here",
     "left_out_and_said_so": "the previous report at the portions a dispatch orders, the reading file at its ordered portions, the ruling records a dispatch orders — varies per dispatch and is not sized here"
    },
@@ -1415,7 +1415,7 @@
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 236903
+      "characters": 236342
      },
      {
       "member": "entry 118, the bridge-fault section",
@@ -1435,7 +1435,7 @@
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 23412
+      "characters": 22382
      },
      {
       "member": "the latest report of the arc, whole: cc_report_l3_comparison_tabulation_thirtieth_2026_10_31.md",
@@ -1446,7 +1446,7 @@
       "characters": 151805
      }
     ],
-    "characters": 973751,
+    "characters": 972160,
     "left_out_and_said_so": "the verification reads at the objects (the reading file at its sections, the guard state, the ref files, the away-returns close) — varies per batch and is not sized here"
    }
   }
@@ -3832,7 +3832,7 @@
     "characters_had_every_clause_been_closed_at_the_next_marked_clause": 51684,
     "characters_had_every_clause_run_to_its_paragraph_end": 160906,
     "share_of_the_six_session_start_spans": 12.29,
-    "share_of_the_whole_ordinary_session_start_read": 5.47
+    "share_of_the_whole_ordinary_session_start_read": 5.48
    },
    "per_span": [
     {
@@ -3892,7 +3892,7 @@
    ],
    "the_two_denominators": {
     "the_six_session_start_spans": 105441,
-    "the_whole_ordinary_session_start_read": 236903
+    "the_whole_ordinary_session_start_read": 236342
    },
    "how_these_relate_to_the_sums_above": "a marked clause lies INSIDE a sub-block, so these values overlap table 2's sums and are never added to them"
   }

====================================================================================================
ARTIFACT tools/audit/status_batch_bound.json
  base 864deb43c5dae6415a8c8b9e98901e7b2c2a96ae  blob 7341bd0b7033bb2e71d8f361c170a01684c9b6b3
  new          blob 276476ff453223b5a1203f97ad6349d5dc38b721
diff --git a/7341bd0b7033bb2e71d8f361c170a01684c9b6b3 b/276476ff453223b5a1203f97ad6349d5dc38b721
index 7341bd0b70..276476ff45 100644
--- a/7341bd0b7033bb2e71d8f361c170a01684c9b6b3
+++ b/276476ff453223b5a1203f97ad6349d5dc38b721
@@ -1,7 +1,7 @@
 {
  "what_this_is": "RULING 4's FORWARD BOUND, applied at one batch close: which of the then-previous batch's STATUS.md entries moved to the archive, and the mechanical proof that nothing was lost or altered in transit (#12). Every figure here is computed; none is transcribed (D-431).",
  "generated_by": "tools/audit/gen_status_batch_bound.py",
- "dispatch": "cc_instruction_boot_chain_landing_2026_11_02.md, Task 3",
+ "dispatch": "cc_instruction_records_landing_2026_11_07.md, Task 3",
  "★_every_previous_aiming_of_this_tool_kept_rather_than_replaced": [
   {
    "executing_act": "cc_instruction_preparation_sixth.md, Task 1",
@@ -801,46 +801,44 @@
    "base_commit": "3dbade755a80520af21db8618d6e8ece5d923c07",
    "the_then_previous_batch": "cc_instruction_per_session_reading_extension_2026_11_02.md",
    "the_kind_of_move": "ordinary"
+  },
+  {
+   "executing_act": "cc_instruction_records_landing_2026_11_07.md, Task 3",
+   "base_commit": "113b2ce680e527e81342d8f79d5acbad281334d7",
+   "the_then_previous_batch": "cc_instruction_boot_chain_landing_2026_11_02.md",
+   "the_kind_of_move": "ordinary"
   }
  ],
  "the_ruling": "Ruling 4 of cowork_rulings_2026_08_17_governing_surface_split.md: an entry is SUPERSEDED the moment a later batch's close exists; the site keeps only the latest batch's entries, and every future batch close moves the then-previous batch's entries in the same act that writes its own.",
- "base_commit": "3dbade755a80520af21db8618d6e8ece5d923c07",
- "the_then_previous_batch": "cc_instruction_per_session_reading_extension_2026_11_02.md",
+ "base_commit": "113b2ce680e527e81342d8f79d5acbad281334d7",
+ "the_then_previous_batch": "cc_instruction_boot_chain_landing_2026_11_02.md",
  "the_kind_of_move": "ordinary",
- "entries_moved": 4,
- "characters_moved": 2377,
+ "entries_moved": 3,
+ "characters_moved": 1867,
  "the_moved": [
   {
    "line_at_base": 8,
-   "characters": 1704,
-   "sha256": "5bff028e24b2960ede3288060a13640885a94b49646668540a0e832ca04b8d03",
+   "characters": 1382,
+   "sha256": "897a897200f6c7fee7e71f69a15e8143a6095f42d356f27d83681ba14b06181d",
    "membership": "names the dispatch",
    "the_one_declared_adjustment_applied": true,
-   "opening": "*2026-11-02 (CC — `records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md`, Task 3, the close. **★★ STEP 4's SECOND DISPAT"
+   "opening": "*2026-11-02 (CC — `records/cc/instructions/cc_instruction_boot_chain_landing_2026_11_02.md`, Task 3, the close. **★★ THE BOOT-CHAIN LANDING: HANDOFF E"
   },
   {
    "line_at_base": 10,
-   "characters": 233,
-   "sha256": "4ce8c791d7305c6381d8ce21800d8bdd8f6ab7688c5218ed005662fde02c6f16",
+   "characters": 244,
+   "sha256": "8b2eb03debd9bfe11d0e74cc24ed7961b4ebc92924e64401034fbd1086d7c17c",
    "membership": "says `Same dispatch`, in the run below the entry that names it",
    "the_one_declared_adjustment_applied": false,
-   "opening": "*2026-11-02 (CC — Same dispatch, Task 2. **THE PER-SESSION READING MEASUREMENT IS EXTENDED BY THREE ADDITIONS AND REGENERATED.** **POINTER** — `record"
+   "opening": "*2026-11-02 (CC — Same dispatch, Task 1. **THE RECORD'S AMENDMENT PARAGRAPH IS INSERTED INTO HANDOFF ENTRY 291 §4 STEP 3**, the wording above it kept."
   },
   {
    "line_at_base": 12,
-   "characters": 228,
-   "sha256": "f049f7171efefd4093eab394efe67ec44c61409fa942570f8fae22b7aadc3dec",
-   "membership": "says `Same dispatch`, in the run below the entry that names it",
-   "the_one_declared_adjustment_applied": false,
-   "opening": "*2026-11-02 (CC — Same dispatch, Task 1. **ONE STALE COMMENT IN THE BOOT-PACK TOOL IS CORRECTED**, its former wording kept. **POINTER** — `records/cc/"
-  },
-  {
-   "line_at_base": 14,
-   "characters": 212,
-   "sha256": "a13f475548e7c9a0a2542e2bdc02a48ed20f80536e1c334cffd30ebdea75afa6",
+   "characters": 241,
+   "sha256": "17a359dd4b913313ee4b91140f9443333c68422999c209766b71a2ca4edbd1ea",
    "membership": "says `Same dispatch`, in the run below the entry that names it",
    "the_one_declared_adjustment_applied": false,
-   "opening": "*2026-11-02 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRY 476 ARE LANDED**, as they stood. **POINTER** — `records/cc/reports/cc_repor"
+   "opening": "*2026-11-02 (CC — Same dispatch, Task 0. **THIS DISPATCH, HANDOFF ENTRIES 477 AND 478 AND THE 2026-11-02 RULING RECORD ARE LANDED**, as they stood. **"
   }
  ],
  "reconciliation": {

~~~~

## 3(c) — `python -I artifact_diffs.py /c/s/MS 113b2ce680e527e81342d8f79d5acbad281334d7 tools/audit/evidence_pin_membership.json` (exit 0)

~~~~
====================================================================================================
ARTIFACT tools/audit/evidence_pin_membership.json
  base 113b2ce680e527e81342d8f79d5acbad281334d7  blob b0c4673afcbb1eb6bfcef132bf5f7491f2064404
  new          blob b0c4673afcbb1eb6bfcef132bf5f7491f2064404
  IDENTICAL
~~~~

## This appendix's own assembler, quoted whole: `build_appendix.py`

~~~~
"""Assemble the report's appendix from scratch printouts, verbatim, each under a heading naming
its command and step. argv[1] = scratch dir; argv[2] = output path."""
import os
import sys

S, OUT = sys.argv[1], sys.argv[2]
SECTIONS = [
    ("Start state, before Task 0 — `python tools/audit/gen_per_session_reading.py --check` (exit 2)",
     "boot_per_session_check.txt"),
    ("Start state, before Task 0 — `python tools/audit/gen_evidence_pin_membership.py --check` (exit 1)",
     "boot_evidence_pin_check.txt"),
    ("0(c) / A1 — `python tools/audit/changed_paths.py` (exit 0), whole", "a1_enumeration.txt"),
    ("0(c) — the count script, quoted whole: `landing_set_check.py`", "landing_set_check.py"),
    ("0(c) — `python -I landing_set_check.py a1_enumeration.txt landing_paths.txt` (exit 0), output",
     "landing_set_check_out.txt"),
    ("0(d) — the last-bytes script, quoted whole: `last_bytes_check.py`", "last_bytes_check.py"),
    ("0(d) — `python -I last_bytes_check.py /c/s/MS landing_paths.txt` (exit 0), output: every "
     "file's blob, size, zero-byte count, last 70 bytes and final-line tail", "last_bytes_out.txt"),
    ("0(e) — `python tools/audit/gen_evidence_pin_membership.py --check` before (exit 1)",
     "t0_ep_check1.txt"),
    ("0(e) — `python tools/audit/gen_evidence_pin_membership.py` (write, exit 0)", "t0_ep_write.txt"),
    ("0(e) — `python tools/audit/gen_evidence_pin_membership.py --check` after (exit 0)",
     "t0_ep_check2.txt"),
    ("0(e) — `git diff c9aa4e8563dd7c8ef03780c8bf562e324e5c4db7 b0c4673afcbb1eb6bfcef132bf5f7491f2064404` "
     "(the artifact's blob at the start tip against the new blob)", "t0_ep_diff.txt"),
    ("0(e) — the pathspec file fed to `git add --pathspec-from-file`, quoted whole", "t0_pathspec.txt"),
    ("0(e) — `python tools/audit/changed_paths.py --staged` (exit 0), whole", "t0_staged.txt"),
    ("0(e) — `git push origin master` (exit 0)", "t0_push.txt"),
    ("0(f) — the opening capture: `python tools/audit/gen_guard_state.py --check` (exit 1), whole",
     "cap_opening.txt"),
    ("0(f) — `python tools/audit/gen_guard_classification.py --check` (exit 2)", "t0_classification.txt"),
    ("3(b) — `python tools/audit/gen_status_batch_bound.py --apply` (exit 0)", "t3_apply.txt"),
    ("3(b) — `python tools/audit/gen_status_batch_bound.py --check` (exit 0)", "t3_bound_check.txt"),
    ("3(b) — `python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md` (exit 0)",
     "t3_split_check.txt"),
    ("3(b) — `python tools/audit/gen_status_residue_move.py --check` (exit 0)", "t3_residue_check.txt"),
    ("3(b) — `python tools/audit/gen_status_archive_pass.py --check` (exit 0)", "t3_archive_pass_check.txt"),
    ("3(c)1 — `python tools/audit/gen_evidence_pin_membership.py --check` (exit 0)", "t3c_ep_check.txt"),
    ("3(c)2 — `python tools/audit/gen_session_start_read_size.py --check` before (exit 1)",
     "t3c_ssrs_check1.txt"),
    ("3(c)2 — `python tools/audit/gen_session_start_read_size.py` (write, exit 0)", "t3c_ssrs_write.txt"),
    ("3(c)2 — `python tools/audit/gen_session_start_read_size.py --check` after (exit 0)",
     "t3c_ssrs_check2.txt"),
    ("3(c)2 — `python tools/audit/gen_defense_share.py --check` before (exit 1)", "t3c_ds_check1.txt"),
    ("3(c)2 — `python tools/audit/gen_defense_share.py` (write, exit 0)", "t3c_ds_write.txt"),
    ("3(c)2 — `python tools/audit/gen_defense_share.py --check` after (exit 0)", "t3c_ds_check2.txt"),
    ("3(c)3 — `python tools/audit/gen_l3_outgoing_population.py --check` before (exit 1)",
     "t3c_l3_check1.txt"),
    ("3(c)3 — `python tools/audit/gen_l3_outgoing_population.py` (write, exit 0)", "t3c_l3_write.txt"),
    ("3(c)3 — `python tools/audit/gen_l3_outgoing_population.py --check` after (exit 0)",
     "t3c_l3_check2.txt"),
    ("3(c)3 — `python tools/audit/gen_l0_l1_outgoing_population.py --check` (exit 0; not regenerated)",
     "t3c_l0l1_check1.txt"),
    ("3(c)4 — `python tools/audit/gen_derivation_boot_pack.py --check` (exit 0; not regenerated)",
     "t3c_dbp_check.txt"),
    ("3(c)5 — `python tools/audit/gen_per_session_reading.py --check` before (exit 1)", "t3c_psr_check1.txt"),
    ("3(c)5 — `python tools/audit/gen_per_session_reading.py` (write, exit 0)", "t3c_psr_write.txt"),
    ("3(c)5 — `python tools/audit/gen_per_session_reading.py --check` after (exit 0)", "t3c_psr_check2.txt"),
    ("3(c) — `python tools/audit/changed_paths.py` after the regenerations (exit 0), whole",
     "t3c_changed.txt"),
    ("3(c) — the diff script, quoted whole: `artifact_diffs.py` (as run; the first run stopped on a "
     "console-encoding error before any diff printed, and `sys.stdout.reconfigure` was added)",
     "artifact_diffs.py"),
    ("3(c) — `python -I artifact_diffs.py /c/s/MS 864deb43c5dae6415a8c8b9e98901e7b2c2a96ae "
     "tools/audit/session_start_read_size.json tools/audit/defense_share.json "
     "tools/audit/l3_outgoing_population.json tools/audit/per_session_reading.json "
     "tools/audit/status_batch_bound.json` (exit 0), whole", "t3c_diffs.txt"),
    ("3(c) — `python -I artifact_diffs.py /c/s/MS 113b2ce680e527e81342d8f79d5acbad281334d7 "
     "tools/audit/evidence_pin_membership.json` (exit 0)", "t3c_diff_ep.txt"),
    ("This appendix's own assembler, quoted whole: `build_appendix.py`", "build_appendix.py"),
]

parts = [
    "# Appendix — the raw printouts of the records landing of 2026-11-07\n\n",
    "Beside `records/cc/reports/cc_report_records_landing_2026_11_07.md`, under Ruling 4 of "
    "`records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`. Every block below "
    "is a printout copied verbatim from the scratch file the command wrote, under a heading naming the "
    "command and the step. Nothing here is needed to read the report proper. The scratch scripts ran "
    "outside the repository with `python -I`; the 3(c′) run and Task 4's capture are not here — they are "
    "in this batch's section of `records/cowork/handoff/cowork_away_returns.md`.\n\n",
]
for heading, name in SECTIONS:
    with open(os.path.join(S, name), encoding="utf-8") as f:
        text = f.read()
    if not text.endswith("\n"):
        text += "\n"
    parts.append("## %s\n\n~~~~\n%s~~~~\n\n" % (heading, text if text.strip() else "(no output)\n"))
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("".join(parts).rstrip("\n") + "\n")
print("wrote %s" % OUT)
~~~~
