# Stage 6 Design — the functional layer (NARROW first slice: tonicization labeling)

> **DRAFT — ratification-gated.** Cowork design, 2026-06-14. User chose **option C** (pivot to Stage 6)
> and the **narrow** entry (start with the highest-value low-risk slice, audit that sub-responsibility,
> then expand). Applies the user's **layer-by-layer audit method**: state the layer's single
> responsibility, audit correct+complete against THAT only — inputs assumed correct, consumers ignored.

---

## §1 — The functional layer: its single responsibility

**Responsibility:** *sequence-label harmonic FUNCTION over the already-decoded chord+key path.* Given the
chords (root/quality, from Stage 3), the key path + KeyArea (Stage 4), and the cadence instrument
(Stage 4c), assign each chord its functional role — tonal degree, T/S/D function, secondary/applied
relationship (tonicization), cadence membership, and the chromatic-predominant specials (aug6,
Neapolitan). Its OUTPUT is the functional label (the Roman numeral *with* its functional decorations,
e.g. `V/V` instead of a bare `II`).

**What it is NOT** (other layers' responsibilities — ignored here per the audit method): it does not
decide chord root/quality (Stage 3 chord layer), nor key/mode (Stage 4 key layer). It *consumes* those as
correct inputs. The existing `harmonicfunctionlayer` is the **chord-competition** layer (rcb/wSeq/wDim) —
NOT this; Stage 6 is a new, higher sequence-labeling pass.

This is exactly the layer the cadence work revealed was missing: the residual that fooled the cadence
detector (reading a tonicization as a cadence) is a *functional-understanding* gap that lives HERE.

---

## §2 — Inputs (assumed correct, per the audit method)

- **Chord path:** per-region root pc + quality (Stage 3 decoded output).
- **Key path + KeyArea:** the prevailing key/mode per region + the KeyArea spans (`analyzed_section.h`,
  Stage 4). *Known imperfect on the relative-pair floor* — see §7 scoping (the first slice is chosen to
  be largely independent of that imperfection).
- **Cadence instrument:** the committed `cadencekeyanchor` detector (Stage 4c) — available for cadence
  labeling in a later slice.
- **Ground truth / metric:** `compare_rn` (the DCML-only metric); per the metric-design investigation
  (`docs/precision_metric_design.md`), `classify_pair` **already credits a correctly-emitted secondary as
  exact** — so the functional gap is **EMISSION** (we don't emit the label), not the comparator. Stage 6's
  job is to emit.

---

## §3 — The narrow first slice: tonicization (secondary-dominant / applied-chord) labeling

**Why this slice first:** it is the single biggest precision slice — **S1 tonicization label-gap ≈ 17.7%**
of the disagreement mass (precision-headroom dossier) — and it is **low-risk "pure-add"**: it refines the
LABEL on readings whose root + global key are *already correct*, so it cannot regress the chord/key axes.
It is also **largely independent of the stuck relative-pair key floor** (those are correct-key cases by
construction), so it pays off now without waiting on Stage 4's floor.

**What it does:** recognize when a chord functions as a **secondary dominant / leading-tone (applied
chord)** of a non-tonic diatonic degree and emit the `/X` tonicization label (e.g. a D-major chord in
C major resolving to G is `V/V`, not a bare `II`/chromatic numeral). Mechanism proposal (validated, not
assumed, in the build's measurement):
- a chord is a candidate applied dominant of degree *d* if its root is the dominant (or its quality the
  applied-LT diminished) of the pitch class of degree *d* in the prevailing key, it carries the raised
  leading tone of *d* (a chromatic alteration vs the key — the same key-signature-relative test the
  cadence detector used), AND the following chord resolves to *d*;
- emit `V/d` (or `viio/d`, `V7/d`, …) per the label-vocabulary contract (§4).
This is the functional generalization of the cadence detector's V→I logic (there: tonic; here: any
diatonic degree), now applied WITH a known key (so it is not circular — Stage 6 consumes the resolved key).

**Out of this slice (later sub-steps):** full T/S/D state labeling, cadence-token labeling (consume the
cadence instrument), tonicization-vs-MODULATION disambiguation from KeyArea spans, aug6 / Neapolitan /
other chromatic predominants, and 6.2 (consolidate the 3 scattered quality-from-key feedback sites) / 6.3
(revisit the closed convention-gap buckets). Each is its own audited sub-responsibility.

---

## §4 — The label-vocabulary contract (pin it — resolves metric-design OQ-L2)

The metric-design investigation co-ratified a draft label vocabulary and left **OQ-L2 (secondary
normalization)** open. Pin it here, since the Stage-6 output spec IS the metric input spec:
- the applied/secondary form is the standard `<numeral>/<degree>` (e.g. `V/V`, `viio6/V`, `V7/ii`),
  degrees as Roman numerals of the prevailing key;
- define the normalization `compare_rn` uses to credit an emitted secondary as exact (must match the
  already-existing `classify_pair` crediting — confirm at source, do not re-invent);
- decide the canonical form for the ambiguous cases the DCML uses (e.g. applied-to-minor-degree casing).
This contract is co-ratified with the slice; the build confirms `compare_rn` already credits it (the
metric-design finding) rather than changing the comparator.

---

## §5 — Behavior-change surface + the audit gate

This is the **functional axis's first intentional change**. It changes the RN OUTPUT (labels), so:
- **Chord axis MUST hold:** root/quality/key unchanged → **BIR gate 57/23/57 byte-identical** (tonicization
  is a label refinement, not a root/key change). An un-adjudicated BIR move is a hard stop.
- **Snapshots WILL move** (RN strings gain `/X`): DCML-adjudicate each, refresh only verified-correct.
- **Measure on `compare_rn`** (mode-present; the corpus has key): the **S1 recovery** (how many
  tonicization-label-gap cases the slice closes) + a **false-label rate** (the audit's "complete +
  CORRECT" check — it must not emit `/X` on chords that are NOT applied, the analogue of the cadence
  detector's contradiction rate). Low false-label rate is the binding constraint.

---

## §6 — Staged build (narrow → audit → expand)

- **6-tonic-i — the tonicization labeler (this design's deliverable).** Build the applied-dominant
  detector + the `/X` emission (composing functional-labeling pass, distinct from `harmonicfunctionlayer`).
  Measure: S1 recovery + false-label rate + chord-axis-gate-held + snapshot adjudication. HELD, ratified.
  **Audit gate (layer-by-layer):** is the tonicization sub-responsibility correct (no false `/X`) and
  complete (covers the S1 applied-chord cases)? Pin the residual as this sub-layer's obligation.
- **6-ii+ (later, separately designed):** cadence-token labeling (consume the cadence instrument), T/S/D
  function states, tonicization-vs-modulation from KeyArea, aug6/Neapolitan; then 6.2 / 6.3.

---

## §7 — For user ratification
1. Approve the functional layer's stated responsibility (§1) and the **narrow tonicization-first** slice
   (§3), audited in isolation per the layer-by-layer method.
2. Approve pinning the label-vocabulary contract (§4) here (resolving metric-design OQ-L2), built to match
   the EXISTING `compare_rn`/`classify_pair` crediting (confirmed at source, comparator unchanged).
3. Confirm the audit gate (§5): chord-axis BIR held byte-identical; the binding metric is S1 recovery vs a
   low false-label rate; snapshots DCML-adjudicated.
4. On ratification, Cowork writes the 6-tonic-i CC instruction (build the applied-dominant labeler +
   measure; chord axis byte-identical; HELD).

## §8 — Stop conditions (carried into the 6-tonic-i instruction)
- The labeler changing chord root/quality/key (it must only add the functional `/X` label) — chord-axis
  gate moving is a STOP.
- A high false-label rate (emitting `/X` on non-applied chords) — report as the slice's
  correctness gap; do not ship a noisy labeler (the analogue of the cadence contradiction bar).
- The labeler needing a richer key/segmentation input than exists (a dependency on a not-yet-correct
  input layer) — surface as a cross-layer finding, do not paper over it.
- Re-inventing the `compare_rn` secondary crediting instead of matching it — confirm at source first.
