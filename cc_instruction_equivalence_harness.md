# CC Instruction: Build Equivalence Harness (suppressed + fn == non-suppressed)

## Pre-reading

Read `C:\s\MS\STATUS.md` and `C:\s\MS\build_and_test.md` before starting.
Current HEAD: `0ab219d4c5` (Phase 1 / E2d-prereq). All tests pass.

---

## Goal

Build a measurement harness — a new test that, for every region in the existing
test corpus, runs the same chord through two pipelines and checks whether the
final winner matches:

| Pipeline A (baseline) | Pipeline B (suppressed + function layer) |
|---|---|
| `analyzeChord(suppress=false)` | `analyzeChord(suppress=true, captureScoringSnapshot=true)` |
| `applyHarmonicFunction(…, nullptr, nullptr)` (no-op) | `applyHarmonicFunction(…, &snapshot, &prefsSuppress)` |
| `applyIter8691Pedal` | `applyIter8691Pedal` |
| `applyPostScoringGates` | `applyPostScoringGates` |

**Expected outcome today**: many divergences (the function layer is currently
incomplete). That is fine — the harness is a measurement tool, not an assertion.
It must build, run, and write a report. It must **not** fail the test suite.

After any future redesign the harness becomes the acceptance criterion: zero
divergences = redesign correct.

---

## Implementation

### 1. New test file

Create `src/composing/tests/equivalence_harness_test.cpp`.

The test body must:

1. Locate and load the same MusicXML corpus files used by the existing
   composing tests (read the existing test fixture setup to find how they
   are located; do not hard-code paths).

2. For each score and each region produced by that score's region analysis:

   a. Reconstruct the inputs needed for both calls:
      `tones`, `localKeyFifths`, `localKeyMode`, `temporalCtx`,
      `attemptPrefs` (baseline, suppress=false),
      `prefsSuppress` (suppress=true, `captureScoringSnapshot = &snapshot`).

   b. Obtain `fnCtx` (HarmonicFunctionContext) from the region's
      `temporalCtx` the same way regionanalyzer.cpp does it at its Pass-1
      call site.

   c. Run **Pipeline A** (baseline):
      - `analyzeChord(tones, …, attemptPrefs, &gateCtxA)` → `resultsA`
      - `applyHarmonicFunction(resultsA, chosenA, fnCtx, nullptr, nullptr)`
      - `applyIter8691Pedal(resultsA, gateCtxA, …)`
      - `applyPostScoringGates(resultsA, …, gateCtxA)`
      - record `resultsA.front().identity` as the reference winner.

   d. Run **Pipeline B** (suppressed + fn):
      - `function::ScoringSnapshot snapshot;`
      - Set `prefsSuppress.suppressProgressionSignals = true` and
        `prefsSuppress.captureScoringSnapshot = &snapshot`.
      - `analyzeChord(tones, …, prefsSuppress, &gateCtxB)` → `resultsB`
      - `applyHarmonicFunction(resultsB, chosenB, fnCtx, &snapshot, &prefsSuppress)`
      - `applyIter8691Pedal(resultsB, gateCtxB, …)`
      - `applyPostScoringGates(resultsB, …, gateCtxB)`
      - record `resultsB.front().identity` as the suppressed winner.

   e. Compare the two winners on: `bassPc`, `rootPc`, `quality`, `tiePriority`.
      Count as a match only if all four agree.

3. Accumulate counts: `totalRegions`, `matchCount`, `divergeCount`.
   For each divergence keep: score name, tick/region index,
   Pipeline-A winner (bassPc, rootPc, quality), Pipeline-B winner.

4. Write the report to
   `src/composing/tests/equivalence_harness_report.txt` in this format:

   ```
   Equivalence Harness Report
   HEAD: <git rev-parse HEAD>
   Date: <ISO-8601>

   Total regions tested : <N>
   Match                : <N>
   Diverge              : <N>  (<pct>%)

   --- Divergences (first 40) ---
   <score>  tick=<T>  A=<bassPc>/<rootPc>/<quality>  B=<bassPc>/<rootPc>/<quality>
   …
   ```

5. End with `SUCCEED()` so the harness never fails the suite, regardless
   of the divergence count.

### 2. Wire into the build

Add the new file to `src/composing/tests/CMakeLists.txt` (or whichever
CMakeLists governs composing_tests). Link against the same targets as the
other test files in that directory.

Do **not** modify any production source file.

---

## Build and run

```
# Build
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"

# Run full composing test suite (harness included)
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/harness_run.txt 2>&1; echo "exit:$?"
head -60 /tmp/harness_run.txt

# Read the harness report
cat src/composing/tests/equivalence_harness_report.txt
```

Both `composing_tests.exe` and `notation_tests.exe` must still pass after
this change. The harness may show divergences — that is expected.

---

## Output

1. The harness file committed (or ready to commit — defer commit until told).
2. `src/composing/tests/equivalence_harness_report.txt` written and forwarded
   in full.
3. A short summary:
   - Total regions tested.
   - Divergence count and percentage.
   - Two or three representative divergence examples (score, tick,
     Pipeline A winner vs Pipeline B winner).
   - Any compile errors or unexpected runtime issues encountered.
