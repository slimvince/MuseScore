# Iteration Plan: Inversion Disambiguation Redesign

## Status: active plan — do not implement without reading this first

## Background and goals

The chord analyzer has 66 remaining genuine inversion errors (Bb6→Gm7/Bb type) after
the enharmonic fast path fix (which resolved 32 from the original 151). A series of
attempts to fix the remainder introduced architectural violations and regressions:

- Temporal score bonuses were added to `contextualBonuses()` inside `RuleBasedChordAnalyzer`
  (violates ARCHITECTURE.md §4.1c — contextual heuristics must not be added to the
  vertical sonority analyzer)
- Baroque stepwise bonuses were amplified to 0.80, exceeding `bassNoteRootBonus` (0.70),
  causing 199 gross false-positive inversions
- Temporal context computation was placed in `batch_analyze.cpp`'s private loop instead
  of the shared `analyzeSection` pipeline (violates §2.10 — shared logic belongs in
  the composing module)

This plan fixes the violations first, then redesigns correctly.

---

## Standing rules — CC must read these files at the start of EVERY iteration

1. `CLAUDE.md` — build/test commands, autonomous scope
2. `STATUS.md` — top summary + today's entries only
3. `ARCHITECTURE.md` — specifically §2.10 (single implementation), §4.1c (vertical/
   contextual boundary, inversion correction layer), §4.1d (unified orchestration layer)
4. `docs/unified_analysis_pipeline.md` — unified pipeline design, P1/P2/P3/P4 paths

## Standing design decisions CC must respect

- **§2.10**: Any shared algorithm belongs in `src/composing/`, not in `batch_analyze.cpp`
  or bridge helpers. Two copies = technical debt.
- **§4.1c**: `RuleBasedChordAnalyzer` is a vertical sonority analyzer. Do not add
  contextual heuristics (temporal, progression-aware) to it. Inversion correction
  belongs in the post-ranking correction layer, not in `contextualBonuses()`.
- **Unified pipeline**: P1 (chord staff), P2 (annotation), P3 (status bar/context menu),
  P4 (right-click note) all use the same inference algorithm. Emitter behavior may
  differ; the algorithm does not.
- **Score bonus ceiling**: Inversion score bonuses must stay strictly below
  `bassNoteRootBonus` (0.70). Any bonus ≥ 0.70 causes outright wins that bypass every
  safety valve, producing systematic false-positive inversions.
- **Enharmonic fast path**: The categorical swap (preferMinorOverMajorAdd6 + AddedSixth
  guard) is working and must not be touched. It is the correct architectural pattern
  for inversion disambiguation: a direct post-ranking decision, not a score modifier.
- **Do not commit** — report results and wait for sign-off after every iteration.
- **Tests**: 407/407 must pass, RealDiff ≤ 4, after every code-change iteration.
- **Corpus runs**: always use `--preset Baroque` unless the iteration explicitly tests
  another preset.

---

## Iteration 0 — Revert harmful changes, establish clean baseline

**Type:** code changes + measurement

**Goal:** Undo the architectural violations introduced during the inversion redesign
attempts. Reach a clean state with only the working fixes in place.

**What to change:**

In `chordanalyzer.h` `ChordAnalyzerPreferences`:
- Remove these four preference fields entirely:
  `nextRootMatchesAltInversionBonus`, `consecutiveBassStepwiseInversionBonus`,
  `recentRootMatchesAltInversionBonus`, `weakBeatInversionBonus`, `weakBeatThreshold`
- Keep `maxTotalInversionContextBonus` (still useful as a safety cap for the existing
  four score-addition signals)
- Add a TODO comment on the existing four signals
  (`stepwiseBassInversionBonus`, `stepwiseBassLookaheadBonus`, `sameRootInversionBonus`,
  `completeTriadInversionBonus`):
  `// TODO: These belong architecturally in the post-ranking correction layer
  // (ARCHITECTURE.md §4.1c), not in the vertical sonority scorer. Technical debt.`

In `chordanalyzer.cpp` `contextualBonuses()`:
- Remove the scoring code for the four removed signals
- Keep the cap accumulation logic for the remaining four signals
- Set the cap's effect via `maxTotalInversionContextBonus` default (2.0 — does not
  bite on the existing four signals whose max combined is 1.85)

In `batch_analyze.cpp` preset builder:
- Baroque preset: remove all amplified inversion bonus values; leave only
  `preferMinorOverMajorAdd6 = true` and the standard `extensionThreshold` as Baroque-
  specific settings. All inversion bonuses use defaults.
- Jazz preset: remove the four new signal reduced values. Keep existing Jazz settings.
- Keep `ChordTemporalContext` new fields (`nextRootPc`, `consecutiveBassStepwiseCount`,
  `recentRootPcs`, `regionMetricWeight`) populated in the batch loop — they will be
  needed as gate conditions in Iteration 3.

**What NOT to change:**
- `preferMinorOverMajorAdd6` flag + AddedSixth guard in the fast path — working, leave alone
- `ChordTemporalContext` struct fields — keep all, they are used in later iterations
- The existing four score-addition signals in `contextualBonuses()` — leave as-is with
  their default values; they help the margin-based correction but must not be amplified
  beyond defaults in any preset

**Verification:**
```
Build:                     pass / fail
Tests:                     407/407 pass
RealDiff:                  before=4, after=N
Corpus preset:             Baroque
3-way genuine BIR=true:    before=66, after=N  (expect ~119 — back to post-enharmonic baseline)
3-way genuine BIR=false:   before=364, after=N (expect ~252)
2-way bassIsRoot:          before=620, after=N
Regressions:               none
```

---

## Iteration 1 — Investigation: analyzeSection structure

**Type:** read-only investigation, no code changes

**Goal:** Understand the shared pipeline before modifying it. CC must report enough
detail that Iteration 2 can be specified precisely without further investigation.

**What to read and report:**

1. Find `analyzeSection` — which file, which namespace, full signature
2. Read its complete implementation: how it iterates regions, how it currently
   constructs `ChordTemporalContext` per region, what it puts on `AnalyzedRegion`
3. Does it currently have any look-ahead logic? Any rolling state?
4. How is it called by P1 (chord staff), P2 (annotation), P3 (status bar/context menu)?
   Which files call it?
5. What is `AnalyzedRegion`? Full struct definition.
6. Is there an `AnalyzedRegion::temporalExtensions` field or equivalent? If not, is
   there a planned location for it?
7. Where does `findTemporalContext()` fit — is it called by `analyzeSection` or by
   consumers directly?
8. Read `docs/unified_analysis_pipeline.md` fully — report what Phase 3c says about
   temporal context migration and `AnalyzedRegion::temporalExtensions`
9. What would a two-pass approach inside `analyzeSection` look like? Where would the
   rolling state (`recentRootPcs`, `consecutiveBassStepwiseCount`) live between regions?

**Report format:**
Prose + code excerpts. Enough detail to write Iteration 2 without another investigation.

---

## Iteration 2 — Move temporal context into shared pipeline

**Type:** code changes

**Goal:** §2.10 compliance. The temporal context computation (`nextRootPc`,
`consecutiveBassStepwiseCount`, `recentRootPcs`, `regionMetricWeight`) must move from
`batch_analyze.cpp`'s private loop into `analyzeSection` in the composing module, so
P1/P2/P3/P4 all inherit it automatically.

**Approach:** Two-pass or one-pass-with-cache, whichever gives better inference quality.
Performance is not a concern if quality is equal; quality wins.

**What to implement** (based on Iteration 1 findings — adjust to actual structure):
- Add rolling state to `analyzeSection`'s region loop:
  - `consecutiveBassStepwiseCount` running counter (increment on stepwise, reset on leap)
  - `recentRootPcs` 3-region circular buffer (shift after each region resolves)
- Add look-ahead per region:
  - `nextRootPc`: lightweight `analyzeChord` on the next region's tones (no context,
    default prefs) — same approach currently in `batch_analyze.cpp`
  - `bassIsStepwiseToNext`: `isDiatonicStep(currentBassPc, nextBassPc)`
- Add metric weight per region:
  - `regionMetricWeight` from beat type of region-start segment
- All fields populated on the `ChordTemporalContext` passed to `analyzeChord`, so the
  chord analyzer receives full context on every call

**§2.10 compliance step:**
After implementing in `analyzeSection`, remove the equivalent computation from
`batch_analyze.cpp`'s `analyzeScore()` private loop. The batch tool becomes a thin
consumer of `analyzeSection` like the other paths.

**What NOT to change:**
- The chord analyzer itself (`chordanalyzer.cpp`) — no scoring changes in this iteration
- `contextualBonuses()` — no changes
- The enharmonic fast path — no changes

**Verification:**
```
Build:                     pass / fail
Tests:                     407/407 pass
RealDiff:                  ≤ 4
Corpus preset:             Baroque
3-way genuine BIR=true:    should be unchanged from Iteration 0 baseline
3-way genuine BIR=false:   should be unchanged from Iteration 0 baseline
All paths verified:        P1/P2/P3 confirmed receiving nextRootPc, recentRootPcs,
                           consecutiveBassStepwiseCount, regionMetricWeight
```

---

## Iteration 3 — Temporal gates in post-ranking correction

**Type:** code changes

**Goal:** Use the temporal context fields as gate conditions for categorical inversion
swaps — not as score additions. Extend the enharmonic fast path in `chordanalyzer.cpp`
with three additional trigger conditions.

**Architectural constraint:** Gates live in the post-ranking correction block, outside
`RuleBasedChordAnalyzer`'s scoring loop. They do not modify any scores. They make a
direct swap decision based on harmonic context evidence.

**Gates to add** (for non-Jazz presets — gated by `preferMinorOverMajorAdd6 = true`):

Inside the enharmonic fast path block, after the existing AddedSixth guard, add:

```
Gate B: context->nextRootPc != -1 && context->nextRootPc == altRootPc
  → The next chord confirms this harmony continues. Strong forward evidence.

Gate C: altRootPc appears in context->recentRootPcs AND context->bassIsStepwiseFromPrevious
  → This root was recently active and the bass is passing through it.

Gate D: context->consecutiveBassStepwiseCount >= 2
  → Multiple consecutive stepwise bass steps = scalar passing line.
    Almost certainly an inversion, not a new root.
```

Each gate independently triggers the same swap as the AddedSixth guard (swap
`results[0]` and `results[bestAltIdx]`, skip margin check). If any one gate fires,
the swap happens.

**Important:** The enharmonic pair check (winner is Major, bestAlt is Minor/Minor7,
`altRootPc == (winnerRootPc + 9) % 12`) must still hold for all gates. Gates are
additional conditions within the enharmonic pair decision, not general inversion logic.

**What NOT to change:**
- `contextualBonuses()` — no changes
- Score values of any kind
- The AddedSixth guard condition — leave exactly as is

**Verification:**
```
Build:                     pass / fail
Tests:                     407/407 pass
RealDiff:                  ≤ 4
Corpus preset:             Baroque
3-way genuine BIR=true:    before=N (Iter 0 baseline), after=N  (expect reduction)
3-way genuine BIR=false:   before=N (Iter 0 baseline), after=N  (must not increase)
2-way bassIsRoot:          before=N, after=N
Chord identity:            before=N%, after=N%
Gates breakdown:           how many of the resolved errors were caught by B vs C vs D
Regressions:               none
```

---

## Iteration 4 — Empirical tuning

**Type:** test-only (no code changes unless results indicate clear improvements)

**Goal:** Determine optimal values for two empirical questions. Run as separate
sub-tests and report results before any changes are committed.

**Sub-test A — Standard preset `preferMinorOverMajorAdd6`:**
Currently `true` for Standard preset (C6 → Am7/C). In standard pop/rock, C6 is a
legitimate harmonic entity distinct from Am7/C. Test both `true` and `false` on a
Standard-repertoire corpus.
- Run corpus with `--preset Standard` both ways
- Report chord identity and genuine error counts for each
- Do NOT change any value without reporting first

**Sub-test B — Baroque stepwise bonus values:**
The existing `stepwiseBassInversionBonus` and `stepwiseBassLookaheadBonus` currently
use defaults (0.50) in Baroque. The ceiling is strictly < 0.70 (bassNoteRootBonus).
Test values 0.50, 0.55, 0.60, 0.65 for Baroque.
- For each value: run corpus `--preset Baroque`, report genuine BIR=true errors and
  BIR=false errors and chord identity
- Find the value that maximises genuine error reduction without increasing BIR=false
- Report the table; do NOT change committed values without sign-off

**Verification format:**
```
Sub-test A:
  Standard + preferMinorOverMajorAdd6=true:   chord identity=N%, genuine errors=N
  Standard + preferMinorOverMajorAdd6=false:  chord identity=N%, genuine errors=N
  Recommendation: true / false

Sub-test B:
  stepwise=0.50: BIR=true=N, BIR=false=N, chord identity=N%
  stepwise=0.55: BIR=true=N, BIR=false=N, chord identity=N%
  stepwise=0.60: BIR=true=N, BIR=false=N, chord identity=N%
  stepwise=0.65: BIR=true=N, BIR=false=N, chord identity=N%
  Recommendation: value=N
```

---

## Iteration 5 — Full path verification

**Type:** verification + any remaining fixes

**Goal:** Confirm the unified pipeline is working correctly across all paths after the
changes in Iterations 2–4.

**What to verify:**
1. P1 (chord staff population): receives full temporal context including nextRootPc,
   recentRootPcs, consecutiveBassStepwiseCount
2. P2 (annotation emitter): same
3. P3 (status bar / context menu): same — confirm the bridge path calls `analyzeSection`
   and not a separate lightweight path that skips temporal context
4. P4 (right-click note annotation): confirm it goes through the unified pipeline;
   confirm the emitter (not the algorithm) handles the "force annotation even if
   passing note" behavior
5. Confirm `findTemporalContext()` in the bridge is no longer the primary temporal
   context source (it was a workaround; `analyzeSection` should now own this)
6. Run the full 407/407 test suite
7. Run corpus Baroque — report final genuine error count

**Report format:**
```
Build:                     pass / fail
Tests:                     407/407 pass
RealDiff:                  ≤ 4
Corpus preset:             Baroque
3-way genuine BIR=true:    final count
3-way genuine BIR=false:   final count
2-way bassIsRoot:          final count
Chord identity:            final %
Path verification:
  P1 temporal context:     full / partial / none
  P2 temporal context:     full / partial / none
  P3 temporal context:     full / partial / none
  P4 unified pipeline:     yes / no / partial
Remaining genuine errors:  characterize any that survive all fixes
```

---

## Between-iteration checklist

After every code-change iteration:
1. `cmd.exe //c "C:\s\MS\setup_and_build.bat"` — must pass
2. `cd C:\s\MS\ninja_build_rel && ./composing_tests.exe` — 407/407, RealDiff ≤ 4
3. `python tools/analyze_inversion_errors.py` with `--preset Baroque`
4. Review `src/composing/tests/chord_mismatch_report.txt`
5. No commit until explicit sign-off

## Technical debt log (do not fix in this plan — note only)

- The four existing score-addition inversion signals (`stepwiseBassInversionBonus`,
  `stepwiseBassLookaheadBonus`, `sameRootInversionBonus`, `completeTriadInversionBonus`)
  are in `contextualBonuses()` inside `RuleBasedChordAnalyzer`. Per §4.1c they belong
  in the post-ranking correction layer. Deferred — they are working without causing
  regressions at default values.
- Duplicate `collectRegionTones()` in bridge and `batch_analyze.cpp` violates §2.10.
  Tracked in ARCHITECTURE.md §4.1c. Deferred to a dedicated refactor session.
