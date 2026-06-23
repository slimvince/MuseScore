# Cowork independent audit — localmodulationdetector (to reconcile with CC)

> Second-opinion pass from the committed-object source (HEAD). Correctness vs DCML modulations, not the gate.

## Responsibility
`detectLocalModulations` — key-agnostic local-modulation **span** detection: candidates = per-cadence local
tonics (from `detectAuthenticCadences`); assign each region to the nearest collection-consistent cadence's
key; commit a span when a run is **SUSTAINED (≥5 regions) AND CONFIRMED (an authentic cadence of that key
inside)**. Output: spans + the global anchor. **Consumes the cadence-detection primitive `detectAuthentic
Cadences` — the SAME primitive `cadencekeyanchor` aggregates.** → confirms the phase-2 decomposition: the
cadence primitive has *two* consumers (anchor + modulation), so it should be its own layer.

## Correctness gaps (vs DCML)
1. **[correctness · key-axis · inherits-cadence-wall] Inherits the cadence false positives.** Candidates come
   from `detectAuthenticCadences`, which over-fires on I→IV/I→V → the spurious subdominant/dominant tonics
   become modulation candidates and **commit spurious spans** (measured 4d-i: precision **47%**, ~43% of FPs
   are exactly the dominant/subdominant misreads; the non-chorale regressions).
2. **[correctness · key-axis] The CONFIRMATION gate self-confirms the spurious case.** A span is "confirmed"
   by an authentic cadence of its key inside it — but the *same* spurious I→IV "cadence to IV" that seeds the
   F span also satisfies its confirmation. So the gate intended to validate a real modulation is
   **circularly satisfied by the false positive** → it cannot filter the spurious spans.
3. **[correctness · key-axis] Sustained-gate insufficient for sustained FPs.** The ≥5-region gate filters
   brief tonicizations, but the I↔IV oscillation FPs are themselves sustained (4d-i: over-mod FPs are
   sustained) → the gate doesn't catch them. The loose collection tolerance (`kPitchTolerance=2`; C vs F
   differ by one pc) lets a region be "consistent" with several nearby keys → assigned to the nearest, which
   may be the spurious one.

## Completeness gaps (vs the modulation case space)
4. **[completeness · key-axis] Recall ~33% (4d-i)** — misses ~2/3 of true DCML modulations (their cadence
   isn't found, or the sustained+confirmed gates reject them).
5. **[completeness · key-axis] Authentic-cadence-confirmed only.** A modulation signaled by a half/plagal
   cadence, or by sustained scale change without an authentic cadence, is undetected.
6. **[completeness · key-axis] Inherits the relative-pair / partial-signature weaknesses** of the cadence
   anchor → mis-detects on exactly those.

## Phase-2 carry-forward
- **Shared cadence primitive** (anchor + modulation consumers) → decomposition.
- **Correctness is upstream-bounded by the cadence-precision wall** — the modulation detector's own gates
  (sustained/confirmed) provably cannot filter the self-confirming spurious cadences, so the root obligation
  is the cadence layer, not here. This is the third key-axis layer in a row whose central correctness gap is
  the SAME cadence I→IV/I→V ambiguity → a strong cross-layer signal that the fix is upstream / constrained-
  joint-soft, not per-layer.

## Reconciliation targets (for CC)
- Confirm precision 47% / recall 33% vs DCML + the FP composition (subdominant/dominant share).
- Confirm the self-confirmation mechanism (does any committed spurious span lack an *independent* confirming
  cadence — i.e. is every FP self-confirmed?).
- Agree the shared-primitive decomposition + the upstream-bounded correctness.
