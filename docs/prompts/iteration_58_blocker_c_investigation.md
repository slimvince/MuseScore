# Iteration 58: Investigate Blocker C — HalfDim candidate absent for 8 Cluster A cases

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=14, BIR=false=132. Jazz BIR=false=12.

Build fresh before every BIR measurement. Verify binary is newer than source.

Do NOT change any source code. Diagnostic and documentation only.

---

## Background

The genuine-14 characterization (Iter 56) identified the following cluster structure:

- **Cluster A — 9 cases**: Minor-6 inversions where the correct root is the bass
  note of an Xm6 voicing. For 8 of these (Blocker C), our analyzer outputs a same-root
  Diminished chord at score 2.1000, and the correct HalfDim chord is **entirely absent**
  from `results[]` — it is not being generated at all, not merely ranked below Diminished.

The working hypothesis from Iter 56 is that greedy segmentation is fragmenting
the Xm6 chord at a boundary that falls between the bass note and the added sixth,
producing a region whose pitch-class set is incomplete. An incomplete pitch-class
set suppresses the HalfDim candidate from the candidate pool before scoring begins.

This is the highest-leverage investigation in genuine-14: if the cause is confirmed
and a fix is identified, it could address 8 cases simultaneously.

---

## Step 1 — Confirm corpus is current

```bash
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Must show BIR=true=14, BIR=false=132. If not, regenerate:
```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

---

## Step 2 — Identify the 8 Blocker C case locations

Read `tools/iter54_genuine14_characterization.txt`. Extract all Cluster A cases
where the HalfDim candidate is noted as absent from `results[]`. These are the
8 Blocker C cases. For each, record:
- stem (BWV filename stem)
- measureNumber
- beat
- our output rootPitchClass, quality
- agreed rootPitchClass (music21 + DCML)

Print a summary table before proceeding to Step 3.

---

## Step 3 — Print greedy region detail for each Blocker C case

For each of the 8 cases, load the current corpus JSON and print:

```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')

BLOCKER_C = [
    # Fill from Step 2 output
    # ('stem', measureNumber, beat),
]

for stem, meas, beat in BLOCKER_C:
    fpath = CORPUS / f'{stem}.ours.json'
    data = json.loads(fpath.read_text(encoding='utf-8'))
    print(f'\n=== BLOCKER C: {stem} m={meas} b={beat:.2f} ===')
    print(f'  (agreed root = ?, our root = ? dim)')

    # Print the erroneous region and its 2 neighbours on each side
    regions = data.get('regions', [])
    for i, r in enumerate(regions):
        if abs(r.get('measureNumber', 0) - meas) <= 2:
            dur_ticks = r.get('endTick', 0) - r.get('startTick', 0)
            print(f"  [region {i}] m={r['measureNumber']} b={r.get('beat', '?'):.2f} "
                  f"endTick={r.get('endTick')} dur={dur_ticks} "
                  f"root={r.get('rootPitchClass')} qual={r.get('quality')!r} "
                  f"bass={r.get('bassPitchClass')} bassIsRoot={r.get('bassIsRoot')} "
                  f"score={r.get('chordScore', 0):.4f} "
                  f"pcMask={r.get('pitchClassSet')}")
            alts = r.get('alternatives', [])
            for j, a in enumerate(alts[:5]):
                print(f"    alt[{j}]: root={a.get('rootPitchClass')} "
                      f"qual={a.get('quality')!r} "
                      f"score={a.get('score', 0):.4f}")
            if not alts:
                print(f"    (no alternatives)")
```

For each case, note:
- The `pitchClassSet` (bitmask) of the erroneous region — which pitch classes are present?
- How many pitch classes are in the set?
- Is the pitch class that would make the chord a HalfDim (the major 6th above the true bass)
  present in the pitchClassSet?
- Are there short neighbouring regions (dur < DIVISION) immediately before or after
  the erroneous region that might contain the missing pitch class?

---

## Step 4 — Check the score source for each case

For each Blocker C case, the relevant notes span a measure boundary or a short
duration. To understand what the greedy boundary split, check the actual note
content:

```python
import json
from pathlib import Path

# For each Blocker C case, examine the raw note events in the JSON.
# The corpus JSON may contain a 'noteEvents' or 'candidates' array — check what
# fields are present at the top level of the JSON.
CORPUS = Path('tools/corpus')
stem = BLOCKER_C[0][0]  # First case as example
fpath = CORPUS / f'{stem}.ours.json'
data = json.loads(fpath.read_text(encoding='utf-8'))
print('Top-level keys:', list(data.keys()))
```

If the JSON contains note-level event data, use it to reconstruct the sounding
pitch classes at the erroneous region's tick range. If not, note what is available.

The key question is: **Is the missing pitch class (M6 of the Xm6) actually sounding
during the erroneous region, but absent from its pitchClassSet?** Or is it in an
adjacent region?

---

## Step 5 — Hypothesis testing: boundary split vs accumulation gap

For each case, determine which hypothesis applies:

**Hypothesis A — Boundary split**: Greedy placed a boundary *within* the Xm6
chord, splitting it into two short regions. The first region has the bass + fifth
(looks like a Diminished fifth dyad), the second region has the added sixth. The
erroneous region is the first half, which genuinely lacks the sixth.

**Hypothesis B — Accumulation gap**: All pitch classes of the Xm6 are sounding
simultaneously in the region, but the pitch-class accumulation in the region's
`pitchClassSet` missed one note (e.g. because a voice enters on a subdivision
that was excluded by the note-change-event filter).

**Hypothesis C — Candidate generation threshold**: The pitch-class set is correct
but the HalfDim candidate is not generated because the scoring system requires a
minimum number of voices or some other structural condition not met.

To distinguish A from B: check the `pitchClassSet` bitmask of the neighbouring
regions. If the sixth appears in an adjacent region (especially a short one at
the same beat cluster), Hypothesis A is confirmed.

To distinguish B from C: if the pitchClassSet contains the required pitch classes
for HalfDim but the candidate is still absent, the issue is in candidate generation
logic, not segmentation.

Report which hypothesis applies to each of the 8 cases.

---

## Step 6 — Check candidate generation for HalfDim

If Hypothesis A or B is confirmed for any case, also check: for a region that
DOES contain the full Xm6 pitch-class set, does the analyzer generate a HalfDim
candidate? To verify this, find any other region in any chorale that has a
HalfDim in its `alternatives[]` and print its `pitchClassSet`. This confirms
that HalfDim candidate generation works when the full pitch-class set is present.

If no HalfDim appears in any region's alternatives across the entire corpus, that
points to Hypothesis C — a candidate generation bug independent of segmentation.

```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')
halfdim_found = []

for jpath in sorted(CORPUS.glob('*.ours.json')):
    data = json.loads(jpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        for a in r.get('alternatives', []):
            if 'half' in str(a.get('quality', '')).lower() or \
               'dim' in str(a.get('quality', '')).lower():
                halfdim_found.append((jpath.stem, r.get('measureNumber'),
                                      a.get('quality'), a.get('score')))

print(f'Regions with diminished/halfdim alternative: {len(halfdim_found)}')
for h in halfdim_found[:20]:
    print(f'  {h}')
```

---

## Step 7 — Determine fix direction

Based on the hypotheses confirmed above, report the fix direction for each case:

**If Hypothesis A (boundary split)**: The fix is to prevent greedy from splitting
a short Xm6 voicing. Options:
1. **Minimum-duration guard**: Do not place a Round 2 boundary if the resulting
   region would be shorter than DIVISION/2. Check if this would suppress the
   splitting boundary without losing legitimate short-chord boundaries.
2. **Round 3 merge**: After Round 2, merge adjacent short regions (dur < DIVISION)
   that have identical bass pitch class and differ only by the added sixth.
   This would reconstruct the full Xm6 pitch-class set.
3. **Boundary inhibition near Xm6 events**: Detect when a note-change tick is
   merely an added sixth above a sustained bass, and suppress it as a candidate
   boundary.

**If Hypothesis B (accumulation gap)**: The fix is in how pitch classes are
accumulated within a region. Check whether note-change-event tick selection
excludes some voice-entry ticks.

**If Hypothesis C (candidate generation)**: The fix is in the chord catalog or
candidate generation logic — HalfDim must be generated for any pitch-class set
containing a minor triad plus major sixth.

For each fix direction, estimate the risk of regressions on BIR=false (would the
fix cause new incorrect chords to appear as HalfDim when they should remain
Diminished?).

---

## Step 8 — Save findings

Save the full diagnostic output to:
```
tools/iter58_blocker_c_investigation.txt
```

Format:
```
=== Blocker C Investigation — Iter 58 ===

Cases examined: 8

[For each case:]
  stem m=N b=N
  Region pitchClassSet: 0xHHHH  PCs present: [list]
  Missing PC for HalfDim: [pitchClass]
  Hypothesis confirmed: [A / B / C]
  Evidence: [boundary split at tick N / accumulation gap / candidate generation]
  Neighbouring region with missing PC: [m=N b=N dur=N ticks / not found]

Summary:
  Hypothesis A (boundary split): N cases
  Hypothesis B (accumulation gap): N cases
  Hypothesis C (candidate generation): N cases
  Mixed: N cases

Recommended fix direction: [description]
Risk assessment: [low / medium / high — basis]
```

Do NOT modify any source code.

---

## Step 9 — Report to Cowork

```
Blocker C Investigation — Iter 58

Cases examined: 8 (all Cluster A HalfDim-absent cases from genuine-14)

Hypothesis breakdown:
  A — boundary split (greedy fragmented the Xm6):  N cases
  B — accumulation gap (sounding but not captured): N cases
  C — candidate generation (missing from pool):     N cases

[For each case:]
  stem m=N b=N
  pitchClassSet: 0xHHHH — missing PC N (the M6)
  Hypothesis: A / B / C
  Evidence: [one sentence]

HalfDim candidate found elsewhere in corpus: [yes / no]
  (If yes: confirms candidate generation works when full PC set present)
  (If no: points to candidate generation bug)

Recommended fix direction:
  [describe — Round 3 merge / duration guard / boundary inhibition / accumulation fix]
  Risk of BIR=false regression: [low / medium / high]

Files saved:
  tools/iter58_blocker_c_investigation.txt: [yes]

Source code modified: no
```
