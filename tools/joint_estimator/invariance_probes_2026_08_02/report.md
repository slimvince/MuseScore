# Invariance probes — octave doubling and input-order permutation (2026-08-02)

READ-ONLY exploratory probe (surprises are the intended product). Repository untouched; all
artifacts in this directory. Apparatus: the committed pure-Python reference decoder
`tools/joint_estimator/probe_decoder.py`, driven by `run_invariance.py` (this directory), which is
adapted from the committed harness
`tools/joint_estimator/transposition_probe_2026_08_02/run_probe.py` (loading / decoding /
comparison machinery reused verbatim where applicable; the committed file was not modified).
Decode configuration = the parity-reference arm: `FittedAdapter(leftover_mode="freq",
table_set="all", weights=decode_parity_ref.json["selected_weights"])`, seg_cap 4, report-only
posterior skipped (the same skip the committed harness uses; it moves neither segments nor
total_score).

## What was completed

1. Establishment: the 12 deterministically sampled pieces (`sorted(stems)[::27][:12]`) decoded
   untransformed reproduce `tools/joint_estimator/decode_parity_ref.json` exactly — **PASS 12/12**
   (segments and total_score; `establish_state.json`).
2. Predictions registered BEFORE running either relation: `predictions_registered.md`.
3. Relation 1 (octave doubling of the highest non-bass part): 12/12 pieces run
   (`octave_state.json`).
4. Relation 2 (note-list order permutation, seeds 1/2/3): 36/36 conditions run
   (`permute_state.json`).
5. Mechanism diagnosis per violation class, grounded at file:line (below;
   `mechanism_diagnosis.txt`, `octave_analysis.txt`).

## The pre-run determination (registered): the emission counts NOTES, not pitch classes

`segment_features` (probe_decoder.py:747-753) adds one `emission_logp` term and one
`spelling_logp` term PER NOTE RECORD (`for e in range(i,j): for n in piece.notes_by_event[e]:`).
A duplicated tone therefore doubles its emission and spelling weight. This is not a decode-side
accident: the fitted emission table was COUNTED per note the same way
(gen_note_tables.py:385-410, `emission[combo][cat] += 1` per note whose onset falls in a kept GT
segment) — per-note is the trained semantics of the model, consistent between fit and decode.
Every other factor was analyzed as invariant under the doubling (bass = per-event lowest midi,
probe_decoder.py:704-709; candidates/missing-tone = pc sets, :1055-1078/:764-770; boundary = per
event, :772-775; cadence = pc sets + bass pcs, :829-899 — live in the selected weight vector via
cad_leading_tone=0.01708 but input-invariant here). So the caveat branch of the dispatch applied,
and the registered Relation-1 prediction was score-change-with-mostly-surviving-readings, not
bit-identity (see predictions_registered.md for the exact registered figures).

## Relation 1 — octave doubling (midi+12 duplicate of every note of the highest non-bass part)

Transform: duplicates appended after all originals (original per-event FP sum order preserved);
pc, lof, onset, duration, covariates unchanged; the doubled part never contains the piece's
lowest note (verified per piece; all 12 pieces are 4-part, doubled part = part 0, soprano).

| piece | segs matched | boundaries identical | total_score delta |
|---|---|---|---|
| bwv10.7 | 32/38 | no | -19.053 |
| bwv153.1 | 24/29 | no | -21.842 |
| bwv2.6 | 27/32 | no | -18.383 |
| bwv245.37 | 38/42 | no | -29.317 |
| bwv271 | 30/34 | no | -19.184 |
| bwv297 | 28/36 | no | -19.368 |
| bwv321 | 26/26 | yes | -13.823 |
| bwv347 | 34/40 | no | -23.509 |
| bwv373 | 25/25 | yes | -13.089 |
| bwv398 | 28/38 | no | -26.402 |
| bwv420 | 31/31 | yes | -20.189 |
| bwv55.5 | 31/37 | no | -20.528 |

Totals: 354/408 segments identical (86.8%); 0/12 pieces bit-identical; 54 violation records.
Violation anatomy: 23 same-span label changes, 7 pure re-cuts (labels at the tick unchanged),
24 span-and-label changes; among label changes, chord class changed in 46, key in 22, root pc in
21.

Prediction scorecard (vs `predictions_registered.md`):
- **P1a PASS 12/12** — total_score strictly decreased on every piece.
- **P1b PART-PASS** — aggregate survival 86.8% >= the registered 85%; but fully-identical pieces
  3/12 vs the registered >= 4/12 (near miss by one).
- **P1c FAIL — the registered surprise of this probe.** Registered: boundary structure survives
  on >= 9/12 pieces. Observed: 3/12. The doubling does not merely flip labels locally; on 9 of 12
  pieces the semi-Markov DP re-optimizes the segmentation itself (re-cut runs of 2-6 segments,
  e.g. bwv398 ticks 12480-15840 re-read from D-major V/I alternation to a retonicized A-major I
  block; bwv10.7 ticks 5280-7680 re-cut 2 segments into 3).

### Mechanism diagnosis (violation classes, each grounded in code and measured factor deltas)

The single underlying mechanism for ALL Relation-1 violations: per-note emission/spelling
weighting (probe_decoder.py:747-753; trained per note at gen_note_tables.py:385-410). Doubling
the soprano doubles that voice's per-tone contribution to the likelihood, which amplifies the
content-score DIFFERENCE between any two candidate readings by exactly the doubled tones'
per-note term differences. Empirical ground (mechanism_diagnosis.txt): for every probed state,
`bass`, `missing_tone`, and `boundary` raw deltas are exactly 0.0 between base and transformed —
only `emission` and `spelling` move, as the pre-run analysis said.

Three measured cases (same span, same event indices, base vs transformed):

1. **Quality inflation** — bwv2.6 @ 5760, G-minor V|Maj -> V|Dom7 (root unchanged, 2). The one
   doubled tone in the span is pc 0 (C = the seventh of D-F#-A-C). Under V|Maj it is a non-member
   (emission delta -2.905 raw); under V|Dom7 a member (-0.069). The content margin obs-exp widens
   +0.483 -> +0.959; the base decode's transition-side preference for the triad reading is
   overrun. Same pattern: bwv271@15360, bwv398@9120 (V|Maj -> V|Dom7), bwv297@10080
   (IV|Maj -> II|Min7), bwv55.5@13440 (IV|Maj -> II|Min7), bwv297@12000 (IV|Min ->
   II|HalfDim7, root 7 -> 4; measured case 3: doubled pc 4 is a member only of the tetrad;
   margin +0.450 -> +0.886). The doubled melody tone is promoted into the chord: note-count
   semantics treat it as twice the evidence.
2. **Key relabel via the spelling factor** — bwv153.1 @ 18000, VII|Dim7 in E major ->
   VII|Dim7/V in A minor (same root 3, same sounding chord). Here the EMISSION delta is identical
   for both readings (-0.121 each); the SPELLING factor decides: the doubled tone (pc 0, C
   natural) bins chromatic-flat relative to an E-major tonic (raw spelling delta -4.522) but
   diatonic relative to A minor (-2.100) (spelling_bin, gen_note_tables.py:218-233). Doubling
   flips the margin -0.232 -> +0.281. So the spelling factor also carries per-note count
   semantics (probe_decoder.py:752-753) and can flip the KEY on its own.
3. **Re-segmentation** (the P1c surprise, 9/12 pieces) — the same per-note amplification changes
   which SPANS score best (a span whose doubled tones fit one chord well gains relative to a cut
   that splits them), and the exact semi-Markov Viterbi (probe_decoder.py:1225-1286) re-optimizes
   globally; boundary-factor terms themselves never moved. The re-cuts concentrate where the
   melody carries non-chord tones against the committed reading (e.g. bwv10.7@0: the pickup
   re-read from Bb-major VI|Min to G-minor I|Min).

Interpretation (stated plainly): the model's design — fit AND decode, consistently — reads
note-count evidence, not pitch-class evidence. Octave doubling is therefore VISIBLE to it by
construction: the probe establishes this is a model property, not a decoder defect. The musical
fact that the sonority's harmonic identity is unchanged is not represented in the per-note
likelihood; 13.2% of committed segments moved under a doubling that changes no pitch class, no
bass, and no event lattice. Any move to pc-level (or voice-deduplicated) emission would be a
model change requiring refit, not a decode patch.

## Relation 2 — input note-list order permutation (seeds 1, 2, 3 per piece)

Result: **committed reading identical 36/36** — 1224/1224 segments (spans, keys, classes, roots)
byte-equal to the parity reference; no boundary moved anywhere.
Bit-identity of total_score: 32/36. Four conditions show an ulp-scale score wobble:
bwv153.1|s2 delta -1.421e-14; bwv321|s1,s2,s3 delta -2.842e-14 each (max |delta| over all 36 =
2.842e-14).

Prediction scorecard: the design-level prediction (bit-identical 36/36) FAILED on the score
channel in 4/36; the registered mechanism caveat P2b PASSED exactly — every violation has
|total_score_delta| < 1e-9 and zero segment-level consequence. Mechanism (registered pre-run,
confirmed by the observed magnitudes): floating-point addition non-associativity in the per-note
accumulation loops — `notes_by_event` is built in input-note order (probe_decoder.py:609-617) and
the emission/spelling `+=` runs in that list order (:747-753), so permuting the input permutes the
addends. The section-5 tie-break fires only on EXACT score equality (:1145-1156), so ulp wobble
would silently re-decide an exact near-tie; at this sample no committed label sat close enough
for the wobble to flip anything. The other identified order-dependent construct,
`event_bass_pc`'s first-minimal `min()` (:704-709), cannot move any label because equal midi
implies equal pc and the bass factor consumes only the pc (:756-762).

Residual finding worth recording: the decoder's committed surface is empirically order-invariant
at this sample, but its total_score is not bit-stable under input permutation. Any future gate
that compares total_score for EXACT equality across runs (e.g. a cross-implementation parity
check at `== 0.0` tolerance) would flake at ~1e-14; the existing parity establishment uses
abs<1e-6 and is safe.

## Artifacts

- `predictions_registered.md` — the pre-run registered predictions (unedited).
- `run_invariance.py` — the probe harness (adapted from the committed run_probe.py).
- `establish_state.json` — establishment, PASS 12/12.
- `octave_state.json` — Relation 1 raw results incl. all 54 violations with per-factor deltas.
- `permute_state.json` — Relation 2 raw results (36 conditions).
- `octave_analysis.txt`, `mechanism_diagnosis.txt` — violation anatomy + measured factor deltas.

Sample: bwv10.7, bwv153.1, bwv2.6, bwv245.37, bwv271, bwv297, bwv321, bwv347, bwv373, bwv398,
bwv420, bwv55.5 (the committed harness's deterministic sample). note_events corpus git hash as
recorded in the state files; decoder and tables at repository HEAD, read-only.
