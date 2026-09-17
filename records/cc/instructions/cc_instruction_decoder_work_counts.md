# ⛔ WITHDRAWN — NEVER HANDED TO CC. DO NOT EXECUTE.

> **Withdrawn by Cowork 2026-07-28, before hand-off, at the user's challenge.** It was written by
> chasing the most recent finding rather than by asking where that finding belongs in the ratified
> plan — the recency-driven behaviour the user warns against. Its subject (the C++-slower-than-
> Python anomaly and the near-quadratic fact extraction) is **OI-199's** subject matter, so a
> bespoke dispatch would duplicate the ratified review (#6 at the process level). The live
> dispatch is `cc_instruction_oi199_pass1.md`, which seals these findings until after its freeze
> commit so the blind pass's discovery of them is evidence about the method.
>
> Retained for provenance only. Its §counters design may be reused if OI-199 pass 1 misses the
> anomaly and a targeted follow-up is later ratified.

---

# (withdrawn) CC instruction — the decoder work-count comparison: is the C++ decoder doing MORE work than the Python reference, or the SAME work slower?

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md`,
> `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\OPEN_ITEMS.md` (INDEX), and the detail files this
> dispatch serves: `open_items/OI-215.md` (the empty-decode cliff — context, NOT this
> dispatch's subject), `open_items/OI-203.md` and `open_items/OI-206.md` (the latency and the
> interactive regression), `open_items/OI-110.md` (**the ratified precedent this dispatch
> follows: a default-OFF counting instrument placed temporarily in a production translation
> unit, used, then REVERTED, kept in history for a one-cherry-pick re-add**).
>
> **The finding that prompts this (Cowork, verified at the committed artifacts, 2026-07-28).**
> The C++ decoder appears to be **slower than the pure-Python reference decoder on comparable
> input**. `large_score_decode_profile.json`: `bach_chorale_001`, 80 events, phase-3 decode
> **5,650 ms**. `window_study.json` cost curve, memoization OFF: Python reference, mean **3,415
> ms** at mean **77.7 events**. At the other end, brandenburg4 at 1,976 events costs 106.7 s in
> C++ where the Python figures extrapolate to roughly 87 s. A compiled semi-Markov dynamic
> program should beat pure Python by one to two orders of magnitude, not lose to it. **The
> cheapest explanation is already excluded:** the build is `RelWithDebInfo` with `/O2 /Ob1
> /DNDEBUG` — optimized, not a debug build (verified in `ninja_build_rel/CMakeCache.txt`).
> Under #3 this is a **surprise**, and under #18 no design may rest on an unchecked causal claim
> about it.
>
> **The question, and why counting beats timing.** Two worlds are possible and they have
> different remedies: **(A) the same work, slower** — a constant-factor implementation problem;
> or **(B) more work** — the two implementations diverge algorithmically despite producing
> byte-identical output, which would mean the decode-parity establishment (#19) proved outputs
> equal while the work performed differed, and that is the more serious finding. **Counts
> separate A from B; timings cannot.** This dispatch counts.
>
> **Current state:** branch `master`; expected HEAD `5135764ed7` — verify; mismatch = STOP.
> Riding Cowork edits: `cowork_handoff.md` and `STATUS.md` ride your first commit. This dispatch
> file stays untracked.
>
> **Hard stops:** origin only; no golden, no `tools/corpus/`, no `tools/robust_stop/` movement;
> **no inference change of any kind — no gate, no threshold, no vocabulary, no segCap, no
> weights**; **no fix for OI-215** (that is a decision surface Cowork is preparing, not a
> dispatch). A surprise is a STOP (#13). VS Code bash rules on every command.
>
> **The one authorized production touch, and its mandatory disposition.** Counting requires
> counters inside `src/composing/analysis/joint/`. CLAUDE.md pre-authorizes edits under
> `src/composing/`, and OI-110 is the ratified pattern: the instrument is **compile-time or
> runtime default-OFF**, adds **zero work and zero behavior change when off**, is proven
> byte-identical with it off (both suites + pipeline snapshots + a corpus regen), and is
> **REVERTED in its own commit at the end of this dispatch**, its hash recorded so it can be
> cherry-picked back. It does not stay in the tree.
>
> **No mid-flight steering:** self-sufficient; anything uncovered waits for the report.

**Dispatch author:** Cowork, 2026-07-28.

**Touchable set:** `src/composing/analysis/joint/` (the default-OFF counters only, reverted at
close); the test dirs (drivers); `tools/joint_estimator/` and `tools/notation_seams/`
(instruments and artifacts); the register INDEX and detail files; `STATUS.md`; the riding
Cowork files.

---

## Task 0 — the rows this dispatch owes

Assign next free IDs; run the living register check; report the mapping.

1. **The C++-slower-than-Python anomaly** — the finding above, with its figures, the excluded
   build-configuration explanation, and the two candidate worlds. Status OPEN, this dispatch's
   subject. Cross-reference OI-203, OI-206, OI-209.
2. **`buildAdapterFacts` is super-linear in events** — the committed scaling law fits
   `events^1.80` (95% CI 1.65–2.09, R²=0.965, n=27), i.e. **fact extraction is near-quadratic in
   the size of its own input**, costing 16.8 s on the largest score before any analysis begins.
   Extraction should be near-linear; a quadratic where linear is expected is a surprise (#3) and
   was reported in the cost profile as a scaling fact rather than flagged as one. Status OPEN;
   Task 2 below establishes its cause.
3. **A correction of record to the cost-profile report** — its conclusion that *"the coupled DP
   dominates and is not reusable across windows, so incremental patching saves ≤40%"* **does not
   follow from what was measured**. The 40.5/59.5 split is the cost share of a **cold whole-piece
   decode**; it does not establish that an edit forces the dynamic program to be recomputed in
   full. Whether this semi-Markov recursion admits a bounded local re-solve, carrying boundary
   conditions from the unchanged prefix and suffix, is a separate algorithmic question that
   nothing has measured. **Incremental patching is UNMEASURED, not refuted** — record it that
   way so no later design cites the refutation. (Also record the second, unstated caveat: the
   split is Python-derived, and Python-to-C++ transfer of a cost *fraction* is not automatic,
   least of all given the anomaly above.)
4. **A declared process finding** — the analysis-cost dispatch required pre-registered
   prediction bands per task (#17b) in two places; none of CC's own were registered before
   measuring. CC surfaced this honestly in its report. The measurements stand (objective,
   generated artifacts, #17f); what was lost is the guard against motivated interpretation, and
   row 3 above is an instance of exactly the interpretation error that guard exists to catch.
   Status: recorded, standing reminder — every future dispatch registers its bands in the
   artifact **before** the measuring run.

## Task 1 — the work-count comparison (the discriminator)

**Predictions first (#17b), recorded in the artifact before the measuring run.** State, with
bands: which world you expect (A same-work-slower, or B more-work), and your expected ratio of
C++ to Python content-score evaluations. No prediction, no run.

Add default-OFF counters to the joint decoder (OI-110 pattern) recording, per `decodePiece`
call:

- `candidateStates` invocations, and candidate tuples produced;
- `segmentContentScore` (or `content(...)`) evaluations — the innermost unit;
- candidates rejected by each of the three filters separately: root-present, member-overlap
  (`present < min(2, |mem|)`), and fit;
- `candidateKeys` invocations and keys kept after the top-K prune;
- dynamic-programming state insertions and updates, and the number of distinct states held per
  boundary;
- **`std::string` constructions on the decode path**, if obtainable without distorting the
  measurement — the class key, `backEnc`, and the state encoding are `std::string` in the
  innermost loops, which is Cowork's named hypothesis for world A and must be checked, not
  assumed.

Add the equivalent counters to the pinned Python reference decoder (`probe_decoder.py`),
counting the same units.

Run both on the **same pieces**: `bach_chorale_001` and at least four further chorales from the
109-piece sampled set, plus one mid-size score both can complete. Publish per piece and in
aggregate: each count for both implementations, their ratio, and the wall time beside them.

**The verdict this task must state plainly.** If the counts match within a small factor and the
times do not, it is **world A** — a constant-factor implementation problem, and the counters
say where. If C++ performs materially more evaluations, it is **world B**, and that is a
**STOP** to be reported, not investigated further here: it would mean the decode-parity
establishment proved equal outputs over unequal work, which bears on #19 and on every figure the
parity underwrites.

## Task 2 — why fact extraction is super-linear

*Predictions first, as above.*

Establish the cause of `buildAdapterFacts` scaling as `events^1.80`. Counters, not timers:
per call, the number of passes over the note collection, the number of note-to-event
assignments, any repeated scan of the full note list per event or per staff, and any container
whose lookup is linear inside a per-event loop. Report the mechanism with file:line, and the
measured count growth against event count on the committed large-score set.

**Do not fix it.** Name the mechanism; the remedy is a later, separately ratified step.

## Task 3 — artifacts, counters reverted, close

Artifacts: `tools/joint_estimator/decoder_work_counts.json` (per piece, both implementations,
all counts, ratios, times, and the recorded predictions with their verdicts) and a short
summary; deterministic; #17f — every figure in the report comes from the artifact, none typed
by hand.

**Then revert the counters in their own final commit**, prove the tree byte-identical to
`5135764ed7` for `src/`, re-run both suites and the pipeline snapshots green, and record the
reverted commit's hash in the row so it can be cherry-picked back (the OI-110 disposition).

Dated notes on the rows; `STATUS.md` entry. Commits per change-class. Push origin.

## Report

Hashes per commit, including the revert. The prediction-versus-measured table with your bands
registered before the run. The per-piece and aggregate count table for both implementations with
ratios. **The plain verdict: world A or world B**, and if A, which counter localizes the cost.
The Task-2 mechanism with file:line and its count-growth evidence. The byte-identity proof for
the revert. Anomalies each diagnosed — a surprise is a STOP.

Standing self-check before reporting: re-read the actual diff of every touched file against the
guiding principles, the conventions, the gate policies, and `DEFECT_TYPES.md`.

**After this dispatch:** Cowork presents the OI-215 decision surface (the empty-decode cliff —
which outranks this work under the user's stated rule that correctness precedes performance
compromise), and, on this dispatch's verdict, either a constant-factor remedy plan or the
world-B stop. Then the analysis-extent decision surface, then OI-207.
