# CC Instruction — Phase 5c Step-M follow-up: the universal foreign-tone precondition + re-measure (L5 §5.6, dormant)

> **Two tasks, both dormant + byte-identical on production. (A)** Close the `V/iv`-on-tonic over-trigger by making the
> §5.6 foreign-tone guard a **universal precondition** — Cowork ruling: this is **algorithmic completion** of the guard
> the spec already specifies as universal, **not** a Phase-B inference fix. **(B)** Re-run the Step-M measurement to
> confirm the 31 false labels are gone and the engage delta is still clean. Spec: `cowork_layer5_function_design.md` §5.6
> (amended 2026-06-29 — the universal-precondition bullet). **Default constants (firewall) — this is a structural guard
> placement, no constant changes. Reuse, do not duplicate. Proportionality.** *(Reminder: the never-bash rule is Cowork's.)*

## §0 — The ruling (why this is completion, not tuning)
§5.6 specifies the foreign-tone test as the **necessary condition for every applied label** ("the trigger's necessary
condition AND its false-positive guard"). The implementation applies it only to the **broadened** path; the **subsumed
`tonicizationlabeler`'s** output bypasses it and returns before the guard runs, so a fully-diatonic `I` before `iv` emits
a false `V/iv` (12/6/13 cases, root-neutral). Making the guard gate the labeler's output too is **completing the guard to
its specified universal coverage** — spec conformance, not accuracy tuning. It therefore lands **now, before any engage**,
not in Phase B.

## §1 — PART A: make the foreign-tone guard a universal precondition (`function/functionrelationallabel.cpp`, `emitAppliedLabel`)
- **Move the foreign-tone test to the emitter's first precondition** — evaluated **before** the `tonicizationlabeler` call
  and before the broadened path. If the chord is **fully diatonic** to the home key (no foreign tone), `emitAppliedLabel`
  returns role None immediately, so **no path** (labeler or broadened) can emit an applied label for it.
- **Equivalent acceptable form:** route the labeler's returned label through the same foreign-tone guard. Either way the
  invariant is: **a fully-diatonic chord never yields an applied label, by any route.** Pick the placement that keeps the
  one guard expression (reuse `diatonicMaskFromFifths` — no second test).
- **Do not change the guard's content or any constant** — only its *placement/coverage*. The legitimate applied labels
  (`V/V`, `V7/IV`, `viio/IV` — all carry a foreign tone) are unaffected; only the diatonic over-trigger is removed.
- **The §5.6 doc amendment (the universal-precondition bullet) rides in this same commit** (the sync rule).

### Part A tests
- The 12/6/13 `I→iv` cases (e.g. Baroque `bwv26.6@11040`, `bwv279@3360`, `bwv301@3840`) now emit the **diatonic numeral**
  (`I`), **not** `V/iv`. The legitimate applied labels (`V/V`, `V7/V`, `viiø7/V`, `V7/IV`, `viio/IV`, `viio7/IV`) still
  emit. The diatonic-guard cases (`bVII7→III`, `ii°→III`) still stay not-applied.

## §2 — PART B: re-run the Step-M measurement (read-only, no production movement)
- Re-run `batch_analyze --dump-l5` + `tools/cc_stepM_l5_measure.py` over all three presets (Baroque / Jazz / Default).
- Confirm: the `V/iv` over-trigger count is now **0 / 0 / 0**; the class-(b) and class-(a) deltas remain **0** (still
  additive — root-neutral); the BIR identity sets remain **53 / 24 / 53**; the RN-agree-vs-DCML improvement is **≥** the
  prior +2.48 / +1.91 / +2.32 (it should rise, the 31 false labels removed).
- Re-confirm the only remaining enumerated regression class is the **tonicization-vs-modulation residual** (the §5.4
  companion's target — deferred, not engaged here). Report its per-preset count + identities, since that residual is the
  known trade the L5-relational engage carries.

## §3 — Gate (both parts — byte-identical on production)
- corpus **53/24/53** unchanged (identity sets identical), `composing` / `notation` / `pipeline_snapshot` green, no golden
  refresh — the harness and the emitter are dormant (no production consumer; re-confirm the grep). **Any production
  movement → STOP.**

## §4 — Deliver
Commit **locally (unpushed)**: Part A (the guard placement + Part-A tests + the §5.6 doc amendment, one commit — sync
rule). Part B is measurement only (the harness already exists; no code change unless the script needs a trivial re-run).
Write `cc_phase5c_stepM_followup_report.md` (gitignored): the Part-A change + tests, the Part-B re-measured table (the
0/0/0 over-trigger, the deltas, the new RN-agree numbers, the tonicization-vs-modulation residual identities), the §3
gate, and the shas — so Cowork verifies the over-trigger is closed, the engage delta is clean, and production is
byte-identical.

**This closes L5's algorithmic completion. The next move is the L5-relational engage ratification** (the measured engage
on the legacy substrate — Cowork verifies the re-measure, the user ratifies the production switch). Do **not** engage in
this task.

## §5 — Stops
- The guard-placement change moves any production output, or removes a *legitimate* applied label (a foreign-tone-bearing
  applied chord) → STOP, report. Any constant change, any threshold tuning, building the §5.4 companion engage or the L5
  production switch → STOP (those are the next, separately-ratified steps). `upstream` → STOP.
