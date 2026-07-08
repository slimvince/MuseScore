# The joint key-and-chord step — architecture design

> **Status: DESIGN (CC, 2026-07-07). READ-ONLY architectural design pass — no `src/` change, no build, no
> corpus write, no constant fitted or tuned.** Engage arc #10 (`cc_instruction_engage_joint_key_chord_design.md`).
> This DESIGNS the owed joint key-and-chord step's architecture; it does **NOT** build it. The build is a later
> algorithmic-completion event (E4-adjacent); this pass enumerates that build, it does not do it. Provenance
> report: `cc_engage_joint_key_chord_design_report.md`.
>
> **★ STRUCTURE ONLY — constants are precision-phase (R5). Not inference work (#8).** This designs the
> *architecture* — where the step lives, how key and chord couple, what it reads/emits, what must be built —
> grounded in published fact (#1) and the existing built structures. It declares shapes; it fits no constant,
> tunes no threshold, chases no case. Where a step needs a fitted value the *shape* is declared and the constant
> marked precision-phase.
>
> **Why a NEW doc, not a section of `cowork_layer5_engagement_design.md` (#6, one home per concern).** The L5
> engagement doc is scoped to **selection within a fixed region key** and explicitly declares the joint step a
> **distinct downstream step, not L5 selection** (§4.1) and **enumerates it as a downstream piece to resolve
> later, not here** (§4.3, the O-18/C3 hinge). This doc is that resolution — the O-4 deliverable ("the C3
> joint-step design document", `cowork_stage5_fitter_design.md`). Folding it into the L5 doc would mix "selection
> within a settled key" with "how the key gets settled by coupling" and muddy that doc's scope. This doc
> **references** the L5 doc's §2 carry contract and §4.1 boundary rather than restating them.
>
> **Grounding tags.** `[code]` = read at the named source symbol on live disk at HEAD `32709a9e7a`; `[contract]`
> = `cowork_confidence_contract.md`; `[research]` = `cowork_functional_analysis_research_grounding.md`; `[data]` =
> a measured figure from a named report; `[flag]` / `[owed]` = a fact the evidence does not close, called out as
> an owed measurement rather than assumed (#5).

---

## §0 — The one finding this design turns on

The joint step is **not a greenfield build.** Its **key-axis half is already built and measured** as the
`decideJointKey` machinery (J-key-i/ii/iii; `section/jointkeydecision.{h,cpp}` `[code]`): a scoped key-state
lattice (the signature home pair ∪ committed modulation spans), a **Viterbi with a key-transition prior**
(`JointKeyWeights.transitionPenalty` `[code]`), a measured **coupled minority** (`coupled = !chordPinned &&
keyAmbiguous`, `jointkeydecision.cpp:289-297` `[code]`; the ~13.5% "coupled core", `jointkeydecision.h:59-61`
`[code]`), and a **config-B chord→key coupling** that rewards the key under which the best chord candidate is
diatonic (`couplingScore`, `jointkeydecision.cpp:275-287` `[code]`).

What it is **missing** is the **chord axis** — the key→chord re-decode. config-B couples in ONE direction only:
it reads the *fixed production chord* alternatives (`chordAlts`) and scores their diatonic-ness under each key
hypothesis; **the chord winner never moves.** And J-key-iii, the production wiring of the key decision, states
the gap by name `[code]` (`regionanalyzer.cpp:388-395`):

> "The CHORD is left as the production chord R0 (NOT re-emitted) … so the chord-axis side-effect … is **DEFERRED
> to a faithful mechanism**. The key axis alone therefore moves; BIR/chord output is byte-identical to
> production."

That deferred chord re-decode is **exactly** the per-key chord re-decode C3 found computed nowhere
(`cc_engage_c3_measurement_report.md` §2.3 `[data]`). So the joint step's architecture is a **total-unification
completion (#6)** of `decideJointKey`: **generalize config-B's one-directional chord→key coupling into a
bidirectional (key, chord) beam by adding the deferred chord re-decode axis** — not a parallel new joint module.
Everything below builds on that single statement.

---

## §1 — Placement in the architecture (Task 1; #7 — the acyclicity question)

### §1.1 The decision: a BOUNDED coupling step, NOT a unified `(key,chord)` hidden state
The dispatch poses the two options `[research]` §3:
- **(A)** a **unified `(key, chord)` decision** (Raphael & Stoddard's single hidden state `(tonic, mode,
  chord-function)`), collapsing the current key-then-chord split into one layer;
- **(B)** the current L3/L4 kept **separate**, with a **bounded coupling** (a beam / bounded fixpoint over the
  carried keys) that respects the cross-layer acyclicity rule.

**Decision: (B) — a bounded coupling step.** Grounded, not by preference but by three binding constraints:

1. **#7 (adhere to layers) + #6 (no duplication).** L3 (`key/keymodesequence`) and L4 (`chord/chordslicedecoder`)
   are **built as separate layers, each with its own decoder, carry, and confidence** `[code]`. Option (A)
   discards both built decoders and re-lays the pipeline into one joint-state decoder — a rebuild of what is
   built (#6 violation) and a re-layering (#7 violation). Raphael & Stoddard's single state is a *modeling*
   choice `[research]` §3; the **recurring recipe** the literature actually prescribes (a **beam of (key, chord)
   hypotheses** + a **key-transition prior** + the **chord re-decoded under alternative keys**, `[research]` §3)
   is realizable in *either* factoring. We pick the factoring that fits the built layers — the bounded coupling
   over the two existing decoders.
2. **Magnitude realism `[research]` §3.** The joint win is **qualitative, concentrated on the hard/coupled
   cases** (the ~13.5% coupled core `[data]`; low single-digit points elsewhere). Collapsing the whole pipeline
   into a joint state to serve a minority is disproportionate. A bounded coupling that **fires only on the
   coupled minority** (the C3 trigger, §3) and is a **pass-through on the ~86.5% majority** is the proportionate
   realization — and it keeps the majority path byte-identical (a #12 property: no information moved where no
   coupling exists).
3. **The acyclicity / forward-only control-flow contract (§8 / §9-D7; L5 engagement §4.1 `[code]`).** The
   architecture forbids a back-edge L3←L4; the only cross-layer recompute is the §8 **localized,
   convergence-bounded, one-pass-closure** mechanism. Option (A) would not violate acyclicity (it has no
   layers to cycle between), but (B) must be designed to respect it — and it does (§1.3).

### §1.2 Where it lives — a distinct step at the L3/L4 → L5 seam
The joint step is a **distinct bounded decision box between the L3 key decode / L4 chord decode and L5
selection** — architecturally the same place `decideJointKey` + `applyJointKeyWiring` already sit (the region
orchestrator, after Pass-1 regions are formed, before L5 selection reasons within the settled key) `[code]`. Its
role, stated against the L5 boundary (L5 engagement §4.1 `[code]`):

- **L3** emits, per region, the carried **key distribution** — the argmax key ∪ `keyAlternatives` (the ranked
  alternative-key menu) ∪ `keyConfidence` (the D-L3a Class-M sequence margin), all already built and carried
  in-memory with no consumer yet (`harmonicrhythm.h:118-119` `[code]`). **The joint step is that consumer.**
- **L4** decodes the chord **under a given key** (its diatonic prior; "this increment takes one key",
  `chordslicedecoder.h:130-133` `[code]`) — a **pure function of (slices, key)**.
- **The joint step** consumes L3's carried key distribution and **drives L4's per-key re-decode** to settle a
  region **(key, chord)** for the coupled minority; on the majority it is a pass-through (L3 argmax + L4's single
  decode stand). It **publishes the settled (key, carry) forward to L5.**
- **L5** then **selects within the settled region key** (L5 engagement §3) — unchanged; it reads the same
  distinct-root carry contract (L5 engagement §2), now produced **under the joint-settled key**.

So the joint step **settles the region key**; L5 **selects the function within it**. The C3 minority (the
genuinely-coupled key↔chord decisions) is the joint step's population, not L5's.

### §1.3 How it avoids re-introducing a cross-layer cycle (#7)
The step is **forward-only** and is a **bounded instance of the §8 forward discipline** (the place the L5
engagement §4.1 reserved for it), by construction:

- It reads L3's **already-emitted, already-carried** key distribution (`keyAlternatives`/`keyConfidence`). It
  does **not** call back into L3's decode — L3 has finished; the alternative keys are the exclusion tail L3
  already published (#12). No L3←(joint) back-edge.
- The per-key chord re-decode is a **forward** invocation of L4 (a pure function). The joint step **drives** L4
  N times (once per carried key); L4 does not reach back into the joint step or L3. No L4←(joint) cycle — the
  joint step is L4's *caller*.
- The key **re-ranking** happens **inside the joint step's own bounded closure** (§2), not as a mutation pushed
  backward into L3's committed output. The joint step **owns** the coupled decision and publishes ONE settled
  (key, chord) forward. It is a new decision box, not a feedback loop over existing layers.
- Its closure is **bounded and convergent** (a single forward beam pass, linear in regions — §2.4; or a
  capped bounded fixpoint), a **declared exception with its own closure**, not a free cross-layer search — the
  precise discipline the §8 spec measured inert for its other bounded instances (edge-extension, one-pass
  closure) `[code]`.

**A placement that WOULD violate acyclicity** (flagged so the build does not drift there): letting L4's chord
decision write back into L3's *committed* region key as a side effect and then re-running L3's whole-score
Viterbi — that is the back-edge #7 forbids. The design avoids it by making the joint step the **owner** of the
coupled (key,chord) decision (it does the re-rank locally, in its own bounded beam) rather than a **feedback
patch** on L3.

---

## §2 — The coupling mechanism (Task 2; structure only, R5)

Designed from the research recipe `[research]` §3 (beam of (key, chord) hypotheses + key-transition prior + chord
re-decoded under alternative keys), realized as the **completion of `decideJointKey` config-B** (§0).

### §2.1 The beam of (key, chord) hypotheses
Per coupled region *r* (the C3 minority, §3), the step maintains a **bounded beam** of joint hypotheses
`h = (k, c_k)` where:
- **`k`** ranges over L3's carried key candidates for *r* — the argmax key ∪ `keyAlternatives`
  (`harmonicrhythm.h:118` `[code]`; the exclusion tail #12), plus, as today, committed modulation-span states
  (`decideJointKey`'s lattice, `jointkeydecision.h:53-56` `[code]`). Beam width **W** over keys = precision-phase
  (the floor is informed by the carried menu depth — `KeyModeSequencePreferences.maxAlternatives = 4`
  `[code]` ⟹ ≤5 keys — but the value is R5, not fitted here).
- **`c_k`** is the chord reading **re-decoded under `k`** (the owed axis, §2.2): the per-slice distinct-root
  carry L4 produces with `k` as its diatonic prior (the L5-engagement §2 carry contract, produced *under k*).

This is the **beam Wu & Yoshii's taxonomy calls the branching/joint coupling** (not the sequential
chord-then-key-from-chord the current pipeline is `[research]` §3) — carried so downstream chord evidence can
re-rank the key and vice versa.

### §2.2 The chord re-decoded under each carried key (the OWED axis)
For each carried key `k_j`, run **L4's existing decoder** (`ChordSliceDecoder::decode(slices, …, k_j, …)`) with
`k_j` as the diatonic prior → the per-slice carry `c_{k_j}` (winner root + the distinct-root distribution + per-
slice confidence) `[code]`. **This is the computation C3 found nowhere** and J-key-iii deferred by name (§0). It
is **not a new decoder** — it is N forward invocations of the built pure function (#6). The chord axis moves
because the decoder's winner *is* key-dependent in principle (the diatonic prior tips genuinely-close readings;
for a symmetric sonority the rotation is key-dependent — G4/C1 spelling-pin) `[code]` — but **how often it
actually flips is an owed measurement** (§5, [owed-3]).

**Faithfulness (the J-key-iii constraint, discharged).** J-key-iii deferred the chord axis because a *faithful*
per-region re-emission "cannot reproduce the multi-pass pipeline chord" — the legacy production chord is emitted
mid-pipeline (before Pass-3 tone merging), so a naïve re-emit injects ~6% same-key root-flip artifact `[code]`
(`regionanalyzer.cpp:388-393`). The **faithful mechanism it named is the engaged `ChordSliceDecoder`**: a **pure
function of (slices, key)**, so re-decoding under a different key is well-defined and reproducible — no multi-pass
artifact. **This is why the joint step is E4-adjacent** (§4): it builds on the engaged decoder, not the retiring
legacy `analyzeChord` seam. On the legacy path a faithful re-decode does not exist; on the decoder path it is
the decoder's own contract.

### §2.3 The key-transition prior — already built, reused (#6)
The "penalize implausibly rapid key change" the recipe requires `[research]` §3 (Raphael & Stoddard / Temperley)
is **already in the built machinery** and is reused verbatim, not rebuilt:
- `decideJointKey`'s Viterbi carries `JointKeyWeights.transitionPenalty` (default 1.2) across regions
  (`jointkeydecision.cpp:300-314` `[code]`);
- the L3 decoder's own `changeCost(a→b) = changeBaseCost + changePerFifthStep·(cof-distance) +
  relativePairExtraCost` (`keymodesequence.h:124-131`, `:261` `[code]`) is the same prior at slice granularity.

The joint step's key axis **inherits** this transition cost (one home, #6). All magnitudes are precision-phase
(R5) — the current values are source-true seeds, not fitted here.

### §2.4 Composition — how key and chord evidence combine into the joint score
The joint score of hypothesis `h = (k, c_k)` for region *r*, given the previous region's settled key `k_prev`:

```
J(h | k_prev) =  keyEmissionFit(k, r)                     // L3 emission — the note-fit of key k
              +  chordFit(c_k | k)                          // L4 — the re-decoded chord's own fit under k
              +  couplingTerm(c_k, k)                       // chord→key: c_k's winner diatonic in k
                                                            //   (the built config-B couplingScore, now over the
                                                            //    RE-DECODED chord, not the fixed production one)
              −  keyTransitionCost(k_prev → k)              // §2.3 transition prior
```

Properties (declared; constants precision-phase R5):
- **Additive, monotone, no veto** — every term re-ranks, none is a hard gate (the `decideJointKey`
  "−7-wall-in-reverse" safety property, `jointkeydecision.h:52-56` `[code]`; and R4 monotone-combination
  `[contract]`). The one structural change vs config-B: `couplingTerm` and `chordFit` are computed over the
  **re-decoded** `c_k`, so the chord axis genuinely participates — the completion of §0.
- **Contract-clean channels (R6, no cross-scorer mixing).** Each channel is a declared quantity; they compose
  into ONE joint scorer over the joint hypothesis space, so the resulting margin (§2.5) is a **single Class-M
  value over one scorer**, not an ad-hoc mix of two margins — R6-compliant by construction.
- **Beam decode, not a fixpoint (recommended).** The region sequence is decoded by **one forward beam / Viterbi
  pass** over the joint states (the existing `decideJointKey` Viterbi shape, extended so each lattice state
  carries its per-key chord re-decode) — **linear in regions, convergent by construction, forward-only** (§1.3).
  A **bounded-fixpoint** variant (re-key → re-chord → re-key, capped at `maxJointSteps` like
  `maxEdgeExtendSteps = 4` `[code]`) is the alternative; it is **not recommended** — the beam achieves the joint
  disambiguation in one pass without an iteration whose convergence must be separately guaranteed. If a fixpoint
  is ever wanted, its cap is the declared closure (§1.3). **[owed-4:** whether a single beam pass suffices or a
  bounded fixpoint adds anything is an owed measurement, §5.**]**

### §2.5 The confidence the step publishes — a declared Class-M joint-decision confidence
Per the contract (U1/U2/R4-R6 `[contract]`), the step publishes, for the named decision
**"joint-key-chord-of-region"**, a **Class-M** confidence:

> **the margin of the winning joint hypothesis `h* = (k*, c*)` over the best *different* joint hypothesis** —
> different in key OR in chord-root — under the joint score `J`, **squashed to [0,1) by a fixed monotone map
> (R5).**

- It is **ONE margin over ONE joint scorer** (§2.4), so it is a legitimate single Class-M value (R6), not a mix
  of the L3 key margin and the L4 chord margin.
- It **attaches to the named joint decision** (U1), distinct from L3's `keyConfidence` (the key-only sequence
  margin, which the step still consumes as an input) and from L5's selection margin (L5 engagement §3.4).
- **Abstention** = the joint margin below the declared bar (U5): where no joint hypothesis dominates, the step
  emits the honest open mark and carries the tied (key, chord) hypotheses forward (#12) — it never forces the
  coupled call (`keymodesequence.h:70-72` "the genuinely ambiguous residual … left for the later, gated
  key-and-chord step — never forced" `[code]`).
- The squash **shape** is declared here (a fixed monotone map, e.g. `m/(m+k)` as D-L5a uses `[code]`); its
  **constant is precision-phase (R5)**; the Class-M → Class-P calibration is Stage-5 (contract §6 C1), out of
  scope.

**No constant is fitted (R5).** Every weight, the beam width, the transition magnitude, the squash constant, and
the trigger bar are default seeds; the point is *declared comparability*, not tuned optimality.

---

## §3 — The trigger (the coupled minority) and the interface (Task 3)

### §3.1 The trigger, grounded in C3
The step fires only on the **genuinely-coupled minority** — never every slice — per the contract C3 definition
(§6-C3 `[contract]`): a region where **(a)** the L3 key confidence is **below its bar** AND **(b)** the chord
decision is **sensitive to the carried key alternatives (a different carried key flips the chord reading).**

The two components map to concrete, source-grounded inputs — with the honest split C3 found:

- **(a) — key uncertain — a PRE-computed pre-filter.** Input: `HarmonicRegion.keyConfidence` (the D-L3a Class-M
  sequence margin, `harmonicrhythm.h:119` `[code]`) **< its bar** (the sequence-margin `uncertainThreshold`,
  default 1.0, `keymodesequence.h:147` `[code]` — precision-phase R5). This is the principled, per-region form
  of `decideJointKey`'s coarse `keyAmbiguous` proxy (near a modulation span, `jointkeydecision.cpp:293-296`
  `[code]`); the design uses the sequence margin, which is the D-L3a boundary confidence, not the demoted
  emission sigmoid.
- **(a′) — chord structurally ambiguous — a PRE-computed cheap pre-filter** (a proxy for (b), before the
  expensive re-decode): the L4 slice's `openQuestion.question != None` / `decision == Abstain` / low
  `SliceConfidence.composite` `[code]`, or `decideJointKey`'s `chordPinned == false` proxy
  (`jointkeydecision.cpp:292` `[code]`). Selects the candidate regions worth re-decoding.
- **(b) — the chord actually flips — computed BY the step's own per-key re-decode (§2.2).** This is the exact
  condition, and it is **not pre-computable read-only** — you can only know the winner flips under a carried key
  by *re-decoding under it*. This is precisely why C3 was found "un-computable read-only"
  (`cc_engage_c3_measurement_report.md` §2.3): (b) IS the owed build. In the engaged step it is computed on the
  pre-filtered (a)∧(a′) candidate set, and the step **commits a coupled (re-ranked) decision only where (b)
  holds** (the winner root differs across the carried keys); where (b) is false the re-decode agrees with the
  L3-argmax decode and the step passes through.

So the trigger is a **two-stage gate**: a cheap pre-filter `(a) ∧ (a′)` (from L3+L4 carry, region-level) selects
candidates; the per-key re-decode computes (b) exactly on those candidates; only `(a) ∧ (b)` commits a coupled
decision. The rest of the corpus is a pass-through (byte-identical decode). This is the proportionality property
(§1.1) made precise.

### §3.2 The interface to Part-1 L5 selection (#7)
The step's forward interface, both directions grounded in the built carries:

- **Reads (upstream):** L3's carried `keyAlternatives` + `keyConfidence` (`harmonicrhythm.h:118-119` `[code]`,
  the region-level candidate-key menu + boundary confidence, in-memory, no consumer yet — the step is the
  consumer, #12); and L4's per-key carry via the re-decode (§2.2), which **is** the L5-engagement §2 distinct-
  root carry, produced under each candidate key.
- **Emits (downstream, forward to L5):** per region, the **settled key `k*`** (possibly re-ranked from L3's
  argmax on the coupled minority; = L3's argmax on the majority), the **settled chord carry `c*`** (the distinct-
  root distribution under `k*`, incl. the exclusion tail #12), and the **Class-M joint-decision confidence**
  (§2.5). This is exactly the shape L5 Part-1 selection already consumes (L5 engagement §2/§3) — L5 reads the
  carry **as if L4 had decoded once under `k*`**; the joint step is transparent to L5's selection logic (it just
  settles which key that carry is under).
- **Acyclicity kept:** joint step → L5 is forward; **L5 never re-ranks the key** — that is the joint step's job,
  upstream of L5 (L5 engagement §4.1 "L5 selection reasons within a *fixed* region key" `[code]`). The joint step
  is the bounded box that fixes the key; L5 selects the function within it.

The F-B correction job (the net-harmful fine-grain override, settled to annotate-not-override, L5 engagement
§3.3) **re-homes here long-run**: the class-(b) coupled-correction it was mis-scoped to attempt (firing off the
C3 population by construction, `cc_engage_c3_measurement_report.md` §4.1 `[data]`) is exactly what a working
joint step performs *on the C3 population it is scoped to* — but that is a later inference-quality question (#8),
not this structural design.

---

## §4 — What must be BUILT (Task 4; the owed build, by layer — enumerated, not built)

The minimal build the step needs, each piece placed by layer (#7), each a completion/reuse of a built structure
(#6), none built in this pass (#8):

| # | Owed build | Layer / home | Reuse vs new (#6) |
|---|---|---|---|
| B1 | **The per-key chord re-decode entry** — a thin driver that invokes the existing `ChordSliceDecoder::decode` once per carried key and collects the per-key distinct-root carries (§2.2). | **Layer 4** (the decoder's caller) | **Reuse** — N forward calls of the built pure decoder; **no new decoder**. Prerequisite: the **distinct-root-preserving carry** (L5 engagement §2.3, owed at E4) so a root-flip is *visible* in the carry. |
| B2 | **The beam/coupling driver** — the joint score `J` (§2.4), the forward beam/Viterbi over joint states (§2.1/§2.4), the key-transition prior (§2.3), the settle + publish (§3.2), the Class-M joint confidence (§2.5). | **The joint step** (the L3/L4→L5 seam; the region orchestrator, where `decideJointKey`/`applyJointKeyWiring` sit) | **Generalize** `decideJointKey` config-B (§0): its lattice, Viterbi, transition prior, coupled flag, and couplingScore are reused; **NEW = the chord re-decode axis** (B1 wired into the beam) + the joint-margin confidence. **Not a parallel joint module** (#6). |
| B3 | **The trigger gate** — the two-stage `(a)∧(a′)` pre-filter (from L3+L4 carry) + the exact `(b)` from B1's re-decode (§3.1). | **The joint step's entry** | **Reuse** the built `keyConfidence` (a) and the L4 `openQuestion`/`composite` / `chordPinned` (a′) signals; (b) is B1's product. |
| B4 | **The production wiring** — replace J-key-iii's key-only override (which leaves the chord = R0, `regionanalyzer.cpp:388-395`) with the settle-and-publish of the completed (key,chord); L5 reads the settled carry. Behind a flag, held until ratified, exactly as J-key-iii is (`setJointKeyWiringEnabled`, `jointkeydecision.h:205-215` `[code]`). | **The region orchestrator** (`regionanalyzer.cpp`) + **L5 input** | **Complete** J-key-iii — its deferred chord axis is B1/B2; the named "faithful mechanism" is the engaged decoder (§2.2). |

**Layer summary (#7):** L3 — **no change** (the step *consumes* its already-built carry). L4 — a **thin per-key
driver** over the built decoder (B1); the distinct-root-preserving carry is its E4 prerequisite. The **joint step**
— a **generalization of `decideJointKey`** (B2/B3), the one home for the coupled decision. L5 — **no change to the
selection architecture** (Part 1); it reads the joint-settled carry (B4). The whole build is **forward-only and
bounded** (§1.3) and is **E4-adjacent** (it builds on the engaged decoder path, §2.2) — the earlier C3
measurement's "building the joint step is forbidden" was a *measurement*-dispatch boundary; this dispatch designs
that build, and the build itself remains a later, separately-ratified event (#8, #14).

---

## §5 — Facts owed / open questions (Task 5; #5 — owed measurements, not assumptions)

Every design point that rests on a fact we do not yet hold, flagged as an **owed measurement** with the read-only
instrument that would settle it — none assumed:

- **[owed-1] The true C3 trigger fire-rate.** `decideJointKey`'s `coupled` ~13.5% `[data]` is a **structural
  proxy** (`!chordPinned && keyAmbiguous`), **not** the exact `(a)∧(b)` condition. The true rate — regions where
  key-uncertain (sequence margin < bar) **and the winner root actually flips under a carried key** — is
  **un-measurable until B1 exists** (the C3 report's finding). **Instrument (post-B1):** a default-off dump over
  the per-key re-decode (the `--dump-fanout`/`--dump-joint-key` pattern) counting `(a)∧(b)` regions. Byte-
  identity-preserving, read-only.
- **[owed-2] The coupling benefit magnitude.** The research sets the expectation — **qualitative win on hard
  cases, low single-digit points overall** `[research]` §3 — but the magnitude on **our** corpus is unmeasured.
  **Instrument (post-B2):** the robust-stop sandwich (class-(b) root-disagree DURATION per preset,
  `a8_rebaseline_measure.py` → `robust_stop_diff.py`) restricted to the coupled regions, before/after the joint
  settle. The acceptance gate for the eventual build event is that the robust stop moves **favorably** (or at
  worst non-increasing) — assumed by no one, measured then.
- **[owed-3] The per-key winner flip-rate.** The chord *is* key-dependent in principle (§2.2), but **how often a
  carried key flips the winner root** is unmeasured. **Instrument (post-B1):** count winner-root disagreement
  across the carried keys per region. Determines whether the chord axis earns its keep.
- **[owed-4] Beam width / fixpoint depth.** Whether a single forward beam pass suffices, how many carried keys
  the beam must hold to catch the true key, and whether a bounded fixpoint (§2.4) ever adds anything over the
  beam — all unmeasured. **Instrument (post-B2):** beam-width ablation on the coupled set.
- **[owed-5] The chord→key coupling term under re-decode.** config-B's `couplingScore` today reads the *fixed*
  production chord's diatonic-ness; once the chord **re-decodes**, whether the coupling term should read the
  re-decoded chord-fit (§2.4) or keep the diatonic-ness form is an A/B, **post-build**.
- **[owed-6] All precision-phase constants** — the beam width W, the transition magnitude, the couplingBonus, the
  trigger bar, the joint-margin squash constant — are **Stage-5 fits** (contract §6 C1/C2), not set here (R5).

None of these is assumed; each is a declared owed measurement for the later build/measure events.

---

## §6 — What this Part settles, and the boundary honored

**Settles:** the joint step's **placement** — a **bounded coupling step** at the L3/L4→L5 seam (NOT a unified
hidden state), grounded against #7/#6/magnitude-realism and the acyclicity rule (§1); the **coupling mechanism** —
a **beam of (key, chord) hypotheses** with the **chord re-decoded under each carried key** (the owed axis, the
completion of `decideJointKey` config-B), a **reused key-transition prior**, a **declared additive composition**,
and a **declared Class-M joint-decision confidence**, all structure-only, constants precision-phase (§2); the
**trigger** grounded in C3 as a two-stage `(a)∧(a′)` pre-filter + exact `(b)` from the re-decode (§3.1), and the
**forward interface** to Part-1 L5 selection with acyclicity kept (§3.2); the **minimal owed build** specified by
layer (B1–B4) as a total-unification generalization of the built machinery, **enumerated not built** (§4); the
**owed measurements** flagged, not assumed (§5).

**The load-bearing architectural statement:** the joint step is the **completion of the chord axis
`decideJointKey`/J-key-iii deferred** — the "faithful mechanism" they named is the engaged `ChordSliceDecoder`'s
per-key re-decode. It is not a new machine; it is the built one, made bidirectional, gated on the coupled
minority.

**Boundary honored (#8 / R5 / #13).** No `src/` change, no build, no corpus write, **no constant fitted or
tuned** — the architecture is designed; the fitting and the build are later phases. Every claim is tagged to the
code / the contract / the research (#1); every fact not held is flagged as an owed measurement (#5), not assumed.
This designs no inference fix — where the joint step's recovery of the F-B corrections requires a
correctness-correlated coupled decision, that is a later inference-quality question (#8), not built here. No
placement re-introduces a cross-layer cycle (§1.3, #7).

*CC, 2026-07-07. Engage arc #10 — the joint key-and-chord step, architecture design (read-only, structure-only).
The biggest precision lever (#4), designed on the foundation Part 1 established and the machinery
`decideJointKey`/J-key-iii already built (#6). Both regression stops untouched/green (no `src/`, no build).
Fork-only; `upstream` untouched.*
