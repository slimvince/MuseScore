# CC report — the draft L3 keyword list counted read-only: one measurement artifact, the ruling record and its entries in git — NO population derived, NO ruling, NO algorithm change, NO decisions-register entry

> **Executed** `records/cc/instructions/cc_instruction_l3_keyword_count_2026_10_17.md`, pinned at Task 0 to blob
> `208961216e5b912f0bb37464c459f38e2c1017e8`, by Claude Code on 2026-10-17 to 2026-10-18, at boot tip
> `79499c21ec70bcf5e0a817050ade5bc1268d6a51` (both ref files, read with the file tools). **This report decides nothing and
> recommends nothing.** No task stopped. Every number below is the verbatim output of a run this batch made, or a size
> and hash the dispatch states as a start-state bar; no value from the artifact is restated in prose (**D-431**).

## THE COUNT, AS TAKEN

**The measuring script**, written to this session's scratch folder outside the repository as `l3_keyword_count.py`,
whole. Before it ran it was proved identical, byte for byte after line-ending normalization, to the dispatch's §1(c)
block read from the pinned blob (the check is `script_vs_dispatch.py`, §7; its output: `dispatch block lines: 148 | script lines: 148 / identical: True`).

```python
# READ-ONLY MEASUREMENT of the DRAFT L3 keyword list. Imports the L0/L1 population tool's own
# matcher and loaders (one path per concern, #6) and never calls its derive() or main().
import json, os, re, sys

ROOT = r"C:\s\MS"
HERE = os.path.join(ROOT, "tools", "audit")
sys.path.insert(0, HERE)
import gen_l0_l1_outgoing_population as pop   # main() is guarded by __main__

CORE = (
    "cadence", "cadential", "plagal", "phrase end",
    "phrase boundary", "phrase grouping", "grouping layer",
    "chord symbol", "chord-symbol", "chordsymbol", "bass note", "slash chord", "root pitch class", "inversion",
    "figured bass", "figured-bass", "thoroughbass", "continuo",
    "harmonic rhythm", "harmonic-rhythm", "harmonicrhythm",
    "read-off",
)
COUNTED_IN_CONTEXT = ("phrase", "grouping", "period", "sentence", "bass", "contradiction", "deceptive")
OUT = os.path.join(HERE, "l3_keyword_count_measurement.json")


class Stop(Exception):
    pass


def whole_word(term, line):
    return re.search(r"(?<![A-Za-z0-9])" + re.escape(term.lower()) + r"(?![A-Za-z0-9])",
                     line.lower()) is not None


def main():
    if len(CORE) != 22 or len(COUNTED_IN_CONTEXT) != 7:
        raise Stop("draft lengths are %d and %d, not 22 and 7" % (len(CORE), len(COUNTED_IN_CONTEXT)))
    if len(set(CORE) | set(COUNTED_IN_CONTEXT)) != 29:
        raise Stop("a drafted word occurs twice")
    classes = pop.load_classes()
    spec = pop.load_specification_document_set()
    if len(spec) != 26:
        raise Stop("the specification document set has %d members, not 26" % len(spec))
    spec_set = set(spec)
    terms = CORE + COUNTED_IN_CONTEXT

    in_set_hits = []                       # every hit record in a set member, whole
    residue_per_term = {t: 0 for t in terms}
    residue_files_per_term = {t: set() for t in terms}
    absent = []
    searched = set()
    for cls in pop.SEARCH_CLASSES:
        for rel in classes[cls]:
            if rel in searched:
                continue
            searched.add(rel)
            path = os.path.join(ROOT, rel)
            if not os.path.isfile(path):
                absent.append(rel)
                continue
            with open(path, "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            for h in pop.search_terms(text, terms, "draft"):
                if rel in spec_set:
                    in_set_hits.append({"file": rel, "line_number": h["line_number"], "term": h["term"],
                                        "whole_word_on_line": whole_word(h["term"], h["line"]),
                                        "line": h["line"]})
                else:
                    residue_per_term[h["term"]] += 1
                    residue_files_per_term[h["term"]].add(rel)
    set_members_not_searched = sorted(spec_set - (searched - set(absent)))
    if set_members_not_searched:
        raise Stop("specification set members not searched (outside the classes or absent): %s"
                   % ", ".join(set_members_not_searched))

    def lines_of(ts):
        return {(h["file"], h["line_number"]) for h in in_set_hits if h["term"] in ts}

    core_lines = lines_of(set(CORE))
    per_term = {}
    for t in terms:
        hs = [h for h in in_set_hits if h["term"] == t]
        per_term[t] = {
            "half": "CORE" if t in CORE else "COUNTED_IN_CONTEXT",
            "in_set_hit_lines": len(hs),
            "in_set_files": len({h["file"] for h in hs}),
            "of_those_hit_lines_where_it_is_also_a_whole_word": sum(1 for h in hs if h["whole_word_on_line"]),
            "residue_hit_lines": residue_per_term[t],
            "residue_files": len(residue_files_per_term[t]),
        }
    adds = {}
    for t in COUNTED_IN_CONTEXT:
        extra = sorted(lines_of({t}) - core_lines)
        adds[t] = {"in_set_hit_lines_no_core_word_reaches": len(extra),
                   "those_lines": [h for h in in_set_hits if h["term"] == t
                                   and (h["file"], h["line_number"]) in set(extra)]}
    all_lines = lines_of(set(terms))
    union_of_parts = core_lines.union(*[set(lines_of({t})) for t in COUNTED_IN_CONTEXT])
    if all_lines != union_of_parts:
        raise Stop("the union of the parts does not equal the whole")
    if any(adds[t]["in_set_hit_lines_no_core_word_reaches"] > per_term[t]["in_set_hit_lines"]
           for t in COUNTED_IN_CONTEXT):
        raise Stop("a word adds more lines than it hits")

    result = {
        "★_what_this_artifact_is": (
            "THE READ-ONLY COUNT OF THE DRAFT L3 KEYWORD LIST, taken before the user rules its membership "
            "(Option B item 3, records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md). "
            "The words are measurement inputs authored by the writing side, not a ruling."),
        "★_what_it_does_not_do": (
            "It derives no outgoing population, tabulates, compares and grades nothing, and judges no word's "
            "sense. The whole-word flag is mechanical; which sense of a word fired is a reading."),
        "the_matcher": "search_terms of tools/audit/gen_l0_l1_outgoing_population.py, imported: case-insensitive substring, one record per matched line per term",
        "the_classes_searched": list(pop.SEARCH_CLASSES),
        "files_searched": len(searched) - len(absent),
        "class_members_absent_from_the_tree": absent,
        "specification_set_members": len(spec),
        "specification_set_members_not_in_the_searched_classes": set_members_not_searched,
        "the_draft": {"CORE": list(CORE), "COUNTED_IN_CONTEXT": list(COUNTED_IN_CONTEXT)},
        "the_counts": {
            "in_set_hit_lines_CORE": len(core_lines),
            "in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT": len(all_lines),
            "in_set_files_with_a_CORE_hit": len({f for f, _ in core_lines}),
            "in_set_files_with_any_hit": len({f for f, _ in all_lines}),
        },
        "per_term": per_term,
        "what_each_COUNTED_IN_CONTEXT_word_adds_beyond_CORE": adds,
        "every_in_set_hit_record": sorted(in_set_hits, key=lambda h: (h["file"], h["line_number"], h["term"])),
        "the_bound_on_this_measurement": (
            "A lower bound on the relevant text, never a census: a passage about L3's subject using none of "
            "these words is not found. Residue is counted per word only; the population run publishes residue "
            "whole. Every specification set member was searched; a member outside the classes or absent "
            "from the tree stops the script."),
    }
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(result, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    c = result["the_counts"]
    print("files searched:", result["files_searched"], "| set members:", len(spec),
          "| set members not searched:", len(set_members_not_searched))
    print("in-set hit lines, CORE:", c["in_set_hit_lines_CORE"],
          "| CORE plus counted-in-context:", c["in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT"])
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (Stop, pop.Stop) as stop:
        print("STOP: %s" % stop)
        sys.exit(2)
```

**Its printed output, verbatim** — `python <scratch>/l3_keyword_count.py > <scratch>/l3_kw_out.txt 2>&1; echo "exit:$?"`,
run from the repository root — **exit 0**:

```
files searched: 206 | set members: 26 | set members not searched: 0
in-set hit lines, CORE: 1013 | CORE plus counted-in-context: 1813
wrote C:\s\MS\tools\audit\l3_keyword_count_measurement.json
```

**The second script**, `l3_kw_checks.py`, which reads the written artifact and
`tools/audit/specification_document_set.json` and nothing else, whole:

```python
"""1(e): the four checks over the written artifact, read from the working tree."""
import json, os

ROOT = r"C:\s\MS"
ART = os.path.join(ROOT, "tools", "audit", "l3_keyword_count_measurement.json")
SPEC = os.path.join(ROOT, "tools", "audit", "specification_document_set.json")

with open(ART, "r", encoding="utf-8") as fh:
    a = json.load(fh)
with open(SPEC, "r", encoding="utf-8") as fh:
    members = {r["member"] for r in json.load(fh)["the_document_set"]}

core = a["the_draft"]["CORE"]
cic = a["the_draft"]["COUNTED_IN_CONTEXT"]
per_term = a["per_term"]

# 1. per_term carries all 29 drafted words, each with its half
c1 = (set(per_term) == set(core) | set(cic) and len(per_term) == 29
      and all(per_term[t]["half"] == "CORE" for t in core)
      and all(per_term[t]["half"] == "COUNTED_IN_CONTEXT" for t in cic))
print("1. per_term carries all 29 drafted words, each with its half:", c1,
      "(%d keys)" % len(per_term))

# 2. CORE count <= CORE plus counted-in-context count
counts = a["the_counts"]
c2 = counts["in_set_hit_lines_CORE"] <= counts["in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT"]
print("2. in_set_hit_lines_CORE <= in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT:", c2)

# 3. distinct (file, line_number) pairs equal the CORE-plus count
records = a["every_in_set_hit_record"]
pairs = {(r["file"], r["line_number"]) for r in records}
c3 = len(pairs) == counts["in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT"]
print("3. distinct (file, line_number) pairs equal the CORE-plus count:", c3,
      "(%d records, %d distinct pairs)" % (len(records), len(pairs)))

# 4. every file is a member of the specification document set
outside = sorted({r["file"] for r in records} - members)
c4 = not outside
print("4. every file in every_in_set_hit_record is a set member:", c4,
      "(files outside the set: %s)" % (outside or "none"))

print("ALL FOUR HELD:", c1 and c2 and c3 and c4)
```

**Its output, verbatim** (exit 0):

```
1. per_term carries all 29 drafted words, each with its half: True (29 keys)
2. in_set_hit_lines_CORE <= in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT: True
3. distinct (file, line_number) pairs equal the CORE-plus count: True (2164 records, 1813 distinct pairs)
4. every file in every_in_set_hit_record is a set member: True (files outside the set: none)
ALL FOUR HELD: True
```

**1(e)'s four checks, graded:**

1. **HELD** — `per_term` carries all 29 drafted words, each with its `half`.
2. **HELD** — `the_counts.in_set_hit_lines_CORE` ≤ `the_counts.in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT`.
3. **HELD** — the distinct `(file, line_number)` pairs in `every_in_set_hit_record` equal
   `the_counts.in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT`. *(The record count exceeds the pair count in the output
   above because the matcher writes one record per matched line PER TERM, so a line two drafted words both match is
   two records and one pair — the matcher's documented shape, not a defect.)*
4. **HELD** — every `file` in `every_in_set_hit_record` is a member of `the_document_set`.

**Where the counts are read.** Per word: `tools/audit/l3_keyword_count_measurement.json` → `per_term` (each word's
half, its in-set hit lines and files, how many of those lines also carry it as a whole word, and its residue lines and
files). What each counted-in-context word adds beyond the core words, with every line that makes it up:
→ `what_each_COUNTED_IN_CONTEXT_word_adds_beyond_CORE`. Every in-set hit line, whole: → `every_in_set_hit_record`. The
artifact's own bound: → `the_bound_on_this_measurement`. **No per-word value is given in this report**, and which sense
of a word fired on any line is not judged here — the whole-word flag is mechanical and the reading is the writing
side's and the user's.

**What was not opened.** The artifact's hit lines were not read by this session beyond the four checks above, which
read only file paths, line numbers and counts. The blind derivation `cowork_blind_derivation_l3_2026_10_17.md` and the
brief `cowork_blind_session_brief_l3.md` were not opened; where either is a member of the searched classes, its hits
were counted by the script like any other file's.

## 1. Task 0 — the sizes, the first line and the last bytes; the commits, by explicit hash

The four blobs written by `git hash-object -w --no-filters <path>` and measured at the objects only
(`t0_measure.py`, §7), whole:

```
== records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md
   blob 03eb01d7d4bcd969177892f8c4fad82816839f22  size 7763
   NUL byte present: False
   ends with a newline: True
   last line: (Ruling 1).*
   last 24 bytes: b'tion); "B"\n(Ruling 1).*\n'
   first line: # Rulings — the L3 outgoing-population sitting, 2026-10-17
   first line equals the expected: True
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_one.md
   blob 43eaf715bf1452d96d0de66f1821c823c0bda5e4  size 4875
   NUL byte present: False
   ends with a newline: True
   last line: instruction; "continue"; "continue"; "B".*
   last 24 bytes: b'nue"; "continue"; "B".*\n'
== records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_two.md
   blob 1f2cad12e523ddb9c9dd5703f9affaf7ddc7189b  size 5354
   NUL byte present: False
   ends with a newline: True
   last line: instruction; "continue"; "continue".*
   last 24 bytes: b'continue"; "continue".*\n'
== records/cc/instructions/cc_instruction_l3_keyword_count_2026_10_17.md
   blob 208961216e5b912f0bb37464c459f38e2c1017e8  size 43956
   NUL byte present: False
   ends with a newline: True
   last line: the STOP added at (4) and the bar added at (1).
   last 24 bytes: b'd the bar added at (1).\n'
```

- **The ruling record: 7,763 bytes — the expected `7763`. Its first line equals the expected
  `# Rulings — the L3 outgoing-population sitting, 2026-10-17`.**
- **Entry 421: 4,875 bytes — the expected `4875`.**
- **Entry 422: PRESENT, 5,354 bytes** (the dispatch states no size for it, by its own restraint paragraph); landed.
- **This dispatch: 43,956 bytes**, the same blob under the default filters as under `--no-filters`
  (`208961216e5b912f0bb37464c459f38e2c1017e8` both ways).
- **No NUL byte in any of the four; each ends with a newline and a whole final line.** (2) held.

| Act | Commit | What it carries |
|---|---|---|
| the tree met | `79499c21ec70bcf5e0a817050ade5bc1268d6a51` | `master` and `origin/master`, both read at the ref files with the file tools |
| Task 0 | `102e701c290260c0c0027fa3db4883abbe37ebb1` | this dispatch, the ruling record, entries 421 and 422 |
| Task 1 | `9c4e3296794b9291ee6d7cb879aab8046ea8e0ae` | `tools/audit/l3_keyword_count_measurement.json`, alone |
| the close | see the git log | `STATUS.md`, `STATUS_ARCHIVE.md`, the re-aimed `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`, the three A2 regenerations, `tools/audit/session_start_read_size.json`, this report, the close section of `records/cowork/handoff/cowork_away_returns.md` |
| the end state | see the git log | the full guard run at the close's tree, with whatever A2 orders regenerated |

The Task 0 commit and its push, whole:

```
[master 102e701c29] record: the l3 outgoing-population ruling, entries 421-422 and the l3 keyword-count dispatch
 4 files changed, 811 insertions(+)
 create mode 100644 records/cc/instructions/cc_instruction_l3_keyword_count_2026_10_17.md
 create mode 100644 records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_one.md
 create mode 100644 records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_two.md
 create mode 100644 records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md
To https://github.com/slimvince/MuseScore
   79499c21ec..102e701c29  master -> master
```

It was verified at the object — `python tools/audit/changed_paths.py --commit 102e701c…` lists exactly the four paths
as added, its parent is `79499c21…`, and `git rev-parse 102e701c…:<path>` returns, per path, the very blob measured
above. The staged set was proved to be exactly the four paths (`changed_paths.py --staged`) before the commit, and the
pinned dispatch was re-hashed immediately before staging and returned its pinned blob. `.git/refs/remotes/origin/master`
then named `102e701c290260c0c0027fa3db4883abbe37ebb1`.

The Task 1 commit and its push, whole:

```
[master 9c4e329679] audit: the read-only count of the draft l3 keyword list (no population, no ruling)
 1 file changed, 21268 insertions(+)
 create mode 100644 tools/audit/l3_keyword_count_measurement.json
To https://github.com/slimvince/MuseScore
   102e701c29..9c4e329679  master -> master
```

Verified at the object: `changed_paths.py --commit 9c4e3296…` lists the artifact alone as added; its parent is
`102e701c…`; the artifact's blob there (`49f3c4e9843f53fd2bed70b4f8c11048109edc38`) equals `git hash-object` of the
written file. `.git/refs/remotes/origin/master` then named `9c4e3296794b9291ee6d7cb879aab8046ea8e0ae`.

## 2. The guard states

**Before the first edit** — `python tools/audit/gen_guard_state.py --check`, exit 1, whole:

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
  [FAIL] tools/audit/gen_evidence_pin_membership.py --check
  [PASS] tools/audit/gen_session_start_read_size.py --check
  [PASS] tools/audit/gen_defense_share.py --check
  [FAIL] tools/audit/gen_epoch_write_path.py --check
  [PASS] tools/audit/gen_derivation_boot_pack.py --check
  [FAIL] tools/audit/gen_recognizer_establishment_sort.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --check
  [PASS] tools/audit/gen_l2_withheld_documents.py --subject l3 --check
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
81 guard(s) run, 14 failing, 4 not run, 20 historical record(s)
```

**A2 HELD AT THE START:** the failing set is exactly the thirteen of the premise ledger plus
`gen_evidence_pin_membership.py --check`, red as A2 predicted because the ruling record was untracked at boot; the
first line's *STALE vs the run* is the guard state's own artifact not re-deriving for that same red. Nothing was
regenerated before the Task 0 commit.

**`tools/audit/gen_guard_classification.py --check` before the close** (exit 2), whole — the same message the previous
batch reported, carried and not chased:

```
STOP: tool(s) in the guard-state population with no authored verdict: ['tools/audit/gen_l0_l1_outgoing_population.py', 'tools/audit/gen_l2_withheld_documents.py', 'tools/audit/gen_withheld_family_reading.py']
```

**At the end** — carried by the end-state commit and recorded in the close section's end-state portion in
`records/cowork/handoff/cowork_away_returns.md`, not asserted here.

## 3. A1 to A3, E0 to E2, graded

- **A1 — HELD, BY CONTENT.** The five tracked inputs this batch edits each diffed empty against `79499c21…`
  (`git diff --stat 79499c21ec70bcf5e0a817050ade5bc1268d6a51 -- <path>`, no output). Per path of Task 0's list, all four
  untracked (`git ls-files --others --exclude-standard`), none tracked. The whole population through
  `tools/audit/changed_paths.py` showed exactly ONE tracked modification, `tools/audit/claude_md_finer_archive.json`,
  whose `git hash-object` equals the tip's blob (`1df4f20771b6782cbb965c293db4d445bc7ec892`, both): line endings only,
  left untouched, never staged. **Untracked paths outside Task 0's list, NOT landed:** none under `records/`,
  `reading_pass/` or `ratification_surfaces/`; at the repository root `Claude outputs/`, `Codex research inventory/` and
  two files under `external resarch summary/`; elsewhere `docs/research_papers/polyph9-release/`, the
  `scratch_artifacts/` population and `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` — exactly the
  standing population A1 names. After Task 1 the same enumeration showed one new untracked path, the artifact, and no
  tracked modification beyond A1's. No further handoff entry or ruling record appeared during the run.
- **A2 — HELD AT THE START** (§2). The end prediction is carried by the end-state commit.
- **A3** — verified at the objects after the last commit, in the close section's end-state portion.
- **E0 — MET.** (2) held; the four named paths in one commit, `102e701c…`; `origin/master` at it; every path accounted
  for (four untracked and landed, none absent, entry 422 present).
- **E1 — MET.** 1(d) exit 0; 1(e)'s four checks held; the artifact alone in one commit, `9c4e3296…`; `origin/master`
  at it.
- **E2** — carried by the end-state commit, not asserted here.

## 4. Task 2 — the close's `STATUS.md` entries and the forward-bound move

**(a)** Three entries written at the top of `STATUS.md`: the close entry first, carrying the `Last updated: ` prefix and
naming this dispatch by its file name, then Task 1's and Task 0's entries, each saying `Same dispatch`. The prefix was
removed from the derivation-commit batch's close entry; no other existing sentence of `STATUS.md` was rewritten or
removed. The three are dated 2026-10-18, the day both task commits and the close were made (§6 item 2).

**(b)** The authored constants of `tools/audit/gen_status_batch_bound.py` were re-aimed after it was read whole at the
object `79499c21…:tools/audit/gen_status_batch_bound.py` — `BASE_COMMIT` at `9c4e3296…` (Task 1, this batch's last task
commit before the close; its `STATUS.md` object is `c8c5b385d13c2af67e636d983e544e7518163f09`, the same blob at
`79499c21…` and at `102e701c…`, established by `git rev-parse` of each), `PREVIOUS_BATCH_DISPATCH` at
`cc_instruction_l3_derivation_commit_2026_10_17.md`, `ACT_DATE` at `2026-10-18`, `DISPATCH` at
`cc_instruction_l3_keyword_count_2026_10_17.md`, `TASK` at `Task 2`, `MOVE_KIND` unchanged at `ordinary` — each
comment re-stated with the former value named, and one row appended to `PREVIOUS_AIMINGS` in the shape the dispatch
gives. The diff against the Task 1 commit, whole (`git diff -U0 9c4e3296… -- tools/audit/gen_status_batch_bound.py`):

```
diff --git a/tools/audit/gen_status_batch_bound.py b/tools/audit/gen_status_batch_bound.py
index 148b5412ae..2df8a4eb25 100644
--- a/tools/audit/gen_status_batch_bound.py
+++ b/tools/audit/gen_status_batch_bound.py
@@ -1332 +1332,31 @@ OUT = os.path.join(HERE, "status_batch_bound.json")
-BASE_COMMIT = "96a24b01b87b94ce157ff471946e38c664d6f844"
+# ★ RE-AIMED 2026-10-18 by `cc_instruction_l3_keyword_count_2026_10_17.md` Task 2, at its 2(b), and
+# ALL FIVE authored inputs moved together, `PREVIOUS_AIMINGS` being appended to rather than replaced
+# (#12) and `MOVE_KIND` staying at the value it already carried, which is the value this move takes.
+# The aiming it replaces is the L3 derivation commit's, which is ALREADY the last row of
+# `PREVIOUS_AIMINGS` — that batch recorded its own aiming in its own act — so it is not appended a
+# second time, and this batch's aiming is appended instead. `BASE_COMMIT` was
+# `96a24b01b87b94ce157ff471946e38c664d6f844` and is now
+# `9c4e3296794b9291ee6d7cb879aab8046ea8e0ae`: this batch's Task 1 commit — the read-only count of the
+# draft L3 keyword list, its one measurement artifact — which is its LAST TASK COMMIT before the close,
+# as the executing dispatch orders. Neither of this batch's task commits carries a `STATUS.md` change,
+# so that commit's `STATUS.md` object is the one both refs carried when this batch opened
+# (`79499c21ec70bcf5e0a817050ade5bc1268d6a51`, read at the two ref FILES with the file tools, D-253) —
+# the same blob at that commit, at this batch's Task 0 commit `102e701c…` and at its Task 1 commit,
+# established at `git rev-parse` of each — and it carries the L3 derivation commit's entries at the
+# head of the dated entries.
+#
+# ★★ THE THEN-PREVIOUS BATCH IS THE L3 DERIVATION COMMIT. `PREVIOUS_BATCH_DISPATCH` was
+# `cc_instruction_l3_brief_landing_2026_10_17.md` and now names
+# `cc_instruction_l3_derivation_commit_2026_10_17.md`, whose close entry names it and whose entry below
+# it says `Same dispatch`; that batch wrote its entries and its move inside its own Task 1, landed in
+# its close commit `ca9c9c42…`, and no close ran between it and this batch writing an entry of its own.
+#
+# **THE DECLARED PREFIX ADJUSTMENT IS EXPECTED TO FIRE**, that batch's close entry carrying the
+# `Last updated: ` prefix at the base commit, which is why this batch's own entries were written into
+# `STATUS.md` BEFORE `--apply` ran. `ACT_DATE` and the executing dispatch's date DIFFER here: the
+# dispatch is dated 2026-10-17 and the move ran on 2026-10-18, and `ACT_DATE` carries the day the move
+# ran. **The second writing's two nameless 2026-09-02 entries remain in `STATUS.md` and no aiming of
+# this tool can identify them** — a declared state and not a STOP, unchanged by this act. **NO COUNT OF
+# THE ENTRIES EXPECTED TO MOVE IS WRITTEN HERE** (D-431): the membership is DERIVED from the entries'
+# own text at the base commit.
+BASE_COMMIT = "9c4e3296794b9291ee6d7cb879aab8046ea8e0ae"
@@ -1441 +1471,4 @@ BASE_COMMIT = "96a24b01b87b94ce157ff471946e38c664d6f844"
-PREVIOUS_BATCH_DISPATCH = "cc_instruction_l3_brief_landing_2026_10_17.md"
+# *(`PREVIOUS_BATCH_DISPATCH` read "cc_instruction_l3_brief_landing_2026_10_17.md" while
+# `cc_instruction_l3_derivation_commit_2026_10_17.md` was the executing act; it is re-stated here for
+# `cc_instruction_l3_keyword_count_2026_10_17.md`, whose then-previous batch is that one.)*
+PREVIOUS_BATCH_DISPATCH = "cc_instruction_l3_derivation_commit_2026_10_17.md"
@@ -1565,2 +1598,6 @@ PREVIOUS_BATCH_DISPATCH = "cc_instruction_l3_brief_landing_2026_10_17.md"
-ACT_DATE = "2026-10-17"
-DISPATCH = "cc_instruction_l3_derivation_commit_2026_10_17.md"
+# *(`ACT_DATE` read "2026-10-17" and `DISPATCH` `cc_instruction_l3_derivation_commit_2026_10_17.md`
+# while that batch was the executing act; both are re-stated here for
+# `cc_instruction_l3_keyword_count_2026_10_17.md`, dated 2026-10-17, whose move ran on 2026-10-18, so
+# the two dates DIFFER and `ACT_DATE` carries the day the move ran, which is this comment's own rule.)*
+ACT_DATE = "2026-10-18"
+DISPATCH = "cc_instruction_l3_keyword_count_2026_10_17.md"
@@ -1712,2 +1749,5 @@ DISPATCH = "cc_instruction_l3_derivation_commit_2026_10_17.md"
-# *"Task 1 — the close"* names in those words.)*
-TASK = "Task 1"
+# *"Task 1 — the close"* names in those words. It names Task 2 while
+# `cc_instruction_l3_keyword_count_2026_10_17.md` is the executing act, that dispatch ordering both
+# halves of the close — this batch's own entries at its 2(a) and this move at its 2(b) and 2(c) —
+# inside its own Task 2, which that dispatch's heading *"Task 2 — the close"* names in those words.)*
+TASK = "Task 2"
@@ -2221,0 +2262,4 @@ PREVIOUS_AIMINGS = [
+    {"executing_act": "cc_instruction_l3_keyword_count_2026_10_17.md, Task 2",
+     "base_commit": "9c4e3296794b9291ee6d7cb879aab8046ea8e0ae",
+     "the_then_previous_batch": "cc_instruction_l3_derivation_commit_2026_10_17.md",
+     "the_kind_of_move": "ordinary"},
```

Every deleted line is one of the five re-aimed value lines or the one comment line that the `TASK` comment extended in
place; no function and no existing row was touched.

**(c)** `python tools/audit/gen_status_batch_bound.py --apply` (exit 0), whole:

```
wrote tools\audit\status_batch_bound.json
  entries moved: 2, 2,074 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

and `--check` (exit 0), whole:

```
  entries moved: 2, 2,074 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

**The prediction HELD, read at the artifact rather than at the green `--check` (OI-379):**
`tools/audit/status_batch_bound.json` → `the_moved` names, by their openings, exactly the derivation-commit batch's two
entries — its close entry, the one naming `cc_instruction_l3_derivation_commit_2026_10_17.md` as Task 1, the close
(membership *names the dispatch*; the one declared prefix adjustment was applied to it), and its Task 0 entry
(membership *says `Same dispatch`*). The two 2026-09-02 entries stayed in `STATUS.md` and were not moved by hand.

## 5. Regenerations, and the members they changed

After (a) to (c), each `--check` A2 names was run; all four were red (`regen_checks_before.txt`, whole):

```
== gen_evidence_pin_membership.py
STALE vs the derivation: evidence_pin_membership.json does not re-derive
== gen_l0_l1_outgoing_population.py
STALE vs the derivation: l0_l1_outgoing_population.json does not re-derive
== gen_defense_share.py
STALE vs the measurement: defense_share.json does not re-derive
== gen_session_start_read_size.py
STALE vs the measurement: session_start_read_size.json does not re-derive
```

The first three were regenerated and each `--check` re-run green, whole:

```
== gen_evidence_pin_membership.py
wrote tools/audit/evidence_pin_membership.json
  generated ratification documents 7; ruling records read 168
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
the evidence pin's class membership re-derives
  generated ratification documents 7; ruling records read 168
  members 7 — pinned 5, UNRESOLVED 0
  tools carrying a pin constant 8; outside this class 3
    tools/audit/gen_artifact_inventory_surface.py        NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_claude_md_finer_surface.py           PINNED — at the commit a ruling record states
    tools/audit/gen_ratified_document_check.py           PINNED — at the commit a ruling record states
    tools/audit/gen_governing_surface_readers.py         PINNED — at the commit a ruling record states
    tools/audit/gen_rulings_sort.py                      NOT PINNED — a record states the commit; the pin is not applied
    tools/audit/gen_deciding_act_recovery.py             PINNED — by the route the tool's own pin constant records
    tools/audit/gen_decisions_filter.py                  PINNED — by the route the tool's own pin constant records
== gen_l0_l1_outgoing_population.py
named members: 11
specification set members as read: 26
files with an admitting hit: 112 (outside the named members: 103)
  of those IN the specification set: 18; residue: 85
population in comparison order: 29 entries (before the cut: 114)
size stop reached: False (threshold 40, evaluated on the IN-set count)
wrote C:\s\MS\tools\audit\l0_l1_outgoing_population.json
l0_l1_outgoing_population.json re-derives
== gen_defense_share.py
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
    of the whole session-start read (248265): 5.22%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
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
    of the whole session-start read (248265): 5.22%
  THE VALUE IS A LOWER BOUND ON MARKED DEFENSE: the marker set's reach is UNMEASURED,
  and the ends are AUTHORED (cowork_defense_clause_ends_2026_09_08.md).
```

Each artifact compared with its committed blob by explicit hash (`git diff -U0 9c4e3296… -- <artifact>`), whole:

```
diff --git a/tools/audit/evidence_pin_membership.json b/tools/audit/evidence_pin_membership.json
index dc18d6a74f..0881139392 100644
--- a/tools/audit/evidence_pin_membership.json
+++ b/tools/audit/evidence_pin_membership.json
@@ -20 +20 @@
-  "ruling_records_read": 167,
+  "ruling_records_read": 168,
@@ -310,0 +311 @@
+  "records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md",
```

```
diff --git a/tools/audit/defense_share.json b/tools/audit/defense_share.json
index 55ffa7b1e0..dd955a9887 100644
--- a/tools/audit/defense_share.json
+++ b/tools/audit/defense_share.json
@@ -80 +80 @@
-  "the_whole_ordinary_session_start_read": 247781,
+  "the_whole_ordinary_session_start_read": 248265,
@@ -145 +145 @@
-  "share_of_the_whole_ordinary_session_start_read": 5.23
+  "share_of_the_whole_ordinary_session_start_read": 5.22
```

```
diff --git a/tools/audit/l0_l1_outgoing_population.json b/tools/audit/l0_l1_outgoing_population.json
index b0d11ea544..bf3664bc8b 100644
--- a/tools/audit/l0_l1_outgoing_population.json
+++ b/tools/audit/l0_l1_outgoing_population.json
@@ -236 +236 @@
-    "release": 75,
+    "release": 73,
@@ -3314,23 +3313,0 @@
-   "STATUS.md": {
-    "path": "STATUS.md",
-    "inventory_class": "governing-documents",
-    "is_a_named_member": false,
-    "in_the_specification_document_set": false,
-    "admitting_hit_count": 0,
-    "recorded_hit_count": 2,
-    "admitting_hits": [],
-    "recorded_hits": [
-     {
-      "line_number": 8,
-      "term": "release",
-      "tier": "recorded",
-      "line": "*Last updated: 2026-10-17 (CC — `records/cc/instructions/cc_instruction_l3_derivation_commit_2026_10_17.md`, Task 1, the close. **★★ THE BLIND DERIVATION OF L3 IS IN GIT AS IT STANDS — NOT COMPARED, NOT RATIFIED — AND THE RELEASED L3 BRIEF IS IN GIT, PROVED UNCHANGED SINCE ITS RELEASE; NO ALGORITHM CHANGED.** ★ `cowork_blind_derivation_l3_2026_10_17.md` is committed exactly as the deriving session delivered it, its DRAFT banner intact; before staging, its size, its first line, its single DRAFT banner line and its last line were checked against what the writing side recorded, and nothing in it was read beyond those checks. ★ `cowork_blind_session_brief_l3.md` is committed with its RELEASED banner, after its size and its banner line were proved equal to what the writing side recorded at release; every line it changed since its DRAFT commit lies in the banner block at its head. ★ Handoff entries 419 and 420 and this dispatch are committed as they stood, the dispatch pinned to its blob and proved unmoved before staging. **No comparison of the derivation with anything was made**; no session booted, no score copied or staged, no pack rendered, no file Task 0 committed was edited, no ruling taken and no question or recommendation put to the user, no open-items row created, flipped or discarded, no decisions-register entry and no `D-NNN` allocated; no `src/` file, build, test, golden, corpus of scores or measurement of the analysis. Per the OI-222 pointer convention this entry is a **POINTER** — the whole of it is `records/cc/reports/cc_report_l3_derivation_commit_2026_10_17.md` — and no count is restated here (**D-431**).)*"
-     },
-     {
-      "line_number": 10,
-      "term": "release",
-      "tier": "recorded",
-      "line": "*2026-10-17 (CC — Same dispatch, Task 0. **THIS DISPATCH, THE BLIND DERIVATION OF L3, THE RELEASED L3 BRIEF AND HANDOFF ENTRIES 419 AND 420 ARE LANDED**, as they stood: the brief proved unchanged since its release, the derivation checked at its size and its three lines, and the dispatch pinned to its blob and proved unmoved, each before staging. **POINTER** — `records/cc/reports/cc_report_l3_derivation_commit_2026_10_17.md` (**D-431**).)*"
-     }
-    ]
-   },
```

- **`tools/audit/evidence_pin_membership.json`** — **the one member change allowed, and only it:** the ruling record
  `records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md` added to the list of ruling
  records read, with that list's count moving with it. No member of the evidence-pin class moved.
- **`tools/audit/l0_l1_outgoing_population.json`** — **a moved hit record of `STATUS.md`, allowed and reported by
  name:** `STATUS.md`'s per-file record is gone, its two RECORDED-tier hits on the term `release` (lines 8 and 10 —
  the derivation-commit batch's two entries this batch's move took to the archive) leaving with it, and the `release`
  hit count falls with them. `STATUS.md` carried no admitting hit, is not a named member and is not in the
  specification document set; **no member of the population moved**, and the population and residue lists are
  unchanged.
- **`tools/audit/defense_share.json`** — the whole-read denominator and the share derived from it, both moved by this
  batch's `STATUS.md` entries; no clause, row or span moved.
- **`tools/audit/session_start_read_size.json`** — regenerated LAST, after the final `STATUS.md` edit; `--check` green,
  whole:

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
    STATUS.md                                                                 11836
    DECISIONS.md                                                             127727
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → gating_ids     2826
  total at the tree 248265
  further spans of the same artifact, NOT counted into the read:
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → the_gating_rows    62498
    tools/audit/nongating_apparatus_rows.json → ★_the_live_gating_answer → ★_the_frozen_enumeration_measured_against_this_one     4951
  vs 1760d9a4a8: 367121 [whole-file practice] -> 248265 [ruled membership]  (-118856, -32.38%)  <- CROSSES A REGIME BOUNDARY
  vs 594074e1e1: 296832 [whole-file practice] -> 248265 [ruled membership]  (-48567, -16.36%)  <- CROSSES A REGIME BOUNDARY
```

`tools/audit/gen_l2_outgoing_population.py` was not run, in any operating mode, and its artifact was not touched (A2).

## 6. Declared departures

1. **The dispatch was read from the working tree before it was pinned** — standing clause P-2's fallback route, the
   user's opening line naming only the file. Pinned at Task 0 (`git hash-object -w`, blob `20896121…`); re-hashed and
   proved unmoved immediately before staging; the committed blob is the same. The §1(c) script was compared against
   the block read from the pinned blob, not from the working tree.
2. **The calendar date changed during the run.** The dispatch is dated 2026-10-17; this batch's reads and its first
   guard run took place on 2026-10-17, and both task commits and the close fall on 2026-10-18 (`git show -s
   --format='%H %ci'` of each task commit). So this batch's `STATUS.md` entries are dated 2026-10-18, and `ACT_DATE` is
   `2026-10-18` and DIFFERS from the dispatch's date, which the tool's own comment provides for.
3. **One check beyond the dispatch's own was run, read-only:** `script_vs_dispatch.py` proved the scratch script
   identical to the dispatch's text before it ran. It writes nothing.
4. **`git hash-object -w` was run on working-tree files** — the dispatch for P-2 under the default filters, then the
   four Task 0 files with `--no-filters` as Task 0 orders, and `claude_md_finer_archive.json` without `-w` for A1.
   Every committed blob equals the blob measured.
5. **Most checks and scripts were run with `PYTHONIOENCODING=utf-8`**; the measuring script itself was run exactly as
   1(d) gives it, and its output is ASCII.
6. **Each commit message carries one trailer line after the ordered subject** — the co-author attribution this
   session's instructions require — as a second paragraph; the subject lines are exactly the ordered ones.
7. **The forward-bound tool was read whole at the object through `git show 79499c21…:<path>` redirected to a scratch
   file**, then read there with the file tools.
8. **This report was assembled by a scratch script** that replaced marked places with the run outputs verbatim (§7).

## 7. The scripts, whole

`t0_measure.py` — Task 0's measurement at the git objects:

```python
"""Task 0 (2): measure each landed file at its blob (git object reads only)."""
import subprocess

ROOT = r"C:\s\MS"
BLOBS = [
    ("records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md",
     "03eb01d7d4bcd969177892f8c4fad82816839f22"),
    ("records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_one.md",
     "43eaf715bf1452d96d0de66f1821c823c0bda5e4"),
    ("records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_two.md",
     "1f2cad12e523ddb9c9dd5703f9affaf7ddc7189b"),
    ("records/cc/instructions/cc_instruction_l3_keyword_count_2026_10_17.md",
     "208961216e5b912f0bb37464c459f38e2c1017e8"),
]
FIRST = "# Rulings — the L3 outgoing-population sitting, 2026-10-17"


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], check=True,
                          stdout=subprocess.PIPE).stdout


for path, blob in BLOBS:
    raw = git("cat-file", "blob", blob)
    size = git("cat-file", "-s", blob).decode().strip()
    text = raw.decode("utf-8")
    lines = text.split("\n")
    last = lines[-2] if text.endswith("\n") else lines[-1]
    print(f"== {path}")
    print(f"   blob {blob}  size {size}")
    print(f"   NUL byte present: {bytes([0]) in raw}")
    print(f"   ends with a newline: {text.endswith(chr(10))}")
    print(f"   last line: {last}")
    print(f"   last 24 bytes: {raw[-24:]!r}")
    if "rulings" in path:
        print(f"   first line: {lines[0]}")
        print(f"   first line equals the expected: {lines[0].rstrip(chr(13)) == FIRST}")
```

`script_vs_dispatch.py` — the identity check of the measuring script against the pinned dispatch:

```python
"""Compare the scratch script with the dispatch's 1(c) code block, read from the pinned blob."""
import subprocess

ROOT = r"C:\s\MS"
BLOB = "208961216e5b912f0bb37464c459f38e2c1017e8"
SCRIPT = r"C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\9e4a9670-a40a-400c-b5cf-17541484626d\scratchpad\l3_keyword_count.py"

text = subprocess.run(["git", "-C", ROOT, "cat-file", "blob", BLOB], check=True,
                      stdout=subprocess.PIPE).stdout.decode("utf-8")
section = text.split("### 1(c) The measuring script", 1)[1].split("### 1(d)", 1)[0]
block = section.split("```python\n", 1)[1].split("\n```", 1)[0] + "\n"
with open(SCRIPT, "r", encoding="utf-8", newline="") as fh:
    script = fh.read().replace("\r\n", "\n")
print("dispatch block lines:", block.count("\n"), "| script lines:", script.count("\n"))
print("identical:", block == script)
if block != script:
    for i, (a, b) in enumerate(zip(block.split("\n"), script.split("\n")), 1):
        if a != b:
            print("first difference at line", i)
            print("  dispatch:", repr(a))
            print("  script:  ", repr(b))
            break
```

`assemble_report.py` — the report assembly:

```python
import os, sys
S = r"C:\Users\vince\AppData\Local\Temp\claude\c--s-MS\9e4a9670-a40a-400c-b5cf-17541484626d\scratchpad"
REPORT = r"C:\s\MS\records\cc\reports\cc_report_l3_keyword_count_2026_10_17.md"
MARKS = {
    "KW_SCRIPT": "l3_keyword_count.py",
    "KW_OUT": "l3_kw_out.txt",
    "CHK_SCRIPT": "l3_kw_checks.py",
    "CHK_OUT": "l3_kw_checks.txt",
    "T0_MEASURE": "t0_measure.txt",
    "T0_COMMIT": "t0_commit.txt",
    "PUSH_T0": "push_t0.txt",
    "T1_COMMIT": "t1_commit.txt",
    "PUSH_T1": "push_t1.txt",
    "GUARD_START": "guard_start.txt",
    "GC_PRE": "gc_preclose.txt",
    "SBB_DIFF": "sbb_diff.txt",
    "SBB_APPLY": "sbb_apply.txt",
    "SBB_CHECK": "sbb_check.txt",
    "REGEN_BEFORE": "regen_checks_before.txt",
    "REGEN_RUN": "regen_run.txt",
    "DIFF_EPM": "diff_epm.txt",
    "DIFF_DS": "diff_ds.txt",
    "DIFF_POP": "diff_pop.txt",
    "SSRS_CHECK": "ssrs_check.txt",
    "T0_SCRIPT": "t0_measure.py",
    "SVD_SCRIPT": "script_vs_dispatch.py",
    "ASSEMBLE_SCRIPT": "assemble_report.py",
}
with open(REPORT, "r", encoding="utf-8", newline="") as fh:
    text = fh.read()
# The one inline marker first — this script's own text, inserted below, carries its name.
with open(os.path.join(S, "script_vs_dispatch.txt"), "r", encoding="utf-8-sig", newline="") as fh:
    svd = " / ".join(l for l in fh.read().replace("\r\n", "\n").split("\n") if l)
inline = "{{" + "SVD_INLINE" + "}}"
if text.count(inline) != 1:
    sys.exit(f"STOP: {inline} occurs {text.count(inline)} times")
text = text.replace(inline, "`" + svd + "`")
for mark, name in MARKS.items():
    with open(os.path.join(S, name), "r", encoding="utf-8-sig", newline="") as fh:
        body = fh.read().replace("\r\n", "\n").rstrip("\n")
    token = "{{" + mark + "}}"
    if text.count(token) != 1:
        sys.exit(f"STOP: {token} occurs {text.count(token)} times")
    text = text.replace(token, body)
with open(REPORT, "w", encoding="utf-8", newline="") as fh:
    fh.write(text)
print("assembled", REPORT)
```

The measuring script `l3_keyword_count.py` and the checks script `l3_kw_checks.py` are given whole under
*THE COUNT, AS TAKEN* above.

## 8. Observations, recorded and not acted on

1. **Handoff entry 422 was present at boot** and is landed; it names this report as the next session's first read
   after its own.
2. **The untracked `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` still stands in the tree**, reported
   again. Not landed, not opened.
3. **The classification tool's STOP message is unchanged** from the previous batch's (§2).
4. **The measuring script's population is the inventory's three classes de-duplicated across classes**, as the
   script's own `searched` set gives; the artifact's `files_searched` is that count. Stated so a reader does not expect
   it to equal the sum of the three classes' sizes.

## 9. What this batch did not do

No outgoing population derived; nothing tabulated, compared, dispositioned or graded; no word's sense judged and no
position taken on which words belong in the list; the artifact's hit lines not read beyond the four checks; the blind
derivation and the L3 brief not opened; no session booted, no score copied, staged or written, no pack rendered; no
edit to any handoff entry or ruling record; no tool source edited except the authored aiming of
`gen_status_batch_bound.py`, and no new tool added to the repository; `gen_l2_outgoing_population.py` not run; no
open-items row created, flipped or discarded; no decisions-register entry and no `D-NNN`; nothing in the suspension
file; no ruling taken and no question or recommendation put to the user; no `src/` file, build, test, golden, corpus
of scores, or anything under `tools/corpus/`, `tools/robust_stop/` or `tools/dcml/`; no measurement of the analysis; no
governing document edited except `STATUS.md` and `STATUS_ARCHIVE.md`.

## 10. The plan's tell, in one sentence

**Did this batch produce anything other than the landed paths, the one artifact, the close's files and the report?**
**Yes, by addition only:** the end-state commit carries the guard run's own artifact and whatever A2 orders
regenerated; the scratch scripts of §7 and their outputs live outside the repository; and the `git hash-object -w`
calls wrote the four Task 0 blobs into the object store, each of which the Task 0 commit then references. Nothing
else.

## 11. The standing self-check (D-434) over this batch's own work

Run over the diffs actually on disk — the Task 0 and Task 1 commits at their objects, and the close's diff of
`STATUS.md` and `gen_status_batch_bound.py` read in full above — before this report was committed.

1. **The guiding principles.** **#6** — the count imports the population tool's own matcher and loaders; no second
   matcher exists, and no repository tool was added. **#12** — every in-set hit line is published whole in the
   artifact; the forward-bound move is byte-faithful and its reconciliation is green; every former value of a re-aimed
   constant is named in its comment. **#10 / #14** — no behaviour of the analysis changed; nothing here is a behaviour
   change. **#15** — every verdict above is read at an object or an artifact, not asserted: the commits by explicit
   hash, the moved entries at `the_moved`, the regenerations at their diffs. **#17(f) / D-431** — no value from the
   artifact is restated in prose or in `STATUS.md`; the numbers in this report are the runs' verbatim outputs, which
   the dispatch orders included, and start-state bars the dispatch states. **#19** — the artifact states its own bound
   (a lower bound, never a census) in its own field. **#24** — no difference between measured quantities is asserted.
2. **The conventions.** American English; no self-invented label, abbreviation or numbering (the scratch script names
   are file names, given whole); every non-musical use of a reserved word is qualified — *decisions-register*,
   *open-items row*, *measurement*, *check*, *script*; *score* appears only for the music; the drafted search words
   appear only as quoted search words, never in a non-musical sense of this report's own.
3. **The checklist's rule on quantities and premises (D-431).** Every quantity is named as an artifact and a field, or is a run's verbatim output;
   every premise checked was checked at its primary source — the refs at the ref files, the sizes at the blobs, the
   `STATUS.md` blob at three commits, the moved entries at the artifact.
4. **The file-tools rule.** Working-tree content was read with the file tools only. The shell was used for git object
   queries by explicit hash (`git diff <hash> -- <path>`, `git rev-parse <hash>:<path>`, `git show <hash>:<path>`,
   `git cat-file`), for `git hash-object`, `git add` by explicit path, `git commit` and `git push`, and for the
   sanctioned scripts and this batch's own scratch scripts. No `git status` or working-tree `git diff` was run; every
   shell command carried `; echo "exit:$?"`.
5. **Uncertainty on any comparison.** None asserted.

**Found by the check and corrected on the spot:** nothing. **Found and not correctable inside this batch's scope:**
nothing new; the carried items are §8's.
