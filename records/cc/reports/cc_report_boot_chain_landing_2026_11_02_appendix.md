# Appendix — the boot-chain landing, 2026-11-02: the raw printouts

Beside `records/cc/reports/cc_report_boot_chain_landing_2026_11_02.md` (Ruling 4 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`, as relayed by the dispatch). Every block below is a raw printout, verbatim, under a heading naming its command and step. Nothing the report proper needs is here. Scratch directory of origin: `C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\04215257-2fa9-42f1-9ba3-3af5891ba839\scratchpad`.

## A1. Start state 3 — `python tools/audit/gen_per_session_reading.py --check` at boot, before Task 0 (exit 2)

~~~~
STOP: a member of a derived population has no add-commit: records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_eight.md
~~~~

## A2. 0(c) — A1: `python tools/audit/changed_paths.py`, whole

~~~~
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_boot_chain_landing_2026_11_02.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_eight.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_seven.md
??	records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md
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
398 changed path record(s) [worktree]
~~~~

## A3. 0(d) — the scratch script `lastbytes.py`

~~~~
"""0(d): for each blob named on the command line, print its size, its zero-byte count and its last 70 bytes."""
import subprocess
import sys

for blob in sys.argv[1:]:
    data = subprocess.run(["git", "cat-file", "blob", blob], capture_output=True, check=True).stdout
    print("blob", blob)
    print("  size", len(data))
    print("  zero bytes", data.count(b"\x00"))
    print("  ends with newline", data.endswith(b"\n"))
    print("  last 70 bytes", repr(data[-70:]))
~~~~

## A4. 0(d) — its output over the four landing blobs

~~~~
blob 1dc34966fa8c41e3cb9dc5b4e7862fc0a6b64fbd
  size 43966
  zero bytes 0
  ends with newline True
  last 70 bytes b"record. **No step, prediction or stop\nchanged but item 1's wording.**\n"
blob 3813f2d46c1809c3d6bcb3f768e8324c7fbad685
  size 7636
  zero bytes 0
  ends with newline True
  last 70 bytes b' "narrow"; "continue";\n"continue"; "B"; "continue"; "continue"; "A".*\n'
blob 4e96afb6df20e8e58b75ddea9a7fe32a49e47f42
  size 8286
  zero bytes 0
  ends with newline True
  last 70 bytes b'continue"; "continue"; "B"; "continue"; "continue"; "A"; "continue".*\n'
blob 07f6813c7f20b8c3019f2dacbd02d2253270127f
  size 6622
  zero bytes 0
  ends with newline True
  last 70 bytes b'\'s words: the opening instruction;\n"narrow"; "continue"; "continue".*\n'
~~~~

## A5. 0(e) — `python tools/audit/gen_evidence_pin_membership.py --check` before (exit 1)

~~~~
STALE vs the derivation: evidence_pin_membership.json does not re-derive
~~~~

## A6. 0(e) — `python tools/audit/gen_evidence_pin_membership.py` (write mode, exit 0)

~~~~
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 172
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

## A7. 0(e) — `--check` after (exit 0)

~~~~
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 172
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

## A8. 0(e) — `git diff f460a683… c9aa4e85…` (the artifact at the start tip against the regenerated blob)

~~~~
diff --git a/f460a683346cfa4241852538227075a298bcec76 b/c9aa4e8563dd7c8ef03780c8bf562e324e5c4db7
index f460a68334..c9aa4e8563 100644
--- a/f460a683346cfa4241852538227075a298bcec76
+++ b/c9aa4e8563dd7c8ef03780c8bf562e324e5c4db7
@@ -17,7 +17,7 @@
  },
  "counts": {
   "generated_ratification_documents": 7,
-  "ruling_records_read": 171,
+  "ruling_records_read": 172,
   "members": 7,
   "members_pinned": 5,
   "members_unresolved": 0,
@@ -312,6 +312,7 @@
   "records/cowork/rulings/cowork_rulings_2026_10_18_l3_keyword_list_sitting.md",
   "records/cowork/rulings/cowork_rulings_2026_10_26_l3_position_57_sitting.md",
   "records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md",
   "records/cowork/rulings/cowork_rulings_oi345_oi342_2026_08_07.md"
  ],
  "named_in_a_ruling_record_but_not_generated": {
~~~~

## A9. 0(f) — the opening capture, `python tools/audit/gen_guard_state.py --check` (exit 1), whole

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

## A10. 0(f) — the start tip's `tools/audit/guard_state.json` → `summary`, read from `git show f01c8874…:tools/audit/guard_state.json`

~~~~
{
 "run": 83,
 "passing": 70,
 "failing": 13,
 "failing_tools": [
  "tools/audit/gen_phase3_gate_partition.py --check",
  "tools/audit/gen_filing_convention_application.py --check",
  "tools/audit/gen_artifact_inventory.py --check",
  "tools/audit/gen_artifact_inventory_surface.py --check",
  "tools/audit/gen_test_construction_evidence.py --check",
  "tools/audit/gen_retirement_caller_check.py --check",
  "tools/audit/decisions/apply_soft_discard.py --check",
  "tools/audit/decisions/apply_residue_discard.py --check",
  "tools/audit/gen_epoch_write_path.py --check",
  "tools/audit/gen_recognizer_establishment_sort.py --check",
  "tools/audit/decisions/gen_cluster_dispositions.py --verify",
  "tools/audit/decisions/gen_home_classification.py --check",
  "tools/audit/decisions/gen_phase1p_delegation_bar.py --check"
 ]
}
~~~~

## A11. 0(f) — `python tools/audit/gen_guard_classification.py --check` (exit 2)

~~~~
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_per_session_reading.py', 'tools/audit/gen_withheld_family_reading.py']
~~~~

## A12. 1(a) — `git grep -n "cowork_handoff_entry_two_hundred_and_ninety_one" -- tools/` (exit 0)

~~~~
tools/audit/gen_per_session_reading.py:200:ENTRY_291 = HANDOFF_FOLDER + "/cowork_handoff_entry_two_hundred_and_ninety_one.md"
tools/audit/per_session_reading.json:1330:    "path": "records/cowork/handoff/cowork_handoff_entry_two_hundred_and_ninety_one.md",
~~~~

## A13. 1(c) — the scratch script `t1c_compare.py`

~~~~
"""1(c): compare entry 291's four inserted lines with the record's four quoted lines (61-64),
each with its leading '> ' removed; also check the inserted lines' indentation and line endings.
Both files are read from git blobs named on the command line (entry-291 working blob, record blob)."""
import subprocess
import sys

def blob_lines(blob):
    data = subprocess.run(["git", "cat-file", "blob", blob], capture_output=True, check=True).stdout
    return data, data.decode("utf-8").split("\n")

entry_data, entry = blob_lines(sys.argv[1])
record_data, record = blob_lines(sys.argv[2])

anchor = [i for i, l in enumerate(entry) if "sizes at a listing." in l]
print("anchor lines (1-based):", [i + 1 for i in anchor])
a = anchor[0]
inserted = entry[a + 1:a + 5]
print("line after the four:", repr(entry[a + 5]))
quoted = record[60:64]
ok = True
for n, (ins, quo) in enumerate(zip(inserted, quoted), 1):
    ins_ok = ins.startswith("   > ") and not ins.startswith("    ")
    ins_text = ins[len("   > "):]
    quo_text = quo[len("> "):] if quo.startswith("> ") else None
    equal = ins_text == quo_text
    ok = ok and ins_ok and equal
    print("line %d: indentation 3 spaces + '> ' %s; text equal %s" % (n, ins_ok, equal))
print("carriage returns in entry 291:", entry_data.count(b"\r"))
print("RESULT:", "EQUAL" if ok else "NOT EQUAL")
~~~~

## A14. 1(c) — its output (entry 291 blob `f0d3abae…`, record blob `3813f2d4…`)

~~~~
anchor lines (1-based): [91]
line after the four: '4. **It writes the paper sizing (§2), lands it, and reports it to the user in plain words.** It asks nothing'
line 1: indentation 3 spaces + '> ' True; text equal True
line 2: indentation 3 spaces + '> ' True; text equal True
line 3: indentation 3 spaces + '> ' True; text equal True
line 4: indentation 3 spaces + '> ' True; text equal True
carriage returns in entry 291: 0
RESULT: EQUAL
~~~~

## A15. 1(d) — the capture after the insertion, `python tools/audit/gen_guard_state.py --check` (exit 1), whole

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

## A16. 1(d) — the comparison with the opening capture

~~~~
cmp cap_open.txt cap_t1.txt -> exit 0 (byte-identical)
~~~~

## A17. 3(a) — the keyword search over `STATUS.md` (case-insensitive, the 26 `L3_KEYWORDS` terms plus `repeat` and `tie`, each as a substring; the Grep tool's `-o` output)

~~~~
28:phrase
~~~~

## A18. 3(b) — the forward-bound tool's authored constants at `f01c8874…:tools/audit/gen_status_batch_bound.py` (search of the scratch copy)

~~~~
2463:BASE_COMMIT = "37d8ebb68f60a62f01b1f618288fd95a8a9a6512"
2689:PREVIOUS_BATCH_DISPATCH = "cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md"
2970:ACT_DATE = "2026-11-02"
2971:DISPATCH = "cc_instruction_per_session_reading_extension_2026_11_02.md"
3237:TASK = "Task 3"
3244:MOVE_KIND = "ordinary"
3248:PREVIOUS_AIMINGS = [
~~~~

## A19. 3(b) — `python tools/audit/gen_status_batch_bound.py --apply` (exit 0)

~~~~
wrote tools\audit\status_batch_bound.json
  entries moved: 4, 2,377 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
~~~~

## A20. 3(b) — `python tools/audit/gen_status_batch_bound.py --check` (exit 0)

~~~~
  entries moved: 4, 2,377 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
~~~~

## A21. 3(b) — `python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md` (exit 0)

~~~~
  STATUS.md / STATUS_ARCHIVE.md: moved 131 span(s), 457,949 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
~~~~

## A22. 3(b) — `python tools/audit/gen_status_residue_move.py --check` (exit 0)

~~~~
  candidates: 17, moved 16, left at site by the reading 1
  characters moved: 46,105
  byte-present in the companion exactly once: True
  absent from the must-read:                  True
  every flagged entry still at site:          True
~~~~

## A23. 3(b) — `python tools/audit/gen_status_archive_pass.py --check` (exit 0)

~~~~
  dated entries moved: 52
  at the pass commit, the live file was exactly base-minus-range: True
  the moved block is verbatim in the archive at HEAD:             True
  the moved block is absent from the live file at HEAD:           True
~~~~

## A24. 3(c) 1 — `gen_evidence_pin_membership.py --check` (exit 0)

~~~~
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 172
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

## A25. 3(c) 2 — `gen_session_start_read_size.py --check` before (exit 1)

~~~~
STALE vs the measurement: session_start_read_size.json does not re-derive
~~~~

## A26. 3(c) 2 — `gen_session_start_read_size.py` (write mode, exit 0)

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
    STATUS.md                                                                 11146
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 236903
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 236903 [ruled membership]  (-130218, -35.47%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 236903 [ruled membership]  (-59929, -20.19%)  <- CROSSES A REGIME BOUNDARY
~~~~

## A27. 3(c) 2 — `gen_session_start_read_size.py --check` after (exit 0)

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
    STATUS.md                                                                 11146
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 236903
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 236903 [ruled membership]  (-130218, -35.47%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 236903 [ruled membership]  (-59929, -20.19%)  <- CROSSES A REGIME BOUNDARY
~~~~

## A28. 3(c) 2 — `gen_defense_share.py --check` before (exit 1)

~~~~
STALE vs the measurement: defense_share.json does not re-derive
~~~~

## A29. 3(c) 2 — `gen_defense_share.py` (write mode, exit 0)

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
    of the whole session-start read (236903): 5.47%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
~~~~

## A30. 3(c) 2 — `gen_defense_share.py --check` after (exit 0)

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
    of the whole session-start read (236903): 5.47%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
~~~~

## A31. 3(c) 3 — `gen_l3_outgoing_population.py --check` before (exit 1)

~~~~
STALE vs the derivation: l3_outgoing_population.json does not re-derive
~~~~

## A32. 3(c) 3 — `gen_l3_outgoing_population.py` (write mode, exit 0)

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

## A33. 3(c) 3 — `gen_l3_outgoing_population.py --check` after (exit 0)

~~~~
l3_outgoing_population.json re-derives
~~~~

## A34. 3(c) 3 — `gen_l0_l1_outgoing_population.py --check` (exit 0; not regenerated)

~~~~
l0_l1_outgoing_population.json re-derives
~~~~

## A35. 3(c) 4 — `gen_derivation_boot_pack.py --check` (exit 0; not regenerated)

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

## A36. 3(c) 5 — `gen_per_session_reading.py --check` before (exit 1)

~~~~
STALE vs the measurement: per_session_reading.json does not re-derive
~~~~

## A37. 3(c) 5 — `gen_per_session_reading.py` (write mode, exit 0)

~~~~
wrote tools/audit/per_session_reading.json
  the ordinary session-start read (imported) 236903
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  invariant share: dispatches 32.35 %, reports 19.00 %
  reports with an appendix beside them 5: reports proper 195320, appendices 773904 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674447
  Cowork, per sitting, in the shape of the sitting of entry 461: 973751
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
~~~~

## A38. 3(c) 5 — `gen_per_session_reading.py --check` after (exit 0)

~~~~
the per-session reading measurement re-derives
  the ordinary session-start read (imported) 236903
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  invariant share: dispatches 32.35 %, reports 19.00 %
  reports with an appendix beside them 5: reports proper 195320, appendices 773904 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674447
  Cowork, per sitting, in the shape of the sitting of entry 461: 973751
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
~~~~

## A39. 3(c) — `python tools/audit/changed_paths.py` after the regenerations, whole

~~~~
 M	STATUS.md
 M	STATUS_ARCHIVE.md
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
402 changed path record(s) [worktree]
~~~~

## A40. 3(c) — the scratch script `diff_artifacts.py`

~~~~
"""3(c): diff each moved artifact against its blob at a named commit, between explicit blob hashes.
Usage: diff_artifacts.py <base-commit> <out-dir> <path> [<path> ...]
For each path: the base blob (git rev-parse <base>:<path>), the working blob (git hash-object -w),
and `git diff <base-blob> <work-blob>` written to <out-dir>/<basename>.diff."""
import os
import subprocess
import sys

def git(*args):
    return subprocess.run(["git", *args], capture_output=True, check=True, text=True).stdout.strip()

base, out_dir, paths = sys.argv[1], sys.argv[2], sys.argv[3:]
for path in paths:
    base_blob = git("rev-parse", "%s:%s" % (base, path))
    work_blob = git("hash-object", "-w", path)
    diff = subprocess.run(["git", "diff", base_blob, work_blob], capture_output=True, check=True).stdout
    out = os.path.join(out_dir, os.path.basename(path) + ".diff")
    with open(out, "wb") as f:
        f.write(diff)
    print("%s  base %s  work %s  diff %d bytes -> %s" % (path, base_blob, work_blob, len(diff), out))
~~~~

## A41. 3(c) — its index (base blob at `f01c8874…`, working blob, diff size)

~~~~
tools/audit/session_start_read_size.json  base f86a3fe23483ac3761a9ae68bd2770b5f2b8b2fe  work 1bb887339a5a10ec35a363927f482b58aaa5eb5b  diff 2198 bytes -> C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/04215257-2fa9-42f1-9ba3-3af5891ba839/scratchpad\session_start_read_size.json.diff
tools/audit/defense_share.json  base a0ba4c0782ccf3cc15e8093e06ecf55d8086a550  work 2ad87e2668e5688af2d286806181d9c91d81ef58  diff 1145 bytes -> C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/04215257-2fa9-42f1-9ba3-3af5891ba839/scratchpad\defense_share.json.diff
tools/audit/l3_outgoing_population.json  base 8aac2cfc00123a2858e989cd8dfc99ac66b27a61  work b196fe6e8c6d19cdf48c7a9af3c0bca38570b137  diff 1389 bytes -> C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/04215257-2fa9-42f1-9ba3-3af5891ba839/scratchpad\l3_outgoing_population.json.diff
tools/audit/per_session_reading.json  base 83c4da75b939920042f116b8749f60ea4d7e473e  work 7bd7885cffd03cb92bf632e594610bf16cb0e9e5  diff 5979 bytes -> C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/04215257-2fa9-42f1-9ba3-3af5891ba839/scratchpad\per_session_reading.json.diff
tools/audit/status_batch_bound.json  base 663c6981adb2cfc889309a1de6feeb721a651fa2  work 7341bd0b7033bb2e71d8f361c170a01684c9b6b3  diff 5016 bytes -> C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/04215257-2fa9-42f1-9ba3-3af5891ba839/scratchpad\status_batch_bound.json.diff
tools/audit/gen_status_batch_bound.py  base d66f4869702b6bfa920636bbdc9f4ba9f86d6f98  work 97637f2c5d7d59338b4a19f10f29bd278f0f244d  diff 4777 bytes -> C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/04215257-2fa9-42f1-9ba3-3af5891ba839/scratchpad\gen_status_batch_bound.py.diff
STATUS.md  base bd2447879dd675345476f75bf8c3dfb1a22e0b90  work 748b4b265363bbc64b3352eab5ee46667b3f25fb  diff 6438 bytes -> C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/04215257-2fa9-42f1-9ba3-3af5891ba839/scratchpad\STATUS.md.diff
STATUS_ARCHIVE.md  base 4ef7d7f1a35c51ccd0aa66272701892bedb4c604  work dd4b444f097912f60933222f2191c1ba2e07d89f  diff 3590 bytes -> C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/04215257-2fa9-42f1-9ba3-3af5891ba839/scratchpad\STATUS_ARCHIVE.md.diff
~~~~

## A42. 3(c) — `session_start_read_size.json`

~~~~
diff --git a/f86a3fe23483ac3761a9ae68bd2770b5f2b8b2fe b/1bb887339a5a10ec35a363927f482b58aaa5eb5b
index f86a3fe234..1bb887339a 100644
--- a/f86a3fe23483ac3761a9ae68bd2770b5f2b8b2fe
+++ b/1bb887339a5a10ec35a363927f482b58aaa5eb5b
@@ -176,11 +176,11 @@
   },
   "characters_per_member": {
    "CLAUDE.md": 105441,
-   "STATUS.md": 11657,
+   "STATUS.md": 11146,
    "DECISIONS.md": 117490,
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
   },
-  "total_characters": 237414,
+  "total_characters": 236903,
   "further_spans_of_the_same_artifact_NOT_counted_into_the_read": {
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows": {
     "characters": 62498,
@@ -276,10 +276,10 @@
    "from_commit": "1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
    "from_total": 367121,
    "from_regime": "whole-file practice",
-   "to_total": 237414,
+   "to_total": 236903,
    "to_regime": "ruled membership",
-   "change_in_characters": -129707,
-   "change_percent": -35.33,
+   "change_in_characters": -130218,
+   "change_percent": -35.47,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   },
@@ -287,10 +287,10 @@
    "from_commit": "594074e1e1900079e449d2b79a38920d21bca6e6",
    "from_total": 296832,
    "from_regime": "whole-file practice",
-   "to_total": 237414,
+   "to_total": 236903,
    "to_regime": "ruled membership",
-   "change_in_characters": -59418,
-   "change_percent": -20.02,
+   "change_in_characters": -59929,
+   "change_percent": -20.19,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   }
~~~~

## A43. 3(c) — `defense_share.json`

~~~~
diff --git a/a0ba4c0782ccf3cc15e8093e06ecf55d8086a550 b/2ad87e2668e5688af2d286806181d9c91d81ef58
index a0ba4c0782..2ad87e2668 100644
--- a/a0ba4c0782ccf3cc15e8093e06ecf55d8086a550
+++ b/2ad87e2668e5688af2d286806181d9c91d81ef58
@@ -77,7 +77,7 @@
  ],
  "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
   "the_six_session_start_spans": 105441,
-  "the_whole_ordinary_session_start_read": 237414,
+  "the_whole_ordinary_session_start_read": 236903,
   "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked defense; the second says how much of the WHOLE boot it is. A share quoted against one of them is not the share against the other."
  },
  "per_span": [
@@ -142,7 +142,7 @@
   "characters_had_every_clause_been_closed_at_the_next_marked_clause": 51684,
   "characters_had_every_clause_run_to_its_paragraph_end": 160906,
   "share_of_the_six_session_start_spans": 12.29,
-  "share_of_the_whole_ordinary_session_start_read": 5.46
+  "share_of_the_whole_ordinary_session_start_read": 5.47
  },
  "every_clause_published_so_the_tables_reach_is_inspectable_rather_than_asserted": [
   {
~~~~

## A44. 3(c) — `l3_outgoing_population.json`

~~~~
diff --git a/8aac2cfc00123a2858e989cd8dfc99ac66b27a61 b/b196fe6e8c6d19cdf48c7a9af3c0bca38570b137
index 8aac2cfc00..b196fe6e8c 100644
--- a/8aac2cfc00123a2858e989cd8dfc99ac66b27a61
+++ b/b196fe6e8c6d19cdf48c7a9af3c0bca38570b137
@@ -20111,7 +20111,7 @@
      "the_statement": "hit, outside the specification document set, not dispositioned by this comparison; reachable by the mining map",
      "hit_records": [
       {
-       "line_number": 22,
+       "line_number": 20,
        "term": "phrase",
        "tier": "admitting",
        "line": "*★ ARCHIVED 2026-08-17, THE SECOND ACT — the dated entries that PREDATE (or paraphrase) the OI-222 pointer convention fell to `operative-rule-text` in the pinned measurement and stayed when the block above was cleared. They were READ one by one and moved verbatim to `STATUS_ARCHIVE.md` by `records/cc/instructions/cc_instruction_preparation_seventh.md` Task 1, under Ruling 3 of `records/cowork/rulings/cowork_rulings_2026_08_17_sixth_return.md`, which brings them under Ruling 4's own line. **One candidate did NOT move and is flagged:** the navigational paragraph at the foot of this file is not a completed batch's dated record but a live pointer to the archive and to the gate policy, so the read-before-move safeguard left it at site. The per-entry reconciliation is re-derived by `tools/audit/gen_status_residue_move.py --check`.*"
~~~~

## A45. 3(c) — `per_session_reading.json`

~~~~
diff --git a/83c4da75b939920042f116b8749f60ea4d7e473e b/7bd7885cffd03cb92bf632e594610bf16cb0e9e5
index 83c4da75b9..7bd7885cff 100644
--- a/83c4da75b939920042f116b8749f60ea4d7e473e
+++ b/7bd7885cffd03cb92bf632e594610bf16cb0e9e5
@@ -15,11 +15,11 @@
    "its_one_home": "`tools/audit/session_start_read_size.json`, written by `tools/audit/gen_session_start_read_size.py`; what stands here is that tool's own `measure` called at the tree, and its total is checked against that artifact on every run",
    "characters_per_member": {
     "CLAUDE.md": 105441,
-    "STATUS.md": 11657,
+    "STATUS.md": 11146,
     "DECISIONS.md": 117490,
     "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
    },
-   "total_characters": 237414,
+   "total_characters": 236903,
    "the_reading_of_claude_md": {
     "regime": "ruled membership",
     "characters": 105441
@@ -1332,7 +1332,7 @@
     "read_by": "Cowork, per sitting",
     "the_mandate_class": "unwritten practice",
     "the_record_that_mandates_it": "the writing side's own boot instruction — entry 291 §4 step 3 and entry 169's Boot block; no user ruling names these reads",
-    "characters": 9655
+    "characters": 10140
    },
    {
     "member": "the three handoff entry files with the latest add-commits",
@@ -1345,28 +1345,28 @@
      "the_writing_sides_read": "unwritten practice"
     },
     "the_record_that_mandates_it": "the standing clause `Every dispatch's read-first block names the CURRENT HANDOVER BLOCK`, which this repository carries as numbered entry files; the writing side's three is its own practice",
-    "the_population_count": 396,
+    "the_population_count": 398,
     "the_three": [
-     {
-      "name": "cowork_handoff_entry_four_hundred_and_seventy_three.md",
-      "added_in_commit": "bfd15c7fdd6e010a2ad163cfb0dddd26e46239a1",
-      "added_at_unix_time": 1793605025,
-      "characters": 7122
-     },
-     {
-      "name": "cowork_handoff_entry_four_hundred_and_seventy_two.md",
-      "added_in_commit": "bfd15c7fdd6e010a2ad163cfb0dddd26e46239a1",
-      "added_at_unix_time": 1793605025,
-      "characters": 7261
-     },
      {
       "name": "cowork_handoff_entry_four_hundred_and_seventy_six.md",
       "added_in_commit": "dd06b5fea97a0f7e1fee4ffa35b7aebdc704ebd5",
       "added_at_unix_time": 1793616911,
       "characters": 8572
+     },
+     {
+      "name": "cowork_handoff_entry_four_hundred_and_seventy_eight.md",
+      "added_in_commit": "60d9048cda3b0a33b216e3a4e468b29dbe5d14d8",
+      "added_at_unix_time": 1793626075,
+      "characters": 6606
+     },
+     {
+      "name": "cowork_handoff_entry_four_hundred_and_seventy_seven.md",
+      "added_in_commit": "60d9048cda3b0a33b216e3a4e468b29dbe5d14d8",
+      "added_at_unix_time": 1793626075,
+      "characters": 8234
      }
     ],
-    "characters": 22955
+    "characters": 23412
    }
   ],
   "totals_by_side": {
@@ -1374,7 +1374,7 @@
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 237414
+      "characters": 236903
      },
      {
       "member": "BUILD_AND_TEST.md",
@@ -1394,13 +1394,13 @@
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 22955
+      "characters": 23412
      }
     ],
-    "without_the_injected_copy_of_CLAUDE_md": 674501,
-    "with_it": 843683,
+    "without_the_injected_copy_of_CLAUDE_md": 674447,
+    "with_it": 843629,
     "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, 169182 characters",
-    "under_ruling_2_of_2026_11_01": 738242,
+    "under_ruling_2_of_2026_11_01": 738188,
     "how_ruling_2_moves_it": "Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`: the injected copy is the read of the six spans, so their file-tool read (105441 characters) leaves the sum and the injected copy stays; the eight-line check's own reads are not sized here",
     "left_out_and_said_so": "the previous report at the portions a dispatch orders, the reading file at its ordered portions, the ruling records a dispatch orders — varies per dispatch and is not sized here"
    },
@@ -1408,7 +1408,7 @@
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 237414
+      "characters": 236903
      },
      {
       "member": "entry 118, the bridge-fault section",
@@ -1424,11 +1424,11 @@
      },
      {
       "member": "entry 291, whole",
-      "characters": 9655
+      "characters": 10140
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 22955
+      "characters": 23412
      },
      {
       "member": "the latest report of the arc, whole: cc_report_l3_comparison_tabulation_thirtieth_2026_10_31.md",
@@ -1439,7 +1439,7 @@
       "characters": 151805
      }
     ],
-    "characters": 973320,
+    "characters": 973751,
     "left_out_and_said_so": "the verification reads at the objects (the reading file at its sections, the guard state, the ref files, the away-returns close) — varies per batch and is not sized here"
    }
   }
@@ -3825,7 +3825,7 @@
     "characters_had_every_clause_been_closed_at_the_next_marked_clause": 51684,
     "characters_had_every_clause_run_to_its_paragraph_end": 160906,
     "share_of_the_six_session_start_spans": 12.29,
-    "share_of_the_whole_ordinary_session_start_read": 5.46
+    "share_of_the_whole_ordinary_session_start_read": 5.47
    },
    "per_span": [
     {
@@ -3885,7 +3885,7 @@
    ],
    "the_two_denominators": {
     "the_six_session_start_spans": 105441,
-    "the_whole_ordinary_session_start_read": 237414
+    "the_whole_ordinary_session_start_read": 236903
    },
    "how_these_relate_to_the_sums_above": "a marked clause lies INSIDE a sub-block, so these values overlap table 2's sums and are never added to them"
   }
~~~~

## A46. 3(b) — `status_batch_bound.json`

~~~~
diff --git a/663c6981adb2cfc889309a1de6feeb721a651fa2 b/7341bd0b7033bb2e71d8f361c170a01684c9b6b3
index 663c6981ad..7341bd0b70 100644
--- a/663c6981adb2cfc889309a1de6feeb721a651fa2
+++ b/7341bd0b7033bb2e71d8f361c170a01684c9b6b3
@@ -1,7 +1,7 @@
 {
  "what_this_is": "RULING 4's FORWARD BOUND, applied at one batch close: which of the then-previous batch's STATUS.md entries moved to the archive, and the mechanical proof that nothing was lost or altered in transit (#12). Every figure here is computed; none is transcribed (D-431).",
  "generated_by": "tools/audit/gen_status_batch_bound.py",
- "dispatch": "cc_instruction_per_session_reading_extension_2026_11_02.md, Task 3",
+ "dispatch": "cc_instruction_boot_chain_landing_2026_11_02.md, Task 3",
  "★_every_previous_aiming_of_this_tool_kept_rather_than_replaced": [
   {
    "executing_act": "cc_instruction_preparation_sixth.md, Task 1",
@@ -795,46 +795,52 @@
    "base_commit": "37d8ebb68f60a62f01b1f618288fd95a8a9a6512",
    "the_then_previous_batch": "cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md",
    "the_kind_of_move": "ordinary"
+  },
+  {
+   "executing_act": "cc_instruction_boot_chain_landing_2026_11_02.md, Task 3",
+   "base_commit": "3dbade755a80520af21db8618d6e8ece5d923c07",
+   "the_then_previous_batch": "cc_instruction_per_session_reading_extension_2026_11_02.md",
+   "the_kind_of_move": "ordinary"
   }
  ],
  "the_ruling": "Ruling 4 of cowork_rulings_2026_08_17_governing_surface_split.md: an entry is SUPERSEDED the moment a later batch's close exists; the site keeps only the latest batch's entries, and every future batch close moves the then-previous batch's entries in the same act that writes its own.",
- "base_commit": "37d8ebb68f60a62f01b1f618288fd95a8a9a6512",
- "the_then_previous_batch": "cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md",
+ "base_commit": "3dbade755a80520af21db8618d6e8ece5d923c07",
+ "the_then_previous_batch": "cc_instruction_per_session_reading_extension_2026_11_02.md",
  "the_kind_of_move": "ordinary",
  "entries_moved": 4,
- "characters_moved": 2639,
+ "characters_moved": 2377,
  "the_moved": [
   {
    "line_at_base": 8,
-   "characters": 1910,
-   "sha256": "89e0904d187e6d63f84ef1c526cd3ff45d3df157e8f7a7e4038e7c451bf90e2f",
+   "characters": 1704,
+   "sha256": "5bff028e24b2960ede3288060a13640885a94b49646668540a0e832ca04b8d03",
    "membership": "names the dispatch",
    "the_one_declared_adjustment_applied": true,
-   "opening": "*2026-11-02 (CC — `records/cc/instructions/cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md`, Task 3, the close. **★★ RULING 1 OF 2026-11"
+   "opening": "*2026-11-02 (CC — `records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md`, Task 3, the close. **★★ STEP 4's SECOND DISPAT"
   },
   {
    "line_at_base": 10,
-   "characters": 281,
-   "sha256": "fe77343ea031ea1c3a1b9ee085e02f054440cf733acd4fc389ab53078bc77518",
+   "characters": 233,
+   "sha256": "4ce8c791d7305c6381d8ce21800d8bdd8f6ab7688c5218ed005662fde02c6f16",
    "membership": "says `Same dispatch`, in the run below the entry that names it",
    "the_one_declared_adjustment_applied": false,
-   "opening": "*2026-11-02 (CC — Same dispatch, Task 2. **TWO FORMER WORDINGS OF `CLAUDE.md`'S DECISION-SURFACE BLOCK MOVED VERBATIM TO `CLAUDE_ARCHIVE.md`, UNDER RU"
+   "opening": "*2026-11-02 (CC — Same dispatch, Task 2. **THE PER-SESSION READING MEASUREMENT IS EXTENDED BY THREE ADDITIONS AND REGENERATED.** **POINTER** — `record"
   },
   {
    "line_at_base": 12,
-   "characters": 224,
-   "sha256": "c80095d3ff8d1ef78f46e7c709b7f72413e4f77d93ffbafb2ef5094f642a6375",
+   "characters": 228,
+   "sha256": "f049f7171efefd4093eab394efe67ec44c61409fa942570f8fae22b7aadc3dec",
    "membership": "says `Same dispatch`, in the run below the entry that names it",
    "the_one_declared_adjustment_applied": false,
-   "opening": "*2026-11-02 (CC — Same dispatch, Task 1. **THE L3 DERIVATION BOOT PACK IS FROZEN**, its deriving session having run. **POINTER** — `records/cc/reports"
+   "opening": "*2026-11-02 (CC — Same dispatch, Task 1. **ONE STALE COMMENT IN THE BOOT-PACK TOOL IS CORRECTED**, its former wording kept. **POINTER** — `records/cc/"
   },
   {
    "line_at_base": 14,
-   "characters": 224,
-   "sha256": "605008e67a3d3548cab0843863ee7ad27450bdfd293cc932ab798a5f59f7d9e4",
+   "characters": 212,
+   "sha256": "a13f475548e7c9a0a2542e2bdc02a48ed20f80536e1c334cffd30ebdea75afa6",
    "membership": "says `Same dispatch`, in the run below the entry that names it",
    "the_one_declared_adjustment_applied": false,
-   "opening": "*2026-11-02 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRIES 472 TO 475 ARE LANDED**, as they stood. **POINTER** — `records/cc/reports"
+   "opening": "*2026-11-02 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRY 476 ARE LANDED**, as they stood. **POINTER** — `records/cc/reports/cc_repor"
   }
  ],
  "reconciliation": {
~~~~

## A47. 3(b) — `tools/audit/gen_status_batch_bound.py`

~~~~
diff --git a/d66f4869702b6bfa920636bbdc9f4ba9f86d6f98 b/97637f2c5d7d59338b4a19f10f29bd278f0f244d
index d66f486970..97637f2c5d 100644
--- a/d66f4869702b6bfa920636bbdc9f4ba9f86d6f98
+++ b/97637f2c5d7d59338b4a19f10f29bd278f0f244d
@@ -2460,7 +2460,18 @@ OUT = os.path.join(HERE, "status_batch_bound.json")
 # entries. The then-previous batch is that fourth execution; its close entry's `Last updated: ` prefix was
 # MOVED to this batch's close entry in the same edit that wrote this batch's entries, before `--apply` ran.
 # **NO COUNT OF THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431).
-BASE_COMMIT = "37d8ebb68f60a62f01b1f618288fd95a8a9a6512"
+#
+# ★★ RE-AIMED 2026-11-02 BY `records/cc/instructions/cc_instruction_boot_chain_landing_2026_11_02.md`
+# Task 3(b). `BASE_COMMIT` was `37d8ebb68f60a62f01b1f618288fd95a8a9a6512` and is now
+# `3dbade755a80520af21db8618d6e8ece5d923c07`: this batch's Task 1 commit, which is its LAST TASK COMMIT
+# before the close. That commit carries no `STATUS.md` change, so its `STATUS.md` object is the one both refs
+# carried when this batch opened (the blob `bd2447879dd675345476f75bf8c3dfb1a22e0b90`, at the commit
+# `f01c88747e7fe5719d79e63f9a1d2f3d3622bcfa` and at `3dbade75…`, established at `git rev-parse` of each,
+# one command per commit) — and it carries the per-session reading extension's entries at the head of the
+# dated entries. The then-previous batch is that extension; its close entry's `Last updated: ` prefix was
+# MOVED to this batch's close entry in the same edit that wrote this batch's entries, before `--apply` ran.
+# **NO COUNT OF THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431).
+BASE_COMMIT = "3dbade755a80520af21db8618d6e8ece5d923c07"
 
 # The batch whose entries this aiming moves, named by its dispatch because that is what each of its
 # entries says of itself. On an ORDINARY move it is the THEN-PREVIOUS batch and Ruling 4's forward
@@ -2686,7 +2697,10 @@ BASE_COMMIT = "37d8ebb68f60a62f01b1f618288fd95a8a9a6512"
 # *(`PREVIOUS_BATCH_DISPATCH` read "cc_instruction_pruning_rulings_third_execution_2026_11_01.md" while
 # `cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md` was the executing act; it is re-stated here
 # for `cc_instruction_per_session_reading_extension_2026_11_02.md`, whose then-previous batch is that one.)*
-PREVIOUS_BATCH_DISPATCH = "cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md"
+# *(`PREVIOUS_BATCH_DISPATCH` read "cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md" while
+# `cc_instruction_per_session_reading_extension_2026_11_02.md` was the executing act; it is re-stated here
+# for `cc_instruction_boot_chain_landing_2026_11_02.md`, whose then-previous batch is that one.)*
+PREVIOUS_BATCH_DISPATCH = "cc_instruction_per_session_reading_extension_2026_11_02.md"
 
 # ★ THE ACT DATE IS THE DAY THE MOVE RAN, NOT THE DAY THE DISPATCH WAS WRITTEN. This executing
 # dispatch is dated 2026-09-07 and this batch ran on 2026-09-07, so the two agree; the field is kept
@@ -2967,8 +2981,12 @@ PREVIOUS_BATCH_DISPATCH = "cc_instruction_pruning_rulings_fourth_execution_2026_
 # while that batch was the executing act; both are re-stated here for
 # `cc_instruction_per_session_reading_extension_2026_11_02.md`, dated 2026-11-02 in its file name, whose move
 # ran on 2026-11-02, so the two dates agree and `ACT_DATE` keeps its value.)*
+# *(`ACT_DATE` read "2026-11-02" and `DISPATCH` `cc_instruction_per_session_reading_extension_2026_11_02.md`
+# while that batch was the executing act; both are re-stated here for
+# `cc_instruction_boot_chain_landing_2026_11_02.md`, dated 2026-11-02 in its file name, whose move ran on
+# 2026-11-02, so the two dates agree and `ACT_DATE` keeps its value.)*
 ACT_DATE = "2026-11-02"
-DISPATCH = "cc_instruction_per_session_reading_extension_2026_11_02.md"
+DISPATCH = "cc_instruction_boot_chain_landing_2026_11_02.md"
 # TASK IS A CHOICE, DECLARED RATHER THAN IMPLIED. On an ORDINARY move the executing dispatch orders
 # the move and this batch's own `STATUS.md` entries in the same numbered task, so both halves of "the
 # same act that writes its own entries" sit inside it, and that task is what the archive header names.
@@ -3899,6 +3917,10 @@ PREVIOUS_AIMINGS = [
      "base_commit": "37d8ebb68f60a62f01b1f618288fd95a8a9a6512",
      "the_then_previous_batch": "cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md",
      "the_kind_of_move": "ordinary"},
+    {"executing_act": "cc_instruction_boot_chain_landing_2026_11_02.md, Task 3",
+     "base_commit": "3dbade755a80520af21db8618d6e8ece5d923c07",
+     "the_then_previous_batch": "cc_instruction_per_session_reading_extension_2026_11_02.md",
+     "the_kind_of_move": "ordinary"},
 ]
 
 HEADER_ORDINARY = (
~~~~

## A48. 3(a)/3(b) — `STATUS.md`

~~~~
diff --git a/bd2447879dd675345476f75bf8c3dfb1a22e0b90 b/748b4b265363bbc64b3352eab5ee46667b3f25fb
index bd2447879d..748b4b2653 100644
--- a/bd2447879dd675345476f75bf8c3dfb1a22e0b90
+++ b/748b4b265363bbc64b3352eab5ee46667b3f25fb
@@ -5,13 +5,11 @@
 > Historical entries live in `STATUS_ARCHIVE.md` (reference-only, NOT part of the session-start
 > read) — a superseded entry moves there instead of accumulating here.
 
-*Last updated: 2026-11-02 (CC — `records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md`, Task 3, the close. **★★ STEP 4's SECOND DISPATCH OF THE PRUNING ITERATION: THE PER-SESSION READING MEASUREMENT IS EXTENDED AND RE-RUN.** ★ `tools/audit/gen_per_session_reading.py` now also measures three things: what each dispatch and each report of the L3 comparison arc shares line for line with the one before it; the size of the appendix file that stands beside a report under Ruling 4 of 2026-11-01, every report of the folder with one listed with both sizes; and the Claude Code side's per-batch total under Ruling 2 of 2026-11-01, the six spans' file-tool read replaced by the injected copy. The extension was proved on eight planted cases, and its regenerated artifact, compared with a run of the unextended tool at the same tree, moved nothing but additions and its `generated_for` field. ★ The measurement was re-run, and the report sets the values before the pruning rulings and after them side by side. ★ One stale comment in `tools/audit/gen_derivation_boot_pack.py` was corrected — all five built subjects are frozen — its former wording kept and that tool's check output byte-identical before and after. **One measurement tool extended and one comment of another tool corrected; no other tool edited or added. No algorithm change; no decisions-register entry, no `D-NNN`, no open-items row**; no `src/` file, build, test, golden, corpus of scores or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md` — and no figure is restated here (**D-431**).)*
+*Last updated: 2026-11-02 (CC — `records/cc/instructions/cc_instruction_boot_chain_landing_2026_11_02.md`, Task 3, the close. **★★ THE BOOT-CHAIN LANDING: HANDOFF ENTRIES 477 AND 478 AND THE USER'S RULING RECORD OF 2026-11-02 ARE LANDED, AND ENTRY 291 CARRIES THE RECORD'S AMENDMENT.** ★ The record, `records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md`, holds the user's two rulings of that day on the Cowork start-up chain and on the dispatch form: a new Cowork session reads its start-up chain at named sections rather than as whole entries, and a dispatch points to a standing clause by its section and sends no one through earlier dispatches. ★ The record's amendment paragraph was inserted into handoff entry 291 §4 step 3, directly after that step's last line, the wording above it kept. ★ This dispatch is the first written under the record's Ruling 2: it points to standing clauses by section and sends no one through earlier dispatches. **No tool edited or added but the forward-bound tool's re-aiming; no algorithm change; no decisions-register entry, no `D-NNN`, no open-items row**; no `src/` file, build, test, golden, corpus of scores or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_boot_chain_landing_2026_11_02.md` — and no figure is restated here (**D-431**).)*
 
-*2026-11-02 (CC — Same dispatch, Task 2. **THE PER-SESSION READING MEASUREMENT IS EXTENDED BY THREE ADDITIONS AND REGENERATED.** **POINTER** — `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md` (**D-431**).)*
+*2026-11-02 (CC — Same dispatch, Task 1. **THE RECORD'S AMENDMENT PARAGRAPH IS INSERTED INTO HANDOFF ENTRY 291 §4 STEP 3**, the wording above it kept. **POINTER** — `records/cc/reports/cc_report_boot_chain_landing_2026_11_02.md` (**D-431**).)*
 
-*2026-11-02 (CC — Same dispatch, Task 1. **ONE STALE COMMENT IN THE BOOT-PACK TOOL IS CORRECTED**, its former wording kept. **POINTER** — `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md` (**D-431**).)*
-
-*2026-11-02 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRY 476 ARE LANDED**, as they stood. **POINTER** — `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md` (**D-431**).)*
+*2026-11-02 (CC — Same dispatch, Task 0. **THIS DISPATCH, HANDOFF ENTRIES 477 AND 478 AND THE 2026-11-02 RULING RECORD ARE LANDED**, as they stood. **POINTER** — `records/cc/reports/cc_report_boot_chain_landing_2026_11_02.md` (**D-431**).)*
 
 *2026-09-02 (CC — **★★ THE L0/L1 COMPARISON IS OPEN AND SEVEN OF ITS TWENTY-NINE DOCUMENTS ARE TABULATED; THE READING FILE EXISTS.** `ratification_surfaces/cowork_comparison_l0_l1_reading.md` places **every statement of positions 1 to 7** — the two `ARCHITECTURE.md` sections and all five root design documents, which is the whole of Ruling 32's items 1 and 2 — under exactly one of the phase definition's five dispositions, with the current-text axis carried beside it. ★ **EVERY DISPOSITION IS A PROPOSAL AND NOTHING IS APPLIED**: no outgoing text is edited, the derivation is untouched, and the file states in terms that the user is asked to rule nothing in it. ★ **THE STOP IS AT A MEMBER BOUNDARY AND THE REMAINDER IS UNTOUCHED RATHER THAN PARTLY WORKED** (**D-672**): positions 8 to 29 have not been read for tabulation, quoted, counted or dispositioned, the file's own §0 says which are done and where the next dispatch resumes, and the three sections that can only be written once the population is complete are marked NOT YET WRITTEN rather than left to look empty. ★ **THE INDEPENDENCE RECORD IS RELAYED WHOLE, WITH NO VERDICT WORD ATTACHED** — and the two places where an outgoing statement of this comparison meets a passage the deriving session's own stop-on-meeting record says it SAW are named at the rows, which is a fact the user reads the AGREES verdicts against. ★ **THE ARITHMETIC CLOSES AT EVERY DOCUMENT** and is stated as a sum rather than asserted. Per the OI-222 pointer convention this entry is a **POINTER** — every row, every count and every proposal is the reading file — and no figure is restated here (**D-431**).)*
 
~~~~

## A49. 3(b) — `STATUS_ARCHIVE.md`

~~~~
diff --git a/4ef7d7f1a35c51ccd0aa66272701892bedb4c604 b/dd4b444f097912f60933222f2191c1ba2e07d89f
index 4ef7d7f1a3..dd4b444f09 100644
--- a/4ef7d7f1a35c51ccd0aa66272701892bedb4c604
+++ b/dd4b444f097912f60933222f2191c1ba2e07d89f
@@ -6226,3 +6226,13 @@ the inference era. **The full handover: the 2026-07-28 entry-point block in
 
 *2026-11-02 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRIES 472 TO 475 ARE LANDED**, as they stood. **POINTER** — `records/cc/reports/cc_report_pruning_rulings_fourth_execution_2026_11_02.md` (**D-431**).)*
 
+> **★ RULING 4's FORWARD BOUND, 2026-11-02.** The entries below are the PREVIOUS batch's (`cc_instruction_per_session_reading_extension_2026_11_02.md`), moved verbatim out of `STATUS.md` by `cc_instruction_boot_chain_landing_2026_11_02.md` Task 3 in the same act that wrote this batch's own entries — Ruling 4 of `cowork_rulings_2026_08_17_governing_surface_split.md`: *an entry is SUPERSEDED the moment a later batch's close exists, and the site keeps only the latest batch's entries.* Nothing was edited in transit; the reconciliation is re-derived by `tools/audit/gen_status_batch_bound.py --check`.
+
+*2026-11-02 (CC — `records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md`, Task 3, the close. **★★ STEP 4's SECOND DISPATCH OF THE PRUNING ITERATION: THE PER-SESSION READING MEASUREMENT IS EXTENDED AND RE-RUN.** ★ `tools/audit/gen_per_session_reading.py` now also measures three things: what each dispatch and each report of the L3 comparison arc shares line for line with the one before it; the size of the appendix file that stands beside a report under Ruling 4 of 2026-11-01, every report of the folder with one listed with both sizes; and the Claude Code side's per-batch total under Ruling 2 of 2026-11-01, the six spans' file-tool read replaced by the injected copy. The extension was proved on eight planted cases, and its regenerated artifact, compared with a run of the unextended tool at the same tree, moved nothing but additions and its `generated_for` field. ★ The measurement was re-run, and the report sets the values before the pruning rulings and after them side by side. ★ One stale comment in `tools/audit/gen_derivation_boot_pack.py` was corrected — all five built subjects are frozen — its former wording kept and that tool's check output byte-identical before and after. **One measurement tool extended and one comment of another tool corrected; no other tool edited or added. No algorithm change; no decisions-register entry, no `D-NNN`, no open-items row**; no `src/` file, build, test, golden, corpus of scores or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md` — and no figure is restated here (**D-431**).)*
+
+*2026-11-02 (CC — Same dispatch, Task 2. **THE PER-SESSION READING MEASUREMENT IS EXTENDED BY THREE ADDITIONS AND REGENERATED.** **POINTER** — `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md` (**D-431**).)*
+
+*2026-11-02 (CC — Same dispatch, Task 1. **ONE STALE COMMENT IN THE BOOT-PACK TOOL IS CORRECTED**, its former wording kept. **POINTER** — `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md` (**D-431**).)*
+
+*2026-11-02 (CC — Same dispatch, Task 0. **THIS DISPATCH AND HANDOFF ENTRY 476 ARE LANDED**, as they stood. **POINTER** — `records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md` (**D-431**).)*
+
~~~~

## A50. 3(d) — this scratch script, `build_appendix.py`

~~~~
"""3(d): assemble the appendix from the scratch printouts, each verbatim under a heading naming its
command and step. Reads only files in this scratch directory; writes the one appendix path given."""
import json
import os
import sys

S = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]

def text_of(name):
    data = open(os.path.join(S, name), "rb").read()
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        # the console code page wrote this file (a `§` printed through Windows-1252)
        return data.decode("cp1252")

def start_tip_summary():
    gs = json.loads(text_of("gs_start.json"))
    s = gs["summary"]
    return json.dumps({"run": s["run"], "passing": s["passing"], "failing": s["failing"],
                       "failing_tools": [t["tool"] + " " + " ".join(t.get("args", []))
                                         for t in s["failing_tools"]]}, indent=1, ensure_ascii=False)

LITERAL = {
    "kw": "28:phrase\n",
    "sbb_consts": (
        "2463:BASE_COMMIT = \"37d8ebb68f60a62f01b1f618288fd95a8a9a6512\"\n"
        "2689:PREVIOUS_BATCH_DISPATCH = \"cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md\"\n"
        "2970:ACT_DATE = \"2026-11-02\"\n"
        "2971:DISPATCH = \"cc_instruction_per_session_reading_extension_2026_11_02.md\"\n"
        "3237:TASK = \"Task 3\"\n"
        "3244:MOVE_KIND = \"ordinary\"\n"
        "3248:PREVIOUS_AIMINGS = [\n"),
    "cmp": "cmp cap_open.txt cap_t1.txt -> exit 0 (byte-identical)\n",
}

SECTIONS = [
    ("Start state 3 — `python tools/audit/gen_per_session_reading.py --check` at boot, before Task 0 (exit 2)", "boot_psr_check.txt"),
    ("0(c) — A1: `python tools/audit/changed_paths.py`, whole", "a1_enum.txt"),
    ("0(d) — the scratch script `lastbytes.py`", "lastbytes.py"),
    ("0(d) — its output over the four landing blobs", "lastbytes_out.txt"),
    ("0(e) — `python tools/audit/gen_evidence_pin_membership.py --check` before (exit 1)", "epm_check1.txt"),
    ("0(e) — `python tools/audit/gen_evidence_pin_membership.py` (write mode, exit 0)", "epm_write.txt"),
    ("0(e) — `--check` after (exit 0)", "epm_check2.txt"),
    ("0(e) — `git diff f460a683… c9aa4e85…` (the artifact at the start tip against the regenerated blob)", "epm_diff.txt"),
    ("0(f) — the opening capture, `python tools/audit/gen_guard_state.py --check` (exit 1), whole", "cap_open.txt"),
    ("0(f) — the start tip's `tools/audit/guard_state.json` → `summary`, read from `git show f01c8874…:tools/audit/guard_state.json`", "@summary"),
    ("0(f) — `python tools/audit/gen_guard_classification.py --check` (exit 2)", "gc_open.txt"),
    ("1(a) — `git grep -n \"cowork_handoff_entry_two_hundred_and_ninety_one\" -- tools/` (exit 0)", "t1a_grep.txt"),
    ("1(c) — the scratch script `t1c_compare.py`", "t1c_compare.py"),
    ("1(c) — its output (entry 291 blob `f0d3abae…`, record blob `3813f2d4…`)", "t1c_out.txt"),
    ("1(d) — the capture after the insertion, `python tools/audit/gen_guard_state.py --check` (exit 1), whole", "cap_t1.txt"),
    ("1(d) — the comparison with the opening capture", "@cmp"),
    ("3(a) — the keyword search over `STATUS.md` (case-insensitive, the 26 `L3_KEYWORDS` terms plus `repeat` and `tie`, each as a substring; the Grep tool's `-o` output)", "@kw"),
    ("3(b) — the forward-bound tool's authored constants at `f01c8874…:tools/audit/gen_status_batch_bound.py` (search of the scratch copy)", "@sbb_consts"),
    ("3(b) — `python tools/audit/gen_status_batch_bound.py --apply` (exit 0)", "sbb_apply.txt"),
    ("3(b) — `python tools/audit/gen_status_batch_bound.py --check` (exit 0)", "arc1.txt"),
    ("3(b) — `python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md` (exit 0)", "arc2.txt"),
    ("3(b) — `python tools/audit/gen_status_residue_move.py --check` (exit 0)", "arc3.txt"),
    ("3(b) — `python tools/audit/gen_status_archive_pass.py --check` (exit 0)", "arc4.txt"),
    ("3(c) 1 — `gen_evidence_pin_membership.py --check` (exit 0)", "c1_epm.txt"),
    ("3(c) 2 — `gen_session_start_read_size.py --check` before (exit 1)", "c2_ssrs_check1.txt"),
    ("3(c) 2 — `gen_session_start_read_size.py` (write mode, exit 0)", "c2_ssrs_write.txt"),
    ("3(c) 2 — `gen_session_start_read_size.py --check` after (exit 0)", "c2_ssrs_check2.txt"),
    ("3(c) 2 — `gen_defense_share.py --check` before (exit 1)", "c2_ds_check1.txt"),
    ("3(c) 2 — `gen_defense_share.py` (write mode, exit 0)", "c2_ds_write.txt"),
    ("3(c) 2 — `gen_defense_share.py --check` after (exit 0)", "c2_ds_check2.txt"),
    ("3(c) 3 — `gen_l3_outgoing_population.py --check` before (exit 1)", "c3_l3_check1.txt"),
    ("3(c) 3 — `gen_l3_outgoing_population.py` (write mode, exit 0)", "c3_l3_write.txt"),
    ("3(c) 3 — `gen_l3_outgoing_population.py --check` after (exit 0)", "c3_l3_check2.txt"),
    ("3(c) 3 — `gen_l0_l1_outgoing_population.py --check` (exit 0; not regenerated)", "c3_l0l1_check1.txt"),
    ("3(c) 4 — `gen_derivation_boot_pack.py --check` (exit 0; not regenerated)", "c4_bp_check.txt"),
    ("3(c) 5 — `gen_per_session_reading.py --check` before (exit 1)", "c5_psr_check1.txt"),
    ("3(c) 5 — `gen_per_session_reading.py` (write mode, exit 0)", "c5_psr_write.txt"),
    ("3(c) 5 — `gen_per_session_reading.py --check` after (exit 0)", "c5_psr_check2.txt"),
    ("3(c) — `python tools/audit/changed_paths.py` after the regenerations, whole", "close_enum.txt"),
    ("3(c) — the scratch script `diff_artifacts.py`", "diff_artifacts.py"),
    ("3(c) — its index (base blob at `f01c8874…`, working blob, diff size)", "diff_index.txt"),
    ("3(c) — `session_start_read_size.json`", "session_start_read_size.json.diff"),
    ("3(c) — `defense_share.json`", "defense_share.json.diff"),
    ("3(c) — `l3_outgoing_population.json`", "l3_outgoing_population.json.diff"),
    ("3(c) — `per_session_reading.json`", "per_session_reading.json.diff"),
    ("3(b) — `status_batch_bound.json`", "status_batch_bound.json.diff"),
    ("3(b) — `tools/audit/gen_status_batch_bound.py`", "gen_status_batch_bound.py.diff"),
    ("3(a)/3(b) — `STATUS.md`", "STATUS.md.diff"),
    ("3(b) — `STATUS_ARCHIVE.md`", "STATUS_ARCHIVE.md.diff"),
    ("3(d) — this scratch script, `build_appendix.py`", "build_appendix.py"),
]

parts = [
    "# Appendix — the boot-chain landing, 2026-11-02: the raw printouts\n\n",
    "Beside `records/cc/reports/cc_report_boot_chain_landing_2026_11_02.md` (Ruling 4 of "
    "`records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`, as relayed by the dispatch). "
    "Every block below is a raw printout, verbatim, under a heading naming its command and step. Nothing the "
    "report proper needs is here. Scratch directory of origin: "
    "`C:\\Users\\vince\\AppData\\Local\\Temp\\claude\\c--s-MS\\04215257-2fa9-42f1-9ba3-3af5891ba839\\scratchpad`.\n\n",
]
for n, (title, src) in enumerate(SECTIONS, 1):
    if src == "@summary":
        body = start_tip_summary() + "\n"
    elif src.startswith("@"):
        body = LITERAL[src[1:]]
    else:
        body = text_of(src)
    if not body.endswith("\n"):
        body += "\n"
    parts.append("## A%d. %s\n\n~~~~\n%s~~~~\n\n" % (n, title, body))
parts.append("## Self-check of this appendix\n\nEvery block is a file the run wrote or a tool result copied as "
             "printed; none was edited. The report proper carries the batch's self-check.\n")
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("".join(parts))
print("wrote", OUT, "sections", len(SECTIONS))
~~~~

## Self-check of this appendix

Every block is a file the run wrote or a tool result copied as printed; none was edited. The report proper carries the batch's self-check.
