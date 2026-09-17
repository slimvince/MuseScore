# CC Instruction — Stage-5 Phase 2.2c: execute the ratified RETIRE-5 · per-carrier scoping (O-9) · candidate re-selection under the full-corpus stop

> **ACTIVE DISPATCH (Cowork, 2026-07-05).** Sixth CC increment of the Stage-5 arc. Premises: the 2.2b
> report (`cc_stage5_phase2_2b_report.md`, read in full) + **the user ratifications of 2026-07-05**:
> (1) **all 14 rule verdicts as proposed** — RETIRE {GateA, GateF, GateGB, GateGC, GateK} · RETAIN
> {GateI, FM2, GateJ, GateL} · DEFER {BiasCorrection, GateE, GateH, GateGD, GateGE}; (2) **the O-9
> resolution** (design §15 O-9): per-carrier scoping for the diverging shared levers + candidate
> re-selection. **The retirements ARE executed here (ratified). The re-selected fit candidate is
> PREPARED ONLY — its adoption is still a separate user event.** No fitted value ships in this dispatch.
>
> Read first: CLAUDE.md · STATUS.md (top) · BUILD_AND_TEST.md · docs/scoring_model.md §4/§6 · design
> §4.2/D-7/D-10/O-9 · `cc_stage5_phase2_2b_report.md` §3.
>
> **Current state (Cowork-verified 2026-07-05):** batch stop 53/24/53; corpus `0dd64660f4` 352×3; suites
> 1116/53/11. Expected dirty: the Cowork fold files (STATUS · COWORK_HANDOFF · design — the O-9/§14
> negative-transfer records) + known scratch. **Hard stops:** any FIT-value adoption; any write under
> `tools/corpus/`; sandwich mismatch (post-retirement — see Task 1's special note); any push.
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`.

---

## Task 0 — state check
HEAD, branch, dirty set vs expectation. Report.

## Task 1 — execute the RETIRE-5 (ratified; FIVE separate commits, each revertible)

For each of **GateA, GateF, GateGB, GateGC, GateK**, its own commit (`refactor(composing):`):
1. Delete the rule's block in `postscoringgates.cpp`; remove its `PostScoringRule` enum member +
   `ruleOff` guard + name-map entry; vacate its synthetic fixtures in `postscoringgates_tests.cpp` and
   the rule's `PostScoringRuleDisable` test (they exercise a never-firing path — the 2.2b evidence);
   `docs/scoring_model.md` §6 sync in the same commit (row moved to a "retired (Stage 5, 2026-07-05)"
   note with the evidence ref, not silently deleted).
2. **Byte-identity proof per retirement:** the rule fires on ZERO corpus cells (2.2b firing-site ledger),
   so its removal must be corpus-byte-identical — prove it: full-corpus regen ×3 vs frozen = 0 diffs
   after EACH retirement commit (or after the five as a batch with one proof ×3, stating which; the
   per-commit differential then cites the batch proof). **A non-byte-identical retirement = STOP**
   (the evidence was wrong; revert that commit, report).
3. Suites after the five: composing count DROPS by the vacated fixtures (state old→new count); notation/
   snapshots unchanged, no golden refresh.

Also in ONE `docs:` commit: `docs/scoring_model.md` §6 gains the ratified RETAIN-4 / DEFER-5 dispositions
(one line each, evidence refs to the 2.2b report), and `tools/param_manifest.json`'s G7 rows update
(GateK's margin row → status `retired`; values untouched elsewhere).

## Task 2 — per-carrier scoping for the diverging shared levers (O-9; mechanism only, values UNCHANGED)

Make `bassNoteRootBonus` and `kWStepIn` **per-carrier deliverable**:
- `bassNoteRootBonus` is already a `ChordAnalyzerPreferences` field — per-carrier delivery = the preset
  builders set it explicitly per preset (all presets today: the same 0.70 — values unchanged in this
  dispatch).
- `kWStepIn` is a file-level global with no per-preset surface — give it one using the SAME
  write-at-configuration-time pattern the override loader uses (the preset configuration writes the
  global; default = current 0.10 everywhere; state the exact plumbing incl. what the notation/production
  path does — if the production path has no preset-selection moment where the write can live, deliver
  per-carrier for the batch/fitting path now and STOP-AND-REPORT the production-path question rather
  than improvising a production behavior change).
- **Byte-identity proof:** with all values at current defaults, full-corpus regen ×3 = 0 diffs; suites
  green. Manifest `preset_scope` column updates for the two rows (shared → per-preset, with the O-9
  evidence ref) in the same commit.

## Task 3 — score-verify `bwv392@17520` (guardrail (2); mechanical extraction + the structural test)

At the blocking cell: the sonority's pitch-class set (from the score/regen dump), the two-tier
structural test (transposition-invariant or share-tone template?), our root under the candidate vs
baseline vs the WiR root + RN, duration. Verdict per the policy: provably class-(a) or **class-(b) on
any doubt**. Report the evidence; if (b) — expected — the case stands as a hard blocker for any
candidate that creates it.

## Task 4 — candidate re-selection under the FULL-corpus hard stop (prepared only)

Under the post-retirement rule set (≡ Config I behavior by construction — prove via the Task-1
byte-identity) and the Task-2 per-carrier scoping (Jazz carrier pinned at its current values for BOTH
levers — its surface must be byte-identical to baseline BY CONSTRUCTION; verify):
1. Sweep `bassNoteRootBonus` (Baroque/Default delivery) over {0.70, 0.7125, 0.725, 0.7375, 0.75, 0.7625,
   0.775} × (`sameRootInversionBonus` 0.475 [Bar/Def], `kWStepIn` 0.125 [Bar/Def]) on the fitting split
   (feasibility per §4.2), reusing the committed 2.2b ledger points where the vector matches exactly.
2. Full-corpus surface ×3 for every fitting-feasible point: **the selection rule = the highest
   fitting-split objective whose full-corpus check adds ZERO new class-(b) batch cases on ANY carrier**
   (the S-3 rejection loop; `bwv392@17520` is the known trip at 0.775). Report the whole trade curve
   (value → fitting gain → held-out → full-corpus ×3 → batch diffs explained), not just the winner.
3. The selected candidate's complete decision surface (the 2.2b §3.1 shape: held-out once, DLC probe,
   snapshot-impact preview, D-4 Default eligibility, Jazz = byte-identical-by-construction check) +
   the **prepared adoption artifact** (values + manifest + scoring_model + goldens scope) — **NOT
   applied**.

## Task 5 — sandwich + suites + report + fold
1. Sandwich ×3 on the REAL dirs = 53/24/53 set-diff empty (the retirements are byte-identical, so the
   stop is unchanged); corpus byte-untouched.
2. Report `cc_stage5_phase2_2c_report.md` (force-add): the five retirement differentials + proofs; the
   scoping mechanism + proofs; the bwv392 verification; the trade curve + selected candidate + surface +
   prepared artifact; reuse-vs-new + **what retires: the five rules (the arc's first real retirements —
   name them)**; all SHAs.
3. Fold (`docs(cowork):`, exact list): STATUS.md (22q) · COWORK_HANDOFF.md · `cowork_stage5_fitter_design.md`
   (O-9 + §14) · `cc_instruction_stage5_phase2_2c.md` (force-add).

## STOP conditions
- A retirement that is NOT corpus-byte-identical (evidence contradiction — revert, report).
- The kWStepIn production-path plumbing question (Task 2) — report, don't improvise.
- No sweep point passes the full-corpus zero-new-class-(b) rule (then the family result is "the coupled
  gain is not adoptable at any swept value" — report the curve, the user decides).
- Sandwich mismatch; suite regression beyond the declared vacated-fixture drop; any push; any adoption.

## Acceptance
Five retirement commits, each with differential + byte-identity ✓ · RETAIN/DEFER dispositions recorded ✓ ·
per-carrier mechanism byte-identical, manifest synced ✓ · bwv392 class verdict evidenced ✓ · the trade
curve + selected candidate + full surface + prepared-not-applied artifact ✓ · sandwich + suites (new
composing count stated) ✓ · report + fold with SHAs ✓.
