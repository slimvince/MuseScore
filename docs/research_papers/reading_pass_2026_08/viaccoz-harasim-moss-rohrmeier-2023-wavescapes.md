# FETCHED CONTENT RECORD — Viaccoz, Harasim, Moss & Rohrmeier 2023, "Wavescapes: A visual hierarchical analysis of tonality using the discrete Fourier transform" (Musicae Scientiae 27(3))

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from the publisher's full-text
> page `https://journals.sagepub.com/doi/full/10.1177/10298649211034906`. STRUCTURED CONTENT
> RECORD from one prompted extraction call over the whole text — a bounded, declared read.
> (The reachability report filed this as JNMR 2023; the venue is Musicae Scientiae — corrected
> here for the bibliography reconciliation.) Population row 18 (R-7 alternative: tonality in a
> transform space); CENTRAL — second independent pass owed.

## Method

Pieces partitioned into segments; each segment a 12-dimensional duration-weighted pitch-class
vector; a hierarchy function combines segments at every temporal scale (measure → whole piece),
giving a keyscape-shaped triangular plot. Each vector is decomposed by the discrete Fourier
transform into six non-trivial complex coefficients: 1–2 chromatic/tritone distributions;
3 augmented triads and hexatonic collections; 4 fully-diminished chords and octatonic
collections; 5 diatonic collections and fifths relations; 6 whole-tone collections. Phase → hue,
normalized magnitude → opacity; one wavescape per coefficient. No key-finding algorithm anywhere.

## The transform-space position (as quoted)

Keyscapes "are not suitable for representing extended tonality" in 19th-century music because
they assume "common-practice tonality, such as the existence of 24 major and minor keys"; the
DFT approach "does not rely on style-specific theoretical assumptions but only presupposes an
encoding of the music as pitch classes in 12-tone equal temperament."

## Applications and numbers

Eight case studies: Josquin, Bach, Liszt, Chopin, Scriabin, Webern, Ligeti, Coltrane. Example
magnitudes: Liszt Faust opening — mean normalized magnitude of coefficient 3 = 0.652 against
coefficient 6 = 0.172 (supporting a hexatonic over an augmented-triad reading); Josquin Ave
Maria — coefficient 5 mean 0.61 (diatonic predominance; hexachord 0.64). No accuracy evaluation
— there is no ground truth for the pictures; the numbers are descriptive magnitudes.

## Limits and availability

Deterministic pictures; the analyst interprets. Resolution (segment duration) and focus
coefficient are manual choices. Pitch-class only — spelling, timbre, rhythm, form outside the
representation (12-tone equal temperament presupposed, so ENHARMONIC — spelling is discarded).
Python library at `https://github.com/DCMLab/wavescapes` (MIDI, MusicXML, audio input).
