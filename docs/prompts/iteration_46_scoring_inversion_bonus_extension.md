# Iteration 46: Scoring architecture — extend inversion bonuses to Augmented and HalfDiminished

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=32, BIR=false=177.

---

## Background

Two categories of genuine-32 errors are blocked by the same root cause:

**Gate P (TYPE-B Augmented):** Our winner is E+ (root-pos Augmented); the correct
reading is C+/E (1st-inversion Augmented). C+/E never appears in results[] because
`supportsContextualInversionBonuses` requires quality==Major||Minor. Augmented
inversions receive neither the stepwiseBassInversionBonus (+0.50) nor the
completeTriadInversionBonus (+0.45), so they fall below results[] threshold.

**Cluster A (HalfDiminished):** Our winner is Minor with bass=root (Xm, bassIsRoot=true);
the correct reading is HalfDiminished in 1st inversion (Yø7/X, same bass).
The HalfDim 1st-inv reading is absent from results[] for 4 of 6 genuine cases
for the same reason: HalfDiminished also excluded from supportsContextualInversionBonuses.

The architectural fix: extend inversion bonus support to Augmented and HalfDiminished
quality candidates. This lets them compete on merit. If correctly-spelled Augmented
inversions and HalfDim inversions now rank high enough to enter results[], the gate
layer (Gate P, Gate Q) becomes viable — or may not even be needed if the scoring
change alone promotes the correct reading to winner.

This is a **diagnostic + controlled implementation** iteration. Read the scoring
code thoroughly before changing anything.

---

## Step 1 — Read the scoring code (no changes yet)

Read `src/composing/analysis/chord/chordanalyzer.cpp`. Find:

1. The definition or computation of `supportsContextualInversionBonuses` (or the
   equivalent flag/condition that gates stepwiseBassInversionBonus and
   completeTriadInversionBonus). Report the exact line number and condition.

2. Every bonus that is gated behind this flag — list each bonus name, value, and
   the exact guard condition. Include:
   - stepwiseBassInversionBonus
   - completeTriadInversionBonus
   - sameRootInversionBonus
   - Any others gated on quality==Major||Minor

3. The `bassNoteRootBonus` — confirm it fires only when rootPc==bassPc (i.e.,
   root-position candidates only). Report line and value.

4. Whether Augmented or HalfDiminished are currently mentioned anywhere in the
   inversion bonus section.

Report all line numbers. Do NOT make any changes in this step.

---

## Step 2 — Model the change

Before modifying code, reason through the expected impact:

**Augmented extension:**
- An Augmented triad has 3 notes: root (R), M3 (R+4), A5 (R+8).
- Root-position Augmented: bass=R, gets bassNoteRootBonus (+0.70).
- 1st-inversion Augmented: bass=M3 (R+4). With the extension, this candidate
  would get stepwiseBassInversionBonus (if bass stepwise) + completeTriadInversionBonus.
- 2nd-inversion Augmented: bass=A5 (R+8). Same bonuses would apply.
- Risk: boosting ALL Augmented inversions may promote incorrect ones. The Augmented
  triad's full symmetry (all 3 roots are equivalent) means the scoring must rely
  heavily on context to prefer the correct root.

**HalfDiminished extension:**
- A HalfDim7 chord: root (R), m3 (R+3), d5 (R+6), m7 (R+10).
- 1st inversion: bass=m3 (R+3). With extension: gets inversion bonuses.
- The Xm6 = Yø7/X equivalence means: when bass=B and the chord is {B,D,F,A},
  both Bm6 (root-pos Minor6) and G#ø7/B (HalfDim 1st-inv) are valid readings.
  With inversion bonuses, Gø7/B might score high enough to compete.

**Scoring neutrality principle:**
The extension should not CREATE preferences — it should remove a systematic
disadvantage. Augmented and HalfDiminished inversions should compete on the
same terms as Major and Minor inversions. Any context-sensitivity (stepwise
bass, metric weight, etc.) already in the bonus computation will naturally apply.

---

## Step 3 — Implement the extension

Make the minimal targeted change: extend `supportsContextualInversionBonuses`
(or the equivalent condition) to include Augmented and HalfDiminished.

Follow this exact pattern:
- If the current code is:
  ```cpp
  bool supportsContextualInversionBonuses =
      (quality == ChordQuality::Major || quality == ChordQuality::Minor);
  ```
- Change to:
  ```cpp
  bool supportsContextualInversionBonuses =
      (quality == ChordQuality::Major || quality == ChordQuality::Minor ||
       quality == ChordQuality::Augmented || quality == ChordQuality::HalfDiminished);
  ```

Add a comment explaining the extension:
```cpp
// Extended in Iter 46 to include Augmented and HalfDiminished: these quality
// types were systematically excluded from inversion bonuses, causing correct
// inverted readings (e.g. C+/E, Yø7/X) to fall below the results[] threshold.
// They now compete on equal terms with Major/Minor inversions.
```

If the code structure differs from the pattern above, preserve the existing style
exactly and extend it analogously. Do NOT change bonus values. Do NOT add new
bonus types. Do NOT modify the bonus amounts.

---

## Step 4 — Build and run both test suites

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 and 53/53. If composing_tests fail, read
`src/composing/tests/chord_mismatch_report.txt` and fix before continuing.

If pipeline_snapshot_tests fail (output changed for some regions), confirm the
changed regions are improvements before refreshing goldens:
```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 5 — Check candidate pool for target cases

Before full corpus run, verify the extension had the intended effect. For the
TYPE-B (Gate P) and Cluster A (Gate Q) target cases, check whether the correct
alternative now appears in results[]:

```python
import json
from pathlib import Path

# Regenerate just these files first — run batch_analyze on them individually
# or use the full corpus regeneration in Step 6 and then inspect.

TYPEB_TARGETS = [
    # (stem, meas, beat, expected_alt_rootPc, expected_alt_quality)
    ('bwv288', 11, 1.0,  0, 'Augmented'),   # C+/E — correct root P4 below E
    ('bwv309', 12, 3.0, 10, 'Augmented'),   # Bb+/D — correct root P4 below D
    ('bwv331',  2, 1.0,  0, 'Augmented'),   # C+/E
]

CLUSTER_A_TARGETS = [
    ('bwv259',   8, 1.0,  1, 'HalfDiminished'),  # C#ø7/E (rootPc=1)
    ('bwv284',   3, 3.0,  9, 'HalfDiminished'),  # Aø7/C  (rootPc=9)
    ('bwv335',   8, 1.0,  1, 'HalfDiminished'),  # C#ø7/E
    ('bwv40.8', 10, 1.0,  0, 'HalfDiminished'),  # Cø7/Eb (rootPc=0)
    ('bwv407',   7, 4.0, 11, 'HalfDiminished'),  # Bø7/D  (rootPc=11)
    ('bwv90.5',  8, 2.0, 11, 'HalfDiminished'),  # Bø7/D
]

CORPUS = Path('tools/corpus')

for stem, meas, beat, exp_rootPc, exp_qual in TYPEB_TARGETS + CLUSTER_A_TARGETS:
    fpath = CORPUS / f'{stem}.ours.json'
    if not fpath.exists():
        print(f'{stem}: FILE MISSING')
        continue
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            found = False
            for i, a in enumerate(r.get('alternatives', [])):
                if (a.get('quality') == exp_qual and
                        a.get('rootPitchClass') == exp_rootPc):
                    margin = r.get('chordScore', 0) - a.get('score', 0)
                    print(f'FOUND  {stem} m{meas} b{beat}: {exp_qual} rootPc={exp_rootPc}'
                          f' at alt[{i}] margin={margin:.4f} '
                          f'winner={r.get("quality")} rootPc={r.get("rootPitchClass")}')
                    found = True
                    break
            if not found:
                winner_q = r.get('quality')
                print(f'ABSENT {stem} m{meas} b{beat}: {exp_qual} rootPc={exp_rootPc}'
                      f' — winner={winner_q} rootPc={r.get("rootPitchClass")}')
            break
```

Report for each case: FOUND (with margin and rank) or ABSENT (still not generated).

If all TYPE-B and Cluster A targets show ABSENT: the scoring extension was
insufficient — the bonuses alone don't bring these candidates above threshold.
In that case, report and consider a dedicated raw-score boost (separate from the
inversion bonus flag) for Augmented and HalfDiminished inversion candidates.

---

## Step 6 — Baroque corpus validation

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report BIR=true and BIR=false. Interpret the results:

- BIR=true decreases AND BIR=false is unchanged or decreases: scoring fix is working
  cleanly — correct inversions promoted to winner without introducing regressions.
- BIR=true decreases AND BIR=false increases: some correct inversions promoted
  (good) but some incorrect inversions also boosted (regressions). Report all
  BIR=false changes in detail.
- BIR=true unchanged AND BIR=false increases: the extension boosted wrong inversions
  without fixing target cases. HARD STOP — revert the change.
- BIR=true unchanged AND BIR=false unchanged: extension had no effect on any region.
  Report and investigate whether the build was correct.

**Hard stop conditions:**
- BIR=false increases by more than 3: STOP. Revert. Report the regression cases.
- Any regression in a case that was previously correct: STOP. Report.

---

## Step 7 — Jazz corpus validation

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz BIR=false must not exceed 75. If it does: STOP, revert, report Jazz
regression cases in detail.

Restore Baroque corpus after Jazz run:
```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
```

---

## Step 8 — Commit (only if Steps 4–7 pass)

If and only if:
- composing_tests 407/407
- notation_tests 53/53
- BIR=false ≤ 177 + 3 and all regressions understood
- Jazz BIR=false ≤ 75

Then commit:
```
git add src/composing/analysis/chord/chordanalyzer.cpp
git commit -m "Scoring: extend inversion bonuses to Augmented and HalfDiminished

supportsContextualInversionBonuses previously gated on Major||Minor only.
Augmented and HalfDiminished inversion candidates received neither the
stepwiseBassInversionBonus (+0.50) nor completeTriadInversionBonus (+0.45),
causing correct inverted readings (e.g. C+/E, Yø7/X) to fall below the
results[] threshold entirely.

Extended the flag to include Augmented and HalfDiminished so these candidates
compete on equal terms. This unlocks the candidate pool for Gate P (TYPE-B
Augmented root correction) and Gate Q (HalfDim7/1st-inversion over Minor6).

BIR=true: 32→N  BIR=false: 177→N"
```

Then update `build_and_test.md` with new baselines.

---

## Step 9 — Report to Cowork

```
Step 1 — Scoring code:
  supportsContextualInversionBonuses condition: [exact code, line N]
  Bonuses gated on it: [list with values]
  bassNoteRootBonus: [value, condition, line N]

Step 2 — Model:
  Expected impact on Augmented inversions: [describe]
  Expected impact on HalfDiminished inversions: [describe]
  Risk areas: [describe]

Step 3 — Implementation:
  Change made at: line [N]
  Exact code written: [show]

Step 4 — Tests:
  composing_tests: N/407
  notation_tests: N/53
  Pipeline snapshot: [updated / no change / failed]

Step 5 — Candidate pool check:
  TYPE-B targets FOUND: N / 3
  Cluster A targets FOUND: N / 6
  [Any still ABSENT — list]

Step 6 — Baroque validation:
  BIR=true: 32→N  (Δ=N)
  BIR=false: 177→N  (Δ=N)
  Regressions (if any): [list with stem, meas, beat, before, after]

Step 7 — Jazz validation:
  Jazz BIR=false: N  (must be ≤ 75)
  Jazz regressions: [list or "none"]

Step 8 — Committed: [yes — hash] / [not committed — reason]
```
