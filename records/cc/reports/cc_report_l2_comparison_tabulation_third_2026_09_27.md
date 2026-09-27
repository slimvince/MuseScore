# CC REPORT — THE L2 COMPARISON, FOURTH BATCH: THE TABULATION CONTINUED FROM POSITION 6 — POSITIONS 6, 7 AND 8 TABULATED WHOLE, THE REMAINDER UNTOUCHED (2026-09-27)

> **Executes** `records/cc/instructions/cc_instruction_l2_comparison_tabulation_third_2026_09_27.md`, pinned
> at blob `b4e6d17cc742807a1fa1423d543d62672a0637e6`. **No task STOPped.** The tabulation tabulated
> **positions 6, 7 and 8**, each whole and each in its own commit. It stopped at the member boundary after
> position 8, under the dispatch's capacity judgment (Task 1(h)) and its batching rule (Task 1(g), D-672).
> The stop is recorded here and in the reading file's §0. **This report decides nothing**: it relays what
> was run and what was written, and it makes no recommendation about the derivation, the method, any
> disposition or any open question. Every output is quoted verbatim from the run. **No count the population
> tool produces, and no count of the reading file's rows, is restated in prose (D-431).** The member sizes
> are at `tools/audit/l2_outgoing_population.json` → `the_tabulation_population` → `the_members`. The row
> arithmetic is at the feet of the reading file's §6.6, §6.7 and §6.8 and at its §13. The one exception the
> dispatch orders is the capacity judgment of Task 1(h), which states each member's `lines` and `bytes` as
> read at the artifact.

---

## 0. The ordered first read

The session's opening instruction named only this dispatch, so **the dispatch file was the first file
read**, to learn what to do. *(`CLAUDE.md` and the auto-memory index reached the session's context at boot
as injected context, before any tool call — recorded the way the dispatch's ordered-first-read block asks.)*
The first read after the dispatch was `cowork_blind_derivation_l2_2026_09_27.md`. It was read from its `## 5.`
heading to its end first, which is §5, then §6, then §7 in that order, and then **the whole file** from its
first line. This came before any read of `STATUS.md`, `DECISIONS.md` or anything else (Ruling 2 of the
comparison-design sitting). This is declared at §5, item 1. **The derivation's own counts, taken by this
session at its structure: 49 statements (L2-S1 to L2-S49), 18 open questions (OQ-L2-1 to OQ-L2-18), 5 marked
★ (OQ-L2-2, 4, 5, 8 and 16)** — equal to the reading file's manifest, so no STOP.

Then, in the dispatch's order:

- (1) `CLAUDE.md` at its six session-start spans, which were in context at boot. Then `STATUS.md`,
  `DECISIONS.md` whole, and `BUILD_AND_TEST.md` whole, its condition being met because this batch runs the
  guard set. Then the gating answer at `tools/audit/nongating_apparatus_rows.json` →
  `★_the_live_gating_answer` → `gating_ids`.
- (2) `cowork_audit_protocol.md`'s dispatch-protocol section in full.
- (3) The two rulings of 2026-09-27 and the comparison-design sitting, whole.
- (4) The phase definition, §0 and §3.4.
- (5) `FRAMEWORK.md` §5, from `### L0` through `### The boundary contracts`.
- (6) The brief's §2, §4 and §7.
- (7) The pack's L2 `counted`, `THE_WITHHELD_FAMILY` (`identities`, `documents`, `passages`) and `LEAKS`,
  read and not regenerated.
- (8) The second batch's report, whole, and the current handover block,
  `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_four.md`, which this batch lands.
- (9) The artifact's `the_passage_rule`, `the_order` and `the_members` from position 6 onward.
- (10) The reading file's banner and §0 to §6's reading rules, the first row blocks of §6.1, §6.5's foot and
  §10 to §16.

**Not read, as the dispatch orders:** the released dispatch, its report, the second dispatch, and the L0/L1
reading file's §10, since position 62 was not reached. The outgoing texts were opened member by member, as
Task 1 orders.

---

## 1. Task 0 — the records landed, and pushed

**0(a) — the pin.** `git hash-object -w` over the dispatch gave `b4e6d17cc742807a1fa1423d543d62672a0637e6`.
Re-read now at the object:

```
$ git cat-file -s b4e6d17cc742807a1fa1423d543d62672a0637e6
56771
$ git rev-parse 0ee62fc2eba2635c857047c000d6724349db55b1:records/cc/instructions/cc_instruction_l2_comparison_tabulation_third_2026_09_27.md
b4e6d17cc742807a1fa1423d543d62672a0637e6
```

The committed blob is the pinned one, so the blob did not move between the pin and staging.

**0(b) — the refs, read with the file tools.** `.git/refs/heads/master` and
`.git/refs/remotes/origin/master` both read `3158c3c24c031505f55ad19190a09d766614fd75`, and
`.git/COMMIT_EDITMSG` carries *"Close: the L2 tabulation continued from position 5, under its dispatch"*.
**The chain, read at the objects by explicit hash:**

```
commit 3158c3c24c031505f55ad19190a09d766614fd75
parent bbbc80c0496028a770f996b0f120c21746c9c1a1
subject Close: the L2 tabulation continued from position 5, under its dispatch
 9 files changed, 789 insertions(+), 31 deletions(-)
commit bbbc80c0496028a770f996b0f120c21746c9c1a1
parent 392e278a5bdca4d8151d2e91a0afe7ff240dec6e
subject comparison L2: member 5 tabulated - 417 outgoing statements placed, proposals only
 1 file changed, 5943 insertions(+), 20 deletions(-)
commit 392e278a5bdca4d8151d2e91a0afe7ff240dec6e
parent 35ac1778d05ace507fd00f533fb14d17ca6443ff
subject record: entry 263 and the second L2 tabulation dispatch
 2 files changed, 732 insertions(+)
```

**The chain matches the one the FACT relays**, commit for commit.

**0(c) — A1's check.** `python tools/audit/changed_paths.py`, exit 0. The capture is saved outside the
repository at `…\scratchpad\changed_paths.txt`. Every record other than the untracked paths under
`scratch_artifacts/`, verbatim:

```
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_l2_comparison_tabulation_third_2026_09_27.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_four.md
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
396 changed path record(s) [worktree]
```

Per named path, `git ls-files --others --exclude-standard -- <path>` returned each of the two landing paths
as untracked. **Nothing was staged**: the index's tree (`git write-tree`) and `3158c3c2…^{tree}` are the
same object, `64eae132f8273178121e8fcaa20da136c505c87d`.

**0(d) — the last-bytes check**, at each blob, re-read now at the objects:

```
dispatch b4e6d17c 56771
b'. TOWARDS the ultimate objective and TOWARDS the guiding principles.*\n' 0
handoff 5fa402dd 6654
b'ce: Cowork, 2026-09-27 (Stockholm), the sitting booted on entry 263.*\n' 0
```

No zero byte, and no final line broken off mid-word.

**0(e) — the commit.** The staged set, proved against the tip's tree by explicit hash:

```
:000000 100644 0000000000000000000000000000000000000000 b4e6d17cc742807a1fa1423d543d62672a0637e6 A	records/cc/instructions/cc_instruction_l2_comparison_tabulation_third_2026_09_27.md
:000000 100644 0000000000000000000000000000000000000000 5fa402ddde81bc317a3e4b93ca1ead8c74bd4ee5 A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_four.md
```

**Commit `0ee62fc2eba2635c857047c000d6724349db55b1`** — `record: entry 264 and the third L2 tabulation
dispatch`. Pushed; `.git/refs/remotes/origin/master` read `0ee62fc2…`.

**0(f) — the opening guard capture**, after the commit: `python tools/audit/gen_guard_state.py` (write mode,
the default), exit 0. It is saved outside the repository at
`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\4bb24b3f-9912-4418-9c90-9aff669b056a\scratchpad\guard_open.txt`.
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

**Against A2: holds exactly.** The twelve named reds, no thirteenth, and zero STOPs in the runner.
`gen_evidence_pin_membership.py --check` PASSES, as A2 predicts. The opening capture left
`tools/audit/guard_state.json` byte-identical to its committed blob: the working file hashed to
`7be0bb9e5f92283fda4061f9b3ff23db8afbdd27`, the object at `3158c3c2…` and at every member commit of this
batch. So the value of record at that object's `summary` is the one this capture produced.

**The guard classification**, `python tools/audit/gen_guard_classification.py`, exit 2, against the FACT —
exactly the four names, no fifth:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

**0(g) — the two blobs, verified at the object before Task 1**, and again at the close:

```
cowork_blind_derivation_l2_2026_09_27.md  at 0ee62fc2…, at a22d8a41…, working tree: d78ac530992860d38d1f605a77a2961d5440a2f6
cowork_blind_session_brief_l2.md          at 0ee62fc2…, at a22d8a41…, working tree: c5ff83dcad2107ac8c05ead21724cbab0d9471fd
```

Both are the relayed blobs.

**E0: MET.** Two paths in one commit; `origin/master` at the commit; the pin proved; A1 established by the
enumeration; the opening capture as A2 predicts; the two blobs verified before Task 1.

---

## 2. Task 1 — the tabulation, continued

### 2.1 The capacity judgments (1(h)), each stated before the member was opened

| Position | Member | `lines` | `bytes` | Judgment | Outcome |
|---|---|---|---|---|---|
| 6 | `cowork_layer4_chordsymbol_design.md`, whole | 629 | 59,128 | finishable whole | tabulated whole, committed |
| 7 | `cowork_layer3_keymode_design.md`, whole | 536 | 53,650 | finishable whole | tabulated whole, committed |
| 8 | `cowork_layer5_engagement_design.md`, whole | 659 | 55,597 | finishable whole | tabulated whole, committed |
| 9 | `cowork_stage5_fitter_design.md`, whole | 1,545 | 147,929 | **NOT finishable whole** in the context that remained | **not opened**; the writing stops here (D-672) |

The sizes are read at `the_members` → `lines`, `bytes`. **Position 6 was finished whole, so no first-member
finding arises under 1(h).** Each member's first and last line texts are quoted in that member's manifest
header in the reading file. At the close, each member's published range was re-checked mechanically. The
artifact's `first_line_text` and `last_line_text` were compared with the document's line at each locator,
in the blob at `a22d8a41…`:

```
6 cowork_layer4_chordsymbol_design.md 1 629 629 FIRST MISMATCH LAST MISMATCH
7 cowork_layer3_keymode_design.md 1 536 536 first ok last ok
8 cowork_layer5_engagement_design.md 1 659 659 first ok last ok
```

**Position 6's two "mismatches" are line ends only.** That document's blob is stored with CRLF line ends,
so each line read from it ends in a carriage return the artifact's text does not carry. The first line reads
`'# Architectural Layer 4 — CHORD SYMBOL (with NON-CHORD TONES) — Architecture & Design\r'`, against the
artifact's text without the `\r`; the last reads `"  scorer's competitiveness constant.\r"`, likewise. With
the carriage return set aside, both texts match, so every range matches the file. This is not an apparatus
defect of the kind the Findings section names.

### 2.2 The members, as written

§6.6, §6.7 and §6.8 of `ratification_surfaces/cowork_comparison_l2_reading.md`, each in the shape §6.1 to
§6.5 use:

- the manifest header, including a remark on what kind of text the member is and which placement readings
  apply;
- the rows, numbered from M.1;
- the *not a statement* list;
- the four foot sections: the arithmetic, the distribution, the current-text axis with its DIFFERS list, and
  the marks.

Their statement counts, their *not a statement* counts, their distributions and their current-text axes are
at each member's own foot and at §13, and are not restated here (D-431).

**In each member's commit:**

- §0's row for that position became **DONE (§6.M)**, and §0's stop paragraph was rewritten to be true of the
  file. The first and second batches' stops are kept as their own sentences.
- The member's RELOCATED rows were appended to §10, its QUARANTINED rows with their audit questions to §11,
  and its ADOPTED — proposed rows and every DIFFERS to §12.
- §13 gained the member's row, and the running totals with the arithmetic check restated.
- §16's progress clause was brought true.

**Member 8 relocates no row and proposes none.** §10's foot says so in words, and §12's proposals list
gained nothing. **The one banner edit** was made in member 6's commit, exactly as 1(f) orders:
*"and further under `records/cc/instructions/cc_instruction_l2_comparison_tabulation_third_2026_09_27.md` Task
1,"* inserted after the second dispatch's Task 1 words.

### 2.3 How the rows were checked before each commit (1(g))

The rows were re-read against the file mechanically as well as by eye, over scratch copies taken from git
objects by explicit hash. For each member:

- **A quotation check.** Every quoted outgoing statement, and every *not a statement* quotation, was
  compared with the member's text at the object, with whitespace collapsed, emphasis marks stripped and
  the source's block-quote prefixes removed. Every short quotation of the derivation or the outgoing text
  inside the axis and difference sentences, and inside §12's added entries, was compared against both
  texts. **Every quotation matches its source.**
- **A count check.** The claims, the dispositions and the verdicts were counted from the member text
  itself. Every claim was reconciled to exactly one disposition and at least one verdict, and every row
  naming a statement §6.3 names as NEAREST was checked to say so. The foot's arithmetic and §13 are taken
  from that count.
- **A build check.** The member was inserted into the committed reading file in scratch, and the build was
  verified before placing:
  - §6.1 up to the previous member was byte-identical to the parent blob's span;
  - §10, §11 and §12 named exactly the member's RELOCATED, QUARANTINED, proposed and DIFFERS sets;
  - the diff outside the member touched only the ordered updates.
- **A word scan.** This session's own prose, with quotations removed, was scanned for British spellings and
  for non-musical uses of the reserved words.
- **A consistency check, member 8.** Every *"travelling with Row 8.n"* was checked to point at a row of the
  same disposition, and every *"as at Row 8.n"* at a row carrying the same derived statement and verdict.

**The corrections those checks caught, all made before the commit:**

- rows naming L2-S31 without the NEAREST mention §6.3 entry 1 requires (member 6);
- a derived statement cited in a row with no verdict against it (member 6, removed; and one sentence of
  member 8's, removed);
- a sentence of member 8 at line 266, inside D-384's home as cited, first left unmarked and then marked
  WITHHELD;
- a sentence of member 8 at lines 161–162, first left untabulated, then inserted as its own row; the
  member was renumbered by script, which mapped every in-member row reference;
- non-musical uses of the reserved words, and British spellings, in this session's own prose. These were
  *resolve* for settling, *part*, *scale*, *measure*, *bar* for a threshold, *beat*, *sharpen*, a bare
  *tie*/*tied*/*ties*, *rest*, *resolution* for a field name, *neighbour*, *behaviour* and *labelled*. Each
  was rephrased. The code names `resolver` and `ResolutionBasis`, and the compound *tie-break*, were kept.

### 2.4 The commits

| Member | Commit | Reading-file blob | Staged set, proved against the parent tree |
|---|---|---|---|
| 6 | `ba275ceb82f294cde6a2ab2a82d48fce1dc2624d` | `afa2883c…` → `cfec72a0bdb8387b5ba8b083402b180fe2cac2b6` | the reading file only |
| 7 | `413c0adba12c479968f1e9d8c4fb9ddebfe8f81d` | `cfec72a0…` → `bf0c16ff3e525b34968360a969600280a87c9cbe` | the reading file only |
| 8 | `a22d8a41affe6182e0abed22c2e60af336cc25ae` | `bf0c16ff…` → `0b2ae38e7fd996d9b94f593e15610e975fa40767` | the reading file only |

Each subject is `comparison L2: member <M> tabulated - <n> outgoing statements placed, proposals only`, with
`<n>` the member's manifest-header count, as 1(g) orders. After each push, `origin/master` read the new tip
at the ref file. For member 8, the staged set proved against the parent tree was:

```
$ git diff-tree -r --name-status cc6c99522aabfdb4daa69e6b995ceafbb4ee541f 01e162aa053fd4bf8a94b911268fee66c5dc2cce
M	ratification_surfaces/cowork_comparison_l2_reading.md
```

**The chain of this batch, read at the objects:**

```
commit 0ee62fc2eba2635c857047c000d6724349db55b1
parent 3158c3c24c031505f55ad19190a09d766614fd75
subject record: entry 264 and the third L2 tabulation dispatch
 2 files changed, 786 insertions(+)
commit ba275ceb82f294cde6a2ab2a82d48fce1dc2624d
parent 0ee62fc2eba2635c857047c000d6724349db55b1
subject comparison L2: member 6 tabulated - 272 outgoing statements placed, proposals only
 1 file changed, 3013 insertions(+), 16 deletions(-)
commit 413c0adba12c479968f1e9d8c4fb9ddebfe8f81d
parent ba275ceb82f294cde6a2ab2a82d48fce1dc2624d
subject comparison L2: member 7 tabulated - 224 outgoing statements placed, proposals only
 1 file changed, 2524 insertions(+), 14 deletions(-)
commit a22d8a41affe6182e0abed22c2e60af336cc25ae
parent 413c0adba12c479968f1e9d8c4fb9ddebfe8f81d
subject comparison L2: member 8 tabulated - 212 outgoing statements placed, proposals only
 1 file changed, 2659 insertions(+), 14 deletions(-)
```

### 2.5 §6.1 to §6.5 proven untouched (A5)

The span from `### 6.1 — ` up to the line before `## 7.` in the blob at `3158c3c2…`, and the span from
`### 6.1 — ` up to the separator before `### 6.6 — ` in the last member commit's blob `0b2ae38e…`, were
extracted to scratch files outside the repository and compared there:

```
at 3158c3c2 441976 6dc9b33b968cc89668ef8962f5b4cbc2753ff2f75739dabd499c2afe4777ee6a
at last member commit 441976 6dc9b33b968cc89668ef8962f5b4cbc2753ff2f75739dabd499c2afe4777ee6a
identical: True
```

At each member's own build, the same kind of check proved every earlier member byte-identical to its
parent blob. At member 7 the span was §6.1 up to §6.6; at member 8 it was §6.1 up to §6.7.

### 2.6 The readings applied, and the cases they could not decide

The two reading rules at the head of §6 were applied unchanged. So were the second batch's three
placement readings, as the dispatch's premise ledger orders:

- glossary entries and runtime scenarios are tabulated;
- an item title that is a noun phrase or a label is listed under *not a statement*, and one that states a
  plan or an event is placed HISTORICAL;
- a description of a built, dormant layer's mechanism is QUARANTINED, and a ruled rule a derived statement
  contradicts is UNPLACED.

As the ledger states, this session read the third reading as reaching whichever dormant layer a member
describes. Where those readings did not decide a line by themselves, this session took the further readings
below, applied throughout and stated in each member's manifest so they can be challenged. **None is
ruled.**

- **A design principle is placed on its own terms**, against the derived statements that speak to it.
- **A build state, a plan, an owed build or an owed measurement is HISTORICAL.**
- **A rejected alternative named with its reasons is listed under *not a statement*** (member 8).
- **A rule the text records as a ruling, or as a chosen design decision, that a derived statement
  contradicts is UNPLACED even where the sentence lies outside the ruling's home as cited** — for instance a
  later restatement of the same rule. It is marked *travelling with* the home row, and WITHHELD is marked
  only inside the home.
- **Cross-member travelling.** Where a member-6, -7 or -8 row describes the same dormant mechanism an
  earlier member's QUARANTINED row already asks about, the row travels with that earlier row. Examples are
  *travelling with Row 5.63*, *6.192(ii)*, *7.9(ii)* and, in member 7, *Row 2.27*, *2.47(ii)* and
  *2.17*. Every cross-member target was checked at the committed reading file to exist and to be
  QUARANTINED.
- **Two boundary marks.** In member 6, the sentence that opens a line before D-331's home as cited and holds
  the whole of it is marked WITHHELD. In member 7, the sentence that opens a line before D-348's home and
  carries its first claim is marked WITHHELD, while the sentence that opens inside D-343's home and runs
  past its last line is not marked. Each is stated at its member's foot. **Member 8 has no boundary case.**

**No case arose that these readings could not decide.**

### 2.7 The members done and not done

- **DONE: positions 1 to 8.** Positions 6, 7 and 8 were done by this batch.
- **NOT DONE: positions 9 to 62.** They are UNTOUCHED: not read for tabulation, not quoted, not counted and
  not placed. **Nothing is partly worked.**
- **The next writing resumes at position 9**, `cowork_stage5_fitter_design.md`, whole.
- §7, §8, §9 and §14 of the reading file stay NOT YET WRITTEN.

### 2.8 The next member's size, looked at as 1(h) orders

**Position 9's size gives reason to doubt that a fresh session can finish it whole, and this batch's own
experience adds this to what the writing side already knows.** Over positions 6, 7 and 8, a member of
roughly 540 to 660 lines took a whole member's worth of this session's capacity: its rows, its checks and
its build came to a scratch draft of roughly 145 to 185 KB per member. Position 9 is about 2.3 times member 8's
length by line and about 2.7 times by byte. Scaled on that experience, its draft would run to several
hundred KB before its checks, and it would be tabulated from a context already carrying the ordered first
read. **That is a question for the writing side and the user under 1(h) and D-671, not something this
batch solves. The member was not opened and not split.**

**E1: MET for positions 6, 7 and 8.**

- The manifest.
- Every outgoing statement with exactly one disposition, or UNPLACED with what was read.
- Every DIFFERS with its one-sentence difference, and nothing chosen.
- The marks of 1(c) where they apply. **No SEEN home lies in any of the three members**, and each foot says
  so.
- The transfer list, audit questions and proposals gathered at §10, §11 and §12.
- §0 and the §16 progress clause true of the file.
- The capacity judgment stated before each member.
- No recommendation anywhere.
- A5 intact, §6.1 to §6.5 included.

---

## 3. Task 2 — the close

**2(a) — the `STATUS.md` entry**, written first, at the top. The `Last updated: ` prefix was moved to it from
the second batch's entry. Quoted whole:

> *Last updated: 2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_comparison_tabulation_third_2026_09_27.md`. **★★ THE L2 TABULATION CONTINUED FROM POSITION 6: POSITIONS 6, 7 AND 8 — `cowork_layer4_chordsymbol_design.md`, `cowork_layer3_keymode_design.md` AND `cowork_layer5_engagement_design.md`, EACH WHOLE — ARE NOW TABULATED, AND POSITIONS 9 ONWARD ARE UNTOUCHED.** ★ **THE RECORDS ARE COMMITTED** — this dispatch and `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_sixty_four.md`, each checked at its blob for a complete final line before it was staged. ★ **THE READING FILE `ratification_surfaces/cowork_comparison_l2_reading.md` IS EXTENDED BY THREE MEMBERS, ONE COMMIT EACH**: positions 1 to 8 are now tabulated, every outgoing statement of positions 6, 7 and 8 placed under exactly one proposed disposition beside the current-text axis, the file's transfer list, audit questions, proposals and distribution updated in each member's commit, and its first five members proven byte-unchanged at the objects. ★ **THE WRITING STOPPED AT THE MEMBER BOUNDARY AFTER POSITION 8** under the dispatch's capacity judgment, position 9 — `cowork_stage5_fitter_design.md` — judged not finishable whole in the context that remained; positions 9 onward are UNTOUCHED, not partly worked (D-672), and the file's own §0 says where the next writing resumes. ★★ **EVERY DISPOSITION IS A PROPOSAL AND NOTHING IS APPLIED**: no outgoing text, derivation, brief, boot pack or register was edited; the five questions the derivation marks for the user are not put; no recommendation is made anywhere. No session booted; no open-items row created, flipped or discarded; no decisions-register identity allocated; no tool source edited but the forward bound's authored aiming; no governing document amended but this file and its archive; no `src/` file, build, test, golden, score corpus or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_l2_comparison_tabulation_third_2026_09_27.md` — and no figure is restated here (**D-431**).)*

No existing sentence of `STATUS.md` was rewritten or removed by hand. The prefix moved from the second
batch's entry to this one, which is the forward bound's declared adjustment.

**2(b) — the forward bound.** `STATUS.md`'s object was checked first. `git rev-parse <commit>:STATUS.md`
gives blob `10b6894dc1d95bbb4ae9da837c2c97defb280e88` at `0ee62fc2…` (Task 0), at `3158c3c2…` and at the
last member commit `a22d8a41…`: the same object. **The aiming set:**

| Field | Value |
|---|---|
| `BASE_COMMIT` | `0ee62fc2eba2635c857047c000d6724349db55b1` |
| `PREVIOUS_BATCH_DISPATCH` | `cc_instruction_l2_comparison_tabulation_second_2026_09_27.md` |
| `ACT_DATE` | `2026-09-27` |
| `DISPATCH` | `cc_instruction_l2_comparison_tabulation_third_2026_09_27.md` |
| `TASK` | `"Task 2"` |
| `MOVE_KIND` | `"ordinary"`, unchanged |
| `RULINGS` | unchanged |

One row was appended to `PREVIOUS_AIMINGS`. The second batch's aiming was already its last row and was not
appended again. The head comments were amended as the previous batches amended them, each field's former
value named in its comment (#12). Source blob `9364ce7ca288299a8f8c23bae61ebe1afdf01f18` →
`3f71f8e86cf27e5cc8052ad5b7abae95aaff2455` (`git diff --numstat` between the two blobs: 46 added, 5
removed).

```
$ python tools/audit/gen_status_batch_bound.py --apply
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 2,033 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
exit:0
$ python tools/audit/gen_status_batch_bound.py --check
  entries moved: 1, 2,033 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
exit:0
```

**The entry that moved, by name** (OI-379 — a green `--check` is not the proof): the second batch's entry,
the one naming `records/cc/instructions/cc_instruction_l2_comparison_tabulation_second_2026_09_27.md`.
`status_batch_bound.json` records its opening as `*2026-09-27 (CC —
`records/cc/instructions/cc_instruction_l2_comparison_tabulation_second_2026_09_27.md`. **★★ THE L2
TABULATION CONTINUED FROM POSITI`, with membership `names the dispatch` and
`the_one_declared_adjustment_applied: true`. That entry's text now stands once in `STATUS_ARCHIVE.md`, under a
header naming this act. **The prediction held**: exactly that one entry moved. **The two 2026-09-02 entries
stayed** — both still open with `*2026-09-02 (CC` in `STATUS.md` — and were not moved by hand. No STOP.
`STATUS_ARCHIVE.md` gained lines and lost none (blob `4270cba663ca0e896eee3090cf538021fc9da04c` →
`a4453322fb470ad8ba4f390cdd0001d17b204f87`: four lines added, none removed).

**2(c) — the regenerations, each then `--check`, all exit 0, no `STOP:` line and no traceback.** They ran in
the dispatch's order, with `gen_session_start_read_size.py` last and after the final edit to `STATUS.md`:

```
$ python tools/audit/gen_evidence_pin_membership.py
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
exit:0
$ python tools/audit/gen_evidence_pin_membership.py --check
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
exit:0
$ python tools/audit/gen_l0_l1_outgoing_population.py
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
exit:0
$ python tools/audit/gen_l0_l1_outgoing_population.py --check
l0_l1_outgoing_population.json re-derives
exit:0
$ python tools/audit/gen_l2_outgoing_population.py
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
exit:0
$ python tools/audit/gen_l2_outgoing_population.py --check
l2_outgoing_population.json re-derives
exit:0
$ python tools/audit/gen_defense_share.py
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
    of the whole session-start read (246552): 5.26%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
exit:0
$ python tools/audit/gen_defense_share.py --check
the defense-share measurement re-derives
  (the same lines as the write run above, identical)
exit:0
$ python tools/audit/gen_session_start_read_size.py
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
    STATUS.md                                                                 11390
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 246552
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 246552 [ruled membership]  (-120569, -32.84%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 246552 [ruled membership]  (-50280, -16.94%)  <- CROSSES A REGIME BOUNDARY
exit:0
$ python tools/audit/gen_session_start_read_size.py --check
the session-start read measurement re-derives
  (the same lines as the write run above, identical)
exit:0
```

*(Where a line reads "(the same lines as the write run above, identical)", the `--check` run printed the
write run's lines after its first line, character for character. The full captures are the scratch files
`regen_*.txt` beside the guard captures.)*

**What moved.** Each artifact's blob at the last member commit `a22d8a41…` was compared with the new blob. The
three that moved were compared line by line after both were extracted from git objects and the working tree
into scratch:

```
tools/audit/evidence_pin_membership.json   54f774d82a2d2e5a9ec99b13666bd83d63ac5257 -> 54f774d82a2d2e5a9ec99b13666bd83d63ac5257 (same)
tools/audit/l0_l1_outgoing_population.json e310fb57ac53f9a06f8a9295d70c17ec143e3ce3 -> e310fb57ac53f9a06f8a9295d70c17ec143e3ce3 (same)
tools/audit/l2_outgoing_population.json    484518b81b3480c5f0e657c2743044c17a2bdd2b -> 84ad204d75ea8849e1f8adfdbbc26aac21252049
   one hunk: the STATUS.md residue record's first hit record ("line_number": 8, "term": "boundary"), its "line"
tools/audit/defense_share.json             b015b020574a83abd8f2a5c5aef0286c946a7afa -> 7a990839fac91653b130280bd943fc13a9a10699
   one hunk: "the_whole_ordinary_session_start_read"
tools/audit/session_start_read_size.json   68f19948cf7787cd3056c84cb403568df5f57659 -> cb23ba9f0a91f8d30c5267f59c6bb9c280c9ff7d
   six hunks: characters_per_member -> STATUS.md; total_characters; and, for each of the two earlier
   readings, to_total, change_in_characters and change_percent
tools/audit/status_batch_bound.json        157416fc6f83925449cbe4f1372ba313c0ef57cb -> 2c124983dae0f1c59ccf4b3cde162e292fef7cdf
   (rewritten by the forward bound's --apply, 2(b))
```

**Against A3: HOLDS.**

- **`evidence_pin_membership.json` and `l0_l1_outgoing_population.json` did not move.**
- **`l2_outgoing_population.json` moved in exactly one field, inside the `STATUS.md` residue record**: the
  first hit record's `line`. That hit is the term search's hit on the new `STATUS.md` entry line, which
  replaced the moved entry at the same line. No member of the outgoing population or of the tabulation
  population moved, and no file entered or left the population or the residue.
- **`defense_share.json` and `session_start_read_size.json` moved only in what `STATUS.md`'s new size
  moves.**

**2(d) — the closing guard capture**, write mode, exit 0, saved at
`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\4bb24b3f-9912-4418-9c90-9aff669b056a\scratchpad\guard_close2.txt`.
**Verdict by verdict against 0(f): the two capture files are byte-identical** (`cmp guard_open.txt
guard_close2.txt` printed nothing and exited 0). **THE CONDITION HOLDS**: every PASS still PASS, the same
twelve FAIL, the NOT RUN and HISTORICAL lines identical, population 80. `tools/audit/guard_state.json`
itself moved only in the captured output of two tools: the forward bound's *"entries moved"* line, and the
session-start read size's lines. The blob went from `7be0bb9e5f92283fda4061f9b3ff23db8afbdd27` to
`25ce197f6e6641818ce1d5a5e36d5d6264a4eedb`, 6 lines changed, and no verdict changed. *(A first closing
capture was run with an output-encoding setting the opening capture did not carry, and is set aside. §5,
item 6 says why.)* **The guard classification**, exit 2, naming exactly the four tools of the FACT:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

**E2: MET.** It is derived from the declared start state plus this batch's footprint (P-3). At the tree
carrying the close: population 80, zero STOPs in the runner, the failing set exactly the twelve named plus
none, and the classification STOP unchanged.

---

## 4. The assumptions, graded

- **A1 — HOLDS**, established by the enumeration at 0(c). There was exactly one tracked modification,
  `tools/audit/claude_md_finer_archive.json`, carried and not chased, and exactly the two untracked landing
  paths, within the standing untracked population. Nothing was staged. At the close,
  `python tools/audit/changed_paths.py` lists exactly the eight close files Task 3 names plus that standing
  modification, and the standing untracked population.
- **A2 — HOLDS**: exactly the twelve at the opening capture, and no thirteenth.
  `gen_evidence_pin_membership.py --check` PASSED, as predicted.
- **A3 — HOLDS**: see 2(c).
- **A4 — HOLDS.** No tool was added and none enrolled. Exactly one tool source was touched,
  `tools/audit/gen_status_batch_bound.py`'s authored aiming. `gen_l2_outgoing_population.py` and
  `gen_guard_state.py` were not edited. Population 80 throughout.
- **A5 — HOLDS**, verified at the objects.
  - `git diff-tree -r --name-status 3158c3c2… a22d8a41…` lists exactly three paths: the reading file and
    the two landed records.
  - The close commit adds only the files Task 3 names, proved at its staging.
  - The derivation and the brief are at the relayed blobs at `0ee62fc2…`, at `a22d8a41…` and in the
    working tree.
  - The pack directory `tools/audit/derivation_boot_pack/l2/` is tree `dae537febafb3df10f8899b0d60eb9227f9cdf8b`,
    and `derivation_boot_pack.json` is blob `db340baf15f7fa3ad1ab29d067f12a47b4354ace`, at both `3158c3c2…`
    and `a22d8a41…`.
  - Nothing in the batch's footprint lies under the input contract, the L0/L1 reading file, any outgoing
    text, the five tools A5 names, any governing document other than `STATUS.md` and `STATUS_ARCHIVE.md`,
    or any source of the decisions register.
  - **§6.1 to §6.5 of the reading file are byte-identical**, as shown at §2.5.

---

## 5. Declared departures

1. **The dispatch file was read before the derivation.** The user's opening line named only the dispatch,
   so it had to be read first to learn the ordered first read. The derivation was then the first read of
   anything else (§0).
2. **The pin was taken after the dispatch was read from the working tree**, which is the declared-departure
   route of the standing clause (P-2). The blob was proved unmoved at staging (`b4e6d17c…`).
3. **Each member was placed by building the extended reading file in scratch and copying it into place**,
   not by an editor edit, because a member's text is large. Each build started from the reading file's
   committed blob at the member's parent commit, read by `git show` at the explicit hash, so no
   working-tree content was read through the shell. Before staging, the copied file's hash was proved equal
   to the scratch build's.
4. **Every commit message carries the exact subject the dispatch gives**, followed by a co-author trailer
   line in the message body. The subject line itself is verbatim.
5. **The placement readings of §2.6** were taken and are stated in each member's manifest. **None is ruled.**
6. **The first closing guard capture was set aside and re-run.** It was run with
   `PYTHONIOENCODING=utf-8` in the environment, a setting this session had used for its own scratch scripts;
   the opening capture was run without it. Its verdicts were identical to the opening capture's. But one
   tool's captured stdout, `tools/open_items_split_check.py`, then carried a dash character where the
   committed capture carries a replacement character, so `guard_state.json` would have moved in a line the
   batch did not cause. The capture was re-run under the opening capture's conditions, without that setting.
   That re-run, `guard_close2.txt`, is byte-identical to the opening capture, and it is the one reported
   and committed. *(The first run's file, `guard_close.txt`, stays in scratch, and its verdict comparison
   is `gcmp_out.txt`.)*
7. **Two of this session's scratch checks were replaced mid-run, and are stated here so no reader relies on
   them.** A recursive value comparison written for 2(c) reported no difference for files whose bytes
   differed, so its output was discarded. A line-level comparison, `tdiff_*.txt`, was used instead; its
   results are the ones in 2(c). Neither is a repository tool.

*Operational notes, not departures.* The armed guard denied several commands, each for a stated reason:

- `cat`, `grep` or a heredoc aimed at a path the guard reads as a repository or scratch path;
- a `python -c` code string naming a path.

None was worked around. Each was re-run in the sanctioned form: the file tools, or a script file in scratch
run with absolute paths.

---

## 6. Findings of the run

**No finding number is allocated, and no apparatus defect was met.** Every member range matched the file,
every outgoing text parsed into statements, and every derived statement carries its six fields. **No 1(h)
finding arises**, since position 6 was finished whole. The doubt about position 9 is recorded at §2.8, as
1(h) asks, and is not a finding.

---

## 7. What this batch did NOT do

- **No disposition applied anywhere.** Every disposition in the reading file is a proposal. No outgoing
  text, derivation, brief, boot pack, pack artifact, input contract, L0/L1 reading file or source of the
  decisions register was edited.
- **No decision** on any disposition, difference, open question, the derivation or the method. **No verdict**
  on the deriving session's independence. **No recommendation** in the reading file, this report or any
  commit message. **The five questions the derivation marks for the user (OQ-L2-2, 4, 5, 8, 16) are not
  put.**
- **No session booted, and no subagent spawned.** No measurement of the analysis was built, designed, scoped
  or run.
- **No tool source touched but the forward bound's authored aiming.** No guard enrolment, and no freeze of
  the L2 pack.
- **No open-items row created, flipped or discarded; no decisions-register identity.** No `src/` change,
  golden or test, and nothing under `tools/corpus/`, `tools/robust_stop/` or `tools/dcml/`.
- **No disposition of any residue file or of any of the eight LISTED item-2 documents.**
- **§6.1 to §6.5 were not re-opened, re-tabulated, re-numbered or corrected.**
- **Positions 9 to 62 were not tabulated**, and are untouched. **No member was split by hand.**

**The plan's tell, in one sentence:** the batch produced **nothing** in the repository other than the landed
records, the reading file's three new member subsections with their updates to §0, §10 to §13 and the §16
progress clause and the one banner edit, the Task 2 files and this report. Outside the repository it
produced only scratch files: the member drafts, the counting, quotation-checking, build-verifying and
consistency scripts, the guard and regeneration captures, and the extracted comparison spans. It also
produced the loose git blob objects that `git hash-object -w` wrote for the ordered checks.

---

## 8. Self-check — the standing clause, run over the work on disk

1. **Principles.**
   - **#19**: the reading file establishes nothing and says so. Every row carries both texts' words and can
     be re-placed at the texts.
   - **#6**: the population's cut is the tool's, and no member was split by hand.
   - **#12**: the earlier batches' stops stay as their own sentences in §0, and UNPLACED, SILENT and every
     DIFFERS are kept. The first closing capture is kept in scratch rather than overwritten.
   - **#13**: the capacity judgment was stated before each member. The stop is a recorded member-boundary
     stop, not a partly worked member.
   - **#17(f)/D-431**: no artifact count is restated in the reading file or in this report's prose, save the
     1(h) sizes the dispatch orders and the rough estimate of §2.8, which is this session's own experience and
     not an artifact count. The tools' printouts are quoted verbatim.
   - **#24**: no difference between measured quantities is asserted.
2. **Conventions.** This session's prose is in American English: British spellings in authored prose were
   corrected, and left where they sit inside quotations. The reserved words were checked by a scan of each
   member's own prose, with quotations removed, and the non-musical uses found were rephrased before each
   commit (§2.3). No invented label is left undefined.
3. **Figures and premises.** Every quantity in this report is one of: a tool's verbatim printout, a git
   object identity, a pointer to an artifact field or to the reading file's feet and §13, or a 1(h) size read
   at the artifact. The premises were checked at their objects: the refs, the chain, the guard object, the
   two blobs, the pack, `STATUS.md`'s blob at the three commits and the §6.1 to §6.5 span.
4. **File-tools rule.** Working-tree content was read with the file tools. The shell ran git object queries
   by explicit hash, the sanctioned scripts, and scratch scripts reading scratch files and git objects. The
   commands the guard denied were re-run in the sanctioned form.
5. **Uncertainty.** No comparison of measured quantities is made. §2.8's estimate is stated as rough.

*Provenance: Claude Code, 2026-09-27, executing the dispatch above from its pinned blob. The close commit
carries this file, so its own hash, the pushed branch and `origin/master` after the push are reported in
the session's closing message and are at the git log.*
