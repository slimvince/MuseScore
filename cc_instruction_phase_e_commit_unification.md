# CC Instruction: Phase E — Unify the commit path in regionanalyzer.cpp

## Context

This is Phase E Step 5 architectural work. See `docs/redesign_plan.md` Step 5 and
`COWORK_HANDOFF.md` "Architecture direction" section (near the top).

**Goal:** Every chord commitment in `regionanalyzer.cpp` — main Pass 1 loop, Pass 2
sub-regions, Pass 2b sub-regions — must flow through the same helper. No manual
inline field assignments.

**Constraint:** This is pure structural refactoring. No new scoring logic, no threshold
changes, no behaviour changes. Output should be **byte-identical** on all test suites.
If it is not byte-identical, stop and report why before proceeding.

---

## What you are fixing

There are currently three commit sites in `regionanalyzer.cpp`, all doing the same
work with different code:

### Site 1 — Main Pass 1 loop (~line 473)
```cpp
advanceTemporalContext(temporalCtx, runningStepwiseCount, recentRootsBuf,
                       chosenResult.identity);
temporalCtx.nextRootPc = -1;
temporalCtx.nextBassPc = -1;

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
This site calls `advanceTemporalContext` correctly, then does the confidence block
separately. The two pieces belong together.

### Site 2 — Pass 2 sub-region loop (~line 695)
```cpp
subCtx.previousRootPc  = chosenSub.identity.rootPc;
subCtx.previousQuality = chosenSub.identity.quality;
subCtx.previousBassPc  = chosenSub.identity.bassPc;

// Step 2 redesign: populate predecessor confidence fields (subGateCtx in scope)
{ ... identical confidence block using subGateCtx ... }
```
This site BYPASSES `advanceTemporalContext` with a 3-line manual assignment.
Consequence: `consecutiveBassStepwiseCount` and `recentRootPcs` are never updated
for sub-region sequences — a silent inconsistency.

### Site 3 — Pass 2b sub-region loop (~line 895)
Identical to Site 2 — same bypass, same omission.

---

## Task 1 — Read the current code

Before touching anything, read these sections precisely:

```
sed -n '460,500p' C:/s/MS/src/composing/analysis/region/regionanalyzer.cpp
sed -n '680,720p' C:/s/MS/src/composing/analysis/region/regionanalyzer.cpp
sed -n '880,920p' C:/s/MS/src/composing/analysis/region/regionanalyzer.cpp
```

Also read `advanceTemporalContext` in full:
```
sed -n '700,755p' C:/s/MS/src/composing/analysis/chord/chordanalyzer.h
```

And read `PostScoringGateContext` to understand the fields used in the confidence block:
```
sed -n '751,820p' C:/s/MS/src/composing/analysis/chord/chordanalyzer.h
```

Confirm the three sites match the description above. Note the exact line numbers in
the current file (they may have shifted slightly).

---

## Task 2 — Design decision: sub-region rolling state

The two sub-region loops iterate over sub-slices within a parent region, each with
their own `subCtx`. Because they bypass `advanceTemporalContext`, sub-regions currently
never update `consecutiveBassStepwiseCount` or `recentRootPcs`.

For the unification to call `advanceTemporalContext` at Sites 2 and 3, the call needs
`runningStepwiseCount` and `recentRootsBuf` variables. There are two options:

**Option A — per-pass rolling state.** Declare `int subRunningStepwiseCount = 0` and
`std::array<int, 3> subRecentRootsBuf = {-1,-1,-1}` at the start of each sub-region
loop. Pass these to `advanceTemporalContext`. Sub-regions now maintain rolling state
within their own sequence. This is architecturally correct but may produce non-byte-
identical output if `consecutiveBassStepwiseCount` or `recentRootPcs` affect scoring
for any sub-region.

**Option B — silent no-ops for rolling state.** Declare the same local variables but
do not initialise them from any parent state, so they start fresh per-parent and only
accumulate within that parent's sub-region sequence. Functionally equivalent to Option A
for a single-parent sub-region run, but explicitly scoped.

**Decision:** Use **Option A**. It is architecturally correct. If the output is not
byte-identical, report which sub-region score changed and why — do not silently adjust
the state initialisation to force byte-identity.

---

## Task 3 — Extend advanceTemporalContext

Add a new overload (or extend the existing ones) in `chordanalyzer.h` that also accepts
a `const PostScoringGateContext&` parameter and performs the confidence-field update
internally:

```cpp
inline void advanceTemporalContext(
    ChordTemporalContext&             ctx,
    int&                              runningStepwiseCount,
    std::array<int, 3>&               recentRootsBuf,
    const ChordIdentity&              chosen,
    const PostScoringGateContext&     gateCtx) noexcept
{
    // Delegate to the existing overload for rolling state + identity fields.
    advanceTemporalContext(ctx, runningStepwiseCount, recentRootsBuf, chosen);

    // Predecessor confidence fields (Step 2 redesign).
    const int winRoot = chosen.rootPc;
    ctx.previousWinnerRootPcWeight = (winRoot >= 0)
        ? gateCtx.pcWeight[static_cast<size_t>(winRoot)] : 0.0;
    ctx.previousDistinctPcs  = gateCtx.distinctPcs;
    ctx.previousWinnerScore  = gateCtx.rawCandidates.empty()
        ? 0.0 : gateCtx.rawCandidates[0].score;
    ctx.previousWinnerMargin = (gateCtx.rawCandidates.size() >= 2)
        ? gateCtx.rawCandidates[0].score - gateCtx.rawCandidates[1].score
        : -1.0;
}
```

Place this overload immediately after the existing `ChordIdentity` overload (~line 741).

Update the doc-comment on the overload group to reflect that the new overload also
updates predecessor confidence fields.

---

## Task 4 — Replace all three commit sites in regionanalyzer.cpp

### Site 1 (main loop)
Replace:
```cpp
advanceTemporalContext(temporalCtx, runningStepwiseCount, recentRootsBuf,
                       chosenResult.identity);
temporalCtx.nextRootPc = -1;
temporalCtx.nextBassPc = -1;

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
With:
```cpp
advanceTemporalContext(temporalCtx, runningStepwiseCount, recentRootsBuf,
                       chosenResult.identity, gateCtx);
temporalCtx.nextRootPc = -1;
temporalCtx.nextBassPc = -1;
```

### Site 2 (Pass 2 sub-region loop)
At the start of the outer loop that iterates parent regions in Pass 2, declare:
```cpp
int subRunningStepwiseCount = 0;
std::array<int, 3> subRecentRootsBuf = {-1, -1, -1};
```
These reset for each parent region (declare inside the per-parent loop, before the
sub-region loop begins).

Replace:
```cpp
subCtx.previousRootPc  = chosenSub.identity.rootPc;
subCtx.previousQuality = chosenSub.identity.quality;
subCtx.previousBassPc  = chosenSub.identity.bassPc;

// Step 2 redesign: populate predecessor confidence fields (subGateCtx in scope)
{
    const int winRoot = chosenSub.identity.rootPc;
    subCtx.previousWinnerRootPcWeight = (winRoot >= 0)
        ? subGateCtx.pcWeight[static_cast<size_t>(winRoot)] : 0.0;
    subCtx.previousDistinctPcs = subGateCtx.distinctPcs;
    subCtx.previousWinnerScore = subGateCtx.rawCandidates.empty()
        ? 0.0 : subGateCtx.rawCandidates[0].score;
    subCtx.previousWinnerMargin = (subGateCtx.rawCandidates.size() >= 2)
        ? subGateCtx.rawCandidates[0].score - subGateCtx.rawCandidates[1].score
        : -1.0;
}
```
With:
```cpp
advanceTemporalContext(subCtx, subRunningStepwiseCount, subRecentRootsBuf,
                       chosenSub.identity, subGateCtx);
```

### Site 3 (Pass 2b sub-region loop)
Same pattern as Site 2 — same replacement, same per-parent-loop rolling state
declaration.

---

## Task 5 — Build and test

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/compose_out.txt 2>&1; echo "exit:$?"
head -20 /tmp/compose_out.txt
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/notation_out.txt 2>&1; echo "exit:$?"
head -20 /tmp/notation_out.txt
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_out.txt 2>&1; echo "exit:$?"
tail -20 /tmp/snap_out.txt
```

Expected: **416/416 · 52/52 · 11/11, zero snapshot diffs** (byte-identical).

If any snapshot diffs appear, run `--update-goldens` only AFTER confirming the diff
is architecturally expected from the sub-region rolling state change (Option A). Do
NOT update goldens silently — report the diff content first.

If there are failures in composing or notation tests (not snapshot), stop and report
the failure message before proceeding.

---

## Task 6 — Corpus spot-check

Run the corpus quality check to confirm BIR numbers are unchanged:

```
cd C:\s\MS && python tools/analyze_inversion_errors.py > /tmp/bir_check.txt 2>&1; echo "exit:$?"
cat /tmp/bir_check.txt
```

BIR baselines: Baroque BIR=false = 13, Jazz BIR=false = 7. Neither must increase.

---

## Report format

Write findings to `C:\s\MS\cc_phase_e_commit_unification_report.md`:

**Section 1 — Site survey**: Confirm the three commit sites match the description
above. Note exact line numbers as found.

**Section 2 — Implementation**: What was changed in `chordanalyzer.h` (new overload)
and `regionanalyzer.cpp` (three sites). Show the before/after diff for each site (10
lines context).

**Section 3 — Rolling state**: Where were `subRunningStepwiseCount` /
`subRecentRootsBuf` declared? Did any sub-region's `consecutiveBassStepwiseCount` or
`recentRootPcs` change value as a result?

**Section 4 — Test results**: composing / notation / snapshot counts and any diffs.
If snapshots drifted, show the full diff content.

**Section 5 — BIR check**: Baroque and Jazz BIR=false numbers after the change.

**Section 6 — Commit recommendation**: If all tests pass and BIR is unchanged,
propose a commit message. Do not commit until Cowork confirms.
