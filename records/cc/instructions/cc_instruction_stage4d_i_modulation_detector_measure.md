# CC Instruction: Stage 4d-i — build the local-modulation detector + MEASURE (no production re-keying)

## Authorization + framing

Implements the **ratified** `docs/stage4d_local_modulation_design.md` (§1 responsibility, §2 mechanism,
§3 no-circularity rule, §4 integration, §5 staging — user ratified items 1–3, 2026-06-14). **4d-i builds
the detector and MEASURES its correctness diagnostically — the production key path is UNTOUCHED → byte-
identical.** Re-keying production is **4d-ii**, separately ratified, gated on this measurement (the
proven measure-before-wire discipline). The detector is the biggest precision lever (~95% of S1; gap ~3006
regions; ceiling ~1800–2500).

Zone: `src/composing/` (the detector) + `tools/` (diagnostic + measurement). HELD — no commit. Tag every
claim `[probe]`/`[code]`/`[oracle]`.

## ⛔ The no-circularity rule (§3 — HARD, the load-bearing soundness property)

**The local-key hypothesis MUST derive ONLY from key-agnostic signals** — the committed cadence instrument
(`detectAuthenticCadences`, which exposes per-cadence local tonics from absolute root motion + leading tone,
NO resolved key) + raw region structure (root motion, pitch content / diatonic-collection consistency with
the *hypothesized* local key). **It MUST NOT read the resolved key, `KeyModeAnalysisResult`, or the current
`KeyArea`** (which is built from the stay-home key → circular). Confirm at source the detector's inputs are
key-agnostic. If it cannot be built without the resolved key, that is a finding — STOP and report.

## Build — the modulation detector (section/piece-scoped)

A new composing pass (its own file / the section layer — CC's call; NOT the per-region `analyzeKeyMode`
scorer, NOT Stage 6). It produces **candidate local-key spans** (diagnostic only — it does NOT re-key the
production result this run):
1. **Candidates** = the per-cadence local tonics from `detectAuthenticCadences` (the per-cadence list, NOT
   the single global `aggregateGlobalAnchor`).
2. **Establishment test:** the candidate local key spans ≥ a threshold (provisional **≥5 chords / a sustained
   run**, `[empirical — Stage-5 fits]`) of regions consistent with that local key's diatonic collection
   (raw pitch content vs the hypothesized collection — key-agnostic).
3. **Confirmation test:** a cadence (V→I of the local tonic) inside the span (from the cadence instrument).
4. **Commit a candidate span** only when establishment AND confirmation hold (conservative — prefer missing
   a borderline modulation over inventing one, per the ratified precision-lean). Output the span list per
   piece.

## Measure (DIAGNOSTIC, byte-identical) — the deliverable

A read-only diagnostic (a `batch_analyze` dump of candidate spans + a `tools/` script) comparing the
detector's candidate spans to **DCML's modulation annotations** (local keys). Report `[probe][oracle]`:
1. **Precision (the BINDING constraint):** of the spans we commit, how many are a real DCML modulation
   (we must NOT modulate where DCML doesn't — the over-modulation / false-key analogue of the cadence
   contradiction + the tonicization false-label rate). Characterize the false commits.
2. **Recall / track-rate:** of DCML's modulations, how many do we catch — the lift from the current 9.7%
   toward the ~1800–2500 realistic ceiling. Misses characterized (no cadence in span, span too short, etc.).
3. **Reference baseline:** run the de-masking `compare_rn --partial-key-breakdown` to restate the current
   masked-modulation error (was ~19.8% / 237 of partial) so the detector's potential is framed against it.
4. **Per-span sanity:** spot-check a sample of committed spans against DCML (oracle) — right local key, right
   extent.

## Byte-identity gate (4d-i is measurement-only)
Production key/RN output UNCHANGED — the detector is diagnostic-only, never feeds the resolver/KeyArea this
run. Prove: **BIR 57/23/57**, `pipeline_snapshot_tests` **11/11 zero golden diffs**, composing/notation
suites green. Any movement = the detector leaked into the key path = STOP.

## Held / report — `cc_stage4d_i_report.md`
The detector at source (key-agnostic inputs CONFIRMED — no resolved-key/KeyArea dependency), the
precision/recall/track-rate of candidate spans vs DCML, the over-modulation (false-commit) characterization,
the de-masking baseline, per-span oracle spot-checks, the byte-identity proof. **Branch recommendation:**
high precision + worthwhile recall ⇒ proceed to 4d-ii (wire the re-keying + re-gate all three presets,
DCML-adjudicated); poor precision (over-modulating) ⇒ refine the establishment/confirmation gates (report
what's misfiring). Every number `[probe]`, every root `[oracle]`. HELD — no commit.

## Stop conditions
- The detector reading the resolved key / `KeyModeAnalysisResult` / the current `KeyArea` (circularity) —
  STOP; inputs must be key-agnostic (cadence + raw structure). This is the ratified hard rule.
- Production key/byte-identity moving (BIR/snapshot/suite) — the detector leaked into the key path; STOP.
- Low precision (committing spans DCML doesn't modulate) — report as the gate-tuning finding; do NOT
  recommend wiring an over-modulating detector.
- Needing an off-limits (`src/notation`/`src/engraving`) edit — surface it (scoping said composing-zone;
  optional fermata salience is a later 4d-iii refinement, not this run).
