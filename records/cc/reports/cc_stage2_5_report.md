# CC Stage 2.5 report — P3 performance baseline (+ 2 riders)

*Session 6, 2026-06-12. Base: `6be2b30a96`. Measurement-only; zero production-code
changes. Claims tagged [probe] (measured) / [code] (read from source).*

This closes the last Stage-2 roadmap item. Deliverable: a committed, re-runnable
P3 profile harness + `docs/perf_p3_baseline.md`, plus the two riders.

---

## §1 — Harness design + placement rationale

### What was built  [code]

A **`DISABLED_` gtest**, `P3PerfBaseline.DISABLED_Sweep`, added to the existing
`pipeline_snapshot_tests` binary
(`src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp`, +`<chrono>`
+`<numeric>`). It:

1. Loads each of 4 perf-corpus scores **full / uncapped** (the snapshot corpus caps
   at 16 measures; perf must not).
2. Enumerates **every chord-bearing ChordRest tick** (deduped across staves/voices)
   — the ticks a user can actually click to fire a status-bar query.
3. Wall-times one `analyzeHarmonicContextAtTick(score, tick)` per tick (the exact
   public entry the status bar uses), **5 full sweeps** per score, reporting
   **median-of-5** for median/p95/max/sweep-total.
4. Counts P4 fallbacks (`!ctx.wasRegional`) once (deterministic across runs).
5. For the slowest tick of each score, if >100 ms, reconstructs one ±1-measure
   expansion iteration by separately timing `analyzeHarmonicRhythm` (Pass-0) vs
   `analyzeSection` — both public, both already used by this binary.

Output is a machine-readable `==== P3PERF BEGIN/END ====` block on stdout, which
`docs/perf_p3_baseline.md`'s tables are lifted from verbatim.

### Placement decision — the one reviewable choice

**Recommendation: keep it as a `DISABLED_` test in `pipeline_snapshot_tests`** (as
built). Reasoning:

| Option | Cost | Re-runnable @ Stage 3 | Verdict |
|---|---|---|---|
| **DISABLED_ test in `pipeline_snapshot_tests` (chosen)** | ~0 build wiring — reuses the proven IoC + `ScoreRW` env that already loads DCML scores and drives `analyzeHarmonicContextAtTick`; corpus root already = repo root | Yes (`--gtest_also_run_disabled_tests --gtest_filter='*P3Perf*'`) | **Cheapest honest; not throwaway; out of default CI** |
| New `perf_p3_tests` binary | +~140 lines duplicated CMake + `environment.cpp` mirror + `add_subdirectory` + ninja target | Yes | Cleaner separation, but the duplication buys nothing the `DISABLED_` gate doesn't already give |
| `tools/` binary (à la `batch_analyze`) | New target; **and** the documented Qt-access-violation-via-subprocess issue + Git-Bash-launch requirement (memory `feedback_batch_analyze_windows`) | Yes | Worst — reintroduces a solved IoC/launch problem |

`DISABLED_` is the standard gtest idiom for "committed, re-runnable, never runs in
the default sweep" — exactly the perf-test contract. **Cowork's call** per the
trust model; if a separate binary is preferred for hygiene I can split it (the body
is self-contained). **P1 commit awaits this confirmation.**

### Honesty notes

- Production untouched. The harness only calls public entries
  (`analyzeHarmonicContextAtTick`, `analyzeHarmonicRhythm`, `analyzeSection`).
- The attribution is a **reconstruction** (one ±1-measure iteration), not in-situ
  instrumentation — instrumenting inside
  `analyzeNoteHarmonicContextRegionallyInWindow` would be a production change.
- One cosmetic post-edit after the data run: removed a duplicate `GTEST_LOG_(INFO)`
  emission so the block prints once. Timing code byte-identical → numbers stand.

---

## §2 — Numbers + budget recommendation  [probe]

Machine: AMD Ryzen 9 3900X (12C/24T, 3.8 GHz), 32 GB, Windows 11, release
(`ninja_build_rel`), single-threaded. Median-of-5-sweeps per query (ms):

| Score | Measures | Queries | median | p95 | max | P4 |
|---|---:|---:|---:|---:|---:|---:|
| bach_chorale_001 | 23 | 80 | 85.7 | 176.6 | 179.0 | 0 |
| chopin_bi105_op30_1 | 54 | 248 | 215.4 | 368.6 | 507.7 | 0 |
| bach_bwv806_prelude | 37 | 462 | 33.3 | 1081.8 | 3143.8 | 0 |
| mozart_k279_1 | 100 | 1441 | 105.9 | 2754.4 | 7014.9 | 0 |

**Headlines:**

1. **P3 is uncached per-query re-analysis and it is expensive** — median tens to
   low-hundreds of ms; p95 up to 2.75 s; worst single click ~7 s (Mozart m68).
2. **Pass-0 (`analyzeHarmonicRhythm`) is ~98–99.9% of cost; `analyzeSection`
   < 0.3 ms** (attribution table in the doc). The decoder restructures the
   sub-millisecond `analyzeSection` layer — not the dominant cost.
3. **Heavy-tailed; the tail grows with score length** (p95 176→369→1082→2754 ms),
   driven by the up-to-9× expanding-window retry. Median tracks local note density
   /convergence, not raw size (dense chorale 86 ms > sparse-tick bwv806 33 ms).

**Budget recommendation (numbers in hand):** Stage-3 beam-1 must keep per-query
**p95 ≤ observed p95 × 1.10** — a tight 10% factor justified because the decoder
lives in the < 0.3 ms `analyzeSection` layer, while the whole expensive Pass-0
windowing is upstream and unchanged. Ceilings: chorale ≤194.3, chopin ≤405.4,
bwv806 ≤1189.9, mozart ≤3029.9 ms. Equivalently: the decoder's own added cost
< 1 ms/region. Re-run this harness at Stage 3.1 alongside the 0/353 byte-identity
gate.

**Separate pre-existing concern (flagged, not a Stage-3 item):** P3 is already
outside any interactive budget purely from uncached Pass-0 × window expansion —
its own optimization track (caching / incremental / expansion cap), quantified
here so it is not later mistaken for decoder regression.

---

## §3 — P4-fallback counts  [probe]

**0 P4 fallbacks across all 2231 queries** (80+248+462+1441). On these four
batch-loadable scores the regional (P3) path never empties; the status-bar entry
never reached `analyzeHarmonicContextLocallyAtTick`. This closes the ARCHITECTURE
§1.3 "P4-fallback rate unknown" honestly **for batch-loadable scores**: the rate is
**0 on this corpus**. Not provably 0 in general — P4 still exists for ticks with no
`tick2measure`/segment and possibly for score shapes absent here.

---

## §4 — Test-count reconciliation (Rider 1)  [probe/code]

**Outcome: explanation-only. No discovery bug. No lost pinned tests.** The arithmetic
resolves cleanly; the "67" was a single-file under-count.

### Evidence

`python -m unittest discover -s tools/tests -p 'test_*.py'` → **`Ran 70 tests ... OK`**.
All discovered, all pass. Per file (current, HEAD `6be2b30a96`):

| File | Tests |
|---|---:|
| `tools/tests/test_metric_scripts.py` | 67 |
| `tools/tests/test_snapshot_sources.py` | 3 |
| **Total** | **70** |

`def test` counts across commits (`git show <commit>:<file> | grep -c 'def test'`):

| Commit | `test_metric_scripts.py` | `test_snapshot_sources.py` | two-file total |
|---|---:|---:|---:|
| `001b15df2d` (2.3 final) | 65 | 3 | **68** |
| `1a08e96d8a` (2.4 V2) | 65 | 3 | 68 |
| `6be2b30a96` (2.4 V4, HEAD) | **67** | 3 | **70** |

The V4 commit `6be2b30a96` diff on `test_metric_scripts.py`: **+2 added, −0 removed**
— the two net-new tests are `test_canonical_five_presets_present` and
`test_default_preset_is_accepted` (the `--preset Default` follow-through). No
consolidation, no removal.

### Conclusion

- **2.3's "68/68"** was the correct **two-file** suite total (65 + 3).
- **2.4's "67/67"** quoted **only `test_metric_scripts.py`** (which went 65→67 in
  V4), silently dropping `test_snapshot_sources.py`'s 3 tests.
- The instruction's `68 + 2 = 70 ≠ 67` resolves as: **70 IS the correct total**;
  67 was the under-count. The full suite grew 68 → 70 (the expected +2), and the 3
  snapshot-source tests were never lost — `unittest discover` finds all 70 and they
  pass.

No discovery/skip artifact exists; no fix needed. Per the instruction ("if
explanation-only, it goes in the report"), there is **no Rider-1 commit**.

---

## §5 — Unknowns / caveats

- [probe-limitation] **One binary invocation** (5 internal warm sweeps/score), not 3
  separate process launches — cross-process variance not isolated. One Mozart sweep
  alone is ~16 min (944 s); 3 launches ≈ 4+ h. The 5 internal warm sweeps are the
  realistic in-app condition (score loaded, queried repeatedly). The reported
  per-line numbers already satisfy "≥3 runs, median-of-runs."
- [probe] P4-fallback = 0 is corpus-specific, not a general proof.
- [code→probe] Attribution is a single-iteration reconstruction over the ±1-measure
  window (production untouched); it pins the Pass-0 ≫ analyzeSection ratio, not the
  full per-query expansion multiplier (visible in the median-vs-attribution gap).
- [probe] Absolute ms are machine/build-specific; the Stage-3 gate is the **ratio**
  (×1.10), which is machine-independent. Re-run on the same machine for apples-to-
  apples.
- [probe] Post-cosmetic-edit (duplicate-log removal) verified green: rebuild clean,
  snapshot suite **11/11 PASSED** (90.7 s). Timing code is byte-identical to the run
  that produced the numbers, so the data is unaffected regardless.

---

## Commits

- **P1** `perf: P3 status-bar baseline harness + docs/perf_p3_baseline.md (Stage 2.5)`
  — harness (`src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp`,
  modified) + `docs/perf_p3_baseline.md` (new). This report is untracked by repo
  convention (`/cc_*.md` is gitignored — like all prior `cc_stage2_*` reports).
  **Awaiting Cowork confirmation on placement** (§1).
- **P2** (Rider 2, direct) — `STATUS.md` + `COWORK_HANDOFF.md` +
  `docs/implementation_roadmap.md` bookkeeping flush, as they stand (coherence
  sanity-checked: roadmap 2.4 = Cowork's falsification edit; handoff/STATUS = 2.4
  closure + 2.5-next entries).
- **Rider 1** — explanation-only (§4), no commit.
