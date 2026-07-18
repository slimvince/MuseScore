# Ratified architecture — the key/mode/chord estimator is JOINT (option A)

**Decision (user-ratified 2026-07-14).** The tonal analyzer's key, mode, and chord are inferred by a
**single joint probabilistic estimate**, not a feed-forward pipeline and not an ad-hoc provisional-then-
refine loop. Grounding: `cowork_key_chord_joint_inference_grounding.md` (five-stream literature review,
primary sources fetched). This **supersedes the incremental "key layer" framing** of
`cowork_key_layer_design_opening.md` — the key layer is not a separable layer to bolt on; it is one axis of
the joint estimate.

Why (settled over 2026-07-14): the mutual dependence of key/mode/chord is the *established* structure of
tonal analysis (Micchi et al. 2020; Wu et al. 2020; the whole probabilistic + multi-task lineage), our
OI-175 finding is that dependence appearing as an ad-hoc iteration, and — judged purely on long-term
inference accuracy under our own methodology — no argument survives for the alternatives: feed-forward
(B) is a greedy approximation that can only lose to a joint global decode and commits information early
(#12); a learned black box (C) needs data we lack and is un-establishable/undiagnosable (#1/#3/#18/#19).
The residual ideas of B and C survive only *inside* A (approximate inference for tractability; a learned
factor only where theory supplies no form).

---

## 1. What A is (the spec direction — forms to be pinned in the design pass)

- **State:** a joint `(tonic, mode, chord)` per unit, with **segmentation as a modeled (semi-Markov)
  variable**, not a fixed pre-pass a provisional key shaped (the Raphael-Stoddard composite-state structure +
  the semi-CRF segmentation lineage).
- **Inference:** **exact joint decode** (Viterbi/DP over the joint state) is the target; approximate
  inference is held in reserve *only* if exact decode proves intractable (an inference technique, not an
  architecture change).
- **Factors = our enumerated clues.** Every hint in `cowork_evidence_inventory.md` enters as an emission,
  transition, or prior *term* in the one decode — the joint model is the antidote to the information loss a
  pipeline causes (#12).
- **Parameters:** each factor's **form** comes from established theory (#1/#2); its numeric **values** are
  **fit once, globally, against ground truth** (#19) and frozen — **never per-case tuned** (#8; the DT-2
  firewall). A wrong result is diagnosed as a *structural* error (wrong form / missing clue) or accepted as
  irreducible residual, never patched by twiddling a weight.
- **Learned factors** are admitted *only* where established theory supplies no form, kept as a single
  inspectable term inside the model (the C-kernel, hybridized — not a black box replacing the model).

## 2. The factor roster (evidence → term; forms to be derived, not assumed)

From `cowork_evidence_inventory.md` §8, mapped to the joint model (`cowork_key_chord_joint_inference_grounding.md` §5):

- NCT-cleaned **tone collections / pitch content** → emission `P(pitches | tonic, mode, chord)`, metric-weighted;
- **notated signature + declared mode** → prior on `(tonic, mode)` (fixed input);
- **notated spelling + accidentals** → spelling-conditioned emission + mode disambiguation;
- **cadence votes + leading-tone events** → emission/transition factor on `(tonic, mode)` at cadence points (the OI-166 channel, as a *factor*);
- **progression grammaticality** → the chord transition term (licensed motions weighted up);
- **harmonic rhythm + boundary strength** → the segmentation (semi-Markov segment-duration) model;
- **beat strength / metric position** → emission weighting + a chord-change-on-strong-beat prior;
- **fermatas + phrase facts** → segment-boundary and cadence-location priors;
- **bass-motion skeletons** → a bass/inversion emission.

## 3. What this reframes (the in-flight items are now parts of A)

- **OI-166** (key-agnostic cadence pre-scan) — still built, at L1.5; it is now the **cadence factor** of A, not a forward vote. Its precision probe still gates whether/how strongly the factor is weighted.
- **OI-168 / OI-170** (the δ collection-membership fix) — the signature-mask collection term is the correct *form* of that emission factor; the class-(a) fix stands as adopting the right form.
- **OI-174 / OI-147** (spurious `Altered` / exotic modes on plain material) — a **mode-vocabulary and mode-emission-form** question for A (should exotic modes be states, emissions, or excluded?), a design-pass decision.
- **OI-175** (provisional key → segmentation) — **superseded** by A's joint decode with segmentation as a modeled variable; the ad-hoc back-edge dissolves into the joint estimate.
- **OI-23 (~30 hand-set chord constants) + the hand-set key change-costs (OI-91/OI-97)** — replaced by A's fit-once factors; the accumulated ad-hoc weights retire as the joint model is fit.
- **The measurement chain (OI-145 wave 1)** — **retained in full**: A is graded against DCML ground truth through the same robust unit; the hardening we did is what lets A be measured honestly.

## 4. The path to A (the #17 funnel — research/design first, no building yet)

1. **Term-level theory-grounding audit** (the "consult-and-derive" pass): enumerate every factor in §2, derive its *form* from established theory/research (#1/#2), triage the current terms keep/fix/drop, and name the genuinely-open forms where theory runs out (#5). This is the direct answer to "do we have the right terms with the right forms."
2. **Joint-model structure design** (with the user): the state space, the factorization (conditional independences / how the factors multiply), the segmentation model, and the **open decisions** — the mode vocabulary (OI-174), the factorization, and any theory-gap factor.
3. **Desk-simulate → read-only probe → build** (the funnel): no build until the structure + forms are pinned and ratified; each factor's contribution probed read-only where possible before it is wired.
4. **Fit once, establish, measure** (Stage-5 discipline, DT-2 firewall): forms fixed, values fit globally against GT, established (#19), measured on the retained measurement chain.

## 5. What is NOT yet decided (honestly, for the design pass)

The state space's exact contents (esp. the **mode vocabulary**); the precise **functional form** of each factor and the **joint factorization**; whether our richer-than-published clue set actually improves precision (the one CONJECTURE, resolved only by build-and-measure); the exact-vs-approximate inference call if the state space is large; **how the values are fit — the fitting parameterization** (generative, Raphael-Stoddard's unsupervised EM, vs discriminative, the Masada & Bunescu semi-Markov CRF with the same theory-derived factors as feature functions — see §6); and any factor where published theory supplies no form. These are the design pass's agenda — nameable, bounded, and mostly closable by deriving from the literature, not by groping.

## 6. Recorded assessment (Cowork, 2026-07-18) — agreement, two reservations, one refinement

Recorded at the user's request after the ratification, as design-pass input.

**Agreement.** Under the standing constraints (diagnosable, theory-derived forms, values fit once
globally, #1/#18/#19), A is the best-established structure available, and its payoff lands exactly where
the measured defects are: mode, relative major/minor, local key (OI-174/OI-147; the key-LOCAL column).

**Reservation 1 — the joint win is asymmetric (grounding doc §2b/§2c), and the predictions must say so.**
Ni et al.: key ~77→84 %, chord +≈1 pp. Wu et al.: key +3.5 pp, chord ≈flat. RNBERT: explicit joint-decoding
machinery gave a small degradation. A is the established route to **mode/key** precision; on the **chord
root** it buys coherence more than accuracy. The root-agree residual (~34 %) is more plausibly dominated by
emission quality, segmentation, and GT-granularity noise than by missing coupling. The #17b written
predictions for A's adoption must reflect this asymmetry — large movement expected on the key columns,
modest on root; a large root claim would itself be a surprise (#3).

**Reservation 2 — A is a constrained optimum, not a global one (stated for honesty of the record).** On
pure measured precision the published state of the art for symbolic Roman-numeral analysis is the learned
shared-representation models (AugmentedNet, RNBERT, AnalysisGNN — grounding doc §2c), trained on the same
DCML corpora used here as ground truth, so "data we lack" is only partially true. A is chosen because those
models are un-establishable and undiagnosable under #1/#18/#19 — and because their absolute RN accuracy
(~45–50 %) leaves the gap plausibly small on this domain. The decision stands; its basis is the
methodology, not a claim that A out-measures the learned systems.

**Refinement — the fitting parameterization is an open design-pass decision (added to §5).** "Forms from
theory, values fit once" leaves open *how* the fit is done. The generative fit (Raphael-Stoddard,
unsupervised EM) is the weakest instantiation; a **discriminatively fit semi-Markov model** (the Masada &
Bunescu semi-CRF lineage, grounding doc §3: the same theory-derived factors as feature functions, weights
fit once globally against DCML GT) is the same architecture A with typically strictly better precision.
To be decided in the structure-design step, beside the mode vocabulary.

**A possible later form upgrade, not an architecture change:** tree-structured harmonic grammars
(Rohrmeier, *Journal of Mathematics and Music* 2011; Harasim, O'Donnell & Rohrmeier, ISMIR 2018) capture
prolongation and tonicization that a first-order chord transition cannot. Evidence base thinner, fitting
harder; **not fetched in the 2026-07-14 review** — if ever pursued, it enters as a candidate form for the
chord-transition factor only, after its own primary-source grounding pass.

## 7. Plan amendments (Cowork, 2026-07-18, user-directed) — guardrails to pin before the funnel advances

Recorded with the §6 assessment; each has a register row. None changes the decision or the §4 ordering.

1. **Held-out evaluation (OI-176, gates the fit event).** The plan fits A's values against DCML GT and
   grades on the same GT through the robust unit; a figure graded on the data that fit it is not
   established (#19/#16). Declare the fit/held-out split (or k-fold over the 326 covered pieces) before
   any value is fit; the headline claim is the held-out figure.
2. **Capacity budget (OI-177, gates the fit event).** Parameter count and regularization declared and
   justified against corpus size before fitting. Fitted values are Bach-chorale values; generalization
   claims stay de-scoped (the OI-7 pattern).
3. **Architecture-adoption protocol for the robust stop (OI-178, before A's first measured decode).**
   The class-(b) per-preset non-increase is a ratchet for incremental change; A's first decode moves runs
   in both directions. Write the adoption-event variant (aggregate criterion + explained per-run diff +
   O-12 snapshot + ratification) now, not on a live diff.
4. **Ground-truth ceiling (OI-179, can ride the term-grounding audit, read-only).** Measure per-axis
   annotator/GT agreement; interpret #17b targets and "irreducible residual" verdicts against it —
   otherwise structural error and annotator disagreement are indistinguishable in the residual.
5. **Sanctioned dual path (OI-180, structure-design step).** Building A beside the certified stack
   temporarily violates #6; declare the parallel decode, side-by-side grading (#15), and the retirement
   map (the R1–R9 pattern) up front so the transition is pre-ratified.
6. **Desk-sim form for a joint decode (OI-181, before A's desk-sim stage).** #17c's hand-trace does not
   scale to a joint DP; declare the small-instance form (tiny synthetic inputs; single-piece traces with
   the printed DP table).

---

*Provenance: the architecture decision is the user's, 2026-07-14, on the grounding review. The register
(OI rows re-tagged as A-factors / superseded) and `STATUS.md`/`cowork_handoff.md` are updated to point here
as the governing architecture; the key-layer design opening is marked superseded-by-this at its next touch.*
