# Iteration 26: Re-characterize remaining BIR=true=53 cases

## Goal

Re-run the Iter 19 categorization script on the updated corpus (post-Iter 25
baseline: BIR=true=53, BIR=false=787). Get fresh category counts and full
per-case lists for both Cat 1 and Cat 2 so Cowork can identify the next target.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — confirm baselines: BIR=true=53, BIR=false=787

---

## Step 2 — Confirm corpus is current

The corpus JSON files should already reflect the Iter 25 analyzer (run during
that iteration's Step 5). Confirm by checking a timestamp on any `.ours.json`
file. If they predate the Iter 25 build, re-run:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 3 — Run the categorization script

```
cd C:\s\MS && python tools/analyze_bir_true_iter19.py
```

Capture the complete output verbatim.

---

## Step 4 — Print full per-case lists for ALL categories

Add (or confirm already present) print blocks for every case in every
non-empty category. Print one line per case in the format:

```
[CAT1] file=bwvXX  m=N  beat=X  winner=SYMBOL  alt=SYMBOL  margin=+X.XX  key=KEY
[CAT2] file=bwvXX  m=N  beat=X  winner=SYMBOL  alt=SYMBOL  margin=+X.XX  key=KEY
```

Re-run the script and capture all case lines.

---

## Step 5 — For Cat 2: report the winner/alt quality pair breakdown

For Cat 2, also group by `winner_quality × alt_quality` pair and sort by
count descending — same format as the Iter 22 report:

```
(Augmented→Major7)=N  (Major→Minor)=N  ...
```

---

## Step 6 — Report to Cowork

Provide:
1. Complete Step 3 output verbatim.
2. Complete per-case lists from Step 4 verbatim.
3. Cat 2 quality-pair breakdown from Step 5.
4. A 4-line interpretation:
   - What are the two largest remaining categories?
   - What is the dominant Cat 2 sub-pattern?
   - Are the remaining Cat 1 cases mostly the 7 I3 (correct chord absent from
     candidates) or are there other fixable patterns?
   - What is the recommended single target for Iteration 27?

Do NOT implement any fix. Do NOT commit script changes.
