# Iteration 72: PC-count adaptive score threshold + Dvorak test re-anchor

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration

Baselines (verify against STATUS.md): BIR=true=5, BIR=false=125. Jazz BIR=false=12.
(Iter 71 head 415b3ba563 — tuplet alignment + narrow Fix A. Bridge still on Jaccard.)

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background and confirmed root cause

Six notation tests fail when the bridge is switched to greedy-expand.
Five are Corelli op01n08d failures. The root cause is now fully diagnosed:

All five failing Corelli ticks have note-onset events and ARE present in
`collectNoteChangeTicks()` output. The failure is Hypothesis H2: the candidate
region's `analyzeChord` winner score falls below `effectiveAnchorMinScore`
(Round 1) and `effectiveRound2MinScore` (Round 2) because the pitch content
is thin — either a single pitch class (G unison) or a dyad (G+B, G+Bb).

The score thresholds (1.5 / 1.25) were calibrated against SATB regions with
3–4 pitch classes where full triads or seventh chords are the norm. The
maximum achievable `analyzeChord` winner score for a 1- or 2-PC region is
structurally below these thresholds even for a perfectly matched chord:
there simply are not enough tones to accumulate weight across a template.

The fix: apply a per-region PC-count factor to the score threshold at
evaluation time. For 1-PC regions the threshold drops toward the actual
achievable score; for 2-PC regions it relaxes proportionally; for 3+ PC
regions it remains unchanged. SATB chorales always have 3+ PCs per region
so BIR should self-calibrate.

The sixth failing test (`HarmonicAnnotationKeepsRomanAtLowConfidenceNoteContext`)
is a Jaccard fragmentation artifact — greedy-expand's behavior is musically
correct and the test should be re-anchored to a genuinely ambiguous region.

---

## Step 1 — Read before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp` in full.

Locate every comparison of the form:
- `winnerScore >= ...` or `score >= ...` in the Round 1 anchor promotion block
- `initialScore >= ...` or `score >= ...` in the Round 2 gap-fill block

These are the threshold comparison sites that will receive the PC-count factor.

Also read `src/composing/analysis/chord/chordanalyzer.h` to confirm the return
type of `analyzeChord` — specifically what field holds the winner score and
what type holds the tone vector (needed for PC counting in Step 3).

---

## Step 2 — Measure actual scores at the five failing Corelli ticks

Before writing any formula, measure what `analyzeChord` actually produces at
each failing tick. Add a temporary `fprintf(stderr, ...)` diagnostic to
`greedyExpandSegmentation()` that fires when the score path contains
"corelli" (case-insensitive) and prints for every Round 0 candidate:

```
DIAG tick=%d pcCount=%d winnerScore=%.4f winnerRoot=%d
```

Build `batch_analyze` only. Run on the Corelli fixture:

```bash
cd C:\s\MS\ninja_build_rel && ./batch_analyze \
    ../src/notation/tests/data/corelli_op01n08d.mscx 2>&1 | grep DIAG
```

(Adjust path to the fixture as needed — find it with grep in src/notation/tests/.)

From the output, report for each of the five failing ticks (960, 8160, 10080,
13920, 15360):
- pcCount (number of distinct pitch classes in the collected tones)
- winnerScore (what analyzeChord returned)
- winnerRoot

These measured scores drive the threshold formula in Step 3.

---

## Step 3 — Implement PC-count adaptive threshold

From the Step 2 measurements, derive a scaling formula that satisfies:

1. For 3+ PC regions: effective threshold = kAnchorMinScore (unchanged)
2. For the failing 1-PC regions: effective threshold ≤ measured winnerScore × 0.95
   (5% margin below the actual score so it just passes)
3. For the failing 2-PC regions: effective threshold ≤ measured winnerScore × 0.95
4. Monotonically increasing: T(1) < T(2) < T(3) = kAnchorMinScore

A linear formula that satisfies these constraints:

```cpp
/// Number of distinct pitch classes sounding in a candidate region's tone set.
static int countDistinctPCs(const std::vector<analysis::ChordAnalysisTone>& tones)
{
    std::bitset<12> seen;
    for (const auto& t : tones) {
        if (t.pitchClass >= 0 && t.pitchClass < 12) {
            seen.set(static_cast<size_t>(t.pitchClass));
        }
    }
    return static_cast<int>(seen.count());
}

/// Per-region score threshold scaled by pitch-class density.
/// kFullPCThreshold = kAnchorMinScore (or kRound2MinScore for Round 2).
static double pcAdaptiveThreshold(double kFullPCThreshold,
                                   int regionPCCount,
                                   double kPCFloorFraction)
{
    // kPCFloorFraction: fraction of kFullPCThreshold applied at 1 PC.
    // Derived from Step 2 measurements — adjust before committing.
    // At 3+ PCs: full threshold. Linear interpolation below 3.
    const double fraction = (regionPCCount >= 3)
        ? 1.0
        : kPCFloorFraction + (1.0 - kPCFloorFraction)
          * (regionPCCount - 1) / 2.0;
    return kFullPCThreshold * fraction;
}
```

The constant `kPCFloorFraction` must be derived from the Step 2 data:

```
kPCFloorFraction = min(measured 1-PC winnerScore) × 0.95 / kAnchorMinScore
```

If there are no 1-PC failing ticks with a valid score, derive from the 2-PC
data with appropriate scaling. Document the derivation in a comment.

Apply `pcAdaptiveThreshold()` at each Round 1 and Round 2 score comparison
site found in Step 1, passing the candidate region's collected tones. The
`countDistinctPCs()` helper runs on the same `tones` vector already available
at the comparison site — no additional data collection needed.

**Important**: apply the factor per-region at comparison time, not globally.
The global `effectiveAnchorMinScore` from Iter 69 is unchanged; the PC-count
factor is an additional local adjustment.

---

## Step 4 — Build and run tests (bridge on Jaccard)

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Confirm binary timestamps. Then:

```bash
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Required: 407/407 composing, 53/53 notation. Bridge is still on Jaccard at
this point — notation tests must pass regardless. Any failure here means the
PC-count threshold introduced a regression. Stop and report.

---

## Step 5 — BIR validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Hard stops — revert all harmonicsegmenter.cpp changes and report if:
- BIR=true ≠ 5
- BIR=false ≠ 125

Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz hard stop: BIR=false > 75 (current 12). Restore Baroque corpus after.

---

## Step 6 — Update STATUS.md and commit PC-count fix

Remove the Step 2 diagnostic `fprintf` before committing.

Update `C:\s\MS\STATUS.md`: set HEAD commit, confirm BIR unchanged, set
active iteration to "Iter 72 Part A committed / bridge switch pending".

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add C:\s\MS\STATUS.md
git commit -m "Composing: PC-count adaptive score threshold in greedy-expand (Iter 72)

Apply per-region pitch-class-count factor to anchor promotion and Round 2
gap-fill score thresholds in greedyExpandSegmentation().

Root cause (confirmed): Corelli trio sonata dominant beats contain 1-2
distinct PCs (G unison; G+B or G+Bb dyad). Maximum achievable analyzeChord
winner score for thin-PC regions is structurally below the SATB-calibrated
thresholds (1.5 / 1.25), causing valid dominant anchors to be suppressed.

Fix: pcAdaptiveThreshold() scales threshold by kPCFloorFraction at 1 PC,
linearly interpolating to the full threshold at 3+ PCs. SATB chorales
always have 3+ PCs and self-calibrate to the existing thresholds.

kPCFloorFraction = N (derived from measured scores at failing Corelli ticks).
BIR=true=5, BIR=false=125 unchanged. Jazz BIR=false=N."

git push
```

---

## Step 7 — Re-anchor Dvorak low-confidence test

The test `HarmonicAnnotationKeepsRomanAtLowConfidenceNoteContext` in
`src/notation/tests/notationimplode_tests.cpp` was written against Jaccard's
region fragmentation. Greedy-expand correctly subsumes the artificial low-
confidence pocket into a larger confident region (0.76 vs expected < 0.5).
The musical situation does not justify low confidence at the chord level.

Re-anchor the test to the genuinely ambiguous region at m4 b2 of Dvorak
op08n06 (Bbsus/G vs F/G competing readings, chordScoreMargin ≈ 0.14). The
new assertion should verify that a note in that region has chord-level
ambiguity (margin < 0.2, or confidence < some threshold appropriate to the
actual greedy-expand output at that position). Do not assert a specific
confidence value less than 0.5 unless the actual measured value supports it.

Read the test carefully before modifying — understand what the test is
asserting and what the correct greedy-expand output is at the new anchor
position. The test must pass after re-anchoring.

```bash
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Commit the re-anchored test:

```bash
git add src/notation/tests/notationimplode_tests.cpp
git add C:\s\MS\STATUS.md
git commit -m "Test: re-anchor HarmonicAnnotationKeepsRomanAtLowConfidence to greedy-expand

Previous anchor (Dvorak op08n06 low-confidence pocket) was a Jaccard
fragmentation artifact — greedy-expand correctly subsumes the transient
passage into a larger confident region.

Re-anchored to m4 b2 (Bbsus/G vs F/G, margin ~0.14) — a genuinely
ambiguous chord reading in the same piece. Test now validates chord-level
ambiguity rather than Jaccard-specific segmentation."

git push
```

---

## Step 8 — Re-attempt bridge switch

Re-apply the bridge change: replace `detectHarmonicBoundariesJaccard()` in
`src/notation/internal/notationcomposingbridgehelpers.cpp` with
`greedyExpandSegmentation()` + `placedRegionsToTicks()` +
`HarmonicSegmenterCallbacks`.

Build and run notation tests:

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

**If 53/53 pass:**

```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Update STATUS.md: mark §2.10 resolved, set active iteration "Iter 72 complete".

```bash
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/
git add C:\s\MS\STATUS.md
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Replace detectHarmonicBoundariesJaccard() with greedyExpandSegmentation().
PC-count adaptive thresholds (Iter 72) allow greedy-expand to handle
sparse unison/dyad dominant entries in Corelli trio sonata and similar
textures. Iters 69-72 together make greedy-expand texture-general.

Bridge and batch paths now use the same segmentation algorithm (§2.10).
Pipeline snapshot goldens refreshed.
BIR=true=5, BIR=false=125. Jazz BIR=false=N."

git push
```

**If tests still fail:** report remaining failures with actual vs expected.
Revert bridge file. Do not commit bridge change.

---

## Step 9 — Report to Cowork

```
Step 2 — Measured scores at failing Corelli ticks:
  tick  960 (m1  b3): pcCount=N winnerScore=N.NN winnerRoot=N
  tick 8160 (m6  b3): pcCount=N winnerScore=N.NN winnerRoot=N
  tick 10080 (m8  b1): pcCount=N winnerScore=N.NN winnerRoot=N
  tick 13920 (m10 b3): pcCount=N winnerScore=N.NN winnerRoot=N
  tick 15360 (m11 b3): pcCount=N winnerScore=N.NN winnerRoot=N

kPCFloorFraction chosen: N.NN (derived from: ...)

Tests (bridge on Jaccard, after PC-count fix):
  composing: N/407
  notation: N/53

BIR=true: 5 → N
BIR=false: 125 → N
Jazz BIR=false: 12 → N

PC-count fix committed: [hash]

Dvorak test re-anchored: [yes — hash / describe new assertion]

Bridge switch:
  notation_tests: N/53
  Remaining failures (if any): [list with actual vs expected]
  Pipeline snapshot goldens refreshed: [yes / no]
  Committed: [hash / not committed — reason]

§2.10 status: [resolved / still blocked — remaining issue]
```
