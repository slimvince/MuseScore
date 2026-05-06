# Phase 4 — Recon: HarmonicRegion Retirement Surface

**Scope:** Read-only investigation. No source edits, no build, no
tests. Characterize the four unknowns that gate Phase 4
implementation: residual `ChordTemporalContext` content, full
`HarmonicRegion` consumer surface, Pass 0–4 dependency depth on
`HarmonicRegion`, and feasibility of moving `analyzeSection` from
the bridge layer to the composing module. Output a recon report
that drives the Phase 4 implementation split.

This recon mirrors the 3c-recon pattern (commit `d35f003aa2`,
`docs/divergence_d_recon.md`) — citation-heavy, verdict-driven,
implementation-shape recommendation.

**Reference docs (read first):**
- `docs/unified_analysis_pipeline.md` — overall plan; Phase 4 is
  "retire HarmonicRegion + prepareUserFacingHarmonicRegions"
- `docs/policy2_coalescing_map.md` — describes Pass 0–4 inside
  `prepareUserFacingHarmonicRegions` (line 1575 of
  `notationcomposingbridgehelpers.cpp` per the policy2 doc)
- `docs/divergence_d_recon.md` — for the critical preservation
  note: `findTemporalContext` is NOT cruft; the seeding pattern
  (call once, evolve forward through regions) must move into
  `analyzeSection`'s body when `prepareUserFacingHarmonicRegions`
  retires
- Phase 3c-impl commit `9f515d6372` for current state

**Phase 2 audit appendix (in `docs/unified_analysis_pipeline.md`):**
- Confirms zero emitter-leaked fields on `ChordTemporalContext`
- Lists 5 fields migrated to `AnalyzedRegion::temporalExtensions`
- Lists 3 dead fields deleted

---

## Pre-flight

1. `git status` and `git diff --stat` — trailing `\0` or mid-token
   truncation means a prior CC session was cut by usage limit;
   stop and surface.
2. Confirm on `master`, up-to-date with origin (or use the
   appropriate worktree for this recon if mainline is busy).

---

## Investigation

This is a read-only recon. Do not modify any source file. Do not
run the build or tests. The only file written this session is the
recon report itself.

### Q1 — `ChordTemporalContext` post-3c residual

Locate the current `ChordTemporalContext` definition (likely in
`src/composing/chordanalyzer.h` or a sibling header — grep
`struct ChordTemporalContext` to confirm). Characterize what
remains after Phase 3c's migrations and deletions:

**Important:** do not confuse `ChordTemporalContext` (the legacy
struct being audited here) with `ChordTemporalExtensions` (the
new struct created in Phase 3c on `AnalyzedRegion`, holding the
5 migrated fields per `src/composing/analyzed_section.h`). Different
types, different lifetimes; the latter is canonical going forward.

- **Field inventory.** List every field still on the struct. For
  each: type, default, who writes it, who reads it (file:line cites).
- **Coupling analysis.** Are the remaining fields cohesive (one
  thematic concept) or grab-bag (multiple unrelated concerns)?
- **Cleanest fate.** Three options:
  - **(a) Delete the struct entirely.** Only viable if all remaining
    fields can move to `AnalyzedRegion` or be inlined at call sites.
  - **(b) Rename and keep.** Viable if remaining fields are still a
    cohesive concept that just outgrew the original name.
  - **(c) Flatten into AnalyzedRegion.** Viable if fields are
    cohesive but the wrapper struct doesn't carry its weight.

State the verdict and evidence. Whichever fate is recommended,
identify the consumers that would need updating.

### Q2 — `HarmonicRegion` consumer sweep

Find every reference to `HarmonicRegion` in the codebase. For each:

- File and line
- Whether the reference is a *producer* (creates `HarmonicRegion`
  instances), a *consumer* (reads from `HarmonicRegion`), a *signature*
  (function takes/returns `HarmonicRegion`), or a *type-only* reference
  (forward decl, header include, etc.)
- For consumers and signatures: assessment of whether the
  reference uses `HarmonicRegion` as a passive carrier (could
  trivially be swapped for `AnalyzedRegion`) or makes
  type-specific assumptions (would need real refactor)

Known references already enumerated (verify and expand):
- `prepareUserFacingHarmonicRegions` returns `vector<HarmonicRegion>`
- Pass 0–4 helpers operate on it (Q3 covers depth)
- `detectCadences` / `detectPivotChords` take `vector<HarmonicRegion>`
  with 1:1 adapter inside emitters
- `analyzeSection`'s body translates `HarmonicRegion → AnalyzedRegion`

What might exist that we haven't enumerated:
- Test fixtures that construct `HarmonicRegion` directly
- Diagnostic / debug code paths
- Tools (`tools/` directory) that consume `HarmonicRegion` —
  earlier retirement work (`docs/symbol_input_audit.md`, commits
  `02e3733afb` + `69716deead`) deleted Jazz-path tool consumers
  including `analyzeScoreJazz` and `injectWrittenRootTone`. Verify
  the residual tool surface is clean of `HarmonicRegion`
  references.
- Any caller outside `src/notation/internal/` and `src/composing/`

**Question to answer:** Is the consumer surface what we think it is,
or are there hidden consumers that change Phase 4's risk profile?

### Q3 — Pass 0–4 dependency depth on `HarmonicRegion`

For each pass inside `prepareUserFacingHarmonicRegions`, characterize
whether the logic uses `HarmonicRegion` as a passive carrier (mechanical
conversion possible) or encodes type-specific assumptions (real
refactor needed). Reference policy2_coalescing_map.md for the pass
breakdown:

- **Pass 0** — boundary detection (delegates to `analyzeHarmonicRhythm`
  / `Smoothed`; likely thin)
- **Pass 1** — gap-tone region insertion (`inferGapRegion`,
  `regionSupportsGapTones`, `inferSparseGapChord`,
  `analyzeGapWithContext`, `applyGapKeyContext`)
- **Pass 2** — within-measure same-chord merge (`appendMeasureRegion`)
- **Pass 3** — measure-opening carry
- **Pass 4** — key/mode stabilization (`stabilizeHarmonicRegionsForDisplay`)

For each pass:
- What `HarmonicRegion` methods/fields does it touch?
- Are those methods/fields present on `AnalyzedRegion` already (post-3c)?
  If not, what would need adding?
- Does the pass's logic make assumptions that conversion would
  break? (e.g., "fields are mutable in-place," "this method's
  side effect is X," etc.)
- Conversion verdict: mechanical, real-refactor, or genuinely-blocked?

Special attention to the gap-tone passes (Pass 1) — they may use
`HarmonicRegion`-specific construction patterns since they're
producing new regions during analysis, not just consuming existing
ones.

### Q4 — `analyzeSection` move to composing — feasibility

`analyzeSection` currently lives in `mu::notation::internal`
namespace inside `notationcomposingbridgehelpers.cpp` (per Phase 2
deviation note). The unified-pipeline plan envisions composing as
the home for analysis types and entry points; the bridge layer
should be only emitter coordination + score-side IO.

For `analyzeSection` to move to `src/composing/`:

- **What does it currently access?** Score, Segment, Fraction —
  these are engraving types. Trace what `analyzeSection` actually
  needs from them.
- **What's the layering picture?** Can the composing module see
  engraving types directly, or does it have to receive
  pre-extracted note data from the bridge? Look at composing
  module's existing CMake links and includes.
- **What's the seeding-pattern requirement?** Per the divergence
  D recon, when `prepareUserFacingHarmonicRegions` retires, the
  `findTemporalContext` seeding pattern (call once, evolve
  forward) moves into `analyzeSection`'s body. `findTemporalContext`
  is currently called by the canonical path at
  `src/notation/internal/notationharmonicrhythmbridge.cpp:213-214`
  (per the divergence D recon). Determine which module it lives
  in and whether `analyzeSection`, if relocated to composing,
  could still call it — or whether the helper itself would also
  need relocating.
- **Three feasibility positions:**
  - **(a) Move is mechanical** — composing can already see what
    it needs; the move is just a file-relocation + namespace
    adjustment.
  - **(b) Move requires intermediate types** — composing needs
    bridge-layer pre-extracted note data passed as parameters
    instead of direct Score* access. Real refactor.
  - **(c) Move requires layering rework** — composing module's
    current dependency boundaries don't permit it; we'd need to
    decide whether to relax the boundary or accept that
    `analyzeSection` stays in bridge.

State the verdict and evidence.

### Q5 — Synthesis and Phase 4 implementation shape

Based on Q1–Q4, recommend a Phase 4 implementation split. Three
shapes to consider:

- **One session.** Everything mechanical or near-mechanical;
  Pass 0–4 conversion straightforward; ChordTemporalContext fate
  clear; analyzeSection move feasible. Snapshot byte-identity
  expected throughout.
- **Two sessions: 4a + 4b.**
  - 4a: Convert `detectCadences` / `detectPivotChords` signatures
    to consume `AnalyzedRegion` (or `AnalyzedSection`). Drop the
    1:1 adapters in emitters. Snapshot byte-identical.
  - 4b: Rewrite Pass 0–4 to operate on `AnalyzedRegion` natively.
    `analyzeSection` becomes canonical. `prepareUserFacingHarmonicRegions`
    retires. `HarmonicRegion` deleted. `ChordTemporalContext`
    handled per Q1's verdict. Snapshot byte-identical.
- **Three sessions: 4a + 4b + 4c.**
  - 4a, 4b as above.
  - 4c: Move `analyzeSection` to composing module.
    `ChordTemporalContext` rename if applicable. (Possibly with
    a 4c-recon if the move is non-trivial per Q4.)

Recommend the split shape with reasoning. Identify the
behavior-preservation risk per chunk:
- "Mechanical conversion, byte-identity expected" — low risk
- "Conversion touches analysis logic shape, byte-identity expected
  but verify" — medium risk
- "Logic actually changes, byte-identity not expected" — should not
  be in scope; flag if any chunk falls here

Identify dependency order. Note any recon-to-impl gaps where
additional sub-recon would help.

---

## Deliverable

Write a single report file at `docs/phase4_recon.md` with sections
matching Q1–Q5 above. Concise and citation-heavy — every claim
backed by file:line. Total length: probably 4–7 pages of markdown.
The report's audience is "next session planning the actual Phase 4
implementation," not historical archaeology — keep findings in
service of the implementation-shape decision.

Suggested skeleton:

```markdown
# Phase 4 — HarmonicRegion Retirement Recon

Date: 2026-04-25
Scope: read-only, no source edits.

## Recommended implementation shape

[One sentence: 1 / 2 / 3 sessions, with one-line evidence summary]

## Q1 — ChordTemporalContext residual

[Field inventory, coupling analysis, recommended fate, evidence]

## Q2 — HarmonicRegion consumer sweep

[Full reference list with classifications]

## Q3 — Pass 0–4 dependency depth

[Per-pass conversion verdict with evidence]

## Q4 — analyzeSection move feasibility

[Layering picture, verdict on move, evidence]

## Q5 — Synthesis

[Recommended split, dependency order, behavior-preservation risk
per chunk, any sub-recons needed]
```

---

## Commit + push

Single commit, just the recon report. Suggested message:

```
Phase 4 recon: characterize HarmonicRegion retirement surface

Investigates ChordTemporalContext post-3c residual, full HarmonicRegion
consumer surface, Pass 0-4 dependency depth on HarmonicRegion, and
feasibility of moving analyzeSection to the composing module.

Recommends Phase 4 implementation split: [1/2/3 sessions per Q5
verdict].

Informs Phase 4-impl shape and identifies any sub-recons needed.
```

**Push to origin at end of session.**

---

## Report back

- Commit hash + push confirmation
- The recommended Phase 4 split (1 / 2 / 3 sessions) with one-sentence
  evidence summary
- The single most surprising finding from Q1–Q4 (this is what we pay
  the recon cost for; if there's nothing surprising, say so — that
  itself is a finding)
- The behavior-preservation risk picture per chunk (low / medium —
  any "high" should be flagged immediately)
- Whether any chunk requires its own sub-recon (analogous to how 3c-recon
  preceded 3c-impl)
- Any deviations from this prompt and why

---

## Scope guardrails

- **Do not** modify any source file. The only file written this
  session is `docs/phase4_recon.md`.
- **Do not** run the build or tests. This recon is pure code +
  history reading.
- **Do not** propose code changes in the report — the Phase 4-impl
  prompt(s) come after, informed by the recon's verdict and split
  recommendation.
- **Do not** speculate beyond what the code shows. If Q1–Q4 don't
  have clear evidence in places, say so explicitly. "I don't know,
  but here's what I'd need to investigate further" is more useful
  than a confident guess.
- **Do not** propose deleting `findTemporalContext` itself — per
  `docs/divergence_d_recon.md`, the canonical path uses it for
  seeding. Phase 4 moves the seeding pattern into `analyzeSection`'s
  body; the helper survives. If the recon surfaces a tempting
  argument to remove it, reject — cite the divergence D recon.
- **Do not** confuse `ChordTemporalContext` (the struct being
  audited in Q1) with `ChordTemporalExtensions` (the struct created
  in Phase 3c on `AnalyzedRegion` to hold the 5 migrated fields).
  Different types; different lifetimes; the latter is canonical
  going forward.
