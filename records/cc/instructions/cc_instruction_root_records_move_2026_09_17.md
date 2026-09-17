# CC INSTRUCTION — move the root record files into `records/`, fix every reference, regenerate, commit and push, 2026-09-17

**THE BASE.** The current commit should be `5d24edb565b2e0e9efc92e082c163112bd97087f` on branch `master`.
**Check this first (Task 0).**

**WHY THIS EXISTS.** The user ruled on 2026-09-16 that the Cowork and CC record files **cannot stay in the
repository root**, and on 2026-09-17 ordered the actual move and the fixing of all references. Two earlier batches
prepared it and are the inputs of this one:

- the map: `records/cc/reports/cc_report_root_records_reference_map_2026_09_16.md` — **read it from its pinned blob
  `aafb7591f7e0bbcde89c97e5f8baf89985693bdb`** (`git cat-file blob`), never from the working tree;
- the mechanical check of that map: `records/cc/reports/cc_report_reference_map_check_2026_09_17.md` and
  `tools/audit/reference_map_check.json`.

This batch is also **the second backup**, still undone as the hundred-and-eighty-ninth and hundred-and-ninetieth
handoff entries record: its commits are pushed at the end.

**The writing side does not touch this file while the batch runs.**

**★ SECOND ISSUE.** The first run stopped at Task 0(c): the guard refused `git status` (D-253). Nothing was moved,
edited or committed; the only change was the first issue's blob, `0b4f33233cabf359645d11d9d76f85843dd6636b`. This
issue replaces every `git status` with `tools/audit/changed_paths.py`, and moves the content proofs to a `git diff`
between two commit hashes after Commit 2, before anything is pushed. **Start again from Task 0.**

---

## THE ROUTE RULE

- **Reading** working-tree files: the file tools only (Glob, Grep, Read). No shell text utility, no interpreter code
  that reads a file, no redirection from a file (`CLAUDE.md` Conventions, D-253).
- **Moving**: `git mv` for a TRACKED file; a plain move command for an UNTRACKED file. No other shell act on a file.
- **Editing**: the Edit file tool, one changed passage at a time.
- **Running**: only the tools this dispatch names, and git. **`git status`, and `git diff` without two explicit commit
  hashes, are forbidden** (`CLAUDE.md` Conventions, D-253) and the guard refuses them. Which paths changed is
  enumerated with `python tools/audit/changed_paths.py` (working tree) or `--staged`; what changed inside a file is
  read with `git diff <hashA> <hashB>` between two commits, by explicit hash taken from a commit command's own output.
  *(Corrected 2026-09-17 after the first run of this dispatch stopped at a guard refusal of `git status`. Former
  wording of this bullet: "only the tools this dispatch names, and git.")*
- **Never open, list, search or move anything under** `docs/research_papers/polyph9-release/`, `scratch_artifacts/`,
  `external resarch summary/`, `Claude outputs/`, `Codex research inventory/` or `.git/`.
- **If a guard refuses anything, STOP and report the refusal text verbatim.**

---

## TASK 0 — start state

**(a)** `git hash-object -w` on this dispatch. Record the identity; take later reads of it from `git cat-file blob`.

**(b)** `git rev-parse --abbrev-ref HEAD`, `git rev-parse HEAD`. **Not `master` at the base → STOP.**

**(c)** `python tools/audit/changed_paths.py` — capture the whole output into the report's appendix. It is the start
state every later difference is read against. Its docstring states its limits: it reports what git reports, and an
untracked DIRECTORY is one record, not one record per file.

**(d)** Run the guard set: `python tools/audit/gen_guard_state.py --check`. **Capture its whole output.** Its failing
set at this start state is the reference for Task 5. A failure present here is **reported, never corrected** by this
batch.

---

## TASK 1 — the population, and where each file goes

**(a) The files already mapped.** Every root file in the map's Task 1 §1.1, §1.2, §1.3 and §1.4, with its T / U mark
as listed there. (The check batch's check 4 found those lists and marks equal to the repository; re-confirm with one
Glob per pattern, keeping only results with no `/` in their path — the map's §"How this report was produced" records
that Glob recursed — and **STOP if any list differs**.)

**(b) Five further root files, added on the user's ruling that record files cannot stay at the root.** Confirm each
exists at the root with Glob, and its tracked status with `git ls-files -- "<name>"`:

- `cowork_owner_rulings_2026_08_07.md`
- `cowork_pending_rulings_2026_08_02.md`
- `cowork_document_route_rulings_2026_08_08.md`
- `cowork_instruction_return_session.md`
- `cowork_away_returns.md`

Then Glob the root for `cowork_owner_rulings_*.md`, `cowork_pending_rulings_*.md`,
`cowork_document_route_rulings_*.md` and `cowork_instruction_*.md`. **Any root file those patterns find that is not
named above → STOP**, naming it.

**(c) Destinations:**

| Files | Go to |
|---|---|
| `cowork_handoff_entry_*.md`, `cowork_handoff.md`, `cowork_handoff_archive.md`, `cowork_away_returns.md` | `records/cowork/handoff/` |
| `cowork_rulings_*.md`, `cowork_ruling_*.md`, `cowork_owner_rulings_*.md`, `cowork_pending_rulings_*.md`, `cowork_document_route_rulings_*.md` | `records/cowork/rulings/` |
| `cowork_instruction_*.md` | `records/cowork/instructions/` |
| `cc_instruction_*.md` | `records/cc/instructions/` |
| every other root `cc_*.md` | `records/cc/reports/` |

File names do not change. **If a destination already holds a file of the same name → STOP**, naming both.

**NOT in the move:** every other root `cowork_*.md` (the map's §1.5, including
`cowork_report_plan_evaluation_2026_08_21.md`), the directory `cowork_scratch_2026_08_11/`, and every file outside
the root.

---

## TASK 2 — move

Move every file of Task 1 to its destination: `git mv` for T, a plain move for U. **An untracked file stays
untracked; this batch adds no untracked moved file to git.**

Then `python tools/audit/changed_paths.py --staged` and `python tools/audit/changed_paths.py`, both captured.
**Proof, in the report:**
- every tracked moved file appears in the `--staged` output as a rename from its root name to its destination, and
  nothing else is staged;
- every untracked moved file is found by Glob at its destination and not at the root (the tool cannot show this,
  because an untracked directory is one record);
- the working-tree output differs from Task 0(c) only by those renames and by records for the destination folders.
**Any other difference → STOP.**

---

## TASK 3 — fix the references in CODE

**The rule.** A tool that, at the start state, reached a moved file at the root — by a built path, a root scan, a
prefix rule or an authored table keyed by a root name — is edited so that it reaches **the same file at its new
path**, and **its population and its output are otherwise unchanged**. A read at a fixed old commit (the map's
§2(b).1 group F, and any other `git show` / `git cat-file` / `ls-tree` at a named commit) is **not** edited: at that
commit the file was at the root.

**Where to find them.** Every tool in the map's §2(b).1 groups A, B, C and D, and §2(b).3 and §2(b).4. Group E names
tools that open root files which are **not** moving; of those, only the ones that open a file Task 1(b) adds
(`tools/audit/gen_discard_records.py` opens `cowork_away_returns.md`) are in scope. **Then**, because Task 1(b)'s
five files were outside the map's population, Grep every file of the types `*.py *.mjs *.js *.sh *.ps1 *.bat
*.cmake` for each of those five names, and read each hit under the same rule.

For each tool, read its hit lines and the surrounding function with Read **before** editing. A group-C tool that
classifies names taken from committed data is **not edited** unless Task 5 shows its guard failing because of this
batch.

**Bars:**
- **No file under `src/` is edited.** If the rule requires a `src/` edit → STOP, naming the file and line.
- No change to a tool beyond the path, the root scan's directories, the prefix rule's directory anchor, or a table
  key. **Any edit that would need more → STOP**, naming it.
- `tools/audit/check_reference_map.py` is **not** edited; it checks the map as of 2026-09-16.

**Report, per tool:** the file, each changed line before and after, and which rule-case it is. For a tool with no
guard mode, state for each changed path that a Glob finds exactly one file there.

---

## TASK 4 — fix the references in documents, by the map's §2(c) class

Read the map's §2(c).0 for the class rules. The filing convention is D-674 (`cowork_design_doc_template.md`).

- **LIVE** documents: every mention of a moved file **by its root name** is changed to its new path (for example
  `` `cowork_rulings_2026_08_17_session_start_read_sitting.md` `` → `` `records/cowork/rulings/cowork_rulings_2026_08_17_session_start_read_sitting.md` ``).
  **Nothing else on the line changes.** This includes `CLAUDE.md`, `ARCHITECTURE.md` and `cowork_handoff.md` (itself
  moved) wherever the map classes them LIVE.
  - `ARCHITECTURE.md`: a path in an existing sentence is changed; **no delegation is added, removed or reworded**.
    If any change there would do more than replace a path → STOP.
  - If `ARCHITECTURE.md` changes, `tools/audit/gen_specification_document_set.py`'s `GRADES` keys that name a moved
    file are changed to match (map §2(b).1 group D).
- **DATED** documents, including every moved file except `cowork_handoff.md` (LIVE, map §2(c).1): **not edited.** A dated record keeps the names it was written with.
- **GENERATED** files: **not hand-edited.** They change only through their generator in Task 5.
- **FROZEN** files: not touched.
- **UNDECIDED** files (among them every `open_items/OI-*.md` and `cowork_away_returns.md`): **not edited.** List in
  the report every UNDECIDED file that mentions a moved file by its root name.

**The decisions register.** In `tools/audit/decisions/backbone_decisions.json`, wherever an entry's home names a moved
file by its root name, that name is changed to the new path, and nothing else (`CLAUDE.md`, the decisions-register section,
rule (d)). It is regenerated in Task 5.

**`.gitignore` line 116**, `/cc_e2d_*.md`, is changed to `/records/cc/reports/cc_e2d_*.md`, so the files it covers stay
ignored after their move.

**Report, per document:** the file and each changed line before and after. **Proof:** for every changed line, the
line with the new path replaced by the root name equals the old line.

---

## TASK 5 — regenerate and re-run the guards

**(a)** `python tools/audit/decisions/gen_decisions_register.py`, then its `--check`, then `gen_cluster_dispositions.py
--verify` (locate that tool with Glob first; the writing side did not establish its directory). **The diff rule of (c)
applies to every file this step rewrites.**

**(b)** `python tools/audit/gen_guard_state.py --check`, captured whole. Compare with Task 0(d), guard by guard.

**(c)** For every guard that **passed at Task 0(d) and fails now**: run that tool's own write mode once, then its
check again. Name every artifact it rewrote. **The content of those rewrites is proved in Task 6, after Commit 2, by a
diff between two commit hashes.** A guard that failed at Task 0(d) is not regenerated.

**(d)** Every guard's result now equals Task 0(d)'s, or differs only as (c) allowed. **Otherwise → STOP.**

---

## TASK 6 — commit, STATUS.md, push

**Commit 1 — the moves only.** Every tracked rename from Task 2, nothing else.

**Commit 2 — references and regeneration.** Every edit of Tasks 3 and 4, every artifact Task 5 rewrote, and these
record files of the batches that prepared this move (confirm each exists with Glob; add each whether tracked or not):
- `records/cc/instructions/cc_instruction_root_records_reference_map_2026_09_16.md`
- `records/cc/reports/cc_report_root_records_reference_map_2026_09_16.md`
- `records/cc/instructions/cc_instruction_reference_map_check_2026_09_17.md`
- `records/cc/reports/cc_report_reference_map_check_2026_09_17.md`
- `tools/audit/check_reference_map.py`
- `tools/audit/reference_map_check.json`
- `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_nine.md`
- `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety.md`
- this dispatch, `records/cc/instructions/cc_instruction_root_records_move_2026_09_17.md`

**The content proof, after Commit 2 and before anything else.** Take both commit hashes from the commit commands' own
output. Run `git diff <Commit 1 hash> <Commit 2 hash>`. Check, and state in the report, that:
- every changed line in a Task 3 tool is one of the rule-cases Task 3 allows;
- every changed line in a Task 4 document or in `backbone_decisions.json` equals its old line once the new path is
  replaced by the root name;
- every changed line in an artifact a Task 5 generator rewrote is a moved file's root name becoming its new path.

**If any change goes beyond that → STOP: no Commit 3, no push.** Report the commit hashes and the lines; the user
decides. Nothing has left the machine at that point.

**Write the report (Task 7) now, before Commit 3.**

**Commit 3 — the close.** The report, and the `STATUS.md` entry for this batch, as a pointer to this batch's report, with the forward
bound performed as `STATUS.md`'s own head describes it (`tools/audit/gen_status_batch_bound.py` re-aimed at the
then-previous batch, this batch's entry written first, `--apply` second). Read that tool's docstring before running
it. **If the forward bound cannot be performed as described → do not guess: write the entry, skip the bound, and
report why.**

**Push.** `git push origin master`. Never `--force`. If the push fails, report the error verbatim; do not retry with
other options.

**Each commit message ends with the attribution lines your session's own instructions give.**

---

## TASK 7 — the report

Write, **with the Write file tool**, `records/cc/reports/cc_report_root_records_move_2026_09_17.md`, carrying: Task 0's
answers and captures; the population with each file's source, destination and T / U mark; the Task 2 proof; every
Task 3 and Task 4 change with its proof; the UNDECIDED list; Task 5's commands, outputs and comparison; the identities of
Commits 1 and 2. **Name members; state a total only as a sum of named members or as a figure a tool printed, cited to
that output** (D-431). The report is written before Commit 3 and included in it, so Commit 3's identity and the push
result go in the chat reply only.

At the foot of your chat reply give: the report's path, the dispatch blob identity, the three commit identities, and
the push result.

---

## DECLARED BY THE WRITING SIDE

- **What this batch's orders move:** the git object store; the Task 1 files (moved, not edited); the code files Task 3
  edits; the LIVE documents Task 4 edits; `tools/audit/decisions/backbone_decisions.json`; `.gitignore`; the artifacts
  the generators in Task 5 rewrite; `STATUS.md` and `STATUS_ARCHIVE.md` through the forward bound; the new report; three
  commits and one push. **No DATED, UNDECIDED or FROZEN document is edited, and no file under `src/`.**
- **The destinations of Task 1(b)'s five files, and the new `records/cowork/instructions/` folder, are the writing
  side's choice**, shown to the user before this batch was run. The rest of the layout is the one put to the user
  with the map dispatch.
- **What the writing side checked at the files before release:** the map's Task 1 headings, §2(b).1 whole, §2(c).0,
  §2(c).1, and its lines for the five files of Task 1(b); the check batch's report whole; the map dispatch whole;
  `.gitignore` whole; `gen_guard_state.py` lines 14–15, 36 and 55; `tools/audit/changed_paths.py` whole (after the
  first run stopped); the five §2(b).1 deciding lines the check batch did
  not confirm (all found as the map describes); `CLAUDE.md` rule (d) of the decisions-register section; `STATUS.md`
  whole. **Not read by the writing side:** the tools Task 3 edits beyond those lines, `gen_status_batch_bound.py`,
  `gen_decisions_register.py`, `gen_cluster_dispositions.py`, `backbone_decisions.json`, the map's §2(b).2, §2(b).3
  and §2(b).4, and the map's §2(c) lists beyond the lines named.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

- Task 0(b) not at the base.
- Any guard refusal.
- A Task 1 list differing from the map, or an unnamed file under Task 1(b)'s patterns, or a name collision.
- Any unexpected difference in Task 2's proof.
- A Task 3 edit needing a `src/` file or more than a path, scan directory, anchor or key.
- A Task 4 `ARCHITECTURE.md` change beyond a path.
- A Task 5 rewrite beyond name-to-path, or a guard result differing otherwise.
- **Any instruction here found false at the objects.**

**On a STOP after Task 2: do not undo the moves or any commit.** Report the exact state (`python
tools/audit/changed_paths.py` and `--staged`, captured, and any commit hashes) and stop; the user decides.

## WHAT THIS BATCH MAY NOT DO

Edit any DATED, UNDECIDED or FROZEN document, or any file under `src/`; hand-edit a generated file; rename a file;
move anything not in Task 1; add an untracked moved file to git; run any build or test; open, list or search the
excluded locations; use `--force`.
