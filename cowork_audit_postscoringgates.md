# Cowork independent audit — postscoringgates (gate layer A–L, the dissolution target) — to reconcile with CC

> Second-opinion pass from the committed-object source (HEAD) + the gate provenance.

## Responsibility
`applyPostScoringGates` — **post-scoring chord-IDENTITY disambiguation**: resolve the share-tone / inversion /
symmetric ambiguities the local competition left wrong (MinorAdd6↔HalfDim7 = same pcs; Augmented/dim
symmetric; first/second inversions) using **CONTEXT** — key membership, the *next-region* root, stepwise
bass, metric duration. Gates A–L (~12), Baroque/classical-calibrated (`preferMinorOverMajorAdd6`; margins
`kGateI=0.45 / kGateK=0.20 / kGateL=0.35`). This is the **compensation layer** + the **refactor-#2
dissolution target**.

## Correctness
1. **[correctness — helpful] The gates improve their target ambiguity classes** (the BIR cases) — each is a
   calibrated rule for a specific mis-identification.
2. **[correctness — accretion] Heuristic accretion** (A–L, intricate sequencing, the `originalWinner`-capture
   bug history) — hard to reason about, like the competition bonuses.
3. **[correctness — style] Baroque/classical-calibrated** → may not generalize (Jazz).

## Completeness
4. **[completeness] Gate coverage gaps** — ambiguities no gate covers leave the (possibly wrong) competition
   winner; the symmetric dim7/aug floor remains pc-undefined for some.

## ★ Phase-2 — the UNIFYING finding: both axes are "local decision needs CONTEXT"
The gates exist because the chord decision is **LOCAL** (per-region competition) — they patch in
*next-region + key* context **post-hoc**. That is the SAME root issue as the key axis:
- **Key axis:** the local per-region scorer can't decide the relative pair / the modulation → needs
  **global/cadential context** (the cadence anchor, the joint key-path).
- **Chord axis:** the local competition can't decide the share-tone/inversion identity → the gates patch in
  **next-region/key context**.
Both are **the local decision being insufficient → wanting a JOINT/contextual decision.** So the per-layer
audit independently re-derives that the **constrained-joint architecture is the right target for BOTH axes**,
bottom-up — the gates are the chord-axis *evidence* of it, exactly as the cadence/relative-pair walls are the
key-axis evidence. The gate layer's obligation IS its own dissolution (refactor #2: the joint decision
subsumes each gate, proof-obligation per gate).

**Tractability split (a prioritization insight):**
- **Chord-axis joint is TRACTABLE** — the gates already *work* (context patches that pass the BIR gate), so
  dissolving them into a joint decision is mostly a refactor; the contextual fixes are proven hand-buildable.
- **Key-axis joint is the HARDER wall** — the same joint approach is right, but the context *evidence*
  (cadence) is imprecise (the I→IV/I→V wall), so it needs precision/calibration before the joint pays off.
→ The chord-axis gate-dissolution is the **lower-risk** joint-architecture step; the key-axis joint is
gated on evidence precision.

## Reconciliation targets (for CC)
- Confirm each gate's contextual inputs (next-region root / key / stepwise bass) — i.e. that every gate IS a
  context patch a joint decision could subsume.
- Confirm the Baroque-calibration / Jazz-generalization concern empirically.
- Agree the unifying "local-needs-context" reading + the chord-tractable / key-walled split.
