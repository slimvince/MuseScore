# CC dispatch — LANDING: HANDOFF ENTRY 477 (AND 478), THE 2026-11-02 BOOT-CHAIN RULING RECORD, AND ITS AMENDMENT PARAGRAPH INSERTED INTO ENTRY 291 §4 STEP 3 — DOCUMENTATION ONLY; NO ALGORITHM CHANGE (2026-11-02)

> **STATUS: RELEASED 2026-11-02**: written, checked at its sources in a turn of its own, corrected and released by the
> Cowork sitting booted on `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_seven.md`. The check is
> recorded at the end of this file with every former wording. *(Former wording of this banner's first sentences,
> preserved (#12): "**STATUS: WRITTEN 2026-11-02 — NOT YET RELEASED** by the Cowork sitting booted on `…_seventy_seven.md`.
> Its check at its sources runs in a turn of its own; this banner is set to RELEASED only after that check, which is
> recorded at the end of this file with every former wording. **Until then this dispatch is NOT handed to Claude
> Code.**")* It is executed by Claude Code when the user
> hands it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that
> step and report it. Do not continue to the next one.**
>
> **THE WRITING SIDE'S RESTRAINT, declared.** Once released this dispatch is final. The writing side will not touch it,
> nor any file it names, while this batch runs. The one file the writing side writes after this dispatch lands and before
> hand-over is its handoff entry `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_eight.md`, which
> is why Task 0 states no size for it. **This dispatch, entry 477, entry 478 and the ruling record are NOT in git**; Task 0
> lands them.

## What this batch is, in plain words

On 2026-11-02 the user gave two rulings, recorded in
`records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md` (called ***the record*** below):

- **Ruling 1 ("B")** — a new Cowork session reads its start-up chain (handoff entries 118, 152, 169 and 291) only at
  named sections, not as whole entries. The record quotes one paragraph to be inserted into entry 291 §4 step 3 by a
  Claude Code dispatch, the wording above it kept. **Task 1 inserts it.**
- **Ruling 2 ("A")** — from this dispatch on, a dispatch points to a standing clause by its section only where the clause
  lives in a file Claude Code reads at every batch (in practice the dispatch-protocol section of `cowork_audit_protocol.md`),
  and **never sends Claude Code through a chain of earlier dispatches**: what it needs from one, it states itself. **This
  dispatch is written that way.** Its close (Task 3) and end state (Task 4) are written out in full below; no step of
  this batch requires reading any earlier dispatch.

**Documentation and algorithm, separated.** **Documentation only:** the landed records; one paragraph inserted into one
handoff entry; the forward-bound tool's re-aiming; the artifacts the close regenerates; `STATUS.md`, `STATUS_ARCHIVE.md`;
this batch's report, appendix and away-returns section. **Algorithm: NOTHING changes.** No specification of the analysis
is touched or read; no measurement of the analysis is run. The currently decided method for L3 is `FRAMEWORK.md` §5's L3
block with DP-I, untouched and unread. **This batch decides nothing.**

---

## ★ THE ORDERED FIRST READ

**★ YOUR FIRST TOOL CALL IS ONE READ OF THIS FILE, AND NOTHING ELSE IN THAT CALL.** Do not read `STATUS.md`,
`DECISIONS.md`, `CLAUDE.md` or anything else in that call, and do not issue any other read in parallel with it. If the
read returns a partial view at the tool's page limit, read this file whole in further ranges of the same file before
anything else, and declare it.

**Then the eight-line check of Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`**
(the user's ruling that the injected copy of `CLAUDE.md` stands for the file-tool read of its six session-start spans):
read at the tree with the file tools, each located by search, **the first line of `CLAUDE.md`, the heading line of each of
its six session-start spans, and its last line carrying text**, and compare each with the copy injected into your
context. The last run found them at lines 1, 3, 313, 488, 704, 1536, 1985 and 1994 (RELAYED,
`records/cc/reports/cc_report_per_session_reading_extension_2026_11_02.md` §1; `CLAUDE.md` is 170,510 bytes at this
side's staging, the size that run left). **If every line is identical, the six-span read is not performed. If a line
differs or is missing, read the six spans with the file tools and report it as a finding.** Report the eight lines as
read and as injected.

Then, in this order:

1. `STATUS.md` whole; `DECISIONS.md` whole; `BUILD_AND_TEST.md` whole; `gating_ids` at
   `tools/audit/nongating_apparatus_rows.json`.
2. `cowork_audit_protocol.md` from the line `## The dispatch protocol these audits are commissioned and run under` to the
   end of the file, whole. **Its marked standing clauses bind this batch and are not restated here.**
3. **The record whole** (7,636 bytes at the rulings folder's listing).
4. **Handoff entries 477 and 478 whole.** **Entry 478 is the current handover block** (the standing clause on the
   current handover block). If entry 478 is not on disk, entry 477 is, and you say so.
5. **Entry 291** (`records/cowork/handoff/cowork_handoff_entry_two_hundred_and_ninety_one.md`, 9,725 bytes) at its §4,
   from the line `## 4. What happens next — who does what, in this order` to the line before `## 5.`.
6. `tools/audit/gen_l3_outgoing_population.py` at its `L3_KEYWORDS` list, located by search (for 3(a)'s search).

**Not read, and not needed:** any earlier dispatch or report; `FRAMEWORK.md`; the derivation; the L3 reading file.
Declare any further read you make.

---

## ★ WORDS USED IN THIS DISPATCH, EXPLAINED FIRST

- ***The start tip*** — `f01c88747e7fe5719d79e63f9a1d2f3d3622bcfa`, the commit both ref files named when this dispatch was
  written (the end state of the per-session reading extension batch).
- ***The previous batch*** — the batch run under `records/cc/instructions/cc_instruction_per_session_reading_extension_2026_11_02.md`.
  It is named only so the forward bound (3(b)) can move its `STATUS.md` entries; **you do not read it.**
- ***`<T0>`, `<T1>`*** — this batch's Task 0 and Task 1 commits. ***`<ACT_DATE>`*** — the day the step runs, `YYYY-MM-DD`.
- ***The amendment paragraph*** — the four lines the record quotes under its heading *"The amendment to entry 291 §4 step
  3"*, reproduced exactly in Task 1(b).
- ***A capture*** — the output of `python tools/audit/gen_guard_state.py --check`, saved whole to a scratch file outside
  the repository and read. ***Compared verdict by verdict*** means every tool's PASS / FAIL / NOT RUN / HISTORICAL line
  side by side, and the tally line.

---

## Ruling ledger

- **Ruling 1 of the record, as the record states it:** *"From the next Cowork session on, the start-up chain is read at
  these sections only, each located by a heading search, and not as whole entries"*; and *"the next Claude Code dispatch
  applies this amendment with the file-editing tool, at its Task 0 or a task of its own, inserting the paragraph below
  directly after the last line of step 3 (the line ending "It proves this entry's, the record's and the surface's sizes
  at a listing."), at step 3's indentation, the wording above it untouched"*.
- **Ruling 2 of the record** — the dispatch form above. *"It moves no text, edits no existing dispatch or protocol clause,
  and adds no tool."*
- **Ruling 4 of the 2026-11-01 record** — the report's two-file form (3(d) states it).
- **No new rule is made.**

---

## Premise ledger (written 2026-11-02 by the writing side from staged working-tree copies read with the file tools; no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
  `f01c88747e7fe5719d79e63f9a1d2f3d3622bcfa`.
- **FACT — the chain**, read at `.git/logs/HEAD` lines 2097 to 2101: `08274008d07b7e102a692f59eaedb0905860c39f` →
  `dd06b5fea97a0f7e1fee4ffa35b7aebdc704ebd5` (Task 0) → `db25a104f8aa1c7c75903f68a2f905ecd9f88ce7` (Task 1) →
  `37d8ebb68f60a62f01b1f618288fd95a8a9a6512` (Task 2) → `7016ca9f8652234414022bceae48b2d687befd3c` (the close) →
  `f01c8874…` (the end state); no line after 2101.
- **FACT — `STATUS.md`** (11,766 bytes, read whole): the previous batch's FOUR entries at lines 8, 10, 12 and 14 — its
  close entry carrying `Last updated: `, then its Task 2, Task 1 and Task 0 `Same dispatch` entries; the two 2026-09-02
  entries at 16 and 18; the archive-pointer paragraphs at 20, 22, 24 and 26, the one at 22 being the standing paragraph
  that holds the word *paraphrase* (called ***the paraphrase paragraph*** below). Exactly one line carries `Last updated: `.
- **FACT — the guard state at the start tip**, as entry 477 §1 records it at `tools/audit/guard_state.json` → `summary`:
  run 83, passing 70, failing 13. **RELAYED** (`records/cc/instructions/cc_instruction_pruning_rulings_execution_2026_11_01.md`'s
  premise ledger; entry 477 checked the count, not the names): the thirteen are `gen_phase3_gate_partition.py`,
  `gen_filing_convention_application.py`, `gen_artifact_inventory.py`, `gen_artifact_inventory_surface.py`,
  `gen_test_construction_evidence.py`, `gen_retirement_caller_check.py`, `decisions/apply_soft_discard.py`,
  `decisions/apply_residue_discard.py`, `gen_epoch_write_path.py`, `gen_recognizer_establishment_sort.py`,
  `decisions/gen_cluster_dispositions.py` (its `--verify`), `decisions/gen_home_classification.py`,
  `decisions/gen_phase1p_delegation_bar.py`; and `python tools/audit/gen_guard_classification.py --check` exits 2 naming
  FIVE tools — `gen_l0_l1_outgoing_population.py`, `gen_l2_withheld_documents.py`, `gen_l3_outgoing_population.py`,
  `gen_withheld_family_reading.py`, `gen_per_session_reading.py`. **Read `guard_state.json` at the start tip yourself at
  0(f); the object is the value of record.**
- **FACT — the evidence-pin membership** at the staged `tools/audit/evidence_pin_membership.json`: `ruling_records_read`
  **171**, `members` **7**. Its tool (RELAYED from the 2026-11-01 first pruning dispatch's premise ledger; the tool was not
  read by this side) counts every ruling record on disk under `records/cowork/rulings/` and names a member only by a
  document under `ratification_surfaces/` named in a record, or by a tool named on a line carrying the word PINNED. **The
  record carries neither** (a case-insensitive search of it for `pinned` and for `ratification_surfaces`
  returned no hit). **Prediction:** the regeneration moves `ruling_records_read` 171 → 172 and adds the record's path to
  its list, and nothing else; `members` stays 7.
- **FACT — entry 291 at the staged copy:** 9,725 bytes, LF line endings (no carriage return in it). Its line 91 is
  `   proves this entry's, the record's and the surface's sizes at a listing.` — the only line of the file containing
  `sizes at a listing.`; line 92 opens step 4 (`4. **It writes the paper sizing`). The word `AMENDED` does not occur in it.
- **FACT — `tools/audit/gen_per_session_reading.py`** sizes entry 291 WHOLE as a member of `the_cowork_boot_chain` (its
  member row, lines 781–783 of the staged tool, takes `len(read(ENTRY_291))`; the tool's anchors, lines 195–198, are in
  entries 118 and 152 only), and takes the three handoff entries with the latest add-commits from its handoff population
  (line 707), whose builder STOPs on a member with no add-commit (line 365). **So:** Task 1's
  insertion moves entry 291's member value; Task 0's landing of entries 477 and 478 moves the three latest entries; and
  the tool's check is red from Task 0 until its regeneration, LAST, at 3(c).
- **NOT KNOWN TO THIS SIDE — whether any tool other than `gen_per_session_reading.py` reads or pins entry 291.** Task 1(a)
  establishes it before the edit.
- **ASSUMPTION A1 — the working tree, stated by CONTENT.** Tracked modifications at your boot: **exactly one**,
  `tools/audit/claude_md_finer_archive.json` — standing, carried and not chased (RELAYED, the previous batch's report §9,
  A1 held). **This side wrote no tracked file.** Untracked and landed by Task 0: this dispatch, the record, entry 477 and,
  if it exists, entry 478 — **three or four untracked paths** beyond the standing untracked population, which is not
  landed and is not a STOP. **Your enumeration with `tools/audit/changed_paths.py` establishes A1.** A further untracked
  `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` appearing during the run is the writing side's, NOT landed; see the
  start state.
- **ASSUMPTION A2 — the reds, by cause.**
  - **At your boot, before Task 0:** `gen_per_session_reading.py --check` is expected to STOP (exit 2) — entries 477 and
    478 sit untracked in the handoff folder and the tool STOPs on a member with no add-commit; `gen_evidence_pin_membership.py
    --check` RED — the record is on disk, untracked. Do not run the full guard set before Task 0.
  - **The opening capture (0(f), after `<T0>`):** run 83; zero STOPs in the runner; the thirteen FAIL and
    `gen_per_session_reading.py --check` FAILS (cause: the landed entries change the three latest), and nothing else.
  - **Task 1:** the capture after the insertion is IDENTICAL to the opening capture, verdict by verdict.
  - **Task 3:** `gen_session_start_read_size.py --check` and `gen_defense_share.py --check` RED after 3(a) (both read
    `STATUS.md`), regenerated; `gen_l3_outgoing_population.py --check` expected RED — its `STATUS.md` residue record
    carries the paraphrase paragraph's line number, and 3(a)/3(b) move that line (four entries leave, three arrive; two if
    Task 1 was not committed) — regenerated, moving only line values inside that residue record;
    `gen_l0_l1_outgoing_population.py --check` expected GREEN (the 2026-11-01 first pruning dispatch predicted green for
    the same kind of move; whether that held was not read by this side), and RED allowed, regenerated under the same
    limit;
    `gen_per_session_reading.py` regenerated LAST and again at 3(c′).
  - **A red A2 does not name, met at Task 1's capture, reverts Task 1** (Task 1(d)); met at the close or end state, it is
    reported and graded, NOT regenerated.
- **ASSUMPTION A3** — no `src/` file, build, test, golden, corpus of scores or measurement of the analysis is touched.
- **ASSUMPTION A4 — THE FOOTPRINT.** **Task 0:** the landed files and `tools/audit/evidence_pin_membership.json`.
  **Task 1:** in entry 291, the four inserted lines of Task 1(b) — nothing else. **Task 3:** `STATUS.md`,
  `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py` at its authored aiming and head comments,
  `tools/audit/status_batch_bound.json`, the artifacts 3(c) and 3(c′) regenerate, the report and its appendix,
  `records/cowork/handoff/cowork_away_returns.md`. **Task 4:** `tools/audit/guard_state.json` and the away-returns
  end-state portion.
- **ASSUMPTION A5 — byte-unchanged by this batch:** `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS.md`,
  `DECISIONS_ARCHIVE.md`, `cowork_audit_protocol.md`, `FRAMEWORK.md`, `OPEN_ITEMS.md`, `BUILD_AND_TEST.md`; every tool
  under `tools/audit/` but `gen_status_batch_bound.py`; every file under `tools/audit/decisions/` and
  `tools/audit/derivation_boot_pack/`; every ruling record but the one Task 0 lands; every handoff entry but entry 291 and
  the ones Task 0 lands; every dispatch and report but this batch's own.

## The declared start state — at the tree you will meet

1. Both ref files at the start tip; the one standing modification of A1; this dispatch, the record, entry 477 and entry
   478 (which may be absent) untracked; nothing running.
2. The thirteen failing tools — standing reds, none of them this batch's — and the classification's five-name STOP.
3. `gen_per_session_reading.py --check` STOPs at your boot (A2) — run it before Task 0 only to record this. **If it is
   instead RED or GREEN, report what it printed; that is not a STOP.**
4. `gen_evidence_pin_membership.py --check` RED at your boot (A2) — regenerated inside Task 0.

**A further untracked handoff entry or ruling record appearing during the run:** do not land it; if it makes
`gen_per_session_reading.py` STOP at 3(c), do not regenerate that artifact, report the STOP with its message, and carry the
tool as red into the end state.

## Findings in this batch

**No finding number is allocated.** A finding met during the run is written up on its own in the report and surfaced,
never absorbed.

---

## Task 0 — land the records, and PUSH

- **0(a) — the pin.** `git hash-object -w --no-filters` of this dispatch, in its own call; record its blob and
  `git cat-file -s`; re-hash immediately before staging, equal or STOP.
- **0(b) — the refs and the chain.** Read both ref files with the file tools against the FACT; then `git cat-file -p
  f01c88747e7fe5719d79e63f9a1d2f3d3622bcfa` (expected parent `7016ca9f8652234414022bceae48b2d687befd3c`) and `git cat-file
  -p 7016ca9f8652234414022bceae48b2d687befd3c` (expected parent `37d8ebb68f60a62f01b1f618288fd95a8a9a6512`), each hash
  written literally in its own command. A different chain is a STOP-and-report with nothing committed.
- **0(c) — A1**, by `python tools/audit/changed_paths.py` (the sanctioned enumeration; `git status` is not used, D-253):
  exactly the one standing modification; the landing paths untracked; other untracked paths only the standing population.
  Anything else is reported and is a STOP.
- **0(d) — last bytes** of each landing file, at its blob written `--no-filters`: the object's last 70 bytes and its count
  of zero bytes. Each ends with a newline after a complete line and holds no zero byte; a final line broken off mid-word,
  or a zero byte, is a STOP-and-report. **Expected sizes:** the record 7,636; entry 477 8,286 (both at this side's
  listings). **No size is stated for this dispatch or entry 478**; report all.
- **0(e) — the evidence-pin regeneration, then the commit.** `python tools/audit/gen_evidence_pin_membership.py --check`
  in its own call (expected red — start state 4); `python tools/audit/gen_evidence_pin_membership.py` (write mode, the
  bare invocation); `--check` again, expected green. `git hash-object -w` the new artifact and take `git diff <its blob at
  f01c88747e7fe5719d79e63f9a1d2f3d3622bcfa> <the new blob>` between the two explicit blob hashes into a scratch file:
  **predicted** — `ruling_records_read` 171 → 172 and the one path
  `records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md` added to its list, nothing else; `members`
  stays 7. **A movement of any member, route or state is a STOP-and-report.** Then the commit, exactly these paths and no
  other, staged by explicit path, the staged set proved with `python tools/audit/changed_paths.py --staged`:
  - `records/cc/instructions/cc_instruction_boot_chain_landing_2026_11_02.md` (this dispatch; new)
  - `records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md` (new)
  - `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_seven.md` (new)
  - `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_eight.md` (new; only if it exists at your boot)
  - `tools/audit/evidence_pin_membership.json`

  Subject, exactly: `record: entries 477 and 478, the 2026-11-02 boot-chain ruling record and its landing dispatch` — or,
  if entry 478 is NOT at your boot, `record: entry 477, the 2026-11-02 boot-chain ruling record and its landing dispatch`,
  its absence reported; do not wait for it. Push; read `.git/refs/remotes/origin/master` and verify it equals the new tip.
  **This commit is `<T0>`.**
- **0(f) — the opening capture.** A capture, saved whole and read. Read the start tip's `tools/audit/guard_state.json` →
  `summary` at the object (`git show f01c88747e7fe5719d79e63f9a1d2f3d3622bcfa:tools/audit/guard_state.json`). Then
  `python tools/audit/gen_guard_classification.py --check`, expected exit 2, a STOP naming the five tools of the premise
  ledger — report them by name; a different set is a STOP-and-report. **The failing set must be A2's.** Anything else is
  reported and is a STOP.

**E0:** the named paths in one commit, pushed; the pin proved; A1 reported with its enumeration; the evidence-pin movement
exactly as predicted; the opening capture as A2 states it; the five-name STOP.

---

## Task 1 — INSERT THE AMENDMENT PARAGRAPH INTO ENTRY 291 §4 STEP 3

- **1(a) — who else reads entry 291.** `git grep -n "cowork_handoff_entry_two_hundred_and_ninety_one" -- tools/` in its
  own call; report every hit. **Expected:** hits in `tools/audit/gen_per_session_reading.py` (its `ENTRY_291` constant and
  uses) and possibly in generated artifacts that record its size (`tools/audit/per_session_reading.json`). **A hit in any
  other tool's source is a STOP-and-report before the edit**: name the tool and what it does with the file, read at its
  text; nothing is edited.
- **1(b) — the edit, with the file-editing tool (not a shell command, not a script).** In
  `records/cowork/handoff/cowork_handoff_entry_two_hundred_and_ninety_one.md`, find the line
  `   proves this entry's, the record's and the surface's sizes at a listing.` — **found exactly once, or STOP** — and
  insert directly after it, before the line opening `4. **It writes the paper sizing`, exactly these four lines (three
  spaces, `>`, one space, then the text; LF line endings like the rest of the file):

  ```
     > ★ AMENDED 2026-11-02 by Ruling 1 of `records/cowork/rulings/cowork_rulings_2026_11_02_boot_chain_sitting.md` (the
     > user's word: "B"). The start-up chain is now read at these sections, each located by a heading search, not as whole
     > entries: entry 118, the first paragraph of "THE BRIDGE FAULT"; entry 152, item (vi); entry 169, its "Boot" block and
     > "The cadence for your session"; this entry, §3 and §4. The wording of step 3 above is the former wording, kept (#12).
  ```

  (The fence above is this dispatch's, not part of the text, **and so are the two spaces of this list item's indentation
  that stand in front of every line inside it.** Each inserted line begins with exactly three spaces — step 3's
  indentation — then `>`, one space, then the text. The words after each `> ` are the record's four quoted lines (its
  lines 61 to 64), character for character.) **Nothing else in the file changes.**
- **1(c) — the proof, by search and by size.** With the file tools: the text `★ AMENDED 2026-11-02 by Ruling 1` found
  exactly once, on the line directly after the anchor line; the text `kept (#12).` found exactly once, on the line directly
  before the step-4 line; the anchor line and every line above it unchanged. Then compare the four inserted lines with the
  record's four quoted lines (each with its leading `> ` removed on both sides) by a scratch script quoted whole in the
  appendix: **equal, or STOP and revert**. `git diff --stat` of the file against `<T0>`: **one file, four insertions, no
  deletion.** Report the file's new size (`git hash-object --no-filters` and `git cat-file -s` after `-w`).
- **1(d) — the capture.** A capture, compared verdict by verdict with the opening capture: **IDENTICAL** (A2). **If it
  differs:** do NOT commit; revert the four lines with the file-editing tool; prove the file's `git hash-object
  --no-filters` equal to its blob at `<T0>`; report the differing verdict whole with its cause as you establish it at the
  tool's text (D-669); and go to Task 3 with Task 1 not committed.
- **1(e) — the commit**, the one path staged by explicit path, the staged set proved with `changed_paths.py --staged`.
  Subject: `Entry 291 step 3: insert the 2026-11-02 amendment paragraph (Ruling 1 of the boot-chain record)`. Push; verify
  `origin/master` at the ref file. **This commit is `<T1>`.**

**E1:** the four lines inserted exactly, nothing else changed, the capture identical, one commit, pushed.

---

## Task 2 — none

*(There is no Task 2. This batch has two tasks of work, 0 and 1; the close and the end state are numbered 3 and 4 as
written here. No step is missing.)*

---

## Task 3 — the close (written out in full; no earlier dispatch is read)

**3(a) — the `STATUS.md` entries FIRST**, at the top, above the previous batch's close entry: one pointer entry per
committed task — **the close entry first**, naming this dispatch by its file name
(`records/cc/instructions/cc_instruction_boot_chain_landing_2026_11_02.md`) and carrying the `Last updated: ` prefix; then
Task 1's and Task 0's entries below it, newest first, each opening `Same dispatch`; in the OI-222 pointer convention, the
whole of each being your report; no value restated (D-431); each entry a separate paragraph, separated by one blank line,
in the shape of the entries at lines 8 to 14. **★ THE PREFIX IS MOVED, NOT COPIED, AND THE MOVE IS COMPLETE BEFORE 3(b)
RUNS:** in the same act remove `Last updated: ` — and nothing else — from the previous batch's close entry (now at line 8);
read `STATUS.md` after the edit and confirm exactly one line carries `Last updated: `. **The close entry says in plain
words:** that this batch landed handoff entries 477 and 478 and the user's ruling record of 2026-11-02 on the Cowork
start-up chain and the dispatch form; that it inserted the record's amendment paragraph into handoff entry 291 §4 step 3,
the wording above it kept; that this dispatch is the first written under that record's Ruling 2 (it points to standing
clauses by section and sends no one through earlier dispatches); **no tool edited or added but the forward-bound tool's
re-aiming; no algorithm change; no decisions-register entry, no `D-NNN`, no open-items row**; and that the whole is the
report. Where a task was not committed, it says which and why, and there is no entry for it. **Then the search:**
case-insensitive, every term of `L3_KEYWORDS` (read 6 of the first read) plus *repeat* and *tie*, each as a substring,
over `STATUS.md` — **expected: hits only inside the paraphrase paragraph**; any other hit is reworded at your
own new entries and the search re-run; report the hits as found.

**3(b) — the forward bound.** Read `tools/audit/gen_status_batch_bound.py` at the object
`f01c88747e7fe5719d79e63f9a1d2f3d3622bcfa:tools/audit/gen_status_batch_bound.py` first (a scratch file, searched for its
constants) and **report its authored constants as you find them** (RELAYED, the previous batch's report §6 3(b), the
values it set: `BASE_COMMIT` `37d8ebb68f60a62f01b1f618288fd95a8a9a6512`, `PREVIOUS_BATCH_DISPATCH`
`cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md`, `DISPATCH`
`cc_instruction_per_session_reading_extension_2026_11_02.md`, `TASK` `Task 3`, `MOVE_KIND` `ordinary`, `ACT_DATE`
2026-11-02; a difference is reported and 3(b) proceeds from what the object holds). **Re-aim all of them:**
- `BASE_COMMIT` — this batch's LAST TASK COMMIT before the close (`<T1>`, or `<T0>` if Task 1 was not committed).
  **Check that the `STATUS.md` blob at `BASE_COMMIT` equals its blob at the start tip, each `git rev-parse` in its own
  command.**
- `PREVIOUS_BATCH_DISPATCH` — `cc_instruction_per_session_reading_extension_2026_11_02.md`.
- `DISPATCH` — `cc_instruction_boot_chain_landing_2026_11_02.md`. `TASK` — `Task 3`. `MOVE_KIND` stays `ordinary`.
  `ACT_DATE` — the day the move runs.
- Append this batch's aiming to `PREVIOUS_AIMINGS` in the shape of the rows above it (the previous batch's aiming is
  already its last row — do not append it twice); amend the head comments as the previous batches did, each former value
  named, not deleted (#12).

**Then `--apply` and `--check`, each in its own call.** **Prediction: exactly the previous batch's FOUR entries move** —
its close entry (from which 3(a) removed the prefix) and its Task 2, Task 1 and Task 0 `Same dispatch` entries, at the
base's lines 8, 10, 12 and 14; the two 2026-09-02 entries stay; no STOP. Name the entries that moved, read at the
artifact's `the_moved`. **If the tool STOPs:** establish its cause first (D-669); if the cause is 3(a)'s prefix move
incomplete, complete it, re-run the search and the tool, and declare it; for any other cause, restore the tool's passing
aim, re-run it green, report the STOP with its message, and move nothing by hand. **No correction line is inserted in
`STATUS_ARCHIVE.md`.** After the move, the four checks that read the archive, each in its own call, each exit 0 expected,
each output kept: `python tools/audit/gen_status_batch_bound.py --check`, `python tools/audit/gen_governing_surface_split.py
--check --pair STATUS.md`, `python tools/audit/gen_status_residue_move.py --check`, `python
tools/audit/gen_status_archive_pass.py --check`.

**3(c) — the regenerations**, each check first in its own call, then each red one regenerated (write mode, the bare
invocation) and checked again, all exit 0:
1. `gen_evidence_pin_membership.py --check` — expected GREEN (regenerated at Task 0), not regenerated.
2. `gen_session_start_read_size.py` and `gen_defense_share.py` — both expected RED (the `STATUS.md` member), regenerated.
3. `gen_l3_outgoing_population.py --check` (expected RED, A2) and `gen_l0_l1_outgoing_population.py --check` (expected
   GREEN) — each regenerated only if red; **if regenerated, only line values inside its `STATUS.md` residue record may
   move.** A member of either
   population, or of `the_tabulation_population`, moving is a STOP-and-report.
4. `gen_derivation_boot_pack.py --check` — expected GREEN; the manifest is NOT regenerated.
5. **LAST, after the final edit to `STATUS.md` and after `gen_session_start_read_size.py` has been regenerated:**
   `python tools/audit/gen_per_session_reading.py` (write mode; its `--check` red before), then `--check` GREEN.

**Each moved artifact is diffed against its blob at the start tip** (the evidence-pin artifact against `<T0>`) between
explicit blob hashes, by a scratch script quoted whole in the appendix, **and every changed passage is accounted for.**
Expected: `session_start_read_size.json` — the `STATUS.md` member, the total and the comparisons built on the total;
`defense_share.json` — the whole-read denominator and the share against it; `per_session_reading.json` — the ordinary
read's `STATUS.md` member and every sum and mirror that includes it (both sides of `totals_by_side`,
`under_ruling_2_of_2026_11_01`, the imported denominator `the_two_denominators` →
`the_whole_ordinary_session_start_read` and the share computed from it); **in `the_cowork_boot_chain`, entry 291's
`characters` (Task 1) and the three latest handoff entries (Task 0's landing — name the three, as the tool orders them)
and the sums that include them**; and nothing of the arc populations, the invariant shares, `the_appendices_beside_them`,
`the_reports_with_an_appendix_beside_them` (this batch's own pair is not yet there) or table 2's spans. **Any other
movement is reported by field.**

**3(d) — THE REPORT, IN THE TWO-FILE FORM OF RULING 4 OF THE 2026-11-01 RECORD.** That ruling's words (RELAYED: quoted as
`records/cc/instructions/cc_instruction_pruning_rulings_execution_2026_11_01.md` 3(d) quotes them; the 2026-11-01 record
was not read by this side — read it there if the wording matters to a step): *"a Claude Code
report is written in two files, committed in the same commit: the REPORT PROPER — the ordered first read, the capacity
judgments, every task's account, every claim, grade, declared departure, finding and observation, every check's verdict,
and for every scripted search its terms, its hit count and the rows named — and a separate APPENDIX FILE beside it, named
in the report with its path, its size and the searches it holds, carrying the raw printouts verbatim (every hit line as
the search printed it) and nothing the report proper needs."*
- **The report proper**, `records/cc/reports/cc_report_boot_chain_landing_2026_11_02.md`: your first tool call named
  exactly; your account of what reached you as injected context; the eight-line check with each line as read and as
  injected; a capacity judgment; Tasks 0, 1 and 3, each with what it did and every check's verdict — **for each capture
  its header line, its counts, its failing set by name, and every line that differs from the capture before it**; 1(a)'s
  hits; 1(c)'s proof; the commits in a table (task, commit, parent, the committed blobs); 3(b)'s constants as found and as
  set and `the_moved`; 3(c)'s moved values per artifact; E0, E1, E3 and A1 to A5 graded (E4 and A4/A5 at Task 4);
  declared departures; observations met and not acted on; **a short paragraph on the ordered reads against the work —
  whether this dispatch's close and end state could be executed without reading any earlier dispatch, and if not, which
  step sent you to one** (the effect Ruling 2 of the record asks to be observed); and **the tell in one sentence: did this
  batch produce anything other than the landed records, entry 291's four lines, the Task 3 files, the regenerated
  artifacts, the report and its appendix, the away-returns section, the end state's guard artifact — and, outside the
  repository, scratch files and loose blob objects? If yes, name it.**
- **The appendix**, `records/cc/reports/cc_report_boot_chain_landing_2026_11_02_appendix.md`, beside it: the raw printouts
  verbatim, each under a heading naming its command and step — A1's enumeration whole, every capture whole, the scratch
  scripts and their outputs, the 3(b) apply and the four archive checks, every 3(c) check and diff whole. **The report
  proper names the appendix with its path, its size in bytes and the list of what it holds.**

**3(c′) — THE LAST REGENERATION, after 3(d) has written the report and its appendix in their final form and before
3(e).** `gen_per_session_reading.py` sizes every report of `records/cc/reports/` that has an appendix beside it, so this
batch's pair joins `the_reports_with_an_appendix_beside_them` the moment both files exist. Run `python
tools/audit/gen_per_session_reading.py` (write mode) once more, then `--check` GREEN, and diff the artifact against the one
3(c) left: **expected, only that block: `count` one higher, the two sums higher by this batch's two sizes, and one added
pair naming `cc_report_boot_chain_landing_2026_11_02.md`.** Anything else is reported and is a STOP before 3(f). **After
this run neither the report nor its appendix is edited again**; the run's output and its diff go in the away-returns
section of 3(e), not in the report.

**3(e) — the close section appended to `records/cowork/handoff/cowork_away_returns.md`**, headed **THE BOOT-CHAIN
LANDING — ENTRIES 477 AND 478 AND THE 2026-11-02 RULING RECORD LANDED; THE AMENDMENT PARAGRAPH INSERTED INTO ENTRY 291;
DOCUMENTATION ONLY, NO ALGORITHM CHANGED** (where a task was not committed, the heading says which and why): the report's
content as pointers, 3(c′)'s output and diff, and **the plan line:** *"The next act is the writing side's — the check of
this batch's return at the objects; then step 5, the method ruling's surface over the completed L3 tabulation (Ruling 4
of `records/cowork/rulings/cowork_rulings_2026_08_24_comparison_design_sitting.md`)."* Read the file's last section before
appending, for its form; append only.

**3(f) — the close commit** carries `STATUS.md`, `STATUS_ARCHIVE.md`, `tools/audit/gen_status_batch_bound.py`,
`tools/audit/status_batch_bound.json`, every regenerated artifact that moved, the report, its appendix and
`records/cowork/handoff/cowork_away_returns.md` — by explicit path, the staged set proved with `changed_paths.py
--staged`. Subject: `Close: the boot-chain landing - entries 477 and 478, the 2026-11-02 ruling record, the entry 291
amendment, under its dispatch`. Push; verify `origin/master` at the ref file. **Held back:**
`tools/audit/claude_md_finer_archive.json`, the standing untracked population, every scratch file. **The close does not
assert the end state**; Task 4 carries it.

**E3:** at the tree carrying the close, every check 3(b) and 3(c) name green; `gen_guard_state.py`'s own artifact stale
until Task 4; nothing outside A4 changed.

---

## Task 4 — the end state

- **The run:** `python tools/audit/gen_guard_state.py` (write mode, named) at the tree the close commit left, its output
  saved whole. **The condition:** run **83**; zero STOPs in the runner; the failing set exactly the thirteen, none added;
  `gen_per_session_reading.py --check`, `gen_evidence_pin_membership.py --check` (ruling-record count **172**),
  `gen_derivation_boot_pack.py --check` and `gen_l3_outgoing_population.py --check` PASS; the NOT RUN and HISTORICAL
  lines identical to the opening capture's; against the opening capture **exactly one verdict differs:
  `gen_per_session_reading.py --check` FAIL → PASS**. Then `python tools/audit/gen_guard_classification.py --check`, its
  STOP naming the same five tools as at 0(f) — a further name is a STOP-and-report.
- **The verification at the objects:** `git diff --name-status f01c88747e7fe5719d79e63f9a1d2f3d3622bcfa <the close
  commit>`, every path accounted for against A4 and the Task 0 files, **every file A5 names absent from it**.
- **The record:** append the end-state portion to this batch's section of `records/cowork/handoff/cowork_away_returns.md`
  — the run's header, counts and failing set by name, the comparison with the opening capture, the classification STOP,
  the name-status list, A4 and A5 graded, the close commit's hash. Commit `tools/audit/guard_state.json` and that file
  only, by explicit path, the staged set proved. Subject: `End state: the boot-chain landing - guard run at the close
  tree`. Push; verify `origin/master` at the ref file.

**E4:** the condition held at a fresh run committed only after the run that produced it.

**THIS BATCH ENDS HERE.**

---

## What this batch does NOT do

- **No algorithm change; no specification of the analysis touched; no measurement of the analysis.**
- **No text moves out of any governing document**; `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `DECISIONS.md`,
  `DECISIONS_ARCHIVE.md` and `cowork_audit_protocol.md` are not edited.
- **No tool edited or added** but the forward-bound tool's re-aiming. No guard enrolment changes; no classification
  verdict is authored. `gen_per_session_reading.py` still sizes entries 118, 152, 169 and 291 as its authored text says;
  whether its boot-chain block should follow Ruling 1 is not this batch's question (named below).
- **No entry 291 text changes but the four inserted lines.** No other handoff entry is edited.
- **No decisions-register entry, no `D-NNN`, no open-items row; no earlier report corrected.**

## What this batch deliberately leaves to later acts, named so it is not lost

- **Step 5** — the method ruling's surface over the completed L3 tabulation: the writing side's, after this return is
  verified.
- **The measurement tool's boot-chain block after Ruling 1** — `the_cowork_boot_chain` still sizes entry 169 and entry
  291 whole, while a Cowork session now reads them at named sections; the writing side's observation, not acted on.
- **Carried, unchanged:** the fourth pruning report's observation (a) (table 2 classes the decision-surface block as
  carrying a former wording); the previous report's observation (b) (the three latest handoff entries are picked by name
  where add-commit times tie); the five ★ questions the derivation marks for the user; the classification tool's five
  unauthored verdicts; the decisions register's drifted home anchors.

---

## The writing side's self-check over this dispatch (recorded, per the standing clause; D-434)

*Written by the writing side after the draft, before its check at its sources; the check runs in a turn of its own and
is recorded in the next section.*

- **Read at the objects this sitting**, through staged copies and the file tools: the ref files; `.git/logs/HEAD` at
  lines 2097 to 2102; `STATUS.md` whole; the record whole; entries 477, 476 and 291 whole; entry 118 at lines 27–51,
  entry 152 at 55–69, entry 169 at 26–43 and 293–328; `cowork_audit_protocol.md` at lines 180–314 and its `#` headings;
  the previous dispatch at lines 1–265 and 658–817; the previous report at lines 20–99, 494–543 and 753–848; the first
  pruning dispatch at lines 258–497 and 850–999; `evidence_pin_membership.json` by search; `gen_per_session_reading.py`
  by search for its anchors; the handoff, rulings and `records/cowork` listings.
- **Not read:** the 2026-11-01 pruning ruling record; `DECISIONS.md`, `CLAUDE.md` (the user narrowed this sitting's boot), `gen_status_batch_bound.py`,
  `gen_guard_state.py`, `changed_paths.py`, `gen_evidence_pin_membership.py`, `gen_l3_outgoing_population.py`, the
  fourth pruning dispatch, `cowork_away_returns.md`, any git object.
- **Self-sufficiency (D-251) and Ruling 2 of the record:** every act has its exact text or command, a prediction and a
  stop; the close and end state are written out and cite no earlier dispatch; standing clauses are left to the protocol
  section the first read orders.

## This file's check at its sources (D-434; runs in a turn of its own)

*Run by the writing side in the turn after the draft landed, at staged copies with the file tools.* **Held at the
source:** the four amendment lines, text after `> `, equal to the record's lines 61 to 64; the two quotations of Ruling 1
and the one of Ruling 2 at the record (lines 38–39, 56–59, 99); entry 291's line 91 (the only `sizes at a listing.`),
its line 92 and its LF endings; `STATUS.md`'s lines 8 to 26; the chain at `.git/logs/HEAD` 2097–2101; the record's and
entry 477's sizes at their listings; the evidence-pin counts (171, 7) and the record's search for `pinned` and
`ratification_surfaces` (no hit); the measurement tool at lines 199–200, 356–365, 707 and 778–798. **Four corrections,
each at its site; former wordings:**

1. **Task 1(b), content.** The four lines sit inside this dispatch's list item, so each carries two extra spaces of
   indentation in the file, and a reader copying them would insert five spaces where step 3's indentation is three.
   Former wording: *"(The fence above is this dispatch's, not part of the text. The words after each `> ` are the record's
   four quoted lines, character for character; the three leading spaces are step 3's indentation.)"*
2. **3(d), a quotation marked as read that was not.** The Ruling 4 quotation was taken from the first pruning dispatch,
   not from the 2026-11-01 record. Former wording: *"That ruling's words: "*, with no relay mark.
3. **Premise ledger, the evidence-pin tool's routes**, stated as fact though the tool was not read. Former wording: *"Its
   tool counts every ruling record on disk under `records/cowork/rulings/` and names a member only by a document under
   `ratification_surfaces/` named in a record, or by a tool named on a line carrying the word PINNED."*
4. **Premise ledger, the measurement tool**: the line range cited mixed path constants with anchors, and the folder-listing
   and STOP claims rested on a relay; both are now cited at the tool's lines. Former wording: *"(no anchor inside it; its
   authored anchors are in entries 118 and 152 only, lines 194 to 200 of the staged tool), and lists
   `records/cowork/handoff` from the file system to find the three entries with the latest add-commits."*

Also added to the self-check's not-read list: the 2026-11-01 pruning ruling record. **No step, prediction or stop
changed but item 1's wording.**
