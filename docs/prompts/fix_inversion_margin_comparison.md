# Fix: inversion correction margin comparison uses inflated raw scores

## Context loading — do this first

1. `CLAUDE.md` — standing instructions, build/test commands, autonomous-operation scope.
2. `STATUS.md` — top summary line and the `2026-05-04` entries only.
3. `src/composing/analysis/chord/chordanalyzer.cpp` — specifically:
   - The post-ranking inversion correction (~lines 1925–1970, look for the
     `// ── Inversion / bass-root bias correction ──` comment)
   - The `bassNoteRootBonus` constant (search for it; currently 0.70)

---

## What was diagnosed

Fix 3 (guaranteed-inversion-alternative append) resolved cap exhaustion: the
correct chord (e.g. Gm) now reaches `results[]` in the 151 three-way-confirmed
bassIsRoot errors. But the inversion correction still does not flip because the
margin check blocks it.

The margin check currently computes:

```cpp
const double margin = winner.score - bestAlt.score;
if (margin < inversionSuspicionMargin) { /* flip */ }
```

`winner.score` already includes the bass-root bonus (`bassNoteRootBonus` = 0.70,
stored in the candidate as `appliedBassBonus` before it was built into a
`ChordAnalysisResult`). In bass-heavy regions, the guaranteed-alt is appended
only because it barely clears the de-inflated threshold; its score is roughly
`(winner.score − 0.70) × 0.75`. The raw gap `winner.score − alt.score` is
therefore typically well above 1.40, far exceeding `inversionSuspicionMargin`
(0.70). The correction was designed to fire when "the bass bonus is the sole
advantage," but it measures the gap *after* the bonus has already widened it.

---

## The fix

**Goal:** compare de-bonused scores so the margin reflects the organic scoring
gap rather than the bass-bonus-inflated one.

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`

### Step 1 — Locate the margin computation

Find the inversion correction block (search for `inversionSuspicionMargin`).
Inside it, find the line that computes `margin` as the difference between
`winner.score` and the best alternative's score. It will look roughly like:

```cpp
const double margin = winner.score - bestAlt.score;   // (exact name may vary)
```

### Step 2 — Replace with de-bonused margin

`ChordAnalysisResult` does not store `appliedBassBonus` directly, but we can
recover it: the correction already guards on
`winner.identity.rootPc == winner.identity.bassPc`, so the winner is always
a bass-root candidate. For a bass-root winner the applied bonus equals
`bassNoteRootBonus` (the constant 0.70).

Replace the margin line with:

```cpp
// De-bonus the winner's score before comparing so the margin reflects the
// organic scoring gap.  The correction fires when the bass bonus is the
// primary (or sole) reason the winner leads the alternative; using the raw
// score inflates the gap by up to bassNoteRootBonus, incorrectly suppressing
// the flip for bass-heavy regions where the correct chord barely clears the
// admission threshold.
const double winnerDebonused = winner.score
    - (winnerBassIsRoot ? bassNoteRootBonus : 0.0);
const double margin = winnerDebonused - bestAlt.score;
```

`winnerBassIsRoot` is already evaluated just above this point in the correction
block; reuse it. `bassNoteRootBonus` is the constant already in scope.

### Step 3 — Verify the guard is still intact

The correction block should already have (from Fix 3's regression fix):

```cpp
if (prefs.inversionSuspicionMargin > 0.0 ...)
```

confirming it does not fire in Pass 2. Leave that guard exactly as is.

---

## What NOT to touch

- Do **not** change `inversionSuspicionMargin` (0.70), `bassNoteRootBonus`
  (0.70), `kScoreThresholdRatio`, or any other scoring constants.
- Do **not** touch the guaranteed-alt block added in Fix 3 or its Pass 2 guard.
- Do **not** touch `chordanalyzer_catalog.musicxml`.
- Do **not** commit — report results and wait for sign-off.

---

## Verification

### Build and test

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.
**Pass criterion:** 407/407 tests pass, RealDiff ≤ 4.

### Corpus analysis

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

### Report format

```
Build:              pass / fail
Tests:              N/N pass
RealDiff:           before=4, after=N
3-way genuine bassIsRoot errors:  before=151, after=N
2-way chord_disagree bassIsRoot:  before=805, after=N
Regressions:        none / <description>
Notes:              <anything unexpected>
```

If RealDiff increases, revert the change and report which cases regressed before
attempting any further tuning.
