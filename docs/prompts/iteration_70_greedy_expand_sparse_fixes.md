# Iteration 70: Fix greedy-expand sparse-texture failures (Task #58 prerequisite)

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration

Baselines (verify against STATUS.md): BIR=true=5, BIR=false=125. Jazz BIR=false=12.
(Iter 69 Part A committed b653f5a4a4 — texture-adaptive thresholds in harmonicsegmenter.cpp.)

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Iter 69 Part A implemented texture-adaptive thresholds (vertical + horizontal density).
BIR=5/125/Jazz=12 confirmed unchanged. However Part B (bridge switch) still fails
10 notation tests — the adaptive thresholds did not fix the Corelli/Dvorak failures.

Three distinct failure patterns remain:

**Pattern 1 — Empty regions / missing beats** (tests 3, 4, 6, 7, 10):
Sparse late-onset dominant entries (short-duration notes in Corelli trio) fail
Round 1's duration gate. The current `effectiveAnchorMinDurationTicks` still
rejects them even after Iter 69's relaxation because the DIVISION/4 absolute
floor or the horizontalFactor formula may not scale far enough for very sparse
textures. The entry is short but it is the only harmonic event in that stretch
— it is significant precisely because of the surrounding sparseness.

**Pattern 2 — Smearing** (tests 5, 6, 10):
Round 2 gap-fill has two tonic anchors far apart and fills the intervening gap
with the tonic chord, overwriting the sparse dominant that should appear at one
specific beat. The bilateral context from distant anchors dominates the local
note-change evidence. When the gap is long (sparse horizontal), Round 2 should
prefer the candidate's own local chord identity over the distant bilateral blend
— especially when the local chord differs from both neighbors.

**Pattern 3 — Sustained support threshold** (tests 1, 2):
`effectiveStaveThreshold` is computed from `nEligibleStaves` (total eligible
staves in the score) rather than `meanActiveStaves` (average staves concurrently
active). For a 2-staff fixture where staves alternate, nEligibleStaves=2 gives
threshold=2 but individual beats only have 1 staff active → the gate never fires.
The threshold base must be `meanActiveStaves`, not `nEligibleStaves`.

---

## Step 1 — Read before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp` in full. Locate:
1. Where `effectiveStaveThreshold` is computed — confirm it uses `nEligibleStaves`
2. Where `effectiveAnchorMinDurationTicks` is computed — note the floor value
3. Round 2 gap-fill logic — understand how bilateral context is blended with
   local candidate score to produce the placed chord identity

Also read the failing test fixtures to understand the actual note durations
involved. For Corelli op01n08d, look at the sparse late-dominant entries
(the beats expected to carry "G" that are instead empty or carry "Cm"):
what are their actual tick durations in the score?

Report the actual durations of the failing Corelli dominant entries in the
Step 9 report — this validates the duration fix.

---

## Step 2 — Fix Pattern 3: threshold base

In the pre-measurement pass, change the staff count threshold computation
from using `nEligibleStaves` to using `meanActiveStaves`:

```cpp
// Was: max(1, round(nEligibleStaves * 0.75))
// Now: based on how many staves are actually active on average
const int effectiveStaveThreshold
    = std::max(1, static_cast<int>(std::round(meanActiveStaves * 0.75)));
// SATB (meanActive ≈ 3.5):  round(2.625) = 3  ← matches prior behaviour
// Trio alternating (≈ 1.5): round(1.125) = 1
// Piano alternating (≈ 1.0): round(0.75) = 1
```

`nEligibleStaves` is still needed for the staff-count pre-loop —
only the threshold formula changes.

---

## Step 3 — Fix Pattern 1: duration floor

From the Step 1 investigation, you know the actual tick durations of the
failing Corelli dominant entries. The duration floor must sit below those
durations for the entries to make Round 1.

Change the duration floor so it scales with `meanTickSpacing` rather than
being an absolute constant. The principle: in a sparse texture (few events,
large mean spacing), even a short entry is significant. The floor should be
a fraction of `meanTickSpacing`:

```cpp
// Floor scales with horizontal density:
// sparse (large meanTickSpacing) → lower floor → short entries eligible
const int durationFloor
    = std::max(mu::engraving::Constants::DIVISION / 8,
               static_cast<int>(meanTickSpacing * 0.1));

const int effectiveAnchorMinDurationTicks
    = std::max(durationFloor,
               static_cast<int>(kAnchorMinDurationTicks * horizontalFactor));
```

Adjust the `0.1` multiplier based on the actual failing entry durations from
Step 1 — it must be low enough that those entries pass. For SATB
(meanTickSpacing ≈ DIVISION, horizontalFactor ≈ 1.0):
`max(DIVISION/8, DIVISION×0.1) = max(DIVISION/8, DIVISION/10) = DIVISION/8`
for the floor, and `max(DIVISION/8, DIVISION) = DIVISION` for the threshold —
so SATB is unchanged. Verify this self-calibration before proceeding.

---

## Step 4 — Fix Pattern 2: Round 2 local-evidence preference

This is the most surgical change. In Round 2 gap-fill, when a candidate's own
local `analyzeChord` result identifies a chord that differs from the bilateral
blend AND the local score is >= `effectiveRound2MinScore`:

- Keep the candidate's local chord identity (rootPitchClass, bassPitchClass,
  quality, confidence from local analysis)
- Do NOT override it with the bilateral blend chord identity
- The bilateral context is still used to decide whether to promote the
  candidate at all (score gate) — only the chord identity assignment changes

The condition to check before applying any bilateral chord-identity override:

```cpp
if (candidate.confidence >= effectiveRound2MinScore
    && candidateChordDiffersFromBilateral(candidate, leftAnchor, rightAnchor)) {
    // Trust local evidence — keep candidate's own chord
    placed.rootPitchClass = candidate.rootPitchClass;
    placed.bassPitchClass = candidate.bassPitchClass;
    placed.quality        = candidate.quality;
    placed.confidence     = candidate.confidence;
    placed.reason         = "round2-local-preferred";
} else {
    // Bilateral blend as before
    ...
}
```

Define `candidateChordDiffersFromBilateral` as: candidate root PC differs from
both left and right anchor root PCs. Do not parse quality strings — compare
rootPitchClass integers only.

Additionally, scale the Round 2 bilateral preference by gap length: if the gap
spans more than `4 × effectiveAnchorMinDurationTicks`, reduce the bilateral
context weight so local evidence dominates more strongly. Read the current
Round 2 implementation first — adapt to its actual structure rather than
forcing this exact pattern.

---

## Step 5 — Build and run all tests

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Confirm binary timestamps before running tests.

```bash
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

At this stage the bridge is still on Jaccard — notation tests must pass 53/53.
Any failure here means the sparse fixes introduced a batch-path regression —
stop and report which tests fail and what changed.

---

## Step 6 — BIR validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

**Hard stops — revert all changes and report if:**
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

## Step 7 — Update STATUS.md and commit sparse fixes

Update `C:\s\MS\STATUS.md`:
- Set HEAD commit to the new hash
- Confirm BIR baselines unchanged
- Set active iteration to "Iter 70 committed / bridge switch pending"

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add C:\s\MS\STATUS.md
git commit -m "Composing: fix greedy-expand sparse-texture failures (Iter 70)

Three targeted fixes to greedyExpandSegmentation():

1. Threshold base: effectiveStaveThreshold now uses meanActiveStaves
   (avg concurrent staves) instead of nEligibleStaves (total eligible).
   Fixes alternating-staff fixtures (piano, duo) where no single beat
   has all eligible staves active.

2. Duration floor: scales with meanTickSpacing so short-duration
   note-change events in sparse horizontal textures reach Round 1
   anchor eligibility. Floor = max(DIVISION/8, meanTickSpacing*0.1).

3. Round 2 local-evidence preference: when a gap candidate's own
   chord identity differs from bilateral context and scores above
   effectiveRound2MinScore, the local chord is kept rather than
   overridden by distant anchor blend. Prevents tonic smearing across
   long gaps containing clear dominant entries.

BIR=true=5, BIR=false=125 unchanged. Jazz BIR=false=N."

git push
```

---

## Step 8 — Re-attempt bridge switch

Re-apply the Iter 68/69 bridge change: replace `detectHarmonicBoundariesJaccard()`
in `src/notation/internal/notationcomposingbridgehelpers.cpp` with
`greedyExpandSegmentation()` + `placedRegionsToTicks()` + `HarmonicSegmenterCallbacks`.

Build, then run notation tests:
```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

**If 53/53 pass:**
```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Update STATUS.md: mark §2.10 resolved, set active iteration to "Iter 70 complete".

```bash
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/
git add C:\s\MS\STATUS.md
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Replace detectHarmonicBoundariesJaccard() with greedyExpandSegmentation()
in notationcomposingbridgehelpers.cpp. Sparse-texture fixes in Iter 70
allow greedy-expand to handle Corelli trio, Dvorak, and small piano fixtures.

Bridge and batch paths now use the same segmentation algorithm (§2.10).
Pipeline snapshot goldens refreshed.

BIR=true=5, BIR=false=125. Jazz BIR=false=N."

git push
```

**If any tests still fail:** report each remaining failure with actual vs
expected (same format as Iter 68/69 reports). Do not update assertions.
Revert the bridge file. Do not commit the bridge change.

---

## Step 9 — Report to Cowork

```
Sparse-texture investigation:
  Corelli sparse dominant entry durations (actual ticks): N
  Duration floor chosen: N  (= meanTickSpacing × N at Corelli density)

Fix summary:
  Pattern 1 (empty regions): duration floor now N — entries pass Round 1: [yes/no]
  Pattern 2 (smearing): local-evidence preference applied at N cases: [describe]
  Pattern 3 (sustained support): threshold base = meanActiveStaves → threshold=1
    for alternating-staff fixture: [yes/no]

Tests (bridge on Jaccard, before bridge switch):
  composing: N/407
  notation: N/53

BIR=true: 5 → N
BIR=false: 125 → N
Jazz BIR=false: 12 → N

Sparse fix committed: [hash]

Bridge switch (Part B):
  notation_tests: N/53
  Remaining failures (if any): [list]
  Pipeline snapshot goldens refreshed: [yes/no]
  Committed: [hash / not committed — reason]

§2.10 status: [resolved / still blocked — remaining issue]
```
