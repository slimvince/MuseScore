# Iteration 25: Implement Gate I — prefer diatonic first-inversion over root-position minor

## Background

Iter 24 established: 17 Cat-1 I4 cases share an identical structure. Our
winner is a Minor chord at bass note B (bassIsRoot=true). The correct answer
is a major (or dim) chord rooted at B−4 semitones with B in the bass —
a standard 6-chord (first inversion). That first-inversion chord is always
present as alt[1] in results[], losing to our winner by a small score margin
(typically 0.09, max 0.40). The 7 I3 cases (correct chord not in candidates)
are not targeted here.

**Expected outcome:** BIR=true 71 → ~54 (17 I4 fixes). BIR=false must not rise.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=71, BIR=false=788

---

## Step 2 — Read and report before writing code

Read `src/composing/analysis/chord/chordanalyzer.cpp` and report verbatim:

**A.** Gates E and F in full. Confirm neither already targets the I4 pattern
   (Minor root-position winner vs. same-bass major first inversion at interval
   4). If either does, STOP and report — Gate I may be redundant.

**B.** The last gate in the current sequence (Gate H or whatever comes last).
   Report its closing `}` line number so Gate I can be inserted immediately
   after it.

**C.** The score field on `ChordAnalysisResult` (or `ChordCandidate` — whatever
   `results[]` holds). What is the field name used in winner/alt score
   comparisons inside the existing gates? (e.g., `.score`, `.totalScore`,
   `.chordScore` — confirm the exact name from gate code.)

**D.** Does a diatonic-membership helper already exist (e.g., a function like
   `isDiatonic(rootPc, keyTonicPc, mode)` or a lookup table for scale
   intervals by mode)? If yes, report its signature. If no, we will write it
   inline.

---

## Step 3 — Implement Gate I

Insert Gate I immediately after the last existing gate. The gate must:

### 3a — Entry condition

Fire only when **all** of:
- `winnerBassIsRoot == true`
- `originalWinnerQuality == ChordQuality::Minor`
- `results.size() >= 2`
- `keyTonicPc >= 0` (key context is available — do not fire without key)

### 3b — Search loop

Iterate `results[1..]` (not results[0]) looking for a candidate `inv` where:
1. `inv.identity.bassPc == winner.identity.bassPc` — same bass note
2. `inv.identity.bassPc != inv.identity.rootPc` — it IS an inversion (not
   root position)
3. `(winner.identity.bassPc - inv.identity.rootPc + 12) % 12 == 4` — bass is
   exactly a major third above the alt's root (I4 interval)
4. Alt root is diatonic to current key (see §3c)
5. `winner.<scoreField> - inv.<scoreField> <= 0.45f` — margin within gate range

On the first candidate satisfying all five: swap `results[0]` with
`results[iIdx]` and break.

### 3c — Diatonic check

If a diatonic helper already exists, use it.

If not, compute inline using the mode-indexed interval sets below. The
`mode` variable holds the KeySigMode enum value already used by Gate G-E
(`keyModeTonicOffset`). Map it to a set of diatonic semitone offsets from
the tonic:

```
Major (Ionian, mode 0):        {0,2,4,5,7,9,11}
Minor (Aeolian, mode 5):       {0,2,3,5,7,8,10}
Dorian (mode 1):               {0,2,3,5,7,9,10}
Phrygian (mode 2):             {0,1,3,5,7,8,10}
Lydian (mode 3):               {0,2,4,6,7,9,11}
Mixolydian (mode 4):           {0,2,4,5,7,9,10}
Locrian (mode 6):              {0,1,3,5,6,8,10}
```

Compute: `isDiatonic = (diatonicSet.count((invRootPc - keyTonicPc + 12) % 12) > 0)`

Use `std::array<std::array<int,7>, 7>` or an equivalent constexpr table —
do NOT use a runtime heap allocation.

### 3d — Field names

Use the exact field names found in Step 2C for the score comparison. Use
`winner.identity.bassPc`, `winner.identity.rootPc`, `inv.identity.bassPc`,
`inv.identity.rootPc` — or the correct struct path confirmed in Step 2C.

### 3e — Do not change any existing gate

Gates A through the last existing gate must remain unchanged. Gate I is
additive only.

---

## Step 4 — Build and run all tests

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Expected: build pass (warnings only), 407/407, 53/53, 11/11.

Any test failure or new warning: **STOP and report verbatim.**

---

## Step 5 — Run corpus analysis

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report new BIR=true and BIR=false counts.

Expected: BIR=true ≈54 (17 fixes), BIR=false = 788 (unchanged).

**If BIR=false > 788: STOP and report verbatim. Do not proceed.**

**If BIR=true improvement < 10: STOP — gate may not be reaching target cases.
Report which of the 17 I4 test cases were and were not fixed.**

---

## Step 6 — If results clean: check for collateral wins or losses

Run:
```
cd C:\s\MS && python tools/analyze_bir_true_iter19.py
```

Report the new category breakdown (Cat 1 / Cat 2 / Cat 3 / Cat 4 counts).
The I4 cases should have moved out of Cat 1. Any unexpected change in Cat 2
or Cat 3 counts should be noted.

---

## Step 7 — Update pipeline snapshot goldens if needed

If BIR=true improved by ≥10 AND BIR=false ≤788 AND all unit tests passed:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 8 — Update baselines and STATUS.md

Update `build_and_test.md`:
- Replace BIR=true baseline with actual new count
- Attribution: Iteration 25

Update `STATUS.md` with a 2026-05-07 entry:
```
Iter 25: Gate I — first-inversion preference for diatonic chords
- Pattern: Minor root-position winner (e.g. Em) beats correct first-inversion
  major chord (e.g. C/E) at the same bass by ~0.09 score margin
- Fix: Gate I fires when winner is Minor bassIsRoot=true, runner-up has same
  bass at interval+4 from its own root (I4 = major-third inversion), root is
  diatonic to key, and score margin ≤ 0.45
- Net improvement: BIR=true 71→N (17 targeted I4 fixes; 7 I3 cases deferred)
- BIR=false: unchanged at 788
- New baselines: BIR=true=N, BIR=false=788
```

---

## Step 9 — Commit and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 25: Gate I — prefer diatonic first-inversion (I4) over root-position minor [N BIR=true fixes, M remaining]" && git push
```

---

## Step 10 — Report

```
Step 2 findings:
  Gate E: [brief summary]
  Gate F: [brief summary]
  Overlap with I4: none / [describe if found]
  Last existing gate: Gate [X] ends at line N
  Score field name: [field]
  Diatonic helper: exists / not-exists (written inline)

Code change:
  File: chordanalyzer.cpp
  Location: after Gate [X], lines N–N
  Diatonic table: [inline / helper function name]

Build:               pass
Composing tests:     407/407
Notation tests:      53/53
Pipeline snapshots:  11/11
BIR=true:            N  (was 71, improved by N)
BIR=false:           788

Category breakdown (Iter 19 script):
  Cat 1: N  Cat 2: N  Cat 3: N  Cat 4: N

Pipeline goldens updated: yes / no
build_and_test.md updated: yes
STATUS.md updated:         yes
GitHub push:               done — [commit hash]
```
