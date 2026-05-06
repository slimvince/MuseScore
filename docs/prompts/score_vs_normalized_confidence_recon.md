# Recon — `score` vs `normalizedConfidence` Semantics

**Scope:** Read-only investigation. No source edits, no build, no
tests. Determine whether `ChordAnalysisResult::score` and
`ChordAnalysisResult::normalizedConfidence` are intended to produce
the same ordering of candidates, or whether they measure
genuinely different things. The question was deferred from the
three-paths divergence recon (commit `ee50b1760c` direction; the
recon itself surfaced the divergence at m285 where `score`-order
puts `Csus(add9)` first while `normalizedConfidence`-order puts
`Cm7b5` first).

The Divergence E fix (commit `9047b8adf9`) closed the consumer-side
issue by having both UIs trust `chordResults`'s analyzer-given
ordering. But the underlying analyzer-internal question remains:
why do these two metrics disagree, and is that disagreement a
calculation bug or a meaningful semantic distinction?

**Reference docs (read first):**
- `docs/three_paths_divergence_recon.md` — surfaced the metric
  disagreement at m285
- `docs/divergence_d_recon.md` — context: `analyzeChord` returns
  candidates "sorted by score descending" per
  `chordanalyzer.h:571`
- `src/composing/analysis/chord/chordanalyzer.{h,cpp}` — analyzer
  source where both metrics are computed

**Memory references** (auto-loaded):
- `project_no_stripping_in_production` — analyzer outputs maximal;
  metric-internal questions don't violate the principle but should
  be understood
- `project_chord_symbol_ban` — analyzer reads notes only; this
  recon doesn't touch inputs

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree if mainline is busy).

---

## Investigation

This is a read-only recon. Do not modify any source file. Do not
run the build or tests. The only file written this session is the
recon report itself.

### Q1 — `score` definition and computation

Locate where `ChordAnalysisResult::score` is defined and computed
in `src/composing/analysis/chord/chordanalyzer.{h,cpp}`. Trace:

- The field's declaration (file:line, type)
- Where it's assigned during chord identification
- What goes into the calculation (which factors, weights,
  normalizations)
- Whether it's bounded (e.g., 0-1, or open-ended)

Document the semantics in plain language: what does a higher
`score` mean? What does a lower one mean? What's the unit?

### Q2 — `normalizedConfidence` definition and computation

Same exercise for `normalizedConfidence`:

- Field declaration (file:line, type)
- Computation site
- Inputs to the calculation
- Bounds (likely 0-1 if it's "normalized")

The name suggests it's a normalization of `score` (or a score-like
quantity), but the m285 case shows that's not strictly true — they
produce different orderings. Determine whether:

- **(α) Linear normalization of `score`.** If
  `normalizedConfidence = f(score)` where `f` is monotonic, then
  ordering must be identical. The m285 disagreement would be a
  calculation bug.
- **(β) Different inputs.** `normalizedConfidence` consumes
  factors that `score` doesn't (e.g., context awareness,
  relative-to-other-candidates normalization). Then ordering
  divergence is by design.
- **(γ) Different weighting of same inputs.** Both metrics
  consider the same factors but apply different weights, producing
  different rankings on edge cases.

### Q3 — When did each metric get introduced?

Brief git archaeology: `git log --follow` on the relevant lines.
- When was `score` introduced?
- When was `normalizedConfidence` introduced?
- Was one introduced as a replacement for the other, or do they
  serve distinct documented purposes?

This helps disambiguate intentional-distinction from
accidental-divergence.

### Q4 — Where is each consumed?

Trace the read sites:
- `chordResults` is sorted by `score` (per the divergence-D recon)
- `normalizedConfidence` is consumed where? Status bar formatter?
  Right-click menu (pre-Divergence-E fix; now bypassed)? Anywhere
  else?

If `normalizedConfidence` has only one consumer (the
now-removed right-click sort), then practically the metric is
unused post-Divergence-E. That changes the recommendation — we
might be able to simplify by removing it.

### Q5 — Synthesis: bug or semantic distinction?

Based on Q1-Q4, classify:

- **Calculation bug.** The metrics are intended to produce the
  same ordering but a calculation issue makes them diverge on
  some inputs. Fix: align the computation.
- **Semantic distinction.** The metrics measure genuinely
  different things; their disagreement is meaningful. Document
  the distinction; preserve both.
- **Unused metric.** `normalizedConfidence` no longer has a
  meaningful consumer post-Divergence-E. Recommend removing it
  entirely.
- **Unclear from code reading.** Honest uncertainty; recommend
  empirical follow-up.

State the recommendation with evidence.

---

## Deliverable

Write a single report file at
`docs/score_vs_normalized_confidence_recon.md` with sections
matching Q1-Q5. Citation-heavy — every claim about computation
or behavior backed by file:line. Total length: probably 2-3
pages of markdown.

Suggested skeleton:

```markdown
# `score` vs `normalizedConfidence` Recon

Date: 2026-04-26
Scope: read-only, no source edits.

## Verdict

[Calculation bug / semantic distinction / unused metric / unclear,
with one-paragraph evidence summary]

## Q1 — `score` semantics

[Definition, computation, what higher/lower means]

## Q2 — `normalizedConfidence` semantics

[Same for the second metric]

## Q3 — Introduction history

[git archaeology findings]

## Q4 — Consumer sites

[Where each is read; whether normalizedConfidence has live
consumers post-Divergence-E]

## Q5 — Synthesis and recommendation

[Verdict + recommended next action]
```

---

## Commit + push

Single commit, just the recon report. Suggested message:

```
Recon: score vs normalizedConfidence semantics

Investigates whether the analyzer's two metrics
(ChordAnalysisResult::score, ::normalizedConfidence) are intended
to produce the same ordering of candidates or measure different
things. Question deferred from the three-paths divergence recon
(commit ee50b1760c).

Verdict: [calculation bug / semantic distinction / unused metric
/ unclear].

Recommends [fix shape].
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- Verdict with one-sentence rationale
- The most surprising finding (e.g., `normalizedConfidence` has no
  live consumers post-Divergence-E; or the two metrics differ in
  factors A, B, C; or the disagreement is a clear calculation bug)
- Recommended next action (fix / document / remove / further
  recon)
- Any deviations from this prompt and why

---

## Scope guardrails

- **Do not** modify any source file. The only file written this
  session is `docs/score_vs_normalized_confidence_recon.md`.
- **Do not** run the build or tests. Pure code-and-history reading.
- **Do not** propose code changes in the report — fix prompts
  come after, informed by the verdict.
- **Do not** speculate. "I can't tell from code alone" is a valid
  finding.
- **Do not** broaden scope to other ChordAnalysisResult fields.
  This recon is narrowly about score vs normalizedConfidence.
