# EXTRACT — de Haas, Magalhães, Wiering & Veltkamp 2013, "Automatic Functional Harmonic Analysis" (HarmTrace; CMJ 37(4)) — population row 5, CENTRAL, first pass

> **Establishment bound:** read 2026-08-30 via three prompted extraction calls over the full
> text at the author's open copy (method and limits in the fetched content record). CENTRAL:
> second independent pass owed.

## Claims, labeled

- **[FACT — §model]** HarmTrace consumes chord LABELS plus a GIVEN key and never sees notes or
  voicing ("For simplicity, we ignored voice-leading"); its output is a functional parse tree
  over those labels.
- **[FACT — §model]** Modulation is EXCLUDED from the shipped grammar, on the paper's own
  measured-ambiguity ground, verbatim: "even with a constrained modulation specification that
  allows modulation only to specific other keys, and restricts the number of modulations, the
  total number of ambiguous analyses quickly explodes." Only parallel-mode change (root fixed)
  is expressible; multi-key pieces are to be pre-segmented by an external key finder.
- **[FACT — §parsing]** Error-correcting parsing (delete/insert to depth three, fewest
  corrections preferred) makes the parser total: on 5,028 real-world sequences it "never crashes
  or refuses to produce valid output" (3.38 deletions, 9.85 insertions per song; deleted chords
  under 6% of chords parsed).
- **[FACT — §evaluation]** The analyses themselves are NOT evaluated against ground truth — only
  parse statistics and worked examples; "we evaluate its parsing performance."
- **[FACT — §model]** Ambiguity is managed by constraining rule application (typed grammar,
  precedence), with residual multiple analyses accepted and exponential growth acknowledged.
- **[THEORY]** The grammar's basis — Riemann's three functions; Rohrmeier's generative syntax
  (2007, 2011); hierarchical recursion — is established published theory adopted, not
  established here.
- **[CONJECTURE]** Applicability beyond the jazz-biased corpus (a Bach chorale is shown, no
  measurement).

## Coupling facts (mandatory)

- **Assumes upstream:** the tonality (key) DECIDED, and the chord labels DECIDED — a completed
  chord-level analysis; single-key stretches (or an upstream segmentation into them).
- **Hands downstream:** a hierarchical functional reading over given labels; corrected
  (deleted/inserted) chords as a byproduct.
- **Stated scope:** label-level functional analysis, jazz-biased vocabulary, no modulation, no
  inversions/voicing concern, phrase structure deferred to post-processing.

## Measured results (corpus, metric, value)

Parse statistics on 72 and 5,028 sequences (table in the fetched content record); runtime
10 ms / 76.5 ms per song. No harmonic-accuracy measurement.

## Bearing on the framework (first pass)

- **DP-O (hierarchy — open):** what the disposition surface promised is confirmed at the
  primary: an executed grammar branch with error-correcting parsing and the measured
  tractability lesson. DP-O's falsifier (a tree model beating a matched-capacity sequence model
  on this repertoire's ground truth) is NOT supplied — HarmTrace's trees are never graded
  against ground truth at all. DP-O stays open on this paper's evidence.
- **Δ4 confirmed at the primary:** function is decided over bare chord sequences with tonality
  assumed known — its input is what the framework's L2 settlement already IS, so it is no
  counter-evidence to deriving the Roman numeral rather than deciding it separately.
- **The modulation-ambiguity lesson** is chain-level evidence FOR deciding tonality WITH the
  chords rather than parsing it hierarchically over labels (DP-B/DP-E direction): pushed to the
  grammar level, key changes explode; decided in the one pass, they are a bounded transition.
- **L2 candidate admission (robustness):** the deletion/insertion repair is the label-level
  analogue of admitting imperfect surfaces — enrichment for the detail phase, as the surface
  said (DP-M/§8.4 untouched: the repair edits the INPUT stream, not an earlier layer's
  published decision).

## Verification targets touched

- None of V1–V13 originates here.
