# The repository-side re-run of the transposition-equivariance probe (OI-243 / OI-244)

> **2026-08-03 (CC, phase 1o, Task 4).** Read-only on the repository; everything written lives in
> this directory. **No figure is transcribed here** — every quantity is a field of
> `rerun_analysis.json`, cited by path (D-431).

## Why this run exists

`OPEN_ITEMS.md` OI-243 records the 2026-08-02 probe as run by a sub-agent with an agent-written
script, established only by its own self-check and its six bit-exact conditions, and states that
**the row's first action is a repository-side re-run before the finding carries any load (#19)**.
Two family rows — OI-243 and OI-244 — could not bear weight until this ran.

## What was run, and what was changed to run it

The committed apparatus
`tools/joint_estimator/transposition_probe_2026_08_02/run_probe.py` was driven **unchanged**. It
could not run here as it stands because its `REPO` and `OUT` constants are absolute sandbox paths
that exist on no machine in this repository. `rerun_repo_side.py` imports the committed module,
re-points exactly those two constants and the resumability budget, **asserts the three measurement
constants (`SEG_CAP`, `SHIFTS`, `K_TO_F`) equal to the committed values before running**, and
drives the two phases. Everything the driver touched is enumerated in `rerun_record.json` →
`what_the_driver_changed`; anything else differing would have been a stop.

Re-implementing the probe was deliberately not done. It would have produced a second answer to one
question (#6) and would have measured the new script rather than the committed one — which is the
opposite of what the row asks for.

## Order of operations, as the dispatch requires

1. **Establish first.** The twelve sampled pieces must reproduce the committed decode parity
   reference; a failure is a stop and the finding cannot be re-measured with this apparatus.
   Result: `rerun_analysis.json` → `A_reproduction.establishment`.
2. **Predictions registered before measuring** (#17b) — `predictions.md`, written and committed
   before `rerun_repo_side.py` was invoked, and stating explicitly whether reproduction or
   divergence was predicted, and why.
3. **Re-run** over the same pieces and shifts: `transpose_state.json`.
4. **Score** reproduction per condition and per violation identity, and score every registered
   prediction: `rerun_analysis.json` → `A_reproduction`, `predictions_scored`.

## The separation the original run did not make (§4.4)

The dispatch asks how much of the measured non-equivariance is **defensible enharmonic ambiguity**
and how much is **boundary movement and collapse** — the number the family design needs, and one
the original run did not compute. The five classes and the rule for each were registered in
`predictions.md` **before** they were computed and are restated in code in `analyze_rerun.py`, so
the definition and the computation cannot drift apart. Results:
`rerun_analysis.json` → `B_separation_the_dispatch_asked_for`.

The load-bearing definitional choices, stated so they can be argued with:

- **Boundary movement is never defensible.** An engraver's spelling choice can move a label; it
  cannot make the same sounding music divide into different segments.
- **A pruned-away expected reading is never defensible.** If the correctly-shifted state was not in
  the candidate set at all, the decode never weighed it — that is the admission prune (OI-244), not
  a spelling judgment.
- **Only the tritone shift is enharmonically ambiguous.** The probe's declared convention had to
  choose sharpward for +6 and had no choice to make at +2 or −3, so a label flip at those two
  shifts cannot be excused by the spelling frame.

## What this run does not settle

It re-measures; it does not fix, and nothing here designs a remedy. The disposition of OI-243 and
OI-244 belongs to the family design at its own stage, over the whole family at once (`CLAUDE.md`,
the one-fix-per-family rule of 2026-07-28) — and the phase-3 gate is narrowed, not opened
(`tools/audit/phase3_gate_partition.json`).

## Files

| file | what it is |
|---|---|
| `predictions.md` | the predictions, registered before any decode ran |
| `rerun_repo_side.py` | the driver: imports the committed apparatus, re-points two paths, asserts the measurement constants |
| `rerun_record.json` | what the driver changed and what each phase returned |
| `establish_state.json` | phase 1 raw results (written by the committed apparatus) |
| `transpose_state.json` | phase 2 raw results: all conditions, every violation (written by the committed apparatus) |
| `analyze_rerun.py` | the scoring: reproduction against the committed run, and the §4.4 separation |
| `rerun_analysis.json` | every figure this run produced |
