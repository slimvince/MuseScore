# CC instruction — post-switch increment 1: the OI-203 latency measurement (read-only) + OI-193, the full-posterior marginals (contract §3.3 group (ii))

> **★ DATED AMENDMENT (Cowork, 2026-07-28, at the Tasks-1/2 verification — the partition is
> ratified; resume at Task 3 with expected HEAD `7dcfbf2096`):** Tasks 1–2 are DELIVERED and
> Cowork-verified at the objects. **The logsumexp parity ruling (CC's flagged risk):** Task
> 3's C++↔Python parity target remains **BIT-IDENTITY FIRST** — the prior establishment
> record says it is likely reachable on this platform (`std::log` == Python `math.log`
> bit-for-bit on 80,961 values, the 2026-07-25 Task-A record; picojson doubles bit-exact;
> Neumaier summation established): implement logsumexp with the SAME operation order as the
> Python reference (same max-subtraction, Neumaier-compensated sums, same exp/log calls). If
> a residual drift nonetheless appears, that is a **STOP-and-characterize** (which operation,
> which pieces, max ULP distance), NOT a self-ratified tolerance — a declared tolerance bar
> would be a protocol choice for Cowork/the user with the mechanism named (the Neumaier
> lesson: exact parity was achievable once the mechanism was found). Everything else in Tasks
> 3–4 stands as written. **Scheduling note: the OI-206 investigation dispatch
> (`cc_instruction_oi206_investigation.md`) runs BEFORE this follow-up** — the live
> interactive regression outranks the marginals' C++ half.

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (lean since the
> switch — header + both entries), `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md`
> (INDEX; this dispatch works rows **OI-203** (measurement half) and **OI-193** (the named
> completion) — read both detail files), `C:\s\MS\cowork_notation_output_contract.md` (§3.3
> group (ii) — THE specification this dispatch delivers — and §5.5's oracle conditions).
>
> **Where the project stands:** the notation switch is executed (`2a81af273e`) — the joint
> estimator's record path is the production notation analysis on the default flag; the batch
> surface has been A's since the OI-178 adoption. This dispatch delivers the FIRST post-switch
> completion: the ratified uncertainty contract's group (ii) — the full forward-backward
> marginals — plus the OI-203 latency measurement (measurement ONLY; the cache design returns
> to Cowork with the numbers).
>
> **Current state:** branch `master`; expected HEAD `2a81af273e` (the switch, pushed) —
> verify; mismatch = STOP. Riding Cowork edit: `cowork_handoff.md` (commit with Task 1).
> This dispatch file stays untracked.
>
> **Hard stops, always:** origin only; NO change to the committed decode/MAP path (the
> marginals are ADDITIVE — the committed segments, scores, corpus, goldens, and
> `tools/robust_stop/` must not move; any diff there is a STOP); no inference-value change of
> any kind; the marginal publication is BLOCKED until its oracle passes (#19 — publishing an
> unestablished marginal is the Class-B defect); no [0,1] calibration claims (model
> probabilities, status-marked); files outside the touchable set; a surprise is a STOP (#13).
> VS Code bash rules on every command.
>
> **Feasibility:** if the marginal work does not fit one session, STOP after any complete,
> committed unit with a partition proposal (the established precedent) — the natural seam is
> Python-reference-first, C++ second.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-27, at the switch verification ("go" on the post-switch
agenda).

**Touchable set:** NEW `tools/joint_estimator/gen_marginals_ref.py` + its artifacts +
extensions to the joint diagnostics in `tools/batch_analyze.cpp` (default-OFF drivers only);
`src/composing/analysis/joint/**` (ADDITIVE marginal computation + record fields; the decode
arithmetic itself untouched); NEW timing instrument code ONLY in the test/tools layer (Task
1); the relevant test dirs + CMake lists; `ARCHITECTURE.md`, `STATUS.md`, register index +
detail files (row notes/flips); the riding Cowork file. **Pinned instruments import-only.
`fit_weights.py`'s lattice forward/backward machinery may be IMPORTED as the reference basis
(carried establishment from the fit arc's logZ checks) — never edited.**

---

## Task 1 — the OI-203 latency MEASUREMENT (read-only; ONE commit; no cache design, no fix)

1. A timing instrument (test-layer or a default-OFF tools driver — no production code) that
   measures, on ≥4 representative scores (small chorale → the largest snapshot fixture, plus
   ≥1 corpus-scale piece loaded through the app harness): (a) one whole-score
   `produceNotationRecord` wall time (cold); (b) the note-seam funnel's per-query wall time as
   the consumers experience it today (which includes the whole-score produce per query); (c)
   the per-query time were the record memoized (produce once, then N `noteView` lookups) — the
   measured bound the cache design will be judged against.
2. Generated artifact (`tools/notation_seams/noteseam_latency.json`, #17f): per score — size
   (measures/notes), the three timings, machine note. A dated measurement note on the OI-203
   detail file (row stays OPEN — the design decision is Cowork's next step with these
   numbers).

## Task 2 — the Python marginals reference (the oracle side)

1. NEW `tools/joint_estimator/gen_marginals_ref.py`: exact forward-backward over the SAME
   pruned decode lattice `decode_piece` explores (same candidate sets, same seg_cap, same
   tables/weights — the marginals are OF the production decode's lattice, stated in the
   artifact), computing per piece: per-event boundary marginal probability; per committed
   segment, the committed key's marginal mass and every candidate key's mass; the committed
   class's mass and every scoreable class's mass (the §3.3 group (ii) fields). Reuse the fit
   arc's lattice machinery by import where it serves (carried establishment); document any
   place the decode lattice and the fit lattice differ (a difference is a finding to state,
   not to paper over).
2. **The pre-declared oracle (contract §5.5 + the OI-193 row — ALL must pass before anything
   is published):** (a) forward logZ == backward logZ per piece (machine tolerance, report the
   max |Δ|); (b) per-span/per-event mass normalization (sums to 1 within machine tolerance);
   (c) synthetic-case agreement with the fit-arc lattice arithmetic (the desk-sim S1 shape at
   hand-computable size — hand-check one case in the report); (d) MAP consistency — the
   committed path's mass is the modal assignment wherever the decode margin is large (report
   the correlation between the §3.3 group (i) gap and the marginal mass — direction must be
   monotone; a violation is a STOP).
3. Artifact `marginals_ref.json` (full precision, the C++ parity oracle) + the oracle-results
   block; deterministic (two runs byte-identical). Commit.

## Task 3 — the C++ marginals on the module + record (ADDITIVE)

1. `computeMarginals(...)` in the joint module beside `computePosteriorSlice` — the same
   lattice, Neumaier-disciplined sums where Python sums; the record gains the group (ii)
   fields per the contract: the masses as SEPARATE named fields beside the group (i) gaps
   (never a redefinition), each carrying establishment status; the ranked-alternatives
   ordering source stamp flips to "marginal mass" ONLY if the contract's re-ordering clause is
   implemented in the same commit with its tests — otherwise ordering stays group-(i)-stamped
   (state which you did).
2. **Parity establishment:** a default-OFF `batch_analyze` driver decodes the committed corpus
   and verifies the C++ marginals against `marginals_ref.json` — bit-identical (the
   established Neumaier pattern); 326 pieces, every field. Any divergence = STOP.
3. **Nothing else moves:** the committed decode (segments/scores) byte-identical (the
   marginal pass must not perturb the decode — prove via the corpus spot-check); suites
   green; goldens untouched (the snapshot serializer does not serialize the new fields unless
   you add a record-arm structural test for them — golden-less, per the standing pattern).
4. Unit tests: normalization, the boundary-marginal shape on a synthetic piece, the
   MAP-consistency direction, the empty/degenerate guards.

## Task 4 — row flips + doc sync

OI-193 INDEX row → ✅ RESOLVED (delivered + oracle-established; dated detail note with the
oracle figures); the contract's §3.3 group (ii) gains a dated "DELIVERED" note (Cowork
authorizes this one contract edit — cite this dispatch); `ARCHITECTURE.md` (the marginal
publication as-built); `STATUS.md` entry. Commits per change-class; push origin.

## Report

Hashes; the Task-1 latency table (the artifact's numbers — no interpretation beyond the
memoization bound); the oracle results (logZ max |Δ|, normalization, the hand-checked
synthetic case, the gap↔mass monotonicity); the parity result (pieces × fields, divergences =
0); the decode-untouched proof; suite totals; reuse-vs-new / what-retires (expected: the fit
arc's lattice machinery reused by import; nothing retires); anomalies (a surprise is a STOP).
Standing self-check before reporting.

**After this unit:** OI-194 (the ornament labels — its own dispatch), the OI-203 cache
decision surface (Cowork, with Task 1's numbers), then the OI-180 retirement-map increments.
