# The ARM and the SITE for the framework document's nine behavioural statements

> **WORKING ARTIFACT — NOT A GOVERNING DOCUMENT. IT RULES NOTHING.**
>
> Written 2026-08-28 by CC under `cc_instruction_arm_and_site_fillin.md`, which is the named later act
> of Ruling 4 of `cowork_rulings_2026_08_26_framework_opening_sitting.md`: the framework phase's
> statements carry sub-fields 3, 4 and 5, and a side allowed to read code adds sub-field 1 (the ARM)
> and sub-field 2 (the SITE) afterwards.
>
> **★ THIS BATCH BINDS. IT DOES NOT GRADE.** Naming where a statement binds is this file's work.
> Deciding whether the code SATISFIES a statement is specification-against-code, which the user's
> ruling of 2026-08-15 reserves to the AUDIT as evidence. Where binding surfaced a disagreement, it is
> recorded below as a **QUARANTINED AUDIT QUESTION** — stated once, unresolved, not investigated, not
> measured, and nothing corrected on account of it. They are also gathered together at the end.
>
> **★ WHY THIS IS A SEPARATE FILE AND NOT AN EDIT TO THE FRAMEWORK DOCUMENT.**
> `cowork_framework_document_draft_2026_08_28.md` is another side's unratified draft and this batch is
> barred from editing it — not one character was changed, and its blob was pinned before anything was
> read and re-checked at the end. **Whether this fill-in is later folded into that document is the
> user's call at ratification and is NOT this batch's to take.**
>
> **★ WHAT IS BOUND AGAINST.** The nine behavioural statements **B1 to B9** at §10.2 of the framework
> document. No statement is re-typed here; each is cited to §10.2 by its identifier and named by its
> subject in one line (**D-431** — a text enters by citation, not transcription).
>
> **★ HOW SITES ARE NAMED.** By file and by function or type, **never by line number** (**D-307** — a
> line number quoted in prose goes stale on the next insertion above it).
>
> **★ THE TWO ARMS, AS THE RECORD DEFINES THEM.** **JOINT** — the joint estimator, the production
> inference on the batch/corpus surface (`batch_analyze --joint-inference`) and, since the 2026-07-27
> notation switch, on the in-app notation surface (`useJointNotationRecord` defaults ON). **LEGACY** —
> the stage-by-stage path it replaced, compiled and dormant, selected only by an explicit `false`,
> awaiting deletion at the OI-180 retirement map. Both were re-established at the files in this
> session; `CLAUDE.md` gate block (A) is where the arm status is homed.

---

## B1 — a harmonic boundary falls only at a change point

**Statement.** §10.2, **B1**: harmonic boundaries against the change-point set.

**SUB-FIELD 1 — THE ARM: BOTH, and it binds differently on each.** On the JOINT arm one module
produces both terms of the statement — the change points and the segment boundaries read off them —
so the containment is structural. On the LEGACY arm the two terms are produced by **different
modules**: the change-point set is the slicer's, and the harmonic boundaries come from the
segmenter and from two later sub-boundary passes, so the containment is not settled by construction.

**SUB-FIELD 2 — THE SITE.**

*JOINT:*
- `src/composing/analysis/joint/jointfactadapter.cpp`, `buildAdapterFacts` — builds the **event
  lattice**: the boundary set is the sorted-unique union of every notated onset and every notated
  note end over the adapter's notes, and the events are the consecutive boundary pairs. This is the
  joint arm's change-point set.
- `src/composing/analysis/joint/jointdecoder.cpp`, `decodePiece` — a decoded segment's `startTick` and
  `endTick` are read from `Piece::events` at the segment's own first and last event indices, so a
  published harmonic boundary is an event boundary by construction. The carrier is
  `SegmentSummary` (`src/composing/analysis/joint/jointdecoder.h`).

*LEGACY:*
- `src/composing/analysis/slicing/slicer.cpp` / `.h`, `changePointSlices` — the change-point set: the
  sorted-unique union of every onset and every release of an eligible note, clipped to the loaded
  span.
- `src/composing/analysis/harmony/harmonicsegmenter.cpp`, `greedyExpandSegmentation` and
  `placedRegionsToTicks` — the coarse harmonic boundaries under the production (`Smoothed`)
  granularity.
- `src/composing/analysis/region/regionanalyzer.cpp`, `denseBoundaryTicks` — the coarse boundaries
  under the `PreserveAllChanges` granularity (a boundary at every pitch-class-set change between
  adjacent chord-rest segments).
- `src/composing/analysis/region/regionanalyzer.cpp`, `analyzeRegions` — the Pass 2 onset-Jaccard
  sub-boundary pass, the Pass 2b iterative bass-movement sub-boundary pass, and `absorbShortRegions`,
  which together add and remove boundaries after Pass 1.

**HOW YOU FOUND IT.** Read `slicing/slicer.h` whole (its header states the change-point contract);
then grepped `regionanalyzer.cpp` for `boundaries|greedyExpandSegmentation|denseBoundaryTicks|Pass 1`
to find the boundary producers, and `jointdecoder.cpp` for `startTick|endTick` to find where a joint
segment's ticks come from; `jointfactadapter.cpp` was read at its event-lattice block, located by
grepping the file for `event|lattice|onset|offset`.

**REACHABLE? REACHED**, on both arms. Each arm has a named producer for both terms of the statement.

**QUARANTINED AUDIT QUESTION.** On the LEGACY arm the harmonic-boundary producers
(`greedyExpandSegmentation`, `denseBoundaryTicks`, the Pass 2/2b sub-boundary passes,
`absorbShortRegions`) do not consume `changePointSlices`, so whether every legacy harmonic boundary
is a member of that arm's change-point set is not settled by construction. Unresolved.

---

## B2 — a tonality change coincides with a harmonic boundary

**Statement.** §10.2, **B2**: the published tonality per span, across consecutive spans.

**SUB-FIELD 1 — THE ARM: BOTH, and it binds differently on each.** On the JOINT arm the tonality is
part of the decoded segment's own state, so one span carries exactly one tonality by construction.
On the LEGACY arm the tonality is decided at a **finer grain than the harmonic span** — per slice —
and is then reduced to one tonality per region by a duration-majority rule, so the statement holds of
the published surface only after that reduction.

**SUB-FIELD 2 — THE SITE.**

*JOINT:*
- `src/composing/analysis/joint/jointdecoder.cpp`, `decodePiece`, and the `SegmentSummary` carrier in
  `jointdecoder.h` (`tonicPc`, `isMajor`) — one tonality per decoded segment.
- `src/composing/analysis/joint/jointnotationrecord.cpp`, `computeModalReading` — assembles
  `ModalKeyRun`s as maximal runs of consecutive committed segments sharing one tonality.
- `src/composing/analysis/section/sectionanalyzer.cpp`, `groupKeyAreas` — the shared region-to-
  key-area grouping, reached from the record arm through `analyzeSectionFromRecord`.

*LEGACY:*
- `src/composing/analysis/key/keymodesequence.cpp`, `KeyModeSequenceDecoder::decode` (and
  `redecodeRange`) — the per-slice tonality sequence, carrier `SliceKeyMode`
  (`keymodesequence.h`).
- `src/composing/analysis/region/regionanalyzer.cpp`, `analyzeRegions` — the `localKeyForRegion`
  reduction (duration-majority over the region's slice run) and `inheritRegionKeyContext`, which
  propagate one tonality per region onto `HarmonicRegion::keyModeResult`.
- `src/composing/analysis/section/sectionanalyzer.cpp`, `groupKeyAreas`, and the key-island
  stabilization block of `analyzeSection` (skipped when `jointKeyWiringEnabled()` is set; that
  switch is default OFF, `src/composing/analysis/section/jointkeydecision.cpp`).
- `src/composing/analysis/region/regionanalyzer.cpp`, the J-key-iii re-key pass in `analyzeRegions`,
  which overrides `region.keyModeResult` — gated on `jointKeyWiringEnabled()`, default OFF.

**HOW YOU FOUND IT.** Grepped `regionanalyzer.cpp` for `localKeyForRegion` and read the surrounding
reduction and its declared contract; read `keymodesequence.h` whole at its `SliceKeyMode` and decoder
declarations; grepped `src/composing/analysis/section` for `groupKeyAreas|detectCadences` to find the
shared grouping; grepped `src` for `jointKeyWiringEnabled` to establish the default.

**REACHABLE? REACHED**, on both arms.

**QUARANTINED AUDIT QUESTION.** On the LEGACY arm a slice-level tonality change inside a region is
collapsed by `localKeyForRegion`'s duration-majority rule, so a tonality change that does **not**
coincide with a harmonic boundary cannot appear on the published surface. Whether that satisfies B2
or removes its falsifier is unresolved.

---

## B3 — every sounding note of a span carries a chord-tone assignment

**Statement.** §10.2, **B3**: the per-note assignment against the span's sounding-note set.

**SUB-FIELD 1 — THE ARM: BOTH, and it binds differently on each — but on neither arm is the
assignment a PUBLISHED fact.** On the JOINT arm a per-note category is computed inside the content-
score arithmetic and is not carried out of it. On the LEGACY production path no per-note assignment is
computed at all — the scorer works over pitch-class-aggregated tones; a per-note chord-tone-versus-
non-chord-tone decision exists in a **compiled but unwired** Layer-4 per-slice module, and it reduces
its answer to pitch classes rather than keeping it per note.

**SUB-FIELD 2 — THE SITE.**

*JOINT (computed, not published):*
- `src/composing/analysis/joint/jointprimitives.cpp`, `noteCategory` — classifies one note's pitch
  class against the candidate chord's member set as `member` / `within` / `outside`.
- `src/composing/analysis/joint/jointdecoder.cpp`, `segmentContentScore` — the only caller: it walks
  `Piece::notesByEvent` over the segment's events and feeds each note's category to
  `FittedAdapter::emissionLogp` (`src/composing/analysis/joint/jointadapter.h`). The category is
  consumed as a content-score term and is not retained.
- `src/composing/analysis/joint/jointnotationrecord.h`, `RecordSegment` — what IS published per
  segment: `members` / `memberPcs` (the chord's own member pitch classes) and `bassPerEvent` (the
  bass's factor role per event). There is no per-note assignment field.

*LEGACY:*
- `src/composing/analysis/types/analysistypes.h`, `ChordAnalysisTone` — the production scorer's tone
  record. It is pitch-class-aggregated and carries no chord-tone/elaboration field.
- `src/composing/analysis/chord/chordslicedecoder.cpp` / `.h`, `ChordSliceDecoder::classifyMembership`,
  `MembershipResult`, and `SliceChord::chordTonePcs` / `SliceChord::nonChordTonePcs` — the per-note
  chord-tone-versus-non-chord-tone ladder over `FocalNote`s, reduced to pitch classes on the result.
  **Its own header declares it not wired into the live analysis pipeline**, exercised only under the
  read-only `batch_analyze --decode-chords` diagnostic.

**HOW YOU FOUND IT.** Grepped `src/composing` for
`chordTone|nonChordTone|isChordTone|nct` and for `passing|neighbour|suspension|anticipation|ornament|
elaborat` (case-insensitive) — the first sweep returned only unrelated matches on the production
path, which is itself the finding; then grepped for `noteCategory` and `emissionLogp` to locate the
joint arm's computation and its single caller; read `chordslicedecoder.h` whole, which is where the
membership ladder and its isolation declaration are stated.

**REACHABLE? AMBIGUOUS**, and the two readings are named because the binding turns on which is meant.
**Reading (a)** — *assignment* = the per-note category the analysis computes while deciding: a site
exists, on the JOINT arm, at `noteCategory` / `segmentContentScore`. **Reading (b)** — *assignment* =
a published per-note fact whose totality can be observed against the span's sounding-note set, which
is how §10.2 writes B3's observable: **no site on either arm.** This entry does not choose between
them.

**QUARANTINED AUDIT QUESTION.** On the JOINT arm the category is computed over the notes whose
**onset** falls in one of the segment's events (`Piece::notesByEvent`), not over the notes **sounding**
across the span, so a note held in from an earlier segment carries no category in the segment it
sounds through. Whether that meets B3's "every sounding note" is unresolved.

---

## B4 — the published chord symbol agrees with the tonality and degree it was derived from

**Statement.** §10.2, **B4**: the root pitch class against the tonic transposed by the degree's
interval.

**SUB-FIELD 1 — THE ARM: BOTH, and the two arms compute the statement's two sides in OPPOSITE
DEPENDENCY ORDER.** On the JOINT arm the root is **derived from** the tonality and the degree, and the
chord symbol from that root, so B4's equality is true by construction. On the LEGACY arm the root is
**decided from the notes** by the scorer and the **degree is derived from it**, so the two sides are
produced in the reverse order and the equality is not structural.

**SUB-FIELD 2 — THE SITE.**

*JOINT:*
- `src/composing/analysis/joint/jointprimitives.cpp`, `frameworkAndRoot`, `chordFactorPcs` and
  `rootSpellingLof` — the root and its tonal spelling derived from the label class together with the
  segment's tonic and mode. `rootSpellingLof`'s own declaration states that its pitch class equals
  the decoder's root pitch class by construction.
- `src/composing/analysis/joint/jointrender.cpp`, `jointChordSymbol` — the symbol string, built from
  that root's canonical spelling plus the class's quality.
- `src/composing/analysis/joint/jointnotationrecord.cpp`, `assembleNotationRecord` — stores
  `RecordSegment::rootPc`, `rootSpellingLof` and `chordSymbol` on the notation surface.
- `tools/batch_analyze.cpp`, `writeJointInferenceJson` — the batch/corpus surface: emits
  `rootPitchClass`, `chordSymbol` and `romanNumeral` from the same shared render primitives.

*LEGACY:*
- `src/composing/analysis/chord/chordanalyzer.cpp`, `buildChordResult` — its "Degree assignment"
  block searches the key's scale for the **already-decided** root pitch class and sets
  `ChordFunction::degree` (leaving it at −1 when no scale member matches), and its diatonic check
  follows.
- `src/composing/analysis/chord/chordsymbolformatter.cpp`, `ChordSymbolFormatter::formatSymbol` and
  `ChordSymbolFormatter::formatRomanNumeral` — the published symbol and numeral, rendered from
  `ChordIdentity::rootPc` / `rootTpc` and from `ChordFunction`.

**HOW YOU FOUND IT.** Read `jointprimitives.h` and `jointrender.h` whole for the derivation chain;
grepped `chordanalyzer.cpp` for `buildChordResult|function.degree =|diatonicToKey` and read the
degree-assignment block that returned; grepped `chordsymbolformatter.cpp` for
`^std::string ChordSymbolFormatter::` to name the two rendering entry points.

**REACHABLE? REACHED**, on both arms.

**QUARANTINED AUDIT QUESTION.** On the LEGACY arm `ChordFunction::degree` is −1 whenever the decided
root is not a member of the mode's scale, so for those spans B4's equality has no left-hand side to
test. Unresolved.

---

## B5 — no published fact of a later layer changes a published fact of an earlier one

**Statement.** §10.2, **B5**: the facts published at each layer, compared before and after the later
layer runs.

**SUB-FIELD 1 — THE ARM: BOTH, and it binds differently on each.** On the JOINT/record arm every
consumer of the decode is declared a pure function of what the decode published, so the statement
binds to the **absence** of a mover. On the LEGACY arm there are several named movers, of which two
run in production, two are switched off by default and two are dormant.

**SUB-FIELD 2 — THE SITE.**

*JOINT / record arm:*
- `src/composing/analysis/joint/jointnotationrecord.cpp`, `assembleNotationRecord` — declared score-
  decode-independent: it consumes the already-computed piece and decode result, never re-decodes and
  never reads the score.
- `src/composing/analysis/section/sectionrecordadapter.cpp`, `analyzeSectionFromRecord`,
  `regionFromRecordSegment` and `chordResultFromRecordSegment` — declared consumers of the published
  record that never re-decode, never invoke the legacy analysis and compute no inference; one record
  segment maps to one region, one-to-one.
- `src/composing/analysis/section/sectionanalyzer.cpp`, `groupKeyAreas` — shared with the legacy arm;
  it writes `AnalyzedRegion::keyAreaId` back onto the regions it groups.

*LEGACY:*
- `src/composing/analysis/function/harmonicfunctionlayer.cpp`, `applyHarmonicFunction` — the
  progression-signal terms enter the chord competition and can move the winner.
- `src/composing/analysis/chord/postscoringgates.cpp`, `applyPostScoringGates` — the post-scoring
  gates move the committed chord after the competition has selected one.
- `src/composing/analysis/region/regionanalyzer.cpp`, `backfillNextRootPc` — writes
  `ChordFunction::nextRootPc` into regions already analyzed.
- `src/composing/analysis/region/regionanalyzer.cpp`, the J-key-iii re-key pass in `analyzeRegions`,
  and `src/composing/analysis/section/sectionanalyzer.cpp`, the key-island stabilization in
  `analyzeSection` — both keyed off `jointKeyWiringEnabled()`
  (`src/composing/analysis/section/jointkeydecision.cpp`), default OFF.
- `src/composing/analysis/function/forwardoverride.cpp` / `.h`, `overrides`, `overrideBar` and
  `OnePassClosure::tryOverride` together with its localized forward recompute — **the** mechanism the
  record specifies for a later layer overturning an earlier one. Its own header declares it has no
  production consumer.
- `src/composing/analysis/grouping/groupinglayer.cpp`, `assembleGrouping` — declared additive and
  read-only over the layer beneath it, and declared to have no production consumer; its header names
  `detectCadences` / `detectPivotChords`
  (`src/composing/analysis/section/sectioncadencedetection.cpp`) and the key-area grouping as the
  live paths it would retire.

**HOW YOU FOUND IT.** Read `jointnotationrecord.h` and `sectionrecordadapter.h` whole for the record
arm's declared purity; read `forwardoverride.h` and `groupinglayer.h` whole for the two named
override/assembly mechanisms and their dormancy declarations; grepped `src` for
`jointKeyWiringEnabled` and `assembleGrouping` to establish which paths are reachable in production.

**REACHABLE? REACHED**, on both arms.

**QUARANTINED AUDIT QUESTION.** `groupKeyAreas` writes `keyAreaId` back onto `AnalyzedRegion`s that
an earlier stage has already produced, on **both** arms. Whether writing a back-reference onto an
earlier layer's published object counts as changing a published fact is unresolved.

---

## B6 — where rivals are published, the committed reading is among them and carries the greatest mass

**Statement.** §10.2, **B6**: the rival set and the committed reading, by membership and by ordering
on mass.

**SUB-FIELD 1 — THE ARM: BOTH, and it binds differently — including between the JOINT arm's two
production surfaces.** On the JOINT arm rivals are published on the **notation** surface as two
re-scoring axes, and **not at all** on the batch/corpus surface, where the rival array is emitted
empty for every region. On the LEGACY arm rivals are the chord scorer's ranked candidate list and the
tonality decoder's surviving candidates, both carried on the region.

**SUB-FIELD 2 — THE SITE.**

*JOINT, notation surface:*
- `src/composing/analysis/joint/jointdecoder.cpp`, `computePosteriorSlice` — builds
  `SegmentSlice::keyAxis` and `SegmentSlice::chordAxis` (`jointdecoder.h`, `PosteriorAxis`): parallel
  label and content-score arrays with `committed` an index into them, so membership of the committed
  reading is structural.
- `src/composing/analysis/section/sectionrecordadapter.cpp`, `recordAlternatives` and
  `regionFromRecordSegment` — project the chord axis onto `AnalyzedRegion::alternatives`, ranked by
  content score descending, with the committed entry dropped because it is the region's
  `chordResult`.

*JOINT, batch/corpus surface:*
- `tools/batch_analyze.cpp`, `writeJointInferenceJson` — emits a literal empty `alternatives` array
  for every region. No rival set is published on that surface.

*LEGACY:*
- `src/composing/analysis/region/harmonicrhythm.h`, `HarmonicRegion::alternatives` and
  `HarmonicRegion::keyAlternatives`, filled in `src/composing/analysis/region/regionanalyzer.cpp`
  (`analyzeRegions`, and the `RegionKeyReduction` that carries the region-level candidate-tonality
  menu).
- `src/composing/analyzed_section.h`, `AnalyzedRegion::alternatives` and `appendCappedAlternatives` —
  the per-consumer projection of the one carried list.
- `src/composing/analysis/key/keymodesequence.h`, `SliceKeyMode::alternatives`, produced by
  `KeyModeSequenceDecoder::decode`.
- `src/composing/analysis/decode/chordpathdecoder.h`, `ChordPathNode::alternatives` and
  `winnerMargin` — declared inert at beam 1, nothing reads the accumulated path.

**HOW YOU FOUND IT.** Grepped `src/composing/analysis` for `alternatives` to enumerate every carrier;
read `computePosteriorSlice` in `jointdecoder.cpp` to see how the committed index is set on each axis;
grepped `sectionrecordadapter.cpp` for `alternatives|committed|chordAxis|keyAxis` and read the
projection; read `writeJointInferenceJson` in `tools/batch_analyze.cpp`, reached by grepping that file
for `joint-inference`.

**REACHABLE? REACHED**, on both arms.

**QUARANTINED AUDIT QUESTIONS.** *(i)* Both joint posterior axes re-score the **committed span** under
alternative labels, so the committed reading's own within-segment content score need not be the
maximum on either axis — the decode optimizes the whole path, not the segment. Unresolved. *(ii)* On
the batch/corpus surface the published rival set is unconditionally empty, not empty because the
reading is uncontested. Unresolved.

---

## B7 — a rival that differs in segmentation is published as such

**Statement.** §10.2, **B7**: the boundaries of each rival against the committed segmentation.

**SUB-FIELD 1 — THE ARM: NEITHER.** No arm publishes a rival that carries boundaries of its own, so
the statement has no arm to bind to. This is the one statement that binds identically on the two arms
— namely, nowhere.

**SUB-FIELD 2 — THE SITE: NO SITE.** Every rival carrier found is a set of alternative **labels over
the committed span**:

- `src/composing/analysis/joint/jointdecoder.cpp`, `computePosteriorSlice` — both axes re-score the
  committed span `[i, j)`; the key axis varies the tonality with the class fixed, the chord axis
  varies the class with the tonality fixed. Neither varies `i` or `j`.
- `src/composing/analysis/joint/jointdecoder.h`, `PosteriorAxis` — parallel `labels` and `scores`
  arrays and a `committed` index. There is no boundary field.
- `src/composing/analysis/region/harmonicrhythm.h`, `HarmonicRegion::alternatives`;
  `src/composing/analyzed_section.h`, `AnalyzedRegion::alternatives`;
  `src/composing/analysis/decode/chordpathdecoder.h`, `ChordPathNode::alternatives` — all
  `ChordAnalysisResult` lists, and `ChordAnalysisResult`
  (`src/composing/analysis/chord/chordanalyzer.h`) carries an identity and a function and no ticks.
- `src/composing/analysis/key/keymodesequence.h`, `SliceKeyMode::alternatives` — alternative
  tonalities for one slice of a fixed slice grid.
- `src/composing/analysis/harmony/harmonicsegmenter.h`, `PlacedRegion` with `round == 0` — the one
  place where *unchosen candidate boundaries* exist at all. They are discarded inside
  `analyzeRegions` (`src/composing/analysis/region/regionanalyzer.cpp`), which takes only
  `round >= 1`, and `placedRegionsToTicks` likewise extracts only promoted regions. Nothing publishes
  them.

**WHAT WAS SEARCHED, so the NO SITE verdict can be re-run.** Grepped the whole repository, case-
insensitively, for `alternativeSegment|rivalSegment|altBoundar|segmentationAlternat|boundaryAlternat|
alternativeBoundar` — no files. Grepped `src` for `rival` — every hit was the substring inside
*arrival*, in cadence and grouping code. Grepped `src/composing/analysis` for `alternatives` and
opened every carrier the sweep returned (listed above). Grepped for `.round`/`round >= 1` to establish
what happens to the segmenter's unpromoted candidates. Read `computePosteriorSlice` to confirm both
axes hold the segment fixed, and `RawFanoutSummary` / `computeRawFanoutSummary`
(`src/composing/analysis/chord/chordanalyzer.h`) to confirm the fan-out diagnostic counts roots and
qualities, not boundaries.

**REACHABLE? NO SITE.** Reported as a finding, not as a failure. **No nearest plausible site was
invented**, and no statement was stretched to reach one.

---

## B8 — slices tile the working span exactly

**Statement.** §10.2, **B8**: the slice list, tested for covering, gapless and non-overlapping over
the loaded domain.

**SUB-FIELD 1 — THE ARM: BOTH, and it binds differently on each.** The LEGACY arm's slicer states
B8's property, including B8's own carve-out — an interior stretch where every eligible voice rests is
an **explicit empty slice**. The JOINT arm's event lattice **omits** an interval in which nothing
sounds rather than emitting an empty one.

**SUB-FIELD 2 — THE SITE.**

*LEGACY:*
- `src/composing/analysis/slicing/slicer.cpp` / `.h`, `changePointSlices` and the `Slice` type — the
  header states the covering, lossless, gapless, non-overlapping partition over the clipped loaded
  span, and states that an interior all-rest stretch is an explicit empty slice rather than an
  omission.

*JOINT:*
- `src/composing/analysis/joint/jointfactadapter.cpp`, `buildAdapterFacts` — the event-lattice block:
  boundaries are every notated onset and note end; for each consecutive pair the loop tests whether
  any note spans it and **continues past the pair when none does**, so an interval with nothing
  sounding produces no event.
- `src/composing/analysis/joint/jointdecoder.h`, `Piece::events` / `EventRec` — the carrier that
  results.

**HOW YOU FOUND IT.** Read `slicing/slicer.h` whole. For the joint arm, grepped
`jointfactadapter.cpp` case-insensitively for `event|lattice|onset|offset` and read the event-lattice
block it located.

**REACHABLE? REACHED**, on both arms.

**QUARANTINED AUDIT QUESTION.** The JOINT arm's event lattice drops a silent interval instead of
emitting an empty event, which is precisely the case B8's "not falsified by" clause describes as an
explicit empty slice. Whether the omission falsifies B8 on that arm is unresolved.

---

## B9 — every confidence crossing a layer boundary is bounded, class-declared and named to its decision

**Statement.** §10.2, **B9**: each value another layer may read, tested for the unit interval, a
declared class, and the decision it belongs to.

**SUB-FIELD 1 — THE ARM: BOTH, and this is the sharpest arm difference found.** The LEGACY arm
carries a bounded value produced by one shared sigmoid and an unbounded margin, each with its class
stated in prose at its own declaration. The JOINT/record arm carries **raw content-score differences
in nats, deliberately not remapped** — and puts one of them into a field whose own declaration states
the unit interval. On the batch/corpus surface the joint arm emits a **literal constant** where the
schema names a confidence. No code-level class tag exists on either arm; the class is stated in prose
at each field.

**SUB-FIELD 2 — THE SITE.**

*LEGACY:*
- `src/composing/analysis/key/keymodeanalyzer.h`, `normalizedConfidenceSigmoid` and
  `KeyModeAnalysisResult::normalizedConfidence` — bounded to the unit interval; its declaration states
  that it is an internal gate input and diagnostic export, **not** the layer-boundary confidence.
- `src/composing/analysis/key/keymodesequence.h`, `SliceKeyMode::confidence` and `uncertain`, produced
  by `KeyModeSequenceDecoder::decode` — the sequence margin, unbounded, named at its declaration as
  the layer-boundary confidence.
- `src/composing/analysis/region/harmonicrhythm.h`, `HarmonicRegion::keyConfidence` — the same margin
  carried to the region, with the class and the decision stated in the field's own comment.
- `src/composing/analyzed_section.h`, `KeyArea::confidence` and `AnalyzedRegion::hasAssertiveExposure`
  / `keyExposureBucket`, set in `src/composing/analysis/section/sectionanalyzer.cpp`.
- `src/composing/analysis/chord/chordanalyzer.h`, `ChordIdentity::score`, and
  `src/composing/analysis/decode/chordpathdecoder.h`, `ChordPathNode::winnerScore` /
  `winnerMargin` — unbounded ranking quantities.
- `src/composing/analysis/harmony/harmonicsegmenter.h`, `PlacedRegion::confidence` — the chord
  content score at placement time, internal to segmentation.
- Dormant, but stating the class at the field: `src/composing/analysis/chord/chordslicedecoder.h`,
  `SliceChord::confidence` and `SliceConfidence`; and
  `src/composing/analysis/voiceleading/textureclassifier.h` / `.cpp`, `TextureSpan::confidence` —
  the one value found that is **bounded in code** (`clamp01`) with its class named at its own
  declaration.

*JOINT / record arm:*
- `src/composing/analysis/joint/jointdecoder.h`, `PosteriorAxis::scores`, produced by
  `computePosteriorSlice` — weighted within-segment content scores in nats, published without
  remapping.
- `src/composing/analysis/section/sectionrecordadapter.cpp`, `keyAxisGap` and
  `regionFromRecordSegment` — the committed key axis entry minus the best other entry, placed into
  `AnalyzedRegion::keyModeResult.normalizedConfidence`; and the record-arm exposure constants
  `kAssertiveKeyExposureGap` / `kTentativeKeyExposureGap` in the same file, which the bucket is
  thresholded against instead of the legacy arm's unit-interval literals.
- `tools/batch_analyze.cpp`, `writeJointInferenceJson` — emits `keyConfidence` as a literal constant
  for every region.

**HOW YOU FOUND IT.** Grepped `keymodesequence.h` and `keymodeanalyzer.h` for
`confidence|margin` and read the declarations that returned; read `analyzed_section.h` and
`harmonicrhythm.h` whole at their confidence fields; grepped `sectionrecordadapter.cpp` for
`normalizedConfidence|keyExposureBucket|keyAxis` and read `keyAxisGap` and the two exposure
constants; grepped `src` for `ConfidenceClass|confidenceClass|Class-M|marginClass` to test whether any
code-level class tag exists — it does not, and the only hits were prose at field declarations, which
located the texture-span value.

**REACHABLE? REACHED**, on both arms.

**QUARANTINED AUDIT QUESTIONS.** *(i)* On the record arm an unbounded value in nats is carried in
`KeyModeAnalysisResult::normalizedConfidence`, a field whose own declaration states the unit interval,
and the fields are read through `AnalyzedRegion` by consumers of both arms. Unresolved. *(ii)* On the
batch/corpus surface `keyConfidence` is a literal constant and is not the confidence of any decision.
Unresolved. *(iii)* No confidence value carries a machine-readable class; the class is stated in prose
at each declaration, so B9's "class-declared" is not observable at an object. Unresolved.

---

## The quarantined audit questions, gathered

Stated once each, unresolved, **not investigated and not measured**. Each is reserved to the audit
under the user's ruling of 2026-08-15: a disagreement between specification and code is evidence for
the audit, and no document is corrected on the ground that the code says otherwise.

1. **B1** — on the LEGACY arm the harmonic-boundary producers do not consume `changePointSlices`, so
   the containment B1 asserts is not settled by construction there.
2. **B2** — on the LEGACY arm a slice-level tonality change inside a region is collapsed by the
   duration-majority reduction, so B2's falsifier cannot appear on the published surface.
3. **B3** — on the JOINT arm the per-note category is computed over notes **onsetting** in the
   segment's events, not over the notes **sounding** across the span.
4. **B4** — on the LEGACY arm the degree is −1 wherever the decided root is not in the mode's scale,
   so B4's equality has no left-hand side for those spans.
5. **B5** — `groupKeyAreas` writes a back-reference (`keyAreaId`) onto regions an earlier stage
   published, on both arms.
6. **B6(i)** — both joint posterior axes re-score the committed span, so the committed reading's own
   within-segment content score need not be the maximum on either axis.
7. **B6(ii)** — on the batch/corpus surface the published rival set is unconditionally empty.
8. **B8** — the JOINT arm's event lattice omits a silent interval instead of emitting an empty event.
9. **B9(i)** — the record arm carries an unbounded nat value in a field declared to be in the unit
   interval.
10. **B9(ii)** — the batch/corpus surface emits a literal constant where the schema names a
    confidence.
11. **B9(iii)** — no confidence carries a machine-readable class; the class is prose at the
    declaration.

*A twelfth observation, recorded here because it was met while binding and is not a
statement-versus-code disagreement:* three joint-module headers —
`src/composing/analysis/joint/jointfactadapter.h`, `jointdecoder.h` and `jointadapter.h` — carry the
declaration `DORMANT (no production consumer)`, while `buildAdapterFacts` is called by
`src/composing/analysis/joint/jointnotationproducer.cpp` and by `tools/batch_analyze.cpp`. It is
recorded, not acted on: no row is created and no file is edited by this batch.
