# Appendix — the raw printouts of `cc_report_pruning_rulings_execution_2026_11_01.md`

> The printouts this batch's commands and scratch scripts produced, VERBATIM, each under a heading naming the
> command and the step it served (Ruling 4 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`).
> Every verdict, count and difference stands in the report proper; this file is read where a verification needs a
> particular printout. Assembled mechanically from the scratch output files by `build_appendix.py`, so nothing in it
> was retyped.

## 0(c) — A1's enumeration: `python tools/audit/changed_paths.py`

```
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_pruning_rulings_execution_2026_11_01.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_five.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_four.md
??	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_six.md
??	records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md
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
```

## 0(c) — `git ls-files --others --exclude-standard -- <path>` per landing path (a loop over named paths)

```
== records/cc/instructions/cc_instruction_pruning_rulings_execution_2026_11_01.md
records/cc/instructions/cc_instruction_pruning_rulings_execution_2026_11_01.md
exit:0
== records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md
records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_four.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_four.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_five.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_five.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_six.md
records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_six.md
exit:0
```

## 0(c) — `git diff --stat a18148e529cd9f50aeb831cb531bf8813a472eb4 -- <path>` per named path (a loop over named paths)

```
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
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_forty_eight.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_forty_nine.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty_one.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty_two.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty_three.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty_four.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty_five.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty_six.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty_seven.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty_eight.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_fifty_nine.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_one.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_two.md
exit:0
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_three.md
exit:0
```

## 0(d) — the last-bytes check over the five landing blobs (scratch script `lastbytes.py`)

```
b_dispatch.bin: size 102666 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b'h is handed to Claude Code by the user, with the longer opening line.\n'
b_record.bin: size 28805 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b'file tools; no shell command ran, in the container or on the\ndevice.*\n'
b_e464.bin: size 17607 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b' written from that point should not need pruning. Still 2nd\nfor f.".*\n'
b_e465.bin: size 10793 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b'sume" (after switching the model); "continue"; "A"; "A"; "continue".*\n'
b_e466.bin: size 6295 bytes; zero bytes 0; ends with newline True
  last 70 bytes: b'on entry 465. The user\'s words: the opening instruction;\n"continue".*\n'
```

## 0(e) — `python tools/audit/gen_evidence_pin_membership.py --check` (before)

```
STALE vs the derivation: evidence_pin_membership.json does not re-derive
```

## 0(e) — `python tools/audit/gen_evidence_pin_membership.py` (write mode)

```
wrote tools/audit/evidence_pin_membership.json
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

## 0(e) — `python tools/audit/gen_evidence_pin_membership.py --check` (after)

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

## 0(e) — `git diff 7c29492a… f460a683…` (the evidence-pin artifact, between explicit blobs)

```
diff --git a/7c29492ac930063603571c5698570f2a5b36675e b/f460a683346cfa4241852538227075a298bcec76
index 7c29492ac9..f460a68334 100644
--- a/7c29492ac930063603571c5698570f2a5b36675e
+++ b/f460a683346cfa4241852538227075a298bcec76
@@ -17,7 +17,7 @@
  },
  "counts": {
   "generated_ratification_documents": 7,
-  "ruling_records_read": 170,
+  "ruling_records_read": 171,
   "members": 7,
   "members_pinned": 5,
   "members_unresolved": 0,
@@ -311,6 +311,7 @@
   "records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md",
   "records/cowork/rulings/cowork_rulings_2026_10_18_l3_keyword_list_sitting.md",
   "records/cowork/rulings/cowork_rulings_2026_10_26_l3_position_57_sitting.md",
+  "records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md",
   "records/cowork/rulings/cowork_rulings_oi345_oi342_2026_08_07.md"
  ],
  "named_in_a_ruling_record_but_not_generated": {
```

## 0(e) — `python tools/audit/changed_paths.py --staged` before the Task 0 commit

```
A	records/cc/instructions/cc_instruction_pruning_rulings_execution_2026_11_01.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_five.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_four.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_six.md
A	records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md
M	tools/audit/evidence_pin_membership.json
6 changed path record(s) [staged]
```

## 0(e) — the Task 0 commit and push

```
[master 8112c4d226] record: entries 464 to 466, the pruning-iteration ruling record and the step-4 first dispatch
 6 files changed, 1843 insertions(+), 1 deletion(-)
 create mode 100644 records/cc/instructions/cc_instruction_pruning_rulings_execution_2026_11_01.md
 create mode 100644 records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_five.md
 create mode 100644 records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_four.md
 create mode 100644 records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_six.md
 create mode 100644 records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md
```

## 0(e) — the Task 0 push

```
To https://github.com/slimvince/MuseScore
   a18148e529..8112c4d226  master -> master
```

## 0(f) — the opening guard capture: `python tools/audit/gen_guard_state.py --check`

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

## 0(f) — `python tools/audit/gen_guard_classification.py --check`

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_per_session_reading.py', 'tools/audit/gen_withheld_family_reading.py']
```

## 0(g) — BEFORE: `python tools/audit/gen_session_start_read_size.py --check`

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
    STATUS.md                                                                 11997
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 248426
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 248426 [ruled membership]  (-118695, -32.33%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 248426 [ruled membership]  (-48406, -16.31%)  <- CROSSES A REGIME BOUNDARY
```

## 0(g) — BEFORE: `python tools/audit/gen_defense_share.py --check`

```
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
    of the whole session-start read (248426): 5.22%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

## 0(g) — BEFORE: `python tools/audit/decisions/gen_decisions_register.py --check`

```
the register matches the data (20 files: the index + 19 group files)
```

## 0(g) — BEFORE of Decision 2: `python tools/audit/decisions/gen_cluster_dispositions.py --verify`

```
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
```

## 0(g) — BEFORE of Decision 2: `python tools/audit/decisions/reaim_home_anchors.py --check`

```
  D-196: CLAUDE.md:1979 -> CLAUDE.md:1991   (drift +12)
  D-253: CLAUDE.md:1918-1936 -> CLAUDE.md:1930-1948   (drift +12)
  D-254: CLAUDE.md:1961-1968 -> CLAUDE.md:1973-1980   (drift +12)
  D-268: cowork_confidence_contract.md:36-48 -> cowork_confidence_contract.md:54-66   (drift +18)
  D-269: cowork_confidence_contract.md:83-85 -> cowork_confidence_contract.md:101-103   (drift +18)
  D-601: cowork_confidence_contract.md:89-101 -> cowork_confidence_contract.md:107-119   (drift +18)
anchors drifted: 6
```

## 1(b) — the record check (scratch script `t1b_record_check.py`)

```
SOURCE, AS READ (raw, line breaks shown as \n):
'- **Carried for the next dispatch (not applied here):** amend `CLAUDE.md` Conventions, *How a decision surface\n  is written*, step 4, replacing the OPEN QUESTION clause with this ruling, former wording preserved in place\n  (#12).'
line breaks with two-space continuation set aside: 2
SOURCE AFTER THE THREE SET-ASIDES:
Carried for the next dispatch (not applied here): amend `CLAUDE.md` Conventions, *How a decision surface is written*, step 4, replacing the OPEN QUESTION clause with this ruling, former wording preserved in place (#12).
LEDGER QUOTATION:
Carried for the next dispatch (not applied here): amend `CLAUDE.md` Conventions, *How a decision surface is written*, step 4, replacing the OPEN QUESTION clause with this ruling, former wording preserved in place (#12).
RECORD CHECK PASS: the quotation holds at its source, character for character, after the three set-asides
```

## 1(f) — the Task 1 reconciliation on the real files (scratch script `t1f_reconcile.py`)

```
[1] count in old CLAUDE.md = 1: '*(Former wording, preserved (#12): "**and how far that reaches is an OPEN'
[1] count in old CLAUDE.md = 1: 'the wide reading would change an outcome is flagged to him.")*'
[1] count in old CLAUDE.md = 1: 'is the route. *(Former wording,'
[1] count in old CLAUDE.md = 1: 'for this block**")*'
[1] PASS — P1 and P2 located, ends included
[2] PASS — the old CLAUDE.md with the two replacements EQUALS the new CLAUDE.md
[3] P1: in new archive 1, in old archive 0, in new CLAUDE.md 0
[3] P2: in new archive 1, in old archive 0, in new CLAUDE.md 0
[3] PASS — the new archive begins with the old; P1 and P2 moved, once each
[4] sizes in characters:
    old CLAUDE.md: 169617
    new CLAUDE.md: 169182
    P1: 455
    P2: 309
    pointer 1: 165
    pointer 2: 164
    old CLAUDE_ARCHIVE.md: 12881
    new CLAUDE_ARCHIVE.md: 14768
    appended block: 1887
    CLAUDE.md difference (new - old): -435
TASK 1 RECONCILIATION PASS
```

## 1(f) — planting F1 and F2 (scratch script `plant_faults_t1.py`)

```
F1 planted at character 16 'S' -> 'X'
F2 planted at character 13690 'Q' -> 'q'
```

## 1(f) — planted fault F1

```
[1] count in old CLAUDE.md = 1: '*(Former wording, preserved (#12): "**and how far that reaches is an OPEN'
[1] count in old CLAUDE.md = 1: 'the wide reading would change an outcome is flagged to him.")*'
[1] count in old CLAUDE.md = 1: 'is the route. *(Former wording,'
[1] count in old CLAUDE.md = 1: 'for this block**")*'
[1] PASS — P1 and P2 located, ends included
Traceback (most recent call last):
  File "C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\98f00c1a-583d-4710-be1e-e25cebd3f837\scratchpad\t1f_reconcile.py", line 46, in <module>
    raise AssertionError(f"ASSERTION 2 FAILED at character {i}: expected {expected[i:i+60]!r} vs new {new_c[i:i+60]!r}")
AssertionError: ASSERTION 2 FAILED at character 16: expected 'Standing Instructions for This Repository\n\n## Guiding princi' vs new 'Xtanding Instructions for This Repository\n\n## Guiding princi'
```

## 1(f) — planted fault F2

```
[1] count in old CLAUDE.md = 1: '*(Former wording, preserved (#12): "**and how far that reaches is an OPEN'
[1] count in old CLAUDE.md = 1: 'the wide reading would change an outcome is flagged to him.")*'
[1] count in old CLAUDE.md = 1: 'is the route. *(Former wording,'
[1] count in old CLAUDE.md = 1: 'for this block**")*'
[1] PASS — P1 and P2 located, ends included
[2] PASS — the old CLAUDE.md with the two replacements EQUALS the new CLAUDE.md
[3] P1: in new archive 0, in old archive 0, in new CLAUDE.md 0
Traceback (most recent call last):
  File "C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\98f00c1a-583d-4710-be1e-e25cebd3f837\scratchpad\t1f_reconcile.py", line 54, in <module>
    assert (a_new, a_old, c_new) == (1, 0, 0), f"ASSERTION 3 FAILED for {name}"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ASSERTION 3 FAILED for P1
```

## 1(g) — `python tools/audit/gen_governing_surface_split.py --check --pair CLAUDE.md`

```
  CLAUDE.md / CLAUDE_ARCHIVE.md: moved 9 span(s), 6,540 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
```

## 1(g) — `python tools/audit/gen_claude_md_finer_archive.py --check` (the unpredicted red)

```
FAIL: the finer archive record does not re-derive: tools\audit\claude_md_finer_archive.json
```

## 1(g) — `python tools/audit/gen_claude_md_prune_backlog.py --check` (the unpredicted red)

```
FAIL: the prune-at-amendment backlog record does not re-derive: tools\audit\claude_md_prune_backlog.json
```

## 1(g), cause — the finer-archive check at the reversed tree

```
FAIL: the finer archive record does not re-derive: tools\audit\claude_md_finer_archive.json
```

## 1(g), cause — the prune-backlog check at the reversed tree

```
FAIL: the prune-at-amendment backlog record does not re-derive: tools\audit\claude_md_prune_backlog.json
```

## 1(g), cause — field-by-field diagnosis (scratch script `cause_diag.py`)

```
== gen_claude_md_finer_archive: 1 differing leaf path(s)
  .reconciliation.every_span_the_ruling_REFUSED_is_still_present_at_site_exactly_once
    committed: 'True'
    rebuilt:   'False'
== gen_claude_md_prune_backlog: 1 differing leaf path(s)
  .reconciliation.every_span_the_reading_flagged_is_still_present_at_site_exactly_once
    committed: 'True'
    rebuilt:   'False'
```

## 2(a) — the backbone markers and the two excerpts (scratch script `t2a_excerpts.py`)

```
PRECEDING_REGIME_START in home_granularity: 1
REMOVED_FILE_START in scope_of_application: 1
REMOVED_FILE_END after it: 1
EXCERPT (iii-a):
THE PRECEDING REGIME, superseded and recorded here rather than deleted: from the phase-1n ruling of the same day until phase 1q the field was deliberately MIXED — D-430 was applied to 46 entries across 5 documents, where section granularity decided something, and every other entry carried a document-level home pending the next touch. The user ended that staging on 2026-08-03 by ruling ONE re-classification pass over the whole population (`OPEN_ITEMS.md` OI-291).
EXCERPT (iii-b):
**THE FILE THIS POINTER FORMERLY NAMED IS REMOVED (user, 2026-08-09, Ruling 1 of `cowork_rulings_2026_08_09_return.md`; recorded here in the D-644 shape — state the current arrangement, record the removal as closed).** `phase1q_reclassification.json` held NEITHER the phase-1q record NOR the present classes: the applying run had been performed by more than one wave since the 2026-08-04 establishment froze it and its snapshot as byte-identical, rewriting it each time (measured at `tools/audit/decisions/phase1q_record_divergence.json`, from git objects by explicit hash). The current arrangement is TWO files with one job each — the phase-1q record at the established, hash-guarded snapshot, and the LIVE derived view at `home_classification.json`, which is where this pointer now aims and which carries `the_phase_1r_re_run`, `the_2026_08_08_apply` and `write_list` unchanged. Every committed state of the removed file remains reachable in git history at the commits the divergence artifact names, so nothing is lost (#12, the recomputable-collapse clause) and one concern has one home (#6). TRIED AND CLOSED: restoring the stale file from the snapshot (a second, unguarded copy of the record — the OI-305 divergence class reopened) and renaming it for what it held (an orphan generated artifact with no writer and no consumer — undeclared dormancy).
2(a) EXCERPTS PASS
```

## 2(c) — `python tools/audit/decisions/gen_decisions_register.py` (write mode)

```
wrote 20 files: DECISIONS.md (the index, 772 lines) + 19 group files under decisions/ (477 decisions)
```

## 2(c) — `python tools/audit/decisions/gen_decisions_register.py --check`

```
the register matches the data (20 files: the index + 19 group files)
```

## 2(c) — `git diff --stat 8112c4d2… -- decisions/` (empty)

```
(empty)
```

## 2(e) — the Task 2 reconciliation on the real files (scratch script `t2e_reconcile.py`)

```
[1] count in old DECISIONS.md = 1: '> **Shape ratified by the user, 2026-07-28**'
[1] count in old DECISIONS.md = 1: "three delegations were written into `ARCHITECTURE.md` on the user's ru"
[1] count in old DECISIONS.md = 1: 'Alongside the register, every one of the harvested statements'
[1] count in old DECISIONS.md = 1: 'and `tools/audit/decisions/disposition_manifest.json`.'
[1] count in old DECISIONS.md = 1: ' THE PRECEDING REGIME, superseded'
[1] count in old DECISIONS.md = 1: ' **THE FILE THIS POINTER FORMERLY NAMED IS REMOVED'
[1] count in old DECISIONS.md = 1: ' Because the pass now runs twice over the same entries'
[1] count in old DECISIONS.md = 1: '> **★ Corrections to this scope block, 2026-08-04.**'
[1] count in old DECISIONS.md = 1: '-> `header.scope.corrections_2026_08_04.former_wording_preserved_verba'
[1] count in old DECISIONS.md = 1: '> register-level events above are where to look.'
[1] count in old DECISIONS.md = 1: '  register-level ratification events are listed in the preamble above.'
[1] count in old DECISIONS.md = 1: 'the register-level ratification events listed in the preamble are the '
[1] line numbers (1-based): block (1) 10-83; block (2) 233-246; block (4) 270-276
[1] line numbers: x1 88; x2 122; x3 229; (iii-a) 250; (iii-b) 258
[1] PASS
[2] PASS — the old DECISIONS.md with every replacement made once EQUALS the new DECISIONS.md
[3] block (1): in new archive 1, in new DECISIONS.md 0
[3] block (2): in new archive 1, in new DECISIONS.md 0
[3] excerpt (iii-a): in new archive 1, in new DECISIONS.md 0
[3] excerpt (iii-b): in new archive 1, in new DECISIONS.md 0
[3] block (4): in new archive 1, in new DECISIONS.md 0
[3] old line 88: in new archive 1, in new DECISIONS.md 0
[3] old line 122: in new archive 1, in new DECISIONS.md 0
[3] old line 229: in new archive 1, in new DECISIONS.md 0
[3] PASS
[4] sizes in characters:
    old DECISIONS.md: 127727
    new DECISIONS.md: 117490
    difference (new - old): -10237
    archived block (1): 7012
    archived block (2): 657
    archived excerpt (iii-a): 466
    archived excerpt (iii-b): 1354
    archived block (4): 2291
    archived old line 88: 48
    archived old line 122: 101
    archived old line 229: 437
    S1 pointer: 377
    S2 line: 99
    S3 line: 140
    S4 line: 449
    S5 pointer: 397
    pointer (iii-a): 143
    pointer (iii-b): 203
    S7 pointer: 323
    old DECISIONS_ARCHIVE.md: 1670
    new DECISIONS_ARCHIVE.md: 15976
    appended block: 14306
TASK 2 RECONCILIATION PASS
```

## 2(e) — planting F3 and F4 (scratch script `plant_faults_t2.py`)

```
F3 planted at character 24365 'D' -> 'X'
F4 planted at character 3228 'P' -> 'p'
```

## 2(e) — planted fault F3

```
[1] count in old DECISIONS.md = 1: '> **Shape ratified by the user, 2026-07-28**'
[1] count in old DECISIONS.md = 1: "three delegations were written into `ARCHITECTURE.md` on the user's ru"
[1] count in old DECISIONS.md = 1: 'Alongside the register, every one of the harvested statements'
[1] count in old DECISIONS.md = 1: 'and `tools/audit/decisions/disposition_manifest.json`.'
[1] count in old DECISIONS.md = 1: ' THE PRECEDING REGIME, superseded'
[1] count in old DECISIONS.md = 1: ' **THE FILE THIS POINTER FORMERLY NAMED IS REMOVED'
[1] count in old DECISIONS.md = 1: ' Because the pass now runs twice over the same entries'
[1] count in old DECISIONS.md = 1: '> **★ Corrections to this scope block, 2026-08-04.**'
[1] count in old DECISIONS.md = 1: '-> `header.scope.corrections_2026_08_04.former_wording_preserved_verba'
[1] count in old DECISIONS.md = 1: '> register-level events above are where to look.'
[1] count in old DECISIONS.md = 1: '  register-level ratification events are listed in the preamble above.'
[1] count in old DECISIONS.md = 1: 'the register-level ratification events listed in the preamble are the '
[1] line numbers (1-based): block (1) 10-83; block (2) 233-246; block (4) 270-276
[1] line numbers: x1 88; x2 122; x3 229; (iii-a) 250; (iii-b) 258
[1] PASS
Traceback (most recent call last):
  File "C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\98f00c1a-583d-4710-be1e-e25cebd3f837\scratchpad\t2e_reconcile.py", line 119, in <module>
    raise AssertionError(f"ASSERTION 2 FAILED at character {k}: expected {expected[k:k+80]!r} vs new {new_d[k:k+80]!r}")
AssertionError: ASSERTION 2 FAILED at character 24365: expected 'D-001 | Key, mode and chord are inferred by ONE joint decode | LIVE | — | `ARCHI' vs new 'X-001 | Key, mode and chord are inferred by ONE joint decode | LIVE | — | `ARCHI'
```

## 2(e) — planted fault F4

```
[1] count in old DECISIONS.md = 1: '> **Shape ratified by the user, 2026-07-28**'
[1] count in old DECISIONS.md = 1: "three delegations were written into `ARCHITECTURE.md` on the user's ru"
[1] count in old DECISIONS.md = 1: 'Alongside the register, every one of the harvested statements'
[1] count in old DECISIONS.md = 1: 'and `tools/audit/decisions/disposition_manifest.json`.'
[1] count in old DECISIONS.md = 1: ' THE PRECEDING REGIME, superseded'
[1] count in old DECISIONS.md = 1: ' **THE FILE THIS POINTER FORMERLY NAMED IS REMOVED'
[1] count in old DECISIONS.md = 1: ' Because the pass now runs twice over the same entries'
[1] count in old DECISIONS.md = 1: '> **★ Corrections to this scope block, 2026-08-04.**'
[1] count in old DECISIONS.md = 1: '-> `header.scope.corrections_2026_08_04.former_wording_preserved_verba'
[1] count in old DECISIONS.md = 1: '> register-level events above are where to look.'
[1] count in old DECISIONS.md = 1: '  register-level ratification events are listed in the preamble above.'
[1] count in old DECISIONS.md = 1: 'the register-level ratification events listed in the preamble are the '
[1] line numbers (1-based): block (1) 10-83; block (2) 233-246; block (4) 270-276
[1] line numbers: x1 88; x2 122; x3 229; (iii-a) 250; (iii-b) 258
[1] PASS
[2] PASS — the old DECISIONS.md with every replacement made once EQUALS the new DECISIONS.md
[3] block (1): in new archive 0, in new DECISIONS.md 0
Traceback (most recent call last):
  File "C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\98f00c1a-583d-4710-be1e-e25cebd3f837\scratchpad\t2e_reconcile.py", line 129, in <module>
    assert na == 1 and nd == 0, f"ASSERTION 3 FAILED for {name}"
           ^^^^^^^^^^^^^^^^^^^
AssertionError: ASSERTION 3 FAILED for block (1)
```

## 2(f) — `python tools/audit/gen_governing_surface_split.py --check --pair DECISIONS.md`

```
  DECISIONS.md / DECISIONS_ARCHIVE.md: moved 0 span(s), 0 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
```

## 2(f) — AFTER of Decision 2: `python tools/audit/decisions/gen_cluster_dispositions.py --verify`

```
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
```

## 2(f) — AFTER of Decision 2: `python tools/audit/decisions/reaim_home_anchors.py --check`

```
  D-196: CLAUDE.md:1979 -> CLAUDE.md:1991   (drift +12)
  D-253: CLAUDE.md:1918-1936 -> CLAUDE.md:1930-1948   (drift +12)
  D-254: CLAUDE.md:1961-1968 -> CLAUDE.md:1973-1980   (drift +12)
  D-268: cowork_confidence_contract.md:36-48 -> cowork_confidence_contract.md:54-66   (drift +18)
  D-269: cowork_confidence_contract.md:83-85 -> cowork_confidence_contract.md:101-103   (drift +18)
  D-601: cowork_confidence_contract.md:89-101 -> cowork_confidence_contract.md:107-119   (drift +18)
anchors drifted: 6
```

## 2(f) — the Task 2 guard capture: `python tools/audit/gen_guard_state.py --check`

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
  [FAIL] tools/audit/gen_l0_l1_outgoing_population.py --check
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
  [FAIL] tools/audit/gen_l3_outgoing_population.py --check
  [PASS] tools/audit/decisions/gen_decisions_register.py --check
  [FAIL] tools/audit/decisions/gen_cluster_dispositions.py --verify
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --check
  [PASS] tools/audit/decisions/gen_cluster_dispositions.py --producible
  [FAIL] tools/audit/decisions/gen_home_classification.py --check
  [FAIL] tools/audit/decisions/gen_phase1p_delegation_bar.py --check
  [PASS] tools/audit/decisions/gen_reads5_repack.py --check
  [PASS] tools/audit/decisions/gen_decision_clusters.py --check
  [FAIL] tools/audit/decisions/gen_phase1w_legacy_verification.py --check
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
83 guard(s) run, 19 failing, 4 not run, 20 historical record(s)
```

## 2(f) — the opening and Task 2 captures compared (scratch script `guard_compare.py`)

```
BEFORE header: STALE vs the run: guard_state.json does not re-derive | ['83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)']
AFTER  header: STALE vs the run: guard_state.json does not re-derive | ['83 guard(s) run, 19 failing, 4 not run, 20 historical record(s)']
differing verdicts: 5
  tools/audit/decisions/gen_phase1w_legacy_verification.py --check: [PASS] -> [FAIL]
  tools/audit/gen_defense_share.py --check: [PASS] -> [FAIL]
  tools/audit/gen_l0_l1_outgoing_population.py --check: [PASS] -> [FAIL]
  tools/audit/gen_l3_outgoing_population.py --check: [PASS] -> [FAIL]
  tools/audit/gen_session_start_read_size.py --check: [PASS] -> [FAIL]
AFTER failing set: ['tools/audit/gen_phase3_gate_partition.py --check', 'tools/audit/gen_filing_convention_application.py --check', 'tools/audit/gen_l0_l1_outgoing_population.py --check', 'tools/audit/gen_artifact_inventory.py --check', 'tools/audit/gen_artifact_inventory_surface.py --check', 'tools/audit/gen_test_construction_evidence.py --check', 'tools/audit/gen_retirement_caller_check.py --check', 'tools/audit/decisions/apply_soft_discard.py --check', 'tools/audit/decisions/apply_residue_discard.py --check', 'tools/audit/gen_session_start_read_size.py --check', 'tools/audit/gen_defense_share.py --check', 'tools/audit/gen_per_session_reading.py --check', 'tools/audit/gen_epoch_write_path.py --check', 'tools/audit/gen_recognizer_establishment_sort.py --check', 'tools/audit/gen_l3_outgoing_population.py --check', 'tools/audit/decisions/gen_cluster_dispositions.py --verify', 'tools/audit/decisions/gen_home_classification.py --check', 'tools/audit/decisions/gen_phase1p_delegation_bar.py --check', 'tools/audit/decisions/gen_phase1w_legacy_verification.py --check']
```

## 2(f), cause — `decisions/gen_phase1w_legacy_verification.py --check` at the edited tree

```
STOP: A1 (the marker is generated text): quote not at tools/audit/decisions/gen_decisions_register.py:514. It is now at line(s) [473] — re-aim the citation.
```

## 2(f), cause — `gen_l0_l1_outgoing_population.py --check` at the edited tree

```
STALE vs the derivation: l0_l1_outgoing_population.json does not re-derive
```

## 2(f), cause — `gen_l3_outgoing_population.py --check` at the edited tree

```
STALE vs the derivation: l3_outgoing_population.json does not re-derive
```

## 2(f), cause — `gen_defense_share.py --check` at the edited tree

```
STALE vs the measurement: defense_share.json does not re-derive
```

## 2(g) — the generator's changed passages (scratch script `extract_written.py`)

```
generator: 10 changed passage(s) (old line range -> new line range):
   ('insert', 98, 97, 98, 137)
   ('replace', 107, 180, 147, 150)
   ('replace', 185, 185, 155, 155)
   ('replace', 219, 219, 189, 189)
   ('replace', 362, 362, 332, 332)
   ('replace', 371, 384, 341, 345)
   ('replace', 386, 386, 347, 347)
   ('replace', 392, 392, 353, 354)
   ('replace', 403, 403, 365, 367)
   ('replace', 441, 450, 405, 409)
written gen_added.txt and archive_appended.txt
```

## 2(g) — the word scan over the generator's added lines (scratch script `wordscan.py`)

```
gen_added.txt:3: [\bregister\b] # history text — the register-level ratification events, the harvest-and-clusters disposition table,
gen_added.txt:41: [\bregister\b] > **★ THE REGISTER-LEVEL RATIFICATION EVENTS — ARCHIVED 2026-11-01 → `DECISIONS_ARCHIVE.md`.** The shape
gen_added.txt:45: [\bregister\b] > register-level events — archived to `DECISIONS_ARCHIVE.md`, pointed at above — are where to look.
gen_added.txt:46: [\bregister\b] register-level ratification events are archived in `DECISIONS_ARCHIVE.md`; the preamble above points there. (Field added 2026-08-03 on the
gen_added.txt:47: [\bregister\b] "the register-level ratification events archived in `DECISIONS_ARCHIVE.md` are the place to look "
gen_added.txt: 5 hit(s)
```

## 2(g) — the word scan over the archive's appended block (scratch script `wordscan.py`)

```
archive_appended.txt:8: [\bregister\b] > the move would have left them false. The decisions register's data file, `tools/audit/decisions/backbone_decisions.json`, is
archive_appended.txt:15: [\bregister\b] **(1) The register-level ratification events — `DECISIONS.md` lines 10–83 at `8112c4d226`.**
archive_appended.txt:41: [\bnotes?\b] > rephrased at the user's direction (the pedaled note can be in any voice, the D-207
archive_appended.txt:47: [\bregister\b] > refinement of the contract-home case. The register-level ratification does not overwrite
archive_appended.txt:62: [\bregister\b] > the register records the decision correctly; it is not a judgment that the decision is good, and it
archive_appended.txt:66: [\binstrument\b] > `OPEN_ITEMS.md` OI-315), and **D-468** was entered (the pinned block-(A) instrument's declared
archive_appended.txt:71: [\bregister\b] > is ratified is that the register records each decision correctly, never that the code obeys it.
archive_appended.txt:74: [\bregister\b] > only that the register transcribes that event correctly, and nothing is counted twice. Landing in
archive_appended.txt:89: [\bfigures?\b] > its provenance), D-576's caveat was recorded beside the figures it qualifies in gate block (A), and
archive_appended.txt:94: [\bregister\b] Alongside the register, every one of the harvested statements about decisions in this repository has been given a recorded disposition, so that none was silentl
archive_appended.txt:118: [\bfigures?\b] > **★ Corrections to this scope block, 2026-08-04.** User, 2026-08-04 (R3), dispatch `cc_instruction_phase1_delegations_and_corrections.md`: the three statement
archive_appended.txt:121: [\bfigures?\b] > - **'The remainder, measured'** — the unresolved figure was HAND-CARRIED in an authored string that nothing regenerated, and it disagreed with the computed di
archive_appended.txt:121: [\bfigures?\b] > - **'The remainder, measured'** — the unresolved figure was HAND-CARRIED in an authored string that nothing regenerated, and it disagreed with the computed di
archive_appended.txt:121: [\bfigures?\b] > - **'The remainder, measured'** — the unresolved figure was HAND-CARRIED in an authored string that nothing regenerated, and it disagreed with the computed di
archive_appended.txt:122: [\bmode\b] > - **The home-granularity claim** — that every `contract-home` or `gap` entry carries a `home_section` block — was false of the entries the six read waves ente
archive_appended.txt:124: [\bregister\b] > **Why the former wordings are preserved rather than replaced silently.** #12. Both sentences were true when written; what changed under them was the work — th
archive_appended.txt:124: [\bregister\b] > **Why the former wordings are preserved rather than replaced silently.** #12. Both sentences were true when written; what changed under them was the work — th
archive_appended.txt:128: [\bregister\b] > register-level events above are where to look.
archive_appended.txt:130: [\bregister\b] register-level ratification events are listed in the preamble above. (Field added 2026-08-03 on the
archive_appended.txt:132: [\bregister\b] The second-to-last row is about the DECISIONS; the last is about the ENTRIES. **243 of 477** entries carry a recorded event at which the entry itself — this quo
archive_appended.txt: 20 hit(s)
```

## 2(f) ★ — the reversal: regenerate (write mode)

```
wrote 20 files: DECISIONS.md (the index, 861 lines) + 19 group files under decisions/ (477 decisions)
```

## 2(f) ★ — the reversal: `gen_decisions_register.py --check`

```
the register matches the data (20 files: the index + 19 group files)
```

## 2(f) ★ — the five checks at the reversed tree (a loop over tool names)

```
== tools/audit/decisions/gen_phase1w_legacy_verification.py
phase1w: A1 held; 57 entries derived; 35 anchors located; 5 recorded figures located
exit:0
== tools/audit/gen_l0_l1_outgoing_population.py
l0_l1_outgoing_population.json re-derives
exit:0
== tools/audit/gen_l3_outgoing_population.py
l3_outgoing_population.json re-derives
exit:0
== tools/audit/gen_defense_share.py
the defense-share measurement re-derives
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
exit:0
== tools/audit/gen_session_start_read_size.py
the session-start read measurement re-derives
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
exit:0
```

## 3(b) — `python tools/audit/gen_status_batch_bound.py --apply`

```
wrote tools\audit\status_batch_bound.json
  entries moved: 3, 2,718 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

## 3(b) — `python tools/audit/gen_status_batch_bound.py --check`

```
  entries moved: 3, 2,718 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

## 3(b) — `python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md`

```
  STATUS.md / STATUS_ARCHIVE.md: moved 131 span(s), 457,949 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters
```

## 3(b) — `python tools/audit/gen_status_residue_move.py --check`

```
  candidates: 17, moved 16, left at site by the reading 1
  characters moved: 46,105
  byte-present in the companion exactly once: True
  absent from the must-read:                  True
  every flagged entry still at site:          True
```

## 3(b) — `python tools/audit/gen_status_archive_pass.py --check`

```
  dated entries moved: 52
  at the pass commit, the live file was exactly base-minus-range: True
  the moved block is verbatim in the archive at HEAD:             True
  the moved block is absent from the live file at HEAD:           True
```

## 3(c) — the six A2 checks before regeneration (a loop over tool names)

```
== tools/audit/gen_evidence_pin_membership.py
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 171
  members 7 — pinned 5, UNRESOLVED 0
exit:0
== tools/audit/gen_defense_share.py
STALE vs the measurement: defense_share.json does not re-derive
exit:1
== tools/audit/gen_session_start_read_size.py
STALE vs the measurement: session_start_read_size.json does not re-derive
exit:1
== tools/audit/gen_l0_l1_outgoing_population.py
l0_l1_outgoing_population.json re-derives
exit:0
== tools/audit/gen_l3_outgoing_population.py
STALE vs the derivation: l3_outgoing_population.json does not re-derive
exit:1
== tools/audit/gen_per_session_reading.py
STOP: the imported ordinary read measures 248127 characters and its committed artifact says 248426 at the same tree
exit:2
```

## 3(c) — `python tools/audit/gen_session_start_read_size.py` (write mode)

```
wrote tools/audit/session_start_read_size.json
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
    STATUS.md                                                                 11698
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 248127
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 248127 [ruled membership]  (-118994, -32.41%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 248127 [ruled membership]  (-48705, -16.41%)  <- CROSSES A REGIME BOUNDARY
```

## 3(c) — `python tools/audit/gen_defense_share.py` (write mode)

```
wrote tools/audit/defense_share.json
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
    of the whole session-start read (248127): 5.22%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

## 3(c) — `python tools/audit/gen_l3_outgoing_population.py` (write mode)

```
item 1: #### Layer 4 — the per-slice chord-symbol decoder — 140 lines
item 1: #### Layer 5 — the function/cadence layer — 117 lines
item 1: #### Layer 6 — the grouping layer — 65 lines
item 1: ### 4.3 ChordSymbolFormatter — 115 lines
item 1: ### 4.3b HarmonicRhythm — 81 lines
item 1: #### Harmonic rhythm detection — 20 lines
item 2: 12 distinct names, 12 resolve (844831 bytes), 4 in the specification set
item 3: 26 in-set files with a hit, 1364 distinct hit lines over them (ARCHITECTURE.md inside the six spans: 83, outside: 355); residue files: 150
item 4: in a specification-set member — 10
item 4: in an item-2 document that resolves — 9
item 4: inside item 1 — 3
transfer span: ratification_surfaces/cowork_comparison_l0_l1_reading.md — 287 lines
transfer span: ratification_surfaces/cowork_comparison_l2_reading.md — 948 lines
tabulation population: 57 members, 11276 lines, 1075960 bytes
wrote C:\s\MS\tools\audit\l3_outgoing_population.json
```

## 3(c) — `python tools/audit/gen_per_session_reading.py` (write mode)

```
wrote tools/audit/per_session_reading.json
  the ordinary session-start read (imported) 248127
    CLAUDE.md, the whole file as the executing sessions report it injected   169617
    BUILD_AND_TEST.md                                                         27236
    cowork_audit_protocol.md, the dispatch-protocol section                  108389
    the blind derivation of L3, whole                                        126702
  arc dispatches 30, 4982224 characters; arc reports 30, 3741155 characters
  Claude Code, per batch, in the thirtieth dispatch's shape: 696707
  Cowork, per sitting, in the shape of the sitting of entry 461: 995526
  six spans 105876 characters, 106 sub-blocks, archive-class 14269, doubt-defaulted 90909
  settled spans: 4 by hash, 2 by opening only, 2 not found
```

## 3(c) — the six A2 checks after regeneration (a loop over tool names)

```
== tools/audit/gen_evidence_pin_membership.py
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 171
  members 7 — pinned 5, UNRESOLVED 0
exit:0
== tools/audit/gen_defense_share.py
the defense-share measurement re-derives
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
exit:0
== tools/audit/gen_session_start_read_size.py
the session-start read measurement re-derives
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
exit:0
== tools/audit/gen_l0_l1_outgoing_population.py
l0_l1_outgoing_population.json re-derives
exit:0
== tools/audit/gen_l3_outgoing_population.py
l3_outgoing_population.json re-derives
exit:0
== tools/audit/gen_per_session_reading.py
the per-session reading measurement re-derives
  the ordinary session-start read (imported) 248127
    CLAUDE.md, the whole file as the executing sessions report it injected   169617
exit:0
```

## 3(c) — the moved artifacts' new and tip blobs

```
== tools/audit/session_start_read_size.json
warning: in the working copy of 'tools/audit/session_start_read_size.json', LF will be replaced by CRLF the next time Git touches it
0220060a466118cd31e7cf975724e4248cad7a6f
bd65f9f36e45c4abcdac4e58824dbcca0ff0361c
== tools/audit/defense_share.json
warning: in the working copy of 'tools/audit/defense_share.json', LF will be replaced by CRLF the next time Git touches it
b0fe1494643d685f1675a318339002fcf6da18ef
371d7932396427bc7a1d33214d7e2ca5ffd1f1cb
== tools/audit/l3_outgoing_population.json
warning: in the working copy of 'tools/audit/l3_outgoing_population.json', LF will be replaced by CRLF the next time Git touches it
7b4f925f671036e259d75e28a84dc6427c99be48
13d1750be95ecdcf408405ff7d6f67bba8db1dfe
== tools/audit/per_session_reading.json
warning: in the working copy of 'tools/audit/per_session_reading.json', LF will be replaced by CRLF the next time Git touches it
931c00dca5d6f4cf7970a91597b9a90e442bb18b
cfdbb22d3eda609cd51fe8ddf478804ecea04087
== tools/audit/status_batch_bound.json
warning: in the working copy of 'tools/audit/status_batch_bound.json', LF will be replaced by CRLF the next time Git touches it
4dbb1123826c53465761c982989761c410f90029
c1e07b1d145e7a2249445d77de9896e44aa1594f
```

## 3(c) — `session_start_read_size.json` between explicit blobs

```
diff --git a/bd65f9f36e45c4abcdac4e58824dbcca0ff0361c b/0220060a466118cd31e7cf975724e4248cad7a6f
index bd65f9f36e..0220060a46 100644
--- a/bd65f9f36e45c4abcdac4e58824dbcca0ff0361c
+++ b/0220060a466118cd31e7cf975724e4248cad7a6f
@@ -176,11 +176,11 @@
   },
   "characters_per_member": {
    "CLAUDE.md": 105876,
-   "STATUS.md": 11997,
+   "STATUS.md": 11698,
    "DECISIONS.md": 127727,
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
   },
-  "total_characters": 248426,
+  "total_characters": 248127,
   "further_spans_of_the_same_artifact_NOT_counted_into_the_read": {
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows": {
     "characters": 62498,
@@ -276,10 +276,10 @@
    "from_commit": "1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
    "from_total": 367121,
    "from_regime": "whole-file practice",
-   "to_total": 248426,
+   "to_total": 248127,
    "to_regime": "ruled membership",
-   "change_in_characters": -118695,
-   "change_percent": -32.33,
+   "change_in_characters": -118994,
+   "change_percent": -32.41,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   },
@@ -287,10 +287,10 @@
    "from_commit": "594074e1e1900079e449d2b79a38920d21bca6e6",
    "from_total": 296832,
    "from_regime": "whole-file practice",
-   "to_total": 248426,
+   "to_total": 248127,
    "to_regime": "ruled membership",
-   "change_in_characters": -48406,
-   "change_percent": -16.31,
+   "change_in_characters": -48705,
+   "change_percent": -16.41,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   }
```

## 3(c) — `defense_share.json` between explicit blobs

```
diff --git a/371d7932396427bc7a1d33214d7e2ca5ffd1f1cb b/b0fe1494643d685f1675a318339002fcf6da18ef
index 371d793239..b0fe149464 100644
--- a/371d7932396427bc7a1d33214d7e2ca5ffd1f1cb
+++ b/b0fe1494643d685f1675a318339002fcf6da18ef
@@ -77,7 +77,7 @@
  ],
  "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
   "the_six_session_start_spans": 105876,
-  "the_whole_ordinary_session_start_read": 248426,
+  "the_whole_ordinary_session_start_read": 248127,
   "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked defense; the second says how much of the WHOLE boot it is. A share quoted against one of them is not the share against the other."
  },
  "per_span": [
```

## 3(c) — `l3_outgoing_population.json` between explicit blobs

```
diff --git a/13d1750be95ecdcf408405ff7d6f67bba8db1dfe b/7b4f925f671036e259d75e28a84dc6427c99be48
index 13d1750be9..7b4f925f67 100644
--- a/13d1750be95ecdcf408405ff7d6f67bba8db1dfe
+++ b/7b4f925f671036e259d75e28a84dc6427c99be48
@@ -20123,7 +20123,7 @@
      "the_statement": "hit, outside the specification document set, not dispositioned by this comparison; reachable by the mining map",
      "hit_records": [
       {
-       "line_number": 20,
+       "line_number": 18,
        "term": "phrase",
        "tier": "admitting",
        "line": "*★ ARCHIVED 2026-08-17, THE SECOND ACT — the dated entries that PREDATE (or paraphrase) the OI-222 pointer convention fell to `operative-rule-text` in the pinned measurement and stayed when the block above was cleared. They were READ one by one and moved verbatim to `STATUS_ARCHIVE.md` by `records/cc/instructions/cc_instruction_preparation_seventh.md` Task 1, under Ruling 3 of `records/cowork/rulings/cowork_rulings_2026_08_17_sixth_return.md`, which brings them under Ruling 4's own line. **One candidate did NOT move and is flagged:** the navigational paragraph at the foot of this file is not a completed batch's dated record but a live pointer to the archive and to the gate policy, so the read-before-move safeguard left it at site. The per-entry reconciliation is re-derived by `tools/audit/gen_status_residue_move.py --check`.*"
```

## 3(c) — `per_session_reading.json` between explicit blobs

```
diff --git a/cfdbb22d3eda609cd51fe8ddf478804ecea04087 b/931c00dca5d6f4cf7970a91597b9a90e442bb18b
index cfdbb22d3e..931c00dca5 100644
--- a/cfdbb22d3eda609cd51fe8ddf478804ecea04087
+++ b/931c00dca5d6f4cf7970a91597b9a90e442bb18b
@@ -15,11 +15,11 @@
    "its_one_home": "`tools/audit/session_start_read_size.json`, written by `tools/audit/gen_session_start_read_size.py`; what stands here is that tool's own `measure` called at the tree, and its total is checked against that artifact on every run",
    "characters_per_member": {
     "CLAUDE.md": 105876,
-    "STATUS.md": 11997,
+    "STATUS.md": 11698,
     "DECISIONS.md": 127727,
     "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
    },
-   "total_characters": 248426,
+   "total_characters": 248127,
    "the_reading_of_claude_md": {
     "regime": "ruled membership",
     "characters": 105876
@@ -782,28 +782,28 @@
      "the_writing_sides_read": "unwritten practice"
     },
     "the_record_that_mandates_it": "the standing clause `Every dispatch's read-first block names the CURRENT HANDOVER BLOCK`, which this repository carries as numbered entry files; the writing side's three is its own practice",
-    "the_population_count": 383,
+    "the_population_count": 386,
     "the_three": [
      {
-      "name": "cowork_handoff_entry_four_hundred_and_sixty_one.md",
-      "added_in_commit": "6ab3c9ab6f11ed63f3058dc8a4fd2727dd41da65",
-      "added_at_unix_time": 1793526537,
-      "characters": 15962
+      "name": "cowork_handoff_entry_four_hundred_and_sixty_five.md",
+      "added_in_commit": "8112c4d2260d381dd35fe050df6837bb0488bcf7",
+      "added_at_unix_time": 1793557730,
+      "characters": 10716
      },
      {
-      "name": "cowork_handoff_entry_four_hundred_and_sixty_two.md",
-      "added_in_commit": "6ab3c9ab6f11ed63f3058dc8a4fd2727dd41da65",
-      "added_at_unix_time": 1793526537,
-      "characters": 14669
+      "name": "cowork_handoff_entry_four_hundred_and_sixty_four.md",
+      "added_in_commit": "8112c4d2260d381dd35fe050df6837bb0488bcf7",
+      "added_at_unix_time": 1793557730,
+      "characters": 17468
      },
      {
-      "name": "cowork_handoff_entry_four_hundred_and_sixty_three.md",
-      "added_in_commit": "023353b20cd77c31552a354fc512c879c7974348",
-      "added_at_unix_time": 1793530857,
-      "characters": 16354
+      "name": "cowork_handoff_entry_four_hundred_and_sixty_six.md",
+      "added_in_commit": "8112c4d2260d381dd35fe050df6837bb0488bcf7",
+      "added_at_unix_time": 1793557730,
+      "characters": 6264
      }
     ],
-    "characters": 46985
+    "characters": 34448
    }
   ],
   "totals_by_side": {
@@ -811,7 +811,7 @@
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 248426
+      "characters": 248127
      },
      {
       "member": "BUILD_AND_TEST.md",
@@ -831,11 +831,11 @@
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 46985
+      "characters": 34448
      }
     ],
-    "without_the_injected_copy_of_CLAUDE_md": 709543,
-    "with_it": 879160,
+    "without_the_injected_copy_of_CLAUDE_md": 696707,
+    "with_it": 866324,
     "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, 169617 characters",
     "left_out_and_said_so": "the previous report at the portions a dispatch orders, the reading file at its ordered portions, the ruling records a dispatch orders — varies per dispatch and is not sized here"
    },
@@ -843,7 +843,7 @@
     "the_members_it_sums": [
      {
       "member": "the ordinary session-start read (imported)",
-      "characters": 248426
+      "characters": 248127
      },
      {
       "member": "entry 118, the bridge-fault section",
@@ -863,7 +863,7 @@
      },
      {
       "member": "the three handoff entry files with the latest add-commits",
-      "characters": 46985
+      "characters": 34448
      },
      {
       "member": "the latest report of the arc, whole: cc_report_l3_comparison_tabulation_thirtieth_2026_10_31.md",
@@ -874,7 +874,7 @@
       "characters": 151805
      }
     ],
-    "characters": 1008362,
+    "characters": 995526,
     "left_out_and_said_so": "the verification reads at the objects (the reading file at its sections, the guard state, the ref files, the away-returns close) — varies per batch and is not sized here"
    }
   }
@@ -3320,7 +3320,7 @@
    ],
    "the_two_denominators": {
     "the_six_session_start_spans": 105876,
-    "the_whole_ordinary_session_start_read": 248426
+    "the_whole_ordinary_session_start_read": 248127
    },
    "how_these_relate_to_the_sums_above": "a marked clause lies INSIDE a sub-block, so these values overlap table 2's sums and are never added to them"
   }
```
