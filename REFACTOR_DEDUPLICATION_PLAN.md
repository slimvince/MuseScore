# Deduplication Refactor — Multi-Session Plan

This document breaks a deduplication cleanup of the composing/notation bridge
layer into small iterations. Each iteration is a self-contained Claude Code
(CC) session that builds, tests, and commits a single focused change.

## Audit findings this plan acts on

Full duplication audit lives in the commit that added this file. Headlines:

- `keyModeScaleIntervals` (21×7 mode-interval table) is duplicated in three
  translation units in `src/notation/internal/` (bridge, helpers, implode) and
  has two more narrower copies inside `src/composing/analysis/chord/chordanalyzer.cpp`.
- `diatonicDegreeForRootPc` is defined in an anonymous namespace in helpers
  but the same scale-degree loop is re-inlined in five call sites.
- `notationtuningbridge.cpp` inlines `((keyFifths * 7) % 12 + 12) % 12` twice
  while every other site calls `ionianTonicPcFromFifths`.
- `notationtuningbridge.cpp` has three separate `static GlobalInject<...>`
  declarations for the same `IComposingAnalysisConfiguration`.
- Four call sites rebuild a chord-track `excludeStaves` set from scratch when
  `staffIsEligible` already excludes chord-track staves.
- The sequence `findTemporalContext → analyzeChord → refresh identity →
  recompute function fields` appears twice in `notationcomposingbridge.cpp`
  (the second copy explicitly comments that it replicates the first).
- `PedalWindow` scan + sort + release-tick logic is written twice inside
  `notationcomposingbridgehelpers.cpp`.
- `NotationInteraction::addAnalyzedHarmonyToSelection` is a third
  annotation entry point that bypasses the bridge formatter and does not
  honor `scoreNoteSpelling`.
- `notationimplodebridge.cpp::populateChordTrack` re-implements cadence
  classification (PAC/PC/DC/HC) and pivot detection instead of calling
  `detectCadences` / `detectPivotChords` — the two implementations have
  already diverged in rule details.
- Test helpers (`tones`, `tonesFromRange`, `diatonicResult`, `analysisConfig`)
  are re-declared across test files.

## Branch strategy — cherry-pick rules

There are two branches:

- **master** — full project including implode / chord-track work.
- **submission** — upstream submission branch; excludes implode.

For each iteration, the iteration section states one of:

- **Cherry-pick: yes** — commit is safe to cherry-pick onto submission.
- **Cherry-pick: no (implode-only)** — commit touches implode; keep on master.
- **Cherry-pick: split** — iteration produces two commits; cherry-pick
  only the non-implode commit. Iteration section gives the exact commit
  split.

Cherry-pick command (CC runs this only when instructed):

```
git checkout submission
git cherry-pick <sha>
git checkout master
```

## Per-iteration preflight (start of every CC session)

1. **Read context** (in this order):
   - `CLAUDE.md` (auto-loaded; project conventions — note that the build
     commands inline here are STALE; always defer to BUILD_AND_TEST.md)
   - `BUILD_AND_TEST.md` — **authoritative** source for build, test, and
     run commands. Always re-read at the start of every session; do not
     rely on remembered commands from a previous session or from CLAUDE.md.
     The build directory is `ninja_build_rel`, not `ninja_build`.
   - `ARCHITECTURE.md` (§3 Bridge Architecture, plus any section referenced in
     the iteration)
   - `STATUS.md` (last few entries to see what has been committed)
   - This file — only the specific iteration section plus the Branch
     Strategy section above
2. **Confirm baseline green.** Use the exact commands from
   BUILD_AND_TEST.md. As of this writing:
   - Build: `powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"`
     (do NOT use `cmd.exe //c` — MSYS2 mangles `//` into a UNC path)
   - Composing tests: `/c/s/MS/ninja_build_rel/composing_tests.exe`
   - Notation tests: `/c/s/MS/ninja_build_rel/notation_tests.exe`
   - Read `src/composing/tests/chord_mismatch_report.txt`
   - Note baseline: expected 381/381 composing, 51/51 notation (per
     STATUS.md). If baseline is different, stop and report before proceeding.
   If any of the above commands fails or looks unfamiliar, re-read
   BUILD_AND_TEST.md before improvising.
3. **Execute the iteration** following its Steps section.
4. **Build + test after change.** Same commands as step 2. Numbers must not
   regress. If any test fails, stop and report; do not commit.
5. **Commit.** Use the commit message template in the iteration section.
6. **Cherry-pick if instructed** (see Branch Strategy).
7. **Update STATUS.md.** Append a one-paragraph entry under a new heading
   dated with `date` (from Git Bash). Include commit SHA and test results.

## Out-of-scope safety valve

The default pre-authorization in CLAUDE.md covers `src/composing/`,
`src/notation/internal/notationaccessibility.cpp`, and `ARCHITECTURE.md`.
Several iterations in this plan legitimately touch other files in
`src/notation/internal/` (bridge .cpp files) and `src/notation/tests/`.
These are required for a bridge-layer refactor and are explicitly authorized
for the iterations listed below.

Iterations that touch `notationinteraction.cpp` or the composing catalog XML
are marked **STOP — REQUIRES USER APPROVAL** at the top of their section. CC
must post the plan summary back to the user and wait for explicit go-ahead
before starting those iterations.

---

## Iteration 1 — Promote `keyModeScaleIntervals` to a shared header

**Goal.** One 21-mode interval table, owned by the composing module. Delete
the three bridge-layer copies and the two narrower copies in
`chordanalyzer.cpp`.

**Files touched.**
- `src/composing/analysis/key/keymodeanalyzer.h` — add declaration
- `src/composing/analysis/key/keymodeanalyzer.cpp` — add definition
- `src/notation/internal/notationcomposingbridge.cpp` — delete copy at lines
  76-104, replace one local call
- `src/notation/internal/notationcomposingbridgehelpers.cpp` — delete copy at
  lines 84-112, update callers
- `src/notation/internal/notationimplodebridge.cpp` — delete copy at lines
  528-556, update callers (**implode-touching commit**)
- `src/composing/analysis/chord/chordanalyzer.cpp` — replace the two narrower
  7-mode tables at lines 1646 and 2115 with slices of the shared 21-mode
  table

**Steps.**
1. In `keymodeanalyzer.h`, add:
   ```cpp
   /// Scale degrees (semitone offsets from tonic) for every mode defined
   /// by KeySigMode. Indexed by keyModeIndex(mode). Size is always 7 even
   /// for modes whose scale has fewer distinct pitch classes — the table
   /// expresses the canonical diatonic mapping used for Roman-numeral
   /// degree lookup.
   const std::array<int, 7>& keyModeScaleIntervals(KeySigMode mode);
   ```
2. In `keymodeanalyzer.cpp`, define it. Copy the 21×7 table verbatim from
   `notationcomposingbridge.cpp:78-100`. Keep the bounds-safe fallback
   (returns mode-0 row when index is out of range).
3. In each of the three notation TUs: delete the anonymous-namespace
   `keyModeScaleIntervals` function, add a `using
   mu::composing::analysis::keyModeScaleIntervals;` at the top of the
   anonymous namespace (or qualify inline). Verify every call site still
   compiles.
4. In `chordanalyzer.cpp` lines 1646 and 2115: replace the local
   `MODE_SCALES` arrays with calls into the new exported function. The local
   code indexes only 7 diatonic modes; guard the call with the same
   `modeScaleIdx < 7` check already present there.
5. Grep for any remaining `MODE_SCALES` tokens; none should remain.

**Build & test.** Numbers must match baseline.

**Commit message.**
```
Promote keyModeScaleIntervals to shared composing header

Removes 21×7 mode-interval table duplication across three notation
bridge TUs plus two narrower copies inside chordanalyzer. Single
source of truth now lives at composing/analysis/key/keymodeanalyzer.{h,cpp}.

No behavior change: callers were already using identical tables.
```

**Cherry-pick: split.**
- Commit 1a: changes to `composing/`, `notationcomposingbridge.cpp`,
  `notationcomposingbridgehelpers.cpp`. Cherry-pick.
- Commit 1b: changes to `notationimplodebridge.cpp`. Do not cherry-pick.

---

## Iteration 2 — Export `diatonicDegreeForRootPc`; retire 5 inline copies

**Prereq.** Iteration 1 merged.

**Goal.** One shared function for "which scale degree does this root
pitch-class occupy in this key/mode?". Delete the five inline loops.

**Files touched.**
- `src/notation/internal/notationcomposingbridgehelpers.h` — add declaration
- `src/notation/internal/notationcomposingbridgehelpers.cpp` — move the
  existing anonymous-namespace definition (currently at line 151) into
  `mu::notation::internal` public scope; remove from anonymous namespace
- `src/notation/internal/notationcomposingbridge.cpp` — replace inline loops
  at lines 119-125 (`applySparseChordKeyContext`) and 852-860 (inside
  `addHarmonicAnnotationsToSelection`). The `diatonicToKey` follow-up check
  in `applySparseChordKeyContext` (lines 127-145) should stay but should
  consume the degree returned by the helper
- `src/notation/internal/notationcomposingbridgehelpers.cpp` — replace inline
  loop in `applyGapKeyContext` at lines 1700-1737
- `src/notation/internal/notationimplodebridge.cpp` — replace inline loops
  in the pivot path at lines 1049-1058 and in the borrowed-chord path at
  lines 1265-1284 (**implode-touching commit**)

**Steps.**
1. Add to `notationcomposingbridgehelpers.h`:
   ```cpp
   /// Returns the diatonic scale degree [0..6] of rootPc in (keyFifths, keyMode),
   /// or -1 if rootPc is not in the scale.
   int diatonicDegreeForRootPc(int rootPc, int keyFifths,
                               mu::composing::analysis::KeySigMode keyMode);
   ```
2. In `notationcomposingbridgehelpers.cpp`, move the existing definition at
   lines 151-163 out of the anonymous namespace into `mu::notation::internal`.
3. For each call site: replace the inline loop with a call to
   `diatonicDegreeForRootPc(rootPc, keyFifths, keyMode)`. Preserve the
   surrounding `diatonicToKey` and `function.degree` assignments that follow.
4. Grep: after this iteration there should be **zero** places in the notation
   layer that iterate a `scale` array comparing to `rootPc`.

**Build & test.** Must match baseline.

**Commit message.**
```
Export diatonicDegreeForRootPc; remove 5 inline degree loops

The helper was defined in an anonymous namespace so every caller wrote
its own copy of the (tonicPc + scale[i]) % 12 == rootPc loop. Expose it
via notationcomposingbridgehelpers.h and replace all inline copies.

No behavior change.
```

**Cherry-pick: split.**
- Commit 2a: helper export + calls in `notationcomposingbridge.cpp` and
  `notationcomposingbridgehelpers.cpp`. Cherry-pick.
- Commit 2b: calls in `notationimplodebridge.cpp`. Do not cherry-pick.

---

## Iteration 3 — Use `ionianTonicPcFromFifths` in tuning bridge

**Goal.** Two-line swap. Close a formula-drift channel.

**Files touched.**
- `src/notation/internal/notationtuningbridge.cpp` — lines 193 and 552

**Steps.**
1. At `notationtuningbridge.cpp:193`, replace
   `const int ionianPc = ((keyFifths * 7) % 12 + 12) % 12;` with
   `const int ionianPc = mu::composing::analysis::ionianTonicPcFromFifths(keyFifths);`
2. Same at line 552.
3. Verify the header for `ionianTonicPcFromFifths` is already included
   (composing/analysis/key/keymodeanalyzer.h is included transitively
   through the bridge helpers). Add an explicit include if needed.

**Build & test.** Must match baseline.

**Commit message.**
```
Use ionianTonicPcFromFifths in tuning bridge

Removes two inline copies of the fifths→tonic-PC formula that diverged
from every other site in the codebase. Single formula location.
```

**Cherry-pick: yes.**

---

## Iteration 4 — Consolidate `GlobalInject` in tuning bridge

**Goal.** Replace three separate `static GlobalInject<IComposingAnalysisConfiguration>`
declarations with one accessor local to the translation unit.

**Files touched.**
- `src/notation/internal/notationtuningbridge.cpp` — lines 75, 556, 769

**Steps.**
1. In the anonymous namespace at the top of `notationtuningbridge.cpp`, add:
   ```cpp
   const mu::composing::IComposingAnalysisConfiguration* analysisConfig()
   {
       static muse::GlobalInject<mu::composing::IComposingAnalysisConfiguration> cfg;
       return cfg.get().get();
   }
   ```
2. Replace each of the three per-function `static GlobalInject` blocks
   (lines 75-78, 556-559, 769-772) with a call to `analysisConfig()`.
   Preserve null-check semantics exactly as in the current code.
3. Grep: only one `GlobalInject<IComposingAnalysisConfiguration>` should
   remain in this TU.

**Build & test.** Must match baseline.

**Commit message.**
```
Tuning bridge: one analysisConfig() accessor, not three injects

Replaces three separate static GlobalInject<IComposingAnalysisConfiguration>
declarations with a single TU-local accessor. No behavior change; reduces
wiring duplication.
```

**Cherry-pick: yes.**

---

## Iteration 5 — `buildChordTrackExcludeStaves` helper

**Goal.** Factor the four identical "collect chord-track staves into
excludeStaves" loops behind one helper. Leaves callers that ALSO add
non-chord-track exclusions untouched.

**Files touched.**
- `src/notation/internal/notationanalysisinternal.h` — add helper
- `src/notation/internal/notationcomposingbridge.cpp` — three sites
  (lines 655-660, 676-681, 728-734)
- `src/notation/internal/notationtuningbridge.cpp` — one site
  (lines 753-758)

**Steps.**
1. Add to `notationanalysisinternal.h`:
   ```cpp
   /// Returns the set of staff indices that are chord-track staves in sc.
   /// These should be excluded from harmonic analysis input but may receive
   /// annotation output (see chord-track priority rule).
   inline std::set<size_t> chordTrackExcludeStaves(const mu::engraving::Score* sc)
   {
       std::set<size_t> out;
       for (size_t si = 0; si < sc->nstaves(); ++si) {
           if (isChordTrackStaff(sc, si)) {
               out.insert(si);
           }
       }
       return out;
   }
   ```
   Add `#include <set>` if missing.
2. At each of the four sites, replace the inline loop with
   `std::set<size_t> excludeStaves = chordTrackExcludeStaves(score);`
3. Grep: zero remaining inline loops matching the pattern
   `for .* nstaves .* isChordTrackStaff`.

**Build & test.** Must match baseline.

**Commit message.**
```
Factor chordTrackExcludeStaves helper; retire 4 inline loops

Each bridge entry point was rebuilding the same exclude-staves set.
Single helper in notationanalysisinternal.h. No behavior change.
```

**Cherry-pick: yes.**

---

## Iteration 6 — Factor `refreshChordResultWithDisplayContext`

**Goal.** Pull the duplicated sequence `findTemporalContext → analyzeChord →
refresh identity → recompute tonal-function fields` out of both
`analyzeNoteHarmonicContextRegionallyInWindow` and
`addHarmonicAnnotationsToSelection`. The annotation path comment at
`notationcomposingbridge.cpp:800-810` explicitly notes this replication.

**Prereq.** Iterations 1 and 2 merged.

**Files touched.**
- `src/notation/internal/notationcomposingbridgehelpers.h` — add declaration
- `src/notation/internal/notationcomposingbridgehelpers.cpp` — define
- `src/notation/internal/notationcomposingbridge.cpp` — call from both sites

**Steps.**
1. Add helper signature:
   ```cpp
   /// Replaces a region's chord result with a fresh analysis using
   /// display-style ChordTemporalContext at the segment. Preserves the
   /// region's key/mode context and recomputes function fields
   /// (keyTonicPc, keyMode, degree, diatonicToKey) for the new root.
   /// Returns the refreshed result; when tones is empty, returns
   /// fallbackResult unchanged.
   mu::composing::analysis::ChordAnalysisResult
   refreshChordResultWithDisplayContext(
       const mu::engraving::Score* sc,
       const mu::engraving::Segment* seg,
       const std::set<size_t>& excludeStaves,
       const std::vector<mu::composing::analysis::ChordAnalysisTone>& tones,
       int keyFifths,
       mu::composing::analysis::KeySigMode keyMode,
       const mu::composing::analysis::ChordAnalysisResult& fallbackResult);
   ```
2. Extract the shared body. Use `diatonicDegreeForRootPc` (from Iteration 2)
   for the degree lookup.
3. In `analyzeNoteHarmonicContextRegionallyInWindow` (bridge.cpp:311): the
   existing code does a slightly different thing — it keeps all candidate
   results and applies a lambda. Factor only the "prepare preferredResult
   from region.chordResult with fresh context" slice of logic — not the
   multi-candidate handling. Leave the multi-candidate selection inline.
4. In `addHarmonicAnnotationsToSelection` (bridge.cpp:836-863): replace the
   whole block that builds `annotationResult` with a single call to the new
   helper.
5. Delete the long comment at lines 800-810 that explained the replication.

**Build & test.** Must match baseline — this is behavior-preserving.

**Commit message.**
```
Factor refreshChordResultWithDisplayContext

Both the single-note display path and the annotation write path ran the
same findTemporalContext → analyzeChord → recompute-function-fields
sequence, with a comment explicitly acknowledging the replication. One
helper now. Removes a confirmed drift channel.
```

**Cherry-pick: yes.**

---

## Iteration 7 — Factor PedalWindow scanning in helpers.cpp

**Goal.** One `PedalWindowIndex` or similar, consumed by both
`collectRegionTones` and `detectHarmonicBoundariesJaccard`.

**Files touched.**
- `src/notation/internal/notationcomposingbridgehelpers.cpp` only (internal
  refactor)

**Steps.**
1. Hoist the `PedalWindow` struct to file scope (anonymous namespace).
2. Extract the two identical scan+sort passes (around lines 803-878 and
   1185-1249) into a static function like:
   ```cpp
   std::vector<PedalWindow> buildPedalWindowIndex(
       const Score* sc,
       int startTick,
       int endTick,
       const std::set<size_t>& excludeStaves);
   ```
3. Have both callers use the shared function. Preserve the earliest-release
   logic exactly — this is a drift-risk surface so the diff must look tiny.
4. If the two existing callers use slightly different filter criteria
   (check carefully), parameterize the helper rather than maintaining two.

**Build & test.** Must match baseline.

**Commit message.**
```
Factor PedalWindow scanning in bridge helpers

collectRegionTones and detectHarmonicBoundariesJaccard each scanned
pedal spanners and sorted the results. Now one builder consumed by
both. Behavior-preserving.
```

**Cherry-pick: yes.**

---

## Iteration 8 — Extract shared test helpers

**Goal.** Stop reinventing `tones()`, `diatonicResult()`, `analysisConfig()`
in every test file.

**Files touched.**
- New: `src/composing/tests/test_helpers.h`
- New: `src/notation/tests/test_helpers.h`
- `src/composing/tests/chordanalyzer_tests.cpp` (lines 34-108)
- `src/composing/tests/synthetic_tests.cpp` (lines 42-69)
- `src/composing/tests/keymodeanalyzer_tests.cpp` (lines 41-50)
- `src/notation/tests/notationannotate_tests.cpp` (lines 54-68)
- `src/notation/tests/notationimplode_tests.cpp` (lines 59-83 and 428-437)
  — **implode-touching file; see cherry-pick note**
- `src/notation/tests/notationtuning_tests.cpp` (lines 51-56)
- Relevant CMakeLists.txt files to include the new headers

**Steps.**
1. Create `src/composing/tests/test_helpers.h` with:
   - `std::vector<ChordAnalysisTone> tones(std::initializer_list<int> pitches)`
   - `std::vector<ChordAnalysisTone> tonesFromRange(...)` (pulled from
     `synthetic_tests.cpp`)
   - `std::vector<KeyModeAnalyzer::PitchContext> flatPitches(...)` (pulled
     from `keymodeanalyzer_tests.cpp`)
   - `ChordAnalysisResult makeRomanResult(...)` (pulled from
     `chordanalyzer_tests.cpp:74-92`)
   - `const ChordAnalysisResult* findCandidate(const std::vector<ChordAnalysisResult>&, int rootPc, ChordQuality, bool min7 = false)`
2. Create `src/notation/tests/test_helpers.h` with:
   - `const mu::composing::IComposingAnalysisConfiguration* analysisConfig()`
   - `const mu::composing::IComposingChordStaffConfiguration* chordStaffConfig()`
   - `ChordAnalysisResult diatonicResult(int degree, ChordQuality quality, ...)`
     generalised so annotation tests can express non-C-major chords
3. Replace all local definitions with includes. Keep test-file-local
   helpers only if they're genuinely unique to that file.

**Build & test.** Must match baseline. Watch for any compile error in tests
caused by header include ordering.

**Commit message.**
```
Extract shared test helpers (composing + notation)

Tone builders, chord-result constructors, and IoC config accessors
were re-declared in 5+ test files. Now one header per module.
No runtime behavior change.
```

**Cherry-pick: split.**
- Commit 8a: `composing/tests/test_helpers.h` + consumers in composing tests.
  Cherry-pick.
- Commit 8b: `notation/tests/test_helpers.h` + consumers in
  `notationannotate_tests.cpp` and `notationtuning_tests.cpp`.
  Cherry-pick.
- Commit 8c: consumers in `notationimplode_tests.cpp`. Do not cherry-pick.

---

## Iteration 8.5 — Pinning tests for `addAnalyzedHarmonyToSelection`

**Goal.** Before iteration 9 routes `NotationInteraction::addAnalyzedHarmonyToSelection`
through the bridge, capture its current output as explicit assertions. These tests
are deliberately labeled "BehaviorSnapshot" so that anyone reading a failing test in
iter 9 immediately knows the failure is expected: the old expectation must be updated
to the corrected post-bridge value, not reverted.

This iteration was inserted between 8 and 9 because a test audit during iter 4
confirmed zero notation-test coverage for this path. See the iter 8.5 CC session
prompt for the full rationale.

**Files touched.**
- `src/notation/tests/notationinteraction_harmony_pinning_tests.cpp` — new file
- `src/notation/tests/notationtuning_data/harmony_pinning_i_iv_v_i.mscx` — new fixture
- `src/notation/tests/CMakeLists.txt` — register new source

**Cherry-pick: yes** (pure test addition, no production code changes).

---

## Iteration 9 — STOP — REQUIRES USER APPROVAL

**Title.** Route `NotationInteraction::addAnalyzedHarmonyToSelection` through
the bridge.

**Why this needs approval.** `notationinteraction.cpp` is outside the default
pre-authorized scope (CLAUDE.md) and this is a behavior-touching change.
Current per-note path does not honor `scoreNoteSpelling`, does not exclude
chord-track staves from input, and has no minimum-duration gate. Fixing
these changes observable behavior of the "Add chord symbols / Roman
numerals / Nashville numbers" per-note action.

**Before starting, post to user:**
- Summary of current behavior vs proposed behavior.
- Whether to (a) delete the function and route the UI action to
  `addHarmonicAnnotationsToSelection`, (b) keep it as a per-note entry point
  but reroute formatting through a new `mu::notation::formatChordResult(...)`
  helper, or (c) leave it alone.

**Do not proceed** until the user picks a path.

**If option (b) is chosen, provisional steps:**
1. Add to `notationcomposingbridge.h`:
   ```cpp
   struct FormattedChordResult {
       std::string symbol;
       std::string roman;
       std::string nashville;
   };
   FormattedChordResult formatChordResultForStatusBar(
       const mu::engraving::Score* sc,
       const mu::composing::analysis::ChordAnalysisResult& result,
       int keyFifths);
   ```
2. Route both `harmonicAnnotation` and the per-note UI path through it.
3. Fix the chord-track-staff exclusion and the spelling issue while
   touching this code.

**Cherry-pick: yes (assuming no implode coupling in the final fix).**

---

## Iteration 10 — STOP — REQUIRES USER APPROVAL

**Title.** Reconcile implode's cadence / pivot logic with
`detectCadences` / `detectPivotChords`.

**Why this needs approval.** Implode has already diverged from the shared
helpers. Reconciling is behavioral work that will shift cadence labels in
chord-track output. Catalog-grade changes are not pre-authorized.

**Before starting, post to user:**
1. Run this diff exercise on a representative score (Dvořák op08n06 or
   BWV 227.7): generate the chord-track annotations with the current
   inline cadence logic, then with `detectCadences`. Report label deltas
   per measure.
2. Propose one of:
   - **(a) Adopt the shared helpers** — accept any label changes, update
     any tests that codify the old labels, commit.
   - **(b) Keep implode's version and rename it** — e.g. rename the inline
     logic to `classifyChordStaffCadence` with a comment explaining why it
     differs from `detectCadences`. No sharing, but the divergence becomes
     explicit and no one is tempted to reconcile them silently.
3. Ask the user which.

**Do not proceed** until the user picks.

**Cherry-pick: no (implode-only).**

---

## Post-plan bookkeeping

After each iteration commit, append to STATUS.md under a new dated heading:

```
## <DATE> — deduplication iteration N

- Commit(s): <sha>
- Files touched: <list>
- Cherry-picked: yes / no / split (<sha-of-cherry-picked-commit>)
- Composing tests: 381/381 pass
- Notation tests: 51/51 pass
- Chord mismatch report: <corpus numbers unchanged / delta>
```

When all auto-run iterations (1–8) are done, before starting 9 or 10, post
a summary to the user listing the eight commits and the remaining open
questions.
