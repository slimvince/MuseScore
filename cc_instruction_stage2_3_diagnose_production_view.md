# CC Instruction: Stage 2.3 — diagnoseChord becomes a true production view (+ 2 riders)

## Context

Roadmap **2.3**, the last open HIGH finding from the implementation review.
`diagnoseChord` is currently a second scorer: it skips `applyHarmonicFunction` entirely
(no rcb / wSeq / wDim / steps / Gate R), uses the legacy single-bass path, applies no
threshold/cap, and adds contextual terms via the diagnose-only `contextualBonuses`
helper. It has already misled two investigations (the bwv320 "slash-synthesis"
retraction; the bwv14.5 mischaracterisation) — both documented in COWORK_HANDOFF.
Architecture principle #2: *"diagnoseChord must be a view into the production
pipeline's intermediate state, not a separate parallel scorer."*

**Goal:** a diagnose call must produce **the production winner by construction** —
because it runs the production code — plus introspection detail, never a reimplementation.

Standing rules (handoff): never guess; pin behavior; explicit staging; `muse` never.
Base: `0520a2dda2`. Pre-authorized scope (`src/composing/**`) suffices; riders touch
`tools/analyze_inversion_errors.py`, `BUILD_AND_TEST.md`, `docs/score_inventory.md`.

---

## Task 1 — Survey (report §1 before implementing)

1. **All `diagnoseChord` consumers**: tests, any batch_analyze diagnostic mode, any
   tool that parses its dump format (the C3/C4 investigations got dumps from
   somewhere — find the path). For each consumer: what fields does it actually use?
2. **The dump's current content**: per-cell vertical breakdown (12×17 grid),
   `contextualBonuses` inline rcb, what's missing vs production (progression signals,
   competition, threshold/cap, Iter 86/91/pedal, gates A–L).
3. **Feasibility of the preferred design** (Task 2): can `analyzeChord` expose its
   internally-built `ScoringSnapshot` via an optional out-param (mirroring the existing
   `gateCtxOut` pattern) with zero behavior change when unused? Identify any copy-cost
   or lifetime concern.

## Task 2 — Implement: diagnose = production call + introspection

Preferred design (adjust only with stated reasons in the report):

1. `analyzeChord` gains an optional `fn::ScoringSnapshot* snapshotOut = nullptr`
   (pattern: `gateCtxOut`). When null: byte-identical behavior, zero cost beyond a
   branch. When set: copies/moves the snapshot out after `applyHarmonicFunction` ran.
2. `diagnoseChord` is rewritten to: call the REAL `analyzeChord` (same prefs, same
   temporal context, `snapshotOut` + `gateCtxOut` set), then the REAL
   `applyIter8691Pedal` + `applyPostScoringGates` — i.e., the exact production
   sequence every `regionanalyzer` commit site runs. The dump then decorates:
   - the per-cell vertical breakdown from the snapshot (KEEP this — it is the tool's
     value), clearly labeled as ORACLE terms;
   - the competition terms per surviving candidate (rcb incl. Gate R outcome, wSeq,
     wDim, step bonuses) — sourced from the pipeline's actual inputs (snapshot +
     context), labeled COMPETITION;
   - the post-gate trail: which of Iter 86/91/pedal and gates A–L fired (from
     gateCtx / result deltas), labeled POST-GATES;
   - the FINAL winner — which is the production winner by construction.
3. **Eliminate the duplicates this makes dead**: `kDiagTemplates` (byte-identical
   mirror of the template array — a 5-site sync burden) and `contextualBonuses`
   (diagnose-only rcb divergence, flagged in audit Finding 2b) should both become
   unreferenced under this design — remove them and update `scoring_model.md` §2/§9
   (sync rule: the atomic-update site list shrinks; renumber accordingly) and the
   stale-comment sites that reference them.
4. Update consumers found in Task 1 to the new dump format (mechanical). If an
   external-format consumer can't be updated in scope: stop and ask.

## Task 3 — Tests

1. **The agreement invariant (the point of 2.3):** new test iterating the catalog
   fixtures (and a sample of musicxml fixtures): for each,
   `diagnoseChord(...).finalWinner == analyzeWithGates(...).winner` — identity AND
   score. This pins "diagnose can never drift from production again."
2. **The acceptance case from the roadmap:** a Δ=+7b-shape fixture (bwv320 mapping
   from `postscoringgates_tests.cpp`): diagnose's dump must show rcb withheld by
   Gate R on the continued-root candidate and the production winner C — the exact
   information whose absence caused the historical mis-diagnoses.
3. Keep/adapt any existing diagnose tests per their actual intent (survey).

## Task 4 — Riders (missed adjustments from the hygiene pass — relay gap)

1. `tools/analyze_inversion_errors.py`: no-arg default `_CORPUS_DIR` →
   `tools/corpus/baroque` (matching characterise; the flat-dir default now errors);
   BUILD_AND_TEST.md §4 legacy no-arg line repointed to `--corpus-dir tools/corpus/baroque`.
2. `docs/score_inventory.md`: add the WiR-coverage fact prominently in the
   `tools/corpus` section: **only 326/353 chorales resolve to WiR human annotations
   (324 distinct analysis files; 27 scores can never produce a "genuine" gate error)**
   + one line on the gate's three qualifiers (human-adjudicated 326, music21-filtered,
   batch granularity) pointing to roadmap 5.2.

## Task 5 — Verify (full gate — production code is touched)

Build; composing (498 + new agreement tests) / notation 52 / snapshots 11/11 ZERO
diffs; Python 68/68; BIR both presets via per-preset dirs → Baroque 13 (+24/13 via
analyze_inversion with its NEW default, exercising rider 1), Jazz 7 + identity set.
**Production byte-identity is a hard requirement** — diagnoseChord's own output format
is the only thing allowed to change.

## Commits (propose, await Cowork as a set)

- D1 `refactor: diagnoseChord replays the production pipeline (Stage 2.3)` — analyzeChord
  snapshotOut + diagnose rewrite + kDiagTemplates/contextualBonuses removal +
  scoring_model.md sync + tests.
- D2 `tools+docs: analyze_inversion_errors default to validated corpus dir; WiR-coverage
  fact in score_inventory (hygiene riders)`.

## Report — `cc_stage2_3_report.md`

§1 survey (consumers + dump usage); §2 design as built + deviations; §3 what became
dead and was removed (with the §9 sync-site list before/after); §4 the agreement
invariant + Δ=+7b dump excerpt (show the rcb/Gate-R lines); §5 verification table;
§6 unknowns. Tag claims [probe]/[code].

Stop conditions: snapshotOut can't be added without behavior change; any snapshot diff
or BIR movement; an unupdatable dump consumer; the agreement invariant failing on ANY
fixture (that would mean the replay isn't faithful — find out why, don't relax the test).
