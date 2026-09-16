# CC Instruction: Stage 2.5 — P3 performance baseline (+ 2 riders) — closes Stage 2

## Context

Roadmap **2.5**, the last Stage-2 item: capture the P3 status-bar path's performance
NOW, before Stage 3 adds decode cost. Purpose: an honest pre-decoder baseline + the
budget envelope for the decoder's quality-level-0 (beam-1 must remain status-bar
viable). Measurement-only — zero production-code changes. Base: `6be2b30a96`.

Standing rules (handoff trust model 1–4) apply.

## Task 1 — Profile harness

P3 = `analyzeHarmonicContextRegionallyAtTick` (per status-bar query: expanding measure
window → `analyzeHarmonicRhythm` Pass-0 → `analyzeSection`). Build the cheapest honest
harness — suggestion (adapt with reasons): a notation-tests–style benchmark fixture or
a small tool target that loads a score, then calls the public per-tick entry
(`analyzeHarmonicContextAtTick`) for EVERY chord-bearing tick, wall-timing each query.
Decide and document whether it lands as a committed manual/disabled test or a tools/
binary — it should be re-runnable at Stage 3, not throwaway.

Measure (per score; ≥3 runs, report median-of-runs):
1. Per-query latency: median / p95 / max (ms), query count.
2. Scores spanning size classes — suggest from the snapshot corpus: a chorale
   (bach_chorale_001), a mid-size piano piece (chopin BI105-1), the largest convenient
   (mozart K279-1 or bwv806 prelude). Same machine, release build, note CPU.
3. Scaling shape: does per-query cost grow with score size / window expansion? (Plot
   not needed — a table of per-score medians + the largest-window outliers suffices.)
4. P4-fallback frequency over the same sweep (you now have the call site — count P3
   empties; closes the §1.3 "rate unknown" honestly for batch-loadable scores).
5. If a query is egregious (>100 ms class), one coarse attribution (Pass-0 vs
   analyzeSection — a timer around each suffices; no profiler integration this run).

## Task 2 — The committed profile note

`docs/perf_p3_baseline.md`: machine/build context, the table, scaling observations,
P4-fallback counts, and one explicit paragraph: "Stage-3 budget: quality level 0
(beam-1) must keep per-query p95 within <observed p95 × small factor — state your
recommendation with the numbers in hand>." STATUS-ready summary line in the report.

## Task 3 — Riders

1. **Python-test-count reconciliation**: 2.3 verified 68/68; 2.4 reported 67/67
   including +2 new (68+2=70≠67). Explain with evidence: run the suite, enumerate test
   names, diff against the 2.3-era list (git show the test files at `001b15df2d` if
   needed). If tests were consolidated/removed in the V4 edit, say which and why; if
   3 tests are silently not discovered (e.g. a discovery/skip artifact), that is a real
   bug — fix the discovery, don't lose pinned tests.
2. **Bookkeeping docs flush**: commit STATUS.md + COWORK_HANDOFF.md +
   docs/implementation_roadmap.md as they stand (includes Cowork's 2.4-row
   falsification edit + the V4/2.4 closure entries; sanity-check coherence only).

## Commits

- P1 `perf: P3 status-bar baseline harness + docs/perf_p3_baseline.md (Stage 2.5)` —
  await Cowork confirmation (harness placement is the one reviewable choice).
- P2 (rider 2 docs flush) — direct.
- Rider 1's outcome: if a discovery bug was found+fixed, its own small commit (direct,
  tests-only); if explanation-only, it goes in the report.

## Report — `cc_stage2_5_report.md`

§1 harness design + placement rationale; §2 the numbers table + budget recommendation;
§3 P4-fallback counts; §4 the test-count reconciliation (evidence, not hand-waving);
§5 unknowns. Tag claims [probe]/[code].

Stop conditions: the per-tick API can't be driven outside the live app without
production changes (report the design obstacle, don't hack around it); the
reconciliation reveals lost pinned tests that can't be recovered cleanly.
