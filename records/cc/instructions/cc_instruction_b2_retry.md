# CC Instruction — B2 retry: Augmented dominant 7th template with M3 guard + Tristan catalog update

**Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`

**Current state:** Branch `master`, HEAD `f6630b29cd` (tooling commit), **working tree
clean.** BIR baselines (lenient-OR): Baroque BIR=true=28, BIR=false=16; Jazz BIR=true=35,
BIR=false=10. Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.
Tests: 407/407 composing, 52/52 notation, pipeline_snapshot 11/11 (1 skipped).

The first B2 attempt (adding `{0,4,8,10}` Augmented dominant 7th template) produced
3 composing-test failures and was reverted. This instruction fixes both root causes
before re-applying the template.

---

## Root cause analysis (both failures must be fixed)

**Failure 1 — Sus4 test:**  
`{E,A,C,D}` expected Sus4♯5 (perfect 4/4 template match for Esus4♯5) but the new
aug7 template at root E scored 3/4 tones matching (E✓, G#✗, C✓, D✓) and won anyway
because the large aug5 bonus (+8) on the present C tone outweighed the penalty for the
absent major third G#. **Fix:** require the major third (`pcWeight[rootPc+4]`) to be
above `extensionThreshold` before the aug7 template can score for any given root.

**Failure 2 — Tristan chord catalog:**  
`{C,F#,A#,D}` at catalog m285 had ground truth `rootPc=C, hasMinorSeventh=false`
(pre-B2 best match was C dom7b5, 3/4 tones). With B2, `D7♯5 = {D,F#,A#,C}` is a
perfect 4/4 match and correctly wins. Catalog approval obtained: update ground truth
to D7♯5.

---

## Step 1 — Add the M3-present guard in the template scoring loop

In `src/composing/analysis/chord/chordanalyzer.cpp`, find the inner loop that iterates
over `(rootPc, tplIdx)` template/root combinations (the "Score every root × template
combination" block, near the `basisIndepMatrix` / `complexityFactorMatrix` /
`augFactorMatrix` declarations around L2013).

At the start of the inner loop body — **before** any score computation for that
(rootPc, tplIdx) pair — add this guard:

```cpp
// B2 guard: the 4-tone Augmented (aug7) template requires the major third to be
// present above extensionThreshold. Without this, the template over-fires on chords
// where the aug5 or m7 matches but the defining major-third tone is absent.
if (templates[tplIdx].quality == ChordQuality::Augmented
    && templates[tplIdx].tones.size() == 4
    && pcWeight[(rootPc + 4) % 12] <= prefs.extensionThreshold) {
    continue;
}
```

This guard is entirely self-contained — it identifies the aug7 template by its
structural properties (Augmented quality + 4 tones) and checks `pcWeight`, which is
already computed from the sounding tones before the template loop. For the Tristan
chord `{C,F#,A#,D}` at root D: `pcWeight[(2+4)%12] = pcWeight[6] = pcWeight[F#]` —
F# is present, guard passes, D7♯5 scores normally ✓. For the Sus4 test `{E,A,C,D}`
at root E: `pcWeight[(4+4)%12] = pcWeight[8] = pcWeight[G#]` — G# is absent (floor
level ≤ 0.1), guard fires, aug7 skipped for this root ✓.

**Do not add this guard** anywhere else (not in `diagnoseChord`, not in a
post-scoring filter). The scoring loop guard is the correct and minimal place.

---

## Step 2 — Re-apply the template addition (same 4 sites as before)

**Site 1 — `analyzeChord` templates array (L1955)**

Change `std::array<TemplateDef, 16>` → `std::array<TemplateDef, 17>`.

Insert immediately after the existing Augmented triad line:
```cpp
{ ChordQuality::Augmented,      { 0, 4, 8 },        { 0, +4, +8 }       },
{ ChordQuality::Augmented,      { 0, 4, 8, 10 },    { 0, +4, +8, -2 }   },  // aug7 (C7♯5)
```

**Site 2 — Three score matrices (L2013–2015)**

Change each `std::array<std::array<double, 16>, 12>` → `std::array<std::array<double, 17>, 12>`:
```cpp
std::array<std::array<double, 17>, 12> basisIndepMatrix{};
std::array<std::array<double, 17>, 12> complexityFactorMatrix{};
std::array<std::array<double, 17>, 12> augFactorMatrix{};
```

**Site 3 — `diagnoseChord` templates array (L3368)**

Change `std::array<TemplateDef, 16>` → `std::array<TemplateDef, 17>`.

Insert the same new entry in the same position (after the Augmented triad in
`kDiagTemplates`). No guard is needed in `diagnoseChord` — it is a diagnostic
path only and does not affect production results.

---

## Step 3 — Update the Tristan chord catalog entry

**File:** `src/composing/tests/data/chordanalyzer_catalog_jazz.musicxml`

Find measure 285 (one long line). Make the following changes **within that measure**:

**Change 1 — numeral element:**  
Old: `<numeral-root text="I">1</numeral-root>`  
New: `<numeral-root text="II+7">2</numeral-root>`

**Change 2 — analysisKind attribute:**  
Old: `<harmony analysisKind="Tristan">`  
New: `<harmony analysisKind="augmented-seventh">`

**Change 3 — root step:**  
Old: `<root><root-step>C</root-step></root>`  
New: `<root><root-step>D</root-step></root>`

**Change 4 — kind text:**  
Old: `<kind text="CTristan">none</kind>`  
New: `<kind text="D7#5">none</kind>`

The notes (C4, F#4, A#4, D5) are **unchanged** — they are the sounding chord, not the
annotation.

---

## Step 4 — Remove 285 from `kJazzSymbolExceptions`

**File:** `src/composing/tests/chordanalyzer_musicxml_tests.cpp`

Find the line:
```cpp
static const std::set<int> kJazzSymbolExceptions = { 60, 164, 285, 316, 329, 333, 340 };
```

Remove `285` from the set (the comment above it says "m285 CTristan: non-standard pitch
set, no matching template" — with B2 there IS a matching template):
```cpp
static const std::set<int> kJazzSymbolExceptions = { 60, 164, 316, 329, 333, 340 };
```

Also update or remove the comment line `//   m285 CTristan: non-standard pitch set, no
matching template.` since it no longer applies.

---

## Step 5 — Build and run all three test suites

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_b2r.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_b2r.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_b2r.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_b2r.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_b2r.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_b2r.txt | tail -5; echo "exit:$?"
```

**Expected:** 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

If any snapshot fails, check the diff:
```
grep -A 30 "FAILED\|Expected\|Actual" /tmp/snap_b2r.txt | head -80; echo "exit:$?"
```

Run `--update-goldens` **only if** you verify the new winner is musically correct
(i.e., the snapshot shows an Augmented+seventh chord winning on a chord that genuinely
has both M3 and aug5 present). Do NOT update goldens if an existing correct chord is
flipping to aug7 on a chord that lacks the major third.

---

## Step 6 — Read mismatch report

```
cat C:\s\MS\src\composing\tests\chord_mismatch_report.txt; echo "exit:$?"
```

Expected: 4 RealDiff / 127 ConventionDiff — unchanged. The Tristan chord m285 was
previously a `ConventionDiff` (analyzer produced a different symbol); after the catalog
update the analyzer and catalog should agree, so this entry should disappear and the
ConventionDiff count might drop by 1 to 126. Report the actual counts.

---

## Step 7 — BIR check, both presets

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py > /tmp/bir_baroque_b2r.txt 2>&1; echo "exit:$?"
cat /tmp/bir_baroque_b2r.txt; echo "exit:$?"

cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py > /tmp/bir_jazz_b2r.txt 2>&1; echo "exit:$?"
cat /tmp/bir_jazz_b2r.txt; echo "exit:$?"
```

Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.

If either hard stop is hit: **revert ALL changes** (`git checkout
src/composing/analysis/chord/chordanalyzer.cpp
src/composing/tests/data/chordanalyzer_catalog_jazz.musicxml
src/composing/tests/chordanalyzer_musicxml_tests.cpp`), report the regression details,
and stop.

---

## Step 8 — Commit (if all clean)

If all tests pass and BIR is within hard stops:

```
cd C:\s\MS && git add src/composing/analysis/chord/chordanalyzer.cpp src/composing/tests/data/chordanalyzer_catalog_jazz.musicxml src/composing/tests/chordanalyzer_musicxml_tests.cpp; echo "exit:$?"
cd C:\s\MS && git commit -m "B2: add Augmented dominant 7th template {0,4,8,10} with M3-present guard

Adds a dedicated template for C7#5 alongside the Augmented triad. Guard: require
pcWeight[rootPc+4] > extensionThreshold before the aug7 template can score for a
given root (M3 must be present). This prevents over-firing on chords where the aug5
or m7 matches but the defining major-third is absent (e.g. Esus4#5 with A not G#).

Catalog: m285 Tristan chord {C,F#,A#,D} updated to D7#5 (perfect 4/4 template
match). Previous C reading was a 3/4 dom7b5 partial match; D7#5 is more accurate.
Removes m285 from kJazzSymbolExceptions.

BIR: Baroque BIR=true=XX BIR=false=XX; Jazz BIR=true=XX BIR=false=XX.
Tests: 407/407 composing, 52/52 notation, 11/11 pipeline_snapshot (1 skipped).
[Mismatch report: X RealDiff / X ConventionDiff]"; echo "exit:$?"
```

---

## Report back

1. Did the M3-present guard correctly block aug7 at root E for the Sus4 test?
2. BIR delta Baroque + Jazz (before → after)
3. Mismatch report counts (RealDiff + ConventionDiff, noting any delta from 4/127)
4. Any snapshot goldens refreshed (with description of what changed)
5. Commit hash, or revert notice if a hard stop was hit
