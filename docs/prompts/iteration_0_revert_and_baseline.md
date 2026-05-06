# Iteration 0: Revert harmful changes and establish clean baseline

## ⚠ Critical behaviour rules for this session

- **Think, investigate, and REPORT — do not implement speculatively.**
  If you find anything unexpected, ambiguous, or not covered by this document:
  STOP. Report what you found. Wait for instructions. Do not improvise a fix.
- **Make only the changes listed in the "Changes to make" section below.**
  Do not add improvements, refactor anything extra, or make any change not
  explicitly listed here, no matter how obvious or helpful it seems.
- **Do not commit.** Report results and wait for sign-off.
- If at any point the build fails or a test regresses, STOP immediately and
  report the failure before attempting any further changes.

---

## Step 1 — Context loading (read ALL of these before touching any code)

1. `CLAUDE.md` — standing instructions, build/test commands
2. `STATUS.md` — top summary line and the 2026-05-04 and 2026-05-05 entries only
3. `ARCHITECTURE.md` — read §2.10, §4.1c, and §4.1d in full
4. `docs/unified_analysis_pipeline.md` — read in full
5. `docs/prompts/iteration_plan_inversion_redesign.md` — read in full; this is
   the master plan for this and all subsequent iterations
6. `src/composing/analysis/chord/chordanalyzer.h` — `ChordAnalyzerPreferences`
   struct and `ChordTemporalContext` struct (search for both)
7. `src/composing/analysis/chord/chordanalyzer.cpp` — the `contextualBonuses()`
   function in full (search for `contextualBonuses`)
8. `tools/batch_analyze.cpp` — the preset builder section
   (search for `// ── Build chord analyzer preferences from preset ──`)

After reading, briefly confirm in your report that you have read and understood:
- Why contextual heuristics must not be inside `RuleBasedChordAnalyzer` (§4.1c)
- Why shared logic must not live in `batch_analyze.cpp` (§2.10)
- What the unified pipeline is and why P1/P2/P3/P4 must use one algorithm
- Why inversion score bonuses must stay strictly below `bassNoteRootBonus` (0.70)

---

## Step 2 — Verify current state before changing anything

Search for and confirm the following are present (grep/read as needed):

A. In `ChordAnalyzerPreferences` (chordanalyzer.h), confirm these five fields exist:
   - `nextRootMatchesAltInversionBonus`
   - `consecutiveBassStepwiseInversionBonus`
   - `recentRootMatchesAltInversionBonus`
   - `weakBeatInversionBonus`
   - `weakBeatThreshold`

B. In `contextualBonuses()` (chordanalyzer.cpp), confirm scoring code exists for
   those five signals.

C. In the preset builder (batch_analyze.cpp), confirm Baroque has amplified values
   (0.80) for `stepwiseBassInversionBonus` and `stepwiseBassLookaheadBonus`.

D. In `ChordTemporalContext` (chordanalyzer.h), confirm these fields exist:
   - `nextRootPc`
   - `consecutiveBassStepwiseCount`
   - `recentRootPcs`
   - `regionMetricWeight`

E. Confirm `preferMinorOverMajorAdd6` flag and AddedSixth guard are present in the
   inversion correction block (search for `preferMinorOverMajorAdd6`).

Report what you find for each of A–E. If anything is absent or different from what
is described, report it and STOP — do not proceed to changes until confirmed.

---

## Step 3 — Changes to make

Make ONLY the following changes. Nothing else.

### Change 1 — chordanalyzer.h: remove five preference fields

In `struct ChordAnalyzerPreferences`, remove these five fields entirely:
```
nextRootMatchesAltInversionBonus
consecutiveBassStepwiseInversionBonus
recentRootMatchesAltInversionBonus
weakBeatInversionBonus
weakBeatThreshold
```

Leave `maxTotalInversionContextBonus` in place (it still serves as a safety cap
for the four remaining score-addition signals).

Also add this TODO comment immediately before the four existing inversion bonus
fields (`stepwiseBassInversionBonus` etc.):
```cpp
// TODO (ARCHITECTURE.md §4.1c): These four score-addition signals belong in the
// post-ranking correction layer, not in the vertical sonority scorer. They are
// left here as pre-existing technical debt; do not add further contextual signals
// to this section.
```

### Change 2 — chordanalyzer.cpp: remove scoring code for the five signals

In `contextualBonuses()`, remove the scoring accumulation for the five removed
signals:
- `nextRootMatchesAltInversionBonus` block
- `consecutiveBassStepwiseInversionBonus` block
- `recentRootMatchesAltInversionBonus` block
- `weakBeatInversionBonus` / `weakBeatThreshold` block

Leave the cap accumulation logic for the remaining four signals untouched.
Leave `maxTotalInversionContextBonus` clamping untouched.

### Change 3 — batch_analyze.cpp: revert preset builder inversion values

In the preset builder, make the following changes:

**Baroque preset:**
- Remove `stepwiseBassInversionBonus` assignment (revert to default 0.50)
- Remove `stepwiseBassLookaheadBonus` assignment (revert to default 0.50)
- Remove `sameRootInversionBonus` assignment (revert to default 0.40)
- Remove `completeTriadInversionBonus` assignment (revert to default 0.45)
- Remove `nextRootMatchesAltInversionBonus` assignment (field no longer exists)
- Remove `consecutiveBassStepwiseInversionBonus` assignment (field no longer exists)
- Remove `recentRootMatchesAltInversionBonus` assignment (field no longer exists)
- Remove `weakBeatInversionBonus` assignment (field no longer exists)
- Remove `maxTotalInversionContextBonus` assignment (revert to default 2.0)
- KEEP `preferMinorOverMajorAdd6 = true` — this is correct and working

**Jazz preset:**
- Remove `nextRootMatchesAltInversionBonus` assignment (field no longer exists)
- Remove `consecutiveBassStepwiseInversionBonus` assignment (field no longer exists)
- Remove `recentRootMatchesAltInversionBonus` assignment (field no longer exists)
- Remove `weakBeatInversionBonus` assignment (field no longer exists)
- Remove `maxTotalInversionContextBonus` assignment if present
- Keep all existing Jazz settings (`extensionThreshold`, `preferMinorOverMajorAdd6 = false`,
  and any reduced values for the four remaining inversion signals if they were set)

**Do NOT touch:**
- The `ChordTemporalContext` fields (`nextRootPc`, `consecutiveBassStepwiseCount`,
  `recentRootPcs`, `regionMetricWeight`) — leave their population in the batch loop
  exactly as is. They are not used in scoring now but will be used as gate conditions
  in a future iteration.
- `preferMinorOverMajorAdd6` — leave as is for all presets
- The enharmonic fast path / AddedSixth guard — do not touch at all
- Any file outside `chordanalyzer.h`, `chordanalyzer.cpp`, `batch_analyze.cpp`

---

## Step 4 — Build and test

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.

If build fails or any test regresses: STOP. Report the failure verbatim. Do not
attempt to fix it — wait for instructions.

---

## Step 5 — Corpus analysis

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

The corpus JSON files must be regenerated using the new binary with `--preset Baroque`
before running the script. Check `run_bach_preset.py` or equivalent for the correct
invocation. Confirm the preset used in your report.

---

## Step 6 — GitHub push (backup)

After a clean build and passing tests, push to GitHub:
```
cd C:\s\MS && git add -A && git commit -m "Revert: remove harmful inversion bonus amplification and four new scoring signals" && git push
```

Only push if build passes and 407/407 tests pass. If tests fail, do not push.

---

## Step 7 — Report

```
Architecture understanding confirmed: yes/no + one sentence per rule
State verification (A–E):            confirmed / differences found: <list>
Changes made:                         list of files and what changed
Build:                                pass / fail
Tests:                                407/407 pass / N failures: <list>
RealDiff:                             before=4, after=N
Corpus preset used:                   Baroque (confirm explicitly)
3-way genuine BIR=true:               before=66, after=N
3-way genuine BIR=false:              before=364, after=N
2-way bassIsRoot:                     before=620, after=N
Chord identity:                       before=80.3%, after=N%
GitHub push:                          done / skipped (reason)
Unexpected findings:                  none / <describe>
```
