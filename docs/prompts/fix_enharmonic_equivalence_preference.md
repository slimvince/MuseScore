# Fix: direct enharmonic-equivalence preference for Major-add6 / Minor7 pairs

## Context loading — do this first

1. `CLAUDE.md` — standing instructions, build/test commands, autonomous-operation scope.
2. `STATUS.md` — top summary line and the `2026-05-04` entries only.
3. `src/composing/analysis/chord/chordanalyzer.cpp` — specifically:
   - The post-ranking inversion correction block (search for
     `// ── Inversion / bass-root bias correction ──`)
   - The guaranteed-inversion-alternative block added in Fix 3
     (search for `// ── Guaranteed inversion alternative ──`)
   - The `ChordQuality` enum and `ChordAnalysisResult::identity` struct

---

## Background

Three rounds of fixes have clarified the real problem:

- **Fix 1** (threshold de-inflation): the correct chord now clears the admission
  threshold and enters `rawCandidates`.
- **Fix 3** (guaranteed-alt append): the correct different-rootPc chord now
  appears in `results[]`.
- **Fix 4** (de-bonused margin — reverted): failed because the organic pcWeight
  distribution in bass-heavy regions inflates bass-root scores independently of
  the explicit bass bonus. The de-bonused gap between winner and alternative
  remains > `inversionSuspicionMargin` (0.70) for most of the 151 target cases.
  It also caused a regression on Cm13 (complex extended chord incorrectly
  flipped).

**Root cause (confirmed):** Score-based discrimination cannot resolve the
enharmonic equivalence between `X_Major_add6` and `Ym7` (where Y = (X+9)%12)
in bass-heavy textures, because the organic pcWeight distribution favours
the bass-root reading at every level of the scorer, not just through the
explicit bonus. A margin threshold — bonused or de-bonused — is the wrong tool.

**The fix:** For the specific structural case where winner and alternative share
the same four pitch classes (the Major-add6 / Minor7 enharmonic pair), apply
a direct preference rule rather than a margin comparison. When the bass note is
the Major-chord root and a Minor7 alternative exists with the same pitch classes,
the Minor7 reading is always preferred. This is what the reference plugin
algorithm achieves structurally by not modelling 6th chords at all — we want
the same outcome without losing 6th-chord vocabulary.

---

## The enharmonic equivalence pattern

`X Major (add6)` and `Ym7` (where `Y = (X + 9) % 12`) span identical pitch
classes:

| Winner (bass-root) | Correct label    |
|--------------------|-----------------|
| Bb6 (Bb,D,F,G)    | Gm7/Bb          |
| C6  (C,E,G,A)     | Am7/C           |
| Eb6 (Eb,G,Bb,C)   | Cm7/Eb          |
| F6  (F,A,C,D)     | Dm7/F           |
| G6  (G,B,D,E)     | Em7/G           |
| Ab6 (Ab,C,Eb,F)   | Fm7/Ab          |
| … (all 12 roots)  | …               |

The pattern holds whenever:
- `winnerRootPc == bassPc` (bass is labeled as root)
- winner quality is Major (possibly with added-sixth annotation)
- alternative quality is Minor or Minor7
- `altRootPc == (winnerRootPc + 9) % 12`
- the four pitch classes match (winner's root, M3, P5, M6 = alt's minor
  third, perfect fifth, minor seventh relative to alt's root)

---

## The fix

**File:** `src/composing/analysis/chord/chordanalyzer.cpp`

### Step 1 — Locate the inversion correction block

Find the block starting with:
```
// ── Inversion / bass-root bias correction ──
```

Inside it, find where `bestAlt` (the best clean Major/Minor alternative with
a different rootPc) is identified, and where the margin check
(`margin < inversionSuspicionMargin`) gates the flip.

### Step 2 — Add an enharmonic-equivalence fast path BEFORE the margin check

Before the existing `if (margin < inversionSuspicionMargin)` branch, insert:

```cpp
// ── Enharmonic equivalence fast path ────────────────────────────────────
//
// Major-add6 and Minor7 chords span identical pitch classes when the
// Minor7 root is a minor third below the Major root (i.e. altRootPc ==
// (winnerRootPc + 9) % 12).  In bass-heavy textures, the scorer
// systematically favours the bass-root Major reading even after the
// explicit bass bonus is removed; score-based margin comparison cannot
// reliably distinguish the two readings.
//
// When the winner is a Major-quality chord AND the best clean alternative
// is Minor or Minor7 quality AND their roots satisfy the enharmonic-
// equivalence relationship, prefer the alternative directly — without a
// margin check.  This mirrors what unweighted template-matching approaches
// (including the reference plugin) achieve structurally.
//
// Guard conditions (all must hold):
//   (a) winnerBassIsRoot — we are in a potential inversion situation
//   (b) winner quality is Major (with or without extensions — but NOT
//       Dominant7, which is a distinct quality)
//   (c) bestAlt quality is Minor or Minor7
//   (d) altRootPc == (winnerRootPc + 9) % 12  (minor-third below)
//
// No margin check is applied here; the pattern alone is sufficient.
const bool winnerIsMajorFamily =
    (winner.identity.quality == ChordQuality::Major);
const bool altIsMinorFamily =
    (bestAlt.identity.quality == ChordQuality::Minor
     || bestAlt.identity.quality == ChordQuality::Minor7);
const int  expectedAltRoot = (winnerRootPc + 9) % 12;
const bool isEnharmonicPair =
    winnerIsMajorFamily
    && altIsMinorFamily
    && (bestAlt.identity.rootPc == expectedAltRoot);

if (winnerBassIsRoot && isEnharmonicPair) {
    // Promote bestAlt to position 0 by swapping with winner.
    // Do NOT do a full re-sort — only this specific pair is being resolved.
    std::swap(results[0], results[bestAltIdx]);
    // Skip the margin-based flip below; we are done for this region.
    goto endInversionCorrection;   // or use a bool flag — see impl note
}
```

**Implementation note on `goto` vs flag:** Using `goto` to a label
`endInversionCorrection:` placed just after the existing correction block
is the simplest implementation. If the coding standard forbids `goto`,
use a `bool didEnharmonicFlip = false;` flag set to `true` here, and
wrap the margin-based section in `if (!didEnharmonicFlip) { … }`.

**`bestAltIdx`**: the existing correction code walks `results[]` to find
`bestAlt`. Capture the index during that walk (e.g. `bestAltIdx`) so the
swap targets the right position.

### Step 3 — Fix the re-sort in the existing margin-based branch

CC observed that the existing margin-based correction does a full re-sort
after applying `inversionBonusReduction`, which can promote a same-root
chord (e.g. Csus4) above the intended bestAlt. Change the existing
correction logic to swap `results[0]` and `results[bestAltIdx]` explicitly,
rather than re-sorting the entire vector. This is a correctness fix
independent of the enharmonic-equivalence path.

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
**Pass criterion:** 407/407 tests pass, RealDiff ≤ 4.

### Corpus analysis

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

### Report format

```
Build:                  pass / fail
Tests:                  N/N pass
RealDiff:               before=4, after=N
3-way genuine errors:   before=151, after=N
2-way bassIsRoot:       before=805, after=N
Enharmonic fast path:   yes — swaps N/N cases in synthetic tests
Re-sort fix applied:    yes / no
Regressions:            none / <description>
Notes:                  <anything unexpected>
```

If RealDiff increases, identify the regressing case and report before
attempting any further changes.
