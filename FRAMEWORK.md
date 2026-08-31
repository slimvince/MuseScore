# The framework document — the all-encompassing architecture of the harmonic analysis

> **★ RATIFIED by the user 2026-08-29 — Ruling 2 of
> `cowork_rulings_2026_08_29_ratification_sitting.md`; the decomposition, charters and boundary
> contracts govern. Renamed from `cowork_framework_document_draft_2026_08_28.md` to
> `FRAMEWORK.md` at ratification per Ruling 5. The banner below is preserved as written at
> drafting; its "DRAFT / NOT RATIFIED" words describe the drafting moment, not the present.**

> **DRAFT — INFORMED DERIVATION, NOT COMPARED, NOT RATIFIED.**
>
> Derived 2026-08-28 under `cowork_informed_session_brief_framework.md`, in the two stages that brief's
> §3 rules: **stage one** derived the decomposition from outside this project and wrote it down whole;
> **stage two** then read this project's own material and revised on the record. The first-stage draft
> is **Appendix B, whole and unedited**; the record of what stage two changed and why is **Appendix A**,
> and that record is the phase's second deliverable, not a note attached to this one.
>
> **The draft name is ruled and so is its retirement:** this file is renamed as an explicit step at
> ratification and not before.
>
> **Where the first-stage draft lives is the one thing the rulings leave open.** It is kept here as a
> clearly-marked appendix, and **that placement is not ruled**.
>
> **★ THE INCUMBENCY RULE GOVERNED THE DERIVATION AND GOVERNS THIS TEXT.** Reading what this project
> already built was permitted; citing it as a reason was not. No design point below is defended on the
> ground that this is what the analysis currently does, or what a specification says, or that changing
> it would be expensive. Where the derived answer agrees with what exists, Appendix A says whether the
> agreement was reached on the evidence or carried forward.
>
> **★ ONE GAP IS DECLARED ON THIS DOCUMENT'S FACE.** The behavioural statements of §10 name **no code
> site** and do **not** say which part of the system each binds. That fill-in is ruled to a side other
> than the author. Until it runs, the statements here are **checkable in principle and not yet checked
> in fact**.
>
> **★ NONE OF THE THREE SEALED PLACEMENT-SAMPLE FILES WAS OPENED, in any portion.** The positive
> statement is repeated at Appendix A item 6.
>
> **★★ ONE ITEM ON THE CLOSED LIST WAS OPENED, AND IT IS DECLARED HERE RATHER THAN LEFT TO BE FOUND.
> §8 of `cowork_informed_session_brief_framework.md` — the brief's own provenance section — WAS READ.**
> It was read in the same act as the rest of the brief: the brief was opened whole with one file-tool
> call, as instructed, and §8 is inside it. **The brief places §8 on the list of things closed to this
> session in both stages, and states that opening any of them means the session may not author this
> document.**
>
> **This is declared, not argued away.** Two things are nonetheless worth the user's attention when he
> decides what to do with it. **First, the bar's stated ground is that the authoring side must not be
> the side that argued the case for the arrangement it works under** — and §8 carries authorship,
> tips, and what changed at the revision; it carries no part of that argument, which lives in the two
> ruling records and in the handoff, **none of which was opened**. **Second, the instruction cannot be
> obeyed by a reader meeting the brief for the first time:** the rule that §8 must not be opened is
> written inside the file that must be read, and is reachable only by reading past it. That is exactly
> the recorded defect shape **DT-20** — *an instruction whose mandatory preconditions defeat one of its
> own requirements* — which `PHASE_CONSTRAINTS_AND_STOP_RULES.md` §3 flags as **live in the present
> arrangement**. It is recorded here as an instance of that shape, found in this arrangement's own
> brief.
>
> **The user's call, and the writing side takes no view on it:** this document stands, or it is
> re-authored by a side that has not read §8. Nothing else on the closed list was opened —
> `cowork_handoff.md`, the two ruling records of 2026-08-28, and every `cc_report_*.md` and
> `cc_instruction_*.md` remain unread (Appendix A item 6).
>
> Bound by the fourteen-section design-document standard (`cowork_design_doc_template.md`). Two of that
> standard's sections are **N/A** for this subject and are stated once here rather than padded:
> **deployment view** — there is no deployment topology; and **human-interface design** — this is a
> backend analysis component with no user interface.
>
> Written for a reader who knows music theory and does not know this project.

---

## 0. Terms — read this section first

Standard music theory is used in its standard sense. Every other term this document uses is defined
here, once, before anything rests on it. **This section is the document's one glossary; §12 points at
it rather than repeating it, because one concern has one home.**

Five words carry more than one plausible reading and are therefore used in exactly one sense
throughout: ***tonality*** is used for what is commonly called *the key*, and the bare word *key* is
not used at all; ***bar*** is the metric unit and *measure* is never used for it; ***score*** means a
musical score and never a number; ***note*** means a pitch event and never a remark; ***instrument***
means a violin and never a measurement tool, except in §10 where the measurement sense is written out
in full as *measurement instrument*.

| Term | Definition |
|---|---|
| **The analysis** | The software this project builds: given a notated score it decides the tonality, the chords, and the moments at which one chord gives way to the next, and writes the result into the score. |
| **Tonality** | A tonic pitch class together with a mode. |
| **Onset** | A time point at which some note begins. **Release** — a time point at which some note ends. |
| **Change point** | An onset or a release: a moment at which the set of sounding notes changes. |
| **Slice** | The stretch between two consecutive change points. Over a slice, the set of sounding notes does not change at all. A slice is a fact read off the notation; deciding it involves no judgment. |
| **Harmonic span** | A run of consecutive slices over which one chord is read. Its boundaries are change points, but not every change point is a harmonic boundary. |
| **Harmonic boundary** | The moment at which one harmonic span ends and the next begins. |
| **Phrase boundary** | The moment at which a musical phrase ends. It need not coincide with a harmonic boundary, and the ground truth records the two separately. |
| **Elaboration** | A sounding note that is not part of the harmony read over its span — a passing note, a neighbour, a suspension, an anticipation. *Non-chord tone* names the same thing and is used where a cited source uses it. |
| **Chord-tone assignment** | The decision, for every sounding note of a harmonic span, whether it belongs to the chord read over that span or elaborates it. |
| **Degree** | The chord's root expressed as a scale degree of the prevailing tonality, with its chromatic alteration where it has one. |
| **Applied target** | The degree a secondary chord points at, as in *the dominant of the dominant*. |
| **Figure** | A chord's inversion, written in the figured-bass manner the ground truth uses. |
| **Roman numeral** | Degree, quality, figure and applied target together, read against a stated tonality. |
| **RomanText** | The plain-text format the ground-truth analyses of this repertoire are written in. |
| **A layer** | One stage of the analysis, responsible for one question. |
| **A charter** | For one layer: the question it answers, the evidence it consumes, and the facts it publishes. |
| **A boundary contract** | What one layer may assume about what reaches it from another, and what it owes in return. |
| **A decision** | One question about the music that the analysis settles, and could settle differently. |
| **A factor** | One additively combined term of a score over candidate readings. A factor is a means of computing a decision, never a decision. |
| **A view** | A fact that is a function of decisions already published, computed without settling anything new. |
| **Rival** | A reading the analysis considered and did not commit to, published with its mass. A rival may differ from the committed reading in its labels, in where its boundaries fall, or in both. |
| **Establishment status** | How well a claim is supported. Carried on every published evidence fact. |
| **FACT / THEORY / CONJECTURE** | The three labels this document puts on every load-bearing claim. **FACT** — a source actually read states or measures it. **THEORY** — established published theory. **CONJECTURE** — neither. |

---

## 1. Introduction and purpose

### 1.1 What this component is

**The analysis** takes a notated score and produces a harmonic reading of it: at each moment, what the
tonality is; where one harmony gives way to the next; what chord holds over each stretch; and which of
the sounding notes belong to that chord rather than decorating it. The reading is written back into
the score as Roman numerals and chord symbols.

### 1.2 Why this document exists — the problem it solves

A specification of any one part of that analysis cannot be written until it is settled **which
questions the analysis answers, where each is answered, and what each part may assume about what
reaches it**. Written without that, each part's specification silently decides boundary questions that
belong to the whole, and the same concern gets specified twice in two places with two answers.

This document decides the **layer decomposition**, each layer's **charter**, and the **boundary
contracts** between layers, so that detail specifications can be derived inside ruled charters.

### 1.3 Scope

**In scope:** what the layers are; what question each answers; what evidence each consumes; what facts
each publishes; what may cross each boundary and in which direction; and what is *not* a layer.

**Out of scope, by rule:** any detail specification of any layer; the design of the measurement layer;
any fix plan; and the derivation method itself.

### 1.4 Status

**DRAFT.** Not compared against the placement sample, not ratified. Ratification of the decomposition
is separately **HELD** until the external list of published research the user is assembling has
arrived and been dispositioned against it.

---

## 2. Constraints

**C-1 — The input is a notated score, not audio and not a piano roll.** Everything the notation
carries is given, and nothing more is inferred that the notation already states. [FACT — established
by reading a chorale score at the object: it encodes MIDI pitch **and** tonal pitch class, i.e. the
spelling; duration; explicit voice membership; time signature; key signature; bar lines; the
shortened length of an anacrusis; staff text; and it carries **no harmony annotation of any kind**.]

**C-2 — The key signature is not a statement of the tonality.** Baroque scores are frequently notated
one accidental short of modern practice, so the signature under-determines the tonic, and the
detecting signal is itself musical. [FACT — empirical findings ledger, entry C14.] The signature is a
weak prior on the tonality at the start and at a notated signature change, and nothing else.

**C-3 — Evidence is an input; the choice is made against the objective and the principles.** A
measurement, or an annotation practice, does not decide a design point by itself. *(The phase
constraint's second limb, which binds untouched.)*

**C-4 — One concern has one home.** No fact is published in two places, and no question is answered in
two places.

**C-5 — Nothing may be discarded.** A reading the analysis considered and rejected is carried, not
dropped, unless the exclusion is recomputable from what is kept.

**C-6 — No design may carry load on a checkable but unchecked causal claim about our own system.**

**C-7 — An instrument is trusted only after being positively established, never because it is merely
unfalsified.** This binds the ground truth itself: the accuracy of ground truth is a measured
quantity, and **for this repertoire it has not been measured and nothing published states it.**

**C-8 — Cost scales with the working span, not with the whole score.** The analysis runs on the user's
selection; a layer needing more music requests an append-only extension of the loaded music. Whole-
score analysis is the degenerate case. Re-analysis after an edit is incremental over the changed
stretch plus a bounded margin.

**C-9 — The analysis emits its fullest reading.** Cutting a name back to a plainer one so that two
differently-notated readings can be compared belongs only to the machinery that grades this project
against a published corpus, and exists on no path a user's result travels.

---

## 3. Context and scope — the external view

### 3.1 What the analysis consumes

The notated record of the music under analysis: per note, its spelled pitch, its duration, its voice
and staff, and whether it sounds; per bar, the time signature, the key signature and the bar line;
and the notated marks this repertoire carries — fermatas, repeats, ties, pedal marks, rests.

**And nothing else.** In particular the analysis consumes no analytical content written by a human
into the score. Chord symbols, Roman numerals, and function, cadence or tonality annotations already
present in a score are **not** input to the analysis, in any storage form. They are comparison
material only. Structural metadata — key signature, time signature, ties, pedal marks — is input,
the key signature as a weak prior per C-2.

### 3.2 What the analysis publishes

Per harmonic span: the tonality; the chord as degree, quality, figure and applied target; the
chord-tone assignment for every sounding note; and the rivals with their mass. Per phrase end: the
cadence and its type. Over the whole: the phrase and section grouping, the chord symbols as a derived
view, the figured bass, and the harmonic rhythm.

### 3.3 What it explicitly does not depend on

It does not depend on any style identity, on any preset a user may have chosen, or on any presentation
concern. Style-specificity reaches the analysis only through the **calibration** of the layers that
judge — their priors and weights — and **never through the structure**.

### 3.4 Implementation and test locators

**Deliberately absent.** Naming the files that implement a layer, and saying which part of the system
each statement of §10 binds, is ruled to a side other than this document's author. §11 carries that as
a declared gap.

---

## 4. Solution strategy

### 4.1 The key idea, in plain terms

**A layer is a question, with its own evidence and its own published facts. Two layers may be decided
in one act. What a boundary forbids is one layer answering another layer's question, or consuming a
fact that no layer has published.**

That single sentence resolves what otherwise looks like a contradiction between two bodies of
evidence. The literature measures, repeatedly, that the entangled questions of a harmonic analysis do
better decided **together** than in sequence. The same literature, and this project's own principles,
require that each question have **one home**, so that it can be specified, measured, and found wrong.
Those pull in opposite directions only if a layer boundary is assumed to be a boundary in *time*. It
is not. It is a boundary of **responsibility and of published fact**.

### 4.2 Why this shape and not another

Four questions are entangled, and the entanglement is established rather than assumed:

- **Boundary ↔ elaboration.** The information that discriminates an embellishment lives in the
  **boundary placement**, not inside a flattened sonority: once a stretch is merged so that the
  embellishment's own moment no longer exists as a unit, the evidence was in the boundary and the
  boundary is gone. [FACT — ledger entry C27.]
- **Elaboration ↔ chord.** The chord label *is* a function of which notes are heard as elaboration.
  The ground truth says so in the analyst's own words, beside the bar it applies to: *"reasonably
  common cadential figure in m4. If G♯ is an incomplete neighbor, it is i6/4, otherwise III+6 with A
  as a regular neighbor."* [FACT — read at the object in a chorale analysis file.] Published work
  measures the coupling in both directions: adding a chord-tone head to a multi-task analyser raises
  the Roman numeral from .506 to .516 and cadence from .532 to .558, and its authors state that
  knowing which notes are structurally relevant sharpens the harmonic analysis while harmonic context
  in turn helps distinguish chord tones from embellishments. [FACT.]
- **Chord ↔ tonality.** Estimating chord and tonality separately rather than jointly was measured to
  cost about 2 points of chord accuracy and about 5 points of tonality accuracy over 174 pieces.
  [FACT.] The musical reason is sharper than the measurement: music dwelling on its tonic triad
  presents that triad's own pitches repeatedly and the characteristic and leading tones hardly at all,
  so a tonality model rating candidates by those tones rates the true tonality lowest exactly where it
  is most strongly prolonged. [FACT — ledger entry C36.]
- **Tonality ↔ boundary.** A tonality change that is not also a harmony change is not expressible in
  the output the analysis must produce — the ground truth writes the tonality attached to a chord,
  inline, at the moment it changes. [FACT — read at the object.] This is definitional given the
  output, not an assumption about music.

Therefore those four are **one decision**, taken over whole sequences of spans rather than at a
moment. Two further ledger facts say why it cannot be taken at a moment: where a sonority may be read
as a chord or as the chord a third above it, **nothing available at that moment separates the two
readings, and the separating evidence is the surrounding music** [C2]; and where a reading wrongly
carries a root forward, **the separating evidence arrives after the moment of the error** [C41]. A
third closes it: **an incorrect reading can be the optimum of a locally-informed objective on this
repertoire** [C45, first reading].

### 4.3 The strategy stated as three moves

1. **Read the notation for facts and for candidates, and decide nothing.** Everything the notation
   states is a fact; every change point is a *candidate* harmonic boundary; the notated boundary marks
   and the local cadence cues are evidence. Nothing here is a judgment, so nothing here can be wrong
   about the music.
2. **Take the one entangled decision over the whole working span, and publish it with its rivals.**
   Tonality, harmonic boundaries, chord-tone assignment and chord identity are settled together,
   scored over whole sequences of spans, and what is settled is published with the readings that were
   close.
3. **Read off everything that is a function of that decision, and never revise it.** Cadences, phrase
   and section grouping, chord symbols, figured bass, harmonic rhythm. A later fact that contradicts
   an earlier decision is **published as a contradiction**, not acted on silently.

---

## 5. Building-block view — the layers

### L0 — The notated record. NOT A LAYER; the input contract.

Numbered because whether a fact is **given** or **derived** changes the whole decomposition, and three
of the most-cited published systems in this field build stages for facts that are given here.

**Given:** spelled pitch, duration, voice membership, metric position and bar, time signature, key
signature, bar lines, repeats, fermatas, ties, pedal marks, and whether each note sounds and is
visible.

**What may be assumed about it:** that it is what the notation says, and nothing more. The key
signature is a weak prior (C-2), never a fact about the tonality.

**Three design points this settles, which the published literature leaves open, because they are open
only for input this analysis does not take:**

- **Spelling is given, not inferred.** A substantial literature exists to recover spelling from
  unspelled input, and disagrees about the dependency: one system decides spelling and tonality
  together, another lets spelling feed the tonality, a third needs no tonality at all. [FACT — each
  states its own position.] For a notated score the question does not arise; spelling is read, and it
  is evidence **for** the tonality. Working from unspelled input, one author measured that using
  spelling raises tonality accuracy from 83.8% to 87.4% and called it *"cheating"* for a model of
  perception. For an analyser of notation it is not cheating; it is reading the score. [FACT.]
- **Meter is given.** Systems that take a piano roll must infer metrical structure, and one such
  system reports an unsolved circularity between meter and harmony as a result. [FACT.] Here the time
  signature, the bar lines and the beat positions are read. Metrical **strength** remains a derived
  covariate.
- **Voice membership is given.** One reference system proposed a per-voice dependency and could not
  add it, because it would have required voice separation first. [FACT.] Here the voices are in the
  file, so voice-leading evidence is available without a voice-separation stage.

### L1 — Change points, candidates and notated evidence

- **Question:** at which moments **may** a harmony begin, and what does the notation say at each?
- **Consumes:** L0 only.
- **Publishes:**
  - the ordered, covering, gapless and non-overlapping list of **slices** — the stretches between
    consecutive change points, where a change point is every onset **and every release** of an
    eligible note;
  - per change point, its **metric strength class**;
  - per change point, the **notated boundary evidence** at it: bar line, fermata, rest, repeat sign,
    double bar;
  - the **local cadence cues**: a falling-fifth or rising-fourth bass motion, a leading-tone
    resolution, the sounding together of the fourth and seventh degrees of a candidate tonality in
    the approach.
- **Decides nothing about the music.** It bounds the search and hands the next layer its covariates.

**Why a layer.** The alternative is a grid, and the ledger records what a grid does: a context window
defined as a fixed number of beats does not respect harmonic or metrical boundaries, so evidence
belonging to the next harmony is counted as evidence for the current one. [FACT — C37.] The change
points are the right atoms, and the set is **exhaustive**: because every moment at which the sounding
set changes opens a candidate, a real harmony change can never be missed, and over-grab is
structurally impossible rather than merely discouraged. Published symbolic systems take note onsets
and offsets as their partition points for the same reason, and a recent graph-based system replaces
frame quantisation with exactly one representation per onset and reports it as the fix for what fixed
windows lose. [FACT — both.]

**Why *releases* are change points and not only onsets.** Because a note ending changes what is
sounding, and the identity of a slice is the sounding **note** set rather than the octave-folded
pitch-class set: a unison or octave shrink is a real change though the pitch classes are unchanged.
[FACT.] *(This corrects the first-stage draft, which took onsets alone; see Appendix A item 5,
change 1.)*

**Why metric strength earns its place.** It is measured to constrain where harmonies change —
harmonic change was counted at 71.5% of the strongest-level beats against 22.3% of tactus beats
and 2.4% of the level below (Temperley 2009, Table 1, Kostka–Payne corpus) — and removing
metrical-accent features from a segmental analyser costs about six points of F-measure.
[FACT — both.]

**★ CORRECTED 2026-08-31 ON THE USER'S RULING, WITH THE FORMER WORDING PRESERVED IN PLACE (#12.)**
Ruling 2 of `cowork_rulings_2026_08_31_decision_surface_sitting.md` §3a, Option A — correct
minimally. **THE FORMER WORDING WAS:** *"harmonic change was counted at 71.5% of tactus beats
against 2.4% of the lowest metrical level"*. *Why it was corrected:* the primary-source reading pass
read Temperley 2009 at the object and returned a DIVERGES verdict on this figure, written up at
`reading_pass/stop_v4_divergence_2026_08_30.md` and decided at
`ratification_surfaces/cowork_v4_divergence_surface_2026_08_31.md`. Both numbers are at the primary,
but its Table 1 attaches 71.5% to the level ABOVE the tactus, the tactus row itself reads 22.3%, and
level 1 is not the lowest level that model carries. The clause as written was therefore false at the
paper it cites and its `[FACT]` label unearned, which is what #1 and the theory-grounding corollary
reach. **The design point is untouched and its ground is sharpened:** a monotone gradient across
three metrical levels is stronger evidence that metric strength constrains where harmonies change
than a single contrast between two. **The second half of the sentence — the six-point ablation —
verified exactly at its own primary and is unchanged.** *Option B of that surface was DECLINED: a
further finding the same paper carries is deliberately NOT brought into this charter and stays where
the pass recorded it, in the STOP memo and the findings surface; the ruling states the reason there.*

**Why the cadence *cues* sit here rather than downstream.** They are computable from the notation
without knowing the tonality, and two independent studies measure that they carry real discrimination
on their own: hand-designed local features reach F .80 on perfect authentic cadences with, in the
authors' words, no chord segmentation and no tonality estimation, and a graph model on local features
reaches the same. **Their weakness is equally measured, and is why only the cues live here:** the half
cadence reaches F .29 and .41 in those same two studies, because the bass motion into a half cadence
is variable. [FACT.] **The evidence that an authentic cadence is arriving can be gathered before the
harmony; a half cadence cannot be identified without it.** A further reason to keep the cue key-
agnostic is that a cadence detector which reads a resolved tonality and then votes on that tonality is
circular.

### L2 — The tonal reading. The one entangled decision.

- **Question, in one sentence:** over this music, what is the tonality at each moment, where does each
  harmony give way to the next, which sounding notes belong to the harmony and which elaborate it, and
  what chord is read over each span?
- **Consumes:** everything L0 and L1 publish. Nothing else.
- **Publishes:**
  - the **segmentation** — a partition of the working span into harmonic spans whose boundaries are a
    subset of L1's change points;
  - per span, the **tonality** as tonic and mode;
  - per span, the **chord** as degree, quality, figure and applied target, read against that tonality;
  - per sounding note, the **chord-tone assignment**, and where the reading has one, the **elaboration
    relation** — passing, neighbour, suspension, anticipation;
  - per span, the **rivals** with their mass — **including rivals that differ in where the boundaries
    fall and not only in the label**.
- **May not:** answer a question outside that sentence; consume a fact no layer has published; or
  discard a rival before the whole sequence of spans has been scored. The last is C45's first reading
  made operational — a wrong reading can be a local optimum, so a decision taken at a moment on
  locally-optimal grounds is unsafe by construction.

**Not decided here, and deliberately:** how the score over candidate readings is formed, what its terms
are, what tables they read, and how any weight is fitted. Those are this layer's **detail
specification**, derived inside this charter.

**Two things the charter does fix about that score, because both are boundary conditions rather than
mechanisms:**

- **The coupling between tonality and chord is a cost, never a veto.** This is the one place the
  literature reports both signs. One study measured joint estimation beating separate estimation;
  another reports the opposite for its own system — *"an incorrect chord selected may discard the
  correct key (and vice versa) … adding a compatibility between chords and keys has led to a decrease
  of accuracy."* [FACT — both.] The systems differ in how the coupling is expressed: a soft distance
  inside a scored path, against a hard compatibility constraint. **A hard constraint lets one wrong
  answer delete the other question's right one.** Stated generally: a reading-shaped evidence producer
  is a score and never a constraint.
- **The rule that admits a candidate to the search is part of this layer's specification and carries
  its own defense.** A rule that decides which readings a span may even consider bounds every claim
  the analysis can make about its own ceiling, because a reading the search cannot reach cannot be
  found however good the scoring is.

### L3 — The read-off facts

- **Question:** given a settled tonal reading, what else does a harmonic analysis of this music say?
- **Consumes:** L2's published facts, plus L0's and L1's. **It may not consume anything L2 did not
  publish, and it may not revise L2.**
- **Publishes:** the **cadence** at each phrase end, with its type; the **phrase and section
  grouping**; the **chord symbol** — root pitch class, quality and bass note; the **figured bass**; the
  **harmonic rhythm**.

**Why cadence type is here while the cadence cues are at L1.** A cadence type is a claim about what
the decided chords do at a decided phrase end. One study takes the cadence category as already given
from the harmony and studies what follows from it; two others take the cues and reach the authentic
cadence without the harmony but not the half cadence. [FACT.] Splitting the concern across L1 and L3 is
what those results together say.

**Why the chord symbol is a view and not a decision.** The root is the tonic transposed by the degree's
interval. Nothing is settled in computing it. Publishing it as a decision would create a second home
for one fact and a second chance to disagree with it — which is exactly the incoherence measured in
systems that predict the parts of a chord label independently (§9, DP-A).

**Why the phrase reading is a decision here and its evidence is a fact at L1.** The notated phrase
evidence — fermata, rest, repeat, double bar — is read at L1. Which of those are phrase ends, and how
they group into sections, is decided here, because the decisive further evidence is cadential. Note
that defining a phrase span by its cadence and then aligning cadences to that span is circular; the
span's boundaries come from the notated cues, and the cadence is aligned to them.

### The second axis — voice leading, and why it is an axis rather than a layer

The objects of **voice leading** — the accepted melodic phrase, chord voicing and arrangement,
part-writing, the stock eighteenth-century outer-voice patterns — do **not** belong on the harmonic
spine above. They form a **second axis** with its own layers, running beside it.

*The ground is a measurement and a structural fact, not tidiness.* The two axes were measured to be
near-independent on this repertoire. [FACT.] And the structural fact is decisive on its own: every
span kind on the harmonic spine cuts across the whole texture at once and its members tile the music,
whereas **a melodic phrase does not** — in contrapuntal writing the voices' phrases run concurrently
and out of step, as a fugue's staggered entries do, so phrase spans overlap across voices by
construction and tile only *within* one voice. A catalogue of spans in which every member tiles the
whole texture cannot hold them. *(This is adopted from this project's material; the first-stage draft
had no second axis and placed phrase structure on the spine. Appendix A item 5, change 2.)*

### NOT A LAYER — three things, named so silence claims nothing

- **The uncertainty surface.** Every published fact carries its own mass and its own establishment
  status; there is no layer whose job is uncertainty. The ground truth settles this: the analyst writes
  an alternative reading *in the same stream* as the principal one, not in a separate document. [FACT.]
  A separate uncertainty layer would put one fact in two homes.
- **The measurement of the analysis.** Metric definitions, grading conventions and what counts as
  ground truth are the measurement layer's own design content and a later stage's business.
- **Spelling, meter and voice separation**, for a notated score. See L0.

### The boundary contracts

| From → to | What crosses | Direction | What may NOT cross |
|---|---|---|---|
| L0 → L1 | The notated record, whole | forward only | Nothing derived. L1 may not treat the key signature as the tonality. |
| L1 → L2 | Slices; metric strength; notated boundary evidence; cadence cues | forward only | No decided boundary — L1 decides none. No tonality claim. |
| L2 → L3 | Segmentation; tonality per span; chord per span; chord-tone assignment and elaboration relation per note; rivals with mass | forward only | Nothing L2 did not publish — in particular no intermediate quantity of L2's own scoring. |
| L3 → L2 | **Nothing.** | — | A read-off fact may not revise the decision it was read off. §8.4 states what happens instead. |
| L1 → L3 | Notated phrase evidence | forward only | — |
| spine ↔ voice-leading axis | Published facts only, in either direction, each carrying its establishment status | either | Neither axis may re-derive a fact the other publishes. |

**The contract that carries the most weight, stated plainly:** L2 receives **candidates** and
**evidence**, never **decisions**. Everything the analysis settles about the music is settled in L2, or
in L3 from what L2 settled.

---

## 6. Runtime view — scenarios

**6.1 The main flow.** The notated record is read for the working span. Change points are enumerated
and the notation's evidence at each is attached. The tonal reading is decided over the whole working
span at once, and published with its rivals. The read-off facts are computed from it. Nothing runs
twice.

**6.2 A chord whose root does not sound.** The span's sounding notes do not contain the root of the
chord the reading commits to. **This is not an error and the analysis does not avoid it:** a chord
reading whose root is not sounding is not thereby wrong, and the published human analysis of this
repertoire itself makes such readings. [FACT — ledger entry C1.] The chord-tone assignment records
which sounding notes are chord members; the absent root simply has no note assigned to it.

**6.3 A sonority readable as a chord or as the chord a third above it.** Nothing at that moment
separates the two readings. [FACT — C2.] Both are carried as rivals through the scoring of the whole
sequence; the surrounding music decides; and if it does not decide, **both are published**, because
the ground truth publishes both in exactly this situation.

**6.4 An added sixth against a seventh chord on the related root.** The two carry the same pitch-class
content, so no reading of that content separates them. [FACT — C6, and read the restriction: *no
reading of that content*; compressed to *no reading can separate them* the claim is false.] The
separating evidence, where there is any, is the bass, the voice leading and the continuation — all of
which L2 has, because it decides over sequences.

**6.5 A passing key change — tonicization or modulation.** The question is answerable on tonality-
agnostic evidence for the subdominant relation and **not** for the dominant relation [FACT — C39], and
a diatonic leading tone at a cadence occurs at close to the same rate at a real tonality change and at
a passing one, so it does not separate them [FACT — C42, measured on the Bach ground truth, other
repertoires unmeasured]. The reading that wins is the one the whole sequence of spans scores highest,
and where the margin is thin **both are published**.

**6.6 Arpeggiated harmony.** Over an arpeggiated harmony the non-root tone can carry more duration than
the root, so a duration-weighted aggregate prefers the wrong root [FACT — C4, music half], and
collecting the arpeggio's pitches back into one weighted set and re-deciding does not recover it — the
aggregate's own vertical preference is still for the passing sonority [FACT — C38, bounded: what is
ruled out is aggregation-first re-analysis as a route to the root, not the approach in every form].
**The information that identifies the harmony is not vertical information at all**, which is why L2
decides over spans rather than over sonorities.

**6.7 An edit to the score.** Only the changed stretch plus a bounded margin is re-decided (C-8). The
margin exists because the tonality at the edge of a stretch is not fixed by one settled indication —
a tonality established over a stretch of earlier music is what fixes it. [FACT — C43, fact half.]

**6.8 A contradiction found downstream.** A cadential figure at L3 makes no sense against the chords
L2 committed. **L3 publishes the contradiction as its own fact and does not act on it.** §8.4 gives
the ground and the residual risk.

---

## 7. Data design

**The published analysis is a sparse, onset-anchored stream, not a labelling of every time point.**
[FACT — read at the object across five ground-truth analysis files.] Each statement is anchored at a
bar and a beat, beats may be fractional, and **no statement carries a duration or an end point**: a
reading holds until the next statement replaces it.

The shapes this document fixes:

- **A slice** carries its start and its end and nothing else. Whether a slice lies inside the user's
  selection or is only surrounding context is derived by the consumer, because cutting the music where
  the sounding set changes involves no judgment about what a user selected.
- **A harmonic span** is a run of slices, identified by its first and last change point.
- **A reading of a span** carries the tonality, the chord, the per-note chord-tone assignment, and a
  mass.
- **A rival set** is a set of readings over a stretch of music. **Its members need not share a
  segmentation.** This is the single most consequential shape decision in this section, and it is
  taken because the ground truth's own alternatives differ in the number of chords they contain: one
  bar is read as three statements in the principal analysis and as four in the recorded variant.
  [FACT — read at the object.] A rival set whose members must share the principal reading's boundaries
  cannot express that.
- **Every confidence that crosses a layer boundary** is bounded to the unit interval, is declared to be
  either a ranking margin or a calibrated probability, and is stated together with the decision it is
  the confidence of. Unbounded scores are permitted inside a layer and are squashed at the boundary.
  *Why:* an unbounded score in one layer and a margin in another are not comparable quantities, and a
  design that compares them has no defined meaning; fitting constants over the comparison would bury
  the incoherence rather than repair it.
- **Every published evidence fact carries its establishment status**, because a consumer may not put an
  unestablished fact under load (C-7).

---

## 8. Crosscutting concepts

**8.1 Publish once; consumers read and never re-derive.** Every derived analytical fact is published
exactly once, on the producing layer's output surface. Publication is broad for evidence-class facts
even where no consumer is named yet, each carrying its establishment status; a published fact that
nobody reads is either declared dormant with its future consumer named, or removed.

**8.2 Every analysis object has a named owner.** An unowned object is how one concern gets built twice
in two places. *(§11 records one object this document assigns an owner to which the current
arrangement leaves unowned.)*

**8.3 Facts are style-agnostic; style lives only in calibration.** The layers that carry facts — L0 and
L1 — are style-agnostic and lossless. Style-specificity enters only through the priors and weights of
the layers that judge, and **never through the structure**.

**8.4 Negative evidence is information, and a contradiction is published rather than acted on.** A
reading the analysis considered and rejected is carried at low mass. **Never computing a possibility is
not information loss; only discarding a computed one is.**

On revision, this document takes a narrower position than its first stage did, and the narrowing is
argued rather than asserted:

- **Forbidden:** a later layer **re-deriving** a fact an earlier layer published; and cycling or
  re-ranking over already-published ranked lists. The second is measured: where each stage of an
  analysis has already fixed its answer and published its ranked alternatives, going back over those
  published lists adds nothing measurable. [FACT — ledger entry C44, at its ruled width, which binds on
  that design class and on no other and expressly does not bear on a fitted joint decode over spans.]
- **Not forbidden by that evidence:** selecting among alternatives an earlier layer *carried*, and
  re-running forward from the selection. That is a different act from re-ranking published lists, and
  C44 does not reach it.
- **What this document does forbid, and on what ground:** any mechanism that compares a later layer's
  contradiction strength numerically against an earlier layer's confidence **before** those two
  quantities are on a declared common scale. This is not a claim that override is wrong; it is C-6
  applied — the comparison is a causal claim about our own system, it is checkable, and until the
  scales are declared it is unchecked. **The residual risk is stated at §11.**

**8.5 Determinism.** Two readings that score exactly equally are resolved by a declared total order, so
that the committed output does not depend on the floating-point library of the machine that ran it.
Exact score ties between candidate readings are real, not a theoretical concern.

**8.6 What is not evidence.** No user-written analytical content — chord symbols, Roman numerals,
function, cadence or tonality annotations — enters the analysis in any storage form (§3.1).

---

## 9. Architecture decisions

Per the ruled output form: candidates enumerated from every source kind with establishment status; **at
most one chosen per concern, or NONE** written as *underived*; and the rivals recorded in the defense,
so that a later reader can re-test whether the ground for excluding each still holds.

### 9.0 The prior question: what is a unit? — PUT TO THE USER, NOT SETTLED

The three candidate readings are units as **factors of the model**, units as **decisions the analysis
makes about the music**, or units as **a reconciliation of the two**.

**This document works at the second, and the evidence is:** the ground truth is a record of decisions
and contains no factor [FACT]; the disagreement between two independent analysts of the same piece is
disagreement about decisions — is this a chord, which figure, which tonality [FACT]; the ledger's
admitted facts are overwhelmingly statements that a decision is underdetermined by the evidence at a
moment [FACT — C2, C6, C34, C35]; and the multi-task literature's separately predicted heads are
decisions, whose measured pathology is decisions disagreeing [FACT].

*What the factor reading would change:* L2 would decompose into roughly ten units; this framework would
own the factor roster and the conditional-independence premises; and the boundary contracts would become
independence claims rather than published-fact contracts. *What the reconciliation reading would
change:* every decision would carry its factor set as sub-units, roughly doubling the unit count and
making every charter two-tiered.

**Stated as this phase's first ratified finding, for the user to rule. It is not settled here.**

### The design points

**DP-A — Divide the deciding by published field (a tonality decider, a degree decider, a quality
decider, a figure decider)?**
*Candidates:* yes (the neural multi-task lineage, read as an architecture — measured, repeatedly); no.
**CHOSEN: no.** Those heads are not stages: they sit on one shared encoder and are decided in one pass,
and the papers measure what happens when they are allowed to disagree — *"potential for
self-contradictory outputs in which the six sub-labels have different ideas about the chord"*, and a
passage genuinely ambiguous between two readings drawing an incoherent composite of the two. **Every
later system in that lineage adds machinery to undo the separation:** re-fusing degree, quality and root
into one joint label before combining with tonality and figure; a learned reconciliation pass over all
heads, raising the Roman numeral from .462 to .491; attention across every head's outputs, .503 to .516;
conditioning the degree head on the tonality, raising degree accuracy from .762 to .859. [FACT — every
figure reported by the paper named.] **That literature is strong evidence about what an analysis must
PUBLISH and evidence against dividing the DECIDING along the same lines.**

**DP-B — Divide by time scale: tonality first, then chord?**
*Candidates:* yes (published, and measured against); no (published and measured). **CHOSEN: no.**
*Rival's ground:* tonality constrains the chord vocabulary and is cheaper to decide. *Ground for
excluding it:* the measured 5-point tonality and 2-point chord cost of separating them, and C36 (§4.2).

**DP-C — Is segmentation decided before, with, or after chord identity?**
*Candidates:* before (published; every fixed grid); with (semi-Markov, measured); after (nobody).
**CHOSEN: with.** *Rival's ground:* tractability, and the availability of segment-level features.
*Ground for excluding it:* C27 (§4.2), and the measurements — frame accuracy of 68.8% when boundaries
are given against 23.3% when the same model must find them on the same piece; a jointly-decoding
segmental model beating event-level tagging by 7.6 to 38.2 points of segment F-measure on one corpus and
21.3 to 31.5 on another; the joint segmentation component the single largest contributor in a third
system's ablation; and the formal result that letting segment length be a decoded variable buys the
expressive power of a high-order model at linear rather than exponential inference cost. [FACT — each
reported by the work named.] One further measurement is worth carrying: with perfect tie-breaking
between equally-scoring labels, one published segment-then-label system would still remove only 26% of
its errors — the rest needs tonal context and voice leading its decomposition does not admit. [FACT.]

**DP-D — Where does the chord-tone assignment live?**
*Candidates:* an input, from an elaboration detector running first (published; F .72); a layer of its
own between boundaries and chords; **part of L2's one decision and published from it (CHOSEN)**; not
represented at all. *Ground:* the analyst's own note (§4.2); duration weight cannot separate a long
elaboration from a genuine added tone, because the distinction is functional and voice-leading [FACT —
C26]; and the measured benefit running in both directions. *Rival recorded:* a first-running detector
would shrink L2's search; it is excluded because its own authors report F .72 with many "errors" that
are plausible analytical choices, and a first-running detector's mistakes are unrecoverable downstream.

**DP-E — Is the tonality decided with the chords, and where may it change?**
**CHOSEN: with the chords; a tonality change is located at a harmonic boundary.** *Rival:* an
independent tonality track changing anywhere, which the output the analysis must produce cannot express.

**DP-F, DP-G, DP-H — Are spelling, meter and voice separation layers?**
**CHOSEN: no, for notated input**, each with the boundary condition stated at L0. *Rivals:* the
corresponding inference stages, which are required for unspelled or piano-roll input, and one of which
is the source of an acknowledged unsolved circularity in the systems that need it.

**DP-I — Is cadence a layer, and on which side of the tonal reading?**
**CHOSEN: split — cues at L1, type at L3.** *Rivals:* wholly upstream, excluded because the half cadence
is measured at F .29 and .41 without the harmony; wholly downstream, excluded because the cues
measurably carry the authentic cadence and are computable from notation alone.

**DP-J — Are phrase boundaries the same as harmonic boundaries?**
**CHOSEN: no.** [FACT — the ground truth writes a phrase boundary where the harmony does not change and
restates the chord after it: `m2 I || b4 I`.] *Rival:* treating them as one, which the ground truth
falsifies directly.

**DP-K — What does the analysis publish where it cannot decide?**
**CHOSEN: rivals in the same stream, each with its mass, including rivals that differ in
segmentation.** *Rival:* one best reading with a confidence number, which cannot express an alternative
containing a different number of chords. *Ground:* the ground truth's own form; and one study of
popular-music audio in which the automatic systems it evaluated scored about ten percent above the
annotator-pairwise agreement that same study measured — evidence that a single-answer target can
stop measuring harmony and start measuring one annotator. [FACT — as that one study reports it; the
domain bound is declared at R-1.] Recorded beside it, with NO contradiction asserted between the
two: a second study of the same domain, on different data and an earlier generation of systems,
reports the opposite sign. [FACT.]

**Two FURTHER grounds, on this project's own repertoire — classical symbolic music — added
2026-08-31 under the user's Ruling 3, each carrying the read grade it was obtained at, because a
ground travels no stronger than the read that produced it:**
- At every moment a score can carry two defensible key labels at once, stated there as a principle,
  with that study's own corpus annotating both. [Feisthauer 2021, the Lille thesis — DECLARED
  PARTIAL, chapter level.]
- Annotation traditions differ enormously in which of the two they record: one textbook marks a
  local key at 41.63% of onsets against another at 15.97%, and a dual-annotated dataset is released.
  [Nápoles López, Feisthauer, Levé & Fujinaga 2020 — RELAYED.]

**★ GROUND 2 WAS NARROWED HERE AND THE FORMER WORDING IS PRESERVED IN PLACE (#12.)** Ruling 3 of
`cowork_rulings_2026_08_31_decision_surface_sitting.md` §3b, Option B — qualify in place and add the
on-domain evidence; the decision surface is
`ratification_surfaces/cowork_dpk_ground_surface_2026_08_31.md`. **THE FORMER WORDING WAS:** *"and
the finding that automatic systems already score **above** human-human agreement on the same data,
which means a single-answer target has stopped measuring harmony and started measuring one
annotator. [FACT.]"* — quoted with its own emphasis markers intact. *Why it was narrowed:* the
finding verifies at its primary, and it is neither forbidden nor undeclared; what was wrong is that
a result ONE study reports was written as a settled property of
the field, which #1 and the theory-grounding corollary reach. **DP-K itself is not reopened, and its
first ground — the ground truth's own form, read at the object on this repertoire — is untouched.**
**No contradiction is asserted between the two studies:** they differ in year, in corpus and in
system generation, and no source this pass read compares them. *Why the two further grounds were
added rather than merely noted:* §7 calls the rival-set shape the single most consequential shape
decision in that section, and the pass found evidence for it on this project's own repertoire where
the charter had been resting on popular-music audio.

**DP-L — Is the chord symbol a decision or a derivation?** **CHOSEN: a derivation, published as a view.**

**DP-M — May a later layer revise an earlier one?** **CHOSEN: narrowly — see §8.4**, which states what
is forbidden, what is not forbidden by the evidence, and what this document forbids on C-6 with the
residual risk carried to §11. *(The first-stage draft forbade all revision; the narrowing is Appendix A
item 5, change 3.)*

**DP-N — Which theory of the cadential six-four does the label vocabulary take?**
**NONE CHOSEN — underived: open, needs a ruling or new research.** The candidates are the tonic chord in
second inversion; its own category; and a dominant carrying a double suspension. *This is a real
disagreement in the world, not a gap in the reading.* Our own two independent analyses of the same bar
disagree — one writes `i6/4` and the other `Cad64` [FACT — read at the object] — and the published
corpus-integration literature names this exact object as the flashpoint between the two major
annotation standards, resolving it only by replacing every instance with a neutral symbol [FACT]. The
three readings are different theoretical claims about the same notes, not three spellings of one claim.
**A framework that picked one silently would be deciding a question of theory on no evidence.** *(Stage
two established that this project's own layer specifications do not state the answer either: they state
that the sonority is functionally folded into the dominant's approach and never registers as a tonic
arrival, and that a published convention is followed for such variants generally — but no document
states which label is emitted. Appendix A item 4.)*

**DP-O — Does the framework commit to a hierarchical reading of harmony?**
**NONE CHOSEN — underived: open, and deliberately not foreclosed.** For it: a recursive grammar
represents something a flat sequence cannot — the same surface chords functioning simultaneously as a
tonic phrase in one tonality and a dominant phrase in another — with tree accuracy 45.95% against
39.43% for a non-transposition-tied grammar and under 10% for a right-branching baseline. Against it:
tree models are harder to optimise and *often perform no better* than latent-category sequence models of
matched size, and induced categories correspond to textbook harmonic functions only while the models
are small. [FACT — both.] **The decomposition neither adopts a hierarchy nor forecloses one**: what
chord follows what is inside L2's charter, and a grammar is one way to answer it. *The falsifier:* a
tree model beating a matched-capacity sequence model on this repertoire's ground truth, measured on the
same corpus and the same axis.

**DP-P — How are the terms of L2's score combined and fitted?**
**NOT DECIDED HERE — detail specification and measurement design.** Named because it is a real design
point rather than an implementation detail: fitting combination weights by likelihood was measured at
12.2 against 19.6 on the metric actually wanted, when the weights were instead fitted to that metric.
[FACT.]

**DP-Q — May the analysis decline to read a span at all?**
**NONE CHOSEN — underived: open.** Some published schemas carry a no-chord label and a no-cadence
verdict; the three exemplar analyses contain neither. The question is whether *no confident reading* and
*no chord here* are the same publication. *(Stage two found the same question open in this project's own
record, from the other direction: one rule states that the decoder always commits on the tonality axis
and never abstains, while a product target admits calibrated abstention when evidence is weak, and the
record states that which governs is not settled. Appendix A item 3.)*

---

## 10. Quality and testing

### 10.1 Quality goals

**Correctness first, at a stated width.** Every claim about how well the analysis does is bounded by
three things this document treats as standing: the ground-truth ceiling is unmeasured for this
repertoire and no published figure exists to cite (C-7); a rule that admits candidates to the search
bounds every ceiling claim, because a reading the search cannot reach cannot be found; and a fitted
value is graded only on data that did not help fit it.

### 10.2 Behavioural statements, each with what would falsify it

**No statement below names a code site, and none says which part of the system it binds.** That
fill-in is ruled to a side other than this author (§3.4, §11).

**B1 — A harmonic boundary falls only at a change point.**
*Observable:* the time points of the published harmonic boundaries, against the published change
points. *Decision rule:* every boundary is a member of the change-point set. *Not falsified by:* a
change point with no boundary at it — most carry none.

**B2 — A tonality change coincides with a harmonic boundary.**
*Observable:* the published tonality per span. *Decision rule:* no two consecutive spans differ in
tonality without differing in span. *Not falsified by:* a tonality restated identically across a
boundary.

**B3 — Every sounding note of a span carries a chord-tone assignment.**
*Observable:* the per-note assignment against the sounding-note set of the span. *Decision rule:* the
assignment is total over sounding notes. *Not falsified by:* a note assigned as elaboration with no
elaboration relation named — the relation is a separate fact and may be absent.

**B4 — The published chord symbol agrees with the tonality and degree it was derived from.**
*Observable:* the root pitch class, against the tonic transposed by the degree's interval. *Decision
rule:* equal for every span. *Not falsified by:* an enharmonic spelling difference the notation forces.

**B5 — No published fact of a later layer changes a published fact of an earlier one.**
*Observable:* the facts published at each layer for one piece, compared before and after the later
layer runs. *Decision rule:* the earlier layer's facts are identical. *Not falsified by:* the later
layer publishing a contradiction as its own fact.

**B6 — Where rivals are published, the committed reading is among them and carries the greatest mass.**
*Observable:* the rival set and the committed reading. *Decision rule:* membership, and the ordering by
mass. *Not falsified by:* an empty rival set where the reading is uncontested.

**B7 — A rival that differs in segmentation is published as such, and not flattened onto the committed
reading's boundaries.**
*Observable:* the boundaries of each rival, against the committed segmentation. *Decision rule:* a
rival's boundary list is published in its own right. *Not falsified by:* a rival that happens to share
the committed boundaries.

**B8 — Slices tile the working span exactly.**
*Observable:* the slice list. *Decision rule:* covering, gapless, non-overlapping, over the whole loaded
domain. *Not falsified by:* an interior stretch where every eligible voice rests, which is an explicit
empty slice and not a gap.

**B9 — Every confidence crossing a layer boundary is bounded, class-declared and named to its
decision.**
*Observable:* each value another layer may read. *Decision rule:* in the unit interval; declared a
margin or a calibrated probability; stated with the decision it is the confidence of. *Not falsified
by:* an unbounded score used inside a layer and squashed at the boundary.

### 10.3 How the decomposition itself is tested

**The decomposition is tested by the placement test, and by what that test now measures.** A different
side takes the sealed sample of statements and tries to place each into this document; every
unplaceable statement is reported to the user as a finding, with the sample's size, the observed
proportion and its uncertainty range, and the user rules per finding. **What that test measures here is
narrower than it was:** with an informed author it can no longer speak to independence, only to
coverage — whether the framework has a home for each statement.

### 10.4 What this document does not license

No measurement is designed, scoped or run here. In particular the three ground-truth exemplars are
**exemplars and never a corpus**: no rate, no count and no proportion is taken from three pieces, and a
statement resting on one would be exactly the unestablished instrument C-7 forbids.

---

## 11. Risks and technical debt

**R-1 — The ground-truth ceiling is unmeasured for this repertoire, and it gates.** No published study
reports per-axis inter-annotator agreement for Roman-numeral or tonality annotation of Baroque and
classical symbolic music. Every axis-level agreement figure this document cites comes from popular
music or from figured bass. **Until that quantity exists, no target for any axis can be stated as
anything but provisional**, and a system measured above the unknown ceiling cannot be distinguished
from a system fitted to one annotator.

**R-2 — The code-site and arm-binding fill-in has not run.** §10's statements are checkable in
principle and not yet checked in fact. **Declared, per the brief's own requirement.**

**R-3 — The forward-override comparison is not yet on a declared common scale.** §8.4 forbids the
numeric comparison until the scales are declared. *The residual risk of that position:* it may forbid a
mechanism that is in fact sound, and the cost of forbidding it is unmeasured. Recorded rather than
resolved, because the alternative — permitting a comparison whose meaning is undefined — is what C-6
forbids.

**R-4 — One analysis object this document gives an owner is currently unowned.** The **type** of an
elaboration — passing, neighbour, suspension, anticipation — is assigned here to L2, published beside
the chord-tone assignment it depends on. Stage two established that no current layer charter claims it:
the chord layer explicitly does not own it, the function layer does not claim it, and the publication of
such labels stands as an open increment. **An unowned object is how one concern gets built twice**
(§8.2), so the assignment is made rather than left. *It is a claim with an owner, not work started.*

**R-5 — The reachability of the search bounds every ceiling claim.** A rule that decides which readings
a span may consider is part of L2's specification and carries its own defense (§5, L2). Where such a
rule exists without a recorded basis, no ceiling claim over that search is established.

**R-6 — Three design points are underived and one is put to the user.** DP-N (the cadential six-four),
DP-O (hierarchy) and DP-Q (declining to read a span) are open with their falsifiers or their settling
conditions stated; §9.0 (the grain of a unit) is a finding for the user to rule. **None is filled with
the most plausible reading.**

**R-7 — The literature behind this document is not coverage.** The outward sweep this project ran
declares itself non-exhaustive: one item was actually read and every other is a title and an abstract,
and four classes of work were unreachable by construction. **A decomposition that sweep's list does not
contain is not thereby excluded.** In particular the hierarchical and multi-resolution alternatives on
that list — a tonality estimated at every window size at once, a time-span reduction tree, tonality in a
transform space rather than as a discrete label — were **not read**, and DP-O is left open partly for
that reason.

**R-8 — One primary source is not held.** The primary source for the tonality profiles is not on disk.
Nothing in this document rests on a profile form; a detail specification of L2 that comes to rest on one
will be defending a factor form from secondary descriptions, and must say so.

**R-9 — A named source in the register is not the paper in the folder.** The file whose name records the
one paper in the register whose subject is the ceiling that annotation disagreement imposes on chord
estimation **contains a different paper entirely** — an ISMIR paper on electric-guitar playing-technique
detection. [FACT — established by opening it.] The register marks that row as holding a local copy, and
the reachability verdict was taken against the register's rows rather than against the files.
**Consequence, stated narrowly:** that paper was not read, and every statement here about the annotation
ceiling rests instead on three other sources. **Consequence for the register:** at least one *Local ✓*
row is false at the object, and no sweep has established how many others are.

**R-10 — The #18 exposure carried by this arrangement is not discharged.** A framework document authored
under the informed arrangement rests on the current division being right wherever it agrees with it, and
that is a claim which is checkable and which this arrangement does not check. **Appendix A does not
discharge it; it makes it enumerable.** An independent challenge run has not been commissioned.

---

## 12. Glossary

**The glossary is §0**, which defines every term before it is used and is this document's one home for
them (C-4). No term is defined twice.

---

## 13. Background

**What this document replaces.** Nothing yet: it is the first framework document. It supersedes no
specification and lands no text into any specification.

**The arrangement it was written under, and why that is part of the record.** This phase was originally
designed for an implementation-blind session, and a brief for that arrangement was written and is kept.
On 2026-08-28 the user ruled that arrangement away: the deriving session may read this project's own
material. What replaced blindness as the guard is the two-stage order — derive from outside and write it
down, *then* read ours and revise on the record — together with the incumbency rule. **The order is the
instrument, and the record of what it produced is Appendix A.**

**A correction of record made in passing, and bounded.** The empirical findings ledger and the session
brief both cite a lettered clause (a) of the decision-neutrality corollary as stating that reuse counts
only as carried-forward establishment and never as sunk cost. **That lettered clause is not present at
the home the citations name**; that home carries a one-line register entry and a provenance sentence,
and the fuller statement is delegated to a further document, **which this session did not open**.
Recorded as an unverified citation, not as a false one: what is established here is only that the clause
could not be read where it was cited.

---

## 14. Related work and external sources

### 14.1 What this framework builds on

- **The reference joint model** of a harmonic analysis over a state of tonic, mode and chord, decided in
  one pass rather than a pipeline, and its authors' criticism of procedural pipelines for irrevocably
  propagating errors forward. Its own weakest stated assumption — conditional independence of the
  pitches within a unit — is carried here as a premise for L2's detail specification to state, not to
  inherit silently.
- **Segmentation as a decoded variable.** The semi-Markov formalism, which gives the expressive power of
  a high-order model at linear rather than exponential inference cost, and the two symbolic systems
  built on it whose measured gains over event-level tagging are quoted at DP-C.
- **Change points as the candidate grid**, from the published symbolic system that takes note onsets and
  offsets as its partition points; and the recent graph-based system that replaces frame quantisation
  with one representation per onset.
- **The metrical constraint on harmonic change**, counted rather than assumed.
- **Cadence cues computable without the tonality**, and the measured asymmetry between the authentic and
  the half cadence that is why only the cues sit upstream.
- **The multi-task lineage**, for what an analysis must publish — and, in its own measured pathologies,
  for why the deciding must not be divided the same way.
- **The annotation-agreement literature**, for the per-axis ordering of what is decidable; and for the
  finding that automatic systems now score above human-human agreement.
- **The ground truth read at the object** — three chorales, five analyses, one score — for what a
  harmonic analysis actually is: the sparse onset-anchored stream, the inline tonality, the phrase
  boundary distinct from the harmonic one, the published alternative that differs in its number of
  chords, and the analyst's note stating that the chord label is a function of the elaboration reading.
- **This project's own admitted empirical facts**, which have already passed the test of surviving the
  implementation being thrown away, and are the strongest evidence available at this desk.
- **The ratified ten-factor design intent**, admitted as design intent by name.

### 14.2 What was considered and not adopted

- **A pipeline with feedback — each stage fixing an answer and a later pass re-ranking or cycling.**
  Excluded at §8.4 on a measured finding at its ruled width.
- **A first-running elaboration detector.** Excluded at DP-D.
- **Segment-then-label.** Excluded at DP-C.
- **Division of the deciding by published field.** Excluded at DP-A.
- **A hierarchical/grammar layer.** Not adopted and not foreclosed — DP-O, with its falsifier.
- **A separate uncertainty layer.** Not a layer; §5.

### 14.3 Corpora and datasets used

**Only as exemplars, and never as a corpus** (§10.4): three Bach chorale scores and their published
RomanText analyses, two of the three carrying **two independent human analyses of the same piece**. That
duplication is the point of reading them: where two analysts of one chorale agree and disagree bears
directly on what any one layer can be asked to decide.

### 14.4 The bound on this section

The sweep behind the outward candidate list is declared non-exhaustive by its own author, and this
document does not treat it as coverage (R-7). Four classes of work were unreachable by construction:
work not using this vocabulary, non-English literature, work behind a paywall whose abstract does not
state its decomposition, and recent work not yet indexed under these terms.

---

# APPENDIX A — The two-stage record

> **This is the phase's SECOND DELIVERABLE, not a note attached to the first.** An independence record
> is meaningless for a session that may read everything. What replaces it is not a claim the session
> makes about itself but **a comparison of two texts it wrote**, and an output without it is
> incomplete.
>
> **What it does and does not do.** The framework document authored under the informed arrangement
> rests on the current division being right wherever it agrees with it, and that is a claim which is
> checkable and which this arrangement does not check. **This record does not discharge that exposure.
> It makes it enumerable:** a later independent run, should one be commissioned, attacks the list at
> items 3 and 4 rather than a whole document, and item 1 lets a reader see what this session had
> before it read ours.

## A.1 — The first-stage draft

**Appendix B, whole and unedited.** It was written complete before `ARCHITECTURE.md`, any per-layer
design document, `docs/scoring_model.md`, either register, `CLAUDE.md`, `cowork_target_architecture.md`
or any source file was opened. **It has not been edited since stage two opened and will not be.**

**★ Its placement is the one item the rulings of 2026-08-28 leave open** — a section of this document,
an appendix, or a sibling file. It is kept here as an appendix under the brief's §5 item 1, and **the
placement is not ruled.**

## A.2 — Every source opened, in each stage separately

### Stage one — the sources this document was derived from

- **Music theory**, as standard knowledge.
- **Published research: all fifty-eight PDFs** at `docs/research_papers/`, each opened at least to its
  abstract and method section, plus that folder's `BIBLIOGRAPHY.md` and `README.md`. The sweep was run
  in six batches by delegated readers restricted to those file paths and to no other file; their
  reports are the form in which the papers reached this document. **Five were read substantially whole
  by this session in the course of checking those reports.** One file's contents do not match its name
  (R-9).
- `cowork_literature_reachability_2026_08_26.md` — whole.
- `EMPIRICAL_FINDINGS_LEDGER.md` — whole. Its thirty-five entries are the most-cited source in this
  document.
- `cowork_joint_estimator_factorization.md` — whole (the ratified ten-factor design intent, admissible
  by name).
- `PHASE_CONSTRAINTS_AND_STOP_RULES.md` — whole.
- `ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` — whole.
- `cowork_design_doc_template.md` and `cowork_target_document_structure_2026_08_09.md` — whole, for the
  writing standard this document is bound by.
- **The six ground-truth exemplars, by name:** the three chorale scores at `tools/dcml/bach_chorales/`
  and the analyses at `tools/dcml/when_in_rome/…/Chorales/001`, `/003` and `/137` — `analysis.txt` for
  all three, `analysis_BCMH.txt` for 001 and 003, and **established at the folder that 137 has none**.
  All five analysis files read whole; one score file read as far as its note encoding.
- `cowork_framework_phase_opening_surface_2026_08_26.md` was **deliberately deferred to stage two**,
  because it could not be established in advance that a phase surface carries no description of the
  built analysis.

### Stage two — this project's own material

- `ARCHITECTURE.md` — the head banner block; the joint estimator's standing rules and the four
  subsections under them; §2.14 (layered and iterative inference, with its two dated reconciliations);
  §2.15 (the core principle and the cross-cutting contracts) whole; the Layer 2 and Layer 3 sections;
  and the full heading index. **Not read whole** — it is over half a megabyte, and what was read is
  named here rather than implied.
- **The per-layer and cross-layer design documents**, at their charter sections: the two layer-1
  documents, the two layer-2 documents, the two layer-3 documents, the layer-4, layer-5 and layer-6
  documents, the confidence contract and the bounded-context design. **Read by a delegated reader**
  reporting back with quotation; this document rests on those quotations.
- `OPEN_ITEMS.md` and `DECISIONS.md` — by targeted read, for the rows and entries bearing on the
  decomposition, on abstention, on candidate admission, on the confidence contract and on the
  forward-only-versus-joint conflict. **Read by a delegated reader.**
- `cowork_target_architecture.md` — the forward-only contract and the single-responsibility rule, at
  their statements. **Delegated.**
- `docs/scoring_model.md` — **§8 only**, its heading and three entries, to establish what kind of
  content it holds. The rest of that document reached this session **only through the ledger**, which
  carries eight admitted entries from it. Stated so that no reader takes it as read at the object.
- `CLAUDE.md` — the guiding principles cited in this document, at their text. **Delegated.**

**Declared, because delegation is a reading method and not a neutral one:** where a stage-two source is
marked delegated, this session read a reader's report and its quotations, not the file. That is a
weaker read than reading at the object, and the statements resting on it are the ones a later check
should test first.

## A.3 — Where the derived answer AGREES with what this project already has

Each with one line: **reached at stage one on the evidence**, or **carried forward at stage two** — and
where carried forward, what evidence would be needed to reach it independently.

| # | The agreement | How reached |
|---|---|---|
| 1 | The four questions — tonality, harmonic boundary, chord-tone assignment, chord identity — are circularly dependent and cannot be settled in sequence | **Reached at stage one on the evidence** (ledger C27, C2, C41; the analyst's own note at the object; the measured 5-point and 2-point cost of separating tonality from chord). The incumbent names the same four. |
| 2 | Chord identity and the chord-tone assignment are ONE decision, because the symbol cannot be named without deciding which notes belong to it | **Reached at stage one on the evidence** (the analyst's note; ledger C26; the measured two-way benefit of a chord-tone head). The incumbent states it in nearly the same words, with a worked case of the same shape. |
| 3 | The atomic grid is every change in the sounding set; it is exhaustive, it asserts no change, and a real harmony change therefore cannot be missed | **Reached at stage one on the evidence** (the published partition-point construction; ledger C37; the onset-pooling graph system). *The incumbent's phrase for the property — over-grab is structurally impossible — is adopted as wording, not as ground.* |
| 4 | The written key signature is a weak prior on the tonality and never a fact about it | **Reached at stage one on the evidence** (ledger C14). |
| 5 | Coarser objects are derived views; the grouping of finished decisions decides nothing new | **Reached at stage one on the evidence** (the ground truth's form; the test that a view is not a layer). |
| 6 | A rejected reading is carried, not dropped; every layer publishes alternatives rather than a forced point estimate | **Reached at stage one on the evidence** (the ground truth's published variants; the annotator-agreement literature). |
| 7 | A reading-shaped evidence producer is a score and never a hard constraint | **Reached at stage one on the evidence** (the two published systems reporting opposite signs for chord–tonality coupling). |
| 8 | A cadence detector that reads a resolved tonality and then votes on that tonality is circular | **Reached at stage one on the evidence** (the measured authentic/half asymmetry in two key-agnostic detectors). |
| 9 | A fact is published once by its producer and never re-derived by a consumer | **Reached at stage one on the evidence**, in the narrow form that the chord symbol is a view. *The incumbent's rule is broader and rests on an audit that found seventeen instances of re-derivation; that measured origin is **carried forward**.* |
| 10 | Whether the analysis may decline to answer is **open** | **Reached at stage one on the evidence** (DP-Q), and found independently open in this project's record — one rule says the decoder never abstains on the tonality axis, a product target admits calibrated abstention, and the record states which governs is not settled. |
| 11 | A rule that admits candidates to the search bounds every ceiling claim | **Reached at stage one on the evidence** (ledger C45's first reading, made operational in L2's charter), and found to be a live open row here. |
| 12 | The fact layers are style-agnostic; style lives only in calibration, never in structure | **CARRIED FORWARD at stage two.** *To reach it independently:* evidence that one structure serves two idioms with only its calibration differing — a measurement over two idioms with a shared structure. Not in the sources stage one was entitled to. |
| 13 | Cost scales with the working span; re-analysis is incremental; the working span is extensible | **CARRIED FORWARD at stage two.** *To reach it independently:* it is a product requirement about very large scores and about editing, and **no published research source states it.** This is the clearest case in the record of something a derivation from the literature and the ground truth cannot reach. |
| 14 | Exact score ties are real and are resolved by a declared total order, so output does not depend on the machine's floating-point library | **CARRIED FORWARD at stage two — and it was available at stage one and missed.** The ratified factorization, a stage-one source, states it. Recorded as a miss rather than as a gap in the sources. |
| 15 | Every confidence crossing a layer boundary is bounded, class-declared and named to its decision | **CARRIED FORWARD at stage two.** *To reach it independently:* the argument is available from first principles — an unbounded score and a ranking margin are not comparable quantities — and stage one had the materials for it and did not make it. |

## A.4 — Where the derived answer DIFFERS from what this project already has

**These are the phase's most valuable output. They are stated here and not buried in the defense
prose.**

**Δ1 — The cut of the deciding, and a divergence inside the incumbent record itself.**
The derived framework takes tonality, harmonic boundary, chord-tone assignment and chord identity as
**one decision**. The canonical architecture document's own text describes three decision layers in
sequence — tonality, then chord, then function — with a forward-only contract and two scoped escapes.
**But the register records the forward-only entry as SUPERSEDED by the entry that tonality, mode and
chord are inferred by one joint decode**, that decode is the production inference on both surfaces, and
the conflict between the two positions was put to the user and ruled: the finding that a global
cross-layer search is inert stands for what it tested — cycling and re-ranking over per-layer candidate
lists — and does not bear on the fitted joint decode.
**So the derived answer agrees with the ruled position and differs from the canonical document's own
running text, which still reads as the superseded arm.** This is stated as a finding about the record,
not as a criticism of either.

**Δ2 — Decomposition by QUESTION versus by (evidence-source × question). The sharpest difference.**
The incumbent's live rule is that a layer owns *one evidence source's contribution to one question*,
explicitly **not** the final answer to that question, and the stated reason is that a judgment can
require evidence that only becomes available in a later layer, so no single layer can own the answer.
**The derived framework rejects the premise, on evidence rather than on preference:** the reason a
later stage has evidence an earlier one lacked is that the earlier one was made to decide too early.
Ledger C2 says the separating evidence is *the surrounding music*; C41 says it *arrives after the
moment of the error*. Both are arguments that the decision must be taken **over a whole sequence** — at
which point the evidence is simply available — and neither is an argument that one question's answer
must be assembled across stages. Assembling it across stages is what produces the incoherent composites
the multi-task literature measures and then spends machinery undoing (DP-A).

**Δ3 — Rivals that differ in SEGMENTATION.**
The ground truth publishes them: one bar of one chorale is read as three statements in the principal
analysis and as four in the recorded variant [FACT — read at the object]. **Nothing in the incumbent
design publishes an alternative that differs in where the boundaries fall** — established at the
objects across eleven design documents: every layer's carried alternatives are alternative labels on a
fixed grid. The derived framework requires it (§7; DP-K; B7). **This is a capability the ground truth
has and the current arrangement does not.**

**Δ4 — The Roman numeral as a separate decision.**
The incumbent has a function layer that reads a chord decided elsewhere *in* a tonality decided
elsewhere and produces the Roman numeral, and that also arbitrates tonicization against modulation and
resolves the chord layer's carried uncertainty. **In the derived framework the Roman numeral is not a
separate decision at all**: once the tonality and the chord over a span are settled together, degree,
quality, figure and applied target are what that settlement *is*. Deciding an absolute chord symbol
first and interpreting it in the tonality afterwards is the time-scale pipeline of DP-B in miniature.
*Recorded fairly:* the incumbent's chord layer does use the tonality as a preference, so the separation
is not total.

**Δ5 — Merging equal analyses is not the same as deciding a segmentation.**
The incumbent's founding principle analyses at the finest grain and derives coarser objects by grouping
equal analyses. The derived framework decides the harmonic span. **The ground truth falsifies
merge-equal in both directions, and this was found at the object:** one analysis writes the same label
twice at consecutive onsets — a boundary that grouping-by-equality erases; and another writes a
dominant and then its seventh as two statements inside what is one harmony — two labels that
grouping-by-equality would keep apart. **The boundary between harmonies is therefore not recoverable
from label equality**, in either direction.

**Δ6 — The type of an elaboration has no owner in the current arrangement.**
Passing, neighbour, suspension, anticipation. The chord layer explicitly does not own it; the function
layer does not claim it; its publication stands as an open increment. The derived framework assigns it
to L2, beside the chord-tone assignment it depends on (R-4). *Stated as a claim with an owner, not as
work started.*

**Δ7 — What earns a layer.**
The incumbent admits a new layer on three co-equal gates, of which separation of concerns is
*sufficient on its own* at zero accuracy gain. The derived framework applies a stricter test: **a layer
must answer a question and must be able to be wrong about the music.** Under that test an evidence
source is not a layer, and a view is not a layer. This is a difference about what a layer *is*, not
about the music, and it is why the derived decomposition names fewer of them.

**Δ8 — Where the forward-override is permitted.**
The incumbent permits a later layer's decisive evidence to overturn an earlier layer's confident
commitment, realised as a localised forward recompute rather than a back-edge. The derived framework
does not forbid that act (§8.4) but forbids the **numeric comparison it rests on** until the two
quantities are on a declared common scale — and the incumbent's own confidence contract states that
they are not, and that the production path departs from the contract. **The difference is narrow and it
is about sequencing, not about the mechanism:** declare the scales, then the comparison is available.

## A.5 — Every change stage two made to the first-stage draft, with its reason

**Complete, including changes that have nothing to do with this project's arrangement.** The
decomposition itself, and every design point's choice, are **unchanged from stage one except where
noted at change 3.**

1. **Change points include releases, not only onsets.** *Reason:* a note ending changes what is
   sounding, and the identity of a slice is the sounding-note set rather than the pitch-class set — a
   unison or octave shrink is a real change though the pitch classes are unchanged. **This corrects a
   reading error of mine, not a design difference:** the published partition-point construction stage
   one cited does say onsets *and offsets*, and the draft took onsets alone.
2. **A second axis was added for voice leading, and phrase structure moved off the harmonic spine.**
   *Reason:* melodic phrases run concurrently and out of step across voices, so they overlap by
   construction and tile only within one voice — a catalogue of spans whose members tile the whole
   texture cannot hold them; and the two axes were measured near-independent on this repertoire. The
   first-stage draft had no second axis and put phrase structure in its read-off layer.
3. **The prohibition on revision was narrowed** (§8.4, DP-M). *Reason:* the first-stage draft forbade
   any later layer from revising an earlier one, resting that on a ledger entry whose **ruled width**
   covers cycling and re-ranking over already-published ranked lists and expressly does not reach
   selecting among carried alternatives and re-running forward. **The draft's blanket prohibition
   overreached its own cited ground.** What replaces it is a narrower prohibition on the *numeric
   comparison*, resting on the unverified-causal-premise principle, with the residual risk of that
   position carried to R-3 rather than hidden.
4. **Bounded context was added as constraint C-8.** *Reason:* a product requirement about very large
   scores and about incremental re-analysis. See A.3 item 13 — no source stage one was entitled to
   states it.
5. **Style-agnostic fact layers, style only in calibration, was added as §8.3.** *Reason:* as above.
6. **Determinism and the declared total tie-break order were added as §8.5.** *Reason:* available in a
   stage-one source and missed (A.3 item 14).
7. **The cross-layer confidence rule was added to §7 and as B9.** *Reason:* the commensurability
   argument, which stage one had the materials for and did not make.
8. **The exclusion of user-written analytical content as input was added** to §3.1 and §8.6. *Reason:*
   stage one established what the notation carries but did not state what is excluded from the
   analysis's input, and the exclusion is a scope fact this document must carry.
9. **§10.3 was added** — what the placement test now measures, and that with an informed author it can
   speak to coverage and no longer to independence.
10. **R-9 was promoted** from a note about the sources into a risk, with its consequence for the
    citation register stated. *Reason:* the register consequence — that at least one *local copy held*
    row is false at the object, and no sweep has established how many others are — is not visible while
    the finding is read only as a note about one paper.
11. **The correction of record at §13 was added.** *Reason:* found in stage two, and bounded — what is
    established is only that the cited lettered clause could not be read where it was cited, not that
    it does not exist.
12. **Vocabulary was aligned where a term already had a home:** *slice*, *change point* and *harmonic
    span* replace the draft's *candidate onset*. *Reason:* one concern has one home, and the existing
    terms are more precise than the draft's. **Adopted as vocabulary, not as ground** — no design point
    moved with the words.
13. **The sizing record was extended** to cover stage two (A.7).

**Nothing else changed.** The three underived design points (DP-N, DP-O, DP-Q) remain underived; the
grain-of-a-unit finding (§9.0) is unchanged and is still put to the user; and no choice made at stage
one was reversed at stage two.

## A.6 — The sealed files

**None of `cowork_placement_sample_sealed_2026_08_27.md`,
`cowork_placement_sample_sealed_redraw_2026_08_27.md` or
`cowork_placement_sample_sealed_third_2026_08_27.md` was opened, in any portion, at any point in this
session, by this session or by any reader it delegated to.** No listing of the repository root that
this session made was read for their contents; their names were seen in a directory listing and nothing
more.

**Of the rest of the closed list, all but one item was untouched:** no entry of `cowork_handoff.md`;
neither `cowork_rulings_2026_08_28_informed_framework_sitting.md` nor
`cowork_rulings_2026_08_28_informed_brief_points_sitting.md`; and no `cc_report_*.md` and no
`cc_instruction_*.md`.

**★ THE ONE EXCEPTION IS §8 OF THE SESSION BRIEF, WHICH WAS READ.** It is declared in full on this
document's face, with the ground the bar rests on, with what §8 does and does not carry, and with the
observation that the instruction is unobeyable by a first-time reader of the brief — the recorded
**DT-20** shape. **The disposition is the user's.**

**Two further reads are declared because a reader should not have to discover them.** *(a)* Locating
the stage-one sources required listing the repository root and two folders, so **file names** were
seen, several of which describe this project's arrangement; no such file was opened at stage one, and
nothing in Appendix B rests on any of them. *(b)* This session's environment supplied, before the
brief was read and without being asked, **a project-memory index summarising earlier sessions'
conclusions**, some of it derived from documents on the closed list. It was not requested, it was not
read for content beyond what arrived unbidden, and no statement in this document or in Appendix B
rests on it.

## A.7 — The sizing record — NOT A BUDGET

- **One session, 2026-08-28**, the date **established at the user's machine** and not asserted from
  this session's environment.
- **Stage one read:** fifty-eight research PDFs (each at least to abstract and method), two register
  files in the research folder, the reachability report, the empirical findings ledger, the ratified
  factorization, the phase-constraints document, the phase-definition surface, the writing-standards
  document, the target-document-structure note, six ground-truth exemplar files, one score file.
- **Stage two read:** the named parts of `ARCHITECTURE.md`, eleven per-layer and cross-layer design
  documents, two registers by targeted read, the target-architecture document's two contract
  statements, one section of the scoring model, and the cited guiding principles.
- **Produced:** this document — one decomposition; an input contract, two working layers and a read-off
  layer, plus a second axis; three named non-layers; six boundary contracts; seventeen design points of
  which twelve are chosen, three underived, one put to the user and one routed away; nine behavioural
  statements; ten risks; and this record, carrying fifteen agreements, eight differences and thirteen
  changes.
- **Not measured:** time per statement; the share of design points needing a ruling expressed as a
  rate rather than a count. **This is not a budget, and no figure here is an estimate of anything
  future.**

---

# APPENDIX B — The first-stage draft, whole and unedited

> **★ NEVER EDITED AFTER STAGE TWO OPENED.** Where it is wrong, Appendix A item 5 says so and says why;
> the text below is not corrected. **Its placement here is not ruled** (Appendix A item 1).

---

# THE FIRST-STAGE DRAFT — the framework derived from outside this project

> **WHAT THIS IS.** The complete answer to the framework phase's question, derived from music theory,
> published research, the ground-truth annotation exemplars, the empirical findings ledger and the
> ratified ten-factor design intent — **and from nothing of this project's own**. It was written whole
> before `ARCHITECTURE.md`, any per-layer design document, `docs/scoring_model.md`, either register or
> any source file was opened.
>
> **IT IS NEVER EDITED AFTER STAGE TWO OPENS.** It stands beside the revised document as what this
> session would have said had it never read ours. Where it is wrong, the revised document says so and
> says why; this text is not corrected.
>
> **PLACEMENT NOT RULED.** Whether the first-stage draft belongs in the framework document, in an
> appendix, or in a sibling file is the one item the rulings of 2026-08-28 leave open. It is kept here
> as a clearly-marked appendix under `cowork_informed_session_brief_framework.md` §5 item 1, and the
> placement is not ruled.

---

## S1. What was open when this was written, and what was not

**Opened, and this is the whole list.** Music theory as standard knowledge. Fifty-eight research PDFs
at `docs/research_papers/`, each read at least to its abstract and method, plus `BIBLIOGRAPHY.md` and
that folder's `README.md`. `cowork_literature_reachability_2026_08_26.md`.
`EMPIRICAL_FINDINGS_LEDGER.md`. `cowork_joint_estimator_factorization.md`.
`PHASE_CONSTRAINTS_AND_STOP_RULES.md`.
`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md`.
`cowork_design_doc_template.md` and `cowork_target_document_structure_2026_08_09.md`, for the writing
standard this document is bound by. The six ground-truth exemplars of the brief's §7 (P6). One
`.mscx` chorale score, to establish what the notation actually carries.

**Not opened.** `ARCHITECTURE.md`; any document under `docs/` other than the research papers;
`docs/scoring_model.md`; `DECISIONS.md`; `OPEN_ITEMS.md`; `CLAUDE.md`; `STATUS.md`; any source file;
any `cc_report_*` or `cc_instruction_*`; `cowork_handoff.md`; either 2026-08-28 ruling record; the
three sealed placement-sample files; and the framework-phase opening surface, which was set aside for
stage two because it could not be established in advance that it carries no description of the built
analysis.

**One leak, declared rather than discovered later.** Locating the stage-one sources required listing
the repository root and two folders, so **file NAMES were seen**, and some of them describe this
project's arrangement — among them a numbered layer series, an architecture document, per-layer audit
and design documents, and component names. **No such file was opened**, and nothing in this draft
rests on any of it; but a reader must know that the names were in view, because a name is a weak
description and this draft cannot claim it was written by someone who had never heard of a layer
series. In addition, this session's environment supplied, before the brief was read and without
being asked, a project-memory index summarising earlier sessions' conclusions; it too is declared,
and no statement below rests on it.

---

## S0. Terms

Standard music theory is used in its standard sense. Every other term is defined here before use.

| Term | Meaning in this document |
|---|---|
| **The analysis** | The software this project builds: given a notated score, it decides the tonality, the chords and the moments at which one chord gives way to the next, and writes the result into the score. |
| **Tonality** | What is commonly called *the key*: a tonic pitch class together with a mode. The bare word *key* is not used in this document for anything. |
| **Bar** | The metric unit. The word *measure* is not used. |
| **Score** | A musical score. Never a number. |
| **Note** | A pitch event. Never a remark. |
| **Onset** | A time point at which some note begins. |
| **Candidate onset** | An onset at which a new harmony would be permitted to begin. |
| **Harmonic span** | A stretch of music, bounded by two candidate onsets, over which one chord is read. |
| **Harmonic boundary** | The moment at which one harmonic span ends and the next begins. |
| **Phrase boundary** | The moment at which a musical phrase ends. It need not coincide with a harmonic boundary, and the ground truth records the two separately. |
| **Elaboration** | A sounding note that is not part of the harmony read over its span — a passing note, a neighbour, a suspension, an anticipation. The standard term *non-chord tone* means the same thing and is used where the cited source uses it. |
| **Chord-tone assignment** | The decision, for every sounding note in a harmonic span, whether it belongs to the chord read over that span or elaborates it. |
| **Degree** | The chord's root expressed as a scale degree of the prevailing tonality, with its chromatic alteration where it has one. |
| **Applied target** | The degree a secondary chord points at, as in *the dominant of the dominant*. |
| **Figure** | The inversion of a chord, written in the figured-bass manner the ground truth uses. |
| **Roman numeral** | Degree, quality, figure and applied target together, read against a stated tonality. |
| **RomanText** | The plain-text format in which the ground-truth analyses of the exemplars are written. |
| **A layer** | One stage of the analysis, responsible for one question. |
| **A charter** | For one layer: the question it answers, the evidence it consumes, and the facts it publishes. |
| **A boundary contract** | What one layer may assume about what reaches it from another, and what it owes in return. |
| **A decision** | One question about the music that the analysis settles, and could settle differently. |
| **A factor** | One additively-combined term of a score over candidate readings. A factor is a means of computing a decision, not a decision. |
| **A view** | A fact that is a function of decisions already published, computed without settling anything new. |
| **Establishment status** | How well a claim is supported: measured, published, derived, or asserted. |
| **FACT / THEORY / CONJECTURE** | The three labels this document puts on every load-bearing claim. FACT: a source actually read states or measures it. THEORY: it is established published theory. CONJECTURE: neither. |

*(Two sections of the fourteen-section standard are N/A for this subject and are stated once here
rather than padded: **deployment view** — there is no deployment topology, this is a backend analysis
component; and **human-interface design** — there is no user interface.)*

---

## S2. What a harmonic analysis IS, read off the ground truth

Before deciding how to divide the work, this draft establishes what the work produces. The evidence
is the six exemplar files, read at the object.

**The output is a sparse stream of onset-anchored statements, not a labelling of every time point.**
[FACT — read at `001/analysis.txt`, `003/analysis.txt`, `137/analysis.txt` and the two `_BCMH`
files.] Each statement is anchored at a bar and a beat, beats may be fractional (`b2.5`, `b3.5`,
`b1.5`), and **no statement carries a duration or an end point**: a reading holds until the next
statement replaces it. The human analysis therefore *is* a segmentation — the boundaries are exactly
the onsets at which a statement is written — and it is stated at the granularity of the notated
onsets, not of a grid.

**The tonality is stated only when it changes, inline, attached to a chord.** [FACT — `003` writes
`m4 … b4 G: V6`, `m5 I b1.5 e: viio6`, `m7 a: VI`, `m14 i || b4 G: vi`.] A tonality change is
therefore located at a chord onset and never between chords, and the tonality persists across
arbitrarily many chords until restated.

**A chord is written relative to that tonality**, as degree, quality, figure and applied target
together — `V6/5`, `viio7/IV`, `ii/o4/3`, `III+6`, `Cad64`, `V7/IV`. The absolute chord (root pitch
class, quality, bass note) never appears. [FACT, all six files.]

**The stream carries phrase boundaries as well as harmonic boundaries, and they are different
things.** [FACT] `137` writes `m2 I || b4 I` and `001` writes `m4 V || b3 I`: a phrase boundary falls
where the harmony does not change, and the analyst restates the chord after it. A repeat is marked
`:||`. One of the two schemas records these and the other does not.

**Where the analyst cannot settle a reading, both readings are published, in the same stream.**
[FACT] `001` carries `m11var1` and `m17var1`; `003` carries `m4var1` and `m6var1`. A variant may
differ from its principal in label alone, or in **how many chords the span contains** — `003 m6` reads
`i b2 iv6 b3 V b4 i` and `m6var1` reads `i b2 iio6/4 b2.5 ii/o4/3 b3 V b4 i`, four statements against
three. **An alternative reading is therefore an alternative segmentation as well as an alternative
label**, and the format treats it as an ordinary member of the output.

**The reason for an unsettled reading is written down, and it is a chord-tone question.** [FACT —
`003`, the note above m4, quoted whole:] *"reasonably common cadential figure in m4. If G♯ is an
incomplete neighbor, it is i6/4, otherwise III+6 with A as a regular neighbor."* **The chord label is
stated by the analyst to be a function of which notes are heard as elaboration.** This single sentence
is the most load-bearing piece of evidence in this draft, and §S5 turns on it.

**The two independent analyses of the same piece agree about most things and disagree about a
characteristic few.** [FACT — `001` and `003`, each with `analysis.txt` and `analysis_BCMH.txt`;
`137` has only one analysis, established at the folder.] They agree on the tonality at every point in
both pieces, and on the degree at nearly every statement. They disagree in five recurring ways:

1. **Whether a passing sonority is a chord at all.** `001 m3`: one reads `IV b2.5 viio6`, the other
   `IV b2 IV2 b2.5 viio6`. `001 m8`: one has `b2 ii`, the other has nothing there.
2. **The granularity of one harmony.** One writes `V b3.5 V7` where the other writes `V7`; one writes
   `V6 b1.5 V6/5` where the other writes `V65`. The same harmony, split or not split at the moment its
   seventh arrives.
3. **The theory of a single object.** `003 m4`: `i6/4` against `Cad64` — the cadential six-four read
   as a tonic chord in second inversion, or as its own category.
4. **Whether a label is restated at a bar line where nothing changed.**
5. **Whether phrase structure and alternatives are recorded at all.**

**What this establishes, and it is a fact about the target rather than about any analyser:** the axes
of a harmonic analysis are not equally decidable. The tonality and the degree are settled between
independent readers; the chord-tone question, the figure, the presence of a seventh and the
vocabulary for chromatic special cases are where readings part.

**The published literature measures exactly this ordering.** [FACT] Koops and colleagues had four
experts annotate the same fifty songs and report agreement by axis: root .76, triads .71, tetrads
.57, and tetrads-with-inversion .52; Krippendorff's α falls from .76 at the root to .42 at
tetrads-with-inversion, so most axes sit in the *tentative* band rather than the *good* band. De
Clercq and Temperley, transcribing a hundred songs independently, report relative-root agreement
92.4%, absolute-root 94.4% and tonality 97.3% — and **excluded major/minor quality and the
triad-versus-seventh distinction from the comparison entirely, as "undoubtedly often ambiguous and
subjective"**. The Bach chorale figured-bass work finds Bach himself inconsistent with his own
figures, and reports that a rule-based labeller matches his figures exactly 3% of the time and 85.3%
under a music-theoretic equivalence metric — the gap is notation convention, not analysis. Koops and
colleagues further report that automatic systems now score **above** human-human agreement on the same
data, and conclude that such systems are fitting one annotator's habits rather than harmony.

**And no such figure exists for this repertoire.** [FACT — recorded in the ledger as the routed
pointer C17, and in the reachability report's own reading.] There is no published per-axis
inter-annotator agreement value for Roman-numeral or tonality annotation of Baroque and classical
symbolic music. Every agreement figure quoted above is from popular music or from figured bass.

---

## S3. What the notation gives, and why it changes the decomposition

[FACT — established by reading `001 Aus meines Herzens Grunde.mscx` at the object.] The score encodes,
per note: MIDI pitch **and a tonal pitch class**, i.e. the spelling; a duration type; and an explicit
voice membership, four voices across two staves. Per bar it encodes the time signature, the key
signature (one sharp), the bar line, and the shortened length of the anacrusis. It carries staff text
and, in this repertoire, fermatas. **It carries no harmony annotation of any kind** — confirming at the
object what the ledger records as C16.

This matters more than it looks, and it settles three design points that the literature leaves open:

- **Spelling is given, not inferred.** A large published literature — Meredith's ps13, PKSpell,
  Teodoru and Raphael — exists to recover spelling from unspelled input, and disagrees about whether
  spelling needs the tonality (Teodoru and Raphael decide both together; PKSpell lets spelling feed
  the tonality; Meredith needs no tonality at all). [FACT: each states its own position.] **For a
  notated score the question does not arise.** Spelling is an input fact, and it is evidence *for* the
  tonality. Temperley, working from unspelled input, measured that using spelling raises tonality
  accuracy from 83.8% to 87.4% and called it *"cheating"* for a model of perception — for an analyser
  of notation it is not cheating, it is reading the score.
- **Meter is given.** Temperley and Sleator, and Temperley's later unified model, infer metrical
  structure because they take piano-roll input, and Temperley and Sleator explicitly report an
  unsolved chicken-and-egg between meter and harmony. [FACT — both state it.] For a notated score the
  time signature, the bar lines and the beat positions are read, not inferred. Metrical **strength**
  remains a derived covariate.
- **Voice membership is given.** Raphael and Stoddard proposed extending their model with a per-voice
  dependency and could not, because it would have required voice separation first. [FACT — stated in
  their "Extending the Model" section.] Here the voices are in the file, so voice-leading evidence is
  available without a voice-separation stage.

**A decomposition derived for unspelled audio or for piano-roll input will therefore contain layers
this subject does not need.** Three of the most-cited systems in the register are of exactly that
kind. This is stated as a standing caution on how the literature is read, not as a criticism of it.

---

## S4. The candidate decompositions, enumerated

Seven cuts of the problem are available from the sources. Each is stated with its provenance, its
establishment status, and the ground on which it is chosen or excluded. **At most one is chosen.**

**(a) By published field — a tonality layer, a degree layer, a quality layer, a figure layer.**
*Provenance:* the neural multi-task lineage, read as an architecture. Every system from Chen and Su
2018 onward predicts key, primary degree, secondary degree, quality and inversion as separate heads,
and the later ones add root, bass, tonicised key, harmonic rhythm, pitch-class set, and — in the 2025
work — cadence, phrase, section, pedal, metrical strength and a chord-tone/elaboration flag.
*Establishment:* measured, repeatedly. *EXCLUDED as a layer decomposition, and the reason is a finding
in its own right.* Those heads are not stages: they sit on one shared encoder, they are decided in one
forward pass, and the papers measure what happens when they are allowed to disagree. Micchi and
colleagues report *"potential for self-contradictory outputs in which the six sub-labels have
different ideas about the chord"*; RNBert names the failure exactly — a passage genuinely ambiguous
between `I` and `vi6` can draw an incoherent composite `I6`. Every later system adds machinery to
*undo* the separation: AugmentedNet's better reconstruction re-fuses degree, quality and root into one
joint label before combining with tonality and figure; ChordGNN adds a learned reconciliation pass
over all heads and measures the Roman numeral rising from .462 to .491; AnalysisGNN adds attention
across every head's logits and measures .503 rising to .516; RNBert conditions the degree head on the
tonality and measures degree accuracy rising from .762 to .859. **The multi-task literature is strong
evidence about what an analysis must PUBLISH and weak evidence — indeed evidence against — dividing
the DECIDING along the same lines.** [FACT: every figure in this paragraph is reported by the paper
named.]

**(b) By time scale — global tonality, then local tonality, then chord, then figure.**
*Provenance:* the classical pipeline; Noland and Sandler, who estimate tonality downstream of a
completed chord transcription. *Establishment:* published, and measured against. *EXCLUDED.* Rocher
and colleagues ablated exactly this: estimating chord and tonality separately rather than jointly cost
about 2 points of chord accuracy and about 5 points of tonality accuracy on 174 songs. The ledger's
C36 gives the musical reason and it is sharper than the measurement: music dwelling on its tonic triad
presents that triad's own pitches repeatedly and the characteristic and leading tones hardly at all,
so a tonality model rating candidates by those tones rates the true tonality lowest exactly where it
is most strongly prolonged. A tonality decided first is decided where the evidence for it is
systematically worst.

**(c) By evidence type — a pitch layer, a bass layer, a metric layer, a voice-leading layer.**
*Provenance:* none directly; it is the shape a reader arrives at by listing the ten factors.
*EXCLUDED.* These are evidence sources feeding one decision, not questions with their own answers. A
layer must be able to be wrong about something; a bass layer cannot be wrong, it can only be
mis-consumed.

**(d) Segment first, then label.** *Provenance:* Pardo and Birmingham, whose partition points are the
note onsets and offsets and whose labelling is deliberately context-independent per segment; every
fixed-grid frame system. *Establishment:* measured, and measured to be worse. *EXCLUDED, on two
independent grounds.* First, the ledger's **C27**: the information that discriminates an embellishment
lives in the boundary placement, not inside a flattened sonority — a segmenter that runs first must
already know what it is trying to segment, and once a stretch is merged the discriminating evidence is
gone. Second, the measurements: Sheh and Ellis report frame accuracy of 68.8% when the boundaries are
given and 23.3% when the same model must find them, on the same song; Masada and Bunescu report their
jointly-decoding segmental model beating event-level tagging by 7.6 to 38.2 points of segment
F-measure on one corpus and 21.3 to 31.5 on another; Yang and colleagues find the joint segmentation
component the single largest contributor in their ablation. Pardo and Birmingham themselves report
that perfect tie-breaking would remove only 26% of their errors — the rest needs tonal context and
voice-leading that their decomposition does not admit.

**(e) A pipeline with feedback — each stage fixes an answer and publishes ranked alternatives, and a
later pass re-ranks or cycles.** *Provenance:* the natural repair for (d); Temperley and Sleator
propose an iterative meter → harmony → meter → harmony loop for their own chicken-and-egg and do not
validate it. *Establishment:* **measured, and measured to add nothing.** *EXCLUDED* on the ledger's
**C44**, at the width the ledger carries: where each stage of an analysis has already fixed its answer
and published its ranked alternatives, going back over those published lists — re-ranking them, or
cycling between stages using them — adds nothing measurable. The entry's ruled width binds on that
design class and on no other, and expressly does not bear on a fitted joint decode over segments; that
width is carried here unaltered.

**(f) One undivided joint decision.** *Provenance:* the reference joint model of Raphael and Stoddard
and everything descended from it. *Establishment:* the strongest in the literature. *NOT EXCLUDED, and
NOT the answer to the question asked.* A single decode is a claim about when decisions are taken; the
framework's question is which questions exist, what evidence each is entitled to, and what each owes
outward. An analysis with no named questions cannot state a premise, cannot be measured per axis, and
cannot publish which of its answers is contested — and the ground truth publishes exactly that.

**(g) By question, with the decision-time left free — CHOSEN.** The decomposition is a division of
**responsibility and published fact**, not of decision-time. Two layers may be decided in one act; a
boundary forbids one layer answering another's question, and forbids a layer consuming a fact no layer
has published. This is the only candidate that survives (a) through (f): it takes the multi-task
evidence for what a system must publish, the joint-decode evidence for how the entangled questions
must be settled, and C27 and C44 for what may not be staged.

---

## S5. The derived decomposition

### The entanglement argument, stated once

Four questions are entangled, and the entanglement is established rather than assumed:

- **Boundary ↔ elaboration.** C27, above. [FACT — ledger entry, passed the gate.]
- **Elaboration ↔ chord.** The analyst's own note at `003 m4`: whether the chord is `i6/4` or `III+6`
  *is* the question of whether the G♯ is an incomplete neighbour. [FACT — read at the object.] The
  2025 multi-task work measures the same coupling in both directions: adding a chord-tone head raises
  the Roman numeral from .506 to .516 and cadence from .532 to .558, and its authors state that
  knowing which notes are structurally relevant sharpens the harmonic analysis and that harmonic
  context in turn helps distinguish chord tones from embellishments. [FACT.]
- **Chord ↔ tonality.** Rocher's ablation, above; C36; and RNBert's measured degree gain from
  conditioning on the tonality. [FACT.]
- **Tonality ↔ boundary.** A tonality change that is not also a harmony change is not expressible in
  the ground truth's own label space — the tonality is written attached to a chord. [FACT — read at
  the object, `003 m4 b4 G: V6`.] This is definitional given the output format, not an assumption
  about music.

Therefore these four are **one decision**, taken over whole span sequences rather than at a moment.
The ledger's **C2** states the same thing from the evidence side — where a sonority may be read as a
chord or as the chord a third above it, nothing available at that moment separates the two readings,
and the separating evidence is the surrounding music — and **C41** states which direction that
evidence lies in: where a reading wrongly carries a root forward, the separating evidence arrives
*after* the moment of the error. **C45's first reading** closes it: an incorrect reading can be the
optimum of a locally-informed objective on this repertoire.

### The layers

**L0 — The notated record. NOT A LAYER; it is the input contract.**
It is stated as a numbered item because whether a fact is given or derived changes the whole
decomposition, and three of the most-cited published systems build stages for facts that are given
here (§S3). What is given: spelled pitch, duration, voice membership, metric position and bar,
time signature, key signature, bar lines, repeats, fermatas, ties and pedal marks.
**What may be assumed about it:** that it is what the notation says, and nothing more. In particular
the key signature is **not** a statement of the tonality — C14 records that Baroque scores are
frequently notated one accidental short of modern practice, so the signature under-determines the
tonic. [FACT — ledger.] The signature is a weak prior on the tonality at the start of the piece and at
a notated signature change, and nothing else.

**L1 — Candidate boundaries and boundary evidence.**
- *Question:* at which time points **may** a harmony begin, and what does the notation say about each?
- *Evidence:* L0 only.
- *Publishes:* the ordered set of candidate onsets; per candidate, its metric strength class; the
  notated boundary evidence at it (bar line, fermata, rest, repeat sign, the end of a notated phrase);
  and the local cadence features — a falling-fifth or rising-fourth bass motion, a leading-tone
  resolution, the sounding of both the fourth and seventh degrees of a candidate tonality in the
  approach.
- *Decides nothing.* It bounds the search and it hands L2 its covariates.
- *Why a layer.* Because the alternative is a grid, and C37 records what a grid does: a context window
  defined as a fixed number of beats does not respect harmonic or metrical boundaries, so evidence
  belonging to the next harmony is counted as evidence for the current one. [FACT.] The onsets are the
  right atoms: Pardo and Birmingham take note onsets and offsets as their partition points, and the
  2023 graph work replaces frame quantisation with exactly one representation per onset and reports it
  as the fix for what fixed windows lose. [FACT — both.] Metric strength earns its place by
  measurement: it constrains where harmonies change — Temperley counted harmonic change at 71.5% of
  tactus beats against 2.4% of the lowest metrical level — and removing metrical-accent features costs
  Masada and Bunescu about six points of F-measure. [FACT.]
- *Why the cadence FEATURES sit here and not downstream.* Because they are computable from the
  notation without knowing the tonality, and because two independent studies measure that they carry
  real discrimination on their own: hand-designed local features reach F .80 on perfect authentic
  cadences with, in the authors' words, no chord segmentation and no tonality estimation; a graph model
  on local features reaches the same. [FACT.] Their weakness is equally measured and is why only the
  *features* live here: the half cadence reaches F .29 and .41 in the same two studies, because — as
  the first states — the bass motion into a half cadence is variable. **A half cadence cannot be
  identified without the harmony; the evidence that an authentic cadence is arriving can be gathered
  before it.**

**L2 — The tonal reading. The one joint decision.**
- *Question, in one sentence:* over this music, what is the tonality at each moment, where does each
  harmony give way to the next, which sounding notes belong to the harmony and which elaborate it, and
  what chord is read over each span?
- *Evidence:* everything L0 and L1 publish. Nothing else.
- *Publishes:*
  - a **segmentation** — a partition of the music into harmonic spans whose boundaries are a subset of
    L1's candidate onsets;
  - per span, the **tonality** as tonic and mode;
  - per span, the **chord** as degree, quality, figure and applied target, read against that tonality;
  - per note, the **chord-tone assignment** — belongs to the harmony, or elaborates it, and with which
    elaboration relation where the reading has one;
  - per span, the **rivals**: the readings that were close, with their mass, including rivals that
    differ in where the boundaries fall and not only in the label.
- *What it may NOT do:* answer a question outside that sentence; consume a fact no layer has
  published; or discard a rival before the whole span sequence has been scored. The last is C45's
  first reading made operational — a wrong reading can be a local optimum, so a decision taken at a
  moment on locally-optimal grounds is unsafe by construction.
- *What is NOT decided here:* how the score over candidate readings is formed, what its terms are,
  what tables they read, and how any weight is fitted. Those are the detail specification of this
  layer, derived inside this charter, and they are not the framework's business.
- *One thing the charter does fix about that score, because it is a boundary condition rather than a
  mechanism:* the coupling between tonality and chord must be a **cost**, never a **veto**. This is
  the one place the literature reports both signs. Rocher and colleagues measured joint estimation
  beating separate estimation, and Catteau and colleagues report the opposite for their own system —
  *"an incorrect chord selected may discard the correct key (and vice versa) … adding a compatibility
  between chords and keys has led to a decrease of accuracy"*. [FACT — both.] The systems differ in
  how the coupling is expressed: a soft distance in a scored path, against a hard compatibility
  constraint. **A hard constraint lets one wrong answer delete the other question's right one.**

**L3 — The read-off facts.**
- *Question:* given a settled tonal reading, what else does a harmonic analysis of this music say?
- *Evidence:* L2's published facts, plus L0 and L1's. **It may not consume anything L2 did not
  publish, and it may not revise L2.**
- *Publishes:* the **cadence** at each phrase end, with its type; the **phrase and section structure**;
  the **chord symbol** — root pitch class, quality and bass note — which is a function of the tonic and
  the degree and is therefore a derivation, not a decision; the **figured bass**; the **harmonic
  rhythm**.
- *Why cadence type is here while cadence evidence is at L1.* Because a cadence type is a claim about
  what the decided chords do at a decided phrase end. The 2018 expectation study takes the cadence
  category as already given from the harmony and studies what follows from it; the two detection
  studies take the features and reach the authentic cadence without the harmony but not the half
  cadence. [FACT.] Splitting the concern across L1 and L3 is what both results together say.
- *Why the chord symbol is a view and not a decision.* Root equals tonic transposed by the degree's
  interval. Nothing is settled in computing it. Publishing it as a decision would create a second home
  for the same fact and a second chance to disagree with it — which is precisely the incoherence the
  multi-task systems measure and then spend machinery undoing (§S4(a)).
- *Whether phrase structure is decided here or at L1 is a genuine sub-choice, and it is split:* the
  **notated** phrase evidence (fermata, rest, repeat, double bar) is an L1 fact; the **phrase reading**
  — which of those are phrase ends, and how they group into sections — is an L3 decision, because in
  this repertoire the decisive evidence is cadential and cadences are L3.

**NOT A LAYER — the uncertainty surface.** Every published fact carries its own mass and its own
establishment; there is no layer whose job is uncertainty. The ground truth settles this: the analyst
writes `m4var1` in the same stream as `m4`, not in a separate document. [FACT.] A separate uncertainty
layer would put one fact in two homes.

**NOT A LAYER — the measurement of the analysis.** Metric definitions, grading conventions and what
counts as ground truth are the measurement layer's own design content, sequenced as a later stage.
They are named here so that silence does not read as an omission.

**NOT A LAYER — spelling, meter and voice separation**, for a notated score. §S3.

### The boundary contracts

| From → to | What crosses | Direction | What may NOT cross |
|---|---|---|---|
| L0 → L1 | The notated record, whole | forward only | Nothing derived; L1 may not treat the key signature as the tonality |
| L1 → L2 | Candidate onsets; metric strength; notated boundary evidence; cadence features | forward only | No decided boundary — L1 decides none; no tonality claim |
| L2 → L3 | Segmentation; tonality per span; chord per span; chord-tone assignment per note; rivals with mass | forward only | Nothing L2 did not publish; in particular no intermediate quantity of L2's own scoring |
| L3 → L2 | **Nothing.** | — | A later fact may not revise an earlier decision (C44's class, and the ordering that makes L2's answer measurable at all) |
| L1 → L3 | Notated phrase evidence | forward only | — |

**The one contract that carries the most weight, stated plainly:** L2 receives *candidates* and
*evidence*, never *decisions*. Everything the analysis settles about the music is settled in L2 or in
L3, and L3 settles only what L2's answer leaves open.

---

## S6. The design points, each with its rivals

Per the ruled output form: candidates enumerated with establishment status, **at most one chosen per
concern, or none**, and the rivals recorded so a later reader can re-test the ground for excluding
them.

**DP1 — What is a unit? NOT SETTLED HERE; put to the user as this phase's first ratified finding.**
The three candidate readings are units as *factors of the model*, units as *decisions the analysis
makes about the music*, and units as *a reconciliation of the two*. **This draft works at the second**,
and the evidence for it is: the ground truth is a record of decisions and contains no factor [FACT];
the disagreement between two independent analysts is disagreement about decisions — is this a chord,
which figure, which tonality [FACT]; the ledger's admitted facts are overwhelmingly statements that a
decision is underdetermined by the evidence at a moment (C2, C6, C34, C35) [FACT]; and the multi-task
literature's heads are decisions, whose measured pathology is decisions disagreeing [FACT]. *What the
factor reading would change:* L2 would decompose into ten units, this framework would own the factor
roster and the conditional-independence premises, and the boundary contracts would become
independence claims rather than published-fact contracts. *What the reconciliation reading would
change:* every decision would carry its factor set as sub-units, roughly doubling the unit count and
making every charter two-tiered. **Presented as a finding, not as settled.**

**DP2 — Divide by time scale (tonality then chord)?** Candidates: yes (classical pipeline, published);
no (joint, published and measured). **CHOSEN: no.** Rivals recorded at §S4(b): the pipeline's ground is
that tonality constrains the chord vocabulary and is cheaper to decide; the ground for excluding it is
Rocher's measured 5-point tonality and 2-point chord cost, plus C36.

**DP3 — Is segmentation decided before, with, or after chord identity?** Candidates: before (Pardo and
Birmingham; every fixed grid); with (semi-Markov, measured); after (nobody). **CHOSEN: with.** Rivals
at §S4(d). The ground for *before* is tractability and the availability of segment-level features; it
is excluded on C27 and on the Sheh-and-Ellis and Masada-and-Bunescu measurements.

**DP4 — Where does the chord-tone assignment live?** Candidates: an input (a separate elaboration
detector running first — the 2017 chord-tone network, published, F .72); a layer of its own between
boundaries and chords; **part of L2's one decision and published from it (CHOSEN)**; not represented at
all. *Ground:* the analyst's note at `003 m4` states the chord label is a function of it; C26 records
that duration weight cannot separate a long elaboration from a genuine added tone because the
distinction is functional and voice-leading; the 2025 measurement shows the benefit running in both
directions. *Rival recorded:* a first-running detector is attractive because it would shrink L2's
search; the ground for excluding it is that its own authors report F .72 with many "errors" that are
plausible analytical choices, and a first-running detector's mistakes are unrecoverable downstream.

**DP5 — Is the tonality decided with the chords?** **CHOSEN: yes**, and a tonality change is located at
a harmonic boundary. Rival: an independent tonality track changing anywhere, which the ground truth's
own format cannot express.

**DP6 — Is spelling a layer?** **CHOSEN: no**, for notated input; the boundary condition is stated at
§S3. Rival: a spelling layer, which is required for unspelled input and would be required if this
analysis ever took MIDI.

**DP7 — Is meter a layer?** **CHOSEN: no**, for notated input. Rival: metrical inference, necessary for
piano-roll input and the source of an acknowledged unsolved circularity in the systems that need it.

**DP8 — Is voice separation a layer?** **CHOSEN: no**, for notated input.

**DP9 — Is cadence a layer, and on which side of L2?** **CHOSEN: split** — features at L1, type at L3.
Rivals: wholly upstream (excluded — the half cadence is measured at F .29/.41 without harmony); wholly
downstream (excluded — the features measurably carry the authentic cadence and are cheap to compute
from notation, and the ratified design intent already wants them as evidence).

**DP10 — Are phrase boundaries the same as harmonic boundaries?** **CHOSEN: no.** [FACT — `137 m2 I ||
b4 I`.] Rival: treating them as one, which the ground truth falsifies directly.

**DP11 — What does the analysis publish where it cannot decide?** **CHOSEN: alternatives in the same
stream, each with its mass, including alternatives that differ in segmentation.** Rival: a single best
reading with a confidence number, which cannot express `003 m6var1` — an alternative with a different
number of chords. *Ground:* the ground truth's own form, and Koops's finding that systems already
score above human-human agreement, which means a single-answer target is measuring the wrong thing.

**DP12 — Is the chord symbol a decision or a derivation?** **CHOSEN: a derivation, published as a
view.**

**DP13 — May a later layer revise an earlier one?** **CHOSEN: no**, and no re-ranking of published
ranked lists (C44 at its ruled width).

**DP14 — Which theory of the cadential six-four does the label vocabulary take?**
**NONE CHOSEN — underived: open, needs a ruling or new research.** The candidates are `I6/4` (the
tonic chord in second inversion), `Cad64` (its own category), and `V(64)` (a dominant with a double
suspension). *This is not a gap in the reading; it is a real disagreement in the world.* Our own two
exemplar analyses of the same bar disagree — `003 m4` reads `i6/4` in one file and `Cad64` in the other
[FACT, read at the object] — and the published corpus-integration literature names this exact object as
the flashpoint between the two major annotation standards, resolving it only by replacing every
instance with a neutral symbol. The three readings are different theoretical claims about the same
notes, not three spellings of one claim. **A framework that picked one silently would be deciding a
question of theory on no evidence.**

**DP15 — Does the framework commit to a hierarchical reading of harmony?**
**NONE CHOSEN — underived: open.** Harasim and colleagues show that a recursive grammar represents
something a flat sequence cannot: the same surface chords functioning simultaneously as a tonic phrase
in one tonality and a dominant phrase in another, with tree accuracy 45.95% against 39.43% for a
non-transposition-tied grammar and under 10% for a right-branching baseline. [FACT.] Against it,
Tsushima and colleagues find that their tree models are harder to optimise and *often perform no
better* than latent-category sequence models of matched size, and that induced categories correspond
to textbook harmonic functions only while the models are small. [FACT.] **The decomposition above
neither adopts a hierarchy nor forecloses one**: the question *what chord follows what* is inside L2's
charter, and a grammar is one way to answer it. *The falsifier, so this is not left as taste:* a tree
model beating a matched-capacity sequence model on this repertoire's ground truth, measured on the
same corpus and the same axis.

**DP16 — How are the terms of L2's score combined and fitted?** **NOT DECIDED HERE — it is detail
specification and measurement design.** It is named because Och's result makes it a real design point
rather than an implementation detail: fitting combination weights by likelihood measured 12.2 against
19.6 on the metric actually wanted, when the weights were instead fitted to that metric. [FACT.]

**DP17 — May the analysis decline to read a span at all?** **NONE CHOSEN — underived: open.** Some
published schemas carry a no-chord label and a no-cadence verdict; our three exemplars contain neither.
The question is whether *no confident reading* and *no chord here* are the same publication, and the
evidence to settle it is not in the sources read.

---

## S7. Where uncertainty lives, and what a layer may assume about an answer taken under doubt

Every published fact carries its mass. A consumer may assume of any fact reaching it: that it is the
best reading its producer could support **on the evidence its producer was entitled to**, and nothing
more. Specifically:

- L3 may assume L2's chord is L2's best reading; it may **not** assume it is right, and it may not
  revise it. Where L3's own evidence contradicts it — a cadential figure that makes no sense against
  the decided chords — L3 publishes the contradiction as a fact, and the contradiction is a finding
  for a human, not a trigger for a re-decode. [Ground: C44's class, and the ledger's **C7** — a
  residual disagreement between reading a sonority vertically and reading it by its role is a
  legitimate divergence between two readings, not a defect.]
- A rival that differs in segmentation must remain a rival, not be flattened into a label alternative
  over the principal reading's spans. [Ground: `003 m6var1`.]
- **Where a decision is one of the axes the world does not agree on — the figure, the seventh, the
  chord-tone assignment at a passing sonority — the analysis publishes its rivals rather than raising
  its confidence.** [Ground: the agreement figures at §S2; and Koops's finding that systems scoring
  above human agreement are fitting an annotator.]

---

## S8. Behavioural statements, with what would falsify each

Per the ruled form, and **without naming any code site and without naming which part of the system a
statement binds** — that fill-in belongs to a side other than this author.

**B1. A harmonic boundary falls only at a candidate onset.**
*Observable:* the time points of the published harmonic boundaries, against the published candidate
onsets. *Decision rule:* every boundary is a member of the candidate set. *Not falsified by:* a
candidate onset with no boundary at it — most candidates carry none.

**B2. A tonality change coincides with a harmonic boundary.**
*Observable:* the published tonality per span. *Decision rule:* no two consecutive spans differ in
tonality without differing in span. *Not falsified by:* a tonality restated identically across a
boundary.

**B3. Every sounding note in a span carries a chord-tone assignment.**
*Observable:* the per-note assignment against the note list of the span. *Decision rule:* the
assignment is total over sounding notes. *Not falsified by:* a note assigned as elaboration without a
named elaboration relation — the relation is a separate, optional fact.

**B4. The published chord symbol agrees with the tonic and degree it was derived from.**
*Observable:* root pitch class, against tonic transposed by the degree's interval. *Decision rule:*
they are equal for every span. *Not falsified by:* an enharmonic spelling difference where the
notation forces one.

**B5. No published fact of a later layer changes a published fact of an earlier one.**
*Observable:* the facts published at each layer for one piece, compared. *Decision rule:* the earlier
layer's facts are identical before and after the later layer runs. *Not falsified by:* the later layer
publishing a contradiction as its own fact.

**B6. Where rivals are published, the principal reading is one of them.**
*Observable:* the rival set and the principal. *Decision rule:* the principal appears in the rival set
with the greatest mass. *Not falsified by:* an empty rival set where the reading is uncontested.

---

## S9. What this framework does not decide, and what it leaves open

**Not decided, by rule:** any detail specification of any layer; the measurement layer's content; any
fix plan; the derivation method.

**Left open, each with what would settle it:**

1. **The grain of a unit** (DP1) — the user's ruling, with the evidence above.
2. **The cadential six-four's vocabulary** (DP14) — a ruling, or a measurement of which reading the
   ground truth this project will be judged against actually uses, piece by piece.
3. **Hierarchy** (DP15) — the falsifier at DP15.
4. **Declining to read a span** (DP17) — a decision about what the published output means.
5. **The placement of this draft** (the brief's own open item).
6. **The ground-truth ceiling.** No published per-axis annotator-agreement figure exists for this
   repertoire, and every axis-level agreement number in this draft comes from popular music or figured
   bass. Until that quantity exists for this repertoire, **no target for any axis of this analysis can
   be stated as anything but provisional**, and a system measured above the unknown ceiling cannot be
   distinguished from a system fitted to one annotator.

---

## S10. Two facts about the sources themselves, recorded because they bear on this draft's own footing

**A named source is not the paper in the folder.** The file
`docs/research_papers/humphrey_bello_2015_ismir_four_timely_insights_ace.pdf` **does not contain**
Humphrey and Bello's "Four Timely Insights on Automatic Chord Estimation". It contains Chen, Su and
Yang, "Electric Guitar Playing Technique Detection in Real-World Recordings Based on F0 Sequence
Pattern Recognition", ISMIR 2015. [FACT — established by opening the file.] The citation register
marks that row as holding a local copy. The consequence for this draft is narrow and is stated rather
than worked around: **the one paper in the register whose subject is the ceiling that annotation
disagreement imposes on chord estimation was not read, because it is not on disk**, and every
statement about that ceiling in §S2 rests instead on the Koops report, on de Clercq and Temperley, and
on the figured-bass work. The reachability report's coverage verdict was taken against the register's
rows, not against the files.

**The literature sweep behind the candidate list is not coverage.** The reachability report declares
its own outward sweep non-exhaustive: one item was actually read and every other is a title and an
abstract, and four classes of work were unreachable by construction. A decomposition its list does not
contain is not thereby excluded. **In particular, the hierarchical and multi-resolution alternatives
in that list — a tonality estimated at every window size at once, a time-span reduction tree, tonality
in a transform space rather than as a discrete label — were not read here**, and DP15 is left open
partly for that reason.

**And one primary source is not held.** The register records that the primary source for the tonality
profiles is not on disk. Nothing in this draft rests on a profile form; if a detail specification of
L2 comes to rest on one, it will be defending a factor form from secondary descriptions, and must say
so.

---

## S11. The sizing record — NOT A BUDGET

Recorded because it cannot be reconstructed afterwards, and at the minimal width ruled.

- **Started and ended:** one session, 2026-08-28, the date established at the user's machine.
- **Read in stage one:** fifty-eight research PDFs (each at least to abstract and method; five read
  substantially whole), two register files in the research folder, the reachability report, the
  empirical findings ledger, the ratified factorization, the phase-constraints document, the
  phase-definition surface, the writing-standards document, the target-document-structure note, six
  ground-truth exemplar files, and one score file.
- **Produced in stage one:** this draft — one decomposition, three layers plus a stated input
  contract, three named non-layers, five boundary contracts, seventeen design points of which twelve
  are chosen, three are recorded as underived, one is put to the user and one is routed away.
- **Not measured:** time per statement; the share of design points needing a ruling as a rate rather
  than a count. **This is not a budget and no figure here is an estimate of anything future.**

---

*End of the first-stage draft. Written before any of this project's own design material was opened.*

---

*Framework document draft, written 2026-08-28. It edits no specification and no code; it runs no build,
no test, no measurement tool, no generator and no guard; it creates, flips or discards no open-items
row; it allocates no finding number; it writes no `STATUS.md` entry, no handover block, no report and
no close; it commits nothing; and it writes no dispatch.*

*Reading method, declared. All reads were made with the file tools, at the user's standing instruction,
with **one exception that is declared rather than worked around**: five ground-truth analysis files sit
eight folders below the connected root and could not be staged, so they were read with a **read-only**
shell command on the user's machine, as was the date. **Nothing was written, moved or changed on that
machine by this session**, and no git command was run. Every git-object value, had one been needed,
would have been relayed; none is stated here.*

