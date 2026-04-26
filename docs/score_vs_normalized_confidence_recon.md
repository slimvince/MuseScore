# `score` vs `normalizedConfidence` Recon

Date: 2026-04-26  
Scope: read-only, no source edits.  
Base commit: `f6fcc20fe5`

---

## Verdict

**Unused metric.**  `ChordIdentity::normalizedConfidence` has no live consumers
post-Divergence-E.  The only callers — the right-click menu sort and the status-bar
sort — were removed in commit `9047b8adf9`.  The pedal detection code explicitly
declines to read it, computing its own inline sigmoid for documented reasons (see Q4).

The m285 ordering disagreement (the trigger for this recon) was **not a calculation
bug**: the two metrics measure fundamentally different things, and sorting by
`normalizedConfidence` was semantically wrong to begin with.  The disagreement was a
symptom of incorrect usage, already corrected.

**Recommendation:** Remove `ChordIdentity::normalizedConfidence` and its two supporting
preference parameters (`confidenceSigmoidMidpoint`, `confidenceSigmoidSteepness` in
`ChordAnalyzerPreferences`) as dead code.  The metric served as a prototype for future
use; that future has not materialized, and the supporting infrastructure is now only
maintenance burden.

---

## Q1 — `score` semantics

**Declaration:** `ChordIdentity::score` (`double`), `chordanalyzer.h:191`.

```cpp
double score = 0.0;  ///< Template match score (higher = better); ranking only.
```

**Computation:** Summed across 7 additive components during the 12 × 16-template
scoring loop (`chordanalyzer.cpp:1698–1706`):

| Component | Function | Sign |
|---|---|---|
| Template tone coverage | `scoreTemplateTones()` | + |
| Extension bonus / contradiction penalty | `scoreExtraNotes()` | ± |
| Diminished-7th characteristic bonus | `dim7CharacteristicBonus()` | + |
| Non-bass adjustment (e.g., HalfDim m7 in non-bass role) | `nonBassAdjustment()` | ≤ 0 |
| Structural penalties | `structuralPenalties()` | ≤ 0 |
| TPC spelling consistency bonus | `tpcConsistencyBonus()` | + |
| Contextual bonuses (bass-root, diatonic, continuity, resolution) | `contextualBonuses()` | + |

One post-scoring deduction is possible: when inversion suspicion fires
(`chordanalyzer.cpp:1938–1948`), the winner's `score` is reduced by a fraction of the
bass-root bonus and the list is re-sorted.  `normalizedConfidence` is populated
**after** this deduction (`chordanalyzer.cpp:1953`), so it uses final scores.

**Bounds:** Open-ended.  Empirical range from the catalog dump: roughly 4.0–8.0 for
typical real-music chords.

**Semantics:** Absolute quality of one chord template's fit to the observed pitch-class
weights at a given tick.  Higher = better fit.  Used exclusively for candidate ranking
(`chordanalyzer.cpp:1716–1721`, `1946`).

---

## Q2 — `normalizedConfidence` semantics

**Declaration:** `ChordIdentity::normalizedConfidence` (`double`), `chordanalyzer.h:192`.

```cpp
double normalizedConfidence = 0.0;  ///< Sigmoid-normalized score gap, 0.0–1.0; see §P8d.
```

**Computation:** After ranking is complete (`chordanalyzer.cpp:1953–1963`):

```cpp
results[0].identity.normalizedConfidence
    = normalizeChordConfidence(winnerScore, runnerUpScore, prefs);
for (size_t i = 1; i < results.size(); ++i) {
    const double iRunnerUp = (i + 1 < results.size()) ? results[i+1].identity.score : 0.0;
    results[i].identity.normalizedConfidence
        = normalizeChordConfidence(results[i].identity.score, iRunnerUp, prefs);
}
```

Where `normalizeChordConfidence` (`chordanalyzer.cpp:1467–1473`) is:

```cpp
gap = winnerScore - runnerUpScore;
return 1.0 / (1.0 + std::exp(-steepness * (gap - midpoint)));
```

Parameters (from `ChordAnalyzerPreferences`, `chordanalyzer.h:401–409`):
- `confidenceSigmoidMidpoint = 2.0` — gap at which confidence = 0.5
- `confidenceSigmoidSteepness = 1.5` — transition sharpness

**Bounds:** [0.0, 1.0] (sigmoid output).

**Semantics:** The confidence computed for candidate at position `i` is a function of
the gap between `score[i]` and `score[i+1]` — the next candidate's score.  It answers:
*"how much margin does this candidate have over the one ranked just below it?"*

**Critical property:** `normalizedConfidence` is **not monotonic with `score`**.  For
candidates at different positions in the sorted list:

- `results[0].normalizedConfidence` = sigmoid(score[0] − score[1])  — gap to runner-up
- `results[1].normalizedConfidence` = sigmoid(score[1] − score[2])  — gap to third (or 0)
- `results[2].normalizedConfidence` = sigmoid(score[2] − 0)          — gap to nothing

When the winner and runner-up have equal or near-equal scores, the runner-up's
`normalizedConfidence` is large (large gap to third/nothing) while the winner's is near
zero (gap ≈ 0).

**Concrete m285 example** (the trigger case from commit `ee50b1760c`):

```
results[0]  score=5.15  Csus#4       normalizedConfidence = sigmoid(5.15 − 5.15) = sigmoid(0)
                                     = 1/(1+exp(-1.5×(0−2.0))) = 1/(1+exp(3.0)) ≈ 0.047

results[1]  score=5.15  D7#5/C       normalizedConfidence = sigmoid(5.15 − 0)    = sigmoid(5.15)
                                     = 1/(1+exp(-1.5×(5.15−2.0))) ≈ 0.991
```

Sorting by `normalizedConfidence` descending puts `D7#5/C` (the runner-up by score)
ahead of `Csus#4` (the winner by score).  This is **mathematically correct given the
formula** — it is not a calculation bug.

---

## Q3 — Introduction history

**`score`:** Present from the earliest commits.  Part of the original chord analyzer
design.

**`normalizedConfidence`:** Introduced in commit `a8893a9bc4`
("P8d: chord confidence normalization (sigmoid, same shape as key analyzer)").
Commit message: *"add normalizedConfidence (0.0–1.0) alongside raw score"* — explicitly
described as a supplementary metric, not a replacement for `score`.  Added with the
intent of matching the shape of `KeyModeAnalyzerResult::normalizedConfidence`, which IS
actively used.

**Usage history:**

| Commit | Change |
|---|---|
| `a8893a9bc4` | Introduced — computed, no consumer yet |
| `cdaa008e74` (session 26) | Added to status-bar and right-click sort |
| `9047b8adf9` | Removed from both sorts (Divergence E fix) |

Neither commit introducing the sort documented why `normalizedConfidence` was preferred
over `score` for sorting.  The Divergence E recon (`docs/three_paths_divergence_recon.md`)
identified the sort as incorrect and removed it.

---

## Q4 — Consumer sites

### `ChordIdentity::normalizedConfidence` (the field in question)

**Write sites:** `chordanalyzer.cpp:1957`, `chordanalyzer.cpp:1961` (both within
`analyzeChord()`).

**Live read sites:** **None.**

The two consumers that existed before `9047b8adf9`:
- Right-click menu sort (`notationcontextmenumodel.cpp`) — removed
- Status-bar sort (`notationcomposingbridge.cpp`) — removed

**Pedal detection** (`chordanalyzer.cpp:2015–2041`) uses the same sigmoid formula and
the same preference parameters, but **explicitly avoids reading `identity.normalizedConfidence`**.
Instead it computes `c2` inline:

```cpp
// Confidence is measured against the first competitor with a DIFFERENT root.
// Multiple templates for the same chord quality can score identically when their
// extended tones are absent, filling all three result slots with the same root
// — making normalizedConfidence artificially low.
// Comparing the winner's score against the best genuine alternative (different rootPc)
// gives a meaningful pedal-confirmation signal.
double pass2AltScore = 0.0;
// ... find first result with different rootPc ...
const double gap = pass2.front().identity.score - pass2AltScore;
const double c2 = 1.0 / (1.0 + std::exp(-steepness * (gap - midpoint)));
if (c2 >= prefs.pedalConfidenceThreshold) { ... }
```

The comment documents the known defect: when the top-3 result slots are filled with
the same root (e.g., C major triad / C major7 / C9 — all same root), `score[0] − score[1]`
approaches zero even for a clear winner, making `normalizedConfidence` ≈ 0.
The pedal code avoids this by comparing against the best **different-root** alternative.
This is an acknowledged design limitation of gap-to-next as a confidence measure.

### `KeyModeAnalysisResult::normalizedConfidence` (unrelated field, same name)

The `normalizedConfidence` field on `KeyModeAnalysisResult` (a different struct entirely)
IS actively used throughout the key stabilization pipeline:
`notationcomposingbridgehelpers.cpp:634, 681, 710, 720`, `notationcomposingbridge.cpp:279`,
`notationharmonicrhythmbridge.cpp:300, 739`.  This field is not under investigation and
is working correctly.

---

## Q5 — Synthesis and recommendation

### Classification: **Unused metric**

`ChordIdentity::normalizedConfidence` is computed in `analyzeChord()` and stored in
the returned result objects, but no live code reads it.  The two preference parameters
that control its shape (`confidenceSigmoidMidpoint`, `confidenceSigmoidSteepness`) are
similarly dead.

The m285 ordering disagreement was not a calculation error.  It was an incorrect
use of a gap-to-next metric for sorting — a sorting-by-confidence-rather-than-score
error, now corrected.  The metrics diverge by design at tie points and near-tie points
because they answer different questions.

### Why the pedal detection re-derives confidence inline

The inline `c2` computation in pedal detection is a partial redesign of what
`normalizedConfidence` was meant to provide: it uses the same sigmoid but avoids the
same-root-fills-all-slots degenerate case.  The existence of this ad-hoc inline signals
that the original gap-to-position-i+1 formula was known to be insufficient.

### Recommended next action

**Remove** `ChordIdentity::normalizedConfidence` and the two supporting preference
parameters as a cleanup pass.  The removal is:

1. Safe — zero live read sites.
2. Small — three field removals, two preference parameter removals, the
   `normalizeChordConfidence()` static function, and the populate loop at
   `chordanalyzer.cpp:1953–1963`.
3. Clarifying — removes the temptation for future code to sort by it again.

If a genuine confidence signal is needed in future (e.g., for a chord panel UI that
shows "50% confident" next to each candidate), it should be re-derived using the
different-root gap logic from pedal detection, not the position-i+1 gap.  That would
be a separate design effort with a clearer spec.
