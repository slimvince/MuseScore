# The cross-layer confidence & calibration contract (review amendment A-1)

> **Status: RATIFIED (user, 2026-07-02).** Written per the ratified review amendment A-1
> (`cowork_architecture_review_2026_07.md` F-1/F-16). This is a **contract document** — it fixes definitions,
> normalization requirements, comparison rules, and calibration obligations; every numeric constant stays a
> precision-phase (Stage-5) value. Architecture home: the §2.15 contracts (`ARCHITECTURE.md`); the §8
> forward-override (`cowork_layer5_function_design.md` §8) is its principal consumer. As-built formulas below are
> from the specs and session records read 2026-07-02; the exact source-level inventory is a **rider on the CC
> gap-analysis** (`cc_instruction_gap_analysis_spec_vs_impl.md`, Rider 3/6) — items depending on it are marked
> **[as-built: verify]**.

## 1. Why this contract exists

Every decision layer publishes "a confidence", and the architecture's signature control-flow mechanism — the
confidence-weighted forward-override — **numerically compares** quantities across layers: a later layer's
contradiction strength against an earlier layer's confidence. Today those quantities are incommensurable by
construction (review F-1): L3 publishes a sequence-margin, L4 a three-part composite, L5 an **unbounded additive**
combined score while the §8 mechanism clamps to [0,1] (the L5-close D3 clash). Stage-5 weight fitting cannot repair a
comparison between quantities with undefined semantics — it would only bury the incoherence in fitted constants. This
contract defines the semantics once, so every override bar, resolver tie-break, and the future gated joint step
operate on declared, comparable quantities.

## 2. Definitions — the two admissible confidence classes

Every published confidence declares exactly one **class**:

- **Class M — decision margin.** "How much better is the chosen reading than the best *different* reading, under this
  layer's own scoring?" A margin is a **rank statement**, not a probability. Raw margins are unbounded and
  scorer-scale-dependent, so a Class-M confidence is published only **squashed to [0,1]** by a fixed monotone map
  (the map's constants are precision-phase; the map itself is declared per layer). Class M is what every layer can
  compute today.
- **Class P — calibrated probability.** "With what empirical frequency is a decision at this confidence correct,
  measured against ground truth?" Class P is the **Stage-5 target**: a fitted reliability map per (layer × decision
  type) converts the Class-M value into Class P. Until fitted, no layer may claim Class P.

**Rules of use:**
- **U1.** A confidence attaches to a **named decision** (key-of-slice, chord-of-slice, membership-of-note,
  cadence-vote, boundary-strength, function-of-unit) — never to "the layer" in general.
- **U2.** At a **layer boundary** (any value another layer may read), a confidence is **[0,1], class-declared, with
  its decision named**. Unbounded internal scores are permitted *inside* a layer but must be squashed at the boundary.
- **U3.** A consumer may compare two confidences **only within one class and one declared frame** (§4). Treating a
  Class-M margin as a probability (or comparing two Class-M values produced by different scorers without a declared
  conversion) is a contract violation.
- **U4. Provenance.** A carried-forward confidence keeps its (source layer, decision, class) identity; no silent
  re-interpretation downstream.
- **U5. Abstention.** The "uncertain" mark ≡ the decision's confidence is below the layer's declared bar (a
  precision-phase constant). Abstention semantics are therefore uniform: *low confidence in the declared class*, not
  a separate ad-hoc judgment.

## 3. Per-layer inventory (what each layer publishes, in contract terms)

| Layer | Decision | Published confidence (boundary form) | Class | Notes / as-built deltas |
|---|---|---|---|---|
| L1 / L2 | none | — (facts carry no confidence) | — | By design. |
| L1.5 phrase-boundary | boundary-at-tick | graded boundary strength, max-normalised per profile → [0,1] | M (salience-margin variant) | Relative salience within the profile — **comparable within one score's profile only**; consumers (L5 phrase gate, L6) must not compare across scores. |
| L3 key/mode | key/mode-of-slice | sequence margin: best total vs best total forced-different-at-this-slice, squashed | M | The right definition (whole-sequence, not local top-2). **Delta D-L3a:** the spec also stamps a C1 emission `normalizedConfidence` (sigmoid) on the chosen key — TWO numbers ride the boundary; the contract requires ONE declared boundary confidence (the sequence margin) with the emission sigmoid demoted to internal/diagnostic. **[as-built: verify]** The deferred "sequence-margin confidence redesign" (L3 §status) folds into this contract. |
| L4 chord | chord-of-slice (+ per-note membership) | composite: margin ⊕ sufficiency ⊕ membership-cleanliness, squashed | M (declared-composite) | Components + monotone combination declared (§5 R4). **Vertical-fit-only by construction** (no progression signal) — a declared property the L5 override frame (§4) must account for, not a defect. Alternatives capped (topK), spelling-pinned siblings excluded — declared carry limits. |
| L5 function | RN/function-of-unit; cadence; modulation | three fixed components (cadence-vote attribution, licensed-fit, resolver margin) combined at default weights — **must publish squashed [0,1]** | M (declared-composite) | **Delta D-L5a (= review F-1 / L5-close D3):** as built, `FunctionConfidence.combined` is an unbounded additive (observed up to ~5.0) while §8's `earlierConfidence` is [0,1] — the boundary squash required by U2 is missing. Fix at the D3 close-out: keep the additive internally, publish the squashed form. |
| L5 cadence vote | tonic-of-span evidence | weighted vote (monotone sum of evidence + salience − type discount) | M (evidence weight) | Votes are **evidence**, not boundary confidences: they enter §4 frames as contradiction strengths. Their scale is fixed by the same squash discipline when compared against a key confidence (frame F-A below). |
| Legacy path | region key/chord | `normalizedConfidence` sigmoid + known sentinels (0.0 / 0.5 hard-coded — Stage-1c G4) | nominally M, unreliable | Documented unreliable (post-promotion re-rank without recompute). **Retires at engage** (the ENGAGE CRITERIA + RETIREMENT MAP block in `docs/implementation_roadmap.md`, R8); the contract does not attempt to repair it. |
| **VL-C texture (axis 2)** | **texture-of-span** | the best-vs-second-best **fit** margin, where fit = `exp(−distance/fitScale)` of the z-space (ABz) euclidean distance to a class centroid — already ∈ [0,1) | M | The **axis-2** first judgment component (`cowork_voiceleading_axis_design.md` §5.3; `textureclassifier.h`, DORMANT). The published confidence is the exp-fit margin; squash per **R5** below. The output also carries the **full ranked list of ALL class fits with weights** (zero information loss). Three declared floors — **evidential** (min motion samples), **margin**, **fit** — are precision-phase; abstention = margin < margin-floor OR best fit < fit-floor (contract U5), single-voice → *no-pair* abstention. No new §4 comparison frame (nothing compares a VL confidence against a harmonic one). |

## 4. The comparison frames (the §8 override arithmetic, stated once)

A **frame** is a declared triple *(incumbent confidence, contradiction-strength measure, conversion)* under which one
comparison is defined. The general §8 rule, stated once for all instances:

> **Override fires iff** `S_contra > θ · C_incumbent`, with `S_contra` and `C_incumbent` expressed in the **same
> class and scale** per the frame's declared conversion, `θ` a precision-phase constant, and the tie
> (`S_contra = θ · C_incumbent`) going to the **incumbent** (matches L5 §5.3/§8's strictly-greater rule). Each firing
> is once-per-pass (the one-pass closure ledger) and triggers only the localized forward recompute.

The two built instances, as frames:

- **Frame F-A — cadence-confirmed modulation recompute (L5 §5.4).** Incumbent: L3 key-of-span confidence (Class M,
  squashed sequence margin). Contradiction: accumulated cadential vote weight in the candidate key (Class M evidence
  weight). Conversion: both mapped to the common [0,1] scale by their declared squashes before the θ-comparison.
- **Frame F-B — fine-grain chord override (L5 §5.5 case-4).** Incumbent: L4 composite confidence of a `Commit`
  (Class M; **vertical-fit-only** — the frame's θ accounts for the missing progression term, per L5 §15-2).
  Contradiction: the functional-plausibility score of the contradicting context (licensed-progression fit + cadential
  fit). Selection is restricted to carried alternatives / neighbouring committed harmony (never re-derivation).

**New frames require declaration here.** Any future override site (e.g. the A-4 cadence-less confirmation channels;
the recognition consumer's schema-contradiction override, `cowork_progression_schema_design.md` §2) must add its
frame row to this section before build — an undeclared cross-layer comparison is a contract violation.

## 5. Combination and squashing rules

- **R4 (composites).** A composite confidence declares its components, each component's decision and class, and a
  **monotone** combination. Components may be unbounded internally; the published form is squashed (U2).
- **R5 (squash maps).** Each layer declares one fixed monotone squash for its boundary confidence(s). The map's shape
  is structural (declared here); its constants are precision-phase. Until Stage 5 fits them, defaults hold — the
  point is *declared comparability*, not tuned optimality.
  - **VL-C texture-of-span (axis 2).** Squash = the **difference of the two best exp-fits**, `exp(−d₁/fitScale) −
    exp(−d₂/fitScale)`, where d₁ ≤ d₂ are the nearest and second-nearest z-space centroid distances. Monotone in the
    distance margin and bounded in [0,1) by construction (the exp already squashes the unbounded distance); the single
    constant `fitScale` is precision-phase (default = the median nearest-centroid distance over the study fit set).
- **R6 (no cross-scorer margin mixing).** Two Class-M values from different scorers are comparable only through a
  declared frame (§4) — never ad hoc.

## 6. Calibration obligations (Stage 5)

- **C1.** Measure **reliability** per (layer × decision type): empirical correctness (against DCML/WiR, on the
  granularity-robust unit — review A-8) as a function of published confidence. Deliverable: reliability curves +
  fitted maps that upgrade each boundary confidence from Class M to Class P.
- **C2.** Re-express every frame's θ against calibrated quantities (the fitted maps make `θ` interpretable as an
  odds ratio rather than an arbitrary scale factor).
- **C3.** **The gated joint step consumes only calibrated quantities.** Its trigger — the "flagged minority" of
  genuinely-coupled key↔chord decisions — is *defined* in contract terms: slices where the L3 key confidence is below
  its bar **and** the L4 decision is sensitive to the carried key alternatives (i.e. a different carried key flips
  the chord reading). This closes review F-16's "named but unspecified" trigger at the definition level; the joint
  step's own design doc is still owed at Stage 5.
- **C4.** Calibration is measured per preset/idiom where the idiom changes the scorer's behavior; uncalibrated
  presets carry the **"empirically-unvalidated"** mark (review A-7) until their ground truth exists.

## 7. As-built deltas to close (each a small, bounded fix; verified by the gap-analysis riders)

| # | Delta | Home | Close-out |
|---|---|---|---|
| D-L5a | `FunctionConfidence.combined` unbounded at the boundary (D3) | L5 §7 | **✅ CLOSED (`0a88747e7f`, 2026-07-02, E0′-verified):** `combinedBoundary = combined/(combined+k)` published at the OUTPUT boundary (`functionoutput` — the §7 L5→L6 contract), observed ∈ [0, 0.9619] ⊂ [0,1) over the full E0 range; the §8 sites do NOT read `combined` (verified at source: incumbents are the F-A/F-B quantities below); internal additive unchanged |
| D-FS | The FRAME CONTRADICTION scales are undeclared: F-B's `bestPlaus − committedPlaus` (plausibility diff) and F-A's `cadentialWeight` are unbounded/unsquashed while their incumbents are [0,1] — the live commensurability gap behind the E0 override net-harm (968 fires / 45 corrections) | §4 frames / `forwardoverride` call sites | declare both scales (observed ranges measured at E0′ #9 rider); squash-map shape + θ fitted at Stage-5 calibration (C2) — no behavior change before then |
| D-L3a | two key confidences ride the boundary (sequence margin + C1 emission sigmoid) | L3 wiring | declare the sequence margin THE boundary confidence; demote the sigmoid to diagnostic |
| D-LEG | legacy sentinels (0.0/0.5) + post-promotion staleness | legacy resolver | no repair; retires at engage (A-2 map) |
| D-INV | exact formulas/ranges at source for every row of §3 | all | gap-analysis Rider 6 (confidence inventory) confirms or corrects §3 |

## 8. Ratification asks

1. The two-class model (M now, P at Stage 5) and rules U1–U5 / R4–R6.
2. The frame table (§4) as the single home of override arithmetic — new frames declared here before build.
3. The joint-step trigger definition (C3).
4. The close-out list (§7) — D-L5a and D-L3a as small byte-visible-only-in-dormant fixes, D-INV via the gap-analysis.
