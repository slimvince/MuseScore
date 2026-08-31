# FETCHED CONTENT RECORD — McLeod & Rohrmeier 2024, "Detecting chord tone alterations and suspensions" (Journal of New Music Research 52(5))

> **Retrieval record.** Fetched 2026-08-30 by the reading pass from the author's open copy
> `https://apmcleod.github.io/pdf/chord-sus-jnmr.pdf` (publisher: tandfonline
> doi 10.1080/09298215.2024.2412595). Same environment bound as every fetch of this pass: the PDF
> binary cannot be saved here; this is a STRUCTURED CONTENT RECORD assembled from three prompted
> extraction calls over the whole text — a bounded, declared read. Population row 2; CENTRAL —
> second independent pass owed, re-fetch rather than consult this file.

## Call 1 — task and method

Task: per-note binary classification within a chord's duration — chord tone (1: pitch class in
the ground-truth chord label) vs not (0); downstream post-processing converts note decisions into
pitch-class vectors and then into alteration labels (suspensions, added tones, replacements).

**Input assumptions, in the paper's words:** the method "takes as input a chord label (and the
notes present in the score for the duration of that label)" — chord boundaries, root, quality,
inversion GIVEN; a binary local-key major/minor flag is a feature, so key context is given too.
Pitch classes represented as perfect-fifth distances above the GIVEN root.

Model (the Chord Pitches Model): per-note 229-dimensional input — spelled PC as fifth-distance
one-hot (39), octave (11), metrical level of onset/offset (2×4), onset/offset as proportions of
chord duration, duration proportions, distances to adjacent onsets, previous/next chord vectors
(67 each: root, quality of 12, inversion of 4, metrical, duration, key flag, diatonicity flag),
current chord vector (28, root excluded). Feed-forward + Bi-LSTM + feed-forward, sigmoid output.

Base-vocabulary-plus-alterations design, motivation verbatim: "adding an additional feature to
each chord label results in a multiplicative increase in vocabulary size (since each alteration
might occur with any existing label), which reduces the possible training data per label and
weakens predictive power." Two phases: (1) per-note chord-tone classification; (2) windowing at
each onset/offset into 27-dimensional PC vectors (13 fifths either side of the root), binarized
with three thresholds (d default ~0.7–0.9; a add, lower; r replacement ~0.5–0.7), replacement
matching to neighbouring default PCs by maximal-spanning pairing, then iterative merging of
neighbouring vectors under subset/compatibility heuristics. Reduced base vocabularies tested:
full 12 qualities / triads 4 / major-minor 2, with sevenths always treated as added tones so a
7th never blocks a merge; "by training chord labeling models on a reduced set of chord qualities,
their accuracy will increase, and if the missing chord qualities can be inferred by our proposed
method… it is possible that overall label accuracy may also improve."

## Call 2 — experiments and results

Corpus: 924 pieces with functional-harmony labels — internal (to-be-released) + ABC + Annotated
Mozart Sonatas + 36 Corelli trio sonatas; 80/10/10 split.

Two settings: ground-truth chord labels in; and NOISY input — "we take as input the output from a
chord labeling model. Specifically, we use the Chord Classification Model (CCM) proposed by
McLeod and Rohrmeier (2021)."

Results (accuracy; default PCs / non-default PCs / overall), proposed vs heuristic baseline:
- Full vocabulary, ground truth: 96.1 / 36.7 / 89.2 vs 80.2 / 42.0 / 76.1 (p < .001 across
  vocabularies).
- Triads, ground truth: 84.5 / 35.3 / 78.4 vs 67.5 / 37.7 / 64.3.
- Major-minor, ground truth: 84.0 / 28.8 / 77.2 vs 65.3 / 37.5 / 62.4.
- Full, noisy: 78.1 / 35.8 / 73.2 vs 65.5 / 30.7 / 61.1.
- Triads, noisy: 73.2 / 39.2 / 69.0 vs 59.4 / 38.9 / 57.2.
- Major-minor, noisy: 73.5 / 36.6 / 69.0 vs 58.5 / 40.2 / 56.5.

Robustness quote: "The vocabulary reduction has a much smaller effect on our method when compared
to experiment 1. The drop in accuracy from the full vocabulary to the reduced vocabularies is
much smaller (4% compared to 11% with ground truth input)."

Error analysis notes: major/minor triads best across vocabularies; diminished and seventh
qualities hardest under reduction; a shown case where the model finds the right added tone but
notates it as a suspension of a different resolution; a merging error case joining two chords
that should stay distinct. Non-default (alteration) accuracy is low in absolute terms (~29–42%)
in every condition, including for the baseline.

## Call 3 — scope, positioning, availability

Scope: post-hoc by design — "it can be applied as a post-processing step given the output of any
harmonic analysis model." The paper does not analyze failure under substantially wrong chord
labels beyond the noisy experiment, and does not take up whether chord identity and tone
classification should be decided JOINTLY; the sequential shape is justified practically (a flat
joint vocabulary "can complicate the learning process"). Context-dependence of alterations
acknowledged (C4 in C major vs G major implies different pitch sets).

Positioning vs Ju et al. 2017: similar note-classification idea, but Ju et al. require four-part
chorales, use 12 unspelled pitch classes vs 35 spelled here, and take only pitches — no
hypothesis chord label — as input.

Future work: explicit search for suspension resolutions; applying the method as one step in a
harmonic inference pipeline.

Availability: code at `github.com/apmcleod/harmonic-inference`; data partly internal
"to-be-released"; licences not stated in the paper.
