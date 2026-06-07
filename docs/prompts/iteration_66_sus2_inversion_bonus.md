# Iteration 66: Sus2 P5-inversion bonus — fix bwv184.5 m=13 b=3.0 and bwv43.11 m=3 b=2.0

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=5, BIR=false=125. Jazz BIR=false=12.
(Commit af785da463 — Iter 65 Part A: bass-PC exemption in HalfDim allTonesPresent.)

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Two of the remaining 5 BIR=true cases share the same structural signature:
bass PC is the P5 of the agreed sus2 root, winner has bassIsRoot=true
(Power chord, root=bass), and all 3 sus2 tones are present in the region.

**Case bwv184.5 m=13 b=3.0** — Scoring gap.
PCs include D, E, A; bass=A (pc=9). Agreed root: D (pc=2).
Winner: A5 (Power, bassIsRoot=true), score≈2.05.
Alt[N]: Dsus2/A (root=2, sus2, P5 in bass), score≈1.98. Gap ≈ 0.07.
Dsus2 appears in results[] but scores below A5.

**Case bwv43.11 m=3 b=2.0** — Candidate absent from results[].
PCs={A,D,E}; A weight=0.6 (bass), D=0.2, E=0.2; bass=A (pc=9). Agreed root: D (pc=2).
Winner: A5 (Power, bassIsRoot=true), score=2.29.
Alts: Asus (×2) ≈2.22, E7sus/A ≈1.98. No D-rooted Dsus2 in results[].
Root cause (Iter 65): results[] cap=3 filled by A-rooted candidates; the
"guaranteed inversion alternative" slot goes to E7sus/A, not Dsus2.
Dsus2 raw score for this region is unknown — obtain in Step 2.

This iteration:
1. Captures the Dsus2 raw score for bwv43.11 (diagnostic).
2. Implements a targeted sus2 P5-inversion bonus analogous to the Iter 61/65
   HalfDim fix: when winner is Power with bassIsRoot=true and a sus2 candidate
   has its P5 in the bass, force the sus2 candidate into results[] (if absent)
   and apply a score bonus to place it above the Power winner.
3. Spot-checks both cases.

---

## Step 1 — Confirm baselines (no corpus regen)

```bash
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Must show BIR=true=5, BIR=false=125. If not, regenerate with Baroque preset first.

---

## Step 2 — Diagnostic: Dsus2 raw score for bwv43.11

Print current corpus state for both cases. Dsus2 will not appear in alts for
bwv43.11 (confirmed Iter 65). If no D-rooted entry appears, add a temporary
printf in the candidate scoring loop in `chordanalyzer.cpp` to capture the raw
score for root=2 (D) across all templates in this region, then rebuild and
re-run the single file. Report the Dsus2 raw score before the bonus.

```python
import json
from pathlib import Path

for stem, meas, beat in [('bwv184.5', 13, 3.0), ('bwv43.11', 3, 2.0)]:
    data = json.loads((Path('tools/corpus') / f'{stem}.ours.json').read_text(encoding='utf-8'))
    r = next((r for r in data['regions']
              if r.get('measureNumber') == meas and abs(r.get('beat', 0) - beat) < 0.05), None)
    if r:
        print(f'\n=== {stem} m={meas} b={beat} ===')
        print(f'winner: root={r["rootPitchClass"]} qual={r["quality"]!r} '
              f'score={r.get("chordScore", 0):.4f} bassIsRoot={r["bassIsRoot"]}')
        print(f'pcSet: {r.get("pitchClassSet")}  bass={r["bassPitchClass"]}')
        for i, a in enumerate(r.get('alternatives', [])):
            print(f'alt[{i}]: root={a["rootPitchClass"]} qual={a["quality"]!r} '
                  f'score={a.get("score", 0):.4f}')
```

---

## Step 3 — Read the HalfDim inversion bonus (Iter 61+65)

Read `chordanalyzer.cpp` lines ~1994–2035 (the bestAltIdx loop and the
HalfDim inversion guard, including the Iter 65 bass-PC exemption).

Note:
- The exact structural guard conditions
- How `allTonesPresent` is called with the bass-PC exemption
- How the bonus is applied (score delta to candidate and/or deduction from winner)
- Where and how the candidate is force-appended to results[] if absent

The sus2 fix follows the same pattern. Read the exact enum value for the
sus2 template quality — do NOT infer from string names; look for the template
at index 10 (intervals {0, 2, 7}) and confirm the ChordQuality enum value used.

---

## Step 4 — Implement sus2 P5-inversion bonus

Add a sus2 inversion bonus block immediately after the HalfDim inversion block.

**Structural conditions (all must hold):**

1. `winner.quality == ChordQuality::Power` (or whatever the enum value for A5/Power is —
   confirm from source; do not assume the string).
2. `winner.bassIsRoot == true` (equivalently: winner rootPc == bassPc).
3. A sus2 candidate exists where:
   - `candidateRootPc == (bassPc - 7 + 12) % 12`
     [bass is the P5 of the sus2 root — second inversion]
   - `candidateQuality == <sus2 enum value>` (from Step 3)
4. All 3 sus2 tones confirmed sounding:
   - `pcWeight[candidateRootPc] > 0`  (root present at any weight)
   - `pcWeight[(candidateRootPc + 2) % 12] > 0`  (M2 present)
   - bass PC (P5) is sounding by definition — exempt from threshold (consistent
     with Iter 65 bass-PC exemption pattern)
5. Gate: `prefs.preferMinorOverMajorAdd6` (Baroque/Standard only; prevents Jazz
   regressions, same gate as HalfDim and Gate G-E).

**Action when all conditions met:**

- If the sus2 candidate is not already in results[]: force-append it (analogous
  to the "guaranteed inversion alternative" mechanism — locate that append site
  in the code and mirror it for this candidate).
- Apply a score bonus of **+0.25** to the sus2 candidate score. (This covers the
  known gap of 0.07 for bwv184.5 with margin; if bwv43.11's gap is larger, adjust
  upward to clear it, but do not exceed +0.50 without checking regressions first.)
- Do NOT apply a deduction to the Power winner — the bonus alone should suffice.

If the sus2 candidate is not readily accessible at the bonus site (e.g. results[]
is already finalized), add the sus2 check earlier in the pipeline at the same
location as the HalfDim check.

---

## Step 5 — Build and spot-check both cases

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Run the two-file spot-check from Step 2 against freshly regenerated output for
bwv184.5 and bwv43.11 only (or full corpus if partial not supported).

Expected:
- bwv184.5 m=13 b=3.0: winner root=2, qual=Suspended2 (sus2 enum value), bassIsRoot=false
- bwv43.11 m=3 b=2.0: winner root=2, qual=Suspended2 (sus2 enum value), bassIsRoot=false

If only one case flips and the bonus magnitude needs adjustment, tune and rebuild
before proceeding to full corpus.

---

## Step 6 — Run full Baroque corpus and BIR

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true 5→3 (fixes bwv184.5 + bwv43.11), BIR=false 125→≤125.
Hard stops: BIR=false increases > 5 — revert. BIR=true increases — revert immediately.

---

## Step 7 — Jazz validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz BIR=false hard stop: ≤75 (current 12). Restore Baroque after:

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
```

---

## Step 8 — Run both test suites

```bash
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407, 53/53. If pipeline snapshots fail for bwv184.5 or bwv43.11
and the new output is verified correct, refresh goldens:

```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 9 — Commit

```bash
git add src/composing/analysis/chord/chordanalyzer.cpp
git commit -m "Composing: sus2 P5-inversion bonus — Dsus2/A over Power winner

bwv184.5 m=13 b=3.0: Dsus2/A in results[] but 0.07 below A5 (Power) winner.
bwv43.11 m=3 b=2.0: Dsus2/A absent from results[] (cap-3 A-rooted; guaranteed
inversion slot taken by E7sus/A).

Fix: when winner is Power+bassIsRoot=true and sus2 candidate has bass=P5,
force candidate into results[] and apply +N score bonus.
Structural guard: all 3 sus2 tones present (bass PC exempt from threshold).
Gate: prefs.preferMinorOverMajorAdd6 (Baroque/Standard only).

BIR=true: 5 → N  BIR=false: 125 → N  Jazz BIR=false: 12 → N"

git push
```

---

## Step 10 — Report to Cowork

```
Diagnostic:
  bwv43.11 Dsus2 raw score (pre-fix): N
  bwv184.5 Dsus2 score (pre-fix): ≈1.98 (from Iter 63/65)

Sus2 P5-inversion bonus:
  Bonus magnitude applied: +N
  bwv184.5 m=13 b=3.0 winner after: root=N qual=Q bassIsRoot=[yes/no]
  bwv43.11 m=3 b=2.0 winner after: root=N qual=Q bassIsRoot=[yes/no]
  Baroque BIR: BIR=true 5→N  BIR=false 125→N
  Jazz BIR=false: N
  Tests: composing N/407  notation N/53
  Committed: [yes — hash / not committed — reason]

Remaining BIR=true after this iteration: N
```
