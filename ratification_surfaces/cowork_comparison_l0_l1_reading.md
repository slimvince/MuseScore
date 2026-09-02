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
| 3–29 | the remainder of the population, in the artifact's order | **UNTOUCHED** |

**UNTOUCHED means untouched, not partly worked.** Nothing in documents 3–29 has been read for
tabulation, quoted, counted or dispositioned, and no row for any of them exists anywhere. The next
dispatch resumes at **position 3**, `cowork_layer1_note_model_design.md`.

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

**To *the measurement of the analysis* (NOT A LAYER).**

- Row 1.23(ii) — the primitive is validated against this project's own annotated corpus rather than
  cited.
- Row 1.24(ii) — a figure measured only on chorale texture is to be distrusted.

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
