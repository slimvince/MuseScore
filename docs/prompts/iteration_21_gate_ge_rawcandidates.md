# Iteration 21: Extend Gate G-E to reach rawCandidates

## Background

Iter 20 diagnostic established: Gate G-E fires correctly for 21 of the 24
Cat 2 Minor→HalfDim cases — but only in the `inferNextRootPc` look-ahead
(ctx=nullptr, no rootContinuityBonus). In the main `analyzeChord` call the
rootContinuityBonus raises Am6's score enough to push the HalfDim candidate
below the `results[]` threshold; `halfDimAltIdx` search finds nothing; gate
cannot fire.

The 3 remaining Cat 2 cases (bwv40.3, bwv40.8, bwv407) are WRONG-PC: the
HalfDim's rootPc does not fall on gLT, gST, or gMed. They are not targeted
here and must not be affected.

**Expected outcome:** BIR=true 98 → ~77 (21 fixes). BIR=false must not rise.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=98, BIR=false=788

---

## Step 2 — Read and report relevant code sections

Read `src/composing/analysis/chord/chordanalyzer.cpp` and report verbatim:

**A.** The `rawCandidates` variable declaration and the section where `results`
   is populated from it (the filtering/sorting step). Confirm whether
   `rawCandidates` is still in scope — and still contains all candidates
   including low-scoring ones — at the point where Gate G's outer `if` is
   reached.

**B.** The existing "guaranteed-alt append block" (if one exists). This is any
   block that explicitly pushes a candidate into `results[]` even when it did
   not score above the normal threshold. Report its location, condition, and
   mechanism verbatim.

**C.** The full Gate G-E block as it stands after Iter 18: the outer `if`,
   the `halfDimAltIdx` search loop, and the inner swap `if`.

Report all three sections before writing any code.

---

## Step 3 — Implement the rawCandidates extension

**Goal:** when the Gate G outer condition is met (`originalWinnerQuality ==
Minor && originalWinnerHasAddedSixth && prefs.preferMinorOverMajorAdd6`) but
the `halfDimAltIdx` search finds no HalfDim candidate in `results[]`, search
`rawCandidates` for a HalfDim candidate whose rootPc equals gLT, gST, or gMed
and, if found, append it to `results[]` so that the subsequent Gate G-E inner
condition can fire normally.

Implement this as a new block IMMEDIATELY AFTER the existing `halfDimAltIdx`
search loop and BEFORE the Gate G-E inner `if`:

```cpp
// Gate G-E: if HalfDim not in results[], look in rawCandidates (temporal
// context may have suppressed it via rootContinuityBonus)
if (halfDimAltIdx >= results.size()) {
    const int gLT  = (keyTonicPc + 11) % 12;
    const int gST  = (keyTonicPc +  2) % 12;
    const int gMed = (keyTonicPc +  4) % 12;
    for (const auto& rc : rawCandidates) {
        if (rc.identity.quality == ChordQuality::HalfDiminished
            && (rc.identity.rootPc == gLT
                || rc.identity.rootPc == gST
                || rc.identity.rootPc == gMed)) {
            results.push_back(rc);
            halfDimAltIdx = results.size() - 1;
            break;
        }
    }
}
```

**Important constraints:**
- Insert this block ONLY inside the already-open Gate G outer `if` block,
  after the `halfDimAltIdx` search loop.
- The existing `halfDimAltIdx` search loop and inner swap `if` must remain
  UNCHANGED.
- If `keyTonicPc` is not already computed at this scope, use the existing
  value (do not recompute). The three pitch-class variables (gLT, gST, gMed)
  may already exist from the inner `if` — if so, do not re-declare them; move
  or reuse them appropriately.
- If `rawCandidates` has a different name in the actual code, use the correct
  name from Step 2 findings.
- Do not change the guaranteed-alt append block or any other gate.

Report the exact lines inserted and their surrounding context (5 lines before
and after).

---

## Step 4 — Build and run all tests

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Expected: build pass (warnings only), 407/407, 53/53, 11/11.

Any test failure or new warning: **STOP and report verbatim.**

---

## Step 5 — Run corpus analysis

```
cd C:\s\MS && python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Report the new BIR=true and BIR=false counts.

Expected: BIR=true ≈77 (21 fixes from 98), BIR=false = 788 (unchanged).

**If BIR=false rises above 788: STOP and report verbatim. Do not proceed.**

**If BIR=true improvement is significantly fewer than 21 (e.g. ≤5): STOP and
report — the fix may not be reaching the right code path.**

---

## Step 6 — If results are clean: update pipeline snapshot goldens

If BIR=true improved by 15 or more AND BIR=false ≤ 788 AND all unit tests
passed:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
```

Confirm pipeline snapshot tests pass after golden update.

---

## Step 7 — Update baselines and STATUS.md

Update `build_and_test.md`:
- Replace BIR=true baseline with the actual new count
- Update attribution line to Iteration 21

Update `STATUS.md` with a 2026-05-07 entry:
```
Iter 21: Gate G-E rawCandidates extension
- Diagnosis (Iter 20): Gate G-E fired correctly in inferNextRootPc look-ahead
  (ctx=null) for 21 Am6/HalfDim cases, but main pass excluded HalfDim from
  results[] due to rootContinuityBonus raising Am6's effective threshold
- Fix: when halfDimAltIdx not found in results[], search rawCandidates for
  HalfDim at gLT/gST/gMed and append to results[] before Gate G-E fires
- Net improvement: BIR=true 98→N (21 targeted fixes; 3 WRONG-PC cases unaffected)
- BIR=false: unchanged at 788
- New baselines: BIR=true=N, BIR=false=788
```
(Replace N with the actual count.)

---

## Step 8 — Commit and push

```
cd C:\s\MS && git add -A && git commit -m "Iter 21: Gate G-E rawCandidates fallback — reach HalfDim suppressed by temporal context [N BIR=true fixes, M remaining]" && git push
```
(Replace N and M with actual numbers.)

---

## Step 9 — Report

```
Code change:
  File: chordanalyzer.cpp
  Location: Gate G-E, after halfDimAltIdx search loop
  Lines inserted: N–N

Build:               pass
Composing tests:     407/407
Notation tests:      53/53
Pipeline snapshots:  11/11
BIR=true:            N  (was 98, improved by N)
BIR=false:           788

Pipeline goldens updated: yes / no (if no improvement ≥15, goldens not updated)
build_and_test.md updated: yes
STATUS.md updated:         yes
GitHub push:               done — [commit hash]
```
