# The COMPARISON — the blind derivation's statements graded at the oracle and at the current text

> **STATUS: READING FILE — a tabulation delivered to the user. It recommends nothing, establishes
> nothing, and rules on nothing.** Prepared by Claude Code, 2026-08-24, under
> `cc_instruction_comparison_harmony_boundary.md` Task 1, executing Rulings 1–4 and §5 of
> `cowork_rulings_2026_08_24_comparison_design_sitting.md`, under Ruling 4(c) of
> `cowork_rulings_2026_08_21_successor_plan_sitting.md`.
>
> **What the user is asked to rule here: NOTHING.** The ruling on the derivation method comes
> separately, framed by the writing side over this tabulation (Ruling 4 of the comparison-design
> sitting). Nothing below is a recommendation about that ruling, and nothing below is a verdict on
> whether the blind session was blind.
>
> **Manifest of this file's own population, counted at the graded file by this session** — the
> graded file is `cowork_blind_derivation_harmony_boundary_2026_08_23.md` (in git at
> `95c17e6660`, blob `49d92ccb14614ba71ee755d4917cdfc14e370222`): **26 statements** (§3.1–§3.6,
> numbered 1–26) and **10 open questions** (§4, numbered 1–10). These counts were taken at the
> file's own structure and are the counts of record for this comparison; the deriving session had
> relayed the same two counts, and this session re-counted rather than carrying them.

---

## 1. The words used here, explained before they are used

- **The analysis** — the harmonic-analysis software this project builds: given a notated score it
  decides the tonality, the chords, and the moments at which one chord gives way to the next.
- **The blind output** — the file named in the manifest above: 26 statements and 10 open questions
  written by an implementation-blind session that read a curated boot pack, three staged Bach
  chorales with their published human analyses, and six fetched research sources, and nothing else
  in this repository.
- **The oracle** — the user-ratified answer that was deliberately withheld from that session, so
  that what the session derived could be compared against an answer it had not seen. It has two
  arms, quoted at §2 below.
- **The untrusted sources** — this project's current specifications and its current code. Under the
  ruled phase definitions these are **evidence about the present text and never authority over a
  statement**: a disagreement between a statement and the current text is recorded, never resolved.
- **Salvage** — the blind output's own source class for a statement it took from a ruled
  design-intent entry inside its boot pack, cited by that entry's identifier.
- **Chord-span** — a maximal stretch of the score reported as governed by one chord. The blind
  output's own term, kept here.
- **Boundary** — the moment at which one chord-span ends and the next begins. The subject.
- **Partition point** — a moment at which the set of sounding notes changes because at least one
  note starts or at least one note stops. The fetched Pardo–Birmingham paper's term, used by the
  blind output in that sense.
- **Event lattice** — the production decoder's own name for the ordered stretches between
  consecutive notated onsets and offsets that carry at least one sounding note.

## 2. The subject, and the oracle at its two arms

### 2.1 The subject, stated from scratch

Music does not announce its own harmonic boundaries. Something has to decide that one chord is
sounding from here to there and a different one from there onward, and something has to decide
which evidence is allowed to settle that, and in what order when two kinds of evidence disagree.
**How should a harmonic analysis of a notated score decide the moment at which one chord ends and
the next begins, and what evidence should decide it?** That is the question the blind session was
asked, and the question this file grades its answers against.

### 2.2 The oracle's FIRST arm — the evidence-ranking ruling

Located at its own heading text in `ARCHITECTURE.md`, the section
*"The evidential priority the emission is scored under — ACTUAL SOUNDING NOTES ARE THE STRONGEST
EVIDENCE, and the ranking is ARM-INDEPENDENT"*, ruled by the user 2026-08-11. Quoted:

> **THE RANKING, and it binds THIS ARM as it binds the legacy one.** In descending strength:
> **actual sounding notes** — what is literally happening now; **temporal context** — the
> surrounding measures; **the notated key signature**; **the declared major/minor tag**, weakest of
> the four. It is a CROSS-CUTTING EVIDENTIAL RULE about what the analysis may treat as evidence and
> in what order, not a property of either implementation […]

> **WHAT IT MEANS FOR THE EMISSION, which is where the ranking actually bites.** A note that is
> already sounding is a constituent of the sonority. Whether it belongs to the chord is what the
> emission's chord-member and non-chord-tone categories are for — it is not settled by whether the
> note happened to be struck at this event.

And the second of the two grounds the same section gives for the ranking being arm-independent:

> **(2) The Layer-2 slice identity**, which states the same doctrine one layer down and without
> reference to any arm: slice boundaries are every onset **and every release**, and *slice identity
> is the eligible sounding-note set*.

The legacy statement of the same ranking is the priority-of-evidence table in `ARCHITECTURE.md`
§5.2, which the section above names as standing exactly as written (register entry **D-057**):

> | Priority | Source | Description |
> |---|---|---|
> | Strongest | Actual sounding notes | what is literally happening now |
> | Strong | Temporal context | surrounding measures |
> | Weak | Notated key signature | `keySignatureFifths` (circle of fifths position) |
> | Weakest | `KeyMode` enum | explicit major/minor tag (rare, only when user sets it) |

### 2.3 The oracle's SECOND arm — the five recorded corpus traces

Located by its own text in `cowork_joint_estimator_factorization.md` §6, form (b). Quoted whole:

> **(b) Single-piece traces on 3–5 real corpus cases from the known failing sets** (the #17c form:
> FIRST "does the mechanism fire?", THEN "which term moves, by how much?"), proposed:
> `bwv145.5@12960` (the altered-region chord flip the OI-168 fix corrected — the new structure must
> get it without the fix's special form), `bwv352@1440` (the share-tone Am6 vs F♯ø7 case — spelling
> and bass factors must carry it), `bwv10.7@36000` (the segmentation over-grab — the boundary
> factor's test), one relative-major/minor key-failure case drawn from the key-local residual, and
> one genuinely modal chorale (prior + emission variants). The traces are run on paper against the
> specification BEFORE any code exists; a surprise at this stage is cheap and is the point.

**This arm is engaged only where a statement touches a factor of the ratified factorization**, and
every row below says whether it is engaged. The ten ratified factors are the pitch emission, the
spelling emission, the bass/inversion factor, the same-key chord transition, the key transition,
the entry chord at a key change, the segmentation/boundary factor, the fermata, the cadence factor
and the signature/declared-mode prior (`cowork_joint_estimator_factorization.md` §3).

## 3. The grading vocabulary, and that it is CLOSED

Ruling 3 of the comparison-design sitting fixes two axes and the whole verdict language. **No other
verdict word exists, and no numeric grade is given anywhere in this file.**

**Against the oracle — exactly one per statement:**

- **MATCHES** — reproduces the ruled intent in substance.
- **DEFENDED ALTERNATIVE** — differs, with a defense the record cannot dismiss.
- **SILENT** — the oracle does not speak to it.
- **CONTRADICTS, UNDEFENDED**.
- **UNGRADED** — a verdict this session cannot defend in one sentence at the two texts; the row
  then says what was read.

**Against the untrusted sources — exactly one per statement, separately:**

- **AGREES / DIFFERS / THE TEXT IS SILENT**, each with its specification or code location cited.
  **This axis is evidence about the present text and never a verdict on the statement.**

**How the oracle axis was applied, stated so every row is re-gradeable.** A verdict other than
SILENT is recorded only where the oracle's own text makes a claim that the statement reproduces,
departs from, or contradicts. Where the oracle's text is engaged by the statement's subject without
making a claim about it — the second arm naming a corpus case, for instance — the row records
SILENT and says what the arm names. Every row carries the statement's own words beside the oracle's
so that any verdict here can be re-taken at the two texts.

## 4. The caveats that bind this tabulation

- **The D-450/D-575 caveat (Ruling 1 of the withheld-family sitting, restated at §5 of the
  comparison-design sitting).** Two withheld entries — the initial-state signature prior and the
  Baroque partial-signature convention — were withheld on a reading of the withholding test wider
  than its words. **Where a statement cites the notated key signature as boundary evidence, the row
  applies the caveat in terms and is NOT graded CONTRADICTS for that citation.** *Applied and
  recorded: the caveat's own trigger is met on no row of this tabulation.* One statement cites the
  notated key signature (Statement 16) and it **denies** that the signature is a boundary cue rather
  than asserting it, so no row was reached by the caveat. It is recorded as considered rather than
  passed over.
- **Salvage is visible, not penalized.** A statement whose source class is salvage carries its cited
  identifier in its row, and its content is graded exactly as any other statement's.
- **The comparison is TEXTUAL.** No measurement of the analysis was built, designed, scoped or run
  for it. The three ruled score-and-analysis pairs were available to be opened and cited where a
  statement's own text names them; nothing was run over them, and no row below required opening one.
- **Neutral framing.** This file grades. It neither refutes nor confirms, and it makes no
  recommendation of any kind.

## 5. The tabulation — one row per statement, in the blind output's own order

### 5.1 The grain — where the question may be asked at all

---

**Row 1 — Statement 1 (the grain is the minimal stretch).**

*The statement.* The atomic grain of the boundary question is the minimal stretch between two
consecutive partition points; a boundary may be committed only at a partition point; the grain is
fixed by the notation's onsets and offsets, not by the bar, the beat, or a fixed sub-beat sampling
grid. **Defense class:** FACT (Pardo & Birmingham's partition-point definition; Masada & Bunescu's
candidate boundaries at all onsets and offsets; the staged annotations' half-beat changes) plus
THEORY (nothing observable changes inside a minimal stretch). **Source class:** derived.

*The oracle.* Arm one speaks, through the second of the two grounds it gives for itself: *"slice
boundaries are every onset **and every release**, and slice identity is the eligible sounding-note
set."* Arm two is ENGAGED (the statement touches the segmentation/boundary factor) and names
`bwv10.7@36000` as "the segmentation over-grab — the boundary factor's test" without stating a
grain rule.

*Oracle axis:* **MATCHES** — the oracle's own ground states boundaries at every onset and every
release, which is the statement's partition-point grain.

*Current-text axis:* **DIFFERS**, and the difference is between the two layers rather than between
the statement and the record as a whole. `ARCHITECTURE.md` §3.3's Layer-2 module table states the
statement's rule exactly — *"Boundaries = the sorted-unique union of every onset AND every release of
the eligible notes; consecutive boundaries form the slices"* — and `slicer.cpp` takes those from
`model.notes()`, the TIE-RESOLVED note events, so a notated tie point inside a held chain is not a
slice boundary there. The production joint arm does not use that surface: `buildAdapterFacts` in
`src/composing/analysis/joint/jointfactadapter.cpp` builds its event lattice from
`model.notatedNotes()`, the TIE-UNRESOLVED atoms, whose own header states that *"EVERY notated note
is published — tie STARTS and tie CONTINUATIONS alike — with its OWN notated span"*
(`src/composing/analysis/notemodel/note_model.h`). Each atom contributes its own onset and its own
release to the boundary set, so a notated tie point — a moment at which no note starts and none stops,
and therefore not a partition point in the statement's own sense — is an event boundary in that
lattice, and `decodePiece` may commit a chord-span boundary there. The statement's own near-miss
clause does not reach this, because it excuses evaluating a superset of positions only where a
boundary can never be COMMITTED off a partition point. Everything else in the statement holds at both
layers: the lattice's own comment reads *"minimal segments between consecutive notated
onsets/offsets with >=1 sounding note (the Pardo & Birmingham partition)"*, and no bar, beat or fixed
sub-beat grid enters either construction.

---

**Row 2 — Statement 2 (no two adjacent spans carry the same label and inversion).**

*The statement.* A boundary is committed only where the sounding content changes; two adjacent
chord-spans carrying the same label and the same inversion are not two spans, and a same-label
restatement in an annotation is a representation artifact the analysis must not produce.
**Defense class:** THEORY (the degenerate case of Statement 1's undecidability argument) plus FACT
(the machine-translated BCMH reading of chorale 001 restates `I6` where the human-proofread reading
carries one span). **Source class:** derived.

*The oracle.* Arm one does not speak — it ranks evidence classes and says nothing about the shape of
the committed span sequence. Arm two is ENGAGED (the statement touches the same-key chord-transition
factor, whose self-transition cell is what would price such a pair) and names no case of this shape.

*Oracle axis:* **SILENT.**

*Current-text axis:* **DIFFERS.** In `jointdecoder.cpp`'s `decodePiece`, the same-key chord-
transition branch iterates every predecessor class carried at the boundary, the current class
included, so two adjacent committed segments with the same key and the same class are representable
and are priced by the self-transition cell rather than forbidden; the backtrack that assembles the
committed segments performs no merge. `cowork_joint_estimator_factorization.md` §5 records that
equal-content-score segmentations differing by one boundary on repeated-chord runs are real and are
resolved by a declared total order whose first term is *"fewer segments first"* — a tie-break on
exact equality, not a prohibition.

---

**Row 3 — Statement 3 (the question is asked over the sounding set, not the struck set).**

*The statement.* Every note sounding in a minimal stretch, including a note struck earlier and still
held, is evidence for the harmony of that stretch; a reading of only the struck notes is refuted.
**Defense class:** FACT (Pardo & Birmingham weight a note by the stretches it spans; Masada &
Bunescu carry a held-over marking per pitch; Temperley weights by duration; the staged 001 `m1 b2`
annotation names a chord whose fifth is a held soprano note) plus THEORY (the suspension is
definable only if held tones are part of the stretch's content). **Source class:** derived.

*The oracle.* Arm one speaks directly: *"A note that is already sounding is a constituent of the
sonority. Whether it belongs to the chord is what the emission's chord-member and non-chord-tone
categories are for — it is not settled by whether the note happened to be struck at this event."*
Arm two is ENGAGED (pitch emission and bass factors); the factorization's bass factor is specified
as *"each event's **sounding** bass judged against the segment's chord"*.

*Oracle axis:* **MATCHES.**

*Current-text axis:* **DIFFERS.** In `jointdecoder.cpp`, `Piece::prepare` assigns to each event only
the notes whose ONSET lies within it — the field is declared in `jointdecoder.h` as *"note indices
whose ONSET is in event e"* — and the content terms read that set: the pitch emission and the
spelling emission per note in `segmentContent`, the bass factor through `eventBassPc` over the same
set, and the cadence features over the approach and arrival events' sets. `ARCHITECTURE.md` names
this departure in the oracle's own section: *"the known departure — the pitch and bass emissions
reading the STRUCK set where the design says sounding — is `OPEN_ITEMS.md` OI-228, and it remains a
conformance gap DECLARED and not fixed."* Two facts are recorded here because the departure's shape
is narrower than "held tones are dropped". First, the notes the adapter publishes are the
TIE-UNRESOLVED atoms, so a tone tied across a notated boundary re-enters at the continuation atom's
own onset, flagged as a tie continuation, while a tone simply held through later events with no
notated tie is absent from every event after the one it was struck in. Second, the departure is
confined to the per-tone terms: the missing-tone term inside `segmentFeatures` reads
`Piece::overlapPcs(i, j)`, the pitch classes SOUNDING anywhere in the segment's tick span, which is
the sounding set and not the struck one — matching `ARCHITECTURE.md`'s own naming of the departure as
the *pitch and bass emissions*.

---

**Row 4 — Statement 4 (struck and held must nevertheless be distinguishable).**

*The statement.* The analysis must be able to distinguish struck from held per tone per stretch,
because a boundary is overwhelmingly opened by an onset and because held-versus-struck is a
load-bearing input to the non-chord-tone categories. **Defense class:** FACT (Masada & Bunescu's
held-over boolean exists because their features consume it; every chord change checked against the
001 score's opening bars falls at an onset, the check's narrowness routed to Open question 2) plus
THEORY (the standard definitions of suspension and passing tone are stated in those terms).
**Source class:** derived.

*The oracle.* Arm one settles what struck-ness may NOT decide — membership — and says nothing about
whether the distinction must be carried, nor that a boundary is overwhelmingly opened by an onset.
Arm two is ENGAGED (the pitch emission's covariate set) and does not reach the claim.

*Oracle axis:* **SILENT.**

*Current-text axis:* **AGREES.** The tied-over flag is carried per note and passed to the emission as
a covariate in `segmentContent` (`jointdecoder.cpp`), and `cowork_joint_estimator_factorization.md`
§3.1 lists *"tied-over preparation"* among the ratified chord-independent covariates.

---

**Row 5 — Statement 5 (a change of bass against unchanged membership is a boundary).**

*The statement.* Because the target representation distinguishes inversions, a new bass note over the
same root and quality ends the chord-span; a mere re-voicing above an unchanged bass with unchanged
membership is not a boundary. The mechanism is settled; whether a very short bass tone opens the
boundary is the ordinary non-chord-tone decision. **Defense class:** FACT (the staged 001 annotations
mark inversion-only changes as changes; Masada & Bunescu carry bass features per segment) plus
THEORY (the figured inversion is part of the chord identity). **Source class:** derived.

*The oracle.* Arm one does not speak. Arm two is ENGAGED (the bass/inversion factor) and names
`bwv352@1440`, *"the share-tone Am6 vs F♯ø7 case — spelling and bass factors must carry it"*, which
is a chord-identity case rather than an inversion-boundary case, so it does not reach the claim.

*Oracle axis:* **SILENT.**

*Current-text axis:* **AGREES.** The joint state's chord axis is `(degree class, quality, inversion)`
(`cowork_joint_estimator_factorization.md` §1), and the committed segment carries its inversion out
of the class in `decodePiece`'s backtrack (`jointdecoder.cpp`), so a change of inversion is a change
of state and therefore a segment boundary.

### 5.2 The boundary decision itself

---

**Row 6 — Statement 6 (segmentation and labeling are one decision, by exact dynamic programming).**

*The statement.* The analysis chooses the best (segmentation, labeling) pair jointly over the whole
working passage by exact dynamic programming over the minimal stretches — never segmentation first
with labels after, and never stretch-by-stretch greedy commitment. **Defense class:** FACT (Masada &
Bunescu's segmental model measures better than the stretch-by-stretch alternatives on every corpus
they test; Pardo & Birmingham measured that optimizing local per-segment candidate scores cannot
reach the answer key's segmentation; Temperley's search is dynamic programming with retroactive
revision) plus THEORY.
**Source class:** derived independently, **with D-525 and D-527 cited as salvaged corroboration.**

*The oracle.* Arm one does not speak. Arm two is ENGAGED and speaks: it assigns `bwv10.7@36000`, the
segmentation over-grab, to *"the boundary factor's test"* — that is, a segmentation error is the
business of a factor inside the one scored objective the traces are run against.

*Oracle axis:* **MATCHES** — the arm treats segmentation as decided by a factor of the same
objective as the labels, which is the statement's joint claim.

*Current-text axis:* **AGREES.** `ARCHITECTURE.md`'s governing decision at the head of the document:
*"Key, mode, and chord are inferred by ONE probabilistic decode over `(tonic, mode, chord)` with
segmentation as a modeled (semi-Markov) variable."* `decodePiece` in `jointdecoder.cpp` is an exact
block-factorized semi-Markov Viterbi over the whole event lattice with a backtrack, and the
`ARCHITECTURE.md` as-built block names it *"the event lattice + exact block-factorized semi-Markov
Viterbi decoder"*.

---

**Row 7 — Statement 7 (the boundary is decided with chord identity, inside a tonality context; the
chord-span and the tonality span are two kinds with two decisions).**

*The statement.* The fit of a candidate span is the fit of a labeled reading relative to a tonality,
not of an unlabeled span; but the chord-span boundary and the tonality boundary are two different
span kinds with two different decisions, and a chord boundary never by itself asserts a tonality
change. **Defense class:** THEORY plus FACT (Masada & Bunescu's span features are functions of the
candidate label and the span's notes together). **Source class:** derived, **with D-526, D-028 and
D-337 salvaged.**

*The oracle.* Arm one does not speak. Arm two is ENGAGED (the key-transition and entry factors) and
names *"one relative-major/minor key-failure case drawn from the key-local residual"* without
stating how the two axes relate.

*Oracle axis:* **SILENT.**

*Current-text axis:* **DIFFERS.** Two halves stand and one does not. The span typology does carry the
chord-span and the key-span as different kinds (`ARCHITECTURE.md` §2.15), and a segment boundary does
not by itself assert a key change. But the two axes are decided in ONE search over a joint `(k, c)`
state rather than by two decisions — `cowork_joint_estimator_architecture.md` §5a and
`cowork_joint_estimator_factorization.md` §1, and in `decodePiece` the same recurrence carries the
initial, same-key and key-change transitions into one candidate state — and §1 of the factorization
states that *"a key change is permitted only at a segment boundary"*, so a segment boundary is a
precondition for a tonality change.

---

**Row 8 — Statement 8 (the objective is additive over chord-spans and their adjacencies; forms from
theory, values fitted once).**

*The statement.* Per span: how well the sounding content fits the labeled chord, plus how the span
sits in the meter. Per adjacency: how plausible the chord succession is in the tonality context. The
factor forms come from theory and published models; the factor values are fitted once against
annotated music and never tuned per case. **Defense class:** FACT (the factorization is the common
core of all three fetched systems). **Source class:** derived for the factorization; **salvaged
(D-096, D-525) for the fitting discipline**; measured for every value, declared UNESTABLISHED with no
value written.

*The oracle.* Arm one does not speak. Arm two is ENGAGED (the boundary, emission and chord-transition
factors) and names a boundary factor without stating the objective's term set.

*Oracle axis:* **SILENT.**

*Current-text axis:* **AGREES, with the term set named so the reader can re-grade.** The ratified
objective is a sum over segments and boundaries of weighted factor terms
(`cowork_joint_estimator_factorization.md` §2), and forms-from-theory with values-fit-once-and-never-
per-case is the estimator's standing rule (a) in `ARCHITECTURE.md`. The ratified term set is TEN
factors, not three: the statement's *span-content fit* is carried by the pitch emission, the spelling
emission, the bass factor and the missing-tone penalty; its *metric placement* by the boundary factor
with the fermata; its *succession plausibility* by the same-key chord transition. Three further terms
fall outside its three families — the key transition and the entry chord (which the statement's own
Statement 7 defers to the tonality axis), the cadence factor, and the signature/declared-mode prior.
The shipped content terms are summed in `weightedContent` (`jointdecoder.cpp`) over emission,
spelling, bass, missing-tone and boundary. No fitted value is stated here (**D-431**).

---

**Row 9 — Statement 9 (exactly one boundary set; the spans tile; no abstention on the segmentation
axis).**

*The statement.* Every moment of the analyzed span lies in exactly one committed chord-span;
ambiguity is expressed beside the commitment, never by an uncommitted or overlapping segmentation.
**Defense class:** THEORY. **Source class:** derived, **with D-114, D-027 and D-400 salvaged**, and
D-344 and D-498 cited in its premise.

*The oracle.* Neither arm speaks; the claim is about the shape of the published output rather than
about a factor, so arm two is NOT engaged.

*Oracle axis:* **SILENT.**

*Current-text axis:* **AGREES, with the covered domain named.** `decodePiece` commits exactly one
segmentation, chosen by the declared total order at the terminal boundary, and there is no
segmentation-axis abstention. The domain covered is the EVENT LATTICE, and two facts about that
lattice are recorded here as evidence rather than as verdicts: `buildAdapterFacts` omits any
inter-boundary stretch carrying no sounding note (*"a silent gap is not a harmonic event"*), and
`Piece::prepare` excludes anacrusis notes from the content evidence while their events remain in the
lattice. A decode that cannot cover the lattice returns `complete = false` with no segments at all —
a failure, not an abstention.

---

**Row 10 — Statement 10 (no minimum span duration, no maximum change rate, no floor or ceiling).**

*The statement.* The committed boundary set is decided by the fit-versus-cost arithmetic of the joint
objective alone: no minimum chord-span duration, no maximum chord-change rate, no "one chord per bar"
or "one chord per beat" floor or ceiling anywhere in the decision. **Defense class:** FACT (annotated
spans in the staged files range from a half beat to a span carried across a barline and a phrase
mark; none of the three fetched systems carries a duration threshold, and Masada & Bunescu's only
length device is a search cap). **Source class:** derived, **with D-348 and D-337 salvaged as the
ruled analogous shape on the tonality axis.**

*The oracle.* Arm one does not speak. Arm two is ENGAGED (the boundary factor), names the over-grab
case as that factor's test, and states nothing about duration floors or ceilings.

*Oracle axis:* **SILENT.**

*Current-text axis:* **DIFFERS.** The decode carries a hard segment-length cap in EVENTS: the
recurrence in `decodePiece` considers only segment starts within `segCap` events of the current
boundary, and the production notation producer invokes the decode at a cap of four
(`jointnotationproducer.cpp`, *"Whole-score decode, ONCE (§5 total order, seg_cap 4)"*).
`cowork_joint_estimator_factorization.md` §3.7 states the same in specification terms: *"Segment
duration is otherwise implicit-geometric with a hard length cap (the established semi-Markov
default; an explicit harmonic-rhythm duration model is recorded as CONJECTURE-gated future work)."*
Recorded beside it: the cap is a structural bound on span length rather than a scored term, and the
statement's own near-miss clause admits a bounded maximum span length in the search only for
Statement 6.

### 5.3 The evidence — what counts, what tie-breaks, what is never consulted

---

**Row 11 — Statement 11 (the categorized fit of the sounding content is the deciding evidence
class).**

*The statement.* Under the one-span reading every tone of both stretches must be accountable as a
chord member or as a non-chord tone of one chord; under the two-span reading, of two chords;
whichever accounting fits better over the whole passage wins. Pitch content is the deciding evidence
class and everything else shapes or tie-breaks it. **Defense class:** FACT (in all three fetched
systems the dominant term is content fit) plus THEORY. **Source class:** derived; its premise cites
**D-320**.

*The oracle.* Arm one speaks: the ranking's strongest class is *"actual sounding notes — what is
literally happening now"*, above temporal context, the notated key signature and the declared tag.
Arm two is ENGAGED (the pitch emission) and names two cases the emission, spelling and bass factors
must carry.

*Oracle axis:* **MATCHES.**

*Current-text axis:* **AGREES, with one fact recorded beside it.** The content terms are the
emission, spelling, bass and missing-tone families in `segmentContent` (`jointdecoder.cpp`). The fact
recorded, because it bears directly on the statement's own premise and its false-negative path
(which cite D-320, that readings with an absent root occur in the published analyses): candidate
admission in `candidateStates` is decided entirely on pitch content and its first test is
ROOT-PRESENT — a class is admitted only if its root pitch class is among the segment's onset pitch
classes, then only if at least `min(2, |members|)` of its members are present, then only if the
non-member onsets do not exceed the segment's event count. Recorded beside it: the missing-tone term
tests the same classes against the SOUNDING pitch classes of the segment (`Piece::overlapPcs`), so
the admission test and the absence test read different sets. No value for the relative weight of any
evidence family is stated here (**#24**, **D-431**).

---

**Row 12 — Statement 12 (struck and held bear different weight for OPENING a boundary; no tone is
counted twice).**

*The statement.* The evidence for a new span is carried by what is struck at its head; held tones
support continuation and participate as members of the new chord, but a new span whose head strikes
nothing of the new chord is disfavored; and no tone is ever counted twice for being held across the
boundary. **Defense class:** FACT (the checked span heads in the 001 score coincide with onsets, the
corpus-wide claim routed to Open question 2; Masada & Bunescu's held-over marking) plus THEORY.
**Source class:** derived, **with D-467 and D-527 salvaged**; the magnitude declared a fitted value,
UNESTABLISHED.

*The oracle.* Arm one's emission clause forbids struck-ness settling MEMBERSHIP, and this statement
keeps held tones as members, asymmetrizing only the evidence for opening a span; the ranking itself
speaks to evidence CLASSES and not to struck-versus-held within the sounding class. So the oracle's
text makes no claim about this statement's claim. Arm two is ENGAGED (the pitch emission's
covariates) and does not reach it.

*Oracle axis:* **SILENT.**

*Current-text axis:* **DIFFERS**, and on both of the statement's halves. The asymmetry half is
not, as shipped, a weight difference: a tone simply held through an event contributes nothing at all
to that event's emission, because only onset-bearing notes are in the event's note set
(`Piece::prepare`; `jointdecoder.h`'s own field comment) — the OI-228 departure
`ARCHITECTURE.md` names in the oracle's section, seen from the boundary side. The no-double-counting
half does not hold as the statement states it either: the fact surface the adapter reads publishes
tie STARTS and tie CONTINUATIONS as separate atoms, each with its own onset and its own notated span
(`src/composing/analysis/notemodel/note_model.h`), so a tied chain contributes ONE emission term per
notated atom, each carrying the tie-continuation flag — neither the statement's "one onset's worth
across the chain, weighted by sounding duration" nor its named falsifier of one credit per stretch.

---

**Row 13 — Statement 13 (the bass is the single most informative voice, and is never identified with
the root).**

*The statement.* The bass carries three distinct roles — the inversion is read from it, a struck bass
on a strong position is the strongest single boundary cue, and succession plausibility is
bass-sensitive — but "the lowest note is the root" is a known bias, not a rule, and the bass decides
nothing alone. **Defense class:** FACT (Pardo & Birmingham name the failure to weight the bass among
their top error sources; Masada & Bunescu carry a bass-feature family) plus THEORY (figured-bass
practice). **Source class:** derived, **with D-282 and D-465 salvaged**; its premise cites **D-221**.

*The oracle.* Arm one does not speak — it ranks evidence classes, not voices. Arm two is ENGAGED and
speaks: `bwv352@1440`, *"the share-tone Am6 vs F♯ø7 case — spelling and bass factors must carry it"*,
names the bass factor as load-bearing for the case and names it together with the spelling factor
rather than alone.

*Oracle axis:* **MATCHES.**

*Current-text axis:* **AGREES, with one fact recorded beside it.** The bass factor is categorical over
which chord FACTOR sounds in the bass given the class and inversion
(`cowork_joint_estimator_factorization.md` §3.3; the per-event bass term in `segmentContent`), never
an identification of the bass with the root, and the candidate-admission root test reads the segment's
onset pitch classes rather than the bass (`candidateStates`). The fact recorded: `eventBassPc` in
`jointdecoder.cpp` returns the lowest-MIDI note of the event's STRUCK set, so the bass the factor
reads is the lowest note onsetting in that event.

---

**Row 14 — Statement 14 (metric position is a graded prior, never a gate).**

*The statement.* A candidate boundary is more plausible the stronger the metric position of its head;
the analysis prefers strong span heads when the content permits; and no metric position is
unavailable, because annotated boundaries fall on halves of beats. **Defense class:** FACT
(Temperley's strong-beat rule as a graded penalty; Masada & Bunescu's metrical accent features as
learned tendencies; the staged annotations' half-beat boundaries refute a hard beat gate).
**Source class:** derived; the per-level strengths declared fitted and UNESTABLISHED.

*The oracle.* Arm one does not speak. Arm two is ENGAGED (the boundary factor) and says nothing about
metric position.

*Oracle axis:* **SILENT.**

*Current-text axis:* **AGREES.** The boundary term in `segmentContent` is evaluated per event and
conditioned on the event's beat-strength class, on whether the event is the segment head, and on the
fermata context; the four beat-strength classes are `downbeat / mid_strong / other_tactus /
sub_tactus`. `cowork_joint_estimator_factorization.md` §3.7 specifies it as a probability conditioned
on beat-strength class, and §3.8 puts the fermata into it as a prior rather than an exception. It is a
scored term rather than a gate, and no event position is excluded from being a segment head.

---

**Row 15 — Statement 15 (the notated spelling is evidence and is consumed as written).**

*The statement.* Chord templates are matched over spelled tones, so that G♯ and A♭ are different
evidence, and a reading that respects the spelling is preferred over an enharmonic one that does not;
spelling shapes which chord fits and thereby where boundaries fall, and never carries a boundary rule
of its own. **Defense class:** FACT (Temperley's compatibility rule operates on tonal pitch classes)
plus THEORY. **Source class:** derived, **with D-033 salvaged**; D-543 and D-625 cited beside it.

*The oracle.* Arm one does not speak — spelling is a property of the sounding-note class rather than
one of the four ranked classes. Arm two is ENGAGED and speaks: `bwv352@1440` names the spelling
factor as one of the two that must carry the case.

*Oracle axis:* **MATCHES.**

*Current-text axis:* **AGREES.** The spelling emission in `segmentContent` scores the note's
line-of-fifths position relative to the key tonic, so spelled identities reach the fit rather than
pitch classes alone; `cowork_joint_estimator_factorization.md` §3.2 specifies the factor as the
spelled note's scale-degree relation to the key.

---

**Row 16 — Statement 16 (tonality and succession act only through the labeled readings they make
plausible; the written key signature is weaker still; the style setting has no structural effect).**

*The statement.* The prevailing tonality and the chord succession are evidence about boundaries only
through the labeled readings they make plausible; the written key signature is a prior among priors,
overridable by sounding content, and never a boundary cue of its own; the style setting has no
structural effect on the boundary machinery, entering only as fitted values. **Defense class:** THEORY
for the key-signature half. **Source class:** salvaged (**D-345, D-527, D-293**), with the
key-signature half also derived; **D-003** cited beside it.

*The caveat, applied in terms.* This is the one statement that cites the notated key signature. It
**denies** that the signature is a boundary cue rather than asserting it, so the D-450/D-575 caveat's
own trigger — a citation of the notated key signature as boundary evidence — is not met here. The
caveat is recorded as considered and it changes no verdict on this row.

*The oracle.* Arm one speaks: the ranking places the notated key signature third and the declared
major/minor tag weakest, both below actual sounding notes and below temporal context. Arm two is
ENGAGED (the signature/declared-mode prior).

*Oracle axis:* **MATCHES** — the statement's "weaker still, overridable by sounding content" is the
ranking's own placement of those two classes below the sounding notes.

*Current-text axis:* **AGREES, with one fact recorded beside it.** The signature enters as a weak
fitted soft prior on the initial key state with no conditional gate anywhere
(`cowork_joint_estimator_architecture.md` §5a; `cowork_joint_estimator_factorization.md` §3.10; the
prior term applied at the initial-segment branch of `decodePiece`); inference is preset-independent
(`ARCHITECTURE.md`'s head as-built block and standing rule (f)), and the shipped segmentation path
carries no preset-conditional branch. The fact recorded, because the statement says the signature is
never a cue *of its own*: `candidateKeys` in `jointdecoder.cpp` prunes the candidate keys to the top
few by onset-pitch-class overlap with the collection and then ALWAYS keeps the signature key, so the
signature has a structural role in candidate admission beside its role as a scored prior.

---

**Row 17 — Statement 17 (three evidence kinds are never consulted).**

*The statement.* The boundary decision never consults the analysis's own rendered output, nor
user-written chord symbols or other user annotations in the score, nor layout-derived state; ground
truth is graded against and never read at analysis time. **Defense class:** salvaged whole.
**Source class:** salvaged (**D-280, D-501, D-229**), with the circularity argument derived.

*The oracle.* Neither arm speaks: the ranking enumerates four admitted evidence classes and names no
excluded set, and arm two is NOT engaged (an exclusion list is not a factor).

*Oracle axis:* **SILENT.**

*Current-text axis:* **AGREES.** `ARCHITECTURE.md` §3.3 states the two boundary invariants in the same
terms — *"A gate or scoring rule reads STRUCTURED FIELDS ONLY — never a chord-symbol string, never a
Roman numeral"* and *"A written chord symbol in the score may be read ONLY as a comparison or
ground-truth label […] Production paths must not read them as input to analysis at all"* — and
`ARCHITECTURE.md` §3.3's MuseScore-dependency rule carries the layout-state half. The production fact
adapter `jointfactadapter.cpp` reads no harmony element at all.

---

**Row 18 — Statement 18 (no fixed lexicographic ordering resolves disagreeing evidence kinds).**

*The statement.* When evidence kinds disagree, no fixed lexicographic ordering resolves them; the
resolution is the fitted weighting inside the one objective; the only ordering this derivation
asserts is structural — content fit decisive in the ablation sense, boundary-shape priors tipping
what content leaves open, and the never-consulted list absolute — and any finer "evidence A beats
evidence B" claim is a fitted, measured fact rather than a derivable one. **Defense class:** FACT
(the fetched systems disagree with one another about relative strengths) plus THEORY (a lexicographic
ordering is the limit case of extreme weights, and asserting it would hand-set exactly the values the
ruled fitting discipline fits — the statement cites **D-096** and **D-525** for that discipline, and
the boot pack's own principle #17(b)). **Source class:** derived as to structure; measured as to
every pairwise strength, UNESTABLISHED, no ordering value asserted. **Status in the output:** the one
statement the blind session marks Open, deliberately.

*The oracle.* Arm one is itself a ruled, standing, four-class descending-strength ordering of the
evidence — actual sounding notes, then temporal context, then the notated key signature, then the
declared tag — stated as a cross-cutting evidential rule about *"what the analysis may treat as
evidence and in what order"*. Arm two is not engaged (the combination weights are not one of the ten
factors).

*Oracle axis:* **DEFENDED ALTERNATIVE.** The statement declines to assert any ordering finer than
content-first and calls such claims fitted rather than derivable, where the oracle rules exactly such
an ordering over four classes; and the statement carries its defense — that the fetched systems
disagree about relative strengths, that a lexicographic ordering would hand-set the values the ruled
fitting discipline fits, and that the boot pack's own written-prediction gate forbids smuggling a
strength claim past it. Recorded beside it, so the departure is read at its true width: the
statement's own content-first half IS the oracle's top rank, and it is graded MATCHES at Row 11; what
departs is the refusal to rank the three weaker classes against one another.

*Current-text axis:* **AGREES** as to the shipped mechanism. The ten factor terms are combined by one
weight vector and summed, with no lexicographic precedence anywhere in the content score
(`weightedContent` in `jointdecoder.cpp`; the selected weight vector in `jointweights`). No fitted
value and no comparison between fitted values is stated here (**#24**, **D-431**).

### 5.4 Non-chord tones and ornamentation

---

**Row 19 — Statement 19 (non-chord-tone handling is not a separate step).**

*The statement.* There is no pre-cleaning pass that removes ornamental tones before the boundary
decision and no post-hoc repair that re-cuts spans after it; each tone is accounted for inside the
span fit, by category, and the categorization and the boundary are decided together in the one decode.
**Defense class:** FACT (Pardo & Birmingham report their inability to discount passing tones as a
major error class; Masada & Bunescu integrate figuration as segment features and measure better than
the non-integrated alternatives) plus THEORY (pre-cleaning is circular for exactly the tones that
matter). **Source class:** derived independently, **with D-527 and D-285 salvaged** — the statement
says in its own words that it reproduces ruled intent.

*The oracle.* Neither arm speaks. Arm two is ENGAGED (the pitch emission) and names no case of this
shape.

*Oracle axis:* **SILENT.**

*Current-text axis:* **AGREES.** `cowork_joint_estimator_architecture.md` §5a: *"No live cleaning
stage exists. Non-chord tones live INSIDE the pitch-emission factor: each tone is emitted by
category […] Chord identity and tone status are decided together in the one decode."* In the shipped
code each tone is categorized inside `segmentContent` at the moment its emission term is taken, and
no component before or after the decode deletes or reclassifies a tone on ornament grounds.

---

**Row 20 — Statement 20 (the evidence that a tone is ornamental is chord-independent and
melodic-metric).**

*The statement.* Stepwise approach and departure, chromatic-neighbor motion, metric weakness, brevity
relative to neighbors, and tied-over preparation price the non-chord-tone categories, so that a
struck ornamental tone is cheaper to absorb into the standing span than to open a boundary for, while
a genuine change also touched by figuration still wins on content fit. **Defense class:** FACT
(Temperley's ornamental dissonance rule; Masada & Bunescu's figuration features; both directions
visible in the staged chorale 001 at `m3`). **Source class:** derived, **with D-527 salvaged**;
every covariate's weight declared fitted and UNESTABLISHED.

*The oracle.* Neither arm speaks. Arm two is ENGAGED (the pitch emission's covariates) and names no
covariate.

*Oracle axis:* **SILENT.**

*Current-text axis:* **AGREES, with one covariate of the ratified list recorded as not separately
present in the shipped call.** The shipped emission term in `segmentContent` is conditioned on the
tone's category, its metric class (`downbeat / mid_strong / other_tactus / sub_tactus`), its approach
motion, its departure motion (`none / step / leap`) and its tied flag. The ratified covariate list at
`cowork_joint_estimator_factorization.md` §3.1 and `cowork_joint_estimator_architecture.md` §5a
additionally names **chromatic-neighbor motion**, which the shipped call does not pass as an argument
of its own.

---

**Row 21 — Statement 21 (ornament NAMES are derived after the decode; a pedal point annotates a
carried reading).**

*The statement.* Ornament names are derived after the decode from the committed chords by the
standard definitions and published as derived facts; the boundary decision never consumes them. A
pedal point in any voice is an annotation on a carried reading: the harmony changes against the pedal
tone, the pedal tone is priced as a sustained non-chord tone of the spans it crosses, and pedal
detection never mutates the committed spans. **Defense class:** THEORY (the standard definitions are
chord-relative) plus salvage. **Source class:** salvaged (**D-527, D-207, D-385, D-386**), with the
circularity half derived.

*The oracle.* Neither arm speaks; arm two is NOT engaged (ornament naming is downstream of the
factors).

*Oracle axis:* **SILENT.**

*Current-text axis:* **AGREES, with the delivery state recorded.** Nothing in the shipped path feeds
an ornament name into the objective, because no ornament name is computed at all: the notation
record's ornament fields are RESERVED-absent, their own increment being `OPEN_ITEMS.md` OI-194
(`ARCHITECTURE.md`, the notation output-surface record, §3.5), and the record path's pedal fields
*"stay false/-1 (suspended, OI-194)"* (`ARCHITECTURE.md`, the record path block). The ruled shape the
statement describes is `cowork_joint_estimator_architecture.md` §5a — *"Ornament labels […] are
derived AFTER the decode from the committed chord by the standard definitions"* — which is stated and
not built.

---

**Row 22 — Statement 22 (arpeggiation is absorbed by the span fit over sounding content, never by
pooling).**

*The statement.* The tones of a broken chord support one span because each stretch's sounding set
fits the same chord, with the not-currently-sounding members priced as absences rather than as
contradictions, and the analysis never gathers several stretches' notes into one bag to re-derive a
chord from the bag. **Defense class:** salvage plus FACT (Pardo & Birmingham price unmatched template
elements as a mild shortfall) plus THEORY. **Source class:** salvaged (**D-330, D-319**), with the
pricing form derived; its premise cites **D-221** and **D-224**.

*The oracle.* Neither arm speaks. Arm two is ENGAGED (the pitch emission and the missing-tone
penalty) and names no case of this shape.

*Oracle axis:* **SILENT.**

*Current-text axis:* **DIFFERS.** The pricing half holds: an absent chord factor is priced as a
per-factor shortfall normalized per event of segment length (`factorAbsentLogp` in `segmentContent`;
`cowork_joint_estimator_factorization.md` §2's granularity amendment), which is exactly "absences,
not contradictions". The pooling half does not: the shipped decode reads a POOLED pitch-class union
over the whole candidate segment in two places, and the two pool different sets. `candidateStates`
assembles the union of the segment's events' ONSET pitch classes and tests every candidate class's
root presence, member overlap and non-member count against it. The missing-tone term inside
`segmentFeatures` tests each chord factor's presence against `Piece::overlapPcs(i, j)` — the pitch
classes SOUNDING anywhere in the segment's whole tick span, taken from the note spans rather than
from onsets. Recorded beside it: no term re-derives a chord identity FROM a pooled bag; the two
pooled unions are read as an admission filter and as an absence test.

### 5.5 What is published, and how disagreement with a human reading is read

---

**Row 23 — Statement 23 (a boundary-strength is published per committed boundary, with ranked
alternatives per span and open marks).**

*The statement.* Beside the one committed boundary set the analysis publishes, per committed
boundary, a boundary-strength — the declared-class confidence comparing the committed whole reading
against the best whole reading in which that boundary moves or disappears — and, per span, the ranked
alternative readings it was preferred over; where no reading dominates, the commitment stands and
carries an open mark with its reason; near-tie segmentations are carried at low strength rather than
discarded.
**Defense class:** salvage plus THEORY. **Source class:** salvaged (**D-027, D-268, D-032, D-267,
D-349, D-099, D-425, D-387**), with the application to boundaries derived; the squashing map and the
open-mark bar declared fitted or declared constants, UNESTABLISHED.

*The oracle.* Neither arm speaks; arm two is NOT engaged (the published surface is downstream of the
factors).

*Oracle axis:* **SILENT.**

*Current-text axis:* **DIFFERS.** The published uncertainty surface is the posterior slice, and it is
taken with the segmentation HELD: per committed segment it publishes the committed chord class
re-scored under every scoreable candidate key, and every scoreable vocabulary class re-scored under
the committed key, computed post-decode by re-scoring the held span (`ARCHITECTURE.md`, the
POSTERIOR SLICE block; `computePosteriorSlice`). The notation record's per-segment fields
(`jointnotationrecord.h`) carry no boundary-strength, no alternative segmentation and no
boundary-axis open mark, and `ARCHITECTURE.md` records that the record arm publishes the key-axis gap
raw with no remapping, a departure tracked at `OPEN_ITEMS.md` OI-231.

---

**Row 24 — Statement 24 (disagreement with one published human reading is not by itself an error).**

*The statement.* Published readings of the same chorale by two annotation traditions differ in
boundary granularity and placement, and one analyst's own record carries variant readings whose
boundaries differ; the grading of boundaries therefore partitions cases the way the ruled tonality bar
does, and sub-change granularity is graded as its own named class rather than folded into plain
boundary error. **Defense class:** FACT (the enumerated disagreements between the Jones and BCMH
readings of the staged chorales, and the analyst's own recorded variants; the *When in Rome* corpus
paper's own rejection of the concept of ground truth). **Source class:** derived from the staged files
and the fetched corpus paper, **with D-352, D-353 and D-474 salvaged**.

*The oracle.* Neither arm speaks — the traces are a desk-simulation form rather than a grading rule,
and arm two is NOT engaged.

*Oracle axis:* **SILENT.**

*Current-text axis:* **THE TEXT IS SILENT** on a boundary-axis grading partition. The governing
regression unit is deliberately segmentation-invariant and is graded on the chord root, with the
Roman numeral and the key tracked beside it (`CLAUDE.md`, gate threshold and preset policy, block
(A)), so no boundary or segmentation column is measured anywhere in the record. Recorded beside it,
because it is what the statement's own salvage names: the partition the statement describes does
exist in the record for the KEY axis (D-352, D-353, `cowork_layer3_keymode_design.md` §10), and the
ground-truth-ceiling fact the statement cites is on the record at `CLAUDE.md` principle #21 (D-474).

### 5.6 Scale, selection, and context

---

**Row 25 — Statement 25 (the boundary decision works over a bounded working span, with clipped marks
and convergence).**

*The statement.* Cost scales with the selection rather than the piece; boundaries are committed only
inside the selection while music loaded beyond it serves as evidence; a span cut off by the selection
edge is marked as clipped rather than presented as musically closed; and the committed boundaries
inside the selection converge, so that the result after any sequence of extensions equals one fresh
decode over the final loaded span. **Defense class:** salvage, whole, applied to this span kind, plus
THEORY. **Source class:** salvaged (**D-030, D-031, D-260, D-261, D-262, D-264, D-265, D-457,
D-201**), with the application derived.

*The oracle.* Neither arm speaks; arm two is NOT engaged.

*Oracle axis:* **SILENT.**

*Current-text axis:* **DIFFERS.** The ratified contract states exactly these requirements
(`ARCHITECTURE.md` §2.15, the bounded-context contract; `cowork_bounded_context_design.md`), and
Layer 2 implements the clip, the artificial-edge rule and re-slice equivalence (`ARCHITECTURE.md`
§3.3, Layer 2). The production joint arm does not: `produceNotationRecord` decodes the WHOLE score
once, with no selection, no extension request and no clipped mark on an edge segment
(`jointnotationproducer.cpp`, *"Whole-score decode, ONCE"*), which is what `ARCHITECTURE.md` records
as the record producer's own rule — the producer decodes the whole score once and does not cache.

---

**Row 26 — Statement 26 (a stretch of total silence bounds chord-spans; a partial rest does not).**

*The statement.* No chord-span crosses a stretch in which nothing sounds, because a span asserts a
sounding harmony and silence carries none; a short notated rest inside a texture does not bound
anything by itself, and the span continues over it if the fit says so. **Defense class:** THEORY plus
FACT (the staged 137 annotation carries chords across phrase marks). **Source class:** derived.

*The oracle.* Neither arm speaks. Arm two is ENGAGED (the boundary factor's domain is the event) and
names no case of this shape.

*Oracle axis:* **SILENT.**

*Current-text axis:* **DIFFERS.** The partial-rest half holds: `buildAdapterFacts` keeps an
inter-boundary stretch as an event whenever any note sounds across the whole of it, so a single-voice
rest bounds nothing. The total-silence half holds at the lattice and not at the published span: the
same construction omits a stretch in which nothing sounds — its own comment reads *"a silent gap is
not a harmonic event"* — but a committed segment spans consecutive EVENT INDICES and publishes its
extent as the start tick of its first event and the end tick of its last (`decodePiece`'s backtrack),
so where the lattice has omitted a silent stretch between two kept events, the published extent of a
segment covering both bridges that silence. Recorded as evidence about the present text, not as a
verdict on the statement.

## 6. The distribution of verdicts, counted at this file's own rows

No interpretation is offered with these counts, and no ratio, percentage or grade is derived from
them.

**Oracle axis, over 26 rows:**

| Verdict | Count |
|---|---|
| MATCHES | 7 |
| DEFENDED ALTERNATIVE | 1 |
| SILENT | 18 |
| CONTRADICTS, UNDEFENDED | 0 |
| UNGRADED | 0 |

MATCHES: Rows 1, 3, 6, 11, 13, 15, 16. DEFENDED ALTERNATIVE: Row 18. SILENT: Rows 2, 4, 5, 7, 8, 9,
10, 12, 14, 17, 19, 20, 21, 22, 23, 24, 25, 26.

**Current-text axis, over 26 rows:**

| Verdict | Count |
|---|---|
| AGREES | 15 |
| DIFFERS | 10 |
| THE TEXT IS SILENT | 1 |

AGREES: Rows 4, 5, 6, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21. DIFFERS: Rows 1, 2, 3, 7, 10, 12,
22, 23, 25, 26. THE TEXT IS SILENT: Row 24.

**The second arm's engagement, over 26 rows:**

| | Count |
|---|---|
| Engaged (the statement touches a factor of the ratified factorization) | 19 |
| Not engaged | 7 |

Engaged: Rows 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 19, 20, 22, 26. Not engaged: Rows
9, 17, 18, 21, 23, 24, 25. Of the engaged rows, the arm's own text makes a claim reaching the
statement on Rows 6, 13 and 15; on the others it names cases without reaching the statement's claim.

**The caveats, counted:** the D-450/D-575 caveat was applied and its trigger was met on **0** rows
(Row 16 cites the notated key signature and denies rather than asserts that it is a boundary cue).
Rows carrying a salvage source class or citing a salvaged identifier: Rows 6, 7, 8, 9, 10, 11, 12, 13,
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 — each row names its own identifiers.

## 7. The ten open questions — listed, UNGRADED

Ruling 3 states that the open questions are not graded. Each is listed with one sentence on what
would settle it and whether the oracle or the current text already does. **That sentence is
information, not a grade.**

1. **Every fitted value** (the objective's family weights, the covariate strengths, the
   boundary-strength squashing map, the open-mark bar). Settled by the ruled staged fit under the
   pre-fit gates; the oracle does not speak, and the current text already carries fitted tables and a
   selected weight vector compiled into the binary (`ARCHITECTURE.md`'s as-built block), so the
   question is answered for the arm that ships and open for any refit.
2. **May a boundary sit at a pure offset — a moment where notes stop and none starts?** Settled by
   the corpus measurement the question itself names; the oracle's Layer-2 ground admits a release as a
   slice boundary, and the current text admits an event whose start tick is a pure offset, so a
   committed span head at a pure offset is structurally available in the arm that ships.
3. **What the published record says over total silence, and what a fermata does to the evidence.**
   Settled by the output-surface specification the question routes it to; the current text answers
   half of it already — the event lattice omits silent stretches, so nothing is published over them,
   and the fermata enters the boundary factor as a prior and the cadence factor as a location prior
   (`cowork_joint_estimator_factorization.md` §3.8).
4. **The boundary-grading equivalence classes.** Settled only by the measurement-design stage the
   question assigns it to; neither the oracle nor the current text speaks, and the current text
   measures no boundary axis at all (`CLAUDE.md` gate block (A)).
5. **The grain under florid textures.** Settled by the density and cost measurement the question
   names; the oracle does not speak, and the current text carries the standing requirement that very
   large scores be handled (D-201) together with a hard segment-length cap in events, with no such
   measurement on the record.
6. **Should the objective carry an explicit fitted span-length term?** Settled by the ablation the
   question names; the oracle does not speak, and the current text already answers the neighbouring
   question — segment duration is implicit-geometric with a hard cap, and an explicit harmonic-rhythm
   duration model is recorded as CONJECTURE-gated future work
   (`cowork_joint_estimator_factorization.md` §3.7).
7. **The product stance for densely low-strength boundaries.** Settled by a user ruling at that
   design's own sitting; neither the oracle nor the current text speaks, and the record already
   carries the owed product stance for dense uncertainty as **D-498**, which the question itself
   names.
8. **Preset-dependence of committed boundaries.** Settled by a user ruling; the oracle does not
   speak, and the current text answers it for the arm that ships — inference is preset-independent
   (`ARCHITECTURE.md`'s head block; **D-003**), so the committed spans do not differ between presets
   today.
9. **The 137 pairing defect.** **Already ruled**: Ruling 1 of
   `cowork_rulings_2026_08_24_blind_return_sitting.md` fixes the third chorale's human analysis as
   *When in Rome* folder `134`'s `analysis.txt`, matched to the BWV 301 score by content on title,
   signature, meter and bar count, with the pairing rule stated as content and never number.
10. **What three chorales could not test.** Not a question the oracle or the current text can settle;
    it is the staged sample's own stated bound, and the statements whose premises name the untested
    cases (5, 10, 13, 20, 21, 22) carry their exposure in their own residual falsification clauses.

## 8. The blind session's independence record, relayed

**Relayed as facts, with no verdict word attached.** Judging the blindness is the user's, at the
record. Everything in this section down to and including the self-check paragraph is the blind
output's own §6 and §2, read and reported; the two paragraphs after it are this session's own record
of what it did with that material, and say so.

**The stop-on-meeting record — the positive statement.** The output states that no passage stating
how this project's analysis currently decides chord boundaries, or ranks evidence for that decision,
and no passage recognizable as the user's ruled answer to the subject, was met anywhere in the pack,
the brief, or the staged files.

**The three disclosures the output records beside it.**

1. Boot-pack file 02, inside the phase-3 gate qualification, names an open-item family called
   "struck-versus-sounding" and asks whether an item's search space could contain a fact about what
   the decoder or the emission reads. The output records that this was read in full before its
   bearing was weighed; that the session judged it to state that an unsettled question family exists
   near the subject without stating what the analysis does or how evidence is ranked, so the stop
   clause's condition was judged not met and reading continued; and that what was learned from it
   sourced no statement, Statements 3, 4 and 12 being defended from the fetched literature, the
   staged files and theory.
2. Boot-pack file 02 carries two in-place markers reading "[A PASSAGE IS WITHHELD FROM THIS PACK FOR
   THIS SUBJECT.]". The output records that only the markers were seen, that no withheld content
   leaked, that nothing was inferred from the markers' positions, and that the identifier gaps in
   file 05 were treated as evidence of nothing.
3. Boot-pack file 05's admitted entries describe the project's architecture at the level the
   generator admitted. The output records that statements resting on such entries cite them as
   salvaged by identifier; that the two entries closest to the subject that were admitted are D-525
   and D-527; and that Statements 6 and 19 also derive the same conclusions independently from the
   fetched literature so that the derivation does not rest on the salvage alone.

**The files the session records consulting.** The dispatching brief; all seven boot-pack files, each
read whole; all eight staged score and analysis files (three `.mscx` scores read at their title
blocks and at the bars cited, with the 001 score read across its opening bars, and five RomanText
analysis files read whole); the six fetched research sources of its §2, plus one further page it
records as yielding no load-bearing content. The output states that no other file in this repository
was opened, that the only view of the repository outside those reads was a names-only listing of the
root's folder names, that the session's persistent cross-session memory store was deliberately not
read, and that no build, test, measurement tool or repository script was run.

**The input finding the output records in its §2.** The staged score numbered 137 announces itself as
BWV 301, Riemenschneider 71, *Du, o schönes Weltgebäude*, while the staged analysis in folder 137 is
titled *Wer Gott vertraut, hat wohl gebaut*; the output records that the two files therefore do not
describe the same chorale, that it used the 137 analysis only as further exemplar of published
annotation practice, and that no claim in it aligns that analysis to that score. This is the same
finding its Open question 9 carries, and the ruling on it is quoted at §7 above.

**The self-check the output records running on its finished text.** The output states that the whole
document was re-read after assembly and that seven defects were found and corrected in place before
delivery — an overclaimed corpus check in Statements 4 and 12 narrowed to what was actually checked
with the general claim routed to Open question 2; a wrong example removed from Statement 5; a
mislabeled ornament corrected in Statement 20; a weak span example in Statement 10 and an unverified
rest claim in Statement 26 replaced; three bare non-musical uses of the word "score" qualified; and
two miscounts in its noise measurement recounted — and that one earlier defect was caught during
writing, a first draft of the sizing record carrying hand-typed group times that disagreed with its
own timestamp log.

**The sizing record's own values are named to the file and are not restated here** (**D-431**): the
measured phase times, the share of statements marked open, the share settled as to form while
carrying an UNESTABLISHED measured component, the share the session would put to the user, and the
noise measurement's per-source consultation counts are all at
`cowork_blind_derivation_harmony_boundary_2026_08_23.md` §5. The counts this file carries of its own
are the statement count and the open-question count in its manifest header, taken at the graded
file's own structure, together with the verdict distribution at §6, counted at this file's own rows.

**One checked fact about the output's citations, recorded as a fact.** Every distinct design-intent
identifier cited anywhere in the output was read off the output's own text and checked against LIST
ONE of `ratification_surfaces/cowork_withheld_family_harmony_boundary_reading.md` — the list of
entries withheld from the boot pack. **No cited identifier is a member of that list.** No count is
transcribed here (**D-431**); the two files are named so the check can be re-taken. This carries no
verdict word, and what it means for the blindness question is the user's to judge at the record.

## 9. What this file does NOT do

- **It recommends nothing.** No recommendation on the derivation method appears anywhere in it, by
  Ruling 4 of the comparison-design sitting; the method ruling comes to the user afterwards as a
  separately written decision surface over this tabulation.
- **It establishes nothing** (**#19**). Every verdict in it is this session's authored reading, and
  every one is re-gradeable by the user at the two quoted texts. Nothing here clears a guard, closes
  a row, or moves a status.
- **It takes no verdict on the blind session's independence.** §8 relays; it does not judge.
- **It states no verdict on the current text.** The current-text axis is evidence about what the
  specifications and the code say today. A DIFFERS row is not a defect finding, is not an open-items
  row, and adjudicates nothing between the statement and the text — the phase definitions reserve
  that to the audit.
- **It measures nothing about the analysis.** No measurement was built, designed, scoped or run for
  it; the comparison is textual throughout.
- **It edits nothing it grades.** The blind output, the boot pack and its manifest, the dispatching
  brief, the withheld-family reading file, every governing document and every register source are
  byte-unchanged by the act that produced this file.
- **It closes no open item.** `OPEN_ITEMS.md` OI-179 stays OPEN and GATES; OI-372 and OI-374 stand as
  found. No finding number is allocated; the series stands at F88.

---

*Provenance: Claude Code, 2026-08-24, at the tree carrying commit `35dd95e152`, under
`cc_instruction_comparison_harmony_boundary.md` Task 1, executing Rulings 1–4 and §5 of
`cowork_rulings_2026_08_24_comparison_design_sitting.md`. The blind output was read whole as this
session's very first act, before its session-start read, by Ruling 2. The oracle's two arms were
located by their own text and quoted from the files. The untrusted sources were opened per statement.
TOWARDS the ultimate objective and TOWARDS the guiding principles.*
