# CC Instruction: Redesign Step 2 — Predecessor confidence channel

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), `C:\s\MS\build_and_test.md`,
and `C:\s\MS\docs\redesign_plan.md` before starting.

This is **Step 2** of the redesign sequence. Step 1 (free wiring) is complete at
commit `a6d289c461`.

---

## What this task is — and is not

**Is:** Infrastructure only. Four new fields added to `ChordTemporalContext` and
forwarded to `HarmonicFunctionContext`. No new scoring logic reads them.

**Is not:** A scoring change. `harmonicfunctionlayer.cpp` must not be modified.
Expected result: **byte-identical** — same BIR numbers, zero snapshot goldens changed.

---

## Background: the inter-region channel gap

After `applyHarmonicFunction` selects a winner and `advanceTemporalContext` commits it,
the next region's competition pipeline receives only the committed identity (rootPc,
bassPc, quality). It has no way to know how confident that commitment was.

`rootContinuityBonus` applies a flat +0.40 regardless — a wrong predecessor committed
with low confidence gets the same reward as a correct one. Step 2 makes the raw
confidence signals available so Phase E logic can scale or gate the bonus appropriately.

---

## Step 1 (investigation) — sub-region call sites

Before implementing anything, inspect the sub-region `advanceTemporalContext` call sites
in `regionanalyzer.cpp`. CC's Step 1 report identified them at approximately L574, L683,
L767, L770, L870 (may have shifted slightly after Step 1 commits).

For **each** sub-region `advanceTemporalContext` call site, show:
1. The line number
2. Whether a `PostScoringGateContext gateCtx` (or equivalent) is in scope at that point
3. Whether `applyHarmonicFunction` was called through `analyzeChord` at that sub-region
   site with a gateCtx pointer (i.e., `analyzeChord(..., &gateCtx)` vs `analyzeChord(..., nullptr)`)

Also confirm one thing about the main call site at L473: do `applyIter8691Pedal` and
`applyPostScoringGates` (L458–459) take `gateCtx` by value, const-ref, or non-const
ref/pointer? Confirm that `gateCtx.rawCandidates` is NOT modified by those two calls
before `advanceTemporalContext` runs at L473.

Report the sub-region findings before writing any code.

---

## Step 2 — New fields in `ChordTemporalContext` (chordanalyzer.h)

Add four fields to `ChordTemporalContext` after the existing fields. These hold
winner-confidence data from the immediately preceding region:

```cpp
// Step 2 redesign: predecessor confidence channel — forwarded to HarmonicFunctionContext
// All values are pre-gate (from applyHarmonicFunction competition pipeline output).

/// Score of the preceding region's committed winner (post-competition-pipeline).
/// 0.0 if not available (piece start, sub-region without gateCtx).
double previousWinnerScore { 0.0 };

/// Score gap between winner and runner-up in the winning bass group.
/// -1.0 if only one candidate existed (no runner-up).
double previousWinnerMargin { -1.0 };

/// pcWeight of the preceding region's committed winner's root pitch class.
/// 0.0 means the root was entirely absent from the sounded tones.
double previousWinnerRootPcWeight { 0.0 };

/// Distinct pitch-class count in the preceding region.
/// 0 if not available.
int previousDistinctPcs { 0 };
```

---

## Step 3 — New fields in `HarmonicFunctionContext` (harmonicfunctionlayer.h)

Add the same four fields to `HarmonicFunctionContext` after the Step 1 fields, with
identical defaults and the same "no scoring logic yet" comment:

```cpp
// Step 2 redesign: predecessor confidence channel — no scoring logic yet
double previousWinnerScore        { 0.0 };
double previousWinnerMargin       { -1.0 };
double previousWinnerRootPcWeight { 0.0 };
int    previousDistinctPcs        { 0 };
```

---

## Step 4 — Populate the fields at the main call site (regionanalyzer.cpp)

At the main `advanceTemporalContext` call (L473, or current line after Step 1 shifts),
add the following **immediately after** the existing call and the `nextRootPc`/`nextBassPc`
reset lines:

```cpp
// Step 2 redesign: populate predecessor confidence fields
{
    const int winRoot = chosenResult.identity.rootPc;
    temporalCtx.previousWinnerRootPcWeight = (winRoot >= 0)
        ? gateCtx.pcWeight[static_cast<size_t>(winRoot)] : 0.0;
    temporalCtx.previousDistinctPcs = gateCtx.distinctPcs;
    temporalCtx.previousWinnerScore = gateCtx.rawCandidates.empty()
        ? 0.0 : gateCtx.rawCandidates[0].score;
    temporalCtx.previousWinnerMargin = (gateCtx.rawCandidates.size() >= 2)
        ? gateCtx.rawCandidates[0].score - gateCtx.rawCandidates[1].score
        : -1.0;
}
```

Note: `rawCandidates` here is the pre-gate competition pipeline output from
`applyHarmonicFunction`. If a post-scoring gate changed the winner, `rawCandidates[0]`
may not match `chosenResult`. This is acceptable for infrastructure — the values are
advisory confidence signals for future Phase E logic, not truth-committed identities.

---

## Step 5 — Sub-region call sites

Based on your investigation in Step 1, handle the sub-region `advanceTemporalContext`
call sites:

- **If a sub-region site has a `gateCtx` in scope** (from an `analyzeChord(..., &gateCtx)`
  call immediately preceding it): add the same four-line block from Step 4.

- **If a sub-region site does NOT have a `gateCtx` in scope**: leave the four new
  `ChordTemporalContext` fields at their struct defaults (0.0 / 0.0 / 0.0 / 0). Do
  not add a block. Add a comment: `// Step 2: no gateCtx at this sub-region site — predecessor confidence fields left at defaults`.

Do not add a gateCtx parameter to sub-region analyzeChord calls just to enable this.
The cost isn't worth it for infrastructure fields that aren't yet used in scoring.

---

## Step 6 — Wire into HarmonicFunctionContext (chordanalyzer.cpp)

In the `fnCtx` construction block, add four lines after the Step 1 lines:

```cpp
// Step 2 redesign: predecessor confidence channel
fnCtx.previousWinnerScore        = context ? context->previousWinnerScore        : 0.0;
fnCtx.previousWinnerMargin       = context ? context->previousWinnerMargin       : -1.0;
fnCtx.previousWinnerRootPcWeight = context ? context->previousWinnerRootPcWeight : 0.0;
fnCtx.previousDistinctPcs        = context ? context->previousDistinctPcs        : 0;
```

---

## Step 7 — No changes to `harmonicfunctionlayer.cpp`

Do NOT add any code in `harmonicfunctionlayer.cpp` that reads or uses the new fields.
They must be wired through and available, but no scoring logic consumes them yet.

---

## Step 8 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/step2_comp.txt 2>&1; echo "exit:$?"
head -30 /tmp/step2_comp.txt
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/step2_nota.txt 2>&1; echo "exit:$?"
head -30 /tmp/step2_nota.txt
```

Read `src/composing/tests/chord_mismatch_report.txt`. Confirm:
- 407/407 composing, 52/52 notation, 11/11 pipeline snapshots, 0 goldens changed
- Baroque BIR=true=25, BIR=false=16; Jazz BIR=true=36, BIR=false=10

If any snapshot golden drifts, stop and report before doing anything else.

---

## Step 9 — Report, then commit

Report:
1. Sub-region investigation findings (which sites have gateCtx, which don't)
2. Confirmation that rawCandidates is not modified by post-scoring gate calls
3. Final new struct fields (ChordTemporalContext + HarmonicFunctionContext)
4. The population block added at the main call site
5. How each sub-region site was handled
6. Test results — confirm byte-identical

If byte-identical is confirmed, commit with:
```
git commit -m "refactor: Step 2 redesign — predecessor confidence channel (no scoring change)"
```
Update STATUS.md and commit separately:
```
git commit -m "docs: STATUS.md — record Step 2 redesign HEAD (predecessor confidence channel)"
```

Do not push.
