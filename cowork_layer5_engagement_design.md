# Layer-5 engagement design — Part 1: the CARRY and the SELECTION architecture

> **Status: DESIGN (CC, 2026-07-07). READ-ONLY architectural design pass — no `src/` change, no build, no
> corpus write, no constant fitted or tuned.** Engage arc #9, Stage 2 of the ratified plan
> (`cowork_engage_arc_plan.md`). This is **Part 1**: how engaged Layer 5 reads the decoder's governed carry and
> selects among the carried readings by joint consistency. The downstream owner-decisions (the quality-from-key
> owner FQ-2, pedal detection's home, the joint key-and-chord step O-18/C3, the F-B annotate mechanics) are
> **enumerated for follow-on passes (§4.3), NOT resolved here.** Provenance report:
> `cc_engage_l5_carry_selection_design_report.md`.
>
> **★ STRUCTURE ONLY — constants are precision-phase (R5). Not inference work (#8).** This designs the
> *architecture* of the selection (its evidence channels, how the concerns compose, the confidence contract it
> emits), grounded in published fact (#1) and the existing confidence contract. It fits no constant, tunes no
> threshold, and chases no case — declared comparability before tuned optimality (R5). Where a step needs a
> fitted value, the *shape* is declared and the constant marked precision-phase.
>
> **Why a NEW doc, not an edit of `cowork_layer5_function_design.md` (#6, one home per concern).** The existing
> L5 design doc is the **SIGNED spec of the dormant build** — what the §5.5 resolver, the §7 output assembly, and
> the §8 override machinery *are*. This document is a **distinct concern**: how that built machinery is **wired to
> the decoder's carry** at engagement and how the selection is **re-architected** to reason over the full
> distinct-root fan-out (§8 arc measurement) and to reconcile with the settled F-B annotate-not-override finding
> (`cowork_fb_redesign_design.md`). Folding engagement wiring into the signed spec would mix "what was built"
> with "how it engages" and muddy the signed provenance. This doc **references** the signed spec's sections
> (§5.5 / §7 / §8 / §5.0 / §15) rather than restating them.
>
> **Grounding tags.** `[code]` = read at the named source symbol; `[contract]` = `cowork_confidence_contract.md`;
> `[research]` = `cowork_functional_analysis_research_grounding.md`; `[data]` = a measured figure from a named
> report; `[flag]` = a gap the evidence does not close, called out rather than assumed.

---

## §1 — The dormant Layer 5 at the code: built vs owed (Task 1)

Layer 5 is **built and dormant** — no production consumer; exercised only by its unit tests; byte-identical on
production by construction (`functionresolver.h:77`, `functionoutput.h:66-68`) `[code]`. Engagement does **not**
design its machinery from scratch (#6) — it wires an existing pipeline. What follows is the inventory: what is
already built (§1.1–§1.3), and the delta engagement must add (§1.4).

### §1.1 The input contract already declared — `FunctionSlice` [code]
The resolver consumes a `std::vector<FunctionSlice>` (`functionresolver.h:121-148`). Each `FunctionSlice`
**unions** two views:
- the **§5.0 progression view** — `chord` (root+quality projection), `committed`, `metricWeight`, ticks;
- the **L4→L5 carried-reading contract** consumed **directly** from `chord/chordslicedecoder.h` (a declared
  build-detail decision, `functionresolver.h:58-69`) — `decision` (Commit/Inherit/Abstain), `openQuestion`
  (`OpenQuestionLabel`: readingA/readingB + `AmbiguityKind`), `alternatives[]` (ranked carried candidates),
  `confidence` (`SliceConfidence`, composite ∈ [0,1]), and `chosen` (the committed identity carried **verbatim**
  — root+quality+bass/inversion+extensions, the §5.5/§7 emit source).

So the *shape* of the carry Layer 5 reads is **already fixed in code** as the `FunctionSlice` fields. What is not
yet built is the **population** of those fields from the live decoder (today they are hand-injected in tests —
`functionresolver.h:120` "injected by hand"; `functionoutput.h:149` "the tests inject by hand"). That wiring is
the engagement gap (§1.4, §2).

### §1.2 The selection machinery already built — `resolveCarriedReadings` [code]
`resolveCarriedReadings` (`functionresolver.cpp:502-534`) runs one forward pass in two phases:

- **Phase 1 — base resolution.** For every `Abstain` slice, `resolveAbstained` (`:154-348`) **selects among the
  carried readings by the named `AmbiguityKind`**, never re-deriving from notes (D4):
  - *TransitionVsContinuation / ShareTone* — the licensed-progression test (§5.0 `isLicensedProgression`) into
    the established next function; then the neighbouring-harmony continuation; then the §5.7 bass-degree prior;
    then the honest open mark. The **both-licensed** case is telemetered (`bothLicensed`, `:223/:244`) and
    deliberately falls through to the structural tie-breaks (the §5.5 ruling; `[code]` matches the signed spec).
  - *RelativePair* — the cadence tonic-vote (§5.2) between the two candidate tonics (`:258-263`); then prior; then
    open.
  - *CloseReading / InsufficientEvidence* — the `plausibility()` fixed-feature score (licensed-out + licensed-in +
    cadential-fit, `:90-107`), deciding only past `decidingMargin`; then prior; then open.
  - *SymmetricRotation* — over the **full carried rotation pool** (`s.alternatives`, deduped by root, `:290-308`):
    the unique rotation resolving as an applied/leading-tone chord into the next, or the unique rotation a cadence
    pins; else the honest open mark (class-(a) undecidable). **This is the one arm that already reasons over the
    whole `alternatives[]` set, not just the readingA/readingB pair** — the structural precedent §3 builds on.
  - Every non-abstain slice `carryThrough` (`:357-370`) emits `s.chosen` **verbatim** (L4's commit stands).
- **Phase 2 — the fine-grain override (Frame F-B).** `attemptFineGrainOverride` (`:381-498`) — the §8 case-4
  channel. **This is the mechanism measured net-harmful** (`cowork_fb_redesign_design.md`: 1043 fires / 53
  corrections / **809 harms** on the E0 decode chain `[data]`); its disposition is **settled = §3.D-1
  annotate-not-override**. §3 re-frames it; it is NOT re-designed here.

Also built: `resolveCarriedReadingsExtending` (`:608-673`) — the dormant bounded-context forward-extension
requester loop (default OFF ⇒ byte-identical to the base resolver), and the §8 primitive it fires through
(`forwardoverride.cpp` `OnePassClosure::tryOverride` / `forwardRecompute`).

### §1.3 The output assembly already built — `assembleFunctionOutput` [code]
`assembleFunctionOutput` (`functionoutput.h:180-185`) is **pure assembly, no re-derivation** (§7): it shuffles the
Step-1..5 products into the `FunctionLayerOutput` contract and combines the confidence at default weights. It
carries, **additive over the L4 committed chord** (`FunctionAnalysisUnit`, `functionoutput.h:115-127`):
- the **full DCML Roman numeral** (`relational.label`, base RN + relational label already combined upstream);
- the **`FunctionConfidence`** — three fixed components (cadence-vote weight, licensed-progression fit,
  next-best margin) combined at default weights into `combined`, **plus** the boundary squash `combinedBoundary =
  combined/(combined+kBoundary) ∈ [0,1)` (D-L5a, `functionoutput.h:90-98`) required by contract U2;
- the honest **`openMark`**;
- the **`committedIdentity`** carried verbatim (L4's decision preserved, not replaced).
Per region: `FunctionRegionMarkers` (local key possibly modulated, cadence markers).

### §1.4 The confidence contract realized in code, and what is already declared [code][contract]
The contract's frames/rules (`cowork_confidence_contract.md` §4/§5) are realized as:
- **Frame F-B** (`:458-468`) — incumbent `s.confidence.composite` (L4 vertical-fit-only, [0,1]); contradiction
  `bestPlaus − committedPlaus` (integer ∈ {0..3}); the §8 `tryOverride` bar. Faithful to the declared frame; the
  finding is a **premise-invalidation, not a drift** (`cowork_fb_redesign_design.md` §1.4).
- **Frame F-A** — the cadence-confirmed modulation recompute (L5 §5.4; lives on the modulation path, not
  `functionresolver.cpp`).
- **D-L5a CLOSED** — the boundary squash is published (`combinedBoundary`).
- **D-FS OPEN** — the frame contradiction *scales* (F-A cadential weight, F-B plausibility diff) are declared but
  their squash constants / θ are Stage-5 calibration (`[contract]` §7 D-FS). Not touched here.

### §1.5 Built vs owed — the summary Layer 5 engagement stands on
| Concern | Built (dormant) | Owed at engagement |
|---|---|---|
| Input contract | `FunctionSlice` fields declared `[code]` | **populate from the live decoder** (§2 wiring) |
| Abstain selection | `resolveAbstained` per `AmbiguityKind` `[code]` | **generalize to the full distinct-root carry**, not the readingA/readingB pair (§3) |
| Symmetric-rotation over the pool | reasons over full `alternatives[]` `[code]` | the structural precedent §3 extends to all kinds |
| Fine-grain override (F-B) | `attemptFineGrainOverride` `[code]` | **re-frame as annotation** (settled §3.D-1) — §3.3 |
| Output assembly | `assembleFunctionOutput` `[code]` | maps L4 chosen → RN; confidence emit — §3.4 |
| Confidence boundary | `combinedBoundary` (D-L5a) `[code]` | add the selection's joint-consistency margin as a declared Class-M confidence — §3.4 |
| Pedal detection | **none in the decoder** (audit gap) `[code]` | a **new reader-over-carry** — enumerated §4.2 |
| Joint key↔chord | **none** (C3 un-computable, `cc_engage_c3_measurement_report.md`) `[data]` | a **distinct downstream step** O-18 — enumerated §4.3 |

---

## §2 — The carry contract: decoder → Layer 5 (Task 2)

### §2.1 What Layer 5 reads — the distinct-root distribution, not a top-N list
The §8 arc fan-out measurement (`cc_engage_fanout_measure_report.md`) fixes the **factual shape** of the carry
`[data]`: per competition slice the above-threshold ranked set is **wide in readings but narrow in roots** —
median **5/4/5** readings (Baroque/Jazz/Default) but distinct **roots** median **2/1/2**, mean **2.13/1.73/2.12**.
The large reading count is mostly template/voicing variants of the same ~2 roots.

So the carry contract is best expressed on the **meaningful axis — distinct roots**. Per slice Layer 5 reads a
**distribution over distinct roots**, each root carrying:
- its **best voicing/variant** (root+quality+bass/inversion+extensions — the `ChordSliceCandidate` identity,
  carried verbatim for emission, §5.5/§7);
- its **variant set** (the template/voicing/inversion alternatives at that root — the material the bass/inversion
  channel §3.2 reasons over);
- its **carried confidence** — the L4 `SliceConfidence`/score, so a root's *rank and margin* survive, not just its
  presence.

### §2.2 The exclusion tail is load-bearing and must be carried (#12)
The decisive fan-out finding `[data]`: a **≥3rd distinct root clears threshold on 25.1 % / 16.1 % / 24.9 %** of
slices. This is exactly the **load-bearing exclusion tail** (#12, finding-by-exclusion): the ruled-out and
low-confidence roots are **information**, not noise — they are where selection (§3) and the eventual joint step
(§4.3) earn their keep. The contract therefore requires: **carry every above-threshold distinct root, each at its
graded confidence; carry ruled-out roots at low confidence rather than dropping them.** A carry that surfaces only
the winner + one alternate (the legacy cap-of-3 + single diff-root append) **discards the ≥3rd root on ~¼ of
slices** — a #12 violation the engaged carry must not inherit.

### §2.3 Does the decoder's governed carry provide this? The distinct-root guarantee is OWED [code]
The decoder builds `sc.alternatives` as (`chordslicedecoder.cpp:746-789`) `[code]`:
1. the distinct chord **voicings** after `chosen` — deduped by `sameChordVoicing` (`:752`), capped at
   **`topK` (default 6, `chordslicedecoder.h:169`)**;
2. **∪ the prevailing chord** (the L3-incumbent-carry pattern, `:766-789`) — kept alive even when below `topK`, so
   the incumbent root always survives.
Plus `nameOpenQuestion` (`:925-975`) sets `readingB` = the first alternative with a **different root+quality**
(`:929-931`), so on an **abstain** exactly one alternate root is *named*.

**The gap, stated precisely `[code]`:**
- The `topK` cap is on **voicings** (`sameChordVoicing`), **not roots**. `topK=6` voicings can be **saturated by
  the top ~2 roots' inversions/templates** before a 3rd distinct root is reached — so the ≥3rd-root minority
  (25 %/16 % of slices, §2.2) is **not guaranteed to survive** into `alternatives[]`. This is a *smaller* leak
  than the legacy cap-of-3 (topK=6 > 3), but it is **not a structural guarantee**.
- The **incumbent-carry guarantees the prevailing root**, and **readingB names one alternate root on abstains** —
  but neither guarantees a *third* distinct root, and on a **Commit** slice `openQuestion` is `None` (`:914`) so
  **no alternate root is named at all** — only whatever `alternatives[]` happens to hold.
- The signed spec already records this as a known input property, not a defect: §15-2 "the carried `alternatives`
  are **capped (topK)**" `[code]`.

**The owed guarantee (structure only; R5).** The engaged carry must **preserve distinct roots explicitly**, not as
a by-product of a voicing cap. The declared *shape*: a **distinct-root-first carry** — for each distinct root above
threshold, carry its best voicing + its variant set + its confidence, and cap on **distinct roots** (with each
root's own variant depth bounded), rather than capping on a flat voicing list. The exclusion tail (#12) is carried
as the low-confidence roots below the primary set. **The exact cap depths (how many distinct roots, how deep each
root's variant set) are precision-phase constants (R5)** — the fan-out distribution (p90 ≈ 4 roots, max 11)
informs the *floor*, but the value is fitted later, not here. This is an **owed change to the decoder's carry
construction** (Layer 4 / E4), named here so the engagement design and E4 agree on the contract; it is not built
in this pass.

> **Note (scope of the fan-out measurement) `[flag]`.** The §8 fan-out was measured on the **legacy production
> path** (`gateCtx.rawCandidates`, cap-of-3) — the current substrate. The decoder's `alternatives` (topK=6) is the
> *engaged* substrate that replaces it at E4. Both draw from the same 204-cell scored grid, so the **distinct-root
> distribution (median 2, ≥3rd on 25 %/16 %) is a property of the scored set** and applies to the decoder's carry
> too; the exact voicing-count a topK=6 cap admits was not separately measured on the decoder path. The
> distinct-root *guarantee* gap (§2.3) is a structural argument from the cap being voicing-keyed, independent of
> that unmeasured count.

---

## §3 — The selection architecture (Task 3; STRUCTURE only, R5)

### §3.1 The objective: select by JOINT CONSISTENCY, not by strengthening one score
The decisive published lesson `[research]` §2: **select by joint consistency across key / root / inversion /
bass**, not by maximizing any single score. ChordGNN wins the full Roman-numeral label while scoring *lower* on
the individual heads — the payoff is the mutually-consistent reading, not a stronger vertical or progression
score; AnalysisGNN's logit-fusion confirms it. This is the direct analog of our selection problem and the steer
for the L5 objective.

So engaged Layer 5's selection, for each slice, reasons over the **graded distinct-root distribution including the
exclusion tail** (§2, #12) and picks the reading that is **maximally consistent across the evidence channels**,
carrying the rest at graded confidence and open-marking where no reading dominates. This **generalizes**
`resolveAbstained` (§1.2): today only the SymmetricRotation arm reasons over the full pool; the other arms decide
on the readingA/readingB pair. Engaged selection lifts *all* kinds to reason over the full distinct-root carry —
the SymmetricRotation arm is the structural precedent.

### §3.2 The evidence channels, ranked by the research (load-bearing first) [research]
The channels the selection composes, and their evidentiary weight from the literature and our own F-B finding:

| Channel | Role | Grounding |
|---|---|---|
| **Bass / inversion** | **load-bearing** — a strong, semi-independent root-correctness signal. The committed bass (carried verbatim, §2.1) supports/undercuts each candidate root's inversion. | Vuvan et al. 2021 dissociate bass from pitch-class content; both independently drive expectation `[research]` §1 |
| **Pitch spelling** | **load-bearing** — disambiguates enharmonic/symmetric roots pitch-class-blind fit cannot (the symmetric-rotation churn). Read only where the distinction *is* a spelling distinction (§8 crosscutting). | Micchi 2020; McLeod & Rohrmeier 2021 `[research]` §1 |
| **Joint consistency w/ region key** | **load-bearing** — a root's diatonic/functional fit in the region's local key; the §5.7 degree bias is the built soft form. | ChordGNN/AnalysisGNN joint-consistency `[research]` §2 |
| **Cadence tonic-vote** | supporting — pins the tonic in RelativePair / leading-tone-rotation cases (§5.2, already built). | signed spec §5.2 `[code]` |
| **Licensed progression** | **weak / NON-load-bearing for root correctness** — a tidy signal *uncorrelated* with root correctness; used only as a **tie-break among already-consistent readings**, NEVER as an override lever. | F-B measured net-harm `[data]`; Korzeniowski & Widmer 2018; Vuvan 2021 `[research]` §1 |
| **Metric position / harmonic rhythm** | supporting feature (not a hand-weighted prior). | ChordGNN 2023; AnalysisGNN 2025 `[research]` §1 |

The **re-ordering vs the as-built resolver** is the load-bearing structural change: the built `resolveAbstained`
leads with `isLicensedProgression` (the weak channel) as its *primary* separator (Transition/ShareTone arms). The
research says bass/inversion + spelling + key-consistency are the primary channels and progression is the
tie-break. Engaged selection **re-orders** so the load-bearing channels decide and progression only breaks ties
among mutually-consistent readings. *(The channel weights and the deciding margin are precision-phase, R5 — only
the ordering/direction is fixed here.)*

### §3.3 Reconciling with the F-B finding and the existing frames
The settled F-B disposition (`cowork_fb_redesign_design.md` §4, ratified surface) is **§3.D-1: demote F-B from
OVERRIDE to ANNOTATION** (the §8 case-3 honest carry), floored by §3.A (disable). The measured basis: the override
is net-harmful by −756, no θ repairs it, no structural gate on the available features beats disable, and the
incumbent-repair premise is refuted `[data]`. This design **consumes that finding**:
- Engaged selection's **load-bearing channels are bass / spelling / key-consistency / cadence** (§3.2) — exactly
  the channels the research says carry root correctness and F-B lacked.
- The **licensed-progression signal is demoted to a tie-break** among already-consistent readings — never an
  override of a vertically-committed root. This is the structural form of "F-B's progression contradiction is
  uncorrelated with correctness."
- **Frame F-B is re-declared as an annotation channel, not an override frame** (`[contract]` §4 requires the
  re-declaration; the mechanics — the advisory field, the annotate-vs-mutate action — are a **downstream
  follow-on**, §4.3, per the F-B doc's §4.2). Engaged selection **carries the L4 commit unchanged** and, where the
  functional context contradicts it, **surfaces the contradiction as an honest open mark / advisory** (the §8
  case-3 honest carry), preserving the contradiction signal (#12) without overturning the vertically-correct root.

### §3.4 The confidence Layer 5 publishes [contract]
Engaged Layer 5 publishes, per the confidence contract (U2/R4–R6):
- the **`FunctionConfidence`** (§7) — three fixed components combined at default weights (unbounded internal
  `combined`) + the **boundary squash `combinedBoundary ∈ [0,1)`** (D-L5a, already built);
- **NEW: the selection's joint-consistency margin** as a declared **Class-M** confidence — "how much more
  consistent is the selected reading than the best *different-root* reading, across the §3.2 channels" — squashed
  to [0,1) by a fixed monotone map (R5). This is the honest confidence of the *selection decision itself* (U1: it
  attaches to the named decision "function-of-unit-by-selection"), distinct from the resolver's `nextBestMargin`
  component. Its squash shape is declared here; **its constant is precision-phase (R5)**.
- **abstention / open mark = the selection margin below the declared bar** (contract U5) — uniform with the rest
  of the contract; the honest residual is carried, never guessed.

**No constant is fitted (R5).** Every weight, margin, and squash constant above is a default seed; the point is
*declared comparability*, not tuned optimality. The Class-M → Class-P calibration of these confidences is Stage-5
(contract §6 C1), out of this pass.

---

## §4 — Layer boundaries, engagement gaps, and the downstream agenda (Task 4)

### §4.1 Layer boundaries (#7) — what belongs where
- **Layer 4 (the decoder's carry)** owns: producing the per-slice **distinct-root distribution** (candidate
  readings + variants + per-slice confidence + committed identity), under a **region key already chosen by
  Layer 3**. The distinct-root-preserving carry (§2.3) is a **Layer-4/E4** concern.
- **Layer 5 (selection over the carry → the functional analysis)** owns: **selecting** among the carried readings
  by joint consistency (§3), producing the Roman numeral, the cadence markers, the region local key (possibly
  modulated), and the honest open marks. It **reads L4's carry forward and never re-derives from notes** (D4) — it
  reasons **within** the region key L3 chose.
- **The joint key↔chord step (O-18 / contract C3)** is a **distinct step, not L5 selection.** L5 selection reasons
  within a *fixed* region key; the joint step is the coupled machinery that **re-ranks the key under chord
  evidence** (and vice versa) — the "carry a beam of (key, chord) hypotheses and let downstream chord evidence
  re-rank the key" of `[research]` §3. It is the home of the C3 "genuinely-coupled key↔chord minority."
- **Acyclicity (the forward-only control-flow contract, §8/§9-D7).** L5 reads L4's carry forward; the only
  cross-layer *recompute* is the §8 localized-forward-convergence-bounded mechanism (marked-final one-pass
  closure), never a back-edge. The joint step, when built, is a **bounded** instance of that same forward
  discipline (a declared exception with its own closure), not a free cross-layer search — which the spec measured
  inert (§8 "What this is NOT").

### §4.2 Engagement gaps — what the dormant Layer 5 is MISSING for production
1. **The carry wiring** — populate `FunctionSlice` from the live decoder `SliceChord` (today hand-injected;
   §1.1). The load-bearing engagement build.
2. **The distinct-root guarantee in the carry** — the owed §2.3 change to the decoder's carry construction (E4).
3. **Pedal detection as a reader-over-carry** — the **decoder has none** (structural-integrity audit gap; the
   legacy `chordpostpasses.cpp` pedal pass clobbers `results` and re-implements a diff-root scan — a Layer-4
   legacy tangle that retires with E4). Engaged Layer 5 (or its carry) needs pedal detection as a **reader over
   the carry**, not a `results`-mutating post-pass. **Its home is a downstream decision (§4.3).**
4. **The F-B annotate mechanics** — the advisory field on `ResolvedReading` and the annotate-vs-mutate action
   (settled disposition §3.3; mechanics are §4.3).
5. **Frame-scale commensurability (D-FS)** — the contradiction-scale squashes / θ the contract leaves to Stage-5;
   the annotate re-frame (§3.3) removes F-B's override arithmetic from the critical path, but the F-A modulation
   frame still consumes it — a Stage-5 calibration dependency, not this pass.

### §4.3 The downstream pieces this Part DEPENDS ON — enumerate, do not resolve (#8)
Each is a follow-on pass; named here with the carry/selection decision that hinges on it, so the follow-on has its
agenda:

- **FQ-2 — the quality-from-key single owner.** The structural-integrity audit found quality-from-key
  second-guessing has **no single owner** (≥4 sites / 3 layers). **Hinge:** §3.2's key-consistency channel reads a
  root's quality-in-key; if quality-from-key is re-decided in multiple places the selection channel is reading an
  un-owned signal. The owner must be fixed (a Layer-5 decision per the sequencing call) before the key-consistency
  channel is more than structural.
- **Pedal detection's home.** **Hinge:** §4.2 gap 3 — whether pedal detection is a Layer-4 carry annotation (a
  slice property the carry exposes) or a Layer-5 reader-over-carry determines *what the carry contract carries* and
  *what selection consumes*. The distinct-root carry (§2.3) and the selection channels (§3.2) both change if pedal
  points are a carried slice attribute.
- **O-18 / C3 — the joint key-and-chord step.** **Hinge:** the exclusion tail (§2.2, #12) is carried **so the
  joint step can re-rank the region key under the carried chord alternatives** — that is *why* the ≥3rd root is
  load-bearing. The joint step is un-computable today (C3 trigger not computed anywhere,
  `cc_engage_c3_measurement_report.md` `[data]`) and its design is owed at Stage 5; the carry contract (§2) is
  designed to **feed** it (the beam of hypotheses `[research]` §3), and the §4.1 boundary reserves its place. The
  F-B correction job (§3.3) re-homes here long-run.
- **The F-B annotate mechanics.** **Hinge:** §3.3 — the annotation action (the `ResolvedReading` advisory field,
  the contract §4 F-B re-declaration, the L5 §5.5/§10/§15-2 spec edits) is the *mechanics* of the settled
  disposition; a separately-ratified build event (`cowork_fb_redesign_design.md` §4.2). Selection's structure
  (§3.3) is fixed; the mechanics are the follow-on.

---

## §5 — What this Part settles, and the boundary honored

**Settles:** the dormant Layer 5 inventoried at code (built vs owed, §1); the **carry contract** on the
distinct-root fan-out with the exclusion tail preserved (#12) and the decoder's distinct-root guarantee named as
owed (§2); the **selection-by-joint-consistency** architecture — evidence channels ranked load-bearing-first,
progression demoted to a tie-break, reconciled with the F-B annotate finding and the confidence frames (§3,
structure only, constants precision-phase R5); the **layer boundaries**, engagement gaps, and the enumerated
downstream agenda with each hinge named (§4).

**Boundary honored (#8 / R5):** no `src/` change, no build, no corpus write, **no constant fitted or tuned** — the
architecture of the selection is designed; the fitting is the later precision phase. No downstream concern-owner
is resolved (enumerated only, §4.3). Every claim is tagged to the code / the contract / the research (#1); gaps
are flagged (§2.3 note, §4.2), not assumed. This designs no inference fix — where selection's recovery of the 53
F-B corrections requires a correctness-correlated signal, that is declared to Cowork as an inference-quality
question (§3.3), not built here (#8, #13).

*CC, 2026-07-07. Engage arc #9 — Layer-5 engagement design Part 1 (carry + selection), read-only, structure-only.
Both regression stops untouched/green (no `src/`, no build). Fork-only; `upstream` untouched.*

---
---

# Layer-5 engagement design — Part 2: PEDAL detection's home + the F-B ANNOTATE mechanics

> **Status: DESIGN (CC, 2026-07-07). READ-ONLY architectural design pass — no `src/` change, no build, no corpus
> write, no constant fitted or tuned.** Engage arc #11, the **last two Layer-5 engagement design pieces** Part 1
> enumerated as follow-ons (§4.2 gap 3 pedal, §4.3 F-B annotate mechanics). Settling them **closes the Stage-2
> design phase** (`cowork_engage_arc_plan.md`). Provenance report: `cc_engage_l5_pedal_annotate_design_report.md`.
>
> **★ STRUCTURE ONLY — constants are precision-phase (R5). Not inference work (#8).** This designs the *architecture*
> of the pedal reader and the F-B annotation (their homes, how they read the carry, the vehicle they reuse); it
> fits no constant, tunes no threshold, chases no case.
>
> **Why a Part 2 appended here, not a new doc (#6, one home per concern).** Part 1 designed the carry + selection
> and **explicitly deferred these two pieces to itself** as §4.3 downstream hinges ("Pedal detection's home"; "The
> F-B annotate mechanics"). They are the *same* Layer-5-engagement concern, not a distinct one — folding them into
> the doc that enumerated them keeps one home for the engagement design (Part 1 = carry+selection, Part 2 = the two
> owner-decisions it left open). A new doc would split one concern across two files. Section numbering continues
> globally: Part 1 is §1–§5, Part 2 is §6–§10.
>
> **Grounding tags** (as Part 1): `[code]` = read at the named source symbol; `[contract]` =
> `cowork_confidence_contract.md`; `[audit]` = `cowork_structural_integrity_audit.md`; `[fb]` =
> `cowork_fb_redesign_design.md`; `[joint]` = `cowork_joint_key_chord_design.md`; `[flag]` = a gap the evidence
> does not close, called out rather than assumed.

---

## §6 — Pedal detection: a reader over the carry, not a winner-mutator (Task 1)

### §6.1 The current mechanism at the code, and its three symptoms `[code][audit]`
`applyIter8691Pedal`'s pedal tail (`chord/chordpostpasses.cpp:209-281`) runs, over the legacy `results` substrate:
1. reads `r1 = results.front()` (the Pass-1 full-voice winner) and tests `!cptIsBassChordTone(bassPc, r1…)` —
   the structural entry condition "the sounding bass is not a chord tone of the winner" (`:210-215`);
2. strips every tone at `bassPc` and runs a **whole second analysis** `RuleBasedChordAnalyzer{}.analyzeChord(upperTones…)`
   → `pass2` (`:216-249`);
3. computes a confirmation gap = `pass2.front().score − pass2AltScore`, where `pass2AltScore` is found by a
   **hand-rolled scan for the best DIFFERENT-root competitor** in `pass2` (`:262-269`), squashed through a sigmoid
   `c2` (`:270-271`);
4. on `c2 ≥ pedalConfidenceThreshold`: **`results = pass2`** (`:274`) — the whole winner+carry vector is
   overwritten — then stamps `isPedalPoint`/`pedalBassPc` on the new `front()` (`:275-276`).

The structural-integrity audit `[audit §1.1 #7 / §1.3]` catalogues this as **VIOLATION / HIGH** — "a detection
concern mutating the winning identity in place," with three coupled symptoms, all reproduced verbatim above:
- **(i) the clobber** — `results = pass2` replaces the shared winner+carry vector, discarding the Pass-1
  full-voice reading and its distinct-root alternatives (a #12 information-loss on the carry);
- **(ii) the re-implemented diff-root scan** — `:262-269` is the **4th copy** of the "best different-root
  alternative" decision (`[audit §1.3]`: the append `:537-540`, the pedal gap here, the FM2/`promoteToWinner`
  primitive, and the decoder `chordslicedecoder.cpp:927-930`);
- **(iii) the defensive append-disable** — `pass2Prefs.inversionSuspicionMargin = 0.0` + a fresh `pass2GateCtx`
  (`:240-245`) exist **only** to suppress the legacy cap→append/inversion-correction (a display-carry concern)
  because it "would distort the confidence gap used to confirm the pedal" (`:237-239`) — a display concern
  contaminating the detection math.

And the named gap `[audit §1.4]`: **the dormant decoder has NO pedal detection** (grep of
`chordslicedecoder.cpp`: 0 matches `[code]`) — engagement must give pedal a home, it is not inheriting one.

### §6.2 The material pedal needs is (usually) already IN the carry `[code]`
The pedal decision needs two things: (1) the **upper-voice harmony** (the chord above the sustained bass) and
(2) a **confidence gap** confirming it. Both are latent in the decoder's governed carry (Part 1 §2):
- A pedal slice's full pc set is `{pedal bass} ∪ {upper chord}`. A reading whose **root ≠ bass and whose template
  excludes the bass pc** — i.e. the upper-voice chord with the bass as a non-chord-tone — is exactly a **distinct-root
  alternative of the full slice**. The distinct-root-preserving carry Part 1 §2.1/§2.3 mandates (each distinct root
  with its best voicing + variant set + carried confidence, **including the exclusion tail #12**) is therefore the
  natural place the upper-voice reading already lives — *as a carried alternative*, not as a second decode.
- The confirmation gap pedal computes by hand (§6.1 (ii)) is the **carried confidence margin between the pedal
  reading's root and the committed (bass-rooted) root** — already the carry's distinct-root ranking (Part 1 §2.1:
  "carry its confidence, so a root's rank and margin survive").

So the clean design reads the carry rather than re-deriving from a second analysis — **subject to one owed
measurement** (§8.3 [owed-P1]): whether the carried distinct-root alternative (bass-as-non-chord-tone) **agrees**
with today's upper-voice re-decode `pass2`. Stripping the bass pc can change which template wins among the upper
voices, so the equivalence is a corpus fact to *measure*, not assume `[flag]`.

### §6.3 Placement (#7): a reader-over-carry producing a distinct pedal-annotated result
Pedal detection is a **chord-identity concern** (it decides "the harmony is the upper-voice chord; the bass is a
non-chord pedal tone"). Part 1 §4.3 left its home as a hinge between two forms; this pass **decides it**, grounded:

- **Home: a reader over the decoder's Layer-4 carry, emitting a pedal-annotated result — an additive annotation on
  a carried reading, NOT a mutation of the winner.** Because the material it needs is the carry's distinct-root
  distribution (§6.2), and chord identity is Layer 4, the reader sits at the **carry side (Layer-4 output / a
  decoder post-reader)** and feeds L5 selection *one* pedal-annotated candidate. It never owns `results.front()`
  and never writes back into the decoder's scoring — it reads the carry forward and annotates.
- **What it emits:** on the pedal structural condition (bass is a non-chord-tone of the committed reading) **and** a
  carried distinct-root alternative excluding the bass clearing the pedal-confidence bar, the reader **marks that
  alternative as the pedal reading** (`isPedalPoint`, `pedalBassPc`, the upper-voice chord as the identity) and
  carries it as the slice's pedal-annotated candidate — **while the original full-voice reading and the rest of the
  distinct-root distribution SURVIVE in the carry** as honest alternatives (#12: no information loss; the bass-rooted
  reading is retained at its graded confidence, not overwritten). Selection (Part 1 §3) then reasons over the carry
  *including* the pedal annotation, exactly as it reasons over any carried reading.
- **The upper-voice-re-decode fallback, if the measurement forces it `[flag]`.** If [owed-P1] shows the carried
  alternative materially diverges from the bass-stripped re-decode, the correct form is **not** the legacy in-place
  second analysis but a **Layer-4 carry annotation**: the decoder (which already holds the slice's tones) exposes an
  upper-voice-conditioned reading as a *carried slice attribute* — still a reader/annotation, still no winner
  mutation. Which form is right is the measurement's to settle; both keep pedal a reader, never a mutator.

### §6.4 The three symptoms dissolve under reader-over-carry
- **(i) clobber → gone.** The reader **annotates a carried candidate**; it never assigns `results = pass2`. The
  winner+carry vector is not overwritten; the full-voice reading is preserved (#12). The pedal reading is one more
  carried candidate (pedal-annotated), which selection weighs — not a silent replacement of the whole vector.
- **(ii) re-implemented diff-root scan → gone.** The confirmation margin is **read** from the carry's distinct-root
  ranking (§6.2). No 4th hand-rolled scan — this is the FQ-1 tie (§6.5).
- **(iii) defensive append-disable → gone by construction.** The cap→append/inversion-correction the pedal defended
  against is a property of the **legacy `results` substrate** (`[audit §1.2]` the cap→append pair). The decoder's
  carry is **governed** — `topK`-on-distinct-voicings ∪ a principled incumbent-carry (`chordslicedecoder.cpp:746-789`,
  `[audit §1.4]` OK) — there is **no display-carry append to contaminate** the pedal math, so there is nothing to
  defensively disable. The pedal reader reads a clean governed carry.

**All three are symptoms of the single defect** the audit named — pedal *mutating the winning identity in place*
rather than *reading the carry and producing a distinct pedal-annotated result* (`[audit §1.3]`). Removing the
mutation removes all three at once; the reader-over-carry is that removal.

### §6.5 The diff-root need is served by the carry / FQ-1 — do NOT re-implement a 4th scan (#6)
The confirmation margin (§6.1 (ii)) is the **"best different-root alternative"** decision the audit catalogues as
computed 4× (`[audit §1.3]`, FQ-1). Under the engaged carry it is served two-ways-that-are-one: the decoder already
**reads** the best different-root reading from its carry (`chordslicedecoder.cpp:927-930` `[code]`), and FQ-1
unifies that scan into one primitive (`[audit]` FQ-1, sequenced into E4 — Stage-1 STOP-reported the four legacy
scans are *not* byte-identically one, so the unification lands with the decoder, not pre-L5). The pedal reader
therefore **consumes the carry's distinct-root margin** (or the FQ-1 primitive over the carry) — it adds **no fourth
scan**. This is the concrete pedal instance of Part 1 §2.2's load-bearing exclusion tail: the ≥2nd distinct root's
carried confidence *is* the pedal confirmation signal.

---

## §7 — The F-B annotate mechanics: reuse/unify the open-mark (Task 2)

### §7.1 The settled disposition (recap, not re-litigated) `[fb]`
The F-B fine-grain override is **measured net-harmful** — 1043 fires = 53 corrections + **809 harms** + 181 neutral
on the E0 decode chain, ~78 % of fires move an L4-correct root to a wrong one; no θ separates corrections from
harms; no structural gate on the available features beats disable; the incumbent-repair premise is refuted `[fb §2]`.
The ratified disposition is **§3.D-1: demote F-B from OVERRIDE to ANNOTATION** — carry the L4 reading **unchanged**
and flag the functional-context contradiction as calibrated uncertainty (the §8 case-3 honest-carry), floored by
§3.A disable `[fb §3.D-1/§4.1]`. Part 1 §3.3 already consumed this into the selection architecture (progression
demoted to a non-override tie-break). **This section designs only the *mechanics* of the annotation** — the vehicle
it writes to — which Part 1 §4.3 and `[fb §4.2]` left as the follow-on.

### §7.2 The vehicle (#6, the load-bearing decision): unify the open-mark, do NOT add a parallel channel
`[fb §4.2]` proposed *"a new `ResolvedReading` advisory flag `functionContextContradiction`."* The instruction
requires reconciling that with the **existing open-mark machinery**. Decided at the code:

**The existing open-mark carry** is one honest-uncertainty channel threaded through three structs `[code]`:
`ResolvedReading.openMark` (`functionresolver.h:170` — "the honest open mark — genuinely undecidable (§7)") →
`FunctionUnitAssembly.openMark` (`functionoutput.h:165`) → `FunctionAnalysisUnit.openMark` (`functionoutput.h:124`
— the L5→L6 contract). It is the realized §8 **case-3** carry (`cowork_layer5_function_design.md:582`: "earlier
layer was uncertain and the later evidence still cannot decide → carry the residual honestly") and the §15-13
both-licensed fall-through's honest terminus.

**Two rejected forms, and why:**
- **Overloading the plain boolean `openMark = true` on an F-B slice is semantically WRONG.** `openMark` means
  *"no decided answer — genuinely undecidable."* The F-B case is the opposite: **L4 committed confidently** (it is
  *not* undecided — `[fb §3.D-1]` "L4 is not even uncertain (it committed)") and the reading is carried unchanged;
  what is surfaced is a *secondary* contradicting signal. Setting `openMark` would tell L6/display "undecided" when
  L4 decided — an information loss (#12) and a **semantic collision** with the case-3 abstain meaning already on
  that field.
- **A parallel `functionContextContradiction` bool beside `openMark` is a duplicate channel (#6 violation)** —
  two booleans on the same struct both meaning "a surfaced honest-uncertainty annotation on this reading," threaded
  redundantly through the same three structs.

**The #6-clean vehicle: UNIFY into one structured open-mark carrying its REASON/KIND.** Promote the boolean
`openMark` (across the three structs and their assembly) to a small open-mark annotation that names *why* the slice
is marked — one channel, distinct kinds:
- **`Undecided`** — the case-3 abstain / §15-13 both-licensed honest-carry (today's `openMark = true` semantics,
  preserved exactly);
- **`FunctionContextContradiction`** — the F-B case: **the reading stays the L4 commit** (`overrodeCommit` stays
  **false**, `reading` = the committed chord — the additive-not-replace contract `ResolvedReading` already declares,
  `functionresolver.h:160-165` `[code]`), and the annotation carries the contradiction as calibrated uncertainty
  (§7.3).

This **reuses the existing open-mark carry path** (no new field threaded through three structs) and **dissolves
`[fb §4.2]`'s "new advisory field" into "the existing open-mark, enriched with a reason"** — a unification, not a
parallel channel, exactly the instruction's licensed outcome ("a *unified* advisory, not a duplicate"). It composes
with the existing `ResolutionBasis` transparency enum (`functionresolver.h:151-158`): the demoted
`ResolutionBasis::FineGrainOverride` value becomes an **annotation basis** (renamed/re-valued to
`FineGrainContradiction` — an owed spec edit, §8.2), never an override basis.

### §7.3 What it carries (#12): the contradiction as calibrated uncertainty
The information the override used to **discard** — it overwrote the L4-correct root on 809 slices `[fb §2]` — is
now **preserved twice over**:
- the **L4 reading is carried** (the correct root survives — the +756 net-correct-root recovery `[fb §3.A]`);
- the **contradiction is preserved as the open-mark payload** — the frame's two quantities (the L4 composite
  incumbent `C ∈ [0,1]` and the plausibility contradiction `S = bestPlaus − committedPlaus ∈ {2,3}`, `[fb §1.2]`
  `[contract §4 F-B]`) carried as a **Class-M calibrated-uncertainty** on the annotation (squashed per the contract
  R5; **its constant precision-phase, R5**). The 1043 signals `[fb §2]` become uncertainty annotations, not dropped
  — the exact information a future C3 joint step (`[fb §3.D-2]`, Part 1 §4.3) will consume. This is the §8 case-3
  honest-carry realized: **zero information loss** (#12), strictly dominating §3.A disable (which throws the 1043
  signals away) `[fb §4.1 point 4]`.

### §7.4 The trigger: an annotation trigger, never an override lever `[contract §4]`
The F-B fine-grain contradiction becomes an **annotation trigger**: when the frame's `S > θ·C` condition holds
(`[contract §4]` the §8 override arithmetic), the resolver **writes the open-mark reason
`FunctionContextContradiction` + the uncertainty payload** and **leaves the reading = the L4 commit**. It no longer
sets `overrodeCommit = true`, no longer mutates `prog[i].chord = toPC(bestAlt)`, and no longer fires the localized
`forwardRecompute` (`[fb §1.2/§4.2]`, `functionresolver.cpp:490-497` `[code]`) — there is no override, so there is
no recompute. **Frame F-B is re-declared in the contract §4 as an annotation channel, not an override frame**
(`[contract §4]` mandates the re-declaration: "an undeclared cross-layer comparison is a contract violation; a
retired/re-framed one must be recorded here"). This is the mechanical form of Part 1 §3.3 (progression demoted to a
non-override tie-break) and §3.2 (licensed progression is the weak, non-load-bearing channel — it may annotate,
never override a vertically-committed root).

---

## §8 — Boundaries, owed build, owed measurements (Task 3)

### §8.1 Layer boundaries (#7) — acyclicity kept, no new cross-layer reach-in
- **Pedal reader (chord-identity)** — lives at the **carry side (Layer-4 output / decoder post-reader)**; reads the
  decoder's governed carry *forward*, emits a pedal-annotated candidate consumed by L5 selection. **No back-edge**
  into the decoder's scoring; **no `results`-winner mutation**; the diff-root margin is read from the carry / FQ-1,
  not a fresh cross-layer scan. If [owed-P1] forces the upper-voice-conditioned form, it is a **Layer-4 carry
  attribute** the decoder exposes — still forward, still no reach-in.
- **F-B annotation** — lives in **Layer 5** (`functionresolver`, the case-4 site); reads L4's committed reading +
  the functional context the resolver already holds; writes the L5 output's open-mark (additive §7, the
  `ResolvedReading` contract's declared "it annotates; it does not replace"). **No override, no recompute, no
  back-edge** — the acyclicity Part 1 §4.1 requires is *strengthened* (the one former cross-layer *recompute* on
  the F-B path is removed).
- **No new cross-layer reach-in** is introduced by either piece; both are readers/annotators over an existing
  forward carry.

### §8.2 Owed build (enumerated, NOT built — held until ratified; E4/L5-engage-adjacent)
1. **The pedal reader-over-carry** (§6) — a carry-reader emitting the pedal-annotated candidate; consumes the
   distinct-root-preserving carry (Part 1 §2.3, the E4 prerequisite) and the FQ-1 primitive. Layer: carry-side /
   decoder post-reader. Retires `applyIter8691Pedal`'s pedal tail (`chordpostpasses.cpp:209-281`) with the anchor
   (FQ-4 / E4).
2. **The F-B annotation wiring** (§7) — (a) enrich the open-mark to carry a reason/kind across `ResolvedReading`
   (`functionresolver.h`) + `FunctionUnitAssembly` + `FunctionAnalysisUnit` (`functionoutput.h`) + `assembleFunctionOutput`;
   (b) demote `attemptFineGrainOverride` (`functionresolver.cpp:381-498`) from mutate-and-recompute to
   annotate-and-carry; (c) re-value `ResolutionBasis::FineGrainOverride` → `FineGrainContradiction`; (d) the contract
   §4 F-B re-declaration; (e) the L5 §5.5/§10/§15-2 spec edits + `docs/scoring_model.md` sync (per `[fb §4.2]`).
   Layer: L5. A separately-ratified build event (`[fb §4.2]`).

### §8.3 Owed measurements (#5 — flagged, not assumed)
- **[owed-P1] Pedal reader vs the current in-place detection — agreement.** Does the pedal reading read from the
  carried distinct-root alternative (bass-as-non-chord-tone) **agree** with today's upper-voice re-decode `pass2`
  on the corpus? If yes ⟹ a pure reader (no re-decode). If it materially diverges ⟹ the carry must expose an
  upper-voice-conditioned reading (a Layer-4 carry attribute, §6.3). **Not assumed** — a corpus fact to measure
  post-E4-carry, read-only, over the distinct-root-preserving carry. `[flag]`
- **[owed-P2] The confirmation gap from the carried margin vs the recomputed `pass2` sigmoid.** Does reading the
  carry's distinct-root confidence margin reproduce the current pedal-confirmation signal (`c2`, `:270-271`)? Owed
  post-E4. `[flag]`
- **[owed-FB1] F-B annotate is byte-identical on production today** (F-B is dormant — `[fb §1.1]`; its only callers
  are the unit tests and `--dump-fullspine`). The build event's robust-stop sandwich is an **identity-PASS** by
  construction; at engage, removing F-B's 809 harms must **move the class-(b) root-disagree DURATION favorably**
  (`[fb §4.3]` — the harms are ~non-symmetric pitch-class-decidable roots, class-(b) by construction). A measurement
  gate at the build event, **not** an assumption now. `[flag]`

---

## §9 — Stage-2 CLOSURE + the Stage-3 build inventory (Task 4)

### §9.1 The Layer-5 engagement design phase (Stage 2) is COMPLETE
With pedal home and F-B annotate settled, **every Layer-5 engagement design piece is designed, structure-only**:

| Piece | Arc | Doc | State |
|---|---|---|---|
| The carry contract (distinct-root fan-out, exclusion tail #12) + the selection-by-joint-consistency architecture | #9 | this doc Part 1 (§1–§5) | ✓ designed |
| The joint key-and-chord step (the coupled key↔chord decision) | #10 | `cowork_joint_key_chord_design.md` | ✓ designed |
| Pedal detection's home (reader-over-carry) + the F-B annotate mechanics (open-mark unify) | #11 | this doc Part 2 (§6–§10) | ✓ designed |

No Layer-5 engagement concern remains undesigned. The moratorium boundary held throughout: no `src/` change, no
build, no corpus write, **no constant fitted or tuned** (#8 / R5) across all three arcs. **Stage 3 (algorithmic
completion / E4) is the user's to open** — with nothing left undesigned.

### §9.2 What Stage 3 (E4 / algorithmic completion) inherits to BUILD
Each is enumerated (`[audit §3/§4]` fix-queue + sequencing; `[joint §4]`; this doc), not built — a later,
separately-ratified behavior change (#14) proven on the full surface (#15) under the robust-unit stop (#11) with the
re-baseline discipline (#16):

1. **The anchor — the decoder carry replaces `results`** (FQ-4, `[audit §1/§4]`): the cap→append + pedal clobber +
   Iter 86/91 in-place mutation die by construction as the governed carry becomes the substrate.
2. **The distinct-root-preserving carry** (Part 1 §2.3) — the E4 change to the decoder's carry construction (cap on
   *distinct roots*, not voicings; the exclusion tail #12 carried). **Prerequisite** for the pedal reader, the
   joint step B1, and the selection's full-fan-out reasoning.
3. **The pedal reader-over-carry** (Part 2 §6, owed build §8.2 #1) + its owed measurements [owed-P1/P2].
4. **The F-B annotation** (Part 2 §7, owed build §8.2 #2) + [owed-FB1] — the open-mark unify + the
   annotate-not-override demotion + the contract §4 re-declaration.
5. **Quality-from-key's single owner** (FQ-2, `[audit]` X/S12/S15/S16/S17) — decided **with** the §6-block
   dissolution (the arc plan's Stage-2/Stage-3 split); the hinge Part 1 §4.3 named for the key-consistency channel.
6. **The joint step B1–B4** (`[joint §4]`): **B1** the per-key chord re-decode driver over the built decoder (Layer
   4); **B2** the beam/coupling driver generalizing `decideJointKey` (the joint step); **B3** the trigger gate; **B4**
   the production wiring completing J-key-iii — plus its owed measurements (`[joint §5]`: the C3 coupled-set size,
   the beam-width ablation, the root-flip rate — all un-measurable until B1 exists).
7. **The owed migrations** (FQ-8, `[audit]`): the two-segmenters retirement (S3/S4), the two-pitch-context collapse
   (S2), the tpc-reader fold (S6), the `function/` dir rename (S18); **FQ-1** the different-root primitive (retires
   *with* the decoder — the pedal reader and Iter 86/91 route through it); **FQ-3** the `findTemporalContext`
   ownership move.
8. **The confidence-scale fix** (F-1 / S19 / D-FS, `[audit]` FQ-8) — Stage-5-adjacent; the annotate re-frame (§7.4)
   **removes F-B's override arithmetic from the critical path** (Part 1 §4.2 gap 5), leaving only the F-A modulation
   frame consuming the contradiction-scale θ — a Stage-5 calibration dependency, not a Stage-3 blocker.

Then **Stage 4 (R9)** splits `chordanalyzer.cpp` last, and **Stage 5** lifts the moratorium for the precision work
(recover the 53 F-B corrections via a correctness-correlated signal `[fb §4.4]`; wire the calibration maps + θ) —
per `cowork_engage_arc_plan.md`, unchanged.

---

## §10 — What Part 2 settles, and the boundary honored

**Settles:** **pedal detection's home** — a reader over the decoder's governed carry that emits a distinct
pedal-annotated result, never a `results`-winner mutation; the audit's three symptoms (clobber / re-scan /
defensive-disable) shown to **dissolve** under reader-over-carry, the diff-root need served by the carry / FQ-1 with
no 4th scan (§6). **The F-B annotate vehicle** — decided at the code as the **unified open-mark carrying a reason/kind**
(reuse, not a parallel channel; the plain boolean shown semantically wrong for a confident-commit contradiction),
the contradiction carried as calibrated uncertainty (#12), the trigger an annotation lever never an override (§7).
The **layer boundaries** (acyclicity kept, no new reach-in), the **owed build** (enumerated, not built), and the
**owed measurements** (flagged, not assumed) (§8). The **Stage-2-complete** statement and the **Stage-3 build
inventory** (§9).

**Boundary honored (#8 / R5):** no `src/` change, no build, no corpus write, **no constant fitted or tuned** — the
architecture of the pedal reader and the F-B annotation is designed; the fitting is Stage 5. Every claim is tagged
to the code / the audit / the F-B design / the contract / the joint-step design (#1); the pedal reader-vs-detection
agreement, the confirmation-gap reproduction, and the F-B engage-time stop movement are flagged as **owed
measurements** (#5), not assumed. No inference fix is designed here (#8, #13) — recovering the 53 F-B corrections
remains the declared Stage-5 inference-quality question (`[fb §4.4]`).

*CC, 2026-07-07. Engage arc #11 — Layer-5 engagement design Part 2 (pedal home + F-B annotate); closes Stage 2.
Both regression stops untouched/green (no `src/`, no build). Fork-only; `upstream` untouched.*
