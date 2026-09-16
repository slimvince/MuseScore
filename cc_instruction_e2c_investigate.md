# CC Instruction — E2c Investigation (read-only)

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 and §10.

**Current HEAD:** `710d8dba12` (E2b). Working tree clean.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**This is a READ-ONLY investigation. Make zero code changes. Report findings only.**

---

## Goal of E2c

E2c is the actual signal migration: move `rootContinuityBonus`, `wSeqBonus`, and
`wDimBonus` from `analyzeChord()` into `applyHarmonicFunction()`, using the
`ScoringSnapshot` from E2b so the function layer can redo joint scoring with the
signals applied. The result must be byte-identical to the current output.

Before writing the implementation instruction, this investigation must answer five
design questions that determine whether the implementation is straightforward or
requires structural additions to `ChordAnalysisResult`.

---

## Question 1 — What does `buildResult()` transform?

Inside `analyzeChord()`, the `buildResult` lambda converts a `RawCandidate` into
a `ChordAnalysisResult`. Read it fully.

Report:
- Every transformation it makes to `rootPc` (e.g. augmented-root correction)
- Every transformation it makes to `quality` (e.g. Sus2→Sus4 upgrade, Sus→Major
  omitsThird, any other normalisation)
- Every field it derives that is NOT in `RawCandidate` (e.g. extensions, degree,
  diatonic flag)
- Whether the final `ChordAnalysisResult.quality` can differ from
  `RawCandidate.quality` and in how many / which template cases

The concern: `applyHarmonicFunction()` will need to match a winning snapshot cell
(identified by `bassPc`, `rootPc`, `tiePriority`, raw `quality`) back to a
`ChordAnalysisResult` in `result.candidates`. If `buildResult()` changes `quality`
or `rootPc`, a simple field comparison fails.

---

## Question 2 — Does `ChordAnalysisResult` carry `tiePriority`?

Read the `ChordAnalysisResult` struct definition in `chordanalyzer.h`.

Report:
- Full field list
- Whether `tiePriority` (the template index) is present
- Whether `bassPc` is stored directly (not just derived from `bassTpc`)
- Whether raw (pre-correction) `rootPc` and `quality` are stored alongside the
  corrected values, or only the corrected values

The concern: `applyHarmonicFunction()` identifies the winning snapshot cell by
`(bassPc, rootPc, tiePriority)`. If `ChordAnalysisResult` does not carry
`tiePriority`, matching is ambiguous whenever two templates share the same
rootPc, bassPc, and (post-correction) quality — e.g. the major triad and the
major-add9 template over the same root.

---

## Question 3 — What variables are in scope at the three E1 call sites?

Read the three `applyHarmonicFunction()` call sites in `regionanalyzer.cpp`
(added in E1 — Pass 1 ~L457, Pass 2 ~L658, Pass 2b ~L844).

For each site report:
- The exact line numbers
- What `ChordAnalyzerPreferences` variable is in scope (name, const or mutable)
- Whether `context` (or the equivalent temporal-context struct) is in scope
- What `ScoringSnapshot`-sized local variable *could* be declared there
- Whether the refinement calls (`refineSparseChordQualityFromKeyContext`,
  `applyTonicPriorToSparseChord`) happen BEFORE or AFTER the
  `applyHarmonicFunction()` call at each site

The concern: E2c moves the refinement order — the refinements should run on the
function-layer-corrected winner, not the raw scorer winner. This may require
moving call sites.

---

## Question 4 — Can `analyzeChord()` return ALL candidates?

Read the threshold filter in `analyzeChord()` (~L2500–2520). Report:
- The exact formula (`(bestRawScore - winnerBassBonus) * kScoreThresholdRatio`)
- Whether `kScoreThresholdRatio` is a `constexpr` or `prefs`-settable value
- How many candidates typically survive (top-1, top-3, variable?)
- What the maximum possible candidate count is before the filter
  (12 rootPcs × N templates × |bassCandidates|, before dedup — give the exact N)
- Whether there is any existing mechanism for a caller to request a wider threshold
  or all candidates

The concern: `applyHarmonicFunction()` must be able to find the signal-inclusive
winner in `result.candidates`. If the suppressed-signal scorer filters it out
before returning, the function layer cannot promote it. The options are (a) widen
the threshold when `suppressProgressionSignals` is set, or (b) disable the
threshold entirely in that mode. Understanding the typical candidate count after
the filter informs how expensive option (b) is.

---

## Question 5 — How much does `ScoringSnapshot` cover vs. what E2c needs?

Read `ScoringSnapshot` and `ScoringCell` in `harmonicfunctionlayer.h`.

Report:
- Whether the snapshot contains enough information to reconstruct the signal-
  inclusive score for each cell without any additional input beyond what
  `applyHarmonicFunction()` already receives (context, prefs)
- Specifically: can `rootContinuityBonus` be re-applied using
  `fn::rootContinuityBonus(cell.rootPc, ctx.previousRootPc, prefs.rootContinuityBonus)`?
- Can `wSeqBonus` be re-applied using
  `fn::wSeqBonus(cell.rootPc, ctx.nextRootPc, snapshot.distinctPcs, ...)`?
- Can `wDimBonus` be re-applied using
  `fn::wDimBonus(cell.rootPc, cell.quality, ctx.nextRootPc, snapshot.distinctPcs, ...)`?
- What `jointScoringEnabled` and `explorationMode` flags does `applyHarmonicFunction()`
  need access to — are they in `prefs`, or do they need to be passed separately?
- Is `distinctPcs` (needed by `wSeqBonus` and `wDimBonus` gate conditions) stored
  in the snapshot? (It should be, per E2b.)

---

## Proposed implementation plan (after answering the above)

Based on findings from Questions 1–5, propose a concrete E2c implementation plan:

1. **Does `ChordAnalysisResult` need a new field?**  
   If `tiePriority` is absent, propose whether to add it (simple) or use a
   different matching strategy (e.g. match on `bassPc + rootPc + raw-quality`,
   accepting the small ambiguity risk).

2. **Threshold strategy:**  
   Which option is safer — (a) widen threshold when `suppressProgressionSignals`
   is set by multiplying by a larger ratio, (b) disable threshold entirely in that
   mode and let `applyHarmonicFunction()` filter, or (c) something else?

3. **`applyHarmonicFunction()` signature extension:**  
   What parameters does it need beyond the current `(result, ctx)` — specifically,
   does it need the full `ChordAnalyzerPreferences&` or just the fields it uses
   (rootContinuityBonus value, jointScoringEnabled, explorationMode)?

4. **Refinement reordering:**  
   Do the refinement calls need to move after `applyHarmonicFunction()` at any of
   the three sites? If so, at which sites and what is the new ordering?

5. **Step-bonus (Pass B) replication:**  
   The snapshot holds pre-step-bonus scores. The step bonus is applied in Pass B
   inside `analyzeChord()`. If the scorer runs without signals and the function
   layer re-applies signals, who runs Pass B on the re-scored cells? Propose a
   solution.

6. **What changes across which files:**  
   List every file that needs modification and the nature of each change.

---

## Report format

Answer each question with exact line numbers where relevant. For the proposed
plan, be concrete and flag any unresolved risks. The implementation instruction
will be written from this report.

**Make zero code changes.**
