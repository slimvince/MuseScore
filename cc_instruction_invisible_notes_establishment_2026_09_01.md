# The 242 invisible notes in `wq55n02a.mscx` — what they are, established before the file is staged (dispatch, 2026-09-01)

> **STATUS: WRITTEN, NOT STARTED.** Written by the Cowork writing side, executing the condition that is
> part of **Ruling 22 (§3ac)** of `cowork_rulings_2026_08_31_decision_surface_sitting.md`.
> **The user opens it with the CC run of his choice.**
>
> **The writing side's restraint.** From hand-over, the writing side does not touch this file or any file
> named in §0's read-first block while the batch runs.
>
> **What this batch is for.** Ruling 22 stages `tools/dcml/cpe_bach_keyboard/MS3/wq55n02a.mscx` for the
> L0+L1 deriving session **on one condition, which is part of the ruling rather than an addition to it**:
> that the reason for its 242 invisible notes is established at the file first. The count is established;
> the reason is not, and it covers about a fifth of the file. If those notes turn out to be an editorial
> artifact of that edition rather than ordinary notation, the exemplar would teach the deriving session
> about a quirk of one edition instead of about notation, and Ruling 22's declared fallback fires.
>
> **What this batch is NOT.** **It stages nothing, selects nothing, and decides nothing.** It reports
> facts about one file, with a small amount of corpus context. **Whether those facts amount to ordinary
> notation or to an editorial artifact is the user's ruling, on the surface the writing side brings from
> this batch.** Do not offer that verdict, and do not mark the file suitable or unsuitable.

## 0. Boot — read before any other act

You start clueless; a single-file opening instruction is not an exemption (ratified 2026-08-29, P-1).

1. The ordinary session-start read: `CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived
   gating answer.
2. `BUILD_AND_TEST.md` — **conditionally mandatory, condition MET** (this batch runs a Python script it
   writes).
3. `docs/score_inventory.md` — whole. Hard rules 2 and 3 bind.
4. `cowork_rulings_2026_08_31_decision_surface_sitting.md` **§3o (Ruling 15), §3u, §3v, §3aa, §3ab
   (Ruling 21) and §3ac (Ruling 22)** — whole. §3ac is the authority. **§3ab is why this document avoids
   the word *bar* except in its metric sense.**
5. `cc_slot_sweep_report_2026_09_01.md` — whole. Its figures are **relayed**; §1 orders the load-bearing
   ones re-established.
6. This document, whole.

The bash rules of `CLAUDE.md`'s VS Code section bind every command (#6).

## 1. Task 0 and Task 1 — pin, then establish the start state

**Pin** this file and every file §0 names with `git hash-object -w`. A read disagreeing with its pin is a
**STOP**.

**Establish and report before anything rests on it:**

- **The subject file is the object the sweep measured.**
  `tools/dcml/cpe_bach_keyboard/MS3/wq55n02a.mscx` must be **552,240 bytes**, and its `sha256` must equal
  the one the sweep table records for it. **A mismatch is a STOP.**
- **The three counts the sweep reports for it, re-established at the file**: `notes_invisible` **242**,
  `notes_non_sounding` **5**, `cue_sized_small` **244**; and alongside them `chords` **1,140**,
  `measures` **168**, `body_staves` **2**. **A divergence is not a STOP but is reported**, since every
  question below is about those notes.
- **What each of those three counts actually counts, read at `tools/audit/gen_score_tags.py`.** Name the
  element, attribute or child each is derived from, quoting the generator's own line. **This matters
  more than it looks: the sweep already found that `visible="0"` as an attribute does not exist in this
  format and that the child `<visible>0</visible>` is what does.** The three terms must be pinned to what
  the script measured before anything is inferred from them.
- **The tracked-modification shape.** If the standing shell-read guard refuses `git status --porcelain`,
  use the substitute it names and say so.

## 2. Task 2 — where the invisible notes sit

Report, as counts and lists:

**(a)** How many of the file's 168 bars contain at least one invisible note, and **the bar numbers**,
given as ranges where they are contiguous. Are they spread across the file or gathered in a few places?

**(b)** The split **by staff** and **by voice** — how many invisible notes fall in staff 1 and staff 2,
and how many in each `<voice>` within each staff.

**(c)** Whether the invisible notes ever stand **alone** at their moment — that is, whether there is any
tick at which every sounding thing is invisible — and how many such moments there are.

**(d)** Whether any invisible note is **tied** to a visible one, and how many.

**(e)** Three verbatim excerpts of the file itself, each around ten lines, showing an invisible note in
its surrounding context — one from the first place they appear, one from the middle of the file, one
from the last. **Quote the XML as it stands.** The writing side will read these at the object rather
than take a summary of them.

## 3. Task 3 — what the invisible notes are, tested against what would distinguish them

**(a) The duplication test, which is the load-bearing one.** For each invisible note, is there **a
visible note at the same tick with the same pitch**, anywhere in the file? Report: how many invisible
notes have such a partner, how many do not, and — for those that do — whether the partner sits in the
same staff, the other staff, or the same staff in a different voice. **A note written twice, once visibly
and once not, is a different thing from a note written once and hidden**, and this is what separates
them.

**(b) The overlap with the cue-sized notes.** There are 244 cue-sized notes and 242 invisible ones. **How
many notes are BOTH?** Give the three counts: invisible and cue-sized, invisible but not cue-sized,
cue-sized but not invisible.

**(c) The overlap with the five non-sounding notes.** Are those five among the 242 invisible ones, or
separate? **L0's contract gives *whether each note sounds* and *whether it is visible* as two separate
facts**, so how they relate in this file is the point, not an aside.

**(d) What the invisible notes look like as music, without saying what they mean.** Report the
distribution of their durations, and whether they carry ornaments, accidentals, or ties. **Do not
interpret. The counts are the report.**

## 4. Task 4 — the corpus context, kept small and kept honest

The sweep found invisible notes in **17 of 648 files**, with this file's 242 the largest.

Report, from `tools/audit/score_tags_l0l1_sweep.json` and **not by re-reading the scores**: for the
66 files of `tools/dcml/cpe_bach_keyboard/MS3`, how many carry invisible notes at all and what each
carries. This says whether 242 is an outlier within its own corpus or the top of a range.

**This is context, not a criterion.** Ruling 20's fourth bound holds: whole-corpus counts say what the
corpora cannot exercise and **must not be used to pick or reject an exemplar**. Report the numbers; draw
no conclusion from frequency.

## 5. Task 5 — the thirteen `<StaffText>` items, since Ruling 22 excludes them

Ruling 22 excludes `<Harmony>` and `<StaffText>` by element name when this file is staged. **Report the
verbatim text of all thirteen `<StaffText>` items.** The sweep established that in the chorale corpus
`<StaffText>` carries the piece title and catalogue numbers rather than analysis. **If these thirteen are
of that kind, the exclusion of `<StaffText>` may be unnecessary, and that is worth knowing before the
brief is written** — but it is a question for the user, and this batch reports the strings and takes no
view.

## 6. The written predictions, made before the act (#17b)

**A falsified prediction is recorded as falsified and is not repaired into a success.** These are the
writing side's, offered so that the batch's result can contradict something rather than merely
accumulate:

- **P-1:** the invisible notes are **concentrated**, not spread — they fall in a minority of the 168
  bars.
- **P-2:** **a majority of them have a visible partner at the same tick and pitch.**
- **P-3:** the invisible notes and the cue-sized notes are **largely the same notes**, the two counts
  being 242 and 244.
- **P-4:** the five non-sounding notes are **a subset of** the 242 invisible ones.

**Mark each held or falsified with the observed value beside it.** Do not add a prediction of your own
about what the notes mean.

## 7. Done

Done when: the subject file matched its size and digest; the three counts and the generator's definition
of each were re-established and reported; §2's location facts and three verbatim excerpts are given;
§3's duplication, cue-size and non-sounding overlaps are reported with their counts; §4's corpus context
is given from the table; §5's thirteen strings are quoted; and each of the four predictions is marked.
**Every STOP met is written up. Then close on the ruled stop form.**

**The standing self-check runs before the report is written** — the actual diff on disk of every touched
file, against the principles, the conventions and `DEFECT_TYPES.md`. **DT-26 is the live risk: every
count over the invisible notes must reconcile against the 242 total, and a note that fits no category
must be reported rather than dropped.**

## 8. STOPs

The subject file's size or `sha256` not matching §1; a read disagreeing with its pin; writing anywhere
outside this batch's report; any act outside §9.

**Not a STOP, and reported rather than resolved:** a count diverging from the sweep table; a prediction
falsified; the shell-read guard refusing a command; a category that turns out not to apply.

## 9. The footprint

**Created:** this batch's report, and nothing else. **Edited: NOTHING.** **No score is edited, renamed,
moved, converted, copied or re-saved, and no score is written anywhere** — `wq55n02a.mscx` is read only.
**Nothing is staged.** The Couperin fallback file is **not touched, not opened and not read**. No
registry, manifest or pin is touched; `tools/audit/score_tags_l0l1_sweep.json` and
`tools/audit/gen_score_tags.py` are **read only** and neither is edited or regenerated.
`.gitattributes` is **not** edited — that question stays owed to the user (§3y).

**Not done at all:** no build, no test, no golden, no measurement of the analysis; nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; **no boot pack rendered and neither frozen pack
opened**; **no governing document amended**; **no open-items row created, flipped or discarded**; **no
decisions-register entry and no `D-NNN`** — that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route; the workbook not opened; **no score
selected and no score staged**; **no brief written or amended** — the brief's two stale passages stay
owed; no session booted.

**A temporary script is permitted and belongs outside the repository** — the OS temp directory, as the
two preceding batches did. If one is written inside the repository instead, say so and say why; it is not
a STOP but it is a departure.

**The tracked-modification assumption, as a shape with a STOP.** This batch expects untracked Cowork
material, **and expects these tracked-and-modified files: `FRAMEWORK.md`,
`cowork_rulings_2026_08_31_decision_surface_sitting.md`, `tools/audit/derivation_boot_pack.json` and
`tools/audit/gen_derivation_boot_pack.py`** — the four the three preceding batches all established, the
sitting record having since gained §3aa, §3ab and §3ac. **It also expects
`tools/audit/derivation_exemplars/`, `tools/audit/gen_score_tags.py` and
`tools/audit/score_tags_l0l1_sweep.json` as untracked**, being the two preceding batches' products.
**None is a STOP. Any OTHER tracked modification this batch did not make IS a STOP.**

---

*Provenance: written by the Cowork writing side, 2026-09-01, executing the condition that is part of
Ruling 22 (§3ac). The figures this dispatch names — 552,240 bytes, 242 invisible notes, 5 non-sounding,
244 cue-sized, 1,140 chords, 168 bars, 13 `<StaffText>`, and the 17-of-648 corpus fact — are **relayed
from `tools/audit/score_tags_l0l1_sweep.json` by way of `cc_slot_sweep_report_2026_09_01.md`**, and §1
orders the load-bearing ones re-established at the file, because a relayed figure is not this batch's.
No shell command was run on the repository by the writing side. No figure of this project's own
measurement is restated (#17f, D-431).*
