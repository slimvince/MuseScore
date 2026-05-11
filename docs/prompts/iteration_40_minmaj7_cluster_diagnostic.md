# Iteration 40: MinMaj7 cluster diagnostic — Augmented root-pos → MinorMajor7 second-inv

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

Iter 38 identified 6 genuine Cat 2 cases with the pattern `(Augmented→Major7)`.
Each region: our winner is a root-position Augmented triad (bassIsRoot=true) and
the correct answer is a MinorMajor7 chord in second inversion at the same bass.

Observed interval relationship (verified across all 6 cases):
  winner: D+ (rootPc=2, bassPc=2)  → alt: GmMaj7/D (rootPc=7, bassPc=2)
  winner: E+ (rootPc=4, bassPc=4)  → alt: AmMaj7/E (rootPc=9, bassPc=4)
  winner: F#+ (rootPc=6, bassPc=6) → alt: BmMaj7/F# (rootPc=11, bassPc=6)

  Interval: alt.rootPc == (winner.bassPc + 5) % 12  [perfect fourth above bass]
  The winner's bass is the fifth of the alt chord (second inversion).
  The Augmented triad {root, M3, A5} shares all 3 pitch classes with the
  MinMaj7 chord {root+5, root+8, root+0, root+4} — the MinMaj7 just adds
  the chord root (a perfect fourth above the bass).

This pattern was previously identified but deferred due to reported regression
concerns. This iteration investigates whether a gate is viable now.

---

## Step 0 — Historical regression context

Read `STATUS.md` and search for any prior mentions of the MinMaj7 cluster,
Augmented→Major7, or the specific BIR cases (bwv20.11, bwv288, bwv309, bwv331,
bwv40.3, bwv64.8) in the following files:

- `STATUS.md`
- Any iteration prompt files in `docs/prompts/` that reference "MinMaj7",
  "Augmented→Major", or "regression" in the context of Augmented chords

Report:
1. Was a gate for this pattern previously attempted (i.e. was code written)?
   If so, which iteration, and what was the regression count?
2. Or was it only identified as a candidate but never implemented?
3. What specific regression scenario was described — did it affect Baroque,
   Jazz, or both?

This context determines whether to look for a pre-existing abandoned gate
block in chordanalyzer.cpp.

---

## Step 1 — Confirm quality enum name and interval in corpus JSON

Pick one genuine case (bwv20.11, bwv309, or bwv40.3) and print the full
winner and alternatives entries to confirm:
- The exact quality string for the Augmented winner (e.g. "Augmented")
- The exact quality string for the MinMaj7 alt (e.g. "MinorMajor7", "MinMajSeventh", etc.)
- That alt.rootPitchClass == (winner.bassPitchClass + 5) % 12 in the JSON data
- That alt.bassPitchClass == winner.bassPitchClass

```python
import json

TARGETS = [
    ('tools/corpus/bwv20.11.ours.json',  7, 3.0),
    ('tools/corpus/bwv309.ours.json',   12, 3.0),
    ('tools/corpus/bwv40.3.ours.json',   9, 1.0),
]

for fpath, meas, beat in TARGETS:
    data = json.load(open(fpath))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            print(f"\n{fpath} m={meas} b={beat}")
            print(f"  winner: quality={r.get('quality')} rootPc={r.get('rootPitchClass')} "
                  f"bassPc={r.get('bassPitchClass')} bassIsRoot={r.get('bassIsRoot')} "
                  f"score={r.get('chordScore')}")
            for i, a in enumerate(r.get('alternatives', [])):
                interval = (a.get('rootPitchClass', -1) - r.get('bassPitchClass', -1) + 12) % 12
                print(f"  alt[{i}]: quality={a.get('quality')} rootPc={a.get('rootPitchClass')} "
                      f"bassPc={a.get('bassPitchClass')} score={a.get('score')} "
                      f"margin={r.get('chordScore',0)-a.get('score',0):.3f} "
                      f"rootPc−bassPc(mod12)={interval}")
            break
```

Report:
- Exact quality string for the MinMaj7 chord as stored in JSON
- Whether all 6 genuine cases have a MinMaj7 alt with the +5 interval
- Margin range across the 6 cases (to calibrate the threshold)

Do NOT proceed to Step 2 until this is answered.

---

## Step 2 — Check for existing Augmented gate interactions

Read the relevant section of `src/composing/chordanalyzer.cpp` covering
Gate K (Augmented I4 inversion) and Gate L (Augmented→Major TYPE-A).
Report:
- Does either gate's entry condition overlap with the MinMaj7 scenario?
  (winner=Augmented+bassIsRoot=true is shared with Gate L's entry)
- Is there any abandoned or commented-out code block targeting Augmented→MinMaj7?
- Could Gate L's `same-root Major alt` condition ever fire on a MinMaj7 alt
  that has a different root? (It should not — Gate L checks rootPc equality.)

This confirms the new gate would not conflict with existing gates.

---

## Step 3 — False positive scan (structured fields only)

Using the exact quality string confirmed in Step 1 for the MinMaj7 alt, scan
the full Baroque corpus for all regions where:
- `winner.quality == "Augmented"` AND `winner.bassIsRoot == true`
- An alternative exists with `alt.quality == [MinMaj7_quality_string]` AND
  `alt.bassPitchClass == winner.bassPitchClass` AND
  `alt.rootPitchClass == (winner.bassPitchClass + 5) % 12`
- `margin (winner.score − alt.score) ≤ 0.50`

Classify each match as:
- GENUINE: in the genuine-6 list below
- FP: NOT in genuine-6

```python
GENUINE = {
    ('bwv20.11', 7,  3.0),
    ('bwv288',  11,  1.0),
    ('bwv309',  12,  3.0),
    ('bwv331',   2,  1.0),
    ('bwv40.3',  9,  1.0),
    ('bwv64.8',  9,  3.0),
}
```

Do NOT parse chordSymbol or romanNumeral. Use only: quality, bassIsRoot,
bassPitchClass, rootPitchClass, chordScore (winner), score (alternative).

Report: genuine count found, FP count, full FP list (file, measure, beat,
margin, winner.rootPitchClass, winner.bassPitchClass, alt.rootPitchClass,
alt.bassPitchClass — raw values).

Also run the scan at a tighter threshold (≤ 0.35) and report FP count at
that threshold separately.

**If FP count > 2 at both thresholds: STOP. Do not proceed to Jazz scan.**

---

## Step 4 — Jazz scan (only if Baroque FP count ≤ 2 at some threshold)

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
```

Re-run the Step 3 scan at whichever threshold passed. Report Jazz FP count
and list.

Restore Baroque corpus afterward:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 5 — Report to Cowork

```
Step 0 — Historical regression context:
  Previously attempted as code: [yes — iter N / no — candidate only]
  Regression details: [Baroque/Jazz, count, reason] or [not applicable]
  Abandoned gate block found: [yes / no]

Step 1 — JSON structure confirmation:
  MinMaj7 quality string: "[exact string]"
  Interval confirmed (+5 for all 6): [yes / no — list any exceptions]
  Margin range across genuine-6: [min] to [max]

Step 2 — Gate interactions:
  Gate K/L overlap: [yes — describe / no]
  Abandoned code found: [yes / no]

Step 3 — Baroque false positive scan:
  Fields used: [confirm no symbol parsing]
  At threshold ≤ 0.50: genuine=N  FP=N
  At threshold ≤ 0.35: genuine=N  FP=N
  [FP list with raw field values]

Step 4 — Jazz scan (if reached):
  Threshold used: [0.50 / 0.35]
  Jazz FP count: N
  [FP list]
```

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.
