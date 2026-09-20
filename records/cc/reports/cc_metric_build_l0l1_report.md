# CC Metric Build — L0–L1 primitives (ratified precision-metric design)

*CC, 2026-06-13. Base `a652dc1ba7`. Tools-only, DCML-only, reuse-based — no
production/C++ change, no Stage-6 vocabulary. One commit held for Cowork.*

This run built the three metric-first primitives of `docs/precision_metric_design.md`
§4.1 BUILD 1–3 — the L0–L1 rungs that unblock measuring Stage 4. Every primitive is
orchestration (or one new scoring unit) over already-pinned functions; **no existing
metric bucket was redefined** (the 70 metric tests in `test_metric_scripts.py` are
green and untouched). All three primitives live in `tools/compare_rn.py`.

---

## §1 — Each primitive as built (reuse vs add)

### BUILD 1 — `compare_rn --wir-bach DIR` (the Bach WiR coverage mode)

**What it does.** For each `{stem}.ours.json` in DIR: resolve the When-in-Rome
`analysis.txt` via `dcml_parser.find_wir_file`, parse with `dcml_parser.parse_rntxt_file`,
align with `compare_analyses.align_dcml_regions`, classify with `compare_rn.classify_pair`.
Reports the **covered/total** coverage denominator explicitly. Parallel to
`--corpus`/`--cross-corpus`. A `--wir-base DIR` arg (default `tools/dcml/when_in_rome`)
points at the WiR root.

**Reuse vs add.** Pure orchestration — *zero* change to any metric definition (the
cc_stage1d "cross-corpus orchestration is not a metric definition" basis). The scoring
body was factored out of `score_piece` into a shared `score_regions(ours_regions,
dcml_regions)` so the TSV path and the WiR path run **byte-identical** scoring; only the
reference loader differs. New code: `score_corpus_wir`, the `WirCoverage` dataclass, the
shared `score_regions`. This closes the single largest coverage hole — Bach chorales have
no `harmonies.tsv`, so `--cross-corpus` structurally excludes the 326-chorale gate set;
`--wir-bach` is the only committed way to score it.

**Coverage honesty.** `--wir-bach tools/corpus/default` reports `WiR coverage: 326/353
ours files (92.4%) — 27 have no WiR annotation`. The 27 un-annotated scores are never
folded into a `/353` division.

### BUILD 2 — the granularity-robust duration-weighted unit (`--granularity-robust`)

**What it does** (design §2). Builds the grid = **union of region boundaries** from both
sides over the piece tick span → half-open cells `[t_i, t_{i+1})` on which both sides are
piecewise-constant by construction. Per cell: point-sample our active region and the DCML
active row at `t_i` (reusing `compare_analyses._dcml_time_spans` for the DCML tick spans —
the *same* span arithmetic `align_dcml_regions` uses), classify via the reused
`classify_pair`, weight by `(t_{i+1} − t_i)`. Reports **duration-weighted bucket
fractions** (`Σ dur(bucket) / Σ dur(scored)`), plus the unscored duration (gap/unaligned
cells) for honesty. New `--granularity-robust` flag/mode; the region-count buckets stay
available and unchanged — the unit is added **alongside**, not in place of.

**Reuse vs add.** The one genuinely new primitive. New code: `GridStats`,
`grid_score_regions` (the unit), `_active_index_at`, the TSV/WiR corpus wrappers,
`format_grid_report`. Everything it samples (`classify_pair`, `_dcml_time_spans`) is
reused. No production/C++ change — it is `tools/` Python over the existing `.ours.json`.

### BUILD 3 — `--key-breakdown` (the key-context sub-tag, L1 instrument for Stage 4)

**What it does.** Splits `key_disagree` into **S1 `=global ≠local`** (our key tonic+mode
== DCML *global* key → tonicization label-gap, the Stage-6 axis) vs **S2 `≠global`** (our
key ≠ DCML global → genuine key error, the Stage-4 axis), using the key fields both sides
already carry (our `key`; DCML `global_key`). Reports the split and the our-key
**parse-failure caveat** (the dossier's 2.4%), never hidden in a bucket.

**Reuse vs add.** The `_our_key_tonic` / `_dcml_key_tonic` parsers are ported **verbatim**
from the ratified `key_confound.py` driver (dossier §1.5). The split is a
sub-classification *within* the existing `key_disagree` bucket — `kd_eq_global +
kd_ne_global == key_disagree` by construction; the bucket itself is unchanged. New code:
the two key parsers, `key_disagree_subtag`, the `kd_*`/`keyparse_fail` counters on
`PieceStats`, `format_key_breakdown`. `keyparse_fail` (the 2.4%) is counted corpus-wide
over **all** matched pairs; the subset that lands inside `key_disagree` is reported as
falling into S2 ("the dossier's tonic✗ column").

---

## §2 — Test inventory (`tools/tests/test_metric_primitives_l0l1.py`, 21 tests)

The existing **70** metric tests (`test_metric_scripts.py` 67 + `test_snapshot_sources.py`
3) are **green and unchanged** — no bucket was redefined, so none needed editing. The new
tests, all `[hand-derived]`-grounded:

**Segmentation-invariance — the load-bearing property (design §2's justification).**
`TestGridSegmentationInvariance`: one underlying analysis (I over the first half, V over
the second) scored at a **coarse** (2-region) and a **fine** (4-region) segmentation must
yield the **same** duration-weighted fractions. Pinned: `test_coarse_equals_fine_fractions`
(exact 0.75 / root_err 0.25 in both); `test_invariance_is_nontrivial` (the fixture
exercises >1 bucket, so invariance is not vacuous); `test_total_scored_duration_is_
segmentation_independent` (Σ dur is fixed by the piece — the denominator-shift fix). **The
property holds**; the §2 design claim is confirmed, not falsified.

**Hand-derived known-input/known-output.** `TestGridHandDerived`: the coarse fixture's
cells + durations + expected weighted fractions are derived by hand in a comment block and
pinned (exact dur 1440, root_err dur 480, scored 1920 → 0.75/0.25).

**Edge cases.** `TestGridEdgeCases`: zero-length region contributes no boundary (no crash,
no double-count); coincident boundary not double-counted (Σ bucket == scored); gap in ours
coverage charged **unscored**, not mis-bucketed as an error; empty inputs return empty;
**determinism** (two runs identical).

**`--wir-bach` denominator.** `TestWirBachCoverage`: a 2-file fixture dir where only one
stem has a (stubbed) WiR `analysis.txt` → `covered=1 / total=2`, the CLI prints
`WiR coverage: 1/2` — never a silent `/2`-by-corpus-size. Plus the scored movement's
buckets (2 exact) and grid non-empty.

**`--key-breakdown` split.** `TestKeyBreakdownSplit`: three `key_disagree` pairs with our
key = {global, non-global, unparseable} → S1=1, S2=2, keyfail=1 (⊆ S2), corpus-wide
keyparse_fail=1; the S1+S2==key_disagree invariant. `TestKeyTonicHelpers` pins the two
ported parsers against the `key_confound` convention they reproduce.

---

## §3 — Reproduced dossier numbers via the committed modes

Run on `tools/corpus/default` (the batch `.ours.json` already on disk; no regen, no C++
build). These reproduce the headroom dossier (which used `/c/tmp` drivers over the same
pinned functions) and confirm the **committed** modes match.

**`--wir-bach tools/corpus/default` → the §1.2 decomposition (the root_err identity):**

| | committed `--wir-bach` | dossier §1.2 |
|---|---:|---:|
| movements (WiR-covered) | 326 / 353 | 326 |
| matched regions | 10 108 | 10 108 |
| exact | 3 254 | 3 254 |
| partial | 1 019 | 1 019 |
| key_disagree | 2 823 | 2 823 |
| quality_disagree | 306 | 306 |
| **root_err** | **2 706** | **2 706** |

`root_err = 2706` reproduced exactly (the dossier's load-bearing identity `2706 =
all_differ 2576 + music21_dcml_agree 130`).

**`--granularity-robust` → one number that does NOT swing batch↔section.** Run on the
existing Baroque batch (`tools/corpus/baroque`) vs section (`tools/corpus_ab/baroque_section`)
dirs, the same A/B the dossier §1.4 used:

| metric | batch | section | swing |
|---|---:|---:|---:|
| region-count `rn_agree` | 42.3% | 37.9% | **−4.4 pp** |
| region-count `root_err` | 26.7% (2700) | 33.5% (3747) | **+6.8 pp / +1047** |
| **duration-weighted `rn_agree`** | **35.0%** | **34.5%** | **−0.5 pp** |
| **duration-weighted `root_err`** | **38.8%** | **39.6%** | **+0.8 pp** |

The region-count numbers reproduce the dossier §1.4 batch/section A/B exactly (rn_agree
42.3→37.9, root_err 2700→3747 — the denominator-inflation artifact). The duration-weighted
unit removes ~88% of the swing (6.8 pp → 0.8 pp on root_err). The residual 0.8 pp is real:
batch and section are genuinely **different analyses** (section runs extra passes), not a
byte-identical re-segmentation, so a small true difference remains — exactly what the
design predicts (the *artifact* is gone; a real difference is allowed to show).

**`--key-breakdown` → the 63/37 S1/S2 split:**

| | committed `--key-breakdown` | dossier §1.5 |
|---|---:|---:|
| key_disagree total | 2 823 | 2 823 |
| **S1 `=global ≠local`** (Stage 6) | **1 791 (63.4%)** | **1 791 (63%)** |
| **S2 `≠global`** (Stage 4) | **1 032 (36.6%)** | **1 032 (37%)** |
| our-key parse failures | 239 / 10 108 (2.4%) | 239 / 10 108 (2.4%) |

All three primitives reproduce the dossier numbers from the committed modes (not the
throwaway drivers).

---

## §4 — Deviations / unknowns

1. **`grid_score_corpus_tsv` re-parses each piece** (vs threading grid through
   `score_corpus`). Chosen to keep the existing `score_corpus` / `--corpus` /
   `--cross-corpus` code path **byte-untouched** — the double-parse cost is paid only when
   `--granularity-robust` is passed. A deliberate clarity-over-micro-efficiency call; not a
   correctness issue.

2. **The grid is clamped to the ours tick extent** (`_dcml_time_spans` sets `piece_end =
   max ours end_tick`). A DCML span extending past our last region collapses; time
   DCML-covered but ours-uncovered is charged **unscored**, not mis-bucketed (pinned by
   `test_gap_in_ours_coverage_charged_unscored`). This is the reused span arithmetic's
   existing behavior, surfaced — not a new choice. Noted because my first hand-derivation
   of that edge case was wrong (expected 1440 unscored; correct is 480 — the V-span
   collapses); the code was right, the test expectation was corrected.

3. **Section-corpus is Baroque, not Default** — the granularity batch↔section
   demonstration uses `tools/corpus_ab/baroque_section` (the only pre-generated section
   corpus), matching the dossier §1.4 A/B. A Default-section corpus is not pre-generated
   (dossier §4.1); generating one is Stage-5 scope, not L0–L1. The non-swing property is
   preset-robust per 2.2-i, and the unit itself is preset-agnostic.

4. **No stop-condition fired.** No existing metric test needed a change (no bucket
   redefinition); the segmentation-invariance test **passes** (the §2 claim is correct);
   the committed modes **reproduce** the dossier numbers (no wiring divergence); and no
   label-vocabulary / functional-label work was started (that is Stage 6, explicitly out of
   scope here).

---

*Files changed: `tools/compare_rn.py` (the three primitives + shared `score_regions`),
`tools/tests/test_metric_primitives_l0l1.py` (new, 21 tests). 70 existing metric tests
unchanged. No corpus regen, no C++ build.*
