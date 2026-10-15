> **THE INPUT CONTRACT — the ratified specification of L2, cut for the L3 deriving session.**
> Its source is `cowork_derived_specification_l2_2026_10_10.md`; this file is a cut copy of that source and not a
> second version of it. Below this block the source stands verbatim, except that passages stating the L3 layer's own
> ruled or current design have been removed where they stood, with no mark. Do not try to reconstruct them, and do
> not treat a gap as a hint.

# The derived L2 specification — the tonal reading: segmentation, tonality, chord and assignments — as amended by the L2 family rulings of 2026-10-04 to 2026-10-10

> **STATUS: DERIVED SPECIFICATION — THE BLIND DERIVATION OF L2 AS AMENDED BY THE FORTY-THREE L2 FAMILY
> RULING RECORDS OF 2026-10-04 TO 2026-10-10 (`records/cowork/rulings/`, listed in
> `records/cc/instructions/cc_instruction_l2_application_2026_10_10.md` §L); NOT RATIFIED.** Written
> 2026-10-12 or later by Claude Code under that dispatch's Task 1, from the derivation
> `cowork_blind_derivation_l2_2026_09_27.md` at blob `d78ac530992860d38d1f605a77a2961d5440a2f6`, which stands
> untouched as the record of the blind act (D-674; the L2 route ruling of 2026-10-04, §2 step 2). Every
> statement below keeps its derived number and its six-field form; every amendment stands in place and names
> the record and ruling that made it, with the derived wording preserved at the derivation or in the same
> field (#12). **A sub-item opening *Recorded* is a record's own derivation and not a ruling, and is
> challengeable, as the forms section of the dispatch fixes; a sub-item opening *Ruled* or *Beside* carries
> the user's word at the record named.** The open questions of §4
> stand with their ANSWERED marks where a ruling answered them (OQ-L2-2, OQ-L2-4, OQ-L2-5, OQ-L2-6, OQ-L2-9,
> OQ-L2-10, OQ-L2-11, OQ-L2-14, OQ-L2-16) and open otherwise. Nothing in this file is ratified; the
> ratification act is the user's, on a decision surface over this text.
>
> **★ RATIFIED 2026-10-13 AND 2026-10-14, FACE BY FACE — added by
> `records/cc/instructions/cc_instruction_l2_ratification_application_2026_10_14.md`, Task 1.** Every part of
> this file — §0 to §5, L2-S1 to L2-S49 — has since been through a ratification act on the user's word, in
> nine acts under `records/cowork/rulings/cowork_rulings_2026_10_13_l2_ratification_granularity_sitting.md`:
> faces (a) to (h), and a ninth surface for §0, §1 and §4, with §2 and §5 ratified with it. The records are
> `records/cowork/rulings/cowork_rulings_2026_10_13_l2_face_a_ratification_sitting.md` to
> `…_face_f_ratification_sitting.md` (2026-10-13), and `…_2026_10_14_l2_face_g_ratification_sitting.md`,
> `…_2026_10_14_l2_face_h_ratification_sitting.md` and `…_2026_10_14_l2_ninth_surface_ratification_sitting.md`
> (2026-10-14). The corrections those records name are written in place by that dispatch, each line naming the
> record that ordered it, every former wording kept (#12). None of the nine acts changed what L2 computes. The specification
> set is ratified jointly again at the whole-architecture coherence review that ends the detail phase
> (`records/cowork/rulings/cowork_rulings_2026_10_04_l2_route_sitting.md` §2). The sentences above that say
> nothing in this file is ratified are kept as the record of the state before those acts and no longer
> describe the file.

---

## 0. Terms

Standard music theory is used in its standard sense. A reader who knows music theory and not this
project needs only this table. The reserved-word rule binds throughout: bare *key* means tonality (the
file uses *tonality*), bare *score* is a musical score, bare *note* is a pitch event, *figure* is the
figure of a chord, *root* is a chord root, *resolution* is the resolution of a dissonance, and *bar* is
the metric unit. The numerical sense of "score" is always written *candidate score*.

| Term | Meaning in this file |
|---|---|
| **The analysis** | The harmonic-analysis software this project builds. |
| **L0, L1, L2, L3** | The layers of the ratified charter (pack member 07). L0 is the notated record, the input contract. L1 publishes slices, the lowest sounding pitch per slice, metric strength, notated boundary evidence and cadence cues. (was: "L1 publishes slices, metric strength, notated boundary evidence and cadence cues."; cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 2) L2 is this file's subject. L3 reads further facts off L2's settled reading. |
| **The charter** | Pack member 07, the ratified statement of each layer's question, inputs and outputs. Given. |
| **The input contract** | The ratified specification of L0 and L1, cut for this session. Its statements are cited as **IC S-n**. Given. |
| **Event, onset, release, change point, slice, sounding set, silent slice** | As the input contract defines them (IC §0). An event is one sounding pitch from onset to release, with a tied group counting as one event. A change point is an onset or release of an eligible event. A slice is the half-open stretch between consecutive change points. The sounding set of a slice is the set of events sounding over it. |
| **Working span** | The stretch of music the caller asks the analysis to read. Output covers exactly this span, and music loaded beyond it is evidence only (D-260, pack member 05). |
| **Harmonic span** (or just *span*) | The charter's unit of L2's segmentation: a stretch of the working span between two boundaries, carrying one tonality and one chord. The input contract names it the same way ("L2's harmonic span", IC §0). |
| **Boundary** | A change point that L2 decides is the start of a new harmonic span. By the charter, the boundaries are a subset of L1's change points, plus the two span edges. |
| **Tonality** | Tonic, with its spelling, and mode. |
| **Chord** (as L2 decides it) | Four fields, following the charter. **Degree**: the scale step of the chord's root relative to the span's tonality, with any chromatic alteration, such as ♭II or ♯IV. **Quality**: major, minor, diminished, augmented, and the seventh-chord and augmented-sixth qualities. **Figure**: which chord member is in the bass, together with the seventh or other added members. **Applied target**: for an applied chord (V/V, viiø7/ii), the degree it is applied to, possibly recursively (V7/IV/III). |
| **Chord tone / elaboration** | A sounding event within a span is a chord tone of that span's chord or an elaboration. The elaboration relations L2 admits are passing, neighbour, suspension, anticipation, appoggiatura, escape tone, pedal point, and an explicit unclassified elaboration (L2-S8). (was: "The charter's elaboration relations are passing, neighbour, suspension and anticipation."; cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling 1) |
| **Assignment** | The chord-tone or elaboration decision for one event within one span, with its relation where it is an elaboration. |
| **Reading** | One complete candidate answer for the working span. It consists of a segmentation into harmonic spans, and per span a tonality, a chord, and an assignment for every event sounding in it. |
| **Admission rule** | The rule that decides which readings the search may consider at all (charter, L2). |
| **Candidate score** | The number the analysis assigns to a reading. Higher means preferred. It is a sum of **terms**, each a function of the reading and the published evidence. |
| **Term, term weight** | A term is one component of the candidate score, such as "how well the span's notes fit the chord". A term weight is the number a term is multiplied by. (was: "**Term, weight** … A weight is the number a term is multiplied by."; written at the ratification of the ninth surface, cowork_rulings_2026_10_14_l2_ninth_surface_ratification_sitting.md, item 10) |
| **Fit, held-out** | Fitting sets weights from annotated music. Held-out music is kept out of the fit and used only to measure. |
| **Rival** | An alternative reading published beside the chosen one. |
| **Mass** | The share a rival carries in the publication. Its meaning is fixed at L2-S40. (was: "The weight a rival carries in the publication."; written at the ratification of the ninth surface, cowork_rulings_2026_10_14_l2_ninth_surface_ratification_sitting.md, item 10) |
| **The ledger** | Pack member 09, the empirical findings ledger. Its entries are cited **C-n**. |
| **Design-intent entry** | A ratified entry of pack member 05, cited **D-n**. |
| **FACT / THEORY / CONJECTURE** | The brief's labels. **This session fetched no paper.** Every FACT below is therefore a *relayed* FACT: stated in pack member 08's extract, which records that it was read at the object and quotes the page. This matches the input contract's own definition of FACT (IC §0). It is weaker than a FACT this session read itself, and the label **FACT (relayed, 08)** says so wherever it is used. |
| **RULED** | A claim fixed by the charter, by the input contract or by a design-intent entry, cited by its identifier. |
| **Source class** | *derived*, *given* (split below as *given — charter*, *given — input contract*, *given — design intent*), or *measured*. A *measured* statement rests on a measurement or fit this session cannot make, and carries no value. |
| **OQ-L2-n** | An open question, collected in §4. |

---

## 1. The subject, and a finding on the brief's decomposition

**The subject**, from the brief: *how does this layer reach its one decision from what L0 and L1
publish, in what form does it publish the decision and its rivals, and what does it never do?*

**Finding on the decomposition.** Faces (a) to (h) of the brief work as a checklist. The session
wrote to them, and every face receives statements in §3. Three things they leave out, or split in a
way that hides something, are recorded here and repeated in §7.

1. **Faces (b) to (e) are four views of one object.** The candidate score does not have a boundary
   part, a tonality part, an elaboration part and a chord part that can be specified independently.
   Several terms read two or three of the four at once. The clearest case is the elaboration term
   (L2-S33), which has to see the chord of the neighbouring span. The session therefore writes the
   admission rule and the terms of the candidate score (faces (a) and (f)) as the load-bearing
   statements. Faces (b) to (e) mostly say what each of those statements implies for one of the four
   published fields.
2. **Inference is missing as a face.** The charter forbids discarding a rival before the whole
   sequence has been scored. Together with a large joint state (tonality × chord × figure × applied
   target × boundary), that makes *how the search is carried out* a design point in its own right. It
   decides whether the no-discarding rule can be kept at all. It is written at L2-S35 and L2-S36.
3. **The order the analysis works in, notated or unfolded, is L2's.** The input contract hands the
   rest of its OQ-1 to L2's surface (IC §4, OQ-1). None of faces (a) to (h) names it. It is written at
   L2-S46.

---

## 2. How to read a statement

Each statement has the six fields of the brief, §4:

1. **Statement.**
2. **Defense.** Each load-bearing claim is labelled FACT (relayed, 08), THEORY, CONJECTURE or RULED.
3. **Source class.**
4. **Status.**
5. **Premise, and the premise's false-negative path.**
6. **Falsifier.** For a statement about behaviour, this is CODE: an observable, a decision rule, and a near-miss that does not falsify. For a modelling premise with no code site, it is RESIDUAL.

"Exemplar n" means staged file n of the brief's §3.2. The exemplars are met as cases and never
counted (see §6). Where a statement leans on one, the case is named and its role is illustration,
never evidence of a rate.

---

## 3. The statements, face by face

### 3a. Face (a) — the candidate readings, and the rule that admits them

**L2-S1. A reading of the working span has exactly these parts. (i) An ordered partition of the
span into harmonic spans, each starting at a span edge or at one of L1's change points. (ii) Per span,
a tonality: a spelled tonic and a mode. (iii) Per span, a chord: degree with alteration, quality,
figure, and an applied-target chain that may be empty. (iv) Per event sounding in the span, an
assignment: chord tone, or elaboration together with its relation. The search's unit is the whole
reading, not a span.**
- *Defense.* Parts (i) to (iv) are the charter's publication list, read as the structure of one
  object [RULED — charter, L2 "Publishes"]. The whole reading is the unit because the charter forbids
  discarding a rival before the whole sequence of spans has been scored [RULED — charter, L2 "May
  not"]. A span-by-span unit would decide each span before its successors are seen. That is the case
  the ledger records, where a locally informed objective has a wrong reading as its optimum [FACT —
  ledger C45, reading one]. The tonic is spelled because L0 supplies spelled pitch [RULED — charter,
  L0; IC S-3], and because a spelled tonality distinguishes readings the notation distinguishes
  (C♯ major against D♭ major, and a German sixth against a dominant seventh). One published key
  finder uses exactly 42 spelled tonalities (seven letters × ♮, ♯, ♭ × two modes) and calls spelling a
  "thoughtful choice by the composer" [FACT (relayed, 08) — Feisthauer et al. 2020, p. 324, p. 327].
- *Source class.* Given (charter) for the four parts and the no-discarding rule. Derived for spelling
  the tonic.
- *Status.* Settled.
- *Premise.* The charter's four parts are everything a reading contains. **False-negative path:** a
  reading element an analyst writes that none of the four holds. The exemplars show two. The first is a
  suspension or retardation written *into the chord label*: exemplar 3's `V7(4)/iv` followed by
  `V7/iv`, and exemplar 1's `V2(4)`. Under L1 these become one chord plus an elaboration assignment, so
  nothing is lost, but the annotation's boundary where the suspension resolves has no L2 counterpart.
  See L2-S14 and OQ-L2-7. The second is a pivot chord written in two tonalities: exemplar 2, bar 41,
  `N6 F: IV6`, and exemplar 5, bar 1, `V2/IV F: V2`. See L2-S19.
- *Falsifier.* CODE. **Observable:** L2's published record for any working span. **Decision rule:**
  falsified if a published reading lacks any of the four parts, if a span starts at a position that
  is neither a span edge nor a published change point, or if the publication is assembled span by span
  with no whole-reading object behind it. **Not falsified by:** a span whose applied-target chain is
  empty, or a silent span whose chord field carries a named reason (L2-S44).
- *Ruled (cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling 2).* Stands as derived. "L2's
  tonic is **spelled**: seven letters, each natural, sharp or flat — the 42 tonalities of L2-S6 with the two
  modes. L2-S1(ii) and L2-S6 stand as derived on this point."
- *Ruled (cowork_rulings_2026_10_07_l2_reading_parts_sitting.md, Ruling 1).* "L2's algorithm as its statements
  define it is unchanged; L2-S1's wording does not change."
- *Pointer (written at the ratification of face (a), cowork_rulings_2026_10_13_l2_face_a_ratification_sitting.md,
  C6).* The crossing-elaborations item under OQ-L2-3 in §4
  (cowork_rulings_2026_10_09_l2_crossing_elaborations_sitting.md, Ruling 2) measures whether part (iv)'s
  "elaboration together with its relation" is decided inside the candidate score or read off the decided
  reading afterwards.

**L2-S2. The admission rule is specified as a closure test before it is specified as a list. Every
reading a published analysis writes for a passage of the grading repertoire must be admissible,
whether that analysis's principal reading or a recorded variant. A reading type that some analyst
writes and the rule does not admit is excluded only by a named ruling that carries the ceiling cost
it imposes.**
- *Defense.* The charter says in terms that a reading the search cannot reach cannot be found however
  good the scoring is, so the admission rule bounds every claim about the analysis's own ceiling
  [RULED — charter, L2]. One published system measures the two quantities separately. It reports the
  share of frames whose correct label is among the admitted candidates as the "ratio of correctness",
  the system's theoretical maximum, and shows the output falling as that ratio rises with more
  same-source candidates [FACT (relayed, 08) — Rocher et al. 2010, Table 1, p. 144]. **So ceiling and
  output are different quantities, and only the ceiling is the admission rule's to fix.** Published
  analyses carry recorded variants in the same stream [FACT — ledger C16; exemplar 5 carries `m5var1`,
  `m11var1`, `m14var1`, `m17var1`, `m18var1`, `m19var1` and `m31var1`, read at the file]. The
  project's grading bar for tonality counts a match to any recorded reading as defensible [RULED —
  D-352]. A variant the search cannot reach can therefore never be matched.
- *Source class.* Derived.
- *Status.* Settled as the form of the rule. The list it implies is L2-S4 to L2-S8, and the
  measurement that closes the list is OQ-L2-1 (L2-S8's part settled by the elaboration-relations record's
  Ruling 1). (was: "… and the measurement that closes the list is OQ-L2-1."; written at the ratification of
  face (a), cowork_rulings_2026_10_13_l2_face_a_ratification_sitting.md, C8)
- *Premise.* The grading repertoire's published analyses are the population the ceiling is defined
  over. **False-negative path:** a reading no published analysis writes, which a competent analyst
  would. The closure test cannot see it. It is recorded as the test's blind side, and principle #21's
  point that ground truth is itself an instrument applies.
- *Falsifier.* CODE. **Observable:** for each annotated span in the grading corpora, whether the
  annotated reading, converted to L2's four fields, is a member of the admitted set. **Decision
  rule:** falsified if any annotated reading is not admissible and is not on a ruled exclusion list
  with its stated cost. **Not falsified by:** an annotated reading that is admissible and scored low,
  which is the candidate score's error and not the admission rule's.
- *Ruled (cowork_rulings_2026_10_05_l2_chord_vocabulary_sitting.md, Ruling 1).* Stands as derived. The
  ruling is quoted beside L2-S4 (#6).
- *Beside L2-S2 (cowork_rulings_2026_10_05_l2_cadential_six_four_sitting.md, Ruling 1) — the named
  exclusion.* "The third candidate DP-N lists — the six-four as its own category (`Cad64`) — is **not a
  state** in the first specification. This ruling is the named exclusion L2-S2 requires of a reading type an
  analyst writes, so that L2-S2 is met whether or not a grading corpus turns out to write `Cad64` (whether
  one does is unsettled; surface §3). **Its ceiling cost, as stated:** a ground-truth `Cad64` is matched
  only if the grading reads it as one of the two rivals; the cost is not counted."
- *Beside L2-S2 (cowork_rulings_2026_10_05_l2_silence_and_no_chord_sitting.md, Ruling 1) — the named
  exclusion.* ""No chord" over sounding music is not an admissible reading in the first specification. This
  ruling is the named exclusion the derivation's L2-S2 requires of a reading type an analyst writes, so that
  L2-S2 is met whether or not a graded collection turns out to write a no-chord label (unsettled; surface
  §3). **Its cost, as stated:** such a label would never be matched; the cost is not counted."

**L2-S3. No chord is excluded under any tonality. A chord whose pitches are foreign to the span's
tonality is admitted and costs more in the candidate score.**
- *Defense.* The charter fixes the coupling between tonality and chord as a cost, never a veto, and
  generalises it: "a reading-shaped evidence producer is a score and never a constraint" [RULED —
  charter, L2]. Its ground is a measured result: "adding a compatibility between chords and keys has
  led to a decrease of accuracy", because "an incorrect chord selected may discard the correct key
  (and vice versa)" [FACT (relayed, 08) — Rocher et al. 2010, p. 143]. Two further systems keep every
  label reachable under every tonality: "No chord is excluded from any tonality; a non-diatonic chord
  is merely less probable" [FACT (relayed, 08) — Catteau, Martens & Leman, pp. 8, 12–14; Raphael &
  Stoddard 2003, p. 3]. The exemplars show the case the veto would break. Exemplar 5's bar 28 reads a
  major tonic in D minor (`I ||`, a Picardy close), and the published study of the chorales reports
  Picardy-third final cadences outnumbering plain minor ones about ten to one [FACT (relayed, 08) —
  de Clercq, pp. 196–197].
- *Source class.* Given — charter.
- *Status.* Settled.
- *Premise.* A finite cost is always enough to express "unlikely here". **False-negative path:** a
  cost so large that it acts as a veto in practice. It would be caught by L2-S2's closure test, since
  an annotated reading would then be admitted yet never appear in any published rival list.
- *Falsifier.* CODE. **Observable:** the admitted set under a fixed tonality. **Decision rule:**
  falsified if any chord of the vocabulary is absent from it for some tonality, or if the
  tonality–chord cost is infinite for any pair. **Not falsified by:** a large finite cost.
- *Ruled (cowork_rulings_2026_10_07_l2_four_agreeing_statements_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; no wording of L2-S3, L2-S9, L2-S15 or L2-S21 is changed by this ruling."
- *Pointer (written at the ratification of face (a), cowork_rulings_2026_10_13_l2_face_a_ratification_sitting.md,
  C6).* The structural-bass item under OQ-L2-3 in §4 (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md,
  Ruling 3) records that the old bass-degree rule's "never a gate" survives under this statement.

**L2-S4. The chord vocabulary the admission rule ranges over contains at least these classes:
(i) the four triad qualities on every diatonic and chromatically altered degree; (ii) the five
seventh-chord qualities (dominant, major, minor, half-diminished, fully diminished) on every degree;
(iii) the Neapolitan, as ♭II major; (iv) the three augmented sixths; (v) every figure of each: root
position, the inversions, and for sevenths the three inversions with the seventh.**
- *Defense.* The two published readings of exemplar 1's piece, and the published readings of
  exemplars 3 and 5, use chords of every class above: `V65/V`, `viio6`, `V7`, `iio`, `ii%65`, `N6`,
  `III+6`, `viio7/V`, `IVM7/III` [FACT at the files — exemplars 1, 2, 3 and 5]. That establishes the
  classes as needed, not as sufficient. The classes are the standard common-practice harmonic
  vocabulary [THEORY]. One published symbolic system's vocabulary was 12 roots × {major, minor,
  diminished} × {no added note, fourth, sixth, seventh}, plus augmented sixths and suspended chords
  [FACT (relayed, 08) — Masada & Bunescu, p. 4]. Its one generic seventh ("a C major seventh chord and
  a C dominant seventh chord are mapped to the same label") is too coarse for a spelled analysis, since
  the published readings distinguish `IVM7` from `IV7`.
- *Source class.* Derived.
- *Status.* **Open** on whether the vocabulary is complete (OQ-L2-1). Settled that it contains at least
  these classes.
- *Premise.* Chords outside these classes are rare enough in the repertoire to be handled by the
  closure measurement. **False-negative path:** ninth chords, added-sixth chords and eleventh
  sonorities. Exemplar 3 writes a ninth as a suspension (`iv7(9)`) and an eleventh as a retardation
  figure (`ii%65(119)`), so the annotation tradition treats them as elaborations, and they reach L2 as
  elaboration assignments (L2-S8). An added-sixth chord and a seventh chord on the related root share
  their pitch-class content [FACT — ledger C6]. Whether the vocabulary needs an added-sixth class
  separately is part of OQ-L2-1.
- *Falsifier.* CODE. **Observable:** the vocabulary list. **Decision rule:** falsified if any class
  above is missing. **Not falsified by:** additional classes admitted after OQ-L2-1's measurement.
- *Ruled (cowork_rulings_2026_10_05_l2_chord_vocabulary_sitting.md, Ruling 1).* Stands as derived. "For L2's
  specification, every chord kind the vocabulary lists is its own state, choosable and publishable however
  rare — the German, French and Italian sixths each, an applied chain such as V7/IV/III. Where a kind's
  count is below the capacity threshold, its **table estimates** borrow from its declared parent class
  (D-271 item 2's first sentence, which already does this for every table cell), and D-533 keeps a rare
  continuation from scoring as impossible. **D-271's last sentence of item 2 — "The degree vocabulary's
  rare-class pooling (factorization §1) is the same rule applied to the state space itself" — does not carry
  into L2's specification.** D-271's register status is settled at the ratification act, not here (the shape
  the second family used for D-385 and the third for D-333). **L2-S2, L2-S4 and L2-S5 stand as derived**;
  L2-S4's and L2-S5's "Open … (OQ-L2-1)" stay open, the measurement unchanged."
- *Beside L2-S4 (cowork_rulings_2026_10_05_l2_chord_vocabulary_sitting.md, Ruling 1) — carried.* "One
  sentence of a rule the user ratified is set aside for L2; the state is larger, which adds to the
  tractability question OQ-L2-8 ★ (its own surface); a rare kind's precision is bounded by its parent's
  estimates until more annotated music exists, a bound stated (#24)."
- *Beside L2-S4 (cowork_rulings_2026_10_05_l2_chord_vocabulary_sitting.md, Ruling 1) — carried, what it does
  not decide.* "The vocabulary's completeness and the applied chain's maximum depth (OQ-L2-1, a
  measurement); where in the phases that measurement runs; the declared parent classes themselves (the fit's
  detail); tractability (OQ-L2-8 ★)."
- *Beside L2-S4 (cowork_rulings_2026_10_05_l2_chord_vocabulary_sitting.md, Ruling 2).* "For the first L2
  specification, the chord vocabulary carries no added-note classes: a sounding ninth, eleventh or
  thirteenth over a chord is an **elaboration assignment**, with its named relation or the unclassified
  elaboration (the second family's Ruling 1). Whether an added-sixth class is needed is decided by the
  closure measurement (OQ-L2-1). **The extended chords that jazz treats as chord members — the ninth,
  eleventh and thirteenth chords with their altered forms (♭9, ♯9, ♯11, ♭13), and the power chord D-334
  keeps — are written into that specification as a named increment, in the shape of the 2026-10-04 mode
  ruling:** theory-built tables whose source is read on our side (#1); a premise-ledger entry with the
  near-neighbour hazard enumerated (a ninth chord against a seventh chord with a ninth suspension, #17e); a
  desk simulation (#17c); a grading convention; held-out jazz ground truth for the evaluation (#20, D-500).
  **Its trigger is the premise-ledger entry**, so it may land with a declared bound before jazz ground truth
  exists; **L2-S4 stands as derived.**"
- *Beside L2-S4 (cowork_rulings_2026_10_05_l2_chord_vocabulary_sitting.md, Ruling 2) — the user's
  qualification, recorded as he gave it.* "**The user's qualification, recorded as he gave it:** this ruling
  may change when the jazz increment is taken up. *This side's reading of it:* the first specification's
  choice is not offered as the final vocabulary; the increment's own act is where it is revisited, with
  whatever its premise ledger and desk simulation show — no ruling now binds that act's outcome."
- *Beside L2-S4 (cowork_rulings_2026_10_05_l2_chord_vocabulary_sitting.md, Ruling 2) — carried.* "Until the
  increment lands, a jazz `Cmaj9` reads as `Cmaj7` with the ninth as an elaboration, most likely the
  unclassified one (the surface's reading). Row 21.77's rule is narrowed for L2: everything found is stated,
  as chord plus assignments rather than in the chord's name."
- *Beside L2-S4 (cowork_rulings_2026_10_07_l2_chord_tone_membership_sitting.md, Ruling 2) — carried to the
  jazz named increment's premise list, with the user's condition.* "**Carried to the jazz named increment's
  premise list (chord-vocabulary Ruling 2 of 2026-10-05), with the user's condition as part of it:** whether
  a bass line's passing notes (a walking bass, for example) mislead the chord reading, and if so what
  remedies it. **The bass is a musical function, not an instrument:** it may be a keyboard player's left
  hand (piano, accordion, harp, organ, harpsichord), an upright bass, a guitar, a bassoon or any other part.
  **Which part carries the bass line is most likely not determinable**, whether meant as heard or as
  composed. No remedy may rest on naming a bass instrument; where a remedy needs a bass line, identifying it
  is itself a reading carried with its rivals, not a notated fact (the same footing as L2-S28's structural
  bass, and D-389's line between a notated voice and an inferred line)." *The user's words, as the record
  quotes them:* "A. BUT we will most likely not be able to "tell" who is subjectively (or compositonally)
  the "bass". It must not be any specific instrument - could be a pianist's/accordeonists/
  harpists/organist's/cembalist's left hand, an upright bass, a guitar, a basssoon or whatever."

**L2-S5. The applied target is a chain, not a single field. A chord may be applied to a degree that
is itself taken as a temporary tonic of another applied reading (V7/IV/III), and the admission rule
fixes the chain's maximum depth as a ceiling decision under L2-S2.**
- *Defense.* Exemplar 3's published analysis writes `V7/IV/III` [FACT at the file, in the eighth bar
  element, bar 7 if the opening incomplete bar is counted as bar 0]. That is a dominant seventh of the subdominant of the relative major, a
  chain of depth two. The charter's chord field includes "applied target" without a depth bound
  [RULED — charter]. Any fixed depth is an admission decision with a ceiling cost, so it belongs under
  L2-S2's test.
- *Source class.* Derived.
- *Status.* Settled that depth two is admitted. **Open** on the maximum (OQ-L2-1).
- *Premise.* Depth-two chains occur and deeper ones are rare. **False-negative path:** a sequence of
  applied chords in a chromatic passage written at depth three. The closure measurement finds it.
- *Falsifier.* CODE. **Observable:** the admitted chord set. **Decision rule:** falsified if
  `V7/IV/III` under a minor tonality is not admissible. **Not falsified by:** a low candidate score for
  it.
- *Ruled (cowork_rulings_2026_10_05_l2_chord_vocabulary_sitting.md, Ruling 1).* Stands as derived. The
  ruling is quoted beside L2-S4 (#6).

**L2-S6. The tonality vocabulary is the spelled tonics (seven letters, each natural, sharp or flat)
in two modes, major and composite minor. A mode other than these is not admitted until the named
increment's gate is passed (beside this statement).**
- *Defense.* Spelling, as in L2-S1. Two modes: the project's grading ground truth is major/minor only,
  and it counts "a modal passage the major/minor-only ground truth cannot represent" as a genuinely
  ambiguous case [RULED — D-352]. The published key finder uses the same 42 spelled tonalities [FACT
  (relayed, 08) — Feisthauer et al. 2020, p. 327]. On modal chorale melodies, one published study
  reports the literature split. One position analyses them with modal paradigms, and another holds
  that only the melody is modal while "Bach sets the melody in a patently tonal harmonic context".
  The study takes neither side [FACT (relayed, 08) — de Clercq, p. 195, on Burns and Renwick].
- *Source class.* Derived.
- *Status.* Settled for the 42 spelled tonalities. Settled for the first specification at two modes, major
  and composite minor, with the modal extension named as an increment (beside this statement). **Open** for
  tonics that need a double accidental (OQ-L2-1). (was: "**Open** for modes (OQ-L2-2) and for tonics that
  need a double accidental (OQ-L2-1)."; cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling
  1)
- *Premise.* The repertoire's tonalities are major or minor with at most one accidental on the tonic.
  **False-negative path:** a Phrygian close or a modal chorale tune read in its mode by an analyst. It
  becomes an admitted tonal reading plus an unrepresentable modal one, and the closure test reports
  it as an exclusion with a cost.
- *Falsifier.* CODE. **Observable:** the tonality set. **Decision rule:** falsified if any of the 42 is
  missing, or if any other mode is admitted before the named increment's gate is passed (was: "before
  OQ-L2-2 is ruled"; cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling 1). **Not falsified
  by:** a Phrygian cadence read as iv6–V in minor, which is an admitted reading.
- *Beside L2-S6 (cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling 1).* "L2's tonality
  vocabulary in the first L2 specification is **two modes, major and composite minor** (the composite minor
  practice: natural, harmonic and melodic as one tonality with variable sixth and seventh degrees, as D-524
  states it). Modal evidence reaches the user through D-276's counted, un-rounded per-degree inflections,
  never through an inferred mode label. **The modal extension is written INTO that first specification as a
  named increment, not left to a later idea:** the modes in order — Dorian and Mixolydian first; Phrygian
  and Lydian as the next pair; Aeolian is minor's natural variant and needs no state; Locrian is out on
  musical grounds (no stable tonic triad) — and what each needs before it is admitted as a tonality: a
  theory-built pitch profile and chord-expectation table whose source is read on our side (#1; D-531 is the
  precedent for a confirmed hand-built table; Levine's *Jazz Theory Book*, reached through the Modal Harmony
  Ontology, is a candidate source, not yet read); a premise-ledger entry with the near-neighbour flip's
  false-negative path enumerated (#17e — Mixolydian against major, Dorian against minor, each one degree
  apart; Row 23.269 records the legacy decoder declaring "Mixolydian briefly" on an isolated dominant
  seventh; OI-174 is the same shape one scale further out); a desk simulation on real cases (#17c); a
  grading convention for church modes ruled in measurement design — the DCML standard's own same-tonic
  reduction (Dorian and Phrygian to minor, Lydian and Mixolydian to major), which is NOT D-210's
  parent-collection rule and needs its own ruling; and held-out ground truth outside the DCML standard for
  the evaluation (#20), which the jazz corpus of D-500 is meant to supply. **The trigger is the
  premise-ledger entry:** the increment may land as a declared-bound increment (#24, second paragraph)
  before modal ground truth exists, and is measured when it does."
- *Ruled (cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling 2).* Stands as derived. "L2's
  tonic is **spelled**: seven letters, each natural, sharp or flat — the 42 tonalities of L2-S6 with the two
  modes. L2-S1(ii) and L2-S6 stand as derived on this point."
- *Ruled (cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling 1).* Stands as derived.
  "**L2-S6 stands as derived**, its status line amended from "Open for modes (OQ-L2-2)" to settled for the
  first specification with the increment named, and its falsifier's clause "before OQ-L2-2 is ruled"
  replaced by "before the named increment's gate is passed"."
- *Beside L2-S6 (cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling 1) — the user's
  principle, recorded with the ruling.* "The user's stated principle, recorded with this ruling in his
  words: *jazz is a common use case the final product supports; the question on modes is when and not if;
  and lack of ground truth, where good methods exist for recognizing a mode, is not an acceptable ground for
  leaving it out — only the absence of any method would be.*"
- *Beside L2-S6 (cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling 2) — carried,
  UNSETTLED, not filled.* "whether Ruling 2 of 2026-08-29 reaches `FRAMEWORK.md` §0's term definitions;
  which act Row 10.8's "(ratified)" names; OQ-L2-1 (double accidentals) and OQ-L2-17 (enharmonic
  modulation), which stay open as the derivation leaves them; D-494's "enharmonic-identity rule for key
  spans" (index line only, not opened)."
- *Amended at the ratification of face (a) (cowork_rulings_2026_10_13_l2_face_a_ratification_sitting.md, C1).*
  The statement's "major and minor" and "until the question is ruled (OQ-L2-2)" are replaced by the
  tonality-vocabulary record's own words — "major and composite minor", and the named increment's gate, as its
  Ruling 1 already replaced the parallel clause of the *Falsifier*
  (cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling 1). The statement read: "in two modes,
  major and minor. A mode other than these is not admitted until the question is ruled (OQ-L2-2)." The derived
  wording stands at the derivation, L2-S6.

**L2-S7. Any subset of L1's change points may be the boundary set of a reading. No regularity of
harmonic rhythm or segment length is an admission rule. Each such regularity is a term of the
candidate score. If a maximum span length is imposed for tractability, it is an admission rule, it
carries L2-S2's ceiling statement, and it is set no shorter than the longest span any annotation of
the grading repertoire writes.**
- *Defense.* The charter makes boundaries a subset of change points and nothing more [RULED —
  charter]. It also says why a stylistic regularity must not be a rule: a hard constraint "lets one
  wrong answer delete the other question's right one" [RULED — charter, L2]. The published
  enumerate-then-filter system took "harmonic rhythm cannot be syncopated" as a hard rule and records
  its own exceptions in one of its two corpora, describing its rules as "'over fit' to chorale music"
  [FACT (relayed, 08) — Condit-Schultz, Ju & Fujinaga, §3]. The published semi-Markov systems bound
  segment length for cost. One states its bound only as a symbol L, and the other states none and
  reports quadratic cost [FACT (relayed, 08) — Masada & Bunescu, p. 3; Yang, Cwitkowitz & Duan 2023,
  §6]. A bound shorter than a real prolongation would make that prolongation unreachable.
- *Source class.* Derived.
- *Status.* Settled. The bound's value, if any, is *measured* (OQ-L2-3).
- *Premise.* The joint search stays tractable without a tight length bound (see L2-S36). **False-negative
  path:** a tractability failure that forces a bound shorter than a real span. It is visible as a
  closure-test failure and must be ruled, not silently set.
- *Falsifier.* CODE. **Observable:** the boundary sets reachable for a given slice list. **Decision
  rule:** falsified if some subset of change points is unreachable other than through a declared
  maximum span length. **Not falsified by:** a subset reachable and scored low.
- *Beside L2-S7 (cowork_rulings_2026_10_07_l2_any_boundary_set_sitting.md, Ruling 2).* The item this ruling
  adds to OQ-L2-3's list of held-out measurements — the form of a chord's own length in the candidate score
  — which this statement's *Status* names, is quoted beneath OQ-L2-3 in §4.
- *Ruled (cowork_rulings_2026_10_07_l2_any_boundary_set_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; L2-S7's wording is unchanged."

**L2-S8. The elaboration relations admitted are passing, neighbour, suspension, anticipation,
appoggiatura, escape tone, pedal point, and an explicit unclassified elaboration. Retardation is a
suspension that resolves upward — a kind of suspension, not a name of its own.**
- *Defense.* The charter lists four relations [RULED — charter, L2]. It does not say whether the list
  is exhaustive. The published enumerate-then-filter system uses seven contrapuntal models: passing,
  neighbour, suspension/retardation, appoggiatura, escape tone, pedal tone and double passing [FACT
  (relayed, 08) — Condit-Schultz, Ju & Fujinaga, §3]. The exemplars write appoggiaturas as grace notes
  (exemplar 3, `<appoggiatura/>`, read at the file), and exemplar 3's analysis writes retardations
  upward (`i(^2)`) [FACT at the file]. A reading that must call an appoggiatura a "neighbour" or a
  "suspension" is forced into a wrong relation. Admitting no relation for it would force it to be a
  chord tone.
- *Source class.* Given — charter, for the four. Derived, for the want.
- *Status.* Settled: the ruled list (cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling
  1). (was: "**Open** on the list beyond the four (OQ-L2-4 ★).";
  cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling 1)
- *Premise.* The eight relations, with the unclassified elaboration as the residue, are enough for every
  elaboration an analysis of the repertoire writes for a single note. **False-negative path:** a figure named
  over several notes, such as a cambiata, which the per-note assignment of L2-S9 cannot carry as one
  relation; each of its notes then receives its own relation or the unclassified one. How often the
  unclassified elaboration fires is unknown (OQ-L2-13). (was: "The four relations cover the elaborations the
  charter meant. **False-negative path:** an appoggiatura or escape tone. It is either mislabelled or forced
  to be a chord tone, which then changes the chord."; written at the ratification of face (a),
  cowork_rulings_2026_10_13_l2_face_a_ratification_sitting.md, C2)
- *Falsifier.* CODE: the relation set equals the ruled list. (was: "RESIDUAL until ruled. Thereafter CODE:
  the relation set equals the ruled list."; cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md,
  Ruling 1)
- *Amended (cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling 1).* "The elaboration
  relations L2 admits in the first L2 specification are: **passing, neighbour, suspension, anticipation,
  appoggiatura, escape tone, pedal point, and an explicit unclassified elaboration.** **Retardation is a
  suspension that resolves upward** — a kind of suspension, not a name of its own. The appoggiatura and the
  escape tone are the two one-sided relations (leapt to and left by step; stepped to and left by leap);
  pedal point is D-207's class (a tone held or restruck against changing harmony, in any voice); the
  unclassified elaboration is a note the reading finds foreign to the chord that fits no named relation."
  *The derived wording stands at the derivation, L2-S8.*
- *Beside L2-S8 (cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling 1) — carried.* "(b)
  If the relations are part of the search state, each added relation enlarges it (L2-S23's premise; OQ-L2-8
  ★); if the names are read off the decided reading afterwards, the list costs the search nothing — the
  surface's reading, not a fact; which of the two is L2-S33's family's question (surface §A.5(a)). (c) How
  often the unclassified elaboration fires is unknown; no annotated corpus with per-note elaboration labels
  is known to the derivation (OQ-L2-13)."
- *Pointer beside the carried cost (b) above (written at the ratification of face (a),
  cowork_rulings_2026_10_13_l2_face_a_ratification_sitting.md, C4).* Which of the two holds is now decided by
  a held-out measurement: the crossing-elaborations item under OQ-L2-3 in §4
  (cowork_rulings_2026_10_09_l2_crossing_elaborations_sitting.md, Ruling 2).

**L2-S9. An assignment is made per event per span, not per event. An event that sounds across a
span boundary receives one assignment in each span it sounds in. A suspension, for example, is a
chord tone in the span where it is prepared and a suspension in the span where it dissonates.**
- *Defense.* A suspension is by definition a note held from a harmony in which it is a chord tone into
  a harmony in which it is not [THEORY]. The published rule set states the asymmetry in terms: "A note
  cannot start as a non-chord tone and then become a chord tone (though the opposite is possible, in
  the suspension)" [FACT (relayed, 08) — Condit-Schultz, Ju & Fujinaga, §3, melodic rule 3]. L1
  publishes events whole across slices, with a tied group as one event [RULED — IC S-23]. So one event
  can meet two harmonies, and a single per-event assignment could not express the suspension.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* A span-level assignment is fine-grained enough. **False-negative path:** an event whose
  role changes within one span. An example is a long note over which the harmony stays but the note
  becomes a seventh by the other voices' motion, and nothing in the notation marks the point. It is
  expressed only if a boundary is placed there, which L2-S14 permits when the figure changes.
- *Falsifier.* CODE. **Observable:** assignments of events that cross a boundary. **Decision rule:**
  falsified if such an event carries one assignment only, or if it is ever an elaboration in an
  earlier span and a chord tone in a later one because it *became* consonant (as opposed to a new
  event). **Not falsified by:** a suspension resolving within the span into a chord tone, which is a
  new event in the resolving voice.
- *Ruled (cowork_rulings_2026_10_07_l2_four_agreeing_statements_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; no wording of L2-S3, L2-S9, L2-S15 or L2-S21 is changed by this ruling."

**L2-S10. An event is a chord tone of a span only if its spelled pitch class is a member of the
span's chord, spelled. Membership does not imply chord tone, since a consonant elaboration is admitted
(a consonant passing tone, for example). A chord is admissible over a span whose sounding set lacks
its root, or lacks its third.**
- *Defense.* Spelled membership, because L0 supplies spelling and a chord is spelled (L2-S1). The
  published rule set lists "can there be consonant non-chord tones?" among the four sources of
  analytic ambiguity [FACT (relayed, 08) — Condit-Schultz, Ju & Fujinaga, §1.3]. The ledger: a reading
  whose root does not sound is not thereby wrong, and the published analysis makes such readings [FACT
  — ledger C1]. Where the defining third does not sound, no signal at that moment separates the
  readings [FACT — ledger C34]. Requiring the root or the third would therefore exclude annotated
  readings, which fails L2-S2.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Spelling is correct in the record. **False-negative path:** a respelled passing note (a
  ♯4 written as ♭5 for voice-leading reasons) whose spelling differs from the chord's member. It would
  never be a chord tone. The input contract publishes the spelling as written and grades nothing
  [RULED — IC Ruling 58 (i)]. An enharmonic-equivalence allowance at L2 is part of OQ-L2-1.
- *Falsifier.* CODE. **Observable:** assignments. **Decision rule:** falsified if an event whose
  spelled pitch class is not in the chord is assigned chord tone, or if a chord is refused over a span
  for lacking its root. **Not falsified by:** a chord member assigned elaboration.
- *Ruled (cowork_rulings_2026_10_07_l2_chord_tone_membership_sitting.md, Ruling 1).* Stands as derived.
  "**L2-S10 stands as derived; its wording does not change.** Spelled membership stays the condition for a
  chord tone. **L2's algorithm as its statements define it is unchanged.**"
- *Beside L2-S10 (cowork_rulings_2026_10_07_l2_chord_tone_membership_sitting.md, Ruling 1) — carried, not
  dropped (#12).* "Whether L2 admits an **enharmonic allowance** for chord-tone membership is decided by the
  closure measurement OQ-L2-1, as the derivation states ("an enharmonic allowance for chord-tone
  membership", derivation line 1205). L2-S10's share of OQ-L2-1 stays open; this ruling commissions
  nothing." "**A named gap, recorded with no route chosen:** OQ-L2-1 runs on the grading corpora it names
  and is not aimed at scores whose spelling was not written by a person (for example a score imported from
  MIDI, as Row 6.45 names). How often such a score's spelling leaves a chord unreachable is unmeasured.
  *(This side's reading of OQ-L2-1's design; whether any grading corpus was itself imported was not
  checked.)" *Declined:* "Alternative B (the row would wait on a measurement not aimed at its imported-score
  half); Alternative C (a weighed-spelling cost no ground truth could fit, #20, #21; resting on the
  unchecked premise that misspelling is common enough to matter, #18; settling from a surface what the
  derivation routed to a measurement, D-254)."
- *Beside L2-S10 (cowork_rulings_2026_10_07_l2_chord_tone_membership_sitting.md, Ruling 2).* The bass-line
  premise this ruling carries to the jazz named increment, with the user's condition that the bass is a
  musical function and not an instrument, is quoted beside L2-S4.
- *Beside L2-S10 (cowork_rulings_2026_10_07_l2_chord_tone_membership_sitting.md, Ruling 3) — carried.*
  "Carried: the phantom-root failure stays on record at Row 14.18 (proposed QUARANTINED); whether weighing
  alone keeps phantom roots away is a question for the measurement stage (this side's reading)."

### 3b. Face (b) — where one harmony gives way to the next

**L2-S11. A boundary is one of L1's change points, and where the boundaries fall is decided together
with the tonality, the chord and the assignments, in the one decision. It is never decided before the
chord or after it.**
- *Defense.* The charter: the segmentation's "boundaries are a subset of L1's change points" and
  segmentation is decided "with" chord identity (DP-C) [RULED — charter]. The input contract repeats it
  from L1's side: "at L2 the harmonic boundary is decided jointly with the tonality and the chord over
  L1's change points, as the charter's one entangled decision, never sequentially after the chord"
  [RULED — IC, beside S-28, Ruling 55].
- *Source class.* Given — charter (repeated by the input contract).
- *Status.* Settled.
- *Premise.* The change-point set is exhaustive, so no real harmony change falls between change
  points. **False-negative path:** none by construction [RULED — charter, L1 "Why a layer"; IC S-26].
- *Falsifier.* CODE. **Observable:** the published boundaries. **Decision rule:** falsified if a
  boundary lies at a position that is not a change point or span edge, or if the boundary set is
  computed by a pass that does not see candidate chords. **Not falsified by:** a boundary at a change
  point where only one voice moves.
- *Recorded (cowork_rulings_2026_10_06_l2_one_decision_sitting.md, §1d).* Stands as derived — recorded by
  the record as this side's derivation, not ruled; challengeable. "**The family is placed whole.** L2-S11
  stands as derived; no wording change is proposed."

**L2-S12. The metric strength class of a change point enters the candidate score as a term on
reading a boundary there. No metric level forbids a boundary. The term reads the class and its period
as L1 publishes them. Its weights are fitted per class, and none is set here.**
- *Defense.* Harmonic change was counted at 71.5% of beats at the level above the tactus, 22.3% at the
  tactus and 2.4% at the level below [FACT (relayed, 08) — Temperley 2009, Table 1, p. 6; the charter
  carries the same figures, RULED]. The lowest figure is small but not zero, so a rule forbidding
  sub-tactus boundaries would exclude real changes. The paper that imposes exactly that restriction
  states its cost as "only a small loss of accuracy" and gives no value [FACT (relayed, 08) —
  Temperley 2009, p. 7]. A fixed coarse grid "results in a somewhat overanalyzed labeling" when refined
  [FACT (relayed, 08) — Raphael & Stoddard 2003, p. 5]. Removing all metrical-accent features from a
  segmental system lowered segment F-measure from 77.6 to 71.2 on one fold set [FACT (relayed, 08) —
  Masada & Bunescu, Table 5, p. 8]. The class and its period are L1's published facts, and a per-slice
  weight is "a consumer's fitted derivative, never published by L0 or L1" [RULED — IC beside S-35,
  Ruling 47].
- *Source class.* Derived for the shape. *Measured* for the weights: the fit needs annotated boundaries
  on the grading corpora, with the class of each change point, and a held-out split. **UNESTABLISHED;
  no value.**
- *Status.* Settled for the shape. **Open** for the values (OQ-L2-3). (was: "Settled for the shape. **Open**
  for the values."; written at the ratification of face (b),
  cowork_rulings_2026_10_13_l2_face_b_ratification_sitting.md, correction 2)
- *Premise.* The three-level gradient holds on this repertoire (tested under OQ-L2-3, as the metric-strength
  record carries it). That is the input contract's own unestablished premise, which it hands to "L2's
  calibration" [RULED — IC beside S-35, Ruling 47]. **False-negative path:** a repertoire whose gradient is
  flat (continuous Baroque textures). The fitted weights would then be near equal, which the fit shows rather
  than hides. (was: "The three-level gradient holds on this repertoire."; written at the ratification of face
  (b), cowork_rulings_2026_10_13_l2_face_b_ratification_sitting.md, correction 2)
- *Falsifier.* CODE. **Observable:** the admitted boundary sets and the boundary term. **Decision
  rule:** falsified if a boundary at an off-grid or lowest-level change point is inadmissible, or if
  the term reads anything other than L1's class and period. **Not falsified by:** a very low fitted
  weight on weak classes.
- *Ruled (cowork_rulings_2026_10_07_l2_metric_strength_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; no statement's wording changes."

**L2-S13. L1's notated boundary evidence enters as terms on a boundary reading: the flags with their
scope, the positioned marks and the per-voice relations. An absent flag is never read as an absent
boundary. No flag forces or forbids a boundary.**
- *Defense.* The evidence and its form are L1's published list [RULED — IC S-39, S-41, S-50]. The input
  contract states in terms that "an absent flag is never read as an absent boundary" [RULED — IC beside
  S-39, Ruling 48]. The notated evidence is phrase-shaped, not harmony-shaped. The ground truth writes a
  phrase boundary where the harmony does not change and restates the chord [RULED — charter DP-J].
  Exemplar 5 shows the same shape: `m12 I || b4 I` and `m4 I || b4 G: I` [FACT at the file]. A fermata
  is not the cadential arrival's exact place. The published chorale study took "the cadential arrival
  (if any) as the last change of harmony at or before the fermata", with the arrival shifting to the
  strong beat before a weak-beat fermata when the melody allows [FACT (relayed, 08) — de Clercq,
  pp. 192–193]. So the evidence bears on the likelihood of a boundary *near* the flag, not only at it.
- *Source class.* Given — input contract, for the evidence and for "absent is not absent". Derived,
  for its role as terms.
- *Status.* Settled.
- *Premise.* Notated punctuation correlates with harmonic boundaries without coinciding with them.
  **False-negative path:** a flag at a change point where the harmony continues (the restated tonic
  after a fermata). The term then pulls toward a boundary the reading does not need. The fit weighs it.
- *Falsifier.* CODE. **Observable:** readings with and without flags present. **Decision rule:**
  falsified if removing every flag from a passage makes some reading inadmissible, or if adding a flag
  makes some reading inadmissible. **Not falsified by:** the candidate scores changing.
- *Beside L2-S13 (cowork_rulings_2026_10_07_l2_notated_boundary_evidence_sitting.md, Ruling 2).* The item
  this ruling adds to OQ-L2-3's list of held-out measurements — whether a notated boundary flag, with its
  scope, is a term on the elaborations that cross that boundary — is quoted beneath OQ-L2-3 in §4. The flags'
  weights are measured under OQ-L2-3 as well: the record carries forward "the flags' weights (OQ-L2-3)".
  (Sentence added at the ratification of face (b), cowork_rulings_2026_10_13_l2_face_b_ratification_sitting.md,
  correction 2.)
- *Ruled (cowork_rulings_2026_10_07_l2_notated_boundary_evidence_sitting.md, Rulings 1 and 2;
  cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md, Ruling 4, stated with the question).* Ruling 1:
  "L2's algorithm as its statements define it is unchanged; no statement's wording changes." Ruling 2: "L2's
  algorithm as its statements define it is unchanged now; L2-S13's, L2-S31's and L2-S33's wordings are
  unchanged." Nothing-from-L3 Ruling 4: "this confirmation changes nothing in L2's algorithm as its statements
  define it (L2-S13 reads L1's boundary flags; L2-S49 reads nothing L3 publishes, harmonic rhythm included;
  both wordings unchanged)".

**L2-S14. Two adjacent spans never carry the same tonality and the same chord (degree, quality,
figure and applied target all equal). A change of figure alone, such as V6 to V65, is a change of
chord and may be a boundary. A change in which notes are elaborations, with the chord unchanged, is
not a boundary.**
- *Defense.* The published enumerate-then-filter system discards any interpretation in which "the
  same chord is identified in two successive slices", because another sub-segmentation covers it [FACT
  (relayed, 08) — Condit-Schultz, Ju & Fujinaga, §3.2.2, step 7]. Allowing two identical adjacent spans
  would make one musical reading appear as several rivals, which spreads its mass and breaks L2-S40.
  Figure is a field of the charter's chord [RULED — charter], and the two published readings of
  exemplar 1's piece disagree at bar 4 on exactly this. One writes `V6 … V65 … I` and the other
  `V6/5 b3 I` [FACT at the files — exemplars 1 and 2]. So a figure-only boundary is a real rival. The
  elaboration clause follows from the charter placing elaborations on events, not in the chord
  (L2-S1). **A consequence recorded rather than hidden:** exemplar 3's analysis writes a new label
  where a suspension resolves (`V7(4)/iv` then `V7/iv`). In L2's publication that is one span with a
  suspension assignment, so boundary grading against that annotation must map one onto the other
  (OQ-L2-7).
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* A phrase boundary with a restated chord is L3's to publish (DP-J), so L2 loses nothing by
  merging. **False-negative path:** a restatement an analyst writes as a new harmonic event, the
  `|| b4 I` shape. L2 merges it and L3's phrase grouping carries the division. If the measurement layer
  grades L2's boundaries against the annotation's label positions, it will count this as a miss
  (OQ-L2-7).
- *Falsifier.* CODE. **Observable:** consecutive spans. **Decision rule:** falsified if two adjacent
  published spans are identical in all five fields, or if a figure change is inadmissible as a
  boundary. **Not falsified by:** adjacent spans equal in chord and different in tonality.
- *Ruled (cowork_rulings_2026_10_07_l2_adjacent_identical_spans_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; L2-S14's wording does not change." Recorded with the ruling, as the
  surface's reading and not ruled separately: "This side found no reason to suspect L2-S14 costs precision at
  the two places looked at (§A.5 point 3), and proposes no open measurement."

**L2-S15. Rivals that differ only in where a boundary falls are carried as rivals, with their mass,
exactly as rivals that differ in label are.**
- *Defense.* The charter: "per span, the rivals with their mass — including rivals that differ in
  where the boundaries fall and not only in the label" [RULED — charter, L2; DP-K]. The published
  enumerate-then-filter system shows why. One window of a chorale admits six sub-segmentations, and
  the surviving readings differ in how many chords the window holds [FACT (relayed, 08) —
  Condit-Schultz, Ju & Fujinaga, Figure 3].
- *Source class.* Given — charter.
- *Status.* Settled. The form is L2-S41.
- *Premise.* None beyond the charter's.
- *Falsifier.* CODE. **Observable:** the rival list. **Decision rule:** falsified if two readings differing
  only in a boundary position cannot both appear. **Not falsified by:** the boundary rival falling below the
  cut-off the effort setting sets (L2-S42). (was: "the boundary rival falling below a publication threshold
  that obeys L2-S42."; cowork_rulings_2026_10_07_l2_four_agreeing_statements_sitting.md, recorded with
  Ruling 1, §A.4)
- *Ruled (cowork_rulings_2026_10_07_l2_four_agreeing_statements_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; no wording of L2-S3, L2-S9, L2-S15 or L2-S21 is changed by this ruling."

### 3c. Face (c) — the tonality at each moment

**L2-S16. Each span has exactly one tonality, and the tonality can change only at a span boundary.**
- *Defense.* DP-E: "a tonality change is located at a harmonic boundary"; its rival, an independent
  tonality track changing anywhere, "the output the analysis must produce cannot express" [RULED —
  charter, DP-E].
- *Source class.* Given — charter.
- *Status.* Settled.
- *Premise.* The charter's. **False-negative path:** a pivot chord analysts read in two tonalities at
  once. L2-S19 carries it as rivals.
- *Falsifier.* CODE. **Observable:** tonality per span. **Decision rule:** falsified if two tonalities
  are published for one span as its principal reading. **Not falsified by:** a rival with a different
  tonality over the same span.
- *Ruled (cowork_rulings_2026_10_05_l2_pivot_chord_sitting.md, Ruling 1).* Stands as derived. The ruling is
  quoted once, beside L2-S19 (#6); its last sentence names L2-S16.
- *Ruled (cowork_rulings_2026_10_07_l2_one_tonality_per_span_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; L2-S16's wording does not change."

**L2-S17. The written key signature enters as one term of the candidate score, a weak prior over the
spans' tonalities that acts at the start and at each notated signature change, and nowhere else. It
never constrains them. The prior assigns non-trivial weight to the tonalities
one accidental either side of the signature, as well as to the signature's own major and minor. A
tonality or mode tag the record file declares is not read at all.**
- *Defense.* The key signature is "a weak prior (C-2), never a fact about the tonality" [RULED —
  charter, L0]. L2 consumes everything L0 publishes [RULED — charter, L2 "Consumes"], and L0 supplies
  the signature in force at every position [RULED — IC S-6]. The file's declared-mode tag is annotation
  that "no layer of the analysis consumes … as evidence about the music" [RULED — IC beside S-1/S-2,
  Ruling 57 (i)]. Exemplar 3 carries one (`<mode>minor</mode>` beside a one-flat signature), and it is
  passed over. The prior spreads to one accidental either side because Baroque scores are often
  notated one accidental short of modern practice, so the signature under-determines the tonic [FACT —
  ledger C14, the admitted fact half]. **Declared (see §6): the ledger entry that states this also
  names, as not admitted, a design decision about handling it. This session read that sentence. The
  spreading rule here is derived from C14's admitted fact half alone and is the simplest rule
  consistent with it. It is flagged so the comparison can check it for contamination.**
- *Source class.* Given — charter, for the weak prior and "never a constraint". Given — input
  contract, for the tag. Derived, for the spread. *Measured* for the prior's weights, UNESTABLISHED.
- *Status.* Settled in shape. **Open** in value.
- *Premise.* The signature carries information about the tonality at all. **False-negative path:** a piece
  that does not begin in a tonality its signature suggests, or a notated signature change that does not mark
  a change of tonality. The lean then favours a wrong tonality at that point, and it is outweighed by the
  content terms because it is weak. Anywhere else the lean does not act. (was: "a modulating section after
  which the signature is not changed. The prior then pulls toward the old tonality, and it is outweighed by
  content terms because it is weak."; cowork_rulings_2026_10_05_l2_key_signature_prior_sitting.md, Ruling 2;
  brought into line with the amended first sentence on the user's word of 2026-10-13 before Task 0)
- *Falsifier.* CODE. **Observable:** readings under a changed signature with every pitch held fixed.
  **Decision rule:** falsified if any reading becomes inadmissible, if the declared-mode tag changes any
  candidate score, or if the signature's term enters the candidate score at any position other than the
  start and a notated signature change. (was: "falsified if any reading becomes inadmissible, or if the
  declared-mode tag changes any candidate score.";
  cowork_rulings_2026_10_05_l2_key_signature_prior_sitting.md, Ruling 2; brought into line on the user's
  word of 2026-10-13 before Task 0) **Not falsified by:** candidate scores moving a little under a changed
  signature.
- *Ruled (cowork_rulings_2026_10_05_l2_key_signature_prior_sitting.md, Ruling 1) — its last sentence, on the
  declared tag.* Stands as derived. "The chord-and-key layer does not consume the record file's declared
  major/minor tag (a MusicXML `<mode>` element, printed nowhere on the page) in any way — not as a prior,
  not as a hint, not as a rung of the evidence ranking. L2-S17's last sentence stands as derived: "A
  tonality or mode tag the record file declares is not read at all." The tag stays where Ruling 57 put it:
  carried at L0, labelled as read, for a reader outside the analysis. **This resolves the flag Ruling 57
  left to L2's surface.**" "**What it sets aside in the existing design.** The declared-mode half of
  register entries D-528 (the tag "a second conditioning input with its own fitted strength"), D-450 ("the
  key-signature and declared-mode prior"), D-057 (the tag as the weakest rung of the evidence ranking) and
  D-056 (the tag passed on as "a weak hint (`declaredMode`)"). The first three rungs of the ranking — the
  sounding notes, the surrounding music, the key signature — stand. **The register status of those entries
  is not changed here**: the register's same-commit rule is suspended and
  `cowork_register_rule_c_suspension_2026_08_28.md` is the route; no decisions-register identity is
  allocated."
- *Amended (cowork_rulings_2026_10_05_l2_key_signature_prior_sitting.md, Ruling 2) — the statement's first
  sentence.* "The written key signature is a weak lean on the tonality at the start and at each notated
  signature change, and nowhere else — `FRAMEWORK.md` C-2's form, and D-450's. **L2-S17's first sentence is
  to be amended to that form**, and the lean acting on every span (D-450's "persistent pull toward the
  signature at every step") is **excluded by name**. L2-S17's "It never constrains them" stands." (was: "The
  written key signature enters as one term of the candidate score, a weak prior over the spans'
  tonalities."; cowork_rulings_2026_10_05_l2_key_signature_prior_sitting.md, Ruling 2)
- *Beside L2-S17 (cowork_rulings_2026_10_05_l2_key_signature_prior_sitting.md, Ruling 2) — carried,
  UNSETTLED.* ""at the start" of what — the piece, or the stretch the user selected and the analysis loaded
  (the ratified C-2 says only "at the start"; the framework's first-stage draft adds "of the piece");
  whether a notated signature change falling between two note change points becomes a point where the lean
  re-applies."
- *Ruled (cowork_rulings_2026_10_05_l2_key_signature_prior_sitting.md, Ruling 3) — its spread.* Stands as
  derived. "L2-S17's spread stands as derived — non-trivial weight on the signature's own major and minor
  and on the tonalities one accidental either side — read as the minimum the counted table must allow, not a
  ceiling; it agrees in substance with D-528's small categorical table counted from annotated music
  (comparison Rows 48.50 and 10.60). The sizes are a measurement, held out (OQ-L2-3); D-528's
  signature-influence rate, measured by ablation and published at every fit with the expectation that it is
  small, is carried as stated there. The older detect-and-reinterpret fix (D-575) stays retired."

**L2-S18. Wherever a span can be read as an applied chord in the prevailing tonality, it can also be
read as a diatonic chord in a new tonality, and the reverse (V/V in C against V in G). Both readings
are admitted, and both are carried as rivals with their mass. Which one is principal is decided by the
candidate score over the whole sequence, not by a rule.**
- *Defense.* The charter publishes both a tonality and an applied target per span [RULED — charter].
  Both representations are therefore in the output language, and neither is a spelling of the other.
  Two published systems collapse applied chords into brief key changes, "avoiding murky distinctions
  between secondary function and actual modulation" [FACT (relayed, 08) — Raphael & Stoddard 2003,
  p. 2; McLeod & Rohrmeier 2021, §system]. The charter's output forbids that collapse. Where the line
  falls is contested in the literature and in the annotations. "The line between modulation and
  tonicization is not clearly defined in tonal music" (Kostka & Payne, as quoted). The same music
  carries two defensible local-tonality ground truths, and textbooks differ widely in how much they
  tonicize [FACT (relayed, 08) — Nápoles López et al. 2020, §2]. The two annotators of one chorale study
  disagreed mainly on "tonicization versus modulation" [FACT (relayed, 08) — de Clercq, p. 195].
  Exemplars 1 and 2 place the move to D minor in the development at different points. One reads bar 31
  as `i d: iv`, and the other keeps G minor through bar 31 and reads bar 32 as `ii.V`, D minor's V [FACT
  at the files]. Exemplar 3 keeps a whole passage in D minor as chords applied to III (`V7/III`,
  `I/III`, `IVM7/III`) [FACT at the file], where another analyst might write a move to F major. A
  leading tone at a cadence occurs at close to the same rate at real and passing changes, so it does
  not separate them [FACT — ledger C42]. Key-agnostic evidence separates the two for the subdominant
  relation and not for the dominant [FACT — ledger C39].
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* The candidate score has terms that can tell the two apart over a stretch of music, namely
  the tonality-persistence and progression terms of L2-S34. **False-negative path:**
  stretches where no available term separates them. The two then receive near-equal mass, which is the
  honest publication.
- *Falsifier.* CODE. **Observable:** the rival list over a tonicized dominant. **Decision rule:**
  falsified if the applied reading and the tonality-change reading are not both present. **Not
  falsified by:** one of them carrying very small mass.
- *Beside L2-S18 (cowork_rulings_2026_10_07_l2_applied_or_new_tonality_sitting.md, Ruling 1) — carried.*
  "**Carried, not dropped (#12):** D-291's measured ground ("of the affected cases 92.7 % are
  cadence-confirmed local keys in the ground truth", relayed from the register entry) stays on record as
  evidence. A fitted cadential progression term (L2-S34 (iii)) carries that tendency; whether a hard cadence
  condition would read better is opened, under Ruling 6 of the L2-S10 record of this date, only when there
  is reason to suspect it would improve the inference."
- *Beside L2-S18 (cowork_rulings_2026_10_07_l2_applied_or_new_tonality_sitting.md, Ruling 1).* The cost the
  ruling's ground restates as accepted on 2026-10-06 and not re-decided — a key change chosen with no
  cadence at all where the fit repays it — is quoted beside L2-S34
  (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 2).
- *Ruled (cowork_rulings_2026_10_07_l2_applied_or_new_tonality_sitting.md, Rulings 1, 2 and 3).* "L2's
  algorithm as its statements define it is unchanged; L2-S18's wording does not change."

**L2-S19. A pivot chord, read by an analyst in two tonalities at once, is published as one span
with one tonality. The other tonality's reading of the same span is published as a rival with its
mass. Whether L2 should instead be able to publish a span as a pivot, carrying both tonalities in the
principal reading, is a question for the user (OQ-L2-5 ★).**
- *Defense.* The charter publishes "per span, the tonality", in the singular [RULED — charter].
  Exemplar 2 writes `N6 F: IV6` at bar 41 (one chord, a Neapolitan in A minor and IV6 in F), and
  exemplar 5 writes `V2/IV F: V2` at bar 1 and `VII C: I` at bar 29 [FACT at the files]. Exemplar 1's
  analysis, the other reading of exemplar 2's piece, writes the same bar 41 as `IV.IV6`, a change to F
  at that chord with no pivot [FACT at the file]. So one analyst writes a pivot and the other does not.
  Rivals express "either" and cannot express "both at once". The pivot is a real theoretical claim
  (THEORY: the pivot-chord modulation of standard textbooks), and the charter's singular may not have
  been meant to exclude it.
- *Source class.* Derived.
- *Status.* Settled (cowork_rulings_2026_10_05_l2_pivot_chord_sitting.md). (was: "**Open** (OQ-L2-5 ★).";
  cowork_rulings_2026_10_05_l2_pivot_chord_sitting.md, Ruling 1)
- *Premise.* Rivals suffice. **False-negative path:** a consumer (L3's cadence reading, or a display
  for the user) that needs the pivot as one fact. It would see two readings splitting the mass and no
  statement that they hold together.
- *Falsifier.* CODE: falsified if two tonalities are published for one span as its principal reading. (was:
  "RESIDUAL until ruled."; cowork_rulings_2026_10_05_l2_pivot_chord_sitting.md, Ruling 1) (the record marks
  this as the surface's reading, not ruled separately)
- *Ruled (cowork_rulings_2026_10_05_l2_pivot_chord_sitting.md, Ruling 1).* Stands as derived. "For L2's
  specification, each harmonic span carries exactly one tonality in the principal reading. A chord an
  analyst reads in two tonalities at once (a pivot) is published as one span with one tonality, and the
  other tonality's reading of the same span as a rival with its mass. **L2-S19 stands as derived; its status
  "Open (OQ-L2-5 ★)" closes. OQ-L2-5 is answered: the charter's "the tonality" per span is singular**, and a
  pivot is expressed as rivals. No charter sentence is amended. **L2-S16 stands as derived**, untouched by
  this ruling."
- *Beside L2-S19 (cowork_rulings_2026_10_05_l2_pivot_chord_sitting.md, Ruling 1) — carried, UNSETTLED.*
  "Where a consumer wants the label "this chord is in both tonalities", it is the decided chord re-expressed
  in the neighbouring span's tonality (the surface's reading). Whether and where that label is published —
  at L3, or as a display view — is **not decided by this ruling** and is carried to L3's own specification.
  L3's charter list is not amended."
- *Beside L2-S19 (cowork_rulings_2026_10_05_l2_pivot_chord_sitting.md, Ruling 1) — carried.* "A consumer
  that wants "this chord is a hinge" as one fact must compute it, and the masses of the two rivals express
  "either", not "both" (L2-S19's own premise). Which chord an analyst names the pivot is a judgment a fixed
  rule may not reproduce (the surface's reading)."
- *Beside L2-S19's last sentence (cowork_rulings_2026_10_05_l2_pivot_chord_sitting.md, Ruling 1; written at the
  ratification of face (c), cowork_rulings_2026_10_13_l2_face_c_ratification_sitting.md, correction 2(a)).*
  The statement's last sentence states the question as the derivation left it. Ruling 1 has since answered it
  (OQ-L2-5 ANSWERED). The derived wording stands.

**L2-S20. The tonality terms read the chords the reading proposes (degree, function, cadential
progressions) and a recency-weighted account of which spelled scale degrees have sounded. They do not
read a global pitch-class profile of the span.**
- *Defense.* Music that dwells on its tonic presents the tonic triad and hardly the characteristic
  tones, so a model that rates tonalities by the presence of those tones rates the true tonality
  lowest exactly when it is most strongly prolonged [FACT — ledger C36]. A published key finder argues
  that "approaches based on pitch profiles … do not take into account the directedness of music: one or
  a few C♯ can alter our perception, no matter how many C♮ there were before". Its recency-based
  "current diatonic pitch set" alone named the reference tonality on 67.3% of beats of a Mozart corpus,
  against 50.0% for "no modulation" [FACT (relayed, 08) — Feisthauer et al. 2020, pp. 324–325, Table 2;
  that system fitted its three weights on the same 38 movements it reports, by its own statement, so
  the figure is not a held-out figure]. Choice of profile changes a reading materially, and one whole
  piece is read wrong under one profile and right under another [FACT (relayed, 08) — Sapp 2005,
  §examples]. Reading the proposed chords is what the joint decision is for [RULED — charter, DP-B;
  the measured cost of separating tonality from chord is 4.6 points on tonality and 1.8 on chord in the
  one system that ablated it, FACT (relayed, 08) — Rocher et al. 2010, Table 5].
- *Source class.* Derived.
- *Status.* Settled that the global profile is excluded. The exact recency form is *measured*
  (OQ-L2-3).
- *Premise.* Recency-weighted degree evidence plus chord function is enough. **False-negative path:** a
  long tonic prolongation opening the working span, with no earlier music loaded. Recency then has
  nothing to recall, and the edge rule (L2-S22) is what supplies it.
- *Falsifier.* CODE. **Observable:** tonality terms' inputs. **Decision rule:** falsified if a
  tonality term reads a duration-weighted pitch-class distribution of the whole span, or of the whole
  working span, as its only degree evidence. **Not falsified by:** a recency window that happens to
  cover a whole short span.
- *Recorded (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, §1g).* Stands as derived — recorded
  by the record as this side's derivation, not ruled; challengeable. "**The family is placed whole.** L2-S20
  stands as derived; Ruling 4 adds one candidate to OQ-L2-3 and Ruling 3 one reporting requirement to the
  same measurement, neither changing L2-S20's wording. Row 44.50 claim (ii)'s cadence-cue items are for
  L2-S37's family to read (Ruling 5)."
- *Beside L2-S20 (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 3).* The reporting
  requirement this ruling adds to OQ-L2-3's held-out measurement, which this statement's *Status* names, is
  quoted beneath OQ-L2-3 in §4.
- *Beside L2-S20 (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 4).* The candidate form
  this ruling adds to OQ-L2-3's held-out comparison of the spelled-degree evidence's forms is quoted beneath
  OQ-L2-3 in §4.
- *Beside L2-S20 (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 1) — carried, cost
  accepted.* "none beyond retiring the sentence."
- *Beside L2-S20 (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 2) — carried, cost
  accepted.* "none known."
- *Beside L2-S20 (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 3) — carried, cost
  accepted.* "the protection the old design took by placement now rests on the joint decision and is
  confirmed only by the measurement."
- *Beside L2-S20 (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 4) — carried, cost
  accepted.* "one more arm in a measurement already owed."
- *Beside L2-S20 (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 5) — carried, the remedy
  named.* "A separate dominant-shape term stays the named remedy if the measurement-design stage finds L2
  under-reading dominants; the resolution-denying repertoire named with D-494 is where that would show."
- *Beside L2-S20 (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 5) — carried, cost
  accepted.* "an incomplete or ambiguous dominant sonority helps the key only as much as its chord readings
  carry mass."

**L2-S21. The minor mode is one mode whose sixth and seventh degrees may each be raised or not. A
reading in minor may use either form of each without a change of tonality. The tonic chord in major
quality at a minor-mode close (the Picardy third) is a chord of the minor tonality, not a change to
the major.**
- *Defense.* The minor mode's variable sixth and seventh degrees (the natural, harmonic and melodic
  collections) are standard theory [THEORY]. A published key finder notes that minor-mode tonality is
  harder "mostly explained by the floating 6th and 7th scale degrees of the minor scale" [FACT
  (relayed, 08) — Feisthauer et al. 2020, p. 329]. The Picardy third: exemplar 5 bar 28 `I ||` in
  D minor [FACT at the file], and I♯-PA1 final cadences outnumbering i-PA1 about ten to one in the
  Bach chorales [FACT (relayed, 08) — de Clercq, pp. 196–197]. The tonality-change reading of a Picardy
  close would put a one-chord span in the parallel major at every such ending. It is admitted as a
  rival (L2-S3), and it is not the only way to write the close.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Analysts read the Picardy close in the minor tonality. **False-negative path:** an analyst
  who writes a change to the parallel major. It is admitted as a rival.
- *Falsifier.* CODE. **Observable:** the admitted degree set under a minor tonality. **Decision rule:**
  falsified if raised 6̂ or 7̂ chords, or the major tonic, are admissible only through a change of
  tonality. **Not falsified by:** a rival reading in the parallel major.
- *Ruled (cowork_rulings_2026_10_07_l2_four_agreeing_statements_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; no wording of L2-S3, L2-S9, L2-S15 or L2-S21 is changed by this ruling."

**L2-S22. At the edge of the working span, L2's tonality (and the rest of its reading) depends on music
before and after the span. L2 is the layer that asks for more music. It stops asking when its in-span
publication stops changing between successive enlargements. At the top effort setting it stops when its
in-span publication — the readings, the span-rivals and their masses — is the same after an enlargement
as before it. Below the top, the effort setting sets a tolerance on the change in mass within which the
publication counts as unchanged, continuously across settings. At every setting the principal in-span
reading must be unchanged. The safety cap (D-624) ends a loop that does not settle, and the publication
is then marked as truncated (D-263).**
- *Defense.* The output covers exactly the selection, and music beyond it is evidence [RULED — D-260].
  A layer never guesses how much context it needs, and it extends until "the layer's in-selection
  output stops changing" [RULED — D-261, clauses 3 to 6. **See §6: the same entry also carries an
  as-built description, which this session saw and does not use.**]. On the input contract's side,
  "the decision to enlarge, the increment and the stop test belong to the requester, never to L0 or
  L1" [RULED — IC beside S-53, Ruling 46 (v)]. One settled indication does not fix the tonality at the
  edge of the music being read, while a tonality established over a stretch of earlier music does [FACT
  — ledger C43, the fact half]. The masses are real numbers, so "stops changing" needs a rule. Whether
  the rule is identity of the principal reading, identity of the rival set, or a bound on the change in
  mass is not derivable from the ruled words.
- *Source class.* Given — design intent (D-260, D-261) and input contract (Ruling 46), for the
  mechanism. Derived, for the point that the masses need their own rule.
- *Status.* Settled for the mechanism and for the mass rule
  (cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md, Ruling 2; OQ-L2-6 ANSWERED). (was: "Settled
  for the mechanism. **Open** for the mass rule (OQ-L2-6).";
  cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md, Ruling 2; brought into line on the user's
  word of 2026-10-13 before Task 0)
- *Premise.* Convergence happens within the score. **False-negative path:** a reading that never
  converges, such as an oscillating pivot. The record edge (IC Ruling 46 (vi)) or the safety cap (D-624) ends
  the loop, and the publication says so (the record-edge mark, or marked as truncated, D-263). (was: "a
  reading that never converges, such as an oscillating pivot. The record edge (IC Ruling 46 (vi)) ends the
  loop, and the record-edge mark says so."; cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md,
  Ruling 2; brought into line at the ratification of face (c),
  cowork_rulings_2026_10_13_l2_face_c_ratification_sitting.md, correction 2(b))
- *Falsifier.* CODE. **Observable:** the in-span publication after successive enlargements. **Decision
  rule:** falsified if, at the top setting, L2 stops while a reading, a span-rival or a mass still changes
  between enlargements; if, at any setting, it stops while its principal reading still changes; if, below
  the top, it stops while a mass changes by more than that setting's tolerance; if it asks L1 to decide the
  increment; or if a loop ended by the safety cap is published unmarked. (was: "falsified if L2 stops while
  its principal in-span reading still changes, or if it asks L1 to decide the increment.";
  cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md, Ruling 2; brought into line on the user's
  word of 2026-10-13 before Task 0) **Not falsified by:** a marked stop at the safety cap or the record
  edge. (was: "a stop at the record edge."; cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md,
  Ruling 2; brought into line on the user's word of 2026-10-13 before Task 0)
- *Amended (cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md, Ruling 2) — the statement's last
  sentence.* "Position 2. **L2-S22's last sentence is to be replaced**, as this side's wording for the
  application act: "At the top effort setting it stops when its in-span publication — the readings, the
  span-rivals and their masses — is the same after an enlargement as before it. Below the top, the effort
  setting sets a tolerance on the change in mass within which the publication counts as unchanged,
  continuously across settings. At every setting the principal in-span reading must be unchanged. The safety
  cap (D-624) ends a loop that does not settle, and the publication is then marked as truncated (D-263)."
  **OQ-L2-6 is closed** by it. The tolerance values and the defaults of each setting are not ruled here:
  they are decided at the effort setting's build (D-202 stays DEFERRED), as the rival-publication cut-off
  depths are. **This changes L2's algorithm as its statements define it** (the stopping rule for reading
  more music); nothing else in L2 changes." (was: "What counts as "stops changing" for the masses of the
  rivals is open (OQ-L2-6)."; cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md, Ruling 2)
- *Beside L2-S22 (cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md, Ruling 2) — carried.*
  "**Declined:** position 1 (the best reading only — publishes unsettled weights; against D-261's wording);
  position 3 (one fixed tolerance — a cost-driving constant against D-035, the shape declined for the rival
  cut-off, and no measured value found). **Carried, unestablished:** whether the top setting's identity test
  settles before the safety cap in ordinary music — a measurement at the build, under the effort setting's
  design."
- *Beside L2-S22 (cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md, Ruling 1) — recorded with the
  ruling, the surface's readings, not ruled separately.* "**Recorded with the ruling, as the surface's
  readings, not ruled separately:** a forward limit at the next cadence or phrase end is a candidate for a
  lower effort setting (the sizing's entry point (c)), decided at the effort setting's design; the risk that
  convergence between successive enlargements stops early is guarded by the step-size independence test
  already owed (D-264; Rows 45.24, 45.71, 45.72), and no new measurement is proposed;"
- *Beside L2-S22 (cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md, Ruling 2) — the Defense's
  last sentence, overtaken.* The Defense's last sentence ("Whether the rule is identity of the principal
  reading, identity of the rival set, or a bound on the change in mass is not derivable from the ruled
  words.") states what the derivation could derive from the rulings it held. Ruling 2 has since decided the
  rule; see the amended last sentence of the statement. The derived wording stands.

### 3d. Face (d) — which sounding notes belong to the harmony, and which elaborate it

**L2-S23. The assignments are part of the one decision. They are made inside the candidate score,
relative to each candidate reading's chord, and never by a detector that runs first.**
- *Defense.* DP-D: the chord-tone assignment is "part of L2's one decision and published from it". A
  first-running detector is excluded because its authors report F .72 with many "errors" that are
  plausible analytical choices, and because "a first-running detector's mistakes are unrecoverable
  downstream" [RULED — charter, DP-D]. The two published symbolic systems that do best on segmentation
  decide figuration relative to "a candidate chord label y" inside the segment scoring [FACT (relayed,
  08) — Masada & Bunescu, Appendix B, p. 15]. The enumerate-then-filter system decides non-chord tones
  per sub-segmentation [FACT (relayed, 08) — Condit-Schultz, Ju & Fujinaga, §3.2.2, steps 2–4]. The
  first-running detector's ground truth was itself derived from chord labels [FACT (relayed, 08) — Ju
  et al. 2017, §2], so its target presupposes the decision it is meant to precede. A method that finds
  chord tones after the chord is given cannot revise the chord [FACT (relayed, 08) — McLeod &
  Rohrmeier 2024, coupling facts].
- *Source class.* Given — charter.
- *Status.* Settled.
- *Premise.* The joint search can afford the assignment dimension (L2-S36). **False-negative path:**
  the assignment multiplies the state. See OQ-L2-8.
- *Falsifier.* CODE. **Observable:** where assignments are computed. **Decision rule:** falsified if
  any assignment is fixed before the candidate chord it is relative to. **Not falsified by:** a
  precomputed per-event feature (a step to the next note in its voice) that does not depend on the
  chord.
- *Ruled (cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling 2).* Stands as derived. "For
  L2's specification, the pedal reading — the chord read from the upper voices with the held note as an
  elaboration — is one of the readings L2's one decision scores and chooses, like any other, its rivals (the
  reading rooted on the held note among them) published with their mass (L2-S40). **D-385's reader over the
  stored alternatives, choosing the pedal reading after the decode by a confidence threshold, does not carry
  into L2's specification.** D-385's register status is settled at the ratification act, not here (as D-103
  was recorded superseded by D-207). **L2-S23 stands as derived**: the assignments are made inside the
  candidate score, with no exception for the pedal."
- *Beside L2-S23 (cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling 2) — carried, what
  it does not decide.* "When the *label* "pedal point" is written — that travels with Group H to L2-S33's
  family. What becomes of the measurement D-385's build is hard-gated on at OI-4 — not decided here."
- *Pointer (written at the ratification of face (d), cowork_rulings_2026_10_13_l2_face_d_ratification_sitting.md,
  correction 1).* The crossing-elaborations item under OQ-L2-3 in §4
  (cowork_rulings_2026_10_09_l2_crossing_elaborations_sitting.md, Ruling 2), where that ruling's words on this
  statement's wording and its measurement stand quoted.

**L2-S24. The voice-leading evidence an elaboration relation needs is read from L1's per-voice
relations. These are, per onset change point and notated voice, the silence before the onset, the
time since that voice's preceding attack, and the spelled melodic interval from its preceding note,
with the chordal count. The *following* note of an event is read as the preceding-note relation
published at the next onset in the same voice. Where a voice is chordal at either end, L2 has no
published successor for a given note, and it does not construct one (OQ-L2-9, naming IC S-50 and
Rulings 49 and 61).**
- *Defense.* Passing, neighbour, suspension and anticipation are each defined by approach and departure
  in one line [THEORY]. The published figuration heuristics define them by "anchor notes, step
  relations, length and accent" [FACT (relayed, 08) — Masada & Bunescu, Appendix B]. L1 publishes the
  per-voice relations with their witnesses, "named for the relation and not for a boundary" [RULED — IC
  beside S-39, Ruling 49], and a chordal count per voice [RULED — IC Ruling 61]. A consumer reads and
  never re-derives [RULED — D-100]. In a voice that sounds several pitches at once, "the preceding note"
  names a set, and pairing members of two chords into lines is voice separation, which the analysis
  never infers [RULED — IC beside S-13, citing D-389]. Keyboard writing with a chordal accompaniment in one notated
  voice is where this bites [THEORY]. No exemplar's music was read for it (§6).
- *Source class.* Given — input contract, for what is published. Derived, for the successor reading
  and for the refusal.
- *Status.* Settled for single-note voices. Closed for chordal voices as inactive by design
  (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 2). (was: "Settled for single-note
  voices. **Open** for chordal voices (OQ-L2-9).";
  cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 2)
- *Premise.* Notated voice is a usable line. That is the input contract's declared proxy hazard, which
  L2 inherits [RULED — IC S-13, premise]. **False-negative path:** a keyboard voice carrying chords, or a
  line split across notated voices. The elaboration term then has no evidence for those notes, and they
  can only be chord tones or unrelated elaborations. The loss is declared, not repaired.
- *Falsifier.* CODE. **Observable:** the inputs of the elaboration term. **Decision rule:** falsified if
  the term reads any melodic interval not published by L1, or pairs notes across a chordal voice.
  **Not falsified by:** the term being inactive for chordal voices.
- *Ruled (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 2).* Stands as derived. "For
  L2's specification, the voice-leading evidence an assignment reads is what L0 and L1 publish — L1's
  per-voice relations (S-50; Ruling 49 of the L0/L1 sitting) and the chordal count (Ruling 61) — and **no
  fact of the voice-leading axis**."
- *Beside L2-S24 (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 2) — carried,
  UNSETTLED.* "The charter's boundary row lets published facts cross "in either direction" between the
  harmonic layers and the axis, while neither L2's nor L3's consume line names the axis. That tension is the
  charter's own and is left for the whole-architecture coherence review the detail phase ends with (the
  2026-08-30 opening sitting, Ruling 2 item 6, as the route record relays it)."

**L2-S25. Duration and metric position bear on an assignment as terms (covariates). Neither decides
it: no duration cut and no metric position makes a note a chord tone or an elaboration.**
- *Defense.* "Duration weight cannot separate a long non-chord tone from a genuine added tone; both sit
  on the same side of any weight cut, because the distinction is functional and voice-leading" [FACT —
  ledger C26]. Over arpeggiated harmony the non-root tone can carry more duration than the root [FACT —
  ledger C4]. A surface-feature classifier (duration, metric position, approach and departure
  intervals) beats the all-chord-tone baseline by only about four to five points out of sample [FACT
  (relayed, 08) — Hu & Arthur 2021, §results]. So surface covariates carry some information and are
  far from deciding. The one published generative model keeps the metrical position of a pitch as a
  covariate of its category rather than a rule: "we simply allow the output distributions to depend on
  the known measure positions in a manner we will learn from data" [FACT (relayed, 08) — Raphael &
  Stoddard 2003, p. 3].
- *Source class.* Derived. Weights *measured*, UNESTABLISHED.
- *Status.* Settled in shape.
- *Premise.* None beyond the ledger's.
- *Falsifier.* CODE. **Observable:** assignments across a sweep of note durations with pitches and
  voice leading held fixed. **Decision rule:** falsified if some duration threshold flips the assignment
  of every note that crosses it regardless of the rest of the reading. **Not falsified by:** the mass
  of the chord-tone reading changing monotonically with duration.
- *Ruled (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 1).* Stands as derived. "For
  L2's specification, whether a sounding note is a chord tone or an elaboration is **weighed inside L2's one
  decision**: how the note is approached and left, its metric position and its duration are terms of the
  candidate score, and **no fixed tier makes a note a chord tone or an elaboration**. Once the reading has
  made a note an elaboration, its relation's name follows that relation's definition (Ruling 1 of
  `cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md`); a foreign note fitting none is the
  unclassified elaboration. **L2-S25 stands as derived.** **D-333's second half** — the weighting set per
  idiom, never a structural branch — **is carried**, L2-S25's weights being measured; **its first half — the
  three-tier structure fixed — does not carry into L2's specification.** D-333's register status is settled
  at the ratification act, not here (the shape Ruling 2 of the second family used for D-385)."
- *Beside L2-S25 (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 1) — carried.* "The
  weights must be fitted, and no annotated corpus with per-note chord-tone labels is known to the derivation
  (OQ-L2-13), so until one is found or the user rules otherwise they are fitted and graded only through the
  chord; a fixed rule needed no fit. D-333's fixed structure is set aside."

**L2-S26. Grace notes (published as ornamental attachments of a host event) and ornament signs
(published as attributes of an event) are evidence for the assignment of their host and for the
chord. They carry no assignment of their own, because they are not sounding events. Whether L2 also
publishes a relation for a grace attachment, such as "appoggiatura to its host", is OQ-L2-10.**
- *Defense.* A grace note opens no change point and belongs to no sounding set [RULED — IC S-16], and
  the charter's assignment is "per sounding note" [RULED — charter]. The input contract anticipates the
  use: "an on-beat appoggiatura a step above its host is dissonance evidence L2 will want" [RULED — IC
  S-16, flagged there as a conjecture on L2's want]. Exemplar 3 writes appoggiaturas as grace notes in its
  opening bars [FACT at the file, the bars read]. Zero information loss to the end user requires every inferred object to be displayable
  [RULED — D-295]. A relation L2 infers for a grace note is such an object, which is why OQ-L2-10 is
  asked rather than answered no.
- *Source class.* Derived.
- *Status.* Settled that no assignment is made and that no relation is published
  (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 3). (was: "Settled that no assignment
  is made. **Open** on publishing a relation (OQ-L2-10).";
  cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 3)
- *Premise.* The host carries the harmony at its onset [RULED — IC S-16, premise]. **False-negative
  path:** a long appoggiatura that sounds for half its host's value, so that the harmony is heard over
  the appoggiatura first. L2 reads it through the attachment and cannot place a boundary inside the
  host, which the notation does not give a position for.
- *Falsifier.* CODE. **Observable:** assignments and terms. **Decision rule:** falsified if a grace
  note receives a chord-tone assignment or appears in a sounding set. **Not falsified by:** a grace
  note's pitch entering a term.
- *Ruled (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 3).* Stands as derived. "For
  L2's specification, a grace note carries no assignment and L2 publishes no elaboration relation for it; it
  is evidence for its host's assignment and for the chord. **L2-S26 stands as derived; its status "Open on
  publishing a relation (OQ-L2-10)" closes. OQ-L2-10 is answered no.** Whether a grace note clashes with the
  decided chord, and how it moves to its host, are facts L3 can read off L2's published chord and L1's
  published attachment if a consumer wants them."
- *Beside L2-S26's last sentence (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 3;
  written at the ratification of face (d), cowork_rulings_2026_10_13_l2_face_d_ratification_sitting.md,
  correction 2(a)).* The statement's last sentence states the question as the derivation left it. Ruling 3 has
  since answered it (OQ-L2-10 ANSWERED: no). The derived wording stands.
- *Beside L2-S26's Defense, last sentence (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling
  3; written at the ratification of face (d), cowork_rulings_2026_10_13_l2_face_d_ratification_sitting.md,
  correction 2(b)).* OQ-L2-10 has since been answered no (Ruling 3). The user's condition, that not publishing
  such a relation does not break the rule against information loss, was checked at the record's §1c: the grace
  note's pitch, form and host stay published by L1 and the chord by L2, so the relation can be recomputed. The
  derived wording stands.

### 3e. Face (e) — the chord read over each span

**L2-S27. L2 decides the chord as degree, quality, figure and applied target, read against the span's
tonality. It publishes no chord symbol (root pitch class, quality and bass note). That is L3's
read-off.**
- *Defense.* The charter [RULED — charter, L2 "Publishes"; L3; DP-L]. Its reason: "The root is the tonic
  transposed by the degree's interval … Publishing it as a decision would create a second home for one
  fact", the incoherence measured in systems that predict chord parts independently [RULED — charter,
  L3, DP-A]. Deciding the label whole rather than per field is also what the published systems that
  add coherence machinery converge on: "decided HOLISTICALLY over 1540 whole symbols … separate
  per-field outputs can combine inconsistently" [FACT (relayed, 08) — McLeod & Rohrmeier 2021,
  §system].
- *Source class.* Given — charter.
- *Status.* Settled.
- *Premise.* The charter's.
- *Falsifier.* CODE. **Observable:** L2's output schema. **Decision rule:** falsified if L2 publishes a
  root pitch class or a bass note as a field. **Not falsified by:** L3 publishing them.
- *Ruled (cowork_rulings_2026_10_08_l2_chord_as_degree_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; L2-S27's wording does not change."

**L2-S28. The figure is decided in the reading. It is the chord member the reading takes as the
span's structural bass, which is not necessarily the lowest pitch sounding at the span's first slice.
The candidate score has a term relating the figure to the lowest sounding pitch of each slice of the
span, weighted by duration and metric strength. The lowest sounding pitch per slice is not published
by L1 for every slice, which is OQ-L2-11, naming IC S-44 and S-50.**
- *Defense.* In arpeggiated and Alberti textures the lowest pitch of a short slice is not the harmony's
  bass [FACT — ledger C32, C38; IC S-44 declares the same hazard]. Alberti writing requires carrying a
  root across a moving, re-inverted bass, and one continuity rule cannot serve both that and sustained
  arpeggiation [FACT — ledger C32, the conflict half]. So "the bass at the first event" is wrong as a
  rule. One published system uses two definitions of a segment's bass, the lowest note of the first
  event and the lowest note of the whole segment, as separate features whose weights are fitted [FACT
  (relayed, 08) — Masada & Bunescu, Appendix C.3, p. 18]. Inversion accuracy falls steeply away from
  root position in a published large-vocabulary system (71.5 / 54.4 / 38.3 / 40.5 for root, first,
  second and third) [FACT (relayed, 08) — McLeod & Rohrmeier 2021, §results]. That is where the figure
  decision is weakest, so the figure must be carried in the rivals (L2-S14). L1 publishes the lowest
  sounding pitch as a cue anchor, at onset change points and inside cue witnesses [RULED — IC S-44,
  S-49, S-50], not for every slice. Computing it from the sounding set would re-derive an L1-defined
  quantity [RULED — D-100], so L2 writes the want instead.
- *Source class.* Derived.
- *Status.* Settled in shape, and on the per-slice input
  (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 2; OQ-L2-11 ANSWERED). (was: "Settled in
  shape. **Open** on the per-slice input (OQ-L2-11).";
  cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 2; brought into line on the user's word of
  2026-10-13 before Task 0)
- *Premise.* The structural bass is a reading decision, not a notated fact. **False-negative path:** a
  figure analysts read from the first bass note regardless. The term weights would then fit toward the
  first slice, which the fit shows.
- *Falsifier.* CODE. **Observable:** figures over an Alberti span. **Decision rule:** falsified if the
  figure is set by a fixed rule from one slice's lowest pitch. **Not falsified by:** the fitted term
  preferring the first slice.
- *Beside L2-S28 (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 2) — the last sentence's
  want, met at L1.* "at the application act, S-50 of `cowork_derived_specification_l0_l1_2026_09_03.md`
  gains one item — *per slice, the lowest sounding pitch of its sounding set, published under that name,
  with its witness (the note), its establishment status, its provenance and, where not computed, a named
  reason* (the forms S-50 already requires of every item). The derived list stands at the derivation; S-50's
  former wording is preserved at its site (#12). **L2's algorithm as its statements define it is
  unchanged:** L2-S28's term already wants exactly this." "OQ-L2-11 is marked ANSWERED by this ruling, and
  L2-S28's last sentence gains, beside it, a pointer to this ruling (the derived wording standing)." The L1
  edits the ruling orders are written into `cowork_derived_specification_l0_l1_2026_09_03.md` (S-50, its §0
  entry *The lowest sounding pitch* and S-44) and into `FRAMEWORK.md`'s L1 list by
  `records/cc/instructions/cc_instruction_l2_application_2026_10_10.md`, Task 5.
- *Beside L2-S28 (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 2) — the Defense's "not
  for every slice", overtaken.* The Defense's sentence that L1 publishes the lowest sounding pitch "not for
  every slice" describes L1's published list as it stood when this statement was derived. Ruling 2 adds the
  lowest sounding pitch of every slice to that list (S-50 of the L0/L1 specification); see the sub-item
  beside the last sentence. The derived wording stands.
- *Beside L2-S28 (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 3).* The item this ruling
  adds to OQ-L2-3's list of held-out measurements — the bass-scale-degree prior of D-585, after the Rule of
  the Octave — is quoted beneath OQ-L2-3 in §4.
- *Ruled (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 1).* "L2's algorithm as its
  statements define it is unchanged; L2-S28's wording does not change."

**L2-S29. The cadential six-four is admitted under at least the two readings the exemplars write: a
tonic chord in second inversion, and a dominant with the sixth and fourth above its bass as
elaborations. The two are carried as rivals. Which theory is principal is not decided here. The
charter records it as underived (DP-N).**
- *Defense.* DP-N, "NONE CHOSEN — underived" [RULED — charter]. The two published readings of
  exemplar 1's piece disagree at bar 11 and bar 24 on exactly this. One writes `I6/4` and the other
  `V(64)` [FACT at the files — exemplars 1 and 2]. Under L2-S1 the second reading is one chord (V) with
  two suspension-class elaborations. The charter's third candidate, the six-four "as its own category",
  cannot be represented until DP-N is ruled.
- *Source class.* Given — charter (the question is open there). Derived, for admitting both.
- *Status.* **Open** (DP-N, the charter's).
- *Premise.* Carrying both as rivals is enough until DP-N is ruled. **False-negative path:** a
  grading that counts one reading as correct. That is measurement design, not L2.
- *Falsifier.* CODE. **Observable:** rivals at a cadential six-four. **Decision rule:** falsified if
  either reading is inadmissible. **Not falsified by:** one reading carrying most of the mass.
- *Ruled (cowork_rulings_2026_10_05_l2_cadential_six_four_sitting.md, Ruling 1).* Stands as derived. "For
  L2's specification, the cadential six-four is admitted under the two readings the derivation names — a
  tonic chord in second inversion (`I6/4`), and a dominant with the sixth and fourth above its bass as
  suspension-class elaborations (`V(64)`) — and the two are carried as rivals, the decision publishing the
  one the evidence favours with the other as its rival. **No theory is principal. The charter's DP-N stays
  open exactly as ratified; no charter text is amended.** **L2-S29 stands as derived.**" The named exclusion
  the ruling makes is quoted beside L2-S2.
- *Beside L2-S29 (cowork_rulings_2026_10_05_l2_cadential_six_four_sitting.md, Ruling 1) — carried.* "**The
  costs, carried.** The committed label can differ from a given corpus's convention; whether that counts
  against the analysis is a grading question for measurement design (the graded-distance mitigation the
  reading pass relays, and D-352's bar for tonality that counts any recorded reading, are there to draw on).
  L3's cadence reading must handle a committed `I6/4`. The ceiling cost of excluding `Cad64` is uncounted."
- *Beside L2-S29 (cowork_rulings_2026_10_05_l2_cadential_six_four_sitting.md, Ruling 1) — carried, what it
  does not decide.* "**What it does not decide.** How a `Cad64` annotation converts into L2's four fields;
  whether any grading corpus writes `Cad64`; whether the grading accepts either rival; which reading each
  grading corpus uses, piece by piece (the framework's §S9 settling route for DP-N). All measurement
  design."

**L2-S30. No chord term decides a chord from the pitch-class content of the span alone. The chord
terms also read the neighbouring spans' readings (the progression), the assignments (which notes
count), and the voice-leading evidence of L2-S24.**
- *Defense.* Several ledger entries record that pitch-class content under-determines the chord: an
  added-sixth chord and a seventh chord on the related root have the same content [FACT — ledger C6];
  a root-position major triad and the first inversion of its submediant are near-indistinguishable
  vertically [FACT — ledger C8]; a sonority and the chord a third above it are separated only by the
  surrounding music [FACT — ledger C2]; three pitch classes with a tritone do not determine the
  rotation [FACT — ledger C35]; and where a carried root is wrong, the separating evidence arrives after
  the moment [FACT — ledger C41]. A residual disagreement between a vertical reading and a reading by
  role "is a legitimate divergence between two readings, not an analyzer defect" [FACT — ledger C7].
  In one published segment-then-label system, 12% of the labelling errors were "an incomplete chord
  identifiable only through tonal function in context" [RULED — charter, DP-C, carrying Pardo and
  Birmingham 2002].
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Context terms add separating information where content cannot. **False-negative path:**
  passages where neither content nor context separates. Near-equal mass is the honest output.
- *Falsifier.* CODE. **Observable:** the inputs of the chord terms. **Decision rule:** falsified if the
  candidate score's preference between two chords with identical span content is independent of the
  adjacent spans' readings. **Not falsified by:** the preference being weak.
- *Ruled (cowork_rulings_2026_10_09_l2_context_in_chord_terms_sitting.md, Ruling 1).* "Algorithm: unchanged.
  L2-S30's wording does not change; nothing is added to or taken from the candidate score."
- *Beside L2-S30 (cowork_rulings_2026_10_09_l2_context_in_chord_terms_sitting.md, §2) — carried, not decided.*
  "No source held measures the gain from context over content alone on the same data with its uncertainty
  (surface §A.2); the size of that gain is what the fitted weights show (L2-S38)."

### 3f. Face (f) — the candidate score, and how its parts combine

**L2-S31. The candidate score of a reading is a sum over its spans of span terms, plus a sum over
adjacent span pairs of pair terms. A span term reads the span's position, its content (sounding set,
assignments, attachments), the evidence at and inside it, and its four fields. A pair term reads two
adjacent spans' fields and the evidence at their shared boundary. Span length is a variable of the
reading, not a fixed grid.**
- *Defense.* DP-C chooses segmentation decided "with" the chord (semi-Markov). Its grounds include "the
  formal result that letting segment length be a decoded variable buys the expressive power of a
  high-order model at linear rather than exponential inference cost", and a jointly decoding segmental
  model beating event-level tagging by 7.6 to 38.2 points of segment F-measure on one corpus [RULED —
  charter, DP-C]. The published semi-Markov systems use exactly this decomposition, a segment-label
  score plus a label-transition score [FACT (relayed, 08) — Masada & Bunescu, eqs. 3–5; Yang,
  Cwitkowitz & Duan 2023, eq. 3]. The second states it as "segment-level scores that are dependent only
  on the current and the previous segments". Removing the semi-Markov decode was the largest loss of
  any component in the one published ablation (root −0.012, quality −0.028, under-segmentation −0.044)
  [FACT (relayed, 08) — Yang, Cwitkowitz & Duan 2023, Table 2; single figures, no spread reported].
- *Source class.* Derived (inside the charter's DP-C).
- *Status.* Settled.
- *Premise.* Pairwise dependence between adjacent spans is enough. **False-negative path:** longer
  syntax, such as a ii–V–I, or a dominant prolongation across several spans. The pair terms see only
  the II→V and V→I links. Whether a hierarchical model is needed is DP-O, which the charter leaves open
  and "not foreclosed" [RULED — charter]. This form does not foreclose it.
- *Falsifier.* CODE. **Observable:** the candidate score's decomposition. **Decision rule:** falsified
  if some term reads three or more spans' fields, or if span length is fixed in advance. **Not
  falsified by:** a pair term reading L1 evidence inside both spans.
- *Beside L2-S31 (cowork_rulings_2026_10_07_l2_score_decomposition_sitting.md, Ruling 1) — carried, the
  remedy named.* "**Carried, not dropped (#12):** if the measurement-design stage finds L2 losing the choice
  between a key and its relative major or minor over whole passages, a piece-level tonality term is the
  named remedy, and D-616's proof obligation goes with it — show that it reinforces the cases where the mode
  is already clear rather than regressing them."
- *Beside L2-S31 (cowork_rulings_2026_10_07_l2_score_decomposition_sitting.md, Ruling 3) — recorded with the
  ruling, the surface's reading and not a new requirement.* "**Recorded with it, as the surface's reading
  and not a new requirement:** if an over-read of the old kind returned, it would show as a heavy weight on
  assignment-blind forms of L2-S32's terms, where the measurement-design stage would see it."
- *Beside L2-S31 (cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md, the section "A note for whoever
  takes up DP-O — recorded on the user's instruction") — carried for whoever takes up DP-O; the note decides
  nothing.* "**The user's words:** "record that note since we do not yet know (without measurement) if pairs
  are better or worse than longer chord sequences."" "L2-S31 (placed 2026-10-07 with its wording unchanged)
  has L2 score a reading by single spans and adjacent pairs only, and is "falsified if some term reads three
  or more spans' fields". Its premise, that pairwise dependence is enough, is unmeasured. `FRAMEWORK.md`
  DP-O asks only whether to adopt a hierarchy, and its falsifier compares a tree model against a
  matched-capacity sequence model. **A middle option is named by neither:** a flat chain whose terms may
  read three or more adjacent spans — a longer chord-to-chord memory, a cadential-formula term, or the
  sequence term carried as the remedy under Ruling 1. **When DP-O is taken up, the measurement compares
  pairs, longer flat terms and a hierarchy, on this repertoire's ground truth, the same corpus and the same
  axis.** Whether pairs are better or worse than longer chord sequences is not known without that
  measurement (D-254). Cost is not by itself a ground to keep pairs (D-200)." "**Added by Ruling 4:**
  harmonic rhythm — whether a reading's chord changes speed up towards a likely cadence, rated per competing
  reading inside L2 — is a further candidate longer-span term for the same measurement." "This note decides
  nothing: L2-S31's wording and placement are unchanged, and DP-O stays open. *(The defense L2-S31 cites —
  that a decoded segment length buys "the expressive power of a high-order model" — is, in this side's
  reading, about how long a chord lasts and not about chord-to-chord syntax.)*"
- *Ruled (cowork_rulings_2026_10_07_l2_score_decomposition_sitting.md, Rulings 1 and 3).* "L2-S31's wording
  does not change."

**L2-S32. The span content term rates how the span's events, under the reading's assignments, fit
the chord in its spelled form. It counts both what sounds and does not belong (purity) and what
belongs and does not sound (coverage), each with duration-weighted and metric-weighted forms. Chord
tones, elaborations and the absence of chord members each contribute. The coverage part is a cost,
never a requirement (L2-S10).**
- *Defense.* The feature families of the published segmental system are purity, coverage (root, third,
  fifth, added note, all members), bass, bigrams and metrical accent, each in plain, duration-weighted
  and accent-weighted forms, with "figuration-controlled" twins that ignore the notes detected as
  figuration [FACT (relayed, 08) — Masada & Bunescu, §4 and Appendix C]. Segment-level coverage is
  credited for correct labels where the first event lacks the root [FACT (relayed, 08) — Masada &
  Bunescu, §6.2.1]. A neural system adds an "absence" score for pitches that do not sound. It was not
  shown to help on its data [FACT (relayed, 08) — Yang, Cwitkowitz & Duan 2023, Table 2], and that is
  recorded so the absence side is not over-weighted by assumption.
- *Source class.* Derived. Weights *measured*, UNESTABLISHED.
- *Status.* Settled in shape.
- *Premise.* Figuration-controlled forms are well defined because the assignments are part of the
  reading. **False-negative path:** none beyond L2-S24's.
- *Falsifier.* CODE. **Observable:** the content term's inputs. **Decision rule:** falsified if the
  term reads an unspelled pitch class where the spelled pitch is available, or if it treats a missing
  chord member as disqualifying. **Not falsified by:** a fitted weight near zero on some form.
- *Beside L2-S32 (cowork_rulings_2026_10_09_l2_span_content_term_sitting.md, Ruling 2).* The arm this ruling
  adds to OQ-L2-3's held-out comparisons — the content term with an elaboration's contribution split by
  whether its spelled pitch lies in the span's spelled tonality's collection — is quoted beneath OQ-L2-3 in
  §4.
- *Ruled (cowork_rulings_2026_10_09_l2_span_content_term_sitting.md, Ruling 1).* "Algorithm: unchanged.
  L2-S32's wording does not change."
- *Pointer (written at the ratification of face (f), cowork_rulings_2026_10_13_l2_face_f_ratification_sitting.md,
  correction 2).* The observation recorded with score decomposition Ruling 3
  (cowork_rulings_2026_10_07_l2_score_decomposition_sitting.md), quoted beside L2-S31, bears on this
  statement's terms.

**L2-S33. The elaboration term for an event whose anchor, the preparing or resolving note, lies in an
adjacent span reads that adjacent span's candidate reading. The candidate score is therefore not the
"weak" semi-Markov form, in which a span term sees only its own label. It is a form in which the pair
term also carries the elaborations that cross the boundary.**
- *Defense.* A suspension is prepared in the previous harmony and resolved in its own. An anticipation
  sounds before the harmony it belongs to [THEORY]. The published weak-form system had to invent "a
  heuristic to determine whether an anchor note is harmonic whenever the anchor note belongs to the
  previous segment", because its "features … do not have access to the candidate label y_{k−1}" [FACT
  (relayed, 08) — Masada & Bunescu, Appendix B, p. 15]. The general semi-Markov form permits
  previous-label-conditioned segment scores. Both published musical systems use the weak form for speed
  [FACT (relayed, 08) — Yang, Cwitkowitz & Duan 2023, §3.2, as the extract compares them with Sarawagi &
  Cohen]. Using the weak form would replace a decided fact (the adjacent chord) with a guess, which is
  the first-running-detector defect in miniature (L2-S23).
- *Source class.* Derived.
- *Status.* Settled. Its cost falls on L2-S36.
- *Premise.* Elaborations cross at most one boundary. **False-negative path:** a long pedal point
  crossing several spans. Its assignment per span (L2-S9) and the pair terms handle each crossing
  separately, which is enough if "pedal point" is an admitted relation (OQ-L2-4).
- *Falsifier.* CODE. **Observable:** the elaboration term's inputs. **Decision rule:** falsified if the
  term for a suspension reads a heuristic stand-in for its preparing span's chord rather than that
  span's candidate chord. **Not falsified by:** a precomputed consonance feature used beside it.
- *Recorded (cowork_rulings_2026_10_09_l2_crossing_elaborations_sitting.md, §1, "Recorded beside it, not
  ruled").* "L2-S33's premise condition ("which is enough if "pedal point" is an admitted relation
  (OQ-L2-4)") is met by the elaboration record's Ruling 1; the application act may say so beside the
  premise." OQ-L2-4 is marked ANSWERED in §4, and the ruled list of relations, pedal point among them,
  stands beside L2-S8 (cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling 1). Recorded by
  the record as this side's derivation, not ruled; challengeable.
- *Beside L2-S33 (cowork_rulings_2026_10_09_l2_crossing_elaborations_sitting.md, Ruling 2).* The item this
  ruling adds to OQ-L2-3's list of held-out measurements — whether an elaboration's relation is named inside
  the candidate score or derived from the decided reading afterwards — is quoted beneath OQ-L2-3 in §4.
- *Ruled (cowork_rulings_2026_10_09_l2_crossing_elaborations_sitting.md, Ruling 1).* "Algorithm: unchanged.
  L2-S33's wording does not change."
- *Pointer (written at the ratification of face (f), cowork_rulings_2026_10_13_l2_face_f_ratification_sitting.md,
  correction 2).* The notated-boundary-flag item under OQ-L2-3 in §4
  (cowork_rulings_2026_10_07_l2_notated_boundary_evidence_sitting.md, Ruling 2) measures a term in this
  statement's pair term.

**L2-S34. The candidate score carries three families of terms relating the four fields across spans.
(i) Tonality persistence and distance: a cost for a tonality change, graded by the distance between
the two tonalities in a published tonal space. (ii) The tonality–chord cost, of L2-S3. (iii)
Progression: a term on the pair of adjacent chords *read as degrees in their tonalities*, including
the cadential progressions that confirm a tonality. Each family's weights are fitted.**
- *Defense.* (i) Two published joint systems weight transitions by Lerdahl's tonal-pitch-space distance
  [FACT (relayed, 08) — Rocher et al. 2010, §2.3; Catteau, Martens & Leman, §2.1]. One key finder uses
  Weber's table rather than the circle of fifths, "because Mozart often switched between Major and minor
  modes of the same key", and its Weber term was the one that stabilised the reading ("preventing the
  algorithm from switching keys for only 1 or 2 beats when a nonchord tone do appear") [FACT (relayed,
  08) — Feisthauer et al. 2020, §2.3, §4.3]. (ii) The charter [RULED]. (iii) A progression term on
  degrees rather than on root intervals, because "a V-I transition has a different distribution than a
  I-IV transition, even though the root distance is the same", and "using key context could further
  improve chord recognition" [FACT (relayed, 08) — Masada & Bunescu, p. 4, the authors' stated reason].
  A term rewarding continuity of the previous root "suppresses wrong root changes and correct ones
  alike" [FACT — ledger C29]. So no progression term may reward mere persistence of the root. A V→I
  heuristic used alone as tonality evidence had low precision (29 true of 116 detected in one movement)
  [FACT (relayed, 08) — Feisthauer et al. 2020, Table 1]. That is why confirmation is carried by the
  progression term over *proposed* chords, not by a separate detector.
- *Source class.* Derived. The distances are *given* by published theory (THEORY: Lerdahl's tonal pitch
  space; Weber's table). **Which of the two is used, and the weights, are *measured*, UNESTABLISHED.**
- *Status.* Settled in shape. **Open** in value and in the choice of tonal space (OQ-L2-3).
- *Premise.* Distances in a published tonal space order the plausibility of tonality changes on this
  repertoire. **False-negative path:** Romantic enharmonic and chromatic-mediant modulations, which the
  Weber table is, by its user's own caveat, "relevant mostly for the classical period" to rate [FACT
  (relayed, 08) — Feisthauer et al. 2020, §2.3]. The fitted weight on the distance then under-rates them.
- *Falsifier.* CODE. **Observable:** the terms' inputs. **Decision rule:** falsified if the progression
  term reads root intervals without the tonality, or if any term rewards the previous root continuing.
  **Not falsified by:** a fitted weight near zero on one family.
- *Recorded (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, §1f).* Stands as
  derived — recorded by the record as this side's derivation, not ruled; challengeable. "**The family is
  placed whole**, save Row 10.28 (L2-S39's family) and the two travelling rows (L2-S37's family). L2-S34
  stands as derived; the two held-out comparisons added to OQ-L2-3 (Rulings 3 and 4) are additions to its
  open question, not changes to its wording."
- *Beside L2-S34 (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 3).* The
  candidate this ruling adds to OQ-L2-3's held-out comparison of tonal spaces, which this statement's
  *Status* names, is quoted beneath OQ-L2-3 in §4.
- *Beside L2-S34 (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 4).* The
  held-out comparison this ruling adds to OQ-L2-3's list, for a separate entry term, is quoted beneath
  OQ-L2-3 in §4.
- *Beside L2-S34 (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 1) —
  carried, the remedy declined now and named.* "D-341's list entering L2 as a published-theory feature with
  one fitted weight (L2-S39's form) — a second term reading the same chord pair (#6), and a component no
  measured shortfall asks for (D-630, applied by analogy); it stays the named remedy if the
  measurement-design stage finds such a shortfall."
- *Beside L2-S34 (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 1) —
  carried, cost accepted.* "a motion theory licenses but the training music rarely uses gets a small counted
  value."
- *Beside L2-S34 (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 2) —
  carried, cost accepted.* "a key change can be chosen with no cadence at all where the fit repays it — what
  D-494 asks for, and the risk D-337 guarded against."
- *Beside L2-S34 (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 3) —
  carried, cost accepted.* "one more arm in a measurement already owed."
- *Beside L2-S34 (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 4) —
  carried, cost accepted.* "pairs across a change of key are rarer than pairs within one key, so their
  counts are thin; D-533's proportional share is what covers that (the surface's reading)."
- *Beside L2-S34 (cowork_rulings_2026_10_09_l2_published_theory_terms_sitting.md, Ruling 2).* The candidate
  this ruling adds to the held-out comparison of tonal spaces for L2-S34 (i)'s cost — a counted,
  transposition-invariant table over the circle-of-fifths distance between the tonics and the pair of modes
  — is quoted beneath OQ-L2-3 in §4.
- *Beside L2-S34's Source class (written at the ratification of face (f),
  cowork_rulings_2026_10_13_l2_face_f_ratification_sitting.md, correction 3).* The comparison of tonal spaces
  now holds four candidates: two added by the tonality-and-progression record's Ruling 3 (2026-10-06) and the
  published-theory record's Ruling 2 (2026-10-09), both quoted beneath OQ-L2-3 in §4. The derived wording
  stands.

**L2-S35. The candidate score is normalised over whole readings: the masses of all readings of the
working span sum to one. No span's alternatives are normalised against each other alone.**
- *Defense.* Per-state normalisation creates the label-bias problem. The transitions leaving a state
  "compete only against each other", and "Viterbi decoding cannot downgrade a branch based on
  observations after the branch point" [FACT (relayed, 08) — Lafferty, McCallum & Pereira, §2]. The
  charter's reason for forbidding early discarding is the same shape: a wrong reading can be a local
  optimum [RULED — charter, L2; ledger C45]. Evidence after a moment is often the separating evidence
  [FACT — ledger C41, C2]. A model whose masses are normalised per span would let later evidence change
  which branch wins but not how much mass flows into the branch. That is the defect.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* Whole-reading normalisation is computable (L2-S36). **False-negative path:** none on the
  modelling side. The cost is computational.
- *Falsifier.* CODE. **Observable:** the masses. **Decision rule:** falsified if the published masses
  of a span's rivals sum to one by construction independently of the other spans, or if adding
  evidence after a span cannot change the total mass of a branch through it. **Not falsified by:**
  marginals that sum to one per span because they are marginals of a whole-reading distribution.
- *Beside L2-S35 (cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 3).* "The forward override
  of D-339 ("A confident earlier inference can be overturned by decisive later evidence, via one general
  confidence-weighted forward-recompute mechanism") has no site in L2: inside L2 key, boundaries, notes'
  roles and chord are one decision scored over the whole loaded music; at L2's boundary the contract table
  reads "L3 → L2: **Nothing.**" The framework's general admission of the act (§8.4, Δ8) is untouched."

**L2-S36. The search is exact, or it prunes only by a bound that provably cannot discard a reading
whose final candidate score could exceed a kept reading's. No beam that discards readings on partial
candidate scores is admitted. Where exactness is not affordable, the charter's rule, not the search,
is what must give way, and that is a ruling (OQ-L2-8 ★).**
- *Defense.* The charter forbids discarding a rival before the whole sequence of spans has been scored
  [RULED — charter]. A beam that drops partial hypotheses does exactly that. The published beam-search
  system reports "the beam holds alternatives during search and commits one" [FACT (relayed, 08) —
  McLeod & Rohrmeier 2021, coupling facts]. The semi-Markov dynamic programme is exact and linear in
  input length for a fixed maximum span length [FACT (relayed, 08) — Masada & Bunescu, p. 3]. Without
  the bound it is quadratic, by the neural system's own statement [FACT (relayed, 08) — Yang, Cwitkowitz
  & Duan 2023, §6]. One published model found its state small enough that "the size of our state space
  allows for full-fledged dynamic programming", with 168 labels [FACT (relayed, 08) — Raphael & Stoddard
  2003, p. 4]. L2's joint state is far larger: 42 tonalities × a vocabulary of degrees, qualities,
  figures and applied chains × the pair-term dependence of L2-S33. Whether exact inference fits is a
  measurement this session cannot make. "Make it work first; compromise on performance only if it
  proves a problem" is a standing convention [RULED — pack member 02, Conventions]. A search that
  quietly discards would be a correctness compromise dressed as a performance one.
- *Source class.* Derived. The tractability is *measured*, UNESTABLISHED.
- *Status.* Settled as a rule. **Open** on whether it can be met (OQ-L2-8 ★).
- *Premise.* A safe bound exists, as in A* with an admissible heuristic, or exact inference fits.
  **False-negative path:** neither is true for large scores. The user then rules between a narrower
  admission rule (L2-S2's ceiling cost) and a relaxation of the no-discarding rule.
- *Falsifier.* CODE. **Observable:** the search's pruning. **Decision rule:** falsified if any
  hypothesis is dropped on a partial candidate score without a bound certifying that it cannot finish
  above a kept one. **Not falsified by:** readings of zero mass (probability zero, not merely low) never
  being enumerated.
- *Ruled (cowork_rulings_2026_10_05_l2_tractability_sitting.md, Ruling 1).* Stands as derived. "(i) **L2-S36
  stands as derived**: the search weighs every reading it has begun to score through to the end, or drops
  one only by a bound that provably cannot discard a reading that could win; no beam that discards on
  partial candidate scores; where exactness is unaffordable, the charter's rule gives way only by a ruling.
  **OQ-L2-8 stays open as derived.** (ii) **"The end" is the end of the music loaded for the selection** —
  the working span with its context (L2-S43), the context extended by convergence (D-261) under the safety
  cap (D-624) and C-8's scaling — not the end of the whole score, unless the whole score is the selection or
  convergence does not settle before the cap. (iii) **D-297 and L2-S36 govern different acts**: a reading
  the admission rule never generates is not discarded (D-297, `FRAMEWORK.md` §8.4; the admission rule itself
  governed by L2-S2's closure test with exclusions ruled by name); L2-S36 bars dropping a reading the search
  has begun to score. **Proposed addition to L2-S36:** "A reading the admission rule never generates is not
  discarded (D-297; FRAMEWORK §8.4); what this statement bars is dropping a reading the search has begun to
  score." (iv) An effort setting may not quietly reduce how many readings the search keeps; if one ever
  does, that is the ruling OQ-L2-8 names."
- *Beside L2-S36 (cowork_rulings_2026_10_05_l2_tractability_sitting.md, Ruling 1 (iii)) — the proposed
  addition, written beside the statement and not into its bold text.* "A reading the admission rule never
  generates is not discarded (D-297; FRAMEWORK §8.4); what this statement bars is dropping a reading the
  search has begun to score."
- *Recorded (ratification_surfaces/cowork_l2_search_sizing_2026_10_05.md, §8 and §C) — recorded as following
  from the record and the user's word, not as a ruling; written at the ratification of face (f),
  cowork_rulings_2026_10_13_l2_face_f_ratification_sitting.md, correction 4.* (a) §8: "The sizing cannot tell
  whether exact search is affordable at D-201's sizes." (b) §C, *What it settles*: "§8's outcome ("whether a
  code trial may run inside this phase comes to the user") is not put: no code trial and no timing measurement
  is owed before L2's specification is ratified. What is owed instead is that the specification names clear
  entry points where an effort setting applies. This is D-035 ("every cost-driving choice is a setting, never
  a hardcoded constant") and D-202 (one setting, several dials, bounding time) applied to L2, so it is recorded
  as following from the record and his word, not as a new ruling. Which dials exist, and their defaults, are
  decided when the effort setting is built and measured (D-202 stays DEFERRED), not before ratification. The
  tractability record's §1b item 2 sent the dials question to him "before this layer's specification is
  ratified"; his word moves it to the build." (c) §C, *The entry points this sizing locates* (*my reading*, a
  proposal for the application act, not ruled): "(a) the admitted chord vocabulary — which chords may be
  applied and how deep (§3.3), and later the allowed modes under the modal increment, following a style
  setting as he describes; (b) which terms and algorithms run — for instance the crossing-elaboration link
  (§3.5), or a table-only chord reading at the lowest setting, as his example; (c) the context extension's
  limit (D-261, under D-624's cap); (d) a stretch-length cap (§3.2); (e) any reduction of the readings kept.
  Each is a setting the user turns, so none is the "quiet" reduction Ruling 1 (iv) of the tractability record
  bars. The top setting is exact, as L2-S36 states." (d) §5, *Limit 1 — masses* (*my reading*, UNSETTLED; its
  "second speed-up above" is that section's "A provably safe bound"): "A safe bound protects the principal
  reading, not the masses: a reading dropped because it cannot win still carried some mass. The derivation's
  falsifier for L2-S36 excuses only readings of zero mass. So the second speed-up above may be available for
  the principal reading and not for the rivals' masses. This bears on OQ-L2-8 and L2-S35; it is recorded, not
  decided." Section numbers inside these quotations are the sizing's.

**L2-S37. L2 may read L1's cadence cues as evidence only as their establishment status allows. The
leading-tone cue (IC S-46) is *computed* and may carry load. The falling-fifth cue (IC S-45) and the
fourth-and-seventh cue (IC S-47) rest on the stand-in cue window and are *provisional*. No term of the
fitted candidate score reads them until the window is established.**
- *Defense.* "A consumer may not put a provisional item under load until the parameter is
  established" [RULED — IC S-52]. S-48's stand-ins were accepted as provisional on the condition "no
  item resting on them put under load" [RULED — IC beside S-48, Ruling 53]. S-45 searches back within
  the window, and S-47 tests degrees within the window [RULED — IC S-45, S-47]. S-46 reads the slice
  immediately before Z [RULED — IC S-46], so it does not rest on the window. The measurement that would
  establish the window is named as "owed to L2's calibration" [RULED — IC S-48]. It is therefore L2's to
  commission, and it is OQ-L2-12. The progression term of L2-S34 already reads the proposed chords'
  cadential motion, so nothing L2 needs waits on the provisional cues.
- *Source class.* Given — input contract.
- *Status.* Settled.
- *Premise.* None beyond the input contract's.
- *Falsifier.* CODE. **Observable:** the fitted terms' inputs. **Decision rule:** falsified if a fitted
  term reads a provisional-status cue. **Not falsified by:** an experimental, unfitted term reading it
  in a measurement run that is itself establishing the window.
- *Beside L2-S37 (cowork_rulings_2026_10_09_l2_cadence_cues_sitting.md, Ruling 2).* The item this ruling
  adds to OQ-L2-3's list of held-out measurements — the candidate score with a cue term against the same
  score without it — is quoted beneath OQ-L2-3 in §4.
- *Ruled (cowork_rulings_2026_10_09_l2_cadence_cues_sitting.md, Ruling 1).* "Algorithm: unchanged. L2-S37's
  wording does not change."

**L2-S38. Every weight of the candidate score is fitted from annotated music, not set by hand. The
tables are counted from annotated music, once, and frozen; the short list of combination weights is
fitted discriminatively, to the graded measure. Its objective
is the graded measure, not likelihood alone. It is fitted only on freely licensed music. It treats
every recorded analyst variant as an acceptable answer. No value is given here.**
- *Defense.* No value is graded on data that helped fit it. Held-out data and a capacity budget are
  declared before fitting [RULED — principle #20, pack member 02]. Fitting combination weights by
  likelihood was measured at 12.2 against 19.6 on the wanted metric when the weights were fitted to that
  metric [RULED — charter, DP-P]. The published method is minimum error-rate training over a candidate
  list [FACT (relayed, 08) — Och, §4, eqs. 5, 7]. A value that ships is fitted only on public-domain,
  CC0 and CC-BY music [RULED — D-292]. The ground truth carries analyst variants [FACT — ledger C16;
  exemplar 5], and the grading bar counts any recorded reading as defensible [RULED — D-352]. A fit that
  penalised a recorded variant would push weights away from a reading the grading accepts. The
  antipattern, recorded so it is not repeated: a published key finder grid-searched its three weights
  on the same 38 movements it reported on, writing that "no training set was separated from the
  corpus" [FACT (relayed, 08) — Feisthauer et al. 2020, §4.3].
- *Source class.* *Measured*: the fit needs annotated spans with tonality, chord, figure and applied
  target, and assignments derived from them; a held-out split by piece; a capacity budget; and the
  graded measure fixed by the measurement-design stage. **UNESTABLISHED.**
- *Status.* **Open** (the fit is the measurement-design stage's and a later act's).
- *Premise.* The annotated corpora carry what the fit needs. **False-negative path:** assignments are
  not annotated anywhere. The published first-running detector's ground truth was derived from chord
  labels [FACT (relayed, 08) — Ju et al. 2017, §2], so assignments are at best derived from the chord
  annotation, which makes their fit circular. OQ-L2-13 carries this.
- *Falsifier.* CODE. **Observable:** the fit record. **Decision rule:** falsified if any weight is
  hand-set in the shipped model, if the evaluation data overlap the fit data, or if the fit pool
  contains music under a non-commercial or unstated licence. **Not falsified by:** a hand-declared
  provisional value used in a desk simulation and marked as such (principle #17's desk-simulation
  rule).
- *Amended (cowork_rulings_2026_10_05_l2_fit_sitting.md, Ruling 1) — the statement's second sentence.* "The
  term tables of L2's candidate score are counted from annotated music, once, and frozen; the short list of
  combination weights over them is fitted discriminatively, **to the graded measure**. D-525's staging
  stands (each table established on its own; the combination-weight list within D-271's budget); D-525's own
  recorded fallback — the direct-metric few-weight search, the minimum-error-rate protocol — becomes the
  main route, and a likelihood fit may still serve as its starting point. **L2-S38's second sentence is to
  be amended** to: "The tables are counted from annotated music, once, and frozen; the short list of
  combination weights is fitted discriminatively, to the graded measure." Every other sentence of L2-S38
  stands. **DP-P is answered for L2's detail specification by this ruling.** Joint learning of every number
  (Position 3, D-525's recorded excluded alternative) is not adopted; D-525's re-test condition for it
  stands as D-525 records it." (was: "The fit is discriminative, on held-out folds, with its capacity budget
  declared in advance."; cowork_rulings_2026_10_05_l2_fit_sitting.md, Ruling 1)
- *Beside L2-S38 (cowork_rulings_2026_10_05_l2_fit_sitting.md, Ruling 1) — carried, UNSETTLED.* "which
  licence class the chorale analyses fall in (Row 1.24, OI-271, relayed) — every count and fit depends on
  it; what exactly the graded measure is; whether the plain counted model (all weights one) remains a
  mandatory comparison arm under this ruling (D-525's arm, Row 48.36, already relocated to measurement)."
- *Beside L2-S38 (cowork_rulings_2026_10_05_l2_fit_sitting.md, Ruling 2).* "(i) D-383's fixed ranking —
  bass, spelling and key-consistency "decide", a licensed progression "only breaks ties" and "may never
  override a committed root" — **does not carry into L2's specification**, neither as a rule nor as a
  constraint on the fitted weights. Its measured finding (the progression-driven override moving a correct
  root to a wrong one on about 78 % of its fires) is kept as evidence, already set aside for the audit at
  Row 8.74(i). D-383's register status is settled at the ratification act, not here (the shape used for
  D-333 and D-385). (ii) The old fitter's exemption for "any value whose Phase-0 row names a ratified
  structural rationale" (Row 9.160(iii)) **does not carry**: it governed the legacy scorer's hand-set
  constants, and L2 has none."
- *Beside L2-S38 (cowork_rulings_2026_10_05_l2_fit_sitting.md, Ruling 3).* The interim ruled for OQ-L2-13,
  which this statement's *Premise* names, is quoted beneath OQ-L2-13 in §4; the question stays open.

**L2-S39. A distance or profile taken from published theory (Lerdahl's tonal pitch space, Weber's
table, a scale-degree profile) enters the candidate score as a feature whose single weight is fitted.
Its internal constants are the published ones, unchanged, and are not tuned on evaluation music.**
- *Defense.* Fitting a published theory's internal constants would make the theory a fitted table, and
  its establishment would then rest on the fit, not on the theory [RULED — principle #19]. Keeping them
  fixed and fitting one weight keeps the capacity small and the provenance of each part separate. The
  published systems that use these distances hand-set their exponents "after experiment" (1.1 and 1.01)
  [FACT (relayed, 08) — Rocher et al. 2010, §2.3] or set normalisers from stated presumptions [FACT
  (relayed, 08) — Catteau, Martens & Leman, p. 14]. Both are uses of evaluation-adjacent data or
  presumption that the rule above excludes.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise.* The published constants are good enough in shape that a single weight suffices.
  **False-negative path:** a distance whose shape is wrong for this repertoire. The fitted weight tends
  toward zero, and the fix is a different published space, ruled, not a tuned one.
- *Falsifier.* CODE. **Observable:** the fit's parameter list. **Decision rule:** falsified if any
  internal constant of a published distance is a fitted parameter. **Not falsified by:** choosing
  between two published spaces by held-out comparison.
- *Beside L2-S39 (cowork_rulings_2026_10_09_l2_published_theory_terms_sitting.md, Ruling 3) — the forms
  rule.* "Every term's form is taken from established music theory or published research and fixed before
  any value is attached to it (L2-S39 being the case of a published distance or profile)." "**Algorithm, as
  the specification defines it:** L2's specification gains the forms rule — a rule every term, present and
  future, must meet. No present term is learned; whether every present term's form traces to published
  theory or research was not checked term by term (the research iteration is where it would be). **L2 states
  no rule on learned terms** until the research iteration and, if it finds reason, a held-out measurement
  decide one. No other statement's wording changes." *Cost accepted:* "until the research iteration, L2's
  specification is silent on learned terms, so a learned term proposed before then is judged on #1 alone."
- *Beside L2-S39 (cowork_rulings_2026_10_09_l2_published_theory_terms_sitting.md, Ruling 2).* The candidate
  this ruling adds to the held-out comparison of tonal spaces for L2-S34 (i)'s cost — a counted,
  transposition-invariant table over the circle-of-fifths distance between the tonics and the pair of modes
  — is quoted beneath OQ-L2-3 in §4.
- *Beside L2-S39 (cowork_rulings_2026_10_09_l2_published_theory_terms_sitting.md, §1d) — carried as a bound,
  not ruled.* "**Carried as a bound, not ruled:** a published space or profile entering under L2-S39 needs
  its primary fetched and read before its constants carry load (D-473; the tonality-vocabulary record's
  Ruling 1); neither Lerdahl's nor Weber's primary is held."
- *Ruled (cowork_rulings_2026_10_09_l2_published_theory_terms_sitting.md, Ruling 1).* "Algorithm: unchanged.
  L2-S39's wording does not change."
- *Pointer (written at the ratification of face (f), cowork_rulings_2026_10_13_l2_face_f_ratification_sitting.md,
  correction 2).* The bass-scale-degree item under OQ-L2-3 in §4
  (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 3) says a published form of the Rule of the
  Octave would enter under this statement.

### 3g. Face (g) — the rivals, their mass, and the bar on early discarding

**L2-S40. *Mass* is the probability the fitted, whole-reading-normalised model (L2-S35) assigns. A
span-rival's mass is the marginal: the total mass of all whole readings that contain that span, with
that start, that end and that reading of it. Until a reliability map is fitted, mass is a model
quantity and not a calibrated probability. A consumer may compare masses within one working span's
publication and may not read them as frequencies of being right.**
- *Defense.* The charter publishes "the rivals with their mass" and leaves the meaning to the detail
  specification [RULED — charter]. The cross-layer confidence contract fixes two admissible classes. A
  decision margin, which is "a rank statement, not a probability", and a calibrated probability, which "no
  layer may claim … until one is fitted" [RULED — D-267]. A confidence may be compared "only within one
  class and one declared frame" [RULED — D-268, U3]. A normalised model distribution is more than a margin,
  since it sums to one over readings, and less than a calibrated probability, since nothing has checked its
  frequencies. It is therefore published with its class stated as the model's own distribution,
  un-calibrated, and within that class it is neither a decision margin nor a calibrated probability — the
  third kind the confidence contract is to name (cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md,
  Ruling 1). (was: "and within that class it behaves as a margin for the purpose of D-267.";
  cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 1) The marginal is the right per-span
  quantity because the charter's rivals include boundary rivals (L2-S15). A marginal over (start, end,
  reading) counts a boundary rival and a label rival alike, where a marginal over labels at a moment would
  merge them.
- *Source class.* Derived (inside D-267 and D-268, which are given).
- *Status.* Settled. Its class is the third kind, the model's own distribution
  (cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 1; OQ-L2-14 ANSWERED). (was: "Settled. How
  the class of this quantity is named against D-267's two is OQ-L2-14.";
  cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 1; brought into line on the user's word of
  2026-10-13 before Task 0)
- *Premise.* The model is a proper distribution over readings. **False-negative path:** a candidate
  score used with no normaliser (a pure maximum). Mass would then be undefined, and L2-S35 forbids that.
- *Falsifier.* CODE. **Observable:** the published masses. **Decision rule:** falsified if a span's
  published rival masses exceed one in total, if a mass is labelled calibrated before a reliability
  map exists, or if a boundary rival and a label rival over the same stretch are merged into one mass.
  **Not falsified by:** masses summing to less than one because some rivals fall below the cut-off the effort
  setting sets (L2-S42). (was: "masses summing to less than one because some rivals fall below the publication
  threshold (L2-S42)."; cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling 1)
- *Beside L2-S40 (cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 1).* "A span-rival's weight
  (the derivation's *mass*, L2-S40) is declared to be neither a decision margin (Class M) nor a calibrated
  probability (Class P), but a **third kind: the model's own distribution** — each value a share in [0,1],
  the shares of one stretch's rivals summing to at most one, not calibrated, compared only within one
  working span's publication, never read as a frequency of being right, and turned into a calibrated
  probability only through a fitted reliability map." "**What it amends, for the application act (wording
  not ruled here):** D-267 at its home (`cowork_confidence_contract.md` §2: "exactly one" of two classes
  becomes one of three); the confidence sentence of `FRAMEWORK.md` §7 and behavioural statement B9; and
  L2-S40's defense, which leaned to Class M. U1 to U5 of the contract are unchanged. D-267's register
  status, and D-425's, are settled at the ratification act, not here."
- *Beside L2-S40 (cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 1) — the Defense's "two
  admissible classes".* The Defense's sentence that the cross-layer confidence contract fixes two admissible
  classes is true of the contract's text as it stood when this statement was derived. Ruling 1 orders a
  third kind, the model's own distribution, added to the contract at D-267's home; once that amendment is
  made, the sentence describes the contract's former text. The derived wording stands.

**L2-S41. A rival that differs from the principal reading over several consecutive spans is
published as one rival object, with its extent (first and last position), its own spans and fields,
and its whole-reading mass. Each principal span it overlaps refers to it. A consumer therefore sees
one alternative, not several independent ones. Beside the per-span marginals of L2-S40, L2 publishes
the best whole readings, ranked, down to the bound the effort setting sets.**
- *Defense.* The charter's instruction to publish rivals "per span" does not say that rivals are
  independent across spans, and in the joint decision they are not. Reading bar 31 of exemplar 2's
  piece in D minor goes together with reading bar 32 in D minor. One analyst writes both, and the other
  writes neither [FACT at the files — exemplars 1 and 2]. Marginals alone lose that correlation. A
  consumer multiplying per-span marginals would give mass to mixtures no analyst writes, the
  "incoherent composite" the charter measures in systems that decide parts independently [RULED —
  charter, DP-A]. The ground truth writes a variant as a whole alternative stretch (`m17var1`,
  `m18var1`, `m19var1` in exemplar 5 carry one coherent alternative through three bars) [FACT at the
  file], and "the analyst writes an alternative reading in the same stream as the principal one" [RULED
  — charter, "NOT A LAYER"].
- *Source class.* Derived.
- *Status.* Settled in form. How many whole readings are published is an effort setting; its values are
  decided at the effort setting's build and remain an open measurement (OQ-L2-15). (was: "Settled in form.
  How many whole readings are published is *measured* (OQ-L2-15).";
  cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling 1; brought into line on the user's word
  of 2026-10-13 before Task 0)
- *Premise.* A small number of whole readings carries most of the correlated alternatives.
  **False-negative path:** a passage with several independent local ambiguities, where the number of
  whole readings grows as their product. The per-span marginals still carry each ambiguity, and the
  whole-reading list shows only the strongest combinations.
- *Falsifier.* CODE. **Observable:** the rival publication over a multi-span alternative. **Decision
  rule:** falsified if a coherent multi-span alternative appears only as unrelated per-span rivals, with
  no object linking them. **Not falsified by:** the per-span marginals also listing its spans.
- *Amended (cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling 1) — the statement's last
  clause.* "**L2-S41's clause "down to the threshold of L2-S42"** is to read "down to the bound the effort
  setting sets"." (was: "down to the threshold of L2-S42.";
  cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling 1)

**L2-S42. At the top effort setting L2 withholds no span-rival from publication. Below it, the effort
setting sets how deep the cut-off lies, continuously across settings: a span-rival below the cut-off may
be withheld only because it is recomputable, and the cut-off and the withheld total mass per span are
published with the rivals. The ranked list of whole readings is always bounded, and its length is an
effort setting. Below the top effort setting, a cut-off never removes every reading of a chord root
whose readings at a slice together carry weight above the cut-off; that root's best reading is kept, the
grouping by root being internal to L2 and nothing extra published.**
- *Defense.* A collapse is a loss only where the several values cannot be got back. Where the collapsed
  value "is derived deterministically from something still carried, or is regenerable from it, nothing
  has gone" [RULED — principle #12, the recomputable clause]. Every published record carries the table
  set's hashes, the weight vector's identity and the decoder's version [RULED — D-275], which is what
  makes regeneration possible. Publishing the withheld mass keeps the absence visible. An absence with
  no reason is a hidden fact [RULED — IC beside S-52, Ruling 62 item 7, for L1, applied here by the same
  principle].
- *Source class.* Derived.
- *Status.* Settled in form. How deep the cut-off lies below the top setting is decided at the effort
  setting's build and remains an open measurement (OQ-L2-15). (was: "Settled in form. The threshold's value
  is *measured* (OQ-L2-15)."; cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling 1; brought
  into line on the user's word of 2026-10-13 before Task 0)
- *Premise.* Recomputation is practical. **False-negative path:** a consumer outside the analysis that
  cannot rerun it, such as the display. For it the withheld rivals are gone. D-295's "every inferred
  object must be displayable" then requires the display to be able to request them, which is a
  consumer's design and not L2's.
- *Falsifier.* CODE. **Observable:** the publication at the top effort setting and at a lower one. (was:
  "the publication with and without the threshold.";
  cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling 1, and
  cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 2; brought into line on the user's word of
  2026-10-13 before Task 0) **Decision rule:** falsified if any span-rival is withheld at the top setting;
  if, below it, a rival is withheld without the cut-off and the withheld total mass per span being
  published, or cannot be regenerated from the named provenance; or if a cut-off removes every reading of a
  chord root whose readings at a slice together carry weight above it. (was: "falsified if a rival is
  withheld without the threshold and withheld mass being published, or if the withheld rivals cannot be
  regenerated from the named provenance."; cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling
  1, and cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 2; brought into line on the user's
  word of 2026-10-13 before Task 0) **Not falsified by:** a lower setting withholding rivals below its
  cut-off. (was: "a threshold of zero."; cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling
  1, and cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 2; brought into line on the user's
  word of 2026-10-13 before Task 0)
- *Amended (cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling 1).* "At the top effort
  setting the chord-and-key layer withholds no span-rival from publication. Below the top, withholding is
  allowed only as an effort setting, and **the depth of the cut-off is continuous, not on/off: different
  effort settings cut off at different depths** (the user's refinement). Wherever a setting withholds,
  L2-S42's safeguards hold: a withheld rival is withheld only because it is recomputable, and the cut-off
  and the withheld weight per span are published with the rivals. The ranked list of whole readings is
  always bounded, because it cannot in practice be complete beyond the shortest passages (D-297: never
  computing is not loss), and its length is likewise an effort setting." *The derived wording stands at the
  derivation, L2-S42.*
- *Beside L2-S42 (cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling 1) — carried, not
  ruled.* "The cut-off values and the defaults of each setting are not ruled here: they are decided at the
  effort setting's build (D-202 stays DEFERRED; the sizing's §C)."
- *Amended (cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 2) — one sentence added to the
  statement.* "Below the top effort setting, at any slice, a cut-off never removes every reading of a chord
  root whose readings there together carry weight above the cut-off; that root's best reading is kept. The
  grouping by root is internal to L2 (the root is the degree read in its key); nothing extra is published.
  L2-S42, as amended under the rival-publication sitting's Ruling 1, is to gain one sentence saying so (this
  side's wording for the application act; not ruled here)." *The derived wording stands at the derivation,
  L2-S42.*

**L2-S43. No reading is discarded before the whole working span, context included, has been scored.
Where two readings have equal candidate scores to the precision computed, both are published with
equal mass. The principal is chosen between them by a declared, deterministic rule that the
publication names, and the tie is flagged.**
- *Defense.* The no-discarding clause is the charter's [RULED — charter, L2 "May not"]. On ties: a tie
  decided silently by whichever reading the arithmetic happens to reach first would make the published
  principal depend on evaluation order rather than on the music, and would not be reproducible [RULED —
  principle #16, reproducibility]. A
  flagged tie with a named rule is reproducible and honest. A near-tie within a stated tolerance is
  reported as such, not as a win [RULED — principle #17's near-tie rule, applied by analogy to
  published decisions].
- *Source class.* Given — charter, for no-discarding. Derived, for ties.
- *Status.* Settled.
- *Premise.* Exact ties are rare. **False-negative path:** symmetric passages, such as a bare fifth
  read as major or minor. Ties are then common, and the tie flag carries the information.
- *Falsifier.* CODE. **Observable:** the publication at an exact tie. **Decision rule:** falsified if
  one of two tied readings is absent, or if the tie is not flagged. **Not falsified by:** the principal
  being the one the declared rule picks.
- *Recorded (cowork_rulings_2026_10_05_l2_no_early_discarding_sitting.md, §1b).* Stands as derived —
  recorded by the record as this side's derivation, not ruled; challengeable. "**L2-S43 stands as derived.**
  Its first sentence is the L2 charter's own rule (relayed); "the end" is fixed by Ruling 1 of the
  tractability record. Its tie rule follows from D-565 (LIVE), consistent with D-114 and the silence
  family's Ruling 1." Where "the end" is fixed, see the sub-item beside L2-S36
  (cowork_rulings_2026_10_05_l2_tractability_sitting.md, Ruling 1).
- *Beside L2-S43 (cowork_rulings_2026_10_05_l2_no_early_discarding_sitting.md, §1b) — the tie order,
  recorded by the record as this side's derivation and not a ruling; it follows from D-565; written beside
  the statement and not into its bold text.* "L2's declared tie order is D-565's — fewer spans first, then
  the earlier boundary sequence, then a fixed order of the readings' contents."
- *Beside L2-S43 (cowork_rulings_2026_10_05_l2_no_early_discarding_sitting.md, §1b) — carried, left open.*
  "**Left for the application act:** stating that fixed order over the note assignments as well."
- *Recorded (cowork_rulings_2026_10_14_l2_face_g_ratification_sitting.md, correction 2) — beside the carried
  item above; this side's reading, not ruled; challengeable.* "Recorded at the ratification of face (g), as
  this side's reading, not ruled: the successor's §0 defines a reading as including an assignment for every
  event, so 'a fixed order of the readings' contents' already orders the assignments; D-565 requires the order
  to be total. The order among assignments is the canonical order of the encoded reading, of the kind D-565's
  third key names."
- *Beside L2-S43's Defense sentence on near-ties (cowork_rulings_2026_10_05_l2_silence_and_no_chord_sitting.md,
  Ruling 1; written at the ratification of face (g), cowork_rulings_2026_10_14_l2_face_g_ratification_sitting.md,
  correction 3).* Read with the silence record's Ruling 1 (2026-10-05): a near-tie is reported by the two
  readings' masses; no flag is published for it. The one flag is the exact-tie flag of the statement. The
  derived wording stands.

### 3h. Face (h) — the boundaries of the layer

**L2-S44. Where a span's sounding set is empty (a silence L1 publishes as a silent slice, not merged
into a neighbour), L2 either extends the neighbouring harmony through it or publishes the span with a
chord field carrying a named reason ("silent"). The two are rivals. Whether a *sounding* span may be
published with "no chord", as distinct from "no confident chord", is the charter's open DP-Q, and is
not decided here.**
- *Defense.* L1 publishes every silent slice with its length and "is not merged into a neighbour"
  [RULED — IC S-31]. Whether the harmony continues through a silence is L2's question [RULED — IC S-53].
  DP-Q is open [RULED — charter]. It notes that the exemplar analyses carry no no-chord label, and that
  holds for the analyses this session read [FACT at the files — exemplars 2 and 5 whole, and the
  label lists of exemplars 1 and 3]. A silent span has no pitch content to read a chord from, so a named reason is
  the honest field, and the rival that extends the harmony through the rest is how analysts write
  across a rest [THEORY].
- *Source class.* Derived. The sounding case is given as open (charter DP-Q).
- *Status.* Settled for silent spans. **Open** for the sounding case (DP-Q, the charter's).
- *Premise.* A silence inside a phrase is usually heard as continuing the harmony. **False-negative
  path:** a general pause before a new section. The rival with the "silent" chord field carries it.
- *Falsifier.* CODE. **Observable:** readings over a silent slice. **Decision rule:** falsified if a
  silent span is published with a chord and no reason, or if the continuing reading is inadmissible.
  **Not falsified by:** either one carrying most of the mass.
- *Ruled (cowork_rulings_2026_10_05_l2_silence_and_no_chord_sitting.md, Ruling 1).* Stands as derived. "Over
  every stretch where notes sound, the chord-and-key layer infers and publishes its best reading of the
  harmony with the rival readings and their weights. **Even a reading with a very low weight is inferred and
  handed on.** Doubt is shown by the weights alone; there is no "uncertain" flag and no "no chord" answer
  over sounding music in the first specification. **The framework's DP-Q stays open exactly as ratified; no
  framework text is amended.** L2-S44's sounding half stands as derived." The named exclusion the ruling
  makes is quoted beside L2-S2.
- *Beside L2-S44 (cowork_rulings_2026_10_05_l2_silence_and_no_chord_sitting.md, Ruling 1) — carried with the
  ruling, the user's view and not a ruling.* "**Where showing it belongs (the user's view, given in the
  sitting and carried with the ruling as its stated ground, not as a separate ruling).** Whether a very
  low-weight reading is shown, shown greyed, or replaced by "N.C." is the display's decision — the product
  stance the ratified amendment D-498 says is still owed — and may include a user minimum-confidence
  setting. **The caution carried with it:** the weights are not calibrated, and a consumer "may compare
  masses within one working span's publication and may not read them as frequencies of being right"
  (derivation, L2-S40), so a minimum-confidence setting that means the same in every piece needs a fitted
  calibration first."
- *Beside L2-S44 (cowork_rulings_2026_10_05_l2_silence_and_no_chord_sitting.md, Ruling 1) — carried.* "**The
  costs, carried.** D-498's owed decision about mostly-doubtful and non-tonal music is not answered inside
  this layer and stays owed. Over non-tonal music the layer still names a tonal reading; whether its weights
  spread out there is unmeasured. The exclusion's ceiling cost is uncounted."
- *Beside L2-S44 (cowork_rulings_2026_10_05_l2_silence_and_no_chord_sitting.md, Ruling 1) — carried, what it
  does not decide.* "**What it does not decide.** Whether any graded collection writes a no-chord label; how
  an annotation over a silence is graded; whether the weights spread out over non-tonal music; where and how
  D-498's display decision is written. **The silent half of L2-S44 and the twenty rows' placements are the
  sitting's second question and are not ruled here.**"
- *Ruled (cowork_rulings_2026_10_05_l2_silence_and_no_chord_sitting.md, Ruling 2).* Stands as derived.
  "L2-S44's silent half stands as derived. A rest in any voice — one voice or all — is evidence the
  chord-and-key layer weighs; it never forces and never forbids a harmony change (L2-S13). The note-cutting
  layer publishes which voice went silent and whether every voice is silent (the L0/L1 derivation's S-39
  REST-BEGINS and ALL-SILENT flags, and S-31's silent slice not merged into a neighbour; surface §2). A
  complete silence carries two rival readings with their weights: the harmony continues through it (a rest
  inside a phrase — the chord before carries on, or the next has already begun), or a silent stretch with no
  harmony, labelled as silent (a general pause)."
- *Beside L2-S44 (cowork_rulings_2026_10_05_l2_silence_and_no_chord_sitting.md, Ruling 2) — carried,
  UNSETTLED.* "**Left for the application, not ruled:** which side a harmony may extend from into a silence;
  which tonality a silent stretch carries (L2-S16 gives every span exactly one)."

**L2-S45. L2 publishes to L3 the charter's list — the segmentation, the tonality per span, the chord per
span, the assignments per event, and the rivals with their mass (the per-span rivals of L2-S40 and the
rival objects and ranked whole readings of L2-S41, each with its mass; the cut-off the effort setting
sets and the withheld mass per span, L2-S42; the tie flag and the named tie rule of L2-S43; and the
provenance of D-275) — and, where it computes one, an evidence-class fact about the music, with its
establishment status, even where no consumer is named. No term value, term weight, partial candidate
score or other intermediate quantity of L2's own scoring crosses. Every published item carries its
establishment status.**
- *Defense.* The charter's boundary contract: "Nothing L2 did not publish — in particular no
  intermediate quantity of L2's own scoring" [RULED — charter, contract table]. Provenance on every
  record [RULED — D-275]. Establishment status on every evidence-class fact [RULED — D-100; principle
  #19]. A per-note or per-slice weight is a consumer's fitted derivative. This is said at L1 [RULED — IC
  beside S-35, Ruling 47], and by the same reasoning L2's own term weights stay inside L2. (was: "and by the
  same reasoning L2's own weights stay inside L2."; cowork_rulings_2026_10_06_l2_publication_to_next_layer_sitting.md,
  Ruling 1, the recorded "'weight' in L2-S45 is written 'term weight'")
- *Source class.* Given — charter.
- *Status.* Settled.
- *Premise.* L3 needs nothing intermediate.
- *Falsifier.* CODE. **Observable:** L2's output schema. **Decision rule:** falsified if any field carries a
  term value, a term weight or a partial candidate score (was: "a term value, a weight or a partial
  candidate score"; cowork_rulings_2026_10_06_l2_publication_to_next_layer_sitting.md, Ruling 1, the
  recorded "'weight' in L2-S45 is written 'term weight'"; brought into line on the user's word of 2026-10-13
  before Task 0). **Not falsified by:** a mass, which is a published fact.
- *Ruled (cowork_rulings_2026_10_06_l2_publication_to_next_layer_sitting.md, Ruling 1).* Stands as derived.
  "L2-S45 stands as derived in substance. Its "and nothing else" is read, as its own defense, premise and
  falsifier read it, as the ratified boundary contract's bar — "Nothing L2 did not publish — in particular
  no intermediate quantity of L2's own scoring" — and not as a closed list. D-100's rule (evidence-class
  facts published broadly, even with no named consumer, each with its establishment status) applies to L2
  beside that bar. At the application act L2-S45's opening is to be written accordingly; this side's
  wording, not ruled: "L2 publishes to L3 the charter's list — [the list] — and, where it computes one, an
  evidence-class fact about the music, with its establishment status, even where no consumer is named. No
  term value, term weight, partial candidate score or other intermediate quantity of L2's own scoring
  crosses. Every published item carries its establishment status."" "**Recorded with the ruling, not ruled
  (surface §2):** L2-S45's parenthesis is written at the application act to follow the rival-publication
  Ruling 1 and the weight-meaning Ruling 1; L2-S43's tie flag and named tie rule are added to the published
  list; "weight" in L2-S45 is written "term weight"."
- *Amended (cowork_rulings_2026_10_06_l2_publication_to_next_layer_sitting.md, Ruling 1, with the paragraph
  the record marks as recorded with the ruling, not ruled).* "L2-S45 stands as derived in substance. Its
  "and nothing else" is read, as its own defense, premise and falsifier read it, as the ratified boundary
  contract's bar — "Nothing L2 did not publish — in particular no intermediate quantity of L2's own scoring"
  — and not as a closed list. D-100's rule (evidence-class facts published broadly, even with no named
  consumer, each with its establishment status) applies to L2 beside that bar. At the application act
  L2-S45's opening is to be written accordingly; this side's wording, not ruled: "L2 publishes to L3 the
  charter's list — [the list] — and, where it computes one, an evidence-class fact about the music, with its
  establishment status, even where no consumer is named. No term value, term weight, partial candidate score
  or other intermediate quantity of L2's own scoring crosses. Every published item carries its establishment
  status."" *The derived wording stands at the derivation, L2-S45.* (was: "**L2-S45. L2 publishes to L3
  exactly what the charter lists, and nothing else. That is the segmentation, the tonality per span, the
  chord per span, the assignments per event, and the rivals with their mass (with the rival objects and
  thresholds of L2-S40 to L2-S42, and the provenance of D-275). No term value, weight, partial candidate
  score or other intermediate quantity crosses. Every published item carries its establishment status.**";
  cowork_rulings_2026_10_06_l2_publication_to_next_layer_sitting.md, Ruling 1)
- *Beside L2-S45 (cowork_rulings_2026_10_06_l2_publication_to_next_layer_sitting.md, Ruling 1) — carried.*
  "no L2 fact beyond the list is named in these rows, so the wording adds a permission with no present
  content, and telling a later "evidence fact" from an "intermediate quantity" will take judgment."

**L2-S46. L2 works over the record's own positions, in notated order. At each repeat junction L1
publishes, the span following the junction has more than one predecessor, one per pass, and the pair
terms are taken over each. Which order the published ground truth is aligned to, and therefore which
order is graded, is a question for the user (OQ-L2-16 ★).**
- *Defense.* The input contract settled that L1 works in notated order and publishes junction
  adjacencies. It handed "the order the analysis as a whole decides over, and the ground truth's
  alignment" to "L2's surface" [RULED — IC §4, OQ-1, answered for L1 at Ruling 70]. Unfolding is a
  performance reading. L1's refusal to unfold rests on "decides nothing", and L2 can honour both passes
  without choosing one by scoring each junction's predecessors. A published corpus reports that its
  harmony labels "had to be unfolded according to the repeat structures" [RULED — IC S-27, carrying
  Hentschel et al.], so graded ground truth may be in either order. Exemplar 5 notates a repeat
  (`m8 I :|| b4 V`) whose analysis writes one reading across the junction [FACT at the file]. How its
  bar numbers align with the score around that repeat was not established by this session (§6).
- *Source class.* Derived.
- *Status.* Settled. The ground truth's alignment is a fact to be established per corpus at measurement
  design. (was: "Settled for L2's internal order. **Open** for the graded order (OQ-L2-16 ★).";
  cowork_rulings_2026_10_05_l2_working_order_sitting.md, Ruling 1) (the record marks this wording as the
  surface's reading, not ruled separately)
- *Premise.* One reading per span serves both passes. **False-negative path:** a first-ending span whose
  harmony differs by pass. The volta's two endings are different spans, so it is expressible. A span
  *before* the junction whose reading changes because of what follows on the second pass is not.
- *Falsifier.* CODE. **Observable:** pair terms at a junction. **Decision rule:** falsified if the span
  after an end-repeat is scored against one predecessor only. **Not falsified by:** the two
  predecessors' contributions being combined by a declared rule.
- *Ruled (cowork_rulings_2026_10_05_l2_working_order_sitting.md, Ruling 1).* Stands as derived. "For L2's
  specification, L2 decides over notated order: each notated position carries one reading, and at each
  repeat junction L1 publishes, the span on either side has one neighbour per pass, the pair terms taken
  over each and combined by a declared rule."
- *Beside L2-S46 (cowork_rulings_2026_10_05_l2_working_order_sitting.md, Ruling 1) — carried.* "Pass
  attribution is not published: a bar before a junction read two ways is published as two rivals with their
  masses, "either", not "this pass, that pass"."
- *Beside L2-S46 (cowork_rulings_2026_10_05_l2_working_order_sitting.md, Ruling 1) — the condition the
  surface attached, carried.* "If a grading corpus is found whose annotators write different labels on two
  passes of the same notated bars, that is evidence for position two, and the question comes back."
- *Beside L2-S46 (cowork_rulings_2026_10_05_l2_working_order_sitting.md, Ruling 1) — carried, UNSETTLED.*
  "How an unfolded ground truth whose two passes differ on one notated bar is graded against one span
  (measurement design, the same kind as OQ-L2-7); the declared rule combining a junction span's two
  neighbours' contributions (the candidate score's detail); whether a segno or coda sign belongs with the
  junction list (the L0/L1 record's own open reading at OQ-9's answer)."
- *Beside L2-S46's last sentence (cowork_rulings_2026_10_05_l2_working_order_sitting.md, Ruling 1; written at
  the ratification of face (h), cowork_rulings_2026_10_14_l2_face_h_ratification_sitting.md, correction 2).*
  The statement's last sentence states the question as the derivation left it. The working-order record's
  Ruling 1 has since answered OQ-L2-16: L2 decides over notated order, and the ground truth's alignment is not
  a question for the user but a fact to be established per corpus at measurement design. The derived wording
  stands.

**L2-S47. L2 never re-derives an L1 fact. Where it wants something L1 does not publish in usable form,
it writes an open question naming the input-contract statement that would change, and does without in
the meantime. The three wants this derivation found are the successor note in a chordal voice
(OQ-L2-9), the lowest sounding pitch per slice (OQ-L2-11), and an established cue window (OQ-L2-12). A
sounding set extended under a damper-pedal mark (S-54's pedal span; not a pedal point, which L2-S23 and
the elaboration record's Ruling 2 govern) is not a want: the input contract already assigns building it
to the consumer.**
- *Defense.* The charter's layer rule and the fact-publication corollary: "consumers read, never
  re-derive" [RULED — D-100; principle #7]. The brief's instruction [RULED — brief §3.1]. On the pedal:
  "a consumer that wants the pedal-extended sounding set builds it from the slices and the span in one
  step and decides what it means" [RULED — IC beside S-54, Ruling 59]. That is a consumer's act the
  contract sanctions, not a re-derivation.
- *Source class.* Given — charter and brief, for the rule. Derived, for the list.
- *Status.* Settled.
- *Premise.* The list is complete. **False-negative path:** a want this session did not notice. The
  falsifier surfaces it.
- *Falsifier.* CODE. **Observable:** L2's inputs. **Decision rule:** falsified if L2 computes, from L0
  facts, any quantity the input contract defines as an L1 publication (a sounding set, a change point, a
  cue, a relation, a class). **Not falsified by:** L2 reading L0's facts directly for what L1 does not
  define, such as the key signature's value.
- *Amended (cowork_rulings_2026_10_09_l2_never_re_derives_sitting.md, Ruling 1) — the statement's last
  sentence.* "names the damper pedal in full: *"A sounding set extended under a damper-pedal mark (S-54's
  pedal span; not a pedal point, which L2-S23 and the elaboration record's Ruling 2 govern) is not a want:
  the input contract already assigns building it to the consumer."* The derived wording is kept beside it
  (#12)." (was: "A pedal-extended sounding set is not a want: the input contract already assigns building it
  to the consumer."; cowork_rulings_2026_10_09_l2_never_re_derives_sitting.md, Ruling 1)
- *Beside L2-S47 (cowork_rulings_2026_10_09_l2_never_re_derives_sitting.md, Ruling 1) — the three wants, two
  of them answered.* "beside L2-S47's third sentence, a pointer to Ruling 2 of the 2026-10-05
  assignment-evidence record (OQ-L2-9 answered, closed as inactive by design) and Ruling 2 of the 2026-10-08
  structural-bass record (OQ-L2-11 answered, L1's S-50 amended), the derived wording standing. OQ-L2-12
  stays open." OQ-L2-9 is marked ANSWERED in §4
  (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 2), and so is OQ-L2-11
  (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 2).
- *Beside L2-S47 (cowork_rulings_2026_10_09_l2_never_re_derives_sitting.md, §3) — carried, not decided.* "no L2
  statement says whether or how L2 uses the damper-pedal span or the PEDAL-HELD attribute."

**L2-S48. L2's publication covers exactly the working span. The result after any sequence of
enlargements equals a single fresh run over the final loaded span.**
- *Defense.* "The analysis output covers exactly the selection" [RULED — D-260]. "The result after any
  sequence of extensions must equal a single fresh run over the final loaded span" [RULED — D-264]. The
  input contract gives L1's half of the same invariant [RULED — IC beside S-53, Ruling 46 (ii)].
- *Source class.* Given — design intent.
- *Status.* Settled.
- *Premise.* L2's search is deterministic. L2-S43's tie rule makes it so.
- *Falsifier.* CODE. **Observable:** the publication after enlargements against a fresh run. **Decision
  rule:** falsified if they differ in any published field; falsified if two runs over the same selection
  with different enlargement steps publish differently, neither stopped by the safety cap; falsified if the
  publication after an edit differs from a fresh run over the edited record in any published field. (was:
  "falsified if they differ in any published field."; cowork_rulings_2026_10_09_l2_working_span_sitting.md,
  Rulings 2 and 3) **Not falsified by:** differences in internal caches.
- *Beside L2-S48 (cowork_rulings_2026_10_09_l2_working_span_sitting.md, Ruling 2 — "this side's wording, not
  ruled").* "L2 reads no event and no slice outside the music L1 publishes for it — the working span and the
  context L2 has asked for." "The publication does not depend on the size of the steps by which L2 enlarged
  the music it reads (D-261 item 6, D-262)" "**Documentation:** two sentences and one falsifier clause
  beside L2-S48. **Algorithm:** what L2 computes is unchanged now."
- *Beside L2-S48 (cowork_rulings_2026_10_09_l2_working_span_sitting.md, Ruling 2) — carried.* "**Carried,
  stated with the question:** the stopping rule of context-at-the-edge Ruling 2 does not guarantee the
  second sentence by construction (a step that changes nothing while the decisive music lies one step
  further); the owed step-size test (Row 45.72, proposed RELOCATED to the measurement of the analysis) now
  tests L2's own text, and if it fails, strengthening the stopping rule is a later algorithm question for
  the user."
- *Beside L2-S48 (cowork_rulings_2026_10_09_l2_working_span_sitting.md, Ruling 3 — "this side's wording, not
  ruled").* "After an edit, L2 re-decides the changed stretch with a margin around it (C-8; `FRAMEWORK.md`
  §6.7), and its publication equals a single fresh run over the edited record for the same working span.
  Enlargements and edits compose: after any sequence of both, the result equals one fresh run over the music
  L2 ends with." "**Documentation:** one rule and one falsifier clause beside L2-S48. **Algorithm:** what L2
  computes for a given score is unchanged — it is defined as the fresh run; what is added is a constraint on
  how an edit may be handled: no quicker path may publish a different answer."
- *Beside L2-S48 (cowork_rulings_2026_10_09_l2_working_span_sitting.md, Ruling 3) — recorded with the
  ruling, this side's reading, not ruled.* "**Recorded with the question, as this side's reading, not
  ruled:** the margin round an edit cannot then be a fixed width chosen in advance; it reaches as far as the
  edit's effect reaches, found as the context at a selection's edge is (D-261), under the same safety cap
  (D-624); how it is computed is the build's (D-200)."

**L2-S49. L2 consumes nothing L3 publishes: no cadence type, phrase or section grouping, chord symbol,
figured bass or harmonic rhythm. Where a statement above would have wanted one, it reads the L1
evidence it is decided from instead. The dependency is one-way: L3 reads L2.**
- *Defense.* "L3 → L2: Nothing. A read-off fact may not revise the decision it was read off" [RULED —
  charter, contract table]. The places where a want arose are L2-S13 (the phrase-shaped notated
  evidence is read as L1 evidence, not as L3's phrase decision), L2-S34 (cadential confirmation is read
  from the proposed progression, not from L3's cadence type) and L2-S14 (a restatement after a phrase
  end is L3's to divide).
- *Source class.* Given — charter.
- *Status.* Settled.
- *Premise.* L1's evidence plus the progression term carry what L2 needs from phrase and cadence.
  **False-negative path:** a reading that depends on phrase symmetry. One published key-boundary
  study reports an expert placing a modulation to respect "a 2-bar + 2-bar phrase structure" [FACT (relayed,
  08) — Chew, pp. 9–11]. L2 cannot use the phrase reading, and its boundary rival carries the
  expert's placement with its mass.
- *Falsifier.* CODE. **Observable:** L2's inputs. **Decision rule:** falsified if L2 reads any L3
  output. **Not falsified by:** L2 reading L1's notated phrase evidence.
- *Beside L2-S49 (cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md, Ruling 1) — carried, the remedy
  named.* "**Carried, not dropped (#12):** the musical idea — a harmonic sequence found in the chords L2
  itself proposes, read as evidence about key and mode. If the measurement-design stage finds L2's key or
  mode reading falling short on sequential passages (D-494 names its measurement bed, a resolution-denying
  repertoire), a term that rates transposed repetition in the proposed chords is the named remedy to try.
  Such a term reads beyond adjacent pairs, so it belongs to DP-O and is taken up there. Whoever takes up
  DP-O reads the surface's §A.4.1 and this ruling."
- *Beside L2-S49 (cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md, Ruling 2) — stated with the
  ruling, not ruled.* "Stated with the question, so the placement is not read as dropping evidence:
  cadential confirmation enters L2 through the progression term over the chords L2 proposes (L2-S34 Ruling
  2's ground); L1's notated phrase evidence enters as L1's flags (L2-S13); a progression longer than two
  chords is seen link by link, and whether L2 should see it whole is DP-O, open."
- *Beside L2-S49 (cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md, Ruling 3) — the condition.*
  "Claim (ii) of Row 21.46 and claim (ii) of Row 46.42: **HISTORICAL as far as they reach L2.** L2 is
  designed forward-only: nothing from L3 flows back to L2." "**The condition stated with it, in the user's
  words above:** forward-only holds while there is no reason to believe a backward edge would improve the
  inference. As soon as there is reason to suspect it might help, it is tested by measurement. No design
  rule — this placement and the contract table's "L3 → L2: Nothing" included — blocks the ultimate objective
  in the long run." *The user's words, as the record quotes them:* "Are we discussing the actual algorithm -
  or a documentation-technical issue? As long as we have no reason to believe "backward edge" will in any
  way improve our inference (ultimate objective) we will design that way. As soon as we suspect it might
  help with a "backward edge" we should test/measure it. All the above are a direct result of "ultimate
  objective". NO design rule should be able to block that objective in the long run.""
- *Beside L2-S49 (cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md).* The record's note for whoever
  takes up DP-O, which names the sequence term carried under Ruling 1 and harmonic rhythm (Ruling 4) as
  candidates for the same measurement, is quoted beside L2-S31.
- *Ruled (cowork_rulings_2026_10_07_l2_nothing_from_l3_sitting.md, Rulings 1 and 3).* "L2-S49's wording does
  not change."

---

## 4. Open questions

Each names the face it belongs to and the statement that raises it. None is filled with a plausible
reading. The ones marked ★ are those this session would put to the user for a ruling, with the
question it would ask.

*Further open points are carried beside the statements, where the ruling records placed them, and are not
repeated here (#6): marked UNSETTLED beside L2-S6, L2-S17, L2-S19, L2-S24, L2-S38, L2-S44 and L2-S46, and
carried, not decided, beside L2-S47 (the damper pedal). (Recorded at the ratification of the ninth surface,
cowork_rulings_2026_10_14_l2_ninth_surface_ratification_sitting.md, item 2.)*

- **OQ-L2-1 (face (a); L2-S2, S4, S5, S6, S10) — the closure measurement.** Convert every annotated
  span of the grading corpora (both of exemplar 1's traditions, and exemplar 5's with its variants) into
  L2's four fields, and list every annotated reading the admission rule does not reach. This decides
  the vocabulary's completeness (ninth, added-sixth and eleventh classes; double-accidental tonics;
  applied-chain depth; an enharmonic allowance for chord-tone membership). *A measurement, not a
  ruling.* UNESTABLISHED.
  *Kinds added to the closure measurement's list (cowork_rulings_2026_10_05_l2_chord_vocabulary_sitting.md,
  Ruling 2 placements — the surface's proposal, put with the positions, not separately ruled):* the
  minor-major seventh, the dominant seventh with lowered fifth, and the augmented dominant seventh.
  *L2-S10's share stays open (cowork_rulings_2026_10_07_l2_chord_tone_membership_sitting.md, Ruling 1):* the
  record's sentence that L2-S10's share of OQ-L2-1 stays open and commissions nothing, and the named gap it
  records for scores whose spelling was not written by a person, are quoted beside L2-S10.
- **OQ-L2-2 ★ (face (a), (c); L2-S6) — modes.** *Question for the user:* does L2 admit modal readings
  (Dorian, Phrygian, Mixolydian) as tonalities, or read modal passages as major or minor with altered
  degrees, as the grading ground truth does? The literature on chorale melodies is split (L2-S6).
  **ANSWERED (cowork_rulings_2026_10_04_l2_tonality_vocabulary_sitting.md, Ruling 1):**
  "**OQ-L2-2 is answered by this ruling**: L2 does not admit Dorian, Phrygian or Mixolydian as tonalities in
  the first specification; it reads modal passages as major or minor with the inflections counted and
  published; the church modes enter by the named increment under the #17 gate."
- **OQ-L2-3 (face (a), (b), (c), (d), (f); L2-S1, S3, S7, S12, S13, S17, S20, S23, S31, S32, S33, S34, S37,
  S39) — the measured shapes and values.** (was: "**OQ-L2-3 (face (b), (c), (f); L2-S7, S12, S17, S20, S34) —
  the measured shapes and values.**"; recorded at the ratification of the ninth surface,
  cowork_rulings_2026_10_14_l2_ninth_surface_ratification_sitting.md, item 1) The
  maximum span length if any; the metric weights; the key-signature prior's spread and weight; the
  recency form of the tonality degree evidence; the choice between Lerdahl's and Weber's tonal spaces.
  *Measurements, held out.* UNESTABLISHED.
  *Added to the list (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 3):*
  "OQ-L2-3's held-out comparison of tonal spaces names one more candidate beside Lerdahl's and Weber's —
  circle-of-fifths distance together with a relative major/minor term — each entering with fitted weights
  only (L2-S38, L2-S39). Nothing is chosen now."
  *Added to the list (cowork_rulings_2026_10_06_l2_tonality_and_progression_terms_sitting.md, Ruling 4):*
  "the progression term covers the pair across a change of key, each chord read in its own key; a separate
  entry term is one more held-out comparison, added to OQ-L2-3's list."
  *Added to the measurement (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 3):* "**The
  measured finding is carried (#12, #3):** when OQ-L2-3's held-out measurement settles the spelled-degree
  evidence, it reports passages that stay in one key, passages with tonicizations, and passages that change
  key separately; a function-conditioned form of the spelled-degree term stays the named remedy if the
  over-switching shows (D-630, the shape of L2-S34's Ruling 1). The design of that measurement is the
  measurement-design stage's."
  *Added to the list (cowork_rulings_2026_10_06_l2_tonality_evidence_sitting.md, Ruling 4):* "OQ-L2-3's
  held-out comparison of the spelled-degree evidence's forms names one more candidate beside L2-S20's
  recency-weighted account — the per-stretch spelled-degree emission given the stretch's key (Temperley's
  tonal-pitch-class form, the joint estimator's ratified term). Each enters with fitted weights only.
  Nothing is chosen now."
  *Added to the list (cowork_rulings_2026_10_07_l2_any_boundary_set_sitting.md, Ruling 2):* "**OQ-L2-3's
  list of held-out measurements gains one item**, for the application act to write: *"the form of a chord's
  own length in the candidate score: none beyond the boundary terms (the implicit form), or an explicit
  span-length term, and over what unit (change points, beats, or time), compared by held-out measurement."*"
  "**L2's algorithm as its statements define it is unchanged now; L2-S7's and L2-S31's wordings are
  unchanged.** If the measurement ever repays an explicit length term, adding it to the candidate score is a
  separate ruling then (Ruling 6 of the L2-S10 record of 2026-10-07: investigated and measured, never
  asserted)." *Cost accepted:* "one more held-out comparison, and one more fitted weight if the term is ever
  adopted (#20's capacity budget)."
  *Added to the list (cowork_rulings_2026_10_07_l2_notated_boundary_evidence_sitting.md, Ruling 2):*
  "**OQ-L2-3's list of held-out measurements gains one item**, for the application act to write: *"whether a
  notated boundary flag, with its scope, at a boundary is a term on the elaborations that cross that
  boundary (in the pair term of L2-S33), compared by held-out measurement against the same readings without
  it."*" "**L2's algorithm as its statements define it is unchanged now; L2-S13's, L2-S31's and L2-S33's
  wordings are unchanged.** If the measurement ever repays the term, adding it is a separate ruling then."
  *Added to the list (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 3):* "**Documentation:
  OQ-L2-3's list of held-out measurements gains one item**, for the application act to write: *"whether the
  candidate score carries a term on which chord, with which figure, a bass scale degree usually carries (the
  bass-scale-degree prior of D-585, after the Rule of the Octave) — as a counted table or as the published
  rule entering under L2-S39 with one fitted weight, with or without the direction of the bass's approach —
  compared by held-out measurement against the score without it."*" "No term is added; no L2 statement is
  reworded. If the measurement ever repays the term, adding it is its own ruling then (Ruling 6 of the
  L2-S10 record). **Recorded with the ruling:** the old rule's "tie-breaker only" does not survive as a rule
  — every weight is fitted (L2-S38); "never a gate" survives under L2-S3." *Bound carried:* "no source for
  the Rule of the Octave is held (`docs/research_papers/BIBLIOGRAPHY.md`); a published form entering under
  L2-S39 needs one fetched and read first (the theory-grounding corollary) — for the research iteration
  ruled on 2026-10-07." *Cost accepted:* "one more arm in a measurement already owed."
  *Added to the list (cowork_rulings_2026_10_09_l2_span_content_term_sitting.md, Ruling 2):* "**The
  proposal:** OQ-L2-3's held-out comparisons gain one arm — the content term with an elaboration's
  contribution split by whether its spelled pitch lies in the span's spelled tonality's collection, against
  the same term without the split; fitted weights only; nothing chosen now." "**Algorithm: unchanged now.**
  It changes only if the measurement shows the split earning its place beyond its uncertainty (#24). Until
  then L2-S32 stands as worded, with no split by collection." *Cost accepted:* "one more arm in a
  measurement already owed."
  *Added to the list (cowork_rulings_2026_10_09_l2_crossing_elaborations_sitting.md, Ruling 2):*
  "**OQ-L2-3's list of held-out measurements gains one item**, for the application act to write: *"the
  elaboration term with each elaboration's relation named inside the candidate score, against the same term
  rating chord tone against elaboration only, with the relation then derived from the decided reading by the
  standard definitions; graded through the chords and boundaries (OQ-L2-13); fitted weights only; the named
  form kept only if it beats the other beyond the comparison's uncertainty."*" "**Algorithm: unchanged
  now.** L2-S1, L2-S23 and L2-S33 keep their wording (the relation inside the one decision). **Afterwards
  the measurement decides, the burden on the richer form:** if the named form does not beat the other beyond
  its uncertainty (#24), L2 takes the name-afterwards form (D-630); if it does, the named form is confirmed.
  The measurement precedes any build."
  *Added to the list (cowork_rulings_2026_10_09_l2_cadence_cues_sitting.md, Ruling 2):* "**OQ-L2-3's list of
  held-out measurements gains one item**, for the application act to write: *"the candidate score with a cue
  term — L1's cadence cues read against each reading's own tonality at each onset change point, with fitted
  weights, and the fermata's written position and metric class as covariates of where the arrival sits —
  against the same score without it; the leading-tone cue now, the falling-fifth and fourth-and-seventh cues
  only once OQ-L2-12 has established the window; graded on the tonalities, chords and boundaries; fitted
  weights only; the cue term kept only if it beats the score without it beyond the comparison's
  uncertainty."*" "**Algorithm: unchanged now.** L2-S37 keeps its wording; no term of the candidate score
  reads a cue (the surface's reading of the derivation as written). **Afterwards the measurement decides,
  the burden on the richer form:** if the cue term does not beat the score without it beyond its uncertainty
  (#24), L2 stays without it (D-630); if it does, L2-S37 gains the term. The measurement precedes any
  build."
  *Added to the list (cowork_rulings_2026_10_09_l2_published_theory_terms_sitting.md, Ruling 2):* "the
  held-out comparison of tonal spaces for L2-S34 (i)'s cost gains one more candidate — a counted,
  transposition-invariant table over the circle-of-fifths distance between the tonics and the pair of modes,
  with the relative and the parallel relations as their own entries and asymmetries allowed, counted once
  from annotated music and frozen, with one fitted weight (L2-S38 as amended by the fit record's Ruling 1);
  graded like the other candidates; nothing chosen now." "**Algorithm: unchanged now.** L2-S34 (i) and
  L2-S39 keep their wording. If the counted table ever beats the published distances beyond the comparison's
  uncertainty (#24), L2-S34 (i)'s words "in a published tonal space" are amended by their own ruling then;
  an asserted benefit overrides nothing (L2-S10 record, Ruling 6)."
- **OQ-L2-4 ★ (face (a), (d); L2-S8) — the elaboration relations.** *Question for the user:* is the
  charter's list (passing, neighbour, suspension, anticipation) exhaustive? Or are appoggiatura, escape
  tone, pedal point, retardation, and an "unclassified elaboration" admitted as well?
  **ANSWERED (cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling 1):**
  "**OQ-L2-4 is answered by this ruling**: the charter's four are not exhaustive for L2's specification; the
  four named additions are admitted; retardation is not a separate name."
- **OQ-L2-5 ★ (face (c); L2-S19) — pivot chords.** *Question for the user:* may L2 publish a span as a
  pivot carrying two tonalities in its principal reading, or is the charter's "the tonality" per span
  singular, so that a pivot is expressed only as two rivals?
  **ANSWERED (cowork_rulings_2026_10_05_l2_pivot_chord_sitting.md, Ruling 1):**
  "OQ-L2-5 is answered: the charter's "the tonality" per span is singular, and a pivot is expressed as
  rivals."
- **OQ-L2-6 (face (c), (h); L2-S22) — convergence of masses.** When L2 enlarges its context, what counts
  as its in-span publication "no longer changing": the principal reading only, the rival set, or the
  masses within a bound? D-261 says "in-selection output", and the masses are real numbers.
  **ANSWERED (cowork_rulings_2026_10_07_l2_context_at_the_edge_sitting.md, Ruling 2):**
  "Position 2. … **OQ-L2-6 is closed** by it. The tolerance values and the defaults of each setting are not
  ruled here: they are decided at the effort setting's build (D-202 stays DEFERRED), as the
  rival-publication cut-off depths are." The ruled wording stands in L2-S22's amended last sentence.
- **OQ-L2-7 (face (b); L2-S1, S14) — annotation boundaries inside one harmony.** Exemplar 3's tradition
  writes a new label where a suspension resolves (`V7(4)/iv` then `V7/iv`). Exemplar 1's writes
  `V2(4) … V43`. L2 publishes one span with a suspension assignment. *For the measurement-design stage:*
  how boundary grading maps an annotation's retardation labels onto L2's span-plus-assignment. Also,
  how a restatement after a phrase end (`|| b4 I`) is graded.
- **OQ-L2-8 ★ (face (f), (g); L2-S23, S36) — tractability.** *First a measurement:* does exact (or
  bound-safe) inference over the joint state fit on the scores the project must handle? Those include
  very large scores [RULED — D-201]. *Then, if not, a question for the user:* narrow the admission rule
  (with L2-S2's ceiling cost), or relax the charter's no-discarding rule, and by how much?
  *Stays open (cowork_rulings_2026_10_05_l2_tractability_sitting.md, Ruling 1 (i)). The route, recorded at
  the record's §1b as the record's own answer and NOT as a ruling:* "1. **The next act is a paper sizing** —
  no code, no implementation read — by a fresh Cowork session, landed as a document: a number for each of
  the six cost drivers, over the music loaded for a selection (selection plus context, Ruling 1 (ii)), at
  chorale size and at D-201's sizes; every assumed value marked provisional, the result with its
  uncertainty. 2. **Afterwards:** if exact search is clearly affordable, OQ-L2-8 is recorded "expected
  affordable; to be confirmed by measurement at the build"; otherwise **which dials D-202's ambition setting
  gets, and their defaults**, come to the user with the sizes, before this layer's specification is
  ratified; if the sizing cannot tell, whether a code trial may run inside this phase comes to the user on
  its own surface. 3. Speed-ups that leave the result unchanged come first, the dials last (D-200). A dial
  the user rules and the end user turns is not the "quiet" reduction Ruling 1 (iv) bars."
  *Since then (ratification_surfaces/cowork_l2_search_sizing_2026_10_05.md, §8 and §C, recorded there as
  following from the record and the user's word, not as a ruling):* the sizing could not tell; no code trial or
  timing measurement is owed before ratification; the specification names the entry points for the effort
  setting (beside L2-S36); which dials exist and their defaults are decided when the effort setting is built
  (D-202 DEFERRED). OQ-L2-8 stays open until then. *(Recorded at the ratification of the ninth surface,
  cowork_rulings_2026_10_14_l2_ninth_surface_ratification_sitting.md, item 3.)*
- **OQ-L2-9 (face (d); L2-S24) — successor note in a chordal voice.** L1 publishes, per notated voice,
  the relation to the preceding note and a chordal count. In a voice that sounds several pitches, no
  note-to-note successor is published. *The input-contract statements concerned:* S-50's list, with
  Rulings 49 and 61. Would L1 publish per-note predecessor and successor links within a chordal voice,
  or is the elaboration term inactive there by design?
  **ANSWERED (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 2):**
  "**OQ-L2-9 is answered:** L1 publishes no note-to-note link inside a voice that sounds several pitches,
  because pairing chord members into lines is the voice separation S-13 (as Ruling 61 left it) and D-389 say
  the analysis never infers; the elaboration term is inactive there, the loss declared at L2-S24's premise."
- **OQ-L2-10 (face (d); L2-S26) — relations for grace notes.** Does L2 publish an elaboration relation
  for a grace attachment (such as "appoggiatura to host"), given D-295's "every inferred object must be
  displayable"?
  **ANSWERED (cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md, Ruling 3):**
  "OQ-L2-10 is answered no."
  The condition the user attached, in his words as the record's §0 quotes them: "confirmed (I take for
  granted that "not publishing" in this and previous rulings do not break the rule "no information loss /
  always publish everything known, inferred ...." - and it is up to the consuming layer to choose what to
  use and not)." — checked at the record's §1c.
- **OQ-L2-11 (face (e); L2-S28) — lowest sounding pitch per slice.** L1 publishes the lowest sounding
  pitch as a cue anchor at onset change points and in cue witnesses (IC S-44, S-49), not for every
  slice. The figure term wants it for every slice. *The input-contract statements concerned:* S-44 and
  S-50. Would S-50's list gain the lowest sounding pitch per slice?
  **ANSWERED (cowork_rulings_2026_10_08_l2_structural_bass_sitting.md, Ruling 2):**
  The ruling's words are quoted beside L2-S28. *Declined:* "B (L2 computes the pitch itself — one named fact
  with two producers, #6, D-100, the derivation's own "L2 writes the want instead"); C (the term narrowed to
  where L1 publishes it — evidence lost at slices that begin at a release, nothing gained)."
- **OQ-L2-12 (face (f); L2-S37) — the cue window.** The measurement IC S-48 names ("owed to L2's
  calibration"): the distribution of the distance from the last sounding of the fourth and seventh
  degrees to the annotated arrival, and S-45's recall as a function of look-back. Until it runs, two of
  the three cues cannot carry load in L2. UNESTABLISHED.
  *Pointer:* the cue-term measurement under OQ-L2-3 (cowork_rulings_2026_10_09_l2_cadence_cues_sitting.md,
  Ruling 2) waits on this window for the falling-fifth and the fourth-and-seventh cues. *(Recorded at the
  ratification of the ninth surface, cowork_rulings_2026_10_14_l2_ninth_surface_ratification_sitting.md, item
  4.)*
- **OQ-L2-13 (face (d), (f); L2-S38) — ground truth for assignments.** No annotated corpus this
  session knows of carries per-note chord-tone and elaboration labels made independently of the chord
  labels. Fitting and grading the assignment half of the decision needs one, or a ruling that the
  assignments are graded only through the chord.
  *Interim ruled (cowork_rulings_2026_10_05_l2_fit_sitting.md, Ruling 3); the question stays open:* "Until
  an analysed collection marking chord tones and elaborations note by note, independently of the chord
  labels, is found or commissioned, the chord-tone assignments and elaboration relations are **learned and
  graded only through the chord labels** — the interim the third family's ruling already carries as an
  accepted cost ("until one is found or the user rules otherwise they are fitted and graded only through the
  chord", `cowork_rulings_2026_10_05_l2_assignment_evidence_sitting.md`) and the second family records for
  the elaboration names. It stands for the fit ruled in Ruling 1: any counted table touching chord tones and
  elaborations is counted from roles derived from the chord labels. **OQ-L2-13 stays open as a search for
  the measurement-design stage**, not as a choice now." *What the record leaves open:* "Whether a
  later-found collection would change the fit or only the grading"
- **OQ-L2-14 (face (g); L2-S40) — naming mass against D-267.** Is the un-calibrated whole-reading
  distribution declared as Class M (with its squash to 0..1 being the normalisation itself), or does
  D-267 need a third named class? The session holds that it behaves as a margin for comparison purposes
  and does not decide the naming.
  **ANSWERED (cowork_rulings_2026_10_05_l2_weight_meaning_sitting.md, Ruling 1):**
  "A span-rival's weight (the derivation's *mass*, L2-S40) is declared to be neither a decision margin
  (Class M) nor a calibrated probability (Class P), but a **third kind: the model's own distribution** —
  each value a share in [0,1], the shares of one stretch's rivals summing to at most one, not calibrated,
  compared only within one working span's publication, never read as a frequency of being right, and turned
  into a calibrated probability only through a fitted reliability map."
- **OQ-L2-15 (face (g); L2-S41, S42) — how much is published.** The number of whole readings, and how deep
  below the top setting the cut-off lies under which a span-rival is withheld (nothing is withheld at the top
  setting); both decided at the effort setting's build. *Measured* against what the consumers (L3, the
  display) actually read. UNESTABLISHED. (was: "The number of whole readings, and the mass threshold below
  which a span-rival is withheld. *Measured* against what the consumers (L3, the display) actually read.
  UNESTABLISHED."; cowork_rulings_2026_10_05_l2_rival_publication_sitting.md, Ruling 1; brought into line at
  the ratification of the ninth surface, cowork_rulings_2026_10_14_l2_ninth_surface_ratification_sitting.md,
  item 5)
- **OQ-L2-16 ★ (face (h); L2-S46) — the graded order.** *Question for the user:* is the ground truth
  this project grades against aligned to notated order or to unfolded order? Is the working span a
  stretch of notated bars, or of the performed sequence? (This is the remainder of the input
  contract's OQ-1.)
  **ANSWERED (cowork_rulings_2026_10_05_l2_working_order_sitting.md, Ruling 1):**
  - "**L2's working order:** notated order, one reading per notated position (this ruling)."
  - "**The working span:** given in the record's own positions (Ruling 46 clause (i), ruled 2026-09-02).
    That this answers the question's "notated bars, or the performed sequence?" with "notated positions" is
    the surface's reading (its §3 and §B correction 3), put to the user with the surface and not separately
    ruled."
  - "**The ground truth's alignment:** not ruled. It is a fact about each corpus (Ruling 70's own words, "a
    fact about the corpora not established by anything read (#19)"), to be established per corpus where the
    grading is designed."
- **OQ-L2-17 (face (a)–(e), a case the staged set does not supply).** An enharmonic modulation, such
  as a German sixth reinterpreted as a dominant seventh. Spelled tonalities (L2-S1, S6) make the pivot a
  respelling. None of the exemplars read carries one, so how a reading crosses it is not derived here.
- **OQ-L2-18 (face (e), a case the staged set does not supply).** A chord over a pedal point, where the
  pedal is not a chord member for several spans. It is admitted as a relation only if OQ-L2-4 admits
  "pedal point". The staged exemplars read here carry no clear instance (exemplar 6's music was not
  read, §6).
  *Condition met (cowork_rulings_2026_10_05_l2_elaboration_relations_sitting.md, Ruling 1):* "**OQ-L2-18's
  condition** ("only if OQ-L2-4 admits 'pedal point'") **is met**; its case still has no example, and
  OQ-L2-18 otherwise stays as the derivation leaves it."

**Questions the session would put to the user, counted from the ★ marks above: 5 of 18**
(OQ-L2-2, 4, 5, 8, 16). DP-N and DP-Q, which L2-S29 and L2-S44 carry, are the charter's own open
questions and are not counted here.

*Since the derivation (recorded at the ratification of the ninth surface,
cowork_rulings_2026_10_14_l2_ninth_surface_ratification_sitting.md, item 6):* OQ-L2-2, 4, 5 and 16 are
ANSWERED (their marks above), and OQ-L2-8's question goes to the effort setting's build (the line beneath
OQ-L2-8, resting on the sizing's §C, recorded there and not ruled). None of the five remains to be put before
ratification.

---

## 5. The blind act's own record — where it stands

*The measured-cost record, the independence record and the note on the brief's decomposition are the
blind act's own and stand at the derivation, `cowork_blind_derivation_l2_2026_09_27.md` §5–§7, at blob
`d78ac530992860d38d1f605a77a2961d5440a2f6`; they are not restated here (#6).*

A reference in this file to §6 or §7 with no other document named means that section of the derivation.
*(Recorded at the ratification of the ninth surface, cowork_rulings_2026_10_14_l2_ninth_surface_ratification_sitting.md,
item 11.)*

*End of file.*
