# Iteration 9A: Extract `isDiatonicStep()` to composing module (§2.10)

## ⚠ Critical behaviour rules

- **Read first, report, then implement.**
- Pure refactoring — zero behaviour change. Tests must pass identically to post-Iteration-8 baselines.
- Do not commit until all tests and corpus numbers match exactly.
- If anything deviates, STOP and report verbatim.

---

## Background

`isDiatonicStep()` — an inline function that tests whether two pitch classes are a
diatonic step apart (interval of 1 or 2 semitones) — is currently defined identically
in two places:

1. `src/notation/internal/notationcomposingbridgehelpers.h` (bridge path)
2. `tools/batch_analyze.cpp` (batch path)

Per ARCHITECTURE.md §2.10, shared logic belongs in `src/composing/`, not in consumers.
This iteration moves the single canonical definition to `src/composing/analysis/chord/chordanalyzer.h`
and removes the duplicate from each consumer.

Both consumers already include `chordanalyzer.h` (they use `ChordTemporalContext`,
`ChordAnalyzerPreferences`, `ChordAnalyzerFactory`, etc.), so no new includes are
required — adding the function to `chordanalyzer.h` makes it automatically available
in both files.

---

## Step 1 — Context loading

1. `CLAUDE.md` — standing instructions
2. `build_and_test.md` — baselines: BIR=true=109, BIR=false=788

---

## Step 2 — Read and confirm current state

Read:
- `src/notation/internal/notationcomposingbridgehelpers.h` — find the `isDiatonicStep` definition; record exact lines and body
- `tools/batch_analyze.cpp` — find the `isDiatonicStep` definition; record exact lines and body
- `src/composing/analysis/chord/chordanalyzer.h` — identify the namespace used, any existing free utility functions, and the best insertion point (a logical grouping near pitch-class utilities or immediately before `ChordTemporalContext`)

Also confirm:
A. The two definitions are byte-for-byte identical (expected: yes)
B. `notationcomposingbridgehelpers.h` already includes `chordanalyzer.h` (directly or transitively — check existing includes)
C. `tools/batch_analyze.cpp` already includes `chordanalyzer.h` (check existing includes)
D. `isDiatonicStep` does not already exist anywhere in `src/composing/`

Report A–D and the exact line numbers before proceeding.

---

## Step 3 — Add canonical definition to chordanalyzer.h

In `src/composing/analysis/chord/chordanalyzer.h`, in the same namespace as the
surrounding code, add the canonical definition at a logical location (near
pitch-class utilities or immediately before `ChordTemporalContext`):

```cpp
/// Returns true if two pitch classes are a diatonic step apart
/// (chromatic interval of 1 or 2 semitones, shortest path).
inline bool isDiatonicStep(int pc1, int pc2) noexcept
{
    int interval = std::abs(pc1 - pc2);
    interval = std::min(interval, 12 - interval);
    return interval == 1 || interval == 2;
}
```

If `chordanalyzer.h` already has a dedicated utility section or companion utility
header that is already included by both consumers, place it there instead — use
judgment based on what you read.

Report the exact line of insertion.

---

## Step 4 — Remove duplicates from consumers

### Consumer 1: `src/notation/internal/notationcomposingbridgehelpers.h`
Remove the `isDiatonicStep` definition entirely (the lines identified in Step 2).
If the file already includes `chordanalyzer.h` (confirmed in Step 2B), no new
include is needed — the function is now available through the existing include.
If it does NOT include `chordanalyzer.h` directly, add the appropriate include.

### Consumer 2: `tools/batch_analyze.cpp`
Remove the `isDiatonicStep` definition entirely (the lines identified in Step 2).
Same include logic: if `chordanalyzer.h` is already included (confirmed in Step 2C),
no new include is needed. If not, add one.

Report the exact lines removed from each file.

---

## Step 5 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe
cd C:\s\MS && python tools/analyze_inversion_errors.py
```

Expected (must match exactly — this is pure refactoring):
- Composing tests: 407/407, RealDiff ≤ 4
- Notation tests: 53/53
- Pipeline snapshot tests: 11/11
- BIR=true: 109
- BIR=false: 788

Any deviation = STOP and report verbatim before touching anything else.

---

## Step 6 — Push

```
cd C:\s\MS && git add -A && git commit -m "Iter 9A: extract isDiatonicStep to composing module (§2.10)" && git push
```

---

## Step 7 — Report

```
State verification (A–D):
  Definitions identical:                    yes / no
  bridgehelpers.h already includes chord.h: yes / no (path: <include line>)
  batch_analyze.cpp already includes chord.h: yes / no (path: <include line>)
  isDiatonicStep absent from src/composing: yes / no

Changes:
  Canonical definition added to: <file>:<line>
  Removed from bridgehelpers.h:  lines N–N
  New include in bridgehelpers.h: yes (line N) / not needed
  Removed from batch_analyze.cpp: lines N–N
  New include in batch_analyze.cpp: yes (line N) / not needed

Build:                    pass / fail
Composing tests:          407/407 pass, RealDiff=N
Notation tests:           53/53 pass
Pipeline snapshot tests:  11/11 pass
BIR=true:                 109
BIR=false:                788
GitHub push:              done / commit hash
Unexpected findings:      none / <describe>
```
