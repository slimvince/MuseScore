# CC INSTRUCTION — RESUME of the passage-guards-historical batch after its STOP at Task 2(c), 2026-09-17

**WHAT THIS RESUMES.** `records/cc/instructions/cc_instruction_passage_guards_historical_2026_09_17.md`
(blob `f73726f66d8d4c870ed74bc328caca3b0d2e07e7`, per CC's reply) ran Task 0, Task 1 and Task 2(a)–(b) as
ordered and STOPPED at Task 2(c): after Task 1(c)'s `git restore` of `tools/audit/claude_md_finer_archive.json`,
the enumeration still carried a ` M` record for that path (568 records, capture blob
`8559351cea651f763634081bdbb8276f785fe34a`), where the dispatch expected it gone. Nothing was committed, nothing
pushed, nothing undone. **No report file was written for that run; the report this dispatch orders covers BOTH
runs.** Every rule of the original dispatch binds here unless this file says otherwise; read the original whole
from its blob before starting.

**THE BASE.** Branch `master` at **`49c6364242772d34c08b046d5972d5748a4d0763`**, unchanged. The working tree
carries, uncommitted: Task 1(a)'s insertion in `tools/audit/gen_guard_state.py`; Task 1(b)'s six edits in
`tools/audit/gen_guard_classification.py`; and `tools/audit/claude_md_finer_archive.json` as `git restore`
left it. **All three were read at the file by the writing side after the STOP and match the original dispatch's
Task 1** (the insertion at lines 1187–1210 before the closing `}`; the six edits at lines 993, 996–997, 1014,
1018–1019, 1344, 1348–1349; the restored artifact 122 lines, every line ending in CRLF).

**THE CAUSE IS NOT ASSUMED — TASK 0(e) MEASURES IT.** CC's reply offers a likely cause (the committed blob
carries CRLF) and says in terms it is not confirmed. The writing side did not confirm it either: the committed
blob cannot be read with the file tools. So this dispatch measures it by git object query, and the branch is
ruled below BEFORE the measurement is run. Do not reason past the measurement.

**The writing side does not touch this file, and lands nothing in the repository, while the batch runs (D-251).**

## THE ROUTE RULE

Unchanged from the original: **no shell command reads any file** (not `cat`, `head`, `tail`, `type`,
`Get-Content`, nor any other, nor in the scratchpad); every capture is written to the scratchpad, given an
identity with `git hash-object -w`, and read with Read or Grep; a commit hash is taken from `git commit`'s own
printed output; **add no command of your own** — any guard refusal → STOP; edit with the Edit file tool only.
The git object queries this dispatch orders are named below one by one; nothing else.

## TASK 0 — the state, and the measurement

**(a)** `git hash-object -w` on this dispatch. Record the identity. Every later read of this dispatch is
`git cat-file blob <that identity>`. Also `git cat-file blob f73726f66d8d4c870ed74bc328caca3b0d2e07e7` into the
scratchpad and read the original dispatch whole from it.

**(b)** `git rev-parse --abbrev-ref HEAD` and `git rev-parse HEAD`: `master` at
`49c6364242772d34c08b046d5972d5748a4d0763`, else STOP.

**(c)** `python tools/audit/changed_paths.py --staged`, captured: **no path record**, else STOP.

**(d)** `python tools/audit/changed_paths.py`, captured. Compare with
`git cat-file blob 8559351cea651f763634081bdbb8276f785fe34a` (the first run's Task 2(c) capture). **The only
differences allowed:**
- **new, untracked:** this dispatch;
- **new, untracked, IF PRESENT:** `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_four.md`
  (the writing side may land it while this runs; it is NOT committed by this batch — see Task 2(d) and Task 4);
- a difference only under `scratch_artifacts/` is reported, not a STOP.
Anything else → STOP. In particular the ` M` records for `tools/audit/gen_guard_state.py`,
`tools/audit/gen_guard_classification.py` and `tools/audit/claude_md_finer_archive.json` must all still be
present, and no other ` M` may have appeared.

**(e) THE MEASUREMENT — four git object queries and two Grep counts, all captured, none interpreted until (f).**
1. `git rev-parse 49c6364242772d34c08b046d5972d5748a4d0763:tools/audit/claude_md_finer_archive.json` — the
   committed blob's identity. Record it as BLOB_HEAD.
2. `git cat-file blob <BLOB_HEAD>` into the scratchpad (a capture; give it an identity as every capture gets).
   With Grep over that capture: the count of lines matching `\r$`, and the count of lines matching `.`.
   With Grep over the working-tree file `tools/audit/claude_md_finer_archive.json`: the same two counts.
   (The writing side measured the working-tree file at 122 and 122.)
3. `git hash-object -w --no-filters tools/audit/claude_md_finer_archive.json` — the working-tree bytes as a blob,
   with no line-ending conversion. Record it as BLOB_WT.
4. `git diff --ignore-cr-at-eol --stat <BLOB_HEAD> <BLOB_WT>`, captured. Both operands are explicit blob
   hashes, which is the object-query form D-253 admits.
5. `git ls-files --eol -- tools/audit/claude_md_finer_archive.json`, captured. It prints one line of the form
   `i/<eol> w/<eol> attr/<attributes> <path>` and no file content. This is the one index read this dispatch
   orders, and it is ordered because it names the index-side and working-tree-side line endings directly.

**(f) THE RULED BRANCH.** Read the captures of (e) with Read or Grep, then:
- **Branch A — the difference is line endings and nothing else:** the `--stat` output of (e)4 is EMPTY
  (no file listed, no insertions, no deletions), AND the `.`-line counts of (e)2 are equal for the blob and the
  working-tree file. Then the ` M` record on `tools/audit/claude_md_finer_archive.json` is a line-ending
  report over content that equals the committed record, and **it is ALLOWED at Task 1(b) below and at every
  later enumeration in this batch.** The file is never staged and never committed (it is one of the five
  excluded paths of the original Task 2(d)). Continue to Task 1.
- **Branch B — anything else:** any line in the `--stat` output, or unequal `.`-line counts, or a git error
  on any of (e)1–5. **STOP.** Report every capture with its identity. Do not restore, rewrite or regenerate
  the artifact.
Whatever (e)5 prints is REPORTED verbatim in either branch and decides nothing: the branch is decided by
(e)4 and (e)2 alone.

**(g)** Read whole: handoff entry 193 §1 (`records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_three.md`).

## TASK 1 — prove the tree is still the first run's Task 2 tree, then the task commit

**(a)** `python tools/audit/gen_guard_state.py --check`, captured whole. It must be **byte-identical** to
`git cat-file blob 3cf63b086a2418290b1d4f179dc5f4e9804462a6` (the first run's Task 2(a) capture; counts line
`78 guard(s) run, 15 failing, 4 not run, 19 historical record(s)`), else STOP.

**(b)** `python tools/audit/changed_paths.py`, captured. Against Task 0(d)'s capture: **no difference at all**
other than under `scratch_artifacts/`. (Under Branch A the ` M` for `tools/audit/claude_md_finer_archive.json`
is present and allowed.) Anything else → STOP.

**(c) Task commit, by explicit path only:** `tools/audit/gen_guard_state.py`;
`tools/audit/gen_guard_classification.py`; the original dispatch
`records/cc/instructions/cc_instruction_passage_guards_historical_2026_09_17.md`; this dispatch;
`records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_three.md`. Check with
`changed_paths.py --staged` before committing: **exactly those five.** **Never** `docs/research_papers/BIBLIOGRAPHY.md`,
`docs/research_papers/README.md`, `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_eight.md`,
`tools/audit/guard_state.json`, `tools/audit/guard_classification.json`, `tools/audit/claude_md_finer_archive.json`,
and never `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_four.md`. Record the hash as the
TASK COMMIT.

## TASK 2 — the report, covering both runs

Write with the Write file tool `records/cc/reports/cc_report_passage_guards_historical_2026_09_17.md` (Glob
first; if it exists → STOP). It carries:
- **the first run**, from CC's chat reply as the writing side received it: its Task 0 result, its Task 1 as
  made, its Task 2(a) and 2(b) results with their capture identities (`2781d206…`, `5a4aa703…`, `9554b6f3…`,
  `3cf63b08…`, `98d16ef8…`, `8559351c…`), the STOP at 2(c) and the ` M` record that caused it, and **its one
  declared departure** — `git config --get core.autocrlf`, run without being ordered, printing `true`;
- **this run**: Task 0(d) and (e) captures with identities, the (e)5 line verbatim, the branch taken at (f)
  and the two figures that decided it, Task 1(a)'s byte-identity, Task 1(b), and the task commit hash;
- name members; state a total only as a sum of named members or a figure a tool printed (D-431).
**(d)** If `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_four.md` is present in the
working tree, the report says so and says it was not committed; it is not opened.

## TASK 3 — the close and the push

As the original dispatch's Task 4, with these changes and no others:

1. **The `STATUS.md` entry** names BOTH dispatches (the original and this resume) and additionally states, in one sentence, what Task 0(e) measured about
   `tools/audit/claude_md_finer_archive.json` — under Branch A: that the working-tree copy equals the committed
   record except for line endings, that git reports it modified for that reason, and that it stays uncommitted
   as ruled. It restates no figure.
2. **The forward bound — the same TWO moves**, Move 1 catch-up on
   `cc_instruction_defense_share_authored_ends_2026_09_08.md`, Move 2 ordinary on
   `cc_instruction_root_records_move_finish_commit_three_2026_09_17.md`; `BASE_COMMIT` = this batch's TASK
   COMMIT (Task 1(c)); `DISPATCH` = **this** dispatch's file name; `TASK` = `"Task 3"`. The same fallback as the
   original, verbatim, if either move cannot be performed as the docstring and the precedent describe.
3. `python tools/audit/gen_session_start_read_size.py`, then `python tools/audit/gen_defense_share.py`. Any STOP
   or FAIL printed → STOP, no commit.
4. `python tools/audit/gen_guard_state.py --check`, captured: every guard's result equal to Task 1(a)'s capture,
   else STOP (no commit, no push).
5. **Close commit, by explicit path only:** `STATUS.md`; `tools/audit/session_start_read_size.json`;
`tools/audit/defense_share.json`; this batch's report; and **if the bound ran**, `STATUS_ARCHIVE.md`,
`tools/audit/gen_status_batch_bound.py` and `tools/audit/status_batch_bound.json`. Never the seven excluded
paths of Task 1(c). Check with `changed_paths.py --staged` before committing.
6. `git diff <TASK COMMIT> <close commit>`: changes only in those paths; the two measurement artifacts only in
   values that follow from `STATUS.md` changing (and `STATUS_ARCHIVE.md`, if the bound ran); the report a
   whole-file addition. Otherwise → STOP, no push.

**Push:** `git push origin master`. Never `--force`. A failure is reported verbatim, with no retry by other options.

At the foot of the chat reply: the report's path, this dispatch's blob identity, the branch taken at Task 0(f)
with its two deciding figures, the (e)5 line verbatim, the task commit and close commit hashes, whether the
bound ran, and the push result verbatim.

## DECLARED BY THE WRITING SIDE

- **Checked at the files after the STOP:** the two edited tools at the lines named above; the restored
  artifact's 122 lines and 122 CR-terminated lines (Grep over a staged copy); `gen_claude_md_finer_archive.py`
  line 592, which writes with `newline="\n"`; `.gitattributes`, whose `* text=auto` is the rule that reaches
  `tools/audit/*.json`; `tools/audit/changed_paths.py`, whose working-tree enumeration is
  `git status --porcelain=v1 -z` — so the ` M` is git's own report; both ref files at
  `49c6364242772d34c08b046d5972d5748a4d0763`.
- **Relayed, not checked:** every capture identity above and the first run's Task 0–2 results, from CC's chat
  reply; that `core.autocrlf` is `true`, from the same reply.
- **Not established:** the committed blob's line endings, and therefore the cause of the ` M`. Task 0(e)
  establishes it; the branch at (f) is ruled on the measurement's two figures and on nothing this side believes
  about git's conversion rules.
- **No decisions-register entry is written by this batch**, as the original says; the open point stands at entry
  193 §1.
- The ordinary session-start read still binds you (P-1, D-230).

## STOP CONDITIONS

Any Task 0 mismatch; Branch B at Task 0(f); any Task 1 difference not allowed; any excluded path staged; any
guard refusal; any Task 3 STOP; **any instruction here found false at the objects.** On any STOP: undo nothing;
report the captures and every commit hash; stop.
