# The derived L3 specification — the read-off facts: cadence and its type, phrase and section grouping, chord symbol, figured bass, harmonic rhythm — as amended by the L3 family rulings of 2026-11-02 to 2026-11-08

> **STATUS: DERIVED SPECIFICATION — THE BLIND DERIVATION OF L3 AS AMENDED BY THE L3 FAMILY RULING RECORDS OF
> 2026-11-02 TO 2026-11-08 (`records/cowork/rulings/`, listed in
> `records/cc/instructions/cc_instruction_l3_application_2026_11_08.md` §L); NOT RATIFIED.** Written by Claude Code
> under that dispatch's Task 1, from the derivation `cowork_blind_derivation_l3_2026_10_17.md` at blob `c01793f98c51e0267fb0dc7487613ac477cc1fbb`, which stands untouched as the record of the blind act (D-674; the L3 route
> ruling of 2026-11-02, §2 step 2). Every derived statement keeps its number and its six-field form; every amendment
> stands in place and names the record that made it and the ruling, or, where a record's own derivation made it, the record's section, with the derived wording preserved at the derivation or
> in the same field (#12). **A sub-item or mark opening *Recorded* is a record's own derivation and not a ruling, and is
> challengeable; one opening *Ruled*, *Beside* or *ANSWERED* carries the user's word at the record named.** A `(was: …)`
> or `(added; …)` mark that says *text ratified* marks wording the user ratified as written at the statement-texts
> ruling record it names (Rulings 12 to 17, `records/cowork/rulings/`, 2026-11-13 and 2026-11-14); one that says
> *staleness fix shown* marks a correction the writing side made and showed the user without a question (the user's
> rule of 2026-09-22). Statements under *Statements added by the L3 family rulings* carry no L3-S number. The open
> questions of §4 stand with their ANSWERED marks where a ruling answered them (OQ-L3-2, OQ-L3-3, OQ-L3-4, OQ-L3-5, OQ-L3-6, OQ-L3-7, OQ-L3-8 and OQ-L3-10) and open
> otherwise. Apart from the wordings marked *text ratified*, nothing in this file is ratified; the ratification act
> over the file is the user's, on a decision surface over this text.

*Application in progress: this file carries the amendments of §L.1 to §L.33 of records/cc/instructions/cc_instruction_l3_application_2026_11_08.md only. §L.34 to §L.55 are applied by later Claude Code sessions, one stretch each (was: "§L.16 to §L.55"; staleness fix shown, records/cc/instructions/cc_instruction_l3_application_session_4_task_1_stretch_3_2026_11_22.md, §3 item 4); the banner above is true of the file only when the last of them removes this line.*

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, Ruling 1).* Stands as derived.
  > L3's chord symbol publishes the root spelled — the span's spelled tonic transposed by the degree's diatonic interval, the degree's alteration applied, applied chains resolved from the far end (L3-S2) — with the pitch class the charter names published in the same item as its projection.

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
assignments and not in the chord (L2-S4, L2-S8), are not written into the chord symbol. They are read in the continuo-grain figured bass (L3-S28), which gives under every bass note what actually sounds
above it; of the elaborations, the span figure (L3-S25) figures only those L2 assigns as a suspension or an
appoggiatura. (was: "They are read in the figured bass (L3-S25)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (h); staleness fix shown, ratification_surfaces/cowork_l3_application_release_statement_texts_surface_2026_11_13_part_6.md, under Ruling 7 of the second Part B ruling record) (iii) **A silent span:** the chord symbol carries L2's named reason
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
- *Recorded (records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (i)).* Stands as derived — recorded by the record as this side's derivation, not ruled; challengeable.
  > L3-S6's merging rule stands as derived; DP-N is not decided here.

**L3-S7. At each change of tonality in L2's principal reading, L3 publishes the pivot label as a view: the decided
chord of the span on each side of the change, re-expressed as a scale degree in the other tonality, each carrying a
flag stating whether that chord is diatonic in both tonalities. The flag is a fact, not a test of pivot-ness. No chord
is named "the pivot". Each rival whole reading L2 publishes gives its own set. Under IC-L2 a pivot is published as one
span with one tonality and the other tonality's reading as a rival (L2-S19); the label re-expresses L2's decided
chords and decides no tonality.** (was: "L3 does not publish a pivot label (*this chord is degree a in one tonality and degree b in the next*). Under IC-L2 a pivot is published as one span with one tonality and the other tonality's reading as a rival (L2-S19). The label is a re-expression of L2's decided chord in the neighbouring span's tonality. It is not on L3's charter list, and adding it is a ruling (OQ-L3-8)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_13_l3_application_release_statement_texts_sitting.md, Ruling 12)
- *Defense.* IC-L2 carries the question to this specification in terms: *"Whether and where that label is published — at L3, or as
  a display view — is not decided by this ruling and is carried to L3's own specification"* [RULED — L2-S19, beside,
  pivot-chord Ruling 1]. The pivot-label record's Ruling 1 answers it: L3 publishes the label as a view [RULED —
  OQ-L3-8]. Nothing is decided in re-expressing a decided chord; no chord is chosen as the pivot; L2's one tonality per
  span is untouched. For a label at L3 rather than one computed only by a display, the record's grounds are the charter
  placing the chord symbol, itself a view, at L3 [RULED — charter, L3], and D-100 and D-295 read as reaching a view;
  that reading, and so the choice of a label at L3 over one at a display, the record states as this side's. Exemplars 1
  and 2 show the case: one analyst writes the pivot (`N6 F: IV6`) and the other writes the change at the same chord with
  no pivot (`IV.IV6`) [FACT at the files]; a pivot-aware output can be compared directly with the annotation that writes
  the pivot. (was: "IC-L2 carries the question to this specification in terms: *"Whether and where that label is published — at L3, or as a display view — is not decided by this ruling and is carried to L3's own specification. L3's charter list is not amended"* [RULED — L2-S19, beside, pivot-chord Ruling 1]. The label would be a view, since nothing is decided in re-expressing a decided chord, and it would serve the pivot's theoretical claim [THEORY — the pivot-chord modulation of standard textbooks; no source fetched]. The charter fixes what L3 publishes [RULED — charter, L3 "Publishes"]. A derivation that adds an output decides L3's *what*, which the brief reserves. Exemplars 1 and 2 show the case: one analyst writes the pivot (`N6 F: IV6`) and the other writes the change at the same chord with no pivot (`IV.IV6`) [FACT at the files]. So the label is an analyst's choice of description, and L2's rivals already carry its musical content."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_13_l3_application_release_statement_texts_second_sitting.md, Ruling 13)
- *Source class.* Given — IC-L2 (the carried question) and the charter (the chord symbol, a view, at L3). Ruled — OQ-L3-8, the
  pivot-label record's Ruling 1 (the label as a view). Derived — the reach of D-100 and D-295 to a view, as the record
  states it. (was: "Given — charter (the list) and IC-L2 (the carried question). Derived (the reading of the label as a view)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_13_l3_application_release_statement_texts_second_sitting.md, Ruling 13)
- *Status.* Ruled — OQ-L3-8 ANSWERED (pivot-label record, Ruling 1); body and falsifier ratified (cowork_rulings_2026_11_13_l3_application_release_statement_texts_sitting.md, Ruling 12); Defense and Source class ratified (cowork_rulings_2026_11_13_l3_application_release_statement_texts_second_sitting.md, Ruling 13). (was: "**Open** (OQ-L3-8 ★)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md, Ruling 1; staleness fix shown, records/cowork/rulings/cowork_rulings_2026_11_13_l3_application_release_statement_texts_second_sitting.md)
- *Premise.* L2's rivals carry the pivot's content. **False-negative path:** a consumer that needs
  *both at once* as one fact. L2-S19 records that the masses of the two rivals express "either", not
  "both". That consumer is served by the label the pivot-label record's Ruling 1 places. (was: "That consumer is unserved until the ruling."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md, Ruling 1; staleness fix shown, records/cowork/rulings/cowork_rulings_2026_11_13_l3_application_release_statement_texts_second_sitting.md)
- *Falsifier.* CODE. **Observable:** L3's output schema, and the pivot-label outputs at each change of tonality in L2's principal
  reading and in each rival whole reading L2 publishes. **Decision rule:** falsified if any L3 output changes the
  tonality L2 decided for a span, or publishes a second tonality as decided for a span; if a re-expressed degree is not
  the decided chord of its span re-expressed in the other tonality; if a diatonic-in-both flag misstates whether that
  chord is diatonic in both tonalities; if any chord is named "the pivot"; or if a pivot label is published where the
  reading it belongs to has no change of tonality. **Not falsified by:** the re-expression of each side's decided chord as
  a scale degree in the other tonality, with its flag — the record's purpose, *"the re-expression is allowed while a
  second tonality decided for a span is barred"*; nor by the two rival chord symbols, which are identical for a true
  common-chord pivot (L3-S6). (was: "CODE until ruled. **Observable:** L3's output schema. **Decision rule:** falsified if L3 publishes a field carrying two tonalities for one span. **Not falsified by:** the two rival chord symbols, which are identical for a true common-chord pivot (L3-S6)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_13_l3_application_release_statement_texts_sitting.md, Ruling 12)

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md, Ruling 1).* Stands as derived.
  > **L3 decides where phrases end as a weighed choice. Every change point and both edges of the working span are candidate phrase ends; the principal partition is published with its rivals and their mass; no item of evidence forces or forbids a phrase end; an absent flag is never read as an absent phrase end.** The re-homed primitive's strength profile and the notated markers stay, as evidence entering as fitted terms (L3-S9 (i)), not as rules.
- *Beside L3-S8 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md, Ruling 1).*
  > **What this supersedes, stated exactly:**
  > - **D-478**, at its L3 home, as a rule deciding a phrase end — the rule Ruling 48 kept on purpose. The profile's peak survives only as evidence.
  > - **D-481**, at its L3 home: no marker is a phrase end unconditionally.
  > - **D-477** survives only in the narrower reading, as a rule on the cue evidence computed from the written page, and not on the L3 decision, which uses cadential evidence (L3-S9 (ii)) [this side's reading, put to the user on the surface].

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
  (relayed, 08) — Hamanaka et al. 2013, p. 210]. L1 publishes it as a restatement relation over the notes, which the phrase-end evidence may read (OQ-L3-5
  ANSWERED — thematic-parallelism record, Ruling 1). (was: "No layer beneath publishes it (OQ-L3-5)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1; staleness fix shown, ratification_surfaces/cowork_l3_application_release_edit_order_2026_11_14.md)
- *Falsifier.* CODE. **Observable:** the inputs of the phrase model's terms. **Decision rule:**
  falsified if any term reads a quantity not published by L0, L1 or L2; if the cadential-progression
  term at p reads a phrase end; or if a slur or dynamic enters a fitted term before a held-out
  measurement admits it. **Not falsified by:** a fitted weight near zero on any family.
- *Beside L3-S9 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 2).*
  > **c.** Rows 36.74 (i) and 36.146 — the phrase-length term (L3-S9 family (iii)) is in the model from the start as a fitted weight; the old text's own words *"they raise accuracy"* are the reason to suspect a gain (the 2026-10-07 ruling); its costs answered by L3-S14 and #20 and, on this side's reading, by Ruling 1's whole-span decision. Metric parallelism goes with item k. Algorithm: changes against the old documents, which deferred it.
- *Beside L3-S9 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 2).*
  > **d.** Row 40.24 (iii) — accelerating harmonic rhythm before a candidate position, read from L2's published boundaries, enters as a candidate term admitted only if a held-out measurement repays it (as L3-S9 (iv)); this side's reading of the 2026-10-07 ruling. Algorithm: changes (one candidate term added).
- *Beside L3-S9 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 2).*
  > **e.** Row 37.46 — no conflict of substance with L3-S9: reading per-voice surface cues as phrase evidence is not modelling voice leading, which the framework gives its own axis. Documentation only.
- *Beside L3-S9 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 2).*
  > **h.** Rows 8.45 (ii), 57.259 — the notated evidence and its scope stay at L1 (relayed through L3-S9 (i)); L3 does not copy them onto its units (#6); on this side's reading D-485 loses its subject at L3 under Ruling 1. Documentation only.
- *Beside L3-S9 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1).*
  > L3-S9's phrase-end evidence (premise at lines 394–397) may read it

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
- *Beside L3-S10 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 2).*
  > Row 8.84 (i) and §9 point 2 — the cadential arrival (L3-S10) is not held to a fixed window; the window's stated purpose (*"for example a suspended resolution"*) is met by L2 merging elaborations into the span they decorate (L2-S14, relayed); a fixed limit would cut off a prolonged half cadence such as exemplar 1 bars 11–12 (relayed); the charter aligns the cadence to the phrase boundaries and Ruling 2's rewording keeps that direction. The fate of a cadence at no phrase end (D-455) goes to the cadence family. Algorithm: changes against the old text.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 2).* Stands as derived.
  > L3-S11 and L3-S13 have no DIFFERS rows and stand as derived until ratified with their statements.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 1).* Stands as derived.
  > **The phrase reading tiles the working span with two kinds of unit — phrases, and the stretches between phrases (a post-cadential codetta, an introduction before the first phrase) — and each unit carries which kind it is.**
- *Beside L3-S12 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 1).*
  > **What this supersedes, stated exactly:** **D-458**, at its L3 home — the codetta is a unit of its own, not an annexe field. **UNSETTLED:** whether D-458 was among the decisions re-homed to L3 by Ruling 48 of the L0/L1 comparison (that record not read); the supersession is for the application act and the register route to carry either way.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_units_sitting.md, Ruling 2).* Stands as derived.
  > L3-S11 and L3-S13 have no DIFFERS rows and stand as derived until ratified with their statements.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md, Ruling 1).* Stands as derived.
  > **The statements, as ratified (the derivation's wording, unchanged; …):**
- *Beside L3-S14 (records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md, Ruling 1).*
  > **Not decided by this ruling, carried:**
  > - The observation of the first cut's §5: the amended second sentence of L2-S38 (L2 fit Ruling 1) no longer contains *"on held-out folds, with its capacity budget declared in advance"*. Principle #20 binds L2 directly. Left for the application act or a later L2 coherence pass.
  > - Whether L3's weights are fitted to the graded measure, as L2's now are (the first cut's §1, L3-S14). L3-S14 does not say; not raised.
  > - OQ-L3-11 (L3-S14's fit) is a measurement, not a ruling; OQ-L3-12 is the measurement stage's.
  > - Claims of the same rows graded against other statements, or where the derivation is silent (among them the UNPLACED claims against L3-S8 and L3-S22 that the third cut's §2 names), are not placed by this ruling.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 1).* Stands as derived.
  > **L3 publishes a cadence only where some phrase reading — the principal or a rival — ends a phrase, at most one per phrase end, an elided one included. A cadence-like pattern at any other position is published as evidence named for the pattern, never as a cadence, with its establishment status.**
- *Beside L3-S15 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 1).*
  > **What this supersedes, stated exactly:** **D-455**, at L3, in that an off-phrase-end pattern is no longer published as an "internal cadence". Its substance — never moved to a boundary, never discarded — survives: the pattern stays published as evidence. **UNSETTLED:** whether D-455 was re-homed to L3 by Ruling 48 of the L0/L1 comparison (that record not read); the supersession is for the application act and the register route to carry either way.
- *Beside L3-S15 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 2).*
  > **a.** Rows 8.11 (ii), 8.59 (ii), 8.101 (ii), 9.89 (iii), 37.31 (i) — the cadence is L3's, read off L2's decided chords at L3's decided phrase ends, not detected by the old function layer and read by the grouping layer; follows from the charter. Algorithm: changes against the old documents, decided by the charter.
- *Beside L3-S15 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 2).*
  > **b.** Row 40.64 — evidence-class facts are published without a named consumer, each with its establishment status (`CLAUDE.md`, the fact-publication corollary's amendment of 2026-07-12); and the pattern evidence has a consumer in any case, L3's phrase decision (L3-S9 (ii)). Documentation only.
- *Beside L3-S15 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 2).*
  > **d.** The cadence side of Rows 36.6, 36.12, 36.133 (their (i) halves AGREE with L3-S15), 36.14 (iii), 36.58 (i) — the cadence is read at L3's decided phrase ends, not at a gate fed by peaks picked from the page; follows from the morning's Ruling 1 and the charter. Algorithm: nothing beyond Ruling 1.
- *Beside L3-S15 (records/cowork/rulings/cowork_rulings_2026_11_02_l3_cadence_placement_sitting.md, Ruling 2).*
  > **e.** Rows 2.15, 2.18, 7.336, 57.502 (i) — D-495 (the flat-profile fallback) loses its subject at L3: under the morning's two rulings phrase ends are always decided over every candidate position and cadential evidence enters at each, so the starvation it describes cannot arise in the same form; the votes it weighted are a cadence's votes on the key (D-336, index title), which L3 cannot cast (charter: *"it may not revise L2"*; L3-S38, quoted at the reading file). This side's reading. Algorithm: the old fallback rule drops out; no new mechanism.

**L3-S16. The cadence is published as its defining features, each a view of a lower layer's fact:**
(1) the arrival position (L3-S10) and its metric strength class (IC-L1 S-35); (2) the chords of the
progression's last spans, normally the final, the penultimate and, where present, the pre-dominant
span, each with L2's four fields, in the arrival span's tonality, with the chord symbols of L3-S1;
(3) the relation of the arrival's tonality to the tonality before the phrase (the same, or a change, by
degree); (4) the suspensions and appoggiaturas sounding at the arrival or on the penultimate chord, as
L2 assigns them (a 4–3 over the dominant, for example); (5) whether the phrase end is elided (L3-S11);
(6) **the scale degree of the highest sounding pitch at the arrival, read off the highest sounding pitch per slice that L1 publishes (OQ-L3-4 ANSWERED — cadence-features
record, Ruling 2).** (was: "which carries a named reason ("not computable: no layer beneath publishes it") until OQ-L3-4 is ruled."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 2; staleness fix shown, ratification_surfaces/cowork_l3_application_release_edit_order_2026_11_14.md)
- *Defense.* These are what the textbook categories are defined by: the degrees and inversions of the
  last chords, the soprano's degree at the arrival, and the tonal context [THEORY — standard harmony and
  form theory; no source fetched]. Published detectors and models read the same things. Their features
  describe the arrival Z, the chord before it Y and the preparation X [FACT (relayed, 08) — Bigo et
  al. 2018, §2]. A model of cadence choice encodes key area, cadence type and the chord member of the
  soprano at the arrival as one token [FACT (relayed, 08) — de Clercq, p. 194]. The global key there
  matters less than the local key implications [FACT (relayed, 08) — de Clercq, p. 195]. Feature (4)
  comes from L2's assignments: exemplar 3 writes `V(4)` then `V` at its cadences [FACT at the file],
  and the cadential suspension is part of what an analyst writes. Feature (6) needs the highest
  sounding pitch. L1 publishes the lowest sounding pitch per slice (IC-L1 S-50) and, per slice, the highest sounding pitch of its sounding set (OQ-L3-4 ANSWERED — cadence-features record, Ruling 2),
  and S-50 is exhaustive: *"an absence in an L1 publication means not there"* [RULED — IC-L1 beside
  S-50, Ruling 60]. Computing it from the sounding set here would supply a notated fact that, by
  IC-L1's own test, is an L1-kind fact (computable from L0 with no tonality, chord or boundary as
  input) [RULED — IC-L1 S-51]. The brief forbids filling it [RULED — brief §3.1]. Feature (6) is read off that publication. (was: "and no highest one"; "The want is OQ-L3-4."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 2; staleness fix shown, ratification_surfaces/cowork_l3_application_release_edit_order_2026_11_14.md)
- *Source class.* Derived. Each feature's content is given by the layer that publishes it.
- *Status.* Settled for (1) to (6) (for (6): OQ-L3-4 ANSWERED — cadence-features record, Ruling 2). (was: "Settled for (1) to (5). **Open** for (6) (OQ-L3-4)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 2; staleness fix shown, ratification_surfaces/cowork_l3_application_release_edit_order_2026_11_14.md)
- *Premise.* These features determine every type of L3-S17. **False-negative path:** the evaded
  cadence, defined by what the following music does instead of arriving [THEORY — Caplin's typology;
  no source fetched]. Its features include the next phrase's opening, which (2) to (5) partly hold and
  thematic parallelism would complete (OQ-L3-5).
- *Falsifier.* CODE. **Observable:** published cadences. **Decision rule:** falsified if any feature
  differs from the lower layer's fact it is read off, or if feature (6) carries a value while no layer
  beneath publishes the highest sounding pitch. **Not falsified by:** a feature carrying a named reason.
- *Beside L3-S16 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1).*
  > **a. Group 1 — the cadence is read in the tonality L2 decided.** Rows 2.4, 7.52, 7.120, 7.229, 7.294(ii), 20.46(ii) **RELOCATED** to *L1 — Change points, candidates and notated evidence* (the key-agnostic cues); Rows 7.98 and 20.48 **RELOCATED** to *L2 — The tonal reading. The one entangled decision.* (the aggregation into the tonality), as the reading file proposes. Follows from DP-I, the charter's L3 sentences, and items a and e of the 2026-11-02 cadence-placement Ruling 2. D-336's circularity does not arise at L3: the tonality is settled before L3 reads and L3 sends nothing back. D-336 and D-081 are superseded **at L3 only**; the key-agnostic cue survives at L1. **Documentation only** at L3; the algorithm change (cadence read in the decided tonality) was already decided by the charter and item a. *Not examined:* D-336's further claim that the old key-dependent detector conflated perfect and imperfect.
- *Beside L3-S16 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1).*
  > **b. Group 2 — the highest sounding pitch's degree at the arrival is published as a feature of the cadence**, under that name and never as *soprano* or *melody*, carrying "not computable: no layer beneath publishes it" until a lower layer publishes the pitch. Rows 2.7(ii), 2.8, 7.1(ii), 7.31(i), 7.101(ii), 7.105, 7.107(i), 7.301(ii), 8.40(ii), 36.36(i), 36.130(i) recorded as decided against **in so far as they keep the fact unpublished**. Supersedes D-584's "soft optional nudge" in that respect only. **NOT decided:** whether the perfect/imperfect call ever rests on this feature — that is L3-S17's question (with OQ-L3-2 ★), where D-584's ground carries its full weight. **Algorithmic:** one published feature added; the call itself untouched.
- *Beside L3-S16 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1).*
  > **c. Rows 2.7(iii) and 7.108 ADOPTED:** L3 never attempts to identify a structural melody among the voices. Ground: D-584's own words and Row 7.108's *"a hard, partly-perceptual problem deliberately out of scope"*. **Documentation only.**
- *Beside L3-S16 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1).*
  > **The D-599 test of the six 2026-11-02 rulings, for L3-S16 (entry 484 §2 item 2), recorded as derivation, ratified with Ruling 1:** feature (1) is at a phrase end L3 has decided (phrase-ends Ruling 1; cadence-placement Ruling 1); feature (5) rests on the same decided end; feature (2) reads L2's decided chords (cadence-placement Ruling 2 item a); a cadence at a rival phrase reading's end is published as cadence-placement Ruling 1 says; nothing in the six touches feature (4). Documentation only.
- *Beside L3-S16 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1).*
  > **Carried, UNSETTLED (not decided by this ruling):**
  > - Feature (3)'s wording: "the tonality before the phrase" may mean the end of the preceding unit (now possibly a codetta or introduction, phrase-units Ruling 1) or the phrase's own opening, which can differ (phrase-units Ruling 2 item g). For the application act to bring back to the user.
  > - Whether a cadence's chords also carry L2's rival chord readings; L3-S16 says *"with L2's four fields"* and no ruling read settles principal-only.
  > - Whether `FRAMEWORK.md`'s charter is later than D-336's dates (2026-06-26; 2026-08-02) and D-584's (2026-06-26; 2026-08-04).

**L3-S17. The cadence type is a view of the defining features under a declared vocabulary. No cadence vocabulary is principal at L3 (OQ-L3-2 ANSWERED — cadence-type record,
Ruling 2).** (was: "Which vocabulary is principal is not decided here (OQ-L3-2 ★)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 2; staleness fix shown, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_third_sitting.md) **Every type of the declared vocabularies is a
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
- *Status.* Settled in form. No vocabulary is principal (OQ-L3-2 ANSWERED — cadence-type record, Ruling 2). Feature (6) becomes computable once L1 publishes the highest sounding pitch per slice (OQ-L3-4 ANSWERED — cadence-features record, Ruling 2). Each declared vocabulary publishes its perfect/imperfect split as two separately named views: (i) on the bass-derived inversion alone; (ii) on the bass-derived inversion plus feature (6). View (ii) carries *not yet validated*, and no consumer may put it under load until a measurement establishes it (cadence-type record, Ruling 1). The split is computable wherever its features carry values; *type not computable* only where a feature is missing (cadence-type record, Ruling 3 item b). (was: "Settled in form. **Open** on the principal vocabulary (OQ-L3-2 ★). Feature (6) blocks the PAC/IAC split in every vocabulary until OQ-L3-4 is ruled."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Rulings 2 and 3 item b; staleness fix shown, its second sentence; text ratified, its sentences from "Feature (6)" on, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_third_sitting.md, Ruling 14)
- *Premise.* Each vocabulary's types are functions of chords, degrees, the scale degree of the highest sounding pitch at the arrival (feature (6) of L3-S16) and the context. (was: "Each vocabulary's types are functions of chords, degrees, the soprano and the context."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 1 items b and c; staleness fix shown, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_third_sitting.md)
  **False-negative path:** a type whose definition needs something none of the features holds, such as
  the evaded cadence's expectation (L3-S16's premise), or a half cadence that Caplin distinguishes from
  a mere dominant arrival by the presence of a cadential progression before it [THEORY — Caplin 1998; no
  source fetched]. Feature (2)'s pre-dominant span holds the latter. The former stays a named reason.
- *Falsifier.* CODE. **Observable:** the type against the features. **Decision rule:** falsified if
  two cadences with identical features receive different types under one vocabulary, or if a type
  depends on anything but the features. **Not falsified by:** two vocabularies giving different types
  for one cadence.
- *Beside L3-S17 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 1).*
  > **Each declared cadence vocabulary publishes its perfect/imperfect split as two separately named views: (i) on the bass-derived inversion alone, as D-584 has it; (ii) on the bass-derived inversion plus the scale degree of the highest sounding pitch at the arrival (feature (6) of L3-S16). View (ii) carries the establishment status *not yet validated*, and no consumer may put it under load until a measurement establishes it** (#19; the fact-publication corollary's amendment of 2026-07-12).
  >
  > - **NOT decided:** the principal vocabulary (Decision 2, OQ-L3-2); any vocabulary's definition of perfect or imperfect (written from sources actually read, surface §A.5); Row 2.9's confidence half (*"the top voice may nudge the confidence"*), which goes with L3-S19.
- *Beside L3-S17 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).*
  > **a.** The type is L3's, read off L2's decided chords: Rows 8.88 (i) and 38.26 (i) recorded as decided against; Row 7.99 **RELOCATED** to *L2 — The tonal reading. The one entangled decision.*; Row 28.47 **QUARANTINED** for the audit. Ground: the charter's *"A cadence type is a claim about what the decided chords do at a decided phrase end"*; item a (and item c for 28.47) of the 2026-11-02 cadence-placement Ruling 2.
- *Beside L3-S17 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).*
  > **b.** Row 7.104: the perfect/imperfect split is computable wherever its features carry values; *type not computable* only where a feature is missing. L3-S17's status sentence on feature (6) is overtaken; its correction is the application act's.
- *Beside L3-S17 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).*
  > **c.** Row 7.115 (i): the evaded cadence published as *type not computable* with its reason until OQ-L3-5.
- *Beside L3-S17 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).*
  > **d.** Rows 8.37 (i) and 8.38 (i): follow from Ruling 1c of the 2026-11-03 cadence-features record.
- *Beside L3-S17 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 3).*
  > **e.** Rows 7.109, 7.110 (i), 7.111, 7.113, 7.114 (i) and 7.97 (i) **ADOPTED — proposed** as types or rules of the declared vocabularies; each wording written from its source when that vocabulary is declared.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md, Ruling 1).* Stands as derived.
  > **Algorithmic (decided against the older documents):** a cadence's mass comes only from the doubt already carried — L2's rival objects and ranked whole readings, and L3's rival phrase ends — never from a product of per-span marginals; mass L2 does not publish is carried as unaccounted. **No cadence type carries a fixed, by-rule lowering of its confidence, and the top note does not nudge the mass.**
- *Beside L3-S19 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md, Ruling 1).*
  > L2's publication that L3-S19 reads (rival objects, ranked whole readings to a bound, the withheld mass per span) is ruled at Ruling 1 of `cowork_rulings_2026_10_05_l2_rival_publication_sitting.md`.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1).* Stands as derived.
  > **Algorithmic (decided against the older documents only):** L3 reads the cadence under each of L2's two readings as published, and never converts one into the other or collapses the six-four and the dominant into one dominant approach; where the readings differ in arrival position or in the chord before the dominant, the cadences are published as rivals with their mass. Nothing currently ratified is changed: this follows from Ruling 1 of the L2 cadential six-four record and from Ruling 1 of `cowork_rulings_2026_11_03_l3_cadence_mass_sitting.md` (L3-S19).
- *Beside L3-S20 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadential_six_four_sitting.md, Ruling 1).*
  > **Carried, UNSETTLED (not decided by this ruling):** that the type comes out the same under both readings is the derivation's own CONJECTURE; its false-negative path (an analyst under `I6/4` placing the half-cadential arrival at bar 11's first dominant, carried by L3's rival at bar 11) stands as written.

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
- *Beside L3-S22 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 1).*
  > **As ratified:** (1) sections are decided at L3, as the charter says; on this point the charter overtakes D-454 and D-456 [a derivation on the shape the phrase-ends record used — *"overtaken by the charter … a consequence recorded under D-599"* — not a ruling written about these two decisions before today]; (2) a section boundary is always a phrase boundary, phrases and sections read as one consistent grouping (L3-S22; the derivation's §7 point 6; rows 57.352 and 19.39(iii) agree); (3) the evidence for a section boundary is L3-S23's four families, each a weighed term, and no single item forces or forbids a section boundary — the phrase-ends Rulings 1 and 2 extended from phrases to sections, this side's reading, now ratified; (4) family (iv) reads the restatement relation L1 publishes, its weight measured, UNESTABLISHED until then. **Whether sections may contain sections is NOT part of this ruling** (Decision 1).
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 2).* Stands as derived.
  > sections may contain sections to any depth, each level tiling the level above, the top level covering the working span; a one-level reading stays reachable; how many levels a passage has is left to the evidence and the measured weights, UNESTABLISHED until measured.

**L3-S23. The evidence bearing on a section boundary falls into four families, each entering as fitted
terms.** (i) **Notated section evidence** from L1: REPEAT flags and the junction adjacencies, final and
double bar lines, key- and time-signature changes, tempo changes, and section labels or rehearsal
letters in the marks list. (ii) **Cadential evidence** from L3's own cadences: the type of the cadence
closing the preceding phrase and its tonality relation (L3-S16 (3)). (iii) **Tonal evidence** from L2:
where the tonality changes and how far, across the candidate boundary. (iv) **Thematic return**, the
restatement of earlier material. It reads the restatement relation L1 publishes (OQ-L3-5 ANSWERED — thematic-parallelism record, Ruling 1), its
weight measured, UNESTABLISHED until then (sections record, Ruling 1 item (4)). (was: "No layer beneath publishes it, and it is written as OQ-L3-5 and not filled."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1; records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_fourth_sitting.md, Ruling 15)
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
  second home. It was the want OQ-L3-5, now answered: L1 publishes it (thematic-parallelism record, Ruling 1). (was: "It is the want OQ-L3-5."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1; staleness fix shown, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_fourth_sitting.md)
- *Source class.* Given — IC-L1 (what (i) contains). Derived (the four families). *Measured* (the
  weights), UNESTABLISHED.
- *Status.* Settled in shape. **Open** on the weights (OQ-L3-11). Family (iv) reads the restatement relation L1 publishes (OQ-L3-5 ANSWERED — thematic-parallelism record, Ruling 1); how that relation extends across several voices is carried UNSETTLED by the same record. (was: "Settled in shape. **Open** on the weights (OQ-L3-11) and on (iv) (OQ-L3-5)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1; records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 1; staleness fix shown, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_fourth_sitting.md)
- *Premise.* Families (i) to (iii) carry enough to rank section boundaries until (iv) is published.
  **False-negative path:** a recapitulation in the subdominant with no notated mark, exemplar 1's own
  case. Without (iv) it is found only through the cadence and the key change, and may carry low mass.
- *Falsifier.* CODE. **Observable:** the section model's inputs. **Decision rule:** falsified if any term
  reads a quantity no layer beneath or L3 itself publishes, in particular a melodic-repetition relation
  computed at L3. **Not falsified by:** weights near zero.
- *Beside L3-S23 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1).*
  > L3-S23's family (iv), *thematic return*, changes from *"not filled"* to reading the published relation; L3-S9's phrase-end evidence (premise at lines 394–397) may read it; L3-S42's premise (lines 1186–1188) is answered — the relation is published by L1, not the axis. The weights stay measured and UNESTABLISHED (OQ-L3-11). L3's bar on computing the relation itself stands as written.
- *Beside L3-S23 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 1).*
  > **As ratified:** (1) sections are decided at L3, as the charter says; on this point the charter overtakes D-454 and D-456 [a derivation on the shape the phrase-ends record used — *"overtaken by the charter … a consequence recorded under D-599"* — not a ruling written about these two decisions before today]; (2) a section boundary is always a phrase boundary, phrases and sections read as one consistent grouping (L3-S22; the derivation's §7 point 6; rows 57.352 and 19.39(iii) agree); (3) the evidence for a section boundary is L3-S23's four families, each a weighed term, and no single item forces or forbids a section boundary — the phrase-ends Rulings 1 and 2 extended from phrases to sections, this side's reading, now ratified; (4) family (iv) reads the restatement relation L1 publishes, its weight measured, UNESTABLISHED until then. **Whether sections may contain sections is NOT part of this ruling** (Decision 1).

**L3-S24. L3 publishes the grouping (boundaries, nesting and rivals) and, for each section at every level of the
nesting, a form-function name where the chosen naming scheme has one (such as *exposition*, *second theme*,
*development* or *recapitulation*), "no name" being a possible reading. Each name is published with its rival names
and their mass, carrying its establishment status — UNESTABLISHED until measured against a ground truth (OQ-L3-6
ANSWERED — sections record, Ruling 3).** (was: "L3 publishes the grouping (boundaries, nesting and rivals) and not form-function names such as *exposition*, *second theme*, *development* or *recapitulation*. Naming the sections' formal functions is not on L3's charter list (OQ-L3-6 ★)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_fifth_sitting.md, Ruling 16)
- *Defense.* The charter lists *"the phrase and section grouping"* [RULED — charter, L3 "Publishes"],
  and adding an output is a ruling on L3's *what*, which the brief reserves [RULED — brief §0, "never
  WHAT it does"]. Exemplar 2 writes such names [FACT at the file], so analysts do publish them, and
  the want is real. A form-function name is a theoretical claim on top of the grouping, and theories of
  form differ [THEORY — standard form theory; no source fetched]. Exemplar 1's phrase at bar 13 against
  exemplar 2's *second theme* at bar 14 (L3-S13) shows that a name can move a boundary in an
  analyst's reading. The user ruled that L3 works out form-function names and publishes them (sections record, Ruling 3), on D-295 and on
  D-100 (its application to L3 this side's reading, as the record says): a name L3 works out is published; the
  differing theories are met by rival names with their mass, their establishment status and the verifiability
  contract, and the bar 13 / bar 14 case is a possibility, not load-bearing, until measured. (added; records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_fifth_sitting.md, Ruling 16)
- *Source class.* Given — charter (the grouping; the form-function names, which the charter's *Publishes* list gains by the sections
  record, Ruling 3). *Measured* (the weighing of a section's rival names, which rests on a fit not yet made),
  UNESTABLISHED. (was: "Given — charter."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_fifth_sitting.md, Ruling 16)
- *Status.* Settled in shape (OQ-L3-6 ANSWERED — sections record, Ruling 3). **Open** on the naming scheme, on what evidence the
  names read, and on whether names ever feed back into the section decision (the same ruling, *Not decided by this
  ruling*). (was: "**Open** (OQ-L3-6 ★)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_fifth_sitting.md, Ruling 16)
- *Premise.* The section grouping is decided without reading the names. **False-negative path:** a boundary an analyst may place
  because of a name (possibly exemplar 2's *second theme* at bar 14 against exemplar 1's phrase beginning at bar 13,
  L3-S13, which leaves to L3-S23 whether the two are the same kind of boundary). Such a boundary is reached only through
  L3-S23's four families until a measurement shows that names should feed back. (was: "The grouping is useful without names. **False-negative path:** a consumer that needs the names. It is unserved until the ruling."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_fifth_sitting.md, Ruling 16)
- *Falsifier.* CODE. **Observable:** L3's output schema. **Decision rule:** falsified if the schema has no place for a section's
  form-function name reading ("no name" included); if a form-function name is published without its rival names and
  their mass, or without its establishment status; or if a name carries a status other than UNESTABLISHED before it is
  measured against a ground truth. **Not falsified by:** "no name" as a reading; a section carrying the text of a
  notated section label, which is an L1 mark referenced by identity. (was: "CODE until ruled. **Observable:** L3's output schema. **Decision rule:** falsified if a section carries a form-function name. **Not falsified by:** a section carrying the text of a notated section label, which is an L1 mark referenced by identity."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_fifth_sitting.md, Ruling 16)
- *Beside L3-S24 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3).*
  > **Not decided by this ruling:** which naming scheme (sonata-form labels, Caplin's theme types, or both); what evidence the names read (key areas are the next family, entry 481 §2 item 4; thematic return; cadences); whether names ever feed back into the section decision (a measurement first, under the 2026-10-07 Ruling 6). Row 41.63's quartet set: whether it is held now and whether its labels name formal functions stays UNSETTLED [relayed from §3 (1); Row 41.63 not read by the sitting that put this ruling].

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
  that a continuo player would figure on its own. That grain is served by the second figured bass of L3-S28, read off the spelled intervals above the lowest
  sounding pitch that L1 publishes at every slice (OQ-L3-7 ANSWERED — figured-bass record, Ruling 1). (was: "That grain needs the spelled interval content above the lowest sounding pitch per slice, which no layer beneath publishes (L3-S28, OQ-L3-7)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1; staleness fix shown, ratification_surfaces/cowork_l3_application_release_edit_order_2026_11_14.md) In the bars
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
- *Recorded (records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, §2 (e)).* Stands as derived — recorded by the record as this side's derivation, not ruled; challengeable.
  > **(e) The span figure** (L3-S25 to L3-S27) rests on the charter's list, L2-S28's definition of the figure and the method stated with the 2026-10-08 Ruling 1; no question raised on it.

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
- *Recorded (records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, §2 (e)).* Stands as derived — recorded by the record as this side's derivation, not ruled; challengeable.
  > **(e) The span figure** (L3-S25 to L3-S27) rests on the charter's list, L2-S28's definition of the figure and the method stated with the 2026-10-08 Ruling 1; no question raised on it.

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
- *Recorded (records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, §2 (e)).* Stands as derived — recorded by the record as this side's derivation, not ruled; challengeable.
  > **(e) The span figure** (L3-S25 to L3-S27) rests on the charter's list, L2-S28's definition of the figure and the method stated with the 2026-10-08 Ruling 1; no question raised on it.

**L3-S28. L3 publishes a second figured bass, at the continuo grain, named apart from the span figure of L3-S25.
Under every bass note, passing bass notes included, it gives what actually sounds above it. It is read off the
spelled intervals above the lowest sounding pitch that L1 publishes at every slice, and written by L3-S26's
accidental rule and L3-S27's full-figure rule. L3 does not compute that interval content itself. The span figure of
L3-S25 is unchanged (OQ-L3-7 ANSWERED — figured-bass record, Ruling 1).** (was: "A figured bass at the continuo grain, where every bass note including passing bass notes is figured by the sonority actually sounding above it, needs the spelled interval content above the lowest sounding pitch at every slice. No layer beneath publishes it. L3 does not compute it, and the want is OQ-L3-7, naming IC-L1 S-49 and S-50."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_sixth_sitting.md, Ruling 17)
- *Defense.* IC-L1 publishes the interval content above the lowest sounding pitch only at the two
  slices of a cue, Y and Z, as unspelled semitone distances [RULED — IC-L1 S-49], and the lowest
  sounding pitch at every slice [RULED — IC-L1 S-50]. S-50 is exhaustive [RULED — IC-L1 beside S-50,
  Ruling 60]. The quantity wanted is S-49's quantity, spelled, at every slice. Computing it here would
  re-derive an L1-defined quantity. The input contract records exactly this shape for L2's want of the
  lowest sounding pitch per slice: L2 *"writes the want instead"*, and the ruling that answered it
  declined *"L2 computes the pitch itself — one named fact with two producers"* [RULED — L2-S28; OQ-L2-11
  answer]. No staged case of a figured passing bass note was met (L3-S25's premise; OQ-L3-14). The user ruled that L1 publishes, at every slice, the spelled intervals above its lowest sounding pitch, and that L3
  reads its continuo-grain figure off that publication (figured-bass record, Ruling 1, alternative B); L3 computing the
  intervals itself was declined (alternative C: one fact, two producers; D-100; the 2026-10-08 precedent). The one harm
  of B named, a reader mistaking the continuo figure for the harmony, is reduced by naming the two outputs apart; the
  continuo figure's use in comparison with composer figures is not shown. (added; records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_sixth_sitting.md, Ruling 17)
- *Source class.* Given — IC-L1 (the spelled intervals above the lowest sounding pitch at every slice, which IC-L1 gains by the
  figured-bass record, Ruling 1) and IC-L2 (the precedent). Derived (the continuo-grain figure written from them). (was: "Given — IC-L1 (what is published) and IC-L2 (the precedent). Derived (the want)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_sixth_sitting.md, Ruling 17)
- *Status.* Settled (OQ-L3-7 ANSWERED — figured-bass record, Ruling 1). The record gives the output no name beyond *"named apart
  from the span figure"*, and does not state whether a bass note held under moving upper voices carries one figure or
  one at each slice. No staged case of a figured passing bass note was met (OQ-L3-14, which the record carries as a
  measurement matter). (was: "**Open** (OQ-L3-7)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_sixth_sitting.md, Ruling 17)
- *Premise.* The continuo grain is part of what the charter's *figured bass* means. **False-negative path:** the charter means
  only the span figure. The second output is then an addition to L3's *Publishes* list, which the figured-bass record
  reads as not needed, since the list names *"the figured bass"* without a grain (the record's reading, not a ruling). (was: "The continuo grain is part of what the charter's *figured bass* means. **False-negative path:** the charter means only the span figure. L3-S25 then suffices and the want lapses. The question is put with OQ-L3-7."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_sixth_sitting.md, Ruling 17)
- *Falsifier.* CODE. **Observable:** L3's figured bass inputs and outputs. **Decision rule:** falsified if L3 computes interval
  content over the sounding set itself; if a bass note, a passing bass note included, carries no continuo-grain figure;
  if a continuo-grain figure differs from the spelled intervals L1 publishes above the lowest sounding pitch, as written
  by L3-S26's and L3-S27's rules; if the two figured basses are published under one name; or if adding the
  continuo-grain output changes any span figure of L3-S25 (the same music analysed with and without it). **Not
  falsified by:** L3 computing an interval between two events that L2's facts name, such as a suspended event and the
  structural bass (L3-S25). (was: "CODE. **Observable:** L3's figured bass inputs. **Decision rule:** falsified if L3 computes interval content over the sounding set itself. **Not falsified by:** L3 computing an interval between two events that L2's facts name, such as a suspended event and the structural bass (L3-S25)."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1; text ratified, records/cowork/rulings/cowork_rulings_2026_11_14_l3_application_release_statement_texts_sixth_sitting.md, Ruling 17)

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
- *Beside L3-S30 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, Ruling 1).*
  > L3 publishes no separate grouping of L2's spans by root and quality. The coarse view is formed by a consumer from L3-S30's change classes (the changes marked root or quality changed), a view and not a re-derivation.
- *Recorded (records/cowork/rulings/cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, §2 (e)).* Stands as derived — recorded by the record as this side's derivation, not ruled; challengeable.
  > L3-S30 and L3-S31 stand as derived; §9 point 5 is answered by L3-S30.

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
- *Recorded (records/cowork/rulings/cowork_rulings_2026_11_03_l3_harmonic_rhythm_sitting.md, §2 (e)).* Stands as derived — recorded by the record as this side's derivation, not ruled; challengeable.
  > L3-S30 and L3-S31 stand as derived; §9 point 5 is answered by L3-S30.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* Stands as derived.
  > L3-S32, L3-S33, L3-S34 and L3-S36 as derived
- *Beside L3-S32 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).*
  > L3's mass and status rules as the five statements give them; against the older documents, the confidence contract's Class-M margins, max-normalised strengths and squashed composites are replaced, for L3, by the model's own distribution.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* Stands as derived.
  > L3-S32, L3-S33, L3-S34 and L3-S36 as derived

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* Stands as derived.
  > L3-S32, L3-S33, L3-S34 and L3-S36 as derived

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* Stands as derived.
  > L3-S35 as derived and in the form of Ruling 1 (both masses per rival), its principal the best L3 reading given L2's principal reading (charter line 532).
- *Beside L3-S35 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 1).*
  > every L3 rival of an L3 decision is published with both masses, under distinct names: its mass given L2's principal reading (the conditional) and its marginal mass over L2's published readings (the overall), with the unaccounted remainder published.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_mass_and_status_sitting.md, Ruling 2).* Stands as derived.
  > L3-S32, L3-S33, L3-S34 and L3-S36 as derived

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md, Ruling 2).* Stands as derived.
  > L3-S37 and L3-S39 as derived
- *Beside L3-S37 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md, Ruling 2).*
  > L3's input rules become part of its ratified specification as the two statements give them; no change against the currently decided method (the charter's consume line; mass-and-status Ruling 1; the OQ-L3-4, OQ-L3-5 and OQ-L3-7 rulings, which applied L3-S39's rule). No inference changes.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).* Stands as derived.
  > L3-S38 as derived
- *Beside L3-S38 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_s38_ratification_sitting.md, Ruling 1).*
  > L3-S38 becomes part of L3's ratified specification as its text gives it. **No change against the currently decided method**, which was stated with the question: L3 reads everything L2 publishes (its reading, its rivals with mass) plus L0's and L1's published facts, and nothing else (L3-S37, ratified); never revises L2; L2 reads nothing L3 publishes; a backward edge is tested by measurement as soon as there is reason to suspect it helps; key areas read off L2's principal reading, a new one at every change of tonality (key-areas Ruling 2). No inference changes.

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
- *Status.* Settled. The list is the list of wants this derivation found. Three are answered: OQ-L3-4 (cadence-features record, Ruling 2), OQ-L3-5 (thematic-parallelism record, Ruling 1) and OQ-L3-7 (figured-bass record, Ruling 1). OQ-L3-1 stays open, carried as an investigation (chord-symbol record, §2 (g)). (was: "Settled. The list is a list of wants, each open."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md, Ruling 2; staleness fix shown, ratification_surfaces/cowork_l3_application_release_statement_texts_surface_2026_11_13_part_7.md, under Ruling 7 of the second Part B ruling record)
- *Premise.* The list is complete. **False-negative path:** a want this session did not notice. The
  falsifier surfaces it.
- *Falsifier.* CODE. **Observable:** L3's inputs. **Decision rule:** falsified if L3 computes, from L0
  facts or from L1's sounding sets, any quantity of the kind IC-L1 S-51 assigns to L1, or any quantity
  IC-L1 or IC-L2 defines as a publication. **Not falsified by:** L3 computing an interval between two
  events that L2's facts name (L3-S25), or reading an L0 fact that no layer defines (L3-S26).
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_boundaries_sitting.md, Ruling 2).* Stands as derived.
  > L3-S37 and L3-S39 as derived

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
- *Status.* Settled. (was: "**Open** on whether L3 may request (OQ-L3-10 ★). Settled that edge-crossing units are marked."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1)
- *Premise.* L3's in-span publication converges within the cap for ordinary music. **False-negative
  path:** section readings that never settle short of the whole piece. They are then marked truncated
  at every selection smaller than the piece.
- *Falsifier.* CODE. **Observable:** L3's publication after successive enlargements. **Decision rule:**
  falsified if an edge-crossing unit lacks its mark, if L3 stops while its in-span publication still
  changes and the cap has not been reached, or if a cap stop is unmarked. **Not falsified by:** a marked
  stop at the cap or at the record's own edge.
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1).* Stands as derived.

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
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md, Ruling 1).* Stands as derived.
  > **The statements, as ratified (the derivation's wording, unchanged; …):**

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
  thematic parallelism, whose relation is published by L1, not the axis (OQ-L3-5 ANSWERED —
  thematic-parallelism record, Ruling 1); L3 reads it as L1's published fact. (was: "thematic parallelism (OQ-L3-5), which may be published by the axis rather than by L1. If it is, L3 reads it as a published fact under the charter's spine–axis row."; records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1; staleness fix shown, ratification_surfaces/cowork_l3_application_release_edit_order_2026_11_14.md)
- *Falsifier.* RESIDUAL — a modelling premise.
- *Beside L3-S42 (records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1).*
  > L3-S42's premise (lines 1186–1188) is answered — the relation is published by L1, not the axis.
- *Ruled (records/cowork/rulings/cowork_rulings_2026_11_04_l3_fit_and_rest_sitting.md, Ruling 1).* Stands as derived.
  > **The statements, as ratified (the derivation's wording, unchanged; …):**

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

  **ANSWERED (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_type_sitting.md, Ruling 2):**
  > **No cadence vocabulary is principal at L3. Every declared vocabulary's types are published side by side, each a view of L3-S16's features; which vocabulary a display shows first is a presentation setting, not an analysis decision.**
  >
  > - **NOT decided:** which vocabularies are declared, and each one's definitions (written from sources actually read, surface §A.5).
- **OQ-L3-3 ★ (face (b); L3-S8, L3-S11) — a phrase end with no notated cue.** *Question for the user:*
  the charter says *"the span's boundaries come from the notated cues, and the cadence is aligned to
  them"*. At an elided cadence such as exemplar 1 bar 42 or exemplar 3 bar 12 beat 3, the only notated
  cues are the bar line (bar 42) or nothing beyond the per-voice relations and the metric class (bar 12
  beat 3). May the cadential evidence place a phrase end there? L3-S8 makes every change point a
  candidate and lets the evidence decide. That is this session's reading, and it moves the charter's
  sentence from a rule about *where* boundaries may fall to a statement about *which evidence leads*.

  **ANSWERED (records/cowork/rulings/cowork_rulings_2026_11_02_l3_phrase_ends_sitting.md, Ruling 2):**
  > **A phrase end may fall wherever the evidence as a whole puts it, including at a cadence with no notated cue** (the derivation's cases: exemplar 1 bar 42 and exemplar 3 bar 12 beat 3, relayed).
- **OQ-L3-4 (faces (c), (h); L3-S16) — the highest sounding pitch per slice.** The PAC/IAC split in
  every vocabulary needs the soprano's degree at the arrival. L1 publishes the lowest sounding pitch per
  slice and no highest one (IC-L1 S-50, exhaustive). *The input-contract statement concerned:* IC-L1
  S-50 (with S-44's naming and S-51's test). Would S-50's list gain *per slice, the highest sounding
  pitch of its sounding set*, published under that name with its witness? Until then feature (6)
  carries a named reason.

  **ANSWERED (records/cowork/rulings/cowork_rulings_2026_11_03_l3_cadence_features_sitting.md, Ruling 2):**
  > **IC-L1 S-50's list gains *"per slice, the highest sounding pitch of its sounding set"*, published under that name.**
  >
  > **NOT decided:** whether any cadence type reads the pitch (L3-S17, OQ-L3-2 ★; D-584's ground — doubling, a lead below the top — carries its full weight there).
- **OQ-L3-5 (faces (b), (d), (h); L3-S9, L3-S23, L3-S42) — thematic parallelism.** Section reading,
  the evaded cadence, and some phrase ends need a relation saying that a stretch restates an earlier
  one, transposed or not. No layer beneath publishes it. By IC-L1 S-51's test it is an L1-kind item.
  It may instead belong to the voice-leading axis. *The input-contract statements concerned:* IC-L1
  S-50 and S-51, or the charter's spine–axis row. Which layer publishes it, and in what form?

  **ANSWERED (records/cowork/rulings/cowork_rulings_2026_11_03_l3_thematic_parallelism_sitting.md, Ruling 1):**
  > OQ-L3-5 RATIFIED: L1 publishes a restatement relation over the notes; its similarity measure is measured; L3 reads it
  >
  > **The derivation, as ratified:**
  > 1. *Not computed at L3.* Already settled: L3-S39 (*"L3 never re-derives a fact a layer beneath it publishes, and never supplies a fact of a lower layer's kind by computing it from the notation"*) and L3-S23's falsifier (*"falsified if any term reads a quantity no layer beneath or L3 itself publishes, in particular a melodic-repetition relation computed at L3"*).
  > 2. *It passes S-51's test for an L1 output:* both methods read at source compute it from note facts (onsets, durations, pitches; beat positions in the 2007 paper, relayed) with no tonality, chord or boundary as input — for one melodic line.
  > 3. *What L1 publishes, and what it does not:* S-50's naming rule bars a field named *boundary*, *phrase* and the rest, so L1 does not publish a boundary-strength profile. It publishes the relation itself; turning repetitions into boundary evidence (including GTTM's start-orientation) is L3's own terms.
  > 4. *Not the voice-leading axis* (this sitting's argument; the derivation had left it open): the axis's objects are *"the accepted melodic phrase, chord voicing and arrangement, part-writing, the stock eighteenth-century outer-voice patterns"* (`FRAMEWORK.md` lines 502–504); a restatement relation over notes is none of these and needs no phrase. If the axis wants it, the spine–axis row lets it read L1's publication (line 534).
  > 5. *The similarity measure is not chosen here.* Both sources state it is replaceable and that many definitions are possible; which one infers best is measured (D-254), and it is marked UNESTABLISHED until then.
- **OQ-L3-6 ★ (face (d); L3-S24) — form-function names.** *Question for the user:* does L3 publish
  names of formal function (exposition, second theme, development, recapitulation) beside the grouping,
  as exemplar 2 writes them? Adding them amends L3's charter list.

  **ANSWERED (records/cowork/rulings/cowork_rulings_2026_11_03_l3_sections_sitting.md, Ruling 3):**
  > L3 works out, for each section at every level of the nesting, a form-function name where the chosen naming scheme has one (e.g. *exposition*, *second theme*, *development*, *recapitulation*), "no name" being a possible reading; each name is published with its rival names and their mass, carrying its establishment status — UNESTABLISHED until measured against a ground truth.
- **OQ-L3-7 (faces (e), (h); L3-S28) — the continuo grain.** A figured bass that figures passing bass
  notes by their own sonority needs the spelled interval content above the lowest sounding pitch at
  every slice. IC-L1 S-49 publishes it only at cue slices and unspelled. *The input-contract statements
  concerned:* IC-L1 S-49 and S-50. Would L1 publish it per slice, spelled? With it goes the question
  whether the charter's *figured bass* means the continuo grain at all.

  **ANSWERED (records/cowork/rulings/cowork_rulings_2026_11_03_l3_figured_bass_sitting.md, Ruling 1):**
  > L1 publishes, at every slice, the spelled intervals above its lowest sounding pitch. L3 publishes a second figured bass at the continuo grain, read off that publication, named apart from the span figure, giving under every bass note — passing bass notes included — what actually sounds above it, written by L3-S26's accidental rule and L3-S27's full-figure rule. The span figure of L3-S25 is unchanged.
- **OQ-L3-8 ★ (face (a); L3-S7) — the pivot label.** *Question for the user:* IC-L2 carries to this
  specification whether the label *"this chord is in both tonalities"* is published at L3 or as a
  display view. Does L3's charter list gain it? It would be a view, deciding nothing.

  **ANSWERED (records/cowork/rulings/cowork_rulings_2026_11_03_l3_pivot_label_sitting.md, Ruling 1):**
  > at each change of tonality in L2's principal reading, L3 publishes the decided chord of the span on each side of the change, re-expressed as a scale degree in the other tonality, each carrying a flag stating whether that chord is diatonic in both tonalities — the flag a fact, not a test of pivot-ness (exemplar 2's Neapolitan pivot at bar 41, B♭ major over D, is chromatic in A minor and would carry "no"). No chord is named "the pivot". Each rival whole reading L2 publishes gives its own set (this side's proposal, put with B and confirmed with it).
- **OQ-L3-9 (face (a); L3-S5) — the augmented sixth in a display.** L3 publishes no root for the
  augmented sixths. Whether a display respells them as dominant-seventh symbols is the display's
  convention. Recorded so the gap is not mistaken for a defect.

  **RECORDED ANSWER (records/cowork/rulings/cowork_rulings_2026_11_03_l3_chord_symbol_sitting.md, §2 (e)):**
  > not a question for the user. L3 publishes the quality, the bass and a named reason in place of the root; a dominant-seventh respelling would assert a chord L2 did not decide, so it is a display's own act.

  *Recorded by the record as this side's derivation, not ruled; challengeable.*
- **OQ-L3-10 ★ (face (h); L3-S40) — L3 as a requester of more music.** *Question for the user:* may L3,
  like L2, ask the caller for a larger span when its in-span phrase or section reading depends on music
  beyond the edge, stopping by convergence under the safety cap? If not, L3 marks every edge-crossing
  unit and stops at the span.

  **ANSWERED (records/cowork/rulings/cowork_rulings_2026_11_03_l3_edge_of_span_sitting.md, Ruling 1):**
  > L3 may ask the caller for more music where its in-selection phrase or section reading depends on music beyond the edge; it stops when its own in-selection phrases and sections stop changing between successive enlargements, under the same safety cap (D-624), and marks its publication truncated if the cap ends the loop (D-263). Units cut by the edge carry their mark (settled already in L3-S40).
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

**Questions for the user, counted from the ★ marks: 5 of 14** (OQ-L3-2, 3, 6, 8, 10); all five are now ANSWERED, each by the record its ANSWERED mark names. (was: "(OQ-L3-2, 3, 6, 8, 10)."; staleness fix shown, records/cc/instructions/cc_instruction_l3_application_session_3_task_1_stretch_2_2026_11_22.md, §3 item 6) DP-N and DP-Q,
which L3-S6, L3-S18 and L3-S20 touch, are the charter's own open questions and are not counted here.

---

## Statements added by the L3 family rulings

### Added — records/cowork/rulings/cowork_rulings_2026_11_03_l3_key_areas_sitting.md, Rulings 1 and 2, key areas (K1 and K2)

*Ruling 1 (K1), as ruled:*

> L3 publishes key areas — runs of consecutive spans of L2's segmentation grouped by tonality — as an output of its own; what exactly a key area is, is K2 (§4).

*Ruling 2 (K2), as ruled:*

> a key area is a maximal run of consecutive spans of L2's segmentation sharing one tonality in L2's principal reading, closed and a new one opened at every change of tonality; it decides nothing beyond L2's reading. Each rival whole reading L2 publishes gives its own sequence of key areas, carrying whatever L2 publishes for that reading (this side's proposal, put with A and ruled with it).

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1, part A

*Part A, as `ratification_surfaces/cowork_l3_tier3_display_surface_2026_11_04.md` states it after the check:*

> ## 2. Part A — every display string is made outside the analysis, from published facts (10 row-parts)
>
> **The rows, in the old documents' own words:**
> - **Row 4.2** (line 2100) and **Row 4.3** (2116), `ARCHITECTURE.md` §4.3: the formatter is *"Kept separate from
>   `ChordAnalyzer` so the analysis layer remains display-agnostic"*; *"analysis produces data, formatters produce
>   strings."* Graded AGREES with L3-S5.
> - **Row 19.1** (23848) and **Row 19.3 (ii)** (23874), `ARCHITECTURE.md` §2.3: *"Analysis components produce structured
>   data — they never produce display strings"*; the separation *"must be maintained throughout."* AGREES with L3-S5.
> - **Row 15.42 (iii)** (21811): *"display renderings are presentation, facts are published"*. AGREES with L3-S5.
> - **Row 7.329 (ii)** (8245) and **Row 7.330** (8263), the old function-layer design: translating cadence labels is
>   *"a display/formatting task on the structured cadence-type identifiers"*. The derivation is silent.
> - **Row 21.191** (30195), **Row 21.205** (30399) and **Row 57.119** (73487): Roman numerals and Nashville numbers are
>   *"presentation choices, not separate analyses"*, and *"encode the same information"*. The derivation is silent.
>
> **The proposal** (Row 4.2): *"that every display string be produced outside the analysis, from published facts, and
> that the analysis carry no display convention — L3-S5 carries this for the chord symbol's root only."*
>
> **Why the record already settles it:**
> - **L3-S5** (derivation `cowork_blind_derivation_l3_2026_10_17.md` lines 258–260 **[checked]**): a display that needs a
>   root for every chord *"reads the quality and the bass and chooses its own convention, as a display act, and never
>   publishes it back into the analysis."* L3-S27 (lines 848–850 and its status line 863 **[checked]**) says the same of
>   the figured bass: the full figure *"is the published fact"*, an abbreviated figure *"a view of it under a declared
>   convention"*, and *"Which convention a display defaults to is the display's own choice."* Where else the derivation
>   names a display (L3-S29, lines 892–893 and 909–910 **[checked]**: a comparison with the composer's figures is *"the
>   measurement layer's act or a display's"*) it agrees. The proposal states the rule once for all of L3. *[Corrected by
>   the check, §10 items 3 and 4. Former wording: "L3-S25's status line (863 [checked]) says the same of the figured bass:
>   … The derivation already applies the rule in the two places it speaks of display; …"]*
> - **The chord-symbol Ruling 1 of 2026-11-03** (the user's word "confirmed" **[checked]**) has L3 publish the chord
>   symbol as fields — the spelled root with its pitch class, the quality, the bass. **The pivot-label Ruling 1** of the
>   same day (the user's word "yes" **[checked]**) publishes the pivot as a re-expressed degree with a flag. That neither
>   ruling publishes a text string is this side's reading; neither says so in terms. *[Corrected by the check, §10 item 5.
>   Former wording: "as structured fields — … the bass — not as a string. … with a flag, not as a label string."]*
> - **D-100** (`DECISIONS.md` line 267, LIVE **[checked]**): *"Every derived fact is published exactly once, on the
>   producing layer's output surface"*. A Roman numeral and a Nashville number made from the same decided chord are two
>   ways of writing one fact, so they are renderings, not two facts.
>
> **Weak points:**
> 1. *"The analysis carry no display convention"* must not be read against the chord-symbol ruling. A spelled root is
>    information the reading decided (F♯ is not G♭), not a way of writing it; the ruling published it on that ground. The
>    proposal concerns how facts are turned into text.
> 2. L3 publishes some facts in the form the ground-truth annotations use (the figure *"written in the figured-bass manner
>    the ground truth uses"*, `FRAMEWORK.md` glossary line 97, as the chord-symbol record quotes it **[relayed]**). That
>    is the form of a published fact, fixed so it can be graded, not a display string. A display may still abbreviate it.
> 3. Row 4.2's own sentence names a component of the old code (`ChordAnalyzer`). What is adopted is the rule, not the
>    component; the code's present state stays with the QUARANTINED audit questions of Rows 15.42 (i)–(ii) and 19.3 (i).

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1):*
  > **A (10 row-parts: 4.2, 4.3, 7.329 (ii), 7.330, 15.42 (iii), 19.1, 19.3 (ii), 21.191, 21.205, 57.119) — ADOPTED.** Every display string is produced outside the analysis, from published facts; the analysis carries no display convention; a Roman numeral and a Nashville number are two renderings of one decided chord. Grounds: L3-S5's premise, L3-S27, L3-S29; the chord-symbol and pivot-label Rulings 1 of 2026-11-03; D-100.

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1, part B

*Part B, as `ratification_surfaces/cowork_l3_tier3_display_surface_2026_11_04.md` states it after the check:*

> ## 3. Part B — the tonic / subdominant / dominant summary is no published fact (10 row-parts)
>
> **The rows:**
> - **Row 7.5 (i) and (ii)** (line 3235), the old function-layer design: *"The three-role summary (tonic / subdominant /
>   dominant) is a lossy, deterministically-derivable read-out, not a stored output; it is built only if and when an
>   accessibility/teaching display needs it, and never drives analysis."*
> - Travelling with it: **Row 7.6** (3252), a first-class three-role analysis *"rejected (it would invent judgments no
>   data can verify)"*; **Row 7.24** (3534); **Row 7.59** (4090), *"Optionally derive the three-role read-out … by a fixed
>   lookup; not part of the analysis"*; **Row 7.226 (ii)** (6732); **Row 7.227** (6748), rejected because it *"would have
>   to resolve the few context-dependent role cases, which no reference data can verify"*; **Row 7.228** (6763), *"The
>   read-out, if built for accessibility, defaults those cases to their tonic-side bucket"*; **Row 7.274** (7429), the
>   glossary entry; **Row 7.294 (i)** (7712), no three-role prediction target, *"the literature outputs Roman numerals and
>   treats the three roles as a derived view"*. The derivation is silent on all of them. Rows 7.226–7.228 carry the SEEN
>   mark: the deriving session saw D-335's heading line only.
>
> **The proposal** (Row 7.5): *"that the tonic / subdominant / dominant summary be no published fact of the analysis — at
> most a read-out a display computes from the published chord — and that no decision read it"*, Row 7.228's tonic-side
> default carried for any such read-out.
>
> **Why the record already settles it:**
> - **D-335** (`DECISIONS.md` line 435, LIVE, 2026-08-02 · user **[checked]**): *"The function layer outputs the Roman
>   numeral; the tonic/subdominant/dominant summary is a derived read-out, never a stored output"*. Rows 7.226 to 7.228
>   lie in D-335's home (the old function-layer design §9, lines 621–626); the other rows say the same at other places of
>   that document. D-335 speaks of the old function layer; that its subject is now L3's is this side's reading, on the
>   charter's placing of the cadence and the chord symbol at L3. Adopting the proposal carries a live ruling of the
>   user's into L3's specification. *[Corrected by the check, §10 item 6. Former wording: "The rows above are D-335's home
>   text and its glosses."]*
> - **The ruled standard for departing from a design rule** (`CLAUDE.md`, *HOW A DECISION SURFACE IS WRITTEN*, step 4,
>   citing the 2026-10-07 ruling **[checked]**): a rule holds while there is no reason to suspect that breaking it would
>   improve the inference. The summary *"never drives analysis"* (Row 7.5 (ii)), and the literature *"outputs Roman
>   numerals and treats the three roles as a derived view"* (Row 7.294 (i)); so, on this side's reading, publishing it
>   would not change what is inferred. *[Corrected by the check, §10 item 7. Former wording: "No decision reads the
>   summary and the grading is against Roman numerals (Row 7.294 (i)), so publishing it would not change what is
>   inferred."]*
> - **D-295** (line 509, LIVE **[checked]**), *"every inferred object must be displayable"*, is met: the summary can be
>   displayed, computed by the display from the published chord.
>
> **Weak point — the tension with the pivot label, stated.** The pivot-label ruling put a re-expression of L2's decided
> facts at L3 rather than at a display, after the lesson *"What harm is there in exposing such names?"* (entry 499, as
> that record quotes it **[relayed]**). By that lesson, L3 could publish the summary too. **The difference is the harm D-335
> names:** the pivot label re-expresses the decided chord and settles nothing (that record: *"No chord is named 'the
> pivot'"*), whereas the summary must put the few context-dependent chords on one side or the other, a judgment Row 7.227
> says *"no reference data can verify"*. Publishing it at L3 would publish that judgment as a fact of the analysis. One
> variant was considered and is not recommended: L3 publishes the summary with a flag on the context-dependent chords in
> place of the tonic-side default. It meets the harm, but it would overturn a live ruling without any reason to expect a
> gain in inference, which the step 4 standard requires. **If the user sees a gain this side does not, the variant is
> the alternative to raise.**

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1):*
  > **B (10 row-parts: 7.5 (i), 7.5 (ii), 7.6, 7.24, 7.59, 7.226 (ii), 7.227, 7.228, 7.274, 7.294 (i)) — ADOPTED.** The tonic / subdominant / dominant summary is no published fact of the analysis — at most a read-out a display computes from the published chord, defaulting its context-dependent cases to the tonic side — and no decision reads it. Grounds: D-335 (LIVE, user, 2026-08-02); the `CLAUDE.md` decision-surface step 4 standard; D-295 met by the display read-out. **Declined variant:** L3 publishes the summary with a flag on the context-dependent chords — it would overturn D-335 with no reason to expect a gain in inference.

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1, part C

*Part C, as `ratification_surfaces/cowork_l3_tier3_display_surface_2026_11_04.md` states it after the check:*

> ## 4. Part C — the grouping has one producer, L3, and it is what a display reads (1 row-part)
>
> - **Row 8.54** (line 9601), the old grouping design: *"The contract to the display layer above is this structure; L6 is
>   its only producer."* The derivation is silent. **Proposal:** *"that the grouping have L3 as its only producer, and be
>   the surface a display reads."*
> - **Settled by:** the charter's L3 *Publishes* list, which includes the phrase and section grouping (as the route
>   record §2 restates it **[checked there]**; `FRAMEWORK.md` itself not read **[relayed]**); the key-areas Ruling 2 of
>   2026-11-03, which adds key areas to L3's grouping (Rows 3.1 (iii), 8.12 and the others ADOPTED, that record's lines
>   89–90 **[checked]**; *corrected by the check, §10 item 8; former wording: "[checked at that record's line 127 by
>   search]"*); and D-100 (one
>   fact, one home, on the producing layer's surface).
> - **Weak point:** "L6" is an old layer name. What is adopted is "L3 is the grouping's only producer"; no layer number
>   from the old documents enters the specification.

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1):*
  > **C (1 row-part: 8.54) — ADOPTED.** The grouping has L3 as its only producer and is the surface a display reads. Grounds: the charter's L3 *Publishes* list [relayed]; key-areas Ruling 2; D-100.

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1, part D

*Part D, as `ratification_surfaces/cowork_l3_tier3_display_surface_2026_11_04.md` states it after the check:*

> ## 5. Part D — nothing L3 publishes is written into the score except by the user's own act (4 row-parts)
>
> - **Row 19.5** (line 23902), `ARCHITECTURE.md` §2.9: *"It never modifies the main score automatically."* Travelling with
>   it: **Row 19.4** (23889), *"The system presents analytical findings and suggestions"*; **Row 19.6** (23916), *"All
>   score modifications require explicit user action"*; **Row 19.8** (23944), the user acts on a suggestion *"explicitly
>   through standard MuseScore editing"*. The derivation is silent. **Proposal:** *"that nothing L3 publishes be written
>   into the score except by the user's explicit act."*
> - **Settled by — this side's reading, the weakest of the four parts:** no register entry on this subject was found
>   (`DECISIONS.md` searched for *explicit user*, *modif… the score*, *display-agnostic*, *formatter*, *Nashville*: one
>   hit, line 90, a passage naming the formatter's source file under D-311, whose subject is a file split, not this
>   **[checked]**; the `decisions/` group files not searched). The ground is the charter's shape: L3's outputs are things
>   it *publishes*, and the score is L0's notated record, which the layers beneath L3 read and L3 reads through them. A
>   layer that wrote into the score would change what it and they read. *[Corrected by the check, §10 item 9. Former
>   wording: "… *Nashville*: no matching entry [checked by search]). … which every layer reads. A layer that wrote into
>   the score would change its own input."]* So the sentence, read as a statement about L3, restates what L3 already is; it adds no step and removes none.
> - **Weak points:** (1) the rule in `ARCHITECTURE.md` is about the whole application, not one layer; adopting it into
>   L3's specification states only L3's part of it. (2) Row 19.4 says nothing about L3 in particular; it travels because
>   it opens the same paragraph. (3) The disposition vocabulary has no charter for the user interface, so the alternative
>   to adopting is to leave the rows as proposals, which the route record allows. This side sees no gain in that, and
>   found no harm in adopting. *[Corrected by the check, §10 item 10. Former wording: "Nothing is gained by that; no harm
>   in adopting was found."]*

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_display_sitting.md, Ruling 1):*
  > **D (4 row-parts: 19.4, 19.5, 19.6, 19.8) — ADOPTED.** Nothing L3 publishes is written into the score except by the user's explicit act. Ground: this side's reading of the charter's shape (L3 publishes; the score is the notated record the layers read); no register entry found on the subject (the index searched, the `decisions/` group files not).

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1, part A

*Part A, as `ratification_surfaces/cowork_l3_tier3_span_kinds_surface_2026_11_04.md` states it after the check:*

> ## 2. Part A — each kind of span is named by what bounds it, as a distinct kind; the bare word "region" is not used (8 row-parts)
>
> **The rows, in the old documents' own words:**
> - **Row 19.37** (line 24433), `ARCHITECTURE.md`: *"**The span typology** — a "region" is a *family* of spans, each named
>   by its bounding criterion."* Proposal: *"that every kind of span L3 publishes be named by the criterion that bounds
>   it."*
> - **Row 19.40** (24514), the same bullet: *""Region" unqualified is **banned** as ambiguous; every layer names the span
>   it operates on."* ADOPTED — proposed, travelling with Row 19.37.
> - **Row 38.62 (i) and (ii)** (47658), `cowork_target_architecture.md`: *"**★ Spans are a typed family, not one "region" —
>   name each by its bounding criterion (user-ratified 2026-06-29).**"* Proposal for (i): *"that the spans L3 publishes be
>   held as a family of distinct kinds, never as one kind under one bare word."* (ii) travels with Row 19.37.
> - **Row 38.64 (i) and (ii)** (47688): *"Each segmentation is a distinct **span type**, defined by **what event bounds
>   it** and serving **one analytical need**; the bare word "region" must name exactly one of them, never several."* (i)
>   travels with Row 19.37, (ii) with Row 19.40.
> - **Row 38.83 (i)** (48007): *"every layer names the span it operates on by its type — "chord-span", "key-span",
>   "punctuation-span", "decision-context span" —"*. Travels with Row 19.40.
> - **Row 38.84** (48024): *""Region" unqualified is banned as ambiguous."* Travels with Row 19.40, *"which tabulates the
>   same sentence"*.
>
> The derivation is silent on all eight.
>
> **Why the record already settles it:**
> - **D-028** (`DECISIONS.md` line 258, LIVE **[checked]**): *"The span typology - every layer names the span it operates
>   on; bare 'region' is banned"*, home `ARCHITECTURE.md`. The reading file places D-028's home at `ARCHITECTURE.md` lines
>   1141–1142 and names Row 19.40 as lying in it (lines 23765 and 25431 **[checked]**). So Row 19.40 is the home text of a
>   live register entry, and the rows travelling with it say the same or close to it (weak point 2 states the one
>   difference in wording). Adopting them carries that entry into L3's specification. *[Corrected by the check, §9 item 4.
>   Former wording: "and the rows travelling with it restate it."]*
> - **The rulings already define each L3 span kind by what bounds it** (each **[checked]** at its record):
>   - a **phrase unit** is bounded by phrase ends as L3 decides them (phrase-units Ruling 1 of 2026-11-02, §2: *"The phrase
>     reading tiles the working span with two kinds of unit — phrases, and the stretches between phrases … — and each unit
>     carries which kind it is"*; the derivation's glossary, line 40: a phrase end is *"given as a position in the record
>     (a change point or span edge)"*);
>   - a **section** is bounded by section boundaries L3 decides, each of them a boundary of the phrase reading (sections
>     Ruling 1 (2) of 2026-11-03: *"a section boundary is always a phrase boundary"*; Ruling 2: sections may contain
>     sections, *"each level tiling the level above"*);
>   - a **key area** is bounded by changes of tonality in L2's principal reading (key-areas Ruling 2 of 2026-11-03: *"a
>     maximal run of consecutive spans of L2's segmentation sharing one tonality in L2's principal reading, closed and a
>     new one opened at every change of tonality"*);
>   - L3 reads two kinds it does not decide: the **harmonic span**, bounded by L2's decision (one chord and one tonality
>     each, the glossary line 29), and the **working span**, bounded by the caller's request (glossary line 28).
>
>   So the rule names, at the level of a principle, what the rulings did kind by kind.
> - **The derivation does not use "region" as the name of a span.** A search of it for *region* finds one line (382
>   **[checked]**), a relayed fact about a grouping theory whose rule *"needs region and chord distances supplied from
>   outside"* (Hamanaka, Hirata & Tojo 2013). There the word is that theory's term for a key region in a distance measure,
>   not a name the derivation gives a span (this side's reading).
>
> **Weak points:**
> 1. **D-028's index row records no date and no ratifier** (the column shows "—"). It is marked LIVE. The outgoing Row
>    38.62 says *"user-ratified 2026-06-29"*; that is the old document's own claim **[relayed]**, not checked against any
>    ruling record. The register entry, not the old document's parenthesis, is the ground.
> 2. **Row 38.64 (ii) and Rows 19.40 / 38.84 differ in wording.** One says the bare word must name *"exactly one of them,
>    never several"*; the other two ban it outright. Both are met if L3's specification does not use the word at all, which
>    is the derivation's present state (the line 382 reading above). Nothing is chosen between them.
> 3. **"Serving one analytical need"** (Row 38.64 (i)) is carried as written. On this side's reading it describes why the
>    kinds are distinct and adds no test of its own; the bounding event is what the rule fixes.
> 4. **The old names are not adopted.** Row 38.83 (i) lists *"chord-span", "key-span", "punctuation-span", "decision-context
>    span"*. What is adopted is the rule, not those names; the names are Row 19.38's, which the reading file places
>    separately (RELOCATED, UNPLACED and HISTORICAL by claim, line 24479 **[checked]**). L3's specification would use the
>    names the derivation and the rulings already use (harmonic span, working span, phrase unit, section, key area).
> 5. **"Every layer"** in Rows 19.40 and 38.83 (i) speaks of the whole system. Adopted into L3's specification it states
>    only L3's part. D-028 already states the whole.
> 6. **The bare word "span".** The glossary lets bare *span* stand for the harmonic span (line 29). That names exactly one
>    kind, so it is consistent with the rule; whether the application act writes it out in full each time is an editorial
>    matter for that act, not a question here.

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1):*
  > **A (8 row-parts: 19.37, 19.40, 38.62 (i), 38.62 (ii), 38.64 (i), 38.64 (ii), 38.83 (i), 38.84) — ADOPTED.** L3's kinds of span are distinct kinds, each named by what bounds it, and the bare word "region" is not used. Grounds: **D-028** (`DECISIONS.md` line 258, LIVE; the index records no date or ratifier): *"The span typology - every layer names the span it operates on; bare 'region' is banned"*, Row 19.40 lying in its home (the reading file, lines 23765 and 25431); the rulings that define each L3 kind by its bound (phrase units, phrase-units Ruling 1 of 2026-11-02; sections, sections Rulings 1 (2) and 2 of 2026-11-03; key areas, key-areas Ruling 2 of 2026-11-03). The old names (chord-span, key-span, punctuation-span) are not adopted; Row 19.38 keeps its own placements.

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1, part B

*Part B, as `ratification_surfaces/cowork_l3_tier3_span_kinds_surface_2026_11_04.md` states it after the check:*

> ## 3. Part B — the music is segmented several ways at once (1 row-part)
>
> - **Row 38.63** (line 47674): *"A tonal stream is segmented **many ways at once**, not one."* The derivation is silent.
>   **Proposal:** *"that L3's specification state that the music is segmented several ways at once, L2's harmonic spans,
>   L3's phrase units and its sections among them."*
> - **Settled by:** the rulings themselves. Over one working span the analysis publishes at least four segmentations, each
>   ruled: L2's harmonic spans (the glossary, from the charter and L2's input contract **[relayed]**); L3's phrase units
>   (phrase-units Ruling 1); its sections, nested to any depth (sections Rulings 1 and 2); and its key areas (key-areas
>   Rulings 1 and 2), with a sequence of key areas for each rival whole reading L2 publishes (key-areas Ruling 2, *"this
>   side's proposal, put with A and ruled with it"*). The statement says in one sentence what those rulings already did.
> - **Weak point:** the proposal's list (*"among them"*) is open. The key areas, ruled after the reading file was written,
>   belong in it; the application act writes the list as it stands then.

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1):*
  > **B (1 row-part: 38.63) — ADOPTED.** The music is segmented several ways at once: L2's harmonic spans, L3's phrase units, its sections and its key areas, each ruled.

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1, part C

*Part C, as `ratification_surfaces/cowork_l3_tier3_span_kinds_surface_2026_11_04.md` states it after the check:*

> ## 4. Part C — for any two kinds of span, the specification says whether one nests in the other or the two cut across; it never states nesting where they cut across (2 row-parts)
>
> **The rows:**
> - **Row 38.83 (ii)** (line 48007): *"for any two it relates, states whether they **nest** or **cross-cut**."* Proposal:
>   *"that L3's specification state, for any two spans it relates, whether one nests in the other or the two cross-cut."*
> - **Row 57.354** (74603): *"Asserting containment where the truth is cross-cutting (e.g. nesting key-areas inside
>   punctuation-spans) is a modelling error."* Proposal, travelling with Rows 38.83 (ii) and 57.353: *"that L3 never state
>   that one span kind nests in another where the two cut across each other, key areas inside phrase units among them."*
>
> The derivation is silent on both.
>
> **Why the record already settles it.** The rule asks the specification to state each relation; the relations themselves
> are fixed by the rulings (points 1 and 2) or follow from them on this side's reading (points 3 and 4), except one, which
> is open and stays open (point 5): *[Corrected by the check, §9 item 10. Former wording: "are already fixed by the
> rulings, except one, which is open and stays open (point 5):"]*
>
> 1. **Harmonic spans nest in key areas.** A key area is *"a maximal run of consecutive spans of L2's segmentation"*
>    (key-areas Ruling 2 **[checked]**), so each harmonic span lies whole inside one key area. The same ruling gives each rival whole reading its own
>    sequence of key areas; that a rival's own spans then nest in its own key areas is this side's reading. *[Corrected by
>    the check, §9 item 5. Former wording: "For a rival whole reading, its own spans nest in its own key areas (the same
>    ruling)."]*
> 2. **Phrase units nest in sections, and sections in sections.** *"Each section is a run of consecutive units, sections at
>    one level tile the level above"* (L3-S22, derivation lines 701–703 **[checked]**; ratified, sections Rulings 1 (2) and
>    2).
> 3. **Key areas and phrase units cut across each other.** Phrase-units Ruling 2, item g **[checked]**: *"a change of
>    tonality may fall inside a phrase unit and a phrase may end without one"*, ratifying Rows 7.63, 8.52 (ii), 19.39 (iv)
>    and 57.353; the same item says *"The key-areas half waits for the key-areas family."* Key-areas Ruling 2 then closed a
>    key area at every change of tonality, deciding *"nothing beyond L2's reading"* *[corrected by the check, §9 item 6;
>    former wording: "and at nothing else"]*, and that record's §4 notes Row 8.76 (key areas *"not nested
>    in punctuation-spans"*) as *"consistent with Ruling 2"*. Putting the two rulings together — this side's reading — a key
>    area may begin inside a phrase unit and a phrase unit may end inside a key area, so neither kind nests in the other.
>    Row 57.354's own example is this pair.
> 4. **Key areas and sections cut across each other** — this side's reading, from points 2 and 3: a change of tonality
>    inside a phrase unit is also inside that unit's section; and a section boundary, being a phrase-unit boundary, need not
>    change tonality.
> 5. **Harmonic spans and phrase units — OPEN, not settled here.** The old text's *"chord-spans ⊂ punctuation-spans"* is
>    Row 19.39 (ii), placed UNPLACED by the reading file (line 24509 **[checked]**), because L3-S8 makes *"Every change point
>    and both span edges"* candidate phrase ends, a change point not being only a boundary of L2's spans (as that row
>    quotes it **[relayed]**). That row is tier item 14's (the UNPLACED rows), not this cut's. Adopting Row 38.83 (ii) obliges
>    the specification to state this relation once item 14 places it; it does not decide it.
>
> The phrase reading and the top level of sections each cover the working span (L3-S12, L3-S22 **[checked]**); L2's
> reading, and so its harmonic spans and the key areas read off them, is a reading *"for the working span"* (glossary line
> 33, from L2 **[relayed]**). *[Corrected by the check, §9 item 7. Former wording: "All of the kinds above lie inside the
> working span, and the phrase reading and the top level of sections each cover it (L3-S12, L3-S22 [checked])."]*
>
> **Weak points:**
> 1. Points 3 and 4 are this side's readings joining two rulings each. Neither ruling states the relation in those words.
> 2. Point 5 is a real gap in what can be stated today. It is a gap in placement, not a choice for this cut: the row is
>    already routed to item 14.
> 3. "Cut across" means that in general neither kind contains the other. In a given passage a key area and a section may
>    happen to begin and end together; the rule does not forbid that, it forbids stating containment as a rule.

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_span_kinds_sitting.md, Ruling 1):*
  > **C (2 row-parts: 38.83 (ii), 57.354) — ADOPTED.** For each pair of kinds of span the specification states whether one nests in the other or the two cut across, and never states containment where they cut across. As the surface §4 states them: harmonic spans nest in key areas and phrase units nest in sections (settled by the rulings); key areas cut across phrase units and across sections (this side's reading, joining two rulings each); **whether a phrase end may fall inside a harmonic span is NOT decided by this ruling** — Row 19.39 (ii), UNPLACED, tier item 14's; the specification states that relation once item 14 places it.

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1, part A

*Part A, as `ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md` states it after the check:*

> ## 2. Part A — cost: every cost-driving choice a setting, optional refinements separable, re-analysis local (3 row-parts)
>
> **The rows, in the old documents' own words:**
> - **Row 19.29 (i) and (ii)** (line 24281): *"**(a)** every cost-driving choice is an explicit *setting*, never a
>   hardcoded constant; **(b)** every optional expensive refinement is a cleanly separable on/off stage."* Proposals:
>   (i) *"that every choice of L3 that drives its cost be an explicit setting and never a constant written into the
>   code"*; (ii) *"that every optional expensive refinement of L3 be a separable stage that can be turned on and off."*
> - **Row 19.53 (ii)** (24715): *"**(R2)** re-analysis is incremental over the dirty span plus a bounded margin"*.
>   Proposal: *"that L3's re-analysis after an edit cover only the edited span and a bounded margin around it."* Claims
>   (i) and (iii) of the same row are ADOPTED — carried by L3-S40, whose defense holds L3 to *"the bounded-context rule
>   that cost scales with the working span"* (as the row quotes it).
>
> The derivation is silent on all three.
>
> **Why the record already settles it:**
> - **D-035** (`DECISIONS.md` line 265, LIVE **[checked]**): *"The effort setting - every cost-driving choice is a
>   setting, never a hardcoded constant"*, home `ARCHITECTURE.md`; Row 19.29 lies in its home (reading file line 25429
>   **[checked]**).
> - **D-030** (line 260, LIVE **[checked]**): *"Bounded context - cost scales with the working span, not the whole
>   score"*; Row 19.53 lies in its home (line 25431 **[checked]**). Claim (ii) is the re-analysis half of the same
>   sentence whose other two halves L3-S40 already carries.
> - **The tractability record of 2026-10-05** (`records/cowork/rulings/cowork_rulings_2026_10_05_l2_tractability_sitting.md`
>   **[checked]**) already reads these settings for L2 without deciding any dial: Ruling 1 (iv), *"An effort setting may
>   not quietly reduce how many readings the search keeps"*; §1b item 3, *"A dial the user rules and the end user turns is
>   not the "quiet" reduction Ruling 1 (iv) bars"*; and **D-202** (line 659, **DEFERRED** **[checked]**), the effort
>   control as one setting with several dials, deferred until a measurement shows which pieces must be switchable (as
>   that record quotes it).
>
> **Weak points:**
> 1. **No dial is decided, and none is proposed.** Adopting the rule says only that a cost-driving choice of L3, where one
>    exists, is a setting rather than a constant. Which settings L3 has, and their defaults, are D-202's deferred question.
> 2. **The tractability ruling is L2's.** That a setting may not quietly reduce the readings L3 keeps is not ruled for
>    L3; on this side's reading it follows for L3 from Row 19.77 below (D-297): a reading L3 has computed and then drops
>    is a loss.
> 3. **"Bounded margin" and context growth.** For L2, context grows by convergence under a safety cap (tractability
>    Ruling 1 (ii)), and what "the answer stops changing" means is open (OQ-L2-6). Row 19.53 (ii) says the margin is
>    bounded; it does not say how the bound is set, and adopting it decides nothing about OQ-L2-6.
> 4. **D-035's index row names only claim (a).** Claim (b), the separable stage, stands in the same sentence of its home
>    (the row's locator, lines 1070–1072); that it is covered by D-035 is this side's reading of the home's extent.

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1):*
  > **A (3 row-parts: 19.29 (i), 19.29 (ii), 19.53 (ii)) — ADOPTED.** Every cost-driving choice of L3 is an explicit setting, never a constant written into the code; every optional expensive refinement is a separable stage that can be turned on and off; re-analysis after an edit covers the edited span and a bounded margin. Grounds: **D-035** and **D-030** (`DECISIONS.md` lines 265 and 260, LIVE), Rows 19.29 and 19.53 lying in their homes (the reading file, lines 25429 and 25431). **Not decided:** which effort settings L3 has and their defaults (D-202, DEFERRED); how the margin's bound is set (OQ-L2-6 untouched).

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1, part B

*Part B, as `ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md` states it after the check:*

> ## 3. Part B — style lives only in the fitted values, never in the structure (1 row-part)
>
> - **Row 19.33** (line 24357): *"Style-specificity lives **only** in the *calibration* of the judgment layers (their
>   priors/weights), **never in structure**."* Proposal: *"that any style-specific behavior of L3 live only in the fitted
>   values of its model, never in its structure."* The derivation is silent.
> - **Settled by: D-024** (line 254, LIVE **[checked]**): *"The fact layers are style-agnostic; style lives only in
>   calibration"*, home `ARCHITECTURE.md`; Rows 19.32 and 19.33 lie in its home (line 25430 **[checked]**). L3 is a
>   judgment layer; the half of D-024 that speaks to it is *"style lives only in calibration"*.
> - **Weak points:**
>   1. **The naming-scheme question stays open, and this rule bears on how it is answered, not on what the answer is.**
>      Sections Ruling 3 of 2026-11-03 *[corrected by the check, §12 item 2; former wording: "Ruling 6"]* left open *"which naming scheme (sonata-form labels, Caplin's theme types, or both)"*
>      (`cowork_rulings_2026_11_03_l3_sections_sitting.md`, line 161 **[checked]**). Under this rule, whichever scheme is
>      chosen, a dependence on style sits in fitted values (for example the mass a name receives), not in a separate
>      structure per style. That is the content of D-024 carried into L3; it chooses no scheme.
>   2. Under the user's rule of 2026-10-07 (no design rule may block the ultimate objective in the long run; a rule is
>      tested by measurement as soon as there is reason to suspect breaking it would improve inference), this rule holds
>      until such a reason appears. This sitting met none, and did not search for one. *[Corrected by the check, §12
>      item 7. Former wording: "None is on the record this sitting read."]*

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1):*
  > **B (1 row-part: 19.33) — ADOPTED.** Any style-specific behaviour of L3 lives only in the fitted values of its model, never in its structure. Ground: **D-024** (line 254, LIVE), Row 19.33 in its home (line 25430). **Not decided:** which naming scheme sections use (sections Ruling 3 of 2026-11-03 left it open).

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1, part C

*Part C, as `ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md` states it after the check:*

> ## 4. Part C — what L3 reads, and what counts as losing information (5 row-parts)
>
> **The rows:**
> - **Row 19.56 (iii)** (line 24761): *"within its scope uses *all* the information L1 carries losslessly (notated
>   spelling, metric weight, voice)"*. Proposal: *"that L3 read, within its scope, all of the information the layers
>   beneath it publish without loss — the notated spelling, the metric weight and the voice — and discard none of it."*
> - **Row 19.76 (ii)** (25094): *"…the ruled-out reading is carried on the output surface at low confidence, unless the
>   elimination is recomputable from what that surface does keep."* Proposal: *"that a reading L3 rules out need not be
>   published where its exclusion can be recomputed from what L3 does publish."* Claim (i) is ADOPTED — carried by L3-S13.
> - **Row 19.77** (25111): *"NEVER COMPUTING a possibility is not information loss; only DISCARDING a computed one is."*
>   Proposal: *"that an alternative L3 decides on measured evidence never to compute is no loss of information, and that
>   only a reading L3 computed and then left out of its publication is."*
> - **Row 19.78** (25126): *"A layer that decides, on measured evidence, not to work out a particular alternative at all
>   has lost nothing"*. ADOPTED — proposed, travelling with Row 19.77.
> - **Row 19.82** (25182): *"A published fact that no one reads is either **declared dormant**, with its future consumer
>   named, or removed."* Proposal: *"that an L3 fact no consumer reads be either declared dormant, with its future consumer
>   named, or removed — evidence-class facts being published broadly as Row 19.81 states."*
>
> The derivation is silent on all five.
>
> **Why the record already settles it:**
> - **Row 19.56 (iii): D-033** (line 263, LIVE **[checked]**): *"Each layer owns one evidence-source-times-question
>   contribution and uses all of L1's information"*; Row 19.56 lies in its home (line 25432 **[checked]**). With it,
>   L3-S37 as ratified: L3 reads everything L2 publishes plus L0's and L1's published facts, and nothing else (as the
>   L3-S38 ratification record of 2026-11-03 states the decided method **[checked there]**; L3-S37's own text
>   **[relayed]**).
> - **Row 19.76 (ii): D-099** (line 266, LIVE **[checked]**): *"Negative evidence is information - a ruled-out possibility
>   is carried, not dropped"*; Rows 19.75 and 19.76 lie in its home (line 25433 **[checked]**). The exception in claim (ii)
>   is part of the same sentence of the home; a ruled-out reading that can be recomputed from what is published is not
>   dropped information.
> - **Rows 19.77 and 19.78: D-297** (line 290, LIVE, 2026-08-02 · user **[checked]**): *"Correction of record: never
>   computing a possibility is not information loss; only discarding a computed one is"*; both rows lie in its home (line
>   25433 **[checked]**). The tractability record read D-297 for L2 (Ruling 1 (iii)).
> - **Row 19.82:** **no register entry was found homed at it** (the marks name D-100's home as falling in Rows 19.80 and
>   19.81, line 25433 **[checked]**). It is consistent with: **D-100** (line 267, LIVE): every derived fact published once,
>   on its producer's surface, evidence-class facts broadly even where no consumer is named (read for L2 by the
>   publication-to-next-layer Ruling 1 of 2026-10-06, line 37 **[checked]**) — which the proposal keeps; **D-581** (line
>   308, LIVE, 2026-08-04 · user **[checked]**): *"Information not yet consumed is NOT automatically a defect"*, classified
>   preserved-awaiting-consumer, lost, should-already, or unclear — the row's "declared dormant, with its future consumer
>   named" is that first class; and **D-297**: removing a fact means no longer computing it, which is no loss.
>
> **Weak points:**
> 1. **"Voice" in Row 19.56 (iii).** The proposal names notated spelling, metric weight and voice as examples. Which of
>    them L0 and L1 publish is their input contracts' matter, not read by this sitting. Adopted, the statement reads "all
>    that the layers beneath publish", the three named as the old text names them.
> 2. **Row 19.82 rests on consistency, not on a register entry.** And D-295 (line 509, LIVE, 2026-08-02 · user
>    **[checked]**: *"every inferred object must be displayable"*) together with D-522 (line 302, LIVE **[checked]**:
>    *"Explaining an inference to the end user is a late-bound DISPLAY consumer of facts that already exist"*) means
>    *[corrected by the check, §12 item 8; former wording: "(line 302, LIVE: explaining to the end user is a display
>    *consumer*)"]*, on this side's reading, that a fact the display reads is a fact someone
>    reads. So "no one reads" reaches only a fact no display and no later layer reads.
> 3. **Row 19.76 (ii) narrows what L3 must publish** (a redundant ruled-out reading may be left out). It changes nothing
>    that is inferred, and nothing is lost, since the reading can be recomputed from what is published.

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1):*
  > **C (5 row-parts: 19.56 (iii), 19.76 (ii), 19.77, 19.78, 19.82) — ADOPTED.** L3 reads, within its scope, all the information the layers beneath it publish without loss and discards none of it; a reading L3 rules out need not be published where its exclusion can be recomputed from what L3 publishes; an alternative L3 decides on measured evidence never to compute is no loss of information, and only a reading L3 computed and then left out of its publication is; an L3 fact no consumer reads is either declared dormant with its future consumer named, or removed, evidence-class facts being published broadly. Grounds: **D-033**, **D-099**, **D-297** (LIVE; Rows 19.56, 19.76, 19.77, 19.78 in their homes, lines 25432–25433); for Row 19.82, which no register entry is homed at, consistency with **D-100**, **D-581** and D-297, a display being a reader (D-295, D-522).

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1, part D

*Part D, as `ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md` states it after the check:*

> ## 5. Part D — the analysis code depends on no type of the score editor (1 row-part)
>
> - **Row 20.7** (line 25741): *"**The analysis library (`composing`) depends on no MuseScore or engraving types**"*.
>   Proposal: *"that the code computing L3's facts depend on no type of the score editor."* The derivation is silent.
> - **Settled by: D-229** (line 491, LIVE **[checked]**): *"The MuseScore-dependency rule - one general rule for what our
>   code may depend on"*; Rows 20.7 to 20.9 lie in its home (line 27106 **[checked]**). With it **D-072** (line 488, LIVE
>   **[checked]**): *"The dependency rule - the analysis library knows nothing about the score format"*.
> - **Weak point:** this is a rule on the code. The specification states it as a requirement on any implementation of
>   L3; nothing about the present code is examined or claimed here.

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1):*
  > **D (1 row-part: 20.7) — ADOPTED.** The code computing L3's facts depends on no type of the score editor. Grounds: **D-229** (line 491, LIVE), Row 20.7 in its home (line 27106); **D-072** (line 488, LIVE).

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1, part E

*Ruling 1, part E, as the record quotes it:*

> A reading missing from L3's own candidate readings is remedied inside L3, by widening its candidate set; a backward edge is not the remedy, except as the deliberate, surfaced, measured and documented exception D-466 admits.

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1, part F

*Part F, as `ratification_surfaces/cowork_l3_tier3_architecture_rules_surface_2026_11_04.md` states it after the check:*

> ## 7. Part F — the grouping is an explanatory output, not an accuracy requirement (2 row-parts)
>
> - **Row 8.105 (i)** (line 10437, WITHHELD — D-461): *"L6 is a deliberate **explainability** layer, not an accuracy
>   requirement"*. Proposal: *"that the phrase and section grouping be held as an explanatory output of the analysis, not
>   as an accuracy requirement on it."* Claim (ii), *"does not grow detection of its own"*, is UNPLACED (L3-S8 DIFFERS)
>   and is tier item 14's, not this cut's.
> - **Row 36.111 (i)** (42101, WITHHELD — D-480): *"So this primitive is **not** an accuracy requirement"*. ADOPTED —
>   proposed, travelling with Row 8.105 (i). Claim (ii) is UNPLACED (L3-S38 DIFFERS) and is item 14's.
>
> The derivation is silent on both claims (i).
>
> **Settled by:**
> - **D-461** (line 464, LIVE, 2026-08-04 · user **[checked]**): *"The grouping layer is an explainability layer, not an
>   accuracy requirement, and is deliberately kept thin"*, home `cowork_layer6_grouping_design.md` §7; Row 8.105 lies in
>   it (line 11245 **[checked]**).
> - **D-480** (line 471, LIVE, 2026-08-04 · user **[checked]**): *"The phrase-boundary primitive is NOT an accuracy
>   requirement — a competitive reference engine does no phrase segmentation at all — so it is built right but kept
>   proportionate"*; Row 36.111 lies in its home (lines 42120–42124 **[checked]**).
> - **L3-S38 as ratified:** *"L2 reads nothing L3 publishes"* — so nothing L3 publishes can carry the accuracy of L2's
>   reading (this side's reading of the two together).
>
> **Weak points:**
> 1. **"Not an accuracy requirement" does not exempt L3's own facts from measurement.** Each still carries its
>    establishment status (for example sections Ruling 3 *[corrected by the check, §12 item 3; former wording: "Ruling
>    6"]*: form-function names UNESTABLISHED until measured). On this
>    side's reading, the rule says the analysis's accuracy is not made to depend on the grouping; it does not say the
>    grouping is never measured.
> 2. **Both rows carry the WITHHELD mark:** the deriving session was not shown D-461 or D-480. That the derivation is
>    silent here is consistent with that.
> 3. **"Kept thin" and "kept proportionate"** are not in claims (i); they stand with claims (ii), item 14.

- *In short (records/cowork/rulings/cowork_rulings_2026_11_04_l3_architecture_rules_sitting.md, Ruling 1):*
  > **F (2 row-parts: 8.105 (i), 36.111 (i)) — ADOPTED.** The phrase and section grouping is an explanatory output of the analysis, not an accuracy requirement on it. Grounds: **D-461** and **D-480** (lines 464 and 471, LIVE, 2026-08-04 · user), Rows 8.105 and 36.111 in their homes. This does not exempt L3's own facts from measurement; each carries its establishment status. Claims (ii) of both rows (UNPLACED) stay with tier item 14.

### Added — records/cowork/rulings/cowork_rulings_2026_11_04_l3_literature_facts_sitting.md, Ruling 1

*Ruling 1, as the record quotes it:*

> As facts of the published literature, recorded with D-607's standing: almost all published work on locating phrase endings addresses a single melodic line, and the cues it uses are validated on single lines; for several simultaneous voices no validated deterministic rule set has been established, and L3's phrase model rests on fitted terms instead.

---

## 5. The blind act's own record — where it stands

*The measured-cost record, the independence record and the note on the brief's decomposition are the blind act's own and stand at the derivation, `cowork_blind_derivation_l3_2026_10_17.md` §5–§7, at blob `c01793f98c51e0267fb0dc7487613ac477cc1fbb`; they are not restated here (#6).*
