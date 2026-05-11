# Iteration 27: Implement Gate J (Major+I3) and Gate K (Augmented+MinMaj7)

## Background

Two consistent Cat-2 patterns remain:

**Gate J target (6 cases):** winner is Major root-position (bassIsRoot=true),
correct answer is a Minor/Minor7 chord in first inversion at the same bass
(interval I3: `(winner.bassPc − alt.rootPc + 12) % 12 == 3`).
Examples: C→Am/C, G→Em/G, F→Dm/F, E→C#m7/E.

**Gate K target (7 cases):** winner is Augmented root-position, correct answer
is a MinorMajorSeventh chord in second inversion at the same bass
(interval I7: `alt.rootPc == (winner.bassPc + 5) % 12`).
Examples: D+→GmMaj7/D, E+→AmMaj7/E, F#+→BmMaj7/F#.

One existing miss to investigate: bwv244.10 m2 (Fm→DbMaj7/F, key=Abmaj,
margin=0.02) appears to satisfy Gate I's I4 condition but is still a mismatch.

**Expected outcome:** BIR=true 53 → ~39 (13 targeted fixes). BIR=false must
not rise.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=53, BIR=false=787

---

## Step 2 — Read and report before writing code

**A.** Read Gate I as actually implemented in `chordanalyzer.cpp` (the code
   inserted in Iter 25). Report it verbatim. Specifically note:
   - Does it restrict alt quality (e.g. only ChordQuality::Major, excluding
     Major7/MajorWithSeventh)?
   - Does it use `originalWinnerQuality` or something else for the entry check?

**B.** Inspect bwv244.10 case directly:
   - Open `tools/corpus/bwv244.10.ours.json`, find measure 2 beat 1.
   - Report the winner symbol, score, and full alternatives list.
   - Based on Gate I's actual code (Step 2A), explain why it did not fire.

**C.** Find the `ChordQuality` enum in the source. Report which enum value
   corresponds to `GmMaj7` / `AmMaj7` / `BmMaj7` (minor-major seventh chords).
   Also confirm the enum value for `Augmented`.

**D.** Report the line number where Gate I ends so Gate J and K can be
   inserted immediately after.

---

## Step 3 — Fix Gate I miss (if applicable)

Based on Step 2A/B findings: if Gate I has an unintended alt-quality
restriction that excludes Major7/MajorWithSeventh alts, remove that
restriction. The only quality filters Gate I should apply are:
- The winner must be `ChordQuality::Minor`
- The alt must not be root-position (bassPc ≠ rootPc)
- The interval must be 4
- The alt root must be diatonic

If the miss is caused by something else (e.g. the alt is not in results[]),
report that and do NOT modify Gate I — this step becomes a no-op.

---

## Step 4 — Implement Gate J: Major winner + I3 minor inversion

Insert Gate J immediately after Gate I.

### Entry condition (ALL required)
- `originalWinnerQuality == ChordQuality::Major` (confirm exact enum name)
- `winnerBassIsRoot == true`
- `results.size() >= 2`
- `keyTonicPc >= 0`

### Search loop

Iterate `results[1..]` for candidate `inv` satisfying ALL:
1. `inv.identity.bassPc == winner.identity.bassPc` — same bass
2. `inv.identity.bassPc != inv.identity.rootPc` — inv is NOT root-position
3. `(winner.identity.bassPc − inv.identity.rootPc + 12) % 12 == 3` — I3
   interval (bass is minor third above alt root)
4. `inv.identity.quality` is Minor or MinorSeventh (or any minor-family
   quality — use the enum values found in Step 2C; do NOT restrict so tightly
   that Minor7 chords are excluded)
5. Alt root diatonic to key (reuse the same inline `scale` array approach from
   Gate I)
6. `winner.identity.score − inv.identity.score <= 0.35f`

On first match: swap `results[0]` and `results[iIdx]`, break.

(The 0.35 threshold covers 6 of the 7 cases, deliberately excluding the 0.64
outlier bwv244.40 until regression testing confirms safety.)

---

## Step 5 — Implement Gate K: Augmented winner + MinorMajorSeventh I7

Insert Gate K immediately after Gate J.

### Entry condition (ALL required)
- `originalWinnerQuality == ChordQuality::Augmented` (confirm exact enum name)
- `winnerBassIsRoot == true`
- `results.size() >= 2`
- `keyTonicPc >= 0`

### Search loop

Iterate `results[1..]` for candidate `inv` satisfying ALL:
1. `inv.identity.bassPc == winner.identity.bassPc` — same bass
2. `inv.identity.rootPc == (winner.identity.bassPc + 5) % 12` — alt root is
   a perfect fourth above the bass (equivalent: bass is perfect fifth of alt
   root = second inversion I7)
3. `inv.identity.quality == ChordQuality::<MinorMajorSeventh>` — use the enum
   value found in Step 2C for GmMaj7/AmMaj7-type chords
4. Alt root diatonic to key
5. `winner.identity.score − inv.identity.score <= 0.50f`

On first match: swap `results[0]` and `results[iIdx]`, break.

---

## Step 6 — Build and run all tests

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Expected: build pass (warnings only), 407/407, 53/53, 11/11.
Any failure: **STOP and report verbatim.**

---

## Step 7 — Run corpus analysis

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report new BIR=true and BIR=false.

Expected: BIR=true ≈39–40 (13 fixes), BIR=false ≤787.

**If BIR=false rises above 787: STOP and report verbatim.**
**If BIR=true improvement < 8: STOP — report which of the target cases were
and were not fixed, with their diagnostic details.**

---

## Step 8 — Update pipeline snapshot goldens if clean

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 9 — Update baselines and STATUS.md

Update `build_and_test.md` with actual new BIR counts and Iter 27 attribution.

Update `STATUS.md`:
```
Iter 27: Gates J and K — Major+I3 and Augmented+MinMaj7 inversions
- Gate J: Major root-position winner vs Minor first-inversion at same bass
  (I3 interval); threshold 0.35; targets C→Am/C, G→Em/G, F→Dm/F pattern
- Gate K: Augmented root-position winner vs MinorMajorSeventh second-inversion
  at same bass (alt.rootPc = bass+5); threshold 0.50; targets D+→GmMaj7/D
  pattern (augmented triad is 3-note subset of MinMaj7)
- [If Gate I fix applied]: also fixed Gate I miss (alt quality restriction
  excluded Major7 alts)
- Net improvement: BIR=true 53→N (J: ~6 fixes, K: ~7 fixes)
- BIR=false: N (was 787)
- New baselines: BIR=true=N, BIR=false=N
```

---

## Step 10 — Commit and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 27: Gates J+K — Major+I3 and Augmented+MinMaj7 inversions [N BIR=true fixes, M remaining]" && git push
```

---

## Step 11 — Report

```
Step 2 findings:
  Gate I actual quality restriction: [describe]
  bwv244.10 miss reason: [describe]
  Gate I fix applied: yes / no
  ChordQuality for MinMaj7: ChordQuality::[value]
  ChordQuality for Augmented: ChordQuality::[value]
  Gate I ends at line N; Gate J inserted N–N; Gate K inserted N–N

Build:               pass
Composing tests:     407/407
Notation tests:      53/53
Pipeline snapshots:  11/11
BIR=true:            N  (was 53, improved by N)
BIR=false:           N  (was 787)

GitHub push:         done — [commit hash]
```
