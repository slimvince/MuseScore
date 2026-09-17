# CC Instruction: Stage 3.1b — decode-once / query-many (+ rule-5 doc riders)

## Context

Implements design §8 under the ratified Q1/Q7 decisions: whole-score decode, cached in
the bridge; P3 warm queries become lookups; P4/bridge consume decoded path state (the
D-P4/D-BRIDGE closure). Base: `8e4bb4902d`.

**⚠ This is the first change since the reviews that can alter what the LIVE product
shows users.** Today each P3 query analyzes its own expanding ±measure window; a cached
whole-score decode serves whole-score results. Window-edge segmentation differs from
whole-score segmentation, so per-tick answers CAN change. The design under-confronted
this; the instruction confronts it: the answer-delta is **measured and ratified before
anything is committed**. Plausibly the whole-score answer is *better* (more context,
more consistency — the same reason the batch/section results are our reference), but
per no-surprises that is a measured decision, not an assumption.

Standing rules (trust model 1–5). Mandatory reads: design §8/§9 + Q1/Q7; the 2.4
D-P4/D-BRIDGE decisions (their revisit triggers close here); `docs/perf_p3_baseline.md`;
the P3/P4 orchestrator (`notationcomposingbridge.cpp` `analyzeHarmonicContextAtTick` /
`...RegionallyAtTick` / `...LocallyAtTick`).

## Task 1 — Survey + plan (report §1 before implementing)

1. **Cache home + lifecycle**: where in the bridge the per-score cache lives (per Q1),
   keyed how, and the **invalidation hook**: survey what score-change notification the
   notation layer offers (command/undo stack signals, score serial/dirty counter).
   **Conservative MVP mandated: invalidate the WHOLE cache on any score change.** The
   design's bounded-window re-decode is a documented follow-up (state it in the code
   comment + report), not 3.1b scope — correctness first. If NO reliable change signal
   exists: stop and report (a stale cache showing wrong labels is worse than slow).
2. **What the cached decode actually is**: one whole-score Pass-0 + `analyzeSection` +
   beam-1 decode (the `path()` plumbing from 3.1), producing per-region committed
   identities + the path state. Confirm the granularity P3 serves from it (section
   regions — the user-facing granularity per the 2.2-i dossier).
3. **P4-consumes-path placement**: the cached-path consumption lives at the
   ORCHESTRATOR level (`analyzeHarmonicContextAtTick`): P3 = cache lookup; the P4
   fallback, when it fires with a warm cache, receives path-derived temporal context.
   The raw `analyzeHarmonicContextLocallyAtTick` function keeps its cold path for
   direct callers — **the pipeline-snapshot harness calls the raw functions and must
   stay byte-identical (11/11 zero diffs is a hard gate of this instruction too)**.
   Confirm this split keeps the snapshot surface untouched; any snapshot diff = stop.
4. **Cold path**: first query (or post-invalidation) = build the cache at
   approximately today's cost; no regression vs today for the cold case.

## Task 2 — Implement (per plan)

Composing-module touches expected minimal (the 3.1 `path()` plumbing should suffice —
if `chordpathdecoder.h` or any composing analysis file changes, say so: it triggers the
full corpus A/B in Task 4). The cache + orchestrator rewiring is notation-side.
**Authorized files**: `src/notation/internal/**` (bridge + orchestrator),
`src/composing/**` if needed (flag it), tests both sides, CMakeLists.

## Task 3 — The answer-delta A/B (ratification input — run BEFORE proposing commits)

Over the 4 perf-corpus scores (chorale_001, BI105-1, bwv806 prelude, K279-1):
for every chord-bearing tick, old path (window re-analysis) vs new path (warm cache) —
1. count of ticks whose displayed result differs (root / quality / bass / key
   separately);
2. classify a sample (≥15 or all, whichever is smaller) of root-differing ticks:
   window-artifact resolved (new = section/batch reading) vs genuinely new reading —
   with DCML verdicts where the score is DCML-covered;
3. the per-tick consistency property: under the cache, does the SAME tick always get
   the SAME answer as the P1/P2 chord-track display (the dossier's "user sees" lens)?
   Today P3-vs-P1 can disagree (window vs section granularity) — quantify before/after.

## Task 4 — Verification gate

- Suites: composing 505 / notation 52 (+ new cache tests: invalidation-on-edit,
  cold-equals-fresh, warm-equals-cold) / snapshots **11/11 ZERO diffs** / Python 70 /
  batch regression.
- Corpus: if any composing-module file changed → full 0/353 × 3 A/B (3.1 protocol);
  else one Baroque regen + characterise (13, identity set) as the spot-gate, batch
  provably untouched by file map.
- **Perf — the point of 3.1b**: full `P3PerfBaseline` sweep. Expect: cold first-query
  ≈ baseline; warm per-query median/p95 orders below the 33–215 ms medians (design
  target). Report cold + warm separately per score. A warm p95 not dramatically below
  baseline = the cache isn't working — stop, don't ship a no-op.
- P4 fallback behavior: count unchanged (0 expected on the perf corpus); if the cache
  changes the count, explain why.

## Task 5 — Rule-5 doc riders (separate docs commit, content pre-decided)

1. Pin the **Baroque-13 identity set** (with ticks, from the handoff sweep entry) next
   to the Jazz-7 set in CLAUDE.md's gate-policy section (and BUILD_AND_TEST if the
   Jazz set appears there).
2. Replicate the music21 **freeze-anchor** sentence from the gitignored
   `tools/corpus/README.md` into committed `tools/REPRODUCIBILITY.md`.
3. Apply 2.1's never-applied ARCHITECTURE.md file-map sentence (sectionanalyzer
   location + Pass-0 injection contract — text in `cc_stage2_1_report.md` §2; verify
   it's still absent first).

## Commits — ALL held for Cowork ratification (incl. the docs rider this time)

- B1 `feat: decode-once cache for the P3/P4 query path (Stage 3.1b)` — held pending
  the Task-3 answer-delta ratification.
- B2 `docs: pin Baroque-13 identity set; freeze-anchor + file-map riders (rule-5 sweep)`.

## Report — `cc_stage3_1b_report.md`

§1 plan (cache home, invalidation hook found, P4 placement); §2 implementation map;
§3 **the answer-delta tables + classifications + DCML verdicts** (the ratification
centerpiece); §4 verification incl. cold/warm perf; §5 rider diffs; §6 unknowns.

Stop conditions: no reliable score-change signal; any snapshot diff; warm-cache perf
not materially better; answer-delta dominated by genuinely-new readings that are DCML-
wrong (would mean whole-score P3 is WORSE — report, don't rationalize); any composing
behavior change outside the declared file map.
