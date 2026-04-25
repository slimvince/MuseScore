# Policy #2 — Coalescing Divergence Map

Date: 2026-04-24  
Scope: read-only analysis; no source edits.

---

## Closed divergences

| Divergence | Closed by | Notes |
|---|---|---|
| **B — Jazz-path suppression** (`forceClassicalPath`) | 02e3733afb (production) + 69716deead (tools) | The Jazz path and `forceClassicalPath` flag are deleted. All paths now use the single classical §4.1c Jaccard path; boundary divergence between P2 and P1/P3 on Jazz scores is eliminated by removing the Jazz path entirely. |
| **D — Tick-regional post-region re-analysis** (display-context re-`analyzeChord`) | Phase 3c commit (recon at d35f003aa2) | The display-context re-analysis in P3 (`collectRegionTones` + `findTemporalContext` + second `analyzeChord` re-run) is deleted. P3 now consumes `AnalyzedSection` via `analyzeSection()`, identical to the per-region pipeline used by P2. Extension fields and alternatives are now consistent across P2 and P3. |

---

## Q1 — The Coalescing Surface

All region merging, gap-filling, and key-smoothing is encapsulated in
`prepareUserFacingHarmonicRegions` (`notationcomposingbridgehelpers.cpp:1575`).
Its internal passes, in execution order:

### Pass 0 — Raw boundary detection

Delegated to `analyzeHarmonicRhythm(Smoothed)` (`notationharmonicrhythmbridge.cpp`).

**Classical path** (single path — no Jazz path, no `forceClassicalPath` flag):

| Function | Location | Role |
|---|---|---|
| `detectHarmonicBoundariesJaccard` | `notationcomposingbridgehelpers.cpp` | Jaccard distance on 1-quarter-note windows; fires boundary when ≥ threshold |
| `detectOnsetSubBoundaries` | `notationcomposingbridgehelpers.cpp` | Onset-only Jaccard within each coarse region; threshold 0.25 |
| `detectBassMovementSubBoundaries` | `notationcomposingbridgehelpers.cpp` | Fires sub-boundary on any bass PC change ≥ `minGapTicks` |

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
| Pass 0 — Jazz path (`collectChordSymbolBoundaries`) | ~~retired~~ | ~~retired~~ | ~~retired~~ | — |
| Pass 1 — `inferGapRegion` / `analyzeGapWithContext` | ✓ | ✓ | ✓ | — |
| Pass 1 — `regionSupportsGapTones` / `inferSparseGapChord` | ✓ | ✓ | ✓ | — |
| Pass 2 — same-chord merge (`appendMeasureRegion`) | ✓ | ✓ | ✓ | — |
| Pass 3 — measure-opening carry | ✓ | ✓ | ✓ | — |
| Pass 4 — key/mode stabilization | ✓ | ✓ | ✓ | — |
| `minimumDisplayDurationBeats` filter | — | ✓ | — | — |
| `forceClassicalPath=true` | ~~retired~~ | ~~retired~~ | ~~retired~~ | — |
| Post-region display re-analysis (`collectRegionTones` + `analyzeChord` re-run) | — | — | ~~retired~~ | — |
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

### Divergence B — Annotation Jazz-path suppression (**CLOSED**)

**Closed by:** 02e3733afb (production Jazz path retired) + 69716deead (tool-side
cleanup). The Jazz boundary path (`collectChordSymbolBoundaries`,
`scoreHasValidChordSymbols`) and `forceClassicalPath` flag have been deleted.
All paths — P1, P2, P3 — now use the single §4.1c Jaccard classical path.

**Historical summary:** P2 previously passed `forceClassicalPath=true` to force
Jaccard boundaries even when the score contained STANDARD chord symbols, while P1
and P3 defaulted to `forceClassicalPath=false` and would take chord-symbol
boundaries on Jazz scores. This caused boundary divergence between annotation and
implode/status-bar on any score with existing chord symbols. The fix was not to
unify the flag, but to retire the Jazz path entirely.

---

### Divergence C — Short-region silencing (P2 vs. P1/P3)

**What differs:** P2 applies `minimumDisplayDurationBeats` (default 0.5 beats,
`notationcomposingbridge.cpp:781`) after `prepareUserFacingHarmonicRegions`.
P1 and P3 have no such gate.

**Effect:** A region shorter than 0.5 beats produces a chord result in P1/P3
(implode places a note; status-bar shows a symbol) but is silently skipped in
P2 (no annotation written).

---

### Divergence D — Tick-regional post-region re-analysis (P3 vs. P1/P2) (**CLOSED**)

**Closed by:** Phase 3c implementation (see commit following `d35f003aa2`
recon report). The display-context re-analysis (`collectRegionTones` +
`findTemporalContext` + `analyzeChord` re-run) in P3 was deleted; P3 now
consumes `AnalyzedSection` (the canonical per-region pipeline output) via
`analyzeSection()`, identical to what P2 annotates.

**Historical summary:** After `prepareUserFacingHarmonicRegions`, P3 previously
re-collected tones for the matched region via `collectRegionTones`, built a
`findTemporalContext` display context, and re-ran `analyzeChord`.  P1 and P2
used `region.chordResult` directly, producing divergent extension fields and
alternative candidates on any tick not at a region boundary.

**Tie-break rule (deleted):** when the display re-analysis produced a different
formatted symbol/Roman/Nashville than `region.chordResult`, P3 prepended
`region.chordResult` so the harmonic-region winner stayed first.  This rule and
the entire display re-analysis code path are now deleted.

**Alternatives improvement:** the retired path produced degenerate inversion-noise
alternatives (e.g. 3× D-major entries at scores 2.818 / 2.563 / 2.563 in
`bach_bwv806_gigue`) because the segment-local lookback diverged from the
per-region-evolved temporal context at every non-boundary tick.  The canonical
per-region path now supplies alternatives that are harmonically distinct candidates
(confirmed via Step D snapshot diff, ~58% of sampled ticks affected).

**Recon report:** `docs/divergence_d_recon.md`, committed at `d35f003aa2`.

---

## Summary

```
                       P1 Implode  P2 Annotation  P3 Tick-regional  P4 Tick-local
prepareUserFacing          ✓            ✓               ✓               —
forceClassicalPath         retired      retired         retired         —
minimumDuration gate       —            ✓               —               —
display re-analysis        —            —               retired         —
tick-local fallback        —            —               —               ✓
```

**One live divergence** remains between paths that share `prepareUserFacingHarmonicRegions`:

- **C** (duration gate) causes annotation to silently drop sub-beat regions that
  implode and status-bar expose.

Divergences B (Jazz-path suppression) and D (display re-analysis) are **closed**:

- **B** — Jazz path and `forceClassicalPath` flag deleted in 02e3733afb + 69716deead.
  All paths share the single classical §4.1c boundary detection.
- **D** — Display-context re-analysis deleted in Phase 3c (recon at d35f003aa2).
  P3 now consumes `analyzeSection()` output, consistent with P2.

**Highest priority:** Divergence C — a unified boundary source (shared pre-computed
regions passed to all callers) would resolve it and complete pipeline unification.
