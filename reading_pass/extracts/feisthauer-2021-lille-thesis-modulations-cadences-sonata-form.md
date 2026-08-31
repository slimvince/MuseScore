# EXTRACT — Feisthauer 2021, the Lille thesis (modulations and cadences for sonata form) — population row 16, first pass

> **Establishment bound:** chapter-level structured read, 2026-08-30, three prompted extraction
> calls over the open university deposit — NOT a page-by-page whole read of the 100+-page
> French text (declared in the fetched content record; a deeper read is its own slice if the
> user orders it).

## Claims, labeled

- **[FACT — ch. 5]** A three-criterion dynamic-programming key tracker — cadential anchoring
  (V→I strength), diatonic note compatibility, and Weber-distance key proximity, over
  beat × 24-key states — reaches about 85% per-beat key accuracy on annotated Mozart string
  quartets, with the modulation/tonicization boundary acknowledged "porous" and no per-criterion
  ablation.
- **[FACT — ch. 6]** Descriptor-based cadence classification reproduces the published
  asymmetry: PAC F1 0.80 (Bach fugues) / 0.69 (Haydn, precision > 80%) against HC F1 0.29 —
  the same PAC/HC gap as V6's two verified primaries, at this thesis's own corpora.
- **[FACT — ch. 6]** Medial-caesura detection from abstract descriptors locates the caesura
  correctly for HALF the corpus on a very small training set — sonata-form structure detection
  is measured hard even with hand-crafted descriptors.
- **[FACT — ch. 2 §2.2]** The dual-tonality reading is stated as a principle: at every moment
  the score carries TWO defensible key labels — the modulation's and the tonicization's — and
  the thesis's specialized corpus annotates both.
- **[FACT — structure]** Key estimation and cadence detection are engineered as SEPARATE
  problems; their mutual dependence is noted theoretically and left unformalized.
- **[CONJECTURE — ch. 7]** That the local/global tonality interplay can be refined and the
  approach scaled to full sonata-form analysis — stated future work.

## Coupling facts (mandatory)

- **Assumes upstream (ch. 5 model):** the symbolic score with beats; nothing else — chords are
  not presupposed; (ch. 6 classifier): descriptor extraction over the score, cadence labels for
  training.
- **Hands downstream:** a key per beat + modulation points; cadence-arrival decisions; a
  medial-caesura location.
- **Stated scope:** classical string quartets and keyboard works; French-theory framing;
  no chord-level output anywhere — the thesis analyzes tonality and structure WITHOUT a chord
  layer.

## Bearing on the framework (first pass)

- **DP-B/DP-E adjacent, and worth carrying:** the thesis's key tracker uses cadential
  anchoring INSIDE the key decision (a V→I measure as a criterion) — an existence proof of
  cadence evidence feeding tonality rather than being read off it, which is the framework's
  own L1-cue direction (cadence cues upstream, voting; DP-I). Its per-beat key state with a
  proximity-penalized path is the same mechanism family as the incumbent's ruled change-cost
  design (D-347/D-348 territory) — corroboration of direction from an independent group.
- **The dual-tonality principle (ch. 2)** is a third independent statement of the two-column
  key ground truth (with Nápoles López et al. 2020, row 13, same collaboration; and the ruled
  D-211 dual columns) — the findings surface can cite it as convergent.
- **V6 corroboration:** the PAC/HC asymmetry replicates in the thesis's own numbers.
- No falsifier candidate against any chosen point; nothing here decides chords or publishes
  rivals, so DP-A/C/D/K are untouched.

## Verification targets touched

- None of V1–V13 originates here (V6's figures live in the two published papers, both already
  VERIFIED; the thesis's own numbers merely corroborate).
