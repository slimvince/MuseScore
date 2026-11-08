# Appendix — raw printouts for `cc_report_llm_correction_2026_11_07.md` (STOPPED at 1(e))

Every block below is a printout as the command produced it. Scratch files lived outside the repository in the session
scratchpad; their content is reproduced here.

## 0(a) — the pin

`git hash-object -w --no-filters records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md`

```
ce5fbebab416074fc54d140534a627aff4e4d1b6
```

`git cat-file -s ce5fbebab416074fc54d140534a627aff4e4d1b6`

```
73435
```

Before staging: `git ls-files -s -- records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md`

```
100644 ce5fbebab416074fc54d140534a627aff4e4d1b6 0	records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md
```

## 0(b) — the chain

`git cat-file -p 7c2d1bccc885b1e11204727f0800ffe20fd84b21` (first lines)

```
tree 880059cb7aa405b3482edb792726a7088bf1d18d
parent 8ac62876975b891fef7ed2fc87257383dcf2c33f
```

`git cat-file -p 8ac62876975b891fef7ed2fc87257383dcf2c33f` (first lines)

```
tree 15682b96ec5697fc68e482f42355c5c06ec21f28
parent 113b2ce680e527e81342d8f79d5acbad281334d7
```

## 0(c) — `python tools/audit/changed_paths.py` (A1 and the landing set)

Lines 1–15 and the last two lines verbatim; lines 16–402 are the standing `scratch_artifacts/` population, each a `??`
line, unchanged from the population the previous batches carried.

```
 M	docs/research_papers/BIBLIOGRAPHY.md
 M	docs/research_papers/README.md
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_five.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_four.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_one.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_three.md
??	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_two.md
...
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
403 changed path record(s) [worktree]
```

## 0(d) — last bytes: the script and its output

The script (scratch, outside the repository):

```python
# 0(d): for each landing file, write its blob with --no-filters, then read the blob back by hash
# and report size, last 70 bytes, count of zero bytes, and whether it ends in a newline after a complete line.
import subprocess, sys
PATHS = [
    "records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy.md",
    "records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_one.md",
    "records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_two.md",
    "records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_three.md",
    "records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_four.md",
    "records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_five.md",
    "records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md",
]
bad = 0
for p in PATHS:
    h = subprocess.run(["git", "hash-object", "-w", "--no-filters", p], capture_output=True, text=True, check=True).stdout.strip()
    data = subprocess.run(["git", "cat-file", "blob", h], capture_output=True, check=True).stdout
    zeros = data.count(b"\x00")
    ends_nl = data.endswith(b"\n")
    last_line = data.rstrip(b"\n").rsplit(b"\n", 1)[-1]
    print(f"{p}\n  blob {h}  size {len(data)}  zero_bytes {zeros}  ends_with_newline {ends_nl}")
    print(f"  last70 {data[-70:]!r}")
    print(f"  last_line_tail {last_line[-40:]!r}")
    if zeros or not ends_nl:
        bad += 1
print("RESULT:", "STOP" if bad else "ok", bad)
```

Output:

```
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy.md
  blob d360b1d4843e51701615363db1a2b42febd83864  size 6607  zero_bytes 0  ends_with_newline True
  last70 b'n entry 569. The user\'s words: the opening instruction;\n"shortened".*\n'
  last_line_tail b'"shortened".*'
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_one.md
  blob f83da1cca7e840fa280f8b7a56df1637e41dcacf  size 7932  zero_bytes 0  ends_with_newline True
  last70 b'are/algorithms. Then we can consolidate and fix whatever is\nneeded."*\n'
  last_line_tail b'needed."*'
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_two.md
  blob f3f7c16919b66c28b16584a3bad9d6921e9fec07  size 7061  zero_bytes 0  ends_with_newline True
  last70 b'n entry 571. The user\'s words: the opening instruction;\n"shortened".*\n'
  last_line_tail b'"shortened".*'
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_three.md
  blob b93f1dd18ba910444f30d0808682fa7979dff8ab  size 6027  zero_bytes 0  ends_with_newline True
  last70 b'n entry 572. The user\'s words: the opening instruction;\n"shortened".*\n'
  last_line_tail b'"shortened".*'
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_four.md
  blob 2c6a3f15500784297b97a4a5510f045c76d662ae  size 5676  zero_bytes 0  ends_with_newline True
  last70 b' The user\'s words: the opening instruction;\n"shortened"; "continue".*\n'
  last_line_tail b'"shortened"; "continue".*'
records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_five.md
  blob ffa71ddc2c69da15924668e1ecb1764ab9be62e7  size 4584  zero_bytes 0  ends_with_newline True
  last70 b'n entry 574. The user\'s words: the opening instruction;\n"shortened".*\n'
  last_line_tail b'"shortened".*'
records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md
  blob ce5fbebab416074fc54d140534a627aff4e4d1b6  size 73435  zero_bytes 0  ends_with_newline True
  last70 b' (an unexplained red is a STOP).\n- **The banner is set to RELEASED.**\n'
  last_line_tail b'- **The banner is set to RELEASED.**'
RESULT: ok 0
```

## Boot — `python tools/audit/gen_per_session_reading.py --check` (exit 2)

```
STOP: a member of a derived population has no add-commit: records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy.md
```

## 0(e) — `python tools/audit/changed_paths.py --staged`

```
A	records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_five.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_four.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_one.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_three.md
A	records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_two.md
7 changed path record(s) [staged]
```

## 0(f) — the opening capture, `python tools/audit/gen_guard_state.py --check` (exit 1), whole

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

`python tools/audit/gen_guard_classification.py --check` (exit 2):

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_l3_outgoing_population.py', 'tools/audit/gen_per_session_reading.py', 'tools/audit/gen_withheld_family_reading.py']
```

## 1(a) — the script and its output

The script is the dispatch's 1(a) block, saved verbatim to the scratchpad as `task1a.py` and run from the repository
root (its text is in the dispatch at lines 330–398 of the pinned blob `ce5fbebab416074fc54d140534a627aff4e4d1b6`; not
re-copied here, #6). Output (exit 0):

```
applied: 7 superseded, 2 noted; lines 22553 unchanged
```

Numstat, between explicit blobs (the working-tree `git diff --numstat` the dispatch names was refused by the shell-read
guard; see the report's departures):

```
git rev-parse 566d37e583da3ee23d2d46957ead8eb202290973:tools/audit/decisions/backbone_decisions.json
9f34b0cab42c2fc69d3af8613ac3e0a9237d6b03
git hash-object -w --no-filters tools/audit/decisions/backbone_decisions.json
92081e6df087ce6a5fc913c2601e9c56dd2b10b9
git diff --numstat 9f34b0cab42c2fc69d3af8613ac3e0a9237d6b03 92081e6df087ce6a5fc913c2601e9c56dd2b10b9
16	16	9f34b0cab42c2fc69d3af8613ac3e0a9237d6b03 => 92081e6df087ce6a5fc913c2601e9c56dd2b10b9
```

## 1(b) — the regeneration

```
$ python tools/audit/decisions/gen_decisions_register.py --check        (exit 1)
STALE vs the data: DECISIONS.md
STALE vs the data: decisions/group_N.md
$ python tools/audit/decisions/gen_decisions_register.py                (exit 0)
wrote 20 files: DECISIONS.md (the index, 772 lines) + 19 group files under decisions/ (477 decisions)
$ python tools/audit/decisions/gen_decisions_register.py --check        (exit 0)
the register matches the data (20 files: the index + 19 group files)
```

## 1(c) — the regenerated files' diff, between explicit blobs (normalized with git's filters)

Blobs: `DECISIONS.md` `4a945aaded7db494934fdbd8b545b8e29e0f4551` → `262c97c150468dd674368ff5b53ebc98ac5762d0`
(numstat `9	9`); `decisions/group_N.md` `1512ad31c496d25f1358f5d9dd71a1356a0b9d78` →
`11061aa54286a54dcb8daace33f8ce186e98ccec` (numstat `16	16`). The first `--no-filters` hash of the working-tree files
(`06e1631a…`, `6f56c744…`) differed from the committed blobs on every line, because those working-tree copies carry
CRLF line endings that the committed blobs do not; the diff below is between the filter-normalized blobs, which are the
blobs `<T1>` committed.

`DECISIONS.md`:

```
@@ -142,8 +142,8 @@
 | Decisions recorded | **477** |
 | — of which live | 427 |
 | — of which superseded in fact | 7 |
-| — of which superseded by | 9 |
-| — of which deferred | 21 |
+| — of which superseded by | 16 |
+| — of which deferred | 19 |
 | — of which shelved with evidence | 2 |
@@ -591,15 +591,15 @@
-| D-440 | … | DEFERRED | 2026-08-04 · user | `ARCHITECTURE.md` |
-| D-441 | … | DEFERRED | 2026-08-04 · user | `ARCHITECTURE.md` |
-| D-442 | … | NOT STATED | 2026-08-04 · user | `docs/llm_integration.md` §4.3 |
-| D-443 | … | NOT STATED | 2026-08-04 · user | `docs/llm_integration.md` §8.1 |
+| D-440 | … | SUPERSEDED BY Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` | …
+| D-441 | … | SUPERSEDED BY Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` | …
+| D-442 | … | SUPERSEDED BY Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` | …
+| D-443 | … | SUPERSEDED BY Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` | …
 | D-444 | … | NOT STATED | …
 | D-445 | … | NOT STATED | …
-| D-446 / D-447 / D-448 | … | NOT STATED | …
+| D-446 / D-447 / D-448 | … | SUPERSEDED BY Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` | …
```

(The decision titles are elided with "…" in this transcription only; the full hunk is reproducible with
`git diff 4a945aaded7db494934fdbd8b545b8e29e0f4551 262c97c150468dd674368ff5b53ebc98ac5762d0`.)

`decisions/group_N.md`: sixteen changed lines, reproducible with
`git diff 1512ad31c496d25f1358f5d9dd71a1356a0b9d78 11061aa54286a54dcb8daace33f8ce186e98ccec` — seven **Status.** lines
from `DEFERRED` / `NOT STATED` to `SUPERSEDED BY Ruling 1 of \`…llm_test_only_sitting.md\``, and nine **Provenance.**
lines each the former line with the 1(a) sentence appended at its end (the `★ USER RULING 2026-11-07 …(was deferred|was
not stated)…` sentence for the seven, the `★ NOTE 2026-11-07 … Status unchanged.` sentence for D-444 and D-445). No other
line changed.

## 1(d) — `python tools/audit/changed_paths.py --staged`

```
M	DECISIONS.md
M	decisions/group_N.md
M	tools/audit/decisions/backbone_decisions.json
3 changed path record(s) [staged]
```

## 1(e) — the capture after `<T1>`: its difference from 0(f)

The whole capture is 0(f)'s with exactly these lines changed (`diff cap_0f.txt cap_1e.txt`):

```
38c38
<   [PASS] tools/audit/gen_rulings_sort.py --check
---
>   [FAIL] tools/audit/gen_rulings_sort.py --check
61,62c61,62
<   [PASS] tools/audit/gen_session_start_read_size.py --check
<   [PASS] tools/audit/gen_defense_share.py --check
---
>   [FAIL] tools/audit/gen_session_start_read_size.py --check
>   [FAIL] tools/audit/gen_defense_share.py --check
79,80c79,80
<   [PASS] tools/audit/decisions/reaim_home_anchors.py --check
<   [PASS] tools/audit/decisions/gen_live_prohibition_pointers.py --check
---
>   [FAIL] tools/audit/decisions/reaim_home_anchors.py --check
>   [FAIL] tools/audit/decisions/gen_live_prohibition_pointers.py --check
109c109
< 83 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
---
> 83 guard(s) run, 19 failing, 4 not run, 20 historical record(s)
```

Each newly failing tool's own `--check`:

```
=== tools/audit/gen_rulings_sort.py
FAIL: the rulings sort does not re-derive: C:\s\MS\tools\audit\rulings_sort_classification.json
FAIL: the rulings-sort surface does not re-derive: C:\s\MS\ratification_surfaces\cowork_rulings_sort_surface_2026_08_16.md
exit:1
=== tools/audit/gen_session_start_read_size.py
STALE vs the measurement: session_start_read_size.json does not re-derive
exit:1
=== tools/audit/gen_defense_share.py
STALE vs the measurement: defense_share.json does not re-derive
exit:1
=== tools/audit/decisions/reaim_home_anchors.py
REFUSED: re-serializing the untouched backbone is not byte-identical to the committed file, so writing would reformat it.
exit:2
=== tools/audit/decisions/gen_live_prohibition_pointers.py
REFUSED: re-serializing the untouched backbone is not byte-identical to the committed file, so writing would reformat it.
exit:2
```

## The read-only re-serialization probe (scratch, no repository write)

```python
# Read-only probe: how does json.dumps(indent=2) of the edited data file differ from the file's bytes?
import json, difflib, pathlib
P = pathlib.Path("tools/audit/decisions/backbone_decisions.json")
raw = P.read_bytes().decode("utf-8")
rt = json.dumps(json.loads(raw), indent=2, ensure_ascii=False) + "\n"
a, b = raw.split("\n"), rt.split("\n")
print("file lines", len(a), "roundtrip lines", len(b), "equal", raw == rt)
removed = added = 0
for l in difflib.unified_diff(a, b, lineterm="", n=0):
    if l.startswith("---") or l.startswith("+++") or l.startswith("@@"):
        continue
    if l.startswith("-"):
        removed += 1; print("REMOVED:", l[:150])
    elif l.startswith("+"):
        added += 1; print("ADDED:  ", l[:150])
print("removed", removed, "added", added)
```

Output (the seven REMOVED/ADDED pairs are identical; one shown):

```
file lines 22554 roundtrip lines 22561 equal False
REMOVED: -      "status": "superseded-by", "superseded_by": "Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`",
ADDED:   +      "status": "superseded-by",
ADDED:   +      "superseded_by": "Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`",
… (six more identical pairs)
removed 7 added 14
```
