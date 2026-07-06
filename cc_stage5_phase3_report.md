# CC Stage-5 Phase 3 — CALIBRATION: fitted Class-P maps + C2 θ candidates + D-FS closure + R-11 disposition

> **MEASUREMENT + COMMITTED ARTIFACTS ONLY. No behavior change anywhere** — no boundary wiring, no θ
> adoption, no committed value change, no corpus write, no push. The maps + θ candidates are fitted and
> validated; their WIRING into live boundaries is a separate, later engage-adjacent increment. Per design
> §4.5 (Phase 3) + O-13, contract §6 C1/C2 + §7 D-FS.
>
> **Provenance.** HEAD `02ec8b0d60` (the 2.3 SHA-completion). Frozen gate corpus manifest `git_hash
> c50002fee1`, complete 352/352 each preset, fingerprint-validated. Batch stop **52/24/52** BEFORE and
> AFTER (set-diff empty ×3). The C1 substrate was **regenerated on the current (2.2e-adopted) corpus**;
> the C1 report's numbers predate the adoption, so every curve is re-measured (old→new below). All maps +
> θ + conformal numbers are **[probe]** (ran the instrument, read output).

---

## §0 — State check (Task 0) + the no-contamination sandwich

### §0.1 Task 0 state

- **HEAD** `02ec8b0d60d626d77c7834baed93e40f7c68a97d`; **branch** `master`.
- **Dirty (pre-existing):** `COWORK_HANDOFF.md`, `STATUS.md` (modified); untracked `idiom_discovery/*.txt`,
  `scratch_artifacts/` (known/expected).
- **Batch gate ×3 (BEFORE):** Baroque **52** / Jazz **24** / Default **52**; case-identity **set-diff
  EMPTY** on all three vs the CLAUDE.md authoritative sets (`characterise_bir_false.py`, manifest
  fingerprint-validated, `git c50002fee1`). [probe]

### §0.2 Sandwich (acceptance) — filled at §7

The dispatch computes on dumps + Python + **one sanctioned additive default-off dump field**
(`phraseNumVoices`, Task B). Standard `.ours.json` proven **byte-identical** on the new binary (§7);
suites green, no golden refresh; frozen corpus fingerprint-validated untouched.

### §0.3 Reuse-vs-new + retires

- **Reuses verbatim:** the C1 harness `tools/c1_reliability.py` (+ its A-8 cell loop, the 21k dev-bed
  oracle machinery, `compare_rn`/`compare_analyses`/`dcml_parser` primitives), `cc_e0_fullspine_measure`'s
  per-fire classification logic (correction/harm), `compare_l6_oracle`'s dev-bed driver, the frozen
  per-preset corpus + `characterise_bir_false` gate, `run_bach_preset` invocation form.
- **New (tools-only, additive):** `tools/c1_gen_substrate.py` (substrate regen driver), `tools/calibration_fit.py`
  (Task A maps), `tools/theta_fit.py` (Task C θ), `tools/l15_split.py` (Task B), `tools/conformal_check.py`
  (Task D); one additive default-off dump field `phraseNumVoices` in `tools/batch_analyze.cpp`; the committed
  map artifacts under `tools/calibration_maps/`.
- **Retires:** nothing. (The L5/cadence/L1.5 deferrals are re-verified, not fitted; the legacy path is
  untouched.)

---

## §1 — Task A: re-measured C1 curves (old→new) + the fitted Class-P maps

### §1.1 The re-measured curves — old (C1 report, corpus `0dd64660f4`) → new (corpus `c50002fee1`)

Harmonic rows on the ratified A-8 unit (union-of-boundaries, duration-weighted, variant (b) DCML-only),
326/352 WiR coverage each preset. **The 2.2e kWStepIn adoption barely moved the curves — every ECE delta
is ≤ 0.001 pp.** [probe]

| row | preset | ECE old→new | overall old→new | mono.viol old→new |
|---|---|---|---|---|
| **L3 margin** | Baroque | 0.135 → **0.1355** | 0.6818 → 0.6819 | 4 → 3 |
| L3 margin | Jazz | 0.142 → **0.1419** | 0.6452 → 0.6452 | 4 → 4 |
| L3 margin | Default | 0.125 → **0.1251** | 0.6777 → 0.6777 | 2 → 2 |
| L3 sigmoid | Baroque | 0.382 → **0.3820** | 0.6818 → 0.6819 | 3 → 3 |
| L3 sigmoid | Jazz | 0.439 → **0.4388** | 0.6452 → 0.6452 | 4 → 4 |
| L3 sigmoid | Default | 0.392 → **0.3919** | 0.6777 → 0.6777 | 1 → 1 |
| **L4 composite** | Baroque | 0.110 → **0.1105** | 0.4674 → 0.4674 | 4 → 4 |
| L4 composite | Jazz | 0.108 → **0.1075** | 0.4680 → 0.4680 | 4 → 4 |
| L4 composite | Default | 0.110 → **0.1105** | 0.4675 → 0.4675 | 4 → 4 |
| **L5 combinedBoundary** | Baroque | 0.250 → **0.2496** | 0.2937 → 0.2937 | 4 → 4 |
| L5 combinedBoundary | Jazz | 0.248 → **0.2478** | 0.2913 → 0.2913 | 4 → 4 |
| L5 combinedBoundary | Default | 0.250 → **0.2497** | 0.2934 → 0.2934 | 4 → 4 |

The D-L3a picture holds unchanged: the **sequence margin** is 2.8–3.1× better calibrated than the emission
sigmoid on every preset (margin ECE 0.125–0.142 vs sigmoid 0.382–0.439). The L4 composite remains the
best-calibrated harmonic confidence (ECE 0.11, ~neutral bias). L5 combinedBoundary remains over-confident
AND non-monotone (see §1.3).

### §1.2 The fitted maps (L3 margin + L4 composite; Baroque + Default carriers) — Jazz UNMAPPED (A-7)

Fitted on the **fitting split** (261 scores), validated on the **held-out split** (65). Shape rule (design
§4.5.1): isotonic default; Platt only if near-logistic AND not worse held-out. **All four rows chose
isotonic** (isotonic-vs-Platt max-abs-diff 0.20–0.26 ≫ 0.05 → not near-logistic; Platt held-out ECE was
also worse, e.g. L3 Baroque 0.047 vs isotonic 0.027). Committed to `tools/calibration_maps/`. [probe]

| map (carrier) | shape | pre-map ECE (fit/hel) | **post-map ECE (fit/hel)** | overall (fit/hel) | n (fit/hel) |
|---|---|---|---|---|---|
| **L3 margin (baroque)** | isotonic | 0.133 / 0.154 | 0.000 / **0.027** | 0.683 / 0.679 | 14845 / 3971 |
| **L3 margin (default)** | isotonic | 0.125 / 0.139 | 0.000 / **0.041** | 0.679 / 0.673 | 14804 / 3967 |
| **L4 composite (baroque)** | isotonic | 0.113 / 0.102 | 0.000 / **0.017** | 0.466 / 0.473 | 21094 / 5752 |
| **L4 composite (default)** | isotonic | 0.113 / 0.102 | 0.000 / **0.016** | 0.466 / 0.472 | 21094 / 5752 |

The **held-out post-map ECE is the honesty number**: 0.017–0.041, a **3–6× reduction** vs the pre-map
held-out ECE (0.102–0.154). The maps generalize.

**Flat-band assertion (design §4.5.1 — "the map may not invent resolution there").** ASSERTED and HELD for
L4: the isotonic map's value over the low band [0,0.5) is **constant 0.289** (Baroque & Default) — the
fitter pools the flat low band to its mean, inventing no rise where the data is flat. L4 Baroque knots:
below conf 0.501 → 0.289; then 0.52 / 0.577 / 0.681 / 0.736 / 0.825 / 0.857 (monotone climb). Every map is
**monotone by construction** (isotonic). No map failed its own assertion → no STOP.

### §1.3 The deferrals — RE-VERIFIED on the current corpus (no map fitted)

- **L5 combinedBoundary — deferral STANDS (shape did NOT change post-adoption).** Still non-monotone on all
  three presets (mono-viol 4): the 0.6–0.8 band scores **below** the 0.5–0.6 band (Baroque bins: 0.366 →
  0.215; ECE 0.2496, over-confident −0.13). The 2.2e adoption did not change the inversion → the STOP-
  condition "L5 non-monotonicity having CHANGED shape post-adoption" did **not** trigger; the deferral is
  re-confirmed, not overridden. The mid-range inversion is an **upstream inference-quality signal** (RN
  respect is on the triad-level dormant chain), declared to Cowork — not "fixed" by a non-monotone map.
- **Cadence `tonicVote` — deferral STANDS** (re-measured, dev-bed, fresh dumps): overall precision
  0.36 → **0.3605**, still **anti-monotone** (mono-viol 2: bin 4→5 0.44→0.318, 5→6 0.318→0.25), ~3 distinct
  values — not calibratable (an upstream detection-quality item, §11 scope).
- **L1.5 texture strength (pooled) — unchanged** (re-measured, fresh dumps): overall 0.142 → **0.1420**,
  ECE 0.139 → **0.1394**, signed +0.121, mono-viol 4. **Task B (§3) decides** whether the spike-vs-surface
  split changes the map disposition.

Dev-bed rows old→new are essentially unchanged (L1.5 texture is notation-derived, cadence barely moved) —
the 2.2e adoption did not perturb them.

### §1.4 Contract §3 row-status changes for Cowork to apply (NOT edited here — Cowork-owned doc)

`cowork_confidence_contract.md` §3 is Cowork-owned; the exact row-status changes to apply:

1. **L3 key/mode row** (§3, the sequence-margin line): append — *"Stage-5 Class-P map FITTED (isotonic,
   Baroque+Default carriers; held-out ECE 0.027/0.041), WIRING PENDING (engage-adjacent). Jazz carrier
   UNMAPPED (A-7 empirically-unvalidated). Artifacts: `tools/calibration_maps/stage5_classP_l3_key_margin_{baroque,default}.json`."*
2. **L4 chord row** (§3): append — *"Stage-5 Class-P map FITTED (isotonic, Baroque+Default; held-out ECE
   0.017/0.016; low band pooled flat to 0.289 — no invented resolution), WIRING PENDING. Jazz UNMAPPED
   (A-7). Artifacts: `stage5_classP_l4_chord_composite_{baroque,default}.json`."*
3. **L5 function row** (§3, D-L5a line): append — *"Stage-5 calibration: combinedBoundary NOT
   Class-P-upgradable as-is — non-monotone mid-range re-confirmed on corpus `c50002fee1` (0.6–0.8 band
   below 0.5–0.6, all presets); map DEFERRED, inversion is an upstream inference-quality finding."*
4. **L5 cadence vote row** (§3): append — *"Stage-5 calibration: tonicVote NOT calibratable (anti-monotone,
   ~3 distinct values); recorded as an upstream detection-quality item (out of arc scope)."*
5. **L1.5 phrase-boundary row** (§3): append — *"Stage-5 Task-B spike-vs-surface split MEASURED (§3): the
   SURFACE population alone (98.4 % of ticks), normalized within itself, has usable monotone spread
   (0.13→0.46 across deciles, mono-viol 2) — a per-population map is fittable in principle at a later
   increment; the SPIKE population (1.6 %) is a flat ~0.40 cluster (no usable spread). No map fitted now
   (weak absolute signal, tops at 0.46). The C1 'insufficient spread' reading is refined: the spread exists
   in the surface cues once un-compressed from the spike-dominated per-profile max."*
6. **§7 D-FS row:** append — *"Contradiction scales DECLARED (F-A cadentialWeight squash x/(x+3.5); F-B
   bestPlaus−committedPlaus squash x/(x+2.0); constants precision-phase, R5); θ candidates fitted (§2,
   RECORDED, unwired). Re-measured net-harm CONFIRMS the override problem (F-B: 1043 fires / 53 corrections
   / 809 harms)."*

### §1.5 Task B — the L1.5 spike-vs-surface split

See **§3** (the dedicated Task-B verdict).

---

## §2 — Task C: the frame scales declared + θ candidates (C2 / D-FS closure)

### §2.1 The two contradiction-scale squashes DECLARED (D-FS §4.5.2)

Both frame contradiction quantities are integer-coarse and unbounded at the boundary while their
incumbents are [0,1] (the live commensurability gap D-FS names). Per R5 (monotone, [0,1], constants
precision-phase), the declared squash is **s(x) = x/(x+k)**:

| frame | contradiction quantity | observed range (re-confirmed, current corpus) | declared squash |
|---|---|---|---|
| **F-A** | `cadentialWeight` (confirmed modulations) | **[3.35, 9.35]** med 5.85 n=69 (Baroque/Default); [3.25, 9.35] (Jazz) | s(x)=x/(x+**3.5**) — k ≈ single-authentic-cadence unit |
| **F-B** | `bestPlaus − committedPlaus` | **[2.0, 3.0]** med 2.0 n=1057/1015/1057 | s(x)=x/(x+**2.0**) — k = the minimal contradiction unit |

Also re-confirmed: `l5CombinedBoundary` ∈ **[0, 0.9659]** ⊂ [0,1) (D-L5a closed, reproduced). All ranges
match the C1 §4 declaration (F-A min 3.25→3.35 the only shift, +0.10, within corpus noise). [probe]

### §2.2 θ candidates FITTED (RECORDED, NOTHING WIRED)

The override θ (`forwardoverride.h` `baseBar=1.0`, `confidenceScale=1.0`; rule `S_contra > baseBar +
confidenceScale·C_incumbent`) is **NOT exposed to `--param-override`**, so candidates are fitted POST-HOC
from the dumped fired sites — no re-run, no recompile. **One-sided limitation (RECORDED):** the dump emits
S_contra only at sites that fired at the current bar, so candidates are explorable only in the stricter-bar
direction (raising the bar drops current fires — measurable; a looser bar creates unseen fires). Since the
current override is net-harmful, the useful direction IS the measurable one. Frames are dormant-chain
sites; adoption rides the engage arc.

**Frame F-B (fine-grain chord override).** Re-measured net-harm on the dormant decode chain (E0
methodology, DCML root GT), preset-invariant here (the override is on the decode chain): **1043 fires — 53
corrections, 809 harms, 181 neutral.** At the current bar (1.0, 1.0): fitting (789 fires / 44 corr / 615
harm), held-out (254 / 9 / 194) → corrections−harm = **−571 (fit) / −185 (hel)**. The corrections−harm-
maximizing candidate over the measurable region is **any bar high enough to suppress firing** (e.g.
baseBar 1.0, confidenceScale 4.0 → all fired C∈[0.50,1.0] give bar ≥ 3 ≥ S): fires 0, corr−harm **0**.
Acceptance: 0 ≫ −571 → **strictly better than the current constants**. **This is not a θ retune — the best
measurable θ effectively DISABLES the override.** → declared to Cowork as an **inference-quality finding**
(the F-B fine-grain override, as wired on the decode chain, moves an L4-correct root to wrong ~78 % of the
times it fires); a redesign question for the engage arc, not fittable away.

**Frame F-A (cadence-confirmed modulation).** 69 confirmed modulations, correct/wrong (our modulation tonic
vs DCML local-key tonic) = **39 / 30**. Current effective (τ≥1.0, all fire): fitting (58 / 32 / 26),
held-out (11 / 7 / 4) → corr−harm **+6 (fit) / +3 (hel)**. **Best reduced candidate: τ ≈ 5.0 on
cadentialWeight** → fitting (35 / 25 / 10), held-out (7 / 6 / 1) → corr−harm **+15 (fit) / +5 (hel)** —
raising the bar drops mostly-spurious weak modulations. Acceptance: +15 > +6 → **better than current**.
**Reduced form only:** the full bar's confidenceScale·C term needs the per-modulation L3 incumbent key
confidence, which is **not in the `modulations[]` dump** — the full F-A θ fit is deferred to the engage arc
(an additive per-modulation incumbent-confidence join). RECORDED, unwired.

**No pinned tool was modified for the θ fit** (Task C item 3): the fit reads existing dump fields
(`l5OverrodeCommit`, `l5OverrideContradiction`, `l4Composite`, `modulations[].cadentialWeight/tonicPc`) via
new orchestration only; the full two-sided F-B exploration and the F-A confidenceScale term would each need
an additive engage-arc field, deferred — no STOP tripped (the useful candidates are already measurable).

Ledger: `tools/fit_ledgers/stage5_theta_candidates.jsonl` (below) + `C:/tmp/c1/theta.json`.

---

## §3 — Task B: the L1.5 spike-vs-surface split (verdict material)

The split is **code-truth**: `phraseNumVoices` (the additive dump field) gives the per-profile threshold;
a tick is a marker spike iff raw strength > numVoices·sumWeights (sumWeights=1.0 default). The
**spike-floor invariant is confirmed exactly**: median AND min of (min-spike-strength / numVoices) =
**1.500** = `spikeCeilingFactor` over all 717 profiles — every profile's lowest spike sits exactly at
1.5·numVoices, so the split cleanly separates the two populations. [probe]

Split: **7415 spike ticks (1.6 %)** vs **467 438 surface ticks (98.4 %)**, over 717 movements. Each
population's strength is max-normalized WITHIN the population per profile (the key re-measurement: the C1
pooled curve normalized by the spike-dominated max, compressing all surface cues toward 0).

| population | n | overall precision | spread (max−min emp) | mono-viol | non-empty bins | shape |
|---|---|---|---|---|---|---|
| **SPIKE** | 7415 | 0.384 | 0.158 | 1 | 3 | flat single cluster — 6759/7415 in the top bin at 0.398; bins 0.7–0.9 ~0.24 |
| **SURFACE** | 467 438 | 0.138 | 0.329 | 2 | 10 | **weakly monotone** 0.129 → 0.228 → 0.269 → 0.266 → 0.310 → 0.353 → 0.386 → 0.363 → 0.418 → **0.458** |

**Verdict material (report first; no map fitted).**
- **SPIKE population: NO usable spread.** Deterministic markers (fermata/barline/caesura) cluster tightly
  (all ≥ 1.5·numVoices); within-spike normalization leaves 3 bins with ~0.24–0.40 precision and no
  monotone gradient worth calibrating. Many marker spikes are simply not phrase-final (~0.40 precise).
- **SURFACE population: HAS usable monotone spread** — 0.13 → 0.46 across deciles, mono-viol only 2 (both
  tiny). This is the finding the split enables: **once un-compressed from the spike-dominated per-profile
  max, the surface cues carry a real, near-monotone boundary-likelihood gradient** that the C1 pooled
  curve hid (97.7 % in one bin). → **a per-population map on the surface cues is fittable IN PRINCIPLE at a
  later increment.**
- **But the absolute signal is weak** (surface precision tops at 0.458; overall 0.138), so a fitted
  surface map would be low-ceiling. **The C1 "insufficient spread → deferral" reading is REFINED, not
  overturned:** the spread is sufficient in the surface population; the limitation is the weak absolute
  detection signal, which is upstream of calibration. No map is fitted now (per the dispatch); the
  surface-population map is a recorded engage-arc candidate.

Ledger: `C:/tmp/c1/l15_split.json`.

---

## §4 — Task D: R-11 split-conformal abstention disposition (verdict material)

On the SAME L3/L4 substrate as Task A, comparing two ways of choosing the abstention bar (contract U5) at
declared target-correctness (coverage) levels {0.70, 0.75, 0.80}: **split-conformal** (fitting = calibration,
held-out = test; smallest confidence threshold whose calibration retained-correctness Hoeffding lower bound
δ=0.1 ≥ target) vs **map-implied** (abstain when the fitted Class-P map < target). Both are confidence
thresholds; the comparison is the method-of-choosing. [probe]

| carrier · row | target | conformal (τ / test-retained / test-corr / meets) | map-implied (τ / retained / corr / meets) |
|---|---|---|---|
| Baroque L3 | 0.70 | 0.571 / **0.845** / 0.700 / ✓ | 0.831 / 0.584 / 0.753 / ✓ |
| Baroque L3 | 0.75 | 0.851 / 0.514 / 0.754 / ✓ | 0.893 / 0.198 / 0.779 / ✓ |
| Baroque L3 | 0.80 | 0.890 / 0.231 / 0.773 / ✗ | 0.896 / 0.160 / 0.792 / ✗ |
| Baroque L4 | 0.70 | 0.525 / **0.417** / 0.711 / ✓ | 0.721 / 0.311 / 0.748 / ✓ |
| Baroque L4 | 0.75 | 0.751 / 0.087 / 0.824 / ✓ | 0.982 / 0.055 / 0.897 / ✓ |
| Baroque L4 | 0.80 | 0.893 / 0.065 / 0.878 / ✓ | 0.982 / 0.055 / 0.897 / ✓ |
| Default L3 | 0.70 | 0.526 / 0.874 / 0.699 / ✗ | 0.838 / 0.583 / 0.767 / ✓ |
| Default L3 | 0.75 | 0.813 / 0.648 / 0.757 / ✓ | 0.893 / 0.198 / 0.779 / ✓ |
| Default L3 | 0.80 | 0.888 / 0.257 / 0.784 / ✗ | 0.896 / 0.160 / 0.774 / ✗ |
| Default L4 | 0.70 | 0.525 / 0.417 / 0.711 / ✓ | 0.721 / 0.311 / 0.748 / ✓ |
| Default L4 | 0.75 | 0.751 / 0.087 / 0.824 / ✓ | 0.982 / 0.055 / 0.897 / ✓ |
| Default L4 | 0.80 | 0.893 / 0.065 / 0.878 / ✓ | 0.982 / 0.055 / 0.897 / ✓ |

**Verdict material (recorded for Cowork disposition; nothing adopted).** Conformal **retains substantially
more at the same target** (e.g. Baroque L3@0.70: 0.845 vs 0.584; L4@0.70: 0.417 vs 0.311) with a finite-
sample validity statement — better **efficiency**. But its marginal guarantee **can slip on test** where the
correctness ceiling (~0.78–0.79 for L3) approaches the target (Default L3@0.70 lands 0.699; both methods
miss 0.80 on L3). The map-implied bar is more conservative (lower efficiency) and its step-function nature
makes thresholds coarse, but it reads the per-confidence calibrated probability directly. **Conclusion: conformal
is a useful COMPLEMENT for the abstention bars (better efficiency at achievable targets, distribution-free)
— NOT a replacement for the calibrated map (which supplies the calibrated probability the bar reads).** This
supports the design's "a complement, not a replacement." Ledger: `C:/tmp/c1/conformal.json`.

---

## §5 — Findings declared to Cowork (inference-quality; recorded, not acted on)

1. **F-B override net-harm CONFIRMED + quantified** (§2.2): 1043 fires / 53 corrections / **809 harms** on
   the dormant decode chain — the best measurable θ disables it. The contradiction quantity (bestPlaus−
   committedPlaus ∈ {2,3}) is too coarse and the incumbent (l4Composite ∈ [0.5,1.0]) too high for the
   override to fire selectively. A **redesign** item (not a θ retune), for the engage arc.
2. **L5 combinedBoundary non-monotonicity persists** post-adoption (§1.3) — an upstream inference-quality
   signal, map deferred.
3. **Cadence tonicVote anti-monotone** persists (§1.3 / §3) — upstream detection-quality item.

None changed any constant, threshold, squash, or θ; the batch gate stands at 52/24/52.

---

## §6 — Acceptance

| acceptance item | status |
|---|---|
| Re-measured curves old→new (all rows, all presets) | ✓ §1.1 (all ECE Δ ≤ 0.001) |
| L3 + L4 maps fitted, validated on held-out, committed with provenance | ✓ §1.2 (isotonic; held-out ECE 0.017–0.041; flat-band asserted+held) |
| Deferrals re-verified with reasons | ✓ §1.3 (L5 non-monotone shape UNCHANGED post-adoption; cadence anti-monotone; L1.5→Task B) |
| L1.5 spike-vs-surface split measured | ✓ §3 (surface has usable monotone spread; spike flat; no map fitted) |
| Scales declared + θ candidates surfaced (dormant, recorded, unwired) | ✓ §2 (F-A x/(x+3.5), F-B x/(x+2.0); F-B net-harm confirmed → disable-candidate; F-A τ≈5.0 candidate) |
| Conformal verdict material | ✓ §4 (complement not replacement) |
| Contract-§3 changes listed for Cowork | ✓ §1.4 |
| Sandwich + suites | ✓ §7 |
| Report + fold with SHAs | ✓ (fold: STATUS.md · COWORK_HANDOFF.md · design Phase-3 markers · instruction force-add) |

**No STOP tripped:** no behavior change (standard `.ours.json` byte-identical, suites green); no
non-additive tool modification (the one `phraseNumVoices` field is additive, default-off dump path); no
corpus write; no push. No fitted map was non-monotone or resolution-inventing. The L5 non-monotonicity did
NOT change shape post-adoption (deferral re-confirmed, not re-opened).

---

## §7 — Sandwich record

| check | result |
|---|---|
| Batch gate ×3 **BEFORE** | Baroque **52** / Jazz **24** / Default **52**, set-diff empty vs CLAUDE.md |
| Batch gate ×3 **AFTER** | Baroque **52** / Jazz **24** / Default **52**, **set-diff vs BEFORE = 0** all three |
| Corpus fingerprint validation | `Corpus OK … git c50002fee1` ×3 (frozen corpus byte-untouched — manifest sha256 validated, not a git-status claim per O-12) |
| Standard `.ours.json` byte-identity (new binary, flag OFF) | **BYTE-IDENTICAL** — 15/15 score×preset pairs, 0 mismatches (additive `phraseNumVoices` inert on the standard path) |
| `composing_tests` | **1101/1101 PASSED** |
| `notation_tests` | **53 PASSED + 4 pre-existing SKIPPED** (no failures, baseline) |
| `pipeline_snapshot_tests` | **11/11 PASSED, NO golden refresh** |
| `docs/scoring_model.md` sync | not required — no scoring term added/modified in `chordanalyzer.cpp` (the only C++ change is a diagnostic field in `batch_analyze.cpp`); template count unchanged |

**Substrates (scratch, read-only):** fs+km 352×3 (regen driver, 0 fail); dev-bed fullspine 718 (parallel
regen, 0 fail). All to `C:/tmp/c1/*` + `tools/corpus_l6_oracle/` (gitignored). The frozen gate corpus was
never regenerated.

**Commits (local, unpushed, fork-only):**
- **`7111f589e2`** `feat(tools): Stage-5 Phase 3 — Class-P reliability maps (L3/L4) + calibration/θ/conformal
  harness + additive phraseNumVoices dump field` (the 6 new tools, 4 map artifacts, the θ ledger, the
  additive `batch_analyze.cpp` field).
- **`<DOCS_SHA>`** `docs(cowork): Stage-5 Phase 3 report + fold (STATUS/HANDOFF/design markers/instruction)`
  (this report force-added; the fold).

*Report generated 2026-07-06 on HEAD `02ec8b0d60` (pre-commit); corpus `c50002fee1`.*
