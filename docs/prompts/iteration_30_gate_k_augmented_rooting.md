# Iteration 30: Gate K — Augmented I4 inversion (rooting correction)

## Background

Iter 29 diagnostic established:

**Gate J (I↔vi/I)**: Abandoned. 2 fixes vs 32 BIR=false regressions. The
tonic-I vs vi/I disambiguation requires harmonic-function context (preceding
chords, whether the fifth is present in the voicing) that gate conditions cannot
access. This target is deferred to a future phrase-level approach. Do NOT
implement Gate J in this iteration.

**Gate K (redesigned)**: 3 of the 7 Augmented rooting targets have the correct
augmented inversion alt already present in `results[]` as `Major+SharpFifth`
quality. These are enharmonically the same pitch content as the winner, just
rooted differently:

| File     | m  | b   | Winner | Key  | Correct alt | Alt rootPc | Margin |
|----------|----|-----|--------|------|-------------|------------|--------|
| bwv40.3  | 9  | 1.0 | D+     | Dmin | Bb#5/D      | 10 (Bb)    | +0.062 |
| bwv40.6  | 6  | 1.0 | A+     | Dmin | F#5/A*      | 5 (F)      | +0.062 |
| bwv102.7 | 11 | 2.0 | G+     | Gmin | Eb#5/G      | 3 (Eb)     | +0.117 |

*"F#5/A" is a symbol formatting artefact — `identity.rootPc` holds 5 (F natural).

The other 4 targets either have the wrong enharmonic root in candidates (D# vs
D, F# vs F) or lack any augmented inversion alt entirely. Those require candidate
generation changes and are deferred.

The gate condition for the 3 reachable targets:
- `(winner.bassPc - 4 + 12) % 12 == alt.rootPc` — I4 complement: alt's root
  is a major third below the bass (same as saying bass is the major third of
  the alt's root = classic first inversion of the augmented triad)
- alt quality is `Augmented` OR (`Major` AND has `SharpFifth` extension)
- same bass, not root-position, diatonic, margin ≤ 0.20

Expected: BIR=true 53 → 50 (3 fixes), BIR=false unchanged at 787.

---

## Step 1 — Confirm baseline

The corpus was restored at the end of Iter 29 (Gate J and Gate K both removed,
Iter 25 state). Confirm:

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected: BIR=true=53, BIR=false=787. If different, re-run the build and corpus
first:

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

---

## Step 2 — Read before writing

**A.** Read `src/composing/analysis/chord/chordanalyzer.cpp`. Report:
- The exact enum name for the `SharpFifth` extension (confirm it exists as
  `Extension::SharpFifth`, `Extension::AugmentedFifth`, or similar — look in
  the same header where `Extension::MajorSeventh` is defined).
- Gate I's closing `}` line number (Gate K inserts immediately after).
- Confirm `ChordQuality::Augmented` is the correct enum name.

**B.** Report the field accessor for extensions on an alt in results[] — the same
`hasExtension(inv.identity.extensions, Extension::X)` form used in Iter 27/28,
or whatever the correct form is.

---

## Step 3 — Implement Gate K

Insert Gate K immediately after Gate I (the current last gate).

### Entry condition (ALL required)
- `originalWinnerQuality == ChordQuality::Augmented`
- `winnerBassIsRoot == true`
- `results.size() >= 2`
- `keyTonicPc >= 0`

### Search loop

Iterate `results[1..]` for candidate `inv` satisfying ALL:

1. `inv.identity.bassPc == winner.identity.bassPc` — same bass
2. `inv.identity.bassPc != inv.identity.rootPc` — alt is NOT root-position
3. `(winner.identity.bassPc - inv.identity.rootPc + 12) % 12 == 4` — I4
   interval: alt root is a major third below the bass (bass is the major third
   of the alt's root, making this a first inversion)
4. Alt quality is augmented: `inv.identity.quality == ChordQuality::Augmented ||
   (inv.identity.quality == ChordQuality::Major &&
    hasExtension(inv.identity.extensions, Extension::<SharpFifth>))`
   Use the exact enum name found in Step 2A.
5. Alt root diatonic to key — reuse the same `scale` array from Gate I.
6. `winner.identity.score - inv.identity.score <= 0.20f`

On first match: swap `results[0]` and `results[iIdx]`, break.

**Rationale for 0.20 threshold**: all 3 reachable targets have margin ≤ 0.117.
The 0.20 ceiling gives headroom while staying well below any plausible false-
positive margin.

### Do not implement Gate J

Gate J is deferred. Do not add any vi-chord inversion logic in this iteration.

---

## Step 4 — Build and run all tests

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Expected: build pass (warnings only), 407/407, 53/53, 11/11.
Any failure: **STOP and report verbatim.**

---

## Step 5 — Run corpus analysis

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report new BIR=true and BIR=false.

**Hard stops:**
- **If BIR=false > 787: STOP and report verbatim. Do not proceed.**
- **If BIR=true improvement < 2: STOP** — report which of the 3 target cases
  were and were not fixed, with diagnostic details.

---

## Step 6 — Update pipeline snapshot goldens if clean

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

---

## Step 7 — Update baselines and STATUS.md

Update `build_and_test.md` with actual new BIR counts and Iter 30 attribution.

Update `STATUS.md`:
```
Iter 30: Gate K — Augmented I4 inversion (rooting correction)
- Pattern: Augmented root-position winner (e.g. D+) beats correct first-inversion
  of same augmented collection (Bb#5/D) at tiny margin (~0.06–0.12). Music21
  labels these as III+6 / bVII+6 / IV+6 in figured-bass notation.
- Fix: Gate K promotes alt when quality=Augmented or Major+SharpFifth, same bass,
  (bass - alt.root + 12)%12 == 4, diatonic, margin ≤ 0.20.
- 3 of 7 Augmented rooting targets fixed (4 have wrong enharmonic root or absent
  alt — require candidate generation changes, deferred).
- Gate J (I↔vi/I Major ambiguity): DEFERRED. 2 correct fixes vs 32 BIR=false
  regressions in Baroque corpus — the tonic-I vs vi-chord discrimination
  requires harmonic-function context beyond what ranking gates can access.
- Net improvement: BIR=true 53→N
- BIR=false: N (was 787)
- New baselines: BIR=true=N, BIR=false=N
```

---

## Step 8 — Commit and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 30: Gate K — Augmented I4 rooting correction (III+6/bVII+6 pattern) [N BIR=true fixes, M remaining]" && git push
```

---

## Step 9 — Report

```
Step 2 findings:
  SharpFifth enum name: Extension::[name]
  ChordQuality::Augmented confirmed: yes
  Gate I ends at line N; Gate K inserted lines N–N

Build:               pass
Composing tests:     407/407
Notation tests:      53/53
Pipeline snapshots:  11/11
BIR=true:            N  (was 53, improved by N)
BIR=false:           N  (was 787)

Gate K fixes:
  bwv40.3  m=9  b=1: [fixed / not fixed — margin / condition that failed]
  bwv40.6  m=6  b=1: [fixed / not fixed]
  bwv102.7 m=11 b=2: [fixed / not fixed]

GitHub push:         done — [commit hash]
```
