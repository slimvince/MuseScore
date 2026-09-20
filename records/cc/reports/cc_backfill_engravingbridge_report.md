# CC backfill report — Phase-5 branch backfill (round 2), cluster 1: engravingbridge

**Tests-only. No production logic/behaviour change. `upstream` not touched; local commit only.**

## §0 — Preamble
No unstaged `cowork_*`/`COWORK_*` docs were present (`git status` clean apart from this cluster's test
files + the gitignored `scratch_artifacts/`). Nothing to commit under §0 — consistent with the spec's
"likely nothing new" (the types-header design + plan were committed in `e316ff1ab4`).

## §1 — Headline

| Suite | Before | After |
|---|---|---|
| `composing_tests` | 695 PASSED | **715 PASSED** (+20 new tests) |
| `notation_tests` | 53 PASSED / 4 SKIPPED | **53 PASSED / 4 SKIPPED** (unchanged) |
| `pipeline_snapshot_tests` | 11 PASSED, 0 FAILED | **11 PASSED, 0 FAILED** (goldens NOT refreshed) |
| BIR corpus | 53 / 24 / 53 | **53 / 24 / 53 by construction** (no production byte changed) |

- **No production source touched** — `git status` shows only `src/composing/tests/` (the new test file,
  CMakeLists entry, and 8 fixture files). `notation_tests` + `pipeline_snapshot_tests` were not even
  relinked by the build (they link the unchanged `composing_analysis`), so their results are the same
  binaries as before this change. Corpus is unchanged **by construction**, not by re-measurement.
- **No corpus / snapshot movement** → the §3 STOP condition did not arise.
- **Surfaced defects: NONE.** Every oracle (music-theory / documented contract, re-derived at source)
  matched the current implementation — no `DISABLED_`/xfail was needed.

## §2 — Coverage re-measurement (the round-2 progress check)

UNION branch coverage (`composing_tests ∪ notation_tests`, same runner/methodology as the
`cc_union_branch_coverage_report.md` baseline; `pwsh tools/coverage/run_branch_coverage.ps1`):

| File | Branches | Before (unhit / %) | After (unhit / %) | Δ unhit |
|---|---:|---:|---:|---:|
| `engravingbridge/regiontonecollector.cpp` | 154 | 24 / 84.42% | **12 / 92.21%** | −12 |
| `engravingbridge/regiontonecollector.h`   | 16  | 6 / 62.50%  | **4 / 75.00%**  | −2  |
| `engravingbridge/regiontoneprimitives.cpp`| 244 | 37 / 84.84% | **16 / 93.44%** | −21 |
| `scoreharvest/metricweights.cpp`          | 76  | 20 / 73.68% | **12 / 84.21%** | −8  |
| **cluster total** | **490** | **87 / 82.24%** | **44 / 91.02%** | **−43** |
| whole module (`src/composing/analysis`) | 5586 | 999 / 82.12% | **956 / 82.90%** | −43 |

All −43 of the module's reduction is in this cluster (as expected). The instrumented run executed all
715 composing tests (the 20 new ones included). Two `notation_tests` xfails (`MozartK279…`,
`PopulateChordTrackEmitsCadenceMarkersOnCorelli`) are still `GTEST_SKIP()`'d, unchanged.

## §3 — Tests added (20 tests, file `engravingbridge_branch_tests.cpp`)

Fixtures: 4 new minimal scores authored as `.musicxml` and converted to `.mscx`
(`MuseScore5.exe -o … `, the established fixture pipeline) — `eb_compound` (12/8),
`eb_dense` (dense-start tally), `eb_steps` (stepwise bass + chord-track staff), `eb_pedal` (two
damper pedals + post-start onset) — plus the existing `nm_*` note-model fixtures.

| Test | Function(s) | Branch(es) covered (current source lines) |
|---|---|---|
| `EB_StaffPredicates_OrdinaryHiddenDrumsetChordTrack` | `staffIsEligible` / `isChordTrackStaff` (`.h`) | 96 (hidden), 99 (drumset) — credited; 83 (partName chord-track) exercised (see §5); 87 trackName + ordinary path |
| `EB_WeightedPcView_ExcludedStaffDropped` | `weightedPcView` | 88:35[F] excluded-staff drop |
| `EB_WeightedPcView_NonPlayingAndInvisibleDropped` | `weightedPcView` | 89:19[F] non-playing, 89:30[F] invisible |
| `EB_WeightedPcView_CompoundStressedBeatWeight` | `weightedPcView` beatWeight | 76 COMPOUND_STRESSED (0.85) |
| `EB_WeightedPcView_DenseStartTallyAndDedup` | `weightedPcView` dense-start tally | 190:17[T], 194:17[F], 205:17[T], 208:17[F] |
| `EB_WeightedPcView_PedalTailContributesAndMultiplierZeroNoOp` | `weightedPcView` Pass 4 | 323:9[F] multiplier-zero no-op (+ pedal-tail contribution) |
| `EB_WeightedPcView_PedalPassDenseStartLookAhead` | `weightedPcView` pedal pass | 286:17[T], 286:37[TF] |
| `EB_MetricWeights_CompoundStressedDirect` | `beatTypeToWeight`, `regionMetricWeightForBeatType` | 45 compound-stressed pref, 79 compound-stressed→0.85 |
| `EB_BuildPedalWindowIndex_NormalExcludedIneligible` | `buildPedalWindowIndex` | 163:42[T] excluded staff, 163:75[T] ineligible staff (+ happy path) |
| `EB_BuildPedalWindowIndex_SostenutoSoftDegenerate` | `buildPedalWindowIndex` | 152:13[T] sostenuto, 152:61[T] soft, 158:13[T] degenerate |
| `EB_BuildPedalWindowIndex_SameStartSortedByEnd` | `buildPedalWindowIndex` sort | 173:17[F] same-start → order by end |
| `EB_SoundingAt_ExcludedNonPlayingInvisibleGraceDropped` | `soundingAt` | 55 excluded, 56:19 non-play, 56:30 invisible, 56:43 grace |
| `EB_PitchContextOverSpan_InvisibleAndExcludedDropped` | `pitchContextOverSpan` | 233 invisible, 234 excluded staff |
| `EB_DetectOnsetSubBoundaries_IneligibleStaffExcluded` | `detectOnsetSubBoundaries` | 315 ineligible staff |
| `EB_DetectOnsetSubBoundaries_NonPlayingInvisibleFiltered` | `detectOnsetSubBoundaries` | 327:25 non-play, 327:39 invisible |
| `EB_DetectBassMovementSubBoundaries_IneligibleStaffExcluded` | `detectBassMovementSubBoundaries` | 401 ineligible staff |
| `EB_DetectBassMovementSubBoundaries_NonPlayingInvisibleFiltered` | `detectBassMovementSubBoundaries` | 413:25 non-play, 413:39 invisible |
| `EB_FindTemporalContext_StepwiseBassBothDirections` | `findTemporalContext` | 486 back ineligible, 544 fwd ineligible, 529:9/529:32(T) stepwise-prev, 586:9/586:32(T) stepwise-next |
| `EB_FindTemporalContext_NoPreviousContext` | `findTemporalContext` | 529:32(F) no previous bass |
| `EB_FindTemporalContext_EndOfScoreNoForwardContext` | `findTemporalContext` | 540(F) end-of-score, 586:32(F) no next bass |

Every assertion is the theory/contract-correct value re-derived at source (e.g. the 12/8 beat-3
COMPOUND_STRESSED weight ratio `1.0 : 0.85` is pinned with an explicit `TimeSigFrac(12,8)` oracle;
`isDiatonicStep` drives the stepwise-flag assertions; the sostenuto/soft begin-text strings are the
exact `<sym>keyboardPedalSost/S</sym>` markers the production guard tests).

## §4 — Re-classification of triage "ADD-TEST" branches → EXCLUDE-DEFENSIVE / DEFER (NOT tested)

Per the spec's "re-confirm the class at source — don't trust the triage blindly", the following branch
directions the triage routed to ADD-TEST were re-confirmed at source to be **unreachable defensive
guards or deferred legacy code**, and are therefore NOT tested (the formal exclusion is the Phase-6
coverage seal). These account for the difference between the triage's per-file ADD-TEST counts and the
reachable arms actually covered.

**Provably unreachable (defensive — can't-happen by an upstream invariant or by construction):**
- **`cr->isGrace()` arms** — `regiontoneprimitives.cpp` 320 (detectOnset), 406 (detectBass),
  492/550 (findTemporalContext hasAttacks). A grace note lives in its parent Chord's
  `graceNotesBefore()/After()` and is **never a Segment ChordRest**, so `Segment::cr(track)->isGrace()`
  is always false. (Graces surface only as `NoteModel` events — checked at the NoteEvent level in
  `soundingAt`/`weightedPcView`, which **are** tested: 56:43 / the already-hit 89:43.)
- **`cr->tick() != segTick` "onset-only" guards** — `regiontoneprimitives.cpp` 323 (detectOnset),
  409 (detectBass). A ChordRest's tick equals its own segment's tick by construction, so the guard
  never fires.
- **`tailDuration <= 0`** — `regiontonecollector.cpp` 333. A pedal-tail candidate is recorded only when
  `writtenEnd < endTick`, and every *indexed* pedal window ends after both `startTick` and the
  candidate's `writtenEnd`; `tailStart = max(writtenEnd, startTick) < min(pedalRelease, endTick) =
  tailEnd` always, so the clipped tail is always positive.
- **`bassPitch == max()`** — `regiontonecollector.cpp` 372. Once `totalWeight > 0` (else the function
  already returned), the bass-floor fallback loop always assigns `bassPitch`.
- **`uniCount == 0` (Jaccard)** — `regiontoneprimitives.cpp` 355. Both onset bit-sets are non-empty
  (guarded `if (bits != 0)`), so their union is non-empty.
- **Null / measure-less / segment-less / bounds / malformed-time-sig / exhaustive-enum-default guards** —
  `regiontonecollector.cpp` 58 (null score), 121 (pedal staff absent — but candidates are only recorded
  for staves present in the index), 141 (`pedalWindows.empty()` inside the non-empty-guarded record),
  161/171/173/231/235 (measure-/segment-less), 239/260 (`durInRegion <= 0`, unreachable for the same
  clip reason as 333); `regiontonecollector.h` 76 (`si >= nstaves`), 80 (`!part`), 87:12[F] (instrument
  null); `metricweights.cpp` 43 (switch default), 60/66 (null measure/segment, malformed sig), 89/93/98
  (null score / measure / malformed sig), 142 (null spanner), 147 (null pedal), 163:13 (`staffIdx >=
  nstaves`); `regiontoneprimitives.cpp` 297/382 (`!firstSeg`), 430 (`onsets.empty()`).

**Deferred (Phase 6, legacy):** the **6** `collectPitchContext` arms — `regiontoneprimitives.cpp`
136, 139, 168:44, 174:46, 180:25, 180:39 — retire with the legacy pitch-context builder; left untested
per the spec's DEFER routing.

**Net:** of the cluster's 44 still-unhit arm-directions after this backfill, **43 are
defensive/DEFER** (12 + 4 [bar line 83] + 16 + 12 minus the one tooling artifact below); the only
"real logic" arm not credited is line 83 (a tooling artifact, §5).

## §5 — One credited-coverage caveat: `regiontonecollector.h` line 83 (partName chord-track)

`isChordTrackStaff` line 83 (`part->partName().contains("Chord Track")`, the long-name path) is
**tested and executed** — `EB_StaffPredicates` case (e) loads `eb_steps` (whose staff-0 instrument
long name is "Chord Track", track name empty) and asserts `isChordTrackStaff(sc, 0) == true`, which can
only return true via line 83's true arm; `EB_DetectOnsetSubBoundaries_IneligibleStaffExcluded` and the
`findTemporalContext` tests additionally drive it through the instrumented pipeline (`detectOnset*` /
`NoteModel::build` → `staffIsEligible` → `isChordTrackStaff`).

It is nonetheless **not credited** by the llvm-cov UNION view. `isChordTrackStaff` carries a
`static const muse::String CHORD_TRACK_MARKER` local, which causes a single COMDAT-folded out-of-line
copy; the branch counters for line 83 are attributed to one winning TU whose own runtime calls never
pass a long-name chord-track staff. (By contrast `staffIsEligible` has no static local and is inlined
per-TU, so its 96/hidden and 99/drumset arms *did* move once routed through `NoteModel::build`.) This
is a measurement artifact of header-inline + static-local coverage attribution, **not a test gap** — the
trackName path (line 87 true arm) is independently credited, and the partName path is asserted true.
No production change is warranted; flagged for the Phase-6 seal as "covered-by-test, COMDAT-uncredited".

## §6 — Scope & gate
- **Tests-only**; no production `.cpp`/`.h`/tool logic changed. No gap was closable only by changing
  production (the one un-credited branch, line 83, is a tooling artifact, not a missing test).
- Build green; `composing_tests` 715 (+20); `notation_tests` 53/4-skip and `pipeline_snapshot_tests`
  11/0-fail both unchanged; corpus 53/24/53 by construction.
- `upstream` untouched; local commit only.

## §7 — Deliverable
Local (unpushed) commit: `engravingbridge_branch_tests.cpp` + the `tests/CMakeLists.txt` entry + the 8
fixture files (`data/eb_{compound,dense,steps,pedal}.{musicxml,mscx}`). This report is gitignored.
Commit sha: **`3f2e4bebe268aa6d8e73f4753dbecaa27ee402f9`** (`3f2e4bebe2`) — 10 files changed, 1975
insertions, **zero production source** (Cowork can verify by `git show --stat 3f2e4bebe2`: only
`src/composing/tests/`).
