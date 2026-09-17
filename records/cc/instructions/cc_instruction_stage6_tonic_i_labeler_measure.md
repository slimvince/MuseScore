# CC Instruction: Stage 6-tonic-i — build the tonicization (applied-dominant) labeler + MEASURE (no wiring)

## Authorization + framing

Implements **ratified** `docs/stage6_functional_layer_design.md` (the functional layer's narrow first
slice: tonicization labeling). **Refinement (flagged, in the safer direction):** the design §6 implied
6-tonic-i would wire the label into the RN output. Instead — per the **measure-before-wire** discipline
that caught the weak cadence detector at 4c-i — **6-tonic-i builds the labeler and MEASURES its realized
quality DIAGNOSTICALLY, with production RN output UNCHANGED (byte-identical).** Wiring the label into the
emitted RN is **6-tonic-ii**, separately ratified, gated on this measurement. The tonicization labeler's
**false-label rate is unknown**; measure it before changing any output.

Zone: `src/composing/` (the labeler) + `tools/` (the diagnostic + measurement). HELD — no commit.
Never-guess: read the RN-formatting + metric code at source; tag every claim `[probe]`/`[code]`/`[oracle]`.

## The functional layer's responsibility (audit frame — this slice only)

A NEW functional-labeling pass over the decoded region sequence — **distinct from `harmonicfunctionlayer`**
(that is the chord-COMPETITION layer). Its inputs are assumed correct (the audit method): per-region chord
root/quality (Stage 3) and the **resolved key/KeyArea** (Stage 4 — Stage 6 legitimately consumes the
resolved key; using it is NOT circular here, unlike the cadence detector which had to avoid it). This slice
labels exactly one sub-responsibility: **tonicization (applied-dominant/leading-tone of a non-tonic degree).**

## Build — the tonicization labeler (proposal; validated by §measure, not assumed)

For each region pair (a → b), in the prevailing key, a is an **applied chord of diatonic degree d** (d ≠ tonic)
when [code-driven, read what `chordResult`/key expose]:
- **Applied dominant `V/d` / `V7/d`:** `root(a) ≡ (pc(d) + 7) mod 12`, a is major/dominant quality, a carries
  the **raised leading tone of d** = `(pc(d) + 11) mod 12` present in a's pitch content **and chromatic vs
  the prevailing key** (an accidental — the key-signature-relative test), AND `root(b) == pc(d)`.
- **Applied leading-tone `viio/d` / `viio7/d`:** `root(a) ≡ (pc(d) + 11) mod 12`, a is diminished, resolves to d.
- Emit the label `V/d` (or `V7/d`, `viio/d`, `viio7/d`) with **d written as the Roman numeral of the prevailing
  key** (the §contract form). The **resolution-to-d requirement + the chromatic raised-LT requirement** are the
  false-positive guards (the analogue of the cadence detector's resolution/chromatic discriminators).

Place it as a composing functional-labeling pass (new file under `analysis/function/` or similar — CC's call;
NOT inside `harmonicfunctionlayer`). It computes a per-region tonicization label or "none"; it does **not**
mutate chord root/quality/key.

## Confirm the label-vocabulary contract at source (do NOT re-invent the comparator)

The metric-design investigation (`docs/precision_metric_design.md`) found `compare_rn`'s `classify_pair`
**already credits a correctly-emitted secondary as exact**. **Read `compare_rn.py` / `classify_pair` at
source** and match the labeler's `<numeral>/<degree>` output form + normalization to what the comparator
already credits (resolves metric-design OQ-L2). Report the exact form. Do not change `compare_rn`.

## Measure (DIAGNOSTIC, byte-identical) — the deliverable

A read-only diagnostic (a `batch_analyze` dump of the candidate tonicization label per region, like the
cadence dump) + a `tools/` measurement script comparing the candidates to DCML's secondary/applied labels
(reuse `compare_rn`'s secondary handling). Report `[probe][oracle]`:
1. **False-label rate (the BINDING constraint):** of regions where the labeler emits a `/d`, how many are
   NOT an applied chord per DCML (precision). This must be **low** to ever wire (the tonicization analogue
   of the cadence contradiction rate). Characterize the false positives.
2. **S1 coverage / recovery (recall):** of the DCML applied-chord cases on **correct-key** readings (the S1
   tonicization-label-gap population — identify via `compare_rn`), how many does the labeler correctly catch?
   This is the realized share of the ~17.7% S1 slice.
3. **Scope note:** measure primarily on the **correct-key** subset (this slice is pure-add there); wrong-key
   (relative-pair floor) cases are out of scope (the key layer's problem, not this slice's).

## Byte-identity gate (6-tonic-i is measurement-only)
Production RN output is UNCHANGED — the labeler is diagnostic-only, not emitted into the resolver/formatter
path. Prove it: **BIR 57/23/57**, `pipeline_snapshot_tests` **11/11 zero golden diffs**, composing/notation
suites green. Any movement = the labeler leaked into production output = STOP.

## Held / report — `cc_stage6_tonic_i_report.md`
The labeler at source (inputs + the applied-chord predicate + the false-positive guards), the confirmed
label-vocab form (matched to `compare_rn`, not re-invented), the **false-label rate + S1 recall**, the
byte-identity proof, false-positive characterization. **Branch recommendation:** low false-label + worthwhile
recall ⇒ proceed to 6-tonic-ii (wire the label into the emitted RN; chord axis byte-identical, snapshots
DCML-adjudicated); high false-label ⇒ refine the guards (report what's misfiring). Every number `[probe]`,
every root `[oracle]`. HELD — no commit.

## Stop conditions
- Production RN / byte-identity moving (BIR / snapshot / suite) — the labeler leaked into output; STOP
  (6-tonic-i is measurement-only).
- The labeler mutating chord root/quality/key (it must only PRODUCE a label) — STOP.
- Re-inventing or editing `compare_rn`'s secondary crediting instead of matching it — confirm at source first.
- A high false-label rate — report as the slice's correctness gap (refine the guards); do NOT recommend wiring
  a noisy labeler.
- Needing a richer key/segmentation input than exists (dependency on a not-yet-correct input layer) — surface
  as a cross-layer finding, do not paper over it.
