# Iteration 29: Augmented rooting diagnostic and Gate J regression analysis

## Background

Both Gate K and Gate J failed in Iter 28. Root causes are now understood:

**Gate K** was solving the wrong problem. The Augmented target cases are NOT
MinorMajorSeventh quality errors. They are **augmented chord rooting errors**:

| Our winner | Music21 reference | Key | M21 Roman numeral |
|-----------|------------------|-----|-------------------|
| D+   (root=D, bass=D) | Bb+/D (root=Bb, bass=D) | g minor | III+6 |
| F#+  (root=F#, bass=F#) | D+/F# (root=D, bass=F#) | e minor | bVII+6 |
| A+   (root=A, bass=A) | F+/A  (root=F, bass=A)  | d minor | III+6 |

All three have `(bass − correct_root + 12) % 12 == 4` — the same I4 interval
pattern as Gate I, but applied within Augmented chords rather than Minor→Major.
GmMaj7/D happens to share all three pitch classes of Bb+, which is why it
appeared as alt[0] in results[], but it is the wrong quality. The correct fix
is to promote Bb+/D (augmented inversion), not GmMaj7/D (MinMaj7).

**Gate J** has the right vi-chord restriction design but was guarded behind
`preferMinorOverMajorAdd6` (defaults to `false`; not set in Baroque preset).
CC added the guard because the vi-chord restriction alone caused +4 regressions
in the composing catalog tests (Jazz pieces). Those 4 regressions must be
understood before the guard can be removed or replaced with a targeted fix.

**This iteration is diagnostic only — zero code changes, no commit.**

---

## Step 1 — Restore corpus

The corpus JSON files for bwv40.3 and bwv64.8 are corrupted (JSON parse errors
from the stale Iter 28 Gate K run).

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=53, BIR=false=787.
If different, STOP and report.

---

## Step 2 — Augmented I4 inversion alt availability

For each primary target case, check whether the **correct augmented inversion**
alt (Bb+/D, D+/F#, F+/A) is present anywhere in our candidates —
in `results[]` AND in `rawCandidates` if accessible.

The correct alt for each case has:
- Same `bassPc` as our winner
- Quality = Augmented
- `bassPc != rootPc` (it IS an inversion)
- `(winner.bassPc − alt.rootPc + 12) % 12 == 4` (I4 interval)

Run this Python script to check the corpus JSON for visible alternatives:

```python
import json, re

NOTE_TO_PC = {'C':0,'C#':1,'Db':1,'D':2,'D#':3,'Eb':3,'E':4,'F':5,
              'F#':6,'Gb':6,'G':7,'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}

def parse_root(sym):
    m = re.match(r'^([A-G][b#]?)', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else -1

def parse_bass(sym):
    m = re.search(r'/([A-G][b#]?)$', sym)
    return NOTE_TO_PC.get(m.group(1), -1) if m else parse_root(sym)

# Primary Augmented targets: (file, measure, beat, expected_correct_alt_root_pc)
# correct alt root = (winner_bass + 8) % 12  (one augmented step below bass in
# the opposite direction: Bb=10=(D+8)%12, D=2=(F#+8)%12, F=5=(A+8)%12 — wait
# actually it's (winner_bass - 4 + 12) % 12 = (bass + 8) % 12)
TARGETS = [
    ('tools/corpus/bwv40.3.ours.json',  9,  1.0),
    ('tools/corpus/bwv64.8.ours.json',  9,  3.0),
    ('tools/corpus/bwv40.6.ours.json',  6,  1.0),
    ('tools/corpus/bwv48.7.ours.json',  7,  3.0),
    ('tools/corpus/bwv102.7.ours.json', 11, 2.0),
    ('tools/corpus/bwv309.ours.json',   12, 3.0),
    ('tools/corpus/bwv20.11.ours.json', 7,  3.0),
]

for fpath, m, b in TARGETS:
    data = json.load(open(fpath))
    for r in data.get('regions', []):
        if r['measureNumber'] == m and abs(r['beat'] - b) < 0.15:
            winner_sym = r['chordSymbol']
            bass = r['bassPitchClass']
            ws = r['chordScore']
            correct_root = (bass + 8) % 12   # I4 inversion: correct root is bass-4
            print(f"\n{fpath.split('/')[-1].replace('.ours.json','')} m={m} b={b}")
            print(f"  Winner: {winner_sym}  bass={bass}  key={r['key']}")
            print(f"  Seeking Augmented alt at I4: bassPc=={bass}, rootPc=={correct_root}")
            found = False
            for i, alt in enumerate(r.get('alternatives', [])):
                asym = alt['chordSymbol']
                ar = parse_root(asym)
                ab = parse_bass(asym)
                is_aug = '+' in asym and 'Maj' not in asym and 'Dim' not in asym
                if ab == bass and ar == correct_root and is_aug:
                    print(f"  FOUND at alt[{i}]: {asym}  score={alt['score']:.3f}  "
                          f"margin={ws-alt['score']:+.3f}")
                    found = True
            if not found:
                print(f"  NOT FOUND in alternatives. Alt list:")
                for i, alt in enumerate(r.get('alternatives', [])[:6]):
                    ar=parse_root(alt['chordSymbol'])
                    ab=parse_bass(alt['chordSymbol'])
                    print(f"    alt[{i}]: {alt['chordSymbol']:20s} score={alt['score']:.3f} "
                          f"rootPc={ar} bassPc={ab}")
            break
```

Additionally, for each NOT FOUND case: check `rawCandidates` if exposed in the
JSON, or note that it requires a C++ diagnostic.

---

## Step 3 — Gate J regression analysis

Implement Gate J **without** the `preferMinorOverMajorAdd6` guard (the vi-chord
restriction must stand on its own). Build and run composing tests only:

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

If composing tests fail, report verbatim for each failing test:
- Test name / file / measure / beat
- Expected chord symbol
- Actual chord symbol produced
- Key detected
- Winner and alt chord symbols and scores

Then revert Gate J immediately. Do not run corpus analysis.

**If composing tests all pass with the bare vi-chord restriction** (no preference
guard), that is the new baseline — report pass and do not revert.

---

## Step 4 — Report to Cowork

```
Step 1 corpus restore: BIR=true=N, BIR=false=N (expected 53, 787)

Step 2 — Augmented I4 alt availability:
  bwv40.3  m=9  b=1: [FOUND alt_idx=N score=X margin=+X] / [NOT FOUND, alts: ...]
  bwv64.8  m=9  b=3: [FOUND / NOT FOUND]
  bwv40.6  m=6  b=1: [FOUND / NOT FOUND]
  bwv48.7  m=7  b=3: [FOUND / NOT FOUND]
  bwv102.7 m=11 b=2: [FOUND / NOT FOUND]
  bwv309   m=12 b=3: [FOUND / NOT FOUND]
  bwv20.11 m=7  b=3: [FOUND / NOT FOUND]

  Summary: N/7 have correct augmented inversion alt in results[].
  Maximum margin among found cases: X (determines safe threshold).

Step 3 — Gate J composing test result:
  [PASS — vi-chord restriction alone is sufficient, no regressions]
  OR
  [FAIL — N failing tests, verbatim list follows:]
    Test: [name]
    Expected: [chord]  Actual: [chord]  Key: [key]
    Winner: [sym] score=X   Alt (vi inv): [sym] score=X  margin=X
    ...
```

Do not commit anything.
