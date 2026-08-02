# Registered predictions — invariance probes (written BEFORE running either relation)

Registered: 2026-08-02, before any octave/permute decode was run. Establishment (untransformed
decode == decode_parity_ref.json, 12/12) runs first; the relations run only after it passes.

## The emission note-vs-pitch-class determination (required before predicting Relation 1)

The emission factor counts NOTES, not pitch classes. In `segment_features`
(tools/joint_estimator/probe_decoder.py:747-753) the emission and spelling sums iterate
`for e in range(i, j): for n in piece.notes_by_event[e]:` and add one `emission_logp` term and one
`spelling_logp` term PER NOTE RECORD. A duplicated tone therefore contributes its emission and
spelling log-probabilities a second time (doubled weight for that voice's tones).

Every other factor is invariant under octave doubling of a non-bass voice:
- bass factor: per-event lowest midi -> pc (probe_decoder.py:704-709, used at :756-762); the
  duplicate is +12 above its original, which remains present and lower, so the event minimum is
  unchanged.
- candidate generation: onset pc sets and overlap pc sets only (probe_decoder.py:1055-1078);
  pc content unchanged.
- missing-tone penalty: overlap pc set membership (probe_decoder.py:764-770); unchanged.
- boundary factor: per event, note-independent given the event lattice (probe_decoder.py:772-775).
- cadence features: pc sets and event bass pcs (probe_decoder.py:884-899, 829-862); unchanged.
  (The parity SELECTED weight vector has cad_leading_tone = 0.01708 nonzero, so the cadence factor
  is live — but its inputs are invariant under both transforms.)
- key/chord/entry/prior transitions: functions of states only.

So the ONLY moving quantities under Relation 1 are the emission and spelling sums, via the
duplicated notes' extra terms.

## Relation 1 — octave doubling of the highest non-bass part

Because the emission counts notes (determination above), the caveat branch applies: BIT-IDENTITY IS
NOT PREDICTED. Registered quantitative predictions:

- P1a (direction, 12/12): total_score strictly DECREASES on every piece. Every added term is a
  log-probability < 0 and at least one duplicated note lands in a scored event on every piece.
- P1b (survival): committed readings mostly survive. Aggregate segment survival (identical
  (i,j,tonic,is_major,class_key,root_pc)) >= 85% over the ~408 sampled segments; at least 4/12
  pieces survive fully (all segments identical).
- P1c (violation population): violations concentrate where the doubled part's tones are non-members
  of the committed chord (the doubling amplifies the emission difference between candidate readings
  by exactly the doubled voice's per-note terms) and where the runner-up reading is close; expected
  form is a changed chord class or key on an unchanged or locally re-cut boundary, not wholesale
  re-segmentation. Boundary structure predicted to survive on >= 9/12 pieces.

## Relation 2 — input note-list order permutation (seeds 1, 2, 3)

Design-level (exact arithmetic) prediction: BIT-IDENTICAL decode 36/36. Every factor is a function
of per-event note SETS or an order-symmetric SUM over notes; candidate enumeration and the Viterbi
consult no note order; the section 5 tie-break is a declared total order independent of input order.

Registered mechanism caveat (the known candidate violation channel, stated before running): the
per-note accumulations are floating-point sums taken in list order (probe_decoder.py:748-753 `+=`
in `notes_by_event[e]` list order; `notes_by_event` is built in input-note order at :609-617), and
FP addition is not associative — permuting the addends can move a content score by ~1 ulp. The
section 5 tie-break fires only on EXACT score equality (:1145-1156 `if a_score != b_score: return
a_score > b_score`), so an ulp wobble silently re-decides any near-tie. Also `event_bass_pc` takes
the FIRST minimal-midi note in list order (:704-709), but equal midi implies equal pc and the bass
factor reads only the pc, so that channel cannot move any label.

- P2a: if all 36 decodes are bit-identical, the design-level prediction stands.
- P2b: any violation will show |total_score_delta| < 1e-9 (ulp-scale) and, if segments differ, the
  differing segments will sit on near-degenerate alternatives (content-score gap at ulp scale) —
  i.e., an order-dependence defect whose mechanism is FP summation order, not a data-structure
  order dependence. A violation with |delta| >= 1e-9 or a large score gap would falsify this
  mechanism account and indicate a genuine order-dependent code path.
