# Iteration 36: Extend alternatives JSON, then Gate M diagnostic scan

## Standing rule — no symbol inference

**Every script in this iteration must use only structured numeric/enum fields
(rootPc, bassPc, quality, score, etc.). No chord symbol string parsing of any
kind. No Roman numeral inference. If a needed field is absent from the JSON,
report that fact and stop — do not substitute symbol parsing as a fallback.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baseline: BIR=true=48, BIR=false=787.

---

## Background

Iter 35 (Steps 0–1 already completed) established:
- The genuine three-way set requires DCML agreement; comparison is on root_pc only.
- Winner regions have rootPitchClass, bassPitchClass, quality, and score as structured
  fields. Alternative entries have **only** chordSymbol, romanNumeral, and score —
  rootPitchClass, bassPitchClass, and quality are absent from alternatives.
- Symbol parsing is prohibited, so the Gate M scan cannot run on the current JSON.

The fix: extend the batch_analyze JSON serializer to emit the same structured fields
for each alternative that it already emits for the winner. Then regenerate the corpus
and run the scan.

---

## Step 1 — Extend alternatives JSON output in batch_analyze.cpp

Open `tools/batch_analyze.cpp`. Find the section that serializes the `alternatives`
array for each region. Currently each alternative entry has:
- `chordSymbol`
- `romanNumeral`
- `score`

Add the following fields to each alternative entry, using the same field names and
types already used on winner regions:
- `rootPitchClass` (int, 0–11; the root pitch class of the alternative chord)
- `bassPitchClass` (int, 0–11; the bass pitch class of the alternative chord)
- `quality` (string; the chord quality enum name, e.g. "Minor", "Diminished",
  "DiminishedSeventh", "Major", etc.)
- `bassIsRoot` (bool; true if bassPitchClass == rootPitchClass)

These values come from the same chord object that already supplies `chordSymbol` —
they are NOT derived by parsing the symbol string. Use the existing accessor methods
on the chord/region object. If a field is not available on the alternative chord
object, report what is available and stop — do not fall back to symbol parsing.

Do NOT modify chordanalyzer.cpp or any scoring logic.

---

## Step 2 — Build and verify tests pass

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: composing_tests 407/407, notation_tests 53/53.
Pipeline snapshot goldens should NOT need refreshing — this change only affects
batch_analyze output, not the chord analysis pipeline itself.

If snapshot tests fail anyway, investigate before proceeding. Do not run
`--update-goldens` without understanding why they failed.

---

## Step 3 — Regenerate corpus and confirm baselines

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=48, BIR=false=787. If either number differs, stop and report.

---

## Step 4 — Confirm new fields are present in alternatives

Pick any `.ours.json` file from `tools/corpus/` that has at least 3 alternatives on
some region. Print the raw JSON for that region's `alternatives` array:

```python
import json

data = json.load(open('tools/corpus/bwv302.ours.json'))
for r in data.get('regions', []):
    alts = r.get('alternatives', [])
    if len(alts) >= 3:
        print(f"Region m={r['measureNumber']} b={r['beat']}")
        print(f"Alt fields: {list(alts[0].keys())}")
        for i, a in enumerate(alts[:4]):
            print(f"  alt[{i}]: {a}")
        break
```

Confirm that `rootPitchClass`, `bassPitchClass`, `quality`, and `bassIsRoot` are
present and non-null on at least the first alternative. If any field is still absent,
report which field is missing and why, then stop.

---

## Step 5 — False positive scan (structured fields only)

Using ONLY the fields confirmed in Step 4, write a scan that finds all Baroque corpus
regions where:
- `winner.quality == "Minor"` AND `winner.bassIsRoot == true`
- An alternative exists with `quality` in `{"Diminished", "DiminishedSeventh"}` AND
  `alt.rootPitchClass == winner.rootPitchClass` AND
  `alt.bassPitchClass == winner.bassPitchClass`
- Margin (`winner.score − alt.score`) ≤ 0.50

Do NOT use chordSymbol or romanNumeral anywhere in this script.

For each matching region classify as:
- GENUINE: in the genuine-8 list below
- FP (false positive): NOT in genuine-8

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

Report: genuine count found, FP count, full list of FP cases (file, measure, beat,
margin, winner.quality, winner.rootPitchClass, winner.bassPitchClass, alt.quality,
alt.rootPitchClass, alt.bassPitchClass — raw field values, no symbols).

**If FP count > 2: STOP. Do not proceed to Jazz scan or implementation.**

---

## Step 6 — Jazz scan (only if Baroque FP count ≤ 2)

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
```

Re-run the same scan (same code, same thresholds). Report Jazz FP count and list.

Restore Baroque corpus afterward:

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 7 — Tied-score cases (only if both scans pass)

For the genuine cases with margin=0.00 (bwv302, bwv40.6, bwv85.6, bwv423): confirm
using raw JSON fields that `winner.score == alt.score` exactly. Also report: how many
OTHER regions in the full Baroque corpus have `winner.quality=="Minor"` AND an
alternative with `quality` in `{"Diminished","DiminishedSeventh"}` at exactly the same
score (margin=0.00) and same rootPitchClass. Use structured fields only.

---

## Step 8 — Report to Cowork

```
Step 1 — JSON extension:
  Fields added to alternatives: [list]
  Source of values: [accessor method names, NOT symbol parsing]

Step 2 — Tests:
  composing_tests: N/407
  notation_tests:  N/53
  Pipeline snapshot tests: [pass / fail — if fail, explain]

Step 3 — Baselines after corpus regeneration:
  BIR=true=N  BIR=false=N

Step 4 — Alternatives field confirmation:
  Fields present and non-null: [list]

Step 5 — Baroque false positive scan:
  Fields used: [confirm no symbol parsing]
  Genuine found: N / 8
  FP count: N
  [FP list with raw field values]

Step 6 — Jazz scan (if reached):
  Jazz FP count: N
  [FP list]

Step 7 — Tied-score cases (if reached):
  Confirmed zero-margin genuine: N
  Other Baroque regions with same condition at margin=0.00: N
```

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.
