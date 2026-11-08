# CC dispatch — THE LANGUAGE-MODEL CORRECTION, SECOND RESUME: THREE GRADES ADDED TO THE SPECIFICATION-DOCUMENT-SET TOOL FOR THE §19 BANNER, THEN THE READING-FILE ANNOTATIONS, THE CLOSE AND THE END STATE — DOCUMENTATION AND RECORD-KEEPING ONLY; NO ALGORITHM CHANGE (2026-11-08)

> **STATUS: RELEASED 2026-11-08** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eighty_four.md`, after its check at its sources (recorded
> at the end of this file; two corrections, each with its former wording). Written 2026-11-08 by the sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eighty_two.md`. *(Former wording of the banner's opening,
> kept (#12): "**STATUS: WRITTEN 2026-11-08 — NOT YET RELEASED** by the Cowork sitting booted on [entry 582]. Its check
> at its sources runs in a turn of its own; this banner is set to RELEASED only after that check, which is recorded at the
> end of this file with every former wording. **Until then this dispatch is NOT handed to Claude Code.**")* Once released it is executed by Claude Code
> when the user hands it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear,
> stop at that step and report it. Do not continue to the next one.**
>
> **THE WRITING SIDE'S RESTRAINT, declared.** Once released this dispatch is final. The writing side will not touch it,
> nor any file it names, while this batch runs. The files the writing side writes after this dispatch lands and before
> hand-over are handoff entries numbered above 582, which is why Task 0 states no size for them. **Nothing this dispatch
> lands is in git yet**; Task 0 lands it.

## What this batch is, in plain words

On 2026-11-07 the user ruled that a language model is used only while the software is being developed, never at run time
in the finished product (`records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`, Ruling 1), and
ratified the corrections that follow as derivations (`records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`,
Ruling 1, items 1 to 7; item 7 is "no act now").

**Two batches have applied part of it, and both stopped.** You do not read either dispatch; what you need from them is
stated here.

- ***The first stopped batch*** ran under `records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md`. It
  applied items 1 and 2 (seven register entries made SUPERSEDED BY the 2026-11-07 ruling, two given a provenance note,
  the register regenerated) and stopped on the register data file's format.
- ***The resume batch*** ran under `records/cc/instructions/cc_instruction_llm_correction_resume_2026_11_07.md`. It
  landed its records (`d46a7b48…`), returned the data file to its standard form (`acbb2d7c…`), regenerated the artifacts
  that had gone red (`778c459b…`), and applied items 3 and 4 (`257ad5bf…`): a superseded banner over `ARCHITECTURE.md`
  §19 and over `docs/llm_integration.md`, and a note in the 2026-08-08 route record. **It stopped at the capture after
  that commit**, because `tools/audit/gen_specification_document_set.py` failed: the §19 banner (`ARCHITECTURE.md` line
  8089) names three documents that tool has no grade for, and the tool stops on any `.md` naming in `ARCHITECTURE.md`
  without one. That stop was correct; the gap was the writing side's, whose check had not found this tool. Its report
  and appendix were written and not committed. **Its Tasks 3, 4 and 5 did not run.**

**This batch finishes the work:**

- **Task 0** lands handoff entries 581 and 582 (and any later one), the resume batch's report and appendix, and this
  dispatch, and pushes.
- **Task 1** gives the three new namings their grades in the tool's `GRADES` table, regenerates the tool's artifact,
  then regenerates `tools/audit/period_stratum_split.json`, which records that artifact's SHA-256.
- **Task 2** (items 5 and 6): annotations in the three reading files. *(This was the resume batch's Task 3.)*
- **Task 3** is the close; **Task 4** the end state. *(These were the resume batch's Tasks 4 and 5.)*

**What the three grades are, and why they need no user decision.** The banner's wording is ruled (correction record
Ruling 1 item 3) and is not changed. The tool's own route for a new naming is a grade. The two ruling records are named
where a ruling was taken: the tool already grades that form `provenance-attribution` (its lines 429–432 and 506–508).
`docs/llm_triage_design.md` is named in a sentence of its own, *"The test-time second opinion that ruling allows is
discussed in X."*: `CLAUDE.md` rule (i) admits only an explicit delegation clause or a named home with sections, and the
tool already grades a pointer sentence of the form *"See X."* `bare-appended-citation` (its lines 554–556 and 557–559).
*(★ CORRECTED 2026-11-08 at this file's check, C5. Former wording, kept (#12): "`docs/llm_triage_design.md` is named by
*"is discussed in"*, appended to a sentence: … and the tool already grades *"see X"* appended to a sentence
`bare-appended-citation` (its lines 522–525 and 551–553)." The banner's sentence is not appended to another sentence.)*
All three are excluded forms, so **the specification document
set gains no member** — consistent with correction Ruling 1 item 7 (*"No act now on … the document's membership of the
specification document set"*). This follows from D-599 (the standing principles first; a user choice only where they
do not decide), so it is recorded as a derivation, not a choice (handoff entries 581 §2 item 3 and 582 §2 item 4).

**★ ONE RULE FOR EVERY TEXT EDIT OF TASK 2: NO LINE IS ADDED OR REMOVED.** Every annotation is inserted inside one named
line, so no line number cited in the reading files moves. Each such edit is proved by `--numstat` showing the same number
of lines added as removed, and by the file's line count being unchanged. **Task 1's edit of the tool is not a text edit
of a cited document and adds fifteen lines** (premise ledger).

**Documentation and algorithm, separated.** **Documentation only:** everything this batch edits. Task 1's edit adds
three grades to a check tool's authored table and changes no specification; 3(b)'s re-aiming of the forward-bound tool
changes that record-keeping tool's constants. **Algorithm: NOTHING changes.** No specification of the analysis is
changed in substance; the edited texts describe a language-model product tool, which is not the analysis. The method that
stands is the one the scope document (`ratification_surfaces/cowork_llm_correction_scope_2026_11_07.md`) §5 states.
**This batch decides nothing.**

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
3. **The highest-numbered handoff entry on disk, whole** (582, or a higher one if it exists); it is the current handover
   block.
4. `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md` whole (5,001 bytes) — the ruling this
   batch applies.
5. `tools/audit/gen_specification_document_set.py` lines 153–164 (the `g()` helper and the opening of `GRADES`), 388 (the
   `EXCLUDED` divider), 422–432, 502–525 and 551–572 (the precedents and the table's last entries), and 786–807 (the scan
   and its two STOPs).
6. `tools/audit/gen_l3_outgoing_population.py` at its `L3_KEYWORDS` list, located by search (for 3(a)'s search).

**Not read, and not needed:** the first stopped dispatch and the resume dispatch; any earlier report, the resume batch's
report and appendix included (Task 0 lands them; this dispatch states what it takes from them); the scope document; the
reading files beyond the lines Task 2 names; `FRAMEWORK.md`. Declare any further read you make.

---

## ★ WORDS USED IN THIS DISPATCH, EXPLAINED FIRST

- ***The start tip*** — `257ad5bfc1915f63c1e0b7e54da5692e6003e64b`, the commit both ref files named when this dispatch was
  written: the resume batch's Task 2 commit.
- ***The resume batch's chain*** — `4461d865fcb2c99ef20099487c0d4a4221456112` (the first stopped batch's register
  commit) → `d46a7b4861ef2990c825d71c808107dc30c2a447` (resume Task 0) → `acbb2d7cca503db43530a525072e3584e4d0bf4c`
  (resume Task 1) → `778c459bd722a8e06b3afdb26e00b97889e51759` (resume regeneration) → the start tip (resume Task 2).
- ***The records landing*** — the batch run under `records/cc/instructions/cc_instruction_records_landing_2026_11_07.md`.
  Its two `STATUS.md` entries are still the latest in that file (neither stopped batch wrote one). Named only so the
  forward bound (3(b)) can move them; **you do not read it.**
- ***The test-only ruling*** — Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`.
- ***The correction record*** — `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`.
- ***The set tool*** — `tools/audit/gen_specification_document_set.py`. ***The set artifact*** —
  `tools/audit/specification_document_set.json`, which the set tool writes (its line 111).
- ***The split tool*** — `tools/audit/gen_period_stratum_split.py`. ***The split artifact*** —
  `tools/audit/period_stratum_split.json`, which the split tool writes (its line 73).
- ***The banner*** — `ARCHITECTURE.md` line 8089, the superseded banner the resume batch put over §19.
- ***The edited set*** — the files Tasks 1 and 2 edit by hand: the set tool; `ratification_surfaces/cowork_comparison_l2_reading.md`,
  `ratification_surfaces/cowork_comparison_l0_l1_reading.md`, `ratification_surfaces/cowork_comparison_l3_reading.md`.
  The set artifact and the split artifact are regenerated, not hand-edited.
- ***`<T0>`, `<T1>`, `<T2>`, `<T3>`*** — this batch's task commits (not the resume batch's). ***`<ACT_DATE>`*** — the day
  the step runs, written `YYYY-MM-DD`.
- ***A capture*** — the output of `python tools/audit/gen_guard_state.py --check`, saved whole to a scratch file outside
  the repository and read. ***Compared verdict by verdict*** means every tool's PASS / FAIL / NOT RUN / HISTORICAL line
  side by side, and the tally line.
- ***Red by this batch*** — a tool that passed at the capture before a task and fails at the capture after it, whose
  printed cause names, or whose inputs (read at the tool's source) include, a file the task changed — a file of the
  edited set or an artifact the task regenerated.
- ***Blob form*** — a `--numstat` or diff taken between two explicit blob hashes (`git diff --numstat <blob> <blob>`), as
  the earlier batches did when the shell-read guard refused a working-tree `git diff`. Use it wherever this dispatch names
  a `--numstat` or a diff.

---

## Ruling ledger

- **The correction record, Ruling 1 items 1 to 6** — items 1 to 4 are applied at the start tip; this batch applies items
  5 and 6. Item 7 (no act now) is not applied.
- **The test-only ruling and its Ruling 2** — the ground the correction record rests on.
- **D-599** (LIVE): the standing principles first; a user choice only where they do not decide. The ground for Task 1's
  grades being derivations.
- **`CLAUDE.md` rule (i)** (the grade classes) and the set tool's own precedents — the ground for the three grades.
- **The user's ruling of 2026-11-07 on the three standing modifications** (handoff entry 571 §2 item 1): *"Leave them -
  we will revisit this when we look at the externally compiled list of relevant research/software/algorithms. Then we
  can consolidate and fix whatever is needed."* — the ground for A1.
- **Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md`** — the dispatch form: no chain
  of earlier dispatches; what is needed from one is stated here.
- **Ruling 4 of the 2026-11-01 pruning record** — the report's two-file form (3(d)).
- **No new rule is made.** The amendment of the no-tool-edit rule below is to this side's own dispatch rule, not a
  ruling.

---

## Premise ledger (written 2026-11-08 by the writing side from staged working-tree copies read with the file tools; no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
  `257ad5bfc1915f63c1e0b7e54da5692e6003e64b`.
- **FACT — the chain**, read at `.git/logs/HEAD` lines 2111–2114: each of the five commits of *the resume batch's chain*
  names the one before it as its predecessor there. That `4461d865…`'s parent is `566d37e583da3ee23d2d46957ead8eb202290973`
  is relayed (handoff entry 576 §1).
- **FACT — `STATUS.md`** (10,680 bytes, read whole): the records landing's TWO entries at lines 8 and 10 — its close
  entry carrying `Last updated: `, then its Task 0 `Same dispatch` entry; the two 2026-09-02 entries at 12 and 14; the
  archive-pointer paragraphs at 16, 18, 20 and 22, the one at 18 being the standing paragraph that holds the word
  *paraphrase* (called ***the paraphrase paragraph*** below). Exactly one line carries `Last updated: `. **No entry for
  either stopped batch.**
- **FACT — the banner**, `ARCHITECTURE.md` line 8089, read whole. It names, in this order,
  `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` (where the ruling was taken),
  `docs/llm_triage_design.md` (in *"The test-time second opinion that ruling allows is discussed in
  `docs/llm_triage_design.md`."*) and `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md` (in
  *"Applied under Ruling 1 item 3 of …"*). Line 8088 is the §19 heading; line 8090 the *Full design document* line.
- **FACT — the set tool**, read at the lines named in the first read, item 5:
  - Usage (lines 92–93): the bare invocation writes the artifact; `--check` re-derives and exits 1 on drift.
  - `NAME_RE` (line 722) is `[A-Za-z0-9_./-]+\.md\b`, so a naming's key is its whole path as written.
  - The scan (lines 790–807) takes every `.md` naming in `ARCHITECTURE.md` but `ARCHITECTURE.md` itself, and STOPs on a
    scanned target with no authored grade, and on an authored grade the scan does not find.
  - `GRADES` opens at line 164; the `EXCLUDED` divider is line 388; the table closes with `}` at line 572, after the
    entry for `docs/chordlist_bug_report.md`, whose last line (571) is
    `        "Named once, in the same version-history paragraph."),` — **that text occurs once in the file** (one search).
  - The grade classes are constants (lines 119–123): `BARE_CITATION`, `PROVENANCE` and the rest. For an excluded grade
    no anchor is authored (the comment at lines 153–158).
  - None of the three banner paths has a grade (one search of the tool for `llm_`: hits only at lines 348, 355, 708 and
    709, all for `docs/llm_integration.md`).
- **RELAYED — each of the three targets is named once in `ARCHITECTURE.md`, on line 8089** (handoff entry 582 §2 item 4,
  checked there).
- **RELAYED — the set artifact's expected change** (handoff entry 582 §2 item 3, checked there against the committed
  artifact's `counted` block, its lines 57–97): `targets_named_in_ARCHITECTURE.md` 68 → 71; `namings_scanned` 199 → 202;
  `bare-appended-citation` 17 → 18; `provenance-attribution` 21 → 23; `targets_ADMITTED` 25, `members_total` 26 and every
  member count unchanged. The banner replaced a blank line, so no other naming's line number moves; no grade or property
  anchor in the tool matches the banner's text (lines 166–386 and 617–718), and the `docs/llm_integration.md` governing
  anchor is at line 8096 with two lines of context above it, outside 8089.
- **FACT — the split tool**: usage at lines 54–55 (bare writes; `--check` exits 1 on drift); it reads the set artifact
  (`IN_DOCSET`, line 136) and writes that file's SHA-256 into its own artifact at `the_document_set` → `sha256` (lines
  408–409). **RELAYED** (handoff entry 582 §2 item 2): its `--check` compares the whole rendered text (lines 597–605); its
  reader `gen_july_screen.py` takes the population lists, not the hash; `gen_l0_l1_outgoing_population.py`,
  `gen_l2_outgoing_population.py` and `gen_l3_outgoing_population.py` read the set artifact's member paths only, which
  do not change. **So the split tool, PASS at the start tip, goes red when the set artifact is regenerated, and its
  regeneration should change exactly the one `sha256` line.**
- **RELAYED — the guard state** (handoff entry 582 §2 item 1, read there at the resume batch's appendix):
  - **The fourteen**, failing at the capture after the resume regeneration commit: `gen_phase3_gate_partition.py`,
    `gen_filing_convention_application.py`, `gen_artifact_inventory.py`, `gen_artifact_inventory_surface.py`,
    `gen_test_construction_evidence.py`, `gen_retirement_caller_check.py`, `gen_per_session_reading.py`,
    `gen_epoch_write_path.py`, `gen_recognizer_establishment_sort.py` (each under `tools/audit/`), and
    `apply_soft_discard.py`, `apply_residue_discard.py`, `gen_cluster_dispositions.py --verify`,
    `gen_home_classification.py`, `gen_phase1p_delegation_bar.py` (each under `tools/audit/decisions/`). They are the
    thirteen standing reds and `gen_per_session_reading.py`.
  - **The fifteen**, failing at the capture after the start tip: the fourteen and `gen_specification_document_set.py`.
  - `tools/audit/guard_state.json` at the start tip is the one the records landing committed (no batch since reached its
    end state). **Read it at 0(f) yourself; the object is the value of record.**
  - The classification `--check` STOP (exit 2) named five tools at the first stopped batch's run:
    `gen_l0_l1_outgoing_population.py`, `gen_l2_withheld_documents.py`, `gen_l3_outgoing_population.py`,
    `gen_per_session_reading.py`, `gen_withheld_family_reading.py` [relayed from the resume dispatch's ledger].
- **FACT — the reading-file lines** (carried from the resume dispatch's ledger, where each was found by one exact-text
  search, one hit each, at `4461d865…`; no batch since edited a reading file):
  - L2 (`ratification_surfaces/cowork_comparison_l2_reading.md`): line 72468 holds
    `and its future as a plugin. **The placement readings are those of the earlier`; line 72557 holds
    `what the language-model integration is shown.` — item 1 of the list headed `#### Not a statement — listed so the
    arithmetic closes (34)`.
  - L0/L1 (`ratification_surfaces/cowork_comparison_l0_l1_reading.md`): line 10142 holds
    `> **What it is.** The design of a natural-language interface to the score`.
  - L3 (`ratification_surfaces/cowork_comparison_l3_reading.md`): line 30466 holds
    `— the defense of keeping the fields of Row 21.102.`
- **FACT — the landing files' sizes at the writing side's listing:** entry 581 8,243 bytes; entry 582 9,044;
  `records/cc/reports/cc_report_llm_correction_resume_2026_11_07.md` 17,255; its appendix
  `records/cc/reports/cc_report_llm_correction_resume_2026_11_07_appendix.md` 82,972.
- **NOT KNOWN — which guard tools read the set tool's source, the set artifact or the split artifact** beyond those
  named above. A2 gives a rule, with a capture after each task, so a new red is located between two captures, and A2's
  rule then tests whether the task between them caused it.
- **ASSUMPTION A1 — the working tree, stated by CONTENT.** Tracked modifications at your boot: **exactly three** —
  `tools/audit/claude_md_finer_archive.json` (standing, carried), `docs/research_papers/BIBLIOGRAPHY.md` and
  `docs/research_papers/README.md`; and untracked, beside them, `docs/research_papers/polyph9-release/`. **The last three
  were made by another tool, unintentionally, and the user ruled them left as they are** (the ruling ledger). Also
  untracked: `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx`. **You do not touch, restore, land or delete
  any of these five, and their presence is not a STOP.** If one is absent, report it; that is not a STOP. **The writing
  side wrote no tracked file.** Untracked and landed by Task 0: the landing set. Beyond it, only the standing untracked
  population, which is not landed and is not a STOP. **Your enumeration with `tools/audit/changed_paths.py` establishes
  A1.**
- **ASSUMPTION A2 — the reds.**
  - **At your boot, before Task 0:** `gen_per_session_reading.py --check` may STOP (exit 2; untracked handoff entries) or
    FAIL. Report what it printed; neither is a STOP. Do not run the full guard set before Task 0.
  - **The opening capture (0(f), after `<T0>`):** run 83; zero STOPs in the runner; **failing exactly the fifteen**, and
    nothing else.
  - **The captures after `<T1>` and `<T2>` (1(e), 2(d)):** each compared verdict by verdict with the one before. **A tool
    newly FAIL must be *red by this batch*** (the words above): you report its printed cause and the line of its source
    that reads the changed file, quoted. **Then exactly one of:**
    - **(regenerate)** the tool writes a derived artifact (it has a write mode) and its `--check` compares that artifact
      to what the inputs now give: run the bare write mode, then `--check` green, and diff the artifact against its blob
      before the task in blob form. **Every changed passage must be tied to an edit of that task**: a change only in (i)
      a whole-file size, line count or hash of a file the task changed; (ii) a term-search hit, or a count of hits, that
      changes only because an edited line gained or lost the term; or (iii) at Task 1 only, a passage that publishes one
      of the three new grades or the banner's namings of the three targets, and a count by grade or naming that they
      move. Quote each changed passage in the report, tie it to the edit by name, commit the regenerated artifact as the
      task says, and continue. **A member of any population, list or set entering or leaving, or any other changed
      passage, not so tied, is a STOP-and-report** (the task's commit stays; nothing further runs).
    - **(carry)** the tool compares the file to a fixed value recorded at an earlier act (a hash, a pinned size, a frozen
      copy): **do not regenerate and do not re-pin.** Record it as red by this batch, with its message, and continue.
      Its re-pinning is a question for the writing side, which the report names.
    - **Neither, or unsure:** STOP-and-report.
  - **A newly FAIL tool that is NOT red by this batch is a STOP-and-report.** A tool newly PASS is reported and is not a
    STOP.
  - **Reds named in advance:**
    - **In Task 1, before 1(e):** the split tool goes red when the set artifact is regenerated; 1(c) regenerates it, with
      its own expectation. At 1(e) the set tool is expected FAIL → PASS and the split tool PASS at both captures.
    - **At 2(d), possibly:** `tools/audit/gen_l2_outgoing_population.py` records whole-file byte sizes of the documents
      it names (its line 380), and it and `tools/audit/gen_l3_outgoing_population.py` read the transfer-list section
      (`## 10.`) of the L0/L1 and L2 reading files (`gen_l2_outgoing_population.py` lines 128 and 556;
      `gen_l3_outgoing_population.py` lines 187–194) [relayed from the resume dispatch's ledger]. A size or hit change at
      an edited line is the tied case; anything else is a STOP-and-report.
    - **Already failing, so not "newly FAIL":** the fourteen. Report any change in what they print; it is not a STOP.
    - **Not observable:** `tools/audit/decisions/gen_r1_superseded_reach.py` is HISTORICAL in the runner. Do not run it.
  - **Task 3:** `gen_session_start_read_size.py` and `gen_defense_share.py` expected RED after 3(a) (both read
    `STATUS.md`); `gen_l3_outgoing_population.py --check` and `gen_l0_l1_outgoing_population.py --check` may be red after
    3(a)/3(b) (they carry a `STATUS.md` residue record with line values); `gen_per_session_reading.py` regenerated LAST
    and again at 3(c′).
- **ASSUMPTION A3** — no `src/` file, build, test, golden, corpus of scores or measurement of the analysis is touched.
- **ASSUMPTION A4 — THE FOOTPRINT.** **Task 0:** the landing set. **Task 1:** the set tool (its `GRADES` table only), the
  set artifact, the split artifact, and any artifact 1(e) regenerates under A2. **Task 2:** the three reading files, and
  any artifact 2(d) regenerates. **Task 3:** `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py` at
  its authored aiming and head comments, `tools/audit/status_batch_bound.json`, the artifacts 3(c) and 3(c′) regenerate,
  the report and its appendix, `records/cowork/handoff/cowork_away_returns.md`. **Task 4:**
  `tools/audit/guard_state.json` and the away-returns end-state portion.
- **ASSUMPTION A5 — byte-unchanged by this batch:** `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS.md`,
  `DECISIONS_ARCHIVE.md`, `cowork_audit_protocol.md`, `FRAMEWORK.md`, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`,
  `ARCHITECTURE.md`; every file under `decisions/` and under `docs/` (the A1 modifications stay as they are, unstaged);
  every tool under `tools/audit/` but the set tool and `gen_status_batch_bound.py`; every file under
  `tools/audit/decisions/`; every ruling record; every handoff entry, ratification document, dispatch and report already
  tracked, but the three reading files and `cowork_away_returns.md`. **Excepted from this list: any artifact 1(e) or
  2(d) regenerates under A2, named in the report.**

## The declared start state — at the tree you will meet

1. Both ref files at the start tip; A1's five standing items; the landing set untracked; nothing running.
2. The fifteen failing; the classification's five-name STOP.

**A further untracked handoff entry appearing during the run** (the writing side's, after this dispatch is handed over):
do not land it; if it makes `gen_per_session_reading.py` STOP at 3(c), do not regenerate that artifact, report the STOP
with its message, and carry the tool as red into the end state.

## Findings in this batch

**No finding number is allocated.** A finding met during the run is written up on its own in the report and surfaced,
never absorbed.

---

## Task 0 — land the records, and PUSH

- **0(a) — the pin.** `git hash-object -w --no-filters` of this dispatch, in its own call; record its blob and
  `git cat-file -s`; re-hash immediately before staging, equal or STOP.
- **0(b) — the refs and the chain.** Read both ref files with the file tools against the FACT; then `git cat-file -p` of
  each of `257ad5bfc1915f63c1e0b7e54da5692e6003e64b`, `778c459bd722a8e06b3afdb26e00b97889e51759`,
  `acbb2d7cca503db43530a525072e3584e4d0bf4c` and `d46a7b4861ef2990c825d71c808107dc30c2a447`, each hash written literally
  in its own command, each expected to name the next in *the resume batch's chain* as its parent (the last expected
  parent `4461d865fcb2c99ef20099487c0d4a4221456112`). A different chain is a STOP-and-report with nothing committed.
- **0(c) — A1 and the landing set**, by `python tools/audit/changed_paths.py` (the sanctioned enumeration; `git status`
  is not used, D-253): exactly A1's three tracked modifications; **every path of the landing set untracked, and every
  untracked path under `records/cowork/handoff/`, `records/cowork/rulings/`, `ratification_surfaces/`,
  `records/cc/instructions/` and `records/cc/reports/` a path of the landing set**; other untracked paths only the
  standing population and A1's two untracked items. A path of the landing set missing, or an untracked path in those
  five folders outside it, is reported and is a STOP. **The landing set:**
  - **(i) handoff entries** — `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eighty_one.md`,
    `…_five_hundred_and_eighty_two.md`, and **every untracked handoff entry numbered above 582 at your boot**.
  - **(ii) the resume batch's report and appendix** — `records/cc/reports/cc_report_llm_correction_resume_2026_11_07.md`
    and `records/cc/reports/cc_report_llm_correction_resume_2026_11_07_appendix.md`, as they stand. **Do not edit them.**
  - **(iii) this dispatch** — `records/cc/instructions/cc_instruction_llm_correction_second_resume_2026_11_08.md`.
- **0(d) — last bytes** of each landing file, at its blob written `--no-filters`, by one scratch script quoted whole in
  the appendix: each object's size, its last 70 bytes and its count of zero bytes. Each must end with a newline after a
  complete line and hold no zero byte; a final line broken off mid-word, or a zero byte, is a STOP-and-report naming the
  file. **Expected sizes:** the four of the premise ledger. **No size is stated for this dispatch or any entry above
  582**; report every size in the appendix.
- **0(e) — the commit**, exactly the landing set and no other path, staged by explicit path, the staged set proved with
  `python tools/audit/changed_paths.py --staged`: **its count must equal the landing set's count.** Subject, exactly:
  `record: handoff entries 581 to <N>, the resume batch's report, with the second resume dispatch`, `<N>` the highest
  entry landed written as a number. Push; read `.git/refs/remotes/origin/master` and verify it equals the new tip. **This
  commit is `<T0>`.**
- **0(f) — the opening capture.** A capture, saved whole and read. Read the start tip's `tools/audit/guard_state.json` →
  `summary` at the object (`git show 257ad5bfc1915f63c1e0b7e54da5692e6003e64b:tools/audit/guard_state.json`) and report
  its run, counts and failing set by name. Then `python tools/audit/gen_guard_classification.py --check`, expected exit 2,
  a STOP naming the five tools of the premise ledger — report them by name; a different set is a STOP-and-report. **The
  failing set must be the fifteen of A2.** Anything else is reported and is a STOP.

**E0:** the landing set in one commit, pushed; the pin proved; A1 reported with its enumeration; the opening capture as
A2 states it; the five-name STOP.

---

## Task 1 — the three grades; the set artifact and the split artifact regenerated

**★ THE NO-TOOL-EDIT RULE, AMENDED FOR THE SET TOOL'S `GRADES` TABLE ONLY.** No tool is edited or added in this batch
but the forward-bound tool's re-aiming (3(b)) and **the three entries 1(a) adds to the set tool's `GRADES` table**; no
other line of the set tool changes. *(★ AMENDED 2026-11-08 for the `GRADES` table only, by the writing side, whose own
rule it was. The resume dispatch's wording, kept (#12): "**No tool edited or added** but the forward-bound tool's
re-aiming. No guard enrolment changes; no classification verdict is authored; **no pinned value is re-pinned.**" Why the
amendment needs no user decision: the table is the set tool's authored input, its own header names a later naming
without a grade as a STOP to be met by grading it, and the three grades are derivations — the plain-words section above.
The rest of that rule stands: no guard enrolment changes; no classification verdict is authored; no pinned value is
re-pinned.)*

**1(a) — the edit**, with the file-editing tool, in the set tool. The `old_string` occurs exactly once (premise ledger),
else STOP-and-report. `old_string` (two lines: line 571, then line 572):

```
        "Named once, in the same version-history paragraph."),
}
```

`new_string` (the same two lines, with fifteen lines between them; each line indented exactly as shown — four spaces
before a comment or a key, eight before a constant or a string):

```
        "Named once, in the same version-history paragraph."),
    # ── EXCLUDED, added 2026-11-08 for the §19 superseded banner (`ARCHITECTURE.md` line 8089) ──
    "records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md": g(
        PROVENANCE,
        "Named once, in the §19 superseded banner, recording where the user's ruling that "
        "supersedes the section was taken — a ruling record named where a ruling was taken, as "
        "for the 2026-08-11 fourteenth-stop and the 2026-08-09 second-stop records above."),
    "records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md": g(
        PROVENANCE,
        "Named once, in the same banner, recording under which ruling the banner was applied — "
        "a ruling record named where a ruling was taken."),
    "docs/llm_triage_design.md": g(
        BARE_CITATION,
        "Named once, in the same banner, in a sentence of its own about the test-time second "
        "opinion: '… is discussed in X.' It is neither an explicit delegation clause nor a named "
        "home with sections (`CLAUDE.md` rule (i)); the same grade as the 'See X.' namings above."),
}
```

*(★ CORRECTED 2026-11-08 at this file's check, C2 and C5: the third entry's three `why` lines. Former wording, kept
(#12): `"Named once, in the same banner, 'is discussed in X' appended to a sentence about the "` /
`"test-time second opinion. It is neither an explicit delegation clause nor a named home "` /
`"with sections (`CLAUDE.md` rule (i)); graded as 'see X' appended to a sentence is above."),`. The sentence is not
appended, and the last clause did not parse. The entry is still three string lines, so the fifteen-line count and the
line numbers in 1(a)'s proof are unchanged.)*

**Proof of 1(a):** the tool's line count before and after, higher by exactly 15; `--numstat` in blob form, **`15	0`**;
the fifteen new lines read back at lines 572–586 and the closing `}` at line 587, with the file tools. Then `python -c
"import ast,sys; ast.parse(open('tools/audit/gen_specification_document_set.py',encoding='utf-8').read())"` exits 0.

**1(b) — the set artifact.** `python tools/audit/gen_specification_document_set.py --check` first, in its own call
(expected exit 1 or a STOP no longer naming the three targets; report what it printed). Then the bare write mode, then
`--check` again, **exit 0**. Diff the set artifact against its blob at the start tip, in blob form, by a scratch script
quoted whole in the appendix. **Expected:** the three targets enter with their grades and the banner's namings of them
(line 8089) published — in the tool's graded list (sorted by target), one record per target carrying `target`, `form`,
`admitted` false, `why_this_grade` (the `why` text of 1(a), verbatim), `decided_by` `rule_(i)_not_admitted`,
`namings_in_ARCHITECTURE.md` (one entry: `line` 8089 and `line_text`, the whole banner line stripped) and
`namings_counted` 1 (the set tool's lines 822–831 at the start tip); the `counted` block moves exactly as the premise ledger's RELAYED expectation says
(`targets_named_in_ARCHITECTURE.md` 68 → 71, `namings_scanned` 199 → 202, `bare-appended-citation` 17 → 18,
`provenance-attribution` 21 → 23); `targets_ADMITTED` 25, `members_total` 26 and every member count unchanged; **no
member enters or leaves**. Every changed passage is quoted in the appendix and tied in the report. **A member entering
or leaving, a count other than those four moving, or any other changed passage is a STOP-and-report**, with nothing
committed.

**1(c) — the split artifact.** `python tools/audit/gen_period_stratum_split.py --check` in its own call, **expected exit
1** (the set artifact's hash moved). Then the bare write mode, then `--check` again, **exit 0**. Diff the split artifact
against its blob at the start tip in blob form. **Expected: exactly one changed line, the `sha256` value under
`the_document_set`**, its new value equal to the SHA-256 of the set artifact 1(b) wrote (compute it with
`python -c "import hashlib;print(hashlib.sha256(open('tools/audit/specification_document_set.json','rb').read()).hexdigest())"`
and report both). If `--check` exits 0 before regeneration, report it and do not regenerate; that is not a STOP. Any
other changed passage is a STOP-and-report, with nothing committed.

**1(d) — the commit**, exactly the set tool, the set artifact and the split artifact, by explicit path, the staged set
proved (count 3). Subject: `tools: three grades for the §19 superseded banner's namings; the set and split artifacts
regenerated`. Push; verify `origin/master`. **This commit is `<T1>`.**

**1(e) — the capture after `<T1>`**, compared verdict by verdict with 0(f). **Expected: failing exactly the fourteen**;
the set tool FAIL → PASS; the split tool PASS at both; no other verdict differs. A newly FAIL tool goes through A2's
rule; if A2's rule regenerates anything, commit it by explicit path, the staged set proved, with the subject
`artifacts: regenerated after the three grades`, push and verify.

**E1:** three grades, no member moved, both artifacts regenerated and green, `<T1>` pushed; the capture as expected.

---

## Task 2 — the reading files annotated (Ruling 1 items 5 and 6)

**Each annotation is inserted inside an existing line; no line is added.** With the file-editing tool; the `old_string`
occurs exactly once, else STOP-and-report. **The reading files are about 1 to 5 MB each: locate each `old_string` with
one search for that exact text, never with a pattern that matches many rows, and read only the matched line.** In every
`new_string` below, **replace `<ACT_DATE>` with the day the edit runs**, written `YYYY-MM-DD`; nothing else is changed.

**2(a) — the L2 reading file**, `ratification_surfaces/cowork_comparison_l2_reading.md` (item 5), two edits.

*First,* the member's description (line 72468). `old_string`:

```
and its future as a plugin. **The placement readings are those of the earlier
```

`new_string`:

```
and its future as a plugin. [★ ANNOTATED <ACT_DATE> under Ruling 1 item 5 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`, this member's wording kept (#12): its description of the language-model integration as *a product tool outside the analysis* is stale. Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` rules that a language model is never used at run time in the finished product; the integration is superseded, and a language model may only give a second opinion when the product is tested and struggles with inference. The dispositions are not changed.] **The placement readings are those of the earlier
```

*Second,* item 1 of the list *Not a statement — listed so the arithmetic closes (34)* (line 72557). `old_string`:

```
what the language-model integration is shown.
```

`new_string`:

```
what the language-model integration is shown. [★ ANNOTATED <ACT_DATE> under Ruling 1 item 5 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`, for items 1 to 34 of this list, their wording kept (#12): *a product tool outside the analysis* is stale for the language-model integration, which Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` supersedes. The dispositions are not changed.]
```

**2(b) — the L0/L1 reading file**, `ratification_surfaces/cowork_comparison_l0_l1_reading.md` (item 5), the manifest
description (line 10142). `old_string`:

```
> **What it is.** The design of a natural-language interface to the score
```

`new_string`:

```
> **What it is.** [★ ANNOTATED <ACT_DATE> under Ruling 1 item 5 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`, this description's wording kept (#12): the document describes a language model at run time in the finished product, which Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` rules out; the document is superseded. The dispositions are not changed.] The design of a natural-language interface to the score
```

**2(c) — the L3 reading file**, `ratification_surfaces/cowork_comparison_l3_reading.md` (item 6), the end of item 21
(line 30466). `old_string`:

```
— the defense of keeping the fields of Row 21.102.
```

`new_string`:

```
— the defense of keeping the fields of Row 21.102. [★ ANNOTATED <ACT_DATE> under Ruling 1 item 6 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`, the wording kept (#12): the language-model half of this defense no longer holds, because Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` supersedes `docs/llm_integration.md`. The other half, the Authoritative Chord Symbol Mode (§4.1f), stands. Row 21.102's proposed QUARANTINED is not changed.]
```

**Proof of 2(a) to 2(c):** each file's line count before and after, equal; `--numstat`: **L2 `2	2`, L0/L1 `1	1`, L3
`1	1`**; each changed line read back by its line number (72468, 72557, 10142, 30466) with the file tools. A changed line
at any other number is a STOP-and-report. Then the commit, exactly the three files, by explicit path, proved (count 3).
Subject: `records: the reading files' language-model descriptions annotated under the 2026-11-07 correction`. Push;
verify `origin/master`. **This commit is `<T2>`.**

**2(d) — the capture after `<T2>`**, compared verdict by verdict with 1(e), under A2's rule; any regeneration committed
by explicit path, proved, subject `artifacts: regenerated after the reading-file annotations`, pushed and verified.

**E2:** four in-line annotations, no line added, `<T2>` pushed; every new red traced to Task 2 and handled by A2's rule.

---

## Task 3 — the close (written out in full; no earlier dispatch is read)

**3(a) — the `STATUS.md` entries FIRST**, at the top, above the records landing's close entry: one pointer entry per
committed task of this batch — **the close entry first**, naming this dispatch by its file name
(`records/cc/instructions/cc_instruction_llm_correction_second_resume_2026_11_08.md`) and carrying the `Last updated: `
prefix; then the entries of Tasks 2, 1 and 0 below it, in that order, each opening `Same dispatch`; in the OI-222 pointer
convention, the whole of each being your report; no value restated (D-431); each entry a separate paragraph, separated
by one blank line, in the shape of the entries at lines 8 and 10. **★ THE PREFIX IS MOVED, NOT COPIED, AND THE MOVE IS
COMPLETE BEFORE 3(b) RUNS:** in the same act remove `Last updated: ` — and nothing else — from the records landing's
close entry (now below your new entries); read `STATUS.md` after the edit and confirm exactly one line carries
`Last updated: `. **The close entry says in plain words:** that this batch finished the application of Ruling 1 items 1
to 6 of the 2026-11-07 correction record, begun by the batch under
`records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md` (items 1 and 2, stopped on the data file's format)
and continued by the batch under `records/cc/instructions/cc_instruction_llm_correction_resume_2026_11_07.md` (the data
file's standard form, items 3 and 4, stopped at the specification-document-set check), neither of which wrote a
`STATUS.md` entry; that this batch graded the §19 banner's three namings as excluded forms (no member of the
specification document set moved) and annotated the three reading files — every text kept; **no tool edited or added
but the set tool's `GRADES` table and the forward-bound tool's re-aiming; no algorithm change; no new decisions-register
entry, no `D-NNN`, no open-items row**; and that the whole is the report. **Then the search:** case-insensitive, every
term of `L3_KEYWORDS` (read 6 of the first read) plus *repeat* and *tie*, each as a substring, over `STATUS.md` —
**expected: hits only inside the paraphrase paragraph**; any other hit in your own new entries is reworded there and the
search re-run; report the hits as found. **This expectation is carried from earlier dispatches; the writing side did
not run the search at `STATUS.md`. A hit in an entry you did not write is reported and not reworded, and it is not a
STOP.**

**3(b) — the forward bound.** Read `tools/audit/gen_status_batch_bound.py` at the object
`257ad5bfc1915f63c1e0b7e54da5692e6003e64b:tools/audit/gen_status_batch_bound.py` first (a scratch file, searched for its
constants) and **report its authored constants as you find them**. **Expected, RELAYED** (not read at the tool by the
writing side; no batch since the records landing reached its close): `BASE_COMMIT`
`113b2ce680e527e81342d8f79d5acbad281334d7`, `PREVIOUS_BATCH_DISPATCH` `cc_instruction_boot_chain_landing_2026_11_02.md`,
`DISPATCH` `cc_instruction_records_landing_2026_11_07.md`, `TASK` `Task 3`, `MOVE_KIND` `ordinary`, `ACT_DATE`
2026-11-07. A difference is reported and 3(b) proceeds from what the object holds. **Re-aim all of them:**
- `BASE_COMMIT` — this batch's last task commit before the close: `<T2>`, or the last regeneration commit after it if
  2(d) made one. **Check that the `STATUS.md` blob at `BASE_COMMIT` equals its blob at the start tip, each `git rev-parse`
  in its own command.**
- `PREVIOUS_BATCH_DISPATCH` — `cc_instruction_records_landing_2026_11_07.md` (neither stopped batch wrote a `STATUS.md`
  entry, so the records landing's entries are the ones that move).
- `DISPATCH` — `cc_instruction_llm_correction_second_resume_2026_11_08.md`. `TASK` — `Task 3`. `MOVE_KIND` stays
  `ordinary`. `ACT_DATE` — the day the move runs.
- Append this batch's aiming to `PREVIOUS_AIMINGS` in the shape of the rows above it (the records landing's aiming is
  already its last row — do not append it twice); amend the head comments as the previous batches did, each former value
  named, not deleted (#12).

**Then `--apply` and `--check`, each in its own call.** **Prediction: exactly the records landing's TWO entries move** —
its close entry (from which 3(a) removed the prefix) and its Task 0 `Same dispatch` entry, at the base's lines 8 and 10;
the two 2026-09-02 entries stay; no STOP. Name the entries that moved, read at the artifact's `the_moved`. **If the tool
STOPs:** establish its cause first (D-669); if the cause is 3(a)'s prefix move incomplete, complete it, re-run the search
and the tool, and declare it; for any other cause, restore the tool's passing aim, re-run it green, report the STOP with
its message, and move nothing by hand. **No correction line is inserted in `STATUS_ARCHIVE.md`.** After the move, the
four checks that read the archive, each in its own call, each exit 0 expected, each output kept: `python
tools/audit/gen_status_batch_bound.py --check`, `python tools/audit/gen_governing_surface_split.py --check --pair
STATUS.md`, `python tools/audit/gen_status_residue_move.py --check`, `python tools/audit/gen_status_archive_pass.py
--check`.

**3(c) — the regenerations**, each check first in its own call, then each red one regenerated (write mode, the bare
invocation) and checked again, all exit 0:
1. `gen_session_start_read_size.py` and `gen_defense_share.py` — expected RED (the `STATUS.md` member), regenerated.
2. `gen_l3_outgoing_population.py --check` and `gen_l0_l1_outgoing_population.py --check` — each regenerated only if
   red; **if regenerated, only line values inside its `STATUS.md` residue record may move.** A member of either
   population, or of `the_tabulation_population`, moving is a STOP-and-report.
3. `gen_derivation_boot_pack.py --check` — expected GREEN unless 1(e) or 2(d) recorded it red by this batch; the manifest
   is NOT regenerated here in either case.
4. **LAST, after the final edit to `STATUS.md` and after `gen_session_start_read_size.py` has been regenerated:**
   `python tools/audit/gen_per_session_reading.py` (write mode; its `--check` red before), then `--check` GREEN.

**Each moved artifact is diffed against its blob at `<T2>` (or the last regeneration commit)** in blob form, by a scratch
script quoted whole in the appendix, **and every changed passage is accounted for.** Expected:
`session_start_read_size.json` — the `STATUS.md` member, the total and the comparisons built on the total;
`defense_share.json` — the whole-read denominator and the share against it; `per_session_reading.json` — the ordinary
read's `STATUS.md` member and every sum and mirror that includes it; **in `the_cowork_boot_chain`, the three latest
handoff entries (name the three, as the tool orders them, and say how any tie at `<T0>` was broken) and the sums that
include them**; **in `the_reports_with_an_appendix_beside_them`, TWO added pairs — the first stopped batch's
(`cc_report_llm_correction_2026_11_07.md`, landed at `d46a7b48…`) and the resume batch's
(`cc_report_llm_correction_resume_2026_11_07.md`, landed at `<T0>`) — `count` two higher, the two sums higher by those
four files' sizes in CHARACTERS as the tool reads them (`len()` of the decoded text) [the tool's lines 720–721, relayed
from the resume dispatch], not the byte sizes of 0(d)**; and, **because the artifact at `<T2>` is the one last made
current at the records landing's end state** (relayed: the tool passed there and neither stopped batch regenerated it),
**the handoff population gaining entries 570 onward, and every sum, mirror and share built over it. The dispatch and
report populations do not move:** the tool admits to them only file names opening
`cc_instruction_l3_comparison_tabulation_` and `cc_report_l3_comparison_tabulation_` (its lines 203 and 205) [relayed
from the resume dispatch]. **Any other movement is reported by field.**

**3(d) — THE REPORT, IN THE TWO-FILE FORM OF RULING 4 OF THE 2026-11-01 RECORD.** That ruling's words (RELAYED; read the
2026-11-01 record if the wording matters to a step): *"a Claude Code report is written in two files, committed in the
same commit: the REPORT PROPER — the ordered first read, the capacity judgments, every task's account, every claim,
grade, declared departure, finding and observation, every check's verdict, and for every scripted search its terms, its
hit count and the rows named — and a separate APPENDIX FILE beside it, named in the report with its path, its size and the
searches it holds, carrying the raw printouts verbatim (every hit line as the search printed it) and nothing the report
proper needs."*
- **The report proper**, `records/cc/reports/cc_report_llm_correction_second_resume_2026_11_08.md`: your first tool call
  named exactly; your account of what reached you as injected context; the eight-line check with each line as read and
  as injected; a capacity judgment; Tasks 0 to 3, each with what it did and every check's verdict — **for each capture
  its header line, its counts, its failing set by name, and every line that differs from the capture before it**; **for
  every tool newly red at 1(e) or 2(d): its cause as printed, the source line that reads the changed file, and whether it
  was regenerated or carried**; 0(c)'s enumeration against the landing set and A1; 0(d)'s result; 1(a)'s proof; 1(b)'s
  and 1(c)'s outputs and accounting, the set artifact's `counted` block before and after, and the two SHA-256 values;
  every `--numstat`; the commits in a table (task, commit, parent, the number of committed blobs); 3(b)'s constants as
  found and as set and `the_moved`; 3(c)'s moved values per artifact; E0 to E3 and A1 to A5 graded (E4 and A4/A5 at
  Task 4); declared departures; observations met and not acted on; **a short paragraph on whether this dispatch could be
  executed without reading any earlier dispatch or report, and if not, which step sent you to one**; **the list of tools
  carried red by this batch, as questions for the writing side**; and **the tell in one sentence: did this batch produce
  anything other than the landing set, the edited set, the set and split artifacts, the artifacts A2 and 3(c)
  regenerated, the Task 3 files, the report and its appendix, the away-returns section, the end state's guard artifact —
  and, outside the repository, scratch files and loose blob objects? If yes, name it.**
- **The appendix**, `records/cc/reports/cc_report_llm_correction_second_resume_2026_11_08_appendix.md`, beside it: the
  raw printouts verbatim, each under a heading naming its command and step — A1's enumeration whole, 0(d)'s script and
  output, 1(a)'s proof, 1(b)'s and 1(c)'s outputs and diffs, every `--numstat`, every capture whole, every regeneration
  diff, the 3(b) apply and the four archive checks, every 3(c) check and diff whole. **The report proper names the
  appendix with its path, its size in bytes and the list of what it holds.**

**3(c′) — THE LAST REGENERATION, after 3(d) has written the report and its appendix in their final form and before
3(e).** Run `python tools/audit/gen_per_session_reading.py` (write mode) once more, then `--check` GREEN, and diff the
artifact against the one 3(c) left: **expected, only `the_reports_with_an_appendix_beside_them`: `count` one higher, the
two sums higher by this batch's two sizes in characters as the tool reads them, and one added pair naming
`cc_report_llm_correction_second_resume_2026_11_08.md`.** Anything else is reported and is a STOP before 3(f). **After
this run neither the report nor its appendix is edited again**; the run's output and its diff go in the away-returns
section of 3(e), not in the report.

**3(e) — the close section appended to `records/cowork/handoff/cowork_away_returns.md`**, headed **THE LANGUAGE-MODEL
CORRECTION OF 2026-11-07, SECOND RESUME — RULING 1 ITEMS 1 TO 6 APPLIED; DOCUMENTATION AND RECORD-KEEPING ONLY, NO
ALGORITHM CHANGED**: the report's content as pointers, naming the resume batch's report and appendix as landed at `<T0>`
(that batch appended no section here), 3(c′)'s output and diff, and **the plan line:** *"The next act is the writing
side's — the check of this batch's return at the objects; then L3 family 7's check (the language-model family
surface)."* Read the file's last section before appending, for its form; append only.

**3(f) — the close commit** carries `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`,
`tools/audit/status_batch_bound.json`, every artifact 3(c) and 3(c′) moved, the report, its appendix and
`records/cowork/handoff/cowork_away_returns.md` — by explicit path, the staged set proved with `changed_paths.py
--staged`. Subject: `Close: the language-model correction of 2026-11-07, second resume - Ruling 1 items 1 to 6 applied,
under its dispatch`. Push; verify `origin/master` at the ref file. **Held back:** A1's five standing items, the standing
untracked population, any handoff entry that appeared during the run, every scratch file. **The close does not assert
the end state**; Task 4 carries it.

**E3:** at the tree carrying the close, every check 3(b) and 3(c) name green; `gen_guard_state.py`'s own artifact stale
until Task 4; nothing outside A4 changed.

---

## Task 4 — the end state

- **The run:** `python tools/audit/gen_guard_state.py` (write mode, named) at the tree the close commit left, its output
  saved whole. **The condition:** run **83**; zero STOPs in the runner; **the failing set exactly the thirteen standing
  reds (the fourteen less `gen_per_session_reading.py`) plus the tools carried red by this batch at 1(e) and 2(d),
  named, none other**; `gen_specification_document_set.py --check`, `gen_period_stratum_split.py --check`,
  `gen_per_session_reading.py --check`, `gen_session_start_read_size.py --check`, `gen_defense_share.py --check` and
  `gen_l3_outgoing_population.py --check` PASS unless carried; the NOT RUN and HISTORICAL lines identical to the opening
  capture's; against the opening capture **the verdicts that differ are exactly `gen_specification_document_set.py` and
  `gen_per_session_reading.py` FAIL → PASS, and the carried tools PASS → FAIL**. Then
  `python tools/audit/gen_guard_classification.py --check`, its STOP naming the same five tools as at 0(f) — a further
  name is a STOP-and-report.
- **The verification at the objects:** `git diff --name-status 257ad5bfc1915f63c1e0b7e54da5692e6003e64b <the close
  commit>`, every path accounted for against A4 and the landing set, **every file A5 names absent from it** (the landing
  set's own files appear once, as additions).
- **The record:** append the end-state portion to this batch's section of `records/cowork/handoff/cowork_away_returns.md`
  — the run's header, counts and failing set by name, the comparison with the opening capture, the classification STOP,
  the name-status list's counts by status and every path by name, A4 and A5 graded, the close commit's hash. Commit
  `tools/audit/guard_state.json` and that file only, by explicit path, the staged set proved. Subject: `End state: the
  language-model correction of 2026-11-07, second resume - guard run at the close tree`. Push; verify `origin/master` at
  the ref file.

**E4:** the condition held at a fresh run committed only after the run that produced it.

**THIS BATCH ENDS HERE.**

---

## What this batch does NOT do

- **No algorithm change; no measurement of the analysis.** No specification text is edited; the banner is not changed.
- **Ruling 1 item 7 is not applied** — Ruling 57 clause (ii), Ruling 62 item 11, the DESIGN-INTENT seed list, the
  document's membership of the specification document set, and the four leak-check records stay as they are. The three
  grades leave the membership as it is.
- **No text moves out of any governing document**; `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS.md`,
  `DECISIONS_ARCHIVE.md`, `ARCHITECTURE.md` and `cowork_audit_protocol.md` are not edited.
- **No tool edited or added** but the set tool's `GRADES` table (Task 1) and the forward-bound tool's re-aiming. No guard
  enrolment changes; no classification verdict is authored; **no pinned value is re-pinned.**
- **No line is added to or removed from any reading file.**
- **The resume batch's report and appendix are landed as they stand and not edited; no earlier report is corrected.**
- **No new decisions-register entry, no `D-NNN`, no open-items row.**
- **A1's five standing items are not touched.**

## What this batch deliberately leaves to later acts, named so it is not lost

- **The tools carried red by this batch**, if any — their re-pinning is the writing side's question, put to the user if
  the record does not answer it.
- **The register's home anchors** for D-440 to D-448 (`ARCHITECTURE.md` and `docs/llm_integration.md` line ranges) —
  whether a superseded entry's home should point elsewhere is not decided here.
- **Places not searched for line-number citations of the register's data file** (outside the set handoff entry 577 §2
  names).
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

**RUN 2026-11-08** by the Cowork sitting booted on
`records/cowork/handoff/cowork_handoff_entry_five_hundred_and_eighty_four.md`, at staged working-tree copies read with
the file tools (no shell, no git command); its result is recorded below the five points. *(Former wording of this
paragraph's opening, kept (#12): "**NOT YET RUN.** The banner stays NOT YET RELEASED until the check below is run and
recorded here, every correction at its site with the former wording kept (#12).")* **Points the check must settle:**

- **C1 — the premise ledger, each FACT at its object;** each RELAYED item either read at its object or left marked.
- **C2 — 1(a)'s text:** the fifteen lines' indentation against the table's own entries; the `§` and `—` characters
  against the tool's encoding (it already carries `—`, and `§` on 28 lines by one count-mode search of the staged copy
  at writing); that the comment line
  cannot be mistaken for an entry; the line numbers 572–586 and 587 in 1(a)'s proof.
- **C3 — 1(b)'s expectation:** whether the set artifact publishes a grade's `why` text or the banner's line text for an
  excluded target, so that the expected diff names those passages exactly; and whether `gen_guard_classification.py`,
  `gen_guard_state.py` or any other enrolled tool reads the set tool's source or the split artifact (search `tools/audit`
  for `gen_specification_document_set` and `period_stratum_split`; read only matched lines).
- **C4 — 3(c)'s two added report pairs:** whether `the_reports_with_an_appendix_beside_them` at `<T2>` already holds the
  first stopped batch's pair (it would, if any batch regenerated that artifact after `d46a7b48…`).
- **C5 — the overstatement sweep** over this file's absolutes (every, all, none, only, exactly, never), each hit read at
  its line, this section's own text included.

### The check's result (2026-11-08)

- **C1.** Read at the objects and holding: both ref files at the start tip; `.git/logs/HEAD` lines 2111–2114 give the
  chain as stated (line 2110 gives `4461d865…`'s parent as `566d37e5…`, so that item is no longer only relayed);
  `STATUS.md` at 10,680 bytes, its entries and paragraphs at the lines stated, one line carrying `Last updated: `;
  `ARCHITECTURE.md` lines 8088–8090 as stated, and the three targets named on line 8089 alone (one count-mode search,
  one line); the set tool at lines 92–93, 119–123, 153–164, 388, 429–432, 506–508, 571–572, 722 and 786–807 as stated,
  line 571's text found once, `llm_` hits only at 348, 355, 708 and 709; the split tool at 55, 73, 136 and 407–412 as
  stated (its widening reads the set artifact's member paths and each member's limb and scope, which do not move);
  `gen_l0_l1_outgoing_population.py` lines 291–310 read member paths only, and the L2 and L3 tools import that reader;
  `gen_l2_outgoing_population.py` lines 128–131, 380 and 556 and `gen_l3_outgoing_population.py` lines 189–194 as stated;
  the four reading-file lines hold the four `old_string` texts; the landing files' sizes as stated (the reports
  folder's and handoff folder's listings); `gen_status_batch_bound.py`'s six constants in the working tree equal 3(b)'s
  expectation. **Still relayed, not read here:** the guard state (A2's fourteen and fifteen; the five-name STOP), A1's
  enumeration, the three-latest tie, and that the split tool passes at the start tip.
- **C2.** Indentation matches the table (four spaces before a key or comment, eight before a constant or string); the
  file is LF-only and already carries `§` (28 lines by one count-mode search) and `—`; the comment sits inside the dict
  literal and cannot be read as an entry; the fifteen lines fall at 572–586 and `}` at 587. **One correction**, at 1(a):
  the third entry's `why` text (it called the sentence appended, and its last clause did not parse).
- **C3.** The set tool publishes, per graded target, its `why` text and every naming with its line and whole line text
  (lines 816–831); 1(b)'s expectation now names those fields. A naming moved by the banner was looked for and not found:
  the artifact's citations near line 8089 (8090, 8096) match the file, and `docs/llm_integration.md`'s property anchor
  is still at its line 3 under that document's own banner. A search of the top-level `.py` files of `tools/audit` and of 15
  tools in `tools/audit/decisions` (the subfolders and the other `decisions` tools not searched) for
  `specification_document_set` and `period_stratum_split` found readers only in the set and split tools,
  `gen_guard_state.py` (enrolment, lines 189 and 209), `gen_guard_classification.py` (authored verdict text; it reads
  `guard_state.json` and its own output, not tool sources), `gen_july_screen.py` (the split artifact's populations),
  `gen_derivation_boot_pack.py` (comments only) and the three outgoing-population tools. No reader of the SHA-256 or of
  the set tool's source was found. A2's rule stays as written for anything not found.
- **C4.** At the start tip `per_session_reading.json` → `the_reports_with_an_appendix_beside_them` holds seven pairs,
  the records landing's the last; neither language-model report pair is there. Nothing in Tasks 1 and 2 regenerates it
  (it is among the fourteen already failing), so 3(c)'s two added pairs stand.
- **C5.** Every hit was read at its line. **One correction**, in the plain-words section (the same misdescription as in
  C2, and the precedent lines). The rest either states an instruction, states a fact read in C1, or is marked as an
  expectation or a relay where it is used.

**Documentation only; no algorithm change is decided.** The method that stands is the scope document's §5.
