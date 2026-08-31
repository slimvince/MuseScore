# EXTRACT — Nápoles López, Feisthauer, Levé & Fujinaga 2020, "On Local Keys, Modulations, and Tonicizations" (DLfM 2020) — population row 13, first pass (single pass; not central)

> **Establishment bound:** read 2026-08-30 via two prompted extraction calls over the author's
> open copy; the per-model per-textbook scores were relayed as Figure-read APPROXIMATIONS and
> none is carried below as an exact value.

## Claims, labeled

- **[FACT — §5]** Evaluated symbolic local-key models track TONICIZATION-level ground truth
  better than MODULATION-level ground truth — "an inclination toward the tonicization
  predictions… unexpected, as most researchers do not describe their local-key-estimation models
  as 'tonicization finders'."
- **[FACT — §2]** The same music yields TWO defensible onset-level key ground truths (a
  modulation column and a tonicization column), and annotation traditions differ enormously in
  how much they tonicize (41.63% of onsets in Rimsky-Korsakov's textbook vs 15.97% Tchaikovsky
  vs far fewer in three others).
- **[FACT — §2]** The proposed scoring is duration-weighted with either exact-match or graded
  MIREX weights (dominant/subdominant 0.5, relative 0.3, parallel 0.2); graded weighting adds
  roughly 10–20 points.
- **[FACT — theory, quoted from Kostka & Payne]** "The line between modulation and tonicization
  is not clearly defined in tonal music." — carried by the paper as its framing premise.
- **[FACT — §3]** A released CC BY dataset exists: 201 textbook excerpts, 2,002 labels, dual
  modulation/tonicization annotations (github.com/DDMAL/key_modulation_dataset).
- **[CONJECTURE — §4.3]** That the models would do better trained on this data — stated, dataset
  too small to test.

## Coupling facts (mandatory)

- **Assumes upstream (of the methodology):** a symbolic score, a model emitting one local key
  per onset, and roman-numeral-bearing annotations from which the two ground-truth columns are
  derived.
- **Hands downstream:** a per-onset dual-column evaluation with duration weighting and graded
  key-distance credit.
- **Stated scope:** evaluation methodology and dataset; three models compared untrained;
  tonicization columns partly supplied by the authors where textbooks omitted numerals.

## Measured results

As relayed (approximate, Figure 3): M1/M3 similar shape and better on tonicization columns; M2b
worst and modulation-leaning; exact values not carried.

## Bearing on the framework and the ruled measurement conventions (first pass)

- **Measurement design (where the surface routes it):** this is the direct methodological
  relative of the project's ruled DUAL key columns (home + local, both carried, D-211) and the
  graded proximity idea sits beside the ruled parent-collection reduction. Its central finding —
  that "local key" as models compute it behaves like a tonicization column — bears on how this
  project's key-vs-LOCAL column is read, and on the ruled crediting-rule prohibition (D-656):
  the two ground-truth columns are NOT interchangeable and a system may score oppositely against
  them.
- **DP-K adjacent:** two defensible ground-truth columns for one music is more evidence that a
  single-answer target under-determines — same direction as the framework's rivals-with-mass.
- No falsifier candidate against any chosen point; nothing here touches the framework's cut.

## Verification targets touched

- None of V1–V13 originates here (the framework does not cite this paper's figures).
