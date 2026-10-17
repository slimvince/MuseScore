# CC dispatch — THE READ-ONLY COUNT OF THE DRAFT L3 KEYWORD LIST, taken before the user rules its membership: the records landed, one measurement artifact written, and the close — NOTHING TABULATED, NO POPULATION DERIVED, NO ALGORITHM CHANGE, NO REGISTER ENTRY

> **★★ RELEASED 2026-10-17** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_one.md`, which wrote it, after the check at the
> sources recorded at the end of this file. It is executed by Claude Code when the user hands it over (D-252); the
> Cowork writing side never runs it.
> *(Former banner, preserved (#12): "STATUS: WRITTEN 2026-10-17 — NOT YET RELEASED. … Its check at its sources runs in
> a turn of its own; the banner is set to RELEASED only after that check, which is recorded at the end of this file.")*
>
> **THE WRITING SIDE'S RESTRAINT, declared.** Once released this dispatch is final. The writing side will not touch it,
> nor any file it names, while this batch runs. The one file the writing side writes after release and before
> hand-over is its own handoff entry, `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_two.md`,
> which is why Task 0 states no size for it.

## What this batch is, in plain words

The user ruled, on 2026-10-17 (Option B,
`records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md` §2), which current texts the blind
L3 derivation is compared against. One item of that ruling is a search, over the 26 members of the specification
document set, for an **L3 keyword list** covering L3's five published facts (`FRAMEWORK.md` §5, *L3 — The read-off
facts*: the cadence at each phrase end with its type; the phrase and section grouping; the chord symbol — root pitch
class, quality and bass note; the figured bass; the harmonic rhythm). **The list does not exist yet. The writing side
has drafted it, and the user rules its membership as its own decision.**

Before he rules, this batch counts what each drafted word catches, with the matcher the L0/L1 and L2 population
searches used (the L3 population search is expected to reuse it; that dispatch is not written), and publishes every hit line so that a word matching in a non-musical sense, or inside a longer word, can be seen
rather than argued. That is the shape of the count taken before L2's list was ruled
(`records/cc/instructions/cc_instruction_l2_keyword_count_2026_09_04.md`, which grounded Ruling 86's exclusion of six bare
words, §3co of `records/cowork/rulings/cowork_rulings_2026_08_31_decision_surface_sitting.md`). **The drafted words are
measurement inputs authored by the writing side. They are not a ruling and this batch takes no position on them.**

It does three things and nothing else:

1. **Task 0** lands this dispatch, the ruling record and handoff entries 421 and 422 (422 if present), and pushes.
2. **Task 1** runs one read-only measuring script, writes one artifact, commits it and pushes.
3. **Task 2** closes.

**Documentation and algorithm.** Nothing here changes the algorithm as any specification defines it, and nothing here
amends any documentation: it lands records and measures a search. The currently decided method for L3 is
`FRAMEWORK.md` §5's L3 block (read by this writing side) with DP-I (*"split — cues at L1, type at L3"*).

## Words used in this dispatch, explained first

- **The specification document set** — the 26 member paths at `tools/audit/specification_document_set.json` →
  `the_document_set` → each record's `member`. Ruling 33 (§3an of the 2026-08-31 record) cuts every term search of a
  comparison to it; Option B applies it to L3.
- **The three prose classes** — `SEARCH_CLASSES` in `tools/audit/gen_l0_l1_outgoing_population.py`: the classes of
  `tools/audit/artifact_inventory.json` that the L0/L1 and L2 term searches ran over. A hit file outside the
  specification document set is RESIDUE.
- **The matcher** — `search_terms` in `tools/audit/gen_l0_l1_outgoing_population.py`: case-insensitive substring match,
  one record per matched line per term. The L2 population tool imports it; the L3 population tool is expected to.
- **A hit line** — one line of one file on which at least one term matches.
- **CORE words and COUNTED-IN-CONTEXT words** — the two halves of the draft (Task 1(b)). Both are only inputs. The
  COUNTED-IN-CONTEXT words are those the writing side expects to match often in a non-musical sense, measured
  separately as Ruling 86's six bare words were.
- **The forward bound** — `tools/audit/gen_status_batch_bound.py`, which moves the previous batch's entries from
  `STATUS.md` to `STATUS_ARCHIVE.md` at every close.

## The ruling ledger

| | Record or rule | What it orders | Task |
|---|---|---|---|
| L.1 | The standing clause (a sitting record lands at the next dispatch's Task 0) | The ruling record and entries 421 and 422 landed as they stand. | 0 |
| L.2 | Option B, item 3 (the ruling record §2): the L3 list is drafted by the writing side for L3's five facts and its membership is ruled by the user before the population dispatch is written | This batch measures the draft; it rules nothing and derives no population. | 1 |
| L.3 | D-254 (investigate by default) and the L2 precedent (Ruling 83's owed count, §3cl; the count dispatch of 2026-09-04; Ruling 86, §3co) | The count is taken before the membership is put. That the L2 precedent carries to L3 is this writing side's reading, stated to the user, not a ruling. | 1 |
| L.4 | The user's standing rule of 2026-10-14 (every commit is pushed) | Every commit pushed, the push verified at `.git/refs/remotes/origin/master`. | all |

## Premise ledger (written 2026-10-17 by the writing side from staged copies read with the file tools; no shell command and no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
  `79499c21ec70bcf5e0a817050ade5bc1268d6a51` (read as files). Entry 421 §1 names it the end-state commit of
  `cc_instruction_l3_derivation_commit_2026_10_17.md`, after its Task 0 `96a24b01…` and its close `ca9c9c42…` (relayed
  from entry 421, which read `.git/logs/HEAD`). **Re-read both ref files yourself before Task 0.** If either differs,
  STOP-and-report before any act.
- **FACT — the guard state at the tip** (`tools/audit/guard_state.json` → `summary`): run 81, passing 68, failing 13;
  the thirteen `failing_tools` are those the previous dispatch's premise ledger names (`gen_phase3_gate_partition.py`,
  `gen_filing_convention_application.py`, `gen_artifact_inventory.py`, `gen_artifact_inventory_surface.py`,
  `gen_test_construction_evidence.py`, `gen_retirement_caller_check.py`, `decisions/apply_soft_discard.py`,
  `decisions/apply_residue_discard.py`, `gen_epoch_write_path.py`, `gen_recognizer_establishment_sort.py`,
  `decisions/gen_cluster_dispositions.py --verify`, `decisions/gen_home_classification.py`,
  `decisions/gen_phase1p_delegation_bar.py`), read at the artifact's `failing_tools` list.
- **FACT — the matcher and its helpers** (`tools/audit/gen_l0_l1_outgoing_population.py`, read whole): `search_terms(text,
  terms, tier)` returns one record per matched line per term with `line_number`, `term`, `tier` and the stripped
  `line`; `load_classes()` returns `{class: [paths]}` for `SEARCH_CLASSES`; `load_specification_document_set()` returns
  the member paths; each raises that module's `Stop` on an unreadable input; `ROOT` is the repository root. Importing the
  module runs `use_utf8_output()` and nothing else (its `main()` is guarded by `__main__`).
- **FACT — the ruling record**: 7,763 bytes at the rulings folder's listing and at its staging result; first line
  `# Rulings — the L3 outgoing-population sitting, 2026-10-17`.
- **FACT — handoff entry 421**: 4,875 bytes at the handoff folder's listing and at its staging result.
- **FACT — `STATUS.md`** holds, above the two 2026-09-02 entries, exactly two entries of the previous batch
  (`cc_instruction_l3_derivation_commit_2026_10_17.md`): its close entry, carrying the `Last updated:` prefix, and one
  `Same dispatch` entry, for its Task 0.
- **FACT — `tools/audit/gen_status_batch_bound.py`'s authored constants now** (read at the file): `BASE_COMMIT =
  "96a24b01b87b94ce157ff471946e38c664d6f844"`, `PREVIOUS_BATCH_DISPATCH =
  "cc_instruction_l3_brief_landing_2026_10_17.md"`, `ACT_DATE = "2026-10-17"`, `DISPATCH =
  "cc_instruction_l3_derivation_commit_2026_10_17.md"`, `TASK = "Task 1"`, `MOVE_KIND = "ordinary"`.

- **ASSUMPTION A1 — the working tree, by content.** Expected tracked modifications at boot: only the line-ending-only
  marking of `tools/audit/claude_md_finer_archive.json` the last reports record (re-establish it with `git hash-object`
  against the tip's blob; leave it untouched; never stage it). Expected untracked: this dispatch, the ruling record,
  entry 421, entry 422 if it exists, and the standing population the previous report's A1 lists (`Claude outputs/`,
  `Codex research inventory/`, two files under `external resarch summary/`, `docs/research_papers/polyph9-release/`,
  the `scratch_artifacts/` population, `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`). Any other
  tracked modification at boot or during the run is a STOP-and-report, except a path this batch writes, after the act
  that writes it and until its commit. A further untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md`
  appearing during the run is the writing side's, NOT landed and NOT a STOP. **Check (Task 0, first act):** per tracked
  input this batch edits (`STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`,
  `tools/audit/status_batch_bound.json`, `records/cowork/handoff/cowork_away_returns.md`)
  `git diff --stat 79499c21ec70bcf5e0a817050ade5bc1268d6a51 -- <path>; echo "exit:$?"`, expected empty; per path of
  Task 0's list `git ls-files --others --exclude-standard -- <path>; echo "exit:$?"`; the whole tracked population with
  `tools/audit/changed_paths.py`.
- **ASSUMPTION A2 — the guard run before the first edit:** failing exactly the thirteen above, **and
  `gen_evidence_pin_membership.py --check` is expected red as well**, because a new ruling record is untracked at boot
  and that tool lists the rulings folder of the working tree (`os.listdir` of `records/cowork/rulings`, read at the tool
  by this writing side). Record it, regenerate nothing before the Task 0 commit, and handle it at Task 2(d).
  **Predicted at the end state:** run 81; failing exactly the thirteen. Reds this batch's own acts may cause, classed by
  cause and NOT a STOP: `gen_evidence_pin_membership.py --check` (the ruling record landed); `gen_l0_l1_outgoing_population.py
  --check` and `gen_defense_share.py --check` if Task 2's `STATUS.md` entries move their inputs. **`tools/audit/gen_l2_outgoing_population.py`
  is a HISTORICAL RECORD in the guard runner (`guard_state.json` → `historical_records`): re-deriving it would renumber
  the members the L2 records cite. It is NOT run and NOT regenerated by this batch, in any mode, and its artifact is not
  touched; `gen_session_start_read_size.py --check` if regenerated before the last `STATUS.md` edit;
  `gen_guard_state.py`'s own artifact until the end-state run. Each is handled at Task 2(d). A red outside these is a
  STOP-and-report.
- **ASSUMPTION A3 — byte-unchanged by this batch, verified at the objects after the last commit:** every governing
  document except `STATUS.md` and `STATUS_ARCHIVE.md`; every tool source except the authored aiming of
  `gen_status_batch_bound.py`; every artifact under `tools/audit/` except the new measurement artifact, the forward
  bound's artifact, the guard set's own artifacts and those Task 2(d) regenerates; every ruling record and every handoff
  entry — **except `records/cowork/handoff/cowork_away_returns.md`, which Task 2 appends the close to, and which may
  change only by that appended section**; the records as committed at Task 0; `FRAMEWORK.md`; the blind derivation and
  the L3 brief; every rendered decisions-register file. Any other difference is a STOP-and-report.

## The standing bars, and the commit-and-push discipline

No `src/` edit, no golden, no test changed or run, no build, nothing under `tools/corpus/`, `tools/robust_stop/` or
`tools/dcml/`, **no measurement of the analysis**, **no session booted, no score copied, staged or written, no pack
rendered**. **The blind derivation `cowork_blind_derivation_l3_2026_10_17.md` and the brief `cowork_blind_session_brief_l3.md`
are NOT OPENED** — the comparison-design rulings of 2026-08-24 require the session that compares to read the blind file
first, and this batch must not become a half-reader of it; the measuring script reads only the three prose classes'
files, and if either file is a member of them its hits are counted like any other file's, never read by you. **No
population is derived and nothing is tabulated, compared, dispositioned or graded.** **No tool source edited except the
authored aiming of `gen_status_batch_bound.py`** (its authored inputs, their comments and one appended row of
`PREVIOUS_AIMINGS`; no function); **no new tool is added to the repository** — the measuring script lives in your
session's scratch folder outside the repository, and its text goes into the report. No open-items row created, flipped
or discarded, **no decisions-register entry and no `D-NNN` allocated, nothing written into the suspension file**
(`cowork_register_rule_c_suspension_2026_08_28.md`), no edit to any governing document except `STATUS.md`/`STATUS_ARCHIVE.md`
in Task 2, **no ruling taken, no recommendation, and no position on which words belong in the list.** **Carried, not
chased:** `tools/audit/gen_guard_classification.py`'s STOP (report it whole and carry on);
`tools/audit/claude_md_finer_archive.json` (held back); the untracked `bwv1049_03_presto.mscx` (a score file: left as
found, not opened). **No figure is transcribed from the artifact into the report's prose or into `STATUS.md` (D-431)**;
the sizes and hashes this file states are start-state bars and expected values.

**Commit-and-push per task. Run the FULL guard set BEFORE the first edit (`python tools/audit/gen_guard_state.py
--check`) and again at the end (write mode, committed as the artifact of a real run). After every commit: push, then
read `.git/refs/remotes/origin/master` with the file tools and confirm it names the commit just made.** `origin` is the
fork; `upstream` is not used; never `--force`. Verify every commit at the object by explicit hash. Every shell command
carries `; echo "exit:$?"`. `git status` and `git diff` over the working tree are denied by the armed guard — use the
explicit-hash forms of A1. Write every hash literally in the command: a hash held in a shell variable is denied by the
guard. Plain single-quoted `git commit -m '…'` subjects. Every working-tree read through the file tools (D-253); a
run's output is redirected to a file in your session's scratch folder outside the repository and read with the file
tools. Edit files with your file-editing tool, never by retyping a whole file. The reserved-word rule binds every line
you write.

## The ordered first reads

**(1)** `CLAUDE.md` at its six ruled spans (the membership at its "Build and test commands" block), `STATUS.md` whole,
`DECISIONS.md` whole; rule (a)'s `gating_ids` at `tools/audit/nongating_apparatus_rows.json` →
`★_the_live_gating_answer`. **(2)** Handoff entry 421 whole, and entry 422 whole if it exists; and
`records/cowork/handoff/cowork_away_returns.md` at its last section (the previous batch's close), because Task 2 appends
to that file. **(3)** `cowork_audit_protocol.md`'s dispatch-protocol section. **(4)** The ruling record
`records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md` whole (it is short). **(5)** The
previous batch's dispatch `records/cc/instructions/cc_instruction_l3_derivation_commit_2026_10_17.md` at its Task 1, and
its report `records/cc/reports/cc_report_l3_derivation_commit_2026_10_17.md` at its guard sections and §8.
**(6)** `tools/audit/gen_l0_l1_outgoing_population.py` whole, before Task 1. **(7)**
`tools/audit/gen_status_batch_bound.py` whole at the object
`79499c21ec70bcf5e0a817050ade5bc1268d6a51:tools/audit/gen_status_batch_bound.py` before Task 2.

## Task 0 — land the records, PUSH

To be landed, each as it stands:

1. `records/cc/instructions/cc_instruction_l3_keyword_count_2026_10_17.md` (this dispatch);
2. `records/cowork/rulings/cowork_rulings_2026_10_17_l3_outgoing_population_sitting.md`;
3. `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_one.md`;
4. `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_two.md` — **only if it exists.** No size is
   stated (the restraint paragraph above): report the size you find. If it does not exist, say so and commit the rest.
   **Do not wait for it.**

**Under standing clause P-2 this dispatch is PINNED at Task 0:** `git hash-object -w` it, record the blob and
`git cat-file -s <blob>`, take every later re-read of it from that blob, and prove it unmoved immediately before staging
it.

**The acts, in order:**

**(1)** A1's check, and the guard run before the first edit (A2). Item 1, 2 or 3 absent is a STOP. A path already
tracked and unmodified is reported and not re-landed. Report any other untracked path the enumeration shows under
`records/`, `reading_pass/`, `ratification_surfaces/` or at the repository root — NOT landed, not a STOP.

**(2)** Each size by `git hash-object -w --no-filters <path>; echo "exit:$?"` then `git cat-file -s <that blob>; echo
"exit:$?"`: **the ruling record expected `7763`, entry 421 expected `4875`.** With the file tools, the ruling record's
first line, **expected** `# Rulings — the L3 outgoing-population sitting, 2026-10-17`. Then check the last bytes of every
file of the list: **a trailing NUL byte, or a final line that breaks off mid-word, is a STOP** — name the file and stop;
do not repair it. **Any size different from the one stated, or the first-line check failing, is a STOP.**

**(3)** Commit the paths of the list that exist, by explicit path, never a directory pathspec. Prove the staged set is
exactly those paths before committing. Subject, exactly: `record: the l3 outgoing-population ruling, entries 421-422
and the l3 keyword-count dispatch` (if entry 422 is absent, write `entry 421`). **(4)** PUSH; verify `origin/master` at
the ref file.

**E0:** (2) held; the named paths in one commit; `origin/master` at it; every path accounted for.

## Task 1 — the count

### 1(a) What is measured, in one paragraph

For each drafted word, over every file of the three prose classes: the hit lines inside members of the specification
document set (the population the search will admit), every such hit line published whole with its file and line
number, and the residue counted per word. Then, for the COUNTED-IN-CONTEXT words, which hit lines in the set each adds
that no CORE word already reaches — the figure that shows what including it buys, with the lines that make it up. A
mechanical aid is attached to every hit: whether the word also occurs on that line as a whole word (so a match only
inside a longer word, like `bass` inside a longer word, is visible). **Which sense of a word fired is a reading for the
writing side and the user; this batch does not judge it.**

### 1(b) The draft, authored by the writing side as measurement inputs (not a ruling)

```python
CORE = (
    # the cadence at each phrase end, with its type
    "cadence", "cadential", "plagal", "phrase end",
    # the phrase and section grouping
    "phrase boundary", "phrase grouping", "grouping layer",
    # the chord symbol: root pitch class, quality and bass note
    "chord symbol", "chord-symbol", "chordsymbol", "bass note", "slash chord", "root pitch class", "inversion",
    # the figured bass
    "figured bass", "figured-bass", "thoroughbass", "continuo",
    # the harmonic rhythm
    "harmonic rhythm", "harmonic-rhythm", "harmonicrhythm",
    # the layer's own name in FRAMEWORK.md section 5
    "read-off",
)
COUNTED_IN_CONTEXT = ("phrase", "grouping", "period", "sentence", "bass", "contradiction", "deceptive")
```

*Left out by the writing side, stated so the user sees it: bare `section` (it matches every document's own sections),
bare `figured` (it matches inside "configured"), bare `root` and `quality` (excluded for L2 by Ruling 86), and `fermata`
and `key area` (L1's and L2's vocabulary, already searched for those comparisons; what they relocated to L3 enters
through the transfer list). The user may rule any of them in.*

### 1(c) The measuring script

Write it in your session's scratch folder **outside the repository**, as `l3_keyword_count.py`; its text goes into the
report. It writes exactly one file into the tree.

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

### 1(d) Run it

From the repository root, `python <scratch>/l3_keyword_count.py > <scratch>/l3_kw_out.txt 2>&1; echo "exit:$?"`, then
read the output file with the file tools. **A `STOP:` line or a traceback is a STOP of this batch**: report it whole; do
not edit the script around it, and edit no repository tool. **Exit 0 and the artifact present are E1's first half.**

### 1(e) Checks, each a STOP if it fails

1. The artifact's `per_term` carries all 29 drafted words, each with its `half`.
2. `the_counts.in_set_hit_lines_CORE` ≤ `the_counts.in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT`.
3. The number of distinct `(file, line_number)` pairs in `every_in_set_hit_record` equals
   `the_counts.in_set_hit_lines_CORE_plus_COUNTED_IN_CONTEXT` — count it with a second scratch script reading the
   artifact (its text into the report).
4. Every `file` in `every_in_set_hit_record` is a member of `tools/audit/specification_document_set.json` →
   `the_document_set` (the same second script).

### 1(f) Prove nothing else moved, then commit

Enumerate with `tools/audit/changed_paths.py`. **Expected: one new untracked path,
`tools/audit/l3_keyword_count_measurement.json`, and no tracked modification beyond A1's.** Commit it alone, by explicit
path. Subject, exactly: `audit: the read-only count of the draft l3 keyword list (no population, no ruling)`. PUSH;
verify `origin/master` at the ref file.

**E1:** 1(d) exit 0; 1(e)'s four checks held; the artifact alone in one commit; `origin/master` at it.

## Task 2 — the close

1. **(a) The `STATUS.md` entries.** Write this batch's entries at the top of `STATUS.md`: one pointer entry per task
   that did work — the close entry FIRST, NAMING THIS DISPATCH BY ITS FILE NAME
   (`records/cc/instructions/cc_instruction_l3_keyword_count_2026_10_17.md`), then Task 1's and Task 0's entries below
   it, each saying `Same dispatch`; in the OI-222 pointer convention, the whole of each being your report; no figure
   restated (D-431). The close entry says that the ruling record and entries 421 (and 422) are committed; that the draft
   L3 keyword list was counted read-only and its artifact is `tools/audit/l3_keyword_count_measurement.json`; that the
   words are the writing side's measurement inputs and not a ruling; and that no population was derived, nothing
   tabulated or compared, the derivation and the brief not opened, no `D-NNN` allocated and no open-items row touched —
   or, if a task stopped, which task stopped and that nothing after it was done. **The `Last updated: ` prefix moves
   from the previous batch's close entry to your newest entry.** No other existing sentence of `STATUS.md` is rewritten
   or removed, the forward bound's own declared prefix adjustment excepted.
2. **(b) The forward bound** (read `gen_status_batch_bound.py` whole at the object first, ordered first read (7)).
   Re-aim its authored constants: `BASE_COMMIT` (this batch's Task 1 commit — its last task commit before the close;
   neither task commit carries a `STATUS.md` change, so its `STATUS.md` object is the one both refs carried at boot),
   `PREVIOUS_BATCH_DISPATCH` (`cc_instruction_l3_derivation_commit_2026_10_17.md`), `ACT_DATE` (the day the move runs),
   `DISPATCH` (`cc_instruction_l3_keyword_count_2026_10_17.md`), `TASK` (`Task 2` — this dispatch orders this batch's
   own entries at 2(a) and this move at 2(b) and 2(c), inside its Task 2, which the heading *"Task 2 — the close"* names
   in those words); `MOVE_KIND` stays `ordinary`. Each field's comment re-stated the way every previous re-aiming
   re-stated it — the former value named, not deleted (#12). Append your own aiming to `PREVIOUS_AIMINGS` in the shape
   of the rows above it: `{"executing_act": "cc_instruction_l3_keyword_count_2026_10_17.md, Task 2", "base_commit":
   <the BASE_COMMIT you set>, "the_then_previous_batch": "cc_instruction_l3_derivation_commit_2026_10_17.md",
   "the_kind_of_move": "ordinary"}`. Nothing else is appended and no row is edited.
3. **(c)** Run `gen_status_batch_bound.py --apply`, then `--check`. **Prediction:** it moves **exactly the previous
   batch's two entries** (its close entry, which carries the `Last updated:` prefix, and its one `Same dispatch` entry,
   read at `STATUS.md` by this writing side); the two 2026-09-02 entries stay and are not moved by hand. Do not read a
   green `--check` as proof the bound is met (`OPEN_ITEMS.md` OI-379): report the entries `--apply` actually moved, by
   name. If it STOPs, restore its passing aim, re-run green, report, move nothing by hand.
4. **(d) The regenerations A2 names**, after (a) to (c): for each of `gen_evidence_pin_membership.py`,
   `gen_l0_l1_outgoing_population.py` and `gen_defense_share.py` whose `--check` is red, regenerate it (never
   `gen_l2_outgoing_population.py` — A2), confirm its `--check` green, and compare its artifact with the committed blob by explicit hash.
   **The one member change allowed is the ruling record's addition to the evidence-pin membership; a moved hit record of
   `STATUS.md` in either population artifact is allowed and reported by name. Any other member added, removed or changed
   is a STOP-and-report.** **LAST**, after the final `STATUS.md` edit, regenerate `gen_session_start_read_size.py` and
   confirm its `--check` green. Commit the re-aimed tool, `tools/audit/status_batch_bound.json`, `STATUS.md`,
   `STATUS_ARCHIVE.md`, the regenerated artifacts and the read-size artifact together in the close.
5. **The report**, `records/cc/reports/cc_report_l3_keyword_count_2026_10_17.md`, which decides nothing and recommends
   nothing. Its first section is headed **`THE COUNT, AS TAKEN`** and carries: the script's text; its printed output
   verbatim with its exit code; the second script's text and output; 1(e)'s four checks each graded; and a pointer to
   the artifact's `per_term` and `what_each_COUNTED_IN_CONTEXT_word_adds_beyond_CORE` — **no per-word figure in prose
   (D-431).** Then: Task 0's sizes and first-line check; both guard states; every commit hash; E0, E1 and E2 and A1 to
   A3 graded; the forward bound's aiming, `--apply` and `--check` with the entries moved by name; every regeneration and
   the members it changed; declared departures; and the plan's tell in one sentence — did this batch produce anything
   other than the landed paths, the one artifact, the close's files and the report? If yes, name it.
6. **The full close appended to `records/cowork/handoff/cowork_away_returns.md`** as a section headed **THE DRAFT L3
   KEYWORD LIST COUNTED: ONE READ-ONLY ARTIFACT, THE RULING RECORD AND ITS ENTRIES IN GIT — NO POPULATION, NO RULING, NO
   ALGORITHM CHANGED** (if a task stopped, the heading says which, and says what was not done) — the report's content as
   pointers, and the plan line: **the next act is the writing side's — the check of this batch's return at the objects;
   then the L3 keyword list's membership, put to the user as its own decision on the counted facts; then the population
   dispatch.**
7. **The close does not assert the end state**; one further commit carries it. Commit the close, push, verify; then the
   full guard run in write mode at that tree, the A2 exceptions handled as A2 says, and the one further commit with its
   artifacts, pushed and verified. Re-run `gen_guard_classification.py --check` after it and report the message (a
   change in that message is reported, not a STOP).

**E2:** at the tree carrying the close, a fresh full guard run — the A2 prediction — committed only after the run that
produced it.

**THIS BATCH ENDS HERE.**

## What this batch does NOT do

- **No outgoing population derived, nothing tabulated, compared, dispositioned or graded.**
- **No position on which words belong in the list; no word's sense judged.**
- **The derivation and the brief not opened; no session booted, no score staged or copied, no pack rendered.**
- **No new repository tool; no tool source edited but the forward bound's aiming.**
- **No change to what any layer computes** as its specification defines it; **no documentation amended.**
- **No decisions-register entry, no `D-NNN`, nothing in the suspension file, no ruling taken, nothing put to the user.**

## What this batch deliberately leaves to later acts, named so it is not lost

- **The L3 keyword list's membership** — the user's own decision, put by a Cowork session on this count (Option B item 3).
- **The L3 population dispatch**, written only after that ruling (Option B item 3; D-250).
- **The five questions the derivation marks for the user** (OQ-L3-2, 3, 6, 8 and 10) — not put before the comparison,
  a reading on the L2 precedent carried by entries 420 and 421.
- **The `docs/research_papers/BIBLIOGRAPHY.md` path at line 2234 of the L2 input-contract copy**; **row 39's
  second-extract finding on the L3 charter's "from the harmony"**; **the untracked `bwv1049_03_presto.mscx`** — carried
  by entries 410 to 421, not acted on.

## The writing side's self-check, run before release (D-434)

1. *Principles.* #6 — the count uses the population tool's own matcher and loaders by import, so there is no second
   matcher to disagree with the one the population run will use. #12 — every in-set hit line is published whole; nothing
   is dropped from the set's hits. #19/#24 — the artifact states its own bound (a lower bound, never a census; residue
   counted only). D-431 — every figure lands in the artifact and is cited, never transcribed.
2. *Conventions.* American English; *decisions-register*, *open-items* qualified; *check*, *script*, *measurement*,
   never *instrument*; *score* only for the music; *bass*, *phrase*, *period*, *section* used in this file only for the
   music or as quoted search words, *section* otherwise qualified as a document's.
3. *The bars.* No population; no tabulation; no ruling; no recommendation; the derivation not opened; the records landed
   as they stand; every commit pushed.
4. *Documentation and algorithm.* Nothing here changes the algorithm or amends documentation. The currently decided
   method for L3 is `FRAMEWORK.md` §5's L3 block with DP-I.

*Provenance: Cowork writing side, 2026-10-17 (Stockholm), the sitting booted on
`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twenty_one.md`, at tip
`79499c21ec70bcf5e0a817050ade5bc1268d6a51` read as files; no shell command was run. **Read by this writing side, at the
extent named:** the boot read of entry 291 §4 step 3; entries 291, 420 and 421 whole; the 2026-10-17 ruling record whole;
§3am, §3an, §3cl and §3co of the 2026-08-31 record whole; the 2026-09-27 L2 outgoing-population ruling record whole; the
2026-10-14 L3 withheld-family ruling record whole; `FRAMEWORK.md` at §5's L3 block and the boundary contracts, and its
heading list; the L2 keyword-count dispatch and the L2 outgoing-population dispatch whole; the previous dispatch
`cc_instruction_l3_derivation_commit_2026_10_17.md` whole; its report by search for its guard and regeneration lines;
`tools/audit/gen_l0_l1_outgoing_population.py` whole; `tools/audit/gen_status_batch_bound.py` at its six authored
constants by search; `tools/audit/guard_state.json` at `summary` and its `failing_tools` list; both ref files; and, at
the check below, `gen_evidence_pin_membership.py` by search, `guard_state.json` at `historical_records`,
`specification_document_set.json` at its 26 `member` lines and `artifact_inventory.json` at its class headings and the
26 members' `path` lines. **NOT read:** `gen_l2_outgoing_population.py`; `cowork_audit_protocol.md`; the rows of
`PREVIOUS_AIMINGS`.*

## This file's check at its sources (D-434; run 2026-10-17 in a turn of its own, after the user's "continue")

Scope: completeness, coherence, correctness and absolutes, over this file as first landed (39,269 bytes at its staging
result) against the objects named.

**Confirmed at the objects:** both ref files read `79499c21…`; the guard summary (81 / 68 / 13) and its thirteen failing
tools; the ruling record's size (7,763) and first line; entry 421's size (4,875); the two previous-batch entries at the
head of `STATUS.md` above the two 2026-09-02 entries; the forward bound's six authored constants; `search_terms`,
`load_classes`, `load_specification_document_set`, `read_text`, `SEARCH_CLASSES`, `ROOT` and `Stop` in
`gen_l0_l1_outgoing_population.py`, and that its `main()` is guarded; the specification set's 26 members; **all 26
members carry a `path` entry in the inventory inside the three searched classes** (`ARCHITECTURE.md` in
`governing-documents`, twenty-three in `writing-side-design-documents`, `docs/llm_integration.md` and
`docs/scoring_model.md` in `documentation-directory-prose`); the draft's lengths, 22 and 7, with no word twice.

**Corrected at their sites (#12 — the former wordings are kept here):**
(1) **A guard tool this file ordered regenerated is a HISTORICAL RECORD that must not be re-derived.**
`gen_l2_outgoing_population.py` sits in `guard_state.json` → `historical_records`: re-deriving it renumbers the members
the L2 records cite. A2 and Task 2(d) named it among the tools to regenerate if red; it is now barred in both places.
*Former (A2):* "`gen_l0_l1_outgoing_population.py --check`, `gen_l2_outgoing_population.py --check` and
`gen_defense_share.py --check` if Task 2's `STATUS.md` entries move their inputs;" *Former (2(d)):* "for each of
`gen_evidence_pin_membership.py`, `gen_l0_l1_outgoing_population.py`, `gen_l2_outgoing_population.py` and
`gen_defense_share.py` whose `--check` is red, regenerate it,"
(2) The evidence-pin guard's red was stated as possible, its ground unchecked; the tool lists the working-tree rulings
folder, so it is now stated as expected. *Former:* "**except that `gen_evidence_pin_membership.py --check` may also be
red**, because a new ruling record is untracked at boot (the previous report's §5 grounds its green on there being none;
whether that tool reads untracked files was not checked by this writing side). If it is red: record it,"
(3) "the matcher the population search itself will use" claimed a fact about a dispatch not yet written. *Former:*
"with the matcher the population search itself will use, and publishes".
(4) A specification set member not searched was only listed; a missing member would have under-counted silently against
#12. The script now STOPs on it, and its bound text says so. *Former (script):* `set_members_not_searched =
sorted(spec_set - searched)`; *former (bound):* "A set member outside the searched classes is listed above and not
searched here."
(5) The provenance's NOT-read line named three objects this check then read. *Former:* "**NOT read:**
`gen_evidence_pin_membership.py` (whether it reads untracked files); `gen_l2_outgoing_population.py`;
`tools/audit/artifact_inventory.json` and `specification_document_set.json` (whether every set member lies in the
searched classes — the script lists any that do not); `cowork_audit_protocol.md`; the rows of `PREVIOUS_AIMINGS`."

**Absolutes swept:** *exactly*, *every*, *never*, *nothing*, *no* — each is an order or bar on the executing side, or a
count read at its object above. *"the one file the writing side writes"* (restraint) and *"exactly the previous batch's
two entries"* (prediction) were read at their objects. **Bound:** the script was traced by reading, not run;
`gen_l2_outgoing_population.py` and `cowork_audit_protocol.md` were not read; no task was widened by this check except
the STOP added at (4) and the bar added at (1).
