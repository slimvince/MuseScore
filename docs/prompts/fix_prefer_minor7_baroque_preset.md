# Fix: wire preferMinor7OverMajorAdd6 flag into Baroque preset

## Context loading — do this first

1. `CLAUDE.md` — standing instructions, build/test commands, autonomous-operation scope.
2. `STATUS.md` — top summary line and the `2026-05-04` entries only.
3. `src/composing/analysis/chord/chordanalyzer.h` — `ChordAnalyzerPreferences` struct
   (search for `struct ChordAnalyzerPreferences`)
4. `src/composing/analysis/chord/chordanalyzer.cpp` — the post-ranking inversion
   correction block (search for `// ── Inversion / bass-root bias correction ──`)
   and the guaranteed-alt block (search for `// ── Guaranteed inversion alternative ──`)
5. `tools/batch_analyze.cpp` — preset builder section
   (search for `// ── Build chord analyzer preferences from preset ──`)

---

## Background

After four fix attempts the root cause of the remaining 151 inversion errors is
confirmed: it is a **vocabulary convention difference**, not a scoring bug.

- `{Bb, D, F, G}` with Bb in the bass is legitimately **Bb6** in jazz/pop
  vocabulary and **Gm7/Bb** in classical/functional harmonic analysis.
- These are enharmonically equivalent for the same four pitch classes.
- DCML (the Bach chorale ground truth) always labels this as the Minor7 reading.
- Our catalog (`chordanalyzer_catalog.musicxml`) labels the same pattern as C6,
  C69, CMaj7add13 — the jazz/pop convention.

Every score-based approach to distinguish these has caused regressions because
**both interpretations are locally correct** — the difference is purely which
convention applies. The correct architectural resolution is to make this a
**preset-controlled preference** in `ChordAnalyzerPreferences`.

The preset system already exists in `batch_analyze.cpp` but currently only
wires two things per preset: `KeyModeAnalyzerPreferences` (mode priors) and
`extensionThreshold` (0.12 for Jazz only). All other chord preferences use the
same defaults regardless of preset. This fix extends the preset wiring.

---

## The fix — three parts

### Part 1 — Add flag to ChordAnalyzerPreferences

**File:** `src/composing/analysis/chord/chordanalyzer.h`

In `struct ChordAnalyzerPreferences`, after the existing inversion correction
parameters (`inversionSuspicionMargin`, `inversionBonusReduction`), add:

```cpp
/// When true, a Major-quality bass-root winner is re-interpreted as an
/// inverted Minor7 chord when a Minor/Minor7 alternative exists whose root
/// is a minor third below the winner's root
/// (i.e. altRootPc == (winnerRootPc + 9) % 12).
///
/// This is the enharmonic equivalence: X_Major_add6 and Ym7 span identical
/// pitch classes when Y = (X + 9) % 12 (e.g. Bb6 ↔ Gm7, C6 ↔ Am7).
///
/// Baroque / Standard preset: true — classical functional analysis treats
///   "6th chords" as inverted seventh chords (Bb6 → Gm7/Bb, C6 → Am7/C).
/// Jazz preset: false — the added sixth is a distinct structural quality
///   (C6 is not the same harmonic function as Am7/C).
///
/// Default: false — preserves existing behaviour and keeps catalog tests
/// (which run with default preferences) passing unchanged.
bool preferMinor7OverMajorAdd6 = false;
```

### Part 2 — Apply the flag in the inversion correction

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`

Inside the post-ranking inversion correction block, after `bestAlt` has been
identified (the highest-scoring clean Major/Minor alternative with a different
rootPc), add an enharmonic fast path **before** the existing margin check.

The fast path fires only when `prefs.preferMinor7OverMajorAdd6` is true:

```cpp
// ── Enharmonic equivalence fast path (Baroque/Standard preset) ──────────
//
// When preferMinor7OverMajorAdd6 is set, a Major-quality bass-root winner
// is swapped with a Minor/Minor7 alternative whose root satisfies the
// enharmonic relationship altRootPc == (winnerRootPc + 9) % 12.
// No margin check is applied — the convention is enforced directly.
// This correctly handles Bb6 → Gm7/Bb, C6 → Am7/C, etc. in classical
// contexts, while leaving Jazz preset output unchanged (flag = false).
if (prefs.preferMinor7OverMajorAdd6
    && winnerBassIsRoot
    && bestAlt.identity.quality == ChordQuality::Minor
       || bestAlt.identity.quality == ChordQuality::Minor7)
{
    const int expectedAltRoot = (winnerRootPc + 9 + 12) % 12;
    if (bestAlt.identity.rootPc == expectedAltRoot) {
        // Swap winner and bestAlt — do NOT re-sort the full vector.
        // Only this specific enharmonic pair is being resolved.
        std::swap(results[0], results[bestAltIdx]);
        // Fall through to end of correction block; margin check is skipped.
        goto endInversionCorrection;  // or use a done-flag — see note below
    }
}
```

**Implementation note:** If the codebase style prohibits `goto`, use a
`bool enharmonicFlipDone = false;` flag set to `true` in the block above,
then wrap the existing margin-based section in `if (!enharmonicFlipDone) { … }`.

**`bestAltIdx`:** the correction already walks `results[]` to find `bestAlt`.
Capture the index during that walk so the swap targets the correct position.

**Operator precedence:** note the `||` in the quality check above needs
parentheses to bind correctly with the outer `&&`. Write it as:

```cpp
if (prefs.preferMinor7OverMajorAdd6
    && winnerBassIsRoot
    && (bestAlt.identity.quality == ChordQuality::Minor
        || bestAlt.identity.quality == ChordQuality::Minor7))
```

### Part 3 — Wire the flag in batch_analyze.cpp

**File:** `tools/batch_analyze.cpp`

In the preset builder section (search for
`// ── Build chord analyzer preferences from preset ──`), extend the existing
Jazz-only block:

```cpp
analysis::ChordAnalyzerPreferences chordPrefs;
if (presetName == "Jazz") {
    chordPrefs.extensionThreshold = 0.12;
    // preferMinor7OverMajorAdd6 stays false — C6 is a distinct jazz quality
} else {
    // Baroque, Standard, Modal, Contemporary: classical convention —
    // Major-add6 is an inverted Minor7 in functional harmonic analysis.
    chordPrefs.preferMinor7OverMajorAdd6 = true;
}
```

---

## What NOT to touch

- Do **not** change `inversionSuspicionMargin`, `bassNoteRootBonus`,
  `kScoreThresholdRatio`, or any other scoring constants.
- Do **not** touch the guaranteed-alt block (Fix 3) or its Pass 2 guard.
- Do **not** touch `chordanalyzer_catalog.musicxml`.
- Do **not** commit — report results and wait for sign-off.

---

## Verification

### Build and test

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.

**Pass criterion:** 407/407 pass, RealDiff ≤ 4.

The catalog tests call `analyzeChord` with **default preferences**
(`preferMinor7OverMajorAdd6 = false`), so they are unaffected by this change
and must continue to pass unchanged. If any catalog test regresses, the default
value of the flag is wrong — check that it is `false`.

### Corpus analysis — MUST use Baroque preset

The corpus improvement will only appear when `batch_analyze` is run with
`--preset Baroque` (or any non-Jazz preset after Part 3). Running the
corpus pipeline without a preset, or with `--preset Jazz`, will show no
change because `preferMinor7OverMajorAdd6` stays `false`.

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

The corpus JSON files in `tools/reports/corpus/` must be regenerated using
the new binary **with `--preset Baroque`** before running the script, otherwise
the script reads stale pre-fix data. Check `run_bach_preset.py` or the
equivalent validation runner for the correct invocation.

### Report format

```
Build:                     pass / fail
Tests:                     N/N pass
RealDiff:                  before=4, after=N
Catalog tests:             all pass with default prefs (flag=false) / regressions: <list>
Corpus run preset used:    Baroque (confirm explicitly)
3-way genuine errors:      before=151, after=N
2-way bassIsRoot:          before=805, after=N
Regressions:               none / <description>
Notes:                     <anything unexpected>
```
