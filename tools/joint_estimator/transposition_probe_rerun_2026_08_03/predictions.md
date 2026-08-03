# Predictions — the repository-side re-run of the transposition-equivariance probe

> **REGISTERED BEFORE ANY DECODE RAN IN THIS SESSION** (#17b; the guard whose absence
> `OPEN_ITEMS.md` OI-219 records the cost of). Written 2026-08-03 (CC, phase 1o, Task 4.3 step 2),
> committed in the same act as the driver and BEFORE `rerun_repo_side.py` was invoked.
>
> What this run is: the repository-side re-run `OPEN_ITEMS.md` OI-243 names as its FIRST action,
> owed before that row's finding and OI-244's carry any load (#19). It is a REPRODUCTION run, not a
> new probe: the committed apparatus is driven unchanged, so the honest prediction is reproduction,
> and the informative prediction is the one about §4.4's separation, which the original run did not
> make.

## What was read before predicting

The original run's own predictions and their refutation, at
`tools/joint_estimator/transposition_probe_2026_08_02/report.md` — its P1 (establishment, PASSED
12/12), P2 (≥ 99 % segment equivalence, REFUTED at 811/1224 = 66.26 %) and P3 (violations
concentrate in spelling-sensitive cells and NOT in boundary placement, REFUTED in its second half:
boundaries moved in 27 of 36 conditions).

## R1 — establishment (§4.3 step 1)

**I predict REPRODUCTION: 12 of 12 sample pieces reproduce `decode_parity_ref.json` exactly,
segments and total score both.**

*Why.* Every input is committed and none of it has moved: `probe_decoder.py`, the parity reference,
the note-events artifact (provenance corpus git hash recorded in the committed
`establish_state.json`) and the fitted tables are all in this repository, and every wave since the
original run has been recorded READ-ONLY on the system — no `src/` change, no golden refresh, no
`tools/corpus/` or `tools/robust_stop/` movement. The original ran against a mount of this same
repository. A reproduction is therefore what the record predicts, and a failure would be evidence
that something moved that was not supposed to.

**The one named risk, registered so it is not explained after the fact.** The two runs execute on
different Python builds and therefore different C library transcendental functions. Segment
comparison is exact tuple equality and the total-score comparison is `abs(delta) < 1e-6`, so a
last-place difference in `math.log` cannot move a score past that tolerance by itself — but it
could in principle flip a decode that sits on a near-exact tie. **Predicted incidence: zero.** If
any piece fails, the first question is whether its two total scores differ by less than 1e-9
(a near-tie flip) or materially (something moved).

A secondary, non-blocking prediction: `header_crosscheck_ok` may read false if the corpus XML
directory the header reader wants is absent here. It is a cross-check only — it is not part of the
`ok` verdict and cannot cause a STOP. **Predicted: true on all 12** (the corpus is in the tree).

## R2 — the transposed conditions

**I predict the committed figures reproduce exactly**: 811 of 1224 segments matched (66.26 %);
per shift 340/408, 266/408, 205/408 for +2, −3, +6; boundaries identical in 9 of 36 conditions;
exactly 6 conditions bit-exact, and the same six named ones (bwv297|+2, bwv321|+2, bwv321|−3,
bwv373|+2, bwv398|+2, bwv55.5|+2); 413 violations.

*Why.* The same argument as R1 — the decode is deterministic and the transposition is arithmetic on
committed note records. **A divergence here would be a finding about the APPARATUS, not about the
decoder**, and must be reported as such.

## R3 — §4.4, the separation the original run did not make

The dispatch asks how much of the measured non-equivariance is **defensible enharmonic ambiguity**
and how much is **boundary movement and collapse**. The classification is defined here, before it
is computed, so the definition cannot be chosen to suit the answer:

| class | definition | defensible? |
|---|---|---|
| **BND** | every violation in a condition whose `boundaries_identical` is false | **No.** Segmenting the same sounding music differently is not a spelling choice. |
| **COLLAPSE** | a condition matching ≤ 10 % of its segments (a subset of BND, reported separately) | **No.** |
| **LBL-PRUNE** | a label-only violation whose `expected_state_in_candidates` is false | **No.** The expected reading was never on the candidate list — that is the admission prune (OI-244), not a spelling judgment. |
| **LBL-ENH** | a label-only violation at k = +6 with the expected state in the candidate set | **Yes — this is the defensible upper bound.** +6 is the one shift whose spelling the declared convention had to choose arbitrarily (the sharpward tritone). |
| **LBL-OTHER** | a label-only violation at k = +2 or k = −3 with the expected state in the candidate set | **No.** Those two shifts have an unambiguous engraver spelling, so a flip there cannot be excused by the frame. |

**Predicted, from the committed report's own condition table** (boundaries identical in exactly
bwv297|+2, bwv321|+2, bwv321|−3, bwv373|+2, bwv373|−3, bwv398|+2, bwv398|+6, bwv55.5|+2,
bwv55.5|−3):

- **BND ≈ 396 of 413 violations (≈ 95.9 %)**, with 27 of 36 conditions boundary-moved.
- **COLLAPSE: 3 conditions** (bwv2.6|+6, bwv297|+6, bwv420|+6), each with a total-score delta worse
  than −12.
- **LBL total 17**, split **10 at +6** (all in bwv398|+6) and **7 at −3** (bwv373|−3 six,
  bwv55.5|−3 one); **none at +2**.
- **LBL-PRUNE: 5** (the four bwv373|−3 cells at ticks 10080/11040/12000/12480 and bwv55.5|−3 at
  10560, which the original report diagnoses to the absolute-tonic-pc tie-break).
- **LBL-ENH — the defensible upper bound — predicted 10 of 413, band 8–10 (≈ 1.9–2.4 %).** The band
  is not 10 exactly because whether all ten of bwv398|+6's expected states were in the candidate
  set is not stated in the report and is read from the raw data.

**So the registered claim is: at most about one violation in forty is defensible as an enharmonic
frame difference, and about ninety-six in a hundred are boundary movement.** If the measured
defensible share comes out materially above the band, the caveat carried on OI-243 is stronger than
the row states and the row must be narrowed; if it comes out at or below, the row's finding stands
in the form the row states it.

## R4 — what this run does NOT settle, said in advance

It re-measures; it does not fix. No remedy is designed here and none is implied. The disposition of
OI-243 and OI-244 belongs to the family design at its own stage, over the whole family at once
(`CLAUDE.md`, the one-fix-per-family rule of 2026-07-28).
