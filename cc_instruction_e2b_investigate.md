# CC Instruction — E2b Investigation (read-only)

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 and §10.

**This is a READ-ONLY investigation. Make zero code changes. Report findings only.**

---

## Context

E2a (`80a7adf32e`) moved `rootContinuityBonus`, `wSeqBonus`, `wDimBonus` into
`harmonicfunctionlayer.{h,cpp}`; `chordanalyzer.cpp` still calls them from their
existing sites. E2b's goal is to expose a "scoring snapshot" — a struct that
`analyzeChord()` populates (when an opt-in flag is set) so that E2c can later
redo joint scoring with different bonuses from the function layer.

The E2 investigation concluded that a simple post-hoc re-rank from
`ChordAnalysisResult` alone is NOT viable because:
1. The threshold filter uses the bonus-inclusive winner score — removing bonuses
   lowers the threshold and changes which candidates survive into `results`.
2. `rootContinuityBonus` is folded into `basisIndep`, which affects bass selection.
3. `w_dim` dual-scoring can change which bass is chosen, and the without-wDim
   data does not survive the `analyzeChord()` call.

E2b must therefore capture enough state that E2c can redo the threshold filter,
bass selection, and `w_dim` quality guard independently of the scorer's bonus flags.

---

## What to read

### 1. `RawCandidate` struct

Find the `RawCandidate` struct definition in `chordanalyzer.cpp`. Report:
- All fields with their types
- Which fields represent: bass-independent base, bass-dependent delta,
  complexity/aug factors, bonus accumulation, final score
- Whether it stores rootPc, quality, bassPc, tiePriority, appliedBassBonus
  as separate fields or only as a combined score

### 2. Joint-scoring block structure (~L2287–2454)

Read the joint-scoring block. Report:
- The structure of `perBassWith` and `perBassWithout` — are they vectors of
  `RawCandidate` or some other type?
- How many elements each has (12 × 17 per bass, or a different layout)
- Where `scoreWith` and `scoreNoWDim` diverge — is it only at the `wDimDelta`
  accumulation point, or elsewhere too?
- Exactly when `wSeqBonus` is added — is it added to BOTH scoreWith and
  scoreNoWDim (E2 investigation says yes; confirm)?
- Exactly when `rootContinuityBonus` is applied — it goes into `basisIndep` at
  ~L2075; does that mean it is multiplied by `complexityFactor × augFactor`?

### 3. `bassCandidates` — type and source

What is the type of the bass-candidate collection? How is it constructed? Is it a
`std::vector<int>` of pitch classes, or a richer type? How many elements does it
typically have (1, 2, 3…)?

### 4. Threshold filter

Read the threshold filter at ~L2480. Report:
- The exact formula (`(bestRawScore - winnerBassBonus) * kScoreThresholdRatio`?)
- What `winnerBassBonus` is — is it the `appliedBassBonus` from the winner's
  `RawCandidate`?
- How many candidates typically survive the filter (top-1, top-3, variable?)

### 5. The without-wDim variant

The post-bonus quality guard at ~L2429-2449 chooses between the with-wDim and
without-wDim variants. After that choice:
- What happens to the losing variant's data? Is it std::move-discarded immediately?
- After the guard fires, which variant's `rawCandidates` enters the sort/threshold
  filter at ~L2480?

### 6. Minimum data for E2c

Based on the above, answer: what is the MINIMUM snapshot that E2c needs to:
(a) Reproduce the threshold filter with bonus-excluded scores?
(b) Reproduce the bass selection with bonus-excluded `basisIndep`?
(c) Reproduce the `w_dim` post-bonus quality guard?

Is it necessary to store the full 12 × 17 × |bass| table, or can a smaller
representation suffice (e.g. only the surviving top-N candidates after the
existing filter, tagged with their pre-bonus scores)?

---

## Specific questions

1. **`RawCandidate` fields**: List all fields. Which are needed to redo joint
   scoring? Which are derivable and don't need to be stored?

2. **Bass coupling**: Since `rootContinuityBonus` is folded into `basisIndep`
   (multiplied by `complexityFactor × augFactor`), can E2c simply subtract the
   bonus from `identity.score` to get the pre-bonus score, or does the
   multiplication mean a simple subtraction is wrong?

3. **`w_seq` neutrality**: Confirm that `wSeqBonus` is added identically to
   BOTH the `scoreWith` and `scoreNoWDim` accumulators (i.e. it does not affect
   the with/without-wDim choice). If confirmed, `w_seq` removal is simpler than
   `w_dim` removal.

4. **Snapshot size**: Roughly how many `RawCandidate` entries exist before the
   threshold filter (12 rootPcs × 17 templates × |bassCandidates| ≈ how many)?

5. **Simplest viable snapshot**: Could E2b get away with storing only the
   top-K candidates (e.g. top-10) from the without-wDim variant with their
   decomposed scores (`basisIndep`, `bassDep`, `complexityFactor`, `augFactor`),
   rather than the full pre-filter table? What would be lost?

6. **Proposed struct**: Propose a concrete `ScoringSnapshot` struct (name,
   fields, types) that is the minimum needed for E2c, given the above.
   Include a comment for each field explaining what E2c needs it for.

---

## Report format

Answer each of the 6 questions with exact line numbers where relevant.
Include the full `RawCandidate` field list.
Propose the `ScoringSnapshot` struct as valid C++ (it will go in
`harmonicfunctionlayer.h`).

**Make zero code changes.**
