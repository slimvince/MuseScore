# Iteration 42: Gate O — Augmented root-pos → MinorMajor7 second-inv

## Standing rule — no symbol inference

**No chord symbol string parsing of any kind. No Roman numeral inference.
Use only structured fields (quality, rootPc, bassPc, extensions, context).**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=32, BIR=false=177.

---

## Background

Iter 40–41 established that the MinMaj7 cluster (6 genuine Cat 2 cases) is
partially addressable. The gate condition tested:

Entry:
  - winner.quality == Augmented AND bassIsRoot == true
  - winner has no seventh extension (no MinorSeventh, no MajorSeventh)

Alt (search results[1..end]):
  - alt.quality == Minor (ChordQuality::Minor)
  - alt has MajorSeventh extension → distinguishes MinMaj7 from plain Minor
  - alt.bassPc == winner.bassPc  (same bass)
  - alt.rootPc == (winner.bassPc + 5) % 12  (alt root is P4 above bass = 2nd inv)

Temporal (require context != nullptr):
  - !context->bassIsStepwiseToNext  OR  context->regionMetricWeight >= 1.0

Margin: winner.score − alt.score ≤ 0.50f

Expected outcome: 3 genuine fixes (bwv288, bwv309, bwv331), 0 FPs.
Cases NOT catchable: bwv20.11 (indistinguishable from FP bwv20.7 on all signals),
bwv40.3 and bwv64.8 (margin 0.503, above threshold).

---

## Step 1 — Read existing gate block before writing anything

Read the Gate K and Gate L blocks in `src/composing/chordanalyzer.cpp` to
understand the exact coding pattern used:
- How bestAltIdx is found (loop or direct index?)
- How extension checks are written (`hasExtension(...)`)
- How context fields are guarded (`context != nullptr && ...`)
- Where the new gate should be inserted relative to Gate L

Report the line numbers of Gate L's opening comment and closing brace before
writing any new code.

---

## Step 2 — Implement Gate O

Add Gate O immediately after Gate L in `src/composing/chordanalyzer.cpp`.
Follow Gate L's code structure exactly.

Gate O logic:

```
// Gate O — prefer MinorMajor7 (2nd inversion) over root-position Augmented.
//
// When the winner is a plain Augmented triad (no seventh extension) with
// bassIsRoot=true, and a runner-up has:
//   - Minor quality with MajorSeventh extension (= a MinMaj7 chord)
//   - the same bass as the winner
//   - root a perfect fourth above the bass  (alt.rootPc == (bassPc+5)%12)
//   - score margin within 0.50
// and the temporal context indicates the chord is not a passing augmented
// (bass does NOT move stepwise to next region, OR region is on a strong beat):
//   → prefer the MinMaj7 reading.
//
// Musical basis: the three pitch classes of a root-position Augmented triad
// are a strict subset of the MinMaj7 chord built a P4 above the bass.
// e.g. D+ {D,F#,Bb} ⊂ GmMaj7/D {D,G,Bb,F#}. When the MinMaj7 is available
// as a runner-up and temporal context supports a stable harmonic reading
// (not a passing chord), the MinMaj7 is more specific and correct.
//
// Threshold (kGateOMarginThreshold = 0.50f) calibrated on Baroque corpus.
// See task #36 for planned migration to ChordAnalyzerPreferences.
```

The threshold should be stored as a named file-scope constant:
```cpp
static constexpr float kGateOMarginThreshold = 0.50f;
```

The temporal condition must be guarded for null context. If context is
nullptr, do NOT fire this gate (conservative — no temporal data = no
basis for the temporal filter that prevents FPs).

Search ALL of results[1..end] for the matching alt, not just results[1].
Use the same `bestAltIdx` pattern as Gate L if that searches the full
results vector; otherwise write the search loop explicitly.

Do NOT modify Gate K, Gate L, or any earlier gate.

---

## Step 3 — Build and run both test suites

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 and 53/53. If composing_tests fail, read
`src/composing/tests/chord_mismatch_report.txt` and fix before continuing.

The pipeline snapshot test will likely fail because Gate O changes chord output
for the 3 fixed regions. This is expected and correct. After confirming the
changed output is right, refresh goldens:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Only run --update-goldens after confirming the new output is correct.

---

## Step 4 — Baroque corpus validation

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected:
  BIR=true  = 29  (was 32, −3 from bwv288, bwv309, bwv331)
  BIR=false = 177  (must not increase)

If BIR=false increases: STOP. Do not proceed. Report the regression cases.
If BIR=true reduction is not exactly 3: report which cases fired and which
did not, with their JSON field values.

---

## Step 5 — Jazz corpus validation

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Hard stop: Jazz BIR=false must not exceed 75.

If Jazz BIR=false > 75: stop, do not commit. Report the Jazz regression cases.
Investigate whether the temporal guard or the extension check can be tightened
to exclude the Jazz FPs WITHOUT adjusting the Baroque-calibrated 0.50f threshold.

Restore Baroque corpus after Jazz validation:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 6 — Benchmark score visual check

Per ARCHITECTURE.md Rule 12, open each benchmark score in MuseScore Studio
and confirm the key passages look correct after Gate O:

| Score | Key passages |
|-------|-------------|
| bwv227.7 | Bars 1–2, 8–10, final cadence |
| Chopin BI16-1 | Bars 1–5, 10–16, trio |
| Dvořák op08n06 | Early slow section, chromatic middle |

Report any unexpected chord-track changes in these scores.

---

## Step 7 — Commit (only if all validation passes)

If and only if:
- composing_tests 407/407
- notation_tests 53/53
- pipeline_snapshot_tests pass (after --update-goldens)
- Baroque BIR=true decreased, BIR=false = 177
- Jazz BIR=false ≤ 75
- Benchmark scores look correct

Then commit:
```
git add src/composing/analysis/chord/chordanalyzer.cpp
git commit -m "Gate O: prefer MinMaj7/2nd-inv over root-pos Augmented when temporal context supports

When winner is plain Augmented (no 7th extension) with bassIsRoot=true and a
runner-up has Minor+MajorSeventh quality at the same bass with rootPc=(bassPc+5)%12
(perfect-fourth above bass = second inversion), prefer the MinMaj7 reading when
margin ≤ 0.50 and temporal context indicates stable harmony (bass not moving
stepwise to next region, OR region on strong beat).

Fixes: bwv288 m11 E+→AmMaj7/E, bwv309 m12 D+→GmMaj7/D, bwv331 m2 E+→AmMaj7/E
BIR=true: 32→29. BIR=false: unchanged at 177. Jazz BIR=false: unchanged at 75."
```

Then update `C:\s\MS\build_and_test.md` with the new Baroque baseline
(BIR=true=29) and a Gate O entry in the gate history.

---

## Step 8 — Report to Cowork

```
Step 1 — Gate L location: lines [N–N]

Step 2 — Gate O implementation:
  Inserted at: line [N]
  kGateOMarginThreshold: 0.50f
  Extension check: [exact function call used]
  Temporal guard: [exact condition written]
  Alt search: [loop or bestAltIdx — describe]

Step 3 — Tests:
  composing_tests: N/407
  notation_tests:  N/53
  Pipeline snapshot: [updated / no change needed]
  Mismatch report: [any new mismatches?]

Step 4 — Baroque validation:
  BIR=true: 32→N  (expected 29)
  BIR=false: N  (expected 177)
  Cases that fired: [list]
  Cases that did not fire: [list with reason]

Step 5 — Jazz validation:
  Jazz BIR=false: N  (must be ≤ 75)
  Jazz BIR=true: N
  Any Jazz regressions: [list or "none"]

Step 6 — Benchmark scores: [pass / any issues]

Step 7 — Commit: [hash] or [not committed — reason]
```
