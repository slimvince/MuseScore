# CC dispatch — L3's RULING WRITE-BACK: the three rulings of 2026-10-15 written back to the verdict table and to L3's reading file, which re-renders as RULED, with the shared sentences that read wrongly for L3 moved into each subject's entry — NOTHING withheld, NO pack, NO algorithm change, NO register entry, NO session booted

> **★★ RELEASED 2026-10-15** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_one.md`, which wrote it, after the check at the
> sources recorded at the end of this file. It is executed by Claude Code when the user hands it over (D-252); the
> Cowork writing side never runs it. *(The banner this replaces read, preserved (#12): "**★★ DRAFT UNDER
> CONSTRUCTION BY THE COWORK WRITING SIDE — NOT TO BE HANDED TO CLAUDE CODE.** Claude Code: if you are reading this
> banner, STOP at once, do nothing, and report that you were handed an unfinished draft.")*

## What this batch is, in plain words

On 2026-10-15 the user ruled L3's three verdict lists, one per turn
(`records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`):

- **Ruling 1 ("A")** — LIST ONE stands as authored: the 19 entries proposed IN are withheld.
- **Ruling 2 ("B")** — of the 223 entries proposed OUT, 222 are admitted; **D-605 moves from OUT to IN**.
- **Ruling 3 ("A, both IN")** — the two UNPLACED entries, **D-459 and D-472, are both IN**.

The ruled result is 22 IN, 222 OUT, 0 UNPLACED. This batch writes those three moved verdicts back to
`VERDICTS["l3"]` in `tools/audit/gen_derivation_boot_pack.py`, gives L3's entry in the reading-file tool
(`tools/audit/gen_withheld_family_reading.py`) its `ruling` block, corrects the shared sentences of that tool that
read wrongly for L3 (the ruling record's §3 names three; the ruled rendering makes four more wrong for L3, named
below), and re-renders `ratification_surfaces/cowork_withheld_family_l3_reading.md` as RULED. It is modelled on
`records/cc/instructions/cc_instruction_l2_ruling_writeback_2026_09_05.md`, which did the same for L2.

**Documentation and algorithm.** All three rulings decide only which recorded decisions a future deriving session may
read; this batch edits a table of proposals that nothing reads today, a reading-file tool, and the file it renders.
**Nothing here changes the algorithm as any specification defines it.** The currently decided method for L3 is
`FRAMEWORK.md` §5's L3 block with DP-I (*"split — cues at L1, type at L3"*).

## Words used in this dispatch, explained first

- **Boot pack, withheld family, candidate, verdict (IN / OUT / UNPLACED), finding, reason, guard set, red** — as
  defined in `records/cc/instructions/cc_instruction_l3_candidate_list_and_verdict_pass_2026_10_14.md`, "Words used
  in this dispatch". **IN** means withheld from the pack; **OUT** means admitted to it.
- **The verdict table** — `VERDICTS["l3"]` in the generator: one three-string tuple per candidate (the verdict word,
  the finding, the reason). It is the one home of the verdicts. `WITHHELD` carries no `l3` entry, so nothing in the
  generator reads this table today.
- **The reading file** — `ratification_surfaces/cowork_withheld_family_l3_reading.md`, rendered by
  `python tools/audit/gen_withheld_family_reading.py --subject l3`, whose `--check` re-renders and compares. It is
  generated and never hand-edited.
- **The ruling block** — the `"ruling"` dictionary inside a subject's entry of the reading-file tool's `SUBJECTS`.
  When it is present, `render()` writes the RULED banner, §7 "What was ruled", and the rulings and their notes.
  L2's entry has one; L3's gets one here.
- **A shared sentence** — a line `render()` writes for every subject from a fixed string. Where such a line is true
  of L2 and wrong for L3, this batch moves it, unchanged, into `SUBJECTS["l2"]` and gives `SUBJECTS["l3"]` its own
  text, so L2's file renders byte-identically and L3's file says what is true of L3.
- **The ruling record** — the 2026-10-15 record named above. Every string this batch puts into the tool's L3 ruling
  block, and every rewritten reason, is that record's content; Task 2(f) checks them against it.

## The ruling ledger

| | Record or rule | What it orders | Task |
|---|---|---|---|
| L.1 | The 2026-10-15 ruling record, Rulings 1 to 3 and §2 | D-605, D-459 and D-472 written as IN with rewritten reasons; `SUBJECTS["l3"]` given its ruling block; the file re-rendered; the record landed at Task 0. | 0, 1, 2 |
| L.2 | The same record, §3 | Three sentences of the shared rendering corrected for L3: §8's *"The criterion's reach is unmeasured, and §4 says so"*; the banner's Ruling 81 citation; §5's sentence about what the executing side's report states. | 2 |
| L.3 | The user's standing rule of 2026-09-22 | Staleness and apparent errors in the record are fixed without asking him. It covers the four further sentences this batch's own ruled rendering would make wrong for L3 (Task 2(b), Edits 3, 4, 10, 11 and 12). | 2 |
| L.4 | Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md` | *"No identity is withheld that the user has not ruled."* — the citation L3's banner carries in place of Ruling 81. | 2 |

The user's standing rule: **every commit is pushed, and the push is verified at `.git/refs/remotes/origin/master`.**

## Premise ledger (written 2026-10-15 by the writing side from staged copies read with the file tools; no shell command and no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/HEAD` → `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both `a191a380b3c4b9621bb2628e754582376faf2bf6`. `.git/logs/HEAD` names it
  *"End state: the L3 reading file batch's guard run at the close's tree, with the defense-share artifact regenerated
  under A2"*, its parent `0de5b66a2af0569c9cce7fa0b003c8e9e7c0aad7`. **Re-read both ref files yourself before Task 0.**
- **FACT — the guard start state, at `tools/audit/guard_state.json` → `summary`, read whole by the writing side:**
  run 80, passing 66, failing 14, not run 4, historical 20. The fourteen failing, by name: `gen_phase3_gate_partition.py`,
  `gen_filing_convention_application.py`, `gen_artifact_inventory.py`, `gen_artifact_inventory_surface.py`,
  `gen_test_construction_evidence.py`, `gen_retirement_caller_check.py`, `decisions/apply_soft_discard.py`,
  `decisions/apply_residue_discard.py`, `gen_epoch_write_path.py`, `gen_derivation_boot_pack.py`,
  `gen_recognizer_establishment_sort.py`, `decisions/gen_cluster_dispositions.py --verify`,
  `decisions/gen_home_classification.py`, `decisions/gen_phase1p_delegation_bar.py`. The classification tool
  `gen_guard_classification.py --check` ends on its standing STOP naming `gen_l0_l1_outgoing_population.py`,
  `gen_l2_withheld_documents.py` and `gen_withheld_family_reading.py` (**relayed** from the last report, §2; your start
  run is the proof). Both reading-file runs, `--subject l2 --check` and `--subject l3 --check`, are already enrolled
  and passing; **this batch enrols nothing.**
- **FACT — the three tuples Task 1 edits**, read in `VERDICTS["l3"]` (the block opened by the comment
  `# ── L3, the deriving subject after L2 — PROPOSALS, NOT A WITHHELD FAMILY`), each quoted byte for byte in Task 1.
  The entry key `"D-605": (VERDICT_OUT,` occurs TWICE in the file (once in an earlier table) and `"D-459"` and
  `"D-472"` each occur twice as well; **each whole multi-line old text below occurs once**, because its finding lines
  occur only in the `l3` block (checked by a search for each finding line: one hit each).
- **FACT — `gen_derivation_boot_pack.py --check` IS ALREADY RED** (in the failing fourteen). That nothing in the
  generator reads `VERDICTS["l3"]` (`build()` iterates `WITHHELD`, which carries no `l3`) is **relayed** from the
  last dispatch's premise ledger and the `l3` block's own opening comment; this side did not read `build()`. Inertness of Task 1 is
  proven by the `--check` OUTPUT being byte-identical before and after, as in the last three batches.
- **FACT — the reading-file tool** (`tools/audit/gen_withheld_family_reading.py`, 40,680 bytes at its staging, read
  WHOLE). `SUBJECTS["l2"]` carries a `ruling` block with `record`, `date`, `rulings`, `test_note` and `notes`.
  `SUBJECTS["l3"]` carries none. **`render()` reads `ruling["test_note"]` in two places (§2 and §5) under a bare
  `if ruling:`**, so an L3 ruling block without that key raises a `KeyError`. L2's `test_note` states Ruling 1(a) of
  the L2 sitting, a fifth ground L3's rulings did not add. **This batch makes the key optional** (Edits 7 and 8);
  L3's block carries none, because L3's test was not changed by any ruling.
- **FACT — the shared sentences, read in `render()` and in the rendered L3 file**, each corrected in Task 2:
  1. The ruled banner and the unruled banner each cite *"Ruling 81, §3cj of
     `cowork_rulings_2026_08_31_decision_surface_sitting.md`"* for *no identity is withheld that the user has not
     ruled*. For L3 the rule is Ruling 2 of the 2026-10-14 L3 record, whose words are *"No identity is withheld that
     the user has not ruled."* (record §1b, read whole).
  2. §5: *"…the register group and the LEGACY mark were forbidden to decide anything, and the executing side's report
     states that they did not."* The L3 verdict pass's report (`records/cc/reports/cc_report_l3_candidate_list_and_verdict_pass_2026_10_14.md`
     §7(b)–(c), read whole) states that every verdict was written at each entry's `verbatim` and `plain` *"and
     nothing else"*, and does not name the register group or the LEGACY mark.
  3. §8: *"The criterion's reach is unmeasured, and §4 says so."* L3's §4 says every design-intent entry of the sort
     is a candidate and bounds the population to the sort.
  4. §7, ruled branch: *"Recorded beside the rulings, at the user's acceptance of the sitting's stated caveats:"* —
     true of the L2 record; **the 2026-10-15 record records no such acceptance**, it records the notes "beside the
     ruling".
  5. The list headings *"LIST ONE — IN: proposed to be WITHHELD from the pack"*, *"LIST TWO — OUT: proposed to be
     ADMITTED to the pack"*, and §4's *"the verdicts proposed in each"* — false once the lists are ruled.
  6. L3's own §6 first bullet: *"L3's pack is not rendered until the family is ruled and its members are ruled."* —
     stale once the family's lists are ruled.
  7. L3's own UNPLACED gloss: *"…a recommendation, with its grounds, comes on the decision surface that puts this list
     to you…"* — stale: the surface was put, carried a recommendation, and both entries were ruled IN.
  Items 1 to 3 are the record's §3. Items 4 to 7 are made wrong for L3 by this batch's own ruled rendering (L.3).
  **L2's ruled file carries items 1 to 5 in their L2 form and stays byte-identical**: it is the ruled L2 surface and is
  not re-rendered (see "What this batch deliberately leaves").
- **FACT — the untracked population Task 0 lands:** this dispatch; handoff entry 401
  (`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_one.md`, 8,200 bytes at the handoff folder's
  listing); the ruling record (`records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`,
  12,941 bytes at its staging). Handoff entry 402, if the writing side has written it by the time you boot, is NOT
  landed and is not a STOP.

- **ASSUMPTION A1 — the working tree, by content.** Tracked modifications at boot: **none expected**, except the
  line-ending-only marking of `tools/audit/claude_md_finer_archive.json` the last reports record — the last one at
  its §3, A1 (re-establish
  it; leave it untouched; never stage it). Any other tracked modification at boot or during the run is a
  STOP-and-report, except a path this batch writes, after the task that writes it and until its commit. A further
  untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md` appearing during the run is the writing side's and is
  NOT landed and NOT a STOP. **Check (Task 0, first act):** per tracked input this batch edits
  (`tools/audit/gen_derivation_boot_pack.py`, `tools/audit/gen_withheld_family_reading.py`,
  `ratification_surfaces/cowork_withheld_family_l3_reading.md`, `STATUS.md`, `STATUS_ARCHIVE.md`,
  `tools/audit/gen_status_batch_bound.py`)
  `git diff --stat a191a380b3c4b9621bb2628e754582376faf2bf6 -- <path>; echo "exit:$?"`; per path of Task 0's list
  `git ls-files --others --exclude-standard -- <path>; echo "exit:$?"`; the whole tracked population with
  `tools/audit/changed_paths.py`.
- **ASSUMPTION A2 — the guard run before the first edit:** the fourteen, exactly, and the classification tool's
  standing STOP naming the three tools above. **Predicted at the end state: run 80, historical 20, not run 4, failing
  the same fourteen**; `--subject l3 --check` and `--subject l2 --check` both PASS. Reds this batch's own acts may
  cause, classed by cause and NOT a STOP: `gen_withheld_family_reading.py --subject l3 --check` between Task 1's commit
  and Task 2's render (the table moved, the file not yet re-rendered — expected); `gen_l0_l1_outgoing_population.py
  --check` and `gen_defense_share.py --check` if Task 3's `STATUS.md` entries move their inputs — regenerate, compare
  against the committed blob by explicit hash, commit with the end state, report that no member moved (a member moving
  IS a STOP-and-report); `gen_session_start_read_size.py --check` if regenerated before the last `STATUS.md` edit;
  `gen_guard_state.py`'s own artifact until the end-state run. A red outside these is a STOP-and-report.
- **ASSUMPTION A3 — byte-unchanged by this batch, verified at the objects after the last commit:** every governing
  document except `STATUS.md` and `STATUS_ARCHIVE.md`; `tools/audit/gen_derivation_boot_pack.py` except Task 1's three
  tuples (in each, the verdict word and the reason only; the finding byte for byte); `tools/audit/gen_guard_state.py`
  (not edited at all); **`ratification_surfaces/cowork_withheld_family_l2_reading.md`** (the ruled L2 surface);
  `tools/audit/l3_candidate_list.json` and `tools/audit/l2_candidate_list.json`; every rendered decisions-register
  file; everything under `tools/audit/derivation_boot_pack/` and `tools/audit/derivation_boot_pack.json`; every
  ruling record (the 2026-10-15 one is only landed, as it stands), surface, extract, `FRAMEWORK.md` and the
  suspension file. Any other difference is a STOP-and-report.

## The standing bars, and the commit-and-push discipline

No `src/` edit, no golden, no test changed or run, no build, nothing under `tools/corpus/` or `tools/robust_stop/`,
**no measurement of the analysis built, designed, scoped or run**, no derivation of any specification statement,
**NO SESSION BOOTED, no pack rendered** (the generator runs in `--check` only; `write_all` is never reached), **no
`WITHHELD`, `EXTRAS`, `FROZEN` or `VERDICT_DATE` entry for `l3`, no edit to `CRITERION`, no edit to any verdict word,
finding or reason except the three of Task 1, and no edit to any other `VERDICTS` entry**, no open-items row created,
flipped or discarded, **no decisions-register entry and no `D-NNN` allocated, nothing written into the suspension
file**, no edit to any governing document except `STATUS.md`/`STATUS_ARCHIVE.md` in Task 3, **no re-render or edit of
the L2 reading file**, **no edit to the ruling record** (it is a dated record; Task 0 lands it as it stands), **no
ruling taken, and no question or recommendation put to the user**.

**Commit-and-push per task. Run the FULL guard set BEFORE the first edit (`python tools/audit/gen_guard_state.py
--check`) and again at the end (write mode, committed as the artifact of a real run). After every commit: push, then
read `.git/refs/remotes/origin/master` with the file tools and confirm it names the commit just made.** Verify every
commit at the object by explicit hash. Every shell command carries `; echo "exit:$?"`. `git status` and `git diff`
over the working tree are denied by the armed guard — use the explicit-hash forms of A1. Write every hash literally
in the command: a hash held in a shell variable is denied by the guard (the last report, §9 item 3). Plain
single-quoted `git commit -m '…'` subjects, or double quotes where the subject carries an apostrophe, declared.
Every working-tree read through the file tools (D-253); a run's output is redirected to a file in your session's
scratch folder outside the repository and read with the file tools; every script this dispatch orders is written
there too. Edit files with your file-editing tool, never by retyping a whole file. **If an old text quoted below does
not occur EXACTLY once in its file, that edit is a STOP-and-report for that edit alone**: make nothing for it,
report what you found, and — because Task 2's edits depend on one another — a STOP on any Task 2 edit restores the
tool by explicit hash and ends Task 2. The reserved-word rule binds every line you write: *score*, *key*, *note*,
*figure*, *register*, *measure*, *part*, *scale*, *tie* only in their musical senses, or qualified.

## The ordered first reads

**(1)** `records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md` WHOLE. **(2)**
`CLAUDE.md` at its six ruled spans (the membership at its "Build and test commands" block), `STATUS.md` whole,
`DECISIONS.md` whole; rule (a)'s `gating_ids` at `tools/audit/nongating_apparatus_rows.json` →
`★_the_live_gating_answer`. **(3)** `records/cowork/handoff/cowork_handoff_entry_four_hundred.md` and
`…four_hundred_and_one.md` whole. **(4)** `cowork_audit_protocol.md`'s dispatch-protocol section. **(5)** The last
batch: its dispatch `records/cc/instructions/cc_instruction_l3_reading_file_2026_10_15.md` whole, its report
`records/cc/reports/cc_report_l3_reading_file_2026_10_15.md` whole, its close (the last section of
`records/cowork/handoff/cowork_away_returns.md`). **(6)** The L2 model:
`records/cc/instructions/cc_instruction_l2_ruling_writeback_2026_09_05.md` at Tasks 1 and 2. **(7)**
`tools/audit/gen_withheld_family_reading.py` WHOLE. **(8)** The generator's `VERDICTS["l3"]` block WHOLE. **(9)**
`records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md` at §1b (Ruling 2). **(10)**
`records/cc/reports/cc_report_l3_candidate_list_and_verdict_pass_2026_10_14.md` at §7. **(11)**
`tools/audit/gen_status_batch_bound.py` whole at the object
`a191a380b3c4b9621bb2628e754582376faf2bf6:tools/audit/gen_status_batch_bound.py` before Task 3.

## Task 0 — land this dispatch, entry 401 and the ruling record, and PUSH

To be landed (the standing clause): `records/cc/instructions/cc_instruction_l3_ruling_writeback_2026_10_15.md`,
`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_one.md` and
`records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`. **Each path's standing at the
tip is yours to take under A1** (expected: all three UNTRACKED).

**The acts, in order:** **(1)** A1's check. A path already tracked is reported and not re-landed; entry 401 absent is
reported, not a STOP; the dispatch or the ruling record absent is a STOP. Report any other untracked path the
enumeration shows under `records/`, `reading_pass/` or `ratification_surfaces/` — NOT landed, not a STOP. **(2)** If
`tools/audit/gen_evidence_pin_membership.py --check` is red, regenerate `tools/audit/evidence_pin_membership.json`
and measure it against the committed blob: the only permitted change is its list of ruling records read; any other
movement is a STOP-and-report. **(3)** Commit the paths that exist and are untracked, plus the membership artifact
only if it moved. Subject, exactly:
`record: the L3 ruling write-back dispatch, entry 401 and the 2026-10-15 L3 lists ruling record landed`
(if entry 401 is absent, drop `, entry 401` from the subject). **(4)** PUSH; verify `origin/master` at the ref file.

**Under standing clause P-2 this dispatch is PINNED at Task 0:** record its blob, and prove it unmoved immediately
before staging it.

**E0:** the named paths in one commit; `origin/master` at the commit; every path accounted for.

## Task 1 — the three ruled verdicts, written back to the table; ONE commit

It cannot be stopped partway, so it goes first with nothing large in front (D-670).

**(a)** Run, and keep the output:
`cd C:\s\MS && python tools/audit/gen_derivation_boot_pack.py --check > <scratch>\dbp_before.txt 2>&1; echo "exit:$?"`.

**(b)** In `tools/audit/gen_derivation_boot_pack.py`, inside `VERDICTS["l3"]`, three replacements. **Each keeps the
tuple's FINDING string byte for byte and changes only the verdict word and the reason.** Each old text occurs once;
an occurrence outside `VERDICTS["l3"]` is a STOP-and-report.

**Edit (i) — D-605 → IN (Ruling 2), group E's block.** Old text (once):

```python
        "D-605": (VERDICT_OUT,
                  "Its verbatim rules that a local-key hypothesis derives from key-agnostic signals "
                  "only — the cadence detector and the raw region structure — and never from the "
                  "key-area grouping.",
                  "Its subject is what evidence a modulation decision may read, which is L2's tonality "
                  "decision; it names the cadence detector key-agnostic without stating how a cadence "
                  "is read off."),
```

New text:

```python
        "D-605": (VERDICT_IN,
                  "Its verbatim rules that a local-key hypothesis derives from key-agnostic signals "
                  "only — the cadence detector and the raw region structure — and never from the "
                  "key-area grouping.",
                  "Ruled IN 2026-10-15 from OUT (Ruling 2 of "
                  "`cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`): its subject is "
                  "L2's decision, but its published text states in passing that cadences are detected "
                  "without the key and from the decided chords, which is the core of D-336, withheld by "
                  "Ruling 1; admitted beside it, this entry would carry that answer into the pack "
                  "without citing D-336, and withholding it costs the deriving session nothing it needs, "
                  "L3 receiving the tonality settled."),
```

**Edit (ii) — D-459 → IN (Ruling 3), group H's block.** Old text (once):

```python
        "D-459": (VERDICT_UNPLACED,
                  "Its verbatim makes any confidence the grouping layer publishes — the key-area "
                  "confidence, a span-level aggregate — a Class M boundary confidence whose input is "
                  "the declared key confidence.",
                  "It was read as about key areas and a span aggregate, and the published text does not "
                  "settle whether key-area grouping belongs to L3's section grouping or a view of L2's "
                  "tonality."),
```

New text:

```python
        "D-459": (VERDICT_IN,
                  "Its verbatim makes any confidence the grouping layer publishes — the key-area "
                  "confidence, a span-level aggregate — a Class M boundary confidence whose input is "
                  "the declared key confidence.",
                  "Ruled IN 2026-10-15 from UNPLACED (Ruling 3 of the same record): D-454, withheld by "
                  "Ruling 1, names key-area grouping among the three things the grouping layer "
                  "assembles, so key areas belong to the grouping L3 derives; this entry states how "
                  "that grouping's confidence is formed, and the general confidence rules it applies "
                  "(D-032, D-267, D-268) are admitted by Ruling 2, so withholding it costs the deriving "
                  "session nothing it needs."),
```

**Edit (iii) — D-472 → IN (Ruling 3), group H's block.** Old text (once):

```python
        "D-472": (VERDICT_UNPLACED,
                  "Its verbatim groups neighboring regions in the same key into a key area by a "
                  "smoothing pass, a disagreeing region below the confidence test keeping its own key.",
                  "It was read as a grouping rule over key areas, and the published text does not "
                  "settle whether key-area grouping belongs to L3's section grouping or a view of L2's "
                  "tonality."),
```

New text:

```python
        "D-472": (VERDICT_IN,
                  "Its verbatim groups neighboring regions in the same key into a key area by a "
                  "smoothing pass, a disagreeing region below the confidence test keeping its own key.",
                  "Ruled IN 2026-10-15 from UNPLACED (Ruling 3 of the same record): D-454, withheld by "
                  "Ruling 1, names key-area grouping among the three things the grouping layer "
                  "assembles, and this entry's own text calls it a grouping rule that reads the key "
                  "fields earlier layers published and re-decides none of them; it states how spans are "
                  "grouped by key, a rule L3 derives itself, so admitting it would hand the deriving "
                  "session that answer."),
```

**(c)** Re-run (a) to `<scratch>\dbp_after.txt`: **the output byte-identical to the before file and the same exit
code** (compare by `cmp` and report it). Any difference: restore the generator to `a191a380…` by explicit hash, make
no commit, report, and END THE BATCH at Task 3's report (Task 2 renders from the table and must not run on a table
whose inertness failed).

**(d)** Run `cd C:\s\MS && python tools/audit/gen_withheld_family_reading.py --subject l3 --check > <scratch>\rf_l3_after_t1.txt 2>&1; echo "exit:$?"`.
**Expected: `FAIL: ratification_surfaces/cowork_withheld_family_l3_reading.md differs from what the generator now
renders`, exit 1** — the table moved and the file has not yet been re-rendered. That FAIL is the tool doing its job,
not a STOP; Task 2 clears it. **Do not re-render here.** A `STOP:` line is a STOP-and-report.

**(e)** Re-read the three tuples with the file tools and quote them in the report. Commit the generator alone:
`audit(l3): the 2026-10-15 rulings written back — D-605, D-459 and D-472 to IN; findings unchanged (former: D-605 OUT, D-459 and D-472 UNPLACED)`.
Push; verify.

**E1:** the three old texts each found once; the byte-identity reported; the expected FAIL reported; the commit
pushed.

## Task 2 — the reading-file tool: L3's ruling block, the shared sentences moved per subject; L3's file re-rendered as RULED: ONE commit

### (a) Before the first edit

Run, and keep: `cd C:\s\MS && python tools/audit/gen_withheld_family_reading.py --subject l2 --check > <scratch>\rf_l2_before.txt 2>&1; echo "exit:$?"`.
**Expected: `PASS: ratification_surfaces/cowork_withheld_family_l2_reading.md re-renders byte-identically`, exit 0.**
Anything else is a STOP-and-report before any edit.

### (b) The edits to `tools/audit/gen_withheld_family_reading.py`, in this order

**THE PRINCIPLE OF EVERY EDIT BELOW:** each shared sentence that is wrong for L3 moves out of `render()`, unchanged,
into `SUBJECTS["l2"]`, and `render()` writes it from there; `SUBJECTS["l3"]` carries L3's own text. For `l2` the
rendered file must stay byte-identical — (d) proves it.

**Edit 1 — the `l2` entry gains its copies of the shared sentences.** Old text (once):

```python
            "list, in the fixed group order that dispatch names"),
        # RULED.  Present only once the user has ruled the lists; a subject without this block
```

New text:

```python
            "list, in the fixed group order that dispatch names"),
        # ── SHARED SENTENCES MADE PER SUBJECT.  Moved here from render() on 2026-10-15 by
        #    `cc_instruction_l3_ruling_writeback_2026_10_15.md` Task 2, because each is true of L2 and
        #    wrong for L3 (§3 of `cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`, and the
        #    user's rule of 2026-09-22).  Every string below is the text render() wrote for L2 before the
        #    move, byte for byte; the proof is that `--subject l2 --check` passes before and after.
        "verdict_word": "proposed",
        "banner_ruled_tail": (
            "> boot-list members are ruled, which is a separate decision (Ruling 81, §3cj of",
            "> `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *no identity is withheld that the user",
            "> has not ruled*).",
        ),
        "banner_unruled_tail": (
            "> No identity is withheld, no pack is rendered and no session is booted until you have ruled the",
            "> lists (Ruling 81, §3cj of `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *no identity",
            "> is withheld that the user has not ruled*).",
        ),
        "section_5_tail": (
            "document was opened to decide one; the register group and the LEGACY mark were forbidden to",
            "decide anything, and the executing side's report states that they did not.",
        ),
        "section_8_completeness": (
            "- **It does not claim the candidate list is complete.** The criterion's reach is unmeasured, and",
            "  §4 says so.",
        ),
        "ruled_notes_heading": "**Recorded beside the rulings, at the user's acceptance of the sitting's stated caveats:**",
        # RULED.  Present only once the user has ruled the lists; a subject without this block
```

**Edit 2 — the `l3` entry's heading comment.** Old text (once):

```python
    # Ruling 2 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`: the lists are ruled one
    # per turn, as for L2, from a surface rendered from the table.  No `ruling` block: the lists are
    # not ruled, so the file renders as a reading surface FOR RULING.
```

New text:

```python
    # Ruling 2 of `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`: the lists are ruled one
    # per turn, as for L2, from a surface rendered from the table.  The lists were ruled 2026-10-15
    # (`records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`); the
    # per-subject sentences and the `ruling` block at the end of this entry were added by
    # `cc_instruction_l3_ruling_writeback_2026_10_15.md` Task 2, so the file renders as RULED.
    # (Former wording, preserved (#12): "No `ruling` block: the lists are not ruled, so the file
    # renders as a reading surface FOR RULING.")
```

**Edit 3 — L3's §6 first bullet.** Old text (once):

```python
            "  rendered, and L3's pack is not rendered until the family is ruled and its members are ruled.",
```

New text:

```python
            "  rendered, and L3's pack is not rendered until its members are ruled; the family's three lists",
            "  are ruled (§7).",
```

**Edit 4 — L3's UNPLACED gloss, its per-subject sentences and its ruling block.** Old text (once):

```python
        # The UNPLACED list's heading, corrected for this subject.  The shared heading cites D-658 for
        # making no recommendation; that requirement of D-658 is superseded (`CLAUDE.md`, Conventions,
        # the order of a decision surface's rules, step 8).  L2's ruled file keeps the shared heading.
        "unplaced_gloss": (
            "These could not be defended either way in one sentence at the entry's own verbatim, so "
            "they were not guessed.  Each row says what was read.  This file makes no recommendation on "
            "any of them; a recommendation, with its grounds, comes on the decision surface that puts this "
            "list to you (`CLAUDE.md`, Conventions, the order in which a decision surface's rules apply, "
            "step 5)."),
    },
}
```

New text:

```python
        # The UNPLACED list's heading, corrected for this subject.  The shared heading cites D-658 for
        # making no recommendation; that requirement of D-658 is superseded (`CLAUDE.md`, Conventions,
        # the order of a decision surface's rules, step 8).  L2's ruled file keeps the shared heading.
        # Brought to the RULED state 2026-10-15.  (Former wording, preserved (#12): "…Each row says what
        # was read.  This file makes no recommendation on any of them; a recommendation, with its
        # grounds, comes on the decision surface that puts this list to you (`CLAUDE.md`, Conventions,
        # the order in which a decision surface's rules apply, step 5).")
        "unplaced_gloss": (
            "These could not be defended either way in one sentence at the entry's own verbatim, so "
            "they were not guessed.  The verdict pass placed two entries here; they were put to you on a "
            "decision surface carrying a recommendation with its grounds (`CLAUDE.md`, Conventions, the "
            "order in which a decision surface's rules apply, step 5), and both were ruled IN (§7, "
            "Ruling 3), so the list is empty."),
        # ── THE PER-SUBJECT SENTENCES, L3's text (see the same keys in the `l2` entry) ────────────
        "verdict_word": "ruled",
        "banner_ruled_tail": (
            "> boot-list members are ruled, which is a separate decision (Ruling 2 of",
            "> `records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`: *No identity is",
            "> withheld that the user has not ruled.*)",
        ),
        "banner_unruled_tail": (
            "> No identity is withheld, no pack is rendered and no session is booted until you have ruled the",
            "> lists (Ruling 2 of `records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`:",
            "> *No identity is withheld that the user has not ruled.*)",
        ),
        "section_5_tail": (
            "document was opened to decide one.  The executing side's report",
            "(`records/cc/reports/cc_report_l3_candidate_list_and_verdict_pass_2026_10_14.md` §7) states that",
            "every verdict was written at the entry's verbatim and plain restatement *\"and nothing else\"*.",
        ),
        "section_8_completeness": (
            "- **It does not claim the candidate list is complete.** Every design-intent entry of the sort is a",
            "  candidate, but decisions-register entries outside the sort, and rulings recorded only in a ruling",
            "  record, are reached by no term; §4 states that bound.",
        ),
        "ruled_notes_heading": "**Recorded beside the rulings in the ruling record:**",
        # RULED 2026-10-15.  Every string below is the ruling record's own content, cited to it, and the
        # verdict table carries the ruled verdicts themselves.  No `test_note`: no ruling changed L3's
        # test, so §2 and §5 state it as the verdict pass applied it.
        "ruling": {
            "record": "records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md",
            "date": "2026-10-15",
            "rulings": (
                "**Ruling 1 — LIST ONE stands as authored: all 19 IN entries are withheld** (the user's "
                "word: \"A\").",
                "**Ruling 2 — LIST TWO: 222 of the 223 OUT entries are admitted; D-605 moves to IN "
                "(withheld)** (the user's word: \"B\").",
                "**Ruling 3 — LIST THREE: D-459 and D-472 are both IN (withheld)** (the user's words: "
                "\"A, both IN\").  The list is now empty; the three moved verdicts were written back to "
                "the table by `cc_instruction_l3_ruling_writeback_2026_10_15.md`, and the lists below "
                "are the ruled lists.",
            ),
            "notes": (
                "**Ruling 1, the overlap with the charter.** Some IN entries state what L3's own charter "
                "block in `FRAMEWORK.md` §5 already states: D-526 (the root is the tonic transposed by the "
                "degree's interval), and parts of D-477 and D-455 (the notated phrase evidence read at L1; a "
                "phrase span's boundaries come from the notated cues and the cadence is aligned to them).  "
                "Where the charter is in L3's pack, withholding these hides nothing the session will not "
                "read there; they are kept IN and the overlap is recorded as harmless.  Whether the charter "
                "is in L3's pack is UNSETTLED: L3's boot-list members are a later ruling.",
                "**Ruling 1, also recorded.** D-022, D-336 and D-526 are also IN in L2's ruled family; they "
                "bear on both layers.",
                "**Ruling 2.** D-605's subject is L2's decision, but its published text states in passing "
                "that cadences are detected without the key and from the decided chords, which is the core "
                "of D-336, withheld by Ruling 1; admitted beside a withheld D-336 it would carry that answer "
                "into the pack, and Ruling 84's automatic cross-reference addition does not reach it, "
                "because it does not cite D-336.  D-605 is also IN in L2's ruled family.  D-484 was "
                "considered and kept OUT: it describes the form of the evidence the layer below publishes, "
                "which L3 consumes, and does not say how phrase ends are picked.",
                "**Ruling 2, the bound on the check behind it.** Every one of the 223 OUT rows was read in "
                "the rendered file; the full published text was read in the candidate list for D-268, "
                "D-471, D-482, D-484 and D-605 only.  A further restatement of a withheld entry elsewhere "
                "in LIST TWO is not excluded by that read.",
                "**Ruling 3.** D-454, withheld by Ruling 1, names key-area grouping among the three things "
                "the grouping layer assembles, and D-472's own text says it reads the key fields earlier "
                "layers published and re-decides none of them; so key-area grouping is placed with the "
                "grouping L3 derives.  The general confidence rules D-459 applies (D-032, D-267, D-268) are "
                "admitted by Ruling 2.  `FRAMEWORK.md` does not define \"section\", so whether key areas are "
                "\"section grouping\" in its sense is UNSETTLED; the ruling rests on the record's placement "
                "of key-area grouping in the grouping layer, not on that definition.",
            ),
        },
    },
}
```

**Edit 5 — the RULED banner's citation.** Old text (once):

```python
        w("> boot-list members are ruled, which is a separate decision (Ruling 81, §3cj of")
        w("> `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *no identity is withheld that the user")
        w("> has not ruled*).")
```

New text:

```python
        for line in spec["banner_ruled_tail"]:
            w(line)
```

**Edit 6 — the unruled banner's citation.** Old text (once):

```python
        w("> No identity is withheld, no pack is rendered and no session is booted until you have ruled the")
        w("> lists (Ruling 81, §3cj of `cowork_rulings_2026_08_31_decision_surface_sitting.md`: *no identity")
        w("> is withheld that the user has not ruled*).")
```

New text:

```python
        for line in spec["banner_unruled_tail"]:
            w(line)
```

**Edit 7 — §2's test note, optional.** Old text (once):

```python
    if ruling:
        w("")
        w(ruling["test_note"])
    w("")
    for line in spec["section_3"]:
```

New text:

```python
    # A ruling block carries `test_note` only where a ruling changed the test (L2's Ruling 1(a)).
    if ruling and "test_note" in ruling:
        w("")
        w(ruling["test_note"])
    w("")
    for line in spec["section_3"]:
```

**Edit 8 — §5's test note, optional.** Old text (once):

```python
    if ruling:
        w("")
        w(ruling["test_note"])
    w("")
    w("**Default nothing:** a verdict that could not be defended in one sentence at the entry's own")
```

New text:

```python
    if ruling and "test_note" in ruling:
        w("")
        w(ruling["test_note"])
    w("")
    w("**Default nothing:** a verdict that could not be defended in one sentence at the entry's own")
```

**Edit 9 — §5's last sentence.** Old text (once):

```python
    w("document was opened to decide one; the register group and the LEGACY mark were forbidden to")
    w("decide anything, and the executing side's report states that they did not.")
```

New text:

```python
    for line in spec["section_5_tail"]:
        w(line)
```

**Edit 10 — §4's table heading.** Old text (once):

```python
    w("**The candidates by register group, and the verdicts proposed in each:**")
```

New text:

```python
    w(f"**The candidates by register group, and the verdicts {spec['verdict_word']} in each:**")
```

**Edit 11 — the two list headings.** Old text (once):

```python
        "LIST ONE — IN: proposed to be WITHHELD from the pack",
```

New text:

```python
        "LIST ONE — IN: {verdict_word} to be WITHHELD from the pack",
```

Old text (once):

```python
        "LIST TWO — OUT: proposed to be ADMITTED to the pack",
```

New text:

```python
        "LIST TWO — OUT: {verdict_word} to be ADMITTED to the pack",
```

Old text (once):

```python
        heading, gloss = LIST_HEADINGS[verdict]
```

New text:

```python
        heading, gloss = LIST_HEADINGS[verdict]
        heading = heading.replace("{verdict_word}", spec["verdict_word"])
```

**Edit 12 — §7's notes heading.** Old text (once):

```python
        w("**Recorded beside the rulings, at the user's acceptance of the sitting's stated caveats:**")
```

New text:

```python
        w(spec["ruled_notes_heading"])
```

**Edit 13 — §8's completeness bullet.** Old text (once):

```python
    w("- **It does not claim the candidate list is complete.** The criterion's reach is unmeasured, and")
    w("  §4 says so.")
```

New text:

```python
    for line in spec["section_8_completeness"]:
        w(line)
```

### (c) The self-check of the edits, before any run

Copy the tip's object to scratch with
`git show a191a380b3c4b9621bb2628e754582376faf2bf6:tools/audit/gen_withheld_family_reading.py > <scratch>\rf_tool_tip.py; echo "exit:$?"`
and compare it with the edited working-tree file using the file tools, or with the explicit-hash form
`git diff -U0 a191a380b3c4b9621bb2628e754582376faf2bf6 -- tools/audit/gen_withheld_family_reading.py` written to
scratch (the form the last batch used and declared). Every removed line must be one of the old texts above; every
added line one of the new texts. Anything else is a STOP-and-report (restore by explicit hash; end Task 2).

### (d) L2 is untouched — the proof

Run `--subject l2 --check` to `<scratch>\rf_l2_after.txt`. **Expected: byte-identical to `rf_l2_before.txt`, exit 0**
(compare by `cmp`). A FAIL means one moved L2 string differs from what `render()` wrote: **do not re-render the L2
file**; restore the tool by explicit hash, report which edit's string differs if you can find it, and end Task 2.

### (e) Render L3's file and check it

Run `python tools/audit/gen_withheld_family_reading.py --subject l3` (it prints `wrote … (N bytes)`), then
`--subject l3 --check` (expected `PASS`, exit 0). A `STOP:` from either run is a STOP-and-report: delete nothing by
hand, restore the tool by explicit hash, leave the rendered file uncommitted, report the message, end Task 2.

**Then READ the rendered file WHOLE** and confirm with `Grep`, reporting each:

- the banner's first line begins `> **STATUS: RULED 2026-10-15` and the next names
  `records/cowork/rulings/cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`;
- `Ruling 81` occurs **nowhere** in the file, and the banner cites Ruling 2 of
  `records/cowork/rulings/cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`;
- `fifth ground` occurs nowhere (no `test_note` for L3);
- `proposed to be` occurs nowhere; the headings read `## LIST ONE — IN: ruled to be WITHHELD from the pack` and
  `## LIST TWO — OUT: ruled to be ADMITTED to the pack`; §4's heading reads `the verdicts ruled in each`;
- LIST ONE carries `**22 entries.**`, LIST TWO `**222 entries.**`, LIST THREE `**0 entries.**` followed by the
  sentence beginning `*The list is empty on this run.`;
- the summary table's last row reads `| **all** | | **244** | **22** | **222** | **0** |`;
- the rows matching `^\| D-\d+ \|` number **244**;
- `D-605`, `D-459` and `D-472` each appear between the LIST ONE and LIST TWO headings;
- `## 7. What was ruled` is present, `## 7. What you are asked to rule` is absent, and §7 carries
  `**Recorded beside the rulings in the ruling record:**`;
- `The criterion's reach is unmeasured` and `at the user's acceptance` occur nowhere; §8 carries
  `§4 states that bound`; §5 carries `and nothing else`.

Any of these failing is a STOP-and-report (restore the tool by explicit hash, leave the rendered file uncommitted,
end Task 2). **Do not paste the file or its counts into the report beyond these confirmations; cite it (D-431).**

### (f) Check the ruling block and the three reasons against the record

With the file tools, open the ruling record (landed at Task 0) and confirm: the three `rulings` strings say what the
record's three ruling headings say, with the user's words `"A"`, `"B"`, `"A, both IN"`; the five `notes` strings are
the record's Ruling 1 "Recorded beside the ruling" and "Also recorded" paragraphs, Ruling 2's ground, alternative (C)
and bound, and Ruling 3's ground and UNSETTLED paragraph; the three reasons of Task 1 rest on the record's grounds at
§1c and §1d; the citation for *"No identity is withheld that the user has not ruled."* is at §1b of the 2026-10-14
record. **A disagreement between a string and the record is a finding about this dispatch: report it, follow the
record, and declare the correction.**

### (g) Commit the two paths together

`tools/audit/gen_withheld_family_reading.py` and `ratification_surfaces/cowork_withheld_family_l3_reading.md` — and
nothing else. Subject:
`audit(l3): the reading file re-rendered as RULED — L3's ruling block; the shared sentences wrong for L3 moved per subject, L2's file byte-unchanged`
(double-quoted, for its apostrophes; declare it). Push; verify.

Then run `python tools/audit/gen_guard_state.py --check` to scratch and read it: **expected 80 run, the same fourteen
failing, both reading-file runs passing**, plus the runner's own *"STALE vs the run"* line for its artifact.

**E2:** (a) PASS; (c) clean; (d) byte-identical; (e) PASS and every confirmation reported; (f) no disagreement, or
each reported and followed; the commit pushed.

## Task 3 — the close

1. **The `STATUS.md` entries and the forward-bound move, IN THIS ORDER** (read `gen_status_batch_bound.py` whole at
   the object first, ordered first read (11)). **(a)** Write this batch's entries at the top of `STATUS.md`: one pointer
   entry per task that did work — the close entry FIRST, NAMING THIS DISPATCH BY ITS FILE NAME
   (`records/cc/instructions/cc_instruction_l3_ruling_writeback_2026_10_15.md`), each earlier task's entry below it
   saying `Same dispatch`; no figure restated (D-431); the entry says that the lists stand RULED, that nothing is
   withheld, no pack rendered, no session booted, no `D-NNN` allocated and no open-items row touched. **The `Last
   updated: ` prefix moves from the last batch's close entry (the topmost at the tip, naming
   `cc_instruction_l3_reading_file_2026_10_15.md`) to your newest entry.** **(b)** Re-aim the five authored constants
   of `gen_status_batch_bound.py`: `BASE_COMMIT` (this batch's last task commit before the close),
   `PREVIOUS_BATCH_DISPATCH` (`cc_instruction_l3_reading_file_2026_10_15.md`), `ACT_DATE` (the day the move runs),
   `DISPATCH` (`cc_instruction_l3_ruling_writeback_2026_10_15.md`), `TASK` (`Task 3`); append your own aiming to
   `PREVIOUS_AIMINGS` on the convention its comments state (every aiming exactly once; the last batch's aiming is
   already its last row). **(c)** Run `gen_status_batch_bound.py --apply`. **Prediction:** it moves **exactly the
   last batch's four entries** (its close entry and the three `Same dispatch` entries for Tasks 2, 1 and 0, read at
   `STATUS.md` at the tip); the two 2026-09-02 entries stay. If it STOPs, restore its passing aim, re-run green,
   report, move nothing by hand. **(d) LAST**, after the final `STATUS.md` edit, regenerate
   `gen_session_start_read_size.py` and confirm its `--check` green. Commit the re-aimed tool,
   `tools/audit/status_batch_bound.json`, `STATUS.md`, `STATUS_ARCHIVE.md` and the read-size artifact together in the
   close.
2. **The report**, `records/cc/reports/cc_report_l3_ruling_writeback_2026_10_15.md`, which decides nothing and
   recommends nothing: both guard states; every commit hash (or a pointer to the git log where it cannot contain
   one); E0 to E3 and A1 to A3 graded; Task 1's three tuples quoted after the edit, the byte-identity and the expected
   FAIL; Task 2's (a), (c), (d), (e) and (f) results; declared departures; and the plan's tell in one sentence — did
   this batch produce anything other than the landed paths, the three verdicts, the tool's edits, L3's re-rendered
   file, the Task 3 files and the report? If yes, name it.
3. **The full close appended to `records/cowork/handoff/cowork_away_returns.md`** as a section headed **THE L3
   RULING WRITE-BACK: THE THREE RULINGS IN THE VERDICT TABLE, L3's READING FILE RE-RENDERED AS RULED, NOTHING
   WITHHELD, NO PACK, NO ALGORITHM CHANGED** (if a task stopped, the heading says so) — the report's content as
   pointers, and the plan line: **the next act is the writing side's — the check of this batch's return at the
   objects, then L3's boot-list members (a separate ruling).**
4. **The close does not assert the end state**; one further commit carries it. Commit the close, push, verify; then
   the full guard run in write mode at that tree, the A2 exceptions handled as A2 says, and the one further commit
   with its artifacts, pushed and verified. Re-run `gen_guard_classification.py --check` after it and report the
   message (expected: the standing STOP naming the same three tools).

**E3:** at the tree carrying the close, a fresh full guard run — the A2 prediction (80 run, 20 historical, 4 not run,
failing the fourteen named) — committed only after the run that produced it.

## What this batch does NOT do

- **No withheld identity, no pack, no session.** The ruled lists stand in the table and in the reading file; the
  family is authored from LIST ONE in a later act, with L3's pack members, which are a separate ruling.
- **No change to what any layer computes** as its specification defines it. Every edit is in a dormant table of
  verdicts, a reading-file tool, or the file it renders.
- **No re-render of L2's ruled reading file.**
- **No decisions-register entry, no `D-NNN`, nothing in the suspension file, no ruling taken.**

## What this batch deliberately leaves to later acts, named so it is not lost

- **`VERDICT_DATE["l3"]`** and **`criterion_block()`'s fixed bullet** (*"its `group` is E — Layer 2, the slicer"*) —
  owed to the batch that builds L3's pack.
- **L3's boot-list members** — a separate ruling, the next decision for the user.
- **The six drifted register anchors and the eight stale derived `home_section` blocks** — register maintenance;
  cause first (D-669).
- **L2's ruled reading file keeps its L2 text** of the sentences this batch makes per subject — the Ruling 81
  citation, the "proposed" headings, the §5 and §8 sentences, the notes heading — and its UNPLACED heading's D-658
  citation (entry 400 §2). They are L2's ruled surface as it stands; whether any is wrong for L2 was not examined by
  this dispatch, and re-rendering that file is not ordered here.
- **The tool's docstring** still says it *"makes no recommendation on any UNPLACED entry (D-658)"*; it renders
  nothing and was left as it stands.

## The writing side's self-check, run before this dispatch was released (D-434)

1. *Principles.* #6 — one verdict table, one reading-file tool, one ruling block per subject; the moved L2 sentences
   leave `render()` and exist once. #12 — every rewritten reason names the former verdict word; the replaced comment
   and gloss keep their former wording in the tool; L2's ruled file untouched. #13/#18 — every inertness claim proven
   by a before/after comparison (Task 1(c), Task 2(d)). #17f/D-431 — the counts are the ruling record's arithmetic
   and are read back at the rendered file, not carried. #19 — both reading-file runs stay guarded.
2. *Conventions.* American English; the vocabulary block precedes first use; *decisions-register* qualified where
   written; *check*, *script*, *generator*, never *instrument*.
3. *The bars.* Three verdicts and no more; nothing withheld; no `WITHHELD`, `EXTRAS`, `FROZEN` or `VERDICT_DATE`
   entry for `l3`; no pack, no session; no register entry; the ruling record untouched; no question to the user.
4. *Documentation and algorithm.* Nothing here changes the algorithm as any specification defines it.

*Provenance: Cowork writing side, 2026-10-15 (Stockholm), the sitting booted on entry 401, at tip
`a191a380b3c4b9621bb2628e754582376faf2bf6` read as files; no shell command was run. **Read by the writing side, at the
extent named:** the boot read of entry 291 §4 step 3 (`CLAUDE.md` at its six ruled spans; `DECISIONS.md`,
`STATUS.md` whole; the gating answer; entry 118's bridge-fault section; entry 152's (v) to (x); entry 169 whole);
entries 291, 399, 400 and 401 whole; the 2026-10-15 ruling record whole; the 2026-10-14 L3 ruling record whole; the
L2 model dispatch whole; the last batch's dispatch and report whole; the L3 verdict-pass report whole;
`gen_withheld_family_reading.py` WHOLE; the generator's `VERDICTS["l3"]` block WHOLE and by search for the three
tuples' lines; `guard_state.json` at `summary`; `.git/HEAD`, both ref files and `.git/logs/HEAD` at the tip's line;
the L3 reading file by search for its headings and banner. **NOT read:** the last batch's close in
`cowork_away_returns.md`, `cowork_audit_protocol.md`, `gen_status_batch_bound.py`, `gen_guard_state.py`, the L2
reading file, `FRAMEWORK.md`.*

## The writing side's check of this dispatch at its sources (recorded per the standing clause and D-434; run 2026-10-15 in a turn of its own, after the user's "continue")

**Checked at the objects and holding.** Every single-line anchor of Task 2's thirteen tool edits occurs exactly once
in the tool as staged (the `verdicts_authored` closing line, the L3 comment line, L3's §6 line, L3's UNPLACED comment
line, both banner lines, the two list headings, the `LIST_HEADINGS` lookup, §4's heading, §5's line, the notes
heading, §8's line); the two `ruling["test_note"]` lines occur twice, as expected, and Edits 7 and 8 each carry a
following line that occurs once. **Every L2 string Edit 1 moves equals the tool's `w()` line character for
character**: the eleven strings were searched as literals in both files and found once in each. Task 1's anchor
lines were searched in the generator: each tuple's first line, its finding's last line and its reason's last line
are at the positions the `l3` block holds, and the finding lines occur once. The ruling block and the three reasons
were read against the 2026-10-15 record (§1, §1c, §1d) and the citation against §1b of the 2026-10-14 record.
`Ruling 81`, `fifth ground` and `proposed to be` were searched in the current L3 file: they occur only at the lines
this batch's edits replace, so Task 2(e)'s "nowhere" expectations follow from the edits.

**Corrected at their sites.** (1) The premise ledger said L2's ruled file carries "items 2 to 5" of the shared
sentences; it carries items 1 to 5 (the Ruling 81 citation is in its banner). (2) The claim that nothing in the
generator reads `VERDICTS["l3"]` was stated as this side's FACT; it is relayed, and now says so. (3) A1 said "the
last four reports" record the line-ending case; that count was not derived, and the sentence now points at the last
report.

**Not established by this check:** that the multi-line old texts match beyond the lines searched (they were copied
from the files as read, and the exactly-once rule turns any mismatch into a STOP); that the tool renders without
error after the edits (no shell; Task 2(e) is the test); the A2 failing names' order in a fresh run.
