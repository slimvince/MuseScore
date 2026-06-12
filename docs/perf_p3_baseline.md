# P3 status-bar performance baseline (Stage 2.5)

*Written 2026-06-12 (session 6). Owner: CC (measurement) / Cowork (review).
Roadmap item 2.5 — the last Stage-2 item. Measurement-only; zero production-code
changes. Base commit: `6be2b30a96`.*

## Purpose

Capture the cost of the **P3 status-bar query path** NOW, before Stage 3's
decoder adds any decode cost. Two uses:

1. An honest **pre-decoder baseline** so the decoder's contribution is isolable.
2. The **budget envelope** for the decoder's quality-level-0 (beam-1 must remain
   "status-bar viable" — §2.14 ARCHITECTURE.md). This note states the regression
   gate in numbers.

## What P3 is

`analyzeHarmonicContextAtTick` (the public per-tick entry the status bar and the
chord-track writer call) → `analyzeHarmonicContextRegionallyAtTick` (P3). P3 runs
an **expanding-measure-window** loop ([`notationcomposingbridge.cpp:334`](../src/notation/internal/notationcomposingbridge.cpp#L334)):

- Initial window = current measure ±1 measure (`kInitialRegionalLookBehindMeasures`
  = `kInitialRegionalLookAheadMeasures` = 1).
- Each iteration re-runs **Pass-0** (`analyzeHarmonicRhythm`) + **`analyzeSection`**
  over the whole window, then compares the matched region's snapshot to the
  previous iteration.
- Converges when two consecutive iterations agree; otherwise expands ±1 measure
  each side and retries, up to `kMaxRegionalExpansionSteps = 8` (so up to **9**
  full window analyses per query, worst case, over an ever-growing window).
- No caching: every status-bar query re-analyzes from scratch.

If P3 yields no result it falls back to P4 (`analyzeHarmonicContextLocallyAtTick`).

## Harness

Placement: a **`DISABLED_` gtest** (`P3PerfBaseline.DISABLED_Sweep`) inside the
existing `pipeline_snapshot_tests` binary
([`pipeline_snapshot_tests.cpp`](../src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp)).
Rationale: cheapest honest, re-runnable, not throwaway — it reuses the proven
IoC + `ScoreRW` environment that already loads DCML scores and drives
`analyzeHarmonicContextAtTick`, and its corpus root is already the repo root, so
any DCML score is reachable. `DISABLED_` keeps noisy/slow timing out of the
default CI sweep. Re-run (here and again at Stage 3) with:

```
./pipeline_snapshot_tests.exe --gtest_also_run_disabled_tests --gtest_filter='*P3Perf*'
```

Per score the harness loads the **full** score (uncapped — the snapshot corpus
caps at 16 measures; this does not), enumerates **every chord-bearing ChordRest
tick** (deduped across staves/voices — the ticks a user can click), and wall-times
one `analyzeHarmonicContextAtTick` query per tick. It runs **5 full sweeps** per
score and reports the **median across the 5 sweeps** of each aggregate
(median/p95/max/sweep-total). P4-fallback counts are deterministic across runs and
measured once. p95 is nearest-rank.

## Machine / build context

- **CPU:** AMD Ryzen 9 3900X (12 cores / 24 threads, 3.8 GHz base). 32 GB RAM.
- **OS:** Windows 11.
- **Build:** release (`ninja_build_rel`), the standard project build.
- **Concurrency:** single-threaded. The bridge/batch analysis path has no
  threading; each query is one CPU core's work.
- **Run:** one binary invocation = 5 internal warm sweeps per score (the score is
  loaded once, then queried repeatedly — this mirrors a running app that has the
  score open and queries on each click). Cross-process variance not separately
  measured (see §Unknowns).

## The numbers  [probe]

Median-of-5-sweeps per query, in milliseconds. **P4 fallbacks = 0 on every score.**

| Score | Size class | Measures | Queries | median | p95 | max | sweep total |
|---|---|---:|---:|---:|---:|---:|---:|
| bach_chorale_001 | small SATB chorale | 23 | 80 | **85.7** | 176.6 | 179.0 | 8.0 s |
| chopin_bi105_op30_1 | mid piano (mazurka) | 54 | 248 | **215.4** | 368.6 | 507.7 | 53.5 s |
| bach_bwv806_prelude | contrapuntal keyboard | 37 | 462 | **33.3** | 1081.8 | 3143.8 | 62.6 s |
| mozart_k279_1 | largest (sonata mvt) | 100 | 1441 | **105.9** | 2754.4 | 7014.9 | 944.0 s |

**Per-query latency is tens of milliseconds at the median and up to ~7 seconds at
the worst single query.** A single status-bar click on Mozart K.279-1 m.68 takes
**~7 s**.

### Largest-window outliers (slowest tick per score)

| Score | slowest tick | measure | latency |
|---|---:|---:|---:|
| bach_chorale_001 | 18000 | 15 | 180 ms |
| chopin_bi105_op30_1 | 71280 | 50 | 510 ms |
| bach_bwv806_prelude | 92160 | 33 | 3207 ms |
| mozart_k279_1 | 130440 | 68 | 7053 ms |

## Scaling shape  [probe]

- **Median tracks per-query convergence + local note density, not raw score
  size.** The dense homophonic chorale sits at a tight ~86 ms (every ±1-measure
  window is 4-voice-dense and converges in ~1–2 iterations). The contrapuntal
  bwv806 prelude has a *lower* median (33 ms) despite being larger — many of its
  462 queries hit sparse/fast-converging windows.
- **The tail (p95 / max) grows strongly with score length.** p95 climbs
  176 → 369 → 1082 → 2754 ms and max 179 → 508 → 3144 → 7015 ms as scores get
  longer. Longer scores admit wider window expansion before convergence, and each
  expansion step re-runs Pass-0 over a bigger window. The distribution is
  **heavy-tailed**: most queries are near the median, a minority blow up by 1–2
  orders of magnitude.
- **Mechanism of the tail:** non-converging ticks drive the expansion loop toward
  its 9-iteration cap, each iteration a full `analyzeHarmonicRhythm` over a window
  that has grown to current ±9 measures. Cost ≈ Σ(Pass-0 over growing windows).

## P4-fallback frequency  [probe]

**0 P4 fallbacks across all 2231 queries** (80 + 248 + 462 + 1441). On these four
batch-loadable scores the regional (P3) path always produced a non-empty result;
P4 (`analyzeHarmonicContextLocallyAtTick`) was never exercised by the status-bar
entry. This closes the §1.3 "P4-fallback rate unknown" honestly for
batch-loadable scores: **on this corpus, P3 never empties.** (Caveat: P4 still
fires for ticks with no `tick2measure`/no segment, and possibly on score shapes
absent from this corpus — the rate is 0 *here*, not provably 0 in general.)

## Cost attribution: Pass-0 vs analyzeSection  [probe]

For the slowest tick of each score, the harness reconstructs **one** ±1-measure
expansion iteration (it cannot instrument *inside*
`analyzeNoteHarmonicContextRegionallyInWindow` without touching production, so it
re-calls the same two public functions over the same window):

| Score | Pass-0 (`analyzeHarmonicRhythm`) | `analyzeSection` | Pass-0 share |
|---|---:|---:|---:|
| bach_chorale_001 | 69.6 ms | 0.09 ms | 99.9% |
| chopin_bi105_op30_1 | 71.9 ms | 0.21 ms | 99.7% |
| bach_bwv806_prelude | 15.7 ms | 0.27 ms | 98.3% |
| mozart_k279_1 | 169.1 ms | 0.27 ms | 99.8% |

**Pass-0 (`analyzeHarmonicRhythm`) is ~98–99.9% of per-iteration cost;
`analyzeSection` is sub-millisecond and negligible.** The expensive work is the
harmonic-rhythm Pass-0 re-segmentation, multiplied by the expansion-loop iteration
count. `analyzeSection` — the layer Stage 3's decoder restructures — is in the
*cheap* part.

## Stage-3 budget recommendation

The decoder (Stage 3.1, beam-1) restructures the greedy argmax that lives **inside
`analyzeSection`**, over the same oracle output. `analyzeSection` currently costs
**< 0.3 ms per window** (above), i.e. < 0.3% of a P3 query. The decoder therefore
has no business adding more than measurement noise to per-query latency: the entire
expensive path (Pass-0 windowing × expansion) is **upstream of the decoder and
unchanged by Stage 3**.

**Recommended Stage-3 regression gate: beam-1 per-query p95 must stay within
`observed p95 × 1.10`** (a deliberately tight 10% factor, because the decoder
operates in the sub-millisecond `analyzeSection` layer, not the dominant Pass-0
layer). With the numbers in hand, the per-score p95 ceilings are:

| Score | observed p95 | beam-1 p95 ceiling (×1.10) |
|---|---:|---:|
| bach_chorale_001 | 176.6 ms | **194.3 ms** |
| chopin_bi105_op30_1 | 368.6 ms | **405.4 ms** |
| bach_bwv806_prelude | 1081.8 ms | **1189.9 ms** |
| mozart_k279_1 | 2754.4 ms | **3029.9 ms** |

Equivalently and more diagnostically: the decoder's **own added cost** (the part
replacing `analyzeSection`'s argmax) must stay **< 1 ms per region** — it is
replacing a < 0.3 ms operation. Re-run this harness at Stage 3.1 and confirm both:
(a) per-query p95 within ×1.10, and (b) the byte-identity gate (0/353 corpus diff)
the decoder skeleton already owes.

**Separate, pre-existing concern (NOT a Stage-3 item):** the P3 path is already far
outside any interactive budget — median 86–215 ms, p95 up to 2.75 s, worst single
click ~7 s — entirely because of uncached per-query Pass-0 re-analysis × up-to-9×
window expansion. This is an existing architecture cost, not introduced by the
decoder; it warrants its own optimization track (query caching / incremental
re-analysis / capping expansion). Quantified here so it is not mistaken for decoder
regression later.

## STATUS-ready summary line

> **Stage 2.5 (P3 profile) [probe]:** P3 status-bar query is uncached per-tick
> re-analysis; median 86–215 ms, p95 up to 2.75 s, worst ~7 s (Mozart K279-1 m68),
> heavy-tailed and growing with score length. **Pass-0 `analyzeHarmonicRhythm` is
> ~99% of cost; `analyzeSection` < 0.3 ms (negligible).** **P4 fallback = 0/2231
> queries** on the 4-score corpus. Stage-3 beam-1 budget: per-query p95 ≤ observed
> ×1.10 (decoder lives in the < 0.3 ms `analyzeSection` layer); P3's uncached-Pass-0
> cost is a separate pre-existing optimization track. Harness =
> `P3PerfBaseline.DISABLED_Sweep` in `pipeline_snapshot_tests`, re-runnable at
> Stage 3. Ryzen 9 3900X, release.

## Unknowns / caveats

- [probe-limitation] **One binary invocation** (5 internal warm sweeps per score),
  not 3 separate process launches — cross-process variance not isolated. Chosen
  because one full sweep of Mozart alone is ~16 min (944 s); 3 separate launches
  would be ~4+ h. The 5 internal sweeps control within-process warmup; the reported
  numbers are warm-cache, which is the realistic in-app condition.
- [probe] P4-fallback rate is 0 *on this corpus*, not provably 0 in general.
- [code→probe] The attribution single-iteration is a **reconstruction** over the
  initial ±1-measure window, not in-situ instrumentation (production untouched).
  It establishes the Pass-0 ≫ analyzeSection ratio, not the full per-query
  expansion multiplier; the multiplier is visible in the median-vs-attribution gap
  (e.g. chorale median 86 ms ≈ ~1.2 iterations of the 70 ms ±1 window).
- [probe] Absolute numbers are machine/build specific (Ryzen 9 3900X, release).
  The Stage-3 gate is the **ratio** (×1.10), which is machine-independent; re-run
  on the same machine for an apples-to-apples comparison.
