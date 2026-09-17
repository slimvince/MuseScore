# The two remaining exemplar slots — a counted sweep, not a hand-picked set (dispatch, 2026-09-01)

> **STATUS: WRITTEN, NOT STARTED.** Written by the Cowork writing side, executing **Ruling 15 (§3o)**'s
> own next act — *"establish at the objects which in-tree scores carry which phenomenon … then bring the
> named set to the user with each score's claim beside it"* — under the three check questions of **§3u**
> and **§3v**, and as the first application of **Ruling 20 (§3z)** Tiers A and B.
> **The user opens it with the CC run of his choice.**
>
> **★ THE WRITING SIDE'S RESTRAINT.** From hand-over, the writing side does not touch this file or any
> file named in §0's read-first block while the batch runs.
>
> **★ WHY A SWEEP AND NOT A HANDFUL OF FILES. STATED BECAUSE IT IS THE REASON THIS BATCH EXISTS.** The
> writing side could stage six or eight likely files and read them. It has been doing exactly that, and
> §3y records the cost: **four consecutive claims in the record asserted without checking**, every one
> written from memory of a reading rather than from the reading. **Worse, choosing WHICH files to open
> is this side's hand — the objection Ruling 12 upheld against its own option D.** A counted sweep
> removes both: the files are not chosen, they are all counted, and the counts are the answer.
>
> **★ AND THE BOUND THAT GOVERNS HOW ITS OUTPUT MAY BE USED — RULING 20's FOURTH.** *Whole-corpus counts
> say what our corpora cannot test; they must not be used to pick exemplars.* **This batch does not
> violate that, and the distinction is exact: it asks EXISTENCE questions — does this file contain a
> grace note, a meter change, a fermata — which is the check Ruling 15 requires at the file before a
> score is staged. It must NOT be used to ask a REPRESENTATIVENESS question**, such as which score sits
> nearest a corpus median. **Frequency is reported so the user can see it. It does not choose.**
>
> **★ THIS BATCH SELECTS NOTHING AND STAGES NOTHING.** It reports counts. **Which files fill the slots
> is the user's**, on the surface the writing side brings from this batch's table.

## 0. Boot — read before any other act

You start clueless; a single-file opening instruction is not an exemption (ratified 2026-08-29, P-1).

1. The ordinary session-start read: `CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived
   gating answer.
2. `BUILD_AND_TEST.md` — **conditionally mandatory, condition MET** (this batch runs a Python script it
   writes).
3. `docs/score_inventory.md` — **whole.** Hard rules **2** and **3** bind by name.
4. `cowork_rulings_2026_08_31_decision_surface_sitting.md` **§3l (Ruling 12), §3o (Ruling 15), §3u, §3v,
   §3y and §3z (Ruling 20)** — **whole.** §3z's four bounds govern this batch's output.
5. `cc_exemplar_decode_report_2026_09_01.md` — **whole**; the slot already filled and the method this
   batch reuses.
6. This document, whole.

The bash rules of `CLAUDE.md`'s VS Code section bind every command (#6).

## 1. Task 0 and Task 1 — pin, then establish the start state

**Pin** this file and every file §0 names with `git hash-object -w`. A read disagreeing with its pin is a
**STOP**.

**Establish and report BEFORE anything rests on it:**

- **The tracked-modification shape.** *If the standing shell-read guard refuses `git status --porcelain`,
  use the substitute it names and say so — the two preceding batches both met this.*
- **That each corpus directory of §2 exists, and its `.mscx` file count.** **A directory that does not
  exist is reported and skipped, not a STOP.**
- **That `tools/audit/derivation_exemplars/l0-l1/bwv1049_03_presto.mscx` still stands at 1,701,770 bytes
  with `sha256 a4d9d89798469f654e120e08884c4c6e3c47c2842e2b2fccc53ec9db87fbac80`.** It is this batch's
  **control**: it must appear in the output table with the counts the previous batch established
  (`<Harmony>` 0, `<FiguredBass>` 0, `<StaffText>` 0, 9 body staves, `programVersion` 3.0.0). **A
  divergence there means the counting script is wrong, and IS a STOP.**

## 2. Task 2 — the sweep

**Over every `.mscx` in these directories, and no others:**

| Directory | Why it is in scope |
|---|---|
| `tools/dcml/bach_chorales/MS3/` | the chorale slot — the gate repertoire and the corpus's own idiom (Ruling 15) |
| `tools/dcml/couperin_clavecin/MS3/` | keyboard ornaments |
| `tools/dcml/scarlatti_sonatas/MS3/` | keyboard ornaments |
| `tools/dcml/handel_keyboard/MS3/` | keyboard ornaments |
| `tools/dcml/cpe_bach_keyboard/MS3/` | keyboard ornaments |
| `tools/dcml/bach_en_fr_suites/MS3/` | keyboard ornaments |
| `tools/dcml/frescobaldi_fiori_musicali/MS3/` | keyboard, and Ruling 19's declared fallback lives here |
| `tools/audit/derivation_exemplars/l0-l1/` | the control |

**Nothing under `"tools/extra scores"`, `tools/corpus/`, `corpora/` or `when_in_rome/` is swept.** If a
listed directory is missing, report and continue.

**Per file, emit one row. Every value is a COUNT taken from the file — never an estimate, never a
judgment.**

**(a) Identity and fitness — Ruling 20 Tier B, the three check questions of §3u and §3v:**
`sha256`; byte size; `<Harmony>`; `<FiguredBass>`; `<StaffText>`; part-list `<Staff>` count and body
`<Staff>` count; `<museScore version>`; `<programVersion>`; `<programRevision>`.

**(b) Notated elements — Ruling 20 Tier A, off `FRAMEWORK.md` §5's L0 given-list and L1's *Publishes*
block:** `<Fermata>`; ties; `<Pedal>`; repeats and voltas; double bars; rests; **distinct time
signatures, listed**; **distinct key signatures, listed**; notes with `visible="0"`; non-sounding notes;
and the bar, chord and note totals.

**(c) Notated elements bearing on the OPEN faces, counted as elements and nothing more:** ornaments **by
`<subtype>` with each subtype named and counted**; `<appoggiatura/>`; `<acciaccatura/>`; grace-note
chords by whatever element the format uses, **named**; `<Tremolo>`; cue-sized notes if the format marks
them.

**★ ON (c), THE ONE LINE THAT KEEPS IT HONEST.** These are **counts of notated elements** — Kind 1, safe.
**They are NOT a claim that any of these opens a change point or sounds.** That is face (a), the largest
hole the charter leaves, and it is the deriving session's to fill. **The count is a fact; what it means
is not this batch's to say, and no row carries an interpretation.**

**★ AND THE THING THIS BATCH MUST NOT DO. NO COLUMN IS A JUDGMENT.** There is **no** *has staggered
entries* column, **no** *has ornaments worth staging*, **no** *suitability* or *quality* column, and no
ranking. Ruling 20's line is that a judged tag is this side's hand with a table around it.

## 3. Task 3 — the discriminating check, which Ruling 20's third bound requires

**For every column, report its distribution over the swept population: how many files have zero, the
minimum, the maximum, and the count of distinct values.** **A column whose value is identical across
every swept file is reported as NON-DISCRIMINATING**, by name, in its own list.

**This is not decoration. It is the P2 lesson written into the method:** a criterion that does not
separate its corpus is a random pick wearing evidence, and Ruling 12's overturn condition fired on
exactly that. **A non-discriminating column tells the user something real — that our corpora cannot
exercise that case — and Ruling 20's bound 4 says that is what this table is FOR.**

**Report also, per corpus and per column, the count of files with a non-zero value**, so a phenomenon
absent from a whole corpus is visible as such.

## 4. Task 4 — the two open slots, answered by existence and not by preference

**Report, as lists of file paths and nothing more:**

- **(a) Files with a NON-ZERO grace-note count, AND separately with a non-zero ornament count**, each
  broken down by subtype. Face (a).
- **(b) Files with MORE THAN ONE distinct time signature**, with the signatures listed. Face (d).
- **(c) Files with a NON-ZERO fermata count.** Face (e).
- **(d) Files that are PLAIN** — `<Harmony>`, `<FiguredBass>` and `<StaffText>` all zero — as a list, and
  **the count of plain files per corpus.**

**Do not recommend a file. Do not rank. Do not mark any file as a candidate.** Ruling 15 requires the
named set to go to the **user** with each claim beside it, and that is the writing side's act on this
batch's table.

**★ ONE RESULT IS EXPECTED AND IS NOT A DEFECT.** §3u established that five of five non-chorale DCML
corpora carry annotation in the score file. **If (d) returns few or no plain files outside the chorales,
that is the established pattern reproducing at scale, not a failure of this batch** — and it is
precisely the fact the user needs, because it decides whether the remaining slots go by decode, by
bar-in-brief, or unfilled.

## 5. Task 5 — write the table

Write **one** machine-readable output — **`tools/audit/score_tags_l0l1_sweep.json`** — and **the script
that generates it**, at `tools/audit/gen_score_tags.py`. **Ruling 20's bounds 1 and 2 are why both
exist:** the table is generated and re-derivable, never hand-maintained (**#19**), and it is **one**
artifact, not a sixth hand-kept registry (**#6**).

**The script takes its directory list as an argument or a named constant at the head — it does not
hard-code a hidden scope.** Its output carries, at the top: the directories swept, the file count per
directory, the generation date, and **the script's own `sha256`**, so a later reader can tell whether a
table was produced by the script standing beside it.

**No existing registry, manifest or pin is edited.** `tools/extra_scores_registry.json`,
`tools/score_census_registry.json`, `tools/corpus_registry.json` and
`tools/snapshot_sources_manifest.json` are **not touched**, not read for authority, and gain no row.

## 6. Done

Done when: the control file reproduced its established counts; every listed directory was swept or
reported missing; every row carries every column of §2 with no estimated value; §3's distribution and
non-discriminating list are reported; §4's four lists are given as paths; and the script and its table
stand at the two paths of §5. **Every STOP met is written up. Then close on the ruled stop form.**

**The standing self-check runs before the report is written** — the actual diff on disk of every touched
file, against the principles, the conventions and `DEFECT_TYPES.md`. **DT-26 is the live risk again: the
per-file counts must reconcile against each file's own whole-file element totals, and a file that fails
to parse is REPORTED, never silently skipped (DT-23).**

## 7. STOPs

The control file's counts diverging from §1; a read disagreeing with its pin; writing anywhere outside
the two paths of §5 and this batch's report; any act outside §8.

**Not a STOP, and reported rather than resolved:** a listed directory missing; a file that fails to
parse; a column that is non-discriminating; **few or no plain files outside the chorales**; the
shell-read guard refusing a command.

## 8. The footprint

**Created:** `tools/audit/gen_score_tags.py`, `tools/audit/score_tags_l0l1_sweep.json`, and this batch's
report — **and nothing else.** **Edited: NOTHING.** **No score is read for anything but counting, and no
score is edited, renamed, moved, converted, copied or re-saved** — including the Frescobaldi file, which
is swept as one row like any other and **is not otherwise touched**. `.gitattributes` is **not** edited —
**the `.mscx` byte-stability question stays OWED to the user (§3y)**. No registry, manifest or pin is
touched; **`tools/snapshot_sources_manifest.json` and the eleven snapshot sources are untouched (Hard
rule 2)**.

**Not done at all:** no build, no test, no golden, **no measurement of the analysis** — every count here
is a property of a score file and none is an output of this project's analyzer; nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; **no boot pack rendered and neither frozen pack
opened**; **no governing document amended**; **no open-items row created, flipped or discarded**; **no
decisions-register entry and no `D-NNN`** — that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route; the workbook not opened; **NO SCORE
SELECTED AND NO SCORE STAGED**; no brief written or amended; no session booted.

**The tracked-modification assumption, as a SHAPE with a STOP.** This batch expects untracked Cowork
material, **and expects these tracked-and-modified files: `FRAMEWORK.md`,
`cowork_rulings_2026_08_31_decision_surface_sitting.md`, `tools/audit/derivation_boot_pack.json` and
`tools/audit/gen_derivation_boot_pack.py`** — the four the two preceding batches both established, the
sitting record having since gained §3y and §3z. **It also expects `tools/audit/derivation_exemplars/` as
UNTRACKED**, being the previous batch's product. **None is a STOP. Any OTHER tracked modification this
batch did not make IS a STOP.**

---

*Provenance: written by the Cowork writing side, 2026-09-01, executing Ruling 15's own next act under
§3u's and §3v's check questions and Ruling 20's Tiers A and B. **The facts this dispatch asserts were
read at their objects by this side with file tools**: the corpus directory names at `tools/dcml/`; the
L0 given-list and L1 *Publishes* block at `FRAMEWORK.md` §5; the control file's size at
`tools/audit/derivation_exemplars/l0-l1/`. **The control file's digest and counts are RELAYED from
`cc_exemplar_decode_report_2026_09_01.md` and §1 orders them re-established, because a relayed figure is
not this batch's.** No shell command was run on the repository by the writing side. No figure of this
project's own measurement is restated (#17f, D-431).*
