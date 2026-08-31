# EXTRACT — McLeod, Suermondt, Rammos, Herff & Rohrmeier 2022, "Three Metrics for Musical Chord Label Evaluation" (FIRE 2022) — population row 4, first pass (single pass; not central)

> **Establishment bound:** read 2026-08-30 via one prompted extraction call over the full text at
> the author's open copy (method and limits in the fetched content record).

## Claims, labeled

- **[FACT — §metrics]** Three graded chord-label distances are defined and released as a toolkit
  (`github.com/DCMLab/chord-eval`): spectral pitch similarity (psychoacoustic, synthesized
  voicings), tone-by-tone (pitch-class overlap with root/bass bonuses; spelled or enharmonic
  classes), mechanical (voicing distance, bipartite matching over semitones).
- **[FACT — §case study]** Two models with IDENTICAL binary chord-symbol recall (31.6% on Mozart
  K279-2) are separated by every graded metric, in different directions per metric — the paper's
  own demonstration that binary accuracy under-measures.
- **[FACT — §motivation]** The paper quotes human expert root agreement of 76–94% as ground for
  graded penalties (a relayed figure — its own primary is the annotation-agreement literature,
  not this paper).
- **[FACT — §metrics]** All three metrics compose with duration-weighted chord-symbol recall.
- **[THEORY]** The psychoacoustic grounding of spectral pitch similarity (Milne et al.) is
  established published theory cited, not established by this paper.
- **[CONJECTURE — §future]** That a full-tonal-context metric is needed — stated as future work.

## Coupling facts (mandatory)

- **Assumes upstream:** two chord labels (root, type, inversion, alterations) to compare —
  nothing else; deliberately no key or tonal context.
- **Hands downstream:** a continuous distance per label pair, composable into duration-weighted
  corpus scores.
- **Stated scope:** label-pair evaluation only; explicitly not a contextual/tonal metric; no
  claim that any one metric governs.

## Measured results

The K279-2 case-study numbers and the divergence examples (in the fetched content record); no
corpus-scale accuracy claims of its own.

## Bearing on the framework (first pass)

- **Measurement design (where the disposition surface routes it):** a concrete graded-metric
  candidate set; the tone-by-tone metric with TONAL pitch classes and root/bass bonuses is the
  nearest relative of this project's ruled root-governed duration-weighted unit, and the
  cadential-six-four measurement-cost mitigation the surface names for DP-N (whichever label
  vocabulary is ruled, graded distance softens the cross-vocabulary cost).
- **No bearing on any framework cut**; no falsifier candidate.
- Caution for later use: the metrics are context-free by design — they cannot replace the ruled
  key-aware grading conventions (parent-collection reduction, abstain-awareness), only sit beside
  them.

## Verification targets touched

- None of V1–V13 originates here.
