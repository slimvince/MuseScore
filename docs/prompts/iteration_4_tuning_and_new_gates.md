# Iteration 4: Stepwise bonus tuning + first/second inversion gates

## ⚠ Critical behaviour rules for this session

- **Think, investigate, and REPORT before implementing each step.**
  Read the relevant code, describe what you see, then implement. If anything
  does not match this document, STOP and report before proceeding.
- **Make only the changes listed here. Nothing else.**
- **Do not retire `analyzeScore()`.** Deferred.
- **Do not touch `contextualBonuses()`.** No scoring changes there.
- **Do not add new `ChordAnalyzerPreferences` fields.** Gates are conditions, not preferences.
- **Do not commit until all verification steps pass.** Then push as instructed.
- If the build fails or any test regresses unexpectedly, STOP and report verbatim.

---

## Step 1 — Context loading (read ALL before touching any code)

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — full read; authoritative build/test commands
3. `STATUS.md` — top summary line and 2026-05-05 entries only
4. `ARCHITECTURE.md` — §2.10, §4.1c, §4.1d in full
5. `docs/prompts/iteration_plan_inversion_redesign.md` — Iteration 4 section in full

Then read these implementation files before changing anything:

6. `tools/batch_analyze.cpp` — the Baroque preset builder section (search for
   `Baroque`). Confirm:
   - `preferMinorOverMajorAdd6 = true` is set
   - `stepwiseBassInversionBonus`, `stepwiseBassLookaheadBonus`,
     `sameRootInversionBonus`, `completeTriadInversionBonus` are NOT set
     (struct defaults 0.50, 0.50, 0.40, 0.45 apply)
   - Note the stale comment around line 2434–2437 (describes amplification that
     was never coded) — you will fix it in Part A.

7. `src/composing/analysis/chord/chordanalyzer.cpp` — read the full post-ranking
   correction block from the outer guard through the end of the Gates B/C/D block
   (added in Iteration 3). Report:
   - Exact line range of the outer guard
   - Exact line range of the `if (prefs.preferMinorOverMajorAdd6)` block
   - Exact line range of `if (bestAlt != nullptr)`
   - The line immediately after the `if (prefs.preferMinorOverMajorAdd6)` closing
     brace and before `if (!didEnharmonicFlip)` — this is the Gate E/F insertion point
   - Confirm `didEnharmonicFlip` is reused across gates A/B/C/D

8. `src/composing/analysis/chord/chordanalyzer.h` — `ChordAnalyzerPreferences`:
   confirm `bassNoteRootBonus` default (must be 0.70 — the hard ceiling).

After reading, confirm each item in your report before proceeding.

---

## Step 2 — Verify current state before changing anything

A. Baroque preset in `batch_analyze.cpp`: only `preferMinorOverMajorAdd6 = true`
   is set; all four inversion bonuses use struct defaults (0.50/0.50/0.40/0.45).
B. `bassNoteRootBonus` default is 0.70 (the ceiling — no bonus may reach this value).
C. The post-ranking correction block in `chordanalyzer.cpp` contains Gates A/B/C/D
   inside `if (prefs.preferMinorOverMajorAdd6)`. No Gate E or F exists.
D. `didEnharmonicFlip` is shared across all gates — once true, later gates do not fire.
E. There is no `expectedFirstInvAltRoot` or `expectedSecondInvAltRoot` variable yet.

Report A–E. If anything differs, STOP and report.

---

## Part A — Stepwise bonus tuning (batch_analyze.cpp only)

### A1 — Fix the stale comment

Find the comment in `batch_analyze.cpp` around line 2434–2437 that describes
"all inversion bonuses amplified" for Baroque. This comment is inaccurate — no
amplification is coded. Replace it with an accurate comment describing what
Baroque actually sets:

```cpp
// Baroque preset: only preferMinorOverMajorAdd6 differs from Standard.
// Inversion bonuses use struct defaults (stepwiseBassInversionBonus=0.50,
// stepwiseBassLookaheadBonus=0.50, sameRootInversionBonus=0.40,
// completeTriadInversionBonus=0.45). Tuning of these values is tracked
// in docs/prompts/iteration_plan_inversion_redesign.md Iteration 4.
```

Report what you changed.

### A2 — Corpus runs at four bonus values

For each of the four values below, temporarily set `stepwiseBassLookaheadBonus`
in the Baroque preset, rebuild, run the corpus check, and record the numbers.
Do the runs IN ORDER. Reset to the baseline (not set) between each run so you
are testing isolated values.

```
Value    stepwiseBassLookaheadBonus
------   --------------------------
current  not set (default 0.50)    ← already known: 119 / 252
0.55     prefs.stepwiseBassLookaheadBonus = 0.55;
0.60     prefs.stepwiseBassLookaheadBonus = 0.60;
0.65     prefs.stepwiseBassLookaheadBonus = 0.65;
```

For each value:
1. Set the value in the Baroque preset block
2. `cmd.exe //c "C:\s\MS\setup_and_build.bat"`
3. `cd C:\s\MS && python tools/analyze_inversion_errors.py`
4. Record 3-way genuine BIR=true and BIR=false
5. Revert the change before the next run

**Selection rule:** choose the highest value where BIR=false stays ≤ 252.
If no value improves BIR=true without increasing BIR=false, keep the default (0.50).

After all four runs, commit the winning value (or leave at default if no improvement).
Report the full table before committing anything.

---

## Part B — New inversion gates (chordanalyzer.cpp only)

These gates target the two non-enharmonic error families identified in the
Iteration 4 exploration:
- 29 errors where our root is the major 3rd of the correct root (+4 semitones
  from alt root to winner root, i.e. +8 from winner to alt)
- 11 errors where our root is the 5th of the correct root (+7 semitones from
  alt root to winner root, i.e. +5 from winner to alt)

Both gates fire only in bridge paths (P1/P2/P3/P4) since they require
`context != nullptr`. They cannot be verified by corpus runs (batch does not
populate temporal context — §2.10 known limitation). Verification is via
`pipeline_snapshot_tests.exe` and corpus-run BIR=false guard.

### B1 — Gate E: first inversion (winner root is the major 3rd of alt root)

**Location:** inside `if (bestAlt != nullptr)`, after the closing brace of the
`if (prefs.preferMinorOverMajorAdd6)` block, before `if (!didEnharmonicFlip)`.

**Condition:** winner is Minor, alt is Major, winner root is 4 semitones above
alt root (i.e., alt root is 8 semitones above winner root), temporal evidence
present, and gated by `preferMinorOverMajorAdd6`.

```cpp
// ── Gate E: first-inversion detection ─────────────────────────────────────
//
// When the winner is Minor with bassIsRoot=true and the best Major alternative
// has its root a minor-6th above the winner root (= winner root is the major
// 3rd of the alt), the scorer has likely identified the bass note (= 3rd of
// the actual chord) as the root.  E.g., F#m wins when D/F# is correct.
//
// Relationship: altRootPc == (winnerRootPc + 8) % 12
// Gated by preferMinorOverMajorAdd6 (classical presets only) and a stepwise
// bass signal (temporal context required).
if (!didEnharmonicFlip
    && prefs.preferMinorOverMajorAdd6
    && context != nullptr
    && winner.identity.quality == ChordQuality::Minor
    && bestAlt->identity.quality == ChordQuality::Major
    && bestAlt->identity.rootPc == (winner.identity.rootPc + 8) % 12
    && (context->bassIsStepwiseFromPrevious || context->bassIsStepwiseToNext)) {
    std::swap(results[0], results[bestAltIdx]);
    didEnharmonicFlip = true;
}
```

### B2 — Gate F: second inversion (winner root is the 5th of alt root)

**Location:** immediately after Gate E (still inside `if (bestAlt != nullptr)`).

**Condition:** alt is Major, winner root is 7 semitones above alt root (i.e., alt
root is 5 semitones above winner root), temporal evidence present, gated by
`preferMinorOverMajorAdd6`. Winner quality is not restricted (within the existing
Major/Minor guard of the outer block).

```cpp
// ── Gate F: second-inversion detection ────────────────────────────────────
//
// When the best Major alternative has its root a perfect-4th above the winner
// root (= winner root is the 5th of the alt), the scorer has likely identified
// the bass note (= 5th of the actual chord) as the root.
// E.g., B or BAug wins when E/B is correct.
//
// Relationship: altRootPc == (winnerRootPc + 5) % 12
// Gated by preferMinorOverMajorAdd6 (classical presets only) and a stepwise
// bass signal (temporal context required).
if (!didEnharmonicFlip
    && prefs.preferMinorOverMajorAdd6
    && context != nullptr
    && bestAlt->identity.quality == ChordQuality::Major
    && bestAlt->identity.rootPc == (winner.identity.rootPc + 5) % 12
    && (context->bassIsStepwiseFromPrevious || context->bassIsStepwiseToNext)) {
    std::swap(results[0], results[bestAltIdx]);
    didEnharmonicFlip = true;
}
```

After inserting both gates, report the exact code inserted before building.

---

## Step 3 — Build and test

```
cmd.exe //c "C:\s\MS\setup_and_build.bat"
```

### Composing tests

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.
Expect: all pass, RealDiff ≤ 4. If any regression: STOP.

### Notation and pipeline snapshot tests

```
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

`pipeline_snapshot_tests.exe` **may fail** if Gates E/F fire on the 10-score corpus.

**If it fails:**
1. Do NOT run `--update-goldens` yet.
2. Examine the diff — identify which scores changed and what the new identifications are.
3. Verify each change is a correct swap (Minor→Major first inversion or second inversion
   with stepwise bass, enharmonically sensible).
4. Report what changed before refreshing goldens.
5. Only after confirming correctness:
   ```
   cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
   ```
6. Re-run to confirm all pass.

If notation_tests or pipeline_snapshot_tests fails for any reason OTHER than expected
golden mismatches: STOP. Report verbatim.

### Corpus run (final, with winning tuning value and new gates)

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Preset: Baroque. Record BIR=true and BIR=false.
- BIR=true: expect improvement from Part A tuning (batch-measurable)
- BIR=false: must stay ≤ 252
- Gates E/F contribute zero to corpus numbers (batch has no temporal context) —
  this is expected and noted

---

## Step 4 — GitHub push

After clean build + all tests pass + BIR=false ≤ 252:

```
cd C:\s\MS && git add -A && git commit -m "Iter 4: stepwise lookahead tuning + first/second inversion gates E/F" && git push
```

---

## Step 5 — Report

```
Context loading confirmed:         yes / issues: <list>
State verification (A–E):          all confirmed / differences: <list>

Part A — Tuning table:
  stepwiseBassLookaheadBonus=0.50: BIR=true=119, BIR=false=252 (baseline)
  stepwiseBassLookaheadBonus=0.55: BIR=true=N,   BIR=false=N
  stepwiseBassLookaheadBonus=0.60: BIR=true=N,   BIR=false=N
  stepwiseBassLookaheadBonus=0.65: BIR=true=N,   BIR=false=N
  Winning value:                   N (or: no improvement — kept default)
  Stale comment fixed:             yes

Part B — Gates E/F inserted:       yes
  Exact insertion point:           <file:line range>
  Code inserted:                   <paste exact block>

Build:                             pass / fail
Composing tests:                   N/N pass, RealDiff=N
Notation tests:                    N/N pass
Pipeline snapshot tests (before):  N/N pass / N failures
  Changed scores:                  <list>
  Changes verified correct:        yes / no / partial: <describe>
Pipeline snapshot tests (after --update-goldens): N/N pass

Final corpus run:
  Preset:                          Baroque (confirm)
  BIR=true:                        N (from N=119 baseline)
  BIR=false:                       N (must be ≤ 252)
  Improvement from tuning (Part A): N errors
  Improvement from gates E/F:      0 in corpus path (expected — §2.10 limitation)
  Improvement from gates E/F in bridge path: confirmed via snapshot / not observable

GitHub push:                       done / commit hash
Unexpected findings:               none / <describe>
```
