# Iteration 71: Fix greedy-expand Pattern 2 (smearing) and tuplet alignment

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration

Baselines (verify against STATUS.md): BIR=true=5, BIR=false=125. Jazz BIR=false=12.
(Iter 70 committed 09f151e815 — sparse-texture fixes; 7 bridge notation failures remain.)

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Iter 70 reduced bridge notation failures from 10 → 7. Three distinct root causes
remain. This iteration addresses two of them; one is left for investigation first.

**Fix A — Pattern 2 (smearing): true-local chord for distinctness check.**
The Iter 70 guard (`local rootPc ≠ both anchor rootPcs → keep local chord`) did
not fire because the candidate's rootPc was set using bilateral context before the
guard runs — it had already been pulled toward the anchor's chord. The fix:
compute a *second* analyzeChord call on the candidate's tones with no bilateral
context (`ctx = nullptr` or equivalent), and use THAT result's rootPc exclusively
for the distinctness comparison. The placement-gating analyzeChord (with bilateral)
is unchanged — only the distinctness comparison uses the true-local result.

**Fix B — Tuplet alignment.**
`collectNoteChangeTicks()` produces mid-tuplet boundary ticks on the Dvorak
fixture. Greedy-expand places a boundary inside a tuplet group, populateChordTrack
then emits chord-track entries at non-beat-aligned ticks, and the implode test
finds overlapping chord/rest inconsistencies. Fix: after collecting note-change
ticks, snap any tick that falls mid-tuplet to the start of its enclosing tuplet
group.

**Investigate C — Low-confidence pocket.**
The test `HarmonicAnnotationKeepsRomanAtLowConfidenceNoteContext` expects
`keyConfidence < 0.5` for a note that greedy-expand now places in a high-
confidence region (0.671). This may resolve once Fix A changes the region
structure (different boundaries → different region the note falls in). Do not
fix this proactively — check after Fix A and Fix B whether it passes.

**Investigate D — Gsus/F7/Eb chord identity in audit test.**
Before spending time on these substitution errors, check whether they disappear
once Fix A corrects the dominant boundaries. If the smearing is fixed and the
correct boundary lands at the expected dominant beat, the tone set changes and
the chord identity may correct itself. Report whether this is still an issue
after Fix A.

---

## Step 1 — Read before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp` in full. Locate:

1. The Round 2 gap-fill distinctness check from Iter 70 — understand the exact
   point where the candidate's chord identity is set and where the distinctness
   comparison occurs.
2. `collectNoteChangeTicks()` — understand how it iterates segments and collects
   ticks; find where tuplet-internal ticks would enter the collection.
3. How `analyzeChord` is called with and without bilateral context in the
   existing code — confirm what the "no bilateral" call signature looks like.

Also read the failing test file for the Dvorak tuplet test to understand what
tick values are involved and what the expected chord-track output is.

---

## Step 2 — Fix A: true-local chord for distinctness comparison

In the Round 2 fill loop, at the point where the Iter 70 distinctness guard runs:

1. Call `analyzeChord` a second time on the candidate's already-collected tones,
   passing `nullptr` (or whatever the existing code uses) for the bilateral
   context parameter. Capture the result as `trueLocalResult`.

2. Replace the distinctness check to use `trueLocalResult.rootPitchClass` rather
   than the candidate's current rootPc (which was set with bilateral context):

```cpp
// True-local: analyzeChord with no bilateral context
const auto trueLocal = chordAnalyzer->analyzeChord(candidateTones,
                                                     prefs,
                                                     /*bilateralCtx=*/nullptr,
                                                     keyFifths, keyMode);

const bool localDiffersFromAnchors
    = (trueLocal.rootPitchClass >= 0)
   && (trueLocal.rootPitchClass != leftAnchorRootPc)
   && (trueLocal.rootPitchClass != rightAnchorRootPc);

if (localDiffersFromAnchors
    && trueLocal.score >= effectiveRound2MinScore) {
    placed.rootPitchClass = trueLocal.rootPitchClass;
    placed.bassPitchClass = trueLocal.bassPitchClass;
    placed.quality        = trueLocal.quality;
    placed.confidence     = trueLocal.score;
    placed.reason         = "round2-true-local-preferred";
}
```

Adjust variable names, types, and method signatures to match the actual
analyzeChord interface — read it before writing. Do not guess parameter order.

This second analyzeChord call only occurs during Round 2 for candidates that
pass the existing placement gate. It does not affect Round 1 or the placement
decision itself — only the chord identity assigned to a placed Round 2 region.

---

## Step 3 — Fix B: tuplet-boundary snap in collectNoteChangeTicks

After `collectNoteChangeTicks()` assembles its tick list, post-process to remove
or snap mid-tuplet ticks.

A tick is "mid-tuplet" if the Segment at that tick is inside a tuplet group and
is NOT the first segment of that tuplet group. The MuseScore engraving API for
checking this: `segment->tuplet()` (or the equivalent for the element at that
tick) returns non-null if the element belongs to a tuplet; the tuplet's
`firstElement()` or `tick()` gives the group start.

Snap rule: if a collected tick `t` is mid-tuplet, replace it with the enclosing
tuplet group's start tick. After snapping, deduplicate the list (a std::set or
post-sort unique pass).

Read an existing MuseScore engraving file that accesses tuplet information
(search for `tuplet()` calls in `src/engraving/`) to confirm the correct API
before writing. Do not guess — the Segment/ChordRest/Tuplet API has changed
across MuseScore versions.

---

## Step 4 — Build and run tests (bridge still on Jaccard)

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Confirm binary timestamps. Then:

```bash
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Required: 407/407 composing, 53/53 notation. Bridge is still Jaccard —
notation tests must pass regardless. Any failure here means Fix A or Fix B
introduced a batch-path regression. Stop and report.

---

## Step 5 — BIR validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Hard stops — revert all changes and report if:
- BIR=true ≠ 5
- BIR=false ≠ 125

Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz hard stop: BIR=false > 75. Restore Baroque corpus after.

---

## Step 6 — Update STATUS.md and commit

Update `C:\s\MS\STATUS.md`: set HEAD commit, confirm BIR unchanged,
set active iteration to "Iter 71 committed / bridge switch pending".

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add C:\s\MS\STATUS.md
git commit -m "Composing: fix Round 2 smearing and tuplet alignment (Iter 71)

Fix A — Round 2 true-local chord preference:
  Distinctness check now uses analyzeChord with no bilateral context to
  determine candidate's true local rootPc. Prevents bilateral contamination
  from anchors defeating the local-preference guard introduced in Iter 70.
  Dominant entries surrounded by tonic anchors now correctly retain their
  local chord identity.

Fix B — Tuplet boundary alignment in collectNoteChangeTicks:
  Mid-tuplet ticks snapped to enclosing tuplet group start.
  Prevents populate-chord-track from emitting entries at non-beat-aligned
  ticks that produce chord/rest overlap on tuplet-containing staves.

BIR=true=5, BIR=false=125 unchanged. Jazz BIR=false=N."

git push
```

---

## Step 7 — Re-attempt bridge switch

Re-apply the bridge change: replace `detectHarmonicBoundariesJaccard()` in
`src/notation/internal/notationcomposingbridgehelpers.cpp` with
`greedyExpandSegmentation()` + `placedRegionsToTicks()` + `HarmonicSegmenterCallbacks`.

Build, then run notation tests:
```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

For any remaining failures, report actual vs expected in the Step 9 format.
Pay attention to whether `HarmonicAnnotationKeepsRomanAtLowConfidenceNoteContext`
and the Gsus/F7/Eb audit entries now pass — these were expected to resolve as
side-effects of Fix A (Investigate C and D).

**If 53/53 pass:**
```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Update STATUS.md: mark §2.10 resolved, set active iteration to "Iter 71 complete".

```bash
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/
git add C:\s\MS\STATUS.md
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Replace detectHarmonicBoundariesJaccard() with greedyExpandSegmentation().
Sparse-texture fixes (Iters 69–71) allow greedy-expand to handle Corelli
trio, Dvorak tuplets, and small alternating-staff fixtures correctly.

Bridge and batch paths now use the same segmentation algorithm (§2.10).
Pipeline snapshot goldens refreshed.
BIR=true=5, BIR=false=125. Jazz BIR=false=N."

git push
```

**If tests still fail:** report remaining failures. Revert bridge file.

---

## Step 9 — Report to Cowork

```
Fix A (true-local distinctness):
  Corelli smearing resolved: [yes / partially / no — which tests still fail]
  Investigate C (low-confidence pocket): [resolved as side-effect / still fails]
  Investigate D (Gsus/F7/Eb): [resolved as side-effect / still fails — describe]

Fix B (tuplet alignment):
  Dvorak tuplet test resolved: [yes / no]

Tests (bridge on Jaccard):
  composing: N/407
  notation: N/53

BIR=true: 5 → N
BIR=false: 125 → N
Jazz BIR=false: 12 → N
Committed: [hash]

Bridge switch:
  notation_tests: N/53
  Remaining failures (if any): [list with actual vs expected]
  Pipeline snapshot goldens refreshed: [yes / no]
  Committed: [hash / not committed — reason]

§2.10 status: [resolved / still blocked — remaining issue]
```
