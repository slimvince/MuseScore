# The L0+L1 exemplar selection — the separation check and the ruled pick (dispatch, 2026-08-31)

> **STATUS: WRITTEN, NOT STARTED.** Written by the Cowork writing side on 2026-08-31, executing
> **Ruling 12** of `cowork_rulings_2026_08_31_decision_surface_sitting.md` §3l. **The user opens it
> with the CC run of his choice** (the 2026-08-26 role ruling: the writing side writes instructions
> to disk and never starts the runs that execute them).
>
> **★ THE WRITING SIDE'S RESTRAINT, DECLARED ON THIS DISPATCH'S FACE.** From the moment this file is
> handed over, the writing side does not touch it, and does not touch any file named in §0's
> read-first block, while the batch runs. A session that edited a live dispatch across four turns had
> CC observe three states of it, one reversing an edit CC had already made; Task 0 exists so that
> cannot recur.
>
> **This dispatch selects exemplar scores. It renders no boot pack, writes no brief, boots no
> deriving session and derives nothing.**

## 0. Boot — read before any other act

You start clueless. **A single-file opening instruction is not an exemption from the standing
conventions** (`CLAUDE.md` Conventions, the ordinary-session-start-read rule, ratified 2026-08-29,
P-1). In order:

1. The ordinary session-start read: `CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, and the
   derived gating answer (`tools/audit/nongating_apparatus_rows.json` → `★_the_live_gating_answer`
   → `gating_ids`).
2. `BUILD_AND_TEST.md` — **conditionally mandatory and the condition is MET here**: this batch runs
   Python tools.
3. `cowork_rulings_2026_08_31_decision_surface_sitting.md` **§3j, §3k and §3l** — Rulings 10, 11 and
   12, which are what this batch executes. **Read them whole, not their headings.**
4. This document, whole.

**The bash rules of `CLAUDE.md`'s VS Code section bind every command in this batch** — the exit-code
echo and the no-large-output rule — and are not restated here (#6).

## 1. Why this batch exists, in one paragraph

**Ruling 10** made **L0+L1** the detail-specification phase's first deriving subject. **Ruling 12**
settled how annotated material reaches that subject's blind deriving session: **plain scores only, no
published analyses, selected by a MECHANICAL criterion over the corpus's own note tables, the
criterion written and shown to the user BEFORE the selection runs.** The criterion is written and is
reproduced whole in §3 of this document. **Ruling 12 also carries an overturn condition**: if the
criterion does not separate the corpus, the ruled outcome flips to staging nothing. **This batch
computes the check, applies the fixed decision rule, and reports. It stages nothing itself.**

## 2. Task 0 — pin the instruction and its subjects

Pin this file and every file §0 names to git blobs with `git hash-object -w`, record the hashes in
the report, and **take every later read in this batch from `git cat-file blob <hash>`** rather than
from the working tree. A read that disagrees with its pin is a **STOP**.

## 3. Task 1 — build the measurement tool and compute the four properties

**The criterion, reproduced whole because this dispatch must be self-sufficient. Every property is
tied to a clause of the ratified L1 charter and to nothing about this project's implementation.**

- **P1 — release-driven change points.** The charter's change point is *"every onset and every
  release"*. **Compute:** from each piece's note table, the onset set **O** = `quarterbeats` and the
  release set **R** = `quarterbeats + duration_qb`. Report **|R \ O|** and its share of |O ∪ R|.
- **P2 — change points invisible to pitch class. THE LOAD-BEARING PROPERTY.** The charter's ground for
  including releases is that a slice's identity is the sounding **note** set and not the octave-folded
  pitch-class set, so a unison or octave shrink is a real change though the pitch classes are
  unchanged. **Compute:** at every change point, form the sounding note multiset immediately before and
  immediately after, and compare it twice — by `midi` pitch, and by pitch class (`midi` mod 12). Report
  the count of change points at which **the note set changes and the pitch-class set does not**.
- **P3 — ties crossing a bar line.** **Compute:** from the `tied` column against `mc`, the count of
  tied groups spanning a bar boundary.
- **P6 — simultaneity density.** **Compute:** `n_onsets` against `n_onset_positions`, from
  `metadata.tsv`.

**P4 (time signature and whether the piece carries more than one) and P5 (repeat and volta bars) are
read from `metadata.tsv` and are used only by the tie-break in Task 2, not by the separation check.**

**Sources, and nothing else:** `tools/dcml/bach_chorales/notes/*.notes.tsv` and
`tools/dcml/bach_chorales/metadata.tsv`. **Establish both at the objects before computing** — the
column names used above were read from one note table and from the metadata header by the writing
side, and a column that is absent or differently named is a **STOP**, not something to work around.

**The criterion uses every note in the table**, where the charter says *"every onset and every release
of an **eligible** note"*. **Eligibility is a question the derivation itself must answer, so the
criterion deliberately does not pre-empt it. This is a simplification of the SELECTION, never of the
specification** — record that sentence in the artifact.

**Output:** a new generator `tools/audit/gen_l0l1_exemplar_selection.py` writing
`tools/audit/l0l1_exemplar_selection.json`, carrying the per-piece values, the distributions, the
decision rule of Task 2 verbatim, and its own verdict. **Every figure this batch reports is a figure of
that artifact, cited to it and never transcribed into prose (#17f, D-431).**

## 4. Task 2 — apply the fixed decision rule, then the ruled pick

**The decision rule, FIXED BEFORE THE MEASUREMENT and not to be adjusted after seeing it.** Let **z**
be the share of pieces whose **P2 count is zero**.

- **If z ≥ 0.5, P2 SEPARATES and Option B stands.** Half or more of the corpus shows nothing on the
  charter's own decisive case, so choosing which pieces are staged buys real coverage.
- **If z < 0.5, P2 DOES NOT SEPARATE and the ruled outcome is Option A: no score is selected and none
  is staged.** A pick that cannot distinguish is a random pick wearing an evidential label.

*The threshold is a declared bar, set before measuring, on the reasoning above; it is not tuned to an
observed distribution and must not be. Report **z** and the verdict, whichever way it falls.*

**If and only if B stands, select THREE pieces**, on the pilot's own precedent of three and on no
number this side invented:

1. Rank all pieces by **P2 descending**; break ties by **P3 descending**, then by **piece number
   ascending**. **The first selection is the top-ranked piece.**
2. **The second** is the highest-ranked piece whose **time signature differs** from the first's.
3. **The third** is the highest-ranked piece whose **repeat/volta structure differs** from the first
   two — carrying repeats where they do not, or the reverse.
4. If a rule at step 2 or 3 cannot be satisfied anywhere in the corpus, **that is a finding**: record
   it, fill the slot with the next-ranked piece, and say plainly in the report which rule went
   unsatisfied.

**Record in the artifact, for each selected piece: its name, its `rel_path` from `metadata.tsv`, and
its P1, P2, P3, P4, P5 and P6 values.** **Stage nothing and copy nothing** — staging is the writing
side's act, performed from this artifact.

## 5. Task 3 — establish the boot-pack generator, READ ONLY

The next dispatch renders an `l0-l1` boot pack, and **this side has not established which tool renders
one.** Two packs exist at `tools/audit/derivation_boot_pack/harmony-boundary/` and `…/scoring-model/`,
each holding a read-me and six numbered members. **Establish at the objects, read-only: which tool
generates a pack, from what ruled reading list, and how a new subject is added.** Report what you find,
with the file and the symbol. **Change nothing.** **If no such generator exists — if the packs were
produced by an act that left no re-runnable tool — that is a finding and a STOP for the next dispatch's
author, not a thing to build here.**

## 6. STOPs — surface, never absorb

- A named column absent from `metadata.tsv` or from a note table, or present under a different name.
- A read disagreeing with its Task 0 pin.
- A piece whose note table cannot be parsed, or which `metadata.tsv` names and the notes directory
  does not hold — **report the identities, do not silently drop them, and report the population both
  ways.**
- Any act outside §7's footprint.
- No pack generator found (Task 3).

**Each STOP is written up and reported. This batch repairs nothing it finds.**

## 7. The footprint — enumerated from this batch's own orders

**Created:** `tools/audit/gen_l0l1_exemplar_selection.py`; `tools/audit/l0l1_exemplar_selection.json`;
this batch's report file.

**Edited:** nothing under `src/`, `tools/corpus/`, `tools/robust_stop/`, `docs/`, and **no existing tool
source except the forward bound's own per-batch re-aiming, `gen_status_batch_bound.py --apply`, which is
EXCEPTED BY NAME** under Ruling 5 of `cowork_rulings_2026_08_26_amendment_landing_sitting.md`. **No
governing document is amended.** **`FRAMEWORK.md` is not touched** — Ruling 11's filtering governs what a
boot pack CARRIES, never what that document SAYS, and no pack is rendered here.

**Not done at all:** no build, no test, no golden, no measurement of the analysis, no corpus
regeneration, nothing under `tools/robust_stop/`. **The corpus's note tables and `metadata.tsv` are read
and never written.** **No open-items row is created, flipped or discarded; no decisions-register entry is
written and no `D-NNN` is allocated** — that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route. **The workbook is not opened.**

**The tracked-modification assumption, stated as a SHAPE with a STOP and never as a count:** this batch
expects the working tree to carry untracked Cowork ruling records, handoff entries and reading-pass
material, and expects to add the two tracked files named above. **If the tree carries a tracked
modification this batch did not make, STOP and report it** rather than proceeding around it.

## 8. Done

The batch is done when: `l0l1_exemplar_selection.json` exists and is regenerable by its own tool; **z**
and the separation verdict are recorded in it; the three selections are recorded with their values, **or
the artifact records that Option A obtains and no piece is selected**; Task 3's finding is reported; and
every STOP met is written up. **Then close on the ruled stop form** — what was done, what was not, and
that the remainder is untouched.

**The standing self-check runs before the report is written** (`CLAUDE.md`, the self-check after every
coding exercise): re-read the actual diff of every touched file against the guiding principles, the
conventions and `DEFECT_TYPES.md`, and surface any violation rather than shipping it.

---

*Provenance: written by the Cowork writing side, 2026-08-31, executing Ruling 12 of
`cowork_rulings_2026_08_31_decision_surface_sitting.md` §3l. Read at the files by this side before
writing: `FRAMEWORK.md` §5 and §9 whole; the phase-definition surface §3.2 and §3.4;
`cowork_blind_session_brief_scoring_model.md` whole; the two existing boot-pack directories at the
object; `tools/dcml/bach_chorales/metadata.tsv`'s header row and first two rows; and one note table,
`notes/001 Aus meines Herzens Grunde.notes.tsv`, for its column names. **No generator, symbol or
convention is named in this dispatch that this side has not opened** — which is why Task 3 orders the
pack generator ESTABLISHED rather than naming one. No shell command was run on the repository by the
writing side. No figure of this project's own measurement is restated (#17f, D-431).*
