# CC Instruction — Stage-5 Phase 2.3: the retained-rule margins (staging step 3) + the family-4 §15-13 population gate

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** Eighth CC increment of the Stage-5 arc, per the P1-ratified
> staging (design §4.3/§4.4) — two cheap measurement questions, **nothing adopted, no committed value
> change, no corpus write, no push**:
> **A.** Staging step 3 — do the three surviving §6-block margins hold any fittable gain at FULL range
> (the 2.1 lesson: a ±step-dead read does not extend to the whole range)? Expected outcome:
> skip-with-record; a surprise is a finding.
> **B.** Family 4's gate — how large is the §15-13 both-licensed fall-through population on the DORMANT
> chain? (The design commissioned the preference weight gated on this count — design §4.4 family 4.)
>
> Read first: CLAUDE.md (the NEW 52/24/52 sets) · STATUS.md (top) · design §4.4 families 2–4 + O-11/O-12 ·
> `cc_stage5_phase2_2e_report.md` (the adopted state) · `cowork_layer5_function_design.md` §15-13 +
> §5.5 (the both-licensed semantics).
>
> **Current state (Cowork-verified 2026-07-06):** HEAD = the 2.2e fold (`83f41cdd31`); **batch stop
> 52/24/52** (re-baselined; manifest `git_hash c50002fee1`); suites 1101/53/11 on the refreshed goldens;
> A-8 ratified 63.36/62.37/63.25; fitting-split baseline 63.5391. Expected dirty: the Cowork fold files
> + known scratch. **Byte-untouched claims cite MANIFEST-FINGERPRINT validation, never git status
> (O-12).** **Hard stops:** any committed value change; any `tools/corpus/` write; sandwich mismatch
> (now vs the 52/24/52 sets); any push.
> **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`.

---

## Task 0 — state check
HEAD, branch, dirty set; characterise ×3 = **52/24/52** set-diff empty vs the re-stamped CLAUDE.md
(the first post-re-baseline anchor). Report.

## Task A — the retained-rule margins, full-range ladders (staging step 3)

The three surviving §6-block numeric margins (all 1b-dead at ±step; the 2.1 lesson mandates the full
range before skip-with-record): **`kGateIMargin` (0.45)** · **`kGateLMargin` (0.35)** ·
**`kHalfDimFirstInversionBonus` (0.55, FM2's)**. Per margin, a 1-D ladder via the driver (Baroque
carrier, fitting split, §4.2 constraints; ~5–7 points over the value's plausible range — declare each
range in the report; ledger committed):
- Δ=0 across the full ladder → **skip-with-record** (the margin is confirmed objective-inert; its rule
  is RETAINED on structural grounds and its constant stays hand-set — a legitimate staging-step-3
  closure, stated per margin).
- Any Δ≠0 → report the point + its full constraint status; do NOT chase it further (a mover here is a
  finding for Cowork, not a fit to run).

## Task B — the §15-13 both-licensed population (family 4's gate; DORMANT chain, decode-only)

The §15-13 site is dormant-chain-only (the L5 resolver's `tieBreakOrOpen` fall-throughs at
`functionresolver.cpp` :233/:279 — the BOTH-LICENSED cases specifically; the Phase-0 manifest G9 rows).
Measure its population:
1. If the existing `--dump-fullspine` output already exposes enough to count both-licensed
   fall-throughs (read the dump schema first), count from the dump. If NOT: add an **additive,
   default-off** counter/field on the fullspine path ONLY (the sanctioned dump-flag pattern; byte-identity
   with the flag absent proven — standard `.ours.json` untouched by construction, snapshots no refresh).
2. Run the fullspine chain over the corpus ×3 carriers (scratch); count per carrier: total resolver
   decisions · both-licensed fall-throughs (the §15-13 population) · their breakdown by outcome
   (tie-break vs open mark) · duration share · per-score distribution (max/median).
3. **Deliverable = the gate verdict material:** is the population large enough for an evidence-based
   fit (design §4.4 family 4: "if the population is too small for a fit to be evidence-based, the item
   returns to the user with the number and stays a recorded §15-13 open item")? No fit runs either way —
   the number + Cowork/user decide.

## Task C — sandwich + report + fold
1. Sandwich ×3 = **52/24/52** set-diff empty; corpus manifests fingerprint-validated (O-12 wording);
   suites green, no golden refresh.
2. Report `cc_stage5_phase2_3_report.md` (force-add): the three margin ladders + per-margin closure (or
   findings); the §15-13 population table + the gate verdict material; byte-identity proof for any new
   dump field; reuse-vs-new + retires (expected nothing); all SHAs.
3. Fold (`docs(cowork):`): `STATUS.md` (22v) · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md`
   (the O-12 record + staging-step-3 closure marker) · `cc_instruction_stage5_phase2_3.md` (force-add).

## STOP conditions
- Any committed value change; any adoption; any corpus write; any push.
- A Task-B implementation that cannot stay additive/default-off (report, don't restructure the dormant
  chain).
- Sandwich mismatch vs 52/24/52; suite regression; cost >4× (~50 s/eval; Task A ≈ 15–21 evals; Task B ≈
  3 fullspine corpus runs).

## Acceptance
Three full-range margin ladders ledgered + per-margin closure ✓ · the §15-13 population measured ×3
carriers with outcome breakdown ✓ · byte-identity for any added dump field ✓ · sandwich 52/24/52 ✓ ·
report + fold with SHAs ✓.
