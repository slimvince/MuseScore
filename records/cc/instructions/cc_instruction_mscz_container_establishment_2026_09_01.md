# The `.mscz` container, and the plainness of one candidate score — Ruling 15's constraint (iii), established (dispatch, 2026-09-01)

> **STATUS: WRITTEN, NOT STARTED.** Written by the Cowork writing side, executing the establishment
> **Ruling 15 (§3o) ordered in its own constraint (iii)** and scoped by the finding at **§3u** of
> `cowork_rulings_2026_08_31_decision_surface_sitting.md`. **The user opens it with the CC run of his
> choice.**
>
> **★ THE WRITING SIDE'S RESTRAINT.** From hand-over, the writing side does not touch this file or any
> file named in §0's read-first block while the batch runs.
>
> **★ A NOTE ON THIS FILE'S DATE, STATED RATHER THAN LEFT TO BE INFERRED.** The sitting record this
> batch serves is named and banner-dated **2026-08-31** and is still IN PROGRESS; the sitting has run
> past midnight and **this dispatch is written on 2026-09-01**. The record's name and banner are **NOT**
> changed here — every cross-reference in the tree points at the 08-31 name, and re-dating a live record
> is not this side's act. **The crossing is recorded so a later reader meets it rather than discovers
> it.**
>
> **★ WHAT THIS BATCH IS FOR, IN ONE SENTENCE.** Ruling 15 states that a practical constraint is
> **UNESTABLISHED and must be established before anything is promised** — that `tools/extra scores/`
> holds `.mscz`, a zipped binary container, while the chorales are plain-XML `.mscx`. **The leading
> exemplar candidate for the staggered-entries slot is now a `.mscz`, so that constraint has become
> load-bearing.** This batch establishes what the container is and what one candidate score contains.
>
> **★ AND WHAT IT DELIBERATELY DOES NOT DECIDE.** The half of constraint (iii) that asks *whether a
> session reading with file tools can read a `.mscz` directly* is **NOT put to this batch**, because it
> is answerable by reason once Task 2 reports what the container is, and that reasoning is the writing
> side's to do in front of the user. **This batch reports facts about files. It selects no score, stages
> nothing, promises nothing, and writes no decoded copy into the repository.**

## 0. Boot — read before any other act

You start clueless; a single-file opening instruction is not an exemption (ratified 2026-08-29, P-1).

1. The ordinary session-start read: `CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, the derived
   gating answer.
2. `BUILD_AND_TEST.md` — **conditionally mandatory, condition NOT met** (this batch builds nothing, runs
   no test and runs no project tool). **Read it anyway if any step tempts you toward a build; a batch
   that finds itself wanting one has left its scope.**
3. `docs/score_inventory.md` — **whole**. It is the live governing surface for every score-touching
   task, `CLAUDE.md` sends you there first, and **its Hard rules 2 and 3 bind this batch by name.**
4. `cowork_rulings_2026_08_31_decision_surface_sitting.md` **§3l (Ruling 12), §3o (Ruling 15) and §3u** —
   the two rulings that scope what a staged score may be, and the finding that ordered this batch —
   **whole.**
5. This document, whole.

The bash rules of `CLAUDE.md`'s VS Code section bind every command (#6).

**★ HARD RULE 3 BINDS EVERY COMMAND IN THIS BATCH: the path `"tools/extra scores"` CONTAINS A SPACE and
is always quoted.** An unquoted use is a defect in this batch even where the shell tolerates it.

## 1. Task 0 and Task 1 — pin, then establish the start state BEFORE anything rests on it

**Pin** this file and every file §0 names with `git hash-object -w`; later reads from `git cat-file
blob`. A read disagreeing with its pin is a **STOP**.

**★ THE FOUR SCORE FILES ARE NOT TRACKED AND CANNOT BE PINNED THAT WAY** — `tools/dcml/` is a set of
gitignored clones and `"tools/extra scores/"` is registered, not versioned. **Establish and record each
one's `sha256`, byte size and mtime BEFORE Task 2 and AGAIN at Task 4**, and the two records must match:
that is this batch's proof it modified no input, and it replaces the pin.

**Establish and report, BEFORE any assertion rests on it:**

- **That the four files exist at these paths with these sizes.** This side read the sizes from a
  directory listing on 2026-09-01; **a size that does not match is not a STOP but IS reported**, because
  it means the file moved since this dispatch was written and every count below is then about a
  different object.

  | Path | Bytes this side recorded |
  |---|---:|
  | `"tools/extra scores/large/bach-brandenburg-concerto-no-4-bwv-1049-mvt-iii-presto.mscz"` | 75,260 |
  | `"tools/extra scores/large/haydn-symphony-no-6.mscz"` | 127,386 |
  | `tools/dcml/ABC/MS3/n01op18-1_01.mscz` | 430,695 |
  | `tools/dcml/ABC/MS3/n01op18-1_01.mscx` | 2,050,969 |

- **The tracked-modification shape** (§6), reported before Task 2 begins.
- **Whether `unzip`, `python -m zipfile` or an equivalent is available**, named. **If nothing can read a
  ZIP, STOP and report that** — it is itself an answer to constraint (iii) and is not worked around by
  installing anything.

## 2. Task 2 — what the container IS

**For each of the three `.mscz` files**, without extracting anything into the repository:

**(a) List the archive members** — name, uncompressed size, compression method — and report the listing
whole. **Do not summarise it.**

**(b) State whether the archive contains exactly one score `.mscx`**, and name every other member and
what it appears to be from its name and size alone. **A guess about a member's purpose is labelled a
guess.**

**(c) Extract to a scratch directory OUTSIDE the repository working tree** — the OS temp directory, not
a path under the repo, not a gitignored path under the repo. **Report the absolute scratch path used.**
Record the extracted `.mscx`'s byte size and `sha256`.

**★ WRITTEN PREDICTIONS, MADE BEFORE THE ACT (#17b). A falsified prediction is RECORDED as falsified and
is not repaired into a success.**

- **P-i:** each `.mscz` is a ZIP holding **exactly one** score `.mscx`, plus container metadata and
  probably a thumbnail image.
- **P-ii:** the `.mscx` inside `n01op18-1_01.mscz` is **NOT byte-identical** to its sibling
  `n01op18-1_01.mscx`, because the two mtimes are about a year apart and the `.mscz` is the later.
- **P-iii:** the Brandenburg inner `.mscx` carries **0 `<Harmony>`** and **0 `<FiguredBass>`**, and
  **9 staves**, matching `tools/extra_scores_registry.json`'s measured row.

## 3. Task 3 — the losslessness test, and the plainness check

**(a) THE LOSSLESSNESS TEST, which is why the `ABC` pair is in this batch at all.** `tools/dcml/ABC/MS3/`
holds `n01op18-1_01.mscz` **and** `n01op18-1_01.mscx` side by side. **Compare the archive's inner `.mscx`
against that sibling**, and report, in this order: whether they are byte-identical; if not, the number of
differing lines and **the first ten differences in full**; and **whether any difference touches a
`<Note>`, `<Chord>`, `<Rest>`, `<Staff`, `<Measure>`, `<TimeSig>` or `<KeySig>` element, or only
version stamps, ordering and layout**. **That last distinction is the load-bearing one** — it is what
decides whether decoding a container recovers the notation or alters it, and the answer is reported
plainly whichever way it falls.

**(b) THE PLAINNESS CHECK, on all three extracted `.mscx`.** For each, report **exact counts**, each
obtained by counting in the file and never estimated:

- the number of `<Staff id="N">` **part-list** entries and of `<Staff id="N">` **body** sections, given
  separately, with the ids;
- the count of `<Harmony>`; the count of `<FiguredBass>`; the count of `<StaffText>`;
- every `<trackName>` and every `<instrumentId>`, listed in order;
- **whether any two body staves carry the same notes.** Establish it, do not eyeball it: for each body
  staff emit the ordered sequence of `<pitch>` values for the **first 24 chords** and report the
  sequences; then state which pairs of staves match over that window and which do not. **A pair matching
  over 24 pitches is reported as *matches over the tested window*, never as *duplicate* —** the wider
  claim needs the whole staff and this batch does not make it.

**★ WHY THIS SHAPE.** In `tools/dcml/corelli/MS3/op01n08a.mscx` two staves carry the same bass line, one
bearing 56 Roman numerals and one bearing 47 figured-bass items, and the part list names them
misleadingly. **That file was going to be staged as an exemplar.** This check exists so no candidate is
promised on a registry row again.

## 4. Task 4 — prove nothing moved

**Re-record each of the four input files' `sha256`, size and mtime** and show them against Task 1's.
**Any difference is a STOP.** **Delete the scratch directory** and say so, or state plainly that it was
left and where.

## 5. Done

Done when: the three archives' member listings are reported whole; the losslessness comparison is
reported with its verdict on whether any difference touches notation; the plainness counts are reported
for all three extracted scores with the pitch windows shown; each of the three written predictions is
marked **held** or **FALSIFIED** with the observed value beside it; the four inputs are proven unmoved;
and every STOP met is written up. **Then close on the ruled stop form.**

**The standing self-check runs before the report is written** — the actual diff on disk of every touched
file, against the principles, the conventions and `DEFECT_TYPES.md`.

## 6. STOPs

No ZIP reader available; an input file's `sha256` differing between Task 1 and Task 4; extraction
writing anywhere under the repository working tree; a read disagreeing with its pin; any act outside §7.

**Not a STOP, and each is reported rather than resolved:** an input file's size differing from §1's
table; a prediction falsified; an archive holding more than one `.mscx`, or none.

## 7. The footprint

**Created:** this batch's report, and nothing else. **Edited: NOTHING.** No score is edited, renamed,
moved, converted or re-saved. **No decoded `.mscx` is written into the repository** — not into
`"tools/extra scores/"`, not into `tools/dcml/`, not into a scratch folder under the repo, not anywhere
tracked or gitignored within it. **No tool source is edited.** No registry, manifest or pin is touched —
**`tools/snapshot_sources_manifest.json` and the eleven snapshot sources are untouched, Hard rule 2.**

**Not done at all:** no build, no test, no golden, no measurement of the analysis, nothing under
`tools/corpus/`, `tools/robust_stop/`, `src/` or `docs/`; **no boot pack rendered and neither frozen pack
opened**; **no governing document amended**; **no open-items row created, flipped or discarded**; **no
decisions-register entry and no `D-NNN`** — that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route; the workbook not opened; **no score
selected and NO SCORE STAGED**; no brief written; no session booted.

**One optional line, and it is optional.** `tools/ziprw/` exists in the tree. **If and only if it costs
under a minute**, say in one sentence what it is from its own files — it may be a MuseScore build
dependency and nothing to do with this question. **Establish or omit; do not guess.**

**The tracked-modification assumption, as a SHAPE with a STOP and with the known exceptions named.** This
batch expects untracked Cowork material, **and expects these tracked-and-modified files:
`cowork_rulings_2026_08_31_decision_surface_sitting.md` (the writing side landed §3t and §3u into it),
`FRAMEWORK.md`, `tools/audit/gen_derivation_boot_pack.py`, `tools/audit/derivation_boot_pack.json`, and
the `l0-l1` pack's files** — all products of the three preceding batches. **None is a STOP. Any OTHER
tracked modification this batch did not make IS a STOP.**

---

*Provenance: written by the Cowork writing side, 2026-09-01, executing the establishment Ruling 15's
constraint (iii) ordered, as scoped by §3u. **The facts this dispatch asserts were read at their objects
by this side with file tools**: the four paths and their byte sizes from directory listings of
`"tools/extra scores/large"` and `tools/dcml/ABC/MS3`; the Brandenburg row's measured staves, measures
and notes from `tools/extra_scores_registry.json`; the Corelli staff-duplication and annotation counts
from `tools/dcml/corelli/MS3/op01n08a.mscx`; Hard rules 2 and 3 from `docs/score_inventory.md`. Task 1
nonetheless orders the sizes re-established at the files, because a size is a claim about a file's
current state and this side's read is not the batch's. **No shell command was run on the repository by
the writing side.** No figure of this project's own measurement is restated (#17f, D-431).*
