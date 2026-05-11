# Iteration 38: Gate M deferral, genuine-32 re-characterization, near_agree audit

## Standing rule — no symbol inference

**Every script in this iteration must use only structured numeric/enum fields
(rootPc, bassPc, quality, score, etc.). No chord symbol string parsing of any
kind. No Roman numeral inference. If a needed field is absent from the JSON,
report that fact and stop — do not substitute symbol parsing as a fallback.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines (post-Iter 36 corpus regeneration): BIR=true=32, BIR=false=177.

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.

---

## Background

Iter 37 definitively ruled out Gate M (Minor→Diminished TYPE-A). No combination
of available runtime-accessible JSON fields separates the 8 genuine cases from
25 FPs. The genuine and FP cases within both structural subgroups are
indistinguishable without DCML harmonic context, which is not available at
runtime.

Separately, the Iter 36 corpus regeneration changed baselines from 48/787 to
32/177 by activating `_matches_alternative()` in `compare_analyses.py`. The 16
BIR=true cases that moved from `chord_disagree` to `near_agree` are regions
where our system already ranks the correct chord as alternative[1] — our scorer
finds it, just doesn't promote it to winner. These are prime gate candidates.

This iteration has three goals:
1. Document Gate M deferral in the appropriate project files.
2. Re-characterize the genuine-32 set (fresh category counts under new baselines).
3. Enumerate and characterize the 16 near_agree BIR=true cases as potential
   gate targets.

---

## Step 1 — Document Gate M deferral

Check whether a deferred-gate record exists anywhere in the project
(STATUS.md, ARCHITECTURE.md, build_and_test.md, or similar). Then add a
Gate M entry in the appropriate place using this content:

```
Gate M — Minor→Diminished TYPE-A (deferred, Iter 37, 2026-05-09)
  Genuine cases:  8  (Minor root-pos winner, Diminished alt at same root)
  FP count:      25  (using any available JSON structural fields)
  Reason: The 8 genuine cases split into two structural subgroups, each
  sharing an identical structural profile with a large FP cluster.
  GROUP A (4 cases, margin 0.29–0.44, minor keys, P5 in pitch set): one FP
  (bwv227.1) is structurally identical to genuine bwv227.11 — same chorale,
  key, pitch class set, margin.
  GROUP B (4 cases, margin=0.00, 3-note chord, no P5/d5): 22 FPs share the
  same profile.
  No JSON field or combination (rootPc, keyTonic, keyMode, margin, noteCount,
  pitchClassSet, beat, bassIsRoot) cleanly separates genuine from FP.
  Leading-tone hypothesis tested and falsified (0/8 genuine match).
  Requires DCML harmonic function context not available at runtime.
  Do not attempt again without a new runtime signal source.
```

---

## Step 2 — Confirm corpus and script state

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=32, BIR=false=177. If different, stop and report.

---

## Step 3 — Re-characterize genuine-32

Run the categorization script (already patched in Iter 34 to always output
genuine three-way cases):

```
cd C:\s\MS && python tools/analyze_bir_true_iter19.py
```

Capture the complete output verbatim. Report:
- Total genuine three-way cases (should be 32)
- Cat 1 / Cat 2 / Cat 3 / Cat 4 counts and all per-case lines
- Cat 2 quality-pair breakdown: `(winner_quality → alt_quality) = N`  sorted
  by count descending
- Any known-deferred patterns still present (Gate J: Major→Minor I3,
  MinMaj7 cluster, Minor→Diminished)

---

## Step 4 — Enumerate near_agree BIR=true cases

The 16 near_agree cases are regions where:
- Our winner has bassIsRoot=true
- `_matches_alternative()` in `compare_analyses.py` matched one of our
  alternatives to music21's root_pc AND quality
- These were previously counted as chord_disagree (BIR=true errors) but are
  now classified as near_agree

First, read `tools/compare_analyses.py` and find:
- Exactly where `_matches_alternative()` is defined and what it returns
- Where near_agree cases are accumulated during the comparison pass
- Whether the comparison pass stores the matched alternative's index,
  quality, and rootPc anywhere

Then write a script that enumerates all BIR=true near_agree cases across the
Baroque corpus. For each:
- File name (bwv stem)
- Measure number, beat
- Winner: quality, rootPitchClass, bassPitchClass, score
- Matched alternative: quality, rootPitchClass, bassPitchClass, score
- Margin (winner.score − alt.score)

The script may need to replicate the comparison pass logic to identify which
alternative matched. Use only structured fields (rootPitchClass, quality from
the JSON). Do NOT parse chordSymbol or romanNumeral.

If `compare_analyses.py` does not store enough intermediate state to recover
the matched alternative details, report what IS available and what would need
to change to surface this data.

---

## Step 5 — Characterize near_agree patterns

From the Step 4 enumeration, produce:

A. Quality-pair breakdown:
   `(winner_quality → matched_alt_quality) = N`  sorted by count descending

B. Margin distribution: how many cases at margin=0.00, margin ≤ 0.20,
   margin ≤ 0.35, margin ≤ 0.50?

C. Are any near_agree quality pairs the same as patterns already covered by
   an existing gate? If so, note which gate and whether these were supposed
   to be fixed.

D. Which quality pair (if any) appears most promising as a gate candidate
   (high case count, clean structural condition, not previously attempted)?
   Report the count and a brief structural description — do not propose
   implementation yet.

---

## Step 6 — Report to Cowork

```
Step 1 — Gate M deferral:
  Documented in: [file name and section]

Step 2 — Baseline confirmation:
  BIR=true=N  BIR=false=N

Step 3 — Genuine-32 categorization:
  [Complete script output verbatim]
  Cat 1: N  Cat 2: N  Cat 3: N  Cat 4: N
  Cat 2 quality pairs (sorted): [list]
  Known-deferred patterns present: [list]

Step 4 — near_agree enumeration:
  Total near_agree BIR=true cases found: N
  [Full list: file, m, beat, winner_q, winner_rootPc, alt_q, alt_rootPc, margin]
  [Or: what data was unavailable and why]

Step 5 — near_agree patterns:
  Quality pairs: [list sorted by count]
  Margin distribution: [counts at each threshold]
  Overlap with existing gates: [yes/no/which]
  Most promising candidate: (WQ→AQ)=N — [brief structural description]
```
