# EXTRACT — BACHI (arXiv:2510.06528v2), boundary-aware symbolic chord recognition — population row 12, first pass (single pass; not central)

> **Establishment bound:** read 2026-08-30 via prompted extraction over the arXiv HTML full text
> (method and limits in the fetched content record). Authors not relayed; fill at any later pass.

## Claims, labeled

- **[FACT — §architecture]** Boundaries are a SEPARATELY SUPERVISED signal (binary boundary
  sequence predicted by an MLP) that CONDITIONS the encoder by feature-wise modulation — not a
  decoded variable of the labeling search.
- **[FACT — §architecture]** The chord label is factored root × quality × bass and filled by
  confidence-ordered masked iterative decoding (three commits, highest confidence first, no
  autoregression).
- **[FACT — §results]** On a ~1,500-piece classical corpus (When-in-Rome + DCML, converted to
  absolute labels): full-chord macro-accuracy 68.1 vs Harmony Transformer v2 62.1, ChordGNN
  58.5, AugmentedNet 57.2, rule-based 28.4. On corrected POP909-CL: 82.4 vs 82.2 (HT v2).
- **[FACT — §ablation]** The boundary and iterative-decoding machinery moves the FULL-chord
  (joint-consistency) column (66.1 → 68.1) while the per-element columns barely move — the gain
  is coherence between the separately-predicted elements, not per-element accuracy.
- **[FACT — §discussion]** The learned decoding ORDER differs by repertoire: quality-first
  chains dominate on classical (33.2% quality→root→bass), bass-first on pop (56.4%
  bass→root→quality).
- **[FACT — §data]** The original POP909 annotations carried large systematic defects (40.6%
  start-beat misalignment; 14.2% missing key-signature changes) — a ground-truth-quality fact in
  the direction of this project's principle #21.
- **[CONJECTURE — §discussion]** That the human-ear-training analogy explains the gains —
  interpretive framing, not measured causation.

## Coupling facts (mandatory)

- **Assumes upstream:** an UNSPELLED piano-roll (MIDI pitch, 88 keys, quantized 12 frames/beat).
  No spelling, no voice membership, no metrical strength input relayed. Its L0 is therefore
  POORER than this project's notated record — its design solves problems (enharmonic input) this
  project's input does not have.
- **Hands downstream:** absolute chord labels (root, quality, bass) per frame/segment; no key
  output in the main system (a key-detection variant ablated at 67.6); no rivals, no chord-tone
  assignment.
- **Stated scope:** pop and classical symbolic corpora, absolute chord labels (not Roman
  numerals, not tonality-bearing analysis).

## Measured results

Tables in the fetched content record (two corpora × five systems × four columns; ablations).

## Bearing on the framework (first pass)

- **DP-C (segmentation decided WITH):** BACHI is the disposition surface's promised comparable,
  not a falsifier: boundaries supervised separately and injected as conditioning is a DIFFERENT
  cut, and nothing here measures it against joint decoding on this project's axis — its
  evaluation is absolute-chord accuracy on unspelled input without tonality. The framework's
  DP-C ground (given-vs-found boundary measurements, semi-Markov formal result) is untouched.
- **DP-A:** the ablation is same-direction evidence — the machinery's gain concentrates in the
  JOINT consistency of separately-predicted elements, which is the incoherence the framework's
  DP-A cites, here patched by iterative re-fusion (the "adds machinery to undo the separation"
  pattern the framework already names).
- **Measurement phase:** a 2026 benchmarking comparable with public code and a corrected pop
  corpus; the POP909 defect figures are useful ground-truth-quality evidence.
- No falsifier candidate against any chosen point.

## Verification targets touched

- None of V1–V13 originates here.
