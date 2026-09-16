# CC Instruction: Scoring Oracle / Competition Pipeline Segregation

## Pre-reading (mandatory)

Read the following before touching any code:
- `C:\s\MS\STATUS.md`
- `C:\s\MS\build_and_test.md`
- `C:\s\MS\docs/scoring_model.md`   ← required for any scoring-logic change
- `C:\s\MS\src\composing\analysis\function\harmonicfunctionlayer.h` (full)
- `C:\s\MS\src\composing\analysis\function\harmonicfunctionlayer.cpp` (full)
- `C:\s\MS\src\composing\analysis\chord\chordanalyzer.cpp` L2500–L3330
  (jointScoringEnabled, wSeqBonus/wDimBonus lambdas, wStepInBonus/wStepOutBonus,
   applyStepBonusGuard, per-bass competition loop, result building, gateCtx fill)
- `C:\s\MS\src\composing\analysis\region\regionanalyzer.cpp` — the three production
  call sites (search `applyHarmonicFunction`)

Current HEAD: `0ab219d4c5` (Phase 1 / E2d-prereq).
Baseline: composing 408/408 · notation 52/52 · pipeline snapshots 11/11.
Equivalence harness baseline: **13 divergences (6.1%)**.

---

## Why this change

`applyHarmonicFunction` was designed to be the progression-signal layer that
sits between raw template scoring and the post-scoring passes (Iter 86/91,
gates). Every attempt to enable it has failed because it was required to
replicate parts of `analyzeChord`'s competition loop from a snapshot, and the
replica was always incomplete. Three attempts (v2, v3, v3b) each revealed a
new missing piece; a fourth would find more.

The root cause, confirmed by CC's independent architectural review: the
competition loop — winner selection, threshold, cap, gateCtx production — must
live in exactly one place. Right now it lives in `analyzeChord`. It needs to
move to `applyHarmonicFunction`.

---

## Target architecture

### `analyzeChord` — scoring oracle only

After this change `analyzeChord` does **only** what depends on the raw tones
and key, and nothing that depends on progression context:

- Evaluate every (bass, root, template) combination.
- Compute `basisIndep`, `basisDep` (including `appliedBassBonus`),
  `complexityFactor`, `augFactor`, `wCompleteBonus` for each cell.
- Compute region-level metadata: `pcWeight`, `tpcForPc`, `scale`,
  `keyTonicPc`, `keyMode`, `distinctPcs`, `jointScoringEnabled`.
- Pack the cells and metadata into a `ScoringSnapshot`.
- Build a `HarmonicFunctionContext` from `context*` (previousRootPc,
  nextRootPc, previousBassPc, nextBassPc, keyFifths, keyMode).
- Call `applyHarmonicFunction` with the snapshot and ctx to obtain
  `results[]`, `chosenResult`, and a filled `gateCtx`.
- Return `results[]` (externally identical behaviour to today).

`analyzeChord` must **not** apply `rootContinuityBonus`, `wSeqBonus`,
`wDimBonus`, or step bonuses. It must **not** run a competition loop or
select a winner itself.

### `applyHarmonicFunction` — the competition pipeline

After this change `applyHarmonicFunction` owns the entire winner-selection
process. Its new signature (replace the existing one):

```cpp
void applyHarmonicFunction(
    const ScoringSnapshot&                   snapshot,
    const HarmonicFunctionContext&           ctx,
    const ChordAnalyzerPreferences&          prefs,
    std::vector<ChordAnalysisResult>&        results,      // out — filled from scratch
    ChordAnalysisResult&                     chosenResult, // out
    analysis::PostScoringGateContext*        gateCtx);     // out — filled completely
```

It must perform, in order:

1. **Re-score cells with progression signals.**
   For each cell in snapshot (choose between `cellsWithWDim` and
   `cellsWithoutWDim` as part of the quality guard below):
   - Add `rootContinuityBonus` into `basisIndep` before the cf × af multiply.
   - Compute `wSeqBonus` and `wDimBonus` as post-multiply additives.

2. **Pass B — step bonuses (`applyStepBonusGuard`).**
   For each bass group, apply the step-bonus guard exactly as it runs in the
   current competition loop (competitor check at `(bassPc−3)%12`, `kStepBudget`
   tolerance, `kWStepIn + kWStepOut` bonus for qualifying root-position
   non-Power candidates). This guard must replicate the current lambda in
   `chordanalyzer.cpp` exactly.

3. **Per-bass quality guard (wDim acceptance).**
   For each bass, compare the post-step best-with-wDim vs best-without-wDim
   score and accept the with-wDim variant only if its winner quality is
   `Diminished` or `HalfDiminished`.

4. **Cross-bass winner selection.**
   From all per-bass winners (using the accepted variant per bass), choose the
   global winner. No patching of any field — the winner is the cell that
   actually scored highest.

5. **Threshold.**
   `threshold = (winnerScore − winnerCell.appliedBassBonus) * kScoreThresholdRatio`.

6. **Build `results[]`.**
   From the winning bass's cells, include every cell whose signal-inclusive
   score ≥ threshold, capped at 3, with the winner at position 0. Append a
   diff-root entry if the diff-root condition holds. Construct each
   `ChordAnalysisResult` correctly (bassPc, bassTpc, rootPc, quality,
   tiePriority, score, etc.).

7. **Fill `gateCtx` completely.**
   Bass-dependent fields: `bassPc`, `bassTpc`, `threshold`, `rawCandidates`
   (all winning-bass cells above threshold, sorted score desc / tiePriority asc
   / rootPc asc — same sort key analyzeChord uses today at L3224–3229).
   Bass-independent fields (copy from snapshot metadata): `pcWeight`,
   `tpcForPc`, `scale`, `keyTonicPc`, `keyMode`, `distinctPcs`.

### What disappears

- `ChordAnalyzerPreferences::suppressProgressionSignals` — remove the field
  and every branch that reads it in `chordanalyzer.cpp` and
  `harmonicfunctionlayer.cpp`.
- `ChordAnalyzerPreferences::captureScoringSnapshot` — the snapshot is now
  always produced internally; the external opt-in pointer is no longer needed.
  Remove the field. (If a test or tool currently reads it, update that site.)
- The old `applyHarmonicFunction` signature (taking `results[]` and optional
  `snapshot*`/`prefs*`). Replace entirely with the new signature above.
- The three explicit `function::applyHarmonicFunction(results, chosenResult,
  fnCtx, nullptr, nullptr)` calls in `regionanalyzer.cpp`. They are now
  redundant: `analyzeChord` calls `applyHarmonicFunction` internally.

### What must not change

- `applyIter8691Pedal` — signature and behaviour unchanged.
- `applyPostScoringGates` — signature and behaviour unchanged.
- `analyzeChord`'s external signature (parameters + return type).
- All three `regionanalyzer.cpp` call-site call sequences (except removing
  the now-redundant `applyHarmonicFunction` call).
- `diagnoseChord` — read it; if it calls `analyzeChord` internally or reads
  `suppressProgressionSignals`/`captureScoringSnapshot` from prefs, update
  accordingly.
- `analyzeWithGates()` test helper — update if needed but preserve behaviour.

---

## Implementation notes

### Moving `kScoreThresholdRatio`

This constant is currently defined in `chordanalyzer.cpp`. It is now a
function-layer constant. Move it to `harmonicfunctionlayer.h` as an
`inline constexpr double`.

### Moving `applyStepBonusGuard`

The lambda in `chordanalyzer.cpp` must become a free function. Declare it in
`harmonicfunctionlayer.h` (or a shared internal header) so
`harmonicfunctionlayer.cpp` can call it. The function signature needs:
- `std::vector<ScoringCell>& perBassCells` (the cells for one bass, with
  mutable scores so the bonus can be added in place in the `finalScores` map
  or equivalent)
- `int candBassPc`
- The constants `kWStepIn`, `kWStepOut`, `kStepBudget` (already in
  `harmonicfunctionlayer.h`)

Preserve the guard logic exactly: competitor at `(bassPc−3)%12`, checks for
`HalfDiminished`, `Diminished`, and `Minor` with `intervalCount == 4`;
blocked if competitor score ≥ candidate score − `kStepBudget`.

### `wStepInBonus` / `wStepOutBonus`

If these are currently lambdas capturing local state in `analyzeChord`, they
need to become free functions or the logic must be inlined. Read the current
implementation carefully before deciding.

### `ScoringSnapshot` cell population

The snapshot is currently populated mid-loop inside `analyzeChord`'s
per-bass competition (L3116–3138) with **pre-step** cell scores. Under the
new design, `analyzeChord` (scoring oracle) captures cells immediately after
scoring (before any signal application), which is functionally the same.
The `wSeqBonus` field in each cell remains 0 at capture time (signals are
added by the function layer). Verify that `jointScoringEnabled` is correctly
set in the snapshot before `applyHarmonicFunction` reads it.

### `HarmonicFunctionContext` construction in `analyzeChord`

`analyzeChord` already has access to `context->previousRootPc`,
`context->nextRootPc`, `context->previousBassPc`, `context->nextBassPc`. Use
these to populate `fnCtx` before calling `applyHarmonicFunction`. Handle
`context == nullptr` (fnCtx defaults to −1 for unknown values).

### `docs/scoring_model.md`

Update §4 (scoring pipeline) and any section describing the suppression
mechanism. Add a §10 or §11 entry describing the new architecture: scoring
oracle vs competition pipeline, and the removal of `suppressProgressionSignals`.
The template count and 4-site checklist (§9) are unchanged by this redesign
(no templates are added or removed).

---

## Phased execution

### Phase 1 — Read and plan (no code changes)

Before writing a single line, read the full competition loop in
`chordanalyzer.cpp` (L2500–L3330) and map:
- Every lambda that needs to become a free function (list them).
- Every call site in `regionanalyzer.cpp` that will lose its explicit
  `applyHarmonicFunction` call.
- Every test/tool file that reads `suppressProgressionSignals` or
  `captureScoringSnapshot` from prefs.

Write this map as a short block comment at the top of your implementation
response, then proceed to Phase 2.

### Phase 2 — Implement

Make all changes. Build after each logical sub-step (scoring oracle refactor,
then function layer expansion, then cleanup). If any sub-step introduces a
build failure, fix it before proceeding.

Build command:
```
powershell.exe -Command "Start-Process 'C:\s\MS\setup_and_build.bat' -Wait -NoNewWindow"
```

### Phase 3 — Verify

Run all three suites and the equivalence harness:

```
cd C:\s\MS\ninja_build_rel

# Composing tests (includes equivalence harness)
./composing_tests.exe > /tmp/comp_out.txt 2>&1; echo "exit:$?"
head -30 /tmp/comp_out.txt

# Read harness report
cat C:\s\MS\src\composing\tests\equivalence_harness_report.txt

# Notation tests
./notation_tests.exe > /tmp/nota_out.txt 2>&1; echo "exit:$?"
head -20 /tmp/nota_out.txt

# Pipeline snapshots
./pipeline_snapshot_tests.exe > /tmp/snap_out.txt 2>&1; echo "exit:$?"
head -30 /tmp/snap_out.txt
```

If `pipeline_snapshot_tests` fails: the output change is expected if the
competition logic produces identical winners (it should). Run:
```
./pipeline_snapshot_tests.exe --update-goldens > /tmp/snap_update.txt 2>&1; echo "exit:$?"
./pipeline_snapshot_tests.exe > /tmp/snap_rerun.txt 2>&1; echo "exit:$?"
head -20 /tmp/snap_rerun.txt
```
Only update goldens if you have verified the new output is **correct**. Do not
update goldens to hide regressions.

Run the BIR corpus check:
```
cd C:\s\MS
python tools/run_bach_preset.py --preset Baroque --output-dir tools/corpus
python tools/analyze_inversion_errors.py
python tools/run_bach_preset.py --preset Jazz --output-dir tools/corpus
python tools/analyze_inversion_errors.py
```
Hard stops: Baroque BIR=false ≤ 25, Jazz BIR=false ≤ 13.

---

## Acceptance criteria

| Check | Required |
|---|---|
| Equivalence harness divergences | **0** |
| composing_tests | 408/408 (harness included) |
| notation_tests | 52/52 |
| pipeline_snapshot_tests | 11/11 (goldens may be refreshed if output verified correct) |
| Baroque BIR=false | ≤ 25 |
| Jazz BIR=false | ≤ 13 |
| `suppressProgressionSignals` field | Deleted |
| Explicit `applyHarmonicFunction` calls in regionanalyzer | Deleted |
| `docs/scoring_model.md` | Updated |

If the harness divergence count is not 0, **stop and report** — do not commit.
Identify which divergences remain and why.

---

## Output

Report:
1. The Phase-1 map (lambdas, call sites, prefs readers).
2. Build outcome for each phase.
3. Final test results (all four suites + BIR for both presets).
4. Equivalence harness divergence count (must be 0).
5. Any unexpected findings.

Do not commit unless all acceptance criteria are met and explicitly confirmed.
