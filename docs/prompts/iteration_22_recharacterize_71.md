# Iteration 22: Re-characterize remaining BIR=true=71 cases

## Goal

Re-run the Iter 19 categorization script on the updated corpus (post-Iter 21
baseline: BIR=true=71, BIR=false=788). The category distribution has changed
now that 27 Cat 2 Minor→HalfDim cases were fixed. Identify the new dominant
pattern(s) for Cowork to target next.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — confirm baselines: BIR=true=71, BIR=false=788

---

## Step 2 — Confirm corpus is current

The corpus JSON files in `tools/corpus/` must reflect the Iter 21 analyzer.
If `run_bach_preset.py` was already run as part of Iter 21 Step 5, the files
are current. Confirm by checking the modification timestamp of a few
`*.ours.json` files. If they predate the Iter 21 build, re-run:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 3 — Run the categorization script

```
cd C:\s\MS && python tools/analyze_bir_true_iter19.py
```

This produces:
- The four-category summary table (Cat 1–4 counts and percentages)
- The `[CAT2-MHD]` and `[CAT1-CLN]` case lists appended at the end

Capture the **complete output** verbatim.

---

## Step 4 — Produce extended case lists for the two largest categories

Identify the two largest categories (by count) in the new output. For each,
print ALL cases explicitly (file, measure, beat, winner symbol, alt symbol,
margin, key) — not just the top 5 examples. Use the existing `[CAT2-MHD]` /
`[CAT1-CLN]` logic as a model; add analogous per-case print blocks for
whatever the new dominant categories are.

If Cat 2 Minor→HalfDim is still present (the 3 WRONG-PC cases), print those
explicitly too.

Re-run the script after adding the new print blocks and capture all case lines.

---

## Step 5 — Report to Cowork

Provide:

1. The complete Step 3 output verbatim.
2. The complete per-case lists from Step 4 verbatim.
3. A 5-line interpretation:
   - What are the two largest remaining categories?
   - Does any sub-group (winner quality × alt quality pair) clearly dominate?
   - Are the margins tight (fixable by gate) or wide (scoring issue)?
   - What is the most promising single target for Iteration 23?

Do NOT implement any fix. Do NOT commit script changes.
