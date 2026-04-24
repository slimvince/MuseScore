# Unified Analysis + Emission Pipeline

Date: 2026-04-24
Status: Draft — Phase 0 design, pre-implementation.
Predecessors: `docs/policy2_coalescing_map.md` (divergences A/C/D still
open after Jazz retirement), project memory
`project_unified_analysis_pipeline.md`.

## Problem

Four user-facing paths currently share `prepareUserFacingHarmonicRegions`
but diverge in two remaining ways after the Jazz-path retirement
(02e3733afb + 69716deead):

- **Divergence C** — annotation (P2) applies
  `minimumDisplayDurationBeats = 0.5` after shared analysis; implode (P1)
  and tick-regional (P3) do not. Sub-beat regions appear in the chord
  track and status bar but are silently dropped from Roman numeral
  annotation.
- **Divergence D** — tick-regional (P3) re-runs `analyzeChord` with a
  display-context `ChordTemporalContext` built from the final region
  list. This can populate temporal-context extension fields (e.g.
  `bassIsStepwiseFromPrevious`) differently than what annotation (P2)
  saw when it wrote earlier.

Beyond the divergences, structural duplication persists between implode's
`populateChordTrack` and annotation's `addHarmonicAnnotationsToSelection`:
cadence detection, chord formatting, `hasAssertiveExposure` computation.
Each drifts independently.

Modulation-aware Roman numeral annotation ("V of V in the mediant")
cannot be implemented cleanly against the current architecture because
key boundaries are not a first-class output — they exist only as
`keyModeResult` fields on individual regions, post-stabilization
smoothed but never explicitly grouped into key areas.

## Goals

- Single shared analysis pipeline producing per-region structured output
  consumed by thin emitters.
- Key boundaries as first-class output: consecutive same-key regions
  grouped into `KeyArea` spans.
- `hasAssertiveExposure` promoted from implode-internal computation to
  shared output field.
- Close divergence D by populating temporal-context extension fields
  inside the shared pipeline — no post-pipeline re-analysis.
- Close divergence C by making the duration gate an explicit
  annotation-emitter option with rationale, after verifying it does
  observable work on representative scores.
- Enable modulation-aware Roman numeral annotation as an
  annotation-emitter feature consuming `KeyArea` spans.

## Non-goals

- P4 (tick-local) is left parallel. Its point-in-time semantics differ
  too much from region-based analysis to force a single API without
  distortion. Two modules, documented relationship.
- LLM triage integration (`docs/llm_triage_design.md`) is a separate
  effort, unaffected by this refactor.
- New analyzer capabilities beyond what modulation-aware annotation
  requires. No new chord identification logic, no new cadence rules.
- Batch_analyze tool-side refactor. Tools retain their current classical-
  path access. If any implementation step surfaces a tool-side impact,
  pause and surface for decision — do not expand scope into `tools/`
  silently.

## Architecture

### Shared output

```cpp
struct AnalyzedRegion {
    // Identity (existing HarmonicRegion fields, unchanged semantics)
    int startTick;
    int endTick;
    ChordAnalysisResult chordResult;
    bool hasAnalyzedChord;
    KeyModeAnalysisResult keyModeResult;
    std::vector<ChordAnalysisTone> tones;

    // Promoted from implode-local state
    bool hasAssertiveExposure;

    // Populated during pipeline, not via post-hoc re-run (closes divergence D)
    ChordTemporalExtensions temporalExtensions;

    // Key-area membership (see below)
    int keyAreaId;
};

// Narrower than the analyzer-input ChordTemporalContext; holds only
// the output-facing extension fields that downstream emitters and
// status-bar display consume. Exact field set determined by Phase 2
// audit of current ChordTemporalContext usage.
struct ChordTemporalExtensions {
    bool bassIsStepwiseFromPrevious;
    bool bassIsStepwiseToNext;
    bool sameRootAsPrevious;
    // ... remaining fields determined by Phase 2 audit
};

struct KeyArea {
    int startTick;
    int endTick;
    int keyFifths;
    KeySigMode mode;
    double confidence;
    // AnalyzedRegion::keyAreaId indexes into AnalyzedSection::keyAreas.
};

struct AnalyzedSection {
    std::vector<AnalyzedRegion> regions;
    std::vector<KeyArea> keyAreas;
};
```

### Pipeline entry point

```cpp
namespace mu::composing::analysis::pipeline {

AnalyzedSection analyzeSection(
    const engraving::Score* score,
    engraving::Fraction startTick,
    engraving::Fraction endTick,
    std::set<size_t> excludeStaves,
    HarmonicRegionGranularity granularity);

}
```

Internally this wraps the existing classical-path boundary detection
plus `prepareUserFacingHarmonicRegions` pipeline (Passes 0–4), then
enriches with `hasAssertiveExposure`, temporal extensions, and
key-area grouping.

Location: `src/composing/analysis/pipeline/` (new directory). The
pipeline is pure analysis — no engraving mutation, no notation-specific
behavior. The existing `notationcomposingbridgehelpers.cpp` analysis
functions move here as the implementation core; the bridge layer
(`src/notation/internal/`) retains only the Score-to-input adapter.

### Key-area detection

Runs after Pass 4 (`stabilizeHarmonicRegionsForDisplay`) on the smoothed
region list. Algorithm:

1. Walk regions in order. A key area opens at the first region.
2. Close the current key area and open a new one when the next region's
   `(keyFifths, mode)` differs from the current key area's key AND the
   next region's `keyModeResult.normalizedConfidence` meets a threshold
   (initial proposal: 0.8, reusing the assertive-confidence constant).
3. Regions whose key disagrees with the enclosing area but don't clear
   the threshold retain their own `keyModeResult` (status-bar display
   still accurate) but are grouped into the enclosing area via
   `keyAreaId` (so the annotation emitter writes Roman numerals
   relative to the enclosing area's key, not the transient local
   disagreement).

This is a smoothing pass, not a new analyzer. It leverages existing
`keyModeResult` fields and the stabilization already done in Pass 4.
The threshold and single-region-trigger policy are initial sketches;
Phase 5 tunes empirically against representative modulating scores.

### Emitters

```cpp
// src/notation/internal/notationimplodeemitter.cpp
void emitImplodedChordTrack(
    engraving::Score* score,
    const AnalyzedSection& analyzed,
    const ImplodeEmitterOptions& opts);

// src/notation/internal/notationannotationemitter.cpp
void emitHarmonicAnnotations(
    engraving::Score* score,
    const AnalyzedSection& analyzed,
    const AnnotationEmitterOptions& opts);
```

Emitter options:

```cpp
struct ImplodeEmitterOptions {
    // All regions emit as chord-track notes; no duration filter.
    // No rendition preferences here — those live in engraving.
};

struct AnnotationEmitterOptions {
    // Divergence C resolution — see §"Divergence resolution" below.
    std::optional<double> minimumDisplayDurationBeats = 0.5;

    // Modulation-aware Roman numerals: when true, Roman numerals are
    // written relative to the enclosing KeyArea, producing modulation-
    // consistent annotation across key areas. Default true.
    bool useKeyAreaRelativeRomanNumerals = true;
};
```

### Path consolidation under the unified pipeline

| Path | Today | After refactor |
|------|-------|----------------|
| P1 Implode | `prepareUserFacingHarmonicRegions` → `populateChordTrack` | `analyzeSection` → `emitImplodedChordTrack` |
| P2 Annotation | `prepareUserFacingHarmonicRegions` → `addHarmonicAnnotationsToSelection` | `analyzeSection` → `emitHarmonicAnnotations` |
| P3 Tick-regional | `prepareUserFacingHarmonicRegions` → match region → re-run `analyzeChord` with display context | `analyzeSection` → match region → read `temporalExtensions` directly |
| P4 Tick-local | `collectSoundingAt` + `resolveKeyAndMode` + `analyzeChord` | Unchanged. Parallel module. |

## Divergence resolution

### Divergence C (duration gate)

Before retiring the 0.5-beat gate, Phase 3b must include an observation
run:

- Pick 10 representative scores with sub-beat regions (identified from
  current mismatch reports).
- Run annotation emitter with gate enabled and disabled.
- Diff the visual output and mismatch counts.

Decision rule:

- If the gate measurably reduces clutter or false annotations without
  suppressing correct ones → keep as documented emitter option (default
  0.5, settable).
- If the gate suppresses equally many correct and incorrect annotations
  → retire, either immediately in Phase 3b or folded into Phase 5.
  `minimumDisplayDurationBeats` becomes `std::nullopt` default and the
  option is removed in follow-up cleanup.

### Divergence D (post-pipeline re-analysis)

Closed by construction: `AnalyzedRegion::temporalExtensions` is
populated during the pipeline's own `analyzeChord` invocation per
region, using the already-built region list as context. P3 reads the
field directly; no second `analyzeChord` call.

Expected snapshot impact: P3 status-bar extension fields may change on
some regions. The change is documented as the correct unification;
snapshots are updated in Phase 3c.

## Migration plan

| Phase | Scope | Success gate | Snapshot impact |
|-------|-------|--------------|-----------------|
| 0 | Commit this design doc | doc pushed | none |
| 1 | Snapshot harness for P1/P2/P3/P4 on 10-score corpus subset | snapshots stored, asserted in CI | baseline established |
| 2 | Introduce `AnalyzedRegion`, `KeyArea`, `AnalyzedSection`, `analyzeSection` alongside existing types; audit `ChordTemporalContext` fields to define `ChordTemporalExtensions` | no call-site changes; unit tests cover new types; all snapshots unchanged | none |
| 3a | Convert implode to consume `AnalyzedSection` via `emitImplodedChordTrack` | implode snapshots unchanged; tests pass | none |
| 3b | Convert annotation to `emitHarmonicAnnotations`; observation run for divergence C; record decision | annotation snapshots unchanged (gate behavior preserved); C decision recorded | none |
| 3c | Convert tick-regional to read from `AnalyzedSection`; remove P3 display re-analysis | P3 status-bar snapshots may shift — documented and updated; mismatch baseline must hold | P3 extension fields may change |
| 4 | Retire `HarmonicRegion` and public `prepareUserFacingHarmonicRegions` API; update callers | no callers remain; all tests pass | none |
| 5 | Implement modulation-aware Roman numeral annotation in `emitHarmonicAnnotations` consuming `KeyArea` spans; tune key-area threshold empirically; if Phase 3b said retire divergence C, fold the retirement in here | new tests cover modulation cases; annotation snapshots shift for modulating scores | expected on modulating scores |

Each phase is one CC session, one commit, one push. Commits form a
reviewable chain.

## Test strategy

**Snapshot harness** (Phase 1): for each of 10 representative scores,
capture JSON output of P1 chord track, P2 annotation list, P3 status-bar
chord result at sampled ticks, P4 tick-local result at sampled ticks.
Corpus composition:

- 4 Bach chorales (dense SATB, strong baseline)
- 3 Classical/Romantic pieces (includes modulations, varied rhythmic
  density)
- 3 synthetic edge cases (sub-beat regions, single-voice line,
  ambiguous cadence)

Snapshots are stored in `src/composing/tests/data/pipeline_snapshots/`
and asserted byte-exact in CI. Any expected change in a phase commit
explicitly updates the snapshot file with a commit message noting what
changed and why.

**Unit tests for the pipeline itself** (Phase 2): `AnalyzedSection`
production from synthetic inputs, `KeyArea` grouping with controlled
key sequences, `ChordTemporalExtensions` population.

**Existing tests**: the 376 `composing_tests` and 53 `notation_tests`
must continue to pass at every phase boundary. Mismatch baseline
(0/135 abstract, 135/135 symbol/roman) must hold.

## Open questions

1. **`HarmonicRegionGranularity` enum** — three values (Default, Coarse,
   Smoothed) are in active use. Does `AnalyzedSection` carry granularity
   as metadata, or is the selection made at `analyzeSection` call time
   and not preserved? Proposal: pass-through only, no metadata storage.

2. **`ChordTemporalExtensions` field audit** — current
   `ChordTemporalContext` has many fields. Which are genuinely
   "output extension fields that downstream consumers read" vs
   "input state the analyzer uses"? Audit in Phase 2; goal is the
   narrowest useful output struct.

3. **Key-area confidence threshold** — initial proposal 0.8 (reuses
   assertive-confidence constant). Alternative: a lower "key change
   candidate" threshold with additional confirmation from the following
   region. Empirical check against representative modulating scores in
   Phase 5.

4. **Batch_analyze adoption** — batch_analyze stays on its own
   classical-path access. If any implementation step surfaces a
   tool-side impact (e.g. shared struct change forces a tool-side
   build break), pause and surface for decision rather than expanding
   scope into `tools/`.

5. **Roman numeral notation format for modulations** — standard
   conventions exist (e.g., `V/V` for secondary dominant in original
   key vs. `V` in target key). The modulation-aware annotation's
   output format needs a small design decision. Deferred to Phase 5
   spec.
