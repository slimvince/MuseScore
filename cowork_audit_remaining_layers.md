# Cowork audit — remaining P3/P4 layers (completeness pass) — reconcile with CC

> Brisk second-opinion pass over the orchestration/output layers (lower obligation density). Committed-object
> source (HEAD). Obligations fold into `cowork_audit_obligation_map.md`.

## sectionanalyzer (residual: analyzeSection + Layer-B stabilization + KeyArea)
- **Responsibility:** section orchestration — Layer-B 1-region-island key stabilization + degree/function
  re-derivation + KeyArea grouping.
- **[correctness — same entrenchment pattern] Layer-B stabilization** removes a non-persistent single-region
  key (smoothing) → can erase a real one-region modulation (entrenchment) or correctly drop noise. Same
  smoothing→entrenchment as the resolver hysteresis. **Made INERT when joint wiring is on** (the joint Viterbi
  IS the smoother) → confirms the migration: the joint decode unifies BOTH old smoothing layers (hysteresis +
  Layer-B). Folds into **K3**.
- **[correctness] KeyArea grouping is confidence-gated ≥0.8** → the **X1** blind spot (key areas not formed on
  uncertain regions).

## tonicizationlabeler
- **Responsibility:** label applied/secondary tonicizations (V/x, viio/x) from the prevailing key.
- **[correctness — S1] The tonicization↔modulation boundary.** A brief applied chord (tonicization) vs a
  sustained local key (modulation) is a notation-convention boundary; the labeler reads tonicization where
  DCML may annotate a modulation (the 6-tonic/S1 finding). Needs local-key/modulation context (cadence/KeyArea)
  to decide — folds into **S3 / the key-axis modulation work**.
- **[phase-2 — decomposition] Duplicated pc/collection helpers.** Its `tonicization_detail` namespace
  re-implements the diatonic-collection mask **identical to cadencekeyanchor's** (and the jkd/lmd-prefixed
  copies in jointkeydecision/localmodulationdetector). **A shared key-collection primitive is duplicated
  across ≥4 layers** → a clean decomposition obligation (add to S3).

## Mechanical / output (skim — low obligation)
- **harmonicsegmenter:** cohesive segmentation primitive (`greedyExpandSegmentation` + privates); correctness =
  boundary detection — same segmentation-granularity concern as `regionanalyzer` **S1**, no new obligation.
- **regiontonecollector + primitives:** tone collection / pitch-context gathering (data plumbing). Stable; the
  one note is the lookback/lookahead **pitch-context window** that feeds the scorer's window-coupling (K2-adjacent).
- **chordsymbolformatter / keymodeformatting:** output string rendering (RN/symbol/Nashville). **Display
  correctness** only (spelling; the mode-collapse rendering) — downstream of the analysis, low priority.
- **chordvoicing:** keyboard-reduction voicing (display). Low obligation.
- **chorddiagnose:** diagnostic replay (a tool, not production output). Low obligation.
- **modepriorpresets:** the per-preset mode priors — **`[empirical]` = a Stage-5 CALIBRATION target** (feeds
  the scorer's `modePrior`). Folds into **K3 calibration**.

## Net: phase-1 coverage COMPLETE
No new obligation changes the two-track verdict. Additions folded into the map: Layer-B stabilization → K3
(the joint unifies the smoothers); KeyArea confidence-gate → X1; tonicization↔modulation → S1/key-axis;
**duplicated key-collection primitive across ≥4 layers → S3 (decomposition)**; mode-prior presets → K3
(calibration); output layers → display-correctness (low priority). Phase 1 (all ~19 layers) is audited; the
obligation map stands.
