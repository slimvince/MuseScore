# Iteration 35: Gate M diagnostic — Minor→Diminished TYPE-A (clean rewrite)

## Standing rule — no symbol inference

**Every script in this iteration must use only structured numeric fields from the
JSON (rootPc, bassPc, quality, score, etc.). No chord symbol string parsing of any
kind. No Roman numeral inference. If a needed field is absent from the JSON, report
that fact and stop — do not substitute symbol parsing as a fallback.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baseline: BIR=true=48, BIR=false=787.

---

## Step 0 — Three-way definition (mandatory — answer before anything else)

Read `tools/analyze_bir_true_iter19.py`. Find the exact logic that classifies a
region as a "genuine three-way error". Report:

1. Which sources are compared? List their exact names as used in the script.
2. Is DCML (human-annotated corpus) **required** to disagree with our output, or
   can the condition fire on algorithmic sources only?
3. Quote the exact boolean condition verbatim (the relevant 3–10 lines of code).

Do not proceed to Step 1 until this is answered.

---

## Step 1 — Inspect raw JSON structure of alternatives

Pick any `.ours.json` file from `tools/corpus/` that has at least 3 alternatives
on some region. Print the raw JSON for that region's `alternatives` array — every
field, exactly as stored. Do not summarise or paraphrase.

Example approach:
```python
import json

data = json.load(open('tools/corpus/bwv302.ours.json'))
for r in data.get('regions', []):
    alts = r.get('alternatives', [])
    if len(alts) >= 3:
        print(f"Region m={r['measureNumber']} b={r['beat']}")
        print(f"Winner fields: {list(r.keys())}")
        print(f"Alt[0] fields: {list(alts[0].keys())}")
        for i, a in enumerate(alts[:4]):
            print(f"  alt[{i}]: {a}")
        break
```

Report:
- Every field name present on a winner region entry
- Every field name present on an alternatives entry
- Specifically: is `quality` present and non-null for alternatives?
- Is `rootPc` or equivalent present for alternatives?
- Is `bassPc` or equivalent present for alternatives?

Do not proceed to Step 2 until this is answered.

---

## Step 2 — False positive risk scan (structured fields only)

Using ONLY the fields confirmed in Step 1, write a scan that finds all Baroque
corpus regions where:
- Winner quality == Minor AND winner bassIsRoot == true
- An alternative exists with quality == Diminished (with or without DiminishedSeventh
  extension — treat both as Diminished family) AND same root as winner AND same bass
  as winner (root-position alt)
- Margin (winner.score − alt.score) ≤ 0.50

If `quality` is null for alternatives, or if root/bass structured fields are absent
from alternatives, **STOP and report which fields are missing**. Do not substitute
symbol parsing.

For each matching region classify as:
- GENUINE: in the genuine-48 list below
- FP (false positive): NOT in genuine-48

Genuine-48 Minor→Dim/Dim7 targets (from Iter 34, trusted):
```python
GENUINE = {
    ('bwv187.7',  14, 2.0),
    ('bwv227.11', 10, 3.0),
    ('bwv278',     8, 2.0),
    ('bwv301',     2, 3.0),
    ('bwv302',     1, 4.0),
    ('bwv40.6',   14, 2.0),
    ('bwv85.6',    5, 1.0),
    ('bwv423',     9, 2.0),
}
```

Report: genuine count, FP count, full list of FP cases (file, measure, beat, margin,
and the raw field values used — no symbols).

**If FP count > 2: STOP. Do not proceed to Jazz scan or implementation.**

If FP count ≤ 2: run the same scan on the Jazz corpus:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
```
Then rerun scan. Report Jazz FP count.
Restore Baroque corpus afterward:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 3 — Tied-score cases (if scan shows FP ≤ 2)

Only reach this step if Step 2 passed. For the 4 genuine Minor→Diminished cases
with margin=0.00 (bwv302, bwv40.6, bwv85.6, bwv423): confirm using raw JSON fields
that winner.score == alt.score exactly, and report how many other regions in the
full Baroque corpus have winner.quality==Minor and an alt with Diminished quality
at exactly the same score and same root. Use structured fields only.

---

## Step 4 — Report to Cowork

```
Step 0 — Three-way definition:
  Sources: [list]
  DCML required: [yes / no]
  Condition (verbatim):
    [quoted code]

Step 1 — JSON structure:
  Winner fields: [list]
  Alt fields: [list]
  quality present and non-null for alts: [yes / no / sometimes]
  rootPc present for alts: [yes / no]
  bassPc present for alts: [yes / no]

Step 2 — False positive scan:
  Fields used: [list — confirm no symbol parsing]
  Baroque: genuine=N  FP=N
  [FP list with raw field values]
  Jazz (if reached): genuine=N  FP=N

Step 3 (if reached):
  Tied-score zero-margin FP count: N
```

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.
