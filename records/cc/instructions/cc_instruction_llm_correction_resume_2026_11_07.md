# CC dispatch — THE LANGUAGE-MODEL CORRECTION, RESUMED: THE REGISTER'S DATA FILE RETURNED TO ITS STANDARD FORM, THEN RULING 1 ITEMS 3 TO 6 OF THE 2026-11-07 CORRECTION RECORD APPLIED — DOCUMENTATION AND RECORD-KEEPING ONLY; NO ALGORITHM CHANGE (2026-11-07)

> **STATUS: RELEASED 2026-11-08** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_nine.md`, after its check at its sources (C1 to
> C5, recorded at the end of this file). **It may now be handed to Claude Code.** *(Former wording of this banner's first
> sentence, kept (#12): "**STATUS: WRITTEN 2026-11-07 — NOT YET RELEASED** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_seven.md`." The rest of the banner below is the
> wording written then.)*
>
> Its check at its sources runs in a turn
> of its own; this banner is set to RELEASED only after that check, which is recorded at the end of this file with every
> former wording. **Until then this dispatch is NOT handed to Claude Code.** Once released it is executed by Claude Code
> when the user hands it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear,
> stop at that step and report it. Do not continue to the next one.**
>
> **THE WRITING SIDE'S RESTRAINT, declared.** Once released this dispatch is final. The writing side will not touch it,
> nor any file it names, while this batch runs. The files the writing side writes after this dispatch lands and before
> hand-over are handoff entries numbered above 577, which is why Task 0 states no size for them. **Nothing this dispatch
> lands is in git yet**; Task 0 lands it.

## What this batch is, in plain words

On 2026-11-07 the user ruled that a language model is used only while the software is being developed, never at run time
in the finished product (`records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`, Ruling 1), and
ratified the corrections that follow as derivations (`records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`,
Ruling 1, items 1 to 7; item 7 is "no act now").

**The batch that applied them stopped.** It ran under `records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md`
(called ***the stopped dispatch*** below — **you do not read it**; everything you need from it is stated here). It
committed and pushed two commits: `566d37e583da3ee23d2d46957ead8eb202290973` (it landed handoff entries 570 to 575 and the
stopped dispatch) and `4461d865fcb2c99ef20099487c0d4a4221456112` (items 1 and 2: seven register entries made
SUPERSEDED BY the 2026-11-07 ruling, two given a provenance note, the register regenerated). Then it stopped, because its
edit of the register's data file had put each superseded entry's new `superseded_by` key on the same line as its
`status` key — so that no line was added — and two tools that guard that file refuse to run unless the file is exactly
what Python's standard JSON writer produces from it. Its report and appendix were written and not committed.

**This batch finishes the work:**

- **Task 0** lands handoff entries 576 and 577 (and any later one), the stopped batch's report and appendix, and this
  dispatch, and pushes.
- **Task 1** returns the data file to its standard form (the seven joined lines each split in two; nothing else moves),
  then regenerates the three artifacts that went red at the stopped batch's last capture.
- **Task 2** (items 3 and 4): a superseded banner over `ARCHITECTURE.md` §19 and over `docs/llm_integration.md`; a note
  in the 2026-08-08 route record.
- **Task 3** (items 5 and 6): annotations in the three reading files.
- **Task 4** is the close; **Task 5** the end state.

**★ ONE RULE FOR EVERY TEXT EDIT OF TASKS 2 AND 3: NO LINE IS ADDED OR REMOVED.** Every banner, note and annotation
either takes the place of one named blank line or is inserted inside one named line, so no line number cited in the files
those tasks edit moves. Each such edit is proved by `--numstat` showing the same number of lines added as removed, and by
the file's line count being unchanged. **The data file is the one exception, and it is this batch's Task 1:** its
re-serialization adds seven lines. *(★ AMENDED 2026-11-07 for the data file only, by the writing side, whose own bar it
was. The stopped dispatch's wording, kept (#12): "★ ONE RULE FOR EVERY TEXT EDIT OF TASKS 1 TO 3: NO LINE IS ADDED OR
REMOVED. … So no line number cited in the files those tasks edit moves." Why the amendment needs no user decision: the
rule's stated purpose was that no cited line number moves; the writing side searched for citations of the data file by
line number in the tools of `tools/audit/decisions` that read it, in `tools/audit/gen_rulings_sort.py`, in the
register's generator, in the twenty `decisions/group_*.md` files and in `DECISIONS.md`, and found none — handoff entry
577 §2. Places outside that set were not searched.)*

**Documentation and algorithm, separated.** **Documentation only:** everything this batch edits, apart from 4(b)'s
re-aiming of the forward-bound tool, which changes that record-keeping tool's constants and no specification. **Algorithm:
NOTHING changes.** No specification of the analysis is changed in substance; the re-serialization changes the data file's
layout and not one value in it; the edited design texts describe a language-model product tool, which is not the
analysis. The method that stands is the one the scope document
(`ratification_surfaces/cowork_llm_correction_scope_2026_11_07.md`) §5 states. **This batch decides nothing.**

---

## ★ THE ORDERED FIRST READ

**★ YOUR FIRST TOOL CALL IS ONE READ OF THIS FILE, AND NOTHING ELSE IN THAT CALL.** Do not read `STATUS.md`,
`DECISIONS.md`, `CLAUDE.md` or anything else in that call, and do not issue any other read in parallel with it. If the
read returns a partial view at the tool's page limit, read this file whole in further ranges of the same file before
anything else, and declare it.

**Then the eight-line check of Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`**:
read at the tree with the file tools, each located by search, **the first line of `CLAUDE.md`, the heading line of each of
its six session-start spans, and its last line carrying text**, and compare each with the copy injected into your
context. **If every line is identical, the six-span read is not performed. If a line differs or is missing, read the six
spans with the file tools and report it as a finding.** Report the eight lines as read and as injected, with their line
numbers.

Then, in this order:

1. `STATUS.md` whole; `DECISIONS.md` whole; `BUILD_AND_TEST.md` whole; `gating_ids` at
   `tools/audit/nongating_apparatus_rows.json`.
2. `cowork_audit_protocol.md` from the line `## The dispatch protocol these audits are commissioned and run under` to the
   end of the file, whole. **Its marked standing clauses bind this batch and are not restated here** (Ruling 2 of
   `records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md`).
3. **The highest-numbered handoff entry on disk, whole** (577, or a higher one if it exists); it is the current handover
   block.
4. `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md` whole (5,001 bytes) — the ruling this
   batch applies.
5. `tools/audit/gen_l3_outgoing_population.py` at its `L3_KEYWORDS` list, located by search (for 4(a)'s search).

**Not read, and not needed:** the stopped dispatch; any earlier dispatch or report, the stopped batch's report and
appendix included (Task 0 lands them; this dispatch states what it takes from them); the scope document; the reading
files beyond the lines Task 3 names; `FRAMEWORK.md`. Declare any further read you make.

---

## ★ WORDS USED IN THIS DISPATCH, EXPLAINED FIRST

- ***The start tip*** — `4461d865fcb2c99ef20099487c0d4a4221456112`, the commit both ref files named when this dispatch was
  written: the stopped batch's register commit.
- ***The stopped batch*** — the batch run under the stopped dispatch. Its two commits are named above. Its report:
  `records/cc/reports/cc_report_llm_correction_2026_11_07.md`; its appendix: `…_appendix.md` beside it.
- ***The records landing*** — the batch before the stopped one, run under
  `records/cc/instructions/cc_instruction_records_landing_2026_11_07.md`. Its two `STATUS.md` entries are the latest in
  that file (the stopped batch wrote none). Named only so the forward bound (4(b)) can move them; **you do not read it.**
- ***The test-only ruling*** — Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`.
- ***The correction record*** — `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`.
- ***The data file*** — `tools/audit/decisions/backbone_decisions.json`, the register's source of record.
- ***The standard form*** — the file's text equal to `json.dumps(json.loads(raw), indent=2, ensure_ascii=False) + "\n"`,
  where `raw` is the file's text. Three tools check this before they write the file and refuse otherwise (premise ledger).
- ***The joined lines*** — the seven lines of the data file, one per superseded entry, that hold both keys, each reading
  `      "status": "superseded-by", "superseded_by": "Ruling 1 of `` `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` ``",`
  (six leading spaces).
- ***The edited set*** — the seven files Tasks 1 to 3 edit by hand or script: the data file, `ARCHITECTURE.md`,
  `docs/llm_integration.md`, `records/cowork/rulings/cowork_document_route_rulings_2026_08_08.md`,
  `ratification_surfaces/cowork_comparison_l2_reading.md`, `ratification_surfaces/cowork_comparison_l0_l1_reading.md`,
  `ratification_surfaces/cowork_comparison_l3_reading.md`. (`DECISIONS.md` and `decisions/group_N.md` were regenerated
  by the stopped batch's register commit; this batch does not change them.)
- ***`<T0>`, `<T1>`, `<T2>`, `<T3>`*** — this batch's task commits (not the stopped batch's). ***`<ACT_DATE>`*** — the day
  the step runs.
- ***A capture*** — the output of `python tools/audit/gen_guard_state.py --check`, saved whole to a scratch file outside
  the repository and read. ***Compared verdict by verdict*** means every tool's PASS / FAIL / NOT RUN / HISTORICAL line
  side by side, and the tally line.
- ***Red by this batch*** — a tool that passed at the capture before a task and fails at the capture after it, whose
  printed cause names, or whose inputs (read at the tool's source) include, a file of the edited set changed by that task.
- ***Blob form*** — a `--numstat` or diff taken between two explicit blob hashes (`git diff --numstat <blob> <blob>`),
  as the stopped batch did when the shell-read guard refused a working-tree `git diff` (its report §6, departure 2). Use
  it wherever this dispatch names a `--numstat` or a diff.

---

## Ruling ledger

- **The correction record, Ruling 1 items 1 to 6** — what the stopped batch began and this batch finishes. Items 1 and
  2 are already applied at the start tip; this batch applies items 3 to 6. Item 7 (no act now) is not applied.
- **The test-only ruling and its Ruling 2** — the ground the correction record rests on.
- **The user's ruling of 2026-11-07 on the three standing modifications** (handoff entry 571 §2 item 1): *"Leave them -
  we will revisit this when we look at the externally compiled list of relevant research/software/algorithms. Then we
  can consolidate and fix whatever is needed."* — the ground for A1.
- **Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md`** — the dispatch form: no chain
  of earlier dispatches; what is needed from one is stated here.
- **Ruling 4 of the 2026-11-01 pruning record** — the report's two-file form (4(d)).
- **The register's own rule**, at `tools/audit/decisions/gen_decisions_register.py` line 16: *"To change an entry, edit
  `backbone_decisions.json` and re-run this generator."*
- **The data file's format rule**, enforced by the tree's own tools (premise ledger) — the ground for Task 1.
- **No new rule is made.** The amendment of the no-line-added rule above is to this side's own dispatch rule, not a
  ruling.

---

## Premise ledger (written 2026-11-07 by the writing side from staged working-tree copies read with the file tools; no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
  `4461d865fcb2c99ef20099487c0d4a4221456112`.
- **RELAYED — the chain** (the stopped batch's report §3 and §4; handoff entry 576 §1, read there at `.git/logs/HEAD`
  lines 2109–2110): `7c2d1bccc885b1e11204727f0800ffe20fd84b21` (the records landing's end state) →
  `566d37e583da3ee23d2d46957ead8eb202290973` (the stopped batch's Task 0) → `4461d865…` (its Task 1).
- **FACT — `STATUS.md`** (10,680 bytes, read whole): the records landing's TWO entries at lines 8 and 10 — its close
  entry carrying `Last updated: `, then its Task 0 `Same dispatch` entry; the two 2026-09-02 entries at 12 and 14; the
  archive-pointer paragraphs at 16, 18, 20 and 22, the one at 18 being the standing paragraph that holds the word
  *paraphrase* (called ***the paraphrase paragraph*** below). Exactly one line carries `Last updated: `. **No entry for the
  stopped batch.**
- **RELAYED — the guard state** (the stopped batch's appendix, its 0(f) capture and its 1(e) difference, read by the
  writing side):
  - `tools/audit/guard_state.json` at the start tip is the one committed by the records landing (the stopped batch did
    not reach its Task 5): run 83, 70 passing, 13 failing. **The thirteen standing reds:** `gen_phase3_gate_partition.py`,
    `gen_filing_convention_application.py`, `gen_artifact_inventory.py`, `gen_artifact_inventory_surface.py`,
    `gen_test_construction_evidence.py`, `gen_retirement_caller_check.py`, `gen_epoch_write_path.py`,
    `gen_recognizer_establishment_sort.py` (each under `tools/audit/`), and `apply_soft_discard.py`,
    `apply_residue_discard.py`, `gen_cluster_dispositions.py --verify`, `gen_home_classification.py`,
    `gen_phase1p_delegation_bar.py` (each under `tools/audit/decisions/`).
  - **The stopped batch's last capture (after its register commit):** run 83, **19 failing** — the thirteen;
    `gen_per_session_reading.py`; and five newly red: `tools/audit/gen_rulings_sort.py`,
    `tools/audit/gen_session_start_read_size.py`, `tools/audit/gen_defense_share.py`,
    `tools/audit/decisions/reaim_home_anchors.py`, `tools/audit/decisions/gen_live_prohibition_pointers.py`. 4 NOT RUN,
    20 HISTORICAL.
  - The classification `--check` STOPs (exit 2) naming five tools: `gen_l0_l1_outgoing_population.py`,
    `gen_l2_withheld_documents.py`, `gen_l3_outgoing_population.py`, `gen_per_session_reading.py`,
    `gen_withheld_family_reading.py`.
  **Read `tools/audit/guard_state.json` at the start tip yourself at 0(f); the object is the value of record.**
- **FACT — the format rule and the two refusing tools** (handoff entry 576 §2 item 2, read there at the tools):
  `tools/audit/decisions/reaim_home_anchors.py` (lines 97–103) and `tools/audit/decisions/gen_live_prohibition_pointers.py`
  (lines 161–170) refuse to run unless the data file is in the standard form. **RELAYED** (the stopped batch's report §1):
  `tools/audit/decisions/gen_home_classification.py` (lines 731–741) makes the same check; it was already failing at the
  records landing's end state.
- **RELAYED — the probe** (the stopped batch's appendix, last section; Claude Code's printout, not re-run by the writing
  side): at the start tip the data file has 22,554 lines when split on `\n` and its standard form 22,561; the only
  difference is the seven joined lines, each becoming a `status` line and a `superseded_by` line — seven removed,
  fourteen added.
- **FACT — the register's index is unchanged by the re-serialization in principle**: the generator reads the data as
  JSON (`gen_decisions_register.py`), and the re-serialization changes no value. 1(b) proves it with `--check`.
- **FACT — `tools/audit/gen_rulings_sort.py`** reads the data file (line 110 `BACKBONE`, parsed as JSON at line 483) and
  copies each sorted entry's `status` into its rows (line 524); its surface prints that status (line 910, `**status:**`).
  A search of the tool for `status` found no other use of the entry's status or of `status_source`. The tool's
  `classify()` was not read whole.
- **FACT — no citation of the data file by line number** was found in the set handoff entry 577 §2 item 1 names (above,
  under the amended rule). **If you meet one anywhere, report it as an observation; it is not a STOP.**
- **FACT — the design texts and the route record**, read at the objects at the start tip:
  - `ARCHITECTURE.md` line 8088 `## 19. LLM Integration — Claude Composer`; line 8089 blank; line 8090
    `> **Full design document:** `docs/llm_integration.md`` followed by two spaces.
  - `docs/llm_integration.md` line 1 `# LLM Integration in MuseScore Studio — Design Document`; line 2 blank; line 3
    `> **Status:** Design phase. No code written yet.` followed by two spaces.
  - `records/cowork/rulings/cowork_document_route_rulings_2026_08_08.md` (5,056 bytes) line 37 reads, whole,
    `  document is authoritative, not stale).`
  - `docs/llm_triage_design.md` exists (relayed from the stopped dispatch's ledger; not re-read).
- **FACT — the reading-file lines**, each found by one exact-text search, one hit each:
  - L2 (`ratification_surfaces/cowork_comparison_l2_reading.md`, 5,068,067 bytes): line 72468 holds
    `and its future as a plugin. **The placement readings are those of the earlier`; line 72557 holds
    `what the language-model integration is shown.` — item 1 of the list headed `#### Not a statement — listed so the
    arithmetic closes (34)` (heading at line 72555, relayed).
  - L0/L1 (`ratification_surfaces/cowork_comparison_l0_l1_reading.md`, 1,102,100 bytes): line 10142 holds
    `> **What it is.** The design of a natural-language interface to the score`.
  - L3 (`ratification_surfaces/cowork_comparison_l3_reading.md`, 5,135,149 bytes): line 30466 holds
    `— the defense of keeping the fields of Row 21.102.`
- **NOT KNOWN — which guard tools read the files Tasks 2 and 3 edit**, beyond those named in A2. A2 gives a rule, with a
  capture after each task, so a new red is located between two captures, and A2's rule then tests whether the task
  between them caused it. *(★ CORRECTED at C5; former wording in the check section.)*
- **ASSUMPTION A1 — the working tree, stated by CONTENT.** Tracked modifications at your boot: **exactly three** —
  `tools/audit/claude_md_finer_archive.json` (standing, carried), `docs/research_papers/BIBLIOGRAPHY.md` and
  `docs/research_papers/README.md`; and untracked, beside them, `docs/research_papers/polyph9-release/`. **The last three
  were made by another tool, unintentionally, and the user ruled them left as they are** (the ruling ledger). Also
  untracked and observed by the stopped batch: `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`. **You do
  not touch, restore, land or delete any of these five, and their presence is not a STOP.** If one is absent, report it;
  that is not a STOP. **The writing side wrote no tracked file.** Untracked and landed by Task 0: the landing set. Beyond
  it, only the standing untracked population, which is not landed and is not a STOP. **Your enumeration with
  `tools/audit/changed_paths.py` establishes A1.**
- **ASSUMPTION A2 — the reds.**
  - **At your boot, before Task 0:** `gen_per_session_reading.py --check` may STOP (exit 2; untracked handoff entries) or
    FAIL. Report what it printed; neither is a STOP. Do not run the full guard set before Task 0.
  - **The opening capture (0(f), after `<T0>`):** run 83; zero STOPs in the runner; **failing exactly the 19 the ledger
    names**, and nothing else.
  - **The captures after `<T1>`, `<T2>` and `<T3>` (1(c), 2(d), 3(d)):** each compared verdict by verdict with the one
    before. **A tool newly FAIL must be *red by this batch*** (the words above): you report its printed cause and the
    line of its source that reads the edited file, quoted. **Then exactly one of:**
    - **(regenerate)** the tool writes a derived artifact (it has a write mode) and its `--check` compares that artifact
      to what the inputs now give: run the bare write mode, then `--check` green, and diff the artifact against its blob
      before the task in blob form. **Every changed passage must be tied to an edit of that task or of the stopped
      batch's register commit**: a change only in (i) a whole-file size, line count or hash of a file of the edited
      set, or of a file the stopped batch's register commit changed (`DECISIONS.md` among them); (ii) a term-search hit,
      or a count of hits, that changes only because an edited line gained or lost the term; (iii) at Task 1 only, a
      line number of the data file lying below a joined line and moved down by the number of joined lines above it
      (report it also as an observation under the premise ledger's citation FACT) *(★ CORRECTED at C5; former wording
      in the check section)*; or, for the register, a status value of one of D-440 to D-443 and D-446 to
      D-448 becoming `superseded-by` (from `deferred` for D-440 and D-441, from `not stated` for the rest), and any count
      by status that those seven entries move, and nothing else. Quote each changed passage in the report, tie it to the
      edit by name, commit the regenerated artifact as the task says, and continue. **A member of any population, list
      or set entering or leaving, or any other changed passage, not so tied, is a STOP-and-report** (the task's commit
      stays; nothing further runs).
    - **(carry)** the tool compares the file to a fixed value recorded at an earlier act (a hash, a pinned size, a frozen
      copy): **do not regenerate and do not re-pin.** Record it as red by this batch, with its message, and continue.
      Its re-pinning is a question for the writing side, which the report names.
    - **Neither, or unsure:** STOP-and-report.
  - **A newly FAIL tool that is NOT red by this batch is a STOP-and-report.** A tool newly PASS is reported and is not a
    STOP.
  - **Reds named in advance:**
    - **At 1(c):** `reaim_home_anchors.py` and `gen_live_prohibition_pointers.py` expected FAIL → PASS (1(a) restores
      the standard form). `gen_rulings_sort.py`, `gen_session_start_read_size.py` and `gen_defense_share.py` are the
      stopped batch's red, still red at 0(f); 1(c) regenerates them under the (regenerate) branch, `gen_rulings_sort.py`
      with the register tie above and the two size tools with the `DECISIONS.md` member's size (the stopped batch
      regenerated `DECISIONS.md`) and every sum and share built on it. `gen_home_classification.py` stays in the
      thirteen; report whether its printed cause changed.
    - **At 2(d) and 3(d), possibly:** `tools/audit/gen_l2_outgoing_population.py` records whole-file byte sizes of the
      documents it names (its line 380), and it and `tools/audit/gen_l3_outgoing_population.py` read the transfer-list
      section (`## 10.`) of the L0/L1 and L2 reading files (`gen_l2_outgoing_population.py` lines 128 and 556;
      `gen_l3_outgoing_population.py` lines 187–194) [relayed from the stopped dispatch's check]. A size or hit change at
      an edited line is the tied case; anything else is a STOP-and-report.
    - **Already failing, so not "newly FAIL":** the thirteen. Report any change in what those that read the register
      print; it is not a STOP.
    - **Not observable:** `tools/audit/decisions/gen_r1_superseded_reach.py` is HISTORICAL in the runner (the stopped
      batch's report §4), so no capture shows it. Do not run it.
  - **Task 4:** `gen_session_start_read_size.py` and `gen_defense_share.py` expected RED again after 4(a) (both read
    `STATUS.md`); `gen_l3_outgoing_population.py --check` and `gen_l0_l1_outgoing_population.py --check` may be red after
    4(a)/4(b) (they carry a `STATUS.md` residue record with line values); `gen_per_session_reading.py` regenerated LAST
    and again at 4(c′).
- **ASSUMPTION A3** — no `src/` file, build, test, golden, corpus of scores or measurement of the analysis is touched.
- **ASSUMPTION A4 — THE FOOTPRINT.** **Task 0:** the landing set. **Task 1:** the data file, and the artifacts 1(c)
  regenerates (`tools/audit/rulings_sort_classification.json`,
  `ratification_surfaces/cowork_rulings_sort_surface_2026_08_16.md`, `session_start_read_size.json`,
  `defense_share.json`, each at the path its tool writes). **Task 2:** `ARCHITECTURE.md`, `docs/llm_integration.md`, the
  route record, and any artifact 2(d) regenerates. **Task 3:** the three reading files, and any artifact 3(d)
  regenerates. **Task 4:** `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py` at its authored
  aiming and head comments, `tools/audit/status_batch_bound.json`, the artifacts 4(c) and 4(c′) regenerate, the report and
  its appendix, `records/cowork/handoff/cowork_away_returns.md`. **Task 5:** `tools/audit/guard_state.json` and the
  away-returns end-state portion.
- **ASSUMPTION A5 — byte-unchanged by this batch:** `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS.md`,
  `DECISIONS_ARCHIVE.md`, `cowork_audit_protocol.md`, `FRAMEWORK.md`, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`; every file
  under `decisions/`; everything under `docs/` but `docs/llm_integration.md` (the A1 modifications stay as they are,
  unstaged); every tool under `tools/audit/` but `gen_status_batch_bound.py`; every file under `tools/audit/decisions/`
  but the data file; every ruling record but the route record; every handoff entry, ratification document, dispatch and
  report already tracked, but the three reading files, the rulings-sort surface and `cowork_away_returns.md`. **Excepted
  from this list: any artifact 2(d) or 3(d) regenerates under A2, named in the report.** *(★ CORRECTED at C5; former
  wording in the check section.)*

## The declared start state — at the tree you will meet

1. Both ref files at the start tip; A1's five standing items; the landing set untracked; nothing running.
2. The thirteen standing reds, `gen_per_session_reading.py`, and the stopped batch's five — 19 — none of them yet
   resolved; the classification's five-name STOP.

**A further untracked handoff entry appearing during the run** (the writing side's, after this dispatch is handed over):
do not land it; if it makes `gen_per_session_reading.py` STOP at 4(c), do not regenerate that artifact, report the STOP
with its message, and carry the tool as red into the end state.

## Findings in this batch

**No finding number is allocated.** A finding met during the run is written up on its own in the report and surfaced,
never absorbed.

---

## Task 0 — land the records, and PUSH

- **0(a) — the pin.** `git hash-object -w --no-filters` of this dispatch, in its own call; record its blob and
  `git cat-file -s`; re-hash immediately before staging, equal or STOP.
- **0(b) — the refs and the chain.** Read both ref files with the file tools against the FACT; then `git cat-file -p
  4461d865fcb2c99ef20099487c0d4a4221456112` (expected parent `566d37e583da3ee23d2d46957ead8eb202290973`) and `git
  cat-file -p 566d37e583da3ee23d2d46957ead8eb202290973` (expected parent `7c2d1bccc885b1e11204727f0800ffe20fd84b21`), each
  hash written literally in its own command. A different chain is a STOP-and-report with nothing committed.
- **0(c) — A1 and the landing set**, by `python tools/audit/changed_paths.py` (the sanctioned enumeration; `git status`
  is not used, D-253): exactly A1's three tracked modifications; **every path of the landing set untracked, and every
  untracked path under `records/cowork/handoff/`, `records/cowork/rulings/`, `ratification_surfaces/`,
  `records/cc/instructions/` and `records/cc/reports/` a path of the landing set**; other untracked paths only the
  standing population and A1's two untracked items. A path of the landing set missing, or an untracked path in those
  five folders outside it, is reported and is a STOP. **The landing set:**
  - **(i) handoff entries** — `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_six.md`,
    `…_five_hundred_and_seventy_seven.md`, and **every untracked handoff entry numbered above 577 at your boot**.
  - **(ii) the stopped batch's report and appendix** — `records/cc/reports/cc_report_llm_correction_2026_11_07.md` and
    `records/cc/reports/cc_report_llm_correction_2026_11_07_appendix.md`, as they stand. **Do not edit them.**
  - **(iii) this dispatch** — `records/cc/instructions/cc_instruction_llm_correction_resume_2026_11_07.md`.
- **0(d) — last bytes** of each landing file, at its blob written `--no-filters`, by one scratch script quoted whole in
  the appendix: each object's size, its last 70 bytes and its count of zero bytes. Each must end with a newline after a
  complete line and hold no zero byte; a final line broken off mid-word, or a zero byte, is a STOP-and-report naming the
  file. **Expected sizes, at the writing side's staging:** entry 576 7,274; entry 577 5,956; the stopped report 12,906;
  its appendix 21,864. **No size is stated for this dispatch or any entry above 577**; report every size in the appendix.
- **0(e) — the commit**, exactly the landing set and no other path, staged by explicit path, the staged set proved with
  `python tools/audit/changed_paths.py --staged`: **its count must equal the landing set's count.** Subject, exactly:
  `record: handoff entries 576 to <N>, the stopped batch's report, with the resume dispatch`, `<N>` the highest entry
  landed written as a number. Push; read `.git/refs/remotes/origin/master` and verify it equals the new tip. **This
  commit is `<T0>`.**
- **0(f) — the opening capture.** A capture, saved whole and read. Read the start tip's `tools/audit/guard_state.json` →
  `summary` at the object (`git show 4461d865fcb2c99ef20099487c0d4a4221456112:tools/audit/guard_state.json`) and report
  its run, counts and failing set by name. Then `python tools/audit/gen_guard_classification.py --check`, expected exit 2,
  a STOP naming the five tools of the premise ledger — report them by name; a different set is a STOP-and-report. **The
  failing set must be the 19 of A2.** Anything else is reported and is a STOP.

**E0:** the landing set in one commit, pushed; the pin proved; A1 reported with its enumeration; the opening capture as
A2 states it; the five-name STOP.

---

## Task 1 — the data file returned to its standard form; the stopped batch's reds regenerated

**1(a) — the re-serialization, by one scratch script**, saved outside the repository, quoted whole in the appendix, run
from the repository root with `python <script>`. It writes the standard form, and proves before writing that the only
difference from the file is the seven joined lines, each split in two. **The script, exactly:**

```python
# The register's data file returned to its standard form after the 2026-11-07 supersession.
import json, pathlib, sys
P = pathlib.Path("tools/audit/decisions/backbone_decisions.json")
raw = P.read_bytes().decode("utf-8")
if "\r\n" in raw:
    sys.exit("STOP: the data file has CRLF line endings; report and do not edit")
data = json.loads(raw)
new = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
if json.loads(new) != data:
    sys.exit("STOP: the re-serialized data differs in value")
HEAD = '      "status": "superseded-by", "superseded_by": "'
a, b = raw.split("\n"), new.split("\n")
joined = [k for k, l in enumerate(a) if l.startswith(HEAD)]
if len(joined) != 7:
    sys.exit(f"STOP: {len(joined)} joined lines, expected 7")
expected = []
for k, l in enumerate(a):
    if k in joined:
        expected.append('      "status": "superseded-by",')
        expected.append('      "superseded_by": "' + l[len(HEAD):])
    else:
        expected.append(l)
if expected != b:
    sys.exit("STOP: the standard form differs from the file in more than the seven joined lines")
P.write_bytes(new.encode("utf-8"))
print(f"re-serialized: {len(joined)} joined lines split; lines {len(a) - 1} -> {len(b) - 1}")
```

**Expected:** it prints `re-serialized: 7 joined lines split; lines <N> -> <N+7>` and exits 0. Any `STOP` line is a
STOP-and-report with the file unwritten. Then `--numstat` of the data file between its blob at the start tip and its new
blob: **expected `14	7`** (fourteen lines added, seven removed).

**1(b) — the proofs before the commit**, each in its own call, each output kept:
1. `python tools/audit/decisions/gen_decisions_register.py --check` — **expected exit 0**: the register's index and group
   files do not change, because no value changed. A `STALE` line is a STOP-and-report with nothing committed.
2. `python tools/audit/decisions/reaim_home_anchors.py --check` — **expected exit 0.**
3. `python tools/audit/decisions/gen_live_prohibition_pointers.py --check` — **expected exit 0.**
4. `python tools/audit/decisions/gen_home_classification.py --check` — already failing (the thirteen); report what it
   prints, and whether its `REFUSED: re-serializing …` line is gone. Not a STOP.

If 2 or 3 does not exit 0, report its whole output: a `REFUSED` line is a STOP-and-report; any other failure is handled
by A2's rule as if at a capture, tied only as A2 says.

Then the commit, exactly the data file, by explicit path, proved with `changed_paths.py --staged` (count 1). Subject:
`decisions: the register's data file re-serialized to its standard form after the 2026-11-07 supersession`. Push;
verify `origin/master` at the ref file. **This commit is `<T1>`.**

**1(c) — the capture after `<T1>`**, compared verdict by verdict with 0(f)'s. **Expected:** `reaim_home_anchors.py` and
`gen_live_prohibition_pointers.py` FAIL → PASS; nothing else changed. Then the three regenerations, each check first in
its own call, then the bare write mode, then `--check` green:
1. `python tools/audit/gen_rulings_sort.py` — tie: in `rulings_sort_classification.json` and
   `cowork_rulings_sort_surface_2026_08_16.md`, only the `status` values of those of D-440 to D-443 and D-446 to D-448 that
   are in its population, as A2 states, and any hash or size of the data file the artifacts record. **A row whose
   `proposed_class` or `decided_by` changes, or a row entering or leaving, is a STOP-and-report.** Name which of the
   seven are in its population.
2. `python tools/audit/gen_session_start_read_size.py` — tie: the `DECISIONS.md` member's size, the total and the
   comparisons built on it.
3. `python tools/audit/gen_defense_share.py` — tie: the whole-read denominator and the share against it.

Each artifact diffed against its blob at `<T1>` in blob form, by a scratch script quoted whole in the appendix, every
changed passage accounted for. Then one commit of the regenerated artifacts, by explicit path, proved; subject
`artifacts: regenerated after the register correction`; push; verify. Then the capture again: **expected failing exactly
the thirteen and `gen_per_session_reading.py` — 14.** Report every tool by name.

**E1:** the data file in its standard form, `14 7`, the register unchanged; `<T1>` pushed; the two refusing tools green;
the three artifacts regenerated and every changed passage tied; 14 failing.

---

## Task 2 — the two design texts marked superseded; the route record noted (Ruling 1 items 3 and 4)

**Each edit below is made with the file-editing tool, `old_string` → `new_string` exactly as given; before each, search
the file for the `old_string` and confirm it occurs exactly once (else STOP-and-report).** In each of 2(a) and 2(b), the
blank line between a heading and a blockquote is replaced by the banner line, which joins the blockquote below it as its
first line; the banner line ends with **exactly two spaces** (a hard line break), shown below as `␠␠` — type two space
characters, not the symbol. No other character changes.

**2(a) — `ARCHITECTURE.md` §19** (Ruling 1 item 3). `old_string` (three lines):

```
## 19. LLM Integration — Claude Composer

> **Full design document:**
```

`new_string` (three lines; the second is one line, ending in two spaces):

```
## 19. LLM Integration — Claude Composer
> **★ SUPERSEDED 2026-11-07 by Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`** (the user: "LLM:S are only to be used during development of the software solution (in order to better it). Never at run-time in the finished product."). This section and its subsections describe a language model at run time in the finished product. Their text is kept below as it stood (#12) and is not a design to build. The test-time second opinion that ruling allows is discussed in `docs/llm_triage_design.md`. Applied under Ruling 1 item 3 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`.␠␠
> **Full design document:**
```

**2(b) — `docs/llm_integration.md`** (Ruling 1 item 3; the banner covers the whole document, its §2.5 included).
`old_string` (three lines):

```
# LLM Integration in MuseScore Studio — Design Document

> **Status:** Design phase.
```

`new_string` (three lines; the second is one line, ending in two spaces):

```
# LLM Integration in MuseScore Studio — Design Document
> **★ SUPERSEDED 2026-11-07 by Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`** (the user: "LLM:S are only to be used during development of the software solution (in order to better it). Never at run-time in the finished product."). This document describes a language model at run time in the finished product. Its text is kept below as it stood (#12) and is not a design to build. The test-time second opinion that ruling allows is discussed in `docs/llm_triage_design.md`. Applied under Ruling 1 item 3 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`.␠␠
> **Status:** Design phase.
```

**2(c) — the route record** (Ruling 1 item 4), `records/cowork/rulings/cowork_document_route_rulings_2026_08_08.md`.
`old_string` (one line, the whole of line 37, with its two leading spaces):

```
  document is authoritative, not stale).
```

`new_string` (one line):

```
  document is authoritative, not stale). ★ NOTE 2026-11-07 (Ruling 1 item 4 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`): Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` supersedes `docs/llm_integration.md` and `ARCHITECTURE.md` §19. This bullet's wording is kept as the 2026-08-08 record; the delegation it made now points at a superseded design.
```

**Proof of 2(a) to 2(c):** for each file, its line count (a count of newline bytes) before and after, equal; `--numstat`
for the three: **`1	1` each**; and the new line read back with the file tools, checked for the two trailing spaces
in 2(a) and 2(b). **And for each of `ARCHITECTURE.md` and `docs/llm_integration.md`, a search for the symbol `␠`
(U+2420) returns zero hits; one hit means the symbol was typed instead of two spaces, and is fixed before the commit.**
Then the commit, exactly the three files, by explicit path, proved (count 3). Subject: `docs: ARCHITECTURE.md section 19
and docs/llm_integration.md marked superseded by the 2026-11-07 language-model ruling; the 2026-08-08 route record
noted`. Push; verify `origin/master`. **This commit is `<T2>`.**

**2(d) — the capture after `<T2>`**, compared verdict by verdict with 1(c)'s last, and A2's rule applied to every tool
newly FAIL; a regeneration's artifact goes in a commit of its own, subject `artifacts: regenerated after the superseded
banners`, by explicit path, proved, pushed, and the capture is run again.

**E2:** three one-line edits, no line added, `<T2>` pushed; every new red traced to Task 2 and handled by A2's rule.

---

## Task 3 — the reading files annotated (Ruling 1 items 5 and 6)

**Each annotation is inserted inside an existing line; no line is added.** The same file-editing discipline as Task 2:
the `old_string` occurs exactly once, else STOP-and-report. **The reading files are about 1 to 5 MB each: locate each
`old_string` with one search for that exact text, never with a pattern that matches many rows, and read only the
matched line.**

**3(a) — the L2 reading file**, `ratification_surfaces/cowork_comparison_l2_reading.md` (item 5), two edits.

*First,* the member's description (line 72468). `old_string`:

```
and its future as a plugin. **The placement readings are those of the earlier
```

`new_string`:

```
and its future as a plugin. [★ ANNOTATED 2026-11-07 under Ruling 1 item 5 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`, this member's wording kept (#12): its description of the language-model integration as *a product tool outside the analysis* is stale. Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` rules that a language model is never used at run time in the finished product; the integration is superseded, and a language model may only give a second opinion when the product is tested and struggles with inference. The dispositions are not changed.] **The placement readings are those of the earlier
```

*Second,* item 1 of the list *Not a statement — listed so the arithmetic closes (34)* (line 72557). `old_string`:

```
what the language-model integration is shown.
```

`new_string`:

```
what the language-model integration is shown. [★ ANNOTATED 2026-11-07 under Ruling 1 item 5 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`, for items 1 to 34 of this list, their wording kept (#12): *a product tool outside the analysis* is stale for the language-model integration, which Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` supersedes. The dispositions are not changed.]
```

**3(b) — the L0/L1 reading file**, `ratification_surfaces/cowork_comparison_l0_l1_reading.md` (item 5), the manifest
description (line 10142). `old_string`:

```
> **What it is.** The design of a natural-language interface to the score
```

`new_string`:

```
> **What it is.** [★ ANNOTATED 2026-11-07 under Ruling 1 item 5 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`, this description's wording kept (#12): the document describes a language model at run time in the finished product, which Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` rules out; the document is superseded. The dispositions are not changed.] The design of a natural-language interface to the score
```

**3(c) — the L3 reading file**, `ratification_surfaces/cowork_comparison_l3_reading.md` (item 6), the end of item 21
(line 30466). `old_string`:

```
— the defense of keeping the fields of Row 21.102.
```

`new_string`:

```
— the defense of keeping the fields of Row 21.102. [★ ANNOTATED 2026-11-07 under Ruling 1 item 6 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`, the wording kept (#12): the language-model half of this defense no longer holds, because Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` supersedes `docs/llm_integration.md`. The other half, the Authoritative Chord Symbol Mode (§4.1f), stands. Row 21.102's proposed QUARANTINED is not changed.]
```

**Proof of 3(a) to 3(c):** each file's line count before and after, equal; `--numstat`: **L2 `2	2`, L0/L1 `1	1`, L3
`1	1`**; each changed line read back by its line number (72468, 72557, 10142, 30466) with the file tools. A changed line
at any other number is a STOP-and-report. Then the commit, exactly the three files, by explicit path, proved (count 3).
Subject: `records: the reading files' language-model descriptions annotated under the 2026-11-07 correction`. Push;
verify `origin/master`. **This commit is `<T3>`.**

**3(d) — the capture after `<T3>`**, as 2(d), the regeneration commit's subject `artifacts: regenerated after the
reading-file annotations`.

**E3:** four in-line annotations, no line added, `<T3>` pushed; every new red traced to Task 3 and handled by A2's rule.

---

## Task 4 — the close (written out in full; no earlier dispatch is read)

**4(a) — the `STATUS.md` entries FIRST**, at the top, above the records landing's close entry: one pointer entry per
committed task — **the close entry first**, naming this dispatch by its file name
(`records/cc/instructions/cc_instruction_llm_correction_resume_2026_11_07.md`) and carrying the `Last updated: ` prefix;
then the entries of Tasks 3, 2, 1 and 0 below it, in that order, each opening `Same dispatch`; in the OI-222 pointer
convention, the whole of each being your report; no value restated (D-431); each entry a separate paragraph, separated
by one blank line, in the shape of the entries at lines 8 and 10. **★ THE PREFIX IS MOVED, NOT COPIED, AND THE MOVE IS
COMPLETE BEFORE 4(b) RUNS:** in the same act remove `Last updated: ` — and nothing else — from the records landing's close
entry (now at line 8); read `STATUS.md` after the edit and confirm exactly one line carries `Last updated: `. **The close
entry says in plain words:** that this batch finished the application of Ruling 1 items 1 to 6 of the 2026-11-07
correction record, which the batch under `records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md` began and
stopped after its register commit (seven register entries superseded by the 2026-11-07 language-model ruling and two
noted); that this batch returned the register's data file to its standard form, marked the two design texts superseded,
noted the 2026-08-08 route record and annotated the three reading files — every text kept; **no tool edited or added but
the forward-bound tool's re-aiming; no algorithm change; no new decisions-register entry, no `D-NNN`, no open-items
row**; and that the whole is the report. **Then the search:** case-insensitive, every term of `L3_KEYWORDS` (read 5 of
the first read) plus *repeat* and *tie*, each as a substring, over `STATUS.md` — **expected: hits only inside the
paraphrase paragraph**; any other hit is reworded at your own new entries and the search re-run; report the hits as
found. **This expectation is carried from earlier dispatches; the writing side did not run the search at `STATUS.md`.
A hit in an entry you did not write is reported and not reworded, and it is not a STOP.** *(★ CORRECTED at C5; former
wording in the check section.)*

**4(b) — the forward bound.** Read `tools/audit/gen_status_batch_bound.py` at the object
`4461d865fcb2c99ef20099487c0d4a4221456112:tools/audit/gen_status_batch_bound.py` first (a scratch file, searched for its
constants) and **report its authored constants as you find them**. **Expected, RELAYED** (not read at the tool by the
writing side): `BASE_COMMIT` `113b2ce680e527e81342d8f79d5acbad281334d7`, `PREVIOUS_BATCH_DISPATCH`
`cc_instruction_boot_chain_landing_2026_11_02.md`, `DISPATCH` `cc_instruction_records_landing_2026_11_07.md`, `TASK`
`Task 3`, `MOVE_KIND` `ordinary`, `ACT_DATE` 2026-11-07. A difference is reported and 4(b) proceeds from what the object
holds. **Re-aim all of them:**
- `BASE_COMMIT` — this batch's last task commit before the close: `<T3>`, or the last regeneration commit after it if
  3(d) made one. **Check that the `STATUS.md` blob at `BASE_COMMIT` equals its blob at the start tip, each `git rev-parse`
  in its own command.**
- `PREVIOUS_BATCH_DISPATCH` — `cc_instruction_records_landing_2026_11_07.md` (the stopped batch wrote no `STATUS.md`
  entry, so the records landing's entries are the ones that move).
- `DISPATCH` — `cc_instruction_llm_correction_resume_2026_11_07.md`. `TASK` — `Task 4`. `MOVE_KIND` stays `ordinary`.
  `ACT_DATE` — the day the move runs.
- Append this batch's aiming to `PREVIOUS_AIMINGS` in the shape of the rows above it (the records landing's aiming is
  already its last row — do not append it twice); amend the head comments as the previous batches did, each former value
  named, not deleted (#12).

**Then `--apply` and `--check`, each in its own call.** **Prediction: exactly the records landing's TWO entries move** —
its close entry (from which 4(a) removed the prefix) and its Task 0 `Same dispatch` entry, at the base's lines 8 and 10;
the two 2026-09-02 entries stay; no STOP. Name the entries that moved, read at the artifact's `the_moved`. **If the tool
STOPs:** establish its cause first (D-669); if the cause is 4(a)'s prefix move incomplete, complete it, re-run the search
and the tool, and declare it; for any other cause, restore the tool's passing aim, re-run it green, report the STOP with
its message, and move nothing by hand. **No correction line is inserted in `STATUS_ARCHIVE.md`.** After the move, the
four checks that read the archive, each in its own call, each exit 0 expected, each output kept: `python
tools/audit/gen_status_batch_bound.py --check`, `python tools/audit/gen_governing_surface_split.py --check --pair
STATUS.md`, `python tools/audit/gen_status_residue_move.py --check`, `python tools/audit/gen_status_archive_pass.py
--check`.

**4(c) — the regenerations**, each check first in its own call, then each red one regenerated (write mode, the bare
invocation) and checked again, all exit 0:
1. `gen_session_start_read_size.py` and `gen_defense_share.py` — expected RED (the `STATUS.md` member), regenerated.
2. `gen_l3_outgoing_population.py --check` and `gen_l0_l1_outgoing_population.py --check` — each regenerated only if
   red; **if regenerated, only line values inside its `STATUS.md` residue record may move.** A member of either
   population, or of `the_tabulation_population`, moving is a STOP-and-report.
3. `gen_derivation_boot_pack.py --check` — expected GREEN unless 1(c), 2(d) or 3(d) recorded it red by this batch; the
   manifest is NOT regenerated here in either case.
4. **LAST, after the final edit to `STATUS.md` and after `gen_session_start_read_size.py` has been regenerated:**
   `python tools/audit/gen_per_session_reading.py` (write mode; its `--check` red before), then `--check` GREEN.

**Each moved artifact is diffed against its blob at `<T3>` (or the last regeneration commit)** in blob form, by a scratch
script quoted whole in the appendix, **and every changed passage is accounted for.** Expected:
`session_start_read_size.json` — the `STATUS.md` member, the total and the comparisons built on the total;
`defense_share.json` — the whole-read denominator and the share against it; `per_session_reading.json` — the ordinary
read's `STATUS.md` member and every sum and mirror that includes it; **in `the_cowork_boot_chain`, the three latest
handoff entries (name the three, as the tool orders them, and say how any tie at `<T0>` was broken) and the sums that
include them**; **in `the_reports_with_an_appendix_beside_them`, the stopped batch's pair landed at `<T0>`
(`count` one higher, the two sums higher by its two files' sizes in CHARACTERS as the tool reads them — `len()` of the
decoded text, its lines 720–721 — not the byte sizes of 0(d); one added pair naming
`cc_report_llm_correction_2026_11_07.md`)**; and, **because the artifact at `<T3>` is the one last made current at the
records landing's end state** (relayed: the tool passed there and the stopped batch committed no artifact of it), **the
handoff population gaining entries 570 onward, and every sum, mirror and share built over it. The dispatch and report
populations do not move:** the tool admits to them only file names opening `cc_instruction_l3_comparison_tabulation_` and
`cc_report_l3_comparison_tabulation_` (its lines 203 and 205). **Any other movement is reported by field.** *(★ CORRECTED
2026-11-08 at C5; former wording in the check section.)* *(★ CORRECTED
2026-11-07 at the writing side's check, the sitting booted on entry 578. Former wording, kept (#12): "and **in
`the_reports_with_an_appendix_beside_them`, the stopped batch's pair landed at `<T0>` (`count` one higher, the sums
higher by its two sizes, one added pair naming `cc_report_llm_correction_2026_11_07.md`)**." Why: it named neither the
unit of the tool's sizes nor the three populations that also move.)*

**4(d) — THE REPORT, IN THE TWO-FILE FORM OF RULING 4 OF THE 2026-11-01 RECORD.** That ruling's words (RELAYED; read the
2026-11-01 record if the wording matters to a step): *"a Claude Code report is written in two files, committed in the
same commit: the REPORT PROPER — the ordered first read, the capacity judgments, every task's account, every claim,
grade, declared departure, finding and observation, every check's verdict, and for every scripted search its terms, its
hit count and the rows named — and a separate APPENDIX FILE beside it, named in the report with its path, its size and the
searches it holds, carrying the raw printouts verbatim (every hit line as the search printed it) and nothing the report
proper needs."*
- **The report proper**, `records/cc/reports/cc_report_llm_correction_resume_2026_11_07.md`: your first tool call named
  exactly; your account of what reached you as injected context; the eight-line check with each line as read and as
  injected; a capacity judgment; Tasks 0 to 4, each with what it did and every check's verdict — **for each capture its
  header line, its counts, its failing set by name, and every line that differs from the capture before it**; **for every
  tool newly red at 1(c), 2(d) or 3(d): its cause as printed, the source line that reads the edited file, and whether it
  was regenerated or carried**; 0(c)'s enumeration against the landing set and A1; 0(d)'s result; 1(a)'s output, 1(b)'s
  four outputs and 1(c)'s accounting, naming which of the seven entries are in the rulings sort's population; every
  `--numstat`; the commits in a table (task, commit, parent, the number of committed blobs); 4(b)'s constants as found
  and as set and `the_moved`; 4(c)'s moved values per artifact; E0 to E4 and A1 to A5 graded (E5 and A4/A5 at Task 5);
  declared departures; observations met and not acted on (a citation of the data file by line number, if you meet one,
  goes here); **a short paragraph on whether this dispatch could be executed without reading any earlier dispatch or
  report, and if not, which step sent you to one**; **the list of tools carried red by this batch, as questions for the
  writing side**; and **the tell in one sentence: did this batch produce anything other than the landing set, the edited
  set, the artifacts 1(c), A2 and 4(c) regenerated, the Task 4 files, the report and its appendix, the away-returns
  section, the end state's guard artifact — and, outside the repository, scratch files and loose blob objects? If yes,
  name it.**
- **The appendix**, `records/cc/reports/cc_report_llm_correction_resume_2026_11_07_appendix.md`, beside it: the raw
  printouts verbatim, each under a heading naming its command and step — A1's enumeration whole, 0(d)'s script and
  output, 1(a)'s script and output, 1(b)'s four outputs, every `--numstat`, every capture whole, every regeneration diff,
  the 4(b) apply and the four archive checks, every 4(c) check and diff whole. **The report proper names the appendix
  with its path, its size in bytes and the list of what it holds.**

**4(c′) — THE LAST REGENERATION, after 4(d) has written the report and its appendix in their final form and before
4(e).** Run `python tools/audit/gen_per_session_reading.py` (write mode) once more, then `--check` GREEN, and diff the
artifact against the one 4(c) left: **expected, only `the_reports_with_an_appendix_beside_them`: `count` one higher, the
two sums higher by this batch's two sizes in characters as the tool reads them, and one added pair naming
`cc_report_llm_correction_resume_2026_11_07.md`.** *(★ CORRECTED 2026-11-07 at the writing side's check: "in characters
as the tool reads them" added; the former wording is the same sentence without those words (#12).)*
Anything else is reported and is a STOP before 4(f). **After this run neither the report nor its appendix is edited
again**; the run's output and its diff go in the away-returns section of 4(e), not in the report.

**4(e) — the close section appended to `records/cowork/handoff/cowork_away_returns.md`**, headed **THE LANGUAGE-MODEL
CORRECTION OF 2026-11-07, RESUMED — RULING 1 ITEMS 1 TO 6 APPLIED; DOCUMENTATION AND RECORD-KEEPING ONLY, NO ALGORITHM
CHANGED** *(★ CORRECTED at C5; former wording in the check section)*: the
report's content as pointers, 4(c′)'s output and diff, and **the plan line:** *"The next act is the writing side's — the
check of this batch's return at the objects; then L3 family 7's check (the language-model family surface)."* Read the
file's last section before appending, for its form; append only.

**4(f) — the close commit** carries `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`,
`tools/audit/status_batch_bound.json`, every artifact 4(c) and 4(c′) moved, the report, its appendix and
`records/cowork/handoff/cowork_away_returns.md` — by explicit path, the staged set proved with `changed_paths.py
--staged`. Subject: `Close: the language-model correction of 2026-11-07, resumed - Ruling 1 items 1 to 6 applied, under
its dispatch`. Push; verify `origin/master` at the ref file. **Held back:** A1's five standing items, the standing
untracked population, any handoff entry that appeared during the run, every scratch file. **The close does not assert
the end state**; Task 5 carries it.

**E4:** at the tree carrying the close, every check 4(b) and 4(c) name green; `gen_guard_state.py`'s own artifact stale
until Task 5; nothing outside A4 changed.

---

## Task 5 — the end state

- **The run:** `python tools/audit/gen_guard_state.py` (write mode, named) at the tree the close commit left, its output
  saved whole. **The condition:** run **83**; zero STOPs in the runner; **the failing set exactly the thirteen plus the
  tools carried red by this batch at 1(c), 2(d) and 3(d), named, none other**; `gen_per_session_reading.py --check`,
  `gen_decisions_register.py --check` (as the runner names it), `gen_rulings_sort.py --check`,
  `gen_session_start_read_size.py --check`, `gen_defense_share.py --check`, `reaim_home_anchors.py --check`,
  `gen_live_prohibition_pointers.py --check` and `gen_l3_outgoing_population.py --check` PASS unless carried; the NOT RUN
  and HISTORICAL lines identical to the opening capture's; against the opening capture **the verdicts that differ are
  exactly those six tools — `gen_per_session_reading.py` and the stopped batch's five — FAIL → PASS, and the carried
  tools PASS → FAIL**. Then `python tools/audit/gen_guard_classification.py --check`, its STOP naming the same five
  tools as at 0(f) — a further name is a STOP-and-report.
- **The verification at the objects:** `git diff --name-status 4461d865fcb2c99ef20099487c0d4a4221456112 <the close
  commit>`, every path accounted for against A4 and the landing set, **every file A5 names absent from it** (the landing
  set's own files appear once, as additions).
- **The record:** append the end-state portion to this batch's section of `records/cowork/handoff/cowork_away_returns.md`
  — the run's header, counts and failing set by name, the comparison with the opening capture, the classification STOP,
  the name-status list's counts by status and every path by name, A4 and A5 graded, the close commit's hash. Commit
  `tools/audit/guard_state.json` and that file only, by explicit path, the staged set proved. Subject: `End state: the
  language-model correction of 2026-11-07, resumed - guard run at the close tree`. Push; verify `origin/master` at the
  ref file.

**E5:** the condition held at a fresh run committed only after the run that produced it.

**THIS BATCH ENDS HERE.**

---

## What this batch does NOT do

- **No algorithm change; no measurement of the analysis.** The edited design texts are marked superseded, not
  rewritten; their text stays. The data file's values do not change.
- **Ruling 1 item 7 is not applied** — Ruling 57 clause (ii), Ruling 62 item 11, the DESIGN-INTENT seed list, the
  document's membership of the specification document set, and the four leak-check records stay as they are.
- **No text moves out of any governing document**; `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS.md`,
  `DECISIONS_ARCHIVE.md` and `cowork_audit_protocol.md` are not edited.
- **No tool edited or added** but the forward-bound tool's re-aiming. No guard enrolment changes; no classification
  verdict is authored; **no pinned value is re-pinned.**
- **No line is added to or removed from any file Tasks 2 and 3 edit.** The data file gains seven lines (Task 1).
- **The stopped batch's report and appendix are landed as they stand and not edited; no earlier report is corrected.**
- **No new decisions-register entry, no `D-NNN`, no open-items row.**
- **A1's five standing items are not touched.**

## What this batch deliberately leaves to later acts, named so it is not lost

- **The tools carried red by this batch**, if any — their re-pinning is the writing side's question, put to the user if
  the record does not answer it.
- **The register's home anchors** for D-440 to D-448 (`ARCHITECTURE.md` and `docs/llm_integration.md` line ranges) do
  not move, because no line is added there; whether a superseded entry's home should point elsewhere is not decided here.
- **Places not searched for line-number citations of the data file** (outside the set handoff entry 577 §2 names).
- **L3 family 7's check** (the language-model family surface) — the writing side's, after this batch's return is
  verified.
- **What the scope document leaves open** (correction record §2): its §3D (places not searched: `src/`, the `docs`
  sub-folders, `DECISIONS.md` beyond the rows read) and §7 item 3 (a search of the whole rulings folder).
- **The three standing modifications of A1** — the user's, when the externally compiled list of research, software and
  algorithms is taken up.
- **Carried, unchanged:** the measurement tool's boot-chain block after the 2026-11-02 Ruling 1; the three-latest pick by
  name where add-commit times tie; the classification tool's five unauthored verdicts; the decisions register's drifted
  home anchors; `gen_r1_superseded_reach.py` HISTORICAL in the runner.

---

## This file's check at its sources (D-434; runs in a turn of its own)

*Not yet run. The writing side's check is recorded here, with every former wording, before the banner is set to
RELEASED.* *(The former wording of this section, kept (#12). The check is now PART RUN, below.)*

**PART RUN 2026-11-07 by the Cowork sitting booted on handoff entry 578, at staged working-tree copies read with the file
tools; no git command run.** Entry 578 §3 step 3 named five points. Four are settled here; the fifth is not run.

- **C1 — 1(b)'s expectation that the two refusing tools exit 0 after 1(a): HOLDS.**
  `tools/audit/decisions/reaim_home_anchors.py` returns 0 under `--check` whenever it passes its format guard (lines
  105–110: it prints the drift and returns). `tools/audit/decisions/gen_live_prohibition_pointers.py` past its guard
  (lines 167–170) rewrites the pointer only in the `status_source` of its class members, read from
  `tools/audit/decisions/phase1w_legacy_verification.json` (`transfer` = `live-prohibition-in-spec`, line 59; fourteen
  such members there), and a search of that file for `D-440` to `D-448` found none; its pointer text carries
  `ARCHITECTURE.md` line numbers of three do-not-retry lines (lines 76–79, 111), which Task 2 does not move because it
  adds no line. Both tools passed at the records landing's end state (the stopped appendix, its 0(f) capture).
- **C2 — the rulings sort: HOLDS; all seven are in its population.** The population is the filter artifact's
  `proposed_class` = `DECIDING-ACT-NAMED` (`gen_rulings_sort.py` lines 120, 476–478); in
  `tools/audit/decisions_filter_classification.json` each of D-440 to D-448 carries that class (lines 13161 to 13456), so
  D-440 to D-443 and D-446 to D-448 are all in it, and D-444 and D-445 too. `classify()` (from line 377, read to line 421, its last
  branch's opening) and `word_hits()` (lines 366–374) read, in the lines read, `home_is_layer_spec`, `nonspec_kind`, `home`, `title` and `plain` only; the last branch's
  body was not read. The stopped commit changed
  the seven `status` values and put its nine notes in `status_source` (nine hits of the two 2026-11-07 note openings on
  `"status_source"` lines of the data file); neither field is read in the lines read, so no `proposed_class` or `decided_by` is
  expected to move from that commit, and 1(c) item 1's STOP on such a move covers the part not read. *(★ CORRECTED at
  C5; former wording in C5 below.)* 1(c) item 1's tie stands as written. **Not read:** whether the artifacts record a hash or size
  of the data file; 1(c) item 1 already ties such a change.
- **C3 — the two size tools: HOLDS.** `gen_session_start_read_size.py`'s members are `CLAUDE.md`, `STATUS.md` and
  `DECISIONS.md` (lines 140–148); of these only `DECISIONS.md` changed at the stopped commit (its 1(d), three staged
  paths). `gen_defense_share.py` measures defense clauses inside `CLAUDE.md`'s spans and takes its denominators through
  the imported reader (its lines 15–30, 120), so the movement expected is the whole-read denominator and the share against it; any other is A2's
  STOP. *(★ CORRECTED at C5; former wording in C5 below.)*
  1(c) items 2 and 3 stand as written.
- **C4 — 4(c)'s expectation for `per_session_reading.json`: CORRECTED** at its site, former wording kept. The tool reads
  its dispatch, report and handoff populations from the folder listing and STOPs on a member with no add-commit
  (`gen_per_session_reading.py` lines 356–365, 701–706). *(★ CORRECTED at C5; former wording in C5 below.)* But
  its sizes are characters (lines 720–721), and the expectation named neither that nor the three populations that also
  move since the artifact was last current. 4(c′) given the same unit.
- **C5 — A2's tie wording ("at or because of the edited lines") and the overstatement sweep (every, all, none, only,
  exactly, never, each hit read at its line): NOT RUN.** Capacity ended this sitting first. **The banner stays NOT YET
  RELEASED until C5 is run and recorded here.** *(The former wording of this bullet, kept (#12). C5 is now RUN, below.)*

**C5 — RUN 2026-11-08 by the Cowork sitting booted on handoff entry 579**, at staged working-tree copies read with the
file tools; no git command run. Objects read for it, beyond this file: `STATUS.md` whole; the test-only ruling record
at its lines 1–34; `tools/audit/gen_per_session_reading.py` at lines 193–206, 338–343, 350–369, 389–401 and 690–728.

- **A2's tie wording: CORRECTED.** Two defects. (1) The tie admitted a size change only *"of a file of the edited
  set"*, but 1(c) items 2 and 3 and A2's own *Reds named in advance* expect the two size tools to move by `DECISIONS.md`'s
  size, and `DECISIONS.md` is outside the edited set (the words-explained list says so). Read literally, the general
  sentence made 1(c)'s named ties a STOP. (2) *"because of"* set no bound on what could be argued as caused. Former
  wording, kept (#12): *"a change only in a size, line count, hash or term-search hit of a file of the edited set, at or
  because of the edited lines; or,"*. The new wording names three tied kinds, the third (data-file line numbers below a
  joined line, Task 1 only) so that it agrees with the premise ledger's rule that a line-number citation of the data
  file is an observation, not a STOP.
- **The overstatement sweep:** the six words searched over this whole file, this check section included, and each hit
  read at its line. Hits that are instructions, STOP conditions or expectations stated as such stand. Hits checked at
  an object and holding: line 104's *"the stopped batch wrote none"* and the ledger's *"Exactly one line carries
  `Last updated: `"* (`STATUS.md`, read whole: only its line 8 carries it, and no entry is the stopped batch's); line 17's
  paraphrase and the two banners' quotation of the user (the test-only record, lines 25–34); 3(a)'s *"may only give a
  second opinion when the product is tested and struggles with inference"* (the same lines). **Corrected at their sites:**
  - **The title and 4(e)'s heading.** Former wordings, kept (#12): *"— DOCUMENTATION ONLY; NO ALGORITHM CHANGE"* and
    *"; DOCUMENTATION ONLY, NO ALGORITHM CHANGED"*. Why: the body's own *Documentation and algorithm* paragraph excepts
    4(b)'s re-aiming of a tool, and the batch regenerates tool artifacts; the headings claimed more than the body.
  - **The premise ledger's NOT KNOWN item.** Former wording, kept (#12): *"so every red is traced to the one task that
    caused it."* Why: a capture after each task locates a new red; it does not by itself establish the cause (the
    dispatch's own clause on a handoff entry appearing during the run is a cause that is not a task).
  - **A5.** Former wording ended *"…, the rulings-sort surface and `cowork_away_returns.md`."* with no exception. Why:
    A4 allows artifacts 2(d) and 3(d) regenerate, unnamed; if one lay in a place A5 lists, Task 5's check *"every file
    A5 names absent"* would fail on an act A2 permits.
  - **4(a)'s keyword search.** Former wording ended *"report the hits as found."* Why: the expectation *"hits only inside
    the paraphrase paragraph"* was not run by the writing side, and the instruction to reword at new entries could not
    be met for a hit in an older entry.
  - **4(c)'s populations, and C4's sentence on them.** Former wordings, kept (#12): in 4(c), *"**the dispatch population
    gaining the stopped dispatch and this dispatch, the report population gaining the stopped report (its
    `the_appendix_beside_it` naming the stopped appendix), the handoff population gaining entries 570 onward, and every
    sum, mirror and share built over those populations.**"*; in C4, *"…, so the stopped pair counts only once landed — as
    written."* Why, read at the tool: `DISPATCH_PREFIX` is `cc_instruction_l3_comparison_tabulation_` and
    `REPORT_PREFIX` is `cc_report_l3_comparison_tabulation_` (lines 203, 205), so neither the stopped dispatch, this
    dispatch nor the stopped report can enter those populations; and the appendix pairs are taken from the report
    folder's listing with no add-commit test and no prefix (`pair_appendices`, lines 389–401; lines 713, 719–721), so a
    pair counts whether landed or not. The 4(c) expectation for the stopped pair, and 4(c′)'s for this batch's pair
    (written at 4(d), not committed until 4(f)), hold as written.
  - **C2's reading of `classify()`.** Former wordings, kept (#12): *"read `home_is_layer_spec`, `nonspec_kind`, `home`,
    `title` and `plain` only."* and *"neither field is read by the rule, so no `proposed_class` or `decided_by` can move
    from that commit."* Why: the function was read to its last branch's opening, not whole.
  - **C3's sentence on `gen_defense_share.py`.** Former wording, kept (#12): *"so only the whole-read denominator and
    the share against it can move."* Why: the tool was read at lines 15–30 and 120 only.
- **Not checked here:** the terms of `L3_KEYWORDS`; C1's reading of the two refusing tools (not redone, per handoff
  entry 579 §3 step 3).
- **The banner stays NOT YET RELEASED in this landing.** Setting it to RELEASED is the next act, landed and proved on
  its own. *(Done 2026-11-08 by the same sitting, in its next turn: the banner reads RELEASED.)*
