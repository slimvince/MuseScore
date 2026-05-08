# Iteration 32: Gate L — Augmented root-position → same-root Major (TYPE-A quality correction)

## Background

Post-Iter 30 baseline: BIR=true=52, BIR=false=787.

The Iter 31 re-characterization identified 4 Cat 1 Augmented→Major cases where our
analyzer outputs an Augmented root-position chord but the reference says the same root
in Major quality:

| File      | m  | b   | Winner | Alt | Margin | Key  |
|-----------|----|-----|--------|-----|--------|------|
| bwv144.6  | 15 | 2.0 | B+     | B   | +0.30  | Bmin |
| bwv245.15 | 16 | 4.0 | E+     | E   | +0.30  | Cmaj |
| bwv312    |  7 | 3.0 | E+     | E   | +0.24  | Cmaj |
| bwv245.37 | 16 | 4.0 | F+     | F   | +0.30  | FDor |

All four are TYPE-A errors (same root, same bass, different quality). The correct
chord is Major at the same root; the Augmented alt is already present in results[].

This iteration: diagnostic first, then implement Gate L if false positive risk is low.

---

## Step 1 — Context loading

Read these two files before doing anything else:

1. `C:\s\MS\CLAUDE.md` — standing instructions
2. `C:\s\MS\build_and_test.md` — authoritative commands and baselines

Confirm stated baselines: BIR=true=52, BIR=false=787.

---

## Step 2 — Confirm corpus is current

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=52, BIR=false=787. If different, regenerate:

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

---

## Step 3 — Diagnostic: false positive risk for Gate L

Before implementing, scan the full corpus to find every region where:
- Winner is Augmented, bassIsRoot=true (our analyzer chose Augmented root-position)
- A Major alt exists in results[] at the **same root** (same rootPc as winner) and
  **same bass** (bassPc == winner's bassPc, i.e. alt is also root-position)
- Margin ≤ 0.40

For each such region, record whether it is a BIR=true error (we need to fix it) or
a BIR=false region (we are correct — Augmented IS right). The false positive risk is
the count of BIR=false regions that Gate L would fire on and incorrectly promote to Major.

Run this script from `C:\s\MS`:

```python
import json, glob, os, re

NOTE_TO_PC = {'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,'E':4,'F':5,
              'F#':6,'Gb':6,'G':7,'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}

def parse_root(sym):
    m = re.match(r'^([A-G][b#]?)', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else -1

def parse_bass(sym):
    m = re.search(r'/([A-G][b#]?)$', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else parse_root(sym)

# Load the BIR=true error set (files where we have a known error)
# We'll use the analyze_inversion_errors approach: compare our JSON to music21 JSON
bir_true_set = set()  # (bwv, measure, beat) tuples
for f in sorted(glob.glob('tools/corpus/*.ours.json')):
    bwv = os.path.basename(f).replace('.ours.json', '')
    ref_f = f.replace('.ours.json', '.music21.json')
    if not os.path.exists(ref_f):
        continue
    ours = json.load(open(f))
    ref  = json.load(open(ref_f))
    ref_map = {}
    for r in ref.get('regions', []):
        ref_map[(r['measureNumber'], round(r['beat'], 2))] = r
    for r in ours.get('regions', []):
        if not r.get('bassIsRoot', False):
            continue
        key2 = (r['measureNumber'], round(r['beat'], 2))
        if key2 not in ref_map:
            continue
        rr = ref_map[key2]
        if rr.get('bassIsRoot', True):
            continue  # reference also says root-position → not a BIR=true error
        bir_true_set.add((bwv, r['measureNumber'], round(r['beat'], 2)))

print(f"BIR=true error set size: {len(bir_true_set)}\n")

# Now scan for Gate L candidate fires (Augmented winner + same-root Major alt)
hits_error   = []  # would-fix BIR=true cases
hits_correct = []  # would-break BIR=false cases (false positives)

THRESHOLD = 0.40

for f in sorted(glob.glob('tools/corpus/*.ours.json')):
    bwv = os.path.basename(f).replace('.ours.json', '')
    data = json.load(open(f))
    for r in data.get('regions', []):
        if not r.get('bassIsRoot', False):
            continue
        if r.get('quality', '') != 'Augmented':
            continue
        wb = r.get('bassPitchClass', -1)
        wr = parse_root(r.get('chordSymbol', ''))
        ws = r.get('chordScore', 0)
        key = r.get('key', '?')

        for i, alt in enumerate(r.get('alternatives', [])):
            asym = alt.get('chordSymbol', '')
            ar = parse_root(asym)
            ab = parse_bass(asym)
            # Major quality: no '+', no 'm', no 'dim', no 'aug', no '7' suffix for
            # minor-family chords. Simplest check: symbol matches root only or root+extensions
            # A plain Major chord symbol is just the root note (possibly with Maj7 etc.)
            # We want Major quality specifically: check that it's NOT Augmented/Minor/Dim
            is_major_quality = ('+' not in asym and 'm' not in asym.lower()[:2]
                                and 'dim' not in asym.lower() and 'aug' not in asym.lower()
                                and 'sus' not in asym.lower())
            # More reliable: check that it contains no quality markers at all (plain Major)
            # or contains only 'Maj' (MajorSeventh etc.)
            # Actually quality field is in the JSON:
            aq = alt.get('quality', '')
            if aq != 'Major':
                continue
            if ar != wr:
                continue   # different root
            if ab != wb:
                continue   # not root-position alt
            margin = ws - alt.get('score', 0)
            if margin > THRESHOLD:
                continue

            beat_r = round(r['beat'], 2)
            key3 = (bwv, r['measureNumber'], beat_r)
            is_error = key3 in bir_true_set
            entry = (f"  {'ERROR ' if is_error else 'CORRECT'} "
                     f"bwv={bwv:12s} m={r['measureNumber']:3} b={r['beat']:.1f}  "
                     f"winner={r['chordSymbol']:8s} alt[{i}]={asym:8s}  "
                     f"margin={margin:+.3f}  key={key}")
            if is_error:
                hits_error.append(entry)
            else:
                hits_correct.append(entry)
            break   # only first qualifying alt per region

print(f"Gate L would FIX {len(hits_error)} BIR=true error(s):")
for e in hits_error:
    print(e)

print(f"\nGate L would BREAK {len(hits_correct)} BIR=false correct case(s) [FALSE POSITIVES]:")
for e in hits_correct:
    print(e)

print(f"\nSummary: fixes={len(hits_error)}, false_positives={len(hits_correct)}")
```

**Hard stop**: if `false_positives > 0`, STOP and report the full list. Do not implement
Gate L until a refined condition is found.

If `false_positives == 0` and `fixes >= 3`, proceed to Step 4.

---

## Step 4 — Read chordanalyzer.cpp before writing

Read `src/composing/analysis/chord/chordanalyzer.cpp`. Report:

A. The line number where Gate K ends (its closing `}`) — Gate L inserts immediately after.
B. Confirm the exact field access for `winner.identity.rootPc` and `winner.identity.bassPc`
   (same accessor pattern used in Gate K).
C. Confirm `ChordQuality::Major` is the correct enum name (it should be — used in Gate I/K).
D. The `scale[]` array form used in Gate I/K for diatonic checking — confirm it is
   `scale[inv.identity.rootPc]` vs `scale[rootPc]` (exact variable name).

---

## Step 5 — Implement Gate L

Insert Gate L immediately after Gate K (after its closing `}`).

### Entry condition (ALL required)

```cpp
if (originalWinnerQuality == ChordQuality::Augmented
    && winnerBassIsRoot
    && results.size() >= 2
    && keyTonicPc >= 0)
{
```

### Search loop

Iterate `results[1..]` for candidate `inv` satisfying ALL:

1. `inv.identity.quality == ChordQuality::Major`
2. `inv.identity.rootPc == winner.identity.rootPc` — same root as winner
3. `inv.identity.bassPc == winner.identity.bassPc` — same bass (alt is root-position)
4. Root diatonic to key: `scale[inv.identity.rootPc] != 0`
   (reuse the same `scale` array already built for Gate I/K in this scope)
5. `winner.identity.score - inv.identity.score <= 0.35f`

On first match: `std::swap(results[0], results[iIdx]); break;`

### Rationale

All 4 targets have margin ≤ 0.30; threshold 0.35 adds headroom. The same-root same-bass
condition (conditions 2+3) restricts the gate to TYPE-A quality substitution at root
position, avoiding inversion ambiguity. The diatonic check prevents spurious fires on
chromatic passing augmented chords whose root is non-scale.

---

## Step 6 — Build and run all tests

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Expected: build pass (warnings only), 407/407, 53/53, 11/11.
**Any failure: STOP and report verbatim.**

---

## Step 7 — Run corpus analysis

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report new BIR=true and BIR=false.

**Hard stops:**
- **If BIR=false > 787: STOP and report verbatim. Do not proceed.**
- **If BIR=true improvement < 3: STOP** — report which target cases were and were
  not fixed, with their actual margins from the Step 3 diagnostic.

---

## Step 8 — Update pipeline snapshot goldens if clean

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Confirm all 11/11 pass after golden update.

---

## Step 9 — Update baselines and STATUS.md

Update `build_and_test.md`: new BIR=true and BIR=false counts, Iter 32 attribution.

Update `STATUS.md`:
```
Iter 32: Gate L — Augmented root-position → same-root Major (TYPE-A quality correction)
- Pattern: Augmented root-position winner (e.g. E+) beats correct Major at same root (E)
  at small margin; Cat 1 / TYPE-A quality error. Seen in Bmin, Cmaj, FDor contexts.
- Fix: Gate L promotes Major alt when same root, same bass (root-position), diatonic,
  quality==Major, margin ≤ 0.35. Inserted after Gate K.
- Targets: bwv144.6 B+→B (Bmin), bwv245.15 E+→E (Cmaj), bwv312 E+→E (Cmaj),
  bwv245.37 F+→F (FDor). Expected 4 fixes.
- Diagnostic confirmed 0 false positives at threshold 0.35 across full Baroque corpus.
- Net improvement: BIR=true 52→N
- BIR=false: N (was 787)
- New baselines: BIR=true=N, BIR=false=N
```

---

## Step 10 — Commit and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 32: Gate L — Augmented root-pos → same-root Major TYPE-A correction [N BIR=true fixes, M remaining]" && git push
```

---

## Step 11 — Report

```
Step 2 baseline:     BIR=true=N, BIR=false=N (expected 52, 787)

Step 3 diagnostic:
  Gate L would fix: N BIR=true errors
  Gate L false positives: N BIR=false cases (expected 0)
  [full list of both]

Step 4 findings:
  Gate K ends at line N; Gate L inserted at lines N–N
  ChordQuality::Major confirmed: yes
  scale[] accessor: scale[inv.identity.rootPc]

Build:               pass
Composing tests:     407/407
Notation tests:      53/53
Pipeline snapshots:  11/11

BIR=true:            N  (was 52, improved by N)
BIR=false:           N  (was 787)

Gate L fixes:
  bwv144.6  m=15 b=2: [fixed / not fixed — reason if not]
  bwv245.15 m=16 b=4: [fixed / not fixed]
  bwv312    m=7  b=3: [fixed / not fixed]
  bwv245.37 m=16 b=4: [fixed / not fixed]

GitHub push:         done — [commit hash]
```
