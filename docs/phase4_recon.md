# Phase 4 — HarmonicRegion Retirement Recon

Date: 2026-04-25
Scope: read-only, no source edits.

## Recommended implementation shape

**Two sessions (4a + 4b)** — detectCadences/detectPivotChords conversion is
mechanical and logically self-contained (4a); retiring `prepareUserFacingHarmonicRegions`
and inlining Passes 0–4 into `analyzeSection` is larger but still mechanical
conversion (4b).  `analyzeSection` stays in the bridge (correct layering for
`Score*`-dependent code); the file move to composing is deferred to a future
4c requiring interface redesign.

---

## Q1 — ChordTemporalContext residual

### Field inventory

Struct definition: `src/composing/analysis/chord/chordanalyzer.h:484`

| Field | Type | Default | Writer | Readers |
|---|---|---|---|---|
| `previousRootPc` | `int` | `-1` | `findTemporalContext` (helpers.cpp:1553) | `analyzeChord` continuity scoring |
| `previousQuality` | `ChordQuality` | `Unknown` | same | same |
| `previousBassPc` | `int` | `-1` | same | stepwise-bass detection |
| `bassIsStepwiseFromPrevious` | `bool` | `false` | `findTemporalContext` (helpers.cpp:1563) + harmony bridge | `analyzeChord` inversion bias (§4.1b) |
| `bassIsStepwiseToNext` | `bool` | `false` | harmonicrhythmbridge per-region loop | `analyzeChord` inversion bias |

Five fields total.  Three dead fields were deleted in Phase 2; these five are
all active.

### Coupling analysis

The five fields form a single coherent concept: **the previous-chord context
the chord analyzer needs to disambiguate the current sonority** (root
continuity, inversion resolution via stepwise bass).  This is the analyzer
INPUT surface.  It is completely separate from `ChordTemporalExtensions`
(harmonicrhythm.h:40–46), which is the OUTPUT snapshot read by emitters after
analysis.

Phase 3c created `ChordTemporalExtensions` as a parallel output struct
mirroring all five fields, plus `toExtensionsSnapshot()` (harmonicrhythm.h:50)
to copy from input to output.  The invariant is:

```
ChordTemporalContext  →  analyzeChord()  →  stored in HarmonicRegion.temporalExtensions
     (input)                                 (ChordTemporalExtensions, output)
```

### Recommended fate

**(b) Rename and keep** — but not in Phase 4.

`ChordTemporalContext` is NOT being retired.  Phase 4 does not touch it.  The
struct survives as the chord-analyzer input; only `HarmonicRegion` (the results
carrier) is being retired.

A future rename to something like `ChordAnalysisInputContext` would align with
the docstring note at chordanalyzer.h:482 ("A future TemporalContext struct
(planned for analysis/temporal/) will accumulate full progression context").
That rename is cosmetic and belongs after Phase 4 when the analysis pipeline is
stable.

**Consumers that would need updating on rename:** `findTemporalContext`
signature and body (helpers.cpp:1511–1570), all call sites in
notationharmonicrhythmbridge.cpp (lines 213–214, 393, 542, 674–675), the
`ChordTemporalContext subCtx` locals (harmonicrhythmbridge.cpp:393, 542).

---

## Q2 — HarmonicRegion consumer sweep

### Full reference list

| File | Lines | Classification |
|---|---|---|
| `src/composing/analysis/region/harmonicrhythm.h` | 69–78 | **Struct definition** (HarmonicRegion); also defines ChordTemporalExtensions and toExtensionsSnapshot |
| `src/composing/analyzed_section.h` | 34, 56–57 | Comment references only — no code |
| `src/notation/internal/notationanalysisinternal.h` | 101–126 | **Debug infrastructure** — `HarmonicRegionDebugCapture` struct + `ScopedHarmonicRegionDebugCapture` RAII + thread-local get/set |
| `src/notation/internal/notationcomposingbridge.h` | 39, 51, 122, 127 | **Type-only**: include of harmonicrhythm.h; `HarmonicRegionGranularity` enum (NOT the struct); `analyzeHarmonicRhythm` signature |
| `src/notation/internal/notationcomposingbridge.cpp` | 704, 839–873 | **1:1 adapter** in `emitAnnotation` — converts `AnalyzedRegion` → `HarmonicRegion` to call detectCadences/detectPivotChords |
| `src/notation/internal/notationcomposingbridgehelpers.h` | 204–208, 266, 283 | **Signatures**: `prepareUserFacingHarmonicRegions`, `detectCadences`, `detectPivotChords` |
| `src/notation/internal/notationcomposingbridgehelpers.cpp` | 246–311, 1573–2082, 2092–2290 | **Main body**: `stabilizeHarmonicRegionsForDisplay`; all of `prepareUserFacingHarmonicRegions` (Passes 0–4); `detectCadences`; `detectPivotChords`; thin `analyzeSection` delegate |
| `src/notation/internal/notationharmonicrhythmbridge.cpp` | 98–806 | **Primary producer** — `analyzeHarmonicRhythm` returns `vector<HarmonicRegion>` |
| `src/notation/internal/notationimplodebridge.cpp` | 1282–1298 | **1:1 adapter** in `emitImplodedChordTrack` — same pattern as notationcomposingbridge.cpp |
| `src/notation/tests/notationannotate_tests.cpp` | 66–77, 92–406 | **Direct construction** — `HarmonicRegion region(...)` factory at line 67; all test vectors build `HarmonicRegion` instances to drive detectCadences/detectPivotChords |
| `src/notation/tests/notationimplode_tests.cpp` | 365–413 | **Test helper** — `normalizePopulatedRegionStarts(vector<HarmonicRegion>&)` — measure-aligned normalization logic not shipped to production |
| `src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp` | 134, 285, 299–315, 364, 418, 454, 695 | **Direct caller** of `prepareUserFacingHarmonicRegions`; helper functions `regionToImplodeEntry`, `regionContaining` typed on `HarmonicRegion` |
| `tools/batch_analyze.cpp` | 1784, 1820, 1845–1881 | **Active consumer** (classical path) — calls `prepareUserFacingHarmonicRegions` (line 1881) and uses `HarmonicRegionDebugCapture`/`ScopedHarmonicRegionDebugCapture` (1849–1853) |

### Classification notes

**Passive carriers** (trivial swap for AnalyzedRegion): the two 1:1 adapters in
notationcomposingbridge.cpp and notationimplodebridge.cpp; all pass logic in
`prepareUserFacingHarmonicRegions`; `stabilizeHarmonicRegionsForDisplay`.
These access only fields that exist identically on `AnalyzedRegion`.

**Structural fixtures** (not passive — need real update):
- `notationannotate_tests.cpp` constructs `HarmonicRegion` directly to drive
  detectCadences/detectPivotChords.  When 4a converts those functions to take
  `AnalyzedRegion`, every test vector must be retyped.  The construction helper
  at line 67 (`HarmonicRegion region(...)`) becomes `AnalyzedRegion region(...)`.
  This is mechanical but file-wide.
- `pipeline_snapshot_tests.cpp` calls `prepareUserFacingHarmonicRegions` directly
  and has `HarmonicRegion`-typed helpers.  Phase 4b must port these to
  `analyzeSection`.

**Out-of-scope consumer** (tool-side, per UAP doc):
- `tools/batch_analyze.cpp` — calls `prepareUserFacingHarmonicRegions` and
  uses `HarmonicRegionDebugCapture`.  The Jazz-path retirement (02e3733afb +
  69716deead) removed `analyzeScoreJazz` and `injectWrittenRootTone` but left
  the classical-path references intact.  Phase 4b MUST surface a tool-side
  decision before retiring `prepareUserFacingHarmonicRegions` — see Q5.

**Is the consumer surface what we thought?** Mostly yes, plus:
1. `tools/batch_analyze.cpp` classical-path references (not cleaned by Jazz retirement)
2. `notationimplode_tests.cpp` — `normalizePopulatedRegionStarts` test helper
3. `HarmonicRegionDebugCapture` debug infrastructure — survives unless we redesign it

The hidden consumers change Phase 4b's scope somewhat (test-file and tool-file
impact) but not its risk profile.

---

## Q3 — Pass 0–4 dependency depth on HarmonicRegion

The passes live entirely inside `prepareUserFacingHarmonicRegions`
(helpers.cpp:1573–2082) plus `stabilizeHarmonicRegionsForDisplay`
(helpers.cpp:246–311).

### Pass 0 — boundary detection (analyzeHarmonicRhythm)

`analyzeHarmonicRhythm` is in `notationharmonicrhythmbridge.cpp:98–806`.  It
returns `vector<HarmonicRegion>` and is called at helpers.cpp:1586.

`HarmonicRegion` fields it populates: all six (`startTick`, `endTick`,
`chordResult`, `alternatives`, `hasAnalyzedChord`, `keyModeResult`, `tones`,
`temporalExtensions`).

Conversion strategy for Phase 4b: `analyzeSection` calls `analyzeHarmonicRhythm`
unchanged, then does a one-time 1:1 translation of the returned
`vector<HarmonicRegion>` to `vector<AnalyzedRegion>` at the boundary — the same
translation the current `analyzeSection` body does at helpers.cpp:2323–2336
(minus `hasAssertiveExposure` and `keyAreaId`, which get filled by
`analyzeSection` anyway).  `analyzeHarmonicRhythm` keeps its current return
type; `HarmonicRegion` survives as an implementation detail of Pass 0.

Verdict: **mechanical**.

### Pass 1 — gap-tone region insertion

Lambdas: `regionSupportsGapTones`, `applyGapKeyContext`, `inferSparseGapChord`,
`analyzeGapWithContext`, `inferGapRegion`, `carryGapRegion`.

`HarmonicRegion` fields touched during construction of gap regions:
`startTick`, `endTick`, `hasAnalyzedChord`, `keyModeResult`, `tones`,
`chordResult`, `alternatives`.  All present on `AnalyzedRegion`.

The "temporalExtensions stays at defaults for gap regions" is already handled by
a code comment at helpers.cpp:1797: *"Gap analyzer is invoked context-free;
temporalExtensions stays at defaults."*  With `AnalyzedRegion`, the same
default holds (`ChordTemporalExtensions{}`).

`std::optional<HarmonicRegion>` return types of `inferGapRegion` and
`analyzeGapWithContext` become `std::optional<AnalyzedRegion>` — search-and-
replace.

Verdict: **mechanical**.

### Pass 2 — within-measure same-chord merge (appendMeasureRegion)

`sameChordIdentity` reads `lhs/rhs.chordResult.identity.rootPc` and `.quality`.
`appendMeasureRegion` reads `.startTick`, `.endTick`, calls
`mergeChordAnalysisTones(back.tones, region.tones)` — all field-compatible.

`std::vector<HarmonicRegion> measureRegions` becomes `std::vector<AnalyzedRegion>`.
`std::optional<HarmonicRegion> previousDisplayRegion` becomes `optional<AnalyzedRegion>`.

Verdict: **mechanical**.

### Pass 3 — measure-opening carry (helpers.cpp:2060–2073)

```cpp
HarmonicRegion carriedMeasureOpening = measureRegions[1];
carriedMeasureOpening.startTick = measureStartTick;
carriedMeasureOpening.tones = collectRegionTones(...);
measureRegions[0] = std::move(carriedMeasureOpening);
```

Fields accessed: `.tones`, `.startTick`, `distinctPitchClassCount`.  All
present on `AnalyzedRegion`.  Type substitution is the only change.

Verdict: **mechanical**.

### Pass 4 — key/mode stabilization (stabilizeHarmonicRegionsForDisplay, helpers.cpp:246–311)

Fields accessed (read + write):
- `regions[i].keyModeResult.keySignatureFifths` / `.mode` — present on AnalyzedRegion
- `region.chordResult.function.degree` / `.keyTonicPc` / `.keyMode` / `.diatonicToKey` — present
- `region.chordResult.identity.rootPc` — present
- `region.tones` — present

Parameter change: `vector<HarmonicRegion>&` → `vector<AnalyzedRegion>&`.

No mutable-in-place assumptions are broken; `AnalyzedRegion` fields are value
types with no hidden invariants.

Verdict: **mechanical**.

### Summary

All five passes are **mechanical conversions**.  No pass makes type-specific
assumptions that differ between `HarmonicRegion` and `AnalyzedRegion`.
No pass is genuinely blocked.

One structural note: `HarmonicRegion` is NOT deleted from the codebase by
Phase 4b.  `analyzeHarmonicRhythm` continues to return it.  Phase 4b retires
`HarmonicRegion` from the public bridge-helper API
(`prepareUserFacingHarmonicRegions`, `detectCadences`, `detectPivotChords`)
and from the pass logic, but the struct remains as an implementation detail of
Pass 0.  Full codebase deletion of `HarmonicRegion` would require changing
`analyzeHarmonicRhythm`'s return type — a larger change that would be its own
session after Phase 4b.

---

## Q4 — analyzeSection move to composing — feasibility

### Current access pattern

`analyzeSection` (helpers.cpp:2302–2369) takes:
- `const mu::engraving::Score* sc`
- `const mu::engraving::Fraction& from`
- `const mu::engraving::Fraction& to`
- `const std::set<size_t>& excludeStaves`

It calls `prepareUserFacingHarmonicRegions`, which calls:
- `analyzeHarmonicRhythm(sc, ...)` — engraving `Score*`
- `sc->tick2measure(startTick)` — engraving `Score*`
- `measure->tick()`, `measure->nextMeasure()` — engraving `Measure*`
- `collectRegionTones(sc, ...)` — bridge helper taking `Score*`
- `mu::engraving::Constants::DIVISION` — engraving constant
- `mu::engraving::Fraction::fromTicks()` — engraving Fraction

`findTemporalContext` (helpers.cpp:1512) takes `Score*` and `Segment*`.  It
lives in `notationcomposingbridgehelpers.h/cpp` (bridge layer).

### Layering picture

`composing_analysis` CMakeLists.txt (analysis/CMakeLists.txt): `NO_QT`, no
engraving link.  Explicitly designed to be engraving-independent via the
tick-integer convention (harmonicrhythm.h:34: *"so that this header stays free
of the engraving Fraction include"*).

`composing` CMakeLists.txt: links `composing_analysis`, `muse_global`,
`intonation` — no engraving link.

Moving `analyzeSection` with its `Score*` parameter to either `composing` or
`composing_analysis` would require adding `engraving` as a link-time dependency
— a deliberate violation of the current architecture.

The comment at helpers.cpp:2299–2301 states the design intent explicitly:
*"Keeping it here today preserves the correct dependency direction (bridge
depends on composing, not the reverse)."*

### Seeding-pattern requirement

`findTemporalContext` is called at notationharmonicrhythmbridge.cpp:213–214
(the canonical seeding call for the regional-accumulation path) and also at
harmonicrhythmbridge.cpp:674–675 (dense-boundary path).  These calls are
**inside `analyzeHarmonicRhythm`**, not inside `prepareUserFacingHarmonicRegions`.
Therefore retiring `prepareUserFacingHarmonicRegions` does NOT move the seeding
pattern — it stays inside `analyzeHarmonicRhythm`, which continues to be called
by `analyzeSection`.

The divergence D recon note (commit d35f003aa2) that the seeding pattern
"moves into analyzeSection's body" refers to the longer-term vision where
`analyzeHarmonicRhythm`'s per-tick logic is also inlined.  This is not
required for Phase 4b.

### Feasibility verdict

**(c) Move requires layering rework** — if the `Score*` interface is preserved.

**(b) Move requires intermediate types** — if `analyzeSection`'s interface is
redesigned to take pre-extracted note data (tick-indexed tone lists, etc.)
instead of `Score*`.  This is a real refactor and would require the composing
module to define a stable extraction-result type that the bridge fills and the
composing-side entry point consumes.

**For Phase 4, the pragmatic path is:** `analyzeSection` stays in the bridge
(correct layering), becomes the canonical entry point by inlining Passes 0–4,
and the file move is deferred to a future phase (4c or beyond) with an explicit
interface-redesign step.  This achieves the primary Phase 4 goal — retiring
`prepareUserFacingHarmonicRegions` — without violating the composing/engraving
boundary.

---

## Q5 — Synthesis and Phase 4 implementation shape

### Recommended split: 2 sessions (4a + 4b)

#### Session 4a — Convert detectCadences/detectPivotChords

**Scope:**
- Change `detectCadences` and `detectPivotChords` signatures in
  `notationcomposingbridgehelpers.h/cpp` from `vector<HarmonicRegion>` to
  `vector<AnalyzedRegion>` (or `AnalyzedSection` + count).
- Drop the 1:1 adapter in `notationcomposingbridge.cpp:846–856` (emitAnnotation
  path).
- Drop the 1:1 adapter in `notationimplodebridge.cpp:1282–1298`
  (emitImplodedChordTrack path).
- Update `notationannotate_tests.cpp` — retype all `HarmonicRegion` construction
  to `AnalyzedRegion` (factory helper at line 67 + every test vector).

**What does NOT change:** `prepareUserFacingHarmonicRegions`, `analyzeSection`,
all pass logic, any other file.

**Dependency order:** 4a can start immediately from this recon.

**Behavior-preservation risk: LOW — mechanical conversion, byte-identity
guaranteed.** The only logic in detectCadences/detectPivotChords is arithmetic
on `chordResult.function.degree`, `keyModeResult`, and `startTick` — all fields
identical on both types.

**Sub-recon needed before 4a?** No.

---

#### Session 4b — Retire prepareUserFacingHarmonicRegions

**Scope:**
- `analyzeSection` inlines Passes 0–4 on `AnalyzedRegion` natively:
  - Calls `analyzeHarmonicRhythm` → converts result to `vector<AnalyzedRegion>`
    (1:1 translation, same as current helpers.cpp:2323–2336).
  - Inlines the Pass 1–4 lambdas and logic from
    `prepareUserFacingHarmonicRegions`, operating on `AnalyzedRegion`.
  - `stabilizeHarmonicRegionsForDisplay` parameter becomes `vector<AnalyzedRegion>&`.
  - The key-area grouping and `hasAssertiveExposure` assignment (current
    analyzeSection body) folds into the same function.
- `prepareUserFacingHarmonicRegions` is deleted (or kept as a deprecated shim
  — see tool-side note below).
- Update `pipeline_snapshot_tests.cpp` — port to `analyzeSection` instead of
  `prepareUserFacingHarmonicRegions`.

**Tool-side decision required before 4b can complete:**
`tools/batch_analyze.cpp` calls `prepareUserFacingHarmonicRegions` directly
(line 1881) and uses `HarmonicRegionDebugCapture` (lines 1849–1853).  Per the
unified analysis pipeline doc (*"If any implementation step surfaces a
tool-side impact, pause and surface for decision"*), Phase 4b must not proceed
to full deletion of `prepareUserFacingHarmonicRegions` without an explicit
decision on one of:
- **(a) Keep a thin shim** — `prepareUserFacingHarmonicRegions` stays as a
  deprecated wrapper that calls `analyzeSection` and translates back.  Cleanly
  isolates tool-side update to a future session.
- **(b) Update batch_analyze.cpp** — port to `analyzeSection` in this session.
  Simple but expands scope into `tools/`.
- **(c) Remove the batch_analyze classical path** — if the tool's use of
  `prepareUserFacingHarmonicRegions` is superseded by `analyzeSection`.
  Requires verifying tool-side impact is acceptable.

Recommendation: option (a) — shim first, port tools in a follow-on.

**Behavior-preservation risk: MEDIUM — large code volume (~500 lines of pass
logic rewritten), but byte-identity expected.** The snapshot test suite is the
primary safety net and must be run before and after.

**Not in scope for 4b:**
- Moving `analyzeSection` to the composing module (Q4 verdict: deferred)
- Changing `analyzeHarmonicRhythm`'s return type (HarmonicRegion survives
  there as an implementation detail)
- Full deletion of `HarmonicRegion` from the codebase

**Sub-recon needed before 4b?** No architectural unknowns block it.  The
tool-side decision (shim vs. update) is a product decision, not a code-reading
question; surface it at session start rather than spinning up a formal sub-recon.

---

### `analyzeSection` move — deferred (potential 4c)

Requires redesigning the `analyzeSection` interface away from `Score*` before
the composing module can host it.  This is a real refactor (position b of Q4):
define a bridge-side extraction step that produces a tick-indexed note-data
structure, pass it to a composing-side analysis function.  The engraving
boundary constraint (`NO_QT`, no engraving link in composing_analysis) must be
respected.  Defer until Phase 4b is validated and the interface design can be
given proper attention.

---

### Dependency order

```
[This recon] → 4a (detectCadences/detectPivotChords) → 4b (retire prepareUserFacing...)
                                                           ↓
                                                    [Tool-side decision at 4b start]
                                                    [Potential 4c: analyzeSection move]
```

4a has no blocker.  4b depends on 4a (avoids double conversion in two places).

### Behavior-preservation risk summary

| Chunk | Risk | Evidence |
|---|---|---|
| 4a — detectCadences/detectPivotChords | **Low** | Pure type substitution; logic unchanged; test-covered |
| 4b — retire prepareUserFacing | **Medium** | ~500 lines rewritten; byte-identity expected; verify with snapshot suite |
| 4c — analyzeSection move | **Medium** | Interface redesign required; architectural decision |

No chunk falls into "logic actually changes, byte-identity not expected."  The
analysis logic is preserved verbatim; only the type signatures change.

---

## Appendix — files that will change in each session

**4a:**
- `src/notation/internal/notationcomposingbridgehelpers.h` — detectCadences/detectPivotChords signatures
- `src/notation/internal/notationcomposingbridgehelpers.cpp` — detectCadences/detectPivotChords implementations
- `src/notation/internal/notationcomposingbridge.cpp` — drop 1:1 adapter (lines 846–856, 873)
- `src/notation/internal/notationimplodebridge.cpp` — drop 1:1 adapter (lines 1282–1298)
- `src/notation/tests/notationannotate_tests.cpp` — retype all HarmonicRegion test vectors

**4b:**
- `src/notation/internal/notationcomposingbridgehelpers.cpp` — inline Passes 0–4 into analyzeSection; retire or shim prepareUserFacingHarmonicRegions; stabilizeHarmonicRegionsForDisplay retypes parameter
- `src/notation/internal/notationcomposingbridgehelpers.h` — retire or shim prepareUserFacingHarmonicRegions declaration
- `src/notation/tests/pipeline_snapshot_tests/pipeline_snapshot_tests.cpp` — port to analyzeSection
- `src/notation/tests/notationimplode_tests.cpp` — normalizePopulatedRegionStarts helper retypes

**Not touched by 4a or 4b (survives):**
- `src/composing/analysis/region/harmonicrhythm.h` — HarmonicRegion struct stays (analyzeHarmonicRhythm's return type)
- `src/notation/internal/notationharmonicrhythmbridge.cpp` — analyzeHarmonicRhythm stays unchanged
- `src/notation/internal/notationanalysisinternal.h` — HarmonicRegionDebugCapture (used by batch_analyze; survives at least through shim phase)
- `src/composing/analysis/chord/chordanalyzer.h:484` — ChordTemporalContext stays unchanged
- `tools/batch_analyze.cpp` — out of scope per UAP doc; shim keeps it working
