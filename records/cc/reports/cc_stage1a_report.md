# CC Report: Stage 1a — Pin the function layer (unit tests) + tie stability

*Executed 2026-06-10 against HEAD `e7d4ba2b1a`. Instruction:
`cc_instruction_stage1a_functionlayer_tests.md` (roadmap items 1.2 + 1.7).*

**Session note:** a VS Code restart interrupted the first execution attempt before
anything was written to disk; this run restarted Task 1 from scratch. No partial
state was carried over.

## Summary

- **23 new tests** in `src/composing/tests/functionlayer_tests.cpp` (new file),
  registered in `src/composing/tests/CMakeLists.txt`. Composing 416 → **439/439**.
- **52/52 notation · 11/11 pipeline snapshots** (1 intentional skip =
  `PipelineDivergenceCObservation.GenerateReport`). Zero snapshot diffs, no goldens
  touched.
- **Zero production-code changes.** Only the two allowed files were touched.
  No BIR run performed — the production binary's analysis code is untouched, so the
  24/13 / 35/7 baselines cannot have moved.
- All tests passed on the first run; no behavior had to be "discovered" by trial.

## 1. Survey (Task 1)

### Directly testable free functions (exposed in `harmonicfunctionlayer.h`)

| Function | Signature (actual) |
|---|---|
| `rootContinuityBonus` | `(int candidateRootPc, int previousRootPc, double bonusValue) → double` |
| `wSeqBonus` | `(int candRootPc, int nextRootPc, int distinctPcs, bool jointScoringEnabled) → double` |
| `wDimBonus` | `(int candRootPc, ChordQuality quality, int nextRootPc, int distinctPcs, bool jointScoringEnabled) → double` |
| `wStepInBonus` | `(int candBassPc, int rootPc, bool jointScoringEnabled, int previousBassPc) → double` |
| `wStepOutBonus` | `(int candBassPc, int rootPc, bool jointScoringEnabled, int nextBassPc) → double` |

All five are stateless (post-`e7d4ba2b1a`; no phase parameter). Signatures match the
instruction's expectations; no discrepancies.

### Only reachable through `applyHarmonicFunction` (file-local — NOT re-exposed)

- **`applyStepBonusGuard`** — anonymous namespace in `harmonicfunctionlayer.cpp`
  (operates on the file-local `WorkCand` type, so re-exposing it would have required a
  production change). All four §4 guards tested end-to-end.
- **wDim post-bonus quality guard** (Iter 97a-v3) — inline in `applyHarmonicFunction`
  after the bass-group loop. Tested end-to-end.
- **Sort comparator / FP tie policy** — inline lambda in `applyHarmonicFunction`
  (~L384). Tested end-to-end; the comparator is exactly as documented:
  score desc → tiePriority asc → rootPc asc, no epsilon.
- **Score formula + term ordering** — Pass A arithmetic. Pinned via a hand-computed
  single-cell snapshot.

### Pass A/B/C structure (confirmed)

Pass A: per-cell `rcb` (with Gate R zeroing, Final phase only) folded into basisIndep
**before** the `× complexityFactor × augFactor` multiply; `wCompleteBonus`, `wSeq`,
`wDim` added **after**. Two parallel variants built (with-wDim / without-wDim).
Pass B: `applyStepBonusGuard` on both variants, only when
`phase == ScoringPhase::Final`. Pass C: per-bass local best → global best per variant;
then the post-bonus quality guard picks the variant; sort, threshold
(`(best − winnerBassBonus) × 0.75`), top-3 + diff-root append.

### Instruction/code discrepancies

None material. Two minor notes:

1. **`wStepIn`/`wStepOut` have an extra documented-nowhere non-fire condition:**
   `previousBassPc == candBassPc` (same bass, no motion) returns 0 — distinct from the
   `< 0` unknown check. Pinned in
   `WStepIn_NoFireOnLeapSlashOrMissingContext`. Not a contradiction of §4 (delta 0 is
   not a step), but §4 doesn't call it out explicitly.
2. **§2 doc nuance (see Findings F1)** — the Sus4♭5/HalfDim "identical PC sets" wording.

## 2. Test inventory (Task 2 + 3)

All in `functionlayer_tests.cpp`, suite `Composing_FunctionLayerTests`.

| # | Test | Pins (scoring_model.md rule) |
|---|---|---|
| 1 | `Constants_MatchScoringModelSection4` | §4 values: kWSeq 0.20, kWDim 0.15, kWStepIn/Out 0.10, kStepBudget 0.21, kScoreThresholdRatio 0.75, prefs.rootContinuityBonus 0.40 |
| 2 | `RootContinuity_FiresOnEqualRoot` | §4 rcb fire + configured-value passthrough |
| 3 | `RootContinuity_NoFireOnDifferentOrUnknownRoot` | §4 rcb non-fire (differs / previousRootPc = −1) |
| 4 | `WSeq_FiresOnPerfectFourthUpToNextRoot` | §4 w_seq fire incl. mod-12 wraparound |
| 5 | `WSeq_NoFireWhenAnyConditionBroken` | §4 w_seq: each condition individually broken (interval ≠ 5, P5 direction, distinctPcs 3, joint off, next = −1) |
| 6 | `WDim_FiresForDimAndHalfDimLeadingTone` | §4 w_dim fire (Dim + HalfDim) |
| 7 | `WDim_NoFireOnWrongQualityIntervalOrSparseRegion` | §4 w_dim non-fire incl. the distinctPcs ≥ 4 quality-flip guard (commented per instruction) |
| 8 | `WStepIn_FiresOnSemitoneOrWholeToneEitherDirection` | §4 w_stepIn fire: deltas {1,2,10,11} |
| 9 | `WStepIn_NoFireOnLeapSlashOrMissingContext` | §4 w_stepIn non-fire: leap, slash, prev = −1, prev == bass, joint off |
| 10 | `WStepOut_MirrorsStepInAgainstNextBass` | §4 w_stepOut symmetric fire/non-fire |
| 11 | `StepGuard_RootPositionOnly_SlashGetsNoBonus` | §4 step guard 2 (root-position only), via pipeline |
| 12 | `StepGuard_RootPositionCandidateGetsBonus` | control: root-position twin gets +0.10 |
| 13 | `StepGuard_M7FamilyCompetitorInsideBudgetBlocks` | §4 step guard 3: HalfDim competitor at (bass−3) mod 12, 0.80 ≥ 1.0 − kStepBudget → blocked |
| 14 | `StepGuard_M7FamilyCompetitorOutsideBudgetDoesNotBlock` | §4 step guard 3 boundary pair: 0.78 < 0.79 → not blocked |
| 15 | `StepGuard_MinorTriadCompetitorDoesNotBlock_Min7Does` | §4 step guard 3 quality scope: isMin7 ≡ Minor ∧ intervalCount == 4; plain minor triad spares the bonus |
| 16 | `StepGuard_PowerQualityExcluded` | §4 step guard 4 (Power exclusion) |
| 17 | `StepGuard_SegmentationPhaseSuppressesStepBonus` | §4 step guard 1 (phase gate) — step-bonus analogue of the Gate R phase test |
| 18 | `WDimPostBonusGuard_RejectsContaminatedWithVariant` | §4 w_dim post-bonus quality guard: with-winner not Dim/HalfDim → fallback to without-wDim |
| 19 | `WDimPostBonusGuard_AcceptsDimWinner` | §4 post-bonus guard: Dim with-winner accepted, legitimately overturning a higher-scoring rival bass |
| 20 | `ScoreFormula_SingleCellHandComputed` | §3 formula + term ordering: (1.3 + 0.40 rcb + 0.25) × 0.9 × 0.8 + 0.5 + 0.20 = 2.104, asserted at 1e-12; also pins w_seq inversion-independence (slash cell) |
| 21 | `TiePolicy_ExactTie_LowerTiePriorityWins` | §3 tie policy key 2: identical doubles, tpl 7 (Sus4♭5) beats tpl 8 (HalfDim) regardless of insertion order |
| 22 | `TiePolicy_ExactTie_LowerRootPcBreaksFullTie` | §3 tie policy key 3: same score AND tiePriority → lower rootPc wins (confirmed: the comparator does fall back to rootPc) |
| 23 | `TiePolicy_NearTie_HigherScoreWinsRegardlessOfTiePriority` | §3 near-tie canary: 0.02 margin (Δ=+7b class) decided by raw double inequality; FP re-association tripwire (commented) |

Fixture style follows `gater_tests.cpp`: `makeCell`/`makeSnapshot`/`runPipeline`
helpers, `EXPECT_NEAR` 1e-9 (1e-12 where bitwise-reproducible), §-rule comments.

## 3. Findings (pinned as-is, NOT fixed)

**F1 — §2 doc wording: Sus4♭5 vs HalfDim "identical PC sets" is imprecise.**
The full interval sets differ ({0,5,6,10} vs {0,3,6,10}); no transposition makes them
equal. The exact-tie mechanism is their shared **subset {0,6,10}**: when only those
three tones sound, both templates match identically at the same root and tie exactly.
The tie-policy behavior itself is correct and now pinned (test 21); only the doc
wording overstates the equivalence. Doc-only; left for a later doc pass (sync rule not
violated — no code change here).

**F2 — Post-bonus quality-guard winner scan is first-wins on exact ties.**
The scan that determines `postBonusWinnerQuality` uses strict `>`, so when the
with-wDim variant's best score is exactly tied between a Dim and a non-Dim cell, the
**cell-storage-order-first** one decides whether the with-variant is accepted. Benign
today (both variants are identical whenever wDim didn't fire, and a genuine wDim fire
breaks the tie by +0.15), but it is an ordering sensitivity the Stage 3 decoder
migration should be aware of. Not separately testable without contrived equality; not
pinned as its own test.

**F3 — wStep helpers treat `previousBassPc == candBassPc` as no-fire** (delta 0 is not
in {1,2,10,11}, and there is also an explicit early-out). Musically sensible
(repeated bass is not a step), but §4's gate list doesn't mention it. Pinned in test 9.

**F4 — The m7-family guard blocks at `>=` (competitor exactly at
`cand.score − kStepBudget` blocks).** The boundary pair (tests 13/14) brackets it at
0.80/0.78 rather than exact equality because `1.0 − 0.21` is not exactly representable;
an exact-equality pin would itself be FP-fragile. The `>=` semantics are pinned by the
bracket.

**F5 — Diff-root append interacts silently with the threshold.** While designing
fixtures: a sub-threshold diff-root candidate is never appended (the append loop
breaks at the threshold), so "guaranteed inversion alternative" is only guaranteed
among above-threshold candidates. Matches the code comment's intent; noted for the
Stage 3 obligation list.

No crashes, no UB, no §4/code contradictions requiring a stop.

## 4. Counts

| Suite | Before | After |
|---|---|---|
| composing_tests | 416/416 | **439/439** (+23, all new) |
| notation_tests | 52/52 | **52/52** |
| pipeline_snapshot_tests | 11/11 (+1 skip) | **11/11 (+1 skip)**, zero diffs |

BIR: not re-run — tests-only change; analysis code in the production binary is
byte-identical, baselines remain 24/13 (Baroque) / 35/7 (Jazz) by construction.

## 5. Commit proposal (awaiting Cowork confirmation — NOT committed)

Files: `src/composing/tests/functionlayer_tests.cpp` (new),
`src/composing/tests/CMakeLists.txt` (one line).

```
test: pin function-layer bonuses and FP tie policy (Stage 1a)

Unit tests for rootContinuityBonus, wSeq, wDim (incl. post-bonus quality
guard), wStepIn/Out and all four applyStepBonusGuard guards (root-position,
m7-family budget boundary, Power exclusion, phase gate), plus exact-tie and
near-tie determinism tests pinning the scoring_model.md FP tie policy.
Pins current behavior as the differential baseline for the Stage 3 decoder
migration (implementation_roadmap.md 1.2, 1.7). Production code untouched.
```
