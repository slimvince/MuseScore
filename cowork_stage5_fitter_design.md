# Stage-5 Weight-Fitting ("the fitter") — Design

> **Status: SIGNED (user, 2026-07-04).** The full §15 sign-off surface (A-1, A-2, A-4, A-5, A-6, A-7ask,
> A-8ask, A-9ask) ratified 2026-07-04 ("ok then, forward!" + the A-3 selection); **A-3 RULED: defer the
> Jazz-carrier fit** — the idiom-#2 target (Baroque/Default carriers) is fitted now; the Jazz fit waits
> for a licensed jazz ground-truth conversion (D-5 option i). Drafted, independently audit-folded (20
> findings), and user-refined (idiom axis; style-table model; coordinate/estimation refinements) the
> same day. The Stage-5 arc's design
> document, written per the handoff's NEXT directive (2026-07-04) under the two user-ratified binding
> constraints: the **fitting-pool license constraint** (census §8c, 2026-07-04) and the **A-8 dual-track**
> metric semantics (2026-07-03). Template: `cowork_design_doc_template.md` (all 14 sections; arc42
> Deployment view and Human-interface design are N/A — backend analysis module, no deployment topology,
> no UI — stated once here). No code accompanies this document; CC instructions are written just-in-time
> after ratification, one at a time. **The first CC dispatch of this arc must also demand the
> acquisition-round fold-commit SHA (owed, never stated — the 22g precedent: a commit is verified at its
> object or its SHA is demanded).**

---

## §0 TERMS

Every term below is either standard music theory in its standard sense, defined here, or cited to the
document that defines it. Nothing is used before its row. Words with more than one plausible reading are
pinned to ONE sense for this document.

| term | sense in this document |
|---|---|
| **the fitter** | The Stage-5 component this document designs: the machinery that replaces hand-chosen numeric constants in the harmonic-analysis scoring pipeline with values optimized against the declared objective, under the declared constraints. |
| **constant / parameter** | A numeric value in the scoring pipeline that was chosen by hand (a bonus, penalty, threshold, weight, squash constant, or override factor θ). "Parameter" is used once the constant is under the fitter's management. |
| **objective** | The single quantity the fitter maximizes: duration-weighted **root agreement** on the robust unit under variant (b), measured on the fitting split of the licensed pool. Declared fully in §4.2, including the scope of every constraint attached to it. |
| **robust unit** | The granularity-robust **union-of-boundaries cell**: overlay our region boundaries with the human-annotation row boundaries; each resulting half-open tick span is scored once and weighted by its duration. Defined and measured in `cc_a8_rebaseline_measure_report.md` §1.1. |
| **variant (b)** | The adjudication rule "human annotation only, no music21 anywhere": each cell is scored directly against the WiR human annotation. (Its ratified name elsewhere is "variant (b) DCML-only", where "DCML" names the *annotation format*; this document says "variant (b)" to avoid the corpus/format ambiguity — see the DCML row.) `cc_a8_rebaseline_measure_report.md` §1.3. |
| **WiR human annotations** | The When-in-Rome human harmonic analyses of the reference corpus's Bach chorales (Roman-numeral text files in the DCML annotation format), license CC-BY-SA. The ground truth of variant (b). Coverage: 326 of the 352 corpus scores. |
| **DCML** | The Digital and Cognitive Musicology Lab. Used in TWO derived senses elsewhere in the project — (i) the *annotation format* the WiR analyses use, (ii) the lab's *Distant Listening Corpus*. In this document "DCML" appears only inside the fixed names "DCML annotation format" and the ratified variant name quoted above; the corpus is always called the DLC. |
| **DLC** | The Distant Listening Corpus: the 40 DCML-lab corpora held as research material. License class NC — **excluded from the fitting pool**, validation-only (§2 constraint 1). |
| **the reference corpus** | The frozen 352-score Bach-chorale regression corpus (per-preset dirs under `tools/corpus/`, manifest-stamped). Its established project name is "the gate corpus"; this document says "reference corpus" because "gate" is pinned to a different sense here (see the Gate A–L row). |
| **fitting pool** | The set of (score, ground-truth) sources whose data may shape ship-intended parameter values: the PD / CC0 / CC-BY(-SA) license classes only. Census §8c. |
| **validation pool** | Sources usable only for held-out validation, quality assurance, and statistics — never to shape a shipped parameter: all NC-class sources (the 40 DLC corpora, MCMA, Essen, …) and all no-license sources. Census §8c. |
| **fitting split / held-out split** | The division *within* the fitting pool: parameters are optimized on the fitting split only; the held-out split is never optimized against and is scored only at declared checkpoints (§4.2 declares the one deliberate exception). The split discipline is the ratified OQ-C1 rule (roadmap E2 line: dev/held-out, demotion only by recorded decision, registry `split` field). |
| **the batch stop** | The current hard regression stop: the batch-region BIR=false **case-identity sets** Baroque 53 / Jazz 24 / Default 53, with the two-tier class-(a)/(b) policy (CLAUDE.md). "Stop" is used, not "gate", to keep this word distinct from the senses in the next two rows. |
| **BIR / BIR=false** | "Bass-is-root" — the project's historical label for the batch metric's case class: a region where the analyzed bass is not the analyzed root and the analysis root disagrees with the adjudicated ground-truth root (the `bassIsRoot`=false half of the secondary metric's three-way split; CLAUDE.md). Appears only inside "the batch stop"'s definition and reports. |
| **Gate A–L** | One of the lettered post-scoring correction rules in the chord scorer (`docs/scoring_model.md` §6): rank-mutating swaps/pulls applied after template scoring. Always written with its letter or as "Gates A–L". **The live lettered set is A, E, F, the G-family (G-E/G-B/G-C/G-D), H, I, J, K, L — Gates B, C, D were removed at Stage 3.4b as provably dead code.** The §6 block also contains unlettered members (the bias correction, the FM2 fallback); the dissolution scope in §4.4 is the whole block, lettered or not. (Gate R is NOT in this set — it is a scoring-time guard, see its row.) |
| **Gate R** | The rcb bass-chord-tone guard inside template scoring (`docs/scoring_model.md` §4) — a scoring-time entry condition, not a post-scoring rank mutation. Outside the §4.4 dissolution scope; its documented coupling to the temporal-signal migration is roadmap item 3.3. |
| **engage criterion G1–G6 / engage step E0–E5** | The ratified criteria (G1–G6) and staged plan (E0 dormant measurement → E1 wire default-off → E2 measured A/B → E3 default-on, a user event → E4 retirements → E5 seal) for switching the dormant chain on (`docs/implementation_roadmap.md`, ENGAGE CRITERIA block). Always written with the number. |
| **class (a) / class (b)** | The two-tier failure classes: class (a) = the sonority's root is pitch-class-undecidable by construction (symmetric or share-tone collections — a coin-flip between rotations); class (b) = the root is pitch-class-decidable and the analysis is functionally wrong. CLAUDE.md two-tier policy; per-cell test in `cc_a8_rebaseline_measure_report.md` §1.5. |
| **Class M / Class P** | The two admissible confidence classes of the confidence contract: Class M = a squashed decision margin (a rank statement); Class P = a calibrated probability (empirical correctness at that confidence). `cowork_confidence_contract.md` §2. |
| **reliability map** | The fitted monotone map from a layer's published Class-M confidence to empirical correctness, upgrading it to Class P. The map is part of contract obligation **C1**'s deliverable (curves + fitted maps); the C1 measurement arc delivered the curves, and the maps land here. |
| **frame / θ** | A declared cross-layer comparison (incumbent confidence, contradiction strength, conversion) and its override factor: an override fires if and only if the contradiction strength exceeds θ times the incumbent confidence, expressed in one scale. `cowork_confidence_contract.md` §4. Re-expressing θ against calibrated quantities is contract obligation **C2**. |
| **D-FS** | The contract §7 as-built delta "frame scales undeclared": the F-A/F-B contradiction quantities are unbounded while their incumbents are [0,1]. Closed in this arc (§4.5). |
| **A-7 mark** | The ratified review amendment: a preset or idiom without empirical ground truth carries the "empirically-unvalidated" mark until its ground truth exists (roadmap AMENDMENTS block; contract C4). |
| **idiom** | One of the FIVE ratified harmonic-progression idioms (2026-06-30, empirically discovered and cap-robust): #1 Diatonic-functional, #2 Chromatic-functional, #3 Seventh-functional, #4 Triadic-modal, #5 Chromatic-coloristic, plus the two separate cross-attributes mode and chromaticism (`cowork_style_taxonomy_proposal.md`). The idiom is the project's structural style axis — genre/era is NOT an axis (Baroque, galant and Classical share idiom #2). |
| **preset** | A named configuration of scoring preferences (Baroque, Jazz, Default) — the LEGACY style carrier, predating the idiom taxonomy. Under the ratified taxonomy a preset is a **named idiom-weighting** ("presets = idioms, for now": the user selects an idiom directly; genre-named mixtures are deferred). In this arc presets remain the runtime delivery mechanism, but the style identity of every fitted value is the IDIOM (§9 D-10). Baroque-tuned values are never widened to cover another style (CLAUDE.md). |
| **fit target** | The unit a style-varying fit is performed for: an (idiom, ground-truth pool) pair, delivered at runtime through the preset carrier(s) mapped to that idiom. The Bach-chorale fit is an idiom-#2 fit delivered via the Baroque and Default carriers (§9 D-10). |
| **style coordinates** | The full style position of a piece under the ratified taxonomy: its weighting over the five harmonic idioms (the mixture simplex — a preset is a named point in it) plus the two cross-attributes (mode, chromaticism), plus — for parameters whose evidence is textural rather than progression-based — the **axis-2 texture class** (measured orthogonal to the harmonic idioms, cross-ARI 0.030). Which coordinates a given parameter's value may respond to is selected per parameter (§9 D-11 iv). |
| **stratum** | A declared sub-population of a fit target's covered scores sharing a style coordinate — e.g. the major-mode vs minor-mode chorales within the idiom-#2 pool. The unit of the style-response measurement (§4.4a). |
| **style-response structure** | Per parameter: the measured shape of how its fitted optimum responds to the style coordinates — **invariant** (no response) / **discrete table** (per-idiom and/or cross-attribute-conditioned values with measured borders) / **continuous** (interpolated over idiom-mixture coordinates from fitted anchor values). Decided by the §4.4a measurement, recorded in the manifest. |
| **production path** | The analysis path that runs by default and writes the shipped output and the reference-corpus `.ours.json` today. Note it is NOT "legacy everywhere": the rebuilt L1–L3 are live in production; "production" = the current default composition (live rebuilt layers + the legacy chord competition + the post-scoring correction block). |
| **dormant chain** | The rebuilt L1→L2→L3→L4-decoder→L5 spine measured end-to-end by engage step E0: built, validated, default-off, awaiting the engage criteria. |
| **fit surface** | The set of (parameter × consuming path) pairs the fitter may change — which constants, read by which paths (production / dormant chain / both). Established by measurement in Phase 0 (§4.1), not assumed. |
| **adoption event** | The deliberate, user-ratified act of committing a fitted parameter set as the new behavior (each one a revertible commit with a measured before/after). No fitted value changes behavior without one. |
| **sensitivity** | The measured change in the objective per unit perturbation of one parameter, all others held — the quantity that ranks parameters by leverage and detects dead constants. Measured in Phase 1 (it requires the harness; §4.1/§4.3). |
| **"gated on X" (participle)** | Used only in its ordinary English sense "conditional on X" (e.g. "flag-gated", "ratification-gated"). Never a noun sense. |

Cross-document handles used with citation only (each expands at its source): **E-13/E-14** = binding items
of `cowork_product_tool_register.md` (E-13: the tuning bridge is a consumer-migration site; E-14: zero
information loss to the end user); **the 22b/22f/22g precedents** = STATUS.md session rulings cited where
used.

---

## 1. Introduction & purpose

**What this is.** The scoring pipeline's numeric constants — template bonuses and penalties, the
progression-signal weights, the post-scoring correction thresholds, the confidence squash constants, and
the two override factors θ — were all chosen by hand against small case sets. Stage 5 replaces hand-tuning
with fitting: the constants become parameters optimized against a declared, ratified objective on licensed
data, under hard regression constraints, with every adoption a deliberate user event.

**Why it exists (the problems it solves).**
1. **Hand-tuning has stopped scaling.** The scoring model's own record (`docs/scoring_model.md` §8) lists
   repeated failed hand-adjustment attempts; the roadmap froze template work "until Stage 5 (fitting makes
   template ambiguity tractable)".
2. **The post-scoring correction layer is structural debt.** The `docs/scoring_model.md` §6 block (Gates
   A–L and its unlettered members) is a set of post-hoc rank mutations patching systematic scoring biases
   case-family by case-family. Dissolving it into fitted weights is **OWED refactor #2** (standing mandate
   2026-06-14); this arc is its named discharge point (retirement map R1: "Gates A–L — E4, or Stage 5 if
   first").
3. **The confidence contract's calibration obligations are due here.** C1's curves are measured
   (`cc_c1_reliability_report.md`) but C1's fitted reliability maps remain; C2 (θ re-expression) and the
   C3 joint-step design are assigned to Stage 5 (`cowork_confidence_contract.md` §6).
4. **The metric arc ends here.** The ratified A-8 dual-track holds "until the Stage-5 fitter lands"; at
   adoption, retirement item R10 fires and the robust unit becomes the governing regression stop.

**Scope (in).** Parameter inventory; the fitting harness and sensitivity measurement; fits of the
existing constants per fit target (idiom-labeled, preset-carried — §9 D-10) where style-varying and once
where style-invariant; the one commissioned NEW parameter deferred to this arc by ratified record (the
L5 §15-13 preference-among-licensed weight — §4.4 family 4); the §6-block dissolution audit; reliability
maps (completing C1); θ re-expression + the D-FS scale declarations (C2); the R10 re-baseline decision
surface.

**Scope (out).** The C3 gated joint key↔chord step (its own design document, gated on this arc's
calibrated quantities — §11); joint segmentation (deferred past Stage 5, roadmap); the `chordanalyzer.cpp`
file split (OWED refactor #1 — **parked by ratified R9**: after the E4 removals, "split once"); new
templates or new inference *signals* (template work becomes tractable after fitting; it is a separate
later decision; the §15-13 weight is a fitted preference over an existing decision structure, not a new
signal); candidate levers R-1…R-10 (none commissioned; §14 disposes R-11/R-12/R-13, the three
Stage-5-neighborhood method levers); the engage decision itself (E3 is its own user event).

**Status.** DRAFT for sign-off. No implementation exists; locators are deferred until built.

---

## 2. Constraints

1. **★ The fitting-pool license constraint (user-ratified 2026-07-04; census §8c; binding).** Parameter
   values intended to ship are fitted **only** on the fitting pool (PD / CC0 / CC-BY(-SA)): the reference
   chorales (PD scores) with their WiR human annotations (CC-BY-SA), and — when their ground truth is
   conversion-ready — CoCoPops, BCFB, GuitarSet, OpenEWLD, OpenScore. The validation pool (all NC-class:
   the 40 DLC corpora, MCMA, Essen, Chordonomicon, NC ChoCo partitions; all no-license sources: Mikrokosmos,
   Batik, iRb, …) may validate, QA, and inform statistics but must never shape a shipped parameter.
   Measurement ground truth is not a shipped parameter — the A-8 metric may keep its adjudication sources.
   **The census requires the design doc to declare its objective-vs-validation source split: §2 states the
   constraint and §3a carries the full declaration table** (placement note: the census wording says "§2/§6";
   this document's data declaration lives in §3a and §7, which are its data-declaration homes — recorded so
   the deviation is deliberate, not drift). The constraint also enters the roadmap Stage-5 block at this
   arc's first CC docs commit (census §8c ride).
2. **★ The A-8 dual-track (user-ratified 2026-07-03; binding).** The objective's basis is the robust unit
   under variant (b), **root governs, RN and key always tracked beside it**. Until the fitter lands, the
   **batch stop is THE hard regression stop** (case-identity sets 53/24/53 + the two-tier policy, R10
   unchanged). When the robust unit governs (at R10), the hard stop becomes **class-(b) root-disagree
   duration non-increase per preset** plus a **mandatory explained per-run set-diff**.
3. **The two-tier class policy carries over unchanged** (CLAUDE.md): zero new class-(b) cases on any preset
   at any adoption event; class-(a) additions only under the five guardrails (score-verified per case,
   doubt defaults to class (b), class-(b) non-increasing, identities recorded, interim-only).
4. **Preset policy (CLAUDE.md):** presets are fitted separately; a Baroque-tuned value is never widened to
   accommodate another style; a cross-style problem is solved by a structural entry condition or a
   preset-specific override.
4b. **The idiom taxonomy governs the style axis of fitted values (ratified 2026-06-30; contract C4).**
   Style-varying parameters vary **per idiom**, not per genre-named preset: every fitted value is
   idiom-labeled (§9 D-10), the manifest classifies each parameter's style scope (§4.1), and calibration
   is measured "per preset/idiom where the idiom changes the scorer's behavior" (contract §6 C4). A
   per-idiom fit exists only where that idiom has licensed ground truth; idioms without it keep the A-7
   mark (the taxonomy's own caveat: jazz/pop idioms are analysis-USE-unvalidated until their GT exists).
4c. **★ OPTIMIZE FOR IDIOMS ONLY — NEVER FOR THE CURRENT USER SETTINGS (user mandate, 2026-07-04).**
   The fitting objective is always an idiom's objective (its ground-truth pool); a genre-named preset is
   NEVER an optimization target — presets enter evaluation exclusively as regression surfaces (the
   configurations users can select today must not change silently) and as delivery carriers of
   idiom-labeled fits. There is consequently ONE fit per idiom, not one per carrier (D-4: the Baroque and
   Default carriers both deliver the single idiom-#2 fit; the Jazz carrier receives no fit until the
   idiom-#3 target exists). What is END-USER-FACING (which presets exist, what they are named, how they
   weight idioms) is a SEPARATE, LATER product decision — the taxonomy's deferred preset→idiom-weighting
   migration — and nothing in this arc pre-empts it.
5. **Knowledge-based coding / measure-first:** every fitting decision is gated on a measurement that
   precedes it (Phase 0's inventory + cost numbers gate the harness design; Phase 1's sensitivity numbers
   gate the optimizer choice and family staging; a differential report gates each §6-block retirement).
   No production value changes on an assumption.
6. **Held-out discipline (OQ-C1):** the held-out split is never optimized against; it is scored only at
   adoption events and declared checkpoints; demotion of a held-out item happens only by recorded decision
   (registry `split` field). §4.2 declares the one deliberate, bounded exception (the adoption-time
   full-corpus batch-stop check) and why it is accepted.
7. **Adoption discipline / no surprises:** infrastructure increments are byte-identical with proof
   (sandwich: the batch stop measured before and after, standard output byte-compared); behavior changes
   happen only at adoption events — each one revertible, measured per preset on both metric tracks, and
   user-ratified.
8. **Zero information loss (E-14, user principle):** calibration re-scales confidences; it never prunes
   the ranked alternatives a layer publishes. A reliability map is a monotone re-labeling, not a filter.
9. **Documentation in lockstep:** any commit touching a scoring term updates `docs/scoring_model.md` in the
   same commit (CLAUDE.md sync rule); the confidence contract's §3/§5 rows update when squashes or θ gain
   fitted values; this document flips to AS-BUILT status at landing.
10. **Total unification:** the fitter reuses the pinned measurement instruments (`tools/
    a8_rebaseline_measure.py`, `tools/c1_reliability.py`, `characterise_bir_false.py`) as its objective and
    calibration reader — it must not re-implement scoring or comparison logic; every CC increment reports
    reuse-vs-new and what retires.
11. **Full test coverage** of new fitter code paths at each increment (standing objective 2026-06-21).
12. **Fork-only:** everything stays on `origin` (`slimvince/MuseScore`); never `upstream`.

---

## 3. Context & scope (external view)

**Imports / consumed inputs.**
- **The reference corpus** (352 scores) and its **WiR human annotations** (326/352 coverage) — the fitting
  pool's current entirety (§3a below).
- **The pinned measurement instruments:** `tools/a8_rebaseline_measure.py` (the objective's measurement —
  self-validating against the pinned grid primitive on every piece), `tools/c1_reliability.py` (reliability
  curves), `tools/characterise_bir_false.py` (the batch stop; refuses unmanifested or contaminated dirs —
  a harness requirement, §4.3), `tools/run_bach_preset.py` (regen).
- **The C1 evidence** (`cc_c1_reliability_report.md`): per-(layer × decision × preset) reliability curves,
  the calibration facts its §5 recorded for this arc.
- **The parameter sites** (inventory owed to Phase 0; the two known homes are the chord scorer
  `src/composing/analysis/chord/chordanalyzer.cpp` + `postscoringgates.cpp` and the preset definitions in
  `tools/batch_analyze.cpp`; the D-FS/θ sites are the contract §4 frame call sites; the L5 §15-13 site is
  the function resolver).
- **The confidence contract** (`cowork_confidence_contract.md`): class definitions, frames, squash rules,
  the C1–C4 obligations.

**Exports / products.**
- **The parameter manifest** (§7): the authoritative enumeration of every fitted or deliberately-frozen
  constant with site, family, preset scope, and license provenance.
- **Fitted parameter sets per fit target** (idiom-labeled, delivered via the preset carriers), each
  adopted (or rejected) at its own adoption event.
- **Reliability maps** per (layer × decision × preset) — completing C1's deliverable.
- **Fitted θ + declared squash scales** for frames F-A and F-B (C2; closes D-FS).
- **Per-rule differential reports** and the §6-block retirement verdicts (R1 discharge).
- **The R10 re-baseline decision surface** — the measured material for the user's deliberate switch of the
  governing regression stop to the robust unit.

**Consumers.** The production path (fitted scoring constants); the contract §4 override sites (fitted θ);
the engage arc — engage criterion G2 compares the dormant chain against the legacy path on the robust
unit, so a fitted dormant chain is G2's candidate; Stage 6 (consumes calibrated confidences); the C3
joint-step design (gated on calibrated quantities existing).

**Explicitly not depended on:** music21 as an adjudicator anywhere in the objective (variant (b) is the
basis); the validation pool for any parameter value; the engage decision (the fitter measures both paths
where the fit surface touches both — §9 D-9 — but never flips the default).

**§3a The declared objective-vs-validation source split (constraint 1's required declaration).**

| role | sources | license basis | what it may do |
|---|---|---|---|
| **Objective (fitting split)** | The reference-corpus chorales WITH WiR annotations, fitting-split members only (split defined in Phase 1; registry `split` field) | scores PD; WiR annotations CC-BY-SA | shape parameter values |
| **Objective (held-out split)** | The remaining WiR-annotated reference-corpus chorales | same | adoption-event and declared-checkpoint scoring only; never optimized against (§4.2 exception declared) |
| **Deferred objective candidates** | CoCoPops, OpenEWLD, BCFB, GuitarSet, OpenScore sets — fitting-pool members whose ground truth is not yet conversion-ready | CC-BY / CC-BY-SA per census | none until a ratified conversion increment brings each in (per-source decision; Jazz-preset question §9 D-5) |
| **Validation pool** | 40 DLC corpora, MCMA, Essen + all other NC; Mikrokosmos, Batik + all other no-license | NC / none | style-generalization checks, QA, statistics; never shapes a value |
| **Measurement-only adjudication** | WiR (doubles as measurement GT); music21 (variant (a) continuity diagnostics only) | — | metrics and diagnostics; variant (a) never enters the objective |

**Locators.** Implementation and test locators are deferred (nothing is built); Phase 0's manifest becomes
the parameter locator; harness locators are added at the AS-BUILT flip.

---

## 4. Solution strategy

The fundamental shape: **inventory the parameter space, build the evaluation harness, measure sensitivity
through it, then fit family-by-family against one declared objective — retiring the post-scoring
correction rules as the fitted weights reproduce their fixes, and calibrating the surviving confidences
last — with the batch stop held as the tripwire throughout, and every behavior change a ratified adoption
event.** Five phases; each phase's *decisions* are gated on its predecessor's *measurements*. Two
ratification checkpoints (after Phase 0 and after Phase 1's sensitivity screen) keep the user's hand on
the decisions the measurements feed.

### §4.1 Phase 0 — inventory and cost (read-only; no perturbation)

Phase 0 contains only work that needs no new machinery:

1. **Parameter inventory.** Enumerate at source every hand-chosen numeric constant in the scoring pipeline:
   the §4 bonus/penalty terms and §5 joint terms of `docs/scoring_model.md`, the §6-block entry thresholds
   and margins, the per-preset values in the preset definitions, the confidence squash constants, the two
   frame θ values, the layer abstention bars, and the L5 §15-13 site (the both-licensed fall-through —
   family 4's home). Each row records: name, site, current value, the preset(s) it varies by, its
   **declared style scope** — style-invariant (a structural constant no idiom should move, with the
   rationale) vs **idiom-varying** (a value expected to differ by idiom — e.g. progression-signal weights;
   the A-10 rider already records the L4 membership tie-breaker as an idiom-calibrated constant) — the
   path(s) that read it (production / dormant chain / both — this establishes the **fit surface**), and
   any structural role that argues freezing it (§4.6). The style-scope column is a declared hypothesis at
   inventory time; the §4.4a style-response measurement replaces the declaration with a measured
   structure wherever strata exist (a "style-invariant" parameter whose per-stratum optima diverge is a
   flagged finding). The staleness check runs both ways: the inventory must
   reconcile with `docs/scoring_model.md` §2–§6, and discrepancies found are doc-drift defects fixed in the
   same arc. This step also verifies at source whether the fit surface touches the tuning bridge (E-13);
   if it does, that site enters the retirement map at this edit.
2. **Objective-evaluation cost.** Measure the wall-clock cost of one full objective evaluation per preset
   with the EXISTING machinery (corpus regen to a manifest-stamped scratch dir + robust-unit measurement +
   batch-stop check on that dir) — the number the harness design and the optimizer budget rest on. Both
   the per-preset case and the all-presets case are timed (shared-scope parameters need the latter — §4.2).

**Checkpoint P0 (ratification):** the fit surface, the freeze list, and the family homes — decided on the
inventory. (Sensitivity is NOT available yet; it needs Phase 1's harness. The optimizer and staging
decisions therefore sit at checkpoint P1, not here.)
**★ P0 RATIFIED (user, 2026-07-04):** the Phase-0 manifest's boundary adopted — 61 rows tunable / 17
frozen — **with the FROZEN-ROW VERIFICATION RIDER:** the Phase-1b sensitivity screen also perturbs the 17
frozen rows (measurement only, nothing adopted), so a freeze that hides real accuracy surfaces as a
finding with its number rather than staying a trusted rationale.

Phase 0 is read-only: source reads plus timing runs of existing tools against scratch copies; the
reference corpus is never written; no parameter value changes anywhere.

### §4.2 The objective, precisely

For preset *p* and candidate parameter vector **w**:

> **maximize** duration-weighted root agreement — Σ dur(cells where our root pitch class equals the WiR
> root pitch class) / Σ dur(scored cells) — over the **fitting split's covered cells**, on the robust
> unit, adjudicated by variant (b).

**Per-evaluation hard constraints** (checked on every candidate, scoped to keep the held-out split out of
the optimization loop):
- **No new class-(b) batch-stop case among fitting-split scores** — the candidate's scratch output is
  checked against the fitting-split subset of the 53/24/53 case-identity sets, for the preset(s) the
  candidate touches. A parameter with shared preset scope is evaluated on every preset that reads it
  (the Phase-0 cost measurement priced this; family staging prefers preset-scoped parameters first).
- **Class-(b) root-disagree duration non-increase on the fitting split's covered cells**, same preset
  scope (the successor-stop semantics, tracked from day one so the R10 handover is continuous).
- Denominator scope declaration (the §2.1a lesson — every rate names its denominator): all per-evaluation
  quantities are over the fitting split's WiR-covered, parseable cells; key-parse-fail duration reported
  separately, never folded in.

**Per-adoption checks** (and at named family checkpoints): the FULL-corpus batch stop, all three presets,
sandwich form; the full-corpus robust-unit numbers on both tracks; the validation sweep (S-5).
**Declared held-out exception:** these adoption-time checks necessarily read held-out-score outcomes —
that is deliberate and accepted, because the hard regression stop outranks split hygiene (a candidate
that breaks a held-out case must never ship, and discovering that only after shipping would be worse than
the leakage). The leakage is bounded — it occurs only at the few user-ratified adoption events, each with
its diff explained and recorded — and it is one-directional (a rejection sends the fit back to the
fitting split; no held-out-derived gradient enters the loop).

**Tracked beside, never collapsed in (ratified respect semantics):** RN agreement (exact+partial) and key
agreement on the same cells, reported for every candidate — a fit that trades RN/key sharply against a
root improvement is surfaced to the user at the adoption event, not silently accepted.

**Class-(a) cells stay in the objective at full weight** initially: they are ~3.5–3.9 % of root-failing
duration under variant (b) (cell-count share ~3.6–4.0 %; both measured,
`cc_a8_rebaseline_measure_report.md` §4.2), too small to distort the fit, and excluding them would hide a
parameter change that destabilizes many symmetric sonorities at once (the two-tier policy's "large
class-(a) net increase trips investigation" signal). Revisit only if Phase-2 fits show class-(a) churn
dominating a fit direction (§15 O-2).

**Baselines the fit starts from** (variant (b), root-agree, full 326/352 coverage): Baroque **63.32 %**,
Jazz **62.37 %**, Default **63.22 %** (RN 44.56/42.40/44.40 %; key 68.11/64.43/67.50 %). The
fitting-split-level baseline is a different (narrower-denominator) number, defined when Phase 1 defines
the split; both are recorded in the fit ledger from day one.

### §4.3 Phase 1 — the fitting harness + the sensitivity screen

**1a — the harness (infrastructure; byte-identical).** A driver that: takes a parameter vector,
materializes it per D-6's declared shape (a flag-gated external override read by the analysis binary at
startup — the shape is decided, §9 D-6; only its file format and exact plumbing are Phase-1 implementation
details), regenerates the affected preset(s) to a manifest-stamped scratch dir that satisfies
`characterise_bir_false.py`'s validation (fingerprints + the `.music21.json` substrate present),
evaluates §4.2 via the pinned instruments, and logs (vector, objective, constraint status, tracked
respects) to a reproducible fit ledger. Requirements: deterministic (fixed seeds where the optimizer
randomizes; two identical runs produce byte-identical ledgers), sandwich-proven (override absent ⇒
byte-identical behavior; reference corpus untouched — all evaluation to scratch), reusing the §3
instruments verbatim. **1a also defines the fitting/held-out split** (registry `split` field, recorded
rationale).

**1b — the sensitivity screen (first use of the harness; decode-only, nothing adopted).** Perturb each
inventoried parameter one-at-a-time (a small ± step around its current value) and measure the objective
delta and the constraint status per preset. **Per the ratified P0 rider, the 17 frozen rows are included
in the screen (read-only)** — a frozen row with material leverage is reported as a finding, never
silently unfrozen. Deliverables: the leverage ranking (which parameters move the
objective at all), the dead list (candidates to "fit to zero"/retire, roadmap 5.2), the interaction
warnings (parameters whose perturbation flips §6-block rule firings — these must be fitted jointly with
the dissolution track, §4.4), and the frozen-row verification findings.

**Checkpoint P1 (ratification):** the optimizer choice (§9 D-3, decided on the measured cost and
sensitivity), the family staging order, the R-13 augmentation decision (§14), and the split definition —
all on 1b's numbers.
**★ P1 RATIFIED (user, 2026-07-04, on the Phase-1 measured surface — `cc_stage5_phase1_report.md`):**
(1) **the 261/65 mode-stratified fitting/held-out split RATIFIED** (`tools/stage5_split_registry.json`);
(2) **optimizer = coordinate/pattern search** (D-3's default, confirmed budget-feasible at ~45 s/eval,
~35 live rows post-dead-pruning); (3) **staging adopted:** the clean lever (`kPowerChord3PcPenalty`,
the one high-leverage row with zero batch-stop interaction) → the coupled continuous cluster (G1
tone factors + G2/G3 bass/root/inversion + G6) fitted JOINTLY with the §6-block dissolution track →
the G7 gate margins by pinned-fixture replay (Δ=0 at the objective's resolution) → abstention bars
last; (4) **R-13 augmentation SKIPPED** (the measured ceiling is coupling-limited, not data-limited);
(5) **the two rider-flagged frozen rows STAY FROZEN with corrected rationales** — `kOtherToneFactor`
= the tone-weight family's declared SCALE ANCHOR (a relative-weight system fixes one unit; its
leverage shows the anchor is load-bearing, not that it should float), `maxTotalInversionContextBonus`
= DELIBERATELY NON-BINDING at its current value (the individual bonuses are the tunable surface; a
floating cap coupled to the bonuses it caps is a redundant degree of freedom). The rationale
corrections ride the next manifest edit.
**★ PHASE 2.1 — THE FIRST FIT DELIVERED as a CANDIDATE (CC, 2026-07-05, `cc_stage5_phase2_1_report.md`;
awaiting Cowork verification):** the family-1 clean lever `kPowerChord3PcPenalty` fitted 1-D on the
fitting split (261, Baroque carrier) → **candidate 0.6375** (best feasible; fitting root +0.073). The row
is **constraint-bounded**: the unconstrained optimum (0.15, +0.376) is infeasible (adds class-(b) batch
cases), so the feasible fit is a modest raise. Decision surface: **held-out regresses −0.098 (overfit
signal)**; full-corpus +0.0376/+0.0854/+0.055 with **batch sets unchanged ×3** and class-(b) duration
down ×3; **D-4 Default adopt-with-Baroque eligible**; Jazz no regression; **S-5 candidate-scoring
instrument gap recorded** (no validation runner threads `--param-override`); snapshot preview ≈6/11
goldens would refresh at adoption. **The candidate + adoption artifact are PREPARED, not applied — the
adoption event (A-4/S-4) is the user's, separate from this fit.** The P1 rationale corrections landed in
that dispatch's manifest edit (`5c5d0aabdc`), values byte-untouched.

### §4.4 Phase 2 — the fits, family by family, per fit target

Style-varying families are fitted per **fit target** (an idiom with licensed ground truth, delivered via
its preset carrier(s) — §9 D-10); style-invariant families are fitted once, evaluated on every covered
target. Families in dependency order (checkpoint P1 may reorder on measured interactions; the order below
is the default hypothesis, stated so deviation is a flagged decision):

1. **Continuous scoring constants** (bonuses, penalties, joint-term weights): the classic fit; per fit
   target where idiom-varying, once where style-invariant (the manifest's style-scope column decides
   which, per §4.1).
2. **The §6-block dissolution (the R1 discharge).** Scope: the ENTIRE post-scoring correction block of
   `docs/scoring_model.md` §6 — the bias correction, the FM2 fallback, and the live lettered Gates (A, E,
   F, G-E/G-B/G-C/G-D, H, I, J, K, L; B/C/D are already gone, Stage 3.4b). For each rule, in the
   roadmap-3.4 discipline: (i) its pinned fixes (the Stage-1.1 test fixtures) are the proof obligations;
   (ii) attempt the fit *with the rule disabled* — the question is whether fitted continuous weights
   reproduce the rule's corrections without its rank mutation; (iii) a **per-rule differential report**
   (which corpus decisions change, class split, pinned-fix status) decides: **retire** (fixes reproduced,
   no class-(b) regression), **retain as structural rule** (the rule encodes a structural fact a
   continuous weight cannot — the roadmap expects Gate J, structural and healthy, to survive longest
   among the post-scoring rules; scoring-time guards like Gate R are outside this scope entirely), or
   **defer with the blocking interaction named**. Nothing retires by silence; each retirement is its own
   commit with the differential report.
3. **Abstention bars** (the per-layer "uncertain" thresholds — contract U5): fitted against
   correct-abstention vs wrong-commit rates on the C1 curves (abstention scored separately, the G2
   discipline).
**§4.4a The style-response measurement (per high-leverage parameter; the table-dimensionality
instrument).** For each parameter the sensitivity screen ranks as high-leverage, before its family fit is
adopted: (i) **fit its optimum per stratum** — the strata available today are the cross-attributes within
the idiom-#2 pool (major vs minor mode; a declared chromaticism split), and each new idiom target added
by O-5 contributes its idiom stratum; (ii) **cluster the per-stratum optima** and test the clustering's
stability (multi-seed, robustness across stratum re-definitions — the idiom-discovery study's own
robustness discipline, reused); (iii) **verdict = the parameter's style-response structure**: the optima
collapse to one value → invariant (its style dimensions drop away); they form stable clusters with clear
border values → a discrete table conditioned on exactly the coordinates that separate the clusters (if
the clusters cut ACROSS idioms — e.g. mode or texture is the real driver — that is a taxonomy-relevant
finding, surfaced, not smoothed into the idiom table); the spread is even with no stable clusters → a
continuous response, realized as interpolation over the style coordinates from the fitted anchor values
(§9 D-11). Two declared guards: per-stratum optima are noisy estimates (each stratum is a smaller fit —
the stability test, not the raw clustering, makes the verdict), and a stratum must meet a declared
minimum covered-duration to produce an optimum at all (an under-sized stratum is reported as
unmeasurable, never extrapolated).

4. **The L5 §15-13 preference-among-licensed weight — the one commissioned new parameter.** The 22b
   ruling deferred the resolver's preference order among multiple licensed progression readings "to
   Stage-5 weight fitting" (L5 §15-13); this arc owns it. Gated on its own cheap measurement first: count
   the both-licensed fall-through population on the reference corpus (decode-only); if the population is
   too small for a fit to be evidence-based (the count and its class split are the checkpoint material),
   the item returns to the user with the number and stays a recorded §15-13 open item — not silently
   dropped, not fitted on noise.

Each family lands as its own adoption event (or is rejected on its numbers).

### §4.5 Phase 3 — calibration (completing C1's maps; C2)

1. **Reliability maps (C1's remaining deliverable).** Per (layer × decision × fit target) — contract C4:
   calibration is measured per preset/idiom where the idiom changes the scorer's behavior, so the map's
   style identity is the idiom, like every other fitted value — fit a **monotone**
   map from published Class-M confidence to empirical correctness on the C1 substrate (isotonic regression
   as the default shape; Platt-style parametric where the curve is smooth; choice recorded per row). The
   C1 report's §5 facts bound what is fittable now:
   - **L3 key:** the map rides the **sequence margin** (ECE 0.125–0.142; the emission sigmoid is demoted —
     D-L3a closed).
   - **L4 chord composite:** the strongest candidate (ECE 0.11, monotone above ~0.5); its flat low band is
     mapped honestly (a wide flat segment, not invented resolution).
   - **L5 combinedBoundary:** **not Class-P-upgradable as-is** — non-monotone mid-range (the 0.6–0.8 band
     scores below the 0.5–0.6 band). The fitter records the calibration failure and the map is deferred;
     the inversion is an upstream inference-quality finding (declared to the user at the Phase-3
     checkpoint, not silently "fixed" by a non-monotone map).
   - **Cadence tonicVote:** anti-monotone with three distinct values — not calibratable; recorded as an
     upstream detection-quality item, out of this arc's scope (§11).
   - **L1.5 texture strength:** 97.7 % mass in one bin — insufficient spread; the spike-vs-surface split is
     evaluated as a Phase-3 measurement before any map is attempted.
2. **θ re-expression + D-FS closure (C2).** Declare the F-A (`cadentialWeight`, observed [3.25, 9.35]) and
   F-B (`bestPlaus − committedPlaus`, observed [2.0, 3.0]) contradiction scales; fix each frame's squash
   shape; re-fit θ against the calibrated maps so it reads as an odds ratio. The E0-measured override
   net-harm (968 fires / 45 corrections — recorded at contract §7 D-FS) is the acceptance reference:
   fitted θ must not score worse than the current constants on that same fires-vs-corrections measure.
3. **C3 unblocking (design only).** With calibrated quantities existing, the gated joint key↔chord step's
   *design document* becomes writable (its trigger is already defined, contract C3). Writing it is a
   separate, later Cowork task — named here as unblocked, not started.

### §4.6 What is deliberately NOT fitted

Structural predicates (template interval definitions, the class-(a) structural test, §6-block entry
*conditions* as opposed to their numeric thresholds, the outer-guard structure), the licensed-progression
grammar itself (L5 §5.0 — spec-owned; family 4 fits a preference *among* licensed readings, it does not
change what is licensed), and any value whose Phase-0 row names a ratified structural rationale. The
freeze list is part of the manifest and part of checkpoint P0.

### §4.7 Phase 4 — adoption and the R10 re-baseline

When the fitted families are adopted and the §6-block verdicts are in: assemble the **R10 decision
surface** — per preset, both metric tracks, before/after, the robust-unit baselines to adopt as the new
stop, the identity form (`stem@runStartTick`, the re-slice-stable form matching the ratified per-run
set-diff semantics; the A-8 instrument emits both forms), and the successor stop semantics (constraint 2).
The user ratifies the switch; the batch stop is retired **into** the robust-unit stop (case-identity +
two-tier policy carrying over) as one deliberate re-baseline event. Until that event, every increment of
this arc holds the batch stop.

---

## 5. Building-block view

| block | responsibility | consumes | produces |
|---|---|---|---|
| **Parameter manifest** | The single enumeration of fittable/frozen constants (§7 schema) | Phase-0 source reads | the fit surface; the freeze list |
| **Fitting harness** | Vector → materialized override → scratch regen (manifest-stamped) → objective + constraints → ledger | manifest, pinned instruments | fit ledger (reproducible); the split definition |
| **Sensitivity screen** | One-at-a-time perturbation measurement (Phase 1b, through the harness) | manifest + harness | leverage ranking, dead list, interaction warnings |
| **Optimizer** | Proposes vectors (family-scoped) | ledger | candidate parameter sets |
| **Differential reporter** | Per-candidate and per-rule decision diffs: batch-stop set-diff (explained), robust-unit run diff, class split, pinned-fix status | harness outputs | adoption-event / retirement evidence |
| **Calibration fitter** | Reliability maps + θ/squash fits | C1 harness outputs | Class-P maps, fitted θ, D-FS declarations |
| **Validation runner** | Scores adopted candidates on the validation pool (style generalization) | fitted sets, validation pool | per-style validation report (informative, never objective) |

All blocks are tools-side (Python + existing dump flags) except the parameter-override read in the
analysis binary (§9 D-6) — the one anticipated `src/` change, landing flag-gated + byte-identical (override
absent) before any fit uses it.

---

## 6. Runtime view (scenarios)

**S-1 One fit evaluation.** Optimizer proposes **w** for a family scoped to preset *p* (or to the preset
set reading a shared parameter) → harness materializes **w** → scratch regen of the affected preset(s) →
objective + per-evaluation constraints (§4.2 scopes: fitting split only) via pinned instruments → ledger
row. The reference corpus is never written.

**S-2 A rule-retirement audit (Phase 2, family 2).** Fit with rule X disabled → differential report:
pinned fixtures replayed (pass/fail per case), corpus decision diff classified (a)/(b), robust-unit delta
→ verdict retire / retain / defer → if retire: the removal commit carries the report, the rule's tests
convert to pinned-behavior-of-the-fitted-weights tests, `docs/scoring_model.md` §6 updates in the same
commit.

**S-3 A tripwire trip.** A candidate's scratch output adds a fitting-split batch-stop case classed (b) →
the candidate is rejected in the ledger (constraint violation), the fit continues elsewhere in the space;
no stop-and-ask is needed because nothing was adopted. If a *family's best* candidate trips it, that
finding goes to the user as the family's result (the family may be unfittable under the constraint —
itself knowledge).

**S-4 An adoption event.** Family fit complete → the §4.2 per-adoption checks (full-corpus batch stop ×3
sandwich, full robust-unit both tracks) + differential and validation reports assembled → user ratifies →
one revertible commit (parameters + doc sync + report) → STATUS/handoff fold per standing practice.

**S-5 Validation sweep.** After each adoption: score the adopted set on the validation pool per style
family (DLC sub-corpora as style probes) → report per-style deltas (informative). Any negative per-style
root-agreement delta (against that source's own ground truth, duration-weighted on pc-decidable
sonorities — the class-(b) analogue, so defined) is surfaced to the user as evidence for a structural
entry condition (constraint 4's preferred fix), never fixed by widening a fitted value. No numeric
threshold is imposed: every negative delta is surfaced with its size; the user decides.

---

## 7. Data design

**Parameter manifest row:** `name · site (file + anchor) · family (continuous / §6-block threshold /
abstention / §15-13 / squash / θ) · current value · preset scope (shared | per-preset) · style scope
(style-invariant + rationale | idiom-varying) · consuming path(s)
(production | dormant | both) · status (fit | frozen + rationale) · license provenance (filled at first
fitted value: which pool/split shaped it) · sensitivity (Phase-1b measurement)`.

**Fit ledger row:** `run id · preset(s) · family · vector · objective (fitting-split) · tracked respects
(RN, key) · constraint results (fitting-split batch set-diff summary, class-(b) duration delta) ·
timestamp · instrument versions`. The ledger is committed (it is the fit's provenance); large per-cell
enumerations stay regenerable scratch pinned by the driver, per the A-8 precedent.

**Fitted-set artifact:** per fit target: the idiom label, the preset carrier(s) it is delivered through,
the vector, its ledger reference, the adoption-event commit, and the license-provenance statement
("fitted on: reference-corpus fitting split (PD/CC-BY-SA), idiom #2 ground truth, only").

**Reliability-map artifact:** per (layer × decision × preset): map type, knots/parameters, the C1 substrate
reference, and the declared domain caveats (flat segments, deferred rows).

Ownership: all artifacts are tools-side files under version control; the pipeline reads adopted values from
its normal configuration sites (the adoption commit writes them there — the manifest cross-references, it
does not become a runtime dependency).

---

## 8. Crosscutting concepts

- **Determinism & reproducibility.** Regen is proven deterministic (the M3 arc); the harness adds: fixed
  optimizer seeds, committed configurations, byte-identical double-run checks on the ledger. Any
  nondeterminism found is a stop-and-investigate, never noise to average over — all comparisons in this
  arc are exact.
- **License provenance as a first-class property.** Every shipped parameter can answer "what data shaped
  you?" from the manifest + ledger. This is the mechanism that keeps commercialization from silently
  inheriting an NC-derived value (census §8c's stated purpose).
- **The no-surprise sandwich** (batch stop before/after + byte-identity where claimed) wraps every
  increment, infrastructure and adoption alike.
- **Honest failure reporting.** A family that cannot beat its baseline under the constraints, a rule that
  cannot be retired, a confidence that cannot be calibrated — each is a *finding*, reported with its
  evidence, never smoothed over (the C1 report's treatment of tonicVote is the model).
- **Error/edge handling.** Cells without WiR coverage are unscored, never mis-bucketed (the A-8 rule);
  key-parse failures reported separately (the §2.1a denominator lesson — every reported rate names its
  denominator, and §4.2 does).
- **Performance.** The harness is offline tooling; the only runtime-relevant change is parameter *values*.
  No performance budget changes in this arc.

---

## 9. Architecture decisions

**D-1 Objective = robust unit, variant (b), root governs; RN/key tracked.** *Alternatives:* multi-respect
weighted objective (rejected for now: the respect weights would themselves be unratified hand-tuning —
root-governs is the ratified semantics; RN/key visibility at adoption events covers the trade-off risk);
variant (a) (rejected: music21 is an algorithm, not ground truth; discards ~82 % of human-adjudicated
error time; root-only by construction). *Consequence:* the fit inherits the ratified metric exactly; no
new metric definitions enter this arc.

**D-2 The pool split per §3a.** *Alternative:* fit on everything and relicense later (rejected: the
constraint exists precisely to prevent that path-dependence). *Consequence:* today's effective objective
data is the WiR-annotated reference corpus; broadening it is per-source ratified work (D-5).

**D-3 Optimizer: decided at checkpoint P1, with the decision structure declared now.** The pipeline is a
discrete, non-differentiable decision cascade; the objective is evaluated by running it. *Default:*
**coordinate / pattern search** over family-scoped subspaces (derivative-free, constraint-friendly,
trivially deterministic, easy to ledger) — feasible if and only if the Phase-0 cost measurement allows
the implied evaluation budget. *Considered:* structured-perceptron-style updates (roadmap 5.1's other
name) — requires a per-cell decomposable loss and parameter-linear scores; adopted only if the budget
forces it AND the score's parameter-linearity holds on the fit surface. *Considered and deferred:*
CMA-ES/black-box global search (only if coordinate search stalls at a measured plateau). The choice is
made once, at P1, on the cost + sensitivity numbers.

**D-4 Style-varying fits are per fit target; Default's relationship to the idiom-#2 fit measured, not
assumed.** Style-varying families are independent fits per fit target (constraints 4/4b). Default's
batch-stop set differs from Baroque's by a two-case swap (four identities in the symmetric difference,
CLAUDE.md), and both carriers deliver the same idiom-#2 fit under D-10. The rule: evaluate the idiom-#2
fitted vector on the Default carrier; **Default adopts it if that evaluation improves Default's objective
over Default's baseline and trips no constraint** (exact comparison — the evaluator is deterministic,
there is no noise floor); a separate Default treatment runs only if the vector regresses Default or the
user asks. *Alternative:* always fit every carrier independently (rejected: carriers mapped to the same
idiom fitting the same data independently would differ only by optimizer path — a spurious divergence;
the measurement, not the history, makes the adopt-or-not call per carrier).

**D-5 The Jazz data question — surfaced, not decided here.** The Jazz preset's idioms (#3
Seventh-functional, plus #5 for its chromatic-coloristic material) carry the A-7 mark: no licensed
analysis ground truth exists for them yet, and the only objective data today is Bach chorales (idiom #2).
Fitting Jazz-carrier weights against idiom-#2 data contradicts both the mark's honesty and D-10's
idiom-labeling (the result would be an idiom-#2 fit mislabeled as a jazz style). *Options for
ratification:* (i) **defer the Jazz-carrier fit** until a fitting-pool jazz source (CoCoPops / OpenEWLD)
is conversion-ready — its own ratified increment, which creates the idiom-#3 fit target — fitting the
idiom-#2 target (Baroque/Default carriers) now; the design's recommendation, because it is the only
option that is licensed, honest, and idiom-correct; (ii) fit the Jazz carrier on Bach anyway and keep the
mark (records a number, changes little, mislabels the style axis); (iii) pull the jazz-GT conversion into
this arc (scope growth; the conversion is corpus work, not fitter work). **★ A-3 RULED (user, 2026-07-04):
option (i) — the Jazz-carrier fit is DEFERRED to the jazz-GT conversion increment (O-5's first
instance); this arc fits the idiom-#2 target.**

**D-6 Parameter materialization: a flag-gated external override read at startup — the shape is decided
now; only its details are Phase 1's.** The harness needs hundreds-to-thousands of evaluations;
rebuild-per-vector is infeasible. *Shape:* a parameter-override input (file or command-line) to the
analysis binary, default-off, byte-identical when absent — the same discipline as every dump flag.
*Alternative:* generated-header rebuilds (rejected on evaluation cost); direct Python re-implementation of
scoring (rejected: violates one-path-per-concern — the C++ pipeline IS the scorer). Phase 1 decides only
file format and plumbing within this shape.

**D-7 §6-block dissolution is an audited per-rule verdict, not a bulk deletion.** Per §4.4; the
roadmap-3.4 discipline with the Stage-1.1 pinned tests as proof obligations. *Alternative:*
delete-and-refit-globally (rejected: loses the per-rule causal account, risks laundering a regression
through aggregate numbers).

**D-8 Calibration maps are monotone or deferred.** A non-monotone empirical curve (L5 combinedBoundary) is
an upstream finding, not a mapping target — fitting a non-monotone map would launder an inference defect
into the confidence semantics. (Contract R4/R5 monotonicity carries this.)

**D-9 The fit surface includes both consuming paths where a constant is shared.** Where production and the
dormant chain read the same constant (a Phase-0 fact per manifest row), the fit evaluates the objective on
the **production path** (it is what the reference corpus and the stop measure) while the differential
reporter *also* tracks the dormant chain's robust-unit numbers (the G2 quantity) — so fitting never
silently degrades the engage candidate. The surfacing test: if the best production value increases the
dormant chain's class-(b) root-disagree duration on any preset, that conflict goes to the user (it is
evidence about the paths' divergence, relevant to the E-steps).

**D-10 The style identity of every fitted value is the IDIOM; presets are its delivery carriers.** The
ratified taxonomy (2026-06-30) makes the five idioms the structural style axis and presets named
idiom-weightings ("presets = idioms, for now"); fitting per genre-named preset would bake the retired
genre axis into fitted constants at the very moment the taxonomy replaces it. Therefore: (i) every
style-varying fitted set is **labeled by the idiom whose ground truth shaped it** — the Bach-chorale fit
is an **idiom-#2 (Chromatic-functional)** fit (Baroque, galant and Classical share idiom #2, per the
discovery study), delivered through the Baroque and Default preset carriers; (ii) the manifest classifies
every parameter as style-invariant or idiom-varying (§4.1), so the fitter knows which values a future
idiom multiplies and which it must not; (iii) a per-idiom fit target exists only where that idiom has
licensed ground truth (today: idiom #2 only — the fitting-pool jazz/pop sources create targets for #3/#4
when conversion-ready, O-5); (iv) **mixture semantics are explicitly deferred**: how a preset that
weights several idioms combines their fitted parameter sets — and the idiom auto-detection that would
drive it at runtime — is the taxonomy's own deferred roadmap feature (an inference feature, after the
architecture is complete, per its decision 4), NOT this arc's work; this arc delivers idiom-labeled sets
1:1 through the existing carriers so that later work composes them without refitting. *Alternatives:*
fit per preset with no idiom labels (rejected: orphans the fitted artifacts the moment presets become
weightings — the migration would not know what the values mean); fit per idiom with runtime mixture now
(rejected: pulls the deferred auto-detection feature into a fitting arc, violating the standing
inference-feature ordering and unneeded while each carrier maps to one idiom). *Consequence for the batch
stop:* the corpus dirs and the 53/24/53 sets stay keyed by preset carrier (the instruments' existing
shape); the idiom label lives in the manifest and the fitted-set artifacts, not in the stop's plumbing.
*The two axes, stated plainly (user question, 2026-07-04):* the **idiom is the FITTING axis** (what
ground truth shaped a value; what a fitted set means) and the **preset is the EXECUTION-and-REGRESSION
axis** (the only configurations the pipeline can run today, each a user-selectable surface that must not
change silently — which is why evaluation and the stops stay preset-keyed even though the Jazz carrier's
corpus numbers measure its *configuration* on idiom-#2 material, not "jazz"). The two merge at the
taxonomy's own preset→idiom-weighting migration: a deliberate future re-key of the preset-keyed
instruments (its own ratified re-baseline event, never drift). Once a second idiom's ground truth lands
(O-5), the evaluation key generalizes to the pair (carrier × ground-truth idiom) — today that matrix has
a single idiom-#2 column.

**D-11 A parameter's value lives in a per-parameter style table of MEASURED dimensionality, estimated
anchor-first.** The general model: a style-varying parameter is a function over the style coordinates
(the idiom-mixture simplex + the two cross-attributes) — in the worst case continuous, in the best case
constant. Three commitments: (i) **the dimensionality is measured per parameter, never assumed** — the
§4.4a style-response measurement decides which coordinates a parameter responds to, so each parameter's
table has exactly the dimensions its measured response needs (most are expected to need zero or one);
(ii) **estimation is anchor-based** — fitted values at the idiom vertices (and at cross-attribute splits
where §4.4a demands them), NEVER a dense table over continuous coordinates (unfillable by any data we
will hold); the discrete-table case reads the anchors directly, and the continuous case is realized as a
declared interpolation over them — **linear mixing of anchor values over the idiom weights is the
recorded default hypothesis**, which makes the deferred mixture semantics (D-10 iv) the same machinery:
anchors fitted now compose into mixtures later without refitting; (iii) **border values are measured,
not designed** — where §4.4a finds stable clusters, the table's conditioning and its borders come from
the cluster structure, with a cross-idiom cluster surfaced as a taxonomy finding rather than forced into
the idiom axis. Four refinements (folded 2026-07-04, second pass — the "how do the coordinates really
relate to parameters" analysis): (iv) **coordinate selection is per parameter, and the candidate set
includes the axis-2 texture class** — a parameter's optimum responds to style only THROUGH the
distributional statistics its evidence weights (root-continuation rate, inversion prevalence, seventh
prevalence, chromatic density…); the harmonic idioms quantize the *progression*-statistics space, but the
inversion/bass/pedal parameter families weight *textural* evidence, and texture is measured orthogonal to
the harmonic idioms — so those families' style coordinate is plausibly the axis-2 class, not the harmonic
idiom (a §4.4a-testable hypothesis once texture strata exist; within the chorale pool they are thin — the
chorales are ~98 % one texture class); (v) **estimation refinement: hierarchical shrinkage (partial
pooling)** — the statistically standard treatment of "one parameter, several related strata, limited data
per stratum" estimates per-stratum values shrunk toward the pooled value in proportion to stratum data;
the §4.4a cluster verdict is its discrete approximation, and the "default to the simpler structure" guard
is what shrinkage does continuously; whether the fit uses explicit shrinkage or the discrete verdict is a
checkpoint-P1 decision on the measured stratum sizes; (vi) **mixing validity is parameter-family-
dependent** — the template score is additive in the bonus/penalty magnitudes (given fixed structural
conditions), so linear anchor mixing of THAT family equals linear score mixing (principled); threshold-
family parameters sit inside indicator conditions, where an interpolated threshold is well-defined but is
NOT a mixture of the anchor behaviors — the structure verdict records per family whether its anchors may
be mixed continuously or only selected discretely; (vii) **the coordinates vary within a piece** —
chromaticism (and the idiom mixture itself) is a per-passage quantity, and the taxonomy's ratified
auto-detection decision already reads the mixture forward off committed progressions; the anchor model
supports time-varying weights without refitting (the anchors are fixed; only the mixing weights move).
*Alternatives:* a fixed per-idiom table for every style-varying parameter (rejected:
unmeasured dimensionality — pays five-way data cost for parameters that may respond to nothing, and
hides cross-attribute structure inside idiom cells); a global continuous regression per parameter over
style features (rejected for now: the current one-vertex data cannot support it, and it would dissolve
the ratified discrete taxonomy without evidence). *Consequence:* the manifest's style-scope column is the
declared prior; the style-response structure is its measured replacement; the fitted-set artifact stores
anchors + the structure verdict (including mixability) per parameter.

---

## 10. Quality & testing

- **Per-increment acceptance (all increments):** composing + notation suites green; snapshots no-refresh
  (or a refresh justified by an adopted behavior change); the sandwich (batch stop 53/24/53 case-identity
  set-diff empty ×3 before/after for infrastructure; explained and ratified diffs for adoptions);
  reference corpus byte-untouched by harness runs.
- **Harness self-tests:** the objective evaluation self-validates against the pinned A-8 instrument on
  every piece (the A-8 §0.2 discipline: the reused loop proves itself byte-identical to the pinned
  primitive); double-run ledger byte-identity; a known-vector fixture — the current constants, evaluated
  at FULL coverage, must reproduce the ratified §4.2 baselines exactly (the fixture is full-coverage by
  construction; the fitting-split baseline is recorded beside it once the split exists).
- **Per-rule proof obligations:** the Stage-1.1 pinned fixture tests replayed under the candidate weights;
  the differential report's class split verified per the two-tier guardrails (score-verified class-(a)
  claims).
- **Calibration tests:** map monotonicity asserted; reliability-map reproduction from the committed C1
  substrate; θ acceptance vs the E0 override fires-vs-corrections reference (§4.5).
- **Validation-pool checks:** per-style deltas reported at every adoption per S-5's defined analogue test;
  every negative delta surfaced, user decides.
- **Coverage:** new harness/tooling paths covered per the standing objective; the parameter-override read
  path in the binary gets its own unit tests (override absent → byte-identical proof included).

---

## 11. Risks & technical debt

- **Overfitting a ~326-score, single-composer fitting split.** Mitigations: the held-out split; the
  validation-pool style sweep at every adoption; R-13 transposition augmentation (decided at checkpoint
  P1, §14); the sensitivity screen's dead-list pruning (fewer live parameters, less variance). Residual
  risk is real and stated: until the fitting pool broadens (D-5 and successors), fitted values are
  Bach-chorale-shaped — exactly as the hand-tuned values already are, but now measurably so.
- **Idiom coverage of the fitting pool is one of five.** Only idiom #2 (Chromatic-functional) has licensed
  ground truth today; idioms #1/#3/#4/#5 have no fit target and keep the A-7 mark. Cross-IDIOM
  style-response structure is therefore unmeasurable until a second idiom's target exists (O-5); what IS
  measurable now is the cross-attribute response within idiom #2 (§4.4a — the mode/chromaticism strata).
  The risk is stated so a one-idiom fit is never mistaken for a style-general one.
- **Clustering noisy per-stratum optima can hallucinate structure.** Each stratum's optimum is an
  estimate from a smaller fit; a clustering verdict taken from raw optima would over-read noise as
  borders. Mitigations are built into §4.4a (stability across seeds and stratum re-definitions; the
  minimum-covered-duration floor; unmeasurable strata reported, never extrapolated) — but the residual
  risk stands: an unstable verdict defaults to the SIMPLER structure (invariant over discrete, discrete
  over continuous), because a wrong extra dimension is fitted noise shipped as style.
- **The objective's ceiling is upstream of weights.** The cross-layer-budget caveat (CLAUDE.md): much
  BIR=false mass is spelling, bass/inversion, segmentation — not weight-reachable. Phase-1b sensitivity
  bounds what fitting can move; the arc's success criterion is honest movement plus the structural
  deliverables (dissolution, calibration, R10), not a promised accuracy jump (the roadmap sized Stage-5
  direct yield small: ~1.3 % batch / ~6–7 % section).
- **Uncalibratable confidences** (L5 mid-range inversion, tonicVote, L1.5 spread): recorded upstream
  findings; their fixes belong to their layers' own future increments, not to maps (D-8). Debt carried
  visibly in the contract §3 rows.
- **Class-(a) churn under weight movement:** symmetric-rotation flips may wobble; the two-tier guardrails
  + the §4.2 full-weight decision keep it visible; a large net class-(a) shift trips investigation.
- **Interaction between dissolution and continuous fits:** rule-disabled fits may need family re-runs
  (Phase-1b interaction warnings size this); budgeted as expected rework, not a surprise.
- **Deferred/gated:** the C3 joint-step design (unblocked at Phase 3, own document); the R9 file split
  (post-E4); template additions (post-fitting decision); Jazz objective data (D-5); the dormant-chain
  shared-constant conflict, if D-9's surfacing test fires (evidence for the E-steps, handled there).

---

## 12. Glossary

§0 TERMS is this document's glossary (single home; no second table to drift).

---

## 13. Background

The scoring constants accreted across the numbered-iteration era (which ran through at least Iter 98; the
iteration-numbered bonus names are that history's residue); repeated hand-adjustment attempts failed
against the invariant web (`docs/scoring_model.md` §8's dead-ends list — B1, B2 ×4, B3). The post-scoring
§6 block grew as corrections to systematic biases (inversion over-fire, enharmonic flips, augmented
rotations), was audited and pinned in Stage 1, partially retired where provably dead (Gates B/C/D, Stage
3.4b), and was scheduled to dissolve into fitted weights when the roadmap's review concluded hand-tuning
had reached its limit. The metric arc that makes fitting honest ran 2026-06→07: granularity bias
quantified (~7× at section view, 15–56× at the robust unit), the music21 filter's ~82 % discard measured,
the human-only variant ratified, reliability curves delivered (C1). This document is the point where
those instruments turn from measurement into optimization. Corrections on record affecting this arc: the
353→352 corpus count fix; the §2.1a denominator-scope lesson (every rate names its denominator); the
D-L3a demotion of the emission sigmoid; the 22b ruling that parked the resolver's preference-among-
licensed lever at L5 §15-13 for this arc (§4.4 family 4).

---

## 14. Related work & external sources

- **Duration-weighted chord-symbol recall** (MIREX audio-chord-estimation "weighted CSR" tradition): the
  robust unit's duration-weighting follows the same principle — segmentation-invariant time-weighted
  agreement. Adopted via the A-8 design; no external code.
- **Structured perceptron** (Collins 2002) and **derivative-free/pattern search** (Hooke–Jeeves family;
  coordinate descent): the two optimizer families D-3 weighs; choice by measured evaluation cost, not
  fashion. **CMA-ES** noted as the escalation option.
- **Calibration methods:** isotonic regression (monotone, non-parametric — the default map shape) and
  Platt scaling (parametric sigmoid) for the Class-M→P maps; standard reliability-diagram/ECE methodology
  already instantiated by the C1 harness.
- **R-11 Conformal prediction** (lever register): weighed here as the abstention-calibration alternative —
  distribution-free coverage guarantees using only the C1 data. *Disposition:* evaluate at Phase 3 as a
  complement for the abstention bars specifically (family 3); not a replacement for reliability maps
  (consumers need graded confidence, not only set-valued abstention). Decision recorded at the Phase-3
  checkpoint.
- **R-12 Multi-granularity self-consistency** (lever register): a cheap uncertainty feature; *disposition:*
  a C1-follow-up measurement candidate, not commissioned in this arc (it adds a signal, and this arc adds
  no new signals — fitting existing decision structures, including family 4's, comes first).
- **R-13 Fitting-time transposition augmentation** (lever register): *disposition:* decided at checkpoint
  P1 — adopted for the Phase-2 fits if the sensitivity screen shows the fit is data-limited (the
  326-score guard); mode-mixture augmentation deferred (it changes label semantics, not just key).
- **Style-conditioned parameter tables — the direct precedents (verified 2026-07-04):**
  **key- and genre-dependent HMMs for chord transcription** (Lee & Slaney, IEEE TASLP 2008; Lee, CMMR
  2008): 24 key-dependent models, and genre-specific simpler models outperforming genre-independent
  complex ones when the right genre is selected — the same architecture as D-10/D-11's anchor tables +
  the deferred idiom auto-detection (their genre selector). **Corpus statistics differ by style in
  exactly our parameter-relevant quantities** (de Clercq & Temperley, *Popular Music* 2011): rock ~94 %
  root-position chords vs ~60 % in common practice (the inversion-bonus family's driving statistic), and
  the pre-dominant→dominant→tonic norms largely absent in rock (the progression-weight family's driving
  statistic) — direct evidence those families are style-varying. **Mode-conditioned parameter tables are
  canonical**: the Krumhansl–Kessler major/minor key profiles and their corpus-fitted successors
  (Temperley; Albrecht & Shanahan) are precisely a parameter table conditioned on the mode
  cross-attribute — four decades of standard practice. **The estimation machinery is standard**:
  mixture-of-experts gating (Jacobs et al. 1991) for mixture-weighted combination; interpolated language
  models and MAP speaker adaptation in speech recognition for the anchor + shrinkage shape (D-11 v/vi).
  **Counter-nuance, honestly carried:** recent joint-corpus deep models report resisting style domain
  shift (AnalysisGNN, 2025 — minor degradation for Roman-numeral prediction across corpora); with large
  data and high-capacity models, style conditioning matters less. Our regime is the opposite — a small
  licensed pool and an interpretable additive scorer — which is exactly where the conditioned-table
  approach is the established fit.
- **Negative transfer under hard parameter sharing** (multi-task-learning literature; verified
  2026-07-05): optimizing a shared parameter for one task/domain harming another is the canonical
  negative-transfer failure of hard sharing, and per-task/branched parameterization is the standard
  remedy — the external precedent for O-9's per-carrier reclassification of the shared bass/root levers
  (the Phase-2.2b Jazz cost under the Baroque-fitted `bassNoteRootBonus`).
- **Considered and rejected:** fitting on music21-adjudicated cells (variant (a)) — an algorithm as
  ground truth; neural proposal models (Stage 7, out of scope); global re-architecture of scoring
  (the review found no structural fault — this arc fits the existing architecture's constants).

---

## §15 Open items & ratification asks

**Asks (the sign-off surface) — ★ ALL RATIFIED (user, 2026-07-04); A-3 ruled = defer the Jazz fit:**
- **A-1** The five-phase shape (§4) with its TWO ratification checkpoints: P0 (fit surface + freeze list,
  on the inventory) and P1 (optimizer + staging + split + R-13, on the harness's sensitivity numbers).
- **A-2** The objective + constraint scoping exactly as §4.2 (root governs; per-evaluation constraints on
  the fitting split; full-corpus checks at adoption events with the declared, bounded held-out exception;
  class-(a) at full weight initially).
- **A-3** The Jazz-preset data decision (D-5): recommendation = defer the Jazz fit until a licensed jazz
  ground-truth source is conversion-ready; fit Baroque/Default now.
- **A-4** The adoption-event protocol (§4.7, S-4): every behavior change user-ratified, one revertible
  commit, both tracks measured.
- **A-5** The §6-block dissolution verdict structure (D-7): retire / retain-as-structural / defer, per
  rule, with differential reports; retention is a legitimate outcome, not a failure.
- **A-6** D-6's parameter-override shape (flag-gated external override, default-off, byte-identical when
  absent) as the sanctioned `src/` touch of this arc.
- **A-7ask** Family 4 (the L5 §15-13 preference-among-licensed weight) commissioned as scoped in §4.4,
  gated on its population measurement. *(Labelled "A-7ask" to avoid colliding with the A-7 mark, §0.)*
- **A-8ask** The idiom axis (D-10 + constraint 4b): fitted values are idiom-labeled with presets as
  delivery carriers; the manifest carries a style-scope column; per-idiom fit targets are ground-truth
  gated; mixture semantics and idiom auto-detection stay deferred to the taxonomy's own roadmap feature.
  *(Same collision-avoidance labelling.)*
- **A-9ask** The per-parameter style-table model (D-11 + §4.4a): dimensionality measured per parameter by
  clustering per-stratum fitted optima under stability guards; anchor-based estimation with linear
  mixing as the recorded default interpolation; unstable verdicts default to the simpler structure; the
  first style-response measurement runs on the mode/chromaticism strata inside the idiom-#2 pool.

**Open items (tracked, not blocking sign-off):**
- **O-1** The fold-SHA demand: the first CC dispatch of this arc demands the acquisition-round fold-commit
  SHA (owed, the 22g precedent) and carries the four uncommitted Cowork files named in the handoff top
  block (STATUS 22k tail · the handoff header · census §8c fitting-pool block · the union-record license
  fixes) plus this design document.
- **O-2** Class-(a) weighting revisit trigger: if Phase-2 fits show class-(a) churn dominating any fit
  direction, the weighting question returns to the user with the measurement.
- **O-3** The roadmap Stage-5 block gains the fitting-pool license constraint at this arc's first CC docs
  commit (census §8c ride; also restated by this document's §2).
- **O-4** The C3 joint-step design document: unblocked at Phase 3; its own Cowork task thereafter.
- **O-5** Broadening the fitting pool (CoCoPops / OpenEWLD / BCFB / GuitarSet / OpenScore conversions):
  each a separate ratified increment; D-5's Jazz decision is the first instance.
- **O-6** E-13 (product-tool register): Phase 0's inventory verifies whether the fit surface touches the
  tuning bridge; if so, it enters the retirement map at that edit (§4.1). *(Resolved at Phase 0: CLEAN —
  the tuning bridge reads no scoring parameter.)*
- **O-7 (Phase 2.1 closure, user-ruled 2026-07-05): the family-1 candidate is PARKED, not adopted.** The
  fitted `kPowerChord3PcPenalty = 0.6375` candidate (full surface in `cc_stage5_phase2_1_report.md`) was
  feasible and improved the full corpus (+0.038/+0.085/+0.055) with class-(b) duration down ×3 and the
  batch sets untouched — but **regressed the held-out split (−0.098)**: the design's own overfit tell.
  Ruling: no value change; the family closes "feasible, constraint-bounded, non-generalizing at held-out";
  the lever re-enters at the family-2 joint fit (its constraint boundary is that fit's subject). The two
  structural findings are banked: the fit is constraint-bounded (the unconstrained optimum lowers the
  penalty, +0.376, blocked by new class-(b) cases — the root-only objective is quality-silent there), and
  the 1b "clean at ±0.05" read does not extend to the full range. The theory question the fit raised
  (is the power chord an accepted chord category?) is recorded at its proper layer: **L4 design §15 O4**
  (idiom-dependent by the theory itself; competitiveness stays an idiom-calibrated constant per §2.15).
  - **O-7 RESOLVED at the family-2 joint fit (Phase 2.2b, CC 2026-07-05, `cc_stage5_phase2_2b_report.md`):**
    re-entered in the 8-row coupled cluster, `kPowerChord3PcPenalty` **does NOT move at the joint optimum**
    — at the coupled point (bassNoteRootBonus 0.775 / kWStepIn 0.125 / sameRootInversionBonus 0.475) its
    whole local ladder [0.20…0.40] is feasible yet every point scores below the current 0.30; its apparent
    standalone leverage (2.1's up-plateau; a fine-grid down-move to 0.225 the 2.1 coarse step-0.15 ladder
    skipped) is **subsumed by `bassNoteRootBonus`**, which the joint fit assigns the bass/root-tone
    correction to instead. The parked lever is inert at the joint optimum — no adoption; `bassNoteRootBonus`
    is the true lever (whose aggressive 0.775 value is itself the source of the candidate's held-out
    class-(b) + Jazz shared-scope cost — the joint fit's central decision-surface finding).
- **O-9 (the Phase-2.2b shared-scope finding — the design's own prediction landing, 2026-07-05):** the
  joint fit's best candidate is blocked by its shared `bassNoteRootBonus 0.775` (+ the `kWStepIn` bump):
  a held-out class-(b) case (`bwv392@17520`, R10 trip on Baroque/Default) and a Jazz duration cost
  (−0.6070, clsB +23120 — no Jazz batch trip). **This is NOT a new design question — it is the §4.4a
  style-response measurement firing through the carrier strata:** the manifest declared
  `bassNoteRootBonus` idiom-varying at Phase 0 (rationale: the rock-vs-common-practice root-position
  statistics, §14), and the Jazz carrier just acted as the first cross-style stratum whose optimum
  diverges — the D-11 verdict is "idiom-varying, CONFIRMED by measurement." **Resolution shape (2.2c):**
  reclassify the diverging shared levers (`bassNoteRootBonus`, `kWStepIn`; others per the same test) to
  per-carrier delivery (the D-10 anchor model: Baroque/Default carriers deliver the idiom-#2 fitted
  value; the Jazz carrier keeps its current effective value — Jazz receives no fit, A-3/4c), then
  re-select the candidate under the full-corpus hard stop (the S-3 rejection loop: gentler
  `bassNoteRootBonus` points from the committed ledger, full surface re-measured; the `bwv392@17520`
  class score-verified per guardrail (2) before it is treated as final). External precedent: negative
  transfer under hard sharing, §14.
  **★ DELIVERED (2.2c, `cc_stage5_phase2_2c_report.md`):** the per-carrier scoping mechanism LANDED
  (`batch_analyze.cpp` `6a468f82ac`: `bassNoteRootBonus` per prefs-field, `kWStepIn` per preset via the
  registered-global writer written BEFORE the override load; values unchanged → byte-identical ×3). The
  **production-path plumbing question is REPORTED, not improvised**: production has no preset-selection
  moment, so it delivers only the Default carrier (via the `bassNoteRootBonus` struct default / the
  `kWStepIn` global initializer); a non-Default-carrier production delivery has no surface. The candidate
  re-selection under the full-corpus hard stop returned **NOT ADOPTABLE AT ANY SWEPT VALUE**: bnrb
  {0.70…0.775} × (srib 0.475, kw 0.125), Jazz pinned byte-identical — low bnrb is fitting-infeasible
  (`bwv379@11520`, absorbed by 0.7375 — the 2.2b coupling), and every fitting-feasible bnrb (0.7375–0.775)
  is full-infeasible on the **score-verified class-(b) `bwv392@17520`** (Baroque AND Default; a Layer-2/4
  segmentation over-grab — `Dm/F` iii6 across the WiR `Gm` vi boundary — driven by the srib/kw pair, not
  bnrb). So O-9's per-carrier delivery is BUILT and byte-identical, but the specific coupled
  `bassNoteRootBonus/sameRootInversionBonus/kWStepIn` candidate is not adoptable: the fitting gain
  (+0.43…+0.51, batch 53→49) is real, but the single new class-(b) is a hard R10 stop. The next-lever
  decision (a gentler srib/kw that does not create bwv392 · a Layer-4 fix for the over-grab · a smaller
  uncoupled gain) is the user's — nothing adopted.
- **O-10 (lesson from the user's methodology challenge, 2026-07-05): RETAINED structural rules carry
  ongoing LIVENESS evidence.** The Gate-K/Gate-L failure mode — a rule's founding cases silently absorbed
  upstream, leaving dead code undetected for weeks — existed because nothing measured rule liveness. For
  the four RETAINED rules (GateI, FM2, GateJ, GateL): their firing-site counts (the 2.2b regen-diff
  method, or cheap telemetry if one is ever built) are re-measured at every adoption event's sandwich and
  recorded in the ledger, so a retained rule whose firing evidence collapses to zero surfaces as a
  finding at the next natural checkpoint instead of by archaeology. (The per-gate a-priori question was
  empirical by nature — this item is the monitoring gap, which was not.)
- **O-8 (housekeeping, user-ruled 2026-07-05, both fixed at the next dispatch):** (1) **fit ledgers become
  committed artifacts** — the per-run ledger files move out of the gitignored `tools/reports/` to a
  committed path; §7's "the ledger is committed" holds for the compact per-run ledgers, while large
  per-cell enumerations stay regenerable scratch pinned by the driver (the A-8 precedent — §7 is amended
  by this sentence); (2) **one validation runner gains `--param-override`** (additive, default
  byte-identical) so the S-5 per-style generalization check CAN run on a candidate before any adoption —
  closing the recorded S-5 instrument gap.

---

*QA record (runs on the full current text). (1) Self-QA against both writing-standard sections
(qualified predicates; §0-before-use; one-sense-per-word) and against the sources read this session (A-8
report, C1 report, contract, census §8c, roadmap blocks, scoring model §1/§2/§4/§6, CLAUDE.md, lever
register, L5 §15-13 via the audit). (2) An INDEPENDENT fresh-eyes adversarial audit (separate context,
all sources re-verified at file level) — 20 findings: 2 HIGH (the Phase-0 sensitivity screen depended on
the Phase-1 harness — fixed by moving sensitivity to Phase 1b and splitting the checkpoint into P0/P1;
the held-out discipline contradicted the corpus-wide per-evaluation tripwire — fixed by scoping
per-evaluation constraints to the fitting split and declaring the bounded adoption-time exception),
10 MED and 8 LOW (all folded: the class-(a) duration figures corrected to 3.5–3.9 % with the cell share
stated separately; reliability maps re-attributed to C1 per the contract; Gate R excluded from the
dissolution scope with its own §0 row; the "gate corpus" third sense renamed to "reference corpus"; Gates
B/C/D's removal moved into the normative sections; the L5 §15-13 lever commissioned as family 4; D-4's
noise-floor language replaced with an exact-comparison rule; the shared-scope evaluation cost declared;
the production-path definition corrected to include the live rebuilt layers; insider handles given §0
rows or citations; the Default set-difference corrected to a two-case swap/four identities; the identity-
form cite corrected to the ratified per-run semantics; the S-5 analogue test defined; the census §2/§6
placement deviation recorded). No audit finding was rejected. The audit's "verified clean" list covers
every headline number against its source. (3) A USER-CAUGHT gap folded after the audit (2026-07-04): the
draft fitted per genre-named preset and never addressed the ratified idiom taxonomy — the style axis of
fitted parameters. Folded as constraint 4b + D-10 + the fit-target term (§0) + the manifest style-scope
column (§4.1/§7) + the idiom-coverage risk (§11) + ask A-8ask; D-4/D-5 and §4.4/§4.5 re-expressed in
fit-target terms; verified at source against `cowork_style_taxonomy_proposal.md` (RATIFIED 2026-06-30,
StyleTag swap executed 2026-07-02) and contract §6 C4. (4) A second USER refinement folded same day: the
per-parameter style-TABLE model — parameter values as functions over the style coordinates with measured
per-parameter dimensionality, decided by clustering per-stratum fitted optima (discrete borders where
clusters are stable, continuous interpolation where the spread is even), anchor-based estimation. Folded
as D-11 + §4.4a + the three §0 rows (style coordinates / stratum / style-response structure) + the
clustering-noise risk (§11) + ask A-9ask. (5) A third USER-prompted pass (2026-07-04, "how do the
coordinates really relate to the parameters — is the model supported by research?"): D-11 gained
refinements iv–vii (per-parameter coordinate selection incl. the axis-2 texture class; hierarchical
shrinkage as the estimation refinement; family-dependent mixing validity — additive weights mix linearly,
thresholds do not; within-piece time-varying mixture weights), the §0 style-coordinates row was extended,
and §14 gained the verified external precedents (key/genre-dependent chord-transcription HMMs; the
rock-vs-common-practice corpus statistics; mode-conditioned key profiles; MoE/adaptation machinery; the
joint-corpus counter-nuance).*
