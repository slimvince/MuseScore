# Architectural Layer 5 — FUNCTION (Roman numeral, cadence, tonicization) — Architecture & Design

> **Status: SIGNED (user, 2026-06-26); amended post-sign-off 2026-06-26.** **Amendment (user-surfaced):** the
> perfect/imperfect cadence distinction (§5.2) no longer rests on the **top voice** — the highest sounding voice is not
> reliably the structural melody (orchestral doubling; barbershop lead below the top), so the call is made on the
> **bass-derived inversion** criterion and the top-voice arrival is only a soft optional nudge. Consequently the top-voice
> primitive is **demoted from a gating build prerequisite to an optional cue** (§15-0); the gating prerequisites are now
> the metric-weight contract and the phrase boundary. Reviewed in two passes before sign-off. Audited against the three design-doc standards
> (specify-by-rule, code-free body, standard vocabulary) + internal consistency (7 fixes + a tie-direction rule), then a
> **language-mechanical pass** (every predicate given a subject; every statement resolved under recursive why/how; every
> concept defined) closing **12 resolution gaps** — independently re-audited as **fully resolved, no fresh holes**. Record:
> `cowork_layer5_spec_review.md`. First spec of the function layer, grounded in `cowork_layer5_function_methods.md`
> (research-first synthesis: three internal source surveys + two primary-sourced external literature passes) and the
> ratified architecture (`cowork_target_architecture.md`, the L4 spec §15-O1). It is written to the design-doc standard:
> every decision path is specified by a **rule** (no preference-shaped holes), the **architecture body (§1–§12) is
> code-free** (mechanisms named by their role), and it uses only **standard music-theory vocabulary**. The as-built
> mapping lives in §13; the **background, related-work, and open-items sections (§13–§15) may name as-built identifiers
> and doc cross-references** where the build hand-off needs them. The body (§1–§12) reads the same whether or not anything
> is built. Nothing is built yet — the incremental build (investigate-each-step, as for L4) follows ratification.
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
3. **Resolution of the carried "uncertain" readings** — Layer 4 commits the chords it can decide
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
  carry. This is the structural content of resolving "uncertain" by selection rather than re-derivation.
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
**Consumes.** Each input is owned and defined by an earlier layer — this layer defines none of its own inputs. The ones
marked **[earlier-layer prerequisite]** are *not yet* defined in their owning spec and must be (in that spec, before this
layer builds — see §15-0); the rest are already defined where cited.
- From Layer 4, per slice (defined in the Layer-4 spec): the committed chord where Layer 4 committed; and where it
  abstained, the **carried readings** (the chosen reading, the best competing reading, and the ranked alternatives), the
  **named open question** (which axis is in dispute — root or quality — and the kind of ambiguity), and the **confidence**
  components.
- From Layer 3 (defined in the Layer-3 spec): the prevailing **local key and mode** over the region, carried with its own
  ranked alternatives and uncertainty (the override-readiness forward-carry).
- From Layer 1 (defined in the Layer-1 note-model spec): the per-note **notated spelling** (also the shared Layer-1.5
  spelling view), each note's **voice**, and the **bass** of each slice (the lowest sounding note).
- **[earlier-layer prerequisite] The metric weight of each slice.** The Layer-2 spec defers it ("derived on demand by the
  consuming layers"); it needs a defined owner and contract before this layer consumes it.
- **(Optional, NOT a prerequisite) The top voice — the highest sounding voice of a slice.** Used only as a *soft,
  optional* confidence nudge in the perfect/imperfect cadence distinction, and only in homophonic textures — the highest
  voice is **not** reliably the structural melody (§5.2), so the distinction rests on the bass-derived inversion criterion
  instead. A top-voice primitive is therefore optional, not a build gate (§15-0).
- **[earlier-layer prerequisite] The phrase boundary (the fermata-marked phrase end in chorales) and, with it, the phrase
  segmentation** that bounds a region (§5.0). No earlier spec detects or defines this, yet the cadence phrase-gate and the
  salience cues (§5.2) rest on it — the most load-bearing of the three prerequisites. (A "section end" is a phrase boundary
  that **also coincides with a structural score boundary** — a double bar, a repeat mark, or the end of the piece — used
  only as the section-end salience cue in §5.2.)

**Produces.** The output conforms to a **named standard at full completeness — the DCML harmony-annotation standard (and
its RomanText interchange form), the convention our ground-truth corpora use — with no simplification.** "No
simplification" is a rule, not an aspiration: wherever the standard defines a fuller label, the layer emits the fuller
label and never a reduced stand-in. Where the standard admits variants (e.g. the Neapolitan as `bII6`; the cadential
six-four), the layer follows the **DCML convention** so its output is directly comparable to the ground truth.
- The **Roman numeral** per analysis unit, carrying **every** component the standard defines, each at full specificity:
  - the **scale-degree** with case marking quality (upper/lower), and the **chromatic alteration** as the exact
    accidental prefix where the degree is non-diatonic (`bII`, `#iv`, `bVI`, …);
  - the **precise chord quality** including the seventh type (major, minor, dominant, half-diminished, fully-diminished);
  - the **exact inversion** as the figured-bass figure (`6`, `64`; `7`, `65`, `43`, `42`) — never a bare numeral where
    an inversion figure is due;
  - the **relational label** at full specificity: an **applied/secondary** chord with its **explicit target degree**
    (`V/V`, `V7/IV`, `viio7/ii`, …, relative to the local key); the **augmented sixth with its nationality** (`It`, `Fr`,
    `Ger`) and inversion figure, never a generic `+6`; the **Neapolitan** (`bII6`); and **modal mixture** as the precise
    borrowed/altered degree.
  The completeness bar is the §10 metric's target: a label is correct only when **every** component matches the standard
  ground truth, so emitting a simplified label is by construction a miss.
- **Cadence markers** at each point of closure: the cadence **type from the full typology** (perfect authentic, imperfect
  authentic, half — including Phrygian — deceptive, plagal, evaded; §5.2), its **location**, and its **confidence** —
  never a reduced set (not merely "authentic versus half").
- The **tonicization-versus-modulation** decision, expressed as the standard distinguishes them: a tonicization stays in
  the prevailing key and is written as an applied chord (`/x`); a confirmed modulation changes the local key.
- The **resolved reading** for each formerly-uncertain slice (a selection among the carried readings, with a function-
  level confidence and, where it remains genuinely undecidable, an honest **open mark** (§7) carried to display).

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

### 5.0 Shared definitions (the terms the rules below stand on)
These five concepts are used throughout §5 and are defined here once so no rule rests on an undefined word.

- **Region.** The bounded span the pipeline already segments — a maximal run of slices between two adjacent **phrase
  boundaries** (§3: in the chorale corpus, fermata-marked), carrying one prevailing key. It is the unit a cadence votes
  for (§5.2), the unit a confirmed modulation re-reads (§5.4), and the bound on a slice's resolution look-ahead (§5.5). The
  *exact* recompute bound for §5.4 (whether it is the single region or the region plus its immediate neighbour) is the one
  refinement deferred to the build (§15-3); everywhere else "region" means the phrase-bounded span just defined.
- **Prevailing harmony (of a slice).** The committed chord (from Layer 4) of the nearest **metrically-strong** slice at or
  before the slice in question, within the same region — the harmony a passing/neighbour figure is heard against.
  ("Metrically strong" is realised **parameter-free** as a **local maximum of the metric weight** — no threshold — per the
  Step-1 build.)
- **The progression.** The ordered sequence of committed chord identities (and, once assigned, their Roman-numeral
  functions) across a region — the chord stream Layer 4 committed, read in order. "The next function" / "the established
  next function" is the function of the next committed (non-abstained) chord, or, where the next chord is itself open, the
  next **cadence-anchored** function (a chord whose function a cadence has fixed, §5.2).
- **A licensed (real) progression.** A **root motion** between two functions is **licensed** when it is one of the standard
  functional successions: a descending-fifth (dominant) motion, a descending-third or ascending-second functional step,
  the resolution of an applied or leading-tone chord to its tonicized target, or a cadential motion (§5.2). A reading
  "participates in a real progression" when its function forms a licensed motion **into** the established next function.
  (Because the test is on *root motion*, a **same-root quality resolution** — e.g. an augmented chord resolving to a chord
  on the same root — is **not** a progression and is outside this test; such voice-leading events are a chord-layer /
  embellishment matter, not function progression. Step-1 build decision.)
  This is a stated, enumerable test — not a preference. (The numeric preference *among* several licensed readings is a
  precision-phase weight; the licensing itself is the rule here.)
- **A resolution (as a detected event).** A **leading-tone resolution** is detected when the leading-tone pitch sounding
  in a voice of the approach chord moves to the tonic in **that same voice** at the arrival; a **tritone resolution** is
  detected when the dominant's tritone (the fourth and seventh degrees) contracts or expands by step to the tonic's third
  and root across the boundary. "Resolution" everywhere in §5 means such a detected voice-motion event — never the mere
  presence of the leading tone or tritone (the false-positive trap). The German augmented sixth versus the dominant
  seventh is separated by **which** resolution the notated spelling implies (the augmented sixth expands outward to the
  dominant; the seventh resolves down to the tonic).

### 5.1 Base Roman-numeral derivation
For each analysis unit with a committed root, quality, inversion, and a prevailing key: the **degree** is the root's
position relative to the tonic; where the root is diatonic the degree is the plain scale-degree, where it is chromatic
the degree is written with its alteration (a lowered or raised degree prefix) without changing the local key. The
**quality and inversion** come from the chord. This step is a deterministic reading; it introduces no judgment beyond the
key and chord it is given.

### 5.2 Cadence detection (key-agnostic, event-pair, feature-scored)
A cadence is tested on an **event pair** — the approach chord and the arrival chord — never on a single chord's interval
content. The rules:

- **Cadential six-four collapse first.** When the approach is a second-inversion tonic-spelled sonority (so identified
  from Layer 4's committed chord, not re-read from the notes) over a bass scale-degree five that proceeds to a
  root-position dominant over the same bass, it is the dominant's accented
  suspension, not a tonic arrival: collapse the pair into a single **dominant approach** so the cadential bass reads
  five-to-one. A second-inversion tonic spelling never registers as a tonic arrival.
- **Authentic cadence — the family gate** (corrected at the Step-2 build, 2026-06-26): the *sequence* (a pre-dominant,
  then a dominant, then the tonic arrival), **a dominant-function approach** (a chord on scale-degree five, **or** a
  leading-tone chord — a seventh-degree diminished triad/seventh — standing in for it) **resolving to the tonic**, and the
  **leading tone resolves to the tonic** across the boundary (the resolution, present as an **event** — not merely the
  leading tone being sounded). **The dominant seventh / tritone resolution is a vote *strengthener*, not a family gate** —
  a *plain* triad V→I with the leading-tone resolution **is** an authentic cadence (Caplin's V(7)→I, the seventh
  parenthetical; and the common chorale phrase-end), the seventh merely raising its vote weight (§5.2 vote).
  - **★ The key-agnostic limit (Step-2 build finding, 2026-06-26 — a corrected premise).** A *plain* triad V→I and a plain
    I→IV are **exact transpositions**: a key-agnostic event-pair test, hypothesising the arrival is the tonic, reads both
    as "V→I" (for a I→IV in C it makes E the "leading tone" of F and E→F a resolution). So the leading-tone-resolution
    event **does NOT by itself discriminate authentic from tonic-to-subdominant** — that needs the key, which this detector
    is *informing*. By design this is **resolved downstream, not here:** (i) the **seventh/tritone**, when present, is a
    position-independent dominant signature (admits robustly); (ii) the **phrase gate** removes the *common* false positive
    (a passing I→IV is mid-phrase, not at a phrase boundary); (iii) the **residual** — a plain I→IV that happens to fall at
    a phrase boundary (rare) — casts only a **weak soft tonic-vote the key layer's aggregation absorbs** against the
    home-signature pull and the genuine cadences. The cadence detector casts soft evidence; the authentic-vs-passing
    disambiguation is a **key-layer** judgement (the cadence-anchored-key model). The **bass scale-degree five-to-one is the
  *perfect* criterion, not the family gate** (an inverted authentic cadence does not have it). Within the family the
  perfect/imperfect distinction is the **bass-derived inversion criterion**; the **outermost-voice criterion is not a hard
  test** (the §5.2 amendment, note below):
  - **Perfect** when both the dominant and the tonic are in **root position** (the bass — reliably the lowest sounding
    voice — carries the cadential five-to-one) **and** no other perfect-condition fails.
  - **Imperfect** is the **complement**: any authentic dominant-to-tonic motion (leading tone resolving) that is **not**
    perfect — chiefly an **inverted** dominant or tonic (so the bass is not five-to-one), a non-tonic outer-voice arrival,
    or the leading-tone-chord substitution. The branch is **total**: every admitted authentic motion is perfect or
    imperfect, with no third outcome.
  - **The melodic-arrival criterion is a soft, optional nudge, never a hard test.** Classical theory's further requirement
    — the *melody* arriving on the tonic — needs identifying the structural melodic line, and **the highest sounding voice
    is not reliably that line** (in much orchestral writing the melody sits in an inner or doubled register; in
    close-harmony idioms such as barbershop the lead is *below* the top voice). So the spec does **not** rest the
    perfect/imperfect call on the top voice. Where a trustworthy melodic top line exists (a homophonic texture), a top
    voice arriving on the tonic may *raise* the confidence of a "perfect" reading, and one not on the tonic may *lower*
    it — but it never forces the call, and the distinction is made on inversion. The tool does **not** attempt melody
    identification (a hard, partly-perceptual problem deliberately out of scope).
- **Half cadence** is a phrase ending **on the dominant** that does not proceed to the tonic (the dominant is the
  phrase-final arrival — nothing follows it within the phrase). The dominant is a **root-position triad in the strong
  case; an inverted or seventh dominant is admitted but at lower weight** (a seventh implies onward motion and weakens the
  reading — it is down-weighted, not excluded). The **Phrygian** half cadence (minor
  mode) is the special case of a first-inversion pre-dominant moving to the dominant with the **bass descending a
  semitone** into it. Half-cadence identity depends on the phrase boundary, and is the weakest reading — held at lower
  confidence by rule.
- **Deceptive cadence** is a **dominant *set up to cadence*** — a phrase-boundary dominant carrying the authentic
  approach features (the pre-dominant→dominant sequence with the leading tone present) — that arrives instead on the
  submediant (the lowered submediant in minor). ("Set up to cadence" carries this same meaning wherever it is used below.)
- **Plagal cadence** — admitted when a **subdominant-family chord** (a pre-dominant: the fourth-degree triad or seventh,
  the second-degree triad or seventh, or the lowered-sixth submediant) **moves to the tonic at a phrase boundary with no
  intervening dominant**; carried at **lower confidence** by rule (a possible post-cadential tonic prolongation rather
  than a structural close).
- **Evaded cadence** — admitted when a **dominant set up to cadence has its expected tonic arrival replaced** by a
  non-tonic continuation or a re-launched phrase (distinct from the deceptive cadence, where the dominant *resolves* to
  the submediant — here the arrival itself is abandoned); carried at **lower confidence** by rule.
- **Chorale phrase gate.** A cadence candidate is admitted only at a **phrase boundary** — in the chorale corpus the
  fermata is the reliable marker. This removes the mid-phrase passing motions that otherwise masquerade as cadences.

Each admitted cadence then casts a **weighted vote for the tonic** of its region (§5.0, §5.3). The weight is a
**monotone-increasing combination — a weighted sum, its weights precision-phase constants —** of the **evidence-strength
cues** (the bass five-to-one, the leading-tone resolution, the dominant seventh) and the **salience cues** (a strong
metric position — the metric weight of §3; a fermata; a section end; the final bar), minus the per-type lower-confidence
discount for half/plagal/evaded cadences. The **direction is fixed here** (more evidence and more salience never lower
the weight; only the relative weights are deferred). The detector reads no already-resolved key; the key is the thing
the vote informs.

### 5.3 Tonicization versus modulation
The default is **tonicization**: the home key holds and a chord leaning toward a non-tonic degree is written as an
**applied chord** of that degree. The home key is changed to a **modulation** only when **both** hold:
- a **cadence in the candidate key confirms it** (an authentic or half cadence whose tonic is the candidate degree), and
- the music **persists** in the candidate key rather than immediately leaving it.

The two conditions play different roles. **Condition (a), cadence confirmation, is a necessary gate**: with no cadence in
the candidate key, the lean stays a tonicization no matter how long it lasts (this is what "a brief lean that lacks a
confirming cadence cannot become a modulation" means — it is the gate failing, not a cost being outweighed). **Condition
(b), persistence, applies only among cadence-confirmed candidates**, and is expressed as a **change-cost (hysteresis)** on
the local-key decision: the cost of committing the key change **falls as the cadence-confirmed candidate area grows in
duration and in accumulated cadential weight** (the §5.2 vote weights of the cadences inside it) — measured in those two
quantities, never a fixed beat count. **At the exact break-even** (the change-cost neither clearly met nor clearly unmet)
the rule **defaults to tonicization** — the home key holds — consistent with tonicization being the default; only the
*magnitude* of the cost is a precision-phase constant, the tie-direction is fixed here. The boundary is a genuine
continuum; a tonicization-versus-short-modulation **disagreement that falls within this break-even band** is, as an
**evaluation policy** (not a machine rule), not counted against the analyzer — there is no single correct answer in the
band. This is also the layer at which the **notated-spelling key signal** is consumed: spelling **indicates a key change**
when the slice's notated accidentals are **sustained and consistent with the candidate key's diatonic set (its key
signature)** rather than passing chromatic inflections of the home key — and even then it is admitted only **as one input
to condition (a)/(b) above, gated by function**, rather than in the key layer where (as measured) the same signal helps
modulation regions but harms stable ones.

*(Step-4 build, 2026-06-26 — reuse + one Step-M check.) §5.3/§5.4 are built by **reusing** the dormant
`localmodulationdetector` (the established + cadence-confirmed span substrate) and Step-3's `forwardoverride` (the §8
recompute), not a re-implementation. Two realisations on record: the **persistence hysteresis is layered on the
detector's committed spans**, keeping the detector's `kEstablishmentMinChords` establishment floor as a **candidate
pre-filter** — so the §5.3 "not a fixed count" rule is honoured at the **decision** level (the hysteresis decides among
candidates), with the fixed floor a conservative pre-filter only; **Step-M check:** measure whether that floor ever
rejects a real short modulation the hysteresis would have admitted. And the **§8 contradiction strength for the
modulation override is the cadential weight** (cadence-vs-key-confidence), with §5.3 owning the persistence/duration —
the clean split.*

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
For each slice Layer 4 abstained on, the layer selects among the **carried readings** by the **named ambiguity kind**
(the kinds — transition, share-tone, relative pair, close, insufficient, **symmetric-rotation** — are exactly the six
ambiguity kinds Layer 4 carries forward; this layer adds no new kind):

- **Transition** (a thin slice heading into a different next chord): decide, by **the progression (§5.0)**, whether the
  slice's notes reduce to a passing/neighbour figure within the **prevailing harmony (§5.0)** or belong to the arriving
  function — and select the reading consistent with that continuation (the one forming a licensed progression, §5.0).
  (The "reduces to a passing/neighbour figure" judgment is made by **the progression test** — whether the slice forms a
  licensed function of its own — **not** by a voice-leading/melodic-reduction test, which this layer does not build, §11;
  where the progression cannot decide, the case is an open mark.)
- **Share-tone** (two readings explaining the same pitch classes — for instance a minor triad with an added sixth versus
  a half-diminished seventh a third below): select the reading that **participates in a licensed progression (§5.0)**
  into the **established next function (§5.0)** — the progression-and-cadence context decides what the note evidence alone
  could not. (No voice-leading test is invoked; this layer defines none — see §11.)
- **Relative pair** (two roots a third apart, major versus minor — the relative reading): this is a **key/tonic**
  question; resolve it by the **cadence tonic-vote** (§5.2) and the **same-collection tonal-centre cues** — the cues that
  separate two keys sharing one scale collection (a relative major/minor pair): which of the two candidate tonics
  **receives the cadential arrival**, **carries the raised leading tone** (the accidental that marks the minor tonic), and
  **sits at the phrase-final or sectional point of emphasis**.
- **Close** (a general low-margin tie between otherwise-unrelated readings): break it by **functional plausibility** —
  a score over fixed features: whether each reading's function forms a licensed progression (§5.0) **out of** the
  prevailing harmony and **into** the established next function, plus its cadential fit — with the soft bass-scale-degree
  prior (§5.7) as the tie-breaker. The features are fixed here; their combination weights and the deciding margin are
  precision-phase constants.
- **Insufficient** (a genuinely too-thin slice): break it by the **same functional-plausibility score** as *close* above;
  where even that does not separate the readings, **carry the uncertainty honestly** to display rather than guess.
- **Symmetric-rotation** (competing rotations of a symmetric sonority — a diminished-seventh or augmented chord whose
  spelling Layer 4's pin could not fix): select the rotation that **resolves as a licensed leading-tone or applied chord
  to its target** (the resolution context — §5.0 — names which root the symmetric sonority is functioning as), or that the
  cadence pins. Where no rotation forms such a resolution, the case is genuinely undecidable (the gate-policy class-(a):
  pitch-class-undecidable, and function finds no resolution either) → **carry the honest open mark** (§7); do not guess a
  rotation. *(This is rare in practice — the measured symmetric-rotation share reaching this layer is ≈0%, the dim7 churn
  having dissolved by abstention earlier; the rule exists for completeness.)*

Where the function evidence does not decide a case either, the layer does not invent a decision: it records the residual
as an honest open mark (carried to display), consistent with the principle that an unverifiable judgment is not made.

**The same selection machinery serves the override of a *confident* commit (the §8 case-4 channel).** When Layer 4
**confidently committed** a fine-grain reading that the established function and cadence contradict (the class-(b)
override duty, §10), the layer does not abstain-resolve it — it **overrides** it, but by the same constraint: it
**selects the corrected reading from the carried alternatives or the prevailing harmony (§5.0) of the adjacent committed
slices within the region** (the "neighbouring committed harmony"), never re-deriving, the override firing per the
confidence-weighted threshold of §8. So this section is the home of selection-among-carried-
readings for **both** the abstained slices (the §8 case-2 menu resolution) and the confident-commit override (case 4).
*(Step-3 build + Step-M check, 2026-06-26: the override is scoped to Layer-4 **`Commit`** decisions ("confidently
committed"). The §10 class-(b) duty was measured as **61 Commit / 25 Inherit**; whether the 25 **Inherit** class-(b) cases
are driven to zero by the Commit-override **plus cascade** (an Inherit that borrows a now-corrected commit), or whether
the override must **extend to Inherit**, is a **Step-M measurement** — not extended speculatively here. If Step M shows an
Inherit class-(b) residual, broaden the override to confidently-decided = {Commit, Inherit}.)*

### 5.6 Relational labels (each on its defining trigger; spelling-aware where needed)
The four labels can co-trigger on one altered chord, so they are tested in a fixed **precedence**, first match wins:
**augmented sixth → Neapolitan → applied/secondary → modal mixture**. The augmented sixth and the Neapolitan are the most
specific (a named chromatic-predominant shape); the applied label fires next (a chord manufacturing dominant function
toward a non-tonic degree); modal mixture is the **residual** — a borrowed degree that is none of the above. So "modal
mixture" is decided not by a positive test for "borrowed" but by being a quality-altering borrowed degree that did **not**
match any earlier label.
- **Applied/secondary chord** (a dominant or leading-tone chord of a non-tonic degree): triggered by **a dominant-function
  chord (a major triad / dominant seventh, or a leading-tone chord — a diminished triad or seventh) of a non-tonic diatonic
  degree that is *chromatic* relative to the home key** — its root a fifth above (or its leading tone a semitone below) the
  **target** degree it is written against, relative to the **local** key.
  - **The chromaticism test is general: the chord contains at least one tone foreign to the home-key collection.** This one
    test is the trigger's necessary condition *and* its false-positive guard; the specific identity of the foreign tone
    varies with the chord type and is **not** a closed enumeration. The named instances (non-exhaustive):
    - a **raised secondary leading tone** — the applied dominant whose target's leading tone is itself chromatic (`V/V`);
    - a **lowered seventh** of an otherwise-diatonic dominant — `V7/IV`, whose target IV has a *diatonic* leading tone (the
      third degree), so the chromatic tone is the ♭7̂, not a raised leading tone;
    - the **foreign tone of a secondary leading-tone chord** — `viio/IV`, `viio7/ii`, etc., whose diminished quality
      contributes the chromatic tone(s) even where the target's own leading tone is diatonic.
  - **The false-positive guard rejects only a genuinely diatonic chord (no foreign tone at all).** It must *not* be a
    raised-leading-tone-only guard: that form wrongly dropped both `V7/IV` (the ♭7̂ case — Step-5 build finding, 2026-06-26)
    and `viio/IV` (the secondary-diminished case — Step-5 follow-up ruling, 2026-06-29, A-D2). A chord fully diatonic to the
    home key is never applied (the natural-minor `bVII7→III`, all-diatonic, stays the diatonic numeral — it is **not**
    `V7/III`). (In the major mode the secondary leading tone of the *dominant* is the diatonic seventh degree, not a raised
    one — the rule reads the spelling, not a presumed accidental.)
  - **The pitch-class-identical major-tonic / `V/iv` case is a function-level decision, NOT a guard matter (deferred to
    §5.3–§5.5).** `V/iv` is rooted on the **home tonic** (the dominant of the subdominant is the tonic itself, tonic+5+7),
    so it is **pitch-class-identical to the major tonic** — `I`, a Picardy- or mixture-coloured tonic in a minor key, whose
    raised third is the chromatic leading tone of `iv`. The foreign-tone test therefore **cannot** separate them (both
    carry that raised third), and a *root-equals-tonic* test would wrongly suppress the **genuine** `V/IV`/`V/iv`
    tonicizations the ground truth labels. The correct reading depends on whether the subdominant is genuinely
    **tonicized** (a cadence or prolongation in it) versus merely the next diatonic chord — the §5.3/§5.4 tonicization-vs-
    tonic arbitration plus the §5.5 resolver. This is an **inference-layer** resolution, deferred with those layers; the
    structural applied trigger emits the applied reading for a tonic-rooted dominant of a diatonic degree, and §5.3–§5.5
    correct it in context. (Step-M finding, 2026-06-29: the reused `tonicizationlabeler` emits `V/iv` for the major tonic
    before `iv` in 62/29/56 units — a known over-trigger whose resolution is the function context, not the guard. An
    earlier framing of this as a "fully-diatonic guard gap" was a **corrected error** — the chord is not diatonic.)
    - **Source-level proof the guard cannot fix it (L5-close review D1, 2026-06-29).** A labeler-fired applied chord
      *always* carries a tone foreign to the home-key collection — over the **same** collection mask the foreign-tone
      guard uses — so hoisting the guard ahead of the labeler's early-return would reject **nothing**: the placement is
      provably **inert**. This converts the deferral from a judgment call into a proof — the correction is genuinely an
      inference (§5.3–§5.5) job, with no structural guard available.
    - **The over-trigger is a class, not just `V/iv` (L5-close review D2).** The same tonic-rooted-applied over-trigger
      appears at other targets (e.g. `V/VII` versus an inline `IV6` at `bwv272@9120`). All are the same inference class
      (a structural applied emission the function context must correct); enumerating the full class is a measurement-
      completeness task for the inference phase, not a new structural defect.
  - **Divergence from the legacy inline path is a Phase-5d / Step-M reconciliation, not a pre-judgment.** The production
    `formatRomanNumeral` inline path emits applied labels **without** this chromatic guard, so it over-emits on the
    genuinely-diatonic case (it would write `V7/III` for the diatonic `bVII7→III`). The unified dormant emitter is *more*
    correct there (the guard rejects it), so the two paths diverge on that case. Because the unified emitter is dormant (no
    production consumer), this is **byte-identical now**; whether each divergence is the right call is **measured at engage
    against the DCML ground truth** (Step M / Phase 5d), never decided by either path's say-so.
- **Neapolitan**: a major triad on the **lowered second degree**, conventionally in first inversion; a chromatic
  pre-dominant, written as the lowered-second-degree chord (the local key is unchanged).
- **Augmented sixth** (Italian, French, German): triggered by the **augmented sixth between the lowered sixth and raised
  fourth degrees**, with the added degree selecting the type (Italian adds the tonic, French the second degree, German
  the lowered third). The German form is **pitch-class-identical to a dominant seventh** and is separated from it **only
  by notated spelling and the resolution it implies (§5.0** — the augmented sixth expands outward to the dominant, the
  seventh resolves down to the tonic) — the one place the layer must read spelling to choose the label.
- **Modal mixture** (the residual label, per the precedence above): a borrowed lowered or raised degree that changes the
  chord's quality but **not** the key, and which matched none of the earlier labels; written with the altered-degree
  prefix, no key change.

### 5.7 The soft bass-scale-degree prior
The bass scale-degree carries a weak functional bias (degrees five and seven lean dominant; degrees four and two lean
pre-dominant; degrees one and three lean tonic), after the Rule of the Octave and functional-bass tradition. It is used
**only** as a soft prior and tie-breaker in §5.2 and §5.5, **never as a gate**: it is many-to-one, direction-dependent,
and overridden by the sequence, the cadence, and any applied-chord context.

## 6. Runtime view (scenarios)
- **A perfect authentic cadence confirming the home key.** Pre-dominant, then root-position dominant with its seventh,
  then root-position tonic at a fermata; both chords root position (the bass-derived inversion criterion) make it perfect;
  the pair passes §5.2; a strong tonic vote confirms the key and the final Roman numerals read in it.
- **A tonicization that stays home.** A dominant-of-the-dominant leans toward the dominant degree but no cadence confirms
  that degree as a key and the lean does not persist; §5.3 keeps the home key and writes the chord as an applied chord.
- **A modulation.** The same lean is followed by an authentic cadence in the new key and the music persists; §5.3 commits
  the key change and §5.4 re-reads the region's chords in the new key.
- **Resolving a share-tone abstention.** Layer 4 carried both the added-sixth and the half-diminished readings and
  abstained; the established progression toward the next function selects the reading that participates in it (§5.5).
- **Resolving a relative-pair abstention.** Two roots a third apart, major versus minor; the cadence tonic-vote decides
  which is the centre (§5.5), and the slice takes the consistent reading.
- **Overriding a fine-grain wrong commit.** A transient sub-slice that the note-layer committed to a pitch-class-decidable
  but contextually-wrong root is overridden **by this layer** when the surrounding cadential/functional context
  contradicts it (the class-(b) override duty, §10). Section grouping is **downstream** of this — once this layer has
  corrected the label, the grouping layer merges the now-consistent slices; grouping does **not** feed back into the
  override (consistent with §3's no-feedback rule). The exact division between this layer's override and the grouping
  layer's merge is the joint item §15-6.

## 7. Data design
Per analysis unit the layer carries: the **Roman numeral** (degree with any alteration, quality, inversion, and the
relational label); a **function confidence** — derived from the evidence that fixed the reading (the §5.2 cadence-vote
weight where a cadence anchored it, the §5.0 licensed-progression fit where the progression decided it, and the margin to
the next-best reading; the components are these, the combining weights are precision-phase); and, where a slice was
uncertain and remains so, an **open mark** naming what is unresolved (carried to display, not a guess). Per region it carries the **local key** (possibly changed by a
confirmed modulation) and the **cadence markers** (type, location, salience). The structure is additive over the Layer-4
result: it annotates and resolves; it does not replace the chord identity Layer 4 committed. The contract to the layer
above (grouping/display) is the Roman numeral plus the cadence and key markers plus any honest **open mark** (§7).

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
  overturned decision is **closed for that pass**: it is **marked final for the remainder of this analysis pass** (a
  one-pass closure flag on the decision), so the recompute it triggers — and any later override in the same pass — cannot
  re-target it. The recompute therefore terminates after one localized forward re-run; it is never a backward request and
  never a loop; it is a forward consumer acting on a decided fact.
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
  the notes (that is Layer 4's job and would duplicate it) — the structural content of the ratified resolution-by-
  selection: a case separable by a note cue is a lower-layer case, a case separable only by function is this layer's,
  leaving no third box.
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
- **Tests are oracle-asserted** against known theory (a perfect versus imperfect cadence by **inversion** — the top-voice
  criterion an optional soft cue, not the test; a
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
- **No voice-leading-based resolution is built.** The layer resolves share-tone and close ties by the progression and the
  cadence (§5.0/§5.5), not by a voice-leading test — the literature finds voice-leading schemata hard to detect from the
  surface, so building one is not justified here. A case only a voice-leading test could decide stays an open mark.
- **Two confidence scales coexist (L5-close review D3, low severity).** The §7 function confidence is an unbounded
  non-negative weighted sum; the §8 override threshold is `[0,1]`-clamped. They are **currently disjoint** (the §7 value
  is not fed to the §8 comparison), so this is not a bug — but their scale/naming should be reconciled at the precision
  phase before any channel couples them. Recorded, not changed (firewall).
- **The phrase-boundary primitive's non-chorale markers are unvalidated.** The graded model carries rest- and
  structural-boundary cues for general (non-chorale) textures, but the corpus is entirely fermata-marked chorales, so
  those markers have **no ground-truth oracle here** — a validation-coverage gap to close against a non-chorale corpus
  when one is available (cf. the verifiability-vs-correctness note: unvalidated ≠ wrong, but flagged).
- **Engagement framing.** References to an "engagement hard-stop" / "before any production switch" (§5/§10) remain true
  *conditionally* — engagement (Phase 5d) is **deferred indefinitely** (production out of scope; the posture is dormant
  build + ground-truth validation). The hard-stops apply *if* a switch is ever made; they are not pending work.

## 12. Glossary
- **Roman numeral** — the chord named by its scale-degree within the key, with quality, inversion, chromatic alteration,
  and relational label (applied, Neapolitan, augmented sixth, mixture).
- **Cadence** — a point of harmonic closure; authentic (dominant to tonic), half (ending on the dominant), deceptive,
  plagal, evaded; the authentic split into perfect and imperfect by **inversion** (the melodic/top-voice arrival a soft
  optional cue only, since the highest voice is not reliably the melody for general instrumentation).
- **Tonicization** — a brief lean toward a non-tonic degree without leaving the key (written as an applied chord).
- **Modulation** — a change of the prevailing key, confirmed by a cadence in the new key and by persistence.
- **Applied (secondary) chord** — a dominant or leading-tone chord of a degree other than the tonic.
- **Cadential six-four** — a second-inversion tonic spelling functioning as the dominant's accented suspension, not a
  tonic arrival.
- **The three-role summary** — the coarse tonic/subdominant/dominant classification, derivable from the Roman numeral; a
  read-out, not a stored output.
- **Class-(b) error** — a root or key error at a sonority whose root is *pitch-class-decidable* (a non-symmetric chord) —
  the meaningful-error class the corpus gate treats as a hard stop, as distinct from the symmetric-rotation churn
  (class-(a)). A project gate term (see the gate policy); used in §10 as this layer's override duty.
- **Ambiguity kind** — the named reason Layer 4 could not separate two readings (transition, share-tone, relative pair,
  close, insufficient), carried forward on an abstain; this layer resolves each by its §5.5 rule and adds no new kind.
- **Region** — the phrase-bounded span the pipeline segments (one prevailing key); the unit of the cadence vote, the
  modulation recompute, and the resolution look-ahead. Full definition: §5.0.
- **Prevailing harmony** — the committed chord of the nearest metrically-strong slice at or before a given slice, within
  its region; the harmony a passing/neighbour figure is heard against (§5.0).
- **The progression** — the ordered committed-chord stream across a region; a **licensed (real) progression** is a root
  motion forming a standard functional succession (§5.0); the **established next function** is the next committed or
  cadence-anchored function (§5.0).
- **Resolution (as an event)** — a detected voice-motion (leading tone → tonic; tritone contracting/expanding to the
  tonic third and root), not the mere presence of those tones (§5.0).
- **Salience** — the weight a cadence arrival carries by its metric position, fermata, section end, or final-bar status;
  combined into the tonic-vote weight as a weighted sum (§5.2).
- **Metric weight** — the metric-position strength of a slice (a downbeat is stronger than an offbeat), supplied by the
  pipeline (§3) and consumed as a salience cue.
- **Persistence / change-cost** — the hysteresis governing how long and how cadentially-weighted a cadence-confirmed
  candidate key area must be before the key is changed; measured in duration and accumulated cadential weight, not beats
  (§5.3).
- **Functional plausibility** — the score breaking a low-margin tie: whether a reading's function forms a licensed
  progression out of the prevailing harmony and into the established next function, plus cadential fit, with the
  bass-degree prior as tie-breaker (§5.5).
- **Function confidence** — the per-unit confidence this layer emits, from the cadence-vote weight / licensed-progression
  fit / margin that fixed the reading (§7).
- **Open mark** — the single carried marker (also the only name for it) naming what remains unresolved on a slice the
  evidence could not decide; emitted to display, never a guess (§7).

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
0. **★ Earlier-layer input prerequisites — close in the proper layer BEFORE this layer builds (§3).** The function layer
   defines none of its own inputs. **Two** it consumes gate the build: (i) the **metric weight** of a slice — **✅ RESOLVED
   2026-06-26**: the contract is documented in the Layer-2 slicing design (slice metric weight = beat-strength at the
   slice's start tick, owned by `scoreharvest/metricweights`, already consumed by Layer 4 — no code); (ii) the **phrase
   boundary + phrase segmentation** — **✅ BUILT (dormant) + Cowork-verified 2026-06-26**: the graded per-voice model lives
   in `engravingbridge/phraseboundaryview.{h,cpp}` (commits `0d10b37a87` de-dup + `5c5d992356` graded model), reachable
   only behind the default-off joint-key gate → **byte-identical on production** (verified at source), with the full marker
   set. **Both gating prerequisites are now closed → the function-layer build is unblocked.** The phrase boundary is
   defined **generally** (the tool analyzes any instrumentation): the fermata is only the *chorale-specific* marker, so
   the owning layer needs a phrase-boundary notion covering non-chorale textures too (rests, structural score boundaries —
   **but not cadential closure**, which is *this* layer's and would be circular). Each is a *proper-layer* amendment (like
   the override-readiness forward-carry), surfaced by this layer's design and closed in its own layer first.
   - **(Demoted — NOT a gating prerequisite) The top voice / highest sounding voice.** Earlier drafts made this a hard
     prerequisite for the perfect-vs-imperfect cadence distinction. It is demoted: **the highest sounding voice is not
     reliably the structural melody** (§5.2 — orchestral doubling, barbershop lead below the top), so the perfect/imperfect
     call is made on the **bass-derived inversion** criterion, and the top voice is at most a **soft, optional confidence
     nudge** in homophonic textures. So a top-voice primitive is *optional* (built only if that soft nudge is wanted), not a
     build gate, and may land alongside the function-layer build rather than before it. The tool does not attempt melody
     identification.
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
     2026-06-26). ✅ DONE (Step-4 build; lock-in test `regionanalysis_tests.cpp:484` — a confident region carries a
     non-empty ranked alternatives list of distinct keys, the reduction the modulation recompute selects among, not the
     v1 placeholder; L5-close-verified 2026-06-29).** The key layer's region-level alternative-keys carry was shipped at a deliberate **byte-identical v1**
     (the representative slice's alternatives) *only because* the consumer was not yet designed. Designing this modulation
     step is the **earliest point we CAN** pin the reduction precisely (it is what the override selects among), so we
     **must** then — replace the v1 with the correct reduction, derived from this override's real selection needs, and
     update the key-layer carry + its lock-in test. Do not carry the v1 placeholder past this step. (Why deferred, not
     pinned up front: it would design the reduction against an unspecified consumer — see the completion-ledger reopen
     note and `cc_instruction_l3_keyalt_forwardcarry.md` §1.3.)
   - **★ Also at this step: re-derive the carry in the J-key-iii re-key path.** The key layer's joint re-key pass
     (`jointKeyWiringEnabled()`, default-OFF today) overrides the chosen key **without** updating the forward-carry
     (`keyAlternatives`/`keyConfidence`) — inert now (gated off, no consumer), but the moment L5 consumes the carry that
     path must re-derive the carry alongside its override, or the carried menu goes stale against the overridden key.
     Bound to this pin so it cannot slip.
4. **Cadence as its own internal sub-unit** consumed by both the modulation arbiter and the resolver (likely, since it is
   shared evidence) — to confirm at build.
5. **The two-tonicization-path unification** and the **predecessor renaming/placement** — structural steps coordinated
   with the joint engagement, like the other migration debt.
6. **The interaction with section grouping** for the class-(b) override duty (§10) — to specify jointly.
7. **The three-role read-out** (§9-D1) — deferred until an accessibility/teaching display needs it.
8. **Pull the two project-memory backlog notes** on extended harmonic functions and cadence internationalization before
   the function vocabulary and any cadence-label localization are finalized.
9. **Prolongation/reduction** — explicitly a later layer, not this one.
