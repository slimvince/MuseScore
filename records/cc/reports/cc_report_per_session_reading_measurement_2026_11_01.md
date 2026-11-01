# CC report — the per-session reading measurement (step 1 of the pruning iteration): TASK 1 STOPPED BEFORE ITS COMMIT — NOTHING MEASURED, NOTHING OF THE TOOL COMMITTED; Task 0 landed; the close and the end state run in the standing form (2026-11-01)

**Dispatch:** `records/cc/instructions/cc_instruction_per_session_reading_measurement_2026_11_01.md`, pinned at Task 0 as blob
`6c675cf77119f7faac1a5bb0d3590c9e19aca7d6` (119,040 bytes by `git cat-file -s`). **This report decides nothing.** It
proposes no fate for any span, makes no recommendation about any member, any span or the pruning iteration, and authors no
class or verdict.

**In one paragraph.** Task 0 landed the dispatch and entries 461 and 462 (`6ab3c9ab6f…`), and the opening guard capture
matched the declared start state exactly. Task 1's tool was written in the imported tools' idiom and **passed all five
proofs on planted faults with no change to the tool between them**, plus one extra check of the add-commit lookup. Its first
write-mode run then **STOPPED**: `STOP: the boot-chain anchor '**(x)**' is found 0 time(s) and must be found exactly once`.
The cause was established at the object before anything was touched (D-669): line 66 of entry 152 opens
`**(x) ★ A CORRECTION TO THE HUNDRED-AND-FIFTY-FIRST ENTRY, …` — its bold run does not close after the item label, so no
line opens with the anchor the dispatch authors, and the premise ledger's FACT that *"the line opening `**(x)**`"* stands at
66 is wrong at the object. The dispatch names that STOP as one that commits nothing of Task 1 (its findings section and the
first-unit rule), so **nothing of Task 1 was committed**: the tool was kept as a loose git blob
`b909c71ea47ef8c62f9bd74e06c634fb217f517b` (recoverable by `git cat-file blob` until the object store is pruned) and
removed from `tools/audit/` with its bytecode cache; `gen_guard_state.py` was not edited; no tool was enrolled. Task 2 then
ran in full under the "Task 1 not committed" branch, and Task 3 carries the end state.

---

## 0. The ordered first read, and what reached me as injected context

**My first tool call was exactly one read of the dispatch file, and nothing else.** It returned a **PARTIAL view**
(lines 1 to 572 of 1,204, at the tool's page limit). Before anything else I read the same file in two further ranges,
573 to 912 and 913 to 1,204, so the whole file was read before any other read.

**Injected context at boot, before any tool call:** (1) `CLAUDE.md`; (2) the memory index `MEMORY.md` from my user memory
folder; (3) a git status snapshot with five recent commits (tip shown as `63163e3156`); (4) an attribution reminder for
commit messages. **The injected `CLAUDE.md` was, by my account, the WHOLE FILE:** its first line as injected was
`# Claude Code — Standing Instructions for This Repository` and its last line `…This applies to CC sessions and Cowork
sessions alike.`; read later with the file tool, the file's line 1 and its last line (1998) are those same lines, and the
injected copy carried every `##` section in the file's order, the conditional spans among them (the gate policy, the local
patches, the bash rules). This is DECLARED, not established (#18): I compared first and last lines and the section order, not
every byte.

**Then, in the dispatch's order:**

- **(1)** `CLAUDE.md` with the file tool: a heading search, then lines 1–312 and 313–666 (Guiding principles through the
  decisions register), 702–772 (the "Build and test commands" block through the session-start read block), and 1536–1998
  (Conventions and the self-check) — the six spans' windows. `STATUS.md` whole. `DECISIONS.md` whole, in three reads (1–362,
  363–612, 613–862). `BUILD_AND_TEST.md` whole (the condition is met). Rule (a)'s `gating_ids` at
  `tools/audit/nongating_apparatus_rows.json`, lines 180 to 414 (the `★_the_live_gating_answer` counts and the whole
  `gating_ids` list); the open-items index was not read.
- **(2)** `cowork_audit_protocol.md`'s dispatch-protocol section, located by a search of its `##`/`###` headings and the
  marker, and read at lines 180 to 1606 in four reads (180–519, 520–899, 900–1269, 1270–1606).
- **(3)** `tools/audit/gen_session_start_read_size.py` whole (804 lines), `tools/audit/gen_defense_share.py` whole (718
  lines), `tools/audit/gen_claude_md_finer_spans.py` whole (790 lines); `tools/audit/gen_governing_surface_spans.py` at the
  constants by one search (`RESOLVED_ROW` … `OPERATIVE` and `CLASSES` at 127–134, `HISTORICAL_MARKERS` 140, the
  `FORMER_WORDING_MARKERS` 165, `DEFENSE_MARKERS` 177, `TABLE_ROW` 197, `FENCE` 198, `STAR_MARKER` 201, `class Stop` 204);
  `tools/audit/output_encoding.py` whole.
- **(4)** `tools/audit/session_start_read_size.json`, `tools/audit/defense_share.json`,
  `tools/audit/claude_md_finer_archive.json` and `tools/audit/claude_md_prune_backlog.json`, each whole.
- **(5)** `tools/audit/gen_guard_state.py` at lines 1–179 (the docstring, the `AUTHORED` list's head comment at 72–74 and
  its first entries), 720–779 (the session-start-read and defense-share entries) and 880–1104 (the L2/L3 entries, the
  decisions group, the prune entries, the list's end and the head of the R4 classification). Not read whole.
- **(6)** Entries 461, 460 and 462 whole (entry 462 existed at my boot).
- **(7)** Not read, as ordered.

---

## The capacity-judgment file, quoted whole

`capacity_judgment_task1.txt`, written with the file tools in my session's scratch folder outside the repository, after
the ordered first read and Task 0 and before any line of the tool:

```
CAPACITY JUDGMENT BEFORE TASK 1 — written 2026-11-01, after the ordered first read and Task 0, before any line of the tool.

WHAT TASK 1 BUILDS. One new measurement tool, tools/audit/gen_per_session_reading.py, writing
tools/audit/per_session_reading.json: table 1 (the imported ordinary session-start read, the four
further members, the arc's dispatch and report populations, the Cowork boot chain, two totals by
side) and table 2 (the six session-start spans of CLAUDE.md cut by the imported finer cut, classed
by the imported classifier, the settled spans marked by hash and by opening, the imported marked
defense totals). Then the five proofs on planted faults (P1 to P5), the write-mode run and the
--check, the self-check and word scan, the enrolment in gen_guard_state.py's authored list with
its two checks, and one commit, pushed.

WHAT THE ORDERED READS TOOK, by my own account. The dispatch (three ranges), the six CLAUDE.md
spans, STATUS.md, DECISIONS.md whole (the largest single read), BUILD_AND_TEST.md whole, the
gating identities, the dispatch-protocol section of cowork_audit_protocol.md (lines 180 to 1606,
the second largest), the three imported tools whole (together about as large as the protocol
section), the coarse constants and output_encoding.py, the four artifacts whole (defense_share.json
the largest of them), the invocation list of gen_guard_state.py at three windows, and entries 461,
460 and 462 whole. Most context went to DECISIONS.md, the protocol section and the three tools.

HAS A SUMMARY OF MY CONTEXT FALLEN? No. No summary has fallen at the time of writing; the whole
conversation from the first read of the dispatch is in my context.

WHAT THE BATCH STILL OWES AFTER TASK 1. The whole close (Task 2: the STATUS.md entries and the
prefix move, the forward-bound re-aim with --apply and --check and the four archive checks, the
regenerations of defense_share, session_start_read_size and then this tool last, the two
population checks, the report, the appended close, the close commit) and the end state (Task 3:
the full guard run in write mode, the classification check, the end-state section, the commit).

MY JUDGMENT. The tool is mostly calls into imported functions whose code I have read in full this
session, so the authored half is the member table and the publication shape. I judge I can finish
Task 1 whole — written, proved, run, enrolled, committed — and still close and reach the end
state. The residual risk is context length: the reads were large, and a summary may fall during
the close. If one falls I will say so plainly in the report and in the STATUS.md close entry. If I
find while building that an imported function behaves otherwise than the dispatch's premise ledger
says, or a proof fails in a way my code cannot correct, I stop under the first-unit rule, commit
nothing of Task 1, and go to Task 2.
```

---

## 1. Task 0

**0(a) — the pin.** `git hash-object -w` of the dispatch → `6c675cf77119f7faac1a5bb0d3590c9e19aca7d6`; `git cat-file -s` →
`119040`. Immediately before staging, `git hash-object` of the working copy → `6c675cf77119f7faac1a5bb0d3590c9e19aca7d6`
again: unmoved.

**0(b) — the refs**, read with the file tools: `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
`63163e31560a2bb663f32dcfae34290f0871026b`, equal to the relayed tip. `git show --stat` of each commit back to the base,
one command each, hash written literally — the chain, as `<commit> <parent>` and subject:

```
63163e31560a2bb663f32dcfae34290f0871026b 3300e3d6513e586d99a08208340139f65c6903ae  End state: the L3 comparison - sections 8, 9 and 14 written, ...  (2 files: cowork_away_returns.md, guard_state.json)
3300e3d6513e586d99a08208340139f65c6903ae e927f9ed201c41e3ac14e9a58a4e87d8680830c3  Close: the L3 comparison - sections 8, 9 and 14 written, ...  (9 files)
e927f9ed201c41e3ac14e9a58a4e87d8680830c3 54392cc3855682e5dc671fdda7e6e6c40db94d18  comparison L3: section 14 written, the independence record relayed
54392cc3855682e5dc671fdda7e6e6c40db94d18 0cae26760f6b7b6c552b8fbea2487eaec779d590  comparison L3: section 9 written, the eight points of the derivation, proposals only
0cae26760f6b7b6c552b8fbea2487eaec779d590 ddccb87fe3a41c2841c8fe21d937082fc5d343bf  comparison L3: section 8 written, the open questions listed ungraded
ddccb87fe3a41c2841c8fe21d937082fc5d343bf 0e926612810189df5267ad19e2e2629051dc78fc  record: entry 460 and the thirtieth l3 comparison tabulation dispatch
0e926612810189df5267ad19e2e2629051dc78fc a714367e6d5185603de611d5f818c5f45c9c5afb  End state: the L3 comparison - position 57 done and sections 7 to 7 written - ...
```

The chain is exactly the relayed one.

**0(c) — A1.** `python tools/audit/changed_paths.py` (repository as the working directory): **397 change records**; exactly
ONE tracked modification, ` M tools/audit/claude_md_finer_archive.json` (the standing one); the untracked population is
given **by its count with every path outside `scratch_artifacts/` named**: `Claude outputs/`, `Codex research inventory/`,
`docs/research_papers/polyph9-release/`, `external resarch summary/Computational Music Theory and Its.pdf`,
`external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf`,
`records/cc/instructions/cc_instruction_per_session_reading_measurement_2026_11_01.md`,
`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_one.md`,
`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_two.md`,
`tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; every other record is under `scratch_artifacts/`. No other
untracked path under `records/`, `tools/audit/` or the repository's top folder. `git ls-files --others --exclude-standard --`
of each of the three named records printed the path itself (untracked), `exit:0`. `git diff --stat 63163e31… -- <path>` of
each named tracked input (`STATUS.md`, `STATUS_ARCHIVE.md`, `gen_status_batch_bound.py`, `status_batch_bound.json`,
`gen_guard_state.py`, the four imported tools, `CLAUDE.md`, `DECISIONS.md`, `cowork_audit_protocol.md`,
`BUILD_AND_TEST.md`, entries 448 to 460 each named, and `cowork_blind_derivation_l3_2026_10_17.md`): **empty for every
one**, `exit:0` each. **A1 holds.**

**0(d) — the last bytes**, each landed file at its blob (`git hash-object -w --no-filters`), the object written to a scratch
file and read by a scratch script:

```
== blob_dispatch.bin   (6c675cf77119f7faac1a5bb0d3590c9e19aca7d6)
  size 119040
  zero bytes 0
  last 70 bytes b'h named one at its ordered first read and holds the quotations to it.\n'
== blob_e461.bin       (9c0de58a20d5f84432ab4920c38ab9ad11de0d25)
  size 16081
  zero bytes 0
  last 70 bytes b'ntinue"; the question on the double copy of `CLAUDE.md`; "continue".*\n'
== blob_e462.bin       (fca1a240a668009e93b614541443221c6326ff32)
  size 14748
  zero bytes 0
  last 70 bytes b'. The user\'s words: the opening instruction;\n"continue"; "continue".*\n'
```

No final line broken off, no zero byte. Entry 461 is 16,081 bytes, as stated; entry 462 is 14,748.

**0(e) — the commit.** Staged by explicit path; `changed_paths.py --staged`:

```
A	records/cc/instructions/cc_instruction_per_session_reading_measurement_2026_11_01.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_one.md
A	records/cowork/handoff/cowork_handoff_entry_four_hundred_and_sixty_two.md
3 changed path record(s) [staged]
```

Committed with the subject `record: entries 461 and 462 and the per-session reading measurement dispatch` →
`6ab3c9ab6f11ed63f3058dc8a4fd2727dd41da65` (parent `63163e31…`, 3 files, 1,509 insertions), read at
`.git/refs/heads/master` and at its own object. Push: `   63163e3156..6ab3c9ab6f  master -> master`;
`.git/refs/remotes/origin/master` reads `6ab3c9ab6f11ed63f3058dc8a4fd2727dd41da65`.

**0(f) — the opening guard capture**, `python tools/audit/gen_guard_state.py --check` (read-only operating mode, named), run
in the background, its output in a scratch file, read with the file tools — verbatim:

```
the guard state re-derives
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
82 guard(s) run, 13 failing, 4 not run, 20 historical record(s)
exit:0
```

Against A2: header *"the guard state re-derives"* (exit 0); run 82; the thirteen FAIL lines are exactly the thirteen named,
none added; zero STOPs in the runner. `python tools/audit/gen_guard_classification.py --check` → exit 2:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_withheld_family_reading.py']
```

exactly the four relayed names.

**0(g) — the two imported measurements at the Task 0 commit**, each in its own call, both exit 0: *"the session-start read
measurement re-derives"* and *"the defense-share measurement re-derives"* (their full outputs are in the scratch files
`t0g_ssr.txt` and `t0g_def.txt`; their values are the committed artifacts' and are not restated, D-431). **The precondition
for Task 1 held.**

---

## 2. Task 1 — written, proved, and STOPPED at its first run; nothing committed

**1(a).** The capacity file is quoted above; it judged Task 1 finishable whole.

**1(b) — the tool**, `tools/audit/gen_per_session_reading.py`, written with the file tools in the idiom of
`gen_session_start_read_size.py` (`HERE`, `ROOT`, `OUT`; the path insert; `use_utf8_output()`; the four imports; its own
`class Stop`; `build()`; `main(argv)` with the `--check` messages the dispatch names; `__main__` catching `Stop` — its own
and each imported tool's — and printing `STOP: …`, exit 2). Its docstring carries what the dispatch orders. Every derivation
is a function over text (`protocol_section`, `bridge_fault_portion`, `roman_items_portion`, `partition_the_six_spans`) or
over a population (`population_rows`, `population_summary`); `build()` reads files and calls them. **Its source is the loose
blob `b909c71ea47ef8c62f9bd74e06c634fb217f517b`**, written by `git hash-object -w` before the file was removed, so the
remainder dispatch's session can recover it exactly (`git cat-file blob b909c71ea47ef8c62f9bd74e06c634fb217f517b`); it is
NOT in any commit.

Three readings of mine are built into it and declared here, each a reading of the dispatch at my code and none of an
imported function:

1. **The protocol partition's accounting.** The dispatch counts a portion as its lines joined by newlines and asks that the
   opening prose, the marked and the unmarked sections sum to the section. Under that counting the portions sum to the
   section LESS the newline that joins each portion to the next, so the tool counts those joining newlines explicitly and
   STOPs unless *opening + marked + unmarked + joining newlines = section*. The equality is exact; it is published.
2. **The settled-span opening match.** The dispatch compares *"the first 120 characters of its `text`"* with *"the first
   120 characters of the entry's `the_opening`"*. Read at the two artifacts, `the_opening` is **whitespace-collapsed**
   (`claude_md_finer_archive.json`'s first entry reads *"(#12; user-ruled 2026-08-11"* on one line where the file breaks the
   line after *"(#12;"*), the shape `gen_claude_md_finer_spans.build()` itself writes (`" ".join(span["text"].split())[:160]`).
   A raw comparison would therefore fail at the first line break of every multi-line sub-block and the opening match could
   never fire; the tool collapses whitespace on both sides, as the producing tool does.
3. **The add-commit lookup.** The dispatch names a per-path `git log --diff-filter=A --format=%H %ct -- <path>`. Timed at
   this repository, one per-path call took **about one second** (`real 0m1.016s`), and the handoff population alone is
   several hundred files, which would put a guard-set member at minutes per run. The tool runs ONE
   `git log --no-renames --diff-filter=A --format=@@%H %ct --name-only -- <folder>` per folder and takes, for each path, the
   first (newest) commit naming it — what a per-path call's first line gives. **Checked, not assumed:** a scratch script
   compared the two lookups for every arc dispatch, every arc report, entries 118, 152, 169 and 291, and the three latest
   handoff entries — `checked 67 mismatched 0` / `ADD-COMMIT CHECK PASS`.

**1(c) — the proofs, before the first run**, each a scratch script importing the tool and calling its functions on an
altered copy, run with `python -I -X utf8` and the shell's working directory set to the scratch folder, each output written
to a scratch file and read with the file tools. Quoted whole:

**P1** (`proof_p1.py`):
```
the marker line deleted, at line 235 : "*★ STANDING CLAUSE — a dispatch's read-first block requires the clause below to be met.*"
the_marked_sections count 38 -> 37  characters 101700 -> 100817
the_unmarked_sections count 1 -> 2  characters 2157 -> 2950
section characters 108389 -> 108300  fall 89  expected 89
the sums still account: yes (protocol_section raised no Stop on the altered copy)
P1 PASS
```

**P2** (`proof_p2.py`):
```
the marker inserted directly above line 896 : '### When a shell-read policy cannot decide, it DENIES — and the ceiling it cannot see is published in the measured rate'
the_marked_sections count 38 -> 39  characters 101700 -> 103946
the_unmarked_sections count 1 -> 0  characters 2157 -> 0
section characters 108389 -> 108478  rise 89  (the line and its newline: 89 )
the sums still account: yes (protocol_section raised no Stop on the altered copy)
P2 PASS
```

**P3** (`proof_p3.py`; the star-marked sub-block chosen is the one opening
`**★ WHAT HAPPENS TO A NAME BORROWED FROM THE PUBLISHED RESEARCH…`, inside Conventions):
```
the ★ removed at line 1616 : '  **★ WHAT HAPPENS TO A NAME BORROWED FROM THE PUBLISHED RESEARCH, AND IN WHAT ORDER THE CLEANUP'
  Guiding principles                            sub-blocks   44 ->   44  characters  26908 ->  26908
  The open-items register                       sub-blocks   17 ->   17  characters  14816 ->  14816
  The decisions register                        sub-blocks    3 ->    3  characters  17109 ->  17109
  This block                                    sub-blocks   20 ->   20  characters   5213 ->   5213
  Conventions                                   sub-blocks   20 ->   19  characters  41071 ->  41070
  The self-check after every coding exercise    sub-blocks    2 ->    2  characters    759 ->    759
six spans 105876 -> 105875  fall 1
the accounting still sums: yes (partition_the_six_spans raised no Stop on the altered copy)
P3 PASS
```

**P4** (`proof_p4.py`; the unaltered run's settled-span matches were listed first by `settled_unaltered.py`, quoted below,
and the span chosen is the one found by hash at line 1775, *"NOTE ON PHASE 2"*):
```
by hash 4 by opening only 2 not found 2
tools/audit/claude_md_finer_archive.json the_left_at_site_by_the_reading by hash — the sub-block stands unchanged [202]
    **★ THAT PARAGRAPH REPLACED A NARROWER ONE, AND THE FORMER WORDING STANDS IN PLACE (#12; user-ruled 
tools/audit/claude_md_finer_archive.json the_left_at_site_by_the_reading by hash — the sub-block stands unchanged [53]
    **★ WHAT IT SUPERSEDES — A POINTER, NEVER A COPY (#6).** R3's clause that an apparatus finding's row
tools/audit/claude_md_finer_archive.json the_refused_by_the_ruling by its opening only — the same sub-block, amended since [388]
    **★ AND WHAT SUCH A ROW IS OWED — IT STOPS BEING OWED, WITH A PER-ROW LAPSE RECORD (user-ruled 2026-
tools/audit/claude_md_finer_archive.json the_refused_by_the_ruling not found []
    *★ [SUPERSEDED by the OI-178 adoption 2026-07-26 — historical] THE OI-168 RE-BASELINE (2026-07-14; r
tools/audit/claude_md_finer_archive.json the_refused_by_the_ruling not found []
    **★ A-8 DUAL-TRACK (MEASURED + RATIFIED, user, 2026-07-03; `cc_a8_rebaseline_measure_report.md`).** 
tools/audit/claude_md_finer_archive.json the_refused_by_the_ruling by hash — the sub-block stands unchanged [1949]
    **★ THE RULE COVERS EVERY READ MECHANISM AND EVERY DIALECT (recorded 2026-08-08 on the user's direct
tools/audit/claude_md_prune_backlog.json the_left_at_site_by_the_reading by its opening only — the same sub-block, amended since [1658]
    **★ THE THREE-PHASE STRUCTURE BELOW IS SUPERSEDED AND ITS TRUTH HALF IS REPLACED (user-ruled 2026-08
tools/audit/claude_md_prune_backlog.json the_left_at_site_by_the_reading by hash — the sub-block stands unchanged [1775]
    **★ NOTE ON PHASE 2 — THE ENUMERATION THIS CLAUSE POINTS AT IS RATIFIED (user, 2026-08-03; D-439).**
```
```
the sub-block: 1775 to 1804 ; changed at line 1804 : '  owed."*)*' -> '  Owed."*)*'
  **★ THAT PARAGRAPH REPLACED A NARROWER ONE, AND THE FORMER W | by hash — the sub-block stands unchanged -> by hash — the sub-block stands unchanged 
  **★ WHAT IT SUPERSEDES — A POINTER, NEVER A COPY (#6).** R3' | by hash — the sub-block stands unchanged -> by hash — the sub-block stands unchanged 
  **★ AND WHAT SUCH A ROW IS OWED — IT STOPS BEING OWED, WITH  | by its opening only — the same sub-block, amended since -> by its opening only — the same sub-block, amended since 
  *★ [SUPERSEDED by the OI-178 adoption 2026-07-26 — historica | not found -> not found 
  **★ A-8 DUAL-TRACK (MEASURED + RATIFIED, user, 2026-07-03; ` | not found -> not found 
  **★ THE RULE COVERS EVERY READ MECHANISM AND EVERY DIALECT ( | by hash — the sub-block stands unchanged -> by hash — the sub-block stands unchanged 
  **★ THE THREE-PHASE STRUCTURE BELOW IS SUPERSEDED AND ITS TR | by its opening only — the same sub-block, amended since -> by its opening only — the same sub-block, amended since 
  **★ NOTE ON PHASE 2 — THE ENUMERATION THIS CLAUSE POINTS AT  | by hash — the sub-block stands unchanged -> by its opening only — the same sub-block, amended since    <- MOVED
found_by_hash 4 -> 3
found_by_opening_only 2 -> 3
not_found 2 -> 2
P4 PASS
```

**P5** (`proof_p5.py`):
```
unaltered: {'first_line_at_the_tree': 27, 'last_line_at_the_tree': 51, 'characters': 2075}
Stop raised: the boot-chain anchor '### ★★ THE BRIDGE FAULT — READ THIS BEFORE YOU WRITE ANYTHING' is found 2 time(s) and must be found exactly once
P5 PASS
```

**No change was made to the tool between any proof and the run**; every proof passed at its first run.

**1(d) — the run, and the STOP.** `python tools/audit/gen_per_session_reading.py` (write mode, named), the repository as
the working directory, output to a scratch file — verbatim, exit 2:

```
STOP: the boot-chain anchor '**(x)**' is found 0 time(s) and must be found exactly once
```

**The cause, established at the object before anything was touched (D-669).** A Grep of entry 152 for `(v)` and `(x)`
found lines 61, 65 and 66; entry 152 was then taken from the git object
`63163e31560a2bb663f32dcfae34290f0871026b:records/cowork/handoff/cowork_handoff_entry_one_hundred_and_fifty_two.md` into a
scratch file and its lines 60 to 68 printed by a scratch script:

```
60 "**(iv)** **The user's Cowork memory store WAS written to, once**, appending one line to `/"
61 "**(v)** The running total of landings is NOT advanced; this stage's landings are NAMED — t"
62 '**(vi) ★ THE BRIDGE FAULT FIRED IN BOTH SHAPES IN THIS SITTING.** Three times it returned '
63 '**(vii)** Read in this stage: `reading_pass/candidacy_upgrades.md` **whole**; `docs/resear'
64 "**(viii)** **This entry's landing is proved at its CONTENT by this side; its SIZE is recor"
65 '**(ix)** **This entry was written once and then FACT-CHECKED AT THE OBJECTS by this side b'
66 "**(x) ★ A CORRECTION TO THE HUNDRED-AND-FIFTY-FIRST ENTRY, FOUND BY THIS ENTRY'S OWN FACT-"
67 ''
68 '---'
```

Line 66 opens `**(x) ★ …` — the bold run closes at the end of that heading phrase, not after `(x)` — so no line opens with
`**(x)**`. The dispatch's anchor and its premise-ledger FACT (*"entry 152's line opening `**(v)**` at 61 and the line
opening `**(x)**` at 66"*) do not hold at the object; line 61's `**(v)**` does. **This is the STOP the dispatch's findings
section names** (*"a boot-chain anchor found other than exactly once … is a STOP in the tool … and a STOP-and-report in the
batch: commit nothing of Task 1, report the message, and go to Task 2"*). I did not loosen the anchor: it is authored by the
dispatch, and re-authoring it would be my resolution of a premise the dispatch states as FACT.

**What I did, under the first-unit rule:** `git hash-object -w -- tools/audit/gen_per_session_reading.py` →
`b909c71ea47ef8c62f9bd74e06c634fb217f517b`; then `rm` of `tools/audit/gen_per_session_reading.py` and of the bytecode cache
`tools/audit/__pycache__/gen_per_session_reading.cpython-314.pyc` the proofs' imports had written; a Glob for
`tools/audit/**/*per_session_reading*` then found nothing; `changed_paths.py` showed only the standing tracked modification
and the standing untracked `.mscx` under `tools/audit/` (394 records). No artifact had been written (the STOP fired inside
`build()`, before the write). **1(e), 1(f) and 1(g) were not performed**: no word scan of a tool that is not committed, no
enrolment, no commit. `gen_guard_state.py` is unedited.

**A portion of 1(e) — the word scan of the tool's own text — was run after the STOP, over the kept blob** (taken by
`git cat-file blob b909c71e…` into a scratch file and searched with the file tools, for the remainder session's benefit),
for *note(s)*, *key(s)*, *part(s)*, *figure(s)*, *rest*, *root*, *scale*, *bar*, *flat*, *stem*, *instrument*, *period*,
*phrase*, *measure*, *tie*, *register* and *mode* as whole words. The hits are: the imported function's name `measure` and
the verb *to measure* (lines 9, 30, 31, 524, 743), `ROOT` as code (109, 189, 308, 327, 811, 820), `key=` as code (338) and
`shape.keys()` as code (403). **One British spelling of my own stands in it: the function name `normalised_opening`** —
reported, not corrected, the tool not being committed; a remainder session that recovers the blob owes the American
spelling. Not otherwise graded.

---

## 3. Task 2 — the close (Task 1 not committed)

**2(a) — the `STATUS.md` entries.** In one edit: the close entry, naming this dispatch by its file name and carrying the
`Last updated: ` prefix, and the Task 0 entry (`Same dispatch`) below it — **no Task 1 entry**, Task 1 not having been
committed — and the prefix removed, and nothing else, from the thirtieth batch's close entry. Read after the edit: **exactly
one line carries `Last updated: `**. The case-insensitive substring search of `STATUS.md` for all 26 ruled terms returned
exactly one hit, `24:phrase`, the standing *paraphrase* line (moved from line 20 by the two new entries). A search for
*repeat* and *tie* returned hits only on lines 12, 14 and 16 — the thirtieth batch's three entries, which carry *thirtieth*,
moved away at 2(b); my two entries carry none.

**2(b) — the forward bound.** `gen_status_batch_bound.py` read at the object `63163e31…` (written to a scratch file and read
there) at its aiming region: `BASE_COMMIT = "e927f9ed…"` (2342), `PREVIOUS_BATCH_DISPATCH = "…twenty_ninth_2026_10_31.md"`
(2547), `ACT_DATE = "2026-10-31"` and `DISPATCH = "…thirtieth_2026_10_31.md"` (2800–2801), `TASK = "Task 2"` (3054),
`MOVE_KIND = "ordinary"` (3061), and `PREVIOUS_AIMINGS` ending at the thirtieth batch's row (3687–3690) — **every constant
as the premise ledger relays it**. `git rev-parse 6ab3c9ab…:STATUS.md` → `5a4061c254b51f53650a69280987432a93e5bd3b` and
`git rev-parse 63163e31…:STATUS.md` → `5a4061c254b51f53650a69280987432a93e5bd3b`, one command each: equal. Re-aimed:
`BASE_COMMIT` → `6ab3c9ab6f11ed63f3058dc8a4fd2727dd41da65` (the Task 0 commit, Task 1 having committed nothing);
`PREVIOUS_BATCH_DISPATCH` → `cc_instruction_l3_comparison_tabulation_thirtieth_2026_10_31.md`; `ACT_DATE` → `2026-11-01`
(the day the move ran); `DISPATCH` → `cc_instruction_per_session_reading_measurement_2026_11_01.md`; `TASK` stays
`Task 2`; `MOVE_KIND` stays `ordinary`; this batch's aiming appended as the last row of `PREVIOUS_AIMINGS`; each head
comment amended in the shape of the rows above it, the former values named. `--apply`:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 3, 3,079 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

`--check` (own call), exit 0:

```
  entries moved: 3, 3,079 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**The prediction held**: `status_batch_bound.json` → `the_moved` names the thirtieth batch's close entry (`line_at_base`
8, `"the_one_declared_adjustment_applied": true`), its Task 1 `Same dispatch` entry (10) and its Task 0 `Same dispatch` entry
(12); the two 2026-09-02 entries stayed; no STOP. **No correction line was inserted in `STATUS_ARCHIVE.md`.** The four
archive checks, each in its own call, each exit 0:

```
python tools/audit/gen_status_batch_bound.py --check
  entries moved: 3, 3,079 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True

python tools/audit/gen_governing_surface_split.py --check --pair STATUS.md
  STATUS.md / STATUS_ARCHIVE.md: moved 131 span(s), 457,949 characters | in companion: True | absent from parent: True | arithmetic balances: True
  TOTAL moved 281 span(s), 793,066 characters; LEFT AT SITE by the reading 17 span(s), 77,794 characters

python tools/audit/gen_status_residue_move.py --check
  candidates: 17, moved 16, left at site by the reading 1
  characters moved: 46,105
  byte-present in the companion exactly once: True
  absent from the must-read:                  True
  every flagged entry still at site:          True

python tools/audit/gen_status_archive_pass.py --check
  dated entries moved: 52
  at the pass commit, the live file was exactly base-minus-range: True
  the moved block is verbatim in the archive at HEAD:             True
  the moved block is absent from the live file at HEAD:           True
```

**2(c) — the regenerations.** Each check first, in its own call:

- `gen_evidence_pin_membership.py --check` → exit 0, GREEN, as predicted — *"the evidence pin's class membership
  re-derives"*, *"generated ratification documents 7; ruling records read 170"*, *"members 7 — pinned 5, UNRESOLVED 0"*.
- `gen_defense_share.py --check` → exit 1, red as A2 provides; `gen_session_start_read_size.py --check` → exit 1, red as A2
  provides. Regenerated (the read size first, then the defense share), each exit 0; each `--check` again → exit 0:
  *"the session-start read measurement re-derives"*, *"the defense-share measurement re-derives"*.
- `gen_per_session_reading.py` — **not regenerated; it does not exist**, Task 1 not having been committed.
- `gen_l0_l1_outgoing_population.py --check` → **exit 1, `STALE vs the derivation: l0_l1_outgoing_population.json does not
  re-derive` — AGAINST A2's prediction of green.** `gen_l3_outgoing_population.py --check` → **exit 1, `STALE vs the
  derivation: l3_outgoing_population.json does not re-derive` — against A2's "expected green".** Both were regenerated as
  A2 provides (each exit 0) and checked again (each exit 0).

**What moved, named at the blob diffs** (each regenerated file written with `git hash-object -w`, each old blob taken by
`git rev-parse 63163e31…:<path>`, one command each; `git diff <old> <new>` between explicit blob hashes):

- `l0_l1_outgoing_population.json` (`87a19f68…` → `bf3664bc…`): `hits_per_term` → `tie` 892 → 889; and the RESIDUE record
  for `STATUS.md` — three `recorded` hits of the term *tie* at lines 8, 10 and 12, all three the thirtieth batch's entries
  (*thirtieth* contains the substring) — removed, those entries having moved to `STATUS_ARCHIVE.md`. **No member of
  `the_population` moved.** The cause is the same one the thirtieth batch named in its own close: its file name.
- `l3_outgoing_population.json` (`13d1750b…` → `7b4f925f…`): one RESIDUE record's `line_number` 20 → 18 — the standing
  *paraphrase* line of `STATUS.md`, shifted by the net two lines this close removed above it. **No member of
  `the_population`, no item-4 passage and no member of `the_tabulation_population` moved.**
- `session_start_read_size.json` (`df865342…` → `c6019963…`): `at_the_tree` → `characters_per_member` → `STATUS.md`,
  `total_characters`, and both rows of `movement_against_each_earlier_reading` (`to_total`, `change_in_characters`,
  `change_percent`). Nothing else.
- `defense_share.json` (`f0334b0c…` → `a69ea370…`): `the_denominators_…` → `the_whole_ordinary_session_start_read`, and
  `the_totals` → `share_of_the_whole_ordinary_session_start_read`. Nothing else.

Every moved value is `STATUS.md`'s size or a sum or share built on it; the values themselves are at the artifacts (D-431).

**2(d) — this report. 2(e) — the close section appended to `records/cowork/handoff/cowork_away_returns.md`. 2(f) — the
close commit**: see §4.

---

## 4. The commits

| Task | Commit | Parent | What it carries |
|---|---|---|---|
| 0 | `6ab3c9ab6f11ed63f3058dc8a4fd2727dd41da65` | `63163e31560a2bb663f32dcfae34290f0871026b` | the dispatch and entries 461 and 462 |
| 1 | — (none: STOPPED before its commit) | — | tool kept as the loose blob `b909c71e…`, not committed |
| 2 | see `git log` (the close commit cannot name its own hash) | `6ab3c9ab…` | `STATUS.md`, `STATUS_ARCHIVE.md`, the forward-bound tool and its artifact, the four regenerated artifacts, this report, the away-returns close |
| 3 | see `git log` | the close commit | the guard state and the end-state portion |

There is no artifact of Task 1, so no artifact blob or size is given.

---

## 5. Grades

- **E0 — MET.** The named paths in one commit; `origin/master` at it; the pin proved; A1 reported with its enumeration; the
  opening capture the thirteen and nothing else; the four-name STOP; both imported measurements green.
- **E1 — NOT MET, by the STOP the dispatch names.** The tool was written in the imported idiom with its docstring, bounds and
  STOPs, and all five proofs ran and passed; the run STOPPED at a boot-chain anchor; nothing of Task 1 was committed or
  enrolled, by the first-unit rule.
- **E2 — at the tree carrying the close:** every `--check` A2 names green (the defense share, the read size, the L0/L1 and
  L3 populations after regeneration, the evidence pin), the four archive checks green; the failing set and the
  classification's STOP are taken at Task 3's run (the classification is expected to name the FOUR, Task 1 not having
  enrolled a fifth).
- **A1 — HOLDS** (§1, 0(c)).
- **A2 — HOLDS IN SUBSTANCE, WITH TWO PREDICTIONS WRONG:** the L0/L1 and L3 checks went red after Task 2, where A2 expected
  green; A2's own remedy (regenerate, compare by explicit hash, name every record that moved) was applied, and only residue
  records moved (§3).
- **A3 — HOLDS:** `gen_l2_outgoing_population.py` was not run in any operating mode.
- **A4 — HOLDS in the narrower form the STOP leaves:** no tool added, no tool enrolled, `gen_guard_state.py` and
  `gen_guard_classification.py` unedited; `gen_status_batch_bound.py` edited at its authored aiming only. Population 82
  expected at Task 3, not 83.
- **A5 — verified at Task 3** at the objects.

---

## 6. Declared departures

1. **The first read was partial** (1–572 of 1,204) and was completed in two further ranges before any other read.
2. **The settled-span opening match compares whitespace-collapsed text** (§2, reading 2) — the artifacts' `the_opening` is
   collapsed, which the premise ledger does not say.
3. **The protocol partition counts the joining newlines explicitly** (§2, reading 1).
4. **One folder-level `git log` replaces the per-path add-commit call**, checked equal on 67 paths (§2, reading 3).
5. **A stray token** (`ls-dummy=0`) sat inside my first 0(c) loop of `git diff --stat` calls and made each iteration's last
   command exit 127; the loop was re-run clean and only its scratch output was affected.
6. **A `wc -l` aimed at `records/cowork/handoff/cowork_away_returns.md` was denied by the armed guard** — my error; the line
   positions were taken with Grep and Read instead.
7. **Commands run with the repository as the working directory**: `changed_paths.py` (whole and `--staged`), the guard
   capture and the classification, the imported measurements, the forward-bound tool, the regenerations, the population
   checks, the tool's own run, `git add`, `git commit`, `git push`, and the `rm` of the two files; scratch scripts ran with
   the scratch folder as the working directory. The `git -C /c/s/MS …` object queries ran from the scratch folder.
8. **`python -I -X utf8` scratch scripts inserted `tools/audit` on their own import path**, since `-I` does not.
9. **No mandate class was found named otherwise by the record I read** — but the ruling records behind rows 2, 4 and the
   reports row (2026-08-17, 2026-08-24, the 2026-09-03 rule) were not opened by this batch, so that is a bound, not a check.

---

## 7. The file's state, and the ordered reads against the task

**The artifact is NOT written and NOT enrolled**; Task 1 STOPPED at its first run on an authored anchor that does not hold at
the object, and nothing of it was committed. The tool's source survives as the loose blob `b909c71e…`.

**The ordered reads against the task.** The reads took most of this context before any unit was opened: `DECISIONS.md`
whole was the largest single read, then the protocol section (lines 180–1606) and the three imported tools read whole,
then `defense_share.json`, the six `CLAUDE.md` spans (read on top of the whole file injected at boot) and the dispatch
itself. **No summary of my context fell** at any point of this session up to the writing of this report.

---

## 8. Findings of the run

1. **The dispatch's entry-152 anchor does not hold at the object.** The authored anchor `**(x)**` and the premise-ledger
   FACT placing it at line 66 are both wrong: line 66 opens `**(x) ★`. The same shape is at line 62 (`**(vi) ★`). Surfaced,
   not repaired; it is the whole reason Task 1 did not land.
2. **A2's green predictions for the L0/L1 and L3 population checks were wrong at this close.** The L0/L1 search counts *tie*
   as a substring, so the thirtieth batch's entries — whose dispatch name carries *thirtieth* — formed a `STATUS.md` residue
   record that left with them; and the L3 search records the line number of the standing *paraphrase* line, which moves
   whenever a close changes the line count above it. Both are residue-record movements; neither touches a population.

---

## 9. Observations met and not acted on

- **Members the planned table does not carry that a session of this batch read before its work:** the memory index
  `MEMORY.md` and the git status snapshot, both injected at boot beside `CLAUDE.md`; `STATUS.md`'s, `DECISIONS.md`'s and the
  gating answer's own reads are in the imported ordinary read. Named, not added.
- **Settled spans not found in the six spans** (from the unaltered proof run, not from an artifact): two of the eight —
  the two the 2026-08-17 ruling refused that sit in the gate policy block (*"[SUPERSEDED by the OI-178 adoption …"* and
  *"A-8 DUAL-TRACK …"*), which is a conditional span, outside the six. Two matched by opening only (*"AND WHAT SUCH A ROW
  IS OWED"*, *"THE THREE-PHASE STRUCTURE"*) — amended since, their record paths now carrying `records/cowork/rulings/`.
- **An imported artifact's field shape differs from the premise ledger's account:** `the_opening` in
  `claude_md_finer_archive.json` and `claude_md_prune_backlog.json` is whitespace-collapsed (§2, reading 2).
- **The per-path add-commit call costs about a second here**, which a guard-set member cannot afford over the handoff folder
  (§2, reading 3).

---

## 10. The plan's tell

**Did this batch produce anything other than the landed records, the tool and its artifact, the enrolment edit, the Task 2
files and the report — and, outside the repository, the scratch files, the five proof copies and the loose blob objects the
hash checks write?** **Yes, one thing, and fewer of the named ones:** the loose blob `b909c71e…` of the uncommitted tool
(written to keep its source recoverable — a loose object like those the hash checks write, but kept on purpose), and the
bytecode cache file the proofs' imports wrote under `tools/audit/__pycache__/`, removed. The tool, its artifact and the
enrolment edit were NOT produced in the repository. The proof copies were held in memory inside the scratch scripts, not
written as files.

---

## 11. The self-check

Re-read the diff of every file this batch wrote: `STATUS.md` (two entries added, one prefix removed — read back, one
`Last updated: ` line), `tools/audit/gen_status_batch_bound.py` (five aiming edits, comments in the earlier rows' shape,
former values named), this report and the away-returns section. Against the principles: nothing touches the analysis, no
`src/`, no measurement of the analysis, no governing document beyond the two of the close; every value in this report is
either a tool's verbatim output or cited to its artifact (D-431); the premise found wrong is reported with the object it was
checked at (#18, #19); nothing was resolved by stretching a dispatch anchor. **Word scan of my own wording** (this report,
the two `STATUS.md` entries, the away-returns section), searched for *note*, *notes*, *key*, *part* as a word, *the rest*,
*figure(s)*, *measure* as a noun, *register* bare, *root*, *scale*, *bar*, *flat*, *stem*, *instrument*, *period*, *phrase*,
*tie*, *take part*, *status bar*, *recorded figure*, *colour*, *centre*, *judgement*, *recognise*, *normalise*, *summarise*:
the hits that stand are quoted text (tool output, the dispatch's anchor, the *paraphrase* line, file names carrying
*thirtieth*), *portion* used for the other sense, and *measurement* as the gauging noun. No numeric grade anywhere.
