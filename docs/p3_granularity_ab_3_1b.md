# P3 window-vs-whole-score granularity A/B (Stage 3.1b)

> **Measured evidence, committed as Stage-5 input.** Produced while evaluating the
> Stage-3.1b decode-once cache. The *whole-score* decode variant (originally ratified as
> Q1) was **shelved** after this A/B; the cache shipped as a **bounded-window** memoization
> that is byte-identical to today's P3. This file preserves the per-tick
> granularity-accuracy comparison so it is not lost with the shelved variant.
>
> *Base commit `8e4bb4902d`. Harness: `Stage31bAnswerDelta.DISABLED_Sweep` (pre-revision
> form, window-vs-whole-score) in `pipeline_snapshot_tests`. DCML verdicts:
> `quarterbeats×480` tick alignment against `tools/dcml/**/harmonies/*.harmonies.tsv`.*

## What was compared

- **OLD / window** — `analyzeHarmonicContextAtTick` as it is today: an expanding ±measure
  window that converges to a stable local reading. Fine-grained.
- **NEW / whole-score** — a whole-score Pass-0 + `analyzeSection`, with each tick reading
  its region's label. Coarse (batch/section granularity); equals the P1/P2 chord-track
  display by construction.

All four perf-corpus scores are DCML-covered.

## Result 1 — the displayed-result delta (per chord-bearing tick)

| Score | ticks | rootDiff | qualDiff | bassDiff | keyDiff |
|---|---:|---:|---:|---:|---:|
| bach_chorale_001 (small, homophonic) | 80 | 0 | 0 | 0 | 0 |
| chopin_bi105_op30_1 (mazurka) | 248 | 0 | 0 | 0 | 5 |
| bach_bwv806_prelude (contrapuntal) | 462 | **185 (40%)** | 286 | 214 | 94 |
| mozart_k279_1 (sonata) | 1441 | **460 (32%)** | 441 | 449 | 119 |

The delta is **zero on small/homophonic music** and **large on contrapuntal/large music**
— it is a granularity effect, not a uniform shift. Whole-score collapses figuration into
broad harmonic-rhythm regions (e.g. bwv806 m3–m4: the window reads `F#m → F#7/C# → Bsus2`
beat-by-beat; whole-score reads a single `A`). This is the 2.2-i dossier's batch-vs-per-beat
~7× granularity gap, realised on the live P3 path.

## Result 2 — DCML correctness of the root-differing ticks (the decisive direction)

For each root-differing tick, the active DCML chord's root was compared to OLD and NEW:

| Score | NEW(whole-score) right, OLD wrong | OLD(window) right, NEW wrong | neither | verdict |
|---|---:|---:|---:|---|
| bach_bwv806_prelude | 64 | 53 | 68 | NEW better, 55/45 |
| mozart_k279_1 | 94 | **173** | 193 | **OLD better, 35/65** |
| **combined (decided)** | **158 (41%)** | **226 (59%)** | 261 | **OLD(window)-favoured** |

**Whole-score is not an accuracy improvement** — it is marginally better on bwv806 (it
rescues badly-wrong window reads) but clearly worse on Mozart (its coarse regions miss
DCML's faster harmonic changes). ~37–42% "neither" reflects both paths being vertical
analysers that miss DCML's functional readings (cadential 6-4, secondaries); the relative
OLD-vs-NEW comparison uses the same DCML reference both sides and is unaffected.

## Result 3 — P3-vs-P1 consistency (the only thing whole-score clearly improves)

Whole-score P3 equals the P1/P2 chord-track display by construction, so it gives **100%
P3↔P1 agreement**; the window path disagrees with P1/P2 on up to **40%** (bwv806) / **32%**
(Mozart) of ticks. So the granularity choice is a genuine three-way tension:

| | per-tick DCML accuracy | P3↔P1 self-consistency | status-bar locality |
|---|---|---|---|
| window (fine) | better (esp. Mozart) | worse | resolves the chord *at the clicked note* |
| whole-score (coarse) | worse on Mozart | perfect | shows the broad region's chord |

## Disposition

- **3.1b shipped the bounded-window cache** (byte-identical to the window column): no
  answer-delta, no accuracy change, snapshots unchanged. The perf win is preserved for
  warm/local re-queries.
- **Whole-score is shelved.** Do not re-attempt without resolving the granularity question
  as a deliberate product decision — which is a **Stage-5** concern (it needs the
  granularity-robust metric the 2.2-i dossier mandated, not a cache-architecture choice).
- The P3↔P1 consistency question is **parked** as an explicit product/Stage-5 item.
