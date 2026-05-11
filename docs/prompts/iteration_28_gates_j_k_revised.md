# Iteration 28: Gates J and K — Revised (vi-chord restriction + corrected threshold)

## Background

Iter 27 attempt failed:
- **Gate J** (Major+I3): +159 BIR=false regressions at threshold 0.35. Root cause:
  the C↔Am/C (I↔vi/I) ambiguity is common in Bach, but the vast majority of
  cases are *correctly* Major root-position. Gate J needs an additional
  discriminating condition.
- **Gate K** (Augmented+MinMaj7): +2 BIR=false with only 5 fixes at threshold 0.50.
  Post-mortem: the two primary targets (bwv40.3 D+→GmMaj7/D and bwv64.8
  F#+→BmMaj7/F#) both have margin=**0.503**, just above the 0.50 cutoff, so they
  were NOT fixed. The 5 "fixes" came from a broader implementation than specified.

**Corpus is currently stale**: code is at Iter 25 (commit a74f26aeeb, Gate I only)
but corpus JSONs reflect the aborted Iter 27 Gate K run; `analyze_inversion_errors.py`
reads 48 BIR=true instead of the correct baseline of 53. Step 1 must restore it.

---

## Step 1 — Restore corpus to Iter 25 baseline

Re-run the corpus analysis to regenerate clean JSONs against the current binary
(Gate I only):

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

**Expected**: BIR=true=53, BIR=false=787.
If different, STOP and report.

---

## Step 2 — Targeted diagnostic: Gate K targets

Before implementing Gate K, extract the margin data for all Augmented
root-position winner cases where the alt is Minor+MajorSeventh at I7 interval.
Write (or run inline in Python) this script:

```python
import json, glob, os, re

NOTE_TO_PC = {'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,'E':4,'F':5,
              'F#':6,'Gb':6,'G':7,'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}

def parse_root(sym):
    m = re.match(r'^([A-G][b#]?)', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else -1

def parse_bass(sym):
    m = re.search(r'/([A-G][b#]?)$', sym)
    if m: return NOTE_TO_PC.get(m.group(1), -1)
    return parse_root(sym)

for f in sorted(glob.glob('tools/corpus/*.ours.json')):
    bwv = os.path.basename(f).replace('.ours.json','')
    data = json.load(open(f))
    for r in data.get('regions', []):
        if not r.get('bassIsRoot'): continue
        wq = r.get('quality','')
        if wq != 'Augmented': continue
        wb = r.get('bassPitchClass', -1)
        ws = r.get('chordScore', 0)
        for i, alt in enumerate(r.get('alternatives', [])):
            asym = alt.get('chordSymbol','')
            if 'mMaj7' not in asym: continue
            ab = parse_bass(asym)
            ar = parse_root(asym)
            if ab != wb: continue          # same bass
            if ar != (wb+5)%12: continue   # I7 interval
            margin = ws - alt.get('score', 0)
            print(f"{bwv:15s} m={r['measureNumber']:3} b={r['beat']}  "
                  f"{r['chordSymbol']:10s} → {asym:15s}  alt_idx={i}  margin={margin:+.3f}")
            break
```

Run and capture full output. This shows the exact margin for each genuine
Gate K target after the corpus is clean.

---

## Step 3 — Implement Gate K (Augmented + MinMaj7/I7, threshold 0.55)

Insert Gate K after Gate I (currently the last gate).

### Entry condition (ALL required)
- `originalWinnerQuality == ChordQuality::Augmented`
- `winnerBassIsRoot == true`
- `results.size() >= 2`
- `keyTonicPc >= 0`

### Search loop

Iterate `results[1..]` for candidate `inv` satisfying ALL:

1. `inv.identity.bassPc == winner.identity.bassPc` — same bass
2. `inv.identity.rootPc == (winner.identity.bassPc + 5) % 12` — I7 interval
   (alt root is a perfect fourth above bass; bass is the fifth of the alt root)
3. `inv.identity.quality == ChordQuality::Minor` **AND**
   `hasExtension(inv.identity.extensions, Extension::MajorSeventh)` — genuine
   MinorMajorSeventh chord. **Do NOT match plain Minor without MajorSeventh.**
4. Alt root diatonic to key (reuse the same `scale` array from Gate I)
5. `winner.identity.score − inv.identity.score <= 0.55f`

On first match: swap `results[0]` and `results[iIdx]`, break.

**Rationale for 0.55**: the two primary targets (bwv40.3, bwv64.8) have
margin=0.503; 0.55 covers them with headroom. Adjust up if the Step 2 diagnostic
reveals targets with larger margins, or down if BIR=false rises.

---

## Step 4 — Implement Gate J (Major + vi-chord I3, threshold 0.35)

Insert Gate J immediately after Gate K.

### The design fix from Iter 27

The original Gate J produced +159 false positives because ANY Major chord can
have a Minor I3 alt nearby. The discriminating condition that eliminates nearly
all false positives: **the alt's root must be the natural vi chord (scale degree 6)
of the current key**, i.e. `inv.identity.rootPc == (keyTonicPc + 9) % 12`.

Mathematically: combining the I3 interval condition
`(winner.bassPc − inv.rootPc + 12) % 12 == 3` with `inv.rootPc == (keyTonicPc+9)%12`
and `winnerBassIsRoot==true` implies `winner.rootPc == keyTonicPc` — the gate
fires **only when the winner is the tonic I chord** and the alt is specifically
the vi chord (relative minor) in first inversion at the tonic bass. This is the
classic I↔vi/I ambiguity (C vs Am/C, G vs Em/G, F vs Dm/F, E vs C#m/E).

All 6 documented target cases satisfy this condition.

### Entry condition (ALL required)
- `originalWinnerQuality == ChordQuality::Major`
- `winnerBassIsRoot == true`
- `results.size() >= 2`
- `keyTonicPc >= 0`

### Search loop

Iterate `results[1..]` for candidate `inv` satisfying ALL:

1. `inv.identity.bassPc == winner.identity.bassPc` — same bass
2. `inv.identity.bassPc != inv.identity.rootPc` — alt is NOT root-position
3. `(winner.identity.bassPc − inv.identity.rootPc + 12) % 12 == 3` — I3 interval
4. `inv.identity.rootPc == (keyTonicPc + 9) % 12` — **vi-chord restriction**:
   alt root is the natural minor sixth (relative minor) of the current key
5. `inv.identity.quality == ChordQuality::Minor ||
    inv.identity.quality == ChordQuality::MinorSeventh`
   (include minor seventh; use exact enum names confirmed in Iter 27 Step 2)
6. Alt root diatonic to key (reuse same `scale` array; with condition 4 this
   is almost always satisfied, but keep the check for safety)
7. `winner.identity.score − inv.identity.score <= 0.35f`

On first match: swap `results[0]` and `results[iIdx]`, break.

---

## Step 5 — Build and run all tests

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Expected: build pass (warnings only), 407/407, 53/53, 11/11.
Any failure: **STOP and report verbatim.**

---

## Step 6 — Run corpus analysis

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report new BIR=true and BIR=false.

**Hard stops:**
- **If BIR=false > 787: STOP and report verbatim.** Do not proceed.
- **If BIR=true improvement < 4: STOP** — report which target cases were
  and were not fixed, with their diagnostic details from Step 2.

If BIR=false is clean (≤787) and BIR=true improved by ≥4, continue.

---

## Step 7 — Update pipeline snapshot goldens if clean

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 8 — Update baselines and STATUS.md

Update `build_and_test.md` with actual new BIR counts and Iter 28 attribution.

Update `STATUS.md`:
```
Iter 28: Gates J and K — revised designs
- Gate K: Augmented root-position vs MinorMajorSeventh second-inversion (I7);
  threshold 0.55; strict MinMaj7 check (Minor quality + MajorSeventh extension);
  targets D+→GmMaj7/D, F#+→BmMaj7/F# pattern (augmented triad ⊂ MinMaj7)
- Gate J: Major root-position (tonic I only) vs vi-chord first-inversion (I3);
  threshold 0.35; vi-chord restriction: alt.rootPc==(keyTonicPc+9)%12 limits
  gate to I↔vi/I ambiguity (C vs Am/C, G vs Em/G, F vs Dm/F);
  eliminates the +159 false-positive explosion from Iter 27
- Net improvement: BIR=true 53→N
- BIR=false: N (was 787)
- New baselines: BIR=true=N, BIR=false=N
```

---

## Step 9 — Commit and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 28: Gates J+K revised — tonic-I↔vi/I (J) and Augmented+MinMaj7 (K) [N BIR=true fixes, M remaining]" && git push
```

---

## Step 10 — Report

```
Step 1 corpus restore:   BIR=true=N, BIR=false=N (expected 53, 787)

Step 2 Gate K targets found: N cases
  [list each file/measure/margin line from the diagnostic]

Gate K: inserted after Gate I; threshold 0.55; MinMaj7 check = Minor + MajorSeventh ext
Gate J: inserted after Gate K; threshold 0.35; vi-chord restriction inv.rootPc==(keyTonicPc+9)%12

Build:               pass
Composing tests:     407/407
Notation tests:      53/53
Pipeline snapshots:  11/11
BIR=true:            N  (was 53, improved by N)
BIR=false:           N  (was 787)

Gate K fixes: [list which bwv cases]
Gate J fixes: [list which bwv cases — confirm these are I↔vi/I at tonic]

GitHub push:         done — [commit hash]
```
