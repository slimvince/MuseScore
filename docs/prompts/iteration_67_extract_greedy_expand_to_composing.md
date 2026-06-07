# Iteration 67: Extract greedy-expand segmentation to src/composing/ (Task #58 Part A)

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=5, BIR=false=125. Jazz BIR=false=12.
(Commit 8441c34eff — build fix after upstream muse_framework migration.)

Build fresh before every BIR measurement. Verify binary is newer than source.

**This is a correctness-preservation refactor.** No BIR change is expected or
desired. If BIR changes in any direction, the extraction introduced a divergence —
revert and report.

---

## Background

The greedy-expand segmentation algorithm lives entirely as `static` functions in
`tools/batch_analyze.cpp`. The bridge path (`src/notation/internal/
notationcomposingbridgehelpers.cpp`) still uses `detectHarmonicBoundariesJaccard`.
Both files carry §2.10 TODO comments noting that the shared logic must move to
`src/composing/` before the bridge can be switched.

This iteration is **Part A only**: extract the greedy-expand implementation into a
new `src/composing/` module so both `batch_analyze` and (in Iter 68) the bridge can
consume it. The bridge is not changed in this iteration.

Functions to extract from `tools/batch_analyze.cpp` (all currently `static`):
- `collectNoteChangeTicks()` — collects note-change tick events from a Score
- `fillGap()` — Round 2 gap-fill helper
- `greedyExpandSegmentation()` — entry point; returns `std::vector<PlacedRegion>`
- `placedRegionsToTicks()` — converts PlacedRegion list to sorted Fraction ticks

Types/constants to extract:
- `struct PlacedRegion` — working type produced by greedyExpandSegmentation
- `kAnchorMinScore` (1.5), `kAnchorMinDurationTicks` (1 × DIVISION), `kRound2MinScore` (1.25)

---

## Step 1 — Read before touching anything

Read the following ranges in `tools/batch_analyze.cpp` and confirm your
understanding of each function's dependencies before writing a single line:

- Lines ~1620–1650: constants + `PlacedRegion` struct
- Lines ~1620–1795: `collectNoteChangeTicks` (find its exact line range)
- Lines ~1795–1940: `fillGap`
- Lines ~1938–2060: `greedyExpandSegmentation`
- Lines ~2060–2080: `placedRegionsToTicks`

Note every type these functions depend on that comes from outside `batch_analyze.cpp`:
engraving Score/Segment/Fraction types, `ChordAnalyzerPreferences`, `IChordAnalyzer`,
`KeySigMode`, etc. These will all be needed in the new header's includes.

Also read the §2.10 TODO comment in `notationcomposingbridgehelpers.cpp` (line ~1146)
to confirm nothing there changes in this iteration.

---

## Step 2 — Create the new module

**New files** (both must be listed in `src/composing/CMakeLists.txt`):

```
src/composing/analysis/harmony/harmonicsegmenter.h
src/composing/analysis/harmony/harmonicsegmenter.cpp
```

**Header (`harmonicsegmenter.h`):**

```cpp
// SPDX-License-Identifier: GPL-3.0-only
// MuseScore-Studio-CLA-applies
#pragma once

#include <vector>
#include <set>
#include <string>
#include "engraving/dom/score.h"
#include "types/fraction.h"
#include "analysis/chord/chordanalyzer.h"   // ChordAnalyzerPreferences, IChordAnalyzer
#include "analysis/key/keymodeanalyzer.h"   // KeySigMode

namespace mu::composing {

/// Minimum analyzeChord winner score for a Round 1 anchor.
/// Tuned against Baroque corpus (Iter 52).
inline constexpr double kAnchorMinScore = 1.5;

/// Minimum region duration (ticks) for Round 1 anchor eligibility.
inline constexpr int kAnchorMinDurationTicks = 1 * engraving::Constants::DIVISION;

/// Minimum score for a candidate to be promoted in Round 2 gap-fill (Iter 53).
inline constexpr double kRound2MinScore = 1.25;

/// Working type produced by greedyExpandSegmentation().
struct PlacedRegion {
    int startTick = 0;
    int endTick   = 0;

    int    round      = 0;
    double confidence = 0.0;
    bool   isAnchor   = false;
    std::string reason;

    int    rootPitchClass = -1;
    int    bassPitchClass = -1;
    std::string quality;   // ChordQuality as string; replace with enum if convenient
};

/// Entry point for greedy-expand segmentation.
/// Returns all note-change-event candidate regions; Round 1 anchors are promoted
/// by score/duration/voice criteria, Round 2 fills gaps using bilateral context.
std::vector<PlacedRegion>
greedyExpandSegmentation(const engraving::Score* score,
                         const engraving::Fraction& startTick,
                         const engraving::Fraction& endTick,
                         const std::set<size_t>& excludeStaves,
                         const analysis::ChordAnalyzerPreferences& prefs,
                         analysis::IChordAnalyzer* chordAnalyzer,
                         int globalKeyFifths,
                         analysis::KeySigMode globalKeyMode);

/// Converts placed regions (round >= 1) to a sorted, deduplicated list of
/// boundary ticks — drop-in replacement for detectHarmonicBoundariesJaccard output.
std::vector<engraving::Fraction>
placedRegionsToTicks(const std::vector<PlacedRegion>& regions);

} // namespace mu::composing
```

Adjust namespaces and includes to match the exact conventions already used in
`src/composing/analysis/chord/chordanalyzer.h`. Do not guess — read an existing
composing header first and mirror its include paths and namespace declarations.

**Implementation (`harmonicsegmenter.cpp`):**

Move the four `static` function bodies from `batch_analyze.cpp` verbatim (after
removing the `static` keyword and adjusting namespaces/includes). Do not change
any logic — this is a pure mechanical move. The constants move to the header as
`inline constexpr`.

---

## Step 3 — Update CMakeLists.txt

Add the two new files to `src/composing/CMakeLists.txt` in the SOURCES section,
alongside the existing `chordanalyzer.cpp` / `keymodeanalyzer.cpp` entries.

Check whether `tools/CMakeLists.txt` already links against `composing` (it almost
certainly does after the Iter 64 include-path fix). If not, add it.

---

## Step 4 — Update batch_analyze.cpp

In `tools/batch_analyze.cpp`:
1. Add `#include "src/composing/analysis/harmony/harmonicsegmenter.h"` (or the
   correct relative path from tools/).
2. Remove the now-extracted `static` definitions for `collectNoteChangeTicks`,
   `fillGap`, `greedyExpandSegmentation`, `placedRegionsToTicks`, `PlacedRegion`,
   and the three constants.
3. Add `using namespace mu::composing;` or qualify all uses — whichever matches
   the existing style in batch_analyze.cpp.
4. Confirm all call sites in `analyzeScore()` still compile.

---

## Step 5 — Build and confirm batch_analyze regression tests pass

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Verify:
- `batch_analyze.exe` builds
- `composing_tests.exe` builds and passes 407/407
- `notation_tests.exe` builds and passes 53/53
- `pipeline_snapshot_tests.exe` passes all (no goldens should change — bridge untouched)

If any test regresses: stop, revert the extraction, report — do not continue.

---

## Step 6 — Confirm BIR unchanged

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

**Required**: BIR=true=5, BIR=false=125. Any change means the extraction
introduced a divergence in the moved functions — revert and report.

---

## Step 7 — Commit

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.h
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add src/composing/CMakeLists.txt
git add tools/batch_analyze.cpp
git add tools/CMakeLists.txt   # only if changed
git commit -m "Refactor: extract greedy-expand segmentation to src/composing/ (Task #58 Part A)

Move greedyExpandSegmentation(), fillGap(), placedRegionsToTicks(), and
collectNoteChangeTicks() from static functions in tools/batch_analyze.cpp
into src/composing/analysis/harmony/harmonicsegmenter.{h,cpp}.

PlacedRegion struct and kAnchorMinScore/kAnchorMinDurationTicks/kRound2MinScore
constants moved to header.

batch_analyze.cpp updated to consume from shared location.
Bridge path (notationcomposingbridgehelpers.cpp) unchanged — Iter 68.

BIR=true=5, BIR=false=125 confirmed unchanged. Tests: 407/407 + 53/53."

git push
```

---

## Step 8 — Report to Cowork

```
Extraction:
  New files: harmonicsegmenter.h + harmonicsegmenter.cpp
  Functions moved: collectNoteChangeTicks, fillGap, greedyExpandSegmentation,
                   placedRegionsToTicks
  batch_analyze.cpp: static definitions removed, includes shared header
  Bridge: unchanged (Iter 68)

Build:
  composing_tests: N/407
  notation_tests: N/53
  pipeline_snapshot_tests: N/N

BIR unchanged: [yes / no — describe if no]

Committed: [yes — hash / not committed — reason]
```
