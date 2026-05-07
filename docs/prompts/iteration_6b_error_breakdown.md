# Iteration 6b: Fresh breakdown of the 111 remaining BIR=true errors

## ⚠ Critical behaviour rules for this session

- **Read-only investigation. Zero code changes. Zero commits.**
- Write and run a Python script inline (do not save to the repo).
- Think carefully and report findings in full detail.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — current baselines only (BIR=true=111, BIR=false=788)

---

## Step 2 — Run the breakdown

The corpus JSONs in `tools/corpus/` are fresh (generated at commit 89ad75d7d1).
Do NOT regenerate them — use them as-is.

Write and run a Python script that reads all corpus JSON files and, for each
genuine BIR=true error region, collects:

1. `winnerRootPc` and `winnerQuality` (the chord the analyzer output)
2. `winnerChordSymbol` (for human-readable examples)
3. `altRootPc` (the reference root)
4. `altChordSymbol` (reference symbol if available)
5. Whether it is an **enharmonic pair**: `altRootPc == (winnerRootPc + 9) % 12`
6. If enharmonic pair: winner quality bucket — MinorAdd6, MajorAdd6, or Other
7. If NOT enharmonic pair: the interval `(altRootPc - winnerRootPc) % 12`
8. `bassIsStepwiseFromPrevious` and `bassIsStepwiseToNext` from `temporalExtensions`
9. Score margin (`winner.score - bestAlt.score`) if present in the JSON

Then report:

**A. Top-level split:**
- Total genuine BIR=true errors: N (confirm = 111)
- Enharmonic pairs (altRoot == (winnerRoot + 9) % 12): N
- Non-enharmonic pairs: N

**B. Enharmonic-pair breakdown (N errors):**
- Winner = Minor + AddedSixth (Gate G-B/C/D target): N
- Winner = Major + AddedSixth (Gate A / Gate B/C/D target): N
- Winner = other quality: N (list qualities)
- Of MinorAdd6 subset: how many have `bassIsStepwiseFromPrevious=true`?
- Of MinorAdd6 subset: how many have `bassIsStepwiseToNext=true`?
- Score margin distribution for MinorAdd6 subset: min, max, median

**C. Non-enharmonic-pair breakdown (N errors):**
- Group by interval `(altRootPc - winnerRootPc) % 12`:
  - interval 8 (+8 semitones from winner to alt = winner is major 3rd of alt = first inversion, Gate E target): N
  - interval 5 (+5 semitones = winner is 5th of alt = second inversion, Gate F target): N
  - other intervals: list with counts
- For each interval group: what winner quality and alt quality appear most often?
- Are there patterns suggesting a fixable class (e.g. all Minor winners, all Major alts)?

**D. Temporal evidence summary across all 111 errors:**
- How many have `bassIsStepwiseFromPrevious=true`?
- How many have `bassIsStepwiseToNext=true`?
- How many have EITHER stepwise signal?
- Of those with a stepwise signal: what fraction are enharmonic-pair errors?

---

## Step 3 — Report

```
Total genuine BIR=true errors:     N (confirm = 111)

A. Top-level:
  Enharmonic pairs (+9 mod 12):   N / 111
  Non-enharmonic pairs:           N / 111

B. Enharmonic-pair subset (N):
  MinorAdd6 winners:              N  (Gate G-B/C/D target in bridge path)
  MajorAdd6 winners:              N  (Gate A/B/C/D target)
  Other quality winners:          N  (list)
  MinorAdd6 → stepwiseFromPrev:  N
  MinorAdd6 → stepwiseToNext:    N
  MinorAdd6 score margin:        min=N, max=N, median=N

C. Non-enharmonic subset (N):
  Interval +8 (first inversion):  N  winner quality: X, alt quality: Y
  Interval +5 (second inversion): N  winner quality: X, alt quality: Y
  Other intervals:                N  breakdown: <table>
  Most common non-enharmonic pattern: <describe>

D. Temporal evidence (all 111):
  bassIsStepwiseFromPrevious=true: N
  bassIsStepwiseToNext=true:       N
  Either stepwise:                 N
  Stepwise AND enharmonic pair:    N

Unexpected findings: none / <describe>
```
