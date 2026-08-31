# EXTRACT — McLeod & Rohrmeier 2024, "Detecting chord tone alterations and suspensions" (JNMR 52(5)) — population row 2, CENTRAL, first pass

> **Establishment bound:** read 2026-08-30 via three prompted extraction calls over the full text
> at the author's open copy (retrieval method and limits in the fetched content record beside
> this file). Locations at section granularity as relayed. CENTRAL: second independent pass owed.

## Claims, labeled

- **[FACT — §method]** The method takes the chord label AS GIVEN — "takes as input a chord label
  (and the notes present in the score for the duration of that label)" — with boundaries, root,
  quality, inversion and a local-key major/minor flag all upstream inputs; it is offered as "a
  post-processing step given the output of any harmonic analysis model."
- **[FACT — §method]** Its stated ground for deriving alterations AFTER a base chord rather than
  enlarging the label space: an alteration feature multiplies vocabulary size and "reduces the
  possible training data per label and weakens predictive power."
- **[FACT — §results]** With ground-truth chords, per-note chord-tone detection reaches 89.2%
  overall (full vocabulary) vs 76.1% for a heuristic baseline (p < .001); under NOISY upstream
  chords (the 2021 system's classification module) it holds 73.2% vs 61.1%.
- **[FACT — §results]** Accuracy on the NON-DEFAULT pitch classes — the alterations themselves —
  is low in absolute terms in every condition (28.8–39.2% for the method; the baseline is
  sometimes higher on that column while far lower overall).
- **[FACT — §results]** Vocabulary reduction costs the method only ~4% under noisy input against
  ~11% under ground-truth input — the stated robustness result.
- **[FACT — §positioning]** Differences from Ju et al. 2017 as the paper states them: Ju et al.
  need four-part chorales, use 12 unspelled pitch classes (vs 35 spelled), and take no hypothesis
  chord label as input.
- **[CONJECTURE — §future]** That explicit search for suspension resolutions would improve
  performance; that reduced-vocabulary labeling plus inferred alterations may improve overall
  label accuracy — both stated as intent/possibility, not measured.

## Coupling facts (mandatory)

- **Assumes upstream:** a completed harmonic analysis — segmentation, chord root/quality/
  inversion, and local-key mode — plus the spelled score for the label's duration. This is the
  load-bearing coupling fact: **the method cannot run before the chord decision and does not
  revise it.**
- **Hands downstream:** per-note chord-tone/non-chord-tone decisions, merged pitch-class vectors,
  and an enriched chord label carrying added/replaced tones and suspensions.
- **Stated scope:** Western tonal repertoire of the 924-piece corpus (Beethoven, Mozart, Corelli,
  internal); alterations defined by example rather than formally; failure under substantially
  wrong chord labels not deeply analyzed; joint-versus-sequential deciding of chord and tones not
  taken up beyond a practical justification of the sequential shape.

## Measured results (corpus, metric, value)

924 pieces (ABC + Mozart Sonatas + 36 Corelli trio sonatas + internal), 80/10/10; per-note
accuracy split default/non-default/overall; six conditions (3 vocabularies × ground-truth/noisy);
full table in the fetched content record.

## Bearing on the framework (first pass; verdicts belong to the findings surface)

- **DP-D — the one rival-shaped item.** The disposition surface's defusing reading is CONFIRMED
  AT THE PRIMARY: the method's own stated scope assumes segmentation and basic chord already
  known (AS010's relay was accurate), so it does not answer the framework's ground for deciding
  chord-tone assignment inside the one entangled decision (ledger C27; the analyst's note). What
  it IS: measured evidence that the TYPE of an elaboration is derivable after the decision — the
  place the framework's R-4 already assigns it — and a measured base-vocabulary-plus-derived-
  alterations route for the L2 detail specification's label-space design.
- **A finding the surface did not carry:** the absolute accuracy on the alterations themselves is
  low (~29–39% non-default), so as a candidate mechanism it is currently strong on confirming
  default chord tones and weak on the alterations proper — a bound any detail specification
  citing it must carry.
- **DP-A direction:** consistent — the flat-multiplied label space is rejected by measurement of
  data sparsity, the same direction as the framework's holistic-but-compact publication design.

## Verification targets touched

- None of V1–V13 originates here. No divergence to report.
