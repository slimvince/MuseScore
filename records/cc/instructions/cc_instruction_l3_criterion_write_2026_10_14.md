# CC dispatch — the L3 CRITERION WRITE: land the records since the tip, write L3's ruled candidate criterion into the boot-pack generator, clear the two guard reds the L2 ratification application left, correct the slice derivation and record row 36's progress — NO verdict, NOTHING withheld, NO pack, NO algorithm change, NO register entry, NO session booted

> **★★ RELEASED 2026-10-14** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_seven.md`, which wrote it, after the user's
> ruling "C" and after the check at the sources recorded at the end of this file. It is executed by Claude Code when
> the user hands it over (D-252); the Cowork writing side never runs it. *(The banner this replaces read, preserved
> (#12): "**★★ DRAFT UNDER CONSTRUCTION BY THE COWORK WRITING SIDE — NOT TO BE HANDED TO CLAUDE CODE.** … Claude
> Code: if you are reading this banner, STOP at once, do nothing, and report that you were handed an unfinished
> draft.")*

## What this batch is, in plain words

On 2026-10-14 the user ruled that L3 (the read-off facts) is the next layer whose detail specification is derived,
that the fresh session deriving it will be given a boot pack with a **withheld family** (the ratified decisions
that state L3's answers, left out so its derived answer can be told apart from recall), and that **every
design-intent entry of the rulings sort is a candidate** for that family. This batch writes that candidate rule
into the generator's table, proves with the generator's own matcher that it reaches every design-intent entry, and
changes nothing else in the generator. It also clears the two guard checks the last batch left failing — one by a
ruling of the user's, one by re-aiming stale references — corrects one count in the slice derivation, records row
36's reading progress, and lands every record written since the tip. **Nothing here changes the algorithm as any
specification defines it.**

## Words used in this dispatch, explained first

- **Boot pack** — the set of files given to a fresh deriving session; built by `tools/audit/gen_derivation_boot_pack.py`.
- **Withheld family** — the register entries left out of a boot pack. Each candidate gets an authored verdict IN
  (withheld), OUT (admitted) or UNPLACED. **This batch authors none.**
- **Candidate criterion** — the generator's `CRITERION[<subject>]` entry: which design-intent entries become
  candidates. Its terms: `groups`, `home_documents`, `architecture_spans`, `keywords`, `always`.
- **Design-intent entry** — an entry of `tools/audit/rulings_sort_classification.json` whose `proposed_class` is
  `DESIGN-INTENT`.
- **Guard set** — the `--check`/`--verify` runs `tools/audit/gen_guard_state.py` performs and records in
  `tools/audit/guard_state.json`. **A red** is a member that fails.
- **Historical record** — a guard-set member moved to `gen_guard_state.HISTORICAL`: its artifact stays on disk as
  committed and the tool is no longer run.

## The ruling ledger — what each record orders, and which task writes it

| | Record (in `records/cowork/rulings/`) | What it orders | Task |
|---|---|---|---|
| L.1 | `cowork_rulings_2026_10_14_next_subject_sitting.md` | L3 is the next subject. Lands only. | 0 |
| L.2 | `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md` | Ruling 1: L3's pack carries a withheld family. Ruling 2: every design-intent entry is a candidate; *"How the whole-population cut is expressed in `tools/audit/gen_derivation_boot_pack.py` is the dispatch's business"*. | 1, 2 |
| L.3 | `cowork_rulings_2026_10_14_l2_outgoing_population_check_sitting.md` | Ruling 1: `gen_l2_outgoing_population.py` becomes a historical record, after the reader enumeration. §2: the second red is stale references, fixed. | 3 |

Handoff entries 394 §2 and 395 §3 order the slice derivation's correction and row 36's progress update (Task 4).
The user's standing rule: **every commit is pushed, and the push is verified at `.git/refs/remotes/origin/master`.**

## Premise ledger (written 2026-10-14 by the writing side from staged copies read with the file tools; no git command was run by the writing side, so every identity only a git query gives is UNSETTLED and is yours to take)

- **FACT — the tip.** `.git/HEAD` → `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both `b6bceef7009f92e89a97c8a79465e5e462e1f49a`, read 2026-10-14.
  **Re-read both yourself before Task 0.**
- **FACT — the guard start state, at the working-tree `tools/audit/guard_state.json` → `summary`:** run 80, passing
  64, **failing 16**, not run 4, historical 19. The sixteen: `gen_phase3_gate_partition.py --check`,
  `gen_filing_convention_application.py --check`, `gen_artifact_inventory.py --check`,
  `gen_artifact_inventory_surface.py --check`, `gen_test_construction_evidence.py --check`,
  `gen_retirement_caller_check.py --check`, `decisions/apply_soft_discard.py --check`,
  `decisions/apply_residue_discard.py --check`, `decisions/gen_retired_subject_moves.py --check`,
  `gen_epoch_write_path.py --check`, `gen_derivation_boot_pack.py --check`,
  `gen_recognizer_establishment_sort.py --check`, `gen_l2_outgoing_population.py --check`,
  `decisions/gen_cluster_dispositions.py --verify`, `decisions/gen_home_classification.py --check`,
  `decisions/gen_phase1p_delegation_bar.py --check`. The classification tool `gen_guard_classification.py` reports
  a standing four-name STOP for tools with no authored verdict (`records/cc/reports/cc_report_l2_ratification_application_2026_10_14.md`
  §2). **UNSETTLED: whether that copy is the tip's blob** — your start-state run measures the tip.
- **FACT — `gen_derivation_boot_pack.py --check` IS ALREADY RED.** So inertness of Task 1's edit is proven by its
  output being **byte-identical before and after the edit**, not by exit 0.
- **FACT — the generator** (`tools/audit/gen_derivation_boot_pack.py`, 514,922 bytes at its staging): `KEYWORDS`
  (eighteen terms) at the line opening `KEYWORDS = (`; `L2_KEYWORDS = KEYWORDS + (` (forty-two); `CRITERION` with
  the keys `harmony-boundary`, `scoring-model`, `l0-l1`, `l2`, the `l2` entry closing with
  `        "keywords": L2_KEYWORDS,` / `        "always": (),` / `    },` and the table closing with `}` on the
  next line; `WITHHELD` and `VERDICTS` each carry an `l2` key; **the string `"l3"` occurs nowhere in the file**
  (search, 2026-10-14).
  `candidates()` matches a group term by `e.get("group") in spec["groups"]` and glosses each group match with
  `group_title()`, which STOPs on a group with no title in the backbone's `groups` table.
- **FACT — the population.** `tools/audit/rulings_sort_classification.json` (586,541 bytes): 411 lines carry a
  `"group": "<letter>"` field and 244 carry `"proposed_class": "DESIGN-INTENT"` (counts by search, not by parse —
  **Task 2's tool count is the proof**). No entry carries group P, R or V–Z. The backbone's `groups` table
  (`tools/audit/decisions/backbone_decisions.json`, `"groups": [`) carries **twenty** ids: A B C D E F G H I J K L
  M N O P Q S T U.
- **FACT — the second red's cause, at the objects.** In `tools/audit/decisions/backbone_decisions.json` →
  `section_home_criterion` → `documents` → `"cowork_confidence_contract.md"` → `section_kind`, the authored
  judgments record `"heading_line": 23, "heading_text": "2. Definitions — the two admissible confidence classes"`
  and `"heading_line": 63, "heading_text": "4. The comparison frames (the §8 override arithmetic, stated once)"`.
  At `cowork_confidence_contract.md` as it stands, line 23 is `## 2. Definitions — the three admissible confidence
  classes` and §4's heading is at **line 81**. `gen_home_classification.classify()` raises on either mismatch, and
  `gen_retired_subject_moves.py` runs `classify()` through `derive_kind_moves()`. The last batch's Task 3 inserted
  eighteen lines inside §2, so the register's `home` anchors **D-268 `:36-48`, D-269 `:83-85` and D-601 `:89-101`**
  now stand eighteen lines early (their quoted passages read at lines 54, 101 and 107 of the contract); **D-267
  `:25-34` is unmoved.** The sanctioned tool for drifted anchors is `tools/audit/decisions/reaim_home_anchors.py`,
  which writes the quote checker's own reported start lines and touches only the line part of `home`.
- **FACT — the first red's mechanism.** `gen_guard_state.HISTORICAL` is a dict of tool path → reason;
  `gen_guard_classification.VERDICTS` is a dict of tool path → `(verdict, evidence, reason)`, and its build STOPs
  if the set of `POINT` verdicts differs from `HISTORICAL`'s keys. Precedent shape: `gen_phase1_finish_line.py`
  keeps its `AUTHORED` entry in `gen_guard_state.py` and has an entry in both tables. **No verdict for
  `gen_l2_outgoing_population.py` exists in `gen_guard_classification.py`** (search). **UNSETTLED: whether it is
  one of the four names of the standing STOP.**
- **FACT — the documentation sites (Task 4).** `cowork_l2_task_b_slice_derivation_2026_09_05.md` (repository
  root, 15,039 bytes): §4 row 36 ends `**The one L3 row.** |`; §5 carries `- **L3's slice: 1 row** — 36.`.
  `reading_pass/candidacy_upgrades.md` (39,674 bytes): its last section before the closing `---` and provenance
  ends with the line `**Not read: the whole of Task B outside this slice — the L2 and L3 groups, in the order this file`
  / `proposes, headed by L2's entangled decision. The remainder is untouched.**`.
- **FACT — the untracked population Task 0 lands**, from the folder listings of 2026-10-14 (modification time
  later than the ref file's): in `records/cowork/rulings/`, exactly the three records of the ledger; in
  `records/cowork/handoff/`, entries 393 to 397 (398 is written by the writing side at its close); in
  `reading_pass/extracts/`, row 36's first extract; in `ratification_surfaces/`, none.
  `records/cc/instructions/` was not listed by the writing side.

- **ASSUMPTION A1 — the working tree, by content.** Tracked modifications at boot: **none expected**, except the
  line-ending-only marking of `tools/audit/claude_md_finer_archive.json` the last report §3 records (content
  equal to the tip's blob, a relay — establish it again; leave it untouched, never stage it). Any other tracked modification, at boot or during
  the run, is a STOP-and-report, except a path this batch writes, after the task that writes it and until its
  commit. A further untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` appearing during the run is the
  writing side's and is NOT landed and NOT a STOP. **Check (Task 0, first act):** per tracked input this batch
  edits (`tools/audit/gen_derivation_boot_pack.py`, `tools/audit/gen_guard_state.py`,
  `tools/audit/gen_guard_classification.py`, `tools/audit/decisions/backbone_decisions.json`,
  `cowork_l2_task_b_slice_derivation_2026_09_05.md`, `reading_pass/candidacy_upgrades.md`, `STATUS.md`,
  `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`) `git diff --stat b6bceef7009f92e89a97c8a79465e5e462e1f49a -- <path>; echo "exit:$?"`;
  per path of Task 0's list `git ls-files --others --exclude-standard -- <path>; echo "exit:$?"`; the whole tracked
  population with `tools/audit/changed_paths.py`.
- **ASSUMPTION A2 — the guard run before the first edit:** the sixteen named above, exactly, and the
  classification tool's standing STOP. **Predicted at the end state:** population 79 run, historical 20, not run 4;
  failing set the sixteen **less** `decisions/gen_retired_subject_moves.py` (cleared by Task 3(ii)) **less**
  `gen_l2_outgoing_population.py` (no longer run) — fourteen. Reds this batch's own acts may cause, classed by cause
  and NOT a STOP: `gen_l0_l1_outgoing_population.py --check` and `gen_defense_share.py --check` if Task 5's
  `STATUS.md` entries move their inputs — regenerate, compare field by field against the committed blob, commit
  with the end state, report that no member moved (a member moving IS a STOP-and-report);
  `gen_session_start_read_size.py --check` if regenerated before the last `STATUS.md` edit. The OUTPUT of the
  already-red `gen_home_classification.py --check` and `gen_cluster_dispositions.py --verify` may change by Task
  3(ii) — report the before and after text; it is not a STOP. A red outside these is a STOP-and-report.
- **ASSUMPTION A3 — `tools/audit/evidence_pin_membership.json`** regenerated at Task 0 grows its list of ruling
  records read by exactly the three records Task 0 lands, and moves nothing else (the last report §2 and §3 measured
  that mechanism). **Measure before accepting**; any other movement is a STOP-and-report.
- **ASSUMPTION A4 — byte-unchanged by this batch, verified at the objects after the last commit:** every governing
  document except `STATUS.md` and `STATUS_ARCHIVE.md`; the generator except the one insertion of Task 1; the two
  guard tools except the two insertions of Task 3(i); the backbone except the two values of Task 3(ii)(a) and the
  three `home` anchors of Task 3(ii)(b); the slice derivation and `candidacy_upgrades.md` except Task 4's two
  replacements and one insertion; `tools/audit/l2_outgoing_population.json`; everything under
  `tools/audit/derivation_boot_pack/` and `tools/audit/derivation_boot_pack.json`; every ruling record, surface,
  extract and the suspension file. Any other difference is a STOP-and-report.

## The standing bars, and the commit-and-push discipline

No `src/` edit, no golden, no test changed or run, no build, nothing under `tools/corpus/` or
`tools/robust_stop/`, **no measurement of the analysis built, designed, scoped or run**, no derivation of any
specification statement, **NO SESSION BOOTED, no pack rendered** (`write_all` is never reached: the only
generator mode you run is `--check`), **no verdict authored for any subject, no `WITHHELD`, `VERDICTS`, `EXTRAS` or
`FROZEN` entry for `l3`, no edit to the `KEYWORDS` or `L2_KEYWORDS` tuples or to any existing `CRITERION` entry**,
no open-items row created, flipped or discarded except an apparatus-finding row under rule (c), **no
decisions-register entry and no `D-NNN` allocated, nothing written into the suspension file, no edit to any entry's
`title`, `verbatim`, `plain`, `patterns`, `rationale` or `status_source`**, no edit to any governing document except
`STATUS.md`/`STATUS_ARCHIVE.md` in Task 5, **no ruling taken, no position weighed, no recommendation anywhere.**

**Commit-and-push per task. Run the FULL guard set BEFORE the first edit (`python tools/audit/gen_guard_state.py
--check`) and again at the end (write mode, committed as the artifact of a real run). After every commit: push,
then read `.git/refs/remotes/origin/master` with the file tools and confirm it names the commit just made.**
Verify every commit at the object by explicit hash. Every shell command carries `; echo "exit:$?"`. `git status`
and `git diff` over the working tree are denied by the armed guard — use the explicit-hash forms of A1. Plain
single-quoted `git commit -m '…'` subjects. Every working-tree read through the file tools (D-253); a run's output
is redirected to a file under `%TEMP%` and read with the file tools. Edit files with your file-editing tool, never
by retyping a whole file. **If an old text quoted below does not occur EXACTLY ONCE in its file, that edit is a
STOP-and-report for that edit alone**: make nothing for it, report what you found, apply the rest. The
reserved-word rule binds every line you write.

## The ordered first reads

**(1)** The three records of the ledger, each WHOLE. **(2)** `CLAUDE.md` at its six ruled spans (the membership at
its "Build and test commands" block), `STATUS.md` whole, `DECISIONS.md` whole, `BUILD_AND_TEST.md` in full; rule
(a)'s `gating_ids` at `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`. **(3)**
`records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_seven.md` and entries 393 to 396 whole, and
`…three_hundred_and_ninety_eight.md` whole if present at boot (the current entry point; absent is reported, not a
STOP). **(4)** `cowork_audit_protocol.md`'s dispatch-protocol section in full. **(5)** The model,
`records/cc/instructions/cc_instruction_l2_criterion_write_2026_09_04.md`, whole; the last batch's dispatch
`records/cc/instructions/cc_instruction_l2_ratification_application_2026_10_14.md` at its premise ledger, Task 0 and
Task 4, its report `records/cc/reports/cc_report_l2_ratification_application_2026_10_14.md` whole, and its close in
`records/cowork/handoff/cowork_away_returns.md` (the last section). **(6)** The generator at `KEYWORDS`,
`L2_KEYWORDS`, `CRITERION`, `group_title()`, `candidates()`, `criterion_is_empty()`, `criterion_block()`, `build()`
and `main()`. **(7)** `tools/audit/gen_guard_state.py` at `AUTHORED`'s `gen_l2_outgoing_population.py` entry and
the whole `HISTORICAL` table with the comment above it; `tools/audit/gen_guard_classification.py` at `VERDICTS`'s
opening and its historical entries, and at `build()`'s STOPs. **(8)** `tools/audit/decisions/gen_home_classification.py`
at `classify()`; `tools/audit/decisions/reaim_home_anchors.py` whole; `tools/audit/decisions/gen_retired_subject_moves.py`
whole. **(9)** `tools/audit/gen_status_batch_bound.py` whole at the object
`b6bceef7009f92e89a97c8a79465e5e462e1f49a:tools/audit/gen_status_batch_bound.py` before Task 5.

## Task 0 — land the records, the extract, the entries and this dispatch, and PUSH

To be landed (the standing clause): every record written since `b6bceef7…`, and this dispatch. **Each path's
standing at the tip is yours to take under A1** (expected: every path UNTRACKED):

1. **Three ruling records**, `records/cowork/rulings/`: `cowork_rulings_2026_10_14_next_subject_sitting.md`,
   `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`,
   `cowork_rulings_2026_10_14_l2_outgoing_population_check_sitting.md`.
2. **Row 36's first extract**, `reading_pass/extracts/ju-margot-mckay-dahn-fujinaga-2020-automatic-figured-bass-annotation-bach-chorales-figured-bass-dataset.md`.
3. **The handoff entries**, `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_three.md` to
   `…three_hundred_and_ninety_eight.md` — six files (398 is written by the writing side at its close; if it is
   absent at boot, land 393 to 397 and report the absence, not a STOP).
4. **This dispatch**, `records/cc/instructions/cc_instruction_l3_criterion_write_2026_10_14.md`.

**The acts, in order:** **(1)** A1's check. A path already tracked is reported and not re-landed; a path that does
not exist is a STOP-and-report for that path, the rest landed. Report any other untracked path the enumeration
shows under `records/`, `reading_pass/` or `ratification_surfaces/` — NOT landed, not a STOP. **(2)** Regenerate
`tools/audit/evidence_pin_membership.json` and measure it against the committed blob, against A3. **(3)** Commit
exactly the paths of items 1 to 4 that exist and are untracked, plus `tools/audit/evidence_pin_membership.json`
only if it moved. Subject, exactly:
`record: the three 2026-10-14 ruling records, row 36's first extract and entries 393 to 398 landed with the L3 criterion-write dispatch`
(if entry 398 is absent, the subject names 393 to 397). **(4)** PUSH; verify `origin/master` at the ref file.

**Under standing clause P-2 this dispatch is PINNED at Task 0:** record its blob, and prove it unmoved immediately
before staging it.

**E0:** the named paths in one commit; `origin/master` at the commit; A3 measured; every path of items 1 to 4
accounted for as landed, already tracked or absent.

## Task 1 — the edit: `CRITERION["l3"]`

**(a) Before the edit**, run and keep the output:

```
cd C:\s\MS && python tools/audit/gen_derivation_boot_pack.py --check > %TEMP%\dbp_before.txt 2>&1; echo "exit:$?"
```

**(b) The edit — one pure insertion into `tools/audit/gen_derivation_boot_pack.py`, nothing else in the file
changes.** Old text (must occur exactly once):

```python
        "keywords": L2_KEYWORDS,
        "always": (),
    },
}
```

New text — the same four lines with the `l3` block inserted between `    },` and `}`:

```python
        "keywords": L2_KEYWORDS,
        "always": (),
    },
    # ── L3, the deriving subject after L2 (the next-subject ruling of 2026-10-14) ────────────────
    # DORMANT BY DESIGN, AND THE DORMANCY IS DECLARED WITH ITS CONSUMER NAMED (the
    # fact-publication corollary).  NOTHING REACHES THIS ENTRY TODAY: `build()` iterates `WITHHELD`,
    # and no `l3` withheld family is authored, because L3's verdicts are ruled list by list at Cowork
    # decision surfaces and no list exists yet.  Its consumer is `build_subject("l3", ...)`, which
    # runs when that family lands — a separate act, not this one.
    #
    # THE RULINGS, both in `records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`:
    #   Ruling 1 — L3's boot pack carries a withheld family.
    #   Ruling 2 — L3's candidate criterion "reaches the whole design-intent class" of
    #              `tools/audit/rulings_sort_classification.json`; how the cut is expressed here is the
    #              dispatch's business, and Ruling 88 of the 2026-08-31 record's note — a NAMING catches
    #              later entries where a word list does not — applies to the choice.
    #
    # HOW THE WHOLE CLASS IS EXPRESSED, and why no tool code changed: `groups` names EVERY group of
    # the decisions register's own `groups` table (the backbone's, twenty ids, P among them though
    # no sort entry carries it today), so every design-intent entry of a registered group matches
    # the group term, and an entry added later to any of them is caught by the naming.  The other
    # four terms are EMPTY: a word list or a document list would only re-pick entries the group
    # term already holds.  If the register ever gains a group, this tuple must gain it in the same
    # act — the check artifact named below compares the two.
    #
    # WHAT THIS TABLE PICKS is proved at `tools/audit/l3_criterion_written_check.json`, the
    # generator's own `candidates()` over this entry; no figure is restated here (D-431).
    # THE BOUND (#24, D-661): the population is the sort artifact's, NOT the decisions register's
    # whole membership; register entries outside the sort are out of every term's reach.
    "l3": {
        "groups": ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                   "Q", "S", "T", "U"),
        "home_documents": (),
        "architecture_spans": (),
        "keywords": (),
        "always": (),
    },
}
```

**(c) Re-read with the file tools after the edit:** `KEYWORDS` and `L2_KEYWORDS` byte-for-byte unchanged; the four
existing `CRITERION` entries byte-for-byte unchanged.

**(d) After the edit**, the same command to `%TEMP%\dbp_after.txt`. **The two outputs and the two exit codes must
be identical** (read both files whole with the file tools and compare). Any difference is a STOP-and-report:
restore the generator by explicit hash and stop the batch.

**One finding, recorded and NOT repaired by this batch:** `criterion_block()`'s non-empty branch renders the fixed
bullet *"its `group` is E — Layer 2, the slicer"* into every subject's manifest whatever its groups. It is false
for `l2` (whose manifest is already rendered) and would be false for `l3`. Inert for `l3` today (no `l3` pack is
built); owed before an `l3` pack is rendered. Report it as found, inert for `l3`, unrepaired, owed.

## Task 2 — prove at the tool's own matcher that the table was written as ruled

**(a)** Write the script **outside the repository**, at `%TEMP%\l3_criterion_written_check.py`. It never calls
`build()`, `write_all()` or `check_all()`, injects nothing, and writes exactly one file into the tree:
`tools/audit/l3_criterion_written_check.json`.

**(b) The script:**

```python
# READ-ONLY CHECK. Imports the generator and calls its own candidate derivation over the COMMITTED
# criterion table. It injects nothing and never calls build(), write_all() or check_all().
import json, os, importlib.util

HERE = r"C:\s\MS\tools\audit"
spec = importlib.util.spec_from_file_location(
    "gen_dbp", os.path.join(HERE, "gen_derivation_boot_pack.py"))
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)          # main() is guarded by __main__, so this renders nothing

PILOT_EIGHTEEN = (
    "slice", "slicing", "segment", "segmentation", "boundary", "boundaries", "change-point",
    "onset", "release", "harmonic rhythm", "where one chord ends", "finest grain", "grain",
    "atomic", "sounding", "struck", "priority of evidence", "evidence ranking",
)
UNCHECKED_BY_THE_RULING = ("D-584", "D-478", "D-526")
fail = []


def check(name, ok, saw):
    if not ok:
        fail.append({"check": name, "saw": saw})
    return {"check": name, "passed": bool(ok), "saw": saw}


sort = gen.read_json(gen.SORT)
bb_data = gen.read_json(gen.BACKBONE)
backbone = {d["id"]: d for d in bb_data.get("decisions", [])}
for r in bb_data.get("retired_entries", {}).get("entries", []):
    e = r.get("the_entry", {})
    if e.get("id") and e["id"] not in backbone:
        backbone[e["id"]] = e
REGISTER_GROUPS = tuple(g["id"] for g in bb_data.get("groups", []) if g.get("id"))

spec_l3 = gen.CRITERION["l3"]
shape = [
    check("KEYWORDS is still the pilot's eighteen", tuple(gen.KEYWORDS) == PILOT_EIGHTEEN,
          len(gen.KEYWORDS)),
    check("L2_KEYWORDS still carries forty-two terms", len(gen.L2_KEYWORDS) == 42, len(gen.L2_KEYWORDS)),
    check("the l2 entry still reads L2_KEYWORDS and groups A, C, D, E, F, G",
          gen.CRITERION["l2"]["keywords"] is gen.L2_KEYWORDS
          and tuple(gen.CRITERION["l2"]["groups"]) == ("A", "C", "D", "E", "F", "G"),
          list(gen.CRITERION["l2"]["groups"])),
    check("the l3 group term names every id of the register's groups table, in its order",
          tuple(spec_l3["groups"]) == REGISTER_GROUPS,
          {"l3": list(spec_l3["groups"]), "register": list(REGISTER_GROUPS)}),
    check("the l3 home-document, passage, keyword and named-identity terms are empty",
          not spec_l3["home_documents"] and not spec_l3["architecture_spans"]
          and not spec_l3["keywords"] and not spec_l3["always"], None),
    check("no l3 withheld family", "l3" not in gen.WITHHELD, None),
    check("no l3 verdict table", "l3" not in gen.VERDICTS, None),
    check("no l3 extras list", "l3" not in gen.EXTRAS, None),
    check("no l3 freeze", "l3" not in gen.FROZEN, None),
]

design_intent = [e for e in sort["entries"] if e.get("proposed_class") == "DESIGN-INTENT"]
di_ids = {e["id"] for e in design_intent}
cands = gen.candidates("l3", design_intent, backbone)
ALL = {c["id"] for c in cands}
G = {c["id"] for c in cands if any(w["criterion"] == "group" for w in c["matched_by"])}
OTHER = sorted({w["criterion"] for c in cands for w in c["matched_by"]} - {"group"})
outside = sorted(e["id"] for e in design_intent if e.get("group") not in REGISTER_GROUPS)

arith = [
    check("the design-intent population is 244", len(design_intent) == 244, len(design_intent)),
    check("the group term picks 244", len(G) == 244, len(G)),
    check("the criterion picks 244 of 244", len(ALL) == 244 and ALL == di_ids, len(ALL)),
    check("no candidate is reached by any other term", not OTHER, OTHER),
    check("no design-intent entry stands outside every register group", not outside, outside),
]

result = {
    "what_this_is": (
        "THE CHECK THAT L3's RULED CANDIDATE CRITERION WAS WRITTEN INTO THE GENERATOR AS RULED. It "
        "reads the COMMITTED criterion table and calls the generator's own candidates() over it. It "
        "authors no verdict, withholds nothing, renders no pack and boots no session."),
    "the_rulings_it_checks": [
        "Rulings 1 and 2 of records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md "
        "- a withheld family, and every design-intent entry a candidate."],
    "how_it_was_derived": (
        "The generator's own candidates() over the committed CRITERION table, nothing injected (#6)."),
    "the_shape_of_the_table": shape,
    "the_arithmetic": arith,
    "the_counts": {"sort_entries_total": len(sort["entries"]),
                   "design_intent_class": len(design_intent),
                   "candidates": len(ALL),
                   "groups_present_among_the_design_intent_entries":
                       sorted({e.get("group") for e in design_intent})},
    "the_three_identities_the_ruling_left_unchecked": {
        i: {"in_the_design_intent_class": i in di_ids, "a_candidate": i in ALL}
        for i in UNCHECKED_BY_THE_RULING},
    "the_bound_on_this_check": (
        "It establishes that the table matches the rulings and that the tool's own matcher picks the "
        "whole design-intent class. It establishes NOTHING about any entry's verdict, and the "
        "population is the sort artifact's, not the decisions register's whole membership (#24, D-661)."),
}

out = os.path.join(HERE, "l3_criterion_written_check.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump(result, fh, indent=1, ensure_ascii=False)
    fh.write("\n")
for row in shape + arith:
    print(("PASS " if row["passed"] else "FAIL ") + row["check"] + f"   saw={row['saw']!r}")
print("wrote", out)
print("FAILED CHECKS:", len(fail))
```

**(c) The command:**
`cd C:\s\MS && python %TEMP%\l3_criterion_written_check.py > %TEMP%\l3_crit_out.txt 2>&1; echo "exit:$?"` — then
read `%TEMP%\l3_crit_out.txt`. **What must hold: `FAILED CHECKS: 0`**, the criterion picking **244 of 244**. **Any
failure ends the batch:** do not adjust the criterion to make a number come out; restore the generator by explicit
hash, report the failing checks, and go straight to Task 5's report and close with Tasks 3 and 4 NOT done (A2's
end-state prediction then does not apply; report the run as measured).

**(d) Commit** the generator and the check artifact together:
`feat(audit): write L3's ruled candidate criterion into the boot-pack generator (dormant; no verdict, nothing withheld, no pack)`.
Push; verify. **Do not paste the artifact into the report; cite it (D-431).**

**E1–E2:** the one insertion; the before/after `--check` outputs identical; `FAILED CHECKS: 0`; the commit pushed.

## Task 3 — the two guard reds

### (i) `gen_l2_outgoing_population.py` becomes a historical record (L.3, Ruling 1)

**(a) The reader enumeration — R4's per-tool condition, FIRST, before any edit.** With the `Grep` file tool, search
the whole repository for the string `l2_outgoing_population` (it is common to the tool's name and its artifact's).
List every hit file. Class each: **(1)** the tool itself, `tools/audit/gen_guard_state.py`,
`tools/audit/gen_guard_classification.py`, `tools/audit/guard_state.json`, `tools/audit/guard_classification.json`;
**(2)** records — any `.md` file, and any `changed_paths_*.json` enumeration artifact; **(3)** anything else. Open
each class-(3) file at its hits and say whether it reads the artifact or imports the tool when it runs. **If any
class-(3) file does, that is a STOP-and-report for Task 3(i) alone**: make no edit for it, report the reader, and
go on to Task 3(ii). Write the enumeration into the report in full.

**(b) The two insertions — only if (a) found no live reader.**

In `tools/audit/gen_guard_state.py`, inside `HISTORICAL`, old text (must occur exactly once):

```python
        "act; the 2026-09-17 root records move turned it red on renamed paths. The artifact stays on disk as "
        "committed (#12).",
}
```

New text:

```python
        "act; the 2026-09-17 root records move turned it red on renamed paths. The artifact stays on disk as "
        "committed (#12).",
    # ── THE FINISHED L2 COMPARISON'S OUTGOING POPULATION ──────────────────────────────────────
    # RECLASSIFIED 2026-10-14 by `cc_instruction_l3_criterion_write_2026_10_14.md` Task 3(i), on the
    # user's Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_10_14_l2_outgoing_population_check_sitting.md`
    # (his word "C"), after the reader enumeration that ruling orders came back with no live reader.
    "tools/audit/gen_l2_outgoing_population.py":
        "HISTORICAL RECORD: the population the finished L2 comparison tabulated, numbered by position, "
        "and records cite members by those positions (member 52, the confidence contract). The "
        "tool re-derives the population from the live tree, so an ordered amendment of a member text "
        "renumbers members: the 2026-10-14 ratification application's ordered edit of "
        "`cowork_confidence_contract.md` would exchange positions 51 and 52. Re-deriving it would change "
        "what ratified records name. The artifact stays on disk as committed (#12, D-646).",
}
```

In `tools/audit/gen_guard_classification.py`, inside `VERDICTS`, old text (must occur exactly once):

```python
    "tools/audit/gen_phase1_completion_inventory.py": (
```

New text — the new entry inserted immediately before it, that line unchanged:

```python
    "tools/audit/gen_l2_outgoing_population.py": (
        POINT, "gen_l2_outgoing_population.py:4-10, :38-41; "
               "records/cowork/rulings/cowork_rulings_2026_10_14_l2_outgoing_population_check_sitting.md §1",
        "★ CLASSIFIED 2026-10-14, ON THE USER'S RULING (his word \"C\"). Its artifact numbers the members "
        "the finished L2 comparison tabulated, and records cite members by position; the tool "
        "re-derives from the live tree, so an ordered amendment of a member text renumbers them — the "
        "2026-10-14 edit of the confidence contract would exchange positions 51 and 52. That is a record "
        "of a completed act, R4's point-in-time side. The reader enumeration the ruling orders found no "
        "live reader (cc_report_l3_criterion_write_2026_10_14.md). Before this date the tool carried NO "
        "verdict in this table."),
    "tools/audit/gen_phase1_completion_inventory.py": (
```

Leave `AUTHORED`'s `gen_l2_outgoing_population.py` entry exactly as it stands (the precedent shape).

**(c) Run** `python tools/audit/gen_guard_classification.py --check` to a temp file and read it. Its `build()`
checks in this order: tools with no authored verdict; verdicts naming a tool the guard state does not carry; the
`POINT` verdicts against `gen_guard_state.HISTORICAL` (the *"disagree"* STOP); then `guard_state.json`'s
`historical_records` against the verdicts (the *"re-run gen_guard_state.py"* STOP). **Expected now:** the first
STOP, naming only tools of the standing STOP and not `gen_l2_outgoing_population.py` — or, if that list has
emptied, the *"re-run gen_guard_state.py"* STOP, which is expected until the end-state run rewrites
`guard_state.json`. **The *"disagree"* STOP, or any other, is a STOP-and-report:** restore both tools by explicit
hash. Report the message whole. **Re-run it after Task 5's end-state guard run**, where only the standing
missing-verdict STOP (less this tool, if it was one of the four) may remain; report that message too.

**(d) Commit** the two tools:
`audit: the L2 outgoing-population tool becomes a historical record (the user's ruling of 2026-10-14)`. Push;
verify.

### (ii) the confidence contract's references in the register's data file (L.3 §2)

**(a) Two authored values in `tools/audit/decisions/backbone_decisions.json`**, inside
`"cowork_confidence_contract.md"`'s `section_kind`. Keep the file's exact formatting (two-space JSON, characters
unescaped) — `gen_home_classification.py` and `reaim_home_anchors.py` both REFUSE a file that does not re-serialize
byte-identically.

Old text (exactly once): `            "heading_text": "2. Definitions — the two admissible confidence classes",`
New text: `            "heading_text": "2. Definitions — the three admissible confidence classes",`

Old text (exactly once, three lines):
```
            "heading_line": 63,
            "heading_text": "4. The comparison frames (the §8 override arithmetic, stated once)",
            "states_rules": true,
```
New text: the same three lines with `63` replaced by `81`.

The former values are stated in the commit message (#12, recoverable from git).

**(b) The drifted `home` anchors, by the sanctioned tool.** Run
`python tools/audit/decisions/reaim_home_anchors.py --check` to a temp file and read it. **Expected exactly three
moves, each `+18`:** D-268 `cowork_confidence_contract.md:36-48` → `:54-66`, D-269 `:83-85` → `:101-103`, D-601
`:89-101` → `:107-119`. **If it reports anything else, write no anchor**: report the list whole and go to (c)
with (a) alone. (That outcome is possible: `gen_cluster_dispositions.py --verify` is already red on a cause the
writing side did not establish, and the tool re-aims every drifted entry in the register, not only these three.
Part (a) alone is what clears `gen_retired_subject_moves.py`.) If exactly those three, run it without `--check`, and confirm by
`python tools/audit/decisions/gen_cluster_dispositions.py --verify` (to a temp file) that none of D-268, D-269 and
D-601 is reported drifted (the check stays red on its standing cause; report its before and after text).

**(c) Regenerate the rendered register** (rule (d)): `python tools/audit/decisions/gen_decisions_register.py`, then
its `--check`. **Expected:** the rendered change is the three `home` anchors at their entries in `decisions/group_C.md`
(the generator renders `**Home.** `<file:lines>`` per entry), plus any line that prints a digest of the backbone
file itself (`DECISIONS.md`'s provenance carries one — the writing side did not establish whether that line is
regenerated). Compare every rendered file that moved against its committed blob; any other change is a
STOP-and-report: restore the backbone and the rendered files by explicit hash and report.

**(d) Measure:** `decisions/gen_retired_subject_moves.py --check` — **PASS predicted**; `decisions/gen_home_classification.py
--check` — red predicted on its standing cause, its text reported before and after (its derived `home_section`
blocks for D-267, D-268, D-269 and D-601 are NOT hand-edited: that classifier's own write mode rewrites them, and it
is not run here because its check is red on a cause this batch does not own).

**(e) Commit** the backbone and the regenerated register files:
`audit: re-aim the register's references into the amended confidence contract (§2 heading text was "the two admissible confidence classes"; §4 heading line was 63; D-268, D-269, D-601 anchors +18)`.
Push; verify.

**E3:** (i) done or STOPped with its reader named; (ii) done, or the anchor part withheld with the drift list
reported; every commit pushed.

## Task 4 — the slice derivation and row 36's progress (documentation only)

**(a)** In `cowork_l2_task_b_slice_derivation_2026_09_05.md`, old text (exactly once): `**The one L3 row.** |`
New text: `**The one L3 row** of this file's own population; L3's whole slice is at §5 *(★ corrected 2026-10-14; former wording, preserved (#12): "**The one L3 row.**")* |`

**(b)** Same file, old text (exactly once): `- **L3's slice: 1 row** — 36.`
New text:

```
- **L3's slice: 4 rows** — 36, 37, 38, 39; rows 34 and 40 carried for their noted L3 bearing and not
  counted twice. *(★ CORRECTED 2026-10-14 under `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_four.md`
  §2, which tested rows 37, 38 and 39 against the L3 charter — §2 of this file removed them from its population as
  L1 rows already read, so they were never tested here — and put the slice to the user by name; his next word was
  "continue", read by that sitting as no challenge to any placement, a reading and not a ruling. Every placement
  stays challengeable at its own row. **FORMER WORDING, PRESERVED (#12): "L3's slice: 1 row — 36."** The
  "40 + 1 = 41" check below counts this file's own §2 population and is unchanged.)*
```

**(c)** In `reading_pass/candidacy_upgrades.md`, insert after the line
`proposes, headed by L2's entangled decision. The remainder is untouched.**` (exactly once) and before the blank
line and `---` that follow it:

```

## ★★ THE L3 SLICE — appended 2026-10-14

**L3's slice, as put to the user by name** (`records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_four.md`
§2; his next word "continue", read by that sitting as no challenge — a reading, not a ruling): rows **36, 37, 38,
39**, with rows **34** and **40** carried from L2's slice for their noted L3 bearing. The derivation is that entry's
and is not restated here (#6).

| Row | Paper | Grade | Extract | Centrality | Second pass |
|---|---|---|---|---|---|
| 36 | Ju, Margot, McKay, Dahn & Fujinaga 2020, automatic figured bass annotation (BCFB) | **AT THE OBJECT**, whole, 7 pp., printed pp. 640–646 | `reading_pass/extracts/ju-margot-mckay-dahn-fujinaga-2020-automatic-figured-bass-annotation-bach-chorales-figured-bass-dataset.md` | **CENTRAL** | **OWED** |
| 37, 38, 39 | (the L0+L1 table above) | read for L1 (the table above) | (the table above) | **not decided for L3** | (the table above) |

*Row 36's cells are relayed from `records/cowork/handoff/cowork_handoff_entry_three_hundred_and_ninety_five.md`
§1. Whether rows 37, 38 and 39 are CENTRAL for L3 is left to the first L3 act that needs it (entry 394 §4
step 5).*
```

**(d) Commit** both files: `docs(reading-pass): L3's slice at four rows, former count kept; row 36's first pass recorded`.
Push; verify.

**E4:** the three edits made, or each reported as a STOP; the diff of each file shows only them.

## Task 5 — the close

1. **The `STATUS.md` entries and the forward-bound move, IN THIS ORDER** (read `gen_status_batch_bound.py` whole at
   the object first, ordered first read (9)). **(a)** Write this batch's entries at the top of `STATUS.md`: one
   pointer entry per task that did work — the close entry FIRST, NAMING THIS DISPATCH BY ITS FILE NAME
   (`records/cc/instructions/cc_instruction_l3_criterion_write_2026_10_14.md`), each earlier task's entry below it
   saying `Same dispatch`; no figure restated (D-431); **the `Last updated: ` prefix moved from the last batch's
   close entry (the topmost at the tip, naming `cc_instruction_l2_ratification_application_2026_10_14.md`) to your
   newest entry.** **(b)** Re-aim the five authored constants of `gen_status_batch_bound.py`: `BASE_COMMIT` (this
   batch's last task commit before the close), `PREVIOUS_BATCH_DISPATCH`
   (`cc_instruction_l2_ratification_application_2026_10_14.md`), `ACT_DATE` (the day the move runs), `DISPATCH`
   (`cc_instruction_l3_criterion_write_2026_10_14.md`), `TASK` (`Task 5`); append your own aiming to
   `PREVIOUS_AIMINGS` on the convention its comments state (the last report §10 item 2: every aiming exactly
   once). **(c)** Run `gen_status_batch_bound.py --apply`. **Prediction:** it moves **exactly the last batch's five
   entries** (its close entry and the four `Same dispatch` entries for Tasks 3 to 0); the two 2026-09-02 entries
   stay. If it STOPs, restore its passing aim, re-run green, report, move nothing by hand. **(d) LAST**, after the
   final `STATUS.md` edit, regenerate `gen_session_start_read_size.py` and confirm its `--check` green. Commit the
   re-aimed tool, `tools/audit/status_batch_bound.json`, `STATUS.md`, `STATUS_ARCHIVE.md` and the read-size artifact
   together in the close.
2. **The report**, `records/cc/reports/cc_report_l3_criterion_write_2026_10_14.md`, which decides nothing: both
   guard states; every SHA (or a pointer to the git log where it cannot contain one); E0 to E4 and A1 to A4 graded;
   Task 1's before/after comparison; Task 2's result by citation to its artifact; Task 3(i)'s reader enumeration
   whole and the classification tool's message; Task 3(ii)'s anchor list and the before/after text of the two red
   checks whose output it changes; the `criterion_block()` finding; declared departures; and the plan's tell in one
   sentence — did this batch produce anything other than the landed paths, the generator's one insertion and its
   check artifact, the two guard-tool insertions, the backbone's two values and three anchors with the regenerated
   register, Task 4's three edits, the Task 5 files and the report? If yes, name it.
3. **The full close appended to `records/cowork/handoff/cowork_away_returns.md`** as a section headed **THE L3
   CRITERION WRITE: L3's CANDIDATE CRITERION IN THE GENERATOR, THE TWO RATIFICATION-APPLICATION REDS CLEARED, NO
   VERDICT, NO PACK, NO ALGORITHM CHANGED** — the report's content as pointers, and the plan line: **the next act is
   the writing side's — L3's candidate list and verdict pass, as for L2.**
4. **The close does not assert the end state**; one further commit carries it. Commit the close, push, verify;
   then the full guard run in write mode at that tree, and the one further commit with its artifacts, pushed and
   verified.

**E5:** at the tree carrying the close, a fresh full guard run — the A2 prediction (79 run, 20 historical, failing
the fourteen named), the A2 exceptions handled as A2 says — committed only after the run that produced it.

## What this batch does NOT do

- **No verdict, no withheld identity, no pack rendered, no session booted.** L3's verdicts are authored and ruled
  later, list by list (Ruling 2).
- **No change to what any layer computes** as its specification defines it. Every edit is a table entry of a tool,
  a reference re-aimed, a guard reclassification on the user's ruling, or documentation.
- **No decisions-register entry, no `D-NNN`, nothing in the suspension file**; D-267's own wording stays as it is,
  waiting on the register route.
- **No repair of `criterion_block()`'s fixed bullet**; no hand-edit of a derived `home_section` block.

*Provenance: Cowork writing side, 2026-10-14 (Stockholm), the sitting booted on entry 397, at tip
`b6bceef7009f92e89a97c8a79465e5e462e1f49a` read as files; no shell command was run. **Read by the writing side,
at the extent named:** the three ruling records, entries 291 and 391 to 397, the model dispatch whole, the last
dispatch at its head, premise ledger, Task 0 and Task 4, its report whole; the generator at the parts named in
first read (6); `gen_guard_state.py` at `AUTHORED`'s L2-population entry and `HISTORICAL`;
`gen_guard_classification.py` at `VERDICTS`' opening and `build()`'s STOPs; `gen_home_classification.py` at
`headings_of()` to `derive_kind_moves()`, `classify()`'s kind checks and `main()`; `reaim_home_anchors.py` and
`gen_retired_subject_moves.py` whole; `gen_decisions_register.py` at its usage and home rendering; the sort file
by search; the backbone at the passages quoted; `cowork_confidence_contract.md` lines 1–121; the slice derivation
at §4–§7; `candidacy_upgrades.md` at its READING PROGRESS section to its end; `guard_state.json` at
`historical_records` and `summary`; the rule (c) suspension file whole; `DECISIONS.md` whole. **NOT read:** `cowork_audit_protocol.md`,
`BUILD_AND_TEST.md`, `gen_status_batch_bound.py`, `gen_cluster_dispositions.py`, row 36's extract, the last close
in `cowork_away_returns.md`, and `records/cc/instructions/`'s listing. The authored choices — the twenty-group
expression, the empty other terms, the subject key `l3`, the wording of the new comments, verdict and `HISTORICAL`
reason, and Task 4's texts — are the writing side's, overrulable by the user before Task 0.*

## The writing side's check of this dispatch at its sources (recorded per the standing clause and D-434; run 2026-10-14 in a turn of its own, after the user's "continue")

**Checked at the objects and holding:** every old text Tasks 1, 3 and 4 quote occurs exactly once at its staged
file (the generator's `l2` closing lines, `HISTORICAL`'s closing lines, the classification tool's
`gen_phase1_completion_inventory.py` line, the backbone's §2 `heading_text` line and its §4 three-line block, the
slice derivation's two strings, `candidacy_upgrades.md`'s closing line); the string `"l3"` occurs nowhere in the
generator; D-269's patterns (*"New frames require declaration here"*) match the contract's lines 101–103; the
register generator renders each entry's full `home`, so the rendered change falls in `decisions/group_C.md`
(D-268, D-269 and D-601 are group C); the last batch's `STATUS.md` entries are five.

**Corrected at their sites:** *(1)* Task 3(ii)(c)'s expectation omitted a digest line of the backbone in the
rendered provenance — added, marked as not established. *(2)* Task 3(ii)(b) did not say that the anchor tool
re-aims drift anywhere in the register, so a list longer than three is possible — said. *(3)* Task 3(i)(c)
expected no STOP other than the standing one, where `build()`'s fourth check stops on `guard_state.json` until
the end-state run rewrites it — the order of the four checks stated, the expected messages corrected, a re-run
after the end state added. *(4)* "ratified records cite members by position" in the `HISTORICAL` reason and the
verdict — the records' ratified standing was not established by the writing side; now "records". *(5)* "no `l3`
key anywhere in the file" rested on an indentation-bound search — re-searched for the bare string and reworded.
*(6)* A1's line-ending fact is a relay from the last report — marked. *(7)* Task 2's failure path left A2's
prediction standing — bounded. *(8)* The provenance said every object named was read — it was not; the read and
unread objects are now listed.

**Not established by this check:** that the guard run's `run` count falls to 79 when a tool moves to `HISTORICAL`
(a prediction from the summary's separate counters, measured by your run); whether `gen_l2_outgoing_population.py`
is one of the standing four unclassified names; the cause of the standing reds; anything in the files the
provenance lists as not read.
