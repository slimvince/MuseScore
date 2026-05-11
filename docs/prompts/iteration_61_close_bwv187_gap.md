# Iteration 61: Close 0.53 scoring gap for bwv187.7 first-inversion HalfDim

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=7, BIR=false=132. Jazz BIR=false=12.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Iter 60 committed two fixes (381b401add):

- **C-1 (kCleanQualities guard)**: When a HalfDim candidate has all 4 chord tones
  confirmed and the winner's bass PC is a chord tone (not root) of that HalfDim, the
  inversion-correction step applies a deduction to the winner. For bwv187.7, this
  fired a −0.50 deduction on the Gm winner.

- **C-2 (alt cap 2→3)**: Raised batch_analyze alternative output cap. This reclassified
  7 BIR=true cases to near_agree (their correct chord was rank 3 in rawCandidates,
  previously invisible to analyze_inversion_errors.py). BIR=true dropped 14→7.

One case remains in BIR=true that is directly fixable by scoring:

**bwv187.7 m=14 b=2.0**
- PCs: {D, E, G, Bb} — full Eø7 set (root=E, m3=G, b5=Bb, m7=D)
- Bass PC: G (= root+3, i.e., first inversion)
- Winner: Gm root=7, score=2.3857 (after C-1 deduction −0.50), bassIsRoot=true
- Eø7:    root=4, score=1.8571, in alt[2]
- Gap:    0.53

The C-1 deduction closed part of the gap but not all of it. The bass-root bonus
on Gm (+0.70) and the non-bass penalty on Eø7 (−0.35) together create a structural
scoring asymmetry that C-1's deduction partially corrects but does not resolve.

---

## Step 1 — Understand the scoring anatomy

Before touching any code, read `chordanalyzer.cpp` and map out the complete scoring
path for the Gm winner and the Eø7 candidate for a region with bass=G and PCs={D,E,G,Bb}:

1. What is the raw score before any bonuses or penalties for each?
2. What bass-root bonus does Gm receive (exact field and amount)?
3. What non-bass penalty does Eø7 receive (exact field and amount)?
4. What C-1 deduction does the winner (Gm) receive, and at which code location?
5. After all adjustments, what is the final score of each?

Document the full scoring breakdown (in the report — not in source code comments).
This audit must use field values, not string parsing.

---

## Step 2 — Assess fix options

Three options to close the 0.53 gap. Assess each before implementing:

**Option A — Increase the C-1 deduction**
The kCleanQualities deduction that fired in C-1 is currently −0.50. If the gap is
0.53, increasing this deduction to ≥ 0.54 (above the gap) would flip the winner.
Risk: any other region where this deduction fires could be affected. Check how many
regions across the Baroque corpus trigger the C-1 guard — print the stem, measure,
beat, and deduction amount for every trigger. If the trigger is rare and the flip
is always correct, this is low-risk.

**Option B — Add a direct bonus for confirmed first-inversion HalfDim**
Instead of penalising the winner further, add a bonus to the HalfDim candidate
when:
- All 4 chord tones confirmed present (same condition as C-1 guard)
- Bass PC is m3 or b5 or m7 of the HalfDim root (genuine inversion, not root position)
This is a positive reward rather than a penalty, which is easier to reason about.
Risk: if the bonus is too large, it may flip cases where the bass-root reading
(Gm) is genuinely correct.

**Option C — Exempt confirmed first-inversion HalfDim from kNonBassPenalty**
The kNonBassPenalty = 0.35 applied to Eø7 because rootPc ≠ bassPc. If all 4
chord tones are confirmed AND the bass is a legitimate chord tone (not a coincident
passing note), exempting from kNonBassPenalty is defensible. This reclaims 0.35
of the 0.53 gap — not enough alone, but combined with the existing C-1 deduction
it may be sufficient.

For each option, print the projected score of Gm and Eø7 after the change, and
the projected score for any other corpus region where the condition fires. Choose
the option with the narrowest applicability (fewest triggers) and the cleanest
logic. Do not combine options unless one option alone is insufficient.

---

## Step 3 — Implement the chosen fix

Implement the chosen option in `chordanalyzer.cpp`. The guard condition must use
structured PC arithmetic only — no quality string parsing, no Roman numeral
inference. The condition for "first-inversion HalfDim with all chord tones
confirmed" has already been implemented in C-1; reuse or extend that code path.

If Option A: change the deduction constant. Check whether it's a named constant
or a literal; if a literal, introduce a named constant.
If Option B: add the bonus adjacent to where other inversion bonuses are applied
(read supportsContextualInversionBonuses logic for context).
If Option C: add an exemption predicate before the kNonBassPenalty application.

---

## Step 4 — Build

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Verify binary timestamp > source timestamp.

---

## Step 5 — Spot-check bwv187.7

Regenerate only bwv187.7 if partial corpus run is supported; otherwise full corpus.

```python
import json
from pathlib import Path
data = json.loads((Path('tools/corpus') / 'bwv187.7.ours.json').read_text(encoding='utf-8'))
r = next((r for r in data['regions']
          if r.get('measureNumber') == 14 and abs(r.get('beat', 0) - 2.0) < 0.05), None)
if r:
    print(f"winner: root={r['rootPitchClass']} qual={r['quality']!r} "
          f"score={r.get('chordScore',0):.4f} bassIsRoot={r['bassIsRoot']}")
    for i, a in enumerate(r.get('alternatives', [])[:3]):
        print(f"alt[{i}]: root={a['rootPitchClass']} qual={a['quality']!r} "
              f"score={a.get('score',0):.4f}")
```

Expected: winner is Eø7 (root=4, HalfDiminished, bassIsRoot=false).

---

## Step 6 — Run full Baroque corpus and measure BIR

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected:
- BIR=true:  7 → 6 (bwv187.7 fixed)
- BIR=false: 132 → ≤ 132 (no regressions)

Hard stops:
- BIR=false increases by > 5: revert and investigate
- BIR=true increases: revert immediately

---

## Step 7 — Jazz validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz BIR=false hard stop: ≤ 75 (current 12).

Restore Baroque after:
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

Expected: 407/407 and 53/53.

Pipeline snapshots: if bwv187.7 now wins as Eø7, the pipeline test will fail.
Verify the change is correct, then refresh goldens only for confirmed improvements:
```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 9 — Commit (if BIR=false ≤ 132 and tests pass)

```bash
git add src/composing/analysis/chord/chordanalyzer.cpp
# If pipeline goldens updated:
# git add src/notation/internal/  (or wherever goldens live)
git commit -m "Composing: close first-inversion HalfDim scoring gap (bwv187.7)

[Option A/B/C — fill in chosen option description].

bwv187.7 m=14: Gm (bassIsRoot=true) → Eø7 (first-inversion HalfDim).
All 4 chord tones confirmed present; bass is m3 of Eø7 root.

BIR=true: 7 → N  BIR=false: 132 → N  Jazz BIR=false: 12 → N"
```

---

## Step 10 — Report to Cowork

```
Step 1 — Scoring anatomy for bwv187.7:
  Gm:  rawScore=N  bassRootBonus=+N  C-1 deduction=−N  finalScore=N
  Eø7: rawScore=N  nonBassPenalty=−N  [any bonus]=+N  finalScore=N
  Gap before fix: 0.53

Step 2 — Option chosen: [A / B / C]
  Rationale: [one sentence]
  Corpus triggers of the guard condition: N regions
  [List any triggers other than bwv187.7 with stem, m=N, correct/regression?]

Step 5 — Spot-check bwv187.7 m=14 b=2.0:
  Winner after: root=N qual=Q bassIsRoot=[yes/no] score=N

Step 6 — Baroque BIR:
  BIR=true:  7 → N  (expected 6)
  BIR=false: 132 → N

Step 7 — Jazz BIR=false: N

Step 8 — Tests:
  composing: N/407
  notation: N/53
  Pipeline snapshots: [N updated / no change / failed]

Step 9 — Committed: [yes — hash] / [not committed — reason]

Remaining genuine-BIR=true after this fix:
  bwv187.7: [fixed / not fixed — reason]
  Hypothesis A (Round 3 merge, 5 cases): pending Iter 62
  bwv244.15: Correct cluster (label disagreement)
  bwv38.6:   pcWeight cluster (B below 0.2 threshold)
  Cluster B: 3 cases
  Cluster C: 2 cases
  Total: N
```
