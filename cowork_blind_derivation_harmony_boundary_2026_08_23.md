# Blind derivation — where one chord ends and the next begins, and what evidence decides it

> **STATUS: DRAFT — BLIND DERIVATION, NOT COMPARED, NOT RATIFIED.**
> Written 2026-08-24 by the deriving session (a fresh Cowork session, per the dispatching brief
> `cowork_blind_session_brief_harmony_boundary.md`). This session read ONLY that brief, the boot pack
> `tools/audit/derivation_boot_pack/harmony-boundary/`, the eight score and analysis files the brief
> stages by name, and the published research cited in §2 — nothing else in this repository. It
> compared nothing against any implementation or specification; a later session does that. Nothing
> here is a verdict on anything the project currently does.

## 0. Terms

Standard music theory is used in its standard sense. Project or technical terms used in this
document, each defined before it is used:

- **The analysis** — the harmonic-analysis software this project builds: given a notated score, it
  decides the tonality, the chords, and the moments at which one chord gives way to the next.
- **Chord-span** — a maximal stretch of the score reported as governed by one chord (one Roman
  numeral with its inversion). The subject of this document is where a chord-span ends.
- **Boundary** — the moment at which one chord-span ends and the next begins.
- **Partition point** — a moment at which the set of sounding notes changes because at least one
  note starts or at least one note stops (the term is the fetched Pardo–Birmingham paper's, used in
  its sense there).
- **Minimal stretch** — the stretch between two consecutive partition points, over which the set of
  sounding notes is constant.
- **Sounding versus struck** — a note is *sounding* at a moment if it has started and not yet
  stopped there, including a note struck earlier and still held; it is *struck* at a moment if its
  onset is at that moment.
- **Tonality** — what is commonly called the key; the bare word *key* is used only in this sense.
- **Bar** — the metric unit (never "measure" as a noun); **beat position** — a position inside a
  bar, written as the staged analysis files write it: `m4 b2.5` is bar 4, halfway between beat 2 and
  beat 3.
- **Non-chord tone** — a sounding note that is not a member of the prevailing chord: passing tone,
  neighbor tone, suspension, anticipation, pedal point, or a tone of an arpeggiation figure, each in
  its standard sense.
- **Joint decode** — an optimization that chooses a whole reading at once: the segmentation into
  chord-spans and the label of every chord-span are decided together over a passage, by exact search
  (dynamic programming), not one stretch at a time.
- **Boundary-strength** — a confidence attached to one committed boundary: how much better the
  committed reading is than the best reading in which that boundary is placed differently or absent.
- **FACT / THEORY / CONJECTURE** — the labels the boot pack's principles prescribe for load-bearing
  claims: FACT is stated or measured in a source actually fetched and read (or directly readable in
  a staged file, cited by file and line); THEORY is established published theory; CONJECTURE is
  neither.
- **Source class of a statement** — *derived* (from theory or fetched research), *salvaged* (taken
  from a ruled design-intent entry in the boot pack, cited by its identifier `D-…`), or *measured*
  (rests on a measurement this session cannot make; written with the measurement it would need, its
  establishment status UNESTABLISHED, and no value).
- **RomanText** — the plain-text format of the staged human analyses: one line per bar, each chord
  change written at its bar and beat position.
- **The three chorales** — the staged scores and analyses named in §2. "The staged 001 files" means
  the pair (score, human analyses) for chorale 001, and so on.

The fourteen-section design-document structure is not claimed for this document: it is a derivation
record produced under a dispatching brief whose §7 fixes this document's own structure (statements,
open questions, sizing record, independence record). The two writing standards that bind every
document — qualified predicates; defined terms, plain vocabulary, no shorthand — are claimed and
were applied.

## 1. What this document answers

**How should a harmonic analysis of a notated score decide the moment at which one chord ends and
the next begins, and what evidence should decide it?** The answer is given as atomic statements
(§3), each carrying its defense, its source class, its status, its silent premise with that
premise's false-negative path, and what would falsify it. What could not be settled on the declared
sources is an open question (§4), never filled with the most plausible reading.

## 2. The sources — declared in full

**Read within the repository (the whole of it):** the dispatching brief; the boot pack's seven
files (`00_READ_THIS_FIRST.md`, `01_the_phase_definitions.md`,
`02_the_guiding_principles_and_the_conventions.md`, `03_the_writing_standards.md`,
`04_the_dispatch_protocol.md`, `05_the_ratified_design_intent.md`, `06_the_defect_type_catalog.md`),
each read whole.

**The staged scores and analyses (by name, per the brief's §3):**
- `tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx` — its own subtitle reads
  "(BWV 269; R 030)".
- `tools/dcml/bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx` — subtitle
  "(BWV 153/3; R 005)".
- `tools/dcml/bach_chorales/MS3/137 Du, o schönes Weltgebäude.mscx` — subtitle "(BWV 301; R 071)".
- `…/when_in_rome/…/Chorales/001/analysis.txt` (analyst Andrew Jones; BWV 269) and
  `analysis_BCMH.txt` beside it (the Bach Chorales Melody-Harmony Corpus reading, machine-translated
  into RomanText).
- `…/Chorales/003/analysis.txt` (analyst Andrew Jones; BWV 153.1) and `analysis_BCMH.txt` beside it.
- `…/Chorales/137/analysis.txt` (analyst Dmitri Tymoczko).

**An input finding, recorded rather than smoothed over.** The staged score "137" announces itself
as BWV 301, Riemenschneider 71, *Du, o schönes Weltgebäude* (score file, lines 89 and 92); the
staged analysis in folder 137 is titled *Wer Gott vertraut, hat wohl gebaut* with no BWV given
(`137/analysis.txt`, lines 3 and 2). The two files therefore do not describe the same chorale, and
the brief's premise that the score numbers are Riemenschneider numbers is false at the 137 score
(its own subtitle says R 071). Consequence for this document: the 137 analysis file is used only as
a further exemplar of published annotation practice; no claim below aligns it to the 137 score. The
001 pair matches (BWV 269 on both sides); the 003 pair matches by title, with the BWV sub-number
written differently on the two sides (153/3 on the score, 153.1 in the analysis) — noted, not
resolved.

**Fetched and read (published research; every load-bearing claim from these is labeled where it is
used):**
1. Pardo & Birmingham, *Algorithms for Chordal Analysis*, Computer Music Journal 26(2), 2002 —
   fetched from https://interactiveaudiolab.github.io/assets/papers/pardo-birmingham-cmj02.pdf.
2. Masada & Bunescu, *Chord Recognition in Symbolic Music: A Segmental CRF Model, Segment-Level
   Features, and Comparative Evaluations on Classical and Popular Music*, TISMIR 1(1), 2018 —
   fetched from https://transactions.ismir.net/articles/10.5334/tismir.18.
3. Temperley, *An Algorithm for Harmonic Analysis*, Music Perception 15(1), 1997 — fetched from
   https://davidtemperley.com/wp-content/uploads/2015/11/temperley-mp97.pdf.
4. Nápoles López, Gotham & Fujinaga, *AugmentedNet: A Roman Numeral Analysis Network with Synthetic
   Training Examples and Additional Tonal Tasks*, ISMIR 2021 — fetched from
   https://archives.ismir.net/ismir2021/paper/000050.pdf.
5. Karystinaios et al., *AnalysisGNN: Unified Music Analysis with Graph Neural Networks*, 2025 —
   fetched from https://arxiv.org/html/2509.06654.
6. Gotham et al., *When in Rome: A Meta-corpus of Functional Harmony*, TISMIR, 2023 — fetched from
   https://transactions.ismir.net/articles/10.5334/tismir.165.

One further page was fetched and yielded no load-bearing content (the Melisma system introduction
page, https://www.link.cs.cmu.edu/melisma/intro.html — it points at source 3, which was then fetched
whole). No needed source failed to fetch; no equation or claim below rests on an unfetched source.

**The admitted-facts hole, worked under as declared.** The pack carries no ledger of empirically
established facts about this project's own data, so this session used none; every place a corpus
fact was wanted is an open question in §4, not a filled value.

## 3. The statements

Each statement carries the six fields the brief's §4 prescribes, in order: the statement; the
defense; the source class; the status; the premise it rests on with that premise's false-negative
path; and what would falsify it (in CODE — the observable, the decision rule over it, and the
near-miss that does NOT falsify it — or in the RESIDUAL, the pattern of disagreement with human
annotation, where the statement is a modelling premise with no code site). This session cannot name
code sites; every CODE observable is named in plain terms for the comparison session to locate.

### 3.1 The grain — where the question may be asked at all

**Statement 1.** The atomic grain of the boundary question is the minimal stretch: the question
"which chord is sounding?" is asked over every stretch between two consecutive partition points, and
a boundary may be committed only at a partition point. The grain is fixed by the notation (onsets
and offsets), not by the bar, not by the beat, and not by a fixed sub-beat sampling unit.

- *Defense.* FACT: Pardo & Birmingham define the partition point as the moment "where the set of
  pitches currently sounding in the music changes by the onset or offset of one or more notes" and
  build all segmentation on minimal stretches between them. FACT: Masada & Bunescu state "harmonic
  changes may occur only when notes begin or end" and take candidate boundaries at "all the note
  onsets and offsets in the input music". THEORY: between two partition points nothing observable
  changes, so no evidence exists to separate two readings that differ only there — a boundary inside
  a minimal stretch is undecidable in principle from a notated score. FACT (staged files): fixed
  coarser grains are refuted by the annotations — the 001 analysis places changes at `m3 b2.5`,
  `m6 b3.5`, `m15 b1.5`, `m20 b3.5` (001 `analysis.txt` lines 14, 17, 28, 34), which a bar or beat
  grain cannot express. A fixed fine sampling grid (AugmentedNet samples at thirty-second notes,
  eight steps per quarter — FACT) expresses these but is either redundant (positions where nothing
  starts or stops carry no evidence) or lossy (music subdividing finer than the grid).
- *Source class.* Derived.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the notated onsets and offsets are the whole of
  the sounding surface. False where notation understates sound: grace notes, tremolos, arpeggiation
  signs, trills and unwritten ornaments sound notes the note list may not carry as plain onsets; a
  score whose ornament realization is not expanded would make the grain silently coarser than the
  music, and nothing in the boundary machinery would show it.
- *Falsification.* CODE. Observable: the set of candidate boundary positions the boundary decision
  actually considers, over a test score containing off-beat onsets. Decision rule: every onset and
  offset position is a candidate and no position inside a minimal stretch is one; the statement is
  falsified if a committed boundary can fall where no note starts or stops, or if an onset position
  is structurally unavailable as a boundary (as a bar- or beat-grained design would make `m3 b2.5`
  unavailable). Near-miss that does NOT falsify: an implementation that evaluates a superset of
  positions (a fine grid) but can only ever COMMIT a boundary at a partition point.

**Statement 2.** A boundary is committed only where the sounding content changes; a stretch over
which the sounding set is constant is never split. Two adjacent chord-spans carrying the same label
and the same inversion are not two spans; a same-label restatement in an annotation is a
representation artifact, not a musical boundary, and the analysis must not produce one.

- *Defense.* THEORY: a boundary with identical content and identical label on both sides asserts a
  distinction no evidence can support (Statement 1's undecidability argument applied to the
  degenerate case). FACT (staged files): the machine-translated BCMH reading of 001 restates `I6` at
  `m9 b2` after `I6` at `m9 b1` (001 `analysis_BCMH.txt` line 17) where the human-proofread reading
  carries one `I6` span (001 `analysis.txt` line 20) — a translation artifact of exactly this shape
  exists in the staged data, so the distinction between a boundary and a restatement is real and
  must be normalized before any comparison.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the published representation (label + inversion
  per span) captures everything a boundary asserts. False if the target representation later gains
  span-level fields beyond label and inversion (for example a marked restrike or a phrase-carried
  annotation) whose change alone should legitimately open a span; the normalization would then
  erase a real distinction and the erasure would not show.
- *Falsification.* CODE. Observable: the committed chord-span sequence on any input. Decision rule:
  no two adjacent committed spans agree in both label and inversion; falsified by any output
  carrying such a pair. Near-miss: two adjacent spans with the same root but different inversion or
  quality — that is a real boundary (Statement 5) and does not falsify.

**Statement 3.** The boundary question is asked over the sounding set, not the struck set: every
note sounding in a minimal stretch — including a note struck earlier and still held — is evidence
for the harmony of that stretch. A reading of only the struck notes is refuted.

- *Defense.* FACT: Pardo & Birmingham weight each note by the number of minimal stretches it spans,
  so a held note bears evidence in every stretch it sounds through. FACT: Masada & Bunescu carry,
  for every pitch of every stretch, "a boolean value … indicating whether or not it is held over
  from the previous event" — held notes are in the evidence, marked as held. FACT: Temperley weights
  events by duration in the fit ("longer events affect the results more"), which is only possible if
  a note bears evidence for as long as it sounds. FACT (staged files): at 001 `m1 b2` the annotation
  reads `IV6` (001 `analysis.txt` line 12) while the soprano G is a held half note (001 score,
  bar-2 block, soprano `half` G then quarter D) — the held G is the fifth of the annotated IV; a
  struck-only reading of that stretch would not contain the chord the human analysis names. THEORY:
  the suspension — a held tone dissonant against a newly struck harmony — is definable only if held
  tones are part of the stretch's content.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: a held note keeps sounding at its notated pitch
  for its notated duration. False for instruments whose sound decays to silence (piano, plucked
  strings): late in a long held chord the notation says "sounding" while the ear may hear nothing;
  on such music the sounding set overstates the evidence and the overstatement would not show in any
  notation-level check.
- *Falsification.* CODE. Observable: the evidence set the chord fit reads for a stretch containing a
  tied-over note (the 001 `m1 b2` stretch is a concrete instance). Decision rule: the held note is
  present in the fit's input for that stretch; falsified if only struck notes reach the fit.
  Near-miss: the held note present but weighted differently from a struck note — that is
  Statement 12, not a falsification of this one.

**Statement 4.** Struck and held are nevertheless not interchangeable: the analysis must be ABLE to
distinguish them per tone per stretch, because (a) a boundary is overwhelmingly opened by an onset,
and (b) held-versus-struck is a load-bearing input to non-chord-tone categories (a suspension is
prepared by a held tone; a passing tone is struck).

- *Defense.* FACT: Masada & Bunescu's held-over boolean exists because their features consume it;
  their figuration features (suspension detection) require the preparation's tie. FACT: every chord
  change in the five staged analysis files is written at a beat position, and over the 001 score's
  opening bars — the stretch this session checked note against annotation — every such position
  carries an onset; no checked change falls at a pure offset (the check's narrowness is Open
  question 2's subject, and the general claim is left to that measurement). THEORY: the standard definitions of suspension (held preparation) and
  passing tone (struck, approached and left by step) are stated in terms of struck-versus-held, so a
  representation that erases the distinction cannot express the definitions.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the note representation preserves ties versus
  restrikes as written. False where an import or a reduction merges tied chains into one long note
  or splits one note into tied fragments: the struck/held distinction then reports the encoding, not
  the music, and suspension features silently mis-fire.
- *Falsification.* CODE. Observable: the per-tone fields available to the emission/fit at each
  stretch. Decision rule: a tone's struck-versus-held status at that stretch is readable there;
  falsified if the representation collapses it. Near-miss: an implementation that stores onset times
  and derives held-ness on demand — the information is available, which is what the statement
  requires.

**Statement 5.** A change of bass against an unchanged chord membership is a boundary: the target
representation distinguishes inversions, so a new bass note over the same root and quality ends the
chord-span. Conversely a mere re-voicing above an unchanged bass with unchanged membership is not a
boundary.

- *Defense.* FACT (staged files): the annotations mark inversion-only changes as changes — 001
  `m13 I b2 I6` (001 `analysis.txt` line 26) and 001 `m16 I6 b2 I` (line 29). THEORY: in Roman-numeral practice the figured inversion is part of
  the chord identity; a representation that reports inversion must place a boundary where the
  inversion changes or it reports a falsehood over half the span. FACT: Masada & Bunescu carry bass
  features per segment ("which note of a given chord appears as the bass"), which is coherent only
  if a segment has one bass identity.
- *Source class.* Derived.
- *Status.* Settled, with its edge open: whether a very short bass tone (an eighth-note passing
  tone in the bass) opens an inversion boundary or is a non-chord tone of the standing span is the
  ordinary non-chord-tone decision (Statements 19–20) applied to the bass, and the staged readings
  disagree on exactly such a case (001 `m3`: the Jones reading carries `IV` to `b2.5`; the BCMH
  reading inserts `IV2` at `b2` — 001 `analysis.txt` line 14 versus `analysis_BCMH.txt` line 11).
  The MECHANISM is settled (bass change can be a boundary; the non-chord-tone machinery decides
  whether it is one here); the disagreement is a granularity fact about annotators, taken up in
  Statement 24.
- *Premise and its false-negative path.* Premise: the lowest sounding notated voice is the bass the
  representation means. False in sparse or crossed textures where the notated lowest tone is not a
  structural bass (a high cello above a resting bass, a voice crossing); an inversion boundary would
  then be opened by a tone no listener hears as the bass, and nothing in the notation flags it.
- *Falsification.* CODE. Observable: committed spans over a passage whose only change is the bass
  (any staged instance above). Decision rule: the analysis CAN commit a boundary there (structural
  capability, not a per-case demand — the non-chord-tone decision may legitimately absorb a given
  case); falsified by a design in which same-membership stretches are unconditionally merged so that
  no inversion boundary can ever be committed. Near-miss: the analysis absorbing one particular
  short bass tone as ornamental — that is the intended behaviour of Statements 19–20, not a
  falsification.

### 3.2 The boundary decision itself

**Statement 6.** Segmentation and labeling are one decision, made over the whole working passage at
once: the analysis chooses the best (segmentation, labeling) pair jointly, by exact dynamic
programming over the minimal stretches, never segmentation first with labels after, and never
stretch-by-stretch greedy commitment.

- *Defense.* FACT: Masada & Bunescu's segmental model, which decides both jointly by "a semi-Markov
  analogue of the usual Viterbi algorithm", beats the stretch-by-stretch alternatives on every
  corpus they test (event accuracy 83.2% versus 77.2% on Bach chorales; 78.0% versus 57.0% on
  TAVERN; a 27.0% relative error reduction on chorales). FACT: Pardo & Birmingham measured that even
  where their labeling was perfect given the right segmentation, a search optimizing their local
  per-segment candidate scores found segmentations reaching only 86.89% label accuracy — their own conclusion is
  that "segment scores generated by our current system do not fully capture the detail needed to
  match the answer key segmentation"; the segmentation cannot be decided apart from what the labels
  will be. FACT: Temperley's search is dynamic programming over the whole passage with retroactive
  revision of earlier chord roots when later evidence demands it. THEORY: a boundary is defined by
  the difference between the readings on its two sides, so its rightness is a property of the whole
  reading, not of the moment. Salvaged corroboration: the ratified fitting parameterization already
  names the semi-Markov conditional-likelihood objective over frozen factor tables (D-525), and the
  ratified non-chord-tone decision states "chord identity and tone status are decided together in
  the one decode" (D-527) — the ruled design intent is a joint decode, and this statement derives
  the same answer independently from the published evidence.
- *Source class.* Derived (independently), with D-525 and D-527 cited as salvaged corroboration.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: an additive per-span objective (span score plus
  transition terms) captures the quality of a whole reading, so that exact dynamic programming over
  it IS the whole-passage decision. False where genuinely non-local dependencies carry weight — a
  parallel passage forty bars later, a piece-level harmonic plan: an additive objective cannot see
  them, the decode would still be exactly optimal FOR ITS OBJECTIVE, and the gap would surface only
  as residual disagreement, never as a search failure.
- *Falsification.* CODE. Observable: the control flow from candidate stretches to committed spans.
  Decision rule: no boundary is irrevocably committed before the whole working passage's evidence
  has been able to bear on it (backward within the passage counts; the bounded-context contract
  bounds the passage); falsified by a design that commits each boundary from left context alone with
  no revision, or that fixes the segmentation before any label is scored. Near-miss: a
  linear-time exact semi-Markov decode (it processes left to right but its commitment is the global
  optimum), and a bounded maximum span length in the search (a search-space cap, not a greedy
  commitment).

**Statement 7.** The boundary decision is made together with the chord-identity decision at the
same level, and inside a tonality context: the fit of a candidate span is the fit of a labeled
reading (degree, quality, inversion relative to a tonality), not of an unlabeled span. But the
chord-span boundary and the tonality boundary are two different span kinds with two different
decisions — a chord boundary never by itself asserts a tonality change, and the tonality's own
change machinery (confirmation, persistence, change-cost) is not restated by this subject.

- *Defense.* THEORY: whether the alto D of a IV bar is a chord seventh (opening IV4/2) or a passing
  tone (no boundary) depends on what the chord IS — the boundary cannot be decided against unlabeled
  pitch content (the 001 `m3` disagreement between the two staged readings is exactly this shape,
  001 `analysis.txt` line 14 versus `analysis_BCMH.txt` line 11). FACT: in Masada & Bunescu, span
  features (purity, coverage, bass, figuration) are all functions of the candidate LABEL and the
  span's notes together. Salvaged: the ruled joint state's chord axis is degree-valued relative to
  the state's own tonic and mode (D-526), so the one decode's chord decisions are tonality-relative
  by construction; the span typology separates the chord-span from the key-span and bans the bare
  word "region" (D-028); tonicization-versus-modulation has its own ruled machinery (cadence
  confirmation plus persistence as a change-cost, D-337), which this subject consumes and does not
  restate.
- *Source class.* Derived, with D-526, D-028 and D-337 salvaged.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the tonality context available to the chord-span
  decision is right enough, often enough, that deciding chord-spans inside it (rather than fully
  jointly with it at every moment) loses only a minority of cases. False on music where chord and
  tonality genuinely co-depend densely (resolution-denying chromatic music): there the chord-span
  boundaries would inherit every tonality error, and the loss would masquerade as chord errors in
  the residual rather than announcing itself.
- *Falsification.* RESIDUAL. This is a modelling premise about decomposition, not one code site. The
  pattern that falsifies it: boundary disagreements with human annotation that concentrate where the
  human's tonality differs from the analysis's, and disappear when the analysis is conditioned on
  the human's tonality — that pattern would show the chord-boundary machinery is fine and the
  decomposition is the fault, at which point the coupled treatment (a joint chord-tonality step) is
  the remedy, not a change to the boundary rules.

**Statement 8.** The objective the joint decode optimizes is additive over chord-spans and their
adjacencies: per span, how well the sounding content fits the labeled chord (every tone categorized,
Statement 19) plus how the span sits in the meter (Statement 14); per adjacency, how plausible the
chord succession is in the tonality context. The factor FORMS come from theory and published
models; the factor VALUES are fitted once against annotated music and never tuned per case.

- *Defense.* FACT: this factorization — span-content fit, metric placement, succession plausibility
  — is the common core of all three fetched systems (Pardo–Birmingham: the template candidate score
  S = P − (M + N); Temperley: compatibility + strong-beat + variance rules summed into "a single
  global score"; Masada & Bunescu: purity/coverage + metrical accent + chord bigram features).
  Salvaged: forms-from-theory with values-fitted-once is the ruled fitting decision (D-096), the
  staged fit with frozen generative tables and a small discriminative weight vector is ruled
  (D-525), and per-case tuning is the named defect the catalog forbids (DT-2, and D-096's "never
  tuned per case").
- *Source class.* Derived for the factorization; salvaged (D-096, D-525) for the fitting
  discipline; measured for every VALUE — the weights and table entries are quantities this session
  cannot supply: the measurement they need is the ruled staged fit on the annotated corpus,
  establishment status UNESTABLISHED, no value written here.
- *Status.* Settled as to form; every value open until fitted.
- *Premise and its false-negative path.* Premise: one weighting of the factors serves the whole
  repertoire in scope. False where styles genuinely re-rank evidence kinds (chorale versus florid
  keyboard figuration): a single weighting would be a compromise wrong at both ends, and since the
  fit averages over the corpus, the wrongness would hide inside per-style residuals rather than
  showing in any aggregate number.
- *Falsification.* CODE for the form: observable — the terms the span objective actually sums;
  decision rule — they are exactly (span-content fit, metric placement, succession plausibility)
  with no term reading forbidden evidence (Statement 17); falsified by a load-bearing term of
  another kind smuggled in, or by any value hand-set per passage. Near-miss: additional PUBLISHED
  evidence facts carried beside the objective without deciding it (publication is Statement 23's
  business). RESIDUAL for the sufficiency of the form: systematic boundary errors that no weighting
  of these three factor kinds can remove would falsify the factorization itself.

**Statement 9.** The decode commits exactly one boundary set — the best whole reading — and never
abstains on the segmentation axis: every moment of the analyzed span lies in exactly one committed
chord-span (silence handling per Open question 3). Ambiguity is expressed beside the commitment
(Statement 23), never by an uncommitted or overlapping segmentation.

- *Defense.* THEORY: chord-spans of one texture tile the music by construction — the question
  "which chord is sounding here?" has exactly one committed answer per moment or the output is not
  an analysis of the whole selection; overlapping or absent spans would make every downstream
  consumer (Roman numeral emission, grading) undefined. Salvaged: the decoder's ruled behaviour on
  the tonality axis is to commit its best path and never abstain (D-114); every layer emits ranked
  candidates plus a confidence, never a forced point estimate ALONE but always a committed best
  (D-027); the span typology's members tile the music, the one ruled exception being per-voice
  phrase-spans (D-400) — the chord-span is not that exception.
- *Source class.* Derived, with D-114, D-027, D-400 salvaged.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: even genuinely non-tonal stretches are best served
  by a committed nearest reading plus honest low confidence, rather than by a segmentation gap. This
  is the stance the ruled record takes for unrecognized scales (D-344: report the best-fitting
  recognized mode, never the unrecognized scale) and its cost is real: on out-of-vocabulary music
  the committed spans are noise with low confidence, and a consumer that ignores confidence reads
  them as analysis. The false-negative path is a consumer under-reading the confidence, which no
  notation-level check shows (the ruled product stance for dense uncertainty is owed — D-498 —
  and Open question 7 records the boundary-side face of it).
- *Falsification.* CODE. Observable: the committed span set over any analyzed selection. Decision
  rule: the spans partition the selection (no gap, no overlap); falsified by an output with a moment
  in zero or two committed chord-spans. Near-miss: carried ALTERNATIVE segmentations beside the
  committed one — that is required by Statement 23, and the alternatives may overlap the committed
  spans freely.

**Statement 10.** The committed boundary set is decided by the fit-versus-cost arithmetic of the
joint objective alone: there is no minimum chord-span duration, no maximum chord-change rate, no
"one chord per bar" or "one chord per beat" floor or ceiling anywhere in the decision.

- *Defense.* FACT (staged files): annotated spans range from a half beat (001 `m6 b3 V b3.5 V7`,
  `analysis.txt` line 17) to a span carried across a barline and a phrase mark (137 `m3 … b3 V ||`
  with the next bar's first labeled position at `b2` — the carry covers more than three beats; 137
  `analysis.txt` lines 11–12), so any fixed floor or ceiling is refuted by published practice
  inside a single piece. FACT: none of the three fetched systems carries a duration
  threshold; Temperley's strong-beat rule penalizes weak-beat STARTS, not short spans as such, and
  Masada & Bunescu's only length device is a search cap (L = 20 events), not a musical rule.
  Salvaged analogy: on the tonality axis the ruled record states in terms that brief-versus-sustained
  has NO duration threshold and falls out of fit-versus-cost arithmetic (D-348); the same shape is
  the right one here and for the same reason — the boundary is a continuum with no published
  threshold (D-337's ground).
- *Source class.* Derived, with D-348/D-337 salvaged as the ruled analogous shape.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the fitted succession and metric terms suffice to
  keep the committed harmonic rhythm musical (they penalize implausibly fast change where the
  corpus does). False on music whose figuration density far exceeds the fitted corpus (the
  Wagner-class scores the record requires be handled, D-201): there the terms fitted on chorales may
  under-penalize rapid spurious change, the output would fragment, and no rule would exist to catch
  it because this statement removed the rule — the guard is the fitted values' scope, which is
  exactly the premise's weak point.
- *Falsification.* CODE. Observable: the decision terms of the objective. Decision rule: no term
  reads a span's duration against a fixed threshold and no term counts spans per bar against a
  limit; falsified by any such term. Near-miss: a fitted, continuous span-length or
  succession-rate term (a semi-Markov length model) — that is arithmetic, not a threshold, and
  Open question 6 asks whether it should exist.

### 3.3 The evidence — what counts, what tie-breaks, what is never consulted

**Statement 11.** The primary evidence for keeping two adjacent stretches in one chord-span or
separating them is the categorized fit of the sounding content on each side: under the
one-span reading every tone of both stretches must be accountable as a chord member or as a
non-chord tone of one chord; under the two-span reading, of two chords. Whichever accounting fits
better — over the whole passage, with all terms — wins. Pitch content is the deciding evidence
class; everything else in Statements 13–16 shapes or tie-breaks it.

- *Defense.* FACT: in all three fetched systems the dominant term is content fit (Pardo–Birmingham's
  template score; Temperley's compatibility rule ordered 1, 5, 3, ♭3, ♭7, ornamental; Masada &
  Bunescu's purity and coverage features, which their ablations make the strongest family). THEORY:
  a chord is constituted by its tones; every other evidence kind (meter, bass, succession) is
  information ABOUT where chords tend to change, not about what is sounding.
- *Source class.* Derived.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the annotated target actually follows the sounding
  content. False where annotators name a chord whose defining tone never sounds (the ruled record
  carries exactly this fact: readings with an absent root occur in the published analyses — the
  tried-and-reverted absent-root guard's ground, D-320); content fit alone would score such spans
  badly, the fitted values absorb some of it, and the remainder sits invisibly in the residual.
- *Falsification.* CODE. Observable: the objective's terms and their fitted weights (once fitted).
  Decision rule: the content-fit family carries decisive weight in the sense that zeroing it changes
  committed boundaries on a majority of test passages, while zeroing any other single family does
  not; falsified if a non-content family dominates in that ablation sense. Near-miss: individual
  cases where a tie-breaker decides — that is the tie-breakers doing their job.

**Statement 12.** Within the content evidence, a struck tone and a held tone bear different weight
for OPENING a boundary: a boundary at a moment where nothing is struck is licensed only by an
offset (Open question 2), and the evidence FOR a new span is carried by what is struck at its head;
held tones support continuation and participate as members of the new chord, but a new span whose
head strikes nothing of the new chord is disfavored. No tone is ever counted twice for being held
across the boundary.

- *Defense.* FACT (staged files): every span head named by the 001 analysis over the score's
  opening bars coincides with an onset in the staged score (the stretch this session checked note
  against annotation; the corpus-wide claim is Open question 2's measurement, not asserted here).
  FACT: Masada & Bunescu's held-over marking exists so features can treat the two differently. THEORY: an onset is the composer's act of change; a held tone was already accounted
  for by the previous span, so re-crediting it as new evidence double-counts one notated event.
  Salvaged: a rebuilt chord scoring must not lean on the removed held-note repetition bonus — the
  faithful note model counts a tie once (D-467); the ruled emission conditions on the tied-over /
  syncopated preparation as a covariate (D-527), which is this asymmetry in ruled form.
- *Source class.* Derived, with D-467 and D-527 salvaged.
- *Status.* Settled as to the asymmetry's existence and direction; its magnitude is a fitted value
  (measured; UNESTABLISHED; the measurement is the ruled staged fit).
- *Premise and its false-negative path.* Premise: notated ties and restrikes reflect the sounding
  articulation. False on encodings that normalize repeated notes into ties or vice versa
  (Statement 4's premise, inherited here); the asymmetry would then systematically mis-aim, and on
  such scores boundaries would drift toward wherever the encoder put restrikes.
- *Falsification.* RESIDUAL for the direction (it is a modelling premise): if fitted models that
  ignore struck-versus-held match human boundaries as well as models that use it, the asymmetry
  carries no information and the statement falls. CODE for the no-double-counting half: observable —
  the per-stretch evidence a tied chain contributes; decision rule — one onset's worth across the
  chain, weighted by sounding duration, never one onset per stretch; falsified by a re-strike credit
  at each stretch head.

**Statement 13.** The bass is the single most informative voice for the boundary decision, in three
distinct roles — the inversion is read from it (Statement 5), a struck bass on a strong position is
the strongest single boundary cue, and succession plausibility is bass-sensitive — but the bass is
never identified with the root: "the lowest note is the root" is a known bias, not a rule, and the
bass decides nothing alone.

- *Defense.* FACT: Pardo & Birmingham name the failure to weight the bass among their top error
  sources ("adding extra weight to the bass note … could have resolved" several cases). FACT:
  Masada & Bunescu carry a dedicated bass-feature family. THEORY: in figured-bass practice the bass
  is the voice the harmony is reckoned over; chorale and continuo textures state harmonic motion in
  the bass. Salvaged: the ruled record warns from measurement that a bare bass-is-root signal
  rewards wrong readings (D-282: "BIR rewards wrong-root=bass") and that two thirds of one gate
  population existed to correct the scorer's bass-as-root pull (D-465) — the bias is real, measured,
  and must not be rebuilt into the boundary evidence.
- *Source class.* Derived, with D-282 and D-465 salvaged.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: a structural bass exists and is the notated lowest
  sounding tone (Statement 5's premise, inherited — the ruled record already carries the sparse
  upper-register counter-case, D-221). False in unaccompanied upper-voice textures and during bass
  rests; there the "bass role" evidence should silently stand down, and a design that instead
  promotes the momentary lowest tone would inject boundaries nothing musical supports.
- *Falsification.* CODE. Observable: the feature set of the span objective. Decision rule: bass
  identity enters as inversion evidence and as covariates, and no term equates lowest-note with
  root or lets bass evidence alone commit a boundary against the content fit; falsified by a
  bass-only decision path. Near-miss: a case where bass evidence tips an otherwise near-tied
  decision — tipping near-ties is what evidence is for.

**Statement 14.** Metric position is a graded prior, never a gate: a candidate boundary is more
plausible the stronger the metric position of its head, the analysis prefers span heads on strong
positions when the content permits, and NO metric position is unavailable — annotated boundaries
fall on halves of beats and the analysis must be able to place them there.

- *Defense.* FACT: Temperley's strong-beat rule ("prefer chord spans that start on strong beats of
  the meter", implemented as a graded penalty by beat strength). FACT: Masada & Bunescu's metrical
  accent features ("chord segments are more likely to begin on accented beats") are learned
  tendencies, not constraints. FACT (staged files): boundaries at `b2.5`, `b3.5`, `b1.5` in the 001
  and 137 analyses (001 `analysis.txt` lines 14, 17, 28; 137 `analysis.txt` lines 14, 21–22) refute
  any hard beat gate. Temperley's own hard version ("time points that are not beats of the metrical
  structure at all are simply disallowed as segment boundaries") is workable only because his beat
  structure includes low metrical levels; stated over the actual beat it would be refuted by the
  staged data, which is why this statement grades rather than gates.
- *Source class.* Derived.
- *Status.* Settled as to gradedness and direction; the per-level strengths are fitted values
  (measured; UNESTABLISHED).
- *Premise and its false-negative path.* Premise: the notated meter is the heard meter. False under
  hemiola, syncopated styles, or a mis-notated source: the prior would then pull boundaries toward
  notated positions the music does not accent, and because it is only a prior, the damage would be
  a quiet bias in ambiguous cases — visible only in the residual against annotations of such music.
- *Falsification.* CODE. Observable: the metric term's form and the candidate set. Decision rule:
  the term is monotone in metric strength and no position is excluded; falsified by a binary
  beat/bar gate or by any position structurally unavailable (also falsified through Statement 1).
  Near-miss: a fitted metric term that is nearly flat — weak is allowed; absent or gating is not.

**Statement 15.** The notated spelling is evidence and is consumed as written: chord templates are
matched over spelled tones (so G♯ and A♭ are different evidence), and a reading that respects the
spelling is preferred over an enharmonic one that does not. Spelling shapes WHICH chord fits and
thereby where boundaries fall; it never carries a separate boundary rule of its own.

- *Defense.* FACT: Temperley's compatibility rule operates on tonal pitch classes, "not neutral
  pitch classes, preserving enharmonic spelling distinctions", and his variance rules prefer
  compact line-of-fifths readings. THEORY: notated spelling is the composer's own record of
  function (a chorale's raised fourth spelled as such announces the applied dominant), and the
  brief's scope is notated scores, where spelling is present by construction. Salvaged: the layer
  contract requires using ALL the information the note reader carries losslessly — "notated
  spelling, metric weight, voice" (D-033); the ruled encoding for discovery work keeps spelling
  where it exists (D-543); spelling presence is tested with the validity predicate (D-625).
- *Source class.* Derived, with D-033 salvaged.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the source's spelling is trustworthy. False for
  imported or auto-transcribed scores (MIDI-derived input spells by convenience): there
  spelling-sensitive fits would mis-rank templates, and the failure would look like chord errors,
  not like what it is — evidence corruption at the input. The analysis must be ABLE to weigh
  spelling down where the source declares itself unspelled (D-543's mod-12 fallback is the ruled
  shape of that ability).
- *Falsification.* CODE. Observable: the template/emission fit's input representation. Decision
  rule: spelled tone identities reach the fit (not pitch-class-mod-12 only); falsified by a mod-12
  collapse on spelled sources. Near-miss: mod-12 handling of genuinely unspelled input.

**Statement 16.** The prevailing tonality and the chord succession are evidence about boundaries
only THROUGH the labeled readings they make plausible (Statement 7's conditioning and Statement 8's
succession term). The written key signature is weaker still: a prior among priors, overridable by
sounding content, and never a boundary cue of its own. The style setting has no structural effect
on the boundary machinery at all — style enters only as fitted values.

- *Defense.* THEORY: a key signature declares a default collection, not a harmonic event; nothing
  changes at a moment because of the signature. Salvaged: the ruled stance toward the written key
  signature on the tonality axis is a deliberately weak prior the note evidence overrides (D-345,
  which also records that the style preset first acts at the tonality decision — upstream facts and
  the cutting of music into stretches are preset-independent in that ruled account); the ruled
  style-adaptation rule for the emission is "values-only … same structure, no per-style rule code"
  (D-527); inference is preset-independent in the ruled record's presentation sense (D-003), and
  fitted values are per idiom, never per preset (D-293).
- *Source class.* Salvaged (D-345, D-527, D-293), with the key-signature half also derived.
- *Status.* Settled as to structure. One edge is deliberately left open: whether the fitted VALUES'
  style-dependence may move a committed boundary on the same notes under two presets. The ruled
  record answers yes in principle (values differ per idiom) — Open question 8 records the product
  question that follows.
- *Premise and its false-negative path.* Premise: style-dependence of values does not amount to
  style-dependence of structure. False if a fitted covariate exists in one style's tables and is
  absent (not merely weak) in another's: absence is structure wearing a value's clothes, and the
  per-style rule-code ban would be breached without any rule code existing.
- *Falsification.* CODE. Observable: the boundary machinery's code paths under different presets.
  Decision rule: identical control flow, differing only in table values; falsified by a
  preset-conditional branch in segmentation logic. Near-miss: different committed boundaries under
  different presets on ambiguous music — values legitimately do that.

**Statement 17.** Three evidence kinds are NEVER consulted by the boundary decision: the analysis's
own rendered output (chord-symbol strings, Roman-numeral text — no reading back of the presentation
layer); user-written chord symbols or other user annotations in the score (comparison labels only,
never analysis input); and layout-derived state (positions, spacing — presentation products, not
musical facts). Ground-truth annotations are graded against, never read at analysis time.

- *Defense.* Salvaged, whole: gates and scoring read structured fields only, never a chord-symbol
  string or a Roman numeral (D-280, with its ruled ground — symbol-derived signals are lossy and
  entangled with the formatter, and reading the rendered form back makes the analysis depend on its
  own presentation); a written chord symbol is read only as a comparison or ground-truth label,
  never as input that influences what the analyzer computes (D-501 — a symbol is user content and
  may be wrong, and in a measurement tool it would compare the annotation with itself); the bridge
  layer never reads layout-derived state as analysis input (D-229). THEORY: each is either
  derivative of the analysis itself (circular) or not a property of the music.
- *Source class.* Salvaged (D-280, D-501, D-229).
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the input representation actually excludes these
  channels, so nothing needs to police them at decision time. False if a future evidence fact is
  derived FROM one of them upstream and published as an ordinary fact — the boundary decision would
  consume it without knowing its provenance; the false-negative path is provenance-blind fact
  publication, and the guard is the publication contract's provenance rules, not this statement.
- *Falsification.* CODE. Observable: the transitive inputs of every objective term. Decision rule:
  no path from presentation output, user symbols, or layout state into any term; falsified by one
  such path. Near-miss: a measurement tool placing user symbols BESIDE the output for comparison.

**Statement 18.** When evidence kinds disagree, no fixed lexicographic ordering resolves them: the
resolution is the fitted weighting inside the one objective, and the only ordering this derivation
asserts is structural — content fit is decisive in the ablation sense (Statement 11), boundary-shape
priors (meter, struck-head, succession) tip what content leaves open, and the never-consulted list
(Statement 17) is absolute. Any finer "evidence A beats evidence B" claim is a fitted, measured
fact, not a derivable one.

- *Defense.* FACT: the fetched systems disagree with each other about relative strengths (Temperley
  resolves compatibility ties by line-of-fifths variance; Masada & Bunescu let training set every
  weight; Pardo & Birmingham hand-set template weights and report the residual cost), so the
  literature does not license a fixed ordering. THEORY: a lexicographic ordering is the limit case
  of extreme weights; asserting it without measurement would hand-set exactly the values the ruled
  fitting discipline says are fitted (D-096, D-525). The pack's own principle #17(b) demands a
  written prediction per assumption BEFORE measuring — this statement deliberately refuses to
  smuggle strength claims past that gate.
- *Source class.* Derived as to structure; measured as to every pairwise strength (the measurement:
  the ruled staged fit plus per-family ablations on held-out annotated music; establishment status
  UNESTABLISHED; no ordering value asserted).
- *Status.* Open — deliberately: the fitted ordering cannot be settled on the declared sources, and
  writing one would be the filled-plausible-reading this brief forbids.
- *Premise and its false-negative path.* Premise: a single fitted weighting exists under which the
  disagreements of evidence kinds resolve acceptably across the scope. False if the evidence kinds
  interact non-additively (meter mattering only during figuration, bass only in homophony): a
  weighting would then be the wrong function family, and the misfit would be invisible except as an
  unexplained residual floor.
- *Falsification.* RESIDUAL: per-family ablations on held-out annotated music are the observable;
  the statement's structural half is falsified if some non-content family proves decisive in the
  ablation sense, and its refusal half is vindicated or refuted by whether the fitted weighting
  reproduces human boundary placements better than any hand-declared ordering.

### 3.4 Non-chord tones and ornamentation — kept from faking and from hiding boundaries

**Statement 19.** Non-chord-tone handling is not a separate step: there is no pre-cleaning pass
that removes ornamental tones before the boundary decision, and no post-hoc repair that re-cuts
spans after it. Each tone is accounted for INSIDE the span fit, by category — chord member,
within-scale non-chord tone, outside-scale tone — and the categorization and the boundary are
decided together in the one decode.

- *Defense.* FACT: Pardo & Birmingham, who lack integrated non-chord-tone handling, report "the
  system's inability to discount passing tones from consideration" as a major error class (23% of
  their errors) — the separate-or-absent treatment is measured to fail. FACT: Masada & Bunescu
  integrate figuration detection as segment features inside the joint model and beat the
  non-integrated alternatives. THEORY: pre-cleaning is circular for exactly the tones that matter —
  a suspension is DEFINED relative to the chord, so deciding it before the chord inverts the
  definition. Salvaged: the ruled record states this outcome in terms — "No live cleaning stage
  exists", tones emitted by category inside the one decode, with the published cleaners' error rate
  (~28%) named as the reason a pre-cleaning commitment upstream is forbidden, and the suspension's
  chord-relative definition named as the circularity (D-527); ornaments are handled chord-first,
  "segmentation + NCT post-process, never union re-derive / richer vocabulary" (D-285).
- *Source class.* Derived (independently from the fetched evidence), with D-527 and D-285 salvaged
  — this statement reproduces ruled intent and says so.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the category vocabulary (member / within-scale /
  outside-scale) plus chord-independent covariates carries enough of the ornament distinctions to
  price them. False for ornament kinds whose identity is irreducibly contextual beyond covariates
  (a chain of suspensions over a sequence): the categories would price them as generic dissonance,
  the spans would still commit, and the shortfall would surface only as boundary drift on exactly
  such passages.
- *Falsification.* CODE. Observable: the pipeline order around the decode. Decision rule: no
  component before the decode deletes or reclassifies tones on ornament grounds, and no component
  after it moves a committed boundary on ornament grounds; falsified by either. Near-miss: deriving
  ornament LABELS after the decode (Statement 21) — that names tones, it moves nothing.

**Statement 20.** The evidence that a tone is ornamental is chord-independent and melodic-metric:
stepwise approach and departure, chromatic-neighbor motion, metric weakness, brevity relative to
its neighbors, and tied-over preparation. These covariates price the non-chord-tone categories so
that a struck ornamental tone is cheaper to absorb into the standing span than to open a boundary
for — which is what keeps figuration from faking boundaries — while a genuine change also touched
by figuration still wins on content fit — which is what keeps figuration from hiding boundaries.

- *Defense.* FACT: Temperley's ornamental dissonance rule — prefer ornamental readings for tones
  "closely followed by an event a step or half-step away in pitch height" — is exactly the
  stepwise-departure covariate, and his strong-beat interaction supplies metric weakness. FACT:
  Masada & Bunescu's figuration features encode passing, neighbor and suspension shapes as
  chord-independent tests and measurably help. Salvaged: the ruled emission conditions on "stepwise
  approach and departure, chromatic-neighbor motion, metric weakness, the tied-over/syncopated
  preparation … every covariate computable without knowing the chord, so no circularity" (D-527).
  FACT (staged files): the mechanism's two directions are both visible in chorale 001 — the alto's
  struck lower-neighbor eighth (the D of E–D–E) inside the IV span at `m3 b1.5` opens no boundary
  in the Jones reading (001 `analysis.txt` line 14; the staged score's fourth Measure block, the
  pickup bar being the first, alto eighths E–D–E–F♯), while the same bar's
  `b2.5` DOES open one (viio6) because the content genuinely changes; and the two published readings
  of `m3 b2` disagree about which mechanism wins there (`IV` carried, versus `IV2` inserted —
  `analysis_BCMH.txt` line 11), which is the near-tie the pricing must express as low
  boundary-strength rather than decide loudly.
- *Source class.* Derived, with D-527 salvaged.
- *Status.* Settled as to the covariate set's membership and both directions of the mechanism;
  every covariate's weight is fitted (measured; UNESTABLISHED).
- *Premise and its false-negative path.* Premise: ornamentality is expressible per tone from local
  melodic-metric shape. False for arpeggiation and pedal points, whose ornamentality is a property
  of a PATTERN over many tones, not of one tone's approach and departure — Statements 21 and the
  arpeggiation half below carry them separately; a design that priced only per-tone covariates and
  claimed this statement satisfied would miss both, and the miss would look like fragmentation over
  arpeggiated textures.
- *Falsification.* RESIDUAL, in both directions, on annotated music: spurious-boundary rate over
  figurated passages (boundaries the annotation lacks, at figuration onsets) and missed-boundary
  rate where figuration coincides with annotated changes. The statement is falsified if removing
  the covariates does not raise these rates (they carry nothing) or if no fitted pricing brings
  both directions down together (the mechanism is the wrong shape).

**Statement 21.** Ornament NAMES (passing tone, neighbor tone, suspension, anticipation, pedal
point) are derived after the decode from the committed chords by the standard definitions and
published as derived facts; the boundary decision never consumes them. A pedal point — in any voice
— is an annotation on a carried reading: the harmony changes against the pedal tone, the pedal
tone is priced as a sustained non-chord tone of the spans it crosses, and pedal detection never
mutates the committed spans.

- *Defense.* THEORY: the standard definitions are chord-relative, so the names are computable
  exactly when the chords are committed and not before (the same circularity as Statement 19).
  Salvaged: ornament labels derived after the decode and published for presentation is the ruled
  shape (D-527); the pedal-point class is voice-independent (D-207); pedal detection's ruled home is
  a reader over the carried output that "annotates a carried reading — never a second analysis that
  overwrites the winner" (D-385), consuming the carry's own ranked alternatives rather than adding a
  new scan (D-386).
- *Source class.* Salvaged (D-527, D-207, D-385, D-386), with the circularity half derived.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: pricing a pedal tone as a sustained non-chord
  tone inside the ordinary emission is enough for the BOUNDARY decision even before any pedal
  pattern is recognized. False for long pedals under rich harmonic motion: tone-by-tone pricing
  taxes every span the pedal crosses, and a fit could prefer readings that wrongly include the
  pedal tone as a member (flattening real boundaries); the pattern-level fact "this is one pedal"
  would have paid the tax once. The false-negative path is boundary flattening over pedal
  passages, visible only in the residual there.
- *Falsification.* CODE for the order: observable — dataflow between the decode and the ornament
  namer; decision rule — names read committed spans, spans never read names; falsified by a name
  feeding the objective. RESIDUAL for the pricing premise: boundary agreement over annotated pedal
  passages versus elsewhere.

**Statement 22.** Arpeggiation is absorbed by the span fit over sounding content, never by pooling:
the tones of a broken chord support one span because each stretch's sounding set fits the same
chord (with the not-currently-sounding members priced as absences, not as contradictions), and the
analysis never gathers several stretches' notes into one bag to re-derive a chord from the bag.

- *Defense.* Salvaged: "Never a pooled recompute" is ruled in terms — membership is judged per
  stretch against the prevailing chord, because pooling "over-reads, treating every passing note as
  a chord tone", and that failure motivated a rebuild (D-330); pooling an arpeggio's notes and
  re-reading the chord from the pool was implemented, measured worse (duration-weighting lets the
  wrong pitch win), and reverted — do not retry (D-319). FACT: Pardo & Birmingham's template score
  prices absent template tones as a mild shortfall ("M = unmatched template elements") rather than
  as contradictions, which is exactly what lets a two-tone stretch of a broken triad fit the triad.
  THEORY: an arpeggio is one harmony unfolded in time; its unity is that one chord accounts for
  every stretch, not that its notes co-sound.
- *Source class.* Salvaged (D-330, D-319), with the pricing form derived.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: pricing absences mildly (rather than pooling)
  still leaves the true chord the best whole-passage reading over sparse textures. False at the
  sparse extreme — a one-note stretch fits many chords and the succession term must carry the
  decision; if the fitted succession values are weak there, fragmentation or arbitrary labels
  result, and the failure clusters on thin textures (the ruled record's sparse-texture cautions,
  D-221/D-224, are the same cluster seen from the legacy side).
- *Falsification.* CODE for the prohibition: observable — the fit's per-stretch input; decision
  rule — no term reads a union of several stretches' tones as if co-sounding; falsified by a pooled
  bag anywhere in the boundary path. RESIDUAL for the pricing premise: boundary agreement on
  annotated arpeggiated textures.

### 3.5 What is published, and how disagreement with a human reading is read

**Statement 23.** Beside the one committed boundary set (Statement 9), the analysis publishes, per
committed boundary, a boundary-strength — the declared-class confidence comparing the committed
whole reading against the best whole reading in which that boundary moves or disappears — and, per
span, the ranked alternative readings it beat. Where no reading dominates at a boundary, the
commitment stands and carries an open mark with its reason. Ruled-out segmentations that were
near-ties are carried at low strength, not discarded.

- *Defense.* Salvaged, largely: every layer emits ranked candidates plus a confidence, never a
  forced point estimate alone (D-027); a confidence attaches to a NAMED decision, and
  "boundary-strength" is one of the named decision kinds in the ruled confidence contract (D-268);
  confidences crossing a boundary between layers are in [0, 1] and class-declared (D-032, D-267);
  the whole-reading comparison (re-run with the decision forced otherwise, not the local top-two
  gap) is the ruled shape of sequence-decision confidence on the tonality axis (D-349), and the
  boundary is a sequence decision of the same kind; negative evidence is carried, not dropped
  (D-099); the uncertainty surface's ruled contract is the full posterior with the local slice as
  the first delivered step (D-425); a contradiction or irreducible ambiguity is surfaced on the one
  open mark with a reason, never on a parallel flag (D-387). THEORY: the near-tie the two staged
  001 readings expose at `m3 b2` (Statement 20) is exactly the case a downstream consumer and a
  grader need the strength for; a committed boundary set without strengths asserts certainty the
  evidence does not hold.
- *Source class.* Salvaged (D-027, D-268, D-032/D-267, D-349, D-099, D-425, D-387), with the
  application to boundaries derived.
- *Status.* Settled as to what is published; the strength's squashing map and the open-mark bar are
  fitted or declared constants (measured; UNESTABLISHED).
- *Premise and its false-negative path.* Premise: forcing one boundary and re-decoding yields a
  well-defined "best different reading" for every committed boundary at bearable cost. False if
  the forced-alternative space is ill-defined at edges (the first span head; boundaries adjacent to
  silence) — the strength would there be computed against a degenerate rival and read as strong; the
  false-negative path is over-confident strengths at exactly the positions where the definition
  frays.
- *Falsification.* CODE. Observable: the published output surface for one analyzed passage.
  Decision rule: per boundary a class-declared strength in [0, 1]; per span, ranked alternatives;
  open marks carrying reasons where declared bars are not met; falsified by a boundary published
  bare, an alternative list pruned to the winner, or a second parallel ambiguity flag. Near-miss:
  the full posterior arriving as a later step with the local slice first — that is the ruled
  delivery order (D-425).

**Statement 24.** Disagreement between the analysis's boundaries and one published human reading is
not by itself an error: published readings of the SAME chorale by two annotation traditions differ
in boundary granularity and placement, and one analyst's own record carries variant readings whose
boundaries differ. The grading of boundaries therefore partitions cases the way the ruled tonality
bar does — agreement demanded where the published readings are unanimous; where they differ or a
variant is recorded, matching ANY recorded reading (or declaring the ambiguity) meets the bar — and
sub-change granularity (added seventh, inversion change, cadential six-four notation) is graded as
its own named class, never silently folded into plain boundary error.

- *Defense.* FACT (staged files), the disagreements enumerated: 001 `m6 b3 V b3.5 V7` (Jones)
  versus `m6 … b3 V7` (BCMH) — one boundary tradition splits the added seventh, the other does not
  (001 `analysis.txt` line 17; `analysis_BCMH.txt` line 14); same shape at `m15 b1 V6 b1.5 V6/5`
  versus `V65` whole (lines 28 / 23) and at `m20` (lines 34 / 28); placement disagreement plus
  reading disagreement at `m8` (`I b2 ii b2.5 viio6 b3 I6` versus `I b2 viio6 b3 I6`, lines 19 / 16);
  insertion disagreement at `m3 b2` (Statement 20). The analyst's own variants move boundaries: 001
  `m17var1` shifts the arrival of I from `b3` to `b3.5` (lines 30–31); 003 `m4` records `i6/4`
  against `m4var1 III+6` with the analyst's note spelling out that the choice turns on whether one
  tone is an incomplete neighbor (003 `analysis.txt` lines 16–18), and the BCMH tradition writes the
  same bar as `Cad64` (003 `analysis_BCMH.txt` line 12) — three notations of one passage, two
  boundary structures. FACT: the When in Rome corpus paper "explicitly rejects the concept of
  'ground truth'" for this material and stores alternative analyses per work. Salvaged: the ruled
  grading bar on the tonality axis has exactly this partition — unambiguous cases demand the single
  reading, genuinely ambiguous cases are met by any recorded reading or an uncertain mark (D-352);
  accuracy and calibration are graded separately (D-353); ground truth is itself an instrument whose
  agreement ceiling is unmeasured for this repertoire, with no published number to cite (#21,
  D-474); the annotation is "one published human reading, graded against in this project, not a
  specification" (the brief's own words).
- *Source class.* Derived from the staged files and the fetched corpus paper, with D-352, D-353 and
  D-474 salvaged.
- *Status.* Settled as to the partition's shape; the equivalence classes a boundary comparison
  needs (how near is "the same boundary"; what merges/splits count as sub-change granularity) are a
  measurement-design decision this session may not take — Open question 4.
- *Premise and its false-negative path.* Premise: recorded variants and cross-tradition
  disagreement identify the genuinely ambiguous cases well enough to partition the grading. False
  where both traditions happen to agree on a reading that is nevertheless not unique (unanimity by
  small sample, not by musical necessity — with mostly one or two readings per piece this is
  common): the partition would then demand agreement on cases that deserve the ambiguous bar, and
  the analysis would be graded wrong for defensible readings. The three-chorale sample cannot bound
  how often; the ceiling measurement (OI-179's subject, named in the pack) is the only route.
- *Falsification.* RESIDUAL by construction (this is a grading premise): the observable is the
  distribution of boundary disagreements over the unanimous/divergent partition on annotated music;
  the statement is falsified for practical purposes if disagreements concentrate on unanimous cases
  (the partition buys nothing) — and vindicated if a material share of raw boundary "errors" lands
  on divergent cases and reclassifies as defensible.

### 3.6 Scale, selection, and context

**Statement 25.** The boundary decision must work over a bounded working span: its cost scales with
the selection, not the piece; boundaries are committed only inside the selection while music loaded
beyond it serves as evidence; a span cut off by the selection edge is marked as clipped, never
presented as musically closed; and when the analysis extends its loaded context to settle an edge,
the committed boundaries inside the selection must converge — the result after any sequence of
extensions equals one fresh decode over the final loaded span.

- *Defense.* Salvaged, whole, from the ruled bounded-context family, applied to this span kind: cost
  scales with the working span, re-analysis is incremental, the working span is extensible (D-030);
  whole-score analysis is the degenerate case (D-031); output covers exactly the selection,
  everything beyond is evidence, never a result (D-260); context is extended incrementally with the
  stop condition being convergence of the in-selection answer, never a guessed amount (D-261, the
  increment being the requester's own scale, D-262); any sequence of extensions equals a single
  fresh run (D-264); the extension request is a data-supply call downward, inference flows forward
  (D-265); an edge span clipped by the selection is marked with its provenance, and an unclosed edge
  span carries an extension cue that only the pipeline driver may act on (D-457); very large scores
  must be handled and are expected to be common (D-201). THEORY: a chord-span is decided by local
  content plus bounded context (its neighbors and tonality), so a bounded decode with convergence is
  adequate in principle — the semi-Markov decode's additive objective (Statement 8) is exactly the
  kind that localizes.
- *Source class.* Salvaged (D-030, D-031, D-260, D-261/262/264/265, D-457, D-201), with the
  application derived.
- *Status.* Settled.
- *Premise and its false-negative path.* Premise: the in-selection boundary set really does converge
  under context extension (the additive objective localizes). False if a boundary near the edge
  oscillates between two readings as context grows (a near-tie flipping with each extension): the
  convergence stop would never fire and a cap would fire instead — and a cap that fired is never
  the discovered amount (D-261's own clause), so the case must surface as an open mark, not as a
  silent commitment. The false-negative path is a cap-terminated extension read as convergence.
- *Falsification.* CODE. Observable: committed in-selection boundaries as a function of loaded
  context on an edge-ambiguous passage. Decision rule: boundaries identical after convergence to a
  fresh whole-span decode (the equivalence invariant), spans at the selection edge carrying the
  clipped mark; falsified by chunking-dependent boundaries or an unmarked clipped span. Near-miss:
  different intermediate states during extension — only the converged result binds.

**Statement 26.** A stretch of total silence bounds chord-spans: no chord-span crosses a stretch in
which nothing sounds, because a span asserts a sounding harmony and silence carries none. A short
notated rest INSIDE a texture (a breath, a voice resting while others sound) does not bound
anything by itself — the span continues over it if the fit says so.

- *Defense.* THEORY: the chord-span's meaning is "this chord governs this stretch of sounding
  music"; over total silence there is no sounding anything, and any label there is invention (the
  brief's own reserved-word discipline: a rest is the silence). The partial-rest half follows from
  Statement 3 — the sounding set over the stretch is what is read, and it is non-empty while any
  voice sounds. FACT (staged files): the annotations carry chords across the `||` phrase marks and
  leave bar-initial positions unlabeled where the previous chord carries (137 `analysis.txt`
  lines 11–12: `… b3 V ||` then a bar whose first labeled position is `b2`), so phrase breathing
  does not bound a span in published practice.
- *Source class.* Derived.
- *Status.* Settled for total silence and for partial rests; what the published record should SAY
  over a total-silence gap (nothing at all, or an explicit no-harmony span) is representation, not
  boundary decision, and is left to the output-surface's own specification — noted in Open
  question 3 with the fermata/pause cases it interacts with.
- *Premise and its false-negative path.* Premise: notated silence is silence (no pedal-sustain, no
  reverberant carry). False on piano music under a sustain pedal marking and on music with
  laissez-vibrer notations: sound genuinely crosses the notated rest, a harmony audibly persists,
  and a design that hard-bounds at notated silence would cut a span the ear carries — invisible in
  a notation-level check unless pedal markings are read as sounding-state evidence.
- *Falsification.* CODE. Observable: committed spans over a passage with a whole-texture rest and
  over one with a single-voice rest. Decision rule: no span crosses the former; the latter is
  crossable; falsified by either direction inverted. Near-miss: an anacrusis — the first span
  starting at the first onset rather than at bar 1, beat 1 is required by Statement 1, not a
  silence rule (the staged 001 and 003 annotations both begin at a pickup: `m0 b3` and `m0 b4`).

## 4. Open questions — stated, never filled

1. **Every fitted value.** The weights of the objective's families, the covariate strengths, the
   boundary-strength squashing map and the open-mark bar are all fitted quantities (Statements 8,
   12, 14, 18, 20, 23). Establishment status UNESTABLISHED; the measurement each needs is the ruled
   staged fit plus per-family ablations on held-out annotated music. No ruling is asked; this is
   fit-phase work.
2. **May a boundary sit at a pure offset — a moment where notes stop and none starts?** Statement 1
   admits offsets as candidate positions; Statement 12 disfavors strike-less span heads; all five
   staged analyses place every change at an onset, but three chorales cannot settle the general
   case (a chord "changing" when a suspension resolves downward IS an onset; the genuinely
   offset-only change may be rare or nonexistent). Wanted: a corpus measurement — the share of
   annotated changes falling at positions with no onset, over the full annotated corpus. This is an
   instance of the admitted-facts hole; no value is guessed.
3. **What the published record says over total silence, and what a fermata does to the evidence.**
   Statement 26 bounds spans at total silence; whether the output there carries nothing or an
   explicit no-harmony stretch is an output-surface decision, and whether a fermata's notated
   lengthening should raise its position's metric weight (the staged chorales change chords AT
   fermata arrivals, e.g. 001 `m4`) is an evidence-design detail the declared sources do not
   settle. Would ask the user: "Over a whole-texture silence, does the published analysis carry an
   explicit empty stretch or no stretch at all?"
4. **The boundary-grading equivalence classes.** Statement 24 demands a partition and a named
   sub-change class; what counts as "the same boundary" (exact position only? within an eighth?),
   how merges/splits are scored, and whether the headline number is stretch-weighted or
   boundary-weighted (the fetched Masada & Bunescu paper reports both event-level accuracy and
   the segment-level F-measure — the published term for the precision–recall summary — and the two
   rank systems differently) is measurement design — the
   measurement-design stage's business, not this session's. Would ask, at that stage: "Which
   comparison classes does the boundary measurement declare?"
5. **The grain under florid textures.** On chorales the minimal-stretch grain is small; on a
   Wagner-class score (which the ruled record requires be handled and expects to be common, D-201)
   the number of minimal stretches per bar grows with figuration density, and the decode's cost and
   the fitted values' validity there are unmeasured. Wanted: a measurement of minimal-stretch
   density and decode cost over large chromatic scores before any cap or coarsening is designed;
   any cap would interact with the undischarged sub-beat annotation duration gate the ruled record
   carries (D-471).
6. **Should the objective carry an explicit fitted span-length term?** Statement 10 removes
   thresholds; a continuous fitted length model per meter (the semi-Markov duration term the
   fetched model family supports) is neither required nor excluded by the declared sources —
   Temperley's evidence is positional only, and none of the fetched systems fits a duration term
   for classical music. Wanted: an ablation — does a fitted length term improve held-out boundary
   agreement beyond the metric-position prior? No ruling asked; fit-phase.
7. **The product stance for densely low-strength boundaries.** Statement 23 will, on genuinely
   ambiguous music, produce many open-marked boundaries; the ruled record already owes a product
   stance for dense abstention (D-498), and the boundary axis inherits it. Would ask the user, at
   that design's sitting: "What does the user see where boundary after boundary carries an open
   mark?"
8. **Preset-dependence of committed boundaries.** Under the values-only rule (Statement 16) two
   presets may commit different boundaries on the same notes. Acceptable, or must segmentation be
   preset-invariant with only labels varying? The ruled record's inference-is-preset-independent
   entry (D-003) reads as presentation-scoped, so this session does not stretch it; the question is
   put rather than answered: "May the committed chord-spans differ between presets on the same
   score?"
9. **The 137 pairing defect (input finding, §2).** The staged 137 score (BWV 301, R 071) and the
   staged 137 analysis (*Wer Gott vertraut, hat wohl gebaut*) are different chorales. Before any
   comparison or grading uses the 137 pair, which chorale the pair should consist of needs a
   ruling; this session used the 137 analysis only as annotation-practice evidence and aligned
   nothing to the 137 score. Would ask now: "Which file is the intended member of the 137 pair —
   and is the snapshot suite's third Bach member the score or the analysis?"
10. **What three chorales could not test.** The staged sample is homorhythmic, four-voice, Baroque,
    Bach, with changes mostly at beats and eighths: it exercised held-tone membership, passing and
    neighbor tones, inversion boundaries, phrase marks, fermatas, anacrusis, and two-tradition
    disagreement — and could not exercise pedal points (none staged), arpeggiated or florid
    accompaniment textures, orchestral doubling, sparse two-voice textures, dense chromatic
    harmony, or any non-Baroque style. Statements whose premises name those cases (5, 10, 13, 20,
    21, 22) rest on theory and fetched research alone there, and their residual falsification
    clauses are where the exposure lives.

## 5. The sizing record

Every count below is a plain count over this document; every duration was measured by this session
with `date -u` timestamps written to a log file at the moment each block was finished (the log's
producer is the shell `date` utility; the log was written incrementally, never reconstructed).
Reading-phase boundaries additionally use the staged files' local arrival timestamps produced by
`stat` on the staged copies.

- **Statements: 26.** Open questions: 10.
- **Time, by measured phase (all times UTC, 2026-08-24, copied from the timestamp log after it was
  read back whole):** brief staged 06:22:54; boot pack staged 06:24:08; chorale analyses staged
  06:27:24; reading and research ended / derivation writing began 06:34:46 (so the whole read of
  pack + scores + analyses + six fetched sources measured 11 min 52 s from the brief's staging);
  the document preamble (§0–§2) took to 06:36:38; statements 1–5 to 06:37:56; 6–10 to 06:39:31;
  11–18 to 06:41:22; 19–22 to 06:42:32; 23–26 to 06:43:54; the open questions and these records to
  06:45:53. The 26 statements together therefore measured 7 min 16 s of session wall-clock
  (06:36:38 → 06:43:54), an arithmetic average of about 17 s per statement; the figure is
  wall-clock between the log writes bracketing each group. The statements were drafted from notes
  accumulated during the reading phase, whose 11 min 52 s is where most of the deriving actually
  happened — the two figures must be read together. No finer per-statement figure is claimed,
  because no per-statement stopwatch was run.
- **Share marked open: 1 of 26 statements** (Statement 18). **Share settled as to form but carrying
  an UNESTABLISHED measured component: 6 of 26** (Statements 8, 12, 14, 18, 20, 23). **Share whose
  sixth field could not be written (UNVERIFIABLE): 0 of 26** — every statement carries a CODE or
  RESIDUAL falsification.
- **Share this session would put to the user for a ruling: 0 of 26 statements** (none needs a
  ruling to stand as written) **and 4 of 10 open questions** (numbers 3, 7, 8, 9 — each carries its
  question verbatim above; number 9 is the one that should be put NOW, since it concerns a staged
  input pair a later comparison would otherwise trust).
- **The noise measurement — what each statement actually consulted.** Pack file 05 (the ratified
  design intent) was consulted by 19 of 26 statements (all except 1, 2, 3, 4, 5, 14, 26). Pack
  file 02 (principles and conventions) was consulted by Statement 18 (principle #17b) and
  Statement 24 (principle #21 beside D-474). Pack file 06 (defect types) by Statement 8 (DT-2).
  Pack files 00, 01, 03 and 04 were consulted by NO statement — they governed this document's
  conduct and form (the reading order, the FACT/THEORY/CONJECTURE discipline, the writing
  standards, the figures-by-citation rule) and contributed no content to any statement. Fetched
  source 1 (Pardo–Birmingham) was consulted by Statements 1, 3, 6, 8, 11, 13, 19, 22; source 2
  (Masada–Bunescu) by 1, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 19, 20 and Open question 4; source 3
  (Temperley) by 3, 6, 8, 10, 11, 14, 15, 18, 20 and Open question 6; source 4 (AugmentedNet) by
  Statement 1; source 5 (AnalysisGNN) by NO statement — it was read as background on the current
  state of the field and contributed no load-bearing claim; source 6 (When in Rome corpus paper) by
  Statement 24. The staged score and analysis files were consulted by Statements 1, 2, 3, 4, 5, 7,
  10, 12, 14, 20, 23, 24, 26 and §2's input finding.

## 6. The independence record

**Opened, in full:** the dispatching brief; all seven boot-pack files (00 through 06), each read
whole; all eight staged score/analysis files (three `.mscx` scores — read at their title blocks and
at the bars cited in §3, with the 001 score read across its opening bars; five RomanText analysis
files, each read whole); the six fetched sources of §2, plus the one low-yield page noted there.
**No pack file was left unopened. Nothing else in the repository was opened**: no specification, no
handoff, no status file, no register, no code. Before any folder access was granted, locating the
brief returned a names-only listing of the repository root's folder names (no file names, no
contents); that listing is the only view of the repository this session had outside the reads named
above. The session's persistent cross-session memory store was deliberately not read at any point,
so nothing could reach this session from earlier sessions' notes by that route. No build, test,
measurement tool or repository script was run; the only executions were `date`/`stat` timestamp
logging in the session workspace and the file deliveries the dispatching brief's §7 orders.

**The stop-on-meeting record.** No passage stating how THIS project's analysis currently decides
chord boundaries, or ranks evidence for that decision, and no passage recognizable as the user's
ruled answer to the subject, was met anywhere in the pack, the brief, or the staged files — the
positive statement the brief requires. Three disclosures are recorded so that the blindness is
judged rather than assumed:

1. Pack file 02, inside the phase-3 gate qualification (the block beginning "QUALIFICATION — PHASE
   3 WAITS…"), names an open-item family called "struck-versus-sounding" and asks whether an item's
   search space "could … contain a fact about (a) what the decoder or the emission READS — struck
   versus sounding tones, note counting, pitch representation — or (b) how candidates are
   ADMITTED?" This was read in full before its bearing was weighed. Judgment, recorded: it states
   that an UNSETTLED question family exists near this subject; it does not state what the analysis
   does or how evidence is ranked, so the stop clause's condition was judged not met and reading
   continued. What was learned from it — that struck-versus-sounding is contested territory in this
   project — did not source any statement above (Statements 3, 4 and 12 are defended from the
   fetched literature, the staged files and theory alone), but a comparison session should know the
   passage was seen.
2. Pack file 02 carries two in-place markers "[A PASSAGE IS WITHHELD FROM THIS PACK FOR THIS
   SUBJECT.]" (one following the never-work-from-memory convention, one following the
   defense-at-its-home convention). Only the markers were seen; no withheld content leaked, nothing
   was inferred from the markers' positions, and per the pack's read-me the identifier gaps in file
   05 were likewise treated as evidence of nothing.
3. Pack file 05's admitted entries describe the project's architecture at the level the generator
   admitted (a joint estimator, layers, carried alternatives, a decode). Statements above that rest
   on such entries cite them as SALVAGED by identifier, exactly as the brief's source-class field
   provides; the two entries closest to this subject that were admitted — D-525 (a semi-Markov
   objective) and D-527 (tone categories decided inside one decode) — are corroboration this session
   is REQUIRED to treat as ruled design intent, and Statements 6 and 19 also derive the same
   conclusions independently from the fetched literature so that the derivation does not rest on
   the salvage alone.

**The self-check, run on the finished text before delivery (the standing self-check the pack's
conventions demand, recorded rather than claimed).** The whole document was re-read after assembly
and seven defects were found and corrected in place before delivery: an overclaimed corpus check in
Statements 4 and 12 (a partial note-against-annotation check had been written as a five-file check;
narrowed to what was actually checked, with the general claim routed to Open question 2); a wrong
example in Statement 5 (a cited 003 change was not inversion-only; removed); a mislabeled ornament
in Statement 20 (the alto D of E–D–E is a lower neighbor, not a passing tone; corrected); a weak
span example in Statement 10 and an unverified rest claim in Statement 26 (both replaced with what
the staged files actually show); three bare non-musical uses of the word "score" (qualified to
"candidate score" per the reserved-word convention); and two miscounts in the noise measurement
(pack-file 05's consulted-by count and the staged-files list; recounted against the statements'
own citations). One earlier defect was caught during writing: a first draft of the sizing record
carried hand-typed group times that disagreed with the log (the DT-11 shape); it was corrected by
reading the log back whole and copying, and the correction is noted here so the record shows the
check fired.

*(End of the blind derivation. This file is the session's whole output; it is compared against the
withheld ruling by a separate later session, and nothing in it is to be read as a description of
what the project's analysis currently does.)*
