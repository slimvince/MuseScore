# CC dispatch — THE PRUNING ITERATION, STEP 4's SECOND DISPATCH: THE PER-SESSION READING MEASUREMENT EXTENDED (WHAT A DISPATCH OR REPORT SHARES WITH ITS PREDECESSOR; THE APPENDIX FILE BESIDE A REPORT; RULING 2's AFTER-FIGURE) AND RE-RUN, BEFORE AND AFTER SIDE BY SIDE; ONE STALE TOOL COMMENT CORRECTED — MEASUREMENT AND DOCUMENTATION ONLY; NO ALGORITHM CHANGE (2026-11-02)

> **STATUS: RELEASED 2026-11-02**: written, checked at its sources in a turn of its own, corrected and released by the
> Cowork sitting booted on `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_five.md`. The check is
> recorded at the end of this file with every former wording. *(Former wording of this banner's first sentences,
> preserved (#12): "**STATUS: WRITTEN 2026-11-02 — NOT YET RELEASED** by the Cowork sitting booted on `…_seventy_five.md`.
> Its check at its sources runs in a turn of its own; this banner is set to RELEASED only after that check, which is
> recorded at the end of this file with every former wording. **Until then this dispatch is NOT handed to Claude
> Code.**")* It is executed by Claude Code when the user
> hands it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that
> step and report it. Do not continue to the next one, and do not resolve an exclusion that contradicts a task.**
>
> **THE WRITING SIDE'S RESTRAINT, declared.** Once released this dispatch is final. The writing side will not touch it,
> nor any file it names, while this batch runs. The one file the writing side writes after this dispatch lands and before
> hand-over is its handoff entry `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_six.md`, which is
> why Task 0 states no size for it. **Entry 476 and this dispatch are NOT in git**; Task 0 lands them.

## What this batch is, in plain words

On 2026-11-01 the user ruled four things about shrinking what every session must read before it works
(`records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`, called ***the record*** below; its §1
to §4 are ***Ruling 1*** to ***Ruling 4***). Ruling 3 was committed by the third execution dispatch (RELAYED, the
fourth dispatch's line 21) and Ruling 1 by the fourth
(`records/cc/instructions/cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md`, called ***the fourth
dispatch***; its report `records/cc/reports/cc_report_pruning_rulings_fourth_execution_2026_11_02.md`, called ***the
fourth report***). Rulings 2 and 4 bind each dispatch's form, and the fourth run followed both (the fourth report §1 and
§10).

What the plan still owes before the user's next questions is a **measurement**, done by extending the existing tool
`tools/audit/gen_per_session_reading.py` (called ***the tool***; its artifact `tools/audit/per_session_reading.json`,
called ***the artifact***). Three additions, each named in the record or in the handoff entry that carried it out:

1. **The invariant share** (handoff entry 464 §1 and §2 item (iv)): for each dispatch and each report of the L3
   comparison arc, how many of its characters stand on lines it shares word for word with the dispatch or report before
   it. This sizes how much of a dispatch merely restates its predecessor — the figure the user's ruling on the dispatch
   form (the plan's candidate (d)) waits for.
2. **The appendix file beside a report** (Ruling 4, *"the measurement tool sizes the appendix file beside the report
   from then on"*): a report's raw printouts now go in a separate file beside it; the tool sizes that file.
3. **Ruling 2's after-figure** (Ruling 2's bound: *"the step-4 dispatch's re-run of the measurement carries the
   after-figure"*): the Claude Code side's per-batch total once the injected copy of `CLAUDE.md` is the read of its six
   session-start spans.

Then the measurement is re-run, and **the values before the pruning rulings stand beside the values after them** in the
report (Task 3(d)).

**One more act, small and separate (Task 1):** a comment in `tools/audit/gen_derivation_boot_pack.py` still says *"all
three subjects being spent"*; five subjects are built and all five are now frozen. The user's rule of 2026-09-22 —
staleness is fixed without asking — covers it.

**Documentation and algorithm, separated as the user requires.** **Measurement and documentation only:** one measurement
tool extended (the tool), one comment in a second tool corrected, the artifacts the steps regenerate, `STATUS.md`,
`STATUS_ARCHIVE.md` and this batch's records. **Algorithm:** NOTHING changes. No specification of the analysis is touched;
no measurement of the analysis is run. The currently decided method for L3 is `FRAMEWORK.md` §5's L3 block with DP-I,
untouched and unread. **This batch decides nothing** and moves no text out of any governing document.

---

## ★ THE ORDERED FIRST READ (carries Ruling 2 of the record)

**★ YOUR FIRST TOOL CALL IS ONE READ OF THIS FILE, AND NOTHING ELSE IN THAT CALL.** Do not read `STATUS.md`,
`DECISIONS.md`, `CLAUDE.md` or anything else in that call, and do not issue any other read in parallel with it. If the
read returns a partial view at the tool's page limit, read this file whole in further ranges of the same file before
anything else, and declare it.

**Then take the two cited texts into scratch files**, each command in its own call, each hash written literally, each
scratch file named by its absolute path outside the repository:

- **The fourth dispatch:** `git rev-parse 08274008d07b7e102a692f59eaedb0905860c39f:records/cc/instructions/cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md`
  (expected `50edaf8582a3748089caffe03641a3629ed68c62` — RELAYED from the fourth report §3 0(a)), `git cat-file -s` of it
  (expected `51166`), then `git cat-file blob` of it into a scratch file. **That scratch file is *the fourth dispatch*;
  every line number below that names it is a line of it.** A different blob or a `bad object` is a STOP-and-report.
- **The third dispatch:** blob `6d59532fff7f64280e4daf3bc8cc588fd68d2acc` (expected size `41161`; RELAYED from the fourth
  report §1), into a scratch file. **That scratch file is *the third dispatch*.**

**Ruling 2's eight-line check, exactly as the fourth run performed it** (the fourth report §1: the first line, the six
span heading lines and the last line carrying text, each read at the tree with the file tools and compared with the
injected copy; the six-span read only if a line differs or is missing, reported as a finding). Report the eight lines as
read and as injected.

Then, in this order:

1. `STATUS.md` whole; `DECISIONS.md` whole; `BUILD_AND_TEST.md` whole; `gating_ids` at
   `tools/audit/nongating_apparatus_rows.json`.
2. `cowork_audit_protocol.md` from the line `## The dispatch protocol these audits are commissioned and run under` to the
   end of the file, whole.
3. **The record whole** (28,805 bytes at this side's staging result).
4. **The handoff entries 475 and 476 whole** (`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_five.md`
   and `…_seventy_six.md`). **Entry 476 is the current handover block.**
5. **The fourth report whole** (the report proper; 43,279 bytes at this side's staging result); its appendix only where
   a step below names it.
6. **The fourth dispatch whole**, and **the third dispatch at its lines 380 to 433** (its Task 3 and Task 4, which the
   fourth dispatch's Task 3 and Task 4 cite).
7. **The tool, `tools/audit/gen_per_session_reading.py`, whole** (51,784 bytes at this side's staging result).
8. **For Task 1:** `tools/audit/gen_derivation_boot_pack.py` at `build()`, located by searching for the comment line
   containing *"all three subjects being spent"*, read from the comment opening *"EVERY SUBJECT IS STILL BUILT IN FULL"*
   to the `for subject in sorted(WITHHELD):` line after it.

**Not read, and not needed:** the first and second pruning dispatches, the step-1 measurement dispatches, the L3 reading
file, the derivation, `FRAMEWORK.md`. Declare any further read you make.

---

## ★ WORDS USED IN THIS DISPATCH, EXPLAINED FIRST

- ***The start tip*** — `08274008d07b7e102a692f59eaedb0905860c39f`, the commit both ref files named when this dispatch
  was written (the fourth run's end-state commit).
- ***`<T0>`, `<T1>`, `<T2>`*** — THIS batch's Task 0, Task 1 and Task 2 commits. ***`<ACT_DATE>`*** — the day the step
  runs, written `YYYY-MM-DD`.
- ***The arc*** — the L3 comparison arc: the dispatches whose names open `cc_instruction_l3_comparison_tabulation_` and
  the reports whose names open `cc_report_l3_comparison_tabulation_` (the tool's own `DISPATCH_PREFIX` and
  `REPORT_PREFIX`).
- ***A member's predecessor*** — the member just before it in its population's own order, which the tool already
  computes: by add-commit time, then by name (`population_rows`). The first member has none.
- ***Shared with its predecessor*** — defined exactly in Task 2(b)'s code: a line of the member, with its line ending,
  counts as shared when the predecessor holds the same line not already matched; the order of lines is ignored;
  whitespace-only lines are counted apart and are not in the share. **It is a line measure, not a judgement of copying:**
  a line changed by one character counts as not shared, and a short common line (a `---` rule, a fence) counts as shared
  wherever it stands.
- ***The invariant share*** — the shared characters as a percentage of the member's own characters.
- ***An appendix file*** — under Ruling 4, `<stem>_appendix.md` beside the report `<stem>.md` in `records/cc/reports/`.
- ***The report proper*** — the report file itself, without its appendix.
- ***The before-artifact*** — the artifact at the commit `d17a84afdbfbf78c16ff4514df63185fad114a5c`, the close of the
  step-1 measurement's remainder batch, from which the record says every figure it rests on was read (the record's
  header). ***The after-artifact*** — the artifact as this batch's close leaves it.
- ***The opening capture*** — the output of `python tools/audit/gen_guard_state.py --check` taken at 0(f), saved whole.
  ***A capture*** taken later is the same command; ***compared verdict by verdict*** means every tool's PASS / FAIL /
  NOT RUN / HISTORICAL line set side by side, and the tally line.

---

## Ruling ledger

- **Ruling 4 of the record** — the appendix file and *"the measurement tool sizes the appendix file beside the report
  from then on, so the share the printouts take is measured rather than estimated."*
- **Ruling 2 of the record** — its bound: *"The saving is the six spans' 105,876 less the check's own reads, not
  measured; the step-4 dispatch's re-run of the measurement carries the after-figure."*
- **Candidate (d), as the record's provenance and handoff entry 464 §1 carry it** — the dispatch form's invariant share
  *"is NOT sized by table 1 and goes to measurement first (D-254), as an addition to the measurement tool in step 4's
  dispatch"*; entry 464 §2 item (iv) defines it: *"for each arc dispatch and report, the characters shared verbatim with
  its predecessor against its own"*, *"proved on planted faults as the standing new-tool rule requires, the tool's
  `--check` re-proved"*.
- **The user's rule of 2026-09-22** — staleness and apparent errors in the record are fixed without asking him; it does
  not extend to a verdict, a measured value or a finding. Task 1 is a comment.
- **No new rule is made.** Every choice of definition in Task 2 is the writing side's, written into the tool's docstring
  and the artifact so the user can challenge it there.

---

## Premise ledger (written 2026-11-02 by the writing side from staged working-tree copies read with the file tools; no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
  `08274008d07b7e102a692f59eaedb0905860c39f`.
- **FACT — the chain**, read at `.git/logs/HEAD` lines 2092 to 2096: `1126176e…` → `bfd15c7fdd6e010a2ad163cfb0dddd26e46239a1`
  (Task 0) → `1bfa1a2bcf84cfe756e5a00a62c73dd28948d3a4` (the L3 freeze) → `fbf6485ff6fd02dafa3b64c5fa4382acf15d7d09`
  (Ruling 1) → `ac25ae01d9a06eec1fc6be1e9e1c3c7dcb6558da` (the close) → `08274008…` (the end state); no line after 2096.
- **FACT — the guard state at the start tip**, at `tools/audit/guard_state.json` → `summary`: run 83, passing 70,
  failing 13. The fourth run's end-state portion of `records/cowork/handoff/cowork_away_returns.md` reads *"83 guard(s)
  run, 13 failing, 4 not run, 20 historical record(s)"*, `gen_per_session_reading.py --check` PASS, and
  `gen_guard_classification.py --check` STOPs naming exactly five tools. **Read the object yourself at 0(f).**
- **FACT — the fourth run's results, checked by this side at the objects:** `CLAUDE.md` 170,510 bytes with the two dated
  pointers at its lines 1890–1891 and 1922–1924 and neither former wording in it; `CLAUDE_ARCHIVE.md` carrying both at its
  end; `FROZEN["l3"]` in the boot-pack tool with the ten digests the fourth report §4 tables; `STATUS.md` (12,024 bytes)
  with the fourth dispatch's FOUR entries at its lines 8, 10, 12 and 14 — the close entry carrying `Last updated: `, then
  the Task 2, Task 1 and Task 0 `Same dispatch` entries — and the two 2026-09-02 entries at 16 and 18.
- **FACT — the tool, read whole.** Its report population is every file of `records/cc/reports/` whose name opens
  `REPORT_PREFIX`, ordered by add-commit; it sizes each whole. **No file of that population is an appendix today**: the
  reports folder's listing holds no name opening `cc_report_l3_comparison_tabulation_` and ending `_appendix.md`. The
  folder's appendix files at the listing are four, each beside its report:
  `cc_report_pruning_rulings_execution_2026_11_01_appendix.md`, `…_reexecution_2026_11_01_appendix.md`,
  `…_third_execution_2026_11_01_appendix.md` and `…_fourth_execution_2026_11_02_appendix.md`. **So the arc's own
  appendix count is zero today, and the folder-wide pairing (Task 2(b) edit 5) is what gives Ruling 4's share a value
  now.**
- **FACT — the tool's `generated_for` is stale.** It names *"cc_instruction_per_session_reading_measurement_2026_11_01.md,
  Task 1"*; the remainder batch completed the tool (its own docstring, lines 31–35) and the artifact has been regenerated
  by later batches. The remainder report's §6 item 5 declared it (RELAYED, handoff entry 464 §1). Task 2 sets it to this
  dispatch, the former value named in the report.
- **FACT — the Claude Code side's per-batch composition** in the tool (`cc_members`, lines 694–703) sums the ordinary
  session-start read, which contains the six spans read with the file tool, and adds the whole injected `CLAUDE.md` only
  in `with_it`. Under Ruling 2 the six spans' file-tool read leaves the sum and the injected copy stays: **with_it − six**.
  The eight-line check's own reads are a few hundred characters and are not sized.
- **FACT — the stale comment**, at the staged boot-pack tool, lines 9043–9047 (688,664 bytes at this side's staging
  result): *"Stopping the build for a spent subject would leave this tool checking almost nothing, all three subjects
  being spent."* Five subjects are built (`WITHHELD`: `harmony-boundary`, `scoring-model`, `l0-l1`, `l2`, `l3`) and all
  five are in `FROZEN`. **The fourth dispatch also named the first block of `VERDICTS["l3"]`'s opening comment as stale;
  it is not.** It was corrected on 2026-10-17 by `cc_instruction_l3_brief_landing_2026_10_17.md` Task 1 (the away-returns
  section of that batch), and the staged tool's lines 6695–6708 carry the corrected text with its former wording
  preserved. **Nothing is done to it.**
- **NOT KNOWN TO THIS SIDE — whether any guard pins either tool's own blob, or whether the boot-pack manifest records
  anything of its tool's source text.** Task 1(c) and Task 2(f) catch both by prediction, each with its stop.
- **NOT KNOWN TO THIS SIDE — the running time the invariant share adds** to the tool's `--check` (it reads every arc
  dispatch and report once more; the two populations are 30 files each). Report it.
- **ASSUMPTION A1 — the working tree, stated by CONTENT.** Tracked modifications at your boot: **exactly one**,
  `tools/audit/claude_md_finer_archive.json` — standing, carried and not chased (the fourth report §8, A1 held; the end
  state's `changed_paths.py`). **This side wrote no tracked file.** Untracked and landed by Task 0: this dispatch and
  entry 476 — **two untracked paths** beyond the standing population.
- **ASSUMPTION A2 — the reds, by cause.**
  - **The opening capture** (0(f)) fails exactly the thirteen of the start tip's `guard_state.json` and
    `gen_per_session_reading.py --check` — cause: Task 0's landed entry moves the boot chain's three latest entries.
    **If entry 476 was not landed, `gen_per_session_reading.py --check` stays GREEN** (this dispatch's name is outside
    the arc's prefix) and the thirteen alone are the opening failing set; every later prediction that names its FAIL →
    PASS then reads PASS → PASS. Anything else is reported and is a STOP.
  - **Task 1:** the capture after the comment is corrected is IDENTICAL to the opening capture, and
    `gen_derivation_boot_pack.py --check` prints exactly what it printed at 1(a).
  - **Task 2:** after 2(a)'s regeneration with the tool as it stands, `gen_per_session_reading.py --check` is GREEN;
    after the extension and its regeneration it is GREEN; the capture compared with Task 1's differs in exactly that one
    verdict, FAIL → PASS.
  - **Task 3:** as the fourth dispatch's 3(c), read with this batch's paths (Task 3 below).
- **ASSUMPTION A3** — no `src/` file, build, test, golden, corpus of scores or measurement of the analysis is touched.
- **ASSUMPTION A4 — THE FOOTPRINT.** **Task 1:** in `tools/audit/gen_derivation_boot_pack.py`, the one comment edit of
  Task 1(b) — nothing else in it; **nothing regenerated**. **Task 2:** in `tools/audit/gen_per_session_reading.py`, the
  edits 1 to 9 of Task 2(b) — nothing else; and the artifact, regenerated. **Task 3:** `STATUS.md`, `STATUS_ARCHIVE.md`,
  `tools/audit/gen_status_batch_bound.py`, `tools/audit/status_batch_bound.json`, the artifacts 3(c) regenerates, the
  report and its appendix, `records/cowork/handoff/cowork_away_returns.md`. **Task 4:** `tools/audit/guard_state.json`
  and the away-returns end-state portion.
- **ASSUMPTION A5 — byte-unchanged by this batch:** `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS.md`,
  `DECISIONS_ARCHIVE.md`, every file under `tools/audit/derivation_boot_pack/`, `tools/audit/derivation_boot_pack.json`,
  every ruling record, every handoff entry up to 475, every dispatch and report but this batch's own, and every file under
  `tools/audit/decisions/`.

## The declared start state — at the tree you will meet

Both ref files at the start tip; the one standing modification of A1; this dispatch and entry 476 untracked (entry 476
may be absent — Task 0 says what then); nothing running.

## Findings in this batch

**No finding number is allocated.**

---

## Task 0 — land the records, and PUSH

- **0(a) — the pin.** `git hash-object --no-filters` of this dispatch, in its own call; report the blob and `git
  cat-file -s` after 0(e). Re-hash immediately before staging; equal, or STOP.
- **0(b) — the chain and the before-artifact.** Each hash written literally in its own command: `git cat-file -p
  08274008d07b7e102a692f59eaedb0905860c39f` (expected parent `ac25ae01d9a06eec1fc6be1e9e1c3c7dcb6558da`); `git cat-file
  -p ac25ae01d9a06eec1fc6be1e9e1c3c7dcb6558da` (expected parent `fbf6485ff6fd02dafa3b64c5fa4382acf15d7d09`). Then `git
  cat-file -t d17a84afdbfbf78c16ff4514df63185fad114a5c` (expected `commit`) and `git rev-parse
  d17a84afdbfbf78c16ff4514df63185fad114a5c:tools/audit/per_session_reading.json` — **report the blob; this is the
  before-artifact.** A different chain, or a `bad object` for either query, is a STOP-and-report with nothing committed.
- **0(c) — A1**, by `python tools/audit/changed_paths.py` (the sanctioned enumeration; `git status` is not used, D-253):
  exactly the one standing modification; the two landing paths untracked; other untracked paths only the standing
  population. Anything else is reported and is a STOP.
- **0(d) — last bytes** of the two landing files, at blobs written `--no-filters`: each ends with a newline after a
  complete line and holds no zero byte. **No size is stated for either**; report both.
- **0(e) — the commit.** `python tools/audit/gen_evidence_pin_membership.py --check` first, expected GREEN with nothing
  regenerated (no ruling record is landed). Then exactly these paths and no other, staged by explicit path, the staged set
  proved with `python tools/audit/changed_paths.py --staged`:
  - `records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md` (this dispatch; new)
  - `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_six.md` (new)

  Subject, exactly: `record: entry 476 and the step-4 second dispatch (the per-session reading extension)`. If entry 476
  is NOT at your boot, land this dispatch alone with the subject `record: the step-4 second dispatch (the per-session
  reading extension)`, report the absence, and do not wait for it. Push; read `.git/refs/remotes/origin/master` and
  verify it equals the new tip. **This commit is `<T0>`.**
- **0(f) — the opening capture.** `python tools/audit/gen_guard_state.py --check`, output saved whole to a scratch file
  and read. Read the start tip's `tools/audit/guard_state.json` → `summary` at the object (`git show
  08274008d07b7e102a692f59eaedb0905860c39f:tools/audit/guard_state.json`). Then `python
  tools/audit/gen_guard_classification.py --check`, expected exit 2, a STOP naming five tools — report them by name; a
  number other than five is a STOP-and-report. **The failing set must be A2's.** Anything else is reported and is a STOP.

**E0:** the two records landed, pushed; the opening capture as A2 states it.

---

## Task 1 — CORRECT THE STALE COMMENT IN THE BOOT-PACK TOOL

- **1(a) — before.** `python tools/audit/gen_derivation_boot_pack.py --check`, in its own call, output saved whole.
  Expected exit 0, *"the derivation boot pack re-derives"*, and five lines *"<subject>: FROZEN — <n> file(s) at their
  recorded blobs"*. Anything else is a STOP-and-report with nothing edited.
- **1(b) — the edit**, with the file-editing tool. Replace exactly these two lines inside `build()` (located by the
  first read's item 8):

  ```python
      # subject would leave this tool checking almost nothing, all three subjects being spent.  What
      # changes for a FROZEN subject is what the manifest KEEPS of that build (Ruling 1, 2026-09-20).
  ```

  with exactly these five:

  ```python
      # subject would leave this tool checking almost nothing, every built subject being spent.  What
      # changes for a FROZEN subject is what the manifest KEEPS of that build (Ruling 1, 2026-09-20).
      # ★ CORRECTED <ACT_DATE> by `cc_instruction_per_session_reading_extension_2026_11_02.md` Task 1,
      # under the user's rule of 2026-09-22: five subjects are built and all five are frozen.  FORMER
      # WORDING, PRESERVED (#12): "… almost nothing, all three subjects being spent."
  ```

  *(The fence lines are not in it. `<ACT_DATE>` is the date. The four leading spaces are the indentation of the lines
  replaced; if it differs at the object, follow the object and report it.)* **Nothing else in the tool changes.**
- **1(c) — after, WITHOUT write mode.** `python tools/audit/gen_derivation_boot_pack.py --check`, in its own call:
  **expected output identical to 1(a)'s, byte for byte** (compare the two saved files). `python
  tools/audit/changed_paths.py`: modified are the tool and the standing `claude_md_finer_archive.json`, nothing else.
  Then the full capture, compared verdict by verdict with the opening capture: **expected IDENTICAL.**
- **1(d) — the commit**, exactly `tools/audit/gen_derivation_boot_pack.py`, staged by explicit path, the staged set
  proved. Subject, exactly: `Correct a stale comment in the derivation boot pack tool: all five built subjects are
  frozen`. Push; verify `origin/master` at the ref file. **This commit is `<T1>`.**

**★ THE CASE FOR TASK 1 — 1(c) not as predicted** (the `--check` output differs, or a capture verdict differs). Reverse
the edit with the file-editing tool and prove the tool equal to its `<T0>` blob (`git hash-object` against `git
rev-parse <T0>:tools/audit/gen_derivation_boot_pack.py`); run the `--check` once more and prove its output equal to
1(a)'s. **Do not run write mode.** Report what differed. **Then go on to Task 2** — Task 2 does not depend on Task 1 —
with `<T1>` meaning `<T0>`, and say in the close entry that Task 1 was not committed and why.

**E1:** the comment corrected; the boot-pack check's output unchanged; the capture identical; one commit, pushed.

---

## Task 2 — EXTEND THE MEASUREMENT TOOL, PROVE IT, RE-RUN IT

- **2(a) — the tool as it stands, re-run first.** `python tools/audit/gen_per_session_reading.py` (write mode), in its
  own call, output saved whole; then `--check`, expected GREEN. **Copy the artifact to a scratch file — this is *the
  baseline at this tree*.** Its `the_cowork_boot_chain`'s three latest entries are reported. *(This isolates what the
  extension moves from what Task 0's landing moved.)*
- **2(b) — the edits**, each with the file-editing tool, in this order. Every `old` text is quoted from this side's
  staged copy; **locate each by search before editing**, and if any is not found exactly once, STOP-and-report with the
  tool reversed to its `<T1>` blob.

  **Edit 1 — the import.** After the line `import sys` insert the line `from collections import Counter`.

  **Edit 2 — the constant.** After the line `REPORT_PREFIX = "cc_report_l3_comparison_tabulation_"` insert:

  ```python
  APPENDIX_SUFFIX = "_appendix.md"      # Ruling 4 of the 2026-11-01 record: `<stem>_appendix.md` beside `<stem>.md`
  ```

  **Edit 3 — the populations leave out appendix files.** In `population_rows`, replace

  ```python
          if not name.startswith(prefix):
              continue
  ```

  with

  ```python
          if not name.startswith(prefix) or name.endswith(APPENDIX_SUFFIX):
              continue
  ```

  **Edit 4 — three new functions.** Directly after the function `population_summary` (after its `return { … }` block and
  the two blank lines that follow it, before the comment line opening `# ── table 2: the six spans, partitioned`),
  insert:

  ```python
  # ── the appendix beside a report (Ruling 4 of the 2026-11-01 record) ────────────────────────────
  def pair_appendices(names: list[str]) -> dict[str, str]:
      """Every appendix file among `names`, keyed by the report it stands beside: the report of
      `<stem>_appendix.md` is `<stem>.md`. An appendix with no report beside it is a STOP."""
      present = set(names)
      pairs = {}
      for name in sorted(names):
          if not name.endswith(APPENDIX_SUFFIX):
              continue
          report = name[:-len(APPENDIX_SUFFIX)] + ".md"
          if report not in present:
              raise Stop("an appendix file has no report beside it: %s" % name)
          pairs[report] = name
      return pairs


  # ── the invariant share: what a member shares line for line with its predecessor ───────────────
  def shared_with_predecessor(text: str, previous: str) -> dict:
      """The characters of `text` on lines that also stand in `previous`, matched line for line with
      their line endings, each line of `previous` matched at most once, order ignored.
      Whitespace-only lines are counted apart and are not in the share."""
      available = Counter(previous.splitlines(keepends=True))
      shared = blank = 0
      for line in text.splitlines(keepends=True):
          if available[line] > 0:
              available[line] -= 1
              if line.strip():
                  shared += len(line)
              else:
                  blank += len(line)
      return {
          "characters": len(text),
          "characters_on_lines_shared_with_the_predecessor": shared,
          "characters_on_whitespace_only_lines_shared_and_not_counted_above": blank,
          "share_percent": round(100.0 * shared / len(text), 2) if text else 0.0,
      }


  def invariant_shares(folder: str, rows: list[dict]) -> dict:
      """Each member of a derived population against the member before it in the population's own
      order (add-commit time, then name). The first member has no predecessor."""
      previous_name = previous_text = None
      shared_total = own_total = 0
      for row in rows:
          text = read(folder + "/" + row["name"])
          if previous_text is None:
              row["the_predecessor"] = None
              row["shared_with_the_predecessor"] = None
          else:
              s = shared_with_predecessor(text, previous_text)
              row["the_predecessor"] = previous_name
              row["shared_with_the_predecessor"] = s
              shared_total += s["characters_on_lines_shared_with_the_predecessor"]
              own_total += s["characters"]
          previous_name, previous_text = row["name"], text
      return {
          "members_with_a_predecessor": max(len(rows) - 1, 0),
          "their_characters": own_total,
          "their_characters_on_lines_shared_with_the_predecessor": shared_total,
          "share_percent": round(100.0 * shared_total / own_total, 2) if own_total else 0.0,
          "how_a_line_is_shared": "a line of the member, with its line ending, counts as shared when "
                                  "the predecessor holds the same line not already matched; the order "
                                  "of lines is ignored; whitespace-only lines are counted apart and are "
                                  "not in the share. A line changed by one character counts as not "
                                  "shared, and a short common line counts as shared wherever it stands.",
      }

  ```

  *(The last line of the block is one blank line; together with the existing blank line before the table-2 comment
  there are then two, as between the tool's other functions. Follow the object's spacing and report it.)*

  **Edit 5 — compute them in `build()`.** Directly after the two lines

  ```python
      for r in latest_entries:
          r["characters"] = len(read(HANDOFF_FOLDER + "/" + r["name"]))
  ```

  insert:

  ```python

      dispatch_shares = invariant_shares(DISPATCH_FOLDER, dispatch_rows)
      report_shares = invariant_shares(REPORT_FOLDER, report_rows)
      appendix_pairs = pair_appendices(sorted(os.listdir(os.path.join(ROOT, REPORT_FOLDER))))
      for row in report_rows:
          beside = appendix_pairs.get(row["name"])
          row["the_appendix_beside_it"] = (
              {"name": beside, "characters": len(read(REPORT_FOLDER + "/" + beside))} if beside else None)
      reports_with_an_appendix = []
      for report, beside in sorted(appendix_pairs.items()):
          proper = len(read(REPORT_FOLDER + "/" + report))
          appendix = len(read(REPORT_FOLDER + "/" + beside))
          reports_with_an_appendix.append({
              "the_report": report,
              "characters_of_the_report_proper": proper,
              "the_appendix": beside, "characters_of_the_appendix": appendix,
              "the_appendix_share_of_the_two_percent":
                  round(100.0 * appendix / (proper + appendix), 2) if proper + appendix else 0.0,
          })
  ```

  *(The pairs carry no add-commit and are ordered by the report's name, so a report and appendix written by a batch and
  not yet committed are measured like any other — which Task 3(c)'s last regeneration relies on.)*

  **Edit 6 — publish them beside the two arc populations.** Replace the line

  ```python
      the_dispatches.update(population_summary(dispatch_rows, 5, "the_last_five"))
  ```

  with

  ```python
      the_dispatches.update(population_summary(dispatch_rows, 5, "the_last_five"))
      the_dispatches["the_invariant_share"] = dispatch_shares
  ```

  and replace the line

  ```python
      the_reports.update(population_summary(report_rows, 3, "the_last_three"))
  ```

  with

  ```python
      the_reports.update(population_summary(report_rows, 3, "the_last_three"))
      the_reports["the_invariant_share"] = report_shares
      the_reports["the_appendices_beside_them"] = {
          "count": sum(1 for r in report_rows if r["the_appendix_beside_it"]),
          "characters_total": sum(r["the_appendix_beside_it"]["characters"]
                                  for r in report_rows if r["the_appendix_beside_it"]),
          "how_these_relate_to_the_sizes_above": "every size above is of the report proper only; an "
                                                 "appendix file is sized here and in "
                                                 "`the_reports_with_an_appendix_beside_them`, never "
                                                 "added to the report's own size",
      }
  ```

  **Edit 7 — Ruling 2's after-figure.** In `totals_by_side`, directly after the line

  ```python
              "the_injected_copy_added_in_with_it": "CLAUDE.md, the whole file, %d characters" % whole,
  ```

  insert:

  ```python
              "under_ruling_2_of_2026_11_01": cc_without + whole - six,
              "how_ruling_2_moves_it": "Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_"
                                       "pruning_iteration_sitting.md`: the injected copy is the read of "
                                       "the six spans, so their file-tool read (%d characters) leaves the "
                                       "sum and the injected copy stays; the eight-line check's own reads "
                                       "are not sized here" % six,
  ```

  **Edit 8 — the artifact's new member, its `generated_for` and its bounds.** (i) Replace

  ```python
          "generated_for": "cc_instruction_per_session_reading_measurement_2026_11_01.md, Task 1 — "
                           "step 1 of the pruning iteration the user ordered on 2026-10-31",
  ```

  with

  ```python
          "generated_for": "cc_instruction_per_session_reading_extension_2026_11_02.md, Task 2 — step 4's "
                           "second dispatch of the pruning iteration the user ordered on 2026-10-31; "
                           "first built for step 1 (cc_instruction_per_session_reading_measurement_"
                           "2026_11_01.md, Task 1)",
  ```

  (ii) Directly after the line `            "the_arc_reports": the_reports,` insert:

  ```python
              "the_reports_with_an_appendix_beside_them": {
                  "the_folder": REPORT_FOLDER,
                  "how_a_pair_is_found": "every file of the folder whose name ends `%s`, beside the report "
                                         "named by its stem; an appendix with no report beside it is a "
                                         "STOP" % APPENDIX_SUFFIX,
                  "read_by": "Cowork: the report proper in full under the user's rule of 2026-09-03, the "
                             "appendix at need (Ruling 4 of the 2026-11-01 record)",
                  "count": len(reports_with_an_appendix),
                  "characters_of_the_reports_proper": sum(r["characters_of_the_report_proper"]
                                                          for r in reports_with_an_appendix),
                  "characters_of_the_appendices": sum(r["characters_of_the_appendix"]
                                                      for r in reports_with_an_appendix),
                  "the_pairs": reports_with_an_appendix,
              },
  ```

  (iii) In `the_bounds_this_artifact_declares_on_itself`, after the line
  `            "The dispatch and report populations are complete only relative to their name prefixes.",`
  insert:

  ```python
              "The invariant share is a LINE measure, not a judgement of copying: a line changed by one "
              "character counts as not shared, and a short common line counts as shared wherever it "
              "stands. It compares each member with its predecessor only.",
              "An appendix file is found by its name alone (`<stem>_appendix.md` beside `<stem>.md`).",
  ```

  (iv) In `what_this_does_not_assert`, after the line
  `            "That the dispatch and report populations are complete beyond the name prefixes.",` insert:

  ```python
              "That a line shared with the predecessor was copied from it, or that a line not shared "
              "was newly written.",
  ```

  **Edit 9 — the docstring and the printout.** (i) In the docstring, directly before the line `WHY IT EXISTS.  The
  user's instruction of 2026-10-31, in his words:` insert this paragraph followed by one blank line:

  ```text
  AND, SINCE 2026-11-02, THREE ADDITIONS (`cc_instruction_per_session_reading_extension_2026_11_02.md`,
  Task 2 — step 4's second dispatch).  (1) THE INVARIANT SHARE: for each dispatch and each report of the
  arc, the characters on lines it shares with its predecessor (the member before it in the population's
  own order), matched line for line with line endings, order ignored, whitespace-only lines apart — the
  figure the dispatch-form question waits for (handoff entry 464 §1).  (2) THE APPENDIX FILE BESIDE A
  REPORT: under Ruling 4 of the 2026-11-01 record a report's raw printouts stand in `<stem>_appendix.md`
  beside it; appendix files leave the populations, are sized beside their reports, and every report of
  the folder with one is listed with both sizes.  (3) RULING 2's AFTER-FIGURE: the Claude Code side's
  per-batch total with the six spans' file-tool read replaced by the injected copy.
  ```

  (ii) In the docstring's list *THE STOPS*, after the line `  * a dispatch, a report or a handoff entry of a derived
  population with no add-commit;` insert:

  ```text
    * an appendix file of the reports folder with no report beside it;
  ```

  (iii) In `main`, directly after the one line that ends `t1["the_arc_reports"]["characters_total"]))` (the last line of
  the `print` call opening `print("  arc dispatches %d, %d characters; arc reports %d, %d characters"`), insert, at the
  indentation of that `print` call:

  ```python
      print("  invariant share: dispatches %.2f %%, reports %.2f %%"
            % (t1["the_arc_dispatches"]["the_invariant_share"]["share_percent"],
               t1["the_arc_reports"]["the_invariant_share"]["share_percent"]))
      ap = t1["the_reports_with_an_appendix_beside_them"]
      print("  reports with an appendix beside them %d: reports proper %d, appendices %d characters"
            % (ap["count"], ap["characters_of_the_reports_proper"], ap["characters_of_the_appendices"]))
  ```

  **Nothing else in the tool changes.** Report the tool's new size and line count.

- **2(c) — the planted-fault proofs**, by ONE scratch script outside the repository, quoted whole in the appendix, which
  puts `tools/audit` on its path, imports the tool as a module, and calls its functions on literal inputs. **Each proof
  prints PASS or FAIL with the values; all must PASS.**
  - **P1 — a hand-counted case.** `shared_with_predecessor("a\nb\nb\n\nc", "b\nx\na\n\n")` returns `characters` 8,
    shared 4, whitespace-only 1, `share_percent` 50.0. *(By hand: `a\n` matches, the first `b\n` matches, the second
    does not, the blank line matches and is counted apart, `c` does not.)*
  - **P2 — identity.** `shared_with_predecessor("x\ny\n", "x\ny\n")` returns shared 4, `share_percent` 100.0.
  - **P3 — nothing before.** `shared_with_predecessor("x\ny\n", "")` returns shared 0, `share_percent` 0.0; and
    `shared_with_predecessor("", "x\n")` returns `characters` 0, `share_percent` 0.0.
  - **P4 — a planted one-character change.** `shared_with_predecessor("abc\ndef\n", "abc\ndeF\n")` returns shared 4,
    `share_percent` 50.0 — the changed line is not shared.
  - **P5 — the planted orphan.** `pair_appendices(["r_x.md", "r_x_appendix.md", "r_y_appendix.md"])` raises the tool's
    `Stop` and its message names `r_y_appendix.md`.
  - **P6 — the pairing.** `pair_appendices(["r_x.md", "r_x_appendix.md", "r_z.md"])` returns exactly
    `{"r_x.md": "r_x_appendix.md"}`.
  - **P7 — the populations at the tree.** After 2(d), from the artifact: no name in `the_arc_reports` →
    `the_population` or `the_arc_dispatches` → `the_population` ends with `_appendix.md`; the first member of each has
    `the_predecessor` null and every other member's `the_predecessor` is the name of the member before it.
  - **P8 — the folder-wide pairs at the tree.** After 2(d): `the_reports_with_an_appendix_beside_them` → `count` is 4 or
    more, and its `the_pairs` names each of the four appendix files this side's premise ledger lists, each beside its
    report. **A count above 4 is reported, not a failure** (an appendix may have been added since).

  **Any FAIL is the ★ case for Task 2.**
- **2(d) — the regeneration.** `python tools/audit/gen_per_session_reading.py` (write mode), in its own call, output
  saved whole (the new printout lines included); then `--check`, GREEN. Report the `--check` run's wall time (the
  first NOT KNOWN item).
- **2(e) — THE COMPARISON WITH THE BASELINE AT THIS TREE**, by a scratch script quoted whole in the appendix: load the
  baseline of 2(a) and the regenerated artifact as JSON, walk both, and print every path whose value differs, was added
  or was removed, each classed against this prediction. **The prediction, in full:**
  - **Changed:** exactly one value, `generated_for` (report its former and new value).
  - **Added:** `the_invariant_share` under `the_arc_dispatches` and under `the_arc_reports`; `the_appendices_beside_them`
    under `the_arc_reports`; `the_reports_with_an_appendix_beside_them` under `table_1_the_per_session_reading`;
    `under_ruling_2_of_2026_11_01` and `how_ruling_2_moves_it` under the Claude Code side's entry of `totals_by_side`;
    in every member record of `the_arc_dispatches` and `the_arc_reports` (in `the_population` and in `the_last_five` /
    `the_last_three`), `the_predecessor` and `shared_with_the_predecessor`, and in every member record of
    `the_arc_reports`, `the_appendix_beside_it`; and the three bound sentences and one non-assertion sentence of edit 8
    (iii) and (iv), as list elements added at the positions given.
  - **Removed:** nothing. **Unmoved:** every other value — every size, count, total, population member, table-2 value.

  **Then two arithmetic checks, printed with their values:** `under_ruling_2_of_2026_11_01` equals `with_it` minus
  `the_reading_of_claude_md` → `characters`; and `the_reports_with_an_appendix_beside_them` → `characters_of_the_appendices`
  equals the sum of its pairs' `characters_of_the_appendix`. **Any other difference, or a failed check, is the ★ case for
  Task 2.** *(A list element inserted moves the index of the elements after it; the script compares the two lists of
  edit 8 (iii) and (iv) as lists of strings, and reports an insertion as added, not as every later element changed.)*
- **2(f) — the checks.** The full capture, compared verdict by verdict with Task 1's capture (or with the opening one
  where Task 1 went to its ★ case): **exactly one verdict differs, `gen_per_session_reading.py --check` FAIL → PASS.**
  Anything else is the ★ case for Task 2.
- **2(g) — the commit**, exactly `tools/audit/gen_per_session_reading.py` and `tools/audit/per_session_reading.json`,
  staged by explicit path, the staged set proved. Subject, exactly: `Extend the per-session reading measurement: the
  invariant share, the appendix beside a report, Ruling 2's after-figure`. Push; verify `origin/master` at the ref file.
  **This commit is `<T2>`.**

**★ THE CASE FOR TASK 2 — anything other than predicted at 2(b) to 2(f).** Reverse the tool with the file-editing tool
and prove it equal to its `<T1>` blob; run write mode once and prove the artifact equal to the baseline of 2(a); report
what differed, with the printouts. **Do not commit the extension.** The artifact as 2(a) left it is then committed alone
(the boot chain's movement from Task 0, nothing else), with the subject `The per-session reading measurement re-run at
the tree Task 0 left`, and Task 3 says the extension was not committed and why.

**E2:** the tool extended by edits 1 to 9 and nothing else; P1 to P8 PASS; the comparison exactly as predicted; the
capture differing in the one predicted verdict; one commit, pushed.

---

## Task 3 — the close: EXECUTE THE FOURTH DISPATCH'S TASK 3 (its lines 427 to 486), with these overrides

The fourth dispatch's Task 3 executes the third dispatch's Task 3 (its lines 380 to 421) with the fourth's overrides.
Read both under these overrides, which govern where they differ:

- **3(a) — `STATUS.md`.** The close entry names THIS dispatch by its file name and carries the `Last updated: ` prefix,
  **moved off the fourth dispatch's close entry (now at `STATUS.md`'s line 8)**, the move complete before 3(b) runs,
  exactly one line carrying it afterwards. Below it, one `Same dispatch` entry per COMMITTED task, newest first. **It
  says in plain words:** that this batch is step 4's second dispatch of the pruning iteration; that it extended the
  per-session reading measurement with three additions — what each arc dispatch and report shares line for line with
  the one before it, the size of the appendix file beside a report, and the Claude Code side's per-batch total under
  Ruling 2 — and re-ran it, the before and after values standing side by side in the report; that it corrected one
  stale comment in the boot-pack tool; **one measurement tool extended and one comment of another tool corrected; no
  other tool edited or added**; no algorithm change; no decisions-register entry, no `D-NNN`, no open-items row; and
  that the whole is the report (a POINTER, D-431, no figure restated). Where a task was not committed, it says which
  and why.
- **3(b) — the forward bound.** Read `tools/audit/gen_status_batch_bound.py` at the object
  `08274008d07b7e102a692f59eaedb0905860c39f:tools/audit/gen_status_batch_bound.py` first; **report its authored
  constants as you find them** (RELAYED, the fourth report §6 3(b): `BASE_COMMIT` `fbf6485f…`,
  `PREVIOUS_BATCH_DISPATCH` the third dispatch, `DISPATCH` the fourth dispatch, `TASK` `Task 3`, `MOVE_KIND`
  `ordinary`, `ACT_DATE` 2026-11-02; a difference is reported and 3(b) proceeds from what the object holds). Re-aim:
  `BASE_COMMIT` this batch's LAST TASK COMMIT before the close (**check that the `STATUS.md` blob at `BASE_COMMIT`
  equals its blob at the start tip, each `git rev-parse` in its own command**); `PREVIOUS_BATCH_DISPATCH`
  `cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md`; `ACT_DATE` the day the move runs; `DISPATCH`
  `cc_instruction_per_session_reading_extension_2026_11_02.md`; `TASK` `Task 3`; `MOVE_KIND` stays `ordinary`; append
  this batch's aiming to `PREVIOUS_AIMINGS` (do not append the fourth dispatch's aiming twice); amend the head comments
  as the previous batches did, the former values named (#12). **Then `--apply` and `--check`, each in its own call.
  Prediction: exactly the fourth dispatch's FOUR entries move** — its close entry and its Task 2, Task 1 and Task 0
  `Same dispatch` entries (base lines 8, 10, 12 and 14); the two 2026-09-02 entries stay; no STOP. The cited STOP
  handling, *no correction line* rule and four archive checks bind.
- **3(c) — the regenerations**, as the fourth dispatch's 3(c), with: **`CLAUDE.md` is not edited by this batch, so class
  (c) does NOT apply** and the confinement check's allowed paths are `STATUS.md` and `STATUS_ARCHIVE.md` alone, base the
  start tip. Expected, by the fourth run's 3(c): `gen_session_start_read_size.py --check` and `gen_defense_share.py
  --check` RED (the `STATUS.md` member), regenerated; L0/L1 GREEN, not regenerated; L3 RED or GREEN — if RED, it may move
  only line values inside its `STATUS.md` residue record; the boot-pack manifest NOT regenerated, its `--check` green.
  **Then LAST `python tools/audit/gen_per_session_reading.py`** (write mode), `--check` green. **Each moved artifact is
  diffed against its start-tip blob — the artifact of this tool against its `<T2>` blob — and every changed passage
  accounted for**: in the artifact, only the ordinary read's `STATUS.md` member and the totals that include it, their
  mirrors in `totals_by_side` (`under_ruling_2_of_2026_11_01` among them), and the imported defense-share denominator of
  the whole ordinary read (`the_two_denominators` → `the_whole_ordinary_session_start_read`).
- **3(c′) — THE LAST REGENERATION, after 3(d) has written the report and its appendix in their final form and before
  3(e).** The tool sizes every report of the folder with an appendix beside it, so this batch's own report and appendix
  join `the_reports_with_an_appendix_beside_them` the moment both exist. Run `python
  tools/audit/gen_per_session_reading.py` (write mode) once more, then `--check` GREEN, and diff the artifact against
  the one 3(c) left: **expected, only that block: `count` one higher, the two sums higher by this batch's two sizes, and
  one added pair naming `cc_report_per_session_reading_extension_2026_11_02.md`.** Anything else is reported and is a
  STOP before 3(f). **After this run, neither the report nor its appendix is edited again**; the run's output and its
  diff go in the away-returns section of 3(e), not in the report (editing the report would change the size just
  measured).
- **3(d) — the report, in Ruling 4's two-file form**, at **`records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md`**
  and its appendix **`records/cc/reports/cc_report_per_session_reading_extension_2026_11_02_appendix.md`**: the report
  proper carries the first read and the eight-line check, the capacity judgment, every task's account, every check's
  verdict, the grades, the departures and observations; the appendix carries every raw printout verbatim, each under a
  heading naming its command and step. **Add to the report proper:**
  - the tool's 2(b) edits as made (the diff of the tool against its `<T1>` blob, whole — it is short);
  - P1 to P8 with their values; 2(e)'s classed summary and its two arithmetic checks (its per-path records in the
    appendix);
  - **THE BEFORE AND AFTER TABLE**, by a scratch script quoted whole in the appendix that reads the before-artifact
    (`git show d17a84afdbfbf78c16ff4514df63185fad114a5c:tools/audit/per_session_reading.json`) and the after-artifact
    (the working-tree file after 3(c)) and prints, for each of these values, before, after and the difference — each
    printed from the two objects, none typed:
    1. `table_1_the_per_session_reading` → `the_ordinary_session_start_read_imported` → `total_characters`, and its
       `characters_per_member` whole, before and after;
    2. the same → `the_reading_of_claude_md` → `characters`;
    3. each member of `the_further_members` → `characters`, by its `member` text;
    4. `the_arc_dispatches` and `the_arc_reports` → `count`, `characters_total`, `characters_mean`, `characters_max`;
    5. each member of `the_cowork_boot_chain` → `characters`, by its `member` text;
    6. `totals_by_side` → the Claude Code side's `without_the_injected_copy_of_CLAUDE_md` and `with_it`, and the Cowork
       side's `characters`;
    7. `table_2_the_six_spans_partitioned` → `totals` → `characters_of_the_six_spans`, `sub_block_count`,
       `archive_class_characters`, `doubt_defaulted_characters`;

    then, **after only** (they did not exist before): `under_ruling_2_of_2026_11_01`; both `the_invariant_share` blocks
    whole; `the_appendices_beside_them`; and `the_reports_with_an_appendix_beside_them` without its `the_pairs`, then
    each pair's report, its two sizes and the share — **as 3(c) left it, so without this batch's own pair, which 3(c′)
    adds; the report proper says so in one sentence.** **And a second table, per member, after only:** for each arc
    dispatch and each arc report, its name, its characters, its predecessor and its `share_percent`.
  - **One sentence per figure is not wanted.** The tables stand alone; the report proper says in plain words which rulings
    each moved value belongs to, where the record says so (Ruling 1: `CLAUDE.md`; Ruling 3: `DECISIONS.md`; Ruling 2: the
    new total), and asserts nothing else about them.
- **3(e)** — the section appended to `records/cowork/handoff/cowork_away_returns.md` is headed **THE PRUNING ITERATION,
  STEP 4's SECOND DISPATCH — THE PER-SESSION READING MEASUREMENT EXTENDED AND RE-RUN, BEFORE AND AFTER SIDE BY SIDE;
  ONE STALE TOOL COMMENT CORRECTED; MEASUREMENT AND DOCUMENTATION ONLY, NO ALGORITHM CHANGED** (where a task was not
  committed, the heading says which and why). **The plan line:** *"The next act is the writing side's — the check of
  this batch's return at the objects; then, one per turn, the user's yes-or-no on carrying the Cowork boot chain's
  operating paragraphs in the current handoff entry (candidate (e)) and the dispatch-form surface (candidate (d)), which
  the invariant share now sizes; and only then step 5, the method ruling's surface over the completed L3 tabulation
  (Ruling 4 of the comparison-design sitting)."* If the extension was not committed, the plan line says the invariant
  share is still unmeasured and why.
- **3(f) — the close commit**, as the fourth dispatch's 3(f), the report and appendix at this batch's names. Subject:
  `Close: the pruning iteration step 4 second dispatch - the per-session reading measurement extended and re-run, under
  its dispatch`. Push; verify `origin/master` at the ref file.

**E3:** as the fourth dispatch's E3.

---

## Task 4 — the end state: EXECUTE THE FOURTH DISPATCH'S TASK 4 (its lines 490 to 498), with these overrides

- **The verification at the objects** takes `git diff --name-status 08274008d07b7e102a692f59eaedb0905860c39f <the close
  commit>`, every path accounted for against A4 and the Task 0 files, every file A5 names absent.
- **The condition:** a fresh full guard run in write mode; run count 83, zero STOPs; the failing set exactly the
  thirteen, none added; `gen_per_session_reading.py --check` and `gen_derivation_boot_pack.py --check` PASS; against the
  opening capture exactly one verdict differs, `gen_per_session_reading.py --check` FAIL → PASS;
  `gen_guard_classification.py --check` STOPs naming the same five tools as at 0(f).
- **The commit subject:** `End state: the pruning iteration step 4 second dispatch - guard run at the close tree`. Push;
  verify `origin/master` at the ref file.

**E4:** the condition held at a fresh run committed only after the run that produced it.

**THIS BATCH ENDS HERE.**

---

## What this batch does NOT do

- **No algorithm change; no specification of the analysis touched; no measurement of the analysis.** The decided method
  for L3 is unchanged.
- **No text moves out of any governing document.** `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS.md` and
  `DECISIONS_ARCHIVE.md` are not edited.
- **No tool edited or added beyond A4:** the measurement tool's edits 1 to 9, the boot-pack tool's one comment, the
  forward-bound tool's re-aiming. No guard enrolment changes; no classification verdict is authored.
- **No derivation boot pack file and no manifest regenerated or edited.** `VERDICTS["l3"]`'s comment is not touched (the
  premise ledger says why).
- **No decisions-register entry, no `D-NNN`, no open-items row; no earlier report corrected** (D-674).
- **No figure is interpreted.** The report states what was measured; whether any figure is large or small is the user's
  question on the next surfaces.

## What this batch deliberately leaves to later acts, named so it is not lost

- **Candidate (e)** — the user's yes-or-no on carrying the Cowork boot chain's operating paragraphs in the current
  handoff entry — and **candidate (d)**, the dispatch-form surface the invariant share sizes: the writing side's, one per
  turn, after this batch's return is verified.
- **The fourth report's observation (a)** — `per_session_reading.json`'s table 2 still classes the decision-surface block
  as carrying a former wording, its classifier now matching the marker in the new pointer. Recorded; not acted on here.
- **Carried, unchanged:** the five ★ questions the derivation marks for the user; the classification tool's five
  unauthored verdicts; the decisions register's drifted home anchors; step 5.

---

## The writing side's self-check over this dispatch (recorded, per the standing clause; D-434)

*Written by the writing side after the draft, before its check at its sources; the check runs in a turn of its own and
is recorded in the next section.*

- **Read at the objects this sitting**, through staged copies and the file tools: the ref files and `.git/logs/HEAD` at
  lines 2092 to 2096; the fourth report whole; the fourth dispatch whole; the record whole; entries 475, 474, 464 and 291
  whole; the tool whole; `CLAUDE.md` at 1880–1929 and by search; `CLAUDE_ARCHIVE.md` at 145–173; `STATUS.md` at 1–26;
  the boot-pack tool at 455–544, 6680–6734, 9042–9050 and by search; `guard_state.json` at its `summary` and by search
  for tool paths; `cowork_away_returns.md` at 24708–24715, 24766–24773 and 30266–30363; the first pruning dispatch at
  995–1024 and by search; the reports folder's listing; the instructions folder's listing by search.
- **Not read:** the third dispatch (a git object) — every line range given for it is the fourth dispatch's; the second
  dispatch; the step-1 measurement dispatches; `DECISIONS.md`; `CLAUDE.md` beyond the lines named; `cowork_audit_protocol.md`;
  `gen_guard_state.py`; `gen_status_batch_bound.py`; `changed_paths.py`; any git object.
- **Self-sufficiency (D-251):** every new act (the comment, the nine edits, the proofs, the comparison, the before and
  after table) has its exact text or command and a prediction with a stop; the close and end state are cited at a fixed
  git object the executing side reads itself.
- **No new mechanism beyond the measurement Ruling 4 and entry 464 name:** three additions to an existing measurement
  tool; no tool's verdict or behaviour elsewhere changes.

## This file's check at its sources (D-434; runs in a turn of its own)

*Run 2026-11-02 by the writing side, in the turn after the draft landed, over the draft as landed (58,274 bytes at its
staging result, after a second commit: the first landing was stale, the bridge fault).*

**Checked at the objects and found to hold:**

- Every `old` text of Task 2(b), at the staged tool, each found exactly once: `import sys` (line 126);
  `REPORT_PREFIX` (193); the `if not name.startswith(prefix):` test (348); `population_summary` (362) and the two blank
  lines before the table-2 comment (375); the `for r in latest_entries:` loop (627); the two `population_summary`
  calls (641, 650); `"the_injected_copy_added_in_with_it"` (717); `"generated_for"` and its second line (748–749);
  `"the_arc_reports": the_reports,` (774); the bound (809) and the non-assertion (819); `WHY IT EXISTS.` (26); the STOP
  line on add-commits (104). The indentation of each quoted line, against the object, but one (correction 1).
- Every name the new code uses is defined before it in `build()`: `reports`, `report_rows`, `dispatch_rows`, `six`,
  `whole`, `cc_without`; `os` and `read` at module level.
- The boot-pack comment's two lines and their indentation (9046–9047); `VERDICTS["l3"]`'s corrected comment (6695–6708)
  and its correction's record (`cowork_away_returns.md` 24766–24773).
- The quotations of the record (Ruling 2's bound, lines 164–166; Ruling 4, 302–304) and of entry 464 (§1 lines 70–74,
  §2 item (iv) lines 94–97), word for word.
- `STATUS.md` lines 8 to 18; `CLAUDE.md`'s pointer lines; the chain at `.git/logs/HEAD`; the four appendix files at the
  reports folder's listing; the fourth dispatch's Task 3 (427–486) and Task 4 (490–498) line ranges; the fourth report's
  §6 3(b) constants.
- Each prediction of A2, 2(e), 3(c), 3(c′) and Task 4 against the tool's code: Task 0's entry is the only landed file the
  tool measures; the extension adds keys and changes `generated_for` and nothing else; `STATUS.md` reaches the artifact
  only through the imported ordinary read and the defense-share denominator; this batch's own report and appendix reach
  it only through the folder-wide pairs.

**Corrected, every former wording preserved here (#12):**

1. *Edit 9 (iii), the anchor in `main`.* Former wording: "In `main`, directly after the two lines" followed by a code
   block quoting one line, `t1["the_arc_reports"]["count"], t1["the_arc_reports"]["characters_total"]))`, at eleven
   spaces once the block's own indentation is removed. The object has the line at thirteen spaces, and it is one line,
   not two. The anchor is now the line's ending and the `print` call it closes.
2. *What this batch is.* Former wording: "All four are now carried out: Ruling 3 by the third execution dispatch,
   Rulings 1, 2 and 4 by the fourth". Too wide: Rulings 2 and 4 are rules of form that bind every dispatch, not acts
   one batch completes, and Ruling 3's commit is relayed, not read. Now stated per ruling, with its source.
3. *The first read, item 7.* Former wording: "(51,784 bytes, 868 lines at this side's staging result)". The line count
   was the file tool's numbering, not established as the file's count. The count is dropped.
4. *A2, the opening capture.* The draft did not say what happens if entry 476 is absent. Then nothing the tool measures
   moves at Task 0, and `gen_per_session_reading.py --check` stays green. Without this clause a correct run would have
   met an unpredicted green and stopped. **This is the one correction of content.** Added, no former wording.
5. *0(f) and Task 4, the classification STOP.* Former wordings: "a STOP naming exactly the five tools the fourth report
   §3 0(f) names" and "STOPs naming exactly the five tools". The fourth report names no tool there; it says "the five
   relayed tools". Now: report them by name at 0(f), a number other than five a STOP-and-report, and the same five at
   Task 4.

**Swept for absolutes** (only, never, nowhere, every, all, none, nothing, exactly, whole, complete, identical,
independent). Each hit was read at its line:

- *Exactly* and *identical* are predictions, each with its stop.
- *Every* in Task 2(b) and 2(e) ranges over the members the code iterates, which the code bounds.
- *NOTHING changes* (algorithm) and *no other tool* are bounded by A4.
- *No file of that population is an appendix today* is bounded by the listing it cites.
- *Nothing is done to it* (`VERDICTS["l3"]`) is an order, not a claim.

**Risks named, not removed (#13):**

- The running time the invariant share adds to the guard run is not known; 2(d) reports it.
- Whether a guard pins either tool's blob is not known; Task 1(c) and 2(f) catch it, each with its ★ case.
- The 3(c′) ordering — report final, then the last regeneration — is new to this dispatch form. If Claude Code edits the
  report after that run, the end state's `--check` turns red; 3(c′) forbids it and Task 4 would show it.
