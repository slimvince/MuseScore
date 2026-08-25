# Blind derivation — how a harmonic analysis should score a candidate chord reading against the evidence

> **STATUS: DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED.**
>
> Written 2026-08-24 by an implementation-blind deriving session under
> `cowork_blind_session_brief_scoring_model.md`. It states what the analysis **should** do for the
> subject of §2 of that brief, derived from music theory, from published research fetched and read,
> and from the ruled design intent carried in the session's boot pack. **It describes nothing that
> any code or specification of this project currently does, and it compares itself against nothing.**
> It authorizes no fix, no build, no specification edit and no measurement.
>
> The independence record is §5 and it carries a stop-on-meeting event and a second, larger
> contamination the session did not choose. **Read §5 before relying on any statement here.**

---

## 0. Terms used in this document

A reader who knows music theory and does not know this project should be able to read every
statement below. Standard music-theory words are used in their standard sense. The project's
reserved-word convention binds this document: the bare word *score* is the music, the bare word
*key* is a tonality, the bare word *measure* is the bar. Where a non-musical sense is meant it is
qualified — *candidate score*, *measurement*, *level of detail*.

- **The analysis** — the harmonic-analysis software this project builds. Given a notated score it
  decides the tonality, the chords, and where one chord gives way to the next.
- **Tonality** — what is commonly called "the key": a tonic together with a mode.
- **A tone event** — one notated note, with a pitch, a notated spelling, an onset, a duration and a
  voice. Distinct from the *pitch class* it sounds.
- **The sounding set at an instant** — the set of tone events whose sounding span contains that
  instant.
- **An atomic stretch** — the span between two consecutive instants at which the sounding set
  changes, by an onset or an offset. Nothing shorter is distinguishable from the notation alone.
- **A candidate stretch** — a run of one or more consecutive atomic stretches, considered as the
  span of one chord.
- **A candidate reading** — the object whose fit is judged. §1 statement S1 says what it consists of.
- **A role assignment** — for each tone event sounding inside a candidate stretch, whether that
  event is being read as a member of the candidate chord or as an ornament (a passing tone,
  neighbour tone, suspension, anticipation, appoggiatura, pedal tone or escape tone).
- **A factor** — one multiplicative term of a probability of the observed music given a candidate
  reading.
- **A candidate score** — the single comparable quantity a candidate reading is reduced to, so that
  two candidate readings can be ranked.
- **The exemplars** — the three annotated chorales the brief staged to this session by name. They
  are published human readings, not a specification, and this session ran no measurement over them.
  They are named in §5.

---

## 1. The statements

Each statement carries six fields. Field 6 is written in terms of an **observable** and a
**decision rule over it**; naming code sites is left to a later session, as the brief directs.

Source classes: **derived** (from theory or fetched research), **salvaged** (taken from a ruled
design-intent entry in the boot pack, cited by identifier), **measured** (resting on a measurement
this session cannot make — written with the measurement it would need, status UNESTABLISHED, no
value).

### 1.1 What is being scored

---

**S1 — The object whose fit is judged is a labelled stretch that includes a role for every tone
event sounding inside it.**

1. **Statement.** A candidate reading consists of: a start instant and an end instant; a tonality; a
   chord identity (a scale degree relative to that tonality, a quality, and an inversion); and, for
   every tone event sounding anywhere inside that span, an assignment of that event to a role —
   chord member (naming which chord factor it realizes) or ornament (naming which ornament class).
   The role assignment is **part of the scored object**, not a filter applied before scoring and not
   a label derived after it.
2. **Defense.** THEORY (common-practice harmony): two readings of one passage can agree on every
   sounding pitch and disagree only about which tone is ornamental, and they then name different
   chords. FACT (exemplar, `Chorales/003/analysis.txt`, bar 4, annotator Andrew Jones, proofread by
   Dmitri Tymoczko and Hamish Robb): the annotator writes, in the corpus file itself, *"If G# is an
   incomplete neighbor, it is i6/4, otherwise III+6 with A as a regular neighbor."* The file then
   records **both** readings, `m4 i6/4 …` and `m4var1 III+6 …`. FACT (desk trace at the notes of
   `003 Ach Gott, vom Himmel sieh darein.mscx`, bar 4, first beat): the four sounding events are
   C5, E4, G♯3, E3 — the tenor G♯ an eighth on the beat, moving to A for a quarter across the
   half-beat, then back to G♯. Under one role assignment G♯ is the ornament and the chord is A minor
   in second inversion; under the other A is the ornament and the chord is an augmented triad on C
   with E in the bass. **The pitch content over the candidate stretch is identical in both
   readings.** A model whose scored object is the stretch's pitch content alone therefore cannot
   assign these two readings different candidate scores, whatever its terms are.
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: cases of this shape are not confined to one
   bar of one chorale — the ornament-versus-chord-member question is the general reason two
   competent analysts disagree about a chord label. **False-negative path:** if such cases were
   in fact rare and always resolved by some other term, a model without role assignment would
   still rank correctly on almost all stretches, and its failure would show only as a small,
   diffuse loss that no per-case inspection would attribute to this cause. The path is closed by
   measuring the share of stretches on which two admissible role assignments over the same pitch
   content name different chords — a measurement this session may not run.
6. **What would falsify it.** **Observable:** the candidate scores the model assigns to two readings
   constructed to share a candidate stretch and its complete pitch content while differing only in
   which tone event is assigned an ornament role. **Decision rule:** if the model's construction
   makes those two candidate scores necessarily equal — because the scored object does not carry
   roles — S1's requirement is unmet. **Not falsified by:** the two readings receiving equal scores
   in some particular passage where the evidence genuinely balances; S1 asks that the model be
   *able* to separate them, not that it always does.

---

**S2 — The finest span the scoring model may reason over is the atomic stretch, and every candidate
stretch is a whole number of consecutive atomic stretches.**

1. **Statement.** Boundaries between chords are admitted only at instants where the sounding set
   changes. A candidate stretch begins at such an instant, ends at such an instant, and contains no
   partial atomic stretch.
2. **Defense.** THEORY: between two consecutive changes of the sounding set, nothing in the notation
   distinguishes one instant from another, so no evidence exists that could place a boundary inside
   such a span. FACT (Pardo & Birmingham 2002, fetched and read, two independent extraction passes
   in agreement): *"A partition point occurs where the set of pitches currently sounding in the
   music changes by the onset or offset of one or more notes"*; *"A minimal segment is the interval
   between two sequential partition points."* SALVAGED (boot pack **D-023**): the atomic analysis
   unit is the constant-sonority slice, never the metric beat. SALVAGED (**D-022**): analyse at the
   finest grain where harmony is well defined and derive everything coarser.
3. **Source class.** derived, corroborated by salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the notation is the whole of the evidence, so
   two instants indistinguishable in the notation are indistinguishable to the model. **False-negative
   path:** a boundary genuinely falling mid-span would exist if some evidence outside the sounding
   set placed it — a written rest that does not change the sounding set, a bar line, a fermata, a
   phrase mark, a figured-bass digit. Each of those is itself a notated event and can be admitted as
   an additional partition point; the premise is therefore that *the partition-point set is derived
   from the notation*, not that it is derived from pitch onsets alone. Stated so that a later design
   widens the partition set rather than breaking the rule.
6. **What would falsify it.** **Observable:** the start and end instants of every candidate stretch
   the model considers. **Decision rule:** if any is an instant at which no notated event begins or
   ends, S2 is violated. **Not falsified by:** a candidate stretch that is longer than one atomic
   stretch, which is the ordinary case; nor by the model *reporting* a chord as sounding at an
   arbitrary instant inside a stretch, which is a read-out, not a boundary.

---

**S3 — The extent of the stretch is part of the candidate, decided by the same comparison that
decides the chord — not fixed before scoring begins.**

1. **Statement.** The model does not receive a segmentation and then label it. A candidate is a
   (stretch, tonality, chord, role assignment) whole, and the winning segmentation is whichever one
   the winning set of candidates induces.
2. **Defense.** THEORY: the extent of a chord and its identity are mutually determining — one cannot
   ask "which chord is this" without having fixed "this", and one cannot fix "this" without a view
   of which chord it would be. FACT (Masada & Bunescu 2018, *Chord Recognition in Symbolic Music: A
   Segmental CRF Model*, fetched and read, two independent extraction passes in agreement): the
   model scores a segmentation **s** and a labelling **y** jointly,
   `P(s, y | x, w, u) = exp(wᵀF(s,y,x) + uᵀG(s,y,x)) / Z(x)`, with the partition function summed
   over *all labelled segmentations*, and inference performed by *"a semi-Markov analogue of the
   usual Viterbi algorithm"*. FACT (same paper): segment-level features *"capture the extent to
   which the events in an entire segment of music are compatible with a candidate chord label"* and
   cannot be expressed by a model that labels events rather than segments. FACT (Pardo & Birmingham
   2002, same paper as S2): labelling accuracy with the correct segmentation supplied is reported at
   **88.66 %** mean, and drops to **76.50 %** when the same system must also find the segmentation —
   so segmentation is not a solved preliminary, it is most of the remaining error. SALVAGED
   (**D-001**): tonality, mode and chord are inferred by one decode with segmentation as a modelled
   variable.
3. **Source class.** derived, corroborated by salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: a separately-decided segmentation would have
   to be decided on evidence that does not depend on the chord identity, and no such sufficient
   evidence exists. **False-negative path:** if surface cues alone (metric accent, bass change, rests,
   bar lines) placed boundaries accurately enough, a two-stage design would lose nothing measurable,
   and the loss from separating the stages would be invisible except as a diffuse accuracy
   difference. Closing it requires measuring boundary placement from surface cues alone against
   annotated boundaries — not run here.
6. **What would falsify it.** **Observable:** whether any candidate stretch the model finally commits
   to could not have been reached because a boundary was fixed before chord identity was considered.
   **Decision rule:** construct a passage where the correct boundary is placeable only with knowledge
   of the chord; if the model cannot produce that boundary at any setting, the segmentation is not
   inside the comparison. **Not falsified by:** the model using surface cues as *evidence* about
   boundaries — that is a term (S11), not a pre-decision.

---

**S4 — Where two competent published readings of one passage differ, they differ about the extent of
the stretch at least as often as about the chord, so the model's candidate space must contain both
granularities.**

1. **Statement.** The candidate space must admit, over the same music, both a coarse reading in which
   one chord spans a beat and a fine reading in which that beat carries two chords. The model may
   prefer one; it may not be unable to represent the other.
2. **Defense.** FACT (exemplars, two independent published readings of one chorale — `Chorales/001/analysis.txt`,
   analyst Andrew Jones, and `Chorales/001/analysis_BCMH.txt`, the Bach Chorales Melody-Harmony
   Corpus): at bar 3 one reading gives `IV b2.5 viio6 b3 I` where the other gives
   `IV b2 IV2 b2.5 viio6 b3 I` — an extra chord inside the same beat. At bar 8 one gives
   `I b2 ii b2.5 viio6 b3 I6` where the other gives `I b2 viio6 b3 I6` — one reading has a chord the
   other does not. At bars 6, 16 and 20 one gives `V b3.5 V7` where the other gives a single `V7` —
   the same harmony, divided or not divided at the arrival of the seventh. FACT (same pair, chord
   identity): where both name a chord at the same instant, the names agree in the large majority of
   places. **This session did not count these and reports no rate:** three chorales are exemplars,
   not a corpus, and a count over them would not be a measured fact about this project's data.
3. **Source class.** derived from the exemplars as illustration; the *rate* claim is **measured** and
   its value is **UNESTABLISHED**. The measurement it would need: over a corpus carrying two
   independent readings of the same music, the share of disagreements attributable to boundary
   placement versus to chord naming, per axis.
4. **Status.** open — as to the rate. Settled as to the requirement that both granularities be
   representable, which does not depend on the rate.
5. **Premise, and its false-negative path.** Premise: a disagreement between two competent analysts
   marks a place where the music genuinely admits two readings, rather than a place where one analyst
   erred. **False-negative path:** if one of the two annotation traditions is systematically coarser
   by editorial convention rather than by musical judgment, the disagreements would measure the
   conventions and not the music. That is not excluded here and is one reason the rate is left
   unestablished. The exemplars carry a visible instance of convention difference: one tradition
   writes `Cad64` where the other writes `i6/4` for the same sonority (`Chorales/003/*`, bar 4).
6. **What would falsify it.** **Observable:** the set of candidate stretches the model will consider
   over a given passage. **Decision rule:** if for some beat the model's candidate space contains
   only one-chord-per-beat readings, or only sub-beat readings, S4 is violated. **Not falsified by:**
   the model *ranking* the coarse reading above the fine one everywhere in some repertoire.

---

### 1.2 The terms

---

**S5 — Chord-predicted tones that are present are counted per chord factor — root, third, fifth,
seventh, added tone — and never as one aggregate count.**

1. **Statement.** The presence of the root, of the third, of the fifth and of each further chord
   factor are separate terms, each free to carry its own strength. "How many of the chord's tones are
   present" is not admissible as the term.
2. **Defense.** THEORY (common-practice harmony): the factors are not interchangeable evidence. The
   third determines the quality; the root and third together nearly determine the chord's identity;
   the fifth is the tone most freely omitted in four-part writing and its absence is close to
   uninformative; a seventh present is strong positive evidence for a seventh chord, and its absence
   is strong evidence against one. An aggregate count asserts that these are exchangeable, which is
   a claim music theory contradicts. FACT (Masada & Bunescu 2018, chord-coverage features f₄–f₉ and
   f₁₁–f₁₈, fetched and read, cross-checked): the published model uses *"indicator and real-valued
   features testing whether the segment contains the root, third, fifth, seventh, or added tones"* —
   one feature per chord factor, not one count. CONTRAST, recorded because an excluded alternative
   is evidence about the choice: Pardo & Birmingham 2002 use `M` = *"plain count (not weighted) of
   template elements not found in the segment"*, an aggregate, and their own tie-break machinery then
   has to repair the losses that aggregate causes — the first tie-break rule they state is a
   root-weight rule, which is precisely a per-factor distinction reintroduced after the fact.
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the per-factor strengths genuinely differ in
   the repertoire, so the extra parameters buy accuracy rather than variance. **False-negative path:**
   if the fitted per-factor strengths came out indistinguishable from one another, the aggregate
   would be the better model on capacity grounds and the separation would be over-parameterization.
   The path is closed by fitting them separately and reporting the spread with its uncertainty (#24);
   until that is done, the separation rests on theory alone and its cost in capacity is real (S23).
6. **What would falsify it.** **Observable:** the model's parameter set. **Decision rule:** if there
   is one strength governing chord-tone presence rather than one per chord factor, S5 is violated.
   **Not falsified by:** several factors *sharing* a fitted strength because the fit was pooled under
   a declared capacity budget — that is a declared pooling decision, and it is recorded as one.

---

**S6 — A chord-predicted tone that never sounds anywhere in the stretch is a distinct term from a
tone that sounds only briefly, and the absence term is per chord factor.**

1. **Statement.** Absence is not the zero of the presence term. A stretch in which the third never
   sounds and a stretch in which the third sounds for a sixteenth are different evidence, and the
   model states which term separates them.
2. **Defense.** THEORY: the omission of a chord factor is a compositional choice with its own
   conventions — the fifth is routinely omitted, the third almost never in a triad meant to carry a
   quality, the root frequently in a seventh chord over a moving bass — while a factor sounding
   briefly is a different phenomenon, usually an arrival or a departure at a boundary. Folding the
   two into one continuous quantity asserts that a very short presence is nearly an absence, which
   the conventions above do not support. FACT (Masada & Bunescu 2018, cross-checked): the published
   model carries **both** kinds — indicator coverage features (present at all or not) **and**
   duration-weighted coverage features measuring *"proportion of the segment time that is covered by
   a particular chord note"* — as separate features rather than one.
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the indicator and the duration-weighted
   quantity are not redundant. **False-negative path:** they are strongly correlated by construction
   — a factor present at all is usually present for a while — so a fit could assign nearly all the
   weight to one and leave the other inert, which would look like a working model carrying a dead
   term. A dead term is the shape the boot pack's defect catalog names **DT-7** (never-fires /
   always-fires mechanism), and detecting it requires reporting each term's realized range over the
   corpus, not merely its fitted strength.
6. **What would falsify it.** **Observable:** the model's candidate scores for two otherwise
   identical readings, one in which a chord factor is absent throughout the stretch and one in which
   it sounds for the shortest available duration. **Decision rule:** if the two scores differ only by
   the amount the duration-weighted term alone would give, with no separate contribution for absence,
   S6 is unmet. **Not falsified by:** the two terms being fitted to similar values.

---

**S7 — A sounding tone the chord does not predict counts against the reading only if that reading
assigns it no ornament role; a tone assigned an ornament role is evidence about the ornament model,
not negative evidence about the chord.**

1. **Statement.** Negative evidence is not "every sounding pitch outside the chord". It is "every
   sounding pitch outside the chord that this reading cannot explain". A reading that explains a
   dissonance as a suspension pays the price the ornament model charges for a suspension in that
   metric position and that voice — not a flat penalty for a foreign tone.
2. **Defense.** THEORY: the entire common-practice theory of non-chord tones exists because foreign
   tones are normal and rule-governed, not anomalous. A flat penalty for any foreign tone makes
   every suspension, passing tone and appoggiatura evidence against the chord that the theory says
   they decorate — so the model would be most confident exactly where the music is plainest and least
   ornamented. FACT (Pardo & Birmingham 2002, both extraction passes): their `N` is unconditional —
   *"sum of weights for notes not matching any template element"* — and the second extraction pass
   records that *"the paper does not explicitly justify why N is subtracted rather than ignored"*;
   the choice is presented without a theoretical ground. FACT (Masada & Bunescu 2018): the published
   model does **not** leave this unconditional — it carries *"figuration-controlled"* variants of the
   purity and coverage features that *"ignore notes that were heuristically detected as figuration"*,
   with figuration detected by rules covering *"passing and neighbor notes"* and *"suspensions and
   anticipations"*. That is the same correction made outside the model, by heuristic; S7 requires it
   made inside the model, by S1's role assignment, so that the choice of role is scored rather than
   assumed.
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: charging an ornament its own price is not a
   licence to explain any tone away, because the ornament model's own factors (metric position,
   melodic approach and departure, duration, voice) make an implausible ornament expensive.
   **False-negative path:** if the ornament model is too permissive, a reading can buy an arbitrary
   chord by declaring the inconvenient tones ornamental — the failure would appear not as a wrong
   ornament label but as a wrong chord, with the ornament labels never inspected. The path is closed
   only by grading the role assignment itself, which S26 shows the exemplar annotations cannot
   support; that is the strongest reason S26 is an open question rather than a detail.
6. **What would falsify it.** **Observable:** the candidate scores of two readings of one stretch
   that differ only in whether a given foreign tone is assigned an ornament role. **Decision rule:**
   if the reading that assigns the role is charged the same amount for that tone as the reading that
   does not, the negative-evidence term is unconditional and S7 is violated. **Not falsified by:** an
   implausible ornament costing as much as, or more than, an unexplained tone — that is the ornament
   model working.

---

**S8 — The lowest sounding tone is a separate term from the pitch-class content, because inversion
is decided by it and by almost nothing else.**

1. **Statement.** The identity of the lowest sounding tone event, and the span over which it is
   lowest, enter as their own term. They are not recoverable from the set of pitch classes present,
   and inversion cannot be scored without them.
2. **Defense.** THEORY: root position, first inversion and second inversion share their pitch-class
   content exactly and differ only in which factor is in the bass; a term over pitch classes alone
   is constant across all three, so a model without a bass term cannot rank inversions at all.
   Further, the bass carries evidence beyond inversion — a cadential six-four is recognised by a bass
   that does *not* move while the upper voices do, and the perfect/imperfect distinction at a cadence
   turns on the bass arrival. FACT (Masada & Bunescu 2018, cross-checked): the published model
   carries sixteen bass features (f₂₀–f₃₅) comparing *"lowest note in first event (or overall) to
   chord tones"*, with the stated reading that *"if the bass note instead matches the chord's third
   or fifth, this may indicate that the chord is inverted."*
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the lowest sounding tone is a well-defined
   quantity over a candidate stretch. **False-negative path:** it is not always well defined — the
   lowest tone can change inside a stretch (a moving bass under one harmony, an arpeggiated bass, a
   bass rest, a texture with no true bass voice). Each of those is a case where "the bass of this
   stretch" needs a rule, and the rule is a design decision this statement does not take. The
   published model's own answer is to carry *both* "first event" and "overall" variants rather than
   choose, which is evidence that the question is real and not settled by inspection.
6. **What would falsify it.** **Observable:** the candidate scores assigned to the three inversions
   of one triad over one stretch. **Decision rule:** if they are equal by construction, there is no
   bass term. **Not falsified by:** the three scores being close where the bass is genuinely
   ambiguous, for instance under S8's own unresolved case of a moving bass.

---

**S9 — Notated spelling is a term distinct from pitch class, and the model may not reduce the
notation to pitch classes before scoring.**

1. **Statement.** Whether a tone is written G♯ or A♭ is evidence, and it is evidence the pitch class
   does not carry. The scored observation is the spelled tone.
2. **Defense.** THEORY and FACT (Temperley 2000, *The Line of Fifths*, fetched and read): enharmonic
   equivalents are not interchangeable in tonal cognition — *"the same NPC interval can have very
   different qualities in different TPC guises"* — and the paper's own example turns on a spelling
   choice determining whether a chord reads as A7 or E♭7. FACT (same paper): the author reports two
   passages with *identical* pitch-class distributions and different key implications, which is a
   direct demonstration that a pitch-class representation is lossy for exactly the question the
   analysis asks. FACT (same paper): the paper argues the dependency runs the way this statement
   needs — *"spelling information is determined independently of key, and then serves as input in
   key determination"* — and reports that key-finding benefits from spelled rather than
   pitch-class-mod-12 input. FACT (Temperley 2002, *A Bayesian Approach to Key-Finding*, fetched and
   read): the same key model measured **83.8 %** without spelling distinctions and **87.4 %** with
   them. SALVAGED (**D-033**): within its scope a layer uses all the information the note reader
   carries losslessly, notated spelling named among them.
3. **Source class.** derived, corroborated by salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the notated spelling in our sources reflects a
   musical judgment rather than an engraving accident. **False-negative path:** Temperley states the
   counter-case himself — composers sometimes spell *"based on matters of convenience, rather than
   substantive musical factors"*, and a source that has passed through transposition, machine
   translation or a reduction may carry spellings no one chose. The exemplars carry a live instance
   of the hazard: one of the two annotation files for each chorale records that it reached the
   repository by *"Automated translation"* (`Chorales/001/analysis_BCMH.txt` and
   `Chorales/003/analysis_BCMH.txt`, the Proofreader field). So the spelling term must be able to
   carry *how reliable this source's spelling is*, rather than trusting it uniformly.
6. **What would falsify it.** **Observable:** the model's candidate scores for one passage and for
   the same passage with every tone respelled enharmonically. **Decision rule:** if the scores are
   identical, spelling is not a term. **Not falsified by:** the scores being identical for a passage
   where no respelling changes any interval's diatonic size — there the two representations agree and
   nothing should move.

---

**S10 — Duration enters as the weight on every tone-level observation, and it is not a term of its
own.**

1. **Statement.** Wherever a tone event is an observation — as chord-factor presence, as negative
   evidence, as an ornament — it enters weighted by how long it sounds within the candidate stretch.
   "How long the tones sound" is not a separate quantity added beside the others.
2. **Defense.** THEORY: a tone sounding for a whole bar and a tone sounding for a thirty-second are
   not equal evidence for the same chord, and the difference between them is exactly duration, not a
   second property. FACT (Pardo & Birmingham 2002, both passes): the published system weights notes
   by *"the number of minimal segments a note spans"*, and applies that weight to the positive and
   negative terms alike. FACT (Masada & Bunescu 2018, cross-checked): duration-weighted variants
   appear throughout, of the form
   `f₂(s,y) = Σ_{n∈s.Notes} 𝟙[n ∈ y]·n.len / Σ_{n∈s.Notes} n.len` — the weight multiplies the
   observation rather than standing beside it. **The denominator in that published form is the
   subject of S16 and is not adopted here.**
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the durational weight is linear in sounding
   time. **False-negative path:** it may not be — a tone twice as long may be less than twice the
   evidence, and the published models above assert linearity without testing it. A non-linear weight
   is a different model and would show as a systematic error on stretches with extreme duration
   ratios; the linearity is therefore an ASSUMPTION carried openly rather than a FACT, and S23's
   fit discipline governs any value attached to it.
6. **What would falsify it.** **Observable:** the model's parameter set and its per-observation
   arithmetic. **Decision rule:** if there is a term whose argument is the durations of the stretch's
   tones and which is not a weight on some other observation, duration has become its own term and
   S10 is violated. **Not falsified by:** the *stretch's* total duration entering the boundary term
   (S29) — that is a property of the stretch, not of a tone.

---

**S11 — Metric placement enters twice, as two separate terms with different arguments: as evidence
about where a boundary falls, and as evidence about a tone's role.**

1. **Statement.** One term takes the metric weight of the candidate stretch's **starting instant** and
   bears on whether a chord change happens there. A different term takes the metric weight of an
   individual **tone event** and bears on whether that event is a chord member or an ornament. These
   are two terms; collapsing them into one is a modelling error.
2. **Defense.** THEORY: the two are separate conventions and can point opposite ways in one passage.
   Chord changes tend to fall on strong beats. Ornaments tend to fall on weak beats — but the
   suspension and the appoggiatura are precisely the ornaments that fall on strong beats, which is
   why they are dissonances of accent. A single "strong beats favour chord tones" term would make
   every suspension improbable at the moment the theory says to expect it. FACT (Masada & Bunescu
   2018, cross-checked): the published model's metrical feature f₃₆ is the *"accent value of the
   first event in a candidate segment"* — a boundary-level term, whose stated ground is that
   *"chord changes tend to attract an accent"* — while accent-weighted variants of purity and
   coverage are separate, tone-level features. FACT (desk trace, S1's own case, `003 …mscx` bar 4):
   the two candidate role assignments there are separated in opposite directions by the two uses —
   G♯ falls **on** the beat and A falls off it, which favours G♯ as the chord member; A sounds four
   times as long, which favours A. A model with one metric term cannot represent that opposition.
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: metric weight is available and meaningful for
   the music the analysis meets. **False-negative path:** it is neither where the notated meter is
   nominal (unmetered music, recitative, music whose bar lines are editorial) nor where the metric
   hierarchy is genuinely ambiguous. In that case both terms lose their argument at once, and the
   model must be able to run with them inert rather than silently reading a default accent. A term
   that silently reads a default is the shape the defect catalog names **DT-1** (an unverified causal
   premise carrying load).
6. **What would falsify it.** **Observable:** the model's terms and their arguments. **Decision
   rule:** if the metric weight of a tone event and the metric weight of a stretch's first instant
   feed the same term with the same strength, S11 is violated. **Not falsified by:** the two terms
   being fitted to similar strengths.

---

**S12 — What precedes and what follows enter as a term over the sequence of committed readings, never
as a term inside the fit of one stretch.**

1. **Statement.** The evidence that a chord is likely because of the chord before it is a transition
   term whose arguments are two adjacent readings. It is not admitted as a bonus or penalty inside
   the term that judges how well one reading fits the tones sounding in its own stretch.
2. **Defense.** THEORY: the two are different claims about different observations. "These tones fit
   this chord" is a claim about the sounding music; "this chord follows that one" is a claim about a
   progression and is true or false independently of what sounds. Mixing them means a candidate can
   be rewarded for fitting the tones by a term that never looked at the tones. FACT (Masada &
   Bunescu 2018, cross-checked): the published model separates them structurally — the segment-label
   features **F**(s,y,x) and the label-transition features **G**(s,y,x) are distinct vectors with
   distinct weight vectors, and the transition features g₁ are chord bigrams. FACT (Temperley 2002,
   fetched and read): the same separation appears on the tonality axis — the key model's transition
   term is a fixed modulation probability, *"0.8 probability of remaining in the same key versus
   0.2/23 for switching"*, entirely separate from the pitch-class likelihood. SALVAGED (**D-171**,
   principle #7): a layer is enhanced only with what belongs to it.
3. **Source class.** derived, corroborated by salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: separating the two loses nothing, because the
   product of a fit term and a transition term reaches every reading a mixed term could reach.
   **False-negative path:** it would lose something if a genuine interaction existed — if, for
   example, the *degree* to which a stretch's tones support a chord depended on what preceded it (a
   chord anticipated by the previous harmony being recognisable on less evidence). Such an
   interaction cannot be expressed as a product of the two separate terms, and its existence is an
   open empirical question this statement does not settle. It is named here so that a later design
   that needs it declares it rather than smuggling it back into the fit term.
6. **What would falsify it.** **Observable:** the arguments of each term. **Decision rule:** if any
   term that changes with the identity of the neighbouring reading also takes the stretch's own tone
   events as an argument, the separation is broken. **Not falsified by:** the two terms multiplying
   together in the total — that is the combination rule (S18), not a mixed term.

---

### 1.3 The form of a term

---

**S13 — Every term is a conditional probability of an observation given the candidate reading — a
factor of a likelihood — and not a count, a bonus, a penalty or an unbounded weight.**

1. **Statement.** Each term states how probable the observation it takes as its argument is, given
   that the candidate reading is the true one. Its range is the unit interval; its meaning is fixed
   without reference to any other term; and it has a unit — probability — rather than an arbitrary
   scale.
2. **Defense.** THEORY (probability): three properties follow from the form and from no other, and
   each is needed by a decision this model must make. **(i) The combination rule is derived rather
   than chosen** — factors of a likelihood multiply, and nothing has to be decided about how strong a
   count is relative to a penalty (S18). **(ii) Two candidates over stretches of different extent are
   comparable**, because both are probabilities of the *same* observed music under different
   hypotheses (S27, S28) — which is the property the segmentation decision needs and the property an
   arbitrary-unit total cannot have. **(iii) The model can say a stretch is badly explained by every
   candidate**, because a likelihood has an absolute value, where a ranking margin has only a
   relative one (S36). FACT (Temperley 2002, fetched and read): the key model is stated as
   `p(structure | surface) ∝ p(surface | structure) · p(structure)`, and the whole-piece score is
   the product of per-segment, per-pitch-class factors. FACT (Masada & Bunescu 2018, cross-checked):
   the segmental model's score is exponentiated and normalized by
   `Z(x) = Σ_{s',y'} exp(wᵀF(s',y',x))` *summed over all labelled segmentations*, which is what makes
   its scores comparable across segmentations at all. **EXCLUDED ALTERNATIVE, recorded because an
   excluded alternative is evidence about the choice:** Pardo & Birmingham's `S = P − (M + N)`, a
   published, working and much simpler form. It is excluded not because it performs badly — the paper
   reports 88.66 % labelling accuracy with segmentation supplied — but because its three terms are on
   scales that are only implicitly commensurable: `P` and `N` are duration-weighted sums, `M` is a
   plain count, and the subtraction asserts they can be added. That is the shape the boot pack's
   defect catalog names **DT-8** (scale-incommensurable comparison).
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the quantities the model needs to compare are
   genuinely probabilities of observations, so a probabilistic reading of each term is available.
   **False-negative path:** it is not available for a term whose argument is not an observation. A
   term expressing a *preference* — that simpler analyses are better, that a reading agreeing with
   the key signature is better — is not the probability of anything observed, and forcing it into
   likelihood shape by inventing an observation for it is the defect the catalog names **DT-9** (an
   unvalidated proxy standing in for the quantity actually wanted). Such a preference belongs in the
   prior over candidates, where it is a probability of a *hypothesis* and not of an observation, and
   the model must say for each term which of the two it is.
6. **What would falsify it.** **Observable:** each term's stated range and unit. **Decision rule:** a
   term whose value can exceed one, or whose value has no stated interpretation as a probability of a
   named observation or of a named hypothesis, violates S13. **Not falsified by:** the arithmetic
   being carried out in log space with terms that are negative numbers — that is the same quantity in
   a different representation, and S13 is about the quantity.

---

**S14 — Choosing the probabilistic form is defended on comparability and derivability, and NOT on a
claim that it will measure more accurately; that claim is unestablished and a measured counter-case
exists.**

1. **Statement.** S13's ground is what the form makes possible, not what it is expected to score. Any
   claim that adopting it will raise agreement with human annotations is unestablished until measured
   on this project's own data, and the record of the field does not support assuming it.
2. **Defense.** FACT (Temperley 2002, fetched and read): in that paper's own reported comparison, the
   properly Bayesian variant — the one that scores *absent* pitch classes as well as present ones,
   and is therefore the more complete likelihood — measured **77.1 %**, while the flat-input
   key-profile variant, which is not a likelihood at all, measured **83.8 %**. The extraction records
   that the author leaves the gap unexplained. THEORY: this is what one expects when a likelihood's
   independence premise is badly violated — a well-formed model with a false factorization can be
   beaten by an ill-formed model whose errors happen to cancel. SALVAGED (boot pack **D-182**,
   principle #19): a recorded figure is trusted only once positively established, never because it is
   merely unfalsified. SALVAGED (**D-029**): prefer what can be checked against ground truth, and
   where sound theory cannot be checked, build it with an explicit unvalidated mark rather than
   refusing it — which is exactly the standing this statement gives S13.
3. **Source class.** derived; the accuracy claim it refuses is **measured** and **UNESTABLISHED**.
   The measurement it would need: the two forms fitted under one capacity budget and graded on held-
   out annotated music, per axis, with uncertainty (#20, #24).
4. **Status.** settled — as a bar on what may be claimed. The underlying accuracy question is open.
5. **Premise, and its false-negative path.** Premise: Temperley's measured reversal is evidence about
   models of this kind generally, not only about that one model. **False-negative path:** it may be
   specific to the absent-pitch-class term, or to his segmentation, or to his corpus — in which case
   this statement is over-cautious, and the cost of the over-caution is that a real improvement gets
   carried as unvalidated for longer than necessary. That cost is accepted, and is the smaller of the
   two errors here.
6. **What would falsify it.** **Observable:** any document, dispatch or report of this project that
   states or implies that the probabilistic form is more accurate. **Decision rule:** such a statement
   is unsupported unless it cites a held-out measurement on this project's data. **Not falsified by:**
   a *prediction*, recorded before measuring, that it will be more accurate — the Premise Gate
   requires such predictions and this statement does not forbid them.

---

**S15 — A term whose value is a proportion of the stretch — a ratio with the stretch in its
denominator — is not admissible as a factor of the likelihood, because it removes the dependence on
the stretch's extent that the segmentation decision needs.**

1. **Statement.** Terms of the form "the fraction of this stretch's sounding time that is chord tone"
   may be computed and reported as diagnostics, but may not carry the fit. The factor that carries
   the fit is over the tone events themselves, so that a longer stretch accumulates more factors and
   a shorter one fewer.
2. **Defense.** THEORY: if every term is a proportion, then a stretch and the same stretch cut in half
   with the same content score the same, and nothing in the model prefers either — the extent has been
   normalized out of exactly the quantity that is supposed to decide the extent. Conversely, an
   unnormalized product over tone events is automatically extent-sensitive: more observations means
   more factors, and a stretch is preferred precisely when the extra observations are well explained.
   FACT (Masada & Bunescu 2018, cross-checked over two independent extraction passes): the published
   model's duration-weighted features **are** proportions, dividing by the total sounding duration in
   the segment; and the same two passes found, independently, that **the paper states no penalty,
   feature or normalization that controls how many segments the model prefers**. The second pass
   records it as *"The paper does not discuss constraints on segment quantity."* The two facts sit
   together: a model built from proportions has to recover extent-sensitivity from somewhere, and in
   that model it is left to the fitted weights and the partition function rather than to a stated
   term. **This is a gap in the published state of the art, not a settled solution to be copied.**
3. **Source class.** derived.
4. **Status.** settled as to the prohibition; the positive question — what term *does* control the
   number of stretches — is open and is S29.
5. **Premise, and its false-negative path.** Premise: extent-sensitivity should come from the number
   of explained observations rather than from a normalization. **False-negative path:** an
   unnormalized product is extent-sensitive in a way that may be *too strong* — every additional tone
   event multiplies in another factor below one, so a long stretch is penalized simply for containing
   more music, and the model would prefer to cut everything as finely as possible. That is the mirror
   failure, it is real, and S29 is where it is answered. Naming both directions here is what stops
   S15 from being read as "unnormalized is safe".
6. **What would falsify it.** **Observable:** each fit-carrying term's denominator. **Decision rule:**
   if a fit-carrying term divides by a quantity that grows with the stretch, S15 is violated.
   **Not falsified by:** a *reported diagnostic* being a proportion — proportions are the readable
   form for a human and are welcome outside the fit.

---

**S16 — No term may be applied after a winner has been selected.**

1. **Statement.** Every term participates in the comparison that chooses the winner. A quantity
   computed from the winning reading and then used to adjust, correct, override or re-rank it is not
   a term of this model; it is a second decision procedure, and this model has one.
2. **Defense.** SALVAGED (**D-170**, principle #6): one path per concern — two places that decide
   which reading wins are two paths for one concern. SALVAGED (**D-171**, principle #7): a layer is
   enhanced only with what belongs to it. THEORY: a post-selection adjustment cannot be given a
   probabilistic reading, because by the time it runs the probability it would have to modify has
   already been maximized; so admitting one forfeits every property S13 was chosen for. Further, the
   adjustment's own effect is unmeasurable in the ordinary way — it is applied to whatever the first
   procedure happened to pick, so its behaviour depends on the first procedure's errors rather than
   on the music, and a change to either changes the other's population. That dependence is the shape
   the defect catalog names **DT-14** (a mechanism guarded by a precondition its real population
   almost never satisfies) waiting to happen.
3. **Source class.** derived, resting on salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: everything a post-selection adjustment could
   express can be expressed as a term inside the comparison. **False-negative path:** it could not be,
   if the quantity the adjustment uses is only definable once a winner exists — for instance "how far
   ahead of the runner-up the winner is". Such a quantity is real and useful, but it is a **confidence
   read-out** (S35), not evidence, and using it to change the winner would be circular. The
   distinction — a quantity computed from the ranking may be *reported*, never *fed back* — is what
   keeps this premise true, and it is stated so the exception is not discovered later as a licence.
6. **What would falsify it.** **Observable:** the order of operations from evidence to committed
   reading. **Decision rule:** if any committed reading can differ from the argmax of the candidate
   score, some quantity acted after selection and S16 is violated. **Not falsified by:** a later layer
   *selecting a different reading from the carried alternatives* on evidence that layer owns — that is
   a different decision by a different layer with its own evidence, not an adjustment to this one.

---

### 1.4 How the terms combine

---

**S17 — The terms combine as a product of factors, equivalently a sum of their logarithms; not as a
weighted sum of unlike quantities and not lexicographically.**

1. **Statement.** The candidate score is the product of every factor, and the comparison between two
   candidates is the comparison of those products.
2. **Defense.** THEORY (probability): given S13, the product is not a choice — it is what a joint
   probability of conditionally independent observations *is*. Choosing any other combination rule
   would mean the terms are not the probabilities S13 says they are. **Lexicographic combination is
   excluded:** ordering candidates by one term and using the others only to break ties asserts that no
   quantity of evidence in the later terms can outweigh any difference in the first, and no
   music-theoretic claim supports that about any pair of these terms — the whole difficulty of the
   subject is that bass evidence, pitch-class evidence and metric evidence routinely conflict and are
   traded off. **A weighted sum of unlike raw quantities is excluded** for the reason S13 gives
   against `P − (M + N)`: it requires a commensurability between a duration-weighted sum and a plain
   count that nothing establishes (**DT-8**).
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the factors are conditionally independent given
   the candidate reading — see S18, which is where that premise is stated and where it is shown to be
   false in a known way. **False-negative path:** carried by S18.
6. **What would falsify it.** **Observable:** the arithmetic that reduces the terms to the candidate
   score. **Decision rule:** if it is not a product of the factors, or a sum of their logarithms,
   S17 is violated. **Not falsified by:** the sum of logarithms being computed with per-term
   multipliers, which is S19's declared departure and is governed there.

---

**S18 — The product form carries a conditional-independence premise, and the model declares that
premise explicitly, per factor group, together with the path by which it could be false without
showing.**

1. **Statement.** Writing the likelihood as a product of factors asserts that, **given** the candidate
   reading — its tonality, its chord, its extent and its role assignment — the observations those
   factors take as arguments are conditionally independent of one another. The model states which
   groups of observations that assertion covers, and states for each group how a violation would
   manifest.
2. **Defense.** THEORY (probability): the product form is exactly equivalent to the conditional
   independence assertion; there is no version of the one without the other. FACT (Temperley 2002,
   fetched and read, and this is the paper's own statement of its premise): the key model assumes
   *"twelve independent decisions as to whether or not to use each pitch class."* SALVAGED
   (**D-180**, principle #17(a) and (e)): every load-bearing causal claim is labelled FACT / THEORY /
   ASSUMPTION, and every insulation claim — every "X cannot affect Y" — must enumerate the
   false-negative path explicitly. A conditional-independence premise **is** an insulation claim, in
   the form "given the chord, observing this tone tells us nothing further about that one", so
   principle #17(e) applies to it directly and is what makes this statement mandatory rather than
   good practice.
3. **Source class.** derived, resting on salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** The premise is the subject of the statement. Its
   **false-negative path**, in the general form: a violated independence premise does **not** show as
   a wrong answer on the cases where it is violated. It shows as **over-confidence** — the product
   over-counts correlated evidence, so the winning candidate's margin over the runner-up is inflated,
   while the winner itself is often still right. A model checked only by whether the winner is correct
   will therefore never detect it. Detecting it requires checking the **calibration** of the score:
   whether readings the model gives probability *p* are correct about *p* of the time. That is a
   measurement over the carried alternatives and their margins, not over the winners, and it is the
   reason S35 requires the alternatives to be published.
6. **What would falsify it.** **Observable:** the model's own written statement of its factorization
   and the independence groups it asserts. **Decision rule:** a factor group with no written premise,
   or with a premise that names no path to being false, violates S18 — the absence of the statement is
   the violation, independently of whether the premise happens to hold. **Not falsified by:** a
   declared premise turning out to be false; S18 requires the declaration, and S19 is what a known
   falsity then obliges.

---

**S19 — The known violation of independence is repetition: the same pitch sounding again is not
independent evidence, so the model's tone-level factors are over sounding time, not over note
onsets.**

1. **Statement.** A pitch class restruck five times in a stretch does not supply five times the
   evidence of one sounding. The tone-level factors therefore take the **duration** of a pitch's
   presence as the observation, per S10, and do not multiply in one factor per notated onset. Where
   the model nonetheless needs an onset-level factor, it declares that it is over-counting and states
   what it does about it.
2. **Defense.** FACT (Temperley 2002, fetched and read; this is the paper's own diagnosis of its own
   model): *"the weighted-input approach assumes a generative model in which the composer decides to
   use C and G once, and then makes eight independent decisions to use E. But a more plausible model
   is that the composer decides to use certain pitch-classes, and then decides to repeat one of
   them."* FACT (same source, the consequence stated by the author): such models *"tend to give
   excessive weight to repeated events."* THEORY: repetition of a tone is governed by texture,
   figuration and instrument idiom — an Alberti bass, a repeated-chord accompaniment, a tremolo —
   which are causes of the observation that have nothing to do with which chord is sounding, so
   conditioning on the chord does not make the repetitions independent.
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: duration-weighting removes the over-counting.
   **False-negative path:** it removes only part of it. A repeated-chord accompaniment and a single
   sustained chord of the same total duration are treated identically by a duration-weighted model,
   which is right for this question; but two *different* pitches sounding simultaneously in an
   octave-doubled texture are still counted twice, and doubling is likewise a texture decision, not
   evidence about the chord. So the residual violation is **octave doubling and voice count**, and it
   is not closed by S19. It is named here rather than left to be rediscovered: a model that
   duration-weights and believes itself finished with this premise is the more dangerous state,
   because it has a defensible answer to the question and an unnoticed remainder.
6. **What would falsify it.** **Observable:** the candidate scores for a stretch and for the same
   stretch with one of its tones restruck several times at the same pitch, with the total sounding
   time unchanged. **Decision rule:** if the two scores differ, an onset-level factor is
   over-counting. **Not falsified by:** the two scores differing through a *boundary* term, since
   restriking creates new partition points and therefore new admissible boundaries — the comparison
   must hold the candidate stretch fixed.

---

**S20 — Per-factor weights on the log-factors are a declared departure from the pure product, and the
all-weights-equal setting is a mandatory measured comparison arm, not a formality.**

1. **Statement.** If the model raises factors to fitted powers — equivalently, multiplies the
   log-factors by fitted weights — that is a departure from the likelihood S13 defines, and it is
   declared as one. The model is fitted and reported **with** and **without** those weights, and the
   weighted arm must beat the unweighted arm on held-out data before the weights are kept.
2. **Defense.** THEORY: per-factor powers are the standard repair for a violated independence premise
   — they let a factor group that is internally correlated contribute less than its raw count implies.
   They are therefore a **correction for a modelling error**, and their size measures how wrong the
   factorization is. That makes the unweighted arm the diagnostic that matters, not a baseline to be
   waved past. SALVAGED (**D-182**, principle #19): trusted only once positively established.
   SALVAGED (principle #20 as carried in the boot pack's principles file): every fit event declares
   its held-out data and its capacity budget before fitting, and the headline claim is the held-out
   figure; a fitted-and-self-measured number is not established.
3. **Source class.** derived, resting on salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: a large fitted weight indicates a bad
   factorization rather than a genuinely strong evidence source. **False-negative path:** it can
   indicate either, and the two are not distinguishable from the weight alone. What distinguishes
   them: a weight correcting an independence violation should **shrink as the factor group's
   internal correlation is modelled properly**, whereas a weight reflecting genuine evidence strength
   should not move. So the diagnostic is not the weight's size but its **movement** when the
   factorization is improved — which requires the weights from before and after to be kept side by
   side (#12).
6. **What would falsify it.** **Observable:** the fit record. **Decision rule:** a weighted model
   reported without an all-weights-equal arm measured on the same held-out data violates S20.
   **Not falsified by:** the unweighted arm measuring worse — that is the expected outcome and is what
   the comparison is for.

---

**S21 — The comparison between candidate scores is exact: no tolerance, no epsilon, and ties are
resolved by a declared total order stated in advance.**

1. **Statement.** Two candidate scores are compared as they are. Where they are equal, the winner is
   chosen by an order over candidates that is declared before any music is analysed, is total (it
   leaves no pair unresolved), and is deterministic across platforms and runs.
2. **Defense.** THEORY (numerical): a comparison with a tolerance makes the winner depend on the
   order in which the arithmetic was performed and on the precision of the machine, so the same music
   can analyse differently on two builds. SALVAGED (principle #16 as carried in the boot pack's
   principles file): reproducibility — every measurement is stamped to its inputs and its tool. A
   result that cannot be reproduced on another machine cannot be stamped to anything. THEORY: exact
   ties are not a numerical accident here but a musical reality — a symmetric sonority such as a fully
   diminished seventh or an augmented triad has no pitch-class-decidable root, so several candidate
   readings are genuinely equally supported by the pitch-class evidence, and the model will meet exact
   ties as a matter of course. FACT (Pardo & Birmingham 2002, both extraction passes): that published
   system needed **three** ordered tie-break rules — highest root weight, then prior probability,
   then a diminished-seventh contextual rule — and reports that even with all three applied the share
   of segments with unresolved ties only *"drops below 2 %"*. Ties are common enough to need a
   declared answer.
3. **Source class.** derived, resting on salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: a declared total order is better than an
   arbitrary one because it is inspectable and stable. **False-negative path:** a total order also
   *hides* the tie — the model commits, and a reader sees a winner where the evidence had none. That
   is a real information loss (#12), and it is closed not by weakening the order but by S35: the
   runner-up and the margin are published, so a zero margin is visible as a zero margin.
6. **What would falsify it.** **Observable:** the analysis of one score run twice, on two machines or
   two builds, with the arithmetic reordered. **Decision rule:** any difference in the committed
   readings falsifies S21. **Not falsified by:** a difference caused by different fitted values or
   different inputs — the comparison must hold those fixed.

---

### 1.5 Where the numbers come from

---

**S22 — The form of every factor is derived from music theory before any number is attached to it,
and no factor exists whose only justification is that fitting it improved a measurement.**

1. **Statement.** A factor enters the model because a music-theoretic claim says the observation it
   takes bears on the chord. Its numerical strength is then fitted. A factor discovered by searching
   for quantities correlated with the annotations, and justified afterwards, is not admitted.
2. **Defense.** SALVAGED (**D-096**): *"Factor FORMS come from theory; factor VALUES are fit ONCE
   against ground truth and are never tuned per case. Every factor's shape is derived from
   established music theory before any number is attached to it."* SALVAGED (**D-168**, principle
   #4): the objective is maximum-precision inference — which is what makes a correlate that
   generalizes badly worse than no factor at all. THEORY: a factor derived from theory carries a
   prediction about *where* it will fire and *which way*; a factor found by correlation carries no
   such prediction, so nothing about it is falsifiable except the measurement that produced it, and
   a later corpus can only confirm or disconfirm it as a whole.
3. **Source class.** salvaged.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: theory is a rich enough source of factor forms
   that this restriction does not starve the model. **False-negative path:** it may not be, for
   phenomena the theory does not name — texture, instrument idiom, engraving convention, corpus-
   specific notation habits — which demonstrably bear on the observations (S19's repetition case is
   one). Where such a factor is genuinely needed, the honest route is to state the mechanism as a
   CONJECTURE, write the prediction before measuring, and carry it marked unvalidated (S14's
   standing) — not to relabel a correlate as theory after the fact.
6. **What would falsify it.** **Observable:** the written defense at each factor. **Decision rule:**
   a factor whose defense names no music-theoretic claim and no published research, and instead names
   a measurement it improved, violates S22. **Not falsified by:** a theory-derived factor being
   *retired* because measurement showed it inert — removing an unearning factor is not the same act as
   admitting an unexplained one.

---

**S23 — The number of free parameters is declared against the number of independent training
observations before fitting, and the per-factor separations this model asks for are counted against
that budget.**

1. **Statement.** Before any value is fitted, the model states how many free parameters it has and
   how many independent observations the annotated music supplies for them. Every separation S5, S6
   and S11 require — per chord factor, present versus absent, two metric terms — multiplies the
   parameter count, and the increase is stated at the same time as the separation is claimed.
2. **Defense.** SALVAGED (principle #20 as carried in the boot pack's principles file): every fit
   event declares its held-out data and its capacity budget — parameter count, regularization,
   justified against corpus size — **before** fitting; the headline claim is the held-out figure.
   THEORY (statistics): the separations this document argues for are each defensible individually and
   compound multiplicatively; a model with a per-factor, per-presence-mode, per-metric-position,
   per-inversion parameter has a cell count that outruns any chorale corpus, and its per-cell
   estimates then measure sampling noise. **This statement is the counterweight to S5, S6 and S11
   and is placed here deliberately:** those three statements each argue for more parameters on
   theoretical grounds, and a document that argued only in that direction would be recommending an
   unfittable model.
3. **Source class.** salvaged, with a derived consequence.
4. **Status.** settled as a requirement; **open** as to what the budget permits, which cannot be
   decided without knowing the corpus size and the fit design.
5. **Premise, and its false-negative path.** Premise: the annotated observations are independent
   enough to count. **False-negative path:** they are not — chorales by one composer in one style,
   annotated by one analyst, supply far fewer independent observations than their event count
   suggests, and a budget computed from the event count will be too generous by an unknown factor.
   Naming the effective sample size rather than the raw count is the honest form, and this session
   cannot supply either.
6. **What would falsify it.** **Observable:** the fit record. **Decision rule:** a fit performed with
   no declared parameter count and no declared budget violates S23, whatever its result. **Not
   falsified by:** the budget being generous, provided it is stated and defended.

---

**S24 — No value is graded on the music that helped fit it, and the reported figure is the held-out
figure.**

1. **Statement.** The fit declares its held-out data — a split or a k-fold — before fitting. Every
   figure reported as the model's quality is computed on data that took no part in choosing any
   value.
2. **Defense.** SALVAGED (principle #20 as carried in the boot pack's principles file): *"No value is
   graded on data that helped fit it… A fitted-and-self-measured number is not established (#19)."*
   SALVAGED (**D-182**, principle #19). THEORY (statistics): a model with the parameter count S23
   warns about can reach an arbitrarily good figure on its own fitting data, so a self-measured
   figure carries no information about the model at all — it measures the parameter count.
3. **Source class.** salvaged.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: a split of the annotated music produces two
   genuinely independent halves. **False-negative path:** it does not, where the same chorale melody
   is harmonised twice in the corpus, where two annotation traditions cover the same works, or where
   the split is made at the event level rather than the piece level. The exemplars show the hazard
   directly: two of the three chorales here carry **two** independent readings of the same music, and
   a naive split could place one reading in the fitting half and the other in the held-out half —
   which would leak the answer while satisfying the letter of the rule. The split is therefore made
   over **works**, not over annotations or events, and the rule is stated that way.
6. **What would falsify it.** **Observable:** the fit record's declared split, and the works on each
   side of it. **Decision rule:** any work appearing on both sides, under any annotation, falsifies
   the split's independence. **Not falsified by:** two *different* works sharing a chorale tune,
   which is a weaker dependence and is recorded rather than excluded.

---

**S25 — A factor whose value cannot be counted from the available annotations is either given a
value derived from theory and declared as such, or is an open question — it is never fitted against
a proxy for the quantity it needs.**

1. **Statement.** Where the annotated music does not record the quantity a factor is about, the
   model may not fit that factor against something else that correlates with it. It states the value
   from theory, marked unvalidated, or it leaves the factor open.
2. **Defense.** FACT (exemplars, examined directly): **the role assignment S1 makes part of the
   scored object is not recorded in either annotation tradition.** `Chorales/001/analysis.txt`,
   `Chorales/001/analysis_BCMH.txt`, `Chorales/003/analysis.txt`, `Chorales/003/analysis_BCMH.txt`
   and `Chorales/134/analysis.txt` record chord labels at positions and nothing about individual
   tone events; the only place a role is named anywhere in the five files is in **prose notes** an
   analyst wrote for a human reader — *"If G# is an incomplete neighbor…"*, *"with A as a regular
   neighbor"*, *"parallel fifths evaded by voice crossing in m. 6"*. So the ornament model's own
   parameters have **no directly countable ground truth in these sources.** SALVAGED (**D-180**,
   principle #17(d)): every proxy-to-target link is itself a premise, and a structural proxy never
   stands in for a behavioural quantity unvalidated — which is the shape the defect catalog names
   **DT-9**. THEORY: fitting the ornament model against chord-label agreement means fitting it against
   the outcome it is supposed to be an input to, so it will absorb every other error the model makes.
3. **Source class.** derived; the extent of the gap beyond these five files is **measured** and
   **UNESTABLISHED** — the measurement it would need is an inventory of which annotation sources, if
   any, record per-tone chord-tone-versus-ornament labels, and at what agreement.
4. **Status.** **open.** This is the largest open question in this derivation and §2 states it as one.
5. **Premise, and its false-negative path.** Premise: the ornament model needs its own ground truth
   because it is a distinct claim from the chord label. **False-negative path:** it might not — if the
   role assignment were fully determined by the chord label plus the tones, then annotating the chord
   would annotate the roles implicitly and the gap would be illusory. That is exactly false in S1's
   case, where **the same tones and two different chord labels** are each consistent with a role
   assignment; but S1 is one bar, and how often the roles are recoverable from the label is not known
   here. Recording the path this way says precisely what would close the question.
6. **What would falsify it.** **Observable:** the provenance recorded for each fitted value.
   **Decision rule:** a value for a per-tone role factor reported as fitted, whose fit record names as
   its target a quantity other than annotated per-tone roles, violates S25. **Not falsified by:** such
   a value being *stated from theory* and marked unvalidated — that is the permitted route.

---

**S26 — The style of the music enters only as a prior over the fitted values, never as a filter over
which candidates exist.**

1. **Statement.** A style setting may change how strongly a factor weighs. It may not remove a chord
   from the candidate space, and it may not change the structure of the model.
2. **Defense.** SALVAGED (**D-024**): the fact layers are style-agnostic and lossless; style-
   specificity lives *only* in the calibration of the judging layers — their priors and weights —
   **never in structure**. SALVAGED (**D-003**): inference is preset-independent; presets are
   presentation concerns. THEORY: a style filter over the candidate space makes the model unable to
   be wrong about style — a passage of chromatic harmony inside a piece labelled diatonic becomes
   unanalysable rather than surprising — and it makes the most interesting cases, where the music
   departs from its own idiom, the ones the model handles worst. SALVAGED (**D-201**): very large
   scores of unfamiliar repertoire must be handled and are expected to be more common than the
   corpora fitted on, which is the same argument from the other end.
3. **Source class.** salvaged.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: a prior is always strong enough to do the work
   a filter would do. **False-negative path:** a prior that is *too* weak leaves an implausible
   candidate reachable, and one that is too strong is a filter in all but name — the distinction is a
   matter of degree, and the honest test is not the mechanism's name but whether the note evidence
   can actually override it on a real passage. So the test is stated behaviourally, in field 6, and
   not as "is it implemented as a prior".
6. **What would falsify it.** **Observable:** the candidate space and the committed reading for one
   passage analysed under two style settings. **Decision rule:** if a chord that is reachable under
   one setting is unreachable under another, style has filtered the candidate space and S26 is
   violated. **Not falsified by:** the same chord being ranked differently under the two settings —
   that is the prior working.

---

### 1.6 Comparability

---

**S27 — Two candidate readings are directly comparable exactly when they are scored over the same
observations.**

1. **Statement.** The comparison between two candidate scores is meaningful when both are
   probabilities of the same observed music. Two readings of the same stretch satisfy this. Two
   readings of different stretches do not, on their own, and S28 says what does.
2. **Defense.** THEORY (probability): a likelihood is a function of a hypothesis for **fixed** data.
   Comparing likelihoods computed over different data compares two different functions and means
   nothing. SALVAGED (**D-032**): every confidence crossing a layer boundary is bounded, class-declared
   and named to its decision — which is the same requirement one level up, that a comparable quantity
   states what it is comparable *within*.
3. **Source class.** derived, corroborated by salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: "the same observations" is a checkable
   property. **False-negative path:** it is checkable only if the observation set is explicit. A model
   that filters its observations per candidate — dropping tones it treats as ornamental before scoring
   — silently makes the observation sets differ between candidates, and then the comparison is invalid
   in a way nothing in the arithmetic reveals. **This is the precise technical reason S7 requires the
   ornament to be *scored* rather than *filtered out*:** the filtered model is not merely less
   principled, its comparisons are between different quantities.
6. **What would falsify it.** **Observable:** the set of tone events each candidate's score is
   computed over. **Decision rule:** if two candidates over one stretch are scored over different tone
   event sets, S27 is violated. **Not falsified by:** the two candidates assigning those same events
   different roles — that is S1 working.

---

**S28 — A complete reading of a passage explains every observation in it exactly once, and it is
complete readings that are compared when the segmentation is in question.**

1. **Statement.** The comparison that decides where boundaries fall is between complete readings of a
   whole covered span — every tone event in the span belongs to exactly one candidate stretch and is
   scored exactly once. A model may not compare a two-chord reading of a bar against a one-chord
   reading by comparing one of the two chords against the one.
2. **Defense.** THEORY (probability): this is what makes the scores commensurable — both readings are
   then likelihoods of the same data, differing only in the hypothesis, and S27 is satisfied by
   construction. FACT (Masada & Bunescu 2018, cross-checked): the published model's partition function
   `Z(x) = Σ_{s',y'} exp(...)` is summed over **all labelled segmentations of the input**, which is
   exactly the statement that competing segmentations are normalized against one another over the same
   input. THEORY: without the exactly-once condition, a model that can leave an observation unexplained
   prefers whichever segmentation lets it drop the most inconvenient evidence, and that preference is
   an artifact of the bookkeeping rather than a musical judgment.
3. **Source class.** derived.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: every tone event belongs to exactly one stretch.
   **False-negative path:** a tone event may **span** a boundary — it is sounding before and after the
   chord changes, which is ordinary in a suspension, a pedal tone or any sustained voice. Such an event
   is not naturally the property of one stretch. The exactly-once condition must therefore be stated
   over **sounding time** rather than over notated events: each atomic stretch of each voice's sounding
   time is explained once, and a note spanning a boundary contributes to both stretches in proportion.
   Stating it over events instead would break on the pedal tone, which is the case S1's family is built
   from. This is a correction to the naive form of the statement and is recorded rather than smoothed
   away.
6. **What would falsify it.** **Observable:** the total sounding time scored by a complete reading,
   compared against the total sounding time in the covered span. **Decision rule:** if they differ,
   some observation is unscored or double-scored and S28 is violated. **Not falsified by:** the two
   readings being of different *spans* — the comparison is only defined over one covered span, which
   is what this statement fixes.

---

**S29 — The number of stretches is controlled by a declared term with a stated form, not left to
emerge from the fit; and what that term should be is an open question.**

1. **Statement.** The model carries an explicit term whose argument is the act of placing a boundary,
   or equivalently a prior over how long a chord lasts. Its form is written down and defended. It is
   not left to be an emergent consequence of the other terms' fitted weights.
2. **Defense.** THEORY: S15 establishes that the product form is extent-sensitive by construction, and
   in a direction that is not obviously right — every additional tone event multiplies in another
   factor below one, so unless something opposes it the model prefers to cut the music as finely as the
   atomic stretches allow. Something must oppose it, and if nothing is declared, the opposition comes
   from whatever the fitted weights happen to produce, which is a decision taken by accident. FACT
   (Masada & Bunescu 2018, established by **two independent extraction passes that agreed**): the
   published segmental model states **no** term, feature or penalty controlling the number of segments
   — the second pass records *"The paper does not discuss constraints on segment quantity. No explicit
   penalty or feature preference toward specific segment counts appears in the model formulation or
   feature descriptions."* FACT (Temperley 2002): the analogous question on the tonality axis **is**
   answered explicitly there, by a stated transition probability — *"0.8 probability of remaining in
   the same key versus 0.2/23 for switching"* — so the field does answer this question where it has
   noticed it. FACT (exemplars): the disagreements between the two published readings of chorale 001
   are visibly concentrated on this exact question (S4).
3. **Source class.** derived. The *form* the term should take is **open**.
4. **Status.** **open.** The requirement that such a term be declared is settled; its form is not.
   §2 carries the question.
5. **Premise, and its false-negative path.** Premise: chord duration has a distribution regular enough
   to model. **False-negative path:** it may be governed less by a duration prior than by metric
   structure — chords change on beats, and on some beats more than others — in which case the right
   term is over metric positions (S11's boundary term) and a duration prior would be a worse
   parameterization of the same fact, fitting the tempo and the note values rather than the harmonic
   rhythm. That the two candidate forms are hard to distinguish is precisely why the term must be
   declared and defended rather than emergent.
6. **What would falsify it.** **Observable:** the model's term list. **Decision rule:** if no term
   takes boundary placement or stretch extent as its argument, S29 is violated. **Not falsified by:**
   that term measuring weak once fitted — a declared term measured inert is a finding, and an
   undeclared one is a defect.

---

**S30 — Candidate scores are not comparable across different passages, and no threshold on the raw
score may be used to decide anything.**

1. **Statement.** The score of a reading of one passage says nothing about the score of a reading of
   another. A fixed numerical threshold applied to raw candidate scores — to accept a reading, to
   abstain, to trigger any behaviour — is forbidden.
2. **Defense.** THEORY (probability): a likelihood over more observations is smaller, simply because
   more factors below one are multiplied in. A threshold on it therefore selects for short passages
   and sparse textures, and the selection has nothing to do with analytical quality. This is the shape
   the defect catalog names **DT-8** (scale-incommensurable comparison) applied across passages instead
   of across terms. THEORY: what *is* comparable across passages is a quantity built from the
   competition within each passage — a posterior over candidates, or the margin between the winner and
   the best alternative — because normalizing over that passage's own candidates removes the dependence
   on how many observations it holds. SALVAGED (**D-032**): a confidence crossing a layer boundary is
   in the unit interval, class-declared, and named to its decision — which is exactly the normalized
   quantity and not the raw score.
3. **Source class.** derived, corroborated by salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the normalized quantity is comparable across
   passages where the raw one is not. **False-negative path:** it is comparable only to the extent that
   the candidate sets are comparable. A passage where the model enumerated three candidates and one
   where it enumerated forty produce margins that mean different things, and the normalization hides
   that. So a published confidence carries the size and the identity of the candidate set it was
   normalized over, or it is not comparable either — which is a real limit on S30's own remedy and is
   stated here rather than discovered later.
6. **What would falsify it.** **Observable:** any constant in the model compared against a raw
   candidate score. **Decision rule:** its existence violates S30. **Not falsified by:** a constant
   compared against a normalized confidence or a margin, which is the permitted form.

---

### 1.7 What may never enter the fit

---

**S31 — A written analytical label in the score — a chord symbol, a Roman numeral, a figured-bass
figure, a written key name — never enters the fit as evidence.**

1. **Statement.** Such a label may be read for comparison, for grading and for display. It may not
   contribute to any factor that decides which reading wins.
2. **Defense.** THEORY: a written chord symbol is a human's answer to the very question the model is
   asking. Admitting it makes the model's agreement with human analyses **unfalsifiable** on every
   score that carries one — the model would be graded, in part, on reproducing an input it was given.
   THEORY: it also makes the model's behaviour discontinuous in an invisible way, since the same music
   analyses differently according to whether an editor happened to write symbols above the staff.
   SALVAGED (**D-024**): the fact layers carry facts, never style — and a written analytical label is
   not a fact about the sounding music, it is a judgment about it. **The distinction that must be
   stated to make this rule usable:** the notated **key signature**, **time signature**, **bar lines**,
   **ties**, **beams**, **rests** and **note spellings** are *structural* notation — they record what
   was written to be played, and they are admissible evidence (S9, S11). A Roman numeral is *analytical*
   notation — it records a conclusion. The line falls between what the notation says the music **is**
   and what someone says the music **means**.
3. **Source class.** derived, corroborated by salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the two classes are separable in every source.
   **False-negative path:** figured bass sits close to the line — it is contemporaneous performance
   notation and in one sense structural, but it names harmonies above a bass and in that sense
   analytical. A source carrying figures is therefore not simply admissible or inadmissible; the
   decision needs stating per notation kind, and this statement does not take it for figured bass. It
   names it as the boundary case rather than legislating it.
6. **What would falsify it.** **Observable:** the analysis of one score, and of the same score with
   every written chord symbol and Roman numeral deleted. **Decision rule:** any difference in the
   committed readings falsifies S31. **Not falsified by:** a difference in what is *displayed* or in
   what a comparison reports.

---

**S32 — The analysis's own previous output never enters as evidence for a later analysis.**

1. **Statement.** No committed reading, cached result, stored annotation or previously written
   analysis produced by this system is admitted as an observation. Re-analysing the same music must
   reach the same result from the notation alone.
2. **Defense.** THEORY: a model that reads its own output measures only that it has not changed. Its
   agreement figure becomes a stability figure, and an error, once committed, becomes evidence for
   itself on every subsequent run. THEORY: it also destroys reproducibility — the result then depends
   on the history of the file rather than on its content, so the same score analyses differently
   according to what was done to it before, and no measurement can be stamped to its inputs.
   SALVAGED (principle #16 as carried in the boot pack's principles file): every measurement is
   stamped to corpus and tool. SALVAGED (**D-182**, principle #19): a thing is trusted only when
   positively established, never because nothing has contradicted it — and a self-confirming loop
   produces exactly the appearance of not being contradicted.
3. **Source class.** derived, resting on salvage.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the system's outputs are identifiable as its
   own. **False-negative path:** they may not be, once an output has been written into a score file
   and that file is later used as a source. At that point the system's own analysis is indistinguishable
   from a human's annotation in the same notation — and S31 admits neither as evidence, which is what
   makes S31 and S32 close each other's gap. The pair only holds if **all** analytical notation is
   excluded regardless of who wrote it; excluding only "our own" would leave the loop open through
   any round trip.
6. **What would falsify it.** **Observable:** the analysis of a score, and of the same score after the
   analysis has been written into it and saved. **Decision rule:** any difference in the committed
   readings falsifies S32. **Not falsified by:** an incremental re-analysis reusing computation for
   an unedited span, provided the *result* is identical to a fresh run.

---

**S33 — No factor may be introduced, removed or valued to make a particular passage come out right.**

1. **Statement.** A named passage may motivate an investigation. It may not be the justification for a
   factor's existence or for a value. Every value is fitted once, over the whole fitting set, under
   S23's budget and S24's split.
2. **Defense.** SALVAGED (**D-096**): factor values are fit once against ground truth and are never
   tuned per case. THEORY: per-case tuning is fitting with a sample size of one, so its expected
   generalization is nil while its measured improvement on that case is total — which makes it the
   most rewarding-looking and least valuable change available at any moment. It is the shape the
   defect catalog names **DT-2** (an unestablished constant). SALVAGED (boot pack conventions, the
   candidate-admission ruling): the licence to complete an unfinished rule permits deriving the correct
   rule from the model, **not** loosening a threshold until difficult scores pass.
3. **Source class.** salvaged.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: a change motivated by a case can be told apart
   from a change fitted to it. **False-negative path:** it often cannot, from the change alone — the
   same edit can be principled or per-case depending only on the reasoning behind it, which is not in
   the diff. What distinguishes them is a **written prediction made before measuring**, naming the
   population the change should move and the direction, so that a change which fixes its motivating
   case and moves nothing else is visibly a per-case fit. That is the Premise Gate's clause (b)
   (**D-180**) doing exactly the work it exists for, and this statement's enforceability rests on it.
6. **What would falsify it.** **Observable:** the record accompanying each factor and value.
   **Decision rule:** a factor or value whose record names a passage as its ground, with no
   pre-registered prediction over a population, violates S33. **Not falsified by:** a passage being
   named as the case that *surfaced* a question.

---

### 1.8 What the scoring model must publish

---

**S34 — The model publishes, for every stretch, the ranked alternatives and the margin, not the
winner alone.**

1. **Statement.** Committing to a winner does not discharge the model's output obligation. The
   alternatives it considered, their scores, and the winner's margin over the best alternative are
   published on the model's output surface.
2. **Defense.** SALVAGED (**D-027**): every layer emits ranked candidates plus a confidence, never a
   forced point estimate. SALVAGED (**D-099**): negative evidence is information — a ruled-out reading
   is carried at low confidence rather than discarded, unless the exclusion is recomputable from what
   is kept. SALVAGED (**D-100**): every derived fact is published exactly once on the producing layer's
   surface, and consumers read rather than re-derive. THEORY, and this is the reason specific to *this*
   model: S18's independence premise can only be checked by calibration, and calibration is a
   measurement over the margins, not over the winners. **A model that publishes only its winners
   cannot be checked for the one defect its own form is most prone to.** FACT (exemplars): the
   published human analyses do this themselves — `Chorales/001/analysis.txt` and
   `Chorales/003/analysis.txt` carry alternative readings as explicit `var1` lines beside their primary
   ones, so the practice of recording a second reading is the annotators' own, not an invention here.
3. **Source class.** salvaged, with a derived defense specific to this model.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the alternatives are worth their cost to carry.
   **False-negative path:** the alternative list can be arbitrarily long, and a list truncated at some
   count silently changes what the margin means (S30's own limit). Publishing "the alternatives" is
   therefore under-specified until the truncation rule is stated, and the honest form carries both the
   list and **the rule by which it was truncated**. This statement does not fix that rule.
6. **What would falsify it.** **Observable:** the model's output surface for one stretch.
   **Decision rule:** if it carries a committed reading and no alternative with a score, S34 is
   violated. **Not falsified by:** the alternative list being short where few candidates were
   admissible.

---

**S35 — The model must be able to report that no candidate explains a stretch well, and that report
is distinct from reporting a narrow margin.**

1. **Statement.** Two different states must be separately reportable: *the model is unsure which
   reading is right* (several candidates score similarly), and *the model has no good reading at all*
   (the best candidate explains the music badly). They are independent — a stretch can have a clear
   winner that is a poor explanation, and a stretch can have two excellent readings that tie.
2. **Defense.** THEORY: the two states have different causes and call for different responses. A narrow
   margin means the evidence is genuinely balanced, and the response is to carry both readings forward
   for a later layer with more evidence to select from (S34). A uniformly poor fit means the candidate
   space is wrong for this music — an admissible chord is missing, or the passage is not tonal, or the
   segmentation is wrong at a larger level — and the response is to surface it, not to commit to the
   least bad member. THEORY: this is the property S13(iii) is chosen for. A ranking margin **cannot**
   express the second state, because it is a comparison between candidates and says nothing about how
   any of them stands against the music; an absolute likelihood can. SALVAGED (**D-029**): where
   theory is sound but unverifiable against the corpus, build it with an explicit alternative-confidence
   path and an unvalidated mark rather than refusing it — the shape this second report takes.
3. **Source class.** derived, corroborated by salvage.
4. **Status.** settled as to the requirement. **Open** as to the form of the absolute report, because
   S30 forbids a threshold on the raw score and no substitute is derived here.
5. **Premise, and its false-negative path.** Premise: an absolute fit report is constructible without
   violating S30. **False-negative path:** the obvious construction — comparing the winner's likelihood
   against a fixed number — is exactly what S30 forbids, and the two statements are in tension. The
   resolution has to be a quantity normalized by something intrinsic to the stretch, such as a
   comparison against the likelihood of the same music under a deliberately uninformative reference
   model over the same observations. That is a **candidate** resolution, it is not derived here, and
   naming it is not adopting it. **This tension is the second-largest open question in this
   derivation** and §2 carries it.
6. **What would falsify it.** **Observable:** the model's output for a stretch of atonal or
   non-triadic music. **Decision rule:** if the model's report is indistinguishable from its report on
   a clear, well-fitting triad except in the margin, S35 is unmet. **Not falsified by:** the model
   still naming a best candidate for such a stretch, provided the poor-fit report accompanies it.

---

**S36 — Every published quantity states which of two kinds it is — a ranking margin or a calibrated
probability — and no layer may claim the second until it has been calibrated against held-out data.**

1. **Statement.** A confidence leaving this model is labelled as a margin or as a calibrated
   probability, is in the unit interval, and names the decision it belongs to. The calibrated label is
   a claim about measured behaviour and may not be applied to an uncalibrated quantity however
   probability-like its arithmetic.
2. **Defense.** SALVAGED (**D-032**): every confidence crossing a layer boundary is bounded,
   class-declared as a ranking margin or a calibrated probability, and stated to its decision.
   THEORY, specific to this model: S13 makes the arithmetic probabilistic, which makes it *look*
   calibrated, and S18's independence violation makes it systematically over-confident (S18 field 5).
   **So this model is precisely the kind whose numbers most invite the calibrated label and least
   deserve it by default.** SALVAGED (**D-182**, principle #19): positively established, never merely
   unfalsified.
3. **Source class.** salvaged, with a derived defense specific to this model.
4. **Status.** settled.
5. **Premise, and its false-negative path.** Premise: the two classes are distinguishable by a
   measurement. **False-negative path:** calibration is measured per decision axis and per population,
   so a quantity calibrated on chorales is not thereby calibrated on the orchestral repertoire
   **D-201** requires the system to handle — and the label, once attached, travels with the number.
   The class label must therefore carry the population it was calibrated on, or it will be read as a
   general claim.
6. **What would falsify it.** **Observable:** each published confidence's declared class.
   **Decision rule:** a quantity published as a calibrated probability with no held-out calibration
   measurement behind it violates S36. **Not falsified by:** a margin being published without
   calibration — that is what a margin is.

---

## 2. Open questions

Written as questions, not filled with the most plausible reading. Each names what would settle it.
The three marked **★** are the ones this session would put to the user for a ruling; the others are
work, not rulings.

1. **★ How is the ornament model to be grounded, when no available annotation records per-tone
   roles?** (S25, S7.) The scored object includes a role assignment; the annotations record only chord
   labels. Either a source of per-tone role annotation is found or made, or the ornament model's values
   are declared from theory and carried unvalidated indefinitely. **The ruling asked for:** which of
   those two, and — if the second — what standing an unvalidated ornament model has when the chord
   labels it produces are graded as though established.

2. **★ What controls how many stretches a reading has?** (S29, S15.) The requirement that a boundary
   term be declared is settled; its form is not, and the two candidate forms — a duration prior over
   chords, and a metric-position prior over boundaries — are hard to distinguish empirically and imply
   different things about repertoire with unusual note values or tempi. **The ruling asked for:** which
   form is designed first, given that the choice cannot be made on measurement alone until a corpus of
   more than one style is graded.

3. **★ How can a "no candidate fits this music" report be made without a threshold on a raw score?**
   (S35, S30.) These two statements are in tension and the tension is not resolved here. A comparison
   against an uninformative reference model over the same observations is named as a candidate
   resolution and is not adopted. **The ruling asked for:** whether a reference-model comparison is the
   route, or whether the absolute report is deferred and the model ships able to express only relative
   uncertainty.

4. **What is the capacity budget, and which of the per-factor separations survive it?** (S23, S5, S6,
   S11.) Settled by knowing the effective sample size of the fitting corpus and running the fit under a
   declared budget. Note that the *effective* sample size, not the event count, is what is needed
   (S23 field 5), and this session has no route to either.

5. **Is figured bass structural notation or analytical notation for the purpose of S31?** Settled by a
   decision per notation kind, not by this document.

6. **What is the rule for "the bass of this stretch" when the lowest sounding tone changes inside it?**
   (S8 field 5.) The published state of the art carries both a first-event and an overall variant
   rather than choosing. Settled by deriving the rule from what the bass is evidence *for* — inversion
   — rather than by measuring which variant scores better.

7. **Is the duration weight linear in sounding time?** (S10 field 5.) Assumed by every published model
   examined here and tested by none. Settled by fitting a non-linear weight and comparing on held-out
   data under S24.

8. **Does the strength of the vertical fit genuinely depend on what preceded the stretch?** (S12
   field 5.) If it does, the strict separation of fit terms from transition terms cannot express it.
   Settled by measurement, and worth stating in advance so that a later design that needs the
   interaction declares it rather than reintroducing it inside the fit term.

9. **What is the truncation rule for the published alternative list?** (S34 field 5.) Under-specified
   here; it changes what a margin means, so it interacts with S30 and S36.

10. **How is the reliability of a source's notated spelling represented?** (S9 field 5.) Sources that
    have passed through transposition, reduction or machine translation may carry spellings no musician
    chose, and the exemplars contain such a source. Settled by a per-source declaration, whose form is
    not derived here.

11. **Is the decomposition in §2 of the brief complete?** The brief invites the session to find its
    list of faces incomplete. **One face is missing from it:** *what the scoring model must publish*
    — the output obligation, which §1.8 derives and which the brief's seven faces do not name. It is
    not a presentational detail: S34's requirement follows from S18's independence premise being
    checkable only through the margins, so the output surface is load-bearing for the model's own
    establishment.

---

## 3. The sizing record

Every figure below was measured by the session on itself, from timestamps taken as the work went.
**No figure here is estimated, and no share is given without its denominator.** Where a measurement
was not taken at the granularity the brief asks for, that is stated rather than reconstructed.

### 3.1 The measurement that was not taken at the granularity asked for

The brief asks for **the time spent per statement**. Timestamps were taken at **batch boundaries**,
not at each statement, so the per-statement figure below is a **batch mean** and not a per-statement
measurement. This is reported as a shortfall against the brief, not presented as what was asked for.
A later deriving session that wants per-statement times must take a timestamp per statement.

**A caveat on what this session's clock measures.** The deriving side is a model session, so the
elapsed time is the wall-clock of generation. It is a real cost and it is what this pilot can
measure, but it is not the same quantity as a human analyst's time on the same work, and a budget
set from it should say which of the two it is budgeting.

### 3.2 The timings, as measured (all times UTC, 2026-08-24)

| Boundary | Time | Elapsed |
|---|---|---|
| Session start; first read of the brief | 22:10:28 | — |
| Stop-on-meeting event recorded (§5.2) | 22:12:43 | 2 min 15 s from start |
| Reading complete; first statement begun | 22:27:58 | **17 min 30 s reading** |
| Statements S1–S12 written (12 statements) | 22:31:01 | 3 min 03 s |
| Statements S13–S21 written (9 statements) | 22:33:06 | 2 min 05 s |
| Statements S22–S30 written (9 statements) | 22:34:55 | 1 min 49 s |
| Statements S31–S36 + the open questions (6 statements) | 22:36:26 | 1 min 31 s |

- **Reading before the first statement: 1,050 s (17 min 30 s).**
- **Writing the 36 statements: 508 s (8 min 28 s).**
- **Ratio of reading to writing: 2.07 : 1.**
- **Batch mean over the three statement-only batches (S1–S30, 30 statements, 417 s): 13.9 s per
  statement.** The fourth batch is excluded from that mean because it also carried the eleven open
  questions, so its elapsed time is not attributable to its six statements alone.
- **Whole-file figure including the fourth batch and its open questions: 508 s / 36 statements =
  14.1 s per statement**, which double-counts the open-question time into the statements and is
  given only because it is the figure the brief's wording names.

### 3.3 The counts and the shares, each with its denominator

| Quantity | Count | Denominator | Share |
|---|---|---|---|
| Statements written | 36 | — | — |
| Statements whose status is *open* (wholly or in a named part) | 5 | 36 | 13.9 % |
| Statements the session would put to the user for a ruling | 3 | 36 | 8.3 % |
| Statements whose sixth field could not be written (UNVERIFIABLE) | **0** | 36 | 0 % |
| Statements resting in whole or in part on a *measured* source class, value UNESTABLISHED | 3 | 36 | 8.3 % |
| Statements whose primary source class is *derived* | 29 | 36 | 80.6 % |
| Statements whose primary source class is *salvaged* | 7 | 36 | 19.4 % |
| Open questions recorded | 11 | — | — |
| Open questions the session would put to the user for a ruling | 3 | 11 | 27.3 % |

The five statements whose status is *open*: **S4** (open as to a rate, settled as to the
requirement), **S23** (settled as a requirement, open as to what the budget permits), **S25**
(open), **S29** (open as to the term's form, settled as to its being declared), **S35** (open as to
the form of the absolute report, settled as to the requirement).

The three statements carrying a question the session would put to the user: **S25**, **S29**,
**S35** — the three questions marked ★ in §2, and the question each would ask is written there.

The three statements resting in part on a *measured* source class, with no value stated: **S4**
(the share of two-reading disagreements attributable to boundary placement), **S14** (whether the
probabilistic form measures more accurately on this project's data), **S25** (how far the
per-tone-role annotation gap extends beyond the five exemplar files).

**The format test named in the brief.** The brief states that five statements will be sampled for
the form, and that the sample will include a probabilistic factor form and a conditional-independence
premise. Both kinds arose from the subject and are written: the probabilistic factor form is
**S13** (with **S17** as its combination rule and **S14** as the bar on what may be claimed for it),
and the conditional-independence premise is **S18** (with **S19** as the known violation and **S20**
as the declared repair). Neither was manufactured to satisfy the paragraph; each is where the
derivation arrived.

### 3.4 The noise measurement — which sources each statement actually used

**Boot-pack files consulted by at least one statement (3 of the 7 files in the pack):**

| Pack file | Statements it contributed to | Count |
|---|---|---|
| `05_the_ratified_design_intent.md` | S2, S3, S9, S12, S14, S16, S18, S20, S22, S24, S25, S26, S27, S30, S31, S32, S33, S34, S35, S36 | 20 |
| `02_the_guiding_principles_and_the_conventions.md` | S14, S20, S21, S23, S24, S32, S33, S36 | 8 |
| `06_the_defect_type_catalog.md` | S6, S11, S13, S16, S17, S25, S30, S33 | 8 |

**Boot-pack files consulted by NO statement (4 of the 7):**

| Pack file | What it was used for instead |
|---|---|
| `00_READ_THIS_FIRST.md` | The reading order and the boundary. No content reached a statement. |
| `01_the_phase_definitions.md` | Established what a deriving session may and may not do. No content reached a statement. |
| `03_the_writing_standards.md` | Governed the **form** of this document — the §0 terms table, qualified predicates, plain vocabulary, the status banner, the reserved-word convention. No content reached a statement. |
| `04_the_dispatch_protocol.md` | Read whole. It governs how dispatches, reports and ruling records are written and sequenced. **Nothing in it bears on the subject**, and no statement uses it. It is the largest pack file after the design intent and it contributed nothing to this derivation's content. |

*Recorded because it is a sizing fact and not a complaint:* `04_the_dispatch_protocol.md` and
`01_the_phase_definitions.md` together are a substantial share of the pack's reading and produced no
statement. A later pack for a subject of this kind could test whether the deriving session needs them
at all, or needs only the clauses that bind a deriving session's own conduct.

**Fetched research consulted, by statement:**

| Source | Fetched | Statements | Count |
|---|---|---|---|
| Masada & Bunescu 2018, *Chord Recognition in Symbolic Music: A Segmental CRF Model* (arXiv 1810.10002) | yes — **two independent extraction passes, cross-checked, in agreement** | S3, S5, S6, S7, S8, S10, S11, S12, S13, S15, S28, S29 | 12 |
| Pardo & Birmingham 2002, *Algorithms for Chordal Analysis*, Computer Music Journal 26(2) | yes — **two independent extraction passes, cross-checked, in agreement** | S2, S3, S5, S7, S10, S13, S17, S21 | 8 |
| Temperley 2002, *A Bayesian Approach to Key-Finding* | yes — one pass | S9, S12, S13, S14, S18, S19, S29 | 7 |
| Temperley 2000, *The Line of Fifths* | yes — one pass | S9 | 1 |
| Casacuberta, review of Temperley's *Music and Probability* (MTO 16.2) | yes — one pass | **none** | 0 |

**Sources that could NOT be fetched. No statement rests on either; the gap is stated, not filled.**

| Source | Why not fetched | What it would have borne on |
|---|---|---|
| Gotham et al., *When in Rome: A Meta-corpus of Functional Harmony* (TISMIR) | the fetch of the redirected file was refused (permission not answered in time) | S4 and S25 — what the corpus itself says about alternative readings, the `var` convention, and whether annotator variance is measured. **S4's rate claim is left UNESTABLISHED partly for this reason.** |
| *Non-chord Tone Identification Using Deep Neural Networks* (DLfM 2017) | the host returned HTTP 429 | S7 and S25 — which features identify ornaments, and what accuracy is reachable. **The ornament model in S7 therefore rests on theory and on the figuration heuristics reported in the Masada & Bunescu paper, and on no dedicated source.** |

**Exemplars consulted, by statement:**

| Exemplar file | Statements | Count |
|---|---|---|
| `Chorales/003/analysis.txt` (When in Rome; analyst Andrew Jones) | S1, S4, S25, S34 | 4 |
| `Chorales/001/analysis.txt` (When in Rome; analyst Andrew Jones) | S4, S25, S34 | 3 |
| `Chorales/001/analysis_BCMH.txt` | S4, S9, S25 | 3 |
| `Chorales/003/analysis_BCMH.txt` | S4, S9, S25 | 3 |
| `003 Ach Gott, vom Himmel sieh darein.mscx` — the notes, bar 4 | S1, S11 | 2 |
| `Chorales/134/analysis.txt` (When in Rome; analyst Dmitri Tymoczko) | S25 | **1** |

**Exemplars staged to the session and NOT opened:** the score files
`001 Aus meines Herzens Grunde.mscx` and `137 Du, o schönes Weltgebäude.mscx` were named by the
brief and were **not** opened — the desk trace was run at one score only. Chorale 134's analysis was
opened and used in exactly one statement. *Recorded as a sizing fact:* the derivation needed the
**paired** annotations (two readings of one work) far more than it needed the third work, and it
needed the notes of exactly one bar of one score. A later pack sizing this kind of unit could weight
toward more paired annotations rather than more works.

---

## 4. The self-check

Run over this document before it was reported, against the guiding principles, the conventions and
the defect-type catalog carried in the boot pack.

- **#1 / #2 (fact and theory based; specific research over general).** Every load-bearing claim
  carries FACT, THEORY or CONJECTURE. Four sources were fetched and read; the two central ones were
  extracted twice independently and cross-checked, and the agreement is recorded at §3.4. Two sources
  could not be fetched and **no claim is carried out of either** (§3.4).
- **#6 (one path per concern).** Each statement states one rule once. Where two statements bear on
  one another they cross-reference rather than restate — S7 and S27, S15 and S29, S30 and S35,
  S18 and S36.
- **#12 (no information loss).** Excluded alternatives are recorded with the statements that exclude
  them, not dropped: Pardo & Birmingham's `S = P − (M + N)` at S13 and S17, the lexicographic
  combination at S17, the aggregate chord-tone count at S5, the filter-then-score design at S7 and
  S27. Corrections made while writing are recorded in place rather than smoothed away — S28's
  exactly-once condition is stated over sounding time **after** the naive event-level form was found
  to break on the pedal tone, and that is written into the statement.
- **#17(a) (premise ledger) and #17(e) (false-negative paths).** Every statement carries field 5, and
  every field 5 names a path by which its premise could be false without showing. **No field 5 is a
  restatement of the statement.**
- **#17(f) / D-431 (no hand-transcribed figures).** Figures quoted from fetched papers are the
  papers' own published values, cited to the paper — they are not measurements of this project.
  **No figure of this project's own is stated anywhere in this document**, and no count over the
  exemplars is given (S4 field 2 says so in terms). The sizing record's figures are this session's
  measurements of itself, taken from timestamps recorded as the work went.
- **#19 (nothing trusted merely unfalsified).** S14 exists to stop the probabilistic form being
  claimed as more accurate on no measurement; S20 requires the identity-weight arm; S36 forbids the
  calibrated label without calibration.
- **#24 (every figure carries its uncertainty).** No difference between two measured quantities is
  asserted anywhere in this document. Where a difference would have been the natural claim — S4's
  rate — it is left UNESTABLISHED with the measurement it needs named.
- **Conventions — reserved words.** The bare word *score* is used for the music throughout; the
  numerical sense is always *candidate score*. The bare word *key* is not used at all for a lookup;
  *tonality* is used where the record's own convention would allow bare *key*. *Measure* appears
  only as the verb and as *measurement*; the metric unit is *bar*. *Note* as a remark is written
  *note* only in the phrase "prose notes", which is the analysts' own word for their own text — the
  pitch event is *tone event* throughout. *Interval* is used in the pitch sense only. *Register*,
  *mode*, *figure*, *root*, *part*, *rest*, *flat*, *instrument*, *scale*, *beat* and *resolution*
  are used in their musical senses or qualified.
- **Conventions — no self-invented labels.** The statement identifiers S1–S36 are this document's
  internal numbering and are not a project-wide scheme; they are used nowhere but here. No
  abbreviation is coined. Terms that would otherwise be jargon are defined in §0 before first use.
- **Writing standards — qualified predicates.** Checked by forcing each two-place word to name its
  argument: *fits* (by what measure — the likelihood of the observations, S13), *comparable* (within
  what — S27, S28, S30), *uncertain* (about what — S35 separates the two kinds), *established*
  (by what measurement — named per statement), *strong* / *weak evidence* (in what term).
- **The defect-type catalog.** This document names the shapes it is written against, at the
  statements where they apply: **DT-1** at S11, **DT-2** at S33, **DT-7** at S6, **DT-8** at S13,
  S17 and S30, **DT-9** at S13 and S25, **DT-14** at S16. It also reports one instance of **DT-20**
  against the session's own boot conditions, at §5.3.

**What this document does not do.** It authorizes no fix, no design, no build, no specification
edit and no measurement. It compares nothing against anything. It creates, flips and discards no
open-items row, and allocates no finding number. It commits nothing and runs nothing.

---

## 5. The independence record

### 5.1 Everything the session opened

**From the boot pack** — all six files and the read-me were opened. `05_the_ratified_design_intent.md`
was **not read to its end**; see §5.2.

**Exemplars, all staged by the brief by name:** `Chorales/001/analysis.txt`,
`Chorales/001/analysis_BCMH.txt`, `Chorales/003/analysis.txt`, `Chorales/003/analysis_BCMH.txt`,
`Chorales/134/analysis.txt`, and the score `003 Ach Gott, vom Himmel sieh darein.mscx`. The two other
staged scores were **not opened** (§3.4).

**Fetched sources, by citation:** Masada & Bunescu 2018 (arXiv 1810.10002); Pardo & Birmingham 2002
(*Computer Music Journal* 26(2), obtained from the authors' own copy); Temperley 2002, *A Bayesian
Approach to Key-Finding*; Temperley 2000, *The Line of Fifths*; Casacuberta's review of *Music and
Probability* (*Music Theory Online* 16.2). Two further sources could not be fetched and are named
with the gap they leave at §3.4.

**Nothing else inside the repository was opened.** No specification, no code, no register, no
handoff, no dispatch, no report, no status surface. No branch rule was taken, no commit log read,
nothing was run over the corpus.

### 5.2 The stop-on-meeting event

**Where.** `tools/audit/derivation_boot_pack/scoring-model/05_the_ratified_design_intent.md`, at the
entry **D-220**, continuing into **D-221**. Recorded at 22:12:43 UTC.

**How much was seen before stopping.** Entries **D-001 through D-219 in full**; **D-220 in full**;
**D-221's decision text partially** — the first two lines of its quoted block. Reading of that file
stopped there, at approximately line 619 of 4,307. **The remainder of the file — the entries after
D-221 — was not read.**

**Why it fired.** D-220 and D-221 state, in code-level terms and naming code identifiers, how a guard
and a bonus behave in this project's chord scoring. That is a statement about how this project's
analysis currently scores a candidate reading, which is the subject the brief's stop clause names.
The call was not obvious — the file is the pack's *design-intent* member and the brief names it as
this session's salvage source — and it was made on the ground that these two entries describe a
mechanism as built rather than stating an intent. **Nothing seen at D-220 or D-221 was used,
paraphrased or reasoned from anywhere in this document**, and no statement above cites either.

**A second exposure inside the same file, caused by the session itself and recorded because an
unrecorded one is the failure.** Before reading the file's body, the session listed **all 241 entry
headings** — identifier and title — in order to navigate a 4,307-line file. That listing therefore
put in front of the session the **titles** of every entry beyond the stop point, several of which
name scoring decisions. **No title beyond D-221 was used in any statement**, and no statement cites
an identifier above D-221. The exposure is nonetheless real and is reported rather than argued away:
a title is a compressed statement, and a later session navigating a large pack file should be told
whether a heading scan is permitted before the body is read. **This session's own judgment is that
it should not be, and that the pack should carry its own table of contents so the question does not
arise.**

### 5.3 A larger contamination the session did not choose, reported in full

**This is the most important item in this record and it is not a stop-on-meeting event, because the
session never opened anything to meet it.**

This session's boot carried, automatically and before the brief was read, the project's standing
instruction file `CLAUDE.md` in full, as part of the session's own system context. That file is not
in the boot pack — the pack's own copy of the principles and conventions (member `02`) is **cut**,
and the cut removed exactly the material described below. The uncut file the session was given
carries, among other things:

- a section stating gate thresholds by name and value, and naming a retired gate;
- a block on preset scoring caps stating which scoring constant is set on which code path, the
  default it inherits, whether the cap currently binds, and the individual bonus values behind one
  preset's behaviour;
- a section on the scoring-model document, its synchronisation rule, the template-count model, and
  the named steps for adding a template;
- named scoring terms and guards, described by their code identifiers and by what they test;
- the ratified measurement baselines and the grading conventions the analysis is measured under.

**What the session did with it.** Nothing. No statement above uses any of it; no threshold, constant,
identifier, guard, term name, baseline or figure from it appears anywhere in this document; and the
derivation's factor structure was built from the fetched literature, from music theory and from the
exemplars, which is where every FACT above is cited. **But "it was not used" is exactly the defence
this project's own never-work-from-memory rule rejects** — correct memory is indistinguishable from
incorrect memory without checking, and unused knowledge is indistinguishable from used knowledge
without a check nobody can run. **The honest statement is therefore: this session was not blind in
the sense the brief intends, and its independence cannot be established by its own assurance.**

**Why it matters to the pilot specifically.** The unit this pilot sizes is a derivation of the
scoring model, and the material above is about the scoring model. The contamination is not incidental
to this subject; it is aimed at it. **A comparison of this output against the project's current
specification will therefore over-state the agreement by an unknown amount**, and no part of that
agreement may be read as independent corroboration.

**What it is, by name.** This is the shape the boot pack's defect catalog names **DT-20** —
*self-defeating instruction composition: an instruction (or protocol application) whose mandatory
preconditions defeat one of its own requirements, e.g. a required session-start read that leaks
exactly what a blinding requirement withholds.* The catalog's own example is this case. The pack was
cut correctly; the leak is upstream of the pack, in what a session of this kind is given before it
reads anything.

**What would close it, stated because naming a defect without a route is half a finding.** A
deriving session for a blinded subject would have to boot without the project's standing instruction
file in its context — for example from a working directory that carries only the brief, the pack and
the staged exemplars. Whether that is available on this side is not something this session can
determine, and it is not proposing a mechanism; it is stating the condition that would have to hold.

### 5.4 The positive statements the record owes

- Apart from §5.2 and §5.3, **no passage in the brief or in the pack was met that states how this
  project's analysis currently scores a candidate reading.**
- **No file outside those named in §5.1 was opened.**
- **No measurement was built, scoped or run**, over the exemplars or over anything else. No count
  over the three chorales appears in this document.
- **The exemplars were treated as exemplars.** Where a rate would have been the natural claim, it is
  written as UNESTABLISHED with the measurement it needs (S4, S25).

---

## 6. What this document is not

It is a first derivation of one subject by one session, blind in intent and — by §5.3 — not blind in
fact. It has been compared against nothing. It is not a specification, it is not ratified, and no
part of it binds anything. Its three ★ questions are unanswered, and its largest one (S25 — that the
ornament model the derivation requires has no ground truth in the annotations available) may
reasonably change the shape of the answer rather than being settled inside it.
