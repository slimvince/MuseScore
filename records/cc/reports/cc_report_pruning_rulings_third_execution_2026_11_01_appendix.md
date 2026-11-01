# CC report APPENDIX — the pruning iteration, step 4, Rulings 1 and 3 carried out a third time (2026-11-01)

> **STATUS: SESSION REPORT APPENDIX.** The raw printouts of `records/cc/reports/cc_report_pruning_rulings_third_execution_2026_11_01.md`, verbatim, under Ruling 4 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`. Every verdict, count and difference stands in the report proper; this file is read where a verification needs a particular printout. Assembled from the session's scratch files by a scratch script, so every printout is byte-for-byte as the command wrote it.

## 0(b) `git show --stat c483c6968f2de0da68afeb47b48a8807dbe593ed`

````text
commit c483c6968f2de0da68afeb47b48a8807dbe593ed
Author: Vincent Wong <65764495+slimvince@users.noreply.github.com>
Date:   Sun Nov 1 21:40:37 2026 +0100

    End state: the pruning iteration step 4 first dispatch re-executed - guard run at the close tree, the A2 regenerations already met inside the close
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 records/cowork/handoff/cowork_away_returns.md | 44 +++++++++++++++++++++++++++
 tools/audit/guard_state.json                  | 18 +++++------
 2 files changed, 53 insertions(+), 9 deletions(-)
````

## 0(b) `git show --stat bead6080d9d0a720a857ccb2350d90dc19894a91`

````text
commit bead6080d9d0a720a857ccb2350d90dc19894a91
Author: Vincent Wong <65764495+slimvince@users.noreply.github.com>
Date:   Sun Nov 1 21:31:03 2026 +0100

    Close: the pruning iteration step 4 first dispatch re-executed - Rulings 1 and 3, under its dispatch
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 STATUS.md                                          |    4 +-
 STATUS_ARCHIVE.md                                  |    6 +
 ...eport_pruning_rulings_reexecution_2026_11_01.md |  350 +++++
 ...ning_rulings_reexecution_2026_11_01_appendix.md | 1654 ++++++++++++++++++++
 records/cowork/handoff/cowork_away_returns.md      |   56 +
 tools/audit/defense_share.json                     |    2 +-
 tools/audit/gen_status_batch_bound.py              |   32 +-
 tools/audit/per_session_reading.json               |   48 +-
 tools/audit/session_start_read_size.json           |   16 +-
 tools/audit/status_batch_bound.json                |   36 +-
 10 files changed, 2147 insertions(+), 57 deletions(-)
````

## 0(b) `git show --stat f2d0ae14ba2037ba4111c12c52d314b463d77741`

````text
commit f2d0ae14ba2037ba4111c12c52d314b463d77741
Author: Vincent Wong <65764495+slimvince@users.noreply.github.com>
Date:   Sun Nov 1 21:09:32 2026 +0100

    record: entries 467 to 469 and the step-4 first dispatch's re-execution dispatch
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 ...ction_pruning_rulings_reexecution_2026_11_01.md | 626 +++++++++++++++++++++
 ...k_handoff_entry_four_hundred_and_sixty_eight.md |  84 +++
 ...rk_handoff_entry_four_hundred_and_sixty_nine.md |  77 +++
 ...k_handoff_entry_four_hundred_and_sixty_seven.md |  86 +++
 4 files changed, 873 insertions(+)
````

## 0(c) `python tools/audit/changed_paths.py` — A1's enumeration, whole

````text
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_pruning_rulings_third_execution_2026_11_01.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_one.md
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
397 changed path record(s) [worktree]
````

## 0(c) `git ls-files --others --exclude-standard -- <path>`, the three landing paths

````text
== ls-files --others: records/cc/instructions/cc_instruction_pruning_rulings_third_execution_2026_11_01.md
records/cc/instructions/cc_instruction_pruning_rulings_third_execution_2026_11_01.md
exit:0
== ls-files --others: records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy.md
exit:0
== ls-files --others: records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_one.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_one.md
exit:0
````

## 0(c) `git diff --stat c483c6968f… -- <path>`, the fourteen named paths

````text
== diff --stat c483c696 -- CLAUDE.md
exit:0
== diff --stat c483c696 -- CLAUDE_ARCHIVE.md
exit:0
== diff --stat c483c696 -- DECISIONS.md
exit:0
== diff --stat c483c696 -- DECISIONS_ARCHIVE.md
exit:0
== diff --stat c483c696 -- tools/audit/decisions/gen_decisions_register.py
exit:0
== diff --stat c483c696 -- tools/audit/decisions/gen_phase1w_legacy_verification.py
exit:0
== diff --stat c483c696 -- tools/audit/decisions/backbone_decisions.json
exit:0
== diff --stat c483c696 -- tools/audit/decisions/cluster_dispositions.json
exit:0
== diff --stat c483c696 -- STATUS.md
exit:0
== diff --stat c483c696 -- STATUS_ARCHIVE.md
exit:0
== diff --stat c483c696 -- tools/audit/gen_status_batch_bound.py
exit:0
== diff --stat c483c696 -- tools/audit/status_batch_bound.json
exit:0
== diff --stat c483c696 -- cowork_audit_protocol.md
exit:0
== diff --stat c483c696 -- BUILD_AND_TEST.md
exit:0
````

## 0(d) `git hash-object -w --no-filters`, the three landing files

````text
== records/cc/instructions/cc_instruction_pruning_rulings_third_execution_2026_11_01.md
6d59532fff7f64280e4daf3bc8cc588fd68d2acc
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy.md
6aa05266b0dbed8f5f8dde2d316ec60175d0d026
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_one.md
a666d06e1bd8ce9ed197823ef02eee176de1fff6
exit:0
````

## 0(d) size, last 70 bytes and zero-byte count of each blob

````text
== 6d59532f (dispatch)
41161
0000000   o   n   s       w   a   s       f   o   u   n   d   ;       t
0000020   h   e       f   o   u   r       c   o   r   r   e   c   t   i
0000040   o   n   s       a   r   e       o   f       w   o   r   d   i
0000060   n   g       a   n   d       a   t   t   r   i   b   u   t   i
0000100   o   n   .   *   *  \n
0000106
zero bytes:
0
== 6aa05266 (entry 470)
7999
0000000   o   n       e   n   t   r   y       4   6   9   .       T   h
0000020   e       u   s   e   r   '   s       w   o   r   d   s   :    
0000040   t   h   e       o   p   e   n   i   n   g       i   n   s   t
0000060   r   u   c   t   i   o   n   ;  \n   "   c   o   n   t   i   n
0000100   u   e   "   .   *  \n
0000106
zero bytes:
0
== a666d06e (entry 471)
6241
0000000   .       T   h   e       u   s   e   r   '   s       w   o   r
0000020   d   s   :       t   h   e       o   p   e   n   i   n   g    
0000040   i   n   s   t   r   u   c   t   i   o   n   ;  \n   "   c   o
0000060   n   t   i   n   u   e   "   ;       "   c   o   n   t   i   n
0000100   u   e   "   .   *  \n
0000106
zero bytes:
0
````

## 0(e) `python tools/audit/gen_evidence_pin_membership.py --check`

````text
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
````

## 0(f) `python tools/audit/gen_guard_state.py --check` — the opening capture, whole

````text
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
````

## 0(f) `python tools/audit/gen_guard_classification.py --check`

````text
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_per_session_reading.py', 'tools/audit/gen_withheld_family_reading.py']
````

## 0(g) `gen_session_start_read_size.py --check`

````text
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
    STATUS.md                                                                 11863
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 248292
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 248292 [ruled membership]  (-118829, -32.37%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 248292 [ruled membership]  (-48540, -16.35%)  <- CROSSES A REGIME BOUNDARY
````

## 0(g) `gen_defense_share.py --check`

````text
the defense-share measurement re-derives
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   41071  ( 8.45%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (105876): 12.24%
    of the whole session-start read (248292): 5.22%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
````

## 0(g) `decisions/gen_decisions_register.py --check`

````text
the register matches the data (20 files: the index + 19 group files)
````

## 0(g) `decisions/gen_cluster_dispositions.py --verify` — the BEFORE of Decision 2, whole

````text
backbone decisions: 477
cross-references resolving: ALL
verbatim quotes found at their cited home: 477/477
cited line numbers correct: 465/471   (6 cited to a file with no line number, by design)
  LINE DRIFT D-196: cited CLAUDE.md:1979, actually starts at line 1991
  LINE DRIFT D-253: cited CLAUDE.md:1918-1936, actually starts at line 1930
  LINE DRIFT D-254: cited CLAUDE.md:1961-1968, actually starts at line 1973
  LINE DRIFT D-268: cited cowork_confidence_contract.md:36-48, actually starts at line 54
  LINE DRIFT D-269: cited cowork_confidence_contract.md:83-85, actually starts at line 101
  LINE DRIFT D-601: cited cowork_confidence_contract.md:89-101, actually starts at line 107
````

## 0(g) `decisions/reaim_home_anchors.py --check` — the BEFORE of Decision 2, whole

````text
  D-196: CLAUDE.md:1979 -> CLAUDE.md:1991   (drift +12)
  D-253: CLAUDE.md:1918-1936 -> CLAUDE.md:1930-1948   (drift +12)
  D-254: CLAUDE.md:1961-1968 -> CLAUDE.md:1973-1980   (drift +12)
  D-268: cowork_confidence_contract.md:36-48 -> cowork_confidence_contract.md:54-66   (drift +18)
  D-269: cowork_confidence_contract.md:83-85 -> cowork_confidence_contract.md:101-103   (drift +18)
  D-601: cowork_confidence_contract.md:89-101 -> cowork_confidence_contract.md:107-119   (drift +18)
anchors drifted: 6
````

## 0(g) `gen_l0_l1_outgoing_population.py --check`

````text
l0_l1_outgoing_population.json re-derives
````

## 0(g) `gen_l3_outgoing_population.py --check`

````text
l3_outgoing_population.json re-derives
````

## 0(g) `decisions/gen_phase1w_legacy_verification.py --check`

````text
phase1w: A1 held; 57 entries derived; 35 anchors located; 5 recorded figures located
````

## 0(g) `gen_claude_md_finer_archive.py --check`

````text
FAIL: the finer archive record does not re-derive: tools\audit\claude_md_finer_archive.json
````

## 0(g) `gen_claude_md_prune_backlog.py --check`

````text
FAIL: the prune-at-amendment backlog record does not re-derive: tools\audit\claude_md_prune_backlog.json
````

## 0(g) the differing-values script (`differing_values.py`), BEFORE

````text
== gen_claude_md_finer_archive: 1 differing value(s) (artifact vs rebuild)
   reconciliation.every_span_the_ruling_REFUSED_is_still_present_at_site_exactly_once: artifact True | rebuild False
== gen_claude_md_prune_backlog: 1 differing value(s) (artifact vs rebuild)
   reconciliation.every_span_the_reading_flagged_is_still_present_at_site_exactly_once: artifact True | rebuild False
````

## 1(a) the capacity judgment file

````text
CAPACITY JUDGMENT BEFORE TASK 1 — written after the 0(g) BEFORE captures, before any edit.

What Tasks 1 and 2 do. Task 1 replaces two bracketed former wordings in CLAUDE.md's decision-surface
block with dated pointers and appends both, verbatim, to CLAUDE_ARCHIVE.md; proved by a scratch
reconciliation with two planted faults; checked at the edited tree (the split pair, the two
historical archive checks and their differing values, the population confinement check with its
added class (c), a full read-only guard capture); one commit. Task 2 makes the eight generator edits
of the cited text, regenerates DECISIONS.md, re-aims the legacy-mark check's two generator citations
from that tool's own STOP messages (2(c')), appends the four classes and the three old sentences
verbatim to DECISIONS_ARCHIVE.md, re-points the legacy-mark check's recorded figure 79 to
DECISIONS_ARCHIVE.md (2(d')), and is proved the same way with two planted faults; one commit.

What the BEFORE captures of 0(g) took. Read size and defense share green (the Task 1
precondition); the register generator "matches the data (20 files)" (the Task 2 precondition); the
cluster dispositions verify and the home-anchor report each list the same six drifted anchors; both
population checks and the legacy-mark check green; the two historical archive checks FAIL, each with
exactly the one differing value the premise ledger names (artifact true, rebuild false).

What the ordered reads took, by my own account. The largest were the two cited texts (the second
dispatch whole and the first dispatch's text at lines 1 to 1022), DECISIONS.md whole, the
dispatch-protocol section of cowork_audit_protocol.md (lines 180 to 1606), the generator whole,
BUILD_AND_TEST.md whole and the second report whole. The protocol section, DECISIONS.md and the two
cited texts together took the most. The eight-line check of Ruling 2 replaced the six-span read of
CLAUDE.md.

Whether a summary of my context has fallen. No. No summary of this session's context has fallen at
the time of writing.

What the batch still owes after Task 2. The close (STATUS.md entries and the prefix move, the
forward-bound re-aim and --apply, the four archive checks, the regenerations under the population
confinement check, the two-file report and its appendix, the away-returns section, the close commit)
and the end state (a full guard run in write mode, the classification check, the end-state portion,
its commit).

Judgment. The ordered reads have taken a large share of this session's context. The edits are small
and located; the proofs are scratch scripts whose printouts stay in scratch files. I judge I can
finish both tasks whole and still close and reach the end state, keeping every printout in scratch
and quoting only what the report needs. If a summary of context falls, the first-unit rule governs
the task in hand and the report says so.
````

## 1(b) the record check (`t1b_record_check.py`)

````text
AS READ: '- **Carried for the next dispatch (not applied here):** amend `CLAUDE.md` Conventions, *How a decision surface\n  is written*, step 4, replacing the OPEN QUESTION clause with this ruling, former wording preserved in place\n  (#12).'
NORMALIZED: 'Carried for the next dispatch (not applied here): amend `CLAUDE.md` Conventions, *How a decision surface is written*, step 4, replacing the OPEN QUESTION clause with this ruling, former wording preserved in place (#12).'
1(b) RECORD CHECK PASS
````

## 1(f) the Task 1 reconciliation (`t1f_reconcile.py`) on the real files

````text
assertion 1 PASS
assertion 2 PASS
P1: in new archive 1, in old archive 0, in new CLAUDE.md 0
P2: in new archive 1, in old archive 0, in new CLAUDE.md 0
assertion 3 PASS
SIZES (characters):
  old CLAUDE.md 169617; new CLAUDE.md 169182; difference -435
  P1 455; P2 309; pointer 1 165; pointer 2 164
  old CLAUDE_ARCHIVE.md 12881; new CLAUDE_ARCHIVE.md 14773; appended block 1892
TASK 1 RECONCILIATION PASS
````

## 1(f) planted faults F1 and F2

````text
== F1
planted at offset 16: 'S' -> 'X'
           ^^^^^^^^^^^^^^^^
AssertionError: assertion 2: the rebuilt CLAUDE.md does not equal the new one
== F2
planted at offset 13705: 'h' -> 'X'
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: assertion 3: P1 counts wrong
````

## 1(g) `gen_governing_surface_split.py --check --pair CLAUDE.md`

````text
  CLAUDE.md / CLAUDE_ARCHIVE.md: moved 9 span(s), 6,540 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
````

## 1(g) `gen_claude_md_finer_archive.py --check`

````text
FAIL: the finer archive record does not re-derive: tools\audit\claude_md_finer_archive.json
````

## 1(g) `gen_claude_md_prune_backlog.py --check`

````text
FAIL: the prune-at-amendment backlog record does not re-derive: tools\audit\claude_md_prune_backlog.json
````

## 1(g) the differing-values script at the edited tree

````text
== gen_claude_md_finer_archive: 1 differing value(s) (artifact vs rebuild)
   reconciliation.every_span_the_ruling_REFUSED_is_still_present_at_site_exactly_once: artifact True | rebuild False
== gen_claude_md_prune_backlog: 1 differing value(s) (artifact vs rebuild)
   reconciliation.every_span_the_reading_flagged_is_still_present_at_site_exactly_once: artifact True | rebuild False
````

## 1(g) `gen_l0_l1_outgoing_population.py --check` (first)

````text
STALE vs the derivation: l0_l1_outgoing_population.json does not re-derive
````

## 1(g) `gen_l3_outgoing_population.py --check` (first)

````text
STALE vs the derivation: l3_outgoing_population.json does not re-derive
````

## 1(g) `git diff bf3664bc… 913e4d15…` — the L0/L1 population diff, whole

````text
diff --git a/bf3664bc8bf5d7d2ceeeeb352c58df77217f7a6b b/913e4d15c1989692078676202ffc7fccbfa7dc39
index bf3664bc8b..913e4d15c1 100644
--- a/bf3664bc8bf5d7d2ceeeeb352c58df77217f7a6b
+++ b/913e4d15c1989692078676202ffc7fccbfa7dc39
@@ -2753,13 +2753,13 @@
       "line": "declaration, where that clause is stated once and is not repeated here (#6)."
      },
      {
-      "line_number": 1933,
+      "line_number": 1929,
       "term": "tie",
       "tier": "recorded",
       "line": "through the file tools (Read / Grep / Glob), never through shell text utilities — no `cat`, `wc`,"
      },
      {
-      "line_number": 1954,
+      "line_number": 1950,
       "term": "repeat",
       "tier": "recorded",
       "line": "2026-08-07/08, self-reported at the user's challenge after repeated use for row statuses,"
````

## 1(g) `git diff 7b4f925f… 38c7fd78…` — the L3 population diff, whole

````text
diff --git a/7b4f925f671036e259d75e28a84dc6427c99be48 b/38c7fd78a541c0f8de579a21a3d232873a41f959
index 7b4f925f67..38c7fd78a5 100644
--- a/7b4f925f671036e259d75e28a84dc6427c99be48
+++ b/38c7fd78a541c0f8de579a21a3d232873a41f959
@@ -192,7 +192,7 @@
     "resolves_at_the_path_as_written": true,
     "in_the_specification_document_set": false,
     "inventory_class": "governing-documents",
-    "bytes": 170942
+    "bytes": 170510
    },
    {
     "name_as_written": "cowork_layer5_engagement_design.md",
@@ -264,7 +264,7 @@
     "resolves_at_the_path_as_written": true,
     "in_the_specification_document_set": false,
     "inventory_class": "governing-documents",
-    "bytes": 170942
+    "bytes": 170510
    },
    {
     "name_as_written": "records/cowork/rulings/cowork_rulings_2026_08_09_second_stop.md",
@@ -300,7 +300,7 @@
     "resolves_at_the_path_as_written": true,
     "in_the_specification_document_set": false,
     "inventory_class": "governing-documents",
-    "bytes": 170942,
+    "bytes": 170510,
     "named_in_sections": [
      "#### Layer 5 — the function/cadence layer",
      "#### Layer 6 — the grouping layer"
@@ -33034,7 +33034,7 @@
   "item_2_listed_not_compared_whole": [
    {
     "name": "CLAUDE.md",
-    "bytes": 170942,
+    "bytes": 170510,
     "inventory_class": "governing-documents",
     "in_the_residue": true,
     "the_statement": "named inside the six item-1 spans; LISTED and not compared whole under the named-documents derivation; the lines that name it are tabulated inside item 1"
@@ -36407,7 +36407,7 @@
   "item_2": {
    "distinct_names": 12,
    "distinct_names_that_resolve": 12,
-   "summed_bytes_of_the_distinct_names_that_resolve": 844831,
+   "summed_bytes_of_the_distinct_names_that_resolve": 844399,
    "distinct_names_that_are_specification_set_members": 4
   },
   "item_3": {
````

## 1(g) `python tools/audit/gen_guard_state.py --check` at the Task 1 edited tree, whole

````text
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
  [FAIL] tools/audit/gen_session_start_read_size.py --check
  [FAIL] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_per_session_reading.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [FAIL] tools/audit/gen_derivation_boot_pack.py --check
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
83 guard(s) run, 17 failing, 4 not run, 20 historical record(s)
````

## 1(g) `python tools/audit/gen_derivation_boot_pack.py --check` at the Task 1 edited tree — the unpredicted red

````text
FROZEN SOURCES: 17 of 30 frozen pack file(s) would render at a different length from the sources as they stand today. NOT COMPARED; sets no exit code.
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
  - scoring-model/02_the_guiding_principles_and_the_conventions.md: the directory holds 60536 characters; today's sources would render 68308
  - scoring-model/03_the_writing_standards.md: the directory holds 15002 characters; today's sources would render 15048
  - scoring-model/04_the_dispatch_protocol.md: the directory holds 99970 characters; today's sources would render 108389
  - scoring-model/05_the_ratified_design_intent.md: the directory holds 295073 characters; today's sources would render 295142
STALE: the derivation boot pack does not re-derive
  - derivation_boot_pack.json does not re-derive
  - l3/02_the_guiding_principles_and_the_conventions.md does not re-render
````

## Task 1 reversal: `gen_derivation_boot_pack.py --check` at the reversed tree

````text
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
````

## Task 1 reversal: `gen_l0_l1_outgoing_population.py --check` after restoration

````text
l0_l1_outgoing_population.json re-derives
````

## Task 1 reversal: `gen_l3_outgoing_population.py --check` after restoration

````text
l3_outgoing_population.json re-derives
````

## 2(a) the excerpt check (`t2a_excerpts.py`)

````text
PRECEDING_REGIME_START in home_granularity: 1
REMOVED_FILE_START in scope_of_application: 1
REMOVED_FILE_END after it: 1
(iii-a): 'THE PRECEDING REGIME, superseded and recorded here rather than deleted: from the phase-1n ruling of the same day until phase 1q the field was deliberately MIXED — D-430 was applied to 46 entries across 5 documents, where section granularity decided something, and every other entry carried a document-level home pending the next touch. The user ended that staging on 2026-08-03 by ruling ONE re-classification pass over the whole population (`OPEN_ITEMS.md` OI-291).'
(iii-b): '**THE FILE THIS POINTER FORMERLY NAMED IS REMOVED (user, 2026-08-09, Ruling 1 of `cowork_rulings_2026_08_09_return.md`; recorded here in the D-644 shape — state the current arrangement, record the removal as closed).** `phase1q_reclassification.json` held NEITHER the phase-1q record NOR the present classes: the applying run had been performed by more than one wave since the 2026-08-04 establishment froze it and its snapshot as byte-identical, rewriting it each time (measured at `tools/audit/decisions/phase1q_record_divergence.json`, from git objects by explicit hash). The current arrangement is TWO files with one job each — the phase-1q record at the established, hash-guarded snapshot, and the LIVE derived view at `home_classification.json`, which is where this pointer now aims and which carries `the_phase_1r_re_run`, `the_2026_08_08_apply` and `write_list` unchanged. Every committed state of the removed file remains reachable in git history at the commits the divergence artifact names, so nothing is lost (#12, the recomputable-collapse clause) and one concern has one home (#6). TRIED AND CLOSED: restoring the stale file from the snapshot (a second, unguarded copy of the record — the OI-305 divergence class reopened) and renaming it for what it held (an orphan generated artifact with no writer and no consumer — undeclared dormancy).'
2(a) EXCERPTS PASS
````

## 2(c) `decisions/gen_decisions_register.py` (write mode)

````text
wrote 20 files: DECISIONS.md (the index, 772 lines) + 19 group files under decisions/ (477 decisions)
````

## 2(c) `decisions/gen_decisions_register.py --check`

````text
the register matches the data (20 files: the index + 19 group files)
````

## 2(c') `decisions/gen_phase1w_legacy_verification.py --check`, run 1

````text
STOP: A1 (the marker is generated text): quote not at tools/audit/decisions/gen_decisions_register.py:514. It is now at line(s) [473] — re-aim the citation.
````

## 2(c') `decisions/gen_phase1w_legacy_verification.py --check`, run 2

````text
STOP: A1 (the marker is generated text): quote not at tools/audit/decisions/gen_decisions_register.py:516. It is now at line(s) [475] — re-aim the citation.
````

## 2(c') `decisions/gen_phase1w_legacy_verification.py --check`, run 3 (step 5)

````text
STOP: recorded figure 79: quote not found anywhere in DECISIONS.md
````

## 2(d') `decisions/gen_phase1w_legacy_verification.py --check` after the re-point

````text
phase1w: A1 held; 57 entries derived; 35 anchors located; 5 recorded figures located
````

## 2(e) the Task 2 reconciliation (`t2e_reconcile.py`) on the real files

````text
assertion 1 PASS
assertion 2 PASS
block (1): in new archive 1, in new index 0
block (2): in new archive 1, in new index 0
excerpt (iii-a): in new archive 1, in new index 0
excerpt (iii-b): in new archive 1, in new index 0
block (4): in new archive 1, in new index 0
line 88: in new archive 1, in new index 0
line 122: in new archive 1, in new index 0
line 229: in new archive 1, in new index 0
assertion 3 PASS
SIZES (characters):
  old DECISIONS.md 127727; new DECISIONS.md 117490; difference -10237
  block (1) 7012
  block (2) 657
  excerpt (iii-a) 466
  excerpt (iii-b) 1354
  block (4) 2291
  line 88 48
  line 122 101
  line 229 437
  S1 377
  S5 397
  POINTER_PRECEDING_REGIME 143
  POINTER_REMOVED_FILE 203
  S7 323
  x1 new 99
  x2 new 140
  x3 new 96
  old DECISIONS_ARCHIVE.md 1670; new DECISIONS_ARCHIVE.md 15987; appended block 14317
TASK 2 RECONCILIATION PASS
````

## 2(e) planted faults F3 and F4

````text
== F3
planted at offset 16: 'e' -> 'X'
AssertionError: assertion 2: the rebuilt index does not equal the new one
== F4
planted at offset 4594: 'n' -> 'X'
AssertionError: assertion 3: block (1) counts wrong
````

## 2(f) `gen_governing_surface_split.py --check --pair DECISIONS.md`

````text
  DECISIONS.md / DECISIONS_ARCHIVE.md: moved 0 span(s), 0 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
````

## 2(f) `decisions/gen_cluster_dispositions.py --verify` — the AFTER of Decision 2, whole

````text
backbone decisions: 477
cross-references resolving: ALL
verbatim quotes found at their cited home: 477/477
cited line numbers correct: 465/471   (6 cited to a file with no line number, by design)
  LINE DRIFT D-196: cited CLAUDE.md:1979, actually starts at line 1991
  LINE DRIFT D-253: cited CLAUDE.md:1918-1936, actually starts at line 1930
  LINE DRIFT D-254: cited CLAUDE.md:1961-1968, actually starts at line 1973
  LINE DRIFT D-268: cited cowork_confidence_contract.md:36-48, actually starts at line 54
  LINE DRIFT D-269: cited cowork_confidence_contract.md:83-85, actually starts at line 101
  LINE DRIFT D-601: cited cowork_confidence_contract.md:89-101, actually starts at line 107
````

## 2(f) `decisions/reaim_home_anchors.py --check` — the AFTER of Decision 2, whole

````text
  D-196: CLAUDE.md:1979 -> CLAUDE.md:1991   (drift +12)
  D-253: CLAUDE.md:1918-1936 -> CLAUDE.md:1930-1948   (drift +12)
  D-254: CLAUDE.md:1961-1968 -> CLAUDE.md:1973-1980   (drift +12)
  D-268: cowork_confidence_contract.md:36-48 -> cowork_confidence_contract.md:54-66   (drift +18)
  D-269: cowork_confidence_contract.md:83-85 -> cowork_confidence_contract.md:101-103   (drift +18)
  D-601: cowork_confidence_contract.md:89-101 -> cowork_confidence_contract.md:107-119   (drift +18)
anchors drifted: 6
````

## 2(f) `gen_l0_l1_outgoing_population.py --check` (first)

````text
STALE vs the derivation: l0_l1_outgoing_population.json does not re-derive
````

## 2(f) `gen_l3_outgoing_population.py --check` (first)

````text
STALE vs the derivation: l3_outgoing_population.json does not re-derive
````

## 2(f) `git diff bf3664bc… 3e654a59…` — the L0/L1 population diff, whole

````text
diff --git a/bf3664bc8bf5d7d2ceeeeb352c58df77217f7a6b b/3e654a591d85b6c3c61ef15c02ffbcb0e71af99a
index bf3664bc8b..3e654a591d 100644
--- a/bf3664bc8bf5d7d2ceeeeb352c58df77217f7a6b
+++ b/3e654a591d85b6c3c61ef15c02ffbcb0e71af99a
@@ -2775,43 +2775,43 @@
     "recorded_hit_count": 30,
     "admitting_hits": [
      {
-      "line_number": 313,
+      "line_number": 224,
       "term": "key signature",
       "tier": "admitting",
       "line": "| D-528 | The key signature and declared mode enter as a WEAK FITTED SOFT PRIOR with no conditional gate anywhere — the probability calculus delivers 'consult it only when unsure', and the hard declared-mode wall is formally retired | LIVE | — | `cowork_joint_estimator_architecture.md` §5a |"
      },
      {
-      "line_number": 405,
+      "line_number": 316,
       "term": "change-point",
       "tier": "admitting",
       "line": "| D-628 | The finest meaningful extension step is the change-point — within a slice the sounding set is constant, so a finer request loads no note and changes no answer | LIVE | — | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 405,
+      "line_number": 316,
       "term": "sounding set",
       "tier": "admitting",
       "line": "| D-628 | The finest meaningful extension step is the change-point — within a slice the sounding set is constant, so a finer request loads no note and changes no answer | LIVE | — | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 433,
+      "line_number": 344,
       "term": "key signature",
       "tier": "admitting",
       "line": "| D-056 | Notes always win - the notated key signature is a weak hint, not a bypass | LIVE | — | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 562,
+      "line_number": 473,
       "term": "fermata",
       "tier": "admitting",
       "line": "| D-482 | The two hand-synchronised copies of the fermata scan retire into one owned primitive, and that retirement changes no output | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
      },
      {
-      "line_number": 563,
+      "line_number": 474,
       "term": "fermata",
       "tier": "admitting",
       "line": "| D-483 | The picked boundaries are validated against the analysts' own phrase marks; a fermata-derived phrase list is inadmissible as ground truth because the primitive reads fermatas | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §7 |"
      },
      {
-      "line_number": 764,
+      "line_number": 675,
       "term": "MusicXML",
       "tier": "admitting",
       "line": "| D-199 | The MusicXML declared-mode import fix is intentional and must not be reverted | LIVE | — | `CLAUDE.md` |"
@@ -2819,181 +2819,181 @@
     ],
     "recorded_hits": [
      {
-      "line_number": 186,
+      "line_number": 116,
       "term": "slice",
       "tier": "recorded",
       "line": "| **slice** | The smallest stretch of music analysed: a span during which exactly the same notes are sounding. It begins when any note starts or stops and ends at the next such moment. |"
      },
      {
-      "line_number": 187,
+      "line_number": 117,
       "term": "release",
       "tier": "recorded",
       "line": "| **onset / release** | The moment a note is struck and the moment it stops sounding. |"
      },
      {
-      "line_number": 290,
+      "line_number": 201,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-008 | The true probabilities are deferred to a later step | DEFERRED | — | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 306,
+      "line_number": 217,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-451 | A desk simulation's table values are provisional, enter no fit, and a verdict that would flip inside a provisional value's plausible range is reported as a near-tie, never as a win | LIVE | 2026-08-04 · user | `CLAUDE.md` |"
      },
      {
-      "line_number": 318,
+      "line_number": 229,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-565 | Exact score ties in the decode are real and are broken by a declared TOTAL ORDER on paths, implemented identically in every decoder — no epsilon, no platform dependence | LIVE | 2026-08-04 · user | `cowork_joint_estimator_factorization.md` §5 |"
      },
      {
-      "line_number": 334,
+      "line_number": 245,
       "term": "slice",
       "tier": "recorded",
       "line": "| D-425 | The uncertainty surface's contract IS the full posterior; the local slice is the first delivered step, and the completion is a named step, never an indefinite upgrade | LIVE | — | `cowork_notation_adoption_increment.md` §4 |"
      },
      {
-      "line_number": 342,
+      "line_number": 253,
       "term": "slice",
       "tier": "recorded",
       "line": "| D-023 | The atomic analysis unit is the constant-sonority slice, never the metric beat | LIVE | — | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 358,
+      "line_number": 269,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-191 | The two-tier regression class policy - functional regression stops, rotation churn is tracked | LIVE | — | `CLAUDE.md` |"
      },
      {
-      "line_number": 373,
+      "line_number": 284,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-282 | Meta-finding: the oracle/tier metric, never a bare proxy - superseded by the robust-unit stop and the two-tier policy | SUPERSEDED BY D-115 and D-191 | — | `cowork_architecture_reassessment.md` §4 ⚠gap |"
      },
      {
-      "line_number": 393,
+      "line_number": 304,
       "term": "slice",
       "tier": "recorded",
       "line": "| D-539 | The standing method for every error slice: decompose it into structural, fitted and ceiling BEFORE building anything — derive, never assert | LIVE | — | `cowork_engage_arc_plan.md` |"
      },
      {
-      "line_number": 405,
+      "line_number": 316,
       "term": "slice",
       "tier": "recorded",
       "line": "| D-628 | The finest meaningful extension step is the change-point — within a slice the sounding set is constant, so a finer request loads no note and changes no answer | LIVE | — | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 416,
+      "line_number": 327,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-040 | The tie-unresolved atoms are republished additively for the joint estimator | LIVE | — | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 417,
+      "line_number": 328,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-569 | Collecting, filtering and weighting are THREE separate responsibilities; the collection layer collects and annotates, and does nothing else | LIVE | 2026-08-04 · user | `cowork_layer1_tone_collection_design.md` the opening block (above the first section heading) ⚠gap |"
      },
      {
-      "line_number": 422,
+      "line_number": 333,
       "term": "slice",
       "tier": "recorded",
       "line": "## E. Layer 2 — the slicer — [full entries](decisions/group_E.md)"
      },
      {
-      "line_number": 454,
+      "line_number": 365,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-588 | Preset coverage beyond the analysed corpora is three tiers with NO bare guessing — measured, editorially declared with a stated theory rationale, or self-correcting by detection | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 481,
+      "line_number": 392,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-321 | Winner selection compares candidate scores exactly, with no epsilon anywhere in the ranking | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` “Floating-point tie policy” |"
      },
      {
-      "line_number": 482,
+      "line_number": 393,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-322 | Any change to optimization flags or to the order of the scoring arithmetic requires a full corpus A/B on both presets | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` “Floating-point tie policy” |"
      },
      {
-      "line_number": 491,
+      "line_number": 402,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-333 | The membership tie-break's direction is an idiom-calibrated number, never a branch on style — the three-tier structure is fixed | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |"
      },
      {
-      "line_number": 493,
+      "line_number": 404,
       "term": "slice",
       "tier": "recorded",
       "line": "| D-380 | The carry's meaningful axis is DISTINCT ROOTS, and every above-threshold root is carried at graded confidence — a carry of winner-plus-one discards the third root on about a quarter of slices | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§2.2 The exclusion tail is load-bearing and must be carried” |"
      },
      {
-      "line_number": 530,
+      "line_number": 441,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-383 | Bass, spelling and tonality-consistency DECIDE; a licensed progression is only a tie-break among already-consistent readings and may never override a committed root | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§3.2 The evidence channels, ranked by the research” |"
      },
      {
-      "line_number": 559,
+      "line_number": 470,
       "term": "eligible",
       "tier": "recorded",
       "line": "| D-479 | The boundary cues run per eligible voice and aggregate to the texture, and BOTH the per-voice and the texture boundaries are published | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
      },
      {
-      "line_number": 566,
+      "line_number": 477,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-490 | FALSIFIED: no threshold can make the fine-grain function override net-positive — the harm rate is flat against both quantities the threshold is built from | LIVE | 2026-08-04 · user | `docs/scoring_model.md` |"
      },
      {
-      "line_number": 602,
+      "line_number": 513,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-585 | The bass-scale-degree / Rule-of-the-Octave prior is admitted as a SOFT prior and tie-breaker only, never a gate | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 630,
+      "line_number": 541,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-499 | RATIFIED AMENDMENT A-10: four documentation riders — a consolidated ownership page for the notation-derived views, the membership tie-breaker recorded as idiom-calibrated, and the producer-agnostic seam pinned as a design property | LIVE | 2026-08-04 · user | `cowork_architecture_review_2026_07.md` §9 ⚠gap |"
      },
      {
-      "line_number": 634,
+      "line_number": 545,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-660 | A research-tied name is not renamed but is governed by a two-tier rule, and the terminology cleanup runs in a fixed order with no tree-wide rename | LIVE | — | `CLAUDE.md` |"
      },
      {
-      "line_number": 634,
+      "line_number": 545,
       "term": "tied",
       "tier": "recorded",
       "line": "| D-660 | A research-tied name is not renamed but is governed by a two-tier rule, and the terminology cleanup runs in a fixed order with no tree-wide rename | LIVE | — | `CLAUDE.md` |"
      },
      {
-      "line_number": 677,
+      "line_number": 588,
       "term": "slice",
       "tier": "recorded",
       "line": "| D-545 | The uniform mechanical extractor for idiom discovery is the external library, stopping at the note-and-slice front — OUR OWN key/chord/function inference must NEVER touch the extraction | NOT STATED | — | `ARCHITECTURE.md` |"
      },
      {
-      "line_number": 709,
+      "line_number": 620,
       "term": "slice",
       "tier": "recorded",
       "line": "| D-513 | A corpus registry's content summary is enumeration provenance, not evidence that an annotation layer is present — per-slice presence must be measured | LIVE | — | `cowork_score_census.md` §3 |"
      },
      {
-      "line_number": 783,
+      "line_number": 694,
       "term": "release",
       "tier": "recorded",
       "line": "| D-434 | The writing side runs the standing self-check before a dispatch is released, and records its output | LIVE | — | `cowork_audit_protocol.md` |"
      },
      {
-      "line_number": 806,
+      "line_number": 717,
       "term": "tie",
       "tier": "recorded",
       "line": "| D-611 | The tidy guardrails, in three tiers — and the dormant path and its staged scaffolding are DEFERRED-ENGAGEMENT, not dead code: removing them is a STOP | LIVE | 2026-08-04 · user | `cowork_l1l4_review_charter.md` |"
````

## 2(f) `git diff 7b4f925f… 156d34d8…` — the L3 population diff, whole

````text
diff --git a/7b4f925f671036e259d75e28a84dc6427c99be48 b/156d34d88ff51f58d7815b37e6a2f4427e8b818a
index 7b4f925f67..156d34d88f 100644
--- a/7b4f925f671036e259d75e28a84dc6427c99be48
+++ b/156d34d88ff51f58d7815b37e6a2f4427e8b818a
@@ -498,7 +498,7 @@
    "paths_in_more_than_one_searched_class": [],
    "hits_per_term": {
     "cadence": 979,
-    "phrase": 581,
+    "phrase": 579,
     "inversion": 518,
     "grouping": 242,
     "chord symbol": 208,
@@ -19281,420 +19281,408 @@
       "governing-documents"
      ],
      "in_the_specification_document_set": false,
-     "hit_lines_distinct": 56,
-     "hits": 69,
+     "hit_lines_distinct": 54,
+     "hits": 67,
      "the_statement": "hit, outside the specification document set, not dispositioned by this comparison; reachable by the mining map",
      "hit_records": [
       {
-       "line_number": 28,
-       "term": "phrase",
-       "tier": "admitting",
-       "line": "> phase-1g entries (D-317…D-342) — D-319…D-341 directly; D-317/D-318 with rephrased plain"
-      },
-      {
-       "line_number": 34,
-       "term": "phrase",
-       "tier": "admitting",
-       "line": "> rephrased at the user's direction (the pedaled note can be in any voice, the D-207"
-      },
-      {
-       "line_number": 160,
+       "line_number": 90,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "`chordsymbolformatter.cpp`, which the record arm runs. A swept population with two demonstrated"
       },
       {
-       "line_number": 256,
+       "line_number": 173,
        "term": "phrase",
        "tier": "admitting",
        "line": "> **How a whole-document delegation is read.** A delegation that names a DOCUMENT and no section reaches EVERY section of it; a delegation that names SECTIONS reaches those sections and their subsections and no others; and the rule-stating half is judged PER SECTION in both cases. **THIS IS NOW PART OF THE RULE, NOT AN INTERPRETATION OF IT (user, 2026-08-03, phase 1r).** At phase 1q it was this pass's reading of D-430's \"delegates a stated concern to that section BY NAME\", taken on the record's own precedent rather than a preference — `OPEN_ITEMS.md` OI-290 states in terms that \"`ARCHITECTURE.md:1331` delegates 'this layer' and admits all sixteen of that document's entries\" — and the strict alternative was recorded as available to the user. The user then WROTE the reading into `CLAUDE.md` rule (h) itself as the GRANULARITY clause, so D-430's verbatim now carries it and the strict alternative is CLOSED. Its defense, stated with it: the strict reading would evict every document delegated as a whole, signed layer specifications among them, on the accident of how a pointer happens to be phrased, making the rule retroactively destructive rather than refining. THE STRICT ALTERNATIVE, PRESERVED (#12): read literally, a whole-document delegation names no section, so no section of it would be admitted and the seven whole-document homes would lose every entry between them."
       },
       {
-       "line_number": 311,
+       "line_number": 222,
        "term": "chord symbol",
        "tier": "admitting",
        "line": "| D-526 | The joint state's chord axis is SCALE-DEGREE-VALUED — a Roman numeral relative to the state's own tonic and mode — and the chord symbol is a DERIVED fact published once | LIVE | — | `cowork_joint_estimator_architecture.md` §5a |"
       },
       {
-       "line_number": 426,
+       "line_number": 337,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-605 | The local-key hypothesis derives from key-agnostic signals ONLY and never from the key-area grouping, which is a post-grouping of the resolved key — a hard design rule, not a preference | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 437,
+       "line_number": 348,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-290 | The key-agnostic local cadence approach is FALSIFIED at its precision ceiling | LIVE ⚠LEGACY | 2026-08-02 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 449,
+       "line_number": 360,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-494 | RATIFIED AMENDMENT A-4: the function layer must gain key-confirmation channels that do not require a cadence, plus an enharmonic-identity rule for key spans | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 470,
+       "line_number": 381,
        "term": "chord symbol",
        "tier": "admitting",
        "line": "| D-280 | Gates read structured fields only - never a chord symbol string and never a Roman numeral | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 475,
+       "line_number": 386,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-302 | No further local scoring fix for inversions may be attempted — the remaining divergence is not an analyzer defect | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 486,
+       "line_number": 397,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-327 | The root-continuity guard reads the reconstructed inversion credit, superseding the designed sounding-third test | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 488,
+       "line_number": 399,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-329 | Completeness of the candidate list is the priority — a chord never listed can never be chosen | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §4 |"
       },
       {
-       "line_number": 489,
+       "line_number": 400,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-330 | Never a pooled recompute — the chord is never re-derived from several stretches' notes thrown together | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §8 |"
       },
       {
-       "line_number": 490,
+       "line_number": 401,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-331 | Every chord decision carries its ranked alternatives and its confidence — committed, inherited, and abstained alike, never pruned | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |"
       },
       {
-       "line_number": 491,
+       "line_number": 402,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-333 | The membership tie-break's direction is an idiom-calibrated number, never a branch on style — the three-tier structure is fixed | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |"
       },
       {
-       "line_number": 492,
+       "line_number": 403,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-334 | The bare-fifth chord type stays in the catalogue structurally; whether it wins is an idiom-calibrated number | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |"
       },
       {
-       "line_number": 503,
+       "line_number": 414,
        "term": "chord symbol",
        "tier": "admitting",
        "line": "| D-501 | A tool may read a written chord symbol ONLY as a comparison or ground-truth label — never as input that influences what the analyzer computes | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 507,
+       "line_number": 418,
        "term": "bass note",
        "tier": "admitting",
        "line": "| D-536 | The bass note and the chord are chosen TOGETHER — the winner is the (bass, root, template) triple — replacing the sequential commit-the-bass-then-score pipeline | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 508,
+       "line_number": 419,
        "term": "slash chord",
        "tier": "admitting",
        "line": "| D-537 | The completeness bonus fires ONLY for a root-position reading whose three triad tones are all present — the guard that stops it from demoting genuine slash chords | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 514,
+       "line_number": 425,
        "term": "cadence",
        "tier": "admitting",
        "line": "## H. Layer 5 and Layer 6 — function, cadence, grouping — [full entries](decisions/group_H.md)"
       },
       {
-       "line_number": 514,
+       "line_number": 425,
        "term": "grouping",
        "tier": "admitting",
        "line": "## H. Layer 5 and Layer 6 — function, cadence, grouping — [full entries](decisions/group_H.md)"
       },
       {
-       "line_number": 518,
+       "line_number": 429,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-081 | The cadence detector is key-agnostic | LIVE | — | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 519,
+       "line_number": 430,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-082 | The grouping layer is additive, read-only, with no feedback | LIVE | — | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 519,
+       "line_number": 430,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-082 | The grouping layer is additive, read-only, with no feedback | LIVE | — | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 525,
+       "line_number": 436,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-336 | Cadence detection is key-agnostic and votes for the key rather than reading one | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §9 |"
       },
       {
-       "line_number": 526,
+       "line_number": 437,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-337 | A lean toward another degree is a tonicization by default; a key change needs a confirming cadence AND persistence, expressed as a change-cost | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §9 |"
       },
       {
-       "line_number": 529,
+       "line_number": 440,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-382 | The function layer selects by JOINT CONSISTENCY across tonality, root, inversion and bass — not by maximizing any one score — and every ambiguity kind reasons over the full carried distribution | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§3.1 The objective: select by JOINT CONSISTENCY, not by strengthening one score” |"
       },
       {
-       "line_number": 532,
+       "line_number": 443,
        "term": "contradiction",
        "tier": "admitting",
        "line": "| D-387 | A contradiction between the function context and a committed chord is surfaced on the ONE open mark, enriched with a reason — not on a second parallel flag, and not by overloading the plain undecided mark | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§7.2 The vehicle” |"
       },
       {
-       "line_number": 542,
+       "line_number": 453,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-397 | The homeless analysis objects are ASSIGNED to named owners on the voice-leading dimension — the stock patterns, the melodic phrase, chord voicing, and part-writing advice — as claims, discharged only at each owner's own ratified design | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 544,
+       "line_number": 455,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-400 | A PER-VOICE span kind is admitted to the span typology — melodic phrases overlap across voices by construction and tile only within one voice | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 546,
+       "line_number": 457,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-454 | The grouping layer detects nothing — it assembles what earlier layers decided, and pressure to add detection means the work belongs elsewhere | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §6 |"
       },
       {
-       "line_number": 546,
+       "line_number": 457,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-454 | The grouping layer detects nothing — it assembles what earlier layers decided, and pressure to add detection means the work belongs elsewhere | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §6 |"
       },
       {
-       "line_number": 547,
+       "line_number": 458,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-455 | A cadence away from a grouping boundary is surfaced as internal, never snapped to the nearest boundary and never discarded | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 547,
+       "line_number": 458,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-455 | A cadence away from a grouping boundary is surfaced as internal, never snapped to the nearest boundary and never discarded | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 548,
+       "line_number": 459,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-456 | Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 548,
+       "line_number": 459,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-456 | Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 548,
+       "line_number": 459,
        "term": "period",
        "tier": "admitting",
        "line": "| D-456 | Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 549,
+       "line_number": 460,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-457 | A group truncated by the selection edge is marked as truncated, and a group that runs off the edge unclosed carries an extension cue the grouping layer only surfaces | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.1 |"
       },
       {
-       "line_number": 549,
+       "line_number": 460,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-457 | A group truncated by the selection edge is marked as truncated, and a group that runs off the edge unclosed carries an extension cue the grouping layer only surfaces | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.1 |"
       },
       {
-       "line_number": 550,
+       "line_number": 461,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-458 | The codetta refinement is read as the as-built tiling: keep the strong cut, drop the weak one, and record the codetta end as an annexe | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.1 |"
       },
       {
-       "line_number": 551,
+       "line_number": 462,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-459 | The key-area confidence is a declared margin-class boundary confidence, and its input is the declared key confidence — never the grading diagnostics' sigmoid | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.2 |"
       },
       {
-       "line_number": 552,
+       "line_number": 463,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-460 | A group counts as fully resolved exactly when no unit in it carries an unresolved mark — no confidence threshold enters the test | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.4 |"
       },
       {
-       "line_number": 553,
+       "line_number": 464,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-461 | The grouping layer is an explainability layer, not an accuracy requirement, and is deliberately kept thin | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §7 |"
       },
       {
-       "line_number": 553,
+       "line_number": 464,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-461 | The grouping layer is an explainability layer, not an accuracy requirement, and is deliberately kept thin | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §7 |"
       },
       {
-       "line_number": 554,
+       "line_number": 465,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-462 | Cadence validation is scoped to LOCATION; cadence TYPE is only partially attributable and is never a clean gate | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §10 |"
       },
       {
-       "line_number": 554,
+       "line_number": 465,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-462 | Cadence validation is scoped to LOCATION; cadence TYPE is only partially attributable and is never a clean gate | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §10 |"
       },
       {
-       "line_number": 556,
+       "line_number": 467,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-476 | The phrase-boundary primitive is owned by the notation-derived view layer — not by the note model, and not by the function layer that consumes it | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 557,
+       "line_number": 468,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-477 | Phrase boundaries are read from the written surface alone — never from a resolved key, chord or cadence — and the boundaries this misses are accepted, not recovered here | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §2 |"
       },
       {
-       "line_number": 557,
+       "line_number": 468,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-477 | Phrase boundaries are read from the written surface alone — never from a resolved key, chord or cadence — and the boundaries this misses are accepted, not recovered here | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §2 |"
       },
       {
-       "line_number": 558,
+       "line_number": 469,
        "term": "phrase boundary",
        "tier": "admitting",
        "line": "| D-478 | A phrase boundary is a peak in a continuous boundary-strength profile, not the OR of a few binary signals | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 558,
+       "line_number": 469,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-478 | A phrase boundary is a peak in a continuous boundary-strength profile, not the OR of a few binary signals | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 559,
+       "line_number": 470,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-479 | The boundary cues run per eligible voice and aggregate to the texture, and BOTH the per-voice and the texture boundaries are published | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 560,
+       "line_number": 471,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-480 | The phrase-boundary primitive is NOT an accuracy requirement — a competitive reference engine does no phrase segmentation at all — so it is built right but kept proportionate | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §8 |"
       },
       {
-       "line_number": 561,
+       "line_number": 472,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-481 | The notated markers are emitted as boundaries unconditionally; only the surface-cue strength is peak-picked | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §4.4 |"
       },
       {
-       "line_number": 562,
+       "line_number": 473,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-482 | The two hand-synchronised copies of the fermata scan retire into one owned primitive, and that retirement changes no output | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 563,
+       "line_number": 474,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-483 | The picked boundaries are validated against the analysts' own phrase marks; a fermata-derived phrase list is inadmissible as ground truth because the primitive reads fermatas | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §7 |"
       },
       {
-       "line_number": 564,
+       "line_number": 475,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-484 | The phrase-boundary primitive is a derived view: it inherits the loaded span, requests no extension of its own, and publishes a per-profile max-normalised boundary confidence | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §2 |"
       },
       {
-       "line_number": 565,
+       "line_number": 476,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-485 | Each picked boundary should carry which cue fired and at what scope; the picked set is scope-blind today and the refinement waits for the inference phase | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §4.4 |"
       },
       {
-       "line_number": 568,
+       "line_number": 479,
        "term": "contradiction",
        "tier": "admitting",
        "line": "| D-492 | The recommended redesign is to demote the override to an annotation — carrying the earlier reading unchanged and surfacing the contradiction — floored by simply disabling it | LIVE | 2026-08-04 · user | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 570,
+       "line_number": 481,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-495 | RATIFIED AMENDMENT A-5: when the phrase-boundary profile is flat, cadence admission relaxes with vote-weight scaling instead of starving | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 570,
+       "line_number": 481,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-495 | RATIFIED AMENDMENT A-5: when the phrase-boundary profile is flat, cadence admission relaxes with vote-weight scaling instead of starving | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 601,
+       "line_number": 512,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-584 | The perfect/imperfect cadence call is made on the BASS-DERIVED inversion; the soprano arrival degree is demoted to a soft optional nudge and the tool never attempts melody identification | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 601,
+       "line_number": 512,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-584 | The perfect/imperfect cadence call is made on the BASS-DERIVED inversion; the soprano arrival degree is demoted to a soft optional nudge and the tool never attempts melody identification | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 603,
+       "line_number": 514,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-607 | Polyphonic phrase-boundary detection has NO validated deterministic rule set in the literature — the extension is engineering on monophonic cues, validated against our own corpus, and is not settled science | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 649,
+       "line_number": 560,
        "term": "chord-symbol",
        "tier": "admitting",
        "line": "| D-315 | A one-line fix was made to MuseScore's own chord-symbol parser and is live in the fork | LIVE | 2026-08-02 · user | `CLAUDE.md` |"
       },
       {
-       "line_number": 668,
+       "line_number": 579,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-504 | A recognised harmonic sequence is ALWAYS emitted as key evidence — the earlier gate that emitted it only where no cadence existed threw corroboration away | LIVE | — | `cowork_progression_schema_design.md` §4.5 |"
       },
       {
-       "line_number": 778,
+       "line_number": 689,
        "term": "chord-symbol",
        "tier": "admitting",
        "line": "| D-316 | The chord-symbol parser sussus fix is a recorded local patch with an UPSTREAMABLE distribution disposition | LIVE | — | `CLAUDE.md` |"
       },
       {
-       "line_number": 817,
+       "line_number": 728,
        "term": "contradiction",
        "tier": "admitting",
        "line": "| D-649 | Where the implementation contradicts the decision being homed, the decision is written in as what it is with the contradiction stated beside it and no verdict taken | LIVE | — | `cowork_audit_protocol.md` |"
       },
       {
-       "line_number": 846,
+       "line_number": 757,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-221 | A sparse upper-register lowest note does not earn inversion bonuses | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |"
````

## 2(f) `python tools/audit/gen_guard_state.py --check` at the Task 2 edited tree, whole

````text
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
  [FAIL] tools/audit/gen_session_start_read_size.py --check
  [FAIL] tools/audit/gen_defense_share.py --check
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
83 guard(s) run, 16 failing, 4 not run, 20 historical record(s)
````

## 2(f) `diff` of the Task 2 capture against the opening capture

````text
61,62c61,62
<   [PASS] tools/audit/gen_session_start_read_size.py --check
<   [PASS] tools/audit/gen_defense_share.py --check
---
>   [FAIL] tools/audit/gen_session_start_read_size.py --check
>   [FAIL] tools/audit/gen_defense_share.py --check
109c109
< 83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
---
> 83 guard(s) run, 16 failing, 4 not run, 20 historical record(s)
````

## 3(b) `gen_status_batch_bound.py --apply`

````text
wrote tools\audit\status_batch_bound.json
  entries moved: 2, 2,585 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
````

## 3(b) `gen_status_batch_bound.py --check`

````text
  entries moved: 2, 2,585 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
````

## 3(b) `gen_governing_surface_split.py --check --pair STATUS.md`

````text
  STATUS.md / STATUS_ARCHIVE.md: moved 131 span(s), 457,949 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
````

## 3(b) `gen_status_residue_move.py --check`

````text
  candidates: 17, moved 16, left at site by the reading 1
  characters moved: 46,105
  byte-present in the companion exactly once: True
  absent from the must-read:                  True
  every flagged entry still at site:          True
````

## 3(b) `gen_status_archive_pass.py --check`

````text
  dated entries moved: 52
  at the pass commit, the live file was exactly base-minus-range: True
  the moved block is verbatim in the archive at HEAD:             True
  the moved block is absent from the live file at HEAD:           True
````

## 3(c) `gen_evidence_pin_membership.py --check`

````text
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
````

## 3(c) `gen_session_start_read_size.py --check` (before)

````text
STALE vs the measurement: session_start_read_size.json does not re-derive
````

## 3(c) `gen_defense_share.py --check` (before)

````text
STALE vs the measurement: defense_share.json does not re-derive
````

## 3(c) `gen_l0_l1_outgoing_population.py --check` (before)

````text
l0_l1_outgoing_population.json re-derives
````

## 3(c) `gen_l3_outgoing_population.py --check` (before)

````text
STALE vs the derivation: l3_outgoing_population.json does not re-derive
````

## 3(c) the four checks after regeneration

````text
== gen_session_start_read_size.py
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
    STATUS.md                                                                 12082
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 238274
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 238274 [ruled membership]  (-128847, -35.10%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 238274 [ruled membership]  (-58558, -19.73%)  <- CROSSES A REGIME BOUNDARY
exit:0
== gen_defense_share.py
the defense-share measurement re-derives
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   41071  ( 8.45%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (105876): 12.24%
    of the whole session-start read (238274): 5.44%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
exit:0
== gen_l0_l1_outgoing_population.py
l0_l1_outgoing_population.json re-derives
exit:0
== gen_l3_outgoing_population.py
l3_outgoing_population.json re-derives
exit:0
````

## 3(c) `git diff 7b4f925f… 246b9ddd…` — the L3 population diff against the start tip, whole

````text
diff --git a/7b4f925f671036e259d75e28a84dc6427c99be48 b/246b9ddda9bdf5fef039e85c0ceb8170215d7736
index 7b4f925f67..246b9ddda9 100644
--- a/7b4f925f671036e259d75e28a84dc6427c99be48
+++ b/246b9ddda9bdf5fef039e85c0ceb8170215d7736
@@ -498,7 +498,7 @@
    "paths_in_more_than_one_searched_class": [],
    "hits_per_term": {
     "cadence": 979,
-    "phrase": 581,
+    "phrase": 579,
     "inversion": 518,
     "grouping": 242,
     "chord symbol": 208,
@@ -19281,420 +19281,408 @@
       "governing-documents"
      ],
      "in_the_specification_document_set": false,
-     "hit_lines_distinct": 56,
-     "hits": 69,
+     "hit_lines_distinct": 54,
+     "hits": 67,
      "the_statement": "hit, outside the specification document set, not dispositioned by this comparison; reachable by the mining map",
      "hit_records": [
       {
-       "line_number": 28,
-       "term": "phrase",
-       "tier": "admitting",
-       "line": "> phase-1g entries (D-317…D-342) — D-319…D-341 directly; D-317/D-318 with rephrased plain"
-      },
-      {
-       "line_number": 34,
-       "term": "phrase",
-       "tier": "admitting",
-       "line": "> rephrased at the user's direction (the pedaled note can be in any voice, the D-207"
-      },
-      {
-       "line_number": 160,
+       "line_number": 90,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "`chordsymbolformatter.cpp`, which the record arm runs. A swept population with two demonstrated"
       },
       {
-       "line_number": 256,
+       "line_number": 173,
        "term": "phrase",
        "tier": "admitting",
        "line": "> **How a whole-document delegation is read.** A delegation that names a DOCUMENT and no section reaches EVERY section of it; a delegation that names SECTIONS reaches those sections and their subsections and no others; and the rule-stating half is judged PER SECTION in both cases. **THIS IS NOW PART OF THE RULE, NOT AN INTERPRETATION OF IT (user, 2026-08-03, phase 1r).** At phase 1q it was this pass's reading of D-430's \"delegates a stated concern to that section BY NAME\", taken on the record's own precedent rather than a preference — `OPEN_ITEMS.md` OI-290 states in terms that \"`ARCHITECTURE.md:1331` delegates 'this layer' and admits all sixteen of that document's entries\" — and the strict alternative was recorded as available to the user. The user then WROTE the reading into `CLAUDE.md` rule (h) itself as the GRANULARITY clause, so D-430's verbatim now carries it and the strict alternative is CLOSED. Its defense, stated with it: the strict reading would evict every document delegated as a whole, signed layer specifications among them, on the accident of how a pointer happens to be phrased, making the rule retroactively destructive rather than refining. THE STRICT ALTERNATIVE, PRESERVED (#12): read literally, a whole-document delegation names no section, so no section of it would be admitted and the seven whole-document homes would lose every entry between them."
       },
       {
-       "line_number": 311,
+       "line_number": 222,
        "term": "chord symbol",
        "tier": "admitting",
        "line": "| D-526 | The joint state's chord axis is SCALE-DEGREE-VALUED — a Roman numeral relative to the state's own tonic and mode — and the chord symbol is a DERIVED fact published once | LIVE | — | `cowork_joint_estimator_architecture.md` §5a |"
       },
       {
-       "line_number": 426,
+       "line_number": 337,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-605 | The local-key hypothesis derives from key-agnostic signals ONLY and never from the key-area grouping, which is a post-grouping of the resolved key — a hard design rule, not a preference | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 437,
+       "line_number": 348,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-290 | The key-agnostic local cadence approach is FALSIFIED at its precision ceiling | LIVE ⚠LEGACY | 2026-08-02 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 449,
+       "line_number": 360,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-494 | RATIFIED AMENDMENT A-4: the function layer must gain key-confirmation channels that do not require a cadence, plus an enharmonic-identity rule for key spans | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 470,
+       "line_number": 381,
        "term": "chord symbol",
        "tier": "admitting",
        "line": "| D-280 | Gates read structured fields only - never a chord symbol string and never a Roman numeral | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 475,
+       "line_number": 386,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-302 | No further local scoring fix for inversions may be attempted — the remaining divergence is not an analyzer defect | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 486,
+       "line_number": 397,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-327 | The root-continuity guard reads the reconstructed inversion credit, superseding the designed sounding-third test | LIVE ⚠LEGACY | 2026-08-02 · user | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 488,
+       "line_number": 399,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-329 | Completeness of the candidate list is the priority — a chord never listed can never be chosen | LIVE ⚠LEGACY | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §4 |"
       },
       {
-       "line_number": 489,
+       "line_number": 400,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-330 | Never a pooled recompute — the chord is never re-derived from several stretches' notes thrown together | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §8 |"
       },
       {
-       "line_number": 490,
+       "line_number": 401,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-331 | Every chord decision carries its ranked alternatives and its confidence — committed, inherited, and abstained alike, never pruned | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |"
       },
       {
-       "line_number": 491,
+       "line_number": 402,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-333 | The membership tie-break's direction is an idiom-calibrated number, never a branch on style — the three-tier structure is fixed | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |"
       },
       {
-       "line_number": 492,
+       "line_number": 403,
        "term": "chordsymbol",
        "tier": "admitting",
        "line": "| D-334 | The bare-fifth chord type stays in the catalogue structurally; whether it wins is an idiom-calibrated number | LIVE | 2026-08-02 · user | `cowork_layer4_chordsymbol_design.md` §15 |"
       },
       {
-       "line_number": 503,
+       "line_number": 414,
        "term": "chord symbol",
        "tier": "admitting",
        "line": "| D-501 | A tool may read a written chord symbol ONLY as a comparison or ground-truth label — never as input that influences what the analyzer computes | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 507,
+       "line_number": 418,
        "term": "bass note",
        "tier": "admitting",
        "line": "| D-536 | The bass note and the chord are chosen TOGETHER — the winner is the (bass, root, template) triple — replacing the sequential commit-the-bass-then-score pipeline | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 508,
+       "line_number": 419,
        "term": "slash chord",
        "tier": "admitting",
        "line": "| D-537 | The completeness bonus fires ONLY for a root-position reading whose three triad tones are all present — the guard that stops it from demoting genuine slash chords | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 514,
+       "line_number": 425,
        "term": "cadence",
        "tier": "admitting",
        "line": "## H. Layer 5 and Layer 6 — function, cadence, grouping — [full entries](decisions/group_H.md)"
       },
       {
-       "line_number": 514,
+       "line_number": 425,
        "term": "grouping",
        "tier": "admitting",
        "line": "## H. Layer 5 and Layer 6 — function, cadence, grouping — [full entries](decisions/group_H.md)"
       },
       {
-       "line_number": 518,
+       "line_number": 429,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-081 | The cadence detector is key-agnostic | LIVE | — | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 519,
+       "line_number": 430,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-082 | The grouping layer is additive, read-only, with no feedback | LIVE | — | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 519,
+       "line_number": 430,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-082 | The grouping layer is additive, read-only, with no feedback | LIVE | — | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 525,
+       "line_number": 436,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-336 | Cadence detection is key-agnostic and votes for the key rather than reading one | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §9 |"
       },
       {
-       "line_number": 526,
+       "line_number": 437,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-337 | A lean toward another degree is a tonicization by default; a key change needs a confirming cadence AND persistence, expressed as a change-cost | LIVE | 2026-08-02 · user | `cowork_layer5_function_design.md` §9 |"
       },
       {
-       "line_number": 529,
+       "line_number": 440,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-382 | The function layer selects by JOINT CONSISTENCY across tonality, root, inversion and bass — not by maximizing any one score — and every ambiguity kind reasons over the full carried distribution | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§3.1 The objective: select by JOINT CONSISTENCY, not by strengthening one score” |"
       },
       {
-       "line_number": 532,
+       "line_number": 443,
        "term": "contradiction",
        "tier": "admitting",
        "line": "| D-387 | A contradiction between the function context and a committed chord is surfaced on the ONE open mark, enriched with a reason — not on a second parallel flag, and not by overloading the plain undecided mark | LIVE | 2026-08-02 · user | `cowork_layer5_engagement_design.md` “§7.2 The vehicle” |"
       },
       {
-       "line_number": 542,
+       "line_number": 453,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-397 | The homeless analysis objects are ASSIGNED to named owners on the voice-leading dimension — the stock patterns, the melodic phrase, chord voicing, and part-writing advice — as claims, discharged only at each owner's own ratified design | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 544,
+       "line_number": 455,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-400 | A PER-VOICE span kind is admitted to the span typology — melodic phrases overlap across voices by construction and tile only within one voice | LIVE | 2026-08-02 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 546,
+       "line_number": 457,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-454 | The grouping layer detects nothing — it assembles what earlier layers decided, and pressure to add detection means the work belongs elsewhere | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §6 |"
       },
       {
-       "line_number": 546,
+       "line_number": 457,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-454 | The grouping layer detects nothing — it assembles what earlier layers decided, and pressure to add detection means the work belongs elsewhere | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §6 |"
       },
       {
-       "line_number": 547,
+       "line_number": 458,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-455 | A cadence away from a grouping boundary is surfaced as internal, never snapped to the nearest boundary and never discarded | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 547,
+       "line_number": 458,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-455 | A cadence away from a grouping boundary is surfaced as internal, never snapped to the nearest boundary and never discarded | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 548,
+       "line_number": 459,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-456 | Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 548,
+       "line_number": 459,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-456 | Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 548,
+       "line_number": 459,
        "term": "period",
        "tier": "admitting",
        "line": "| D-456 | Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §9 |"
       },
       {
-       "line_number": 549,
+       "line_number": 460,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-457 | A group truncated by the selection edge is marked as truncated, and a group that runs off the edge unclosed carries an extension cue the grouping layer only surfaces | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.1 |"
       },
       {
-       "line_number": 549,
+       "line_number": 460,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-457 | A group truncated by the selection edge is marked as truncated, and a group that runs off the edge unclosed carries an extension cue the grouping layer only surfaces | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.1 |"
       },
       {
-       "line_number": 550,
+       "line_number": 461,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-458 | The codetta refinement is read as the as-built tiling: keep the strong cut, drop the weak one, and record the codetta end as an annexe | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.1 |"
       },
       {
-       "line_number": 551,
+       "line_number": 462,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-459 | The key-area confidence is a declared margin-class boundary confidence, and its input is the declared key confidence — never the grading diagnostics' sigmoid | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.2 |"
       },
       {
-       "line_number": 552,
+       "line_number": 463,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-460 | A group counts as fully resolved exactly when no unit in it carries an unresolved mark — no confidence threshold enters the test | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §5.4 |"
       },
       {
-       "line_number": 553,
+       "line_number": 464,
        "term": "grouping layer",
        "tier": "admitting",
        "line": "| D-461 | The grouping layer is an explainability layer, not an accuracy requirement, and is deliberately kept thin | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §7 |"
       },
       {
-       "line_number": 553,
+       "line_number": 464,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-461 | The grouping layer is an explainability layer, not an accuracy requirement, and is deliberately kept thin | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §7 |"
       },
       {
-       "line_number": 554,
+       "line_number": 465,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-462 | Cadence validation is scoped to LOCATION; cadence TYPE is only partially attributable and is never a clean gate | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §10 |"
       },
       {
-       "line_number": 554,
+       "line_number": 465,
        "term": "grouping",
        "tier": "admitting",
        "line": "| D-462 | Cadence validation is scoped to LOCATION; cadence TYPE is only partially attributable and is never a clean gate | LIVE | 2026-08-04 · user | `cowork_layer6_grouping_design.md` §10 |"
       },
       {
-       "line_number": 556,
+       "line_number": 467,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-476 | The phrase-boundary primitive is owned by the notation-derived view layer — not by the note model, and not by the function layer that consumes it | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 557,
+       "line_number": 468,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-477 | Phrase boundaries are read from the written surface alone — never from a resolved key, chord or cadence — and the boundaries this misses are accepted, not recovered here | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §2 |"
       },
       {
-       "line_number": 557,
+       "line_number": 468,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-477 | Phrase boundaries are read from the written surface alone — never from a resolved key, chord or cadence — and the boundaries this misses are accepted, not recovered here | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §2 |"
       },
       {
-       "line_number": 558,
+       "line_number": 469,
        "term": "phrase boundary",
        "tier": "admitting",
        "line": "| D-478 | A phrase boundary is a peak in a continuous boundary-strength profile, not the OR of a few binary signals | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 558,
+       "line_number": 469,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-478 | A phrase boundary is a peak in a continuous boundary-strength profile, not the OR of a few binary signals | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 559,
+       "line_number": 470,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-479 | The boundary cues run per eligible voice and aggregate to the texture, and BOTH the per-voice and the texture boundaries are published | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 560,
+       "line_number": 471,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-480 | The phrase-boundary primitive is NOT an accuracy requirement — a competitive reference engine does no phrase segmentation at all — so it is built right but kept proportionate | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §8 |"
       },
       {
-       "line_number": 561,
+       "line_number": 472,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-481 | The notated markers are emitted as boundaries unconditionally; only the surface-cue strength is peak-picked | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §4.4 |"
       },
       {
-       "line_number": 562,
+       "line_number": 473,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-482 | The two hand-synchronised copies of the fermata scan retire into one owned primitive, and that retirement changes no output | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §6 |"
       },
       {
-       "line_number": 563,
+       "line_number": 474,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-483 | The picked boundaries are validated against the analysts' own phrase marks; a fermata-derived phrase list is inadmissible as ground truth because the primitive reads fermatas | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §7 |"
       },
       {
-       "line_number": 564,
+       "line_number": 475,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-484 | The phrase-boundary primitive is a derived view: it inherits the loaded span, requests no extension of its own, and publishes a per-profile max-normalised boundary confidence | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §2 |"
       },
       {
-       "line_number": 565,
+       "line_number": 476,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-485 | Each picked boundary should carry which cue fired and at what scope; the picked set is scope-blind today and the refinement waits for the inference phase | LIVE | 2026-08-04 · user | `cowork_phrase_boundary_design.md` §4.4 |"
       },
       {
-       "line_number": 568,
+       "line_number": 479,
        "term": "contradiction",
        "tier": "admitting",
        "line": "| D-492 | The recommended redesign is to demote the override to an annotation — carrying the earlier reading unchanged and surfacing the contradiction — floored by simply disabling it | LIVE | 2026-08-04 · user | `docs/scoring_model.md` |"
       },
       {
-       "line_number": 570,
+       "line_number": 481,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-495 | RATIFIED AMENDMENT A-5: when the phrase-boundary profile is flat, cadence admission relaxes with vote-weight scaling instead of starving | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 570,
+       "line_number": 481,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-495 | RATIFIED AMENDMENT A-5: when the phrase-boundary profile is flat, cadence admission relaxes with vote-weight scaling instead of starving | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 601,
+       "line_number": 512,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-584 | The perfect/imperfect cadence call is made on the BASS-DERIVED inversion; the soprano arrival degree is demoted to a soft optional nudge and the tool never attempts melody identification | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 601,
+       "line_number": 512,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-584 | The perfect/imperfect cadence call is made on the BASS-DERIVED inversion; the soprano arrival degree is demoted to a soft optional nudge and the tool never attempts melody identification | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 603,
+       "line_number": 514,
        "term": "phrase",
        "tier": "admitting",
        "line": "| D-607 | Polyphonic phrase-boundary detection has NO validated deterministic rule set in the literature — the extension is engineering on monophonic cues, validated against our own corpus, and is not settled science | LIVE | 2026-08-04 · user | `ARCHITECTURE.md` |"
       },
       {
-       "line_number": 649,
+       "line_number": 560,
        "term": "chord-symbol",
        "tier": "admitting",
        "line": "| D-315 | A one-line fix was made to MuseScore's own chord-symbol parser and is live in the fork | LIVE | 2026-08-02 · user | `CLAUDE.md` |"
       },
       {
-       "line_number": 668,
+       "line_number": 579,
        "term": "cadence",
        "tier": "admitting",
        "line": "| D-504 | A recognised harmonic sequence is ALWAYS emitted as key evidence — the earlier gate that emitted it only where no cadence existed threw corroboration away | LIVE | — | `cowork_progression_schema_design.md` §4.5 |"
       },
       {
-       "line_number": 778,
+       "line_number": 689,
        "term": "chord-symbol",
        "tier": "admitting",
        "line": "| D-316 | The chord-symbol parser sussus fix is a recorded local patch with an UPSTREAMABLE distribution disposition | LIVE | — | `CLAUDE.md` |"
       },
       {
-       "line_number": 817,
+       "line_number": 728,
        "term": "contradiction",
        "tier": "admitting",
        "line": "| D-649 | Where the implementation contradicts the decision being homed, the decision is written in as what it is with the contradiction stated beside it and no verdict taken | LIVE | — | `cowork_audit_protocol.md` |"
       },
       {
-       "line_number": 846,
+       "line_number": 757,
        "term": "inversion",
        "tier": "admitting",
        "line": "| D-221 | A sparse upper-register lowest note does not earn inversion bonuses | LIVE ⚠LEGACY | — | `docs/scoring_model.md` |"
@@ -20123,7 +20111,7 @@
      "the_statement": "hit, outside the specification document set, not dispositioned by this comparison; reachable by the mining map",
      "hit_records": [
       {
-       "line_number": 18,
+       "line_number": 20,
        "term": "phrase",
        "tier": "admitting",
        "line": "*★ ARCHIVED 2026-08-17, THE SECOND ACT — the dated entries that PREDATE (or paraphrase) the OI-222 pointer convention fell to `operative-rule-text` in the pinned measurement and stayed when the block above was cleared. They were READ one by one and moved verbatim to `STATUS_ARCHIVE.md` by `records/cc/instructions/cc_instruction_preparation_seventh.md` Task 1, under Ruling 3 of `records/cowork/rulings/cowork_rulings_2026_08_17_sixth_return.md`, which brings them under Ruling 4's own line. **One candidate did NOT move and is flagged:** the navigational paragraph at the foot of this file is not a completed batch's dated record but a live pointer to the archive and to the gate policy, so the read-before-move safeguard left it at site. The per-entry reconciliation is re-derived by `tools/audit/gen_status_residue_move.py --check`.*"
````

## 3(c) `git diff 32767966… 06759e7e…` — session_start_read_size.json

````text
diff --git a/3276796651c466ca78c5d9b66610669af4b6573d b/06759e7e4de5f7c5af9dcf7a481f81a5501809b2
index 3276796651..06759e7e4d 100644
--- a/3276796651c466ca78c5d9b66610669af4b6573d
+++ b/06759e7e4de5f7c5af9dcf7a481f81a5501809b2
@@ -176,11 +176,11 @@
   },
   "characters_per_member": {
    "CLAUDE.md": 105876,
-   "STATUS.md": 11863,
-   "DECISIONS.md": 127727,
+   "STATUS.md": 12082,
+   "DECISIONS.md": 117490,
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
   },
-  "total_characters": 248292,
+  "total_characters": 238274,
   "further_spans_of_the_same_artifact_NOT_counted_into_the_read": {
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows": {
     "characters": 62498,
@@ -276,10 +276,10 @@
    "from_commit": "1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
    "from_total": 367121,
    "from_regime": "whole-file practice",
-   "to_total": 248292,
+   "to_total": 238274,
    "to_regime": "ruled membership",
-   "change_in_characters": -118829,
-   "change_percent": -32.37,
+   "change_in_characters": -128847,
+   "change_percent": -35.1,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   },
@@ -287,10 +287,10 @@
    "from_commit": "594074e1e1900079e449d2b79a38920d21bca6e6",
    "from_total": 296832,
    "from_regime": "whole-file practice",
-   "to_total": 248292,
+   "to_total": 238274,
    "to_regime": "ruled membership",
-   "change_in_characters": -48540,
-   "change_percent": -16.35,
+   "change_in_characters": -58558,
+   "change_percent": -19.73,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   }
````

## 3(c) `git diff 33fc249f… fe1f38ae…` — defense_share.json

````text
diff --git a/33fc249fb78c03fe9d920d671cfef58c6ac0199d b/fe1f38ae34793b0b8b71430eefcd75d3a00c63e0
index 33fc249fb7..fe1f38ae34 100644
--- a/33fc249fb78c03fe9d920d671cfef58c6ac0199d
+++ b/fe1f38ae34793b0b8b71430eefcd75d3a00c63e0
@@ -77,7 +77,7 @@
  ],
  "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
   "the_six_session_start_spans": 105876,
-  "the_whole_ordinary_session_start_read": 248292,
+  "the_whole_ordinary_session_start_read": 238274,
   "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked defense; the second says how much of the WHOLE boot it is. A share quoted against one of them is not the share against the other."
  },
  "per_span": [
@@ -142,7 +142,7 @@
   "characters_had_every_clause_been_closed_at_the_next_marked_clause": 51684,
   "characters_had_every_clause_run_to_its_paragraph_end": 160906,
   "share_of_the_six_session_start_spans": 12.24,
-  "share_of_the_whole_ordinary_session_start_read": 5.22
+  "share_of_the_whole_ordinary_session_start_read": 5.44
  },
  "every_clause_published_so_the_tables_reach_is_inspectable_rather_than_asserted": [
   {
````

## 3(c) `gen_per_session_reading.py --check` (before)

````text
STALE vs the measurement: per_session_reading.json does not re-derive
````

## 3(c) `gen_per_session_reading.py` (write mode)

````text
wrote tools/audit/per_session_reading.json
  the ordinary session-start read (imported) 238274
    CLAUDE.md, the whole file as the executing sessions report it injected   169617
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674135
  Cowork, per sitting, in the shape of the sitting of entry 461: 972954
  six spans 105876 characters, 106 sub-blocks, archive-class 14269, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
````

## 3(c) `gen_per_session_reading.py --check` (after)

````text
the per-session reading measurement re-derives
  the ordinary session-start read (imported) 238274
    CLAUDE.md, the whole file as the executing sessions report it injected   169617
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 674135
  Cowork, per sitting, in the shape of the sitting of entry 461: 972954
  six spans 105876 characters, 106 sub-blocks, archive-class 14269, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
````

## 3(c) `git diff 13654d2a… 3305cac0…` — per_session_reading.json

````text
diff --git a/13654d2a216ef92c204e5f10b2fdd856ad38eb20 b/3305cac01da11b36483c02ab430c889a7284c25c
index 13654d2a21..3305cac01d 100644
--- a/13654d2a216ef92c204e5f10b2fdd856ad38eb20
+++ b/3305cac01da11b36483c02ab430c889a7284c25c
@@ -15,11 +15,11 @@
    "its_one_home": "`tools/audit/session_start_read_size.json`, written by `tools/audit/gen_session_start_read_size.py`; what stands here is that tool's own `measure` called at the tree, and its total is checked against that artifact on every run",
    "characters_per_member": {
     "CLAUDE.md": 105876,
-    "STATUS.md": 11863,
-    "DECISIONS.md": 127727,
+    "STATUS.md": 12082,
+    "DECISIONS.md": 117490,
     "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
    },
-   "total_characters": 248292,
+   "total_characters": 238274,
    "the_reading_of_claude_md": {
     "regime": "ruled membership",
     "characters": 105876
@@ -782,28 +782,28 @@
      "the_writing_sides_read": "unwritten practice"
     },
     "the_record_that_mandates_it": "the standing clause `Every dispatch's read-first block names the CURRENT HANDOVER BLOCK`, which this repository carries as numbered entry files; the writing side's three is its own practice",
-    "the_population_count": 389,
+    "the_population_count": 391,
     "the_three": [
      {
-      "name": "cowork_handoff_entry_four_hundred_and_sixty_eight.md",
+      "name": "cowork_handoff_entry_four_hundred_and_sixty_seven.md",
       "added_in_commit": "f2d0ae14ba2037ba4111c12c52d314b463d77741",
       "added_at_unix_time": 1793563784,
-      "characters": 7526
+      "characters": 7559
      },
      {
-      "name": "cowork_handoff_entry_four_hundred_and_sixty_nine.md",
-      "added_in_commit": "f2d0ae14ba2037ba4111c12c52d314b463d77741",
-      "added_at_unix_time": 1793563784,
-      "characters": 6648
+      "name": "cowork_handoff_entry_four_hundred_and_seventy.md",
+      "added_in_commit": "749ab8c88a7e5221c73fcdc7d96a040c7fb3580b",
+      "added_at_unix_time": 1793567013,
+      "characters": 7952
      },
      {
-      "name": "cowork_handoff_entry_four_hundred_and_sixty_seven.md",
-      "added_in_commit": "f2d0ae14ba2037ba4111c12c52d314b463d77741",
-      "added_at_unix_time": 1793563784,
-      "characters": 7559
+      "name": "cowork_handoff_entry_four_hundred_and_seventy_one.md",
+      "added_in_commit": "749ab8c88a7e5221c73fcdc7d96a040c7fb3580b",
+      "added_at_unix_time": 1793567013,
+      "characters": 6218
      }
     ],
-    "characters": 21733
+    "characters": 21729
    }
   ],
   "totals_by_side": {
@@ -811,7 +811,7 @@
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 248292
+      "characters": 238274
      },
      {
       "member": "BUILD_AND_TEST.md",
@@ -831,11 +831,11 @@
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 21733
+      "characters": 21729
      }
     ],
-    "without_the_injected_copy_of_CLAUDE_md": 684157,
-    "with_it": 853774,
+    "without_the_injected_copy_of_CLAUDE_md": 674135,
+    "with_it": 843752,
     "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, 169617 characters",
     "left_out_and_said_so": "the previous report at the portions a dispatch orders, the reading file at its ordered portions, the ruling records a dispatch orders — varies per dispatch and is not sized here"
    },
@@ -843,7 +843,7 @@
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 248292
+      "characters": 238274
      },
      {
       "member": "entry 118, the bridge-fault section",
@@ -863,7 +863,7 @@
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 21733
+      "characters": 21729
      },
      {
       "member": "the latest report of the arc, whole: cc_report_l3_comparison_tabulation_thirtieth_2026_10_31.md",
@@ -874,7 +874,7 @@
       "characters": 151805
      }
     ],
-    "characters": 982976,
+    "characters": 972954,
     "left_out_and_said_so": "the verification reads at the objects (the reading file at its sections, the guard state, the ref files, the away-returns close) — varies per batch and is not sized here"
    }
   }
@@ -3260,7 +3260,7 @@
     "characters_had_every_clause_been_closed_at_the_next_marked_clause": 51684,
     "characters_had_every_clause_run_to_its_paragraph_end": 160906,
     "share_of_the_six_session_start_spans": 12.24,
-    "share_of_the_whole_ordinary_session_start_read": 5.22
+    "share_of_the_whole_ordinary_session_start_read": 5.44
    },
    "per_span": [
     {
@@ -3320,7 +3320,7 @@
    ],
    "the_two_denominators": {
     "the_six_session_start_spans": 105876,
-    "the_whole_ordinary_session_start_read": 248292
+    "the_whole_ordinary_session_start_read": 238274
    },
    "how_these_relate_to_the_sums_above": "a marked clause lies INSIDE a sub-block, so these values overlap table 2's sums and are never added to them"
   }
````
