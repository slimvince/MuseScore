# Design: Temporal Context Expansion for Inversion Disambiguation

## Status: design memo — read before implementing

This document describes the full set of temporal context signals that should be
added to resolve inversion confusion, plus how the preset system should modulate
their strength.  Implement after `fix_prefer_minor7_baroque_preset.md` is in
place (the preset flag is the last-resort fallback; this work makes it rarely
needed).

---

## The problem in one sentence

The remaining 151 genuine inversion errors (Bb6 → Gm7/Bb etc.) occur in regions
where the raw scoring gap between the bass-root winner and the correct inverted
alternative is ~1.4, well above the `inversionSuspicionMargin` of 0.70.  Every
point the gap closes below 0.70 is a case the existing correction handles
automatically.  More temporal signals → smaller gaps → more automatic fixes →
fewer cases needing the preset fallback.

---

## What is already in the system

`ChordTemporalContext` currently carries:
- `previousRootPc` — root of the previous chord
- `previousQuality` — quality of the previous chord
- `previousBassPc` — bass of the previous chord
- `bassIsStepwiseFromPrevious` — bass moved by diatonic step from prev
- `bassIsStepwiseToNext` — bass moves by diatonic step to next region
- `nextBassPc` — bass pitch class of the next region (used for lookahead)

These feed the existing bonuses (all applied only to inverted Major/Minor
candidates):
- `stepwiseBassInversionBonus`        +0.50 (stepwise from prev)
- `stepwiseBassLookaheadBonus`        +0.50 (stepwise to next)
- `sameRootInversionBonus`            +0.40 (prev root == candidate root)
- `completeTriadInversionBonus`       +0.45 (stepwise + full triad present)

Maximum current bonus: +1.85 (all four firing).  Raw gap to close: ~1.4.
So full temporal evidence already closes the gap.  The 151 errors are cases
where the evidence is partial or absent.

---

## New signals to add

### Signal 1 — Next region's inferred root  (`nextRootPc`)

**What:** the chord root of the NEXT harmonic region, not just its bass note.

**Why powerful:** if the next chord's root matches the current inversion
candidate's root (e.g. current region is Bb-bass, next region is Gm7 in root
position), the current region is almost certainly the same harmony in inversion.
Analogous to `sameRootInversionBonus` (previous root) but looking forward.

**Implementation in `batch_analyze.cpp`:** `nextBassPc` is already being looked
up by peeking at the next region's tones.  Extend this peek to also run a
lightweight `analyzeChord` call (or reuse the next iteration's result) and store
the root as `ctx.nextRootPc`.  This requires a one-region look-ahead cache.

**New field in `ChordTemporalContext`:**
```cpp
int nextRootPc = -1;   ///< Inferred root of the next harmonic region; -1 if unknown.
```

**New preference:**
```cpp
/// Bonus for an inverted Major/Minor candidate whose root matches the
/// NEXT region's chord root.  The harmony is about to return to the
/// inversion's true root, confirming the current note is a passing bass.
double nextRootMatchesAltInversionBonus = 0.50;
```

**Scoring location:** inside `contextualBonuses()`, alongside the existing
`sameRootInversionBonus` block:
```cpp
if (isInvertedMajMin
    && context->nextRootPc != -1
    && context->nextRootPc == rootPc) {
    score += prefs.nextRootMatchesAltInversionBonus;
}
```

---

### Signal 2 — Consecutive stepwise bass count  (`consecutiveBassStepwiseCount`)

**What:** how many consecutive regions (including the current one) have shown
stepwise bass motion.  C→Bb→A→G over four regions = count of 3 at the Bb
region.

**Why powerful:** a single stepwise bass step might be coincidence; two or more
in sequence almost always means a passing/scalar bass line, making every
non-root tone in the sequence an inversion.

**New field in `ChordTemporalContext`:**
```cpp
int consecutiveBassStepwiseCount = 0;  ///< How many consecutive stepwise bass moves ending here.
```

**Implementation in `batch_analyze.cpp`:** track a running counter alongside
`previousBassPc`; increment when stepwise, reset to 0 on a leap.

**New preference:**
```cpp
/// Additional bonus per consecutive stepwise bass region beyond the first,
/// for inverted Major/Minor candidates.  Scalar bass lines are strong
/// evidence of passing inversions.
/// Applied as: consecutiveBassStepwiseCount * bonus (capped at 3).
double consecutiveBassStepwiseInversionBonus = 0.30;
```

**Scoring location:** inside `contextualBonuses()`:
```cpp
if (isInvertedMajMin && context->consecutiveBassStepwiseCount >= 2) {
    const int extraSteps = std::min(context->consecutiveBassStepwiseCount - 1, 3);
    score += extraSteps * prefs.consecutiveBassStepwiseInversionBonus;
}
```

---

### Signal 3 — Recent root window  (`recentRootPcs`)

**What:** a short circular buffer of the last 2–3 chord roots before the current
region.

**Why powerful:** if G appeared as a chord root 1–3 regions ago and the current
region has Bb in the bass with pitch classes matching Gm7, the harmony almost
certainly persisted into inversion rather than switching to a new Bb6 chord.
Progression memory beyond just the immediately previous chord.

**New field in `ChordTemporalContext`:**
```cpp
std::array<int, 3> recentRootPcs = {-1, -1, -1};
///< Root pitch classes of the 3 most recent regions, most recent first.
///< -1 = not yet available.
```

**Implementation in `batch_analyze.cpp`:** maintain a rolling buffer of the last
3 inferred roots and copy it into `ctx` at each region.

**New preference:**
```cpp
/// Bonus for an inverted Major/Minor candidate whose root appeared as a
/// chord root within the recent window.  The harmony is persisting;
/// the current region is a bass inversion of the active harmony.
/// Applied once regardless of how many times the root appeared.
double recentRootMatchesAltInversionBonus = 0.35;
```

**Scoring location:**
```cpp
if (isInvertedMajMin) {
    for (int recentRoot : context->recentRootPcs) {
        if (recentRoot == rootPc) {
            score += prefs.recentRootMatchesAltInversionBonus;
            break;  // Apply once only
        }
    }
}
```

---

### Signal 4 — Metric weight of current region  (`regionMetricWeight`)

**What:** a normalised [0,1] value reflecting the metric strength of the beat
on which this region falls — 1.0 for a strong downbeat, lower for weak beats
and offbeats.

**Why useful:** root-position chords dominate structurally strong beats;
inversions and passing chords cluster on weak beats.  A Bb-bass chord on beat 2
of a 4/4 bar is far more likely to be an inversion than the same chord on beat 1.

**New field in `ChordTemporalContext`:**
```cpp
double regionMetricWeight = 1.0;  ///< Normalised metric strength [0,1]; 1=downbeat.
```

**Implementation:** `batch_analyze.cpp` already has `getBeatWeight()`.  Convert
the enum value to a normalised float and store in ctx.

**New preference:**
```cpp
/// Bonus applied to inverted Major/Minor candidates when the region falls
/// on a metrically weak beat (regionMetricWeight < weakBeatThreshold).
double weakBeatInversionBonus = 0.30;

/// Threshold below which a region is treated as metrically weak.
double weakBeatThreshold = 0.60;
```

**Scoring location:**
```cpp
if (isInvertedMajMin
    && context->regionMetricWeight < prefs.weakBeatThreshold) {
    score += prefs.weakBeatInversionBonus;
}
```

---

## Preset scaling of ALL inversion bonuses

Currently every inversion-related bonus uses a single default value regardless
of preset.  The Baroque preset should substantially increase all of them; Jazz
should decrease most of them (since bass-root 6th chords are structurally normal
in jazz and should not be de-emphasised).

Extend the preset builder in `batch_analyze.cpp`:

```cpp
analysis::ChordAnalyzerPreferences chordPrefs;

if (presetName == "Jazz") {
    chordPrefs.extensionThreshold                    = 0.12;
    chordPrefs.preferMinor7OverMajorAdd6             = false;
    // Contextual inversion bonuses reduced — bass-root 6th chords are idiomatic
    chordPrefs.stepwiseBassInversionBonus            = 0.20;
    chordPrefs.stepwiseBassLookaheadBonus            = 0.20;
    chordPrefs.sameRootInversionBonus                = 0.15;
    chordPrefs.completeTriadInversionBonus           = 0.20;
    chordPrefs.nextRootMatchesAltInversionBonus      = 0.20;
    chordPrefs.consecutiveBassStepwiseInversionBonus = 0.10;
    chordPrefs.recentRootMatchesAltInversionBonus    = 0.15;
    chordPrefs.weakBeatInversionBonus                = 0.10;

} else if (presetName == "Baroque") {
    chordPrefs.preferMinor7OverMajorAdd6             = true;  // last-resort fallback
    // Contextual inversion bonuses amplified — inversions are extremely common
    // in counterpoint; bass lines are characteristically stepwise
    chordPrefs.stepwiseBassInversionBonus            = 0.80;
    chordPrefs.stepwiseBassLookaheadBonus            = 0.80;
    chordPrefs.sameRootInversionBonus                = 0.65;
    chordPrefs.completeTriadInversionBonus           = 0.70;
    chordPrefs.nextRootMatchesAltInversionBonus      = 0.70;
    chordPrefs.consecutiveBassStepwiseInversionBonus = 0.50;
    chordPrefs.recentRootMatchesAltInversionBonus    = 0.55;
    chordPrefs.weakBeatInversionBonus                = 0.50;

} else {
    // Standard, Modal, Contemporary: defaults + prefer Minor7 over Major add6
    chordPrefs.preferMinor7OverMajorAdd6             = true;
}
```

**The role of `preferMinor7OverMajorAdd6` in this scheme:** it is the last-resort
fallback for regions where ALL temporal signals are absent (phrase starts,
isolated chords, no previous or next context).  In those cases the new signals
contribute nothing, and the gap stays at ~1.4.  The flag ensures the correct
reading still wins even then.  As temporal coverage improves, fewer and fewer
regions need the flag — it becomes a safety net rather than the primary mechanism.

---

## Implementation order

1. Add new fields to `ChordTemporalContext` (header change — one pass).
2. Populate them in `batch_analyze.cpp` (build the look-ahead cache, rolling
   buffer, metric weight conversion).
3. Add new preferences to `ChordAnalyzerPreferences` with conservative defaults
   (so non-preset callers are unaffected).
4. Add scoring logic in `contextualBonuses()` in `chordanalyzer.cpp`.
5. Wire preset values in `batch_analyze.cpp` preset builder.
6. Build, run 407/407 tests (defaults unchanged → no regressions expected).
7. Run corpus with `--preset Baroque` and report 3-way genuine error count.

## Verification

```
Build:                     pass / fail
Tests:                     407/407 pass (default prefs unchanged)
RealDiff:                  before=4, after=N
Corpus run preset used:    Baroque  ← must confirm explicitly
3-way genuine errors:      before=151, after=N
2-way bassIsRoot:          before=805, after=N
Signals firing breakdown:  how many of the 151 are now resolved by each signal
                           (extend analyze_inversion_errors.py if possible)
Regressions:               none / <description>
```
