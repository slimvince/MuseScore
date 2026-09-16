# CC Instruction — B3: dim7 dedicated template {0,3,6,9}

**Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`

**Current state:** Branch `master`, HEAD `945a9e2f18`, **working tree clean.**
BIR baselines (lenient-OR): Baroque BIR=true=28, BIR=false=16; Jazz BIR=true=36,
BIR=false=10. Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.
Tests: 407/407 composing, **52/52 notation (fully green)**, pipeline_snapshot
11/11 (1 skipped, no goldens touched).
Mismatch report: Jazz 3 RealDiff / 127 ConventionDiff; Standard 0 / 1.
Roman numeral baseline: rn_agree=27.6% (16,905/61,233). Hard stop: rn_agree must
not drop below 27.6%.

---

## Background

Currently, the diminished seventh chord is scored via the 3-tone Diminished triad
template + `dim7CharacteristicBonus` (a fixed score bonus when the ♭♭7 tone is present
above threshold, gated in STEP 1 on the complete diminished triad being present).

B3 replaces this bonus approach with a proper 4-tone template `{0,3,6,9}` (C°7),
consistent with how aug7 is now handled (dedicated 4-tone Augmented template added in
B2). The 4-tone template gives a score computed directly from pitch evidence at all 4
tones rather than a fixed bonus on top of the 3-tone score.

**Note:** B3 does NOT fix the enharmonic rotation ambiguity. All rotations of {0,3,6,9}
share the same PC set (C°7 = E♭°7 = G♭°7 = B♭♭°7), so the template fires on all four
roots equally. Correct rotation is determined by the `wDim` bonus + `nextRootPc` context
— this is orthogonal to adding the template and stays unchanged.

The templates array is currently 17 entries wide (after B2). B3 grows it to 18.

---

## Part A — Read first, report before any code change

Before making any changes, read the following in `chordanalyzer.cpp`:

1. The existing Diminished triad template entry in the `analyzeChord` templates array
   — note the exact score offsets for each interval.
2. The `dim7CharacteristicBonus` code — find the block that fires it:
   - What score offset does it apply?
   - What is its exact firing condition (the STEP 1 completeness guard requires all
     of root + ♭3 + ♭5 above threshold before the bonus fires)?
   - Does it fire inside the main template scoring loop (per rootPc), or in a separate pass?
3. The existing Diminished triad entry in `kDiagTemplates` (the `diagnoseChord` array).

**Report back these three things before proceeding:**

a. The score offsets used in the existing 3-tone Diminished template entry  
   (e.g. `{ 0, -3, -1 }` or whatever they are).  
b. The exact bonus offset `dim7CharacteristicBonus` currently adds.  
c. The exact location (function + approximate line number) where
   `dim7CharacteristicBonus` fires.

Do not make any file changes until you have reported these three facts.

---

## Part B — Template addition (4 sites)

Once you have confirmed the offsets from Part A, apply the following changes.

### B1 — Guard in the scoring loop

Place this guard **at the very start of the inner (rootPc, tplIdx) loop body**, alongside
the B2 aug7 guard already present:

```cpp
// B3 guard: the 4-tone Diminished (dim7) template requires the minor third (rootPc+3),
// diminished fifth (rootPc+6), AND diminished seventh (rootPc+9) all to be present
// above extensionThreshold. This prevents it from firing on incomplete diminished
// sonorities where the ♭♭7 is absent — those fall through to the 3-tone Diminished
// template.
if (templates[tplIdx].quality == ChordQuality::Diminished
    && templates[tplIdx].intervals.size() == 4
    && (pcWeight[(rootPc + 3) % 12] <= prefs.extensionThreshold
        || pcWeight[(rootPc + 6) % 12] <= prefs.extensionThreshold
        || pcWeight[(rootPc + 9) % 12] <= prefs.extensionThreshold)) {
    continue;
}
```

### B2 — Add the dim7 template in `analyzeChord` (17 → 18)

Change `std::array<TemplateDef, 17>` → `std::array<TemplateDef, 18>`.

Insert immediately after the existing 3-tone Diminished triad entry:

```cpp
{ ChordQuality::Diminished,     { 0, 3, 6 },        { /* existing 3-tone offsets */ }    },
{ ChordQuality::Diminished,     { 0, 3, 6, 9 },     { /* 3-tone offsets + ♭♭7 offset */ } },  // dim7 (C°7)
```

For the ♭♭7 offset in the 4-tone entry, use the same value that `dim7CharacteristicBonus`
currently adds (reported in Part A). This preserves the calibrated scoring weight for
that tone.

### B3 — Update three score matrices (17 → 18)

```cpp
std::array<std::array<double, 18>, 12> basisIndepMatrix{};
std::array<std::array<double, 18>, 12> complexityFactorMatrix{};
std::array<std::array<double, 18>, 12> augFactorMatrix{};
```

### B4 — Add the dim7 template in `diagnoseChord` (17 → 18)

Same insertion as B2 inside `kDiagTemplates`. No guard needed in `diagnoseChord`.

---

## Part C — dim7CharacteristicBonus interaction

With the 4-tone template in place, there is a potential double-scoring issue: when all
4 dim7 tones are above threshold, BOTH the 4-tone template (via template score) AND the
3-tone template + bonus (since the complete triad is also present) would fire for the
same root, producing two candidates with different scores but the same root/quality.

**Recommended resolution:** Condition `dim7CharacteristicBonus` so it does NOT fire when
the 4-tone template guard passes (i.e. when ♭♭7 is above `extensionThreshold`). When
all 4 tones are present, the 4-tone template handles scoring; when ♭♭7 is absent, the
bonus path is moot (guard already blocks it) and the 3-tone template handles it cleanly.

In practice: wrap the `dim7CharacteristicBonus` application with:

```cpp
// Only fire when ♭♭7 is NOT above threshold — the 4-tone template handles the
// full-dim7 case; the bonus is vestigial when the template is active.
if (pcWeight[(rootPc + 9) % 12] <= prefs.extensionThreshold) {
    // existing dim7CharacteristicBonus logic here
}
```

If this change produces unexpected test failures, revert the bonus suppression (keep
the original bonus), report the failures, and let double-scoring coexist for now (the
4-tone template should still dominate if its score is higher).

---

## Part D — Build and run all three test suites

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_b3.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_b3.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_b3.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_b3.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_b3.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_b3.txt | tail -5; echo "exit:$?"
```

Expected: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

If any snapshot fails, read the diff:
```
grep -A 30 "FAILED\|Expected\|Actual" /tmp/snap_b3.txt | head -60; echo "exit:$?"
```

Only update goldens if the new dim7 template wins on a chord where all 4 tones (root,
♭3, ♭5, ♭♭7) are genuinely present above threshold AND the old reading was a 3-tone
partial match. Do NOT update a golden if a plain diminished triad flips to dim7 on a
chord lacking the ♭♭7 — that is a spurious fire.

---

## Part E — Mismatch report

```
cat C:\s\MS\src\composing\tests\chord_mismatch_report.txt; echo "exit:$?"
```

Expected: 3 RealDiff / 127 ConventionDiff (Jazz) — unchanged or potentially improved
if any catalog dim7 entries previously needed exceptions.

---

## Part F — BIR check, both presets

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py > /tmp/bir_baroque_b3.txt 2>&1; echo "exit:$?"
cat /tmp/bir_baroque_b3.txt; echo "exit:$?"

cd C:\s\MS && python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus; echo "exit:$?"
cd C:\s\MS && python tools/analyze_inversion_errors.py > /tmp/bir_jazz_b3.txt 2>&1; echo "exit:$?"
cat /tmp/bir_jazz_b3.txt; echo "exit:$?"
```

Hard stops: Baroque BIR=false > 25, Jazz BIR=false > 13.
If either is hit: revert all changes in `chordanalyzer.cpp`, report, stop.

---

## Part G — Commit (if clean)

```
cd C:\s\MS && git add src/composing/analysis/chord/chordanalyzer.cpp; echo "exit:$?"
cd C:\s\MS && git commit -m "B3: add dedicated dim7 template {0,3,6,9} (C°7)

Promotes dim7 detection from a bonus-on-triad approach to a proper 4-tone
template alongside the 3-tone Diminished entry. Guard: skip the 4-tone
Diminished template for any root where ♭3 (rootPc+3), ♭5 (rootPc+6), or ♭♭7
(rootPc+9) is absent below extensionThreshold — all four tones must be present.
dim7CharacteristicBonus suppressed when the 4-tone template is active (♭♭7
above threshold) to avoid double-scoring.

Enharmonic rotation ambiguity is unchanged — all four rotations of {0,3,6,9}
score equally; wDim + nextRootPc selects the correct root as before.

BIR: Baroque BIR=true=XX BIR=false=XX; Jazz BIR=true=XX BIR=false=XX.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).
Mismatch: X RealDiff / X ConventionDiff."; echo "exit:$?"
```

---

## Report back

1. Part A findings: 3-tone Diminished template offsets, dim7CharacteristicBonus offset,
   bonus location
2. Whether the bonus suppression in Part C was applied or reverted (and why)
3. All test results (composing / notation / snapshot pass counts)
4. BIR delta Baroque + Jazz (before → after)
5. Mismatch counts
6. Any snapshot goldens updated (and why they are correct)
7. Commit hash or revert notice
