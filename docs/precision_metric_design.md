# Precision-Metric Design — the measurement instrument for maximally-precise inference of (mode, functional chord, actual chord)

> **DRAFT. Design + scoping only; no production code, no behavior change.**
> Drafted against base commit `a652dc1ba7` ([probe] `git rev-parse --short HEAD`) — the base it was
> written against, not a statement of its current standing. Read-only investigation. Deliverable for
> the ratification gate that precedes building any metric.
>
> **★ THE "UNCOMMITTED" CLAIM IS STRUCK: THIS FILE IS TRACKED AND COMMITTED (corrected 2026-08-14 at
> `cc_instruction_scoring_model_pass.md`, discharging the false half of `OPEN_ITEMS.md` OI-274's
> third instance).** Established at the git object by explicit hash, not asserted. **The former
> wording, preserved (#12), was:** "**DRAFT — UNCOMMITTED. Design + scoping only; no production code,
> no behavior change.** Base commit `a652dc1ba7` ([probe] `git rev-parse --short HEAD`)."
>
> **What this correction does NOT decide.** Only the false statement about the file's own standing
> is struck. The DRAFT marking stands as written; nothing above says whether the ratification gate
> this document is a deliverable for has been passed, and this correction establishes nothing either
> way about that.
>
> Every existence claim is tagged **[code]** (read the source) or **[probe]** (ran it and read
> output). Every design choice is argued. The chicken-and-egg (a functional-precision metric needs
> a functional-label vocabulary that is itself Stage-6 output) is resolved explicitly in §3.
>
> *Inputs read: `cc_precision_headroom_dossier.md`, `cc_stage1d_report.md` §1, `cowork_corpus_audit.md`,
> `docs/p3_granularity_ab_3_1b.md`, `cc_stage2_2_ab_dossier.md`, `docs/redesign_plan.md` (arch addendum)
> + `cowork_target_architecture_review.md` §A (rn_agree baseline), `docs/implementation_roadmap.md`
> Stages 4–6, and the metric sources `tools/compare_rn.py` / `tools/dcml_parser.py` /
> `tools/compare_analyses.py`.*

---

## §0 — TL;DR (the build/reuse split, up front)

| | What | Status |
|---|---|---|
| **REUSE as-is** | `compare_rn.classify_pair` buckets (exact/partial/key_disagree/quality_disagree/root_err); `compare_analyses.align_dcml_regions` (time-overlap lenient-OR); `dcml_parser` DCML/WiR parse + root_pc resolution | exists, pinned by 54 metric tests [doc] |
| **REUSE, promote to committed mode** | the dossier's **Bach-WiR wiring** (the throwaway `/c/tmp/bach_rn_decomp.py` that feeds `compare_rn` the WiR rntxt reference it lacks) → a first-class `compare_rn --wir-bach` mode | prototype exists; not committed |
| **BUILD (genuinely new)** | (1) a **granularity-robust scoring unit** (duration-weighted over a fixed grid) so batch/section stop disagreeing by ~7×; (2) the **label-vocabulary contract** (Stage-6 output spec = metric input spec) + the metric-side parser fixes (F-2 It6/Ger/Fr/N) it requires; (3) the **DCML-only objective** for Stage-5 fitting | none built |
| **KEY FINDING (changes the framing)** | `classify_pair` **already credits** a correctly-emitted secondary (`V7/V` vs `V7/V` → `exact` [probe]). S1 tonicization (17.7%) sits in `key_disagree` **because we emit `II` not `V/V`** — the comparator can score it; the pipeline can't emit it. So **the metric is not the blocker for the functional axis; emission is.** This *interleaves* metric work with Stage 6 rather than strictly preceding it (§4). |

---

## §1 — What already exists (don't rebuild what's there)

### 1.1 `compare_rn` IS already the DCML-only metric

**Claim (instruction Task 1.1): "remove the music21 filter" = "use `compare_rn`, not the BIR gate."** Confirmed.

- `compare_rn.classify_pair(ours_region, dcml_region)` compares **our output directly to the DCML
  annotation** — there is no music21 leg anywhere in `compare_rn.py` [code] (the only imports are
  `compare_analyses` and `dcml_parser`; no `.music21.json` is read). The music21 filter lives in the
  *other* two scripts: `characterise_bir_false.main` and `analyze_inversion_errors.py` gate a case on
  `three_way_classify == 'music21_dcml_agree'` [code, cc_stage1d §1.2 / 2.2-i §1]. That three-way is
  what makes "13 BIR=false" a *music21-filtered* number. `compare_rn` has no such filter.
- The four buckets and exactly what each compares [code `classify_pair:229-293`]:

  | bucket | condition | precision axis it measures |
  |---|---|---|
  | `exact` | root_pc equal ∧ degree-base (case) equal ∧ normalised RN strings equal | full agreement |
  | `partial` | root_pc equal ∧ degree-base equal ∧ strings differ (inversion/extension) | figured-bass / inversion detail |
  | `key_disagree` | root_pc equal ∧ degree-base **differs** ∧ coarse `extract_quality` **agrees** | **key/mode-context + tonicization** (V↔I, II↔V/V) |
  | `quality_disagree` | root_pc equal ∧ degree-base differs ∧ coarse quality differs | **true chord-quality** error |
  | `root_err` | root_pc differs | **actual-chord root** (≡ the BIR=false *set*, unfiltered by music21) |

  `rn_agree = (exact + partial) / matched`. The split invariant `key_disagree + quality_disagree =
  #(root match ∧ degree differs)` is pinned [doc, cc_stage1d §1.2].
- Root_pc comparison is the same on both sides: ours `rootPitchClass`; DCML `root_pc` is **computed
  from the `numeral` column resolved in the effective key** (`_resolve_effective_dcml_key` folds
  `localkey` then `relativeroot`), so a DCML `V/V` in C resolves to sounding root D=2 [code
  `dcml_parser:99-133, 240-257`; probe §1.5 below]. This is why the actual-sounding root, not the
  notational degree, is what `root_err` adjudicates.

**Corpora it runs on TODAY [code]:** `compare_rn` is **TSV-only** in committed form. Its `--corpus`
path globs `*.ours.json` and matches `{stem}.harmonies.tsv` (`_find_tsv`); its `--cross-corpus`
iterates the 10 non-Bach corpora in `CROSS_CORPORA` (dvorak…bach_suites), all of which have
`harmonies.tsv`. **Bach chorales have NO `.harmonies.tsv`** — their human annotation is When-in-Rome
**rntxt**, which `compare_rn` does not load. So `--cross-corpus` **structurally excludes Bach** — and
the documented "non-Bach 27.6%/15.4%/6.3% / root_err 50.7%" figures are exactly that exclusion
[doc, headroom dossier §1.4; this reproduces the cowork arch-review §A "rn_agree 27.6%" baseline].

### 1.2 The Bach-WiR wiring (what to formalize)

The headroom dossier scored Bach by wiring the WiR reference `compare_rn` lacks, **reusing the
committed machinery verbatim**: `compare_rn.classify_pair` + `compare_analyses.align_dcml_regions` +
`dcml_parser.find_wir_file`/`parse_rntxt_file` [doc, dossier §1.1 Tool row]. The only new code was the
glue that (a) finds the WiR `analysis.txt` for a stem (`find_wir_file` walks
`Corpus/Early_Choral/Bach…/Chorales/*/remote.json` [code `dcml_parser:410-451`]) and (b) parses it to
`DcmlRegion`s (`parse_rntxt_file`, which already exists and is metric-pinned [code; cc_stage1d §1.1]).

**Recommendation: promote this to a committed `compare_rn --wir-bach DIR` mode** (parallel to
`--corpus`/`--cross-corpus`). It is ~20 lines of orchestration over already-pinned metric functions —
**not a new metric**. Doing so closes the single largest coverage hole (the 326-chorale gate set is
the most-annotated, most-homophonic, most-trusted slice and `compare_rn` can't currently touch it) and
makes the dossier's central numbers reproducible without a `/c/tmp` driver. The metric definition does
not change; only the reference-file plumbing is added (the cc_stage1d NOT-PINNED §3.2 "cross-corpus
orchestration is not a metric definition" applies — this is orchestration, safe to add).

> **Coverage fact to carry forward [doc, roadmap 5.2]:** only **326/353** gate chorales have a WiR
> annotation at all; 27 scores can never be scored against human ground truth. `--wir-bach` must
> report the 326 denominator explicitly, never silently divide by 353.

### 1.3 What `compare_rn` does NOT yet measure (the gaps, against the headroom axes)

**(a) Granularity — the big one.** `classify_pair` scores **whatever regions exist**; the denominator
is "number of our regions that aligned to a DCML row" (`score_piece` iterates `for ours_r, dr in
zip(ours_regions, matches)` [code `compare_rn:357-389`]). It has **no fixed scoring unit**. The 2.2-i
A/B proved the consequence: holding the *analysis byte-identical*, switching batch→section regions
moved `rn_agree` 42.3%→37.9% and `root_err` 2700→3747 — and **root_agree absolute stayed flat
(7418→7424)** [probe, dossier §3.5]. The "+1047 root_err" is **denominator inflation**, not new
errors: finer regions add comparison points, almost all disagreements, while the correct-region count
holds. **So the same system scores ~7× worse on per-beat than on batch granularity, and the integer is
not comparable across the two** [doc, 2.2-i §3.2]. This is the genuine new design work (§2).

**(b) Tonicization / secondary labels — measurable, but only once emitted.** Traced empirically
[probe `/c/tmp/probe_secondary.py`, this session]:

```
exact         | ours=V7/V (Dom7)  dcml=V7/V (Dom7)   we emit secondary in DCML notation → CREDITED
exact         | ours=V/V  (Maj)   dcml=V/V  (Maj)    triad secondary → CREDITED
key_disagree  | ours=II   (Maj)   dcml=V/V  (Maj)    we emit GLOBAL-key degree → lands in key_disagree
key_disagree  | ours=II7  (Dom7)  dcml=V7/V (Dom7)   same: root✓ quality✓ degree✗
root_err      | ours=I    (Maj)   dcml=V    (rootA)  cadential-6-4 / dominant-bass → root_err
```

**The comparator can already score a secondary** — `split_rn` keeps the full suffix, so `V7/V` vs
`V7/V` is `exact`. The reason S1 tonicization (17.7%) is *not* credited today is that the **pipeline
emits `II` (the global-key reading), not `V/V`** [confirmed: dossier §2 S1 "root+sonority+global-key
all correct; degree differs only because DCML reads a local tonic"]. So **the metric is not the gap on
the secondary axis — emission is.** The degree-string comparison already does the right thing; the
chicken-and-egg is real but narrower than feared (§3).

**Caveat — the metric-side parser has known holes for the harder functional tokens [code/probe,
cc_stage1d F-2; 2.2-i §4]:** `normalise_rn`/`split_rn`/`extract_quality` mis-handle the augmented-sixth
and Neapolitan vocabulary: `It6` matches degree `I` and is mis-read as a **major tonic** (wrong root
contamination); `Ger65`/`Fr43`/`N6` fall through `split_rn`→`?`→root-only fallback. On Bach this is 2
tokens (nil), but cross-corpus DCML has `Ger`≈1400, `It`≈600, `Fr`≈480 [probe, 2.2-i §4]. **So before
Stage 6 emits aug6/Neapolitan labels, the metric must learn to parse DCML's side of them** — that is a
concrete BUILD item, bundled with the label-vocabulary contract (§3.1).

**(c) Cadence / figured-bass fine detail.** `partial` lumps all inversion/extension/figured-bass
differences into one "agreement" bucket (10.1%, S6) [doc, dossier §2]. Cadential function (PAC/HC), the
cadential-6-4 *as a label* (vs the literal `I64`), and figured-bass inversion correctness are **not
separable** in the current buckets. These are Stage-6 outputs with no metric slot yet; the contract
(§3.1) must reserve one.

---

## §2 — The granularity-robust scoring unit (the genuine new design work)

### 2.1 The problem, stated precisely

The 2.2-i ~7× gap and the 3.1b double-digit per-tick swing are the **same artifact seen twice**: the
metric's denominator is the *segmentation*, and segmentation is a free variable. Two failure modes:

1. **Denominator shift** [probe, 2.2-i §3.5]: finer regions → more aligned pairs → `rn_agree%` falls
   even though `root_agree` *count* is flat. "Improved consistency" can be manufactured by growing the
   denominator (3.1b whole-score's only real win was P3↔P1 self-consistency, *not* accuracy [doc]).
2. **Coverage asymmetry**: one coarse region spanning a barline gets **one** comparison (to the
   beat it happens to agree with); two measure-aligned regions get **a comparison per beat** and
   surface the disagreement the coarse region masked (bwv10.7 m20: OFF `Bb/C` pairs to an agreeing
   pre-downbeat DCML row; ON splits at the barline and the downbeat half aligns to `iv` → error
   surfaces, **root unchanged** [probe, 2.2-i §3.2]).

A metric that "scores whatever regions exist" therefore reports a number that depends on a choice
(batch vs section vs sub-beat) that has nothing to do with analysis quality. **One of the numbers
lies** — and the user-visible one is the *finer* one (the status-bar resolves the chord at the clicked
note; the chord track shows the broad region [doc, 3.1b Result 3 / dossier §1.4]).

### 2.2 The design: a fixed-grid, duration-weighted unit

**Scoring unit = a fixed time grid, each cell weighted by its duration, scored by point-sampling both
sides.** Concretely:

- **Grid:** the **tactus/sub-beat tick lattice** — every distinct onset tick present in *either* our
  output or the DCML annotation, within the piece's tick span. (Equivalently: the union of region
  boundaries from both sides, which yields a set of half-open cells `[t_i, t_{i+1})` over which **both**
  sides are constant by construction.) This is segmentation-**invariant**: refining either side's
  regions adds boundaries that split a cell into two cells *carrying the same two labels*, so the
  duration-weighted score is unchanged.
- **Per-cell verdict:** sample our active region at `t_i` and the DCML active row at `t_i` (both via
  the existing `align_dcml_regions` time-overlap substrate, evaluated at a point rather than a region —
  §2.3), classify with the **reused `classify_pair` buckets**, weight the verdict by `(t_{i+1}-t_i)`.
- **Reported number:** **duration-weighted bucket fractions** = `Σ dur(cell in bucket) / Σ dur(all
  cells)`. This is the fraction of *musical time* (not of *regions*) in each bucket — the quantity a
  listener/user actually experiences.

**Why this kills both failure modes:**

- **Denominator shift → gone.** Total weight = total scored duration, which is fixed by the piece, not
  by either side's segmentation. Splitting a region cannot change `Σ dur`. (Contrast the current
  region-count denominator, which *is* the segmentation.)
- **Coverage asymmetry → gone.** A barline-spanning coarse region is sampled at every grid tick it
  covers; if it disagrees with DCML on the downbeat half, that half's *duration* is charged as
  `root_err` whether or not our segmentation drew a boundary there. The bwv10.7 error surfaces under
  batch *and* section because the **time** under the wrong label is the same in both.

**The metric explicitly reports the granularity it is invariant to:** it is duration-exact, so there is
no "batch number" vs "section number" — there is one number, the time-weighted one. (If a coarser
*reporting* view is wanted for the chord-track product question, it is a **presentation** rollup of the
same cells, not a different metric.)

### 2.3 Reuse the substrate; the unit is the only new piece

`align_dcml_regions(mode="time-overlap")` already converts DCML `(measure, beat)` onsets to ticks and
treats each DCML row as spanning `[start_tick, next_row.start_tick)` [code `compare_analyses:377-393,
516-532`]. The grid unit needs the **same span arithmetic evaluated as point-membership at each grid
tick** instead of best-overlap per region. That is a thin new function over existing helpers
(`_dcml_time_spans`, the tick anchoring) — **no production/C++ change** [stop-condition check: the unit
is prototypable purely in `tools/` Python over existing `.ours.json` + WiR/TSV; it does not require
batch_analyze to emit anything new]. The lenient-OR 50% rule is a *region-pair* concept and is simply
not used by the point-sampled unit (a point is in exactly one span on each side).

### 2.4 What it costs to prototype

- Per-piece: cheap (one pass over the merged boundary set).
- Corpus-wide: needs the `.ours.json` already on disk (`tools/corpus/default/` for Bach, the
  cross-corpus dirs for the rest) — **no regen** for batch granularity. The dossier's §4.1 caveat (a
  *Default-section* corpus is not pre-generated) **dissolves** under this design: the duration-weighted
  unit makes the section corpus unnecessary, because it scores the same time-mass regardless of which
  segmentation produced the `.ours.json`. That is the point — it removes the granularity fork instead
  of measuring both forks.

> **Open design question (OQ-G1):** sample at onset ticks only, or integrate over the cell? Onset-tick
> point-sampling with duration weight is exact when both sides are piecewise-constant between grid
> boundaries (they are, by construction of the grid as the union of boundaries) — so the two are
> identical here. Flagged only so the ratifier confirms the grid = union-of-boundaries choice (vs a
> fixed metrical grid e.g. every 16th, which would *approximate* and reintroduce a tunable). **Recommend
> union-of-boundaries (exact).**

---

## §3 — The functional-label chicken-and-egg

### 3.1 The label-vocabulary CONTRACT (Stage-6 output spec = metric input spec)

Stage 6 will emit functional labels; the metric must compare them to DCML's Roman numerals. The two
specs are **the same object**, co-designed once here. The contract has three columns: the **label
class**, **how Stage 6 emits it** (our RN string), and **how DCML writes it** (already parsed by
`dcml_parser` — the table records what the metric must match against).

| Class | Stage-6 emits (ours) | DCML/WiR writes | Metric status today | Action |
|---|---|---|---|---|
| **Diatonic triad/7th** | `V`, `ii6`, `V7`, `viio6` | same | ✅ scored (exact/partial) | reuse |
| **Secondary dominant / applied** | `V/V`, `V7/V`, `viio/V`, `V65/IV` | `V/V`, `vii/o7/V`, `V65/IV` | ✅ **already credited if emitted** [probe §1.3b] | **emit it** (Stage 6); metric reuse |
| **Cadential 6-4** | a *label* distinct from literal `I64` (e.g. `Cad64` or `V(64)`) | DCML `I64` within a `Cad`-marked context / WiR `Cad.` token | ⚠ today both read as `I64`/`I` → `root_err` vs the dominant root | **define the canonical token** + teach metric the Cad context |
| **Augmented sixth** | `It6`, `Fr43`, `Ger65` | `It6`, `Fr`, `Ger65` | ❌ `It6`→Maj-tonic (wrong root); `Ger`/`Fr`→`?` root-only [F-2] | **fix `dcml_parser` + `extract_quality`** (BUILD §3.1a) |
| **Neapolitan** | `N6` or `bII6` | `N6` / `bII6` | ❌ `N6`→`?` root-only | **fix parser** (BUILD) |
| **Modal mixture** | borrowed-degree RN (e.g. `bVI`, `iv` in major) | same (DCML accidental-prefixed degree) | ⚠ root scored; the *mixture* status is not a separate axis | reuse root/quality; no new axis needed |
| **Tonicization vs modulation** | KeyArea span boundary (Stage 4.2) drives whether a region is `V/x` (tonicized) or a local-key `V` (modulated) | DCML `localkey` ≠ `globalkey` flag [code `dcml_parser` resolves both] | ⚠ measurable as **S1 movement out of key_disagree** | reuse buckets + a key-context sub-tag (§3.2) |

**BUILD item §3.1a (the metric-side parser fix the contract forces):** extend `dcml_parser._compute_root_pc`
/ `compare_rn.split_rn` / `extract_quality` to parse `It/Fr/Ger/N` to their correct roots and qualities
(aug6 → the actual bass/root the chord targets; `N6`→`bII`). This is the same F-2 fix the 2.2-i dossier
scoped (apply `It6`; it left `Ger`/`Fr`/`N` as honest-non-scoring) — the contract now **requires the
full fix**, because Stage 6 will *emit* these and the metric must score them, not fall back to root-only.
Bundle it with the contract, not before (it is gate-neutral on Bach [probe, 2.2-i §4]).

> **OQ-L1 (a genuine Stage-6 fork, do not guess):** the **cadential-6-4 token**. Three options — (a)
> emit literal `I64` and let the metric treat it as agreement-with-DCML-`I64` (loses the functional
> claim that it *is* a dominant); (b) emit a dominant-rooted label `V(64)` (matches DCML's *function*
> but mismatches DCML's *notation* `I64` unless the metric maps them); (c) emit a dedicated `Cad64`
> token and teach the metric a `Cad64 ≡ {DCML I64 in cadential context}` equivalence. This decides both
> Stage-6's output *and* whether cadential-6-4 lands in `exact` or `root_err`. **It cannot be pinned
> without a Stage-6 design decision** — surfaced as an OQ, not guessed.
>
> **OQ-L2:** secondary-dominant **notation normalization** — DCML writes `vii/o7/V` (slashed-o
> half-dim), WiR writes `viio7/V`; our `normalise_rn` would need a canonical form for both sides.
> Low-risk (string normalization, same family as the existing `%`→`ø` rule) but must be in the
> contract so both sides agree.

### 3.2 The incremental measurability ladder

The whole point of designing the metric first is that **Stage 4 can be measured before Stage 6's
vocabulary exists, and Stage 6 is measured class-by-class as it ships** — no big-bang label set blocks
anything. The ladder, rung by rung (each rung scorable against DCML with the tools named):

| Rung | What it measures | Scorable with | Available |
|---|---|---|---|
| **L0** | root (`root_err`), root+coarse-quality (`quality_disagree`), key/degree (`key_disagree`) | `compare_rn` buckets, **TODAY**, no new labels | ✅ now (needs only §1.2 `--wir-bach` + §2 grid) |
| **L1 — Stage 4** | **key correctness**: the `key_disagree, ≠global` half (S2, 10.2%) shrinking; KeyArea spans matching DCML `localkey≠globalkey` regions | L0 buckets + a **key-context sub-tag** on `key_disagree` (split `=global≠local` vs `≠global`) — the dossier's `/c/tmp/key_confound.py` cross-tab, promoted to a committed `--key-breakdown` [probe, dossier §1.5] | ✅ measurable the moment Stage 4 ships; **needs no Stage-6 label** |
| **L2 — Stage 6 secondaries** | **tonicization**: S1 (17.7%) migrating `key_disagree → exact/partial` as the pipeline emits `V/V` | reuse (comparator already credits §1.3b); + the contract's `/x` normalization (OQ-L2) | unlocks when Stage 6 emits secondaries |
| **L3 — Stage 6 cadence/aug6/N** | cadential-6-4, aug6, Neapolitan correctness | the contract's parser fixes (§3.1a) + the cadence-token decision (OQ-L1) | unlocks per class as Stage 6 emits each |
| **L4 — figured bass** | inversion/extension detail inside `partial` (S6, 10.1%) | a sub-split of `partial` by inversion figure | last; lowest yield |

**The ladder is the resolution of "metric first vs Stage 6 first":** L0–L1 are pure-reuse + the two
BUILD items (§1.2, §2) and are **strictly metric-first** (they gate Stage 4's measurability and need no
functional labels). L2–L3 are **co-designed** with Stage 6 because the label *is* the Stage-6 output —
the metric cannot be "finished" ahead of Stage 6 for those rungs, only *specified* (the contract §3.1).

### 3.3 The Stage-5 objective function

Stage 5 fits the ~30 emission/transition constants against DCML [doc, roadmap 5.1; arch-review §A.2].
Its objective must be **DCML-only and granularity-robust** by Tasks 1–2. Concretely:

- **Optimand:** maximize duration-weighted `rn_agree` (= `exact + partial` time-fraction, §2.2) on a
  **held-out** DCML split, with the bucket structure as a multi-objective decomposition (so a fit that
  trades `root_err`↓ for `quality_disagree`↑ is visible, not hidden in a scalar).
- **Granularity:** the §2 fixed-grid duration-weighted unit — **not** the region-count denominator
  (which the fitter could game by changing segmentation; the 2.2-i artifact is exactly that hazard).
- **DCML-only:** **no** `three_way_classify` / music21 filter. The fitting gate is the human annotation,
  full stop (corpus audit C2 mandate: music21 is an algorithm, not ground truth; the filter discards
  95.2% of the root-error mass [doc, dossier §1.2]). The music21 three-way may still be *reported*
  alongside (to size the filter's effect, as the dossier did) but never *optimized against*.
- **Coverage honesty:** report the 326/353 WiR denominator and per-corpus breakdown; never aggregate a
  single number that hides which corpus moved (the cross-corpus root_err ranges corelli 55%→dvorak 41%
  [doc, dossier §1.4] — a scalar would let a fit win on chorales while losing on Corelli).
- **Weighting across rungs:** fit L0 (root/quality/key-degree) first — it is fully available and
  regression-bounded; bring L2–L3 functional rungs into the objective only as Stage 6 emits them
  (otherwise the fitter optimizes a constant — the unemitted-secondary residual S1 — it cannot move).

---

## §4 — Recommendation: build-vs-reuse + ordering + open questions

### 4.1 Build vs reuse (consolidated)

**REUSE (no change):**
- `compare_rn.classify_pair` buckets + the split invariant [pinned, 54 tests].
- `compare_analyses.align_dcml_regions` time-overlap span arithmetic [pinned].
- `dcml_parser` DCML-TSV + WiR-rntxt parse, root_pc resolution incl. `relativeroot` [pinned].

**BUILD (new, in priority order):**
1. **`compare_rn --wir-bach DIR`** — promote the dossier's Bach-WiR wiring to a committed mode (~20
   lines orchestration over pinned functions; closes the 326-chorale coverage hole). *Metric-first;
   needed for L0 on the most-trusted corpus.*
2. **The fixed-grid duration-weighted unit** (§2) — the one genuinely new metric primitive; removes the
   ~7× batch/section fork; prototypable in `tools/` Python, **no production change**. *Metric-first;
   gates Stage 4's and Stage 5's measurability.*
3. **The key-context sub-tag** (§3.2 L1, `--key-breakdown`) — promote `key_confound.py`'s cross-tab;
   makes Stage 4 measurable (S1 vs S2 split). *Ships with / just after Stage 4.*
4. **The label-vocabulary contract + parser fixes** (§3.1, §3.1a) — the F-2 aug6/Neapolitan parse fix
   + secondary `/x` normalization + the cadence-token decision (OQ-L1). *Co-designed with Stage 6;
   each class lands as Stage 6 emits it.*

### 4.2 Does "metric first" stand, or interleave?

**It interleaves — and the re-grounded order is confirmed with one refinement.** The headroom dossier
and roadmap put the metric "first in the back half" [doc, roadmap §⚠ re-grounding: "the DCML-only +
granularity-robust METRIC is the immediate next instrument… it gates Stage 4's AND Stage 6's
measurability"]. This investigation **confirms** that for **L0–L1** (BUILD items 1–3): they are pure
metric work, need no functional labels, and unblock Stage 4 — do them first. But it **refines** the
framing for **L2–L3**: because `classify_pair` *already credits* a correctly-emitted secondary
(§1.3b), the functional axis is **not blocked on a new metric** — it is blocked on **emission**. The
metric work there is the **contract** (§3.1), which is *simultaneously* Stage-6's output spec. So:

> **Recommended order (confirms the roadmap, sharpened):**
> **(i)** build the granularity-robust unit + `--wir-bach` + key-context sub-tag (BUILD 1–3) — strictly
> first, fully metric, unblocks measuring Stage 4; **(ii)** ratify the label-vocabulary contract (§3.1)
> as a **joint** Stage-6-output / metric-input artifact *before* Stage 6 codes, resolving OQ-L1/L2;
> **(iii)** Stage 4 (key path) — measured immediately on rung L1; **(iv)** Stage 6 co-developed,
> measured class-by-class on rungs L2–L3 as each label ships; **(v)** Stage 5 fits last on the §3.3
> objective. Beam stays shelved [doc, dossier §3.3 trigger].

The single substantive adjustment to the prior plan: **the contract (§3.1) is not "metric work that
precedes Stage 6" — it is a Stage-6 design artifact co-ratified with the metric.** That is the
chicken-and-egg, resolved: you do not build a functional-precision metric ahead of Stage 6; you
**co-design the label vocabulary** (one table, §3.1), which lets the *already-capable* comparator score
each functional class the moment Stage 6 emits it, while L0–L1 (which need no labels) proceed strictly
metric-first.

### 4.3 Open questions for the ratifier (do not guess — these are forks)

- **OQ-G1** (§2.4): grid = union-of-region-boundaries (exact, recommended) vs a fixed metrical grid
  (approximate, introduces a tunable). *Metric-internal; recommend union-of-boundaries.*
- **OQ-L1** (§3.1): the cadential-6-4 token — `I64` vs `V(64)` vs dedicated `Cad64` + metric
  equivalence. **A Stage-6 output-design fork**; decides whether cadential-6-4 scores as `exact` or
  `root_err`. Cannot be pinned without Stage-6 design.
- **OQ-L2** (§3.1): secondary/applied-chord notation normalization (`vii/o7/V` vs `viio7/V`) — canonical
  form for both sides. Low-risk; must be in the contract.
- **OQ-C1** (§3.3): the held-out split for Stage 5 — which corpora are train vs held-out, given only
  326 Bach + the cross-corpus set, and the C5 audit note that we own unused human annotation
  (en_fr_suites 89, cpe_bach 66, WiR non-Bach ~700) [doc, corpus audit C5] that Stage 5 should pull in
  rather than fit-and-validate on the same narrow slice.
- **OQ-V1** (corpus audit C2): the **music21 version** that generated the `.music21.json` is recorded
  nowhere [doc]. The DCML-only metric does not depend on it, but the three-way *reporting* leg does —
  pin or freeze-by-fiat before any number derived from the three-way is quoted again.

### 4.4 Stop-condition disclosures (per the instruction)

- **compare_rn does NOT fail Task-1's assumption** — it confirms it (DCML-only, no music21 filter) and
  *exceeds* it: the comparator already credits correctly-emitted secondaries, which narrows the
  build/reuse split toward **reuse** on the functional axis (the new work is the contract + emission,
  not a new comparator). Reported per the stop condition (it changes the split: less to build than the
  "functional metric is genuinely new" framing assumed).
- **The granularity-robust unit does NOT require a production change to prototype** — it is `tools/`
  Python over existing `.ours.json`. Designed on paper here; the §2.4 note explains why it also
  *removes* the need for the Default-section corpus regen the dossier deferred.
- **The label-vocabulary contract cannot be fully pinned without Stage-6 forks** — OQ-L1 (cadence
  token) is surfaced as an open question, not guessed, exactly because it is a Stage-6 output-design
  decision entangled with the metric.

---

*Drafted by CC, 2026-06-13, base `a652dc1ba7`. Read-only: the only repo write is this draft. Probe
driver `/c/tmp/probe_secondary.py` (throwaway) reuses `compare_rn`/`dcml_parser` verbatim. Awaiting
Cowork/user ratification before any metric is built.*
