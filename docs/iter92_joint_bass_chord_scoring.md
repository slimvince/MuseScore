# Iter 92 — Joint (Bass, Chord) Scoring

*Design written 2026-05-16. Implements holistic bass+chord inference to fix two
confirmed bugs found during ground-truth QA.*

> **Status (updated 2026-05-20):** This design is **implemented and committed**
> (`80fe13b59b`). It remains the authoritative reference for the JOINT formula and its
> guards. Follow-up scope below has since landed: the `w_seq` bonus marked "deferred" in
> the weights table is committed (Iter 95, +0.20, P4-below descending-fifth, `distinctPcs ≥ 4`),
> and `w_dim` was added in Iter 96. The dim7/dominant family fix (STEP 1 / Gate J, commit
> `3d80d0a91d`) is a **separate subsystem** (diminished-triad completeness + vii°→V7
> completion) and does not supersede anything in this document. The "No code committed yet"
> framing in the original draft is historical.

---

## Background and motivation

The current analyzer pipeline is sequential:

1. Select bassPc from the lowest-pitched tone that meets `bassPassingToneMinWeightFraction`
2. Given bassPc, score all 12×16 = 192 (root, template) pairs
3. Return the highest-scoring pair

Two bugs discovered during ground-truth QA (2026-05-16) both flow from step 1 being
committed before step 2:

**Bug 1 — Passing-note bass contamination**

When the bass voice has two eighth notes within one beat window (e.g. G3 onset +
F#3 passing), the lower-pitched note wins on absolute MIDI pitch regardless of when
it entered the region. Both G3 and F#3 may have equal pcWeight (both = 0.20), equal
duration (240 ticks), but F#3 (MIDI 54) < G3 (MIDI 55) so F#3 is selected as bassPc.
This flips the chord root: instead of G major the analyzer infers Am/F# or Em/F#.

Confirmed by diagnostic on bwv293 region [4800,5280): two tones, equal evidence,
wrong one wins on lowest-pitch tiebreak.

**Bug 2 — Incomplete slash chord beats complete root-position triad**

Given pitch classes {C, E, G} with C in bass, Em/C scores ~2.86 while C major scores
~2.40 (gap ~0.46). Em/C wins even though:
- B (the 5th of Em) is absent from the region
- C is not a tone of the Em triad; it only "fits" as the bass of the slash chord

Root-position completeness (all triad tones present above extensionThreshold) provides
no scoring advantage in the current system. Seen on bwv103.6, bwv283, bwv310, bwv319.

---

## Design: JOINT (bass, chord) scoring

Replace the sequential two-step with a joint enumeration:

```
for each bass_candidate in bass_register_tones:
    for each (root, template) in 12×16:
        score = base_score(pcWeights, root, template)   // bass-independent matrix
                + bass_delta(bass_candidate, root, template)  // 3 of 7 components
                + w_complete * complete_bonus(bass_candidate, root, template)
                + w_onset   * onset_signal(bass_candidate)
                + w_passing * passing_penalty(bass_candidate)
                + w_stepIn  * stepIn_bonus(bass_candidate, previousBassPc)
                + w_stepOut * stepOut_bonus(bass_candidate, nextBassPc)
        track best (bass_candidate, root, template) triple
```

The winner is the (bass, root, template) triple with highest composite score.

### Bass candidates

"Bass register tones" = all tones `t` where `t.pitch < (lowestPitch + kBassRegisterSemitones)`.
Suggested `kBassRegisterSemitones = 12` (one octave). This is the same population the
existing `bassPassingToneMinWeightFraction` filter considers; the JOINT loop just
considers all of them as candidates rather than committing to one.

### Score decomposition

The 12×16 template scoring currently has 7 components. 4 are bass-independent (compute
once per (root, template)); 3 depend on bassPc:
- `appliedBassRootBonus` — depends on bassPc
- `nonBassAdjustment` — depends on bassPc
- inversion branch of `contextualBonuses` — depends on bassPc

Compute the bass-independent matrix (192 entries) once, then add the 3 bass-dependent
deltas for each candidate. With ~3–5 bass candidates this is ~3–5× the cost of the
current scoring loop — acceptable.

### JOINT formula weights (calibrated from empirical case data)

| Signal | Weight | Direction | Notes |
|--------|--------|-----------|-------|
| `w_complete` | +0.50 | bonus | All triad tones ≥ extensionThreshold AND distinctPcs≥3; bass-candidate must be root OR chord tone |
| `w_onset` | +0.15 | bonus | `t.onsetAtRegionStart == true` |
| `w_passing` | −0.10 | penalty | `t.onsetAtRegionStart == false` (enters mid-region) |
| `w_stepIn` | +0.10 | bonus | `(bass_candidate.pc - previousBassPc + 12) % 12 ∈ {1, 2, 10, 11}` (semitone or tone step) |
| `w_stepOut` | +0.10 | bonus | `(nextBassPc - bass_candidate.pc + 12) % 12 ∈ {1, 2, 10, 11}` |
| `w_seq` | deferred | — | Sequential root-progression bonus; depends on nextRootPc; deferred to later iter |

**Calibration rationale:**

- `w_complete = +0.50`: Bug 2 scoring gap is ~0.46. A 0.50 bonus applied to the
  root-position reading when all 3 triad tones are present closes the gap with a small
  margin. Gated on `distinctPcs≥3` to prevent Iter 90-style regressions where the gate
  fired on sparse (1–2 PC) regions.
- `w_onset = +0.15` / `w_passing = −0.10`: Bug 1 case has equal pcWeight and equal
  duration; a net 0.25 swing when the onset note also makes a better chord is sufficient
  to break the tie in the right direction. Kept small so the onset signal can be
  overridden by strong chord evidence on the other candidate.
- `w_stepIn/Out = +0.10` each: Smooth bass voice-leading is a real but weak signal.
  Kept below `w_onset` so it does not dominate.

### w_complete guard (prevents Iter 90-style regressions)

The Iter 90 unconditional iii/III flip caused +12/+22 regressions because it promoted
cases where the "complete" triad was genuinely Em/C (correct slash chord) rather than
C major. The `w_complete` guard is more restrictive:

```
complete_bonus applies when:
    distinctPcs >= 3
    AND pcWeight[triad_root] > extensionThreshold
    AND pcWeight[triad_3rd]  > extensionThreshold
    AND pcWeight[triad_5th]  > extensionThreshold
    AND bass_candidate.pc == triad_root
        (root-position reading only — not for slash chord candidates)
```

A genuine Em/C where B is present above threshold will NOT get the root-position bonus
for the C major reading (because C≠B, the 5th of Em, is not present at Em's 5th).
The existing Em/C slash-chord reading gets no bonus either (bass≠Em's root). Net effect:
correct slashes are not demoted; incorrect slashes (C, E, G only — B absent) lose to the
correct C major reading.

---

## Struct changes required

### `ChordAnalysisTone` (chordanalyzer.h, lines 50–72)

Add field:
```cpp
bool onsetAtRegionStart = false;
```

Populated by callers that know the region's startTick:
- `notationcomposingbridgehelpers.cpp::collectRegionTones` (~line 1172): already has
  `regionStartTick`; set `t.onsetAtRegionStart = (firstTickInRegion == regionStartTick)`.
- `buildTonesAtSegment` (~line 422): already has segment tick; compare to region startTick
  passed down from the caller.
- `tools/batch_analyze.cpp`: region startTick available from placed-region boundaries;
  set during tone collection.

### `ChordTemporalContext` (chordanalyzer.h, lines 517–559)

Add field:
```cpp
int nextBassPc = -1;   // -1 = unknown
```

Populated by:
- `notationharmonicrhythmbridge.cpp` (~lines 335–353): already computes nextBassPc locally
  for `bassIsStepwiseToNext`; assign `context.nextBassPc = nextBassPc` before discarding.
- `tools/batch_analyze.cpp` (~lines 1755–1771): already computes nextBassPc for
  `bassIsStepwiseToNext`; assign `context.nextBassPc` similarly.

---

## Implementation insertion point

`chordanalyzer.cpp` lines 1620–1655 (current bass-selection block). The joint loop
replaces these ~35 lines. The 12×16 scoring loop starting at ~line 1753 is refactored:
bass-independent components extracted into a helper, called once per (root, template),
then bass-dependent deltas added per candidate.

**Augmented root post-correction** (~lines 1898–1917) currently does:
```cpp
rootPc = normalizePc(lowestPitch);
```
This must change to:
```cpp
rootPc = winningBassPc;
```
where `winningBassPc` is the winning candidate's pc (not necessarily `lowestPitch`).

**`diagnoseChord`** (lines 2726+) mirrors `analyzeChord` and must be updated in sync.

---

## Four-step implementation and validation order

Run corpus check after each step. Each step must not increase total BIR errors before
proceeding.

**Step 1 — Bass-only joint (onset + passing only, no complete):**
Implement the (bass candidate) enumeration with only `w_onset` and `w_passing`. No
chord-identity bonuses yet. Verify Bug 1 cases improve, no new regressions.

**Step 2 — Add `w_complete`:**
Add the root-position completeness bonus with its guard. Verify Bug 2 cases improve.
Run Baroque + Jazz BIR check. Any increase in either = hard stop.

**Step 3 — Add `w_stepIn` / `w_stepOut`:**
Add voice-leading signals using `previousBassPc` / `nextBassPc`. Should be neutral to
slightly positive. Run BIR check.

**Step 4 — Full JOINT validation:**
Run full test suite (composing + notation + pipeline_snapshot). Update goldens if
any chord outputs changed (expected — new bass selections will affect chord symbols).
Run `--update-goldens` only after verifying changes are correct.

---

## Files to touch (in order)

1. `src/composing/analysis/chord/chordanalyzer.h` — add struct fields
2. `src/composing/analysis/chord/chordanalyzer.cpp` — joint scoring loop
3. `src/notation/internal/notationcomposingbridgehelpers.cpp` — populate `onsetAtRegionStart`
4. `src/notation/internal/notationharmonicrhythmbridge.cpp` — assign `context.nextBassPc`
5. `tools/batch_analyze.cpp` — assign `onsetAtRegionStart` and `context.nextBassPc`
6. Pipeline snapshot goldens — refresh after verifying changes are correct

---

## Tooling left in the tree (from Iter 90 investigation)

These remain useful for validation:
- `tools/analyze_wrong_root_iter90.py` — characterization script (122 cases)
- `tools/iter90_wrong_root_characterization.txt` — full enumeration (columns: stem, measure,
  beat, our quality, DCML quality, offset, bass-to-true, margin, alts_have_true)
- `tools/analyze_iter90_regressions.py` — dumps BIR=true cases with pcWeights, alts, key info
- `tools/inject_dcml_rn.py` — injects GT and US labels into MusicXML copies for visual QA

Run `tools/analyze_wrong_root_iter90.py` after implementing each step to track progress
against the 122 characterized cases.

---

## Expected outcome

Baroque BIR=false=188 should decrease significantly (target: sub-150). BIR=true=38 should
not increase materially. Jazz BIR=false=13 should remain stable (the completeness guard
is gated on distinctPcs≥3 which excludes sparse Jazz voicings that currently score correctly).
