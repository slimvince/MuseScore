# Non-Chord-Tone Detection — Design Analysis

Date: 2026-04-26
Status: Strategic discussion. Deferred until LLM-triage corpus data
identifies which analyzer gaps NCT detection would actually address.

## What NCT detection would do

A non-chord-tone (NCT) is a note that sounds during a chord region
but isn't part of the chord's harmonic identity. Common types:
passing tones (PT), neighbor tones (NT), suspensions (SUS),
anticipations (ANT), appoggiaturas, escape tones, pedal tones,
chromatic neighbors, cambiata, échappée.

Today the analyzer doesn't distinguish chord tones from NCTs. It
labels everything sounding during a region as part of the chord.
This produces correct surface analysis (the chord literally
contains those pitches) but can diverge from traditional
analytical convention, which "reads through" passing material to
identify the structural chord.

Concrete example surfaced during Phase 5b verification: K.279/1 m7
beat 1 has a trill ornament including D# above a C major chord
region. The analyzer labels this `Cadd#9`. The score's editorial
Roman numeral analysis labels the same chord `I(add#9)`. So in
this specific case, the analyzer matches expert editorial
analysis. But in many other Classical/Baroque passages, similar
chromatic motion would be labeled by editors as a passing tone
and rendered as plain `I` rather than `I(add#9)`. The convention
gap is real.

## What good NCT detection requires

Real NCT detection isn't a small fix. Four requirements:

1. **Voice-leading tracking.** Most NCTs are identified by
   stepwise approach AND stepwise resolution within a single
   voice line. Requires durable voice tracking across chord
   boundaries — the analyzer doesn't currently track voices as
   entities.
2. **Metric weighting.** NCTs typically fall on weak beats,
   chord tones on strong beats. The analyzer has time-signature
   data but doesn't currently consult metric position when
   scoring chord-tone candidates.
3. **Style awareness.** A `#9` in Mozart is almost always
   passing/neighbor; a `#9` in bebop is structural altered-dominant
   tension. Naive NCT detection misclassifies based on style.
   Style-aware detection conflicts with the chord-symbol-ban
   principle if it requires reading user-written analytical
   content; structural cues (instrumentation, tempo, key signature
   density) might be defensible signals.
4. **Probabilistic output.** NCT identification is inherently
   uncertain. Boolean classification is brittle; confidence-weighted
   classification is what real analyzers (music21's various tools,
   the DCML team's analyses) use.

## Architectural fit

Two viable shapes:

**Shape A — NCT-aware chord identification.** The chord-ID logic
itself becomes smarter about distinguishing chord tones from NCTs.
Output is still "maximal" in the sense that it accurately reflects
what the analyzer concludes — it just concludes differently because
it's now better at the underlying classification. Consistent with
the no-stripping-in-production principle: the analyzer produces
what it sees, but it sees more accurately.

**Shape B — NCT-based output smoothing layer.** Post-analysis
filter that strips alterations identified as NCTs. **Banned** —
violates the no-stripping-in-production principle (same category
as extension stripping). Rejected for the same reasons.

Shape A is the right architectural fit if NCT detection is
pursued.

## Quality impact estimate

**On the synthetic test catalog (composing_tests):** Modest. The
remaining RealDiff entries (post-stripping, post-viiø-fix, post-b9/#9-fix)
are mostly representational gaps (special notations like `C7alt`,
`CPhryg`, `CTristan`, `Cm9b5`) plus a couple of sus4/triad cases
that might benefit from suspension detection. So at most ~2
entries shift. Not transformational on this metric.

**On real-music annotations against editorial Roman analysis:**
Where NCT detection genuinely helps. Most Classical/Baroque corpus
contains NCT-rich textures (passing tones in voice leading,
neighbor figures, suspensions at cadences). The current analyzer
over-labels these as chord-tone alterations. NCT detection would
produce annotations closer to traditional Roman numeral
conventions: `I — IV — V — I` instead of `I — I(add6) —
IV(add#11) — V(add9) — I`-style strings.

**On jazz / extended-harmony idioms:** Risk of regression. What
looks like a passing tone in Classical is often structural
extension in jazz. A naive CPE-tuned NCT detector would strip
genuine `b9` and `#11` colorings on dominant chords. Style-awareness
becomes load-bearing.

**On chord-ID consistency:** Modest improvement. Same music in
slightly different voicings should produce same chord ID; NCT
detection stabilizes this if voice-leading context is consistent.

**On downstream features (cadence, pivot, key inference):**
Indirect improvement. All consume chord-ID output; cleaner chord
IDs propagate. Cadence detection particularly — suspensions are
NCT-by-construction, and proper suspension detection cleans up
cadence output significantly.

## Why defer

Three reasons to defer until LLM-triage corpus data is available:

1. **The current 5 remaining RealDiff entries don't depend on
   NCT detection.** None of the 4 special notations are NCT-related;
   only the 2 sus4/triad cases might benefit. So NCT detection
   wouldn't move the composing_tests baseline meaningfully.
2. **LLM-triage provides cheaper quality signal.** LLMs have
   internalized enough music theory to recognize "this `Cadd#9`
   is just a trill ornament" patterns. Running LLM-triage on real
   corpus would surface *where* NCT detection would help — before
   we invest in implementing it. That data also tells us which
   style assumptions to bake into the detector.
3. **The current state is already analytically valid.** K.279/1
   m7 verification showed the analyzer matching expert editorial
   Romans beat-for-beat. Without empirical data showing real-world
   over-labeling, we'd be implementing NCT detection on
   speculation.

## Sequencing

If/when NCT detection is pursued:
1. LLM-triage workflow runs on real corpus, produces a "categories
   of analyzer gaps" report.
2. From that report, decide whether NCT detection is the
   highest-leverage next investment vs. alternatives (better key
   inference for non-CPE styles, better extension recognition for
   jazz, better chromatic-harmony handling, etc.).
3. If pursued: voice-tracking infrastructure → metric-weighting
   integration → simple PT/NT detection → measurement →
   broader NCT vocabulary. Probably 3-5 CC sessions for v0.
4. Style-awareness as a follow-up rather than v0 — start with
   CPE-tuned detection, observe behavior on jazz/extended corpus,
   add style configuration if regressions are real.

## Voice-leading detection — the piano problem

A specific complication for NCT detection in our actual use case:
much user-facing analysis runs on piano scores where multiple
voices are played by a single hand on a single staff. Voice
tracking is harder than in orchestra scores.

Cases ranked by tractability:

1. **Distinct instruments (orchestra, string quartet).** Voice
   per instrument. Trivial.
2. **Distinct MuseScore voice slots.** MuseScore stores up to 4
   voices per staff. If the composer used voice slots correctly,
   voices are explicit. *But* many users put everything in voice
   1, especially in piano scores.
3. **Single voice slot, polyphonic content (typical piano).**
   All notes in one voice slot. Voice membership must be inferred
   from: stem direction, register, onset timing, beam grouping,
   rhythmic continuity, sustained-note tracking.

For the typical piano case, hybrid strategy:

- **Use voice-slot data when present.** Voice slots are
  structural notational metadata (analogous to time signature),
  not analytical interpretation — reading them is consistent with
  the chord-symbol-ban principle.
- **Use stem direction within voice slot 1.** Up-stem vs.
  down-stem on the same staff often signals separate voice
  candidates. Bach chorale convention.
- **Use staff boundaries.** Piano treble vs. bass staff are
  typically separate voices, with hand-crossing as a known
  exception.
- **Fall back to register-based inference** when structural cues
  don't give clean separation. Notes in similar register moving
  stepwise → likely same voice. Onset-aligned notes → likely
  chord or same-rhythm group. Tied notes → continue voice.

The structural-data approach is consistent with the analyzer's
existing architecture: it consumes notes + structural metadata
(key signature, time signature, ties, pedal) and infers analytical
content. Voice slots and stem direction belong in the same
"structural metadata" category — already in the score, not
user-written analytical claims.

Inference falls back to harder territory but isn't fundamentally
different from existing inference work (boundary detection, key
detection, etc.).

## Open questions

- How accurate is voice-slot usage in real-world MuseScore scores?
  If most users don't use slots properly, the structural-data
  approach has limited reach.
- How well does the engraving layer's existing voice/stem logic
  cope with edge cases (cross-staff playing, voice crossings)?
  The composing module would consume engraving's voice
  determinations — those need to be reliable.
- For sparse textures (single line, lead sheets), voice tracking
  is trivial but NCT detection has weak evidence to work with.
  How does NCT detection degrade gracefully when voice context is
  thin?
- Style detection without reading user-written analytical content
  is a real constraint. Instrumentation cues (lead sheet vs. full
  orchestral score), tempo markings, and key-signature density
  might be enough — but verification would need empirical work on
  real corpora across style boundaries.

## Decision

Deferred. Re-visit after LLM-triage workflow has produced
empirical data on where the analyzer's real-world output diverges
from expert analysis. That data turns NCT detection from a
speculative improvement into a targeted one.
