# CC Instruction: 3.1b revision — bounded-window cache (Q1 re-decided on evidence)

## The decision

**Option (a): bounded-window cache.** Q1's ratified "whole-score" answer is formally
RE-DECIDED — its premise ("whole-score context is better") was falsified by your
measurement (combined DCML verdict 59/41 in the window path's favor; Mozart 35/65
against whole-score). Re-opening a ratified decision on falsifying evidence is the
process working, not a failure. Option (b) is rejected outright: a measured accuracy
regression on the live path plus an 11-golden refresh is everything this plan exists
to prevent.

Two ownership notes for the record: the instruction's §1.4 snapshot-harness premise
(raw functions, not orchestrator) was **Cowork's error**, caught by your stop. And the
answer-delta data you produced is NOT discarded — it is the first measured per-tick
granularity-accuracy comparison and becomes Stage-5 evidence (see Task 3).

## Task 1 — Rebuild the cache as bounded-window

Per your recommendation: cache the converged window result keyed on
`(Score*, undo-token, measure/window-id, excludeStaves)` — small MRU (size: your call,
justify; status-bar usage clusters on a few measures). Requirements:

1. **Byte-identical to today's P3**: zero answer-delta at every tick (the warm result
   IS the cold result, memoized); snapshots **11/11 with NO golden refresh**; all
   suites green; Baroque spot-gate (13, identities). This restores byte-identity as
   the hard gate — no ratification burden on the answers.
2. Invalidation: same conservative whole-cache flush on any score change
   (undo-token key may make this nearly free — state how).
3. Perf: re-run the sweep. Expected shape: first query per window ≈ baseline; repeat
   queries on the same window ≈ your measured ~0.0006 ms class. Report cold/warm per
   score. (The whole-score variant's cross-measure warm win is forfeited — that's the
   accepted cost of correctness; say so in the report, with the numbers.)
4. P4 stays cold (as today). The D-P4/D-BRIDGE "decode-once closes this" claim from
   design §8 is ROLLED BACK to the 2.4 documented-contract state — closure now depends
   on the granularity decision (Task 3), not on this cache.

## Task 2 — Design-doc amendment (same commit)

Append to `docs/decoder_design.md` a dated "§8 amendment (3.1b outcome)":
- Q1 re-decided: bounded-window cache shipped; whole-score SHELVED with the measured
  evidence (32–40% tick delta on contrapuntal scores; DCML 59/41 old-favored;
  Mozart 35/65) — do not re-attempt without the Stage-5 granularity decision.
- The §8 D-P4/D-BRIDGE closure claim rolled back accordingly.
- The §1.4-premise erratum (snapshot harness flows through the orchestrator).
- Cross-reference: this is the 2.2-i granularity finding recurring (fine per-tick view
  is more DCML-accurate per tick; coarse section view is self-consistent) — the
  P3↔P1 consistency question is hereby PARKED as an explicit product/Stage-5 question,
  not resolvable by cache architecture.

## Task 3 — Preserve the evidence

Promote the answer-delta A/B data (per-score tick-delta counts, DCML verdict tables,
P3-vs-P1 consistency quantification) from the report into a small committed artifact
`docs/p3_granularity_ab_3_1b.md` (tables + one-paragraph reading, no narrative
sprawl) — flagged as Stage-5 input alongside the granularity-robust metric mandate.
Update roadmap 5.2's row: add "P3 window-vs-whole-score A/B (3.1b) is measured
evidence: granularity choice changes per-tick DCML accuracy by double digits."

## Commits (after the gate passes — held for Cowork)

- B1′ `feat: bounded-window decode cache for the P3 query path (Stage 3.1b, byte-identical)`
  — cache + tests + design-doc amendment + the granularity-AB artifact + roadmap touch.
- B2 (the rule-5 doc riders) — unchanged from your applied working-tree state, commit
  as previously specified.

## Report — update `cc_stage3_1b_report.md` (append a "revision" section)

§R1 the rebuilt cache (key, MRU size, invalidation); §R2 verification incl. snapshots
11/11 NO refresh + zero answer-delta proof (state how proven — e.g. the Task-3 A/B
harness re-run showing 0 differing ticks); §R3 cold/warm perf table + the forfeited
cross-measure win quantified; §R4 anything that didn't match this instruction.

Stop conditions: any snapshot diff or nonzero answer-delta (the bounded-window cache
has no excuse for either); warm perf not materially better on repeat queries; the
undo-token invalidation proving unreliable.
