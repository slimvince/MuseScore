# Iteration 1: Investigation — analyzeSection structure

## ⚠ Critical behaviour rules for this session

- **This is a read-only investigation. Make zero code changes.**
  Your only job is to read, understand, and report. Nothing else.
- **Think carefully and report findings in full detail.**
  The purpose of this iteration is to give enough information to write
  Iteration 2 precisely, without another investigation pass.
- **Do not propose or begin implementing anything.**
  If you see something that looks wrong or improvable, note it in your report
  under "Unexpected findings" and stop there.
- **Do not commit anything.**

---

## Step 1 — Context loading

Read ALL of these before investigating:

1. `CLAUDE.md` — standing instructions
2. `STATUS.md` — top summary line and 2026-05-04 and 2026-05-05 entries only
3. `ARCHITECTURE.md` — §2.10, §4.1c, §4.1d in full
4. `docs/unified_analysis_pipeline.md` — read in full; pay close attention to:
   - The P1/P2/P3/P4 path consolidation table
   - The "Divergence D" closure description
   - The `AnalyzedRegion::temporalExtensions` migration plan (Phase 3c)
   - The `ChordTemporalContext` audit findings (dead fields section)
5. `docs/prompts/iteration_plan_inversion_redesign.md` — read in full

---

## Step 2 — Find and read analyzeSection

Search the entire codebase for `analyzeSection`:

```
grep -r "analyzeSection" C:\s\MS\src --include="*.h" --include="*.cpp" -l
grep -r "analyzeSection" C:\s\MS\tools --include="*.h" --include="*.cpp" -l
```

For every file that contains `analyzeSection`:
- Read the full function signature(s)
- Read the full implementation
- Note the file path and namespace

Report: where does `analyzeSection` live? What is its full signature?

---

## Step 3 — Understand analyzeSection internals

Read the full implementation of `analyzeSection` and report in detail:

**A. Region loop structure**
- How does it iterate over harmonic regions?
- Is it a single pass or multiple passes?
- Does it currently have any look-ahead logic?
- Does it currently maintain any rolling state between regions
  (e.g., previous root, running counters, buffers)?

**B. ChordTemporalContext construction**
- How is `ChordTemporalContext` currently built per region?
- Which fields does it populate, and how?
- Does it call `findTemporalContext()`? Or build context inline?
- Does it already populate `nextRootPc`, `consecutiveBassStepwiseCount`,
  `recentRootPcs`, `regionMetricWeight`? If so, how? If not, confirm they
  are absent.

**C. AnalyzedRegion struct**
- Read the full `AnalyzedRegion` struct definition
- Is there an `temporalExtensions` field or equivalent?
- What fields does `AnalyzedRegion` currently carry?
- Where is it defined?

**D. analyzeChord call site**
- Where inside `analyzeSection` is `analyzeChord` called?
- What context object is passed to it?
- Is the context object built fresh per region or accumulated?

---

## Step 4 — Understand how P1/P2/P3 call analyzeSection

Search for all call sites of `analyzeSection`:

```
grep -r "analyzeSection" C:\s\MS\src --include="*.cpp" -n
```

For each call site:
- Which path is it? (chord staff population / annotation / status bar / context menu)
- What arguments does it pass?
- Does any call site do post-processing of `ChordTemporalContext` after the call?
- Does any call site currently call `findTemporalContext()` separately?

Also search for remaining uses of `findTemporalContext`:
```
grep -r "findTemporalContext" C:\s\MS\src --include="*.cpp" -n
```
Report every location.

---

## Step 5 — Understand the two-pass requirement

For `nextRootPc` to be populated, `analyzeSection` needs to know the next region's
inferred root before analyzing the current region. This requires either:
- A two-pass approach: first pass collects all region boundaries and runs a lightweight
  root inference; second pass runs full `analyzeChord` with the look-ahead populated
- A one-region cache: each iteration peeks at the next region's tones, runs a quick
  `analyzeChord` with no context (default prefs, no temporal context) to get
  `nextRootPc`, then proceeds with the current region's full analysis

The batch_analyze.cpp loop already implements the one-region-cache approach.
Read the relevant section of `batch_analyze.cpp` (search for `nextRootPc` population)
and report exactly how it does it. Then assess: would the same approach be feasible
inside `analyzeSection`? Are there any structural obstacles?

---

## Step 6 — Assess migration feasibility

Based on your findings, answer these questions:

1. Is `analyzeSection` the correct place to add temporal context computation,
   or is there a more appropriate location (e.g., a helper it calls, or a wrapper
   around it)?

2. What would need to change in `analyzeSection` to support:
   - Rolling `recentRootPcs` buffer (3-region window)
   - Running `consecutiveBassStepwiseCount` counter
   - Per-region `regionMetricWeight` from beat type
   - Per-region `nextRootPc` via one-region look-ahead

3. After the move, would `batch_analyze.cpp` need to keep any of its current
   temporal context population code, or could it be removed entirely?

4. Are there any dependency or interface constraints that would prevent moving
   this logic from `batch_analyze.cpp` to `src/composing/`?
   (e.g., types not available in the composing module, Score* dependencies)

5. Does `findTemporalContext()` in the bridge become redundant after the move,
   or does it serve a different purpose?

---

## Step 7 — Report

Provide a detailed prose + code-excerpt report covering all findings from Steps 2–6.

Structure:
```
analyzeSection location:     file path, namespace, signature
Single or multi-pass today:  single / multi
Current rolling state:       yes (describe) / none
Look-ahead today:            yes (describe) / none
ChordTemporalContext fields populated today: <list>
Fields absent today:         <list>
AnalyzedRegion temporalExtensions: present / absent
findTemporalContext() call sites: <list with file:line>
Migration feasibility:       feasible / obstacles: <describe>
One-region-cache approach:   feasible inside analyzeSection / obstacles: <describe>
Recommended implementation approach for Iteration 2: <describe in enough detail
  that Iteration 2 can be written without further investigation>
Unexpected findings:         none / <describe>
```

No code changes. No commits.
