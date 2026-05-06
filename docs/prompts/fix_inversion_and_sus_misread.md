# Fix: Inversion Confusion and Sus Misread in ChordAnalyzer

## Context loading — do this first, before anything else

Read these files before touching any code:

1. `CLAUDE.md` — standing instructions, autonomous-operation pre-authorization, build/test commands.
2. `STATUS.md` — read only the top summary line and the `2026-04-25 → 2026-05-04` rollup section; the rest is historical.
3. `src/composing/analysis/chord/chordanalyzer.cpp` — read the whole file or at minimum:
   - The `RawCandidate` struct and the scoring loop (~lines 1668–1720)
   - `structuralPenalties()` (~lines 1159–1250)
   - The post-ranking inversion correction (~lines 1859–1938)

You do not need ARCHITECTURE.md, unified_analysis_pipeline.md, or the memory files for this task.

---

## What has been diagnosed

Two systematic failure modes were identified by corpus analysis across 353 Bach chorales.

### Issue 1 — Inversion confusion (491 cells, 60% of corpus)

When a chord is in first inversion (the third of the chord is in the bass), the analyzer
names the bass note as the root instead of the actual chord root.

Top mispairs: Gm7/Bb → Bb6, Am7/C → C6, Em7/G → G6 — the enharmonic-equivalent
added-sixth reading wins over the correct minor-seventh reading.

### Issue 2 — Sus misread (210 cells, 38% of corpus)

The analyzer labels a region as a sus chord when the ground truth is a non-sus chord.
The driving pattern is: passing or suspension P4 tones accumulate enough regional weight
to clear the sus-template's structural penalty threshold, so the sus template wins when
the underlying harmony is a triad or seventh chord.

Top mispairs: Dsus/Esus/Gsus wins where GT says major triad, minor triad, or a
non-diatonic trichord.

### Root mechanism — shared by both issues

Inside `analyzeChord()`, after scoring all 12 × 16 root × template combinations, results
are kept above a 75%-of-winner threshold:

```cpp
// chordanalyzer.cpp line 1711
const double threshold = bestRawScore * kScoreThresholdRatio;   // kScoreThresholdRatio = 0.75
```

The winner's score is inflated by the bass-root bonus (+0.70 maximum). For `Minor7`
templates whose root is not the bass, `nonBassAdjustment` adds −0.35. Combined, the
scoring gap between the bass-root winner and its enharmonic non-bass equivalent is up
to **1.05**. When the non-bass chord tones have low weight (bass-heavy/sparse-upper-voice
regions — common in Bach chorales where the bass note is sustained and upper voices move
quickly), this 1.05 gap exceeds 25% of the winner's score and the correct chord falls
below the threshold and is never added to `results[]`.

The post-ranking inversion correction at lines ~1859–1938 cannot fire because there is
nothing to correct against — the correct chord was never admitted to results in the
first place.

Issue 2 has the same threshold-exclusion pathway for its bass-driven cases. It also has
a secondary pathway: even when the correct chord is not excluded, a passing P4 with
weight ≥ 0.20 (the current `extensionThreshold`) prevents the `kSus4MissingFourth`
penalty (−0.70) from firing, so the sus template wins on quality even when the root
assignment is correct.

---

## Fix 1 — Threshold de-inflation  (addresses Issue 1 fully; Issue 2 bass-driven cases)

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`

**Locate** the two lines after the rawCandidates sort (currently line 1711):

```cpp
const double bestRawScore = rawCandidates.empty() ? 0.0 : rawCandidates.front().score;
const double threshold = bestRawScore * kScoreThresholdRatio;
```

**Replace with:**

```cpp
const double bestRawScore = rawCandidates.empty() ? 0.0 : rawCandidates.front().score;

// De-inflate the threshold when the best-scoring candidate's lead comes from a
// bass-root bonus.  A bass-inflated winner sets an artificially high bar that
// can exclude its enharmonic non-bass alternative (e.g. Gm7 when Bb6 wins, or
// the correct non-sus chord when a sus template wins from the bass note).
// Using the de-bonused score as the threshold base ensures those alternatives
// survive into results[] where the post-ranking inversion correction can
// evaluate and flip them.
// When the winner carries no bass bonus (winnerBassBonus == 0) this is
// identical to the original formula.
const double winnerBassBonus = rawCandidates.empty()
                               ? 0.0
                               : rawCandidates.front().appliedBassBonus;
const double threshold = (bestRawScore - winnerBassBonus) * kScoreThresholdRatio;
```

**Why this is safe:**

- `appliedBassBonus` is already computed per candidate in the scoring loop and stored in
  `RawCandidate::appliedBassBonus`. No new computation required.
- The winner always exceeds the new threshold: `bestRawScore ≥ (bestRawScore − bonus) × 0.75`
  holds for any `bonus ≤ bestRawScore`.
- No sort order, no score values, no other candidate relationships change — only the
  admission cut for the results window is lowered by `winnerBassBonus × 0.75`.
- When the winner has no bass bonus (any non-bass-root winner) the formula is identical
  to before: zero change in behavior.

---

## Fix 2 — Sus structural fourth threshold  (addresses Issue 2 non-bass-driven cases)

For sus mislabels where Fix 1 does not apply (because the root assignment happens to be
correct but the quality is wrong), the `kSus4MissingFourth` penalty (−0.70) is gated on
whether the P4's pcWeight falls below `extensionThreshold` (0.20). Any passing or
grace-note fourth that lingers in the regional window long enough to accumulate
pcWeight ≥ 0.20 clears this bar, the penalty does not fire, and the sus template wins.

A genuine suspension tone is held across a beat boundary and accumulates weight
comparable to a structural chord tone (typically ≥ 0.5 in a regional window). Passing
fourths that trigger the current bug typically land in the 0.20–0.45 range.

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`

**Step 1 — Add a constant** in the sus-penalty constants block (around line 686,
immediately after `kSus4MissingFourth`):

```cpp
/// Minimum pcWeight for the defining P4 to be treated as a structural suspension
/// tone.  Below this, the Sus4 template is penalised even when the P4 is
/// technically present — passing or ornamental fourths routinely clear 0.20
/// (extensionThreshold) but rarely reach 0.50.
static constexpr double kSus4StructuralFourthThreshold = 0.50;
```

**Step 2 — In `structuralPenalties()`**, locate the sus4 P4 check (currently line ~1185):

```cpp
if (sus4HasPerfectFourth && !isSus4FlatFive) {
    const int fourthPc = static_cast<int>((rootPc + 5) % 12);
    if (pcWeight[static_cast<size_t>(fourthPc)] < extThreshold) {
        score -= kSus4MissingFourth;
    }
}
```

**Replace with:**

```cpp
if (sus4HasPerfectFourth && !isSus4FlatFive) {
    const int fourthPc = static_cast<int>((rootPc + 5) % 12);
    if (pcWeight[static_cast<size_t>(fourthPc)] < kSus4StructuralFourthThreshold) {
        score -= kSus4MissingFourth;
    }
}
```

**Note on regression risk:** This is the change most likely to disturb the existing test
suite. Raising the threshold from 0.20 to 0.50 means genuine sus4 chords where the P4
accumulates weight 0.20–0.49 now get the penalty applied. If the mismatch report shows
new RealDiffs, follow the tuning protocol in the Verification section below before
deciding on the final constant value.

---

## What not to touch

- Do **not** change `kScoreThresholdRatio` (0.75). Fix 1 adjusts the base, not the ratio.
- Do **not** change `kNonBassPenalty` (0.35). The penalty is correct for the root-position
  preference; the fix is in the threshold, not the penalty.
- Do **not** modify `inversionSuspicionMargin`, `inversionBonusReduction`, or any of the
  post-ranking correction parameters at lines ~1859–1938 — those are not the problem.
- Do **not** modify `chordanalyzer_catalog.musicxml`. Catalog changes require explicit
  approval.
- Do **not** commit. Report results and wait for sign-off.

---

## Verification

### Step 1 — Build

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
```

Fix any build errors before proceeding.

### Step 2 — Run tests

```
cd C:\s\MS\ninja_build && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.

**Pass criterion:** All tests pass. `kRealDiffBaseline = 4` in
`chordanalyzer_musicxml_tests.cpp`; the mismatch report must show RealDiff ≤ 4.

**If RealDiff count increases (regression):**

1. Revert Fix 2 only (the sus threshold change). Rebuild and retest. If RealDiff returns
   to 4, the regression is from Fix 2.
2. If Fix 2 is the cause, lower `kSus4StructuralFourthThreshold` in 0.05 steps
   (0.45 → 0.40 → 0.35) until the regression disappears. Report the final value used
   and the RealDiff count at each step.
3. If reverting Fix 2 does not resolve the regression, revert Fix 1 as well and report
   which change caused it — do not attempt further fixes in that session.

**If RealDiff count decreases:** This means the fixes corrected real errors in the
synthetic catalog too. Document which RealDiff entries disappeared and report that.

### Step 3 — Report format

```
Build:         pass / fail
Tests:         N/N pass
RealDiff:      before=4, after=N
Fix 1 change:  <show exact before/after lines>
Fix 2 change:  <show exact before/after lines, including final threshold value>
Regressions:   none / <description>
Notes:         <anything unexpected>
```
