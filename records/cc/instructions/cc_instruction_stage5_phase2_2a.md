# CC Instruction — Stage-5 Phase 2.2a: housekeeping + the rule-disable mechanism + the §6-block dissolution AUDIT (measurement only)

> **ACTIVE DISPATCH (Cowork, 2026-07-05).** Fourth CC increment of the Stage-5 fitter arc. Per the SIGNED
> design (`cowork_stage5_fitter_design.md`) §4.4 family 2 and the P1-ratified staging, the family-2 joint
> fit needs an evidence base first (measure → decide → build): **this dispatch builds the rule-disable
> mechanism and runs the per-rule dissolution audit at CURRENT weights. The joint fit itself is the NEXT
> dispatch (2.2b), on this dispatch's evidence. NOTHING is adopted; no committed constant value changes;
> no rule is retired here.** Also carries the two P2.1-ruled housekeeping fixes (design §15 O-8) and the
> fold (the parked-candidate narrative).
>
> Read first: `C:\s\MS\CLAUDE.md` · `C:\s\MS\STATUS.md` (top) · `C:\s\MS\BUILD_AND_TEST.md` ·
> `C:\s\MS\docs\scoring_model.md` IN FULL (§6 is this dispatch's subject) · design §4.4/D-7 + §15 O-7/O-8 ·
> `cc_stage5_phase2_1_report.md` (the parked candidate; its ledger note).
>
> **Current state (Cowork-verified 2026-07-05):** batch stop 53/24/53; corpus 352/352 ×3 (`0dd64660f4`);
> suites composing 1096 / notation 53 / snapshots 11; the override mechanism + driver live (Phase 1);
> the family-1 candidate PARKED (no value change — O-7). Expected dirty: the Cowork fold files (STATUS ·
> COWORK_HANDOFF · `cowork_stage5_fitter_design.md` · `cowork_layer4_chordsymbol_design.md`) + the known
> deliberately-untracked scratch. **Hard stops:** any behavior change with all flags absent (byte-identity
> is the acceptance); any committed constant/rule change; any write under `tools/corpus/`; sandwich
> mismatch; any push.
>
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`.

---

## Task 0 — state check
HEAD, branch, dirty set vs expectation. Report.

## Task 1 — housekeeping (O-8), two additive fixes
1. **Fit ledgers become committed artifacts:** the driver's per-run ledger output moves to
   `tools/fit_ledgers/` (verify NOT gitignored; if a rule covers it, adjust the DRIVER PATH, never
   .gitignore). The compact per-run ledgers are committed from now on; large per-cell enumerations stay
   regenerable scratch (design §7 as amended by O-8). If the Phase-2.1 ledger files still exist in
   scratch, commit them under the new path as the family-1 record; if not, note regenerability (driver +
   report pin them) — do NOT re-run the 14 evaluations just to recreate files.
2. **S-5 candidate-scoring capability:** add `--param-override <file>` to ONE existing per-style
   validation runner — pick the one that already computes per-style DCML root-agree over the DLC clones
   with the least change (state the choice + rationale). Additive; **default byte-identical** (run
   without the flag before/after the change on one style — outputs byte-identical); with the flag +
   an identity file — byte-identical again; with one perturbed value — output differs (live). No new
   comparison logic.

## Task 2 — the rule-disable mechanism (the same safety class as A-6; flag-gated, byte-identical absent)
Extend the EXISTING override-file grammar (paramoverride) with rule-disable entries for the §6-block:
`disable_rule <Name>` (or a boolean namespace — your call, state it), reaching EACH member of the
`docs/scoring_model.md` §6 post-scoring block INDIVIDUALLY: the bias correction · FM2 · Gate A · E · F ·
G-E · G-B · G-C · G-D · H · I · K · L · J. Requirements:
- Absent ⇒ byte-identical (proof: full-corpus regen ×3 vs frozen corpus, 0 diffs — the Phase-1 discipline).
- An identity override file with zero disables ⇒ byte-identical again.
- Each disable is a clean skip of that rule's block (no logic restructuring — R9 stays parked; if a rule
  cannot be skipped without restructuring, e.g. shared state with a neighbour rule, STOP for that rule
  and report the coupling — do not improvise).
- Unit tests: each name known; unknown rejected; disabled rule provably not firing on a fixture that
  otherwise fires it.
- Doc-sync same commit: a one-line scoring_model §6 note (rules individually disable-able via the
  override file, measurement-only, default absent).

## Task 3 — the per-rule dissolution AUDIT at current weights (measurement only; the 2.2b evidence base)
For EACH rule above, ONE evaluation with that rule alone disabled (current weights; Baroque carrier;
fitting split 261; via the driver — ledger every run under `tools/fit_ledgers/`):
1. **Objective delta** (variant-(b) root-agree duration, fitting split) + RN/key tracked.
2. **Batch-stop subset diff** (fitting-split scores) — every change explained per case with its two-tier
   class (expected small; the 1b screen says the G7 margins are inert at ±step, but disabling a RULE is
   not perturbing its margin — this is the measurement that separates the two).
3. **Pinned-fixture replay:** identify the rule's pinned tests (Stage-1.1 / `postscoringgates_tests.cpp`
   et al. — name them per rule in the report); run them with the rule disabled; record pass/fail per
   fixture. A rule with NO identifiable pinned test is itself a finding (report it; do not invent tests
   in this dispatch).
4. If an existing diagnostic already counts rule firings, record firing counts; if none exists, note it —
   do NOT build new telemetry here.

**Deliverable: the per-rule audit table** — for each rule: objective Δ · batch diff (explained) ·
fixtures pass/fail · firing info (if available) · a PROVISIONAL classification: (a) disable-inert at
current weights (retirement candidate — 2.2b tests whether fitted weights reproduce its fixtures),
(b) disable-harmful (its corrections are load-bearing — joint-fit subject), (c) coupled/unresolvable
(the Task-2 STOP class). **No verdict is issued here** — verdicts are 2.2b's, per D-7, each its own
audited retirement with user ratification.

## Task 4 — sandwich + suites + report + fold
1. End-of-run sandwich ×3 = 53/24/53 set-diff empty; corpus byte-untouched; suites green, no golden
   refresh (all-flags-absent binary).
2. Report `cc_stage5_phase2_2a_report.md` (force-add, own commit): the mechanism + proofs; the
   housekeeping proofs; the full per-rule audit table with every number's denominator named;
   reuse-vs-new + retires (expected: retires NOTHING yet — this dispatch produces the evidence for
   retirements, not retirements); all SHAs.
3. Fold (`docs(cowork):`, exact list): `STATUS.md` (22o) · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md`
   (O-7/O-8 + the §4.1/§4.3 P-markers) · `cowork_layer4_chordsymbol_design.md` (O4 — the power-chord
   admissibility record) · `cc_instruction_stage5_phase2_2a.md` (force-add).

## STOP conditions
- Byte-identity failure at any proof.
- A rule that cannot be cleanly skipped (report the coupling per rule; continue with the others; >3 such
  rules = stop the audit and report).
- Sandwich mismatch; suite regression; cost >4× (~50 s/eval × ~14 rule evals ≈ 12 min expected).
- Anything that would adopt, retire, or change a committed value.

## Acceptance
Ledger path committed ✓ · S-5 runner override-capable with proofs ✓ · rule-disable mechanism proven
byte-identical absent ✓ · the 14-rule audit table complete with explained diffs + fixture replays ✓ ·
sandwich + suites ✓ · report + fold with SHAs ✓.
