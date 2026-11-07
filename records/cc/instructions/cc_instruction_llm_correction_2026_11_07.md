# CC dispatch — THE LANGUAGE-MODEL CORRECTION: RULING 1 ITEMS 1 TO 6 OF THE 2026-11-07 CORRECTION RECORD APPLIED (THE REGISTER, TWO DESIGN TEXTS, ONE RULING RECORD, THREE READING FILES) — DOCUMENTATION ONLY; NO ALGORITHM CHANGE (2026-11-07)

> **STATUS: RELEASED 2026-11-07** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_four.md`, after the check recorded at the end of
> this file was completed (C1 in part, the overstatement sweep run). **This dispatch may now be handed to Claude Code.**
> The lines below are the former banner, kept (#12).
>
> **STATUS: WRITTEN 2026-11-07 — NOT YET RELEASED** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_one.md`. Its check at its sources runs in a turn
> of its own, in a later Cowork session; this banner is set to RELEASED only after that check, which is recorded at the
> end of this file with every former wording. **Until then this dispatch is NOT handed to Claude Code.** Once released it
> is executed by Claude Code when the user hands it over (D-252); the Cowork writing side never runs it.
> **★ 2026-11-07, the check's first sitting (booted on entry 572):** the check ran in part and is recorded at the end of
> this file. Four corrections were made at their sites. **The dispatch stays NOT YET RELEASED**, because point C1 (which
> guard tools read the edited files) needs reads that did not fit that sitting. **If any
> expected result does not appear, stop at that step and report it. Do not continue to the next one.**
>
> **THE WRITING SIDE'S RESTRAINT, declared.** Once released this dispatch is final. The writing side will not touch it,
> nor any file it names, while this batch runs. The files the writing side writes after this dispatch lands and before
> hand-over are handoff entries (`records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy_two.md` to
> `…_five_hundred_and_seventy_five.md`, and possibly one more), which is why Task 0 states no size for them. *(★ STALENESS
> FIXED 2026-11-07 at the release. Former wording (#12): "(`…_five_hundred_and_seventy_two.md` and possibly one more)".)* **Nothing this dispatch lands is in git yet**; Task 0
> lands it.

## What this batch is, in plain words

On 2026-11-07 the user ruled that a language model is used only while the software is being developed, never at run time
in the finished product (`records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`, Ruling 1), and
that entries conflicting with that are corrected, with their downstream effects (its Ruling 2). The same day he
ratified the corrections as derivations (`records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`,
Ruling 1, items 1 to 7; item 7 is "no act now"). The previous batch landed those records. **This batch applies items 1
to 6.**

- **Task 0** lands the handoff entries written since, and this dispatch, and pushes.
- **Task 1** (items 1 and 2): seven register entries become SUPERSEDED BY the 2026-11-07 ruling; two get a provenance
  note. The change is made in the register's data file and the register is regenerated.
- **Task 2** (items 3 and 4): a superseded banner over `ARCHITECTURE.md` §19 and over `docs/llm_integration.md`; a note
  in the 2026-08-08 route record.
- **Task 3** (items 5 and 6): annotations in the three reading files.
- **Task 4** is the close; **Task 5** the end state.

**★ ONE RULE FOR EVERY TEXT EDIT OF TASKS 1 TO 3: NO LINE IS ADDED OR REMOVED.** Every banner, note and annotation either
takes the place of one named blank line or is inserted inside one named line. So no line number cited in the files
those tasks edit moves. *(★ NARROWED 2026-11-07 at the check (overstatement sweep). Former wording (#12): "ONE RULE FOR
EVERY TEXT EDIT IN THIS BATCH" and "no line number cited anywhere in the record moves" — Task 4(a) adds entries to
`STATUS.md`, and Task 4 writes new files, so the rule never covered the whole batch.)* Each edit is proved by `git diff --numstat` showing the same number of lines added as removed, and by the
file's line count being unchanged.

**Documentation and algorithm, separated.** **Documentation only:** everything this batch edits, apart from 4(b)'s re-aiming of the forward-bound tool, which changes
that record-keeping tool's constants and no specification. *(★ NARROWED 2026-11-07 at the check (overstatement sweep).
Former wording (#12): "everything this batch edits.")* **Algorithm: NOTHING
changes.** No specification of the analysis is changed in substance; the edited design texts describe a language-model
product tool, which is not the analysis. The method that stands is the one the scope document
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
3. **The highest-numbered handoff entry on disk, whole** (the highest above 571 that exists); it is the current handover
   block. *(★ CORRECTED 2026-11-07 at the check (point C2). Former wording (#12): "(572 if it exists, else 571)".)*
4. `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md` whole (5,001 bytes) — the ruling this
   batch applies.
5. `tools/audit/gen_l3_outgoing_population.py` at its `L3_KEYWORDS` list, located by search (for 4(a)'s search).

**Not read, and not needed:** any earlier dispatch or report; the scope document; the reading files beyond the lines
Task 3 names; `FRAMEWORK.md`. Declare any further read you make.

---

## ★ WORDS USED IN THIS DISPATCH, EXPLAINED FIRST

- ***The start tip*** — `7c2d1bccc885b1e11204727f0800ffe20fd84b21`, the commit both ref files named when this dispatch was
  written (the end state of the records landing of 2026-11-07).
- ***The previous batch*** — the batch run under `records/cc/instructions/cc_instruction_records_landing_2026_11_07.md`.
  Named only so the forward bound (4(b)) can move its `STATUS.md` entries; **you do not read it.**
- ***The test-only ruling*** — Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md`.
- ***The correction record*** — `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`.
- ***The edited set*** — the nine files Tasks 1 to 3 edit: `tools/audit/decisions/backbone_decisions.json`,
  `DECISIONS.md`, `decisions/group_N.md`, `ARCHITECTURE.md`, `docs/llm_integration.md`,
  `records/cowork/rulings/cowork_document_route_rulings_2026_08_08.md`,
  `ratification_surfaces/cowork_comparison_l2_reading.md`, `ratification_surfaces/cowork_comparison_l0_l1_reading.md`,
  `ratification_surfaces/cowork_comparison_l3_reading.md` — nine paths; `DECISIONS.md` and `decisions/group_N.md` are
  written by the generator, not by hand, so the hand-edited files are seven.
- ***`<T0>`, `<T1>`, `<T2>`, `<T3>`*** — this batch's task commits. ***`<ACT_DATE>`*** — the day the step runs.
- ***A capture*** — the output of `python tools/audit/gen_guard_state.py --check`, saved whole to a scratch file outside
  the repository and read. ***Compared verdict by verdict*** means every tool's PASS / FAIL / NOT RUN / HISTORICAL line
  side by side, and the tally line.
- ***Red by this batch*** — a tool that passed at the capture before a task and fails at the capture after it, whose
  printed cause names, or whose inputs (read at the tool's source) include, a file of the edited set changed by that task.

---

## Ruling ledger

- **The correction record, Ruling 1 items 1 to 6** — what this batch applies. Item 7 (no act now) is not applied.
- **The test-only ruling and its Ruling 2** — the ground the correction record rests on.
- **The user's ruling of 2026-11-07 on the three standing modifications** (handoff entry 571 §2 item 1): *"Leave them -
  we will revisit this when we look at the externally compiled list of relevant research/software/algorithms. Then we
  can consolidate and fix whatever is needed."* — the ground for A1.
- **Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md`** — the dispatch form.
- **Ruling 4 of the 2026-11-01 pruning record** — the report's two-file form (4(d)).
- **The register's own rule**, at `tools/audit/decisions/gen_decisions_register.py` line 16: *"To change an entry, edit
  `backbone_decisions.json` and re-run this generator."*
- **No new rule is made.**

---

## Premise ledger (written 2026-11-07 by the writing side from staged working-tree copies read with the file tools; no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
  `7c2d1bccc885b1e11204727f0800ffe20fd84b21`.
- **RELAYED — the chain** (handoff entry 570 §2 item 1, read there at `.git/logs/HEAD` lines 2106–2108):
  `864deb43c5dae6415a8c8b9e98901e7b2c2a96ae` → `113b2ce680e527e81342d8f79d5acbad281334d7` (the previous batch's Task 0)
  → `8ac62876975b891fef7ed2fc87257383dcf2c33f` (its close) → `7c2d1bcc…` (its end state).
- **FACT — `STATUS.md`** (10,680 bytes, read whole): the previous batch's TWO entries at lines 8 and 10 — its close entry
  carrying `Last updated: `, then its Task 0 `Same dispatch` entry; the two 2026-09-02 entries at 12 and 14; the
  archive-pointer paragraphs at 16, 18, 20 and 22, the one at 18 being the standing paragraph that holds the word
  *paraphrase* (called ***the paraphrase paragraph*** below). Exactly one line carries `Last updated: `.
- **RELAYED — the guard state at the start tip** (handoff entry 570 §2 item 1, read there at the previous batch's
  away-returns section): run 83, failing 13 — the thirteen of the previous dispatch's premise ledger; the classification
  `--check` STOPs naming five tools: `gen_l0_l1_outgoing_population.py`, `gen_l2_withheld_documents.py`,
  `gen_l3_outgoing_population.py`, `gen_withheld_family_reading.py`, `gen_per_session_reading.py`. **Read
  `tools/audit/guard_state.json` at the start tip yourself at 0(f); the object is the value of record.**
- **FACT — the register's data and generator**, read at the objects:
  - `decisions/group_N.md` lines 3–7 is a banner: a generated file, not hand-edited; source of record
    `tools/audit/decisions/backbone_decisions.json`; generator `tools/audit/decisions/gen_decisions_register.py`.
  - The generator (lines 88–96) maps the data value `"superseded-by"` to the label `SUPERSEDED BY`, and (lines 424–426,
    485–487) appends the entry's `superseded_by` value after the label. It renders `status_source` as the entry's
    **Provenance.** line (line 523). It writes `DECISIONS.md` (the index) and one file per group (lines 591–598, 622–627);
    `--check` regenerates in memory and prints `STALE vs the data: <path>` per differing file, exit 1, else exit 0
    (lines 611–620).
  - In the data file, each decision begins at a line `      "id": "D-NNN",` (six spaces): D-440 line 9343, D-441 9366,
    D-442 9389, D-443 9427, D-444 9465, D-445 9503, D-446 9541, D-447 9579, D-448 9617. Their `status` lines:
    `      "status": "deferred",` for D-440 (9350) and D-441 (9373); `      "status": "not stated",` for D-442 to D-448
    (9396, 9434, 9472, 9510, 9548, 9586, 9624). Each has one `      "status_source": "…",` line.
  - The precedent form of a supersession, at D-line 1903–1917 of the data: `"status": "superseded-by"`, a
    `"superseded_by"` key carrying free text (`"D-001"`), and the reason appended to `status_source` as a
    *★ USER RULING …* sentence ending *"(was superseded-in-fact)."*. This batch follows that form.
- **FACT — the design texts and the route record**, read at the objects:
  - `ARCHITECTURE.md` line 8088 `## 19. LLM Integration — Claude Composer`; line 8089 blank; line 8090
    `> **Full design document:** `docs/llm_integration.md`` followed by two spaces; the opening blockquote runs to 8098.
  - `docs/llm_integration.md` line 1 `# LLM Integration in MuseScore Studio — Design Document`; line 2 blank; line 3
    `> **Status:** Design phase. No code written yet.` followed by two spaces.
  - `records/cowork/rulings/cowork_document_route_rulings_2026_08_08.md` lines 33–37: route (i)'s bullet for
    `docs/llm_integration.md`; line 37 reads, whole, `  document is authoritative, not stale).`
  - `docs/llm_triage_design.md` exists; line 1 `# LLM-Assisted Triage for Chord Inference Validation — Design Discussion`.
- **FACT — the reading-file lines**, read at the objects:
  - L2 (`ratification_surfaces/cowork_comparison_l2_reading.md`, 5,068,067 bytes): lines 72465–72469 the member's
    description, line 72468 reading, whole, `> the analysis it is handed as context, and its future as a plugin. **The
    placement readings are those of the earlier`; line 72555 `#### Not a statement — listed so the arithmetic closes
    (34)`; items 1 to 34 at lines 72557–72590, each describing a statement as *a statement about a product tool outside
    the analysis* or as a label or table row; line 72557 is item 1.
  - L0/L1 (`ratification_surfaces/cowork_comparison_l0_l1_reading.md`, 1,102,100 bytes): line 10142 reads, whole,
    `> **What it is.** The design of a natural-language interface to the score — a consumer of the analysis`.
  - L3 (`ratification_surfaces/cowork_comparison_l3_reading.md`, 5,135,149 bytes): lines 30465–30466 are item 21 of a
    numbered list; line 30466 reads, whole, ``    `useExistingChordSymbols`." (3233–3235) — the defense of keeping the
    fields of Row 21.102.``
- **NOT KNOWN — which guard tools read the edited set.** The writing side did not read the guard tools for their inputs.
  A2 therefore does not predict the reds of Tasks 1 to 3 tool by tool. It gives a rule instead, with a capture after each
  task so every red is traced to the one task that caused it. *(★ NOTE 2026-11-07 at the check (point C1): the check
  read some of them in part; A2 now names the reds it found and ties the ruled change itself to the rule. The rest
  stay not known.)*
- **ASSUMPTION A1 — the working tree, stated by CONTENT.** Tracked modifications at your boot: **exactly three** —
  `tools/audit/claude_md_finer_archive.json` (standing, carried), `docs/research_papers/BIBLIOGRAPHY.md` and
  `docs/research_papers/README.md`; and untracked, beside them, `docs/research_papers/polyph9-release/`. **The last three
  were made by another tool, unintentionally, and the user ruled them left as they are** (the ruling ledger). **You do
  not touch, restore, land or delete any of the four, and their presence is not a STOP.** If one is absent, report it;
  that is not a STOP. **The writing side wrote no tracked file.** Untracked and landed by Task 0: the landing set.
  Beyond it, only the standing untracked population, which is not landed and is not a STOP. **Your enumeration with
  `tools/audit/changed_paths.py` establishes A1.**
- **ASSUMPTION A2 — the reds.**
  - **At your boot, before Task 0:** `gen_per_session_reading.py --check` expected to STOP (exit 2; handoff entries
    untracked). Do not run the full guard set before Task 0.
  - **The opening capture (0(f), after `<T0>`):** run 83; zero STOPs in the runner; the thirteen FAIL and
    `gen_per_session_reading.py --check` FAILS (the landed entries change the three latest), and nothing else.
  - **The captures after `<T1>`, `<T2>` and `<T3>` (1(e), 2(d), 3(d)):** each compared verdict by verdict with the one
    before. **A tool newly FAIL must be *red by this batch*** (the words above): you report its printed cause and the
    line of its source that reads the edited file, quoted. **Then exactly one of:**
    - **(regenerate)** the tool writes a derived artifact (it has a write mode) and its `--check` compares that artifact
      to what the inputs now give: run the bare write mode, then `--check` green, and diff the artifact against its blob
      before the task between explicit blob hashes. **Every changed passage must be tied to an edit of that task**; a
      member of any population, list or set entering or leaving is a STOP-and-report (the task's commit stays; nothing
      further runs) — **except where every member entering or leaving is tied to the task's own edit, as follows: at
      1(e), one of D-440 to D-443 and D-446 to D-448 entering a superseded set or count (or leaving a deferred or
      not-stated one), or D-444 or D-445 changing only by the provenance note; at 2(d) and 3(d), a change only in a
      size, line count, hash or term-search hit of a file that task edited, at the edited line. Then quote each such
      changed passage in the report, tie it to the edit by name, commit the regenerated artifact as 1(e) says, and
      continue.** A member entering or leaving that is not so tied stays a STOP-and-report. *(★ AMENDED 2026-11-07 at
      the check (point C1). Former wording (#12): the sentence ended at "(the task's commit stays; nothing further
      runs)." with no exception, which would have stopped the batch after `<T1>` was pushed, because the ruled
      supersession itself moves the seven entries into a superseded set.)*
    - **(carry)** the tool compares the file to a fixed value recorded at an earlier act (a hash, a pinned size, a frozen
      copy): **do not regenerate and do not re-pin.** Record it as red by this batch, with its message, and continue.
      Its re-pinning is a question for the writing side, which the report names.
    - **Neither, or unsure:** STOP-and-report.
  - **A newly FAIL tool that is NOT red by this batch is a STOP-and-report.** A tool newly PASS is reported and is not a
    STOP.
  - **Reds predicted by name** *(★ ADDED 2026-11-07 at the check (point C1); a partial prediction, not a complete one —
    a tool not named here is still handled by the rule above)*:
    - **At 1(e): `tools/audit/decisions/gen_r1_superseded_reach.py --check`** (passing at the start state) is expected
      newly FAIL. It re-derives `tools/audit/decisions/r1_superseded_reach.json` from the working-tree register and
      compares byte for byte (its lines 779–797); the artifact counts the register's entries per superseded status and
      how many carry a populated `superseded_by` (lines 553–560), and lists superseded entries outside its NO-HOME
      class (lines 571–574). Seven entries entering `superseded-by` change those counts and may add members to that
      list. That is the tied case of the rule above: regenerate, quote, tie to D-440 to D-443 and D-446 to D-448, and
      continue.
    - **At 2(d) and 3(d), possibly:** `tools/audit/gen_l2_outgoing_population.py` records whole-file byte sizes of the
      documents it names (its line 380), and it and `tools/audit/gen_l3_outgoing_population.py` read the transfer-list
      section (`## 10.`) of the L0/L1 and L2 reading files (`gen_l2_outgoing_population.py` lines 128 and 556;
      `gen_l3_outgoing_population.py` lines 187–194). Whether Task 2's or Task 3's edits fall inside what they read
      was not checked by the writing side. A size or hit change at an edited line is the tied case; anything else is a
      STOP-and-report.
    - **Already failing at the start state, so not "newly FAIL":** `gen_filing_convention_application.py` and
      `gen_cluster_dispositions.py`, `gen_home_classification.py`, `gen_phase1p_delegation_bar.py`,
      `apply_soft_discard.py`, `apply_residue_discard.py` under `tools/audit/decisions/`, each of which reads the
      register. Report any change in what they print; it is not a STOP.
  - **Task 4:** `gen_session_start_read_size.py` and `gen_defense_share.py` expected RED after 4(a) (both read
    `STATUS.md`; and `DECISIONS.md`, which Task 1 regenerated, is in the session-start read, so they may already be red
    at 1(e) and handled there); `gen_l3_outgoing_population.py --check` and `gen_l0_l1_outgoing_population.py --check`
    may be red after 4(a)/4(b) (they carry a `STATUS.md` residue record with line values); `gen_per_session_reading.py`
    regenerated LAST and again at 4(c′).
- **ASSUMPTION A3** — no `src/` file, build, test, golden, corpus of scores or measurement of the analysis is touched.
- **ASSUMPTION A4 — THE FOOTPRINT.** **Task 0:** the landing set. **Task 1:** `backbone_decisions.json`, `DECISIONS.md`,
  `decisions/group_N.md`, and any artifact 1(e) regenerates. **Task 2:** `ARCHITECTURE.md`, `docs/llm_integration.md`,
  the route record, and any artifact 2(d) regenerates. **Task 3:** the three reading files, and any artifact 3(d)
  regenerates. **Task 4:** `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py` at its authored
  aiming and head comments, `tools/audit/status_batch_bound.json`, the artifacts 4(c) and 4(c′) regenerate, the report and
  its appendix, `records/cowork/handoff/cowork_away_returns.md`. **Task 5:** `tools/audit/guard_state.json` and the
  away-returns end-state portion.
- **ASSUMPTION A5 — byte-unchanged by this batch:** `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS_ARCHIVE.md`,
  `cowork_audit_protocol.md`, `FRAMEWORK.md`, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`; everything under `docs/` but
  `docs/llm_integration.md` (the A1 modifications stay as they are, unstaged); every tool under `tools/audit/` but
  `gen_status_batch_bound.py`; every file under `tools/audit/decisions/` but `backbone_decisions.json` **and any
  artifact A2's rule regenerates** *(★ AMENDED 2026-11-07 at the check (point C6); former wording (#12): "every file
  under `tools/audit/decisions/` but `backbone_decisions.json`;" — which contradicted A2's regeneration of an artifact
  in that folder, such as `r1_superseded_reach.json`)*; every ruling record
  but the route record; every handoff entry, ratification document, dispatch and report already tracked, but the three
  reading files and `cowork_away_returns.md`; every group file under `decisions/` but `group_N.md`.

## The declared start state — at the tree you will meet

1. Both ref files at the start tip; A1's four standing items; the landing set untracked; nothing running.
2. The thirteen failing tools — standing reds, none of them this batch's — and the classification's five-name STOP.
3. `gen_per_session_reading.py --check` STOPs at your boot (A2). **If it is instead RED or GREEN, report what it printed;
   that is not a STOP.**

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
  7c2d1bccc885b1e11204727f0800ffe20fd84b21` (expected parent `8ac62876975b891fef7ed2fc87257383dcf2c33f`) and `git
  cat-file -p 8ac62876975b891fef7ed2fc87257383dcf2c33f` (expected parent `113b2ce680e527e81342d8f79d5acbad281334d7`), each
  hash written literally in its own command. A different chain is a STOP-and-report with nothing committed.
- **0(c) — A1 and the landing set**, by `python tools/audit/changed_paths.py` (the sanctioned enumeration; `git status`
  is not used, D-253): exactly A1's three tracked modifications; **every path of the landing set untracked, and every
  untracked path under `records/cowork/handoff/`, `records/cowork/rulings/`, `ratification_surfaces/` and
  `records/cc/instructions/` a path of the landing set**; other untracked paths only the standing population and
  `docs/research_papers/polyph9-release/`. A path of the landing set missing, or an untracked path in those four
  folders outside it, is reported and is a STOP. **The landing set:**
  - **(i) handoff entries** — `records/cowork/handoff/cowork_handoff_entry_five_hundred_and_seventy.md`,
    `…_five_hundred_and_seventy_one.md`, and **every untracked handoff entry numbered above 571 at your boot**
    (`…_five_hundred_and_seventy_two.md` to `…_five_hundred_and_seventy_five.md` are written; a later one may be).
    *(★ STALENESS FIXED 2026-11-07 at the release. Former wording (#12): "(`…_five_hundred_and_seventy_two.md` and
    `…_five_hundred_and_seventy_three.md` are written; a later one may be).")*
    *(★ CORRECTED 2026-11-07 at the check (point C2): the entry the checking sitting writes, 573, would otherwise be an
    untracked handoff path outside the landing set, which this step makes a STOP. Former wording (#12): "and
    `…_five_hundred_and_seventy_two.md` if it exists at your boot.")*
  - **(ii) this dispatch** — `records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md`.
- **0(d) — last bytes** of each landing file, at its blob written `--no-filters`, by one scratch script quoted whole in
  the appendix: each object's size, its last 70 bytes and its count of zero bytes. Each must end with a newline after a
  complete line and hold no zero byte; a final line broken off mid-word, or a zero byte, is a STOP-and-report naming the
  file. **Expected sizes, at the writing side's listing:** entry 570 6,607; entry 571 7,932. **No size is stated for
  this dispatch or any entry above 571**; report every size in the appendix. *(★ CORRECTED 2026-11-07 at the check
  (point C2). Former wording (#12): "No size is stated for this dispatch or entry 572".)*
- **0(e) — the commit**, exactly the landing set and no other path, staged by explicit path, the staged set proved with
  `python tools/audit/changed_paths.py --staged`: **its count must equal the landing set's count.** Subject, exactly:
  `record: handoff entries 570 to <N>, with the language-model correction dispatch`, `<N>` the highest entry landed
  written as a number. *(★ CORRECTED 2026-11-07 at the check (point C2). Former wording (#12): "`record: handoff entries
  570 to 572, with the language-model correction dispatch` — or, if entry 572 is NOT at your boot, `record: handoff
  entries 570 and 571, with the language-model correction dispatch`, its absence reported; do not wait for it.")* Push; read `.git/refs/remotes/origin/master` and verify it equals the new tip. **This commit is `<T0>`.**
- **0(f) — the opening capture.** A capture, saved whole and read. Read the start tip's `tools/audit/guard_state.json` →
  `summary` at the object (`git show 7c2d1bccc885b1e11204727f0800ffe20fd84b21:tools/audit/guard_state.json`) and report
  its run, counts and failing set by name. Then `python tools/audit/gen_guard_classification.py --check`, expected exit 2,
  a STOP naming the five tools of the premise ledger — report them by name; a different set is a STOP-and-report. **The
  failing set must be A2's.** Anything else is reported and is a STOP.

**E0:** the landing set in one commit, pushed; the pin proved; A1 reported with its enumeration; the opening capture as
A2 states it; the five-name STOP.

---

## Task 1 — the register: seven entries SUPERSEDED BY, two noted (Ruling 1 items 1 and 2)

**1(a) — the data edit, by one scratch script**, saved outside the repository, quoted whole in the appendix, run from the
repository root with `python <script>`. It edits text, not a re-serialised JSON, so the file's formatting is untouched;
it adds no line; and it proves before writing that nothing but the intended fields changed. **The script, exactly:**

```python
# Ruling 1 items 1 and 2 of the 2026-11-07 correction record, applied to the register's data file.
import json, pathlib, sys
P = pathlib.Path("tools/audit/decisions/backbone_decisions.json")
text = P.read_bytes().decode("utf-8")
if "\r\n" in text:
    sys.exit("STOP: the data file has CRLF line endings; report and do not edit")
before = json.loads(text)
TEST_ONLY = "records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md"
CORR = "records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md"
SUP = {"D-440": "deferred", "D-441": "deferred", "D-442": "not stated", "D-443": "not stated",
       "D-446": "not stated", "D-447": "not stated", "D-448": "not stated"}
NOTE = ("D-444", "D-445")
SUP_BY = "Ruling 1 of `" + TEST_ONLY + "`"
SUP_TAIL = (" ★ USER RULING 2026-11-07 (Ruling 1 of `" + TEST_ONLY + "`, applied under Ruling 1 item 1 of `"
            + CORR + "`): a language model is never used at run time in the finished product, so this decision "
            "about a language model in the shipped product is SUPERSEDED BY that ruling (was {was}). The quoted "
            "wording and the 2026-08-04 entry ratification are kept (#12).")
NOTE_TAIL = (" ★ NOTE 2026-11-07 (Ruling 1 item 2 of `" + CORR + "`): Ruling 1 of `" + TEST_ONLY + "` removes the "
             "language-model bridge as one of the core access layer's two consumers. The rules themselves use no "
             "language model, and that ruling does not speak to the other consumer, a future plugin interface. "
             "Status unchanged.")
lines = text.split("\n")
def span(i):
    s = [k for k, l in enumerate(lines) if l == f'      "id": "{i}",']
    if len(s) != 1:
        sys.exit(f"STOP {i}: {len(s)} id lines")
    e = next((k for k in range(s[0] + 1, len(lines)) if lines[k].startswith('      "id": "')), len(lines))
    return s[0], e
for i in list(SUP) + list(NOTE):
    s, e = span(i)
    ss = [k for k in range(s, e) if lines[k].startswith('      "status_source": "') and lines[k].endswith('",')]
    if len(ss) != 1:
        sys.exit(f"STOP {i}: status_source lines {ss}")
    tail = SUP_TAIL.format(was=SUP[i]) if i in SUP else NOTE_TAIL
    lines[ss[0]] = lines[ss[0]][:-2] + tail + '",'
    if i in SUP:
        st = [k for k in range(s, e) if lines[k] == f'      "status": "{SUP[i]}",']
        if len(st) != 1:
            sys.exit(f"STOP {i}: status lines {st}")
        lines[st[0]] = f'      "status": "superseded-by", "superseded_by": "{SUP_BY}",'
new = "\n".join(lines)
after = json.loads(new)
bd = {d["id"]: d for d in before["decisions"]}
ad = {d["id"]: d for d in after["decisions"]}
if set(bd) != set(ad):
    sys.exit("STOP: the set of decisions changed")
for i in ad:
    b, a = dict(bd[i]), dict(ad[i])
    if i in SUP:
        if not (b["status"] == SUP[i] and "superseded_by" not in b and a["status"] == "superseded-by"
                and a["superseded_by"] == SUP_BY
                and a["status_source"] == b["status_source"] + SUP_TAIL.format(was=SUP[i])):
            sys.exit(f"STOP {i}: the superseded fields are not as intended")
        for x in ("status", "superseded_by", "status_source"):
            b.pop(x, None); a.pop(x, None)
    elif i in NOTE:
        if a["status_source"] != b["status_source"] + NOTE_TAIL:
            sys.exit(f"STOP {i}: the note is not as intended")
        b.pop("status_source"); a.pop("status_source")
    if a != b:
        sys.exit(f"STOP {i}: a field other than the intended ones changed")
if {k: v for k, v in before.items() if k != "decisions"} != {k: v for k, v in after.items() if k != "decisions"}:
    sys.exit("STOP: something outside the decisions list changed")
if new.count("\n") != text.count("\n"):
    sys.exit("STOP: the line count changed")
P.write_bytes(new.encode("utf-8"))
print(f"applied: {len(SUP)} superseded, {len(NOTE)} noted; lines {text.count(chr(10))} unchanged")
```

**Expected:** it prints `applied: 7 superseded, 2 noted; lines <N> unchanged` and exits 0. Any `STOP` line is a
STOP-and-report with the file unwritten. Then `git diff --numstat -- tools/audit/decisions/backbone_decisions.json`:
**expected `16	16`** (seven status lines and nine provenance lines, each replaced in place).

**1(b) — the regeneration.** `python tools/audit/decisions/gen_decisions_register.py --check` in its own call (expected
exit 1, `STALE vs the data:` for `DECISIONS.md` and `decisions/group_N.md` and no other path; another path is a
STOP-and-report); then `python tools/audit/decisions/gen_decisions_register.py` (write mode); then `--check` again,
expected exit 0.

**1(c) — the regenerated files accounted for.** `git diff -- DECISIONS.md decisions/group_N.md` into a scratch file,
quoted whole in the appendix. **Expected, and nothing else:**
- `decisions/group_N.md`: for each of D-440 to D-443 and D-446 to D-448, its **Status.** line now opens `SUPERSEDED BY
  Ruling 1 of` followed by the test-only ruling's path in backticks; for all nine, its **Provenance.** line is the former
  one with the 1(a) sentence added at its end.
- `DECISIONS.md`: the index rows of those seven entries, where the index renders them, with the same status text; the
  status tallies (deferred and not stated lower by 2 and 5, superseded by higher by 7) where the index states them.
  **The *Backbone data* sha256 line in *Provenance of this register* does NOT change**: the generator prints the value
  stored in `tools/audit/decisions/cluster_dispositions.json` → `header.inputs.backbone.sha256`
  (`gen_decisions_register.py` lines 284 and 451–452), not a hash of the data file as it now stands. Report it as
  unchanged; do not edit it. *(★ CORRECTED 2026-11-07 at the check (point C3). Former wording (#12): "the data file's
  sha256 line in *Provenance of this register*.")*
**Any other changed passage is reported by line and is a STOP-and-report before the commit.**

**1(d) — the commit**, exactly `tools/audit/decisions/backbone_decisions.json`, `DECISIONS.md` and
`decisions/group_N.md`, by explicit path, the staged set proved with `changed_paths.py --staged` (count 3). Subject:
`decisions: D-440 to D-443 and D-446 to D-448 superseded by the 2026-11-07 language-model ruling; D-444 and D-445
noted`. Push; verify `origin/master` at the ref file. **This commit is `<T1>`.**

**1(e) — the capture after `<T1>`**, compared verdict by verdict with 0(f)'s, and A2's rule applied to every tool newly
FAIL. If a regeneration runs, its artifact goes in a commit of its own, subject `artifacts: regenerated after the
register correction`, by explicit path, proved, pushed, and the capture is run again. Report every tool by name.

**E1:** the data edit as intended and nothing else; the register regenerated and `--check` green; the diff accounted
for; `<T1>` pushed; every new red traced to Task 1 and handled by A2's rule.

---

## Task 2 — the two design texts marked superseded; the route record noted (Ruling 1 items 3 and 4)

**Each edit below is made with the file-editing tool, `old_string` → `new_string` exactly as given; before each, search
the file for the `old_string` and confirm it occurs exactly once (else STOP-and-report).** In each, the blank line
between a heading and a blockquote is replaced by the banner line, which joins the blockquote below it as its first
line; the banner line ends with **exactly two spaces** (a hard line break), shown below as `␠␠` — type two space
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

**Proof of 2(a) to 2(c):** for each file, its line count (a count of newline bytes) before and after, equal; `git diff
--numstat` for the three: **`1	1` each**; and the new line read back with the file tools, checked for the two
trailing spaces in 2(a) and 2(b). **And for each of `ARCHITECTURE.md` and `docs/llm_integration.md`, a search for the
symbol `␠` (U+2420) returns zero hits; one hit means the symbol was typed instead of two spaces, and is fixed before the
commit.** *(★ ADDED 2026-11-07 at the check (point C5).)* Then the commit, exactly the three files, by explicit path, proved (count 3). Subject:
`docs: ARCHITECTURE.md section 19 and docs/llm_integration.md marked superseded by the 2026-11-07 language-model
ruling; the 2026-08-08 route record noted`. Push; verify `origin/master`. **This commit is `<T2>`.**

**2(d) — the capture after `<T2>`**, as 1(e), the regeneration commit's subject `artifacts: regenerated after the
superseded banners`.

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

**Search first: if this text occurs more than once in the file, use instead the whole of line 72557 as `old_string`
and the same line with the bracket appended as `new_string`, and declare it.** `new_string`:

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
(lines 30465–30466). `old_string`:

```
— the defense of keeping the fields of Row 21.102.
```

**Search first: if this text occurs more than once in the file, use instead the whole of line 30466 as `old_string` and
the same line with the bracket appended as `new_string`, and declare it.** `new_string`:

```
— the defense of keeping the fields of Row 21.102. [★ ANNOTATED 2026-11-07 under Ruling 1 item 6 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_correction_sitting.md`, the wording kept (#12): the language-model half of this defense no longer holds, because Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_07_llm_test_only_sitting.md` supersedes `docs/llm_integration.md`. The other half, the Authoritative Chord Symbol Mode (§4.1f), stands. Row 21.102's proposed QUARANTINED is not changed.]
```

**Proof of 3(a) to 3(c):** each file's line count before and after, equal; `git diff --numstat`: **L2 `2	2`, L0/L1 `1	1`,
L3 `1	1`**; each changed line read back by its line number (72468, 72557, 10142, 30466) with the file tools. A changed line
at any other number is a STOP-and-report. Then the commit, exactly the three files, by explicit path, proved (count 3).
Subject: `records: the reading files' language-model descriptions annotated under the 2026-11-07 correction`. Push;
verify `origin/master`. **This commit is `<T3>`.**

**3(d) — the capture after `<T3>`**, as 1(e), the regeneration commit's subject `artifacts: regenerated after the
reading-file annotations`.

**E3:** four in-line annotations, no line added, `<T3>` pushed; every new red traced to Task 3 and handled by A2's rule.

---

## Task 4 — the close (written out in full; no earlier dispatch is read)

**4(a) — the `STATUS.md` entries FIRST**, at the top, above the previous batch's close entry: one pointer entry per
committed task — **the close entry first**, naming this dispatch by its file name
(`records/cc/instructions/cc_instruction_llm_correction_2026_11_07.md`) and carrying the `Last updated: ` prefix; then
the entries of Tasks 3, 2, 1 and 0 below it, in that order, each opening `Same dispatch`; in the OI-222 pointer
convention, the whole of each being your report; no value restated (D-431); each entry a separate paragraph, separated
by one blank line, in the shape of the entries at lines 8 and 10. **★ THE PREFIX IS MOVED, NOT COPIED, AND THE MOVE IS
COMPLETE BEFORE 4(b) RUNS:** in the same act remove `Last updated: ` — and nothing else — from the previous batch's close
entry (now at line 8); read `STATUS.md` after the edit and confirm exactly one line carries `Last updated: `. **The close
entry says in plain words:** that this batch applied Ruling 1 items 1 to 6 of the 2026-11-07 correction record — seven
register entries superseded by the 2026-11-07 language-model ruling and two noted, the two design texts marked
superseded, the 2026-08-08 route record noted, the three reading files annotated — every text kept; **no tool edited or
added but the forward-bound tool's re-aiming; no algorithm change; no new decisions-register entry, no `D-NNN`, no
open-items row**; and that the whole is the report. **Then the search:** case-insensitive, every term of `L3_KEYWORDS`
(read 5 of the first read) plus *repeat* and *tie*, each as a substring, over `STATUS.md` — **expected: hits only inside
the paraphrase paragraph**; any other hit is reworded at your own new entries and the search re-run; report the hits as
found.

**4(b) — the forward bound.** Read `tools/audit/gen_status_batch_bound.py` at the object
`7c2d1bccc885b1e11204727f0800ffe20fd84b21:tools/audit/gen_status_batch_bound.py` first (a scratch file, searched for its
constants) and **report its authored constants as you find them**. **Expected, RELAYED** (the previous dispatch's 4(b)
instruction, not read at the tool by the writing side): `BASE_COMMIT` `113b2ce680e527e81342d8f79d5acbad281334d7`,
`PREVIOUS_BATCH_DISPATCH` `cc_instruction_boot_chain_landing_2026_11_02.md`, `DISPATCH`
`cc_instruction_records_landing_2026_11_07.md`, `TASK` `Task 3`, `MOVE_KIND` `ordinary`, `ACT_DATE` 2026-11-07. A
difference is reported and 4(b) proceeds from what the object holds. **Re-aim all of them:**
- `BASE_COMMIT` — this batch's last task commit before the close: `<T3>`, or the last regeneration commit after it if
  3(d) made one. **Check that the `STATUS.md` blob at `BASE_COMMIT` equals its blob at the start tip, each `git rev-parse`
  in its own command.**
- `PREVIOUS_BATCH_DISPATCH` — `cc_instruction_records_landing_2026_11_07.md`.
- `DISPATCH` — `cc_instruction_llm_correction_2026_11_07.md`. `TASK` — `Task 4`. `MOVE_KIND` stays `ordinary`.
  `ACT_DATE` — the day the move runs.
- Append this batch's aiming to `PREVIOUS_AIMINGS` in the shape of the rows above it (the previous batch's aiming is
  already its last row — do not append it twice); amend the head comments as the previous batches did, each former value
  named, not deleted (#12).

**Then `--apply` and `--check`, each in its own call.** **Prediction: exactly the previous batch's TWO entries move** —
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
3. `gen_derivation_boot_pack.py --check` — expected GREEN unless 1(e), 2(d) or 3(d) recorded it red by this batch; the
   manifest is NOT regenerated here in either case.
4. **LAST, after the final edit to `STATUS.md` and after `gen_session_start_read_size.py` has been regenerated:**
   `python tools/audit/gen_per_session_reading.py` (write mode; its `--check` red before), then `--check` GREEN.

**Each moved artifact is diffed against its blob at `<T3>` (or the last regeneration commit)** between explicit blob
hashes, by a scratch script quoted whole in the appendix, **and every changed passage is accounted for.** Expected:
`session_start_read_size.json` — the `STATUS.md` member, the total and the comparisons built on the total;
`defense_share.json` — the whole-read denominator and the share against it; `per_session_reading.json` — the ordinary
read's `STATUS.md` member and every sum and mirror that includes it, and **in `the_cowork_boot_chain`, the three latest
handoff entries (name the three, as the tool orders them, and say how any tie at `<T0>` was broken) and the sums that
include them**. **Any other movement is reported by field.**

**4(d) — THE REPORT, IN THE TWO-FILE FORM OF RULING 4 OF THE 2026-11-01 RECORD.** That ruling's words (RELAYED from the
previous dispatch; read the 2026-11-01 record if the wording matters to a step): *"a Claude Code report is written in two
files, committed in the same commit: the REPORT PROPER — the ordered first read, the capacity judgments, every task's
account, every claim, grade, declared departure, finding and observation, every check's verdict, and for every scripted
search its terms, its hit count and the rows named — and a separate APPENDIX FILE beside it, named in the report with its
path, its size and the searches it holds, carrying the raw printouts verbatim (every hit line as the search printed it)
and nothing the report proper needs."*
- **The report proper**, `records/cc/reports/cc_report_llm_correction_2026_11_07.md`: your first tool call named exactly;
  your account of what reached you as injected context; the eight-line check with each line as read and as injected; a
  capacity judgment; Tasks 0 to 4, each with what it did and every check's verdict — **for each capture its header line,
  its counts, its failing set by name, and every line that differs from the capture before it**; **for every tool newly
  red at 1(e), 2(d) or 3(d): its cause as printed, the source line that reads the edited file, and whether it was
  regenerated or carried**; 0(c)'s enumeration against the landing set and A1; 0(d)'s result; 1(a)'s output and 1(c)'s
  accounting; every `--numstat`; the commits in a table (task, commit, parent, the number of committed blobs); 4(b)'s
  constants as found and as set and `the_moved`; 4(c)'s moved values per artifact; E0 to E4 and A1 to A5 graded (E5 and
  A4/A5 at Task 5); declared departures; observations met and not acted on; **a short paragraph on whether this dispatch
  could be executed without reading any earlier dispatch, and if not, which step sent you to one**; **the list of tools
  carried red by this batch, as questions for the writing side**; and **the tell in one sentence: did this batch produce
  anything other than the landing set, the edited set, the artifacts A2 and 4(c) regenerated, the Task 4 files, the
  report and its appendix, the away-returns section, the end state's guard artifact — and, outside the repository,
  scratch files and loose blob objects? If yes, name it.**
- **The appendix**, `records/cc/reports/cc_report_llm_correction_2026_11_07_appendix.md`, beside it: the raw printouts
  verbatim, each under a heading naming its command and step — A1's enumeration whole, 0(d)'s script and output, 1(a)'s
  script and output, 1(b)'s outputs, 1(c)'s diff, every `--numstat`, every capture whole, every regeneration diff, the
  4(b) apply and the four archive checks, every 4(c) check and diff whole. **The report proper names the appendix with
  its path, its size in bytes and the list of what it holds.**

**4(c′) — THE LAST REGENERATION, after 4(d) has written the report and its appendix in their final form and before
4(e).** Run `python tools/audit/gen_per_session_reading.py` (write mode) once more, then `--check` GREEN, and diff the
artifact against the one 4(c) left: **expected, only `the_reports_with_an_appendix_beside_them`: `count` one higher, the
two sums higher by this batch's two sizes, and one added pair naming `cc_report_llm_correction_2026_11_07.md`.** Anything
else is reported and is a STOP before 4(f). **After this run neither the report nor its appendix is edited again**; the
run's output and its diff go in the away-returns section of 4(e), not in the report.

**4(e) — the close section appended to `records/cowork/handoff/cowork_away_returns.md`**, headed **THE LANGUAGE-MODEL
CORRECTION OF 2026-11-07 — RULING 1 ITEMS 1 TO 6 APPLIED; DOCUMENTATION ONLY, NO ALGORITHM CHANGED**: the report's
content as pointers, 4(c′)'s output and diff, and **the plan line:** *"The next act is the writing side's — the check of
this batch's return at the objects; then L3 family 7's check (the language-model family surface)."* Read the file's last
section before appending, for its form; append only.

**4(f) — the close commit** carries `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`,
`tools/audit/status_batch_bound.json`, every artifact 4(c) and 4(c′) moved, the report, its appendix and
`records/cowork/handoff/cowork_away_returns.md` — by explicit path, the staged set proved with `changed_paths.py
--staged`. Subject: `Close: the language-model correction of 2026-11-07 - Ruling 1 items 1 to 6 applied, under its
dispatch`. Push; verify `origin/master` at the ref file. **Held back:** A1's four standing items, the standing untracked
population, any handoff entry that appeared during the run, every scratch file. **The close does not assert the end
state**; Task 5 carries it.

**E4:** at the tree carrying the close, every check 4(b) and 4(c) name green; `gen_guard_state.py`'s own artifact stale
until Task 5; nothing outside A4 changed.

---

## Task 5 — the end state

- **The run:** `python tools/audit/gen_guard_state.py` (write mode, named) at the tree the close commit left, its output
  saved whole. **The condition:** run **83**; zero STOPs in the runner; **the failing set exactly the thirteen plus the
  tools carried red by this batch at 1(e), 2(d) and 3(d), named, none other**; `gen_per_session_reading.py --check`,
  `gen_decisions_register.py --check` (as the runner names it) and `gen_l3_outgoing_population.py --check` PASS unless
  carried; the NOT RUN and HISTORICAL lines identical to the opening capture's; against the opening capture **the
  verdicts that differ are exactly `gen_per_session_reading.py --check` FAIL → PASS and the carried tools PASS → FAIL**.
  Then `python tools/audit/gen_guard_classification.py --check`, its STOP naming the same five tools as at 0(f) — a
  further name is a STOP-and-report.
- **The verification at the objects:** `git diff --name-status 7c2d1bccc885b1e11204727f0800ffe20fd84b21 <the close
  commit>`, every path accounted for against A4 and the landing set, **every file A5 names absent from it** (the landing
  set's own files appear once, as additions).
- **The record:** append the end-state portion to this batch's section of `records/cowork/handoff/cowork_away_returns.md`
  — the run's header, counts and failing set by name, the comparison with the opening capture, the classification STOP,
  the name-status list's counts by status and every path by name, A4 and A5 graded, the close commit's hash. Commit
  `tools/audit/guard_state.json` and that file only, by explicit path, the staged set proved. Subject: `End state: the
  language-model correction of 2026-11-07 - guard run at the close tree`. Push; verify `origin/master` at the ref file.

**E5:** the condition held at a fresh run committed only after the run that produced it.

**THIS BATCH ENDS HERE.**

---

## What this batch does NOT do

- **No algorithm change; no measurement of the analysis.** The edited design texts are marked superseded, not
  rewritten; their text stays.
- **Ruling 1 item 7 is not applied** — Ruling 57 clause (ii), Ruling 62 item 11, the DESIGN-INTENT seed list, the
  document's membership of the specification document set, and the four leak-check records stay as they are.
- **No text moves out of any governing document**; `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS_ARCHIVE.md` and
  `cowork_audit_protocol.md` are not edited; `DECISIONS.md` changes only by regeneration.
- **No tool edited or added** but the forward-bound tool's re-aiming. No guard enrolment changes; no classification
  verdict is authored; **no pinned value is re-pinned.**
- **No line is added to or removed from any file Tasks 1 to 3 edit.**
- **No new decisions-register entry, no `D-NNN`, no open-items row; no earlier report corrected.**
- **A1's four standing items are not touched.**

## What this batch deliberately leaves to later acts, named so it is not lost

- **The tools carried red by this batch**, if any — their re-pinning is the writing side's question, put to the user if
  the record does not answer it.
- **The register's home anchors** for D-440 to D-448 (`ARCHITECTURE.md` and `docs/llm_integration.md` line ranges) do
  not move, because no line is added; whether a superseded entry's home should point elsewhere is not decided here.
- **L3 family 7's check** (the language-model family surface) — the writing side's, after this batch's return is
  verified.
- **What the scope document leaves open** (correction record §2): its §3D (places not searched: `src/`, the `docs`
  sub-folders, `DECISIONS.md` beyond the rows read) and §7 item 3 (a search of the whole rulings folder).
- **The three standing modifications of A1** — the user's, when the externally compiled list of research, software and
  algorithms is taken up.
- **Carried, unchanged:** the measurement tool's boot-chain block after the 2026-11-02 Ruling 1; the three-latest pick by
  name where add-commit times tie; the classification tool's five unauthored verdicts; the decisions register's drifted
  home anchors.

---

## The writing side's self-check over this dispatch (recorded, per the standing clause; D-434)

*Written by the writing side after the draft, before its check at its sources; the check runs in a turn of its own and
is recorded in the next section.*

- **Read at the objects this sitting**, through staged copies and the file tools: both ref files; `STATUS.md` whole;
  `DECISIONS.md` at D-599's row; the gating artifact at its counts; the correction record whole; the boot-chain record
  whole; the previous dispatch lines 1–500 (for its form; this dispatch sends no one to it);
  `tools/audit/decisions/gen_decisions_register.py` lines 14–27, 80–99, 418–532 and 560–629;
  `tools/audit/decisions/backbone_decisions.json` at lines 1908–1919 and 9340–9429, and by search for every
  `"status"` and `"superseded_by"` line; `ARCHITECTURE.md` lines 8086–8100; `docs/llm_integration.md` lines 1–8;
  `docs/llm_triage_design.md` lines 1–6; the route record lines 30–39; the L2 reading file lines 72463–72470 and
  72555–72591; the L0/L1 reading file lines 10141–10143; the L3 reading file lines 30463–30466.
- **Not read:** any guard tool's inputs (hence A2's rule instead of a prediction); `gen_status_batch_bound.py`,
  `gen_per_session_reading.py`, `gen_guard_state.py`, `changed_paths.py`, `gen_guard_classification.py`; the data file
  at D-443 to D-448 beyond their `id` and `status` lines (their `status_source` lines are found by the script, which
  STOPs if one is not as expected); whether the three `old_string`s of 3(a) item 1 and 3(c) are unique in their files
  (the dispatch has Claude Code search first, with a fallback); the L2 member's lines 72466–72467 and 72469 beyond what
  is quoted; `CLAUDE.md`; `DECISIONS.md` beyond D-599's row; any git object.
- **Self-sufficiency (D-251) and Ruling 2 of the 2026-11-02 record:** every act has its exact text or command, a
  prediction or a rule, and a stop; the close and end state are written out and cite no earlier dispatch; standing
  clauses are left to the protocol section the first read orders.
- **Known weakness, for the check:** A2 does not predict the reds of Tasks 1 to 3. The check should judge whether the
  rule is enough, or whether the writing side should first read the guard tools that take `DECISIONS.md`,
  `ARCHITECTURE.md`, `docs/llm_integration.md` or the reading files as inputs.

## This file's check at its sources (D-434; runs in a turn of its own)

**NOT YET RUN.** The next Cowork session runs it, in a turn of its own: coherence, completeness, correctness and
overstatement, each claim of the premise ledger at its object, corrections at their sites with former wordings kept
(#12), recorded here; then the banner is set to RELEASED.

**★ RUN IN PART, 2026-11-07 — the Cowork sitting booted on handoff entry 572.** That line above is the former wording,
kept (#12). Read at the objects through staged copies and the file tools; no shell, no git command.

- **Read and found as stated:** both ref files at `7c2d1bcc…`; `STATUS.md` whole (10,680 bytes, the entries at lines 8,
  10, 12, 14, one `Last updated: `); entries 570 and 571 at 6,607 and 7,932 bytes in the handoff folder's listing.
  The data file at D-440 to D-448's `id`, `status` and `status_source` lines by a search of those keys (every line
  number of the premise ledger found as stated; one `status_source` line per entry), and D-443's object whole (lines
  9427–9463): its `status_source` is one line, six spaces, opening `"status_source": "` and ending `",`, as 1(a)'s
  script expects. The precedent at 1903 (`"status": "superseded-by"`) and 1917 (`"superseded_by": "D-001"`, the
  object's last key). The generator at lines 34–35, 90–91, 284, 425–426, 444–457, 486–487, 607–608. Each `old_string`
  of Tasks 2 and 3 searched as exact text in its staged file: one occurrence each, at `ARCHITECTURE.md` (the 2(a)
  three-line text), `docs/llm_integration.md` (2(b)), the route record line 37 (2(c)), the L2 reading file lines 72468
  and 72557 (3(a)), the L0/L1 reading file line 10142 (3(b)), the L3 reading file line 30466 (3(c)); so the fallbacks
  of 3(a) and 3(c) will not be needed. `gen_status_batch_bound.py` in the working tree: `BASE_COMMIT`
  `113b2ce680e527e81342d8f79d5acbad281334d7` (line 2486), `PREVIOUS_BATCH_DISPATCH`
  `cc_instruction_boot_chain_landing_2026_11_02.md` (2718), `ACT_DATE` `2026-11-07` (3007), `DISPATCH`
  `cc_instruction_records_landing_2026_11_07.md` (3008), `TASK` `Task 3` (3274), `MOVE_KIND` `ordinary` (3281), so
  4(b)'s relayed constants hold at the working tree (4(b) still reads them at the start tip's object).
- **C1 — A2's rule against a prediction: NOT SETTLED; the reason the dispatch is not released.** `guard_state.json`
  enrols about thirty tools under `tools/audit/decisions/` (lines 12–41 of its list), among them
  `gen_r1_superseded_reach.py`, `gen_home_classification.py`, `gen_cluster_dispositions.py`,
  `gen_verbatim_subject_consistency.py` and `gen_phase1w_legacy_verification.py`; their inputs were not read. A tool
  that lists entries by status would see seven entries enter a superseded set at 1(e), which A2 makes a
  STOP-and-report with `<T1>` already pushed and Tasks 2 to 4 not run. Separately, the outgoing-population tools
  term-search the specification documents; whether the 2(a) banner's words in `ARCHITECTURE.md` add a hit (a member
  entering, again a STOP) was not checked. The rule is safe (it stops rather than corrupts) but likely to stop the
  batch part-way. **To settle before release:** read, narrowly, which enrolled tools take
  `backbone_decisions.json`, `DECISIONS.md`, `decisions/group_N.md`, `ARCHITECTURE.md`, `docs/llm_integration.md`,
  the route record or the reading files as inputs, and for each whether it regenerates, is pinned, or counts a
  population the edits change; then predict the reds at 1(e), 2(d) and 3(d) by name, or change the order of Tasks 1
  to 3 if that keeps a part-way STOP from leaving the register and the design texts out of step.
- **C2 — corrected:** the first read, 0(c)(i), 0(d) and 0(e)'s subject named entry 572 as the last possible entry.
  The checking sitting's own entry 573 would have been an untracked handoff path outside the landing set, a STOP at
  0(c). Each site now names every entry above 571.
- **C3 — corrected:** 1(c) expected the data file's sha256 line in `DECISIONS.md` to change. The generator prints the
  stored value from `cluster_dispositions.json`'s header, so that line does not change.
- **C4 — the 1(a) script, read line by line:** the edit adds no line; `superseded_by` goes on the status line,
  not as the object's last key as in the precedent. The two are equal as JSON and the generator reads parsed data.
  Whether any enrolled tool checks the data file's text form (key order or one key per line) is part of C1.
  `16	16` for the numstat is consistent with seven status lines and nine `status_source` lines.
- **C5 — corrected:** the `␠␠` convention. Added to the proof of 2(a) to 2(c): a search for `␠` in the two files
  must return zero (it returns zero at the staged copies today).
- **Overstatement sweep** over this dispatch's absolutes was not run; it is owed with C1.

**★ CONTINUED 2026-11-07 — the Cowork sitting booted on handoff entry 573.** Read at the objects through staged copies
and the file tools; no shell, no git command. Both ref files still at `7c2d1bcc…`; this file at 63,325 bytes when
staged before these edits.

- **C1 — settled in part; A2 amended.** The tools of `guard_state.json`'s derived list (lines 9–99) were staged, all but
  `gen_status_batch_bound.py` and `output_encoding.py`, and searched for the edited files' names and for the status values. Found at the objects:
  `tools/audit/decisions/gen_r1_superseded_reach.py` (passing at the start state, `summary.failing_tools` at
  `guard_state.json` lines 1647–1726 not naming it) re-derives its artifact from the working-tree register and counts
  entries per superseded status (lines 553–560, 571–574, 779–797), so it goes newly FAIL at 1(e), and its regeneration
  moves members of a count and possibly of a list: under A2's former wording a STOP after `<T1>` was pushed, with Tasks
  2 to 4 not run. `tools/audit/gen_l2_outgoing_population.py` records whole-file byte sizes (line 380) and, with
  `gen_l3_outgoing_population.py`, reads the reading files' `## 10.` sections (lines 128, 556; 187–194). Reordering
  Tasks 1 to 3 was considered and not taken: a STOP after the banners and before the register would leave the two out of
  step the other way. **Correction:** A2's regenerate branch now treats a member entering or leaving as tied, and so not
  a STOP, only where the member is one of the ruled entries or the change is a size, line count, hash or hit of a file
  the task edited, at the edited line; and A2 names the reds found. The writing side did not read every tool that takes
  the register or the edited documents as input; the rule covers those not named.
- **C4 — not settled by this sitting.** These searches looked for file names and status values, not for a check of the
  data file's key order or one-key-per-line form. It stays open and is covered by A2's rule (an unexplained red is a
  STOP).
- **C6 — corrected:** A5 named every file under `tools/audit/decisions/` but the data file as byte-unchanged, which
  contradicted A2's regeneration of an artifact in that folder. A5 now excepts artifacts A2's rule regenerates.
- **Still owed before release:** the overstatement sweep over this dispatch's absolutes; then the banner set to
  RELEASED, the file landed and proved.

**★ COMPLETED 2026-11-07 — the Cowork sitting booted on handoff entry 574.** Read at the objects through staged copies
and the file tools; no shell, no git command. Both ref files still at `7c2d1bcc…`; this file at 69,157 bytes when staged
before these edits; A2, A5 and this section read; C1 not redone.

- **The overstatement sweep.** A search for *every, all, none, only, never, exactly, complete* (any case) over this
  file, each hit read at its line. Most hits are instructions to Claude Code (what to commit, what to stop on) or
  predictions it tests, and were left. Hits stating a fact were tested at their objects:
  - Line 21's and the 2(a)/2(b) banners' *"only while the software is being developed, never at run time"*, and the
    1(a) script's *"never used at run time in the finished product"*: as the user's words read at the test-only ruling
    record's lines 25–26 and its plain-terms paragraph (lines 32–35). Left.
  - **Corrected — the 3(a) annotation** (L2 reading file, line 72468): *"a language model may only give a second
    opinion when the product is tested"* was wider than the user's condition (the test-only record, lines 28–29: *"when
    we test our product, and our product struggles with inference"*). Now *"…when the product is tested and struggles
    with inference"*. Former wording (#12): *"may only give a second opinion when the product is tested."* The
    annotation stays inside its one line.
  - **Corrected — "ONE RULE FOR EVERY TEXT EDIT IN THIS BATCH"** and *"no line number cited anywhere in the record
    moves"*: Task 4(a) adds `STATUS.md` entries and Task 4 writes new files. Narrowed to Tasks 1 to 3, former wording
    kept at the site.
  - **Corrected — "Documentation only: everything this batch edits"**: 4(b) re-aims a tool's constants. Narrowed, former
    wording kept at the site.
  - Line 128 (*exactly one line carries `Last updated: `*): as found at `STATUS.md` by this sitting. 4(b)'s *"exactly the
    previous batch's TWO entries move"*: `STATUS.md`'s entries at lines 8 and 10 are the previous batch's two, read.
    The check section's *"Each site now names every entry above 571"*: the sites found by a search for *above 571* are
    the first read's item 3, 0(c)(i), 0(d), and 0(e) by `<N>`. Left.
  - Not re-established by this sweep, and so not claimed: the self-check's *"every act has its exact text or command, a
    prediction or a rule, and a stop"* (the writing side's own assessment); A1's *"exactly three"* and the start state's
    *"thirteen"* (stated for Claude Code to establish at its boot).
- **Staleness fixed** (the user's rule of 2026-09-22): the banner's list of handoff entries the writing side writes after
  this dispatch, and 0(c)(i)'s list of entries written, now run to entry 575; former wordings kept at the sites.
- **C4 stays open**, covered by A2's rule (an unexplained red is a STOP).
- **The banner is set to RELEASED.**
