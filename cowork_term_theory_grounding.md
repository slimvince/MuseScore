# Term-level theory grounding — the derivation half of the theory-grounding audit

**Author:** Cowork, 2026-07-19, at the user's direction — the theory-derivation half of the term-level
theory-grounding audit (`cowork_joint_estimator_architecture.md` §4 step 1; the #17 funnel's first stage,
READ-ONLY). Companion: the code-enumeration half `cc_term_inventory_report.md` +
`tools/term_inventory/term_inventory.csv` (95 terms, 80 live). **Method:** five parallel deep-research
passes with primary-source fetch (2026-07-19); every load-bearing claim labeled **FACT** (stated/measured
in a fetched paper), **THEORY** (established published theory), or **CONJECTURE**, per #1. Verification:
the central sources (Raphael-Stoddard, Ni et al., Temperley, Masada & Bunescu) were extracted
independently by 2–3 agents each and cross-checked for agreement; unfetchable sources are flagged and no
equation is carried from an unfetched text. **Nothing here decides anything** — the keep/fix/drop rows are
*inputs* to the design pass; the decisions (mode vocabulary, factorization, fitting) are the user's.

---

## 0. Headline findings

1. **Most of our live emission-side terms already have the right FORM family** — the L4 oracle is
   recognizably the Pardo-Birmingham positive/negative-evidence template score, which is established and
   measured (88.7 % with tie-breaks on their corpus). What is unestablished everywhere is the VALUES
   (hand-set, 1 of ~95 terms ever fit) — confirming the fit-once plan, not indicting the forms.
2. **The biggest theory-backed gaps match CC's gap map exactly:** no NCT-cleaning on the live path (the
   published lineage measures its worth), a spelling-blind key emission (Temperley measured spelling
   worth **+3.6 pp** on key accuracy — the single best-established unused clue we hold), and no
   key-conditioned transition model (the established Ni et al. form).
3. **Two factors have NO published form at all: F2 (signature/declared-mode prior) and the
   cadence→key factor (F4 as evidence).** Our terms there are ahead of the literature — they must be
   declared ASSUMPTIONS with #17b predictions or fit from corpus, not cited.
4. **The literature's mode vocabulary is {major, minor} — nothing more, anywhere fetched.** Every joint
   model (Raphael-Stoddard, Ni, Temperley, Noland) uses 2 modes × 12 tonics. Input to the user's
   OI-174/OI-132/OI-147 decision.
5. **No published inter-annotator agreement figure exists for classical symbolic RN analysis — the
   ceiling we owe under #21 is unmeasured by the entire field.** The in-repo BCMH overlap (87 stems)
   would produce a figure nobody has published. BCMH is prima facie independent (FACT: "we encoded" —
   the PeARL lab's own annotations, borrowing only the DCML syntax) but unestablished (annotator count
   unknown; annotations sit on a reduction; reached us through machine translation).
6. **The fitting question has measured answers:** discriminative fitting of a factored model (semi-CRF,
   L2-regularized, convex) beat structured-perceptron and hand-set weights on exactly our corpus type
   (60 Bach chorales, +6.2 pp) — but LOST to hand-set weights at 46-piece heterogeneous scale, and a
   generative HMM beat a CRF at 18-training-songs scale. 326 pieces sits above every corpus where
   discriminative lost. Och's MERT precedent (8 theory-derived weights fit on 640 sequences by direct
   error minimization, explicitly no overfitting at that scale) is the established protocol for the
   few-weight regime. This validates OI-176/OI-177 as gates and gives the design pass two concrete
   candidate protocols.

---

## 1. Per-factor derivations (form ← literature; triage input ← `term_inventory.csv`)

### F1 — pitch emission P(pitches | tonic, mode, chord) + NCT handling

**Established forms (FACT at fetched sources):**
- **Pardo & Birmingham 2002 (CMJ 26(2))**: template score **S = P − (M + N)** — P = weighted positive
  evidence (note weight = minimal-segment span count), N = weighted non-template notes, M = missed
  template tones; 72 templates; ordered tie-break rules (root weight → corpus prior → dim7 resolution by
  step). Measured: 84.5 % → **88.7 %** with tie-breaks. Their own verdict: the scheme "is not
  sufficient, but improving it while maintaining generality is not easy."
- **Raphael & Stoddard 2003/2004**: the joint-model emission — each pitch classified into **5 categories**
  (root / third / fifth / in-scale-not-triad / non-scale); emission probability depends only on
  (category, metric position ω) — ≈20 parameters, trainable. Within-category uniformity is asserted,
  never tested (FACT-of-absence).
- **Temperley 2002 (ICMAI)**: Bernoulli presence/absence per scale degree per segment,
  P(surface|key) = Π_present S_pc × Π_absent (1 − S_pc), values corpus-estimated (Kostka-Payne table
  fetched). **Measured warning:** duration-weighted input UNDERPERFORMED flat presence/absence
  ("repeated notes appeared to carry too much weight"); and the proper Bayesian form scored WORSE
  (77.1 %) than the heuristic sum (83.8 %) — unresolved in the literature.
- **NCT lineage:** Melisma's ornamental-dissonance rule (stepwise-followed + metrically weak — FACT,
  verbatim); Masada & Bunescu's figuration heuristics (the semi-CRF feature counterpart); Ju et al. 2017
  DNN NCT-identification F1 **72.2 %** on 140 chorales. No generative P(NCT | chord, meter) with fitted
  parameters exists (FACT-of-absence).

**Triage input vs our terms:** `scoreTemplateTones`/`scoreExtraNotes` (+ structural penalties) ARE the
Pardo-Birmingham form family — **keep form, fit values**. The root>second>other weighting (1.8/1.2/1.0)
and extension/foreign/contradiction split are refinements the literature doesn't contradict but has never
fit. **Fix:** NCT-cleaning is absent live (the dormant `classifyTone` machinery is the F1 "cleaned" half
— the roster says NCT-cleaned; the live path feeds raw collections). **Flag (potential form defect):**
the L1.5 repetition boost ×(1+0.3·(n−1)) (`regiontonecollector.cpp:297`) moves emission input TOWARD
duration/repetition weighting — the direction Temperley measured as HARMFUL for key emission
(presence/absence won). Needs its own #17b prediction before A adopts it.

### F2 — prior on (tonic, mode) from notated signature + declared mode

**Established form: NONE (FACT-of-absence, confirmed by dedicated search).** PKSpell (ISMIR 2021) states
it outright: "a formalization of the relation between local keys, global key, and key signatures is
missing in the literature." Every fetched key model takes note lists only. Closest relative: Illescas
et al. 2007 use notated accidentals as a hard diatonic FILTER (not a prior; and note-accidentals, not the
signature). **Consequence:** our signature-proximity / declared-mode-penalty / partial-signature terms
cannot cite a form. They are ASSUMPTIONS — each needs a ledger entry with a written quantitative
prediction, or the prior gets FIT (a 2-parameter categorical prior is cheap under the F10 budget).
The direction is theory-plausible (a signature of k fifths conventionally implies its relative pair —
textbook THEORY); the functional form and strength are ours to establish.

### F3 — spelling-conditioned emission + mode disambiguation

**Established forms (FACT):** Temperley's TPC key profiles over the line of fifths — the **only direct
published measurement of notated spelling improving key inference: 87.4 % vs 83.8 %** (+3.6 pp,
Kostka-Payne), with his honesty caveat (spelling may itself encode the key). Micchi et al. TISMIR 2020:
spelled input "not worse while performing a harder, more musically relevant task" (neural). Spelling
algorithms (ps13 99.8 % on WTC-I; PKSpell 0.13 % error) establish that spelling is nearly deterministic
given context — so as EVIDENCE it is high-precision. Teodoru & Raphael 2007 is now FETCHED
(user-supplied PDF, 2026-07-19, `docs/research_papers/`): the generative spelling|key form is
FACT-grade — a hidden Markov chain of per-measure LOCAL KEYS, the voices' spellings evolving as
conditionally independent Markov chains given the keys, one DP jointly decoding spelling + key
(exactly the spelling↔local-key coupling, in generative form). Measured caveat (FACT, their abstract):
trainable from unlabeled data, but training gave NO demonstrated improvement over the
hand-initialized parameters.

**Triage input:** our chord-level TPC terms (`tpcConsistencyBonusPerTone`, Sus4 TPC factors, nonBass TPC
waiver) — **keep**, they are the F3 chord half. **The gap is the key axis:** the L3 emission is
spelling-blind (CC's inventory) while the best-established unused clue we hold is exactly
spelling→(tonic, mode). The dormant `spellingview` is the carrier. Form for A: a TPC-profile emission
term (Temperley's form, values fit on our corpus) or a raised-7̂/♭7̂ contrast term (see F4). The
enharmonic-rotation gate block (FM2/H/G-D/G-E-as-promotion) does post-hoc what this term does in-model —
**drop-at-adoption candidates** once the in-model term is established.

### F4 — cadence + leading-tone evidence for (tonic, mode)

**Established forms:** cadence DETECTION is established (Bigo et al. ISMIR 2018: 44 binary features,
linear SVM, PAC F1 0.80 on Bach; the key-fingerprint features are exactly the tritone pair — "both 4̂ and
7̂ of the implied key present in the last four beats" (63/63 Bach PACs) — and the resolution feature
7̂→1̂ (52/63)). Cadence-as-KEY-EVIDENCE is **not** established as a published factor (FACT-of-absence):
Bigo deliberately avoids key estimation; Sears/IDyOM conditions on key (wrong direction). **The one
on-point source, Feisthauer et al. SMC 2020, is now FETCHED (user-supplied PDF, 2026-07-19,
`docs/research_papers/`) and its forms are FACT-grade:** (i) the **current diatonic pitch set** CS(b) —
a 7-vector of the last-heard accidental per note name, **defaulting to the key signature** (also the
only published F2-style signature use found); (ii) pitch compatibility as the count distance
ddiat(CS(b), S(k)) = |{note names altered differently}|; (iii) the **V→I detector**: at least two of
three voice leadings — leading-tone→tonic, seventh-resolution, root-of-V→root-of-I — with NAMED false
positives (parallel major/minor of the same tonic; I→IV read as V→I); (iv) the **tonality-anchoring
measure** cV→I(b, k) = 0 at the V or I of a detected V→I in k, else min[cap, previous + 1] — a
beats-since-last-cadence decay; (v) keys chosen by minimizing a weighted cost of the three measures
over the whole tonal plan (a DP over key segments). Measured: 84.8 % keys on 38 Mozart quartet
movements. This is the established feature-and-decay SHAPE for A's cadence factor; its probabilistic
weighting is still ours to fit. **Chorale-specific priors (FACT, de Clercq
EMR 2015, 2,124 fermata events / 346 chorales):** the fermata soprano degree re-interpreted as 1̂/2̂/3̂ of
a closely-related key via authentic/half cadence matches **80.6 %** of internal cadences (89.3 % on
stepwise-descent approaches); in minor, the **relative major (mediant) is the most typical internal key
area** — a published quantitative bridge from cadence events to (tonic, mode) choice in OUR repertoire.
The leading-tone criterion in profile form (FACT): Temperley's minor profile has ♭7̂ = 1.5 (the profile
minimum) vs 7̂ = 4.0 — THE quantitative relative-major/minor discriminator.

**Triage input:** the live cadence labels are key-DEPENDENT degree patterns (annotation-only) — cannot
serve as evidence without circularity; OI-166's key-agnostic detector remains the right build, now with
Bigo's feature set as the established basis for its features and de Clercq's tables as chorale priors.
**Caveat carried to the design pass:** half-cadence detection F1 ≈ 0.3–0.4 everywhere measured — the
cadence factor's weight must respect detector noise on exactly the cadence class most informative about
dominant function. `trueLeadingToneBoost` (presence test) — **fix toward a resolution-event form**
(7̂→1̂), which is what the literature's features test.

### F5 — chord transition / progression grammaticality

**Established form (FACT):** the key-conditioned first-order transition **p(cₜ | cₜ₋₁, kₜ)**, MLE from
transposed (key-normalized) corpus counts — Ni et al. 2012, inside a single joint decode. Empirical
basis for chorales (FACT, Rohrmeier DCRR-004/ICMPC 2008): chorale pc-set transitions are strongly skewed
(top ~10 sets ≈ 59 % of mass) and **directionally asymmetric** (I→V ≠ V→I; Piston's textbook table
"significantly fails" on the asymmetries) — so the table must be asymmetric and corpus-fit, not
rule-set. Grammars (Rohrmeier 2011; Harasim PACFG ISMIR 2018) add recursion and latent structure;
measured evidence: PACFG tree accuracy 45.9 % vs PCFG 39.4 % on JAZZ (n=13 test); Tsushima et al.:
in sequence perplexity PCFG ≤ HMM ≤ higher-order Markov at scale. **No Markov-vs-grammar comparison
exists on Bach-chorale harmonic labeling (FACT-of-absence)** — the grammar upgrade stays a possible
later form for this one factor (arch doc §6), not the design.

**Triage input:** our three live fragments (`wSeq`'s single V→I motion, `resolutionBonus`'s 3 rules,
`wDim`, Gate J, rcb-as-self-transition) — **replace at adoption** by the fitted key-conditioned
transition table (the fragments are 5 hand-set cells of a table the literature says to fit whole). The
dormant `functionprogression` licensing grammar is the rule-form cousin — its content becomes training
regularization/structure, not a live term.

### F6 — segmentation model

**Established form (FACT):** the semi-CRF over segments (Sarawagi & Cohen objective; Masada & Bunescu
applied it to 60 Bach chorales — OUR corpus type): segment features (purity ≈ our collections, coverage
≈ our templates, bass, transition, metric accent), hard length cap L=20, **no explicit duration
distribution** (FACT: none published for chorales; Harana's duration term is implicitly geometric;
explicit-duration evidence exists only on pop audio — Korzeniowski & Widmer: static geometric-family
duration models are far worse than adaptive ones, log-prob −4.0 vs −2.0). **The measured segmentation
signal in chorales is METER:** removing metrical-accent features costs **−5.9 pp** event accuracy
(83.6 → 77.7, FACT).

**Triage input:** our L2 is a hard-threshold filter cascade (anchor 1.5 / round-2 1.25 / floors) + the
OI-175 head-gap tonic overwrite — **replace at adoption** by segment scoring inside the decode
(the ratified semi-Markov choice); the head-gap tonic prior dissolves (OI-175 already superseded-by-A).
Duration model: start implicit-geometric (the established default), harmonic-rhythm refinement is
CONJECTURE territory flagged as such.

### F7 — metric weighting

**Established forms (FACT):** Raphael-Stoddard's emission-conditioned-on-ω (learned, form only — the
learned table was never published); Temperley's strong-beat rule; and the ONE quantified
change-on-strong-beat prior: **changes of harmony at 71.5 % of above-tactus beats / 22.3 % of tactus /
2.4 % of sub-tactus** (Temperley 2009, Kostka-Payne). Masada's −5.9 pp accent ablation (F6) is the
measured magnitude on chorales.

**Triage input:** our two metric-weight tables (the OI-86 duplication) — **keep form** (beat-type →
weight is exactly q(·|ω)), **unify per #6, fit values**; the Round-1 on-beat hard filter → becomes the
soft change-on-strong-beat prior (the 71.5/22.3/2.4 pattern is the established shape; our corpus fit
supplies chorale values).

### F8 — fermata / phrase priors

**Established (FACT):** the convention is real and load-bearing in the literature — "fermatas in Bach
chorales indicate the end of each musical phrase" (DeepBach, conditioning variable; BachBot, token,
"more realistic phrase lengths"; de Clercq: fermatas delineate phrases but the cadential arrival can
shift to the prior strong beat when the fermata is metrically weak — documented failure mode). **No
analysis system uses fermatas as cadence-location priors (FACT-of-absence)** — the factor is novel in
direction but its premise is the best-documented convention in the repertoire (2,124 events counted).

**Triage input:** fermatas are currently UNREAD on the live path (evidence-inventory row). A's factor:
segment-boundary + cadence-location prior at fermatas, weak-beat displacement handled per de Clercq.
Low-risk, high-precision clue; needs a fire-rate prediction (#17b) before weighting.

### F9 — bass / inversion emission

**Established forms:** Ni et al.'s **p(b | c)** ("captures chord inversions"; top-3 constraint ≈
root/1st/2nd inversion — FACT) + bass-continuity p(b | b̄), inside the joint decode; measured: the
chord-conditioned bass chain is worth ≈10 pp of bass accuracy (83.8 vs 73.6, audio). Figured-bass
tradition (C.P.E. Bach 1753, Arnold 1931 via Ju et al. ISMIR 2020) is the THEORY that bass+figures
determine inversion; Ju's BCFB (139 chorales with Bach's OWN figures) exists as a resource. **No fitted
symbolic P(bass degree | chord, inversion) table for chorales is published (FACT-of-absence)** — but
its form is fully determined by the audio analogue and the theory; fitting it is routine.

**Triage input:** our bass-root bonus family / inversion bonuses / Gate I / bias correction are ad-hoc
additive stand-ins for a categorical emission — **keep the evidential content, refit as p(bass | chord,
inversion)**; Gate I's threshold (0.45 Baroque-calibrated) dissolves into the fitted table at adoption.
Note: Bach's own figures (BCFB) overlap our corpus — a potential established GT source for this factor
alone.

### F10 — (tonic, mode) transition

**Established forms (FACT, all fetched):** flat stay/switch (Temperley .8 / .2/23 — explicitly flagged
by him as oversimplified); Krumhansl-correlation-derived table (Noland & Sandler — relative-key
affinity EMERGES from the profile correlations, 0.651 max; 91 % Beatles keys); **circle-of-fifths
distance cost i^1.1** (Rocher et al. 2010 — the published CoF-weighted form); learned 24×24 MLE + count
pruning (Ni); transposition-invariant interval table (Raphael-Stoddard — who could not reliably estimate
it and hand-set it, FACT). **Measured warning for the fit discipline (Noland, FACT): re-fitting the
EMISSIONS of a key HMM collapsed accuracy 91 % → 18–28 %** (the states stop meaning keys) — a published
instance of what may NOT be blindly re-fit.

**Triage input:** our decoder change cost **2.0 + 0.60·cofDistance (+2.0 relative-pair)** is squarely in
the Rocher/Noland form family — **keep form, fit values** (they are hand-set, OI-91/OI-97). The
relative-pair special case has published support (Noland's correlation table; de Clercq's mediant
priority in minor). Asymmetric (sharpward/flatward) refinements: no published form (FACT-of-absence). *Update 2026-07-19
(user-supplied PDFs, `docs/research_papers/`): the Catteau et al. form is now VERIFIED —
**P(Cₙ|Cₙ₋₁) = exp(−d(Cₙ,Cₙ₋₁)/d_norm,C)** and **P(Sₙ|Sₙ₋₁) = exp(−d(Sₙ,Sₙ₋₁)/d_norm,S)**, exponential
in the Lerdahl Tonal-Pitch-Space distances (within-scale chord table with non-diatonic entries γ=9,
δ=2γ; each row normalized to sum 1; chord-in-scale fit P(C|S) as a profile inner product; a single
one-stage Viterbi over (scale, chord) — untrained, "requires no explicit training" confirmed). And
Chew 2002 (spiral array) is now fetched: key boundaries as the distance-minimizing segmentation of the
center-of-effect trajectory — a geometric, non-probabilistic F10 relative.*
**Mode-vocabulary input for the user:** every fetched key-transition model is over 12×2 states; the
exotic-mode states have no literature basis as TRANSITION states (they can still exist as EMISSION
variants — that split is exactly the user's OI-174/OI-132/OI-147 decision).

---

## 2. The ground-truth ceiling (OI-179, literature half) — and the BCMH verdict

**FACT-of-absence (the central finding):** no published study reports per-axis inter-annotator agreement
for RN/key annotation of Baroque/classical symbolic music. TAVERN has duplicate annotations but
published no number; ABC split pieces between annotators (no overlap by design); the Mozart sonatas
corpus is consensus-built (agreement unmeasurable post hoc); When in Rome 2020/2023 states the variance
is unmeasured; Dilemmadata (2026) identifies 84 dual-annotated pieces and computes nothing yet.

**The quantified bounds that DO exist (all FACT, different domains):** rock symbolic-by-ear, 2
annotators (de Clercq & Temperley 2011): **root 92.4–94.4 %, key 97.3 %**; pop audio, 4 annotators
(Koops 2019 CASD, duration-weighted): **root 0.76**, maj/min 0.73, +inversion −5 pp, tetrads 0.57;
Krippendorff's α clears 0.667 only for root. Axis ordering is invariant everywhere: **root/key ≫ full
label; inversion always costs ~5 pp; quality is the most subjective axis.** CONJECTURE (well-grounded):
clean-score chorale annotation should sit above the audio figures, plausibly near the de Clercq-Temperley
band — but it is UNMEASURED, which is precisely OI-179's point.

**BCMH:** independent in origin (FACT: the PeARL lab "encoded" its own key+RN annotations on KernScores
note data, borrowing only the DCML syntax; one `**harm` spine per chorale; no fetched source links its
content to any existing analysis). **Unestablished as an instrument (#19):** annotator count/identity
and validation are UNKNOWN (the JEP:HPP Method section and the dataset zip's headers are the two places
that would settle it — the zip is fetch-blocked in this environment but downloadable on the user's
machine); the annotations sit on a homorhythmic REDUCTION (unit mismatch with our full-texture grading
must be handled in the measurement design); they reached the repo through a machine translation into
rntxt (Nápoles López), whose noise would be part of any measured disagreement. **Consequence:** the
87-stem two-annotator measurement is feasible, would be a figure the field has not published, and its
instrument-establishment steps are: (a) read the BCMH zip headers / the 2023 Method section; (b) declare
the reduction-alignment convention; (c) treat translation noise as a named component. Feeds OI-179;
the measurement itself stays read-only and does not touch the robust stop.

*Update 2026-07-19: the user downloaded the dataset to `tools/BCMH_dataset/` and Cowork read it at the
files — step (a)'s zip half is DONE and NEGATIVE: `annotated/` holds 100 reduction files with the
`**harm` spine, `original_KernScores/` the 100 sources, and **no file carries an annotator record** (the
only editor records are Craig Sapp's KernScores note-encoding provenance, grep-verified) — so annotator
count/identity remains UNKNOWN and the 2023 JEP:HPP Method section is the one remaining route. The local
originals do improve the measurement design: grading can target BCMH's own `**harm` spines directly,
removing or cross-checking the WiR machine-translation noise component (caveat (c)).*

---

## 3. The fitting parameterization (arch doc §5/§6 question) — what the literature establishes

**The theory (FACT at fetched sources):** discriminative conditional-likelihood fitting of a factored
sequence model is convex (fully observed labels), permits arbitrary overlapping theory-derived features,
and dominates asymptotically (Lafferty 2001; Ng & Jordan 2002); generative ML/EM reaches its (higher)
asymptotic error with far fewer samples (log vs linear in parameter count). The semi-CRF objective +
L2/Gaussian prior + L-BFGS is the established segmental instantiation (Sarawagi & Cohen; Sha & Pereira
for the prior; Sutton & McCallum: σ² insensitive within ~10×; regularization makes the objective
strictly concave).

**The measured smalldata record (FACT):** at 18 training songs a generative HMM still beat the CRF
(Burgoyne 2007, with explicit CRF over-training countermeasures); at 46 heterogeneous excerpts hand-set
theory weights (Melisma) beat BOTH learned systems; at 60 Bach chorales the L2-regularized semi-CRF won
clearly (+6.2 pp over structured perceptron, tenfold-CV × 10 reshuffles, and 10× lower run-to-run
variance). **Nothing fetched fits a joint (tonic, mode, chord) model discriminatively at ~300-piece
scale — our fit would be past the measured crossover but in unmeasured territory (honest CONJECTURE).**

**The few-weight alternative (FACT):** Och 2003 MERT — 8 theory-derived weights fit on 640 sequences by
direct task-error minimization (Powell + exact line search, multiple restarts, bootstrap CIs), "no
serious overfitting" at that scale, with the explicit warning against many more parameters. This is the
established protocol if A's fitted surface is kept to tens of interpretable weights.

**What this hands the design pass:** two literature-established candidate protocols — (i) semi-CRF
conditional likelihood + L2 + piece-level k-fold (the Masada protocol, closest corpus match), (ii)
MERT-style direct search over few weights + bootstrap CIs (the Och protocol, matches #24's uncertainty
mandate natively) — plus three published guardrails that map onto our principles: piece-level splits
always (OI-176/#20); feature-support cutoffs and weight caps as small-data hygiene (OI-177); and
Noland's collapse warning (91 %→18–28 % when the wrong component is re-fit) as the canonical instance
of "what may be re-fit is itself a design decision." Generative-vs-discriminative is NOT decided here —
it is the arch doc §5 question, now with its evidence assembled.

---

## 4. The user's open decisions, as sharpened by this pass (brought, not decided)

1. **Mode vocabulary (OI-174/OI-132/OI-147): ✅ DECIDED 2026-07-19** — {major, minor} states, modal
   color in the emission, un-rounded modal reading published for the presentation layer
   (`cowork_joint_estimator_architecture.md` §5a).
2. **Fitting parameterization: ✅ DECIDED 2026-07-19** — staged: generative tables from counts
   (frozen), convex conditional-likelihood fit of the few combination weights, identity-weight
   generative baseline as mandatory ablation, assembly ledgered as our synthesis, fully-joint
   discriminative fit recorded as the unconstrained alternative
   (`cowork_joint_estimator_architecture.md` §5a).
3. **The degree-state question (CC gap-map group 1): ✅ DECIDED 2026-07-19** — scale-degree-valued
   chord state (Roman numeral relative to tonic and mode); chord symbol as the derived published fact;
   applied-degree classes for tonicization; root-valued state and momentary modulation recorded as
   excluded alternatives (`cowork_joint_estimator_architecture.md` §5a).
4. **Non-chord-tone handling placement: ✅ DECIDED 2026-07-19** — no live cleaning stage; non-chord
   tones as emission categories with chord-independent melodic/metric covariates; ornament labels
   derived post-decode and published; per-style adaptation through table values only
   (`cowork_joint_estimator_architecture.md` §5a).
5. **The signature/declared-mode prior: ✅ DECIDED 2026-07-19** — weak fitted transposition-invariant
   soft prior, no conditional gate (the probability calculus confines its influence to ambiguous
   regions), signature-influence rate published at every fit, declared-mode wall retired
   (`cowork_joint_estimator_architecture.md` §5a).

*All five design decisions of this section are ratified as of 2026-07-19 — the record is
`cowork_joint_estimator_architecture.md` §5a; what remains for the structure-design step is listed in
that document's §5.*

---

## 5. Source register

Fetched primary sources (FACT-grade citations live in the sections): Pardo & Birmingham CMJ 2002 ·
Raphael & Stoddard ISMIR 2003 (equations OCR-garbled, structure from prose; CMJ 2004 paywalled) ·
Temperley ICMAI 2002 + Temperley & Sleator CMJ 1999 + Temperley JNMR 2009 + "What's Key for Key?" 1999
(partial) · Ju et al. ISMIR 2017 (NCT) · Illescas et al. ICMC 2007 · PKSpell ISMIR 2021 · Meredith ps13
ESCOM 2003 · Micchi et al. TISMIR 2020 · Ni et al. arXiv:1107.4969 (TASLP 2012 version paywalled) ·
Rohrmeier DCRR-004 2006 (ICMPC 2008 blocked; same corpus analysis) · Harasim et al. ISMIR 2018 ·
Rohrmeier 2011 rules via TU-Dresden reproduction (JMM original paywalled) · Tsushima et al.
arXiv:1708.02255 · Masada & Bunescu TISMIR 2019 · Yang et al. (Harana) ISMIR 2023 · Korzeniowski &
Widmer ISMIR 2018 · Noland & Sandler ISMIR 2006 · Rocher et al. ISMIR 2010 · Bigo et al. ISMIR 2018 ·
Karystinaios & Widmer ISMIR 2022 · Sears et al. JNMR 2018 (partial) · de Clercq EMR 2015 ·
Hadjeres et al. (DeepBach) ICML 2017 · Liang et al. (BachBot) ISMIR 2017 · Ju et al. ISMIR 2020 (BCFB) ·
Nápoles López et al. (AugmentedNet) ISMIR 2021 · TAVERN ISMIR 2015 · ABC Frontiers 2018 · Mozart
sonatas TISMIR 2021 · Chen & Su ISMIR 2018 · When in Rome TISMIR 2020 + 2023 · Dilemmadata arXiv 2026 ·
de Clercq & Temperley PM 2011 · Koops JNMR 2019 (+ Utrecht TR CS-2017-018) · Humphrey & Bello ISMIR
2015 · BCMH repo + issue #1 + PeARL lab page + PubMed 37227858 · Lafferty et al. ICML 2001 · Ng &
Jordan NIPS 2001 · Sarawagi & Cohen NIPS 2004 · Sha & Pereira NAACL 2003 · Sutton & McCallum tutorials
2006/2012 (2012 truncated) · Och ACL 2003 · Burgoyne et al. ISMIR 2007 · Sheh & Ellis ISMIR 2003.

**Closed 2026-07-19 by user-supplied PDFs (filed at `docs/research_papers/`, indexed in its README):**
Feisthauer et al. SMC 2020 (§F4 forms verified); Catteau et al. GfKl 2006 (§F10 exponential-in-Lerdahl-
distance verified); Teodoru & Raphael ISMIR 2007 (§F3 spelling|local-key HMM verified); Chew 2002
spiral-array key boundaries (§F10 note); Sears et al. 2023 JEP:HPP (BCMH statistics FACT-grade — 100
reductions, NCTs excluded by construction, 10,056 chord tokens / 149 unique types, 6,328/90 major vs
3,728/93 minor; **the Method section names NO annotator and no validation**, citing only Verbeten &
Sears 2019 for the corpus); Mauch & Dixon ISMIR 2010 (identified as the NNLS-chroma front-end paper —
peripheral); plus a cleaner Raphael & Stoddard ISMIR 2003 copy (prose claims re-confirmed verbatim;
equation numerals still extract garbled — the parameter counts stay flagged as reconstructed). The
BCMH dataset zip was also user-downloaded and inspected (§2 update): no annotator record in any file.

**Still unfetched/unverified (no equation carried):** Krumhansl 1990 / Temperley 2001 / 2007 (books);
Verbeten & Sears 2019 (SMPC presentation — the one remaining route to BCMH's annotator identity,
likely only via the PeARL lab directly); Mauch & Dixon TASLP 2010 (the DBN paper — distinct from the
filed ISMIR one); the Rohrmeier & Cross ICMPC 2008 text (its substrate DCRR-004 is fetched); Ni et al.
TASLP 2012 published version; Raphael & Stoddard CMJ 2004.
