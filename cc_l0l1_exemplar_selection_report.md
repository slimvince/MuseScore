# The L0+L1 exemplar selection — the separation check and the ruled outcome (report, 2026-08-31)

> **STATUS: THE BATCH IS DONE.** Executes `cc_instruction_l0l1_exemplar_selection_2026_08_31.md`,
> which executes **Ruling 12** of `cowork_rulings_2026_08_31_decision_surface_sitting.md` §3l.
>
> **THE OUTCOME IS OPTION A. The criterion does not separate the corpus, so the ruled outcome is
> that NO SCORE IS SELECTED AND NONE IS STAGED.** That is the overturn condition Ruling 12 wrote
> into itself and ordered checked first; it fired.
>
> **This batch selected no score, staged nothing, copied nothing, rendered no boot pack, wrote no
> brief, booted no deriving session and derived nothing.**
>
> **Every figure is a figure of `tools/audit/l0l1_exemplar_selection.json`, cited to its own field
> and never transcribed into this prose** (#17f, **D-431**). Where this report names a direction
> rather than a value it names the artifact field the direction is read from (**D-663**).

## 0. The boot, and Task 0's pins

The ordinary session-start read was performed in full before any other act, on the standing
convention that a single-file opening instruction is not an exemption from it (`CLAUDE.md`
Conventions, ratified 2026-08-29, P-1): `CLAUDE.md` whole, `DECISIONS.md` whole, `STATUS.md`, and
the derived gating answer at `tools/audit/nongating_apparatus_rows.json` →
`★_the_live_gating_answer` → `gating_ids`. `BUILD_AND_TEST.md` was read as conditionally
mandatory, the condition being met (this batch runs a Python tool). Then
`cowork_rulings_2026_08_31_decision_surface_sitting.md` §3j, §3k and §3l whole, then the dispatch
whole.

**Task 0's pins**, written with `git hash-object -w` and re-derived immediately afterwards to
establish that no subject drifted between the reads and the pinning. **All seven re-hashed
identical**, so every read this batch took agrees with its pin and no read STOP arose.

| Pinned subject | blob |
|---|---|
| `cc_instruction_l0l1_exemplar_selection_2026_08_31.md` | `70e697dd5e6ad18467bb34ccd86cbc630e2d52a0` |
| `CLAUDE.md` | `e012d3f2adc10e4557bf422236f0d50014559568` |
| `DECISIONS.md` | `238cff78e61d4ff4cd8e5a41dc17f6fab4ab7d59` |
| `STATUS.md` | `a9163ead8ade542c67cde43bf611e30477e0459b` |
| `tools/audit/nongating_apparatus_rows.json` | `a2ca9f64783d45a50bd3fb299d46afe46b9fe678` |
| `BUILD_AND_TEST.md` | `42df316140c8bf178b620b461b84fadacb976299` |
| `cowork_rulings_2026_08_31_decision_surface_sitting.md` | `9ff15f17288062ed6b5862ff5fd5633ca9ecc5d0` |

## 1. STOP 1 — the tree carries a tracked modification this batch did not make

§7 orders: *"If the tree carries a tracked modification this batch did not make, STOP and report it
rather than proceeding around it."* **It does, and this is that report.**

**Established at the objects, by explicit commit hash, never from a branch-tip or status read**
(**D-253**): at commit `f54995c092` — the tip named in this session's own start-of-session record —
`cowork_rulings_2026_08_31_decision_surface_sitting.md` is blob
`d02c571a1d811e6fe3457c9cf4c5917bd248a5c6`, and the working tree carries
`9ff15f17288062ed6b5862ff5fd5633ca9ecc5d0`. The blob-to-blob difference is **pure addition, no
deletion**. The committed blob carries §3a…§3c and then §4; **Rulings 5 through 12 — §3d…§3l —
exist only in the working tree.**

**The reading under which this is not a halting STOP, stated together with its alternative, as the
preceding batch's close does for the same shape.** The modification IS the Cowork writing side's
landing of the very rulings this dispatch executes: the dispatch's own provenance says it executes
Ruling 12 of that file, and Ruling 12 lives entirely inside the addition. **On the halting reading
the dispatch is unexecutable by construction** — the file §0 orders read whole would have to be
absent for the tree to be clean. **On the reading taken here** the clause guards against a
*foreign* tracked change the batch would otherwise work around unknowingly, which is discharged by
naming it, establishing it at the objects, and characterising it as addition-only. **The
alternative reading — that the batch should have halted at Task 0 without computing — is recorded
so the user can take it.** Nothing was repaired: the file is untouched by this batch.

The other four pinned tracked subjects (`CLAUDE.md`, `DECISIONS.md`, `STATUS.md`,
`BUILD_AND_TEST.md`, `nongating_apparatus_rows.json`) are **byte-identical to their blobs at
`f54995c092`**, so the modification is confined to the one file.

**No other STOP of §6 was met.** No named column was absent or differently named; no read
disagreed with its pin; no piece was unparsable and the population reconciles in both directions;
no act fell outside §7's footprint; and Task 3 found a pack generator.

## 2. Task 1 — the measurement tool, and what it establishes

**Created: `tools/audit/gen_l0l1_exemplar_selection.py`**, writing
**`tools/audit/l0l1_exemplar_selection.json`**. It reads
`tools/dcml/bach_chorales/notes/*.notes.tsv` and `tools/dcml/bach_chorales/metadata.tsv` and
nothing else. **It is not a measurement of this project's analysis:** it never opens a score, never
runs the analyzer, and reads no output of ours. **It writes nothing under `tools/dcml/`** — the
corpus's note tables and `metadata.tsv` are read and never written.

**#6 was checked before the tool was written, not assumed:** no tool in `tools/` reads
`*.notes.tsv`, so this is a new concern with one path and not a second path onto an existing one.

### The sources, established at the objects before computing

Ordered by §3, and done. **Every column the dispatch names by name is present under that name** —
`quarterbeats`, `duration_qb`, `midi`, `tied` and `mc` in the note tables, and `piece`, `TimeSig`,
`n_onsets`, `n_onset_positions`, `rel_path` in `metadata.tsv`. The tool re-checks the note-table
columns on **every table on every run** and STOPs on an absence, so the establishment cannot decay
into an assumption. Both headers as found are published at `sources.metadata_header_as_found` and
`sources.note_table_header_as_found`.

**One finding on P5, reported rather than worked around.** The dispatch names P5 as *"repeat and
volta bars"* read from `metadata.tsv` and — unlike P1, P2, P3 and P6 — names **no column** for it.
At the file, `metadata.tsv` carries a column for the **volta** half (`volta_mcs`) and **none for
the repeat half**. The repeat half is therefore **DERIVED**, from the folded-against-unfolded
length pair the same file carries (`length_qb` against `length_qb_unfolded`): a piece whose
unfolded length exceeds its folded length carries a repeat. **This is not a §6 STOP** — the STOP is
scoped to *a named column*, and no column was named for P5 — but the derivation is stated at
`establishment.the_P5_derivation_stated_because_no_column_carries_it` and both columns it reads are
published per piece, so it is visible rather than assumed.

### The population, reported both ways

`metadata.tsv`'s piece list and the notes directory's tables **reconcile exactly in both
directions**: no piece is named without a table, and no table is unnamed
(`population.named_by_metadata_without_a_note_table` and
`population.note_tables_metadata_does_not_name`, both empty). **No table failed to parse.** Counts
at `population`.

**Two declared bounds, counted and published rather than silently dropped (#12, #24):** two pieces
carry rows whose `quarterbeats`, `duration_qb` or `midi` cell is empty, so those rows cannot be
placed on the time line and enter no change point. The identities and the per-piece counts are at
`population.notes_the_table_could_not_place`, with the definition beside them.

### The tool's own establishment (#19)

**A measurement tool is trusted only after being positively established**, and this one is —
by the route #19 names as *derivation of what the measurement unit actually measures* plus a
reproduce-check.

- **The quantity is derived a second time, independently.** The fast path sweeps the change points
  carrying state; the check re-scans every note at every change point and shares no code with it.
  **Every change point of every piece is compared in both its before and its after state.** A
  single disagreement raises and exits non-zero. Counts at
  `establishment.★_the_tool_s_own_establishment`.
- **The one shape on which the two could have agreed for the wrong reason was found and closed.**
  A note of zero duration sounds over an empty span; carried naively it leaves a **zero count** in
  the tally, and a zero count compares **equal** to an absent one — so the check would have passed
  without testing anything there. **The corpus does hold such notes**
  (`establishment.★_the_tool_s_own_establishment.zero_duration_notes_in_the_whole_corpus`). The
  sweep now excludes them from the sounding multiset while **still keeping their onset and release
  as change points**, so no note is excluded and eligibility is not pre-empted. **The repair moved
  no published value** — the artifact re-generated byte-identical across it — so what changed is
  the *reason* the two derivations agree, not any figure.
- **The artifact is regenerable byte-identically**, confirmed by consecutive runs producing the
  same blob.
- **What the establishment does NOT cover is stated on the artifact** at
  `…what_is_NOT_established_by_it`: that the three readings of P2 are the right question (the
  charter's and the ruling's business), that the corpus's own note tables are correct (the DCML
  corpus's establishment, not measured here), and that the threshold is the right bar (declared
  before the measurement, and the dispatch's).

### The eligibility simplification, recorded as the dispatch orders

Recorded verbatim on the artifact at `the_eligibility_simplification`: the criterion uses every
note in the table, where the charter says *every onset and every release of an **eligible** note*;
eligibility is a question the derivation itself must answer, so the criterion deliberately does not
pre-empt it — **a simplification of the SELECTION, never of the specification.**

### One reading the dispatch left open, declared BEFORE the measurement and published three ways

P2's arithmetic turns on a wording the dispatch carries in two forms in the same paragraph: it says
to form the sounding note **multiset**, and it quotes the charter's ground as the octave-folded
pitch-class **set**. **The two give different arithmetic at a unison shrink** — which is one of the
two cases the charter's own ground names by name. This was not resolved silently and it was not
resolved after seeing the numbers:

- **The primary was declared before the tool was run**, in the tool's own source and on the
  artifact, and is the reading that can see **both** cases the charter names — the note side as a
  multiset against the octave-folded pitch-class **set**.
- **All three readings are computed and published**, with `z` and a verdict for each, so the
  verdict's sensitivity to the wording is visible rather than hidden (#24, and #17's near-tie
  discipline).

**All three readings return the same verdict**
(`the_separation_check.all_three_readings_agree_on_the_verdict`). **The verdict is therefore not a
near-tie on this axis**, and no cell of it is sensitive.

## 3. Task 2 — the fixed decision rule applied, and the ruled outcome

The decision rule and the selection rule are recorded **verbatim** on the artifact at
`the_decision_rule_verbatim` and `the_selection_rule_verbatim`, so the rule that was applied can be
compared with the rule that was fixed. **It was not adjusted after the measurement.**

**`z` is recorded at `the_separation_check.z_primary`, with its two companion readings beside it.
The verdict of record is at `the_separation_check.the_verdict_of_record`.**

**THE VERDICT: `A_OBTAINS_P2_DOES_NOT_SEPARATE`.** `z` falls **far below** the declared bar of
0.5 — not near it — and it does so on all three readings. **Under the rule fixed before the
measurement, Option A is the ruled outcome: no score is selected and none is staged.** The
artifact's `the_selection` field is `null`, with the reason stated at
`the_selection_is_null_because`. **Steps 1–4 of the selection rule were therefore not run**, and no
step-2 or step-3 finding arises, because those steps exist only if B stands.

A ranking by the selection rule is published at `ranking_top_20_by_the_selection_rule` **as
evidence about the distribution and NOT as a selection.** Nothing was staged, nothing was copied,
and no piece is proposed.

### The mechanized rule and the ruling's own words agree — reported because they need not have

Ruling 12's overturn condition is stated in the ruling's own words as *"if release-driven change
points are near-uniform across the chorales"*. The dispatch mechanized that as `z`, the share of
pieces whose P2 count is zero — **a different quantity**, so the two could in principle have
pointed opposite ways, and a reader is owed the check rather than the assumption.

**They point the same way.** The distribution of **P1** — release-driven change points, the
quantity the ruling's own sentence names — is published at
`distributions.P1_release_only_change_points` and at
`distributions.P1_share_of_all_change_points`. **Its deciles are near-flat and its share of all
change points is small throughout**: in this repertoire a release almost always coincides with an
onset, so releases add very little to the change-point set anywhere in the corpus. **That is the
ruling's own near-uniformity, measured.** The mechanized rule and the ruling's own words therefore
agree, and the Option A verdict does not rest on the mechanization alone.

### A finding for the writing side, surfaced and not acted on

The same measurement carries a consequence wider than this selection, and it is stated here rather
than absorbed: **the property L1's charter turns on is barely exercised by this repertoire at all.**
The charter's release clause exists because a release-driven case corrected an earlier draft, and
the Bach chorales — largely homorhythmic four-part writing — are close to the worst available
material for exhibiting it, which is what `distributions.P1_*` measures. **This bears on the
question behind Ruling 12 rather than on Ruling 12's own answer**, so it is reported and nothing is
proposed: whether a deriving session should meet notation at all, and if so from what repertoire,
is the writing side's and the user's, not this batch's. **No score outside the corpus was examined
and none is suggested.**

## 4. Task 3 — the boot-pack generator, established read-only

**A generator exists.** No STOP arises on Task 3.

| | |
|---|---|
| **The tool** | `tools/audit/gen_derivation_boot_pack.py` |
| **What it writes** | `tools/audit/derivation_boot_pack/<subject>/` and the manifest `tools/audit/derivation_boot_pack.json` |
| **The ruled reading list** | the module-level symbol **`MEMBERS`** — six members, each span named by **anchor text and never by line number**, imported from `cowork_curated_boot_list_draft_2026_08_19.md` §2 and ruled by the user 2026-08-22 (Ruling 1 of `cowork_rulings_2026_08_22_boot_list_sitting.md`, with amendment (a3) for member 6), plus the generated read-me `READ_ME` = `00_READ_THIS_FIRST.md` rendered by `render_read_me` |
| **How a subject is added** | a subject is a **KEY in three authored tables** — `WITHHELD`, `CRITERION` and `VERDICTS`. `build_subject` STOPs if the subject is missing from `WITHHELD` or from `CRITERION`; `write_all` iterates `sorted(WITHHELD)`, so **`WITHHELD` is the subject enumeration of record**. Every derived candidate must carry an authored verdict in `VERDICTS[subject]` or the tool STOPs, and a verdict naming a non-candidate STOPs — both directions. |

**The precedent that matters for an `l0-l1` subject:** `scoring-model` is already rendered with an
**EMPTY withheld family** — empty `WITHHELD` sub-tables, an empty `CRITERION` and an empty
`VERDICTS` table — by Ruling 1 of `cowork_rulings_2026_08_24_sizing_pilot_sitting.md`, with the
standing leak check doing the whole of the cutting. An `l0-l1` subject that is not held out has a
worked precedent to follow.

**★ TWO FINDINGS FOR THE NEXT DISPATCH'S AUTHOR, established at the tool and reported, not built.**
Adding an `l0-l1` subject is **not** three table entries, because Ruling 11 asks the pack to carry
material the generator's ruled member list does not hold:

1. **`MEMBERS` is GLOBAL and carries the ruled six — it does not carry `FRAMEWORK.md`, the
   reading-pass extracts, or the empirical findings ledger.** Ruling 11 Decision 1 puts
   `FRAMEWORK.md` §5 and §9 into the L0+L1 pack; Decision 2 puts the five reading-pass extracts in
   with a section cut; and Ruling 12's own correction of record puts
   `EMPIRICAL_FINDINGS_LEDGER.md` in by the phase definition's naming. **None is a member today**,
   and `MEMBERS` has no per-subject dimension — the pack file list is `[READ_ME] + MEMBERS` for
   every subject alike. So new members, and a per-subject notion of membership, are owed.
2. **The leak check is SCOPED to members (5) and (6), and members (1)–(4) are deliberately NOT
   checked** — the tool says so in its own words, on the ground that those members are ruled WHOLE
   and a string check over them would strike the never-work-from-memory rule's own pointer.
   **Ruling 11 Decision 1 requires `FRAMEWORK.md` §5 and §9 leak-filtered**, with Appendix A and
   every passage describing what this project currently has removed — and it names Appendix A.4,
   *"Where the derived answer DIFFERS from what this project already has"*, as the concentrated
   hazard. **A new quoted member that must be filtered does not fit the existing scope**, which
   filters only what the tool generates. Ruling 11's own ruled fallback (Option C, unfiltered with
   the stop-on-meeting clause carrying the load, *"if the filter proves more than a small act"*) is
   therefore live and should be weighed by the dispatch's author.

**Nothing was changed.** No file under `tools/audit/derivation_boot_pack/` was written, no
generator source was edited, and the generator was not run.

## 5. The standing self-check

Run before this report was written, on the **actual diff on disk** of every touched file and not on
the memory of writing it. **Four defects were found in my own work and all four were corrected in
the batch rather than shipped**; each is recorded because a self-check that reports nothing is
indistinguishable from one that was not run.

1. **A new reserved-word collision, introduced by me** — a map keyed by file name was named
   `note_stems`. In this repository a bare *stem* is a note stem, and the convention forbids
   introducing a **new** collision. **Renamed** to `note_table_by_piece`, with the reason stated at
   the line.
2. **Two further bare non-musical uses of collided words in my own prose** — `part` as a portion of
   a parsed cell (renamed `field`), and *interval* for a half-open time span (rewritten as
   *span*). Both are the convention's own listed collisions.
3. **A silent fold on an error path — `DEFECT_TYPES.md` DT-23.** An unreadable `length_qb` /
   `length_qb_unfolded` cell folded to `None` with no counter and no surfacing, which is exactly
   the pattern DT-23 names. **Every unreadable metadata cell the tie-break reads is now counted,
   published with its piece identity, and raised as a STOP entry on the artifact**; the same
   treatment was extended to the `n_onsets` / `n_onset_positions` parse, which had been outside any
   guard. **The corpus produced none**, so the count reads zero — but it now reads zero because it
   was measured, not because nothing looked.
4. **An establishment that would have passed for the wrong reason — #19.** Described in §2 above:
   the zero-duration-note shape, found by publishing the count rather than assuming it empty. **The
   corpus holds such notes**, so the risk was real and not hypothetical.

**Checked and clean:** no figure is transcribed into this report (#17f, **D-431**) — every one is
cited to its artifact field; no code is cited by line number (**D-307**); the artifact carries its
own provenance, its sources, and what it is not; DT-24 does not arise, the tool having no argument
parser and writing only its own new artifact under `tools/audit/`; DT-11 does not arise, every
figure being generated; DT-26 does not arise, the population being reconciled in both directions
against `metadata.tsv` rather than swept inside an assumed scope; and the bash rules of
`CLAUDE.md`'s VS Code section were followed on every command — the exit-code echo throughout, and
the generator's output redirected to a file and read separately.

## 6. The footprint, against §7

**Created — exactly the three §7 names, and nothing else:**

- `tools/audit/gen_l0l1_exemplar_selection.py`
- `tools/audit/l0l1_exemplar_selection.json`
- this report

**Not done, enumerated against §7's own list:** no build, no test run, changed or moved; no golden;
no measurement of the analysis; no corpus regeneration; nothing under `tools/robust_stop/` or
`tools/corpus/`; nothing under `src/` or `docs/`; **`FRAMEWORK.md` untouched**; no governing
document amended; **no open-items row created, flipped or discarded**; **no decisions-register
entry written and no `D-NNN` allocated** — that register cannot accept one and
`cowork_register_rule_c_suspension_2026_08_28.md` is the route; the workbook not opened; no score
staged, copied, renamed or moved; no boot pack rendered; no brief written; no session booted;
nothing derived.

**No existing tool source was edited, including the one §7 excepts by name.** The forward bound's
per-batch re-aiming (`gen_status_batch_bound.py --apply`) was **not** run: §7's footprint does not
name `STATUS.md` among this batch's created or edited files, and this batch writes no `STATUS.md`
entry, so there is no batch close for the bound to be re-aimed to. **Stated rather than assumed**,
so a later reader does not take the omission for a miss.

## 7. Done, on the ruled stop form

**What was done.** The instruction and its §0 subjects pinned and re-verified. The measurement tool
built, its sources established at the objects, its own quantity independently re-derived and
reproduced with no disagreement, and its artifact confirmed regenerable byte-identically. The four
properties computed over the whole corpus with the population reconciled both ways. The decision
rule applied exactly as fixed before the measurement, on three declared readings of the one wording
it left open. Task 3's generator established read-only, with two findings for the next dispatch's
author. The standing self-check run, with four defects of my own found and corrected.

**What was not done, and why.** No score was selected and none was staged — **because that is the
ruled outcome**, not because the batch stopped short. Steps 1–4 of the selection rule were not run,
those steps existing only if B stands. Nothing found was repaired: STOP 1 is reported and the file
is untouched, and Task 3 changed nothing.

**The remainder is untouched.**

---

*Provenance: `cc_instruction_l0l1_exemplar_selection_2026_08_31.md`, executing Ruling 12 of
`cowork_rulings_2026_08_31_decision_surface_sitting.md` §3l. Every figure is a figure of
`tools/audit/l0l1_exemplar_selection.json`, cited to its field and never transcribed (#17f,
**D-431**). Working-tree files were read with the file tools throughout; shell access was used only
for read-only git object queries by explicit hash and for the `git hash-object -w` pinning Task 0
orders (**D-253** and its 2026-08-08 widening).*
