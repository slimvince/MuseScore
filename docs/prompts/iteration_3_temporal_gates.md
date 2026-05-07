# Iteration 3: Temporal gates B/C/D in post-ranking correction

## ⚠ Critical behaviour rules for this session

- **Think, investigate, and REPORT before implementing each step.**
  Read the relevant code section, describe what you see and what you plan to change,
  then implement. If anything does not match what this document describes, STOP
  and report before proceeding.
- **Make only the changes listed in this document.** Do not refactor, improve,
  or simplify anything not explicitly listed here.
- **Touch only `chordanalyzer.cpp`.** No other file changes in this iteration.
- **Do not add anything to `ChordAnalyzerPreferences`.** Gates are conditions,
  not preference fields.
- **Do not change any score values.** Gates make a direct swap decision — they
  do not modify scores.
- **Do not touch `contextualBonuses()`.** No changes to that function.
- **Do not touch the existing AddedSixth guard condition.** Leave it exactly as is.
- **Do not commit until all verification steps pass.** Then push as instructed.
- If the build fails or any test regresses unexpectedly, STOP immediately and
  report verbatim. Do not attempt to fix.

---

## Step 1 — Context loading (read ALL before touching any code)

1. `CLAUDE.md` — standing instructions, build/test commands
2. `build_and_test.md` — authoritative build and test commands; read in full
3. `STATUS.md` — top summary line and the 2026-05-05 Iterations 0–2 entry only
4. `ARCHITECTURE.md` — §2.10, §4.1c, §4.1d in full
5. `docs/unified_analysis_pipeline.md` — in full
6. `docs/prompts/iteration_plan_inversion_redesign.md` — Iteration 3 section in full

Then read these implementation files before changing anything:

7. `src/composing/analysis/chord/chordanalyzer.h`:
   - `ChordQuality` enum — note what quality values exist (confirm there is NO
     `Minor7` quality — minor seventh is an *extension*, not a quality)
   - `ChordTemporalContext` struct — confirm the four fields `nextRootPc`,
     `consecutiveBassStepwiseCount`, `recentRootPcs`, `regionMetricWeight` are
     present (added in Iteration 2)
   - `ChordAnalyzerPreferences` struct — confirm `preferMinorOverMajorAdd6` field
     exists; confirm there is NO gate-related field

8. `src/composing/analysis/chord/chordanalyzer.cpp` — read the **full
   post-ranking correction block**: from the comment
   `// non-bass alternative (margin < inversionSuspicionMargin)` through to the
   end of the inversion correction (search for `didEnharmonicFlip`). Read every
   line. Report:
   - Exact line numbers of the outer guard (`if (prefs.inversionSuspicionMargin > 0.0 ...`)
   - Exact line numbers of the `if (prefs.preferMinorOverMajorAdd6)` block
   - Exact line numbers and condition of the existing AddedSixth guard
   - All variable names in scope at the gate insertion point
   - Whether `context` (the `ChordTemporalContext*` parameter) is accessible there
   - Whether `!didEnharmonicFlip` correctly represents "the AddedSixth guard did
     not fire"

After reading, confirm each item in your report before proceeding to Step 2.

---

## Step 2 — Verify current state before changing anything

Confirm:

A. The `ChordQuality` enum has: Unknown, Major, Minor, Diminished, Augmented,
   HalfDiminished, Suspended2, Suspended4, Power — and NO `Minor7` value.
B. `ChordTemporalContext` has all four new fields from Iteration 2:
   `nextRootPc`, `consecutiveBassStepwiseCount`, `recentRootPcs`, `regionMetricWeight`.
C. The existing AddedSixth guard fires on:
   `winnerIsMajor && winnerHasAddedSixth && altIsMinor && bestAlt->identity.rootPc == expectedAltRoot`
   (or equivalent variable names — report the exact condition as written).
D. No gates B/C/D exist yet anywhere in the file.
E. `context` (type `const ChordTemporalContext*`) is a parameter of `analyzeChord`
   and is accessible at the gate insertion point.
F. `didEnharmonicFlip` is initialised to `false` before the AddedSixth guard and
   is set to `true` when the guard fires.

Report findings for A–F. If anything differs, report and STOP.

---

## Step 3 — Change to make

### The only change: add Gates B, C, D to `chordanalyzer.cpp`

**Location:** Inside the `if (prefs.preferMinorOverMajorAdd6)` block, immediately
after the closing brace of the existing AddedSixth guard `if` statement (the one
that sets `didEnharmonicFlip = true`), and before the closing brace of the
`if (prefs.preferMinorOverMajorAdd6)` block.

**Prerequisites shared by all three gates:**

```cpp
if (!didEnharmonicFlip
    && context != nullptr
    && winnerIsMajor
    && altIsMinor
    && bestAlt->identity.rootPc == expectedAltRoot)
```

Use whatever variable names Step 1 confirmed are in scope. The important point
is that all three gates require:
- The AddedSixth guard did NOT already fire (`!didEnharmonicFlip`)
- `context` is non-null (temporal data is available)
- The winner is Major quality
- The best alternative is Minor quality
- The enharmonic pair relationship holds (`bestAlt->identity.rootPc == expectedAltRoot`)

Note: the gates deliberately do NOT require `winnerHasAddedSixth`. The gates are
designed to catch cases where the AddedSixth guard fails — for example, when a weak
note at interval 10 (minor seventh) suppresses AddedSixth detection even though the
sixth is present. The temporal evidence alone is sufficient justification.

**Gate B — next chord confirms this harmony:**

```cpp
// Gate B: the next region's inferred root matches the alternative (Minor) root.
// Strong forward evidence that this harmony persists — the bass is passing through
// a chord tone, not establishing a new root.
if (!didEnharmonicFlip
    && context != nullptr
    && winnerIsMajor && altIsMinor
    && bestAlt->identity.rootPc == expectedAltRoot
    && context->nextRootPc != -1
    && context->nextRootPc == bestAlt->identity.rootPc) {
    std::swap(results[0], results[bestAltIdx]);
    didEnharmonicFlip = true;
}
```

**Gate C — root was recently active and bass is moving stepwise:**

```cpp
// Gate C: the alternative root appears in the 3-region window AND the bass is
// moving stepwise from the previous region.  The root has been recently active
// and the bass is passing through it — strong evidence of an inversion.
const auto& rpc = context->recentRootPcs;
const bool altRootIsRecent = (rpc[0] == bestAlt->identity.rootPc
                              || rpc[1] == bestAlt->identity.rootPc
                              || rpc[2] == bestAlt->identity.rootPc);
if (!didEnharmonicFlip
    && context != nullptr
    && winnerIsMajor && altIsMinor
    && bestAlt->identity.rootPc == expectedAltRoot
    && context->bassIsStepwiseFromPrevious
    && altRootIsRecent) {
    std::swap(results[0], results[bestAltIdx]);
    didEnharmonicFlip = true;
}
```

Note: declare `rpc` and `altRootIsRecent` only if `context != nullptr`. Either
wrap them inside the prerequisite check or guard the declaration. Do not
dereference a null pointer.

**Gate D — scalar bass line:**

```cpp
// Gate D: two or more consecutive stepwise bass moves ending here.
// A scalar bass line is strong evidence of a passing inversion, not a new root.
if (!didEnharmonicFlip
    && context != nullptr
    && winnerIsMajor && altIsMinor
    && bestAlt->identity.rootPc == expectedAltRoot
    && context->consecutiveBassStepwiseCount >= 2) {
    std::swap(results[0], results[bestAltIdx]);
    didEnharmonicFlip = true;
}
```

**Important:** each gate independently triggers the same swap and sets
`didEnharmonicFlip = true`. Once any gate fires, the remaining gates do not
fire (because of `!didEnharmonicFlip`). This is intentional.

After implementing, report the exact code you inserted (full block) before
moving to the build step.

---

## Step 4 — Build and test

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
```

### Composing tests

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.
Expect: all tests pass, RealDiff ≤ 4.
If any test regresses: STOP. Report verbatim.

### Notation tests

```
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
```

The `pipeline_snapshot_tests` (P1–P4 golden snapshot test) **may fail** if gates
B/C/D fire on the 10-score corpus. This is EXPECTED — the gates are working.

**If pipeline_snapshot_tests fails:**
1. Do NOT run `--update-goldens` yet.
2. Examine the diff output to identify which scores changed and what the new
   chord identifications are.
3. Verify manually that each change is a correct swap (Minor replacing Major,
   enharmonic pair relationship holding, temporal evidence present).
4. Report which scores changed and what changed before refreshing goldens.
5. Only after confirming the changes are correct, run:
   ```
   cd C:\s\MS\ninja_build_rel && ./notation_tests.exe --update-goldens
   ```
6. Then re-run `./notation_tests.exe` and confirm all tests now pass.

If notation_tests fails for any reason OTHER than expected golden mismatches
(e.g. a crash, a non-snapshot test failure): STOP. Report verbatim.

---

## Step 5 — Corpus run

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Preset: Baroque (confirm explicitly in report).

**Expected direction:**
- 3-way genuine BIR=true: below 119 (genuine reduction — gates should fire on
  some Bb6→Gm7/Bb type errors)
- 3-way genuine BIR=false: ≤ 252 (must not increase — gates must not create new
  false positives)

If BIR=false increases above 252: STOP. Report verbatim. Do not push.

---

## Step 6 — Gates breakdown

Without making code changes, report which gate fired on how many of the resolved
errors. If the corpus tool does not provide per-gate breakdown, report the overall
reduction and note that per-gate breakdown requires diagnostic output not currently
available.

---

## Step 7 — GitHub push

After clean build + all tests pass + corpus BIR=false ≤ 252:

```
cd C:\s\MS && git add -A && git commit -m "Temporal gates B/C/D: enharmonic inversion correction via progression context" && git push
```

---

## Step 8 — Report

```
Context loading confirmed:         yes / issues: <list>
State verification (A–F):          all confirmed / differences: <list>
Code inserted (exact block):       <paste the full inserted block>
Build:                             pass / fail
Composing tests:                   N/N pass, RealDiff = N
Notation tests (before goldens):   pass / N failures in pipeline_snapshot_tests
  Changed scores:                  <list score IDs and what changed>
  Changes verified correct:        yes / no / partial: <describe>
Notation tests (after --update-goldens): N/N pass
Corpus preset:                     Baroque (confirm)
3-way genuine BIR=true:            before=119, after=N
3-way genuine BIR=false:           before=252, after=N
Gates breakdown:
  Gate B (nextRootPc match):       N swaps
  Gate C (recentRoot + stepwise):  N swaps
  Gate D (consecutiveStepwise≥2):  N swaps
GitHub push:                       done / commit hash
Unexpected findings:               none / <describe>
```
