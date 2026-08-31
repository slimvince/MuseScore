# EXTRACT — Lazzari 2023, "Knowledge-Based Chord Embeddings" (the Modal Harmony Ontology) — population row 7, CENTRAL-adjacent, first pass

> **STATUS: FIRST-PASS EXTRACT, READ AT THE OBJECT (session 3 of the reading pass, 2026-08-31).**
> Written under `cowork_reading_pass_commission_2026_08_30.md` §4.
>
> **★ ROW 7's STOP IS RESOLVED. The user supplied the document** — the third time a blocked row has
> closed by that route, after rows 15 and 19. **The workbook was NOT opened**; the file sits beside it
> in the same folder and a supplied PDF is not the workbook.
>
> **GRADE: AT THE OBJECT, DECLARED PARTIAL.** 129 pages, staged through the bridge and read as page
> images. **Read whole:** front matter and abstract; contents; ch. 1 (introduction, contribution,
> structure); ch. 2 opening; **ch. 4 entire — the row's own subject**; §5.1 and §5.2 opening (what the
> headline accuracy measures); **ch. 6 entire**; ch. 7 entire; ch. 8 entire; the bibliography's
> opening. **NOT read in detail:** ch. 2 (background), ch. 3 (related work), §§5.2–5.5 (the embedding
> methods and their own experiments). *A deeper read of ch. 5 is its own slice if ordered.*

## Identity — and the row is confirmed at the object, not inferred

**Nicolas Lazzari, "Knowledge-Based Chord Embeddings"**, Master thesis in Knowledge Engineering,
Artificial Intelligence, Department of Computer Science and Engineering, **Alma Mater Studiorum —
Università di Bologna**, academic year 2021–2022, session 4. Supervisor **Valentina Presutti**,
co-supervisor **Andrea Poltronieri**. 129 pages; the file's own production date is January 2023.

**Why eight searches missed it: it is a master's thesis**, indexed as a paper nowhere the pass's
queries could reach.

**The list's description is confirmed on both halves, at the object.**

- *"the Modal Harmony Ontology"* — the abstract, verbatim: **"We design and implement the Modal
  Harmony ontology (MHO), using OWL (the standard web ontology language). It formalises one of the
  most important theories used to interpret western music: the Modal Harmony Theory."**
- *"all seven modes formalized"* — §4.1: **"Seven scales are defined by TMH: Ionian, Dorian, Phrygian,
  Lydian, Mixolydian, Aeolian, and Locrian."**
- *"multiple modal interpretations returned per progression"* — **Table 4.1**, §4.3.1. See below.

**★ AND IT IS A DISTINCT WORK FROM ROW 6, WHICH SETTLES THE OPEN QUESTION IN THE OPPOSITE DIRECTION
FROM THE LEAD.** The pass's live lead was that row 7 might dissolve into row 6 (the NTUA
description-logic line). **It does not.** This is a different group at a different institution, and it
cites row 6's family as *related work* at its own §3.1.3, "Functional Harmony Ontology". **The
decision surface delivered hours earlier recommended AGAINST closing row 7 into row 6 on #19 grounds
— that half the description did not match and an unfalsified resemblance is not an identification.
The document establishes that the recommendation was right and the tempting option would have
dropped a real paper.**

## Claims, labeled

### The theory formalised

**[FACT, §4.1]** MHO formalises **Modal Harmony Theory (TMH)**, sourced to *The Jazz Theory Book*
(Levine) and *Music in Theory and Practice Vol. 1* (Benward). Verbatim: **"the theory of Tonal
Harmony, based only on Major and Minor scales, is a proper subset of the theory of Modal Harmony."**

**[FACT, §4.1]** Each of the seven scales is built from a degree of the major scale, and a scale
carries both a **root** and a **tonality** — E Phrygian has root E and tonality C. The seven positions
are named **tonic, supertonic, mediant, subdominant, dominant, submediant, leading-tone**, and a chord
built on a position takes that role. Verbatim: *"each chord can be classified with a role based on the
context it is interpreted in. This allows the classification of a chord based on its function (i.e.
its role) within a scale and is the basis of Functional Harmonic Analysis."*

### The ontology, and how it is built

**[FACT, §4.2]** MHO **imports and extends two existing ontologies** — the **Chord Ontology** and the
**Music Theory Ontology (mto)**. The extension adds **24 missing intervals** (mostly compound) and
**56 additional chord qualities**.

**[FACT, §4.2]** **Chord quality is inferred from constituent notes by OWL reasoning**, not asserted.
Quoted axiom: `Class: MajorTriad EquivalentTo: (chord:interval value mto:MajorThirdInterval) and
(chord:interval value mto:PerfectFifthInterval)`. A Tristan-chord axiom is given as a worked case
(augmented fourth + augmented sixth + augmented ninth). Inference runs in the **OWL-EL profile**,
*"able to perform inference in polynomial time"*.

**[FACT, §4.2.1]** The scale-to-chord relation cannot be inferred by domain and range axioms alone, so
the ontology uses the **rolification** technique — property-chain axioms encoding *if-then* rules in
OWL2. **Algorithm 1** automates the rolification, at **O(|P|)** in the number of properties; it needs
inverse properties, hence **OWL-DL** in general, though some reasoners allow inverses under EL.

**[FACT, §4.2.1]** *"The final ontology is automatically generated by using the music21 library to
retrieve the association between a modal scales and its notes."* **A total of 6,344 axioms.**

**[FACT, §4.2.1] Quality restrictions are declared to be genre-dependent and editable:** *"They can be
updated by domain experts and eventually refined given the domain of application of the ontology …
the concept of tonic chord is slightly different between Rock music and Jazz."*

### The knowledge graph and what it answers

**[FACT, §4.3]** The KG's entities are extracted from **ChoCo** — **which is population row 8 of this
same pass** — loaded into Stardog under EL reasoning. **7,651 chord individuals.**

**[FACT, §4.2/§4.3]** Six competency questions, each answered by a SPARQL query given in full: which
notes are in a mode; what is the role of a note in a mode; in which role can a note be classified;
which chords are in a mode; which are the roles of a chord; which chords absolve a role.

### ★ Table 4.1 — the row's own description, at the object

**[FACT, §4.3.1]** For the progression **C:maj – G:maj – A:min – F:maj**, the query returns **ten scale
readings with their Roman annotations**:

| Scale | Roman annotation |
|---|---|
| F Lydian Mode | V ii iii I |
| D Dorian Mode | °vii IV V iii |
| A Aeolian Mode | iii °vii I vi |
| F♯ Minor Scale | iii °vii I vi |
| G Dorian Mode | IV ii °vii |
| G Mixolydian Mode | IV I ii °vii |
| E Phrygian Mode | vi iii IV ii |
| B Locrian Mode | ii vi °vii V |
| C Ionian Mode | I V vi IV |
| C Major Scale | I V vi IV |

*Partial annotations — where a scale contains only a subset of the progression's notes — were
manually removed.* The thesis's gloss: *"The traditional I - V - vi - IV annotation is correctly
retrieved by the query, alongside many other annotations. Each of this can be seen as a different way
to musically interpret the chord sequence."*

**★ [FACT] THE ENUMERATION CARRIES NO MASS, NO RANKING AND NO CONFIDENCE.** Ten readings are returned
as a set, derived from scale membership; nothing in the method prefers one over another, and the
traditional reading is one row among ten with no marker distinguishing it.

**★ [FACT — the author's own bound, and it governs how any of this may be quoted] IT IS A PROOF OF
CONCEPT, NOT AN EVALUATED METHOD.** Verbatim: *"the query in Listing 4.11 can only handle simple
notations and should be seen as a proof of concept of applying the KG to the roman annotation task.
We claim, however, that by extending the presented query into a proper annotation system it would be
possible to obtain a method that is directly comparable to the related works. We will investigate
this option in future works."* **There is NO evaluation of the Roman-notation inference anywhere in
the thesis** — no corpus, no ground truth, no accuracy. Complex Roman notations such as parallel
chords are explicitly out.

**[FACT, §4.3.1] One property worth carrying: the query needs nothing but the chords.** *"does not
require any additional information besides the chord progression itself"* — contrasted in the same
paragraph with music21, for which *"a prior knowledge of the reference scale within which the
progression should be interpreted needs to be explicitly provided."*

### ★ What the headline 0.86 actually measures — established at §5.1, not taken from the abstract

**[FACT, §5.1]** The abstract's *"chord classification … accuracy: 0.86"* is the **Odd One Out**
intrinsic embedding metric: given a set of chords and one outsider, does the embedding place the
outsider furthest from the set's mean. **k = 4, 1,000 runs, 10 randomly sampled sets; random baseline
E[acc] = 1/5 = 0.2.**

**★ AND THE CLASSIFICATION IT IS SCORED AGAINST IS THE ONTOLOGY'S OWN.** Verbatim: *"The
classification is performed using the Knowledge Graph described in Chapter 4. In particular, we
consider 10 sets C by randomly sampling scales and the corresponding chord functions from the KG."*
**So 0.86 measures how well an embedding reproduces the knowledge graph that generated its labels.
It is an internal-consistency figure, not an accuracy against any human annotation**, and it must
never be quoted as one.

**[FACT, §5.1]** Training data: ≈16,000 chord progressions, over 1M chord instances, from ChoCo
(>20,000 tracks, 18 datasets), parsed to JAMS and converted to Harte notation.

### Structure segmentation — Chapter 6

**★ [FACT, §6.1.1] IT IS SECTIONAL FORM SEGMENTATION, NOT HARMONIC BOUNDARY SEGMENTATION**, and the
thesis draws the distinction itself: musical form study *"can be divided in two main categories:
phrase-structure segmentation and global segmentation"*, and from that point *"we refer to global
music structure segmentation as music structure segmentation"* — *"identifying and labelling key
music segments (e.g. chorus, verse, bridge)"*. Also: *"A correct segmentation does not necessarily
assign the correct labels to each section … but rather focuses on the correct estimation of the
boundaries of each section."*

**[FACT, §6.1.3]** Data: the **Billboard** dataset, **889 expert-annotated tracks**, chords in Harte
format with section labels; 80 unique section labels reduced to **11**. Model: a stacked **LSTM**, 5
layers, hidden dimension 256, dropout 0.2, binary cross-entropy.

**[FACT, §6.1.4] Table 6.2, pairwise precision/recall/F1 and the entropy-based under/over-segmentation
scores, all via `mir_eval`:**

| Model | P | R | F1 | S_U | S_O | S_F1 |
|---|---|---|---|---|---|---|
| FORM_raw | **0.673** | 0.337 | 0.420 | 0.673 | 0.337 | 0.420 |
| FORM_simple | 0.663 | 0.340 | 0.423 | 0.663 | 0.340 | 0.423 |
| fasttext | 0.616 | 0.604 | 0.596 | 1 | 1 | 1 |
| pitchclass2vec | 0.617 | 0.591 | 0.586 | 1 | 1 | 1 |
| **rdf2vec** (the ontology-only embedding) | 0.619 | 0.584 | **0.581** | 0.962 | 0.926 | 0.944 |
| **meta-embedding** | 0.624 | **0.608** | **0.598** | 1 | 1 | 1 |

**[FACT, §6.1.2]** FORM is named as *"the only approach proposed in literature for global music
segmentation on symbolic harmonic content"* — a suffix-tree method over chord strings, re-implemented
by the author for comparison.

**[FACT, §6.1.4] Label leaking is identified and addressed:** the embeddings were retrained from
scratch on a ChoCo subset **with the whole Billboard dataset removed**, because training embeddings on
Billboard could leak section information. *Declared and acted on, which is better practice than most
of the population.*

**[FACT, §6.1.4]** Against audio: *"State-of-the-art results are obtained by approaches based on
Convolutional Neural Networks, with a pairwise F1 scores of 58.09 ± 15.77 which is a similar result to
the one obtained on Table 6.2."* **The thesis reports no variance for its own figures**, so the
"similar result" comparison is against a mean with a ±15.77 spread and no significance test.

**★ [OBSERVATION — FLAGGED, NOT ASSERTED AS AN ERROR] Three of the six models score exactly 1.000 on
all three entropy-based measures (S_U, S_O, S_F1) while their pairwise F1 sits near 0.59.** The thesis
does not remark on it. It is recorded here because the thesis's own Figure 6.3(c) warns that
*"Pairwise metrics can be misguiding in absence of S_O and S_U"* — so the measures brought in as the
corrective are the ones reading saturated. **This side has not established a cause and does not claim
one; a reader relying on those columns should look at them before quoting them.**

### Theory and conjecture

**[THEORY]** Modal Harmony Theory itself, and the OWL/description-logic machinery (rolification,
EL/DL profiles) are established published work applied here, not established by this thesis.

**[CONJECTURE, ch. 7–8]** Extending MHO to model melodies; expanding the Roman-notation query into a
proper annotation system; using the embeddings to enhance automatic chord transcription and
cover-song detection. All stated as future work.

**[FACT, ch. 7 footnote]** Two further Polifonia artefacts are named: the **Modal Tonal ontology** and
the **Tonalities pilot**. **Neither is read**, and neither is added to the population here.

## Coupling facts (the commission's mandatory widening)

**ASSUMES upstream:** **chord LABELS in Harte notation** and nothing else. **No notes, no score, no
metre, no voices, no key, no segmentation.** For the ontology's classification: a chord expressed
through the Chord Ontology (root plus intervals). For the Roman-notation query: the chord progression
alone — explicitly *not* a reference scale. For the segmentation model: a chord sequence plus section
labels for training.

**HANDS downstream:** a SPARQL-queryable knowledge graph; per-chord role classifications within a
named scale; **an unranked, unweighted enumeration of scale readings with their Roman annotations**;
chord embedding vectors; and, from Chapter 6, section boundaries and labels. **No confidence and no
mass on anything.**

**ITS OWN STATED SCOPE:** Western tonal and modal music at the **chord-label level**; the
Roman-notation inference is a proof of concept handling simple notations only; the segmentation
evaluation is **popular music** (Billboard). It infers no chord from notes and estimates no key.

## Bearing — flagged for the user and for any later verdict, NOT decided here

- **★ The mode question** (routed by the disposition surface to the L2 detail specification, the
  measurement design and the style system). **This is the fullest formal seven-mode vocabulary the
  pass has read**, with roles, quality restrictions per mode, and Tonal Harmony stated as a *proper
  subset* of Modal Harmony. **But it classifies GIVEN chord labels against a GIVEN scale; it infers no
  mode from notes**, so it is a vocabulary and a reasoning scheme, not a mode-detection method. It
  sits beside row 6 (a seven-mode functional ontology, likewise inferring nothing from notes), row 9
  (four-mode detection with the tonic given), row 10 (major-minorness as a continuum) and row 11 (the
  DCML standard's two-valued key axis).
- **★ DP-K — and this is the sharpest thing the row contributes.** MHO **publishes multiple readings**
  — ten for a four-chord progression — which is superficially DP-K's shape. **It publishes them with
  no mass, no ranking and no evidence separating them.** That makes it the **third** system in this
  population to publish alternatives without mass, after HarmTrace's rule-order precedence and row 6's
  flat function classes. **Read together they are an existence proof of what "publish the rivals"
  degenerates into when nothing scores them**, and they show that the load in DP-K's chosen wording is
  carried by the clause *"each with its mass"* rather than by the plurality. *Whether that strengthens
  DP-K's record is a verdict, and is not taken here.*
- **L3's phrase and section grouping.** Sectional form recovered from the **chord stream alone** at
  F1 ≈ 0.60, against 0.42 for the only prior symbolic method and 58.09 ± 15.77 for audio
  state-of-the-art. **Pop repertoire, section labels rather than phrase boundaries**, so it does not
  transfer to L3's own object without argument — but it is evidence that sectional structure is
  substantially recoverable from harmony, which is the direction L3's charter takes.
- **DP-J** — untouched: nothing here compares phrase boundaries with harmonic boundaries.
- **§7 data design / DP-L** — the chord-quality-from-intervals inference by OWL reasoning is a third
  independent instance, beside rows 3 and 8, of the field treating the chord label as **derived** from
  a structured description rather than as a primitive.
- **NO FALSIFIER CANDIDATE against any chosen design point.** Every point this row touches is either
  chosen and unthreatened or already open.

## What this extract does NOT establish

- The contents of chapters 2, 3 and §§5.2–5.5, not read in detail.
- The full experimental detail behind the 0.86 figure (§5.4) — **what it measures is established at
  §5.1**, which is the part that governs how it may be quoted.
- The cause of the saturated S_U / S_O / S_F1 values in Table 6.2.
- Whether MHO has been adopted or evaluated by anyone since.
- The Modal Tonal ontology and the Tonalities pilot, named and not opened.

*Provenance: session 3 of the reading pass, 2026-08-31. Read AT THE OBJECT from
`external resarch summary/Tesi___Knowledge_based_chord_embeddings_nicolas_lazzari.pdf`, staged
through the bridge; the file was supplied by the user and is **not moved** — the folder carries his
signature-table classification. **The workbook beside it was not opened.** No specification derived,
no document amended, no code opened, no register row or entry written.*
