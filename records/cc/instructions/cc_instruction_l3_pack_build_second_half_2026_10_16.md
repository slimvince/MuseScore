# CC dispatch — L3's PACK BUILD, SECOND HALF: the records landed; the generator's "rendered before the scoping rulings" test keyed on an authored list and L2's spent pack frozen; L3's verdict date and the criterion bullet; `WITHHELD["l3"]` and `EXTRAS["l3"]` authored; L3's pack RENDERED; the lists to the user — NO session booted, NO algorithm change, NO register entry

> **★★ RELEASED 2026-10-16** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twelve.md`, which wrote it, after the check at the
> sources recorded at the end of this file. It is executed by Claude Code when the user hands it over (D-252); the
> Cowork writing side never runs it. *(The banner this replaces read, preserved (#12): "**★★ DRAFT UNDER CONSTRUCTION
> BY THE COWORK WRITING SIDE — NOT TO BE HANDED TO CLAUDE CODE.** Claude Code: if you are reading this banner, STOP at
> once, do nothing, and report that you were handed an unfinished draft.")*

## What this batch is, in plain words

The first half of L3's pack build (`records/cc/instructions/cc_instruction_l3_pack_build_first_half_2026_10_15.md`)
landed its records, derived and printed L3's withheld documents, and cut the two input-contract copies. Its Task 1 —
freezing L2's spent pack — STOPPED at its own condition, and its Task 2 was not performed
(`records/cc/reports/cc_report_l3_pack_build_first_half_2026_10_15.md` §5, §6). Since then:

- the user confirmed the five derived documents (`records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_documents_confirmation_sitting.md`,
  Ruling 1, his word *"yes"*);
- the writing side found that the record settles the freeze STOP and recorded a derivation, not a ruling
  (`records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md`);
- the writing side derived the per-file cut list for L3's research-extracts member
  (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`).

This batch does the rest of the pack build:

1. **Task 0** lands those records and handoff entries 410 to 412, and pushes.
2. **Task 1** repairs the one test the freeze STOP found (§0 of the derivation record) and then freezes L2's pack,
   with the before/after comparison D-657 demands. **A movement outside the expected shape is a STOP with nothing
   committed, and the batch then ends after its close** — L3's pack is not built while L2's is live (Ruling 1 of
   `cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, noted).
3. **Task 2** redoes the first half's Task 2 (three edits) as written there.
4. **Task 3** authors `WITHHELD["l3"]` and `EXTRAS["l3"]` together — `build()` builds every subject of `WITHHELD`,
   and `build_subject` reads `EXTRAS[subject]`, so neither can land without the other.
5. **Task 4** renders L3's pack, proves the four frozen subjects did not move, and assembles the lists that go to
   the user before any session boots.
6. **Task 5** closes.

**Documentation and algorithm.** Every ruling this batch executes decides only what a future deriving session reads,
and the derivation it applies decides what the record of a spent session says. This batch edits a pack generator and
its manifest and renders a pack directory. **Nothing here changes the algorithm as any specification defines it.** The
currently decided method for L3 is `FRAMEWORK.md` §5's L3 block with DP-I (*"split — cues at L1, type at L3"*).

## Words used in this dispatch, explained first

- **Boot pack, member, extra, withheld family, verdict (IN / OUT / UNPLACED), guard set, red, spent subject /
  FROZEN, digest, the manifest, the criterion bullet, home document, input contract, a cut copy** — as defined in
  "Words used in this dispatch" of `records/cc/instructions/cc_instruction_l3_pack_build_first_half_2026_10_15.md`.
  **IN** means withheld from the pack.
- **The generator** — `tools/audit/gen_derivation_boot_pack.py`.
- **The scoping rulings** — the two rulings that changed how a pack is built after the first three packs were
  rendered: limb B of Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_21_l2_extracts_member_cutting_sitting.md`
  (every line of a rendered extra is scanned for leak strings, and the hits are listed for the user) and Ruling 1 of
  `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md` (the cross-reference rule searches only
  `title`, `verbatim` and `plain`).
- **A filter entry** — one dict in a part's `removals` list (`anchor`, `opens_with`, `closes_with`, `why`) or `cuts`
  list (`heading_contains`, `heading_level`, `why`, and `runs_to_end` where given), read by the generator's
  `filter_part`.
- **A carried part** — one of the twelve extract files that are already parts of `EXTRAS["l2"]`'s member (8). Its L3
  part carries L2's filter entries for that file **unchanged and in L2's order**, then the additions this dispatch
  gives (the cut list's §3 rule).
- **A dump** — the manifest dict `build()` returns, written by the dump script below to a file in your scratch folder
  outside the repository, exactly as `write_all` would write it. Producing a dump writes nothing into the repository.

## The ruling ledger

| | Record or rule | What it orders | Task |
|---|---|---|---|
| L.1 | The standing clause (a sitting record lands at the next dispatch's Task 0) | The records named in Task 0, landed as they stand. | 0 |
| L.2 | The derivation at `cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md` §2, applying Ruling 1 of `cowork_rulings_2026_09_27_l2_leak_list_sitting.md` as ruled | The three tests on `subject in FROZEN` keyed on an authored list of the packs rendered before the scoping rulings; the D-657 comparison; any other movement a STOP. | 1 |
| L.3 | Boot-list Ruling 1, "Noted, not ruled" | L2's pack frozen before L3's is built. | 1 |
| L.4 | Entries 398 §2, 399 §2, 401 §3 item 7, carried by the first half's Task 2 | `VERDICT_DATE["l3"]`; the criterion bullet derived from the authored groups. | 2 |
| L.5 | Boot-list Rulings 4 and 5; the confirmation record's Ruling 1 | `WITHHELD["l3"]`: the five confirmed documents with finding, date and reason; no withheld passage of `CLAUDE.md`. | 3 |
| L.6 | Boot-list Rulings 1 and 3; Ruling 1 of `cowork_rulings_2026_10_15_l3_first_pass_extracts_sitting.md`; limb A of Ruling 1 of 2026-09-21; the cut list | `EXTRAS["l3"]`: the shared charter member, the seventeen-file extracts member cut per file, the shared ledger member. | 3 |
| L.7 | Boot-list Ruling 3 and Ruling 5's ground; Ruling 84 as Ruling 2 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md` restates it | The render; the extras' leak scan listed to the user; every cross-reference addition that would withhold an entry the user ruled admitted put to him as its own list. | 4 |
| L.8 | The user's standing rule (entry 393 §2; 2026-10-14) | Every commit pushed, the push verified at `.git/refs/remotes/origin/master`. | all |

## Premise ledger (written 2026-10-16 by the writing side from staged copies read with the file tools; no shell command and no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/HEAD` → `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both `a01e9402fbaf034fe0d357214b67c06a8294309c` (the first half's end state).
  **Re-read both ref files yourself before Task 0.**
- **RELAYED — the guard start state** (entry 410 §1, read there at `tools/audit/guard_state.json` → `summary`): run 81,
  failing 14, `gen_derivation_boot_pack.py --check` among them. Not re-read by the writing side.
- **RELAYED — why the generator's `--check` is red** (report §2, measured by the first half): *"derivation_boot_pack.json
  does not re-derive"*, *"l2/02_the_guiding_principles_and_the_conventions.md does not re-render"*,
  *"l2/07_the_charter_the_layers_and_the_decisions.md does not re-render"* — `l2` being live.
- **FACT — the generator, read at these parts:** `VERDICT_DATE` carries `harmony-boundary` and `l2` and no `l3`;
  `FROZEN` carries `harmony-boundary` (frozen 2026-08-31), `scoring-model` (2026-08-31) and `l0-l1` (2026-09-04), each
  with `finding`, `date`, `reason` and `digests`, and the table ends with the two lines `    # made false by that
  session's run.` and `}`; `WITHHELD` carries the four subjects `harmony-boundary`, `scoring-model`, `l0-l1`, `l2`;
  `EXTRAS` carries the same four and no `l3`; `CRITERION["l3"]` exists (twenty groups); `VERDICTS["l3"]` exists.
  `build_subject` tests `subject in FROZEN` in exactly three places (found by search over the whole file; the other
  three hits, `if subject in FROZEN:` in `build()`, `write_all` and `check_all`, are not edited): the field choice
  `XREF_FIELDS_FROZEN if subject in FROZEN else XREF_FIELDS`, the line `extras_leaks: list[dict] | None = None if
  subject in FROZEN else []`, and the `★_what_these_are` switch `if subject in FROZEN else (`. `build()` builds every
  subject of `WITHHELD`, adds `★_FROZEN` and calls `frozen_from_disk` for a frozen one; `write_all` writes the
  manifest, and every subject's directory **except a frozen one's**; `main()` takes `--subject` and `--check`.
  **The generator was NOT read at `filter_part`, `_cut_spans`, `_removal_spans` or `render_extra` by this writing
  side**; the cut list's writing side read them (entry 412 §2).
- **RELAYED — L2's pack directory**, its ten files' digests as the first half measured them at `5499f3e2…` and the report
  §5 table records them (all three forms agreeing): `00_READ_THIS_FIRST.md` `fd27dee7a4b6bca3454d12c659aa34a96cd1abc1`;
  `01_the_phase_definitions.md` `518b1e50d60af2b4e2ddcd8978623832eb071899`;
  `02_the_guiding_principles_and_the_conventions.md` `41288e7375faca980c566ca0367fca1c7de760e8`;
  `03_the_writing_standards.md` `a41983018cb27ed4a47d24ff8bb9e95181ed0572`; `04_the_dispatch_protocol.md`
  `72b8a1fb58ed50a2fbdc65a08ff4ec68e863e9da`; `05_the_ratified_design_intent.md`
  `6ae0b1d8c9a830cfc3f2021f37460f05fad23547`; `06_the_defect_type_catalog.md` `1dec7621dc48d89242cacaf79b3048cd965d6a19`;
  `07_the_charter_the_layers_and_the_decisions.md` `5796c2d1bda0520b067ccde300e25336b9606884`;
  `08_the_fifty_six_research_extracts.md` `69404bace220b25589e78edc7c89c513ae5a0e2e`;
  `09_the_empirical_findings_ledger.md` `925c458e6a77b728bc9815ac75fb8c8a6c1bc0f6`. **Yours are the digests; a
  difference from these is a STOP.**
- **FACT — the first half's in-memory simulation** (report §5): with `FROZEN["l2"]` added and the generator otherwise as
  it stands, `l2`'s record moved in `LEAKS`, `LEAKS_IN_THE_EXTRAS` (removed), `THE_WITHHELD_FAMILY`, `counted`,
  `the_members_as_rendered` and `★_FROZEN`; the three frozen subjects did not move. The cause is the three tests above.
- **FACT — the named risk, stated by the derivation (§2) and NOT measured by anyone:** a frozen subject is still built
  from today's sources, and `frozen_from_disk` re-points member sizes at the directory but does not re-point the
  extras' leak list. L2's charter source (`FRAMEWORK.md` §5) has changed since L2's pack was rendered, so a leak hit's
  line number in member (7) may move, and then `LEAKS_IN_THE_EXTRAS` moves and Task 1's STOP fires. **Whether it
  fires is unmeasured; Task 1 measures it.**
- **FACT — L3's withheld documents** at `tools/audit/l3_withheld_documents.json` (read whole): 22 IN identities; five
  documents — `ARCHITECTURE.md` (D-022, D-472, D-495, D-584, D-605), `cowork_joint_estimator_architecture.md` (D-526),
  `cowork_layer5_function_design.md` (D-336), `cowork_layer6_grouping_design.md` (D-454, D-455, D-456, D-457, D-459,
  D-460, D-461, D-462), `cowork_phrase_boundary_design.md` (D-476, D-477, D-478, D-479, D-480, D-481, D-485). The
  confirmation record's table states the same.
- **RELAYED — the ruled L3 family:** 22 IN, 222 OUT, 0 UNPLACED (entry 401 §1 and the first half's premise ledger; the
  22 IN checked by the confirmation sitting at `VERDICTS["l3"]`).
- **FACT — the twelve carried files** are parts of `EXTRAS["l2"]`'s member (8), each found once by its `"source"` line
  (§5 of this dispatch names them). The other five (rows 36, 37, 38, 39 and ChoCo) are not parts of it.
- **RELAYED — every filter string of §5** was searched at its own file by the cut list's writing side in a turn of its
  own (its §7): every anchor found once, every delimiter on the right side of its anchor, every cut heading found once
  at `## `. **Whether each runs without a STOP is proved only by the render.**

- **ASSUMPTION A1 — the working tree, by content.** Tracked modifications at boot, expected: none, except the
  line-ending-only marking of `tools/audit/claude_md_finer_archive.json` the last reports record (re-establish it;
  leave it untouched; never stage it). Any other tracked modification at boot or during the run is a STOP-and-report,
  except a path this batch writes, after the task that writes it and until its commit. A further untracked
  `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` appearing during the run is the writing side's, NOT landed and
  NOT a STOP. **Check (Task 0, first act):** per tracked input this batch edits (`tools/audit/gen_derivation_boot_pack.py`,
  `tools/audit/derivation_boot_pack.json`, `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`)
  `git diff --stat a01e9402fbaf034fe0d357214b67c06a8294309c -- <path>; echo "exit:$?"`; per path of Task 0's list
  `git ls-files --others --exclude-standard -- <path>; echo "exit:$?"`; the whole tracked population with
  `tools/audit/changed_paths.py`.
- **ASSUMPTION A2 — the guard run before the first edit:** the fourteen, plus **`gen_evidence_pin_membership.py
  --check` red** if the untracked ruling records are read by it (the first half's start run had exactly this
  fifteenth red; two ruling records are expected to be untracked now — Task 0's item 3). The classification tool's standing STOP naming
  `gen_l0_l1_outgoing_population.py`, `gen_l2_withheld_documents.py` and `gen_withheld_family_reading.py`
  **[relayed]**. **Predicted at the end state:** run 81; failing the fourteen less `gen_derivation_boot_pack.py` if its
  `--check` goes green after Task 4 — **a red `--check` after Task 4's render is a STOP before that task's commit**
  (Task 4(b)). Reds this batch's own acts may cause, classed by cause and NOT a STOP: `gen_evidence_pin_membership.py
  --check` (Task 0 handles it); `gen_derivation_boot_pack.py --check` between Task 3's edit and Task 4's render;
  `gen_l0_l1_outgoing_population.py --check` and `gen_defense_share.py --check` if Task 5's `STATUS.md` entries move
  their inputs — regenerate, compare against the committed blob by explicit hash, commit with the end state, report
  that no member moved (a member moving IS a STOP-and-report); `gen_session_start_read_size.py --check` if regenerated
  before the last `STATUS.md` edit; `gen_guard_state.py`'s own artifact until the end-state run. A red outside these is
  a STOP-and-report.
- **ASSUMPTION A3 — byte-unchanged by this batch, verified at the objects after the last commit:** every governing
  document except `STATUS.md` and `STATUS_ARCHIVE.md`; **every file under `tools/audit/derivation_boot_pack/harmony-boundary/`,
  `…/scoring-model/`, `…/l0-l1/` and `…/l2/`**; in the generator, everything except the edits Tasks 1 to 3 quote;
  `tools/audit/l2_withheld_documents.json`, `tools/audit/l3_withheld_documents.json`, `tools/audit/gen_l2_withheld_documents.py`;
  both input-contract copies under `tools/audit/derivation_exemplars/l3/`; every ruling record, the cut list and every
  extract (landed only, as they stand); `FRAMEWORK.md`; `EMPIRICAL_FINDINGS_LEDGER.md`; every rendered
  decisions-register file. Any other difference is a STOP-and-report.

## The standing bars, and the commit-and-push discipline

No `src/` edit, no golden, no test changed or run, no build, nothing under `tools/corpus/` or `tools/robust_stop/`,
**no measurement of the analysis built, designed, scoped or run**, no derivation of any specification statement,
**NO SESSION BOOTED, NO BRIEF WRITTEN, NO SCORE COPIED OR STAGED**, **no pack directory written except
`tools/audit/derivation_boot_pack/l3/`** (and that one only at Task 4(a)), **no edit to `CRITERION`, to `MEMBERS`, to
`CHARTER_MEMBER_7`, to `LEDGER_MEMBER_9`, to `EXTRAS["l2"]`, to `WITHHELD` for any subject but `l3`, or to any
`VERDICTS` entry**, no edit to `filter_part`, `_cut_spans`, `_removal_spans`, `render_extra` or any other function
body except the three tests and the one STOP Task 1 quotes and Task 2's edit of `criterion_block`, no open-items row created, flipped or discarded, **no
decisions-register entry and no `D-NNN` allocated, nothing written into the suspension file**, no edit to any governing
document except `STATUS.md`/`STATUS_ARCHIVE.md` in Task 5, **no edit to any ruling record, to the cut list, to any
extract or to either input-contract copy**, **no leak list acted on — every list goes to the user — no ruling taken,
and no question or recommendation put to the user**.

**Commit-and-push per task. Run the FULL guard set BEFORE the first edit (`python tools/audit/gen_guard_state.py
--check`) and again at the end (write mode, committed as the artifact of a real run). After every commit: push, then
read `.git/refs/remotes/origin/master` with the file tools and confirm it names the commit just made.** Verify every
commit at the object by explicit hash. Every shell command carries `; echo "exit:$?"`. `git status` and `git diff` over
the working tree are denied by the armed guard — use the explicit-hash forms of A1. Write every hash literally in the
command: a hash held in a shell variable is denied by the guard. Plain single-quoted `git commit -m '…'` subjects.
Every working-tree read through the file tools (D-253); a run's output is redirected to a file in your session's
scratch folder outside the repository and read with the file tools; every script this dispatch orders is written there
too and its text goes into the report. Edit files with your file-editing tool, never by retyping a whole file. **If an
old text quoted below does not occur EXACTLY once in its file, that edit is a STOP-and-report for that edit alone**:
make nothing for it and report what you found. The reserved-word rule binds every line you write: *score*, *key*,
*note*, *figure*, *register*, *measure*, *part*, *scale*, *tie* only in their musical senses, or qualified (a pack
"part" in the generator's own field name is that tool's existing identifier and stays).

## The ordered first reads

**(1)** `records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md` WHOLE;
`records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_documents_confirmation_sitting.md` WHOLE;
`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md` WHOLE. **(2)** `CLAUDE.md` at its six ruled spans (the
membership at its "Build and test commands" block), `STATUS.md` whole, `DECISIONS.md` whole; rule (a)'s `gating_ids` at
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`. **(3)** Handoff entries 410, 411 and 412,
whole. **(4)** `cowork_audit_protocol.md`'s dispatch-protocol section. **(5)** The first half: its dispatch WHOLE, its
report WHOLE, its close (the section of `records/cowork/handoff/cowork_away_returns.md` headed *THE L3 PACK BUILD,
FIRST HALF*). **(6)** `records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md` and
`records/cowork/rulings/cowork_rulings_2026_10_15_l3_first_pass_extracts_sitting.md` WHOLE. **(7)** The generator at:
its docstring, `VERDICT_DATE`, `FROZEN` whole, `CHARTER_MEMBER_7`, `LEDGER_MEMBER_9`, `EXTRAS["l2"]` at the twelve
carried parts, `WITHHELD["l2"]` and `L2_WITHHELD_DOCUMENTS`, `filter_part`, `_removal_spans`, `_cut_spans`,
`render_extra`, `criterion_block`, `cross_reference_additions`, `build_subject` WHOLE, `build()` WHOLE,
`frozen_block`, `frozen_from_disk`, `write_all`, `check_all`, `main`. **(8)** `tools/audit/l3_withheld_documents.json`
WHOLE. **(9)** `tools/audit/gen_status_batch_bound.py` whole at the object
`a01e9402fbaf034fe0d357214b67c06a8294309c:tools/audit/gen_status_batch_bound.py` before Task 5.

## The two scripts used across Tasks 1 to 4 (outside the repository working tree; not committed; their text goes into the report)

**`dump_build.py`** — writes a dump:

```python
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location(
    "dbp", r"C:\s\MS\tools\audit\gen_derivation_boot_pack.py")
dbp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dbp)
manifest, packs, displaced = dbp.build()
with open(sys.argv[1], "w", encoding="utf-8", newline="") as fh:
    fh.write(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print("dumped", sys.argv[1], "subjects:", sorted(manifest["subjects"]))
```

Run as `python <scratch>\dump_build.py <scratch>\<name>.json; echo "exit:$?"`. A `Stop` raised by `build()` ends the
script with its message: report it whole. **Nothing in it writes into the repository.**

**`diff_paths.py`** — a helper the comparison scripts below import: `diff(a, b, path="")` returns the list of every
JSON path at which two parsed values differ (recursing into dicts by key and lists by index; a missing key or a
different list length is itself a difference at that path), each with both values printed truncated to 300 characters.
Write it yourself; its text goes into the report.

## Task 0 — land the records, and PUSH

To be landed (the standing clause), each as it stands:

1. `records/cc/instructions/cc_instruction_l3_pack_build_second_half_2026_10_16.md` (this dispatch);
2. `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_ten.md`, `…four_hundred_and_eleven.md`,
   `…four_hundred_and_twelve.md`, and `…four_hundred_and_thirteen.md` if present;
3. `records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_documents_confirmation_sitting.md` and
   `records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md`;
4. `reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`.

**The acts, in order:** **(1)** A1's check. A path already tracked and unmodified is reported and not re-landed; entry
413 absent is reported, not a STOP; this dispatch or any of items 3 and 4 absent is a STOP. Report any other untracked
path the enumeration shows under `records/`, `reading_pass/` or `ratification_surfaces/` — NOT landed, not a STOP.
**(2)** If `tools/audit/gen_evidence_pin_membership.py --check` is red, regenerate
`tools/audit/evidence_pin_membership.json` and measure it against the committed blob: the only permitted change is its
list of ruling records read, gaining the two of item 3; any other movement is a STOP-and-report. **(3)** Commit the
paths that exist and are untracked or modified, plus the membership artifact only if it moved. Subject, exactly:
`record: the L3 pack-build second-half dispatch, entries 410-412, the confirmation and freeze-derivation records and the L3 extracts cut list landed`
(if entry 413 is present, write `entries 410-413`). **(4)** PUSH; verify `origin/master` at the ref file.

**Under standing clause P-2 this dispatch is PINNED at Task 0:** record its blob, and prove it unmoved immediately
before staging it.

**E0:** the named paths in one commit; `origin/master` at it; every path accounted for.

## Task 1 — the repair, then the freeze of L2's spent pack, in ONE commit

It cannot be stopped partway once its edits begin, so it goes first with nothing large in front (D-670). **The
`FROZEN["l2"]` entry is written BEFORE the tool is run in any write mode** — while `l2` is live, a write run re-renders
its directory from today's sources and overwrites the record this task exists to preserve.

**(a) PROVE THE DIRECTORY IS WHAT WAS COMMITTED.** For each of the ten files of `tools/audit/derivation_boot_pack/l2/`,
take `git hash-object <file>` and `git rev-parse a01e9402fbaf034fe0d357214b67c06a8294309c:<path>` and prove they are
equal. **A file on disk that differs from its committed blob, a file present on disk and not in the commit, or the
reverse, is a STOP-and-report and nothing is written.**

**(b) MEASURE THE TEN DIGESTS.** For each file take `git hash-object <file>` **and** `git hash-object --no-filters
<file>`, prove the two agree, and prove each equals the value in the premise ledger. **A disagreement is a
STOP-and-report.**

**(c) THE BEFORE DUMP.** With the generator untouched: `python <scratch>\dump_build.py <scratch>\B0.json`. Also take the
committed manifest: `git show a01e9402fbaf034fe0d357214b67c06a8294309c:tools/audit/derivation_boot_pack.json >
<scratch>\C.json; echo "exit:$?"`.

**(d) THE REPAIR — five edits, made in this order, and no other line touched.**

*Edit 1.1 — the authored list.* Old text (once):

```python
    # made false by that session's run.
}

# The header row of `DEFECT_TYPES.md`'s catalog table, matched exactly once.  Amendment (a3)
```

New text:

```python
    # made false by that session's run.
}

# ══════════════════════════════════════════════════════════════════════════════════════════════
# AUTHORED — WHICH PACKS WERE RENDERED BEFORE THE 2026-09-21 AND 2026-09-27 SCOPING RULINGS.
#
# Two rulings changed how a pack is built: limb B of Ruling 1 of
# `records/cowork/rulings/cowork_rulings_2026_09_21_l2_extracts_member_cutting_sitting.md` (the leak
# check over the rendered extras) and Ruling 1 of
# `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md` (the cross-reference
# rule searches `title`, `verbatim` and `plain` only).  A pack rendered BEFORE them keeps, in its
# manifest record, the shape it was built under — the five-field search and no limb-B list — so
# that the record of what its session was given does not move (the 2026-09-27 ruling's own scope
# note; D-646).  Until 2026-10-15 this tool tested that as "is in `FROZEN`", which was exact while
# the three packs frozen below were the only packs rendered before those rulings.  `l2`'s pack was
# rendered UNDER both rulings and is frozen too, so the two tests come apart, and the test is keyed
# here instead (the derivation recorded at
# `records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md`, §2).  Every
# subject named here must be in `FROZEN` — a pack cannot be rendered after its subject is frozen,
# `write_all` writing nothing into a frozen directory — and each entry carries its finding, its
# date and its reason, or the tool STOPS.
# ══════════════════════════════════════════════════════════════════════════════════════════════
RENDERED_BEFORE_THE_SCOPING_RULINGS: dict[str, dict] = {
    "harmony-boundary": {
        "finding": ("Frozen on 2026-08-31 (its `FROZEN` entry), so its pack was rendered before the "
                    "2026-09-21 and 2026-09-27 rulings."),
        "date": "2026-10-15",
        "reason": ("Its manifest record keeps the shape its pack was built under, so that the record "
                   "of what its session was given does not move (Ruling 1 of "
                   "`cowork_rulings_2026_09_27_l2_leak_list_sitting.md`, its scope note; D-646)."),
    },
    "scoring-model": {
        "finding": ("Frozen on 2026-08-31 (its `FROZEN` entry), so its pack was rendered before the "
                    "2026-09-21 and 2026-09-27 rulings."),
        "date": "2026-10-15",
        "reason": ("Its manifest record keeps the shape its pack was built under, so that the record "
                   "of what its session was given does not move (Ruling 1 of "
                   "`cowork_rulings_2026_09_27_l2_leak_list_sitting.md`, its scope note; D-646)."),
    },
    "l0-l1": {
        "finding": ("Frozen on 2026-09-04 (its `FROZEN` entry), so its pack was rendered before the "
                    "2026-09-21 and 2026-09-27 rulings."),
        "date": "2026-10-15",
        "reason": ("Its manifest record keeps the shape its pack was built under, so that the record "
                   "of what its session was given does not move (Ruling 1 of "
                   "`cowork_rulings_2026_09_27_l2_leak_list_sitting.md`, its scope note; D-646)."),
    },
}

# The header row of `DEFECT_TYPES.md`'s catalog table, matched exactly once.  Amendment (a3)
```

*Edit 1.2 — the field choice and its comment.* Old text (once):

```python
# Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md`: for every
# subject that is NOT FROZEN the rule searches only the fields member (5) renders besides the
# identifier — `title`, `verbatim`, `plain`.  A FROZEN subject keeps the five-field search its pack
# was built under, so that its manifest record — the record of what its session was given — does not
# move; the same scoping as limb B's `extras_leaks` in `build_subject` (D-657).
```

New text:

```python
# Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_09_27_l2_leak_list_sitting.md`: for every
# subject whose pack is built under that ruling the rule searches only the fields member (5) renders
# besides the identifier — `title`, `verbatim`, `plain`.  A subject named in
# `RENDERED_BEFORE_THE_SCOPING_RULINGS` keeps the five-field search its pack was built under, so that
# its manifest record — the record of what its session was given — does not move; the same scoping
# as limb B's `extras_leaks` in `build_subject` (D-657).  ★ CORRECTED by the second half of L3's
# pack build, under the 2026-10-15 derivation at
# `records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md`; FORMER
# WORDING, PRESERVED (#12): "for every subject that is NOT FROZEN the rule searches only the fields
# member (5) renders besides the identifier — `title`, `verbatim`, `plain`.  A FROZEN subject keeps
# the five-field search its pack was built under".
```

and old text (once):

```python
                                     XREF_FIELDS_FROZEN if subject in FROZEN else XREF_FIELDS)
```

New text:

```python
                                     XREF_FIELDS_FROZEN
                                     if subject in RENDERED_BEFORE_THE_SCOPING_RULINGS
                                     else XREF_FIELDS)
```

*Edit 1.3 — limb B and its comment.* Old text (once):

```python
    # an authored filter.  It runs only for a subject that is NOT FROZEN — a frozen subject's record
    # describes a directory rendered before this check existed (D-657).
    extras_leaks: list[dict] | None = None if subject in FROZEN else []
```

New text:

```python
    # an authored filter.  It runs for every subject not named in
    # `RENDERED_BEFORE_THE_SCOPING_RULINGS` — a subject named there has a record describing a
    # directory rendered before this check existed (D-657).  ★ CORRECTED by the second half of L3's
    # pack build, under the 2026-10-15 derivation at
    # `records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md`; FORMER
    # WORDING, PRESERVED (#12): "It runs only for a subject that is NOT FROZEN — a frozen subject's
    # record describes a directory rendered before this check existed (D-657)."
    extras_leaks: list[dict] | None = (
        None if subject in RENDERED_BEFORE_THE_SCOPING_RULINGS else [])
```

*Edit 1.4 — the additions' wording.* Old text (once):

```python
                if subject in FROZEN else (
```

New text:

```python
                if subject in RENDERED_BEFORE_THE_SCOPING_RULINGS else (
```

*Edit 1.5 — the STOP, in `build()`, in the docstring and in `the_STOPS`, and the ruling in `the_rulings_it_executes`.*
Old text (once):

```python
    if orphan_freeze:
        raise Stop(f"FROZEN names subject(s) this tool does not build: {orphan_freeze}")
```

New text:

```python
    if orphan_freeze:
        raise Stop(f"FROZEN names subject(s) this tool does not build: {orphan_freeze}")
    # STOP 13: the authored list of packs rendered before the scoping rulings names only FROZEN
    # subjects, and each entry carries its finding, its date and its reason (the 2026-10-15
    # derivation).
    not_frozen = sorted(set(RENDERED_BEFORE_THE_SCOPING_RULINGS) - set(FROZEN))
    if not_frozen:
        raise Stop(f"RENDERED_BEFORE_THE_SCOPING_RULINGS names subject(s) that are not FROZEN: "
                   f"{not_frozen}")
    for s, r in sorted(RENDERED_BEFORE_THE_SCOPING_RULINGS.items()):
        for f in ("finding", "date", "reason"):
            if not r.get(f):
                raise Stop(f"the entry for {s!r} in RENDERED_BEFORE_THE_SCOPING_RULINGS lacks its {f}")
```

Old text (once), in the docstring:

```python
     does not hold a file this tool renders for it STOPS it, because the manifest cannot describe
     a file that is not there.
```

New text:

```python
     does not hold a file this tool renders for it STOPS it, because the manifest cannot describe
     a file that is not there;
 13. an entry of `RENDERED_BEFORE_THE_SCOPING_RULINGS` naming a subject that is not FROZEN, or
     lacking its finding, its date or its reason, STOPS it (the 2026-10-15 derivation).
```

Old text (once):

```python
            "a subject with graded candidates and no authored date in `VERDICT_DATE`",
        ],
```

New text:

```python
            "a subject with graded candidates and no authored date in `VERDICT_DATE`",
            "an entry of `RENDERED_BEFORE_THE_SCOPING_RULINGS` naming a subject that is not FROZEN, "
            "or lacking its finding, its date or its reason",
        ],
```

Old text (once):

```python
            "rule searches only the fields member (5) renders, for every subject that is not "
            "FROZEN.",
        ],
```

New text:

```python
            "rule searches only the fields member (5) renders, for every subject that is not "
            "FROZEN.",
            "The derivation recorded at "
            "`records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md`, "
            "applying Ruling 1 of `cowork_rulings_2026_09_27_l2_leak_list_sitting.md` as ruled — the "
            "field choice, limb B and the additions' wording keyed on the authored list "
            "`RENDERED_BEFORE_THE_SCOPING_RULINGS` rather than on FROZEN membership — and the freeze "
            "of the spent `l2` pack (Ruling 1 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, "
            "noted).",
        ],
```

**After the five edits, `subject in FROZEN` must occur in `build_subject` nowhere** — search the function and report
the result (expected: no hit).

**(e) THE REPAIR IS INERT BEFORE THE FREEZE.** `python <scratch>\dump_build.py <scratch>\B1.json`. A script (outside the
working tree, importing `diff_paths.py`) proves and prints: `diff(B0.subjects, B1.subjects)` is EMPTY; every top-level
key of B0 and B1 is the same set; every top-level value except `the_STOPS` and `the_rulings_it_executes` is equal;
`B1.the_STOPS == B0.the_STOPS + [the one string Edit 1.5 adds]` and `B1.the_rulings_it_executes ==
B0.the_rulings_it_executes + [the one string Edit 1.5 adds]`. **Anything else is a STOP: restore the generator with
`git checkout a01e9402fbaf034fe0d357214b67c06a8294309c -- tools/audit/gen_derivation_boot_pack.py; echo "exit:$?"`,
commit nothing in this task, and go to Task 5 (the close), whose report says the batch stopped here.**

**(f) THE FROZEN ENTRY.** Old text (once — Edit 1.1 kept these two lines and added no other copy of them):

```python
    # made false by that session's run.
}
```

Insert, between the comment line and the `}`, the new entry `"l2": {…}` in the shape the `l0-l1` entry uses: its
`digests` the ten values of (b) keyed by file name in the order the premise ledger lists them, and three authored
fields **quoted verbatim from here and composed by you not at all** — they are the first half's Task 1(c) texts,
unchanged:

- `finding`: *"Its deriving session has RUN (Ruling 1 of
  `records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, noted), and the specification it
  produced, `cowork_derived_specification_l2_2026_10_10.md`, was ratified face by face on 2026-10-13 and 2026-10-14.
  The pack is STALE against today's sources — its rendered charter member lacks the 2026-10-14 amendment to L2's block
  of `FRAMEWORK.md` §5 — so the digests recorded here are those of the files on disk, proved equal to their committed
  blobs: what the session was given, and not a re-render."*
- `date`: *"2026-10-15"*
- `reason`: *"A spent subject's pack is the record of what its session was given rather than an input to be kept
  current (Ruling 17(a); D-646). Left live it would re-render the charter member with an amendment ruled after the
  session ran, and so back-date into a completed derivation's record a text its session never read (#12); and L3's
  pack shares the charter member with it (`CHARTER_MEMBER_7`), so it must be frozen before L3's is built (the boot-list
  record's Ruling 1, noted). Frozen at the blobs it carries, with the hash STOP."*

followed, inside the table and after the entry, by this comment, verbatim:

```python
    # `l2` IS FROZEN ABOVE, ITS DERIVING SESSION HAVING RUN; its own ground is in its own entry and is
    # not restated here (#6).  Frozen by the second half of L3's pack build, after the test for a
    # pack rendered before the scoping rulings was keyed on its own authored list below.
```

*(This comment is the first half's comment with its last sentence changed: that sentence read "Frozen 2026-10-15 by
the first half of L3's pack build.", which would be false of this act. The `finding`, `date` and `reason` above are
the first half's unchanged, as entry 411 §3 item 2 orders; `date` is the date the freeze was decided.)*

**`l2` is NOT added to `RENDERED_BEFORE_THE_SCOPING_RULINGS`**: its pack was rendered under both rulings.

**(g) THE D-657 COMPARISON — the one the derivation orders, before half from the committed manifest at an explicit
hash.** `python <scratch>\dump_build.py <scratch>\B2.json`. A script (outside the working tree) loads `C.json`,
`B1.json`, `B2.json`, imports the EDITED generator as `dbp` exactly as `dump_build.py` does, and defines
`T(rec) = r = copy.deepcopy(rec); r["★_FROZEN"] = dbp.frozen_block("l2"); dbp.frozen_from_disk("l2", r); return r` —
which is exactly what `build()` does to a frozen subject's record, in the same order. It proves and prints:

1. **Against the committed manifest (the governing comparison):** for each of `harmony-boundary`, `scoring-model` and
   `l0-l1`, `diff(C.subjects[s], B2.subjects[s])` is EMPTY; and `diff(T(C.subjects["l2"]), B2.subjects["l2"])` is
   EMPTY.
2. **Against the repaired build before the freeze:** for the same three, `diff(B1.subjects[s], B2.subjects[s])` is
   EMPTY; `diff(T(B1.subjects["l2"]), B2.subjects["l2"])` is EMPTY; every top-level value of B1 and B2 except
   `subjects` is equal.

**Expected:** every listed diff EMPTY. **Whether item 1's `l2` comparison is empty is UNMEASURED** — the premise
ledger's named risk (`LEAKS_IN_THE_EXTRAS` line numbers in member (7) moving with the changed charter) and any count
over today's inputs that has moved since 2026-09-27 would show there. **Any non-empty diff is a STOP with nothing
committed:** print every differing path with both values; restore the generator with `git checkout
a01e9402fbaf034fe0d357214b67c06a8294309c -- tools/audit/gen_derivation_boot_pack.py; echo "exit:$?"`; confirm at the
object that the tracked file equals that blob; commit nothing in this task; go to Task 5, whose report puts the whole
diff at its head under the heading `TASK 1 STOPPED — THE L2 FREEZE MOVES L2's RECORD BEYOND THE FROZEN SHAPE`. The
derivation's own bound applies: what the repair is then is the user's (D-436, D-657), and no fix is taken.

**(h) REGENERATE AND CHECK.** Only after (g) is wholly empty: `python tools/audit/gen_derivation_boot_pack.py >
<scratch>\dbp_t1_write.txt 2>&1; echo "exit:$?"` (write mode, no `--subject`; with all four subjects frozen,
`write_all` writes the manifest and no pack directory). Prove the written manifest is byte-identical to `B2.json`.
Then `--check` to `<scratch>\dbp_t1_check.txt` and report its whole output and exit code — **expected:** *"the
derivation boot pack re-derives"*, four `FROZEN — N file(s) at their recorded blobs` lines, exit 0; a red result is
reported with its lines, and is a STOP only if a line names a frozen subject's file or digest. **Prove at the object
that no file of any of the four pack directories moved** — every file compared against the tip's blob by explicit hash.

**Commit exactly these two paths:** `tools/audit/gen_derivation_boot_pack.py` and `tools/audit/derivation_boot_pack.json`.
Subject, exactly: `key the pre-scoping-rulings test on an authored list, then freeze the l2 boot pack at its rendered blobs`.
Push; verify. Publish the deleted-line enumeration for the generator: every deleted line must be inside an old text
this task quotes.

**E1:** the ten files proved equal to their committed blobs; the ten digests taken twice, agreeing, and equal to the
premise ledger's; (e) and (g) wholly empty; the manifest equal to B2; `--check` as reported; every pack directory
byte-unchanged; one commit, pushed.

## Task 2 — `VERDICT_DATE["l3"]` and the criterion bullet, in ONE commit

**This is the first half's Task 2, (b) to (d), performed exactly as written there** — Edit 1 (the date), Edit 2 (the
stale sentence under *THE DATE* in `VERDICTS["l3"]`'s opening comment) and Edit 3 (the criterion bullet, in its two
places) — **every old text and new text taken from that dispatch's Task 2 without change**, except two substitutions,
because the edits are made by this batch and not on 2026-10-15: in Edit 2's new text, *"★ CORRECTED 2026-10-15 by the
first half of L3's pack build;"* is written *"★ CORRECTED by the second half of L3's pack build;"*; in Edit 3's comment,
*"(2026-10-15, the first half of L3's pack build; owed since entry 398 §2)"* is written *"(the second half of L3's pack
build; owed since entry 398 §2)"*. Edit 1's comment is unchanged (its dates are the authoring and ruling dates). The writing side found each of the old texts at the generator once
(*"THE DATE.  Ruling 2 requires"* at its comment; *"The candidate criterion is a PATTERN MATCH over the rulings sort and
the decisions "*; *"its `group` is E — Layer 2, the slicer",*).

**(a)** Before the edits: `python <scratch>\dump_build.py <scratch>\B3.json`.

**(e)** After the edits: `python <scratch>\dump_build.py <scratch>\B4.json`. A script proves and prints: every
top-level value of B3 and B4 is equal except `subjects`; `diff(B3.subjects[s], B4.subjects[s])` is EMPTY for
`harmony-boundary`, `scoring-model` and `l0-l1`; and for `l2`, the JSON text of `B3.subjects["l2"]` with the
JSON-escaped string `its `group` is E — Layer 2, the slicer` replaced, **exactly once**, by `its `group` is one of the
register groups listed under `the_groups` below` parses to a value whose `diff` against `B4.subjects["l2"]` is EMPTY.
Report how many times the old bullet occurred in `B3.subjects["l2"]` (expected: once). **Expected, and why it is
admitted:** `l2`'s frozen record changes in that one bullet line, which was false of `l2` (six groups, not group E
alone); correcting it is a staleness fix under the user's rule of 2026-09-22, and it moves no withheld set and no file
(entry 411 §3 item 3). **Anything else is a STOP-and-report and nothing is committed.** `VERDICT_DATE["l3"]` is read
only by `build_subject("l3", …)`, which no build reaches before Task 3; its inertness is shown by this comparison.

Then regenerate the manifest in write mode (no pack directory is written, all four subjects being frozen), prove it
byte-identical to `B4.json`, and run `--check` (expected exit 0).

**Commit exactly** `tools/audit/gen_derivation_boot_pack.py` and `tools/audit/derivation_boot_pack.json`. Subject,
exactly: `l3 verdict date and the criterion group bullet derived from the authored groups`. Push; verify.

**E2:** the three edits as written; the comparison as expected; the deleted-line enumeration published, every deleted
line inside the quoted old texts.

## Task 3 — `WITHHELD["l3"]` and `EXTRAS["l3"]`, authored together; committed with Task 4's render

**(a) The confirmed documents.** Old text (once):

```python
WITHHELD: dict[str, dict] = {
    "harmony-boundary": {
```

New text:

```python
# ── L3's withheld documents — the set the user CONFIRMED on 2026-10-15 ───────────────────────────
# Ruling 5 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md` orders the set DERIVED (the home
# documents of the entries `VERDICTS["l3"]` grades IN), printed, and confirmed before it is
# authored; Ruling 1 of `cowork_rulings_2026_10_15_l3_withheld_documents_confirmation_sitting.md`
# confirms it (his word: "yes").  The names are those of `tools/audit/l3_withheld_documents.json` →
# `documents`, in its order; the identities homed in each are that artifact's and are not restated
# here (D-431).
L3_WITHHELD_DOCUMENTS: tuple[str, ...] = (
    "ARCHITECTURE.md",
    "cowork_joint_estimator_architecture.md",
    "cowork_layer5_function_design.md",
    "cowork_layer6_grouping_design.md",
    "cowork_phrase_boundary_design.md",
)

WITHHELD: dict[str, dict] = {
    "harmony-boundary": {
```

**(b) The `l3` entry of `WITHHELD`.** Old text (once):

```python
    # THE `framework` SUBJECT IS ABSENT DELIBERATELY, not by oversight: its deriving session is
```

New text — the entry inserted before that comment, the comment line itself unchanged:

```python
    # ── L3, THE THIRD DERIVING SUBJECT OF THE DETAIL-SPECIFICATION PHASE ────────────────────────
    # The pack's members by Rulings 1 to 5 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md`.
    #
    # THE IDENTITIES ARE NOT WRITTEN HERE: `build_subject` withholds every candidate
    # `VERDICTS["l3"]` grades IN — the family the rulings of
    # `cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md` fixed.
    #
    # NO `withheld_passages`: Ruling 4 of the boot-list record — no passage of `CLAUDE.md` is
    # withheld for L3.  NO `the_identity_the_ruling_names`: no ruling names one for L3.
    "l3": {
        # Built from the L3 block of `FRAMEWORK.md` §5 (heading "L3 — The read-off facts"): its
        # "Question" line verbatim and its "Publishes" line without its markup, joined by the words
        # "It publishes".
        "the_subject_in_plain_words":
            "L3, the read-off facts: given a settled tonal reading, what else does a harmonic "
            "analysis of this music say? It publishes the cadence at each phrase end, with its "
            "type; the phrase and section grouping; the chord symbol — root pitch class, quality "
            "and bass note; the figured bass; the harmonic rhythm.",
        "the_oracle_this_family_protects": (
            "NO ORACLE PASSAGE IS NAMED FOR L3. Ruling 1 of "
            "`cowork_rulings_2026_10_14_l3_withheld_family_sitting.md` orders a withheld family "
            "so that the deriving session's answer can be told apart from recall, and names no "
            "oracle passage. What the family protects is therefore the entries themselves: the "
            "recorded current answers to L3's question — the cadence at each phrase end and its "
            "type, the phrase and section grouping, the chord symbol, the figured bass and the "
            "harmonic rhythm. Those are the identities `VERDICTS[\"l3\"]` grades IN; the documents "
            "below are their homes."),
        "withheld_documents": {
            doc: {
                "finding": (
                    "A home document of entries the ruled L3 verdict table grades IN, derived "
                    "under Ruling 5 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md` and "
                    "confirmed by Ruling 1 of "
                    "`cowork_rulings_2026_10_15_l3_withheld_documents_confirmation_sitting.md`; the "
                    f"identities homed in `{doc}` are listed at "
                    "`tools/audit/l3_withheld_documents.json` -> `documents`."),
                "date": "2026-10-15",
                "reason": (
                    "Confirmed by the user (his word: \"yes\"). A deriving session that opened the "
                    "document would read the ruled answers its IN entries carry, so its name "
                    "becomes a leak string for members (5) and (6) and for the extras, and a "
                    "design-intent entry whose own text names it is withheld with it."),
            }
            for doc in L3_WITHHELD_DOCUMENTS
        },
        "withheld_passages": [],
    },

    # THE `framework` SUBJECT IS ABSENT DELIBERATELY, not by oversight: its deriving session is
```

**(c) The `l3` entry of `EXTRAS`.** It is inserted after the `l2` entry, as the last entry of the dict. Old text (once):

```python
        LEDGER_MEMBER_9,
    ],
}
```

(The same first two lines also close `l0-l1`'s entry, but there they are followed by `    "l2": [`, not by `}`, so
the three lines together occur once — at the end of `EXTRAS`, read by the writing side.) New text: the same lines,
with this inserted between `    ],` and `}`:

```python
    "l3": [
        CHARTER_MEMBER_7,
        {
            "number": 8,
            "filename": "08_the_seventeen_research_extracts.md",
            "title": "Seventeen published sources, read at the object — the L3 slice and the "
                     "first-pass extracts that bear on it",
            "source": "reading_pass/extracts/ — the first extractions of the six L3-slice rows (36, "
                      "37, 38 and 39, with 34 and 40 carried from L2's slice; Ruling 3 (i) of "
                      "`cowork_rulings_2026_10_15_l3_boot_list_sitting.md`) and the eleven "
                      "first-pass extracts admitted by Ruling 1 of "
                      "`cowork_rulings_2026_10_15_l3_first_pass_extracts_sitting.md`",
            "rendered_from": "the seventeen files themselves, quoted whole, each with the sections "
                             "and passages stating this project's own positions cut PER FILE "
                             "(Ruling 1 of 2026-09-21, limb A), the ruled shared cut strings "
                             "unchanged, and L2's filters carried unchanged for the twelve files "
                             "L2's member (8) already holds; the per-file list is "
                             "`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`",
            "parts": [
                # … the seventeen parts, in the order and with the contents (d) gives …
            ],
        },
        LEDGER_MEMBER_9,
    ],
```

**(d) The seventeen parts.** Write them in the order of `"order"` in the JSON object below. Every part is
`{"source": <path>, "spans": [{"kind": "whole"}], "removals": [...], "cuts": [...]}`, written in the multi-line dict
style the `l2` parts use, `true` written `True`.

- **A carried part** (its path is a key of `"carried"`): copy, **from the generator's own text**, every filter-entry
  dict of `EXTRAS["l2"]`'s member (8) part whose `"source"` line is that path — its `removals` items and its `cuts`
  items, **verbatim, in L2's order, with nothing changed, `why` strings included** — then append, after L2's
  `removals`, the dicts of `"removals_added"`, and after L2's `cuts`, the dicts of `"cuts_added"`, in the order given.
  The writing side found each of the twelve `"source"` lines once in `EXTRAS["l2"]`. **Copy the L2 entries from the
  file, not from memory and not from this dispatch** — this dispatch does not restate them.
- **A new part** (its path is a key of `"new"`): its `removals` and `cuts` are exactly the lists given.

**The authority is this JSON object.** Write it, byte for byte, to `<scratch>\l3_member8_expected.json`; the check at
(e) compares the generator against it, so a Python literal that does not equal it is caught there.

```json
{
 "order": [
  "reading_pass/extracts/ju-margot-mckay-dahn-fujinaga-2020-automatic-figured-bass-annotation-bach-chorales-figured-bass-dataset.md",
  "reading_pass/extracts/bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md",
  "reading_pass/extracts/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md",
  "reading_pass/extracts/sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md",
  "reading_pass/extracts/illescas-rizo-inesta-2007-harmonic-melodic-and-functional-automatic-analysis.md",
  "reading_pass/extracts/declercq-2015-a-model-for-scale-degree-reinterpretation.md",
  "reading_pass/extracts/feisthauer-2021-lille-thesis-modulations-cadences-sonata-form.md",
  "reading_pass/extracts/hamanaka-hirata-tojo-2013-computational-music-theory-gttm.md",
  "reading_pass/extracts/lazzari-2023-knowledge-based-chord-embeddings-modal-harmony-ontology.md",
  "reading_pass/extracts/napoleslopez-feisthauer-leve-fujinaga-2020-local-keys-modulations-tonicizations.md",
  "reading_pass/extracts/mcleod-rohrmeier-2021-modular-harmonic-analysis.md",
  "reading_pass/extracts/bachi-2026-boundary-aware-symbolic-chord-recognition.md",
  "reading_pass/extracts/hentschel-moss-mcleod-neuwirth-rohrmeier-2021-unified-chord-model.md",
  "reading_pass/extracts/mcleod-rohrmeier-2024-chord-tone-alterations-suspensions.md",
  "reading_pass/extracts/sapp-2005-visual-hierarchical-key-analysis.md",
  "reading_pass/extracts/dehaas-magalhaes-wiering-veltkamp-2013-harmtrace-functional-analysis.md",
  "reading_pass/extracts/deberardinis-etal-2023-choco-chord-corpus.md"
 ],
 "new": {
  "reading_pass/extracts/ju-margot-mckay-dahn-fujinaga-2020-automatic-figured-bass-annotation-bach-chorales-figured-bass-dataset.md": {
   "removals": [
    {"anchor": "**STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-10-14).** Written under",
     "opens_with": "> ",
     "closes_with": "open-items row or decisions-register entry.**",
     "why": "the opening status block above the first heading: candidacy row, slice placement, handoff entries, independence bookkeeping"},
    {"anchor": "`docs/research_papers/ju_margot_mckay_dahn_fujinaga_2020_ismir_bcfb_figured_bass.pdf`",
     "opens_with": "**File:**",
     "closes_with": "(1,022,218 bytes at the staging result).",
     "why": "the Identity section's file line: a repository path and a staging figure"},
    {"anchor": "the printed word is \"obbligato\". Former wording, preserved (#12): \"obligato\"",
     "opens_with": " *(★ CORRECTED 2026-10-15 at the cross-check against the second extract",
     "closes_with": "\"obligato\".)*",
     "why": "a correction-of-record note"},
    {"anchor": "This bears on guiding principle #20, fit/evaluation separation",
     "opens_with": " *(",
     "closes_with": "cross-validated.)*",
     "why": "this project's principle #20 applied to the paper's figure"},
    {"anchor": "the paper says \"one octave apart\", not \"an octave or more\"",
     "opens_with": " *(★ CORRECTED 2026-10-15 at the cross-check against the second",
     "closes_with": "22\".)*",
     "why": "a correction-of-record note"}
   ],
   "cuts": [
    {"heading_contains": "detail specification could adopt, adapt, or must argue against", "heading_level": "## ",
     "why": "the ruled shared cut string, unchanged (Ruling 2 of 2026-09-05; Ruling 1 of 2026-09-20; Ruling 1 of 2026-09-21)"},
    {"heading_contains": "★ Findings, routed and not applied", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "Centrality", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "What this extract does NOT do", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "The read-back, recorded", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "The cross-check against the second extract (2026-10-15)", "heading_level": "## ", "runs_to_end": true,
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"}
   ]
  },
  "reading_pass/extracts/bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md": {
   "removals": [
    {"anchor": "**STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under",
     "opens_with": "> ",
     "closes_with": "> #12.)*",
     "why": "the opening status block: candidacy row, V6, DP-I, Ruling 10, correction-of-record notes and a ruling"},
    {"anchor": "that make this L1's paper",
     "opens_with": " ",
     "closes_with": "L1's paper",
     "why": "the `###` heading's trailing words placing the paper in this project's L1; the heading `### ★ The two exclusions` is kept"},
    {"anchor": "`docs/research_papers/bigo_feisthauer_giraud_leve_2018_ismir_cadence_detection_features.pdf`",
     "opens_with": "**File:**",
     "closes_with": "cadence_detection_features.pdf`.",
     "why": "the Identity section's file line: a repository path"},
    {"anchor": "The feature that IS the L1 charter's third cue.",
     "opens_with": " ",
     "closes_with": "third cue.",
     "why": "a bold label tying the paper's feature to this project's L1 charter; `**★ [FACT, §2.1]**` is kept"},
    {"anchor": "the dropped condition is what separates the two features",
     "opens_with": " *(★ CORRECTED 2026-09-20 ON THE USER'S RULING.",
     "closes_with": "the feature whose implied tonality has Z's bass as its tonic.)*",
     "why": "a correction-of-record note"},
    {"anchor": "prints \"hard-coded\", places \"but\" before \"with\"",
     "opens_with": "*(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED (#12): \"Note that we previously",
     "closes_with": "the citation \"[9]\".)*",
     "why": "a correction-of-record note"},
    {"anchor": "— and it is the framework's own sentence",
     "opens_with": " ",
     "closes_with": "own sentence",
     "why": "a bold label tying the paper's sentence to this project's framework"},
    {"anchor": "and the Table 4 values now given beside the quotation do not bear it",
     "opens_with": " *(★ CORRECTED 2026-09-20 ON THE USER'S RULING. FORMER WORDING, PRESERVED (#12):",
     "closes_with": "and R lowers Haydn PAC.)*",
     "why": "a correction-of-record note"},
    {"anchor": "the page trains PAC and PAC+rIAC on the Bach corpus",
     "opens_with": " *(★ CORRECTED 2026-09-20. FORMER WORDING, PRESERVED",
     "closes_with": "no rIAC-only classifier was met in the pages as read)*",
     "why": "a correction-of-record note"},
    {"anchor": "\"Suspensions were expected to be significant for both PAC and HC and\"",
     "opens_with": " *(★ CORRECTED 2026-09-20. FORMER WORDING,",
     "closes_with": "they do not appear significantly in these corpora.\")*",
     "why": "a correction-of-record note"}
   ],
   "cuts": [
    {"heading_contains": "detail specification could adopt, adapt, or must argue against", "heading_level": "## ",
     "why": "the ruled shared cut string, unchanged (Ruling 2 of 2026-09-05; Ruling 1 of 2026-09-20; Ruling 1 of 2026-09-21)"},
    {"heading_contains": "★ Findings, routed and not applied", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "Centrality", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "What this extract does NOT do", "heading_level": "## ", "runs_to_end": true,
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"}
   ]
  },
  "reading_pass/extracts/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md": {
   "removals": [
    {"anchor": "**STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under",
     "opens_with": "> ",
     "closes_with": "> for the act; the ground is the second extract's §9.4 and §5.",
     "why": "the opening status block: candidacy row, V6, Ruling 10, correction-of-record notes and a ruling"},
    {"anchor": "`docs/research_papers/karystinaios_widmer_2022_arxiv_cadence_detection_gnn.pdf`",
     "opens_with": "**File:**",
     "closes_with": "cadence_detection_gnn.pdf`.",
     "why": "the Identity section's file line: a repository path"},
    {"anchor": "that is, row 37's.",
     "opens_with": " —",
     "closes_with": "row 37's.",
     "why": "a pointer to this project's row 37"},
    {"anchor": "§3.1's text names the time signature",
     "opens_with": "*(★ CORRECTED 2026-09-20 — a locator added",
     "closes_with": "with no locator.)*",
     "why": "a correction-of-record note"},
    {"anchor": "The deliberate weakening of row 37's frame, and its stated purpose.",
     "opens_with": " ",
     "closes_with": "its stated purpose.",
     "why": "a bold label naming this project's row 37; `**★ [FACT, §3.1]**` is kept"},
    {"anchor": "preserved (#12): \"no assumptions and reference to\"",
     "opens_with": "*(★ CORRECTED 2026-09-20 — the page prints \"no assumptions on and reference to\"",
     "closes_with": "\"no assumptions and reference to\".)*",
     "why": "a correction-of-record note"},
    {"anchor": "preserved (#12): \"three different scales, note-wise,",
     "opens_with": "*(★ CORRECTED 2026-09-20 — the page prints \"three different levels",
     "closes_with": "onset-wise and beat-wise (the latter\".)*",
     "why": "a correction-of-record note"},
    {"anchor": "the reference model's Bach PAC precision 0.89",
     "opens_with": "*(★ CORRECTED 2026-09-20 — four bold marks",
     "closes_with": "digit changed.)*",
     "why": "a correction-of-record note"},
    {"anchor": "preserved (#12): \"on Bach fugues\"",
     "opens_with": " *(★ CORRECTED 2026-09-20 — the page prints \"in Bach",
     "closes_with": "\"on Bach fugues\".)*",
     "why": "a correction-of-record note"},
    {"anchor": "independent replication.\" — the page describes a different method",
     "opens_with": "*(★ CORRECTED 2026-09-20 ON THE USER'S RULING. Former wording, preserved (#12): \"★ [FACT, §6.1] The",
     "closes_with": "independent replication.)*",
     "why": "a correction-of-record note"},
    {"anchor": "the quotation had closed with a full stop mid-sentence",
     "opens_with": "*(★ CORRECTED 2026-09-20 —",
     "closes_with": "emerging in the learning model.\"*\".)*",
     "why": "a correction-of-record note"},
    {"anchor": "§6.2 works three examples, not one",
     "opens_with": "*(★ CORRECTED 2026-09-20 — two places in this paragraph.",
     "closes_with": "considerations\".)*",
     "why": "a correction-of-record note"},
    {"anchor": "which the L0 contract also gives",
     "opens_with": ",",
     "closes_with": "never as a fact about the tonality",
     "why": "this project's L0 contract and its key-signature rule, stated beside the paper's input"},
    {"anchor": "\"No chord segmentation, no harmonic analysis, no",
     "opens_with": "*(★ CORRECTED 2026-09-20 — a negative given its bound: the page describes",
     "closes_with": "decided tonality —\".)*",
     "why": "a correction-of-record note"},
    {"anchor": "\"Nothing else: no chord, no key, no segmentation.\"",
     "opens_with": " *(★ CORRECTED 2026-09-20 — a negative given its bound. Former",
     "closes_with": "no segmentation.\")*",
     "why": "a correction-of-record note"},
    {"anchor": "\"Pre-training on a second dataset is required for the best",
     "opens_with": "*(★ CORRECTED 2026-09-20 — two places: a claim wider than Table 2",
     "closes_with": "cannot reach form-level judgements, by design.\")*",
     "why": "a correction-of-record note"}
   ],
   "cuts": [
    {"heading_contains": "detail specification could adopt, adapt, or must argue against", "heading_level": "## ",
     "why": "the ruled shared cut string, unchanged (Ruling 2 of 2026-09-05; Ruling 1 of 2026-09-20; Ruling 1 of 2026-09-21)"},
    {"heading_contains": "★ Findings, routed and not applied", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "Centrality", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "What this extract does NOT do", "heading_level": "## ", "runs_to_end": true,
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"}
   ]
  },
  "reading_pass/extracts/sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md": {
   "removals": [
    {"anchor": "**STATUS: FIRST-PASS EXTRACT, READ WHOLE AT THE OBJECT (2026-08-31).** Written under",
     "opens_with": "> ",
     "closes_with": "> changed.",
     "why": "the opening status block: candidacy row, the doubt default, Ruling 10, the cross-check bookkeeping"},
    {"anchor": "FORMER WORDING, PRESERVED (#12): \"*Journal of New Music Research* **47:1**",
     "opens_with": " *(★ CORRECTED 2026-10-15 at the",
     "closes_with": "The \"published online\" date matches the download stamp.)*",
     "why": "a correction-of-record note in the Identity section"},
    {"anchor": "`docs/research_papers/sears_pearce_caplin_mcadams_2018_jnmr_cadence_expectations.pdf`",
     "opens_with": "**File:**",
     "closes_with": "cadence_expectations.pdf`.",
     "why": "the Identity section's file line: a repository path"},
    {"anchor": "added 2026-10-15 at the cross-check:**",
     "opens_with": ",",
     "closes_with": "at the cross-check",
     "why": "a dating of this project's correction inside a bold label; the bound itself, read from the paper's Table 5, is kept"}
   ],
   "cuts": [
    {"heading_contains": "★ The doubt-default question, answered", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "detail specification could adopt, adapt, or must argue against", "heading_level": "## ",
     "why": "the ruled shared cut string, unchanged (Ruling 2 of 2026-09-05; Ruling 1 of 2026-09-20; Ruling 1 of 2026-09-21)"},
    {"heading_contains": "★ Findings, routed and not applied", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "Centrality", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"},
    {"heading_contains": "What this extract does NOT do", "heading_level": "## ", "runs_to_end": true,
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"}
   ]
  },
  "reading_pass/extracts/deberardinis-etal-2023-choco-chord-corpus.md": {
   "removals": [
    {"anchor": "**Establishment bound:** read 2026-08-30 via one prompted extraction call over the open full",
     "opens_with": "> ",
     "closes_with": "(route in the fetched content record).",
     "why": "the opening status block: this pass's retrieval bookkeeping"}
   ],
   "cuts": [
    {"heading_contains": "Bearing", "heading_level": "## ",
     "why": "the ruled shared cut string, unchanged (Ruling 2 of 2026-09-05; Ruling 1 of 2026-09-20; Ruling 1 of 2026-09-21)"},
    {"heading_contains": "Verification targets touched", "heading_level": "## ", "runs_to_end": true,
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"}
   ]
  }
 },
 "carried": {
  "reading_pass/extracts/illescas-rizo-inesta-2007-harmonic-melodic-and-functional-automatic-analysis.md": {
   "removals_added": [
    {"anchor": "not fetched, §9)",
     "opens_with": " (",
     "closes_with": "§9)",
     "why": "this read's own act, inside §3"},
    {"anchor": "row 7); results",
     "opens_with": ",",
     "closes_with": "row 7",
     "why": "this project's row number beside the paper's reference [13]; \"(Temperley & Sleator)\" is kept"},
    {"anchor": "and what this read did NOT do",
     "opens_with": ",",
     "closes_with": "did NOT do",
     "why": "the §9 heading's trailing words; \"## 9. What the paper does NOT claim\" is kept"},
    {"anchor": "fetch the online results report, the rule set at the authors' URL",
     "opens_with": "**This read did not**",
     "closes_with": "where they last stood read.",
     "why": "§9's second paragraph: this read's own bookkeeping; the paragraph on what the paper does not claim is kept"}
   ],
   "cuts_added": [
    {"heading_contains": "0. What this row is, taken from its own rows and not from any summary", "heading_level": "## ",
     "why": "Limb A of Ruling 1 of 2026-09-21: project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"}
   ]
  },
  "reading_pass/extracts/declercq-2015-a-model-for-scale-degree-reinterpretation.md": {
   "removals_added": [
    {"anchor": "§9.3 (a), under the standing rule of handoff entry 198 §7",
     "opens_with": " *(★ CORRECTED 2026-09-19 at the second extract's cross-check",
     "closes_with": "related key area\" — the page prints the hyphen.)*",
     "why": "a correction-of-record note, claim (7)"},
    {"anchor": "its §9.3 (e), under the standing rule",
     "opens_with": " *(★ CORRECTED 2026-09-19 at the second extract's cross-check,",
     "closes_with": "No value is changed.)*",
     "why": "a correction-of-record note, claim (10)"},
    {"anchor": "his words, \"I agree with recommendation A\" — the second extract's §9.4 (f)",
     "opens_with": " *(★ CORRECTED 2026-09-19 ON THE USER'S",
     "closes_with": "image.)*",
     "why": "a correction-of-record note and a ruling, claim (10)"},
    {"anchor": "§9.3 (b), under the standing rule of handoff entry 198 §7",
     "opens_with": " *(★ CORRECTED 2026-09-19 at the second extract's cross-check, its",
     "closes_with": "and its close is now carried.)*",
     "why": "a correction-of-record note, claim (13)"},
    {"anchor": "said the paper \"takes the second position operationally\"",
     "opens_with": " *(★ This sentence's first writing",
     "closes_with": "accidentals is why it can.)*",
     "why": "a correction-of-record note, claim (15)"},
    {"anchor": "and it bears on a live grading convention",
     "opens_with": ",",
     "closes_with": "grading convention",
     "why": "the claim label's trailing words pointing at this project's grading convention"},
    {"anchor": "this quotation is this extract's emphasis; the page prints the sentence without it",
     "opens_with": " *(★ REMARK ADDED 2026-09-19 at the second",
     "closes_with": "measure agreement with an annotator rather than predictive value.",
     "why": "claim (15a)'s remark and the paragraph after it: D-211, CLAUDE.md, and this project's two key columns"},
    {"anchor": "added by the whole reading of this extract",
     "opens_with": ",",
     "closes_with": "extract",
     "why": "the claim (19) label's trailing words: this extract's own history"},
    {"anchor": "Recorded as DATA and routed nowhere",
     "opens_with": " *(★ REMARK ADDED 2026-09-19, the second extract's §9.3 (d):",
     "closes_with": "and no transfer is claimed here.**",
     "why": "claim (19)'s remark and the routing sentence after it, which names D-522"},
    {"anchor": "NOT ADMITTED, and `BIBLIOGRAPHY.md` line 38 records",
     "opens_with": " **That work is candidacy row 24",
     "closes_with": "took the same course.)*",
     "why": "claim (20)'s tail: candidacy row, bibliography line, #1 and row 7"},
    {"anchor": "the bold on \"Figure 5\" is this extract's emphasis",
     "opens_with": "*(★ REMARK",
     "closes_with": "No word is changed.)*",
     "why": "claim (21)'s remark"},
    {"anchor": "\"five or six\"; the whole reading counted",
     "opens_with": " *(★ The first writing of this line read",
     "closes_with": "it is five in each.)*",
     "why": "a correction-of-record note in Coupling facts"}
   ],
   "cuts_added": []
  },
  "reading_pass/extracts/feisthauer-2021-lille-thesis-modulations-cadences-sonata-form.md": {
   "removals_added": [
    {"anchor": "the same PAC/HC gap as V6's two verified primaries",
     "opens_with": " —",
     "closes_with": "at this thesis's own corpora.",
     "why": "the V6 clause in the claims (first-pass record §2.3); the V6 clause in the verification section goes with L2's last-section cut"}
   ],
   "cuts_added": []
  },
  "reading_pass/extracts/hamanaka-hirata-tojo-2013-computational-music-theory-gttm.md": {
   "removals_added": [
    {"anchor": "`external resarch summary/Computational Music Theory and Its.pdf` —",
     "opens_with": "**File as supplied:**",
     "closes_with": "(see the foot of this file).",
     "why": "a repository path and a pointer to the cut section"},
    {"anchor": "the numbers row 19 exists to supply",
     "opens_with": " —",
     "closes_with": "to supply",
     "why": "this project's row number in the table label"},
    {"anchor": "WHICH IS THE ROW'S WHOLE YIELD",
     "opens_with": ",",
     "closes_with": "WHOLE YIELD",
     "why": "this project's row in the label"}
   ],
   "cuts_added": []
  },
  "reading_pass/extracts/lazzari-2023-knowledge-based-chord-embeddings-modal-harmony-ontology.md": {
   "removals_added": [
    {"anchor": "it is a master's thesis**, indexed as a paper nowhere",
     "opens_with": "**Why eight searches missed it:",
     "closes_with": "queries could reach.",
     "why": "this pass's search bookkeeping"},
    {"anchor": "which is population row 8 of this same pass",
     "opens_with": " —",
     "closes_with": "same pass** —",
     "why": "this project's population row"},
    {"anchor": "which is better practice than most",
     "opens_with": " *Declared and acted on,",
     "closes_with": "of the population.*",
     "why": "this extract's grading of the paper against this project's population"}
   ],
   "cuts_added": []
  },
  "reading_pass/extracts/napoleslopez-feisthauer-leve-fujinaga-2020-local-keys-modulations-tonicizations.md": {
   "removals_added": [],
   "cuts_added": []
  },
  "reading_pass/extracts/mcleod-rohrmeier-2021-modular-harmonic-analysis.md": {
   "removals_added": [
    {"anchor": "exactly the L0 contract this project's framework gives",
     "opens_with": " —",
     "closes_with": "(spelling, meter given)",
     "why": "a comparison with this project's L0 contract"},
    {"anchor": "so nothing like the framework's DP-K rival stream",
     "opens_with": " —",
     "closes_with": "boundary.",
     "why": "a comparison with this project's DP-K"}
   ],
   "cuts_added": []
  },
  "reading_pass/extracts/bachi-2026-boundary-aware-symbolic-chord-recognition.md": {
   "removals_added": [
    {"anchor": "a ground-truth-quality fact in the direction of this project's principle #21",
     "opens_with": " —",
     "closes_with": "principle #21.",
     "why": "this project's principle #21"},
    {"anchor": "POORER than this project's notated record",
     "opens_with": " Its L0 is therefore",
     "closes_with": "project's input does not have.",
     "why": "a comparison with this project's L0"}
   ],
   "cuts_added": []
  },
  "reading_pass/extracts/hentschel-moss-mcleod-neuwirth-rohrmeier-2021-unified-chord-model.md": {
   "removals_added": [
    {"anchor": "the DP-N flashpoint evidence lives elsewhere",
     "opens_with": " —",
     "closes_with": "(the meta-corpus paper)",
     "why": "this project's decision point DP-N and where its evidence is held"}
   ],
   "cuts_added": []
  },
  "reading_pass/extracts/mcleod-rohrmeier-2024-chord-tone-alterations-suspensions.md": {
   "removals_added": [],
   "cuts_added": []
  },
  "reading_pass/extracts/sapp-2005-visual-hierarchical-key-analysis.md": {
   "removals_added": [],
   "cuts_added": []
  },
  "reading_pass/extracts/dehaas-magalhaes-wiering-veltkamp-2013-harmtrace-functional-analysis.md": {
   "removals_added": [],
   "cuts_added": []
  }
 }
}
```

*How the `why` strings were set, so the choice can be checked:* every removal's `why` is the cut list's own (its §4
writes one per removal); every cut's `why` is the cut list's §3 default — *"Limb A of Ruling 1 of 2026-09-21:
project-facing text (`reading_pass/l3_extracts_per_file_cut_list_2026_10_16.md`, §4, this file)"* — except the
shared cut strings, which carry L2's own `why` as §3 says. The cut list's per-cut "ground" column is not copied into
the `why`; the list itself is cited.

**(e) THE CHECK OF THE AUTHORED MEMBER, before any build.** A script (outside the working tree) imports the edited
generator as `dbp`, loads `<scratch>\l3_member8_expected.json` as `X`, and proves and prints, each with PASS or FAIL:

1. `dbp.EXTRAS["l3"][0] is dbp.CHARTER_MEMBER_7` and `dbp.EXTRAS["l3"][2] is dbp.LEDGER_MEMBER_9` (the shared objects,
   by identity), and `len(dbp.EXTRAS["l3"]) == 3`;
2. member (8)'s `[p["source"] for p in parts] == X["order"]`, and every part's `spans == [{"kind": "whole"}]`;
3. for each path in `X["new"]`: `part["removals"] == X["new"][path]["removals"]` and `part["cuts"] ==
   X["new"][path]["cuts"]`, with `part.get("removals")` and `part.get("cuts")` present;
4. for each path in `X["carried"]`: with `L` the part of `dbp.EXTRAS["l2"]`'s member (8) whose `source` is that path
   (found exactly once), `part["removals"] == L["removals"] + X["carried"][path]["removals_added"]` and `part["cuts"]
   == L["cuts"] + X["carried"][path]["cuts_added"]`;
5. `dbp.WITHHELD["l3"]["withheld_documents"]` has exactly the five keys of `L3_WITHHELD_DOCUMENTS`, in the order of
   `tools/audit/l3_withheld_documents.json` → `documents`, each with non-empty `finding`, `date` and `reason`; and
   `dbp.WITHHELD["l3"]["withheld_passages"] == []`;
6. `dbp.EXTRAS["l2"]` and `dbp.WITHHELD["l2"]` are equal to those of the generator at Task 2's commit (load that blob
   by `git show <Task 2 commit>:tools/audit/gen_derivation_boot_pack.py` into a scratch file and import it under
   another module name — **it reads its sources from `HERE`, so import it only for these two tables and call
   nothing**). If that import itself fails, report the error whole and take item 6 instead from the deleted-line and
   added-line enumeration of the generator against Task 2's commit: no deleted or added line may fall between the
   line `    "l2": [` that opens `EXTRAS["l2"]` and that list's closing `    ],`, or inside `WITHHELD["l2"]`.

**A FAIL is a STOP for this task:** correct the literal so the check passes, never the JSON object, and report every
FAIL and its correction. A FAIL in item 6 is a STOP-and-report with nothing committed: `EXTRAS["l2"]` is barred.

**(f) The four rulings in `the_rulings_it_executes`.** Old text (once) — the string Task 1's Edit 1.5 appended, its
last two lines:

```python
            "of the spent `l2` pack (Ruling 1 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, "
            "noted).",
        ],
```

New text:

```python
            "of the spent `l2` pack (Ruling 1 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, "
            "noted).",
            "Rulings 1 to 5 of `cowork_rulings_2026_10_15_l3_boot_list_sitting.md` — the `l3` "
            "subject's pack: the charter member and the ledger member as `l2` carries them, the "
            "extracts member over L3's slice and the first-pass extracts that bear on L3, no withheld "
            "passage of member (2), and withheld documents derived and confirmed before being "
            "authored.",
            "The rulings of `cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md` — the `l3` "
            "withheld family: every identity the authored verdicts grade IN is withheld.",
            "Ruling 1 of `cowork_rulings_2026_10_15_l3_withheld_documents_confirmation_sitting.md` — "
            "the derived set of the `l3` withheld documents, confirmed.",
            "Ruling 1 of `cowork_rulings_2026_10_15_l3_first_pass_extracts_sitting.md` — the eleven "
            "first-pass extracts of the `l3` extracts member, each cut per file under limb A of Ruling "
            "1 of `cowork_rulings_2026_09_21_l2_extracts_member_cutting_sitting.md`.",
        ],
```

**No commit in Task 3.** Its edits are committed with Task 4's render.

## Task 4 — the render, the proof that the four frozen subjects did not move, and the lists for the user; ONE commit with Task 3

**(a) THE RENDER.** Before it: `python <scratch>\dump_build.py <scratch>\B5.json` — **a `Stop` here is a STOP for the
batch's build half:** report it whole (above all an extras filter whose anchor, delimiter or heading is not found
exactly once, which names the file and the string), make no correction to any filter string, restore the generator to
Task 2's commit by explicit hash, commit nothing from Tasks 3 and 4, and go to Task 5. Then run `python
tools/audit/gen_derivation_boot_pack.py > <scratch>\dbp_t4_write.txt 2>&1; echo "exit:$?"` (write mode, no
`--subject`). `write_all` writes the manifest and **only** `tools/audit/derivation_boot_pack/l3/`, the four other
subjects being frozen. Record the output verbatim. **The `l3` line's verdict figures must read `IN 22`**; report the
OUT and UNPLACED figures as printed beside the relayed expectation `OUT 222 / UNPLACED 0` — **IN other than 22 is a
STOP before the commit**; a difference in OUT or UNPLACED is reported for the user, not a STOP. Prove the written
manifest byte-identical to `B5.json`.

**(b)** Run `--check` to `<scratch>\dbp_t4_check.txt`. **Expected: `the derivation boot pack re-derives`, four
`FROZEN — N file(s) at their recorded blobs` lines, exit 0.** Record verbatim. **Red is a STOP before the commit.**

**(c) THE FOUR FROZEN SUBJECTS DID NOT MOVE.** A script (outside the working tree, importing `diff_paths.py`) loads the
manifest at Task 2's commit (by `git show <hash>:tools/audit/derivation_boot_pack.json` into a scratch file) and the
manifest on disk now, and proves and prints: `diff` EMPTY for each of `harmony-boundary`, `scoring-model`, `l0-l1` and
`l2` under `subjects`; the top-level keys the same set; every top-level value equal except three — `the_rulings_it_executes`
is the old list followed by exactly the four strings of Task 3(f), and `the_pack_files_in_order` and `subjects` each
differ from the old only by the added key `l3`. **Any other difference is a STOP before the commit.** And by explicit
hash: no file under the four frozen directories differs from Task 2's commit.

**(d) The pack directory.** List `tools/audit/derivation_boot_pack/l3/` and report the file names (expected ten:
`00_READ_THIS_FIRST.md`, members (1) to (6) under their ruled names, `07_the_charter_the_layers_and_the_decisions.md`,
`08_the_seventeen_research_extracts.md`, `09_the_empirical_findings_ledger.md`); report that they agree with
`the_pack_files_in_order` → `l3`. Report member (8)'s counts from the manifest — parts, removals, cuts, `runs_to_end`
cuts — beside the authored totals the JSON object of Task 3(d) and the twelve L2 parts give.

**(e) THE LISTS FOR THE USER — this batch decides NONE of them.** Assemble in the report, read out of the manifest and
the rendered files, never transcribed from here:

1. **`subjects.l3.THE_WITHHELD_FAMILY.derived_cross_reference_additions.additions`** — every entry, with its identity,
   title and `derived_because`. **Then, under the heading `RULING 84 — ADDITIONS THAT WOULD WITHHOLD AN ENTRY THE
   USER RULED ADMITTED`, every addition whose identity `VERDICTS["l3"]` grades OUT**, with that OUT verdict's finding
   and reason beside it (Ruling 84 as Ruling 2 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md` restates
   it: *"an automatic cross-reference addition that would withhold an entry he has ruled admitted is put to him as
   its own list"*). If there is none, say so in those words.
2. `subjects.l3.LEAKS.entries` — members (5) and (6).
3. **`subjects.l3.LEAKS_IN_THE_EXTRAS.entries`** — limb B, every line, grouped by member and file.
4. **Member (8)'s title lines** — the first line of each of the seventeen parts as rendered (the cut list's §2 keeps
   every title, each naming a row or population row).
5. **Member (2) for L3** — search the rendered `02_…` file of `l3/` for each of the five withheld document names and
   for `ARCHITECTURE.md`, and report every hit with its line number there; `ARCHITECTURE.md` in the
   never-work-from-memory rule is the by-design naming the `LEAKS` block's scope note describes ("member (2)'s
   Conventions span names `ARCHITECTURE.md` in the never-work-from-memory rule BY DESIGN"). (Ruling 4 of the
   boot-list record withholds no passage of `CLAUDE.md` for L3; this is the measurement of what that leaves.)

**Commit exactly**, each by its own path, never a directory pathspec: `tools/audit/gen_derivation_boot_pack.py`,
`tools/audit/derivation_boot_pack.json`, and every file under `tools/audit/derivation_boot_pack/l3/` by the names (d)
listed. Prove the staged set is exactly these and that nothing under the four frozen directories is staged. Subject,
exactly: `author the l3 withheld family and extras, and render the l3 boot pack; the lists go to the user`. Push;
verify.

**E3/E4:** Task 3(e) all PASS; the render's IN 22; `--check` green; (c) as stated; (d) and (e) reported whole; one
commit, pushed.

## Task 5 — the close

1. **The `STATUS.md` entries and the forward-bound move, IN THIS ORDER** (read `gen_status_batch_bound.py` whole at the
   object first, ordered first read (9)). **(a)** Write this batch's entries at the top of `STATUS.md`: one pointer
   entry per task that did work — the close entry FIRST, NAMING THIS DISPATCH BY ITS FILE NAME
   (`records/cc/instructions/cc_instruction_l3_pack_build_second_half_2026_10_16.md`), each earlier task's entry below
   it saying `Same dispatch`; no figure restated (D-431). The close entry says what happened: either that L2's pack is
   frozen after the pre-scoping-rulings test was keyed on its authored list, `VERDICT_DATE["l3"]` and the criterion
   bullet are written, L3's withheld family and extras are authored and its pack is RENDERED, and the lists go to the
   user before any session boots — or, if a task stopped, which task stopped and that nothing after it was done. It
   says that no session is booted, no brief written, no score staged, no `D-NNN` allocated and no open-items row
   touched. **The `Last updated: ` prefix moves from the first half's close entry to your newest entry.** **(b)**
   Re-aim the five authored constants of `gen_status_batch_bound.py`: `BASE_COMMIT` (this batch's last task commit
   before the close), `PREVIOUS_BATCH_DISPATCH` (`cc_instruction_l3_pack_build_first_half_2026_10_15.md`), `ACT_DATE`
   (the day the move runs), `DISPATCH` (`cc_instruction_l3_pack_build_second_half_2026_10_16.md`), `TASK`
   (`Task 5`); append your own aiming to `PREVIOUS_AIMINGS` on the convention its comments state. **(c)** Run
   `gen_status_batch_bound.py --apply`. **Prediction:** it moves **exactly the first half's four entries** (its close
   entry and the three `Same dispatch` entries for its Tasks 4, 3 and 0, read at `STATUS.md` by the writing side); the
   two 2026-09-02 entries stay. If it STOPs, restore its passing aim, re-run green, report, move nothing by hand. **(d)
   LAST**, after the final `STATUS.md` edit, regenerate `gen_session_start_read_size.py` and confirm its `--check`
   green. Commit the re-aimed tool, `tools/audit/status_batch_bound.json`, `STATUS.md`, `STATUS_ARCHIVE.md` and the
   read-size artifact together in the close.
2. **The report**, `records/cc/reports/cc_report_l3_pack_build_second_half_2026_10_16.md`, which decides nothing and
   recommends nothing. **If Task 1 stopped, its first section is the diff (g) printed, under the heading Task 1(g)
   names.** Otherwise its first section is headed **`THE LISTS FOR THE USER — BEFORE ANY SESSION BOOTS`** and carries
   Task 4(e) whole. Then: both guard states; every commit hash; E0 to E4 and A1 to A3 graded; Task 1's ten digests with
   the two-form agreement and the disk-equals-commit proof per file; the outputs of every comparison script with the
   scripts' texts; Task 3(e)'s PASS lines; the render's printed output; declared departures; and the plan's tell in one
   sentence — did this batch produce anything other than the landed paths, the repair, the freeze, the three Task 2
   edits, the `l3` entries of `WITHHELD` and `EXTRAS` with `L3_WITHHELD_DOCUMENTS` and the four ruling strings, the
   rendered `l3` directory, the manifest, the Task 5 files and the report? If yes, name it.
3. **The full close appended to `records/cowork/handoff/cowork_away_returns.md`** as a section headed **THE L3 PACK
   BUILD, SECOND HALF: L2 FROZEN, L3's PACK RENDERED — THE LISTS GO TO THE USER BEFORE ANY BOOT; NO SESSION, NO
   ALGORITHM CHANGED** (if a task stopped, the heading says which, and says what was not done) — the report's content
   as pointers, and the plan line: **the next act is the writing side's — the check of this batch's return at the
   objects, then the lists put to the user; the brief and the boot come only after his rulings on them.**
4. **The close does not assert the end state**; one further commit carries it. Commit the close, push, verify; then the
   full guard run in write mode at that tree, the A2 exceptions handled as A2 says, and the one further commit with its
   artifacts, pushed and verified. Re-run `gen_guard_classification.py --check` after it and report the message
   (expected: the standing STOP naming the same three tools; a change in that message is reported, not a STOP).

**E5:** at the tree carrying the close, a fresh full guard run — the A2 prediction — committed only after the run
that produced it.

**THIS BATCH ENDS HERE.** No session boots from the pack before the user has ruled on every list of Task 4(e).

## What this batch does NOT do

- **No session booted, no brief written, no score staged or copied.**
- **No list of Task 4(e) acted on.** No filter string corrected after a STOP; no additional cut authored.
- **No change to what any layer computes** as its specification defines it.
- **No decisions-register entry, no `D-NNN`, nothing in the suspension file, no ruling taken.**

## What this batch deliberately leaves to later acts, named so it is not lost

- **The lists of Task 4(e)**, to the user through the writing side, before any boot.
- **The brief, and the blind deriving session in a fresh Cowork session** — including how the two input-contract
  copies under `tools/audit/derivation_exemplars/l3/` and the staged scores reach the session (the first half's "leaves
  to later"; the L2 precedent attached its scores by name at boot and kept its input contract outside the pack).
- **The staged score set** (boot-list Ruling 6) — put to the user with each claim beside it before anything is staged.
- **The proposal to leave the `docs/research_papers/BIBLIOGRAPHY.md` path at line 2234 of the L2 input-contract copy**
  — not ruled (entry 410 §2). Nothing in this batch touches that copy.
- **`reading_pass/candidacy_upgrades.md`'s reading-progress record** — rows 36 and 39's second extractions; one update
  after the run (entry 169 §3).
- **The six drifted register anchors, the eight stale derived `home_section` blocks, the three cosmetic slips of the
  generated reading files** — as the first half left them.

## The writing side's self-check, run before this dispatch was released (D-434)

1. *Principles.* #6 — the repair keys one concept on one authored list instead of a proxy; the carried filters are
   copied from L2's own entries and proved equal, not retyped; the charter and ledger members are the shared objects.
   #12 — every replaced comment keeps its former wording; L2's record is proved unmoved beyond the frozen shape against
   the committed manifest at an explicit hash; L2's pack is frozen at the bytes its session read. #13/#18 — the named
   risk is stated before the run and measured by it, with a STOP rather than a prediction. #17f/D-431 — every count
   this dispatch states is read at an artifact or a record and named as such, the relayed ones marked RELAYED. #19 — every authored filter is checked against its JSON authority
   before the build, and the render proves both directions.
2. *Conventions.* American English; the vocabulary block precedes first use; *decisions-register* qualified; *check*,
   *script*, *generator*, never *instrument*.
3. *The bars.* No session; no list acted on; no register entry; every record landed as it stands; no question to the
   user.
4. *Documentation and algorithm.* Nothing here changes the algorithm as any specification defines it.

*Provenance: Cowork writing side, 2026-10-16 (Stockholm), the sitting booted on
`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_twelve.md`, at tip
`a01e9402fbaf034fe0d357214b67c06a8294309c` read as files; no shell command was run. **Read by the writing side, at the
extent named:** the boot read of entry 291 §4 step 3 (`CLAUDE.md` at its six ruled spans; `DECISIONS.md`, `STATUS.md`
whole; the gating answer; entry 118's bridge-fault section; entry 152's (v) to (x); entry 169 whole); entries 291, 410,
411 and 412 whole; the cut list and the freeze derivation record whole; the boot-list, confirmation, first-pass extracts
and 2026-10-14 L3 withheld-family ruling records whole; `tools/audit/l3_withheld_documents.json` whole; the first-half
dispatch whole; the first-half report at its heading list, §1, §2, §3 and §5; the L2 second-half dispatch at its
heading list and its Task 9; `FRAMEWORK.md` at the L3 block of §5; the generator at its docstring's STOP list,
`VERDICT_DATE`, `MEMBERS`, `FROZEN`, `CHARTER_MEMBER_7`, `LEDGER_MEMBER_9`, the head of `EXTRAS`, the start of
`EXTRAS["l2"]`'s member (8) and its parts at the McLeod & Rohrmeier 2021 and BACHI entries and the tail of its last part,
`L2_WITHHELD_DOCUMENTS`, `WITHHELD` whole, `CRITERION["l3"]`, the field tuples and `cross_reference_additions`,
`withhold_passage`, `build_subject` whole, `build()` whole, `verify_frozen`, `frozen_block`, `frozen_from_disk`,
`write_all`, `check_all` and `main`, and by search for the twelve carried parts' `"source"` lines and for every old
text quoted above. **NOT read:** `filter_part`, `_cut_spans`, `_removal_spans`, `render_extra`, `criterion_block`'s
body, `render_read_me`; the other ten carried L2 parts' filter entries (Task 3(d) has them copied from the file, not
from here); `cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`; `gen_status_batch_bound.py`;
`gen_guard_state.py`; any extract.*

## The writing side's check of this dispatch at its sources (recorded per the standing clause and D-434; run 2026-10-16 in a turn of its own, after the user's "continue")

Scope: completeness, coherence, correctness and absolutes, against the objects the provenance names. **Confirmed at
the objects:** by one search over the generator, the distinctive line of every Task 1 old text occurs once (the three
`subject in FROZEN` tests at the field choice, `extras_leaks` and the `★_what_these_are` switch; the comment line
`# subject that is NOT FROZEN …`; the docstring's `a file that is not there.`; `"FROZEN.",`; the `VERDICT_DATE` STOP
string in `the_STOPS`), and the other three `subject in FROZEN` hits are `if subject in FROZEN:` in `build()`,
`write_all` and `check_all`, untouched by this dispatch; `WITHHELD: dict[str, dict] = {` occurs once; the closing
`        LEDGER_MEMBER_9,` / `    ],` / `}` of `EXTRAS` was read at its lines; the twelve carried `"source"` lines each
occur once in `EXTRAS["l2"]`; the JSON object of Task 3(d) was read back against the cut list's §4 file by file.

**Corrected at their sites, former wordings kept here (#12):** (1) the comments of Edits 1.2 and 1.3, the STOP 13
comment and docstring line, and the `l2` freeze comment carried dates that would be false when Claude Code makes the
edit — former wordings: *"★ CORRECTED 2026-10-15 (the derivation at"* (twice), *"(2026-10-15)"* (twice), *"Frozen
2026-10-16 by the second half of L3's pack build"*; they now name the act and the derivation's date, and the change
from the first half's comment is declared at the comment; (2) Task 2 read only one phrase as changed, which would have
left *"★ CORRECTED 2026-10-15"* and *"(2026-10-15, …"* standing in edits made later — former wording: *"except one word:
in Edit 2's new text and in Edit 3's comment, read "the first half of L3's pack build" as "the second half of L3's pack
build""*; (3) the bars forbade every function-body edit but Task 1's, while Task 2 edits `criterion_block` — former
wording: *"except the three tests and the one STOP Task 1 quotes,"*; (4) the premise ledger called the first half's
digests a FACT — they are relayed from its report; (5) *"in exactly three places besides nothing else"* is now stated
with the search and the three other hits; (6) the plain-words field's comment said *"Taken from"* where the sentence
joins two lines with words of this side's — former wording: *"Taken from the L3 block … its "Question" line and its
"Publishes" line, without their markup."*; (7) the self-check's *"every count is the tool's, the ruling's or the
artifact's"* was wider than the ledger, which marks relayed counts — corrected to say so; (8) A2's *"two ruling
records are untracked now"* was not checked at git — now *"expected"*; (9) Task 4(e) item 5 attributed the by-design
note to the wrong scope note — now quoted from the `LEAKS` block; (10) Task 3(e) item 6 gained a fallback if the older
generator cannot be imported; (11) the provenance now says the last L2 part was read at its tail.

**Bound:** the check re-read this dispatch whole and the generator at the lines named; it did not read `filter_part`,
`_cut_spans`, `_removal_spans` or `render_extra`, did not open any extract, and relies on the cut list's own §7 for
the strings running — which the render proves. No task, ruling, prediction of a count or bar was widened.
