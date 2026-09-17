# CC INSTRUCTION — finish the root records move from the current tree: fix the 43 quotes, regenerate the nine newly failing guards, commit, prove, close, push, 2026-09-17

**THE BASE.** Branch `master`, commit `5d24edb565b2e0e9efc92e082c163112bd97087f`, **with an uncommitted working tree that
is already moved.** The previous batch ran
`records/cc/instructions/cc_instruction_root_records_move_2026_09_17.md` (second issue, blob
`ce2290509e905ae41d3422c06c937b3d3cbe9f98`) and STOPPED in its Task 5(c), before any commit. Its report is
`records/cc/reports/cc_report_root_records_move_2026_09_17.md`. **Read that report whole before Task 0.** Read the
previous dispatch whole as well: this one keeps its route rule, its Task 6 commit structure and its Task 7 report
rules except where it names a change.

**DO NOT UNDO THE MOVES. DO NOT START FROM THE PREVIOUS DISPATCH'S TASK 0.** The index already holds exactly the
978 renames of its Commit 1 (previous report §0).

**WHY THE PREVIOUS DISPATCH CANNOT FINISH AS WRITTEN — a defect of the writing side.** Its Task 6 proof allowed a
regenerated artifact to change **only** by a root file name becoming its new path. The previous batch predicted,
without measuring (its §7(c)), that several of the nine guards that newly fail measure sizes or digests of files it
edited, so a correct rewrite would fail that bar. Two of them are size measurements by name and output file
(`gen_session_start_read_size.py`, `gen_defense_share.py`); for the rest the prediction is unmeasured. This dispatch widens the bar for those nine guards only, and adds STOPs for the ways a wider bar could hide a
real break.

**The writing side does not touch this file, or any file in its read-first block, while the batch runs (D-251).**

**★ SECOND ISSUE.** The first run (dispatch blob `b5d6566eebf3553821291199d95cec2c67949491`) stopped at Task 1(a),
before any edit, staging or commit; its report is `records/cc/reports/cc_report_root_records_move_finish_2026_09_17.md`.
The cause is this dispatch's defect, not a batch error: Task 1(a) and Task 1(c)2 assumed the cited line numbers in
`CLAUDE.md` were current, and eight of the 43 entries' quotes start 39 or 55 lines below their cited lines, a drift
the other `CLAUDE.md` entries already show in `--verify` (for example D-200 and D-308, which quote no moved file).
**That drift is a pre-existing failure of `--verify`, so this batch reports it and does not correct it** — the same
rule as the previous dispatch's Task 0(d). Tasks 1(a) and 1(c)2 are corrected below, the former wordings kept.
Task 0(d) and Task 3's list gain the first run's report; Task 4's report path changes so that report is not
overwritten. **Start again from Task 0.**

**★ THIRD ISSUE.** The second issue's run (dispatch blob `09be9b2b43e53d8814c22c7c3b7f3576d3f60163`) stopped at Task 0
on a guard refusal of a `tail` the executing session added to read a capture; nothing was edited, staged or committed.
Its report is `records/cc/reports/cc_report_root_records_move_finish_second_2026_09_17.md`. **So that a further stop
needs no new issue for its report alone**, stop reports of this dispatch are now handled by pattern: Task 0(d) allows,
and Commit 2 adds, every file Glob finds at `records/cc/reports/cc_report_root_records_move_finish*_2026_09_17.md`;
Task 4 writes to the first name of a stated series that does not yet exist. **And read every capture with Read or
Grep, wherever it is stored — never with a shell command.** **Start again from Task 0.**

---

## THE ROUTE RULE (unchanged from the previous dispatch, restated because it binds)

- **Reading** working-tree files: Glob, Grep, Read only (`CLAUDE.md` Conventions, D-253).
- **Editing**: the Edit file tool.
- **Running**: only the commands this dispatch names, and git. **No `git status`. No `git diff` unless both sides are
  commit hashes taken from a commit command's own output.** Changed paths come from `python
  tools/audit/changed_paths.py` (working tree) or `python tools/audit/changed_paths.py --staged`. To compare two
  captures, give each a blob identity with `git hash-object -w <capture>` and compare the identities.
- **Add no auxiliary command of your own.** The previous batch stopped on one (its §0), and so did this dispatch's
  second-issue run. **A capture is read with Read or Grep, wherever it is stored; no shell command reads any file.**
  *(Third issue added the second sentence.)*
- **Never open, list, search or move anything under** `docs/research_papers/polyph9-release/`, `scratch_artifacts/`,
  `external resarch summary/`, `Claude outputs/`, `Codex research inventory/` or `.git/`.
- **If a guard refuses anything, STOP and report the refusal text verbatim.**

---

## TASK 0 — re-capture the state

**(a)** `git hash-object -w` on this dispatch. Record the identity.

**(b)** `git rev-parse --abbrev-ref HEAD` and `git rev-parse HEAD`. **Not `master` at
`5d24edb565b2e0e9efc92e082c163112bd97087f` → STOP.**

**(c)** `python tools/audit/changed_paths.py --staged`, captured, given a blob identity. **It must be
`4e959e003bbdd5b51e336ee669bd761eba00d7fc`** (the previous report's Task 2 and stop captures). Different → STOP.

**(d)** `python tools/audit/changed_paths.py`, captured, given a blob identity. Compare it with the previous stop
capture, `git cat-file blob fd3a25f41083e97d29ea6a5da0f9ae3b9d7dba1b`. **The only records allowed to be new** are
untracked records for these three paths:
- `records/cc/reports/cc_report_root_records_move_2026_09_17.md`
- `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_one.md`
- this dispatch, `records/cc/instructions/cc_instruction_root_records_move_finish_2026_09_17.md`
- every stop report of earlier runs of this dispatch: each file Glob finds at
  `records/cc/reports/cc_report_root_records_move_finish*_2026_09_17.md` *(third issue; former wording: "the first
  run's stop report, `records/cc/reports/cc_report_root_records_move_finish_2026_09_17.md`")*

A difference that lies only in records under `scratch_artifacts/` is **reported, not a STOP** (this batch never
writes there). **Any other difference → STOP.**

**(e)** `python tools/audit/gen_guard_state.py --check`, captured whole, given a blob identity. Compare it guard by
guard with the previous Task 5(b) capture, `git cat-file blob d3774d3735639fcf8a604ee5d357a94933f2305f`
(`81 guard(s) run, 24 failing, 4 not run, 16 historical record(s)`). **Any guard whose result differs → STOP.**
Call this capture **the reference run**.

---

## TASK 1 — the 43 quotes in the decisions register

**Background.** `tools/audit/decisions/gen_cluster_dispositions.py --verify` checks that every register entry's
`verbatim` quote exists at its home and starts at the cited line. The previous batch changed moved file names to
paths inside the home documents (its Task 4) and changed only `home` values in the register data, so the quotes of
43 entries no longer match (previous report §7(a): D-199, D-249, D-252, D-253, D-254, D-294, D-416, D-640 to D-658,
D-660 to D-664, D-666 to D-677). `--verify` already failed at the start state for other reasons and still does.

**(a) Establish the set; do not take it from this dispatch.** Take the previous batch's `--verify` output from
`git cat-file blob 9cfcddcbc553da8f804aafe0748025ebdcf229e4`. For each `verbatim NOT FOUND` line, decide whether the
entry's `verbatim` field in `tools/audit/decisions/backbone_decisions.json` names a moved file by its root name
**and** the home now carries that name as a `records/…` path inside the quoted passage, **wherever that passage now
starts** (locate the passage's opening line with Grep and Read from there; do not rely on the cited line number). The
entries for which both hold are the set. *(Corrected in the second issue. Former wording: "at that place (Read the
home at the cited line)".)* **If the set is not exactly the 43 identities listed above → STOP**, naming
the difference.

**(b) Edit.** In each entry of the set, inside its `verbatim` field only, change each moved root name to the path
the home now carries at that place — the same mapping Task 4 of the previous dispatch used. **Nothing else in the
field or the entry changes.** One Edit per changed passage.

**(c) Regenerate and check.**
1. `python tools/audit/decisions/gen_decisions_register.py`, then `--check`.
2. `python tools/audit/decisions/gen_cluster_dispositions.py --verify`, captured. **None of the 43 identities may
   appear in a `verbatim NOT FOUND` line. The only failure lines allowed that are absent from blob
   `9cfcddcbc553da8f804aafe0748025ebdcf229e4` are exactly eight `LINE DRIFT` lines, one for each of D-199, D-249,
   D-253, D-254, D-294, D-656, D-660 and D-675, each giving as its actual start line the value in the "Where the
   quoted passage starts now" column of the first run's report §0 (1432, 1836, 1850, 1893, 976, 1083, 1616, 1714
   respectively).** A missing one, a different start line, or any other new `MISS`, `LINE DRIFT`, `DANGLING` or
   `FIELD SHAPE` line → STOP. The two summary count lines may change only as 43 fewer misses and eight more drifts
   imply; state the arithmetic in the report. **Do not change any entry's cited line number** — the drift is
   pre-existing and is reported, not corrected. *(Corrected in the second issue. Former wording: "and no `NOT FOUND`
   or other failure line may appear that is absent from blob `9cfcddcbc553da8f804aafe0748025ebdcf229e4`.**
   Otherwise → STOP.")*
3. `python tools/audit/decisions/gen_cluster_dispositions.py --check` and `--producible`. **If either fails → STOP.
   Do not run that tool's write mode.** (It writes the disposition layer of record; this batch has no licence to
   regenerate it.)
4. `python tools/audit/changed_paths.py`, captured, given a blob identity: **the Task 1 state.**

---

## TASK 2 — the nine newly failing guards

**The nine** (previous report §7(b)), each with its write mode **read at the tool this sitting by the writing side**:

| Guard | Write mode — run exactly this | Artifacts it writes |
|---|---|---|
| `tools/audit/gen_discard_records.py` | no argument | `tools/audit/discard_records.json` |
| `tools/audit/gen_specification_document_set.py` | no argument | `tools/audit/specification_document_set.json` |
| `tools/audit/gen_rulings_sort.py` | no argument | `tools/audit/rulings_sort_classification.json` and `ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md` |
| `tools/audit/gen_claude_md_finer_archive.py` | no argument — **never `--apply`** | `tools/audit/claude_md_finer_archive.json` |
| `tools/audit/gen_post_split_archive.py` | no argument — **never `--apply`** | `tools/audit/post_split_archive.json` |
| `tools/audit/gen_claude_md_prune_backlog.py` | no argument — **never `--apply`** | `tools/audit/claude_md_prune_backlog.json` |
| `tools/audit/gen_session_start_read_size.py` | no argument | `tools/audit/session_start_read_size.json` |
| `tools/audit/gen_defense_share.py` | no argument | `tools/audit/defense_share.json` |
| `tools/audit/gen_derivation_boot_pack.py` | no argument — **never `--subject`** | `tools/audit/derivation_boot_pack.json` |

*Why `--apply` is barred:* in the three archive tools `--apply` calls `apply_move()`, which the tools' own help
texts describe as performing the ruled move or moves once; with neither flag, `main` only rebuilds and writes the
tool's record. *On the boot pack:*
every subject it builds is in its `FROZEN` table, and `write_all` writes nothing into a frozen subject's directory;
its `--check` compares the manifest and, for a frozen subject, the recorded digests. **Read each tool's docstring and
`main` before running it. If what you read contradicts the table → STOP.**

**(a) Order.** Run the nine write modes in the table's order, **with `gen_session_start_read_size.py` before
`gen_defense_share.py`** (the defense-share measurement re-derives its whole-read denominator through the read-size
reader — `STATUS.md`'s current head entry). After each write mode, run that tool's `--check` once. **A write mode that
prints a STOP or exits non-zero → STOP.**

**(b) Nothing else may be written.** After all nine: `python tools/audit/changed_paths.py`, captured. **Every record
that is new or changed against the Task 1 state must be one of the artifacts in the table's third column, or a Task 1
file** (`backbone_decisions.json`, `DECISIONS.md`, `decisions/group_*.md`). **Any change under
`tools/audit/derivation_boot_pack/` → STOP.** Any other path → STOP. *Bound, stated rather than hidden: this
comparison cannot see a second write to a path that was already modified before Task 2 (for example `CLAUDE.md`);
the Task 3 content proof is what covers those files.*

**(c) The guard set.** `python tools/audit/gen_guard_state.py --check`, captured whole. Compare with **the reference
run** guard by guard. **Every one of the nine must now PASS; every other guard's result must equal the reference
run's.** Otherwise → STOP.

**(d) What the content of those rewrites may be** — checked in Task 3's proof, after Commit 2:
- a moved file's root name becoming its new path;
- a changed number that is a size, a line count, a character count, a word count, a share or a digest **of a file
  this batch or the previous batch edited or regenerated**;
- a line or span coordinate that moved because such a file changed length.

**Anything else → STOP**, and specifically: a boolean that was `true` becoming `false`; a verdict, class or status
word changing; an entry or member appearing or disappearing; the number of occurrences of `STOP`, `HALT` or `does not re-derive`
in the file rising; and in `ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md`, **any
change other than a root name becoming its new path.**

---

## TASK 3 — commit, prove, close, push

**Commit 1 — the moves only.** `git commit` of the index as it stands (the 978 renames). No `git add` before it. No
`-a`. Record the hash from the command's output.

**Commit 2 — references, quotes, regeneration, and the record files of this line of work.** Add **by explicit path
only** (never `git add -A`, `.`, or a directory):
- every path that `changed_paths.py` shows modified in the working tree **except these three pre-existing edits, which
  are not this line of work and must not be committed:** `docs/research_papers/BIBLIOGRAPHY.md`,
  `docs/research_papers/README.md`, and `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_eight.md`
  (its working-tree modification predates the move; its rename is already in Commit 1);
- these record files, each confirmed with Glob first:
  - `records/cc/instructions/cc_instruction_root_records_reference_map_2026_09_16.md`
  - `records/cc/reports/cc_report_root_records_reference_map_2026_09_16.md`
  - `records/cc/instructions/cc_instruction_reference_map_check_2026_09_17.md`
  - `records/cc/reports/cc_report_reference_map_check_2026_09_17.md`
  - `tools/audit/check_reference_map.py`
  - `tools/audit/reference_map_check.json`
  - `records/cc/instructions/cc_instruction_root_records_move_2026_09_17.md`
  - `records/cc/reports/cc_report_root_records_move_2026_09_17.md`
  - every file Glob finds at `records/cc/reports/cc_report_root_records_move_finish*_2026_09_17.md` except this run's
    own report, which goes in Commit 3 *(third issue; former wording:
    "`records/cc/reports/cc_report_root_records_move_finish_2026_09_17.md` (the first run's stop report)")*
  - `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_nine.md`
  - `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety.md`
  - `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_one.md`
  - this dispatch

**No other untracked file is added.** The 171 moved untracked files stay untracked. Before committing, run
`changed_paths.py --staged` and confirm that none of the three excluded paths shows a modification in the index
(entry 188 may show only its Commit 1 rename, which is already committed and so should not appear at all). Record the hash.

**The content proof, after Commit 2 and before anything else.** `git diff <Commit 1 hash> <Commit 2 hash>`. State in
the report, per file class, that:
- every changed line in a previous-batch Task 3 tool is one of that dispatch's rule-cases (path, scan directory,
  prefix anchor, table key);
- every changed line in a previous-batch Task 4 document, in `.gitignore`, and in `backbone_decisions.json` equals its
  old line once each new path is replaced by its root name;
- every changed line in `DECISIONS.md` and `decisions/group_*.md` equals its old line once each new path is replaced by
  its root name;
- every changed line in a Task 2 artifact is one of the kinds Task 2(d) allows, and none of the kinds it bars;
- each record file in the list above is an addition of a whole file.

**If any change goes beyond that → STOP: no Commit 3, no push.** Report both hashes and the lines. Nothing has left
the machine.

**Write the report (Task 4) now, before Commit 3.**

**Commit 3 — the close.**
1. Write the `STATUS.md` entry for this line of work, as a pointer to this batch's report and to the previous batch's
   report (no figure restated, D-431).
2. Perform the forward bound as `STATUS.md`'s own head entry describes it: `tools/audit/gen_status_batch_bound.py`
   re-aimed at the then-previous batch (the batch `STATUS.md`'s current dated entries name), **with `BASE_COMMIT` set
   to the Commit 2 hash**, this entry written first and `--apply` second. Read that tool's docstring before running it.
   Re-aiming its authored inputs is the tool-source edit Ruling 5 of
   `records/cowork/rulings/cowork_rulings_2026_08_26_amendment_landing_sitting.md` allows. **If the bound cannot be
   performed as described → do not guess: keep the entry, skip the bound, and report why.**
3. Because `STATUS.md` changed, run `python tools/audit/gen_session_start_read_size.py` then
   `python tools/audit/gen_defense_share.py`, in that order.
4. `python tools/audit/gen_guard_state.py --check`, captured. **Every guard's result must equal Task 2(c)'s.**
   Otherwise → STOP, no Commit 3, no push.
5. Commit, by explicit path: the report, `STATUS.md`, `STATUS_ARCHIVE.md` and `gen_status_batch_bound.py` if the bound
   ran, and the two measurement artifacts. Record the hash.
6. `git diff <Commit 2 hash> <Commit 3 hash>`: changes only in those paths, and in the two measurement artifacts only
   Task 2(d)'s allowed kinds. **Otherwise → STOP, no push.**

**Push.** `git push origin master`. Never `--force`. If it fails, report the error verbatim and do not retry with other
options.

**Each commit message ends with the attribution lines your session's own instructions give.**

---

## TASK 4 — the report

Write, with the Write file tool, the first of these paths that Glob does not find:
`records/cc/reports/cc_report_root_records_move_finish_third_2026_09_17.md`, then `…_fourth_…`, then `…_fifth_…`
(same pattern, the ordinal word changed). **If all three exist → STOP before writing.** *(Third issue. Former wording:
"`records/cc/reports/cc_report_root_records_move_finish_second_2026_09_17.md` *(corrected in the second issue so the
first run's report is not overwritten; former path `records/cc/reports/cc_report_root_records_move_finish_2026_09_17.md`)*".)*
The report carries:
Task 0's identities and comparisons; Task 1's set, each edit before and after, and the `--verify`, `--check` and
`--producible` results; Task 2's commands, outputs and the two comparisons; Commits 1 and 2 with the content proof.
**Name members; state a total only as a sum of named members or as a figure a tool printed, cited to that output**
(D-431). Commit 3's steps 3–6, its hash and the push result go in the chat reply.

At the foot of the chat reply: the report's path, this dispatch's blob identity, the three commit hashes, and the push
result.

---

## DECLARED BY THE WRITING SIDE

- **What this batch's orders move:** the git object store; `tools/audit/decisions/backbone_decisions.json` (the 43
  `verbatim` fields); `DECISIONS.md` and `decisions/group_*.md` through their generator; the ten artifacts in Task 2's
  third column through their generators; `STATUS.md`, `STATUS_ARCHIVE.md` and `gen_status_batch_bound.py` through the
  forward bound; `session_start_read_size.json` and `defense_share.json` a second time at the close; the new report;
  three commits and one push. **No `src/` file, no DATED, UNDECIDED or FROZEN document, no file under
  `tools/audit/derivation_boot_pack/`, and no hand edit of a generated file.**
- **One regenerated file is a ratification surface:** `ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md`
  is written by `gen_rulings_sort.py` and renders each entry's `home` and quoted decision from the register data. It
  is regenerated because the register is a generated surface that changes only through its data and generators
  (`CLAUDE.md`, decisions-register section, rule (d)), and only a name-to-path change is allowed in it (Task 2(d)).
- **Checked at the files by the writing side this sitting:** the previous dispatch whole; the previous report whole;
  `gen_derivation_boot_pack.py` at its `FROZEN` table, `WITHHELD`-driven `build` loop, `write_all`, `check_all` and
  `main`; `gen_rulings_sort.py` at its docstring, constants, surface renderer tail and `main`;
  `gen_claude_md_finer_archive.py` at its docstring and `main`; `gen_post_split_archive.py` and
  `gen_claude_md_prune_backlog.py` at `main`; the argument handling and `OUT` constant of all nine tools;
  `open_items/OI-285.md` lines 100–118; `STATUS.md` whole; `.git/refs/heads/master`; the `at_tree` reader in
`gen_session_start_read_size.py` (it reads the working-tree file, so `--check` passes after a write mode without a
commit); Ruling 5 of `records/cowork/rulings/cowork_rulings_2026_08_26_amendment_landing_sitting.md` at its heading and
ruled sentence; `gen_status_batch_bound.py` only at a search for `BASE_COMMIT` and `--apply`.
- **Not read by the writing side:** the bodies of `gen_discard_records.py`, `gen_specification_document_set.py`,
  `gen_session_start_read_size.py` and `gen_defense_share.py` beyond their `main`, `OUT` and (for the first) `at_tree`;
  `gen_status_batch_bound.py` beyond that search; `gen_cluster_dispositions.py`; `backbone_decisions.json`; `changed_paths.py`.
- **A conjecture the handoff record carried is withdrawn here.** The hundred-and-ninety-first handoff entry guessed the
  boot-pack failure came from a subject that is not frozen. At the tool, every subject it builds is frozen, so the
  failure is the manifest `derivation_boot_pack.json`, whose member records are built from current sources (the
  tool's `frozen_block` docstring). **Not established by the writing side:** which fields of the manifest differ. Task
  3's proof is what shows that.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

- Task 0: not at the base; the staged capture's identity differs; an unallowed working-tree difference; a guard result
  differing from the previous Task 5(b) run.
- Any guard refusal.
- Task 1: the set is not the 43; a new `--verify` failure line other than the eight allowed `LINE DRIFT` lines; `--check` or `--producible` failing.
- Task 2: a tool whose docstring or `main` contradicts the table; a write mode printing STOP or exiting non-zero; any
  path written outside the table; any change under `tools/audit/derivation_boot_pack/`; a guard result other than
  those allowed.
- Task 3: a changed line of a barred kind; an excluded path in the index; a Commit 3 guard result differing; a Commit
  3 change outside its paths.
- **Any instruction here found false at the objects.**

**On any STOP: do not undo the moves or any commit.** Report `changed_paths.py` and `--staged`, captured, and every
commit hash; stop; the user decides.

## WHAT THIS BATCH MAY NOT DO

Run any `--apply` other than the forward bound's; run `gen_cluster_dispositions.py` in a write mode; edit any DATED,
UNDECIDED or FROZEN document or any `src/` file; hand-edit a generated file; add any untracked file other than those
Task 3 names; commit the three excluded edits; rename or move any file; run any build or test; open, list or search
the excluded locations; use `--force`.
