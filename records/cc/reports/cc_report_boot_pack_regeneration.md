# CC REPORT — THE DERIVATION BOOT PACKS ARE REGENERATED

*Executing `cc_instruction_boot_pack_regeneration.md`, written by the Cowork writing side against tip
`68c42b7f7743c02bdebefacdd9ed06ca9060fbbe`. This batch carries NO ruling and NO decision. It is a
regeneration and one forward-bound move.*

*Every figure below is stated beside the command that produced it. Where a hash appears, the side it
was measured on is named. No hash of this file is written into this file.*

---

## 0. What this batch is, in one paragraph

Three ruled clause amendments landed in `CLAUDE.md` at principles #18, #19 and #24 on 2026-08-26. The
two derivation boot packs render the guiding principles and the ratified design intent, and both were
generated before that landing, because the amendment-landing dispatch's §6 fenced off the generator,
the manifest and the pack directories. So both packs rendered the pre-amendment text, and the previous
batch reported that consequence rather than leaving it to be found. This batch cures it, checks that
the cure did not move what is withheld from an implementation-blind session, moves the `STATUS.md`
forward bound with the tool ruled for it, runs the guard sweep, and does nothing else.

---

## 1. Task 0 — the start state

### 1(a) The session-start read

Taken in full through the file tools (**D-253**): `CLAUDE.md`, `STATUS.md`, `DECISIONS.md`. The
conditional read `BUILD_AND_TEST.md` was **taken**, because this session runs measurement tools whose
commands the record keeps there. Rule (a)'s pointer was opened at its artifact —
`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer` → `gating_ids`.

### 1(b) The tip

`.git/refs/heads/master`, read with the file tool, reads
`68c42b7f7743c02bdebefacdd9ed06ca9060fbbe`. **It matches the tip the dispatch was written against**,
so nothing below rests on another tree. This is the **ref side** — the branch tip as the ref file
records it, not a worktree measurement and not a blob hash.

### 1(c) The changed-path population

```
python tools/audit/changed_paths.py
```

→ **834 changed path record(s) [worktree]**, of which:

| | count | note |
|---|---|---|
| untracked (`??`) | **833** | the standing untracked population — already routed, and **not committed by this batch** |
| tracked, modified (` M`) | **1** | `cowork_handoff.md` |

**★ THE ONE TRACKED MODIFICATION IS DECLARED RATHER THAN ASSUMED AWAY, BECAUSE THE DISPATCH DOES NOT
MENTION IT.** Task 0(c) speaks only of an untracked population; the tree also carried one *tracked*
modification at the start of this batch — `cowork_handoff.md`, which is the writing side's own file
and is consistent with Task 0(d)'s statement that the sixty-sixth entry is already merged there. **It
is not mine, it was not touched, and it is not in this batch's commit.** It is named here so that a
reader reconciling the tree arithmetic is not left to discover an unexplained modification.

### 1(d) The handoff merge

`cowork_handoff_entry_66_pending.md` does not exist in the tree (Glob over the repository root
returns no such path), and the dispatch states the merge is already done. **Not re-performed, and no
pending file created.**

---

## 2. Task 1 — the drift, measured before it was cured

```
python tools/audit/gen_derivation_boot_pack.py --check
```

**Exit code: 1.** The complete output, verbatim:

```
STALE: the derivation boot pack does not re-derive
  - derivation_boot_pack.json does not re-derive
  - harmony-boundary/02_the_guiding_principles_and_the_conventions.md does not re-render
  - harmony-boundary/05_the_ratified_design_intent.md does not re-render
  - scoring-model/02_the_guiding_principles_and_the_conventions.md does not re-render
  - scoring-model/05_the_ratified_design_intent.md does not re-render
```

**The drift list is exactly what the dispatch predicted** — the manifest plus four pack files, two per
subject. The dispatch's premise held, so its STOP condition ("if it exits 0") did not fire.

**Why member 05 is in the list as well as member 02, stated because the dispatch's own paragraph
predicts only the principles.** Member 02 is the two `CLAUDE.md` spans, which the amendments changed
directly. Member 05 is GENERATED from the ruled design intent, whose entries carry the register's own
`verbatim` fields — and the previous batch re-anchored three of those entries to the amended home
text. Both halves of the drift therefore have the same cause, and neither is a surprise (#3, #13).

---

## 3. Task 2 — the regeneration

```
python tools/audit/gen_derivation_boot_pack.py
```

**Exit code: 0.** Output, verbatim:

```
wrote tools\audit\derivation_boot_pack.json
  harmony-boundary: design-intent 244 · candidates 75 · IN 16 / OUT 59 / UNPLACED 0
    withheld 33 (16 authored + 17 derived) · documents 1 · passages 2 · leaks 3
    rendered: 208 design-intent entries, 25 defect-type rows, 7 files
  scoring-model: design-intent 244 · candidates 0 · IN 0 / OUT 0 / UNPLACED 0
    withheld 0 (0 authored + 0 derived) · documents 0 · passages 0 · leaks 3
    rendered: 241 design-intent entries, 25 defect-type rows, 7 files
```

No flag was passed. `--subject` was **not** used: both subjects were stale and both were re-rendered.

Then, immediately:

```
python tools/audit/gen_derivation_boot_pack.py --check
```

**Exit code: 0.** Output, verbatim: `the derivation boot pack re-derives`.

**The two exit codes, stated together as the dispatch asks: BEFORE = 1, AFTER = 0.**

---

## 4. Task 3 — the blinding check. Counts only.

**Nothing withheld is named here.** No withheld passage, no withheld identity string and no withheld
document name appears anywhere in this report, so a session that must stay blind can read it.

### 4.1 The six numbers, new pack against old

| subject | quantity | BEFORE Task 2 | AFTER Task 2 | changed? |
|---|---|---|---|---|
| `harmony-boundary` | withheld identities | 33 | 33 | **no** |
| `harmony-boundary` | withheld documents | 1 | 1 | **no** |
| `harmony-boundary` | withheld passages | 2 | 2 | **no** |
| `scoring-model` | withheld identities | 0 | 0 | **no** |
| `scoring-model` | withheld documents | 0 | 0 | **no** |
| `scoring-model` | withheld passages | 0 | 0 | **no** |

**All six are unchanged, so the dispatch's STOP does not fire.** A regeneration that changed what is
withheld would not be a regeneration; this one changed nothing of the kind.

### 4.2 Where each number was read, and how the BEFORE side was established twice

- **AFTER** — `tools/audit/derivation_boot_pack.json` → `subjects.<subject>.counted`, read with the
  file tools at the tree the regeneration left.
- **BEFORE, first route** — the same field of the same file, read with the file tools **before** the
  regeneration was run.
- **BEFORE, second route** — `git show 68c42b7f7743c02bdebefacdd9ed06ca9060fbbe:tools/audit/derivation_boot_pack.json`,
  a content-addressed read by explicit hash (the one git read **D-253** permits), captured outside the
  repository and read with the file tools. **This is the blob side** — the file as the commit records
  it, which for this file is the same content the worktree held before Task 2, the path carrying no
  worktree modification at the start state (§1(c)).

The two BEFORE routes agree on all six numbers. That matters because the first route is a reading of a
file this batch then overwrote: without the second, the comparison would rest on a value that can no
longer be re-read.

### 4.3 The withheld identities split, reported because the total alone could hide an offsetting move

| subject | authored | derived (cross-reference additions) | total |
|---|---|---|---|
| `harmony-boundary` | 16 → 16 | 17 → 17 | 33 → 33 |
| `scoring-model` | 0 → 0 | 0 → 0 | 0 → 0 |

Neither half moved, so the unchanged total is not the sum of two changes cancelling.

### 4.4 Three further checks, taken because `--check` alone re-renders with the *same* withholding

`--check` re-renders and compares; it cannot by itself tell a reader that the withholding still lands
where it did, because it applies the same authored table it always applies. Three additional
measurements were taken at the objects:

1. **The cut is the same size.** Each withheld passage's `characters_omitted` in the new manifest is
   identical to the value in the committed manifest at the tip (690 and 211). A passage anchor that
   had drifted onto different text would move that number.
2. **The markers are in place.** The omission marker appears **twice** in `harmony-boundary`'s member
   02 and **zero** times in `scoring-model`'s, which is what the two subjects' passage counts require.
   (Measured by a content search over the pack directory; the marker string is the generator's own and
   discloses nothing.)
3. **Nothing else in the pack moved.** `leaks` is 3 → 3 for both subjects; rendered design-intent
   entries 208 → 208 and 241 → 241; defect-type rows 25 → 25; files in the pack 7 → 7; and the
   design-intent class 244 → 244. Had an entry entered or left the withheld set, at least one of these
   would have moved.

### 4.5 What DID change in the pack, stated so the regeneration is not read as inert

The four drifted files now carry the amended governing text. Positively established rather than
assumed: a content search over the pack directory for the three amended clauses' opening phrases
returns **three hits in each subject's member 02** — one per amended principle — and one hit in each
subject's member 05, which is the register entry whose `verbatim` quotes the amended home text. Before
the regeneration those files carried the pre-amendment wording, which is what made them drift.

---

## 5. Task 4 — the `STATUS.md` entry and the forward bound

### 5.1 The entry

One entry written in `STATUS.md`, at the head of the file under its own living-document convention.
Per the OI-222 remedy it is a **POINTER** to this report, and per **D-431** it restates **no count, no
identity and no rendered value**. It names what the batch did and what it did not do, and it carries
the `Last updated: ` prefix, which the previous batch's entry gave up in the same act (that prefix
movement is the one declared textual adjustment the forward-bound tool already imports rather than
re-decides).

### 5.2 The forward bound — the tool was read first, then re-aimed, then run

The dispatch deliberately does not state the flag. **It was read from the tool's own argument parser**
(`main()`: a mutually exclusive group of `--apply`, "perform the move (once)", and `--check`,
"re-derive the reconciliation"), not inferred.

**The exact command line used:**

```
PYTHONIOENCODING=utf-8 python tools/audit/gen_status_batch_bound.py --apply
```

The `PYTHONIOENCODING` prefix is this session's standing precaution for the OI-374 encoding class and
changes no behaviour of the tool, which routes its own printing through `output_encoding.py` in any
case.

**The five aiming constants, with the value each was set to:**

| constant | value set |
|---|---|
| `BASE_COMMIT` | `68c42b7f7743c02bdebefacdd9ed06ca9060fbbe` |
| `PREVIOUS_BATCH_DISPATCH` | `cc_instruction_amendment_landing.md` |
| `ACT_DATE` | `2026-08-26` |
| `DISPATCH` | `cc_instruction_boot_pack_regeneration.md` |
| `TASK` | `Task 4` |

`ACT_DATE` was already at the value this batch requires, both batches falling on the same date; it was
checked against the archive header it is interpolated into rather than left unread, which is the check
the dispatch's "five, not three" correction asks for. `RULINGS` was **not** touched: it names Ruling 4
of 2026-08-17, the standing ruling the tool executes, and it is not an aiming constant.

**And one row appended to `PREVIOUS_AIMINGS`**, recording the outgoing aiming:

| field | value |
|---|---|
| `executing_act` | `cc_instruction_amendment_landing.md, Task 7` |
| `base_commit` | `2d7c3c3119e92dadb7b8fbffa76403ef5c7b6f5f` |
| `the_then_previous_batch` | `cc_instruction_register_reconciliation.md` |

**Why the appended row is inside the carve-out and not a widening of it.** Ruling 5 of
`cowork_rulings_2026_08_26_amendment_landing_sitting.md` states the mechanism in its own words: *"It is
re-aimed each batch by editing three authored constants and appending a row to its `PREVIOUS_AIMINGS`
list"*, and then rules **that** re-aiming a named carve-out. The append is part of the act the ruling
names, not an extra edit taken beside it. The tool's own comment demands the same thing — *"every
previous aiming is recorded rather than overwritten (#12)"* — and omitting the row would reproduce
exactly the gap the previous batch had to backfill one row above it.

**The order of operations, which is load-bearing.** The entry was written **first** and the previous
batch's entry had its `Last updated: ` prefix taken off in the same edit; only then was `--apply` run.
Run the other way round, the tool's occurrence test would have found the previous entry zero times in
the live file and STOPped, because it looks for the text with that prefix already stripped.

**The result:**

```
wrote tools\audit\status_batch_bound.json
  entries moved: 1, 2,617 characters
  byte-present in the archive exactly once: True
  absent from the must-read:                True
```

Exit code 0. `STATUS.md` now holds this batch's entry alone; the previous batch's entry stands verbatim
in `STATUS_ARCHIVE.md` under the header the tool interpolates `ACT_DATE`, `DISPATCH` and `TASK` into —
which is why those three had to be re-aimed and not only the two that steer the move.

### 5.3 The two validations the sweep re-ran

Both passed at the final sweep round: `gen_status_batch_bound.py --check`, and
`gen_governing_surface_split.py --check --pair STATUS.md`.

---

## 6. Task 5 — the sweep

The ruled sweep is `python tools/audit/gen_guard_state.py`, with
`python tools/audit/gen_guard_classification.py` run after it, in that order, because the
classification reads the artifact the state tool writes and its own STOP requires the order.

### 6.1 Round 1

**75 guards run, 71 passing, 4 failing, 4 not run, 16 historical records.**

Every red was classified **at its own captured text, before anything was regenerated**:

| # | guard | captured text | class | acted |
|---|---|---|---|---|
| 1 | `gen_filing_convention_application.py --check` | `STOP: derived candidates with no authored verdict: BUILD_AND_TEST_ARCHIVE.md, OPEN_ITEMS_ARCHIVE.md, cc_report_preparation_fourteenth.md. An unclassified candidate is a STOP, never a silent pass (D-661).` | **DECISION — the standing [[OI-372]] red** | **untouched** |
| 2 | `apply_soft_discard.py --check` | `STOP: the committed plan's recorded arithmetic disagrees with the data file's: the plan records {'the_live_record_before': 677, 'retired_by_this_act': 165, 'the_live_record_after': 512}, while the block's former population is 680 and 165 record(s) carry this act's own `retired_by`` | **DECISION — standing** | **untouched** |
| 3 | `apply_residue_discard.py --check` | `STOP: the sitting's arithmetic does not reconcile at ['the_whole_population', 'the_live_record']` … `"the_live_record": {"before_this_act": 515, "after_this_act": 477, "the_movement_the_sitting_states": "512 → 474", "it_reconciles": false}` … `the ruling makes this a STOP-and-report, not an adjustment` | **DECISION — standing** | **untouched** |
| 4 | `gen_session_start_read_size.py --check` | `STALE vs the measurement: session_start_read_size.json does not re-derive` | **regeneration (staleness), by construction** | **regenerated** |

**Red 1 is the standing red the dispatch names.** `open_items/OI-372.md` rows this tool, and the
previous batch's report records the same guard failing with **exactly these three** unclassified
candidates. **The list is unchanged: the same three, no fourth.** It was **not** regenerated, **not**
run in write mode, and **not** investigated. One correction of record, offered because it bears on how
the row will be read and not because anything was done about it: OI-372's narrative describes the
tool's **third** STOP (an authored verdict naming a document the derivation no longer carries), while
what fires at this tree is the **second** (a derived candidate with no authored verdict), which is
raised first in the tool's own order. Whether the third STOP is still latent behind it is **not
established here** and no verdict is proposed — the row's own text reserves that.

**Reds 2 and 3 are the two the dispatch names and forbids curing.** Curing either means running a
ruled discard act in write mode, which this dispatch does not authorise. Both were left. Their
arithmetic is unsatisfiable together with the register's growth: red 3's live-record limb reconciles at
no value while the sitting's stated movement pins a size the register has since passed.

**Red 4 is a staleness red and was regenerated.** Its subject is the size of the session-start read,
and this batch wrote to `STATUS.md`, which is a member of that read — so the measurement was stale *by
construction* the moment Task 4 ran. This is the same class the previous batch met and cured for the
same reason. Regenerated with `python tools/audit/gen_session_start_read_size.py`, exit code 0.

**No red was ambiguous, so the dispatch's absolute rule — treat an unclassifiable red as a DECISION red
and STOP — was not reached.**

### 6.2 Round 2

**75 guards run, 72 passing, 3 failing, 4 not run, 16 historical records.**

The failing set is the three standing reds and nothing else. `gen_derivation_boot_pack.py --check`
passes, which is this batch's own subject clearing.

### 6.3 Round 3 — run with this report present on disk

**75 guards run, 72 passing, 3 failing, 4 not run, 16 historical records** — identical to round 2.

**Why a third round was run at all.** The standing red's candidate population is derived over the
repository root's own `*.md` files, so a report landing at the root can in principle enter it and widen
a red this batch is forbidden to touch. The check was therefore re-run with `cc_report_boot_pack_regeneration.md`
present. **The candidate list is unchanged — the same three, no fourth.** This report did not widen the
standing red.

### 6.4 The blast radius the dispatch told me to watch

The dispatch notes that one register row moves five artifacts, two of them invisible to an instruction
phrased as regenerating only what goes red, and says that since no register row is ordered here the
radius should not open — and that its opening would itself be a finding. **It did not open.** No
register row was created, moved or touched; `DECISIONS.md`, `tools/audit/decisions/backbone_decisions.json`
and every file under `decisions/` are unmodified at the tree this report closes over, and every
register guard passes.

### 6.5 The residue, in full

1. `gen_filing_convention_application.py --check` — the standing [[OI-372]] decision red.
2. `apply_soft_discard.py --check` — decision red, named by the dispatch and forbidden to cure here.
3. `apply_residue_discard.py --check` — decision red, named by the dispatch and forbidden to cure here.

Four guards are **NOT RUN** and sixteen are **HISTORICAL RECORDS**; both populations are the guard
runner's own authored classes and neither moved this batch.

---

## 7. Everything that moved, named in full

Measured with `python tools/audit/changed_paths.py` at the tree this report closes over. Thirteen
tracked paths differ from the tip; **twelve are this batch's and one is not.**

| path | why it moved | fence bullet |
|---|---|---|
| `tools/audit/derivation_boot_pack.json` | Task 2 | named |
| `tools/audit/derivation_boot_pack/harmony-boundary/02_the_guiding_principles_and_the_conventions.md` | Task 2 | named |
| `tools/audit/derivation_boot_pack/harmony-boundary/05_the_ratified_design_intent.md` | Task 2 | named |
| `tools/audit/derivation_boot_pack/scoring-model/02_the_guiding_principles_and_the_conventions.md` | Task 2 | named |
| `tools/audit/derivation_boot_pack/scoring-model/05_the_ratified_design_intent.md` | Task 2 | named |
| `tools/audit/gen_status_batch_bound.py` | Task 4(b) — five aiming constants and one appended row | named carve-out |
| `STATUS.md` | Task 4(a) entry written; Task 4(b) tool then took the previous entry out | named |
| `STATUS_ARCHIVE.md` | written by `gen_status_batch_bound.py --apply` | tool output |
| `tools/audit/status_batch_bound.json` | written by the same run | tool output |
| `tools/audit/guard_state.json` | written by `gen_guard_state.py` | tool output |
| `tools/audit/guard_classification.json` | written by `gen_guard_classification.py` | tool output |
| `tools/audit/session_start_read_size.json` | written by `gen_session_start_read_size.py` | tool output |
| `cc_report_boot_pack_regeneration.md` | this file, new | named |
| — | — | — |
| `cowork_handoff.md` | **NOT THIS BATCH'S.** Modified in the tree at the start state (§1(c)). Untouched here and **not in the commit.** | outside |

Two artifacts moved without ever appearing in a failing set — `guard_state.json` and
`guard_classification.json` — because they record the sweep rather than being checked by it. They are
named here for that reason.

The untracked population is **833** at the start and **833** at the close, this report being the only
new path and being committed. The tree arithmetic closes: 834 records at the start, 847 at the close,
the difference being twelve paths this batch wrote plus this report.

---

## 8. Departures, and every instruction I could not obey

**No instruction of this dispatch could not be obeyed, and the §7 fence was not reached.** Nothing
required a write outside it, so no route was chosen, no fence widened, and no weaker form of an
instruction was substituted. Four things are declared anyway, because each is something a reader would
otherwise have to discover.

**(1) A tracked modification existed at the start state and the dispatch does not mention it.**
`cowork_handoff.md`. Left untouched, not staged, not committed. §1(c).

**(2) The generator's own source was opened, and it carries the authored withheld table.** Task 3 asks
for three counts per subject; the counts live in a manifest field whose name is not stated in the
dispatch, so the generator was read to locate them. Its authored inputs sit in the same file. **This
session is not a deriving session and boots from no pack**, so no blinding of mine was at stake — and
nothing read there is quoted, paraphrased or hinted at in this report, which carries counts only.

**(3) One staleness red was regenerated, and the dispatch does not name it.** Task 5 orders the sweep
"as ruled" and names three reds that are not this batch's to cure; the standing sweep rule cures a
regeneration red and STOPs on a decision red. `gen_session_start_read_size.py` was run in write mode on
that basis, and `tools/audit/session_start_read_size.json` is named in §7 as its output. **If the
writing side intended the sweep to be read-only in this batch, this is the one act to disallow** — it
is separable, it moved no verdict, and it changed nothing but a measurement of the read's own size.

**(4) `gen_guard_classification.py` was run after each `gen_guard_state.py` run.** It is the second
half of the ruled sweep and its own STOP requires that order; `tools/audit/guard_classification.json`
is named in §7 as its output.

**Declared, not measured:** the dispatch's own account of why the packs were stale, and the previous
batch's account of the standing red's candidate list, are quoted from those records; the candidate list
itself was **re-measured here** and agrees.

---

## 9. What this batch did not do

No edit to `CLAUDE.md`. No edit to `ARCHITECTURE.md`. **No entry in the decisions register** — a
regeneration is not a ratification, so rule (c) is not engaged, and the two broken discard-act checks
stayed out of this batch's path exactly as the dispatch shaped it to. No `src/` change. No test
changed, moved or run. No golden. Nothing under `tools/corpus/`. Nothing under `tools/robust_stop/`.
No open-items row created, flipped or discarded. No finding number allocated. No admission to the
empirical findings ledger. Neither blind derivation output was opened. No behaviour change to the
analysis, and no measurement of the analysis built, designed, scoped or run. No derivation and no
comparison. Exactly one path under `tools/` ending `.py` differs from the tip, and it is the one the
dispatch permits by name. Nothing of the standing untracked population was committed or touched.

---

## 10. The standing self-check

The diff of every path this batch wrote was re-read on disk before this report was closed, against the
guiding principles, the conventions, the gate and preset policies, and the known problem types.

- **#6, one path per concern.** Nothing was copied to a second home. The forward bound was moved by the
  one tool that owns it, and the entry it took out is in one place.
- **#12, no information loss.** The previous batch's entry travelled whole and byte-faithfully, proven
  by the tool's own two-direction reconciliation rather than by my reading of it. The outgoing aiming
  of the forward-bound tool was written down instead of being written over.
- **#15, verify at the objects.** Every count in §4 was read at the artifact, and the earlier side of
  the comparison was established twice — once at the file before it was rewritten, once through a
  content-addressed read by explicit hash.
- **#17f and D-431.** The `STATUS.md` entry is a pointer and carries no count, no identity and no
  rendered value. Every figure in this report is stated beside the command that produced it.
- **#19.** Nothing here is trusted for being unfalsified: the cure was checked by re-running the check,
  and the blinding was checked by four independent measurements rather than by the check alone.
- **The reserved-word convention.** *Measurement tool*, *check* and *generator* are used throughout; no
  script is called an instrument.

One thing the self-check surfaced and could not close inside this batch's fence, carried to the writing
side rather than acted on: the row that tracks the standing red describes a different STOP of that tool
than the one firing at this tree. It is stated in §6.1, no verdict is proposed, and the row is
untouched.
