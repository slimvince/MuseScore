# CC Instruction — E2a: Move progression-signal lambdas to function layer (code organisation)

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 (bonus terms)
and §10 (function layer migration plan).

**Current state:** Branch `master`, HEAD `dd29a04967`, working tree clean.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**This instruction introduces zero behavioral change.** Every test must produce
an identical result before and after. If any test changes, revert everything.

---

## Background

E2 investigation (`cc_instruction_e2_investigate.md`) showed that migrating the
three progression signals to a true post-analysis pass requires a "scoring
snapshot" mechanism (E2b) not yet built. E2a is the preparatory code-organisation
step: move the lambda bodies to named free functions in the function layer.
`chordanalyzer.cpp` calls them from their current sites — nothing moves in
execution order. This establishes the function layer as the authoritative home
for progression-signal logic and creates the seam for E2c.

Three signals to extract:
1. `rootContinuityBonus` — in `bassIndependentContextualBonuses` (~L1652 in
   `chordanalyzer.cpp`); also the parallel site in `contextualBonuses()` (~L1478,
   used only by `diagnoseChord`).
2. `wSeqBonus` lambda — joint-scoring loop (~L2235).
3. `wDimBonus` lambda — joint-scoring loop (~L2254).

---

## Part A — Read before touching any file

Read the following in `chordanalyzer.cpp`:

1. `bassIndependentContextualBonuses` function — exact lines and signature; the
   `previousRootPc == rootPc` block; whether `context` can be null at that site.
2. `contextualBonuses` function — the parallel `rootContinuityBonus` site
   (~L1478); confirm it mirrors the one above.
3. `wSeqBonus` lambda (~L2235) — full body including the `static constexpr double
   kWSeq` declaration and the call site at ~L2382.
4. `wDimBonus` lambda (~L2254) — full body including the `static constexpr double
   kWDim` declaration and the call site within the dual-scoring loop.
5. The existing `#include` list at the top of `chordanalyzer.cpp` — confirm that
   `composing/analysis/function/harmonicfunctionlayer.h` is NOT yet included.

Confirm exact line numbers before proceeding.

---

## Part B — Add free functions to the function layer

### B1 — `harmonicfunctionlayer.h`

Add the following inside `namespace mu::composing::function`, after the existing
`HarmonicFunctionContext` struct and before the closing brace:

```cpp
// -----------------------------------------------------------------------
// Progression-signal bonus functions (E2a: called from chordanalyzer.cpp
// at their existing call sites; will become a post-analysis pass in E2c).
// -----------------------------------------------------------------------

/// Bonus magnitude constants — defined here because they are function-layer
/// properties, not scoring-model constants.
inline constexpr double kWSeq = 0.20;  ///< Sequential root-progression bonus (Iter 95)
inline constexpr double kWDim = 0.15;  ///< Dim/HalfDim leading-tone bonus (Iter 96)

/// Root-continuity bonus.
/// Returns bonusValue when candidateRootPc == previousRootPc, else 0.
/// Called from bassIndependentContextualBonuses (and diagnoseChord path).
double rootContinuityBonus(int candidateRootPc, int previousRootPc,
                           double bonusValue);

/// Sequential root-motion bonus (+kWSeq).
/// Rewards a candidate whose root sits a P4 below nextRootPc (classic V→I).
/// Callers pass nextRootPc = context->nextRootPc, or -1 if context is null.
double wSeqBonus(int candRootPc, int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode);

/// Diminished/HalfDim leading-tone bonus (+kWDim).
/// Rewards a Dim/HalfDim candidate whose root sits one semitone below
/// nextRootPc (leading-tone-of-next). For the with-wDim path only.
/// Callers pass nextRootPc = context->nextRootPc, or -1 if context is null.
double wDimBonus(int candRootPc, analysis::ChordQuality quality,
                 int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode);
```

### B2 — `harmonicfunctionlayer.cpp`

Add the implementations (all in `namespace mu::composing::function`):

```cpp
double rootContinuityBonus(int candidateRootPc, int previousRootPc,
                           double bonusValue)
{
    return (candidateRootPc == previousRootPc) ? bonusValue : 0.0;
}

double wSeqBonus(int candRootPc, int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode)
{
    if (!jointScoringEnabled || explorationMode) return 0.0;
    if (nextRootPc < 0 || distinctPcs < 4) return 0.0;
    const int delta = ((nextRootPc - candRootPc) % 12 + 12) % 12;
    return (delta == 5) ? kWSeq : 0.0;
}

double wDimBonus(int candRootPc, analysis::ChordQuality quality,
                 int nextRootPc, int distinctPcs,
                 bool jointScoringEnabled, bool explorationMode)
{
    if (!jointScoringEnabled || explorationMode) return 0.0;
    if (nextRootPc < 0 || distinctPcs < 4) return 0.0;
    using Q = analysis::ChordQuality;
    if (quality != Q::Diminished && quality != Q::HalfDiminished) return 0.0;
    const int delta = ((nextRootPc - candRootPc) % 12 + 12) % 12;
    return (delta == 1) ? kWDim : 0.0;
}
```

---

## Part C — Update `chordanalyzer.cpp`

### C1 — Add include and namespace alias

At the top of `chordanalyzer.cpp`, after the existing analysis includes, add:

```cpp
#include "composing/analysis/function/harmonicfunctionlayer.h"
```

Add a namespace alias alongside the existing ones (if present):

```cpp
namespace fn = mu::composing::function;
```

### C2 — Replace `rootContinuityBonus` in `bassIndependentContextualBonuses`

Replace the existing inline block (the `previousRootPc == rootPc` check at ~L1660):

```cpp
// REMOVE:
if (context->previousRootPc == rootPc) {
    score += prefs.rootContinuityBonus;
}

// REPLACE WITH:
score += fn::rootContinuityBonus(rootPc, context->previousRootPc,
                                  prefs.rootContinuityBonus);
```

### C3 — Replace `rootContinuityBonus` in `contextualBonuses`

Apply the identical replacement at the parallel site in `contextualBonuses()` (~L1478).
The two sites must stay in sync — this is the `||` invariant noted in scoring_model.md §5.

### C4 — Replace the `wSeqBonus` lambda

Remove the `static constexpr double kWSeq = 0.20;` line.

Replace the lambda body so it delegates to the function layer. Keep the lambda
wrapper so the call site at ~L2382 is unchanged:

```cpp
auto wSeqBonus = [&](int candRootPc) -> double {
    return fn::wSeqBonus(candRootPc,
                         context ? context->nextRootPc : -1,
                         distinctPcs,
                         jointScoringEnabled,
                         prefs.explorationMode);
};
```

### C5 — Replace the `wDimBonus` lambda

Remove the `static constexpr double kWDim = 0.15;` line.

Replace the lambda body. The dual-scoring structure (two parallel accumulators,
post-bonus quality guard) stays exactly as-is — do NOT touch that. Only the
lambda body changes:

```cpp
auto wDimBonus = [&](int candRootPc, analysis::ChordQuality quality) -> double {
    return fn::wDimBonus(candRootPc, quality,
                         context ? context->nextRootPc : -1,
                         distinctPcs,
                         jointScoringEnabled,
                         prefs.explorationMode);
};
```

**Important:** If the existing lambda signature differs from this (e.g. different
parameter names or no quality parameter), adjust to match the actual code. Do NOT
change the dual-scoring structure, the call sites, or the post-bonus quality guard.
Report any discrepancy.

---

## Part D — Build and verify zero behavioral change

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2a.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2a.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2a.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2a.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2a.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2a.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped) —
byte-identical to baseline. If any count changes at all, revert everything.**

Do NOT run BIR — code organisation only cannot change BIR.

---

## Part E — Commit

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.h \
  src/composing/analysis/function/harmonicfunctionlayer.cpp \
  src/composing/analysis/chord/chordanalyzer.cpp; echo "exit:$?"

cd C:\s\MS && git commit -m "E2a: move progression-signal lambdas to function layer (code organisation)

rootContinuityBonus, wSeqBonus, wDimBonus are now free functions in
src/composing/analysis/function/harmonicfunctionlayer.{h,cpp}.
chordanalyzer.cpp calls them from their existing sites via thin lambda
wrappers — execution order and call sites are unchanged.

kWSeq (0.20) and kWDim (0.15) constants moved to harmonicfunctionlayer.h.
rootContinuityBonus uses prefs.rootContinuityBonus (0.40) as before.

The dual-scoring structure for w_dim (two parallel accumulators, post-bonus
quality guard) is not touched — it stays in analyzeChord().

This is code organisation only. E2b will expose a scoring snapshot;
E2c will use it to make the function layer a true post-analysis pass.

Zero behavioral change. All tests identical to HEAD dd29a04967."; echo "exit:$?"
```

---

## Report back

1. Exact lines replaced in `chordanalyzer.cpp` for each of the five substitutions
2. Confirm both `rootContinuityBonus` sites (L1478 and L1660) were updated
3. Test results — confirm all three suites byte-identical to baseline
4. Commit hash
5. Any discrepancy between the actual lambda signature and what's prescribed above
   (report but do not deviate from the prescribed logic)
