# CC — Layer 1 coverage-gate report (branch/block coverage of the new code)

> Closes the §5.1b coverage requirement for the ratified layer-1 commit `e30bb45a4f`.
> **TEST-ONLY: no production / behavior / scoring change** — only added tests + one minimal
> fixture and measured. Commit locally (unpushed); Cowork verifies test-only; user ratifies.

## §1 — Tool
No gcov/llvm-cov/clang/OpenCppCoverage in this MSVC/ninja environment. Used the VS BuildTools
**`Microsoft.CodeCoverage.Console.exe`** (Dynamic Code Coverage), which instruments the existing
Release `/Zi` PDB binaries at runtime and exports **Cobertura**. It reports **line/block**
coverage (an uncovered block = an untaken branch arm); it does not emit per-condition data, so
sub-line branch arms are audited manually below. Coverage was **unioned** across
`composing_tests` and `notation_tests` (a line is covered if hit in either), then filtered to the
§1 files. (Reproduce: `Microsoft.CodeCoverage.Console.exe collect --output X.cobertura.xml
--output-format cobertura -- composing_tests.exe`.)

## §2 — In-scope files: before → after
Scope = the code layer 1 introduced/rewrote: `notemodel/note_model.{h,cpp}`, and in
`engravingbridge` the derived views `weightedPcView` / `soundingAt` / `buildTones` + the
Score-based one-shot wrappers (the `collectRegionTones`/`collectSoundingAt` wrappers). OUT of
scope (left in place for layers 2/3): `collectPitchContext`, `detectOnsetSubBoundaries`,
`detectBassMovementSubBoundaries`, `findTemporalContext` internals.

| File | Before | After |
|---|---|---|
| `notemodel/note_model.cpp` | 100% (49/49) | **100% (49/49)** |
| `engravingbridge/regiontonecollector.cpp` (`weightedPcView` + `collectRegionTones` wrapper) | 85.6% (101/118) | **100% (118/118)** |
| `engravingbridge/regiontoneprimitives.cpp` (`soundingAt`, `buildTones`, `collectSoundingAt` wrapper, + out-of-scope co-tenants) | 96.0% (194/202) | **97.5% (197/202)** — every remaining uncovered line is OUT-OF-SCOPE co-tenant code (see §4) |
| `notemodel/note_model.h` (inline accessors) | — | inline-accessor artifact (§4) |
| `engravingbridge/regiontonecollector.h` (pre-existing inline predicates) | — | pre-existing / artifact (§4) |

**Every reachable in-scope branch is now exercised.** The `weightedPcView` executable body is
100%; the `soundingAt`/`buildTones`/wrapper code is 100% (the only uncovered primitives lines are
the out-of-scope detectors / pitch-context / temporal-context internals).

## §3 — Tests added (uncovered → now-covered)
All in `note_model_tests.cpp`; one minimal fixture (`nm_dense_start.{musicxml,mscx}`).

| Test | Covers (file:line) | The branch |
|---|---|---|
| **T9** `WeightedPcView_EmptyRegionReturnsEmpty` | collector.cpp **L59** | `end <= start` early return (`end==start` and `end<start`). |
| **T10** `WeightedPcView_DenseStartLookAheadExclusion` | collector.cpp **L184–190, L200–213** | the `excludeLookAheadOnDenseStart` block (≥3 PCs at start) + the forward-walk exclusion of post-start onsets; asserts 6 PCs (off) vs 3 (on). |
| **T11** `CollectSoundingAt_ScoreWrapper` | primitives **L94–98** | the Score-based `collectSoundingAt` one-shot wrapper. |
| **T12** `SoundingAt_SustainedNoteMidSpan` | (deterministic) | `soundingAt` sustained partition (onset<tick) + descending-onset ordering, no horizon. |
| **T13** `WeightedPcView_DenseStartSustainCount` | collector.cpp **L193–196** | the sustain-counting loop body of the excludeLookAhead block (a note sustaining into the region start). |
| **T14** `WeightedPcView_BassFloorFallback` | collector.cpp **L367–369** | the bass-floor fallback, reached via a test pref `bassPassingToneMinWeightFraction=0.9` (no PC reaches the threshold). |

Manual branch-arm audit of the few sub-line conditionals in `weightedPcView`/`soundingAt`
(the `passes(...)` filter `&&` chain, the forward-vs-sustain `onset >= startTick` split, the
`onset==tick` anchor-vs-sustain partition, the `legacyCap`-free overlap edges): each arm is
exercised by T1–T14 + the regionanalyzer-driven full-suite runs (multi-region scores with
sustains, ineligible staves via T8, grace/invisible filtering via T4/T7).

## §4 — Documented non-covered lines (NOT chased — with reasons)
- **Out-of-scope co-tenants** (per §1; covered when their layers are built): primitives
  **L136, L138** (`collectPitchContext`), **L354** (`detectBassMovementSubBoundaries` empty
  guard), **L453, L510** (`findTemporalContext` `bassIsStepwise*` internals).
- **Pre-existing inline predicate** (NOT layer-1-new code — `staffIsEligible`/`isChordTrackStaff`
  predate layer 1; layer 1 only reuses them): collector.h **L78** = the `!part` defensive guard
  in `isChordTrackStaff` (a staff always has a part → unreachable defensive; not changed — that
  would be a production edit). collector.h **L100** = the chord-track `return false` — it **is**
  behaviorally executed (T8 asserts a Chord-Track note's `staffEligible==false`, which requires
  this return); the MSVC block tool under-attributes inlined header one-liners.
- **Inline-accessor tool artifact**: note_model.h **L110** = `notes()` — called by the test
  helpers `countNotes`/`findNote` on every assertion; under-attributed because it is an inlined
  one-liner. No production change can fix the attribution.

No genuinely-reachable in-scope branch is left uncovered, and no branch was covered by changing
production.

## §5 — Gate / invariance
- **Full branch coverage of the §1 new code** — every reachable branch exercised; unreachable /
  out-of-scope / artifact lines documented above.
- **Both suites pass:** composing **553→559** (T1–T14), notation **57/57**, pipeline snapshots
  **11/11**.
- **Test-only invariance:** the only files changed vs `e30bb45a4f` are `note_model_tests.cpp` +
  `nm_dense_start.{musicxml,mscx}` — **zero production files**. Therefore the analyzer binary is
  byte-identical and the snapshot/BIR/oracle numbers are **unchanged by construction** (snapshots
  re-run green confirms it; the corpus was not regenerated because production is untouched —
  regenerating would be byte-identical and wasteful). The pre-existing HELD B2 changes
  (`localmodulationdetector.{cpp,h}`, `batch_analyze.cpp`) remain uncommitted and untouched.

## §6 — Deliverable
Committed locally (unpushed): `note_model_tests.cpp` (T9–T14) + `nm_dense_start.{musicxml,mscx}`.
This report (HELD). Next: layer 2.
