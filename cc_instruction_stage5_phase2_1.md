# CC Instruction — Stage-5 Phase 2.1: the clean-lever fit (kPowerChord3PcPenalty) — CANDIDATE ONLY, no adoption

> **ACTIVE DISPATCH (Cowork, 2026-07-04).** Third CC increment of the Stage-5 fitter arc, per the SIGNED
> design `cowork_stage5_fitter_design.md` and the **RATIFIED Checkpoint P1** (design §4.3: split 261/65 ·
> coordinate search · the four-step staging · R-13 skipped · the two rider-flagged rows stay frozen with
> corrected rationales). Read design §2 (esp. 4c idioms-only), §4.2 (objective + constraints), §4.4
> (family fits), §4.7/S-4 (adoption events), D-4, and your own `cc_stage5_phase1_report.md`.
>
> **THE CENTRAL RULE OF THIS DISPATCH: the fit produces a CANDIDATE + a decision surface. NO committed
> constant value changes. Adoption is a SEPARATE user-ratified event after this report** (design A-4:
> every behavior change is user-ratified, one revertible commit — that commit is NOT in this dispatch).

> **Read first (every session):** `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (top entries),
> `C:\s\MS\BUILD_AND_TEST.md`, `C:\s\MS\docs\scoring_model.md` (this touches scoring-constant *values*
> in candidate form).
>
> **Current state (Cowork-verified 2026-07-04):** batch stop 53/24/53; corpus 352/352 ×3 (`0dd64660f4`);
> suites composing 1096 / notation 53 / snapshots 11; the harness live (override mechanism byte-identity
> proven; driver fixture reproduces 63.32/62.37/63.22; ratified split in `tools/stage5_split_registry.json`,
> fitting-split baselines 63.50/62.43/63.37). Expected dirty: the Cowork fold files + the known
> deliberately-untracked scratch. **Hard stops:** any committed constant value change; any write under
> `tools/corpus/`; sandwich mismatch; any push.
>
> **VS Code bash rules apply:** `; echo "exit:$?"`; large output → file + `head`.

---

## Task 0 — state check
HEAD, branch, dirty set vs expectation. Report.

## Task 1 — manifest rationale corrections (ratified at P1; values untouched)
Edit ONLY the two `status_rationale` strings in `tools/param_manifest.json`:
- `kOtherToneFactor`: → "frozen: the tone-weight family's declared SCALE ANCHOR — a relative-weight
  system fixes one unit; measured leverage (0.161, Phase-1b rider) shows the anchor is load-bearing,
  not that it should float (P1 ruling 2026-07-04)."
- `maxTotalInversionContextBonus`: → "frozen: DELIBERATELY NON-BINDING at its current value (2.0 >
  the 1.85 bonus sum); the individual inversion bonuses are the tunable surface; a floating cap coupled
  to the bonuses it caps is a redundant degree of freedom. Not 'inert' as a fittable — binds if reduced
  (Phase-1b rider, Δ 0.101); kept non-binding by ruling (P1, 2026-07-04)."
Commit (`feat(tools):` or `docs:` at your judgment; values and all other fields byte-untouched — state
the diff discipline in the report).

## Task 2 — THE FIT: kPowerChord3PcPenalty (single row; coordinate search; fitting split only)
Via `stage5_fit_driver.py` on the **Baroque carrier** (the idiom-#2 primary; constraint 4c):
1. **Search shape:** a declared ladder over the row's plausible range — the manifest bounds if the row
   has a `bounds()` entry; otherwise declare [0.0, 1.2] (current 0.30) with ~9 coarse steps, then refine
   around the best with 2 rounds of halved step (a 1-D pattern search; deterministic, every evaluation
   ledgered). State the ladder in the report.
2. **Objective per evaluation:** variant-(b) root-agree duration on the **RATIFIED FITTING SPLIT (261)**
   (`a8 --scores` per the split registry); RN + key tracked beside; per-evaluation constraints per design
   §4.2 (no new class-(b) batch case among fitting-split scores; class-(b) duration non-increase on the
   fitting split).
3. **The candidate** = the best constraint-satisfying value. If the best value is the current 0.30
   (no improvement exists), that IS the family result — report it honestly, the family closes "already
   optimal at this resolution."

## Task 3 — the candidate's decision surface (per-adoption checks, design §4.2/S-4 — measured, not adopted)
For the single best candidate value:
1. **Held-out (65) scored ONCE** (a declared checkpoint — record in the ledger as `heldout_check`):
   fitting-split gain vs held-out gain stated side by side. A held-out regression while the fitting
   split gains = the overfit signal — report prominently, no STOP (the user decides at adoption).
2. **Full-corpus, all three carriers (scratch):** root/RN/key deltas vs the ratified baselines; the
   batch-stop sets ×3 with **every set change explained per case with its two-tier class** (the
   mandatory explained diff); class-(b) root-disagree duration deltas ×3.
3. **D-4 Default rule:** the candidate evaluated on Default — adopt-with-Baroque eligibility stated
   (improves Default's objective, no constraint trip). **Jazz = regression spot-check only** (batch 24
   set + class-(b) duration; NO leverage/fit reading — A-3/4c).
4. **Style/validation sweep (S-5), scoped:** IF an existing instrument from the Wave-1 per-style
   baselines can score the candidate on the DLC research corpora as-is (read-only, no new comparison
   logic), run it and report per-style root deltas. If no such instrument exists ready-to-run, **do NOT
   build one in this dispatch** — record the gap as a named Cowork item in the report (the S-5 guard
   then rides the adoption ratification as a recorded caveat).
5. **Snapshot impact preview:** with the candidate in a scratch run, state whether pipeline-snapshot
   goldens WOULD need refreshing at adoption (do not refresh anything).

## Task 4 — report + fold
1. Report `cc_stage5_phase2_1_report.md` (force-add, own commit): the ladder + ledger refs; the
   candidate + its full decision surface (Task 3, every number with its denominator named); the
   PREPARED adoption artifact (the exact one-commit change that adoption would apply — file+line+value —
   prepared as a description, NOT applied); reuse-vs-new + retires; all SHAs.
2. Fold (`docs(cowork):`, exact list): `STATUS.md` (22n entry) · `COWORK_HANDOFF.md` (header) ·
   `cowork_stage5_fitter_design.md` (the P1-ratified marker) · `cc_instruction_stage5_phase2_1.md`
   (force-add).
3. End-of-run sandwich: characterise ×3 on the REAL dirs = 53/24/53 set-diff empty; corpus byte-untouched;
   suites green (no golden refresh — nothing adopted).

## STOP conditions
- Any committed constant value change, anywhere.
- The best candidate trips a fitting-split class-(b) constraint (then the honest family result is
  "unfittable under constraint" — report, don't search around the constraint by relaxing anything).
- Sandwich mismatch; suite regression; a needed instrument modification beyond additive flags already
  landed (report instead).
- Evaluation cost >4× the ~45 s Phase-1 figure.

## Acceptance
Rationale corrections landed (values byte-untouched) ✓ · the 1-D fit ledgered + deterministic ✓ · the
candidate's decision surface complete (fitting/held-out/full-corpus/3-carrier/batch-diffs-explained) ✓ ·
adoption artifact PREPARED not applied ✓ · sandwich + suites ✓ · report + fold with SHAs ✓.
