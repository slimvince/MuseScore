# Iteration 49: Close iteration path 1 — documentation and Git wrap-up

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Confirmed baselines: BIR=true=21, BIR=false=128. Jazz BIR=false=20.

Do NOT change any source code. Documentation and Git only.

---

## Context

The current incremental gate/scoring iteration path has reached its natural end:
- All actionable genuine error clusters have been investigated
- Remaining genuine-21 residual is fully characterised and blocked with the current architecture
- Boundary detection algorithm confirmed at its parameter optimum; deprecated in favour of Task #62
- Baseline is clean and reproducible from committed code as of 5df8421114

This iteration documents the state of the project, writes a closing summary, and tags the closing commit.

---

## Step 1 — Update ARCHITECTURE.md

Read the current ARCHITECTURE.md first. Then update or add the following sections:

**Final BIR baselines (iteration path 1 close):**
- BIR=true: 21 (three-way genuine errors, bassIsRoot=true)
- BIR=false: 128 (three-way genuine errors, bassIsRoot=false)
- Jazz BIR=false: 20
- Corpus: 353 Bach chorales, Baroque preset

**Active gates — list each with:**
- Gate name and iteration introduced
- Condition (structural fields only — no symbol strings)
- Effect on BIR at introduction

Gates to document (read chordanalyzer.cpp to confirm exact conditions):
G-E, H, I, K, L — and any others present in the gate block.

**Scoring architecture — Iter 46 extension:**
Document the extension of `supportsContextualInversionBonuses` and
`qualifiesForCompleteTriadInversionBonus` to include Augmented and HalfDiminished
(chordanalyzer.cpp, committed 36bf4738a8). Effect: BIR=true 32→21, BIR=false 177→128.

**Deprecated algorithm:**
`detectHarmonicBoundariesJaccard` is deprecated. Document:
- Why: fixed quarter-note window (wrong for non-4/4), Jaccard measures pitch-class
  overlap not harmonic function, running accumulation suppresses boundaries,
  single-pass with no revision. Parameter tuning confirmed exhausted (Iter 48/48b/48c).
- Replacement: Task #62 — iterative greedy-expand algorithm with preset-controlled
  stopping threshold. Both implementations (notationcomposingbridgehelpers.cpp and
  batch_analyze.cpp) to be replaced. §2.10 TODO remains open (Task #58).

**Genuine-21 residual — what remains and why it is not further reducible:**

Gate M cluster (7 cases):
  Winner=Minor, correct=Diminished or HalfDiminished. Gate requires precise
  temporal separator between root-position Minor and the correct alternative.
  Diagnosed in Iter 47: no reliable temporal signal separates genuine from FP
  at viable thresholds. Blocked with current architecture.

Cluster A (7 cases):
  Winner=Minor6 (root-position), correct=HalfDiminished 1st inversion (same bass).
  5/7 cases: correct alternative absent from results[] even after Iter 46 scoring
  extension — candidate-generation gap. 2/7: FP rate 9:2 at all viable thresholds.
  Blocked with current architecture.

Power/Suspended cluster (4 cases):
  Not fully diagnosed. Deferred — will be encountered naturally during
  calibration of the replacement algorithm (Task #62).

Edge cases (2–3 cases):
  Individually examined; no common pattern; no viable gate found.

**Pending tasks:**
- Task #36: Move gate thresholds into ChordAnalyzerPreferences
- Task #50: Build verified BWV→DCML MSCX mapping registry
- Task #58: Consolidate duplicate detectHarmonicBoundariesJaccard implementations
- Task #62: Design and implement replacement segmentation algorithm (next major initiative)
- Task #63: This task (in progress)

---

## Step 2 — Write closing summary document

Create `docs/iteration_path1_summary.md` with:

```
# Iteration Path 1 — Closing Summary

## Scope
Incremental improvement of the chord analyser in src/composing/ via diagnostic
iterations, gate additions, and scoring architecture changes. Approximately 49
iterations from initial audit through baseline restoration.

## Total error reduction
BIR=true:  [starting value] → 21   (Δ = N)
BIR=false: [starting value] → 128  (Δ = N)
Jazz BIR=false: 20

[Read tools/analyze_inversion_errors.py and git log to find the earliest
recorded BIR values to fill in starting values.]

## Key milestones
[List the 5–6 most impactful changes with iteration number, commit hash,
and BIR delta. Candidates: Gate G-E rawCandidates fallback, Gate I,
Gate K, Gate L, Iter 46 scoring extension, Iter 36 batch_analyze fix.]

## Architecture decisions made during this path
1. Scoring: supportsContextualInversionBonuses extended to Augmented and
   HalfDiminished (Iter 46, 36bf4738a8) — single largest improvement.
2. Boundary detection: detectHarmonicBoundariesJaccard deprecated (Task #62).
   Replacement: iterative greedy-expand with preset-controlled stopping threshold.
   See ARCHITECTURE.md §boundary-detection for full design.
3. batch_analyze.cpp must emit structured alternative fields (rootPitchClass,
   bassPitchClass, quality, bassIsRoot) for compare_analyses.py reclassification
   to function. Committed in Iter 36 (recovered in 5df8421114).

## Genuine-21 residual
[Summarise from Step 1 above — Gate M blocked, Cluster A blocked,
Power/Suspended deferred, edge cases no pattern.]

## Process lessons
- Always build fresh before measuring. Verify binary timestamp > source timestamp.
- Commit all changes that affect BIR metrics immediately — never leave
  pipeline-affecting changes in the working tree uncommitted.
- The §2.10 duplication (two implementations of the same algorithm) is a
  persistent source of divergence risk. Consolidation (Task #58) is a
  prerequisite for Task #62.
```

---

## Step 3 — Verify build_and_test.md

Confirm build_and_test.md reflects:
- BIR=true=21, BIR=false=128 as current Baroque baselines
- Jazz BIR=false=20
- Both commits (36bf4738a8 Iter 46, 5df8421114 Iter 36 recovery) noted

---

## Step 4 — Git tag

```
git tag iter-path1-final 5df8421114 -m "Iteration path 1 complete: BIR=true=21 BIR=false=128 Jazz=20"
git push origin iter-path1-final   # if remote exists
```

---

## Step 5 — Run both test suites to confirm clean state

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 and 53/53.

---

## Step 6 — Report to Cowork

```
ARCHITECTURE.md: updated [yes/no]
  Gates documented: [list]
  Iter 46 extension documented: [yes/no]
  Deprecated algorithm documented: [yes/no]
  Genuine-21 residual documented: [yes/no]

docs/iteration_path1_summary.md: created [yes/no]
  Starting BIR values found: BIR=true=[N] BIR=false=[N]
  Total reduction: BIR=true Δ=[N] BIR=false Δ=[N]
  Key milestones listed: [N]

build_and_test.md: verified [yes/no]

Git tag: iter-path1-final → [hash]

Tests: composing=[N]/407  notation=[N]/53

Committed: [yes — hash] / [no — reason]
```
