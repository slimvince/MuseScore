# Cowork independent audit — regionanalyzer (segmentation + per-region analysis) — reconcile with CC

> Second-opinion pass from committed-object source (HEAD).

## Responsibility
`analyzeRegions` — the region pipeline: **Pass 1** (coarse boundary detection + `analyzeChord` per region) →
**Pass 2** (onset-Jaccard sub-boundaries + re-analyze) → **Pass 2b** (bass-movement sub-boundaries) →
**Pass 3** (coalesce/absorb short regions). ⚠ **Multiple responsibilities:** SEGMENTATION (where chords
change) + per-region CHORD-ANALYSIS orchestration + the post-merge — a decomposition flag.

## Correctness
1. **[correctness — segmentation granularity] Segmentation drives measured correctness.** Boundaries decide
   the regions the chord/key layers analyze; the section-vs-batch granularity gap (per-beat root-error ~7×
   the batch region-error) shows segmentation granularity materially moves the numbers — under/over-
   segmentation = wrong analysis units.
2. **[correctness/structure — the triplication HAZARD] Pass 1/2/2b carry DUPLICATED region-collapse +
   chord-analysis bodies** ("DUPLICATED … keep in sync with the Pass 2 site"; the beam-1 decoder repeated).
   Manual sync = a divergence hazard (a fix to one pass not mirrored → inconsistent segmentation). This is the
   behavior-entangled structure deferred from the splits.
3. **[correctness — the merge/chord MISMATCH] Pass 3 merges tones AFTER the chord was computed** (coalesce/
   absorb + `mergeChordAnalysisTones`) → the final region's tones ≠ the tones the chord was identified on.
   **This is the exact coupling that made the J-key-iii re-emission unfaithful** — the chord identity is NOT a
   clean function of the final region.

## Completeness
4. **[completeness] Boundary coverage** — coarse + onset-Jaccard + bass-movement; harmonic changes none of
   these passes catch are mis-segmented.

## ★ Phase-2 — two STRUCTURAL obligations (different in kind from the correctness ones)
- **The Pass triplication** → de-duplicate into one parameterized pass. **Behavior-sensitive** (de-dup may
  shift segmentation) → deferred under the no-inference rule; needs explicit ratification + careful
  byte-identity, NOT a free refactor.
- **The chord-identity-vs-final-region mismatch** (chord computed mid-pipeline, tones merged in Pass 3) is a
  deep architecture issue: it broke faithful chord re-emission and means the chord layer's output can't be
  cleanly recomputed from the final region. A real target for the constrained-joint / re-layering work — the
  chord identity should be a function of the final region, or the merge should re-chord.

## Reconciliation targets (for CC)
- Quantify Pass-divergence risk (have the duplicated bodies already drifted?) + the segmentation
  over/under-rate vs DCML boundaries.
- Confirm the Pass-3 merge changes the tone set vs the chord-computed-on set (the re-emission root cause).
