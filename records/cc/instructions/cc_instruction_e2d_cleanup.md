# CC Instruction — E2d-cleanup: Eliminate Pass B code duplication

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`.

**Current HEAD:** post-E2d (two commits ahead of `20f992a5e7`). Confirm with
`git log --oneline -3`. Working tree must be clean.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**One commit. Zero behavioral change.** Must pass 407/407, 52/52, 11/11
byte-identical to HEAD. Revert if any test changes.

---

## Problem

E2d introduced `runPassB` in `harmonicfunctionlayer.cpp` — a second
implementation of the same algorithm that lives as `applyStepBonusGuard` in
`chordanalyzer.cpp`. The constants `kWStepIn`, `kWStepOut`, `kStepBudget` are
also defined in `harmonicfunctionlayer.h`. Any future change to the guard logic
or constants must be made in two places, and they will drift.

This instruction eliminates the duplication: one implementation, called from
both sites.

---

## Design

**Introduce `StepBonusCell` and `applyStepBonus()` in `chordanalyzer.h`.**

`StepBonusCell` is a minimal plain struct — just the fields needed by the
algorithm. `applyStepBonus()` is a free function declared in `chordanalyzer.h`
and defined in `chordanalyzer.cpp`. It contains the single authoritative
implementation of Pass B.

The constants (`kWStepIn`, `kWStepOut`, `kStepBudget`) move to `chordanalyzer.h`
and are removed from `harmonicfunctionlayer.h`.

`harmonicfunctionlayer.cpp` already includes `chordanalyzer.h` transitively
(via `ChordAnalysisResult` and related types). Confirm this in Part A.

The `applyStepBonusGuard` call in `chordanalyzer.cpp` is gated on
`!prefs.suppressProgressionSignals` (so the scorer skips it when the function
layer is handling Pass B). The function layer's `runPassB` lambda is replaced
with two calls to `applyStepBonus`.

---

## Part A — Mandatory reads before editing

### A1 — Confirm include chain

Read `harmonicfunctionlayer.h` and `harmonicfunctionlayer.cpp`. Confirm that
one of the includes (direct or transitive) brings `chordanalyzer.h` into scope
so that adding `StepBonusCell` and `applyStepBonus` to `chordanalyzer.h` makes
them available in `harmonicfunctionlayer.cpp` without a new `#include`.

If `chordanalyzer.h` is NOT reachable from `harmonicfunctionlayer.cpp`, report
this and add an explicit `#include` in `harmonicfunctionlayer.cpp`.

### A2 — Read `applyStepBonusGuard` lambda (chordanalyzer.cpp L2330–2368)

Read the full lambda. Report:
- The exact type of `perBassWith` elements (likely `RawCandidate`). Confirm it
  has a `.score` field and a `.templateIdx` (or equivalent) field that indexes
  into `templates[]`.
- How the m7-family guard resolves `intervalCount` in the scorer — it uses
  `templates[oi].intervals.size()` (or similar) directly, since `templates` is
  captured by the lambda. Confirm this.
- Whether `applyStepBonusGuard` is currently gated on `!suppressProgressionSignals`
  or runs unconditionally.
- The exact call site(s): is it called once per bass (inside the `bi` loop) or
  once for all basses together?

### A3 — Read `runPassB` lambda (harmonicfunctionlayer.cpp)

Confirm its current form after E2d. Note any differences from the description
in E2d (e.g. edge cases added, loop structure). This is the code to DELETE once
the shared function is working.

### A4 — Read `kWStepIn/kWStepOut/kStepBudget` locations

Confirm these constants are currently defined in `harmonicfunctionlayer.h` (added
in E2d-infra). Report the exact lines.

---

## Part B — Add `StepBonusCell` and constants to `chordanalyzer.h`

Near the bottom of `chordanalyzer.h`, before the closing of the namespace,
add:

```cpp
// ── Pass B shared data types (used by chordanalyzer.cpp and harmonicfunctionlayer.cpp) ──

/// Minimal cell descriptor for applyStepBonus(). Callers fill this from
/// either RawCandidate (scorer path) or ScoringCell+score (function-layer path).
struct StepBonusCell {
    int          bassPc        { -1 };
    int          rootPc        { -1 };
    ChordQuality quality       { ChordQuality::Major };
    int          intervalCount { 0 };
    double       score         { 0.0 };   ///< Modified in place by applyStepBonus.
};

/// Step-bonus constants (single source of truth — replaces duplicates in
/// harmonicfunctionlayer.h).
inline constexpr double kWStepIn    = 0.10;
inline constexpr double kWStepOut   = 0.10;
inline constexpr double kStepBudget = kWStepIn + kWStepOut + 0.01;

/// Apply the stepwise-bass-motion bonus (Pass B) to a flat vector of cells.
/// Cells from multiple basses may be mixed — the guard compares only within
/// the same bassPc group. Call separately for the with-wDim and
/// without-wDim score variants (since scores diverge for Dim/HalfDim cells).
///
/// @param cells        Cells to score; .score is read and modified in place.
/// @param previousBassPc  Bass PC of the preceding region (-1 = unknown).
/// @param nextBassPc      Bass PC of the following region (-1 = unknown).
/// @param jointEnabled    Must be true for any bonus to apply (same gate as
///                        wSeqBonus / wDimBonus).
void applyStepBonus(std::vector<StepBonusCell>& cells,
                    int previousBassPc,
                    int nextBassPc,
                    bool jointEnabled);
```

---

## Part C — Implement `applyStepBonus` in `chordanalyzer.cpp`

Add the definition near `applyStepBonusGuard` (e.g. just before the
`analyzeChord` function). This is the single authoritative Pass B
implementation.

```cpp
void applyStepBonus(std::vector<StepBonusCell>& cells,
                    int previousBassPc,
                    int nextBassPc,
                    bool jointEnabled)
{
    if (!jointEnabled) return;

    for (std::size_t ci = 0; ci < cells.size(); ++ci) {
        StepBonusCell& cand = cells[ci];
        if (cand.rootPc != cand.bassPc) continue;           // root-position only
        if (cand.quality == ChordQuality::Power) continue;

        double stepIn = 0.0;
        if (previousBassPc >= 0 && previousBassPc != cand.bassPc) {
            const int d = ((cand.bassPc - previousBassPc) % 12 + 12) % 12;
            if (d == 1 || d == 2 || d == 10 || d == 11) stepIn = kWStepIn;
        }
        double stepOut = 0.0;
        if (nextBassPc >= 0) {
            const int d = ((nextBassPc - cand.bassPc) % 12 + 12) % 12;
            if (d == 1 || d == 2 || d == 10 || d == 11) stepOut = kWStepOut;
        }
        if (stepIn + stepOut == 0.0) continue;

        // m7-family guard: if a minor-seventh (or dim / half-dim) competitor
        // rooted a minor third below this bass is competitive, suppress the bonus.
        const int compRoot = ((cand.bassPc - 3) % 12 + 12) % 12;
        bool blocked = false;
        for (std::size_t oi = 0; oi < cells.size() && !blocked; ++oi) {
            const StepBonusCell& other = cells[oi];
            if (other.bassPc != cand.bassPc) continue;
            if (other.rootPc != compRoot)    continue;
            if (other.quality != ChordQuality::Diminished
             && other.quality != ChordQuality::HalfDiminished
             && !(other.quality == ChordQuality::Minor
                  && other.intervalCount == 4)) continue;
            if (other.score >= cand.score - kStepBudget) blocked = true;
        }
        if (!blocked) cand.score += stepIn + stepOut;
    }
}
```

**Verify against `applyStepBonusGuard`:** Read the lambda again and confirm
the step-distance condition, guard direction, and guard threshold match
exactly. If there is any discrepancy, the lambda is authoritative — update
the free function accordingly and note the difference in the report.

---

## Part D — Replace `applyStepBonusGuard` call in `chordanalyzer.cpp`

### D1 — Gate on `!suppressProgressionSignals`

The scorer's `applyStepBonusGuard` currently runs unconditionally (confirmed
in Part A2). Wrap the entire call (or the lambda definition + call) so it only
runs when `!prefs.suppressProgressionSignals`:

```cpp
if (!prefs.suppressProgressionSignals) {
    applyStepBonusGuard(perBassWith,   /* ... existing args ... */);
    applyStepBonusGuard(perBassWithout,/* ... existing args ... */);
}
```

### D2 — Replace the lambda body with a call to `applyStepBonus`

After gating, replace the lambda body with:

```cpp
// Build StepBonusCell vectors from perBassWith / perBassWithout.
// templates[] is in scope here; use it to fill intervalCount.
auto toStepCells = [&](const auto& perBass) {
    std::vector<StepBonusCell> cells;
    cells.reserve(perBass.size());
    for (const auto& rc : perBass) {
        StepBonusCell c;
        c.bassPc        = rc.bassPc;          // or however bassPc is stored
        c.rootPc        = rc.rootPc;
        c.quality       = rc.quality;
        c.intervalCount = static_cast<int>(
            templates[rc.templateIdx].<INTERVALS_FIELD>.size());
        c.score         = rc.score;
        cells.push_back(c);
    }
    return cells;
};

auto applyBack = [](auto& perBass, const std::vector<StepBonusCell>& cells) {
    for (std::size_t i = 0; i < perBass.size(); ++i)
        perBass[i].score = cells[i].score;
};

auto cellsWith    = toStepCells(perBassWith);
auto cellsWithout = toStepCells(perBassWithout);
applyStepBonus(cellsWith,    temporalCtx.previousBassPc, temporalCtx.nextBassPc, jointScoringEnabled);
applyStepBonus(cellsWithout, temporalCtx.previousBassPc, temporalCtx.nextBassPc, jointScoringEnabled);
applyBack(perBassWith,    cellsWith);
applyBack(perBassWithout, cellsWithout);
```

**Field names:** Replace `rc.bassPc`, `rc.rootPc`, `rc.quality`, `rc.templateIdx`,
`rc.score`, and `<INTERVALS_FIELD>` with the exact field names confirmed in
Part A2. Replace `temporalCtx.previousBassPc` / `temporalCtx.nextBassPc` with
whatever the in-scope variables are at the `applyStepBonusGuard` call site.

**Confirm `jointScoringEnabled`** is in scope at this call site (it is computed
earlier in `analyzeChord()`).

If `applyStepBonusGuard` is called inside the `bi` loop (once per bass), the
`toStepCells` / `applyBack` wrappers operate on a single bass's cells each
time — `applyStepBonus` handles that correctly (the bassPc guard is a no-op
when all cells share the same bassPc).

---

## Part E — Replace `runPassB` in `harmonicfunctionlayer.cpp`

Delete the `runPassB` lambda and its two call sites. Replace with:

```cpp
if (snapshot->jointScoringEnabled) {
    const std::size_t N = snapshot->cellsWithWDim.size();

    // Build StepBonusCell vectors for both variants.
    auto makeStepCells = [&](const std::vector<double>& scores) {
        std::vector<StepBonusCell> cells;
        cells.reserve(N);
        for (std::size_t i = 0; i < N; ++i) {
            const ScoringCell& sc = snapshot->cellsWithWDim[i];
            StepBonusCell c;
            c.bassPc        = sc.bassPc;
            c.rootPc        = sc.rootPc;
            c.quality       = sc.quality;
            c.intervalCount = sc.intervalCount;
            c.score         = scores[i];
            cells.push_back(c);
        }
        return cells;
    };

    auto cellsWith    = makeStepCells(scoreWith);
    auto cellsWithout = makeStepCells(scoreWithout);

    applyStepBonus(cellsWith,    ctx.previousBassPc, ctx.nextBassPc, /*jointEnabled=*/true);
    applyStepBonus(cellsWithout, ctx.previousBassPc, ctx.nextBassPc, /*jointEnabled=*/true);

    for (std::size_t i = 0; i < N; ++i) {
        scoreWith[i]    = cellsWith[i].score;
        scoreWithout[i] = cellsWithout[i].score;
    }
}
```

`jointEnabled=true` is passed directly (we are inside the `if (jointScoringEnabled)`
guard, so it is always true — but passing it explicitly keeps the function's
contract self-documenting). Alternatively, remove the outer `if` and pass
`snapshot->jointScoringEnabled` to both calls.

---

## Part F — Remove duplicate constants from `harmonicfunctionlayer.h`

Delete the three lines added in E2d-infra:

```cpp
inline constexpr double kWStepIn   = 0.10;
inline constexpr double kWStepOut  = 0.10;
inline constexpr double kStepBudget = kWStepIn + kWStepOut + 0.01;
```

They are now in `chordanalyzer.h`. If `harmonicfunctionlayer.cpp` references
these constants by the namespace-qualified name `fn::kWStepIn` etc., those
references will now resolve from `chordanalyzer.h` — confirm the unqualified
or qualified name still compiles. If they were unqualified and are now in a
different namespace, update the references accordingly.

---

## Part G — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2dc.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2dc.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2dc.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2dc.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2dc.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2dc.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407, 52/52, 11/11 — byte-identical to HEAD.**

If tests fail:
- A compile error about `StepBonusCell` not found → the include chain from
  `harmonicfunctionlayer.cpp` to `chordanalyzer.h` is broken. Add an explicit
  `#include`.
- A compile error about `applyStepBonus` not found → `chordanalyzer.cpp`
  includes its own header, but confirm the function is in the correct namespace.
- A test divergence → the free function body differs from the original lambda.
  Re-read `applyStepBonusGuard` and diff against `applyStepBonus` line by line.
  Do NOT update goldens. Report and revert.

---

## Part H — Commit

```
cd C:\s\MS && git add \
  src/composing/analysis/chord/chordanalyzer.h \
  src/composing/analysis/chord/chordanalyzer.cpp \
  src/composing/analysis/function/harmonicfunctionlayer.h \
  src/composing/analysis/function/harmonicfunctionlayer.cpp; echo "exit:$?"

cd C:\s\MS && git commit -m "E2d-cleanup: extract applyStepBonus free function, eliminate Pass B duplication

Replace the runPassB lambda in harmonicfunctionlayer.cpp and the
applyStepBonusGuard lambda body in chordanalyzer.cpp with a single
shared applyStepBonus() free function declared in chordanalyzer.h and
defined in chordanalyzer.cpp.

StepBonusCell struct (bassPc, rootPc, quality, intervalCount, score) added
to chordanalyzer.h as the common cell descriptor for the algorithm.

Constants kWStepIn, kWStepOut, kStepBudget moved to chordanalyzer.h
(single definition); duplicates removed from harmonicfunctionlayer.h.

applyStepBonusGuard call in analyzeChord() gated on
!prefs.suppressProgressionSignals — scorer skips Pass B in suppression
mode since applyHarmonicFunction() handles it via the shared function.

Zero behavioral change. All tests identical to HEAD."; echo "exit:$?"
```

---

## Report back

1. Part A2 findings — exact `RawCandidate` field names used in `toStepCells`
2. Whether any discrepancy was found between `applyStepBonusGuard` and the
   free function (if so: what and which was authoritative)
3. Whether `chordanalyzer.h` was already reachable from
   `harmonicfunctionlayer.cpp` or required an explicit `#include`
4. Namespace of `kWStepIn` etc. in `chordanalyzer.h` and whether references
   in `harmonicfunctionlayer.cpp` needed updating
5. Test results and commit hash
