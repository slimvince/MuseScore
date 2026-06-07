# Iteration 75: Sparse anchor placement + Fix B scope + m11:960 boundary

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration

Baselines (verify against STATUS.md): BIR=true=3, BIR=false=119. Jazz BIR=false=10.
(Iter 74 committed 237f9f08b2 — template complexity + key-tonic prior. Bridge still Jaccard.)

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Context

With bridge=greedy-expand, 5 Corelli op01n08d tests still fail. Two distinct root
causes remain after Iter 74:

**Problem 1 — m1:960 G anchor not placed.**
Round 1/Round 2 fails to place a G-rooted anchor at tick 960 (m1 beat 3). Because
nothing is placed in [startTick, firstPlaced), head-gap synthesis fires and Fix B's
tonic prior (correctly implemented) overrides the whole span to Cm — including
tick 960 which should be G. The primary fix is making Round 1/Round 2 place the G
anchor. Fix B is a safety net for a genuine short pickup, not a substitute for
missing anchor placement.

**Problem 2 — Fix B scope too broad.**
When the head-gap span is multi-chord (several beats or more), applying the tonic
prior to the entire span is wrong. The tonic prior should only fire when the span
is short enough to plausibly be a pickup bar or anacrusis — not when it contains
multiple distinct harmonies.

**Problem 3 — m11:960 boundary (greedy-expand only).**
Fix A (template complexity) resolves Gmadd9→Gm with bridge=Jaccard because Jaccard's
boundaries happen to isolate m11:960 cleanly. With greedy-expand, the analyzed
region pulls in extra tones that activate add9, defeating Fix A. The region boundary
does not land where it should.

---

## Step 1 — Read before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp` in full. Locate:
1. The Round 1 anchor promotion block — every condition that must be true for a
   candidate to be promoted to anchor.
2. The Round 2 gap-fill block — every condition that must be true for a candidate
   to be placed as a Round 2 region.
3. The head-gap synthesis block (Fix B from Iter 73/74) — where it fires and what
   the span check currently looks like.
4. `collectNoteChangeTicks()` — confirm whether tick 960 would be collected given
   the Corelli op01n08d note content at m1 beat 3.

---

## Step 2 — Diagnostic: why is m1:960 G rejected?

With the bridge temporarily switched to greedy-expand (do NOT commit this), add
`fprintf(stderr, ...)` diagnostics to `greedyExpandSegmentation()` that fire when
the score path contains "corelli" (case-insensitive) and print for every candidate
evaluated at or near tick 960:

```
DIAG-CAND tick=%d pcCount=%d winnerScore=%.4f threshold=%.4f round=R%d passed=%d reason=%s
```

Also print when head-gap synthesis fires:
```
DIAG-HEAD startTick=%d headEnd=%d spanTicks=%d winnerRoot=%d tonicPriorFired=%d
```

Build batch_analyze only. Run on the Corelli fixture:
```bash
cd C:\s\MS\ninja_build_rel && ./batch_analyze \
    ../src/notation/tests/data/corelli_op01n08d.mscx 2>&1 | grep DIAG
```

From the output, answer:
1. Is tick 960 present in the candidate set? If not — why not (onset missing,
   filtered by staff eligibility, or something else)?
2. If present — what is winnerScore, what is the effective threshold, and which
   gate rejects it (score < threshold, duration < floor, pcCount < minimum,
   activeStaves < required)?
3. What is the head-gap span (startTick to headEnd)? How many ticks wide?
4. Does Fix B's tonic prior fire, and over what span?

Report findings before making any code changes.

---

## Step 3 — Fix A: make Round 1/Round 2 place G at m1:960

From Step 2 diagnostic, identify the specific gate rejecting tick 960. Apply the
minimal targeted fix to allow the G-dominant anchor to be placed.

**Do not widen thresholds globally.** The fix must be targeted to the specific
rejection reason identified in Step 2. Examples:

- If pcCount is 1 (G unison) and the PC-count adaptive threshold still rejects it:
  verify that `kPCFloorFraction` from Iter 72 is correctly applied at this site.
  If there is a second threshold comparison site that was missed in Iter 72, apply
  the same PC-count adaptation there.

- If duration < floor: the G sonority at m1:960 may be shorter than
  `effectiveDurationFloor`. Verify that the duration floor is not blocking a
  musically valid beat-level entry. If the floor is too conservative for sparse
  counterpoint, add a secondary path: if pcCount <= 2 AND the candidate is the
  ONLY candidate in its vicinity (no competing candidates within N ticks), relax
  the duration floor by a factor of 0.5.

- If activeStaves < required: the staff threshold may be too high for a sparse
  texture moment. Verify that the effective staff threshold for this score is
  correct given the eligible staff count.

Whatever gate is responsible — fix it, document the reason in a code comment, and
verify the fix places G at tick 960 by re-running the diagnostic.

---

## Step 4 — Fix B: scope the tonic prior to short head-gap spans

In `greedyExpandSegmentation()`, at the head-gap synthesis block, add a span-length
guard before applying the tonic prior:

```cpp
// Tonic prior is only valid for a short pickup/anacrusis span.
// A long head-gap contains multiple distinct harmonies — applying
// the tonic to the whole span is musically wrong.
static constexpr int kHeadGapTonicPriorMaxTicks =
    2 * mu::engraving::Constants::DIVISION;  // 2 beats — adjust if needed

const int headSpanTicks = headEnd - startTick.ticks();
const bool spanIsShortEnoughForTonicPrior
    = (headSpanTicks <= kHeadGapTonicPriorMaxTicks);

if (!resultIsTonic
    && headMargin < kHeadGapTonicPreferenceMargin
    && spanIsShortEnoughForTonicPrior) {
    // Apply tonic prior only for short pickups.
    headRegion.rootPitchClass = tonicPC;
    headRegion.reason = "head-gap-tonic-prior";
}
```

Adjust `kHeadGapTonicPriorMaxTicks` based on the actual Corelli head-gap span
measured in Step 2. The threshold should be comfortably below the span length
that was causing the incorrect Cm override, and comfortably above a genuine
one-beat pickup.

---

## Step 5 — Investigate m11:960 boundary (greedy-expand)

With bridge=greedy-expand and diagnostics still active, examine what region
covers tick 960 in measure 11:

```
DIAG-REGION startTick=%d endTick=%d rootPc=%d quality=%s pcCount=%d tones=[list]
```

Print this for every placed region that covers or borders tick 960 in m11.

Determine:
- What tones are accumulated in the region covering m11:960?
- Which tone(s) trigger the add9 detection (the 9th above root)?
- Does the extra tone come from a note that starts before m11:960 and sustains
  through it, or from a note that starts after m11:960 in the same region?
- Is there a note-change tick at the correct boundary that would isolate m11:960
  if it were recognized?

If the extra tone comes from a sustained note that should have ended before
m11:960 (a tie chain with a release at m11:960), confirm whether the note-end
tick for that release was collected by Iter 73's note-end pass.

Report findings. If a targeted fix is clear (e.g., a specific note-end tick is
missing), implement it. If the root cause requires more investigation, report
that and defer to Iter 76.

---

## Step 6 — Remove diagnostics, build and run tests (bridge on Jaccard)

Remove all `fprintf` diagnostics. Revert bridge to Jaccard.

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Required: 407/407 composing, 53/53 notation. Any failure is a regression.

---

## Step 7 — BIR validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Hard stops — revert and report if:
- BIR=true increases above 3
- BIR=false increases above 119

Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz hard stop: BIR=false > 75 (current 10). Restore Baroque corpus after.

---

## Step 8 — Update STATUS.md and commit

Update `C:\s\MS\STATUS.md`: new HEAD commit, BIR baselines, active iteration.

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add src/composing/analysis/chord/chordanalyzer.cpp
git add C:\s\MS\STATUS.md
git commit -m "Composing: sparse anchor placement + Fix B scope + boundary fix (Iter 75)

Fix A — Sparse dominant anchor placement:
  [describe the specific gate that was blocking tick 960 and the fix]

Fix B — Head-gap tonic prior scoped to short spans:
  Tonic prior now only fires when head-gap span <= kHeadGapTonicPriorMaxTicks.
  Prevents incorrect tonic override of multi-chord head gaps.

Fix C — m11:960 boundary (if resolved):
  [describe or omit if deferred]

BIR=true: 3 → N. BIR=false: 119 → N. Jazz BIR=false: 10 → N."

git push
```

---

## Step 9 — Re-attempt bridge switch

Re-apply the bridge change. Build and run notation tests:

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

For each remaining failure, report: test name, tick, expected, actual.

**If 53/53 pass:**
```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Update STATUS.md: §2.10 resolved, "Iter 75 complete".

```bash
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/
git add C:\s\MS\STATUS.md
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Iters 69–75: greedy-expand made texture-general for bridge path.
§2.10 compliance achieved.
BIR=true=N, BIR=false=N. Jazz BIR=false=N."

git push
```

**If tests still fail:** report remaining failures with actual vs expected and
musical assessment (genuine algorithmic gap vs Jaccard-specific assertion).

---

## Step 10 — Report to Cowork

```
Step 2 diagnostic findings:
  Tick 960 in candidate set: [yes / no — reason]
  If present: winnerScore=N threshold=N rejecting gate=[name]
  If absent: reason=[onset missing / staff filter / other]
  Head-gap span: startTick=N headEnd=N spanTicks=N
  Tonic prior fired over span: [yes / no]

Fix A (sparse anchor placement):
  Gate fixed: [name and description]
  G now placed at tick 960: [yes / no]

Fix B (tonic prior scope):
  kHeadGapTonicPriorMaxTicks: N
  Prior now correctly scoped: [yes / no]

Fix C (m11:960 boundary):
  Extra tone source: [sustained note / post-960 onset / other]
  Note-end tick present: [yes / no]
  Fixed: [yes / deferred to Iter 76 — reason]

Tests (bridge on Jaccard):
  composing: N/407
  notation: N/53

BIR=true: 3 → N
BIR=false: 119 → N
Jazz BIR=false: 10 → N

Committed: [hash]

Bridge switch:
  notation_tests: N/53
  Remaining failures: [list with actual vs expected + musical assessment]
  Committed: [hash / not committed]

§2.10 status: [resolved / still blocked — remaining issue]
```
