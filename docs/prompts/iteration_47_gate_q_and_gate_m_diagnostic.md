# Iteration 47: Gate Q + Gate M — combined diagnostic

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=21, BIR=false=128. Jazz hard stop: BIR=false ≤ 75.

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.

---

## Background

Post-Iter-46 genuine-21 has two actionable clusters:

**Gate Q — HalfDiminished first-inversion over Minor6 root-position (7 cases)**
Pitch-class identity: Xm6 {X, m3, P5, M6} = Yø7/X {Y, X, m3, P5} where Y=(X−3)%12.
The Iter 46 scoring extension brought HalfDim inversions into results[]; Gate Q
promotes them when harmonic context supports the inversion reading.

**Gate M — tied Minor root-position vs Minor inversion (7 cases, margin=0.000)**
All seven cases show exactly tied scores between root-position Minor and an
inverted Minor reading. After Iter 46, inversions can accumulate enough bonus
points to tie root-position candidates — temporal/metric context is the only
available tiebreaker. This has transformed Gate M from a high-FP pattern into
a potentially zero-FP zero-margin gate.

Both diagnostics must be completed before any implementation is planned.

---

## PART 1 — Gate Q Diagnostic

### Step 1 — Confirm quality strings and alt structure for Gate Q cases

For each of the 7 Cluster A genuine cases, print winner + all alternatives.
Confirm the exact quality strings and that the HalfDim alt is now in results[]:

```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')

CLUSTER_A = [
    ('bwv259',  8, 1.0, 'bwv259'),
    ('bwv335',  8, 1.0, 'bwv335'),
    ('bwv78.7', 16, 1.0, 'bwv78.7'),
    ('bwv84.5',  5, 1.0, 'bwv84.5'),
    ('bwv90.5',  8, 2.0, 'bwv90.5-a'),
    ('bwv90.5', 12, 2.0, 'bwv90.5-b'),
    ('bwv96.6',  2, 1.0, 'bwv96.6'),
]

for stem, meas, beat, label in CLUSTER_A:
    fpath = CORPUS / f'{stem}.ours.json'
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            wRootPc = r.get('rootPitchClass', -1)
            wBassPc = r.get('bassPitchClass', -1)
            target_rootPc = (wRootPc - 3 + 12) % 12
            print(f'\n{label}  m={meas} b={beat}')
            print(f'  winner: quality={r.get("quality")!r} rootPc={wRootPc} '
                  f'bassPc={wBassPc} bassIsRoot={r.get("bassIsRoot")} '
                  f'score={r.get("chordScore"):.4f}')
            print(f'  (target alt: HalfDim rootPc={target_rootPc} bassPc={wBassPc})')
            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                flag = ''
                if (a.get('rootPitchClass') == target_rootPc and
                        a.get('bassPitchClass') == wBassPc):
                    flag = '  ← GATE Q TARGET'
                print(f'  alt[{i}]: quality={a.get("quality")!r} '
                      f'rootPc={a.get("rootPitchClass")} '
                      f'bassPc={a.get("bassPitchClass")} '
                      f'bassIsRoot={a.get("bassIsRoot")} '
                      f'score={a.get("score"):.4f} margin={margin:.4f}{flag}')
            break
```

Report:
- Exact winner quality string (e.g., "Minor", "Minor6", "MinorSixth" — note any variation)
- Exact HalfDim quality string
- How many of 7 have the HalfDim alt in results[] now?
- Is alt.bassIsRoot consistently False?
- Margin range across the genuine cases with the alt present

### Step 2 — Full Baroque corpus FP scan for Gate Q

Using the exact quality strings from Step 1:

```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')
WINNER_QUALITY = '???'   # from Step 1 — winner quality
ALT_QUALITY    = '???'   # from Step 1 — HalfDim quality string

GENUINE = {
    ('bwv259',  8, 1.0),
    ('bwv335',  8, 1.0),
    ('bwv78.7', 16, 1.0),
    ('bwv84.5',  5, 1.0),
    ('bwv90.5',  8, 2.0),
    ('bwv90.5', 12, 2.0),
    ('bwv96.6',  2, 1.0),
}

matches = []
for fpath in sorted(CORPUS.glob('*.ours.json')):
    stem = fpath.stem.replace('.ours', '')
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r.get('quality') != WINNER_QUALITY:
            continue
        if not r.get('bassIsRoot', False):
            continue
        wRootPc = r.get('rootPitchClass', -1)
        wBassPc = r.get('bassPitchClass', -1)
        wScore  = r.get('chordScore', 0.0)
        target  = (wRootPc - 3 + 12) % 12
        meas = r.get('measureNumber', -1)
        beat = r.get('beat', -1.0)

        for a in r.get('alternatives', []):
            if (a.get('quality') == ALT_QUALITY and
                    a.get('bassPitchClass') == wBassPc and
                    a.get('rootPitchClass') == target):
                margin = wScore - a.get('score', 0.0)
                if margin <= 0.50:
                    is_genuine = (stem, meas, beat) in GENUINE
                    matches.append({
                        'stem': stem, 'meas': meas, 'beat': beat,
                        'wRootPc': wRootPc, 'wBassPc': wBassPc,
                        'margin': margin, 'genuine': is_genuine,
                    })
                break

genuine_found = [x for x in matches if x['genuine']]
fp_list       = [x for x in matches if not x['genuine']]

print(f'Gate Q scan (≤ 0.50):')
print(f'  Genuine: {len(genuine_found)} / {len(GENUINE)}')
print(f'  FP: {len(fp_list)}')
print('\nFP list:')
for x in fp_list:
    print(f'  {x["stem"]:<20} m={x["meas"]:>3} b={x["beat"]:.1f} '
          f'margin={x["margin"]:.4f}')

for t in [0.35, 0.20, 0.10]:
    fp_t  = [x for x in fp_list       if x['margin'] <= t]
    gen_t = [x for x in genuine_found if x['margin'] <= t]
    print(f'\nAt ≤ {t}: genuine={len(gen_t)} FP={len(fp_t)}')
```

Report:
- FP count at each threshold
- Whether a threshold exists where genuine ≥ 5 and FP ≤ 2
- Full FP list with raw values

If FP > 3 at all thresholds: STOP for Gate Q. Do not proceed to Step 3.

### Step 3 — Temporal context for Gate Q matches

For all matches (genuine + FP), print temporal fields:

```python
TEMPORAL = ['nextRootPc', 'previousRootPc', 'previousQuality',
            'previousBassPc', 'bassIsStepwiseFromPrevious',
            'bassIsStepwiseToNext', 'consecutiveBassStepwiseCount',
            'regionMetricWeight']

print('\nTemporal context — Gate Q matches:')
for x in matches:
    fpath = CORPUS / f'{x["stem"]}.ours.json'
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == x['meas'] and abs(r['beat'] - x['beat']) < 0.15:
            label = 'GENUINE' if x['genuine'] else 'FP'
            print(f'\n{label}  {x["stem"]} m={x["meas"]} b={x["beat"]:.1f}  '
                  f'margin={x["margin"]:.4f}')
            for f in TEMPORAL:
                print(f'  {f}: {repr(r.get(f, "MISSING"))}')
            break
```

Report any temporal fields that cleanly separate genuine from FP.

---

## PART 2 — Gate M Diagnostic

### Step 4 — Print Gate M case details

The 7 Gate M cases all have margin=0.000. After Iter 46, the alt is Minor with
same rootPc but different bassPc (an inversion). Print full details for each:

```python
GATE_M = [
    ('bwv187.7',  14, 2.0, 'bwv187.7'),
    ('bwv227.11', 10, 3.0, 'bwv227.11'),
    ('bwv278',     8, 2.0, 'bwv278'),
    ('bwv301',     2, 3.0, 'bwv301'),
    ('bwv302',     1, 4.0, 'bwv302'),
    ('bwv40.6',   14, 2.0, 'bwv40.6'),
    ('bwv85.6',    5, 1.0, 'bwv85.6'),
]

print('Gate M cases (margin=0.000):')
for stem, meas, beat, label in GATE_M:
    fpath = CORPUS / f'{stem}.ours.json'
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r['measureNumber'] == meas and abs(r['beat'] - beat) < 0.15:
            print(f'\n{label}  m={meas} b={beat}')
            print(f'  winner: quality={r.get("quality")!r} '
                  f'rootPc={r.get("rootPitchClass")} '
                  f'bassPc={r.get("bassPitchClass")} '
                  f'bassIsRoot={r.get("bassIsRoot")} '
                  f'score={r.get("chordScore"):.4f}')
            for i, a in enumerate(r.get('alternatives', [])):
                margin = r.get('chordScore', 0) - a.get('score', 0)
                print(f'  alt[{i}]: quality={a.get("quality")!r} '
                      f'rootPc={a.get("rootPitchClass")} '
                      f'bassPc={a.get("bassPitchClass")} '
                      f'bassIsRoot={a.get("bassIsRoot")} '
                      f'score={a.get("score"):.4f} margin={margin:.4f}')
            # Also print temporal fields
            for f in TEMPORAL:
                print(f'  {f}: {repr(r.get(f, "MISSING"))}')
            break
```

Report for each case:
- The alt's quality, rootPc, bassPc, bassIsRoot — confirm it is a Minor inversion
  (same rootPc as winner, different bassPc, bassIsRoot=False) or a different chord
- Whether margin is exactly 0.0000 or very close
- All temporal fields

### Step 5 — Gate M FP scan (margin=0.000 exact-tie cases)

The zero-margin condition is an extremely precise trigger. Scan for all corpus
regions where winner=Minor/bassIsRoot=true AND alt=Minor at the same rootPc but
different bassPc AND margin ≤ 0.001 (effectively exact ties only):

```python
GATE_M_GENUINE = {
    ('bwv187.7',  14, 2.0),
    ('bwv227.11', 10, 3.0),
    ('bwv278',     8, 2.0),
    ('bwv301',     2, 3.0),
    ('bwv302',     1, 4.0),
    ('bwv40.6',   14, 2.0),
    ('bwv85.6',    5, 1.0),
}

TIE_THRESHOLD = 0.001   # near-zero only

gate_m_matches = []
for fpath in sorted(CORPUS.glob('*.ours.json')):
    stem = fpath.stem.replace('.ours', '')
    data = json.loads(fpath.read_text(encoding='utf-8'))
    for r in data.get('regions', []):
        if r.get('quality') != 'Minor':
            continue
        if not r.get('bassIsRoot', False):
            continue
        wRootPc = r.get('rootPitchClass', -1)
        wBassPc = r.get('bassPitchClass', -1)
        wScore  = r.get('chordScore', 0.0)
        meas = r.get('measureNumber', -1)
        beat = r.get('beat', -1.0)

        for a in r.get('alternatives', []):
            if (a.get('quality') == 'Minor' and
                    a.get('rootPitchClass') == wRootPc and
                    a.get('bassPitchClass') != wBassPc):
                margin = wScore - a.get('score', 0.0)
                if abs(margin) <= TIE_THRESHOLD:
                    is_genuine = (stem, meas, beat) in GATE_M_GENUINE
                    gate_m_matches.append({
                        'stem': stem, 'meas': meas, 'beat': beat,
                        'wRootPc': wRootPc, 'wBassPc': wBassPc,
                        'altBassPc': a.get('bassPitchClass'),
                        'altBassIsRoot': a.get('bassIsRoot'),
                        'margin': margin,
                        'genuine': is_genuine,
                    })
                break

gm_genuine = [x for x in gate_m_matches if x['genuine']]
gm_fp      = [x for x in gate_m_matches if not x['genuine']]

print(f'\nGate M scan (exact tie ≤ 0.001):')
print(f'  Genuine: {len(gm_genuine)} / 7')
print(f'  FP: {len(gm_fp)}')
print('\nFP list:')
for x in gm_fp:
    print(f'  {x["stem"]:<20} m={x["meas"]:>3} b={x["beat"]:.1f} '
          f'wRoot={x["wRootPc"]} wBass={x["wBassPc"]} '
          f'altBass={x["altBassPc"]} margin={x["margin"]:.6f}')
```

Report: FP count at the exact-tie threshold. If FP ≤ 2 at margin ≤ 0.001:
Gate M is viable without any temporal guard (the tie condition is selective enough).
If FP > 2: report the FP list and check whether temporal signals separate them.

---

## Step 6 — Report to Cowork

```
PART 1 — Gate Q:

Step 1 — Quality strings and alt presence:
  Winner quality string: "[exact]"
  HalfDim quality string: "[exact]"
  Cases with HalfDim alt in results[]: N / 7
  Alt.bassIsRoot: [consistently False / other]
  Margin range (genuine cases with alt): [min] to [max]

Step 2 — FP scan:
  At ≤ 0.50: genuine=N  FP=N
  At ≤ 0.35: genuine=N  FP=N
  At ≤ 0.20: genuine=N  FP=N
  At ≤ 0.10: genuine=N  FP=N
  Best threshold (genuine ≥ 5, FP ≤ 2): [N or "none"]
  [FP list]

Step 3 — Temporal signals:
  Signals separating genuine from FP: [describe or "none"]

Gate Q viability: [VIABLE — threshold=N / BLOCKED — reason]

PART 2 — Gate M:

Step 4 — Case details:
  Alt confirmed as same-rootPc Minor inversion: [yes / no — describe]
  Margin: [exact 0.0000 for all / varies]
  Temporal fields pattern: [describe]

Step 5 — FP scan (exact tie ≤ 0.001):
  Genuine: N / 7
  FP: N
  [FP list]
  Does tie condition alone separate genuine from FP? [yes / no]

Gate M viability: [VIABLE — tie alone sufficient / VIABLE — tie + temporal guard /
                  BLOCKED — reason]
```

Do NOT implement any gate. Do NOT modify chordanalyzer.cpp. Do NOT commit.
