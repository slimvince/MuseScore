# CC report — Stage-5 fitter, Phase 2.1: the first fit (`kPowerChord3PcPenalty`) — CANDIDATE ONLY

**Dispatch:** `cc_instruction_stage5_phase2_1.md` (Cowork, 2026-07-04) · **Design:** `cowork_stage5_fitter_design.md` (SIGNED, P1-ratified)
**HEAD at dispatch:** `652dd50861` · **branch:** `master` · fork-only (`origin` = `slimvince/MuseScore`), local/unpushed.
**Nature:** the third CC increment of the Stage-5 arc — the FIRST FIT. Produces a **CANDIDATE + a decision surface only.**
**NO committed constant value changed; NO adoption.** Adoption is a separate user-ratified revertible commit (A-4/S-4) that is *not* in this dispatch — this report ends with the adoption artifact **prepared, not applied.**

---

## Commit SHAs (this dispatch)

| # | SHA | Type | Contents |
|---|---|---|---|
| 1 — manifest rationales | **`5c5d0aabdc`** | `docs(tools):` | the two P1-ratified `status_rationale` strings (`kOtherToneFactor`, `maxTotalInversionContextBonus`); **values byte-untouched** |
| 2 — fit optimizer | **`f14e57d6e0`** | `feat(tools):` | fit-driver `fit` coordinate-search subcommand (§5 Optimizer block) + `evaluate --split`; purely additive |
| 3 — this report | *(this commit)* | `docs(cowork):` | `cc_stage5_phase2_1_report.md` (force-add; `/cc_*.md` is gitignored) |
| 4 — the fold | *(next commit)* | `docs(cowork):` | STATUS 22n · COWORK_HANDOFF · design P1 marker · `cc_instruction_stage5_phase2_1.md` (force-add) |

---

## Task 0 — state check

- **HEAD** `652dd50861`, branch `master`, fork-only, local/unpushed.
- **Dirty set matched the dispatch's expectation exactly:** the three Cowork narrative fold files (`COWORK_HANDOFF.md`, `STATUS.md`, `cowork_stage5_fitter_design.md`, carrying the session-22n P1-ratification + P2.1-dispatch text) + the deliberately-untracked scratch (`idiom_discovery/vl_*_out.txt`, `scratch_artifacts/`). Nothing else. **No STOP.**
- **Corpus:** baroque/jazz/default each **352 `.ours.json` + 352 `.music21.json`**; manifest `git_hash 0dd64660f4` (unchanged). Reference corpus read-only throughout.
- **Suites at entry:** composing 1096 / notation 53 / snapshots 11 (Phase-1 end-state; unchanged — no `src/` touch this dispatch).

---

## Task 1 — the two manifest rationale corrections (values byte-untouched)

Edited ONLY the `status_rationale` string on two rows of `tools/param_manifest.json`, to the P1-ratified wording:

- **`kOtherToneFactor`** → *"frozen: the tone-weight family's declared SCALE ANCHOR — a relative-weight system fixes one unit; measured leverage (0.161, Phase-1b rider) shows the anchor is load-bearing, not that it should float (P1 ruling 2026-07-04)."*
- **`maxTotalInversionContextBonus`** → *"frozen: DELIBERATELY NON-BINDING at its current value (2.0 > the 1.85 bonus sum); the individual inversion bonuses are the tunable surface; a floating cap coupled to the bonuses it caps is a redundant degree of freedom. Not 'inert' as a fittable — binds if reduced (Phase-1b rider, Δ 0.101); kept non-binding by ruling (P1, 2026-07-04)."*

**Diff discipline (verified with `git diff --word-diff`):** exactly **2 lines changed, 2 ins / 2 del** — only the two `status_rationale` string bodies. `group`, `name`, `site`, `family`, `value`, `per_preset`, `preset_scope`, `status` (stays `frozen`), `license_provenance`, `sensitivity` all byte-untouched on both rows; every other row untouched. JSON re-parses. **Commit `5c5d0aabdc`** (`docs(tools):` — a rationale-text correction in a tools artifact; no value change → `docs` chosen over `feat`).

---

## Task 2 — THE FIT: `kPowerChord3PcPenalty` (1-D coordinate search, fitting split only)

**Target row.** `kPowerChord3PcPenalty` — G1 continuous, **shared** preset scope, **idiom-varying**, current value **0.30**, site `chordanalyzer.cpp:116`. Chosen at P1 as the clean lever (the one high-leverage Phase-1b row with no batch-stop interaction at ±0.05).

**Search shape (declared).** The manifest has **no `bounds()` entry** for this row (the `bounds` strings elsewhere in the manifest are code-location refs in the `site` field, not fit ranges). Per the dispatch fallback: **ladder [0.0, 1.2], 9 coarse steps (step 0.15)**, then **2 rounds of halved step** around the best FEASIBLE point (a deterministic 1-D pattern search; tie-break toward the current 0.30 on a flat objective). Evaluations: 9 coarse + refine-r1 {0.675, 0.825} (around coarse-best 0.75) + refine-r2 {0.6375, 0.7125} (around r1-best 0.675) = **13 ladder points + 1 baseline = 14 evaluations.**

**Objective + constraints (design §4.2).** Per evaluation: **variant-(b) root-agree duration on the ratified FITTING SPLIT (261)** (`a8 --scores fitting`, via the driver), RN + key tracked beside; per-evaluation constraints **on the fitting split** — no NEW class-(b) batch-stop case (vs the 53/24/53 identity sets restricted to fitting-split scores), and class-(b) root-disagree duration non-increase. **Fitting-split baseline: 63.5026 % @ 0.30** (reproduces the ratified fitting-split baseline 63.50).

**The ladder (fitting split, 261, Baroque carrier):**

| value | root % | Δroot | batch (fit-subset) | new class-(b) | class-(b) dur Δ | feasible |
|---|---|---|---|---|---|---|
| 0.00 | 63.8219 | **+0.3193** | 46 | 3 | −21960 | **NO** |
| 0.15 | 63.8784 | **+0.3758** ← unconstrained max | 45 | 1 | −25920 | **NO** |
| 0.30 (current) | 63.5026 | 0.0000 | 46 | 0 | 0 | yes |
| 0.45 | 63.5610 | +0.0584 | 46 | 0 | −4320 | yes |
| 0.60 | 63.5610 | +0.0584 | 46 | 0 | −5280 | yes |
| **0.6375** | **63.5756** | **+0.0730** | **46** | **0** | **−6240** | **yes ← CANDIDATE** |
| 0.675 | 63.5756 | +0.0730 | 46 | 0 | −6240 | yes |
| 0.7125 | 63.5756 | +0.0730 | 46 | 0 | −6240 | yes |
| 0.75 | 63.5756 | +0.0730 | 46 | 0 | −6240 | yes |
| 0.825 | 63.5756 | +0.0730 | 46 | 0 | −6240 | yes |
| 0.90 | 63.5756 | +0.0730 | 46 | 0 | −6240 | yes |
| 1.05 | 63.5756 | +0.0730 | 46 | 0 | −6240 | yes |
| 1.20 | 63.5756 | +0.0730 | 46 | 0 | −6240 | yes |

**The candidate = `kPowerChord3PcPenalty` 0.6375.** It is the **best constraint-satisfying value**: the objective is **flat at 63.5756 % across the whole plateau 0.6375 → 1.20**, so 0.6375 (the leftmost plateau point found, closest to the current 0.30) is the minimal, conservative choice on a flat objective. Fitting-split gain **+0.0730** (63.5026 → 63.5756), feasible (0 new class-(b), class-(b) duration −6240 = non-increasing).

**★ The fit is CONSTRAINT-BOUNDED — the important structural finding.** The *unconstrained* optimum is **v = 0.15 (+0.3758)** — i.e. **lowering** the penalty gains ~5× more root agreement. But 0.15 (and 0.0) are **INFEASIBLE**: relaxing the power-chord penalty adds **new class-(b) batch-stop cases** among the fitting-split scores (1 at 0.15, 3 at 0.0) even though it *decreases* aggregate class-(b) duration. The no-new-class-(b) constraint (the batch-stop successor semantics) blocks the large-gain direction. So the feasible optimum is a **modest raise** (+0.073), not the larger down-direction gain. Per the dispatch: the search did **not** relax any constraint to chase 0.15 — it reports the best *feasible* value and the blocked direction transparently. This is **not** the "unfittable under constraint" STOP (a feasible improvement exists); it is a feasible-but-constraint-bounded result.

**Phase-1b reconciliation.** The 1b screen tagged this row "clean (no batch-stop interaction)" — accurate **at ±0.05** (0.25/0.35 stay feasible). The full ladder shows that characterization does **not** extend to the whole range: the **down**-direction becomes infeasible below the current value. The candidate lives entirely in the feasible raise region, so the P1 "clean lever, fit isolated first" staging holds; the nuance is recorded.

**Cost / determinism.** 14 evaluations, **~50.5 s/eval** (~11m47s total) — regen-dominated, within the Phase-0 figure (far under the 4×/>180 s STOP). Every evaluation ledgered (`tools/reports/stage5_fit_ledger.jsonl` + the per-run `stage5_fit_kPowerChord3PcPenalty.jsonl`). The search is deterministic (fixed ladder + deterministic tie-break; the Phase-1 determinism proof on the shared `evaluate()` path stands).

---

## Task 3 — the candidate's decision surface (measured, NOT adopted)

### 3.1 Held-out (65) scored ONCE — the overfit check (declared `heldout_check` checkpoint)

| split (denominator) | baseline root % | candidate root % | gain |
|---|---|---|---|
| **fitting (261)** | 63.5026 | 63.5756 | **+0.0730** |
| **held-out (65)** | 62.6364 | 62.5385 | **−0.0979** |

**★ OVERFIT SIGNAL — surfaced prominently.** The candidate **gains on the fitting split but REGRESSES the held-out split (−0.098 root-agree duration)**. This is exactly the design's declared overfit tell (§4.2/§4.3, split hygiene). **No STOP** — the held-out split is never a hard constraint; it is the risk the user weighs at adoption. The full-corpus net (below) stays positive only because fitting (~80 % of covered duration) outweighs held-out (~20 %): 0.8·(+0.073) + 0.2·(−0.098) ≈ **+0.038**, matching the measured Baroque full-corpus +0.0376. The full-corpus number **masks** the held-out regression; the split view exposes it.

### 3.2 Full-corpus, all three carriers (denominator: 326 WiR-covered cells per preset; scratch)

| preset | root base→cand (Δ) | RN Δ | key Δ | batch | batch set-diff (explained) | class-(b) dur Δ | class-(a) dur Δ |
|---|---|---|---|---|---|---|---|
| **Baroque** | 63.3234→63.3610 (**+0.0376**) | +0.0145 | −0.0058 | 53→53 | **EMPTY** (base = CLAUDE.md) | **−4560** | +1440 |
| **Jazz** | 62.3664→62.4518 (**+0.0854**) | +0.0420 | +0.0116 | 24→24 | **EMPTY** (base = CLAUDE.md) | **−7800** | +720 |
| **Default** | 63.2192→63.2742 (**+0.0550**) | +0.0347 | −0.0058 | 53→53 | **EMPTY** (base = CLAUDE.md) | **−5520** | +960 |

- Baseline full-corpus roots reproduce the ratified §4.2 baselines exactly (63.3234≈63.32 / 62.3664≈62.37 / 63.2192≈63.22).
- **The mandatory explained batch set-diff = EMPTY on all three carriers.** `batch_added = {}`, `batch_removed = {}`, `batch_class_changed = {}`, and the measured baseline set **equals the CLAUDE.md canonical 53/24/53 set on all three** (verified via a8's per-case class mapping). **There is nothing to explain per case — the candidate touches no batch-stop identity.**
- **class-(b) (pc-decidable-root) root-disagree duration DECREASES on all three presets** (−4560 / −7800 / −5520) — the successor-stop metric *improves* everywhere.
- **class-(a) duration** rises a small amount (+1440 / +720 / +960) but with **zero batch class-(a) set change** (no added/removed/changed batch case) — sub-threshold duration wobble in already-scored cells, not new symmetric-rotation batch cases; far below any "large class-(a) net increase" (design guardrail 3).
- RN slightly up on all three; key essentially flat (−0.0058 Baroque/Default, +0.0116 Jazz). No sharp RN/key-vs-root trade (the tracked-respect check).

### 3.3 D-4 — Default's relationship to the idiom-#2 fit (measured, not assumed)

The idiom-#2 candidate evaluated on the **Default carrier improves Default's objective (+0.055 > 0)** and **trips no constraint** (batch 53→53 empty diff, no new class-(b), class-(b) duration −5520). Per **D-4, Default is ELIGIBLE to adopt-with-Baroque** — no separate Default treatment is indicated by the numbers.

### 3.4 Jazz — regression spot-check only (A-3 / 4c; NO leverage/fit reading)

Batch **24→24** (empty diff), class-(b) duration **−7800** (improves). **No Jazz regression.** (The +0.0854 Jazz root is *not* read as a fit result — A-3 defers the Jazz-carrier fit to the jazz-GT conversion increment.)

### 3.5 S-5 style/validation sweep — SCOPED REUSE-ONLY → **gap recorded, not built**

Verified at source that **none** of the per-style validation instruments accept `--param-override`: `run_dlc_baseline.py`, `run_validation.py`, `run_{beethoven,chopin,corelli,cpe_bach,dvorak,grieg,mozart,schumann,tchaikovsky}_validation.py`, `validate_slices_corpus.py`. They can only score the **committed baseline**, not the candidate. Scoring the candidate on the DLC research corpora as-is would require **either** threading `--param-override` through a validation runner **or** composing `run_bach_preset --param-override` (regens arbitrary corpus dirs but computes no per-style DCML root-agree) with the `run_*_validation.py` comparison (computes it but with no override) — i.e. an instrument modification or new comparison logic, **out of a fit dispatch's scope (Task 3.4).**

> **★ RECORDED COWORK ITEM — "S-5 candidate-scoring instrument gap":** no validation runner threads `--param-override`, so the S-5 per-style generalization check cannot be run on a *candidate* today. The S-5 guard rides the adoption ratification as a **recorded caveat** until an override-capable per-style validation runner exists (a small additive flag on one runner + the DCML per-style root-agree it already computes). **Not built this dispatch, per instruction.**

### 3.6 Snapshot impact preview (empirical; nothing refreshed)

Ran `batch_analyze --preset Default --dump-regions notation` (the P1–P4 notation path the goldens pin) on the exact 11 snapshot scores, candidate override vs baseline, diffed:

| result | scores |
|---|---|
| **DIFFERS (6)** | 137 chorale · BWV806 Prelude · BWV806 Gigue · K279-1 · BI105-2 op30-2 · corelli op01n08a |
| identical (5) | 001 chorale · 003 chorale · K280-1 · BI105-1 op30-1 · schumann n01 |

The 5 identical scores rule out a stdout log-line artifact (the override "applied N" message is on stderr). The 6 diffs are **genuine region/segmentation changes** (e.g. K279-1 a region `endTick 18240→17760`, `duration 11.25→10.25`). **→ At adoption the pipeline-snapshot goldens WOULD need refreshing (≈6 of 11).** Consistent with this row's 0.308 Phase-1 leverage — the constant is more load-bearing across common-practice textures than its "power chord" name implies. **Nothing refreshed** (nothing adopted).

---

## The PREPARED adoption artifact (described — NOT applied)

The single revertible commit that a **separate, user-ratified adoption event** (A-4 / S-4) would apply:

1. **`src/composing/analysis/chord/chordanalyzer.cpp:116`** — `static double kPowerChord3PcPenalty = 0.30;` → **`= 0.6375;`** (the one behavior change).
2. **`tools/param_manifest.json`** (the `kPowerChord3PcPenalty` row) — `"value": 0.30` → **`0.6375`**; and fill `"license_provenance": null` → the §7 fitted-on statement (*"reference-corpus fitting split (PD/CC-BY-SA), idiom #2 ground truth, only"*).
3. **`docs/scoring_model.md`** (CLAUDE.md sync rule, same commit) — the two value references: line 117 (template-16 note `kPowerChord3PcPenalty = 0.30`) and line 558 (§ constant table `0.30`) → **`0.6375`**.
4. **Rebuild** (5 binaries — the mutable-global initializer changes).
5. **`pipeline_snapshot_tests.exe --update-goldens`** then re-run green — refreshing ≈**6 of 11** goldens (§3.6), only after confirming the delta is the intended fit effect.
6. The commit carries the before/after decision surface (this report) + STATUS/handoff fold (S-4).
- **Per-preset at adoption:** Baroque adopts the idiom-#2 fit; **Default adopts-with-Baroque** (D-4 eligible, measured §3.3); **Jazz unchanged** by this fit (A-3).

---

## Reuse-vs-new + what retires

- **Reuses (verbatim):** `run_bach_preset.py` (regen + `--param-override`), `a8_rebaseline_measure.py` (`--corpus-root`/`--preset`/`--scores`), `characterise_bir_false.py` (batch-stop sandwich), the frozen corpus, `stage5_split_registry.json` (261/65), the `batch_analyze --param-override` binary — all Phase-1 landings, unmodified.
- **New (committed):** the fit-driver `fit` coordinate-search optimizer + `evaluate --split` (`f14e57d6e0`, additive — existing modes byte-unchanged); the two manifest rationale corrections (`5c5d0aabdc`, values byte-untouched).
- **New (gitignored scratch, regenerable):** the fit ledger rows + per-run output under `tools/reports/`; the decision-surface scratch.
- **Retires:** NOTHING. Candidate + decision surface only.

**Provenance note (as-built vs design §7).** §7 states "the ledger is committed." As-built, **`/tools/reports/` is `.gitignore`'d (line 25)**, so the fit ledger is regenerable scratch; the fit's full provenance (the ladder table + the surface) is captured in this **committed, force-added report**. **Recorded for Cowork** as a §7-vs-`.gitignore` reconciliation item (either force-add the ledger, or amend §7 to "provenance captured in the report / regenerable scratch pinned by the driver" — consistent with §7's own A-8 precedent for large per-cell enumerations). Not a blocker.

---

## Sandwich + suites (end-of-run acceptance)

- **Sandwich — `characterise_bir_false.py` on the REAL per-preset dirs ×3:** Baroque **53** / Jazz **24** / Default **53**; **stem@tick set-diff EMPTY both directions** vs the CLAUDE.md canonical sets (parsed + compared, all three). `SANDWICH_RESULT: ALL_MATCH_SETDIFF_EMPTY`.
- **Reference corpus byte-untouched:** `git status tools/corpus/` = 0 dirty; manifest `git_hash 0dd64660f4` unchanged. Every regen (fit, surface, snapshot preview) went to scratch.
- **Suites (no rebuild — no `src/` touch; no golden refresh — nothing adopted):** composing **1096** / notation **53** / snapshots **11**; **0 FAILED**.

---

## STOP conditions — status (none tripped)

- **No committed constant value change, anywhere:** CONFIRMED — only rationale strings (`5c5d0aabdc`), additive tool code (`f14e57d6e0`), and this report. `kPowerChord3PcPenalty` in source is still `0.30`.
- **Best candidate trips a fitting-split class-(b) constraint → "unfittable":** did NOT fire. A feasible improvement exists (0.6375, +0.073). The *unconstrained* max (0.15) is infeasible — reported transparently as **constraint-bounded**; no constraint was relaxed to reach it.
- **Sandwich mismatch / suite regression:** none.
- **Instrument modification beyond additive flags already landed:** none needed. The `fit` mode + `evaluate --split` are additive changes to the **fitter harness / optimizer** (the ratified §5 block), not to the Phase-1 instruments (a8 / run_bach_preset / batch_analyze / characterise), which were used as-is.
- **Eval cost > 4× the ~45 s figure:** not tripped (~50.5 s/eval).

---

## Checkpoint — the adoption decision is the user's

The family result: **a feasible, constraint-bounded candidate `kPowerChord3PcPenalty = 0.6375`** with a small full-corpus root gain on all three carriers (+0.0376 / +0.0854 / +0.055), **batch-stop sets untouched ×3**, class-(b) duration **down** ×3, Default adopt-with-Baroque eligible, no Jazz regression — **against** a **held-out root regression (−0.098)** and a **≈6/11 snapshot-golden refresh** at adoption, with the **S-5 per-style generalization check unrunnable on a candidate today** (recorded gap). The larger objective gain (+0.376) is real but **constraint-blocked** (it would add class-(b) batch cases). Cowork verifies → **the adoption decision (and whether the held-out regression + snapshot churn are acceptable for a +0.04 full-corpus root gain) is the user's.**
