# CC REPORT — THE L2 COMPARISON, EIGHTH BATCH: THE TABULATION CONTINUED FROM POSITION 29 — POSITIONS 29 TO 38 TABULATED WHOLE, MEMBER 17'S REMARK CORRECTED AND MEMBER 22'S HEADINGS MARKED, THE REMAINDER UNTOUCHED (2026-09-29)

> **Executes** `records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md`, pinned
> at blob `22f79440951b69dac4f27c6a8d2ea97724ad44fa`. *(The title counts as the dispatch's own title counts; the
> reading file's §0 calls this run the seventh batch, and so does everything below.)* **No task STOPped.** The
> tabulation tabulated **positions 29 to 38**, each whole and each in its own commit, and stopped at the member
> boundary after position 38 **by the dispatch's order**, so that position 39 opens the next batch with nothing in
> front of it (D-670). Task 1A's one correction commit followed the last member commit. **This report decides
> nothing**: it relays what was run and what was written, and makes no recommendation about the derivation, the
> method, any disposition or any open question. Every output is quoted verbatim — the shell calls and their results
> extracted from this session's transcript file by a scratch script (§6, item 8), the saved outputs from the files
> the run wrote them to — filled into this report by a scratch script rather than typed. The session's scratch
> directory is written `<scratch>` in the quoted commands. **No count the population tool produces, and no count of
> the reading file's rows, is restated in prose (D-431)**; the row arithmetic is at the feet of the reading file's
> §6.29 to §6.38 and at its §13. The one exception the dispatch orders is the capacity judgment of Task 1(h), which
> states each member's `lines` and `bytes` as read at the artifact, and the comparison of position 39's size with
> position 23's that 1(h) orders for the report. Commit subjects are quoted as git prints them.

---

## 0. The ordered first read

The session's opening instruction named only this dispatch, so **the dispatch file was the first file read**, to
learn what to do; that read returned the file up to its line 658 (§6, item 1). *(`CLAUDE.md` and the auto-memory
index reached the session's context at boot as injected context, before any tool call.)* The first read after it
was `cowork_blind_derivation_l2_2026_09_27.md`, located with the file tools: its headings were listed, then **§5,
§6 and §7 were read in that order in one read of the file's closing span, and then the whole file from its first
line**. This came before any read of `STATUS.md`, `DECISIONS.md` or anything else. The remainder of the dispatch,
from its line 659, was read next.

The reads then continued in the dispatch's order: **(1)** `STATUS.md`; `DECISIONS.md` whole; `BUILD_AND_TEST.md`,
its condition being met because this batch runs the guard set; the gating answer at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`. *(`CLAUDE.md` was not
opened with a file tool; its whole content was in the context from boot, the six session-start spans among it.)*
**(2)** the audit protocol's dispatch-protocol section whole; **(3)** the three ruling records whole; **(4)** the
phase definition's §0 and §3.4; **(5)** `FRAMEWORK.md` §5 from the L0 charter to the end of the boundary contracts;
**(6)** the brief's §2, §4 and §7; **(7)** the boot pack's L2 counted set, withheld family (identities, documents,
passages) and leaks; **(8)** entry 268 whole; **(9)** the population artifact's `the_passage_rule`, `the_order` and
`the_members` from position 29 through 39, located by a search of the working-tree file and read from the object at
`f64f054d…` copied to scratch by explicit hash;
**(10)** the reading file's banner through the paragraph under `## 6.` that states the reading rules, with the first
three row blocks of §6.1; §6.24 from its heading to the end of its manifest; §6.28 whole; and §10 to §16 — **the
last not whole**, §11 and §12 having been read at their heads and ends and not through their middles (§6, item 2).
The derivation's own counts at its structure matched its manifest, and the boot pack's counted set matched the
relayed values.

**Not read, as the dispatch orders:** the L0/L1 reading file's §10, since position 62 was not reached; the sixth
batch's report and the earlier dispatches. The outgoing text of every member tabulated here is `ARCHITECTURE.md`,
read from its object at the Task 0 commit (blob `1ce6176c43e70348cef01f9a856426db10e18f98`, no line ending in a
carriage return), copied to scratch by explicit hash. Task 1A's own ordered read is at §3. **Reads beyond the
ordered set are declared at §6, item 3.**

---

## 1. Task 0 — the records landed, and pushed

**0(a) — the pin.** `git hash-object -w` over the dispatch and the handoff entry, then their sizes at the object:

```
$ git hash-object -w records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md; echo "exit:$?"; git hash-object -w records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md; echo "exit:$?"
warning: in the working copy of 'records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md', LF will be replaced by CRLF the next time Git touches it
22f79440951b69dac4f27c6a8d2ea97724ad44fa
exit:0
warning: in the working copy of 'records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md', LF will be replaced by CRLF the next time Git touches it
1adfa726712849d8b1b02b50cd572b1622454d99
exit:0
```

The sizes at the object, 96484 and 7616 bytes, were read by `git cat-file -s` at the end of the 0(b) call quoted
below. The blob was proved unmoved at staging: the first hash of 0(d) below and the index entry at 0(e) are the same.

**0(b) — the refs**, read with the file tools: `.git/refs/heads/master` and `.git/refs/remotes/origin/master` each
read `f64f054d9a19ccaf1c91dfbb0024a8f46f986076`, equal to the FACT. The chain, by explicit hash:

```
$ for h in f64f054d9a19ccaf1c91dfbb0024a8f46f986076 5aea89048e5d4f9f7812b4303b7f2247ce514618 3d76ccfa69bfd7db4d5b1b8e94fd361ab8b9a2b2 1cff398a50681b80a57df37087a4b17ff836c05d 4a4d26f8b5809de75c5f57e967c015eda9cfb23e 8a17050f47cec3f535a9ea8deb4e6d857e5a1adf 3441d3657a2fbb9dd7fc43743cf78f64fe7af962 3513346e9b5c571bc5c0528f3712fa52b03d4bfc 1f2366d859991dfe5d0f5026593c8e58d9faa2f3; do echo "=== $h"; git show --stat --format='commit %H%nparent %P%nsubject %s' $h; done > "<scratch>/chain.txt" 2>&1; echo "exit:$?"; git cat-file -s 22f79440951b69dac4f27c6a8d2ea97724ad44fa; git cat-file -s 1adfa726712849d8b1b02b50cd572b1622454d99; echo "exit:$?"
exit:0
96484
7616
exit:0
```

```
=== f64f054d9a19ccaf1c91dfbb0024a8f46f986076
commit f64f054d9a19ccaf1c91dfbb0024a8f46f986076
parent 5aea89048e5d4f9f7812b4303b7f2247ce514618
subject Close: the L2 tabulation continued from position 23, under its dispatch

 STATUS.md                                          |    2 +-
 STATUS_ARCHIVE.md                                  |    4 +
 ...rt_l2_comparison_tabulation_sixth_2026_09_28.md | 1332 ++++++++++++++++++++
 tools/audit/defense_share.json                     |    2 +-
 tools/audit/gen_status_batch_bound.py              |   51 +-
 tools/audit/guard_state.json                       |   12 +-
 tools/audit/l2_outgoing_population.json            |    2 +-
 tools/audit/session_start_read_size.json           |   16 +-
 tools/audit/status_batch_bound.json                |   20 +-
 9 files changed, 1412 insertions(+), 29 deletions(-)
=== 5aea89048e5d4f9f7812b4303b7f2247ce514618
commit 5aea89048e5d4f9f7812b4303b7f2247ce514618
parent 3d76ccfa69bfd7db4d5b1b8e94fd361ab8b9a2b2
subject comparison L2: member 15 SEEN mark and six feet corrected, no row re-tabulated

 .../cowork_comparison_l2_reading.md                | 32 ++++++++++++++--------
 1 file changed, 20 insertions(+), 12 deletions(-)
=== 3d76ccfa69bfd7db4d5b1b8e94fd361ab8b9a2b2
commit 3d76ccfa69bfd7db4d5b1b8e94fd361ab8b9a2b2
parent 1cff398a50681b80a57df37087a4b17ff836c05d
subject comparison L2: member 28 tabulated - 2 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 142 +++++++++++++++++++--
 1 file changed, 128 insertions(+), 14 deletions(-)
=== 1cff398a50681b80a57df37087a4b17ff836c05d
commit 1cff398a50681b80a57df37087a4b17ff836c05d
parent 4a4d26f8b5809de75c5f57e967c015eda9cfb23e
subject comparison L2: member 27 tabulated - 18 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 358 ++++++++++++++++++++-
 1 file changed, 343 insertions(+), 15 deletions(-)
=== 4a4d26f8b5809de75c5f57e967c015eda9cfb23e
commit 4a4d26f8b5809de75c5f57e967c015eda9cfb23e
parent 8a17050f47cec3f535a9ea8deb4e6d857e5a1adf
subject comparison L2: member 26 tabulated - 24 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 449 ++++++++++++++++++++-
 1 file changed, 435 insertions(+), 14 deletions(-)
=== 8a17050f47cec3f535a9ea8deb4e6d857e5a1adf
commit 8a17050f47cec3f535a9ea8deb4e6d857e5a1adf
parent 3441d3657a2fbb9dd7fc43743cf78f64fe7af962
subject comparison L2: member 25 tabulated - 53 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 873 ++++++++++++++++++++-
 1 file changed, 859 insertions(+), 14 deletions(-)
=== 3441d3657a2fbb9dd7fc43743cf78f64fe7af962
commit 3441d3657a2fbb9dd7fc43743cf78f64fe7af962
parent 3513346e9b5c571bc5c0528f3712fa52b03d4bfc
subject comparison L2: member 24 tabulated - 130 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 2065 +++++++++++++++++++-
 1 file changed, 2049 insertions(+), 16 deletions(-)
=== 3513346e9b5c571bc5c0528f3712fa52b03d4bfc
commit 3513346e9b5c571bc5c0528f3712fa52b03d4bfc
parent 1f2366d859991dfe5d0f5026593c8e58d9faa2f3
subject comparison L2: member 23 tabulated - 373 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 5651 +++++++++++++++++++-
 1 file changed, 5634 insertions(+), 17 deletions(-)
=== 1f2366d859991dfe5d0f5026593c8e58d9faa2f3
commit 1f2366d859991dfe5d0f5026593c8e58d9faa2f3
parent 33077b883affa549090e4323c8bf22e423835645
subject record: entry 267 and the sixth L2 tabulation dispatch

 ...on_l2_comparison_tabulation_sixth_2026_09_28.md | 1045 ++++++++++++++++++++
 ...rk_handoff_entry_two_hundred_and_sixty_seven.md |   93 ++
 2 files changed, 1138 insertions(+)
```

The chain is the one the FACT relays: the tip `f64f054d…` is the sixth batch's close, its parent is that batch's
correction commit `5aea8904…`, then members 28 down to 23, and that batch's Task 0 `1f2366d8…`.

**0(c) — A1's check.** `python tools/audit/changed_paths.py` over the whole tracked population, written to a scratch
file and read with the file tools, and the two landing paths with the index tree against the tip tree:

```
$ python tools/audit/changed_paths.py > "<scratch>/changed0.txt" 2>&1; echo "exit:$?"; for p in records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md; do git ls-files --others --exclude-standard -- "$p"; done; echo "exit:$?"; git write-tree; echo "exit:$?"; git rev-parse f64f054d9a19ccaf1c91dfbb0024a8f46f986076^{tree}; echo "exit:$?"
exit:0
records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md
records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md
exit:0
1be4ababdd4e972bfb10d45bd72479d40651b77e
exit:0
1be4ababdd4e972bfb10d45bd72479d40651b77e
exit:0
```

The enumeration's first nine lines and its last two:

```
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md
??	scratch_artifacts/baseline_composing.txt
…
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
396 changed path record(s) [worktree]
```

Every line between them is under `scratch_artifacts/`. So the enumeration shows **exactly one tracked
modification**, `tools/audit/claude_md_finer_archive.json`, the **two untracked landing paths**, and the standing
untracked population, as A1 declares; and the index tree equals the tip's tree, so nothing was staged.

**0(d) — the last-bytes check**, per landed file at its blob:

```
$ A=$(git hash-object -w --no-filters records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md); B=$(git hash-object -w --no-filters records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md); echo "$A $B"; python "<scratch>/lastbytes.py" 22f79440951b69dac4f27c6a8d2ea97724ad44fa 1adfa726712849d8b1b02b50cd572b1622454d99; echo "exit:$?"
22f79440951b69dac4f27c6a8d2ea97724ad44fa 1adfa726712849d8b1b02b50cd572b1622454d99
blob 22f79440951b69dac4f27c6a8d2ea97724ad44fa size 96484
  last 70 bytes: b'. TOWARDS the ultimate objective and TOWARDS the\nguiding principles.*\n'
  zero bytes: 0
  ends with newline byte (0x0a): True
  CR count: 0
blob 1adfa726712849d8b1b02b50cd572b1622454d99 size 7616
  last 70 bytes: b'ce: Cowork, 2026-09-29 (Stockholm), the sitting booted on entry 267.*\n'
  zero bytes: 0
  ends with newline byte (0x0a): True
  CR count: 0
exit:0
```

Each file ends in a newline byte and carries no zero byte and no carriage return.

**0(e) — the commit and the push.**

```
$ git add -- records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md; echo "exit:$?"; git write-tree; echo "exit:$?"
warning: in the working copy of 'records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md', LF will be replaced by CRLF the next time Git touches it
exit:0
fa37f46991a298fbeb5164262bb99bc794a16760
exit:0
$ git diff --stat --name-status 1be4ababdd4e972bfb10d45bd72479d40651b77e fa37f46991a298fbeb5164262bb99bc794a16760; echo "exit:$?"; git ls-tree -r fa37f46991a298fbeb5164262bb99bc794a16760 -- records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md; echo "exit:$?"
A	records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md
exit:0
100644 blob 22f79440951b69dac4f27c6a8d2ea97724ad44fa	records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md
100644 blob 1adfa726712849d8b1b02b50cd572b1622454d99	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md
exit:0
$ git commit -q -m 'record: entry 268 and the seventh L2 tabulation dispatch

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'; echo "exit:$?"; git push -q origin master; echo "exit:$?"
exit:0
exit:0
```

`fa37f469…` is the staged tree and `1be4abab…` the tip's tree, each written as its literal hash. Both refs then read
`b91c56971806e69af6bdccb10198a95d87fd5d05` at their files, read with the file tools, and the commit is:

```
$ git show --stat --format='commit %H%nparent %P%nsubject %s' b91c56971806e69af6bdccb10198a95d87fd5d05; echo "exit:$?"; echo "PYTHONIOENCODING=[${PYTHONIOENCODING-unset}]"; echo "SHELL=$SHELL"; python --version
commit b91c56971806e69af6bdccb10198a95d87fd5d05
parent f64f054d9a19ccaf1c91dfbb0024a8f46f986076
subject record: entry 268 and the seventh L2 tabulation dispatch

 ..._l2_comparison_tabulation_seventh_2026_09_29.md | 1102 ++++++++++++++++++++
 ...rk_handoff_entry_two_hundred_and_sixty_eight.md |   93 ++
 2 files changed, 1195 insertions(+)
exit:0
PYTHONIOENCODING=[unset]
SHELL=/bin/bash.exe
Python 3.14.3
```

**0(f) — the opening guard capture.** The environment, recorded so that 2(d) could run under the same one — Git
Bash, `PYTHONIOENCODING` not set, Python 3.14.3, as the last three lines of the call quoted at 0(e) show. The
invocation that writes, saved to a scratch file outside the repository:

```
$ python tools/audit/gen_guard_state.py > "<scratch>/guard_open.txt" 2>&1; echo "exit:$?"
exit:0
```

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
  [PASS] tools/audit/gen_evidence_pin_membership.py --check
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
80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

Against A2: exactly the twelve FAIL verdicts the FACT names, and no thirteenth; `gen_evidence_pin_membership.py
--check` passes. Then the classification (its exit status 2 is its STOP):

```
$ python tools/audit/gen_guard_classification.py > "<scratch>/guardclass_open.txt" 2>&1; echo "exit:$?"; git show f64f054d9a19ccaf1c91dfbb0024a8f46f986076:tools/audit/guard_state.json > "<scratch>/guard_state_f64f.json"; echo "exit:$?"
exit:2
exit:0
```

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

Exactly the four tools of the FACT, and no fifth. The object of `tools/audit/guard_state.json` at `f64f054d…`, copied
to scratch, reads 80 run, 68 passing and 12 failing, the same as the capture.

**0(g) — the two blobs**, verified before Task 1 opened, at `b91c5697…` and in the working tree, with their sizes:

```
$ git rev-parse b91c56971806e69af6bdccb10198a95d87fd5d05:cowork_blind_derivation_l2_2026_09_27.md b91c56971806e69af6bdccb10198a95d87fd5d05:cowork_blind_session_brief_l2.md; echo "exit:$?"; git hash-object cowork_blind_derivation_l2_2026_09_27.md cowork_blind_session_brief_l2.md; echo "exit:$?"; git cat-file -s d78ac530992860d38d1f605a77a2961d5440a2f6; git cat-file -s c5ff83dcad2107ac8c05ead21724cbab0d9471fd; echo "exit:$?"
d78ac530992860d38d1f605a77a2961d5440a2f6
c5ff83dcad2107ac8c05ead21724cbab0d9471fd
exit:0
d78ac530992860d38d1f605a77a2961d5440a2f6
c5ff83dcad2107ac8c05ead21724cbab0d9471fd
exit:0
125549
35952
exit:0
```

Both agree with the FACT.

**E0 — MET.** Two paths in one commit; `origin/master` at the commit; the pin proved; A1 reported with its
enumeration; the opening capture held against A2; the two blobs verified.

---

## 2. Task 1 — the tabulation, continued

### 2.1 The capacity judgments (1(h))

| Position | `lines` | `bytes` | Judgment | Written out before opening? |
|---|---|---|---|---|
| 29 | 90 | 4,556 | can finish whole | **yes**, verbatim below |
| 30 | 396 | 26,335 | can finish whole | **yes**, verbatim below |
| 31 | 9 | 1,097 | can finish whole | **yes**, verbatim below |
| 32 | 16 | 1,046 | can finish whole | **yes**, verbatim below |
| 33 | 43 | 3,158 | can finish whole | **yes**, verbatim below |
| 34 | 26 | 1,990 | can finish whole | **yes**, verbatim below |
| 35 | 3 | 173 | can finish whole | **yes**, verbatim below |
| 36 | 15 | 1,080 | can finish whole | **yes**, verbatim below (§6, item 5) |
| 37 | 10 | 722 | can finish whole | **yes**, verbatim below |
| 38 | 27 | 13,982 | can finish whole | **yes**, verbatim below |

The sizes are the artifact's, read at `tools/audit/l2_outgoing_population.json` → `the_tabulation_population` →
`the_members`. Each member from 29 to 38 was finished whole. **Each judgment was written out before the member's
text was read**, as its own paragraph in scratch, and appended to the scratch capacity log by a scratch script
that stamps the time; that log is the proof the dispatch asks for, the sixth batch having shown that the session's
transcript file does not keep such messages once a compaction has passed over them. **This context was not
compacted during Task 1.** The capacity log, verbatim:

```
=== appended 2026-09-29 06:30:54 UTC ===
**Capacity judgment before position 29 (written out before any read of its text, per 1(h)).** Position 29, `ARCHITECTURE.md` passages under *10. Visualization*: the artifact gives `lines` 90 and `bytes` 4556. Twelve ranges, two of them code blocks, so the code-line reading of member 23 applies. The context is uncompacted, the session-start reads and Task 0 are done, and every member left to the stop (positions 29 to 38) is small next to position 23. My judgment is that position 29 can be finished whole in the context that remains, together with the batch's later members and its close.

=== appended 2026-09-29 06:44:56 UTC ===
**Capacity judgment before position 30 (written out before any read of its text, per 1(h)).** Position 30, `ARCHITECTURE.md` passages under *11. Intonation*: the artifact gives `lines` 396 and `bytes` 26335, the largest of positions 29 to 38, in fifty-one ranges, three of them code blocks and one a text block. One member is committed and the context has not been compacted. Much of §11 is about the tuning tools, which the earlier readings list under *not a statement*, so the draft should be of moderate size. My judgment is that position 30 can be finished whole in the context that remains, with positions 31 to 38, Task 1A and the close still to run.

=== appended 2026-09-29 07:02:24 UTC ===
**Capacity judgment before position 31 (written out before any read of its text, per 1(h)).** Position 31, `ARCHITECTURE.md` passages under *12. User Interface*: the artifact gives `lines` 9 and `bytes` 1097, one range, a table. Two members are committed and the context has not been compacted. My judgment is that position 31 can be finished whole in the context that remains, with positions 32 to 38, Task 1A and the close still to run.

=== appended 2026-09-29 07:04:38 UTC ===
**Capacity judgment before position 32 (written out before any read of its text, per 1(h)).** Position 32, `ARCHITECTURE.md` passages under *14. ML Readiness*: the artifact gives `lines` 16 and `bytes` 1046, two ranges. Three members are committed and the context has not been compacted. My judgment is that position 32 can be finished whole in the context that remains, with positions 33 to 38, Task 1A and the close still to run.

=== appended 2026-09-29 07:07:44 UTC ===
**Capacity judgment before position 33 (written out before any read of its text, per 1(h)).** Position 33, `ARCHITECTURE.md` passages under *15. Development Phases*: the artifact gives `lines` 43 and `bytes` 3158, six ranges. Four members are committed and the context has not been compacted. My judgment is that position 33 can be finished whole in the context that remains, with positions 34 to 38, Task 1A and the close still to run.

=== appended 2026-09-29 07:13:42 UTC ===
**Capacity judgment before position 34 (written out before any read of its text, per 1(h)).** Position 34, `ARCHITECTURE.md` passages under *16. Scope Reference*: the artifact gives `lines` 26 and `bytes` 1990, four ranges. Five members are committed and the context has not been compacted. My judgment is that position 34 can be finished whole in the context that remains, with positions 35 to 38, Task 1A and the close still to run.

=== appended 2026-09-29 07:16:29 UTC ===
**Capacity judgment before position 35 (written out before any read of its text, per 1(h)).** Position 35, `ARCHITECTURE.md` passages under *18. Contributing*: the artifact gives `lines` 3 and `bytes` 173, one range. Six members are committed and the context has not been compacted. My judgment is that position 35 can be finished whole in the context that remains, with positions 36 to 38, Task 1A and the close still to run.

=== appended 2026-09-29 07:18:13 UTC ===
**Capacity judgment before position 36 (written out before any read of its text, per 1(h)).** Position 36, `ARCHITECTURE.md` passages under *19. LLM Integration — Claude Composer*: the artifact gives `lines` 15 and `bytes` 1080, three ranges. Seven members are committed and the context has not been compacted. My judgment is that position 36 can be finished whole in the context that remains, with positions 37 and 38, Task 1A and the close still to run.

=== appended 2026-09-29 07:20:18 UTC ===
**Capacity judgment before position 37 (written out before any read of its text, per 1(h)).** Position 37, `ARCHITECTURE.md` passages under *Appendix A — Key Musical Concepts*: the artifact gives `lines` 10 and `bytes` 722, three ranges. Eight members are committed and the context has not been compacted. My judgment is that position 37 can be finished whole in the context that remains, with position 38, Task 1A and the close still to run.

=== appended 2026-09-29 07:22:11 UTC ===
**Capacity judgment before position 38 (written out before any read of its text, per 1(h)).** Position 38, `ARCHITECTURE.md` passages under *Appendix B — MuseScore Score Model Quick Reference*: the artifact gives `lines` 27 and `bytes` 13982, two ranges. One is a code block; the other holds one very long line, the document's version history, which accounts for most of the bytes. Nine members are committed and the context has not been compacted. My judgment is that position 38 can be finished whole in the context that remains, with Task 1A and the close still to run. It is the last member this batch opens.
```

**One of these judgments misstates a count, and the misstatement is reported rather than corrected in the log**
(§7, finding 1): the judgment for position 30 says *"fifty-one ranges"*; the artifact's range list for that member
is longer, as the listing at §2.7 shows. Its `lines` and `bytes` are stated correctly, and the judgment's conclusion
did not depend on the range count.

### 2.2 The members, as written

Each member is a subsection §6.M of the reading file, carrying its manifest (the published ranges by their first
and last lines; the WITHHELD homes from the artifact, with a check of every decision homed inside the ranges at the
decisions backbone; and the SEEN check made at the homes), its rows, its *not a statement* list, its arithmetic, its
distribution, its current-text axis and its marks. **No member of this batch carries a WITHHELD home or a SEEN home**:
every artifact `item_4_identities_inside` from 29 to 38 is empty, and the two SEEN homes in `ARCHITECTURE.md`, D-002
and D-095, lie at lines 21–22 and 43–44, outside every range. The located check of the backbone:

```
$ python "<scratch>/homes.py"; echo "exit:$?"
entry keys: ['id', 'group', 'title', 'verbatim', 'plain', 'home', 'home_is_layer_spec', 'status', 'date', 'ratified_by', 'status_source', 'patterns', 'rationale']
SEEN D-002 ('ARCHITECTURE.md', 21, 22) raw: ARCHITECTURE.md:21-22
SEEN D-095 ('ARCHITECTURE.md', 43, 44) raw: ARCHITECTURE.md:43-44
SEEN D-223 ('docs/scoring_model.md', 1184, 1186) raw: docs/scoring_model.md:1184-1186
SEEN D-261 ('cowork_bounded_context_design.md', 57, 71) raw: cowork_bounded_context_design.md:57-71
SEEN D-275 ('cowork_notation_output_contract.md', 54, 57) raw: cowork_notation_output_contract.md:54-57
SEEN D-279 ('cowork_engage_arc_plan.md', 69, 72) raw: cowork_engage_arc_plan.md:69-72
SEEN D-322 ('docs/scoring_model.md', 286, 291) raw: docs/scoring_model.md:286-291
SEEN D-393 ('cowork_voiceleading_axis_design.md', 372, 377) raw: cowork_voiceleading_axis_design.md:372-377
member 29 homes inside ranges: []
member 30 homes inside ranges: [('D-248', 7294, 7296, (7288, 7299))]
member 31 homes inside ranges: []
member 32 homes inside ranges: []
member 33 homes inside ranges: []
member 34 homes inside ranges: []
member 35 homes inside ranges: []
member 36 homes inside ranges: []
member 37 homes inside ranges: []
member 38 homes inside ranges: []
unparsed homes: 6 [('D-112', 'CLAUDE.md'), ('D-113', 'CLAUDE.md'), ('D-115', 'CLAUDE.md'), ('D-230', 'CLAUDE.md'), ('D-231', 'CLAUDE.md'), ('D-316', 'CLAUDE.md')]
exit:0
```

- **Position 29** — the `ARCHITECTURE.md` passages under *10. Visualization*: the developer's demo view, its step
  event and prerequisite with the correction dated 2026-08-02; the harmonic-map interface; the functional harmony
  map.
- **Position 30** — the passages under *11. Intonation*: the tuning systems and the tuning tools' design, then §11.5
  (the region analysis and the chord track) and §11.6 (the region tuning). One decision is homed inside the ranges,
  **D-248**, at lines 7294–7296 inside range 62, the home of Row 30.67; it is not among the decisions ruled L2's own,
  so no row is marked.
- **Position 31** — the passages under *12. User Interface*: the table of the menu actions. The member places no
  outgoing statement.
- **Position 32** — the passages under *14. ML Readiness*.
- **Position 33** — the passages under *15. Development Phases*: the development tools, a benchmark sign-off and two
  phases' item lists.
- **Position 34** — the passages under *16. Scope Reference*: four one-sentence paragraphs of product scope; two of
  them mix product features outside the analysis with the analysis's own subject in one sentence and are UNPLACED
  with what was read.
- **Position 35** — the passages under *18. Contributing*. The member places no outgoing statement.
- **Position 36** — the passages under *19. LLM Integration — Claude Composer*; its one row is RELOCATED to L3,
  travelling with Row 17.23(ii).
- **Position 37** — the passages under *Appendix A — Key Musical Concepts*: three glossary entries defining standard
  music theory. The member places no outgoing statement.
- **Position 38** — the passages under *Appendix B — MuseScore Score Model Quick Reference*: a code block, a
  traversal, three rules for reading a score, and the document's closing lines, its version history among them.

### 2.3 How the rows were checked before each commit (1(g))

All seven checks ran on every member, on scratch copies taken from git objects by explicit hash, before its commit:

- **the quotation and coverage check** — every quoted outgoing statement and every *not a statement* quotation found
  in the member's text at the object (emphasis stripped, whitespace collapsed, list markers removed, a quotation
  elided with *"…"* matched at both ends), its locator equal to the lines where it is found, every quotation inside
  the member's ranges, and every character of text inside the ranges covered by some quotation, headings excepted
  under reading rule (1). It was proved at position 29 on a planted deletion of one row's quotation, which it
  reported;
- **the manifest check** — every range's first and last line in the built manifest compared with the source line,
  whole or by its opening and closing words;
- **the short-quotation check** — every short quotation inside the axis, difference and disposition sentences, and
  inside the added §10 to §12 entries, found in the derived statement it is attributed to or in the outgoing text;
- **the count check** — claims, dispositions and verdicts counted from the member text, every claim with exactly one
  disposition and at least one verdict, and every row naming a NEAREST statement carrying the NEAREST wording;
- **the build check** — the member inserted into the parent commit's reading file in scratch, §6.1 up to the
  previous member proven byte-identical to the parent blob's span, the §10, §11 and §12 entries proven to name
  exactly the member's relocated, quarantined and DIFFERS statements, and every changed passage outside the member
  listed and read;
- **the word scan** — own prose, quotations removed, for British spellings and non-musical uses of the reserved
  words; each hit that was not the musical sense or a qualified use was rephrased;
- **the scripted consistency check** — every *"travelling with Row M.n"* pointing at a row of the same disposition,
  and every *"as at Row M.n"* at a row naming the same derived statement and verdict. It was proved at position 29 on
  two planted faults, each reported. It reported **no new flag in any member of this batch.** It flags a stable set
  of three rows of earlier members, the same at every run of this batch; each was read at its row and is reported
  at §7, finding 2.

The proofs on planted faults, at position 29:

```
$ PYTHONUTF8=1 python "<scratch>/check_member.py" 29 "<scratch>/m29.md" > "<scratch>/chk29.txt" 2>&1; echo "exit:$?"; PYTHONUTF8=1 python "<scratch>/check_member.py" 29 "<scratch>/m29.md" --drop-quote 5 > "<scratch>/chk29_proof.txt" 2>&1; echo "exit:$?"
exit:0
exit:0
```

The coverage proof's output, from the file that call wrote (its first line and its closing problems list):

```
coverage proof: dropped row 29.5 6043 6044
…
PROBLEMS (1):
   COVERAGE range 6041-6044 uncovered: ['These are the actual output of `analyzeChord` for that candidate.']
```

```
$ S="<scratch>"; PYTHONUTF8=1 python "$S/consistency.py" "$S/planted29.md" "$S/built29.md"; echo "exit:$?"; PYTHONUTF8=1 python "$S/consistency.py" "$S/reading_b91c.md" > "$S/cons_base.txt"; echo "exit:$?"; PYTHONUTF8=1 python "$S/consistency.py" "$S/built29.md" "$S/reading_b91c.md"; echo "exit:$?"
rows parsed: 2715  flags: 5
baseline flags: 3  NEW flags: 2
  NEW ASAT 23.8 L2-S27 AGREES -> Row 6.12(i) does not carry it
  NEW TRAVEL 29.14 (QUARANTINED) -> Row 29.12 carries ['HISTORICAL']
exit:0
exit:0
rows parsed: 2715  flags: 3
baseline flags: 3  NEW flags: 0
exit:0
```

**What the checks caught, and what was changed before the commits.** In the scratch scripts, limits of their own
patterns, each fixed and the member re-checked: a locator wrapped onto a new line; a disposition or verdict with its
period inside the bold; a dash followed by a line break inside a quotation or an item; the manifest's count
sentence broken across a line; the manifest's opening-words window; and, in the consistency check, an axis segment
that ran on into the following *difference* paragraph, which had produced false flags — after that fix the baseline
fell to the three flags of §7, finding 2. The scratch assembly script was also changed to cut a quotation's opening
words at a word boundary rather than mid-word. **In the drafts:** at position 29, a row title using *mode* in its
operating sense, rephrased; at position 30, the British spelling *labelled* in Row 30.46's title, and the locators of
two *not a statement* items (145 and 146), corrected to lines 7429–7430 and 7430–7431. At position 33 the word scan
flagged *analyses*, the plural noun, which is correct American English and was left.

### 2.4 The commits

```
$ S="<scratch>"; cd /c/s/MS && git log --format='%H %s' f64f054d9a19ccaf1c91dfbb0024a8f46f986076..d08b5f955781785918d9fcee24ad8549d377b6d1 > "$S/batchlog.txt"; git diff --name-status f64f054d9a19ccaf1c91dfbb0024a8f46f986076 d08b5f955781785918d9fcee24ad8549d377b6d1 > "$S/batchpaths.txt"; echo "exit:$?"
exit:0
```

```
d08b5f955781785918d9fcee24ad8549d377b6d1 comparison L2: member 17 remark and member 22 heading note corrected, no row re-tabulated
cf3389d038bf2dfeee86485aa980486b0f6b30ea comparison L2: member 38 tabulated - 4 outgoing statements placed, proposals only
b7646b1f95ac3647146392458dd7ec5c22c27f3a comparison L2: member 37 tabulated - 0 outgoing statements placed, proposals only
986457a0f5fe512f68f103ccf3a44ca88050d5c0 comparison L2: member 36 tabulated - 1 outgoing statements placed, proposals only
e98f70d984fa02f3ef5e3a735d92e7a4deaa53e7 comparison L2: member 35 tabulated - 0 outgoing statements placed, proposals only
fff8ac55df4cc2110967bbe4ce48f09ed132c1e1 comparison L2: member 34 tabulated - 4 outgoing statements placed, proposals only
f0e9472c26d153e147240eceb67fb48baee9fbcf comparison L2: member 33 tabulated - 20 outgoing statements placed, proposals only
af0a03ca0e54ad4253fcbb06056de1edfbcab453 comparison L2: member 32 tabulated - 12 outgoing statements placed, proposals only
56db74398379de2d36ca67950911555ce6b62041 comparison L2: member 31 tabulated - 0 outgoing statements placed, proposals only
8a0c77eb6914868ed9ce74e50130244f43c26e44 comparison L2: member 30 tabulated - 87 outgoing statements placed, proposals only
adb02e73ecb7bc05ceba49d4b0267101b9e813e9 comparison L2: member 29 tabulated - 31 outgoing statements placed, proposals only
b91c56971806e69af6bdccb10198a95d87fd5d05 record: entry 268 and the seventh L2 tabulation dispatch
```

Each member commit carries the reading file alone, staged by explicit path. The staged set was proved at every
member by writing the index tree and diffing it against the parent's tree by their two literal hashes, and every
such proof showed the one path `M ratification_surfaces/cowork_comparison_l2_reading.md` with the checked build's
blob; after each push `.git/refs/remotes/origin/master` was read with the file tools and equaled that member's
commit. The proof at position 29, for its shape:

```
$ git hash-object ratification_surfaces/cowork_comparison_l2_reading.md; git hash-object --no-filters ratification_surfaces/cowork_comparison_l2_reading.md; git config --get core.autocrlf; echo "exit:$?"
91580bc07598fb2b3fdbb28918da1d4890800b01
91580bc07598fb2b3fdbb28918da1d4890800b01
true
exit:0
$ S="<scratch>"; python "$S/place.py" "$S/built29.md"; echo "exit:$?"; cd /c/s/MS && git hash-object -w ratification_surfaces/cowork_comparison_l2_reading.md; git hash-object -w "$S/built29.md"; echo "exit:$?"
placed 2528433 bytes
exit:0
warning: in the working copy of 'ratification_surfaces/cowork_comparison_l2_reading.md', LF will be replaced by CRLF the next time Git touches it
fc4d96002539b41c0a57f0fe7e8e6dbc606ecd81
warning: in the working copy of '<scratch>/built29.md', LF will be replaced by CRLF the next time Git touches it
fc4d96002539b41c0a57f0fe7e8e6dbc606ecd81
exit:0
$ git add -- ratification_surfaces/cowork_comparison_l2_reading.md; echo "exit:$?"; git write-tree; echo "exit:$?"; git rev-parse b91c56971806e69af6bdccb10198a95d87fd5d05^{tree}; echo "exit:$?"
warning: in the working copy of 'ratification_surfaces/cowork_comparison_l2_reading.md', LF will be replaced by CRLF the next time Git touches it
exit:0
03b8e02a9b93c5aded2e03731e3467619af6712e
exit:0
fa37f46991a298fbeb5164262bb99bc794a16760
exit:0
$ git diff --name-status fa37f46991a298fbeb5164262bb99bc794a16760 03b8e02a9b93c5aded2e03731e3467619af6712e; echo "exit:$?"; git ls-tree 03b8e02a9b93c5aded2e03731e3467619af6712e -- ratification_surfaces/cowork_comparison_l2_reading.md; echo "exit:$?"
M	ratification_surfaces/cowork_comparison_l2_reading.md
exit:0
100644 blob fc4d96002539b41c0a57f0fe7e8e6dbc606ecd81	ratification_surfaces/cowork_comparison_l2_reading.md
exit:0
$ git commit -q -m 'comparison L2: member 29 tabulated - 31 outgoing statements placed, proposals only

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'; echo "exit:$?"; git push -q origin master; echo "exit:$?"
exit:0
exit:0
$ git show --stat --format='commit %H%nparent %P%nsubject %s' adb02e73ecb7bc05ceba49d4b0267101b9e813e9; echo "exit:$?"
commit adb02e73ecb7bc05ceba49d4b0267101b9e813e9
parent b91c56971806e69af6bdccb10198a95d87fd5d05
subject comparison L2: member 29 tabulated - 31 outgoing statements placed, proposals only

 .../cowork_comparison_l2_reading.md                | 563 ++++++++++++++++++++-
 1 file changed, 548 insertions(+), 15 deletions(-)
exit:0
```

The banner edit 1(f) orders was made once, in the member-29 commit.

The paths this batch's commits touched, from the sixth batch's close to Task 1A's commit, by explicit hash:

```
M	ratification_surfaces/cowork_comparison_l2_reading.md
A	records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md
```

### 2.5 §6.1 to §6.28 proven untouched before Task 1A (A5, step (i))

The span from `### 6.1 — ` up to the line before `## 7.` in the blob at `f64f054d…`, against the span from
`### 6.1 — ` up to the separator before `### 6.29 — ` in the last member commit's blob (commit `cf3389d0…`), both
extracted to scratch by explicit hash:

```
$ S="<scratch>"; cd /c/s/MS && git show f64f054d9a19ccaf1c91dfbb0024a8f46f986076:ratification_surfaces/cowork_comparison_l2_reading.md > "$S/reading_f64f.md"; git show cf3389d038bf2dfeee86485aa980486b0f6b30ea:ratification_surfaces/cowork_comparison_l2_reading.md > "$S/reading_cf33.md"; echo "exit:$?"; PYTHONUTF8=1 python "$S/a5.py" "$S/reading_f64f.md" "$S/reading_cf33.md" "$S"; echo "exit:$?"
exit:0
base span 2258826 later span 2258827 identical: False
exit:0
$ S="<scratch>"; PYTHONUTF8=1 python "$S/a5.py" "$S/reading_f64f.md" "$S/reading_cf33.md" "$S"; cd /c/s/MS && git hash-object -w "$S/a5_base_span.md"; git hash-object -w "$S/a5_later_span.md"; echo "exit:$?"
base span 2258826 later span 2258826 identical: True
warning: in the working copy of '<scratch>/a5_base_span.md', LF will be replaced by CRLF the next time Git touches it
dce559b1fe976fa87d66170b3a422593900c2def
warning: in the working copy of '<scratch>/a5_later_span.md', LF will be replaced by CRLF the next time Git touches it
dce559b1fe976fa87d66170b3a422593900c2def
exit:0
```

The first run compared the two spans raw and found the later one one byte longer. The extra byte is the newline at
the span's end: the base span ends at the line before `## 7.` and the later span at the separator before
`### 6.29 — `, and the blank line those two boundaries leave differs by one line ending. The check was changed to
trim trailing newlines from both spans and re-run: the spans are then identical, and **both, written into the object
store with `git hash-object -w`, give the same blob, `dce559b1fe976fa87d66170b3a422593900c2def`** (§6, item 6).

### 2.6 The readings applied, and the ones taken new

The placement readings of the earlier batches were applied unchanged, and each member's manifest states the ones it
used: a description of the implementation, and presentation code, QUARANTINED; a build state, a plan, a status or a
past event HISTORICAL; the design of a component the record states as planned HISTORICAL — a plan; an item of a
plan placed by what it names (member 24's first reading); program code read by its code line (member 23's first
reading), a code line with a comment saying what it is or does QUARANTINED and a run of uncommented code lines and
each fence line listed; a statement about a product tool outside the analysis — the tuning tools, the preferences,
the menu actions, the language-model integration, MuseScore's own score model — under *not a statement*; a rule of
how a change is verified, what the ground truth annotates and how the comparison tools grade, RELOCATED to *the
measurement of the analysis*, annotated *(NOT A LAYER)*; a sentence for which no one disposition can be defended
at the two texts UNPLACED with what was read; a label, a heading, a pointer, provenance, a defense, a test record, a
definition of a term and the document's account of itself under *not a statement*; and a later statement of
content an earlier row carries travelling with the earliest row carrying it. **No row of this batch travels with
Row 1.23**, so the sentence the premise ledger orders for such a row was never owed.

**Readings taken new, each stated in its member's manifest so the writing side can check it:**

- **Position 30.** The two code blocks and the text block of §11.3g declare the tuning tools' own types and display;
  each of their lines is listed under *not a statement* as a statement about a product tool outside the analysis,
  the fifth batch's reading governing them, as member 23's second reading listed the lines naming a preference.
  Member 23's code-line reading, written for the analysis's own code, is not applied to them.
- **Position 33.** A sentence about how a development tool is itself built — how it initializes MuseScore's
  modules, what it links against, what it skips when loading a score — says nothing the analysis does, must do, may
  assume or must not do, and is listed under *not a statement* as *the build of a development tool*.

**Where two earlier readings meet, stated so it can be checked** (no reading new):

- **Position 37.** The second batch tabulated glossary entries as statements at member 5, whose glossary defined the
  function layer's own terms and so said what the analysis does; this appendix's entries define standard music
  theory and say nothing the analysis does, must do, may assume or must not do, so the fifth batch's reading — a
  definition of a term is listed — places them, and the member places no outgoing statement.
- **Position 38.** The version history is one line holding the document's successive revision remarks; it is listed as
  one item, the document's account of itself, its quotation elided in the middle as member 28 elided a run of code.

### 2.7 The members done and not done, and what the next member's size suggests

**Done:** positions 29 to 38, each whole. **Not done:** positions 39 to 62 — UNTOUCHED, not partly worked; nothing of
position 39 was read for tabulation, drafted or committed, its entry in the artifact having been read for its size
only, as read (9) orders. **The next writing resumes at position 39**, the passages of `docs/scoring_model.md`, as
the reading file's §0 says. §7, §8, §9 and §14 stay headed NOT YET WRITTEN.

**Position 39's size, against position 23's** (1(h)), read at the artifact:

```
$ python "<scratch>/sizes.py" > "<scratch>/sizes.txt" 2>&1; echo "exit:$?"
exit:0
23 None None lines 817 bytes 58356 ranges 100
29 None None lines 90 bytes 4556 ranges 12
30 None None lines 396 bytes 26335 ranges 68
38 None None lines 27 bytes 13982 ranges 2
39 None None lines 990 bytes 88918 ranges 98
40 None None lines 382 bytes 41085 ranges 25
```

*(The first column is the position; the scratch script printed no path or heading because those fields carry other
names in the artifact; the lines, bytes and range counts are the artifact's. Position 30's line is the evidence for
§7, finding 1.)* Position 39 is larger than position 23 — **990 lines and 88,918 bytes, against 817 lines and 58,356
bytes** — so it is the
largest member met so far, by about a fifth in lines and about half again in bytes. **What the evidence suggests:**
position 23 was finished whole by the sixth batch as its first member, in a context not yet compacted, the
compaction coming after its commit; this batch finished positions 29 to 38 without a compaction, the largest of them
(position 30, 396 lines) among its first two. That is evidence that a fresh session can finish a member of position
23's size whole when it is the first member opened. It is **not** evidence that the same holds at position 39's
size, which no batch has yet met, and the difference in bytes is larger than the difference in lines. This gives
some reason to doubt that a fresh session can finish position 39 whole together with anything after it, and no
evidence either way on whether it can finish position 39 alone. **Nothing is decided here**: the dispatch's rule —
no member split by hand (D-671), the first-member rule of 1(h) — governs the next batch, and what to do about the
size is the writing side's question.

**E1 — MET for every member done**: each manifest; every outgoing statement with exactly one disposition, or
UNPLACED with what was read; every DIFFERS with its one-sentence difference and nothing chosen; the marks of 1(c)
where they apply (none of this batch's members carries a WITHHELD or SEEN home, and the check was made at the
homes); the transfer list, audit questions and proposals gathered; §0 and the §16 progress clause true of the file
at each commit; the banner edit made once; the capacity judgment written out before each member and quoted from the
capacity log; the seven checks run before each commit; no recommendation anywhere; no member beyond position 38
opened; A5 step (i) intact. **One judgment misstates a range count** (§2.1; §7, finding 1).

---

## 3. Task 1A — the corrections, one commit

**The ordered read, taken now and only now:** §6.17's manifest from its heading to its end; §6.22's
`#### Not a statement` list whole and its `#### The arithmetic at this member`; and the lines of §6 that state
reading rule (1) — all from the scratch copy of the last member commit's blob `cf3389d0…`, taken by explicit hash.

**What the read found, so it can be checked.** §6.17's SEEN paragraph ends with the parenthesis the dispatch quotes,
word for word. §6.22's list, read whole, holds **exactly four headings — items 27, 30, 60 and 94**, at
`ARCHITECTURE.md` lines 1435, 1492, 1638 and 2422, the four the dispatch names; **there is no fifth.**

**The correction** was applied to a scratch copy by a scratch script and checked before it was placed:

```
$ S="<scratch>"; PYTHONUTF8=1 python "$S/task1a.py" "$S/reading_cf33.md" "$S/built1a.md"; echo "exit:$?"
Task 1A applied
exit:0
```

**A5 step (ii)** — the `f64f054d…` span against the span of the built file, written into the object store and
compared with `git diff` between the two literal blob hashes:

```
$ S="<scratch>"; PYTHONUTF8=1 python "$S/a5.py" "$S/reading_f64f.md" "$S/built1a.md" "$S"; cd /c/s/MS && git hash-object -w "$S/a5_later_span.md" 2>/dev/null; echo "exit:$?"
base span 2258826 later span 2259451 identical: False
5d1af816f7a898ebf580ba0e30411b3eb77d79fc
exit:0
$ git diff dce559b1fe976fa87d66170b3a422593900c2def 5d1af816f7a898ebf580ba0e30411b3eb77d79fc > "<scratch>/a5ii_diff.txt"; echo "exit:$?"
exit:0
```

```
diff --git a/dce559b1fe976fa87d66170b3a422593900c2def b/5d1af816f7a898ebf580ba0e30411b3eb77d79fc
index dce559b1fe..5d1af816f7 100644
--- a/dce559b1fe976fa87d66170b3a422593900c2def
+++ b/5d1af816f7a898ebf580ba0e30411b3eb77d79fc
@@ -26859,8 +26859,9 @@ L2-S31 and L2-S38 both DIFFERS.)* DIFFERS: 9.3, 9.25, 9.49, 9.108, 9.160(ii), 9.
 > `tools/audit/decisions/backbone_decisions.json`, and located that way **two of the eight lie in this member:
 > D-002, homed at `ARCHITECTURE.md:21-22`, and D-095, homed at `ARCHITECTURE.md:43-44`.** Both are marked below as
 > *SEEN — §6.3 entry 4*. The other six are homed outside `ARCHITECTURE.md`. *(The same located check places D-279's
-> home, `cowork_engage_arc_plan.md:69-72`, inside position 15, whose committed foot says no SEEN home lies there;
-> that member is not re-opened, and the report names it as a finding of this run.)*
+> home, `cowork_engage_arc_plan.md:69-72`, inside position 15. When this member was written, member 15's manifest and
+> foot said no SEEN home lies there; the sixth batch's correction commit `5aea89048e5d4f9f7812b4303b7f2247ce514618`
+> brought its manifest, its foot and Row 15.19 true, and re-opened nothing else of that member.)*
 
 ---
 
@@ -32580,6 +32581,12 @@ regressions." — §3.3, D-GAP (locator: lines 2426–2427).
     its claim is stated by Row 22.129.
 95. "**Facts.**" (2424) — *a label*.
 
+*Items 27, 30, 60 and 94 are headings, listed here in departure from reading rule (1) at the head of §6, under which a
+heading is neither tabulated nor listed. They are kept, and counted in this list's 95, so that the item numbers the
+marks below cite stay as they are; no statement, disposition or verdict of this member depends on them. (The sixth
+batch's report, §7, finding 1, named three of them; the fourth was found at the file by the writing side of the
+seventh batch's dispatch.)*
+
 #### The arithmetic at this member
 
 - Rows written: **131** (22.1 to 22.131).
```

**Every changed passage the diff shows is one Task 1A names, and both passages Task 1A names are among them.** No
other passage of §6.1 to §6.28 moved.

**(i) §6.17's manifest remark on member 15 — before** (as committed at `cf3389d0…`):

```
 > *SEEN — §6.3 entry 4*. The other six are homed outside `ARCHITECTURE.md`. *(The same located check places D-279's
-> home, `cowork_engage_arc_plan.md:69-72`, inside position 15, whose committed foot says no SEEN home lies there;
-> that member is not re-opened, and the report names it as a finding of this run.)*
```

**after:**

```
+> home, `cowork_engage_arc_plan.md:69-72`, inside position 15. When this member was written, member 15's manifest and
+> foot said no SEEN home lies there; the sixth batch's correction commit `5aea89048e5d4f9f7812b4303b7f2247ce514618`
+> brought its manifest, its foot and Row 15.19 true, and re-opened nothing else of that member.)*
```

**(ii) §6.22's four heading items — before:** the list ended at item 95 and was followed, after a blank line, by
`#### The arithmetic at this member`, with no remark on its headings. **After:** one paragraph inserted after item 95
and a blank line:

```
+*Items 27, 30, 60 and 94 are headings, listed here in departure from reading rule (1) at the head of §6, under which a
+heading is neither tabulated nor listed. They are kept, and counted in this list's 95, so that the item numbers the
+marks below cite stay as they are; no statement, disposition or verdict of this member depends on them. (The sixth
+batch's report, §7, finding 1, named three of them; the fourth was found at the file by the writing side of the
+seventh batch's dispatch.)*
```

The word scan of the new wording found no British spelling and no non-musical use of a reserved word; both passages
were read back at the built file. The staged set, the commit and the push:

```
$ S="<scratch>"; python "$S/place.py" "$S/built1a.md"; cd /c/s/MS && git add -- ratification_surfaces/cowork_comparison_l2_reading.md 2>/dev/null; git write-tree; git rev-parse cf3389d038bf2dfeee86485aa980486b0f6b30ea^{tree}; git hash-object --no-filters "$S/built1a.md"; echo "exit:$?"
placed 2697491 bytes
b745f01504ba7d1c29cc5e9ffc755aed3c1e4a3c
7b4b4f72f1f2d7155ac559d4f39e1f0196f35f0a
0ec16901636587336574dddd505f7f1868713281
exit:0
$ git diff --name-status 7b4b4f72f1f2d7155ac559d4f39e1f0196f35f0a b745f01504ba7d1c29cc5e9ffc755aed3c1e4a3c; git ls-tree b745f01504ba7d1c29cc5e9ffc755aed3c1e4a3c -- ratification_surfaces/cowork_comparison_l2_reading.md; git commit -q -m 'comparison L2: member 17 remark and member 22 heading note corrected, no row re-tabulated

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>'; echo "exit:$?"; git push -q origin master; echo "exit:$?"
M	ratification_surfaces/cowork_comparison_l2_reading.md
100644 blob 0ec16901636587336574dddd505f7f1868713281	ratification_surfaces/cowork_comparison_l2_reading.md
exit:0
exit:0
$ git show --stat --format='commit %H%nparent %P%nsubject %s' d08b5f955781785918d9fcee24ad8549d377b6d1; echo "exit:$?"
commit d08b5f955781785918d9fcee24ad8549d377b6d1
parent cf3389d038bf2dfeee86485aa980486b0f6b30ea
subject comparison L2: member 17 remark and member 22 heading note corrected, no row re-tabulated

 ratification_surfaces/cowork_comparison_l2_reading.md | 11 +++++++++--
 1 file changed, 9 insertions(+), 2 deletions(-)
exit:0
```

`.git/refs/remotes/origin/master` then read `d08b5f955781785918d9fcee24ad8549d377b6d1` at its file.

**E1A — MET**: one commit carrying the reading file alone; both passages (i) and (ii) corrected as named, and no other
passage of §6.1 to §6.28 moved (A5 step (ii)); no disposition, verdict, row or item number, or count changed; each
passage before and after above.

---

## 4. Task 2 — the close

**2(a) — the `STATUS.md` entry**, written first, at the top: one pointer entry naming this dispatch by its file name,
with the `Last updated: ` prefix moved to it from the sixth batch's entry, whose opening now reads
`*2026-09-28 (CC — …`. The entry names the members now tabulated by position and by their headings, states that
every disposition is a proposal and nothing is applied, states what the correction commit did without re-tabulating
or renumbering anything, and says the writing stopped at position 38 by the dispatch's order so that position 39
opens the next batch; it restates no count (D-431). **It was word-scanned with the file tools before 2(b)**: the two
hits were *Key*, inside the heading *Appendix A — Key Musical Concepts* named as `ARCHITECTURE.md` writes it — a
quotation of the heading's own name, not a use of the word in the entry's own prose — and *decisions register*, a
qualified use; nothing was changed. *(At the time of the scan the first hit was read as the musical sense; it is not —
the heading's *Key* means *principal* — and the reason it stands is that it is the heading's own name, quoted.)*

**2(b) — the forward bound re-aimed.** `STATUS.md`'s object at this batch's Task 0 commit, at `f64f054d…` and at
Task 1A's commit is the same blob:

```
$ git rev-parse f64f054d9a19ccaf1c91dfbb0024a8f46f986076:STATUS.md b91c56971806e69af6bdccb10198a95d87fd5d05:STATUS.md; echo "exit:$?"
ac5e8a7fcf494095426947cd3ba08d4a0479afd8
ac5e8a7fcf494095426947cd3ba08d4a0479afd8
exit:0
$ git rev-parse d08b5f955781785918d9fcee24ad8549d377b6d1:STATUS.md; echo "exit:$?"; python tools/audit/gen_status_batch_bound.py --apply > "<scratch>/sbb_apply.txt" 2>&1; echo "exit:$?"; python tools/audit/gen_status_batch_bound.py --check > "<scratch>/sbb_check.txt" 2>&1; echo "exit:$?"
ac5e8a7fcf494095426947cd3ba08d4a0479afd8
exit:0
exit:0
exit:0
```

All five authored constants were moved, `MOVE_KIND` staying `"ordinary"` and `RULINGS` unchanged, this batch's
aiming appended to `PREVIOUS_AIMINGS` (the sixth batch's aiming already being its last row, it was not appended
again), and each field's former value named in its comment. The tool against its committed object at Task 1A's
commit, by explicit hash:

```
$ S="<scratch>"; cd /c/s/MS && N=$(git hash-object -w tools/audit/gen_status_batch_bound.py 2>/dev/null); echo "new $N"; git rev-parse d08b5f955781785918d9fcee24ad8549d377b6d1:tools/audit/gen_status_batch_bound.py; echo "exit:$?"
new feaae43fea381577a3c71b2f2ffc9ebdcc2597e1
2326e2d6e3ca65316d6ce0061d2c50a1ac71da90
exit:0
$ S="<scratch>"; cd /c/s/MS && git diff 2326e2d6e3ca65316d6ce0061d2c50a1ac71da90 feaae43fea381577a3c71b2f2ffc9ebdcc2597e1 > "$S/d_tool.txt"; echo "exit:$?"
exit:0
```

```
diff --git a/2326e2d6e3ca65316d6ce0061d2c50a1ac71da90 b/feaae43fea381577a3c71b2f2ffc9ebdcc2597e1
index 2326e2d6e3..feaae43fea 100644
--- a/2326e2d6e3ca65316d6ce0061d2c50a1ac71da90
+++ b/feaae43fea381577a3c71b2f2ffc9ebdcc2597e1
@@ -786,7 +786,33 @@ OUT = os.path.join(HERE, "status_batch_bound.json")
 # tool can identify them** — a declared state and not a STOP, unchanged by this act. **NO COUNT OF
 # THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431): the membership is DERIVED from the entries'
 # own text at the base commit.
-BASE_COMMIT = "1f2366d859991dfe5d0f5026593c8e58d9faa2f3"
+# ★ RE-AIMED 2026-09-29 by `cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md` Task 2, at
+# its 2(b), and ALL FIVE authored inputs moved together, `PREVIOUS_AIMINGS` being appended to rather than
+# replaced (#12) and `MOVE_KIND` staying at the value it already carried, which is the value this move
+# takes. The aiming it replaces is the sixth L2 tabulation batch's, which is ALREADY the last row of
+# `PREVIOUS_AIMINGS` — that batch recorded its own aiming in its own act — so it is not appended a
+# second time, and this batch's aiming is appended instead. `BASE_COMMIT` was
+# `1f2366d859991dfe5d0f5026593c8e58d9faa2f3` and is now
+# `b91c56971806e69af6bdccb10198a95d87fd5d05`: this batch's Task 0 commit, entry 268 and the seventh
+# tabulation dispatch. Neither Task 0 nor any member commit nor the Task 1A correction commit of this
+# batch commits `STATUS.md`, so that commit's `STATUS.md` object is the one the tree carried when this
+# batch opened (`ac5e8a7fcf494095426947cd3ba08d4a0479afd8`, read by explicit hash, D-253) — the same blob
+# at this batch's Task 0 commit and at its parent `f64f054d9a19ccaf1c91dfbb0024a8f46f986076`, established
+# at each — and it carries the sixth tabulation batch's entry at the head of the dated entries.
+#
+# ★★ THE THEN-PREVIOUS BATCH IS THE SIXTH L2 TABULATION. `PREVIOUS_BATCH_DISPATCH` was
+# `cc_instruction_l2_comparison_tabulation_fifth_2026_09_28.md` and now names
+# `cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md`, whose entry names it; that batch wrote
+# its entry and its move inside its own Task 2, and no close ran between it and this batch.
+#
+# **THE DECLARED PREFIX ADJUSTMENT IS EXPECTED TO FIRE**, that entry carrying the `Last updated: `
+# prefix at the base commit, which is why this batch's own entry was written into `STATUS.md` BEFORE
+# `--apply` ran. `ACT_DATE` and the executing dispatch's date AGREE here, both being 2026-09-29.
+# **The second writing's two nameless 2026-09-02 entries remain in `STATUS.md` and no aiming of this
+# tool can identify them** — a declared state and not a STOP, unchanged by this act. **NO COUNT OF
+# THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431): the membership is DERIVED from the entries'
+# own text at the base commit.
+BASE_COMMIT = "b91c56971806e69af6bdccb10198a95d87fd5d05"
 
 # The batch whose entries this aiming moves, named by its dispatch because that is what each of its
 # entries says of itself. On an ORDINARY move it is the THEN-PREVIOUS batch and Ruling 4's forward
@@ -822,7 +848,11 @@ BASE_COMMIT = "1f2366d859991dfe5d0f5026593c8e58d9faa2f3"
 # `cc_instruction_l2_comparison_tabulation_fifth_2026_09_28.md` was the executing act; it is re-stated
 # here for `cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md`, whose then-previous batch is
 # that one.)*
-PREVIOUS_BATCH_DISPATCH = "cc_instruction_l2_comparison_tabulation_fifth_2026_09_28.md"
+# *(`PREVIOUS_BATCH_DISPATCH` read "cc_instruction_l2_comparison_tabulation_fifth_2026_09_28.md" while
+# `cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md` was the executing act; it is re-stated
+# here for `cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md`, whose then-previous batch is
+# that one.)*
+PREVIOUS_BATCH_DISPATCH = "cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md"
 
 # ★ THE ACT DATE IS THE DAY THE MOVE RAN, NOT THE DAY THE DISPATCH WAS WRITTEN. This executing
 # dispatch is dated 2026-09-07 and this batch ran on 2026-09-07, so the two agree; the field is kept
@@ -866,9 +896,12 @@ PREVIOUS_BATCH_DISPATCH = "cc_instruction_l2_comparison_tabulation_fifth_2026_09
 # 2026-09-28, so the two dates agree.)* *(`ACT_DATE` read "2026-09-28" and `DISPATCH`
 # `cc_instruction_l2_comparison_tabulation_fifth_2026_09_28.md` while that batch was the executing act;
 # both are re-stated here for `cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md`, dated
-# 2026-09-28, whose move ran on 2026-09-28, so the two dates agree.)*
-ACT_DATE = "2026-09-28"
-DISPATCH = "cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md"
+# 2026-09-28, whose move ran on 2026-09-28, so the two dates agree.)* *(`ACT_DATE` read "2026-09-28" and
+# `DISPATCH` `cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md` while that batch was the
+# executing act; both are re-stated here for `cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md`,
+# dated 2026-09-29, whose move ran on 2026-09-29, so the two dates agree.)*
+ACT_DATE = "2026-09-29"
+DISPATCH = "cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md"
 # TASK IS A CHOICE, DECLARED RATHER THAN IMPLIED. On an ORDINARY move the executing dispatch orders
 # the move and this batch's own `STATUS.md` entries in the same numbered task, so both halves of "the
 # same act that writes its own entries" sit inside it, and that task is what the archive header names.
@@ -945,7 +978,11 @@ DISPATCH = "cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md"
 # close"* names in those words. It names Task 2 again while
 # `cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md` is the executing act, that dispatch
 # ordering both halves of the close — this batch's own entry at its 2(a) and this move at its 2(b) —
-# inside its own Task 2, which that dispatch's heading *"Task 2 — the close"* names in those words.)*
+# inside its own Task 2, which that dispatch's heading *"Task 2 — the close"* names in those words. It
+# names Task 2 again while `cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md` is the
+# executing act, that dispatch ordering both halves of the close — this batch's own entry at its 2(a)
+# and this move at its 2(b) — inside its own Task 2, which that dispatch's heading *"Task 2 — the
+# close"* names in those words.)*
 TASK = "Task 2"
 # ★ WHAT KIND OF MOVE THIS AIMING PERFORMS. Two values and no others.
 #   "ordinary"  — the move Ruling 4's forward clause describes: the then-previous batch's entries,
@@ -1375,6 +1412,10 @@ PREVIOUS_AIMINGS = [
      "base_commit": "1f2366d859991dfe5d0f5026593c8e58d9faa2f3",
      "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_fifth_2026_09_28.md",
      "the_kind_of_move": "ordinary"},
+    {"executing_act": "cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md, Task 2",
+     "base_commit": "b91c56971806e69af6bdccb10198a95d87fd5d05",
+     "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md",
+     "the_kind_of_move": "ordinary"},
 ]
 
 HEADER_ORDINARY = (
```

`--apply`, then `--check`:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 2,908 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

```
  entries moved: 1, 2,908 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**The prediction held.** Read at the files with the file tools (a green `--check` is not the proof, OI-379): exactly
the sixth batch's ONE entry moved — the entry naming
`records/cc/instructions/cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md`, from which the `Last
updated: ` prefix had been moved at 2(a) — and it now stands in `STATUS_ARCHIVE.md` under the header
*"★ RULING 4's FORWARD BOUND, 2026-09-29."*, which names this dispatch's Task 2. `STATUS.md` keeps this batch's
entry and the two 2026-09-02 entries. No STOP.

**2(c) — the regenerations**, each then `--check`, all exit 0, the last after the final edit to `STATUS.md`:

```
$ S="<scratch>"; cd /c/s/MS && for g in gen_evidence_pin_membership gen_l0_l1_outgoing_population gen_l2_outgoing_population gen_defense_share gen_session_start_read_size; do echo "=== $g"; python tools/audit/$g.py; echo "gen exit:$?"; python tools/audit/$g.py --check; echo "check exit:$?"; done > "$S/regen.txt" 2>&1; echo "exit:$?"
exit:0
```

```
=== gen_evidence_pin_membership
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
gen exit:0
the evidence pin's class membership re-derives
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
check exit:0
=== gen_l0_l1_outgoing_population
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
gen exit:0
l0_l1_outgoing_population.json re-derives
check exit:0
=== gen_l2_outgoing_population
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
gen exit:0
l2_outgoing_population.json re-derives
check exit:0
=== gen_defense_share
wrote tools/audit/defense_share.json
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   39804  ( 8.72%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (104609): 12.39%
    of the whole session-start read (247392): 5.24%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
gen exit:0
the defense-share measurement re-derives
  row Why followed by a space, a colon or a comma          matched  31  (bold 0, italic 31)
  row Evidence followed by a colon                         matched   1  (bold 0, italic 1)
  row Founding instance followed by a colon or a comma     matched   2  (bold 1, italic 1)
  Guiding principles                                      3099 of   26908  (11.52%)  in 7 clause(s)
  The open-items register                                 3041 of   14816  (20.53%)  in 6 clause(s)
  The decisions register                                  3345 of   17109  (19.55%)  in 11 clause(s)
  This block                                                 0 of    5213  ( 0.00%)  in 0 clause(s)
  Conventions                                             3472 of   39804  ( 8.72%)  in 10 clause(s)
  The self-check after every coding exercise                 0 of     759  ( 0.00%)  in 0 clause(s)
  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends
    the ruled closing reading would attribute 51684; the literal paragraph reading 160906
    of the six session-start spans (104609): 12.39%
    of the whole session-start read (247392): 5.24%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
check exit:0
=== gen_session_start_read_size
wrote tools/audit/session_start_read_size.json
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              39804
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 168350, the six session-start spans 104609, overstated by 63741
    CLAUDE.md                                                                104609
    STATUS.md                                                                 12230
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 247392
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 247392 [ruled membership]  (-119729, -32.61%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 247392 [ruled membership]  (-49440, -16.66%)  <- CROSSES A REGIME BOUNDARY
gen exit:0
the session-start read measurement re-derives
  rule (a) points at tools/audit/nongating_apparatus_rows.json -> ★_the_live_gating_answer -> gating_ids
  CLAUDE.md is read under the regime: ruled membership
    [session start] Guiding principles                                       26908
    [session start] The open-items register                                  14816
    [session start] The decisions register                                   17109
    [session start] This block                                                5213
    [session start] Conventions                                              39804
    [session start] The self-check after every coding exercise                 759
    [conditional  ] Project context                                            260
    [conditional  ] Autonomous operation — composing module                   1261
    [conditional  ] Build and test commands                                   6489
    [conditional  ] Gate threshold and preset policy                         47180
    [conditional  ] Scoring model                                             3583
    [conditional  ] Score corpora                                              408
    [conditional  ] Local patches — do not revert                             6676
    [conditional  ] VS Code extension — bash command rules                    3013
  whole file 168350, the six session-start spans 104609, overstated by 63741
    CLAUDE.md                                                                104609
    STATUS.md                                                                 12230
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 247392
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 247392 [ruled membership]  (-119729, -32.61%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 247392 [ruled membership]  (-49440, -16.66%)  <- CROSSES A REGIME BOUNDARY
check exit:0
```

Each artifact's committed blob at Task 1A's commit against the new blob, the new blobs written into the object store
with `git hash-object -w`:

```
$ for f in evidence_pin_membership l0_l1_outgoing_population l2_outgoing_population defense_share session_start_read_size status_batch_bound guard_state; do echo "$f $(git rev-parse d08b5f955781785918d9fcee24ad8549d377b6d1:tools/audit/$f.json) $(git hash-object -w tools/audit/$f.json 2>/dev/null)"; done; echo "exit:$?"
evidence_pin_membership 54f774d82a2d2e5a9ec99b13666bd83d63ac5257 54f774d82a2d2e5a9ec99b13666bd83d63ac5257
l0_l1_outgoing_population e310fb57ac53f9a06f8a9295d70c17ec143e3ce3 e310fb57ac53f9a06f8a9295d70c17ec143e3ce3
l2_outgoing_population 6b62ebd223370aff2c3cec60983ba7e6d806b1dd 8d88bab3ecc78bd60249430a218eafeaadb580c0
defense_share 15b81bc389d2091cda5e7b1995a355c444eaee6b d9be5534e2d31961de19e8b119f58d97c8f5cad0
session_start_read_size 9e8a3e4817697475d67c75a5fe5e3df3736c57fa 160d6673dba6336eb6188a66ec3f1f7eb5013fe5
status_batch_bound 424d01a65e9baf1d217be316ec845b52cc34667a 135beaebaf28653b44107b17c9e8c459263ae2eb
guard_state 8d11ee777fff3cd1e2617b6a80ad70d87f851440 8d11ee777fff3cd1e2617b6a80ad70d87f851440
exit:0
```

`evidence_pin_membership.json` and `l0_l1_outgoing_population.json` **did not move**. For the four that moved, both
blobs were compared line by line with `git diff` between their two literal hashes:

```
$ S="<scratch>"; cd /c/s/MS && git diff 6b62ebd223370aff2c3cec60983ba7e6d806b1dd 8d88bab3ecc78bd60249430a218eafeaadb580c0 > "$S/d_l2pop.txt"; git diff 15b81bc389d2091cda5e7b1995a355c444eaee6b d9be5534e2d31961de19e8b119f58d97c8f5cad0 > "$S/d_defense.txt"; git diff 9e8a3e4817697475d67c75a5fe5e3df3736c57fa 160d6673dba6336eb6188a66ec3f1f7eb5013fe5 > "$S/d_ssrs.txt"; git diff 424d01a65e9baf1d217be316ec845b52cc34667a 135beaebaf28653b44107b17c9e8c459263ae2eb > "$S/d_sbb.txt"; echo "exit:$?"
exit:0
```

`l2_outgoing_population.json`:

```
diff --git a/6b62ebd223370aff2c3cec60983ba7e6d806b1dd b/8d88bab3ecc78bd60249430a218eafeaadb580c0
index 6b62ebd223..8d88bab3ec 100644
--- a/6b62ebd223370aff2c3cec60983ba7e6d806b1dd
+++ b/8d88bab3ecc78bd60249430a218eafeaadb580c0
@@ -40138,7 +40138,7 @@
        "line_number": 8,
        "term": "boundary",
        "tier": "admitting",
-       "line": "*Last updated: 2026-09-28 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 23: POSITIONS 23 TO 28 — THE `ARCHITECTURE.md` PASSAGES UNDER *4. Existing Components — The Analysis Foundation*, *5. Planned Analysis Extensions*, *6. The Style System*, *7. The Knowledge Base*, *8. Planned Generation Components* AND *9. The Constraint System*, EACH WHOLE — ARE NOW TABULATED, AND POSITIONS 29 ONWARD ARE UNTOUCHED.** ★ **THE RECORDS ARE COMMITTED** — this dispatch and `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_seven.md`. ★ **THE READING FILE `ratification_surfaces/cowork_comparison_l2_reading.md` IS EXTENDED MEMBER BY MEMBER, ONE COMMIT EACH**: every outgoing statement of positions 23 to 28 is placed under exactly one proposed disposition beside the current-text axis, only the lines inside each member's published ranges tabulated, and the file's transfer list, audit questions, proposals and distribution updated in each member's commit. ★ **ONE CORRECTION COMMIT BROUGHT MEMBER 15'S SEEN MARK AND SIX FEET TRUE WITHOUT RE-TABULATING ANY ROW**: the check made at the homes finds D-279's home inside member 15, and its manifest, its foot and the one row reaching that home now say so; the feet of members 11 to 16 lose a malformed generated sentence. No disposition, verdict or count moved, and the file's other earlier members are unchanged at the objects. ★ **THE WRITING STOPPED AT THE MEMBER BOUNDARY AFTER POSITION 28** under the dispatch's capacity judgment: position 29, the `ARCHITECTURE.md` passages under *10. Visualization*, was judged not finishable together with the close in the context that remained, the context having been compacted once already, inside position 24's work after its text was read and before its rows were drafted; positions 29 onward are UNTOUCHED, not partly worked (D-672), and the file's own §0 says where the next writing resumes. ★ **THREE FINDINGS ARE REPORTED AND LEFT AT THEIR SITES**, a committed member never being re-opened beyond the correction the dispatch names; the report names them. ★★ **EVERY DISPOSITION IS A PROPOSAL AND NOTHING IS APPLIED**: no outgoing text, derivation, brief, boot pack or decisions register was edited; the five questions the derivation marks for the user are not put; no recommendation is made anywhere. No session booted; no open-items row created, flipped or discarded; no decisions-register identity allocated; no tool source edited but the forward bound's authored aiming; no governing document amended but this file and its archive; no `src/` file, build, test, golden, corpus of scores or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_l2_comparison_tabulation_sixth_2026_09_28.md` — and no count is restated here (**D-431**).)*"
+       "line": "*Last updated: 2026-09-29 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 29: POSITIONS 29 TO 38 — THE `ARCHITECTURE.md` PASSAGES UNDER *10. Visualization*, *11. Intonation*, *12. User Interface*, *14. ML Readiness*, *15. Development Phases*, *16. Scope Reference*, *18. Contributing*, *19. LLM Integration — Claude Composer*, *Appendix A — Key Musical Concepts* AND *Appendix B — MuseScore Score Model Quick Reference*, EACH WHOLE — ARE NOW TABULATED, AND POSITIONS 39 ONWARD ARE UNTOUCHED.** ★ **THE RECORDS ARE COMMITTED** — this dispatch and `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_eight.md`. ★ **THE READING FILE `ratification_surfaces/cowork_comparison_l2_reading.md` IS EXTENDED MEMBER BY MEMBER, ONE COMMIT EACH**: every outgoing statement of positions 29 to 38 is placed under exactly one proposed disposition beside the current-text axis, only the lines inside each member's published ranges tabulated, and the file's transfer list, audit questions, proposals and distribution updated in each member's commit. ★ **ONE CORRECTION COMMIT BROUGHT MEMBER 17'S REMARK ON MEMBER 15 TRUE AND MARKED MEMBER 22'S FOUR HEADING ITEMS, WITHOUT RE-TABULATING OR RENUMBERING ANYTHING**: the remark now says the sixth batch's correction commit brought member 15's manifest, foot and SEEN row true, and a note under member 22's list says which of its items are headings kept in departure from the file's first reading rule. No disposition, verdict, row or item number, or count moved, and the file's other earlier members are unchanged at the objects. ★ **THE WRITING STOPPED AT THE MEMBER BOUNDARY AFTER POSITION 38 BY THE DISPATCH'S ORDER**, so that position 39, the passages of `docs/scoring_model.md`, opens the next batch with nothing in front of it (D-670); positions 39 onward are UNTOUCHED, not partly worked (D-672), and the file's own §0 says where the next writing resumes. ★ **THE RUN'S FINDINGS AND DECLARED DEPARTURES ARE REPORTED AND LEFT AT THEIR SITES**, a committed member never being re-opened beyond the correction the dispatch names; the report names them. ★★ **EVERY DISPOSITION IS A PROPOSAL AND NOTHING IS APPLIED**: no outgoing text, derivation, brief, boot pack or decisions register was edited; the five questions the derivation marks for the user are not put; no recommendation is made anywhere. No session booted; no open-items row created, flipped or discarded; no decisions-register identity allocated; no tool source edited but the forward bound's authored aiming; no governing document amended but this file and its archive; no `src/` file, build, test, golden, corpus of scores or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_l2_comparison_tabulation_seventh_2026_09_29.md` — and no count is restated here (**D-431**).)*"
       },
       {
        "line_number": 10,
```

The one changed line is the hit record at line 8 of `STATUS.md`, inside the entry for `STATUS.md` in
`the_residue_for_the_mining_map` — the new entry replacing the sixth batch's at that line. **No member of the
outgoing population or of the tabulation population moved, and no file entered or left the population or the
residue.**

`defense_share.json`:

```
diff --git a/15b81bc389d2091cda5e7b1995a355c444eaee6b b/d9be5534e2d31961de19e8b119f58d97c8f5cad0
index 15b81bc389..d9be5534e2 100644
--- a/15b81bc389d2091cda5e7b1995a355c444eaee6b
+++ b/d9be5534e2d31961de19e8b119f58d97c8f5cad0
@@ -77,7 +77,7 @@
  ],
  "the_denominators_both_re_derived_through_the_imported_reader_at_this_tree": {
   "the_six_session_start_spans": 104609,
-  "the_whole_ordinary_session_start_read": 247347,
+  "the_whole_ordinary_session_start_read": 247392,
   "why_two": "the first says how much of what a session reads OF `CLAUDE.md` is marked defense; the second says how much of the WHOLE boot it is. A share quoted against one of them is not the share against the other."
  },
  "per_span": [
```

`session_start_read_size.json`:

```
diff --git a/9e8a3e4817697475d67c75a5fe5e3df3736c57fa b/160d6673dba6336eb6188a66ec3f1f7eb5013fe5
index 9e8a3e4817..160d6673db 100644
--- a/9e8a3e4817697475d67c75a5fe5e3df3736c57fa
+++ b/160d6673dba6336eb6188a66ec3f1f7eb5013fe5
@@ -176,11 +176,11 @@
   },
   "characters_per_member": {
    "CLAUDE.md": 104609,
-   "STATUS.md": 12185,
+   "STATUS.md": 12230,
    "DECISIONS.md": 127727,
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids": 2826
   },
-  "total_characters": 247347,
+  "total_characters": 247392,
   "further_spans_of_the_same_artifact_NOT_counted_into_the_read": {
    "tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows": {
     "characters": 62498,
@@ -276,10 +276,10 @@
    "from_commit": "1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
    "from_total": 367121,
    "from_regime": "whole-file practice",
-   "to_total": 247347,
+   "to_total": 247392,
    "to_regime": "ruled membership",
-   "change_in_characters": -119774,
-   "change_percent": -32.63,
+   "change_in_characters": -119729,
+   "change_percent": -32.61,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   },
@@ -287,10 +287,10 @@
    "from_commit": "594074e1e1900079e449d2b79a38920d21bca6e6",
    "from_total": 296832,
    "from_regime": "whole-file practice",
-   "to_total": 247347,
+   "to_total": 247392,
    "to_regime": "ruled membership",
-   "change_in_characters": -49485,
-   "change_percent": -16.67,
+   "change_in_characters": -49440,
+   "change_percent": -16.66,
    "★_this_comparison_crosses_a_regime_boundary": true,
    "what_that_means_here": "the two sides answer DIFFERENT questions — one side counts the whole of `CLAUDE.md` because that was the practice there, the other counts only the spans the ruled membership names — so the change is not a saving one act made, and must not be read as one"
   }
```

Both move only in what `STATUS.md`'s new size moves.

`status_batch_bound.json`:

```
diff --git a/424d01a65e9baf1d217be316ec845b52cc34667a b/135beaebaf28653b44107b17c9e8c459263ae2eb
index 424d01a65e..135beaebaf 100644
--- a/424d01a65e9baf1d217be316ec845b52cc34667a
+++ b/135beaebaf28653b44107b17c9e8c459263ae2eb
@@ -1,7 +1,7 @@
 {
  "what_this_is": "RULING 4's FORWARD BOUND, applied at one batch close: which of the then-previous batch's STATUS.md entries moved to the archive, and the mechanical proof that nothing was lost or altered in transit (#12). Every figure here is computed; none is transcribed (D-431).",
  "generated_by": "tools/audit/gen_status_batch_bound.py",
- "dispatch": "cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md, Task 2",
+ "dispatch": "cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md, Task 2",
  "★_every_previous_aiming_of_this_tool_kept_rather_than_replaced": [
   {
    "executing_act": "cc_instruction_preparation_sixth.md, Task 1",
@@ -441,22 +441,28 @@
    "base_commit": "1f2366d859991dfe5d0f5026593c8e58d9faa2f3",
    "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_fifth_2026_09_28.md",
    "the_kind_of_move": "ordinary"
+  },
+  {
+   "executing_act": "cc_instruction_l2_comparison_tabulation_seventh_2026_09_29.md, Task 2",
+   "base_commit": "b91c56971806e69af6bdccb10198a95d87fd5d05",
+   "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md",
+   "the_kind_of_move": "ordinary"
   }
  ],
  "the_ruling": "Ruling 4 of cowork_rulings_2026_08_17_governing_surface_split.md: an entry is SUPERSEDED the moment a later batch's close exists; the site keeps only the latest batch's entries, and every future batch close moves the then-previous batch's entries in the same act that writes its own.",
- "base_commit": "1f2366d859991dfe5d0f5026593c8e58d9faa2f3",
- "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_fifth_2026_09_28.md",
+ "base_commit": "b91c56971806e69af6bdccb10198a95d87fd5d05",
+ "the_then_previous_batch": "cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md",
  "the_kind_of_move": "ordinary",
  "entries_moved": 1,
- "characters_moved": 2603,
+ "characters_moved": 2908,
  "the_moved": [
   {
    "line_at_base": 8,
-   "characters": 2603,
-   "sha256": "c8a34def290a24ef50708ff1034829090ad5531a278c13eb6ff98576ac101fe1",
+   "characters": 2908,
+   "sha256": "71969d0d7cc1e903c1a6f25ca3baef26a910e87d51485de711038afe2bcbbe51",
    "membership": "names the dispatch",
    "the_one_declared_adjustment_applied": true,
-   "opening": "*2026-09-28 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_fifth_2026_09_28.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITIO"
+   "opening": "*2026-09-28 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_sixth_2026_09_28.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITIO"
   }
  ],
  "reconciliation": {
```

It moves by the re-aim alone. **Against A3: every movement is one A3 names, and there is no other.**

**2(d) — the closing guard capture**, by the invocation that writes, saved outside the repository, under the
environment 0(f) recorded — Git Bash, with `PYTHONIOENCODING` removed from the command's environment by `env -u`
(it was already not set), Python 3.14.3. It was launched as a background command, and its output is quoted from the
scratch file it wrote:

```
$ S="<scratch>"; cd /c/s/MS && env -u PYTHONIOENCODING python tools/audit/gen_guard_state.py > "$S/guard_close.txt" 2>&1; echo "exit:$?"
Command running in background with ID: bs4roqy70. Output is being written to: C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\e956339b-905e-44b6-889d-140afb8cc350\tasks\bs4roqy70.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains C:\s\MS; directory changes made by the backgrounded command do not apply to subsequent commands.
```

The background task then exited with code 0, its output file reading `exit:0`. The capture, verbatim:

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
  [PASS] tools/audit/gen_evidence_pin_membership.py --check
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
80 guard(s) run, 12 failing, 4 not run, 19 historical record(s)
```

Verdict by verdict against 0(f), by a scratch script comparing the two saved captures line by line:

```
opening verdict lines 103 closing verdict lines 103
PASS open 68 close 68
FAIL open 12 close 12
NOT RUN open 4 close 4
HISTORICAL open 19 close 19
FAIL set identical: True
verdict lines differing: 0
```

Then the classification:

```
$ S="<scratch>"; cd /c/s/MS && env -u PYTHONIOENCODING python tools/audit/gen_guard_classification.py > "$S/guardclass_close.txt" 2>&1; echo "exit:$?"; G=$(git hash-object -w tools/audit/guard_state.json 2>/dev/null); echo "new guard_state blob $G"; git rev-parse d08b5f955781785918d9fcee24ad8549d377b6d1:tools/audit/guard_state.json; echo "exit:$?"
exit:2
new guard_state blob 5ba6375f905dfd6fb808669b06b3714660a44794
8d11ee777fff3cd1e2617b6a80ad70d87f851440
exit:0
$ S="<scratch>"; cd /c/s/MS && git diff 8d11ee777fff3cd1e2617b6a80ad70d87f851440 5ba6375f905dfd6fb808669b06b3714660a44794 > "$S/d_guard.txt"; echo "exit:$?"
exit:0
```

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

— exactly the four tools of the FACT. `tools/audit/guard_state.json` against its committed object at Task 1A's
commit:

```
diff --git a/8d11ee777fff3cd1e2617b6a80ad70d87f851440 b/5ba6375f905dfd6fb808669b06b3714660a44794
index 8d11ee777f..5ba6375f90 100644
--- a/8d11ee777fff3cd1e2617b6a80ad70d87f851440
+++ b/5ba6375f905dfd6fb808669b06b3714660a44794
@@ -1041,7 +1041,7 @@
       "exit_code": 0,
       "verdict": "PASS",
       "stdout": [
-        "  entries moved: 1, 2,603 characters",
+        "  entries moved: 1, 2,908 characters",
         "  byte-present in the archive exactly once: True",
         "  absent from the must-read:                True"
       ],
@@ -1161,15 +1161,15 @@
         "    [conditional  ] VS Code extension — bash command rules                    3013",
         "  whole file 168350, the six session-start spans 104609, overstated by 63741",
         "    CLAUDE.md                                                                104609",
-        "    STATUS.md                                                                 12185",
+        "    STATUS.md                                                                 12230",
         "    DECISIONS.md                                                             127727",
         "    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826",
-        "  total at the tree 247347",
+        "  total at the tree 247392",
         "  further spans of the same artifact, NOT counted into the read:",
         "    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498",
         "    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951",
-        "  vs 1760d9a4a8: 367121 [whole-file practice] -> 247347 [ruled membership]  (-119774, -32.63%)  <- CROSSES A REGIME BOUNDARY",
-        "  vs 594074e1e1: 296832 [whole-file practice] -> 247347 [ruled membership]  (-49485, -16.67%)  <- CROSSES A REGIME BOUNDARY"
+        "  vs 1760d9a4a8: 367121 [whole-file practice] -> 247392 [ruled membership]  (-119729, -32.61%)  <- CROSSES A REGIME BOUNDARY",
+        "  vs 594074e1e1: 296832 [whole-file practice] -> 247392 [ruled membership]  (-49440, -16.66%)  <- CROSSES A REGIME BOUNDARY"
       ],
       "stderr": [],
       "what_it_checks": "what an ordinary session reads at session start, in characters, measured at the tree and at the recorded earlier commit's git object. It is the arc's own subject made checkable: the pruning direction of 2026-08-16 is about this number, and every act in the arc has had to state what it saved. Its load-bearing STOP is a demand about the tree AS IT STANDS — rule (a)'s artifact-and-key pointer is PARSED FROM THE CLAUSE ITSELF and must RESOLVE in the artifact it names, so a pointer that has stopped resolving fails on the day it stops rather than being hidden inside a number. It goes red when a governing surface changes, which is the point: the session-start read moved and the record does not yet say so. ★ WHAT IT DOES NOT ASSERT: that the membership is complete — it is AUTHORED, and each member carries the clause that makes it one so the authored half is checkable by reading three clauses; and nothing about whether the read is small enough, which is [[OI-370]]'s own subject"
@@ -1195,7 +1195,7 @@
         "  TOTAL 12957 character(s) in 34 clause(s), at the AUTHORED ends",
         "    the ruled closing reading would attribute 51684; the literal paragraph reading 160906",
         "    of the six session-start spans (104609): 12.39%",
-        "    of the whole session-start read (247347): 5.24%",
+        "    of the whole session-start read (247392): 5.24%",
         "  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,",
         "  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md)."
       ],
```

The file moves only in the three tools' output lines that `STATUS.md`'s new size and the forward bound's new move
change — the same shape the sixth batch's close recorded. **E2 — MET**: population 80; zero STOPs in the runner; the
failing set exactly the twelve named, plus none; the NOT RUN and HISTORICAL lines identical to 0(f); the
classification STOP unchanged.

**2(e)** — this report. **Task 3** commits it with the close; the close commit's hash is not in this report, which
cannot contain it: see the git log for the commit with the subject
`Close: the L2 tabulation continued from position 29, under its dispatch`.

---

## 5. The assumptions, graded

- **A1 — HELD**, established by the enumeration at 0(c): exactly one tracked modification,
  `tools/audit/claude_md_finer_archive.json`, standing and not chased; the two untracked landing paths; the standing
  untracked population. At the close, the tracked paths differing from Task 1A's commit are the Task 2 files and that
  one standing modification, measured at Task 3; the standing modification is held back from the close.
- **A2 — HELD**: the opening capture shows exactly the twelve FAIL verdicts, and
  `gen_evidence_pin_membership.py --check` passes there.
- **A3 — HELD**, measured at 2(c) line by line.
- **A4 — HELD**: no tool added, none enrolled; the one tool source touched is
  `tools/audit/gen_status_batch_bound.py`'s authored aiming; `gen_l2_outgoing_population.py` and
  `gen_guard_state.py` are not edited; population 80 at both captures.
- **A5 — HELD**, at the objects, in both steps: step (i) at §2.5, step (ii) at §3. The batch's commits touched only
  the reading file and the two landed records until the close (§2.4), so the derivation and the brief (verified at
  0(g)), the pack and its artifact, the input contract, the L0/L1 reading file, every outgoing text, the generator
  sources named and every governing document are unchanged by them until the close, which adds only `STATUS.md` and
  `STATUS_ARCHIVE.md` among governing documents; §6.1 to §6.28 are byte-identical but for Task 1A's two named
  passages.

---

## 6. Declared departures

1. **The dispatch was read before the derivation, and before it was pinned** (P-2), because the opening instruction
   named it and it was the file that said what to do; its first read returned it up to line 658, and the remainder
   was read after the derivation. The pin at 0(a) and the hash at staging are the same blob.
2. **§10 to §16 of the reading file were not read whole at the opening read (read (10))**: §11 and §12 were read at
   their heads and their ends and not through their middles — the lines holding the earlier members' audit
   questions and proposals. What this batch appended to those sections was placed by the build check, which proves
   §6.1 up to the previous member and the §10 to §12 entries against the parent blob, and was read back in the built
   file; nothing in them was moved.
3. **Reads beyond the ordered set, of §6.1 to §6.28**: targeted searches and short reads of earlier members' rows
   and manifests, on the scratch copy of the reading file taken at `b91c5697…` by explicit hash, to find the earliest
   row a new statement travels with, the row an *"as at"* names, and the wording in which an earlier manifest states
   a reading this batch applies; and, for §7, finding 2, the rows of the three flags. None of those rows was edited
   or re-tabulated. Read (10) orders *"Do NOT re-read §6.1 to §6.28 otherwise"*; the travelling rule the dispatch
   also orders cannot be applied without finding the earlier row, so the reads are declared rather than avoided. The
   read of §6.28 whole ran on into the first lines of `## 7.`, which is headed NOT YET WRITTEN.
4. **Shell variables in commands that fed a displayed value**: at Task 0's last-bytes check (`A=$(…)`, `B=$(…)`,
   quoted at 0(d)) and at position 31's staging (`T=$(git write-tree)`, echoed for display). Every `git diff` that
   proved a staged set ran between two literal hashes.
5. **Position 36's range check ran before its capacity judgment was written out**: the scratch viewer's range check
   for position 36 ran inside position 35's call, printing the member's range count and first and last lines to
   nowhere — its output was sent to the null device and not viewed. No text of position 36 was read before its
   judgment was written.
6. **A5 step (i)'s comparison was changed after its first run** to trim trailing newlines from both spans (§2.5).
   Both spans then give the same blob.
7. **One stray heredoc-fed Python command ran during position 33** — `python - <<'EOF'` with an empty body, naming no
   path. It waited on its input past the shell tool's time limit, was moved to the background, and was stopped.
   Scratch checks were otherwise run as script files with absolute paths.
8. **The shell calls quoted in this report are extracted from the session's transcript file** by a scratch script
   that prints each call with its result; they are quoted as extracted, not retyped. The saved outputs are quoted
   from the files the run wrote.
9. **A command the guard denied**: a `sed` over a scratch script, whose path sat in a shell variable, during
   position 29; the edit was made with the file tools instead.
10. **Scratch scripts were run with `PYTHONUTF8=1`** where they printed text outside the console's code page, after
    one of them failed to print under the default. The guard runner and every repository tool ran without it.
11. **The closing guard capture ran in the background** and was compared with the opening one from the saved files
    (§4, 2(d)). While it ran, the running Python processes were listed with PowerShell to see which guard tool it had
    reached, and the session waited on the runner's process to exit; neither read a file. The closing capture named
    `env -u PYTHONIOENCODING` where the opening capture relied on the variable not being set; the variable was not set
    at either.

---

## 7. Findings of the run

1. **The capacity judgment for position 30 misstates its range count** — *"fifty-one ranges"*, where the artifact's
   range list is longer (§2.7's listing). Its `lines` and `bytes` are right. The log stands as written, and the finding is reported here.
2. **Three rows of earlier members are flagged by the consistency check at every run of this batch, and each was read
   at its row.**
   - **Row 7.94**, *"AGREES — as at Row 7.93"* on L2-S34: Row 7.93 reads *"L2-S34: **AGREES**"*, so the two rows
     agree; the flag is the script's own limit.
   - **Row 17.1(iii)**, *"travelling with Row 1.1(i)"*: its disposition, *"ADOPTED — proposed"*, is wrapped across a
     line break inside its bold, which the script does not parse; Row 1.1(i) carries the same disposition. The flag
     is the script's own limit.
   - **Row 7.168**, *"L2-S20: **AGREES** — as at Row 7.167, the spelled degrees being among the tonality terms'
     evidence"*: Row 7.167 carries L2-S20 with the verdict **DIFFERS**. Read in place, Row 7.168's *"as at"* points at
     the words of L2-S20 that Row 7.167 quotes, not at its verdict; but the reading file's own use of *"as at Row M.n"*
     elsewhere names a row with the same derived statement and the same verdict, so this one departs from that use.
     **Left at its site**, §6.1 to §6.28 not being re-opened beyond Task 1A's passages.
3. **Three identifiers named in member 29's text — `SegmentationStepCallback`, `SegmentationStepEvent` and
   `IHarmonicMap` — are defined nowhere under `src/`**, by a search with the file tools. The search was used only to
   confirm that §10 describes planned components, as its own correction says; the reading file does not cite it.

No defect in the comparison apparatus was met: every member's document existed at its path, every published range's
first and last line matched the file, and every outgoing text parsed into statements.

---

## 8. What this batch did NOT do

- **No decision** on any disposition, any difference, any open question, the derivation or the method; no verdict on
  the deriving session's independence; no session booted; no measurement built or run.
- **No edit** to the derivation, the brief, the pack or its artifact, the input contract, the L0/L1 reading file, any
  outgoing text, any governing document other than `STATUS.md` and `STATUS_ARCHIVE.md`, any source of the decisions
  register or of the open-items register, or `tools/audit/gen_l2_outgoing_population.py`.
- **No disposition applied anywhere**, and no recommendation anywhere. The five ★ questions (OQ-L2-2, 4, 5, 8 and 16)
  are listed, ungraded, and put to nobody. §6.1 to §6.28 were not re-opened beyond Task 1A's named passages.
- **No act on Rows 11.67, 11.70(ii) or 1.23**, and **none on Rows 24.30, 24.57, 24.58(i) or 24.72**; no row of this
  batch travels with Row 1.23. *(Row 33.10 travels with Row 24.57 and carries the annotation "(NOT A LAYER)" itself;
  that is a pointer to the earlier row and not an act on it.)*
- **No open-items row** created, flipped or discarded; no decisions-register identity allocated; no finding number.
- **No `src/` edit, no golden, no test changed, moved or run, no build**; nothing under `tools/corpus/`,
  `tools/robust_stop/` or `tools/dcml/`.
- **No tool source touched** but the authored aiming of `gen_status_batch_bound.py`; no guard tool added or enrolled;
  no member split by hand and none skipped; no member beyond position 38 opened.

**The plan's tell, in one sentence:** this batch produced nothing other than the landed records, the reading file's
new member subsections with their updates to §0, §10 to §13 and the §16 progress clause and the one banner edit,
Task 1A's corrections, the Task 2 files and this report — and, outside any commit, the loose blobs that
`git hash-object -w` wrote into the object store for the comparisons by explicit hash.

---

## 9. Self-check — the standing clause, run over the work on disk

Each member subsection was checked before its commit as §2.3 describes, on the built file and not on the draft
alone, and the reading file placed in the repository was the checked build, byte for byte, its blob hash read before
staging. Task 1A's diff was read whole at the blob level (§3). The `STATUS.md` entry was word-scanned before the
forward bound ran, and the re-aim's comments were read back against the sixth batch's shape. This report was
word-scanned after it was built, its code blocks filled from the saved output files by a scratch script rather than
typed. The staged set of the close is proved by explicit path at Task 3. **Against the principles:** no disposition
is applied (#19 — the reading file is authored evidence, re-placeable at the quoted texts); nothing is dropped (#12 —
Task 1A's former wordings stand in git and are quoted above; the findings are left at their sites and written here);
one path per concern is kept (#6 — each reading is stated once, in its member's manifest); and every departure from
the dispatch's route is declared above rather than smoothed over.
