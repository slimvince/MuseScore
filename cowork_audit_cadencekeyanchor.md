# Cowork independent audit — cadencekeyanchor (to reconcile with CC's primary audit)

> My second-opinion pass, from the committed-object header/impl + the prior verified measurements
> (B/B2 investigations). Correctness/completeness judged vs the TRUE analysis (DCML oracle), not the gate.
> To be reconciled with `cc_audit_cadencekeyanchor_report.md`.

## Responsibility (the contract)
The header exposes **two** jobs: `detectAuthenticCadences` (key-agnostic V→I detection) + `aggregateGlobal
Anchor` (vote the cadences into one global tonic+mode). Borderline **dual responsibility** — and the detection
half is **a reusable primitive consumed by more than this layer** (the modulation detector's
`detectLocalModulations` consumes the same cadence stream). → **Phase-2 decomposition note:** the cadence
*detection primitive* and the *global-anchor aggregation policy* may warrant being separate layers.

## Correctness gaps (vs DCML)
1. **[correctness · key-axis · behavior-changing] The leading-tone test structurally false-positives on
   I→IV / I→V.** The test requires the dominant's leading tone `(root(a)+4)` present in `a` — but that pc is
   `a`'s **major third**, present in *every* major triad. So any major triad → triad-a-fourth-above (= I→IV)
   passes, as does I→V; the detector cannot tell a genuine V→I from a plain I→IV/I→V **without a key** (the
   price of key-agnosticism). Measured (B): the resulting anchor is **~44% pin-wrong vs DCML**; subdominant
   spans 72% spurious. The 4c-iii salience markers (`chromaticLeadingTone`/`endsPhrase`/Picardy) only
   *down-weight* these in aggregation — detection still emits the false cadences. This is the recurring
   precision wall; likely needs the constrained-joint "cadence = SOFT" treatment or better key-agnostic
   discrimination, not a local fix.
2. **[correctness · key-axis · behavior-changing] `chromaticLeadingTone` mis-fires on partial/modal
   signatures.** It is computed vs the NOTATED signature collection; a Dorian-notated piece's true raised LT
   can read as diatonic (or vice versa) → wrong salience on exactly the partial-sig pieces (the bridge-anchor
   wall).

## Completeness gaps (vs the case space)
3. **[completeness · key-axis] Authentic-only.** Detects only descending-fifth V→I. Misses half (→V),
   plagal (IV→I), deceptive (V→vi), phrygian-half. Pieces whose key is best signaled by a non-authentic
   cadence are un/mis-anchored. (Partly within the stated narrow contract, but a real coverage limit for
   "correctly anchor every piece".)
4. **[completeness · key-axis] Global-only — no modulation.** One global (tonic,mode) per span; a modulating
   piece has multiple local keys the anchor can't represent (delegated to the separate modulation layer).
5. **[completeness · key-axis] Incompletely resolves its OWN target.** Built to break the relative-major/minor
   tie — but only lifts relative-pair correctness ~78→82% (B2), and on partial-sig pieces it mis-resolves
   (Dorian → wrong relative). The cases it was created to solve are the ones it's least complete on.
6. **[completeness/robustness · key-axis] Windowing-unstable.** On a windowed (bridge 16-measure) input the
   anchor flips vs the stable full-score anchor (B2: mozart→F, corelli→Gm) — correctness depends on input
   window size.

## Phase-2 carry-forward (interactions — noted, not chased)
- As a SOFT evidence producer the imprecision is "tolerable," but its false cadences **propagate** to the
  modulation detector + the joint decision (the non-chorale regressions) — so these obligations DO matter for
  key-axis correctness.
- Detection-primitive shared with the modulation detector → decomposition (above).
- The leading-tone ambiguity is *inherent* to key-agnostic detection — the obligation is really "the
  key-agnostic cadence-precision ceiling," which points at calibration / the constrained-joint soft-decode,
  not a within-layer patch.

## Reconciliation targets (what CC's empirical audit should quantify)
- The detection false-positive rate vs DCML (confirm the I→IV/I→V mechanism + the ~44%/72% numbers).
- The anchor's accuracy vs DCML global key, split by relative-pair / modulation / partial-sig.
- The authentic-only coverage (how many DCML pieces have no detectable authentic cadence → un-anchored).
- Agreement on the dual-responsibility / shared-primitive decomposition note.
