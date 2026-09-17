# CC instruction — the OI-206 investigation: call-path confirmation + the windowed-vs-whole-piece decode measurement (READ-ONLY; the fix decision surface follows)

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md`,
> `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (INDEX), and the three detail files
> this dispatch serves: `open_items/OI-206.md` (the user-reported regression — READ ITS DATED
> NOTES IN FULL: the mechanism is field-established, the 3.1b correction names the recorded
> evidence), `open_items/OI-203.md` (the measured latency figures), `open_items/OI-207.md`
> (the conformance audit that runs after this). Also the recorded evidence this dispatch's
> Task 2 extends: `docs/p3_granularity_ab_3_1b.md` (the 3.1b window-vs-whole A/B on the
> LEGACY analyzer) and `cowork_architecture_review_2026_07.md` §7 (the Tristan scale case).
>
> **What this is:** the investigation BEFORE the OI-206 fix ruling — investigate-by-default.
> NO fix, NO design, NO behavior change anywhere in this dispatch. Two questions: (1) confirm
> the regression's call-path facts at the code; (2) measure, for the JOINT estimator, what the
> 3.1b A/B measured for the legacy analyzer — how decode accuracy and stability depend on the
> analyzed span — so the fix alternatives (keyed cache; off-thread computation; bounded
> grow-until-stable interactive decode) can be rated on numbers, not beliefs.
>
> **Current state:** branch `master`; expected HEAD `7dcfbf2096` (the marginals reference,
> pushed) — verify; mismatch = STOP. Riding Cowork edits: `cowork_handoff.md` AND `STATUS.md`
> *(dated addition, Cowork 2026-07-28: the session-close handover block + the STATUS
> session-close entry were written while this dispatch was in flight — both ride your first
> commit; they are the only expected non-yours tracked diffs)*. This dispatch file stays
> untracked.
>
> **Hard stops:** origin only; NO `src/` production change (test-layer/tools instruments
> only); no golden, corpus, or `tools/robust_stop/` movement; a surprise is a STOP (#13).
> VS Code bash rules on every command.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-28.

**Touchable set:** the test dirs (instrumented confirmation + measurement drivers), NEW
`tools/joint_estimator/gen_window_study.py` + artifacts, `tools/notation_seams/` artifacts,
register index + detail files (dated notes), `STATUS.md`, the riding Cowork file.

---

## Task 1 — the call-path confirmation (the OI-206 mechanism, closed at the code)

Confirm at the code, with citations (a small generated fact table, not prose assertions):

1. Which selection kinds invoke `analyzeHarmonicContextAtTick` (the funnel): single-note
   selection yes; list/range/measure/rest/other-element selections — enumerate each caller
   chain from the selection-changed handling to the funnel, with file:line. The field pattern
   (only single-note is slow; ctrl-click additions instant) must be REPRODUCED by the code
   facts — a mismatch is a finding.
2. Exactly how many `produceNotationRecord` calls one single-note selection event triggers
   (once, or more — the status bar AND accessibility AND anything else each calling?). If
   more than once per event, that multiplier is a headline finding.
3. That the call is synchronous on the UI thread (cite the call chain), and that no
   re-trigger loop exists (the earlier total-freeze presentation was repeated selection
   events, not a loop — confirm).
4. The other record-arm consumers' interactive frequency (annotation emit, implode, tuning —
   user-action-scoped, not per-selection — confirm), so the fix surface knows the note seam
   is the only per-selection payer.

## Task 2 — the windowed-vs-whole-piece decode study (the joint estimator's own numbers)

**The question (the 3.1b transfer question, unmeasured for A):** how do the decode's
committed readings and accuracy depend on the analyzed span — and how fast does a queried
reading STABILIZE as the span grows? This feeds both the accuracy side (does bounding the
span cost correctness?) and the user's recorded grow-until-satisfied design (the stopping
criterion needs a measured stability curve).

New read-only instrument `tools/joint_estimator/gen_window_study.py` (imports the established
decode machinery; embedded-equivalent tables via the committed artifacts):

1. **The stability curve (the headline):** for every covered corpus piece, pick the declared
   query sample (every downbeat). For each query tick t, decode nested spans CENTERED on t
   (span sizes in measures: 4, 8, 16, 32, 64, whole piece — clip at piece bounds; declare
   the exact construction) and record, per span size: the committed (key, class) AT t, the
   §3.3 key-axis gap at t, and whether the reading at t equals the whole-piece decode's
   reading at t. Publish: per span size, the fraction of queries whose reading equals the
   whole-piece reading (duration-weighted and count), and the distribution of the SMALLEST
   span at which the reading becomes stable (equals the whole-piece reading and stops
   changing thereafter) — the measured "how much context does a query actually need" curve.
2. **The accuracy side:** for span sizes 8/16/32/whole, grade the windowed readings at the
   query points against the DCML ground truth on the robust unit's cell basis (root and
   key-local at the queried cells; reuse the established grading substrate import-only) —
   does bounding the span COST ground-truth accuracy, and where (cite the worst pieces;
   expected sensitive class: long modulation spans and pieces whose global context revises
   openings — the desk-sim S2 retroactive-revision shape).
3. **The cost side:** decode wall time per span size (the latency numbers already exist for
   whole-piece; complete the curve).
4. Artifacts (#17f): `window_study.json` (full data) + a short summary; deterministic.
5. **Prediction discipline (#17b), recorded in the artifact BEFORE measuring:** state your
   expected direction per curve (e.g. "stability fraction rises monotonically with span;
   most queries stable well below whole-piece; accuracy at 16 measures within X of
   whole-piece") — a band miss is a reported finding, not silently absorbed.

## Task 3 — dated notes + close

Dated notes on OI-206 (Task-1 facts) and OI-203 (the cost curve completes its figures);
`STATUS.md` entry. Commits per change-class (Task 1; Task 2; notes+doc). Push origin.
**NO fix anywhere — the fix decision surface is Cowork's next step, built on this dispatch's
artifacts + the 3.1b evidence + the Tristan review.**

## Report

Hashes; the Task-1 fact table (callers, call count per event, synchronicity, no-loop, the
field-pattern reproduction); the Task-2 curves' headline numbers (stability fractions per
span; the smallest-stable-span distribution; the accuracy deltas per span; the cost curve)
+ your prediction-vs-measured table; anomalies (a surprise is a STOP). Standing self-check
before reporting.

**After this dispatch:** Cowork presents the OI-206 fix decision surface to the user (the
alternatives — keyed record cache; off-thread computation; bounded grow-until-stable
interactive decode per the user's recorded design, with the measured stopping criterion —
each rated on these numbers against the principles and #4). Then OI-207 (the
decision-conformance audit), then the marginals C++ follow-up.
