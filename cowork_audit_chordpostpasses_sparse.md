# Cowork independent audit — chordpostpasses + sparsechordrefinement (peripheral chord-axis) — reconcile w/ CC

> Second-opinion pass from committed-object source (HEAD). Two small post-scoring refinements.

## chordpostpasses (Iter-86/91 pedal)
**Responsibility:** post-competition chord-identity refinement for BASS cases — Iter-86 (bass-b7 → MinorSeventh
promotion), Iter-91 (bass-as-root), two-pass PEDAL detection. `cptIsBassChordTone` decides whether the bass is
a chord tone (triad intervals + detected 7th/9th/11th/13th extensions) → slash chord (Cm7/F) vs structural
pedal point.
- **[correctness — OK] Specific, thorough bass-tone test** (handles slash vs pedal correctly per the extension
  bitmask). A targeted refinement.
- **[phase-2] Another post-scoring CONTEXT patch (bass context)** — same "local-needs-context" pattern as the
  gates; part of the post-scoring compensation cluster a joint/contextual decision would subsume.

## sparsechordrefinement
**Responsibility:** refine chord QUALITY for SPARSE regions (few notes) using KEY context —
`diatonicTriadShapeForDegree` + `tonesFitTriadShape` infer the likely diatonic triad quality from the key for
an under-determined region.
- **[correctness — key-dependent] Reasonable** (the key constrains the likely sparse triad), but
  **KEY-DEPENDENT → inherits key-axis errors** (a wrong key refines a sparse chord wrongly).
- **[completeness] Diatonic-only** — chromatic/non-diatonic sparse chords aren't refined.
- **[phase-2] Key coupling** (the chord↔key circularity again — sparse chord depends on the key) + another
  context patch (key context).

## Phase-2 — the post-scoring compensation CLUSTER (chord-axis complete)
gates (A–L) + post-passes (Iter-86/91/pedal) + sparse-refinement together = the **post-scoring
context-patch cluster**: each brings *external context* (next-region / key / bass) to fix an identity the
LOCAL competition got wrong. This is the chord-axis manifestation of "local decision needs context" — all
candidates to be subsumed by the joint/contextual decision (and, for the gates, the refactor-#2 dissolution).
The chord↔key coupling recurs (diatonic-root tiebreak in the oracle, key context here) — a phase-2 circularity
note.

## Chord axis — AUDIT COMPLETE (5 layers)
oracle (~95% correct, symmetric floor reserved) → competition/function (rule-reachable obligations) →
post-scoring compensation cluster (gates + post-passes + sparse = context patches). **Remedy: competition-rule
completion + gate-dissolution; the floor → reserved learned slice.** Healthy vs the key axis.
