# Stage 3.1b — decode-once / query-many — implementation + answer-delta report

> Base commit `8e4bb4902d` (Stage 3.1 complete). **Status: implemented, measured,
> NOT committed — all commits held for Cowork ratification per the instruction.**
> Owner: CC. Companion design: `docs/decoder_design.md` §8/§9 + Q1/Q7.
>
> **RESOLVED (Cowork ratified option a, 2026-06-12): bounded-window cache shipped.**
> The original whole-score variant (§1–§6 below) was **measured, found not better
> (worse on Mozart 35/65), and SHELVED**; the two stop conditions it tripped
> (snapshots 0/11; DCML-worse) are moot. The cache was **rebuilt as a bounded-window
> memoization** (see **§R** — the binding outcome) that is **byte-identical** to today's
> P3: **snapshots 11/11 with no golden refresh**, zero answer-delta, all suites green, and
> the warm re-click win preserved (~4–5 orders faster). §1–§6 are retained as the record of
> the whole-score measurement (now Stage-5 evidence: `docs/p3_granularity_ab_3_1b.md`).
> **Still uncommitted — held for Cowork (commits B1′ + B2).**

---

## §1 — Plan (cache home, invalidation hook, P4 placement) + the snapshot finding

### 1.1 Cache home + lifecycle (Q1)

The "bridge" is a set of free functions in `mu::notation` (`notationcomposingbridge.cpp`);
there is no bridge object instance to hang a member cache on. The status-bar entry is
`harmonicAnnotation(note)` → `analyzeNoteHarmonicContextDetails(note)` →
`analyzeHarmonicContextAtTick(note->score(), …)` — the only handle the analysis layer
gets is a `const Score*`. So the cache is a **file-scope, process-wide, size-1
most-recently-used slot** (`g_decodeCache`) in `notationcomposingbridge.cpp`, keyed on
`(const Score*, changeToken, excludeStaves)`. Size-1 MRU fits the status-bar use case
(one score in focus); multiple open scores thrash but stay correct. Single-threaded (the
analysis path has no threading — `perf_p3_baseline.md` §Machine), so no mutex.

### 1.2 Invalidation hook found (the Task-1.1 hard-stop question — PASSED)

A reliable, const-reachable, monotonic per-edit token exists:

```
score->undoStack()->currentIndex()      // size_t, engraving/editing/undo.h:289
// Score::undoStack() : virtual UndoStack* undoStack() const;  (score.h:505)
// m_currentIndex advances on every committed undoable macro (undo.cpp m_nextState++)
```

Verified: `UndoStack::currentIndex() const` returns the monotically-advancing
`m_currentIndex`; `Score::undoStack()` is `const`. Already used for change-detection in
production (`playcounttext.cpp:50`). **Conservative MVP (mandated): ANY change to the
token invalidates the WHOLE cache** — a full whole-score re-decode on the next query. The
design's bounded-window re-decode (§8) is a documented follow-up, not 3.1b scope. If the
score has **no** reachable undo stack, `scoreChangeToken` returns `nullopt`, the cache is
marked invalid, and every query rebuilds fresh (no caching, no staleness risk, no
regression vs today). So there is no "no reliable signal → stop" condition: the signal
exists.

### 1.3 What the cached decode is, P3 granularity, and the P4 placement

- **The cached unit** is one whole-score Pass-0 (`analyzeHarmonicRhythm`) + `analyzeSection`
  over `[0, lastMeasure.endTick)` — `buildWholeScoreSection()`. This yields the per-region
  committed identities + the path state (each region's `temporalExtensions` snapshot). P3
  serves **section regions** (the user-facing granularity, 2.2-i dossier).
- **P3 = cache lookup.** The new `analyzeHarmonicContextAtTick` gets the cached whole-score
  section and calls `buildRegionalContextFromSection(tick, section, …)` — the *same*
  region-match-and-construct code the windowed path used, factored out so the ONLY
  difference between old and new is **which section** is matched (a ±window section vs the
  whole-score section). This isolates the answer-delta to exactly one variable and
  guarantees byte-identical context construction when the matched region agrees.
- **P4 placement.** P4 (`analyzeHarmonicContextLocallyAtTick`) is kept on its **cold
  `findTemporalContext` path** for 3.1b. Rationale (conservative MVP, mirroring the
  whole-cache-invalidation mandate): P4 fires **0/2231** on the perf corpus, so the D-P4
  "consume decoded path state" closure would be a live behaviour change on a path with
  **zero corpus coverage** — unmeasurable and unverifiable. The cache *enables* the D-P4
  closure (the decoded path is now available at the orchestrator), but wiring it is
  **deferred and flagged for ratification** (§6) rather than shipped blind. The raw
  `analyzeHarmonicContextLocallyAtTick` stays byte-identical for the snapshot's direct P4
  calls regardless.

### 1.4 ⚠ Snapshot-harness wiring — a correction to the instruction's premise

The instruction (Task 1.3) states "the pipeline-snapshot harness calls the raw functions
and must stay byte-identical." **This is only half true, and the half that is false is
load-bearing:**

- **P4 snapshot** (`buildTickLocalArray`) calls the raw `analyzeHarmonicContextLocallyAtTick`
  directly → unaffected by the cache → byte-identical. ✔
- **P3 snapshot** (`buildTickRegionalArray`, line 448) calls the **orchestrator**
  `analyzeHarmonicContextAtTick` — exactly the function the cache now rewires. ✘

Therefore the P3 snapshot **does** go through the whole-score cache. The snapshot 11/11
gate can only stay green **iff the whole-score answer equals the windowed answer at every
sampled P3 tick on the 10 snapshot scores** — which is precisely the answer-delta this
stage is built to measure. The "snapshots stay untouched by construction" assumption does
not hold; whether they stay green is an *empirical* result reported in §4, and a non-zero
P3 snapshot diff is the answer-delta surfacing on the snapshot corpus (handled per the
stop condition: report, do not refresh goldens, do not commit).

---

## §2 — Implementation map

All changes are **notation-side only** — no composing-module file is touched, so the batch
corpus path (`batch_analyze` → `analyzeRegions`, which never goes through the bridge) is
**provably untouched**. Per Task 4 that downgrades the corpus gate to a Baroque spot-check.

**`src/notation/internal/notationcomposingbridge.cpp`**
- `+#include "engraving/editing/undo.h"` (UndoStack::currentIndex).
- `buildRegionalContextFromSection(tick, section, outContext)` — factored out of the old
  `analyzeNoteHarmonicContextRegionallyInWindow` body (the region match + context build,
  verbatim). Returns false when no region matches.
- `buildWholeScoreSection(sc, excludeStaves)` — whole-score Pass-0 + `analyzeSection`.
- `WholeScoreDecodeCache` struct + `g_decodeCache` (size-1 MRU) + `scoreChangeToken()` +
  `cachedWholeScoreSection()` (the hit/miss + rebuild logic).
- `analyzeNoteHarmonicContextRegionallyInWindow` reduced to: build window section →
  `buildRegionalContextFromSection` → format symbol/roman/nashville for convergence.
  (Behaviour unchanged; it now shares the construction helper.)
- `analyzeHarmonicContextAtTick` (production) rewired: P3 = `cachedWholeScoreSection` +
  `buildRegionalContextFromSection`; P4 fallback unchanged (cold).
- New non-production entries: `analyzeHarmonicContextAtTickWindowed` (the verbatim old
  orchestrator, for the A/B), `analyzeHarmonicContextAtTickWholeScoreUncached`
  (cache-bypassed, cold-equals-fresh reference), `clearHarmonicDecodeCacheForTesting`,
  `harmonicDecodeCacheBuildCountForTesting`.

**`src/notation/internal/notationcomposingbridge.h`** — declares the four new entries
(documented as A/B + test instrumentation, not the production path).

**`src/notation/tests/notationdecodecache_tests.cpp`** (new) + CMakeLists — cache unit
tests: WarmEqualsCold, OneBuildServesAllTicks, ColdEqualsFreshAtEveryTick,
InvalidationOnEdit, DistinctScoresDoNotShareCache.

**`src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp`** — two new
DISABLED harnesses: `Stage31bAnswerDelta.DISABLED_Sweep` (the §3 centerpiece) and
`Stage31bPerf.DISABLED_ColdWarm` (the §4 cold/warm perf).

---

## §3 — The answer-delta (window vs warm cache) — RATIFICATION CENTERPIECE

**Headline: the answer-delta is LARGE on contrapuntal/large scores, and the whole-score
reading is NOT cleanly more correct than the window reading — on the largest score
(Mozart) it is measurably WORSE against DCML.** This trips the instruction's stop
condition ("answer-delta dominated by genuinely-new readings that are DCML-wrong →
whole-score P3 is WORSE — report, don't rationalize"). **Recommendation: do NOT ship
whole-score-cached P3 as-is; see §6 for the bounded-window alternative that keeps the
perf win with zero answer-delta.**

### 3.1 Per-tick displayed-result delta (`Stage31bAnswerDelta.DISABLED_Sweep`)

OLD = `analyzeHarmonicContextAtTickWindowed` (expanding ±measure window, today's live
path). NEW = `analyzeHarmonicContextAtTick` (whole-score decode cache). Counts = ticks
whose **displayed** field differs.

| Score | ticks | rootDiff | qualDiff | bassDiff | keyDiff | old/newEmpty | old/newP4 |
|---|---:|---:|---:|---:|---:|---:|---:|
| bach_chorale_001 (small homophonic) | 80 | **0** | 0 | 0 | 0 | 0/0 | 0/0 |
| chopin_bi105_op30_1 (mazurka) | 248 | **0** | 0 | 0 | **5** | 0/0 | 0/0 |
| bach_bwv806_prelude (contrapuntal) | 462 | **185 (40%)** | 286 | 214 | 94 | 0/0 | 0/0 |
| mozart_k279_1 (sonata) | 1441 | **460 (32%)** | 441 | 449 | 119 | 0/0 | 0/0 |

Pattern: the delta is **zero on small/homophonic music and huge on
contrapuntal/large music**. P4 fires 0× on both paths (confirms the P4-deferral has zero
corpus impact; D-P4 untested by construction).

### 3.2 Mechanism — whole-score = coarse (batch/section) granularity; P3 now matches P1/P2

The window path analyses a ±1..±9-measure window and converges to a fine, local reading.
The whole-score Pass-0 + `analyzeSection` segments the *entire* score, producing **broad
harmonic-rhythm regions** — one chord label spanning several beats of figuration. Every
tick inside a broad region returns that region's single label. Example (bwv806 m3–m4):
the window reads `F#m → F#7/C# → Bsus2` beat-by-beat; the whole-score reads `A` across the
whole span. This is exactly the **batch (cross-barline) vs per-beat granularity gap the
2.2-i dossier quantified at ~7×** — now realised on the live P3 path.

Consequently NEW = the whole-score `analyzeSection` region answer = **the P1/P2
chord-track/implode display** (both consume whole-score `analyzeSection`). So the
**P3-vs-P1 consistency property §8/Task-3.3 asked for is achieved**: where a user selects
the whole score, the status bar (P3) now agrees with the chord track (P1/P2) at **100%**
of ticks; before, they disagreed on up to **40%** (bwv806) / **32%** (Mozart) of ticks.
The delta IS that prior P3↔P1 inconsistency being removed.

### 3.3 DCML verdicts on the root-differing ticks — the decisive direction

For every root-differing tick I looked up the active DCML chord (`quarterbeats×480` tick
alignment; absolute root = local-tonic + `root`-in-fifths) and asked whether OLD or NEW
matches the DCML root. (All ticks DCML-covered; 0 skipped.)

| Score | NEW matches (OLD wrong) | OLD matches (NEW wrong) | neither | decided verdict |
|---|---:|---:|---:|---|
| bach_bwv806_prelude | **64** | 53 | 68 | NEW better, 55/45 |
| mozart_k279_1 | 94 | **173** | 193 | **OLD better, 35/65** |
| **combined (decided)** | **158 (41%)** | **226 (59%)** | 261 | **OLD-favored** |

- On **bwv806** whole-score is marginally better (it rescues the badly-wrong window reads
  like m3–4 `F#m/Bsus2`→`A`-correct).
- On **Mozart** whole-score is **clearly worse** (the coarse regions miss DCML's faster
  harmonic changes — e.g. m22 window reads the actual `ii`/`I6` motion while whole-score
  flattens to a single `Dm`).
- ~37–42% "neither" on both: both paths are vertical analysers that miss DCML's functional
  readings (cadential 6-4, secondaries) — not cache-specific, but it makes the metric
  noisy; the **relative** old-vs-new comparison is fair (same DCML reference).

**Conclusion: whole-score P3 is not an improvement; it is a *different, coarser*
granularity that improves P3↔P1 consistency and perf enormously but does not improve (and
on the largest score degrades) per-tick DCML accuracy.** The design's optimistic prior
("plausibly the whole-score answer is better — more context") is **not** supported by the
measurement.

### 3.4 The snapshot corpus is the same delta (why 11/11 fail — see §4)

The P3 snapshot (`buildTickRegionalArray`) calls the orchestrator (§1.4), so it flows
through the cache. All 11 snapshots drift. Two classes of drift:
- **Benign path-state drift (display unchanged):** e.g. `bach_chorale_001` — `root`/
  `quality`/`key`/`wasRegional` are **identical** (G major); only the `temporalExtensions`
  fields move (`previousRootPc` −1→2, `previousQuality` unknown→major). The window-edge
  region had no predecessor; the whole-score region has its real one. The user sees the
  same chord. (This is "window artifact resolved" — strictly more correct context.)
- **Genuine displayed-chord drift:** bwv806/Mozart and the `alternatives` lists
  (e.g. `bach_chorale_003` alt root E→G) — the §3.1/§3.3 delta.

## §4 — Verification (suites, snapshots, corpus spot-gate, cold/warm perf)

| Gate | Result | Notes |
|---|---|---|
| composing_tests | **505/505 PASS** | unchanged — notation-side-only change |
| notation_tests | **57 PASS** (52 baseline + 5 new cache tests) | ran 56 + the 140 s `ColdEqualsFresh` separately |
| decode-cache unit tests | **5/5 PASS** | cold==fresh @ every tick, warm==cold, invalidation-on-edit, MRU pointer-keying |
| pipeline snapshots | **0/11 — ALL FAIL** | the §3 answer-delta (P3 snapshot → orchestrator → cache). **Goldens NOT refreshed** (held for ratification) |
| Python tests | **70/70 PASS** (`unittest`) | tools untouched |
| batch_analyze regression | **PASS** | batch path untouched |
| Baroque corpus spot-gate | **13/13, exact identity set** | `{bwv102.7, bwv14.5, bwv17.7, bwv174.5, bwv245.17, bwv245.40, bwv261, bwv269, bwv301, bwv381, bwv422, bwv432, bwv45.7}` — batch path provably untouched, confirmed |
| **cold/warm perf** | **see below** | the decode-once payoff — overwhelming |

**Cold/warm perf (`Stage31bPerf.DISABLED_ColdWarm`):**

| Score | cold first-query | warm median | warm p95 | warm max |
|---|---:|---:|---:|---:|
| bach_chorale_001 | 276 ms | **0.0006 ms** | 0.0007 ms | 0.004 ms |
| chopin_bi105_op30_1 | 1405 ms | **0.0006 ms** | 0.0007 ms | 0.004 ms |
| bach_bwv806_prelude | 2308 ms | **0.0008 ms** | 0.0010 ms | 0.005 ms |
| mozart_k279_1 | 10127 ms | **0.0008 ms** | 0.0011 ms | 0.006 ms |

Warm queries are **~5–6 orders of magnitude** below the uncached 86–215 ms medians — the
decode-once win is real and decisive (NOT a no-op). Cold first-query is a one-time
whole-score decode (Mozart 10.1 s > today's 7 s worst single click, because whole-score
Pass-0 ≫ one window) amortised over thousands of sub-µs warm queries. **The perf gate
passes overwhelmingly; the *correctness* gate (snapshots + DCML) is what stops us.**

## §5 — Rule-5 doc riders (B2 docs commit — applied, uncommitted)

1. **Baroque-13 identity set pinned (with ticks).** `CLAUDE.md` and `build_and_test.md`
   gate-policy sections now carry the Baroque-13 set next to the Jazz-7 set:
   `{bwv102.7@17520, bwv14.5@8160, bwv17.7@46080, bwv174.5@6240, bwv245.17@4800,
   bwv245.40@51360, bwv261@33840, bwv269@20640, bwv301@960, bwv381@4800, bwv422@23040,
   bwv432@5520, bwv45.7@20160}` + the Default-14 note. **Independently re-confirmed** by
   this session's `characterise_bir_false.py --corpus-dir tools/corpus/baroque` run (the 13
   ticks match exactly).
2. **Freeze-anchor prose replicated** into committed `tools/REPRODUCIBILITY.md` (it
   previously only pointed at the gitignored `tools/corpus/README.md`); the committed record
   is now self-contained.
3. **ARCHITECTURE.md file-map sentence applied** (verified absent first): adds the
   `sectionanalyzer.{h,cpp}` row to the composing file-map table + the Pass-0 injection
   contract paragraph (Stage 2.1's never-applied 2.1 §2 text).

## §6 — Unknowns / flagged decisions

1. **THE RATIFICATION FORK (Q1 re-open, recommended).** The measured answer-delta shows
   whole-score P3 is coarser and not more DCML-correct (worse on Mozart). The instruction
   reserved this for ratification. Two ways forward:
   - **(a) Ship whole-score (Q1 as ratified):** accept the Mozart accuracy regression and
     the 11/11 golden refresh in exchange for P3↔P1 consistency + the perf win. The
     goldens would be refreshed and the §3.3 Mozart degradation consciously accepted.
   - **(b) Bounded-window cache (recommended, re-opens Q1):** cache the *converged window
     result* keyed on `(score, token, measure)` instead of the whole-score section. This
     is **byte-identical to today** (same window algorithm), so **snapshots stay 11/11,
     no answer-delta, no DCML regression** — and it still delivers the decode-once perf win
     (warm re-clicks within/over a measure are free; the per-measure window is computed
     once). Q1 considered and rejected "needed ±window per query" in favour of whole-score
     on the assumption whole-score was better; the data does not bear that out. **I
     recommend (b)** unless the project's position is firmly "P3 must equal the
     batch/section chord-track reading," in which case (a).
2. **P4 / D-P4 closure deferred (flagged).** P4 kept cold (`findTemporalContext`). P4 fires
   0/2231; wiring decoded-path context would be an unmeasurable, untestable live change on
   a 0-fire path. The cache enables the closure; wiring is deferred — ratify whether to
   include.
3. **Size-1 MRU pointer-reuse hazard.** The cache keys on `const Score*`. A freed score
   whose address is reused by a new score with the same `undoStack()->currentIndex()` and
   same excludeStaves could false-hit. **CLOSED in the revision — see §R4** (lifecycle flush
   in `Notation::setScore`; no per-lifetime id or `cmdState` generation exists in engraving,
   confirmed by investigation, so the close-hook is the reliable fix).
4. **DCML metric caveats.** Root-pc via `root`-in-fifths + resolved localkey; secondary/
   tonicised chords and my fifths arithmetic can mis-resolve, inflating "neither." The
   relative OLD-vs-NEW verdict (same DCML reference both sides) is unaffected.
5. **Goldens deliberately not refreshed; nothing committed.** Per the stop conditions, the
   11/11 snapshot drift and the answer-delta are reported for ratification — no
   `--update-goldens`, no commit.

---

# §R — REVISION: bounded-window cache (Q1 re-decided 2026-06-12)

> Cowork ratified **option (a): bounded-window cache**. The whole-score variant above is
> **shelved** (evidence preserved in `docs/p3_granularity_ab_3_1b.md`). This section
> supersedes §1.2/§2 (cache implementation), §3 (the answer-delta is now the byte-identity
> proof), and §4 (snapshots now pass). Still **uncommitted** — held for Cowork.

## §R1 — The rebuilt cache

The cache now **memoizes the per-window section build** inside the *unchanged* expanding-±-
measure-window P3 path, instead of replacing it with a whole-score decode.

- **What is cached:** `buildWindowSection(score, ws, we, exclude)` = Pass-0
  (`analyzeHarmonicRhythm`) + `analyzeSection` over one window — the single expensive step
  of the convergence loop, and a **pure function** of its inputs under a fixed score.
- **Key:** `(windowStartTick, windowEndTick)` under a `(score, undo-token, excludeStaves)`
  guard. **MRU size = 16** windows. Justification: a click in measure *m* expands through
  `[m−1,m+1], [m−2,m+2], …` (usually converging in 1–2 steps); clicks cluster on a few
  adjacent measures; 16 window-sections cover the hot set, at KB–tens-of-KB each (≪ 1 MB).
- **Invalidation:** the undo-token (`undoStack()->currentIndex()`) makes a change check
  O(1); any guard mismatch flushes the whole MRU. Conservative MVP, as before; bounded
  incremental re-decode remains a documented follow-up.
- **Byte-identity argument:** P3's algorithm (convergence loop, region match, formatting,
  P4 fallback) is untouched; only a pure function is memoized, so every per-tick answer is
  unchanged. `useCache=false` (`analyzeHarmonicContextAtTickUncachedForTesting`) bypasses
  the cache for the A/B reference.
- **P4 / D-P4:** P4 stays cold (`findTemporalContext`). The §8 D-P4/D-BRIDGE "decode-once
  closes this" claim **depended on the whole-score decode and is rolled back** to the 2.4
  documented-contract state (see the `docs/decoder_design.md` §8 amendment).

## §R2 — Verification (byte-identity restored)

| Gate | Result |
|---|---|
| **pipeline snapshots** | **11/11 PASS — NO golden refresh** (byte-identity restored) |
| **byte-identity A/B** | `CachedEqualsUncachedAcrossWarmSweep`: cached == uncached at **every tick** across a warm sweep incl. MRU eviction (unit test, on by default). `Stage31bAnswerDelta` perf-corpus sweep asserts `rootDiff=qualDiff=bassDiff=keyDiff=0` |
| **decode-cache unit tests** | **4/4 PASS** — CachedEqualsUncached, ReclickAddsNoBuilds, InvalidationOnEdit, DistinctScoresDoNotShareCache |
| composing_tests | **505/505** (unchanged) |
| notation_tests | **56/56** (52 baseline + 4 cache tests) |
| Python / batch / Baroque-13 | unchanged by file-map (no composing/tools touched); Baroque spot-gate `13`/exact-identities held earlier this session (batch path byte-identical) |

Zero answer-delta proof: the bounded-window cache memoizes a pure function, so it cannot
differ from the uncached path — proven by (a) the snapshot 11/11 no-refresh and (b) the
`CachedEqualsUncachedAcrossWarmSweep` per-tick equality test.

## §R3 — Cold/warm perf (`Stage31bPerf.DISABLED_ColdWarm`)

| Score | cold/click median | cold/click p95 | warm re-click median | warm re-click p95 | warm max |
|---|---:|---:|---:|---:|---:|
| bach_chorale_001 | 117 ms | 226 ms | **0.0035 ms** | 0.0125 ms | 0.062 ms |
| chopin_bi105_op30_1 | 293 ms | 561 ms | **0.0029 ms** | 0.0081 ms | 0.019 ms |
| bach_bwv806_prelude | 48 ms | 1043 ms | **0.0034 ms** | 0.0084 ms | 0.021 ms |
| mozart_k279_1 | 342 ms | 2505 ms | **0.0035 ms** | 0.0086 ms | 0.039 ms |

- **Cold per-click ≈ the uncached baseline** (`perf_p3_baseline.md`: medians 86/215/33/106 ms,
  p95 177/369/1082/2754 ms). The cold p95s track the baseline closely (226/561/1043/2505 vs
  177/369/1082/2754); cold medians are the same order (sampled 30 spread ticks, each with the
  cache cleared, so each is a genuine fresh window analysis). **No decoder-induced
  regression** — a cold click *is* the window analysis plus an O(1) guard check + one MRU
  insert.
- **Warm re-click ≈ 0.003 ms** — **~4–5 orders of magnitude** below a cold click. This is the
  bounded-window decode-once payoff: re-clicking a note (or a same-measure neighbour) serves
  every window section from the MRU. (Not the whole-score variant's 0.0006 ms pure-lookup —
  the warm window path still runs the cheap convergence loop with cached sections — but still
  ~40,000× faster than cold.)

The bounded-window warm win is **local** (re-click / same-measure neighbour); the
whole-score variant's cross-measure warm win is **forfeited** — the accepted cost of
byte-identity.

## §R4 — Pointer-reuse hazard CLOSED (the approval pre-condition) + deviations

**The pointer-reuse hazard (§6.3) is closed via a lifecycle flush.** Investigation
(thorough — `Score`/`MasterScore`/`EngravingObject` ctors/dtors, `cmdState`, the EID
register, `Score::validScores`): **no per-lifetime Score id exists** and **no Score-level
destruction channel exists** (only `elementDestroyed`, for child elements). `IGlobalContext`
is not an option — the notation module deliberately does not link `context` (circular-dep
risk). So the fix is the instruction-endorsed **close hook**, at the cleanest single point:

- **`Notation::setScore()`** (`notation.cpp`) now calls the new public
  `mu::notation::clearHarmonicDecodeCache()` on every score install, **before** its
  early-return (so it fires even when a new score is installed at a reused address equal to
  the dangling previous pointer). `ExcerptNotation` installs via the same base `setScore`,
  so master and part scores are both covered.
- **Why this is reliable AND complete with one hook:** the cache only ever holds the score
  of a clicked note — necessarily a score currently installed in a `Notation`. A reused-
  address score can only be *queried* after it is *installed* via `setScore`, and that
  install flushes the stale entry first. So no false-hit window exists. `setScore` is rare
  (load/replace), so warm-cache perf during interaction is unaffected.
- **Test:** `LifecycleFlushDropsCache` pins the flush primitive (`clearHarmonicDecodeCache()`
  drops the cache → next query rebuilds). The address-reuse event itself is **not
  deterministically forceable** in the ScoreRW unit env (no `Notation`; allocator reuse is
  nondeterministic) — documented in the test + the cache code comment, per the instruction's
  allowance.

**Deviations from the revision instruction:** none substantive. MRU size = 16 (justified,
§R1). The byte-identity A/B is realized as a fast always-on unit test
(`CachedEqualsUncachedAcrossWarmSweep`) plus the DISABLED perf-corpus sweep
(`Stage31bAnswerDelta`, asserting 0 diffs). The guard is a lifecycle flush rather than an
in-guard identity token because no reliable per-lifetime identity exists (investigated).
