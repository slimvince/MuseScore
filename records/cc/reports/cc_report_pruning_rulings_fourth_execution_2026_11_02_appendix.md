# CC report APPENDIX — the pruning iteration, step 4, Ruling 1 carried out a fourth time (2026-11-02)

> **APPENDIX FILE of `records/cc/reports/cc_report_pruning_rulings_fourth_execution_2026_11_02.md`** (Ruling 4
> of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`). It carries the raw
> printouts VERBATIM, each under a heading naming its command and the step it served. Every verdict, count and
> difference stands in the report proper; this file is read where a verification needs a particular printout.

## A1. Task 0(b) — `git show --stat 1126176e2a4b48fc01bbb5b545210715366cb24a`

````text
commit 1126176e2a4b48fc01bbb5b545210715366cb24a
Author: Vincent Wong <65764495+slimvince@users.noreply.github.com>
Date:   Sun Nov 1 22:52:58 2026 +0100

    End state: the pruning iteration step 4 third execution - guard run at the close tree, the A2 regenerations already met inside the close
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 records/cowork/handoff/cowork_away_returns.md | 44 +++++++++++++++++++++++++++
 tools/audit/guard_state.json                  | 22 +++++++-------
 2 files changed, 55 insertions(+), 11 deletions(-)
````

## A2. Task 0(b) — `git show --stat c7b6985a9c0be8fb7f975addf2fb0642c0311c29`

````text
commit c7b6985a9c0be8fb7f975addf2fb0642c0311c29
Author: Vincent Wong <65764495+slimvince@users.noreply.github.com>
Date:   Sun Nov 1 22:43:47 2026 +0100

    Close: the pruning iteration step 4 - Rulings 1 and 3 carried out a third time, under its dispatch
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 STATUS.md                                          |    6 +-
 STATUS_ARCHIVE.md                                  |    6 +
 ...t_pruning_rulings_third_execution_2026_11_01.md |  399 +++
 ..._rulings_third_execution_2026_11_01_appendix.md | 3160 ++++++++++++++++++++
 records/cowork/handoff/cowork_away_returns.md      |   54 +
 tools/audit/defense_share.json                     |    4 +-
 tools/audit/gen_status_batch_bound.py              |   29 +-
 tools/audit/l0_l1_outgoing_population.json         |   74 +-
 tools/audit/l3_outgoing_population.json            |  154 +-
 tools/audit/per_session_reading.json               |   48 +-
 tools/audit/session_start_read_size.json           |   18 +-
 tools/audit/status_batch_bound.json                |   26 +-
 12 files changed, 3808 insertions(+), 170 deletions(-)
````

## A3. Task 0(b) — `git show --stat f630b1eb09b2a0c395a94ff2b99b6b5d7936b43c`

````text
commit f630b1eb09b2a0c395a94ff2b99b6b5d7936b43c
Author: Vincent Wong <65764495+slimvince@users.noreply.github.com>
Date:   Sun Nov 1 22:37:34 2026 +0100

    ruling: four classes of history text out of the rendered DECISIONS.md and into DECISIONS_ARCHIVE.md under Ruling 3 of 2026-11-01 - the decisions register data unedited, one check citation re-aimed
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 DECISIONS.md                                       | 111 ++------------
 DECISIONS_ARCHIVE.md                               | 131 ++++++++++++++++
 tools/audit/decisions/gen_decisions_register.py    | 167 ++++++++-------------
 .../decisions/gen_phase1w_legacy_verification.py   |  19 ++-
 4 files changed, 221 insertions(+), 207 deletions(-)
````

## A4. Task 0(b) — `git show --stat 749ab8c88a7e5221c73fcdc7d96a040c7fb3580b`

````text
commit 749ab8c88a7e5221c73fcdc7d96a040c7fb3580b
Author: Vincent Wong <65764495+slimvince@users.noreply.github.com>
Date:   Sun Nov 1 22:03:33 2026 +0100

    record: entries 470 and 471 and the step-4 third execution dispatch
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 ...n_pruning_rulings_third_execution_2026_11_01.md | 505 +++++++++++++++++++++
 ...owork_handoff_entry_four_hundred_and_seventy.md |  91 ++++
 ...k_handoff_entry_four_hundred_and_seventy_one.md |  72 +++
 3 files changed, 668 insertions(+)
````

## A5. Task 0(c) — A1's enumeration, `python tools/audit/changed_paths.py`, whole

````text
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_five.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_four.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_three.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_two.md
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
399 changed path record(s) [worktree]
````

## A6. Task 0(c) — `git ls-files --others --exclude-standard -- <path>` per landing path

````text
== records/cc/instructions/cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md
records/cc/instructions/cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_two.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_two.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_three.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_three.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_four.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_four.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_five.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_five.md
exit:0
````

## A7. Task 0(c) — `git diff --stat 1126176e… -- <path>` per named path

````text
== CLAUDE.md
exit:0
== CLAUDE_ARCHIVE.md
exit:0
== DECISIONS.md
exit:0
== DECISIONS_ARCHIVE.md
exit:0
== tools/audit/decisions/gen_decisions_register.py
exit:0
== tools/audit/decisions/gen_phase1w_legacy_verification.py
exit:0
== tools/audit/decisions/backbone_decisions.json
exit:0
== tools/audit/decisions/cluster_dispositions.json
exit:0
== STATUS.md
exit:0
== STATUS_ARCHIVE.md
exit:0
== tools/audit/gen_status_batch_bound.py
exit:0
== tools/audit/status_batch_bound.json
exit:0
== cowork_audit_protocol.md
exit:0
== BUILD_AND_TEST.md
exit:0
== tools/audit/gen_derivation_boot_pack.py
exit:0
== tools/audit/derivation_boot_pack.json
exit:0
== tools/audit/derivation_boot_pack/l3
exit:0
````

## A8. Task 0(d) — the last-bytes check (scratch script `t0d_lastbytes.py`)

````text
dispatch 50edaf8582a3748089caffe03641a3629ed68c62: size 51166 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b'e freeze. That\ncosts a further dispatch but leaves the record intact.\n'
entry 472 619924318d32fb0efdb16e7656de7caf28655598: size 7300 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b'on entry 471. The user\'s words: the opening instruction;\n"continue".*\n'
entry 473 b5815df9e93eece09d7934cac0576ec08ff05a85: size 7177 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b'on entry 472. The user\'s words: the opening instruction;\n"continue".*\n'
entry 474 9d80352ec5d33d44a378ec7a1b133002ab3a86f5: size 8872 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b"ting booted on entry 473. The user's words: the opening\ninstruction.*\n"
entry 475 0f01a014cedb57277d747cd1d15cea627eaafb26: size 6785 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b'74. The user\'s words: the opening\ninstruction; "naroow"; "continue".*\n'
````

## A9. Task 0(e) — `python tools/audit/gen_evidence_pin_membership.py --check`

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

## A10. Task 0(e) — `python tools/audit/changed_paths.py --staged`

````text
A	records/cc/instructions/cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_five.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_four.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_three.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_two.md
5 changed path record(s) [staged]
````

## A11. Task 0(e) — `git show --stat` of the Task 0 commit

````text
commit bfd15c7fdd6e010a2ad163cfb0dddd26e46239a1
Author: Vincent Wong <65764495+slimvince@users.noreply.github.com>
Date:   Mon Nov 2 08:37:05 2026 +0100

    record: entries 472 to 475 and the step-4 fourth execution dispatch
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 ..._pruning_rulings_fourth_execution_2026_11_02.md | 615 +++++++++++++++++++++
 ..._handoff_entry_four_hundred_and_seventy_five.md |  85 +++
 ..._handoff_entry_four_hundred_and_seventy_four.md |  98 ++++
 ...handoff_entry_four_hundred_and_seventy_three.md |  83 +++
 ...k_handoff_entry_four_hundred_and_seventy_two.md |  85 +++
 5 files changed, 966 insertions(+)
````

## A12. Task 0(f) — the opening guard capture, `python tools/audit/gen_guard_state.py --check`, whole

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

## A13. Task 0(f) — `python tools/audit/gen_guard_classification.py --check`

````text
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_per_session_reading.py', 'tools/audit/gen_withheld_family_reading.py']
````

## A14. Task 0(g) — `gen_session_start_read_size.py --check`

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
    STATUS.md                                                                 12082
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 238274
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 238274 [ruled membership]  (-128847, -35.10%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 238274 [ruled membership]  (-58558, -19.73%)  <- CROSSES A REGIME BOUNDARY
````

## A15. Task 0(g) — `gen_defense_share.py --check`

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
    of the whole session-start read (238274): 5.44%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
````

## A16. Task 0(g) — `decisions/gen_decisions_register.py --check`

````text
the register matches the data (20 files: the index + 19 group files)
````

## A17. Task 0(g) — `decisions/gen_cluster_dispositions.py --verify`, whole (the BEFORE of Decision 2)

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

## A18. Task 0(g) — `decisions/reaim_home_anchors.py --check`, whole (the BEFORE of Decision 2)

````text
  D-196: CLAUDE.md:1979 -> CLAUDE.md:1991   (drift +12)
  D-253: CLAUDE.md:1918-1936 -> CLAUDE.md:1930-1948   (drift +12)
  D-254: CLAUDE.md:1961-1968 -> CLAUDE.md:1973-1980   (drift +12)
  D-268: cowork_confidence_contract.md:36-48 -> cowork_confidence_contract.md:54-66   (drift +18)
  D-269: cowork_confidence_contract.md:83-85 -> cowork_confidence_contract.md:101-103   (drift +18)
  D-601: cowork_confidence_contract.md:89-101 -> cowork_confidence_contract.md:107-119   (drift +18)
anchors drifted: 6
````

## A19. Task 0(g) — `gen_l0_l1_outgoing_population.py --check`

````text
l0_l1_outgoing_population.json re-derives
````

## A20. Task 0(g) — `gen_l3_outgoing_population.py --check`

````text
l3_outgoing_population.json re-derives
````

## A21. Task 0(g) — `decisions/gen_phase1w_legacy_verification.py --check`

````text
phase1w: A1 held; 57 entries derived; 35 anchors located; 5 recorded figures located
````

## A22. Task 0(g) — `gen_claude_md_finer_archive.py --check`

````text
FAIL: the finer archive record does not re-derive: tools\audit\claude_md_finer_archive.json
````

## A23. Task 0(g) — `gen_claude_md_prune_backlog.py --check`

````text
FAIL: the prune-at-amendment backlog record does not re-derive: tools\audit\claude_md_prune_backlog.json
````

## A24. Task 0(g) — the differing-values script (`differing_values.py`), BEFORE

````text
== gen_claude_md_finer_archive: 1 differing value(s) (artifact vs rebuild)
   reconciliation.every_span_the_ruling_REFUSED_is_still_present_at_site_exactly_once: artifact True | rebuild False
== gen_claude_md_prune_backlog: 1 differing value(s) (artifact vs rebuild)
   reconciliation.every_span_the_reading_flagged_is_still_present_at_site_exactly_once: artifact True | rebuild False
````

## A25. Task 1(a) — `gen_derivation_boot_pack.py --check`, before the freeze

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

## A26. Task 1(b) 1 — `git log … -- tools/audit/derivation_boot_pack/l3`

````text
ca55115f81ee99cc057f04a75747f51a93a43073 2026-10-17 11:08:01 +0200 author the l3 withheld family and extras, and render the l3 boot pack; the lists go to the user
````

## A27. Task 1(b) 2 — `git log … -- cowork_blind_derivation_l3_2026_10_17.md …`

````text
96a24b01b87b94ce157ff471946e38c664d6f844 2026-10-17 22:19:15 +0200 record: the l3 blind derivation, the released l3 brief and entries 419-420 landed
````

## A28. Task 1(b) 3 — the forty hash queries (scratch script `t1b_forty_hashes.py`)

````text
| File | at <T0> | at the render commit | hash-object | hash-object --no-filters | all four equal |
|---|---|---|---|---|---|
| `00_READ_THIS_FIRST.md` | `b3f25abafea31719ee91fa26244636923496165b` | `b3f25abafea31719ee91fa26244636923496165b` | `b3f25abafea31719ee91fa26244636923496165b` | `b3f25abafea31719ee91fa26244636923496165b` | yes |
| `01_the_phase_definitions.md` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | yes |
| `02_the_guiding_principles_and_the_conventions.md` | `51d1ad73a10f732fec10d792069ecc2833503d5e` | `51d1ad73a10f732fec10d792069ecc2833503d5e` | `51d1ad73a10f732fec10d792069ecc2833503d5e` | `51d1ad73a10f732fec10d792069ecc2833503d5e` | yes |
| `03_the_writing_standards.md` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` | yes |
| `04_the_dispatch_protocol.md` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` | yes |
| `05_the_ratified_design_intent.md` | `fe04029239a93f3908d0a776d98108b22fb7484b` | `fe04029239a93f3908d0a776d98108b22fb7484b` | `fe04029239a93f3908d0a776d98108b22fb7484b` | `fe04029239a93f3908d0a776d98108b22fb7484b` | yes |
| `06_the_defect_type_catalog.md` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | yes |
| `07_the_charter_the_layers_and_the_decisions.md` | `2ed8a5ca2b531f48519279941059fee259af03b7` | `2ed8a5ca2b531f48519279941059fee259af03b7` | `2ed8a5ca2b531f48519279941059fee259af03b7` | `2ed8a5ca2b531f48519279941059fee259af03b7` | yes |
| `08_the_seventeen_research_extracts.md` | `91c8af752315f991c2a681bd7b2b189c0f51dab8` | `91c8af752315f991c2a681bd7b2b189c0f51dab8` | `91c8af752315f991c2a681bd7b2b189c0f51dab8` | `91c8af752315f991c2a681bd7b2b189c0f51dab8` | yes |
| `09_the_empirical_findings_ledger.md` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` | yes |
files in the directory at <T0>: 10; equal to the ten named: True
1(b) STEP 3 PASS
````

## A29. Task 1(d) — `gen_derivation_boot_pack.py` (write mode)

````text
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
````

## A30. Task 1(d) — `changed_paths.py` after write mode, whole

````text
 M	tools/audit/claude_md_finer_archive.json
 M	tools/audit/derivation_boot_pack.json
 M	tools/audit/gen_derivation_boot_pack.py
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
396 changed path record(s) [worktree]
````

## A31. Task 1(d) — the ten L3 files re-hashed after write mode

````text
| File | at <T0> | at the render commit | hash-object | hash-object --no-filters | all four equal |
|---|---|---|---|---|---|
| `00_READ_THIS_FIRST.md` | `b3f25abafea31719ee91fa26244636923496165b` | `b3f25abafea31719ee91fa26244636923496165b` | `b3f25abafea31719ee91fa26244636923496165b` | `b3f25abafea31719ee91fa26244636923496165b` | yes |
| `01_the_phase_definitions.md` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | `518b1e50d60af2b4e2ddcd8978623832eb071899` | yes |
| `02_the_guiding_principles_and_the_conventions.md` | `51d1ad73a10f732fec10d792069ecc2833503d5e` | `51d1ad73a10f732fec10d792069ecc2833503d5e` | `51d1ad73a10f732fec10d792069ecc2833503d5e` | `51d1ad73a10f732fec10d792069ecc2833503d5e` | yes |
| `03_the_writing_standards.md` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` | `a41983018cb27ed4a47d24ff8bb9e95181ed0572` | yes |
| `04_the_dispatch_protocol.md` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` | `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da` | yes |
| `05_the_ratified_design_intent.md` | `fe04029239a93f3908d0a776d98108b22fb7484b` | `fe04029239a93f3908d0a776d98108b22fb7484b` | `fe04029239a93f3908d0a776d98108b22fb7484b` | `fe04029239a93f3908d0a776d98108b22fb7484b` | yes |
| `06_the_defect_type_catalog.md` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | `1dec7621dc48d89242cacaf79b3048cd965d6a19` | yes |
| `07_the_charter_the_layers_and_the_decisions.md` | `2ed8a5ca2b531f48519279941059fee259af03b7` | `2ed8a5ca2b531f48519279941059fee259af03b7` | `2ed8a5ca2b531f48519279941059fee259af03b7` | `2ed8a5ca2b531f48519279941059fee259af03b7` | yes |
| `08_the_seventeen_research_extracts.md` | `91c8af752315f991c2a681bd7b2b189c0f51dab8` | `91c8af752315f991c2a681bd7b2b189c0f51dab8` | `91c8af752315f991c2a681bd7b2b189c0f51dab8` | `91c8af752315f991c2a681bd7b2b189c0f51dab8` | yes |
| `09_the_empirical_findings_ledger.md` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` | `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6` | yes |
files in the directory at <T0>: 10; equal to the ten named: True
1(b) STEP 3 PASS
````

## A32. Task 1(e) — THE D-657 COMPARISON (scratch script `t1e_compare.py`), whole

````text
ADDED    subjects -> l3 -> counted -> ★_which_of_these_counts_describe_the_DIRECTORY
         before null
         after  "`files_in_the_pack` is COUNTED IN THE PACK DIRECTORY. The other counts here are over this tool's authored tables and over the candidate derivation against toda…
         [the added field under counted]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 0 -> spans -> 0 -> lines_rendered
         before 242
         after  null
         [a span's lines_rendered removed]
ADDED    subjects -> l3 -> the_members_as_rendered -> 0 -> ★_where_this_record's_measures_COME_FROM
         before null
         after  "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at the frozen file itself and never at a re-render. The per-span, per-part and…
         [the added per-member field]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 1 -> spans -> 0 -> lines_rendered
         before 309
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 1 -> spans -> 1 -> lines_rendered
         before 463
         after  null
         [a span's lines_rendered removed]
ADDED    subjects -> l3 -> the_members_as_rendered -> 1 -> ★_where_this_record's_measures_COME_FROM
         before null
         after  "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at the frozen file itself and never at a re-render. The per-span, per-part and…
         [the added per-member field]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 2 -> spans -> 0 -> lines_rendered
         before 189
         after  null
         [a span's lines_rendered removed]
ADDED    subjects -> l3 -> the_members_as_rendered -> 2 -> ★_where_this_record's_measures_COME_FROM
         before null
         after  "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at the frozen file itself and never at a re-render. The per-span, per-part and…
         [the added per-member field]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 3 -> spans -> 0 -> lines_rendered
         before 1426
         after  null
         [a span's lines_rendered removed]
ADDED    subjects -> l3 -> the_members_as_rendered -> 3 -> ★_where_this_record's_measures_COME_FROM
         before null
         after  "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at the frozen file itself and never at a re-render. The per-span, per-part and…
         [the added per-member field]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 4 -> entries_rendered
         before 218
         after  null
         [a member-level count removed]
ADDED    subjects -> l3 -> the_members_as_rendered -> 4 -> ★_where_this_record's_measures_COME_FROM
         before null
         after  "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at the frozen file itself and never at a re-render. The per-span, per-part and…
         [the added per-member field]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 5 -> rows_rendered
         before 25
         after  null
         [a member-level count removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 5 -> columns_kept
         before ["ID", "type (plain)"]
         after  null
         [a member-level count removed]
ADDED    subjects -> l3 -> the_members_as_rendered -> 5 -> ★_where_this_record's_measures_COME_FROM
         before null
         after  "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at the frozen file itself and never at a re-render. The per-span, per-part and…
         [the added per-member field]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 6 -> parts -> 0 -> spans -> 0 -> lines_rendered
         before 240
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 6 -> parts -> 0 -> spans -> 1 -> lines_rendered
         before 240
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 6 -> parts -> 0 -> filters_applied -> 0 -> the_text_removed
         before "*(This is adopted from this project's material; the first-stage draft\nhad no second axis and placed phrase structure on the spine. Appendix A item 5, change 2…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 6 -> parts -> 0 -> filters_applied -> 0 -> characters_removed
         before 161
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 6 -> parts -> 0 -> filters_applied -> 1 -> the_text_removed
         before "*(Stage\ntwo established that this project's own layer specifications do not state the answer either: they state\nthat the sonority is functionally folded into…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 6 -> parts -> 0 -> filters_applied -> 1 -> characters_removed
         before 363
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 6 -> parts -> 0 -> filters_applied -> 2 -> the_text_removed
         before "*(Stage two found the same question open in this project's own\nrecord, from the other direction: one rule states that the decoder always commits on the tonali…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 6 -> parts -> 0 -> filters_applied -> 2 -> characters_removed
         before 338
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 6 -> parts -> 0 -> characters
         before 36207
         after  null
         [a `parts` entry's characters removed]
ADDED    subjects -> l3 -> the_members_as_rendered -> 6 -> ★_where_this_record's_measures_COME_FROM
         before null
         after  "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at the frozen file itself and never at a re-render. The per-span, per-part and…
         [the added per-member field]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> spans -> 0 -> lines_rendered
         before 332
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 0 -> the_text_removed
         before "> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-10-14).** Written under\n> `cowork_reading_pass_commission_2026_08_30.md` §4.\n>\n> **The grade.…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 0 -> characters_removed
         before 1445
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 1 -> the_text_removed
         before "**File:** `docs/research_papers/ju_margot_mckay_dahn_fujinaga_2020_ismir_bcfb_figured_bass.pdf`\n(1,022,218 bytes at the staging result)."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 1 -> characters_removed
         before 136
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 2 -> the_text_removed
         before " *(★ CORRECTED 2026-10-15 at the cross-check against the second extract, at the\npage: the printed word is \"obbligato\". Former wording, preserved (#12): \"ob…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 2 -> characters_removed
         before 165
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 3 -> the_text_removed
         before " *(This bears on guiding principle #20, fit/evaluation separation: the\n85.3% is a figure the rules were selected against. The machine-learning figures below a…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 3 -> characters_removed
         before 179
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 4 -> the_text_removed
         before " *(★ CORRECTED 2026-10-15 at the cross-check against the second\nextract, at the footnote: the paper says \"one octave apart\", not \"an octave or more\". Form…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 4 -> characters_removed
         before 279
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 5 -> heading
         before "## What an L3 detail specification could adopt, adapt, or must argue against"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 5 -> closes_before
         before "## ★ Findings, routed and not applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 5 -> the_text_removed
         before "## What an L3 detail specification could adopt, adapt, or must argue against\n\n*(The L3 charter, `FRAMEWORK.md` §5 \"L3 — The read-off facts\": L3 answers \"g…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 5 -> characters_removed
         before 2362
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 6 -> heading
         before "## ★ Findings, routed and not applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 6 -> closes_before
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 6 -> the_text_removed
         before "## ★ Findings, routed and not applied\n\n**(1) A statement in `FRAMEWORK.md` pairs this paper's figures wrongly.** `FRAMEWORK.md` Appendix B, §S2\n(the first-s…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 6 -> characters_removed
         before 2733
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 7 -> heading
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 7 -> closes_before
         before "## What this extract does NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 7 -> the_text_removed
         before "## Centrality\n\n**CENTRAL** — L3 publishes the figured bass, this is the one producer of it in the read set (the row's\nrecorded reason), and its claims would…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 7 -> characters_removed
         before 409
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 8 -> heading
         before "## What this extract does NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 8 -> closes_before
         before "## The read-back, recorded"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 8 -> the_text_removed
         before "## What this extract does NOT do\n\nIt derives no specification statement, amends no document, opens no code, touches no measurement tool,\ncorpus or golden, w…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 8 -> characters_removed
         before 328
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 9 -> heading
         before "## The read-back, recorded"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 9 -> closes_before
         before "## The cross-check against the second extract (2026-10-15)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 9 -> the_text_removed
         before "## The read-back, recorded\n\nAfter the sections above were written, the text was read back against the page images, and swept for\nabsolutes (only, never, eve…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 9 -> characters_removed
         before 865
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 10 -> heading
         before "## The cross-check against the second extract (2026-10-15)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 10 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 10 -> the_text_removed
         before "## The cross-check against the second extract (2026-10-15)\n\nThe second independent extraction is at\n`reading_pass/extracts_second_pass/ju-margot-mckay-dahn-…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> filters_applied -> 10 -> characters_removed
         before 978
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 0 -> characters
         before 13448
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> spans -> 0 -> lines_rendered
         before 225
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 0 -> the_text_removed
         before "> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under\n> `cowork_reading_pass_commission_2026_08_30.md` §4.\n>\n> **The grade.…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 0 -> characters_removed
         before 2069
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 1 -> the_text_removed
         before "**File:** `docs/research_papers/bigo_feisthauer_giraud_leve_2018_ismir_cadence_detection_features.pdf`."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 1 -> characters_removed
         before 103
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 2 -> the_text_removed
         before " that make this L1's paper"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 2 -> characters_removed
         before 26
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 3 -> the_text_removed
         before " The feature that IS the L1 charter's third cue."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 3 -> characters_removed
         before 48
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 4 -> the_text_removed
         before " *(★ CORRECTED 2026-09-20 ON THE USER'S RULING.\nFORMER WORDING, PRESERVED (#12): \"Both notes 4 and 7 of the tonality that would be implied by the bass of\nZ …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 4 -> characters_removed
         before 434
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 5 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED (#12): \"Note that we previously reported 82% of PAC\ndetection in fugues with manual hand-coded rules but …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 5 -> characters_removed
         before 296
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 6 -> the_text_removed
         before " — and it is the framework's own sentence"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 6 -> characters_removed
         before 41
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 7 -> the_text_removed
         before " *(★ CORRECTED 2026-09-20 ON THE USER'S RULING. FORMER WORDING, PRESERVED (#12):\n\"**[FACT, §4.4]** Rhythmic features matter most where the harmony is weakest…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 7 -> characters_removed
         before 341
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 8 -> the_text_removed
         before " *(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED\n(#12): \"(PAC, rIAC or HC)\" — the page trains PAC and PAC+rIAC on the Bach corpus and PAC and HC on the\…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 8 -> characters_removed
         before 261
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 9 -> the_text_removed
         before " *(★ CORRECTED 2026-09-20. FORMER WORDING,\nPRESERVED (#12): \"Suspensions were expected to be significant for both PAC and HC and\" — the page (358,\n§4.2) sa…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 9 -> characters_removed
         before 337
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 10 -> heading
         before "## What an L1 detail specification could adopt, adapt, or must argue against"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 10 -> closes_before
         before "## ★ Findings, routed and not applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 10 -> the_text_removed
         before "## What an L1 detail specification could adopt, adapt, or must argue against\n\n- **Adopt — the three-onset frame (X, Y, Z) as the shape of a local cue.** A cu…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 10 -> characters_removed
         before 1056
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 11 -> heading
         before "## ★ Findings, routed and not applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 11 -> closes_before
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 11 -> the_text_removed
         before "## ★ Findings, routed and not applied\n\n**(1) The L1 charter's cadence-cue paragraph verifies at this primary, in three separate places.** The\ncharter says t…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 11 -> characters_removed
         before 2007
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 12 -> heading
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 12 -> closes_before
         before "## What this extract does NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 12 -> the_text_removed
         before "## Centrality\n\n**CENTRAL** — it is the primary under a chosen design point's recorded ground and under verification\ntarget V6. **A second independent extrac…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 12 -> characters_removed
         before 235
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 13 -> heading
         before "## What this extract does NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 13 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 13 -> the_text_removed
         before "## What this extract does NOT do\n\nIt derives no specification statement, amends no document, opens no code, touches no measurement tool,\ncorpus or golden, w…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> filters_applied -> 13 -> characters_removed
         before 660
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 1 -> characters
         before 7476
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> spans -> 0 -> lines_rendered
         before 280
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 0 -> the_text_removed
         before "> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under\n> `cowork_reading_pass_commission_2026_08_30.md` §4.\n>\n> **The grade.…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 0 -> characters_removed
         before 2383
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 1 -> the_text_removed
         before "**File:** `docs/research_papers/karystinaios_widmer_2022_arxiv_cadence_detection_gnn.pdf`."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 1 -> characters_removed
         before 90
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 2 -> the_text_removed
         before " — that is, row 37's."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 2 -> characters_removed
         before 21
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 3 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20 — a locator added: §3.1's text names the time signature; the key signature is\nin Figure 1's caption. Former wording, preserved (#12):…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 3 -> characters_removed
         before 268
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 4 -> the_text_removed
         before " The deliberate weakening of row 37's frame, and its stated purpose."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 4 -> characters_removed
         before 68
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 5 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20 — the page prints \"no assumptions on and reference to\" (p. 3). Former wording,\npreserved (#12): \"no assumptions and reference to\"…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 5 -> characters_removed
         before 157
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 6 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20 — the page prints \"three different levels, note-wise, onset-wise and beat-wise\npredictions\" (p. 4, §6.1). Former wording, preserved…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 6 -> characters_removed
         before 240
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 7 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20 — four bold marks, as read twice at page 5 at the size the file tool delivers:\nthe reference model's Bach PAC precision 0.89, the pre…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 7 -> characters_removed
         before 426
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 8 -> the_text_removed
         before " *(★ CORRECTED 2026-09-20 — the page prints \"in Bach\nfugues\" (p. 5). Former wording, preserved (#12): \"on Bach fugues\".)*"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 8 -> characters_removed
         before 121
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 9 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20 ON THE USER'S RULING. Former wording, preserved (#12): \"★ [FACT, §6.1] The\nindependent replication.\" — the page describes a differe…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 9 -> characters_removed
         before 221
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 10 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20 — the quotation had closed with a full stop mid-sentence. Former wording,\npreserved (#12): \"…emerging in the learning model.\"*\".)*…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 10 -> characters_removed
         before 155
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 11 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20 — two places in this paragraph. §6.2 works three examples, not one; and the\npage prints \"high-level musical considerations\" (p. 6).…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 11 -> characters_removed
         before 313
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 12 -> the_text_removed
         before ", which the L0 contract also gives, as a weak prior and never as a fact about the tonality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 12 -> characters_removed
         before 90
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 13 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20 — a negative given its bound: the page describes none of those steps, and does\nnot say it lacks them. Former wording, preserved (#12)…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 13 -> characters_removed
         before 231
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 14 -> the_text_removed
         before " *(★ CORRECTED 2026-09-20 — a negative given its bound. Former\nwording, preserved (#12): \"Nothing else: no chord, no key, no segmentation.\")*"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 14 -> characters_removed
         before 141
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 15 -> the_text_removed
         before "*(★ CORRECTED 2026-09-20 — two places: a claim wider than Table 2, and an unprinted gloss in the stated\nscope. Former wording, preserved (#12): \"Pre-training…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 15 -> characters_removed
         before 278
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 16 -> heading
         before "## What an L1 detail specification could adopt, adapt, or must argue against"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 16 -> closes_before
         before "## ★ Findings, routed and not applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 16 -> the_text_removed
         before "## What an L1 detail specification could adopt, adapt, or must argue against\n\n- **Adopt as evidence, not as machinery — the granularity result.** A cadence c…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 16 -> characters_removed
         before 1953
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 17 -> heading
         before "## ★ Findings, routed and not applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 17 -> closes_before
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 17 -> the_text_removed
         before "## ★ Findings, routed and not applied\n\n**(1) ★ THE FRAMEWORK'S \".29 AND .41\" PAIR IS VERIFIED, AND BOTH VALUES SIT IN THIS ONE TABLE.** The L1\ncharter car…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 17 -> characters_removed
         before 3731
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 18 -> heading
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 18 -> closes_before
         before "## What this extract does NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 18 -> the_text_removed
         before "## Centrality\n\n**CENTRAL** — the second primary under V6 and under DP-I's recorded ground. **A second independent\nextraction is owed** and has not been perf…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 18 -> characters_removed
         before 164
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 19 -> heading
         before "## What this extract does NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 19 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 19 -> the_text_removed
         before "## What this extract does NOT do\n\nIt derives no specification statement, amends no document, opens no code, touches no measurement tool,\ncorpus or golden, w…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> filters_applied -> 19 -> characters_removed
         before 664
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 2 -> characters
         before 9190
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> spans -> 0 -> lines_rendered
         before 279
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 0 -> the_text_removed
         before "> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under\n> `cowork_reading_pass_commission_2026_08_30.md` §4.\n>\n> **The grade.…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 0 -> characters_removed
         before 1648
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 1 -> the_text_removed
         before " *(★ CORRECTED 2026-10-15 at the\ncross-check. FORMER WORDING, PRESERVED (#12): \"*Journal of New Music Research* **47:1** (2018), pp. 29–52.\nPublished online…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 1 -> characters_removed
         before 447
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 2 -> the_text_removed
         before "**File:** `docs/research_papers/sears_pearce_caplin_mcadams_2018_jnmr_cadence_expectations.pdf`."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 2 -> characters_removed
         before 96
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 3 -> heading
         before "## ★ The doubt-default question, answered"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 3 -> closes_before
         before "## Claims, labeled"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 3 -> the_text_removed
         before "## ★ The doubt-default question, answered\n\n**Its method does NOT bear on L1's cues. It bears on perception, and — secondarily — on how a cadence\nground trut…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 3 -> characters_removed
         before 2577
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 4 -> the_text_removed
         before ", added 2026-10-15 at the cross-check"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 4 -> characters_removed
         before 37
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 5 -> heading
         before "## What an L1 detail specification could adopt, adapt, or must argue against"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 5 -> closes_before
         before "## ★ Findings, routed and not applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 5 -> the_text_removed
         before "## What an L1 detail specification could adopt, adapt, or must argue against\n\n**Nothing, and that is the finding.** The method needs a key L1 does not have, …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 5 -> characters_removed
         before 490
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 6 -> heading
         before "## ★ Findings, routed and not applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 6 -> closes_before
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 6 -> the_text_removed
         before "## ★ Findings, routed and not applied\n\n**(1) ★ A THIRD INDEPENDENT STATEMENT THAT THE HALF CADENCE IS NOT SEPARABLE BY LOCAL EVIDENCE — AND IT\nCOMES FROM A …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 6 -> characters_removed
         before 4490
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 7 -> heading
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 7 -> closes_before
         before "## What this extract does NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 7 -> the_text_removed
         before "## Centrality\n\n**NOT CENTRAL for L1** — no claim of this paper carries load in an L1 detail specification, which is the\ndoubt-default question answered abov…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 7 -> characters_removed
         before 650
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 8 -> heading
         before "## What this extract does NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 8 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 8 -> the_text_removed
         before "## What this extract does NOT do\n\nIt derives no specification statement, amends no document, opens no code, touches no measurement tool,\ncorpus or golden, w…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> filters_applied -> 8 -> characters_removed
         before 1017
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 3 -> characters
         before 9453
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> spans -> 0 -> lines_rendered
         before 634
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 0 -> the_text_removed
         before "> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT.** All 7 pages of the held PDF\n> `docs/research_papers/illescas_rizo_inesta_2007_icmc_harmonic_melodi…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 0 -> characters_removed
         before 3261
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 1 -> heading
         before "## 0. What this row is, taken from its own rows and not from any summary"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 1 -> closes_before
         before "## 1. Identity, established at the object"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 1 -> the_text_removed
         before "## 0. What this row is, taken from its own rows and not from any summary\n\n**`reading_pass/candidacy_upgrades.md`, line 96 (the row), read at the file:**\n\n>…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 1 -> characters_removed
         before 2912
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 2 -> heading
         before "## 1. Identity, established at the object"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 2 -> closes_before
         before "## 2. The input, the output and the repertoire, established at the pages"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 2 -> the_text_removed
         before "## 1. Identity, established at the object\n\n**What page 1 prints.** Title *\"HARMONIC, MELODIC, AND FUNCTIONAL AUTOMATIC ANALYSIS\"*; authors *Plácido\nR. Ill…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 2 -> characters_removed
         before 2099
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 3 -> heading
         before "## 2. The input, the output and the repertoire, established at the pages"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 3 -> closes_before
         before "## 3. What the paper actually does — stated in the paper's own structure"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 3 -> the_text_removed
         before "## 2. The input, the output and the repertoire, established at the pages\n\n**Input.** *\"polyphonic scores in symbolic format\"* (abstract, page 1); *\"transc…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 3 -> characters_removed
         before 1800
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 4 -> the_text_removed
         before " (not fetched, §9)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 4 -> characters_removed
         before 18
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 5 -> the_text_removed
         before ", row 7"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 5 -> characters_removed
         before 7
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 6 -> heading
         before "## 4. What the record's decision points take from this paper, and what they do not — answered at the object"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 6 -> closes_before
         before "## 5. What the paper reports, and what each figure is a figure OF — and the uncertainty practice"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 6 -> the_text_removed
         before "## 4. What the record's decision points take from this paper, and what they do not — answered at the object\n\n**No ratified text names this paper** (§6). So n…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 6 -> characters_removed
         before 7463
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 7 -> heading
         before "## 5. What the paper reports, and what each figure is a figure OF — and the uncertainty practice"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 7 -> closes_before
         before "## 6. Where the record bears on row 34 — established by sweep and by reading this sitting, not relayed"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 7 -> the_text_removed
         before "## 5. What the paper reports, and what each figure is a figure OF — and the uncertainty practice\n\n**The paper reports NO accuracy figure, no percentage, no c…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 7 -> characters_removed
         before 1725
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 8 -> heading
         before "## 6. Where the record bears on row 34 — established by sweep and by reading this sitting, not relayed"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 8 -> closes_before
         before "## 7. The findings, each with what it is a candidate for and what bounds it"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 8 -> the_text_removed
         before "## 6. Where the record bears on row 34 — established by sweep and by reading this sitting, not relayed\n\n**WHICH TERMS WERE RUN, AND HOW EACH WAS READ.** **Id…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 8 -> characters_removed
         before 5811
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 9 -> heading
         before "## 7. The findings, each with what it is a candidate for and what bounds it"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 9 -> closes_before
         before "## 8. The reference-list result, because it reaches held rows — with the traps"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 9 -> the_text_removed
         before "## 7. The findings, each with what it is a candidate for and what bounds it\n\n**(1) Row 34 is readable from here, and was read whole.** The record carried it …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 9 -> characters_removed
         before 4178
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 10 -> heading
         before "## 8. The reference-list result, because it reaches held rows — with the traps"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 10 -> closes_before
         before "## 9. What the paper does NOT claim, and what this read did NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 10 -> the_text_removed
         before "## 8. The reference-list result, because it reaches held rows — with the traps\n\n**Fourteen entries, derived at page 7 (all in the reference section, numbered…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 10 -> characters_removed
         before 2994
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 11 -> the_text_removed
         before ", and what this read did NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 11 -> characters_removed
         before 31
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 12 -> the_text_removed
         before "**This read did not** fetch the online results report, the rule set at the authors' URL, the Kern Scores\nsite or any cited work; open row 4's, 7's, 45's, 48's…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 12 -> characters_removed
         before 711
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 13 -> heading
         before "## 10. The verdict, on the candidacy criterion as the record states it"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 13 -> closes_before
         before "## 11. What the whole reading of this extract found — written in the act that ran it, after §0–§10 and before any landing"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 13 -> the_text_removed
         before "## 10. The verdict, on the candidacy criterion as the record states it\n\n**NOT CENTRAL.** No ratified text of the record names this paper, characterises it or…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 13 -> characters_removed
         before 1529
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 14 -> heading
         before "## 11. What the whole reading of this extract found — written in the act that ran it, after §0–§10 and before any landing"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 14 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 14 -> the_text_removed
         before "## 11. What the whole reading of this extract found — written in the act that ran it, after §0–§10 and before any landing\n\n**The reading.** This extract was …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> filters_applied -> 14 -> characters_removed
         before 6333
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 4 -> characters
         before 9731
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> spans -> 0 -> lines_rendered
         before 1035
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 0 -> the_text_removed
         before "> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-09-12).** Written under\n> `cowork_reading_pass_commission_2026_08_30.md` §4, whose form the rem…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 0 -> characters_removed
         before 9065
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 1 -> heading
         before "## Identity — a PREFIX title match BY CONSTRUCTION; the journal's own running head and pagination printed; ONE author, matching exactly; NO licence line printe…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 1 -> closes_before
         before "## What the paper is, in its own structure"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 1 -> the_text_removed
         before "## Identity — a PREFIX title match BY CONSTRUCTION; the journal's own running head and pagination printed; ONE author, matching exactly; NO licence line printe…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 1 -> characters_removed
         before 4642
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 2 -> the_text_removed
         before " *(★ CORRECTED 2026-09-19 at the second extract's cross-check, its\n§9.3 (a), under the standing rule of handoff entry 198 §7. FORMER WORDING, PRESERVED (#12):…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 2 -> characters_removed
         before 217
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 3 -> the_text_removed
         before " *(★ CORRECTED 2026-09-19 at the second extract's cross-check,\nits §9.3 (e), under the standing rule of handoff entry 198 §7. FORMER WORDING, PRESERVED (#12):…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 3 -> characters_removed
         before 417
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 4 -> the_text_removed
         before " *(★ CORRECTED 2026-09-19 ON THE USER'S\nRULING of that date — his words, \"I agree with recommendation A\" — the second extract's §9.4 (f) and\n§9.7. FORMER W…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 4 -> characters_removed
         before 350
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 5 -> the_text_removed
         before " *(★ CORRECTED 2026-09-19 at the second extract's cross-check, its\n§9.3 (b), under the standing rule of handoff entry 198 §7. FORMER WORDING, PRESERVED (#12):…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 5 -> characters_removed
         before 334
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 6 -> the_text_removed
         before " *(★ This sentence's first writing said the paper \"takes the second position operationally\";\nthe whole reading of this extract caught it. The paper declines…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 6 -> characters_removed
         before 238
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 7 -> the_text_removed
         before ", and it bears on a live grading convention"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 7 -> characters_removed
         before 43
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 8 -> the_text_removed
         before " *(★ REMARK ADDED 2026-09-19 at the second\nextract's cross-check, its §9.3 (d), under the standing rule of handoff entry 198 §7: the bold inside\nthis quotati…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 8 -> characters_removed
         before 877
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 9 -> the_text_removed
         before ", added by the whole reading of this\nextract"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 9 -> characters_removed
         before 44
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 10 -> the_text_removed
         before " *(★ REMARK ADDED 2026-09-19, the second extract's §9.3 (d):\nthe bold inside this quotation is this extract's emphasis, not the page's. No word is changed.)*\…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 10 -> characters_removed
         before 553
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 11 -> the_text_removed
         before " **That work is candidacy row 24, NOT ADMITTED, and\n`BIBLIOGRAPHY.md` line 38 records \"(no open copy found)\" — it is not held.** Under #1 and the\ntheory-gr…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 11 -> characters_removed
         before 409
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 12 -> the_text_removed
         before "*(★ REMARK\nADDED 2026-09-19, the second extract's §9.3 (d): the bold on \"Figure 5\" is this extract's emphasis, not\nthe page's. No word is changed.)*"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 12 -> characters_removed
         before 148
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 13 -> heading
         before "## ★ Two arithmetic residues, DERIVED here and with their cause NOT established"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 13 -> closes_before
         before "## ★ The placement question, DECIDED AT THE PAPER"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 13 -> the_text_removed
         before "## ★ Two arithmetic residues, DERIVED here and with their cause NOT established\n\nBoth were derived at the paper's own tables and stated figures; neither is a…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 13 -> characters_removed
         before 2951
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 14 -> heading
         before "## ★ The placement question, DECIDED AT THE PAPER"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 14 -> closes_before
         before "## Cross-primary check (mandatory item (j)) — NOTHING TO RUN ON, established; three false positives named; and one corpus-identity finding"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 14 -> the_text_removed
         before "## ★ The placement question, DECIDED AT THE PAPER\n\nThe slice-derivation row (line 79) places row 40 in **L2's slice with an L3 bearing**, and says in\nterms:…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 14 -> characters_removed
         before 3330
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 15 -> heading
         before "## Cross-primary check (mandatory item (j)) — NOTHING TO RUN ON, established; three false positives named; and one corpus-identity finding"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 15 -> closes_before
         before "## Reference-list check (mandatory item (i)) — a THIRD outcome shape, and it is named rather than generalised"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 15 -> the_text_removed
         before "## Cross-primary check (mandatory item (j)) — NOTHING TO RUN ON, established; three false positives named; and one corpus-identity finding\n\n**Run and establi…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 15 -> characters_removed
         before 3305
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 16 -> heading
         before "## Reference-list check (mandatory item (i)) — a THIRD outcome shape, and it is named rather than generalised"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 16 -> closes_before
         before "## Coupling facts (mandatory)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 16 -> the_text_removed
         before "## Reference-list check (mandatory item (i)) — a THIRD outcome shape, and it is named rather than generalised\n\n**Derived at the pages, not estimated.** The r…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 16 -> characters_removed
         before 4187
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 17 -> the_text_removed
         before " *(★ The first writing of this line read \"five or six\"; the whole reading counted the\n  columns at both tables and it is five in each.)*"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 17 -> characters_removed
         before 136
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 18 -> heading
         before "## What an L2 (or L3) detail specification could adopt, adapt, or must argue against"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 18 -> closes_before
         before "## ★ Findings, routed and NOT applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 18 -> the_text_removed
         before "## What an L2 (or L3) detail specification could adopt, adapt, or must argue against\n\n**What is NOT adoptable, said first because it bounds everything below …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 18 -> characters_removed
         before 4768
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 19 -> heading
         before "## ★ Findings, routed and NOT applied"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 19 -> closes_before
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 19 -> the_text_removed
         before "## ★ Findings, routed and NOT applied\n\n**Nothing in this section is applied, restated as settled, or built on. Each is put to the user with the\nground for t…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 19 -> characters_removed
         before 12503
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 20 -> heading
         before "## Centrality"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 20 -> closes_before
         before "## What this extract does NOT do"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 20 -> the_text_removed
         before "## Centrality\n\n**CENTRAL — on the commission's SECOND route only.**\n\n**The load-bearing-claim route is ABSENT, and that is established rather than assumed.…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 20 -> characters_removed
         before 4526
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 21 -> heading
         before "## ★ What the whole reading of this extract found — written AFTER the reading, not before it"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 21 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 21 -> the_text_removed
         before "## ★ What the whole reading of this extract found — written AFTER the reading, not before it\n\n**THE READING WAS RUN, IN ITS OWN ACT, AFTER THE REST OF THIS F…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> filters_applied -> 21 -> characters_removed
         before 8832
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 5 -> characters
         before 23972
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> spans -> 0 -> lines_rendered
         before 58
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 0 -> the_text_removed
         before "> **Establishment bound:** chapter-level structured read, 2026-08-30, three prompted extraction\n> calls over the open university deposit — NOT a page-by-page …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 0 -> characters_removed
         before 297
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 1 -> the_text_removed
         before " —\n  the same PAC/HC gap as V6's two verified primaries, at this thesis's own corpora."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 1 -> characters_removed
         before 86
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 2 -> heading
         before "## Bearing on the framework (first pass)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 2 -> closes_before
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 2 -> the_text_removed
         before "## Bearing on the framework (first pass)\n\n- **DP-B/DP-E adjacent, and worth carrying:** the thesis's key tracker uses cadential\n  anchoring INSIDE the key d…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 2 -> characters_removed
         before 1061
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 3 -> heading
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 3 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 3 -> the_text_removed
         before "## Verification targets touched\n\n- None of V1–V13 originates here (V6's figures live in the two published papers, both already\n  VERIFIED; the thesis's own …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> filters_applied -> 3 -> characters_removed
         before 184
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 6 -> characters
         before 2055
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> spans -> 0 -> lines_rendered
         before 307
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 0 -> the_text_removed
         before "> **STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (session 3 of the reading pass,\n> 2026-08-31).** Written under `cowork_reading_pass_commission_2026_0…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 0 -> characters_removed
         before 1150
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 1 -> the_text_removed
         before "**File as supplied:** `external resarch summary/Computational Music Theory and Its.pdf` —\n**not moved** (see the foot of this file)."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 1 -> characters_removed
         before 132
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 2 -> the_text_removed
         before " — the numbers row 19 exists to supply"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 2 -> characters_removed
         before 38
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 3 -> the_text_removed
         before ", WHICH IS THE ROW'S WHOLE YIELD"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 3 -> characters_removed
         before 32
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 4 -> heading
         before "## Bearing on the framework — flagged, not decided (verdicts belong to Task 4)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 4 -> closes_before
         before "## Bibliographic by-catch, routed here and written into no register"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 4 -> the_text_removed
         before "## Bearing on the framework — flagged, not decided (verdicts belong to Task 4)\n\n**Read against `FRAMEWORK.md` §9 (DP-O) and §11 (R-7), both read at the file …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 4 -> characters_removed
         before 3579
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 5 -> heading
         before "## Bibliographic by-catch, routed here and written into no register"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 5 -> closes_before
         before "## What this does and does not close"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 5 -> the_text_removed
         before "## Bibliographic by-catch, routed here and written into no register\n\n**The chapter's own reference [6] is the paper row 19 was flagged on**, and it disagrees…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 5 -> characters_removed
         before 1335
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 6 -> heading
         before "## What this does and does not close"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 6 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 6 -> the_text_removed
         before "## What this does and does not close\n\n**CLOSES:** the reading of row 19's subject at a primary of the line, **at the object, whole**, by the\nsame three auth…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> filters_applied -> 6 -> characters_removed
         before 2528
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 7 -> characters
         before 11826
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> spans -> 0 -> lines_rendered
         before 270
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 0 -> the_text_removed
         before "> **STATUS: FIRST-PASS EXTRACT, READ AT THE OBJECT (session 3 of the reading pass, 2026-08-31).**\n> Written under `cowork_reading_pass_commission_2026_08_30.m…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 0 -> characters_removed
         before 1023
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 1 -> the_text_removed
         before " — and the row is confirmed at the object, not inferred"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 1 -> characters_removed
         before 55
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 2 -> the_text_removed
         before "**Why eight searches missed it: it is a master's thesis**, indexed as a paper nowhere the pass's\nqueries could reach."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 2 -> characters_removed
         before 117
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 3 -> the_text_removed
         before "**★ AND IT IS A DISTINCT WORK FROM ROW 6, WHICH SETTLES THE OPEN QUESTION IN THE OPPOSITE DIRECTION\nFROM THE LEAD.** The pass's live lead was that row 7 might…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 3 -> characters_removed
         before 704
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 4 -> the_text_removed
         before " — **which is population row 8 of this\nsame pass** —"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 4 -> characters_removed
         before 52
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 5 -> the_text_removed
         before " *Declared and acted on, which is better practice than most\nof the population.*"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 5 -> characters_removed
         before 79
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 6 -> heading
         before "## Bearing — flagged for the user and for any later verdict, NOT decided here"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 6 -> closes_before
         before "## What this extract does NOT establish"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 6 -> the_text_removed
         before "## Bearing — flagged for the user and for any later verdict, NOT decided here\n\n- **★ The mode question** (routed by the disposition surface to the L2 detail …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 6 -> characters_removed
         before 2550
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 7 -> heading
         before "## What this extract does NOT establish"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 7 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 7 -> the_text_removed
         before "## What this extract does NOT establish\n\n- The contents of chapters 2, 3 and §§5.2–5.5, not read in detail.\n- The full experimental detail behind the 0.86 f…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> filters_applied -> 7 -> characters_removed
         before 922
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 8 -> characters
         before 12242
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> spans -> 0 -> lines_rendered
         before 57
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 0 -> the_text_removed
         before "> **Establishment bound:** read 2026-08-30 via two prompted extraction calls over the author's\n> open copy; the per-model per-textbook scores were relayed as …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 0 -> characters_removed
         before 231
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 1 -> heading
         before "## Bearing on the framework and the ruled measurement conventions (first pass)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 1 -> closes_before
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 1 -> the_text_removed
         before "## Bearing on the framework and the ruled measurement conventions (first pass)\n\n- **Measurement design (where the surface routes it):** this is the direct me…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 1 -> characters_removed
         before 939
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 2 -> heading
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 2 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 2 -> the_text_removed
         before "## Verification targets touched\n\n- None of V1–V13 originates here (the framework does not cite this paper's figures)."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> filters_applied -> 2 -> characters_removed
         before 117
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 9 -> characters
         before 2209
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> spans -> 0 -> lines_rendered
         before 91
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 0 -> the_text_removed
         before "> **Establishment bound on every claim below:** read 2026-08-30 via three prompted extraction\n> calls over the full text at the author's open copy (see the fe…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 0 -> characters_removed
         before 1196
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 1 -> the_text_removed
         before " —\n  i.e., exactly the L0 contract this project's framework gives (spelling, meter given)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 1 -> characters_removed
         before 89
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 2 -> the_text_removed
         before " — so nothing like the framework's DP-K rival stream crosses its output\n  boundary."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 2 -> characters_removed
         before 83
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 3 -> heading
         before "## Bearing on the framework (first-pass reading; verdicts belong to the findings surface)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 3 -> closes_before
         before "## Verification targets touched (population §3)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 3 -> the_text_removed
         before "## Bearing on the framework (first-pass reading; verdicts belong to the findings surface)\n\n- **DP-A (no division of the deciding by published field):** the C…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 3 -> characters_removed
         before 1449
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 4 -> heading
         before "## Verification targets touched (population §3)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 4 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 4 -> the_text_removed
         before "## Verification targets touched (population §3)\n\n- None of V1–V13's figures originates here (the framework predates this paper's entry into the\n  record and…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> filters_applied -> 4 -> characters_removed
         before 209
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 10 -> characters
         before 3420
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> spans -> 0 -> lines_rendered
         before 62
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 0 -> the_text_removed
         before "> **Establishment bound:** read 2026-08-30 via prompted extraction over the arXiv HTML full text\n> (method and limits in the fetched content record). Authors …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 0 -> characters_removed
         before 194
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 1 -> the_text_removed
         before " — a ground-truth-quality fact in\n  the direction of this project's principle #21."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 1 -> characters_removed
         before 82
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 2 -> the_text_removed
         before " Its L0 is therefore\n  POORER than this project's notated record — its design solves problems (enharmonic input) this\n  project's input does not have."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 2 -> characters_removed
         before 150
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 3 -> heading
         before "## Bearing on the framework (first pass)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 3 -> closes_before
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 3 -> the_text_removed
         before "## Bearing on the framework (first pass)\n\n- **DP-C (segmentation decided WITH):** BACHI is the disposition surface's promised comparable,\n  not a falsifier:…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 3 -> characters_removed
         before 1057
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 4 -> heading
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 4 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 4 -> the_text_removed
         before "## Verification targets touched\n\n- None of V1–V13 originates here."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> filters_applied -> 4 -> characters_removed
         before 66
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 11 -> characters
         before 2291
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> spans -> 0 -> lines_rendered
         before 59
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 0 -> the_text_removed
         before "> **Establishment bound:** read 2026-08-30 via two prompted extraction calls over the full text\n> at the author's open copy (method and limits in the fetched …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 0 -> characters_removed
         before 863
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 1 -> the_text_removed
         before " — the DP-N flashpoint evidence lives elsewhere (the meta-corpus paper)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 1 -> characters_removed
         before 71
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 2 -> heading
         before "## Bearing on the framework (first pass)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 2 -> closes_before
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 2 -> the_text_removed
         before "## Bearing on the framework (first pass)\n\n- **DP-L / §7 data design:** direct support for the disposition surface's reading — a candidate\n  reference for th…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 2 -> characters_removed
         before 570
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 3 -> heading
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 3 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 3 -> the_text_removed
         before "## Verification targets touched\n\n- None of V1–V13 originates here."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> filters_applied -> 3 -> characters_removed
         before 66
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 12 -> characters
         before 1977
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> spans -> 0 -> lines_rendered
         before 77
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 0 -> the_text_removed
         before "> **Establishment bound:** read 2026-08-30 via three prompted extraction calls over the full text\n> at the author's open copy (retrieval method and limits in …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 0 -> characters_removed
         before 929
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 1 -> heading
         before "## Bearing on the framework (first pass; verdicts belong to the findings surface)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 1 -> closes_before
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 1 -> the_text_removed
         before "## Bearing on the framework (first pass; verdicts belong to the findings surface)\n\n- **DP-D — the one rival-shaped item.** The disposition surface's defusing…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 1 -> characters_removed
         before 1232
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 2 -> heading
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 2 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 2 -> the_text_removed
         before "## Verification targets touched\n\n- None of V1–V13 originates here. No divergence to report."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> filters_applied -> 2 -> characters_removed
         before 91
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 13 -> characters
         before 3064
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> spans -> 0 -> lines_rendered
         before 62
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 0 -> the_text_removed
         before "> **Establishment bound:** read 2026-08-30 via one prompted extraction call over the author's\n> open copy (method and limits in the fetched content record). C…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 0 -> characters_removed
         before 795
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 1 -> heading
         before "## Bearing on the framework (first pass)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 1 -> closes_before
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 1 -> the_text_removed
         before "## Bearing on the framework (first pass)\n\n- **R-7 discharged for this alternative in substance: read, and it is NOT a rival\n  decomposition of the analysis …
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 1 -> characters_removed
         before 1077
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 2 -> heading
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 2 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 2 -> the_text_removed
         before "## Verification targets touched\n\n- None of V1–V13 originates here."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> filters_applied -> 2 -> characters_removed
         before 66
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 14 -> characters
         before 1893
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> spans -> 0 -> lines_rendered
         before 73
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 0 -> the_text_removed
         before "> **Establishment bound:** read 2026-08-30 via three prompted extraction calls over the full\n> text at the author's open copy (method and limits in the fetche…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 0 -> characters_removed
         before 867
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 1 -> heading
         before "## Bearing on the framework (first pass)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 1 -> closes_before
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 1 -> the_text_removed
         before "## Bearing on the framework (first pass)\n\n- **DP-O (hierarchy — open):** what the disposition surface promised is confirmed at the\n  primary: an executed gr…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 1 -> characters_removed
         before 1324
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 2 -> heading
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 2 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 2 -> the_text_removed
         before "## Verification targets touched\n\n- None of V1–V13 originates here."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> filters_applied -> 2 -> characters_removed
         before 66
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 15 -> characters
         before 2544
         after  null
         [a `parts` entry's characters removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> spans -> 0 -> lines_rendered
         before 42
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 0 -> the_text_removed
         before "> **Establishment bound:** read 2026-08-30 via one prompted extraction call over the open full\n> text (route in the fetched content record)."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 0 -> characters_removed
         before 140
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 1 -> heading
         before "## Bearing on the framework (first pass)"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 1 -> closes_before
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 1 -> the_text_removed
         before "## Bearing on the framework (first pass)\n\n- **DP-L / §7 data design — same direction, independent of the McLeod family:** a large\n  engineering effort arriv…
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 1 -> characters_removed
         before 784
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 2 -> heading
         before "## Verification targets touched"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 2 -> closes_before
         before "<the end of the text>"
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 2 -> the_text_removed
         before "## Verification targets touched\n\n- None of V1–V13 originates here."
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> filters_applied -> 2 -> characters_removed
         before 66
         after  null
         [a filter's measurement field removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 7 -> parts -> 16 -> characters
         before 1342
         after  null
         [a `parts` entry's characters removed]
ADDED    subjects -> l3 -> the_members_as_rendered -> 7 -> ★_where_this_record's_measures_COME_FROM
         before null
         after  "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at the frozen file itself and never at a re-render. The per-span, per-part and…
         [the added per-member field]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 8 -> parts -> 0 -> spans -> 0 -> lines_rendered
         before 675
         after  null
         [a span's lines_rendered removed]
REMOVED  subjects -> l3 -> the_members_as_rendered -> 8 -> parts -> 0 -> characters
         before 50962
         after  null
         [a `parts` entry's characters removed]
ADDED    subjects -> l3 -> the_members_as_rendered -> 8 -> ★_where_this_record's_measures_COME_FROM
         before null
         after  "`characters` is the length of this file AS THE PACK DIRECTORY HOLDS IT, measured at the frozen file itself and never at a re-render. The per-span, per-part and…
         [the added per-member field]
ADDED    subjects -> l3 -> ★_FROZEN
         before null
         after  {"★_this_subject_is_FROZEN_and_is_NOT_re-rendered": "Its deriving session has RUN, so this pack is the record of what that session was given rather than an inpu…
         [the added ★_FROZEN block]

differences: 464
    19  a `parts` entry's characters removed
   406  a filter's measurement field removed
     3  a member-level count removed
    25  a span's lines_rendered removed
     1  the added field under counted
     9  the added per-member field
     1  the added ★_FROZEN block

★_FROZEN fields: ['date', 'finding', 'reason', 'the_digest_form', 'the_digests', '★_so_read_the_member_records_below_with_this_in_mind', '★_the_former_wording_of_the_clause_above_PRESERVED_12', '★_this_subject_is_FROZEN_and_is_NOT_re-rendered']
★_FROZEN date: 2026-11-02
★_FROZEN digests: {"00_READ_THIS_FIRST.md": "b3f25abafea31719ee91fa26244636923496165b", "01_the_phase_definitions.md": "518b1e50d60af2b4e2ddcd8978623832eb071899", "02_the_guiding_principles_and_the_conventions.md": "51d1ad73a10f732fec10d792069ecc2833503d5e", "03_the_writing_standards.md": "a41983018cb27ed4a47d24ff8bb9e95181ed0572", "04_the_dispatch_protocol.md": "72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da", "05_the_ratified_design_intent.md": "fe04029239a93f3908d0a776d98108b22fb7484b", "06_the_defect_type_catalog.md": "1dec7621dc48d89242cacaf79b3048cd965d6a19", "07_the_charter_the_layers_and_the_decisions.md": "2ed8a5ca2b531f48519279941059fee259af03b7", "08_the_seventeen_research_extracts.md": "91c8af752315f991c2a681bd7b2b189c0f51dab8", "09_the_empirical_findings_ledger.md": "925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6"}

member characters unmoved: True [18713, 68743, 15048, 108389, 263863, 5910, 36208, 118166, 50963]
counted.files_in_the_pack unmoved: True 10
LEAKS_IN_THE_EXTRAS unmoved: True entries 3
counted.extras_lines_with_a_leak_hit unmoved: True 6

1(e) COMPARISON: AS PREDICTED
````

## A33. Task 1(f) — `gen_derivation_boot_pack.py --check`, after the freeze

````text
FROZEN SOURCES: 17 of 39 frozen pack file(s) would render at a different length from the sources as they stand today. NOT COMPARED; sets no exit code.
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
  l3: FROZEN — 10 file(s) at their recorded blobs
  scoring-model: FROZEN — 7 file(s) at their recorded blobs
````

## A34. Task 1(f) — the full guard capture after the freeze, whole

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

## A35. Task 1(f) — the capture compared with the opening capture (`cmp_captures.py`)

````text
before header: STALE vs the run: guard_state.json does not re-derive
before tally:  83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
after header:  STALE vs the run: guard_state.json does not re-derive
after tally:   83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
verdicts compared: 107; differing: 0
failing after: ['tools/audit/decisions/apply_residue_discard.py --check', 'tools/audit/decisions/apply_soft_discard.py --check', 'tools/audit/decisions/gen_cluster_dispositions.py --verify', 'tools/audit/decisions/gen_home_classification.py --check', 'tools/audit/decisions/gen_phase1p_delegation_bar.py --check', 'tools/audit/gen_artifact_inventory.py --check', 'tools/audit/gen_artifact_inventory_surface.py --check', 'tools/audit/gen_epoch_write_path.py --check', 'tools/audit/gen_filing_convention_application.py --check', 'tools/audit/gen_per_session_reading.py --check', 'tools/audit/gen_phase3_gate_partition.py --check', 'tools/audit/gen_recognizer_establishment_sort.py --check', 'tools/audit/gen_retirement_caller_check.py --check', 'tools/audit/gen_test_construction_evidence.py --check']
````

## A36. Task 1(g) — `changed_paths.py --staged`

````text
M	tools/audit/derivation_boot_pack.json
M	tools/audit/gen_derivation_boot_pack.py
2 changed path record(s) [staged]
````

## A37. Task 1(g) — `git show --stat` of the Task 1 commit

````text
commit 1bfa1a2bcf84cfe756e5a00a62c73dd28948d3a4
Author: Vincent Wong <65764495+slimvince@users.noreply.github.com>
Date:   Mon Nov 2 08:58:52 2026 +0100

    Freeze l3 in the derivation boot pack: its deriving session has run (Ruling 17(a), D-646), before Ruling 1 edits CLAUDE.md
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 tools/audit/derivation_boot_pack.json   | 845 ++++++++------------------------
 tools/audit/gen_derivation_boot_pack.py |  34 ++
 2 files changed, 244 insertions(+), 635 deletions(-)
````

## A38. Task 2, cited 1(a) — the capacity judgment file

````text
CAPACITY JUDGMENT BEFORE THIS BATCH'S TASK 2 (the cited Task 1, Ruling 1) — written after Task 1's
commit (the freeze, <T1> 1bfa1a2bcf), before any edit of CLAUDE.md or CLAUDE_ARCHIVE.md.

What Task 2 does. It replaces two bracketed former wordings in CLAUDE.md's decision-surface block with
dated pointers and appends both, verbatim, to CLAUDE_ARCHIVE.md; proves the move by a scratch
reconciliation with two planted faults; checks the edited tree (the split pair, the two historical
archive checks and their differing values, the population confinement check with class (c), a full
read-only guard capture compared with the capture after Task 1, the boot-pack check expected GREEN);
one commit. No step of any cited Task 2 (Ruling 3) runs: Ruling 3 is committed.

What the BEFORE captures of 0(g) took. Read size and defense share green (the precondition); the
register generator matches its data (20 files); the same six drifted anchors in the cluster
dispositions verify and the home-anchor report; both population checks and the legacy-mark check
green; the two historical archive checks FAIL, each with exactly its one differing value (artifact
True, rebuild False). Task 1's capture after the freeze is identical to the opening capture.

What the ordered reads took, by my own account. The largest were DECISIONS.md whole, the
dispatch-protocol section of cowork_audit_protocol.md (lines 180 to 1606), the first dispatch's text at
its lines 1 to 1022, the second dispatch whole, the third dispatch whole and the second report whole;
the protocol section and DECISIONS.md together took the most. The eight-line check replaced the
six-span read of CLAUDE.md. The reads the cited texts order only for Ruling 3's steps (the register
generator whole, the backbone header, DECISIONS_ARCHIVE.md whole, the split application's DECISIONS.md
entry, the legacy-mark check's ranges) were NOT performed, Ruling 3 being committed — declared.

Whether a summary of my context has fallen. No. No summary of this session's context has fallen at
the time of writing.

What the batch still owes after Task 2. The close (STATUS.md entries and the prefix move, the
forward-bound re-aim and --apply, the four archive checks, the regenerations under the population
confinement check, the two-file report and its appendix, the away-returns section, the close commit)
and the end state (a full guard run in write mode, the classification check, the end-state portion,
its commit).

Judgment. Task 2 is small and located; its edits and reconciliation are the same acts the second and
third runs made and proved (the new CLAUDE.md blob d8b285af… both times). I judge I can finish Task 2
whole and still close and reach the end state. The risk is context length, the reads having been
large; it is mitigated by keeping every printout in scratch files and quoting only what the report
needs.
````

## A39. Task 2, cited 1(b) and 1(c) — the record check and the end strings (`t2_1b_1c.py`)

````text
1(b) the sentence as read (line breaks as \n): '- **Carried for the next dispatch (not applied here):** amend `CLAUDE.md` Conventions, *How a decision surface\n  is written*, step 4, replacing the OPEN QUESTION clause with this ruling, former wording preserved in place\n  (#12).'
1(b) after the three differences: 'Carried for the next dispatch (not applied here): amend `CLAUDE.md` Conventions, *How a decision surface is written*, step 4, replacing the OPEN QUESTION clause with this ruling, former wording preserved in place (#12).'
1(b) RECORD CHECK PASS
1(c) P1 opening: found 1 time(s), at line 1890
1(c) P1 closing: found 1 time(s), at line 1894
1(c) P2 locator: found 1 time(s), at line 1925
1(c) P2 closing: found 1 time(s), at line 1928
````

## A40. Task 2, cited 1(e) — the archive's ending before and after the first append (`t2_archive_tail.py`)

````text
claude_archive_t1.md 12973 bytes; CR count 0 ; last 60 bytes: b'ngs\n  bind mechanically only if every session reads them"*\n\n'
claude_archive_new_probe.md 14877 bytes; CR count 0 ; last 60 bytes: b'ALLOCATED for the 2026-09-21 ruling or for this block**")*\n\n'
````

## A41. Task 2, cited 1(f) — the reconciliation on the real files

````text
assertion 1 PASS
assertion 2 PASS
P1: in new archive 1, in old archive 0, in new CLAUDE.md 0
P2: in new archive 1, in old archive 0, in new CLAUDE.md 0
assertion 3 PASS
SIZES (characters):
  old CLAUDE.md 169617; new CLAUDE.md 169182; difference -435
  P1 455; P2 309; pointer 1 165; pointer 2 164
  old CLAUDE_ARCHIVE.md 12881; new CLAUDE_ARCHIVE.md 14774; appended block 1893
TASK 1 RECONCILIATION PASS
````

## A42. Task 2, cited 1(f) — the two planted faults written (`t2_1f_plant.py`)

````text
F1 changed offset 16: 'S' -> 'X'
F2 changed archive offset 13696 : 'Q' -> 'q'
````

## A43. Task 2, cited 1(f) — planted fault F1

````text
assertion 1 PASS
FAIL: assertion 2: old CLAUDE.md with both replacements differs from the new
````

## A44. Task 2, cited 1(f) — planted fault F2

````text
assertion 1 PASS
assertion 2 PASS
P1: in new archive 0, in old archive 0, in new CLAUDE.md 0
FAIL: assertion 3: P1 counts
````

## A45. Task 2, cited 1(g) — `gen_governing_surface_split.py --check --pair CLAUDE.md`

````text
  CLAUDE.md / CLAUDE_ARCHIVE.md: moved 9 span(s), 6,540 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
````

## A46. Task 2, cited 1(g) — `gen_claude_md_finer_archive.py --check`

````text
FAIL: the finer archive record does not re-derive: tools\audit\claude_md_finer_archive.json
````

## A47. Task 2, cited 1(g) — `gen_claude_md_prune_backlog.py --check`

````text
FAIL: the prune-at-amendment backlog record does not re-derive: tools\audit\claude_md_prune_backlog.json
````

## A48. Task 2, cited 1(g) — the differing-values script, at the edited tree

````text
== gen_claude_md_finer_archive: 1 differing value(s) (artifact vs rebuild)
   reconciliation.every_span_the_ruling_REFUSED_is_still_present_at_site_exactly_once: artifact True | rebuild False
== gen_claude_md_prune_backlog: 1 differing value(s) (artifact vs rebuild)
   reconciliation.every_span_the_reading_flagged_is_still_present_at_site_exactly_once: artifact True | rebuild False
````

## A49. Task 2, cited 1(g) — `gen_l0_l1_outgoing_population.py --check` (before write mode)

````text
STALE vs the derivation: l0_l1_outgoing_population.json does not re-derive
````

## A50. Task 2, cited 1(g) — `gen_l3_outgoing_population.py --check` (before write mode)

````text
STALE vs the derivation: l3_outgoing_population.json does not re-derive
````

## A51. Task 2, cited 1(g) — L0/L1 write mode

````text
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
````

## A52. Task 2, cited 1(g) — L3 write mode

````text
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
````

## A53. Task 2, cited 1(g) — L0/L1 `--check` after write mode

````text
l0_l1_outgoing_population.json re-derives
````

## A54. Task 2, cited 1(g) — L3 `--check` after write mode

````text
l3_outgoing_population.json re-derives
````

## A55. Task 2, cited 1(g) — `git diff 3e654a59… d4a7a548…` (L0/L1, <T1> blob against regenerated), whole

````text
diff --git a/3e654a591d85b6c3c61ef15c02ffbcb0e71af99a b/d4a7a548785221b15d658f1f8eab5317b56c6398
index 3e654a591d..d4a7a54878 100644
--- a/3e654a591d85b6c3c61ef15c02ffbcb0e71af99a
+++ b/d4a7a548785221b15d658f1f8eab5317b56c6398
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

## A56. Task 2, cited 1(g) — `git diff 246b9ddd… b196fe6e…` (L3, <T1> blob against regenerated), whole

````text
diff --git a/246b9ddda9bdf5fef039e85c0ceb8170215d7736 b/b196fe6e8c6d19cdf48c7a9af3c0bca38570b137
index 246b9ddda9..b196fe6e8c 100644
--- a/246b9ddda9bdf5fef039e85c0ceb8170215d7736
+++ b/b196fe6e8c6d19cdf48c7a9af3c0bca38570b137
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
@@ -33022,7 +33022,7 @@
   "item_2_listed_not_compared_whole": [
    {
     "name": "CLAUDE.md",
-    "bytes": 170942,
+    "bytes": 170510,
     "inventory_class": "governing-documents",
     "in_the_residue": true,
     "the_statement": "named inside the six item-1 spans; LISTED and not compared whole under the named-documents derivation; the lines that name it are tabulated inside item 1"
@@ -36395,7 +36395,7 @@
   "item_2": {
    "distinct_names": 12,
    "distinct_names_that_resolve": 12,
-   "summed_bytes_of_the_distinct_names_that_resolve": 844831,
+   "summed_bytes_of_the_distinct_names_that_resolve": 844399,
    "distinct_names_that_are_specification_set_members": 4
   },
   "item_3": {
````

## A57. Task 2, cited 1(g) — the full guard capture at the edited tree, whole

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

## A58. Task 2, cited 1(g) — the capture compared with Task 1(f)'s capture (`cmp_captures.py`)

````text
before header: STALE vs the run: guard_state.json does not re-derive
before tally:  83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
after header:  STALE vs the run: guard_state.json does not re-derive
after tally:   83 guard(s) run, 16 failing, 4 not run, 20 historical record(s)
verdicts compared: 107; differing: 2
  tools/audit/gen_defense_share.py --check: PASS -> FAIL
  tools/audit/gen_session_start_read_size.py --check: PASS -> FAIL
failing after: ['tools/audit/decisions/apply_residue_discard.py --check', 'tools/audit/decisions/apply_soft_discard.py --check', 'tools/audit/decisions/gen_cluster_dispositions.py --verify', 'tools/audit/decisions/gen_home_classification.py --check', 'tools/audit/decisions/gen_phase1p_delegation_bar.py --check', 'tools/audit/gen_artifact_inventory.py --check', 'tools/audit/gen_artifact_inventory_surface.py --check', 'tools/audit/gen_defense_share.py --check', 'tools/audit/gen_epoch_write_path.py --check', 'tools/audit/gen_filing_convention_application.py --check', 'tools/audit/gen_per_session_reading.py --check', 'tools/audit/gen_phase3_gate_partition.py --check', 'tools/audit/gen_recognizer_establishment_sort.py --check', 'tools/audit/gen_retirement_caller_check.py --check', 'tools/audit/gen_session_start_read_size.py --check', 'tools/audit/gen_test_construction_evidence.py --check']
````

## A59. Task 2, cited 1(g) — `gen_derivation_boot_pack.py --check` at the edited tree

````text
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
````

## A60. Task 2, cited 1(i) — `changed_paths.py --staged`

````text
M	CLAUDE.md
M	CLAUDE_ARCHIVE.md
2 changed path record(s) [staged]
````

## A61. Task 3(b) — `gen_status_batch_bound.py --apply`

````text
wrote tools\audit\status_batch_bound.json
  entries moved: 3, 2,803 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
````

## A62. Task 3(b) — `gen_status_batch_bound.py --check`

````text
  entries moved: 3, 2,803 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
````

## A63. Task 3(b) — `gen_governing_surface_split.py --check --pair STATUS.md`

````text
  STATUS.md / STATUS_ARCHIVE.md: moved 131 span(s), 457,949 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
````

## A64. Task 3(b) — `gen_status_residue_move.py --check`

````text
  candidates: 17, moved 16, left at site by the reading 1
  characters moved: 46,105
  byte-present in the companion exactly once: True
  absent from the must-read:                  True
  every flagged entry still at site:          True
````

## A65. Task 3(b) — `gen_status_archive_pass.py --check`

````text
  dated entries moved: 52
  at the pass commit, the live file was exactly base-minus-range: True
  the moved block is verbatim in the archive at HEAD:             True
  the moved block is absent from the live file at HEAD:           True
````

## A66. Task 3(c) — `gen_evidence_pin_membership.py --check`

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

## A67. Task 3(c) — `gen_session_start_read_size.py --check` (before)

````text
STALE vs the measurement: session_start_read_size.json does not re-derive
````

## A68. Task 3(c) — `gen_defense_share.py --check` (before)

````text
STALE vs the measurement: defense_share.json does not re-derive
````

## A69. Task 3(c) — `gen_l0_l1_outgoing_population.py --check`

````text
l0_l1_outgoing_population.json re-derives
````

## A70. Task 3(c) — `gen_l3_outgoing_population.py --check` (before)

````text
STALE vs the derivation: l3_outgoing_population.json does not re-derive
````

## A71. Task 3(c) — `gen_derivation_boot_pack.py --check`

````text
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
````

## A72. Task 3(c) — `gen_session_start_read_size.py` (write mode)

````text
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
    STATUS.md                                                                 11919
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 237676
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 237676 [ruled membership]  (-129445, -35.26%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 237676 [ruled membership]  (-59156, -19.93%)  <- CROSSES A REGIME BOUNDARY
````

## A73. Task 3(c) — `gen_defense_share.py` (write mode)

````text
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
    of the whole session-start read (237676): 5.45%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
````

## A74. Task 3(c) — `gen_l3_outgoing_population.py` (write mode)

````text
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
````

## A75. Task 3(c) — read size `--check` after

````text
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
    STATUS.md                                                                 11919
    DECISIONS.md                                                             117490
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 237676
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 237676 [ruled membership]  (-129445, -35.26%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 237676 [ruled membership]  (-59156, -19.93%)  <- CROSSES A REGIME BOUNDARY
````

## A76. Task 3(c) — defense share `--check` after

````text
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
    of the whole session-start read (237676): 5.45%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
````

## A77. Task 3(c) — L3 `--check` after

````text
l3_outgoing_population.json re-derives
````

## A78. Task 3(c) — `gen_per_session_reading.py --check` (before)

````text
STALE vs the measurement: per_session_reading.json does not re-derive
````

## A79. Task 3(c) — `gen_per_session_reading.py` (write mode, LAST)

````text
wrote tools/audit/per_session_reading.json
  the ordinary session-start read (imported) 237676
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 675026
  Cowork, per sitting, in the shape of the sitting of entry 461: 973845
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
````

## A80. Task 3(c) — `gen_per_session_reading.py --check` after

````text
the per-session reading measurement re-derives
  the ordinary session-start read (imported) 237676
    CLAUDE.md, the whole file as the executing sessions report it injected   169182
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 675026
  Cowork, per sitting, in the shape of the sitting of entry 461: 973845
  six spans 105441 characters, 106 sub-blocks, archive-class 13834, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
````

## A81. Task 3(c) — the blobs against the start tip (`t3c_diffs.py`)

````text
tools/audit/l0_l1_outgoing_population.json: start tip 3e654a591d85b6c3c61ef15c02ffbcb0e71af99a -> now d4a7a548785221b15d658f1f8eab5317b56c6398 (moved)
  diff written to t3c_diff_l0_l1_outgoing_population.txt, 20 lines, 1 hunk(s)
tools/audit/l3_outgoing_population.json: start tip 246b9ddda9bdf5fef039e85c0ceb8170215d7736 -> now 8aac2cfc00123a2858e989cd8dfc99ac66b27a61 (moved)
  diff written to t3c_diff_l3_outgoing_population.txt, 58 lines, 6 hunk(s)
tools/audit/session_start_read_size.json: start tip 06759e7e4de5f7c5af9dcf7a481f81a5501809b2 -> now 5b4a34653d5459bbf08938bcdb7d81e8a90d251d (moved)
  diff written to t3c_diff_session_start_read_size.txt, 79 lines, 6 hunk(s)
tools/audit/defense_share.json: start tip fe1f38ae34793b0b8b71430eefcd75d3a00c63e0 -> now 15f650412fe3ad5176bbce82f6881ec55555e606 (moved)
  diff written to t3c_diff_defense_share.txt, 87 lines, 4 hunk(s)
tools/audit/per_session_reading.json: start tip 3305cac01da11b36483c02ab430c889a7284c25c -> now 7ecee4da295a8599eab97146bc8f85369e76f794 (moved)
  diff written to t3c_diff_per_session_reading.txt, 356 lines, 25 hunk(s)
````

## A82. Task 3(c) — diff of `l0_l1_outgoing_population.json` against the start tip, whole

````text
diff --git a/3e654a591d85b6c3c61ef15c02ffbcb0e71af99a b/d4a7a548785221b15d658f1f8eab5317b56c6398
index 3e654a591d..d4a7a54878 100644
--- a/3e654a591d85b6c3c61ef15c02ffbcb0e71af99a
+++ b/d4a7a548785221b15d658f1f8eab5317b56c6398
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

## A83. Task 3(c) — diff of `l3_outgoing_population.json` against the start tip, whole

````text
diff --git a/246b9ddda9bdf5fef039e85c0ceb8170215d7736 b/8aac2cfc00123a2858e989cd8dfc99ac66b27a61
index 246b9ddda9..8aac2cfc00 100644
--- a/246b9ddda9bdf5fef039e85c0ceb8170215d7736
+++ b/8aac2cfc00123a2858e989cd8dfc99ac66b27a61
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
@@ -20111,7 +20111,7 @@
      "the_statement": "hit, outside the specification document set, not dispositioned by this comparison; reachable by the mining map",
      "hit_records": [
       {
-       "line_number": 20,
+       "line_number": 22,
        "term": "phrase",
        "tier": "admitting",
        "line": "*★ ARCHIVED 2026-08-17, THE SECOND ACT — the dated entries that PREDATE (or paraphrase) the OI-222 pointer convention fell to `operative-rule-text` in the pinned measurement and stayed when the block above was cleared. They were READ one by one and moved verbatim to `STATUS_ARCHIVE.md` by `records/cc/instructions/cc_instruction_preparation_seventh.md` Task 1, under Ruling 3 of `records/cowork/rulings/cowork_rulings_2026_08_17_sixth_return.md`, which brings them under Ruling 4's own line. **One candidate did NOT move and is flagged:** the navigational paragraph at the foot of this file is not a completed batch's dated record but a live pointer to the archive and to the gate policy, so the read-before-move safeguard left it at site. The per-entry reconciliation is re-derived by `tools/audit/gen_status_residue_move.py --check`.*"
@@ -33022,7 +33022,7 @@
   "item_2_listed_not_compared_whole": [
    {
     "name": "CLAUDE.md",
-    "bytes": 170942,
+    "bytes": 170510,
     "inventory_class": "governing-documents",
     "in_the_residue": true,
     "the_statement": "named inside the six item-1 spans; LISTED and not compared whole under the named-documents derivation; the lines that name it are tabulated inside item 1"
@@ -36395,7 +36395,7 @@
   "item_2": {
    "distinct_names": 12,
    "distinct_names_that_resolve": 12,
-   "summed_bytes_of_the_distinct_names_that_resolve": 844831,
+   "summed_bytes_of_the_distinct_names_that_resolve": 844399,
    "distinct_names_that_are_specification_set_members": 4
   },
   "item_3": {
````

## A84. Task 3(c) — diff of `session_start_read_size.json` against the start tip, whole

````text
diff --git a/06759e7e4de5f7c5af9dcf7a481f81a5501809b2 b/5b4a34653d5459bbf08938bcdb7d81e8a90d251d
index 06759e7e4d..5b4a34653d 100644
--- a/06759e7e4de5f7c5af9dcf7a481f81a5501809b2
+++ b/5b4a34653d5459bbf08938bcdb7d81e8a90d251d
@@ -40,7 +40,7 @@
    "regime": "ruled membership",
    "why_this_regime": "this `CLAUDE.md` carries the membership block, so the read is the six spans it names at session start and nothing else of the file",
    "the_clause_that_makes_it_a_member": "★ AND THIS IS WHAT A SESSION READS OF `CLAUDE.md` ITSELF — SIX SPANS AT SESSION START, EIGHT READ ONLY WHEN THE SESSION'S WORK TOUCHES THEM (user-ruled 2026-09-07).",
-   "characters": 105876,
+   "characters": 105441,
    "the_session_start_spans": [
     {
      "name": "Guiding principles",
@@ -75,8 +75,8 @@
      "name": "Conventions",
      "kind": "session start",
      "located_by": "the heading “## Conventions”",
-     "characters": 41071,
-     "lines": 452
+     "characters": 40636,
+     "lines": 448
     },
     {
      "name": "The self-check after every coding exercise",
@@ -160,8 +160,8 @@
    "why_the_conditional_spans_are_not_summed_in": "each is read by the sessions its own condition names and not by an ordinary one, which is what CONDITIONAL means. Counting them would report a read no ordinary session takes — the same error this tool already refuses for `BUILD_AND_TEST.md`.",
    "★_the_overstatement_this_repair_removes": {
     "what_it_is": "until 2026-09-07 this tool measured `len(CLAUDE.md)` as an ordinary session's read of that file. Both values are measured HERE, at the same tree, so the difference is the overstatement itself and not an estimate.",
-    "the_former_measurement_the_whole_file": 169617,
-    "the_repaired_measurement_the_six_session_start_spans": 105876,
+    "the_former_measurement_the_whole_file": 169182,
+    "the_repaired_measurement_the_six_session_start_spans": 105441,
     "characters_the_former_measurement_overstated_by": 63741
    },
    "★_the_reconciliation_against_the_block_itself_run_on_every_run": {
@@ -175,12 +175,12 @@
    }
   },
   "characters_per_member": {
-   "CLAUDE.md": 105876,
-   "STATUS.md": 12082,
+   "CLAUDE.md": 105441,
+   "STATUS.md": 11919,
    "DECISIONS.md": 117490,
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
   },
-  "total_characters": 238274,
+  "total_characters": 237676,
   "further_spans_of_the_same_artifact_NOT_counted_into_the_read": {
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows": {
     "characters": 62498,
@@ -276,10 +276,10 @@
    "from_commit": "1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
    "from_total": 367121,
    "from_regime": "whole-file practice",
-   "to_total": 238274,
+   "to_total": 237676,
    "to_regime": "ruled membership",
-   "change_in_characters": -128847,
-   "change_percent": -35.1,
+   "change_in_characters": -129445,
+   "change_percent": -35.26,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   },
@@ -287,10 +287,10 @@
    "from_commit": "594074e1e1900079e449d2b79a38920d21bca6e6",
    "from_total": 296832,
    "from_regime": "whole-file practice",
-   "to_total": 238274,
+   "to_total": 237676,
    "to_regime": "ruled membership",
-   "change_in_characters": -58558,
-   "change_percent": -19.73,
+   "change_in_characters": -59156,
+   "change_percent": -19.93,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   }
````

## A85. Task 3(c) — diff of `defense_share.json` against the start tip, whole

````text
diff --git a/fe1f38ae34793b0b8b71430eefcd75d3a00c63e0 b/15f650412fe3ad5176bbce82f6881ec55555e606
index fe1f38ae34..15f650412f 100644
--- a/fe1f38ae34793b0b8b71430eefcd75d3a00c63e0
+++ b/15f650412fe3ad5176bbce82f6881ec55555e606
@@ -76,8 +76,8 @@
   }
  ],
  "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
-  "the_six_session_start_spans": 105876,
-  "the_whole_ordinary_session_start_read": 238274,
+  "the_six_session_start_spans": 105441,
+  "the_whole_ordinary_session_start_read": 237676,
   "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked defense; the second says how much of the WHOLE boot it is. A share quoted against one of them is not the share against the other."
  },
  "per_span": [
@@ -119,12 +119,12 @@
   },
   {
    "name": "Conventions",
-   "characters": 41071,
+   "characters": 40636,
    "marked_clauses": 10,
    "characters_those_clauses_hold": 3472,
    "characters_had_every_clause_been_closed_at_the_next_marked_clause": 22081,
    "characters_had_every_clause_run_to_its_paragraph_end": 33971,
-   "share_of_this_span": 8.45
+   "share_of_this_span": 8.54
   },
   {
    "name": "The self-check after every coding exercise",
@@ -141,8 +141,8 @@
   "characters_those_clauses_hold": 12957,
   "characters_had_every_clause_been_closed_at_the_next_marked_clause": 51684,
   "characters_had_every_clause_run_to_its_paragraph_end": 160906,
-  "share_of_the_six_session_start_spans": 12.24,
-  "share_of_the_whole_ordinary_session_start_read": 5.44
+  "share_of_the_six_session_start_spans": 12.29,
+  "share_of_the_whole_ordinary_session_start_read": 5.45
  },
  "every_clause_published_so_the_tables_reach_is_inspectable_rather_than_asserted": [
   {
@@ -552,39 +552,39 @@
    "the_span_it_stands_in": "Conventions",
    "the_marker_row_it_matched": "Why followed by a space, a colon or a comma",
    "emphasis": "italic",
-   "first_line": 1939,
+   "first_line": 1935,
    "the_marked_run_as_written": "Why:",
    "characters_had_it_been_closed_at_the_next_marked_clause": 2901,
    "it_would_have_been_closed_at_the_next_marked_clause": false,
    "characters_had_it_run_to_its_paragraph_end": 2901,
    "the_authored_end_anchor": "erroring loudly rather than returning silently-wrong content.",
-   "the_line_the_anchor_ends_on": 1942,
+   "the_line_the_anchor_ends_on": 1938,
    "characters": 319
   },
   {
    "the_span_it_stands_in": "Conventions",
    "the_marker_row_it_matched": "Why followed by a space, a colon or a comma",
    "emphasis": "italic",
-   "first_line": 1977,
+   "first_line": 1973,
    "the_marked_run_as_written": "Why:",
    "characters_had_it_been_closed_at_the_next_marked_clause": 318,
    "it_would_have_been_closed_at_the_next_marked_clause": false,
    "characters_had_it_run_to_its_paragraph_end": 318,
    "the_authored_end_anchor": "and it operationalizes principle #5 (investigate when facts may be scarce).",
-   "the_line_the_anchor_ends_on": 1980,
+   "the_line_the_anchor_ends_on": 1976,
    "characters": 318
   },
   {
    "the_span_it_stands_in": "Conventions",
    "the_marker_row_it_matched": "Evidence followed by a colon",
    "emphasis": "italic",
-   "first_line": 1986,
+   "first_line": 1982,
    "the_marked_run_as_written": "Evidence:",
    "characters_had_it_been_closed_at_the_next_marked_clause": 153,
    "it_would_have_been_closed_at_the_next_marked_clause": false,
    "characters_had_it_run_to_its_paragraph_end": 153,
    "the_authored_end_anchor": "the fifty-ninth performed it and counted one.",
-   "the_line_the_anchor_ends_on": 1987,
+   "the_line_the_anchor_ends_on": 1983,
    "characters": 153
   }
  ],
````

## A86. Task 3(c) — diff of `per_session_reading.json` against the start tip, whole

````text
diff --git a/3305cac01da11b36483c02ab430c889a7284c25c b/7ecee4da295a8599eab97146bc8f85369e76f794
index 3305cac01d..7ecee4da29 100644
--- a/3305cac01da11b36483c02ab430c889a7284c25c
+++ b/7ecee4da295a8599eab97146bc8f85369e76f794
@@ -14,15 +14,15 @@
   "the_ordinary_session_start_read_imported": {
    "its_one_home": "`tools/audit/session_start_read_size.json`, written by `tools/audit/gen_session_start_read_size.py`; what stands here is that tool's own `measure` called at the tree, and its total is checked against that artifact on every run",
    "characters_per_member": {
-    "CLAUDE.md": 105876,
-    "STATUS.md": 12082,
+    "CLAUDE.md": 105441,
+    "STATUS.md": 11919,
     "DECISIONS.md": 117490,
     "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
    },
-   "total_characters": 238274,
+   "total_characters": 237676,
    "the_reading_of_claude_md": {
     "regime": "ruled membership",
-    "characters": 105876
+    "characters": 105441
    }
   },
   "the_further_members": [
@@ -34,8 +34,8 @@
     "read_by": "Claude Code, per batch — DECLARED by the executing sessions in their reports, not established by this tool (#18)",
     "the_mandate_class": "unwritten practice",
     "the_record_that_mandates_it": "no clause of `CLAUDE.md` names the injection; the dispatches' clause \"injected context does not stand in for this read\" carries no stated ground in the record (entry 461 §2, item (a)); the membership block's own provenance paragraph records that until 2026-09-07 the whole-file read was PRACTICE mandated by no clause",
-    "characters": 169617,
-    "characters_the_six_spans_read_with_the_file_tool_add_on_top_of_it": 105876,
+    "characters": 169182,
+    "characters_the_six_spans_read_with_the_file_tool_add_on_top_of_it": 105441,
     "characters_of_the_file_outside_the_six_spans": 63741
    },
    {
@@ -782,28 +782,28 @@
      "the_writing_sides_read": "unwritten practice"
     },
     "the_record_that_mandates_it": "the standing clause `Every dispatch's read-first block names the CURRENT HANDOVER BLOCK`, which this repository carries as numbered entry files; the writing side's three is its own practice",
-    "the_population_count": 391,
+    "the_population_count": 395,
     "the_three": [
      {
-      "name": "cowork_handoff_entry_four_hundred_and_sixty_seven.md",
-      "added_in_commit": "f2d0ae14ba2037ba4111c12c52d314b463d77741",
-      "added_at_unix_time": 1793563784,
-      "characters": 7559
+      "name": "cowork_handoff_entry_four_hundred_and_seventy_four.md",
+      "added_in_commit": "bfd15c7fdd6e010a2ad163cfb0dddd26e46239a1",
+      "added_at_unix_time": 1793605025,
+      "characters": 8835
      },
      {
-      "name": "cowork_handoff_entry_four_hundred_and_seventy.md",
-      "added_in_commit": "749ab8c88a7e5221c73fcdc7d96a040c7fb3580b",
-      "added_at_unix_time": 1793567013,
-      "characters": 7952
+      "name": "cowork_handoff_entry_four_hundred_and_seventy_three.md",
+      "added_in_commit": "bfd15c7fdd6e010a2ad163cfb0dddd26e46239a1",
+      "added_at_unix_time": 1793605025,
+      "characters": 7122
      },
      {
-      "name": "cowork_handoff_entry_four_hundred_and_seventy_one.md",
-      "added_in_commit": "749ab8c88a7e5221c73fcdc7d96a040c7fb3580b",
-      "added_at_unix_time": 1793567013,
-      "characters": 6218
+      "name": "cowork_handoff_entry_four_hundred_and_seventy_two.md",
+      "added_in_commit": "bfd15c7fdd6e010a2ad163cfb0dddd26e46239a1",
+      "added_at_unix_time": 1793605025,
+      "characters": 7261
      }
     ],
-    "characters": 21729
+    "characters": 23218
    }
   ],
   "totals_by_side": {
@@ -811,7 +811,7 @@
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 238274
+      "characters": 237676
      },
      {
       "member": "BUILD_AND_TEST.md",
@@ -831,19 +831,19 @@
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 21729
+      "characters": 23218
      }
     ],
-    "without_the_injected_copy_of_CLAUDE_md": 674135,
-    "with_it": 843752,
-    "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, 169617 characters",
+    "without_the_injected_copy_of_CLAUDE_md": 675026,
+    "with_it": 844208,
+    "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, 169182 characters",
     "left_out_and_said_so": "the previous report at the portions a dispatch orders, the reading file at its ordered portions, the ruling records a dispatch orders — varies per dispatch and is not sized here"
    },
    "Cowork, per sitting, in the shape of the sitting of entry 461": {
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 238274
+      "characters": 237676
      },
      {
       "member": "entry 118, the bridge-fault section",
@@ -863,7 +863,7 @@
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 21729
+      "characters": 23218
      },
      {
       "member": "the latest report of the arc, whole: cc_report_l3_comparison_tabulation_thirtieth_2026_10_31.md",
@@ -874,7 +874,7 @@
       "characters": 151805
      }
     ],
-    "characters": 972954,
+    "characters": 973845,
     "left_out_and_said_so": "the verification reads at the objects (the reading file at its sections, the guard state, the ref files, the away-returns close) — varies per batch and is not sized here"
    }
   }
@@ -2578,14 +2578,14 @@
    },
    {
     "name": "Conventions",
-    "characters": 41071,
-    "characters_given_to_the_finer_cut": 41072,
+    "characters": 40636,
+    "characters_given_to_the_finer_cut": 40637,
     "characters_of_the_blank_lines_between_sub_blocks": 11,
     "sub_block_count": 20,
     "by_kind": {
      "block": {
       "sub_blocks": 12,
-      "characters": 23065
+      "characters": 22630
      },
      "star-marked sub-block": {
       "sub_blocks": 8,
@@ -2599,7 +2599,7 @@
      },
      "preserved-former-wording": {
       "sub_blocks": 2,
-      "characters": 9411
+      "characters": 8976
      }
     },
     "by_shape_element": {
@@ -2609,7 +2609,7 @@
      },
      "former_wording_marker": {
       "sub_blocks": 2,
-      "characters": 9411
+      "characters": 8976
      }
     },
     "star_marked_sub_blocks": {
@@ -2620,7 +2620,7 @@
      "sub_blocks": 16,
      "characters": 32362
     },
-    "archive_class_characters": 9411,
+    "archive_class_characters": 8976,
     "doubt_defaulted_characters": 31635,
     "settled_sub_blocks": {
      "sub_blocks": 3,
@@ -2911,26 +2911,26 @@
      {
       "kind": "block",
       "first_line_at_the_tree": 1850,
-      "last_line_at_the_tree": 1928,
-      "characters_with_line_endings": 7422,
+      "last_line_at_the_tree": 1924,
+      "characters_with_line_endings": 6987,
       "the_class": "preserved-former-wording",
       "the_doubt_default_decided_it": false,
       "the_classifiers_evidence": {
-       "the_marker_matched": "former wording",
-       "the_quotation_that_places_it": "\"**and how far that reaches is an OPEN\n     QUESTION the user has not answered**: read at its widest it could be taken a"
+       "the_marker_matched": "Former wording",
+       "the_quotation_that_places_it": "\"I cannot think of any example of decision\n     surface that should exclude a recommendation.\""
       },
       "the_amendment_record_shape": [
        "former_wording_marker"
       ],
       "carries_a_ruled_date_header": false,
-      "text_sha256": "2bc9ce24537b488524686250b38722da6ef1484e28b799a74026d7aa89869b32",
+      "text_sha256": "957f6b5039c181f8ead45794414427f259cecc9b22fab12b64ffd01595aaefaf",
       "the_opening": "- **HOW A DECISION SURFACE IS WRITTEN, AND IN WHAT ORDER ITS RULES APPLY (consolidated here on the\n  user's direction, 2026-09-21; each part keeps its own home ",
       "settled_at_an_earlier_sitting": []
      },
      {
       "kind": "block",
-      "first_line_at_the_tree": 1930,
-      "last_line_at_the_tree": 1948,
+      "first_line_at_the_tree": 1926,
+      "last_line_at_the_tree": 1944,
       "characters_with_line_endings": 1867,
       "the_class": "operative-rule-text",
       "the_doubt_default_decided_it": true,
@@ -2947,8 +2947,8 @@
      },
      {
       "kind": "star-marked sub-block",
-      "first_line_at_the_tree": 1949,
-      "last_line_at_the_tree": 1971,
+      "first_line_at_the_tree": 1945,
+      "last_line_at_the_tree": 1967,
       "characters_with_line_endings": 1989,
       "the_class": "preserved-former-wording",
       "the_doubt_default_decided_it": false,
@@ -2974,8 +2974,8 @@
      },
      {
       "kind": "block",
-      "first_line_at_the_tree": 1973,
-      "last_line_at_the_tree": 1980,
+      "first_line_at_the_tree": 1969,
+      "last_line_at_the_tree": 1976,
       "characters_with_line_endings": 810,
       "the_class": "operative-rule-text",
       "the_doubt_default_decided_it": true,
@@ -2992,8 +2992,8 @@
      },
      {
       "kind": "block",
-      "first_line_at_the_tree": 1982,
-      "last_line_at_the_tree": 1987,
+      "first_line_at_the_tree": 1978,
+      "last_line_at_the_tree": 1983,
       "characters_with_line_endings": 599,
       "the_class": "operative-rule-text",
       "the_doubt_default_decided_it": true,
@@ -3049,8 +3049,8 @@
     "sub_blocks": [
      {
       "kind": "block",
-      "first_line_at_the_tree": 1989,
-      "last_line_at_the_tree": 1989,
+      "first_line_at_the_tree": 1985,
+      "last_line_at_the_tree": 1985,
       "characters_with_line_endings": 74,
       "the_class": "operative-rule-text",
       "the_doubt_default_decided_it": false,
@@ -3068,8 +3068,8 @@
      },
      {
       "kind": "block",
-      "first_line_at_the_tree": 1991,
-      "last_line_at_the_tree": 1998,
+      "first_line_at_the_tree": 1987,
+      "last_line_at_the_tree": 1994,
       "characters_with_line_endings": 685,
       "the_class": "operative-rule-text",
       "the_doubt_default_decided_it": true,
@@ -3086,15 +3086,15 @@
    }
   ],
   "totals": {
-   "characters_of_the_six_spans": 105876,
-   "characters_given_to_the_finer_cut": 105882,
+   "characters_of_the_six_spans": 105441,
+   "characters_given_to_the_finer_cut": 105447,
    "characters_of_the_blank_lines_between_sub_blocks": 49,
    "sub_block_count": 106,
    "how_the_two_counts_relate": "each span is given to the finer cut as its lines joined by newlines with one closing newline added, so the characters given exceed the six spans' own count by one per span",
    "by_kind": {
     "block": {
      "sub_blocks": 44,
-     "characters": 55420
+     "characters": 54985
     },
     "numbered-principle sub-block": {
      "sub_blocks": 24,
@@ -3116,7 +3116,7 @@
     },
     "preserved-former-wording": {
      "sub_blocks": 3,
-     "characters": 11316
+     "characters": 10881
     },
     "defense-and-declined-alternatives": {
      "sub_blocks": 1,
@@ -3142,7 +3142,7 @@
     },
     "former_wording_marker": {
      "sub_blocks": 4,
-     "characters": 26826
+     "characters": 26391
     },
     "accepted_costs_paragraph": {
      "sub_blocks": 1,
@@ -3161,7 +3161,7 @@
     "sub_blocks": 39,
     "characters": 56976
    },
-   "archive_class_characters": 14269,
+   "archive_class_characters": 13834,
    "doubt_defaulted_characters": 90909,
    "settled_sub_blocks": {
     "sub_blocks": 6,
@@ -3227,7 +3227,7 @@
      "the_opening": "**★ THE RULE COVERS EVERY READ MECHANISM AND EVERY DIALECT (recorded 2026-08-08 on the user's direction, at the third measured instance family).** The restricti",
      "found_at_the_tree": "by hash — the sub-block stands unchanged",
      "the_sub_blocks_it_matched_first_line_at_the_tree": [
-      1949
+      1945
      ]
     },
     {
@@ -3259,8 +3259,8 @@
     "characters_those_clauses_hold": 12957,
     "characters_had_every_clause_been_closed_at_the_next_marked_clause": 51684,
     "characters_had_every_clause_run_to_its_paragraph_end": 160906,
-    "share_of_the_six_session_start_spans": 12.24,
-    "share_of_the_whole_ordinary_session_start_read": 5.44
+    "share_of_the_six_session_start_spans": 12.29,
+    "share_of_the_whole_ordinary_session_start_read": 5.45
    },
    "per_span": [
     {
@@ -3301,12 +3301,12 @@
     },
     {
      "name": "Conventions",
-     "characters": 41071,
+     "characters": 40636,
      "marked_clauses": 10,
      "characters_those_clauses_hold": 3472,
      "characters_had_every_clause_been_closed_at_the_next_marked_clause": 22081,
      "characters_had_every_clause_run_to_its_paragraph_end": 33971,
-     "share_of_this_span": 8.45
+     "share_of_this_span": 8.54
     },
     {
      "name": "The self-check after every coding exercise",
@@ -3319,8 +3319,8 @@
     }
    ],
    "the_two_denominators": {
-    "the_six_session_start_spans": 105876,
-    "the_whole_ordinary_session_start_read": 238274
+    "the_six_session_start_spans": 105441,
+    "the_whole_ordinary_session_start_read": 237676
    },
    "how_these_relate_to_the_sums_above": "a marked clause lies INSIDE a sub-block, so these values overlap table 2's sums and are never added to them"
   }
````

## A87. Task 3(c) — the field names on the changed lines of that diff (`t3c_keys.py`)

````text
   1  (no field name: 1945)
   1  (no field name: 1949)
   2  CLAUDE.md
   2  STATUS.md
   6  added_at_unix_time
   6  added_in_commit
   4  archive_class_characters
  38  characters
   4  characters_given_to_the_finer_cut
   2  characters_of_the_six_spans
   2  characters_the_six_spans_read_with_the_file_tool_add_on_top_of_it
   2  characters_with_line_endings
  12  first_line_at_the_tree
  14  last_line_at_the_tree
   6  name
   2  share_of_the_six_session_start_spans
   2  share_of_the_whole_ordinary_session_start_read
   2  share_of_this_span
   2  text_sha256
   2  the_injected_copy_added_in_with_it
   2  the_marker_matched
   2  the_population_count
   2  the_quotation_that_places_it
   2  the_six_session_start_spans
   2  the_whole_ordinary_session_start_read
   2  total_characters
   2  with_it
   2  without_the_injected_copy_of_CLAUDE_md
````
