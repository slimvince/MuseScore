# CC Instruction — Stage-5 Phase 2.2d: the (sameRootInversionBonus, kWStepIn) sub-sweep — is there a feasible slice of the family-2 gain?

> **ACTIVE DISPATCH (Cowork, 2026-07-05).** Seventh CC increment of the Stage-5 arc. Premise: the 2.2c
> family-2 closure (`cc_stage5_phase2_2c_report.md` Task 4 + design §15 O-11 ii — read both): the
> coupled candidate is blocked at every swept `bassNoteRootBonus` value, and BOTH blockers are driven by
> the fixed `sameRootInversionBonus 0.475 + kWStepIn 0.125` bump (`bwv379@11520` at fitting;
> `bwv392@17520` at full corpus). **This dispatch asks the one remaining cheap question: does a SMALLER
> (srib, kw) bump exist that keeps a real gain and blocks NOTHING?** Measurement + candidate surface
> only — **no adoption, no committed value change, no corpus write, no push.**
>
> Read first: CLAUDE.md · STATUS.md (top) · design §4.2 (objective/constraints) + §15 O-9/O-11 ·
> the 2.2b/2.2c reports' sweep sections.
>
> **Current state (Cowork-verified 2026-07-05):** HEAD = the 2.2c fold; batch stop 53/24/53; corpus
> `0dd64660f4` byte-identical to the RETIRE-4 binary's output (proven at 2.2c); suites 1101/53/11;
> per-carrier delivery for both levers live (values unchanged). Expected dirty: the Cowork fold files
> (STATUS · COWORK_HANDOFF · design) + known scratch. **Hard stops:** any committed value change; any
> `tools/corpus/` write; sandwich mismatch; any push.
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`.

---

## Task 0 — state check
HEAD, branch, dirty set vs expectation. Report.

## Task 1 — the 2-D sub-sweep (Baroque carrier; fitting split first)

Grid: `sameRootInversionBonus ∈ {0.40, 0.4125, 0.425, 0.4375, 0.45, 0.4625}` ×
`kWStepIn ∈ {0.10, 0.1125, 0.125}` (18 points; the (0.40, 0.10) corner = the current values, the
baseline anchor; the ratified Gate-R search bound `srib > 0.35` holds across the grid).
`bassNoteRootBonus` stays 0.70 everywhere (its own movement is family-2-closed; if the surface
suggests a small bnrb interaction would unlock a point, SAY so in the report — do not sweep it).

Per point (via the driver; every eval ledgered to a committed `tools/fit_ledgers/stage5_2_2d_sweep.jsonl`):
1. Fitting-split (261) objective + §4.2 feasibility (no new class-(b) batch case; class-(b) duration
   non-increase) — **track `bwv379@11520` explicitly** (its first appearance bounds the feasible region).
2. For every fitting-feasible point with gain > 0: **full-corpus Baroque + Default** checks (zero new
   class-(b) anywhere; **track `bwv392@17520` explicitly**; Jazz byte-identical by construction — state
   it, spot-verify once).

## Task 2 — selection + the decision surface (candidate only, if one exists)

Selection rule (the S-3 loop, unchanged): **highest fitting-split gain whose full-corpus checks add
ZERO new class-(b) cases on any carrier.** If a candidate exists:
- held-out (65) scored ONCE; the full surface (root/RN/key ×3 carriers, batch diffs explained with
  class, class-(a)/(b) durations, DLC probe via `run_dlc_baseline --param-override`, snapshot-impact
  preview, D-4 Default eligibility) + the **prepared-not-applied adoption artifact** (incl. the
  kStepBudget recomputation note from O-11/2.2c Task 2 if kw moves).
- If NO grid point passes: the family-2 arc closes fully ("no feasible slice of the coupled gain
  exists at this grid resolution") — report the surface with the blocking case per point; that closure
  is itself the deliverable.

## Task 3 — sandwich + report + fold
1. Sandwich ×3 on the REAL dirs = 53/24/53 set-diff empty; corpus byte-untouched; suites green.
2. Report `cc_stage5_phase2_2d_report.md` (force-add, own commit): the 18-point surface (every number's
   denominator named; the two tracked cases' appearance map), the selection (or the closure), the
   decision surface, reuse-vs-new + retires (expected: nothing), all SHAs.
3. Fold (`docs(cowork):`, exact list): `STATUS.md` (22s) · `COWORK_HANDOFF.md` ·
   `cowork_stage5_fitter_design.md` (the O-11 record) · `cc_instruction_stage5_phase2_2d.md` (force-add).

## STOP conditions
- Any committed value change; any adoption; any corpus write; any push.
- Sandwich mismatch; suite regression.
- Cost >4× (~50 s/fitting eval; the grid ≈ 18 fitting evals + a handful of full surfaces ≈ within the hour).
- A grid point whose feasibility cannot be determined cleanly (report it, continue the rest).

## Acceptance
18-point ledgered surface with the two tracked cases mapped ✓ · selection per the rule (or the honest
full closure) ✓ · candidate surface + prepared-not-applied artifact (if any) ✓ · sandwich + suites ✓ ·
report + fold with SHAs ✓.
