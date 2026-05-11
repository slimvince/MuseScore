# Iteration 59: Fix Hypothesis C — add HalfDim candidate generation for full-PC-set regions

## Standing rule — no symbol inference

**No chord symbol string parsing. No Roman numeral inference. Structured fields only.**

Read `C:\s\MS\CLAUDE.md` and `C:\s\MS\build_and_test.md` first.
Baselines: BIR=true=14, BIR=false=132. Jazz BIR=false=12.

Build fresh before every BIR measurement. Verify binary is newer than source.

---

## Background

Iter 58 identified two root causes for the 8 Blocker C genuine-14 cases:

**Hypothesis A (4 cases)** — greedy boundary split. The erroneous region is missing
a chord tone that sits in an immediately-preceding short region (dur ≈ 1 tick).
Fix: Round 3 merge (Iter 60).

**Hypothesis C (4 cases)** — candidate generator restriction. The region's
`pitchClassSet` contains the full HalfDim PC set (e.g. `{C#, E, G, B}` = C#m7b5),
yet the generator produces only same-root Minor and same-root Diminished candidates
— it does NOT enumerate "root PC + m3 + b5 + m7 → HalfDim" as a candidate.

HalfDim does appear in the corpus (484 winners, 693 alts), so this is not a global
bug — it is a missing enumeration path for regions where the bass PC happens to be
the HalfDim root and the full seventh-chord set is present.

This iteration implements the Hypothesis C fix only. Hypothesis A (Round 3 merge)
is deferred to Iter 60.

---

## Step 1 — Locate the candidate generation code

Read `src/composing/chordanalyzer.cpp`. Search for the section that builds the
candidate list for a region — it will iterate over pitch classes or chord types
and call something like `analyzeChord`, `scoreChord`, or emit entries into a
`results` or `candidates` vector.

Specifically locate:
1. Where Diminished candidates are generated (root + m3 + b5).
2. Whether there is an adjacent enumeration for HalfDim (root + m3 + b5 + m7).
3. If HalfDim is enumerated at all, under what condition — is it conditional on
   a minimum PC count, a minimum voice count, or some other guard that the
   affected regions fail?

Print the relevant code section (file path and line range) before making any change.

---

## Step 2 — Understand the failing condition

For bwv244.44, the region has `pitchClassSet = {C#, E, G, B}` — exactly the
C#m7b5 set. Our output is same-root Diminished (C#dim = {C#, E, G}). The
HalfDim candidate (C#m7b5) is absent from `alternatives[]`.

Before modifying anything, instrument the candidate generator to trace what it
does for this specific region:

```bash
# Locate the bwv244.44 region at m=5 b=1.0 in the corpus JSON
python - <<'EOF'
import json
from pathlib import Path
r = next((r for r in json.loads(
    (Path('tools/corpus') / 'bwv244.44.ours.json').read_text()
    )['regions']
    if r.get('measureNumber') == 5 and abs(r.get('beat', 0) - 1.0) < 0.05), None)
if r:
    print(f"pitchClassSet: {r.get('pitchClassSet')}")
    print(f"winner: root={r.get('rootPitchClass')} qual={r.get('quality')!r}")
    print(f"alts ({len(r.get('alternatives',[]))} total):")
    for a in r.get('alternatives', []):
        print(f"  root={a.get('rootPitchClass')} qual={a.get('quality')!r} score={a.get('score',0):.4f}")
EOF
```

Then read the candidate generation code and trace why C#m7b5 is not produced.
Document the finding: is it a missing branch, a guard condition, or a data issue?

---

## Step 3 — Implement the fix

The fix must enumerate a HalfDim candidate for any pitch class P in the region's
set when the set contains all four of: P, P+3 (m3), P+6 (b5), P+10 (m7)
(all mod 12). Add this enumeration adjacent to the existing Diminished enumeration.

**Locate the right insertion point.** The fix belongs in the candidate enumeration
loop, not in the scoring function. Do not modify scoring weights — add only the
missing candidate to the pool so that the existing scoring and ranking logic can
evaluate it on equal terms with other candidates.

Pseudocode intent:
```
for each pitchClass P in region.pitchClassSet:
    if {P, P+3, P+6, P+10} ⊆ region.pitchClassSet:
        add candidate: root=P, quality=HalfDim (or "m7b5" — use the exact
        quality string the codebase uses for HalfDim; check existing HalfDim
        entries in the corpus to confirm the string)
```

Read the actual data structures in `chordanalyzer.cpp` and implement the fix
using those structures. Do not guess at type names — read the code first.

Confirm the quality string for HalfDim by examining a corpus JSON that already
contains a HalfDim result:
```bash
python - <<'EOF'
import json
from pathlib import Path
for jpath in sorted(Path('tools/corpus').glob('*.ours.json')):
    data = json.loads(jpath.read_text())
    for r in data.get('regions', []):
        for a in r.get('alternatives', []):
            if 'half' in str(a.get('quality','')).lower():
                print(jpath.name, r.get('measureNumber'), a.get('quality'))
                raise SystemExit
EOF
```

---

## Step 4 — Build

```bash
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Fix any compile errors. Do not change the scoring logic, the gate thresholds,
or any file outside `src/composing/`. Verify binary timestamp > source timestamp.

---

## Step 5 — Spot-check the 4 Hypothesis C cases

Before running the full corpus, spot-check the 4 Hypothesis C cases:

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus \
    --filter bwv187.7 bwv244.15 bwv244.44 bwv38.6
```

If `--filter` is not supported, run the full corpus (Step 6 handles this).

For each of the 4 cases, print the winner and top-3 alternatives:
```python
import json
from pathlib import Path

CORPUS = Path('tools/corpus')
CASES = [
    ('bwv187.7',  14, 2.0),
    ('bwv244.15',  5, 1.0),
    ('bwv244.44',  5, 1.0),
    ('bwv38.6',    7, 3.0),
]

for stem, meas, beat in CASES:
    fpath = CORPUS / f'{stem}.ours.json'
    if not fpath.exists():
        print(f'{stem}: not in corpus — skipping')
        continue
    data = json.loads(fpath.read_text(encoding='utf-8'))
    r = next((r for r in data.get('regions', [])
               if r.get('measureNumber') == meas and abs(r.get('beat', 0) - beat) < 0.05),
              None)
    if not r:
        print(f'{stem} m={meas} b={beat}: region not found')
        continue
    print(f'\n{stem} m={meas} b={beat}:')
    print(f'  winner: root={r.get("rootPitchClass")} qual={r.get("quality")!r} '
          f'score={r.get("chordScore",0):.4f} bassIsRoot={r.get("bassIsRoot")}')
    for i, a in enumerate(r.get('alternatives', [])[:5]):
        print(f'  alt[{i}]: root={a.get("rootPitchClass")} qual={a.get("quality")!r} '
              f'score={a.get("score",0):.4f}')
```

Expected: the HalfDim candidate now appears in `alternatives[]` for each case.
If it appears but does not win, note the margin — a gate or scoring adjustment
may be needed in a follow-up iteration.

---

## Step 6 — Run full Baroque corpus and measure BIR

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

**Expected outcome:**
- BIR=true: 14 → 10 (the 4 Hypothesis C cases fixed, if HalfDim now wins)
- BIR=false: 132 → ≤ 132 (no new regressions; small improvement possible)

**Hard stops:**
- BIR=false increases by > 5: revert and investigate which chords became HalfDim incorrectly
- BIR=true increases: revert immediately

If HalfDim appears in `alternatives[]` but does not win (Step 5 showed it ranked
below Diminished), note the margin. A scoring bias toward Diminished over HalfDim
when both fit the PC set may need a tie-breaking rule (e.g. prefer the fuller
chord when the seventh PC is present and unambiguous). Do NOT add such a rule in
this iteration — report it and defer to Iter 60 characterization.

---

## Step 7 — Run Jazz corpus validation

```bash
cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz \
    --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Jazz BIR=false hard stop: ≤ 75 (current 12, so any increase warrants inspection).

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

Expected: 407/407 and 53/53. If pipeline snapshot tests fail, inspect whether
the changes are genuine improvements (HalfDim now wins where Diminished won before).
If so, refresh goldens:
```bash
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Only refresh if each changed region is a confirmed improvement.

---

## Step 9 — Commit (only if BIR=false ≤ 132 and tests pass)

```bash
git add src/composing/chordanalyzer.cpp
git commit -m "Composing: enumerate HalfDim candidate for regions with full m7b5 PC set

Hypothesis C fix from Iter 58 Blocker C investigation.

4 of 8 Cluster A genuine-14 cases had the complete HalfDim pitch-class set
(root + m3 + b5 + m7) in the region but the candidate was not generated —
only same-root Minor and Diminished were enumerated. Added enumeration:
for each PC in the set, if {PC, PC+3, PC+6, PC+10} ⊆ set, add HalfDim
candidate rooted at PC.

BIR=true: 14 → N  BIR=false: 132 → N  Jazz BIR=false: 12 → N"
```

---

## Step 10 — Report to Cowork

```
Step 2 — Failing condition identified:
  [Describe why HalfDim was not generated — missing branch / guard condition / other]
  Code location: [file, line range]

Step 5 — Spot-check (4 Hypothesis C cases):
  bwv187.7 m=14 b=2.0: HalfDim in alts [yes/no] — wins [yes/no] — margin N
  bwv244.15 m=5 b=1.0:  HalfDim in alts [yes/no] — wins [yes/no] — margin N
  bwv244.44 m=5 b=1.0:  HalfDim in alts [yes/no] — wins [yes/no] — margin N
  bwv38.6   m=7 b=3.0:  HalfDim in alts [yes/no] — wins [yes/no] — margin N

Step 6 — Baroque BIR:
  BIR=true:  14 → N  (expected 10 if all 4 win)
  BIR=false: 132 → N  (hard stop: > 137)
  Interpretation: [N cases fixed / HalfDim appears but doesn't win: scoring bias]

Step 7 — Jazz BIR=false: N (hard stop ≤ 75)

Step 8 — Tests:
  composing: N/407
  notation: N/53
  Pipeline snapshots: [refreshed N / no change / failed]

Step 9 — Committed: [yes — hash] / [not committed — reason]

Remaining genuine-14 after this fix:
  Hypothesis A cases (need Iter 60 Round 3 merge): 4
  Residual Cluster A (HalfDim appears but doesn't win): N
  Cluster B: 3
  Cluster C: 2
  Total: N
```
