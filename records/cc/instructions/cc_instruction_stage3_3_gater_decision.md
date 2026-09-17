# CC Instruction: 3.3 Gate R decision — reconstructed-credit (option 1)

## The decision

**Option 1 — reconstructed-credit.** Gate R tests the pipeline-reconstructed
`fullBasisDep = cell.basisDep + cappedInv ≤ 0` ("the candidate earned no inversion
credit"). Rationale, on the record:

1. **It is the correct execution of the ratified INTENT, and the ratified MECHANISM
   text is hereby superseded as falsified-by-derivation** (Method F). The redesign's
   goal (design §6 / audit Finding 6) was to remove Gate R's cross-layer dependence on
   the oracle's `basisDep`. Post-migration, `cappedInv` is computed in Pass A itself —
   option 1 makes Gate R read a value its OWN layer computes. Fully intra-layer;
   Finding 6 closes. The "direct pcWeight third test" was an approximation of the
   proxy's semantics; your derivation shows the true discriminator is `cappedInv == 0`
   (which for Dim legitimately includes the temporal completeTriad gate). Reading the
   true semantics beats reading the approximation.
2. Byte-identical by construction on every quality; gater_tests F2 green unchanged —
   a free consistency check.
3. Options 2 (accept a theoretical gap and hope the corpus has no instance) and 3
   (replicate the approximation's error per-quality with more code) are rejected:
   both preserve a wrong mechanism description at different costs.

**Documentation requirements (same commit):**
- `docs/decoder_design.md` §6: dated amendment — the pcWeight mechanism superseded;
  the derivation summary (old fires ⟺ `cappedInv==0`; the Dim divergence; why
  reconstructed-credit is the faithful form); pointer to your report §1.
- `docs/scoring_model.md` §4 Gate R: the condition's TRUE semantics ("no inversion
  credit earned — `fullBasisDep ≤ 0` over the pipeline-reconstructed value"), replacing
  the sounding-third framing; keep the Cm7add11/F spare-case and Δ=+7b fire-case
  explanations re-worded to the credit semantics.

## The basisIndep ≤1-ULP reassociation — one hardening requirement

Your disjointness + comparison-surface argument is accepted as the PRIMARY approach,
but winner selection runs at full precision and undocumented near-ties may exist
anywhere in 353×3 scores. Therefore: if the 0/353×3 A/B shows **any** diff, do NOT
reconcile case-by-case — switch immediately to your documented **bit-identical
fallback** (expose `d` separately so `(V+d)+r` composes exactly) and re-run. The
fallback is pre-approved; a diff under the primary is not a stop, it's the trigger.

## Proceed

Task 1 is accepted as complete (the survey is exemplary — the mutual-exclusivity
proof for `bb`/`cappedInv` and the Dim derivation are exactly Method D). Implement
(Task 2) with option 1 + the doc requirements above; verify (Task 3) unchanged;
one atomic commit, held for ratification as instructed.
