# CC Instruction — E2d-enable: Enable progression-signal suppression (Commit 2 retry)

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\docs\scoring_model.md` §4 and §10.

**Current HEAD:** `de418dea5f` (E2d-infra). Working tree must be clean.
Tests: 407/407 composing, 52/52 notation, 11/11 snapshot (1 skipped).

**One commit.**

---

## Context — why the previous attempt was reverted

The original E2d.md Commit 2 required byte-identical snapshot test output.
That requirement is wrong. The pipeline snapshot goldens were pinned against
the pre-E2c output, which included gate-pushed alternatives (Gates A/B/F/G
in `analyzeChord()`) built from signal-inclusive `rawCandidates`. Moving
signal computation to the function layer changes how alternatives are
selected — they become the function layer's top-2 by rescored signal-inclusive
score rather than gate-pushed entries. This is an intended consequence of
the migration, not a defect.

The correct acceptance criteria are:

1. **407/407 composing tests pass** — these test primary chord labels.
2. **52/52 notation tests pass** — these test the full pipeline.
3. **Pipeline snapshot tests: winner is verified correct for every case,
   then goldens are updated** to accept the function layer's output as the
   new baseline.

The winner was confirmed correct in all 11 snapshot test cases during the
previous attempt. This instruction completes the migration.

---

## Design decisions (unchanged from E2d.md)

All design decisions from `C:\s\MS\cc_instruction_e2d.md` §Design decisions
apply. In summary:

- Two-variant Pass B (`runPassB` applied separately to `scoreWith[]` and
  `scoreWithout[]`).
- `jointScoringEnabled` gates Pass B.
- `kWStepIn`, `kWStepOut`, `kStepBudget` constants from E2d-infra.
- `intervalCount` field on `ScoringCell` for the m7-family guard.
- `ctx.previousBassPc` / `ctx.nextBassPc` for step direction.
- Cross-bass promotion via `(tiePriority, rootPc)` match + bassPc/bassTpc patch.

---

## Implementation

### Step 1 — Implement `applyHarmonicFunction()` (same as E2d.md Part G)

Read `C:\s\MS\cc_instruction_e2d.md` Part G for the full replacement body.
Implement it exactly as specified there.

**One addition not in Part G — sort alternatives by rescored score.**

After the winner is rotated to `candidates[0]`, the remaining entries are
still in suppressed-signal order. Replace the bare `candidates.resize(3)`
trim with a sort of the tail so that `candidates[1]` and `candidates[2]`
are the highest-scoring non-winner cells by the function layer's rescored
score.

To do this, before trimming, build a score map from `(tiePriority, rootPc)`
to rescored score (using the same `winScores[]` array used to find the
winner). Then sort `candidates[1..]` descending by that score, then trim:

```cpp
// Build a lookup: (tiePriority, rootPc) → rescored score.
// winScores[] is the already-computed per-cell score array (scoreWith or
// scoreWithout depending on acceptWithWDim).
std::unordered_map<int, double> scoreMap;  // key: tiePriority * 12 + rootPc
for (std::size_t i = 0; i < N; ++i) {
    const ScoringCell& sc = snapshot->cellsWithWDim[i];
    const int key = sc.tiePriority * 12 + sc.rootPc;
    scoreMap[key] = winScores[i];
}

auto rescoredScore = [&](const analysis::ChordAnalysisResult& r) -> double {
    const int key = r.identity.tiePriority * 12 + r.identity.rootPc;
    const auto it = scoreMap.find(key);
    return (it != scoreMap.end()) ? it->second
                                  : -std::numeric_limits<double>::infinity();
};

// Sort tail (candidates[1..]) by descending rescored score.
if (candidates.size() > 1) {
    std::sort(candidates.begin() + 1, candidates.end(),
              [&](const auto& a, const auto& b) {
                  return rescoredScore(a) > rescoredScore(b);
              });
}

// Trim to top-3.
if (candidates.size() > 3) candidates.resize(3);
```

### Step 2 — Enable suppression at all three call sites (same as E2d.md Part H)

Read `C:\s\MS\cc_instruction_e2d.md` Part H for the exact lines to set at
each `regionanalyzer.cpp` call site:

```cpp
<prefs_copy>.suppressProgressionSignals = true;
<prefs_copy>.captureScoringSnapshot     = &<snap>;
```

---

## Verification — winner check before updating goldens

Build and run the full test suite:

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2de.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2de.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2de.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2de.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2de.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2de.txt | tail -5; echo "exit:$?"
```

**Expected after this step:**
- 407/407 composing ✓
- 52/52 notation ✓
- Pipeline snapshot: some or all of the 11 tests fail (alternatives differ)

**If composing or notation fail: revert everything and report. Do not proceed.**

**For each failing snapshot test**, read the diff output and confirm that
`candidates[0]` (the winner — rootPc, quality, inversion, bassPc) is
identical between expected and actual. Report any test where candidates[0]
differs — that would be a correctness failure requiring investigation before
proceeding.

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_detail.txt 2>&1; echo "exit:$?"
grep -A 30 "FAILED\|Mismatch\|Expected\|Actual" /tmp/snap_detail.txt | head -100; echo "exit:$?"
```

**Only proceed to goldens update if candidates[0] is correct in every
failing test.**

---

## Update goldens

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe --update-goldens > /tmp/snap_update.txt 2>&1; echo "exit:$?"
head -20 /tmp/snap_update.txt; echo "exit:$?"
```

Re-run to confirm all 11 pass on the new goldens:

```
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_final.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_final.txt | tail -5; echo "exit:$?"
```

**Expected: 11/11 (or 10/10 + 1 skipped) on the new goldens.**

---

## Commit

Find the golden files that were updated:

```
cd C:\s\MS && git diff --name-only; echo "exit:$?"
```

Commit all changed files (function layer code + regionanalyzer + goldens):

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.cpp \
  src/composing/analysis/region/regionanalyzer.cpp; echo "exit:$?"

cd C:\s\MS && git add $(git diff --name-only | grep -v "^src/composing/analysis"); echo "exit:$?"
```

(The second `git add` picks up the golden JSON files, which live outside
`src/composing/analysis/`. Adjust the path filter if needed to include only
the golden files and nothing else unintended.)

```
cd C:\s\MS && git commit -m "E2d-enable: progression-signal suppression with Pass B replication

applyHarmonicFunction() rescores all snapshot cells with signals
re-applied, runs two-variant Pass B (with-wDim / without-wDim), runs the
per-bass quality guard, and selects the global winner. Alternatives are
re-ranked by rescored signal-inclusive score.

suppressProgressionSignals=true enabled at all three regionanalyzer.cpp
call sites. The scorer runs without rootContinuityBonus, wSeqBonus, and
wDimBonus; the function layer re-applies all three plus the step bonus.

Cross-bass promotion: if the signal-inclusive winner is on a different bass
than the suppressed-signal scorer's winner, bassPc and bassTpc are patched
from the snapshot cell.

Pipeline snapshot goldens updated: winner (candidates[0]) is identical to
the pre-suppression baseline in all cases; alternatives now reflect the
function layer's rescored ranking rather than analyzeChord() gate-pushed
entries. This is the intended outcome of the signal migration.

docs/scoring_model.md §10 updated: E2c and E2d marked done."; echo "exit:$?"
```

---

## After this commit

Hand `C:\s\MS\cc_instruction_e2d_cleanup.md` to CC. That instruction
extracts `applyStepBonus` into a shared free function to eliminate the
Pass B code duplication between `chordanalyzer.cpp` and
`harmonicfunctionlayer.cpp`.

---

## Report back

1. Composing and notation test results
2. How many pipeline snapshot tests failed before --update-goldens
3. Confirm: was candidates[0] correct in every failing test?
4. Pipeline snapshot test results after --update-goldens (all 11 pass?)
5. List of golden files updated (from `git diff --name-only`)
6. Commit hash
7. Any deviation from the specified implementation
