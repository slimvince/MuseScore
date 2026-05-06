# Phase 3c — Recon: Origin and Purpose of P3's Display-Context Analysis

**Scope:** Read-only investigation. No source edits. Determine
whether P3's second `analyzeChord` call (with `collectRegionTones` +
`findTemporalContext` context) is **(α) cruft** that predates the
canonical per-region analysis path and was never cleaned up,
**(β) an edge-case handler** that solves a specific problem the
per-region call mishandles, or **(γ) a genuine improvement** the
per-region call should absorb.

This recon informs how Phase 3c-impl is shaped. The presumption
going in is **(α)** — Pass 0 (Jaccard boundary detection) already
establishes the principled per-region window, so the per-region
`analyzeChord` call operates on the harmonically-justified note set
by construction. The display-context call is guilty until proven
innocent. Recon's job is to confirm, refute, or refine that prior.

**Reference docs:**
- `docs/policy2_coalescing_map.md` — divergence D definition,
  cites lines 327–354 (display re-analysis) and 372–375 (tie-break
  prepend) of `notationcomposingbridge.cpp`
- `docs/unified_analysis_pipeline.md` — refactor plan
- Phase 3b commit `ee8e2655bd` for context

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit; stop
   and surface.
2. Confirm on `master`, up-to-date with origin.

---

## Investigation

This is a read-only recon. Do not modify any source file. The only
file written this session is the recon report itself.

### Q1 — Origin archaeology

Find when each piece of code was introduced and what problem it
addressed.

For each of the following, run `git log --follow --diff-filter=A --
<path>` to find the introducing commit, and `git blame` the relevant
line ranges to see the most recent significant edit:

- The second `analyzeChord` call inside P3 (around lines 327–354 of
  `src/notation/internal/notationcomposingbridge.cpp` per
  policy2_coalescing_map.md — verify the line range, the file may
  have shifted)
- The tie-break prepend (around lines 372–375, same file)
- `collectRegionTones` (likely in
  `src/notation/internal/notationcomposingbridgehelpers.cpp` or a
  similar bridge-layer file — locate it)
- `findTemporalContext` (same area)
- `prepareUserFacingHarmonicRegions` (per policy2 doc:
  `notationcomposingbridgehelpers.cpp:1575`)
- The per-region `analyzeChord` invocation site inside
  `prepareUserFacingHarmonicRegions`

For each: capture introducing commit hash, date, one-line commit
message, and (if available) PR/issue reference. Also note any
significant subsequent changes documented by `git blame` (e.g., a
follow-up commit that explains intent in its message).

**Question to answer:** Which came first — the per-region path or
the display-context path? If the display-context call predates
`prepareUserFacingHarmonicRegions`, it's likely legacy. If it
postdates, it was added deliberately and the commit message should
explain why.

### Q2 — Input comparison

For a single representative region (pick one from any corpus score),
characterize what note set each `analyzeChord` call sees:

- **Per-region call:** What note set does
  `prepareUserFacingHarmonicRegions` pass into `analyzeChord` for
  this region? Trace from the call site backward to whatever
  collects/aggregates notes for the region. Note the collection
  function and its window definition.
- **Display-context call:** What does `collectRegionTones` collect
  for the same region? Same notes? Wider window? Different
  selection criteria (e.g., bass-emphasis, voice-leading filtering)?
- **Temporal context:** What `ChordTemporalContext` (or equivalent)
  does each call get? Per-region call's context is constructed
  somewhere in the Pass 0–4 pipeline; display-context call's
  context is constructed by `findTemporalContext`. Are they the
  same struct populated identically, or different?

**Question to answer:** Do the two calls operate on the same input,
different-but-equivalent input, or genuinely different input? If
genuinely different, what's the substantive difference?

### Q3 — `findTemporalContext` semantics

Read `findTemporalContext`'s implementation. Characterize:

- Does it construct context from the same neighboring-region data
  Pass 0–4 already produces, or does it re-derive context from
  raw score data?
- Does it do anything Pass 0–4's context construction doesn't — e.g.,
  weight bass tones differently, span across region boundaries,
  consider longer/shorter time windows?
- Are there flags or branches inside it that suggest it was added
  to handle a specific case?

**Question to answer:** Is `findTemporalContext` doing principled
work the per-region context construction lacks, or is it doing the
same thing via a different code path?

### Q4 — Test coverage hint

Look for tests (in `src/composing/tests/`,
`src/notation/tests/`, or `tools/`) that exercise the divergence
between per-region and display-context analysis. Specifically:

- Tests that assert different chord identities depending on which
  path is invoked
- Tests that explicitly call P3 (the regional tick API) and check
  display-specific behavior
- Tests with names like "*display*", "*context*", "*regional*" in
  the analysis test suites
- Comments in tests documenting why a specific case requires the
  display-context analysis

**Question to answer:** Does the test suite document any case where
the display-context analysis produces a known-better result than
the per-region analysis would? If yes, those cases are the (β)
edge-case handlers. If no documented test cases exist, the (α)
cruft hypothesis gains weight.

### Q5 — Synthesis

Based on Q1–Q4, classify:

**(α) Cruft.** Display-context call predates per-region
canonicalization, no documented test coverage justifies its
existence, `findTemporalContext` does nothing Pass 0–4 doesn't.
**Implication for Phase 3c:** delete the second call, alternatives
come from per-region with high confidence those are the canonical
results. Phase 3c collapses back to the original prompt's shape (no
3c-prep needed). Snapshot byte-identity expected for all paths
except additive `alternatives` field on `tickRegional`.

**(β) Edge-case handler.** Display-context call solves a specific
documented case the per-region path mishandles. **Implication:**
identify the case, decide whether to preserve handling (3c-prep
folds the edge-case logic into per-region) or accept degradation
on that case. May affect snapshots.

**(γ) Genuine improvement.** `findTemporalContext` does principled
work Pass 0–4 doesn't (e.g., cross-boundary context, different
weighting, dynamic window expansion). **Implication:** 3c-prep
folds the logic into per-region; expect snapshot diffs in
implode/annotation that should be inspected as discoveries.

State the verdict and the evidence for it.

---

## Deliverable

Write a single report file at `docs/divergence_d_recon.md` with
sections matching Q1–Q5 above. Concise and citation-heavy — every
claim backed by file:line or commit hash. Total length: probably
3–6 pages of markdown. The report's audience is "next session
planning the actual Phase 3c implementation," not historical
archaeology — keep findings in service of the (α)/(β)/(γ) decision.

Suggested skeleton:

```markdown
# Divergence D — Display-Context Analysis Recon

Date: 2026-04-25
Scope: read-only, no source edits.

## Verdict

**(α) Cruft** / **(β) Edge-case handler** / **(γ) Improvement** —
[one paragraph evidence summary]

## Q1 — Origin archaeology

| Function | Introduced (commit, date) | One-line intent |
|---|---|---|
| ... |

[Brief narrative: which came first, what does the timeline suggest]

## Q2 — Input comparison

[Side-by-side characterization of note sets and temporal context]

## Q3 — findTemporalContext semantics

[What it actually does, what Pass 0–4 already does]

## Q4 — Test coverage

[Documented test cases, or absence thereof]

## Q5 — Synthesis and Phase 3c implication

[Verdict, evidence, recommended Phase 3c shape]
```

---

## Commit + push

Single commit, just the recon report. Suggested message:

```
Phase 3c recon: characterize divergence D's display-context analysis

Investigates origin, semantics, and test coverage of P3's second
analyzeChord call (collectRegionTones + findTemporalContext).
Determines whether the call is (α) cruft predating canonical
per-region analysis, (β) an edge-case handler for a specific
documented case, or (γ) a principled improvement the per-region
path should absorb.

Verdict: [α/β/γ with one-line evidence]

Informs Phase 3c-impl shape: delete-and-go (α), edge-case-fold (β),
or expander-fold-with-snapshot-discovery (γ).
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- The verdict — α, β, or γ — with two-sentence evidence summary
- The single most surprising finding from Q1–Q4 (this is what we
  pay the recon cost for; if there's nothing surprising, say so —
  that itself is a finding)
- Any deviations from this prompt and why
- Recommended Phase 3c-impl shape based on the verdict

---

## Scope guardrails

- **Do not** modify any source file. The only file written this
  session is `docs/divergence_d_recon.md`.
- **Do not** run the build or tests. This recon is pure code+history
  reading.
- **Do not** propose code changes in the report — Phase 3c-impl
  prompt comes after, informed by the verdict.
- **Do not** speculate beyond what the code and history show. If
  Q1–Q4 don't have clear evidence, say so explicitly. "I don't
  know" is a valid finding; "probably (α) but the commit history is
  unclear" is more useful than a confident guess.
