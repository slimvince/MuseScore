# CC Instruction — E1: Harmonic function layer shell

**Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`

**For this session — also read:** `C:\s\MS\docs\scoring_model.md` (full document).
This session introduces a new architectural layer that the scoring model doc must
describe. Read it before touching any files.

**Current state:** Branch `master`, HEAD `3ac52e1198`. **Working tree may be dirty** — a Cowork agent incorrectly made source edits that must be reverted before starting. Run the cleanup step below first.

## Part 0 — Revert unauthorised Cowork edits

```
cd C:\s\MS
git checkout -- src/composing/analysis/CMakeLists.txt src/composing/CMakeLists.txt src/composing/tests/CMakeLists.txt src/composing/analysis/region/regionanalyzer.cpp docs/scoring_model.md; echo "exit:$?"
rm -rf src/composing/analysis/function; echo "exit:$?"
git status; echo "exit:$?"
```

Expected: working tree clean, no untracked files under `src/composing/analysis/function/`.
If `git status` shows anything else, stop and report before proceeding.
BIR baselines (lenient-OR): Baroque BIR=true=28, BIR=false=16; Jazz BIR=true=36,
BIR=false=10. Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**This instruction introduces zero behavioral change.** Every test must produce
an identical result before and after. If any test changes, revert everything.

---

## Background

The chord scorer (`analyzeChord()`) has accumulated 12 post-scoring gates and
three progression-signal bonuses (`rootContinuityBonus`, `w_seq`, `w_dim`) that
do not belong inside a pitch-evidence scorer — they perform functional/contextual
reasoning that belongs in a separate layer. The B3 attempt showed the scorer is
approaching a complexity ceiling where new changes unpredictably interact with
existing mechanics.

Phase E introduces a harmonic function layer that sits between `analyzeChord()`
output and the final chord label. Migration is incremental:

- **E1 (this instruction):** Introduce the architectural slot as a pure pass-through.
  Zero logic changes. Creates the call sites and interface for E2/E3 to fill in.
- **E2:** Migrate `rootContinuityBonus`, `w_seq`, `w_dim` out of the scorer.
- **E3:** Migrate post-scoring gates (Gate J, Gates A–D, dim7 rotation selection).
- **E4:** Cadence detection and functional labeling completeness.

---

## Part A — Read before touching any file

Read the following sections of `src/composing/analysis/region/regionanalyzer.cpp`:

1. The three `analyzeChord()` call sites:
   - Pass 1 (~L444): `chordAnalyzer->analyzeChord(tones, localKeyFifths, localKeyMode, &temporalCtx, attemptPrefs)`
   - Pass 2 (~L637): `chordAnalyzer->analyzeChord(subTones, subKeyFifths, subKeyMode, &subCtx, prefs)`
   - Pass 2b (~L814): `chordAnalyzer->analyzeChord(subTones, subKeyFifths, subKeyMode, &subCtx, prefs)`
2. The `refineSparseChordQualityFromKeyContext()` calls immediately after each
   `analyzeChord()` call — these are the correct insertion points.
3. `src/composing/analysis/CMakeLists.txt` — how subdirectories are added.
4. Any existing subdirectory `CMakeLists.txt` (e.g. `analysis/chord/CMakeLists.txt`
   or `analysis/region/CMakeLists.txt`) — as a pattern to follow.

Confirm the exact line numbers before proceeding.

---

## Part B — Create the new module

### B1 — Directory and source files

Create `src/composing/analysis/function/harmonicfunctionlayer.h`:

```cpp
// harmonicfunctionlayer.h
// Harmonic function layer — post-analysis pass between analyzeChord() output
// and final chord label. Called from regionanalyzer.cpp after each non-
// exploratory analyzeChord() call.
//
// E1: pass-through (no changes to ChordAnalysisResult).
// E2: progression signals migrate here (rootContinuityBonus, w_seq, w_dim).
// E3: post-scoring gates migrate here (Gate J, Gates A–D, dim7 rotation).
// E4: cadence detection and functional labeling.
//
// See docs/scoring_model.md §10 for the full migration plan.

#pragma once

#include "src/composing/analysis/chord/chordanalyzer.h"

namespace mu::composing::function {

/// Context passed to the function layer for each region.
/// Extended in later phases (E4: phrase boundaries, cadence evidence).
struct HarmonicFunctionContext {
    int keyFifths { 0 };
    KeySigMode keyMode { KeySigMode::Ionian };
    int previousRootPc { -1 };   ///< Root PC of the preceding region (-1 = unknown)
    int nextRootPc { -1 };       ///< Root PC of the following region (-1 = unknown)
};

/// Apply harmonic function reasoning to the winning chord candidate.
/// Modifies \p result in-place. Called after analyzeChord() + refinement,
/// gated on !prefs.explorationMode. E1: no-op.
void applyHarmonicFunction(ChordAnalysisResult& result,
                           const HarmonicFunctionContext& ctx);

} // namespace mu::composing::function
```

Create `src/composing/analysis/function/harmonicfunctionlayer.cpp`:

```cpp
// harmonicfunctionlayer.cpp

#include "harmonicfunctionlayer.h"

namespace mu::composing::function {

void applyHarmonicFunction(ChordAnalysisResult& result,
                           const HarmonicFunctionContext& ctx)
{
    // E1: pass-through.
    // Logic is added incrementally:
    //   E2 — rootContinuityBonus, w_seq, w_dim migrate here
    //   E3 — Gate J, Gates A–D, dim7 rotation selection migrate here
    //   E4 — cadence detection, functional label completeness
    (void)result;
    (void)ctx;
}

} // namespace mu::composing::function
```

### B2 — CMakeLists for the new submodule

Create `src/composing/analysis/function/CMakeLists.txt`, following the
pattern of the existing analysis submodule CMakeLists files you read in Part A.
Link to whatever the other analysis submodules link to (composing_chord or
similar). The target name should be `composing_function` or
`composing_harmonicfunction` — follow the naming convention you observe.

### B3 — Wire into `src/composing/analysis/CMakeLists.txt`

Add `add_subdirectory(function)` in the appropriate position (after the other
`add_subdirectory` calls for analysis submodules).

### B4 — Wire the new library into the top-level composing module

In `src/composing/CMakeLists.txt`, add the new library to the
`target_link_libraries(composing ...)` block.

---

## Part C — Insert call sites in `regionanalyzer.cpp`

Add `#include "src/composing/analysis/function/harmonicfunctionlayer.h"` at the
top of `regionanalyzer.cpp`.

At each of the three insertion points (after `refineSparseChordQualityFromKeyContext()`
in Pass 1, Pass 2, and Pass 2b), add:

```cpp
if (!prefs.explorationMode) {
    function::HarmonicFunctionContext fnCtx;
    fnCtx.keyFifths = <localKeyFifths or subKeyFifths>;
    fnCtx.keyMode = <localKeyMode or subKeyMode>;
    fnCtx.previousRootPc = <temporalCtx or subCtx>.previousRootPc;
    fnCtx.nextRootPc = <temporalCtx or subCtx>.nextRootPc;
    function::applyHarmonicFunction(chosenResult, fnCtx);
}
```

Use the correct variable names for each pass (Pass 1 uses `localKeyFifths` /
`localKeyMode` / `temporalCtx`; Pass 2/2b use `subKeyFifths` / `subKeyMode` /
`subCtx`). Adjust if the actual variable names differ from what's above.

The `!prefs.explorationMode` gate ensures the function layer is never called
during segmentation-internal boundary exploration — consistent with how all
other context-dependent bonuses are gated.

---

## Part D — Update `docs/scoring_model.md`

Add a new **§10. Harmonic function layer** section at the end of the document:

```markdown
## 10. Harmonic function layer

**Module:** `src/composing/analysis/function/harmonicfunctionlayer.{h,cpp}`

A post-analysis pass that sits between `analyzeChord()` output and the final
chord label. Called from `regionanalyzer.cpp` after each non-exploratory
`analyzeChord()` call — gated on `!prefs.explorationMode` — at three sites:
Pass 1 (~L444+refinement), Pass 2 (~L637+refinement), Pass 2b (~L814+refinement).

`HarmonicFunctionContext` carries: `keyFifths`, `keyMode`, `previousRootPc`,
`nextRootPc`. Extended in E4 with phrase-boundary and cadence evidence.

**E1 (current):** Pass-through. No changes to `ChordAnalysisResult`.

**E2 (planned):** Progression signals migrate out of `chordanalyzer.cpp`:
- `rootContinuityBonus` (currently in `bassIndependentContextualBonuses`)
- `w_seq` (currently in main scoring loop)
- `w_dim` (currently in main scoring loop)

**E3 (planned):** Post-scoring gates migrate out of `analyzeChord()`:
- Gate J (vii°→V7 completion)
- Gates A–D (Minor-add6 ↔ HalfDim7 enharmonic)
- `dim7CharacteristicBonus` rotation selection

**E4 (planned):** Cadence detection, tonic confirmation, functional label
completeness (secondary dominants, borrowed chords, augmented sixths).

**Rationale.** The scoring model §4 documents that `rootContinuityBonus`,
`w_seq`, and `w_dim` are progression signals (not pitch-evidence terms) and
that Gates A–L are functional-reasoning corrections on top of a pitch scorer.
Having them inside `analyzeChord()` couples functional reasoning to the
pitch-evidence scorer, making each new template addition risk unexpected gate
interactions (B1/B2/B3 history). The function layer provides the correct
architectural home for these terms.
```

Update the document header's "Last updated" line to note E1.

---

## Part E — Build and verify zero behavioral change

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e1.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e1.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e1.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e1.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e1.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e1.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped) —
identical to baseline. If any count changes at all, revert everything.**

Do NOT run BIR — a pure pass-through cannot change BIR.

---

## Part F — Commit

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.h \
  src/composing/analysis/function/harmonicfunctionlayer.cpp \
  src/composing/analysis/function/CMakeLists.txt \
  src/composing/analysis/CMakeLists.txt \
  src/composing/CMakeLists.txt \
  src/composing/analysis/region/regionanalyzer.cpp \
  docs/scoring_model.md; echo "exit:$?"

cd C:\s\MS && git commit -m "E1: introduce harmonic function layer shell (pass-through)

New module src/composing/analysis/function/harmonicfunctionlayer.{h,cpp}.
Defines HarmonicFunctionContext (keyFifths, keyMode, previousRootPc,
nextRootPc) and applyHarmonicFunction() — currently a no-op pass-through.

Wired into regionanalyzer.cpp after each non-exploratory analyzeChord()
call (Pass 1 / Pass 2 / Pass 2b), gated on !prefs.explorationMode.

This creates the architectural slot for:
  E2: migration of rootContinuityBonus / w_seq / w_dim out of the scorer
  E3: migration of post-scoring gates (Gate J, Gates A-D, dim7 rotation)
  E4: cadence detection and functional labeling

Zero behavioral change. All tests identical to HEAD 3ac52e1198.
docs/scoring_model.md §10 added describing the layer and migration plan."; echo "exit:$?"
```

---

## Report back

1. Exact line numbers where the three call sites were inserted
2. CMakeLists target name chosen and link structure
3. Test results — confirm all three suites are byte-identical to baseline
4. Commit hash
5. Any naming or include-path adjustments needed (report but do not fix without
   flagging — the interface must be stable for E2)
