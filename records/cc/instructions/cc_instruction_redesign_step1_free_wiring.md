# CC Instruction: Redesign Step 1 — Forward free ChordTemporalContext fields

## Pre-reading (mandatory)

Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header), `C:\s\MS\build_and_test.md`,
and `C:\s\MS\docs\redesign_plan.md` before starting.

This is **Step 1** of the redesign sequence described in `docs/redesign_plan.md`.

---

## What this task is — and is not

**Is:** Pure infrastructure wiring. Fields that already exist in `ChordTemporalContext`
and are already computed at the call site are forwarded into `HarmonicFunctionContext`
so that downstream code in `applyHarmonicFunction` can see them when Phase E logic is
added later.

**Is not:** A scoring change. No new logic in `harmonicfunctionlayer.cpp` should use
the new fields. The test suite outcome must be **byte-identical** — BIR numbers and
pipeline snapshot goldens must be unchanged.

**Expected result:** Both test suites pass. Mismatch report matches STATUS.md baselines
exactly. Zero snapshot goldens changed.

---

## Step 1 — Investigation (read before touching any file)

Read the following and report your findings before implementing:

**a)** `src/composing/analysis/chord/chordanalyzer.h` — the `ChordTemporalContext`
struct (around L570). List every field with its exact C++ type. Confirm the types of:
- `previousQuality`
- `recentRootPcs` (note: size of array and element type)
- `consecutiveBassStepwiseCount`
- `regionMetricWeight`

**b)** `src/composing/analysis/function/harmonicfunctionlayer.h` — the
`HarmonicFunctionContext` struct (around L59). List all existing fields.

**c)** `src/composing/analysis/chord/chordanalyzer.cpp` — the `fnCtx` construction
block (around L2931–2937). Show the exact current code so the new lines can follow the
same null-safety pattern.

**d)** Locate where `recentRootPcs`, `consecutiveBassStepwiseCount`, and
`regionMetricWeight` are written into `ChordTemporalContext`. (They may be set in
`regionanalyzer.cpp` or elsewhere — grep for the field names.) Confirm they have valid
values by the time `fnCtx` is constructed.

Do not change any file until you have reported these findings and confirmed the types
and write-locations.

---

## Step 2 — Implementation

### 2a — Add fields to `HarmonicFunctionContext` (`harmonicfunctionlayer.h`)

Add four new fields to the `HarmonicFunctionContext` struct, after the existing fields.
Match the types exactly from `ChordTemporalContext`. Use these defaults for the
null-context case:

| Field | Type (match ChordTemporalContext) | Null default |
|---|---|---|
| `previousQuality` | (from investigation) | `-1` or the enum's "unknown" value |
| `recentRootPcs[3]` | int array, size 3 | `{-1, -1, -1}` |
| `consecutiveBassStepwiseCount` | int | `0` |
| `regionMetricWeight` | double | `1.0` |

Add a comment above the block:
```cpp
// Step 1 redesign: free wiring — forwarded from ChordTemporalContext, no scoring logic yet
```

### 2b — Wire them in `chordanalyzer.cpp` (`fnCtx` construction)

In the `fnCtx` construction block (L2931–2937), add forwarding for the four new fields.
Follow the existing null-safety pattern exactly:

```cpp
fnCtx.previousQuality             = context ? context->previousQuality             : <null_default>;
fnCtx.consecutiveBassStepwiseCount = context ? context->consecutiveBassStepwiseCount : 0;
fnCtx.regionMetricWeight          = context ? context->regionMetricWeight          : 1.0;
```

For `recentRootPcs` (array), use a conditional copy:
```cpp
if (context) {
    std::copy(std::begin(context->recentRootPcs),
              std::end(context->recentRootPcs),
              std::begin(fnCtx.recentRootPcs));
} else {
    fnCtx.recentRootPcs.fill(-1);  // or std::fill / memset depending on type
}
```
Adjust `fill` vs `std::fill` vs `memset` to match the actual array type — check the
existing code style in the file.

### 2c — No changes to `harmonicfunctionlayer.cpp`

Do NOT add any code in `harmonicfunctionlayer.cpp` that reads or uses the new fields.
They must be wired through and available, but no scoring logic consumes them yet.

---

## Step 3 — Build

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

---

## Step 4 — Run both test suites

```
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/step1_comp.txt 2>&1; echo "exit:$?"
head -30 /tmp/step1_comp.txt

cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/step1_nota.txt 2>&1; echo "exit:$?"
head -30 /tmp/step1_nota.txt
```

Read `src/composing/tests/chord_mismatch_report.txt`. Confirm:
- Composing: 407/407
- Notation: 52/52
- Pipeline snapshots: 11/11 (0 goldens changed)
- Baroque BIR=true=25, BIR=false=16
- Jazz BIR=true=36, BIR=false=10

If any snapshot golden drifted, something in the wiring changed scoring. Stop and
report before doing anything else.

---

## Step 5 — Report

Report:
1. The four types you found in `ChordTemporalContext` (from Step 1)
2. Where `recentRootPcs`, `consecutiveBassStepwiseCount`, `regionMetricWeight` are set
3. The final added struct fields (show the new block in `HarmonicFunctionContext`)
4. The final fnCtx wiring lines
5. Test results — confirm byte-identical

Do NOT commit. Cowork will review the report and confirm before committing.
