# CC dispatch — L3's PACK BUILD, FIRST HALF: the records landed, L2's spent pack frozen, L3's verdict date and the criterion bullet, L3's withheld documents DERIVED AND PRINTED, the two input-contract copies cut — ENDING ON THE STOP FOR THE USER'S CONFIRMATION; NOTHING withheld, NO pack rendered, NO algorithm change, NO register entry, NO session booted

> **★★ RELEASED 2026-10-15** by the Cowork sitting booted on
> `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eight.md`, which wrote it, after the check at the
> sources recorded at the end of this file. It is executed by Claude Code when the user hands it over (D-252); the
> Cowork writing side never runs it. *(The banner this replaces read, preserved (#12): "**★★ DRAFT UNDER CONSTRUCTION
> BY THE COWORK WRITING SIDE — NOT TO BE HANDED TO CLAUDE CODE.** Claude Code: if you are reading this banner, STOP at
> once, do nothing, and report that you were handed an unfinished draft.")*

## What this batch is, in plain words

On 2026-10-15 the user ruled what the session that derives L3's detail specification reads at boot
(`records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, six rulings), which first-pass extracts
it reads (`…_l3_first_pass_extracts_sitting.md`), which scores are staged for it (`…_l3_staged_score_set_sitting.md`)
and which seven passages are cut from its two input-contract specifications (`…_l3_cut_lists_sitting.md`). Ruling 5
of the boot-list record orders the pack-build dispatch to derive L3's withheld documents, print them, and **STOP for
the user's confirmation before they are authored**. This batch is everything that comes before that STOP:

1. **Task 0** lands the Cowork side's records of 2026-10-15 and the four extract files of entries 405–406, and pushes.
2. **Task 1** freezes L2's spent pack at the blobs it carries (boot-list Ruling 1, noted: *"L2's pack must be frozen
   before L3's is built"*).
3. **Task 2** writes `VERDICT_DATE["l3"]` and makes `criterion_block()`'s group bullet true for every subject.
4. **Task 3** derives L3's withheld documents by giving the existing L2 derivation tool a `--subject` parameter,
   writes the L3 artifact, enrols its check, and **prints the set**.
5. **Task 4** writes the two cut input-contract copies under `tools/audit/derivation_exemplars/l3/`, the seven ruled
   cuts each located by its quoted text, and reports a search over them that cuts nothing.
6. **Task 5** closes, and **the batch ends on the STOP**: the derived document set goes to the user through the
   writing side. Nothing is authored into `WITHHELD["l3"]` or `EXTRAS["l3"]` here.

**Documentation and algorithm.** Every ruling this batch executes decides only what a future deriving session reads.
This batch edits a dormant table, a manifest, a derivation tool, and writes two cut copies of ratified documents.
**Nothing here changes the algorithm as any specification defines it.** The currently decided method for L3 is
`FRAMEWORK.md` §5's L3 block with DP-I (*"split — cues at L1, type at L3"*).

## Words used in this dispatch, explained first

- **Boot pack, member, extra, withheld family, verdict (IN / OUT / UNPLACED), guard set, red** — as defined in
  `records/cc/instructions/cc_instruction_l3_ruling_writeback_2026_10_15.md`, "Words used in this dispatch", and in
  the docstring of `tools/audit/gen_derivation_boot_pack.py` (the generator). **IN** means withheld from the pack.
- **Spent subject / FROZEN** — a subject whose deriving session has run. Its pack is no longer an input to be kept
  current; it is the record of what that session was given. `FROZEN` in the generator pins each of its files at one
  digest, and `write_all` writes nothing into a frozen directory (D-646; Ruling 17(a) of
  `cowork_rulings_2026_08_31_decision_surface_sitting.md`).
- **A digest** — the git blob hash of a file's own bytes, the value `git hash-object <file>` prints.
- **The manifest** — `tools/audit/derivation_boot_pack.json`, written by the generator.
- **The criterion bullet** — the first line of the list `criterion_block()` writes under the key *"a candidate is
  every DESIGN-INTENT entry meeting ANY of"*, today the fixed string *"its `group` is E — Layer 2, the slicer"*.
- **Home document** — the part before the first `:` of a decisions-register entry's `home` string.
- **Input contract** — a ratified specification of a lower layer, given to a deriving session as what it receives,
  cut of every passage stating the deriving layer's own ruled or current design (Ruling 2 of the boot-list record).
- **A cut copy** — a copy of a source document with named passages removed where they stood, with no mark, and a
  short head naming its source. It is not a second version of the source (#6).

## The ruling ledger

| | Record or rule | What it orders | Task |
|---|---|---|---|
| L.1 | The standing clause (a sitting record lands at the next dispatch's Task 0) | The 2026-10-15 records, entries 402–409, the cut-list document and the four extract files of entries 405–406, landed as they stand. | 0 |
| L.2 | Boot-list Ruling 1, "Noted, not ruled, for the pack-build dispatch" | L2's pack frozen before L3's is built; housekeeping under the user's rule of 2026-09-22. | 1 |
| L.3 | Entries 398 §2, 399 §2, 401 §3 item 7 (owed items) | `VERDICT_DATE["l3"]`; `criterion_block()`'s fixed bullet, false for `l2` and `l3`. | 2 |
| L.4 | Boot-list Ruling 5 | The home documents of the 22 IN entries derived from the register's data file and the ruled `VERDICTS["l3"]`, printed, and a STOP for the user's confirmation before `WITHHELD["l3"]["withheld_documents"]` is authored. | 3, 5 |
| L.5 | Boot-list Ruling 2; Ruling 1 of `…_l3_cut_lists_sitting.md` | Both specifications cut of exactly the seven passages of §2 of `ratification_surfaces/cowork_l3_input_contract_cut_lists_2026_10_15.md`, each located by its quoted text, a STOP unless found exactly once; the cut copies point back to their sources. | 4 |
| L.6 | The user's standing rule (entry 393 §2; 2026-10-14) | Every commit is pushed, and the push is verified at `.git/refs/remotes/origin/master`. | all |

## Premise ledger (written 2026-10-15 by the writing side from staged copies read with the file tools; no shell command and no git command was run by the writing side, so every identity only a git query gives is yours to take)

- **FACT — the tip.** `.git/HEAD` → `ref: refs/heads/master`; `.git/refs/heads/master` and
  `.git/refs/remotes/origin/master` both `5499f3e2521c2bf4478469f30f3b9fb18f0af655` (the end state of the L3 ruling
  write-back batch, entry 402 §1). **Re-read both ref files yourself before Task 0.**
- **FACT — the guard start state, at `tools/audit/guard_state.json` → `summary`:** run 80, passing 66, failing 14.
  The fourteen are the fourteen the write-back dispatch names in its premise ledger, `gen_derivation_boot_pack.py`
  among them; the writing side read the first nine names at the artifact and relies on that dispatch and entry 403 §1
  for the rest **[relayed]**. The classification tool `gen_guard_classification.py --check` ends on its standing STOP
  naming `gen_l0_l1_outgoing_population.py`, `gen_l2_withheld_documents.py` and `gen_withheld_family_reading.py`
  **[relayed]**.
- **FACT — two items earlier records carried for this batch are ALREADY DONE and are NOT in it.** (i) The two reds of
  entry 393 §1: at `guard_state.json`, `decisions/gen_retired_subject_moves.py --check` is `PASS`, and
  `gen_l2_outgoing_population.py` stands under `retired_invocation` as a HISTORICAL RECORD (cleared by
  `cc_instruction_l3_criterion_write_2026_10_14.md` Task 3, verified in entry 399 §1). (ii) The slice derivation's
  correction: `cowork_l2_task_b_slice_derivation_2026_09_05.md` reads *"L3's slice: 4 rows — 36, 37, 38, 39"* with the
  former wording *"L3's slice: 1 row — 36."* preserved (corrected 2026-10-14 by that dispatch's Task 4).
- **FACT — L2's pack directory**, `tools/audit/derivation_boot_pack/l2/`, at a listing: ten files, `00_READ_THIS_FIRST.md`
  (3,969 bytes), `01_the_phase_definitions.md` (18,850), `02_the_guiding_principles_and_the_conventions.md` (65,389),
  `03_the_writing_standards.md` (15,205), `04_the_dispatch_protocol.md` (109,056),
  `05_the_ratified_design_intent.md` (149,034), `06_the_defect_type_catalog.md` (5,968),
  `07_the_charter_the_layers_and_the_decisions.md` (33,311), `08_the_fifty_six_research_extracts.md` (842,350),
  `09_the_empirical_findings_ledger.md` (51,543), every modification time on 2026-09-27. **Sizes are not digests:
  yours are the digests.** `FROZEN` carries `harmony-boundary`, `scoring-model` and `l0-l1`, each with `finding`,
  `date`, `reason` and `digests`; it carries no `l2`.
- **FACT — L2's deriving session has run** (boot-list Ruling 1, noted: *"L2's pack not being in the generator's
  `FROZEN` table although its deriving session has run"*). The specification it produced,
  `cowork_derived_specification_l2_2026_10_10.md`, was ratified face by face on 2026-10-13 and 2026-10-14 (its banner,
  as the boot-list record relays). **The pack is STALE against today's sources:** the rendered charter member lacks the
  2026-10-14 amendment to L2's block of `FRAMEWORK.md` §5 (boot-list Ruling 1, searched for its heading and for
  "appoggiatura"). **So the digests are taken at the files on disk — what the session was given — and the pack is
  never re-rendered.**
- **FACT — `VERDICT_DATE`** carries `harmony-boundary` and `l2` and no `l3`. `VERDICTS["l3"]`'s group A heading says
  *"authored 2026-10-14"*, and the table's opening comment says each group block's authoring date stands in its own
  heading (the other seventeen headings were not read by the writing side; corrected at the check, former wording
  "`VERDICTS["l3"]`'s group blocks say *"authored 2026-10-14"* in their heading comments"); the three verdicts the user moved were written back on
  2026-10-15; the user ruled the family on 2026-10-15. Its opening comment says, under *THE DATE*, that the entry is
  *"OWED to the batch that builds L3's pack"*.
- **FACT — `criterion_block()`** (the generator) writes the fixed bullet for every subject whose criterion is not
  empty. `CRITERION["harmony-boundary"]["groups"]` is `("E",)`; `l2`'s is six groups; `l3`'s is twenty;
  `scoring-model` and `l0-l1` are empty and take the other branch. `group_title("E")` returns the register's own title,
  *"Layer 2 — the slicer"* (an em dash), which is **not** the bullet's *"Layer 2, the slicer"* (a comma) — so a gloss
  read through `group_title` would move the frozen `harmony-boundary` record, and Task 2 does not use it there.
- **FACT — `tools/audit/gen_l2_withheld_documents.py`** (11,961 bytes, read WHOLE): `SUBJECT = "l2"`,
  `RULED_IN_COUNT = 111`, `RULING_6` (the L2 ruling's text), `OUT` = `tools/audit/l2_withheld_documents.json`; it reads
  `pack.VERDICTS[SUBJECT]` by import and the homes from the backbone, takes the document before the first `:`, and has
  four STOPs. Its `main()` takes `--check` only. Its prose names L2 in `what_this_is`, the bound, and the two
  `--check` messages.
- **FACT — the ruled L3 family:** 22 IN, 222 OUT, 0 UNPLACED (entry 401 §1; verified at the table in entry 403 §1).
  Boot-list Ruling 5 states this side's *expectation* of the derived set — `ARCHITECTURE.md`,
  `cowork_joint_estimator_architecture.md`, `cowork_layer5_function_design.md`, `cowork_layer6_grouping_design.md`,
  `cowork_phrase_boundary_design.md` — **read at the register INDEX's home column, not at the data file; the tool's
  derivation is the object.** It is a prediction, not a condition.
- **FACT — the two input-contract sources**, staged by the writing side at the sizes the boot-list record gives:
  `cowork_derived_specification_l0_l1_2026_09_03.md` 142,523 bytes; `cowork_derived_specification_l2_2026_10_10.md`
  218,121 bytes. Each of the seven quoted passages was read at its lines by the writing side (L0/L1 file lines 103–105,
  108–110, 1128–1132, 1163–1164, 887–888; L2 file lines 288–290, 1944–1946). In every case the character before the
  passage's first word is a space on the same line. **The L2 precedent's cut copy** is
  `tools/audit/derivation_exemplars/l2/the_l0_l1_specification_the_input_contract.md`, written by
  `cc_instruction_l2_brief_landing_2026_09_27.md` Task 4(a); `tools/audit/derivation_exemplars/l3/` does not exist.

- **ASSUMPTION A1 — the working tree, by content.** Tracked modifications at boot, expected: **two**, both the
  writing side's corrected first extracts — `reading_pass/extracts/ju-margot-mckay-dahn-fujinaga-2020-automatic-figured-bass-annotation-bach-chorales-figured-bass-dataset.md`
  (23,494 bytes at its staging, entry 405 §1) and
  `reading_pass/extracts/sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md` (21,076 at the
  extracts folder's listing, entry 406 §1) — plus the line-ending-only marking of
  `tools/audit/claude_md_finer_archive.json` the last reports record (re-establish it; leave it untouched; never stage
  it). Each first extract's standing at the tip (tracked and modified, or untracked) is yours to take. Any other
  tracked modification at boot or during the run is a STOP-and-report, except a path this batch writes, after the task
  that writes it and until its commit. A further untracked `cowork_handoff_entry_*.md` or `cowork_rulings_*.md`
  appearing during the run is the writing side's, NOT landed and NOT a STOP. **Check (Task 0, first act):** per tracked
  input this batch edits (`tools/audit/gen_derivation_boot_pack.py`, `tools/audit/derivation_boot_pack.json`,
  `tools/audit/gen_l2_withheld_documents.py`, `tools/audit/gen_guard_state.py`, `STATUS.md`, `STATUS_ARCHIVE.md`,
  `tools/audit/gen_status_batch_bound.py`)
  `git diff --stat 5499f3e2521c2bf4478469f30f3b9fb18f0af655 -- <path>; echo "exit:$?"`; per path of Task 0's list
  `git ls-files --others --exclude-standard -- <path>; echo "exit:$?"`; the whole tracked population with
  `tools/audit/changed_paths.py`.
- **ASSUMPTION A2 — the guard run before the first edit:** the fourteen, plus **`gen_evidence_pin_membership.py
  --check` red** if the untracked ruling records are read by it (entry 402 §1 item (1): the last batch's start run had
  exactly this fifteenth red for one untracked ruling record; four are untracked now). The classification tool's
  standing STOP naming the three tools above. **Predicted at the end state: run 81** (Task 3 enrols one invocation),
  historical 20, not run 4; **failing the fourteen, or thirteen if `gen_derivation_boot_pack.py --check` goes green
  after Task 1** — the writing side did not establish what turns it red today and does not predict which (#18). Reds
  this batch's own acts may cause, classed by cause and NOT a STOP: `gen_evidence_pin_membership.py --check` (Task 0
  handles it); `gen_l2_withheld_documents.py --check` and `--subject l3 --check` between Task 3's edit and its commit;
  `gen_l0_l1_outgoing_population.py --check` and `gen_defense_share.py --check` if Task 5's `STATUS.md` entries move
  their inputs — regenerate, compare against the committed blob by explicit hash, commit with the end state, report
  that no member moved (a member moving IS a STOP-and-report); `gen_session_start_read_size.py --check` if
  regenerated before the last `STATUS.md` edit; `gen_guard_state.py`'s own artifact until the end-state run. A red
  outside these is a STOP-and-report.
- **ASSUMPTION A3 — byte-unchanged by this batch, verified at the objects after the last commit:** every governing
  document except `STATUS.md` and `STATUS_ARCHIVE.md`; **every file under `tools/audit/derivation_boot_pack/`** (all
  four directories); in the generator, everything except Task 1's inserted `FROZEN` entry and its comment, and Task 2's
  three edits; `tools/audit/l2_withheld_documents.json`; both source specifications; every ruling record and the
  cut-list document (landed only, as they stand); every extract (landed only); `FRAMEWORK.md`; every rendered
  decisions-register file; both reading files. Any other difference is a STOP-and-report.

## The standing bars, and the commit-and-push discipline

No `src/` edit, no golden, no test changed or run, no build, nothing under `tools/corpus/` or `tools/robust_stop/`,
**no measurement of the analysis built, designed, scoped or run**, no derivation of any specification statement,
**NO SESSION BOOTED, NO PACK DIRECTORY WRITTEN** (after Task 1 every built subject is frozen and `write_all` writes into
none of them — Task 1(e) proves it), **no `WITHHELD`, `EXTRAS` or `FROZEN` entry for `l3`, no edit to `CRITERION`,
to `MEMBERS`, to `CHARTER_MEMBER_7`, to `LEDGER_MEMBER_9`, or to any `VERDICTS` entry**, no open-items row created,
flipped or discarded, **no decisions-register entry and no `D-NNN` allocated, nothing written into the suspension
file**, no edit to any governing document except `STATUS.md`/`STATUS_ARCHIVE.md` in Task 5, **no edit to either source
specification, to the cut-list document, to any ruling record or to any extract** (each is landed as it stands), **no
score file copied, staged or written** (see "What this batch deliberately leaves"), **no ruling taken, and no question
or recommendation put to the user**.

**Commit-and-push per task. Run the FULL guard set BEFORE the first edit (`python tools/audit/gen_guard_state.py
--check`) and again at the end (write mode, committed as the artifact of a real run). After every commit: push, then
read `.git/refs/remotes/origin/master` with the file tools and confirm it names the commit just made.** Verify every
commit at the object by explicit hash. Every shell command carries `; echo "exit:$?"`. `git status` and `git diff` over
the working tree are denied by the armed guard — use the explicit-hash forms of A1. Write every hash literally in the
command: a hash held in a shell variable is denied by the guard. Plain single-quoted `git commit -m '…'` subjects, or
double quotes where the subject carries an apostrophe, declared. Every working-tree read through the file tools
(D-253); a run's output is redirected to a file in your session's scratch folder outside the repository and read with
the file tools; every script this dispatch orders is written there too and its text goes into the report. Edit files
with your file-editing tool, never by retyping a whole file. **If an old text quoted below does not occur EXACTLY once
in its file, that edit is a STOP-and-report for that edit alone**: make nothing for it and report what you found. The
reserved-word rule binds every line you write: *score*, *key*, *note*, *figure*, *register*, *measure*, *part*,
*scale*, *tie* only in their musical senses, or qualified.

## The ordered first reads

**(1)** The four 2026-10-15 ruling records named in "What this batch is" WHOLE, and
`ratification_surfaces/cowork_l3_input_contract_cut_lists_2026_10_15.md` WHOLE. **(2)** `CLAUDE.md` at its six ruled
spans (the membership at its "Build and test commands" block), `STATUS.md` whole, `DECISIONS.md` whole; rule (a)'s
`gating_ids` at `tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`. **(3)**
`records/cowork/handoff/cowork_handoff_entry_four_hundred_and_eight.md` and, if present,
`…four_hundred_and_nine.md`, whole. **(4)** `cowork_audit_protocol.md`'s dispatch-protocol section. **(5)** The last
batch: its dispatch `records/cc/instructions/cc_instruction_l3_ruling_writeback_2026_10_15.md` whole, its report
`records/cc/reports/cc_report_l3_ruling_writeback_2026_10_15.md` whole, its close (the last section of
`records/cowork/handoff/cowork_away_returns.md`). **(6)** The models:
`records/cc/instructions/cc_instruction_boot_pack_freeze_l0l1_2026_09_04.md` at Task 1;
`records/cc/instructions/cc_instruction_l2_withheld_documents_2026_09_21.md` at Tasks 1 and 2;
`records/cc/instructions/cc_instruction_l2_brief_landing_2026_09_27.md` at Task 4;
`records/cc/instructions/cc_instruction_l3_reading_file_2026_10_15.md` at the step that enrols
`gen_withheld_family_reading.py --subject l3 --check`. **(7)** The generator at: its docstring, `VERDICT_DATE`,
`FROZEN` whole, `CRITERION`, `criterion_is_empty`, `criterion_block`, `group_title`, `write_all`, `check_all`,
`frozen_from_disk`, `main`, and the opening comment of `VERDICTS["l3"]`. **(8)** `tools/audit/gen_l2_withheld_documents.py`
WHOLE and `tools/audit/l2_withheld_documents.json` WHOLE. **(9)** `tools/audit/gen_guard_state.py` at its authored
invocation list. **(10)** `tools/audit/gen_status_batch_bound.py` whole at the object
`5499f3e2521c2bf4478469f30f3b9fb18f0af655:tools/audit/gen_status_batch_bound.py` before Task 5.

## Task 0 — land the records, and PUSH

To be landed (the standing clause), each as it stands:

1. `records/cc/instructions/cc_instruction_l3_pack_build_first_half_2026_10_15.md` (this dispatch);
2. `records/cowork/handoff/cowork_handoff_entry_four_hundred_and_two.md` through
   `…four_hundred_and_eight.md` (seven files), and `…four_hundred_and_nine.md` if present;
3. `records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md`,
   `…_l3_first_pass_extracts_sitting.md`, `…_l3_staged_score_set_sitting.md`, `…_l3_cut_lists_sitting.md`;
4. `ratification_surfaces/cowork_l3_input_contract_cut_lists_2026_10_15.md`;
5. `reading_pass/extracts_second_pass/ju-margot-mckay-dahn-fujinaga-2020-automatic-figured-bass-annotation-bach-chorales-figured-bass-dataset.md`
   and `reading_pass/extracts_second_pass/sears-pearce-caplin-mcadams-2018-simulating-expectations-for-tonal-cadences.md`
   (row 36's and row 39's second extractions);
6. the two corrected first extracts of A1, in `reading_pass/extracts/` under the same two file names.

**The acts, in order:** **(1)** A1's check. A path already tracked and unmodified is reported and not re-landed;
entry 409 absent is reported, not a STOP; this dispatch or any of items 3 to 5 absent is a STOP. Report any other
untracked path the enumeration shows under `records/`, `reading_pass/` or `ratification_surfaces/` — NOT landed, not a
STOP. **(2)** If `tools/audit/gen_evidence_pin_membership.py --check` is red, regenerate
`tools/audit/evidence_pin_membership.json` and measure it against the committed blob: the only permitted change is its
list of ruling records read, gaining the four of item 3; any other movement is a STOP-and-report. **(3)** Commit the
paths that exist and are untracked or modified, plus the membership artifact only if it moved. Subject, exactly:
`record: the L3 pack-build first-half dispatch, entries 402-409, the four 2026-10-15 L3 ruling records, the cut-list document and rows 36 and 39 extracts landed`
(if entry 409 is absent, write `entries 402-408`). **(4)** PUSH; verify `origin/master` at the ref file.

**Under standing clause P-2 this dispatch is PINNED at Task 0:** record its blob, and prove it unmoved immediately
before staging it.

**E0:** the named paths in one commit; `origin/master` at the commit; every path accounted for.

## Task 1 — freeze L2's spent pack, in ONE commit

It cannot be stopped partway, so it goes first with nothing large in front (D-670). **The `FROZEN` entry is written
FIRST, before the tool is run in any write mode** — while `l2` is live, a write run re-renders its directory from
today's sources, which would overwrite the record this task exists to preserve (the l0-l1 freeze's own ground).

**(a) PROVE THE DIRECTORY IS WHAT WAS COMMITTED.** For each of the ten files of `tools/audit/derivation_boot_pack/l2/`,
take `git hash-object <file>` and `git rev-parse 5499f3e2521c2bf4478469f30f3b9fb18f0af655:<path>` and prove they are
equal. **A file on disk that differs from its committed blob, a file present on disk and not in the commit, or the
reverse, is a STOP-and-report and nothing is written.**

**(b) MEASURE THE TEN DIGESTS.** For each of the ten files take `git hash-object <file>` **and**
`git hash-object --no-filters <file>`, and prove the two agree for every one. **A disagreement is a STOP-and-report.**

**(c) ADD THE FOURTH `FROZEN` ENTRY.** The anchor is the last two lines of the table, matched verbatim:

```
    # made false by that session's run.
}
```

**Insert the new entry between those two lines** — the comment line unchanged and the `}` unchanged. Its four fields:
`digests`, the ten values of (b) keyed by file name in the order of the listing above, in the shape the `l0-l1` entry
uses; and three authored fields **quoted verbatim from this dispatch and composed by you not at all**:

- `finding`: *"Its deriving session has RUN (Ruling 1 of
  `records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md`, noted), and the specification it
  produced, `cowork_derived_specification_l2_2026_10_10.md`, was ratified face by face on 2026-10-13 and 2026-10-14.
  The pack is STALE against today's sources — its rendered charter member lacks the 2026-10-14 amendment to L2's block
  of `FRAMEWORK.md` §5 — so the digests recorded here are those of the files on disk, proved equal to their committed
  blobs: what the session was given, and not a re-render."*
- `date`: *"2026-10-15"*
- `reason`: *"A spent subject's pack is the record of what its session was given rather than an input to be kept
  current (Ruling 17(a); D-646). Left live it would re-render the charter member with an amendment ruled after the
  session ran, and so back-date into a completed derivation's record a text its session never read (#12); and L3's
  pack shares the charter member with it (`CHARTER_MEMBER_7`), so it must be frozen before L3's is built (the boot-list
  record's Ruling 1, noted). Frozen at the blobs it carries, with the hash STOP."*

followed, inside the table and after the entry, by this comment, verbatim:

```
    # `l2` IS FROZEN ABOVE, ITS DERIVING SESSION HAVING RUN; its own ground is in its own entry and is
    # not restated here (#6).  Frozen 2026-10-15 by the first half of L3's pack build.
```

**No other line of the file is touched in this task.**

**(d) REGENERATE THE MANIFEST**, naming the mode you run the tool in, then run `--check` and report its whole output
and exit code. **Prove at the object that no file of any of the four pack directories moved** — every file compared
against the tip's blob by explicit hash — and report the manifest's diff against the tip's blob in full. **Expected:**
the diff is confined to `l2`'s record (the frozen-subject shape `frozen_from_disk` writes) and to any field the
docstring says the manifest derives from the frozen set; **a moved record of `harmony-boundary`, `scoring-model` or
`l0-l1` is a STOP-and-report and nothing is committed.** Whether `--check` exits 0 is reported, not predicted (A2).

**(e) PROVE THE WRITE PATH IS SHUT.** Read `write_all` and report, in one sentence quoted from its code, why it writes
nothing into a frozen subject's directory; and state which subjects `build()` builds today (expected: the four of
`WITHHELD`, none of them `l3`).

**Commit exactly these two paths:** `tools/audit/gen_derivation_boot_pack.py` and `tools/audit/derivation_boot_pack.json`.
Subject, exactly: `freeze the l2 boot pack at its rendered blobs, its deriving session having run`. Push; verify.

**E1:** the ten files proved equal to their committed blobs; the ten digests taken twice and agreeing; the entry and
its comment in one commit with the regenerated manifest; every pack directory proved byte-unchanged; the deleted-line
enumeration for the generator published (expected: none).

## Task 2 — `VERDICT_DATE["l3"]` and the criterion bullet, in ONE commit

**(a)** Run, and keep: `cd C:\s\MS && python tools/audit/gen_derivation_boot_pack.py --check > <scratch>\dbp_t2_before.txt 2>&1; echo "exit:$?"`.

**(b) Edit 1 — the date.** Old text (once):

```python
VERDICT_DATE: dict[str, str] = {
    "harmony-boundary": DATE,
    "l2": "2026-09-05",
}
```

New text:

```python
VERDICT_DATE: dict[str, str] = {
    "harmony-boundary": DATE,
    "l2": "2026-09-05",
    # `l3`'s verdicts were authored on 2026-10-14 (each group block's own heading carries its authoring
    # date) and RULED on 2026-10-15 (`cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`,
    # three rulings; three verdicts written back that day).  The date stamped is the ruling's: a verdict
    # becomes a withholding only when the user has ruled it (Ruling 2 of
    # `cowork_rulings_2026_10_14_l3_withheld_family_sitting.md`).  For `l2` the two dates coincide.
    "l3": "2026-10-15",
}
```

**(c) Edit 2 — the stale sentence under *THE DATE* in `VERDICTS["l3"]`'s opening comment.** Old text (once):

```python
    # THE DATE.  Ruling 2 requires each verdict to carry its date.  `VERDICT_DATE` carries no `l3`
    # entry yet and `build_subject` STOPs without one; it is OWED to the batch that builds L3's pack.
    # Meanwhile each group block's authoring date stands in its own heading comment.
```

New text:

```python
    # THE DATE.  Ruling 2 requires each verdict to carry its date.  `VERDICT_DATE["l3"]` carries it —
    # the ruling's date, with the ground stated there; each group block's authoring date still stands
    # in its own heading comment.  ★ CORRECTED 2026-10-15 by the first half of L3's pack build; FORMER
    # WORDING, PRESERVED (#12): "`VERDICT_DATE` carries no `l3` entry yet and `build_subject` STOPs
    # without one; it is OWED to the batch that builds L3's pack.  Meanwhile each group block's
    # authoring date stands in its own heading comment."
```

**(d) Edit 3 — the criterion bullet.** In `criterion_block()`, old text (once):

```python
    return (
        "The candidate criterion is a PATTERN MATCH over the rulings sort and the decisions "
```

New text:

```python
    # ★ THE GROUP BULLET IS DERIVED FROM THE AUTHORED `groups` TERM (2026-10-15, the first half of L3's
    # pack build; owed since entry 398 §2).  FORMER WORDING, PRESERVED (#12): the bullet was the fixed
    # string "its `group` is E — Layer 2, the slicer" for every subject — true of `harmony-boundary`,
    # whose criterion names group E alone, and false of `l2` (six groups) and `l3` (twenty).  A
    # criterion naming exactly group E keeps that exact string, so the frozen `harmony-boundary`
    # record does not move; `group_title("E")` is NOT used for it, its punctuation differing.
    if tuple(spec["groups"]) == ("E",):
        group_bullet = "its `group` is E — Layer 2, the slicer"
    else:
        group_bullet = ("its `group` is one of the register groups listed under `the_groups` "
                        "below")
    return (
        "The candidate criterion is a PATTERN MATCH over the rulings sort and the decisions "
```

and old text (once):

```python
                "its `group` is E — Layer 2, the slicer",
                "its `home` document is one of the withheld-document candidates",
```

New text:

```python
                group_bullet,
                "its `home` document is one of the withheld-document candidates",
```

**(e)** Regenerate the manifest (name the mode), then run `--check` to
`<scratch>\dbp_t2_after.txt`; report both outputs in full and the manifest's diff against Task 1's commit by explicit
hash. **Expected:** `harmony-boundary`'s, `scoring-model`'s and `l0-l1`'s records byte-unchanged; `l2`'s record changes
in at most the one bullet line, if its frozen record carries the criterion block at all (report which); no pack-directory
file moves. **Anything else is a STOP-and-report and nothing is committed.** (`VERDICT_DATE["l3"]` is read by
`build_subject("l3", …)` only, which no run reaches yet; its inertness is shown by the manifest diff.)

**Commit exactly** `tools/audit/gen_derivation_boot_pack.py` and `tools/audit/derivation_boot_pack.json` (the latter
only if it moved). Subject, exactly:
`l3 verdict date and the criterion group bullet derived from the authored groups`. Push; verify.

**E2:** the three edits as written; the manifest diff as expected; the deleted-line enumeration published, every
deleted line inside the three quoted old texts.

## Task 3 — L3's withheld documents: DERIVED AND PRINTED, authored into nothing; ONE commit

Boot-list Ruling 5, verbatim: *"the pack-build dispatch derives, from the register's data file
(`tools/audit/decisions/backbone_decisions.json`) and the ruled `VERDICTS["l3"]`, the set of home documents of the 22
IN entries; prints it; and **STOPs for the user's confirmation before the set is authored into
`WITHHELD["l3"]["withheld_documents"]`**, each document with its finding, date and reason."*

**The route, and why it is not a new tool:** the derivation is the one L2's tool already performs for `l2`, so the
capability is added as a PARAMETER on that tool and not as a sibling (#6; D-623). **L2's artifact and L2's printed
output must stay byte-identical**, which is the proof that this is an addition.

**(a)** Before any edit run and keep: `python tools/audit/gen_l2_withheld_documents.py --check > <scratch>\wd_l2_before.txt 2>&1; echo "exit:$?"`
(expected: exit 0, *"the L2 withheld-document derivation re-derives"*).

**(b)** Edit `tools/audit/gen_l2_withheld_documents.py`:

1. Replace the four module constants `SUBJECT`, `RULED_IN_COUNT`, `RULING_6` and `OUT` by ONE table `SUBJECTS`, keyed
   `"l2"` and `"l3"`. **`"l2"` carries the four values exactly as they stand today, and every L2 sentence the tool
   writes or prints** (`what_this_is`, `the_ruling_it_executes`, the verdict-table and bound sentences, both `--check`
   messages, the run's closing line) **moved into it unchanged**, so that the `l2` artifact and output are produced
   from the same characters as before. `"l3"` carries: the subject `l3`; the ruled count **22**; the ruling cited as
   *"Ruling 5 of `records/cowork/rulings/cowork_rulings_2026_10_15_l3_boot_list_sitting.md`"* with Ruling 5's text
   quoted above as its verbatim; `OUT` = `tools/audit/l3_withheld_documents.json`; and each sentence with "L2" read as
   "L3", "Ruling 6" as "Ruling 5" and the L2 record's path as the L3 record's. STOP 4's message cites, for `l3`, *"Ruling
   5 names \"the 22 IN entries\", and the user's three rulings of 2026-10-15
   (`cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md`) leave the ruled family at 22 IN, 222 OUT, 0
   UNPLACED"*. *(Corrected at the check. Former wording: "and Ruling 3 of `…lists_sitting.md` records the ruled family
   as 22 IN, 222 OUT, 0 UNPLACED" — the writing side did not read that record, and the totals are relayed from entry
   401 §1 and the write-back dispatch, not read at a ruling.)*
2. `main()` gains `--subject` taking `l2` or `l3`, **default `l2`**, so the existing guard invocation (`--check` with no
   subject) is unchanged. Any other value is a STOP.
3. The docstring gains, after its first paragraph, one paragraph stating that the tool derives for the subject named
   by `--subject`, L3's under Ruling 5 of the 2026-10-15 boot-list record, added 2026-10-15 as a parameter rather than
   a sibling (#6, D-623); **no other docstring line changes**.

**(c)** Prove L2 unchanged: rerun (a)'s command to `<scratch>\wd_l2_after.txt`; prove the two outputs byte-identical
and `tools/audit/l2_withheld_documents.json` byte-identical to its committed blob. **A difference is a STOP-and-report;
restore the tool by explicit hash and end Task 3.**

**(d) Derive L3's set:** `python tools/audit/gen_l2_withheld_documents.py --subject l3 > <scratch>\wd_l3.txt 2>&1; echo "exit:$?"`,
then `--subject l3 --check` (expected exit 0). **Any STOP of the tool is reported whole and ends Task 3 with nothing
committed** — above all STOP 4 (a count other than 22) and STOP 2 (a home that is not a document path).
**Print in the report the derived set exactly as the run printed it**, then, for each document, the IN identities homed
there as the artifact lists them. **Compare it with Ruling 5's stated expectation** (the five documents in the premise
ledger) and report the agreement or each difference — **a difference is a finding for the user, not a STOP.**

**(e) Enrol** `gen_l2_withheld_documents.py --subject l3 --check` in the guard set's authored invocation list in
`tools/audit/gen_guard_state.py`, in the same shape and by the same convention as the existing
`gen_withheld_family_reading.py --subject l3 --check` entry (ordered first read (6)), with a `what_it_checks` text
stating: *"the L3 withheld-document derivation re-derives: the home documents of the entries the ruled L3 verdict
table grades IN, under Ruling 5 of the 2026-10-15 L3 boot-list record, printed for the user's confirmation and
authored into nothing; it STOPs on a count other than 22, an IN identity the backbone lacks, a home that is not a
document path, or a reconciliation failing in either direction"*. Run the full guard set to a scratch file and
report run count and the failing set (expected run 81).

**Commit exactly:** `tools/audit/gen_l2_withheld_documents.py`, `tools/audit/l3_withheld_documents.json`,
`tools/audit/gen_guard_state.py`. Subject, exactly:
`derive and print the L3 withheld documents (Ruling 5), authored into nothing; the derivation tool gains --subject`.
Push; verify.

**E3:** L2's output and artifact byte-identical; L3's set derived, printed and committed as an artifact; the
enrolment in place; `WITHHELD` untouched.

## Task 4 — the two cut input-contract copies, and a search over them that cuts nothing; ONE commit

**(a) Write the copies** with ONE Python script **outside the repository working tree** (not committed; its text goes
into the report). For each of the two jobs below, the script does exactly this:

1. Read the SOURCE from the repository root **as bytes**, decode as UTF-8; record its size and `git hash-object`.
   **Expected sizes: 142,523 and 218,121 bytes.** A different size is reported, not a STOP; the passages are located by
   text.
2. Take its line ending: `"\r\n"` if the text contains `"\r\n"`, otherwise `"\n"`. Call it `EOL`.
3. For each QUOTE of the job (below; copy each byte for byte from this dispatch into the script), build the pattern
   `r"\s+".join(re.escape(w) for w in QUOTE.split())` — so a line break and its indentation inside the passage match
   the single space the cut list wrote for it. **The pattern must match EXACTLY ONCE in the source. If not, STOP:
   write nothing, and report the count for that quote.**
4. The span removed for a quote is its match **plus the run of space characters (U+0020) immediately before it on the
   same line** — never a line break before it. **Every removed span must be disjoint from the others, or STOP.**
5. Build the result as the source with the spans removed, nothing else changed. **Establish and print:** (i) every
   quote's pattern matches the result zero times; (ii) re-inserting each removed span at its offset reproduces the
   source byte for byte; (iii) for each cut, the 80 characters of the result immediately before the place the cut
   was and the 80 immediately after it, verbatim, beside the expected ends given below (`EOL` printed as `⏎`). **A
   cut whose two ends differ from the expected ends is reported and is a STOP for that job.**
6. Prepend the HEAD given for the job, its lines joined by `EOL`, followed by one blank line (`EOL` twice).
7. Write the result as UTF-8 bytes to the job's TARGET (create `tools/audit/derivation_exemplars/l3/` if absent).
   **Establish, and print:** that the written file with the HEAD and its blank line removed from the front equals step
   5's result byte for byte; its size; its `git hash-object`.

**Job 1.** SOURCE `cowork_derived_specification_l0_l1_2026_09_03.md`. TARGET
`tools/audit/derivation_exemplars/l3/the_l0_l1_specification_the_input_contract.md`. HEAD:

```
> **THE INPUT CONTRACT — the ratified specification of L0 and L1, cut for the L3 deriving session.**
> Its source is `cowork_derived_specification_l0_l1_2026_09_03.md`; this file is a cut copy of that source and not a
> second version of it. Below this block the source stands verbatim, except that passages stating the L3 layer's own
> ruled or current design have been removed where they stood, with no mark. Do not try to reconstruct them, and do
> not treat a gap as a hint.
```

QUOTES (Cuts 1 to 5 of the cut-list document §2), one per line:

```
the grouping layer's unit is the punctuation span, bounded by notated punctuation, as Row 13.1's own convention says;
the grouping object is the punctuation span; the phrase-boundary primitive's code name is an inherited collision for OI-229, that primitive being L3's under Ruling 48.
The graded profile, its gap-dominant weights, the marker spikes, the max-normalisation, the adaptive threshold, the peak-picking, the picked set and the *"ends a phrase"* flag are **RELOCATED to the consumer that decides the phrase boundary** — the phrase read-off at L3 under the L1 → L3 contract — *"with D-476 to D-485 re-homed there and D4 (D-478) remaining that consumer's ruled rule"*.
— and relating them is L2's cadence-factor covariate and L3's alignment window, to which Rows 11.12 and 13.14 are relocated.
the harmonic rhythm is over decided harmonic spans, the charter's L3.
```

EXPECTED ENDS after the cuts — what the result's text immediately BEFORE the place of each cut ends with, and what
the text immediately AFTER it begins with (the writing side's reading of the source at the lines the cut-list
document names; `⏎` is `EOL`):

- Cut 1: before ends `bounded by harmony change;` — after begins ` any further span is named by what bounds it`.
- Cut 2: before ends `evidence and not phrases;` — after begins `"* *(The ruling's own sentence uses* bar`.
- Cut 3: before ends `is a published fact."*` — after begins `⏎- *Beside S-39 (Ruling 48, §3bc) — what an absent flag`.
- Cut 4: before ends `every change point (Ruling 47)"*` — after begins `⏎`. **The sentence loses its full stop**: the
  ruled quote includes it, and this job removes exactly the quote.
- Cut 5: before ends `the series is the slice list, already published;` — after begins `"*⏎`.

**Job 2.** SOURCE `cowork_derived_specification_l2_2026_10_10.md`. TARGET
`tools/audit/derivation_exemplars/l3/the_l2_specification_the_input_contract.md`. HEAD:

```
> **THE INPUT CONTRACT — the ratified specification of L2, cut for the L3 deriving session.**
> Its source is `cowork_derived_specification_l2_2026_10_10.md`; this file is a cut copy of that source and not a
> second version of it. Below this block the source stands verbatim, except that passages stating the L3 layer's own
> ruled or current design have been removed where they stood, with no mark. Do not try to reconstruct them, and do
> not treat a gap as a hint.
```

QUOTES (Cuts 6 and 7):

```
D-526's "jazz-specific classes enter only under the OI-7 jazz-ground-truth gate" is read as gating the increment's measurement rather than its landing (the surface's reading, put with the position and not separately ruled).
**False-negative path:** L3's cadence-type reading wanting "how strongly V→I was scored here". It reads the masses of the readings with and without the cadence, which are published, rather than a term value.
```

EXPECTED ENDS:

- Cut 6: before ends `before jazz ground truth⏎  exists;` — after begins ` **L2-S4 stands as derived.**"`.
- Cut 7: before ends `- *Premise.* L3 needs nothing intermediate.` — after begins `⏎- *Falsifier.* CODE.`

*(Why the residues are left as they fall: the ruling cuts exactly the quoted passages; the residues — a semicolon
before a closing quotation in Cuts 2 and 5, the missing full stop in Cut 4 — are what verbatim removal leaves, and no
character outside a quote is touched. The writing side records this here so the user meets it at the check.)*

**(b) THE SEARCH OVER THE TWO COPIES. Its hits are REPORTED, and NOTHING more is cut in this batch.** A second script
outside the working tree reads the two copies, `VERDICTS["l3"]` by import of the generator (its IN entries, with that
module's `VERDICT_IN` token; nothing calls `build()` or `main()`), and `tools/audit/l3_withheld_documents.json`, and
prints, for every line of each copy (numbered from 1 in the copy), every hit of: **(1)** each of the 22 IN identities,
matched as `re.escape(id) + r"(?!\d)"`; **(2)** each document of the derived set, as a plain substring; **(3)** the
string `ARCHITECTURE.md`, and every match of the generator's own `PATH_LIKE`. Print each hit as: copy, line number,
which of 1 to 3 matched, what matched, and the line verbatim; then the count per kind per copy. **Predicted: no hit of
kind (1), and no hit of kind (2) for the five documents Ruling 5 expects** — the cut list's name search over the 22
names and those five documents found only the passages of Cuts 3 and 6 (cut-list document §1). A derived document
outside those five was never searched for, and no prediction is made for it. A hit is not a STOP: it goes to the user
through the writing side. *(Corrected at the check. Former wording: "Predicted: no hit of kind (1) or (2)" — wider
than the search it rested on, which reached the five expected documents and not the derived set.)*

**(c)** Confirm in the report that both sources are byte-identical to their (a)1 hashes after both scripts have run.

**Commit exactly the two copies.** Subject, exactly:
`l3 input contract: the l0-l1 and l2 specifications cut of the seven ruled passages, each pointing back to its source`.
Push; verify.

**E4:** both copies written, every quote found once and removed, both reconstructions byte-exact, every expected line
confirmed; the search reported whole; both sources unchanged.

## Task 5 — the close, ending on the STOP

1. **The `STATUS.md` entries and the forward-bound move, IN THIS ORDER** (read `gen_status_batch_bound.py` whole at the
   object first, ordered first read (10)). **(a)** Write this batch's entries at the top of `STATUS.md`: one pointer
   entry per task that did work — the close entry FIRST, NAMING THIS DISPATCH BY ITS FILE NAME
   (`records/cc/instructions/cc_instruction_l3_pack_build_first_half_2026_10_15.md`), each earlier task's entry below
   it saying `Same dispatch`; no figure restated (D-431); the close entry says that L2's pack is frozen, that L3's
   withheld documents are DERIVED AND PRINTED AND AUTHORED INTO NOTHING, awaiting the user's confirmation under Ruling 5,
   that the two input-contract copies are written, and that nothing is withheld, no pack rendered, no session booted,
   no `D-NNN` allocated and no open-items row touched. **The `Last updated: ` prefix moves from the last batch's close
   entry (the topmost at the tip, naming `cc_instruction_l3_ruling_writeback_2026_10_15.md`) to your newest entry.**
   **(b)** Re-aim the five authored constants of `gen_status_batch_bound.py`: `BASE_COMMIT` (this batch's last task
   commit before the close), `PREVIOUS_BATCH_DISPATCH` (`cc_instruction_l3_ruling_writeback_2026_10_15.md`), `ACT_DATE`
   (the day the move runs), `DISPATCH` (`cc_instruction_l3_pack_build_first_half_2026_10_15.md`), `TASK` (`Task 5`);
   append your own aiming to `PREVIOUS_AIMINGS` on the convention its comments state. **(c)** Run
   `gen_status_batch_bound.py --apply`. **Prediction:** it moves **exactly the last batch's four entries** (its close
   entry and the three `Same dispatch` entries for its Tasks 2, 1 and 0, read at `STATUS.md` at the tip); the two
   2026-09-02 entries stay. If it STOPs, restore its passing aim, re-run green, report, move nothing by hand. **(d)
   LAST**, after the final `STATUS.md` edit, regenerate `gen_session_start_read_size.py` and confirm its `--check`
   green. Commit the re-aimed tool, `tools/audit/status_batch_bound.json`, `STATUS.md`, `STATUS_ARCHIVE.md` and the
   read-size artifact together in the close.
2. **The report**, `records/cc/reports/cc_report_l3_pack_build_first_half_2026_10_15.md`, which decides nothing and
   recommends nothing: both guard states; every commit hash; E0 to E4 and A1 to A3 graded; Task 1's ten digests with
   the two-form agreement and the disk-equals-commit proof per file; Task 2's manifest diffs; **Task 3's derived set,
   printed whole, first in the report under the heading `THE DERIVED DOCUMENT SET — FOR THE USER'S CONFIRMATION UNDER
   RULING 5`**, with its comparison to the stated expectation; Task 4's two scripts, every expected-line confirmation
   and the search's hits whole; declared departures; and the plan's tell in one sentence — did this batch produce
   anything other than the landed paths, the freeze, the three generator edits, the derivation tool's parameter and
   artifact, the enrolment, the two copies, the Task 5 files and the report? If yes, name it.
3. **The full close appended to `records/cowork/handoff/cowork_away_returns.md`** as a section headed **THE L3 PACK
   BUILD, FIRST HALF: L2 FROZEN, L3's WITHHELD DOCUMENTS DERIVED AND PRINTED — STOPPED FOR THE USER'S CONFIRMATION;
   THE INPUT-CONTRACT COPIES CUT; NOTHING WITHHELD, NO PACK, NO ALGORITHM CHANGED** (if a task stopped, the heading
   says so) — the report's content as pointers, and the plan line: **the next act is the writing side's — the check of
   this batch's return at the objects, then the derived document set put to the user for confirmation, then the
   second half of the pack build.**
4. **The close does not assert the end state**; one further commit carries it. Commit the close, push, verify; then the
   full guard run in write mode at that tree, the A2 exceptions handled as A2 says, and the one further commit with its
   artifacts, pushed and verified. Re-run `gen_guard_classification.py --check` after it and report the message
   (expected: the standing STOP naming the same three tools; a change in that message is reported, not a STOP).

**E5:** at the tree carrying the close, a fresh full guard run — the A2 prediction — committed only after the run
that produced it.

**THIS BATCH ENDS HERE.** The derived set is printed and not authored. Ruling 5 reserves the authoring for after the
user's confirmation; nothing in this batch moves towards it.

## What this batch does NOT do

- **No withheld family authored, no extras, no pack rendered, no session booted.** `WITHHELD["l3"]` and `EXTRAS["l3"]`
  do not exist after it.
- **No change to what any layer computes** as its specification defines it.
- **No decisions-register entry, no `D-NNN`, nothing in the suspension file, no ruling taken.**

## What this batch deliberately leaves to later acts, named so it is not lost

- **The second half of L3's pack build**, written by the writing side after the user confirms the derived document
  set: `WITHHELD["l3"]` authored (the 22 IN identities from `VERDICTS["l3"]`, the confirmed documents, no withheld
  passage of `CLAUDE.md` — boot-list Ruling 4), each with finding, date and reason; `EXTRAS["l3"]` — the charter member
  `CHARTER_MEMBER_7` (Ruling 1), the research-extracts member (Ruling 3: the first extractions of rows 36, 37, 38, 39,
  with 34 and 40 carried, and the eleven first-pass extracts of the 2026-10-15 first-pass record, each with its
  project-facing passages cut per file and the record's §2.3 bookkeeping removed, each named exactly and verified at
  the file), and the ledger member; the render; and the extras' leak scan (limb B) listed to the user before any boot.
- **How the input-contract copies and the three staged scores reach the session** — as pack members or as attachments
  named in the brief. The L2 precedent attached its scores by name at boot (`cowork_rulings_2026_09_27_l2_brief_sitting.md`
  §2: the seven-folder limit binds the writing side's bridge and not the deriving session), and kept its input
  contract under `tools/audit/derivation_exemplars/l2/`. No score file is copied by this batch.
- **The brief**, and the blind deriving session in a fresh Cowork session.
- **`reading_pass/candidacy_upgrades.md`'s reading-progress record** — rows 36 and 39 each carry a landed,
  cross-checked second extraction (entries 405–406); one update after the run (entry 169 §3).
- **The six drifted register anchors and the eight stale derived `home_section` blocks** — register maintenance;
  cause first (D-669). **The three cosmetic slips of the generated reading files** (entry 403 §2) — with the next edit
  of that tool.

## The writing side's self-check, run before this dispatch was released (D-434)

1. *Principles.* #6 — the derivation is a parameter on the one tool that already performs it, and the cut copies
   name their sources; #12 — every replaced comment keeps its former wording, L2's derivation and every frozen record
   are proved unmoved, L2's pack frozen at the bytes its session read; #13/#18 — every inertness claim proven by a
   before/after comparison (Task 2(e), Task 3(c)), and the one thing not established (what turns the generator's
   `--check` red) is not predicted; #17f/D-431 — every count is the tool's or the ruling's, read back at the artifact;
   #19 — the new derivation is guarded on its first commit.
2. *Conventions.* American English; the vocabulary block precedes first use; *decisions-register* qualified; *check*,
   *script*, *generator*, never *instrument*.
3. *The bars.* Nothing withheld; no `WITHHELD`, `EXTRAS` or `FROZEN` entry for `l3`; no pack written; no register
   entry; every record landed as it stands; no question to the user.
4. *Documentation and algorithm.* Nothing here changes the algorithm as any specification defines it.

*Provenance: Cowork writing side, 2026-10-15 (Stockholm), the sitting booted on entry 408, at tip
`5499f3e2521c2bf4478469f30f3b9fb18f0af655` read as files; no shell command was run. **Read by the writing side, at
the extent named:** the boot read of entry 291 §4 step 3 (`CLAUDE.md` at its six ruled spans; `DECISIONS.md`,
`STATUS.md` whole; the gating answer; entry 118's bridge-fault section; entry 152's (v) to (x); entry 169 whole);
entries 291, 393, 394 and 398 to 408 whole, entries 395 to 397 by search only; the four 2026-10-15 ruling records
named in "What this batch is" whole (`cowork_rulings_2026_10_15_l3_withheld_family_lists_sitting.md` NOT read — every
statement about it here is relayed from entry 401 §1 and the write-back dispatch); the cut-list document
whole; the 2026-09-27 L2 brief and cut-list records whole; the L3 write-back dispatch at its head, Task 0, Task 3 and
its tail; the l0-l1 freeze dispatch at Task 1; the L2 withheld-documents dispatch by its headings and search; the L2
brief-landing dispatch at Task 4; `gen_l2_withheld_documents.py` WHOLE; the generator at its docstring, `VERDICT_DATE`,
`MEMBERS`, `FROZEN`, `CHARTER_MEMBER_7`, `LEDGER_MEMBER_9`, `EXTRAS` to the head of its `l2` list, `CRITERION`,
`criterion_is_empty`, `criterion_block`, `group_title`, and the head of `VERDICTS["l3"]`; `guard_state.json` at
`summary`, the retired list and the two entries named; both source specifications at the seven passages' lines; the
slice derivation by search; listings of `tools/audit/derivation_boot_pack/`, `tools/audit/derivation_exemplars/`,
`reading_pass/extracts_second_pass/`, the handoff and rulings folders and `records/cc/instructions/`. **NOT read:**
`write_all`, `check_all`, `frozen_from_disk`, `build()` and `main()` of the generator; `gen_guard_state.py`;
`gen_status_batch_bound.py`; the reading-file dispatch's enrolment step; the two first extracts.*

## The writing side's check of this dispatch at its sources (recorded per the standing clause and D-434; run 2026-10-15 in a turn of its own, after the user's "continue")

Scope: completeness, coherence, correctness and absolutes, against the objects the provenance names. **Confirmed at
the objects:** `WITHHELD` carries `harmony-boundary`, `scoring-model`, `l0-l1` and `l2` and no `l3` (its four keys
found by search), so `build()` builds four subjects and, after Task 1, every one of them is frozen; `FROZEN` carries
three entries; each of the seven passages' distinctive line occurs once in its file, at the line the cut-list document
names (one search hit each); Cut 2's text after the quote begins `"* *(The ruling's own sentence uses* bar` (line 110,
read); the four untracked ruling records and the two second extracts exist at the listings by the names given.

**Corrected at their sites, former wordings kept:** (1) Task 3's STOP-4 message cited "Ruling 3" of the 2026-10-15
lists record for the 22 / 222 / 0 totals — that record was not read by this side, so the citation now names the
record and its three rulings, and the provenance says it was not read; (2) Task 4(b)'s prediction of no hit of kind
(2) was wider than the search it rested on, which reached the five expected documents and not the derived set; (3)
the premise ledger said every `l3` group block's heading carries "authored 2026-10-14" where only group A's was read;
the matching comment in Task 2 Edit 1 is reworded to what the table's own opening comment says; (4) the provenance
said entries 393 to 408 were read whole, where 395 to 397 were read by search only.

**Bound:** the check re-read the passages this dispatch quotes and the objects named above; it did not read the
generator functions listed as NOT read, `gen_guard_state.py`, `gen_status_batch_bound.py`, or the lists ruling
record, and Task 2 Edit 1's quotation of Ruling 2 of the 2026-10-14 L3 record is relayed from the write-back dispatch,
which read that record whole. No task, cut, prediction of a count, or bar changed.
