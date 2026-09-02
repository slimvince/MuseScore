# The COMPARISON — L0 and L1: the derived statements against the outgoing text, every outgoing statement dispositioned

> **STATUS: READING FILE — a tabulation delivered to the user. It recommends nothing, establishes
> nothing, applies nothing, and rules on nothing.** Prepared by Claude Code, 2026-09-02, under
> `cc_instruction_comparison_l0_l1_second_2026_09_02.md` Task 2, executing **Ruling 33** (§3an of
> `cowork_rulings_2026_08_31_decision_surface_sitting.md`) together with **Ruling 32** (§3am), and
> through them Rulings 1–4 and §5 of `cowork_rulings_2026_08_24_comparison_design_sitting.md` and the
> disposition discipline of `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §0
> and §3.4.
>
> **EVERY DISPOSITION BELOW IS A PROPOSAL.** Nothing here is applied to any outgoing text, to the
> derivation, to the brief, to the boot pack, or to any register. The user ratifies later, on a
> decision surface the writing side puts over these rows.
>
> **What the user is asked to rule in this file: NOTHING.** The closing section says so in terms.
>
> **Manifest of this file's own population, counted by this session at the two files.** The derived
> file is `cowork_blind_derivation_l0_l1_2026_08_31.md` (in git at `550874eb35`, blob
> `9b102c575643d672e4747b4cfc23e377cd344c27`): **54 statements** (S-1 to S-54) and **17 open
> questions** (OQ-1 to OQ-17). These counts were taken at that file's own structure by this session
> and are the counts of record for this comparison; the deriving session relayed the same two counts
> in its §5, and this session re-counted rather than carrying them.
>
> **★ THIS TABULATION IS INCOMPLETE AND SAYS SO AT ITS HEAD (D-672).** The population is 29
> documents. Which of them are done, which are untouched, and where the next dispatch resumes are
> stated in the *Progress* section immediately below — read it before reading anything else in this
> file. **No document below is partly worked**: a document is either tabulated whole or not begun.

---

## 0. Progress — which documents are done, and where this stops

The population's order is the artifact's:
`tools/audit/l0_l1_outgoing_population.json` → `the_population_in_comparison_order`.

| # | Document | State |
|---|---|---|
| 1 | `ARCHITECTURE.md` — the Layer 1 section | **DONE** |
| 2 | `ARCHITECTURE.md` — the Layer 2 section | **DONE** |
| 3 | `cowork_layer1_note_model_design.md` | **DONE** |
| 4 | `cowork_layer1_tone_collection_design.md` | **DONE** |
| 5 | `cowork_layer1_extend_design.md` | **DONE** |
| 6–29 | the remainder of the population, in the artifact's order | **UNTOUCHED** |

**UNTOUCHED means untouched, not partly worked.** Nothing in documents 6–29 has been read for
tabulation, quoted, counted or dispositioned, and no row for any of them exists anywhere. The next
dispatch resumes at **position 6**, `cowork_layer2_slicing_design.md`.

**The sections that can only be written once every document is done are therefore NOT written**, and
their absence is deliberate rather than an omission: the derived-side rows (one per S-1…S-54 with the
arithmetic check), the distribution of dispositions, and the transfer/audit-question/proposal
gathers over the whole population. What each of those sections will contain is stated where it
belongs below, marked **NOT YET WRITTEN**, so that no reader mistakes a missing section for an empty
one. The per-document gathers for the documents that ARE done are present.

---

## 1. The words used here, explained before they are used

- **The analysis** — the harmonic-analysis software this project builds: given a notated score it
  decides the tonality, the chords, and the moments at which one chord gives way to the next.
- **The derivation** — `cowork_blind_derivation_l0_l1_2026_08_31.md`: 54 statements and 17 open
  questions written by an implementation-blind session that read a brief, a ten-member boot pack,
  four staged scores and fetched research sources, and nothing else of this project. Its statements
  are cited **S-1** to **S-54**, its open questions **OQ-1** to **OQ-17**.
- **L0** — in the ratified charter's own words, *"The notated record. NOT A LAYER; the input
  contract."* Its subject: what a notated record must supply, what may be assumed of it, and what
  happens when a real score does not supply it.
- **L1** — in the charter's own words, *"Change points, candidates and notated evidence."* Its
  question: at which moments **may** a harmony begin, and what does the notation say at each? It
  decides nothing about the music.
- **The outgoing text** — the current specifications describing what the new L0 and L1 charters now
  cover. Under the ruled phase definition the outgoing text is a **witness**: evidence about the
  present text, read after the derivation, and **never authority over a derived statement**. A
  disagreement between the two is recorded here and resolved nowhere.
- **The outgoing population** — the set of outgoing documents this comparison covers, fixed by
  Ruling 32 and cut by Ruling 33, and derived at
  `tools/audit/l0_l1_outgoing_population.json` → `the_population_in_comparison_order`. §3 below.
- **The residue** — the files the population tool's term search HIT that are **outside** the ruled
  specification document set. They are published on that artifact, dispositioned by nobody here, and
  left to the mining map. Nothing in this file touches one.
- **An outgoing statement** — one sentence or one bullet of an outgoing text that states what the
  analysis does, must do, may assume, or must not do, about L0's subject or L1's subject. A sentence
  that is none of those — narrative, provenance, a build state's commit identifier, a test count, a
  pointer to another document — is **not** an outgoing statement, and is listed once per document
  under *not a statement* so completeness can be checked by arithmetic at the document. **A
  paragraph is never a unit.** Where one sentence carries two claims it is two statements, quoted
  with the same sentence and marked (i) and (ii).
- **A disposition** — one of the five fates the phase definition names for an outgoing statement.
  §5 states them and states that the set is closed.
- **The transfer list** — the parking list for content that belongs to another charter, so that
  nothing is silently dropped and nothing is absorbed into the wrong charter.
- **Slice, change point, onset, release** — used throughout in the derivation's and the charter's
  shared sense: a **change point** is a moment that is the onset or the release of at least one
  eligible note; a **slice** is the stretch between two consecutive change points.

**On reserved words, because this file is read beside a music-analysis specification.** Bare *score*
is the music; bare *key* is tonality; bare *bar* is the metric unit and the prohibiting sense is
written *exclude*; bare *note* is a pitch event; bare *tie* is the notated tie; *measurement tool* or
*script* is written where the collided word would be wrong. **No numeric grade appears anywhere in
this file**: the vocabulary of §5 is the whole of the verdict language.

## 2. The subject, re-explained from scratch

A harmonic analysis of a written score cannot begin until two questions are answered, and they are
answered before any chord or tonality is named.

**The first is what the analysis is handed.** A score on paper carries a great many things: notes
with their spellings and durations, rests, bar lines, a time signature, a key signature, ties,
fermatas, repeat signs, pedal markings — and also things that are not the music but somebody's
reading of it, such as a chord symbol written above the staff. Something has to say which of those
the analysis may take as **given**, and what it may assume about them. That is L0, and it is a
contract rather than a computation: a list of facts, and a test for admitting a fact to the list.

**The second is where a harmony is even allowed to begin.** Music does not announce its own harmonic
boundaries, but the notation does say exactly when the set of sounding notes changes — a note starts,
a note stops. Every such moment is a **change point**, and the stretches between consecutive change
points are **slices**. Taking every one of them, rather than a grid of beats, is what makes it
impossible to miss a real harmony change. Beside those moments the notation says other things a later
layer will want to weigh: how strong the beat is, whether a bar line or a fermata or a rest falls
there, and whether the bass has just moved in the way a cadence moves. L1 finds those moments and
publishes what the notation says at each — and **decides nothing about the music**.

**The question this file answers is neither of those.** An implementation-blind session was asked
both questions and answered them without reading this project's specifications or its code. This file
sets that answer beside the specifications the project already has, and gives **every statement of
those specifications** exactly one recorded fate. It settles nothing: it tabulates, so that the user
can settle it.

## 3. The population, and where it comes from

The population is **derived, not chosen here**. It is
`tools/audit/l0_l1_outgoing_population.json` → `the_population_in_comparison_order`, written by
`tools/audit/gen_l0_l1_outgoing_population.py`, and it has two limbs:

- **Ruling 32's eleven named members** — two `ARCHITECTURE.md` sections (Layer 1 and Layer 2), the
  five root design documents those sections delegate to or cite, and the four places the ruling
  established by reading where the current text describes an output the new L1 charter publishes (the
  Layer 5 section and its delegated contract, the phrase-boundary design, and the factorization's
  beat-strength, fermata and cadence factors). Each is proven present at its path on every run, and
  the three `ARCHITECTURE.md` sections are located **by heading text and never by line number**
  (**D-307**).
- **Ruling 33's cut** — every further file the tool's term search admits **that is also a member of
  the ruled specification document set** (`tools/audit/specification_document_set.json` →
  `the_document_set`, path equality, exact). Every other hit file is published on the same artifact as
  the **residue**, and is not dispositioned here.

**No count from that artifact is restated in this file** (#17f, **D-431**) except this file's own row
arithmetic, which is counted at these rows. The comparison is worked in the artifact's order, and
each document below opens with its own manifest header.

**The reach of the search is UNMEASURED and the artifact says so.** The term list is authored, so a
passage about L0's or L1's subject that uses none of those words is not found. Nothing else
independently enumerates "passages of the current text about L0's or L1's subject", so there is no
population to reconcile against and the hit set is published as a **lower bound, never a census**.
What bounds the exposure is that the eleven named members are in the population **by name** regardless
of the search.

## 4. The unit, fixed before the tabulation begins

An **outgoing statement** is one sentence or one bullet that states what the analysis does, must do,
may assume, or must not do, about:

- **L0's subject** — what the notated record supplies, what may be assumed of it, and what happens
  when a real score does not supply it; or
- **L1's subject** — the brief's seven faces: (a) what counts as a note event, (b) what a tie does,
  (c) the change-point set and the slices, (d) metric strength, (e) the notated boundary evidence,
  (f) the local cadence cues, (g) the form of what is published and the bar on deciding.

Everything else in a document is listed once, per document, under **not a statement**, with its kind
named, so that the arithmetic at the foot of each document closes.

## 5. The vocabulary, and that it is CLOSED

Two axes, both closed, both fixed before any grading began. **No other verdict word appears in this
file, and no numeric grade appears anywhere in it.**

**The CURRENT-TEXT AXIS — one per named derived statement, per row.** This axis is evidence about the
present text and is **never a verdict on the derivation**:

- **AGREES** — the derived statement and the outgoing statement say the same thing in substance.
- **DIFFERS** — they say different things. The row then states the difference in one sentence, in
  both texts' own words, **and chooses nothing between them.**
- **THE DERIVATION IS SILENT** — no derived statement speaks to this outgoing statement.

**The DISPOSITION AXIS — exactly one per outgoing statement**, out of the five the phase definition
names, plus the honest default:

- **ADOPTED — carried** — a derived statement already carries this content in substance (named by
  its S-number).
- **ADOPTED — proposed** — no derived statement carries it; it is not implementation-describing, not
  another charter's, not historical, and the worth test does not discard it. **This is a PROPOSAL to
  the user that the outgoing content be added to the derived specification.** The proposal is written
  in one sentence beside the row. It is never written into the derivation.
- **RELOCATED** — its content belongs to another charter. The row names that charter in
  `FRAMEWORK.md` §5's own words, and the statement is appended to the TRANSFER LIST.
- **QUARANTINED** — it states how the implementation currently works, or a measured property of it.
  The row writes the audit question in one sentence.
- **DISCARDED** — under principle #10's worth test, with the finding, the date and the reason in the
  row — all three, or the disposition does not reach the row.
- **HISTORICAL** — it records an event, a build state, a superseded plan, or a status; not a rule.
- **UNPLACED** — this session cannot defend one disposition in one sentence at the two texts. The
  row then says what was read. **This is the honest default and it is NOT a sixth disposition** — it
  is a row the user places.

The charters, named in `FRAMEWORK.md` §5's own words wherever a row relocates to one: **L0 — the
notated record, NOT A LAYER; the input contract**; **L1 — change points, candidates and notated
evidence**; **L2 — the tonal reading, the one entangled decision**; **L3 — the read-off facts**;
**the second axis — voice leading**; and **the measurement of the analysis**, which that section
names explicitly as NOT A LAYER.

**The caveat the pilot carried has NO counterpart here, and that is established rather than assumed.**
The pilot's tabulation was bound by a withheld-family caveat (its D-450/D-575 rows). For this subject
the withheld family is **EMPTY BY RULING** — `tools/audit/derivation_boot_pack.json` → `subjects` →
`l0-l1` records no withheld identities, no withheld documents and no withheld passages — so no row
below applies such a caveat, and none is owed one.

---

## 6. The tabulation, in the population's order

### 6.1 — Document 1: `ARCHITECTURE.md`, the section *"#### Layer 1 — the lossless note model"*

> **Manifest for this document.** Outgoing statements: **35** (rows 1.1 to 1.29; six of those rows
> carry two claims each and are split (i)/(ii), so 29 rows carry 35 statements — the arithmetic is at
> the foot of this document). Listed under *not a statement*: **7**. Counted at this document by this
> session; the count appears here and nowhere else.
>
> **Why this document is in the population:** named by Ruling 32 item 1. It is the current
> specification of the layer that supplies what sounds — L0's subject — and it is the first position
> of the population's order.
>
> **How the section is bounded:** by heading text, from `#### Layer 1 — the lossless note model` to
> the next `#### ` heading (`#### Layer 2 — the deterministic change-point slicer`), exactly as the
> population artifact locates it (**D-307**). Line numbers below are locators beside the heading,
> never the anchor.

---

**Row 1.1 — the note model is the lossless, tie-resolved single source of what sounds.**

*Outgoing statement.* "**The lossless, tie-resolved NOTE MODEL — the single source of truth for
'what sounds.'**" — the module table, first cell (locator: line 1575).

*Derived statements that speak to it.* S-3 (what L0 supplies per note), S-23 (a tied group is one
event), S-18 (ineligible notes are carried, not dropped).

*Current-text axis.* S-3: **AGREES**. S-23: **AGREES**. S-18: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried.** S-3 carries the per-note fact surface, S-23 carries
tie resolution, and S-18 carries the losslessness of the excluded notes; the outgoing statement adds
no content beyond the three.

---

**Row 1.2 — the score is read once into a queryable set.**

*Outgoing statement.* "`NoteModel::build(score)` reads the score **once** into an annotated,
tick-range-queryable set of sounding notes." — the module table (locator: line 1575).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT** — the derivation states what L0 supplies, never how
often a reader walks the file or what query surface it offers.

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does the note model in fact read the score
exactly once, and is the queryable surface it builds the one the change-point construction consumes?

---

**Row 1.3 — the eleven per-note fields.**

*Outgoing statement.* "Each `NoteEvent` carries 11 fields: `pitch, tpc, staff, voice, onset, release,
duration, isGrace, plays, visible, staffEligible`." — the module table (locator: line 1575).

*Derived statements that speak to it.* S-3.

*Current-text axis.* S-3: **DIFFERS**.

*The difference, in both texts' own words.* S-3 requires L0 to supply, per note, *"whether it is
pitched"*, *"whether it is tied to the preceding note and to the following note"*, *"whether it is
cue-sized"*, *"the ornament and articulation signs attached to it"*, and a metric position given as
*"(bar index, offset within the bar, absolute position)"*; the outgoing eleven fields carry none of
those five and carry instead `staffEligible`, which S-3 does not name.

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* the eleven fields are the as-built record's
own list — do the five facts S-3 requires and this list does not carry reach any consumer, and does
`staffEligible` belong to L0's supplied facts or to an eligibility decision above it?

---

**Row 1.4 (i) — a tied group is one span with one onset.**

*Outgoing statement.* "Tied groups are merged into **one** span/onset" — the module table (locator:
line 1575).

*Derived statements that speak to it.* S-23.

*Current-text axis.* S-23: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-23: *"A group of notes joined by ties is one event.
Its onset is the first note's onset; its release is the last note's release."*).

---

**Row 1.4 (ii) — the merge is performed through named engraving calls.**

*Outgoing statement.* "(via the DOM `firstTiedNote`/`lastTiedNote`/`playTicksFraction`)" — the same
sentence (locator: line 1575).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT** — S-23's premise is only that *"the record links
tied notes explicitly"*, and it names no mechanism.

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* do the three named engraving calls
implement S-24's tie test — same spelled pitch, same notated voice, adjacent with no event between —
or do they merge links S-24 would refuse?

---

**Row 1.5 (i) — spans are half-open.**

*Outgoing statement.* "spans are true `[onset,release)`" — the module table (locator: line 1575).

*Derived statements that speak to it.* S-29.

*Current-text axis.* S-29: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-29 derives the half-open convention and calls it
*"not a choice but a consequence of what onset and release mean"*).

---

**Row 1.5 (ii) — the span query has no backward horizon.**

*Outgoing statement.* "answered by **overlap with no horizon** (the old 4-whole-note backward cap is
gone)." — the module table (locator: line 1575).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT** — the derivation never contemplates a bounded
backward search, so it neither states nor excludes one.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that L0 state explicitly that what
sounds at a moment is answered with **no backward horizon**, because a bounded backward search
silently drops a note held longer than the bound — a rule the derivation's own S-29 sounding-set
definition assumes and never writes down.

---

**Row 1.6 (i) — excluded notes are kept and flagged, never dropped.**

*Outgoing statement.* "Grace / non-playing / invisible / staff-ineligible notes are **kept and
flagged, never dropped**." — the module table (locator: line 1575).

*Derived statements that speak to it.* S-16 (grace notes published as ornamental attachments), S-18
(not-played and invisible notes carried as *silent notes*, labelled by which flag excluded them).

*Current-text axis.* S-16: **AGREES**. S-18: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-16 and S-18 together).

---

**Row 1.6 (ii) — a note may be excluded because of the staff it sits on.**

*Outgoing statement.* the category "staff-ineligible" in the same sentence (locator: line 1575).

*Derived statements that speak to it.* S-15 (the five eligibility conditions), S-20 (unpitched notes),
S-2 (annotation carried beside L0).

*Current-text axis.* S-15: **DIFFERS**.

*The difference, in both texts' own words.* S-15 makes eligibility a **per-note** test — *"pitched …
not marked as not to be played … visible … not a grace note … notated duration greater than zero"* —
and names no staff-level fact at all; the outgoing text excludes a note because its **staff** is
ineligible, a category its own delegated contract fills with hidden staves, percussion staves and the
chord-symbol track.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that L0 supply a per-staff
analysis-eligibility fact, since the derivation reaches percussion through S-20 and the chord-symbol
track through S-2 but reaches a **hidden staff** through neither, so a note on a hidden staff is
eligible under S-15 as it stands.

---

**Row 1.7 — the tie-unresolved atoms are republished, each with its own notated span.**

*Outgoing statement.* "`notatedNotes()` republishes the tie-UNRESOLVED atoms — EVERY notated note
incl. tie continuations, each with its OWN notated span, a `tieContinuation` flag, a `hasFermata`
flag, and `resolvedIndex` linking to its tie-resolved `NoteEvent` — the facts the tie-resolved
surface discards that the joint module's event lattice + emission covariates need." — the module
table (locator: line 1575).

*Derived statements that speak to it.* S-23.

*Current-text axis.* S-23: **DIFFERS**.

*The difference, in both texts' own words.* S-23 states that in a tied group *"Only the first note
opens an onset change point; only the last note opens a release change point; the intermediate notes
open nothing"*; the outgoing text republishes every notated note including tie continuations *"each
with its OWN notated span"*, and names the consumer of that surface as the event lattice — so a
notated tie boundary carries an onset and a release there.

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does the event lattice built from
`notatedNotes()` place a change point at a notated tie boundary, which S-23 says is not one — and if
so, may a harmonic boundary be committed there?

---

**Row 1.8 — the republication is additive and moves nothing.**

*Outgoing statement.* "Purely additive: `notes()` and every existing consumer are byte-identical." —
the module table (locator: line 1575).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the additive surface still
byte-identical on `notes()` at the current commit, and is that property tested rather than asserted?

---

**Row 1.9 — the weighted pitch-class view.**

*Outgoing statement.* "`weightedPcView(noteModel, range, …)` — the recomputed `collectRegionTones`
weighting (duration×beat, repetition, cross-voice, pedal, PC aggregation, bass pick), now counting
**one onset per tied group** (tie **de-inflation**) and finding sustains by overlap." — *Derived views
over the model* (locator: line 1579).

*Derived statements that speak to it.* S-33 (slice identity is the event set, not the pitch-class
set), S-44 (the bass is the lowest sounding pitch of the slice's sounding set), S-49 (L1 publishes the
interval content and names no chord).

*Current-text axis.* S-33: **DIFFERS**. S-44: **DIFFERS**. S-49: **DIFFERS**.

*The difference, in both texts' own words.* S-33 fixes that *"Slice identity is the set of events (by
note identity), not the set of pitch classes and not the set of pitches"* and S-44 defines the bass as
*"the lowest sounding pitch of that slice's sounding set"* with no weighting; the outgoing view
aggregates by pitch class and picks a bass through a weighting stack (*"duration×beat, repetition,
cross-voice, pedal, PC aggregation, bass pick"*).

*PROPOSED DISPOSITION.* **RELOCATED — to L2, *the tonal reading, the one entangled decision*.**
Weighting sounding notes into evidence for a reading is scoring, and L1 *"decides nothing about the
music"*; the tie-de-inflation half of the sentence is already carried by S-23 and travels with the
relocation rather than being lost.

---

**Row 1.10 — the old collectors survive as wrappers.**

*Outgoing statement.* "`collectRegionTones`/`collectSoundingAt` are retained as thin **build-once
Score wrappers**." — *Derived views over the model* (locator: line 1582).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* are both wrappers still live at the current
commit, and does either re-read the score rather than the note model?

---

**Row 1.11 — the point-in-time view and its adapters.**

*Outgoing statement.* "`soundingAt(noteModel, tick, …)` — the point-in-time per-note view (replaces
`collectSoundingAt`'s reading half); `buildTones` is now a trivial adapter; `findTemporalContext`
takes the model." — *Derived views over the model* (locator: line 1583).

*Derived statements that speak to it.* S-29 (the sounding set of a slice).

*Current-text axis.* S-29: **THE DERIVATION IS SILENT** on a point-in-time view — S-29 defines the
sounding set of a **slice**, not of an instant.

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does the point-in-time view answer at an
instant what S-29 answers over a slice — in particular, is a note whose release equals the queried
tick included, which S-29 excludes?

---

**Row 1.12 — the segment-first spine still runs and drives all analysis.**

*Outgoing statement.* "The segment-first analysis spine described below (`greedyExpandSegmentation`,
the Pass-1/2/2b sub/merge machinery, `analyzeHarmonicRhythm`) **still runs and still drives all
analysis** — it now consumes `weightedPcView` (unchanged weighting) instead of reading notes
directly." — *Transitional, by design* (locator: line 1586).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **HISTORICAL** — a build state. *(Whether it is a true build state at the
current commit is the audit's business and no verdict on it is taken here.)*

---

**Row 1.13 — the spine retires when Layers 2 and 3 are built.**

*Outgoing statement.* "It retires only when **layer 2** (change-point slicing) and **layer 3**
(per-slice analysis) are built." — *Transitional, by design* (locator: line 1589).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **HISTORICAL** — a superseded plan (the layer numbering it names is the old
four-layer target, not the ratified L0–L3 charter).

---

**Row 1.14 — note-reading ownership has moved; slicing and scoring are frozen.**

*Outgoing statement.* "The note-reading *ownership* has moved to the note model; the slicing/scoring
*logic* is frozen until its layers." — *Transitional, by design* (locator: line 1590).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **HISTORICAL** — a build state.

---

**Row 1.15 — the measured movement the layer caused.**

*Outgoing statement.* "Layer 1 is a **behavior change**, not byte-identical: the faithful tie
de-inflation moved the per-event oracle-root metric **+3/+1/+1 charged** (Baroque/Jazz/Default), with
the KEY tier flat, FLOOR byte-flat, and BIR **−2/+1/−2** (mostly improved)." — *Ratified trade-off on
record* (locator: line 1593).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* are these figures reproducible at the
current commit on the arm that ships, and is the measurement they were taken on the one the record
now governs?

---

**Row 1.16 — the movement is an upstream correction, not a regression.**

*Outgoing statement.* "This is a correct-**upstream** / frozen-**downstream** wobble … it re-tunes at
layer 3 and is **not** an unexplained regression (proven: a legacy reproduction mode reproduced the
prior oracle set byte-exactly)." — *Ratified trade-off on record* (locator: line 1596).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does the legacy reproduction mode still
exist and still reproduce the prior set, which is what the "not a regression" claim rests on?

---

**Row 1.17 — the next step is Layer 3.**

*Outgoing statement.* "**Next: layer 3 (per-slice analysis).**" — *Ratified trade-off on record*
(locator: line 1599).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **HISTORICAL** — a plan, superseded by the ratified charter's sequencing.

---

**Row 1.18 — the finest meaningful extension step is the change point.**

*Outgoing statement.* "When a consumer asks this model to reach further into the score, the smallest
request worth making is one that reaches the next change-point." — the D-628 block (locator: line
1604).

*Derived statements that speak to it.* S-28 (change points are exact positions), S-29 (the sounding
set is constant across a slice), S-53 (the working span is the only thing a caller supplies beyond
L0).

*Current-text axis.* S-28: **THE DERIVATION IS SILENT**. S-29: **THE DERIVATION IS SILENT**. S-53:
**THE DERIVATION IS SILENT** — S-53 fixes what a caller supplies, never the granularity at which a
caller may enlarge it.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the L0/L1 specification state
that the finest meaningful enlargement of the working span is one reaching the next change point,
because within a slice the eligible sounding-note set is constant, so a smaller request loads no note.

---

**Row 1.19 — the reason: a request ending inside a slice is provably a no-op.**

*Outgoing statement.* "it follows from what a Layer-2 slice **is** — the stretch over which the
eligible sounding-note set is constant — so a request that ends inside a slice is *provably* a no-op
rather than merely a small one: no note enters the model and no downstream answer can differ." — the
D-628 block (locator: line 1605).

*Derived statements that speak to it.* S-29.

*Current-text axis.* S-29: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-29 defines the sounding set of a slice, which is the
whole of this sentence's ground).

---

**Row 1.20 — the bound is a fact about the representation, not a tuning choice.**

*Outgoing statement.* "That makes the granularity bound a **fact about the representation**, not a
tuning choice, and it is what bounds the step-size question the requesting layer owns." — the D-628
block (locator: line 1608).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 1.18. *The proposal:* that the
specification record the granularity bound as a consequence of the slice definition rather than as a
settable value, so that no later fit can treat it as one.

---

**Row 1.21 — polyphonic phrase-boundary detection has no validated rule set, and ours may not be
presented as established method.**

*Outgoing statement.* "Polyphonic phrase-boundary detection has NO validated deterministic rule set in
the literature — the L1.5 primitive is our own engineering and may not be presented as established
method." — the D-607 block (locator: line 1612).

*Derived statements that speak to it.* S-39 (the boundary flags L1 publishes), S-50 (the naming bar).

*Current-text axis.* S-39: **THE DERIVATION IS SILENT** — S-39 publishes notated boundary **evidence**
and detects no phrase. S-50: **AGREES** on the underlying discipline, in that S-50 excludes any
published field named *boundary*, *cadence* or *phrase*.

*PROPOSED DISPOSITION.* **RELOCATED — to L3, *the read-off facts*.** `FRAMEWORK.md` §5 assigns *"the
phrase and section grouping"* to L3 and keeps only the notated phrase evidence at L1, and this
statement is about detecting phrases rather than about publishing the evidence.

---

**Row 1.22 — the published work is monophonic.**

*Outgoing statement.* "Almost all published work on locating phrase endings addresses a single melodic
line; for several simultaneous voices nothing comparable has been established." — the D-607 block
(locator: line 1614).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **RELOCATED — to L3, *the read-off facts*** (with Row 1.21; it is that
statement's ground).

---

**Row 1.23 (i) — carrying monophonic cues to polyphony is our own engineering.**

*Outgoing statement.* "Carrying the monophonic cues over to polyphony is therefore engineering of
ours" — the D-607 block (locator: line 1616).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **RELOCATED — to L3, *the read-off facts*.**

---

**Row 1.23 (ii) — it is validated against our own corpus rather than cited.**

*Outgoing statement.* "and it is validated against our own annotated corpus rather than cited." — the
same sentence (locator: line 1617).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **RELOCATED — to *the measurement of the analysis*,** which `FRAMEWORK.md` §5
names explicitly as NOT A LAYER: *"Metric definitions, grading conventions and what counts as ground
truth are the measurement layer's own design content and a later stage's business."*

---

**Row 1.24 (i) — the gap cue generalizes to polyphony.**

*Outgoing statement.* "the **gap cue** generalizes cleanly, because a phrase boundary in polyphony is
a near-simultaneous rest or long note across all voices" — the D-607 block (locator: line 1620).

*Derived statements that speak to it.* S-39 (the REST-BEGINS and ALL-SILENT flags).

*Current-text axis.* S-39: **AGREES** in substance — S-39 publishes both *"REST-BEGINS (a notated
voice's silence begins at this change point, by rest or by unwritten gap, naming the voice)"* and
*"ALL-SILENT (the slice starting here is a silent slice)"*, which is the per-voice and
across-all-voices form of the same cue.

*PROPOSED DISPOSITION.* **RELOCATED — to L3, *the read-off facts*** — the cue's use in **detecting**
a phrase is L3's; the evidence it reads is already L1's at S-39, so nothing of the evidence half is
lost by the relocation.

---

**Row 1.24 (ii) — a figure measured only on chorales is to be distrusted.**

*Outgoing statement.* "which is what makes chorale texture an unusually favourable case and is a
reason to distrust a figure measured only there." — the same sentence (locator: line 1622).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **RELOCATED — to *the measurement of the analysis*** (the same NOT-A-LAYER
target as Row 1.23 (ii)).

---

**Row 1.25 — voice slots and stem direction are notational metadata, so this layer may read them.**

*Outgoing statement.* "**VOICE SLOTS AND STEM DIRECTION ARE STRUCTURAL NOTATIONAL METADATA, NOT
USER-WRITTEN ANALYTICAL CLAIMS — SO THIS LAYER MAY READ THEM**" — the 2026-08-08 block (locator: line
1626).

*Derived statements that speak to it.* S-3 (staff and notated voice are supplied), S-13 (notated
voices only), S-7 (what L0 does **not** supply), S-1 (the admission criterion).

*Current-text axis.* S-3: **AGREES** on the voice slot. S-13: **AGREES** on the voice slot. S-1:
**AGREES** on the test. S-7: **DIFFERS** on stem direction.

*The difference, in both texts' own words.* S-7 states that *"L0 does not supply tempo, dynamics,
slurs, beams, stem directions, or layout"*, defending the exclusion on the ground that *"nothing in §3
consumes them; they are excluded to keep the contract minimal"*; the outgoing statement states that
stem direction is structural notational metadata and that **the analysis may consume it**.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that L0's supplied list gain stem
direction, by the route S-7 itself provides — *"a later layer that needs one adds it by the same
test"* — since S-1's criterion admits it (two copyists agree on a stem direction and it asserts no
harmony). The voice-slot half is already carried by S-3 and S-13 and needs no addition.

---

**Row 1.26 — they are the same category as the key signature, the time signature, a tie and a pedal
mark.**

*Outgoing statement.* "Which voice a note was entered in, and which way its stem points, belong to how
the music was written down — the same category as the key signature, the time signature, a tie or a
pedal marking, all of which this layer already reads." — the 2026-08-08 block (locator: line 1628).

*Derived statements that speak to it.* S-6 (time signature and key signature supplied), S-7 (fermatas,
pedal marks supplied), S-3 (ties supplied per note).

*Current-text axis.* S-6: **AGREES**. S-7: **AGREES**. S-3: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-3, S-6 and S-7 together supply all four of the named
comparators).

---

**Row 1.27 (i) — they are not a claim about the harmony.**

*Outgoing statement.* "They are not somebody's claim about the harmony." — the 2026-08-08 block
(locator: line 1631).

*Derived statements that speak to it.* S-1.

*Current-text axis.* S-1: **AGREES** — S-1's condition (ii) excludes a fact that is *"a claim about
what the music means"*, and neither field is one.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-1).

---

**Row 1.27 (ii) — the analysis may therefore consume them.**

*Outgoing statement.* "**The analysis may therefore consume them.**" — the 2026-08-08 block (locator:
line 1631).

*Derived statements that speak to it.* S-7, S-9 (what L1 reads from L0).

*Current-text axis.* S-7: **DIFFERS** (as at Row 1.25). S-9: **DIFFERS** — S-9 states that *"L1 reads
from L0 everything of S-3 to S-7 except the key signature"*, and stem direction is in none of S-3 to
S-7.

*The difference, in both texts' own words.* S-9 bounds what L1 may read to the S-3-to-S-7 list minus
the key signature; the outgoing statement licenses consumption of a field that list excludes.

*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 1.25.

---

**Row 1.28 — the line is the chord-symbol prohibition's, applied to a new pair of fields.**

*Outgoing statement.* "it is the line the chord-symbol prohibition already draws, applied to a new pair
of fields — the analysis may read what the score IS and may not read what a user has CLAIMED about it
— and voice slot and stem direction fall on the first side." — the 2026-08-08 block (locator: line
1631).

*Derived statements that speak to it.* S-1, S-2, S-8.

*Current-text axis.* S-1: **AGREES**. S-2: **AGREES**. S-8: **AGREES** — all three draw exactly this
line, S-2 for a written chord symbol and S-8 for a composer's own figures.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-1 with S-2 and S-8).

---

**Row 1.29 — the rule binds any voice-tracking work and settles nothing about whether the detector is
built.**

*Outgoing statement.* "The rule binds any voice-tracking work whether or not the non-chord-tone
detector that raised the question is ever built; it decides what such a detector would be ALLOWED to
read and settles nothing about whether it is built, which is a separate deferral recorded at the chord
layer." — the 2026-08-08 block (locator: line 1634).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 1.25 as its reach clause: that the
reading permission be stated as binding on any consumer, independently of whether any particular
consumer is built.

---

#### Not a statement — listed so the arithmetic closes (7)

1. "The analysis pipeline is being rebuilt **upstream-first** onto the ratified 4-layer target
   (`cowork_target_architecture.md`): **note model (L1, DONE) → change-point slicing (L2, BUILT —
   wired, consumed by L3) → per-slice analysis with context (L3) → grouping for display (LN).**" —
   *narrative and build state*, and a pointer to another document. *(Its build-state content is
   carried by Rows 1.12 to 1.14; it is not counted twice.)*
2. "Layer 1 is built and ratified (commits `edd33901ed` …, `e30bb45a4f` …, `4055f89082` …; pushed to
   the fork). Layer 2 is built as a fully-covered module (below) and is now **wired — L3 consumes the
   slicer** (`regionanalyzer.cpp:579`)." — *provenance*: commit identifiers and a code locator.
3. The Layer-1 **delegation pointer** paragraph naming `cowork_layer1_note_model_design.md` — *a
   pointer to another document*, which that document's own row set will cover at population position
   3.
4. The **Layer-1.5 delegation pointer** paragraph naming `cowork_phrase_boundary_design.md`, together
   with its parenthetical siting argument — *a pointer and a filing decision*; the document it names
   is population position 10.
5. "See `cc_layer1_impl_report.md` / `cc_layer1_coverage_report.md` (HELD)." — *a pointer*.
6. The three re-homing provenance marks — "(D-628; re-homed into this specification 2026-08-04 from
   the design document that formerly carried it — the register records which)", "(D-607; re-homed …
   2026-08-04 …)", "(re-homed into this specification 2026-08-08 on the user's ruling)" — *provenance*.
7. The module table's header row, "| Module | Responsibility |" — *not prose*.

#### The arithmetic at this document

- Rows written: **29** (1.1 to 1.29).
- Of those, rows split into two claims and counted as two statements each: **1.4, 1.5, 1.6, 1.23,
  1.24, 1.27** — six rows, so **+6**.
- **Outgoing statements dispositioned: 35.**
- Listed under *not a statement*: **7**.
- **Every outgoing statement carries exactly one disposition, and none carries two.** Checked by
  reading the disposition line of each row: 35 disposition lines over 35 statements, no row without
  one and no row with a second.
- **UNPLACED rows at this document: 0.**

#### The distribution at this document, counted at these rows

| Disposition | Count | Statements |
|---|---|---|
| ADOPTED — carried | 8 | 1.1, 1.4(i), 1.5(i), 1.6(i), 1.19, 1.26, 1.27(i), 1.28 |
| ADOPTED — proposed | 7 | 1.5(ii), 1.6(ii), 1.18, 1.20, 1.25, 1.27(ii), 1.29 |
| RELOCATED | 7 | 1.9, 1.21, 1.22, 1.23(i), 1.23(ii), 1.24(i), 1.24(ii) |
| QUARANTINED | 9 | 1.2, 1.3, 1.4(ii), 1.7, 1.8, 1.10, 1.11, 1.15, 1.16 |
| DISCARDED | 0 | — |
| HISTORICAL | 4 | 1.12, 1.13, 1.14, 1.17 |
| UNPLACED | 0 | — |
| **Total** | **35** | — |

**The column sums to 35, against 35 statements, so the arithmetic closes at this document.** It is
stated as a sum rather than asserted: 8 + 7 + 7 + 9 + 0 + 4 + 0 = 35. **The statement lists in the
right-hand column are the record**, and the integers are re-derivable from them by counting.

#### The current-text axis at this document, counted at these rows

| Verdict | Count |
|---|---|
| AGREES | 20 |
| DIFFERS | 9 |
| THE DERIVATION IS SILENT | 22 |
| **Total verdicts** | **51** |

*(Counted per named derived statement per statement-row, so a row naming three derived statements
contributes three verdicts; a row naming none contributes one SILENT. 51 verdicts over 35 statements
because eleven rows name more than one derived statement.)*

#### What this document's rows put in front of the user, in one paragraph

Two rows carry a difference that is about a **rule** rather than about an implementation, and they
are the ones worth reading first. **Row 1.25 with 1.27(ii)** — the outgoing text licenses the analysis
to read **stem direction**, and the derivation's S-7 excludes it from what L0 supplies; the derivation
provides the route to add it, and the proposal takes that route rather than overriding either text.
**Row 1.6(ii)** — the outgoing text excludes a note because its **staff** is ineligible, and the
derivation's eligibility test S-15 is per-note only, so a note on a hidden staff is eligible as the
derivation stands. Beside those, **Row 1.7** is the sharpest QUARANTINED row: the tie-unresolved
republication gives every tie continuation its own onset and release, where S-23 says the intermediate
notes of a tied group open nothing — the same shape the pilot's comparison found at its own Row 1.

---

### 6.2 — Document 2: `ARCHITECTURE.md`, the section *"#### Layer 2 — the deterministic change-point slicer"*

> **Manifest for this document.** Outgoing statements: **28** (rows 2.1 to 2.28). Listed under *not a
> statement*: **5**. Counted at this document by this session; the count appears here and nowhere
> else.
>
> **Why this document is in the population:** named by Ruling 32 item 1. It is the current
> specification of change-point slicing — the centre of L1's subject, faces (a) and (c).
>
> **How the section is bounded:** by heading text, from `#### Layer 2 — the deterministic
> change-point slicer` to the next `#### ` heading (`#### Layer 3 — key/mode is the sequence
> decoder`), as the population artifact locates it (**D-307**).
>
> **★ This document carries the sharpest disagreement found so far**, at Row 2.16 — grace notes.

---

**Row 2.1 — the slicer's output is a fact, not a judgment.**

*Outgoing statement.* "A pure, deterministic FACT read off the layer-1 note model, **not** a
judgment." — the opening paragraph (locator: line 1640).

*Derived statements that speak to it.* S-50 (what L1 publishes and the naming bar), S-51 (the test for
whether an output is a claim), S-53 (nothing L1 publishes depends on L2).

*Current-text axis.* S-50: **AGREES**. S-51: **AGREES**. S-53: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-51 makes the same distinction mechanical: an output
is evidence rather than a claim when it is computable from L0 facts with no tonality, chord or
boundary as input).

---

**Row 2.2 — the slicer is wired into the live pipeline.**

*Outgoing statement.* "It **is** now wired into the live analysis pipeline: layer 3 consumes the
slicer (`regionanalyzer.cpp:579` → `KeyModeSequenceDecoder`)." — the opening paragraph (locator: line
1641).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **HISTORICAL** — a build state.

---

**Row 2.3 — the slicer's own output did not move; the consuming layer did.**

*Outgoing statement.* "The slicer's own output stays **byte-identical** on the whole-score live path
(the clip is inert there); the analysis movement came from **L3's consumption** of the slices, not
from the slicer." — the opening paragraph (locator: line 1643).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the clip still inert on the whole-score
path at the current commit, and is that tested rather than asserted?

---

**Row 2.4 — the layer enumerates the change-point slices from the note model.**

*Outgoing statement.* "**Enumerate the change-point slices of a score from the note model.**" — the
module table (locator: line 1648).

*Derived statements that speak to it.* S-28, S-29.

*Current-text axis.* S-28: **AGREES**. S-29: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried.**

---

**Row 2.5 — the slice list is ordered, covering, gapless and non-overlapping, and half-open.**

*Outgoing statement.* "`changePointSlices(noteModel)` returns an ordered, **covering, lossless** list
of half-open `[start,end)` spans that **tile the domain with no gaps and no overlaps**." — the module
table (locator: line 1648).

*Derived statements that speak to it.* S-29 (the half-open convention), S-31 (a silent slice is
published like any other), S-32 (the list covers the working span exactly).

*Current-text axis.* S-29: **AGREES**. S-31: **AGREES**. S-32: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (the charter's own *"ordered, covering, gapless and
non-overlapping"*, which S-29 derives the half-open form of).

---

**Row 2.6 — boundaries are the sorted-unique union of every onset and every release of the eligible
notes.**

*Outgoing statement.* "Boundaries = the sorted-unique union of every **onset AND every release** of
the **eligible** notes; consecutive boundaries form the slices." — the module table (locator: line
1648).

*Derived statements that speak to it.* S-28 (two positions are the same change point iff equal as
rationals, with no tolerance), S-15 (what makes a note eligible).

*Current-text axis.* S-28: **AGREES** — *sorted-unique* is exactly S-28's exact-equality merge with no
tolerance. S-15: **AGREES** on the construction, and the eligibility term itself is Row 2.8's subject.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-28 with the charter's own release clause).

---

**Row 2.7 — the enumeration's cost.**

*Outgoing statement.* "O(n log n)." — the module table (locator: line 1648).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT** — the derivation states no cost bound anywhere.

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the enumeration's measured cost the
stated bound on the largest scores the record requires to be handled?

---

**Row 2.8 — a note participates in boundary generation on three flags.**

*Outgoing statement.* "A note participates in boundary generation iff layer 1 flagged it `plays &&
visible && staffEligible`." — *Boundaries over layer-1's eligibility annotation* (locator: line 1651).

*Derived statements that speak to it.* S-15.

*Current-text axis.* S-15: **DIFFERS**.

*The difference, in both texts' own words.* S-15 admits a note as eligible *"if and only if it is
pitched, it is not marked as not to be played, it is visible, it is not a grace note, and its notated
duration is greater than zero"* — five conditions; the outgoing text tests **three** flags, of which
one (`staffEligible`) is not among S-15's, and omits *pitched*, *not a grace note* and *positive
duration*.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the eligibility predicate be
stated once, in one place, over the union of the two lists — S-15's five conditions together with the
staff-level fact Row 1.6(ii) already proposes — since the two texts currently test different
predicates under the same word.

---

**Row 2.9 — the slicer reads the flags and does not re-decide them.**

*Outgoing statement.* "The slicer **reads** those flags; it does not re-filter." —
*Boundaries over layer-1's eligibility annotation* (locator: line 1652).

*Derived statements that speak to it.* S-9 (what L1 reads from L0), S-15.

*Current-text axis.* S-9: **AGREES**. S-15: **AGREES** — S-15 builds eligibility from L0 facts and
re-derives none of them.

*PROPOSED DISPOSITION.* **ADOPTED — carried.**

---

**Row 2.10 — an ineligible note opens no boundary but rides along in the slice's overlapping set.**

*Outgoing statement.* "A muted / invisible / non-tonal-staff note opens **no** boundary, yet still
rides along in each slice's `overlapping()` set (passed through, not dropped)." — *Boundaries over
layer-1's eligibility annotation* (locator: line 1652).

*Derived statements that speak to it.* S-15 (an eligible note *"belongs to the sounding set of every
slice between"* its onset and release), S-18 (excluded notes are carried beside L1's output as
*silent notes*), S-20 (an unpitched note *"enters no sounding set … is not published by L1 at all"*).

*Current-text axis.* S-18: **AGREES** on carrying rather than dropping. S-15: **DIFFERS**. S-20:
**DIFFERS**.

*The difference, in both texts' own words.* S-15 puts only **eligible** events in a slice's sounding
set and S-18 carries the excluded ones **beside** L1's output, labelled by the flag that excluded
them, while S-20 says an unpitched note *"enters no sounding set"* at all; the outgoing text keeps the
ineligible note **inside** each slice's own overlapping set, *"passed through, not dropped"*.

*PROPOSED DISPOSITION.* **UNPLACED.** *What was read:* the two texts agree that nothing is dropped and
disagree about **where** the carried note lives — in the slice's own set, or beside the output — and
that is a difference about the published shape of L1's output rather than about a rule of analysis.
This session cannot defend calling it ADOPTED (the content is not carried: S-18's carrier is a
different structure), RELOCATED (it is L1's own output shape), or QUARANTINED (the sentence states a
rule about the output, not a property of the code) in one sentence at the two texts. **The user
places it.**

---

**Row 2.11 — a slice is constant *tonal* sonority; ineligible notes are passenger metadata.**

*Outgoing statement.* "A slice is therefore 'constant **tonal** sonority'; non-eligible notes are
passenger metadata." — *Boundaries over layer-1's eligibility annotation* (locator: line 1654).

*Derived statements that speak to it.* S-15, S-33.

*Current-text axis.* S-15: **AGREES** — the constancy is over the eligible set in both texts. S-33:
**AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-15 with S-33).

---

**Row 2.12 — slice identity is the eligible sounding-note set, not the pitch-class set.**

*Outgoing statement.* "**Slice identity is the eligible sounding-NOTE set** (not the octave-folded PC
set — a unison/octave shrink is a real boundary though the PC set is unchanged)." — *Boundaries over
layer-1's eligibility annotation* (locator: line 1655).

*Derived statements that speak to it.* S-33.

*Current-text axis.* S-33: **AGREES** — and the agreement is exact, both texts giving the unison or
octave shrink as the case that decides it.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-33, whose own source class is *given*: it quotes the
charter, and this sentence is the charter's other statement of the same rule).

---

**Row 2.13 — the tiled domain is the intersection of the eligible-notes span with the loaded span.**

*Outgoing statement.* "The tiled domain is the intersection of the eligible-notes span with the
model's **loaded span**: `[max(loadedStart, firstEligibleOnset), min(loadedEnd,
lastEligibleRelease))`." — *Covering / empty slices, clipped to the loaded span* (locator: line 1658).

*Derived statements that speak to it.* S-32.

*Current-text axis.* S-32: **DIFFERS**.

*The difference, in both texts' own words.* S-32 states that *"The published slice list covers the
working span exactly. Its first change point is the span's start; its last is the span's end"*, and
that where no eligible event begins at the span's start *"the first slice is a silent slice"*; the
outgoing text tiles the **intersection**, so a working span beginning in silence is tiled from the
first eligible onset instead of from the span's start.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the specification state which of
the two domains is published — the working span exactly, or its intersection with the sounding
material — since the two differ precisely over leading and trailing silence, and Row 2.15 is the same
question stated from the other side.

---

**Row 2.14 — every tick in the domain lands in exactly one slice.**

*Outgoing statement.* "Every tick in that domain lands in exactly one slice." — *Covering / empty
slices* (locator: line 1660).

*Derived statements that speak to it.* S-29, S-30 (no slice has zero length), S-31.

*Current-text axis.* S-29: **AGREES**. S-30: **AGREES**. S-31: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-29's half-open convention is what makes the
exactly-one property hold by construction, which S-29 states in terms).

---

**Row 2.15 — a sustained-in or sustained-out note is clipped to the loaded boundary.**

*Outgoing statement.* "A **sustained-in** note (onset `< loadedStart`) is clipped to start at
`loadedStart`, a **sustained-out** note (release `> loadedEnd`) to end at `loadedEnd` — slicing never
drags outside the loaded span." — *Covering / empty slices* (locator: line 1661).

*Derived statements that speak to it.* S-32.

*Current-text axis.* S-32: **DIFFERS**.

*The difference, in both texts' own words.* Both bound the slicing to the span; S-32 does it by
**keeping the event and marking it** — a slice *"whose sounding set consists of events that began
before the span (marked *entered sounding*)"*, and *"events that release after the span's end are
marked *cut by the span*"* — while the outgoing text does it by **clipping the note's span** and
publishes no such mark.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the *entered sounding* and *cut
by the span* marks S-32 requires be published beside the clipped slice list, so that a consumer can
tell a real onset at the span's start from an artefact of where the span begins.

---

**Row 2.16 — no note kind is special-cased, and a grace note opens and closes a boundary by its span.**

*Outgoing statement.* "**No special-casing of any note kind** — grace and tuplet outcomes fall out of
the note-model spans as facts (verified at source: a grace event carries onset = parent-chord tick and
duration = `playTicksFraction()` = its nominal written value, so a grace genuinely opens/closes a
boundary by its span; tuplet ticks are the model's real, un-snapped ticks)." — *Zero interpretation*
(locator: line 1676).

*Derived statements that speak to it.* S-15, S-16, S-30.

*Current-text axis.* S-16: **DIFFERS**. S-15: **DIFFERS**. S-30: **DIFFERS**.

*The difference, in both texts' own words.* S-16 states flatly that *"A grace note opens no change
point and belongs to no sounding set"*, and S-15 makes *"it is not a grace note"* one of the five
eligibility conditions, on the ground that a grace note has no metric duration of its own so *"a
change point there would be a performance decision, which L1 may not take"*; the outgoing text states
that *"a grace genuinely opens/closes a boundary by its span"*, the span being the grace's nominal
written value at the parent chord's tick. S-30 adds that the derivation relies on graces having **no**
position in order to assert that no slice has zero length.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the specification state, once and
explicitly, whether a grace note opens a change point — the two texts give opposite answers, and the
answer decides both the change-point set and the no-zero-length-slice invariant. **This row is the
sharpest disagreement in the two documents tabulated so far, and it is put as a difference, not
settled here.**

---

**Row 2.17 — the slicer needs no grace or tuplet code.**

*Outgoing statement.* "The slicer needs no grace/tuplet code." — *Zero interpretation* (locator: line
1680).

*Derived statements that speak to it.* S-16.

*Current-text axis.* S-16: **DIFFERS** — S-16 requires a grace note to be excluded from the
change-point set and published instead as an *ornamental attachment* of its host, which is a rule
about graces that some code must implement.

*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 2.16 as its consequence.

---

**Row 2.18 — no thresholds, no merging, no notion of ornamental or passing.**

*Outgoing statement.* "No thresholds, min-gap, merge, or snapping; no notion of
'ornamental/passing/structural'." — *Zero interpretation* (locator: line 1675).

*Derived statements that speak to it.* S-28 (*"There is no tolerance"*), S-31 (a silent slice is not
merged into a neighbour), S-50 (the naming bar).

*Current-text axis.* S-28: **AGREES**. S-31: **AGREES**. S-50: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-28 with S-31).

---

**Row 2.19 — an interior all-rest span is an explicit empty slice, not a gap.**

*Outgoing statement.* "An interior span where all eligible voices rest is an **explicit EMPTY slice**
(empty eligible overlap set), not a gap — it falls out of the consecutive-boundary construction for
free." — *Covering / empty slices* (locator: line 1666).

*Derived statements that speak to it.* S-31.

*Current-text axis.* S-31: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-31: *"A silent slice … is published as a slice like
any other, with its empty set, and is not merged into a neighbour"*).

---

**Row 2.20 — leading and trailing silence inside the loaded span is not sliced.**

*Outgoing statement.* "Leading/trailing silence within the loaded span is not sliced; silence outside
the domain is not invented." — *Covering / empty slices* (locator: line 1668).

*Derived statements that speak to it.* S-32, S-31.

*Current-text axis.* S-32: **DIFFERS**. S-31: **DIFFERS**.

*The difference, in both texts' own words.* S-32 requires the list's first change point to be *"the
span's start"* and, where nothing begins there, a **silent first slice**; the outgoing text does not
slice leading or trailing silence at all.

*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 2.13 — it is the same question
seen from the silence side, and the proposal is the same: state which domain is published.

---

**Row 2.21 — re-slicing on extend is a re-call of the same pure function.**

*Outgoing statement.* "**Re-slice on extend** = re-call `changePointSlices` on the enlarged model (the
slicer is a pure function of (notes, loaded span)): interior real change-points are stable, the edge
slice abutting an *artificial* clip boundary extends into the new context, and the result equals a
fresh slice over the enlarged span (re-slice equivalence)." — *Covering / empty slices* (locator: line
1669).

*Derived statements that speak to it.* S-53 (L1 is computable in one forward pass, the working span
being the only thing a caller supplies beyond L0).

*Current-text axis.* S-53: **THE DERIVATION IS SILENT** on extension — S-53 fixes the span as the
caller's and never contemplates enlarging one.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the specification state the
re-slice equivalence property — that slicing after an enlargement equals slicing a span built at the
enlarged extent — since it is what makes an enlargement safe and the derivation states no equivalent.

---

**Row 2.22 — incremental re-slicing is deferred.**

*Outgoing statement.* "Incremental re-slice is Phase 2b (deferred, byte-identical)." — *Covering /
empty slices* (locator: line 1672).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **HISTORICAL** — a deferral, a status rather than a rule.

---

**Row 2.23 — boundaries are necessary but not sufficient; a real chord change can never be missed.**

*Outgoing statement.* "Boundaries are **necessary but not sufficient** for a chord change (the
exhaustive candidate grid): a real chord change can never be missed (over-grab is structurally
impossible), and the slicer never asserts a change — layer 3 decides which boundaries are real, layer
N groups equal analyses." — *Zero interpretation* (locator: line 1680).

*Derived statements that speak to it.* S-28, S-50, S-53.

*Current-text axis.* S-28: **AGREES** — S-28's ground for refusing a tolerance is exactly that *"A
tolerance would merge distinct moments and could delete a real candidate, which the charter's
construction exists to make impossible."* S-50: **AGREES**. S-53: **AGREES**.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-28 with S-53; the layer numbering in the sentence is
the old scheme and is a naming rather than a claim).

---

**Row 2.24 — the corpus and suite figures at the build.**

*Outgoing statement.* "composing 631/631, notation 53/53, snapshots 11/11 with no golden refresh;
corpus 0/353 `.ours.json` byte-diffs on Baroque/Jazz/Default, gate unchanged at 53/24/53" — *Fully
covered + byte-identical on the live path* (locator: line 1691).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* are these figures the current ones, and do
the suite sizes they name still exist at the current commit?

---

**Row 2.25 — the loaded-edge boundary is artificial, vanishes on extension, and the edge slice grows.**

*Outgoing statement.* "The clip injects a boundary at the loaded start that is not a change-point at
all: a sustained-in note sounds on both sides of it, and it exists only because the far side was not
loaded." — the 2026-08-08 block (locator: line 1703).

*Derived statements that speak to it.* S-28, S-32.

*Current-text axis.* S-32: **DIFFERS**. S-28: **DIFFERS**.

*The difference, in both texts' own words.* S-32 makes the span's start a **change point** — *"Its
first change point is the span's start"* — while S-28 defines a change point as the onset or release
of an eligible event; the outgoing text says the injected boundary *"is not a change-point at all"*
and exists only because the far side was unloaded. **The derivation is internally in the same tension
and does not name it**: S-32 admits a change point that S-28's definition does not produce.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the specification say whether the
span's edge is a change point or an artificial boundary marked as such, since a consumer weighing
boundary evidence at that position needs to know which it is.

---

**Row 2.26 — an "old slices stay byte-identical" assertion is false and must never be written as a
test.**

*Outgoing statement.* "an 'old slices stay byte-identical' assertion is **FALSE and must never be
written as a test**." — the 2026-08-08 block (locator: line 1701).

*Derived statements that speak to it.* None.

*Current-text axis.* **THE DERIVATION IS SILENT.**

*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 2.21: the prohibition is the
operational half of the re-slice equivalence property, and it is the half a later build is most
likely to breach.

---

**Row 2.27 — the slice stays minimal; selection-versus-context is the consumer's to derive.**

*Outgoing statement.* "**The slice stays MINIMAL — it carries start and end and nothing else; whether
a slice is inside the user's selection or is only surrounding context is derived by the consumer.**"
— the 2026-08-08 block (locator: line 1718).

*Derived statements that speak to it.* S-50.

*Current-text axis.* S-50: **DIFFERS**.

*The difference, in both texts' own words.* S-50 publishes *"the slice list … with each slice's
sounding set by event identity"*, so the slice carries its notes; the outgoing text carries *"start
and end and nothing else"* and leaves the notes to be fetched from the note model on demand.

*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the specification state whether
the sounding set is **carried on** the slice or **fetched from** L0 by identity, since S-50 lists it
as published and the outgoing text deliberately does not store it.

---

**Row 2.28 — this layer owns no selection semantics, so a selection tag would be another concern's.**

*Outgoing statement.* "this layer owns no selection semantics — cutting the music where the sounding
set changes involves no judgment about what the user selected — so a selection tag would keep another
component's concern in this one's output." — the 2026-08-08 block (locator: line 1722).

*Derived statements that speak to it.* S-53.

*Current-text axis.* S-53: **AGREES** in substance — S-53's whole point is that L1 publishes
candidates and evidence and leaves every decision to its consumer.

*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-53).

---

#### Not a statement — listed so the arithmetic closes (5)

1. "The **constant-(tonal-)sonority slicer** — layer 2 of the rebuild." — *a naming*, and the layer
   numbering is the old four-layer scheme.
2. "Built with `slicer_tests.cpp` (20 tests: the audit §3 functional set + edge/eligibility cases +
   the Phase-2 bounded-context set CP1–CP7 — degenerate clip-inertness, sustained-in/out clip
   correctness, seam-aware stability on extend, re-slice equivalence)." — *a test count and a test
   locator*.
3. "See `cc_layer2_impl_report.md` (HELD), `cowork_layer2_slicing_design.md`,
   `cc_layer2_audit_dossier.md`." — *a pointer*; the second of the three is population position 6.
4. The **delegation pointer** paragraph naming `cowork_layer2_slicing_design.md`, with its
   parenthetical distinguishing a citation from a delegation — *a pointer and a filing decision*.
5. "On a **whole-score** model `loadedStart ≤ firstEligibleOnset` and `loadedEnd ≥
   lastEligibleRelease`, so the clip is **inert** … byte-identical to before the clip." — *a
   restatement of Row 2.3's measured property in arithmetic form*; it is not counted twice.

#### The arithmetic at this document

- Statements: **28** (rows 2.1 to 2.28; no row of this document splits).
- Listed under *not a statement*: **5**.
- **Every outgoing statement carries exactly one disposition, and none carries two.** 28 disposition
  lines over 28 statements.
- **UNPLACED rows at this document: 1** (Row 2.10).

| Disposition | Count | Statements |
|---|---|---|
| ADOPTED — carried | 12 | 2.1, 2.4, 2.5, 2.6, 2.9, 2.11, 2.12, 2.14, 2.18, 2.19, 2.23, 2.28 |
| ADOPTED — proposed | 10 | 2.8, 2.13, 2.15, 2.16, 2.17, 2.20, 2.21, 2.25, 2.26, 2.27 |
| RELOCATED | 0 | — |
| QUARANTINED | 3 | 2.3, 2.7, 2.24 |
| DISCARDED | 0 | — |
| HISTORICAL | 2 | 2.2, 2.22 |
| UNPLACED | 1 | 2.10 |
| **Total** | **28** | — |

**The column sums to 28, against 28 statements, so the arithmetic closes at this document:**
12 + 10 + 0 + 3 + 0 + 2 + 1 = 28. **The statement lists are the record** and the integers are
re-derivable from them by counting.

#### The current-text axis at this document, counted at these rows

| Verdict | Count |
|---|---|
| AGREES | 27 |
| DIFFERS | 14 |
| THE DERIVATION IS SILENT | 7 |
| **Total verdicts** | **48** |

*(48 verdicts over 28 statements because thirteen rows name more than one derived statement.)*

#### What this document's rows put in front of the user, in one paragraph

**Row 2.16 is the sharpest disagreement in this comparison so far and it is a flat contradiction, not
a nuance**: the derivation states that a grace note opens no change point and belongs to no sounding
set, and the outgoing text states that a grace *"genuinely opens/closes a boundary by its span"*. It
is not a small case — it decides the change-point set on any score with ornaments, and the
derivation's no-zero-length-slice invariant (S-30) is built on the opposite answer. Beside it sit
three questions the two texts answer differently and which are really one question asked three ways —
**what the published domain is** (Rows 2.13, 2.20) and **what the span's edge is** (Row 2.25): the
derivation covers the working span exactly, with a silent first slice and *entered sounding* marks,
while the outgoing text tiles the intersection with the sounding material and publishes no mark. And
**Row 2.10 is the one UNPLACED row so far**, where both texts refuse to drop an ineligible note and
disagree only about where it is carried.

---

### 6.3 — Document 3: `cowork_layer1_note_model_design.md`

> **Manifest for this document.** Outgoing statements: **64** — rows 3.1 to 3.62, of which Row 3.14
> carries three claims and is split (i)/(ii)/(iii), so 62 row numbers carry 64 statements. Listed
> under *not a statement*: **11**. Counted at this document by this session.
>
> **Why this document is in the population:** named by Ruling 32 item 2 — the ratified contract the
> `ARCHITECTURE.md` Layer 1 section delegates to by name. It is the fullest current statement of
> L0's subject in the record.
>
> **A note on this document's form, because it changes how the rows read.** It is a whole design
> document in the fourteen-section standard, so a large part of it is deliberately about the
> *component* rather than about the analysis: its testing plan, its risks, its build state, its
> glossary. Those parts are dispositioned exactly like any other statement, and a good many land as
> QUARANTINED or HISTORICAL for that reason and not because anything is wrong with them.
>
> **Rows are written compactly from here on.** A row carrying no DIFFERS states its quote, its
> location, the derived statements, the verdict and the disposition, and stops; a row carrying a
> DIFFERS states the difference in both texts' own words, as every such row above does.

---

#### §0 — the terms table

**Row 3.1 — the analysis works over the user's selection, extended on request.**
*Statement.* "the **selection** is the music the user chose; the **loaded span** is the music this
layer currently covers (selection plus any granted extensions)" — §0, the first row (locator: line 17).
*Derived.* S-32 (the published slice list covers the working span exactly), S-53 (the working span is
the only thing a caller supplies beyond L0).
*Current-text axis.* S-32: **AGREES**. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.2 — which staves take no part in tonal analysis.**
*Statement.* "**Staff-eligible** | The note's staff takes part in tonal analysis. Ineligible staves
… : **hidden** staves, **percussion (drumset)** staves, and the **chord-symbol track**" — §0
(locator: line 18).
*Derived.* S-20 (unpitched notes), S-2 (annotation carried beside L0), S-15 (the five per-note
conditions).
*Current-text axis.* S-20: **AGREES** on percussion. S-2: **AGREES** on the chord-symbol track.
S-15: **DIFFERS** on hidden staves.
*The difference.* S-15's eligibility test is per note and names no staff-level fact, so a note on a
**hidden** staff meets all five of its conditions where the outgoing text excludes it; S-20 reaches
percussion only because such a note is *unpitched*, and S-2 reaches the chord-symbol track only
because a chord symbol is *annotation*, so neither reaches a hidden staff carrying ordinary pitched
notes.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Rows 1.6(ii) and 2.8: that L0 supply
a per-staff analysis-eligibility fact.

**Row 3.3 — the chord-symbol track is detected and its notes are kept and marked.**
*Statement.* "Detected by the shared staff-eligibility predicate; its notes are kept and marked
ineligible." — §0 (locator: line 19).
*Derived.* S-2, S-18.
*Current-text axis.* S-2: **AGREES**. S-18: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-2 carries the chord-symbol case explicitly, S-18 the
keep-and-label discipline).

**Row 3.4 — the two per-note flags, and that one covers muted and cue notes together.**
*Statement.* "whether the note actually plays (false for muted notes and imported cue notes …), and
whether it is visible" — §0 (locator: line 20).
*Derived.* S-3, S-15, S-18, S-19.
*Current-text axis.* S-3: **AGREES**. S-15: **AGREES**. S-18: **AGREES**. S-19: **DIFFERS**.
*The difference.* S-19 makes cue size an **attribute** that *"does not by itself change eligibility"*,
publishing it and leaving the case to OQ-4; the outgoing text folds an imported cue note into the
**plays** flag, so a cue note is ineligible with no separate fact recorded.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that L0 state whether cue size
survives as its own fact or is absorbed into the sounds flag, since S-19 publishes it and this text
does not.

**Row 3.5 — voice-level eligibility is not this layer's to define.**
*Statement.* "Voice-level 'eligibility' (the three-flag combination consumers use) is defined by the
consuming spec …; this layer defines the staff flag and the two per-note flags it is built from." —
§0 (locator: line 20).
*Derived.* S-15 (eligibility belongs to L1, the charter leaving it to the derivation), S-13.
*Current-text axis.* S-15: **DIFFERS**.
*The difference.* S-15 places the eligibility predicate squarely in L1 and derives it there; the
outgoing text splits it — the staff flag and two per-note flags here, the combination defined in a
consuming specification.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that eligibility have **one** home,
since it is currently defined across at least three documents and the two texts disagree about which
owns it.

#### §1 — introduction and purpose

**Row 3.6 — the layer produces the complete list of notes that actually sound, with their facts.**
*Statement.* "It produces the **complete** list of the notes that actually sound in the music being
analysed — **tie-resolved and lossless** … — together with the facts about each note that the later
architectural layers need." — §1 (locator: line 27).
*Derived.* S-3, S-23, S-18.
*Current-text axis.* S-3: **AGREES**. S-23: **AGREES**. S-18: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.7 — it is built once and no later layer re-reads the score.**
*Statement.* "It is built once and is then read by every later architectural layer; no later
architectural layer reads the raw MuseScore score again." — §1 (locator: line 29).
*Derived.* S-9 (what L1 reads from L0).
*Current-text axis.* S-9: **AGREES** in substance — S-9 fixes L1's inputs as L0's published facts and
nothing else.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.8 — the layer works on the user's selection, not on a whole score.**
*Statement.* "It never works on 'a whole score' in the abstract. It works on **the part of the score
that the user has selected for analysis**" — §1 (locator: line 33).
*Derived.* S-32, S-53.
*Current-text axis.* S-32: **AGREES**. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-32 cites the same ground: whole-score analysis is the
degenerate case).

**Row 3.9 — whole-score reading happens only in offline measurement.**
*Statement.* "(Reading an entire score from beginning to end happens only in our offline testing of
the analysis quality; it never happens in the shipping product.)" — §1 (locator: line 35).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is a whole-score build in fact confined to
the offline measurement path at the current commit?

**Row 3.10 — one shared reading for the whole system.**
*Statement.* "It gives the whole analysis system **one** shared, accurate reading of the notes, so
that every later architectural layer works from the same correct note list instead of each computing
its own." — §1 (locator: line 38).
*Derived.* S-9.
*Current-text axis.* S-9: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.11 — a tied group is one held note with one start and one end.**
*Statement.* "**Tie-resolved.** A group of tied notes is treated as **one single held note** — one
start time and one end time — instead of as the several separate written notes it appears to be." —
§1 (locator: line 43).
*Derived.* S-23.
*Current-text axis.* S-23: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.12 — slurred notes are not merged; only ties join written notes.**
*Statement.* "Slurred notes are *not* merged this way: a slur marks phrasing, not one continuous
sound, so slurred notes — whether of the same pitch or of different pitches — remain separate notes …
Only ties join written notes into one sounding note; slurs do not." — §1 (locator: line 45).
*Derived.* S-24 (the tie test), S-7 (L0 does not supply slurs).
*Current-text axis.* S-24: **AGREES**. S-7: **DIFFERS**.
*The difference.* S-7 excludes slurs from what L0 supplies altogether, naming in its own premise the
false-negative path *"a slur used in place of a tie between identical pitches (S-16) — L0 would then
need slurs to repair the tie"*, and records that as *"not adopted"*; the outgoing text states the
slur-versus-tie rule as a live distinction the layer makes.
*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-24 carries the operative rule — a link is a tie only
on same spelled pitch, same voice, adjacency — which is what makes a slur fail to merge; the
difference is about whether slurs are *supplied*, and it is stated at Row 3.12 rather than resolved).

**Row 3.13 — the layer keeps every note and every fact any later step might need.**
*Statement.* "**Lossless.** Architectural Layer 1 **keeps every note, and every fact about each note
that any later step might need, and never discards any of it or reduces it to a summary.**" — §1
(locator: line 48).
*Derived.* S-2, S-18, S-20.
*Current-text axis.* S-2: **AGREES**. S-18: **AGREES**. S-20: **DIFFERS**.
*The difference.* S-20 states of an unpitched note that *"It is not published by L1 at all"*, and
records the decision to publish it broadly as *"considered and declined"*; the outgoing text keeps
every note without exception.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the specification state whether
losslessness admits an exception for unpitched notes, the two texts differing on exactly that one
class.

**Row 3.14 (i) — no note at all is lost, even one that will not feed tonal analysis.**
*Statement.* "(a) any note at all — even a note that will not feed tonal analysis is kept, only
marked" — §1 (locator: line 50).
*Derived.* S-18.
*Current-text axis.* S-18: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.14 (ii) — pitch, voice and timing are never replaced by a summary.**
*Statement.* "(b) each note's exact pitch, voice, and timing — the real notes are never replaced by a
count, an average, or a pitch histogram" — §1 (locator: line 51).
*Derived.* S-33, S-3.
*Current-text axis.* S-33: **AGREES** — S-33's whole content is that identity is the event set and not
a folded summary. S-3: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.14 (iii) — which notes are present is separated from what a later layer decides about them.**
*Statement.* "(c) the separation between *which notes are present* and *what a later architectural
layer decides about them*" — §1 (locator: line 52).
*Derived.* S-1 (the admission criterion's condition (ii)), S-53.
*Current-text axis.* S-1: **AGREES**. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-1(ii) is this separation stated as a test).

**Row 3.15 — three kinds of note should not contribute to key-and-chord reasoning.**
*Statement.* "Three kinds of note should not contribute to key-and-chord reasoning: notes that are
**muted** …, notes that are **invisible**, and every note that sits on a staff which is not tonal —
drum/percussion staves, the chord-symbol track …, and hidden staves." — §1 (locator: line 56).
*Derived.* S-15, S-18, S-20, S-2.
*Current-text axis.* S-15: **DIFFERS**. S-18: **AGREES**. S-20: **AGREES**. S-2: **AGREES**.
*The difference.* As at Row 3.2 — the hidden-staff case is reached by no derived statement.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 3.2.

**Row 3.16 — they are kept and flagged, never dropped.**
*Statement.* "Architectural Layer 1 **keeps all of these notes and sets a flag on each one saying
which case it is; it never drops them.**" — §1 (locator: line 59).
*Derived.* S-18.
*Current-text axis.* S-18: **AGREES** — S-18 requires exactly this, *"labelled by which flag excluded
them"*.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.17 — ignoring such a note is a separate, later step.**
*Statement.* "Choosing to *ignore* such a note is a separate step done later (the summary views
described below skip any note that is muted, invisible, or on a non-tonal staff)." — §1 (locator:
line 60).
*Derived.* S-15, S-18.
*Current-text axis.* S-15: **AGREES** — eligibility is a decision taken over L0's facts, not inside
them. S-18: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.18 — the layer's scope in one sentence.**
*Statement.* "read the selected music once; resolve ties; record the per-note facts; and answer the
question 'which notes are sounding during a given span of time?'" — §1 (locator: line 64).
*Derived.* S-3, S-23, S-29.
*Current-text axis.* S-3: **AGREES**. S-23: **AGREES**. S-29: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.19 — it does not weight, average or reduce notes to pitch evidence.**
*Statement.* "It does **not** weight, average, or reduce notes to pitch evidence — that is done by
the summary views, on top of it, and by later architectural layers." — §1 (locator: line 68).
*Derived.* S-33, S-49, S-50.
*Current-text axis.* S-33: **AGREES**. S-49: **AGREES**. S-50: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.20 — it does not cut the music into spans and makes no key, chord or function judgement.**
*Statement.* "It does **not** cut the music into spans (that is Architectural Layer 2) and makes
**no** key, chord, or function judgement (that is Architectural Layer 3 and later)." — §1 (locator:
line 70).
*Derived.* S-9, S-51, S-53.
*Current-text axis.* S-9: **AGREES**. S-51: **AGREES**. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.** *(The layer numbering is the old scheme; under the
ratified charter the slicing this sentence excludes is L1's own, which is a renaming and not a
disagreement.)*

**Row 3.21 — it drops no note.**
*Statement.* "It does **not** drop any note — it keeps every note and only marks the ones that should
not feed tonal analysis." — §1 (locator: line 72).
*Derived.* S-18, S-20.
*Current-text axis.* S-18: **AGREES**. S-20: **DIFFERS** (as at Row 3.13).
*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-18; the unpitched exception is stated once at Row
3.13 and is not counted again here).

**Row 3.22 — it does not decide when to rebuild itself and does not watch for edits.**
*Statement.* "It does **not** decide *when* to build or rebuild itself, and does **not** watch for
score edits — it builds, or widens, only when the caller asks." — §1 (locator: line 73).
*Derived.* S-53.
*Current-text axis.* S-53: **AGREES** in substance — the caller supplies the span and L1 does no
looping of its own.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.23 — it does not decide that more music is needed.**
*Statement.* "It does **not** decide that more music is needed — it supplies a widened span on
request, but the request comes from a later architectural layer." — §1 (locator: line 75).
*Derived.* S-53.
*Current-text axis.* S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

#### §2 — constraints

**Row 3.24 — lossless and read-only toward the music.**
*Statement.* "**Lossless, and read-only toward the music:** keep every note, change no note,
summarise no note." — §2 (locator: line 79).
*Derived.* S-1, S-18, S-33.
*Current-text axis.* S-1: **AGREES**. S-18: **AGREES**. S-33: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.25 — one reading for the whole system; no other code re-reads the score.**
*Statement.* "**One reading for the whole analysis system:** there is a single note model; no other
code re-reads the raw score." — §2 (locator: line 80).
*Derived.* S-9.
*Current-text axis.* S-9: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.26 — no limit on how far backwards a span query searches.**
*Statement.* "**No limit on how far backwards in time a query searches:** … the answer must include
notes that started **earlier in time** than that span and are still sounding when it begins, no
matter how much earlier they started." — §2 (locator: line 81).
*Derived.* S-29.
*Current-text axis.* S-29: **THE DERIVATION IS SILENT** — S-29 defines the sounding set without
bounding the search that finds it.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, the same proposal as Row 1.5(ii): that L0 state the
no-backward-horizon rule explicitly.

**Row 3.27 — it operates at any selection size and in any style, within a stated cost budget.**
*Statement.* "**Operates on the user's selected part of the score, at any selection size and in any
musical style** (it makes no assumption about style); it must stay fast even when the selected music
is the entire piece" — §2 (locator: line 84).
*Derived.* S-32.
*Current-text axis.* S-32: **AGREES** on the span half; **THE DERIVATION IS SILENT** on cost.
*PROPOSED DISPOSITION.* **QUARANTINED**, for its cost half. *Audit question:* is the stated
logarithmic-plus-output bound met at the largest score the record requires to be handled?

**Row 3.28 — the loaded span can be widened on request, and the requester decides.**
*Statement.* "Architectural Layer 1 can be asked to **widen the span of music it covers — earlier in
time, later in time, or both — and to take in the extra notes.** Architectural Layer 1 is the
*supplier* … deciding that more music is needed is the requesting architectural layer's
responsibility" — §2 (locator: line 88).
*Derived.* S-53.
*Current-text axis.* S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.29 — it is not responsible for noticing that its model is stale.**
*Statement.* "**Architectural Layer 1 is not responsible for noticing when its note model has become
out of date.** … Deciding that the note model must be rebuilt … is the caller's responsibility" — §2
(locator: line 97).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that L0 state who owns staleness,
since the derivation's contract is silent on what happens when the notated record changes under a
built model.

**Row 3.30 — once built, the results do not change.**
*Statement.* "**Fixed for the architectural layers above it:** once the note model is built, its
results do not change; the only permitted code changes are speed improvements that return *identical*
results." — §2 (locator: line 102).
*Derived.* S-28 (positions are exact), S-53.
*Current-text axis.* S-28: **AGREES** in substance on determinism. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

#### §3 — context and scope

**Row 3.31 — the inputs are the selected score and the notation system's tie information.**
*Statement.* "the user-selected portion of the MuseScore score, plus the notation system's tie
information (which written notes are tied to which)." — §3 (locator: line 106).
*Derived.* S-3, S-23.
*Current-text axis.* S-3: **DIFFERS**.
*The difference.* S-3 requires L0 to supply, per note, a great deal more than pitch and tie links —
its metric position as *"(bar index, offset within the bar, absolute position)"*, its ornament and
articulation signs, its cue size — and S-5 to S-7 require per-bar facts, signature-change positions,
fermatas, pedal marks and tremolo marks; the outgoing input list names the score and the tie
information only.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the input list be stated at the
width S-3 to S-7 require, since the two texts differ over what the layer is handed rather than over
what it does with it.

**Row 3.32 — the operations: build, return every note in onset order.**
*Statement.* "*Build the note model* from the selected music (reading it once). *Return every note in
the note model*, in a fixed order — earliest start time first." — §3 (locator: line 110).
*Derived.* S-3.
*Current-text axis.* S-3: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.33 — the sounding-during-a-span query, with no backward limit.**
*Statement.* "*Which notes are sounding during the span of time from A to B?* — returns the notes
whose own sounding span overlaps the span A-to-B, including notes that started **earlier in time**
than A and are still sounding at A; there is no limit on how far **backwards in time** it searches."
— §3 (locator: line 111).
*Derived.* S-29.
*Current-text axis.* S-29: **AGREES** on the overlap definition; the no-limit half is Row 3.26's.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.34 — the onsets-within-a-span query.**
*Statement.* "*Which notes start within the span of time from A to B?*" — §3 (locator: line 114).
*Derived.* S-28.
*Current-text axis.* S-28: **AGREES** in substance — onsets are the derivation's change points.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.35 — extend widens the covered span, adds notes only, clamps and reports.**
*Statement.* "extensions only ever **add** notes (nothing already loaded changes); each call widens by
**one increment** and returns, the requesting layer, not this one, deciding whether to ask again; a
request past the score edge clamps at the boundary and reports it." — §3 (locator: line 121).
*Derived.* S-53.
*Current-text axis.* S-53: **AGREES** on who decides; **THE DERIVATION IS SILENT** on the clamp and
the append-only property.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that L0 state the append-only and
clamp-and-report properties of enlarging the span, which the derivation does not carry.

**Row 3.36 — the consumers.**
*Statement.* "the derived summary views …; the Architectural Layer 2 slicer; the Architectural Layer 3
key/mode code." — §3 (locator: line 126).
*Derived.* S-9, S-53.
*Current-text axis.* S-9: **AGREES**. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.37 — it knows nothing of keys, chords and function.**
*Statement.* "**What Architectural Layer 1 deliberately knows nothing about:** keys, chords, and
function — it sits beneath all musical judgement." — §3 (locator: line 129).
*Derived.* S-1, S-9, S-51.
*Current-text axis.* S-1: **AGREES**. S-9: **AGREES**. S-51: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

#### §4 to §8 — strategy, structure, runtime, data, crosscutting

**Row 3.38 — read once into one onset-ordered list; one note per tied group.**
*Statement.* "Read the user-selected music exactly once into a single list of notes ordered by start
time. For each group of tied notes, record one note that runs from the first tied note's start time to
the last tied note's end time" — §4 (locator: line 138).
*Derived.* S-23.
*Current-text axis.* S-23: **AGREES**, and exactly — S-23 fixes the onset as the first note's and the
release as the last's.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.39 — mark rather than drop, and answer span queries from the list.**
*Statement.* "Keep every note; for the notes that should not feed tonal analysis, set a marking flag
rather than dropping them; and answer span-of-time questions directly from the list." — §4 (locator:
line 140).
*Derived.* S-18, S-29.
*Current-text axis.* S-18: **AGREES**. S-29: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.40 — a held sound is one note, a long note is never missed, no note is counted twice.**
*Statement.* "a held sound is one note, a long note is never missed, and no note is counted twice." —
§4 (locator: line 143).
*Derived.* S-23.
*Current-text axis.* S-23: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.41 — a note record is one tie-resolved note with the eleven facts.**
*Statement.* "**A note record** — one tie-resolved note together with its facts (the eleven fields
listed in Section 7)." — §5 (locator: line 146).
*Derived.* S-3.
*Current-text axis.* S-3: **DIFFERS** (the same difference as Row 1.3, stated there).
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 3.42.

**Row 3.42 — the eleven facts, enumerated.**
*Statement.* "Each note record carries eleven facts: its **sounding pitch**; its **spelled pitch** …;
which **staff** and which **voice** …; its **start time-position**, its **end time-position**, and its
**duration** …; and four yes/no facts — whether it is a **grace note**, whether it actually **sounds**
…, whether it is **visible**, and whether it is **staff-eligible**" — §7 (locator: line 175).
*Derived.* S-3.
*Current-text axis.* S-3: **DIFFERS**.
*The difference.* S-3 additionally requires *"whether it is pitched"*, *"whether it is tied to the
preceding note and to the following note"*, *"whether it is cue-sized"*, *"the ornament and
articulation signs attached to it"*, and a metric position decomposed into *"(bar index, offset within
the bar, absolute position)"*; the outgoing eleven carry an absolute position only and add
`staff-eligible`, which S-3 does not name.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the per-note fact list be
reconciled to one list — the five S-3 facts absent here decide S-15's eligibility test, S-17's
ornament attribute and S-34's bar-relative metric hierarchy, so their absence is not cosmetic.

**Row 3.43 — the model owns an onset-ordered list, a borrowed score pointer and a look-up index.**
*Statement.* "**The note model** — owns the list of note records ordered by start time, a borrowed
reference to the source MuseScore score, and a numeric look-up index." — §5 (locator: line 147).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does the borrowed score reference outlive
the model in every path that holds one?

**Row 3.44 — building walks every staff, voice and position including grace notes.**
*Statement.* "Building the note model walks every staff, every voice, and every time-position
(including grace notes), resolves ties, records the per-note facts, and sorts the records by start
time." — §5 (locator: line 148).
*Derived.* S-15, S-16.
*Current-text axis.* S-16: **DIFFERS**.
*The difference.* S-16 states that a grace note *"opens no change point and belongs to no sounding
set"* and is published instead as an *ornamental attachment* of its host; the outgoing text walks
grace notes into the same record list as ordinary notes, carrying only an `isGrace` flag.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Rows 2.16 and 2.17 — the same grace
question, met here at the build rather than at the slicer.

**Row 3.45 — the look-up index answers span queries without scanning.**
*Statement.* "**The numeric look-up index** — a structure that lets the two span-of-time questions …
be answered quickly even when the selected music is large, instead of scanning the whole list of notes
every time." — §5 (locator: line 151).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does the index return exactly what a linear
scan returns, in the same order, at the current commit?

**Row 3.46 — the summary views are deliberately lossy and sit on top.**
*Statement.* "**Derived summary views (a separate module, not part of Architectural Layer 1's
core):** … read-only summaries built *on top of* the note model — deliberately lossy convenience
views, with the lossless note model still underneath them." — §5 (locator: line 155).
*Derived.* S-33, S-49.
*Current-text axis.* S-33: **AGREES** that the lossless set is what identity rests on. S-49:
**AGREES** that a derived view is published beside, not instead of, the facts.
*PROPOSED DISPOSITION.* **RELOCATED — to L2, *the tonal reading, the one entangled decision***, for
the weighting view's own content, exactly as Row 1.9; the losslessness half is carried by S-33 and
travels with the relocation rather than being lost.

**Row 3.47 — the five runtime scenarios.**
*Statement.* the five bullets of §6 — building; a span query; three tied quarters plus a following
note becoming **two** notes; a note carried in from earlier; widening the span (locator: lines
161–172).
*Derived.* S-23, S-29, S-53.
*Current-text axis.* S-23: **AGREES** (the three-tied-quarters case is S-23's own arithmetic).
S-29: **AGREES**. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.** *(Counted as one statement: the five bullets are one
worked illustration of rules already rowed, and none states a rule the rows above do not.)*

**Row 3.48 — all times are absolute positions within the piece.**
*Statement.* "All times are absolute time-positions within the piece." — §7 (locator: line 181).
*Derived.* S-3, S-34, S-36.
*Current-text axis.* S-3: **DIFFERS**.
*The difference.* S-3 requires the position as *"(bar index, offset within the bar, absolute
position)"* — three things — because S-34's metrical hierarchy and S-36's anacrusis alignment are
computed from the bar-relative offset; the outgoing text carries the absolute position alone.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 3.42: that the bar index and the
within-bar offset be supplied, the metric-strength class depending on them.

**Row 3.49 — single source of truth.**
*Statement.* "**Single source of truth** — … every architectural layer reads these notes; no
architectural layer re-reads the raw MuseScore score." — §8 (locator: line 186).
*Derived.* S-9.
*Current-text axis.* S-9: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.50 — deterministic.**
*Statement.* "**Deterministic** — the same selected music always produces exactly the same note
model." — §8 (locator: line 188).
*Derived.* S-28.
*Current-text axis.* S-28: **AGREES** in substance.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.51 — edge handling.**
*Statement.* "**Edge handling** — an empty or backwards span of time returns no notes; a silent span
returns no notes; grace, muted, invisible, and non-tonal-staff notes are kept and marked, never
dropped." — §8 (locator: line 191).
*Derived.* S-18, S-31.
*Current-text axis.* S-18: **AGREES** on keep-and-mark. S-31: **DIFFERS**.
*The difference.* S-31 requires a silent stretch to be **published as a slice with an empty sounding
set** rather than passed over — *"Silence is a notated fact and strong boundary evidence"* — where the
outgoing text returns nothing for a silent span.
*PROPOSED DISPOSITION.* **ADOPTED — carried** for the keep-and-mark half; the silence half is the same
question as Rows 2.13 and 2.20 and is not counted a second time there. *(Where a row's two halves
would fall to different dispositions, the disposition recorded is the one its principal clause takes;
this is the only row of this document where that arises, and it is stated rather than left implicit.)*

#### §9 — the architecture decisions

**Row 3.52 — a tied group is one note, and the alternative was weighed.**
*Statement.* "**A group of tied notes is one note, not several.** Alternative considered: keep each
tied note separate. Chosen: one note — the held parts of a tie still sound, so counting them as
separate notes counts the same sustained sound more than once." — §9 (locator: line 195).
*Derived.* S-23.
*Current-text axis.* S-23: **AGREES**, and on the same ground.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.53 — no backward limit, and the alternative was weighed.**
*Statement.* "**No limit on how far backwards in time a query searches.** Alternative considered:
limit the backward-in-time search for speed. Chosen: no limit — a limit silently drops notes held
longer than the limit" — §9 (locator: line 198).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Rows 1.5(ii) and 3.26 — and this row
is the one that carries the **defense** the proposal needs, which is why it is rowed separately.

**Row 3.54 — keep and mark rather than filter while reading.**
*Statement.* "**Keep every note and mark it, rather than filter notes out while reading.** …
Chosen: keep-and-mark — so that choosing to ignore a note is an explicit, reversible step taken in a
later architectural layer." — §9 (locator: line 201).
*Derived.* S-18, S-15.
*Current-text axis.* S-18: **AGREES**. S-15: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 3.55 — the index structure, and the alternatives weighed.**
*Statement.* "**A numeric look-up index** … Alternatives considered: an interval tree, a bucketed
index. Chosen: this structure — it is the simplest one that answers the span-of-time queries quickly
*and* returns notes in exactly the same order a plain left-to-right scan would." — §9 (locator: line
204).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED**, with Row 3.45. *Audit question:* is the order-equivalence
with a linear scan tested rather than asserted?

#### §10 to §14 — testing, risks, glossary, background, related work

**Row 3.56 — the accuracy shift the layer caused, and that it was accepted.**
*Statement.* "**An accepted, fully-explained shift in the accuracy metric, caused by building
Architectural Layer 1 correctly** — resolving ties and removing the backward-in-time search limit
moved the project's accuracy metric by a small, fully-attributed amount" — §11 (locator: line 222).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED**, with Rows 1.15 and 1.16 — the same measurement, recorded
twice in two documents.

**Row 3.57 — grace-note timing is to be confirmed when a later layer uses grace notes.**
*Statement.* "**Grace-note timing** — exactly how a grace note's start time, end time, and duration
are recorded should be confirmed when Architectural Layer 3 begins using grace notes (there is
deliberately no special grace-note handling in Architectural Layer 1)." — §11 (locator: line 228).
*Derived.* S-16, S-15.
*Current-text axis.* S-16: **DIFFERS**.
*The difference.* S-16 settles the grace question — no change point, no membership of any sounding
set, published as an ornamental attachment — and marks its own status *settled*; the outgoing text
records the same question as **open**, to be confirmed later, and states that the layer applies no
special handling.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Rows 2.16, 2.17 and 3.44. **This row
is evidence that the grace question is open in the outgoing record and closed in the derivation**,
which is worth the user's attention when the disagreement at Row 2.16 is ruled.

**Row 3.58 — the whole-score build is interim, and the target is build-over-selection plus extend.**
*Statement.* "**The build currently reads the whole score even when only part of it is queried** — an
**interim** behaviour, not the target. … the target is *build over the selection, then extend on
request*." — §11 (locator: line 230).
*Derived.* S-32, S-53.
*Current-text axis.* S-32: **AGREES** on the target. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **HISTORICAL** — a build state and its plan; the rule it points at is already
carried at Rows 3.8 and 3.28.

**Row 3.59 — what the layer replaces, and the two defects it fixes by construction.**
*Statement.* "**What it replaces:** the earlier per-consumer note collectors … They were tie-blind …
and they limited their backward-in-time search to four whole-notes, which silently dropped notes held
longer than that. Architectural Layer 1 fixes both problems by construction." — §13 (locator: line
254).
*Derived.* S-23.
*Current-text axis.* S-23: **AGREES** on the tie half; **THE DERIVATION IS SILENT** on the horizon
half.
*PROPOSED DISPOSITION.* **HISTORICAL** — it records what was replaced and why.

**Row 3.60 — a specified cue-note flag was removed because the distinction is unrecoverable after
import.**
*Statement.* "**A field we specified then removed:** we had planned a 'cue note' flag, then removed it
— once a MuseScore score is imported, a cue note can no longer be told apart from an ordinary muted
note, and the existing 'does it sound' flag already excludes both." — §13 (locator: line 261).
*Derived.* S-19.
*Current-text axis.* S-19: **DIFFERS**.
*The difference.* S-19 publishes cue size as an attribute and leaves eligibility to the flags,
recording the unresolved cases as OQ-4 and OQ-5; the outgoing text records that the cue distinction is
**not recoverable at all** after import, which if true would close OQ-4 by removing its subject.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that this fact — that an imported
score carries no cue distinction — be stated in L0, because it bears directly on two of the
derivation's open questions and the derivation did not have it. **This is the clearest case in this
document of the outgoing text holding a fact the derivation lacked.**

**Row 3.61 — what the design is built on, from the field.**
*Statement.* "**Built on:** the idea of a **lossless symbolic-music event list** … **Standard
interval-query data structures** … **Tie and playback resolution** comes from MuseScore's own note
model …, not reinvented." — §14 (locator: line 268).
*Derived.* S-23, S-3.
*Current-text axis.* S-23: **AGREES**. S-3: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried** — the lineage is the same one S-23 and S-3 cite.

**Row 3.62 — summarising to pitch classes at read time was rejected as lossy.**
*Statement.* "**Discarded / not used:** **summarising notes to pitch classes at read time** — rejected
here because it is lossy; summarising belongs in the derived views, on top of the lossless model." —
§14 (locator: line 273).
*Derived.* S-33.
*Current-text axis.* S-33: **AGREES**, and decisively — S-33's own content is that identity is the
event set and not the pitch-class set.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

---

#### Not a statement — listed so the arithmetic closes (11)

1. The status banner and its five source-commit identifiers — *provenance and a build state's
   identifiers*.
2. The §0 rows **Tie-resolved / lossless**, **Byte-identical**, **Phase-1a / Phase-1b**, and **The
   system check (§10)** — *four vocabulary rows that point at other sections or other documents and
   state no rule of their own*. (Counted as four.)
3. "**Implementation (source files):** the note model and its look-up index are in
   `src/composing/analysis/notemodel/note_model.{h,cpp}` …" — *an implementation locator*.
4. §10's five testing bullets — *a test plan and its test-file locator*, which state what is checked
   rather than what the analysis does. (Counted as one.)
5. §12's glossary — *definitions restating §1 and §0*, none introducing a rule not already rowed.
6. The §11 bullet's closing sentence, "The build-selection + extend **contract** is what every layer
   above is written against, so the interim is invisible to them." — *a restatement of Row 3.58*.
7. "**Corpora used:** the **353-piece Bach chorale set (plus a Corelli trio)** — used to confirm the
   look-up index stays correct and fast at scale." — *a measurement-corpus citation*.

#### The arithmetic at this document

- Statements: **64** (rows 3.1 to 3.62, with Row 3.14 split into three; Row 3.47's five runtime
  bullets are counted as one, stated at that row).
- Listed under *not a statement*: **11**.
- **Every outgoing statement carries exactly one disposition, and none carries two.**
- **UNPLACED rows at this document: 0.**

| Disposition | Count | Statements |
|---|---|---|
| ADOPTED — carried | 39 | 3.1, 3.3, 3.6, 3.7, 3.8, 3.10, 3.11, 3.12, 3.14(i), 3.14(ii), 3.14(iii), 3.16, 3.17, 3.18, 3.19, 3.20, 3.21, 3.22, 3.23, 3.24, 3.25, 3.28, 3.30, 3.32, 3.33, 3.34, 3.36, 3.37, 3.38, 3.39, 3.40, 3.47, 3.49, 3.50, 3.51, 3.52, 3.54, 3.61, 3.62 |
| ADOPTED — proposed | 16 | 3.2, 3.4, 3.5, 3.13, 3.15, 3.26, 3.29, 3.31, 3.35, 3.41, 3.42, 3.44, 3.48, 3.53, 3.57, 3.60 |
| RELOCATED | 1 | 3.46 |
| QUARANTINED | 6 | 3.9, 3.27, 3.43, 3.45, 3.55, 3.56 |
| DISCARDED | 0 | — |
| HISTORICAL | 2 | 3.58, 3.59 |
| UNPLACED | 0 | — |
| **Total** | **64** | — |

**The column sums to 64, against 64 statements, so the arithmetic closes at this document:**
39 + 16 + 1 + 6 + 0 + 2 + 0 = 64. **The statement lists are the record**; the integers are counted at
them.

**Two rows carry a DIFFERS *and* an ADOPTED — carried disposition, and that is deliberate rather than
an inconsistency.** Row 3.12 (slurs) and Row 3.51 (edge handling) each have a principal clause whose
content a derived statement carries, and a secondary clause on which the two texts differ; the row
states the difference and the disposition follows the principal clause. The two axes are independent
by construction — the current-text axis is evidence about the present text, the disposition axis is
the statement's fate — so a row may honestly carry AGREES on one derived statement, DIFFERS on
another, and one disposition.

#### The current-text axis at this document, counted at these rows

| Verdict | Count |
|---|---|
| AGREES | 81 |
| DIFFERS | 15 |
| THE DERIVATION IS SILENT | 11 |
| **Total verdicts** | **107** |

#### What this document's rows put in front of the user

Three things. **The grace question returns, twice** — at Row 3.44 (the build walks grace notes into
the record list) and at Row 3.57, where the outgoing text records grace timing as an **open** question
to be confirmed later while the derivation's S-16 marks the same question **settled**. Together with
Row 2.16 that is three independent places in the outgoing record where grace notes are handled
opposite to the derivation. **The input list is narrower than the derivation's** — Rows 3.31, 3.42 and
3.48: the outgoing layer is handed the score and its tie links and publishes eleven per-note facts,
where S-3 to S-7 require the bar-relative position, the ornament signs, the cue size, the tie flags
and the per-bar and per-signature facts that S-34 and S-36 compute the metric-strength class from.
**And one row runs the other way** — Row 3.60, where the outgoing text holds a fact the derivation did
not have: an imported score cannot distinguish a cue note from a muted one, which bears directly on
the derivation's OQ-4.

---

### 6.4 — Document 4: `cowork_layer1_tone_collection_design.md`

> **Manifest for this document.** Outgoing statements: **40** (rows 4.1 to 4.40). Listed under *not a
> statement*: **6**. Counted at this document by this session.
>
> **Why this document is in the population:** named by Ruling 32 item 2 — one of the five root design
> documents. It is **not** in the ruled specification document set, and stays in the population by
> name.
>
> **★ THIS DOCUMENT'S OWN BANNER DECLARES IT HISTORICAL, AND THAT CHANGES HOW ITS ROWS READ WITHOUT
> CHANGING HOW THEY ARE DISPOSITIONED.** Its banner states that the responsibility it designs *"is now
> the lossless note model's"*, that it *"is NOT a contract home"*, and that its sign-off checkboxes
> were never ticked. **A document's status is not a disposition**: the phase definition assigns a
> disposition per *statement*, so a statement of this document whose content a derived statement
> carries is ADOPTED — carried exactly as it would be anywhere else, and the banner is rowed as the
> status it is. What the banner does change is the reading: a large part of this document is a
> **verified description of code as it stood**, and such statements land QUARANTINED because that is
> what they are, not because the document is superseded.

---

#### §1 and §2 — the intended role and the scope

**Row 4.1 — collect, and only collect, every sounding note, annotated, losslessly, by one path.**
*Statement.* "**Collect — and only collect — every sounding note in a region, annotated, losslessly,
by ONE path.**" — §1 (locator: line 34).
*Derived.* S-3, S-18, S-33.
*Current-text axis.* S-3: **AGREES**. S-18: **AGREES**. S-33: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 4.2 — it is the boundary between the engraving model and the analysis types.**
*Statement.* "It is the boundary between the engraving model (Score/Segment/Note) and the analysis
types." — §1 (locator: line 35).
*Derived.* S-1, S-9.
*Current-text axis.* S-1: **AGREES**. S-9: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried** (S-1 is that boundary stated as a test).

**Row 4.3 — one factual question, answered with the annotated note set.**
*Statement.* "It answers exactly one factual question: 'for region `[startTick, endTick)`, what notes
sound?' — and returns the **note set**, each note annotated with the facts needed downstream (pitch,
tpc/spelling, staff, voice, onset, offset, in-region duration, `isGrace`, `plays`, `visible`,
staff-eligibility)." — §1 (locator: line 36).
*Derived.* S-3, S-29.
*Current-text axis.* S-29: **AGREES** on the half-open region. S-3: **DIFFERS**.
*The difference.* The same shortfall as Rows 1.3 and 3.42 — no pitched flag, no tie flags, no cue
size, no ornament signs, no bar-relative position — and one addition of its own: an **in-region
duration**, a note's duration clipped to the queried region, which S-3 does not carry and which is a
property of the query rather than of the note.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 3.42, and adding one question of
its own: whether a clipped in-region duration belongs in L0 at all, being a function of the caller's
region.

**Row 4.4 — the four things it must not do.**
*Statement.* "It must **NOT** filter (drop grace/non-playing/invisible), **NOT** weight or aggregate
into pitch-class evidence, **NOT** select a bass, and **NOT** make any harmonic/segmentation/key
decision." — §1 (locator: line 38).
*Derived.* S-18, S-33, S-44, S-51.
*Current-text axis.* S-18: **AGREES**. S-33: **AGREES**. S-51: **AGREES**. S-44: **DIFFERS**.
*The difference.* S-44 defines the bass **inside L1** — *"every cue is defined over the **bass**, which
at a slice is the lowest sounding pitch of that slice's sounding set"* — while the outgoing statement
forbids this layer to select a bass at all.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that the specification state where the
bass is determined, since S-44 places it at L1 as a cue input and this text places it downstream. *(The
two are reconcilable — S-44's bass is read off the sounding set rather than selected by weighting —
and the proposal is that the specification say so rather than leaving the two texts to be read
together.)*

**Row 4.5 — collection, filtering and weighting are three responsibilities.**
*Statement.* "**Collection** (this layer): the facts …. **Filtering** (a distinct, explicit decision)
…. **Weighting** (a distinct derived layer): the pitch-class evidence + bass, computed as a *view*
over the collected notes — never replacing them." — §1 (locator: line 41).
*Derived.* S-15, S-18, S-33, S-49.
*Current-text axis.* S-15: **AGREES**. S-18: **AGREES**. S-33: **AGREES**. S-49: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried** — the derivation draws the same three lines: S-3 and
S-18 for the facts, S-15 for the filter, S-49 for the view published beside rather than instead.

**Row 4.6 — the module is organised by mechanism rather than by responsibility.**
*Statement.* "**NOT this layer, but living in the same module** (a decomposition smell …): the
segmentation sub-boundary detectors …, `findTemporalContext` …, `collectPitchContext` …. The module
header calls itself 'single source of truth for score-walking helpers' — i.e. it is organised by
*mechanism* (score-walking), not by *responsibility*." — §2 (locator: line 55).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* do those three co-located functions still
sit in that module, and does any of them still run on the arm that ships?

#### §3 — what the code did, as verified at the time

*Every row of this section describes the implementation as it stood when the document was written, so
every one is QUARANTINED. The derived statements are named where one speaks to the described
behaviour, because a DIFFERS here is what makes the audit question worth asking.*

**Row 4.7 — staff eligibility as coded.**
*Statement.* "A staff is eligible at a tick iff: it is **shown**, its instrument at that tick does
**not** use a **drumset** …, and it is **not a 'Chord Track' staff** …. So: hidden, percussion, and
chord-symbol staves are dropped" — §3.1 (locator: line 64).
*Derived.* S-15, S-20, S-2.
*Current-text axis.* S-20: **AGREES** on percussion. S-2: **AGREES** on the chord track. S-15:
**DIFFERS** on hidden staves, and on *dropped* rather than *flagged*.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does any live path still **drop** an
ineligible-staff note rather than carry it flagged?

**Row 4.8 — the backward sustain walk stops at a fixed four-whole-note cap.**
*Statement.* "**Backward sustain walk.** From the first segment at/after `startTick`, walk
**backward** while `segTick ≥ startTick − Fraction(4,1)`. `Fraction(4,1)` = **4 whole notes** …, a
**fixed cap**." — §3.2 (locator: line 71).
*Derived.* S-29.
*Current-text axis.* S-29: **DIFFERS** — S-29's sounding set is defined by onset and release with no
search bound, so a note held longer than the cap is in the set S-29 defines and absent from the one
this walk builds.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does any live path still bound the backward
search, and if so does it drop notes S-29's sounding set contains?

**Row 4.9 — the forward walk, and a legacy dense-start branch.**
*Statement.* "**Forward region walk.** Walk segments with `tick < endTick`. (If
`excludeLookAheadOnDenseStart` AND ≥3 PCs already sound at `startTick`, segments after `startTick` are
skipped — a **legacy batch-only path; the bridge leaves it OFF**.)" — §3.2 (locator: line 76).
*Derived.* S-28, S-29.
*Current-text axis.* S-28: **DIFFERS**. S-29: **DIFFERS** — skipping segments after the region's start
removes change points S-28 makes exhaustive.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the dense-start branch reachable on any
arm that ships?

**Row 4.10 — per-note filtering drops grace, silent and invisible notes.**
*Statement.* "**Per-note filtering.** Only `ChordRest`s that are chords and **not grace notes**; per
note, only those with `n->play()` **and** `n->visible()` (silent / invisible notes skipped). Rests
contribute nothing." — §3.2 (locator: line 79).
*Derived.* S-15, S-16, S-18, S-4.
*Current-text axis.* S-15: **AGREES** on the three conditions it shares. S-16: **AGREES** that a grace
opens nothing. S-18: **DIFFERS** — S-18 carries the excluded notes, this skips them. S-4: **DIFFERS**
— S-4 requires L0 to supply per-rest facts, this contributes nothing for a rest.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* are rests supplied to any live consumer as
S-4 requires, or does the surface still contribute nothing for them?

**Row 4.11 — the weighting ladder.**
*Statement.* "Base weight per note occurrence = `(durationInRegion / regionDuration) ×
beatWeight(beatType)`, where `beatWeight`: DOWNBEAT 1.0 · stressed 0.85 · unstressed 0.75 · sub-beat
0.5." — §3.2 (locator: line 82).
*Derived.* S-35.
*Current-text axis.* S-35: **DIFFERS** — S-35 publishes a metric strength **class** as an ordinal with
its level's period and refuses to fold it into a number, while this is a four-valued numeric ladder
folded straight into a weight.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does the shipped arm still weight by this
four-valued ladder, and is that the same quantity S-35's class is meant to publish?

**Row 4.12 — aggregation by pitch class.**
*Statement.* "**Aggregation by PITCH CLASS** into `accum[12]`: sums `totalWeight`,
`durationInRegion`; records the set of distinct onset ticks …, the **lowest** pitch + its tpc, a
per-tick voice count, and an `onsetAtRegionStart` flag" — §3.2 (locator: line 84).
*Derived.* S-33.
*Current-text axis.* S-33: **DIFFERS**, decisively — identity is the event set, not the pitch-class
set.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does any live consumer still receive
pitch-class accumulators in place of the event set?

**Row 4.13 — the repetition boost.**
*Statement.* "**Pass 2 — repetition boost:** `totalWeight ×= (1 + 0.3 × (distinctMetricPositions −
1))`." — §3.2 (locator: line 87).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the constant still in force, and was it
ever fitted?

**Row 4.14 — the cross-voice boost.**
*Statement.* "**Pass 3 — cross-voice boost:** `totalWeight ×= 1.5` if the PC is sounded by `>1` voice
at some tick." — §3.2 (locator: line 88).
*Derived.* S-33.
*Current-text axis.* S-33: **DIFFERS** — a doubling is a change of the event set in S-33 and a weight
multiplier here.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* same as Row 4.13.

**Row 4.15 — the sustain-pedal tail is driven by actual pedal markings.**
*Statement.* "**Pass 4 — sustain-pedal tail:** **driven by actual pedal markings** …. For a note whose
written end is inside the region under an active pedal, adds a **discounted** tail-weight … for the
span from note-off to pedal release." — §3.2 (locator: line 89).
*Derived.* S-54.
*Current-text axis.* S-54: **DIFFERS** — S-54 keeps the notated release whatever pedal mark spans it
and publishes a PEDAL-HELD attribute instead, naming the extend-the-release alternative as OQ-3;
the outgoing text extends the sounding weight to the pedal lift.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does a live path still extend a note's
weight to the pedal lift, which S-54 makes an open question and does not decide?

**Row 4.16 — the weights are normalised to sum to one.**
*Statement.* "**Normalise** all PC weights to sum to **1.0**." — §3.2 (locator: line 93).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the normalisation still applied, and
does any consumer read the un-normalised weight?

**Row 4.17 — bass selection with a passing-tone floor.**
*Statement.* "**Bass selection.** Bass PC = the **lowest pitch among PCs whose weight ≥
`bassPassingToneMinWeightFraction` × total`** …; falls back to the absolute lowest if none clears the
floor." — §3.2 (locator: line 94).
*Derived.* S-44.
*Current-text axis.* S-44: **DIFFERS** — S-44's bass is *"the lowest sounding pitch of that slice's
sounding set"*, with no floor and no weighting, and S-44 names the proxy hazard it accepts.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* which bass does the shipped arm use, and
does any cue or gate read a floored bass where S-44 specifies the lowest sounding pitch?

**Row 4.18 — the output is one entry per sounding pitch class.**
*Statement.* "**Output:** a `vector<ChordAnalysisTone>` with **one entry per sounding pitch class**
(≤12)." — §3.2 (locator: line 97).
*Derived.* S-33, S-50.
*Current-text axis.* S-33: **DIFFERS**. S-50: **DIFFERS**.
*PROPOSED DISPOSITION.* **QUARANTINED**, with Row 4.12.

**Row 4.19 — a second, divergent collection semantics.**
*Statement.* "`buildTones` converts those to `ChordAnalysisTone` **one-per-note** (no weighting …).
… **It is a second, divergent collection semantics** (per-note + unweighted) vs `collectRegionTones`
(per-pitch-class + weighted)." — §3.3 (locator: line 105).
*Derived.* S-50.
*Current-text axis.* S-50: **DIFFERS** — S-50 publishes one output surface and names it exhaustively.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* do two collection semantics still coexist,
and which does the arm that ships read?

**Row 4.20 — the reach, summarised.**
*Statement.* "It reaches **backward** (pre-region sustains) **and forward within the region**; it does
**not** reach forward past `endTick`. … The backward cap is the fixed `Fraction(4,1)` = 4 whole notes
in **both** collectors." — §3.4 (locator: line 111).
*Derived.* S-29, S-53.
*Current-text axis.* S-29: **DIFFERS** (as at Row 4.8). S-53: **AGREES** that the span is the caller's.
*PROPOSED DISPOSITION.* **QUARANTINED**, with Row 4.8.

#### §4 — the findings the document records about that code

**Row 4.21 — the layer conflates three responsibilities.**
*Statement.* "**The layer conflates THREE responsibilities …** As built it does *collection* +
*filtering* + *weighting/aggregation* in one pass …. These are factual, decisional, and interpretive
jobs respectively; merging them is what forces the information loss …, the silent dropping …, and the
divergent paths." — §4.0 (locator: line 117).
*Derived.* S-15, S-18, S-33.
*Current-text axis.* S-15: **AGREES**. S-18: **AGREES**. S-33: **AGREES** — the derivation separates
the same three.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* are the three still merged in one pass on
any live path?

**Row 4.22 — it drops rather than collects-and-annotates.**
*Statement.* "It *identifies* grace notes … and discards them, and likewise discards `!play()`,
`!visible()`, and ineligible-staff notes. Discarding is a filtering decision, not collection — and it
is irreversible information loss" — §4.1b (locator: line 124).
*Derived.* S-18, S-16.
*Current-text axis.* S-18: **AGREES**. S-16: **AGREES** — both require the excluded note to be
published rather than dropped.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the loss still present on any live path?

**Row 4.23 — it turns the score into pitch-class evidence and discards the notes.**
*Statement.* "`collectRegionTones` collapses every note into ≤12 per-pitch-class accumulators.
Register beyond 'lowest per PC' is dropped, **voice identity** is dropped …, **individual
onsets/offsets and tie structure** are dropped …, and **spelling (tpc) is kept only for the lowest
occurrence** of each PC." — §4.1 (locator: line 131).
*Derived.* S-3, S-13, S-23, S-33.
*Current-text axis.* S-3: **AGREES** that those facts are required. S-13: **AGREES**. S-23:
**AGREES**. S-33: **AGREES**.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* which of the four dropped facts is still
unavailable to a live consumer?

**Row 4.24 — the backward reach should be until silent, not a fixed cap.**
*Statement.* "Correct behaviour is to walk back to each voice's actual onset (until the voice is
genuinely silent), not a magic horizon." — §4.2 (locator: line 143).
*Derived.* S-29.
*Current-text axis.* S-29: **THE DERIVATION IS SILENT** on the search, as at Rows 1.5(ii) and 3.26.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Rows 1.5(ii), 3.26 and 3.53 — this is
the fourth independent place in the outgoing record where the no-horizon rule is stated and the
derivation does not carry it.

**Row 4.25 — there is no forward reach, and progression context lives elsewhere.**
*Statement.* "The layer is region-bounded with no anticipation/cross-region forward read; 'what comes
next' is answered downstream …. If we decide a region needs wider context …, today there is no single
place to extend the reach — it is split across layers." — §4.3 (locator: line 146).
*Derived.* S-53.
*Current-text axis.* S-53: **AGREES** that the extension decision is the consumer's.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the reach still split across layers with
no single place to extend it?

**Row 4.26 — two divergent collection semantics risk drift.**
*Statement.* "One layer should have one collection contract; the two paths risk drift (the exact
failure mode the module was created to end)." — §4.4 (locator: line 154).
*Derived.* S-50.
*Current-text axis.* S-50: **AGREES**.
*PROPOSED DISPOSITION.* **QUARANTINED**, with Row 4.19.

**Row 4.27 — the module is multi-responsibility.**
*Statement.* "Segmentation sub-boundary detectors, temporal context, and key-pitch context share the
file with tone collection. The layer's single responsibility is blurred by co-location" — §4.5
(locator: line 157).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED**, with Row 4.6.

**Row 4.28 — the evidence weighting is a stack of unvalidated heuristics.**
*Statement.* "The repetition boost …, cross-voice boost …, the four `beatWeight` values, the
pedal-tail multiplier, and the bass passing-tone floor are hardcoded constants that materially decide
what counts as chord evidence …. None is validated against this layer's own oracle …; they are
inherited heuristics, not measured choices." — §4.6 (locator: line 161).
*Derived.* S-35, S-44, S-48, S-52.
*Current-text axis.* S-48: **AGREES** in discipline — S-48 declares its own window UNESTABLISHED and
refuses to assert a value. S-52: **AGREES** — a provisional item may not be put under load. S-35:
**DIFFERS**. S-44: **DIFFERS**.
*PROPOSED DISPOSITION.* **RELOCATED — to L2, *the tonal reading, the one entangled decision***. What
counts as chord evidence, and with what weight, is L2's; the establishment discipline the sentence
appeals to is already carried at S-48 and S-52 and travels with the relocation rather than being lost.

**Row 4.29 — a legacy branch and an unread surface.**
*Statement.* "`excludeLookAheadOnDenseStart` is a legacy batch-only branch left OFF in production — a
divergent path that should be confirmed dead and removed or justified. `[unverified]`: I have not
re-read `buildPedalWindowIndex`, `safeBeatType`, or the preference *values*" — §4.7 (locator: line
167).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the legacy branch dead at the current
commit, and were the three unverified items ever read?

#### §5 and §6 — the proposed target design and the correctness oracle

**Row 4.30 — collection is pure, lossless and one path; nothing dropped, nothing aggregated.**
*Statement.* "**COLLECTION (this layer) — pure, lossless, ONE path.** Output the **note set**: every
sounding note in the region, each annotated with … the *flags* …. **Nothing is dropped** … and
**nothing is aggregated or weighted.**" — §5 (locator: line 175).
*Derived.* S-3, S-18, S-33.
*Current-text axis.* S-3: **AGREES**. S-18: **AGREES**. S-33: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 4.31 — reach until silent, not to a fixed cap.**
*Statement.* "**Reach until silent, not to a fixed cap.** Within collection, walk back to each voice's
true onset …. Any forward/context reach is an explicit named capability, not a magic horizon." — §5
(locator: line 182).
*Derived.* S-29, S-53.
*Current-text axis.* S-29: **THE DERIVATION IS SILENT**. S-53: **AGREES** on the named-capability half.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, with Row 4.24.

**Row 4.32 — filtering is separate, reversible and inspectable.**
*Statement.* "**FILTERING (a separate, explicit decision).** A thin step that reads the collection's
annotations and decides which notes are eligible …. It is *reversible* (it selects, it does not
destroy) and *inspectable* (the dropped notes remain in the collection)." — §5 (locator: line 185).
*Derived.* S-15, S-18.
*Current-text axis.* S-15: **AGREES**. S-18: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried** — S-15 is exactly this step, and S-18 is exactly its
reversibility.

**Row 4.33 — weighting is a separate derived layer, a view and never a replacement.**
*Statement.* "**WEIGHTING (a separate derived layer).** From the filtered notes, compute the
pitch-class evidence, the weights …, and the bass — as a **view over the note set, never a
replacement.** Its heuristics become tunable parameters validated against an oracle, not hardcoded
magic." — §5 (locator: line 188).
*Derived.* S-33, S-49.
*Current-text axis.* S-33: **AGREES** on view-not-replacement. S-49: **AGREES**.
*PROPOSED DISPOSITION.* **RELOCATED — to L2, *the tonal reading, the one entangled decision***, with
Row 4.28.

**Row 4.34 — the module gains a single responsibility.**
*Statement.* "**Single responsibility for the module.** Move the segmentation detectors, temporal
context, and pitch context out into their own layers; this file becomes collection only." — §5
(locator: line 191).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED**, with Rows 4.6 and 4.27 — it names a code move rather than a
rule of the analysis.

**Row 4.35 — the open sign-off question on the granularity of filtering and weighting.**
*Statement.* "*(Open question for sign-off: are Filtering and Weighting separate layers, or is this
layer 'collection + annotation' with Filtering/Weighting as the immediately-downstream layers 1b/1c?
Either is consistent with the separation — the user decides the granularity.)*" — §5 (locator: line
194).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL** — an unanswered sign-off question on a document whose own
banner records that the sign-off never happened and that the concern was absorbed elsewhere.

**Row 4.36 — this layer's correctness is judged against the score, not against the annotations.**
*Statement.* "This layer is upstream of key and chord, so its correctness is judged against the
**score**, not DCML/music21: does it collect exactly the notes a human reading the score would say
sound in `[start,end)` …, with bass and weights that faithfully reflect the notation?" — §6 (locator:
line 199).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT** — the derivation states falsifiers per statement and
names no grading oracle.
*PROPOSED DISPOSITION.* **RELOCATED — to *the measurement of the analysis*** (NOT A LAYER):
*"Metric definitions, grading conventions and what counts as ground truth are the measurement layer's
own design content."* **It is a substantive rule and the relocation is not a way of setting it
aside** — it is the same rule the record already carries as a standing grading convention.

**Row 4.37 — completeness is all note cases handled, enumerated.**
*Statement.* "Completeness = all note cases handled (sustains past the cap, ties, tuplets, grace,
cross-staff, multi-voice unisons, pedal, invisible/non-playing)." — §6 (locator: line 201).
*Derived.* S-15, S-16, S-18, S-23, S-54.
*Current-text axis.* S-23: **AGREES** (ties). S-16: **AGREES** (grace). S-18: **AGREES**
(invisible/non-playing). S-54: **AGREES** (pedal). S-15: **DIFFERS** — the derivation's eligibility
list reaches neither **tuplets**, **cross-staff** notes nor **multi-voice unisons** as named cases.
*The difference.* This enumeration names eight note cases a complete L0 must handle; S-15's five
conditions and S-3's fact list between them name five of the eight and are silent on tuplets,
cross-staff notes and multi-voice unisons — the last of which is exactly what S-33's slice identity
turns on.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that this eight-case completeness list
be carried into L0 as the check its own statements are tested against. **This row is the second place
in this comparison where the outgoing text supplies something the derivation lacked**, the first being
Row 3.60.

**Row 4.38 — the per-event metric does not cover this layer.**
*Statement.* "the per-event tiered metric does **not** cover this layer." — §6 (locator: line 203).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **RELOCATED — to *the measurement of the analysis*** (NOT A LAYER), with Row
4.36.

#### The banner

**Row 4.39 — the responsibility this document designs is now the note model's.**
*Statement.* "The single responsibility §1 states — collect every sounding note in a stretch of music,
annotated, losslessly, by one path — **is now the lossless note model's**" — the status banner
(locator: line 6).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL** — a status.

**Row 4.40 — the sign-off never happened; the design was superseded by absorption.**
*Statement.* "This document was put to the user for sign-off and its §7 checkboxes were never ticked;
what happened instead is that the design was superseded by the note model absorbing the role." — the
status banner (locator: line 9).
*Derived.* None.
*Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL** — an event.

---

#### Not a statement — listed so the arithmetic closes (6)

1. The banner's filing decision — "**Why it was ruled NOT delegated rather than delegated late:** a
   delegation here would create a SECOND home for a concern that already has one, which principle #6
   forbids" — *a filing decision about this document*.
2. The banner's register pointer — "Its two register entries — D-569 and D-570 — keep the class
   `gap`" — *provenance*.
3. The **provenance block** — "every 'currently does' statement below is from a source read this
   session of `…regiontonecollector.{h,cpp}` and `regiontoneprimitives.cpp` at HEAD `edd33901ed`" —
   *provenance and a commit identifier*.
4. §1's revision note — "*(The original §1 conflated collection with weighting/bass — corrected here
   per the user's three review comments …)*" — *provenance*.
5. §2's **IN this layer** list of three function names — *implementation locators*.
6. §7's five sign-off checkboxes, none ticked — *a sign-off form*, whose unticked state is rowed as
   Row 4.40.

#### The arithmetic at this document

- Statements: **40** (rows 4.1 to 4.40; no row of this document splits).
- Listed under *not a statement*: **6**.
- **Every outgoing statement carries exactly one disposition, and none carries two.**
- **UNPLACED rows at this document: 0.**

| Disposition | Count | Statements |
|---|---|---|
| ADOPTED — carried | 5 | 4.1, 4.2, 4.5, 4.30, 4.32 |
| ADOPTED — proposed | 5 | 4.3, 4.4, 4.24, 4.31, 4.37 |
| RELOCATED | 4 | 4.28, 4.33, 4.36, 4.38 |
| QUARANTINED | 23 | 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12, 4.13, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21, 4.22, 4.23, 4.25, 4.26, 4.27, 4.29, 4.34 |
| DISCARDED | 0 | — |
| HISTORICAL | 3 | 4.35, 4.39, 4.40 |
| UNPLACED | 0 | — |
| **Total** | **40** | — |

**The column sums to 40, against 40 statements:** 5 + 5 + 4 + 23 + 0 + 3 + 0 = 40. **The arithmetic
closes at this document.**

#### The current-text axis at this document, counted at these rows

| Verdict | Count |
|---|---|
| AGREES | 43 |
| DIFFERS | 20 |
| THE DERIVATION IS SILENT | 13 |
| **Total verdicts** | **76** |

#### What this document's rows put in front of the user

**Twenty-three of its forty statements are QUARANTINED**, and that is the document doing its job
rather than failing one: §3 and §4 are a verified description of code and a list of findings about it,
which is exactly the class the phase definition reserves for the audit. The two rows worth reading
now are the ones that run **towards** the derivation rather than against it. **Row 4.37** supplies an
eight-case completeness list — sustains past a cap, ties, tuplets, grace, cross-staff, multi-voice
unisons, pedal, invisible and non-playing — of which the derivation names five and is silent on
tuplets, cross-staff notes and multi-voice unisons; the last is precisely what S-33's slice identity
turns on, so its absence is not decorative. **Row 4.24** is the fourth independent statement of the
no-horizon rule in the outgoing record, and the derivation carries it in none of the four places.

---

### 6.5 — Document 5: `cowork_layer1_extend_design.md`

> **Manifest for this document.** Outgoing statements: **42** (rows 5.1 to 5.42). Listed under *not a
> statement*: **4**. Counted at this document by this session.
>
> **Why this document is in the population:** named by Ruling 32 item 2. It is **not** in the ruled
> specification document set, and stays in the population by name.
>
> **What this document is about, and why the derivation is silent so often.** Its whole subject is
> **enlarging the span of music the analysis holds** — building over a selection and extending it on
> request. The derivation touches that subject at exactly one statement, S-53, which fixes the working
> span as the only thing a caller supplies beyond L0 and says nothing about changing it. So this
> document is the largest single source of **ADOPTED — proposed** rows in the comparison so far: it
> states a contract the derived specification does not have.

---

**Row 5.1 — both operations this document designs are built.**
*Statement.* "**AS-BUILT — BOTH OPERATIONS THIS DOCUMENT DESIGNS ARE BUILT.**" — the status banner
(locator: line 3).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL** — a build state.

**Row 5.2 — it implements the supplier side of the bounded-context contract.**
*Statement.* "Implements the supplier side of the bounded-context contract … at Architectural Layer 1:
build the note model over the **user's selection**, and **extend** the loaded span on request." — the
banner (locator: line 13).
*Derived.* S-32, S-53.
*Current-text axis.* S-32: **AGREES**. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 5.3 — the hard part is isolated behind a byte-identical interim so the contract lands first.**
*Statement.* "the genuinely hard part (the look-up index under extension) is isolated and **deferred
behind a byte-identical interim**, so the *contract* lands first and the layers above are written
against it immediately." — the banner (locator: line 16).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL** — a delivery plan.

#### §1 — what is there now, verified at source

*Every row of this section describes code as it stood, so every one is QUARANTINED.*

**Row 5.4 — the build walks the whole score.**
*Statement.* "`NoteModel::build(const Score*)` — **walks the whole score** (every staff, voice,
segment, grace), resolves ties, annotates each note, sorts by onset …. One whole-piece build." — §1
(locator: line 20).
*Derived.* S-16, S-32.
*Current-text axis.* S-16: **DIFFERS** — the walk takes in grace notes, which S-16 excludes from the
change-point set and from every sounding set. S-32: **DIFFERS** — the build is whole-piece where S-32's
list covers the working span.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the whole-piece walk still the live
build, and does it still take grace notes into the same list?

**Row 5.5 — the note list is the lossless store.**
*Statement.* "`m_notes` — the onset-sorted `NoteEvent` list (the lossless store)." — §1 (locator: line
22).
*Derived.* S-3, S-18.
*Current-text axis.* S-3: **AGREES**. S-18: **AGREES**.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the store still lossless in the sense
S-18 requires — every excluded note present and labelled?

**Row 5.6 — the look-up index is static and built once.**
*Statement.* "`NoteQueryIndex` — the look-up index, **static, built once** from `m_notes` … a
**max-release segment tree**, a *perfect binary tree* sized to a power of two, built once" — §1
(locator: line 23).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED**, with Rows 3.45 and 3.55.

**Row 5.7 — the two queries and their predicates.**
*Statement.* "Queries: `overlapping(t0,t1)` (`onset < t1 && release > t0`, no horizon) and
`onsetIn(t0,t1)`." — §1 (locator: line 27).
*Derived.* S-29.
*Current-text axis.* S-29: **AGREES**, and exactly — S-29's sounding set is *"the set of eligible
events whose onset is at or before t and whose release is after t"*, which is this predicate at a
point rather than over a span.
*PROPOSED DISPOSITION.* **QUARANTINED**, the section being a description of code. *Audit question:*
does the live predicate still use strict `<` on the onset and strict `>` on the release, which is what
makes it S-29's half-open convention rather than the closed alternative?

**Row 5.8 — what makes extension non-trivial.**
*Statement.* "the note list must stay **onset-sorted** as notes are added at the **front** … or
**back** …, and the index is a **static perfect-binary-tree** that does not natively accept
insertions." — §1 (locator: line 29).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* does the live index still require a full
rebuild on every enlargement?

#### §2 — the API change, which the document calls the contract

**Row 5.9 — build over a selection, recording the loaded span and the selection span.**
*Statement.* "**`build` over a selection** — given the score and a **selection span** …, build the
note model holding the notes the selection needs …. The model records its **loaded span** … and the
**selection span**" — §2 (locator: line 35).
*Derived.* S-32, S-53.
*Current-text axis.* S-32: **AGREES**. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 5.10 — telling output slices from context slices is the layers-above's concern.**
*Statement.* "(so the layers above can tell output slices from context slices — though that labelling
is their concern, not Architectural Layer 1's)" — §2 (locator: line 37).
*Derived.* S-53.
*Current-text axis.* S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried**, with Row 2.28.

**Row 5.11 — extend grows the loaded span by a requested tick amount.**
*Statement.* "**`extend(direction, amount)`** — grow the loaded span **earlier** or **later** in time
by the **requested amount, expressed in ticks**" — §2 (locator: line 39).
*Derived.* S-53.
*Current-text axis.* S-53: **THE DERIVATION IS SILENT** — S-53 fixes the span and never contemplates
changing it.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.** *The proposal:* that L0 carry an enlargement operation
at all, the derived contract having none.

**Row 5.12 — the layer is unit-blind: it knows ticks, not slices or bars.**
*Statement.* "Architectural Layer 1 is **unit-blind** — it knows ticks, not slices or measures — so
the requester converts its own natural unit to a tick target before calling" — §2 (locator: line 40).
*Derived.* S-3, S-53.
*Current-text axis.* S-3: **AGREES** that positions are the supplied unit. S-53: **AGREES** that the
caller owns the choice.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, with Row 5.11: that the enlargement's unit be stated
as the position, with conversion the requester's.

**Row 5.13 — the finest meaningful step is the change point.**
*Statement.* "The **finest meaningful step is the change-point/slice**: within a slice the sounding set
is constant, so a sub-change-point (beat/tick) extension loads no new note and changes no analysis —
requesters never ask finer than that." — §2 (locator: line 42).
*Derived.* S-29.
*Current-text axis.* S-29: **AGREES** on the ground — the sounding set is constant across a slice.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Rows 1.18 and 1.20; this is the third
statement of the same rule in the outgoing record.

**Row 5.14 — loading is append-only.**
*Statement.* "Loading is **append-only** (never drop a loaded note)." — §2 (locator: line 44).
*Derived.* S-18.
*Current-text axis.* S-18: **AGREES** in spirit — nothing is dropped — but S-18 is about excluded
notes, not about enlargement, so the append-only property itself is not carried.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, with Row 3.35.

**Row 5.15 — it returns the new span and a boundary flag.**
*Statement.* "Returns the **new loaded span** and a **boundaryReached** flag (true when clamped at the
score start/end)." — §2 (locator: line 44).
*Derived.* S-32.
*Current-text axis.* S-32: **THE DERIVATION IS SILENT** — S-32 marks events at the span's edges and
says nothing about reporting that the score's own edge was reached.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, with Row 3.35.

**Row 5.16 — re-requesting a covered span is a no-op.**
*Statement.* "Re-requesting an already-covered span is a **no-op** (idempotent)." — §2 (locator: line
45).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **ADOPTED — proposed.**

**Row 5.17 — extend does exactly one step and never evaluates a stop condition.**
*Statement.* "**`extend` does exactly one requested step** — it loads what it is asked for and returns;
it does **not** loop, and it **never evaluates a stop/convergence condition** (that is inference, which
Architectural Layer 1 does not do)." — §2 (locator: line 46).
*Derived.* S-51, S-53.
*Current-text axis.* S-51: **AGREES** — evaluating a convergence condition would be exactly the kind of
claim S-51's test excludes. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 5.18 — the queries are unchanged and operate over whatever is loaded.**
*Statement.* "**Queries unchanged** … — they simply operate over whatever is currently loaded." — §2
(locator: line 49).
*Derived.* S-29, S-53.
*Current-text axis.* S-29: **AGREES**. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 5.19 — the decision, the increment, the stop test and the loop live in the requester.**
*Statement.* "The decision to extend, the **increment size**, the **convergence/stop test**, and the
**extend → re-infer → re-check loop** all live in the **requesting layer**, never here (single
responsibility …)." — §2 (locator: line 50).
*Derived.* S-53.
*Current-text axis.* S-53: **AGREES**, and on the same ground.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 5.20 — the increment is a per-call parameter, not a fixed constant of this layer.**
*Statement.* "The increment is the requester's natural inference scale …, so it is a per-call
parameter, not a fixed Architectural-Layer-1 constant." — §2 (locator: line 53).
*Derived.* S-48, S-52.
*Current-text axis.* S-48: **AGREES** in discipline — a value not established is not asserted. S-52:
**AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, with Row 5.11.

#### §3 to §5 — the delivery split, the capture rule, and the index

**Row 5.21 — Phase 1a is the contract with a correct, byte-identical interim.**
*Statement.* "**1a — the contract, with an interim that is correct and byte-identical.** … internally
may still walk the whole score and retain the notes overlapping the loaded span, and rebuild the
static index …" — §3 (locator: line 60).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL** — a delivery increment.

**Row 5.22 — Phase 1b is the efficiency, deferred.**
*Statement.* "**1b — the efficiency, byte-identical, DEFERRED (can land after L4).** … **Gate:**
byte-identical to 1a, and `index ≡ linear scan` over extended spans." — §3 (locator: line 67).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL** — a deferred increment with its gate.

**Row 5.23 — the split corrects the foundational assumption now.**
*Statement.* "This split means the **foundational assumption is corrected now** (everything above is
written to build-selection + extend) while the genuinely tricky code is done later under a
byte-identity gate." — §3 (locator: line 71).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL.**

**Row 5.24 — the model must hold every note overlapping the loaded span, sustained-in included.**
*Statement.* "The loaded model must hold **every note whose span overlaps the loaded span** — `onset <
loadedEnd && release > loadedStart` — which includes a note that **started before `loadedStart` and
sustains into the selection** (it really sounds during the selection; it is content, not mere
context)." — §4 (locator: line 76).
*Derived.* S-29, S-32.
*Current-text axis.* S-29: **AGREES**, exactly — this is S-29's predicate over a span. S-32:
**AGREES** — S-32's *entered sounding* case is this same note.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 5.25 — in the interim the capture is free.**
*Statement.* "**In 1a (interim)** this is free: the whole-score walk sees every note; filtering by
overlap keeps the sustained-in ones automatically." — §4 (locator: line 79).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL.**

**Row 5.26 — a span-scoped walk must find the active note without re-introducing a horizon.**
*Statement.* "a span-scoped walk must additionally find, at `loadedStart`, the note active in each
track … **without** re-introducing the old backward horizon and **without** walking from the score
start." — §4 (locator: line 81).
*Derived.* S-29.
*Current-text axis.* S-29: **THE DERIVATION IS SILENT** on the search that finds the set.
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* has the span-scoped walk been built, and if
so does it find every sustained-in note without a horizon?

**Row 5.27 — sustained-in capture is a different need from reach-back.**
*Statement.* "Distinguish this from **reach-back** (Architectural Layer 3): reach-back loads notes
*entirely before* the selection as **key evidence**; sustained-in capture loads notes that *sound
inside* the selection. Different needs, same supplier mechanism." — §4 (locator: line 85).
*Derived.* S-32, S-53.
*Current-text axis.* S-32: **AGREES** — S-32's *entered sounding* mark exists to draw exactly this
line. S-53: **AGREES**.
*PROPOSED DISPOSITION.* **ADOPTED — carried.**

**Row 5.28 — the interim rebuilds the index on every build and extend.**
*Statement.* "**1a:** **rebuild** `NoteQueryIndex` from the merged onset-sorted `m_notes` on every
build and extend …. Simple, correct, and identical to a fresh build over the enlarged span." — §5
(locator: line 90).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the rebuild still what runs?

**Row 5.29 — the deferred options, to be chosen on measurement.**
*Statement.* "**1b (deferred) options**, to be chosen on measurement, all byte-identical to the 1a
rebuild: a **merge + rebuild** …; or a segment tree sized with **headroom** …; or a different overlap
structure that accepts ordered insertion … — only if the rebuild proves a measured bottleneck." — §5
(locator: line 93).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL** — deferred options with their trigger.

**Row 5.30 — the interface is unchanged, so the choice is invisible above this layer.**
*Statement.* "The **interface is unchanged**, so the choice is invisible above Architectural Layer 1."
— §5 (locator: line 99).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the interface in fact unchanged across
the two implementations?

#### §6 — the invariants the document calls the correctness contract

**Row 5.31 — degenerate byte-identity.**
*Statement.* "**Degenerate byte-identity.** `build(selection = whole score)` and a never-extended model
are **byte-identical** to today's `build(score)` … (The corpus runs this path; it must not move.)" —
§6 (locator: line 102).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the degenerate path still byte-identical
at the current commit?

**Row 5.32 — build-then-extend equivalence.**
*Statement.* "**Build-then-extend equivalence.** `build(A)` then `extend` to span `X` yields a model
**identical** to `build(X)` directly — extension is an optimisation of 'load more, build fresh,' never
a different result." — §6 (locator: line 104).
*Derived.* S-53.
*Current-text axis.* S-53: **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, travelling with Row 2.21 — the L0 half of the same
equivalence the slicer states for itself, and the property that makes enlargement safe.

**Row 5.33 — append-only, no drop.**
*Statement.* "**Append-only / no-drop.** Extension never removes or alters an already-loaded note;
`m_notes` only grows." — §6 (locator: line 107).
*Derived.* S-18.
*Current-text axis.* S-18: **AGREES** in spirit, as at Row 5.14.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, with Row 5.14.

**Row 5.34 — the onset sort is preserved across front and back extension.**
*Statement.* "**Onset-sort preserved** across front (earlier) and back (later) extension." — §6
(locator: line 108).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED.** *Audit question:* is the sort invariant tested on both
directions?

**Row 5.35 — extend is idempotent and loads only the genuinely new notes.**
*Statement.* "**Idempotent extend.** Re-requesting a covered span is a no-op; overlapping requests load
only the genuinely-new notes once." — §6 (locator: line 109).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, with Row 5.16.

**Row 5.36 — extension clamps at the score edge and reports it.**
*Statement.* "**Boundary clamp + report.** Extension never passes the score start/end; it clamps and
sets `boundaryReached`." — §6 (locator: line 111).
*Derived.* S-32.
*Current-text axis.* S-32: **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, with Row 5.15.

#### §8 and §9 — the risks and the delivery

**Row 5.37 — sustained-in capture without a whole-score walk is the deferred correctness point.**
*Statement.* "**Sustained-in without a whole-score walk** — the 1b correctness point …; de-risked by a
read-only DOM spike before 1b, and irrelevant to 1a." — §8 (locator: line 123).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED**, with Row 5.26.

**Row 5.38 — the extensible index is the deferred performance point.**
*Statement.* "**The extensible index** — the 1b performance point …; irrelevant to 1a (rebuild)." — §8
(locator: line 125).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **QUARANTINED**, with Row 5.28.

**Row 5.39 — the result must not depend on how finely the span was enlarged.**
*Statement.* "**Determinism independent of extension granularity** — reaching span `X` in one big step
or several small ones must give an identical model (a required test; falls out of invariant 2)." — §8
(locator: line 126).
*Derived.* S-28, S-53.
*Current-text axis.* S-28: **AGREES** in discipline — determinism at exact positions. S-53: **THE
DERIVATION IS SILENT** on enlargement.
*PROPOSED DISPOSITION.* **ADOPTED — proposed**, with Row 5.32 — it is the property a consumer most
easily breaks, and the derivation carries nothing equivalent.

**Row 5.40 — enlargement and incremental re-analysis are different operations and must not interfere.**
*Statement.* "**Composition with re-analyse-a-sub-range** — extension (grow the loaded span) and the
existing incremental re-analysis (re-run part of it) are different operations on the same model; they
must not interfere." — §8 (locator: line 128).
*Derived.* S-53.
*Current-text axis.* S-53: **THE DERIVATION IS SILENT**.
*PROPOSED DISPOSITION.* **ADOPTED — proposed.**

**Row 5.41 — the Layer-1 specification marks extend designed-but-unbuilt.**
*Statement.* "The Architectural Layer 1 spec already marks *extend* designed-but-unbuilt and §11 as
interim behind this contract; on build, those become as-built" — §9 (locator: line 133).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL** — a statement about another document's build markers. *(Whether
it is true at the current commit is the audit's business; this document's own banner records that both
operations are built, and Document 3's §3 records `extend` as built, which a reader may set beside
it.)*

**Row 5.42 — Phase 1a is the buildable unit; Phase 1b is separate and deferrable.**
*Statement.* "**Phase 1a** (contract + interim) is the buildable unit now; **Phase 1b** (efficiency) is
a separate, byte-identical, deferrable step." — §9 (locator: line 136).
*Derived.* None. *Current-text axis.* **THE DERIVATION IS SILENT.**
*PROPOSED DISPOSITION.* **HISTORICAL.**

---

#### Not a statement — listed so the arithmetic closes (4)

1. The banner's **former status, preserved** — "**FORMER STATUS, PRESERVED (#12):** *'Status: DRAFT
   for sign-off. Read-only design — no code.'*" — *a preserved superseded banner*, whose supersession
   is rowed as Row 5.1.
2. The banner's account of why the correction was costly — "Every sibling design in this family carries
   an accurate as-built banner, which is what made this one costly" — *provenance about the document
   itself*.
3. §7's five test bullets — *a test plan*.
4. "Each is its own gated Claude-Code instruction; 1b gets the DOM spike first." — *a dispatch plan*.

#### The arithmetic at this document

- Statements: **42** (rows 5.1 to 5.42; no row of this document splits).
- Listed under *not a statement*: **4**.
- **Every outgoing statement carries exactly one disposition, and none carries two.**
- **UNPLACED rows at this document: 0.**

| Disposition | Count | Statements |
|---|---|---|
| ADOPTED — carried | 8 | 5.2, 5.9, 5.10, 5.17, 5.18, 5.19, 5.24, 5.27 |
| ADOPTED — proposed | 13 | 5.11, 5.12, 5.13, 5.14, 5.15, 5.16, 5.20, 5.32, 5.33, 5.35, 5.36, 5.39, 5.40 |
| RELOCATED | 0 | — |
| QUARANTINED | 12 | 5.4, 5.5, 5.6, 5.7, 5.8, 5.26, 5.28, 5.30, 5.31, 5.34, 5.37, 5.38 |
| DISCARDED | 0 | — |
| HISTORICAL | 9 | 5.1, 5.3, 5.21, 5.22, 5.23, 5.25, 5.29, 5.41, 5.42 |
| UNPLACED | 0 | — |
| **Total** | **42** | — |

**The column sums to 42, against 42 statements:** 8 + 13 + 0 + 12 + 0 + 9 + 0 = 42. **The arithmetic
closes at this document.**

#### The current-text axis at this document, counted at these rows

| Verdict | Count |
|---|---|
| AGREES | 25 |
| DIFFERS | 2 |
| THE DERIVATION IS SILENT | 26 |
| **Total verdicts** | **53** |

#### What this document's rows put in front of the user

**Twenty-six of the fifty-three verdicts at this document are SILENT, and that is the finding.** The
derivation has no contract for enlarging the span at all: it fixes the working span at S-53 and stops.
The outgoing text has a full one — append-only, idempotent, one step per call, clamp-and-report,
build-then-extend equivalence, determinism independent of how finely the span was enlarged, and the
rule that the requester owns the decision, the increment and the stop test. **Thirteen ADOPTED —
proposed rows come out of this one document**, and taken together they are a single proposal: that the
derived L0 gain an enlargement contract. Whether L0 should have one at all is the user's to rule; what
this document establishes is that the derivation does not have one and the current record does.

---

## 7. The derived side — one row per S-1 to S-54

**NOT YET WRITTEN.** This section is the same matrix as §6 read from the other side, and it can only
be written once every document of the population is tabulated: a derived statement's row must name
**every** outgoing statement that speaks to it, across the whole population, and the arithmetic check
the dispatch orders is that every AGREES and every DIFFERS in §6 appears here and the reverse. Writing
it over one document would state a completeness this comparison does not yet have.

## 8. The open questions OQ-1 to OQ-17

**NOT YET WRITTEN**, for the same reason: each open question is to be listed with one sentence on what
the outgoing text says about it, **with location**, or that it says nothing — and "the outgoing text
says nothing" is a claim over the whole population, not over one document of it.

## 9. The derivation's §7 — the five places the decomposition seemed wrong or incomplete

**NOT YET WRITTEN**, for the same reason as §8: each of the five points is to be answered against what
the outgoing text says, and that answer is a statement about the population as a whole.

## 10. The TRANSFER LIST — every RELOCATED row, by target charter

Gathered from the documents tabulated so far. **This list will grow as the remaining documents are
worked; it is not complete over the population.**

**To L3 — *the read-off facts*.**

- Row 1.21 — polyphonic phrase-boundary detection has no validated deterministic rule set in the
  literature, and this project's primitive may not be presented as established method.
- Row 1.22 — almost all published work on locating phrase endings addresses a single melodic line.
- Row 1.23(i) — carrying the monophonic cues over to polyphony is this project's own engineering.
- Row 1.24(i) — the gap cue generalizes cleanly to polyphony, a phrase boundary there being a
  near-simultaneous rest or long note across all voices.

**To L2 — *the tonal reading, the one entangled decision*.**

- Row 1.9 — the weighted pitch-class view: duration×beat, repetition, cross-voice and pedal weighting,
  pitch-class aggregation, and a weighted bass pick.
- Row 3.46 — the derived summary views as a class: deliberately lossy read-only summaries over the
  note model, the weighting and the bass pick among them.
- Row 4.28 — that the evidence weighting is a stack of unvalidated hardcoded constants that materially
  decide what counts as chord evidence.
- Row 4.33 — weighting as a separate derived layer: a view over the note set, never a replacement,
  with its heuristics becoming tunable parameters validated against an oracle.

**To *the measurement of the analysis* (NOT A LAYER).**

- Row 1.23(ii) — the primitive is validated against this project's own annotated corpus rather than
  cited.
- Row 1.24(ii) — a figure measured only on chorale texture is to be distrusted.
- Row 4.36 — an upstream layer's correctness is judged against the **score**, not against the DCML or
  music21 annotations.
- Row 4.38 — the per-event tiered metric does not cover an upstream layer.

## 11. The AUDIT QUESTIONS — every QUARANTINED row

Gathered from the documents tabulated so far. **Not complete over the population.**

1. Row 1.2 — does the note model read the score exactly once, and is the queryable surface it builds
   the one the change-point construction consumes?
2. Row 1.3 — do the five per-note facts S-3 requires and the eleven fields do not carry reach any
   consumer, and does `staffEligible` belong to L0's supplied facts or to an eligibility decision
   above it?
3. Row 1.4(ii) — do the three named engraving calls implement S-24's tie test, or do they merge links
   S-24 would refuse?
4. Row 1.7 — does the event lattice built from the tie-unresolved atoms place a change point at a
   notated tie boundary, which S-23 says is not one, and may a harmonic boundary be committed there?
5. Row 1.8 — is the additive surface still byte-identical on `notes()` at the current commit, and is
   that tested rather than asserted?
6. Row 1.10 — are both retained wrappers still live, and does either re-read the score rather than the
   note model?
7. Row 1.11 — does the point-in-time view include a note whose release equals the queried tick, which
   S-29 excludes over a slice?
8. Row 1.15 — are the recorded per-preset movements reproducible at the current commit on the arm that
   ships?
9. Row 1.16 — does the legacy reproduction mode still exist and still reproduce the prior set?
10. Row 2.3 — is the loaded-span clip still inert on the whole-score path at the current commit, and
    is that tested rather than asserted?
11. Row 2.7 — is the enumeration's measured cost the stated bound on the largest scores the record
    requires to be handled?
12. Row 2.24 — are the recorded suite and corpus figures the current ones, and do the suite sizes they
    name still exist at the current commit?
13. Row 3.9 — is a whole-score build in fact confined to the offline measurement path at the current
    commit?
14. Row 3.27 — is the stated cost bound met at the largest score the record requires to be handled?
15. Row 3.43 — does the borrowed score reference outlive the note model in every path that holds one?
16. Rows 3.45 and 3.55 — does the look-up index return exactly what a linear scan returns, in the same
    order, at the current commit, and is that tested rather than asserted?
17. Row 3.56 — the same measurement as audit questions 8 and 9 above, recorded a second time in a
    second document: are the recorded per-preset movements reproducible on the arm that ships?
18. Rows 4.6, 4.27 and 4.34 — do the three co-located non-members still sit in that module, and does
    any of them still run on the arm that ships?
19. Row 4.7 — does any live path still **drop** an ineligible-staff note rather than carry it flagged?
20. Rows 4.8 and 4.20 — does any live path still bound the backward search, and if so does it drop
    notes S-29's sounding set contains?
21. Row 4.9 — is the dense-start branch reachable on any arm that ships?
22. Row 4.10 — are rests supplied to any live consumer as S-4 requires, or does the surface still
    contribute nothing for them?
23. Row 4.11 — does the shipped arm still weight by the four-valued beat ladder, and is that the same
    quantity S-35's class is meant to publish?
24. Rows 4.12 and 4.18 — does any live consumer still receive pitch-class accumulators in place of the
    event set?
25. Rows 4.13, 4.14 and 4.16 — are the repetition boost, the cross-voice boost and the normalisation
    still in force, and was any of the three ever fitted?
26. Row 4.15 — does a live path still extend a note's weight to the pedal lift, which S-54 makes an
    open question and does not decide?
27. Row 4.17 — which bass does the shipped arm use, and does any cue or gate read a floored bass where
    S-44 specifies the lowest sounding pitch?
28. Rows 4.19 and 4.26 — do two collection semantics still coexist, and which does the arm that ships
    read?
29. Rows 4.21, 4.22 and 4.23 — are the three responsibilities still merged in one pass, is the
    information loss still present, and which of the four dropped facts is still unavailable?
30. Row 4.25 — is the reach still split across layers with no single place to extend it?
31. Row 4.29 — is the legacy dense-start branch dead at the current commit, and were the three
    unverified items ever read?
32. Row 5.4 — is the whole-piece walk still the live build, and does it still take grace notes into
    the same list as ordinary notes?
33. Row 5.5 — is the note store still lossless in the sense S-18 requires, every excluded note present
    and labelled?
34. Rows 5.6, 5.28, 5.30 and 5.38 — is the index still static and rebuilt whole on every enlargement,
    and is the interface in fact unchanged across the two implementations?
35. Row 5.7 — does the live overlap predicate still use strict `<` on the onset and strict `>` on the
    release, which is what makes it S-29's half-open convention?
36. Row 5.8 — does the live index still require a full rebuild on every enlargement?
37. Rows 5.26 and 5.37 — has the span-scoped walk been built, and if so does it find every sustained-in
    note without a horizon?
38. Row 5.31 — is the degenerate whole-score path still byte-identical at the current commit?
39. Row 5.34 — is the onset-sort invariant tested on both directions of enlargement?

**These are questions for the AUDIT phase. None is answered here, and none is an open-items row.**

## 12. The PROPOSALS — every ADOPTED — proposed row and every DIFFERS, each in one sentence, nothing
chosen

Gathered from the documents tabulated so far. **Not complete over the population.**

**Additions proposed to the derived specification.**

1. Row 1.5(ii) — that L0 state explicitly that what sounds at a moment is answered with no backward
   horizon.
2. Row 1.6(ii) — that L0 supply a per-staff analysis-eligibility fact, which the derivation's per-note
   eligibility test does not reach.
3. Rows 1.18 and 1.20 — that the specification state the change point as the finest meaningful
   enlargement of the working span, and record the bound as a consequence of the slice definition
   rather than as a settable value.
4. Rows 1.25, 1.27(ii) and 1.29 — that L0's supplied list gain stem direction by the route S-7 itself
   provides, and that the reading permission be stated as binding on any consumer.
5. Row 2.8 — that the eligibility predicate be stated once, over the union of S-15's five per-note
   conditions and the staff-level fact, since the two texts currently test different predicates under
   the same word.
6. Rows 2.13 and 2.20 — that the specification state which domain is published: the working span
   exactly, with a silent first slice where nothing begins at its start, or its intersection with the
   sounding material.
7. Row 2.15 — that the *entered sounding* and *cut by the span* marks S-32 requires be published
   beside the clipped slice list.
8. Rows 2.16 and 2.17 — that the specification state, once and explicitly, whether a grace note opens
   a change point. **The two texts give opposite answers.**
9. Rows 2.21 and 2.26 — that the re-slice equivalence property be stated, together with the
   prohibition on asserting that old slices stay byte-identical across an enlargement.
10. Row 2.25 — that the specification say whether the span's edge is a change point or an artificial
    boundary marked as such.
11. Row 2.27 — that the specification state whether a slice carries its sounding set or leaves it to
    be fetched from L0 by identity.
12. Rows 3.2 and 3.15 — the same per-staff eligibility proposal as items 2 and 5 above, met a third
    time; the hidden-staff case is reached by no derived statement in any of the three.
13. Rows 3.4 and 3.60 — that L0 state whether cue size survives as its own fact, **and** that the fact
    the outgoing text holds and the derivation lacks be stated: an imported score carries no cue
    distinction at all, which bears on OQ-4.
14. Row 3.5 — that eligibility have one home, it being currently defined across three documents.
15. Row 3.13 — that the specification state whether losslessness admits an exception for unpitched
    notes, S-20 declining to publish them and the outgoing text keeping every note.
16. Rows 3.26 and 3.53 — the no-backward-horizon rule, with the defense Row 3.53 carries.
17. Row 3.29 — that L0 state who owns staleness when the notated record changes under a built model.
18. Rows 3.31, 3.41, 3.42 and 3.48 — that the input list and the per-note fact list be stated at the
    width S-3 to S-7 require, the bar-relative position in particular, which S-34 and S-36 compute the
    metric-strength class from.
19. Row 3.35 — that the append-only and clamp-and-report properties of enlarging the span be stated.
20. Rows 3.44 and 3.57 — the grace question again, met at the build and at the risk register.
21. Row 4.3 — that the specification state whether a **clipped in-region duration** belongs in L0 at
    all, being a function of the caller's region rather than of the note.
22. Row 4.4 — that the specification state where the bass is determined, S-44 placing it at L1 as a
    cue input and this text placing it downstream.
23. Rows 4.24 and 4.31 — the no-horizon rule for the fourth and fifth time, here with the reach-until-
    silent form and its defense.
24. Row 4.37 — **that the eight-case completeness list be carried into L0** — sustains past a cap,
    ties, tuplets, grace, cross-staff, multi-voice unisons, pedal, invisible and non-playing — of
    which the derivation names five and is silent on tuplets, cross-staff notes and multi-voice
    unisons.
25. **Rows 5.11 to 5.16, 5.20, 5.32, 5.33, 5.35, 5.36, 5.39 and 5.40 — one proposal in thirteen
    parts: that L0 gain an ENLARGEMENT CONTRACT, which the derivation does not have.** Its parts, as
    the outgoing text states them: an enlargement operation at all; its unit stated as the position,
    with conversion the requester's; the change point as the finest meaningful step; append-only, so
    nothing already loaded is dropped or altered; the new span and a boundary-reached report returned;
    idempotence, so a covered request is a no-op; the increment a per-call parameter rather than a
    constant of the layer; build-then-extend equivalence, so enlarging equals building afresh at the
    enlarged extent; determinism independent of how finely the enlargement was taken; and
    non-interference with re-analysing a sub-range. **Whether L0 should carry such a contract at all is
    the user's to rule.**

**Differences stated, with nothing chosen between the two texts.**

1. Row 1.3 — the eleven as-built per-note fields against S-3's list: five facts S-3 requires are
   absent, and one field S-3 does not name is present.
2. Row 1.6(ii) — per-note eligibility (S-15) against staff-level exclusion.
3. Row 1.7 — S-23's "the intermediate notes open nothing" against a republication giving every tie
   continuation its own span.
4. Row 1.9 — S-33's event-set slice identity and S-44's lowest-sounding-pitch bass against pitch-class
   aggregation and a weighted bass pick.
5. Rows 1.25 and 1.27(ii) — S-7's exclusion of stem direction and S-9's bound on what L1 reads,
   against a licence to consume it.
6. Row 2.8 — S-15's five per-note eligibility conditions against a three-flag test carrying a
   staff-level fact S-15 does not name.
7. Row 2.10 — S-15's eligible-only sounding set and S-18's carrier beside the output, against an
   ineligible note riding inside each slice's own overlapping set. **UNPLACED.**
8. Rows 2.13, 2.20 and 2.25 — S-32's exact coverage of the working span, its silent first slice and
   its edge marks, against a domain clipped to the sounding material with an edge boundary the
   outgoing text calls artificial.
9. Row 2.15 — S-32's *entered sounding* / *cut by the span* marking against span clipping.
10. Rows 2.16 and 2.17 — S-16's *"A grace note opens no change point and belongs to no sounding
    set"* against *"a grace genuinely opens/closes a boundary by its span"*, with S-15's
    not-a-grace-note condition and S-30's no-zero-length-slice invariant riding on the answer.
11. Row 2.27 — S-50's published sounding set per slice against a slice carrying start and end only.
12. Rows 4.3, 4.7, 4.10, 4.11, 4.12, 4.14, 4.15, 4.17, 4.18, 4.19, 4.20 and 4.28 — twelve differences
    between the derivation and a **verified description of code as it stood**: the fixed backward cap,
    the dense-start skip, the dropping of grace, silent, invisible and ineligible-staff notes, rests
    contributing nothing, the four-valued beat ladder, pitch-class aggregation, the cross-voice
    multiplier, the pedal tail extending a note's weight to the lift, the floored bass pick, the
    per-pitch-class output, and two divergent collection semantics. **Every one is QUARANTINED rather
    than proposed**, because a description of code is the audit's business and not this comparison's.
13. Row 4.37 — S-15's five eligibility conditions against an eight-case completeness list naming
    tuplets, cross-staff notes and multi-voice unisons, which the derivation does not reach.

## 13. The distribution over the whole population

**NOT YET WRITTEN.** The per-document distribution for document 1 is at §6.1, with its arithmetic
discrepancy reported at the rows rather than reconciled. A distribution over the population is written
when the population is worked.

## 14. The derivation's independence record, relayed

**NOT YET WRITTEN.** The dispatch orders it relayed in its own section with no verdict word attached.
It is a relay of the derivation's §6 and is owed once, not per document; it is deliberately not
written here so that it is written whole rather than in pieces.

## 15. What the user is asked to rule in this file

**NOTHING.** The ruling on these dispositions comes separately, framed by the writing side as a
decision surface over these rows, one decision per turn. Nothing above is a recommendation about that
ruling.

## 16. What this file does NOT do

- **It applies no disposition.** Every one is a proposal. No outgoing text is edited, and the
  derivation is untouched.
- **It establishes nothing** (**#19**). Every verdict in it is this session's authored reading, and
  every one is re-placeable by the user at the two quoted texts.
- **It states no verdict on the derivation, on the deriving session's independence, or on the L0/L1
  split.**
- **It adjudicates nothing between a derived statement and the outgoing text.** A DIFFERS row is not a
  defect finding, is not an open-items row, and decides nothing — the phase definition reserves that
  to the audit.
- **It measures nothing about the analysis.** No measurement was built, designed, scoped or run for
  it; the comparison is textual throughout.
- **It is not complete over its population**, and §0 says exactly which documents are done and which
  are untouched.
