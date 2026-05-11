# Iteration 60: Fix bwv187.7 (kCleanQualities + alt cap), re-characterize 3 misclassified cases

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=14, BIR=false=132. Jazz BIR=false=12.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Iter 59 diagnostic found that Iter 58's "Hypothesis C" cluster of 4 cases was wrong
for 3 of the 4. Only bwv187.7 (m=14 b=2.0) is a genuine first-inversion HalfDim
failure. The other 3 (bwv244.15, bwv244.44, bwv38.6) have distinct root causes that
need separate re-characterization.

**bwv187.7 root cause** — three conspiring issues:
1. Bass-root bonus (+0.70) on Gm vs non-bass-penalty (−0.35) on Eø7: ~1.05 score swing.
2. HalfDiminished excluded from `kCleanQualities`, so the inversion-correction step
   cannot promote first-inversion Eø7 even when all 4 chord tones are present.
3. `batch_analyze` alternative output cap = 2, dropping Eø7 (ranked #4 in rawCandidates,
   above the 0.75-ratio threshold but below the results[] cap).

**Misclassified 3:**
- bwv244.15 m=5 b=1.0: PCs {D,F#,A,B} — Bm7/D6 pair, no HalfDim subset.
- bwv244.44 m=5 b=1.0: Only 3 PCs {D,F#,B} — plain Bm triad; the Iter 58 PC report
  was incorrect or from a different corpus state.
- bwv38.6 m=7 b=3.0: B falls below pcWeight threshold 0.2; analyzer sees {C,D,F,A},
  Dm7 is the correct identification of what the analyzer receives. Root cause is
  pcWeight aggregation upstream.

This iteration:
1. Fixes bwv187.7 (C-1: kCleanQualities, C-2: alt cap 2→3).
2. Re-characterizes bwv244.15, bwv244.44, bwv38.6 to assign them to correct clusters.

---

## Fix C-1 — Add HalfDim to kCleanQualities with inversion guard

Read `src/composing/analysis/chord/chordanalyzer.cpp` lines 2039–2042 (the
`kCleanQualities` definition and the inversion-correction step that uses it).

The fix: add `ChordQuality::HalfDiminished` to `kCleanQualities` **conditionally** —
only when:
- The region's pitch-class set contains all four of the candidate HalfDim chord tones:
  root, root+3, root+6, root+10 (mod 12).
- The bass pitch class is one of {root+3, root+6, root+10} (i.e., a genuine inversion,
  not a root-position HalfDim with a wrong bass reading).

Do not add HalfDim unconditionally to `kCleanQualities` — that would allow the
inversion-correction to promote any HalfDim candidate regardless of PC evidence.

Implementation options (read the surrounding code and choose the one that fits the
existing pattern):
- Add a special-cased branch inside the inversion-correction loop for
  `ChordQuality::HalfDiminished` that applies the above two-condition guard before
  promoting.
- Or, compute a filtered set `kCleanQualitiesForThisRegion` that includes
  HalfDiminished only when the two conditions are met, then use it as before.

In either case, the guard must use structured PC arithmetic, not string parsing.

---

## Fix C-2 — Raise batch_analyze alternative output cap from 2 to 3

Read `tools/batch_analyze.cpp` line 2238 (the cap on alternative entries emitted
into the JSON output). Raise the cap from 2 to 3.

This is a JSON format change only — it does not affect winner selection or scoring.
Effect: `alternatives[]` in corpus JSON will contain up to 3 entries instead of 2.
This helps `analyze_inversion_errors.py` see more of the candidate pool, and it
was the reason Eø7 was invisible in the corpus JSON for bwv187.7 despite being
above the ratio threshold.

Verify that `analyze_inversion_errors.py` and `compare_analyses.py` handle
`alternatives[]` with 3 entries correctly (they should already, since they iterate
over the array rather than indexing by position).

---

## Step 1 — Implement C-1 and C-2, then build

Make both changes. Build:
```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Fix any compile errors. Verify binary timestamp > source timestamp.

---

## Step 2 — Spot-check bwv187.7

Run the full Baroque corpus (or just bwv187.7 if partial run is supported):
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
```

Then check bwv187.7 m=14 b=2.0:
```python
import json
from pathlib import Path
data = json.loads((Path('tools/corpus') / 'bwv187.7.ours.json').read_text(encoding='utf-8'))
r = next((r for r in data['regions']
          if r.get('measureNumber') == 14 and abs(r.get('beat', 0) - 2.0) < 0.05), None)
if r:
    print(f"winner: root={r['rootPitchClass']} qual={r['quality']!r} "
          f"score={r.get('chordScore',0):.4f} bassIsRoot={r['bassIsRoot']}")
    for i, a in enumerate(r.get('alternatives', [])[:5]):
        print(f"alt[{i}]: root={a['rootPitchClass']} qual={a['quality']!r} "
              f"score={a.get('score',0):.4f}")
```

Expected: winner is Eø7 (root=4, quality HalfDiminished), bassIsRoot=false.

If Gm still wins: report the winner score and Eø7 score after the C-1 fix.
The non-bass penalty may still be large enough to prevent Eø7 from winning even
after the inversion-correction step can promote it. In that case, C-1 is necessary
but not sufficient — report the remaining gap for Iter 61 to address with a
targeted scoring adjustment.

---

## Step 3 — Measure BIR

```bash
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected:
- BIR=true: 14 → 13 (bwv187.7 fixed) if Eø7 now wins; 14 if it appears in alts only.
- BIR=false: 132 → ≤ 132 (no regressions).

Hard stops:
- BIR=false increases by > 5: revert C-1 and investigate.
- BIR=true increases: revert immediately.

---

## Step 4 — Jazz validation

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

## Step 5 — Re-characterize the 3 misclassified cases

Using the Baroque corpus (just regenerated), print the full region detail for each
of the 3 misclassified cases. The goal is to assign each to the correct cluster and
determine whether a fix is viable.

```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')
CASES = [
    ('bwv244.15',  5, 1.0, 'misclassified: Bm7/D6 pair'),
    ('bwv244.44',  5, 1.0, 'misclassified: plain Bm triad (3 PCs)'),
    ('bwv38.6',    7, 3.0, 'misclassified: pcWeight threshold drops B'),
]

for stem, meas, beat, note in CASES:
    fpath = CORPUS / f'{stem}.ours.json'
    data = json.loads(fpath.read_text(encoding='utf-8'))
    print(f'\n=== {stem} m={meas} b={beat:.1f} ({note}) ===')
    # Print the target region and its neighbours
    regions = data.get('regions', [])
    for i, r in enumerate(regions):
        if abs(r.get('measureNumber', 0) - meas) <= 1:
            print(f"  [idx={i}] m={r['measureNumber']} b={r.get('beat',0):.2f} "
                  f"dur={r.get('endTick',0)-r.get('startTick',0)} "
                  f"root={r['rootPitchClass']} qual={r['quality']!r} "
                  f"bass={r['bassPitchClass']} bassIsRoot={r['bassIsRoot']} "
                  f"score={r.get('chordScore',0):.4f} "
                  f"pcMask={r.get('pitchClassSet')}")
            for j, a in enumerate(r.get('alternatives', [])[:3]):
                print(f"    alt[{j}]: root={a['rootPitchClass']} "
                      f"qual={a['quality']!r} score={a.get('score',0):.4f}")
```

For each case, determine and document:
- **bwv244.15**: Is this a Bm7 in first inversion (correct winner) or a genuine error?
  What does music21+DCML agree the root is?
- **bwv244.44**: With only 3 PCs, is the Bm triad reading correct, or is this a region
  that should have been merged with an adjacent region to get the full chord? Check
  adjacent regions for the missing m7 PC.
- **bwv38.6**: Is the pcWeight threshold (0.2) dropping B correct behaviour here, or
  is B a genuine structural note being discarded? Print the raw voice/weight data
  if accessible from the corpus JSON.

Then assign each to one of:
- **Correct** — our analyzer is right, the BIR=true classification is wrong (music21
  or DCML annotation issue). Mark for re-examination of the ground truth.
- **Hypothesis A** — boundary/merge issue; the correct chord tone is in an adjacent
  short region. Will be addressed by Round 3 merge (Iter 61+).
- **Scoring** — full PC set present, but scoring/penalty prevents correct winner.
- **pcWeight** — a structural note is below the weight threshold; fix requires
  changing the aggregation logic.
- **Unknown** — needs further investigation.

Save this re-characterization to `tools/iter60_misclassified_recharacterization.txt`.

---

## Step 6 — Run both test suites

```bash
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

Expected: 407/407 and 53/53.

Pipeline snapshot tests: if bwv187.7's winner changes from Gm to Eø7, the pipeline
test for that score will fail. Verify the change is correct before refreshing:
```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

If only bwv187.7-related failures appear and the new output (Eø7) is verified correct,
refresh goldens:
```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 7 — Commit (if BIR=false ≤ 132 and tests pass)

```bash
git add src/composing/analysis/chord/chordanalyzer.cpp
git add tools/batch_analyze.cpp
git add tools/iter60_misclassified_recharacterization.txt
# If pipeline goldens refreshed:
# git add src/notation/internal/  (or wherever goldens live)
git commit -m "Composing: fix first-inversion HalfDim (kCleanQualities guard) + raise alt cap

C-1: Add HalfDim to inversion-correction when all 4 chord tones present and
bass is m3/b5/m7 of candidate HD root. Target: bwv187.7 m=14 (Eø7/G).
C-2: Raise batch_analyze alternative output cap 2→3.

BIR=true: 14 → N  BIR=false: 132 → N  Jazz BIR=false: 12 → N"
```

---

## Step 8 — Report to Cowork

```
C-1 (kCleanQualities guard):
  Code location: chordanalyzer.cpp lines N–N
  Guard conditions used: [describe]

C-2 (alt cap):
  batch_analyze.cpp line N: cap raised 2 → 3

Spot-check — bwv187.7 m=14 b=2.0:
  Winner before: Gm root=7 score=2.8875
  Winner after:  [root=N qual=Q score=N] bassIsRoot=[yes/no]
  Eø7 in alts: [yes / still not visible]

Baroque BIR:
  BIR=true:  14 → N
  BIR=false: 132 → N

Jazz BIR=false: N

Tests:
  composing: N/407
  notation: N/53
  Pipeline snapshots: [N updated / no change / failed — describe]

Re-characterization (3 misclassified cases):
  bwv244.15 m=5 b=1.0: cluster = [Correct / Hyp A / Scoring / pcWeight / Unknown]
    [one sentence evidence]
  bwv244.44 m=5 b=1.0: cluster = [Correct / Hyp A / Scoring / pcWeight / Unknown]
    [one sentence evidence]
  bwv38.6   m=7 b=3.0: cluster = [Correct / Hyp A / Scoring / pcWeight / Unknown]
    [one sentence evidence]

Files saved:
  tools/iter60_misclassified_recharacterization.txt: [yes]

Committed: [yes — hash] / [not committed — reason]

Revised genuine-14 breakdown after this iteration:
  Fixed this iteration: N
  Hypothesis A (boundary split, needs Round 3 merge): 4
  bwv244.15: [cluster]
  bwv244.44: [cluster]
  bwv38.6:   [cluster]
  Cluster B: 3
  Cluster C: 2
  Total remaining BIR=true: N
```
