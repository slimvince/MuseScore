# CC C1 — Reliability instrumentation: curves per (layer × decision × preset) on the ratified A-8 unit

> **READ-ONLY / MEASUREMENT-ONLY. No fitted maps, no squash-map/θ change, no gate change, no inference
> behavior change.** This report MEASURES empirical correctness as a function of published confidence per
> (layer × decision), against human GT, on the ratified A-8 unit (union-of-boundaries, duration-weighted,
> variant (b) DCML-only) for the harmonic rows and on the 16-dev-bed TSV oracle for the phrase/cadence rows.
> It delivers **reliability curves + calibration diagnostics** (contract §6 **C1**). It does NOT deliver fitted
> Class-P maps or any θ — those are the Stage-5 fitter's (C2/C3). Every finding below is **RECORDED for the
> fitter, never acted on** (Task 4).
>
> **Provenance.** Base HEAD `d1d4d3d7f0` ([probe] `git rev-parse --short HEAD`). Frozen gate corpus manifest
> `git_hash = 0dd64660f4`, `complete = true`, 352/352 each preset. New instrument `tools/c1_reliability.py`
> + two additive **default-off** dump fields in `tools/batch_analyze.cpp`, committed at **`088ba617b0`**
> (`feat(tools):`, local/unpushed/fork-only). This report + the CLAUDE.md riders are the docs commit. Every
> quantitative claim is **[probe]** (ran the instrument, read output). The harness reuses the ratified A-8
> cell loop (`a8_rebaseline_measure.build_piece_grid`, self-validated byte-for-byte vs `grid_score_regions`
> on every piece) + the pinned `classify_pair`/key parsers + the 21k `compare_l6_oracle` matcher **verbatim**.

---

## §0 — The no-contamination sandwich (acceptance) + reuse/new/retires

### §0.1 The gate + byte-identity sandwich

The change is **tools-only** (`batch_analyze.cpp`; the composing library is untouched — the standard
`.ours.json` writer is not modified, and the two new fields live only in **default-off dump paths** that
return before it). Proofs [probe]:

| check | result |
|---|---|
| Standard `.ours.json` (new binary, flag OFF) vs frozen corpus | **BYTE-IDENTICAL** (`diff` empty, `bwv10.7`) |
| `git status tools/corpus/` | **clean — corpus byte-untouched** |
| Batch gate BEFORE (`characterise_bir_false` ×3) | **Baroque 53 / Jazz 24 / Default 53** |
| Batch gate AFTER (post-measurement ×3) | **Baroque 53 / Jazz 24 / Default 53** (corpus untouched ⇒ case-identity sets preserved) |
| `pipeline_snapshot_tests` | **11/11 PASS, NO golden refresh** |
| `composing_tests` / `notation_tests` | unaffected (batch_analyze.cpp is not linked into either binary; the composing lib is byte-identical) — re-run green (§7) |

The two additive fields are diagnostic-only and default-off **by construction**: the fullspine path and the
new `--dump-region-keymargin` path both `return` before the standard `writeJson`, so production output cannot
change. The frozen gate corpus was **never regenerated** — all substrates were written to scratch.

### §0.2 Reuse-vs-new + what retires

- **Reuses verbatim (no change):** `a8_rebaseline_measure.build_piece_grid` (the ratified A-8
  union-of-boundaries cell loop; self-validates its variant-(b) 5-bucket decomposition byte-for-byte against
  the pinned `compare_rn.grid_score_regions()` on every piece), `compare_rn._active_index_at` /
  `classify_pair` / `_our_key_tonic` / `_dcml_key_tonic`, `compare_analyses.load_analysis` /
  `_dcml_time_spans`, `dcml_parser.find_wir_file` / `parse_rntxt_file` / `parse_cadence_phrase_markers`,
  `compare_l6_oracle.match_points` / `score_cadence` / `DEV_BEDS` / `_corpus_pieces` / `TOLERANCE_TICKS` (the
  21k TSV oracle machinery), and the frozen per-preset corpus + `characterise_bir_false` gate.
- **New:** the harness `tools/c1_reliability.py` + two **additive default-off** dump fields:
  (1) `--dump-region-keymargin` (emits per BATCH region the L3 **sequence margin** `keySeqMargin` +
  **emission sigmoid** `keySigmoid`), (2) `phraseTextureTicks`/`phraseTextureStrength` in `--dump-fullspine`
  (the L1.5 graded texture profile at every candidate tick).
- **Retires:** nothing. (The legacy path was left out by construction — documented unreliable, retires at
  engage per R8; the HELD-OUT beds were untouched.)

---

## §1 — Task 0: what the dumps export per §3 row (verified at source)

For each contract-§3 inventory row, the published confidence was located **at source** and its export status
verified. **No row is unmeasurable-as-built** — the two that were not exported are covered by additive
default-off fields (the instruction's sanctioned path), not improvised.

| layer × decision | published confidence (at source) | exported as-built? | how measured here |
|---|---|---|---|
| **L3 key — emission sigmoid** | `KeyModeAnalysisResult.normalizedConfidence` (the C1 sigmoid; `keymodesequence.h` §status) | **YES** — frozen corpus region `keyConfidence` (`writeJson`, batch_analyze) | frozen `.ours.json` |
| **L3 key — sequence margin** | `HarmonicRegion.keyConfidence = rep.confidence` (regionanalyzer.cpp §15-3 "the chosen key's sequence-margin confidence") | **NO** — computed in production but **dropped** at the `AnalyzedRegion` conversion (batch_analyze.cpp:692 copies `keyModeResult`, not `keyConfidence`) | **added field** `--dump-region-keymargin` (pure export; STOP-safe — no value computed) |
| **L4 chord — composite** | `SliceConfidence.composite` (`[0,1] = min(marginCertainty, sufficiency, cleanliness)`; already the squashed boundary form) | **YES** — fullspine `l4Composite` (+ `l4Margin`/`l4Sufficiency`/`l4Cleanliness`) | gate fullspine |
| **L5 fn — combinedBoundary** | `FunctionConfidence.combinedBoundary` (D-L5a squashed `combined/(combined+k) ∈ [0,1)`) | **YES** — fullspine `l5CombinedBoundary` | gate fullspine |
| **L5 cadence — vote** | `FunctionalCadence.tonicVote` (evidence-scale vote, F-A) | **YES** — fullspine `cadences[].tonicVote` | dev-bed fullspine |
| **L1.5 boundary — strength** | `PhraseBoundaryProfile.textureStrength` (graded, parallel to `textureTicks`) | **NO** — the dump exported only `pickedTicks` (`phraseBoundaryTicks`), no strength at candidate ticks | **added fields** `phraseTextureTicks`/`phraseTextureStrength` (pure export of the existing profile array) |

The two `NO` rows both had the confidence **present in a live data structure** but not on any dump boundary —
exactly the Task-0 additive-field case. Neither required computing a value (both are pure exports of an
already-computed quantity), so neither tripped the STOP condition. `--dump-region-keymargin`'s per-region
`keySigmoid` was cross-checked to equal the frozen corpus `keyConfidence` byte-for-byte at every region
(same `analyzeScore` ⇒ same regions), confirming the join is faithful.

---

## §2 — The reliability curves (per layer × decision × preset)

10 equal-width bins on [0,1] (declared, fixed — no fitting). Unbounded confidences are mapped to [0,1] by a
**declared monotone squash** `s(x)=x/(x+k)` (ranking is squash-invariant, so the monotonicity finding does not
depend on `k`): L3 margin `k = 1.0` (= `KeyModeSequencePreferences.uncertainThreshold`, the layer's own bar);
cadence vote `k = 3.5` (≈ the single-authentic-cadence unit). [0,1]-native confidences (L3 sigmoid, L4
composite, L5 combinedBoundary, L1.5 max-normalized strength) are binned directly. "emp" = duration-weighted
(harmonic rows) or count-weighted (dev-bed point rows) empirical correctness; ECE = weighted mean
`|emp − mean_conf|`; signed_gap = weighted mean `(emp − mean_conf)` (**>0 underconfident, <0 overconfident**).

### §2.1 L3 key-of-slice — SEQUENCE MARGIN vs EMISSION SIGMOID (correctness = A-8 key respect)

Overall key respect reproduces the ratified A-8 variant-(b) key-agree baseline **to within 0.06–0.27 pp — the
key-parse-fail reweighting** (Baroque 68.18 vs 68.11 %, Jazz 64.52 vs 64.43 %, Default 67.77 vs 67.50 %): the
harness is measuring the same key respect on the same cells, differing only in the denominator's treatment of
the ~0.1–0.4 % parse-fail slice. Mechanism verified at both aggregation paths in **§2.1a** below.

| preset | confidence | overall | ECE | signed_gap | mono. viol. | shape |
|---|---|---|---|---|---|---|
| Baroque | **margin** | 0.6818 | **0.135** | −0.079 (over) | 4 | flat ~0.51 (bins 0–4) → **0.72–0.85** (bins 8–9) |
| Baroque | sigmoid | 0.6818 | **0.382** | +0.361 (under) | 3 | ~flat 0.64–0.71, then 0.80–0.89; 33 % mass at conf≈0.05 |
| Jazz | **margin** | 0.6452 | **0.142** | −0.081 (over) | 4 | ~0.50 → 0.63/0.71/0.83 |
| Jazz | sigmoid | 0.6452 | **0.439** | +0.436 (under) | 4 | ~flat 0.60–0.68; **43 % mass at conf≈0.05** |
| Default | **margin** | 0.6777 | **0.125** | −0.089 (over) | 2 | ~0.5 → 0.73/0.84 |
| Default | sigmoid | 0.6777 | **0.392** | +0.377 (under) | 1 | ~flat 0.61–0.73, then 0.78/0.89 |

**Reading.** The **sequence margin** is discriminative at the top: the highest-margin bins (0.8–1.0, carrying
~55–66 % of scored time) are 72–85 % key-correct, while the lowest bins sit near chance (~0.5). It is mildly
**over**confident (signed −0.08) with a soft mid-range dip (the monotonicity violations are all small, in the
sparse low-mass bins). The **emission sigmoid** is badly miscalibrated: it is nearly flat in correctness while
its value collapses to ≈0.05 for a third-to-nearly-half of the (correct) mass — a systematic **under**confidence
(signed +0.36 to +0.44) that the A-8 relative-minor cases exemplify (e.g. `bwv10.7` region 0: G-minor chosen
correctly, sigmoid 0.010, margin 1.371). ECE is **2.8–3.1× worse for the sigmoid** on every preset.

#### §2.1a — baseline-delta mechanism (Task-1 close-out, 2026-07-04)

§2.1 originally called the reproduction "exactly." That was imprecise — the numbers are near-equal, not equal:
**68.18 vs 68.11 (Baroque) / 64.52 vs 64.43 (Jazz) / 67.77 vs 67.50 (Default)**, same-direction deltas of
**0.06 / 0.08 / 0.27 pp**. The mechanism, read at both aggregation paths (`c1_reliability.py measure_l3` vs
`a8_rebaseline_measure.py measure_preset`) and confirmed by a read-only scratch recomputation over the identical
`build_piece_grid` cells [probe]:

**Denominator scope — the two paths condition the key respect differently, on the SAME numerator (`agree`
duration), SAME cells, and SAME duration weighting:**
- **A-8 baseline** reports `agree / scored_dur` — every scored cell is in the denominator, and the small
  **key-parse-fail** slice (cells where OUR key string does not parse) is reported *separately* (§2.2:
  0.09 / 0.13 / 0.40 %) while still counted in `scored_dur`.
- **C1 (§2.1)** reports `agree / (agree + disagree)` — `measure_l3` **excludes** the key-parse-fail cells from
  the denominator (tracked as `keyfail_w`, reported apart), conditioning the reliability on the cells where OUR
  key parses — the cells a confidence-vs-correctness curve can actually score.

The per-preset delta **equals exactly the key-parse-fail reweighting** of the shared numerator. Recomputed on
the identical cells [probe]: `agree/scored` reproduces **68.11 / 64.43 / 67.50** and `agree/(agree+disagree)`
reproduces **68.18 / 64.52 / 67.77**, the gap being `keyfail% / (1 − keyfail%)` (Default: 67.50 ×
0.399 %/(1 − 0.399 %) = 0.27 pp). The keymargin-join drops **zero** cells on every preset
(`join_drop_ticks = 0` — `--dump-region-keymargin` reproduces the frozen-corpus regions exactly, so the L3
confidence attaches to every cell), and `dcml_keyfail = 0` (all WiR keys parse).

**This is a benign definition/coverage nuance, not a defect** — no mis-join, no wrong parser, no wrong
weighting; only the denominator's treatment of the ~0.1–0.4 % parse-fail slice differs. The §2 reliability
curves are unaffected: they bin the scored (parseable) cells, and each curve's overall-correct figure IS the
C1 `agree/(agree+disagree)` conditioning. **§2.1's "exactly" is corrected to "to within 0.06–0.27 pp, the
key-parse-fail reweighting."**

### §2.2 L4 chord-of-slice — COMPOSITE (correctness = A-8 root respect)

| preset | overall | ECE | signed_gap | mono. viol. | shape |
|---|---|---|---|---|---|
| Baroque | 0.4674 | **0.110** | +0.011 (~neutral) | 4 | flat ~0.29 (bins 0–4) → **0.39/0.58/0.73/0.84** (bins 5–9) |
| Jazz | 0.4680 | **0.108** | +0.014 | 4 | same monotone climb above ~0.5 |
| Default | 0.4675 | **0.110** | +0.011 | 4 | same |

**Reading.** L4 composite is the **best-calibrated harmonic confidence**: above ~0.5 it climbs monotonically
(0.39 → 0.84) and closely tracks the diagonal (ECE 0.11, signed ≈0). Below ~0.5 the root respect is flat at
~0.29 (composite does not separate the low band). The RN-respect reading (tracked beside, same substrate) is
uniformly lower (the fullspine chain's base RN is triad-level by construction, E0″ §4).

### §2.3 L5 function-of-unit — combinedBoundary / D-L5a (correctness = A-8 RN respect)

| preset | overall | ECE | signed_gap | mono. viol. | note |
|---|---|---|---|---|---|
| Baroque | 0.2937 | **0.250** | −0.132 (over) | 4 | 27.8 % of duration has combinedBoundary = 0 (RN respect 0.19 there) |
| Jazz | 0.2913 | 0.248 | −0.131 (over) | 4 | 28.2 % at 0 |
| Default | 0.2934 | 0.250 | −0.132 (over) | 4 | 27.9 % at 0 |

**Reading.** L5 `combinedBoundary` is **poorly calibrated and over-confident**: median confidence ≈0.5 while
RN respect is only ~0.29, and the curve is **non-monotone** — the 0.6–0.8 band (mean conf ~0.7) has *lower* RN
accuracy (0.20–0.22) than the 0.5–0.6 band (0.37). (The base RN is triad-level, so this measures RN-respect on
the dormant chain, not the production RN.) The 0-confidence mass (~28 %) is the resolved-abstain / no-function
units and is correctly low-accuracy.

### §2.4 L5 cadence detection — tonicVote (dev beds; correctness = matched DCML cadence ±480)

`tonicVote` n=294, range **[3.0, 7.0]**, median 3.5 → after squash lands entirely in three bins. Overall
detection precision 0.36.

| bin (mean conf) | tonicVote | count | emp precision |
|---|---|---|---|
| [0.4,0.5) (0.479) | 3.0 | 109 | **0.440** |
| [0.5,0.6) (0.507) | 3.5 | 173 | 0.318 |
| [0.6,0.7) (0.639) | 7.0 | 12 | 0.250 |

**Reading (RECORDED, not fixed).** `tonicVote` is a **poor confidence signal for cadence detection**: it has
almost no spread (three distinct values across 294 detections) **and it is anti-monotone** — higher vote →
*lower* precision (0.44 → 0.32 → 0.25). Over-confident (signed −0.14). The vote-weight tracks harmonic-arrival
strength, not phrase-cadence-ness. (Recall the cadence detector's recall is very low overall — 1.6 % aggregate,
`compare_l6_oracle`; this row measures the *precision* calibration of the detections it does make.)

### §2.5 L1.5 boundary-at-tick — texture strength (dev beds; correct = within ±480 of DCML phraseend)

Strength max-normalized **per profile** (contract §3 — "relative salience within the profile"). Aggregated over
521 movements, 478 863 candidate ticks.

| bin | count | mass | emp (near a boundary) | mean conf |
|---|---|---|---|---|
| [0.0,0.1) | 464 011 | **0.977** | 0.137 | 0.005 |
| [0.1,0.6) | 3 357 | 0.007 | 0.33 → 0.48 (rising) | — |
| [0.6,0.9) | 700 | 0.001 | 0.40 → 0.25 (falling) | — |
| [0.9,1.0) | 6 785 | 0.014 | 0.399 | 0.987 |

Overall 0.142, ECE 0.139, signed +0.121 (under), 4 violations.

**Reading (RECORDED, not fixed).** The **max-normalization concentrates 97.7 % of candidate ticks in the
lowest bin** — the deterministic marker spikes (fermata/barline/caesura, height ≥ max surface strength) set the
per-profile max, compressing all surface-cue strengths toward 0. The strength *is* weakly monotone across the
sparse populated bins (0.14 → ~0.48) — higher relative salience does track boundary-likelihood — but the
signal has almost no usable spread, and even the top (spike) bin is only ~0.40 precise (many marker spikes are
not phrase-final). **Contract caveat honored:** this confidence is *relative within one score's profile*
(comparable within a profile only); the aggregate curve pools per-score-relative values — a declared limitation
of the L1.5 salience-margin variant, not a defect surfaced here.

---

## §3 — The D-L3a comparison (the close-out evidence)

The L3 row measured **both** boundary numbers on the identical decisions/substrate so their curves decide which
is better calibrated (the D-L3a evidence rider). Result, unambiguous on **all three presets**:

| | Baroque | Jazz | Default | verdict |
|---|---|---|---|---|
| ECE — **sequence margin** | **0.135** | **0.142** | **0.125** | — |
| ECE — emission sigmoid | 0.382 | 0.439 | 0.392 | margin **2.8–3.1× better** |
| signed gap — margin | −0.079 | −0.081 | −0.089 | mild over-confidence |
| signed gap — sigmoid | +0.361 | +0.436 | +0.377 | **gross under-confidence** |

**The sequence margin is decisively the better-calibrated of the two boundary numbers** — lower ECE on every
preset and a small symmetric bias, against the sigmoid's large systematic underconfidence. This is measured
**evidence for** the D-L3a close-out (declare the sequence margin THE boundary confidence, demote the emission
sigmoid to internal/diagnostic). **The close-out itself is a separate, ratification-gated increment** — this
report records the evidence only.

---

## §4 — D-FS / D-INV range re-confirmation (this run)

The F-A/F-B contradiction-quantity ranges (the E0′/E0″ #9 readout), re-measured from this run's gate fullspine
dumps — the declaration material C2 needs [probe]:

| quantity (frame) | this run (Baroque / Jazz / Default) | E0″ | status |
|---|---|---|---|
| `l5CombinedBoundary` (D-L5a) | **[0, 0.9659]** (n=26 857) all presets | [0, 0.9619] | ⊂ [0,1) — CLOSED, reproduced |
| F-B override contradiction `bestPlaus−committedPlaus` | **[2.0, 3.0]**, med 2.0, n=1057/1015/1057 | 2–3, n≈1049 | reproduced |
| F-A `cadentialWeight` (confirmed modulations) | **[3.25, 9.35]**, med 5.85, n=69 | 3.35–9.35, n≈60 | reproduced |

Both frame-contradiction scales remain **unbounded/unsquashed at the boundary while their incumbents are [0,1]**
(the live commensurability gap D-FS names) — declared here, unchanged; the squash-map shape + θ are the
Stage-5 fitter's (C2). No behavior change.

---

## §5 — Findings, RECORDED for the Stage-5 fitter (never acted on)

Per Task 4, every observation below is recorded, not fixed. Those touching inference quality are **declared to
Cowork** (they are calibration facts, not architecture changes):

1. **D-L3a:** the L3 emission sigmoid is grossly under-confident (ECE 0.38–0.44); the sequence margin is 2.8–3.1×
   better calibrated. → the fitter's Class-P map for L3 should ride the **margin**; the sigmoid's job is the
   downstream 0.8 gate, not calibrated confidence (§3).
2. **L4 composite is the best-calibrated harmonic confidence** (ECE 0.11, monotone above ~0.5, ~neutral bias) —
   a strong Class-P candidate; its low band (< ~0.5) is undiscriminating (flat ~0.29 root respect).
3. **L5 `combinedBoundary` is over-confident and non-monotone** (ECE 0.25; the 0.6–0.8 band is *less* accurate
   than the 0.5–0.6 band). The fitter must not treat it as calibrated; the mid-range inversion is an
   inference-quality signal (declared to Cowork). NB the RN respect here is on the triad-level dormant chain.
4. **Cadence `tonicVote` is a poor detection-confidence signal** — three distinct values, **anti-monotone**
   (higher vote → lower precision). A vote weight fitted as a Class-M→P confidence would be miscalibrated;
   the detection-precision problem is upstream of calibration (declared to Cowork).
5. **L1.5 texture strength has near-zero usable spread** — per-profile max-normalization (spike-dominated)
   puts 97.7 % of candidate ticks in the lowest bin; the signal is weakly monotone but the top (picked/spike)
   bin is only ~0.40 precise. A spike-vs-surface split is a fitter consideration (recorded).

None of the above changed any constant, threshold, squash, or θ; the batch gate stands at 53/24/53.

---

## §6 — Decision surface (what this measurement supplies)

- **Per-layer reliability curves + calibration diagnostics** (§2) — the C1 deliverable; the Stage-5 fitter's
  input for the Class-M→Class-P maps.
- **The D-L3a close-out evidence** (§3): the sequence margin is the better-calibrated L3 boundary number.
- **The D-FS declaration material** (§4): the F-A/F-B contradiction ranges, re-confirmed.
- **No fitted map, no θ, no behavior change** is proposed or made (Task 4).

The batch-region gate (53/24/53 case-identity + two-tier policy) **remains THE hard stop** until the Stage-5
fitter (R10); this run left it byte-identical (§0).

---

## §7 — Acceptance record + commits

- **Sandwich:** gate 53/24/53 BEFORE and AFTER (corpus byte-untouched, `git status` clean); standard
  `.ours.json` byte-identical (new binary, flag OFF); snapshots **11/11 no refresh**; composing/notation tests
  green (batch_analyze.cpp is not linked into them; composing lib byte-identical).
- **Substrates (scratch, read-only):** gate fullspine 352×3, region-keymargin 352×3, dev-bed fullspine 718
  (regenerated with the new binary; boundary P/R 34.8/22.4 % = the L6 baseline 0.348/0.224 — the picked set is
  unchanged, confirming the additive fields did not perturb detection).
- **Reuse-vs-new + retires:** §0.2 (reuses the A-8 cell loop + the 21k oracle + gate machinery verbatim; new =
  the harness + two additive default-off dump fields; retires nothing).
- **Commits (local, unpushed, fork-only):** **`088ba617b0`** `feat(tools): C1 reliability harness + additive
  default-off L3-margin / L1.5-strength dump fields` (batch_analyze.cpp +107 insertions, purely additive;
  c1_reliability.py new); the docs commit `docs(cowork): C1 reliability report + the A-8 dual-track / 353→352
  CLAUDE.md riders` carries this report (force-added, `/cc_*.md` is gitignored) + the two CLAUDE.md riders.

*Report line count: 305 lines (incl. the §2.1a Task-1 addendum, 2026-07-04).*
