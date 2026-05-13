# Iteration 76: Pipeline snapshot diff review + Power chord quality resolution + Dvorak re-anchor

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration

Baselines (verify against STATUS.md): BIR=true=3, BIR=false=119. Jazz BIR=false=10.
(Iter 75 committed 540aa0bb35 — bridge sparsePrefs fix. Bridge still Jaccard.)

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Context

With bridge=greedy-expand, notation tests are 50/53 — identical failure set to
bridge=Jaccard. No new notation failures from the segmentation switch. The
remaining blockers for committing the bridge switch are:

1. **Pipeline snapshot diffs** — 4 scores produce different output under
   greedy-expand vs Jaccard. The diffs need human review before goldens are
   updated. The scores are:
   - `tools/dcml/bach_chorales/MS3/001 Aus meines Herzens Grunde.mscx`
   - `tools/dcml/bach_chorales/MS3/003 Ach Gott, vom Himmel sieh darein.mscx`
   - `tools/dcml/bach_chorales/MS3/137 Du, o schönes Weltgebäude.mscx`
   - `tools/dcml/schumann_kinderszenen/MS3/n01.mscx`

2. **3 pre-existing notation failures** (fail on both Jaccard and greedy-expand):
   - `CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord` — expects
     `G` at sparse beats, gets `G5` (Power chord). Key-aware quality resolution
     needed for non-tonic sparse roots.
   - `CorelliOp01n08dUserReportedChordTrackAudit` — expects `Cm`/`Fm`, gets
     `C5`/`F5`/`Gsus`. Same root cause.
   - `HarmonicAnnotationKeepsRomanAtLowConfidenceNoteContext` — Dvorak op08n06
     keyConfidence=0.92 where test expects <0.5. Flagged for re-anchor since
     Iter 72; greedy-expand correctly places the note in a high-confidence region.

---

## Step 1 — Read before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp` and
`src/notation/internal/notationharmonicrhythmbridge.cpp` in full. Locate:

1. The `applyTonicPriorToSparseChord` helper added in Iter 75 — understand
   exactly which chord qualities it promotes and under what conditions.
2. Where in the bridge the sparse chord quality is assigned after
   `analyzeChord` returns — this is where the key-aware quality resolver
   (Step 3) will be inserted.
3. The Dvorak test in `src/notation/tests/notationimplode_tests.cpp` —
   read the full test and understand what it currently asserts.

---

## Step 2 — Pipeline snapshot diffs (human review required)

Switch bridge to greedy-expand. Build. Run pipeline snapshot tests and capture
the full diff for each of the 4 failing scores:

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe 2>&1 | grep -A 200 "bach_chorale_001\|bach_chorale_003\|bach_chorale_137\|schumann_kinderszenen"
```

For each of the 4 failing scores, print a structured diff showing ONLY the
regions that differ between the golden (Jaccard) and the actual (greedy-expand)
output. Format:

```
=== bach_chorale_001 ===
tick=N  golden: root=X quality=Y  actual: root=X quality=Z
tick=N  golden: [absent]          actual: root=X quality=Y
tick=N  golden: root=X quality=Y  actual: [absent]
...

=== bach_chorale_003 ===
...
```

**Do not update goldens yet.** Report the diffs to Cowork (Step 8) and wait
for confirmation before touching any golden file. The user will assess whether
each change is musically correct, equivalent, or a regression.

---

## Step 3 — Fix: key-aware quality resolution for sparse non-tonic chords

The `applyTonicPriorToSparseChord` helper (Iter 75) promotes Power/Sus chords
whose root matches the key tonic. Extend this to cover all diatonic scale
degrees: when a sparse region produces a Power or Suspended chord quality, and
the key context is available, assign the diatonic quality for that root PC
in the current key.

**Diatonic quality table (major key, root PC relative to tonic):**

| Scale degree | Quality   |
|-------------|-----------|
| I (0)       | major     |
| II (2)      | minor     |
| III (4)     | minor     |
| IV (5)      | major     |
| V (7)       | major     |
| VI (9)      | minor     |
| VII (11)    | diminished|

**Minor key** (natural minor, root PC relative to tonic):

| Scale degree | Quality   |
|-------------|-----------|
| I (0)       | minor     |
| II (2)      | diminished|
| III (3)     | major     |
| IV (5)      | minor     |
| V (7)       | minor     |
| VI (8)      | major     |
| VII (10)    | major     |

Apply this resolution only when:
- The chord quality from `analyzeChord` is `power` or `sus4` or `sus2`
- `regionPCCount <= 2` (thin evidence — sparse region)
- The root PC maps to a diatonic scale degree in the current key
- No chromatic alteration is suggested by the tones (i.e., the tones present
  are consistent with the diatonic quality)

Read `src/composing/analysis/key/keymodeanalyzer.cpp` (or equivalent) to find
the existing tonic-PC and key-mode resolution before implementing — do not
duplicate logic already present.

**Do not apply this resolution to dense regions (3+ PCs).** Dense regions have
enough evidence to determine quality directly; overriding with the diatonic
assumption would suppress legitimate chord color (e.g. a genuine sus4 chord
in a dense texture).

---

## Step 4 — Fix: re-anchor Dvorak low-confidence test

In `src/notation/tests/notationimplode_tests.cpp`, the test
`HarmonicAnnotationKeepsRomanAtLowConfidenceNoteContext` was written against
Jaccard's fragmentation behavior. Greedy-expand correctly places the note in a
high-confidence region (keyConfidence=0.92).

Re-anchor the test to the genuinely ambiguous region at m4 b2 of Dvorak op08n06
(Bbsus/G vs F/G competing readings, chordScoreMargin ≈ 0.14). The new assertion
should verify that a note in that region has chord-level ambiguity (margin < 0.2)
rather than asserting a specific confidence value below 0.5.

Read the test carefully before modifying. Measure the actual greedy-expand output
at m4 b2 before writing the new assertion — do not guess the values.

```bash
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe --gtest_filter="*LowConfidence*"
```

---

## Step 5 — Build and run tests (bridge on Jaccard)

Remove bridge switch. Revert to Jaccard.

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Required: 407/407 composing. Notation: at minimum no new failures vs the
pre-existing 50/53 baseline. The two Corelli failures (Step 3) should now
pass — target 52/53 or 53/53.

---

## Step 6 — BIR validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Hard stops — revert Step 3 changes and report if:
- BIR=true increases above 3
- BIR=false increases above 119

The diatonic quality resolver applies only to sparse (≤2 PC) regions. Bach
chorales are dense SATB — it should not fire. Verify this is the case.

Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz hard stop: BIR=false > 75 (current 10). Restore Baroque corpus after.

---

## Step 7 — Commit Jaccard-path fixes

```bash
git add src/notation/internal/notationharmonicrhythmbridge.cpp
git add src/notation/tests/notationimplode_tests.cpp
git add C:\s\MS\STATUS.md
git commit -m "Composing: diatonic quality resolution for sparse chords + Dvorak re-anchor (Iter 76)

Fix A — Diatonic quality resolution for sparse non-tonic chords:
  When analyzeChord returns Power/Sus quality on a ≤2-PC region, and the
  root PC maps to a diatonic scale degree in the current key, assign the
  diatonic quality (major/minor/diminished). Dense regions (3+ PCs) are
  unaffected. Resolves G5→G, C5→Cm, F5→Fm in sparse Corelli passages.

Fix B — Dvorak low-confidence test re-anchored:
  Previous anchor (low-confidence pocket) was a Jaccard fragmentation
  artifact. Re-anchored to m4 b2 (Bbsus/G vs F/G, margin ~0.14) —
  a genuinely ambiguous chord reading. Test now validates chord-level
  ambiguity rather than Jaccard-specific segmentation.

BIR=true: 3 → N. BIR=false: 119 → N. Jazz BIR=false: 10 → N."

git push
```

---

## Step 8 — Report snapshot diffs to Cowork and await review

**Stop here.** Present the structured diff output from Step 2 to Cowork.
For each changed tick across the 4 scores, state:
- What Jaccard produced (golden)
- What greedy-expand produces (actual)
- Your musical assessment: is the greedy-expand reading more correct,
  equivalent, or potentially wrong?

Do not update any golden files until the user confirms each diff is acceptable.

---

## Step 9 — (After user confirmation) Update goldens and commit bridge switch

After the user confirms the snapshot diffs are acceptable:

```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Confirm all 11/11 pass. Then commit the bridge switch:

```bash
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/pipeline_snapshot_tests/snapshots/
git add C:\s\MS\STATUS.md
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Iters 69–76: greedy-expand made texture-general for bridge path.
§2.10 compliance achieved — bridge and batch paths use the same
segmentation algorithm.
Pipeline snapshot goldens refreshed (4 scores: bach_chorale_001/003/137,
schumann_kinderszenen_n01).
BIR=true=N, BIR=false=N. Jazz BIR=false=N."

git push
```

Update STATUS.md: §2.10 resolved, "Iter 76 complete".

---

## Step 10 — Report to Cowork

```
Step 2 — Pipeline snapshot diffs:
  bach_chorale_001: [structured diff — tick, golden, actual, assessment]
  bach_chorale_003: [structured diff]
  bach_chorale_137: [structured diff]
  schumann_kinderszenen_n01: [structured diff]

Fix A (diatonic quality resolution):
  G5 → G resolved: [yes / no]
  C5 → Cm resolved: [yes / no]
  F5 → Fm resolved: [yes / no]
  BIR effect: BIR=true 3→N, BIR=false 119→N

Fix B (Dvorak re-anchor):
  New assertion: [describe — tick, measure, what is asserted]
  Test passes: [yes / no]

Tests (bridge on Jaccard):
  composing: N/407
  notation: N/53

Committed: [hash]

[AWAITING USER CONFIRMATION OF SNAPSHOT DIFFS BEFORE STEP 9]

Bridge switch (after confirmation):
  pipeline_snapshot: N/11
  Committed: [hash / not committed — reason]

§2.10 status: [resolved / still blocked — reason]
```
