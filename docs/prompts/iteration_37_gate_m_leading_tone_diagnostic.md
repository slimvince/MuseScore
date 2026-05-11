# Iteration 37: Gate M — Leading-tone diagnostic

## Standing rule — no symbol inference

**Every script in this iteration must use only structured numeric/enum fields
(rootPc, bassPc, quality, keyTonic, keyMode, score, etc.). No chord symbol
string parsing of any kind. No Roman numeral inference. If a needed field is
absent from the JSON, report that fact and stop — do not substitute symbol
parsing as a fallback.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines (post-Iter 36 corpus regeneration): BIR=true=32, BIR=false=177.

Do NOT modify any source file. Do NOT commit. Diagnostic only.

---

## Background

Iter 36 Step 5 found the condition
  "winner.quality==Minor AND bassIsRoot AND alt.quality∈{Diminished,DiminishedSeventh}
   AND same root AND same bass AND margin ≤ 0.50"
produces 8 genuine hits but 25 false positives — far too broad for a gate.
Score alone cannot separate them: 22/25 FPs are at margin=0.00, and the
non-zero FP at margin=0.377 overlaps the genuine margin range.

Hypothesis: the structural distinguisher is **leading-tone membership**.
In Baroque harmony, a diminished triad on the leading tone (the note a
semitone below the tonic) is a structural norm (vii°) in both major and minor
keys. If winner.rootPitchClass == (keyTonic − 1 + 12) % 12, diminished is
almost always preferred over minor. This condition has a musical basis and
requires only key context fields — no reference annotations.

---

## Step 1 — Inspect key context fields in a sample region

Before writing any scan, confirm which key-related fields actually exist on
winner regions in the current corpus JSONs. Print the full set of fields and
their values for the bwv302 m=1 b=4.0 region (a known genuine case):

```python
import json

data = json.load(open('tools/corpus/bwv302.ours.json'))
for r in data.get('regions', []):
    if r['measureNumber'] == 1 and abs(r['beat'] - 4.0) < 0.15:
        print("All winner region fields and values:")
        for k, v in r.items():
            if k != 'alternatives':
                print(f"  {k}: {repr(v)}")
        break
```

Report:
- Is there a key tonic field? Give its exact name and value type (int 0–11?
  or string?).
- Is there a key mode field (major/minor)? Give its exact name and value.
- Any other key-related fields (scale degrees, diatonic set, etc.)?

Do NOT proceed to Step 2 until this is answered.

---

## Step 2 — Leading-tone diagnostic scan

Using the exact field names confirmed in Step 1, run the following diagnostic
over all 33 known regions (8 genuine + 25 FP from Iter 36). For each region:
- Compute `leading_tone_pc = (keyTonic - 1 + 12) % 12`
- Check `is_leading_tone = (winner.rootPitchClass == leading_tone_pc)`
- Report result

If the key tonic field is a string or needs conversion, apply the conversion
using a hardcoded lookup table (no symbol parsing of chord symbols — key
names are a separate category, but prefer int fields if available).

Use this exact target list (file stems, measure, beat):

```python
GENUINE = [
    # (file_stem, measure, beat)
    ('bwv187.7',  14, 2.0),
    ('bwv227.11', 10, 3.0),
    ('bwv278',     8, 2.0),
    ('bwv301',     2, 3.0),
    ('bwv302',     1, 4.0),
    ('bwv40.6',   14, 2.0),
    ('bwv423',     9, 2.0),
    ('bwv85.6',    5, 1.0),
]

FALSE_POSITIVES = [
    ('bwv145.5',  10, 1.0),
    ('bwv227.1',  16, 3.0),
    ('bwv227.7',   1, 4.0),
    ('bwv244.15',  9, 3.0),
    ('bwv257',     1, 1.0),
    ('bwv26.6',    3, 4.0),
    ('bwv274',     2, 4.5),
    ('bwv278',     8, 1.0),
    ('bwv310',     2, 4.0),
    ('bwv313',     8, 3.0),
    ('bwv322',    13, 1.0),
    ('bwv335',     7, 4.0),
    ('bwv337',     5, 1.0),
    ('bwv342',    13, 2.0),
    ('bwv362',     5, 2.0),
    ('bwv371',    19, 1.0),
    ('bwv404',     1, 2.0),
    ('bwv407',    14, 2.0),
    ('bwv62.6',    1, 4.5),
    ('bwv72.6',    3, 4.0),
    ('bwv72.6',    8, 4.0),
    ('bwv74.8',    1, 4.0),
    ('bwv83.5',   11, 2.0),
    ('bwv9.7',     7, 2.0),
    ('bwv9.7',     9, 2.0),
]
```

For each region, print one line:
```
[GENUINE|FP]  file=bwvXX  m=N  b=X  rootPc=N  keyTonic=N  keyMode=STR  leadingTonePc=N  is_leading_tone=True/False  margin=+X.XXX
```

If a region's JSON file is missing or the region cannot be located by
(measureNumber, beat), report that and skip — do not substitute.

---

## Step 3 — Summary and second signal

After printing all 33 lines, report:

A. Leading-tone hit rate:
   - Genuine cases where is_leading_tone=True: N / 8
   - FP cases where is_leading_tone=True: N / 25

B. If is_leading_tone cleanly separates (all 8 genuine are True AND ≤ 2 FP
   are True): report as CLEAN SEPARATION.

C. If leading-tone alone is insufficient, also report for each case:
   - keyMode (major vs minor)
   - Whether the combination (is_leading_tone=True AND keyMode=="minor")
     further separates genuine from FP — give counts for all four quadrants:
     (True/minor, True/major, False/minor, False/major) for genuine and FP
     separately.

D. Report any other structural pattern visible in the data (e.g. beat position,
   measure number, consistent key root across FPs, etc.). Use only fields
   present in the JSON.

---

## Step 4 — Report to Cowork

```
Step 1 — Key context fields:
  Key tonic field: [name] type=[int/string] example value=[X]
  Key mode field:  [name] type=[string] example value=[X]
  Other key fields: [list or "none"]

Step 2 — Leading-tone results (all 33 lines verbatim):
  [paste output]

Step 3 — Summary:
  Genuine is_leading_tone=True: N / 8
  FP      is_leading_tone=True: N / 25
  Separation quality: [CLEAN / PARTIAL / NONE]

  If partial:
    (leading_tone AND minor key) quadrant counts:
      Genuine: TT=N TF=N FT=N FF=N
      FP:      TT=N TF=N FT=N FF=N
  Other structural patterns: [describe or "none observed"]
```

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.
