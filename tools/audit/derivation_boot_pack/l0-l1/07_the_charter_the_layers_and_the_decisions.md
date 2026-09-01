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
whole texture cannot hold them. 

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

## 9. Architecture decisions

Per the ruled output form: candidates enumerated from every source kind with establishment status; **at
most one chosen per concern, or NONE** written as *underived*; and the rivals recorded in the defense,
so that a later reader can re-test whether the ground for excluding each still holds.

### 9.0 The prior question: what is a unit? — SETTLED: a unit is a DECISION the analysis makes about the music

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

**SETTLED BY THE USER, 2026-08-31 — Ruling 8 of
`cowork_rulings_2026_08_31_decision_surface_sitting.md`.** A unit of this architecture is a
**decision the analysis makes about the music** — the second of the three readings above. **A factor
is not a unit:** §0 states that a factor is *"a means of computing a decision, never a decision."*
**The factor roster and the terms that rate candidate readings stay inside L2's detail
specification**, where §5's L2 charter and DP-P already place them.

**★ THIS SECTION'S HEADING AND ITS CLOSING SENTENCE WERE CORRECTED 2026-08-31 ON THE USER'S RULING,
WITH BOTH FORMER WORDINGS PRESERVED IN PLACE (#12.)** Ruling 8 of
`cowork_rulings_2026_08_31_decision_surface_sitting.md` §3g — Option A, the grain of a unit is the
decision; the user's words, verbatim, *"Agree on A"* — scoped into a narrow batch of its own by
Ruling 18 (§3r) of the same record. **THE FORMER HEADING WAS:** *"### 9.0 The prior question: what is
a unit? — PUT TO THE USER, NOT SETTLED"*. **THE FORMER CLOSING SENTENCE WAS:** *"**Stated as this
phase's first ratified finding, for the user to rule. It is not settled here.**"* — each quoted with
its own heading marker and emphasis markers intact. **Both are SUPERSEDED**: each said the question
was open, which it ceased to be when the ruling stood, and a governing surface that misstates the
record on the prior question is the one statement in it most
able to bend a derivation written under it. *Why the words are kept rather than deleted:* a
preservation block is marked as superseded and so reads as history, and removing it would hide from
a later reader that the charter has been corrected. **The three candidate readings above, the
evidence paragraph and the what-each-reading-would-change paragraph are outside the ruled edit and
are untouched**; an excluded alternative is evidence about the choice. **No design point is
reopened, and no charter, boundary contract or other section of this document is edited by that
ruling.**

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
**A framework that picked one silently would be deciding a question of theory on no evidence.** 

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
*no chord here* are the same publication. 

---
