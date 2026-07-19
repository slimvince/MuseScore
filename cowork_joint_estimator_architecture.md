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

**Decided 2026-07-19 (→ §5a):** the mode vocabulary, the fitting parameterization, the chord-state
basis (scale-degree-valued), the non-chord-tone placement, and the signature/declared-mode prior.
**Remaining for the structure-design step:** the precise functional form of each factor and the joint
factorization (how the factors multiply; the conditional independences); the exact-vs-approximate
inference call (mitigated — the ratified state space is compact: 24 keys × the degree vocabulary);
whether our richer-than-published clue set actually improves precision (the one CONJECTURE, resolved
only by build-and-measure); any factor where published theory supplies no form; and the desk-simulation
forms owed by OI-181. These are nameable, bounded, and mostly closable by deriving from the literature,
not by groping.

## 5a. Design decisions ratified (the design pass, 2026-07-19 →)

**★ The factorization specification is USER-RATIFIED (2026-07-19): `cowork_joint_estimator_factorization.md`**
— the variable structure, score form, ten-factor roster, premise ledger P1–P8, decode plan, and
desk-simulation forms/case list. It is the governing structure document; the five decisions below are
its foundations. Next in the funnel: the desk simulation (its §6), then the pre-fit gates
(OI-176/OI-177/OI-178/OI-180). No build before those.

**Mode vocabulary (user-ratified 2026-07-19).** The joint state's mode axis is **{major, minor}** —
minor meaning the composite minor practice (natural/harmonic/melodic as one key with variable sixth and
seventh degrees). **Modal and chromatic color is modeled in the pitch-emission factor**, not the state:
the first build carries the minor-scale variants (raised sixth and seventh) only; church-mode variants
(Dorian sixth, Mixolydian seventh, Phrygian second, …) enter later only through their own premise-ledger
entries (#17); the dominant-family exotic scales are **excluded from the state space** (constrained-
optimum ledger record: the 21-mode state space is excluded because its states are ungradable against any
ground truth we possess — #19/#20 — and OI-174 measured them harming inference). **User's condition,
part of the decision: the un-rounded reading is preserved and published.** The emission factor's
modal-variant evidence is published as a derived fact on the output surface, so the presentation layer
can show the end-user that a passage decoded as, say, D minor would — without the rounding to
major/minor — be called D Dorian, and can choose whether/how to display that by user preference (the
eventual preset ↔ mode-prior mapping is a presentation/preference concern, not an inference state).
Inference states stay two-mode under every preset. This resolves the OI-174/OI-132/OI-147 mode-
vocabulary question at the design level; the rows close when the build lands.

**Fitting parameterization (user-ratified 2026-07-19).** The staged form: **the factor TABLES are fit
generatively from ground-truth counts and frozen** (each table established on its own — the
key-conditioned chord-transition table, the bass-note-given-chord-and-inversion table, the tone-category
emission tables, the key-change table — every entry a musically meaningful probability, per the
published forms); **the small vector of COMBINATION WEIGHTS over the factors is fit discriminatively by
convex conditional likelihood** (the semi-Markov conditional-random-field objective with the logarithms
of the frozen tables as features; L2 penalty; the OI-176 held-out gate and OI-177 capacity budget
govern). **Mandatory ablation arm:** all-weights-equal-one IS the pure generative model, so the weight
layer's contribution is measured on held-out data inside the same machinery, never assumed — its
adoption is gated on winning that comparison. **Ledger entries attached to the decision:** (a) the
staged ASSEMBLY is our synthesis (each stage established separately in the literature; the combination
is an assumption with its own #17b prediction); (b) constrained-optimum record — the unconstrained
alternative is the fully joint discriminative fit with rich free features (possibly a higher ceiling),
excluded because fully joint weights sacrifice the modular diagnosability (#3/#19) the error-correction
loop runs on; re-test if that constraint stops binding; (c) fit-scope declaration (the Noland &
Sandler lesson): which components may be re-fit is declared before any fit — tables from counts, once,
frozen; only the combination weights move; (d) the direct-metric few-weight search (the minimum-error-
rate protocol with bootstrap confidence intervals) is the established fallback if the likelihood-fit
weights measurably disagree with the reported metric.

**Chord state is scale-degree-valued (user-ratified 2026-07-19).** The joint state's chord axis is a
**Roman numeral — scale degree, quality, inversion — relative to the state's tonic and mode** (the
Raphael-Stoddard / Harasim structure). Consequences, all structural: (a) the tonic/degree coupling
terms (the diatonic-root bonus, `buildChordResult`'s degree, Gate G-E's degree condition,
`applyTonicPriorToSparseChord`, the segmenter's head-gap tonic prior — the gap map's group 1) dissolve
by construction — a degree is key-relative by definition; (b) **transposition invariance**: the chord-
transition table pools all keys' evidence (twelvefold counts per cell — the decisive capacity device on
a 326-piece corpus); (c) the ground truth is natively degree-valued, so tables fit from counts with no
conversion layer, and the OI-173 defect class (four inequivalent `diatonicToKey` definitions, two of
`degree`) is never rebuilt. **The chord symbol (root pitch class, quality, bass) is a DERIVED fact,
published once** (root = tonic + the degree's interval) — the robust stop's root metric is unchanged
and every baseline column stays comparable. **Tonicization is applied-degree classes** (the secondary
dominant V/x, applied leading-tone chords, and the standard chromatic classes — Neapolitan sixth,
augmented-sixth chords — per the ground truth's own vocabulary; this also matches jazz analytical
practice, where the secondary dominant, and later the substitute dominant and extended dominant chains,
are applied-degree devices — jazz-specific classes enter only under the OI-7 jazz-ground-truth gate).
**Excluded alternatives recorded:** root-valued chord state (forfeits transposition tying and
structurally preserves the ad-hoc key coupling the audits condemned); momentary modulation for
tonicization (fits Bach acceptably but shreds jazz tonicization chains into micro-keys and departs from
the ground truth's labeling convention).

**Non-chord-tone handling (user-ratified 2026-07-19).** **No live cleaning stage exists.** Non-chord
tones live INSIDE the pitch-emission factor: each tone is emitted by category (chord member vs
within-scale non-chord tone vs outside-scale tone — the Raphael-Stoddard structure), with the emission
probability conditioned on **chord-independent melodic and metric covariates** — stepwise approach and
departure, chromatic-neighbor motion, metric weakness, the tied-over/syncopated preparation (the
figuration-feature forms Masada & Bunescu fit on chorales; every covariate computable without knowing
the chord, so no circularity). Chord identity and tone status are decided together in the one decode
(#12 — no ornament verdict is ever committed early). **Ornament labels (passing tone, neighbor tone,
suspension, appoggiatura, pedal point) are derived AFTER the decode** from the committed chord by the
standard definitions and published as a derived fact for the presentation layer — the same pattern as
the modal-color publication. **Style adaptation is values-only:** the chord-tone boundary shift in jazz
(tensions as chord members) is a VOCABULARY matter handled by the degree-valued quality classes; the
changed ornamental/metric conventions (enclosures, anticipations) are covariate TABLE VALUES refit per
preset — same structure, no per-style rule code; jazz-specific covariate additions enter only under the
OI-7 jazz-ground-truth gate with their own ledger entries. **Establishment resource:** the BCMH
reduction is the chorales with non-chord tones removed — aligning the 87 overlapping full-texture
stems against their reductions yields empirically labeled chord-tone/ornament data for fitting and
validating these emission tables (BCMH's declared instrument status applies). **Excluded alternatives
recorded:** a live pre-cleaning stage (the published cleaners' ~28 % error rate would be hard-committed
upstream, violating #12, and the suspension's chord-relative definition makes pre-cleaning circular);
pure category emission without melodic covariates (discards the established voice-leading evidence —
the strongest ornament discriminator).

**The key-signature and declared-mode prior (user-ratified 2026-07-19).** A **weak, fitted,
transposition-invariant soft prior on (tonic, mode)** from the notated signature — a small categorical
table (local-key tonic distance from the signature's relative pair on the circle of fifths, by mode)
counted from ground truth; the declared mode, where the score carries one, is a second conditioning
input with its own fitted strength. **No conditional gate and no threshold anywhere:** the user's
intent — the signature consulted only where the analysis is otherwise unsure — is delivered by the
probability calculus itself (a weak prior is negligible where the content likelihood is decisive and
tips the scale only where the evidence is ambiguous), never by an "if uncertain" code path. Bach's
modal notation practice (the Dorian chorale written one flat short) is handled statistically as
measured mass one fifth away in minor — no special case. A mid-piece signature change re-anchors the
prior (discharging the OI-94(a) deferral). **The signature-influence rate is measured by ablation and
published at every fit** (the fraction of committed keys the signature factor changed), with the
recorded expectation that it is SMALL — a large fitted weight or influence rate is a #3 finding to
investigate, not to ship. **The declared-mode wall (the −7 hard penalty) is formally retired.**
Whether the prior conditions the initial key state only or also acts as a weak persistent pull is
settled by the desk simulation, not assumed. Ledgered as OUR form — the literature's absence of any
signature prior is explicitly cited (PKSpell: the formalization "is missing"). **Excluded alternatives
recorded:** the hard signature constraint (factually false three ways; the known wall-defect pattern);
no prior at all (discards free information; contradicted by the Stage-4a declared-mode measurement);
the literal conditional "consult only when uncertain" (reintroduces a threshold gate the soft prior
makes unnecessary). *(The signature's separate job — naming the prevailing collection for the
spelling/collection emission, the OI-168 mask — is a different factor and untouched by this decision.)*

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
