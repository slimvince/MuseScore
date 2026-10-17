# The blind derivation of L3 — the read-off facts: cadence and its type, phrase and section grouping, chord symbol, figured bass, harmonic rhythm

> **STATUS: DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED.**
> Written 2026-10-17 by a fresh Cowork session with nothing mounted, under the brief
> `cowork_blind_session_brief_l3.md` (released 2026-10-17). The file name carries the brief's date, which
> was fixed in advance. Nothing in this file has been compared with any text this project already holds.
> Nothing in it is a verdict on anything this project currently does.

---

## 0. Terms

Standard music theory is used in its standard sense. A reader who knows music theory and nothing about
this project needs only this table. The reserved-word rule binds the whole file. Bare *key* means
tonality; *bar* is the metric unit; bare *score* is a musical score, and the numerical sense is always
*candidate score*; *note* is a pitch event; *figure* is the figure of a chord or a figured-bass figure;
*root* is a chord root; *resolution* is the resolution of a dissonance; *rest* is the notated silence;
*part* is a musical part.

| Term | Meaning in this file |
|---|---|
| **The analysis** | The harmonic-analysis software this project builds. |
| **L0, L1, L2, L3** | The layers of the ratified charter (pack member 07). L0 is the notated record. L1 publishes slices, the lowest sounding pitch per slice, metric strength, notated boundary evidence, per-voice relations and cadence cues. L2 makes the one entangled decision: segmentation, tonality, chord, chord-tone assignment, with rivals. **L3 is this file's subject.** |
| **The charter** | Pack member 07: each layer's question, inputs and outputs. Given. |
| **IC-L1** | The ratified L0/L1 specification, cut for this session (`the_l0_l1_specification_the_input_contract.md`). Its statements are cited **IC-L1 S-n**. Given. |
| **IC-L2** | The ratified L2 specification, cut for this session (`the_l2_specification_the_input_contract.md`). Its statements are cited **L2-Sn**. Given. |
| **Event, onset, release, change point, slice, sounding set** | As IC-L1 §0 defines them. A change point is an onset or release of an eligible event. A slice is the half-open stretch between consecutive change points. |
| **Working span** | The stretch of music the caller asks the analysis to read (IC-L1 S-32; L2-S48). |
| **Harmonic span** (or *span*) | One stretch of L2's segmentation, carrying one tonality and one chord (charter; IC-L2 §0). |
| **Chord, as L2 decides it** | Four fields (IC-L2 §0): **degree** (with alteration), **quality**, **figure** (which chord member is in the bass, together with the seventh or other added members), **applied target** (a chain, possibly empty). |
| **Structural bass** | The chord member L2's figure names as the bass of a span. By L2-S28 it is not necessarily the lowest pitch sounding at any slice of the span. |
| **Assignment, elaboration relation** | L2's per-event, per-span decision: chord tone, or elaboration with one of passing, neighbour, suspension, anticipation, appoggiatura, escape tone, pedal point, or unclassified elaboration (L2-S8). |
| **Reading, principal reading, rival** | A reading is one complete candidate answer of L2 for the working span. The principal reading is the one L2 commits. A rival is an alternative L2 publishes beside it (L2-S40 to L2-S42). |
| **Whole reading, rival object, span-rival** | L2 publishes three rival forms. *Span-rivals* are per-span marginals (L2-S40). *Rival objects* are alternatives covering several consecutive spans (L2-S41). *Ranked whole readings* are complete readings of the span, listed down to a bound (L2-S41, L2-S42). |
| **Mass** | The model's own probability of a reading, normalised over whole readings. It is neither a decision margin nor a calibrated probability. It may be compared only within one working span's publication (L2-S40). Not redefined here. |
| **Withheld mass** | The total mass L2 does not publish below its effort-setting cut-off, which L2 publishes per span (L2-S42). |
| **Establishment status** | The status every published item carries: *notated*, *computed*, *provisional* at L1 (IC-L1 S-52), and on L2's items (L2-S45). This file adds the L3 values at L3-S33. |
| **Read-off fact (a view)** | An L3 fact computed from facts L2 has already decided. Nothing new is decided in computing it. The charter's example is the chord symbol. |
| **L3 decision** | An L3 fact that is not fixed by L2's facts and that L3 settles among rivals. The charter's case is the phrase reading: which notated phrase evidence marks a phrase end, and how phrases group into sections. |
| **Phrase end** | The last moment of a phrase as L3 decides it, given as a position in the record (a change point or span edge). |
| **Cadential arrival** | The position at which the final harmony of a cadential progression begins. It lies at or before the phrase end it closes, and need not coincide with it (L3-S10). |
| **Elided phrase boundary** | A position that is both the cadential arrival closing one phrase and the beginning of the next phrase. |
| **Section** | A group of consecutive phrases that L3 publishes as a unit of the grouping. Sections may nest. |
| **Figured bass** | In this file: the thoroughbass figures (the intervals above a bass, with accidentals, and with suspension and resolution figures) describing the harmony L2 decided, published by L3. It is distinct from the **composer's figures**, the figures the notation itself carries. IC-L1 S-8 makes those annotation. |
| **Harmonic rhythm** | The pattern in time of the changes of harmony. Its published form is L3-S30. |
| **Exemplar 1, 2, 3** | The staged files of the brief §3.2. Exemplar 1 is `K545-1.mscx` with its inline analysis. Exemplar 2 is `analysis_DT.txt`, a second analysis of the same movement. Exemplar 3 is `op01n08a.mscx` with its inline analysis and its notated figures. They are **met as cases and never counted**. |
| **FACT / THEORY / CONJECTURE / RULED** | **This session fetched no paper.** Every FACT from the literature is therefore a *relayed* FACT: stated in pack member 08's extract, which records that it was read at the object. It is labelled **FACT (relayed, 08)**. A FACT read at a staged file is labelled **FACT at the file**. **THEORY** is established published theory, and none of its sources was fetched this session, which each THEORY label says. **CONJECTURE** is this session's own reasoning. **RULED** is a claim fixed by the charter or by one of the two input-contract files, cited by its identifier. |
| **Source class** | *derived*; *given* (split as *given — charter*, *given — IC-L1*, *given — IC-L2*); or *measured* (it rests on a fit this session cannot make, and carries no value). |
| **L3-Sn, OQ-L3-n** | The statements of §3 and the open questions of §4 of this file. The numbering follows the L2 specification's own form (L2-Sn, OQ-L2-n) and implies no other scheme. |

**Reading the exemplars' own analytical notation.** These are this session's readings of the files'
notation. Exemplars 1 and 3 carry no legend.

- In the `<Harmony>` elements of exemplars 1 and 3, `{` is read as the beginning of a phrase and `}` as
  its end. `|HC` and `|PAC` are read as half and perfect authentic cadences labelled at the chord they
  are attached to. A prefix `X.` (as in `V.V{`, `v.i{`, `IV.IV6`) is read as a change of local tonality
  to the degree X of the home tonality. `/x` is read as an applied (tonicised) reading. Parenthesised
  digits (as in `V(64)` and `V(4)`) are read as suspended or elaborating intervals above the chord.
- Exemplar 2 is in the plain-text format its header and syntax show: `mN` is a bar, `bK` a beat,
  `Form:` a section label, and `G:` a tonality change.
- **Alignment of exemplar 2's bars with exemplar 1, an assumption stated as the brief requires.** Bar *n*
  of exemplar 2 is taken to be the *n*-th `<Measure>` of exemplar 1's staves in notated order. Both
  have 73 bars, and exemplar 1 has no incomplete opening bar. Exemplar 2 writes no repeat signs.
  Exemplar 1 carries an end-repeat at its bar 28, a start-repeat at its bar 29 and an end-repeat at
  its bar 73. The assumption was checked at four bars. At bar 4, exemplar 1 has `V6 V65 I}` and exemplar
  2 has `V6/5 b3 I`. At bar 11, both carry four harmonies at the same four beats. At bar 24, exemplar 1
  has `V(64)` and exemplar 2 has `I6/4`. At bar 41, exemplar 1 has `IV.IV6 … V7` and exemplar 2 has
  `N6 F: IV6 b3 V7`.

---

## 1. The subject, and a finding on the brief's decomposition

**The subject**, in the brief's words: *how does this layer read each of those facts from what L0, L1
and L2 publish, in what form does it publish each fact and its uncertainty, and what does it never do?*

**Finding on the decomposition.** Faces (a) to (h) work as a checklist, and every face receives
statements in §3. Five things the faces leave out, or split in a way that hides something, are
recorded here and repeated in §7.

1. **L3 holds two kinds of fact, and the faces mix them.** The chord symbol, the figured bass and the
   harmonic rhythm (faces (a), (e), (f)) are *views*: deterministic functions of L2's decided facts and
   of L0 and L1 facts. The phrase ends and the section grouping (faces (b), (d)) are *decisions* that L3
   makes among rivals. The cadence type (face (c)) is a view of L2's chords, read at a position that an
   L3 decision fixes. Face (g) therefore splits in two: a view inherits all its uncertainty from L2
   (L3-S34), and a decision adds uncertainty of its own (L3-S35).
2. **A phrase end and a cadential arrival are two positions, not one.** Face (b) asks where a phrase
   ends and face (c) asks for the cadence. The charter's alignment rule couples the two. Exemplar 1
   places a cadence label at one chord and the phrase-end sign at a later one (bars 11 and 12, and
   again at bars 56 and 57), while exemplar 3 writes both on one chord. This is written
   at L3-S10.
3. **The cadence vocabulary is theory-dependent, in the same way as the cadential six-four of DP-N.**
   Face (c) asks *which cadence types are read* as though one answer existed. The published traditions
   differ on whether an inverted-dominant close, a plagal close and a deceptive close are cadences at
   all. This is written at L3-S17 and OQ-L3-2.
4. **The charter's boundary table has no L0 → L3 row**, although L3's consume line names L0. L3-S37
   reads the consume line as governing.
5. **Harmonic rhythm risks being a second home for L2's segmentation.** The faces do not say what
   harmonic rhythm adds beyond the span list. L3-S30 answers that, so the segmentation is not published
   twice.

---

## 2. How to read a statement

Each statement carries the brief's six fields, §4:

1. **Statement.**
2. **Defense.** Each load-bearing claim is labelled FACT (relayed, 08), FACT at the file, THEORY,
   CONJECTURE or RULED.
3. **Source class.**
4. **Status.**
5. **Premise, and its false-negative path.**
6. **Falsifier.** For a statement about behaviour this is CODE: the observable, the decision rule, and
   a near-miss that does not falsify. For a modelling premise it is RESIDUAL.

Where a statement uses an exemplar, the exemplar illustrates a case and is never evidence of a rate.

---

## 3. The statements, face by face

### 3a. Face (a) — the chord symbol: root, quality, bass note

**L3-S1. The chord symbol is a view of L2's chord. For every harmonic span of every L2 reading L3 reads,
it is the deterministic function of that span's four chord fields and its tonality that L3-S2 to L3-S5
define. Nothing is decided in computing it, and it reads no sounding note. It is published per span of
the principal reading, with a reference to the L2 span it is read off, and per L2 rival under L3-S6.**
- *Defense.* The charter's own words: *"The root is the tonic transposed by the degree's interval.
  Nothing is settled in computing it. Publishing it as a decision would create a second home for one
  fact and a second chance to disagree with it"* [RULED — charter, L3; DP-L, "a derivation, published
  as a view"]. L2 publishes no root and no bass note, *"That is L3's read-off"* [RULED — L2-S27]. The
  measured pathology the charter cites is a composite label assembled from parts decided separately
  [RULED — charter, DP-A]. One published system that factors the label into root, quality and bass
  gains on the full-chord column and hardly at all per element. The gain is coherence between parts,
  not accuracy of any part [FACT (relayed, 08) — BACHI, ablation]. A view of one decided chord is
  coherent by construction, because all three parts are read off the same four fields.
- *Source class.* Given — charter (view, nothing settled). Derived (per span, per rival, the reference).
- *Status.* Settled.
- *Premise.* The four fields and the tonality determine the root, quality and bass. **False-negative
  path:** a chord class for which theory defines no root (L3-S5 (i)). There the function is partial,
  and the gap is published with a named reason rather than filled.
- *Falsifier.* CODE. **Observable:** the chord symbol of each published span, with the L2 fields it
  references. **Decision rule:** falsified if two spans with identical tonality and identical four
  chord fields receive different chord symbols; if a chord symbol changes when any sounding note is
  changed with every L2 field held fixed; or if a chord symbol carries no reference to an L2 span.
  **Not falsified by:** two spans with different chord fields that receive the same chord symbol (a
  pivot, or relative-key readings; see L3-S6).

**L3-S2. The root is spelled. It is the span's spelled tonic transposed by the diatonic interval of
the degree, with the degree's alteration applied. For an applied chord, the chain is resolved from its
far end: the root of the target degree is found in the span's tonality, that root is taken as a
temporary tonic, and the next degree of the chain is read against it, until the chord's own degree is
reached. The pitch class the charter names is published in the same item as the spelled root's
projection.**
- *Defense.* The charter: *"the tonic transposed by the degree's interval"* [RULED — charter, L3]. The
  tonic is spelled (L2-S1, L2-S6, 42 spelled tonalities) [RULED — IC-L2]. A spelled root distinguishes
  what the notation distinguishes, for example C♯ against D♭. A published representation keeps spelled
  and generic pitch classes as distinct types, with conversion one way only, from spelled to generic,
  never back [FACT (relayed, 08) — Hentschel et al. 2021, §model]. So the spelled root is the fact and
  the pitch class is its projection. Publishing only the pitch class would lose what cannot be
  recovered, against the pack's principle #12. The chain rule is the meaning of an applied chord
  [THEORY — standard harmony; no source fetched]: V7/IV/III in C minor is the dominant seventh of the
  subdominant of E♭ major, a chain of depth two that L2 admits (L2-S5) [RULED — IC-L2]. IC-L2 records
  an analysis that writes it [RULED — L2-S5]. None of this session's exemplars writes a chain of depth
  two; exemplar 3 writes chains of depth one, such as `V(4)/iv` and `#viio6/iv` [FACT at the file].
- *Source class.* Given — charter (the transposition). Derived (spelling, the chain order, the
  projection).
- *Status.* Settled in shape. **Open** on one input: how a degree numeral in the minor mode reads the
  sixth and seventh degrees (OQ-L3-1).
- *Premise.* L2's degree field, with its alteration, names one scale step against one reference
  collection. **False-negative path:** IC-L2 defines the degree as *"the scale step of the chord's root
  relative to the span's tonality, with any chromatic alteration, such as ♭II or ♯IV"* (IC-L2 §0). In
  the composite minor, whose sixth and seventh degrees *"may each be raised or not"* (L2-S21), the file
  does not say which form an unaltered VI or VII names. Exemplar 3 writes `viio/VII` (an applied chord
  whose target is an unaltered VII) and `#viio` in C minor, in the same bar [FACT at the file]. That
  shows a tradition in which unaltered VII is the lowered form and `#` marks the raised one, but it
  fixes nothing for L2's field. A wrong reading here moves a root by a
  semitone. It is written as OQ-L3-1, naming IC-L2 §0 and L2-S21, and is not filled.
- *Falsifier.* CODE. **Observable:** roots of applied and minor-mode chords. **Decision rule:**
  falsified if the root of V7/IV/III in C minor is not E♭ (the dominant of A♭, which is the subdominant
  of E♭, the mediant of C minor);
  if a spelled root is replaced by an enharmonic equivalent; or if the published pitch class is not the
  spelled root's projection. **Not falsified by:** two different spelled roots that share one pitch
  class in two different spans.

**L3-S3. The quality is L2's quality field, carried unchanged into the chord-symbol vocabulary: major,
minor, diminished, augmented, the five seventh qualities, and the augmented sixths. The Neapolitan is
a major triad on the lowered second degree. Nothing in the quality is re-read from the sounding notes.**
- *Defense.* L2 decides the quality as part of the chord (L2-S27) [RULED — IC-L2]. Its vocabulary is
  L2-S4's [RULED — IC-L2]. Re-reading the quality from the notes would decide it a second time, which is
  what the charter forbids for the chord symbol [RULED — charter, L3]. A second reason: pitch-class
  content does not fix the quality, since an added-sixth chord and a seventh chord on the related root
  share their content [FACT — ledger C6]. A published integration of annotation standards states that
  converting a Roman numeral to an absolute chord label loses the functional information. Its rule is
  therefore additive: the converted label is kept beside the original, never in place of it [FACT
  (relayed, 08) — de Berardinis et al. 2023, ChoCo, §workflow]. Here, the chord symbol stands beside
  L2's chord and never in place of it.
- *Source class.* Given — IC-L2 (the field). Derived (no re-reading; the additive placement).
- *Status.* Settled.
- *Premise.* Every L2 quality has a chord-symbol counterpart. **False-negative path:** the augmented
  sixths, which carry a quality and no root in the theory that names them (L3-S5 (i)).
- *Falsifier.* CODE. **Observable:** the quality field of the chord symbol against L2's. **Decision
  rule:** falsified if they differ for any span, or if the chord symbol replaces L2's chord in any
  published record. **Not falsified by:** the chord symbol writing the quality in a different notation
  (`m7` for minor seventh).

**L3-S4. The bass note is the chord member that L2's figure names, spelled from the root and quality.
It is the structural bass, not the lowest sounding pitch of any slice. Where the two differ, the chord
symbol shows the structural bass.**
- *Defense.* L2's figure is *"which chord member is in the bass"* (IC-L2 §0), and the figure is *"the
  chord member the reading takes as the span's structural bass, which is not necessarily the lowest
  pitch sounding at the span's first slice"* [RULED — L2-S28]. A view may not decide anything (L3-S1),
  so the bass note can only be the member L2 named. Taking the lowest sounding pitch instead would read
  the notes and could contradict L2's figure, a second chance to disagree with one fact [RULED —
  charter, L3]. In arpeggiated and Alberti textures the lowest pitch of a short slice is not the
  harmony's bass [FACT — ledger C32, C38]. Whether the lowest note equals the named root is a different
  question from whether the root is right [FACT — ledger C28]. Inversion is where a published
  large-vocabulary system is weakest: 71.5 / 54.4 / 38.3 / 40.5 for root, first, second and third
  inversion [FACT (relayed, 08) — McLeod & Rohrmeier 2021, §results]. So the bass note's uncertainty is
  carried through L2's figure rivals (L3-S6), and the chord symbol does not hide it. **Declared (§6):**
  IC-L1 §0, S-44 and its ruling note carry the sentence *"the chord's bass note, which L3 publishes, read
  off the figure L2 decides"*. This session met it before writing this statement. The statement is
  derived from the charter's *view* and from L2-S28's definition of the figure alone. It coincides with
  the sentence and is flagged so the comparison can check it for contamination.
- *Source class.* Derived (from the charter and L2-S28, which are given).
- *Status.* Settled.
- *Premise.* L2's figure names exactly one chord member. **False-negative path:** a span whose
  structural bass L2 holds as a near-tie between two members. L2 publishes that as figure rivals, and
  L3 shows it as two chord-symbol rivals rather than one symbol with a guessed bass.
- *Falsifier.* CODE. **Observable:** chord symbols over a span whose lowest sounding pitch differs from
  L2's structural bass (an Alberti span). **Decision rule:** falsified if the published bass note is
  the lowest sounding pitch rather than the member L2's figure names. **Not falsified by:** the two
  coinciding, which is the common case.

**L3-S5. Where L2's chord carries something the three parts cannot express, the chord symbol says so
and does not stretch.** (i) **Augmented sixths:** the root field carries a named reason ("no root in the
theory that names this chord"), while quality and bass are published. No dominant-seventh respelling is
put in its place. (ii) **Elaborations:** suspensions, retardations and sounding ninths, which L2 holds as
assignments and not in the chord (L2-S4, L2-S8), are not written into the chord symbol. They are read
in the figured bass (L3-S25). (iii) **A silent span:** the chord symbol carries L2's named reason
("silent") and no root (L2-S44). (iv) **Tonality and applied target:** the chord symbol is absolute and
expresses neither. Both stay on L2's chord, which the chord symbol stands beside (L3-S3).
- *Defense.* (i) The augmented sixths are traditionally explained as voice-leading chords built over
  a lowered sixth degree, and the traditional theory assigns them no root [THEORY — standard harmony
  textbooks; no source fetched]. A lead-sheet respelling (A♭7 for a German sixth in C) changes a
  spelled F♯ into G♭ and asserts a dominant seventh the reading did not decide [CONJECTURE]. That would
  decide something in a view, which L3-S1 forbids. Which display convention a user wants is left open
  (OQ-L3-9). (ii) L2's first specification carries no added-note classes. A sounding ninth over a
  chord is an elaboration assignment [RULED — L2-S4, beside, chord-vocabulary Ruling 2]. A chord
  symbol that grew a "sus" or "add" part would be read off the assignments and not off the chord. It
  would then be a second view of the assignments beside the figured bass, one fact in two homes
  [CONJECTURE, on the pack's principle #6]. (iii) L2-S44 [RULED — IC-L2]. (iv) This is the charter's
  definition: root, quality and bass note [RULED — charter, L3].
- *Source class.* Derived.
- *Status.* Settled for (ii), (iii) and (iv). Settled for (i) as published content; **open** on the
  display convention (OQ-L3-9).
- *Premise.* A named reason is a usable publication for a consumer. **False-negative path:** a display
  that needs a root for every chord. It reads the quality and the bass and chooses its own convention,
  as a display act, and never publishes it back into the analysis.
- *Falsifier.* CODE. **Observable:** chord symbols of augmented-sixth spans, of spans with
  suspension assignments, and of silent spans. **Decision rule:** falsified if an augmented sixth
  receives a root; if any elaboration's pitch changes a chord symbol with L2's chord fields held fixed;
  or if a silent span carries a root. **Not falsified by:** a display layer showing its own respelling.

**L3-S6. Chord-symbol rivals are read off L2's rivals, one for each published L2 span-rival, rival
object and whole reading. L2 rivals that give the same chord symbol over the same stretch (same start,
same end) are merged into one chord-symbol rival, whose mass is the sum of theirs and which references
each of them. The principal chord symbol of a stretch is always the one read off L2's principal
reading, even where a merged rival carries more mass.**
- *Defense.* The chord symbol forgets the tonality and the applied target (L3-S5 (iv)). Readings that
  differ only there therefore share one symbol. Relative major and minor name the same collection, so
  the chord read under one is the chord read under the other [FACT — ledger C11]. Exemplar 2 bar 41
  writes `N6 F: IV6`, and exemplar 1 writes `IV.IV6` at the same bar [FACT at the files]. A Neapolitan
  sixth in A minor and IV6 in F major are both B♭ major over D, so the two analysts' disagreement
  vanishes in the chord symbol. Exemplar 2 bar 31 writes `i d: iv`, one G minor triad read as i of G
  minor and iv of D minor. Exemplar 1 writes `i` there, under the G minor it entered at bar 29
  (`v.i{`), and moves to D minor only at bar 32 (`ii.V`) [FACT at the files]. Both give a G minor triad
  at the bar's start. Summing masses over readings that give the same fact is the law of total probability applied
  to a many-to-one function of the reading [THEORY — elementary probability]. Keeping the principal
  symbol tied to L2's principal reading follows from the bar on revision: *"A read-off fact may not
  revise the decision it was read off"* [RULED — charter, contract table, L3 → L2]. Promoting a symbol
  because its summed mass is larger would publish a chord L2 did not commit, which is a second
  decision. Where the cadential six-four is read two ways (`I6/4` against `V(64)`, exemplar 1 bar 24
  and exemplar 2 bar 24 [FACT at the files]; L2-S29 [RULED]), the two readings give different symbols:
  C major over G, against G major over G. They are published as two rivals with their masses, and DP-N
  is not decided here.
- *Source class.* Derived (inside the charter's bar, which is given).
- *Status.* Settled.
- *Premise.* L2 publishes enough of its rival distribution for the sums to mean something. **False-
  negative path:** L2 below its top effort setting withholds rivals under a cut-off, and publishes the
  cut-off and the withheld mass per span [RULED — L2-S42]. The summed masses are then lower bounds, and
  L3 publishes the withheld mass beside them (L3-S34).
- *Falsifier.* CODE. **Observable:** chord-symbol rivals over a pivot span and over a span with
  tonicisation-against-modulation rivals. **Decision rule:** falsified if two rivals with identical
  stretch and identical symbol are published separately; if a merged rival's mass differs from the sum
  of the L2 masses it references; or if the principal chord symbol differs from the one read off L2's
  principal reading. **Not falsified by:** a merged rival's mass exceeding the principal symbol's mass.

**L3-S7. L3 does not publish a pivot label (*this chord is degree a in one tonality and degree b in the
next*). Under IC-L2 a pivot is published as one span with one tonality and the other tonality's reading
as a rival (L2-S19). The label is a re-expression of L2's decided chord in the neighbouring span's
tonality. It is not on L3's charter list, and adding it is a ruling (OQ-L3-8).**
- *Defense.* IC-L2 carries the question to this specification in terms: *"Whether and where that label
  is published — at L3, or as a display view — is not decided by this ruling and is carried to L3's own
  specification. L3's charter list is not amended"* [RULED — L2-S19, beside, pivot-chord Ruling 1]. The
  label would be a view, since nothing is decided in re-expressing a decided chord, and it would serve
  the pivot's theoretical claim [THEORY — the pivot-chord modulation of standard textbooks; no source
  fetched]. The charter fixes what L3 publishes [RULED — charter, L3 "Publishes"]. A derivation that
  adds an output decides L3's *what*, which the brief reserves. Exemplars 1 and 2 show the case: one
  analyst writes the pivot (`N6 F: IV6`) and the other writes the change at the same chord with no
  pivot (`IV.IV6`) [FACT at the files]. So the label is an analyst's choice of description, and L2's
  rivals already carry its musical content.
- *Source class.* Given — charter (the list) and IC-L2 (the carried question). Derived (the reading of
  the label as a view).
- *Status.* **Open** (OQ-L3-8 ★).
- *Premise.* L2's rivals carry the pivot's content. **False-negative path:** a consumer that needs
  *both at once* as one fact. L2-S19 records that the masses of the two rivals express "either", not
  "both". That consumer is unserved until the ruling.
- *Falsifier.* CODE until ruled. **Observable:** L3's output schema. **Decision rule:** falsified if L3
  publishes a field carrying two tonalities for one span. **Not falsified by:** the two rival chord
  symbols, which are identical for a true common-chord pivot (L3-S6).

### 3b. Face (b) — where a phrase ends

**L3-S8. The phrase reading is an L3 decision. For the working span, L3 decides a partition into
grouping units (L3-S12) whose boundaries are positions in the record, and publishes the principal
partition with its rivals and their mass. Every change point and both span edges are candidate phrase
ends. No item of evidence forces or forbids a phrase end, and an absent flag is never read as an
absent phrase end.**
- *Defense.* The charter: *"Which of those are phrase ends, and how they group into sections, is
  decided here, because the decisive further evidence is cadential"* [RULED — charter, L3]. Every
  published fact carries its own mass, and there is no separate uncertainty layer [RULED — charter,
  "NOT A LAYER"]. So the decision is published with rivals, as L2's is. IC-L1 states that the notated
  boundary evidence *"may be empty or near-empty over a passage and is systematically incomplete as a
  phrase signal, so an absent flag is never read as an absent boundary"* [RULED — IC-L1 beside S-39,
  Ruling 48]. A candidate set restricted to flagged positions would read absence as absence. All
  change points are therefore candidates, which also matches the charter's L1 construction, where the
  candidate set is exhaustive so that *"a real harmony change can never be missed"* [RULED — charter,
  L1]. The exemplars show phrase ends at positions with almost no notated cue: exemplar 3's `}{` at
  bar 12 beat 3 and exemplar 1's `}{` at bar 42 (L3-S11) [FACT at the files]. The ground truth also
  writes a phrase boundary where the harmony does not change [RULED — charter, DP-J]. Exemplar 1 bar 58
  shows it: a bare `{` with no chord, inside a span of V [FACT at the file]. So phrase-end candidates
  cannot be restricted to L2's harmonic boundaries either.
- *Source class.* Given — charter (it is decided here, with mass) and IC-L1 (absent is not absent).
  Derived (the candidate set).
- *Status.* Settled, with one charter question open: how the charter's *"the span's boundaries come
  from the notated cues"* reads at an elision with no cue (OQ-L3-3 ★).
- *Premise.* The evidence of L3-S9 separates phrase ends from other positions well enough for a fitted
  model to rank them. **False-negative path:** a phrase end with no notated cue and no cadential
  evidence (an open, non-cadential phrase ending). It gets low mass and appears only as a rival.
- *Falsifier.* CODE. **Observable:** the phrase readings over a passage with and without its flags.
  **Decision rule:** falsified if removing every flag makes some phrase reading inadmissible; if adding
  a flag makes some phrase reading inadmissible; or if a change point is never a candidate. **Not
  falsified by:** masses changing when flags change.

**L3-S9. The evidence bearing on a phrase end at a candidate position p falls into four families.**
(i) **L1's notated evidence at and near p:** the boundary flags with their scope (FERMATA,
REST-BEGINS by voice, ALL-SILENT, REPEAT, BAR-LINE with its type, TIME-SIGNATURE-CHANGE,
KEY-SIGNATURE-CHANGE, BREATH-MARK, CAESURA, TEMPO-CHANGE); the positioned marks list, including section
labels and rehearsal letters; the per-voice relations (the silence before an onset, the time since
that voice's preceding attack, the spelled melodic interval) with the chordal count; and the metric
strength class. (ii) **Cadential-progression evidence read off each L2 reading:** whether the decided
spans ending at or just before p form a cadential progression in their tonality, as L3-S16 describes
it. It is computed with no phrase end as input. (iii) **A phrase-length term** on the distance in bars
from the preceding phrase end. (iv) **Slurs and dynamics from L0**, which enter only if a held-out
measurement repays them. Each family enters as fitted terms, and none is a rule.
- *Defense.* (i) is L1's published list [RULED — IC-L1 S-39, S-41, S-50, beside S-39 Rulings 48, 49,
  50, 61]. The charter routes *"Notated phrase evidence"* from L1 to L3 [RULED — charter, contract
  table]. The fermata delineates the phrase and not necessarily the exact arrival [FACT (relayed, 08)
  — de Clercq, p. 192]. A local detector's rhythmic and break features, among them a strong beat at
  the arrival and rests after it, are reported by its authors to bring an improvement *"especially for
  HC"* [FACT (relayed, 08) — Bigo et al. 2018, §4.4, Table 4, `R-Z-strong-beat`, `R-after-Z-rest-*`]. The per-voice relations are the surface cues that grouping theory names: rest,
  attack-point distance and change of register [THEORY — Lerdahl & Jackendoff's grouping preference
  rules; no source fetched]. A perceptual account places boundary strength in the rise of information
  content from a terminal event to the next event [FACT (relayed, 08) — Sears et al. 2018, §6.3]. (ii)
  is the charter's *"decisive further evidence is cadential"* [RULED — charter]. It avoids the
  circularity the charter names, *"defining a phrase span by its cadence and then aligning cadences to
  that span is circular"* [RULED — charter, L3], because the evidence at p reads only L2's spans and
  never a phrase end. The cadence fact itself is read only at a decided phrase end (L3-S15). Grouping
  is downstream of tonality and harmony in the most developed computational grouping implementation,
  whose most influential grouping rule needs region and chord distances supplied from outside [FACT
  (relayed, 08) — Hamanaka, Hirata & Tojo 2013, pp. 214–217, 220]. That is the charter's ordering of L2
  before L3. (iii) Regular phrase lengths are a strong stylistic tendency in the classical repertoire
  [THEORY — standard form theory; no source fetched]. An expert has placed a modulation to respect a
  2 + 2 bar phrase structure [RULED — L2-S49, premise, which relays Chew; Chew is not in this session's pack]. A regularity must be a
  term and not a rule, by the same argument L2-S7 makes for harmonic rhythm [RULED — L2-S7, charter's
  "a hard constraint lets one wrong answer delete the other question's right one"]. (iv) IC-L1 admits
  neither a dynamic nor a slur as boundary evidence at L1, and leaves *"if measured to help"* to the
  consumer's measurement [RULED — IC-L1 beside S-39, Ruling 50]. L0 supplies both [RULED — IC-L1 S-7].
- *Source class.* Given — IC-L1 (what (i) contains) and charter ((ii) as cadential). Derived (the
  four families, non-circularity, (iii)). *Measured* (every weight; whether (iv) enters), UNESTABLISHED.
- *Status.* Settled in shape. **Open** on values (OQ-L3-11).
- *Premise.* The four families carry most of what separates phrase ends. **False-negative path:**
  thematic parallelism, a grouping cue of its own [THEORY — Lerdahl & Jackendoff's parallelism rule; no
  source fetched], whose published computational form lacks a clear definition of similarity [FACT
  (relayed, 08) — Hamanaka et al. 2013, p. 210]. No layer beneath publishes it (OQ-L3-5).
- *Falsifier.* CODE. **Observable:** the inputs of the phrase model's terms. **Decision rule:**
  falsified if any term reads a quantity not published by L0, L1 or L2; if the cadential-progression
  term at p reads a phrase end; or if a slur or dynamic enters a fitted term before a held-out
  measurement admits it. **Not falsified by:** a fitted weight near zero on any family.

**L3-S10. A phrase end and its cadential arrival are published as two positions. The phrase end is the
last moment of the phrase as L3 decides it. The cadential arrival is the start of the L2 harmonic span
that sounds at the phrase's last moment, when that span completes a cadential progression. The cadence
is aligned to the phrase, never the phrase to the cadence. The arrival lies at or before the phrase end,
and the two may be bars apart when the final harmony is prolonged.**
- *Defense.* The charter: *"the span's boundaries come from the notated cues, and the cadence is
  aligned to them"* [RULED — charter, L3]. A published chorale study took *"the cadential arrival (if
  any) as the last change of harmony at or before the fermata"*, with the arrival shifting to the strong
  beat before a weak-beat fermata when the melody allows [FACT (relayed, 08) — de Clercq, pp. 192–193].
  Reading "the last change of harmony" as the start of the L2 span sounding at the phrase's end gives
  that rule exactly. L2 merges adjacent spans with identical chords and leaves elaborations as
  assignments (L2-S14) [RULED — IC-L2], so a dominant prolonged under a decorating six-four is one
  span and its arrival is where it began. Exemplar 1 bar 11 carries `V|HC`, followed by `V(64)`, `V`,
  `V(64)`, and bar 12 carries `V}` [FACT at the file]. The cadence label stands at the arrival (bar 11,
  beat 1) and the phrase-end sign a bar later. Exemplar 3 bar 4 carries `V|HC}` on a half note under a
  fermata, followed by a rest [FACT at the file]: there the two positions coincide.
- *Source class.* Given — charter (the direction of alignment). Derived (the two positions; the
  reading of the arrival).
- *Status.* Settled.
- *Premise.* The phrase's final harmony is the cadential goal. **False-negative path:** a phrase whose
  last span is a post-cadential tonic–dominant oscillation (exemplar 1 bars 26 to 28: `I|PAC}`, then
  `V7`, `I`, `V`, `I`) [FACT at the file]. If L3 placed the phrase end after the oscillation, the
  arrival rule would find the last tonic of the oscillation and not the cadential one. The exemplar's
  analyst ends the phrase at bar 26 and leaves bars 26 to 28 outside any phrase sign. L3-S12 gives that
  stretch a unit of its own, so the arrival stays at the cadence.
- *Falsifier.* CODE. **Observable:** published phrase ends and arrivals over a prolonged half
  cadence. **Decision rule:** falsified if the arrival is placed after the phrase end; if a phrase end
  is moved to coincide with an arrival without the phrase model's decision; or if the arrival is
  placed at a decorating chord inside a merged span. **Not falsified by:** the arrival and phrase end
  coinciding.

**L3-S11. An elided phrase boundary is published as one position that is both the arrival of the
closing phrase's cadence and the beginning of the next phrase. In the partition, the arrival span
belongs to the phrase it opens, and the closing phrase carries its cadence with an *elided* mark at
that position.**
- *Defense.* Exemplar 1 bar 42 carries `I|PAC}{`, the cadence of the development closing on the first
  chord of the recapitulation in F [FACT at the file]. The right hand runs in sixteenths through bar 41
  into the half-note F that opens bar 42, with no rest (lines 4040 to 4092 of the file) [FACT at the
  file]. Exemplar 3 bar 12 carries `i/iv|PAC}{` at beat 3, inside the bar, where staves 1 to 3 attack
  together with no rest and no fermata [FACT at the file, staves 1 to 3 of bar 12 read]. The overlap of
  a group's end with the next group's beginning is a recognised grouping phenomenon [THEORY — Lerdahl &
  Jackendoff's grouping overlap and elision; no source fetched]. Tiling (L3-S12) needs one owner for the
  arrival span. Giving it to the opening phrase keeps the next phrase's beginning true to the music,
  and the mark keeps the closing phrase's cadence (#12).
- *Source class.* Derived.
- *Status.* Settled in form.
- *Premise.* An elision falls at one position. **False-negative path:** an overlap of several beats,
  where the closing phrase's cadential motion and the opening phrase's first gesture overlap over more
  than one slice. The single-position form records only the arrival. No staged case shows a longer
  overlap (OQ-L3-13).
- *Falsifier.* CODE. **Observable:** grouping units at an elided cadence. **Decision rule:** falsified
  if the arrival span is owned by both units or by neither, or if the closing phrase loses its cadence.
  **Not falsified by:** a rival reading the position as an ordinary phrase end with no elision.

**L3-S12. The phrase reading tiles the working span. Its units are phrases and the stretches that lie
between phrases (a post-cadential codetta, an introduction before the first phrase). Each unit carries
which of the two it is.**
- *Defense.* The charter states, of the harmonic spine, that *"every span kind on the harmonic spine
  cuts across the whole texture at once and its members tile the music"*. It contrasts the melodic
  phrase, which belongs to the voice-leading axis and does not tile [RULED — charter, the second
  axis]. Exemplar 1 leaves bars 26 (after its `I|PAC}`) to 28 outside any phrase sign until `v.i{` at
  bar 29 [FACT at the file]. A tiling that allowed no between-phrase stretch would force that codetta
  into a phrase and move the arrival (L3-S10's false-negative path). A typed tiling serves both.
- *Source class.* Given — charter (tiling). Derived (the second kind of unit).
- *Status.* Settled. How an annotation with gaps and elisions is graded against the tiling is
  measurement design (OQ-L3-12).
- *Premise.* Two kinds of unit suffice. **False-negative path:** a stretch an analyst reads as neither
  phrase nor codetta, such as a transition that dissolves. It is published as a phrase or a
  between-phrase stretch, with the rival carrying the other reading.
- *Falsifier.* CODE. **Observable:** the units over a working span. **Decision rule:** falsified if the
  units leave a gap or overlap (an elision being one position owned once, L3-S11), or if a unit lacks
  its kind. **Not falsified by:** a working span read as one phrase.

**L3-S13. A rival phrase reading, a different placement of a phrase end or a different count of
phrases, is carried with its mass, in the same form as L2's boundary rivals. The masses are composed
from L2's rivals and L3's own model as L3-S35 states.**
- *Defense.* The charter publishes rivals that differ in where boundaries fall, for L2 [RULED —
  charter, L2; DP-K], and applies its rival form to every published fact [RULED — charter, "NOT A
  LAYER"]. The exemplars disagree on a grouping boundary. Exemplar 1 begins a phrase at bar 13
  (`V.V{`), while exemplar 2 places its *second theme* section at bar 14 and keeps bar 13 under the
  exposition's first label [FACT at the files]. Whether those are the same kind of boundary is L3-S23's
  question, and that two analysts place the start differently is the case.
- *Source class.* Given — charter. Derived (the composition reference).
- *Status.* Settled.
- *Premise.* None beyond the charter's.
- *Falsifier.* CODE. **Observable:** the phrase rival list. **Decision rule:** falsified if two phrase
  readings differing only in one phrase end's position cannot both appear. **Not falsified by:** a
  rival below a declared cut-off being withheld with its mass published.

**L3-S14. Every weight of the phrase model is fitted from annotated phrase boundaries, held out by
piece, with its capacity declared before the fit, on licence-clear music only. No value is given here.**
- *Defense.* No value is graded on data that helped fit it [RULED — pack principle #20, as carried by
  L2-S38]. A value that ships is fitted only on public-domain, CC0 and CC-BY music [RULED — D-292 as
  relayed in L2-S38]. Exemplar 3 states *"CC BY-NC-SA 4.0; CCARH; DCML"*, and exemplar 1's copyright
  field is empty [FACT at the files], so neither could enter such a fit. A published grouping system
  reaches F 0.46 at defaults and 0.77 with per-piece hand tuning by its authors, and its automatic
  optimiser recovers almost none of the gain (0.48) [FACT (relayed, 08) — Hamanaka et al. 2013, Table
  8.4, p. 230]. Hand tuning on graded music is the antipattern principle #20 forbids. One published
  cadence detector warns that its own earlier hand-coded rules *"may have resulted in overfitting"*
  [FACT (relayed, 08) — Bigo et al. 2018, §4.4]. Ground truth is itself an instrument [RULED — pack
  principle #21]. The only published two-annotator agreement relayed here covers fermata events in the
  Bach chorales on a composite token, with the author as one of the two annotators [FACT (relayed, 08)
  — de Clercq, pp. 195–196]. It is no ceiling for phrase ends in this repertoire.
- *Source class.* *Measured*: the fit needs annotated phrase beginnings and endings (the exemplars'
  `{` and `}` show that a tradition writes them), L1's evidence at every change point, L2's readings,
  a piece-level held-out split, a capacity budget, and the graded measure, which is the
  measurement-design stage's. **UNESTABLISHED.**
- *Status.* **Open** (OQ-L3-11).
- *Premise.* Licence-clear annotated phrase data exists in sufficient amount. **False-negative path:**
  it does not. The model is then provisional (L3-S33), and no item resting on it carries load.
- *Falsifier.* CODE. **Observable:** the fit record. **Decision rule:** falsified if any weight is set
  by hand in a shipped model, if evaluation and fit data overlap, or if the fit pool holds music under
  a non-commercial or unstated licence. **Not falsified by:** a hand-declared provisional value in a
  desk simulation, marked as such.

### 3c. Face (c) — the cadence at each phrase end, and its type

**L3-S15. A cadence is published only at a phrase end L3 has decided, an elided one included, and at
most one per phrase end. Cadential-progression evidence computed at other positions (L3-S9 (ii)) is
published as an evidence-class fact named for the pattern (never *cadence*), with its establishment
status.**
- *Defense.* The charter publishes *"the cadence at each phrase end, with its type"* [RULED — charter,
  L3]. A cadence type is *"a claim about what the decided chords do at a decided phrase end"* [RULED —
  charter, L3]. Cadential patterns occur where analysts do not write cadences. A published detector's
  false positives include PAC-like endings of each statement of a modulating sequence: *"whether to
  classify them as cadences is a matter of higher-level musicological considerations"* [FACT (relayed,
  08) — Karystinaios & Widmer 2022, §6.2]. Tying the cadence to the phrase decision is where that
  consideration lives. Publishing the pattern evidence broadly follows the pack's rule that
  evidence-class facts are published even without a named consumer, each with its establishment status
  [RULED — D-100 as carried by IC-L1 S-52 and L2-S45]. Naming it for the pattern follows IC-L1's naming
  bar, under which a field named *cadence* would be consumed as a decision [RULED — IC-L1 S-50, by
  analogy].
- *Source class.* Given — charter. Derived (the evidence publication and its name).
- *Status.* Settled.
- *Premise.* Every cadence an analyst writes closes a phrase. **False-negative path:** an analyst who
  labels a cadence inside a phrase (an internal half cadence that does not end a group). L3 publishes
  it only if a rival phrase reading ends there. Otherwise only the pattern evidence carries it.
- *Falsifier.* CODE. **Observable:** cadences and phrase ends. **Decision rule:** falsified if a
  cadence is published at a position that is not a phrase end of the reading it belongs to, or if two
  cadences are published at one phrase end of one reading. **Not falsified by:** pattern evidence at a
  non-phrase-end.

**L3-S16. The cadence is published as its defining features, each a view of a lower layer's fact:**
(1) the arrival position (L3-S10) and its metric strength class (IC-L1 S-35); (2) the chords of the
progression's last spans, normally the final, the penultimate and, where present, the pre-dominant
span, each with L2's four fields, in the arrival span's tonality, with the chord symbols of L3-S1;
(3) the relation of the arrival's tonality to the tonality before the phrase (the same, or a change, by
degree); (4) the suspensions and appoggiaturas sounding at the arrival or on the penultimate chord, as
L2 assigns them (a 4–3 over the dominant, for example); (5) whether the phrase end is elided (L3-S11);
(6) **the scale degree of the highest sounding pitch at the arrival, which carries a named reason
("not computable: no layer beneath publishes it") until OQ-L3-4 is ruled.**
- *Defense.* These are what the textbook categories are defined by: the degrees and inversions of the
  last chords, the soprano's degree at the arrival, and the tonal context [THEORY — standard harmony and
  form theory; no source fetched]. Published detectors and models read the same things. Their features
  describe the arrival Z, the chord before it Y and the preparation X [FACT (relayed, 08) — Bigo et
  al. 2018, §2]. A model of cadence choice encodes key area, cadence type and the chord member of the
  soprano at the arrival as one token [FACT (relayed, 08) — de Clercq, p. 194]. The global key there
  matters less than the local key implications [FACT (relayed, 08) — de Clercq, p. 195]. Feature (4)
  comes from L2's assignments: exemplar 3 writes `V(4)` then `V` at its cadences [FACT at the file],
  and the cadential suspension is part of what an analyst writes. Feature (6) needs the highest
  sounding pitch. L1 publishes the lowest sounding pitch per slice (IC-L1 S-50) and no highest one,
  and S-50 is exhaustive: *"an absence in an L1 publication means not there"* [RULED — IC-L1 beside
  S-50, Ruling 60]. Computing it from the sounding set here would supply a notated fact that, by
  IC-L1's own test, is an L1-kind fact (computable from L0 with no tonality, chord or boundary as
  input) [RULED — IC-L1 S-51]. The brief forbids filling it [RULED — brief §3.1]. The want is OQ-L3-4.
- *Source class.* Derived. Each feature's content is given by the layer that publishes it.
- *Status.* Settled for (1) to (5). **Open** for (6) (OQ-L3-4).
- *Premise.* These features determine every type of L3-S17. **False-negative path:** the evaded
  cadence, defined by what the following music does instead of arriving [THEORY — Caplin's typology;
  no source fetched]. Its features include the next phrase's opening, which (2) to (5) partly hold and
  thematic parallelism would complete (OQ-L3-5).
- *Falsifier.* CODE. **Observable:** published cadences. **Decision rule:** falsified if any feature
  differs from the lower layer's fact it is read off, or if feature (6) carries a value while no layer
  beneath publishes the highest sounding pitch. **Not falsified by:** a feature carrying a named reason.

**L3-S17. The cadence type is a view of the defining features under a declared vocabulary. Which
vocabulary is principal is not decided here (OQ-L3-2 ★). Every type of the declared vocabularies is a
deterministic function of L3-S16's features, and a type that cannot be computed carries a named reason.
The cases where the traditions disagree are named, not settled.**
- *Defense.* The traditions differ on what is a cadence at all. A published chorale study uses perfect
  authentic, imperfect authentic, half, Phrygian, plagal, deceptive, a reinstated *subdominant stop*,
  and *no cadence*. It states that readers with Schenkerian leanings may deny that the subdominant
  stop, the plagal and the deceptive are cadences [FACT (relayed, 08) — de Clercq, pp. 194, 200]. A
  perceptual study uses Caplin's categories, perfect authentic, imperfect authentic, half, deceptive
  and evaded [FACT (relayed, 08) — Sears et al. 2018, §5.1]. A rule-based system uses perfect authentic,
  imperfect, interrupted, plagal, dominant half and subdominant half [FACT (relayed, 08) — Illescas et
  al., Table 4]. The disagreement the exemplars show is the inverted dominant. Exemplar 1 bar 4 carries
  `V6 V65 I}`, a phrase end with no cadence label [FACT at the file]. Under the American textbook
  convention an inverted V–I close is an imperfect authentic cadence, while Caplin's theory requires a
  root-position dominant for an authentic cadence [THEORY — Kostka & Payne; Caplin 1998; neither
  fetched]. This is DP-N's shape. *"The three readings are different theoretical claims about the same
  notes … A framework that picked one silently would be deciding a question of theory on no evidence"*
  [RULED — charter, DP-N, by analogy]. Publishing the features and the type as a view keeps every
  tradition's type recoverable from one fact, as the chord symbol keeps the chord.
- *Source class.* Derived.
- *Status.* Settled in form. **Open** on the principal vocabulary (OQ-L3-2 ★). Feature (6) blocks the
  PAC/IAC split in every vocabulary until OQ-L3-4 is ruled.
- *Premise.* Each vocabulary's types are functions of chords, degrees, the soprano and the context.
  **False-negative path:** a type whose definition needs something none of the features holds, such as
  the evaded cadence's expectation (L3-S16's premise), or a half cadence that Caplin distinguishes from
  a mere dominant arrival by the presence of a cadential progression before it [THEORY — Caplin 1998; no
  source fetched]. Feature (2)'s pre-dominant span holds the latter. The former stays a named reason.
- *Falsifier.* CODE. **Observable:** the type against the features. **Decision rule:** falsified if
  two cadences with identical features receive different types under one vocabulary, or if a type
  depends on anything but the features. **Not falsified by:** two vocabularies giving different types
  for one cadence.

**L3-S18. At a phrase end where no type of the declared vocabulary applies, the cadence field is
published as *no cadence* with its reason. That is distinct from *type not computable*, which states
which feature is missing.**
- *Defense.* Exemplar 1 bar 4 (`V6 V65 I}`) and bar 45 (`I}`, its recapitulation counterpart) end
  phrases with no cadence label [FACT at the file]. One published study encodes problematic events as
  *"NC" (no cadence)* [FACT (relayed, 08) — de Clercq, p. 194]. The charter leaves open whether the
  analysis may decline to read a span, and notes that some schemas carry a no-cadence verdict [RULED —
  charter, DP-Q]. A phrase end without a cadence is a positive reading of the music. A type that cannot
  be computed is a gap in the evidence. Merging the two would hide a fact (#12).
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* The vocabulary's types and *no cadence* exhaust the phrase ends. **False-negative path:**
  a tradition that writes a cadence everywhere a phrase ends. Under it *no cadence* never applies,
  which is that vocabulary's own view.
- *Falsifier.* CODE. **Observable:** cadence fields at phrase ends. **Decision rule:** falsified if a
  phrase end carries an empty cadence field, or if *no cadence* is published where a feature the type
  needs is missing. **Not falsified by:** *no cadence* under one vocabulary and a type under another.

**L3-S19. The principal cadence is read off L2's principal reading at L3's principal phrase end.
Rival cadences are read off L2's rivals at that phrase end, and off L3's rival phrase ends. Because a
cadence reads several spans together, its mass is computed from L2's rival objects and ranked whole
readings, never by multiplying per-span marginals. The mass L2 does not publish is carried as
unaccounted.**
- *Defense.* The bar on revision fixes the principal [RULED — charter, contract table, L3 → L2].
  Multiplying per-span marginals gives mass to *"mixtures no analyst writes, the 'incoherent composite'"*
  [RULED — L2-S41, citing charter DP-A]. A type reads at least two spans (L3-S16 (2)), so its mass is a
  sum over whole readings or over the rival objects that cover the progression [THEORY — elementary
  probability; L3-S34]. L2 publishes rival objects with their extent and whole-reading mass, ranked
  whole readings to a bound, and the withheld mass per span [RULED — L2-S41, L2-S42, L2-S45]. The
  exemplars show why the rivals matter to a cadence. At exemplar 1 bar 31, one analyst reads a G minor
  pivot into D minor and the other stays in G minor until bar 32 [FACT at the files]. Where such rivals
  meet a phrase end, the cadence's tonality relation (L3-S16 (3)) differs between them. A published
  annotator pair disagreed mainly on *tonicization versus modulation* at cadences [FACT (relayed, 08) —
  de Clercq, p. 195], and the same music carries two defensible key ground truths [FACT (relayed, 08)
  — Nápoles López et al. 2020, §2].
- *Source class.* Given — charter (the principal). Derived (the computation and the unaccounted mass).
- *Status.* Settled.
- *Premise.* The ranked whole readings and rival objects cover the readings that matter. **False-
  negative path:** many independent local ambiguities, whose combinations exceed the bounded list
  (L2-S41's premise). The unaccounted mass then grows, and it is published, not hidden.
- *Falsifier.* CODE. **Observable:** cadence rivals and masses over a passage with a multi-span L2
  rival. **Decision rule:** falsified if a cadence's mass equals the product of its spans' marginals
  where a covering rival object exists; if the principal cadence differs from the one read off L2's
  principal reading at L3's principal phrase end; or if unaccounted mass is not published. **Not
  falsified by:** a rival cadence carrying more mass than the principal.

**L3-S20. The cadential six-four is handled under both readings L2 admits (`I6/4` and `V(64)`), each
read as it stands. The type can be the same under both, while the arrival position and the
pre-dominant feature differ. Those differences are published as rivals, and DP-N is not decided.**
- *Defense.* L2 admits both and publishes the one the evidence favours with the other as its rival
  [RULED — L2-S29, cadential-six-four Ruling 1]. IC-L2 carries to this specification: *"L3's cadence
  reading must handle a committed `I6/4`"* [RULED — L2-S29, beside]. Exemplar 1 bar 11 reads `V|HC` then
  `V(64)` at beat 2, and exemplar 2 reads bar 11 as `V b2 I6/4 b3 V b4 I6/4`, then bar 12 `V` [FACT at
  the files]. Under the `V(64)` reading, L2's merging rule (L2-S14) makes bars 11 and 12 one span of V,
  so the arrival is bar 11 beat 1. Under the `I6/4` reading, the last change of harmony before the
  phrase end is the V at bar 12, so the arrival is bar 12. The type, a half cadence, is the same under
  both [CONJECTURE — this session's application of L3-S10 to the two readings]. At the authentic
  cadence of bars 22 to 26, exemplar 1 has `ii6 … V(64) V7 I|PAC}` and exemplar 2 has `ii6 … I6/4 V7 I`
  [FACT at the files]. The last two spans are V7–I under both, and the chord before them differs (V
  with a six-four against I6/4). Reading the six-four as a tonic in second inversion is one theory
  of the cadential six-four among three [RULED — charter, DP-N].
- *Source class.* Given — IC-L2 (both readings). Derived (their consequences for the cadence).
- *Status.* Settled. The principal reading's theory stays open with DP-N.
- *Premise.* L3-S10's arrival rule is right under both readings. **False-negative path:** under the
  `I6/4` reading an analyst places the half-cadential arrival at the first dominant of bar 11, as a
  dominant arrival decorated by a tonic six-four. L3's rival at bar 11 then carries that analyst's
  position, with the other reading's mass.
- *Falsifier.* CODE. **Observable:** cadences over a passage with both six-four readings among L2's
  rivals. **Decision rule:** falsified if either reading yields no cadence reading at all, or if L3
  converts one reading into the other. **Not falsified by:** one reading carrying most of the mass.

**L3-S21. L3 reads L1's cadence cues only as their establishment status allows. The leading-tone cue
(IC-L1 S-46) is computed and may enter a fitted term. The falling-fifth cue (S-45) and the
fourth-and-seventh cue (S-47) are provisional and enter no fitted term until the cue window is
established.**
- *Defense.* *"A consumer may not put a provisional item under load until the parameter is
  established"* [RULED — IC-L1 S-52], and the window's stand-ins were accepted on the condition that no
  item resting on them carries load [RULED — IC-L1 beside S-48, Ruling 53]. L2 applies the same rule
  to itself [RULED — L2-S37]. For L3 the cues are, in any case, weaker than the decided chords. The
  cues reach the authentic cadence without harmony, F .80 and .69 on two corpora, and the half cadence
  only at F .29 and .41 [FACT (relayed, 08) — Bigo et al. 2018, Table 3; Karystinaios & Widmer 2022,
  Table 2]. L3 reads the chords L2 decided (L3-S16).
- *Source class.* Given — IC-L1.
- *Status.* Settled.
- *Premise.* None beyond IC-L1's.
- *Falsifier.* CODE. **Observable:** the phrase model's inputs. **Decision rule:** falsified if a fitted
  term reads a provisional cue. **Not falsified by:** an unfitted term in a measurement run that is
  establishing the window.

### 3d. Face (d) — the grouping of phrases into sections

**L3-S22. The section grouping is an L3 decision. It is a nested grouping over the units of the phrase
reading: each section is a run of consecutive units, sections at one level tile the level above, and
the top level covers the working span. A section boundary is always a boundary of the phrase reading.
The grouping is published with rivals and their mass, composed as L3-S35 states.**
- *Defense.* The charter: *"how they group into sections, is decided here"* [RULED — charter, L3].
  Exemplar 2's `Form:` labels nest. *Exposition* opens at bar 1 and *second theme* at bar 14 inside it,
  *development* at bar 29, *recapitulation* at bar 42, and *second theme* again at bar 59 inside it
  [FACT at the file]. Hierarchical grouping in which groups at one level are made of whole groups of
  the level below is the standard account of musical grouping [THEORY — Lerdahl & Jackendoff's grouping
  well-formedness; no source fetched]. A section boundary that fell inside a phrase would cut the unit
  the grouping is built from. That is a sign that the phrase reading or the section reading is wrong,
  so both are read as one consistent object [CONJECTURE]. A published thesis distinguishes
  phrase-structure segmentation from global segmentation into sections, as two tasks [FACT (relayed,
  08) — Lazzari 2023, §6.1.1].
- *Source class.* Given — charter (decided here). Derived (the nesting, the coincidence with phrase
  boundaries).
- *Status.* Settled in form.
- *Premise.* Sections are made of whole phrases. **False-negative path:** an elided section boundary,
  as at exemplar 1 bar 42, where the development's closing phrase and the recapitulation's opening
  phrase share the arrival [FACT at the file]. L3-S11's single-position elision serves the section
  boundary too, with the arrival span owned by the section it opens.
- *Falsifier.* CODE. **Observable:** the published sections and phrase units. **Decision rule:**
  falsified if a section boundary falls inside a phrase unit, if sections at one level overlap, or if
  the top level leaves part of the working span uncovered. **Not falsified by:** a one-section reading.

**L3-S23. The evidence bearing on a section boundary falls into four families, each entering as fitted
terms.** (i) **Notated section evidence** from L1: REPEAT flags and the junction adjacencies, final and
double bar lines, key- and time-signature changes, tempo changes, and section labels or rehearsal
letters in the marks list. (ii) **Cadential evidence** from L3's own cadences: the type of the cadence
closing the preceding phrase and its tonality relation (L3-S16 (3)). (iii) **Tonal evidence** from L2:
where the tonality changes and how far, across the candidate boundary. (iv) **Thematic return**, the
restatement of earlier material. No layer beneath publishes it, and it is written as OQ-L3-5 and not
filled.
- *Defense.* (i) is L1's published list [RULED — IC-L1 S-39, S-41, S-42, S-43, beside S-41 Ruling 51].
  Time- and key-signature changes are section-level notation in common practice [RULED — IC-L1 S-43].
  Exemplar 1's repeat signs (end-repeat at bar 28, start-repeat at bar 29) coincide with exemplar 2's
  *development* label [FACT at the files]. (ii) and (iii) belong to classical form, whose sections are
  defined by cadential closure and key areas [THEORY — standard form theory; no source fetched]. (iv)
  is shown by the exemplars. Exemplar 2's recapitulation at bar 42 carries the analyst's note
  *"recapitulation begins in the wrong key"* [FACT at the file], so the key-area family alone would not
  find it. What marks it is the return of the opening theme, together with the elided authentic
  cadence that exemplar 1 writes there (`I|PAC}{`) [FACT at the file]. Section detection is measured as
  hard. A published thesis locates the medial caesura of sonata expositions correctly for half its
  corpus [FACT (relayed, 08) — Feisthauer 2021, ch. 6], and a published global-segmentation model on
  popular music reaches pairwise F1 near 0.6 [FACT (relayed, 08) — Lazzari 2023, Table 6.2]. The
  domains differ and neither figure is a target here. Thematic parallelism is a computable relation
  over the notes that needs no tonality, chord or boundary as input. By IC-L1's test it is therefore an
  L1-kind item [RULED — IC-L1 S-51], and computing it at L3 from L0 would put an L1-kind fact in a
  second home. It is the want OQ-L3-5.
- *Source class.* Given — IC-L1 (what (i) contains). Derived (the four families). *Measured* (the
  weights), UNESTABLISHED.
- *Status.* Settled in shape. **Open** on the weights (OQ-L3-11) and on (iv) (OQ-L3-5).
- *Premise.* Families (i) to (iii) carry enough to rank section boundaries until (iv) is published.
  **False-negative path:** a recapitulation in the subdominant with no notated mark, exemplar 1's own
  case. Without (iv) it is found only through the cadence and the key change, and may carry low mass.
- *Falsifier.* CODE. **Observable:** the section model's inputs. **Decision rule:** falsified if any term
  reads a quantity no layer beneath or L3 itself publishes, in particular a melodic-repetition relation
  computed at L3. **Not falsified by:** weights near zero.

**L3-S24. L3 publishes the grouping (boundaries, nesting and rivals) and not form-function names such
as *exposition*, *second theme*, *development* or *recapitulation*. Naming the sections' formal
functions is not on L3's charter list (OQ-L3-6 ★).**
- *Defense.* The charter lists *"the phrase and section grouping"* [RULED — charter, L3 "Publishes"],
  and adding an output is a ruling on L3's *what*, which the brief reserves [RULED — brief §0, "never
  WHAT it does"]. Exemplar 2 writes such names [FACT at the file], so analysts do publish them, and
  the want is real. A form-function name is a theoretical claim on top of the grouping, and theories of
  form differ [THEORY — standard form theory; no source fetched]. Exemplar 1's phrase at bar 13 against
  exemplar 2's *second theme* at bar 14 (L3-S13) shows that a name can move a boundary in an
  analyst's reading.
- *Source class.* Given — charter.
- *Status.* **Open** (OQ-L3-6 ★).
- *Premise.* The grouping is useful without names. **False-negative path:** a consumer that needs the
  names. It is unserved until the ruling.
- *Falsifier.* CODE until ruled. **Observable:** L3's output schema. **Decision rule:** falsified if a
  section carries a form-function name. **Not falsified by:** a section carrying the text of a notated
  section label, which is an L1 mark referenced by identity.

### 3e. Face (e) — the figured bass

**L3-S25. The figured bass L3 publishes describes the harmony L2 decided, in thoroughbass notation. Per
harmonic span it gives the figure of L2's chord as the spelled intervals above the structural bass
(5/3, 6/3, 6/4, 7, 6/5, 4/3, 4/2, with any further members). Per event that L2 assigns as a suspension
or an appoggiatura, it gives the event's interval above the bass at the position where it sounds
against that bass, and the interval of its resolution where the resolution sounds (4–3, 7–6, 9–8, 6/4
to 5/3). Elaborations of the other relations are not figured. Where the lowest sounding pitch of a
slice (IC-L1 S-50) has as its witness an event L2 assigns as a pedal point, that event is the bass of
the figures for as long as it sounds. Nothing is decided in computing any of this.**
- *Defense.* A thoroughbass figure names the intervals above the bass, and a suspension is figured
  with its dissonance and its resolution [THEORY — thoroughbass practice, as Ju et al. cite Arnold;
  Arnold not fetched]. A published figured-bass study figures each note-onset slice by the intervals
  above the bass. It removes from the figure the number of an ornamental note in an upper voice, leaves
  a slice unfigured when the ornamental note is in the bass, and keeps suspension figures as the
  composer wrote them [FACT (relayed, 08) — Ju et al. 2020, §3.2.3, Fig. 4]. Exemplar 3's notated
  figures show the shapes this statement reproduces: `5 4` over a G at bar 1 beat 3 followed by `♮` over
  the G of beat 4, and `7` over an A♭ at bar 3 followed by `6` with no new bass note [FACT at the file;
  the reading of the format's prefix code 3 as a natural sign is this session's]. Each part of the
  statement reads a decided fact. The chord and its figure are L2's (IC-L2 §0, L2-S28). The
  assignments and their relations are L2's (L2-S8, L2-S9). The pitches are L0's spellings of the
  events L2's assignments reference. The lowest sounding pitch and its witness are L1's (IC-L1 S-50)
  [RULED — IC-L1, IC-L2]. A thoroughbass figure is written above the bass and names no root, so it is
  the same under both readings of the cadential six-four: 6/4 over the dominant's bass resolving to 5/3
  [THEORY — thoroughbass practice; no source fetched]. Under `I6/4` it is the chord's figure, and under
  `V(64)` it is two suspension-class elaborations resolving. The figured bass therefore agrees across
  the DP-N rivals where the chord symbol does not (L3-S6), and its rivals merge by L3-S6's rule.
- *Source class.* Derived (from facts given by IC-L1 and IC-L2).
- *Status.* Settled for the span figure and the suspension and appoggiatura figures. The pedal-point
  clause is settled in form, and no staged case exhibits it (OQ-L3-14).
- *Premise.* The span figure plus the suspension and appoggiatura figures is what a thoroughbass
  reader of the decided harmony needs. **False-negative path:** a passing sonority over a bass note
  that a continuo player would figure on its own. That grain needs the spelled interval content above
  the lowest sounding pitch per slice, which no layer beneath publishes (L3-S28, OQ-L3-7). In the bars
  of exemplar 3 whose figures were read (staff 4, bars 1 to 6), the passing D of bar 2 carries no
  figure, and the `6` that follows it stands on the E♭ its analyst reads as `i6` [FACT at the file;
  this session reads a `<FiguredBass>` element as attached to the chord that follows it, as bar 1's
  `5 4` before the G of beat 3 shows]. So no staged case of the continuo grain was met (OQ-L3-14).
- *Falsifier.* CODE. **Observable:** figures over a span with a 4–3 suspension and over a cadential
  six-four under both readings. **Decision rule:** falsified if a span's figure differs from the
  intervals of L2's chord members above the structural bass; if a suspension assigned by L2 is not
  figured with its resolution; if a passing note is figured; or if the two six-four readings give
  different figures over the same bass. **Not falsified by:** the figure being abbreviated in a
  rendering (L3-S27).

**L3-S26. Accidentals in the figures are written relative to the key signature in force (IC-L1 S-6),
read as a sign of the notation and not as a tonality. An accidental is written where a figured
interval's spelled pitch differs from what the signature gives.**
- *Defense.* In thoroughbass notation an accidental in a figure alters the interval from what the key
  signature gives [THEORY — thoroughbass practice; no source fetched]. A published figured-bass system
  needs the score's spelling to write its figures with the right accidentals [FACT (relayed, 08) — Ju
  et al. 2020, §3.3.1]. Exemplar 3 is in C minor under a two-flat signature, writes A♭ with an
  accidental, and figures the leading tone over G as `♮` [FACT at the file; prefix-code reading this
  session's]. Baroque scores are often notated one accidental short of modern practice [FACT — ledger
  C14]. A figure relative to the written signature reproduces the period's own notation, where one
  relative to a decided tonality would not. L3 consumes L0 [RULED — charter, L3 "Consumes"], and reading
  the signature's value is not reading it as the tonality. The input contract draws the same line for
  L2, which is *"not falsified by: L2 reading L0's facts directly for what L1 does not define, such as
  the key signature's value"* [RULED — L2-S47]. L1 alone is barred from the signature [RULED — IC-L1
  S-9].
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* The figures are meant to be read against the written signature. **False-negative path:** a
  consumer wanting figures against a modern signature for the decided tonality. That is a rendering
  choice, made from the spelled intervals, which stay the fact (L3-S27).
- *Falsifier.* CODE. **Observable:** figure accidentals under a changed key signature with every
  spelled pitch held fixed. **Decision rule:** falsified if the spelled intervals change, or if the
  accidentals do not change to match the new signature. **Not falsified by:** a figure carrying no
  accidental because the signature supplies the interval.

**L3-S27. The full figure (every spelled interval of L3-S25) is the published fact. An abbreviated
figure in the conventional short forms is a view of it under a declared convention, which a consumer
names when it asks for one.**
- *Defense.* Thoroughbass abbreviates by convention: 3 and 5 omitted in plain triads, 6 for 6/3, 2 for
  4/2 [THEORY — thoroughbass practice; no source fetched]. A published study grades figures with
  equivalence rules after Arnold: a 3 may be omitted unless a 4 sounds or the 3 resolves a 4–3, a 5
  unless a 6 sounds, a 6–5 resolves or the 5 carries an accidental, an 8 unless a 9 sounds or a 9–8
  resolves, and a 6 in 6/4/3 and 6/4/2 [FACT (relayed, 08) — Ju et al. 2020, §3.2.2]. The same study
  reports that Bach was inconsistent with himself in what he figured, for accidentals, suspensions,
  and 4/2 against 6/4/2 [FACT (relayed, 08) — Ju et al. 2020, §4]. So no single abbreviation matches a
  composer, and choosing one is a convention, not a fact about the music. The study decides 2 against 9
  by register [FACT (relayed, 08) — Ju et al. 2020, footnote 22], where thoroughbass practice writes 9
  for a dissonance resolving to the octave [THEORY — no source fetched]. That is a second convention
  choice, which the declared convention fixes.
- *Source class.* Derived.
- *Status.* Settled. Which convention a display defaults to is the display's own choice.
- *Premise.* Any conventional abbreviation is a deterministic function of the full figure. **False-
  negative path:** a convention whose omissions depend on the preceding figure, such as a continuation
  line. Such a view reads two adjacent full figures and is still a function of published facts.
- *Falsifier.* CODE. **Observable:** published figures. **Decision rule:** falsified if L3 publishes
  only an abbreviated figure, or if an abbreviated rendering cannot be regenerated from the full figure
  and the named convention. **Not falsified by:** two conventions abbreviating one figure differently.

**L3-S28. A figured bass at the continuo grain, where every bass note including passing bass notes is
figured by the sonority actually sounding above it, needs the spelled interval content above the
lowest sounding pitch at every slice. No layer beneath publishes it. L3 does not compute it, and the
want is OQ-L3-7, naming IC-L1 S-49 and S-50.**
- *Defense.* IC-L1 publishes the interval content above the lowest sounding pitch only at the two
  slices of a cue, Y and Z, as unspelled semitone distances [RULED — IC-L1 S-49], and the lowest
  sounding pitch at every slice [RULED — IC-L1 S-50]. S-50 is exhaustive [RULED — IC-L1 beside S-50,
  Ruling 60]. The quantity wanted is S-49's quantity, spelled, at every slice. Computing it here would
  re-derive an L1-defined quantity. The input contract records exactly this shape for L2's want of the
  lowest sounding pitch per slice: L2 *"writes the want instead"*, and the ruling that answered it
  declined *"L2 computes the pitch itself — one named fact with two producers"* [RULED — L2-S28; OQ-L2-11
  answer]. No staged case of a figured passing bass note was met (L3-S25's premise; OQ-L3-14).
- *Source class.* Given — IC-L1 (what is published) and IC-L2 (the precedent). Derived (the want).
- *Status.* **Open** (OQ-L3-7).
- *Premise.* The continuo grain is part of what the charter's *figured bass* means. **False-negative
  path:** the charter means only the span figure. L3-S25 then suffices and the want lapses. The
  question is put with OQ-L3-7.
- *Falsifier.* CODE. **Observable:** L3's figured bass inputs. **Decision rule:** falsified if L3
  computes interval content over the sounding set itself. **Not falsified by:** L3 computing an interval
  between two events that L2's facts name, such as a suspended event and the structural bass (L3-S25).

**L3-S29. L3 never reads the composer's figures, and publishes no comparison between its figured bass
and them. A comparison is the measurement layer's act or a display's.**
- *Defense.* *"Figured bass and chord symbols written by the composer are annotation under S-2, not
  L0"*, usable by a measurement layer as a reference and never as analysis input [RULED — IC-L1 S-8,
  ratified at Ruling 67]. S-2's bar *"binds every layer of the analysis"*, and a reader outside the
  analysis may be handed annotation *"for a purpose other than deciding the music, and may never feed
  it back in"* [RULED — IC-L1 beside S-1/S-2, Ruling 57 (ii)]. A comparison published by L3 would make
  an L3 output change when the annotation is removed, which is S-2's falsifier [RULED — IC-L1 S-2,
  falsifier]. Exemplar 3 carries `<FiguredBass>` elements on its fourth staff [FACT at the file]. This
  session read them as a case of what figures look like, never as input to a statement about what L3
  computes for that piece.
- *Source class.* Given — IC-L1.
- *Status.* Settled.
- *Premise.* None beyond IC-L1's. Its recorded cost stands: where a continuo part's upper voices are not
  written out, the notes under-determine the harmony and the figures are its only record [RULED — IC-L1
  S-8, premise]. L3's figured bass there describes a thinner harmony than the composer's.
- *Falsifier.* CODE. **Observable:** L3's outputs with and without the annotation carrier. **Decision
  rule:** falsified if any L3 output changes when every `<FiguredBass>` element is removed. **Not
  falsified by:** a display showing both side by side.

### 3f. Face (f) — the harmonic rhythm

**L3-S30. The harmonic rhythm L3 publishes is, per bar and per phrase unit, the list of L2's harmonic
boundaries inside it, each referenced by identity and carrying its metric strength class and period
(IC-L1 S-35) and the classes of what changed across it: root, quality, figure, applied target,
tonality. It also gives the count of boundaries per class in each bar. Per phrase unit it adds the
series of its span durations in beats of the notated meter. It does not republish the segmentation.**
- *Defense.* Harmonic rhythm is the rhythm of the changes of harmony, read against the meter, at the
  grain of the bar and the beat [THEORY — standard harmony; no source fetched]. Harmonic change is
  measured to follow the metrical hierarchy: 71.5% of the beats at the level above the tactus carry a
  change, against 22.3% at the tactus and 2.4% below [RULED — charter, L1, carrying Temperley 2009]. So
  the metric position of each change is the content harmonic rhythm adds to the span list. Repertoires
  differ in harmonic rhythm enough that a published detector changes its beat unit from the quarter for
  Haydn to the eighth for Bach *"to cope with the faster harmonic rhythm"* [FACT (relayed, 08) — Bigo et
  al. 2018, §2.3]. The change classes are published separately because analysts differ on what counts
  as a change. Exemplar 1 bar 4 writes `V6 V65`, a figure-only change, where exemplar 2 writes one
  `V6/5` [FACT at the files; L2-S14]. A single count would choose one definition. Referencing L2's
  boundaries rather than restating them follows the one-producer rule: *"published exactly once, on the
  producing layer's output surface; consumers read, never re-derive"* [RULED — pack principles,
  fact-publication corollary; D-100].
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Bar, phrase unit and beat are the grains a consumer of harmonic rhythm reads. **False-
  negative path:** a consumer wanting a rate over a sliding window. It computes the rate from the
  published per-bar lists, which is a consumer's view and not a re-derivation of an L3 fact.
- *Falsifier.* CODE. **Observable:** the harmonic-rhythm record of a bar. **Decision rule:** falsified
  if a listed boundary is not one of L2's, if its metric class differs from L1's, if a change class is
  wrong for the two adjacent spans, or if the record restates a span's chord fields. **Not falsified
  by:** a bar with no boundary, published as an empty list with its reason.

**L3-S31. The harmonic rhythm's uncertainty is read off L2's boundary rivals. The expected count of
boundaries of each class in a bar is the sum, over the change points in it, of the mass of L2 readings
that place a boundary of that class there. That sum is computable from L2's per-span marginals alone.
The distribution of counts needs the whole readings and rival objects (L3-S34). L2 reads none of it.**
- *Defense.* An expectation is linear, so the expected count is the sum of per-position boundary
  probabilities, and the mass of readings with a boundary at p is the total marginal mass of the span
  rivals that start at p [THEORY — elementary probability]. The span marginal is *"the total mass of
  all whole readings that contain that span, with that start, that end and that reading of it"*
  [RULED — L2-S40]. A count's distribution is not linear and needs the joint, as the cadence does
  (L3-S19). L2 consumes nothing L3 publishes, *harmonic rhythm* named among them [RULED — L2-S49].
  IC-L2 records that a harmonic-rhythm term rated per competing reading *inside L2* is a candidate for a
  later measurement [RULED — L2-S31, beside, nothing-from-L3 Ruling 4]. Such a term would be L2's own,
  computed from its own readings, and is not this fact.
- *Source class.* Derived. Given — IC-L2 (L2 reads none of it).
- *Status.* Settled.
- *Premise.* L2's boundary rivals carry the boundary uncertainty. **False-negative path:** rivals
  withheld below a cut-off. Their mass is published per span (L2-S42), and the expected counts carry it
  as unaccounted.
- *Falsifier.* CODE. **Observable:** expected counts against the per-span marginals. **Decision rule:**
  falsified if the expected count differs from the sum of boundary marginals; if a count distribution
  is formed as a product of marginals where a covering rival object exists; or if L2 reads the record.
  **Not falsified by:** expected counts that are not integers.

### 3g. Face (g) — uncertainty on every read-off fact

**L3-S32. Every L3 fact, whether a view or a decision, is published with its own mass and its own
establishment status. There is no separate uncertainty record. L3's mass is of the same class as L2's:
the model's own distribution, not calibrated, comparable only within one working span's publication,
and never read as a frequency of being right.**
- *Defense.* *"Every published fact carries its own mass and its own establishment status; there is no
  layer whose job is uncertainty … A separate uncertainty layer would put one fact in two homes"*
  [RULED — charter, "NOT A LAYER"]. L2's mass is *"a third kind: the model's own distribution … not
  calibrated, compared only within one working span's publication, never read as a frequency of being
  right"* [RULED — L2-S40, weight-meaning Ruling 1]. L3's masses are sums of L2's masses (L3-S34), and
  products of them with L3's own normalised model (L3-S35). No fitted reliability map calibrates
  either, so the class carries over unchanged [CONJECTURE — the class follows from the arithmetic and
  from the absence of any calibration step].
- *Source class.* Given — charter (mass and status on every fact) and IC-L2 (the class). Derived (the
  inheritance).
- *Status.* Settled.
- *Premise.* No L3 fact is calibrated. **False-negative path:** a later fitted reliability map for an
  L3 fact. The class would then change for that fact by its own ruling, as L2-S40 provides for L2.
- *Falsifier.* CODE. **Observable:** every published L3 item. **Decision rule:** falsified if an item
  lacks a mass or an establishment status, or if a mass is labelled calibrated. **Not falsified by:** a
  mass of one where L2 publishes a single reading.

**L3-S33. L3's establishment statuses are three. A *read-off* status is carried by a view, and it is
the weakest status among the items the view reads. *Decided* is carried by an L3 decision whose model
is fitted and established on held-out music. *Provisional* is carried by anything resting on an unfitted
weight, a stand-in value or a provisional input. Until L3-S14's fit exists, every L3 decision, and every
fact read at a position an L3 decision fixes, is provisional.**
- *Defense.* IC-L1's scheme distinguishes notated, computed and provisional, and forbids a consumer
  from putting a provisional item under load [RULED — IC-L1 S-52]. An instrument or recorded figure is
  trusted only after it is positively established [RULED — pack principle #19]. A view cannot be
  better established than what it reads [CONJECTURE — elementary: a function of an unestablished input
  is unestablished]. The cadence is read at a phrase end that L3 decides (L3-S15), so its status
  follows the phrase decision's.
- *Source class.* Derived (inside IC-L1's scheme and principle #19, which are given).
- *Status.* Settled.
- *Premise.* Three statuses suffice. **False-negative path:** a read-off fact over a bar carrying
  L1's defect flag (IC-L1 S-10). The flag travels with the fact, as IC-L1 S-52's premise has it for L1.
- *Falsifier.* CODE. **Observable:** status fields. **Decision rule:** falsified if a cadence or a
  phrase end is marked other than provisional before the phrase model is established, or if a view
  carries a stronger status than an input it reads. **Not falsified by:** a chord symbol marked
  read-off while its cadence is provisional.

**L3-S34. The mass of a view is the total mass of the L2 readings that give it. It is computed from the
L2 rival form that covers the view's extent: per-span marginals for a fact read off one span (the chord
symbol, the span figure), and rival objects or ranked whole readings for a fact read off several spans
(the cadence, a count distribution). The mass not covered is published as unaccounted: L2's withheld
mass (L2-S42) and, where whole readings are needed, the mass beyond the ranked list.**
- *Defense.* A view is a function of the reading, so its probability is the sum of the probabilities of
  the readings mapping to it [THEORY — elementary probability]. Products of per-span marginals assign
  mass to combinations no reading contains [RULED — L2-S41, citing charter DP-A]. L2 publishes the
  forms this needs, and publishes what it withholds [RULED — L2-S40, L2-S41, L2-S42, L2-S45]. An absence
  with no reason is a hidden fact [RULED — IC-L1 beside S-52, Ruling 62 item 7, as L2-S42 applies it].
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* L2's ranked list and rival objects cover the multi-span alternatives that carry mass.
  **False-negative path:** L2-S41's own, the product growth of independent ambiguities. The
  unaccounted mass is then large and published, and a consumer sees that it is.
- *Falsifier.* CODE. **Observable:** masses of single-span and multi-span views. **Decision rule:**
  falsified if a single-span view's mass differs from the sum of the span marginals giving it; if a
  multi-span view's mass is a product of marginals where a covering rival object or whole reading
  exists; or if a view's published masses and its unaccounted mass do not sum to one for the stretch.
  **Not falsified by:** a large unaccounted mass.

**L3-S35. The mass of an L3 decision (a phrase reading, a section reading) composes L2's rivals with
L3's own model. L3's model gives, for each L2 reading r, a normalised distribution over L3 readings d,
given r and the L0 and L1 evidence. The marginal mass of d is the sum over L2's published readings of
r's mass times d's mass given r, with the unaccounted remainder published. The principal L3 reading is
the best d given L2's principal reading. For each L3 rival, L3 publishes under distinct names both its
mass given L2's principal reading and its marginal mass.**
- *Defense.* The law of total probability gives the marginal [THEORY — elementary probability]. The
  principal is fixed by the bar on revision. An L3 principal chosen by the marginal could rest on an L2
  reading L2 did not commit, which would publish a second decision about L2's question [RULED —
  charter, contract table, L3 → L2]. The two masses are different quantities and not one fact in two
  homes. The conditional is L3's own uncertainty given the settled reading, which is the charter's
  premise for L3 (*"given a settled tonal reading"*) [RULED — charter, L3 "Question"]. The marginal adds
  what L2's rivals contribute. A consumer weighing an L3 rival needs to know which source its doubt
  comes from, and neither number recovers the other [CONJECTURE].
- *Source class.* Derived. *Measured* for L3's model (L3-S14), UNESTABLISHED.
- *Status.* Settled in form. **Open** in value (OQ-L3-11).
- *Premise.* L3's decision given a reading depends on that reading and the evidence only. **False-
  negative path:** a phrase decision that should depend on L2's uncertainty itself, for example being
  less ready to end a phrase where L2 is torn. That is not expressible as conditioning on one reading.
  Since L2 publishes no intermediate quantity (L2-S45), it stays unexpressed.
- *Falsifier.* CODE. **Observable:** published phrase rivals with both masses. **Decision rule:**
  falsified if the principal phrase reading is not the best given L2's principal reading; if the
  marginal differs from the stated sum; or if either mass is missing. **Not falsified by:** a rival's
  marginal mass exceeding the principal's.

**L3-S36. Where two L3 readings tie to the precision computed, both are published with equal mass. The
principal is chosen between them by a declared, deterministic order that the publication names, and the
tie is flagged.**
- *Defense.* A tie broken by evaluation order makes the result depend on the arithmetic rather than
  the music, and is not reproducible [RULED — pack principle #16]. IC-L2 fixes the same rule for L2
  [RULED — L2-S43], and L3's views inherit L2's tie flag where they are read off a tied reading.
- *Source class.* Derived (inside principle #16 and L2-S43's form, which are given).
- *Status.* Settled. The order itself (for example, fewer phrase units first, then the earlier
  boundary sequence) is a declaration for the build, not decided here.
- *Premise.* Exact ties are rare. **False-negative path:** symmetric passages. The flag then carries
  the information.
- *Falsifier.* CODE. **Observable:** the publication at an exact tie. **Decision rule:** falsified if a
  tied reading is absent or the tie is not flagged. **Not falsified by:** the principal being the one
  the declared order picks.

### 3h. Face (h) — the boundaries of the layer

**L3-S37. L3 consumes what L0, L1 and L2 publish, and nothing else. From L2 that means the charter's
list and its rivals (L2-S45), never a term value, term weight, partial candidate score or other
intermediate quantity of L2's scoring. The charter's boundary table has no L0 → L3 row, while L3's
consume line names L0. This file reads the consume line as governing.**
- *Defense.* *"Consumes: L2's published facts, plus L0's and L1's. It may not consume anything L2 did
  not publish"* [RULED — charter, L3]. *"No term value, term weight, partial candidate score or other
  intermediate quantity of L2's own scoring crosses"* [RULED — L2-S45]. The table's L2 → L3 row bars
  *"in particular no intermediate quantity of L2's own scoring"* [RULED — charter, contract table]. L3
  reads three L0 facts directly in this file: the key signature's value (L3-S26), the spelled pitches of
  events L2's facts reference (L3-S25), and, if measured to help, slurs and dynamics (L3-S9 (iv)). None
  of them is in the table's L1 → L3 row.
- *Source class.* Given — charter and IC-L2. Derived (the reading of the table's missing row).
- *Status.* Settled, with the missing row recorded as a finding (§7, item 4).
- *Premise.* The consume line governs the table. **False-negative path:** the table is meant to be
  exhaustive. L3-S25 and L3-S26 then need a charter amendment.
- *Falsifier.* CODE. **Observable:** L3's inputs. **Decision rule:** falsified if L3 reads any value
  not published by L0, L1 or L2, or any intermediate quantity of L2. **Not falsified by:** L3 reading an
  L0 fact directly.

**L3-S38. L3 never revises L2, and L2 reads nothing L3 publishes. No L3 fact may change an L2 fact, a
rival or a mass. Where the music suggests that an L3 reading would improve L2's (a phrase symmetry
that would move a key change), that is not acted on in L3. It is a question for a measured backward
edge.**
- *Defense.* *"L3 → L2: Nothing. A read-off fact may not revise the decision it was read off"*
  [RULED — charter, contract table]. *"L2 consumes nothing L3 publishes"* [RULED — L2-S49]. The user's
  condition, recorded with L2-S49: forward-only holds while there is no reason to believe a backward
  edge would improve the inference, and as soon as there is, it is tested by measurement [RULED —
  L2-S49, beside, nothing-from-L3 Ruling 3]. L2-S49's own false-negative path is a modulation an
  expert places to respect a 2 + 2 phrase structure [RULED — L2-S49, premise, which relays Chew; Chew is not in this session's pack].
  That is exactly the case such a measurement would test.
- *Source class.* Given — charter and IC-L2.
- *Status.* Settled.
- *Premise.* None beyond the charter's.
- *Falsifier.* CODE. **Observable:** L2's inputs and published record before and after L3 runs.
  **Decision rule:** falsified if any L2 field differs. **Not falsified by:** L3 publishing a rival
  phrase reading at odds with L2's principal tonality placement.

**L3-S39. L3 never re-derives a fact a layer beneath it publishes, and never supplies a fact of a
lower layer's kind by computing it from the notation. Where it wants one, it writes an open question
naming the input-contract statement concerned, and does without in the meantime. The wants this
derivation found are four: a stated convention for minor-mode degrees (OQ-L3-1, IC-L2 §0 and L2-S21);
the highest sounding pitch per slice (OQ-L3-4, IC-L1 S-50); a repetition or parallelism relation
over the notes (OQ-L3-5, IC-L1 S-50 and S-51); and the spelled interval content above the lowest
sounding pitch per slice (OQ-L3-7, IC-L1 S-49 and S-50).**
- *Defense.* *"Every derived analytical fact is published exactly once, on the producing layer's
  output surface; consumers read, never re-derive"* [RULED — pack principles, fact-publication
  corollary; D-100]. The brief's instruction [RULED — brief §3.1, §2 (h)]. The input contract's
  precedent for L2 [RULED — L2-S47, and the OQ-L2-11 answer's declined option B]. IC-L1's test places a
  computable, decision-free item over the notation at L1 [RULED — IC-L1 S-51].
- *Source class.* Given — charter and brief (the rule). Derived (the list).
- *Status.* Settled. The list is a list of wants, each open.
- *Premise.* The list is complete. **False-negative path:** a want this session did not notice. The
  falsifier surfaces it.
- *Falsifier.* CODE. **Observable:** L3's inputs. **Decision rule:** falsified if L3 computes, from L0
  facts or from L1's sounding sets, any quantity of the kind IC-L1 S-51 assigns to L1, or any quantity
  IC-L1 or IC-L2 defines as a publication. **Not falsified by:** L3 computing an interval between two
  events that L2's facts name (L3-S25), or reading an L0 fact that no layer defines (L3-S26).

**L3-S40. L3's publication covers exactly the working span. A phrase unit or section that crosses a
span edge is published with a mark saying it is cut by the span. L3's in-span facts can depend on music
beyond the span: a phrase that ends after the edge, or a section whose identity rests on earlier
material. Where they do, L3 asks for a larger span from the caller, as L2 does. It stops when its
in-span publication stops changing, under the same safety cap, and marks the publication truncated if
the cap ends the loop. Whether L3 may act as such a requester is a question for the user (OQ-L3-10 ★).**
- *Defense.* *"The analysis output covers exactly the selection, and music beyond it is evidence"*
  [RULED — D-260 as relayed in L2-S22]. A layer *"extends until 'the layer's in-selection output stops
  changing'"* [RULED — D-261 as relayed in L2-S22]. *"The decision to enlarge, the increment and the
  stop test belong to the requester, never to L0 or L1"* [RULED — IC-L1 beside S-53, Ruling 46 (v)].
  L2-S22 makes L2 *"the layer that asks for more music"* [RULED — IC-L2], and its publication covers
  exactly the working span [RULED — L2-S48], so L3 receives no L2 reading of the context. A phrase's end
  beyond the edge is therefore invisible to L3 unless the span grows. The cut mark follows IC-L1's
  pattern for events cut by the span [RULED — IC-L1 S-32]. Sections pose the hardest case. Exemplar 2's
  recapitulation at bar 42 is identified against an exposition 41 bars earlier [FACT at the file], so
  section reading can need context far wider than any phrase, against the bounded-context rule that
  cost scales with the working span [RULED — D-030 and D-031 as relayed in IC-L1 S-32]. The safety cap
  (D-624, relayed in L2-S22) bounds it, and the truncation mark says so.
- *Source class.* Given — design intent as relayed by IC-L1 and IC-L2 (the mechanism). Derived (its
  application to L3).
- *Status.* **Open** on whether L3 may request (OQ-L3-10 ★). Settled that edge-crossing units are marked.
- *Premise.* L3's in-span publication converges within the cap for ordinary music. **False-negative
  path:** section readings that never settle short of the whole piece. They are then marked truncated
  at every selection smaller than the piece.
- *Falsifier.* CODE. **Observable:** L3's publication after successive enlargements. **Decision rule:**
  falsified if an edge-crossing unit lacks its mark, if L3 stops while its in-span publication still
  changes and the cap has not been reached, or if a cap stop is unmarked. **Not falsified by:** a marked
  stop at the cap or at the record's own edge.

**L3-S41. L3 is deterministic. Its publication after any sequence of enlargements, or after an edit,
equals a single fresh run over the final span and the edited record.**
- *Defense.* *"The result after any sequence of extensions must equal a single fresh run over the final
  loaded span"* [RULED — D-264 as relayed in L2-S48]. L2 meets it (L2-S48) and L3's inputs are L2's
  publication plus L0 and L1, which meet it too [RULED — IC-L1 beside S-53, Ruling 46 (ii)]. L3-S36's
  tie order removes the one remaining source of nondeterminism.
- *Source class.* Given — design intent as relayed by IC-L2. Derived (its application to L3).
- *Status.* Settled.
- *Premise.* L3's model is a function of its inputs. **False-negative path:** none known.
- *Falsifier.* CODE. **Observable:** the publication after enlargements against a fresh run.
  **Decision rule:** falsified if any published field differs. **Not falsified by:** internal caches
  differing.

**L3-S42. Two dependencies on out-of-scope subjects are stated as statements in their own right.** (i)
**The voice-leading axis.** L3's phrase is the harmonic spine's phrase, which tiles. The accepted melodic
phrase, which overlaps across voices, is the axis's, and L3 reads no fact of the axis in this
specification. (ii) **The measurement of the analysis.** How an annotation's phrase signs, cadence
labels, gaps and elisions are mapped onto L3's tiling and its features for grading is the
measurement-design stage's (OQ-L3-12).
- *Defense.* (i) The charter places *"the accepted melodic phrase"* on the second axis, whose phrase
  spans *"overlap across voices by construction and tile only within one voice"*, and lets published
  facts cross between spine and axis in either direction [RULED — charter, the second axis and the
  contract table]. IC-L2 records the charter's own tension, that *"neither L2's nor L3's consume line
  names the axis"*, as left for the whole-architecture coherence review [RULED — L2-S24, beside]. (ii)
  The measurement of the analysis is *"a later stage's business"* [RULED — charter, "NOT A LAYER"]. The
  brief puts it out of scope [RULED — brief §2, Scope].
- *Source class.* Given — charter and IC-L2.
- *Status.* Settled as a statement of dependency.
- *Premise.* L3's harmonic phrase does not need the axis's melodic phrase. **False-negative path:**
  thematic parallelism (OQ-L3-5), which may be published by the axis rather than by L1. If it is, L3
  reads it as a published fact under the charter's spine–axis row.
- *Falsifier.* RESIDUAL — a modelling premise.

---

## 4. Open questions

Each names the face of the brief's §2 it belongs to and the statement that raises it. None is filled
with a plausible reading. The five marked ★ are those this session would put to the user for a
ruling, and each carries the question it would ask.

- **OQ-L3-1 (face (a); L3-S2) — the minor-mode degree convention.** IC-L2 §0 defines L2's degree as a
  scale step *"relative to the span's tonality, with any chromatic alteration"*. L2-S21 makes minor one
  mode whose sixth and seventh degrees *"may each be raised or not"*. Neither says which form an
  unaltered VI or VII names. *The input-contract statements concerned:* IC-L2 §0 (the Chord row) and
  L2-S21. A root computed under the wrong convention is a semitone off.
- **OQ-L3-2 ★ (face (c); L3-S17) — the principal cadence vocabulary.** *Question for the user:* which
  theory of cadence names the principal type? The candidates are Caplin's typology, which needs a
  root-position dominant for an authentic cadence and has an evaded category; the American textbook
  set, under which an inverted V–I is an imperfect authentic cadence; and the extended chorale
  vocabulary with the subdominant stop. Or is no vocabulary principal, with the features and every
  declared vocabulary's view published side by side? This is the same kind of question as the
  charter's DP-N, and exemplar 1 bar 4 is its case.
- **OQ-L3-3 ★ (face (b); L3-S8, L3-S11) — a phrase end with no notated cue.** *Question for the user:*
  the charter says *"the span's boundaries come from the notated cues, and the cadence is aligned to
  them"*. At an elided cadence such as exemplar 1 bar 42 or exemplar 3 bar 12 beat 3, the only notated
  cues are the bar line (bar 42) or nothing beyond the per-voice relations and the metric class (bar 12
  beat 3). May the cadential evidence place a phrase end there? L3-S8 makes every change point a
  candidate and lets the evidence decide. That is this session's reading, and it moves the charter's
  sentence from a rule about *where* boundaries may fall to a statement about *which evidence leads*.
- **OQ-L3-4 (faces (c), (h); L3-S16) — the highest sounding pitch per slice.** The PAC/IAC split in
  every vocabulary needs the soprano's degree at the arrival. L1 publishes the lowest sounding pitch per
  slice and no highest one (IC-L1 S-50, exhaustive). *The input-contract statement concerned:* IC-L1
  S-50 (with S-44's naming and S-51's test). Would S-50's list gain *per slice, the highest sounding
  pitch of its sounding set*, published under that name with its witness? Until then feature (6)
  carries a named reason.
- **OQ-L3-5 (faces (b), (d), (h); L3-S9, L3-S23, L3-S42) — thematic parallelism.** Section reading,
  the evaded cadence, and some phrase ends need a relation saying that a stretch restates an earlier
  one, transposed or not. No layer beneath publishes it. By IC-L1 S-51's test it is an L1-kind item.
  It may instead belong to the voice-leading axis. *The input-contract statements concerned:* IC-L1
  S-50 and S-51, or the charter's spine–axis row. Which layer publishes it, and in what form?
- **OQ-L3-6 ★ (face (d); L3-S24) — form-function names.** *Question for the user:* does L3 publish
  names of formal function (exposition, second theme, development, recapitulation) beside the grouping,
  as exemplar 2 writes them? Adding them amends L3's charter list.
- **OQ-L3-7 (faces (e), (h); L3-S28) — the continuo grain.** A figured bass that figures passing bass
  notes by their own sonority needs the spelled interval content above the lowest sounding pitch at
  every slice. IC-L1 S-49 publishes it only at cue slices and unspelled. *The input-contract statements
  concerned:* IC-L1 S-49 and S-50. Would L1 publish it per slice, spelled? With it goes the question
  whether the charter's *figured bass* means the continuo grain at all.
- **OQ-L3-8 ★ (face (a); L3-S7) — the pivot label.** *Question for the user:* IC-L2 carries to this
  specification whether the label *"this chord is in both tonalities"* is published at L3 or as a
  display view. Does L3's charter list gain it? It would be a view, deciding nothing.
- **OQ-L3-9 (face (a); L3-S5) — the augmented sixth in a display.** L3 publishes no root for the
  augmented sixths. Whether a display respells them as dominant-seventh symbols is the display's
  convention. Recorded so the gap is not mistaken for a defect.
- **OQ-L3-10 ★ (face (h); L3-S40) — L3 as a requester of more music.** *Question for the user:* may L3,
  like L2, ask the caller for a larger span when its in-span phrase or section reading depends on music
  beyond the edge, stopping by convergence under the safety cap? If not, L3 marks every edge-crossing
  unit and stops at the span.
- **OQ-L3-11 (faces (b), (d), (g); L3-S9, L3-S14, L3-S23, L3-S35) — the measured values.** All
  weights of the phrase and section models. The fit needs licence-clear music with annotated phrase
  beginnings and endings and section boundaries, a piece-level held-out split and a declared capacity.
  Neither exemplar with phrase signs is licence-clear (exemplar 3 non-commercial, exemplar 1
  unstated). *A measurement, not a ruling.* UNESTABLISHED.
- **OQ-L3-12 (faces (b), (d); L3-S12, L3-S42) — grading against annotations.** *For the
  measurement-design stage:* how an annotation's phrase signs map onto L3's tiling, where the
  annotation leaves gaps (exemplar 1 bars 26 to 28), writes elisions (`}{`), and places its cadence
  label at the arrival and its phrase-end sign later (exemplar 1 bars 11 to 12).
- **OQ-L3-13 (face (b); L3-S11) — a case the staged set does not supply.** An elision whose overlap
  spans several beats rather than one position.
- **OQ-L3-14 (faces (c), (e); L3-S17, L3-S25, L3-S29) — cases the staged set does not supply.** A
  deceptive, an evaded, a plagal and a Phrygian half cadence, to test L3-S16's features against
  L3-S17's types. A figured bass over a pedal point (L3-S25's pedal clause). A figured passing bass
  note, the continuo grain of L3-S28. A continuo part with no written upper voices (IC-L1 S-8's
  recorded cost, L3-S29).

**Questions for the user, counted from the ★ marks: 5 of 14** (OQ-L3-2, 3, 6, 8, 10). DP-N and DP-Q,
which L3-S6, L3-S18 and L3-S20 touch, are the charter's own open questions and are not counted here.

---

## 5. The measured-cost record

*Declared, as the brief says, as the writing side's addition and not a phase requirement. Times are
differences between timestamps this session took with the shell clock (`date -u`) as it worked. The
time the harness spent placing files in context before this session's first act, and the session's
own composing time before its first tool call of the turn, are not measured.*

**Times.**

| Interval | From | To | Duration |
|---|---|---|---|
| Reading, before the first statement was written (first tool call of the working turn to the start of the draft) | 11:28:21 | 11:38:10 | 9 min 49 s |
| Terms, subject and form sections (§0 to §2) | 11:38:10 | — | not separable: written in one call at the start of face (a)'s interval |
| Face (a), L3-S1 to L3-S7 — 7 statements | 11:38:10 | 11:40:23 | 2 min 13 s (≈ 19 s per statement, a face average) |
| Faces (b) and (c), L3-S8 to L3-S21 — 14 statements | 11:40:23 | 11:43:46 | 3 min 23 s (≈ 15 s per statement) |
| Faces (d), (e) and (f), L3-S22 to L3-S31 — 10 statements | 11:43:46 | 11:45:54 | 2 min 8 s (≈ 13 s per statement) |
| Faces (g) and (h), L3-S32 to L3-S42 — 11 statements | 11:45:54 | 11:47:09 | 1 min 15 s (≈ 7 s per statement) |
| Checking and tallying (cross-references, labels, counts) | 11:47:09 | 11:48:44 | 1 min 35 s |
| §4 to §7 | 11:48:44 | 11:50:09 | 1 min 25 s |
| Correction pass after a re-check at the exemplars (see §6, *Corrections made before delivery*) | 11:50:09 | 11:52:02 | 1 min 53 s |

*Per-statement times are face averages. The statements of a face were written in one call, so no
individual statement's time was measured, and none is reported as if it had been.* The first-face
interval includes the time to write §0 to §2.

**Counts. Denominator: 42 statements (L3-S1 to L3-S42).**

| Quantity | Count | Of 42 | Statements |
|---|---|---|---|
| Status carries an **open** part | 13 | 13/42 | S2, S5, S7, S8, S9, S14, S16, S17, S23, S24, S28, S35, S40 |
| …of which this session would put to the user for a ruling (★) | 5 | 5/42 | S7 (OQ-L3-8), S8 (OQ-L3-3), S17 (OQ-L3-2), S24 (OQ-L3-6), S40 (OQ-L3-10) |
| Source class names a **given** source | 26 | 26/42 | S1, S2, S3, S7, S8, S9, S10, S12, S13, S15, S19, S20, S21, S22, S23, S24, S28, S29, S31, S32, S37, S38, S39, S40, S41, S42 |
| …wholly given (no derived part) | 5 | 5/42 | S21, S24, S29, S38, S42 |
| …given by the **charter** | 17 | 17/42 | S1, S2, S7, S8, S9, S10, S12, S13, S15, S19, S22, S24, S32, S37, S38, S39, S42 |
| …given by **IC-L1** | 6 | 6/42 | S8, S9, S21, S23, S28, S29 |
| …given by **IC-L2** | 9 | 9/42 | S3, S7, S20, S28, S31, S32, S37, S38, S42 |
| …given by design-intent entries **as relayed in IC-L1 or IC-L2** | 2 | 2/42 | S40, S41 |
| …given by the **brief** | 1 | 1/42 | S39 |
| Source class includes **measured** | 4 | 4/42 | S9, S14, S23, S35 |
| Sixth field **could not be written** (UNVERIFIABLE) | 0 | 0/42 | — |
| Sixth field is RESIDUAL rather than CODE | 1 | 1/42 | S42 |

A statement may name more than one given source, so the per-source rows do not sum to the given row.

**On the *given* share, as the brief asks.** 26 of 42 statements name a given source, and 5 are
wholly given. The share is high because most statements obey a charter sentence or an input-contract
statement *and* derive the *how* inside it. The wholly given five are the layer's boundary rules and
one ruled exclusion, the composer's figures. The derivation is thinnest on face (h). Faces (b), (c)
and (e) carry most of the derived content.

**What each statement consulted.** Pack members are cited by number (07 the charter, 08 the extracts
by source, 09 the ledger, 02 the principles). IC-L1 and IC-L2 statements are cited by their numbers.
Exemplars are cited as ex1, ex2 and ex3. No fetched source was consulted by any statement, since none
was fetched.

| Statement | Pack | Input contract | Exemplars |
|---|---|---|---|
| S1 | 07 (L3, DP-L, DP-A); 08 BACHI | L2-S27 | — |
| S2 | 07 (L3); 08 Hentschel 2021; 02 #12 | IC-L2 §0, L2-S1, S5, S6, S21 | ex3 |
| S3 | 07 (L3); 09 C6; 08 ChoCo | L2-S4, S27 | — |
| S4 | 07 (L3); 09 C28, C32, C38; 08 McLeod & Rohrmeier 2021 | IC-L2 §0, L2-S28; IC-L1 §0, S-44 (met passage) | — |
| S5 | 07 (L3); 02 #6 | L2-S4 (beside), S8, S44 | — |
| S6 | 07 (table, DP-N); 09 C11 | L2-S18, S29, S42 | ex1, ex2 (bars 24, 31, 41) |
| S7 | 07 (L3) | L2-S19 | ex1, ex2 (bar 41) |
| S8 | 07 (L3, L1, NOT A LAYER, DP-J) | IC-L1 beside S-39 (R48) | ex1 (bars 42, 58), ex3 (bar 12) |
| S9 | 07 (L3, table); 08 de Clercq, Bigo 2018, Sears 2018, Hamanaka 2013 | IC-L1 S-7, S-39, S-41, S-50, R48–R50, R61; L2-S7, S49 | — |
| S10 | 07 (L3); 08 de Clercq | L2-S14 | ex1 (bars 11–12, 26–28), ex3 (bar 4) |
| S11 | 02 #12 | — | ex1 (bar 42), ex3 (bar 12) |
| S12 | 07 (second axis) | — | ex1 (bars 26–29) |
| S13 | 07 (L2, DP-K, NOT A LAYER) | — | ex1 (bar 13), ex2 (bars 13–14) |
| S14 | 02 #20, #21; 08 Hamanaka 2013, Bigo 2018, de Clercq | L2-S38 | ex1, ex3 (licence fields) |
| S15 | 07 (L3); 08 Karystinaios 2022 | IC-L1 S-50, S-52; L2-S45 | — |
| S16 | 08 Bigo 2018, de Clercq | IC-L1 S-35, S-50, S-51, beside S-50 (R60); IC-L2 §0 | ex3 |
| S17 | 07 (DP-N); 08 de Clercq, Sears 2018, Illescas | — | ex1 (bar 4) |
| S18 | 07 (DP-Q); 08 de Clercq; 02 #12 | — | ex1 (bars 4, 45) |
| S19 | 07 (table, DP-A); 08 de Clercq, Nápoles López 2020 | L2-S18, S41, S42, S45 | ex1, ex2 (bar 31) |
| S20 | 07 (DP-N) | L2-S14, S29 | ex1, ex2 (bars 11–12, 22–26) |
| S21 | 08 Bigo 2018, Karystinaios 2022 | IC-L1 S-46, S-48 (R53), S-52; L2-S37 | — |
| S22 | 07 (L3); 08 Lazzari 2023 | — | ex1 (bar 42), ex2 (Form labels) |
| S23 | 08 Feisthauer 2021, Lazzari 2023 | IC-L1 S-39, S-41, S-42, S-43, S-51, R51 | ex1 (bars 28–29, 42), ex2 (bar 42 note) |
| S24 | 07 (L3) | — | ex1 (bar 13), ex2 (Form labels) |
| S25 | 08 Ju 2020 | IC-L1 S-50; IC-L2 §0, L2-S8, S9, S28, S29 | ex3 (bars 1–3, figures) |
| S26 | 07 (L3); 09 C14; 08 Ju 2020 | IC-L1 S-6, S-9; L2-S47 | ex3 |
| S27 | 08 Ju 2020 | — | — |
| S28 | — | IC-L1 S-49, S-50, beside S-50 (R60); L2-S28, OQ-L2-11 | — |
| S29 | — | IC-L1 S-2, S-8, R57 | ex3 |
| S30 | 07 (L1, Temperley figures); 08 Bigo 2018; 02 (fact-publication corollary) | L2-S14 | ex1, ex2 (bar 4) |
| S31 | — | L2-S31 (beside), S40, S42, S49 | — |
| S32 | 07 (NOT A LAYER) | L2-S40 | — |
| S33 | 02 #19 | IC-L1 S-10, S-52 | — |
| S34 | 07 (DP-A) | IC-L1 beside S-52 (R62); L2-S40, S41, S42, S45 | — |
| S35 | 07 (L3, table) | L2-S45 | — |
| S36 | 02 #16 | L2-S43 | — |
| S37 | 07 (L3, table) | L2-S45 | — |
| S38 | 07 (table) | L2-S49 | — |
| S39 | 02 (fact-publication corollary) | IC-L1 S-51; L2-S47, OQ-L2-11 | — |
| S40 | — | IC-L1 S-32, beside S-53 (R46); L2-S22, S48 | ex2 (bar 42) |
| S41 | — | IC-L1 beside S-53 (R46); L2-S48 | — |
| S42 | 07 (second axis, table, NOT A LAYER) | L2-S24 (beside) | — |

**Pack members consulted by no statement:** 00 (read for its order and boundary only), 01 (phase
definitions), 03 (writing standards, applied to the form of the whole file and cited by no statement),
04 (dispatch protocol), 05 (design intent, not read beyond its headings; see §6), 06 (defect catalog).
**Extract sources of 08 consulted by no statement:** McLeod & Rohrmeier 2024, Sapp 2005, de Haas et
al. 2013.

---

## 6. The independence record

**Boot.** At boot this session received the brief alone, with harness scaffolding on the brief's
allow-list, no project folder and no repository file. That was declared in the session's first message
before §0 was read, and is not repeated here. The fifteen staged files arrived in the second message.
None of them was present at boot.

**Files opened, each with the extent seen.** A file marked *pre-read* was placed in context by the
harness before this session's first act of the second turn, without a call by this session.

| File | Extent seen | How |
|---|---|---|
| The brief, `cowork_blind_session_brief_l3.md` | whole (536 lines) | pre-read at boot |
| `00_READ_THIS_FIRST.md` | whole | pre-read |
| `01_the_phase_definitions.md` | whole | pre-read |
| `02_the_guiding_principles_and_the_conventions.md` | whole (lines 1–774) | read by this session in two parts |
| `03_the_writing_standards.md` | whole | pre-read |
| `04_the_dispatch_protocol.md` | lines 1–803 of 1,427 | read by this session; the rest was not read, being process rules that bear on no statement |
| `05_the_ratified_design_intent.md` | **its heading lines only**, every `#`-heading of the file (a heading search whose output was read whole); **no entry body** | stopped by the stop-on-meeting clause; see below |
| `06_the_defect_type_catalog.md` | whole | pre-read |
| `07_the_charter_the_layers_and_the_decisions.md` | whole | pre-read |
| `08_the_seventeen_research_extracts.md` | whole (lines 1–1,815), all seventeen sources: Ju 2020; Bigo 2018; Karystinaios & Widmer 2022; Sears 2018; Illescas; de Clercq; Feisthauer 2021; Hamanaka 2013; Lazzari 2023; Nápoles López 2020; McLeod & Rohrmeier 2021; BACHI; Hentschel 2021; McLeod & Rohrmeier 2024; Sapp 2005; de Haas 2013; ChoCo 2023 | read by this session |
| `09_the_empirical_findings_ledger.md` | whole | pre-read |
| `the_l0_l1_specification_the_input_contract.md` | whole (lines 1–1,737) | read by this session |
| `the_l2_specification_the_input_contract.md` | whole (lines 1–2,433) | read by this session |
| `analysis_DT.txt` (exemplar 2) | whole (72 lines) | pre-read |
| `K545-1.mscx` (exemplar 1) | **not whole.** A search over the whole file for staff, bar, harmony-label, fermata, bar-line, repeat and rest lines (positions and label texts only); every `<Harmony>` label text; lines 1,350–1,419 (staff 1, bars 12–14); lines 4,040–4,099 (staff 1, end of bar 41 to the start of bar 43); the metadata lines | read by this session; flagged too large to pre-read |
| `op01n08a.mscx` (exemplar 3) | lines 1–2,000 pre-read (staves 1 and 2 whole, staff 3 to bar 13); lines 2,000–2,399 read by this session (staff 3 bars 13–16, staff 4 bars 1–6); a search over the whole file for bar, harmony-label, figured-bass, fermata and bar-line positions. Staff 4's figures after bar 6 were not read, only their positions | pre-read in part, read in part |

**Files not opened.** No other file of this project. No fetched source: this session fetched no paper,
so every literature FACT is relayed from pack member 08, and no primary of the seventeen was re-read.
One tool-output file, the harness's saved copy of the heading search over member 05, was read whole.
It is this session's own search output and not a project file.

**The stop-on-meeting record.**

1. **Member 05, its heading lines, lines 2,487 and 2,501 of the member.** The heading search displayed
   the headings of entries D-482 and D-484. The first is about the fermata scan's copies retiring into
   one owned primitive. The second is about the phrase-boundary primitive as a derived view that
   inherits the loaded span, requests no extension and publishes a per-profile max-normalised boundary
   confidence. They are statements about how this project's analysis handles phrase-boundary evidence,
   which is face (b) of the subject. **Seen:** the two heading lines, delivered with the rest of the
   heading list in one output. **Action:** this session stopped reading member 05 there and opened no
   entry body of it. The same listing also showed headings near the subject that are recorded here:
   D-335 (the Roman numeral and a derived function read-out), D-406 and D-502 to D-510 (progression
   recognition), and D-504 (a harmonic sequence emitted as key evidence). None entered a statement.
   Every design-intent identifier this file cites (D-030, D-031, D-100, D-260, D-261, D-264, D-292,
   D-624) is cited **as relayed in IC-L1's or IC-L2's text**, never from member 05.
2. **IC-L1, a ruled statement of L3's design that the cut left in place.** The §0 entry *The lowest
   sounding pitch* (lines 82–86), S-44 (lines 1,252–1,254) and S-44's amendment note (lines
   1,282–1,288) carry *"the chord's bass note, which L3 publishes, read off the figure L2 decides"*.
   **Seen:** whole, while reading the file. This session did not stop reading the file at it. L3-S4
   coincides with it and is flagged at L3-S4 for the comparison to check.
3. **IC-L2's mentions of L3, read as statements of what L2 hands over, as the brief §3.1 directs:**
   L2-S14's premise (a restated chord after a phrase end is L3's to divide), L2-S19 beside (the pivot
   label carried to L3), L2-S26 ruled (a grace note's clash is a fact L3 can read off), L2-S27 (no chord
   symbol at L2), L2-S29 beside (*"L3's cadence reading must handle a committed I6/4"*), L2-S31 beside
   (a harmonic-rhythm term inside L2 as a candidate measurement), and L2-S49.
4. **Statements about this project's existing implementation on other subjects, seen while reading,
   none bearing on §2's subject:** member 02's founding instance of the never-work-from-memory rule
   (slice identity, an L1 subject); member 09's entries whose subjects or bounds name implementation
   mechanisms (C9 and D-300, C47, C20 and others; L2 subjects); IC-L2's L2-S6 beside (a legacy decoder
   declaring "Mixolydian briefly"), L2-S17 (D-528, D-450, D-057, D-056), L2-S18 beside (D-291's
   measured share), L2-S22's note on D-261's as-built description, L2-S35 beside (D-339), L2-S38
   beside (D-383's measured share) and L2-S36's sizing record. None entered a statement.
5. **Positive statement.** Beyond items 1 and 2, this session met no passage stating how this
   project's analysis currently reads a cadence, a phrase, a section, a chord symbol, a figured bass or
   a harmonic rhythm.

**Also recorded.** Member 02's convention *"THE ORDINARY SESSION-START READ BINDS EVEN WHEN THE OPENING
INSTRUCTION NAMES A SINGLE FILE"* contradicts the brief and member 00, which replace that read for this
session. The brief and member 00 were followed. The contradiction has the shape the catalog names DT-20.

**Where a want was written as an open question instead of filled.** Published facts of a layer
beneath: OQ-L3-1 (IC-L2 §0, L2-S21), OQ-L3-4 (IC-L1 S-50), OQ-L3-5 (IC-L1 S-50, S-51, or the axis)
and OQ-L3-7 (IC-L1 S-49, S-50). Cases the staged set does not supply: OQ-L3-13 and OQ-L3-14.

**Corrections made before delivery, recorded so the draft's history is not hidden (#12).** A re-check
of every exemplar citation against the files, after §4 to §7 were written, corrected five sentences.
(a) L3-S25 and L3-S28 had cited a `6` over a passing D at exemplar 3 bar 2 as a figured passing bass
note. Read in element order, that figure stands on the following E♭, so the case was withdrawn and
recorded as not supplied (OQ-L3-14). (b) L3-S2 had said exemplar 3 writes `VII` and writes
`V7/IV/III`. It writes `viio/VII` and no chain of depth two, and the chain is cited to L2-S5 instead.
(c) L3-S6 and L3-S19 had leaned on IC-L2's reading of bar 31. They now state this session's own reading
of the two files. (d) L3-S9 had said rhythmic features help a detector *most* on the half cadence. The
extract's table does not support *most*, and the sentence now quotes the authors' *"especially for
HC"*. (e) L3-S2's falsifier had named D as the root of V7/IV/III in C minor. It is E♭. A sixth
correction, made earlier, relabelled two citations of Chew as relayed through L2-S49, since Chew is not
in this session's pack.

**Exemplars as cases, not a corpus.** No count was taken from any exemplar, no statement rests on how
often anything occurs in them, and the two readings of exemplar 1's piece are used only to show
where competent readers differ.

**Capacity.** No file was left unread for lack of capacity. Member 04 was read in part by choice.
Member 05 was read no further than its headings because of the stop clause. Exemplars 1 and 3 were
read in part, as the brief permits.

---

## 7. Where the brief's decomposition seemed wrong or incomplete

1. **Views and decisions are mixed across the faces.** Faces (a), (e) and (f) are views, and (b) and
   (d) are decisions. Face (c) is a view read at a decided position. Face (g) is therefore two
   questions: a view's mass is a sum over L2's readings (L3-S34), and a decision's mass composes L2's
   rivals with L3's own model (L3-S35).
2. **Faces (b) and (c) share an unnamed object: the alignment of the cadential arrival to the phrase
   end.** The exemplars place a cadence label and a phrase-end sign at different chords (exemplar 1
   bars 11 and 12). L3-S10 publishes both positions.
3. **Face (c) presumes one vocabulary of cadence types.** The traditions differ on what counts as a
   cadence, in the same way as the cadential six-four of DP-N (L3-S17, OQ-L3-2 ★).
4. **The charter's boundary table has no L0 → L3 row, while L3's consume line names L0** (L3-S37). The
   figured bass reads the key signature's value and the events' spellings from L0.
5. **Face (f) does not say what harmonic rhythm adds beyond L2's segmentation.** The answer here is the
   metric position and the class of each change (L3-S30), so that the segmentation is not published
   twice.
6. **Faces (b) and (d) are one object.** Section boundaries must be phrase boundaries (L3-S22), so the
   two are read as one consistent nested grouping, not as two independent decisions.
7. **Face (e)'s *figured bass* is ambiguous between two grains:** the figure of each decided harmony,
   and the continuo grain that figures every bass note. The first is a view of L2's facts (L3-S25), and
   the second needs an L1 publication that does not exist (L3-S28, OQ-L3-7).
8. **The charter's sentence on phrase boundaries meets a hard case at elided cadences** (OQ-L3-3 ★).
   The faces do not anticipate a phrase end with no notated cue.

*End of file.*
