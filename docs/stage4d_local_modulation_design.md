# Stage 4d Design — local-modulation detection (the key layer learns to modulate)

> **DRAFT — ratification-gated.** Cowork design, 2026-06-14. Follows the metric-check reframe (the biggest
> precision slice S1 ≈ 17.7% is **95.6% local-modulation detection — a Stage-4 KEY gap**, not Stage-6
> tonicization labeling) and the key-path scoping (`cc_modulation_keypath_scoping_dossier.md`,
> Cowork-verified: the resolver is a global-key estimator **anchored to the notated signature** via
> `scoreKeySignatureProximity` + a 16-beat lookback + the declared anchor, with **no local-key state at
> all** — it tracks DCML's modulations on only 9.7% of regions vs DCML's 39.9%; the gap is a **structural
> absence**, not a mis-tuned margin). No code until ratified.

---

## §1 — The gap and the responsibility

**Responsibility (key layer):** decide not just a global key but **where the music modulates to a local
key**, and commit those local-key spans. Today the resolver re-estimates a single signature-anchored key
per region and resists switching; it cannot represent "this passage is in the dominant for 8 bars." This
is the structural capability to add. It is the **biggest precision lever** (~95% of S1; gap ~3006 regions /
29.7%; realistic ceiling ~1800–2500, capped by the cadence detector's ~75% realized fraction).

This is a deliberate **behavior change on the key axis** — the resolved key feeds chord emission
(`basisIndep`) and the RN labels, so the BIR gate (57/23/57 — *superseded 2026-06-26: live gate now 53/24/53, L3-wiring delta; CLAUDE.md authoritative*) is **medium-risk** (chord roots can move on
the diatonic-sensitive subset), snapshots move, and it must be DCML-adjudicated and re-gated on all three
presets. Staged measure-first (below).

---

## §2 — The mechanism: cadence-confirmed sustained local-key hypothesis

A local key is committed only when it is both **established** (sustained) and **confirmed** (cadenced) —
exactly the brief-vs-sustained signal the metric-check found separates real modulations (97%) from brief
tonicizations (the ~4% home-key residue, which stay home and become the 6-tonic-i brief-only branch):

1. **Local-key candidates** come from the **committed key-agnostic cadence instrument** — each detected
   authentic cadence exposes a local tonic (its resolution degree), derived from absolute root motion +
   leading tone, **with no resolved key** (so no circularity — §3).
2. **Establishment test:** the candidate local key must span ≥ a threshold (the scoping's ≥5-chord / sustained
   signal) — a run of regions consistent with that local key's diatonic collection.
3. **Confirmation test:** a cadence (V→I of the local tonic) inside the span.
4. **Commit:** when both hold, **override the home-signature pull** for that span — introduce a local-key
   state that re-keys those regions to the local key. The home anchor (`scoreKeySignatureProximity`,
   lookback, declared hint) must **yield** to a confirmed-and-sustained local key, not veto it. Outside
   committed spans, behavior is unchanged (still the signature-anchored global estimate).

Provisional thresholds `[empirical — Stage-5 fits]`; the build measures and the user sets the bar.

---

## §3 — No circularity / key-agnosticism (the architecture constraint)

**The local-key hypothesis MUST derive from key-agnostic signals — the cadence instrument (key-agnostic by
construction) + raw region structure (root motion, diatonic-collection consistency) — NOT from the current
KeyArea**, which is a downstream post-grouping of the resolved (stay-home) key (`sectionanalyzer.cpp:930`)
and would make the detector circular. The flow stays strictly feed-forward: chords → key-agnostic cadence →
local-key hypothesis → re-keyed key path → KeyArea (rebuilt downstream). This is the same discipline that
made the cadence detector usable; it is the load-bearing soundness property and a hard design rule.

---

## §4 — Integration (the audit-method placement)

- The modulation commit lives in the **Stage-4 key layer** — a **section/piece-scoped pass** over the
  per-region key estimates that detects + commits local-key spans (it needs cross-region context the
  per-region resolver lacks), feeding the re-keyed result into the existing `KeyArea` grouping. It is NOT
  the per-region `analyzeKeyMode` scorer (which stays the local-evidence estimator) and NOT Stage 6
  (which only *labels* tonicization-vs-modulation from a committed KeyArea — and now mostly defers to this).
- The home-pull terms (`scoreKeySignatureProximity` etc.) are **not removed** — they remain correct outside
  modulations; the modulation pass overrides them only within a confirmed span.
- All composing-zone. The only possible off-limits future need is optional fermata plumbing for phrase-end
  salience (a recall refinement, not required for v1) — surface it then.

---

## §5 — Staged build (measure-first, per discipline)

- **4d-i — build the modulation detector + MEASURE (no production re-keying → byte-identical).** Produce
  local-key spans diagnostically; measure against DCML modulations with the **de-masking diagnostic**
  (`--partial-key-breakdown`) + the modulation-track-rate (9.7% → ?). **The binding metric is modulation
  CORRECTNESS (track-rate + the de-masked partial split), NOT the gameable rn_agree** — a span we commit
  must be a real DCML modulation (precision) without missing the real ones (recall). Production key
  untouched → BIR 57/23/57, snapshots 11/11 zero-diff. Branch on the realized precision/recall.
- **4d-ii — wire the re-keying into the production key path + re-gate.** The behavior change: re-keyed
  regions change RN + emission. DCML-adjudicate every moved gate case; **un-adjudicated BIR=false increase
  on any preset = hard stop**; refresh only verified-correct snapshots; re-gate all three presets. HELD,
  ratified.
- **4d-iii (later):** recall refinements (fermata salience, weaker-cadence spans) against the 4d-ii residual.

---

## §6 — Measurement + targets
- The **de-masking diagnostic** is the honesty instrument (it exposes a committed home-label credited
  against a DCML local key). Report modulation track-rate, the masked-partial fraction (was 19.8% / 237),
  precision/recall of committed spans, and the de-masked real key correctness.
- Chord axis: BIR 57/23/57 DCML-adjudicated (medium risk). Key axis: S1 recovery (the ~2001 cases).
- The 6-tonic-i tonicization predicate becomes the **brief-only branch** for the home-key residue once
  modulations are committed (a small downstream follow-on, not this design).

---

## §7 — For user ratification
1. Approve the responsibility (§1) + the cadence-confirmed sustained-span mechanism (§2).
2. Approve the **no-circularity rule** (§3): local-key hypothesis from key-agnostic cadence + raw structure,
   never the key-dependent KeyArea.
3. Approve the integration as a section/piece-scoped key-layer pass (§4) and the measure-first staging (§5):
   4d-i build+measure byte-identical → 4d-ii wire+re-gate.
4. On ratification, Cowork writes the 4d-i instruction (build the detector + measure track-rate/precision/recall
   via the de-masking diagnostic; production key untouched; HELD).

## §8 — Stop conditions (carried into 4d-i)
- The local-key hypothesis depending on the resolved key / the current KeyArea (circularity) — STOP; it
  must be key-agnostic (cadence + raw structure).
- 4d-i changing production key output (it is measurement-only → byte-identical) — STOP.
- Committed spans with poor precision (we modulate where DCML doesn't) — report; do not wire a noisy detector.
- 4d-ii regressing the chord-axis gate un-adjudicated — hard stop.
