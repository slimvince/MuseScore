# CC Instruction: Stage 1a — Pin the function layer (unit tests) + tie stability

## Context

Master plan: `docs/implementation_roadmap.md` — this implements Stage 1 items **1.2**
(function-layer bonus tests) and **1.7** (tie-stability test). Stage 1's purpose: **pin
current behavior** before anything is built on or replaced. These tests become the
differential-test harness for the Stage 3 decoder migration — each pinned behavior is a
proof obligation later.

Mandatory reads first: STATUS.md header, `docs/scoring_model.md` §4 (every bonus/gate term
+ the new FP tie policy section), `src/composing/tests/gater_tests.cpp` (the established
test pattern — follow it), `src/composing/analysis/function/harmonicfunctionlayer.h`
(actual signatures — design tests against what IS there, not what this instruction says).

**Hard constraints:**
- **Tests only. Zero production-code changes.** Allowed files: new/extended test files
  under `src/composing/tests/` + its `CMakeLists.txt`. Nothing else.
- **Pin CURRENT behavior, even where it looks questionable.** If a test reveals behavior
  that seems wrong: do NOT fix the production code. Pin it with a comment
  (`// pins current behavior — flagged in cc_stage1a_report.md §Findings`) and report it.
  If you find an outright crash/UB, stop and ask.
- Existing suites must stay green: 416 composing (plus your new ones) · 52 notation ·
  11 snapshots. No BIR run needed (production binary's analysis code is untouched) — state
  this in the report.

## Task 1 — Survey (report discrepancies before writing tests)

Read `harmonicfunctionlayer.{h,cpp}` and confirm the actual signatures and call-site
semantics of: `rootContinuityBonus`, `wSeqBonus`, `wDimBonus`, `wStepInBonus`,
`wStepOutBonus`, `applyStepBonusGuard`, the wDim post-bonus quality guard (the
with-wDim/without-wDim dual scoring fallback), and the Pass A/B/C structure of
`applyHarmonicFunction`. Note which are directly testable free functions vs. only
reachable through `applyHarmonicFunction`. If `applyStepBonusGuard` or the dual-scoring
guard are file-local (anonymous namespace), test them through `applyHarmonicFunction`
end-to-end — do NOT move or re-expose production symbols (that would be a production
change; if unavoidable, stop and ask).

## Task 2 — Bonus-function unit tests (roadmap 1.2)

Place in a new `src/composing/tests/functionlayer_tests.cpp` (or extend
`gater_tests.cpp` if the fixtures are shared — your call, document it). Cover, per
`scoring_model.md` §4 (each documented condition = at least one fire + one non-fire case):

1. **`rootContinuityBonus`**: fires iff `rootPc == previousRootPc` with the configured
   bonus; no fire when previousRootPc = -1 / differs.
2. **`wSeqBonus`** (kWSeq 0.20): fires on `(nextRootPc - candRootPc) mod 12 == 5`,
   `distinctPcs >= 4`, jointScoringEnabled; non-fire cases: each condition individually
   broken (interval ≠ 5, distinctPcs = 3, jointScoring = false, nextRootPc = -1).
   Also pin: inversion does NOT matter (no bass/root-position condition).
3. **`wDimBonus`** (kWDim 0.15): fires for Dim/HalfDim, root one semitone below
   nextRootPc, distinctPcs ≥ 4; non-fire: Major quality, distinctPcs = 3 (the
   quality-flip guard — pin it explicitly with a comment referencing §4).
4. **`wStepInBonus` / `wStepOutBonus`** (0.10 each): fire on semitone/whole-tone bass
   motion from previous / to next; non-fire on larger intervals and missing context.
5. **`applyStepBonusGuard` — all four load-bearing guards** (via `applyHarmonicFunction`
   if file-local), one test each:
   a. root-position-only: slash candidate (`bassPc ≠ rootPc`) gets no step bonus;
   b. m7-family surgical guard: competitor of quality {HalfDim, Dim, Min7-shaped} at
      `(candBassPc-3) mod 12` within kStepBudget blocks the bonus; just OUTSIDE the
      budget does not block (boundary pair);
   c. Power-quality exclusion: Power candidate gets no step bonus;
   d. phase gate: already pinned by `GateR_PhaseGated_FinalFiresSegmentationSkips` —
      add the step-bonus analogue only if cheap (Segmentation phase ⇒ no step bonus).
6. **wDim post-bonus quality guard**: construct a snapshot where the with-wDim global
   winner is NOT Dim/HalfDim (cross-bass contamination case) and assert the fallback to
   the without-wDim result; and a clean case where with-wDim wins legitimately.
7. **Score formula integration sanity** (one test): a single-cell snapshot where you can
   compute `(basisIndep + rcb + basisDep) × complexityFactor × augFactor + wComplete +
   wSeq` by hand and assert the exact result (pins the §3 formula and term ordering).

Follow the `gater_tests.cpp` fixture style (makeCell-type helpers, EXPECT_NEAR with 1e-9,
comments naming the §4 rule each test pins).

## Task 3 — Tie-stability tests (roadmap 1.7)

Pin the documented FP tie policy (scoring_model.md "Floating-point tie policy"):

1. **Exact-tie determinism**: two cells with bitwise-identical scores, different
   tiePriority → lower tiePriority wins (the Sus4♭5-before-HalfDim §2 case is the natural
   fixture: identical PC set, templates 7 vs 8).
2. **Exact-tie rootPc fallback**: identical score AND tiePriority, different rootPc →
   lower rootPc wins (if that is the actual comparator — survey first; pin whatever the
   comparator does).
3. **Near-tie canary**: two cells separated by a tiny margin (e.g. 0.02, the Δ=+7b class)
   → higher score wins regardless of tiePriority. Comment: this test is the canary that
   FP re-association (compiler/platform changes) would trip.

## Task 4 — Register, build, run

Add the new file to `src/composing/tests/CMakeLists.txt` (mirror existing entries).
```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
cd C:\s\MS\ninja_build_rel && ./composing_tests.exe > /tmp/s1a_compose.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s1a_compose.txt
cd C:\s\MS\ninja_build_rel && ./notation_tests.exe > /tmp/s1a_notation.txt 2>&1; echo "exit:$?"
tail -5 /tmp/s1a_notation.txt
cd C:\s\MS\ninja_build_rel && ./pipeline_snapshot_tests.exe > /tmp/s1a_snap.txt 2>&1; echo "exit:$?"
tail -10 /tmp/s1a_snap.txt
```
Expected: all green; composing count = 416 + (your new tests); 52/52; 11/11 zero diffs.

## Report — `cc_stage1a_report.md`

1. **Survey:** actual signatures; which functions were testable directly vs through
   `applyHarmonicFunction`; any instruction/code discrepancies.
2. **Test inventory:** table of every new test → the scoring_model §-rule it pins.
3. **Findings:** any behavior that looks wrong but was pinned as-is (the most valuable
   section — be specific; these feed Stage 3 decisions).
4. **Counts:** old → new composing test count; notation/snapshot confirmation.
5. **Commit proposal:** single commit, tests + CMakeLists only. Suggested message:
   ```
   test: pin function-layer bonuses and FP tie policy (Stage 1a)

   Unit tests for rootContinuityBonus, wSeq, wDim (incl. post-bonus quality
   guard), wStepIn/Out and all four applyStepBonusGuard guards (root-position,
   m7-family budget boundary, Power exclusion, phase gate), plus exact-tie and
   near-tie determinism tests pinning the scoring_model.md FP tie policy.
   Pins current behavior as the differential baseline for the Stage 3 decoder
   migration (implementation_roadmap.md 1.2, 1.7). Production code untouched.
   ```
   Do not commit until Cowork confirms.

Stop and ask if: a production-code change seems required to make something testable, a
test exposes a crash, or the §4 documentation materially contradicts the code (that would
be a sync-rule violation worth its own decision).
