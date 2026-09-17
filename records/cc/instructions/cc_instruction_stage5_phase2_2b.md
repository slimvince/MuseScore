# CC Instruction — Stage-5 Phase 2.2b: verdict evidence completion + the JOINT FIT — candidates + PREPARED verdicts, nothing adopted or retired

> **ACTIVE DISPATCH (Cowork, 2026-07-05).** Fifth CC increment of the Stage-5 arc, on the 2.2a audit
> table (`cc_stage5_phase2_2a_report.md` — read in full; it is this dispatch's premise set). Design:
> §4.4 family 2 + D-7 (per-rule audited verdicts) + §4.2 (objective/constraints) + O-7 (the parked
> family-1 lever re-enters here). **THE CENTRAL RULE: this dispatch produces per-rule VERDICT PROPOSALS
> and fit CANDIDATES with full decision surfaces. NO rule is retired, NO value is adopted, NO committed
> constant changes. Every verdict and every adoption is a separate user-ratified event on this report.**
>
> Read first: CLAUDE.md · STATUS.md (top) · BUILD_AND_TEST.md · docs/scoring_model.md §4/§6 ·
> design §4.2/§4.4/D-7/O-7 · `cc_stage5_phase2_2a_report.md` · `cc_stage5_phase2_1_report.md`.
>
> **Current state (Cowork-verified 2026-07-05):** batch stop 53/24/53; corpus `0dd64660f4` 352×3;
> suites 1116/53/11; the disable mechanism + audit ledgers live. Expected dirty: the Cowork fold files
> (STATUS · COWORK_HANDOFF · design · **`cowork_style_taxonomy_proposal.md` — the §6/§6a preset-layer
> record, a KNOWN Cowork concurrent edit from session 22o, now in your fold list**) + the known
> deliberately-untracked scratch. **Hard stops:** any committed constant/rule change; any write under
> `tools/corpus/`; sandwich mismatch; any push.
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`.

---

## Task 0 — state check
HEAD, branch, dirty set vs expectation (note the taxonomy file is EXPECTED dirty). Report.

## Task 1 — verdict evidence completion (read-only; closes the 2.2a scope caveats)

The 2.2a classifications are fitting-split/Baroque-only. Before any verdict proposal:

1. **Cross-carrier, full-corpus disable table:** each of the 14 rules disabled alone, evaluated
   FULL-corpus on ALL THREE carriers (42 evaluations ≈ 35–55 min — budgeted): root/RN/key deltas,
   batch-stop set diff (explained per case with class), class-(b)/(a) duration deltas. This catches a
   rule inert on the Baroque fitting split but live elsewhere — and note the structural expectation:
   Gates A/E/H sit behind `preferMinorOverMajorAdd6`, which is FALSE on Jazz/Default presets, so their
   Default/Jazz rows should be structurally zero; confirm rather than assume.
2. **Firing-site extraction (no new telemetry):** per rule, diff the full-corpus regen (rule off vs on)
   — the differing cells ARE the rule's effective sites. Per rule: site count + the site list
   (stem@tick, our-root-on vs our-root-off vs WiR root where covered) → committed ledger
   `tools/fit_ledgers/stage5_rule_firing_sites.jsonl`.
3. **Founding-case check:** for each rule, locate its `docs/scoring_model.md` §6 "why it exists"
   case(s) (e.g. Gate K: bwv40.6 m6; Gate L: bwv144.6, bwv245.15; Gate J: the {R−4,R,R+3,R+6} class)
   and state whether the rule still changes that case today (per the Task-1.2 diff). A founding case
   the rule no longer touches is itself evidence (something upstream absorbed the fix — name what, if
   the diff makes it visible; do not guess).
4. **The Gate-J per-case table (the root-vs-RN tension, mechanical part):** at every Gate-J firing site
   with WiR coverage: our root with J on / off · WiR root · WiR RN label (viio-family vs V-family) ·
   duration. Deliverable: the counts — at how many sites/ticks does WiR side with the vii° root vs the
   V7 root? (The musical adjudication of samples is Cowork/user work on this table; you produce the
   mechanical comparison only.) Same table, smaller, for BiasCorrection/GateE/GateH sites.
5. **DLC generalization probe (validation-only use; read-only):** via `run_dlc_baseline.py
   --param-override` on 2–3 DLC styles (state which; e.g. corelli + mozart + a romantic set): baseline
   vs (a) the inert-7 disabled, (b) GateJ disabled. Per-style root-agree deltas reported. NC data —
   QA only, shapes no value.

## Task 2 — the JOINT FIT (the P1-ratified staging step 2; fitting split; candidates only)

Coordinate/pattern search over the coupled continuous cluster, under THREE declared rule
configurations (the dissolution×fit coupling made explicit):
- **Config I — all rules enabled** (the conservative fit).
- **Config II — the 2.2a inert-7 disabled** (GateA/F/GB/GC/GD/K/L off; only if Task 1.1 confirms them
  cross-carrier-inert — a rule live elsewhere drops out of the disabled set, stated).
- **Config III — Config II + the 4 disable-beneficial off** (BiasCorrection/GateE/GateH/GateJ off) —
  the maximal-dissolution candidate; run LAST, and only if Config II is healthy.

**The cluster (rows):** `kRootToneFactor` · `kSecondToneFactor` · `sameRootInversionBonus` ·
`bassNoteRootBonus` · `tpcConsistencyBonusPerTone` · `rootContinuityBonus` · `kWStepIn` (+ its kWStepOut
pair if the sweep shows them coupled) · `kPowerChord3PcPenalty` (re-entering per O-7). Constraints per
design §4.2 on every evaluation (fitting split; no new class-(b) batch case; class-(b) duration
non-increase; the Gate-R invariant `sameRootInversionBonus > kNonBassPenalty` enforced as a search
bound). Search: coordinate sweeps (5 steps/row from the 1b step policy, then halved-step refinement on
movers), max TWO full rounds per config; **budget cap ~6 h total fit time — STOP and report partials
beyond it.** Every evaluation ledgered.

## Task 3 — the decision surface: candidates + PREPARED per-rule verdicts

1. **Per config:** the best feasible vector; held-out (65) scored ONCE per candidate; full-corpus ×3
   carriers (root/RN/key, batch diffs explained, class durations); D-4 Default eligibility; Jazz
   regression spot-check; DLC probe on the winning config (Task 1.5 machinery); snapshot-impact preview.
2. **Per-rule VERDICT PROPOSALS (D-7), each with its evidence refs:** retire (inert everywhere + fixtures
   reproduced-or-vacated under the candidate weights, with the fixture disposition stated) /
   retain-as-structural (load-bearing correction the fit does not reproduce) / defer (named blocking
   interaction). The Gate-J and BiasCorrection proposals must cite the Task-1.4 per-case tables, not
   aggregates. **Proposals only — the user rules on each.**
3. **Prepared artifacts, not applied:** the adoption commit description per candidate config (values +
   rule removals + doc-sync + golden-refresh scope), and the per-rule retirement commit shapes.

## Task 4 — sandwich + suites + report + fold
1. Sandwich ×3 = 53/24/53 set-diff empty; corpus byte-untouched; suites green, no golden refresh.
2. Report `cc_stage5_phase2_2b_report.md` (force-add, own commit): Tasks 1–3 complete with every
   denominator named; reuse-vs-new + retires (retires NOTHING in this dispatch); all SHAs.
3. Fold (`docs(cowork):`, exact list): STATUS.md (22p) · COWORK_HANDOFF.md ·
   `cowork_stage5_fitter_design.md` · `cowork_style_taxonomy_proposal.md` (the §6/§6a Cowork record) ·
   `cc_instruction_stage5_phase2_2b.md` (force-add).

## STOP conditions
- Any committed constant/rule change; any adoption/retirement.
- Config II/III: a disabled-rule configuration whose BEST candidate cannot satisfy the constraints —
  that config's honest result is "dissolution not reproducible by these weights"; report, do not relax.
- Fit budget >~6 h; any single evaluation >4× ~50 s; sandwich mismatch; suite regression.
- A firing-site diff that cannot be attributed cleanly to the disabled rule (report the ambiguity).

## Acceptance
Cross-carrier disable table (14×3) ✓ · firing-site ledger committed ✓ · founding-case dispositions ✓ ·
the Gate-J/Bias per-case tables ✓ · DLC probes ✓ · three-config joint fit ledgered within budget ✓ ·
per-rule verdict PROPOSALS with evidence refs ✓ · prepared-not-applied artifacts ✓ · sandwich + suites ✓ ·
report + fold with SHAs ✓.
