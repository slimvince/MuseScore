# Cowork independent audit — keymodeanalyzer (the key-mode scorer) — to reconcile with CC

> Second-opinion pass from the committed-object source (HEAD). Correctness vs DCML local key, not the gate.

## Responsibility
`analyzeKeyMode` — per-region **key-mode scoring**: enumerate all **252 candidates** (12 tonics × 21 modes),
score each = `scaleScore + triadScore + keySignatureScore + characteristicPitch + trueLeadingTone +
modePrior` (+ a −1.0 declared-mode hint, 4b-i), apply pairwise disambiguation to the top-2 same-signature
modes, rank, output `KeyModeAnalysisResult[]` + confidence. One responsibility (key scoring) with many
evidence sub-terms — not a conflation.

## Correctness gaps (vs DCML)
1. **[correctness · key-axis · STRUCTURAL] The relative major/minor tie — the central limit.** Relatives
   share the diatonic collection, so `scaleScore` + most terms give them near-identical scores; **note
   content alone cannot separate them.** The intended tiebreakers are weak/inert: 4b-ii showed
   `applyPairwiseDisambiguation` is **structurally INERT on the floor** (its clauses fire only when the
   relative's tonic is ABSENT; the floor is tonic-present-both → no-op exactly where needed), `trueLeadingTone`
   pulls the wrong aggregate direction, tonic salience is cap-blunted. So the scorer leans on EXTERNAL signals
   (the declared-mode hint, the cadence anchor) to break the tie — alone it frequently picks the wrong
   relative. Measured: the dominant key-S2 error class (~1383 floor regions flip without the declared crutch).
2. **[correctness · key-axis] 21-mode richness.** The church/exotic-mode candidates (Dorian/Mixolydian/…) can
   mis-win on a single b7/accidental in tonal music; mitigated by `modePrior` + same-signature-family
   selection, but a real risk.
3. **[correctness · partial-sig] `scoreKeySignatureProximity` anchors to the NOTATED signature** → mis-anchors
   on partial/modal signatures (the Dorian wall again).

## Completeness gaps
4. **[completeness · key-axis] Cannot complete the relative decision from notes** (above) — needs external
   cadential/global evidence.
5. **[completeness · key-axis] Per-region scoring over a lookahead window** → window-local coupling (the §4
   coupling the cadence anchor was built to avoid); modulation handled per-region but window-coupled.

## ★ Phase-2 synthesis — the audit is independently RE-DERIVING the constrained-joint target
Across the four key-axis layers audited, each is **insufficient ALONE**, and they are complementary:
- **keymodeanalyzer (this):** note-evidence side — *can't separate relatives from notes* (structural).
- **cadencekeyanchor:** cadence-evidence side — *tries* to break the tie, but over-fires on I→IV/I→V.
- **localmodulationdetector:** inherits the cadence imprecision (self-confirming spurious spans).
- **jointkeydecision (next):** the layer meant to COMBINE them.

So the key-axis correctness obligation is NOT per-layer — it is the **interaction**: the note-scorer's
relative-pair limit + the cadence-precision wall, resolvable only by (a) better cadence precision / calibration
upstream and (b) the **constrained-joint combination** of note + cadence + global evidence. **The per-layer
audit is independently confirming why `architecture_joint_inference.md` is the right target** — not from the
design narrative, but bottom-up from each layer's measured insufficiency. The obligations concentrate at:
**(1) cadence precision (the upstream root), (2) the joint combination (the synthesis layer), (3) the soft
calibration (the weighting).**

## Reconciliation targets (for CC)
- Confirm the relative-pair is the dominant key-S2 class + that the disambiguation terms are inert on the
  tonic-present-both floor (re-confirm the 4b-ii finding at source).
- Quantify the 21-mode mis-win rate (tonal pieces won by a church mode) vs DCML.
- Agree the synthesis: each key-axis layer insufficient alone → the joint combination is the obligation.
