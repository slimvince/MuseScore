# CC Instruction — Phase 5 backfill round 2, cluster 1 of 4: engravingbridge branch tests (~53, oracle-asserted)

> **Why.** The stable-half branch triage (`cowork_phase5_branch_backfill_spec.md`) routed ~321 reachable unhit branches
> to ADD-TEST. This is **cluster 1 — engravingbridge (~53)**. Same rules as backfill round 1: **coverage is the
> gap-finder, NOT the goal.** Each test asserts the **theory/contract-correct value (the oracle), re-derived at
> source** — never an echo of current output. A correct oracle that **fails** current code is a **surfaced defect**
> (`DISABLED_`/xfail + flag), not a weakened test. **Tests-only — no production logic/behaviour change.**
>
> *(Reminder: the never-bash rule is Cowork's file-reading discipline; it does not constrain your build/test/tool runs.)*

## §0 — Preamble
If any `cowork_*`/`COWORK_*` docs are unstaged, commit them local-only first (`docs(cowork): …`) and report the sha.
(The types-header design + plan were committed in `e316ff1ab4`; likely nothing new.)

## §1 — The worklist (engravingbridge ADD-TEST branches)
Files + ADD-TEST counts from the triage: `regiontonecollector.cpp` (16), `regiontonecollector.h` (4),
`regiontoneprimitives.cpp` (25), `scoreharvest/metricweights.cpp` (8).
- **Get the exact unhit locations:** grep `cc_union_branch_coverage_report.md` (§5 — the `file:line:col[arm]` list) for
  each of those files.
- **Re-confirm the class at source** (don't trust the triage blindly — you found audit errors before):
  - **ADD-TEST** → reachable real logic → write an oracle test (this cluster's work).
  - **EXCLUDE-DEFENSIVE** → a can't-happen guard (null/bounds/measure-less fallback, upstream-invariant) → **skip; do
    NOT test and do NOT annotate** — the formal exclusion is the **Phase-6 coverage seal**, not now.
  - **DEFER** → the **6 `collectPitchContext` arms in `regiontoneprimitives.cpp`** (legacy builder, retires in Phase 6)
    → **skip.**
- The spec's engravingbridge bullet lists the oracle *themes* (excluded-staff / non-playing / invisible → dropped;
  stressed mid-bar beat → **0.85** weight; dense-start sustain-in vs onset-at-start tallies + distinct-PC dedup;
  sostenuto/soft pedal **excluded** from sustain windows; pedal outside-region / degenerate → no window; same-start
  pedal sort tiebreak on end-tick; chord-track-named / hidden / drumset staff **ineligible**; onset-only vs sustained;
  stepwise-bass to-prev/to-next flags; end-of-score → no forward context). Use as the **starting point** — **derive the
  exact expected value at source.**

## §2 — Write the tests (oracle-asserted)
- For each ADD-TEST branch, drive the input that reaches it and assert the **theory/contract-correct** result, derived
  from the documented contract / music theory — **not** the implementation's output.
- **A correct oracle that fails current code → `DISABLED_`/xfail with a documented expected-vs-actual + flag** (rule 2 —
  a surfaced defect). Do NOT lower the assertion to the wrong value.
- New test file(s) — e.g. `engravingbridge_branch_tests.cpp` (or extend the existing bridge-touching test), registered
  in `tests/CMakeLists.txt`.

## §3 — Gate
- **All new tests pass** (bar documented xfails); `composing_tests` grows by the ADD-TEST count; **`notation_tests` +
  `pipeline_snapshot_tests` unchanged**; corpus **53/24/53 by construction** (tests-only). Build green.
- **Any corpus/snapshot movement → STOP** (a test leaked into production, or it mis-asserts against current behaviour).
- **Re-measure (the round-2 progress check):** re-run the clang branch-coverage runner scoped to `engravingbridge` →
  confirm the targeted branches are now covered, and report the engravingbridge branch% before→after. *(If the coverage
  toolchain is available this session; otherwise note it deferred to the next coverage pass.)*

## §4 — Scope & stops
- **Tests-only.** NO production logic/behaviour change. A gap closable **only** by changing production → STOP and flag
  it (an L4-build item, not a backfill test).
- Do **NOT** test the deferred `collectPitchContext` arms; do **NOT** annotate the exclude-defensive branches (Phase-6).
- `upstream` never; local commit only.

## §5 — Deliver
Commit **locally (unpushed)**: the new test file(s) + the CMake entry. Write `cc_backfill_engravingbridge_report.md`
(gitignored): tests added (per file/branch), any **surfaced defects** (the xfails, expected-vs-actual), the
engravingbridge branch% before→after, and the commit sha — so Cowork verifies by sha that only test files + CMake
changed (no production source).
