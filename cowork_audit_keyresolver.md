# Cowork independent audit — keyresolver (the ACTIVE production resolver) — to reconcile with CC

> Second-opinion pass from the committed-object source (HEAD). Correctness vs DCML local key.

## Responsibility
`resolveKeyAndModeRanked` — the **active production per-region key resolution orchestrator**: read notated
signature + declared mode → `partialSignatureCorrection` → collect a lookback + dynamic-lookahead pitch
window → call `analyzeKeyMode` (the scorer) → apply **hysteresis** (temporal smoothing) → fallback for
degenerate openings. Output: the ranked region key. (The dormant `jointkeydecision` is its intended
replacement — see phase-2.)

## Correctness gaps (vs DCML)
1. **[correctness · key-axis · inherits-scorer] Relative-pair limit inherited** from `analyzeKeyMode` — the
   resolver cannot separate relatives any better than the scorer it wraps.
2. **[correctness · key-axis] Hysteresis trades flip-noise for ENTRENCHMENT.** The `relativeKeyHysteresisMargin`
   resists switching mode at same-signature (relative) boundaries — good for consistency, but if the opening
   region's relative is WRONG it **entrenches the error** (resists the correction that later evidence wants).
   A local-greedy smoothing, not a global-optimal decode.
3. **[correctness · key-axis] Dynamic-lookahead window coupling.** Expanding the window until "confident"
   crosses phrase/modulation boundaries → a window spanning a key change mixes collections (the §4 coupling
   the cadence anchor was built to avoid).
4. **[correctness/completeness · partial-sig] `partialSignatureCorrection` is declared-gated + one-step.**
   Fires only when a declared mode is present (zero-sig / mode-absent partial-sig stems uncorrected) and only
   one accidental's worth — multi-step modal signatures unhandled.

## Completeness gaps
5. **[completeness · key-axis] Modulation LAG** — hysteresis resists key changes, so a real modulation is
   adopted late (or resisted).
6. **[completeness · partial-sig] Modal/partial signatures** only via the narrow declared-gated correction.

## Phase-2 carry-forward — DUPLICATE decision path
- `keyresolver` (production, ACTIVE) and `jointkeydecision` (dormant) are **two key-decision paths**; the
  joint decision is the intended replacement (J-key-iii, dormant). The resolver's **hysteresis** = the OLD
  local-greedy temporal smoothing; the joint decision's **global key-path Viterbi** = the principled
  replacement. So the resolver's correctness gaps (entrenchment, window coupling, the local greedy nature)
  are precisely what the joint decode targets → the obligation is the migration, not patching the resolver.

## Reconciliation targets (for CC)
- Quantify hysteresis entrenchment (regions where the resolved key is wrong AND hysteresis blocked the correct
  challenger).
- Confirm the partial-sig correction's declared-gated coverage hole.
