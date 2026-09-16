# CC Instruction — E2 Investigation (read-only)

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 (bonus/penalty
terms) and §10 (harmonic function layer migration plan).

**This is a READ-ONLY investigation. Make zero code changes. Report findings only.**

---

## Context

E1 (`dd29a04967`) introduced the harmonic function layer shell:
`src/composing/analysis/function/harmonicfunctionlayer.{h,cpp}`. The files are
compiled into `composing_analysis` (not a separate module). Current interface:

```cpp
struct HarmonicFunctionContext {
    int keyFifths { 0 };
    analysis::KeySigMode keyMode { analysis::KeySigMode::Ionian };
    int previousRootPc { -1 };
    int nextRootPc { -1 };
};

void applyHarmonicFunction(analysis::ChordAnalysisResult& result,
                           const HarmonicFunctionContext& ctx);
```

Call sites in `regionanalyzer.cpp` (post-edit line numbers from E1 report):
- Pass 1: L457-464 (after BOTH `refineSparseChordQualityFromKeyContext` AND
  `applyTonicPriorToSparseChord` — function layer currently sees the refined winner)
- Pass 2: L658-665 (after `refineSparseChordQualityFromKeyContext`)
- Pass 2b: L844-851 (after `refineSparseChordQualityFromKeyContext`)

E2's goal is to migrate three progression signals OUT of `chordanalyzer.cpp` and
INTO `applyHarmonicFunction()`, with ZERO behavioral change.

The three signals to migrate (§4 of scoring_model.md):
1. `rootContinuityBonus` — at `bassIndependentContextualBonuses` (~L1652)
2. `w_seq` / `wSeqBonus` — joint-scoring lambda (~L2190)
3. `w_dim` / `wDimBonus` — joint-scoring lambda with dual-scoring mechanism (~L2209)

---

## What to read

### 1. `ChordAnalysisResult` definition

Read `src/composing/analysis/chord/chordanalyzer.h`. Find the `ChordAnalysisResult`
struct (or class). Report:
- Does it carry a `score` (or `totalScore`) field?
- Does it carry the candidate's `rootPc` and quality separately from `identity`?
- What fields are available that could be used to re-rank candidates in the
  function layer?

### 2. `rootContinuityBonus` — exact code

Read `chordanalyzer.cpp` around L1652. Report:
- The exact condition and bonus value
- What inputs it uses from `context` and from the per-candidate loop variables
- Whether it is additive to `basisIndep` only or affects both `basisIndep` and
  `bassDep`

### 3. `wSeqBonus` — exact code

Read `chordanalyzer.cpp` around L2190. Report:
- The exact lambda body
- All gate conditions (scoring_model.md §4 lists them; confirm against code)
- Exactly where in the joint-scoring loop it's accumulated

### 4. `wDimBonus` — dual-scoring mechanism

Read `chordanalyzer.cpp` around L2209. This is the most complex of the three.
Specifically investigate:
- How the two parallel scorings (with-wDim / without-wDim) are maintained
  — are there two separate score accumulators, two separate result vectors,
  or something else?
- Where the "post-bonus quality guard" check happens — the fallback from
  with-wDim to without-wDim if the with-wDim winner is not Dim/HalfDim
- What data structure (if any) the without-wDim variant is stored in, and
  for how long it lives in scope

### 5. Call site context in `regionanalyzer.cpp`

At each of the three call sites (Pass 1 ~L457, Pass 2 ~L658, Pass 2b ~L844):
- Is the full `results` vector (returned by `analyzeChord`) still in scope
  when `applyHarmonicFunction` is called?
- What is the variable name for the results vector at each call site?
- Is `distinctPcs` in scope? (needed for `w_seq` and `w_dim` gates)
- Confirm the exact variables that `HarmonicFunctionContext` would need added
  to support the three bonus gates

---

## Specific questions to answer

1. **Score field:** Does `ChordAnalysisResult` have a score field? If yes, is it
   the final total score (after all bonuses) or the pre-bonus base score?

2. **Re-ranking feasibility:** After removing the three bonuses from the scorer,
   could `applyHarmonicFunction` re-rank the alternatives by adding the bonuses
   to their stored scores and picking the new top? Or would it need a different
   mechanism (e.g. a `suppressProgressionSignals` flag that tells the scorer to
   run without them, then the function layer runs them)?

3. **`w_dim` dual-scoring:** The dual-scoring mechanism for `w_dim` is the most
   complex. Describe in plain English how `applyHarmonicFunction` would need to
   replicate it after the scorer has run without the bonus.

4. **Interface change needed:** Based on the above, what changes to
   `HarmonicFunctionContext` and/or the `applyHarmonicFunction` signature are
   needed for E2? Specifically:
   - Does `applyHarmonicFunction` need to receive the full results vector
     (instead of / in addition to the single result)?
   - Does it need `distinctPcs`?
   - Does it need anything else that is not currently in scope at the call sites?

5. **Ordering issue:** Currently, refinements (`refineSparseChordQualityFromKeyContext`,
   `applyTonicPriorToSparseChord`) are applied BEFORE `applyHarmonicFunction`.
   If the function layer needs to re-rank and potentially swap the winner, should
   the ordering be reversed (function layer first, then refinements on the new
   winner)? What would break if the ordering changed?

---

## Report format

For each of the 5 questions above, give a clear answer. Include exact line numbers
for the code you examined. Do not speculate — read the code.

If you find that E2 is best split into smaller sub-steps (e.g. migrate only
`rootContinuityBonus` first, leaving `w_seq` and `w_dim` for E2b), say so and
explain why.

**Make zero code changes.**
