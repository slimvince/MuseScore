# Iteration 63: Update baselines, enumerate BIR=false=125, re-characterize genuine BIR=true=6

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=6, BIR=false=125. Jazz BIR=false=12.
(Established by Iter 61 commit a34dba041e; confirmed by Iter 62.)

Build fresh before every BIR measurement. Verify binary is newer than source.

Do NOT change any source code. Documentation and diagnostic only.

---

## Background

Iter 61 committed the first-inversion HalfDim scoring fix and moved BIR=true
7→6, BIR=false 132→125. The prior cluster map (Hypothesis A ×5, bwv244.15
Correct, bwv38.6 pcWeight, Cluster B ×3, Cluster C ×2) is stale — segmentation
boundary shifts from Iter 61 mean per-region identities no longer map 1:1 to
the old enumeration.

This iteration:
1. Updates `build_and_test.md` with new baselines.
2. Enumerates the new BIR=false=125 baseline (standing practice).
3. Fresh-characterizes all 6 remaining BIR=true cases.

---

## Step 1 — Confirm corpus is current

```bash
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Must show BIR=true=6, BIR=false=125. If not, regenerate:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

---

## Step 2 — Update build_and_test.md

Update the baseline section:
- Baroque BIR=true:  6  (was 14 after Iter 46; 7 after Iter 60)
- Baroque BIR=false: 125 (was 132 after Iter 54/55)
- Jazz BIR=false:    12  (unchanged)
- Commits producing these baselines: a34dba041e (Iter 61), ee337aeca4 (Iter 62)
- Baroque regression tolerance: investigate if BIR=false > 135 (125 + 10)
- Update BIR=false enumeration file reference (Step 3 below)

---

## Step 3 — Enumerate BIR=false=125 baseline

Run `tools/diag_iter54_bir_false_enumerate.py` (or equivalent) against the
current corpus and save:

```bash
cd C:\s\MS && python tools/diag_iter54_bir_false_enumerate.py \
    > tools/birfalse_baseline_iter61.txt
```

Confirm the file contains exactly 125 lines (excluding comments/blanks).

Format per case (matching prior enumeration files):
```
stem  measureNumber  beat  ourRootPc  ourQuality  agreedRootPc
```

---

## Step 4 — Extract and print all 6 BIR=true cases

Using `tools/iter54_genuine14_characterization.py` (or equivalent), extract
the current genuine BIR=true=6 cases. Print for each:

```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')

# First: identify all 6 BIR=true cases from analyze_inversion_errors.py
# output. If the script does not list individual cases, read its source
# and add a --verbose flag or equivalent to print each case.

# For each case print:
for stem, meas, beat in GENUINE_6:
    fpath = CORPUS / f'{stem}.ours.json'
    data = json.loads(fpath.read_text(encoding='utf-8'))
    r = next((r for r in data.get('regions', [])
               if r.get('measureNumber') == meas
               and abs(r.get('beat', 0) - beat) < 0.05), None)
    if not r:
        print(f'{stem} m={meas} b={beat}: region not found')
        continue
    print(f'\n=== {stem} m={meas} b={beat:.2f} ===')
    print(f'  winner: root={r["rootPitchClass"]} qual={r["quality"]!r} '
          f'score={r.get("chordScore",0):.4f} '
          f'bass={r["bassPitchClass"]} bassIsRoot={r["bassIsRoot"]}')
    print(f'  pcSet: {r.get("pitchClassSet")}  '
          f'dur={r.get("endTick",0)-r.get("startTick",0)} ticks')
    for i, a in enumerate(r.get('alternatives', [])[:3]):
        print(f'  alt[{i}]: root={a["rootPitchClass"]} '
              f'qual={a["quality"]!r} score={a.get("score",0):.4f}')
    # Print 2 neighbours each side
    regions = data.get('regions', [])
    idx = regions.index(r) if r in regions else -1
    if idx >= 0:
        for nb in regions[max(0,idx-2):idx+3]:
            if nb is r: continue
            print(f'  neighbour: m={nb["measureNumber"]} b={nb.get("beat",0):.2f} '
                  f'root={nb["rootPitchClass"]} qual={nb["quality"]!r} '
                  f'dur={nb.get("endTick",0)-nb.get("startTick",0)}')
```

---

## Step 5 — Assign each case to a cluster

For each of the 6 cases, determine which cluster it belongs to using structured
fields only. Use these cluster definitions:

**Hypothesis A** — boundary split: target region has ≤ 3 PCs; a missing chord
tone appears in a short (dur < DIVISION/2) immediately-adjacent region. The
correct chord would be identifiable from the union of the two regions.

**Scoring gap** — full correct PC set present, correct chord appears in
alternatives[] but scores below the winner. Report the margin.

**pcWeight** — a structural chord tone present in the pcMask (bitfield) but
below the 0.2 weight threshold; the analyzer's effective PC set is incomplete.

**Cluster B** — prior characterization: [read tools/iter54_genuine14_characterization.txt
to recall what Cluster B was — do not infer from chord symbol strings].

**Cluster C** — prior characterization: [same — read the file].

**Correct** — our analyzer is right; the ground-truth annotation appears to
be for a different voicing or the reference sources disagree.

**Unknown** — none of the above applies; needs deeper investigation.

For each case report:
- Cluster assignment and one-sentence evidence
- Whether this case appeared in the prior genuine-14/genuine-7 list
  (cross-reference tools/iter54_genuine14_characterization.txt by stem+measure)
- Whether a fix is visible from the current evidence

---

## Step 6 — Save characterization

Save full output to `tools/iter63_genuine6_characterization.txt`.

Format:
```
=== Genuine BIR=true=6 — Iter 63 characterization ===
Baselines: BIR=true=6  BIR=false=125  (commit a34dba041e)

[For each case:]
stem m=N b=N
  winner: root=N qual=Q score=N bassIsRoot=[T/F]
  pcSet: 0xHHHH  dur=N ticks
  agreed root: N
  alts: [list top 3]
  cluster: [Hypothesis A / Scoring gap / pcWeight / Cluster B / Cluster C /
            Correct / Unknown]
  evidence: [one sentence]
  in prior genuine-14: [yes — was m=N b=N / no — new case]
  fix visible: [yes — describe / no / investigate]

Summary:
  Hypothesis A:   N cases
  Scoring gap:    N cases
  pcWeight:       N cases
  Cluster B:      N cases
  Cluster C:      N cases
  Correct:        N cases
  Unknown:        N cases
```

---

## Step 7 — Commit

```bash
git add build_and_test.md
git add tools/birfalse_baseline_iter61.txt
git add tools/iter63_genuine6_characterization.txt
git commit -m "Iter 63: update baselines (BIR=true=6 BIR=false=125) + enumerate + re-characterize

Post Iter 61 (a34dba041e) and Iter 62 (ee337aeca4).

New baselines:
  Baroque BIR=true:  7 → 6
  Baroque BIR=false: 132 → 125
  Jazz BIR=false:    12 (unchanged)

BIR=false=125 enumerated: tools/birfalse_baseline_iter61.txt
Genuine BIR=true=6 re-characterized: tools/iter63_genuine6_characterization.txt"
```

---

## Step 8 — Report to Cowork

```
Step 1 — Corpus confirmed: BIR=true=6  BIR=false=125

Step 3 — BIR=false=125 enumeration:
  tools/birfalse_baseline_iter61.txt: [yes — N lines]

Step 5 — Genuine BIR=true=6 cluster breakdown:
  [For each case:]
  stem m=N b=N — cluster: X — evidence: [one sentence]
  fix visible: [yes — describe / no / investigate]

  Summary:
    Hypothesis A:   N
    Scoring gap:    N
    pcWeight:       N
    Cluster B:      N
    Cluster C:      N
    Correct:        N
    Unknown:        N

Step 7 — Committed: [yes — hash] / [not committed — reason]

Recommended next iterations (in priority order):
  1. [highest-leverage fixable cluster — N cases]
  2. ...
```
