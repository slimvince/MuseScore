# The direct-metric weight search — the ratified fallback: run, established, and a STOP-for-review

**CC, 2026-07-20.** Dispatch `cc_instruction_direct_metric_weight_fit.md` (Cowork 2026-07-19), executing
the user-ruled option 1 after the likelihood fit's STOP (OI-187), with the user's ruling **★R = M2**.

**PYTHON-ONLY, instrument layer only** — no `src/`, no build, no golden, no corpus regen, no
re-baseline. Pinned instruments import-only. **No adoption proposed.**

Every figure below is read from a generated artifact (#17f): `tools/joint_estimator/weight_search.json`
(the search), `search_grading.json` + `search_grading_summary.txt` (the evaluation). Nothing is
hand-transcribed.

---

## 1. The headline — pooled 5-fold CV, each piece decoded once by its own fold's complement model

| arm | key-LOCAL | key-HOME | root | RN |
|---|---|---|---|---|
| **direct-metric search** | **77.60** | **56.46** | **74.19** | **61.77** |
| identity (generative baseline) | 74.68 | 53.20 | 72.70 | 60.08 |
| likelihood fit (OI-187) | 70.22 | 56.34 | 73.04 | 57.99 |
| all-326 publishable (beside, never in place of) | 77.41 | 56.16 | 74.86 | 62.25 |

**Piece-bootstrap 95 % intervals and paired deltas** (paired on the same resamples, #24):

| axis | direct arm 95 % CI | vs identity | vs likelihood |
|---|---|---|---|
| key-local | [75.72, 79.46] | **+2.92** [+2.06, +3.77] ✓ | **+7.37** [+6.16, +8.65] ✓ |
| key-home | [53.76, 59.14] | **+3.27** [+2.40, +4.17] ✓ | +0.11 [−1.29, +1.60] ✗ |
| root | [72.11, 76.43] | **+1.50** [+0.82, +2.17] ✓ | **+1.15** [+0.45, +1.90] ✓ |
| RN | [59.73, 64.02] | **+1.68** [+0.93, +2.46] ✓ | **+3.77** [+2.97, +4.60] ✓ |

✓ = interval excludes zero. **The direct-metric arm beats the identity generative baseline on all four
axes, every interval excluding zero** — and beats the likelihood arm on three, tying on key-home.

The committed current-system baselines (CLAUDE.md block (A), a different unit — whole-corpus, three
presets) remain root 66.04 / 64.98 / 65.93, key-local 65.99 / 62.98 / 65.71; they are carried for
reference only and are **not** comparable cell-for-cell to the CV columns above.

## 2. The prediction verdicts (#17b — bands written by Cowork before measuring)

| axis | band | measured | verdict |
|---|---|---|---|
| key-local | 74–82 | **77.60** | HOLDS |
| key-home | 57–68 | **56.46** | ★ **MISSED** (by 0.54 pp) |
| root | 72–77 | **74.19** | HOLDS |
| RN | 59–66 | **61.77** | HOLDS |

**Three of four hold. The key-home miss is a STOP-for-review per the dispatch** ("a band miss is a
STOP-for-review; this is a fit event, not an exploration"). Two things must be said about it in the
same breath, and neither is offered as an excuse:

1. **The miss is not statistically resolvable.** The 95 % interval [53.76, 59.14] spans the band's
   lower edge of 57.0. Under #24 a difference inside its interval is not a finding — so the honest
   statement is that the point estimate falls below the band while the uncertainty covers it.
2. **The axis nonetheless improved**, +3.27 pp over identity with the interval excluding zero. This is
   a *shortfall against prediction*, not a regression — the opposite of OI-187, where the load-bearing
   axis inverted.

Also: the dispatch's key-local condition ("must not sit below identity beyond the interval — the
search starts AT identity") is satisfied with room to spare, +2.92 pp above identity.

## 3. The OI-187 mechanism did NOT reappear — the modulation-rate check

| arm | key changes / piece | total | pieces with ZERO key change |
|---|---|---|---|
| **ground truth (WiR local keys)** | **5.28** | 1720 | 4 |
| identity | 7.28 | 2372 | 4 |
| likelihood fit (OI-187) | 4.05 | 1321 | **43** |
| **direct-metric search** | **5.52** | 1800 | 9 |
| all-326 publishable | 6.07 | 1979 | 4 |

This is the check OI-187 exists for. The likelihood objective collapsed the decode toward
never-modulating — 43 pieces decoded in a single key for their whole length. **The direct-metric arm
lands closest to the ground truth of any arm measured** (5.52 vs 5.28), where identity over-modulates
at 7.28. The mechanism is not merely absent; the axis it damaged is the one most improved.

## 4. The weight reading — what the metric strengthened and discounted

Reported on the generative scale (the nine generative weights average 1.0, so the vector reads directly
against the identity ablation where each of them IS 1.0). Mean ± sd across the five folds:

| strengthened | | discounted | |
|---|---|---|---|
| declared_mode | **2.941 ± 1.316** | bass | **0.136 ± 0.052** |
| spelling | 1.414 ± 0.658 | boundary | **0.210 ± 0.081** |
| prior (signature) | 1.390 ± 0.779 | chord_trans | 0.357 ± 0.140 |
| key_trans | 1.355 ± 0.661 | entry | 0.405 ± 0.098 |
| | | emission | 0.792 ± 0.373 |

In plain words: **the metric wants the notated evidence — the declared mode, the key signature, and
the notated spelling — trusted far more, and the learned sequential/positional machinery trusted far
less.** The bass factor is discounted ~7×, the segmentation-boundary factor ~5×, chord transitions
~3×. That is a substantive statement about where this model's counted tables are earning their keep,
and it deserves Cowork's reading against the factorization's premise ledger — it is not obviously
what the ratified §5a design expected.

**The cadence features (the OI-190 watch) — a reversal, reported as a finding:**

| feature | direct metric (mean ± sd, folds@0) | likelihood fit (OI-187 record) |
|---|---|---|
| cad_tritone_pair | **0.000 ± 0.000, zero in 5/5 folds AND all-326** | 0.314 ± 0.046, positive in all 5 |
| cad_fermata_location | **0.000 ± 0.000, zero in 5/5 folds** | 0.082 ± 0.051 |
| cad_leading_tone | 0.202 ± 0.149 (zero in 1 fold) | 0.007 ± 0.029, sign-unstable |
| cad_dominant_tonic_bass | 0.610 ± 0.626 | 0.143 ± 0.115 |

The dispatch asked whether the cadence features earn non-zero weight. **Two of the four are pinned at
exactly zero in every fold — the metric rejects them outright** — and the ranking is the *reverse* of
the likelihood fit's: the feature that carried all the load there (tritone_pair, the ★R1 four-beat
window feature) carries none here, and the feature that was indistinguishable from zero there
(leading_tone) carries some here. Two objectives disagreeing completely about which cadence feature
matters is stronger evidence than premise P8 predicted: the four features are not merely overlapping
with the emission, they appear **mutually substitutable and individually unidentified on this corpus**.
OI-190 updated accordingly; this is a form question (#1/#2), not a value tweak.

## 5. ★ The stability record — a prominently-reported finding (OI-191, NEW)

The dispatch asks for the spread of the converged optima as the published protocol's substitute for a
convexity proof, and says a wide spread is to be reported prominently. It is wide.

| fold | best R | worst R | spread | within 1e-3 of best | selected start | identity-start rank | held-out key-local spread |
|---|---|---|---|---|---|---|---|
| fold0 | 0.469963 | 0.502070 | 0.032107 | 1 of 21 | random05 | 5th | 4.28 pp |
| fold1 | 0.478632 | 0.517433 | 0.038801 | 1 of 21 | likelihood_fit | 13th | 3.38 pp |
| fold2 | 0.471913 | 0.490907 | 0.018994 | 1 of 21 | random17 | 19th | 3.88 pp |
| fold3 | 0.462692 | 0.504311 | 0.041619 | 2 of 21 | random06 | 5th | 5.07 pp |
| fold4 | 0.484699 | 0.542887 | 0.058188 | 2 of 21 | random07 | 14th | 5.42 pp |
| all-326 | 0.477130 | 0.553698 | 0.076568 | 1 of 21 | random07 | 6th | — |

**The surface is rugged, not a dominant basin.** Twenty-one restarts converge to twenty-one materially
different points; only 1–2 land within 1e-3 of the best. The named starts are not reliably good — the
identity start won **zero** folds and ranks mid-pack; selection came from a seeded-random start in 4 of
5 folds. Held-out key-local varies by **3.38–5.42 pp** across a single fold's 21 optima.

The methodological consequence, filed as **OI-191**: taking the training-minimum of 21 draws is a
selection over ~21 effective degrees of freedom stacked on the 13 parameters, and the OI-177 capacity
budget does not account for it — that budget was written for a *convex* fit with one optimum, and its
rule ("effective free parameters ≤ training tokens / 10") counts weights, not restarts. This does not
invalidate the held-out figures (each held-out fold was touched exactly once, by an optimum selected
on training alone), but it bounds how much of the gain should be attributed to the weights rather than
to restart selection.

**Corroborating under-determination:** the selected weight vectors are not consistent across folds.
fold2's optimum is qualitatively different — declared_mode 0.370 (vs ~3.1–3.9 elsewhere), spelling
2.639 (vs ~0.6–1.3), key_trans 2.649 (vs ~0.8–1.2), emission 1.529 (vs ~0.5–0.7) — yet grades
similarly. Quite different weight vectors buy the same performance.

**Training gain, for the record** (identity R at the start → best converged R): 0.5231→0.4700,
0.5325→0.4786, 0.5262→0.4719, 0.5148→0.4627, 0.5374→0.4847, all-326 0.5270→0.4771 — a gain of
0.0499–0.0543, reproducing to within 0.004 across five independent training complements.

## 6. The sensitive cases

| case | segments (identity→selected) | key-local | root | RN |
|---|---|---|---|---|
| `bwv352` (the pc-identical share-tone pair) | 39 → 39 | 92.7 → 92.7 | 81.8 → 81.8 | 73.4 → 73.4 |
| `bwv10.7` (the merge-versus-split case) | 49 → 38 | 61.4 → **70.5** | 85.2 → 83.0 | 64.8 → 62.5 |
| `bwv88.7` (the probe's named dominant error) | 29 → 25 | 22.9 → **70.0** | 60.0 → **71.4** | 28.6 → **55.7** |

- **`bwv352`** is byte-unchanged, and the reading at the C2 probe tick 1440 is the same under both
  arms (A minor, I, root 9). The honest near-tie the desk simulation recorded is not disturbed.
- **`bwv10.7`** is the merge-versus-split case the desk simulation surfaced as its one SURPRISE. The
  selected weights **merge** — 49 segments down to 38 — which is exactly the direction the discounted
  boundary weight (0.210) predicts, and key-local improves 9.1 pp while root and RN give back ~2 pp.
  The reading at tick 36000 is unchanged (C minor, II, root 2) under both arms.
- **`bwv88.7`** is the large mover: the opening is re-read from D major / VI (root 11) to **B minor /
  I (root 11)** — the same root, correctly re-anchored as the tonic of the relative minor rather than
  the sixth degree of the relative major. Key-local 22.9 → 70.0.
- **S5, the deceptive cadence:** the desk simulation's verdict is **PRESERVED** — winner C major under
  both the provisional and the selected cadence weights; margin +4.932 → +3.349. The verdict survives
  even though two of the four cadence features are now pinned at zero.

## 7. Establishment (#19) and reproducibility (#16) — all PASS

| check | result |
|---|---|
| cached-lattice decode == pinned `decode_piece`, identity + 4 random weight vectors | 20 checks, **0 mismatches** (score AND segmentation) |
| cached-lattice decode == pinned `decode_piece` at the **selected** weights | 20 checks, **0 mismatches** |
| scale invariance (decode is a function of the ray of w) | 60 checks, **0 path changes** |
| identity arm reproduces committed `fit_grading.json` | **PASS**, 326 pieces, 0 differing |
| likelihood arm reproduces committed `fit_grading.json` | **PASS**, 326 pieces, 0 differing |
| byte-reproducibility: fold0/start0 re-run alone | **PASS** — weight vector, R (0.4745639360038494), evaluation count (355) and all 26 accepted trace moves identical |

The search cannot afford `decode_piece` once per piece per objective evaluation (2.9 s/piece), so it
caches the decoder's own lattice (`fit_weights.build_unit`, `augment_gt=False`) and re-runs the max-plus
recursion at 17 ms/decode — 167× faster. That is exact rather than approximate **because the lattice is
weight-independent** (the prune is a pitch-content filter; the features are raw factor log-probabilities),
and the establishment rows above are what prove it rather than assert it.

**The scale-invariance consequence for the declared bounds:** the decode depends only on the *ray* of w,
so the dispatch's [0, 5] box **constrains exactly non-negativity** — its upper bound cannot bind, since
any ray with non-negative components rescales into the box. Iterates were held at max-component 1.0 and
no clip ever fired. A weight pinned at 0 therefore remains a meaningful finding (and two cadence weights
are); "pressing the upper bound" is not a state this search can reach, and the dispatch's instruction to
report such a press is vacuous by construction rather than unsatisfied.

## 8. The firewall (grep-proven, as the dispatch requires)

- `grade_stems` is the **only** function in `search_direct.py` that grades (one call site,
  `pr.grade_regions(...)` at line 344).
- The **only** stem source is `training_stems`, which returns `fold_of[s] != fold` (or all-326 for the
  publishable model). `search_direct.py` never constructs a held-out stem list — grepping for
  `== fold` returns nothing.
- Held-out evaluation lives in a separate module, `search_run.py`, runs once per fold **after** the
  search has returned, and feeds nothing back. Selection is `select_optimum` — best TRAINING R, ties by
  lower start index — stated as one function so the rule is grep-visible.
- The per-start held-out figures in the stability block are computed **after** selection is fixed and
  are labelled in the artifact as a diagnostic that entered no decision.

## 9. Cost, and the declared approximation to the published method

Search: **46,597 objective evaluations, 140 core-hours**, 126 starts (6 fits × 21), mean 370
evaluations/start, 19 parallel processes, 8.0 h wall. Evaluation: 5,416 s wall, decode mean 3.04–3.69 s.

Method: coordinate line search on a declared multiplicative grid with random restarts — the published
minimum-error-rate protocol (Och 2003, *Minimum Error Rate Training in Statistical Machine Translation*,
ACL). **The one declared approximation:** Och searches each coordinate line *exactly* by an
upper-envelope sweep over the candidate set; here each line is searched on the declared grid
(stages (2.0, 1.5), (1.25, 1.1), (1.05), ≤3 sweeps each, plus an explicit 0.0 probe per coordinate in
stage 0 so "the metric rejects this factor" is reachable). Recorded in the artifact provenance.

## 10. Anomalies and honest caveats

1. **★ The key-home band miss (§2) is the STOP-for-review.** Not built around; nothing adopted.
2. **★ The rugged surface (§5) — OI-191, NEW.** The capacity budget does not cover restart selection.
3. **★ The cadence-feature reversal (§4) — OI-190 sharpened.** Two features rejected outright; the
   ranking inverts between objectives.
4. **The prune interacts with the weights (OI-188 updated).** At the selected weights the declared
   prune costs key-local +2.15 pp, key-home +3.22 pp, RN +1.19 pp — materially less than at the
   likelihood weights (+7.04 / +9.31) and less than identity on key-local (+4.8). **Unexplained: root
   is −0.58 pp**, i.e. loosening the prune makes root slightly *worse*. Small, but it is an anomaly and
   is carried rather than smoothed over.
5. **Instrument edits after launch, declared in full.** Three edits were made to `search_direct.py`
   after the 19 processes started: an unused `import math` removed; a docstring corrected
   (`search_fit`→`training_stems`); the dispatch filename corrected in the provenance label. **None
   touches arithmetic, a constant, or control flow** — and the byte-reproducibility check in §7 re-ran a
   start under the *committed* code and reproduced the original trace exactly, which establishes rather
   than asserts it. `merge_parts` was additionally hardened to regenerate provenance from the committed
   code and to STOP if any part declares different search constants; it did not trip.
6. **A single-point-of-loss in the run design, for the record.** Each process wrote its part artifact
   only after all its starts finished (~8 h in); a process dying at hour 7 would have lost its weight
   vectors, the logs retaining only the per-start R values. No process died, but the design was mine and
   the risk was real.
7. **Scope.** Fitted values are Bach-chorale values (OI-177 item 6); generalization claims stay
   de-scoped. The prune caveat (OI-188) still makes every column a conservative lower bound.

## 11. What is NOT claimed

No adoption is proposed. The OI-178 robust-stop adoption protocol has **not** been run — no full-corpus
a8 measurement, no `tools/robust_stop/` re-baseline, no class-(b) duration diff, no snapshot. The CV
columns here are on the joint estimator's own decode, not on the committed pipeline, and they do not by
themselves satisfy any adoption gate. The funnel does not advance on this report; it returns for the
user's and Cowork's review, with the §10 items as the agenda.
