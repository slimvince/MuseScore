# Second-pass extract — row 3: Hentschel, Moss, McLeod, Neuwirth & Rohrmeier 2021, the unified chord model

> **STATUS: SECOND INDEPENDENT EXTRACTION (session 2 of the reading pass, 2026-08-31).**
> Written under `cowork_reading_pass_commission_2026_08_30.md` §4, per the independence protocol
> of `reading_pass/continuation.md` §2. **Neither `reading_pass/extracts/` nor
> `docs/research_papers/reading_pass_2026_08/` was opened for this paper before this file was
> written.** Read at its source, `https://apmcleod.github.io/pdf/mec-chord-model.pdf`, in two
> separately-prompted passes.
>
> **GRADE, DECLARED AT ITS FACE: RELAYED, not at-the-object** — the same web-fetch bound the other
> second-pass extracts carry. Session-and-prompt independence, not read-tool independence.

## Identity

Johannes Hentschel, Fabian C. Moss, Andrew McLeod, Markus Neuwirth & Martin Rohrmeier, "Towards a
Unified Model of Chords in Western Harmony", *Music Encoding Conference Proceedings 2021*
(proceedings published 2022).

## What kind of paper this is — stated first, because it governs everything below

**[FACT, established by a direct question] THE PAPER REPORTS NO MEASUREMENT OF ANY KIND.** No corpus
size, no conversion accuracy, no agreement figure, no performance metric. Its evidence is **four
qualitative case studies**. **So nothing in this row can supply a measured value to any design
point, and no figure may be quoted from it, because there are none.** What it can supply is a
representation design and the vocabulary for one.

## Claims, labeled

**[FACT] The problem it addresses is interoperability between annotation traditions, not analysis.**
Relayed verbatim: *"cross-stylistic and cross-theory comparisons are therefore even more difficult,
particularly in a large-scale computational setting that requires a common overarching
representation"*; and *"For our purpose of an overarching harmonic notation and encoding system …
it is necessary to have a unified representation for diverse harmonic practices."*

**[FACT] A chord is modelled as a GRAPH.** Relayed verbatim: the model *"represents chords as
graphs, where the chord label and its position in a piece form a central node, and properties of
the chord are given as labeled edges and attached nodes."*

**★ [FACT] THE THREE PITCH-CLASS TYPES ARE DISTINCT, AND THE CONVERSIONS BETWEEN THEM ARE
ONE-DIRECTIONAL.** The types: **GPC** (generic pitch class, *"A–G"*), **SPC** (spelled pitch class,
*"GPC plus accidentals"*), **EPC** (enharmonic pitch class, *"MIDI note number mod 12"*). The
governing sentence, verbatim: **"An SPC can be converted into an EPC or a GPC, but not vice
versa."** Three parallel interval types are defined the same way: **GIV** (*"the difference between
two GPCs, e.g., any 3rd"*), **SIV** (*"the difference between two SPCs, e.g., a major 3rd"*),
**EIV** (*"the difference between two EPCs, e.g., 5 semitones"*). **No line-of-fifths or TPC type is
part of the model as relayed.**

**[FACT] Mode is an ordered collection of specific intervals, and a key is that plus a tonic.** Mode
is represented as *"an ordered collection of SIVs"*; the paper names *"the combination of a mode and
a tonic pitch as a 'Key'"*. **So mode is not a label drawn from a fixed list — it is a collection,
and any collection is expressible.**

**[FACT] The abstraction levels, in the model's own order.** Score level — *"the set of pitches that
are taken from all the notes within the segment referred to by the chord symbol"*; pitch
equivalences (octave, enharmonic) applied to abstract away from the score; pitch classes as GPC /
SPC / EPC; **pitch functions**, where a pitch class is assigned a role; relative pitch classes,
expressed against a key or tonic; and chord functions and properties — key, chord type, inversion,
function.

**[FACT] Root and bass are PITCH FUNCTIONS carried by individual pitches; inversion is a separate
chord-level property.** Relayed: *"Other common pitch functions are, for example, root, bass note,
and leading tone"*, with inversion listed among chord-level properties as `INV := {0..N}`. **Root
and bass are therefore not derived from one another in this model — each is an attribute a pitch
carries.**

**[FACT] Chord-tone status is a pitch function too, and non-chord tones are marked rather than
removed.** Relayed verbatim: *"Each can be classified as either a chord tone or a non-chord tone.
The possibility of ignoring non-chord tones, such as suspensions or ornaments, is common to many
annotation standards."* Tones may carry functions such as **Suspension** and **Ornament**. The
paper develops no theory of altered or added tones beyond providing the slot.

**★ [FACT] WHAT IS LOST, AND IN WHICH DIRECTION — the model's own account.** SPC → EPC or GPC is
lossy and non-reversible: enharmonic equivalence erases spelling, and the generic reduction erases
accidentals. Score level → pitch-class set loses octave. **Relative ↔ absolute pitch classes
require the key, and the conversion loses information where the key is unknown.** The model
*"represent[s] only those harmonic properties that are explicitly included"* while *"inducing others
where possible (e.g., deriving scale degrees from root and key information)."*

**[FACT of absence] The paper does NOT state what an annotation must carry to be losslessly
convertible.** Asked directly: the dependencies are visible but the conversion rules are not fully
specified in this paper. **A reader wanting a lossless-round-trip guarantee will not find one
here.**

**[FACT] The four case studies and what each is for.** Corelli (1681) — one Dorian chord expressed
simultaneously as figured bass, Roman numeral, Riemannian function and absolute chord. Dvořák
(1893) — Riemannian and Tonfeld functions carried at once. A jazz example (R. Cole 1976) — implicit
pitches exceeding what the absolute chord label names. Gubaidulina (1988) — a post-tonal hexachord
with **no traditional root**, handled through a *"central tone"*.

**[FACT] There is a formal specification and a repository.** A BNF-like formal definition, a
comparison of several annotation standards and further example diagrams are in supplementary online
material; the code repository is cited as `https://github.com/DCMLab/chord-model` (accessed 12
January 2022). **This second pass did not open the repository** — that would be a separate act and
is not one this pass is licensed to take as design input.

**[FACT] Stated scope, verbatim:** *"While the model may not be exhaustive, its general and flexible
nature ensures its extensibility: Its only requirement is that 'chord' in the sense of a collection
of pitches is a meaningful concept in this style."* The stated limit follows from it: traditions
where pitch collections are not meaningful chords are outside the model.

**[CONJECTURE / stated aim, not a result]** A move towards *"a generalized standard for virtually
all harmonic phenomena"*, the paper framing itself as *"a first step towards this goal."* **No
specific future work is stated.**

## Coupling facts (the commission's mandatory widening)

**ASSUMES upstream:** chord labels from some annotation system (figured bass, Roman numerals,
absolute chord syntax, Tonfeld and others) and, where available, score-level pitches. Key and mode
*"may or may not be provided"*, and the model tolerates their absence at the cost of the
relative-pitch-class level. Its one hard requirement is that a chord — a collection of pitches — is
a meaningful object in the style at hand. **It assumes an analysis has been made; it does not make
one.**

**HANDS downstream:** a queryable graph carrying whichever levels the source annotation populated,
plus whatever can be induced from them, and conversions between annotation standards. **Not all
levels are populated for every input** — the model's own point is that different theories specify
information at different levels — so a consumer must handle a partially populated graph rather than
assume a full one.

**ITS OWN STATED SCOPE:** a representation and encoding model. It performs no inference, decides no
chord, finds no boundary, estimates no key, and grades nothing.

## Bearing, flagged for the findings surface (verdicts are Task 4's, not this file's)

- **DP-L and §7 data design** are the row's admitting subjects and this paper is squarely about
  them: the three-type pitch-class hierarchy with **one-directional** conversion, and the
  pitch-function level at which root, bass and chord-tone status are attributes of a pitch rather
  than fields of a chord label.
- **A structural observation worth carrying, stated as an observation and not a verdict:** this
  model puts **chord-tone status at the same level as root and bass — a function a pitch carries,
  attached to the chord's graph** — rather than as a separate downstream annotation. That is a
  representation choice, not an inference claim, and it says nothing on its own about *when* the
  assignment is decided. **It must not be read as evidence for or against DP-D**, whose question is
  where in the inference the assignment happens; a later reader tempted to enlist it either way
  should note that this paper measures nothing and infers nothing.
- **Mode as an ordered SIV collection** is a concrete alternative to a fixed mode list, and bears on
  the mode question the disposition surface raises at rows 9–11.

## What this extract does NOT establish

- The contents of the supplementary material or the repository (neither opened).
- Whether the model has been adopted by any corpus or tool since.
- What `N` bounds in `INV := {0..N}`.
- How the *"central tone"* of the post-tonal case is defined.
- **Nothing here is at-the-object.** Every quotation is relayed, and there are no figures to relay.

*Provenance: second pass of the reading pass, 2026-08-31. Read at the source URL only. No
specification derived, no document amended, no code opened, no register touched.*
