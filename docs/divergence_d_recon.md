# Divergence D — Display-Context Analysis Recon

Date: 2026-04-25
Scope: read-only, no source edits.
Audience: next session planning Phase 3c-impl.

## Verdict

**(α) Cruft, with a vestigial-but-now-active dual purpose.**

The display-context `analyzeChord` call inside P3 (`notationcomposingbridge.cpp:298`)
predates `prepareUserFacingHarmonicRegions` by ~12 days. It is the
*original* tick-local-style analysis from `70e679e819` ("chord staff in
place", 2026-03-31); the per-region pipeline was bolted in alongside on
2026-04-12 (`2e152d50e7`), and the prepend tie-break
(`notationcomposingbridge.cpp:319-322`) exists *only* to reconcile the
new canonical region winner with the legacy display-context output.
`findTemporalContext` does nothing the per-region pipeline doesn't
already do at its seed step (`notationharmonicrhythmbridge.cpp:213-214`)
— in fact the per-region pipeline calls `findTemporalContext` itself.
Test coverage on the disagreement case is zero; tests force
`setAnalysisAlternatives(1)` which short-circuits the multi-element
shape entirely.

The wrinkle: production default is `ANALYSIS_ALTERNATIVES = 3`
(`composingconfiguration.cpp:102`) and the `chordResults[1..N]` tail is
consumed by two real UI surfaces — status-bar text
(`notationcomposingbridge.cpp:501-611`) and right-click menu
(`notationcontextmenumodel.cpp:55-151`). Those alternatives currently
come from the cruft path. So while the *primary* output is genuinely
cruft, the *alternatives vector* is load-bearing UX that needs to land
somewhere when the cruft path is removed.

## Q1 — Origin archaeology

| Function | Introduced | One-line intent |
|---|---|---|
| `findTemporalContext` (helpers) | `70e679e819` (2026-03-31) "chord staff in place" | Original tick-local context construction |
| `collectRegionTones` (helpers) | `70e679e819` (2026-03-31) "chord staff in place" | Original tick-local tone collection |
| Display-context `analyzeChord` call in P3 | `70e679e819` (2026-03-31) — see [notationcomposingbridge.cpp:298](src/notation/internal/notationcomposingbridge.cpp#L298) blamed to `2e152d50e7` after refactor | Originally **was** the P3 path; not a layered-on second opinion |
| `prepareUserFacingHarmonicRegions` (helpers, line 1574) | `2e152d50e7` (2026-04-12) "WIP: notation test additions and docs" | Per-region pipeline — added later, replaced primary path |
| Per-region `analyzeChord` invocation ([notationharmonicrhythmbridge.cpp:273](src/notation/internal/notationharmonicrhythmbridge.cpp#L273)) | First introduced `a3ac7b00cf` (2026-04-05) "wip: add harmonic rhythm analysis"; current shape from `2e152d50e7` | Canonical per-region call |
| Tie-break prepend ([notationcomposingbridge.cpp:319-322](src/notation/internal/notationcomposingbridge.cpp#L319-L322)) | `2e152d50e7` (2026-04-12) | Reconciles legacy display-context call with new region winner |

**Timeline narrative.** `70e679e819` (Mar 31, "chord staff in place")
introduced both `findTemporalContext` and `collectRegionTones` as
helpers for the original tick-local-style P3. At that point P3 was the
*only* path: take the user's segment, collect sounding tones, run
`analyzeChord`, return the up-to-3 candidates as `chordResults`. The
status-bar and right-click submenu were designed against that vector
shape from day one.

Mid-April brought the per-region pipeline: `a3ac7b00cf` (Apr 5) added
`analyzeHarmonicRhythm`; `c7ea8f49f5` (Apr 11) added
`prepareUserFacingHarmonicRegions`; `2e152d50e7` (Apr 12) refactored P3
into `analyzeNoteHarmonicContextRegionallyInWindow` — calling
`prepareUserFacingHarmonicRegions` first (new canonical path), but
*keeping* the original `findTemporalContext` + `collectRegionTones` +
`analyzeChord` block alongside, with the prepend tie-break to keep
region-winner first when the two disagreed. The display-context call
was never re-justified — it just survived the refactor by inertia.

`refreshChordResultWithDisplayContext` was a brief intermediate
factoring (`4e2ee4cc34`) deleted as dead code (`ff1780d911`); doesn't
affect the verdict.

## Q2 — Input comparison

For any region in `[regionStart, regionEnd)`:

| Aspect | Per-region call ([rhythmbridge.cpp:273](src/notation/internal/notationharmonicrhythmbridge.cpp#L273)) | P3 display-context call ([bridge.cpp:298](src/notation/internal/notationcomposingbridge.cpp#L298)) |
|---|---|---|
| Tone collection function | `collectRegionTones(score, regionStart, regionEnd, excludeStaves)` ([rhythmbridge.cpp:226](src/notation/internal/notationharmonicrhythmbridge.cpp#L226)) | `collectRegionTones(score, it->startTick, it->endTick, excludeStaves)` ([bridge.cpp:274](src/notation/internal/notationcomposingbridge.cpp#L274)) |
| Window | `[regionStart, regionEnd)` of the matched region | Same — `it->startTick`/`it->endTick` are the per-region pipeline's outputs |
| Exclude-staves | Same `excludeStaves` set | Same |
| Key context | `localKeyFifths` from per-region `resolveKeyAndMode` ([rhythmbridge.cpp:268](src/notation/internal/notationharmonicrhythmbridge.cpp#L268)) | `it->keyModeResult.keySignatureFifths` (same value, just read from the region) |
| Temporal context | Evolving `temporalCtx` whose `previous*` fields = analysis result of the *previous region* in the boundary list ([rhythmbridge.cpp:286-288](src/notation/internal/notationharmonicrhythmbridge.cpp#L286-L288)) | Fresh `findTemporalContext(sc, seg, ...)` whose `previous*` fields = `analyzeChord` of `collectSoundingAt` at the *segment immediately before the user's clicked tick* ([helpers.cpp:1526-1559](src/notation/internal/notationcomposingbridgehelpers.cpp#L1526-L1559)) |
| `bassIsStepwiseFromPrevious` | Computed from prev-region bass vs. current-region bass | Computed in `findTemporalContext` from previous-segment bass vs. `currentBassPc` (passed in as `it->chordResult.identity.bassPc`) |
| `bassIsStepwiseToNext` | Computed via lookahead `collectRegionTones` on next region ([rhythmbridge.cpp:243-262](src/notation/internal/notationharmonicrhythmbridge.cpp#L243-L262)) | Not populated — `findTemporalContext` comment at [helpers.cpp:1567-1568](src/notation/internal/notationcomposingbridgehelpers.cpp#L1567-L1568) defers this to "two-pass chord staff analysis only" |

**Same input collection function. Same window. Same key. Different
definition of "previous" for the temporal context, and the
display-context call is *strictly less* informed (no
`bassIsStepwiseToNext`, no evolving multi-region history).** The
per-region call sees more context, computed from already-analyzed
neighboring regions. The display-context call sees one segment of
backward lookback derived from raw score data.

For the user's chord-identification purposes, those temporal-context
deltas affect `analyzeChord`'s root-continuity bonus and contextual
inversion resolution scoring (`chordanalyzer.cpp:1358-1407`). When the
user clicks **inside** a region (not at the start), the
display-context call's "previous" is the segment one step back inside
the same region — which is usually the same chord as the current
region, so its `previous*` fields collapse to "same root, same
quality" — feeding a different bonus pattern than the per-region call,
which sees the actual previous region's chord.

## Q3 — `findTemporalContext` semantics

[`findTemporalContext`](src/notation/internal/notationcomposingbridgehelpers.cpp#L1511-L1571):

1. Walk backward from `seg` segment-by-segment looking for a chord
   attack on any non-excluded eligible staff
   ([helpers.cpp:1526-1541](src/notation/internal/notationcomposingbridgehelpers.cpp#L1526-L1541))
2. On first hit, call `collectSoundingAt(sc, s, ...)` — the
   tick-local collector with 4-quarter backward sweep
3. Run `analyzeChord(prevTones, keyFifths, keyMode)` **with no
   temporal context pointer** ([helpers.cpp:1551](src/notation/internal/notationcomposingbridgehelpers.cpp#L1551))
4. Stamp `previousRootPc/Quality/BassPc` from `front()` result
5. Compute `bassIsStepwiseFromPrevious` against the caller-supplied
   `currentBassPc`
6. Explicitly skip `nextRootPc/nextBassPc/bassIsStepwiseToNext` —
   comment at [helpers.cpp:1567-1568](src/notation/internal/notationcomposingbridgehelpers.cpp#L1567-L1568)
   defers them to "two-pass chord staff analysis only"

**What Pass 0–4 already does that this duplicates.** The per-region
pipeline calls `findTemporalContext` itself at
[`rhythmbridge.cpp:213-214`](src/notation/internal/notationharmonicrhythmbridge.cpp#L213-L214)
to seed `temporalCtx` for the very first region (with
`currentBassPc=-1`). After the seed, the pipeline updates
`temporalCtx.previous*` from each region's *analyzed* result rather
than calling `findTemporalContext` per region — which is strictly
better information than `findTemporalContext` produces (it uses the
already-completed region analysis, not a context-free re-analysis of
raw score data).

So `findTemporalContext` itself is fine — it's the *seed function* for
the per-region pipeline. The cruft is calling it *again* from P3 for
display-context construction, when the per-region pipeline has
already done strictly better temporal-context tracking and the
result is sitting on `it->chordResult`'s neighbors.

**No flags or branches inside `findTemporalContext` suggest it was
added for a specific edge case.** The function is straightforward:
nearest-prior-segment lookback, single `analyzeChord` call, copy out
three fields. It doesn't do anything Pass 0–4 doesn't already do
better.

## Q4 — Test coverage

**Production default for `analysisAlternatives`: 3**
([composingconfiguration.cpp:102](src/composing/composingconfiguration.cpp#L102)).

**Test default in every regional/annotation test that sets it: 1**
(forces single-alternative mode, short-circuiting the multi-element
shape):
- [notationimplode_tests.cpp:877](src/notation/tests/notationimplode_tests.cpp#L877)
- [notationimplode_tests.cpp:922](src/notation/tests/notationimplode_tests.cpp#L922)
- [notationimplode_tests.cpp:980](src/notation/tests/notationimplode_tests.cpp#L980)
- [notationimplode_tests.cpp:1123](src/notation/tests/notationimplode_tests.cpp#L1123)
- [notationimplode_tests.cpp:1334](src/notation/tests/notationimplode_tests.cpp#L1334)

All `chordResults` reads in the test suite are `.front()`, `[0]`, or
`empty()` — never `[1]`, `.size() > 1`, or iteration past `front()`:
- `notationimplode_tests.cpp` — 14 reads, all `.front()`/`empty()`
- `notationinteraction_harmony_pinning_tests.cpp` — 1 read, `[0]` only
- `pipeline_snapshot_tests.cpp` — 2 reads, both `.front()`

**No test asserts the count of "|"-separated alternatives in
`harmonicAnnotation`.** Tests like
[notationimplode_tests.cpp:951-953](src/notation/tests/notationimplode_tests.cpp#L951-L953)
only `EXPECT_NE(annotation.find("Cm"), std::string::npos)` — primary
result presence, not alternative content.

**No test exists named `*display*`, `*context*`, or `*regional*` that
asserts a case where the display-context analysis produces a
known-better identity than the per-region analysis.** Searched
`src/composing/tests/`, `src/notation/tests/`, `tools/`. No comments
in tests document such a case either.

**`pipeline_snapshot_tests.cpp` tickRegional snapshots already pin the
`.front()` of the multi-element shape** — the per-region winner after
prepend in the disagreement case, the fresh display-context winner in
the agreement case. The snapshots will record "primary identity"
either way; they don't pin alternatives.

The (α) cruft hypothesis gains weight: zero documented case justifies
the display-context call's continued existence on identity-correctness
grounds.

## Q5 — Synthesis and Phase 3c implication

### Verdict

**(α) Cruft.** Display-context `analyzeChord` call predates the
canonical per-region path; per-region path uses the same input
collection function on the same window with strictly more informed
temporal context; `findTemporalContext` does nothing the per-region
pipeline doesn't already do (and the per-region pipeline calls
`findTemporalContext` itself for seeding); zero test coverage justifies
the divergence on correctness grounds.

### The wrinkle (active vestigial purpose)

The cruft's *output* is load-bearing in two places:

1. **Status-bar `harmonicAnnotation`** ([notationcomposingbridge.cpp:533-540](src/notation/internal/notationcomposingbridge.cpp#L533-L540))
   sorts and renders up to `analysisAlternatives()` distinct candidates
   from the multi-element vector
2. **Right-click menu `appendAnalysisItemsForContext`** ([notationcontextmenumodel.cpp:55-151](src/notationscene/qml/MuseScore/NotationScene/notationcontextmenumodel.cpp#L55-L151))
   sorts and presents up to `analysisAlternatives()` distinct
   candidates as menu items per category

Production default for `analysisAlternatives` is 3, so deleting the
cruft naively (single result from `region.chordResult`) silently
regresses both UIs to a single entry.

### Recommended Phase 3c-impl shape

**Persist the per-region `analyzeChord`'s vector-of-candidates onto
`AnalyzedRegion` and let P3 read alternatives from there.** The
per-region call at
[rhythmbridge.cpp:273](src/notation/internal/notationharmonicrhythmbridge.cpp#L273)
already produces up to 3 candidates and discards the tail
([rhythmbridge.cpp:280](src/notation/internal/notationharmonicrhythmbridge.cpp#L280):
`ChordAnalysisResult chosenResult = results.front();`). Keep them.

Concrete shape:

- Extend `AnalyzedRegion` (`src/composing/analyzed_section.h`) with a
  `std::vector<ChordAnalysisResult> chordResultAlternatives` field
  (or rename `chordResult` → `chordResults` and make it the full
  vector — design choice for Phase 3c-impl, both work).
- In the per-region pipeline, persist the full `results` vector
  (or `results` minus `front()` if keeping `chordResult` separate)
  onto the region.
- Translate into `AnalyzedRegion` during `analyzeSection` exactly as
  Phase 3a/3b do.
- Convert P3 to read `region.chordResult` as `chordResults[0]` and
  `region.chordResultAlternatives` as `chordResults[1..N]`.
- Delete the second `analyzeChord` call, the `findTemporalContext`
  call from P3 (helper itself stays — it still seeds the per-region
  pipeline), the `collectRegionTones` call from P3, the prepend
  tie-break, and the `regionalSnapshotsMatch` two-pass expansion
  (since both passes will now produce identical results).
- Migrate the 5 temporal extension fields to
  `AnalyzedRegion::temporalExtensions` per the original prompt
  (unchanged).
- Delete the 3 dead fields (unchanged).

### Expected Phase 3c-impl shape

Closer to the original Phase 3c prompt than not. The
3c-prep-bonus-question becomes "extend `AnalyzedRegion` with
alternatives" — small additive schema change.

### Snapshot impact

- Implode (P1) and annotation (P2) byte-identical — they don't read
  alternatives.
- Tick-regional (P3) primary identity (`.front()`) byte-identical —
  same as `region.chordResult`, same as today's prepended winner in
  disagreement case.
- Tick-regional alternatives content **may shift on a small subset of
  ticks**: today's alternatives come from `analyzeChord` with a
  segment-local-lookback temporal context; tomorrow's come from
  `analyzeChord` with the per-region-evolved temporal context. The
  shift is the unification, not a regression. Capture pre-migration
  (Step A) and verify byte-identity of primary; alternatives diff
  is documented as expected.

### Why not the alternative options

- **Keep the second `analyzeChord` call but reuse `region.temporalExtensions` for context** — keeps the cruft, doesn't reduce duplication, doesn't fully close divergence D (display tones still re-collected). Smaller patch but punts the cleanup.
- **Proceed-as-planned and accept UX regression** — silently demotes status-bar and right-click menu to single-entry. No path forward without restoring alternatives.

## Surprising finding

`findTemporalContext` is called by the per-region pipeline itself
([rhythmbridge.cpp:214](src/notation/internal/notationharmonicrhythmbridge.cpp#L214))
to **seed** the pipeline's evolving temporal context. The function is
not unique to the cruft path — it's a shared helper that the cruft
path uses for *ad hoc* per-tick lookback, while the canonical path
uses it once for initialization and then evolves the context forward
through analyzed regions. The per-region pipeline therefore already
produces strictly more informed temporal context than the
display-context call, on the same input window, using the same tone
collector and the same temporal-context seed function. The fact that
the cruft path "looked deliberate" in static reading was an artifact
of `findTemporalContext`'s name suggesting principled context
construction — when in fact the per-region pipeline already does the
principled thing better, and the P3 call is just a holdover of the
original shape from before the pipeline existed.
