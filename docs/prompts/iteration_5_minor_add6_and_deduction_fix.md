# Iteration 5: Minor-add6/HalfDim7 gate (G) + deduction neutralization fix

## ⚠ Critical behaviour rules for this session

- **Think, investigate, and REPORT before implementing each step.**
  Read the relevant code, describe what you see, then implement. If anything
  does not match this document, STOP and report before proceeding.
- **Make only the changes listed here. Nothing else.**
- **Do not touch `contextualBonuses()`.** No scoring changes there.
- **Do not add new `ChordAnalyzerPreferences` fields.** Gates are conditions, not preferences.
- **Do not commit until all verification steps pass.** Then push as instructed.
- If the build fails or any test regresses unexpectedly, STOP and report verbatim.

---

## Background

The Iteration 4b diagnostic identified two root causes for why 73 enharmonic-pair
errors resist correction:

**Root Cause 1 (primary, ~63% of errors):**
Winner = Minor + AddedSixth (e.g. Cm6 = C–Eb–G–A).
The correct alt is HalfDiminished at `(winnerRootPc + 9) % 12` (e.g. Am7b5).
These share the same 4 pitch classes — a second enharmonic equivalence pair.
`kCleanQualities = {Major, Minor}` excludes HalfDiminished from the `bestAlt`
search → `bestAlt = nullptr` → the entire correction block is unreachable.
Fix: Gate G, a categorical swap parallel to Gate A.

**Root Cause 2 (secondary, ~16% of errors):**
The margin-based fallback deducts from `results[0]` only. When `results[1]`
shares the original winner's rootPc (e.g. Cm7 after Cm), it also carries
`bassNoteRootBonus` and rises to rank 1 after `stable_sort`, neutralizing
the deduction.
Fix: apply the deduction to ALL candidates with the original winner's rootPc.

---

## Step 1 — Context loading (read ALL before touching any code)

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — full read; authoritative build/test commands
3. `STATUS.md` — top summary line and 2026-05-05 entries only
4. `ARCHITECTURE.md` — §2.10, §4.1c, §4.1d in full

Then read these implementation sections before changing anything:

5. `src/composing/analysis/chord/chordanalyzer.cpp` — the full post-ranking
   correction block from the outer guard through the deduction fallback. Confirm:
   - Exact line of the outer guard: `if (prefs.inversionSuspicionMargin > 0.0 ...)`
   - Exact line of `if (winnerBassIsRoot && winnerQualityTargeted)`
   - Exact line where `const ChordAnalysisResult* bestAlt = nullptr;` is declared
   - Exact line of `if (bestAlt != nullptr)`
   - Exact line of `bool didEnharmonicFlip = false;`
   - Exact lines of the deduction fallback (`results[0].identity.score -= ...`
     through the closing `}` of `if (!didEnharmonicFlip)`)
   - Confirm that `winner` is declared as `const ChordAnalysisResult& winner = results[0];`
     at the top of the outer guard

6. `src/composing/analysis/chord/chordanalyzer.h` — confirm:
   - `bassNoteRootBonus` default (must be 0.70)
   - `inversionSuspicionMargin` default
   - `inversionBonusReduction` default

After reading, report the line numbers and confirm each item before proceeding.

---

## Step 2 — Verify current state before changing anything

A. Inside `if (winnerBassIsRoot && winnerQualityTargeted)`, the first statement
   is the `static constexpr kCleanQualities` array containing only
   `ChordQuality::Major` and `ChordQuality::Minor`.
B. `ChordQuality::HalfDiminished` is NOT in `kCleanQualities`.
C. No gate currently handles winner = Minor + AddedSixth searching for a
   HalfDiminished alt.
D. The deduction fallback applies `results[0].identity.score -= deduction`
   to `results[0]` only (single line, not a loop).
E. `didEnharmonicFlip` is declared INSIDE `if (bestAlt != nullptr)`.

Report A–E. If anything differs, STOP and report.

---

## Part A — Gate G: Minor-add6 ↔ HalfDim7

### Musical reasoning

Cm6 (C–Eb–G–A) and Am7b5 (A–C–Eb–G) span identical pitch classes. In
Baroque/Classical context the half-diminished seventh reading is always
preferred over the minor-add-6 reading. This is the second enharmonic
equivalence pair; Gate A covers Major-add6 ↔ Minor7, Gate G covers the
symmetric Minor-add6 ↔ HalfDim7.

### A1 — Location

Gate G is inserted immediately BEFORE the `const ChordAnalysisResult* bestAlt`
declaration, inside `if (winnerBassIsRoot && winnerQualityTargeted) {`.

After inserting Gate G, the existing bestAlt search and the entire
`if (bestAlt != nullptr)` block (including all of Gates A–F and the deduction
fallback) must be wrapped in `if (!didGateGFire) { ... }`.

The `winner` reference is declared before Gate G and is valid at the time Gate G
reads `winner.identity.rootPc` and `winner.identity.extensions`. After the swap
in Gate G, `winner` (being a reference to `results[0]`) reflects the new rank-1
candidate, but `didGateGFire = true` prevents any further use.

### A2 — Code to insert (before the bestAlt declaration)

```cpp
// ── Gate G: Minor-add6 ↔ HalfDim7 ────────────────────────────────────────
//
// Symmetric to Gate A (Major-add6 ↔ Minor7). When the winner is a Minor chord
// with an added sixth, it shares all four pitch classes with the half-diminished
// seventh whose root lies a minor third above the winner root (9 semitones mod 12):
//   halfDimRootPc == (winnerRootPc + 9) % 12
// In Baroque/Classical context, the half-diminished seventh reading is always
// preferred over the minor-add-6 reading.
//
// Unlike Gates B–F, this gate requires no temporal context — it fires on
// structural grounds alone, like Gate A.
// Gated by preferMinorOverMajorAdd6 (classical presets only).
bool didGateGFire = false;
if (prefs.preferMinorOverMajorAdd6
    && winner.identity.quality == ChordQuality::Minor
    && hasExtension(winner.identity.extensions, Extension::AddedSixth)) {
    const int expectedHalfDimRootPc = (winner.identity.rootPc + 9) % 12;
    for (size_t i = 1; i < results.size(); ++i) {
        if (results[i].identity.rootPc == expectedHalfDimRootPc
            && results[i].identity.quality == ChordQuality::HalfDiminished) {
            std::swap(results[0], results[i]);
            didGateGFire = true;
            break;
        }
    }
}
```

### A3 — Wrap the existing bestAlt block

Immediately after the Gate G block, change:

```cpp
// Find the best alternative that has clean (Major or Minor) quality.
static constexpr std::array<ChordQuality, 2> kCleanQualities = { ...
```

to:

```cpp
if (!didGateGFire) {
    // Find the best alternative that has clean (Major or Minor) quality.
    static constexpr std::array<ChordQuality, 2> kCleanQualities = { ...
```

And close the `if (!didGateGFire)` block at the end of the existing
`if (bestAlt != nullptr) { ... }` closing brace, so the structure becomes:

```cpp
if (!didGateGFire) {
    // [kCleanQualities declaration — unchanged]
    // [bestAlt search loop — unchanged]
    // [if (bestAlt != nullptr) { ... } — unchanged, including all Gates A–F
    //  and the deduction fallback]
}  // end if (!didGateGFire)
```

**Do not modify anything inside the existing bestAlt block.**

After inserting, report the exact line ranges added, the exact line of the new
opening `if (!didGateGFire) {`, and the exact line of its closing `}`.

---

## Part B — Fix deduction neutralization

### B1 — Location

Inside `if (!didEnharmonicFlip)` → `if (!seventhExempt && margin < prefs.inversionSuspicionMargin)`.

The current deduction is a single line:
```cpp
results[0].identity.score -= deduction;
```
followed immediately by `std::stable_sort(...)`.

### B2 — Fix

Replace the single deduction line with a loop that applies the same deduction
to every candidate in `results` that shares the original winner's rootPc.
Store the original rootPc BEFORE the loop (since the sort will change
`results[0]`):

**Old code (single line):**
```cpp
results[0].identity.score -= deduction;
std::stable_sort(results.begin(), results.end(),
                 [](const ChordAnalysisResult& a,
                    const ChordAnalysisResult& b) {
                     return a.identity.score > b.identity.score;
                 });
```

**New code (loop over same-root candidates):**
```cpp
// Apply the deduction to all candidates sharing the original winner's
// root — not just results[0].  Without this, same-root templates
// (e.g. Cm7 after Cm was deducted) rise to rank 1 and neutralize
// the correction.
const int originalWinnerRootPc = results[0].identity.rootPc;
for (auto& cand : results) {
    if (cand.identity.rootPc == originalWinnerRootPc) {
        cand.identity.score -= deduction;
    }
}
std::stable_sort(results.begin(), results.end(),
                 [](const ChordAnalysisResult& a,
                    const ChordAnalysisResult& b) {
                     return a.identity.score > b.identity.score;
                 });
```

Use the SAME `deduction` value and the SAME comparator lambda that the
existing code uses. Do not change any other logic in this block.

After implementing, paste the old code and the new code in the report.

---

## Step 3 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

### Composing tests

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
```

Read `src/composing/tests/chord_mismatch_report.txt`.
Expect: all pass, RealDiff ≤ 4. If any regression: STOP and report verbatim.

### Notation and pipeline snapshot tests

```
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

`pipeline_snapshot_tests.exe` **may fail** if Gate G or the deduction fix
alters output on the 10-score corpus.

**If it fails:**
1. Do NOT run `--update-goldens` yet.
2. Examine the diff — identify which scores changed and what the new identifications are.
3. For Gate G changes: verify each is a genuine Minor-add6 → HalfDim7 flip
   (enharmonically sensible in Baroque/Classical context).
4. For deduction-fix changes: verify each is a correct inversion correction
   (the new rank-1 is a better enharmonic reading than the now-deducted candidates).
5. Report ALL changed scores and your assessment of correctness before updating.
6. Only after confirming each change is correct:
   ```
   cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
   ```
7. Re-run to confirm all pass.

If notation_tests or pipeline_snapshot_tests fails for any reason OTHER than
expected golden mismatches: STOP and report verbatim.

### Corpus run

```
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Preset: Baroque. Record BIR=true and BIR=false.
- BIR=true baseline: 119 (commit 41913a7cf9)
- BIR=false baseline: 252 — must NOT increase

Both Gate G and the deduction fix are batch-measurable (they do not require
temporal context). Expect meaningful improvement to BIR=true from both fixes.
Report the BIR=true improvement separately attributed to each fix if possible
(run with only Part A active, then add Part B), or report the combined number.

---

## Step 4 — Update STATUS.md

Add a 2026-05-05 entry documenting:
- What Iteration 5 did (Gate G for MinorAdd6/HalfDim7, deduction neutralization fix)
- The corpus result (BIR=true before → after, BIR=false)
- The commit hash

---

## Step 5 — GitHub push

After clean build + all tests pass + BIR=false ≤ 252:

```
cd C:\s\MS && git add -A && git commit -m "Iter 5: MinorAdd6/HalfDim7 gate G + fix deduction neutralization" && git push
```

---

## Step 6 — Report

```
Context loading confirmed:         yes / issues: <list>
State verification (A–E):          all confirmed / differences: <list>

Part A — Gate G:
  Insertion point (line before):   <line number of bestAlt declaration>
  Gate G block lines:              <line range>
  if (!didGateGFire) wraps lines:  <line range>
  Code inserted:                   <paste exact Gate G block>

Part B — Deduction fix:
  Old code:                        <paste>
  New code:                        <paste>

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
  Improvement from Gate G alone:   N errors (if measured separately)
  Improvement from deduction fix:  N errors (if measured separately)
  Combined improvement:            N errors

STATUS.md updated:                 yes
GitHub push:                       done / commit hash
Unexpected findings:               none / <describe>
```
