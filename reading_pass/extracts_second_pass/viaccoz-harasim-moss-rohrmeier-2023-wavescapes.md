# Second-pass extract — row 18: Viaccoz, Harasim, Moss & Rohrmeier 2023, Wavescapes

> **STATUS: SECOND INDEPENDENT EXTRACTION (session 2 of the reading pass, 2026-08-31).**
> Written under `cowork_reading_pass_commission_2026_08_30.md` §4, per the independence protocol
> of `reading_pass/continuation.md` §2. **Neither `reading_pass/extracts/` nor
> `docs/research_papers/reading_pass_2026_08/` was opened for this paper before this file was
> written.** Read at its source,
> `https://journals.sagepub.com/doi/full/10.1177/10298649211034906`, in two separately-prompted
> passes.
>
> **GRADE, DECLARED AT ITS FACE: RELAYED, not at-the-object.** Same web-fetch bound as the other
> second-pass extracts. Session-and-prompt independence, not read-tool independence — and see the
> row-17 cross-check §4 for this tool's two measured self-contradictions.

## Identity

Cédric Viaccoz, Daniel Harasim, Fabian C. Moss & Martin Rohrmeier, "Wavescapes: A visual
hierarchical analysis of tonality using the discrete Fourier transform", *Musicae Scientiae*
**27(2)**, pp. 390–427, June 2023 (online 17 January 2022), doi `10.1177/10298649211034906`.

**★ Two citation corrections to our own records, recorded not applied.** `reading_pass/additions.md`
already corrects the reachability report's venue from *JNMR* to *Musicae Scientiae* — that
correction is confirmed here. But it records the issue as **27(3)**, and the journal page states
**27(2), pp. 390–427**, twice on two separate reads. **Both belong to the bibliography
reconciliation the commission defers to its own act; this pass amends nothing.**

**Why this row is in the population:** R-7's third named unread alternative — *tonality in a
transform space rather than as a discrete label*.

## What kind of paper this is — stated first, because it governs everything below

**★ [FACT, established by a direct question] THERE IS NO EVALUATION.** Verbatim from the relay:
*"Explicitly none. The paper does not validate wavescape interpretations against ground truth,
listener judgments, or alternative analyses. Claims rest on musical-theoretical plausibility and
visual pattern interpretation."* Its evidence base is **eight compositions** — Josquin, Bach, Liszt,
Chopin, Scriabin, Webern, Coltrane, Ligeti.

**So, exactly as with row 17, this row can supply no measured value to any design point.** The two
alternatives R-7 names in this territory are both unevaluated visualisation methods.

## Claims, labeled

**[FACT] What a wavescape is.** A triangular arrangement of coloured cells, horizontal axis time in
equal-duration segments, vertical axis the hierarchical level — the base row single segments,
each row above aggregating more of them. Formally `W_k[m,n] = (C_k ∘ F ∘ P)[m,n]`, where `P`
aggregates pitch-class content from segment *m* to segment *n*, `F` applies the discrete Fourier
transform, and `C_k` maps the result to a colour.

**[FACT] The colour carries two quantities.** **Hue** encodes the **phase** φ_k of the chosen
Fourier coefficient, mapped circularly; **opacity** encodes the **normalised magnitude**
α = μ_k / X[0], the coefficient's magnitude divided by the zeroth coefficient.

**[FACT] What the transform is taken of.** A **12-dimensional pitch-class vector** per segment,
each entry the total **duration** of that pitch class in the segment. The DFT is
`X[k] = Σ_{n=0}^{11} x[n] · e^{−i2πnk/12}`.

**★ [FACT] WHAT THE COEFFICIENTS MEAN, IN THE PAPER'S OWN FRAME.** *"The DFT measures the prevalence
of even divisions of the octave in pitch-class sets."* Per coefficient: k=1 the chromatic circle
(singletons maximal); k=2 tritones; k=3 augmented triads and hexatonic scales; k=4 fully diminished
chords and octatonic scales; **k=5 diatonic scales and singletons, mapped along the circle of
fifths**; k=6 whole-tone scales. Coefficients 7–11 are conjugates of 5–1, so the paper works with
k ∈ [1…6], **selecting per piece by data** — *"we focus on those with the largest average normalized
magnitude."*

**★ [FACT] THE FIFTH COEFFICIENT'S PHASE IS READABLE AS A POSITION ON THE CIRCLE OF FIFTHS.**
Verbatim: *"The fifth coefficient maps these scales as well as the singletons along the circle of
fifths in counter-clockwise ascending order"*; diatonic scales *"span six fifths on this circle"*;
and, decisively, *"the phases for this diatonic scale and the singleton G are identical."*

**★ THE READING THAT MATTERS FOR R-7, STATED AS A BOUND RATHER THAN A CONCLUSION.** That last
sentence is the transform space's advertised advantage and its exposed edge at once: **the phase of
k=5 places a segment on the circle of fifths without committing to a key label — and it places a
DIATONIC COLLECTION and a SINGLE NOTE at the same phase.** The continuous representation therefore
carries collection-position information while carrying, at that coefficient, no distinction between
a scale and a note, and none at all between relative major and minor (both being the same
collection). **What that means for using such a space as a tonality representation is not settled by
this paper, which never asks the question.**

**[FACT] The stated case against keyscapes — and it is a scope argument, not an accuracy one.**
Verbatim: keyscapes *"have the shortcoming that they rely on a diatonic key-finding algorithm"*, and
*"the notion of a diatonic key is not equally applicable to pieces from all time periods or styles."*
The method *"does not rely on the concept of musical keys but only on the representation of tones as
pitch classes and thus reveals the tonal structure of a piece in a more general way"*, and is
claimed *"applicable to a wide range of Western musical styles, including the extended tonality of
the 19th century."* **No comparison of accuracy against a key-finding method is made — there is
nothing to compare, neither method being evaluated.**

**[FACT] The paper neither claims nor disclaims replacement of key finding.** Asked directly: it
substitutes *algorithms* — *"we substitute such algorithms by outputs of the DFT and use a color
mapping that exploits geometric properties of the Fourier space"* — and offers **no explicit
disclaimer** that wavescapes do not do what key finding does.

**★ [FACT] ENHARMONIC EQUIVALENCE IS AN EXPLICIT ASSUMPTION, NOT A LIMITATION THE PAPER FLAGS.**
Verbatim: *"A pitch class is the equivalence class of all octave-related pitches in 12-tone equal
temperament (C, C♯, D, D♯, E, F, F♯, G, G♯, A, B♭, B), assuming enharmonic equivalence."* **[sic] on
the mixed spelling in the paper's own list.** *(Note for the chain reading: this is the exact
information V3 measures the cost of discarding — Temperley 2002's 83.8% against 87.4% with spelling
— and this method discards it by construction at its input.)*

**[FACT] Some quantitative values exist, but they are descriptive, not evaluative.** Average
normalised magnitudes per piece and coefficient: Liszt *Faust Symphony* ᾱ₃ = 0.652, ᾱ₆ = 0.172;
Josquin *Ave Maria* ᾱ₅ = 0.61; normative baselines given as hexatonic ᾱ₃ = 1.0 and diatonic
ᾱ₅ ≈ 0.53. **These describe the pieces analysed; none is an accuracy.**

**[FACT of absence] Magnitude is NOT given an interpretive gloss.** Asked directly whether magnitude
is described as clarity, prototypicality or salience: it is not. The paper defines it geometrically —
*"the k-th Fourier coefficient can be described in polar coordinates by their magnitude µk (i.e.,
the distance to zero)"* — and leaves the interpretation to the analyst. **Anyone tempted to read
normalised magnitude as a confidence should note that the paper does not authorise it.**

**[FACT of absence] The effect of the base resolution r is NOT stated**, nor is any coefficient
named as best for common-practice tonality. Resolutions were chosen per piece *"according to the
time signatures of the pieces"* — quarter-note for the Liszt, one breve for the Josquin.

**[FACT] The analyst does the analysis.** Verbatim: *"the role of the analyst is thus focused on the
interpretation and contextualization of the results."* **No automatic segmentation, no key labels,
no ranked alternatives, and no metric for choosing among competing interpretations.**

**[FACT] Stated limitations, verbatim.** Keyscapes and by extension this method *"do not explicitly
provide a tree- or graph-structured analysis of the music"*; the method is *"a first approximation"*
and *"a first building block in the deeper understanding of hierarchical relations"*; and on
hierarchy generally, *"there have been many attempts to formalize Schenkerian's intuitions … however,
there are theoretical and practical difficulties for automatic hierarchical music analysis."*

**[FACT] Complementarity claimed with pitch scapes.** Verbatim: *"Their approach can therefore be
considered complementary to ours and wavescape visualisations might facilitate the interpretability
of pitch scapes"* (Lieck & Rohrmeier 2020).

**[FACT] There is an implementation.** A Python library at `https://github.com/DCMLab/wavescapes`,
taking MIDI, MusicXML or audio. **This pass did not open it.**

## Coupling facts (the commission's mandatory widening)

**ASSUMES upstream:** a symbolic score or an audio recording reduced to **duration-weighted
12-dimensional pitch-class vectors under enharmonic equivalence**, partitioned into equal-length
segments at a resolution chosen by hand from the time signature. **Spelling is discarded by
definition. Octave is discarded. No key, no chords, no boundaries, no meter beyond the resolution
choice.** Its input requirement is the lightest of anything in this population.

**HANDS downstream: a picture.** Per (level, position) cell, a hue and an opacity derived from one
chosen Fourier coefficient. **No segmentation, no labels, no alternatives, no confidence** — and
the paper explicitly assigns interpretation to the human analyst. The underlying complex
coefficients are of course computable and are a real continuous quantity a machine could consume;
**the paper simply does not define any consumer for them.**

**STATED SCOPE:** *"the tonality of Western music, considered in a broad sense as the hierarchical
organization of chords, scales and keys in pieces of music"*, demonstrated from Josquin to Ligeti,
with the extended tonality of the nineteenth century and post-tonal music named as where it earns
its keep.

## Bearing, flagged for the findings surface (verdicts are Task 4's, not this file's)

- **R-7's transform-space alternative is now read at its primary. Like row 17 it is a
  VISUALISATION with no evaluation, no committed analysis and no downstream contract.** Whether
  that discharges R-7 for this item is Task 4's.
- **What it genuinely offers is a representation, and the representation is the interesting part:**
  a continuous, key-free position on the circle of fifths per span per scale, with a magnitude
  measuring how strongly the span resembles an even division of the octave. **That is a candidate
  evidence FORM, not a candidate architecture** — and it discards spelling to get there, which is
  the trade V3 puts a number on in the other direction.
- **DP-B / DP-E:** nothing here decides tonality, so nothing here can falsify a design point about
  how tonality is decided. Its contribution is the observation, made without measurement, that the
  discrete diatonic key label does not fit all repertoires equally — which this project's own
  records already carry from other directions.
- **DP-O (hierarchy, open):** the paper's own limitation sentence is that it does **not** provide a
  tree- or graph-structured analysis. It supplies DP-O no falsifier and no support.

## What this extract does NOT establish

- The contents of Table 1 beyond the values quoted in the text.
- What `C_k`'s hue mapping is exactly.
- Whether any later work extracts labels or segmentations from wavescapes.
- Whether the eight analyses were checked by anyone against a published analysis of the same piece.
- **Nothing here is at-the-object.** Every quotation and value is relayed.

*Provenance: second pass of the reading pass, 2026-08-31. Read at the source URL only. No
specification derived, no document amended, no code opened, no register touched.*
