# EXTRACT — the Irish-traditional mode-detection pair (MCM 2024; Applied Sciences 2025) — population row 9, first pass (single pass; not central)

> **Establishment bound:** the 2025 paper read whole via one prompted extraction call (open
> access); the 2024 MCM chapter ABSTRACT ONLY (paywalled, no open copy found) — its "~80%
> average accuracy" figure is carried at abstract grade and nothing else from it is carried.

## Claims, labeled

- **[FACT — 2024 abstract, abstract-grade]** Template-based and unsupervised methods for
  four-mode diatonic detection on Irish folk melodies reach "an average accuracy of about 80%"
  — the surface's relayed figure confirmed at its source, at abstract grade.
- **[FACT — 2025 §results]** With the TONIC GIVEN (corpus transposed to C), unsupervised
  clustering on BINARY pitch-class profiles separates the four modes at NMI ≈ 0.60 / purity
  > 60% (23,636 tunes); duration/beat weighting does NOT beat binary presence, and large
  learned embeddings fail outright (single-cluster collapse).
- **[FACT — 2025 §2]** The mode problem is stated as melodic, not harmonic-functional: mode
  "primarily governs melodic characteristics… without requiring harmonic resolution", and folk
  melodies may "drift between tonal centers or avoid traditional cadences".
- **[FACT — 2025 §1]** The research-gap claim the disposition surface relayed is the papers'
  own, verbatim: "little research on mode detection. Most existing approaches focus on
  identifying the major and minor modes."
- **[CONJECTURE — 2025 §future]** Generalization to non-Western modal systems.

## Coupling facts (mandatory)

- **Assumes upstream:** symbolic melodies with the TONIC known (pre-transposed corpus) — mode
  inference here never solves tonic-finding; metadata mode labels as ground truth.
- **Hands downstream:** a per-tune mode class (four classes).
- **Stated scope:** monophonic Irish folk tunes, Western diatonic modes, per-TUNE (global)
  classification — no local mode changes, no harmony.

## Bearing on the framework (first pass)

- **The mode question (disposition surface §4, routed to L2 detail / measurement / style):**
  confirms at the primaries both halves of the surface's relay — a working four-mode system
  exists at ~80% (melodic, tonic-given, per-tune), and the field's own statement that general
  mode inference is under-researched. For the L2 mode-vocabulary discussion the transferable
  facts are: binary pitch-class PRESENCE outperformed duration weighting for mode separation
  (an emission-design hint consistent with collection-membership evidence), and the task's
  difficulty concentrates exactly where the tonic is NOT given — which is the part this
  project's joint decode already owns.
- **No bearing on any framework cut**; no falsifier candidate.

## Verification targets touched

- None of V1–V13 originates here.
