# FETCHED CONTENT RECORD — McLeod, Suermondt, Rammos, Herff & Rohrmeier 2022, "Three Metrics for Musical Chord Label Evaluation" (FIRE 2022)

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from the author's open copy
> `https://apmcleod.github.io/pdf/fire-chord-eval.pdf`. Environment bound as for every fetch of
> this pass: PDF binary not savable; STRUCTURED CONTENT RECORD from one prompted extraction call
> over the whole text — a bounded, declared read. Population row 4 (not central).

## The three metrics

1. **Spectral pitch similarity.** Synthesize both chord labels (default piano, three voicings),
   take spectrograms (VQT/CQT/STFT/mel), central frame, cosine distance between them. Fully
   continuous; grounded in psychoacoustics — cited (Milne et al.) as "a good predictor of
   listeners' perception" with "predictive value for tonal fit responses in Krumhansl and
   Kessler's probe tone data."
2. **Tone-by-tone distance.** Chords as pitch-class sets (neutral or tonal/spelled); distance =
   1 − average of the two shared-proportion directions, with parametric root and bass bonuses
   (virtual notes, defaults 1). Example: A minor vs C7 → proportions 2/3 and 1/2, distance 5/12.
3. **Mechanical distance.** Physical voicing distance: bass distance in semitones (weight 1
   default) + minimum-weight bipartite matching (Hungarian algorithm) over remaining pitches +
   penalties for unmatched tones; customizable per-interval distance.

## Motivation against binary accuracy (as stated)

(1) "With a binary metric, every error is penalized equally, although … labelling mistakes may be
unequally egregious. For example, with ground truth C major, C minor and A minor are clearly much
closer to being correct than D♯ minor." (2) Grown vocabularies: "A model which outputs only
triads would be evaluated unfavorably if the ground truth also contains 7th chords, regardless of
whether or not the model correctly predicts the underlying triad." (3) Human expert root
agreement quoted at 76–94%: "To penalize models equally severely for every mistake could be
unfair or uninformative, since expert annotators could make (or even have made) the exact same
mistake."

## Behaviour on examples

- C-major-vs-variants sweep: tone-by-tone cannot separate same-shared-note chords (all G-root
  chords equal) where spectral similarity grades by voicing; mechanical prefers bass near C.
- Mozart K279-2 case study: two models with IDENTICAL binary CSR (31.6%) separate under the
  graded metrics — spectral 20.9 vs 19.9; tone-by-tone 33.4 vs 24.5; mechanical 1.47 vs 2.11 —
  "the variability in evaluation, as well as the importance of picking the appropriate metric."
- Divergence cases: matching voicing with different root/bass (spectral low, tone-by-tone high);
  wholesale semitone shifts (mechanical low, spectral high); inversions of one root (tone-by-tone
  low, mechanical high).

## Toolkit

`https://github.com/DCMLab/chord-eval`. Labels: root, type, inversion (→ bass), alterations
(added/removed/replaced tones); neutral or tonal pitch classes (C♯ ≠ D♭ representable). All three
metrics compose with duration-weighted Chord Symbol Recall. Licence not stated in the paper.

## Limits and intended use (as stated)

Pairwise, context-free ("the distance between a pair of chord labels in isolation" — no key, no
tonal context); mechanical distance deliberately avoids voice-leading theory ("complex and often
controversial music-theoretical decisions"); no single metric best in all cases. Future work: "A
metric which takes the full tonal context into account would be greatly beneficial—if not
essential."
