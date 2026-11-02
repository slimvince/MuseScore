# Appendix — raw printouts of the per-session reading extension batch (2026-11-02)

> The appendix of `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md`, under Ruling 4 of
> `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`. Every printout below is verbatim,
> copied from the scratch file the command wrote, each under a heading naming its command and step. Nothing the
> report proper needs is only here.

## A1 — 0(c) — `python tools/audit/changed_paths.py`, the A1 enumeration, whole

`t0c_changed_paths.txt`:

```
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_six.md
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
396 changed path record(s) [worktree]
```

## A2 — 0(d) — the last-bytes check: the scratch script `t0d_last_bytes.py`, then its output

`t0d_last_bytes.py`:

```
"""0(d): write each landing file as a blob --no-filters, read the blob back, report its size,
its last bytes, whether it ends with a newline after a complete line, and its zero-byte count."""
import subprocess

ROOT = r"C:\s\MS"
PATHS = [
    "records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md",
    "records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_six.md",
]
for p in PATHS:
    blob = subprocess.run(["git", "-C", ROOT, "hash-object", "-w", "--no-filters", p],
                          capture_output=True, text=True, check=True).stdout.strip()
    data = subprocess.run(["git", "-C", ROOT, "cat-file", "blob", blob],
                          capture_output=True, check=True).stdout
    size = int(subprocess.run(["git", "-C", ROOT, "cat-file", "-s", blob],
                              capture_output=True, text=True, check=True).stdout.strip())
    ends_nl = data.endswith(b"\n")
    complete = ends_nl and not data.endswith(b"\n\n") and len(data) > 1
    print(p)
    print("  blob %s  size %d (len %d)" % (blob, size, len(data)))
    print("  last 40 bytes %r" % data[-40:])
    print("  ends with a newline after a complete line: %s" % complete)
    print("  zero bytes: %d" % data.count(b"\x00"))
```

`t0d_out.txt`:

```
records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md
  blob 20968a55882b17b5a75fc84882ff2647dc6a063c  size 64133 (len 64133)
  last 40 bytes b'\xb2) forbids it and Task 4 would show it.\n'
  ends with a newline after a complete line: True
  zero bytes: 0
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_six.md
  blob adae534aa0369663b06fb48f71d651ae59294e62  size 8632 (len 8632)
  last 40 bytes b'ion; "narrow"; "continue"; "continue".*\n'
  ends with a newline after a complete line: True
  zero bytes: 0
```

## A3 — 0(e) — `python tools/audit/gen_evidence_pin_membership.py --check`

`t0e_evpin.txt`:

```
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 171
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

## A4 — 0(f) — THE OPENING CAPTURE, `python tools/audit/gen_guard_state.py --check`, whole

`cap0_opening.txt`:

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
```

## A5 — 0(f) — the start tip's `guard_state.json` summary against the opening capture: the scratch script `t0f_summary.py`, then its output (its set difference compares invocations without their arguments on one side; the summary line carries both)

`t0f_summary.py`:

```
"""0(f): the start tip's guard_state.json summary and its failing set, compared with a capture."""
import json
import re
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
print("summary:", json.dumps(state.get("summary"), ensure_ascii=False))
failing = set()
def walk(o):
    if isinstance(o, dict):
        v = o.get("verdict") or o.get("status")
        inv = o.get("invocation") or o.get("command") or o.get("tool")
        if isinstance(v, str) and v.upper() == "FAIL" and isinstance(inv, (str, list)):
            failing.add(inv if isinstance(inv, str) else " ".join(inv))
        for x in o.values():
            walk(x)
    elif isinstance(o, list):
        for x in o:
            walk(x)
walk(state)
print("failing in the start tip's state (%d):" % len(failing))
for f in sorted(failing):
    print("  ", f)
cap = [l.strip() for l in open(sys.argv[2], encoding="utf-8") if l.strip().startswith("[FAIL]")]
capset = {re.sub(r"^\[FAIL\]\s*", "", l).strip() for l in cap}
print("failing in the capture (%d):" % len(capset))
for f in sorted(capset):
    print("  ", f)
norm = lambda s: " ".join(s.split())
a = {norm(x) for x in failing}
b = {norm(x) for x in capset}
print("capture minus start tip:", sorted(b - a))
print("start tip minus capture:", sorted(a - b))
```

`t0f_summary_out.txt`:

```
summary: {"run": 83, "passing": 70, "failing": 13, "failing_tools": [{"tool": "tools/audit/gen_phase3_gate_partition.py", "args": ["--check"]}, {"tool": "tools/audit/gen_filing_convention_application.py", "args": ["--check"]}, {"tool": "tools/audit/gen_artifact_inventory.py", "args": ["--check"]}, {"tool": "tools/audit/gen_artifact_inventory_surface.py", "args": ["--check"]}, {"tool": "tools/audit/gen_test_construction_evidence.py", "args": ["--check"]}, {"tool": "tools/audit/gen_retirement_caller_check.py", "args": ["--check"]}, {"tool": "tools/audit/decisions/apply_soft_discard.py", "args": ["--check"]}, {"tool": "tools/audit/decisions/apply_residue_discard.py", "args": ["--check"]}, {"tool": "tools/audit/gen_epoch_write_path.py", "args": ["--check"]}, {"tool": "tools/audit/gen_recognizer_establishment_sort.py", "args": ["--check"]}, {"tool": "tools/audit/decisions/gen_cluster_dispositions.py", "args": ["--verify"]}, {"tool": "tools/audit/decisions/gen_home_classification.py", "args": ["--check"]}, {"tool": "tools/audit/decisions/gen_phase1p_delegation_bar.py", "args": ["--check"]}], "not_run": 4, "historical_records": 20}
failing in the start tip's state (13):
   tools/audit/decisions/apply_residue_discard.py
   tools/audit/decisions/apply_soft_discard.py
   tools/audit/decisions/gen_cluster_dispositions.py
   tools/audit/decisions/gen_home_classification.py
   tools/audit/decisions/gen_phase1p_delegation_bar.py
   tools/audit/gen_artifact_inventory.py
   tools/audit/gen_artifact_inventory_surface.py
   tools/audit/gen_epoch_write_path.py
   tools/audit/gen_filing_convention_application.py
   tools/audit/gen_phase3_gate_partition.py
   tools/audit/gen_recognizer_establishment_sort.py
   tools/audit/gen_retirement_caller_check.py
   tools/audit/gen_test_construction_evidence.py
failing in the capture (14):
   tools/audit/decisions/apply_residue_discard.py --check
   tools/audit/decisions/apply_soft_discard.py --check
   tools/audit/decisions/gen_cluster_dispositions.py --verify
   tools/audit/decisions/gen_home_classification.py --check
   tools/audit/decisions/gen_phase1p_delegation_bar.py --check
   tools/audit/gen_artifact_inventory.py --check
   tools/audit/gen_artifact_inventory_surface.py --check
   tools/audit/gen_epoch_write_path.py --check
   tools/audit/gen_filing_convention_application.py --check
   tools/audit/gen_per_session_reading.py --check
   tools/audit/gen_phase3_gate_partition.py --check
   tools/audit/gen_recognizer_establishment_sort.py --check
   tools/audit/gen_retirement_caller_check.py --check
   tools/audit/gen_test_construction_evidence.py --check
capture minus start tip: ['tools/audit/decisions/apply_residue_discard.py --check', 'tools/audit/decisions/apply_soft_discard.py --check', 'tools/audit/decisions/gen_cluster_dispositions.py --verify', 'tools/audit/decisions/gen_home_classification.py --check', 'tools/audit/decisions/gen_phase1p_delegation_bar.py --check', 'tools/audit/gen_artifact_inventory.py --check', 'tools/audit/gen_artifact_inventory_surface.py --check', 'tools/audit/gen_epoch_write_path.py --check', 'tools/audit/gen_filing_convention_application.py --check', 'tools/audit/gen_per_session_reading.py --check', 'tools/audit/gen_phase3_gate_partition.py --check', 'tools/audit/gen_recognizer_establishment_sort.py --check', 'tools/audit/gen_retirement_caller_check.py --check', 'tools/audit/gen_test_construction_evidence.py --check']
start tip minus capture: ['tools/audit/decisions/apply_residue_discard.py', 'tools/audit/decisions/apply_soft_discard.py', 'tools/audit/decisions/gen_cluster_dispositions.py', 'tools/audit/decisions/gen_home_classification.py', 'tools/audit/decisions/gen_phase1p_delegation_bar.py', 'tools/audit/gen_artifact_inventory.py', 'tools/audit/gen_artifact_inventory_surface.py', 'tools/audit/gen_epoch_write_path.py', 'tools/audit/gen_filing_convention_application.py', 'tools/audit/gen_phase3_gate_partition.py', 'tools/audit/gen_recognizer_establishment_sort.py', 'tools/audit/gen_retirement_caller_check.py', 'tools/audit/gen_test_construction_evidence.py']
```

## A6 — 0(f) — `python tools/audit/gen_guard_classification.py --check` (exit 2)

`t0f_classification.txt`:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_per_session_reading.py', 'tools/audit/gen_withheld_family_reading.py']
```

## A7 — Every capture comparison — the scratch script `cmp_captures.py`

`cmp_captures.py`:

```
"""Compare two full guard captures verdict by verdict: every tool's PASS / FAIL / NOT RUN /
HISTORICAL line side by side, the header and the tally line."""
import re
import sys

LINE = re.compile(r"^\s*\[(PASS|FAIL|NOT RUN|HISTORICAL)\]\s+(.*?)\s*$")


def load(path):
    header, tally, verdicts, order = None, None, {}, []
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        m = LINE.match(line)
        if m:
            key = " ".join(m.group(2).split())
            if key in verdicts:
                key = key + " #%d" % sum(1 for k in order if k.startswith(key))
            verdicts[key] = m.group(1)
            order.append(key)
        elif "guard(s) run" in line:
            tally = line.strip()
        elif line.strip() and header is None:
            header = line.strip()
    return header, tally, verdicts, order


a_h, a_t, a_v, a_o = load(sys.argv[1])
b_h, b_t, b_v, b_o = load(sys.argv[2])
print("A:", sys.argv[1])
print("B:", sys.argv[2])
print("header A:", a_h)
print("header B:", b_h)
print("tally A:", a_t)
print("tally B:", b_t)
keys = a_o + [k for k in b_o if k not in a_v]
diff = 0
for k in keys:
    va, vb = a_v.get(k, "(absent)"), b_v.get(k, "(absent)")
    if va != vb:
        diff += 1
        print("DIFFERS: %s : %s -> %s" % (k, va, vb))
print("verdicts compared %d, differing %d; header same %s; tally same %s"
      % (len(keys), diff, a_h == b_h, a_t == b_t))
```

## A8 — 1(a) — `python tools/audit/gen_derivation_boot_pack.py --check`, before the edit

`t1a_bootpack_before.txt`:

```
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
```

## A9 — 1(c) — `python tools/audit/gen_derivation_boot_pack.py --check`, after the edit (byte-identical to A8 by `cmp`)

`t1c_bootpack_after.txt`:

```
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
```

## A10 — 1(c) — the capture after Task 1, `python tools/audit/gen_guard_state.py --check`, whole

`cap1_after_task1.txt`:

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
```

## A11 — 1(c) — the opening capture against the capture after Task 1

`cmp_cap0_cap1.txt`:

```
A: cap0_opening.txt
B: cap1_after_task1.txt
header A: STALE vs the run: guard_state.json does not re-derive
header B: STALE vs the run: guard_state.json does not re-derive
tally A: 83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
tally B: 83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
verdicts compared 107, differing 0; header same True; tally same True
```

## A12 — 2(a) — `python tools/audit/gen_per_session_reading.py` (write mode), the tool as it stood

`t2a_write.txt`:

```
wrote tools/audit/per_session_reading.json
  the ordinary session-start read (imported) 237676
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674763
  Cowork, per sitting, in the shape of the sitting of entry 461: 973582
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
```

## A13 — 2(a) — `python tools/audit/gen_per_session_reading.py --check`

`t2a_check.txt`:

```
the per-session reading measurement re-derives
  the ordinary session-start read (imported) 237676
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674763
  Cowork, per sitting, in the shape of the sitting of entry 461: 973582
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
```

## A14 — 2(b) — `git diff` of the tool's `<T1>` blob `851f98ec…` against the extended blob `6d3f308c…`

`t2b_tool_diff.txt`:

```
diff --git a/851f98ec4c1a01be133731e56bc01e5f43acf56f b/6d3f308c889e7ec6a1ab58b98f4eef0acee8bea4
index 851f98ec4c..6d3f308c88 100644
--- a/851f98ec4c1a01be133731e56bc01e5f43acf56f
+++ b/6d3f308c889e7ec6a1ab58b98f4eef0acee8bea4
@@ -23,6 +23,16 @@ WHAT IT IS.  One artifact, `per_session_reading.json`, carrying two tables.
   the IMPORTED defense-share measurement; and, by text hash, the sub-blocks earlier sittings
   already settled, so that nobody re-proposes them.
 
+AND, SINCE 2026-11-02, THREE ADDITIONS (`cc_instruction_per_session_reading_extension_2026_11_02.md`,
+Task 2 — step 4's second dispatch).  (1) THE INVARIANT SHARE: for each dispatch and each report of the
+arc, the characters on lines it shares with its predecessor (the member before it in the population's
+own order), matched line for line with line endings, order ignored, whitespace-only lines apart — the
+figure the dispatch-form question waits for (handoff entry 464 §1).  (2) THE APPENDIX FILE BESIDE A
+REPORT: under Ruling 4 of the 2026-11-01 record a report's raw printouts stand in `<stem>_appendix.md`
+beside it; appendix files leave the populations, are sized beside their reports, and every report of
+the folder with one is listed with both sizes.  (3) RULING 2's AFTER-FIGURE: the Claude Code side's
+per-batch total with the six spans' file-tool read replaced by the injected copy.
+
 WHY IT EXISTS.  The user's instruction of 2026-10-31, in his words: *"After group 5, together with
 the member's feet and closing sections is a natural break: plan a pruning iteration (shrink the
 context occupied every session by mandatory reading ), then continue."*  The plan the writing side
@@ -102,6 +112,7 @@ THE STOPS — each raised as `Stop`, printed as `STOP: …`, exit 2:
   * a boot-chain anchor found other than exactly once, or the closing opener standing before the
     opening one;
   * a dispatch, a report or a handoff entry of a derived population with no add-commit;
+  * an appendix file of the reports folder with no report beside it;
   * the imported measurement's total disagreeing with its own committed artifact at the tree;
   * the defense-share denominator disagreeing with the reader's six-span total.
 
@@ -124,6 +135,7 @@ import os
 import re
 import subprocess
 import sys
+from collections import Counter
 
 HERE = os.path.dirname(os.path.abspath(__file__))
 ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
@@ -191,6 +203,7 @@ DISPATCH_FOLDER = "records/cc/instructions"
 DISPATCH_PREFIX = "cc_instruction_l3_comparison_tabulation_"
 REPORT_FOLDER = "records/cc/reports"
 REPORT_PREFIX = "cc_report_l3_comparison_tabulation_"
+APPENDIX_SUFFIX = "_appendix.md"      # Ruling 4 of the 2026-11-01 record: `<stem>_appendix.md` beside `<stem>.md`
 
 DERIVATION_PATH = "cowork_blind_derivation_l3_2026_10_17.md"
 SETTLED_SOURCES = (
@@ -345,7 +358,7 @@ def population_rows(folder: str, prefix: str, commits: dict, sized: bool = True)
     is a STOP. Ordered by (time, name)."""
     rows = []
     for name in sorted(os.listdir(os.path.join(ROOT, folder))):
-        if not name.startswith(prefix):
+        if not name.startswith(prefix) or name.endswith(APPENDIX_SUFFIX):
             continue
         path = folder + "/" + name
         if path not in commits:
@@ -372,6 +385,74 @@ def population_summary(rows: list[dict], latest: int, latest_field: str) -> dict
     }
 
 
+# ── the appendix beside a report (Ruling 4 of the 2026-11-01 record) ────────────────────────────
+def pair_appendices(names: list[str]) -> dict[str, str]:
+    """Every appendix file among `names`, keyed by the report it stands beside: the report of
+    `<stem>_appendix.md` is `<stem>.md`. An appendix with no report beside it is a STOP."""
+    present = set(names)
+    pairs = {}
+    for name in sorted(names):
+        if not name.endswith(APPENDIX_SUFFIX):
+            continue
+        report = name[:-len(APPENDIX_SUFFIX)] + ".md"
+        if report not in present:
+            raise Stop("an appendix file has no report beside it: %s" % name)
+        pairs[report] = name
+    return pairs
+
+
+# ── the invariant share: what a member shares line for line with its predecessor ───────────────
+def shared_with_predecessor(text: str, previous: str) -> dict:
+    """The characters of `text` on lines that also stand in `previous`, matched line for line with
+    their line endings, each line of `previous` matched at most once, order ignored.
+    Whitespace-only lines are counted apart and are not in the share."""
+    available = Counter(previous.splitlines(keepends=True))
+    shared = blank = 0
+    for line in text.splitlines(keepends=True):
+        if available[line] > 0:
+            available[line] -= 1
+            if line.strip():
+                shared += len(line)
+            else:
+                blank += len(line)
+    return {
+        "characters": len(text),
+        "characters_on_lines_shared_with_the_predecessor": shared,
+        "characters_on_whitespace_only_lines_shared_and_not_counted_above": blank,
+        "share_percent": round(100.0 * shared / len(text), 2) if text else 0.0,
+    }
+
+
+def invariant_shares(folder: str, rows: list[dict]) -> dict:
+    """Each member of a derived population against the member before it in the population's own
+    order (add-commit time, then name). The first member has no predecessor."""
+    previous_name = previous_text = None
+    shared_total = own_total = 0
+    for row in rows:
+        text = read(folder + "/" + row["name"])
+        if previous_text is None:
+            row["the_predecessor"] = None
+            row["shared_with_the_predecessor"] = None
+        else:
+            s = shared_with_predecessor(text, previous_text)
+            row["the_predecessor"] = previous_name
+            row["shared_with_the_predecessor"] = s
+            shared_total += s["characters_on_lines_shared_with_the_predecessor"]
+            own_total += s["characters"]
+        previous_name, previous_text = row["name"], text
+    return {
+        "members_with_a_predecessor": max(len(rows) - 1, 0),
+        "their_characters": own_total,
+        "their_characters_on_lines_shared_with_the_predecessor": shared_total,
+        "share_percent": round(100.0 * shared_total / own_total, 2) if own_total else 0.0,
+        "how_a_line_is_shared": "a line of the member, with its line ending, counts as shared when "
+                                "the predecessor holds the same line not already matched; the order "
+                                "of lines is ignored; whitespace-only lines are counted apart and are "
+                                "not in the share. A line changed by one character counts as not "
+                                "shared, and a short common line counts as shared wherever it stands.",
+    }
+
+
 # ── table 2: the six spans, partitioned ─────────────────────────────────────────────────────────
 def normalized_opening(text: str) -> str:
     """The whitespace-collapsed opening the settled-span artifacts publish — the same normalization
@@ -627,6 +708,25 @@ def build() -> dict:
     for r in latest_entries:
         r["characters"] = len(read(HANDOFF_FOLDER + "/" + r["name"]))
 
+    dispatch_shares = invariant_shares(DISPATCH_FOLDER, dispatch_rows)
+    report_shares = invariant_shares(REPORT_FOLDER, report_rows)
+    appendix_pairs = pair_appendices(sorted(os.listdir(os.path.join(ROOT, REPORT_FOLDER))))
+    for row in report_rows:
+        beside = appendix_pairs.get(row["name"])
+        row["the_appendix_beside_it"] = (
+            {"name": beside, "characters": len(read(REPORT_FOLDER + "/" + beside))} if beside else None)
+    reports_with_an_appendix = []
+    for report, beside in sorted(appendix_pairs.items()):
+        proper = len(read(REPORT_FOLDER + "/" + report))
+        appendix = len(read(REPORT_FOLDER + "/" + beside))
+        reports_with_an_appendix.append({
+            "the_report": report,
+            "characters_of_the_report_proper": proper,
+            "the_appendix": beside, "characters_of_the_appendix": appendix,
+            "the_appendix_share_of_the_two_percent":
+                round(100.0 * appendix / (proper + appendix), 2) if proper + appendix else 0.0,
+        })
+
     the_dispatches = {
         "the_folder": DISPATCH_FOLDER, "the_name_prefix": DISPATCH_PREFIX,
         "read_by": "Claude Code, per batch (its own dispatch, whole); Cowork, per sitting that "
@@ -639,6 +739,7 @@ def build() -> dict:
                                        "previous dispatch",
     }
     the_dispatches.update(population_summary(dispatch_rows, 5, "the_last_five"))
+    the_dispatches["the_invariant_share"] = dispatch_shares
     the_reports = {
         "the_folder": REPORT_FOLDER, "the_name_prefix": REPORT_PREFIX,
         "read_by": "Cowork, per sitting (whole); Claude Code, per batch (at the portions its "
@@ -648,6 +749,16 @@ def build() -> dict:
                                        "read in full — carried in the handoff entries (entry 461 §4)",
     }
     the_reports.update(population_summary(report_rows, 3, "the_last_three"))
+    the_reports["the_invariant_share"] = report_shares
+    the_reports["the_appendices_beside_them"] = {
+        "count": sum(1 for r in report_rows if r["the_appendix_beside_it"]),
+        "characters_total": sum(r["the_appendix_beside_it"]["characters"]
+                                for r in report_rows if r["the_appendix_beside_it"]),
+        "how_these_relate_to_the_sizes_above": "every size above is of the report proper only; an "
+                                               "appendix file is sized here and in "
+                                               "`the_reports_with_an_appendix_beside_them`, never "
+                                               "added to the report's own size",
+    }
 
     chain_record = ("the writing side's own boot instruction — entry 291 §4 step 3 and entry 169's "
                     "Boot block; no user ruling names these reads")
@@ -715,6 +826,12 @@ def build() -> dict:
             "without_the_injected_copy_of_CLAUDE_md": cc_without,
             "with_it": cc_without + whole,
             "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, %d characters" % whole,
+            "under_ruling_2_of_2026_11_01": cc_without + whole - six,
+            "how_ruling_2_moves_it": "Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_"
+                                     "pruning_iteration_sitting.md`: the injected copy is the read of "
+                                     "the six spans, so their file-tool read (%d characters) leaves the "
+                                     "sum and the injected copy stays; the eight-line check's own reads "
+                                     "are not sized here" % six,
             "left_out_and_said_so": "the previous report at the portions a dispatch orders, the "
                                     "reading file at its ordered portions, the ruling records a "
                                     "dispatch orders — varies per dispatch and is not sized here",
@@ -745,8 +862,10 @@ def build() -> dict:
             "text, gives no span a fate, proposes nothing and decides nothing. Every value is "
             "computed; none is transcribed (D-431).",
         "generated_by": "tools/audit/gen_per_session_reading.py",
-        "generated_for": "cc_instruction_per_session_reading_measurement_2026_11_01.md, Task 1 — "
-                         "step 1 of the pruning iteration the user ordered on 2026-10-31",
+        "generated_for": "cc_instruction_per_session_reading_extension_2026_11_02.md, Task 2 — step 4's "
+                         "second dispatch of the pruning iteration the user ordered on 2026-10-31; "
+                         "first built for step 1 (cc_instruction_per_session_reading_measurement_"
+                         "2026_11_01.md, Task 1)",
         "the_four_mandate_classes": MANDATE_CLASSES,
         "how_a_size_is_counted":
             "a whole file is `len(text)` of the file read by the imported `at_tree` (UTF-8, universal "
@@ -772,6 +891,20 @@ def build() -> dict:
             "the_further_members": further,
             "the_arc_dispatches": the_dispatches,
             "the_arc_reports": the_reports,
+            "the_reports_with_an_appendix_beside_them": {
+                "the_folder": REPORT_FOLDER,
+                "how_a_pair_is_found": "every file of the folder whose name ends `%s`, beside the report "
+                                       "named by its stem; an appendix with no report beside it is a "
+                                       "STOP" % APPENDIX_SUFFIX,
+                "read_by": "Cowork: the report proper in full under the user's rule of 2026-09-03, the "
+                           "appendix at need (Ruling 4 of the 2026-11-01 record)",
+                "count": len(reports_with_an_appendix),
+                "characters_of_the_reports_proper": sum(r["characters_of_the_report_proper"]
+                                                        for r in reports_with_an_appendix),
+                "characters_of_the_appendices": sum(r["characters_of_the_appendix"]
+                                                    for r in reports_with_an_appendix),
+                "the_pairs": reports_with_an_appendix,
+            },
             "the_cowork_boot_chain": boot_chain,
             "totals_by_side": totals_by_side,
         },
@@ -807,6 +940,10 @@ def build() -> dict:
             "The injected copy of `CLAUDE.md` is DECLARED by the executing sessions; this tool "
             "measures the file, not the copy.",
             "The dispatch and report populations are complete only relative to their name prefixes.",
+            "The invariant share is a LINE measure, not a judgement of copying: a line changed by one "
+            "character counts as not shared, and a short common line counts as shared wherever it "
+            "stands. It compares each member with its predecessor only.",
+            "An appendix file is found by its name alone (`<stem>_appendix.md` beside `<stem>.md`).",
             "The imported recognizers are patterns over prose whose reach is UNMEASURED (D-673 "
             "applies: no analysis decision consumes this enumeration); the doubt default places "
             "what no recognizer places; and a sub-block cut at a ★ marker may carry a sentence that "
@@ -817,6 +954,8 @@ def build() -> dict:
             "That any mandate class is right.",
             "That the injected copy of `CLAUDE.md` exists or has the size of the file.",
             "That the dispatch and report populations are complete beyond the name prefixes.",
+            "That a line shared with the predecessor was copied from it, or that a line not shared "
+            "was newly written.",
             "That any sub-block's class is right.",
             "That any size is small or large enough — that is the user's question at step 3.",
             "That any text should move — this tool proposes nothing.",
@@ -846,6 +985,12 @@ def main(argv: list[str]) -> int:
     print("  arc dispatches %d, %d characters; arc reports %d, %d characters"
           % (t1["the_arc_dispatches"]["count"], t1["the_arc_dispatches"]["characters_total"],
              t1["the_arc_reports"]["count"], t1["the_arc_reports"]["characters_total"]))
+    print("  invariant share: dispatches %.2f %%, reports %.2f %%"
+          % (t1["the_arc_dispatches"]["the_invariant_share"]["share_percent"],
+             t1["the_arc_reports"]["the_invariant_share"]["share_percent"]))
+    ap = t1["the_reports_with_an_appendix_beside_them"]
+    print("  reports with an appendix beside them %d: reports proper %d, appendices %d characters"
+          % (ap["count"], ap["characters_of_the_reports_proper"], ap["characters_of_the_appendices"]))
     for name, side in t1["totals_by_side"].items():
         value = side.get("without_the_injected_copy_of_CLAUDE_md", side.get("characters"))
         print("  %s: %d" % (name, value))
```

## A15 — 2(c) — the planted-fault proofs: the scratch script `t2c_proofs.py`, then its output

`t2c_proofs.py`:

```
"""2(c): the planted-fault proofs P1 to P8 of the extended per-session reading tool. Puts
tools/audit on the path, imports the tool as a module, calls its functions on literal inputs
(P1 to P6) and reads the regenerated artifact (P7, P8). Each proof prints PASS or FAIL with
its values."""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\s\MS"
sys.path.insert(0, os.path.join(ROOT, "tools", "audit"))
import gen_per_session_reading as t  # noqa: E402

results = []


def report(name, ok, values):
    results.append(ok)
    print("%s %s — %s" % (name, "PASS" if ok else "FAIL", values))


# P1 — a hand-counted case
r = t.shared_with_predecessor("a\nb\nb\n\nc", "b\nx\na\n\n")
report("P1", r["characters"] == 8
       and r["characters_on_lines_shared_with_the_predecessor"] == 4
       and r["characters_on_whitespace_only_lines_shared_and_not_counted_above"] == 1
       and r["share_percent"] == 50.0, r)

# P2 — identity
r = t.shared_with_predecessor("x\ny\n", "x\ny\n")
report("P2", r["characters_on_lines_shared_with_the_predecessor"] == 4
       and r["share_percent"] == 100.0, r)

# P3 — nothing before, and nothing at all
r1 = t.shared_with_predecessor("x\ny\n", "")
r2 = t.shared_with_predecessor("", "x\n")
report("P3", r1["characters_on_lines_shared_with_the_predecessor"] == 0
       and r1["share_percent"] == 0.0 and r2["characters"] == 0 and r2["share_percent"] == 0.0,
       {"first": r1, "second": r2})

# P4 — a planted one-character change
r = t.shared_with_predecessor("abc\ndef\n", "abc\ndeF\n")
report("P4", r["characters_on_lines_shared_with_the_predecessor"] == 4
       and r["share_percent"] == 50.0, r)

# P5 — the planted orphan
try:
    out = t.pair_appendices(["r_x.md", "r_x_appendix.md", "r_y_appendix.md"])
    report("P5", False, "no Stop raised; returned %r" % out)
except t.Stop as exc:
    report("P5", "r_y_appendix.md" in str(exc), "Stop: %s" % exc)

# P6 — the pairing
out = t.pair_appendices(["r_x.md", "r_x_appendix.md", "r_z.md"])
report("P6", out == {"r_x.md": "r_x_appendix.md"}, out)

# P7 and P8 — at the tree, from the regenerated artifact
art = json.load(open(os.path.join(ROOT, "tools", "audit", "per_session_reading.json"),
                     encoding="utf-8"))
t1 = art["table_1_the_per_session_reading"]
p7_ok = True
p7_vals = {}
for field in ("the_arc_dispatches", "the_arc_reports"):
    pop = t1[field]["the_population"]
    appendix_names = [m["name"] for m in pop if m["name"].endswith("_appendix.md")]
    first_ok = pop[0]["the_predecessor"] is None and pop[0]["shared_with_the_predecessor"] is None
    chain_ok = all(pop[i]["the_predecessor"] == pop[i - 1]["name"] for i in range(1, len(pop)))
    shared_ok = all(isinstance(pop[i]["shared_with_the_predecessor"], dict)
                    for i in range(1, len(pop)))
    p7_vals[field] = {"members": len(pop), "appendix_names": appendix_names,
                      "first_has_no_predecessor": first_ok,
                      "every_other_predecessor_is_the_member_before": chain_ok,
                      "every_other_carries_a_share": shared_ok}
    p7_ok = p7_ok and not appendix_names and first_ok and chain_ok and shared_ok
report("P7", p7_ok, p7_vals)

ap = t1["the_reports_with_an_appendix_beside_them"]
expected = {
    "cc_report_pruning_rulings_execution_2026_11_01.md":
        "cc_report_pruning_rulings_execution_2026_11_01_appendix.md",
    "cc_report_pruning_rulings_reexecution_2026_11_01.md":
        "cc_report_pruning_rulings_reexecution_2026_11_01_appendix.md",
    "cc_report_pruning_rulings_third_execution_2026_11_01.md":
        "cc_report_pruning_rulings_third_execution_2026_11_01_appendix.md",
    "cc_report_pruning_rulings_fourth_execution_2026_11_02.md":
        "cc_report_pruning_rulings_fourth_execution_2026_11_02_appendix.md",
}
pairs = {p["the_report"]: p["the_appendix"] for p in ap["the_pairs"]}
named = all(pairs.get(k) == v for k, v in expected.items())
report("P8", ap["count"] >= 4 and named,
       {"count": ap["count"], "the_pairs": pairs,
        "above_four_reported_not_a_failure": ap["count"] > 4})

print("ALL PASS" if all(results) else "AT LEAST ONE FAIL")
```

`t2c_out.txt`:

```
P1 PASS — {'characters': 8, 'characters_on_lines_shared_with_the_predecessor': 4, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 1, 'share_percent': 50.0}
P2 PASS — {'characters': 4, 'characters_on_lines_shared_with_the_predecessor': 4, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 0, 'share_percent': 100.0}
P3 PASS — {'first': {'characters': 4, 'characters_on_lines_shared_with_the_predecessor': 0, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 0, 'share_percent': 0.0}, 'second': {'characters': 0, 'characters_on_lines_shared_with_the_predecessor': 0, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 0, 'share_percent': 0.0}}
P4 PASS — {'characters': 8, 'characters_on_lines_shared_with_the_predecessor': 4, 'characters_on_whitespace_only_lines_shared_and_not_counted_above': 0, 'share_percent': 50.0}
P5 PASS — Stop: an appendix file has no report beside it: r_y_appendix.md
P6 PASS — {'r_x.md': 'r_x_appendix.md'}
P7 PASS — {'the_arc_dispatches': {'members': 30, 'appendix_names': [], 'first_has_no_predecessor': True, 'every_other_predecessor_is_the_member_before': True, 'every_other_carries_a_share': True}, 'the_arc_reports': {'members': 30, 'appendix_names': [], 'first_has_no_predecessor': True, 'every_other_predecessor_is_the_member_before': True, 'every_other_carries_a_share': True}}
P8 PASS — {'count': 4, 'the_pairs': {'cc_report_pruning_rulings_execution_2026_11_01.md': 'cc_report_pruning_rulings_execution_2026_11_01_appendix.md', 'cc_report_pruning_rulings_fourth_execution_2026_11_02.md': 'cc_report_pruning_rulings_fourth_execution_2026_11_02_appendix.md', 'cc_report_pruning_rulings_reexecution_2026_11_01.md': 'cc_report_pruning_rulings_reexecution_2026_11_01_appendix.md', 'cc_report_pruning_rulings_third_execution_2026_11_01.md': 'cc_report_pruning_rulings_third_execution_2026_11_01_appendix.md'}, 'above_four_reported_not_a_failure': False}
ALL PASS
```

## A16 — 2(d) — `python tools/audit/gen_per_session_reading.py` (write mode), the extended tool

`t2d_write.txt`:

```
wrote tools/audit/per_session_reading.json
  the ordinary session-start read (imported) 237676
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  invariant share: dispatches 32.35 %, reports 19.00 %
  reports with an appendix beside them 4: reports proper 131829, appendices 578857 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674763
  Cowork, per sitting, in the shape of the sitting of entry 461: 973582
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
```

## A17 — 2(d) — `time python tools/audit/gen_per_session_reading.py --check`

`t2d_check.txt`:

```
the per-session reading measurement re-derives
  the ordinary session-start read (imported) 237676
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  invariant share: dispatches 32.35 %, reports 19.00 %
  reports with an appendix beside them 4: reports proper 131829, appendices 578857 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674763
  Cowork, per sitting, in the shape of the sitting of entry 461: 973582
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found

real	0m3.017s
user	0m0.000s
sys	0m0.015s
```

## A18 — 2(e) — the comparison with the baseline at this tree: the scratch script `t2e_compare.py`

`t2e_compare.py`:

```
"""2(e): the regenerated per-session reading artifact against the baseline taken at 2(a) with the
tool as it stood. Walks both as JSON and prints every path whose value differs, was added or was
removed, each classed against the dispatch's prediction; then the two arithmetic checks.
The two lists edit 8 (iii) and (iv) extend are compared as lists of strings, so an insertion is
reported as added and not as every later element changed."""
import difflib
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
base = json.load(open(sys.argv[1], encoding="utf-8"))
new = json.load(open(sys.argv[2], encoding="utf-8"))
verbose = "--quiet" not in sys.argv

STRING_LISTS = ("the_bounds_this_artifact_declares_on_itself", "what_this_does_not_assert")
records = []


def walk(a, b, path):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a:
            if k not in b:
                records.append(("removed", path + [k], a[k], None))
            else:
                walk(a[k], b[k], path + [k])
        for k in b:
            if k not in a:
                records.append(("added", path + [k], None, b[k]))
    elif isinstance(a, list) and isinstance(b, list):
        if path and path[-1] in STRING_LISTS and all(isinstance(x, str) for x in a + b):
            sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op == "equal":
                    continue
                for i in range(i1, i2):
                    records.append(("removed", path + [i], a[i], None))
                for j in range(j1, j2):
                    records.append(("added", path + [j], None, b[j]))
            return
        for i in range(max(len(a), len(b))):
            if i >= len(a):
                records.append(("added", path + [i], None, b[i]))
            elif i >= len(b):
                records.append(("removed", path + [i], a[i], None))
            else:
                walk(a[i], b[i], path + [i])
    else:
        if a != b:
            records.append(("changed", path, a, b))


walk(base, new, [])

T1 = "table_1_the_per_session_reading"
CC = "Claude Code, per batch, in the thirtieth dispatch's shape"
EXPECTED_BOUNDS = [
    "The invariant share is a LINE measure, not a judgement of copying: a line changed by one "
    "character counts as not shared, and a short common line counts as shared wherever it "
    "stands. It compares each member with its predecessor only.",
    "An appendix file is found by its name alone (`<stem>_appendix.md` beside `<stem>.md`).",
]
EXPECTED_NONASSERT = ["That a line shared with the predecessor was copied from it, or that a line "
                      "not shared was newly written."]
BOUND_ANCHOR = "The dispatch and report populations are complete only relative to their name prefixes."
NONASSERT_ANCHOR = "That the dispatch and report populations are complete beyond the name prefixes."


def classify(kind, p, old, newv):
    if kind == "changed" and p == ["generated_for"]:
        return "changed: generated_for"
    if kind != "added":
        return None
    if p == [T1, "the_arc_dispatches", "the_invariant_share"]:
        return "added: the_invariant_share under the_arc_dispatches"
    if p == [T1, "the_arc_reports", "the_invariant_share"]:
        return "added: the_invariant_share under the_arc_reports"
    if p == [T1, "the_arc_reports", "the_appendices_beside_them"]:
        return "added: the_appendices_beside_them under the_arc_reports"
    if p == [T1, "the_reports_with_an_appendix_beside_them"]:
        return "added: the_reports_with_an_appendix_beside_them under table 1"
    if p in ([T1, "totals_by_side", CC, "under_ruling_2_of_2026_11_01"],
             [T1, "totals_by_side", CC, "how_ruling_2_moves_it"]):
        return "added: %s under the Claude Code side" % p[-1]
    if (len(p) == 5 and p[0] == T1 and p[1] in ("the_arc_dispatches", "the_arc_reports")
            and p[2] in ("the_population", "the_last_five", "the_last_three")
            and isinstance(p[3], int)):
        if p[4] in ("the_predecessor", "shared_with_the_predecessor"):
            return "added: %s in a member record of %s" % (p[4], p[1])
        if p[4] == "the_appendix_beside_it" and p[1] == "the_arc_reports":
            return "added: the_appendix_beside_it in a member record of the_arc_reports"
    if len(p) == 2 and p[0] == "the_bounds_this_artifact_declares_on_itself":
        lst = new[p[0]]
        k = lst.index(BOUND_ANCHOR)
        if newv in EXPECTED_BOUNDS and p[1] == k + 1 + EXPECTED_BOUNDS.index(newv):
            return "added: an edit 8 (iii) bound sentence, after the populations bound"
    if len(p) == 2 and p[0] == "what_this_does_not_assert":
        lst = new[p[0]]
        k = lst.index(NONASSERT_ANCHOR)
        if newv in EXPECTED_NONASSERT and p[1] == k + 1:
            return "added: the edit 8 (iv) non-assertion, after the populations one"
    return None


counts = {}
unpredicted = []
for kind, p, old, newv in records:
    c = classify(kind, p, old, newv)
    label = c or "UNPREDICTED"
    counts[label] = counts.get(label, 0) + 1
    if c is None:
        unpredicted.append((kind, p, old, newv))
    if verbose:
        def short(v):
            s = json.dumps(v, ensure_ascii=False)
            return s if len(s) <= 160 else s[:157] + "..."
        print("%-8s %s | %s -> %s  [%s]" % (kind, " / ".join(map(str, p)), short(old), short(newv),
                                            label))

print("== differences: %d" % len(records))
for label in sorted(counts):
    print("  %5d  %s" % (counts[label], label))
gf = [r for r in records if r[1] == ["generated_for"]]
for r in gf:
    print("generated_for former: %s" % r[2])
    print("generated_for new:    %s" % r[3])
print("changed values other than generated_for: %d"
      % sum(1 for r in records if r[0] == "changed" and r[1] != ["generated_for"]))
print("removed: %d" % sum(1 for r in records if r[0] == "removed"))

# member records: every one of the two arc populations carries the added fields
t1n = new[T1]
miss = []
for field, latest in (("the_arc_dispatches", "the_last_five"), ("the_arc_reports", "the_last_three")):
    for grp in ("the_population", latest):
        for i, m in enumerate(t1n[field][grp]):
            need = ["the_predecessor", "shared_with_the_predecessor"]
            if field == "the_arc_reports":
                need.append("the_appendix_beside_it")
            for k in need:
                if k not in m:
                    miss.append((field, grp, i, k))
print("member records lacking a predicted added field: %d" % len(miss))

# the two arithmetic checks
cc = t1n["totals_by_side"][CC]
six = t1n["the_ordinary_session_start_read_imported"]["the_reading_of_claude_md"]["characters"]
lhs, rhs = cc["under_ruling_2_of_2026_11_01"], cc["with_it"] - six
print("ARITH 1: under_ruling_2_of_2026_11_01 %d == with_it %d - six spans %d = %d : %s"
      % (lhs, cc["with_it"], six, rhs, lhs == rhs))
ap = t1n["the_reports_with_an_appendix_beside_them"]
s = sum(p["characters_of_the_appendix"] for p in ap["the_pairs"])
print("ARITH 2: characters_of_the_appendices %d == sum of pairs %d : %s"
      % (ap["characters_of_the_appendices"], s, ap["characters_of_the_appendices"] == s))

MUST = {
    "added: the_invariant_share under the_arc_dispatches": 1,
    "added: the_invariant_share under the_arc_reports": 1,
    "added: the_appendices_beside_them under the_arc_reports": 1,
    "added: the_reports_with_an_appendix_beside_them under table 1": 1,
    "added: under_ruling_2_of_2026_11_01 under the Claude Code side": 1,
    "added: how_ruling_2_moves_it under the Claude Code side": 1,
    "added: an edit 8 (iii) bound sentence, after the populations bound": 2,
    "added: the edit 8 (iv) non-assertion, after the populations one": 1,
}
absent = {k: (counts.get(k, 0), v) for k, v in MUST.items() if counts.get(k, 0) != v}
print("predicted single additions present in the predicted number: %s" % (not absent))
for k, (got, want) in absent.items():
    print("  %s: %d, predicted %d" % (k, got, want))

ok = (not absent and not unpredicted and not miss and len(gf) == 1 and lhs == rhs
      and ap["characters_of_the_appendices"] == s
      and not any(r[0] == "removed" for r in records))
print("2(e) COMPARISON: %s" % ("AS PREDICTED" if ok else "NOT AS PREDICTED"))
```

## A19 — 2(e) — its output, every per-path record and the classed summary, whole

`t2e_out.txt`:

```
changed  generated_for | "cc_instruction_per_session_reading_measurement_2026_11_01.md, Task 1 — step 1 of the pruning iteration the user ordered on 2026-10-31" -> "cc_instruction_per_session_reading_extension_2026_11_02.md, Task 2 — step 4's second dispatch of the pruning iteration the user ordered on 2026-10-31; first...  [changed: generated_for]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 0 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_fifth_2026_10_27.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 0 / shared_with_the_predecessor | null -> {"characters": 239614, "characters_on_lines_shared_with_the_predecessor": 72205, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 112, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 1 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_sixth_2026_10_27.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 1 / shared_with_the_predecessor | null -> {"characters": 259912, "characters_on_lines_shared_with_the_predecessor": 76287, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 113, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 2 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_seventh_2026_10_28.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 2 / shared_with_the_predecessor | null -> {"characters": 233425, "characters_on_lines_shared_with_the_predecessor": 56199, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 111, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 3 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_eighth_2026_10_30.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 3 / shared_with_the_predecessor | null -> {"characters": 181526, "characters_on_lines_shared_with_the_predecessor": 28867, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 105, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 4 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_ninth_2026_10_31.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_last_five / 4 / shared_with_the_predecessor | null -> {"characters": 151805, "characters_on_lines_shared_with_the_predecessor": 43639, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 100, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 0 / the_predecessor | null -> null  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 0 / shared_with_the_predecessor | null -> null  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 1 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_2026_10_18.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 1 / shared_with_the_predecessor | null -> {"characters": 80466, "characters_on_lines_shared_with_the_predecessor": 27722, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 87, "shar...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 2 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_second_2026_10_18.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 2 / shared_with_the_predecessor | null -> {"characters": 84717, "characters_on_lines_shared_with_the_predecessor": 43647, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 87, "shar...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 3 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_third_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 3 / shared_with_the_predecessor | null -> {"characters": 92356, "characters_on_lines_shared_with_the_predecessor": 50693, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 87, "shar...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 4 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_fourth_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 4 / shared_with_the_predecessor | null -> {"characters": 98630, "characters_on_lines_shared_with_the_predecessor": 53623, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 87, "shar...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 5 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_fifth_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 5 / shared_with_the_predecessor | null -> {"characters": 111310, "characters_on_lines_shared_with_the_predecessor": 55187, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 87, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 6 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_sixth_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 6 / shared_with_the_predecessor | null -> {"characters": 126198, "characters_on_lines_shared_with_the_predecessor": 55310, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 87, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 7 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_seventh_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 7 / shared_with_the_predecessor | null -> {"characters": 136728, "characters_on_lines_shared_with_the_predecessor": 64234, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 87, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 8 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_eighth_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 8 / shared_with_the_predecessor | null -> {"characters": 153800, "characters_on_lines_shared_with_the_predecessor": 56313, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 86, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 9 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_ninth_2026_10_20.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 9 / shared_with_the_predecessor | null -> {"characters": 172851, "characters_on_lines_shared_with_the_predecessor": 64314, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 86, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 10 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_tenth_2026_10_20.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 10 / shared_with_the_predecessor | null -> {"characters": 156452, "characters_on_lines_shared_with_the_predecessor": 53511, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 86, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 11 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_eleventh_2026_10_20.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 11 / shared_with_the_predecessor | null -> {"characters": 153985, "characters_on_lines_shared_with_the_predecessor": 67185, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 86, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 12 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 12 / shared_with_the_predecessor | null -> {"characters": 171675, "characters_on_lines_shared_with_the_predecessor": 66573, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 87, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 13 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 13 / shared_with_the_predecessor | null -> {"characters": 185731, "characters_on_lines_shared_with_the_predecessor": 73716, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 88, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 14 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 14 / shared_with_the_predecessor | null -> {"characters": 181526, "characters_on_lines_shared_with_the_predecessor": 55029, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 88, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 15 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_fifteenth_2026_10_24.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 15 / shared_with_the_predecessor | null -> {"characters": 169864, "characters_on_lines_shared_with_the_predecessor": 51220, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 88, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 16 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_sixteenth_2026_10_24.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 16 / shared_with_the_predecessor | null -> {"characters": 177296, "characters_on_lines_shared_with_the_predecessor": 49656, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 89, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 17 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_seventeenth_2026_10_24.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 17 / shared_with_the_predecessor | null -> {"characters": 190948, "characters_on_lines_shared_with_the_predecessor": 53154, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 94, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 18 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_eighteenth_2026_10_25.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 18 / shared_with_the_predecessor | null -> {"characters": 205990, "characters_on_lines_shared_with_the_predecessor": 58587, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 98, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 19 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_nineteenth_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 19 / shared_with_the_predecessor | null -> {"characters": 224366, "characters_on_lines_shared_with_the_predecessor": 61259, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 98, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 20 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twentieth_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 20 / shared_with_the_predecessor | null -> {"characters": 210734, "characters_on_lines_shared_with_the_predecessor": 55828, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 102, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 21 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_first_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 21 / shared_with_the_predecessor | null -> {"characters": 166056, "characters_on_lines_shared_with_the_predecessor": 43669, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 99, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 22 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_second_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 22 / shared_with_the_predecessor | null -> {"characters": 164756, "characters_on_lines_shared_with_the_predecessor": 35778, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 99, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 23 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_third_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 23 / shared_with_the_predecessor | null -> {"characters": 188439, "characters_on_lines_shared_with_the_predecessor": 41175, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 100, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 24 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_fourth_2026_10_27.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 24 / shared_with_the_predecessor | null -> {"characters": 212059, "characters_on_lines_shared_with_the_predecessor": 65150, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 111, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 25 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_fifth_2026_10_27.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 25 / shared_with_the_predecessor | null -> {"characters": 239614, "characters_on_lines_shared_with_the_predecessor": 72205, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 112, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 26 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_sixth_2026_10_27.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 26 / shared_with_the_predecessor | null -> {"characters": 259912, "characters_on_lines_shared_with_the_predecessor": 76287, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 113, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 27 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_seventh_2026_10_28.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 27 / shared_with_the_predecessor | null -> {"characters": 233425, "characters_on_lines_shared_with_the_predecessor": 56199, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 111, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 28 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_eighth_2026_10_30.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 28 / shared_with_the_predecessor | null -> {"characters": 181526, "characters_on_lines_shared_with_the_predecessor": 28867, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 105, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 29 / the_predecessor | null -> "cc_instruction_l3_comparison_tabulation_twenty_ninth_2026_10_31.md"  [added: the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_population / 29 / shared_with_the_predecessor | null -> {"characters": 151805, "characters_on_lines_shared_with_the_predecessor": 43639, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 100, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_dispatches / the_invariant_share | null -> {"members_with_a_predecessor": 29, "their_characters": 4883215, "their_characters_on_lines_shared_with_the_predecessor": 1579730, "share_percent": 32.35, "ho...  [added: the_invariant_share under the_arc_dispatches]
added    table_1_the_per_session_reading / the_arc_reports / the_last_three / 0 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_seventh_2026_10_28.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_last_three / 0 / shared_with_the_predecessor | null -> {"characters": 142049, "characters_on_lines_shared_with_the_predecessor": 40928, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 287, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_last_three / 0 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_last_three / 1 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_eighth_2026_10_30.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_last_three / 1 / shared_with_the_predecessor | null -> {"characters": 90619, "characters_on_lines_shared_with_the_predecessor": 18719, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 166, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_last_three / 1 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_last_three / 2 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_ninth_2026_10_31.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_last_three / 2 / shared_with_the_predecessor | null -> {"characters": 520923, "characters_on_lines_shared_with_the_predecessor": 18160, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 166, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_last_three / 2 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 0 / the_predecessor | null -> null  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 0 / shared_with_the_predecessor | null -> null  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 0 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 1 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_2026_10_18.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 1 / shared_with_the_predecessor | null -> {"characters": 46542, "characters_on_lines_shared_with_the_predecessor": 13186, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 95, "shar...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 1 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 2 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_second_2026_10_18.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 2 / shared_with_the_predecessor | null -> {"characters": 54986, "characters_on_lines_shared_with_the_predecessor": 19534, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 95, "shar...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 2 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 3 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_third_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 3 / shared_with_the_predecessor | null -> {"characters": 61723, "characters_on_lines_shared_with_the_predecessor": 30990, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 126, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 3 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 4 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_fourth_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 4 / shared_with_the_predecessor | null -> {"characters": 69767, "characters_on_lines_shared_with_the_predecessor": 30069, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 137, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 4 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 5 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_fifth_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 5 / shared_with_the_predecessor | null -> {"characters": 56766, "characters_on_lines_shared_with_the_predecessor": 23596, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 106, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 5 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 6 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_sixth_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 6 / shared_with_the_predecessor | null -> {"characters": 57458, "characters_on_lines_shared_with_the_predecessor": 19191, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 98, "shar...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 6 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 7 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_seventh_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 7 / shared_with_the_predecessor | null -> {"characters": 72330, "characters_on_lines_shared_with_the_predecessor": 14692, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 98, "shar...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 7 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 8 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_eighth_2026_10_19.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 8 / shared_with_the_predecessor | null -> {"characters": 62175, "characters_on_lines_shared_with_the_predecessor": 21124, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 103, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 8 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 9 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_ninth_2026_10_20.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 9 / shared_with_the_predecessor | null -> {"characters": 74764, "characters_on_lines_shared_with_the_predecessor": 15617, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 103, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 9 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 10 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_tenth_2026_10_20.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 10 / shared_with_the_predecessor | null -> {"characters": 79270, "characters_on_lines_shared_with_the_predecessor": 22993, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 140, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 10 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 11 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_eleventh_2026_10_20.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 11 / shared_with_the_predecessor | null -> {"characters": 134126, "characters_on_lines_shared_with_the_predecessor": 29095, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 165, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 11 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 12 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twelfth_2026_10_20.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 12 / shared_with_the_predecessor | null -> {"characters": 117568, "characters_on_lines_shared_with_the_predecessor": 27173, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 189, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 12 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 13 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_thirteenth_2026_10_21.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 13 / shared_with_the_predecessor | null -> {"characters": 63286, "characters_on_lines_shared_with_the_predecessor": 17748, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 149, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 13 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 14 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_fourteenth_2026_10_23.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 14 / shared_with_the_predecessor | null -> {"characters": 71420, "characters_on_lines_shared_with_the_predecessor": 21751, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 144, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 14 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 15 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_fifteenth_2026_10_24.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 15 / shared_with_the_predecessor | null -> {"characters": 73117, "characters_on_lines_shared_with_the_predecessor": 27100, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 144, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 15 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 16 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_sixteenth_2026_10_24.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 16 / shared_with_the_predecessor | null -> {"characters": 89385, "characters_on_lines_shared_with_the_predecessor": 28560, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 149, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 16 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 17 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_seventeenth_2026_10_24.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 17 / shared_with_the_predecessor | null -> {"characters": 114017, "characters_on_lines_shared_with_the_predecessor": 29438, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 154, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 17 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 18 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_eighteenth_2026_10_25.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 18 / shared_with_the_predecessor | null -> {"characters": 79766, "characters_on_lines_shared_with_the_predecessor": 19765, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 172, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 18 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 19 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_nineteenth_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 19 / shared_with_the_predecessor | null -> {"characters": 139118, "characters_on_lines_shared_with_the_predecessor": 18862, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 172, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 19 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 20 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twentieth_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 20 / shared_with_the_predecessor | null -> {"characters": 221926, "characters_on_lines_shared_with_the_predecessor": 25615, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 278, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 20 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 21 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_first_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 21 / shared_with_the_predecessor | null -> {"characters": 152663, "characters_on_lines_shared_with_the_predecessor": 35638, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 231, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 21 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 22 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_second_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 22 / shared_with_the_predecessor | null -> {"characters": 167250, "characters_on_lines_shared_with_the_predecessor": 15562, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 168, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 22 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 23 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_third_2026_10_26.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 23 / shared_with_the_predecessor | null -> {"characters": 132154, "characters_on_lines_shared_with_the_predecessor": 15723, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 176, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 23 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 24 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_fourth_2026_10_27.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 24 / shared_with_the_predecessor | null -> {"characters": 228900, "characters_on_lines_shared_with_the_predecessor": 17716, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 171, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 24 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 25 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_fifth_2026_10_27.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 25 / shared_with_the_predecessor | null -> {"characters": 246250, "characters_on_lines_shared_with_the_predecessor": 37391, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 237, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 25 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 26 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_sixth_2026_10_27.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 26 / shared_with_the_predecessor | null -> {"characters": 260055, "characters_on_lines_shared_with_the_predecessor": 43479, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 397, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 26 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 27 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_seventh_2026_10_28.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 27 / shared_with_the_predecessor | null -> {"characters": 142049, "characters_on_lines_shared_with_the_predecessor": 40928, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 287, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 27 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 28 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_eighth_2026_10_30.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 28 / shared_with_the_predecessor | null -> {"characters": 90619, "characters_on_lines_shared_with_the_predecessor": 18719, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 166, "sha...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 28 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 29 / the_predecessor | null -> "cc_report_l3_comparison_tabulation_twenty_ninth_2026_10_31.md"  [added: the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 29 / shared_with_the_predecessor | null -> {"characters": 520923, "characters_on_lines_shared_with_the_predecessor": 18160, "characters_on_whitespace_only_lines_shared_and_not_counted_above": 166, "sh...  [added: shared_with_the_predecessor in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_population / 29 / the_appendix_beside_it | null -> null  [added: the_appendix_beside_it in a member record of the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_invariant_share | null -> {"members_with_a_predecessor": 29, "their_characters": 3680373, "their_characters_on_lines_shared_with_the_predecessor": 699415, "share_percent": 19.0, "how_...  [added: the_invariant_share under the_arc_reports]
added    table_1_the_per_session_reading / the_arc_reports / the_appendices_beside_them | null -> {"count": 0, "characters_total": 0, "how_these_relate_to_the_sizes_above": "every size above is of the report proper only; an appendix file is sized here and...  [added: the_appendices_beside_them under the_arc_reports]
added    table_1_the_per_session_reading / totals_by_side / Claude Code, per batch, in the thirtieth dispatch's shape / under_ruling_2_of_2026_11_01 | null -> 738504  [added: under_ruling_2_of_2026_11_01 under the Claude Code side]
added    table_1_the_per_session_reading / totals_by_side / Claude Code, per batch, in the thirtieth dispatch's shape / how_ruling_2_moves_it | null -> "Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`: the injected copy is the read of the six spans, so their file-t...  [added: how_ruling_2_moves_it under the Claude Code side]
added    table_1_the_per_session_reading / the_reports_with_an_appendix_beside_them | null -> {"the_folder": "records/cc/reports", "how_a_pair_is_found": "every file of the folder whose name ends `_appendix.md`, beside the report named by its stem; an...  [added: the_reports_with_an_appendix_beside_them under table 1]
added    the_bounds_this_artifact_declares_on_itself / 4 | null -> "The invariant share is a LINE measure, not a judgement of copying: a line changed by one character counts as not shared, and a short common line counts as s...  [added: an edit 8 (iii) bound sentence, after the populations bound]
added    the_bounds_this_artifact_declares_on_itself / 5 | null -> "An appendix file is found by its name alone (`<stem>_appendix.md` beside `<stem>.md`)."  [added: an edit 8 (iii) bound sentence, after the populations bound]
added    what_this_does_not_assert / 4 | null -> "That a line shared with the predecessor was copied from it, or that a line not shared was newly written."  [added: the edit 8 (iv) non-assertion, after the populations one]
== differences: 179
      2  added: an edit 8 (iii) bound sentence, after the populations bound
      1  added: how_ruling_2_moves_it under the Claude Code side
     35  added: shared_with_the_predecessor in a member record of the_arc_dispatches
     33  added: shared_with_the_predecessor in a member record of the_arc_reports
      1  added: the edit 8 (iv) non-assertion, after the populations one
      1  added: the_appendices_beside_them under the_arc_reports
     33  added: the_appendix_beside_it in a member record of the_arc_reports
      1  added: the_invariant_share under the_arc_dispatches
      1  added: the_invariant_share under the_arc_reports
     35  added: the_predecessor in a member record of the_arc_dispatches
     33  added: the_predecessor in a member record of the_arc_reports
      1  added: the_reports_with_an_appendix_beside_them under table 1
      1  added: under_ruling_2_of_2026_11_01 under the Claude Code side
      1  changed: generated_for
generated_for former: cc_instruction_per_session_reading_measurement_2026_11_01.md, Task 1 — step 1 of the pruning iteration the user ordered on 2026-10-31
generated_for new:    cc_instruction_per_session_reading_extension_2026_11_02.md, Task 2 — step 4's second dispatch of the pruning iteration the user ordered on 2026-10-31; first built for step 1 (cc_instruction_per_session_reading_measurement_2026_11_01.md, Task 1)
changed values other than generated_for: 0
removed: 0
member records lacking a predicted added field: 0
ARITH 1: under_ruling_2_of_2026_11_01 738504 == with_it 843945 - six spans 105441 = 738504 : True
ARITH 2: characters_of_the_appendices 578857 == sum of pairs 578857 : True
predicted single additions present in the predicted number: True
2(e) COMPARISON: AS PREDICTED
```

## A20 — 2(f) — the capture after Task 2, `python tools/audit/gen_guard_state.py --check`, whole

`cap2_after_task2.txt`:

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
  [PASS] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [PASS] tools/audit/gen_per_session_reading.py --check
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
83 guard(s) run, 13 failing, 4 not run, 20 historical record(s)
```

## A21 — 2(f) — the capture after Task 1 against the capture after Task 2

`cmp_cap1_cap2.txt`:

```
A: cap1_after_task1.txt
B: cap2_after_task2.txt
header A: STALE vs the run: guard_state.json does not re-derive
header B: STALE vs the run: guard_state.json does not re-derive
tally A: 83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
tally B: 83 guard(s) run, 13 failing, 4 not run, 20 historical record(s)
DIFFERS: tools/audit/gen_per_session_reading.py --check : FAIL -> PASS
verdicts compared 107, differing 1; header same True; tally same False
```

## A22 — 3(b) — `python tools/audit/gen_status_batch_bound.py --apply`, then its first `--check`

`t3b_apply.txt`:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 4, 2,639 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

`t3b_check.txt`:

```
  entries moved: 4, 2,639 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

## A23 — 3(b) — the four archive checks, re-run whole at the close tree

`t3b_rerun_bound_check.txt`:

```
$ python tools/audit/gen_status_batch_bound.py --check
  entries moved: 4, 2,639 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
(exit 0)
```

`t3b_rerun_split_status.txt`:

```
$ python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md
  STATUS.md / STATUS_ARCHIVE.md: moved 131 span(s), 457,949 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
(exit 0)
```

`t3b_rerun_residue.txt`:

```
$ python tools/audit/gen_status_residue_move.py --check
  candidates: 17, moved 16, left at site by the reading 1
  characters moved: 46,105
  byte-present in the companion exactly once: True
  absent from the must-read:                  True
  every flagged entry still at site:          True
(exit 0)
```

`t3b_rerun_archive_pass.txt`:

```
$ python tools/audit/gen_status_archive_pass.py --check
  dated entries moved: 52
  at the pass commit, the live file was exactly base-minus-range: True
  the moved block is verbatim in the archive at HEAD:             True
  the moved block is absent from the live file at HEAD:           True
(exit 0)
```

## A24 — 3(c) — the regenerations' write-mode outputs (read size, defense share, the per-session tool)

`t3c_ssr_write.txt`:

```
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
    STATUS.md                                                                 11657
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 237414
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 237414 [ruled membership]  (-129707, -35.33%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 237414 [ruled membership]  (-59418, -20.02%)  <- CROSSES A REGIME BOUNDARY
```

`t3c_defense_write.txt`:

```
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
    of the whole session-start read (237414): 5.46%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

`t3c_psr_write.txt`:

```
wrote tools/audit/per_session_reading.json
  the ordinary session-start read (imported) 237414
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  invariant share: dispatches 32.35 %, reports 19.00 %
  reports with an appendix beside them 4: reports proper 131829, appendices 578857 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674501
  Cowork, per sitting, in the shape of the sitting of entry 461: 973320
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
```

## A25 — 3(c) — every check of 3(c), re-run whole at the close tree

`t3c_rerun_evpin.txt`:

```
$ python tools/audit/gen_evidence_pin_membership.py --check
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 171
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
(exit 0)
```

`t3c_rerun_ssr.txt`:

```
$ python tools/audit/gen_session_start_read_size.py --check
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
    STATUS.md                                                                 11657
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 237414
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 237414 [ruled membership]  (-129707, -35.33%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 237414 [ruled membership]  (-59418, -20.02%)  <- CROSSES A REGIME BOUNDARY
(exit 0)
```

`t3c_rerun_defense.txt`:

```
$ python tools/audit/gen_defense_share.py --check
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
    of the whole session-start read (237414): 5.46%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
(exit 0)
```

`t3c_rerun_l0l1.txt`:

```
$ python tools/audit/gen_l0_l1_outgoing_population.py --check
l0_l1_outgoing_population.json re-derives
(exit 0)
```

`t3c_rerun_l3.txt`:

```
$ python tools/audit/gen_l3_outgoing_population.py --check
l3_outgoing_population.json re-derives
(exit 0)
```

`t3c_rerun_bootpack.txt`:

```
$ python tools/audit/gen_derivation_boot_pack.py --check
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
(exit 0)
```

`t3c_rerun_psr.txt`:

```
$ python tools/audit/gen_per_session_reading.py --check
the per-session reading measurement re-derives
  the ordinary session-start read (imported) 237414
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  invariant share: dispatches 32.35 %, reports 19.00 %
  reports with an appendix beside them 4: reports proper 131829, appendices 578857 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674501
  Cowork, per sitting, in the shape of the sitting of entry 461: 973320
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
(exit 0)
```

## A26 — 3(c) — the artifact diffs: the scratch script `t3c_diffs.py`, its output, then each diff whole

`t3c_diffs.py`:

```
"""3(c): each artifact the close regenerated (and the two population artifacts it did not) written
as a blob and diffed against its base blob. Each base is a commit hash written literally here."""
import subprocess

ROOT = r"C:\s\MS"
OUTDIR = r"C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad"
START = "08274008d07b7e102a692f59eaedb0905860c39f"
T2 = "37d8ebb68f60a62f01b1f618288fd95a8a9a6512"
ARTIFACTS = [
    ("tools/audit/session_start_read_size.json", START),
    ("tools/audit/defense_share.json", START),
    ("tools/audit/l0_l1_outgoing_population.json", START),
    ("tools/audit/l3_outgoing_population.json", START),
    ("tools/audit/per_session_reading.json", T2),
]


def git(*args):
    return subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True, text=True,
                          encoding="utf-8", check=True).stdout


for path, base in ARTIFACTS:
    old = git("rev-parse", "%s:%s" % (base, path)).strip()
    new = git("hash-object", "-w", path).strip()
    name = path.rsplit("/", 1)[1].replace(".json", "")
    out = OUTDIR + "\\t3c_diff_" + name + ".txt"
    diff = git("diff", "--unified=2", old, new)
    open(out, "w", encoding="utf-8").write(diff)
    hunks = diff.count("\n@@")
    print("%s: base %s at %s -> %s; %s; hunks %d; diff in %s"
          % (path, old, base[:8], new, "UNCHANGED" if old == new else "CHANGED", hunks, out))
```

`t3c_diffs_out.txt`:

```
tools/audit/session_start_read_size.json: base 5b4a34653d5459bbf08938bcdb7d81e8a90d251d at 08274008 -> f86a3fe23483ac3761a9ae68bd2770b5f2b8b2fe; CHANGED; hunks 3; diff in C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad\t3c_diff_session_start_read_size.txt
tools/audit/defense_share.json: base 15f650412fe3ad5176bbce82f6881ec55555e606 at 08274008 -> a0ba4c0782ccf3cc15e8093e06ecf55d8086a550; CHANGED; hunks 2; diff in C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad\t3c_diff_defense_share.txt
tools/audit/l0_l1_outgoing_population.json: base d4a7a548785221b15d658f1f8eab5317b56c6398 at 08274008 -> d4a7a548785221b15d658f1f8eab5317b56c6398; UNCHANGED; hunks 0; diff in C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad\t3c_diff_l0_l1_outgoing_population.txt
tools/audit/l3_outgoing_population.json: base 8aac2cfc00123a2858e989cd8dfc99ac66b27a61 at 08274008 -> 8aac2cfc00123a2858e989cd8dfc99ac66b27a61; UNCHANGED; hunks 0; diff in C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad\t3c_diff_l3_outgoing_population.txt
tools/audit/per_session_reading.json: base 2b652810b2e21268b382e53dadee38f0f7391acc at 37d8ebb6 -> 5a92758406847373bdc008ad421da630b7d32faa; CHANGED; hunks 7; diff in C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad\t3c_diff_per_session_reading.txt
```

`t3c_diff_session_start_read_size.txt`:

```
diff --git a/5b4a34653d5459bbf08938bcdb7d81e8a90d251d b/f86a3fe23483ac3761a9ae68bd2770b5f2b8b2fe
index 5b4a34653d..f86a3fe234 100644
--- a/5b4a34653d5459bbf08938bcdb7d81e8a90d251d
+++ b/f86a3fe23483ac3761a9ae68bd2770b5f2b8b2fe
@@ -177,9 +177,9 @@
   "characters_per_member": {
    "CLAUDE.md": 105441,
-   "STATUS.md": 11919,
+   "STATUS.md": 11657,
    "DECISIONS.md": 117490,
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
   },
-  "total_characters": 237676,
+  "total_characters": 237414,
   "further_spans_of_the_same_artifact_NOT_counted_into_the_read": {
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows": {
@@ -277,8 +277,8 @@
    "from_total": 367121,
    "from_regime": "whole-file practice",
-   "to_total": 237676,
+   "to_total": 237414,
    "to_regime": "ruled membership",
-   "change_in_characters": -129445,
-   "change_percent": -35.26,
+   "change_in_characters": -129707,
+   "change_percent": -35.33,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
@@ -288,8 +288,8 @@
    "from_total": 296832,
    "from_regime": "whole-file practice",
-   "to_total": 237676,
+   "to_total": 237414,
    "to_regime": "ruled membership",
-   "change_in_characters": -59156,
-   "change_percent": -19.93,
+   "change_in_characters": -59418,
+   "change_percent": -20.02,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
```

`t3c_diff_defense_share.txt`:

```
diff --git a/15f650412fe3ad5176bbce82f6881ec55555e606 b/a0ba4c0782ccf3cc15e8093e06ecf55d8086a550
index 15f650412f..a0ba4c0782 100644
--- a/15f650412fe3ad5176bbce82f6881ec55555e606
+++ b/a0ba4c0782ccf3cc15e8093e06ecf55d8086a550
@@ -78,5 +78,5 @@
  "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
   "the_six_session_start_spans": 105441,
-  "the_whole_ordinary_session_start_read": 237676,
+  "the_whole_ordinary_session_start_read": 237414,
   "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked defense; the second says how much of the WHOLE boot it is. A share quoted against one of them is not the share against the other."
  },
@@ -143,5 +143,5 @@
   "characters_had_every_clause_run_to_its_paragraph_end": 160906,
   "share_of_the_six_session_start_spans": 12.29,
-  "share_of_the_whole_ordinary_session_start_read": 5.45
+  "share_of_the_whole_ordinary_session_start_read": 5.46
  },
  "every_clause_published_so_the_tables_reach_is_inspectable_rather_than_asserted": [
```

`t3c_diff_l0_l1_outgoing_population.txt`:

```

```

`t3c_diff_l3_outgoing_population.txt`:

```

```

`t3c_diff_per_session_reading.txt`:

```
diff --git a/2b652810b2e21268b382e53dadee38f0f7391acc b/5a92758406847373bdc008ad421da630b7d32faa
index 2b652810b2..5a92758406 100644
--- a/2b652810b2e21268b382e53dadee38f0f7391acc
+++ b/5a92758406847373bdc008ad421da630b7d32faa
@@ -16,9 +16,9 @@
    "characters_per_member": {
     "CLAUDE.md": 105441,
-    "STATUS.md": 11919,
+    "STATUS.md": 11657,
     "DECISIONS.md": 117490,
     "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
    },
-   "total_characters": 237676,
+   "total_characters": 237414,
    "the_reading_of_claude_md": {
     "regime": "ruled membership",
@@ -1368,5 +1368,5 @@
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 237676
+      "characters": 237414
      },
      {
@@ -1391,8 +1391,8 @@
      }
     ],
-    "without_the_injected_copy_of_CLAUDE_md": 674763,
-    "with_it": 843945,
+    "without_the_injected_copy_of_CLAUDE_md": 674501,
+    "with_it": 843683,
     "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, 169182 characters",
-    "under_ruling_2_of_2026_11_01": 738504,
+    "under_ruling_2_of_2026_11_01": 738242,
     "how_ruling_2_moves_it": "Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`: the injected copy is the read of the six spans, so their file-tool read (105441 characters) leaves the sum and the injected copy stays; the eight-line check's own reads are not sized here",
     "left_out_and_said_so": "the previous report at the portions a dispatch orders, the reading file at its ordered portions, the ruling records a dispatch orders — varies per dispatch and is not sized here"
@@ -1402,5 +1402,5 @@
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 237676
+      "characters": 237414
      },
      {
@@ -1433,5 +1433,5 @@
      }
     ],
-    "characters": 973582,
+    "characters": 973320,
     "left_out_and_said_so": "the verification reads at the objects (the reading file at its sections, the guard state, the ref files, the away-returns close) — varies per batch and is not sized here"
    }
@@ -3819,5 +3819,5 @@
     "characters_had_every_clause_run_to_its_paragraph_end": 160906,
     "share_of_the_six_session_start_spans": 12.29,
-    "share_of_the_whole_ordinary_session_start_read": 5.45
+    "share_of_the_whole_ordinary_session_start_read": 5.46
    },
    "per_span": [
@@ -3879,5 +3879,5 @@
    "the_two_denominators": {
     "the_six_session_start_spans": 105441,
-    "the_whole_ordinary_session_start_read": 237676
+    "the_whole_ordinary_session_start_read": 237414
    },
    "how_these_relate_to_the_sums_above": "a marked clause lies INSIDE a sub-block, so these values overlap table 2's sums and are never added to them"
```

## A27 — 3(c) — the scratch script that re-ran the checks of A23 and A25, then its output

`t3_checks_rerun.py`:

```
"""Re-run the read-only checks of 3(b) and 3(c) at the tree the close left, each output whole into
its own scratch file, for the appendix (the first runs were seen only in part on the console)."""
import subprocess

ROOT = r"C:\s\MS"
OUT = r"C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad"
RUNS = [
    ("t3b_rerun_bound_check", ["tools/audit/gen_status_batch_bound.py", "--check"]),
    ("t3b_rerun_split_status", ["tools/audit/gen_governing_surface_split.py", "--check", "--pair", "STATUS.md"]),
    ("t3b_rerun_residue", ["tools/audit/gen_status_residue_move.py", "--check"]),
    ("t3b_rerun_archive_pass", ["tools/audit/gen_status_archive_pass.py", "--check"]),
    ("t3c_rerun_evpin", ["tools/audit/gen_evidence_pin_membership.py", "--check"]),
    ("t3c_rerun_ssr", ["tools/audit/gen_session_start_read_size.py", "--check"]),
    ("t3c_rerun_defense", ["tools/audit/gen_defense_share.py", "--check"]),
    ("t3c_rerun_l0l1", ["tools/audit/gen_l0_l1_outgoing_population.py", "--check"]),
    ("t3c_rerun_l3", ["tools/audit/gen_l3_outgoing_population.py", "--check"]),
    ("t3c_rerun_bootpack", ["tools/audit/gen_derivation_boot_pack.py", "--check"]),
    ("t3c_rerun_psr", ["tools/audit/gen_per_session_reading.py", "--check"]),
]
for name, cmd in RUNS:
    p = subprocess.run(["python"] + cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    open(OUT + "\\" + name + ".txt", "w", encoding="utf-8").write(
        "$ python %s\n%s%s(exit %d)\n" % (" ".join(cmd), p.stdout, p.stderr, p.returncode))
    print("%-24s exit %d" % (name, p.returncode))
```

`t3_checks_rerun_out.txt`:

```
t3b_rerun_bound_check    exit 0
t3b_rerun_split_status   exit 0
t3b_rerun_residue        exit 0
t3b_rerun_archive_pass   exit 0
t3c_rerun_evpin          exit 0
t3c_rerun_ssr            exit 0
t3c_rerun_defense        exit 0
t3c_rerun_l0l1           exit 0
t3c_rerun_l3             exit 0
t3c_rerun_bootpack       exit 0
t3c_rerun_psr            exit 0
```

## A28 — 3(d) — THE BEFORE AND AFTER TABLE: the scratch script `t3d_before_after.py`

`t3d_before_after.py`:

````
"""3(d): THE BEFORE AND AFTER TABLE. Reads the before-artifact (the per-session reading artifact at
d17a84afdbfbf78c16ff4514df63185fad114a5c, taken by `git show` into the file named first) and the
after-artifact (the working-tree file, named second) and prints, for each value the dispatch names,
before, after and the difference, each printed from the two objects and none typed. Then the
after-only blocks, and a second table per arc member, after only."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
before = json.load(open(sys.argv[1], encoding="utf-8"))
after = json.load(open(sys.argv[2], encoding="utf-8"))
T1 = "table_1_the_per_session_reading"
T2 = "table_2_the_six_spans_partitioned"
CC = "Claude Code, per batch, in the thirtieth dispatch's shape"
CW = "Cowork, per sitting, in the shape of the sitting of entry 461"


def row(label, b, a):
    d = (a - b) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else "—"
    fmt = lambda v: "—" if v is None else ("{:,}".format(v) if isinstance(v, int) else str(v))
    dd = ("{:+,}".format(d) if isinstance(d, int) else
          ("%+.2f" % d if isinstance(d, float) else d))
    print("| %s | %s | %s | %s |" % (label, fmt(b), fmt(a), dd))


def head(title):
    print()
    print("**%s**" % title)
    print()
    print("| Value | Before | After | Difference |")
    print("|---|---|---|---|")


ob, oa = before[T1]["the_ordinary_session_start_read_imported"], after[T1]["the_ordinary_session_start_read_imported"]
head("1. The ordinary session-start read (imported)")
row("total_characters", ob["total_characters"], oa["total_characters"])
for k in list(ob["characters_per_member"]) + [k for k in oa["characters_per_member"]
                                             if k not in ob["characters_per_member"]]:
    row("characters_per_member → %s" % k, ob["characters_per_member"].get(k),
        oa["characters_per_member"].get(k))

head("2. The reading of CLAUDE.md (the six spans)")
row("the_reading_of_claude_md → characters", ob["the_reading_of_claude_md"]["characters"],
    oa["the_reading_of_claude_md"]["characters"])

head("3. The further members")
fb = {m["member"]: m["characters"] for m in before[T1]["the_further_members"]}
fa = {m["member"]: m["characters"] for m in after[T1]["the_further_members"]}
for k in list(fb) + [k for k in fa if k not in fb]:
    row(k, fb.get(k), fa.get(k))

head("4. The arc dispatches and the arc reports")
for field in ("the_arc_dispatches", "the_arc_reports"):
    for k in ("count", "characters_total", "characters_mean", "characters_max"):
        row("%s → %s" % (field, k), before[T1][field][k], after[T1][field][k])

head("5. The Cowork boot chain")
cb = {m["member"]: m["characters"] for m in before[T1]["the_cowork_boot_chain"]}
ca = {m["member"]: m["characters"] for m in after[T1]["the_cowork_boot_chain"]}
for k in list(cb) + [k for k in ca if k not in cb]:
    row(k, cb.get(k), ca.get(k))
tb = [m for m in before[T1]["the_cowork_boot_chain"] if "the_three" in m][0]
ta = [m for m in after[T1]["the_cowork_boot_chain"] if "the_three" in m][0]
print()
print("The three latest entries — before: %s; after: %s." % (
    ", ".join("%s (%s)" % (r["name"], "{:,}".format(r["characters"])) for r in tb["the_three"]),
    ", ".join("%s (%s)" % (r["name"], "{:,}".format(r["characters"])) for r in ta["the_three"])))

head("6. Totals by side")
row("Claude Code → without_the_injected_copy_of_CLAUDE_md",
    before[T1]["totals_by_side"][CC]["without_the_injected_copy_of_CLAUDE_md"],
    after[T1]["totals_by_side"][CC]["without_the_injected_copy_of_CLAUDE_md"])
row("Claude Code → with_it", before[T1]["totals_by_side"][CC]["with_it"],
    after[T1]["totals_by_side"][CC]["with_it"])
row("Cowork → characters", before[T1]["totals_by_side"][CW]["characters"],
    after[T1]["totals_by_side"][CW]["characters"])

head("7. Table 2, the six spans partitioned — totals")
for k in ("characters_of_the_six_spans", "sub_block_count", "archive_class_characters",
          "doubt_defaulted_characters"):
    row(k, before[T2]["totals"][k], after[T2]["totals"][k])

print()
print("**After only — values that did not exist before**")
print()
cca = after[T1]["totals_by_side"][CC]
print("- `under_ruling_2_of_2026_11_01`: {:,} (with_it {:,} less the six spans {:,})".format(
    cca["under_ruling_2_of_2026_11_01"], cca["with_it"],
    oa["the_reading_of_claude_md"]["characters"]))
for field in ("the_arc_dispatches", "the_arc_reports"):
    print("- `%s` → `the_invariant_share`, whole:" % field)
    print()
    print("```json")
    print(json.dumps(after[T1][field]["the_invariant_share"], indent=1, ensure_ascii=False))
    print("```")
    print()
print("- `the_arc_reports` → `the_appendices_beside_them`, whole:")
print()
print("```json")
print(json.dumps(after[T1]["the_arc_reports"]["the_appendices_beside_them"], indent=1,
                 ensure_ascii=False))
print("```")
print()
ap = {k: v for k, v in after[T1]["the_reports_with_an_appendix_beside_them"].items()
      if k != "the_pairs"}
print("- `the_reports_with_an_appendix_beside_them`, without `the_pairs`:")
print()
print("```json")
print(json.dumps(ap, indent=1, ensure_ascii=False))
print("```")
print()
print("| The report | Report proper (characters) | Appendix (characters) | Appendix share of the two |")
print("|---|---|---|---|")
for p in after[T1]["the_reports_with_an_appendix_beside_them"]["the_pairs"]:
    print("| `%s` | {:,} | {:,} | %.2f %% |".format(p["characters_of_the_report_proper"],
                                                  p["characters_of_the_appendix"])
          % (p["the_report"], p["the_appendix_share_of_the_two_percent"]))

print()
print("**The second table — per arc member, after only**")
for field in ("the_arc_dispatches", "the_arc_reports"):
    print()
    print("*%s*" % field)
    print()
    print("| # | Name | Characters | Predecessor | Share % |")
    print("|---|---|---|---|---|")
    for i, m in enumerate(after[T1][field]["the_population"], 1):
        s = m["shared_with_the_predecessor"]
        print("| %d | `%s` | {:,} | %s | %s |".format(m["characters"])
              % (i, m["name"], ("`%s`" % m["the_predecessor"]) if m["the_predecessor"] else "—",
                 ("%.2f" % s["share_percent"]) if s else "—"))
````

## A29 — 3(d) — its output, run on the before-artifact (`git show d17a84afdbfbf78c16ff4514df63185fad114a5c:tools/audit/per_session_reading.json`) and the after-artifact as 3(c) left it

`t3d_table.md`:

````

**1. The ordinary session-start read (imported)**

| Value | Before | After | Difference |
|---|---|---|---|
| total_characters | 248,426 | 237,414 | -11,012 |
| characters_per_member → CLAUDE.md | 105,876 | 105,441 | -435 |
| characters_per_member → STATUS.md | 11,997 | 11,657 | -340 |
| characters_per_member → DECISIONS.md | 127,727 | 117,490 | -10,237 |
| characters_per_member → tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids | 2,826 | 2,826 | +0 |

**2. The reading of CLAUDE.md (the six spans)**

| Value | Before | After | Difference |
|---|---|---|---|
| the_reading_of_claude_md → characters | 105,876 | 105,441 | -435 |

**3. The further members**

| Value | Before | After | Difference |
|---|---|---|---|
| CLAUDE.md, the whole file as the executing sessions report it injected at boot | 169,617 | 169,182 | -435 |
| BUILD_AND_TEST.md | 27,236 | 27,236 | +0 |
| cowork_audit_protocol.md, the dispatch-protocol section | 108,389 | 108,389 | +0 |
| the blind derivation of L3, whole | 126,702 | 126,702 | +0 |

**4. The arc dispatches and the arc reports**

| Value | Before | After | Difference |
|---|---|---|---|
| the_arc_dispatches → count | 30 | 30 | +0 |
| the_arc_dispatches → characters_total | 4,982,224 | 4,982,224 | +0 |
| the_arc_dispatches → characters_mean | 166,074 | 166,074 | +0 |
| the_arc_dispatches → characters_max | 259,912 | 259,912 | +0 |
| the_arc_reports → count | 30 | 30 | +0 |
| the_arc_reports → characters_total | 3,741,155 | 3,741,155 | +0 |
| the_arc_reports → characters_mean | 124,705 | 124,705 | +0 |
| the_arc_reports → characters_max | 520,923 | 520,923 | +0 |

**5. The Cowork boot chain**

| Value | Before | After | Difference |
|---|---|---|---|
| entry 118, the bridge-fault section | 2,075 | 2,075 | +0 |
| entry 152, items (v) to (x) | 3,580 | 3,580 | +0 |
| entry 169, whole | 24,913 | 24,913 | +0 |
| entry 291, whole | 9,655 | 9,655 | +0 |
| the three handoff entry files with the latest add-commits | 46,985 | 22,955 | -24,030 |

The three latest entries — before: cowork_handoff_entry_four_hundred_and_sixty_one.md (15,962), cowork_handoff_entry_four_hundred_and_sixty_two.md (14,669), cowork_handoff_entry_four_hundred_and_sixty_three.md (16,354); after: cowork_handoff_entry_four_hundred_and_seventy_three.md (7,122), cowork_handoff_entry_four_hundred_and_seventy_two.md (7,261), cowork_handoff_entry_four_hundred_and_seventy_six.md (8,572).

**6. Totals by side**

| Value | Before | After | Difference |
|---|---|---|---|
| Claude Code → without_the_injected_copy_of_CLAUDE_md | 709,543 | 674,501 | -35,042 |
| Claude Code → with_it | 879,160 | 843,683 | -35,477 |
| Cowork → characters | 1,008,362 | 973,320 | -35,042 |

**7. Table 2, the six spans partitioned — totals**

| Value | Before | After | Difference |
|---|---|---|---|
| characters_of_the_six_spans | 105,876 | 105,441 | -435 |
| sub_block_count | 106 | 106 | +0 |
| archive_class_characters | 14,269 | 13,834 | -435 |
| doubt_defaulted_characters | 90,909 | 90,909 | +0 |

**After only — values that did not exist before**

- `under_ruling_2_of_2026_11_01`: 738,242 (with_it 843,683 less the six spans 105,441)
- `the_arc_dispatches` → `the_invariant_share`, whole:

```json
{
 "members_with_a_predecessor": 29,
 "their_characters": 4883215,
 "their_characters_on_lines_shared_with_the_predecessor": 1579730,
 "share_percent": 32.35,
 "how_a_line_is_shared": "a line of the member, with its line ending, counts as shared when the predecessor holds the same line not already matched; the order of lines is ignored; whitespace-only lines are counted apart and are not in the share. A line changed by one character counts as not shared, and a short common line counts as shared wherever it stands."
}
```

- `the_arc_reports` → `the_invariant_share`, whole:

```json
{
 "members_with_a_predecessor": 29,
 "their_characters": 3680373,
 "their_characters_on_lines_shared_with_the_predecessor": 699415,
 "share_percent": 19.0,
 "how_a_line_is_shared": "a line of the member, with its line ending, counts as shared when the predecessor holds the same line not already matched; the order of lines is ignored; whitespace-only lines are counted apart and are not in the share. A line changed by one character counts as not shared, and a short common line counts as shared wherever it stands."
}
```

- `the_arc_reports` → `the_appendices_beside_them`, whole:

```json
{
 "count": 0,
 "characters_total": 0,
 "how_these_relate_to_the_sizes_above": "every size above is of the report proper only; an appendix file is sized here and in `the_reports_with_an_appendix_beside_them`, never added to the report's own size"
}
```

- `the_reports_with_an_appendix_beside_them`, without `the_pairs`:

```json
{
 "the_folder": "records/cc/reports",
 "how_a_pair_is_found": "every file of the folder whose name ends `_appendix.md`, beside the report named by its stem; an appendix with no report beside it is a STOP",
 "read_by": "Cowork: the report proper in full under the user's rule of 2026-09-03, the appendix at need (Ruling 4 of the 2026-11-01 record)",
 "count": 4,
 "characters_of_the_reports_proper": 131829,
 "characters_of_the_appendices": 578857
}
```

| The report | Report proper (characters) | Appendix (characters) | Appendix share of the two |
|---|---|---|---|
| `cc_report_pruning_rulings_execution_2026_11_01.md` | 25,664 | 88,629 | 77.55 % |
| `cc_report_pruning_rulings_fourth_execution_2026_11_02.md` | 42,897 | 261,900 | 85.93 % |
| `cc_report_pruning_rulings_reexecution_2026_11_01.md` | 30,008 | 73,269 | 70.94 % |
| `cc_report_pruning_rulings_third_execution_2026_11_01.md` | 33,260 | 155,059 | 82.34 % |

**The second table — per arc member, after only**

*the_arc_dispatches*

| # | Name | Characters | Predecessor | Share % |
|---|---|---|---|---|
| 1 | `cc_instruction_l3_comparison_tabulation_2026_10_18.md` | 99,009 | — | — |
| 2 | `cc_instruction_l3_comparison_tabulation_second_2026_10_18.md` | 80,466 | `cc_instruction_l3_comparison_tabulation_2026_10_18.md` | 34.45 |
| 3 | `cc_instruction_l3_comparison_tabulation_third_2026_10_19.md` | 84,717 | `cc_instruction_l3_comparison_tabulation_second_2026_10_18.md` | 51.52 |
| 4 | `cc_instruction_l3_comparison_tabulation_fourth_2026_10_19.md` | 92,356 | `cc_instruction_l3_comparison_tabulation_third_2026_10_19.md` | 54.89 |
| 5 | `cc_instruction_l3_comparison_tabulation_fifth_2026_10_19.md` | 98,630 | `cc_instruction_l3_comparison_tabulation_fourth_2026_10_19.md` | 54.37 |
| 6 | `cc_instruction_l3_comparison_tabulation_sixth_2026_10_19.md` | 111,310 | `cc_instruction_l3_comparison_tabulation_fifth_2026_10_19.md` | 49.58 |
| 7 | `cc_instruction_l3_comparison_tabulation_seventh_2026_10_19.md` | 126,198 | `cc_instruction_l3_comparison_tabulation_sixth_2026_10_19.md` | 43.83 |
| 8 | `cc_instruction_l3_comparison_tabulation_eighth_2026_10_19.md` | 136,728 | `cc_instruction_l3_comparison_tabulation_seventh_2026_10_19.md` | 46.98 |
| 9 | `cc_instruction_l3_comparison_tabulation_ninth_2026_10_20.md` | 153,800 | `cc_instruction_l3_comparison_tabulation_eighth_2026_10_19.md` | 36.61 |
| 10 | `cc_instruction_l3_comparison_tabulation_tenth_2026_10_20.md` | 172,851 | `cc_instruction_l3_comparison_tabulation_ninth_2026_10_20.md` | 37.21 |
| 11 | `cc_instruction_l3_comparison_tabulation_eleventh_2026_10_20.md` | 156,452 | `cc_instruction_l3_comparison_tabulation_tenth_2026_10_20.md` | 34.20 |
| 12 | `cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md` | 153,985 | `cc_instruction_l3_comparison_tabulation_eleventh_2026_10_20.md` | 43.63 |
| 13 | `cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md` | 171,675 | `cc_instruction_l3_comparison_tabulation_twelfth_2026_10_20.md` | 38.78 |
| 14 | `cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md` | 185,731 | `cc_instruction_l3_comparison_tabulation_thirteenth_2026_10_21.md` | 39.69 |
| 15 | `cc_instruction_l3_comparison_tabulation_fifteenth_2026_10_24.md` | 181,526 | `cc_instruction_l3_comparison_tabulation_fourteenth_2026_10_23.md` | 30.31 |
| 16 | `cc_instruction_l3_comparison_tabulation_sixteenth_2026_10_24.md` | 169,864 | `cc_instruction_l3_comparison_tabulation_fifteenth_2026_10_24.md` | 30.15 |
| 17 | `cc_instruction_l3_comparison_tabulation_seventeenth_2026_10_24.md` | 177,296 | `cc_instruction_l3_comparison_tabulation_sixteenth_2026_10_24.md` | 28.01 |
| 18 | `cc_instruction_l3_comparison_tabulation_eighteenth_2026_10_25.md` | 190,948 | `cc_instruction_l3_comparison_tabulation_seventeenth_2026_10_24.md` | 27.84 |
| 19 | `cc_instruction_l3_comparison_tabulation_nineteenth_2026_10_26.md` | 205,990 | `cc_instruction_l3_comparison_tabulation_eighteenth_2026_10_25.md` | 28.44 |
| 20 | `cc_instruction_l3_comparison_tabulation_twentieth_2026_10_26.md` | 224,366 | `cc_instruction_l3_comparison_tabulation_nineteenth_2026_10_26.md` | 27.30 |
| 21 | `cc_instruction_l3_comparison_tabulation_twenty_first_2026_10_26.md` | 210,734 | `cc_instruction_l3_comparison_tabulation_twentieth_2026_10_26.md` | 26.49 |
| 22 | `cc_instruction_l3_comparison_tabulation_twenty_second_2026_10_26.md` | 166,056 | `cc_instruction_l3_comparison_tabulation_twenty_first_2026_10_26.md` | 26.30 |
| 23 | `cc_instruction_l3_comparison_tabulation_twenty_third_2026_10_26.md` | 164,756 | `cc_instruction_l3_comparison_tabulation_twenty_second_2026_10_26.md` | 21.72 |
| 24 | `cc_instruction_l3_comparison_tabulation_twenty_fourth_2026_10_27.md` | 188,439 | `cc_instruction_l3_comparison_tabulation_twenty_third_2026_10_26.md` | 21.85 |
| 25 | `cc_instruction_l3_comparison_tabulation_twenty_fifth_2026_10_27.md` | 212,059 | `cc_instruction_l3_comparison_tabulation_twenty_fourth_2026_10_27.md` | 30.72 |
| 26 | `cc_instruction_l3_comparison_tabulation_twenty_sixth_2026_10_27.md` | 239,614 | `cc_instruction_l3_comparison_tabulation_twenty_fifth_2026_10_27.md` | 30.13 |
| 27 | `cc_instruction_l3_comparison_tabulation_twenty_seventh_2026_10_28.md` | 259,912 | `cc_instruction_l3_comparison_tabulation_twenty_sixth_2026_10_27.md` | 29.35 |
| 28 | `cc_instruction_l3_comparison_tabulation_twenty_eighth_2026_10_30.md` | 233,425 | `cc_instruction_l3_comparison_tabulation_twenty_seventh_2026_10_28.md` | 24.08 |
| 29 | `cc_instruction_l3_comparison_tabulation_twenty_ninth_2026_10_31.md` | 181,526 | `cc_instruction_l3_comparison_tabulation_twenty_eighth_2026_10_30.md` | 15.90 |
| 30 | `cc_instruction_l3_comparison_tabulation_thirtieth_2026_10_31.md` | 151,805 | `cc_instruction_l3_comparison_tabulation_twenty_ninth_2026_10_31.md` | 28.75 |

*the_arc_reports*

| # | Name | Characters | Predecessor | Share % |
|---|---|---|---|---|
| 1 | `cc_report_l3_comparison_tabulation_2026_10_18.md` | 60,782 | — | — |
| 2 | `cc_report_l3_comparison_tabulation_second_2026_10_18.md` | 46,542 | `cc_report_l3_comparison_tabulation_2026_10_18.md` | 28.33 |
| 3 | `cc_report_l3_comparison_tabulation_third_2026_10_19.md` | 54,986 | `cc_report_l3_comparison_tabulation_second_2026_10_18.md` | 35.53 |
| 4 | `cc_report_l3_comparison_tabulation_fourth_2026_10_19.md` | 61,723 | `cc_report_l3_comparison_tabulation_third_2026_10_19.md` | 50.21 |
| 5 | `cc_report_l3_comparison_tabulation_fifth_2026_10_19.md` | 69,767 | `cc_report_l3_comparison_tabulation_fourth_2026_10_19.md` | 43.10 |
| 6 | `cc_report_l3_comparison_tabulation_sixth_2026_10_19.md` | 56,766 | `cc_report_l3_comparison_tabulation_fifth_2026_10_19.md` | 41.57 |
| 7 | `cc_report_l3_comparison_tabulation_seventh_2026_10_19.md` | 57,458 | `cc_report_l3_comparison_tabulation_sixth_2026_10_19.md` | 33.40 |
| 8 | `cc_report_l3_comparison_tabulation_eighth_2026_10_19.md` | 72,330 | `cc_report_l3_comparison_tabulation_seventh_2026_10_19.md` | 20.31 |
| 9 | `cc_report_l3_comparison_tabulation_ninth_2026_10_20.md` | 62,175 | `cc_report_l3_comparison_tabulation_eighth_2026_10_19.md` | 33.98 |
| 10 | `cc_report_l3_comparison_tabulation_tenth_2026_10_20.md` | 74,764 | `cc_report_l3_comparison_tabulation_ninth_2026_10_20.md` | 20.89 |
| 11 | `cc_report_l3_comparison_tabulation_eleventh_2026_10_20.md` | 79,270 | `cc_report_l3_comparison_tabulation_tenth_2026_10_20.md` | 29.01 |
| 12 | `cc_report_l3_comparison_tabulation_twelfth_2026_10_20.md` | 134,126 | `cc_report_l3_comparison_tabulation_eleventh_2026_10_20.md` | 21.69 |
| 13 | `cc_report_l3_comparison_tabulation_thirteenth_2026_10_21.md` | 117,568 | `cc_report_l3_comparison_tabulation_twelfth_2026_10_20.md` | 23.11 |
| 14 | `cc_report_l3_comparison_tabulation_fourteenth_2026_10_23.md` | 63,286 | `cc_report_l3_comparison_tabulation_thirteenth_2026_10_21.md` | 28.04 |
| 15 | `cc_report_l3_comparison_tabulation_fifteenth_2026_10_24.md` | 71,420 | `cc_report_l3_comparison_tabulation_fourteenth_2026_10_23.md` | 30.46 |
| 16 | `cc_report_l3_comparison_tabulation_sixteenth_2026_10_24.md` | 73,117 | `cc_report_l3_comparison_tabulation_fifteenth_2026_10_24.md` | 37.06 |
| 17 | `cc_report_l3_comparison_tabulation_seventeenth_2026_10_24.md` | 89,385 | `cc_report_l3_comparison_tabulation_sixteenth_2026_10_24.md` | 31.95 |
| 18 | `cc_report_l3_comparison_tabulation_eighteenth_2026_10_25.md` | 114,017 | `cc_report_l3_comparison_tabulation_seventeenth_2026_10_24.md` | 25.82 |
| 19 | `cc_report_l3_comparison_tabulation_nineteenth_2026_10_26.md` | 79,766 | `cc_report_l3_comparison_tabulation_eighteenth_2026_10_25.md` | 24.78 |
| 20 | `cc_report_l3_comparison_tabulation_twentieth_2026_10_26.md` | 139,118 | `cc_report_l3_comparison_tabulation_nineteenth_2026_10_26.md` | 13.56 |
| 21 | `cc_report_l3_comparison_tabulation_twenty_first_2026_10_26.md` | 221,926 | `cc_report_l3_comparison_tabulation_twentieth_2026_10_26.md` | 11.54 |
| 22 | `cc_report_l3_comparison_tabulation_twenty_second_2026_10_26.md` | 152,663 | `cc_report_l3_comparison_tabulation_twenty_first_2026_10_26.md` | 23.34 |
| 23 | `cc_report_l3_comparison_tabulation_twenty_third_2026_10_26.md` | 167,250 | `cc_report_l3_comparison_tabulation_twenty_second_2026_10_26.md` | 9.30 |
| 24 | `cc_report_l3_comparison_tabulation_twenty_fourth_2026_10_27.md` | 132,154 | `cc_report_l3_comparison_tabulation_twenty_third_2026_10_26.md` | 11.90 |
| 25 | `cc_report_l3_comparison_tabulation_twenty_fifth_2026_10_27.md` | 228,900 | `cc_report_l3_comparison_tabulation_twenty_fourth_2026_10_27.md` | 7.74 |
| 26 | `cc_report_l3_comparison_tabulation_twenty_sixth_2026_10_27.md` | 246,250 | `cc_report_l3_comparison_tabulation_twenty_fifth_2026_10_27.md` | 15.18 |
| 27 | `cc_report_l3_comparison_tabulation_twenty_seventh_2026_10_28.md` | 260,055 | `cc_report_l3_comparison_tabulation_twenty_sixth_2026_10_27.md` | 16.72 |
| 28 | `cc_report_l3_comparison_tabulation_twenty_eighth_2026_10_30.md` | 142,049 | `cc_report_l3_comparison_tabulation_twenty_seventh_2026_10_28.md` | 28.81 |
| 29 | `cc_report_l3_comparison_tabulation_twenty_ninth_2026_10_31.md` | 90,619 | `cc_report_l3_comparison_tabulation_twenty_eighth_2026_10_30.md` | 20.66 |
| 30 | `cc_report_l3_comparison_tabulation_thirtieth_2026_10_31.md` | 520,923 | `cc_report_l3_comparison_tabulation_twenty_ninth_2026_10_31.md` | 3.49 |
````

## A30 — This appendix's own assembler, the scratch script `assemble_appendix.py`

`assemble_appendix.py`:

````
"""Assemble the appendix of the per-session reading extension report from the saved printouts,
verbatim, each under a heading naming its command and step. Writes the file into the reports folder."""
import io

S = r"C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\3a011105-6c3e-4b45-8b5c-24c09588efa3\scratchpad" + "\\"
OUT = r"C:\s\MS\records\cc\reports\cc_report_per_session_reading_extension_2026_11_02_appendix.md"

SECTIONS = [
    ("A1", "0(c) — `python tools/audit/changed_paths.py`, the A1 enumeration, whole", ["t0c_changed_paths.txt"]),
    ("A2", "0(d) — the last-bytes check: the scratch script `t0d_last_bytes.py`, then its output", ["t0d_last_bytes.py", "t0d_out.txt"]),
    ("A3", "0(e) — `python tools/audit/gen_evidence_pin_membership.py --check`", ["t0e_evpin.txt"]),
    ("A4", "0(f) — THE OPENING CAPTURE, `python tools/audit/gen_guard_state.py --check`, whole", ["cap0_opening.txt"]),
    ("A5", "0(f) — the start tip's `guard_state.json` summary against the opening capture: the scratch script `t0f_summary.py`, then its output (its set difference compares invocations without their arguments on one side; the summary line carries both)", ["t0f_summary.py", "t0f_summary_out.txt"]),
    ("A6", "0(f) — `python tools/audit/gen_guard_classification.py --check` (exit 2)", ["t0f_classification.txt"]),
    ("A7", "Every capture comparison — the scratch script `cmp_captures.py`", ["cmp_captures.py"]),
    ("A8", "1(a) — `python tools/audit/gen_derivation_boot_pack.py --check`, before the edit", ["t1a_bootpack_before.txt"]),
    ("A9", "1(c) — `python tools/audit/gen_derivation_boot_pack.py --check`, after the edit (byte-identical to A8 by `cmp`)", ["t1c_bootpack_after.txt"]),
    ("A10", "1(c) — the capture after Task 1, `python tools/audit/gen_guard_state.py --check`, whole", ["cap1_after_task1.txt"]),
    ("A11", "1(c) — the opening capture against the capture after Task 1", ["cmp_cap0_cap1.txt"]),
    ("A12", "2(a) — `python tools/audit/gen_per_session_reading.py` (write mode), the tool as it stood", ["t2a_write.txt"]),
    ("A13", "2(a) — `python tools/audit/gen_per_session_reading.py --check`", ["t2a_check.txt"]),
    ("A14", "2(b) — `git diff` of the tool's `<T1>` blob `851f98ec…` against the extended blob `6d3f308c…`", ["t2b_tool_diff.txt"]),
    ("A15", "2(c) — the planted-fault proofs: the scratch script `t2c_proofs.py`, then its output", ["t2c_proofs.py", "t2c_out.txt"]),
    ("A16", "2(d) — `python tools/audit/gen_per_session_reading.py` (write mode), the extended tool", ["t2d_write.txt"]),
    ("A17", "2(d) — `time python tools/audit/gen_per_session_reading.py --check`", ["t2d_check.txt"]),
    ("A18", "2(e) — the comparison with the baseline at this tree: the scratch script `t2e_compare.py`", ["t2e_compare.py"]),
    ("A19", "2(e) — its output, every per-path record and the classed summary, whole", ["t2e_out.txt"]),
    ("A20", "2(f) — the capture after Task 2, `python tools/audit/gen_guard_state.py --check`, whole", ["cap2_after_task2.txt"]),
    ("A21", "2(f) — the capture after Task 1 against the capture after Task 2", ["cmp_cap1_cap2.txt"]),
    ("A22", "3(b) — `python tools/audit/gen_status_batch_bound.py --apply`, then its first `--check`", ["t3b_apply.txt", "t3b_check.txt"]),
    ("A23", "3(b) — the four archive checks, re-run whole at the close tree", ["t3b_rerun_bound_check.txt", "t3b_rerun_split_status.txt", "t3b_rerun_residue.txt", "t3b_rerun_archive_pass.txt"]),
    ("A24", "3(c) — the regenerations' write-mode outputs (read size, defense share, the per-session tool)", ["t3c_ssr_write.txt", "t3c_defense_write.txt", "t3c_psr_write.txt"]),
    ("A25", "3(c) — every check of 3(c), re-run whole at the close tree", ["t3c_rerun_evpin.txt", "t3c_rerun_ssr.txt", "t3c_rerun_defense.txt", "t3c_rerun_l0l1.txt", "t3c_rerun_l3.txt", "t3c_rerun_bootpack.txt", "t3c_rerun_psr.txt"]),
    ("A26", "3(c) — the artifact diffs: the scratch script `t3c_diffs.py`, its output, then each diff whole", ["t3c_diffs.py", "t3c_diffs_out.txt", "t3c_diff_session_start_read_size.txt", "t3c_diff_defense_share.txt", "t3c_diff_l0_l1_outgoing_population.txt", "t3c_diff_l3_outgoing_population.txt", "t3c_diff_per_session_reading.txt"]),
    ("A27", "3(c) — the scratch script that re-ran the checks of A23 and A25, then its output", ["t3_checks_rerun.py", "t3_checks_rerun_out.txt"]),
    ("A28", "3(d) — THE BEFORE AND AFTER TABLE: the scratch script `t3d_before_after.py`", ["t3d_before_after.py"]),
    ("A29", "3(d) — its output, run on the before-artifact (`git show d17a84afdbfbf78c16ff4514df63185fad114a5c:tools/audit/per_session_reading.json`) and the after-artifact as 3(c) left it", ["t3d_table.md"]),
    ("A30", "This appendix's own assembler, the scratch script `assemble_appendix.py`", ["assemble_appendix.py"]),
]

buf = io.StringIO()
buf.write("# Appendix — raw printouts of the per-session reading extension batch (2026-11-02)\n\n")
buf.write("> The appendix of `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md`, under Ruling 4 of\n"
          "> `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`. Every printout below is verbatim,\n"
          "> copied from the scratch file the command wrote, each under a heading naming its command and step. Nothing the\n"
          "> report proper needs is only here.\n\n")
for code, title, files in SECTIONS:
    buf.write("## %s — %s\n\n" % (code, title))
    for f in files:
        text = open(S + f, encoding="utf-8").read()
        buf.write("`%s`:\n\n" % f)
        fence = "````" if "```" in text else "```"
        buf.write(fence + "\n" + text + ("" if text.endswith("\n") else "\n") + fence + "\n\n")
data = buf.getvalue().rstrip("\n") + "\n"
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(data)
print("wrote %s, %d characters, %d bytes" % (OUT, len(data), len(data.encode("utf-8"))))
````
