# CC INSTRUCTION — the third backup: commit and push the record files uncommitted at f6b9fadc58, by explicit path, 2026-09-20

**THE BASE.** Branch `master` at **`f6b9fadc58cdff4e97364abb1c70deda7213243c`**, with `origin/master` equal. Both
ref files were read at that value by the writing side on 2026-09-20.

**WHY THIS EXISTS.** Since the second backup (`records/cc/instructions/cc_instruction_backup_second_commit_and_push_2026_09_19.md`),
Cowork sittings have written handoff entries, second extracts, corrected first extracts and the two
reading-pass progress records straight to disk, and no batch has committed them. Part of CC's own record files, now
under `records/cc/` and named below as THE CC RECORD GROUP, and one provenance record under
`tools/audit/derivation_exemplars/`, were untracked at each enumeration since 2026-09-16 that the writing side has read
(the reports of the two 2026-09-16 "second backup" runs and of the second backup). *(★ Corrected 2026-09-20 at the
source check, before hand-over. This note is not an instruction. Former wording, preserved (#12): "CC's own session
reports now under `records/cc/reports/`". That was wider than the fact: many reports there are tracked, and the group
also holds three dispatches under `records/cc/instructions/`.)* **If the disk fails, they are lost.** The user ordered on 2026-09-16 that such
files be committed and pushed as a backup (*"we need to instruct CC to commit and push all our extracts etc.
Otherwise they will be lost if my disc crashes"*, recorded at
`records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_eight.md` §5). **This batch is a backup and its
own close, and nothing else.** It commits the files named below as they stand on disk and writes its own report
(Task 2). It changes the content of no existing file except the ones its close orders by name (Task 3:
`STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`, and the three generated artifacts named
there).

**The writing side does not touch this file or any file on THE LIST, and lands nothing in the repository, while
the batch runs (D-251).**

## THE ROUTE RULE

- **No shell command reads any file.** That rules out `cat`, `head`, `tail`, `type`, `awk`, `Get-Content` and every
  other reader, and it applies in the scratchpad too. Read every capture with Read or Grep.
- Every capture: written to the scratchpad, given an identity with `git hash-object -w`, read with Read or Grep.
  **Name a scratchpad path literally in any command; never through a shell variable.** (A variable path was refused
  by the guard on 2026-09-16: `records/cc/reports/cc_report_second_backup_rerun_2026_09_16.md`.)
- Take a commit hash from the `git commit` command's own printed output (no `-q`, no redirect). **One exception,
  ordered here so it is not a departure:** run `git rev-parse HEAD` once immediately after the task commit (Task
  1(d)) and once after the close commit (Task 3.6), to expand each hash to forty characters.
- **Add no command of your own.** Any guard refusal → STOP.
- Edit files with the Edit file tool only. **No file on THE LIST is edited, opened for editing, re-saved or
  normalised.** They are committed as they stand.

## THE LIST — named members

Each line gives the path and **the size in bytes that the writing side read at a folder listing on 2026-09-20.**

Handoff entries, under `records/cowork/handoff/`:
1. `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_ninety_nine.md` — **28340**
2. `records/cowork/handoff/cowork_handoff_entry_two_hundred.md` — **11176**
3. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_one.md` — **18910**
4. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_two.md` — **22122**
5. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_three.md` — **23898**
6. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_four.md` — **28757**
7. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_five.md` — **25530**
8. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_six.md` — **28179**
9. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_seven.md` — **15925**
10. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_eight.md` — **29353**
11. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_nine.md` — **13841**
12. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_ten.md` — **6869**
13. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_eleven.md` — **5163**
14. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_twelve.md` — **9655**
15. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_thirteen.md` — **11870**
16. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fourteen.md` — **16631**
17. `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_fifteen.md` — **14910**

First extracts, under `reading_pass/extracts/`:
18. `reading_pass/extracts/burgoyne-pugin-kereliuk-fujinaga-2007-a-cross-validated-study-of-modelling-strategies-for-automatic-chord-recognition-in-audio.md` — **55875**
19. `reading_pass/extracts/ju-conditschultz-arthur-fujinaga-2017-non-chord-tone-identification-using-deep-neural-networks.md` — **51246**
20. `reading_pass/extracts/ju-howes-mckay-conditschultz-calvozaragoza-fujinaga-2019-an-interactive-workflow-for-generating-chord-labels.md` — **90247**
21. `reading_pass/extracts/declercq-2015-a-model-for-scale-degree-reinterpretation.md` — **85707**
22. `reading_pass/extracts/harasim-rohrmeier-odonnell-2018-a-generalized-parsing-framework-for-generative-models-of-harmonic-syntax.md` — **96055**
23. `reading_pass/extracts/rohrmeier-2006-towards-modelling-harmonic-movement-in-music.md` — **60160**
24. `reading_pass/extracts/rohrmeier-2011-towards-a-generative-syntax-of-tonal-harmony.md` — **69448**
25. `reading_pass/extracts/pardo-birmingham-2002-algorithms-for-chordal-analysis.md` — **30880**
26. `reading_pass/extracts/temperley-sleator-1999-modeling-meter-and-harmony.md` — **23476**
27. `reading_pass/extracts/bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md` — **15530**
28. `reading_pass/extracts/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md` — **21109**

Second extracts, under `reading_pass/extracts_second_pass/` (each carries the same file name as the first extract
above it in the same position):
29. `reading_pass/extracts_second_pass/burgoyne-pugin-kereliuk-fujinaga-2007-a-cross-validated-study-of-modelling-strategies-for-automatic-chord-recognition-in-audio.md` — **59729**
30. `reading_pass/extracts_second_pass/ju-conditschultz-arthur-fujinaga-2017-non-chord-tone-identification-using-deep-neural-networks.md` — **46339**
31. `reading_pass/extracts_second_pass/ju-howes-mckay-conditschultz-calvozaragoza-fujinaga-2019-an-interactive-workflow-for-generating-chord-labels.md` — **64009**
32. `reading_pass/extracts_second_pass/declercq-2015-a-model-for-scale-degree-reinterpretation.md` — **72089**
33. `reading_pass/extracts_second_pass/harasim-rohrmeier-odonnell-2018-a-generalized-parsing-framework-for-generative-models-of-harmonic-syntax.md` — **70641**
34. `reading_pass/extracts_second_pass/rohrmeier-2006-towards-modelling-harmonic-movement-in-music.md` — **69002**
35. `reading_pass/extracts_second_pass/rohrmeier-2011-towards-a-generative-syntax-of-tonal-harmony.md` — **57095**
36. `reading_pass/extracts_second_pass/pardo-birmingham-2002-algorithms-for-chordal-analysis.md` — **64071**
37. `reading_pass/extracts_second_pass/temperley-sleator-1999-modeling-meter-and-harmony.md` — **52372**
38. `reading_pass/extracts_second_pass/bigo-feisthauer-giraud-leve-2018-relevance-of-musical-features-for-cadence-detection.md` — **50846**
39. `reading_pass/extracts_second_pass/karystinaios-widmer-2022-cadence-detection-graph-neural-networks.md` — **55641**

The two reading-pass progress records, under `reading_pass/`:
40. `reading_pass/l2_slice_reading_progress.md` — **416448**
41. `reading_pass/candidacy_upgrades.md` — **39674**

The provenance record of the one derivation exemplar:
42. `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.provenance.md` — **9600**

And this dispatch:
43. `records/cc/instructions/cc_instruction_backup_third_commit_and_push_2026_09_20.md` — no size is given for it.

## THE CC RECORD GROUP — members named by reference, not retyped

**The members are exactly the paths printed in the two code blocks of §2 of
`records/cc/reports/cc_report_backup_second_commit_and_push_2026_09_19.md`**, the second backup's report, committed
in that batch's close. Those blocks are the one under *"Under `records/cc/instructions/`:"* (three paths) and the one
under *"Under `records/cc/reports/`:"*. They hold that run's untracked records under `records/cc/`, all `??`
then. **This dispatch retypes none of those names, so that no name can be mistyped; read them at that report.** The
group includes the three 2026-09-16 "second backup" dispatches and that day's two reports. **They are committed as
records only. None of them is to be run.** The first and third of those dispatches give their base as `5d24edb565…`
in their opening lines, and the re-run's report records its base check at that commit. The writing side did not open
the second dispatch.

## NEVER STAGED, at the task commit or at the close

`tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`; `tools/audit/claude_md_finer_archive.json`;
`tools/audit/guard_state.json`; `tools/audit/guard_classification.json`; anything under `src/`; any `.pdf`; anything
under `docs/research_papers/`; and any path not named in this dispatch or in THE CC RECORD GROUP. **Open nothing
under `docs/research_papers/`, and do not open the `.mscx` file.**

## TASK 0 — the state

**(a)** `git hash-object -w` on this dispatch. Record the identity. Every later read of this dispatch is
`git cat-file blob <that identity>`.

**(b)** `git rev-parse --abbrev-ref HEAD` and `git rev-parse HEAD` must print `master` and
`f6b9fadc58cdff4e97364abb1c70deda7213243c`, else STOP. `git remote -v`: `origin` must be
`https://github.com/slimvince/MuseScore` for fetch and for push, else STOP.

**(c)** `python tools/audit/changed_paths.py --staged`, captured: it must list **no path record**, else STOP.

**(d)** `python tools/audit/changed_paths.py`, captured. Then, reading the capture with Read or Grep:

- **(i) THE LIST.** Look up each of members 1 to 43 in the capture. **Expected, not required:** members 18 to 28,
  29, 40 and 41 carry a modified record (` M`). Members 1 to 17, 30 to 39 and 43 carry an untracked record (`??`).
  **Member 42 is expected to carry no record of its own and to fall inside the untracked directory record
  `tools/audit/derivation_exemplars/`.** For that case, Glob `tools/audit/derivation_exemplars/**`. If it returns
  exactly member 42 and the `.mscx` file named under NEVER STAGED, member 42 is staged. Any other member of that
  directory is reported and not staged, and is not a STOP.
  **A member whose record is of the other kind is reported and is still staged. Any other member with NO record in
  the capture is reported, Glob-checked for existence, and NOT staged.** A file that exists with no record is
  either already committed as it stands or ignored. Report it either way and add no command to tell which.
  **A member that does not exist on disk → STOP.**
- **(ii) THE CC RECORD GROUP.** Read the report's §2 with the Read tool. **Every record in the capture under
  `records/cc/` must be a `??` record, and its path must be either a member of THE CC RECORD GROUP or member 43.**
  Any other record under `records/cc/`, of any kind → STOP. That includes any ` M`, `D` or `R` record there, and
  any `??` record not in the group. (Task 1 stages this group by its two directories, so an unexpected record there
  would be swept in.) **A group member with no record in the capture is reported and is not a STOP.** Name those
  members in the report; do not list the others one by one. State the group's size only as a number a tool printed
  (D-431).
- **(iii) THE STAGING SET** is: the members of THE LIST that (i) admits for staging, plus every group member that has
  a `??` record. Name the LIST part in the report member by member.
- **(iv)** Every ` M` record not in THE STAGING SET is named in the report. `tools/audit/claude_md_finer_archive.json`
  is expected among them. The second backup's report records it as a ` M` record on 2026-09-19. What modified it has
  not been established. It is not a STOP and it is not staged. **A modified, deleted or renamed record under
  `src/` → STOP.** An untracked `??` record under `src/` is reported and is not a STOP.
- **(v)** Every record under `records/cowork/handoff/` or `reading_pass/` that is NOT in THE STAGING SET is named in
  the report and is **not staged**. Records elsewhere are not listed one by one; the capture's identity stands for
  them.

**(e)** `python tools/audit/gen_guard_state.py --check`, captured whole. The run may exit 1 when the failing set is
not empty; that exit code is not a STOP. **This capture is the reference for Task 3.4.** Report its counts line, and
whether that line equals the closing counts line recorded by
`records/cc/reports/cc_framework_dp_c_correction_second_report_2026_09_20.md`, in its subsection headed *"(d) The guard
set after the edit"*. **A difference is reported and is not a STOP.** Untracked record files may be read by a guard, and the
writing side has not established that none is.

**(f) The size check, by git object and not by a shell read.** For each member of THE LIST that is in THE STAGING SET,
except member 43: `git hash-object -w --no-filters <path>`, then `git cat-file -s <the identity it printed>`. **The
size printed must equal the figure on THE LIST. Any difference → STOP, stage nothing, and report every size found.**
The figures are of the bytes on disk, which is what `--no-filters` hashes. No member's line endings were measured by
the writing side.

**(g) The tail check, with the Read file tool.** For the same members as (f): read each file's closing lines. A
Grep count of lines matching `^` gives the line count; Read from five lines before it. **The last non-empty line must
be ordinary text. A file ending in NUL bytes, or an empty file → STOP.** Report the first 60 characters of each last
non-empty line.
**THE CC RECORD GROUP gets no size check and no tail check, and that is a declared bound.** Its reports were written by
CC. Its three 2026-09-16 dispatches are dispatches, which the writing side writes (D-252) and lands through the Cowork
bridge whose fault the size check exists for. No member carries a size the writing side read for this list. *(★
Corrected 2026-09-20 at the source check, before hand-over. This note is not an instruction. Former wording, preserved
(#12): "No member of it was written through the Cowork bridge, whose fault the size check exists for, and none carries
a size the writing side read." Its first half was never established, and it is contrary to D-252 for the three
dispatches.)* A
member truncated on disk would be committed as it stands. **A commit destroys nothing**: the disk copy is no worse for
being backed up.

## TASK 1 — the task commit

**(a)** Stage THE STAGING SET in two parts:
- **THE LIST part:** by explicit path, one `git add -- <path>` per member or one command naming them all.
- **THE CC RECORD GROUP:** `git add -- records/cc/reports records/cc/instructions`. **This is the one directory
  pathspec this batch uses, and Task 0(d)(ii) is what makes it safe.** Every record in those two directories was
  established there as a group member or member 43.
**Never `git add -A`, `git add .`, `git add -u` or any glob.** A line-ending warning printed by `git add` is reported
verbatim (a count of the warnings, as the tool printed them, and the first and last warning in full) and is not a
STOP.

**(b)** `python tools/audit/changed_paths.py --staged`, captured. It must show **exactly THE STAGING SET and nothing
else**: THE LIST part as named at Task 0(d)(iii), and under `records/cc/` exactly the group members that carried a
record, plus member 43, which is also on THE LIST. *(★ Corrected 2026-09-20 at the source check, before hand-over. This
note is not an instruction. Former wording, preserved (#12): "and under `records/cc/` exactly the group members that
carried a record." It left out member 43, which is under `records/cc/instructions/`, so a literal reading could have
fired a false STOP.)* Anything else → `git restore --staged -- <every staged path>` and STOP.

**(c)** Commit with this message, verbatim (the standing `Co-Authored-By` trailer may follow it):

```
Third backup: record files uncommitted at f6b9fadc58 (user-ordered)

Commits, as they stand on disk, the handoff entries, first and second extracts,
reading-pass progress records, one derivation-exemplar provenance record and CC's
untracked session records uncommitted at f6b9fadc58. No file content changed by this
commit.
Dispatch: records/cc/instructions/cc_instruction_backup_third_commit_and_push_2026_09_20.md
```

**(d)** Record the hash `git commit` printed, then run `git rev-parse HEAD` once. The forty characters it prints must
begin with the printed hash, else STOP. That forty-character value is the **TASK COMMIT**.

## TASK 2 — the report

Write with the Write file tool `records/cc/reports/cc_report_backup_third_commit_and_push_2026_09_20.md`. Glob first;
if it exists → STOP. It carries:
- this dispatch's blob identity;
- Task 0(b) and (c);
- Task 0(d): the capture identity; THE LIST part of THE STAGING SET by name, each member's record kind against the
  expected kind; the group members without a record, by name; every ` M` record not staged; and every record under
  the two named directories that was not staged;
- Task 0(e): the capture identity and counts line, and whether that line equals the previous batch's;
- every size from Task 0(f) against its figure, and every tail line from Task 0(g);
- Task 1(a)'s output as ordered there, Task 1(b)'s capture, and the task commit.

Name members, and state a total only as a sum of named members or as a number a tool printed (D-431). **Write in the
report, before the close commit, everything known before it** — the expected close path list and the Task 3.4
verdict — so that an interrupted chat reply loses only the close hash and the push line.

## TASK 3 — the close and the push

Close as the second backup's Task 3 did, as run and described in its report §7. Read that section before starting.
One forward-bound move.

1. **The `STATUS.md` entry**, written first, at the top of the dated entries, in the file's pointer convention,
   taking the `Last updated: ` prefix. Demote the previous batch's entry to a plain dated entry in the same edit. The
   entry names this dispatch. It says that this batch is a backup commit of record files by explicit path, on the
   user's order of 2026-09-16 recorded at handoff entry 188 §5, and that no file content was changed by the task
   commit. It points at this batch's report and restates no figure.
2. **The forward bound — ONE ordinary move.** Before editing, read `tools/audit/gen_status_batch_bound.py`'s docstring
   and its whole comment block above `PREVIOUS_AIMINGS`. Re-aim the authored inputs:
   - `BASE_COMMIT` = the TASK COMMIT (forty characters);
   - `PREVIOUS_BATCH_DISPATCH = "cc_instruction_framework_dp_c_correction_second_2026_09_20.md"`. The newest
     `STATUS.md` entry at the base names that dispatch.
   - `ACT_DATE` = the day this runs;
   - `DISPATCH = "cc_instruction_backup_third_commit_and_push_2026_09_20.md"`;
   - `TASK = "Task 3"`;
   - `MOVE_KIND = "ordinary"`.

   **Append THIS batch's own aiming to `PREVIOUS_AIMINGS`.** Do not append the replaced one: the framework batch's
   aiming is already the list's last row, recorded by that batch in its own act. This follows the tool's convention
   that each batch appends its own aiming, as the two most recent `★` blocks above `BASE_COMMIT` state. Extend the
   authored comments as those blocks do: add a new `★` block, and a sentence in `TASK`'s running list. Then run
   `--apply`, then `python tools/audit/gen_status_batch_bound.py --check`, which must exit 0.
   **The two nameless 2026-09-02 entries in `STATUS.md` stay where they are.** The tool's own comments record that no
   aiming can identify them. That is a declared state, not a STOP.
   **If the move cannot be performed as the docstring and the precedent describe:** run
   `git restore --source=HEAD --worktree -- STATUS.md STATUS_ARCHIVE.md tools/audit/gen_status_batch_bound.py
   tools/audit/status_batch_bound.json`. Then write this batch's `STATUS.md` entry again exactly as in step 1, with
   one added sentence saying the bound was not performed and why, skip the bound, and report the tool's message
   verbatim. That is not a STOP.
3. `python tools/audit/gen_session_start_read_size.py`, then `python tools/audit/gen_defense_share.py`. Any STOP or
   FAIL printed → STOP, no commit.
4. `python tools/audit/gen_guard_state.py --check`, captured. Every guard's result must equal Task 0(e)'s capture,
   else STOP (no commit, no push).
5. **Close commit, by explicit path only:** `STATUS.md`; `tools/audit/session_start_read_size.json`;
   `tools/audit/defense_share.json`; this batch's report; and, **if the bound ran**, `STATUS_ARCHIVE.md`,
   `tools/audit/gen_status_batch_bound.py` and `tools/audit/status_batch_bound.json`. Check with
   `changed_paths.py --staged` before committing that exactly those paths are staged. Message:
   `Close: third backup commit and push, 2026-09-20`.
6. Run `git rev-parse HEAD` once, for the close commit's forty characters. Then `git diff <TASK COMMIT> <close commit>`.
   It must show changes only in the close commit's paths; the two measurement artifacts changed only in values that
   follow from `STATUS.md` changing (and `STATUS_ARCHIVE.md`, if the bound ran); and the report as a whole-file
   addition. Otherwise → STOP, no push.

**Push:** `git push origin master`. Never `--force`, never `--force-with-lease`, never to `upstream`, no other branch.
A failure is reported verbatim, with no pull, merge, rebase, or retry with other options.

At the foot of the chat reply: the report's path, this dispatch's blob identity, the task commit and close commit
hashes, whether the bound ran, and the push result verbatim.

## THE FOOTPRINT — what this batch's own orders touch, and nothing else

**Committed as they stand, content unchanged:** THE STAGING SET. **Created:** this batch's report. **Edited:**
`STATUS.md`. **Written by `--apply`:** `STATUS_ARCHIVE.md` and `tools/audit/status_batch_bound.json`. **Written by
the two generators:** `tools/audit/session_start_read_size.json` and `tools/audit/defense_share.json`. **No tool source
is edited, except the forward bound's own per-batch re-aiming of `tools/audit/gen_status_batch_bound.py`, EXCEPTED BY
NAME** (Ruling 5 of `records/cowork/rulings/cowork_rulings_2026_08_26_amendment_landing_sitting.md`). No `src/`
file, no build, no test, no golden, no corpus, nothing under `tools/corpus/` or `tools/robust_stop/`, no measurement
of the analysis. No decisions-register entry, and no open-items row created, flipped or discarded. The ordinary
session-start read still binds you (P-1, D-230).

## DECLARED BY THE WRITING SIDE

- **Checked at the files on 2026-09-20:**
  - both ref files read `f6b9fadc58cdff4e97364abb1c70deda7213243c`;
  - every size on THE LIST, at folder listings of `records/cowork/handoff/`, `reading_pass/`,
    `reading_pass/extracts/`, `reading_pass/extracts_second_pass/` and `tools/audit/derivation_exemplars/`;
  - `.gitignore`, whose one `records/cc` pattern is `/records/cc/reports/cc_e2d_*.md`;
  - the second backup's dispatch and report whole;
  - the 2026-09-16 first "second backup" report at its opening, the re-run report whole, and the openings of the
    first and third 2026-09-16 dispatches;
  - `tools/audit/gen_status_batch_bound.py` at lines 330–459 and 730–790: its current aiming and the last rows of
    `PREVIOUS_AIMINGS`;
  - the framework correction's second dispatch at §0–§1 and §4–§7, and its report at its close section;
  - `STATUS.md` whole.
- **How THE LIST was drawn, and its bound.** Members 1 to 41 are every file under `records/cowork/handoff/`,
  `reading_pass/`, `reading_pass/extracts/` and `reading_pass/extracts_second_pass/` whose modification time at the
  listing is later than the second backup's dispatch (1789784675459). *(★ Added 2026-09-20 at the source check. The
listings meant are those made before handoff entry 216 landed. Entry 216 is later than that time and is excepted
under "Not in this batch" below. A second session re-listed the same directories on 2026-09-20 and found the same 41
files, each at its figure. It found no other file later than that time in those four directories, in
`reading_pass/cross_checks/`, `reading_pass/object_reads/`, `records/cowork/rulings/` or
`records/cowork/instructions/`.)* Member 42 is older than that. It is on THE LIST
  because it was untracked at the enumerations named above and entry 188 §5 recommended it for backup. Every member's
  size was read at those listings. **The listings reach only those directories.** Other changed paths in the tree are
  found by Task 0(d)'s capture, and the report names the ones in the directories Task 0(d)(v) names.
- **Relayed, not checked:**
  - that the framework correction's close committed its two dispatches and two reports (handoff entry 210 §0);
  - which members are tracked. The expected kinds at Task 0(d)(i) rest on the first backup having committed every
    path under `reading_pass/` as an addition, which the second backup's dispatch relays from the first backup's
    report;
  - that the `.mscx` held back is recomputable from a tracked archive. That is the reason the third 2026-09-16
    dispatch gives for holding it back, resting on the re-run's premise 4. **Whether it belongs in the public fork
    was never put to the user; it stays held back.**
- **Not in this batch, named so the omission is not mistaken for a miss:**
  - held back until the user says whether they belong in a public fork, as entry 188 §5 holds them: `Claude outputs/`,
    `Codex research inventory/`, `scratch_artifacts/`, `external resarch summary/`, `docs/research_papers/polyph9-release/`
    and the `.mscx` above;
  - also left out: `tools/audit/claude_md_finer_archive.json`, whose modification's cause is unknown; any root
    `cowork_*.md` document (the writing side listed no repository root);
  - carrying no record at the second backup's capture: the stray `reading_pass/extracts/lafferty-mccallum-pereira-2001-conditional-random-fields-for-segmenting-and-labeling-sequence-data-1.md`
    and `records/cowork/handoff/cowork_handoff_entry_one_hundred_and_eighty_two-1.md`;
  - **handoff entry 216**, which the writing side lands before this dispatch is handed over and which is therefore
    reported at Task 0(d)(v), not staged.

## STOP CONDITIONS

- Any Task 0(b) or 0(c) mismatch.
- A member of THE LIST missing from disk.
- An unexpected record under `records/cc/`.
- A changed record under `src/`.
- Any size different from its figure, or any tail that is not ordinary text.
- Any staged path outside THE STAGING SET.
- Any guard refusal, any Task 3 STOP, or any push rejected.
- **Any instruction here found false at the objects.**

On any STOP: undo nothing beyond the unstaging Task 1(b) orders; report the captures and every commit hash; stop.
