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

> **★ CORRECTION OF STATE — the scope-out line above ("the `chordanalyzer.cpp` file split (OWED
> refactor #1 — **parked by ratified R9**)") names an act that was already DELIVERED when this design
> was written** (annotation 2026-08-03, CC, on the user's ruling of that date; `OPEN_ITEMS.md`
> **OI-286**, register entry **D-427**). The split was committed as `41f7c65f63` on **2026-06-17**,
> seventeen days before this design of 2026-07-04. **The scope-out itself is unaffected in substance:**
> what this arc excludes it still excludes, and the sentence is preserved unedited (#12). Two things a
> reader should carry forward. **(i)** The **iteration-API renames** — the other half of OWED refactor
> #1 — are genuinely still owed (**D-428**), and their subject includes live Layer-1.5 code, so they
> are not disposed of by the retirement map. **(ii)** This arc's own §6-block dissolution IS OWED
> refactor #2 (**D-429**), and it is the half this document's scope-in list carries.
>
> **★ CORRECTION REMARK, 2026-08-11 (`OPEN_ITEMS.md` OI-304) — CLAUSE (i) ABOVE ASSERTS THE OPPOSITE
> OF WHAT D-428 NOW RECORDS, AND THE ANNOTATION IS LEFT AS WRITTEN (#12).** Clause (i) says the
> renames' subject *includes live Layer-1.5 code*, so they are not disposed of by the retirement map.
> **D-428 was corrected later the same day** — at phase 1n, against the premise and at the call sites
> — and now records that **every use sits on the legacy arm, so deleting that path discharges them.**
> *Why the remark rather than an edit:* this is a dated annotation block, and its wording is the
> record of what was believed when it was written; editing it would destroy the evidence that the
> correction happened at all. The correction reached the register entry and not the two documents
> that state the premise it refuted — the one-surface-corrected shape the row names — and this is
> the second of those two surfaces.

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
   dropped, not fitted on noise. **MEASURED (Phase 2.3, 2026-07-06 — O-13 ii): the population is LARGE
   (Baroque 5544 / Jazz 5581 / Default 5544; ~16.5 % of scored duration; 351/352 scores) → size-viable, NOT
   noise-limited. But it lives on the DORMANT resolver, whose output is not in today's a8 objective → the fit
   is not runnable until L5 engages (or a resolver-output objective is defined). Returned to the user with the
   number; the §15-13 item stays open.**

Each family lands as its own adoption event (or is rejected on its numbers).

### §4.5 Phase 3 — calibration (completing C1's maps; C2)

> **★ DELIVERED (session 22x, 2026-07-06; `cc_stage5_phase3_report.md`; see O-14). Measurement + committed
> artifacts only, NOTHING wired, NO behavior change, NO push.** Curves re-measured on the adopted corpus
> (ECE Δ≤0.001). Maps 1 (L3 margin) + 2 (L4 composite) FITTED (isotonic, Baroque/Default carriers, Jazz
> A-7-unmapped), validated held-out (post-map ECE 0.017–0.041); L4 flat-band asserted+held (0.289). The
> three deferred rows re-verified (L5 non-monotone shape UNCHANGED → stands; tonicVote anti-monotone; L1.5
> → Task B, which found the SURFACE population has usable monotone spread but a weak absolute signal, no map
> fitted). C2 §2: F-A/F-B scales declared + θ candidates recorded/unwired (F-B override net-harm CONFIRMED
> → best measurable θ disables it, an inference finding). R-11 conformal = complement-not-replacement. C3
> remains design-only, unblocked-not-started.

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

**★ R10-a ASSEMBLED (session 22z, 2026-07-06 — O-15).** The decision surface is built: the committed
robust-unit reference (`tools/robust_stop/` — per-preset `stem@runStartTick` run enumerations + summaries +
manifest), the old→new mapping (every 52/24/52 case still-failing under variant (b), 0 disappear), the
runnable+timed successor sandwich (`tools/robust_stop_diff.py`; class-(b) duration non-increase + explained
run-diff; ≈6 s), and the DRAFT CLAUDE.md gate-replacement text (report-only). One declared finding rides to
R10-b: the 2.2e KEY column is unreproducible (root/RN reproduce exactly; key = the prior 68.13/64.43/67.50,
Jazz byte-identity proving 64.43) — its CLAUDE.md correction is an R10-b action. **R10-b (the user's
ratification + the handover commit) remains the arc-closing event.**

**★ R10-b FIRED — the arc-closing ratification (session 23, 2026-07-06; `cc_stage5_r10b_ratification_report.md`).**
The batch→robust handover is MADE. The CLAUDE.md gate section is now: block (A) the robust-unit stop (class-(b)
root-disagree DURATION non-increase per preset + mandatory explained run-diff; reference `tools/robust_stop/`;
baselines root 63.36/62.37/63.25, RN 44.58/42.40/44.41, key 68.13/64.43/67.50) · block (B) the two-tier per-cell
class policy preserved LIVE · block (C) the batch 52/24/52 sets relocated to history · block (D) caveats
(cross-layer-budget LIVE, granularity ✅ RESOLVED). The batch sets are frozen in BOTH CLAUDE.md history AND
`tools/robust_stop/batch_stop_frozen_history.json` (set-equal to `characterise_bir_false.py` verified). The 2.2e
KEY-column error is corrected (`68.19/64.52/67.77` → `68.13/64.43/67.50`) with the repo-wide occurrence list
dispositioned (one historical design-log line annotated, not rewritten). `characterise_bir_false.py` →
KEPT-AS-DIAGNOSTIC (R3 pattern; its `validate_corpus_dir` is imported by the a8 instrument, so it cannot
bit-rot). Both stops green at close: batch `52/24/52` set-diff empty ×3, robust sandwich identity-PASS (+0/−0,
class-(b) Δ=0 all presets). **Roadmap retirement item R10 is FIRED; the Stage-5 arc is CLOSED.** The engage arc
opens on the inherited dossier: **F-B redesign [1043/53/809, net-harmful override] · §15-13 [5544, parked —
dormant-resolver objective] · θ/map wiring · L1.5 surface map · GateA unification · the L5 inversion · tonicVote.**

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
- **O-4** The C3 joint-step design document: unblocked at Phase 3; its own Cowork task thereafter. **✅ DELIVERED
  (2026-07-07, engage arc #10, `cowork_joint_key_chord_design.md`; observation O-26 below).** Architecture design
  only (read-only / structure-only); the build (B1–B4) is a later, separately-ratified E4-adjacent event.
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
- **O-11 (the GateA byte-identity ruling + family-2 closure, 2026-07-05, Phase 2.2c).** (i) **RULED:
  `alternatives[]` IS inside the byte-identity acceptance contract** — the carried alternatives are a
  load-bearing output surface (the L4 §15 O1b carry contract: L5 overrides select among carried
  readings; E-14 makes them user-visible), so "same winner, different alternatives" is a behavior
  change. Consequence: **GateA's retirement is HELD** (verdict amended RETIRE → DEFER): it is
  winner-inert everywhere but alternatives-active on 36 Baroque scores — its `std::swap` promotion and
  FM2's `push_back(buildResult)` promotion produce the same winner with different carry side-effects.
  **It retires when the promotion machinery unifies** (one promotion path producing one carry — a named
  total-unification item, claimable by the L4 carry work or a §6-block consolidation increment).
  Evidence-method lesson recorded: firing-site/inertness evidence must measure the FULL output surface
  (winner + alternatives), not the winner alone. (ii) **Family 2 (the coupled continuous cluster)
  CLOSED NOT-ADOPTABLE at every swept value** (`cc_stage5_phase2_2c_report.md` Task 4): low
  `bassNoteRootBonus` is fitting-blocked (`bwv379@11520`), every fitting-feasible value is
  full-corpus-blocked by the Task-3-verified class-(b) `bwv392@17520` — which is driven by the
  `sameRootInversionBonus 0.475 + kWStepIn 0.125` PAIR (present even at bnrb 0.70), a **Layer-2/4
  segmentation over-grab** (the candidate reads the RIGHT chord, Dm/F, but starts an eighth late and
  extends across the barline into the GT's Gm region — the weight fit relocates the boundary failure,
  it cannot remove it; the §11 "ceiling is upstream of weights" caveat, now measured at a single case).
  Open follow-up: a cheap (srib, kw) sub-sweep below the blocking bump (investigate-by-default) may
  find a smaller feasible gain; the Layer-4/NCT fix (R-14) stays deferred to its proper turn.
  **★ RESOLVED (2.2d, 2026-07-05): the sub-sweep found a feasible slice — and the ARC'S FIRST ADOPTION
  IS USER-RATIFIED (2026-07-05): candidate (sameRootInversionBonus 0.40 [unchanged], kWStepIn
  0.10→0.125), Baroque/Default carriers, Jazz pinned byte-identical.** Surface: fitting +0.0365,
  held-out +0.0280 (generalizes), full-corpus +0.0347 both carriers, fixes the canonical class-(b)
  `bwv244.32@5760`, ZERO new class-(b) anywhere, DLC net-positive. The tie-break vs (0.425, 0.125)
  ruled for the single-lever point (identical class-(b) win; the alternative's batch edge is class-(a)
  churn + a fragile coupling + struct-default leakage into unmeasured carriers). The adoption event =
  its own dispatch (`cc_instruction_stage5_phase2_2e.md`): the value + provenance stamp (the FIRST §7
  license-provenance fill) + goldens refresh + **the first deliberate frozen-corpus re-baseline**
  (expected 52/24/52, removal-only diff {bwv244.32@5760} ×Baroque/Default; CLAUDE.md sets re-stamped;
  A-8 baselines re-measured) + unmeasured carriers explicitly pinned (mandate 4c) + the O-10
  retained-rule liveness re-measurement. **The batch stop REMAINS the hard stop (dual-track unchanged —
  this is a set re-stamp within the policy, NOT the R10 dissolution).**
  **★ EXECUTED (2.2e, 2026-07-05, `cc_stage5_phase2_2e_report.md`; commit `c50002fee1` `feat(analysis):` +
  the corpus chore).** Landed exactly as specified: kWStepIn 0.10→0.125 (Baroque/Default; production via the
  Default global initializer; Jazz + Standard/Modal/Contemporary pinned 0.10), sameRootInversionBonus 0.40
  unchanged. **Corpus re-baselined 52/24/52**, set-diff = **removal-only `{bwv244.32@5760}`** on Baroque+Default,
  Jazz identical. **★ Jazz byte-identity — a delivery finding (CC, LOAD-BEARING).** `kStepBudget` is DERIVED
  (= kWStepIn+kWStepOut+0.01) and a single-key `applyGlobalOverride` does NOT recompute it — only the FILE loader
  does. So the new 0.235 *initializer* would have LEAKED into the carriers that pin kWStepIn back to 0.10
  (Jazz + Standard/Modal/Contemporary) and broken Jazz byte-identity. `batch_analyze` now RE-DERIVES kStepBudget
  per carrier after the single-key kWStepIn write (Jazz→0.21). Proven load-bearing: a forced-0.235 Jazz regen
  differs on **7** `.ours.json`; the fix restores 0 diff. (The frozen corpus is gitignored, so byte-identity was
  proven by an explicit-override reconstruction of the pre-adoption Jazz, not `git diff` — a process note: snapshot
  the frozen corpus before a future re-baseline regen.) A-8 baselines re-measured (root 63.36/62.37/63.25, RN
  44.58/42.40/44.41, key 68.19/64.52/67.77 **[R10-b correction, 2026-07-06: this key column is the
  non-reproducible 2.2e measurement-entry error; the reproducible key column is 68.13/64.43/67.50 — Jazz
  byte-identity proves 64.43; see O-15 and the block-(A) A-8 note in CLAUDE.md. Historical log line left
  as-recorded per the annotate-don't-rewrite rule.]**); CLAUDE.md re-stamped 52/24/52; goldens refreshed 11/11; O-10
  liveness recorded (all four retained rules LIVE, counts near-prior; ledger `stage5_2_2e_liveness.jsonl`).
  Suites 1101/53/11 green.
  **★ DELIVERED (2.2d, `cc_stage5_phase2_2d_report.md`): the sub-sweep FOUND a feasible slice — the
  answer is YES.** The 18-point 2-D grid (srib∈{0.40…0.4625}×kw∈{0.10,0.1125,0.125}, bnrb fixed 0.70,
  Jazz byte-identical by O-9 construction) yields **three full-feasible points**, all at high kw, with
  a **top-gain 2-point tie at fitting +0.0365**: **(srib 0.40, kw 0.125)** kw-only and **(srib 0.425,
  kw 0.125)** both-levers. Both: held-out +0.0280 (generalizes), Baroque root +0.0347 (identical),
  **newB=0 on all three carriers, D-4 Default eligible, Jazz byte-identical** (the O-9 per-carrier
  delivery removes the 2.2b shared-scope Jazz cost entirely), DLC flat-positive (mozart +0.7), snapshot
  11/11. **★ The tie's *meaningful* improvement is IDENTICAL** — both remove exactly the same single
  class-(b) case `bwv244.32@5760`; the 53→52 vs 53→50 batch gap is entirely **class-(a) churn**
  (`bwv258@10560`+`bwv334@6720`, symmetric-rotation coin-flips). So the family-2 gain was never "no
  feasible slice" — it was a **~14× smaller feasible slice reachable only with bnrb at 0.70 and the bump
  gentle** (bwv392 is absent from the whole srib=0.40 column; the srib bump is what creates it, and at
  (0.425,0.125) it is re-absorbed by the higher kw). CC recommends **(0.40, 0.125)** (minimal/robust,
  single lever, no bwv392 exposure); (0.425,0.125) trades a bigger perturbation + class-(a) churn for
  better tracked-beside RN/key (+0.049/+0.032). **Prepared-not-applied adoption artifact** with the
  kStepBudget note (kw 0.10→0.125 ⟹ kStepBudget 0.21→0.235; override loader recomputes at fit time, a
  baked adoption must ensure the same). **NOTHING adopted; the candidate + the tie-break are the user's
  ratification event** (Family 2 re-opens as ADOPTABLE-PENDING-RATIFICATION, superseding the 2.2c
  not-adoptable closure). (iii)
  **Production-path delivery fact (Task 2):** the production/notation path has NO preset-selection
  moment — it delivers ONLY the Default carrier (struct default + global initializer are its delivery
  surface); a future Default-carrier adoption ships to production through those; non-Default carriers
  are batch/fitting-path-only until a production preset moment exists (D-10 note).
- **O-12 (process lesson from the 2.2e re-baseline, 2026-07-05): the frozen corpus is GITIGNORED —
  "git status clean" was always a VACUOUS byte-untouched check.** `tools/corpus/` is not
  version-controlled (`.gitignore`), so every prior report line citing "git status tools/corpus/ =
  clean" proved nothing; the protection that actually held (and genuinely did — verified) is the
  manifest's per-score sha256 fingerprints + `characterise_bir_false.py`'s refuse-on-mismatch
  validation + the 2.2c frozen-vs-baseline regen comparison. Standing corrections: (1) byte-untouched
  claims cite MANIFEST-FINGERPRINT VALIDATION (or an explicit regen-compare), never git status;
  (2) **every future corpus re-baseline SNAPSHOTS the outgoing frozen corpus before regenerating**
  (2.2e overwrote the old Jazz in place before copying; byte-identity was then proven by an
  explicit-override reconstruction — rigorous, but the snapshot makes it trivial); (3) whether the
  frozen corpus should become git-tracked (or snapshot-archived per re-baseline) is a user call,
  recorded as open.
- **O-13 (staging step 3 closure + the family-4 §15-13 population, 2026-07-06, Phase 2.3;
  `cc_stage5_phase2_3_report.md`).** Two cheap measurements; nothing adopted, no value change, no corpus write.
  **(i) Staging step 3 — the three surviving §6-block margins hold NO fittable gain at full range → each RETAINED,
  constant stays hand-set (skip-with-record).** Full-range 1-D ladders (Baroque carrier, fitting split, refine-0)
  on `kGateIMargin` [0,1.0], `kGateLMargin` [0,1.0], `kHalfDimFirstInversionBonus` [0,1.2]: **no feasible Δ>0 on
  any margin at any point** (best feasible = baseline, `ALREADY-OPTIMAL`). The full range REFINES the ±step-dead 1b
  reading exactly as the 2.1 lesson warns: `kGateLMargin` is globally objective-inert on the Baroque root
  objective (Δ=0 across [0,1.0], even at 0 where Gate L never fires — consistent with its 2.2b Jazz-only liveness);
  `kGateIMargin` and `kHalfDimFirstInversionBonus` are locally flat around their current values but the objective
  DROPS at the extremes (Gate I at both ends — 0.0 stops it firing, 0.8/1.0 fires it on wider gaps, both class-(b)-
  infeasible; the FM2 bonus only when shrunk toward disabling its promotion). Every non-zero Δ is a LOSS in an
  INFEASIBLE direction; the current hand-set values sit at/inside the objective-optimal feasible plateau. So the
  rules are load-bearing (their RETAIN verdicts are re-confirmed by leverage) but hold no fit — a legitimate
  staging-step-3 closure. Ledgers `tools/fit_ledgers/stage5_fit_<margin>.jsonl`.
  **(ii) Family 4's §15-13 population is LARGE — size-viable per the gate, but its lever is on the dormant chain
  whose output is not in today's objective (a DECLARED finding, not a decision).** The both-licensed fall-through
  population (`bothLicensed` telemetry added to the resolver, read via `--dump-fullspine`; byte-identical on
  production, 0/352 ×3): **Baroque 5544 / Jazz 5581 / Default 5544** (Transition ≈3550, ShareTone ≈2000; outcome
  ≈52 % structural tie-break, ≈48 % honest open mark; **~16.5 % of scored duration**, present in 351/352 scores,
  max 87/score, median 15). By the design's stated SIZE gate this is **not too small — the fit is not
  noise-limited.** But the §15-13 weight acts on the DORMANT L5 resolver's output, which does NOT enter the
  current A-8 production/L4-root fitting objective (proven: the field is byte-identical on that path) — so the fit
  is size-viable yet **not runnable against today's objective** (it would move the fullspine L5 roots on those
  ~5544 slices while the a8 objective stays Δ=0 by construction). Running it needs L5 engagement (the resolver
  output becomes what the objective grades) OR a dedicated resolver-output objective + GT — a design/sequencing
  question returned to the user. **No fit run either way (per the dispatch); the number + this substrate
  observation are the checkpoint material.** The §15-13 item stays open, now with its measured population.
- **O-14 (Phase 3 CALIBRATION delivered, 2026-07-06, session 22x; `cc_stage5_phase3_report.md`).** Measurement
  + committed artifacts; NOTHING wired, NO behavior change, NO corpus write, NO push. **(i) Curves re-measured**
  on the adopted corpus `c50002fee1` (predated 2.2e): every harmonic-row ECE Δ≤0.001 — the adoption did not move
  the calibration. **(ii) Class-P maps FITTED + COMMITTED** (`tools/calibration_maps/stage5_classP_{l3_key_margin,
  l4_chord_composite}_{baroque,default}.json`): isotonic on both rows (Platt rejected — iso-vs-Platt maxdiff
  0.20–0.26, not near-logistic, and Platt held-out ECE worse); fit on the 261 fitting split, VALIDATED on the
  65 held-out (post-map held-out ECE 0.017–0.041, 3–6× below pre-map); the L4 flat low band pools to a constant
  **0.289** (flat-band assertion held — no invented resolution); monotone by construction. Jazz UNMAPPED (A-7).
  **(iii) Deferrals re-verified:** L5 combinedBoundary non-monotonicity shape UNCHANGED post-adoption (the STOP
  "shape changed" did NOT trigger — deferral STANDS); cadence tonicVote anti-monotone; L1.5 → Task B. **(iv) Task B**
  (via the additive default-off `phraseNumVoices` dump field; spike-floor invariant confirmed exactly = 1.5·numVoices):
  the SURFACE population (98.4% of ticks), un-compressed from the spike-dominated per-profile max, has usable
  MONOTONE spread (0.13→0.46, mono-viol 2) → a per-population map is fittable IN PRINCIPLE at a later increment;
  the SPIKE population is a flat ~0.40 cluster (no usable spread); NO map fitted (weak absolute signal, tops at
  0.46) — the C1 "insufficient spread" reading is REFINED (spread exists once un-compressed; the limit is the
  weak detection signal, upstream of calibration). **(v) Task C (θ):** F-A/F-B contradiction scales DECLARED
  (`x/(x+3.5)` cadentialWeight, `x/(x+2.0)` plaus-diff; R5, precision-phase; ranges re-confirmed [3.35,9.35] /
  [2.0,3.0]); θ candidates fitted RECORDED/UNWIRED (dormant chain, adoption rides engage) — **F-B fine-grain
  override net-harm CONFIRMED (1043 fires / 53 corrections / 809 harms → 78% of fires move an L4-correct root
  wrong); the corr−harm-maximizing measurable θ effectively DISABLES the override → declared to Cowork as an
  inference-quality finding (redesign, not a θ retune)**; F-A reduced candidate τ≈5.0 on cadentialWeight
  (corr−harm +6→+15 fit / +3→+5 hel) — full form deferred (the L3 incumbent key confidence is not in the
  `modulations[]` dump; the override θ is not `--param-override`-exposed, so candidates are one-sided/stricter-only,
  recorded). **(vi) Task D (R-11 conformal):** split-conformal vs map-implied abstention at targets {0.70,0.75,0.80}
  — conformal retains more at achievable targets (better efficiency, finite-sample-valid) but slips where the
  correctness ceiling nears the target → **complement, not replacement** (recorded for the Cowork disposition).
  **(vii) Contract-§3 row changes listed for Cowork to apply** (report §1.4 — contract is Cowork-owned). Sandwich:
  gate 52/24/52 set-diff empty ×3, corpus fingerprint-validated untouched, standard `.ours.json` byte-identical
  (15/15), suites 1101 / 53+4skip / 11 no refresh. The maps' + θ's WIRING into live boundaries is a separate,
  later engage-adjacent increment. Next: the arc-close checkpoint §4.7/R10.
- **O-27 (ENGAGE ARC #11 — PEDAL detection's home + the F-B ANNOTATE mechanics, read-only / structure-only —
  ★ CLOSES STAGE 2, 2026-07-07; `cowork_layer5_engagement_design.md` Part 2 §6–§10 + report
  `cc_engage_l5_pedal_annotate_design_report.md`).** The last two Layer-5 engagement design pieces (Part 1's §4.3
  hinges). **Fitter-relevant facts:** (a) **Pedal detection** placed as a **reader over the decoder's governed
  carry** (grep-confirmed the decoder has 0 pedal detection today), emitting a distinct pedal-annotated result — its
  confirmation margin **read from the carry's distinct-root ranking / the FQ-1 primitive**, NOT a re-computed scan
  (retires `chordpostpasses.cpp:209-281`'s clobber/re-scan/defensive-disable with the anchor at E4). No new
  precision-phase constant of its own (it consumes the carry's confidences); the pedal-confidence bar remains a
  precision-phase constant. (b) **F-B demoted to an ANNOTATION on the UNIFIED open-mark** — the load-bearing #6
  decision: reuse the existing open-mark carry (enriched with a reason/kind `Undecided` vs
  `FunctionContextContradiction`), NOT a parallel `functionContextContradiction` field (semantically wrong to
  overload the plain boolean; a parallel bool duplicates the channel). **New quantity to calibrate:** the F-B
  contradiction carried as **Class-M calibrated uncertainty** — the frame's `(C = L4 composite, S = plausibility
  diff ∈ {2,3})` become the open-mark payload, squashed (shape declared, constant precision-phase R5). The reading
  stays the L4 commit (`overrodeCommit` false) — **no override, no `forwardRecompute`**, so **F-B's override θ/scale
  (D-FS) leaves the critical path**; only the F-A modulation frame still consumes the contradiction-scale θ (a
  narrowed Stage-5 calibration dependency). (c) **Owed measurements flagged, not assumed (#5):** [owed-P1] the
  pedal reader's agreement with the current in-place detection · [owed-P2] the carried-margin vs the `pass2` sigmoid
  · [owed-FB1] F-B byte-identical today, must move class-(b) DURATION favorably at engage. **★ STAGE 2 (the Layer-5
  engagement design phase) is COMPLETE** — carry+selection (O-25), the joint step (O-26), pedal home + F-B annotate
  (this) all designed, structure-only; Stage 3 (E4 / algorithmic completion) is the user's to open. No `src`/build/
  corpus/fit; both stops green by construction (no code path touched); fork-only.
- **O-26 (ENGAGE ARC #10 — the JOINT key-and-chord step ARCHITECTURE DESIGN, read-only / structure-only,
  2026-07-07; `cowork_joint_key_chord_design.md` + report `cc_engage_joint_key_chord_design_report.md`).** The O-4
  deliverable. **Fitter-relevant facts:** (a) The joint step is designed as a **total-unification completion (#6)
  of the built `decideJointKey`** (J-key-i/ii/iii) — its key-axis half (lattice + Viterbi + **key-transition
  prior** `transitionPenalty` + measured **coupled minority ~13.5%** + config-B chord→key `couplingScore`) is
  built; the design **adds the deferred chord re-decode axis** (`regionanalyzer.cpp:388-395` deferred it "to a
  faithful mechanism" = the engaged `ChordSliceDecoder`, a pure fn of (slices,key)) → a bidirectional (key,chord)
  beam. (b) **Placement = a BOUNDED coupling step** at the L3/L4→L5 seam, forward-only (no L3←L4 back-edge), **not
  a unified hidden state** (#7/#6 + magnitude realism). (c) **New confidence to calibrate:** a declared **Class-M
  joint-decision margin** (winning joint hyp vs best different-key-or-root hyp, squashed; shape declared, constant
  precision-phase R5) beside L3 `keyConfidence` and the L5 selection margin. (d) **New composition to fit:** the
  joint score `keyEmissionFit + chordFit|k + couplingTerm + −keyTransitionCost` — all terms precision-phase
  (`transitionPenalty`, `couplingBonus`, beam width, trigger bar 1.0). (e) **The C3 trigger** is a two-stage gate:
  pre-filter `(a)` `keyConfidence` < seq-margin bar `∧ (a′)` chord-ambiguous, then exact `(b)` from the re-decode
  (why C3 is un-computable read-only — (b) IS the owed build). (f) **Owed measurements flagged, not assumed
  (#5):** [owed-1] true C3 fire-rate (the ~13.5% `coupled` is a proxy) · [owed-2] coupling benefit on the
  robust-stop coupled set (the acceptance gate) · [owed-3] per-key flip-rate · [owed-4] beam width · [owed-5] the
  coupling term under re-decode · [owed-6] the precision-phase constants. **Owed build B1–B4** (per-key re-decode
  driver / beam driver / trigger gate / production wiring) enumerated by layer, E4-adjacent, held until ratified
  (like J-key-iii's flag). All constants precision-phase (R5); no fit. No `src`/build/corpus; both stops green by
  construction (no code path touched); fork-only. Closes O-4.
- **O-25 (ENGAGE ARC #9 — Layer-5 engagement DESIGN Part 1: the carry + selection architecture, read-only /
  structure-only, 2026-07-07; `cowork_layer5_engagement_design.md` + report
  `cc_engage_l5_carry_selection_design_report.md`).** Stage 2 opened on the O-24 real fan-out. **Fitter-relevant
  facts:** (a) the **carry contract** is designed on the **distinct-root axis** (not a top-N reading list) with
  the **exclusion tail carried (#12)** — the fitter's objective scores over this graded distinct-root
  distribution, incl. the ≥3rd-root minority (25/16/25 %). (b) **The decoder's distinct-root guarantee is OWED**:
  `topK` caps on **voicings** (`sameChordVoicing`, default 6), NOT roots, so the ≥3rd root is not structurally
  guaranteed to survive — a distinct-root-preserving carry is an owed Layer-4/E4 change (fitting the cap depths is
  precision-phase). (c) **Selection is re-ordered load-bearing-first** — bass/inversion + spelling +
  key-consistency + cadence decide; **licensed progression is demoted to a tie-break, NEVER an override lever**
  (the F-B net-harm finding + research §1 grounding), which **re-orders the as-built `resolveAbstained`** (it
  leads with the weak progression channel). (d) **F-B reconciled = annotate-not-override** (settled §3.D-1). (e)
  **New confidence to calibrate:** a declared Class-M **joint-consistency selection margin** (squash shape
  declared, constant precision-phase) beside the built `combinedBoundary` (D-L5a). All constants precision-phase
  (R5); no fit. Downstream enumerated for follow-on Parts (FQ-2 quality-from-key owner, pedal detection's home,
  O-18/C3 joint step, F-B annotate mechanics) — not resolved. No `src`/build/corpus; both stops green by
  construction (no code path touched); fork-only.
- **O-24 (ENGAGE ARC #8 — the TRUE untruncated Layer-5 fan-out MEASURED read-only, 2026-07-07;
  `cc_engage_fanout_measure_report.md` + data `cc_engage_fanout_measure_data.json`; instrument
  `tools/measure_fanout.py`).** The O-22 audit measured only the **capped floor** (append fires ~36 %
  Baroque/Default, 21.5 % Jazz); this measures the **uncapped above-threshold ranked set** the cap-of-3
  truncates — `gateCtx.rawCandidates` filtered by `gateCtx.threshold`, captured with the **real production
  context** (the no-`src` paths are unfaithful: `--diagnose-measures` runs NULL context + no threshold;
  `--dump-fullspine` runs a different decoder). A minimal default-OFF `--dump-fanout` field, **1056/1056
  `.ours.json` byte-identical** vs frozen `c50002fee1`, both stops green. **Fitter-relevant facts for the
  Stage-2 design (corpus `c50002fee1`, ×3 presets):** (a) the true above-threshold set is **~2× the capped
  floor** — median **5/4/5** readings, mean **6.35/6.15/6.32**, p99 **27/23/27**, max **49/46/49**; the
  cap-of-3 discards ≥1 above-threshold reading on **79.5/75.4/79.3 %** of slices. (b) **BUT it collapses to a
  small root set** — distinct roots above threshold median **2/1/2**, mean **2.13/1.73/2.12**; the reading
  count is mostly template/voicing variants of ~2 roots (`fanoutTotal`=204 constant = 12 roots × 17 templates,
  the full scored grid — so the meaningful fan-out is strictly the above-threshold subset, ≈3.1 % of the grid).
  (c) **The load-bearing exclusion tail (#12):** a **≥3rd distinct root** clears threshold on **25.1/16.1/24.9
  %** of slices — roots the cap-of-3 + single diff-root append (winner + ≤1 alternate root) **cannot carry**;
  that is where the uncapped carry (E4's governed carry replacing the substrate) is load-bearing for the
  Layer-5 selection the fitter's objective scores over. Observation only (moratorium — no inference coding, no
  design decision); the numbers are for Cowork to open Stage 2 on the real distribution.
- **O-23 (ENGAGE ARC #7 — STAGE 1 PRE-Layer-5 refactor batch DELIVERED, 2026-07-07;
  `cc_engage_pre_l5_refactor_report.md`).** The portable pre-L5 unification wins landed as three
  byte-identical revertible commits (FQ-5 `65764881d0`, FQ-7/S8 `56b06462db`, FQ-6 `5420e6e543`; each
  0-diff `.ours.json` 352×3 + robust PASS + characterise 52/24/52 + suites 1101/53/11 no-refresh). **Two
  fitter-relevant observations for the Stage-2 design:** (a) **FQ-7/S8 done** — the key-decoder's
  cost/window constants (`changeBaseCost`/`changePerFifthStep`/`relativePairExtraCost`/`decayRate`/
  `lookaheadWeight`) now source from the resolver/scoreharvest shared symbols, so a Stage-5 fit of those
  magnitudes moves ONE source (the drift surface the fitter would otherwise have to track is closed);
  **S9 confirmed load-bearing** (the `resolveKeyAndModeRanked@585` grid seed is NOT droppable). (b)
  **FQ-1 + FQ-3 STOP-and-deferred** — FQ-1 ("best different-root" scan) is not one code-level decision
  (divergent predicate/type/use) so it is not a byte-identical Stage-1 unification; FQ-3
  (`findTemporalContext` relocation) folds into the E4 temporal-context ownership move (decoder is the
  E4-decided owner). Both await Cowork adjudication before Stage-2. The §6-block / cap→append tangles
  (FQ-2, FQ-4) remain owned by Stage-2/E4 as planned — unchanged by this batch.
- **O-22 (ENGAGE ARC #6 — the STRUCTURAL-INTEGRITY audit, read-only grounded catalogue, ALL built layers,
  2026-07-07; `cowork_structural_integrity_audit.md` + `cc_engage_structural_integrity_audit_report.md`).**
  Total-unification (#6) + layer-adherence (#7) + build-on-clean-theory (#1) made proactive — the structural
  analogue of the O-20 information-loss audit, swept systematically. READ-ONLY: no `src`/corpus/build/fix;
  both stops untouched/green. The anchor (`results` carry substrate, Layer-4 legacy) is a genuine
  cap→workaround/concern-coupling tangle (cap-of-3 `harmonicfunctionlayer.cpp:521` + the diff-root append
  `:530-549`; **dissolution PROVEN at code** — an uncapped threshold-only build is a strict superset ⟹ the
  append dies; only Iter 91's below-threshold `kPromoteAppendOnly` pull is a legitimate targeted promotion
  that does NOT dissolve); pedal detection clobbers the shared vector + re-scans + defensively disables the
  append. **Its clean-target is ALREADY BUILT in the dormant decoder** (`chordslicedecoder.cpp:746-789/927-930`),
  so the load-bearing sequencing verdict is: **the anchor FOLDS INTO the E4 legacy-path retirement, NOT a
  standalone pre-L5 refactor** — while three portable slices ARE pre-L5 wins (a shared different-root
  primitive; `findTemporalContext` relocation; the fact-layer dup + cap-view cleanups). **Direct bearing on
  THIS arc:** (i) the §6-block dissolution (family 2 / R1) is where **FQ-2 gives quality-from-key its single
  owner** — the audit found it scattered across ≥4 sites/3 layers (sparse refinement, section stabilize,
  Gates L/G-E quality-from-key MUTATION, notation display fallback), and Gates L/G-E's quality mutation is a
  NEW facet of the "gates are functional reasoning in the oracle" debt the dissolution retires; (ii) the
  **F-1 confidence-scale incommensurability is pinned to code** (`functionresolver.cpp:460-468`,
  `functionoutput.h:90-98` — bounded `earlierConfidence` vs unbounded `contradictionStrength`/`combined`) as
  the Phase-3/C2 calibration item it already is, inherited at L5 engage; (iii) the S8 key-decoder
  cost/window constants copied-by-value from the resolver/harvest are a fit-surface drift risk (a fit of one
  drifts the other) the Phase-0 inventory should reconcile. Sweep totals: 1 anchor + 20 sites (6 VIOLATION /
  8 UNCLEAR / 6 OK-RESOLVED; 2 HIGH / 9 MED / 9 LOW); fan-out measured read-only (append fires on ~36%
  Baroque/Default regions). 7 UNCLEAR rows for user adjudication. Next per the sequencing call: the pre-L5
  portable unifications (FQ-1/3/5/6), then §6-block dissolution owns FQ-2, then E4 owns the anchor (FQ-4),
  then R9 splits `chordanalyzer.cpp`.
- **O-21 (ENGAGE ARC #3b — the GateA promotion-unification BUILD event DELIVERED, 2026-07-06;
  `cowork_gateA_unification_design.md` + `cc_engage_gateA_unification_build_report.md`; feat `200681a855`).**
  The ratified arc-#3 design, built (Layer 4 only). One `promoteToWinner` primitive + one builder wrapper
  `buildResultFromGateCtx` now own all post-scoring promotion; the enharmonic Major-add6→Minor7 flip is one
  primitive call whose present branch (`presentHint = bestAltIdx`) reproduces Gate A's `std::swap` byte-for-byte
  and whose append branch reproduces FM2, so the separate `GateA` rule removes byte-identically. **Full-surface
  byte-identity PROVEN at objects** (winner AND `alternatives[]`, whole `.ours.json`): **0 diffs / 1056 files
  across all 352×3, including the 36** — `C_unified == C_HEAD` by construction, so the O-11 held-since-Stage-5
  GateA retirement is now MADE and the **O-19 / L1 information-loss fix-queue item is DISCHARGED** (the correct
  carry — the distinct enharmonic partner kept, no winner near-duplicate — is what the unified primitive
  produces). Both stops green (batch 52/24/52 set-diff empty; robust sandwich identity-PASS, +0/-0, class-(b)&(a)
  dur Δ+0); suites 1101/53+4skip/11 (no golden refresh); committed corpus + robust-stop reference untouched
  (scratch). §6 rules 10→9; FM2 the surviving flip rule. The Stage-5 §6-block dissolution continues from the
  unified surface. Next: the remaining fix-queue (L2 spelling collapse) + the UNCLEAR rows (U1/U2/U3) per O-20.
- **O-20 (ENGAGE ARC #4 — the INFORMATION-LOSS audit, read-only grounded catalogue, 2026-07-06;
  `cowork_information_loss_audit.md` + `cc_engage_information_loss_audit_report.md`).** Principle #12 made
  systematic: a static sweep of the load-bearing surfaces (bass · spelling · distinct alternatives · preserved
  uncertainty, `cowork_functional_analysis_research_grounding.md`) for the a–i(+) loss forms, every hit grounded at
  code and classified on the user's central axis (OK-provisioned / DEFECT-lost / DEFECT-should-already / UNCLEAR;
  ambiguous consumer-status ⟹ UNCLEAR, never guessed, #1). Four parallel read-only tracing passes, every candidate
  CC-verified at code. **11 catalogued sites: 2 DEFECT-LOST, 0 SHOULD-ALREADY, 7 OK-provisioned, 3 UNCLEAR** (+2
  LIVE-path overwrite-on-recompute sites considered and ruled OK; +2 new taxonomy forms recorded). **The
  classification hinge:** production runs the LEGACY `analyzeChord`+gates path while Layer 4 (`ChordSliceDecoder`) /
  Layer 5 (`functionoutput`) are Built+Dormant — so most not-yet-consumed signals are the dormant path's correct
  **forward-provisioning** (OK: K1 `SliceChord`, K2 `FunctionLayerOutput` "NO production consumer", K3
  `HarmonicRegion.keyAlternatives/keyConfidence` "IN-MEMORY ONLY, no consumer yet … exists for Layer 5"), and the
  genuine LOST sites are on the legacy path's user-visible carry surface. **The two DEFECT-LOST (the fix-queue, each
  a later ratified event):** (**L1**, HIGH, #4-relevant — already scoped as O-19) Gate A `std::swap` (preserves the
  distinct enharmonic partner) vs FM2 `push_back(buildResult)` (appends a winner near-duplicate, loses it),
  `postscoringgates.cpp:214-234`; consumer PRESENT (`notationcomposingbridge.cpp:298-300`, user-visible) + future L5.
  (**L2**, MEDIUM, #4-relevant, NEW) the legacy `mergeChordAnalysisTones`/`tpcForPc` spelling collapse
  (`analysisutils.h:175-180` + `chordanalyzer.cpp:1229-1240`) — same-pc different-TPC tones collapse to one spelling
  by **iteration order**, destroying a distinct enharmonic spelling; the rebuild L4 already reads per-note spelling
  correctly (shared `lineOfFifths`), so the fix is the named "**second tpc reader**" unification residual (adopt L4's
  reader on the live path — closes a #4 loss + a #6 duplication). **SHOULD-ALREADY empty** is itself informative
  (substrate cleanly provisioned, not mis-wired; the margin-vs-sigmoid gate is a ratified D-L3a deferral, not a gap).
  **The 3 UNCLEAR for user adjudication:** U1 (the `results.size()>=3` cap — which carry surface L5 binds to, legacy
  `results[]` or rebuild L4 full-cube), U2 (J-key-iii leaves the chord = R0, stale-under-new-key alt ranking — the
  canonical "key-then-chord truncation the owed joint step is meant to fix", `regionanalyzer.cpp:369-375`; O-18's
  still-owed joint step is the future consumer), U3 (coalesce bass re-derive — correction or loss, needs a score
  check). **New taxonomy forms:** (+1) honest-unknown-carry (the positive counter-form — `extensionsKnown`/`openMark`/
  `SliceDecision::Abstain`), (+2) recomputable-collapse (a hard value derived from a carried/regenerable source is
  lossless — guards against over-flagging; e.g. `SliceKeyMode.uncertain ≡ confidence<threshold`). READ-ONLY: no
  `src/`/corpus/build/fix; both stops green by construction; suites unchanged. **The fix-queue (L1/L2) + the UNCLEAR
  rows are the user-adjudication surface; each fix is its own later Gate-A-style ratified event.**
- **O-19 (ENGAGE ARC #3 — the GateA promotion-unification design/scoping pass, 2026-07-06;
  `cowork_gateA_unification_design.md` + `cc_engage_gateA_unification_design_report.md`).** Read-only
  restructuring design (the order-of-operations first step) that assembles the ratification surface for the
  held-since-O-11 GateA retirement. **Blast radius re-measured at HEAD on the FULL surface** (HEAD-binary
  `disable_rule GateA` decode, scratch, frozen corpus read-not-written): **36 Baroque scores, 0 winner-diffs /
  352, alternatives-only** — the 2.2c count reproduced and now **enumerated by name** (the 36 `bwv###` stems).
  **Carry-delta content characterized:** on each slice a Minor7-slash winner's **enharmonic Major-add6 partner**
  is retained as an alternative under Gate A's swap (Idiom A) but **overwritten by a freshly-built near-duplicate
  of the winner** under FM2's append (Idiom B) — a §12 information-loss form (e.g. `bwv17.7@19680`
  `[A6,A6,A6]`→`[A6,A6,F#m7/A]`). Snapshot reach = none (no overlap with the 11-stem snapshot corpus).
  **Source characterization:** one real builder `buildChordResult` + **three** thin `buildResult` wrappers (two
  byte-identical gateCtx copies at `postscoringgates.cpp:65` / `chordpostpasses.cpp:129`, one WorkCand variant at
  `harmonicfunctionlayer.cpp:516`; the `chordpostpasses.cpp:128` "…/analyzeChord" comment is stale —
  analyzeChord delegates to `fn::applyHarmonicFunction`), and **two promotion idioms** (swap-existing vs
  append-built) with no shared primitive. **Design:** one `promoteToWinner` primitive with a **present-first
  dedup guard** + one collapsed builder wrapper ⟹ Gate A + FM2 become the two internal branches of one
  promotion ⟹ the separate `GateA` rule removes **byte-identically** (winner AND carry), reproducing C_HEAD.
  **Correct carry = C_HEAD grounded at the O1b carry contract** (retain the distinct partner reading; the
  FM2-append form loses it — the same anti-pollution principle the Gate G-E phantom-pop already applies,
  `postscoringgates.cpp:388-392`), **not** chosen because Gate A sits at HEAD. All Layer 4, in-layer; nothing
  cross-layer. **The 36-score alternatives delta is the user-ratification surface** for the separate build
  event (winner+alternatives byte-diff ×3 expected identical everywhere; both stops green by construction;
  suites/snapshots unchanged). No `src`/corpus/build/push-of-behavior-change. **O-11 retirement condition now
  has its ratification surface.**
- **O-19 (ENGAGE ARC #12 — the joint key↔chord step's benefit MEASURED = it barely pays, and not at all on its
  scoped population, 2026-07-07, session 35; `cc_engage_stage3_joint_measure_report.md` + data
  `tools/reports/joint_probe_measure.json`).** Stage 3 opens measurement-first (#1/#3/#5): the decisive fact the
  joint-step design (`cowork_joint_key_chord_design.md`) left as owed-2/3 — does re-deciding the chord under
  alternative CARRIED keys improve root-correctness? — measured BEFORE any build (the same guard O-17/O-18 applied
  to F-B). Instrument = default-OFF `--dump-joint-probe` (feat `689840d2ef`) exercising the EXISTING
  `ChordSliceDecoder` as a PURE re-decode fn (`chordslicedecoder.h:524`, "takes one key") under the production
  `HarmonicRegion`'s carried key menu (`keyModeResult ∪ keyAlternatives` + D-L3a `keyConfidence`) — NOT the
  production joint step (no beam/wiring/behavior change; the "faithful mechanism" §2.2 named, run as a probe).
  This is exactly the per-key chord **re-decode O-18 found un-computable read-only** — now computed by the
  standalone probe over the pure decoder (O-18's un-computability was for *production telemetry*; a probe over the
  pure fn is a different, computable thing). Benefit vs the DCML root by the SHARED a8 substrate
  (`_dcml_time_spans`/`_active_index_at`), same as the robust stop (#1). **★ GO/NO-GO (corpus `c50002fee1`, ×3):**
  net corr−harm on the root FLIPS = **+9 / +3 / +10** over ~6200 DCML-scored regions/preset (**+0.05–0.16 pp**;
  oracle ceiling **+0.6 pp**); **harm = 75–90 % of correction** everywhere. On the **coupled minority** (the C3
  population — key sequence margin < 1.0) net **0 / +5 / −2** on n=16/15/11 — zero-to-noise, one preset negative.
  **Fire-rate (owed-1/3):** the chord flips under a carried key in **1.4–1.5 %** of committed regions (0.9–1.4 %
  coupled) — **~10× below** the 13.5 % `decideJointKey` `coupled` proxy; the chord axis is almost always
  KEY-STABLE (carried alts are diatonic-collection siblings ⇒ the diatonic prior barely shifts; fact-grounded #1).
  **Beam width (owed-4):** ~5 carried keys but width-2 captures EVERY available correction. owed-1/2/3 settled
  read-only; owed-4-fixpoint/owed-5/owed-6 build-gated. **Pedal owed-P1:** carry-holds-pedal-root agreement
  0.20/0.50/0.20 — leans to the §6.3 upper-voice-conditioned form, but UNDERPOWERED (n=2–5); flagged not decided.
  **#3:** no new surprise — the design's owed-2 predicted "small"; the measurement sharpens it downward and grounds
  WHY. **Verdict handed up (#8):** the measured evidence does NOT support building the joint step as a precision
  lever — the build decision is Cowork's/the user's, on measured fact. Both stops green **by construction**
  (production byte-identical — 12/12 corpus stems reproduce committed `.ours.json`; no `src/`, no build of the
  joint step, no fit; no golden refresh). Pushed fork-only.
- **O-18 (ENGAGE ARC #2 — the C3 genuinely-coupled key↔chord population MEASURED = UN-COMPUTABLE, 2026-07-06,
  session 25; `cc_engage_c3_measurement_report.md` + `cowork_fb_redesign_design.md` §3.D-2).** The
  specific-research move (#5/#2) the O-17 surprise called for (#3): does F-B's override isolate a net-positive
  correction subpopulation on the C3 coupled minority? Read-only (no `src/`, no build, no telemetry, no corpus
  write, no θ retune). **VERDICT 3 — the C3 trigger is NOT computed anywhere**; it is un-computable read-only
  AND un-surfaceable by additive default-off telemetry. Binding blocker = C3 component **(b)** ("a different
  carried KEY alternative flips the chord reading"): the per-key chord **re-decode** it needs is **the gated
  joint key-and-chord step the contract §6-C3 flags as "still owed at Stage 5"** (`keymodesequence.h:70-72`);
  even the closest mechanism — the J-key-iii joint re-key pass — **explicitly leaves the chord unchanged**
  ("the chord-axis side-effect … is DEFERRED to a faithful mechanism", `regionanalyzer.cpp:369-375`).
  Component (a) is likewise absent from the F-B fullspine chain (`inferLocalKey(...)[0]` + a score-global
  `homeConf` sigmoid, not the per-slice L3 sequence margin — D-L3a's "no sequence-margin substrate on that
  path"; the bar itself is well-defined at source: sequence-margin `uncertainThreshold` 1.0 /
  annotate-gate 0.8, but the bar is not the blocker — (b) is). There is **no already-computed signal to
  surface**; producing (b) would mean **building** the joint step (forbidden #6/#7/#8) — so verdict 3 is a
  **report, not a build** (the dispatch's explicit branch). **Load-bearing consequence:** §3.D-2 (C3-restrict)
  is **removed from the near-term option set** — it is joint-step-gated (a Stage-5+ successor), so the F-B
  frame collapses to **§3.D-1 (annotate-via-open-mark) EVERYWHERE**, floored by disable; recovering the 53
  corrections is a **declared inference-quality question (#8)**. **#3 discharged:** the O-17 surprise
  (contradiction uncorrelated with correctness) is *explained* — F-B fires on any committed-slice-with-a-
  tidier-progression, a population **never filtered for key↔chord coupling**, so it is mis-scoped off the C3
  minority by construction; no residual surprise. Population footing reproduced (1043 = 53 corr + 809 harm +
  181 neutral); complement = the whole population, fourth/fifth harm majority confirmed (472/809 = 58 %).
  **Reproducibility finding surfaced (#16):** the `C:/tmp/c1/fs_*` corpus_manifest is STALE (git_hash
  `d1d4d3d7f0` + sha fingerprints are a Jul-4 leftover; the actual dumps are a Jul-6 `≥c50002fee1` regen the
  fs-driver never re-manifested; `theta_fit` globs directly so the measurement is on the real content) — the
  E0 fs dirs should be re-manifested or the taxonomy scripts should validate. Both stops green **by
  construction** (zero `src/` touched ⟹ byte-identical to HEAD `712830210a` = batch 52/24/52 + robust sandwich
  identity-PASS). On CC's report: Cowork verifies at objects → presents the **annotate(±C3)** build-event
  decision surface to the user (annotate-everywhere now; C3-restrict deferred to the joint step).
- **O-17 (ENGAGE ARC #1 — the F-B fine-grain override REDESIGN design/scoping pass, 2026-07-06, session 24;
  `cc_engage_fb_redesign_design_report.md` + `cowork_fb_redesign_design.md`).** The engage arc's opener,
  read-only (no `src/`, no scoring value, no corpus write, no build, no θ retune — architectural design,
  moratorium-clear; NOT the D-FS θ closure, which Phase 3 already proved a dead end). **The ratified backlog
  pushed fork-only** (`ce509b0961..923f149561`, 76→0; `upstream` untouched). **F-B characterized at the
  source** (`attemptFineGrainOverride`, `functionresolver.cpp:381`; incumbent = the L4 vertical-fit
  `SliceConfidence.composite` — code-truth via `chordslicedecoder.h:404`; contradiction = the coarse
  {0,1,2,3} progression-plausibility count; dormant — only `batch_analyze.cpp:3186`'s E0 harness runs it; NO
  implementation drift, ONE premise-invalidation: §15-2's \"θ accounts for the missing progression term\" is
  refuted). **The 1043/53/809 decomposed at the measured data** (read-only over the existing `C:/tmp/c1/fs_*`
  dumps, `theta_fit`-join reproduced to the unit): the harm rate is **~uniform 71–86 % across every measured
  stratum** (highest harm at the highest L4 confidence ⟹ no θ can separate corrections from harms — the
  code-grounded proof of \"best θ disables it\"); fourth/fifth \"progression tidying\" moves = 55 % of fires /
  58 % of harm; **the discriminator = NONE**; and — the key new result beyond Phase 3 — **the incumbent-repair
  premise is REFUTED at data: even where the selected alternative is vertically ≥ the commit (`g≤0`), harm is
  still 70.8 % (corr−harm −163)**, so making the comparison vertically-fair does not reach net-positive.
  **Options** (each with layer/theory/projected-split/blast-radius/risk): disable-baseline (corr−harm 0,
  +756 recovery — the floor) · gate (degenerates to disable) · incumbent-repair (refuted, large surface) ·
  **re-frame-annotate (§8 case-3 honest carry — 0 harm/0 corr + preserves the 1043 contradiction signals as
  uncertainty; CC's recommendation)** · re-frame-C3 (the correct long-run home = the §6-C3 joint-step
  minority; split UNKNOWN, needs a new measurement — flagged, not assumed). **The 53 lost corrections need a
  correctness-correlated contradiction signal = an inference-quality question, declared to Cowork, out of
  this pass's scope.** Acceptance for the (separately-ratified) build event = the robust-unit stop: class-(b)
  root-disagree DURATION non-increase per preset — dormant ⟹ identity today, must MOVE favorably at engage
  (the 809 harms are ~non-symmetric pitch-class-decidable roots = class-(b), so removing them reduces the
  class-(b) duration). Both stops green (batch 52/24/52; robust sandwich identity-PASS; nothing here touches
  them). On CC's report: Cowork verifies at objects → presents the redesign-option decision surface to the
  user (annotate vs disable vs C3-restrict).
- **O-16 (R10-b — the batch→robust stop handover MADE; STAGE-5 ARC CLOSED, 2026-07-06, session 23;
  `cc_stage5_r10b_ratification_report.md`).** The user's arc-closing ratification event on the R10-a surface.
  Docs + one-JSON-snapshot only — NO `src/`, NO scoring value, NO corpus write, NO build, NO push (outside the
  inference-fixing moratorium: this is regression-STOP infrastructure, not an analyzer change). **(i)** CLAUDE.md
  gate section rewritten to four blocks: (A) the robust-unit regression stop is now THE hard stop (granularity-robust
  union-of-boundaries, variant (b) DCML-only, duration-weighted; root governs, RN+key tracked; reference
  `tools/robust_stop/`; hard stop = class-(b) root-disagree DURATION non-increase per preset + mandatory explained
  run-diff; runnable `a8_rebaseline_measure.py`→`robust_stop_diff.py` ≈6 s; re-baseline discipline generalized from
  2.2e); (B) the two-tier per-cell class policy preserved LIVE (all five guardrails + founding evidence
  `bwv272@4320`/`bwv289@20160`/`bwv291@17760`/`bwv387@10560` intact), now governing the robust unit's per-cell
  classification; (C) the batch 52/24/52 `stem@tick` sets + full L3-wiring/2.2e/corrected-parser history RELOCATED
  to a retrospective, marked superseded (under-counted true per-onset error ~15–56×); (D) caveats — cross-layer-budget
  (O1) kept LIVE, granularity caveat marked ✅ RESOLVED (R10-b delivers the mandated granularity-robust metric).
  **(ii)** The 2.2e KEY-column error corrected `68.19/64.52/67.77`→`68.13/64.43/67.50` in CLAUDE.md (block A) + the
  contradictory "reflects the a8 re-measure" sentence replaced with the byte-identity truth (Jazz key = the prior
  64.43 exactly; identical inputs cannot move it). Repo-wide grep dispositioned: 1 live-normative corrected (CLAUDE.md),
  1 historical design-log line annotated (this doc §2.2e-executed), the rest (O-15/STATUS logs, `tools/robust_stop/`
  README+manifest reproduce-status records, fit-ledger audit `key_pct` data, font-glyph false positives) left as
  history/data. **(iii)** Batch sets frozen in BOTH forms: CLAUDE.md block (C) + machine-readable
  `tools/robust_stop/batch_stop_frozen_history.json` (set-equal to `characterise_bir_false.py` output AND to the
  CLAUDE.md sets, verified before write). **(iv)** `characterise_bir_false.py` → KEPT-AS-DIAGNOSTIC (R3). **(v)** Both
  stops green at close (batch 52/24/52 set-diff empty ×3; robust sandwich identity-PASS +0/−0, class-(b) Δ=0 all
  presets). Corpus fingerprint-validated untouched (`c50002fee1`). No src/corpus/build/push. **Roadmap R10 FIRED;
  §4.7 executed; the Stage-5 arc is CLOSED. The engage arc inherits: F-B redesign [1043/53/809] · §15-13 [5544,
  parked] · θ/map wiring · L1.5 surface map · GateA unification · the L5 inversion · tonicVote.**
- **O-15 (R10-a — the batch→robust stop handover surface ASSEMBLED, 2026-07-06, session 22z;
  `cc_stage5_r10_assembly_report.md`).** Measurement + draft only; NO normative doc change, NO committed
  value, NO corpus write, NO push — the §4.7 R10 decision surface is now assembled for the user's R10-b
  ratification (the handover itself: the CLAUDE.md gate rewrite, the batch-set freeze-as-history, firing
  roadmap R10). **(i) The committed robust-unit reference** lives at **`tools/robust_stop/`** (the diff
  base, the batch-stop's `stem@tick`-set analogue that lives as artifacts because it is ~6.9–7.0k failing
  runs/preset, not 52 lines): per-preset variant-(b) DCML-only root-failing RUN enumerations
  (`stem@runStartTick`, **6868/7036/6883** Baroque/Jazz/Default) + `summary.json` + `manifest.json`
  (corpus `git_hash c50002fee1` · instrument `a8_rebaseline_measure.py@c2914884af` · reproduce-status) +
  `README.md`; generated by the pinned a8 instrument (self-validated grid==oracle on all 326×3). **(ii) ★
  THE KEY-COLUMN FINDING (CC-declared, user-ratified Option-1):** the a8 re-measure reproduces **root
  (63.36/62.37/63.25) and RN (44.58/42.40/44.41) EXACTLY**, but **key = 68.13/64.43/67.50 (the PRIOR
  baseline), NOT the 2.2e-recorded 68.19/64.52/67.77.** Jazz is the proof — byte-identical `.ours.json`
  (2.2e-proven) + WiR + git-unchanged key-path code since `c50002fee1` ⟹ Jazz key MUST equal 64.43
  (measured 64.4321); the recorded 64.52 is unreproducible and self-contradictory ("an a8 re-measure over
  byte-identical inputs cannot move the figure"). Root — the governing metric + dispatch STOP anchor —
  holds; key is tracked-beside; the reproducible values are frozen in the reference and the **2.2e
  key-column error is a DECLARED finding for R10-b to correct** (the CLAUDE.md dual-track note's
  `68.19/64.52/67.77` → `68.13/64.43/67.50`; a normative change reserved for the handover). This is a
  *record* discrepancy in a tools-side metric column, not an inference/behavior problem (corpus
  fingerprint-pristine, instrument self-validating, root/RN exact). **(iii) The old→new mapping:** every
  **52/24/52** batch case (set-equal to `characterise_bir_false.py`) maps to a still-failing variant-(b)
  run — **0 disappear**, all presets (1 Baroque/Default overlap-only `bwv261@33840`, benign; the 2/1/2
  variant-(a) disappearances are the known §3.2 alignment artifact). **(iv) The successor sandwich —
  runnable + timed:** new instrument **`tools/robust_stop_diff.py`** (thin orchestration over a8 outputs,
  constraint-10 — re-implements no scoring/comparison; the robust analogue of `characterise_bir_false.py`);
  the check = `a8_rebaseline_measure.py --out-dir <cand>` (**≈6 s**, dispatch predicted ~14 s) +
  `robust_stop_diff.py --candidate <cand>` (**<1 s**); **hard stop = class-(b) root-disagree DURATION
  non-increase per preset** (class-(b) ≈96.5 % of root-fail time — the §4.2 finding: the batch residual's
  ≈53 % class-(a) was a small-reachable-corner artifact) + a **mandatory explained run-level set-diff** +
  class-(a) duration tracked (INVESTIGATE flag, advisory). Proven end-to-end: identity self-compare PASS
  (empty diff, Δ=0), a synthetic perturbation proving the FAIL/diagnostic/INVESTIGATE paths (exit 1), and a
  raise-on-unmatched-line guard that fixed a real 96-run silent-drop bug (the hyphen stem `bwv248.33-3`).
  **(v) `characterise_bir_false.py` → KEPT-AS-DIAGNOSTIC** (R3 pattern): its `validate_corpus_dir` is
  imported by the a8 instrument, so its load-bearing half cannot bit-rot into uselessness; only the
  per-region 52/24/52 enumeration freezes as history. **(vi) The DRAFT CLAUDE.md gate-replacement text +
  the cost/practicality note** live in the report (report-only). §4.7 R10 decision surface: ASSEMBLED;
  R10-b (the ratification + handover commit) is the remaining, arc-closing event.
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
