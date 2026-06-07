# Iteration 77: Fast secondary-function chords + opening region accuracy

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration

Baselines (verify against STATUS.md): BIR=true=3, BIR=false=119. Jazz BIR=false=10.
(Iter 76 committed 528f9e7f24 — diatonic quality resolution + Dvorak re-anchor.
Bridge still Jaccard. §2.10 still blocked.)

Also read `C:\s\MS\docs\quality_observations_iter76.md` — this records the full
user-reviewed quality findings from four pipeline snapshot scores. The two BLOCKING
issues for the bridge switch are §3.1 and §4.1 of that document. This iteration
addresses both.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Context — two blocking snapshot failures

**Blocking issue 1 (§3.1) — Schumann kinderszenen_n01:**
Greedy-expand misses the C#°7 chord (vii°7/V) at beat 2 of each measure. The
chord lasts approximately one beat in 2/4 time with triplet figures. Jaccard
catches it (but misidentifies it as Gm/C#); greedy-expand skips the beat entirely
and jumps to D (V) at the next downbeat.

Root cause hypothesis: the C#°7 region falls below greedy-expand's duration floor
or score threshold. The chord is sparse (2–3 PCs, diminished quality, short
duration) and surrounded by strong G-major anchors, so bilateral context may be
pulling its score below threshold, or the duration floor may be rejecting it.

**Blocking issue 2 (§4.1) — bach_chorale_137 (BWV 301):**
Greedy-expand produces BbMaj7/D at tick 0 (opening chord) where the correct
reading is Dm (D minor, root position). Jaccard produces Dm/C — correct root,
wrong bass.

Root cause hypothesis: the opening region accumulates extra tones across too wide
a span. The first few ticks of the chorale may include a C in the bass (passing
note or suspension) and Bb in an inner voice, which when combined with D and F
read as BbMaj7/D. Greedy-expand's head-gap synthesis or the initial anchor
placement may be pulling in tones from beyond the first harmonic change.

---

## Step 1 — Read before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp` in full. Locate:

1. The duration floor computation — what is `effectiveDurationFloor` for the
   Schumann fixture (2/4 time, triplet figures, sparse texture)?
2. The Round 2 bilateral context scoring — does it reduce a diminished-quality
   candidate's score when both neighbours are tonic-quality anchors?
3. The head-gap synthesis block and the initial tick-0 region placement — how
   are tones accumulated for the first candidate region?
4. `collectNoteChangeTicks()` — would it collect a tick at the start of the C#°7
   in the Schumann score? Would it collect note-end ticks that bound the C#°7?

---

## Step 2 — Diagnostic: Schumann beat-2 chord rejection

With bridge temporarily switched to greedy-expand, add diagnostics to
`greedyExpandSegmentation()` that fire when the score path contains "schumann"
(case-insensitive). Print for every candidate tick in the first two measures:

```
DIAG-SCHUMANN tick=%d pcCount=%d winnerScore=%.4f threshold=%.4f
  duration=%d durationFloor=%d activeStaves=%d stavesThreshold=%d
  round=R%d passed=%d reason=%s
```

Also print the collected tick set:
```
DIAG-TICKS [list of all collected ticks in first 2000 ticks]
```

Build batch_analyze only. Run on the Schumann fixture (find it with:
`grep -r "schumann_kinderszenen" src/notation/tests --include="*.cpp" -l`).

From the output, answer:
1. Is there a candidate tick at the start of the C#°7 chord? If yes — which
   gate rejects it (score, duration, staves)?
2. If no candidate tick — is the C#°7 onset missing from collectNoteChangeTicks,
   or is it present but failing as a candidate?
3. What is `effectiveDurationFloor` for this score?
4. Would adding note-end ticks for the preceding G-major notes introduce the
   C#°7 onset as a boundary?

---

## Step 3 — Diagnostic: bach_chorale_137 opening region

With bridge still on greedy-expand and diagnostics active, add a second diagnostic
block that fires when the score path contains "137" and prints for every candidate
in [0, 1920) (first 4 beats):

```
DIAG-137 tick=%d pcCount=%d pcs=[list] winnerRoot=%d winnerQuality=%s
  winnerScore=%.4f threshold=%.4f passed=%d reason=%s
```

Also print the full tone set accumulated for the head-gap region if it fires:
```
DIAG-137-HEAD startTick=%d headEnd=%d toneCount=%d pcs=[list]
  winnerRoot=%d winnerQuality=%s
```

From the output, answer:
1. What tones are accumulated in the region covering tick 0?
2. Is Bb present in the accumulation? If so — which voice and which tick does
   it come from?
3. Does head-gap synthesis fire, or does a Round 2 region cover tick 0?
4. What is the score for Dm vs BbMaj7 at tick 0, and why does BbMaj7 win?

---

## Step 4 — Fix A: fast secondary-function chord placement (Schumann)

From Step 2 findings, apply the minimal targeted fix.

**If the C#°7 onset tick is missing from collectNoteChangeTicks:**
The G-major notes preceding the C#°7 end at the same tick the C#°7 begins.
Iter 73's note-end tick collection should have added this tick. Verify whether:
- The G-major notes have `tieForward()` set (which would suppress their note-end
  tick). If so, this is a tie-chain edge case — the note ends but ties forward
  into the next G-major group, suppressing the release tick incorrectly.
- Add a diagnostic to the note-end pass to confirm which ticks it produces for
  the Schumann fixture.

**If the tick IS present but rejected by duration floor:**
The C#°7 chord lasts approximately one beat in 2/4. The duration floor may be
calibrated for denser textures. Apply the following relaxation for sparse
secondary-function chords: if the candidate has `pcCount <= 2`, is the ONLY
candidate between two placed anchors, and its duration >= `DIVISION/4` (one
sixteenth note), halve the effective duration floor for this candidate only.

**If rejected by score threshold:**
Apply the same PC-count adaptive threshold already present from Iter 72, and
verify it is being applied at this site. If bilateral context is pulling the
score below threshold, check whether the bilateral weight is too strong for
a chord that is harmonically distinct from both neighbours (tonic left, dominant
right; diminished candidate in between is maximally distinct and should not be
penalised by bilateral pull).

Document the specific fix with a code comment referencing this iteration.

---

## Step 5 — Fix B: opening region accuracy (bach_chorale_137)

From Step 3 findings, apply the minimal targeted fix.

**If Bb enters the tone accumulation from a passing/inner voice at tick 0:**
The opening D-minor chord likely has D–F–A in the main voices but Bb appears
briefly in an inner voice (perhaps the alto or tenor). If the Bb is from a very
short note (< DIVISION/4), add a minimum-duration gate to the tone accumulation
in `collectRegionTones`: tones from notes shorter than `minToneDuration` are
excluded from chord analysis. Read `HarmonicSegmenterCallbacks.collectRegionTones`
and the lambda that implements it — this is where the duration gate should be
added.

**If head-gap synthesis fires and accumulates too wide a span:**
The head-gap span may extend from tick 0 to the first placed anchor, picking up
tones from multiple harmonies. If the span is multi-beat and includes tones from
later beats (including Bb from a later position), the Fix B scope guard from
Iter 74 should prevent the tonic prior but the tone accumulation is still too wide.
Consider: for head-gap synthesis, limit tone accumulation to [startTick,
startTick + DIVISION) — the first beat only — rather than the full [startTick,
firstPlaced) span.

**If a Round 2 region covers tick 0 and accumulates Bb:**
The Round 2 region's tone window may extend rightward into beats containing Bb.
Check whether the region end tick is correctly bounded by the next candidate tick.

---

## Step 6 — Remove diagnostics. Build and run tests (bridge on Jaccard).

Remove all `fprintf` diagnostics. Revert bridge to Jaccard.

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Required: 407/407 composing. Notation: no regressions below 51/53. Pipeline
snapshot: no regressions below 4/11 (current pre-existing failures).

---

## Step 7 — BIR validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Hard stops:
- BIR=true > 3
- BIR=false > 119

Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz hard stop: BIR=false > 75 (current 10). Restore Baroque corpus after.

---

## Step 8 — Update STATUS.md and commit

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add src/notation/internal/notationharmonicrhythmbridge.cpp
git add C:\s\MS\STATUS.md
git commit -m "Composing: fast secondary-function chord placement + opening region fix (Iter 77)

Fix A — Fast secondary-function chord placement:
  [describe the specific gate/mechanism fixed for Schumann vii°7/V]

Fix B — Opening region tone accumulation:
  [describe the specific fix for bach_chorale_137 opening Bb contamination]

BIR=true: 3 → N. BIR=false: 119 → N. Jazz BIR=false: 10 → N."

git push
```

---

## Step 9 — Re-attempt bridge switch

Re-apply bridge switch. Build. Run all three test suites:

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

**Target:** pipeline_snapshot 9/11 or better (the 2 previously-blocked scores
— Schumann and bach_chorale_137 — now passing; bach_chorale_001 and
bach_chorale_003 golden updates from Iter 76 applied).

Wait — the Iter 76 golden updates for bach_chorale_001 and bach_chorale_003
were NOT committed (Step 9 of Iter 76 was gated on full confirmation). Apply
them now:

```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens \
    --gtest_filter="*bach_chorale_001*:*bach_chorale_003*"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

If Schumann and bach_chorale_137 now pass AND bach_chorale_001/003 goldens are
updated, run full golden refresh and commit bridge switch:

```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Confirm 11/11 pass. Then:

```bash
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/pipeline_snapshot_tests/snapshots/
git add C:\s\MS\STATUS.md
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Iters 69–77: greedy-expand made texture-general for bridge path.
§2.10 compliance achieved — bridge and batch paths use the same
segmentation algorithm.
Pipeline snapshot goldens refreshed (4 scores).
BIR=true=N, BIR=false=N. Jazz BIR=false=N."

git push
```

Update STATUS.md: §2.10 resolved, "Iter 77 complete".

**If tests still fail:** report remaining failures with actual vs expected,
musical assessment, and whether each represents a genuine regression or
a pre-existing quality issue (see quality_observations_iter76.md for
the full catalogue).

---

## Step 10 — Report to Cowork

```
Step 2 — Schumann diagnostic findings:
  C#°7 onset tick in candidate set: [yes / no — reason]
  Rejecting gate: [duration / score / staves / absent from tick set]
  effectiveDurationFloor for this score: N ticks
  Fix applied: [describe]

Step 3 — bach_chorale_137 diagnostic findings:
  Bb in tick-0 accumulation: [yes — from voice X tick Y / no]
  Head-gap fires: [yes / no]
  Dm score at tick 0: N   BbMaj7 score: N
  Fix applied: [describe]

Tests (bridge on Jaccard after fixes):
  composing: N/407
  notation: N/53
  pipeline_snapshot: N/11

BIR=true: 3 → N
BIR=false: 119 → N
Jazz BIR=false: 10 → N

Committed: [hash]

Bridge switch:
  notation_tests: N/53
  pipeline_snapshot: N/11
  Committed: [hash / not committed — remaining failures listed]

§2.10 status: [resolved / still blocked — issue]
```
