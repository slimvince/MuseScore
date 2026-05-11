# Iteration 65: Fix bwv187.7 Gm6 winner + diagnose bwv43.11 sus2 candidate absence

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=6, BIR=false=125. Jazz BIR=false=12.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Iter 63 re-characterization identified two actionable scoring cases:

**Case [3] bwv187.7 m=14 b=2.0** — Scoring gap.
PCs={D,E,G,Bb}, bass=G. Winner: Gm6 (root=7, Minor6, bassIsRoot=true),
score=2.39. Alt[2]: Em7b5/G (root=4, HalfDim, first inversion), score=1.86.
Gap: 0.53. The Iter 61 fix added a HalfDim inversion bonus gated on
`preferMinorOverMajorAdd6`, but targeted Minor (not Minor6) winners. The winner
here is Minor6 — the same structural situation (bass is m3 of the HalfDim root,
all 4 chord tones present) but the winning quality differs.

**Case [6] bwv43.11 m=3 b=2.0** — Unknown / candidate generation.
PCs={D,E,A}, bass=D. Agreed root: D. Expected quality: sus2 (D=root, E=M2,
A=P5). Winner is not D-rooted. No D-rooted sus2 candidate appears in
alternatives[]. The full sus2 PC set IS present. This mirrors the Iter 59
HalfDim situation: the question is whether the sus2 template exists and is
enumerated, and if so, why it scores below the winner.

This iteration:
1. Extends the Iter 61 HalfDim inversion bonus to also fire when the winner
   is Minor6 (not just Minor). Targets bwv187.7. (Part A — code change.)
2. Diagnoses bwv43.11: checks sus2 template existence, enumeration, and
   scoring for {D,E,A}. (Part B — diagnostic only, no code change unless
   the fix is clearly safe and contained.)

---

## Part A — Extend HalfDim inversion bonus to Minor6 winner

### Step 1 — Read the Iter 61 guard

Read `src/composing/analysis/chord/chordanalyzer.cpp` lines 1994–2025
(the bestAltIdx loop and the isHalfDimInversion condition from Iter 61).
Confirm:
1. The exact quality check used to identify the winner as "Minor" — is it
   `ChordQuality::Minor`, or a broader check?
2. Whether extending it to `ChordQuality::MinorSixth` (or equivalent) is
   a one-line change or requires restructuring.
3. Whether the `preferMinorOverMajorAdd6` gate already applies, or needs
   to be added to the Minor6 branch.

### Step 2 — Implement

Extend the condition from `winner.quality == ChordQuality::Minor` to also
cover `ChordQuality::MinorSixth` (use the exact enum value from the codebase).
The structural guard conditions remain the same:
- All 4 HalfDim chord tones confirmed present (root, root+3, root+6, root+10)
- Bass PC is m3, b5, or m7 of the HalfDim candidate root
- Gated on `prefs.preferMinorOverMajorAdd6`

### Step 3 — Build and spot-check bwv187.7

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Regenerate bwv187.7 (or full corpus if partial run not supported) and check
m=14 b=2.0:

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

Expected: winner is Em7b5/G (root=4, HalfDiminished, bassIsRoot=false).

### Step 4 — Run full Baroque corpus and BIR

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true 6→5, BIR=false 125→≤125.
Hard stops: BIR=false increases > 5 — revert Part A. BIR=true increases — revert immediately.

Jazz validation:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```
Jazz BIR=false hard stop: ≤75 (current 12). Restore Baroque after.

### Step 5 — Run both test suites

```bash
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407, 53/53. If pipeline snapshots fail for bwv187.7 and the
new output is verified correct, refresh goldens.

---

## Part B — Diagnose bwv43.11 sus2 candidate absence (diagnostic only)

Do Part B whether or not Part A succeeded. These are independent.

### Step 6 — Check sus2 template existence

Read the template array in `chordanalyzer.cpp` (lines ~1654–1671). Report:
- Is there a sus2 template (intervals: 0, 2, 7 — root, M2, P5)?
- If yes: what is its index and what scoring weights does it carry?
- If no: sus2 is simply not in the candidate pool — that is the root cause.

### Step 7 — Trace bwv43.11 m=3 b=2.0

Print the current corpus detail:

```python
import json
from pathlib import Path
data = json.loads((Path('tools/corpus') / 'bwv43.11.ours.json').read_text(encoding='utf-8'))
r = next((r for r in data['regions']
          if r.get('measureNumber') == 3 and abs(r.get('beat', 0) - 2.0) < 0.05), None)
if r:
    print(f"winner: root={r['rootPitchClass']} qual={r['quality']!r} "
          f"score={r.get('chordScore',0):.4f} bassIsRoot={r['bassIsRoot']}")
    print(f"pcSet: {r.get('pitchClassSet')}  bass={r['bassPitchClass']}")
    for i, a in enumerate(r.get('alternatives', [])[:5]):
        print(f"alt[{i}]: root={a['rootPitchClass']} qual={a['quality']!r} "
              f"score={a.get('score',0):.4f}")
    # neighbours
    regions = data['regions']
    idx = next((i for i,x in enumerate(regions) if x is r), -1)
    for nb in regions[max(0,idx-2):idx+3]:
        if nb is r: continue
        print(f"nb: m={nb['measureNumber']} b={nb.get('beat',0):.2f} "
              f"root={nb['rootPitchClass']} qual={nb['quality']!r}")
```

### Step 8 — Determine root cause and fix direction

Based on Steps 6–7, report:

**If sus2 template is absent**: Adding it requires understanding the scoring
weight design. Do not add it in this iteration — report the finding and note
that adding sus2 to the template list is the fix direction for Iter 66.

**If sus2 template exists but D-rooted sus2 scores below winner**:
- What is the D-rooted sus2 score for {D,E,A}?
- What is the winner's score and quality?
- Is the gap fixable by a targeted bonus (similar to HalfDim or Gate I/K/L),
  or does the template scoring need adjustment?

**If sus2 template exists and scores well but is filtered out**: Identify the
filter (ratio threshold, results[] cap, distinctPcs guard).

Report findings. Implement a fix only if:
- The fix is contained to the sus2 case (no risk of broader regression)
- BIR=false does not increase
- Jazz baseline is preserved

Otherwise, document findings and defer the fix to Iter 66.

---

## Step 9 — Commit

If Part A succeeded and Part B is diagnostic only:
```bash
git add src/composing/analysis/chord/chordanalyzer.cpp
git commit -m "Composing: extend HalfDim first-inversion bonus to MinorSixth winners

bwv187.7 m=14: Gm6 (bassIsRoot=true) → Em7b5/G (HalfDim first inversion).
Extends Iter-61 guard from Minor to also cover MinorSixth winners when all
4 HalfDim chord tones confirmed and bass is m3/b5/m7 of HD root.
Gate: prefs.preferMinorOverMajorAdd6 (Baroque only).

BIR=true: 6 → N  BIR=false: 125 → N  Jazz BIR=false: 12 → N"

git push

If Part B also produced a committed fix, include it in the same commit or
a follow-up commit with its own message — followed by `git push`.

---

## Step 10 — Report to Cowork

```
Part A — bwv187.7 Gm6 → Em7b5/G:
  Guard extension: [one sentence — what changed]
  Spot-check winner after: root=N qual=Q bassIsRoot=[yes/no]
  Baroque BIR: BIR=true 6→N  BIR=false 125→N
  Jazz BIR=false: N
  Tests: composing N/407  notation N/53
  Committed: [yes — hash / not committed — reason]

Part B — bwv43.11 sus2 diagnosis:
  sus2 template in template list: [yes (index N, intervals N) / no]
  If yes — D-rooted sus2 score for {D,E,A}: N  winner score: N
  Root cause: [absent template / scoring gap / filtered out / other]
  Fix direction: [add template / scoring adjustment / filter change / unknown]
  Fix implemented this iteration: [yes — describe / no — deferred to Iter 66]

Remaining BIR=true after this iteration: N
```
