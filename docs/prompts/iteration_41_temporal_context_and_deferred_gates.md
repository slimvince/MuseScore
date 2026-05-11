# Iteration 41: Extend JSON with temporal context — re-diagnose deferred gates

## Standing rule — no symbol inference

**Every script in this iteration must use only structured numeric/enum fields.
No chord symbol string parsing of any kind. No Roman numeral inference.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=32, BIR=false=177.

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.

---

## Background

Gates M (Minor→Diminished), N (Major→Minor first-inv), and the MinMaj7 cluster
(Augmented→Minor second-inv) were declared deferred because Python scans using
only pitch-content fields could not separate genuine cases from false positives.

Those scans were incomplete. `ChordTemporalContext` — which is passed to
`analyzeChord()` and used by existing gates — carries fields that the corpus
JSON does not currently expose:
  - `nextRootPc`: root of the next harmonic region (populated by batch_analyze
    via one-region look-ahead)
  - `previousRootPc`, `previousQuality`, `previousBassPc`: the prior region
  - `bassIsStepwiseFromPrevious`, `bassIsStepwiseToNext`: stepwise bass booleans
  - `consecutiveBassStepwiseCount`: scalar bass-line depth

The same JSON-extension approach used in Iter 36 (adding rootPitchClass,
bassPitchClass, quality to alternatives) applies here: add the populated
ChordTemporalContext fields to the winner-region JSON output, regenerate the
corpus, and re-run all three diagnostics with the new signals.

---

## Step 0 — Confirm which ChordTemporalContext fields batch_analyze populates

Read `tools/batch_analyze.cpp`. Find where ChordTemporalContext is constructed
and advanced between regions. Report:
- Which fields are actively set (non-default) for each region
- In particular: is `nextRootPc` populated via look-ahead? (`chordanalyzer.h`
  says it is — confirm the batch_analyze code path)
- Are `bassIsStepwiseFromPrevious` and `bassIsStepwiseToNext` computed?
- Are `previousQuality`, `previousRootPc`, `previousBassPc` carried forward
  via `advanceTemporalContext()`?

Do NOT proceed to Step 1 until confirmed.

---

## Step 1 — Extend region JSON output in batch_analyze.cpp

In the same section that serializes winner-region fields, add the following
from the ChordTemporalContext that was used when analyzing this region:
  - `nextRootPc` (int, -1 if unknown)
  - `previousRootPc` (int, -1 if unknown)
  - `previousQuality` (string — same qualityToString() used for winner quality)
  - `previousBassPc` (int, -1 if unknown)
  - `bassIsStepwiseFromPrevious` (bool)
  - `bassIsStepwiseToNext` (bool)
  - `consecutiveBassStepwiseCount` (int)

Source: the ChordTemporalContext struct that was passed to analyzeChord() for
this region. Do NOT re-derive these values by parsing chord symbols.

If any field is not available at the serialization point (e.g. nextRootPc is
computed after the fact), describe the sequencing issue and propose how to
capture it.

---

## Step 2 — Build and verify tests pass

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 and 53/53. Pipeline snapshot tests should NOT need refreshing
(batch_analyze output change only). If they fail, investigate before continuing.

---

## Step 3 — Regenerate corpus and confirm baselines

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=32, BIR=false=177. If different, stop and report.

---

## Step 4 — Confirm new fields present in sample regions

Print the new temporal context fields for two known cases:
- bwv302 m=1 b=4.0 (genuine Gate M Minor→Diminished case)
- bwv123.6 m=7 b=2.0 (genuine Gate N Major→Minor case)

```python
import json

SAMPLES = [
    ('tools/corpus/bwv302.ours.json',   1, 4.0, 'Gate M genuine'),
    ('tools/corpus/bwv123.6.ours.json', 7, 2.0, 'Gate N genuine'),
]

TEMPORAL_FIELDS = ['nextRootPc','previousRootPc','previousQuality',
                   'previousBassPc','bassIsStepwiseFromPrevious',
                   'bassIsStepwiseToNext','consecutiveBassStepwiseCount']

for fpath, meas, beat, label in SAMPLES:
    data = json.load(open(fpath))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            print(f"\n{label}  ({fpath.split('/')[-1]} m={meas} b={beat})")
            for f in TEMPORAL_FIELDS:
                print(f"  {f}: {repr(r.get(f, 'MISSING'))}")
            break
```

If any field is MISSING, stop and fix Step 1 before proceeding.

---

## Step 5 — Gate M re-diagnostic with temporal signals

Re-run the Gate M scan (winner.quality=="Minor" AND bassIsRoot AND
alt.quality∈{"Diminished","DiminishedSeventh"} AND same root AND same bass
AND margin ≤ 0.50) on all Baroque corpus regions.

For each match, additionally print:
  `nextRootPc`, `previousRootPc`, `previousQuality`

Then test the resolution hypothesis:
  `resolves_up = (nextRootPc != -1) and (nextRootPc == (winner.rootPitchClass + 1) % 12)`

Report for each of the 8 GENUINE and all FP cases:
  - Does `resolves_up` == True?
  - Does `previousQuality` == "Diminished" or "DiminishedSeventh"?

Genuine-8 set (from Iter 36):
```python
GENUINE_M = {
    ('bwv187.7', 14, 2.0), ('bwv227.11', 10, 3.0),
    ('bwv278',    8, 2.0), ('bwv301',     2, 3.0),
    ('bwv302',    1, 4.0), ('bwv40.6',   14, 2.0),
    ('bwv423',    9, 2.0), ('bwv85.6',    5, 1.0),
}
```

Report:
- Genuine cases where resolves_up=True: N / 8
- FP cases where resolves_up=True: N / 25
- Any other temporal field that separates genuine from FP (describe pattern)
- If resolves_up cleanly separates (all genuine True, ≤ 2 FP True): CLEAN SEPARATION

---

## Step 6 — Gate N re-diagnostic with temporal signals

Re-run the Gate N scan (winner.quality=="Major" AND bassIsRoot AND
alt.quality=="Minor" AND alt.rootPc==(bassPc-3+12)%12 AND same bass
AND margin ≤ 0.45) on all Baroque corpus regions.

For each match, print: `nextRootPc`, `previousRootPc`, `previousQuality`,
`regionMetricWeight` (if present).

Test candidate temporal signals for each of the 6 GENUINE and all FP cases:
  A. `nextRootPc == (winner.bassPitchClass + 4) % 12`
     (next root is major-third above bass = consistent with vi → III pattern)
  B. `nextRootPc == (winner.rootPitchClass + 7) % 12`
     (next root is a fifth above winner root = consistent with I → V)
  C. `previousQuality` value — any dominant-function quality preceding vi?

Genuine-6 set (from Iter 39):
```python
GENUINE_N = {
    ('bwv123.6',  7, 2.0), ('bwv322',  1, 3.0),
    ('bwv337',    1, 2.0), ('bwv392', 11, 4.0),
    ('bwv417',    3, 2.0), ('bwv425', 22, 3.0),
}
```

Report hit rates for each candidate signal across genuine vs FP. If any signal
gives genuine≥5 and FP≤2: report as promising.

---

## Step 7 — MinMaj7 re-diagnostic with temporal signals

For the 8 known MinMaj7 regions (4 genuine + 4 FP from Iter 40), print ALL
new temporal context fields side-by-side:

```python
MINMAJ7_ALL = [
    # (file_stem, measure, beat, label)
    ('bwv20.11', 7,  3.0, 'GENUINE'),
    ('bwv288',  11,  1.0, 'GENUINE'),
    ('bwv309',  12,  3.0, 'GENUINE'),
    ('bwv331',   2,  1.0, 'GENUINE'),
    ('bwv102.7',11,  2.0, 'FP'),
    ('bwv20.7', 13,  3.0, 'FP'),
    ('bwv226.2',10,  3.0, 'FP'),
    ('bwv48.7',  7,  3.0, 'FP'),
]
```

For each, print: quality, rootPc, bassPc, nextRootPc, previousRootPc,
previousQuality, previousBassPc, bassIsStepwiseFromPrevious,
bassIsStepwiseToNext, consecutiveBassStepwiseCount, regionMetricWeight.

Do NOT infer from chordSymbol. Report which temporal fields (if any) differ
between genuine and FP groups, and by how much.

---

## Step 8 — Report to Cowork

```
Step 0 — batch_analyze temporal context population:
  nextRootPc populated: [yes / no — how]
  bassIsStepwiseFromPrevious / ToNext: [yes / no]
  previousQuality / RootPc / BassPc: [yes / no — via advanceTemporalContext()]
  Any fields NOT populated: [list]

Step 1 — Fields added to JSON: [list]

Step 2 — Tests: composing=N/407  notation=N/53

Step 3 — Baselines: BIR=true=N  BIR=false=N

Step 4 — Field confirmation: [present / any MISSING]

Step 5 — Gate M temporal re-diagnostic:
  resolves_up genuine: N / 8
  resolves_up FP: N / 25
  Other separating signals: [describe or "none"]
  Gate M status: [CLEAN SEPARATION / PARTIAL / STILL BLOCKED]

Step 6 — Gate N temporal re-diagnostic:
  Signal A (nextRootPc = bassPc+4): genuine N/6  FP N/25
  Signal B (nextRootPc = rootPc+7): genuine N/6  FP N/25
  Signal C (previousQuality pattern): [describe]
  Gate N status: [CLEAN SEPARATION / PARTIAL / STILL BLOCKED]

Step 7 — MinMaj7 temporal signals:
  [Table of all 8 cases with temporal fields]
  Fields that differ between genuine and FP: [list or "none"]
  MinMaj7 status: [SEPARABLE / PARTIAL / STILL BLOCKED]
```

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.
