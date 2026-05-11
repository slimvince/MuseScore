# Iteration 31: Re-characterize remaining BIR=true=52 cases

## Goal

Re-run the Iter 19 categorization script on the updated corpus (post-Iter 30
baseline: BIR=true=52, BIR=false=787). Get fresh category counts and full
per-case lists to identify the next target.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — confirm baselines: BIR=true=52, BIR=false=787

---

## Step 2 — Confirm corpus is current

Check that corpus JSONs reflect the Iter 30 binary (Gate I + Gate K). If any
doubt, re-run:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Confirm BIR=true=52, BIR=false=787.

---

## Step 3 — Run the categorization script

```
cd C:\s\MS && python tools/analyze_bir_true_iter19.py
```

Capture and report the complete output verbatim.

---

## Step 4 — Print full per-case lists

Confirm the script already prints all cases in Cat 1 and Cat 2. If not, add
print blocks. Each case line format:

```
[CAT1] file=bwvXX  m=N  beat=X  winner=SYMBOL  alt=SYMBOL  margin=+X.XX  key=KEY
[CAT2] file=bwvXX  m=N  beat=X  winner=SYMBOL  alt=SYMBOL  margin=+X.XX  key=KEY
```

Re-run and capture all case lines.

---

## Step 5 — Cat 2 quality-pair breakdown

For Cat 2, group by `winner_quality × alt_quality` pair, sorted by count desc:

```
(MajorQuality→MinorQuality)=N  ...
```

---

## Step 6 — Report to Cowork

Provide:
1. Complete Step 3 output verbatim.
2. Complete per-case lists from Step 4.
3. Cat 2 quality-pair breakdown from Step 5.
4. A brief interpretation:
   - What are the two largest remaining categories?
   - What is the dominant Cat 2 sub-pattern?
   - Which known-deferred cases are still present (Gate J targets, Augmented
     rooting cases)?
   - Is there a new mechanically clear Cat 2 pattern worth targeting?

Do NOT implement any fix. Do NOT commit.
