# notation_seams — the §4.1 presentation-gate gap-scale measurement (seams part 2, P1)

This directory holds the **P1** deliverable of the notation consumer re-plumb
(`cc_instruction_notation_seams_2.md`, the ratified P0–P7 partition): the measured
correspondence that lets the record-path exposure gates preserve the legacy exposure
behavior **without inventing any calibration** (contract `cowork_notation_output_contract.md`
§4.1).

## The problem

On the legacy notation path, several presentation gates fire on
`KeyModeAnalysisResult.normalizedConfidence` (an emission sigmoid in `[0,1]`):

| legacy threshold | gate family |
|---|---|
| **0.35** | `modeNameConfidenceThreshold` — mode-suffix vs fallback-suffix |
| **0.50** | `kTentativeKeyExposureThreshold` / `supportsTentativeKeyExposure` / exposure-bucket lower |
| **0.80** | `kAssertiveKeyExposureThreshold` / `kAnnotateKeyConfidenceThreshold` / `hasAssertiveExposure` / bucket upper |

On the record path there is **no `normalizedConfidence`**. Per Cowork's binding P2 sharpening,
the record path carries the **RAW §3.3 key-axis content-score gap (nats)** in those fields —
`keyAxis.scores[committed] − max(other keyAxis.scores)` — and **no mapping of that gap into a
`[0,1]` pseudo-confidence is permitted** (a sigmoid/normalization would be an invented
calibration — the #19 / DT-2 defect the contract's §3.3 establishment-status rule forbids).

So each `>= threshold` gate must be re-declared as `gap >= g` for a gap-scale constant `g`
**on the nats scale**. These constants are **presentation policy, not inference** — chosen by a
documented, measured correspondence, re-tunable later as presentation policy.

## The method (measured correspondence, not a fit, not a guess)

1. **Measure** (`pipeline_snapshot_tests` — `DISABLED_SeamsGapMeasurement`, opt-in,
   measurement-only): over the snapshot corpus, in the same 16-measure window the goldens pin,
   record per **legacy** region the `normalizedConfidence` the gates read today, and per
   **record** committed segment the §3.3 key-axis content-score gap that replaces it. Emits
   `gap_measurement.json`. Run with:
   ```
   pipeline_snapshot_tests.exe --gtest_also_run_disabled_tests --gtest_filter='*SeamsGapMeasurement*'
   ```
2. **Choose** (`choose_exposure_constants.py`): for each legacy threshold, pick the gap
   constant `g` whose **duration-weighted** record firing rate (fraction of duration with
   `gap >= g`) most nearly equals the legacy duration-weighted rate (fraction with
   `conf >= threshold`). Emits `exposure_constants.json`.
   ```
   python tools/notation_seams/choose_exposure_constants.py
   ```

**Why duration-weighted:** the legacy and record arms segment the same tick span differently,
so a per-region/per-segment COUNT rate is not comparable across arms. Duration weighting is the
only fair cross-arm measure — the same segmentation-invariance principle as CLAUDE.md's robust
unit. The rule preserves the exposure **RATE**, not the per-site identity: which segments fire
differs between arms (the committed readings differ), and that difference is an EXPECTED
inference-driven difference for the P6 dual-arm classification, never bent toward legacy.

## The result

**The authoritative values live in the generated `exposure_constants.json`** (per-threshold:
`chosen_gap_nats`, `legacy_rate_dur`, `record_rate_dur`, `residual_dur`, plus the pool counts) —
they are NOT hand-transcribed here (#17f: figures enter docs only via generated artifacts, so a
re-run cannot leave a stale number in this README). Read that file for the constants.

Qualitatively, over this corpus and window: every record segment had a defined gap (no null),
all 11 scores produced a record with no error, the three chosen gap constants are **monotone in
the threshold** (higher confidence threshold → higher gap constant), and each preserves the
legacy duration-weighted exposure rate to within a small fraction of duration. The count rate is
recorded beside each constant but diverges (the arms segment the same span differently) — which
is exactly why it is NOT the selection basis.

The chosen constants are the values the record-path gates declare at their emitter sites in the later partition
units (P2 section-layer confidence fields; P4 implode `keyExposureBucket` / mode-suffix), each
carrying value + legacy rate + record rate + residual + this rationale, and the OI-182 row
executes there. **P1 measures and selects; it declares no constant in production code and touches
no production behavior** (the measurement test is opt-in `DISABLED_`; the notation output is
byte-identical).

## Files

- `choose_exposure_constants.py` — the selection instrument (stdlib only).
- `gap_measurement.json` — the raw per-region / per-segment measurement (generated, #17f).
- `exposure_constants.json` — the chosen constants + provenance (generated, #17f).
