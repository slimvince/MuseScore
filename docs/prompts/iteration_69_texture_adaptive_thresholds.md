# Iteration 69: Texture-adaptive thresholds in greedy-expand (Task #58 prerequisite)

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration

Baselines (verify against STATUS.md before proceeding): BIR=true=5, BIR=false=125. Jazz BIR=false=12.
(Iter 67 committed dc52617762 — greedy-expand extracted to harmonicsegmenter.h.)

Build fresh before every BIR measurement. Verify binary is newer than source.

**This is a two-part iteration:**
- **Part A**: Make greedy-expand's anchor-promotion thresholds adaptive to the
  score's texture density. BIR must remain exactly 5/125 — SATB chorales must
  self-calibrate to approximately the current constants.
- **Part B**: Re-attempt the Iter 68 bridge switch. Only if Part A validates.

---

## Background

Greedy-expand was tuned against Baroque SATB chorales (dense vertical texture,
regular horizontal rhythm). Its anchor-promotion criteria are hardcoded for this
texture:

- Staff count gate: Round 1 requires ≥3 chord-bearing staves (hardcoded)
- `kAnchorMinScore = 1.5` — minimum chord score for anchor eligibility
- `kAnchorMinDurationTicks = 1×DIVISION` — minimum region duration
- `kRound2MinScore = 1.25` — Round 2 gap-fill minimum score

Iter 68 showed these fail on sparse textures (Corelli trio sonata, Dvorak):
- **Vertical sparseness** (few concurrent voices): chord scores are naturally
  lower when fewer voices confirm the harmony → score gate too strict → valid
  anchors not promoted → boundaries missed → smearing.
- **Horizontal sparseness** (infrequent note-change events): sparse single-onset
  dominant entries don't accumulate enough score/duration to make Round 1 →
  absorbed into surrounding tonic/subdominant regions.

The Baroque BIR pipeline was unaffected because it only exercises SATB chorales.
The failing tests (9 from Notation_ImplodeTests) are the actual quality signal
for sparse polyphonic textures through the bridge path.

**Jaccard handled sparse textures correctly because its similarity measure is
density-agnostic** — it asks "how different is the pitch content?" regardless of
voice count. Greedy-expand must gain the same property through adaptive thresholds.

Texture density has two independent dimensions:
- **Vertical density**: average number of concurrent eligible staves/voices active
  at any note-change tick
- **Horizontal density**: average gap between note-change ticks (larger gap =
  sparser in time)

---

## Step 1 — Read before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp` in full.

Locate and note line numbers for:
1. Every use of the ≥3 staff count comparison (inside `countParticipatingStaves`
   call site or surrounding logic)
2. Every comparison against `kAnchorMinScore`
3. Every comparison against `kAnchorMinDurationTicks`
4. Every comparison against `kRound2MinScore`
5. Where `collectNoteChangeTicks()` is called — this is where the pre-measurement
   pass will be inserted

Also read `src/composing/analysis/harmony/harmonicsegmenter.h` for the constants
and `HarmonicSegmenterCallbacks` definition.

---

## Step 2 — Investigate chord score scaling with voice count

Before writing any adaptive formula, determine how `analyzeChord` winner scores
scale with the number of active voices in practice.

Read the existing test fixtures and their expected scores, or add a temporary
diagnostic: for a sample of regions in the Baroque corpus output
(`tools/corpus/`), cross-reference region duration / staff count against the
confidence values stored in `PlacedRegion.confidence`.

Answer: for a 4-voice SATB region, what is a typical Round 1 anchor confidence?
For a 2-voice region? For a 1-voice region? This determines the scaling factor
for `effectiveAnchorMinScore`.

Report these values in the Step 9 report.

---

## Step 3 — Add texture-density pre-measurement pass

Immediately after `collectNoteChangeTicks()` returns in
`greedyExpandSegmentation()`, add a pre-measurement pass. All data needed is
already available at this point.

**Eligible stave count** (compute once, used in threshold formula):
```cpp
int nEligibleStaves = 0;
for (size_t s = 0; s < score->nstaves(); ++s) {
    if (!excludeStaves.count(s) && callbacks.staffIsEligible(s))
        ++nEligibleStaves;
}
```

**Horizontal density** — mean gap between consecutive note-change ticks:
```cpp
double meanTickSpacing = (candidateTicks.size() > 1)
    ? double(endTick.ticks() - startTick.ticks())
      / double(candidateTicks.size() - 1)
    : double(endTick.ticks() - startTick.ticks());
```

**Vertical density** — mean active staves across candidate ticks. Iterate
through `candidateTicks` and call `countParticipatingStaves()` (already in
anonymous namespace) for each; average the results:
```cpp
double meanActiveStaves = 0.0;
if (!candidateTicks.empty()) {
    for (const auto& tick : candidateTicks) {
        // use next tick as endTick for the region, or tick+1 as a proxy
        meanActiveStaves += countParticipatingStaves(score, tick, /*nextTick*/,
                                                     excludeStaves);
    }
    meanActiveStaves /= double(candidateTicks.size());
}
```
Adjust the `countParticipatingStaves` call to match its actual signature in the
anonymous namespace — read it first.

---

## Step 4 — Compute adaptive thresholds

From the measurements, compute effective thresholds. The reference texture is
SATB: `nEligibleStaves ≈ 4`, `meanActiveStaves ≈ 3.5`,
`meanTickSpacing ≈ 1×DIVISION`. For SATB input, effective thresholds must
reproduce the current constants so BIR is unchanged.

**Staff count threshold** (replaces hardcoded ≥3):
```cpp
const int effectiveStaveThreshold
    = std::max(1, static_cast<int>(std::round(nEligibleStaves * 0.75)));
// SATB (4 eligible):  round(3.0) = 3  ← matches current hardcoded value
// Trio (3 eligible):  round(2.25) = 2
// Piano/duo (2):      round(1.5)  = 2
```

**Score threshold** — scales with vertical density. Derive the exact multiplier
from the Step 2 investigation. The formula shape should be:
```cpp
// verticalFactor in (0, 1]: 1.0 for full SATB density, lower for sparse
const double kRefActiveStaves = 3.5;
const double verticalFactor
    = std::min(1.0, meanActiveStaves / kRefActiveStaves);
const double effectiveAnchorMinScore
    = kAnchorMinScore * (A + (1.0 - A) * verticalFactor);
// where A is derived from Step 2 so that a 1-voice region with a clear
// chord identity still makes Round 1. A = 0.5 is a starting point:
// 1 voice → 0.75, 2 voices → ~1.0, 3.5 voices → 1.5 (unchanged)
```
Adjust `A` based on the Step 2 data. If the score scaling from Step 2 is
flat (scores don't vary much with voice count), keep A close to 1.0 (minimal
relaxation). Document the derivation in a comment.

**Duration threshold** — scales with horizontal density:
```cpp
const double kRefTickSpacing
    = static_cast<double>(mu::engraving::Constants::DIVISION);
const double horizontalFactor
    = std::min(1.0, kRefTickSpacing / meanTickSpacing);
// Sparse horizontal (large spacing) → horizontalFactor small → shorter
// minimum duration required
const int effectiveAnchorMinDurationTicks
    = std::max(mu::engraving::Constants::DIVISION / 4,
               static_cast<int>(kAnchorMinDurationTicks * horizontalFactor));
```

**Round 2 score threshold** — apply the same verticalFactor as anchor score:
```cpp
const double effectiveRound2MinScore
    = kRound2MinScore * (A + (1.0 - A) * verticalFactor);
```

Replace all hardcoded threshold comparisons with these effective values.
Add a brief comment block above the pre-measurement pass explaining the
two density dimensions and referencing Iter 69.

---

## Step 5 — Build and run tests (Part A)

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Required: 407/407 composing, 53/53 notation.

At this stage the bridge is still on Jaccard — notation tests should pass
regardless. Any failure here means the adaptive thresholds introduced a
regression in the batch path. Stop and report if so.

Also confirm binary timestamps:
```bash
stat /sessions/busy-gracious-wozniak/mnt/MS/ninja_build_rel/composing_tests.exe
stat /sessions/busy-gracious-wozniak/mnt/MS/ninja_build_rel/batch_analyze.exe
```

---

## Step 6 — BIR validation (Part A)

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

**Hard stops — revert harmonicsegmenter.cpp and report if:**
- BIR=true ≠ 5 (adaptive thresholds changed SATB anchor placement)
- BIR=false ≠ 125 (same)

If Baroque holds, run Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz hard stop: BIR=false > 75 (current 12).

Restore Baroque corpus after Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
```

---

## Step 7 — Update STATUS.md and commit Part A

Update `C:\s\MS\STATUS.md`:
- Set HEAD commit to the new hash after commit
- Confirm BIR baselines unchanged (BIR=true=5, BIR=false=125, Jazz=N)
- Set active iteration to "Iter 69 Part A complete / Part B in progress"
- Note Jazz BIR=false result

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add src/composing/analysis/harmony/harmonicsegmenter.h
git add C:\s\MS\STATUS.md
git commit -m "Composing: texture-adaptive thresholds in greedy-expand (Iter 69 Part A)

Replace hardcoded SATB-calibrated constants in greedyExpandSegmentation()
with thresholds computed from per-score texture density:

  Vertical density:   meanActiveStaves (avg concurrent eligible staves)
  Horizontal density: meanTickSpacing (avg gap between note-change ticks)

Staff count gate: max(1, round(nEligibleStaves x 0.75))
  SATB-4 -> 3 (unchanged), trio-3 -> 2, piano-2 -> 2

Score/duration thresholds scale with vertical/horizontal factor respectively.
SATB self-calibrates to previous constants; sparse textures relax proportionally.

BIR=true=5, BIR=false=125 unchanged (Baroque).
Jazz BIR=false=N."

git push
```

---

## Step 8 — Part B: Re-attempt bridge switch

Re-apply the Iter 68 bridge change exactly as before: replace
`detectHarmonicBoundariesJaccard()` in
`src/notation/internal/notationcomposingbridgehelpers.cpp` with
`greedyExpandSegmentation()` + `placedRegionsToTicks()` + the
`HarmonicSegmenterCallbacks` lambda pair.

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
All pipeline snapshots must pass after golden refresh. Then commit:
```bash
Update `C:\s\MS\STATUS.md`: set HEAD commit, mark §2.10 resolved, set active
iteration to "Iter 69 complete".

git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/
git add C:\s\MS\STATUS.md
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Replace detectHarmonicBoundariesJaccard() with greedyExpandSegmentation()
in notationcomposingbridgehelpers.cpp. Texture-adaptive thresholds (Iter 69
Part A) allow greedy-expand to handle sparse polyphonic textures correctly.

Bridge and batch paths now use the same segmentation algorithm (§2.10).
Pipeline snapshot goldens refreshed."

git push
```

**If any of the original 9 tests still fail:** report each with actual vs
expected, same format as the Iter 68 failure report. Do not update assertions.
Do not commit the bridge change. Revert the bridge file.

---

## Step 9 — Report to Cowork

```
Part A — Adaptive thresholds:
  Step 2 investigation — typical anchor confidence by voice count:
    1 voice:  ~N
    2 voices: ~N
    3 voices: ~N
    4 voices: ~N
  Threshold formula derived (A constant used): N
  Effective thresholds on Baroque corpus (SATB):
    effectiveStaveThreshold: N
    effectiveAnchorMinScore: N
    effectiveAnchorMinDurationTicks: N
    effectiveRound2MinScore: N
  BIR=true: 5 → N (must be 5)
  BIR=false: 125 → N (must be 125)
  Jazz BIR=false: 12 → N
  Committed: hash

Part B — Bridge switch:
  notation_tests: N/53
  Failing tests (if any): [list with actual vs expected]
  Pipeline snapshot goldens refreshed: [yes / no]
  Committed: [hash / not committed — reason]

§2.10 status: [resolved / still blocked — reason]
```
