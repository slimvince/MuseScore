# Precision-Headroom Investigation — Re-grounding Stages 4–6 on Measured Error Structure

*CC, 2026-06-13. Base commit `a652dc1ba7` (working tree otherwise clean; this dossier and
the throwaway `/c/tmp/*.py` drivers are the only writes — no production code, no behavior
change, no commit beyond this file). Beam-widening is shelved (its Δ=+7a justification is
falsified and re-verified live this session — see `cc_stage3_2_design_report.md` / roadmap
3.2). This is a READ-ONLY measurement + mapping task.*

**Lodestar:** where is the realistically reachable headroom toward maximally-precise inference
of (mode, functional chord, actual chord), and which layer unlocks each slice?

Every number is tagged **[probe]** (ran a script and read output) or **[doc]** (read from a
committed artifact). Every mechanism classification is tagged **sampled** (read N cases and
hand-classified) or **inferred** (deduced from aggregate structure, not case-read).

---

## §1 — Metric stance and the error-structure decomposition

### 1.1 Stance (stated and justified)

| Axis | Choice | Why |
|---|---|---|
| **Ground truth** | **DCML/WiR human annotation ONLY** (no music21 filter) | music21 is an *algorithm*, not ground truth (corpus audit C2 [doc]). The headline gate's "13/24 genuine" requires music21∩DCML agreement — an algorithm adjudicating which human disagreements count. This investigation removes that filter; the three-way (ours/m21/WiR) is computed *only to size the filter's effect*, never to filter. |
| **Config** | **`--preset Default`** (the live out-of-box product config) | The instruction's "user-facing config." `tools/corpus/default/` is manifest-validated at HEAD `a652dc1ba7`, preset=Default, 353 scores, music21 9.9.1 [probe]. Not the Baroque-tuned gate config. |
| **Alignment** | region-centric **time-overlap lenient-OR (≥50% either side)** | The single-sourced comparator in `compare_analyses.align_dcml_regions(mode="time-overlap")` — the same one `compare_rn` and `characterise_bir_false` use [doc/probe]. |
| **Granularity** | **batch (primary) + section (A/B)** | The `.ours.json` regions are batch (cross-barline) regions. Section = measure-aligned (`--section-level`). The 2.2-i ~7× gap means one number lies — both reported below. |
| **Tool** | thin driver `/c/tmp/bach_rn_decomp.py` | Reuses VERBATIM `compare_rn.classify_pair` (the bucket metric) + `compare_analyses.align_dcml_regions`/`three_way_classify` + `dcml_parser.find_wir_file`/`parse_rntxt_file`. It only wires the **Bach WiR rntxt reference that `compare_rn` lacks** (compare_rn is TSV-only; its `--cross-corpus` therefore *excludes Bach* — see 1.4). **Not a new metric.** |
| **Corpus** | **326/353 WiR-covered Bach chorales** (the gate set) | 326 confirmed via `find_wir_file` [probe], not 0 (a sub-probe initially mis-reported 0 by searching paths instead of the stem index — corrected). Non-Bach reported as stale *shape* only (1.4). |

### 1.2 The decomposition — Bach gate set, Default preset, batch granularity [probe]

`python /c/tmp/bach_rn_decomp.py tools/corpus/default` — **326 movements, 10 108 matched regions:**

| Bucket | % matched | count | Target axis |
|---|---:|---:|---|
| exact | 32.2% | 3 254 | (agreement) |
| partial (root+quality, inv/ext differs) | 10.1% | 1 019 | (agreement) |
| **rn_agree (exact+partial)** | **42.3%** | **4 273** | — |
| **key_disagree** (root✓, quality✓, degree✗) | **27.9%** | **2 823** | **mode/key** |
| **quality_disagree** (root✓, quality✗) | **3.0%** | **306** | **functional chord (quality)** |
| **root_err** (root✗) | **26.8%** | **2 706** | **actual chord (root)** |

Three-way (ours/m21/WiR root-pc), same denom 10 108 [probe]:
`all_agree 71.8% (7259) · dcml_ours_agree 1.4% (143) · music21_dcml_agree 1.3% (130) · all_differ 25.5% (2576)`.

**The load-bearing identity:** `root_err 2706 = all_differ 2576 + music21_dcml_agree 130` exactly [probe].
So the actual-chord-root error mass splits cleanly:

- **95.2% (2576) = "neither"** — neither we *nor music21* reach DCML's root.
- **4.8% (130) = vertically fixable** — music21 (a competent vertical analyzer) gets it right, we don't.

**This is the central re-grounding result.** The music21-filtered gate ("13 genuine BIR=false")
measures only the 4.8% vertically-reachable slice and *discards the 95% functional residual by an
algorithm's opinion*. The gate has been optimizing the small reachable-by-emission corner while the
real root-error mass is functional readings vertical analysis cannot reach.

### 1.3 The "neither matches DCML" residual — quantified and characterized [probe]

`all_differ = 2576 regions = 25.5% of all matched` (corpus-wide on Bach) — this corpus-sizes the
3.1b A/B's ~40% "neither" on root-differing ticks [doc]; here it is **95.2% of root-differing
regions** (2576/2706), even higher, because the chorale gate is homophonic. Characterized by reading
22 sampled cases (`/c/tmp/sampler.py`, category `rooterr_localkey_ok` ∩ all_differ) — **sampled**:

- **Cadential 6-4 / dominant-bass** — bwv174.5 m5: ours `I/A` (r=D), WiR `V` (r=A); bwv64.4 m1 ours `I` WiR `V6`. We read the literal tonic-over-dominant-bass sonority; DCML reads the functional dominant.
- **Suspensions / NHT** — bwv306 m2 ours `Vsus4`, WiR `vi`; bwv353 ours `Isus2`, WiR `V6`; bwv368 ours `vi11`, WiR `V6`. We label the suspended sonority; DCML the resolution harmony.
- **Applied/secondary roots** — bwv190.7 ours `V7/V`, WiR `I`; bwv436 ours `V7/V`, WiR `V6`.
- The common thread: **DCML's root is a property of voice-leading/function, not the vertical pitch
  set.** music21 misses them too (that is what `all_differ` *means*) → not a vertical-scoring bug.

### 1.4 Other granularities and corpora

**Section granularity (measure-aligned), same metric, Baroque preset A/B** [probe]
(`tools/corpus/baroque` vs `tools/corpus_ab/baroque_section`; Baroque batch output held byte-identical
across Stage 2.2→3.4 per the roadmap's per-stage gates [doc]):

| | rn_agree | root_err | root_err = neither + m21-fixable | m21-fixable share of root_err |
|---|---:|---:|---|---:|
| **batch** | 42.3% | 26.7% (2700) | 2580 + 120 | **4.4%** |
| **section** | 37.9% | 33.5% (3747) | 2978 + 768 | **20.5%** |

Two effects, both load-bearing: (a) finer regions surface ~1.4× more root errors in *rate* (26.7→33.5%)
and rn_agree drops 4.4pp — the batch gate is the most flattering surface, and the **user-visible**
status-bar (clicked-note) view is finer than batch, so users see closer to the section numbers;
(b) the **vertically-fixable (Stage-5-reachable) slice is ~6× larger at section granularity** (120→768) —
the coarse gate masks vertical errors too, not only functional ones. *Which number is user-visible: the
finer one.* (Default-section corpus is not pre-generated; multiplier measured under Baroque — preset-robust
per 2.2-i [doc]. A Default-section corpus-wide run is the Stage-5 granularity-metric deliverable, not regenerated here.)

**Non-Bach cross-corpus — STALE, shape only** [probe]
(`compare_rn --cross-corpus tools/reports/live_20260603`; June-3, pre-`a652dc1ba7`, pre-F1-metric,
preset uncertain — flagged for Stage-5 re-measure [doc]). 520 movements, 61 233 matched:
`rn_agree 27.6% · key_disagree 15.2% · quality_disagree 6.5% · root_err 50.7%`. This *exactly*
reproduces the documented 27.6%/15.4%/6.3% figures — confirming they are the **non-Bach** set
(Bach excluded). Per-corpus root_err: corelli 55.0%, bach_suites 53.5%, tchaikovsky 53.2%, beethoven
51.7%, mozart 51.5%, grieg 49.1%, schumann 48.9%, chopin 41.6%, dvorak 40.8% (cpe_bach empty — known
0-region issue [doc]). **The actual-chord-root axis dominates harder repertoire (~2× the chorale rate);
the functional-vs-vertical split there is unmeasured** (ABC/Beethoven etc. have no music21.json — §4).

### 1.5 How much rides on key being wrong upstream [probe]

Cross-tab of bucket × (our key tonic+mode vs DCML local/global key), `/c/tmp/key_confound.py`:

- **DCML tonicizes/modulates on 39.9% (4036/10108) of annotations** (local_key ≠ global_key) — its
  local-key analysis is active on ~40% of regions. This is the functional/sequence layer made visible.
- **key_disagree (2823) — root is correct by definition; only the key-context label differs:**
  - **63% (1791): our key = DCML *global* but ≠ DCML *local*** → DCML tonicized and we stayed in the
    global key. **A secondary/tonicization labeling gap, not a key-detection error.**
  - **37% (1032): our key ≠ DCML *global*** → genuine key/mode error.
- **root_err (2706):** 1237 (46%) occur with the *correct* local key (not key-driven); ~1004–1448
  co-occur with wrong key (causation is co-occurrence, not proven — chicken-egg with key inference).

---

## §2 — Slice → unlocking-mechanism map

Sizes are % of the 10 108 matched Bach regions (Default, batch). Confidence per the §1 tags.

| # | Slice | regions | % | What it IS (evidence) | Unlocking layer | Confidence |
|---|---|---:|---:|---|---|---|
| S1 | **Tonicization / secondary label** (key_disagree, =global ≠local) | 1 791 | 17.7% | root+sonority+global-key all correct; degree differs only because DCML reads a local tonic — V/V (bwv153.9, 322), tonicized V (bwv17.7, 37.6, 429), relative-major modulation (bwv10.7, 122.6, 350). 22/22 sampled uniform. | **Stage 6** (functional: secondary dominants / tonicization) consuming **Stage 4.2 KeyArea** spans | **HIGH** sampled |
| S2 | **Key-detection / relative-key error** (key_disagree, ≠global) | 1 032 | 10.2% | root correct; our global key/mode wrong — heavy relative major↔minor (a↔C bwv16.6/420, d↔F bwv244.54/343, e↔G). The documented partial-signature pattern [doc]. | **Stage 4** (key path / relative & partial-signature disambiguation) | **HIGH** sampled |
| S3 | **Root err — functional "neither"** (all_differ) | 2 576 | 25.5% | cadential 6-4, suspensions, passing/NHT, applied roots, pedal — non-vertical readings; music21 also misses (def. of all_differ). 1107 with correct local key (pure functional/ceiling); ~1448 entangled with wrong key. | **Stage 6** (functional) + **structural ceiling**; key-entangled part shares **Stage 4** | **MED-HIGH** (sampled heterogeneous; three-way identity exact) |
| S4 | **Root err — vertically fixable** (music21_dcml_agree) | 130 | 1.3% (→20.5% of root_err at section) | 6th-chord/add6 vs 7th (bwv10.7 VI-add6↔ii6), over-extension M13/M13⁴³ (bwv20.7, 325, 329), inversion/root-selection (vi↔IV6, iii↔I6, V6↔viio6). A better vertical scorer gets these. | **Stage 5** (emission reweight + the frozen B4 6th-chord/extension templates); some **Stage 3** transition | **HIGH** sampled (m21 corroborates reachability) |
| S5 | **Quality / figured-bass convention** (quality_disagree) | 306 | 3.0% | seventh-chord inversion figured-bass labels (vi65↔ii6/5, viiø65↔ii%65) + implied-7th convention gap [doc]. root correct. | **Stage 6** (functional / figured-bass convention) | **MED** sampled (top patterns) |
| S6 | **Inversion/extension residual** (partial) | 1 019 | 10.1% | counts as agreement (root+quality ✓) but inversion/extension differs — figured-bass detail. | **Stage 6** figured bass / minor | **LOW** (not separately sampled) |

**Roll-up by layer (Default batch, % of matched):**

- **Stage 4 (key path):** S2 (10.2%) + the key-entangled part of S3 (≈10–14%) → **~20–24%**, of which ~10% (S2)
  is clean (root already right, only the key/degree wrong). *Inferred for the entangled part.*
- **Stage 6 (functional layer):** S1 (17.7%) + the functional part of S3 (~11% pure + share of entangled)
  + S5 (3.0%) + S6 (10.1%) → **~35–42%**. The single largest reachable axis. Much of it (S1) has the
  chord *and global key already correct* — it is purely a missing functional label.
- **Stage 5 (emission/weight fitting):** S4 → **1.3% at batch, ~6–7% at section**. Small direct yield on the
  gate set, but Stage 5 is the *enabler* (fits the transition/functional/key edges the other layers need).
- **Structural ceiling:** the part of S3 that is genuinely vertical-ambiguous even for a sequence model
  (e.g. pedal points, enharmonically-collapsed readings) — not separately sized (§4).

---

## §3 — Re-grounded roadmap recommendation

### 3.1 What the headroom map changes

The original order (3 decoder → 4 key → 5 fit → 6 functional) assumed precision lives behind the
decoder. The measurement says otherwise, on the gate set:

1. **Search is not where precision lives — confirmed and generalized.** The Δ=+7a finding (greedy path
   *is* the global optimum) is not a one-off: the dominant error mass is **emission/transition/key-context
   labeling**, not search. Re-ranking a lattice cannot move S1/S2/S3/S5 — only re-weighting edges,
   adding a functional/key state space, or fixing the key. Beam-widening stays shelved (3.4 gate-folding
   + Stage-5 edge-reweighting are beam-1 operations).
2. **The largest user-facing precision win is the functional layer (Stage 6), and it is gated on the key
   path (Stage 4).** S1 (17.7%, the biggest single slice) is *root-and-global-key-correct* tonicization
   labels — unlockable only by KeyArea spans (4.2) feeding a secondary-dominant/tonicization labeler (6.1).
   So **Stage 4 is the prerequisite that unlocks the largest functional slice**, and Stage 4 is independent
   of the decoder (roadmap note: "may be promoted ahead of Stage 3" [doc]).
3. **Stage 5's direct yield on the gate is small (1.3% batch) but it is the structural enabler**, and its
   objective must be **granularity-robust + DCML-only** — the batch+music21 gate hides ~95% of the root-error
   mass and ~6× of the vertically-fixable slice (§1.2/1.4). Fitting against the current gate would fit to the
   wrong objective.

### 3.2 Recommended ordering (the decision is Cowork/user's)

> **Finish the Stage-3 consolidation (gate-folding 3.4 → split 3.5) as the substrate, then lead the back
> half with Stage 4, co-develop Stage 6 on its KeyArea output, and run Stage 5 last as the fitter — with a
> granularity-robust, DCML-only objective defined *before* fitting.**

Concretely:
- **3.4/3.5 (now):** continue gate retirement + the chordanalyzer split. Beam stays at 1. Pure consolidation;
  no precision claim. (Δ=+7a routes to Stage 5's transition reweight, per the falsification.)
- **Stage 4 FIRST in the back half:** key as a path (HMM over the 252-candidate window scores) **+ KeyArea spans (4.2)**.
  Directly addresses S2 (~10% clean) and the relative/partial-signature systematic error; *and* produces the
  KeyArea spans S1 needs. Measure key_disagree's "≠global" half before/after.
- **Stage 6 co-developed on the KeyArea output:** secondary-dominant/tonicization labeler closes S1 (17.7%) +
  S5 (3.0%) + the functional part of S3; cadential-6-4 / suspension / passing labeling addresses the largest
  part of S3. This is the rn_agree ceiling the architecture review predicted [doc].
- **Stage 5 LAST as the fitter:** once transition + key + functional edges exist to weight, fit them against
  DCML (structured perceptron / coordinate descent). **Mandatory objective fixes first:** (a) granularity-robust
  metric (the section-vs-batch mix shift, §1.4), (b) DCML-only gate variant (drop the music21 filter — it
  discards 95% of the mass). S4's vertical slice + the frozen B4 6th-chord templates fold in here.
- **Joint segmentation:** defer past Stage 5 (needs the granularity-robust metric to even score; the 3.1b A/B
  showed whole-score is *not* a uniform accuracy win [doc]).

### 3.3 The beam-revisit trigger (so it's revisited on evidence, not forgotten)

Beam>1 is currently beam-1-substitutable (verified — Δ=+7a's greedy path is the global optimum). **Beam
becomes worthwhile when search genuinely matters**, i.e. when there exists a case where the globally-best
path ≠ the greedy path AND the global path is more DCML-correct. That requires a **non-monotone edge**: a
transition/forward-completion edge (a Stage-5 addition) whose benefit only materializes with lookahead, so a
locally-suboptimal node wins globally. **Revisit beam when either:** (a) Stage 5 introduces such a
forward-completion / resolution edge (e.g. the Δ=+7a rcb-suppression + completion edge), and a measured case
shows global-best ≠ greedy with global-best matching DCML; or (b) the functional/key layers create a
genuine path-level competition (cadence-driven re-segmentation) the greedy commit can't express. Until one of
those fires, beam stays at 1.

---

## §4 — Unknowns / what couldn't be measured cheaply, and why

1. **Default-section corpus not pre-generated.** The granularity multiplier (§1.4) is measured under
   **Baroque** preset (batch vs section A/B from existing dirs); preset-robust per 2.2-i but not the exact
   Default-section numbers. A Default-section corpus-wide regen (353 `batch_analyze --section-level` runs) is
   the **Stage-5 granularity-robust-metric task**, deliberately not run here (cost + it is Stage-5 scope).
2. **Non-Bach cross-corpus is triply stale** (June-3 commit, pre-F1-metric, preset uncertain) → reported as
   *shape* only. Re-measure at `a652dc1ba7` under Default is the Stage-5 entry task [doc]. *No metric run was
   blocked by needing a production change* — this is a regen-cost choice, not an obstacle.
3. **Functional-vs-vertical split is unmeasurable on the no-music21 corpora** (ABC/Beethoven and others lack
   `.music21.json`), so the all_differ vs m21-fixable identity (§1.2) is established **on Bach only**. Whether
   the harder repertoire's 50.7% root_err is similarly 95% functional is **unknown** — needs music21 generation
   for those corpora (Stage 5).
4. **"Rides on key" is co-occurrence, not proven causation** (S3 entangled part, §1.5): a region with wrong
   key AND wrong root could be either-causes-either. The clean Stage-4 slice (S2, 1032, root-already-right) is
   causally unambiguous; the ~1000–1448 root-errs-with-wrong-key are a *range*, **inferred** not sampled-causal.
5. **S3 functional sub-types are sampled-heterogeneous, not auto-tallied.** I read cadential-6-4 / suspension /
   applied-root cases but did not count each type corpus-wide — that needs a 6-4/suspension detector, which is
   itself Stage-6 scope. S3's "MED-HIGH" reflects this.
6. **2.4% (239/10108) our-key parse failures** in the key cross-tab regex (unusual mode tokens) lump into the
   tonic✗ column, marginally inflating S2 / the key-driven root-err estimate. Does **not** affect the §1.2
   bucket decomposition (independent of the key parser). Flagged; small.
7. **Structural-ceiling slice is not separately sized** — the part of S3 unreachable by *any* planned layer
   (pedal points, enharmonic collapses, genuinely ambiguous verticals). It is bounded above by S3 (25.5%) and
   below by the music21-also-correct-but-still-no-sequence-model cases; pinning it needs a sequence-model
   oracle that does not exist yet.

---

*Drivers (throwaway, untracked, `/c/tmp/`): `bach_rn_decomp.py`, `key_confound.py`, `sampler.py` — each
reuses the committed metric machinery verbatim; none writes to the repo. This dossier is the only repo write.*
