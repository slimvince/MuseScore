# CC dispatch — THE PRUNING ITERATION, STEP 4: RULING 1 CARRIED OUT A FOURTH TIME, WITH THE L3 DERIVATION BOOT PACK FROZEN FIRST — BY CITATION TO THE THIRD DISPATCH; DOCUMENTATION AND ONE MEASUREMENT-TOOL TABLE ONLY; NO ALGORITHM CHANGE, NO DECISIONS-REGISTER ENTRY (2026-11-02)

> **STATUS: RELEASED 2026-11-02**: written, checked at its sources in a turn of its own, corrected and released by the
> Cowork sitting booted on `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_four.md`. The check is
> recorded at the end of this file with every former wording. *(Former wording of this banner's first sentences,
> preserved (#12): "**STATUS: WRITTEN 2026-11-02 — NOT YET RELEASED** by the Cowork sitting booted on `…_seventy_four.md`.
> Its check at its sources runs in a turn of its own; this banner is set to RELEASED only after that check, which is
> recorded at the end of this file with every former wording. **Until then this dispatch is NOT handed to Claude
> Code.**")* It is executed by Claude Code when the user
> hands it over (D-252); the Cowork writing side never runs it. **If any expected result does not appear, stop at that
> step and report it. Do not continue to the next one, and do not resolve an exclusion that contradicts a task.**
>
> **THE WRITING SIDE'S RESTRAINT, declared.** Once released this dispatch is final. The writing side will not touch it,
> nor any file it names, while this batch runs. The one file the writing side writes after this dispatch lands and before
> hand-over is its handoff entry `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_five.md`, which is
> why Task 0 states no size for it. **Entries 472, 473, 474 and 475 and this dispatch are NOT in git**; Task 0 lands them.

## What this batch is, in plain words

On 2026-11-01 the user ruled four things in `records/cowork/rulings/cowork_rulings_2026_11_01_pruning_iteration_sitting.md`.
**Ruling 3 is committed** (by the third dispatch, commit `f630b1eb09b2a0c395a94ff2b99b6b5d7936b43c`). **Ruling 1 is not**:
two bracketed former wordings in `CLAUDE.md`'s decision-surface block are still to move verbatim to `CLAUDE_ARCHIVE.md`.

Three dispatches have tried Ruling 1. The third,
`records/cc/instructions/cc_instruction_pruning_rulings_third_execution_2026_11_01.md` — **called *the third dispatch*
below** — made the move, reconciled it and confined it exactly as predicted, and then reversed it, because the full guard
capture showed `tools/audit/gen_derivation_boot_pack.py --check` turning red, which no dispatch predicted. Its report,
`records/cc/reports/cc_report_pruning_rulings_third_execution_2026_11_01.md` — **called *the third report*** — gives the
cause at the tool's own text (§4): the L3 derivation boot pack is the one pack not frozen, and its member
`l3/02_the_guiding_principles_and_the_conventions.md` re-renders `CLAUDE.md`'s guiding-principles and Conventions spans
live, so any edit inside those spans turns the check red.

**This batch first FREEZES the L3 pack (Task 1), then runs the third dispatch's Ruling 1 steps again by citation (Task 2).**
Why freeze rather than regenerate is settled from the record, not asked (handoff entry 474 §1, a derivation under D-599):

- the tool's own rule — its docstring paragraph opening *"AND, SINCE 2026-08-31, A SPENT SUBJECT IS FROZEN RATHER THAN
  RE-RENDERED"*, which cites Ruling 17(a) of `cowork_rulings_2026_08_31_decision_surface_sitting.md` and states, in the
  docstring's own words: *"A subject whose deriving session HAS RUN is SPENT: its pack is no longer an input to be kept
  current, it is the RECORD OF WHAT THAT SESSION WAS GIVEN."* D-646 is the ruled shape;
- the fact — L3's deriving session has run: `cowork_blind_derivation_l3_2026_10_17.md` and the released brief were landed
  by `records/cc/instructions/cc_instruction_l3_derivation_commit_2026_10_17.md` (the away-returns section *"THE L3 BLIND
  DERIVATION COMMITTED"*);
- re-rendering would put a `CLAUDE.md` text dated 2026-11-02 into the record of what a session that ran by 2026-10-17 was
  given (#12) — the ground the tool records for `l0-l1` and `l2`.

**Documentation and algorithm, separated as the user requires.** **Documentation:** `CLAUDE.md`, `CLAUDE_ARCHIVE.md`,
`STATUS.md`, `STATUS_ARCHIVE.md`, this batch's records, and the artifacts the cited steps regenerate. **One measurement
tool's authored table:** the `FROZEN` table of `tools/audit/gen_derivation_boot_pack.py` gains an `l3` entry, and its
manifest `tools/audit/derivation_boot_pack.json` is regenerated. **Algorithm:** NOTHING changes; no specification of the
analysis is touched. The currently decided method for L3 is `FRAMEWORK.md` §5's L3 block with DP-I, untouched and
unread. **This batch decides nothing**: Ruling 1 is the user's ruling executed; the freeze applies Ruling 17(a) and D-646
to a subject whose session has run.

**Why a dispatch that cites another's task text is self-sufficient (D-251)** — as the third dispatch states it (its lines
52 to 55): the cited texts are fixed git objects you read yourself; **and every fork the third run met is carried INSIDE
this file**, which overrides every prediction of the third dispatch that its run refuted.

---

## ★ THE ORDERED FIRST READ (carries Ruling 2 of the 2026-11-01 record)

**★ YOUR FIRST TOOL CALL IS ONE READ OF THIS FILE, AND NOTHING ELSE IN THAT CALL.** Do not read `STATUS.md`,
`DECISIONS.md`, `CLAUDE.md` or anything else in that call, and do not issue any other read in parallel with it. If the
read returns a partial view at the tool's page limit, read this file whole in further ranges of the same file before
anything else, and declare it.

**Then, before anything else, take the three cited texts into scratch files**, each command in its own call, each hash
written literally, each scratch file named by its absolute path outside the repository:

- **The third dispatch:** `git rev-parse 749ab8c88a7e5221c73fcdc7d96a040c7fb3580b:records/cc/instructions/cc_instruction_pruning_rulings_third_execution_2026_11_01.md`
  (expected `6d59532fff7f64280e4daf3bc8cc588fd68d2acc` — RELAYED from the away-returns section of the third run), `git
  cat-file -s` of that blob (expected `41161`, this side's staging result of the working-tree file), then `git cat-file
  blob` of it redirected to a scratch file. **That scratch file is *the third dispatch*; every line number below that
  names the third dispatch is a line of it.** A blob other than `6d59532f…`, or a `bad object`, is a STOP-and-report. A
  size other than 41,161 is reported, not a STOP, provided `git hash-object` of the working-tree file equals the blob.
- **The second dispatch, as the third dispatch's first read orders it** (its lines 69 to 74): blob
  `abb7ef061d9f0ab922c935dfaa0157324eee8b14`, expected size `55136`. **That scratch file is *the second dispatch*.**
- **The first dispatch's text, as the third dispatch orders it** (its lines 75 to 77): blob
  `17d9d39c487079ba18fb6ba1380b8ad8750ca822`, expected size `102666`.

**Ruling 2's eight-line check — exactly as the second dispatch orders it**, which the third dispatch cites at its line 79.

Then, in this order:

- **(1) to (6)** As the third dispatch's items (1) to (6) (its lines 83 to 92), with one change to its item (4): **read
  the third dispatch at its lines 1 to 451 WHOLE** (through *"What this batch deliberately leaves to later acts"*; its
  self-check and its check at its sources are not read) in addition to the second dispatch's lines 1 to 562. **Its Task
  1 and Task 3 are this batch's Task 2 and Task 3, under the substitutions and overrides below. No step of any cited
  Task 2 (Ruling 3) is executed: Ruling 3 is committed.**
- **(7)** The handoff entries **474 and 475 whole** (`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_four.md`,
  `…_seventy_five.md`; landed by Task 0). **Entry 475 is the current handover block.**
- **(8)** **The third report at its §4, §6 and §8 whole**, and its appendix only where a step below names it.
- **(9)** As the third dispatch's items (8) and (9) (its lines 95 to 101), **without** item (8)'s addition for Task 2
  (the legacy-mark check is not touched by this batch).
- **(10)** **For Task 1:** `tools/audit/gen_derivation_boot_pack.py` at the docstring paragraph opening *"AND, SINCE
  2026-08-31, A SPENT SUBJECT IS FROZEN"* through the paragraph *"WHAT THE FREEZE DOES"*; the `FROZEN` table whole
  (from its preamble comment *"AUTHORED — the FROZEN table"* through the comment after the `l2` entry and the table's
  closing brace); `RENDERED_BEFORE_THE_SCOPING_RULINGS` and its preamble; the extras leak scan inside `build_subject`
  (from the comment *"LIMB B of Ruling 1"* through `rec["leak_checked"] = True`); `build()` from *"STOP 12's first limb"*
  through the loop that calls `frozen_from_disk`; and `verify_frozen`, `frozen_block`, `frozen_from_disk`, `write_all`
  and `check_all` whole. **Locate each by search before trusting any line number**; this side read them in the staged
  working-tree file (685,856 bytes), where the docstring paragraph begins at line 79, `FROZEN` at 369 and the five
  functions at 9201 to 9415.
- **(11)** As the third dispatch's item (10) (its line 102), with **the footprint A4 below** governing.

---

## ★ WORDS USED IN THIS DISPATCH, EXPLAINED FIRST

- ***The third dispatch / the second dispatch / the first dispatch's text / the third report*** — as defined above.
  ***The record*** — the 2026-11-01 ruling record; ***Ruling 1 … Ruling 4*** are its §1 to §4.
- ***The start tip*** — `1126176e2a4b48fc01bbb5b545210715366cb24a`, the commit both ref files named when this dispatch was
  written (the third run's end-state commit, RELAYED from handoff entry 472).
- ***`<T0>`*** — THIS batch's Task 0 commit. ***`<T1>`*** — this batch's Task 1 commit (the freeze).
- ***`<ACT_DATE>`*** — the day the step runs, written as `YYYY-MM-DD`.
- ***The L3 pack*** — the ten files of `tools/audit/derivation_boot_pack/l3/`. ***The manifest*** —
  `tools/audit/derivation_boot_pack.json`.
- ***Frozen / spent*** — as the tool's docstring defines them: a subject in the `FROZEN` table is not re-rendered; its
  pack directory is checked against recorded git blob hashes, and a mismatch is a STOP.
- Every other word — *a changed passage*, *the current commit*, *the two historical archive checks*, *their differing
  values*, *the two population tools*, *a byte-size value*, *the population confinement check* and its class (c) — as
  the third dispatch defines it (its lines 106 to 171), read under the substitutions below.

### ★ HOW THE CITED TEXTS ARE READ — the substitutions

The third dispatch's substitutions (its lines 119 to 136) apply, **with these changes, which apply to all three cited
texts:**

1. **Wherever any of them names its own file as the act that moves text**, write THIS dispatch's file name,
   `records/cc/instructions/cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md`, with the folder exactly where
   the cited text has one and without it where the cited text has none.
2. **Wherever any of them names its report as the place of a proof**, write this batch's report,
   `records/cc/reports/cc_report_pruning_rulings_fourth_execution_2026_11_02.md`.
3. **Wherever any of them names `c483c6968f2de0da68afeb47b48a8807dbe593ed`, `a18148e529cd9f50aeb831cb531bf8813a472eb4` or
   `e465d797b644a4ac7c58fd6430ff5b64ec658397` as the base a diff, a blob comparison or a tool read is taken against, or as
   the start tip, use the start tip of this batch**, `1126176e2a4b48fc01bbb5b545210715366cb24a` — **except in Task 2, where
   the base of every diff, blob comparison and confinement check is `<T1>`**, so that the freeze is not counted as a
   movement of Ruling 1.
4. **The cited Ruling 1 steps (the first dispatch's text's 1(a) to 1(i), run as the second and third dispatches order
   them) are this batch's Task 2.** They keep their cited labels in the report, under the heading of Task 2. Where a cited
   text says *"Task 1"* of its own batch, read *"Task 2"* of this batch.
5. **Nothing else in any cited text is changed except where a section below overrides a named step. Where this file and
   the third dispatch disagree, this file governs; where the third dispatch and the second dispatch disagree, the third
   governs; and so on down.**

---

## Ruling ledger

**The third dispatch's ruling ledger (its lines 175 to 186) governs Task 2 unchanged.** **For Task 1:** Ruling 17(a) of
`records/cowork/rulings/cowork_rulings_2026_08_31_decision_surface_sitting.md` as the tool quotes it (*"The two existing
packs are not re-rendered. They are frozen, and `--check` ranges over live subjects."*) and D-646, applied to `l3` by the
derivation recorded in handoff entry 474 §1 — the precedent being the `l2` freeze (dated 2026-10-15 in its `FROZEN`
entry, carried out by the batch of 2026-10-16), whose two records are
`records/cowork/rulings/cowork_rulings_2026_10_15_l2_freeze_derivation_sitting.md` and
`records/cowork/rulings/cowork_rulings_2026_10_16_l2_freeze_leak_list_sitting.md`. **No new rule is made.** If the user
overrules the derivation, the question goes to him; you do not decide it.

---

## Premise ledger (written 2026-11-02 by the writing side from staged working-tree copies read with the file tools; no git command was run by the writing side, so every identity only a git query gives is yours to take)

**The third dispatch's premise ledger (its lines 190 to 245, its FACT and NOT-KNOWN items) is carried for Task 2, read
under the substitutions, EXCEPT where an item below replaces it.** Its items on the legacy-mark check and on
`DECISIONS.md`'s values belong to Ruling 3 and are not used. Its assumptions A1 to A5 (its lines 247 to 267) are replaced
by A1 to A5 below, each of which says what of the third's it keeps.

- **FACT — the tip.** `.git/refs/heads/master` and `.git/refs/remotes/origin/master` both
  `1126176e2a4b48fc01bbb5b545210715366cb24a`, read as staged files.
- **RELAYED — the chain since the third dispatch**, from the away-returns section of the third run and its report §7:
  its Task 0 commit `749ab8c88a7e5221c73fcdc7d96a040c7fb3580b` (parent `c483c696…`); its Task 2 commit
  `f630b1eb09b2a0c395a94ff2b99b6b5d7936b43c`; its close commit `c7b6985a9c0be8fb7f975addf2fb0642c0311c29`; its end-state
  commit, the start tip. **Establish the chain yourself at 0(b).**
- **RELAYED — the guard state at the start tip**: *"83 guard(s) run, 13 failing, 4 not run, 20 historical record(s)"*
  (the away-returns end-state portion). **Read `1126176e…:tools/audit/guard_state.json` yourself; the object is the
  value of record.** By the third report §4, `gen_derivation_boot_pack.py --check` exits 0 at the tree Task 1's
  reversal left; it is expected GREEN at the start tip.
- **FACT — `STATUS.md`**, read at its first 25 lines (12,187 bytes at the staging result): the third dispatch's THREE
  entries at its lines 8, 10 and 12 — its close entry (carrying `Last updated: `), its Task 2 `Same dispatch` entry and
  its Task 0 `Same dispatch` entry; the two 2026-09-02 entries at 14 and 16; the archive pointers at 18, 20 and 22.
- **FACT — sizes at the staging results, in bytes:** `CLAUDE.md` 170,942 (handoff entry 474 §1); `STATUS.md` 12,187; the
  third dispatch 41,161; the third report 33,653; entries 472 7,300, 473 7,177 and 474 8,872 (the handoff folder's
  listing). `DECISIONS.md` 119,961 — RELAYED, entry 474 §1.
- **FACT — the class-(c) places in the L3 population artifact at the working tree**, by search of the staged
  `tools/audit/l3_outgoing_population.json`: four `"bytes": 170942` (lines 195, 267, 303, 33025) and
  `"summed_bytes_of_the_distinct_names_that_resolve": 844831` (line 36398) — the five places the third run measured,
  unchanged by its Task 2 and close. **The third dispatch's class (c) holds as written.**
- **FACT — neither population artifact names the boot-pack tool or its directory.** A search of the staged
  `l3_outgoing_population.json` and `l0_l1_outgoing_population.json` for `derivation_boot_pack` finds nothing. So Task 1's
  two edited files are not expected to move either population artifact — **a prediction checked at Task 1(f), not
  assumed.**
- **FACT — the freeze machinery, read at the staged tool.**
  - `write_all` writes the manifest always, and skips every subject in `FROZEN` (*"Nothing is written into a spent
    subject's directory"*). The subjects the tool builds are those of `WITHHELD`: `harmony-boundary`, `scoring-model`,
    `l0-l1`, `l2` and `l3`. **With `l3` frozen, write mode writes the manifest and NO pack file.**
  - `check_all` verifies a frozen subject by `verify_frozen` — the directory holds exactly the recorded files, each at
    its recorded blob hash, any mismatch a STOP — and prints the *"FROZEN SOURCES"* lines for files a re-render would
    produce at a different length, which *"sets no exit code"*.
  - `verify_frozen` STOPs on a freeze record missing its `finding`, its `date` or its `reason`.
  - `build()` still builds every subject in full, frozen or not; for a frozen subject it adds `★_FROZEN`
    (`frozen_block`) and re-points the member records' measured fields at the directory (`frozen_from_disk`): each
    member's `characters` measured at the file; each span's `lines_rendered`, each part's `characters`, and each
    filter's `the_text_removed`, `characters_removed`, `heading` and `closes_before` removed; `entries_rendered`,
    `rows_rendered` and `columns_kept` removed; the key `★_where_this_record's_measures_COME_FROM` added to each member
    record; `counted.files_in_the_pack` counted in the directory, and the key
    `★_which_of_these_counts_describe_the_DIRECTORY` added to `counted`.
  - The extras leak scan (`LEAKS_IN_THE_EXTRAS`, `counted.extras_lines_with_a_leak_hit`) runs for every subject not in
    `RENDERED_BEFORE_THE_SCOPING_RULINGS`, and for a FROZEN subject scans the files its directory holds (Ruling 1 of
    the 2026-10-16 record).
  - Where the tool tests membership of `FROZEN`: a search of it for `in FROZEN`, `set(FROZEN)`, `sorted(FROZEN` and
    `len(FROZEN` finds `build_subject`'s extras scan, `build()`'s two STOP checks and its loop, `write_all` and
    `check_all`, and nothing else. (The field choice and the `★_what_these_are` wording test
    `RENDERED_BEFORE_THE_SCOPING_RULINGS`, not `FROZEN`. `verify_frozen` and `frozen_block` read `FROZEN[subject]`
    for a subject already tested.) The bound is that search.
- **FACT — `l3` needs NO `RENDERED_BEFORE_THE_SCOPING_RULINGS` entry.** That list is for packs rendered before the
  2026-09-21 and 2026-09-27 rulings (its preamble). `VERDICT_DATE["l3"]` is `2026-10-15` (its comment: verdicts ruled
  2026-10-15), and the away-returns section *"THE L3 PACK BUILD, SECOND HALF, RESUMED"* records the pack RENDERED by that
  batch's Tasks 3 and 4 (`ca55115f…`), after `l2` was frozen. **So `l3` freezes with the three-field search and its
  extras leak scan, as it was built, and its manifest record is expected NOT to move except as `frozen_from_disk` and
  `frozen_block` move it.**
- **FACT — the L3 pack directory, at its listing:** exactly these ten files, every one with the same modification time
  (1792227966474 to 1792227966485 ms, i.e. 2026-10-16):
  `00_READ_THIS_FIRST.md` (3,927 bytes), `01_the_phase_definitions.md` (18,850),
  `02_the_guiding_principles_and_the_conventions.md` (69,236), `03_the_writing_standards.md` (15,205),
  `04_the_dispatch_protocol.md` (109,056), `05_the_ratified_design_intent.md` (265,689),
  `06_the_defect_type_catalog.md` (5,968), `07_the_charter_the_layers_and_the_decisions.md` (36,470),
  `08_the_seventeen_research_extracts.md` (119,340), `09_the_empirical_findings_ledger.md` (51,543). `write_all`
  rewrites every file of a live subject at every write-mode run that covers it, so a shared 2026-10-16 time suggests no
  write-mode run touched them since. **This is a reading of file times, not a proof; the proof is git's, at 1(b).**
- **NOT KNOWN TO THIS SIDE — whether the L3 pack's files changed in git between the commit that rendered them and
  `<T0>`.** If they did, the files on disk may not be what L3's session was given, and freezing them would pin the wrong
  record. 1(b) establishes it and carries a stop.
- **ASSUMPTION A1 — the working tree, stated by CONTENT.** Tracked modifications at your boot: **exactly one**,
  `tools/audit/claude_md_finer_archive.json` — standing, carried and not chased (RELAYED: the third report §8, A1 held).
  **This side wrote no tracked file.** Untracked and landed by Task 0: this dispatch and entries 472, 473, 474 and 475 —
  **five untracked paths**. The rest of the third dispatch's A1 binds.
- **ASSUMPTION A2 — the reds, by cause.**
  - **The opening capture** (at 0(g)) fails the thirteen of the start tip's `guard_state.json` and
    `gen_per_session_reading.py --check` — cause: Task 0's landed entries. Anything else is reported and is a STOP.
  - **Task 1:** the capture after the freeze is expected IDENTICAL to the opening capture, verdict by verdict, and
    `gen_derivation_boot_pack.py --check` GREEN with *"l3: FROZEN — 10 file(s) at their recorded blobs"* among its lines.
  - **Task 2, at 1(g):** compared with the capture after Task 1, exactly `gen_session_start_read_size.py --check` and
    `gen_defense_share.py --check` turn RED — the third dispatch's prediction — and **`gen_derivation_boot_pack.py
    --check` stays GREEN**, its *"FROZEN SOURCES"* listing now naming `l3/02_the_guiding_principles_and_the_conventions.md`
    among the files a re-render would produce at a different length (that listing sets no exit code). The population
    movement is the third dispatch's class (a) and class (c) prediction, unchanged.
- **ASSUMPTION A3** — as the third dispatch's A3.
- **ASSUMPTION A4 — THE FOOTPRINT.** **Task 1:** in `tools/audit/gen_derivation_boot_pack.py`, the one `"l3"` entry
  added to `FROZEN` and the one comment block directly after it — nothing else in the tool; and the manifest, regenerated
  by the tool's write mode. **Nothing under `tools/audit/derivation_boot_pack/`.** **Task 2:** as the third dispatch's
  A4 for its Task 1. **Task 3:** as the third dispatch's A4 for its Task 3.
- **ASSUMPTION A5 — byte-unchanged by this batch**: the third dispatch's A5, read with the start tip in place of its
  start tip, every handoff entry from 448 to 471 in place of 448 to 469, **and the ten files of the L3 pack**.

## The declared start state — at the tree you will meet

As the third dispatch's (its lines 269 to 271), with **entries 472 to 475** in place of entries 470 and 471.

## Findings in this batch

**No finding number is allocated.**

---

## Task 0 — land the records, and PUSH

**Execute the third dispatch's Task 0 (its lines 279 to 302) under the substitutions, with these overrides:**

- **0(b) — the chain.** Each hash written literally in its own command: `git cat-file -p
  1126176e2a4b48fc01bbb5b545210715366cb24a` (expected parent `c7b6985a9c0be8fb7f975addf2fb0642c0311c29`); `git cat-file
  -p c7b6985a9c0be8fb7f975addf2fb0642c0311c29` (expected parent `f630b1eb09b2a0c395a94ff2b99b6b5d7936b43c`); `git
  cat-file -p f630b1eb09b2a0c395a94ff2b99b6b5d7936b43c` (expected parent `749ab8c88a7e5221c73fcdc7d96a040c7fb3580b`);
  `git show --stat` of each of the four. **Report the chain.** A different chain is a STOP-and-report.
- **0(c)** — as there, every `git diff --stat` taken against the start tip.
- **0(d) — sizes:** entry 472 7,300; entry 473 7,177; entry 474 8,872 (FACT). **No size is stated for this dispatch or
  entry 475** — report what you find.
- **0(e) — the commit**, exactly these paths and no other, staged by explicit path, the staged set proved with
  `changed_paths.py --staged`:
  - `records/cc/instructions/cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md` (this dispatch; new)
  - `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_two.md` (new)
  - `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_three.md` (new)
  - `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_four.md` (new)
  - `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_seventy_five.md` (new)

  Subject, exactly: `record: entries 472 to 475 and the step-4 fourth execution dispatch`. If entry 475 is NOT at your
  boot, land the remainder with the subject `record: entries 472 to 474 and the step-4 fourth execution dispatch`,
  report its absence, and do not wait for it. Push; verify at the ref file that `origin/master` equals the new tip.
  **This commit is `<T0>`.**
- **0(g)** — as there. The differing-values script's expectation is unchanged (exactly the one value each). **The
  opening capture is the one A2 names.**

**E0:** as the third dispatch's E0.

---

## Task 1 — FREEZE `l3` IN THE BOOT-PACK TOOL, BEFORE ANY EDIT OF `CLAUDE.md`

**Why first:** Task 2 edits `CLAUDE.md`'s Conventions span; with `l3` live, that edit turns this tool's `--check` red
(the third report §4). Frozen, `l3` is checked against its recorded blobs and not against a re-render.

- **1(a) — the check before the act.** `python tools/audit/gen_derivation_boot_pack.py --check`, in its own call, output
  saved and read. **Expected: exit 0 and the line *"the derivation boot pack re-derives"*, the four frozen subjects named
  as at their recorded blobs, `l3` not among them.** Anything else is a STOP-and-report, with nothing edited.
- **1(b) — the L3 pack's history, so the freeze pins what L3's session was given.** Each in its own command:
  1. `git log --format="%H %ad %s" --date=iso -- tools/audit/derivation_boot_pack/l3` — report it whole. **Expected:
     exactly one commit, the render commit, whose hash begins `ca55115f`** (RELAYED: the away-returns section *"THE L3
     PACK BUILD, SECOND HALF, RESUMED"*).
  2. `git log --format="%H %ad %s" --date=iso -- records/cowork/cowork_blind_derivation_l3_2026_10_17.md` (if the path
     differs, locate the file by `git ls-tree -r --name-only <T0>` filtered for `blind_derivation_l3`, and report the
     path used) — report the commit that added it. **Expected: a commit later than the render commit** (RELAYED:
     `96a24b01…`, the derivation-commit batch's Task 0).
  3. For each of the ten files: `git rev-parse <T0>:tools/audit/derivation_boot_pack/l3/<file>`, `git rev-parse <the
     render commit>:tools/audit/derivation_boot_pack/l3/<file>`, `git hash-object <file>` and `git hash-object
     --no-filters <file>` — **all four equal, for every file.** A scratch script may run the forty queries; declare it
     and quote it whole in the appendix.

  **If any of 1 to 3 does not come out as expected — a second commit touching the directory, a derivation landed before
  the render, or any of the four hashes differing for any file — STOP-and-report with nothing edited.** Do not pin files
  from git objects, and do not regenerate the pack; whether the files on disk are what L3's session was given is then a
  question for the writing side.
- **1(c) — the edit**, with the file-editing tool. In `FROZEN`, directly after the comment block that follows the `l2`
  entry (the block opening *"`l2` IS FROZEN ABOVE, ITS DERIVING SESSION HAVING RUN"* and ending *"`cowork_rulings_2026_10_16_l2_freeze_leak_list_sitting.md`)."*)
  and before the table's closing `}`, insert, with each line indented exactly as the `l2` entry's own lines are:

  ```python
      "l3": {
          "finding": ("Its deriving session has RUN: `cowork_blind_derivation_l3_2026_10_17.md` and the released "
                      "`cowork_blind_session_brief_l3.md` were landed by "
                      "`records/cc/instructions/cc_instruction_l3_derivation_commit_2026_10_17.md`. The pack "
                      "directory's files are unchanged in git since the commit that rendered them, and `--check` "
                      "passed at <T0>, so the digests recorded here are those of the files on disk, proved equal "
                      "to their committed blobs: what the session was given, and not a re-render."),
          "date": "<ACT_DATE>",
          "reason": ("A spent subject's pack is the record of what its session was given rather than an input "
                     "to be kept current (Ruling 17(a); D-646). Left live, its member (2) re-renders "
                     "`CLAUDE.md`'s guiding-principles and Conventions spans, so the first edit of either — "
                     "Ruling 1 of `cowork_rulings_2026_11_01_pruning_iteration_sitting.md` — turns `--check` "
                     "red, or, if refreshed, back-dates into a completed derivation's record a text its session "
                     "never read (#12). Frozen at the blobs it carries, with the hash STOP, before that edit."),
          "digests": {
              "00_READ_THIS_FIRST.md": "<blob>",
              "01_the_phase_definitions.md": "<blob>",
              "02_the_guiding_principles_and_the_conventions.md":
                  "<blob>",
              "03_the_writing_standards.md": "<blob>",
              "04_the_dispatch_protocol.md": "<blob>",
              "05_the_ratified_design_intent.md": "<blob>",
              "06_the_defect_type_catalog.md": "<blob>",
              "07_the_charter_the_layers_and_the_decisions.md":
                  "<blob>",
              "08_the_seventeen_research_extracts.md": "<blob>",
              "09_the_empirical_findings_ledger.md": "<blob>",
          },
      },
      # `l3` IS FROZEN ABOVE, ITS DERIVING SESSION HAVING RUN; its own ground is in its own entry and is
      # not restated here (#6).  Frozen by `cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md`
      # Task 1, before Ruling 1 of `cowork_rulings_2026_11_01_pruning_iteration_sitting.md` edited
      # `CLAUDE.md` (the derivation recorded in handoff entry 474 §1).  NOT named in
      # `RENDERED_BEFORE_THE_SCOPING_RULINGS`: its pack was rendered after both scoping rulings.
  ```
  *(The fence lines are not in it. Replace `<T0>` with the first eight characters of `<T0>`'s hash followed by `…`,
  `<ACT_DATE>` with the date, and each `<blob>` with that file's 40-character hash from 1(b) 3. The four leading spaces
  shown are the indentation of the `l2` entry's own key line; if that indentation differs at the object, follow the
  object and report it.)*
- **1(d) — the manifest.** `python tools/audit/gen_derivation_boot_pack.py` (write mode), in its own call, output saved
  and read. Expected: no STOP; *"wrote tools\audit\derivation_boot_pack.json"* (or the same with `/`). Then `git status
  --porcelain` — **expected modified: the tool, the manifest, and the standing `claude_md_finer_archive.json`; nothing
  under `tools/audit/derivation_boot_pack/`.** Then `git hash-object` of each of the ten L3 files — **each equal to its
  1(b) value.**
- **1(e) — THE D-657 COMPARISON**, by a scratch script quoted whole in the appendix: load the manifest at `<T0>` (`git
  show <T0>:tools/audit/derivation_boot_pack.json`) and the regenerated one, walk both as JSON, and print every path
  whose value differs, was added or was removed. **The prediction, in full:**
  - **No difference outside `subjects` → `l3`.** The four other subjects and every top-level field are unmoved.
  - **Inside `subjects` → `l3`, only:** the added key `★_FROZEN` (its `finding`, `date`, `reason` and `the_digests`
    equal to the `FROZEN["l3"]` entry); in each record of `the_members_as_rendered`, the added
    `★_where_this_record's_measures_COME_FROM` and the removals `frozen_from_disk` makes (`lines_rendered` from spans;
    `characters` from parts; `the_text_removed`, `characters_removed`, `heading`, `closes_before` from filters;
    `entries_rendered`, `rows_rendered`, `columns_kept`); in `counted`, the added
    `★_which_of_these_counts_describe_the_DIRECTORY`.
  - **Unmoved inside `l3`:** every member record's `characters`; `counted.files_in_the_pack`; `LEAKS_IN_THE_EXTRAS`
    entry for entry; `counted.extras_lines_with_a_leak_hit`; every other field.

  **Any other difference is the ★ case for Task 1.**
- **1(f) — the checks.** `python tools/audit/gen_derivation_boot_pack.py --check`, in its own call: **expected exit 0,
  *"the derivation boot pack re-derives"*, and *"l3: FROZEN — 10 file(s) at their recorded blobs"***; its *"FROZEN
  SOURCES"* line quoted whole. Then the full guard capture, taken the way the opening capture was taken at 0(g), compared
  verdict by verdict with the opening capture: **expected IDENTICAL** (A2). Both population checks expected GREEN.
- **1(g) — the commit**, exactly `tools/audit/gen_derivation_boot_pack.py` and `tools/audit/derivation_boot_pack.json`,
  staged by explicit path, the staged set proved with `changed_paths.py --staged`. Subject, exactly: `Freeze l3 in the
  derivation boot pack: its deriving session has run (Ruling 17(a), D-646), before Ruling 1 edits CLAUDE.md`. Push;
  verify `origin/master` at the ref file. **This commit is `<T1>`.**

**★ THE CASE FOR TASK 1 — anything other than predicted at 1(c) to 1(f).** Reverse the edit of the tool with the
file-editing tool and prove it equal to its `<T0>` blob (`git hash-object`); run write mode once and prove the manifest
equal to its `<T0>` blob; prove the ten L3 files equal to their 1(b) values. **Then do NOT run Task 2** — Ruling 1 cannot
be committed while `l3` is live — and go to Task 3, whose close entry says that neither task was committed and why.

**E1:** `l3` frozen at the ten blobs 1(b) proved; the manifest moved only as 1(e) predicts; `--check` green; the capture
identical to the opening one; one commit, pushed.

---

## Task 2 — Ruling 1: EXECUTE THE THIRD DISPATCH'S TASK 1 (its lines 306 to 316), with these overrides

**Execute it as written, under the substitutions** — which execute the second dispatch's Task 1 and through it the
first dispatch's text's steps 1(a) to 1(i), with the third dispatch's class (c). **Base `<T1>`** throughout (substitution
3). **Overrides:**

- **1(g) — the full guard capture is compared with the capture taken at Task 1(f), not with the opening capture.** **The
  prediction, in full:** `gen_governing_surface_split.py --check --pair CLAUDE.md` exit 0; the two historical archive
  checks FAIL with the same one differing value each as at 0(g); the L0/L1 artifact moves only inside `CLAUDE.md`'s
  per-file hit record (class (a)); the L3 artifact moves exactly at the five class-(c) places and nowhere else; after the
  regenerations both population checks are green; the guard capture differs from the Task 1(f) capture in exactly
  `gen_session_start_read_size.py --check` and `gen_defense_share.py --check` turning RED; **and
  `gen_derivation_boot_pack.py --check` exits 0**, its output quoted whole in the report. **Anything else is the second
  dispatch's ★ case for its Task 1**, as the third dispatch applies it: reverse the two edits, prove both files and both
  population artifacts equal to their `<T1>` blobs, and go to Task 3.
- **The relayed values of the third run** that the third dispatch's class (c) cites (`CLAUDE.md` 170942 → 170510, the
  sum 844831 → 844399; the third report §4) are the expected values here too: the edit is the same act on the same
  bytes (the third report §4 1(f): the new `CLAUDE.md` blob `d8b285af…`, the same object the second run produced). **A
  different new blob for `CLAUDE.md` is reported**, and the class-(c) rule then binds on the measured size, as written.

**E2** — as the second dispatch's E1, with class (c) read into *"the predicted reds"* and the boot-pack check green.

---

## Task 3 — the close: EXECUTE THE THIRD DISPATCH'S TASK 3 (its lines 380 to 421), with these overrides

- **3(a)** — the close entry names THIS dispatch by its file name and carries the `Last updated: ` prefix, **moved off
  the third dispatch's close entry (now at `STATUS.md`'s line 8)**, the move complete before 3(b) runs, exactly one line
  carrying it afterwards. Below it, one `Same dispatch` entry per COMMITTED task, newest first (as the third run wrote
  them). **It says in plain words:** that this batch carries Ruling 1 out a fourth time, after three runs did not commit
  it; that it first froze the L3 derivation boot pack, because its deriving session has run and its live member (2)
  rendered `CLAUDE.md`'s Conventions span; that it then ran the third dispatch's Ruling 1 steps by citation; and, in
  place of the third dispatch's tool sentence: **one measurement tool's `FROZEN` table extended by one entry and its
  manifest regenerated; no other tool edited or added.** Where a task was not committed, it says which and why. No
  algorithm change; no decisions-register entry, no `D-NNN`, no open-items row.
- **3(b) — the forward bound.** Read `tools/audit/gen_status_batch_bound.py` at the object
  `1126176e2a4b48fc01bbb5b545210715366cb24a:tools/audit/gen_status_batch_bound.py` first; **report its authored
  constants as you find them** (RELAYED, the third report §6 3(b): `BASE_COMMIT` `f630b1eb…`, `PREVIOUS_BATCH_DISPATCH`
  the second dispatch, `DISPATCH` the third dispatch, `TASK` `Task 3`, `MOVE_KIND` `ordinary`, `ACT_DATE` 2026-11-01; a
  difference is reported and 3(b) proceeds from what the object holds). Re-aim: `BASE_COMMIT` this batch's LAST TASK
  COMMIT before the close (**check that the `STATUS.md` blob at `BASE_COMMIT` equals its blob at the start tip, each `git
  rev-parse` in its own command**); `PREVIOUS_BATCH_DISPATCH` `cc_instruction_pruning_rulings_third_execution_2026_11_01.md`;
  `ACT_DATE` the day the move runs; `DISPATCH` `cc_instruction_pruning_rulings_fourth_execution_2026_11_02.md`; `TASK`
  `Task 3`; `MOVE_KIND` stays `ordinary`; append this batch's aiming to `PREVIOUS_AIMINGS` (do not append the third
  dispatch's aiming twice); amend the head comments as the previous batches did, the former value named (#12). **Then
  `--apply` and `--check`, each in its own call. Prediction: exactly the third dispatch's THREE entries move** — its
  close entry and its Task 2 and Task 0 `Same dispatch` entries (base lines 8, 10 and 12); the two 2026-09-02 entries
  stay; no STOP. The cited STOP handling, *no correction line* rule and four archive checks bind.
- **3(c) — the regenerations**, as the third dispatch's 3(c), with: **each population check may be RED or GREEN
  here.** Task 2's 1(g) already regenerated both for `CLAUDE.md`'s movement, so only 3(a) and 3(b)'s edits of `STATUS.md`
  and `STATUS_ARCHIVE.md` remain to move them. The third run met L0/L1 GREEN at its 3(c) (`STATUS.md` carries no L0/L1
  admitting hit; the third report §6 3(c)) and L3 RED by one passage, the `STATUS.md` residue record's *paraphrase* hit
  line 18 → 20. A RED check is regenerated under the confinement check with base the start tip and allowed paths
  `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `STATUS.md` and `STATUS_ARCHIVE.md`, **class (c) applying when Task 2 is
  committed**. Changed line values inside the `STATUS.md` residue record of the L3 artifact are allowed. A GREEN check
  is not regenerated, and its artifact is diffed against the start tip under the same check.
  *(Former wording, preserved (#12): "**both population tools RED where Task 2 was committed**, regenerated under the
  confinement check with base the start tip and allowed paths `CLAUDE.md`, `CLAUDE_ARCHIVE.md`, `STATUS.md` and
  `STATUS_ARCHIVE.md`, **class (c) applying when Task 2 is committed**; changed line values inside the `STATUS.md`
  residue record of the L3 artifact are allowed (the third run's 3(c) met one such passage).")* `per_session_reading.json`'s boot chain moved by entries 472 to 475 — report the three latest entries it
  names. **The boot-pack manifest is NOT regenerated here** (Task 1 did it); its `--check` is expected green. **Quote in
  the report, from the regenerated `session_start_read_size.json`, the `CLAUDE.md` and `STATUS.md` members before and
  after.** Where neither task was committed, the population checks may be green; then neither is regenerated.
- **3(d) — the report, in Ruling 4's two-file form**, at **`records/cc/reports/cc_report_pruning_rulings_fourth_execution_2026_11_02.md`**
  and its appendix **`records/cc/reports/cc_report_pruning_rulings_fourth_execution_2026_11_02_appendix.md`**, as the
  third dispatch's 3(d) orders it. **Add to the report proper:** the reads of the three cited texts (blob, size, scratch
  path); 1(b)'s history and the forty hashes as a table; 1(e)'s comparison output whole; both `--check` outputs of the
  boot-pack tool; every class-(c) passage with its two values.
- **3(e)** — the section appended to `records/cowork/handoff/cowork_away_returns.md` is headed **THE PRUNING ITERATION,
  STEP 4, RULING 1 CARRIED OUT A FOURTH TIME — THE L3 DERIVATION BOOT PACK FROZEN FIRST, THEN TWO FORMER WORDINGS TO
  `CLAUDE_ARCHIVE.md`; DOCUMENTATION AND ONE MEASUREMENT-TOOL TABLE ONLY, NO ALGORITHM CHANGED** (where a task was not
  committed, the heading says which and why). **The plan line is the third run's, with Ruling 1 removed from what is
  pending:** *"The next act is the writing side's — the check of this batch's return at the objects; then step 4's
  SECOND dispatch (the measurement tool extended with the dispatch form's invariant share and the sizing of a report's
  appendix file, and the measurement re-run so the after-values stand beside the before-values); then, one per turn, the
  user's yes-or-no on carrying the Cowork boot chain's operating paragraphs in the current handoff entry (candidate (e))
  and, once the invariant share is measured, the dispatch-form surface (candidate (d)); and only then step 5, the method
  ruling's surface over the completed L3 tabulation (Ruling 4 of the comparison-design sitting)."* If Task 2 was not
  committed, the plan line instead says Ruling 1 is still pending and why.
- **3(f) — the close commit**, as the third dispatch's 3(f), the report and appendix at this batch's names. Subject:
  `Close: the pruning iteration step 4 - Ruling 1 carried out a fourth time, the L3 boot pack frozen first, under its
  dispatch`. Push; verify `origin/master` at the ref file.

**E3:** as the third dispatch's E3.

---

## Task 4 — the end state: EXECUTE THE THIRD DISPATCH'S TASK 4 (its lines 425 to 433), with these overrides

- **The verification at the objects** takes `git diff --name-status 1126176e2a4b48fc01bbb5b545210715366cb24a <the close
  commit>`, every path accounted for against A4 and the Task 0 files, every file A5 names absent — **the ten L3 pack
  files among them**.
- **The commit subject:** `End state: the pruning iteration step 4 fourth execution - guard run at the close tree, the
  A2 regenerations already met inside the close`. Push; verify `origin/master` at the ref file.

**E4:** the condition held at a fresh run committed only after the run that produced it.

**THIS BATCH ENDS HERE.**

---

## What this batch does NOT do

**The third dispatch's list (its lines 441 to 443) binds**, read as: no step of Ruling 3; the legacy-mark check not
touched; **one measurement tool's `FROZEN` table extended by one entry (Task 1)**, and no other tool edited or added. It
does not re-render, regenerate or edit any file of any derivation boot pack; it does not add `l3` to
`RENDERED_BEFORE_THE_SCOPING_RULINGS`; and it corrects no earlier report (D-674).

## What this batch deliberately leaves to later acts, named so it is not lost

- **The third dispatch's list (its lines 447 to 450), unchanged.**
- **Two stale sentences in the boot-pack tool, left as they stand to keep the footprint to one entry:** the comment in
  `build()` saying *"all three subjects being spent"* (five are built, and with this batch all five are frozen); and the
  first block of `VERDICTS["l3"]`'s opening comment, which the L3 pack build's resumed second half named stale (its
  away-returns section, item 2). Documentation of a tool only; for a later act under the user's rule of 2026-09-22.
- **Step 4's second dispatch** (the plan line in 3(e)).

---

## The writing side's self-check over this dispatch (recorded, per the standing clause; D-434)

*Written by the writing side after the draft, before its check at its sources; the check runs in a turn of its own and
is recorded in the next section.*

- **Read at the objects this sitting**, through staged copies and the file tools: the ref files; `STATUS.md` at its first
  25 lines; the third dispatch whole (41,161 bytes); the third report at §4, §6, §7 and §8; the boot-pack tool at its
  docstring lines 75 to 114 and 160 to 175, lines 245 to 529 (`VERDICT_DATE`, `MEMBERS`, `FROZEN`,
  `RENDERED_BEFORE_THE_SCOPING_RULINGS`), 4498 to 4515 (the L3 block's head), 8815 to 8939 (the extras scan and the
  record), 8990 to 9022 (`build()`'s checks and loop), 9183 to 9456 (`pack_dir` to the end), and by search for `^def `,
  for frozen-membership tests, for `OUT`, `PACK_ROOT` and the manifest keys; the two `l2` freeze records whole; the
  away-returns sections *"THE L3 PACK BUILD, SECOND HALF, RESUMED"*, *"THE L3 BLIND DERIVATION COMMITTED"* and the third
  run's, each located by a heading search; the L3 pack directory's listing; both population artifacts by search; the
  handoff entries 474, 473 and 291 whole.
- **Not read:** the second dispatch and the first dispatch's text (git objects), so every line range given for them is
  the third dispatch's own; the `l2` freeze's dispatch (`cc_instruction_l3_pack_build_second_half_resumed_2026_10_16.md`)
  and its report; the L3 derivation-commit report; D-646 at its home; `DECISIONS.md`; `CLAUDE.md`; `OPEN_ITEMS.md`;
  `guard_state.json`; any git object.
- **Self-sufficiency (D-251):** the one fork the third run met (the boot-pack red) has a task here; the new task's
  unknowns (the pack's git history, the manifest's movement, the capture) each have a prediction with a stop.
- **No new mechanism:** Task 1 adds one row to an existing table under an existing ruling; no tool behaviour changes.

## This file's check at its sources (D-434; runs in a turn of its own)

*Run 2026-11-02 by the writing side, in the turn after the draft landed, over the draft as landed (44,727 bytes at its
staging result).*

**Checked at the objects and found to hold:**

- Every line range this file gives for the third dispatch, against the staged working-tree copy (41,161 bytes):
  - D-251, 52–55;
  - the cited texts' reads, 69–77;
  - the eight-line check, 79;
  - items (1) to (6), 83–92;
  - items (8) and (9), 95–101;
  - item (10), 102;
  - the words section, the substitutions and the confinement check, 106–171 (substitutions 119–136);
  - the ruling ledger, 175–186;
  - the premise ledger, 190–245, and A1 to A5, 247–267;
  - the start state, 269–271;
  - Task 0, 279–302; Task 1, 306–316; Task 3, 380–421; Task 4, 425–433;
  - the two closing lists, 441–443 and 447–450;
  - the end of what CC reads, 451.
- The words *"the second dispatch's ★ case for Task 1"* and E1 *"as the second dispatch's E1"* at the third dispatch's
  Task 1.
- `STATUS.md`'s lines 8 to 22. The class-(c) values in the L3 artifact.
- The tool:
  - the `FROZEN` table's four entries and the comment after `l2`, ending as quoted;
  - the four-space indentation of the `l2` key line;
  - the `FROZEN` preamble's quotation of Ruling 17(a);
  - `VERDICT_DATE["l3"]`;
  - `RENDERED_BEFORE_THE_SCOPING_RULINGS` and its preamble;
  - the functions as the premise ledger describes them;
  - `check_all`'s two printed lines;
  - `OUT` and `PACK_ROOT`;
  - that `the_pack_files_in_order` is built from member file names only.
- The L3 pack's ten file names. The away-returns sections and commit prefixes relayed.

**Corrected, every former wording preserved here (#12):**

1. *What this batch is, the tool's rule.* Former wording: "its docstring paragraph opening … , quoting Ruling 17(a) of
   `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *"A subject whose deriving session HAS RUN is SPENT …"*".
   The quoted sentence is the docstring's own, not the ruling's verbatim text. It is now attributed to the docstring.
2. *Premise ledger, the membership tests.* Former wording: "`FROZEN`, `RENDERED_BEFORE_THE_SCOPING_RULINGS` and nothing
   else are tested on frozen membership: a search of the tool for `in FROZEN`, `set(FROZEN)` finds only `build_subject`'s
   extras scan, `build()`'s two STOP checks and its loop, `write_all` and `check_all`." The first clause was garbled and
   the search named was narrower than the one run. It now names the four search patterns, separates the two tables, and
   states the search as its bound.
3. *Ruling ledger, the `l2` precedent's date.* Former wording: "the `l2` freeze of 2026-10-16". Its `FROZEN` entry is
   dated 2026-10-15; the batch that carried it out ran on 2026-10-16. Both are now named.
4. *Premise ledger's opening.* Former wording: "**The third dispatch's premise ledger (its lines 190 to 245) is carried
   for Task 2, read under the substitutions, EXCEPT where an item below replaces it.** Its items on the legacy-mark check
   and on `DECISIONS.md`'s values belong to Ruling 3 and are not used." It left unsaid how the third dispatch's A1 to A5,
   which stand inside its ledger at 247–267, relate to this file's. Now stated.
5. *3(c), the population prediction.* Former wording preserved in place at 3(c). It predicted both population checks
   RED at the close. Task 2's 1(g) already regenerates both, and the third run met L0/L1 GREEN at its own 3(c). The
   prediction now allows either verdict and says what each requires. **This is the one correction of content: as
   written, a green L0/L1 check at the close would have been an unpredicted result.**
6. *Premise ledger, the L3 pack's file times.* Former wording: "rewrites every file of a live subject at every
   write-mode run". With `--subject`, write mode covers one subject only. It now reads "at every write-mode run that
   covers it".

**Swept for absolutes** (only, never, nowhere, every, all, none, nothing, exactly, whole, complete, identical). Each hit
was read at its line:

- *Exactly* and *identical* are predictions, each with a stop.
- *Every fork the third run met* covers its two departures from prediction: the boot-pack red at Task 1, and the green
  L0/L1 check at 3(c), now covered by correction 5.
- *Nothing under `tools/audit/derivation_boot_pack/`* is enforced by 1(d)'s status check and the ten hashes.
- *NOTHING changes* (algorithm) is bounded by A4's footprint.

**Risk named, not removed (#13):** whether any guard pins the boot-pack tool's own blob was not read by this side. If
one does, Task 1(f)'s capture differs from the opening capture, and the ★ case for Task 1 reverses the freeze. That
costs a further dispatch but leaves the record intact.
