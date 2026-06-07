# Iteration 73: Note-end tick collection + head-gap synthesis

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

**You are starting a new session with no memory of previous work.**
Read these files before doing anything else — they are your only source of truth:
1. `C:\s\MS\CLAUDE.md` — standing rules and pre-authorized file list
2. `C:\s\MS\build_and_test.md` — authoritative build and test commands
3. `C:\s\MS\STATUS.md` — current BIR baselines, HEAD commit, active iteration

Baselines (verify against STATUS.md): BIR=true=3, BIR=false=119. Jazz BIR=false=10.
(Iter 72 committed 99812fcbb5 — PC-count adaptive threshold. Bridge still on Jaccard.)

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Two architectural gaps remain in `collectNoteChangeTicks()` and
`greedyExpandSegmentation()` that together cause greedy-expand to produce
no placed regions for the Corelli op01n08d opening (measures 1–2), leaving
the bridge with zero coverage for the analysis window head.

**Gap A — Note-end ticks not collected.**
`collectNoteChangeTicks()` currently collects only note-START events (new
onsets). Per Pardo & Birmingham (Computer Music Journal, 2002), the correct
partition point set is ALL ticks where notes begin OR end: "harmonic changes
may occur only when notes begin or end." Music21's `chordify` implements
the same principle via salami-slicing. When the pitch-class set changes
because sustained notes release — without any new onset — the current
implementation misses that harmonic change entirely. This is an architectural
gap independent of the Corelli failures, but it matters for all sparse
counterpoint where voices enter and exit independently.

**Gap B — No coverage guarantee for the analysis window head.**
If Round 1 + Round 2 produce no placed region covering `[startTick,
firstPlacedRegion.startTick)`, the bridge receives zero chord coverage
for that span. This is always wrong — the analysis window was requested
for a reason. A final synthesis pass must ensure at least one covering
region exists from the window start.

Fix A (note-end ticks) may alone resolve the Corelli opening failures by
providing candidate boundary points that onset-only collection misses.
Fix B (head-gap synthesis) is a safety net that applies regardless.

---

## Step 1 — Read before touching anything

Read `src/composing/analysis/harmony/harmonicsegmenter.cpp` in full. Locate:
1. `collectNoteChangeTicks()` — the full body, especially the onset-only
   guard (`if (n->tieBack()) continue` and the `hasOnset` logic).
2. The main body of `greedyExpandSegmentation()` — find where the placed
   regions vector is finalized before being returned. This is where the
   head-gap synthesis pass (Fix B) will be inserted.
3. How `callbacks.collectRegionTones` is called — confirm the signature
   matches what Fix B will need.

Also read `src/engraving/dom/note.h` or wherever `Note::tieForward()` and
`Note::tieBack()` are declared, to confirm the tie API. Read how
`ChordRest::actualDuration()` (or equivalent) gives the note's sounding
duration so the end-tick can be computed.

---

## Step 2 — Fix A: add note-end ticks to collectNoteChangeTicks

In `collectNoteChangeTicks()`, after (or alongside) the existing onset
collection loop, add a note-end collection pass.

A note's end tick is: `chord->tick().ticks() + chord->actualDuration().ticks()`
(or the equivalent in the actual MuseScore API — read before writing).

**Tie handling — critical:**
- If a note has `tieForward()` set (it ties into the next note), do NOT
  add its end tick — the note continues; there is no harmonic release here.
- If a note does NOT have `tieForward()` (standalone or last in a tie chain),
  ADD its end tick — this is where the note truly releases.
- Notes with `tieBack()` (continuation notes) should be checked for
  `tieForward()` — if they tie onward, skip; if this is the last in the
  chain, add the end tick.

**Staff eligibility:**
Apply the same staff-eligibility filter as the onset pass — only add end
ticks from eligible staves (not in `excludeStaves`, passes
`callbacks.staffIsEligible`).

**Range filter:**
Only add end ticks within `[startTick, endTick)`. End ticks exactly at
`endTick` may be omitted (they are outside the analysis window).

**Deduplication is automatic** — the tick set is a `std::set`; inserting
a tick already present from the onset pass is a no-op.

Implementation shape (adjust to actual MuseScore API):
```cpp
// Note-end pass: collect ticks where notes release without tying forward.
// Per Pardo & Birmingham (2002): harmonic changes occur at note-on OR note-off.
for (Segment* seg = score->firstSegment(SegmentType::ChordRest);
     seg; seg = seg->next1(SegmentType::ChordRest))
{
    if (seg->tick() < startTick || seg->tick() >= endTick) {
        continue;
    }
    for (size_t staffIdx = 0; staffIdx < score->nstaves(); ++staffIdx) {
        if (excludeStaves.count(staffIdx)) { continue; }
        if (!callbacks.staffIsEligible(staffIdx)) { continue; }

        const EngravingItem* el = seg->element(staffIdx * VOICES);
        if (!el || !el->isChord()) { continue; }
        const Chord* chord = toChord(el);

        for (const Note* n : chord->notes()) {
            if (!n->play() || !n->visible()) { continue; }
            if (n->tieForward()) { continue; }  // not a true release

            const int endTickVal = chord->tick().ticks()
                                 + chord->actualDuration().ticks();
            if (endTickVal > startTick.ticks()
                && endTickVal <= endTick.ticks()) {
                tickSet.insert(endTickVal);
            }
            break;  // one release per chord per staff is enough
        }
    }
}
```

Read the existing onset-collection loop carefully and mirror its exact
iteration pattern (segment type, voice indexing, VOICES stride) — the
above is illustrative, not literal. Do not guess the MuseScore API.

---

## Step 3 — Fix B: head-gap synthesis

After `greedyExpandSegmentation()` completes its Round 1 + Round 2 placement
and before returning `placedRegions`, add a head-gap check:

```cpp
// Head-gap safety net: ensure the analysis window [startTick, ...) is covered.
// If the earliest placed region does not reach startTick, synthesize one
// covering region from the accumulated tones in the uncovered head span.
const int headEnd = placedRegions.empty()
    ? endTick.ticks()
    : placedRegions.front().startTick;

if (headEnd > startTick.ticks()) {
    const auto headTones = callbacks.collectRegionTones(
        startTick.ticks(), headEnd);
    if (!headTones.empty()) {
        const auto headResult = chordAnalyzer->analyzeChord(
            headTones, prefs,
            /*bilateralCtx=*/nullptr,
            keyFifths, keyMode);
        if (headResult.score > 0.0) {
            PlacedRegion headRegion;
            headRegion.startTick  = startTick.ticks();
            headRegion.endTick    = headEnd;
            headRegion.round      = 2;
            headRegion.confidence = headResult.score;
            headRegion.isAnchor   = false;
            headRegion.reason     = "head-gap-synthesized";
            headRegion.rootPitchClass = headResult.rootPitchClass;
            headRegion.bassPitchClass = headResult.bassPitchClass;
            headRegion.quality    = /* convert headResult.quality to string */;
            placedRegions.insert(placedRegions.begin(), headRegion);
        }
    }
}
```

Adjust field names and the quality-to-string conversion to match the actual
`PlacedRegion` struct and `analyzeChord` return type — read both before writing.

The same pattern should be applied symmetrically for a **tail gap** if
`placedRegions.back().endTick < endTick.ticks()`, for completeness.
Tail gaps are less common in practice but the same logic applies.

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

Required: 407/407 composing, 53/53 notation. Bridge still on Jaccard.
Any failure is a regression from Fix A or Fix B — stop and report.

---

## Step 5 — BIR validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Hard stops — revert harmonicsegmenter.cpp and report if:
- BIR=true increases above 3
- BIR=false increases above 119

BIR improvements in either direction are welcome — note them.

Jazz:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz hard stop: BIR=false > 75 (current 10). Restore Baroque corpus after.

---

## Step 6 — Update STATUS.md and commit

Remove any diagnostic instrumentation added during development.

Update `C:\s\MS\STATUS.md`: set HEAD commit, update BIR baselines to the
new values, set active iteration to "Iter 73 committed / bridge switch pending".

```bash
git add src/composing/analysis/harmony/harmonicsegmenter.cpp
git add C:\s\MS\STATUS.md
git commit -m "Composing: note-end tick collection + head-gap synthesis (Iter 73)

Fix A — Note-end ticks in collectNoteChangeTicks():
  Per Pardo & Birmingham (CMJ 2002), harmonic boundaries occur at note-on
  OR note-off. Add collection of note-release ticks (notes without
  tieForward) alongside existing onset collection. Deduplication is
  automatic (std::set). Enables detection of harmonic shifts caused by
  voice releases without coincident new onsets — architecturally correct
  for all sparse counterpoint.

Fix B — Head-gap synthesis:
  After Round 1 + Round 2, if [startTick, firstPlacedRegion.startTick)
  is uncovered, synthesize one covering region from the accumulated tones
  in that span. Ensures the bridge always receives chord coverage from
  the start of the requested analysis window. Symmetric tail-gap handling
  added for completeness.

BIR=true: 3 → N. BIR=false: 119 → N. Jazz BIR=false: 10 → N."

git push
```

---

## Step 7 — Re-attempt bridge switch

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

Update STATUS.md: mark §2.10 resolved, set active iteration "Iter 73 complete".

```bash
git add src/notation/internal/notationcomposingbridgehelpers.cpp
git add src/notation/tests/
git add C:\s\MS\STATUS.md
git commit -m "Composing: switch bridge path from Jaccard to greedy-expand (Task #58 Part B)

Replace detectHarmonicBoundariesJaccard() with greedyExpandSegmentation().
Iters 69–73 make greedy-expand texture-general:
  - Iter 69: vertical + horizontal density adaptive thresholds
  - Iter 70: sparse-texture threshold base, duration floor, Round 2 local-evidence
  - Iter 71: true-local chord distinctness, tuplet boundary alignment
  - Iter 72: PC-count adaptive score threshold
  - Iter 73: note-end tick collection, head-gap synthesis

Bridge and batch paths now use the same segmentation algorithm (§2.10).
Pipeline snapshot goldens refreshed.
BIR=true=N, BIR=false=N. Jazz BIR=false=N."

git push
```

**If tests still fail:** report remaining failures with actual vs expected.
Revert bridge file. Do not commit bridge change.

---

## Step 8 — Report to Cowork

```
Fix A — Note-end tick collection:
  New candidate ticks added vs onset-only (Baroque corpus sample): ~N%
  Effect on Corelli opening (m1-m2 now covered): [yes / no]

Fix B — Head-gap synthesis:
  Corelli opening head-gap synthesized: [yes / no — startTick=N, headEnd=N]
  Head region chord: [root / quality / confidence]

Tests (bridge on Jaccard):
  composing: N/407
  notation: N/53

BIR=true: 3 → N
BIR=false: 119 → N
Jazz BIR=false: 10 → N

Committed: [hash]

Bridge switch:
  notation_tests: N/53
  Remaining failures (if any): [list with actual vs expected]
  Pipeline snapshot goldens refreshed: [yes / no]
  Committed: [hash / not committed — reason]

§2.10 status: [resolved / still blocked — remaining issue]
```
