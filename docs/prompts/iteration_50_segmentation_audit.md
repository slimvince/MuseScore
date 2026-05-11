# Iteration 50: Replacement segmentation — architectural audit

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Confirmed baselines: BIR=true=21, BIR=false=128. Jazz BIR=false=20.

Do NOT change any source code in this iteration. Read and report only.

---

## Background

`detectHarmonicBoundariesJaccard` is deprecated (Task #62). It will be replaced
by an iterative greedy-expand algorithm. Implementation begins in `tools/batch_analyze.cpp`
(corpus/BIR path) first; the display path follows after BIR validation.

Before writing any code, we need a precise map of the integration points so the
replacement plugs in cleanly without structural surprises.

---

## Step 1 — Map the segmentation pipeline in batch_analyze.cpp

Read `tools/batch_analyze.cpp` in full. Answer:

1. What function(s) call `detectHarmonicBoundariesJaccard` (or equivalent boundary
   detection logic)? At what line(s)?

2. What inputs does the boundary detection receive?
   - Score/measure data: what type, where does it come from?
   - Pitch-class information: how are pitch classes collected per window?
   - Preferences/threshold: what struct/fields carry these?

3. What does the boundary detection return or produce?
   - What is the region data structure? List every field.
   - How are start/end positions represented (tick, measure+beat, quarter-note index)?

4. What happens immediately after boundary detection?
   - How are regions passed to the chord scorer?
   - What function scores each region? At what line?
   - What does the scorer return per region?

5. How is `ChordTemporalContext` populated?
   - Where is it constructed relative to scoring?
   - Which fields are populated from neighbouring regions?
   - What is the look-ahead/look-back distance currently (in regions)?

6. How are scored regions serialised to JSON?
   - What fields are written per region (winner + alternatives)?
   - Confirm `rootPitchClass`, `bassPitchClass`, `quality`, `bassIsRoot` are present
     on both winner and alternatives (Iter 36 fix, commit 5df8421114).

---

## Step 2 — Map the same pipeline in notationcomposingbridgehelpers.cpp

Read `src/notation/internal/notationcomposingbridgehelpers.cpp`. Answer the same
questions as Step 1 (questions 1–5 only — no JSON serialisation in this path).

Note any divergences from batch_analyze.cpp beyond the §2.10 boundary detection
duplication: are scoring, temporal context, or region structures also duplicated
or have they already converged?

---

## Step 3 — Characterise the region data structure

From Steps 1 and 2, produce a single unified description of the region data
structure used in each path. Include:
- Field name, type, description
- Whether it is set before scoring, during scoring, or after scoring
- Whether it differs between the two paths

This is the data structure the replacement algorithm must produce as output.

---

## Step 4 — Identify integration seam

The replacement algorithm will slot in where `detectHarmonicBoundariesJaccard`
currently sits. Describe the exact seam:

- Signature of the function to be replaced (inputs → outputs)
- What the caller expects to receive (region list with which fields pre-populated)
- What the replacement must produce to leave all downstream code unchanged

If the downstream code makes assumptions about region ordering, region count,
or region granularity that the replacement algorithm must respect, note them.

---

## Step 5 — Identify what needs to change for greedy-expand

The replacement algorithm requires:

**Per-region metadata not currently present:**
- `round` (integer): which iteration placed this region
- `confidence` (float): placement confidence score
- `reason` (string): human-readable explanation of why this chord was placed

**Adaptive look-ahead:**
- Current look-ahead is N regions. The replacement needs to walk outward to the
  nearest high-confidence anchor. Does ChordTemporalContext need new fields, or
  can the existing fields be populated differently?

**Iteration state:**
- The algorithm needs to store partial placements between rounds and detect
  convergence. Is there an existing data structure that could hold this, or
  does a new one need to be designed?

For each item: is it additive (new field alongside existing ones) or does it
require restructuring existing types?

---

## Step 6 — Report to Cowork

```
Step 1 — batch_analyze.cpp pipeline:
  Boundary detection called at: line N, function [name]
  Inputs: [describe]
  Region data structure fields: [list]
  Regions passed to scorer at: line N, function [name]
  ChordTemporalContext populated at: line N
  Current look-ahead: N regions
  JSON serialisation: winner fields=[list], alt fields=[list]

Step 2 — notationcomposingbridgehelpers.cpp pipeline:
  [same structure]
  Divergences from batch_analyze.cpp: [list or "none beyond §2.10"]

Step 3 — Unified region data structure:
  [table: field | type | set when | same in both paths?]

Step 4 — Integration seam:
  Function signature: [inputs → outputs]
  Caller assumptions: [list]
  Replacement must produce: [describe]

Step 5 — What needs to change:
  round/confidence/reason fields: [additive / requires restructure]
  Adaptive look-ahead: [new ChordTemporalContext fields needed / existing fields sufficient]
  Iteration state: [existing structure usable / new type needed]
  Estimated new types or changed signatures: [list]
```
