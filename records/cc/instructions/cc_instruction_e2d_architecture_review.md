# CC Instruction: E2d Architecture Review — Second Opinion (read-only)

## Pre-reading

Read `C:\s\MS\STATUS.md` and `C:\s\MS\build_and_test.md` before starting.
Current HEAD: `0ab219d4c5` (Phase 1 / E2d-prereq). All tests pass.
This instruction is **read-only**. Do not modify any source file. No commits.

---

## Background

The E2d work aims to have `analyzeChord` run with `suppressProgressionSignals=true`
and have the function layer (`applyHarmonicFunction`) apply those signals afterwards.
Three implementation attempts have failed, each uncovering new defects.

Before writing another attempt, we want your independent architectural assessment.
**Please form your own views from the code.** There is no preferred answer; we want
your honest engineering judgment.

---

## Files to read

Read all of these in full before answering the questions:

1. `src/composing/analysis/function/harmonicfunctionlayer.h`
   — struct definitions (`ScoringCell`, `ScoringSnapshot`, `HarmonicFunctionContext`),
     function signatures, constant definitions.

2. `src/composing/analysis/function/harmonicfunctionlayer.cpp`
   — the full implementation of `applyHarmonicFunction` and the bonus functions.

3. `src/composing/analysis/region/regionanalyzer.cpp`
   — focus on the three call sites where the pipeline runs
     (`analyzeChord` → `applyHarmonicFunction` → `applyIter8691Pedal` →
      `applyPostScoringGates` → `refineSparseChordQualityFromKeyContext`).

4. `src/composing/analysis/chord/chordanalyzer.h`
   — `PostScoringGateContext` struct definition and `RawCandidate` struct.

5. `cc_e2d_v3c_investigation_report.md`
   — findings from the most recent investigation: the four known defects
     (BUG-A through BUG-C, GAP-D) and the tick-3840 failure trace.

---

## Questions

Answer each question after reading the files. Where a question asks what you
would do, give your honest first-principles answer — do not try to guess what
the existing code intends or what we want to hear.

---

### Q1 — What does `applyHarmonicFunction` currently do?

Describe in your own words:
- What inputs it reads (be precise about which fields of which structs).
- What it writes or mutates.
- What it leaves unchanged.

---

### Q2 — Pipeline data flow

Look at one of the three call sites in `regionanalyzer.cpp`.
`analyzeChord` produces two outputs that subsequent stages consume:
`results[]` and `gateCtx`.

- Trace exactly which stages read each of these two outputs and what they
  expect to find in them.
- Are there any assumptions a downstream stage makes about these outputs
  that could be violated by the time execution reaches that stage?
  If yes, describe exactly which assumption and what could violate it.

---

### Q3 — The four known defects

The investigation report lists BUG-A, BUG-B, BUG-C, and GAP-D.

- In your view, are these four independent defects, or are they related?
  If related, what connects them?
- What is the earliest point in the design where these defects become
  possible — i.e., what decision or constraint makes them possible at all?

---

### Q4 — Interface design

Set aside the existing implementation entirely.

Given `applyHarmonicFunction`'s intended role — receiving the chord scorer's
output, applying progression-context signals, and producing a result that
subsequent passes (Iter 86/91, post-scoring gates) can rely on — answer:

- What would you want this function to **read**?
- What would you want it to **write**?
- What would you want it to **leave untouched**?
- Would the existing signature support that, or would you change it?

There is no correct answer. We want to know what you would naturally reach for.

---

### Q5 — Fix strategy

Given that three implementation attempts have failed, each revealing a new
defect that the previous fix didn't anticipate:

- Do you think the right path is to fix the four known defects incrementally,
  or does something more fundamental need to change first?
- If you lean toward incremental fixes: are you confident there are no further
  hidden defects after BUG-A through C and GAP-D are addressed?
- If you lean toward something more fundamental: what would you change, and why?

Be honest if you are uncertain. "I don't know yet" is a valid answer if you
would need more information.

---

## Output

Write your findings to `C:\s\MS\cc_e2d_architecture_review_report.md`.

Use this structure:

```
# E2d Architecture Review

## Q1 — What applyHarmonicFunction currently does
…

## Q2 — Pipeline data flow
…

## Q3 — The four known defects
…

## Q4 — Interface design (from scratch)
…

## Q5 — Fix strategy
…

## Summary
3–5 sentences: your honest recommendation.
```

No code changes. No commits. Report only.
