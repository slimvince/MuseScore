# CC REPORT — THE L2 INPUT CONTRACT: THE FIVE CUTS OF THE CUT-LIST SITTING, AND THE CLOSE (2026-09-27)

> Executes `records/cc/instructions/cc_instruction_l2_input_contract_cuts_2026_09_27.md`, run from Task 0
> in order. **No STOP fired.** Every expected result appeared as the dispatch states it. Scratch files
> named below (`scratchpad/…`) live in the session scratchpad outside the repository working tree,
> `C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\ef039709-883c-4360-8fe7-eef26893e103\scratchpad\`,
> and are not committed.
>
> *Before Task 0, the ordinary session-start read was performed (Conventions, Ruling 5 of
> `records/cowork/rulings/cowork_rulings_2026_08_29_ratification_sitting.md`): `STATUS.md`, the head of
> `DECISIONS.md`, and the gating row identities at `tools/audit/nongating_apparatus_rows.json` →
> `★_the_live_gating_answer` → `gating_ids`.*

## 1. Task 0 — the start state, and the new records committed

**0(a) — the pin.** `git hash-object -w records/cc/instructions/cc_instruction_l2_input_contract_cuts_2026_09_27.md`
→ `68ab1be6be7630b170d155d20acb8a6efc5e5ed8`; `git cat-file -s` → `19211`. Every later re-read of the
dispatch was of this blob's content (the working file never changed).

**0(b) — the refs, read with the file tools.** `.git/refs/heads/master` =
`01b59a2df577bca7e7db38a75c35fe312ce82a74`; `.git/refs/remotes/origin/master` =
`01b59a2df577bca7e7db38a75c35fe312ce82a74`. **They agree, at the expected value.**

**0(c) — the working tree.** `python tools/audit/changed_paths.py`, exit 0, 397 records
(`scratchpad/changed0.txt`). Every record other than the untracked paths under `scratch_artifacts/`,
verbatim:

```
 M	tools/audit/claude_md_finer_archive.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	records/cc/instructions/cc_instruction_l2_input_contract_cuts_2026_09_27.md
??	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_five.md
??	records/cowork/rulings/cowork_rulings_2026_09_27_l2_cut_list_sitting.md
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
397 changed path record(s) [worktree]
```

**Nothing was staged** (`git diff --cached --name-only` printed nothing).

The last bytes of each text file 0(d) commits (`scratchpad/tailcheck.py`, reading the bytes):

```
records/cc/instructions/cc_instruction_l2_input_contract_cuts_2026_09_27.md
  size 19211 NUL anywhere: False ends with NUL: False ends with newline: True
  last 160 bytes: b"_batch_bound.py`'s\nauthored inputs and the last row of `PREVIOUS_AIMINGS`; `STATUS.md`'s head entry; and the previous\ndispatch, whose shape this file follows.*\n"
records/cowork/rulings/cowork_rulings_2026_09_27_l2_cut_list_sitting.md
  size 5305 NUL anywhere: False ends with NUL: False ends with newline: True
  last 160 bytes: b'register_rule_c_suspension_2026_08_28.md` is the route, not taken).\n\n---\n\n*Provenance: Cowork, 2026-09-27, both refs at `01b59a2df5\xe2\x80\xa6`. The user\'s word: "A".*\n'
records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_five.md
  size 4943 NUL anywhere: False ends with NUL: False ends with newline: True
  last 160 bytes: b'efore anything\nelse; if they still read `01b59a2df5\xe2\x80\xa6`, the batch has not run.\n\n*Provenance: Cowork, 2026-09-27 (Stockholm), the sitting booted on entry 254.*\n'
```

No trailing NUL; each ends on a complete line.

**0(d) — the commit.** Sizes by `git hash-object -w --no-filters <path>` then `git cat-file -s`:

```
records/cc/instructions/cc_instruction_l2_input_contract_cuts_2026_09_27.md 68ab1be6be7630b170d155d20acb8a6efc5e5ed8 19211
records/cowork/rulings/cowork_rulings_2026_09_27_l2_cut_list_sitting.md d76ae0f4970e5534eb5c0e7d01d0ba50c7103fdf 5305
records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_five.md 46fabbc2d17c96d0d5a57f49fe7321a6136289c3 4943
```

The dispatch is at the blob 0(a) pinned; the ruling record is 5,305 as stated; **the handoff entry
exists and its size is 4,943** (no size was stated for it). The staged set, proved before committing:

```
A	records/cc/instructions/cc_instruction_l2_input_contract_cuts_2026_09_27.md
A	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_five.md
A	records/cowork/rulings/cowork_rulings_2026_09_27_l2_cut_list_sitting.md
100644 68ab1be6be7630b170d155d20acb8a6efc5e5ed8 0	records/cc/instructions/cc_instruction_l2_input_contract_cuts_2026_09_27.md
100644 46fabbc2d17c96d0d5a57f49fe7321a6136289c3 0	records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifty_five.md
100644 d76ae0f4970e5534eb5c0e7d01d0ba50c7103fdf 0	records/cowork/rulings/cowork_rulings_2026_09_27_l2_cut_list_sitting.md
```

Held back and not staged: `tools/audit/claude_md_finer_archive.json` (B7), the untracked research paths
above, and `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` (a score file, B3).

**The Task 0 commit: `9f42ec57cb75b36267aebfc37fc0be3749d9346f`** — three files, 463 insertions. Not
pushed at that point.

**0(e) — the opening guard capture**, `python tools/audit/gen_guard_state.py`, exit 0, saved at
`C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\ef039709-883c-4360-8fe7-eef26893e103\scratchpad\guard_open.txt`
(the tool also wrote `tools/audit/guard_state.json`, the guard set's own artifact). Every verdict,
verbatim:

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
  [FAIL] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [PASS] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --check
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
79 guard(s) run, 13 failing, 4 not run, 19 historical record(s)
```

`gen_evidence_pin_membership.py --check` FAILs here, as the dispatch anticipated after a new ruling
record lands.

**The guard classification**, `python tools/audit/gen_guard_classification.py`, exit 2 — the expected
STOP (B7), reported whole and carried:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

## 2. Task 1 — the five cuts

**1(a).** `git hash-object tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md`
= `a6d84e6ef3423f6bf09cb0acd7763d1b82346320` (as required). `git hash-object
cowork_derived_specification_l0_l1_2026_09_03.md` = `bbde68b96d64bd55346f1a14322bf0e2bc0e11a3` (as
expected).

**1(b) — the cut script**, `scratchpad/cut_input_contract.py`, not committed, verbatim:

```python
import subprocess
import sys

PATH = "tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md"

CUTS = [
    ("1 (lines 1281-1283)", [
        ' The outgoing',
        "  detector over an event pair of chords, and the factorization's features evaluated in candidate key k",
        '  with fitted weights, are *"L2\'s cadence factor … a consumer reading L1\'s cues and its own state"*.',
    ]),
    ("2 (lines 1165-1166)", [
        " — and relating them is L2's cadence-factor covariate and L3's",
        "  alignment window, to which Rows 11.12 and 13.14 are relocated",
    ]),
    ("3 (lines 1316-1317)", [
        ', Row 11.8\'s *"not in the first',
        '  structure"* being L2\'s choice not to consume it',
    ]),
    ("4 (lines 296-299)", [
        ' The',
        "    three-part root-pinning test is L2's decision and is RELOCATED there; its first part is S-14, and",
        '    its second — two spellings of one pitch class in one slice — *"is readable from the sounding set',
        '    L1 publishes by event identity"*.',
    ]),
    ("5 (lines 1578-1580)", [
        " The pack's design intent defines a pedal *point* voice-independently",
        "  (D-207) — a different thing (a held tone in the harmony) from a pedal *mark* (a damper instruction);",
        "  the two words are kept apart here.",
    ]),
]

EXPECTED_LINES = {
    "1 (lines 1281-1283)": '  is gated on boundary evidence at L1."*',
    "2 (lines 1165-1166)": '  every change point (Ruling 47)"*.',
    "3 (lines 1316-1317)": '  carries a named reason."* S-45 itself *"stands as L1\'s"* (Ruling 53).',
    "4 (lines 296-299)": '    published as it stands, never repaired and never resolved by L1, on S-24\'s ground."*',
    "5 (lines 1578-1580)": '  arpeggio as one sonority.',
}

# 1. read as bytes, decode, EOL
orig_bytes = open(PATH, "rb").read()
text = orig_bytes.decode("utf-8")
print("original size (bytes):", len(orig_bytes))
EOL = "\r\n" if "\r\n" in text else "\n"
print("EOL:", repr(EOL))

# 2. needles
needles = [(name, EOL.join(pieces)) for name, pieces in CUTS]

# 3. each needle exactly once in the ORIGINAL text
counts = [(name, text.count(n)) for name, n in needles]
for name, c in counts:
    print("needle", name, "count in original:", c)
if any(c != 1 for _, c in counts):
    print("STOP: a needle does not occur exactly once; nothing written")
    sys.exit(2)

# non-overlap of the five spans in the original
spans = sorted((text.index(n), text.index(n) + len(n), name) for name, n in needles)
for (a0, a1, an), (b0, b1, bn) in zip(spans, spans[1:]):
    if a1 > b0:
        print("STOP: needles overlap:", an, bn)
        sys.exit(2)

# 4. remove each needle (text operation), then the line each needle sat on
result = text
for name, n in needles:
    result = result.replace(n, "", 1)

ok = True
for name, n in needles:
    start = text.index(n)
    removed_before = sum(len(m) for _, m in needles if text.index(m) < start)
    pos = start - removed_before
    ls = result.rfind(EOL, 0, pos)
    ls = 0 if ls < 0 else ls + len(EOL)
    le = result.find(EOL, pos)
    le = len(result) if le < 0 else le
    line = result[ls:le]
    exp = EXPECTED_LINES[name]
    match = line == exp
    ok = ok and match
    print("cut", name, "line after removal:", repr(line), "| equals expected:", match)
    print("   needle count in result:", result.count(n))
if not ok:
    print("STOP: a line does not equal its expected value; nothing written")
    sys.exit(2)

# 5. write
new_bytes = result.encode("utf-8")
with open(PATH, "wb") as f:
    f.write(new_bytes)

written = open(PATH, "rb").read()

# (i) byte-level removal computed independently from the raw bytes
bspans = []
for name, n in needles:
    nb = n.encode("utf-8")
    c = orig_bytes.count(nb)
    assert c == 1, (name, c)
    i = orig_bytes.index(nb)
    bspans.append((i, i + len(nb)))
bspans.sort()
expect_bytes = b""
cur = 0
for a, b in bspans:
    expect_bytes += orig_bytes[cur:a]
    cur = b
expect_bytes += orig_bytes[cur:]
print("(i) written bytes == original bytes with each needle's UTF-8 bytes removed once:", written == expect_bytes)

# (ii) size
needle_byte_total = sum(len(n.encode("utf-8")) for _, n in needles)
print("(ii) result size (bytes):", len(written),
      "| original minus sum of needle byte lengths:", len(orig_bytes) - needle_byte_total,
      "(sum of needle bytes:", needle_byte_total, ")",
      "| equal:", len(written) == len(orig_bytes) - needle_byte_total)

# (iii) git hash-object
h = subprocess.run(["git", "hash-object", PATH], capture_output=True, text=True).stdout.strip()
print("(iii) git hash-object:", h)

# (iv) first four lines byte-identical
o4 = orig_bytes.split(b"\n")[:4]
w4 = written.split(b"\n")[:4]
print("(iv) first four lines byte-identical to the original's:", o4 == w4)
```

Its output, verbatim (`scratchpad/cut_out.txt`, exit 0):

```
original size (bytes): 138946
EOL: '\n'
needle 1 (lines 1281-1283) count in original: 1
needle 2 (lines 1165-1166) count in original: 1
needle 3 (lines 1316-1317) count in original: 1
needle 4 (lines 296-299) count in original: 1
needle 5 (lines 1578-1580) count in original: 1
cut 1 (lines 1281-1283) line after removal: '  is gated on boundary evidence at L1."*' | equals expected: True
   needle count in result: 0
cut 2 (lines 1165-1166) line after removal: '  every change point (Ruling 47)"*.' | equals expected: True
   needle count in result: 0
cut 3 (lines 1316-1317) line after removal: '  carries a named reason."* S-45 itself *"stands as L1\'s"* (Ruling 53).' | equals expected: True
   needle count in result: 0
cut 4 (lines 296-299) line after removal: '    published as it stands, never repaired and never resolved by L1, on S-24\'s ground."*' | equals expected: True
   needle count in result: 0
cut 5 (lines 1578-1580) line after removal: '  arpeggio as one sonority.' | equals expected: True
   needle count in result: 0
(i) written bytes == original bytes with each needle's UTF-8 bytes removed once: True
(ii) result size (bytes): 138058 | original minus sum of needle byte lengths: 138058 (sum of needle bytes: 888 ) | equal: True
(iii) git hash-object: 4e5d5948e67116d15062fe6376d11840d0350b99
(iv) first four lines byte-identical to the original's: True
```

Every needle occurred exactly once; the five spans do not overlap; all five lines equal their expected
values; (i)–(iv) all hold.

## 3. THE SEARCH OVER THE CUT COPY, RE-RUN

**2(a).** The previous batch's search script, `records/cc/reports/cc_report_l2_brief_landing_2026_09_27.md`
§5, 4(b), written verbatim and unchanged to `scratchpad/t4b_search.py` and run over the cut copy (exit
0, `scratchpad/search_out.txt`). Every hit, verbatim (columns: line number in the cut copy, kind 1–4,
what matched, the line):

```
withheld identities searched: 113; withheld documents searched: 21
1	4	L2	> **THE INPUT CONTRACT — the ratified specification of L0 and L1, cut for the L2 deriving session.**
2	4	L2	> Below this block the ratified specification stands verbatim, except that passages stating the L2
34	4	L2	- **The analysis** — the harmonic-analysis software. Its layers are named L0, L1, L2, L3 in the charter
86	4	L2	  Every cue and flag is published with its witnesses so that L2 can weigh it (§3.7).
107	4	L2	  local key` is L2's harmonic span, the charter's own name, bounded by harmony change; the grouping
141	4	L2	way to the next is L2's and is out of scope; where a statement depends on that, the dependency is its
289	4	L2	  statement supplies is carried at L0 by S-3, reached by L2 through its consumption of L0.
302	4	L2	    L2's or L3's and RELOCATED there, the clauses being the L0/L1 half."*
347	4	L2	  a spelled context (S-9) and is carried forward for L2 as the charter's weak prior.
384	4	L2	  computation reads one of those. Not falsified by: L2 or L3 later admitting one of them through S-1.
400	4	L2	  notes, which is exactly the kind of thing L2 decides [RULED — charter, L2's question]. A layer that
400	4	L2	  notes, which is exactly the kind of thing L2 decides [RULED — charter, L2's question]. A layer that
426	4	L2	  key signature is replaced by a different one, all spelled pitches held fixed. Not falsified by: L2's
484	4	L2	  it does not exercise this) would yield one bar and one "bar" class; L2 would receive almost no metric
506	4	L2	  a voice assignment the record file does not carry. Not falsified by: L2 later deriving lines.
602	4	L2	  evidence L2 will want [CONJECTURE on L2's want].
602	4	L2	  evidence L2 will want [CONJECTURE on L2's want].
630	4	L2	  beginning on the upper note) — the harmony is still read on the principal at L1, and L2 receives
711	4	L2	  the interim treatment renders as a dyad; L2 sees an interval that never sounds together.
772	4	L2	  flag, so L2 can weigh it.
788	4	L2	  information for L2's weighing of the next change point and for L3's phrase reading, so it is
803	4	L2	and each ending, which slice would follow which on which pass), so that L2 can read across a repeat
833	4	L2	  impossible. The cost — very short slices in florid textures — is L2's to weigh, not L1's to
855	4	L2	  point; at L2 the harmonic boundary is decided jointly with the tonality and the chord over L1's
909	4	L2	  evidence and would decide that the harmony before the silence continues through it, which is L2's
913	4	L2	- *Premise.* Premise: L2 can consume an empty sounding set. False-negative path: a consumer that
914	4	L2	  divides by the set's size; a specification concern for L2, recorded.
931	4	L2	  entered and cut events keeps the span's edges honest (#12) and lets L2 know that the first slice's
963	4	L2	- *Premise.* The charter's; its false-negative path (a change point that L2 will always find
964	4	L2	  harmonically inert) is by design harmless — L2 may keep the harmony across it.
966	4	L2	  octave doubling's onset is not a change point. Not falsified by: L2 merging across it.
1023	4	L2	  ground truth would decide it — UNESTABLISHED; L1 publishes the class regardless, and L2's weighting
1037	4	L2	  L2's calibration"*.
1083	4	L2	- *Premise.* Premise: L2 can recover a hemiola from the notated class plus the notes. False-negative
1172	4	L2	- *Premise.* Premise: L2 and L3 weigh the flags. Its false-negative path is none at L1.
1219	4	L2	- *Status.* Settled for L1 (OQ-1 answered for L1 at Ruling 70; Ruling 73), the remainder of OQ-1 L2's
1266	4	L2	  passing bass. The cue carries its witnesses and the slice's length, and the weighing is L2's. This
1301	4	L2	  neighbour and the cue fails; the pack's C41 shape (evidence arrives after the moment). L2 can look
1330	4	L2	  and the cue becomes weaker. The published relaxation flag lets L2 weigh it.
1373	4	L2	  evidence, and its false-positive rate is L2's to learn.
1393	4	L2	- *Status.* Open on the measurement (OQ-10, L2's calibration); the stand-ins provisional under S-52
1407	4	L2	  under load, the measurement S-48 names owed to L2's calibration."* OQ-17 is marked ANSWERED at §4.
1424	4	L2	  (D-100). False-negative path: none; if it were dropped, L2 would compute it from the sounding set.
1498	4	L2	  and no chord able to move a change point"*; at L2 jointly with the tonality and the chord over L1's
1522	4	L2	**S-53. Nothing L1 publishes depends on anything L2 decides. Where a statement above would have
1523	4	L2	wanted L2's answer — which slice is the harmonic arrival (S-44), whether a lowest pitch is the
1526	4	L2	to L2. L1 is therefore computable in one forward pass over the working span, and the working span is
1528	4	L2	- *Defense.* The boundary contract: L1 → L2 forward only; *"L2 receives candidates and evidence, never
1528	4	L2	- *Defense.* The boundary contract: L1 → L2 forward only; *"L2 receives candidates and evidence, never
1535	4	L2	- *Falsifier.* CODE. Observable: L1's inputs. Decision rule: falsified if L1 reads any L2 output or any
1536	4	L2	  value not in L0 plus the span. Not falsified by: a caller passing a span computed by an earlier L2
1570	4	L2	  makes exhaustive; publishing the span keeps the information for L2, which may treat a pedalled
1578	4	L2	  L2 see it.
1606	4	L2	  carried to L2's surface.
1663	1	D-501	  input; the ground D-501 and the L0 → L1 boundary contract (*"Nothing derived"*), neither naming a
1670	4	L2	  the measurement S-48 names owed to L2's calibration."* The ruling's own addendum records that the

count per kind:
  1 (withheld identity): 1
  2 (withheld document): 0
  3 (ARCHITECTURE.md or docs/src path): 0
  4 (the token L2): 55
  total: 56
```

**The counts equal the expected ones exactly**: kind 1 = 1 (`D-501` alone), kind 2 = 0, kind 3 = 0,
kind 4 = 55, total 56. **Nothing was removed, edited or judged.**

**2(b)** — `scratchpad/t2b_counts.py` over the cut copy, exit 0:

```
'cadence factor': 0
'cadence-factor': 0
'root-pinning': 0
'D-207': 0
'not in the first': 0
```

All five are 0, as expected. `git hash-object cowork_derived_specification_l0_l1_2026_09_03.md` =
`bbde68b96d64bd55346f1a14322bf0e2bc0e11a3`, **unchanged from 1(a)**.

## 4. Task 3 — the close

**3(a) — the `STATUS.md` entry**, written at the head of the dated entries, quoted whole:

> *Last updated: 2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_input_contract_cuts_2026_09_27.md`. **★★ THE CUT-LIST SITTING'S RECORD IS COMMITTED**, `records/cowork/rulings/cowork_rulings_2026_09_27_l2_cut_list_sitting.md`, with this dispatch and the Cowork side's handoff entry. ★ **RULING 1 OF THAT SITTING IS CARRIED: FIVE NAMED PASSAGES WERE REMOVED VERBATIM FROM THE L2 INPUT CONTRACT**, `tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md`, with no mark — each needle found exactly once before the cut, the line each sat on confirmed afterwards, and the written file established at the raw bytes to be the original with those five passages removed and nothing else. ★ **THE PREVIOUS BATCH'S SEARCH WAS RE-RUN, UNCHANGED, OVER THE CUT COPY**, and its hits are reported whole. ★★ **WHAT THIS BATCH DID NOT DO: no session was booted; THE BRIEF WAS NOT RELEASED AND NOT EDITED; THE SOURCE SPECIFICATION WAS NOT WRITTEN**, and no hit of the search was judged or acted on; no score or analysis file was copied, moved or edited. No open-items row created, flipped or discarded; no decisions-register identity allocated and no `D-NNN` created; no tool source edited but the forward bound's authored aiming; no `src/` file, build, test, golden, score corpus or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_l2_input_contract_cuts_2026_09_27.md` — and no figure is restated here (**D-431**).)*

**★ ONE CHANGE TO AN EXISTING LINE, DECLARED.** In the same edit the brief-landing batch's entry beneath
lost its leading `Last updated: ` prefix. This is `gen_status_batch_bound.py`'s own declared prefix
adjustment, which the dispatch says is expected to fire: `moved_entries()` strips that prefix from the
base-commit text and requires the stripped form in the live file exactly once. That entry then moved to
the archive whole at 3(b), so **no rewritten sentence remains in `STATUS.md`**. This was the last write
to `STATUS.md` in this batch.

**3(b) — the forward bound.** Established first: `git ls-tree` of `STATUS.md` at
`01b59a2df577bca7e7db38a75c35fe312ce82a74` and at `9f42ec57cb75b36267aebfc37fc0be3749d9346f` both give
blob `4d428c9d9ab881e05be6cfe357f8f2a8e57be904`.

The aiming set: `BASE_COMMIT` = `9f42ec57cb75b36267aebfc37fc0be3749d9346f`; `PREVIOUS_BATCH_DISPATCH`
= `cc_instruction_l2_brief_landing_2026_09_27.md`; `DISPATCH` =
`cc_instruction_l2_input_contract_cuts_2026_09_27.md`; `TASK` = `Task 3`; `ACT_DATE` = `2026-09-27`
(the date the move ran); `MOVE_KIND` = `ordinary`; `RULINGS` unchanged; one row appended to
`PREVIOUS_AIMINGS` and no row edited. Each former value is named in its comment.

`python tools/audit/gen_status_batch_bound.py --apply`, exit 0:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 1,865 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

`python tools/audit/gen_status_batch_bound.py --check`, exit 0:

```
  entries moved: 1, 1,865 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**The entry `--apply` actually moved, by name** (not read off the green `--check`, OI-379): the
brief-landing batch's entry, opening *"2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md`. **★★ THE COWORK SIDE'S RECORDS AND THE DRAFT L2 BRIEF ARE COMMITTED**…"*,
at line 8 of the base commit's `STATUS.md`, membership "names the dispatch", the declared adjustment
applied. **The prefix adjustment fired. The two 2026-09-02 entries did NOT move** and were not moved by
hand; they stand in `STATUS.md` directly below this batch's entry.

The tool's diff by blob hashes, `git diff c0a8fd4d1adf41cb338ca964520213cce2cdcd2c
5ce593bdf5a399cafc0240ca832f148c02099bbb` (`tools/audit/gen_status_batch_bound.py`), verbatim:

```diff
@@ -552,7 +552,31 @@ OUT = os.path.join(HERE, "status_batch_bound.json")
 # tool can identify them** — a declared state and not a STOP, unchanged by this act. **NO COUNT OF
 # THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431): the membership is DERIVED from the entries'
 # own text at the base commit.
-BASE_COMMIT = "9378e95a7d620fca6ebd28119d4d1bb6483f9d66"
+# ★ RE-AIMED 2026-09-27 by `cc_instruction_l2_input_contract_cuts_2026_09_27.md` Task 3, at its 3(b),
+# and ALL FIVE authored inputs moved together, `PREVIOUS_AIMINGS` being appended to rather than
+# replaced (#12). The aiming it replaces is the L2 brief landing's, which is ALREADY the last row of
+# `PREVIOUS_AIMINGS` — that batch recorded its own aiming in its own act — so it is not appended a
+# second time, and this batch's aiming is appended instead. `BASE_COMMIT` was
+# `9378e95a7d620fca6ebd28119d4d1bb6483f9d66` and is now
+# `9f42ec57cb75b36267aebfc37fc0be3749d9346f`: this batch's Task 0 commit, the interim carriers. Task 0
+# commits no `STATUS.md`, so that commit's `STATUS.md` object is the one both refs carried when this
+# batch opened (`01b59a2df577bca7e7db38a75c35fe312ce82a74`, read at the two ref FILES with the file
+# tools, D-253) — the same blob at both commits, established at `git ls-tree` of each — and it carries
+# the brief-landing batch's entry at the head of the dated entries.
+#
+# ★★ THE THEN-PREVIOUS BATCH IS THE L2 BRIEF LANDING. `PREVIOUS_BATCH_DISPATCH` was
+# `cc_instruction_l2_pack_build_second_half_2026_09_27.md` and now names
+# `cc_instruction_l2_brief_landing_2026_09_27.md`, whose entry names it; that batch wrote its entry and
+# its move inside its own Task 5, and no close ran between it and this batch.
+#
+# **THE DECLARED PREFIX ADJUSTMENT IS EXPECTED TO FIRE**, that entry carrying the `Last updated: `
+# prefix at the base commit, which is why this batch's own entry was written into `STATUS.md` BEFORE
+# `--apply` ran. `ACT_DATE` and the executing dispatch's date AGREE here, both being 2026-09-27.
+# **The second writing's two nameless 2026-09-02 entries remain in `STATUS.md` and no aiming of this
+# tool can identify them** — a declared state and not a STOP, unchanged by this act. **NO COUNT OF
+# THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431): the membership is DERIVED from the entries'
+# own text at the base commit.
+BASE_COMMIT = "9f42ec57cb75b36267aebfc37fc0be3749d9346f"
 
 # The batch whose entries this aiming moves, named by its dispatch because that is what each of its
 # entries says of itself. On an ORDINARY move it is the THEN-PREVIOUS batch and Ruling 4's forward
@@ -562,7 +586,7 @@ BASE_COMMIT = "9378e95a7d620fca6ebd28119d4d1bb6483f9d66"
 # 4's forward bound moves exactly these, in the act that writes this batch's own" until 2026-09-07,
 # correct while every aiming this tool had ever carried was an ordinary one; it is widened rather
 # than replaced, because the ordinary reading is still the one that governs an ordinary move — #12.)*
-PREVIOUS_BATCH_DISPATCH = "cc_instruction_l2_pack_build_second_half_2026_09_27.md"
+PREVIOUS_BATCH_DISPATCH = "cc_instruction_l2_brief_landing_2026_09_27.md"
 
 # ★ THE ACT DATE IS THE DAY THE MOVE RAN, NOT THE DAY THE DISPATCH WAS WRITTEN. This executing
 # dispatch is dated 2026-09-07 and this batch ran on 2026-09-07, so the two agree; the field is kept
@@ -577,9 +601,12 @@ PREVIOUS_BATCH_DISPATCH = "cc_instruction_l2_pack_build_second_half_2026_09_27.m
 # 2026-09-27, whose move ran on 2026-09-27, so the two dates agree.)* *(`ACT_DATE` read "2026-09-27"
 # and `DISPATCH` `cc_instruction_l2_pack_build_second_half_2026_09_27.md` while that batch was the
 # executing act; both are re-stated here for `cc_instruction_l2_brief_landing_2026_09_27.md`, dated
+# 2026-09-27, whose move ran on 2026-09-27, so the two dates agree.)* *(`ACT_DATE` read "2026-09-27"
+# and `DISPATCH` `cc_instruction_l2_brief_landing_2026_09_27.md` while that batch was the executing
+# act; both are re-stated here for `cc_instruction_l2_input_contract_cuts_2026_09_27.md`, dated
 # 2026-09-27, whose move ran on 2026-09-27, so the two dates agree.)*
 ACT_DATE = "2026-09-27"
-DISPATCH = "cc_instruction_l2_brief_landing_2026_09_27.md"
+DISPATCH = "cc_instruction_l2_input_contract_cuts_2026_09_27.md"
 # TASK IS A CHOICE, DECLARED RATHER THAN IMPLIED. On an ORDINARY move the executing dispatch orders
 # the move and this batch's own `STATUS.md` entries in the same numbered task, so both halves of "the
 # same act that writes its own entries" sit inside it, and that task is what the archive header names.
@@ -627,8 +654,11 @@ DISPATCH = "cc_instruction_l2_brief_landing_2026_09_27.md"
 # its 12(b) — inside its own Task 10, which that dispatch's §12 heading names in those words. It names
 # Task 5 while `cc_instruction_l2_brief_landing_2026_09_27.md` is the executing act, that dispatch
 # ordering both halves of the close — this batch's own entry at its 5(a) and this move at its 5(b) —
-# inside its own Task 5, which that dispatch's §7 heading names in those words.)*
-TASK = "Task 5"
+# inside its own Task 5, which that dispatch's §7 heading names in those words. It names Task 3 while
+# `cc_instruction_l2_input_contract_cuts_2026_09_27.md` is the executing act, that dispatch ordering
+# both halves of the close — this batch's own entry at its 3(a) and this move at its 3(b) — inside its
+# own Task 3, which that dispatch's §5 heading names in those words.)*
+TASK = "Task 3"
 # ★ WHAT KIND OF MOVE THIS AIMING PERFORMS. Two values and no others.
 #   "ordinary"  — the move Ruling 4's forward clause describes: the then-previous batch's entries,
 #                 moved in the same act that writes this batch's own entries.
@@ -1021,6 +1051,10 @@ PREVIOUS_AIMINGS = [
      "base_commit": "9378e95a7d620fca6ebd28119d4d1bb6483f9d66",
      "the_then_previous_batch": "cc_instruction_l2_pack_build_second_half_2026_09_27.md",
      "the_kind_of_move": "ordinary"},
+    {"executing_act": "cc_instruction_l2_input_contract_cuts_2026_09_27.md, Task 3",
+     "base_commit": "9f42ec57cb75b36267aebfc37fc0be3749d9346f",
+     "the_then_previous_batch": "cc_instruction_l2_brief_landing_2026_09_27.md",
+     "the_kind_of_move": "ordinary"},
 ]
 
 HEADER_ORDINARY = (
```

No function changed. The artifact's diff, `git diff 92b55f157bb88fdef2dd5e35809311b0ccddc468
9219e412c4e6a3463f740450204270b101a376bf` (`tools/audit/status_batch_bound.json`), verbatim:

```diff
@@ -1,7 +1,7 @@
 {
  "what_this_is": "RULING 4's FORWARD BOUND, applied at one batch close: which of the then-previous batch's STATUS.md entries moved to the archive, and the mechanical proof that nothing was lost or altered in transit (#12). Every figure here is computed; none is transcribed (D-431).",
  "generated_by": "tools/audit/gen_status_batch_bound.py",
- "dispatch": "cc_instruction_l2_brief_landing_2026_09_27.md, Task 5",
+ "dispatch": "cc_instruction_l2_input_contract_cuts_2026_09_27.md, Task 3",
  "★_every_previous_aiming_of_this_tool_kept_rather_than_replaced": [
   {
    "executing_act": "cc_instruction_preparation_sixth.md, Task 1",
@@ -387,22 +387,28 @@
    "base_commit": "9378e95a7d620fca6ebd28119d4d1bb6483f9d66",
    "the_then_previous_batch": "cc_instruction_l2_pack_build_second_half_2026_09_27.md",
    "the_kind_of_move": "ordinary"
+  },
+  {
+   "executing_act": "cc_instruction_l2_input_contract_cuts_2026_09_27.md, Task 3",
+   "base_commit": "9f42ec57cb75b36267aebfc37fc0be3749d9346f",
+   "the_then_previous_batch": "cc_instruction_l2_brief_landing_2026_09_27.md",
+   "the_kind_of_move": "ordinary"
   }
  ],
  "the_ruling": "Ruling 4 of cowork_rulings_2026_08_17_governing_surface_split.md: an entry is SUPERSEDED the moment a later batch's close exists; the site keeps only the latest batch's entries, and every future batch close moves the then-previous batch's entries in the same act that writes its own.",
- "base_commit": "9378e95a7d620fca6ebd28119d4d1bb6483f9d66",
- "the_then_previous_batch": "cc_instruction_l2_pack_build_second_half_2026_09_27.md",
+ "base_commit": "9f42ec57cb75b36267aebfc37fc0be3749d9346f",
+ "the_then_previous_batch": "cc_instruction_l2_brief_landing_2026_09_27.md",
  "the_kind_of_move": "ordinary",
  "entries_moved": 1,
- "characters_moved": 2707,
+ "characters_moved": 1865,
  "the_moved": [
   {
    "line_at_base": 8,
-   "characters": 2707,
-   "sha256": "5178765c14e8db18ed990c6c6084650aaea093bb50c5dc23b8131df26f7a8f43",
+   "characters": 1865,
+   "sha256": "2690bda85b27a3d1093f19016ff62e386b64966295b57dca4ea2eb2c2fafef7f",
    "membership": "names the dispatch",
    "the_one_declared_adjustment_applied": true,
-   "opening": "*2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_pack_build_second_half_2026_09_27.md`. **★★ THE L2 SUBJECT IS ADDED TO THE DERIVATION BOO"
+   "opening": "*2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md`. **★★ THE COWORK SIDE'S RECORDS AND THE DRAFT L2 BRIEF ARE C"
   }
  ],
  "reconciliation": {
```

`STATUS_ARCHIVE.md`, `git diff 131cd8d01514744febaeb674e27b653a29dd8840
7bce365ddfaca38bbda65cfed0a3849f3a003a9e`: additions only, at the end of the file — the tool's
ordinary header naming `cc_instruction_l2_brief_landing_2026_09_27.md` as the previous batch and
`cc_instruction_l2_input_contract_cuts_2026_09_27.md` Task 3 as the act, then the moved entry verbatim.
`STATUS.md`, `git diff 4d428c9d9ab881e05be6cfe357f8f2a8e57be904 97a10903b3a351b40476e2ef7b3c71dfa5b252b7`:
`1 1` — the new entry in, the brief-landing entry out.

**3(c) — the regenerations**, in the dispatch's order (`scratchpad/regen.txt`), outputs and exit codes
verbatim:

```
=== python tools/audit/gen_evidence_pin_membership.py
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 100
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
--- exit: 0
=== python tools/audit/gen_evidence_pin_membership.py --check
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 100
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
--- exit: 0
=== python tools/audit/gen_l0_l1_outgoing_population.py
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
--- exit: 0
=== python tools/audit/gen_l0_l1_outgoing_population.py --check
l0_l1_outgoing_population.json re-derives
--- exit: 0
=== python tools/audit/gen_session_start_read_size.py
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
    STATUS.md                                                                 10793
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 245955
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 245955 [ruled membership]  (-121166, -33.00%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 245955 [ruled membership]  (-50877, -17.14%)  <- CROSSES A REGIME BOUNDARY
--- exit: 0
=== python tools/audit/gen_defense_share.py
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
    of the whole session-start read (245955): 5.27%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
--- exit: 0
=== python tools/audit/gen_session_start_read_size.py --check
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
    STATUS.md                                                                 10793
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 245955
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 245955 [ruled membership]  (-121166, -33.00%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 245955 [ruled membership]  (-50877, -17.14%)  <- CROSSES A REGIME BOUNDARY
--- exit: 0
=== python tools/audit/gen_defense_share.py --check
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
    of the whole session-start read (245955): 5.27%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
--- exit: 0
```

All eight exit 0; no `STOP:` line and no traceback. All four tools wrote their artifacts, and all four
artifacts differ from the Task 0 commit (the enumeration below reports each as modified).

**The members changed**, each artifact compared with its blob at `9f42ec57cb…` by a structural walk of
the parsed JSON (`scratchpad/json_member_diff.py`, exit 0), verbatim:

```
======== tools/audit/evidence_pin_membership.json
  byte-identical to the Task 0 commit blob: False
  differences: 3
  CHANGED	/counts/ruling_records_read
     was: 99
     now: 100
  ADDED	/ruling_records_read[]
     was: null
     now: "records/cowork/rulings/cowork_rulings_2026_09_27_l2_cut_list_sitting.md"
  LENGTH	/ruling_records_read
     was: 99
     now: 100
======== tools/audit/l0_l1_outgoing_population.json
  byte-identical to the Task 0 commit blob: False
  differences: 1
  CHANGED	/the_term_search/per_file/STATUS.md/recorded_hits[0]/line
     was: *Last updated: 2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md`. **★★ THE COWORK SIDE'S RECORDS AND THE DRAFT L2 BRIEF ARE COMMITTED**, the brief as it stands and not edited. ★ **RULING 1 OF `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sittin …[truncated]
     now: *Last updated: 2026-09-27 (CC — `records/cc/instructions/cc_instruction_l2_input_contract_cuts_2026_09_27.md`. **★★ THE CUT-LIST SITTING'S RECORD IS COMMITTED**, `records/cowork/rulings/cowork_rulings_2026_09_27_l2_cut_list_sitting.md`, with this dispatch and the Cowork side's handoff entry. ★ **RUL …[truncated]
```

So: in the pinned-evidence membership, **no member added, removed or changed** — one ruling record read
added, the cut-list sitting's; in the outgoing population, **no entry added, removed or changed** — one
recorded hit's quoted line in `STATUS.md` changed, the head line now being this batch's entry. Nothing
resolved. (`session_start_read_size.json` and `defense_share.json` changed at 8 and 2 lines each,
`git diff --numstat`; not required to be itemised by the dispatch.)

**3(d) — the closing guard capture**, `python tools/audit/gen_guard_state.py`, exit 0,
`scratchpad/guard_close.txt`: `79 guard(s) run, 12 failing, 4 not run, 19 historical record(s)`. The
guard classification, exit 2, the same STOP as at the opening, carried (B7):

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

**The verdict-by-verdict comparison** (`scratchpad/verdict_compare.py` over the two captures, exit 0),
verbatim:

```
guards at opening: 102 at closing: 102
only at opening: []
only at closing: []
MOVED  FAIL -> PASS  tools/audit/gen_evidence_pin_membership.py --check
same   PASS       tools/audit/register_lint.py
same   PASS       tools/audit/index_status_lint.py --check
same   PASS       tools/audit/gen_arm_comment_sweep.py --check
same   PASS       tools/audit/local_patches_check.py
same   PASS       tools/audit/local_patches_check.py --establish --check
same   PASS       tools/audit/guard_armed_check.py
same   PASS       tools/audit/process_check.py --establish --check
same   PASS       tools/audit/shell_read_guard.py --establish --check
same   PASS       tools/audit/output_encoding.py --establish --check
same   PASS       tools/audit/changed_paths.py --establish
same   PASS       tools/audit/claude_md_rule_triage.py --check
same   PASS       tools/audit/corpus_arm_stamp.py --check
same   PASS       tools/audit/corpus_arm_stamp.py --establish --check
same   PASS       tools/audit/instrument_arm_declaration_effect.py --check
same   FAIL       tools/audit/gen_phase3_gate_partition.py --check
same   PASS       tools/audit/gen_nongating_apparatus_rows.py --check
same   PASS       tools/audit/gen_discard_records.py --check
same   PASS       tools/audit/decisions/gen_true_half_reach.py --check
same   PASS       tools/audit/decisions/gen_true_half_reach_rows.py --check
same   PASS       tools/audit/gen_gating_row_sizing.py --check
same   FAIL       tools/audit/gen_filing_convention_application.py --check
same   PASS       tools/audit/decisions/gen_phase1q_snapshot_establishment.py --check
same   PASS       tools/audit/gen_period_stratum_split.py --check
same   PASS       tools/audit/gen_july_screen.py --check
same   PASS       tools/audit/gen_specification_document_set.py --check
same   PASS       tools/audit/gen_l0_l1_outgoing_population.py --check
same   PASS       tools/audit/gen_withheld_family_reading.py --subject l2 --check
same   FAIL       tools/audit/gen_artifact_inventory.py --check
same   FAIL       tools/audit/gen_artifact_inventory_surface.py --check
same   PASS       tools/audit/gen_status_archive_pass.py --check
same   PASS       tools/audit/gen_doc_change_candidates.py --check
same   FAIL       tools/audit/gen_test_construction_evidence.py --check
same   PASS       tools/audit/gen_decisions_filter.py --check
same   FAIL       tools/audit/gen_retirement_caller_check.py --check
same   PASS       tools/audit/gen_deciding_act_recovery.py --check
same   PASS       tools/audit/gen_rulings_sort.py --check
same   PASS       tools/audit/gen_sole_carrier_subclass.py --check
same   PASS       tools/audit/gen_ratified_document_check.py --check
same   FAIL       tools/audit/decisions/apply_soft_discard.py --check
same   FAIL       tools/audit/decisions/apply_residue_discard.py --check
same   PASS       tools/audit/gen_framework_untrusted_candidates.py --check
same   PASS       tools/audit/gen_phase1_gate_readers.py --check
same   PASS       tools/audit/gen_discard_reach_split.py --check
same   PASS       tools/audit/decisions/gen_retired_subject_moves.py --check
same   PASS       tools/audit/gen_census_movement_classification.py --check
same   PASS       tools/audit/gen_governing_surface_spans.py --check
same   PASS       tools/audit/gen_governing_surface_readers.py --check
same   PASS       tools/audit/gen_governing_surface_split.py --check --pair CLAUDE.md
same   PASS       tools/audit/gen_governing_surface_split.py --check --pair OPEN_ITEMS.md
same   PASS       tools/audit/gen_governing_surface_split.py --check --pair DECISIONS.md
same   PASS       tools/audit/gen_governing_surface_split.py --check --pair STATUS.md
same   PASS       tools/audit/gen_governing_surface_split.py --check --pair BUILD_AND_TEST.md
same   PASS       tools/audit/gen_status_batch_bound.py --check
same   PASS       tools/audit/gen_status_residue_move.py --check
same   PASS       tools/audit/gen_retirement_census_movement.py --check
same   PASS       tools/audit/gen_claude_md_finer_spans.py --check
same   PASS       tools/audit/gen_claude_md_finer_surface.py --check
same   PASS       tools/audit/gen_session_start_read_size.py --check
same   PASS       tools/audit/gen_defense_share.py --check
same   FAIL       tools/audit/gen_epoch_write_path.py --check
same   PASS       tools/audit/gen_derivation_boot_pack.py --check
same   FAIL       tools/audit/gen_recognizer_establishment_sort.py --check
same   PASS       tools/audit/gen_l2_withheld_documents.py --check
same   PASS       tools/audit/decisions/gen_decisions_register.py --check
same   PASS       tools/audit/decisions/gen_cluster_dispositions.py --verify
same   PASS       tools/audit/decisions/gen_cluster_dispositions.py --check
same   PASS       tools/audit/decisions/gen_cluster_dispositions.py --producible
same   FAIL       tools/audit/decisions/gen_home_classification.py --check
same   FAIL       tools/audit/decisions/gen_phase1p_delegation_bar.py --check
same   PASS       tools/audit/decisions/gen_reads5_repack.py --check
same   PASS       tools/audit/decisions/gen_decision_clusters.py --check
same   PASS       tools/audit/decisions/gen_phase1w_legacy_verification.py --check
same   PASS       tools/audit/decisions/reaim_home_anchors.py --check
same   PASS       tools/audit/decisions/gen_live_prohibition_pointers.py --check
same   PASS       tools/audit/gen_claude_md_growth.py --check
same   PASS       tools/audit/prune_at_amendment_lint.py --check
same   PASS       tools/open_items_split_check.py
same   PASS       tools/notation_seams/gen_callpath_facts.py --check
same   NOT RUN    tools/audit/gen_ratification_surface_set.py
same   NOT RUN    tools/audit/reaim_ratification_surface_paths.py
same   NOT RUN    tools/audit/decisions/gen_verbatim_subject_consistency.py
same   NOT RUN    tools/audit/gen_reserved_word_scanner.py
same   HISTORICAL tools/audit/gen_phase1_completion_inventory.py
same   HISTORICAL tools/audit/gen_phase1_finish_line.py
same   HISTORICAL tools/audit/decisions/gen_outstanding_delegations.py
same   HISTORICAL tools/audit/gen_claude_md_finer_archive.py
same   HISTORICAL tools/audit/gen_post_split_archive.py
same   HISTORICAL tools/audit/decisions/gen_phase1n_reading_regime.py
same   HISTORICAL tools/audit/decisions/gen_reads5_yield.py
same   HISTORICAL tools/audit/decisions/gen_reads6_yield.py
same   HISTORICAL tools/audit/decisions/gen_phase1m_measurements.py
same   HISTORICAL tools/audit/decisions/gen_phase1g_triage.py
same   HISTORICAL tools/audit/decisions/gen_reads1_yield.py
same   HISTORICAL tools/audit/decisions/gen_reads2_yield.py
same   HISTORICAL tools/audit/decisions/gen_reads3_yield.py
same   HISTORICAL tools/audit/decisions/gen_reads4_yield.py
same   HISTORICAL tools/audit/decisions/gen_finish_line_item1_routes.py
same   HISTORICAL tools/audit/decisions/gen_item1_rehome_blocker.py
same   HISTORICAL tools/audit/decisions/gen_r1_superseded_reach.py
same   HISTORICAL tools/audit/decisions/gen_reads4_oi326_application.py
same   HISTORICAL tools/audit/gen_claude_md_prune_backlog.py
verdicts moved: 1
PASS -> anything else: none
```

**THE CONDITION HOLDS: no guard that was PASS at the opening carries any other verdict at the closing.**
One FAIL → PASS: `gen_evidence_pin_membership.py --check`, cleared by the 3(c) regeneration.

## 5. Task 4 — the commit and the push

The enumeration before the batch commit (`python tools/audit/changed_paths.py`, exit 0,
`scratchpad/changed_close.txt`, 404 records), every record other than the untracked paths under
`scratch_artifacts/`:

```
 M	STATUS.md
 M	STATUS_ARCHIVE.md
 M	tools/audit/claude_md_finer_archive.json
 M	tools/audit/defense_share.json
 M	tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md
 M	tools/audit/evidence_pin_membership.json
 M	tools/audit/gen_status_batch_bound.py
 M	tools/audit/guard_state.json
 M	tools/audit/l0_l1_outgoing_population.json
 M	tools/audit/session_start_read_size.json
 M	tools/audit/status_batch_bound.json
??	Claude outputs/
??	Codex research inventory/
??	docs/research_papers/polyph9-release/
??	external resarch summary/Computational Music Theory and Its.pdf
??	external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf
??	tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx
404 changed path record(s) [worktree]
```

**Every modified path is inside the footprint assumption.** The guard set's own artifact reported
modified is `tools/audit/guard_state.json` (written by `gen_guard_state.py` at the captures).
`tools/audit/claude_md_finer_archive.json` is held back (B7); the untracked paths are held back and are
the same ones present at the opening.

**The batch commit** carries exactly these, each by its own path:
`tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md`; `STATUS.md`;
`STATUS_ARCHIVE.md`; `tools/audit/gen_status_batch_bound.py`; `tools/audit/status_batch_bound.json`;
`tools/audit/evidence_pin_membership.json`; `tools/audit/l0_l1_outgoing_population.json`;
`tools/audit/session_start_read_size.json`; `tools/audit/defense_share.json`; this report; and
`tools/audit/guard_state.json` — **11 paths.**

**The commits.** Task 0: `9f42ec57cb75b36267aebfc37fc0be3749d9346f`. The batch commit is the commit that
carries this report, so its identity cannot be written inside it; it, the proof of its staged set and
the push result are reported in the session's closing message, and are readable at
`.git/refs/heads/master` and `.git/refs/remotes/origin/master`. This report is not edited after that
commit.

## 6. What I did NOT do

- No tool source edited but `tools/audit/gen_status_batch_bound.py`, at its authored aiming inputs,
  their comments and one appended `PREVIOUS_AIMINGS` row; no function. Not
  `gen_guard_classification.py`, not `gen_withheld_family_reading.py` (the live consumer at its lines
  146–147 not repaired), not `gen_evidence_pin_membership.py`.
- `cowork_derived_specification_l0_l1_2026_09_03.md` not read except by `git hash-object`, and not
  written (its hash equal at 1(a) and 2(b)).
- The brief `cowork_blind_session_brief_l2.md` not edited and not released; nothing under
  `tools/audit/derivation_boot_pack/` or `reading_pass/` touched.
- No governing document amended but `STATUS.md`: not `CLAUDE.md`, `ARCHITECTURE.md`, `OPEN_ITEMS.md`,
  `DECISIONS.md` or any ruling record.
- No score or analysis file copied, moved or edited; the untracked
  `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` left as found.
- No session booted.
- No hit of the search removed, edited or judged.
- No open-items row created, flipped or discarded; no decisions-register identity allocated and no
  `D-NNN` touched.
- No `src/` file, build, test, golden, score corpus, nothing under `tools/corpus/`, `tools/robust_stop/`
  or `tools/dcml/`, no measurement of the analysis, no paper.
- `gen_guard_classification.py`'s STOP carried, not chased.
- `tools/audit/claude_md_finer_archive.json` not staged, not reverted, not investigated.

## 7. What goes to the user

- **1(b)'s five confirmed lines** — §2: every needle once in the original, every line after its cut equal
  to the expected line, and the written file byte-exact.
- **The search re-run over the cut copy** — §3: `D-501` the one remaining identity hit, 55 hits on the
  token `L2`, nothing else; the five strings of 2(b) all absent.
- **The 3(c) changes**: in the pinned-evidence membership, no member changed (one ruling record read
  added, the cut-list sitting's); in the outgoing population, no entry changed, one recorded hit's quoted
  `STATUS.md` line changed to this batch's entry.
- **No STOP fired.**
