# Phase 5c — Architectural Layer 5 (FUNCTION) build plan

> **Status: DRAFT (2026-06-26).** The incremental, investigate-each-step build of the **function layer**, against the
> SIGNED `cowork_layer5_function_design.md`. Same shape as the L4 build (`cowork_phase5b_l4_build_plan.md`): build the
> layer **DORMANT** (production byte-identical), each increment **investigate → build → measure**, **default constants
> only** (the firewall — no accuracy tuning here), and a per-step gate. **Engagement** (the production switch + legacy
> retirement) is the **joint L4+L5 step (Phase 5d)** per the ratified engage-with-L5 strategy — it is *not* part of this
> phase. Prerequisites are met: the L4 decoder (dormant), the L3 region key-alternatives forward-carry, the phrase-boundary
> primitive (dormant), and the metric-weight contract.
>
> **★ Proportionality (standing, user-ratified).** The SOTA reference (Contrapunctus) is competitive with **no** explicit
> phrase/cadence/function layer; the measured function-only residual is small. So **build the mechanisms right at their
> defaults and stop** — do not chase accuracy, do not tune (Phase B). The point of L5 is the explainable decomposition +
> the tonicization-vs-modulation distinction, not a number.

## The build discipline (every step)
- **Dormant + byte-identical.** L5 is built behind a capability gate (default OFF), consuming the dormant L4 decoder's
  output + the dormant phrase-boundary/cadence primitives. Production is untouched: corpus **53/24/53**, both suites, the
  snapshots — unchanged by construction at every step. Movement → STOP.
- **Investigate first.** Each step opens with a read-only confirm of the as-built reuse landscape + the input contract,
  and reports before building (so a surprise amends later steps, or the layer design, before it compounds).
- **Default constants (the firewall).** Build the mechanism + its direction; leave every weight/threshold/margin at the
  spec's stated default. No accuracy tuning — that is Phase B, after the whole stack is built.
- **Reuse, do not duplicate.** Consume the existing primitives the spec names (the dormant `tonicizationlabeler`,
  `cadencekeyanchor` salience/`endsPhrase`, `formatRomanNumeral`, the phrase-boundary view, the proto-functional gate
  heuristics) rather than re-implement; unify the two tonicization paths.
- **The gate criterion (the L4 lesson).** Judge each measurement by **coverage-matched accuracy + correct abstention**,
  never raw coverage — abstaining correctly on a genuinely function-undecidable slice is a *right* outcome.

## Step 0 — Investigate / confirm (read-only) — STOP & report
Confirm, at source, that the L5 inputs and reuse targets are as the spec assumes, and report the reuse-vs-build map:
- the **L4→L5 contract** is consumable from the dormant decoder (the `OpenQuestionLabel`, `AmbiguityKind`, ranked
  `alternatives`, `SliceConfidence`, per `chordslicedecoder.h`);
- the **L3 region key-alternatives forward-carry** (the `keyAlternatives`/`keyConfidence` siblings) reaches L5;
- the **phrase-boundary primitive** (`phraseBoundaryTicks` / the texture strength) is consumable;
- the **reusable function machinery** (dormant `tonicizationlabeler`, `cadencekeyanchor` `endsPhrase`/salience, the
  `formatRomanNumeral` RN/aug6/applied emission, `diatonicDegreeForRootPc`, the `wSeq`/`wDim`/`resolutionEdge`/Gate-E/J
  proto-functional heuristics) — confirm each is reusable and where it plugs in;
- the **misnamed predecessor** (`harmonicfunctionlayer` = chord-identity competition, not function) and the **placement**
  for the new function layer. Report; the rename is an engage-step structural item, not now.
If any input/contract is not consumable, or a structural change beyond the dormant layer is needed → **STOP and report.**

## Step 1 — The progression model + base Roman-numeral derivation (§5.0, §5.1)
- Build the **licensed-progression test** (§5.0): the enumerable set of standard functional root motions (descending-fifth
  dominant; descending-third / ascending-second functional step; applied/leading-tone resolution to target; cadential
  motion) over the committed-chord stream — the resolver's and cadence's shared evidence. Plus "prevailing harmony" and
  "established next function" as defined.
- Build the **base RN derivation** (§5.1): degree (+ chromatic alteration), quality, inversion — reusing
  `diatonicDegreeForRootPc` + `formatRomanNumeral`. Deterministic; no judgment beyond key+chord.
- **Measure/gate:** dormant, byte-identical; unit tests (a licensed vs unlicensed motion; a base RN spot-check).

## Step 2 — The cadence detector (§5.2) — its own sub-unit
- Build the **key-agnostic, event-pair, feature-scored** detector per §5.2: the **cadential-six-four collapse first**; the
  authentic test (bass 5→1 ∧ leading-tone **resolution** ∧ genuine dominant); the **typology** (perfect/imperfect by the
  **bass-derived inversion** criterion — the top-voice arrival only a soft optional nudge per the §5.2 amendment; half
  incl. Phrygian; deceptive; plagal/evaded lower-confidence); the **chorale phrase-gate** (consume the phrase-boundary
  primitive); each admitted cadence casts the **weighted tonic-vote**. Rebuild on the dormant `cadencekeyanchor`
  primitives (`endsPhrase`, `chromaticLeadingTone`, the key-agnostic frame); **retire the circular production detector's
  logic into this one** (the broken key-dependent `sectioncadencedetection` PAC/IAC is replaced — but its retirement is an
  engage-step action; build the correct one dormant first).
- Likely its **own internal unit** consumed by both Step 4 (resolver) and Step 5 (modulation) (§15-4).
- **Measure/gate:** dormant, byte-identical; oracle tests (PAC vs IAC by inversion; Phrygian half; deceptive; the
  six-four collapse; the tonic-vote weight); expect **HC the weakest** (literature) — held at low confidence, not chased.

## Step 3 — The resolver (§5.5) + the fine-grain override (the §8 case-4 channel #2)
- Build the **resolver**: for each L4-abstained slice, **select among the carried readings** by the named ambiguity kind
  (transition / share-tone / relative-pair / close / insufficient), using the progression model (Step 1), the cadence
  tonic-vote (Step 2), and the **soft bass-degree prior** (§5.7). Never re-derive; carry the honest **open mark** where
  undecided.
- Build the **fine-grain override** (§5.5 case-4 clause / §10): override a *confident* L4 fine-grain commit the function/
  cadence contradicts (the class-(b) override duty), by selecting the corrected reading from the carried alternatives /
  neighbouring committed harmony — via the **§8 confidence-weighted-threshold + one-pass-closure** mechanism (build this
  shared mechanism here; Step 4 reuses it).
- **Measure/gate:** dormant, byte-identical; the class-(b) override drives the projected transients toward zero
  (coverage-matched + correct-abstention judged, not raw coverage).

## Step 4 — Tonicization vs modulation (§5.3) + the modulation recompute (§5.4, case-4 #1)
- **★ REUSE, do not re-implement (Step-0 F2, verified):** the dormant **`localmodulationdetector`** (`detectLocalModulations`)
  already commits a local-key span on **established + cadence-confirmed** — "exactly the brief-vs-sustained signal that
  separates a real modulation from a passing tonicization," key-agnostic and byte-identical; and its **re-key (Stage 4d-ii)**
  + **`jointkeydecision`** are the §5.4 recompute substrate. Build §5.3/§5.4 by **unifying these** (+ the J-key-iii re-key
  path), not a fresh implementation.
- Build the **default-tonicize** rule + the **cadence-confirmation gate** + the **persistence change-cost (hysteresis)**
  over the L3 local-key carry (§5.3); the break-even default-to-tonicization; consume the **notated-spelling key signal**
  here (function-gated). *(Where the existing detector's persistence is a **sustained-run gate** and §5.3 specifies a
  **change-cost/hysteresis**, adapt the existing cadence-confirmed substrate to the §5.3 hysteresis — reuse the mechanism,
  match the spec's persistence form.)*
- Build the **modulation recompute** (§5.4): on a confirmed modulation, the **localized, forward, convergence-bounded**
  re-read of the region, via the §8 mechanism (reuse Step 3's). 
  - **★ Honor the two standing pins here (the spec's §15-3):** (a) **pin the region key-alternatives reduction precisely**
    — replace the L3 forward-carry's byte-identical v1 (representative-slice alternatives) with the reduction this override
    actually selects among, and update the carry + its lock-in test; (b) **re-derive the carry in the J-key-iii re-key
    path** so the carried menu cannot go stale against an overridden key. Both are first tasks of this step.
- **Measure/gate:** dormant, byte-identical; oracle tests (tonicization stays home; cadence-confirmed modulation re-reads
  the region; the relative-pair tonic-vote).

## Step 5 — Relational labels (§5.6) + unify the tonicization paths
- Build the **applied/secondary, Neapolitan, augmented-sixth (spelling-aware, the Ger6↔V7 spelling pin), modal-mixture**
  labels on their defining triggers (§5.6), in the fixed **precedence** (aug6 → Neapolitan → applied → mixture).
- **Unify** the two tonicization paths: the dormant `tonicizationlabeler` (keep its chromatic-LT guard) and the inline
  `formatRomanNumeral` applied path → one owned emitter. (The unification *lands* at engage to stay byte-identical; build
  the unified emitter dormant.)
- **Measure/gate:** dormant, byte-identical; oracle tests (V/x target; bII6; It/Fr/Ger by spelling; mixture as residual).

## Step 6 — Output assembly (§7)
- Assemble the L5 output: the **Roman numeral** (full DCML/RomanText completeness, no simplification — §3 Produces), the
  **function confidence** (from cadence-vote / licensed-progression fit / margin), the **open mark** on the genuinely
  undecided, the **cadence + key markers**, and the L5→L6 (grouping) contract. *(The T/S/D derived read-out is deferred —
  §9-D1.)*
- **Measure/gate:** dormant, byte-identical; the output contract is shape-tested.

## Step M — Measure + the engage GO/NO-GO (read-only)
- Run the full dormant L1→L5 spine over the corpus (diagnostic path, both presets): **coverage-matched RN accuracy +
  correct-abstention**, the **class-(b) hard-stop** projection, the function-only residual, and how much abstention L5
  resolves vs correctly carries. This is the data for the joint-engage decision (Cowork + user) — *not* an accuracy chase.

## Phase 5d — Joint L4+L5 engagement (the ratified engage-with-L5 step; NOT this phase)
Switch production onto the new L1→L5 spine and retire the legacy, **gated by the two-tier BIR (zero new class-(b), the
case-identity set, both presets)**. Lands together: the production switch; legacy retirement (the circular cadence
detector, the legacy `analyzeChord` path, one of the two segmenters / pitch-context builders); the **tpc-fold** (the
inline `chordanalyzer.cpp` tpc cluster → `spellingview`); the marker refinements (§11-2b eligibility + tempo-change-only);
the §15 deferred L4 refinements (O2 inherit, C2 types); the coverage seal. **Phase B precision-tuning follows engagement.**

## Deferred / not in Phase 5c (named, not built)
The T/S/D read-out (§9-D1); the §15-O2 bounded-window joint; the global-regulariser/IDyOM phrase cues; the
`harmonicfunctionlayer` rename + the function/ directory split; all threshold/weight tuning (Phase B).
