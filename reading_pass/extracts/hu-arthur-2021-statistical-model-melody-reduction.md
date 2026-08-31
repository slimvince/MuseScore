# EXTRACT — Hu & Arthur 2021, "A Statistical Model for Melody Reduction" — population row 14, first pass (single pass; not central)

> **Establishment bound:** read 2026-08-30 via one prompted extraction call over the arXiv full
> text (route in the fetched content record). Identity: the one Hu & Arthur 2021 publication at
> Arthur's laboratory — settled without the workbook.

## Claims, labeled

- **[FACT — §results]** A surface-feature-only NCT classifier (duration, metric position,
  approach/departure intervals; logistic regression; no harmony at inference) beats the
  all-chord-tone baseline by only ~4–5 points out of sample (TAVERN 76.4 vs 71.2; Haydn 70.6 vs
  66.0, AUC 0.685).
- **[FACT — §data]** The CT/NCT ground truth is DERIVED from human Roman-numeral annotations
  plus key — the authors call the underlying annotation "far from an objective process."
- **[FACT — §positions]** Style dependence is stated and quantified in the data: themes carry
  19% NCTs, the ornamented variations far more (~28% corpus-wide) — and prior NCT work does well
  on chorale-style textures "known to contain mostly CTs" while worsening on virtuosic styles.
- **[CONJECTURE — §future]** That melody reduction as preprocessing improves chord estimation —
  "preliminary results indicate a modest improvement," not published in this paper.

## Coupling facts (mandatory)

- **Assumes upstream:** a monophonic melody line (uppermost voice), meter, and — for TRAINING
  LABELS only — a completed key + Roman-numeral analysis. At inference: surface features only.
- **Hands downstream:** a per-note CT/NCT decision (binary; no elaboration types).
- **Stated scope:** classical theme-and-variation piano repertoire + one quartet set;
  monophonic; longer context unused.

## Bearing on the framework (first pass)

- **DP-D — same direction as the chosen point, from an independent group.** This is exactly the
  "first-running elaboration detector" class DP-D excludes: harmony-blind, weak margins over the
  trivial baseline, style-dependent, and its own ground truth circularly derived FROM a
  harmonic analysis. It measures the information ceiling of surface features alone —
  duration/beat/interval cannot carry the CT/NCT decision far (the direction of ledger C26:
  duration weight cannot separate a long elaboration from an added tone; the functional
  discrimination lives elsewhere).
- **Project NCT design (docs/nct_detection_design.md, the deferred Shape A/B question):**
  useful as the measured floor for Shape-B-like surface classifiers; nothing here supports
  post-analysis stripping over NCT-aware chord identification.
- No falsifier candidate against any chosen point.

## Verification targets touched

- None of V1–V13 originates here.
