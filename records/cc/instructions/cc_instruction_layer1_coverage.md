# CC Instruction — LAYER 1: close the coverage gate (branch coverage of the new code)

> Layer 1 is ratified (`e30bb45a4f`). The §5.1b coverage requirement (full branch coverage of the new code + a
> reported coverage check) was **not demonstrated** in the impl report — only the 8 functional T1–T8 tests. Per
> the standing full-coverage objective (`cowork_handoff.md`) and the per-layer rule, **close this before layer 2.**
> **TEST-ONLY: no production / behavior / scoring change — only add tests and measure.** Commit locally; Cowork
> verifies; user ratifies. This also serves as the well-timed coverage baseline (measured on the fresh layer-1
> code, not on code about to be replaced).

## §1 — Scope: the NEW layer-1 code ONLY
Branch coverage is required for the code layer 1 introduced/rewrote:
- **`notemodel/note_model.{h,cpp}`** — `NoteModel::build`, the tie-merge path, `overlapping`/`onsetIn`/range
  queries, the annotate-and-keep paths, every flag derivation.
- **The derived views** in `engravingbridge` — `weightedPcView` (the recomputed `collectRegionTones` logic incl.
  the de-inflation, the dense-start look-ahead branch, pedal pass, bass-floor fallback), `soundingAt`, the
  `buildTones` adapter, and the Score-based one-shot wrappers.

**OUT of scope (do NOT chase coverage now):** the co-tenant layer-2/3 code that layer 1 left in place —
`detectOnsetSubBoundaries`, `detectBassMovementSubBoundaries`, `collectPitchContext`, `findTemporalContext`
internals. They are covered when their layers are built; covering them now is wasted effort on code that will move.

## §2 — Measure (instrument branch coverage)
- Build the composing test binary with **branch-coverage instrumentation** (gcov/llvm-cov, whatever the build
  supports — follow `build_and_test.md`). Run `composing_tests` (T1–T8 + the existing tests that drive the views
  via `regionanalyzer`); add `notation_tests` if needed for the bridge wrapper paths.
- Extract per-function **branch** coverage for the §1 files. **Report the actual number** + the list of
  **uncovered branches** (file:line + the condition).

## §3 — Fill the gaps (test-only)
For each uncovered branch, classify and act:
- **Reachable** → add a **targeted unit test** (in `note_model_tests.cpp` or a sibling) that exercises it. Likely
  candidates the measurement will surface (illustrative, not a substitute for measuring): empty/`end<=start`
  region (early return), region with **no eligible staff**, **all-rest** region (empty note set), single-note,
  **grace-only** region, the **pedal-tail** pass (with a pedal-marked fixture), the **dense-start look-ahead**
  branch (≥3 PCs at start), the **bass passing-tone-floor fallback**, **overlap-query edges** (note onset before
  the range / release exactly at the boundary), and the **tie-merge** vs no-tie branches.
- **Genuinely unreachable / defensive** (e.g. a null-guard the call graph can't trigger) → **document it** in the
  report (file:line + why unreachable). Do **NOT** fabricate a contrived test, and do **NOT** delete the guard
  (that is a production change).

## §4 — Gate
- **Full branch coverage of the §1 new code** — every *reachable* branch exercised; every *unreachable* branch
  documented with a reason. Report the before→after coverage %.
- Both suites still pass (`composing_tests`, `notation_tests`); no snapshot/BIR/oracle change (this is test-only —
  if any production metric moves, a test accidentally touched production → STOP).
- New tests are deterministic and fixture-backed (reuse the `nm_*` fixtures where possible; add minimal fixtures
  only where a branch needs one).

## §5 — Workflow + deliver
Commit **locally (unpushed)** — test files + any new minimal fixtures only. Write `cc_layer1_coverage_report.md`:
the coverage tool, before→after branch coverage of the §1 files, the uncovered→now-covered branch list, and the
documented-unreachable branches with reasons. Cowork verifies the commit is test-only and the coverage is real;
user ratifies. Then layer 2.

## §6 — Stop conditions
- Any **production / behavior / scoring change** (anything outside test files + minimal fixtures) → STOP
  (test-only). A moved snapshot/BIR/oracle number is the tell.
- A branch can only be covered by **changing production** (e.g. it's dead code) → do NOT change production;
  document it as unreachable and surface it.
- Coverage drifts into the **out-of-scope co-tenant** code (detectors / pitch context) → stop chasing it; note
  it for its layer.
