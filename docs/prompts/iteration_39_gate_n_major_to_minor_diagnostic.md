# Iteration 39: Gate N diagnostic — Major root-pos → Minor first-inversion

## Standing rule — no symbol inference

**Every script in this iteration must use only structured numeric/enum fields
(rootPc, bassPc, quality, score, bassIsRoot, etc.). No chord symbol string
parsing of any kind. No Roman numeral inference. If a needed field is absent
from the JSON, report that fact and stop — do not substitute symbol parsing.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=32, BIR=false=177.

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.

---

## Background

Iter 38 identified the dominant near_agree pattern: `(Major→Minor) = 8`
DCML-confirmed cases where our winner is Major root-position but the correct
answer is Minor first-inversion at the same bass (alt.rootPc == (bassPc−3)%12).
This is the structural complement to Gate I (which promotes Major over Minor).

Two of the 8 cases have negative margins (winner.score − alt.score < 0):
- bwv245.14  m=13 b=2.0  margin=−0.310
- bwv335     m=6  b=3.0  margin=−0.950

A negative margin means the Minor alt already scores HIGHER than the Major
winner in raw terms, yet the Major chord is still returned as winner. Something
is actively promoting the Major chord above a higher-scoring alternative. The
most likely cause: Gate I is misfiring — it sees a Minor winner, finds a
Major alt, and swaps them, producing a Major winner with a lower raw score.
If so, these are Gate I false positives, not Gate N targets.

This must be investigated before designing Gate N.

---

## Step 0 — Inspect the two negative-margin anomalies

For each of the two cases below, read the corpus JSON and print:
1. All winner region fields (excluding alternatives)
2. All alternative entries in full (using the new rootPitchClass, bassPitchClass,
   quality, bassIsRoot fields added in Iter 36)

```python
import json

TARGETS = [
    ('tools/corpus/bwv245.14.ours.json', 13, 2.0),
    ('tools/corpus/bwv335.ours.json',     6, 3.0),
]

for fpath, meas, beat in TARGETS:
    data = json.load(open(fpath))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            print(f"\n=== {fpath} m={meas} b={beat} ===")
            print("Winner fields:")
            for k, v in r.items():
                if k != 'alternatives':
                    print(f"  {k}: {repr(v)}")
            print("Alternatives:")
            for i, a in enumerate(r.get('alternatives', [])):
                print(f"  alt[{i}]: {a}")
            break
```

Then read `src/composing/chordanalyzer.cpp` and find Gate I (the gate that
promotes Major over Minor-first-inversion). Report:
- The exact entry condition for Gate I (what triggers it)
- Whether Gate I could have fired on these two regions given their winner
  and alt data, and if so, which direction it swapped

Answer this question explicitly:
**Was Gate I the mechanism that promoted Major to winner in these two cases,
overriding a higher-scoring Minor alt?**

If yes: note that these two cases are Gate I false positives. They should NOT
be included in the Gate N target list — Gate N must not fight Gate I on the
same regions. Also note: Gate I may need a tighter entry condition to avoid
these swaps.

If no: report what mechanism IS responsible.

Do NOT proceed to Step 1 until Step 0 is answered.

---

## Step 1 — False positive scan (structured fields only)

After Step 0, run the following scan across the full Baroque corpus. For each
region where:
- `winner.quality == "Major"` AND `winner.bassIsRoot == true`
- An alternative exists with `alt.quality == "Minor"` AND
  `alt.bassPitchClass == winner.bassPitchClass` AND
  `alt.rootPitchClass == (winner.bassPitchClass - 3 + 12) % 12`
- `margin (winner.score − alt.score) ≤ 0.45`

classify as:
- GENUINE: in the genuine-6 list below (excludes the two negative-margin cases
  which are Gate I FP territory, not Gate N targets)
- FP (false positive): NOT in genuine-6

```python
# Genuine Gate N targets (negative-margin anomalies excluded):
GENUINE = {
    ('bwv123.6',  7,  2.0),
    ('bwv322',    1,  3.0),
    ('bwv337',    1,  2.0),
    ('bwv392',   11,  4.0),
    ('bwv417',    3,  2.0),
    ('bwv425',   22,  3.0),
}
```

Use only the structured fields confirmed present in the corpus JSONs:
`quality`, `bassIsRoot`, `bassPitchClass`, `rootPitchClass`, `chordScore` (winner),
`score` (alternative). Do NOT parse chordSymbol or romanNumeral.

Report: genuine count found, FP count, full FP list (file, measure, beat,
margin, winner.quality, winner.rootPitchClass, winner.bassPitchClass,
alt.quality, alt.rootPitchClass, alt.bassPitchClass — raw values).

**If FP count > 2: STOP. Do not proceed to Jazz scan.**

---

## Step 2 — Jazz scan (only if Baroque FP count ≤ 2)

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
```

Re-run the same scan. Report Jazz FP count and list.

Restore Baroque corpus afterward:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 3 — Report to Cowork

```
Step 0 — Negative-margin anomaly investigation:
  bwv245.14 m=13 b=2.0:
    Winner: quality=X rootPc=N bassPc=N score=X.XXX
    Alt[0]: quality=X rootPc=N bassPc=N score=X.XXX
    Alt[1]: quality=X rootPc=N bassPc=N score=X.XXX
    Gate I condition check: [fired / did not fire / unclear]
    Mechanism promoting Major to winner: [Gate I / other / unknown]

  bwv335 m=6 b=3.0:
    [same format]

  Conclusion: [Gate I FP / other cause]
  Gate I false positives confirmed: [yes / no / partial]

Step 1 — Baroque false positive scan:
  Fields used: [confirm no symbol parsing]
  Genuine found: N / 6
  FP count: N
  [FP list with raw field values]

Step 2 — Jazz scan (if reached):
  Jazz FP count: N
  [FP list]
```

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.
