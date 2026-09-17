# CC Instruction — Stage-5 Phase 3: CALIBRATION — the fitted Class-P maps + C2 θ candidates + D-FS closure + the R-11 disposition

> **ACTIVE DISPATCH (Cowork, 2026-07-06).** Ninth CC increment of the Stage-5 arc, per design §4.5.
> **Everything in this dispatch is measurement + committed ARTIFACTS: no behavior change anywhere —
> no boundary wiring, no θ adoption, no committed value change, no corpus write, no push.** The maps
> and θ candidates are fitted and validated; their WIRING into live boundaries is a separate, later
> increment (engage-adjacent), exactly like every adoption so far.
>
> Read first: CLAUDE.md (52/24/52) · STATUS.md (top) · design §4.5 + O-13 · `cc_c1_reliability_report.md`
> IN FULL (the substrate + the §5 row facts) · `cowork_confidence_contract.md` §2/§5/§6/§7 ·
> `tools/stage5_split_registry.json`.
>
> **Current state (Cowork-verified 2026-07-06):** HEAD = the 2.3 SHA-completion (`02ec8b0d60`); batch
> stop 52/24/52 (manifest `git_hash c50002fee1`, fingerprint-validated); suites 1101/53/11; A-8
> ratified 63.36/62.37/63.25. Expected dirty: the Cowork fold files + known scratch.
> **Hard stops:** any behavior change (the standard `.ours.json` and all suites byte-stable throughout);
> any corpus write; any push. **VS Code bash rules:** `; echo "exit:$?"`; large output → file + `head`.

---

## Task 0 — state check
HEAD, branch, dirty set; characterise ×3 = 52/24/52 set-diff empty. Report.

## Task A — the fitted Class-P reliability maps (C1's remaining deliverable)

**Scope ruling (constraint 4c / A-7, binding):** maps are fitted for the **idiom-#2 target** and labeled
so — delivered (later, at wiring) through the Baroque/Default carriers. **The Jazz carrier gets NO map**
(fitting a Jazz Class-P map on Bach data would mislabel the style axis); it stays Class M with the A-7
mark. Fit substrate = the C1 harness machinery (`tools/c1_reliability.py` + the dump chains), regenerated
fresh on the CURRENT (2.2e-adopted) corpus — the C1 report's numbers predate the adoption, so re-measure
the curves first; expect small shifts, report old→new per row.

**Split discipline:** maps are FITTED on the fitting split's cells only (the ratified 261, per the split
registry); **validated on the held-out split** (report pre-map vs post-map ECE + monotonicity on BOTH
splits — the held-out post-map ECE is the honesty number).

**The rows (per the design §4.5 dispositions — fit the strong, defer the broken with reasons):**
1. **L3 key-of-slice — the sequence margin** (the D-L3a-declared boundary confidence): fit **isotonic
   regression** (the declared default; a Platt sigmoid ONLY if the isotonic fit is near-logistic — state
   the choice per the declared rule, not preference). Baroque + Default carriers.
2. **L4 chord-of-slice — the composite**: same procedure. The flat low band (< ~0.5) is mapped honestly
   (a wide flat segment — the map may not invent resolution there; assert the fitted map is flat where
   the data is).
3. **DEFERRED with reasons re-verified (no map fitted):** L5 `combinedBoundary` (re-measure the
   non-monotonicity on the current corpus — if it still inverts, the deferral stands; if the 2.2e
   adoption changed the shape, report, don't fit without Cowork), cadence `tonicVote` (3-value
   anti-monotone), L1.5 texture strength (Task B decides).

**Artifacts (committed):** `tools/calibration_maps/stage5_classP_<row>_<carrier>.json` — map type,
knots, fit-substrate reference (corpus git_hash + split), pre/post ECE both splits, the idiom-#2 label +
license-provenance line (the C1 substrate is WiR-adjudicated = fitting-pool). Plus the contract §3 row
updates ride the FOLD as Cowork-file edits? NO — `cowork_confidence_contract.md` is a Cowork-owned doc:
list the exact §3 row-status changes ("map fitted, wiring pending") in the REPORT for Cowork to apply;
do not edit that file.

## Task B — the L1.5 spike-vs-surface split (the pre-map measurement, C1 §5.5)
On the C1 dev-bed substrate: split the candidate ticks into marker-spike vs surface-cue populations and
re-measure the reliability curve per population. Verdict material: does either population alone have
usable spread + monotonicity (→ a map could be fitted per population at a later increment), or does the
deferral stand? Measurement only; no map without the numbers saying so (and report first either way).

## Task C — C2: the frame scales declared + θ candidates (D-FS closure; dormant substrate; candidates only)
1. **Declare the two contradiction-scale squashes** (design §4.5.2): F-A `cadentialWeight` (observed
   [3.25, 9.35]) and F-B `bestPlaus − committedPlaus` (observed [2.0, 3.0]) — propose the squash shape
   per R5 (monotone, [0,1], constants precision-phase), re-confirm the observed ranges on the current
   corpus via the existing dump chain.
2. **Fit θ candidates** on the existing fires-vs-corrections instrument (the E0 #9 / C1 §4 machinery,
   dormant chain, fullspine): for each frame, the θ (against the now-squashed scales + the Task-A mapped
   incumbents where applicable) that maximizes corrections-minus-harm on the fitting split; validated on
   held-out. **Acceptance reference: not worse than the current constants' fires/corrections ratio.**
   Candidates + surfaces RECORDED (ledger + report); **nothing wired — the frames are dormant-chain
   sites; their adoption rides the engage arc** (the same O-13 substrate logic; state this in the report).
3. If the instrument cannot express a needed quantity without modifying pinned tools: additive default-off
   flags only, byte-identity proven — else STOP and report.

## Task D — R-11 conformal disposition (the design §14 checkpoint item)
On the SAME substrate as Task A's L3/L4 rows: compute split-conformal abstention sets (fitting split as
calibration set, held-out as test) at 2–3 declared coverage levels; compare against the fitted maps'
implied abstention (confidence-below-bar) on coverage/efficiency. Deliverable = the recorded verdict
material: does conformal add value for the ABSTENTION bars specifically (design: "a complement, not a
replacement")? Recorded for the Cowork disposition; nothing adopted.

## Task E — sandwich + report + fold
1. Sandwich ×3 = 52/24/52 set-diff empty; corpus fingerprint-validated untouched; suites green, no
   golden refresh; standard `.ours.json` byte-stable (this dispatch computes on dumps + Python only,
   plus any sanctioned additive flags).
2. Report `cc_stage5_phase3_report.md` (force-add): the re-measured C1 curves old→new; per-row map
   fits with pre/post ECE on both splits; the deferral re-verifications; the L1.5 split verdict material;
   the declared scales + θ candidate surfaces; the conformal comparison; the exact contract-§3 row
   changes for Cowork to apply; reuse-vs-new + retires; all SHAs.
3. Fold (`docs(cowork):`): `STATUS.md` (22x) · `COWORK_HANDOFF.md` · `cowork_stage5_fitter_design.md`
   (Phase-3 markers) · `cc_instruction_stage5_phase3.md` (force-add).

## STOP conditions
- Any behavior change; any non-additive tool modification; any corpus write; any push.
- A fitted map that is non-monotone or resolution-inventing (fails its own assertion) — report, don't ship.
- The L5 non-monotonicity having CHANGED shape post-adoption (report before any fitting).
- Sandwich mismatch; suite regression; cost >4× (~expect: 3 fullspine corpus runs + Python fitting;
  well under 2 h).

## Acceptance
Re-measured curves ✓ · L3+L4 maps fitted, validated on held-out, committed with provenance ✓ · deferrals
re-verified with reasons ✓ · L1.5 split measured ✓ · scales declared + θ candidates surfaced (dormant,
recorded, unwired) ✓ · conformal verdict material ✓ · contract-§3 changes listed for Cowork ✓ ·
sandwich + suites ✓ · report + fold with SHAs ✓.
