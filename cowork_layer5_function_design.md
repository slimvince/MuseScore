# Architectural Layer 5 — FUNCTION (Roman numeral, cadence, tonicization) — Architecture & Design

> **Status: DRAFT for review (2026-06-26).** First spec of the function layer, grounded in `cowork_layer5_function_methods.md`
> (research-first synthesis: three internal source surveys + two primary-sourced external literature passes) and the
> ratified architecture (`cowork_target_architecture.md`, the L4 spec §15-O1). It is written to the design-doc standard:
> every decision path is specified by a **rule** (no preference-shaped holes), the prose is **code-free** (mechanisms are
> named by their role; the as-built mapping lives in §13), and it uses only **standard music-theory vocabulary**. This
> document reads the same whether or not anything is built. Nothing is built yet — the incremental build (investigate-each-
> step, as for L4) follows ratification.
>
> **Scope decision on record (user, 2026-06-26):** the layer's output is the **Roman numeral** — the most precise, complete
> analysis. The three-role summary (tonic / subdominant / dominant) is a **lossy, deterministically-derivable read-out**,
> not a stored output; it is built only if and when an accessibility/teaching display needs it, and never drives analysis.
> A first-class three-role analysis is **rejected** (it would invent judgments no data can verify). See §9-D1.

## 1. Introduction & purpose
The function layer reads the **chord** (decided by Layer 4) **in the key** (decided by Layer 3) and produces the
**Roman numeral** — the chord's identity relative to the prevailing key: its scale-degree, quality, inversion, any
chromatic alteration, and its relational role (applied/secondary chord, Neapolitan, augmented sixth, modal mixture). In
the settled architecture this is "mostly a derivation once key and chord are known."

Beyond the derivation, the layer carries **three jobs the lower layers structurally could not do**, because each needs
evidence that only appears once chords are read in sequence within a key:

1. **Cadence detection** — locate and classify the points of harmonic closure (the perfect and imperfect authentic
   cadence, the half cadence including its Phrygian form, the deceptive cadence, and — at lower confidence — the plagal
   and evaded cadences). A cadence is a function-level event (a dominant arriving at, or being denied, a tonic), so it
   belongs after key and chord, never inside the key layer.
2. **Tonicization-versus-modulation arbitration** — decide whether a passage that leans toward a non-tonic degree merely
   *tonicizes* it (the music stays in the home key) or *modulates* to it (the home key changes). This is the single
   largest share of the residual the lower layers hand forward, and it is a function-level judgment by definition.
3. **Resolution of the carried "uncertain" readings (the ratified O1 role)** — Layer 4 commits the chords it can decide
   on the notes and key alone, and for the rest it **abstains**, handing forward the competing readings it carried plus a
   named open question. The function layer resolves each such slice **by selecting among the readings Layer 4 carried**,
   using cadential and progression evidence — never by re-deriving a chord from the raw notes and never by inventing one.

The layer's reason to exist is that these three jobs share one body of evidence — chords read in sequence within a key,
anchored by cadences — and that evidence is exactly what distinguishes the readings the lower layers had to leave open.

## 2. Constraints
- **Forward-only.** The layer consumes Layers 1–4 and produces function; it does not feed them. Its one exception is a
  **single, gated, localized forward-recompute**: when it confirms a *modulation* (a key change), it triggers a bounded
  re-run of the dependent layers over the affected region with the new local key — a forward consumer acting on a decided
  fact, not a request travelling backward. The bound and the trigger are specified in §5.4; the rule that keeps it from
  becoming a back-edge is in §8.
- **Selection, not re-derivation.** For every uncertain slice, the layer's candidate set is **closed by Layer 4** (the
  carried readings). It selects among them; it never re-scores from the notes nor introduces a chord Layer 4 did not
  carry. This is the structural content of the O1 resolution.
- **Spelling-aware where, and only where, the distinction is a spelling distinction.** Two function labels are
  pitch-class-identical and separable only by notated spelling and resolution (the German augmented sixth versus the
  dominant seventh; an applied leading-tone's secondary leading tone). For these the layer reads the notated spelling
  through the one shared spelling interpreter. Elsewhere it does not depend on spelling.
- **Build it right, do not tune it.** This document specifies the *mechanisms and their defining rules*. The numeric
  calibration of any threshold or weight on hard cases is deferred to the precision-tuning phase (the firewall). A rule
  here states *what* evidence decides a case and *in which direction*; it does not fix the exact constant.
- **Correctly-sized ambition (the cross-layer budget).** The genuinely function-only residual is small and concentrated:
  pitch-class-identical share-tone chords on the chord side, and the relative-major/minor and tonicization-versus-
  modulation distinctions on the key side, plus the genuine transition and close-margin ties. The layer is a derivation
  plus a constrained selector plus cadence and tonicization arbitration — not a heavy new inference engine.
- **Output is the Roman numeral.** The three-role summary is a derived read-out only (§9-D1).

## 3. Context & scope (external view)
**Consumes:**
- From Layer 4, per slice: the committed chord where Layer 4 committed; and where it abstained, the **carried readings**
  (the chosen reading, the best competing reading, and the ranked alternatives), the **named open question** (which axis
  is in dispute — root or quality — and the kind of ambiguity), and the **confidence** components.
- From Layer 3: the prevailing **local key and mode** over the region, carried with its own alternatives and uncertainty.
- From Layers 1–1.5: the per-note **notated spelling**, the **bass** of each slice, the **soprano** (outermost) voice,
  the **metric weight** of each slice, and the **phrase boundaries** (notably the fermata, the reliable phrase-end marker
  in chorales).
- The section/phrase segmentation already available to the pipeline.

**Produces:**
- The **Roman numeral** per analysis unit (the chord read in its key: degree, quality, inversion, chromatic alteration,
  and the relational label — applied/secondary, Neapolitan, augmented sixth, mixture).
- **Cadence markers** (type and location) at the points of closure.
- The **tonicization-versus-modulation** decision, expressed as the existing notation distinguishes them: a tonicization
  stays in the prevailing key and is written as an applied chord; a confirmed modulation changes the local key.
- The **resolved reading** for each formerly-uncertain slice (a selection among the carried readings, with a function-
  level confidence and, where it remains genuinely undecidable, an honest residual mark carried to display).

**Does not do (out of scope):**
- **Prolongation or reduction** (phrase-level reduction of a passage to one underlying harmony; Schenkerian or
  time-span/prolongational reduction). That needs grouping and metre and whole-piece recursive parsing and belongs to a
  later layer; the function layer borrows only a light metric/phrase-position weight.
- **Accuracy tuning** of its thresholds on hard cases (the firewall — the precision phase).
- **Grouping/merging** of adjacent same-label slices for display (the cosmetic layer above; it inherits this layer's
  correctness and must not feed back).

## 4. Solution strategy
The layer runs as a forward pass over the key-and-chord stream, in this order:

1. **Derive the base Roman numeral** for every analysis unit from the prevailing key and the committed chord (degree from
   the root relative to the tonic; quality and inversion from the chord; chromatic root spelling where the degree is not
   diatonic).
2. **Detect cadences** key-agnostically, on the *event pair* (the chord approaching a point of arrival and the chord of
   arrival), scored by a feature test (§5.2). Each surviving cadence then casts a **weighted vote for the tonic** of its
   region.
3. **Arbitrate tonicization versus modulation** (§5.3): default to tonicization (the home key holds, the chromatic chord
   is written as applied); promote to a modulation only when a cadence confirms the candidate key *and* the music
   persists in it. A confirmed modulation triggers the gated localized recompute (§5.4).
4. **Resolve the carried uncertain readings** (§5.5) by selecting among Layer 4's carried readings, using the cadence and
   progression context the layer has just established, plus a soft bass-scale-degree prior. The selection is per the named
   ambiguity kind.
5. **Emit the relational labels** (§5.6) — applied/secondary, Neapolitan, augmented sixth, modal mixture — each on its
   defining trigger, spelling-aware where the distinction is a spelling distinction.
6. Optionally **derive the three-role read-out** (§9-D1) by a fixed lookup; not part of the analysis.

Steps 2–3 establish the cadential/keyed frame; step 4 spends that frame on the open questions. The ordering is not
incidental: a slice's resolution often depends on a cadence detected a few slices later, so cadence and key arbitration
precede resolution.

## 5. Building-block view (the internal rules)

### 5.1 Base Roman-numeral derivation
For each analysis unit with a committed root, quality, inversion, and a prevailing key: the **degree** is the root's
position relative to the tonic; where the root is diatonic the degree is the plain scale-degree, where it is chromatic
the degree is written with its alteration (a lowered or raised degree prefix) without changing the local key. The
**quality and inversion** come from the chord. This step is a deterministic reading; it introduces no judgment beyond the
key and chord it is given.

### 5.2 Cadence detection (key-agnostic, event-pair, feature-scored)
A cadence is tested on an **event pair** — the approach chord and the arrival chord — never on a single chord's interval
content. The rules:

- **Cadential six-four collapse first.** When the approach is a second-inversion tonic-spelled sonority over a bass
  scale-degree five that proceeds to a root-position dominant over the same bass, it is the dominant's accented
  suspension, not a tonic arrival: collapse the pair into a single **dominant approach** so the cadential bass reads
  five-to-one. A second-inversion tonic spelling never registers as a tonic arrival.
- **Authentic cadence** requires the *sequence* (a pre-dominant, then a dominant, then the tonic arrival), and at the
  pair: the **bass moves scale-degree five to one**, the **leading tone resolves to the tonic** across the boundary (the
  resolution, present as an event — not merely the leading tone being sounded, which is the third of every major triad
  and is the false-positive trap the prior detectors fell into), and the dominant is a genuine dominant (a seventh or its
  tritone resolving). Within the authentic family:
  - **Perfect** when both the dominant and the tonic are in **root position** and the **soprano arrives on the tonic**.
  - **Imperfect** when the motion is dominant-to-tonic but at least one of those fails — an inverted chord, a soprano on
    the third (or fifth), or a leading-tone-chord substitute for the dominant.
- **Half cadence** is a phrase ending **on the dominant** that does not proceed to the tonic; the dominant is preferentially
  a root-position triad (a seventh implies onward motion and weakens the reading). The **Phrygian** half cadence (minor
  mode) is the special case of a first-inversion pre-dominant moving to the dominant with the **bass descending a
  semitone** into it. Half-cadence identity depends on the phrase boundary, and is the weakest reading — held at lower
  confidence by rule.
- **Deceptive cadence** is a dominant set up to cadence that arrives instead on the submediant (the lowered submediant in
  minor).
- **Plagal and evaded** cadences are recognized but, by rule, carried at **lower confidence**: the plagal as a possible
  post-cadential tonic prolongation rather than a structural close, the evaded as an arrival abandoned and re-launched.
- **Chorale phrase gate.** A cadence candidate is admitted only at a **phrase boundary** — in the chorale corpus the
  fermata is the reliable marker. This removes the mid-phrase passing motions that otherwise masquerade as cadences.

Each admitted cadence then casts a **weighted vote for the tonic** of its region (§5.3). The weight rises with the
strength of the evidence (the bass five-to-one, the leading-tone resolution, the dominant seventh) and with the
**salience** of the arrival (a strong metric position, a fermata, a section end, the final bar). The detector reads no
already-resolved key; the key is the thing the vote informs.

### 5.3 Tonicization versus modulation
The default is **tonicization**: the home key holds and a chord leaning toward a non-tonic degree is written as an
**applied chord** of that degree. The home key is changed to a **modulation** only when **both** hold:
- a **cadence in the candidate key confirms it** (an authentic or half cadence whose tonic is the candidate degree), and
- the music **persists** in the candidate key rather than immediately leaving it.

Persistence is expressed as a **change-cost (hysteresis)** on the local-key decision, not as a fixed number of beats:
the longer and more cadentially-confirmed the candidate area, the lower the cost of committing the key change; a brief
lean that lacks a confirming cadence pays a cost it cannot overcome and stays a tonicization. The boundary is a genuine
continuum; on fast-harmonic-rhythm chorales a defensible tonicization-versus-short-modulation disagreement is **not**
counted as an error. This is also the layer at which the **notated-spelling key signal** is consumed: spelling that
indicates a key change is admitted here, where function gates it, rather than in the key layer where (as measured) it
helps modulation regions but harms stable ones.

### 5.4 The cadence-confirmed modulation recompute (an instance of the §8 general mechanism)
This is the first concrete instance of the confidence-weighted forward override (§8, case 4): a cadence is later evidence
that contradicts a *confident* earlier key inference (the key layer chose its key before any cadence was known), and when
the cadence evidence is decisive it overturns the key. When §5.3 confirms a **modulation**, the layer commits the new
local key for the region and triggers a **bounded re-run** of the dependent reading over **that region only**, with the
new key: the chords of the region are re-read in the new key (their degrees change), and any uncertain slices in the
region are re-resolved against it. The recompute is **localized** (the affected region, not the piece), **forward** (it
re-runs the lower reading with a decided fact; it sends no request upstream), and **convergence-bounded** (a key change
decided once; the recompute does not re-open the key decision that triggered it). The threshold that decides "decisive"
is the cadence-strength-versus-key-confidence bar of §8 (its constant is precision-phase). The rule that prevents
recursion is in §8.

### 5.5 Resolving the carried uncertain readings
For each slice Layer 4 abstained on, the layer selects among the **carried readings** by the **named ambiguity kind**:

- **Transition** (a thin slice heading into a different next chord): decide, by the **progression**, whether the slice's
  notes belong to the prevailing harmony (a passing/neighbour figure within it) or to the arriving function — and select
  the reading consistent with that continuation.
- **Share-tone** (two readings explaining the same pitch classes — for instance a minor triad with an added sixth versus
  a half-diminished seventh a third below): select the reading that **participates in a real progression** toward the
  established next function (the cadential/voice-leading context decides what the lower layers could not).
- **Relative pair** (two roots a third apart, major versus minor — the relative reading): this is a **key/tonic**
  question; resolve it by the **cadence tonic-vote** (§5.2) and the same-collection tonal-centre evidence.
- **Close** (a general low-margin tie between otherwise-unrelated readings): break it by **functional and cadential
  plausibility**, with the soft bass-scale-degree prior (§5.7) as a tie-breaker.
- **Insufficient** (a genuinely too-thin slice): select from the carried readings on the progression where one is clearly
  favoured; where none is, **carry the uncertainty honestly** to display rather than guess.

Where the function evidence does not decide a case either, the layer does not invent a decision: it records the residual
as an honest open mark (carried to display), consistent with the principle that an unverifiable judgment is not made.

### 5.6 Relational labels (each on its defining trigger; spelling-aware where needed)
- **Applied/secondary chord** (a dominant or leading-tone chord of a non-tonic degree): triggered by a **raised secondary
  leading tone** manufacturing dominant function toward that degree; written as the applied chord of the degree, relative
  to the **local** key. (In the major mode the secondary leading tone of the dominant is the diatonic seventh degree, not
  a raised one — the alteration is in the spelling, the degree is unaltered; the rule reads the spelling, not a presumed
  accidental.)
- **Neapolitan**: a major triad on the **lowered second degree**, conventionally in first inversion; a chromatic
  pre-dominant, written as the lowered-second-degree chord (the local key is unchanged).
- **Augmented sixth** (Italian, French, German): triggered by the **augmented sixth between the lowered sixth and raised
  fourth degrees**, with the added degree selecting the type (Italian adds the tonic, French the second degree, German
  the lowered third). The German form is **pitch-class-identical to a dominant seventh** and is separated from it **only
  by notated spelling and resolution** — the one place the layer must read spelling to choose the label.
- **Modal mixture**: a borrowed lowered or raised degree that changes the chord's quality but **not** the key; written
  with the altered-degree prefix, no key change.

### 5.7 The soft bass-scale-degree prior
The bass scale-degree carries a weak functional bias (degrees five and seven lean dominant; degrees four and two lean
pre-dominant; degrees one and three lean tonic), after the Rule of the Octave and functional-bass tradition. It is used
**only** as a soft prior and tie-breaker in §5.2 and §5.5, **never as a gate**: it is many-to-one, direction-dependent,
and overridden by the sequence, the cadence, and any applied-chord context.

## 6. Runtime view (scenarios)
- **A perfect authentic cadence confirming the home key.** Pre-dominant, then root-position dominant with its seventh,
  then root-position tonic at a fermata, soprano on the tonic; the pair passes §5.2; a strong tonic vote confirms the key
  and the final Roman numerals read in it.
- **A tonicization that stays home.** A dominant-of-the-dominant leans toward the dominant degree but no cadence confirms
  that degree as a key and the lean does not persist; §5.3 keeps the home key and writes the chord as an applied chord.
- **A modulation.** The same lean is followed by an authentic cadence in the new key and the music persists; §5.3 commits
  the key change and §5.4 re-reads the region's chords in the new key.
- **Resolving a share-tone abstention.** Layer 4 carried both the added-sixth and the half-diminished readings and
  abstained; the established progression toward the next function selects the reading that participates in it (§5.5).
- **Resolving a relative-pair abstention.** Two roots a third apart, major versus minor; the cadence tonic-vote decides
  which is the centre (§5.5), and the slice takes the consistent reading.
- **Overriding a fine-grain wrong commit.** A transient sub-slice that the note-layer committed to a pitch-class-decidable
  but contextually-wrong root is overridden when the surrounding cadential/functional context contradicts it (the
  class-(b) override duty, §10), in concert with section grouping.

## 7. Data design
Per analysis unit the layer carries: the **Roman numeral** (degree with any alteration, quality, inversion, and the
relational label); a **function confidence**; and, where a slice was uncertain and remains so, an **open mark** naming
what is unresolved (carried to display, not a guess). Per region it carries the **local key** (possibly changed by a
confirmed modulation) and the **cadence markers** (type, location, salience). The structure is additive over the Layer-4
result: it annotates and resolves; it does not replace the chord identity Layer 4 committed. The contract to the layer
above (grouping/display) is the Roman numeral plus the cadence and key markers plus any honest residual mark.

## 8. Crosscutting concepts
- **The confidence-weighted forward override (the general arbitration mechanism).** Every layer's inference carries a
  **calibrated confidence**, and every later layer runs its full analysis over the whole stream — bringing its
  independent evidence to bear on *every* earlier inference, confident or not. How a given earlier inference and the later
  evidence are reconciled follows one four-case model:
  1. **Later evidence agrees with a confident earlier inference → reinforce** (the agreement raises the joint
     confidence; e.g. a cadence confirming the already-chosen key).
  2. **Earlier layer was uncertain and said so → select** among the readings it carried forward (the menu resolution,
     §5.5).
  3. **Earlier layer was uncertain and the later evidence still cannot decide → carry** the residual honestly to display.
  4. **Later evidence contradicts a *confident* earlier inference → override iff the contradiction is decisive.** The
     later evidence overturns the confident commit **only when its strength crosses a threshold that scales with the
     earlier layer's confidence** — a well-founded confident commit demands decisively stronger contradicting evidence
     than a borderline one. This is what makes confidence do real work: it sets the *bar to overturn*, not an absolute
     veto.
  Cases 2 and 4, when they fire, are realized by **one mechanism**: a **localized, forward, convergence-bounded
  recompute** — the dependent reading is re-run over the **affected region only**, with the corrected fact, and the
  overturned decision is **closed for that pass** (the recompute does not re-open the very decision that triggered it, so
  it cannot recurse). It is never a backward request and never a loop; it is a forward consumer acting on a decided fact.
  The two channels this layer needs — the fine-grain chord override (§5.5/§10) and the cadence-confirmed modulation
  recompute (§5.4) — are **instances** of this single mechanism, not one-offs; further channels (future layers) are added
  as further instances. *Rationale (user, 2026-06-26): a confidently-wrong commit must be recoverable by later evidence
  rather than locked in — this gives the precision phase calibrated, tunable levers (the per-channel thresholds) instead
  of a hard gate.* The thresholds themselves are precision-phase calibration (the firewall); this document fixes the
  mechanism and its direction, not the constants. **What this is NOT:** a backward re-derivation or a full joint
  cross-layer search — that was measured inert (the gain is soft-evidence quality, carried forward), so the architecture
  spends its effort on good forward evidence (calibrated confidence + ranked alternatives), not on cycling.
- **Spelling is read only where the distinction is a spelling distinction** (§5.6 German sixth; the applied secondary
  leading tone). Reading spelling everywhere would re-introduce a second spelling interpreter; the layer reads through the
  one shared interpreter, and only for the labels that require it.
- **Uncertainty is carried, not erased.** Where neither the notes, the key, nor the function decide a case, the honest
  residual is preserved to display. The layer resolves what its evidence resolves and marks the rest.
- **The firewall.** Mechanisms here are specified by rule and direction; their numeric calibration is the later precision
  phase.

## 9. Architecture decisions (with the alternatives weighed)
- **D1 — Output the Roman numeral; the three-role summary is a derived read-out (decided, user, 2026-06-26).** The Roman
  numeral is the complete, precise analysis and is what the reference corpora evaluate; the three-role summary
  (tonic/subdominant/dominant) is deterministically derivable from it and therefore lossy to store as a primary output.
  *Rejected:* a first-class three-role analysis — it would have to resolve the few context-dependent role cases, which no
  reference data can verify, violating the build-only-what-we-can-verify discipline. The read-out, if built for
  accessibility, defaults those cases to their tonic-side bucket. (Full reasoning: methods catalog §1.)
- **D2 — Cadence detection is key-agnostic and votes for the key; it does not read a resolved key.** *Rejected:* the prior
  key-dependent detector, which is circular and conflates the perfect with the imperfect cadence; and the single-chord
  interval test, which false-positives on tonic-to-subdominant and tonic-to-dominant because it tests leading-tone
  presence (the major third of any major triad) rather than leading-tone resolution. The event-pair feature test with the
  phrase gate is the corrected design.
- **D3 — Tonicization is the default; modulation requires cadence confirmation plus persistence, as a change-cost.**
  *Rejected:* a fixed-duration rule (no published threshold exists and the boundary is a continuum); and resolving the
  distinction in the key layer (it needs function). The hysteresis over the local-key decision matches the ground-truth
  convention.
- **D4 — The layer selects among Layer 4's carried readings; it never re-derives.** *Rejected:* re-scoring the slice from
  the notes (that is Layer 4's job and would duplicate it) — the structural content of the ratified O1 resolution: a case
  separable by a note cue is a lower-layer case, a case separable only by function is this layer's, leaving no third box.
- **D5 — The bass-scale-degree prior is soft, never a gate.** It is many-to-one and context-overridden; used as a
  tie-breaker only.
- **D6 — Placement and the misnamed predecessor.** The existing layer named for "function" performs chord-identity
  competition, not function; its functional labeling was always marked "planned." This layer is that planned work. Where
  it physically lives, and the renaming of the misnamed predecessor, is a structural step coordinated with the engagement
  (§11, §15), not a behavioural change.
- **D7 — A confident earlier inference can be overturned by decisive later evidence, via one general
  confidence-weighted forward-recompute mechanism (decided, user, 2026-06-26; see §8).** Every later layer brings its
  independent evidence to bear on every earlier inference; agreement reinforces, and a *confident* commit is overturned
  only when the contradicting evidence crosses a threshold scaled to the earlier layer's confidence — firing a localized,
  forward, convergence-bounded recompute. The two channels this layer needs (the modulation recompute §5.4 and the
  fine-grain chord override §5.5/§10) are **instances** of this one mechanism. *Rejected:* (a) treating each override as a
  bespoke one-off (it hides that they are the same mechanism and makes generalizing a rewrite); (b) a hard
  confidence-gate that locks confident commits permanently (a confidently-wrong commit must stay recoverable — this is
  what gives the precision phase tunable per-channel thresholds); (c) a backward re-derivation or full joint cross-layer
  search (measured inert — the gain is soft-evidence quality carried forward, not cycling). The mechanism and its
  direction are fixed here; the thresholds are precision-phase. **This decision is architecture-wide** (it generalizes the
  forward-only control-flow contract for all layers, not just this one) — to be promoted into the target-architecture
  doc; see §15-1.

## 10. Quality & testing
- **The metric is combined Roman-numeral accuracy and correct resolution**, judged against the reference corpora, plus
  the **correct-abstention** principle the lower layers established (resolving what is resolvable and honestly marking the
  rest beats guessing). Coverage is not the goal; coverage-matched accuracy and correct residual-marking are.
- **Cadence detection is measured by precision and recall per type**, with the standing caveat — established across the
  literature — that the **half cadence is the weakest** and is held to a correspondingly modest bar.
- **The class-(b) override duty:** the fine-grain wrong commits projected at engagement must be driven to zero (by this
  layer together with section grouping) before any production switch; this is the engagement hard-stop.
- **Tests are oracle-asserted** against known theory (a perfect versus imperfect cadence by inversion and soprano; a
  German sixth versus a dominant seventh by spelling; an applied chord versus a confirmed modulation by cadence) — not
  echoes of the analyzer's own output.
- **The corpus gate** (the two-tier root-error gate) governs as for the lower layers; a function change that moves a
  pitch-class-decidable root the wrong way is the hard-stop class.

## 11. Risks & technical debt
- **The half cadence is hard** (no tonic arrival to anchor on; phrase-boundary-dependent) — accept lower confidence.
- **The tonicization-versus-modulation boundary is genuinely fuzzy** on fast chorales — defensible disagreements are
  non-errors, not bugs to chase.
- **The German-sixth/dominant-seventh and applied-leading-tone labels depend on spelling** — they inherit the spelling
  layer's correctness; where spelling is absent or contradicted the label is held uncertain.
- **Two tonicization paths exist today** (a dormant labeler and the inline formatter) — the layer must own one and retire
  the duplicate; until then they are migration debt.
- **The predecessor layer is misnamed** — a naming/structural correction owed, coordinated with engagement.
- **The forward-recompute bound** must be held exactly (region-local, key-closed) or it risks becoming a back-edge.

## 12. Glossary
- **Roman numeral** — the chord named by its scale-degree within the key, with quality, inversion, chromatic alteration,
  and relational label (applied, Neapolitan, augmented sixth, mixture).
- **Cadence** — a point of harmonic closure; authentic (dominant to tonic), half (ending on the dominant), deceptive,
  plagal, evaded; the authentic split into perfect and imperfect by inversion and soprano.
- **Tonicization** — a brief lean toward a non-tonic degree without leaving the key (written as an applied chord).
- **Modulation** — a change of the prevailing key, confirmed by a cadence in the new key and by persistence.
- **Applied (secondary) chord** — a dominant or leading-tone chord of a degree other than the tonic.
- **Cadential six-four** — a second-inversion tonic spelling functioning as the dominant's accented suspension, not a
  tonic arrival.
- **The three-role summary** — the coarse tonic/subdominant/dominant classification, derivable from the Roman numeral; a
  read-out, not a stored output.

## 13. Background: what this layer replaces, and the as-built mapping (not needed to understand the layer)
The layer named for "function" in the current code is the **chord-identity competition pipeline** (a vertical scoring
oracle and winner selection); its functional labeling and cadence detection were always the **planned** stage on top of
its winner, never built. Two cadence detectors exist: a production one that is **key-dependent and circular** and
conflates the perfect with the imperfect cadence, and a dormant **key-agnostic** one whose leading-tone test
**false-positives on tonic-to-subdominant and tonic-to-dominant**. Tonicization is labelled twice — by a dormant applied-
chord labeler (with a chromatic-leading-tone guard worth keeping) and by an inline path in the Roman-numeral formatter.
The Roman-numeral formatter already emits the diatonic numeral, chromatic numerals, augmented-sixth labels, and inline
applied-chord labels. The phrase-boundary and chromatic-leading-tone markers already exist as primitives. This layer
unifies, corrects, and completes that scattered, partly-dormant machinery into the single function layer specified above;
the concrete reuse-versus-build map is in the methods catalog §7.

## 14. Related work & external sources (what we borrowed, discarded, and why)
**Borrowed:** the Roman-numeral component representation and the relational-label vocabulary as the output, from the
standard symbolic-analysis corpora and tools (the published autonomous analyzers, the corpus annotation standards, and
the music21 analysis tools); the event-pair, feature-scored, phrase-gated cadence design and the cadence-confirms-key
direction, from the computational cadence-detection literature; the cadence-confirmation-plus-persistence criterion for
modulation, from functional-harmony theory and the corpus annotation conventions; the soft bass-scale-degree prior, from
the partimento Rule-of-the-Octave and functional-bass tradition. **Discarded:** a tonic/subdominant/dominant prediction
target (the literature outputs Roman numerals and treats the three roles as a derived view; the leading analyzer lists it
as unbuilt future work); a key-dependent or single-chord cadence test (circular / false-positive); a fixed-duration
modulation rule (no published threshold; the boundary is a continuum); joint one-step key-and-chord prediction (rejected
by the decomposition; the gated forward selection is the design); and prolongational/Schenkerian reduction (needs
grouping, metre, and whole-piece parsing, below human accuracy computationally — a later layer). Full citations: methods
catalog §Sources.

## 15. Open items & deferred refinements
1. **Promote the confidence-weighted forward-override mechanism (§8 / §9-D7) into the target-architecture doc.** It is
   architecture-wide — it generalizes the forward-only control-flow contract for *every* layer (any confident inference
   overturnable by decisive later evidence via a localized forward recompute), with the modulation recompute (§5.4) and
   the fine-grain override (§5.5/§10) as the function layer's two instances. The canonical control-flow contract should
   carry it so later layers inherit it by default rather than re-deriving it. *(Done — the architecture doc's control-flow
   contract now carries it. The earlier-layer override-readiness was verified at source and closed: chord layer already
   carries alternatives+confidence on confident commits; key layer's region forward-carry is the byte-identical close-out
   `cc_instruction_l3_keyalt_forwardcarry.md`; slicing layer not impacted. See completion-ledger reopen note.)*
2. **Override calibration facts the threshold design must account for (from the source check).** The chord layer's
   carried confidence is **vertical-fit only** (no progression signal — this layer supplies the functional context
   itself, so the threshold scales against vertical decisiveness, not total decisiveness); the carried `alternatives` are
   **capped (topK)** and **exclude spelling-pinned symmetric siblings** (so an override that wanted to revisit a
   spelling-resolved rotation must decide its interaction with the spelling-pin); and there is **no cross-slice
   neighbourhood confidence** — this layer derives neighbourhood decisiveness itself from adjacent slices' carried
   confidence/alternatives. None are earlier-layer defects; they are inputs the override design consumes.
3. **The exact forward-recompute contract** (§5.4) — the precise region bound, the convergence guarantee, and the
   confidence-versus-evidence threshold *shape* (not its constant) — to be pinned with the key layer before the modulation
   step is built. This is the single place the layer touches upstream; getting the bound exactly right is what keeps the
   general mechanism (§8) from becoming a back-edge.
   - **★ Pin the region key-alternatives reduction here — first task of this step, no later (standing obligation, user
     2026-06-26).** The key layer's region-level alternative-keys carry was shipped at a deliberate **byte-identical v1**
     (the representative slice's alternatives) *only because* the consumer was not yet designed. Designing this modulation
     step is the **earliest point we CAN** pin the reduction precisely (it is what the override selects among), so we
     **must** then — replace the v1 with the correct reduction, derived from this override's real selection needs, and
     update the key-layer carry + its lock-in test. Do not carry the v1 placeholder past this step. (Why deferred, not
     pinned up front: it would design the reduction against an unspecified consumer — see the completion-ledger reopen
     note and `cc_instruction_l3_keyalt_forwardcarry.md` §1.3.)
4. **Cadence as its own internal sub-unit** consumed by both the modulation arbiter and the resolver (likely, since it is
   shared evidence) — to confirm at build.
5. **The two-tonicization-path unification** and the **predecessor renaming/placement** — structural steps coordinated
   with the joint engagement, like the other migration debt.
6. **The interaction with section grouping** for the class-(b) override duty (§10) — to specify jointly.
7. **The three-role read-out** (§9-D1) — deferred until an accessibility/teaching display needs it.
8. **Pull the two project-memory backlog notes** on extended harmonic functions and cadence internationalization before
   the function vocabulary and any cadence-label localization are finalized.
9. **Prolongation/reduction** — explicitly a later layer, not this one.
