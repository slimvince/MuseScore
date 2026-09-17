# CC Instruction — E2b Review and Decision

**Read first:** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only),
`C:\s\MS\build_and_test.md`, `C:\s\MS\cc_instruction_e2b.md` (the original
E2b specification).

**Current HEAD:** `80a7adf32e` (E2a). Working tree is **dirty** — a Cowork
session made partial changes that may not be correct and did not build or test.

**Your job:** Review every change, decide whether to revert-and-redo or
fix-in-place, execute that decision, then do a comprehensive code review of
the final result. Do not code anything until the review section is complete.

---

## Part 1 — Establish what changed

```bash
cd /sessions/eloquent-confident-einstein/mnt/MS && git diff HEAD; echo "exit:$?"
```

Read the full diff. Identify every file that was modified and every line that
was added or changed.

Also check for any untracked files:
```bash
cd /sessions/eloquent-confident-einstein/mnt/MS && git status; echo "exit:$?"
```

---

## Part 2 — Assess each changed file

For each file in the diff, answer:

### 2a. `src/composing/analysis/function/harmonicfunctionlayer.h`

```bash
cat -n /sessions/eloquent-confident-einstein/mnt/MS/src/composing/analysis/function/harmonicfunctionlayer.h; echo "exit:$?"
```

Check:
- Is `#include <vector>` present and correctly placed?
- Are the `ScoringCell` and `ScoringSnapshot` struct definitions present?
- Are all fields from the spec in `cc_instruction_e2b.md` Part B present with
  correct names and types?
- Does the file end with `} // namespace mu::composing::function`?
- Is there anything truncated, duplicated, or malformed?

### 2b. `src/composing/analysis/chord/chordanalyzer.h`

```bash
grep -n "ScoringSnapshot\|captureScoringSnapshot\|namespace mu::composing" \
  /sessions/eloquent-confident-einstein/mnt/MS/src/composing/analysis/chord/chordanalyzer.h; echo "exit:$?"
```

Check:
- Is there a forward declaration for `ScoringSnapshot`? What form does it take
  (full `namespace { struct X; }` block, or a single line)?
- Is `captureScoringSnapshot` present in `ChordAnalyzerPreferences`?
- Is the field type `function::ScoringSnapshot*` and default `{ nullptr }`?
- Is `#include <vector>` or any new include needed in this file (given it only
  holds a pointer to an incomplete type)?

### 2c. `src/composing/analysis/chord/chordanalyzer.cpp`

Read the three blocks added by D1, D2, D3:

**D3 — capacity reservation:**
```bash
grep -n "captureScoringSnapshot\|E2b\|nCells" \
  /sessions/eloquent-confident-einstein/mnt/MS/src/composing/analysis/chord/chordanalyzer.cpp | head -30; echo "exit:$?"
```

Find the D3 block and check:
- Is it placed after `bassCandidates` is fully constructed?
- Is `bassCandidates.size()` used (not a hardcoded value)?
- Are both vectors cleared AND reserved?
- Is the cast to `int` safe (no narrowing issues)?

**D1 — cell capture in the joint-scoring loop:**

Read the full inner loop where push_backs happen:
```bash
sed -n '2360,2430p' /sessions/eloquent-confident-einstein/mnt/MS/src/composing/analysis/chord/chordanalyzer.cpp; echo "exit:$?"
```

Check every field assignment in the `if (prefs.captureScoringSnapshot)` block:
- `cell.bassPc` — does it use the correct variable (the bass PC for index `bi`)?
- `cell.rootPc` — does it use the inner loop variable?
- `cell.tiePriority` — does it use the template index? Is the cast from `size_t`
  to `int` explicit?
- `cell.quality` — does it come from `tpl.quality` (or the equivalent template
  reference)? NOT from a `RawCandidate`.
- `cell.basisIndep` — does it use `basisIndepMatrix[rootPc][tplIdx]` (or
  equivalent)? This must be the full matrix value INCLUDING any
  `rootContinuityBonus` contribution — it must NOT be de-inflated here.
- `cell.basisDep` — does it use the local `basisDep` variable (bass-dependent
  delta, NOT the final accumulated score)?
- `cell.complexityFactor` — from the matrix, NOT computed inline.
- `cell.augFactor` — from the matrix, NOT computed inline.
- `cell.wCompleteBonus` — the return value of `wCompleteBonus(...)` for this
  cell. Is it captured in a local before being added to `scoreNoWDim`, so the
  same value is used in both the score and the cell? Or is it recomputed (wrong)?
- `cell.wSeqBonus` — same question: captured in a local, or recomputed?
- `cell.appliedBassBonus` — the bass-root bonus component (used for threshold
  de-inflation). Does it match the variable name used in the surrounding code?
- For `cellsWithoutWDim`: is `wDimDelta` explicitly set to `0.0`?
- For `cellsWithWDim`: is `wDimDelta` set to the actual wDim lambda return value?
- Is the block placed BEFORE the push_backs into `perBassWithout`/`perBassWith`,
  so all local variables are still in scope?

**D2 — final-state capture:**

```bash
sed -n '2460,2510p' /sessions/eloquent-confident-einstein/mnt/MS/src/composing/analysis/chord/chordanalyzer.cpp; echo "exit:$?"
```

Check:
- Is the block placed AFTER `winnerIdx`, `acceptPostBonus`, and `rawCandidates`
  are all finalised?
- `chosenBassPc` — does it guard against empty `bassCandidates`?
- `winnerBassPcWith` — which index does it use (`winnerIdxWith` or `winnerIdx`)?
  It must use the with-wDim-specific winner index, not the post-guard `winnerIdx`.
- `winnerBassPcWithout` — same, must use the without-wDim-specific winner index.
- `distinctPcs` — is `distinctPcs` in scope at this point?
- `acceptedWithWDim` — set to `acceptPostBonus`?

---

## Part 3 — Attempt a build

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

Read the build log to check for errors:
```bash
ls -t /tmp/*.txt /tmp/*.log 2>/dev/null | head -5; echo "exit:$?"
```

(Build output location may vary — check `build_and_test.md` for the log path.)

If it fails to compile, note every error. Do NOT attempt to fix yet.

---

## Part 4 — Decision

Based on Parts 1–3, make one of the following decisions:

**Decision A — Fix in place.** The changes are structurally correct; only the
incomplete `harmonicfunctionlayer.h` needs completing. The variable names,
field assignments, and placement are all right.

**Decision B — Revert and redo.** The changes have substantive errors (wrong
variable names, incorrect field assignments, wrong placement, or structural
issues) that make a clean redo preferable to patching.

State which decision and why. Then execute it.

For Decision A: complete only what is missing. Do not re-touch anything already
correct.

For Decision B:
```bash
cd /sessions/eloquent-confident-einstein/mnt/MS && git checkout -- .; echo "exit:$?"
git status; echo "exit:$?"
```
Then implement E2b from scratch per `cc_instruction_e2b.md`.

---

## Part 5 — Build and test (after fix or redo)

```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/comp_e2b.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED|\[  FAILED  \]" /tmp/comp_e2b.txt | tail -10; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/note_e2b.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/note_e2b.txt | tail -5; echo "exit:$?"
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/snap_e2b.txt 2>&1; echo "exit:$?"
grep -E "PASSED|FAILED" /tmp/snap_e2b.txt | tail -5; echo "exit:$?"
```

**Expected: 407/407, 52/52, 11/11. If anything changes, revert and report.**

---

## Part 6 — Comprehensive code review

Only proceed here after Part 5 passes. Review the final committed (or
to-be-committed) state of all three files against the spec in
`cc_instruction_e2b.md`. For each item below, state Pass / Fail / Note.

### harmonicfunctionlayer.h

- [ ] `#include <vector>` present and not duplicated
- [ ] `ScoringCell` defined inside `namespace mu::composing::function`
- [ ] All 12 fields present: `bassPc`, `rootPc`, `tiePriority`, `quality`,
      `basisIndep`, `basisDep`, `complexityFactor`, `augFactor`,
      `wCompleteBonus`, `wSeqBonus`, `wDimDelta`, `appliedBassBonus`
- [ ] Field types match spec exactly (int, ChordQuality, double)
- [ ] `ScoringSnapshot` defined in same namespace
- [ ] `cellsWithWDim` and `cellsWithoutWDim` are `std::vector<ScoringCell>`
- [ ] All 5 scalar fields present with correct defaults:
      `chosenBassPc {-1}`, `acceptedWithWDim {false}`,
      `winnerBassPcWith {-1}`, `winnerBassPcWithout {-1}`, `distinctPcs {0}`
- [ ] No extra fields beyond spec
- [ ] Comments accurately describe each field's purpose for E2c
- [ ] File compiles cleanly as a standalone header (no missing includes)
- [ ] Namespace closed correctly

### chordanalyzer.h

- [ ] Forward declaration is minimal (pointer-only use; full include not needed)
- [ ] No circular include introduced
- [ ] `captureScoringSnapshot` field placed at end of `ChordAnalyzerPreferences`
- [ ] Type is `function::ScoringSnapshot*`, default is `{ nullptr }`
- [ ] Comment matches spec

### chordanalyzer.cpp — D3 (capacity reservation)

- [ ] Placed after `bassCandidates` is fully populated
- [ ] Both vectors cleared before reserve (handles re-use of the same snapshot)
- [ ] Reserve size = `bassCandidates.size() * 12 * templates.size()`
- [ ] No reallocation risk during the loop

### chordanalyzer.cpp — D1 (cell capture)

- [ ] Block is inside the bass × root × template triple loop
- [ ] Placed BEFORE `push_back` into `perBassWithout`/`perBassWith`
- [ ] `basisIndep` uses the matrix value (full, including rootContinuityBonus)
- [ ] `basisDep` is the pre-multiplication bass-dependent delta
- [ ] `wCompleteBonus` and `wSeqBonus` use locals extracted BEFORE being added
      to `scoreNoWDim` — NOT recomputed after the fact
- [ ] `cellsWithoutWDim` cell has `wDimDelta = 0.0`
- [ ] `cellsWithWDim` cell has `wDimDelta` = the wDim lambda return value
- [ ] Both `push_back` calls use the same `cell` struct (only `wDimDelta` differs)
- [ ] Cell order matches spec: bass outer, rootPc middle, tplIdx inner

### chordanalyzer.cpp — D2 (final-state capture)

- [ ] Placed after the variant-choice block (after `winnerIdx`, `acceptPostBonus`,
      `rawCandidates` are all set)
- [ ] `distinctPcs` is in scope
- [ ] `chosenBassPc` guards against empty `bassCandidates`
- [ ] `winnerBassPcWith` uses the with-wDim-specific index (not post-guard `winnerIdx`)
- [ ] `winnerBassPcWithout` uses the without-wDim-specific index
- [ ] Both winner-bass fields guard against empty `bassCandidates`

### Zero-behavioral-change verification

- [ ] All existing call sites pass `ChordAnalyzerPrefs` without setting
      `captureScoringSnapshot` — confirm with grep
- [ ] Hot path (null pointer check) adds at most one branch per loop iteration
- [ ] No `RawCandidate` field changed
- [ ] No scoring logic changed
- [ ] Test counts byte-identical to HEAD 80a7adf32e

---

## Part 7 — Commit (only after Part 6 complete and all items pass)

```
cd C:\s\MS && git add \
  src/composing/analysis/function/harmonicfunctionlayer.h \
  src/composing/analysis/chord/chordanalyzer.h \
  src/composing/analysis/chord/chordanalyzer.cpp; echo "exit:$?"

cd C:\s\MS && git commit -m "E2b: expose scoring snapshot in analyzeChord() (opt-in)

Add ScoringCell / ScoringSnapshot structs to harmonicfunctionlayer.h.
Add prefs.captureScoringSnapshot pointer to ChordAnalyzerPreferences.

When non-null, analyzeChord() populates a pre-step-bonus scoring cube for
both the with-wDim and without-wDim variants (ScoringSnapshot::cellsWithWDim
and cellsWithoutWDim), covering all bassCandidates x 12 rootPcs x N templates.
Also records: distinctPcs, acceptedWithWDim, chosenBassPc, winnerBassPcWith/
Without.

All existing callers pass prefs without the new field (defaults to nullptr),
so the hot path is completely unchanged.

E2c will set prefs.captureScoringSnapshot and use it to redo joint scoring
with {rootContinuityBonus, w_seq, w_dim} suppressed in the scorer and applied
in applyHarmonicFunction() instead.

Zero behavioral change. All tests identical to HEAD 80a7adf32e."; echo "exit:$?"
```

---

## Report back

1. Decision (A or B) and reasoning
2. Exact list of what was wrong / incomplete in the Cowork changes
3. Code review results — every checklist item, Pass/Fail/Note
4. Test results
5. Commit hash
