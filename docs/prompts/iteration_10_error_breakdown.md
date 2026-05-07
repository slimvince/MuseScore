# Iteration 10: Fresh breakdown of the 109 remaining BIR=true errors

## ⚠ Critical behaviour rules for this session

- **Read-only investigation. Zero code changes. Zero commits.**
- Write and run Python scripts inline (do not save to repo).
- Think carefully and report findings in full detail.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — current baselines: BIR=true=109, BIR=false=788

---

## Step 2 — Regenerate corpus

The corpus JSONs must reflect the current codebase (Iterations 8, 9A, 9B, 9C all
changed analysis behaviour or the shared helpers). Regenerate before analysing:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Confirm BIR=true=109 and BIR=false=788 after regeneration. If either differs,
STOP and report before proceeding.

---

## Step 3 — Run the breakdown

Write and run a Python script (do not save) that reads all corpus JSON files and,
for each genuine BIR=true error, collects:

1. Score filename and measure number
2. `winnerRootPc`, `winnerQuality`, `winnerChordSymbol`
3. `altRootPc`, `altQuality`, `altChordSymbol`
4. Interval: `(altRootPc - winnerRootPc) % 12`
5. Whether enharmonic pair: interval == 9
6. `bassIsStepwiseFromPrevious`, `bassIsStepwiseToNext` (from temporalExtensions if present, else mark as unavailable)
7. Score margin (winner.score − alt.score) if present

Then report:

---

### A. Top-level split

- Total genuine BIR=true errors: N (confirm = 109)
- Enharmonic pairs (interval = 9): N
- Non-enharmonic: N

---

### B. Enharmonic-pair breakdown

For each enharmonic-pair error:
- Winner quality bucket: MinorAdd6, MajorAdd6, Augmented, or Other
- Count per bucket

For the **Augmented** subset (Gate H target):
- How many? (was 9 in Iteration 6b)
- Has this count changed? Gate H now has full temporal context in batch (after Iter 8).
  If the count dropped: Gate H is now firing on some. If unchanged: Gate H is still
  not firing (perhaps no temporal evidence in those specific passages).
- For each remaining augmented error: report the score/measure so we can inspect manually.

For the **MinorAdd6** subset (Gate G-B/C/D target):
- How many remain? (was 48 in Iteration 6b)
- Has this count changed?

For the **MajorAdd6** subset (Gate A/B/C/D target):
- How many remain? (should be 0 — Gate A fixed 2 in Iter 7B)

---

### C. Non-enharmonic breakdown

Group by interval `(altRootPc - winnerRootPc) % 12`:

For each interval group, report:
- Count
- Most common winner quality and alt quality
- Example: score/measure, winner symbol, alt symbol
- Is this a known gate target (interval 8 = Gate E, interval 5 = Gate F)?

Identify any interval group with ≥ 5 errors where:
- The pattern is consistent (same winner/alt quality combination)
- No existing gate addresses it

---

### D. Score margin distribution

For ALL 109 errors:
- What fraction have narrow margin (winner.score − alt.score < 0.3)?
- What fraction have wide margin (> 0.5)?
- Does margin correlate with quality/interval group?

---

### E. Temporal signal availability

If `bassIsStepwiseFromPrevious` / `bassIsStepwiseToNext` are present in the corpus JSON:
- For each error class: how many have sf=true? st=true?
- Which classes have temporal evidence that a gate COULD use?

If these fields are NOT in the corpus JSON: note this as a limitation.

---

## Step 4 — Report

```
Corpus regenerated:        BIR=true=N, BIR=false=N

A. Top-level:
  Total genuine BIR=true:  N (confirm = 109)
  Enharmonic pairs (+9):   N
  Non-enharmonic:          N

B. Enharmonic-pair subset (N errors):
  MinorAdd6:               N (was 48 — change: N)
  MajorAdd6:               N (was 2 — expect 0)
  Augmented:               N (was 9 — change: N)
    Gate H now firing?     yes (N fixed) / no (0 fixed)
    Remaining aug errors:  <score/measure list>
  Other quality:           N (list qualities)

C. Non-enharmonic subset (N errors):
  Interval +8:             N — winner: X, alt: Y
  Interval +5:             N — winner: X, alt: Y
  Other intervals:         <table with counts, winner/alt qualities, examples>
  Most actionable class:   <describe — largest group with consistent pattern>

D. Score margin:
  Narrow (< 0.3):          N (N%)
  Medium (0.3–0.5):        N (N%)
  Wide (> 0.5):            N (N%)
  Correlation with class:  <describe if any>

E. Temporal signals (if available):
  sf=true:                 N / unavailable
  st=true:                 N / unavailable
  Class with most signal:  <describe>

Most actionable finding:   <which class is the best candidate for the next gate?>
Unexpected findings:       none / <describe>
```
