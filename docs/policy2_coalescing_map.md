# Policy #2 — Coalescing Divergence Map

Date: 2026-04-24  
Scope: read-only analysis; no source edits.

---

## Q1 — The Coalescing Surface

All region merging, gap-filling, and key-smoothing is encapsulated in
`prepareUserFacingHarmonicRegions` (`notationcomposingbridgehelpers.cpp:1575`).
Its internal passes, in execution order:

### Pass 0 — Raw boundary detection

Delegated to `analyzeHarmonicRhythm(Smoothed)` (`notationharmonicrhythmbridge.cpp`).

**Classical path** (no STANDARD chord symbols):

| Function | Location | Role |
|---|---|---|
| `detectHarmonicBoundariesJaccard` | `notationcomposingbridgehelpers.cpp` | Jaccard distance on 1-quarter-note windows; fires boundary when ≥ threshold |
| `detectOnsetSubBoundaries` | `notationcomposingbridgehelpers.cpp` | Onset-only Jaccard within each coarse region; threshold 0.25 |
| `detectBassMovementSubBoundaries` | `notationcomposingbridgehelpers.cpp` | Fires sub-boundary on any bass PC change ≥ `minGapTicks` |

**Jazz path** (score has STANDARD chord symbols AND `forceClassicalPath=false`):

| Function | Location | Role |
|---|---|---|
| `collectChordSymbolBoundaries` | `notationcomposingbridgehelpers.cpp` | Boundaries taken from existing STANDARD harmony ticks instead of Jaccard/onset |
| `scoreHasValidChordSymbols` | `notationcomposingbridgehelpers.cpp` | Gate predicate for the Jazz path |

### Pass 1 — Gap-tone region insertion

Executed measure-by-measure inside `prepareUserFacingHarmonicRegions`
(lines 1809–1937).  Fills score gaps left between harmonic rhythm regions.

| Lambda / Function | Lines | Role |
|---|---|---|
| `inferGapRegion` | 1809 | Top-level dispatch: collect gap tones, choose carry vs. analyze |
| `regionSupportsGapTones` | 1603 | Test whether gap tones are acoustically compatible with an adjacent region |
| `inferSparseGapChord` | 1668 | 1–2 PC gap: triad/quality inference without full `analyzeChord` |
| `analyzeGapWithContext` | 1781 | ≥3 PC gap: full `analyzeChord` using adjacent region's key/mode |
| `applyGapKeyContext` | 1636 | Stamps `degree`, `diatonicToKey`, etc. onto sparse gap results |

### Pass 2 — Within-measure same-chord merge

`appendMeasureRegion` lambda (lines 1965–1977).  Adjacent regions with
identical `rootPc + quality` that share a boundary are collapsed into one.

### Pass 3 — Measure-opening carry

Lines 2059–2072.  When a measure opens with a region of < 3 distinct PCs and
the next region within 1 beat has ≥ 3 PCs, the leading region is replaced by a
carry of the richer region.

### Pass 4 — Key/mode stabilization

`stabilizeHarmonicRegionsForDisplay` (line 2079, anonymous namespace at line 247).
Smooths transient single-region key changes: a key that appears for only one
region is preserved only if the following region confirms it, otherwise the
previous stable key is propagated forward.

---

## Q2 — Per-Path Invocation Matrix

Four user-facing analysis paths:

| # | Path | Entry point | File |
|---|---|---|---|
| P1 | **Implode** | `prepareUserFacingHarmonicRegions` direct | `notationimplodebridge.cpp:563` |
| P2 | **Annotation** | `addHarmonicAnnotationsToSelection` | `notationcomposingbridge.cpp:756` |
| P3 | **Tick-regional** | `analyzeNoteHarmonicContextRegionallyInWindow` | `notationcomposingbridge.cpp:291` |
| P4 | **Tick-local** | `analyzeHarmonicContextLocallyAtTick` | `notationcomposingbridge.cpp:218` |

P3 is reached from `addAnalyzedHarmonyToSelection` (`notationinteraction.cpp:8313`)
via `analyzeNoteHarmonicContext` → `analyzeNoteHarmonicContextDetails` →
`analyzeHarmonicContextRegionallyAtTick`.

| Coalescing element | P1 Implode | P2 Annotation | P3 Tick-regional | P4 Tick-local |
|---|:---:|:---:|:---:|:---:|
| Pass 0 — Jaccard boundary detection | ✓ | ✓ | ✓ | — |
| Pass 0 — Onset sub-boundaries | ✓ | ✓ | ✓ | — |
| Pass 0 — Bass-movement sub-boundaries | ✓ | ✓ | ✓ | — |
| Pass 0 — Jazz path (`collectChordSymbolBoundaries`) | ✓ | **suppressed** | ✓ | — |
| Pass 1 — `inferGapRegion` / `analyzeGapWithContext` | ✓ | ✓ | ✓ | — |
| Pass 1 — `regionSupportsGapTones` / `inferSparseGapChord` | ✓ | ✓ | ✓ | — |
| Pass 2 — same-chord merge (`appendMeasureRegion`) | ✓ | ✓ | ✓ | — |
| Pass 3 — measure-opening carry | ✓ | ✓ | ✓ | — |
| Pass 4 — key/mode stabilization | ✓ | ✓ | ✓ | — |
| `minimumDisplayDurationBeats` filter | — | ✓ | — | — |
| `forceClassicalPath=true` | — | ✓ | — | — |
| Post-region display re-analysis (`collectRegionTones` + `analyzeChord` re-run) | — | — | ✓ | — |
| `collectSoundingAt` (4-beat backward sweep) | — | — | — | ✓ |
| `resolveKeyAndMode` with hysteresis | — | — | — | ✓ |
| `refineSparseChordQualityFromKeyContext` | — | — | — | ✓ |

---

## Q3 — Divergence Analysis

### Divergence A — Tick-local vs. all regional paths (P4 vs. P1/P2/P3)

**What differs:** P4 collects notes via `collectSoundingAt` (walks backward up to
4 quarter notes), resolves key via `resolveKeyAndMode` with hysteresis, and runs
`analyzeChord` on the tick-local note set.  P1/P2/P3 all go through
`prepareUserFacingHarmonicRegions`, which collects notes across the entire region
window (`collectRegionTones`) and uses region-level key analysis.

**Effect:** For any given tick, P4 can produce a different root, quality, or key
than P1/P2/P3.  Short notes surrounded by a different harmonic context are the
most vulnerable case.

**Caller:** P4 is the fallback inside `analyzeHarmonicContextAtTick`
(`notationcomposingbridge.cpp:489`) when the regional path returns no results.
The tuning bridge also calls it directly.

---

### Divergence B — Annotation Jazz-path suppression (P2 vs. P1/P3 on Jazz scores)

**What differs:** P2 passes `forceClassicalPath=true`, forcing Jaccard boundaries
even when the score contains STANDARD chord symbols.  P1 and P3 use the default
`forceClassicalPath=false`, so on a Jazz score they take chord-symbol boundaries.

**Effect:** On a score with existing STANDARD harmony elements, the annotation
written by P2 may carve regions at different ticks than the status-bar tooltip
(P3) or an implode operation (P1) shows.  The annotation then *becomes* the
chord symbols that P1/P3 would use as Jazz boundaries in subsequent calls —
but P2 still ignores them on its next run.

**Rationale:** `forceClassicalPath=true` prevents an order-of-annotation
violation where chord symbols written earlier in the same command invocation
shift boundaries for later annotations.

---

### Divergence C — Short-region silencing (P2 vs. P1/P3)

**What differs:** P2 applies `minimumDisplayDurationBeats` (default 0.5 beats,
`notationcomposingbridge.cpp:781`) after `prepareUserFacingHarmonicRegions`.
P1 and P3 have no such gate.

**Effect:** A region shorter than 0.5 beats produces a chord result in P1/P3
(implode places a note; status-bar shows a symbol) but is silently skipped in
P2 (no annotation written).

---

### Divergence D — Tick-regional post-region re-analysis (P3 vs. P1/P2)

**What differs:** After `prepareUserFacingHarmonicRegions`, P3 re-collects tones
for the matched region via `collectRegionTones`, builds a `findTemporalContext`
display context, and re-runs `analyzeChord` (lines 327–354).  P1 and P2 use
`region.chordResult` directly.

**Tie-break rule (lines 372–375):** when the display re-analysis produces a
different formatted symbol/Roman/Nashville than `region.chordResult`, P3 **prepends**
`region.chordResult` so the harmonic-region winner stays first.  The status-bar
display therefore mirrors `region.chordResult` in the disagreement case.

**Residual risk:** when display re-analysis *agrees* with the region result, the
re-analysis becomes the returned `chordResults[0]`; the temporal-context
extensions (e.g. `bassIsStepwiseFromPrevious`) are populated differently than in
the region-level analysis.  Extension fields may differ between what P3 returns
and what P2 annotated.

---

## Summary

```
                       P1 Implode  P2 Annotation  P3 Tick-regional  P4 Tick-local
prepareUserFacing          ✓            ✓               ✓               —
forceClassicalPath         no           YES             no              —
minimumDuration gate       —            ✓               —               —
display re-analysis        —            —               ✓               —
tick-local fallback        —            —               —               ✓
```

**Three live divergences** exist between paths that share `prepareUserFacingHarmonicRegions`:

- **B** (Jazz-path suppression) causes different region boundaries between
  annotation and implode/status-bar on Jazz scores.
- **C** (duration gate) causes annotation to silently drop sub-beat regions that
  implode and status-bar expose.
- **D** (display re-analysis) means status-bar temporal-context fields can differ
  from annotation output even when the top-level chord identity matches.

**Highest priority:** Divergence B — on Jazz scores the annotation writes different
Roman numerals than the status-bar shows for the same tick.  A unified boundary
source (shared pre-computed regions passed to all callers) would resolve B, C, and D.
