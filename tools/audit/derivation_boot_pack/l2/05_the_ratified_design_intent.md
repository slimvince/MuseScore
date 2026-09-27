# The ratified design intent — the entries this pack admits for this subject

This file is GENERATED. It carries the entries of the `DESIGN-INTENT` class of the rulings sort — the decisions the record sorts as ruled design intent rather than as management of the implementation — LESS the family withheld for this subject.

Four fields per entry and no others: the identifier, the title, the decision in the words it was decided in, and its plain restatement. Where a decision is recorded, what defends it, what its status came from and the words a search finds it by are all deliberately absent: each of those names a place or a fact in the implementation's own documents, which this pack does not carry.

Entries are in identifier order. An identifier missing from the run is not an error and is not a gap in the record: it is either outside this class or withheld for this subject, and this pack does not say which.

---

## D-032 — Every confidence crossing a layer boundary is in 0..1, class-declared, with its decision named

**As decided, in the words it was decided in:**

```
**The cross-layer confidence contract — every confidence that crosses a layer boundary is bounded,
class-declared, and named to its decision.** At a layer boundary — any value another layer may read — a
confidence is **in [0,1], class-declared (a ranking margin or a calibrated probability), and stated
```

**In plain words:** Inside a stage, a confidence can be on any scale. The moment another stage can read it, it must be a 0-to-1 number, labelled with what kind of confidence it is and what decision it belongs to.

---

## D-100 — Every derived fact is published exactly once, on the producing layer's output surface

**As decided, in the words it was decided in:**

```
**Every derived analytical fact is published exactly once, on the producing layer's output surface;
consumers read it and never re-derive it.** For **evidence-class** facts — hints a later design could
```

**In plain words:** Whatever a stage works out, it publishes on its own output surface; every later stage reads that instead of working it out again. Facts that are hints a later stage might one day use are published broadly even when nothing reads them yet, each carrying whether it has been established, because a consumer may not rely on an unestablished fact. What to do with a fact nobody reads is decided case by case: keep it with a named future reader stated, or remove it - and a reader outside the analysis counts.

---

## D-113 — Music-theory words are reserved for their music-theory meaning

**As decided, in the words it was decided in:**

```
Any term that coincides even slightly with music theory is used
  ONLY in its musical sense.
```

**In plain words:** In this project a score is a piece of music, a key is a tonality, and a measure is a bar. Where a word is needed in its everyday computing sense, it must be qualified - candidate score, map key, measurement.

---

## D-168 — #4 - the long-term goal is maximum-precision inference

**As decided, in the words it was decided in:**

```
4. **Long-term goal: maximum-precision inference.**
```

**In plain words:** The objective the whole project is measured against is getting the analysis as accurate as it can be made.

---

## D-170 — #6 - total unification: one path per concern

**As decided, in the words it was decided in:**

```
6. **Total unification — no duplication of any code.** One path per concern.
```

**In plain words:** There is exactly one implementation of any given concern. No duplicated code, no second place the same question is answered.

---

## D-171 — #7 - a layer is enhanced only with what belongs to it

**As decided, in the words it was decided in:**

```
7. **Adhere to layers.** Enhance a layer only with algorithms/methods that belong to it,
   nothing else. Worst case, this forces a layer redesign rather than a cross-layer patch.
```

**In plain words:** A stage of the analysis gets only the methods that are properly its own. If the right method does not belong there, the layers are redesigned rather than the method smuggled across.

---

## D-172 — #8 - no inference-problem-driven coding until the refactoring, the architectural design and the algorithmic completion are done

**As decided, in the words it was decided in:**

```
8. **No inference-problem-driven coding until the refactoring, the architectural design and the
   algorithmic completion are done.** Build-it-right comes BEFORE tune-precision, strictly. All
   three must be finished, not the last alone: every method and algorithm implemented in its
   correct layer, the architecture designed, and the refactoring carried out.
```

**In plain words:** Work is not steered by whichever analysis error is currently visible. Until the system is built right - the refactoring carried out, the architecture designed, and every method and algorithm finished in its correct layer - no fix is made because an analysis result is wrong. All three must be done, not the last alone.

---

## D-180 — #17 - the Premise Gate

**As decided, in the words it was decided in:**

```
17. **The Premise Gate.** Before any inference-affecting design is built or probed:
    (a) a **premise ledger** — every load-bearing causal claim explicitly labeled **FACT**
    (citation to code/measurement), **THEORY** (citation to published research answering the
    *specific* question, #2), or **ASSUMPTION**; (b) a **written quantitative prediction per
    assumption** (fire-rate, magnitude, direction, population) recorded *before* measuring —
    no prediction, no build; (c) a **desk simulation** — trace the mechanism by hand through
    the intended architecture on 3–5 real corpus cases drawn from the known failing sets,
    answering FIRST "does the mechanism FIRE on this case?" (control flow — ratified sharpening
    2026-07-10, the EG-2 desk-sim lesson), THEN "which term moves, by how much?" (arithmetic);
    (d) every **proxy→target
    link is itself a ledger premise** (a structural proxy never stands in for a behavioral
    quantity unvalidated); (e) every **insulation claim** ("X cannot affect Y") must enumerate
    the false-negative path explicitly; (f) **no hand-transcribed measurement numbers** —
    figures enter docs only via generated artifacts (the `manifest.json` pattern).
```

**In plain words:** Before anything that affects the analysis is built or even probed: every load-bearing causal claim is written down and labelled as an established fact, a published theory, or an assumption; every assumption gets a written numerical prediction BEFORE anything is measured; the mechanism is traced by hand through three to five real failing cases, asking first whether it fires at all and only then what it changes; any stand-in quantity must itself be justified; any claim that one thing cannot affect another must name how it could; and no number enters a document by being typed in by hand.

---

## D-182 — #19 - an unestablished measurement tool is forbidden (Class B)

**As decided, in the words it was decided in:**

```
19. **Unestablished instruments are FORBIDDEN (Class B).** An instrument, corpus, gate, or
    recorded figure is trusted only after being *positively established* (oracle cross-check,
    derivation of what the measurement unit actually measures, reproduce-check) — never
    because it is merely unfalsified.
    The objects of this principle are the four it names and no others — a measurement tool, a
    corpus, a gate, a recorded figure — and each is an inspectable, re-runnable artifact,
    because each of the three establishment methods named here requires one. A session, a
    person or a conversation is never the object of a Class B demand.
```

**In plain words:** A measuring script, a corpus, a gate or a recorded figure is trusted only once it has been positively shown to be right - checked against an independent oracle, with a derivation of what its unit actually measures, and a reproduce-check. Never merely because nothing has contradicted it.

---

## D-185 — #22 - every hard gate declares in advance how it handles the largest change it will meet

**As decided, in the words it was decided in:**

```
22. **Every hard gate carries a pre-declared protocol for the largest change it will face.**
    A gate written only for incremental change must not be amended under the pressure of a
    live diff — the exceptional-event variant (e.g. architecture-scale adoption: aggregate
    criterion + explained diff + snapshot + ratification) is written and ratified before such
    a change is on the table.
```

**In plain words:** A rule that decides whether a change may ship must say, before the fact, what it does when the change is far bigger than the incremental ones it was written for. It must never be rewritten while such a change is sitting in front of it.

---

## D-201 — Very large scores must be handled, and are expected to be more common than our corpora

**As decided, in the words it was decided in:**

```
**Very large scores MUST be handled, and are expected to be a MORE COMMON use than our corpora.** A
Wagner act or a symphony has to produce an analysis; the user expects such music to be a more common
```

**In plain words:** A Wagner act or a symphony must work. The user expects such scores to be a more common use than the chorales the system was fitted on. This is a standing requirement every later design is judged against, not a defect report.

---

## D-205 — A human acts as ground truth where no formal ground truth exists

**As decided, in the words it was decided in:**

```
**A HUMAN acts as ground truth where no formal ground truth exists (user-decided 2026-07-13).** For
repertoire nobody has published an analysis of, the reference answer is a person's judgment. That person
may reach it by any method they choose, **including** letting an automated triage judge point them at the
```

**In plain words:** For music nobody has published an analysis of, the reference answer is a person's judgment. They may reach it however they like, including by letting an automated judge point them at the passages most likely to be wrong. That judge is guidance for the human, never a grader and never a number we report.

---

## D-262 — The extension increment is chosen by the requesting layer, not by the layer that supplies the notes

**As decided, in the words it was decided in:**

```
   layer; it is not fixed and not Architectural Layer 1's to decide.** Architectural Layer 1 is domain-blind, and no
   single size fits every layer (Architectural Layer 3 probes at phrase/measure scale, Architectural Layer 4 at
   harmony/slice scale), so the requester sets it to **its own natural inference scale** — the smallest step that
   could plausibly change its output (knowledge, not a guess). It is an **efficiency knob only**: a larger increment
   means fewer round-trips (and perhaps a slightly larger final loaded span), never a different answer, because
   convergence (item 6) fixes the result. Mechanically this is forced — the requester owns the *extend → re-infer →
   re-check* loop, and Architectural Layer 1's *extend* executes **exactly the one requested step and never evaluates
   convergence** (that would be inference, which it does not do), so the increment can only be a per-call parameter
   from the requester.
```

**In plain words:** How much music to load per extension step is set by the layer asking for it, in its own natural inference scale, because the note supplier is domain-blind and no single step size fits every layer. The increment is an efficiency knob only - a larger step means fewer round trips, never a different answer, because convergence fixes the result.

---

## D-264 — Extension is an optimisation of load-more-then-rerun: any sequence of extensions equals one fresh run

**As decided, in the words it was decided in:**

```
- **Equivalence invariant (the correctness guard).** The result after **any** sequence of extensions must equal a
  **single fresh run over the final loaded span** — extension is an optimisation of *"load more, then run from
  scratch,"* never a different computation. In practice the forward cascade is **bounded**: the new context changes
  inference only where it actually reaches (a carried-in key affects the leading-edge slices and decays inward), so
  only the affected slices re-infer — the same locality that makes the stop condition terminate, and which composes
  with the existing *"re-analyse a sub-range"* capability.
```

**In plain words:** The result after any sequence of extensions must equal a single fresh run over the final loaded span. Extension exists to avoid recomputing from scratch; it is never allowed to be a different computation, and the analysis must not depend on how many steps reached a given span.

---

## D-267 — There are exactly two admissible confidence classes, and no layer may claim a calibrated probability until one is fitted

**As decided, in the words it was decided in:**

```
Every published confidence declares exactly one **class**:

- **Class M — decision margin.** "How much better is the chosen reading than the best *different* reading, under this
  layer's own scoring?" A margin is a **rank statement**, not a probability. Raw margins are unbounded and
  scorer-scale-dependent, so a Class-M confidence is published only **squashed to [0,1]** by a fixed monotone map
  (the map's constants are precision-phase; the map itself is declared per layer). Class M is what every layer can
  compute today.
- **Class P — calibrated probability.** "With what empirical frequency is a decision at this confidence correct,
  measured against ground truth?" Class P is the **Stage-5 target**: a fitted reliability map per (layer × decision
  type) converts the Class-M value into Class P. Until fitted, no layer may claim Class P.
```

**In plain words:** Every published confidence declares one of two classes. A decision margin says how much better the chosen reading is than the best different one under that layer's own scoring - a rank statement, not a probability, published only after being squashed into the zero-to-one range. A calibrated probability says with what measured frequency a decision at this confidence is correct; it is the later target, and until its reliability map is fitted no layer may claim it.

---

## D-292 — The fitting-pool licence constraint - values that ship are fitted only on freely-licensed music

**As decided, in the words it was decided in:**

```
> **(e) A value that SHIPS may be fitted only on freely-licensed music.** The pool a ship-intended weight or
> table is estimated on is restricted to public-domain, CC0 and CC-BY sources. Music carrying a
> non-commercial licence or no stated licence — the record names the DCML corpora, MCMA and Essen — may be
```

**In plain words:** Any number that is fitted and then shipped may be fitted only on public-domain or permissively-licensed music. Music under a non-commercial or unstated licence may be used to check and validate, never to fit a shipped value.

---

## D-313 — A confidence map is monotone or it is not fitted — a non-monotone curve is an upstream finding, not a mapping target

**As decided, in the words it was decided in:**

```
**D-8 Calibration maps are monotone or deferred.** A non-monotone empirical curve (L5 combinedBoundary) is
an upstream finding, not a mapping target — fitting a non-monotone map would launder an inference defect
into the confidence semantics. (Contract R4/R5 monotonicity carries this.)
```

**In plain words:** Turning a layer's internal confidence number into a statement about how often it is right is only done when a higher number really does mean more often right. Where the measured curve goes the wrong way in places, that is reported as a fault in the layer, not smoothed over by the map.

---

## D-365 — A corpus search driven by the SUM of all needs is worth running, but it is step 3 of 3 — the needs list and the re-scoring of what is already enumerated come first

**As decided, in the words it was decided in:**

```
**The question that created this section:** is a corpus search useful that is NOT driven by one architectural
need — the "need" being the sum of all needs? **Answer: yes, but the search is step 3 of 3.** The sum of all
needs must first exist as an artifact, and once it does, re-scoring the EXISTING enumeration against it is
cheaper and likely higher-yield than new searching (the Wave-2 lesson: the finds were already inside enumerated
containers — the dismissals were purpose-relative, made with harmonic-axis eyes only).
```

**In plain words:** Searching against everything the project needs at once is useful, but only after two cheaper steps. First the full list of needs has to exist as a written artifact. Then every collection already enumerated is re-scored against that list, without searching at all. Only what is still uncovered afterwards is searched for.

---

## D-419 — Until the recognition consumer is built, the function layer does not touch the harmonic vocabulary

**As decided, in the words it was decided in:**

```
- **Until the RECOGNITION CONSUMER is built, the function layer does not touch this vocabulary —
  and the connection is absent, not partial.** The consumer is the separate, named piece of work
  that makes this catalog the function layer's multi-chord disambiguation prior and the grouping
  layer's sequence-span annotation; it is also where the §6.7 idioms first do any work, by
  weighting which entries count. Until it exists the function layer makes **no** use of the catalog
  at all. *Why:* it follows from the ratified build order — vocabulary, then the grouping layer,
  then wire the consumer — and from this component's own contract that it supplies **ranked
  candidates and decides nothing**: with no consumer there is nothing to receive the candidates, so
  a partial connection would be a consumer built by accident and unratified. This is the
  declared-dormancy form the fact-publication corollary requires: the component is published with
  its future consumer **named**, rather than left to look like waste.
```

**In plain words:** The reference catalog of named progressions and the function layer are connected by a separate piece of work that has not been built. Until it is, the function layer makes no use of the catalog at all — it is not a partial or optional connection, it is absent. That piece is also where the five idioms first do any work, by weighting which catalog entries count.

---

## D-442 — A validation failure goes back to the language model as a tool-call error and is never shown to the user

**As decided, in the words it was decided in:**

```
Violations are fed back to the LLM as tool call errors, not shown to the user.
The LLM corrects and retries. Only clean output reaches the score.
```

**In plain words:** When the checks reject something the model proposed — a note outside an instrument's range, parallel fifths, a malformed bar — the rejection is returned to the model, which corrects itself and tries again. The user never sees the rejected attempt; only output that passed the checks reaches the music.

---

## D-447 — The model's tool definitions are generated from the operation set, never maintained by hand

**As decided, in the words it was decided in:**

```
Tool definitions for the LLM are generated automatically from the operation
set schemas. Adding a new operation to the operation set automatically makes
it available as an LLM tool. No manual maintenance.
```

**In plain words:** What the model is told it can do is derived from the operations themselves. Adding an operation makes it available to the model with no second list to keep in step.

---

## D-454 — The grouping layer detects nothing — it assembles what earlier layers decided, and pressure to add detection means the work belongs elsewhere

**As decided, in the words it was decided in:**

```
Layer 6 defines **no detection of its own**: it assembles §5.1–§5.3 (punctuation-span segmentation, key-area grouping,
cadence alignment) and hosts the **read-through carries** — §5.4 the Layer-5 residual and §5.5 the consumer's schema
annotations, both carried verbatim, neither *detected* here. There is no additional *detection* rule and no hierarchy.
Pressure to add detection is a signal to check whether the work belongs in an **earlier** layer (a detection that should be
a primitive) or is an **out-of-scope extension** (§9-D3) — not a new Layer-6 mechanism.
```

**In plain words:** The grouping stage adds no detector of its own. It puts together the boundaries, cadences, keys and unresolved marks the earlier stages produced. If it starts to feel as though grouping needs to detect something, that is a sign the work belongs to an earlier stage or is out of scope — not that grouping needs a new mechanism.

---

## D-455 — A cadence away from a grouping boundary is surfaced as internal, never snapped to the nearest boundary and never discarded

**As decided, in the words it was decided in:**

```
- **D4 — Cadences align to punctuation-spans, asymmetrically; an off-boundary cadence is surfaced, not snapped (§5.3).**
  *Rejected:* forcing every punctuation-span to end with a cadence (contradicts the ground truth) and snapping a stray
  cadence to the nearest boundary (hides a real tension signal and would be a covert upstream override).
```

**In plain words:** A cadence usually lands where a grouping span ends, but a span may end with no cadence at all, so the relation runs one way only. A cadence that lands nowhere near a boundary is marked as falling inside a span and shown as such. It is not dragged to the nearest boundary and it is not thrown away.

---

## D-456 — Sections, periods and sentences are out of the grouping layer's core for PROPORTIONALITY — not disqualified for lacking an oracle

**As decided, in the words it was decided in:**

```
- **D3 — Sections / periods / sentences are out of L6's *core* for PROPORTIONALITY — NOT disqualified for lack of an
  oracle (user-ratified verifiability contract, 2026-06-29).** They are sound theory and *do* lack an oracle in our
  corpus, but the contract is explicit that **lack of ground truth is not a disqualifier.** They stay out of the thin core
  because L6 is the *flat-grouping assembly* layer and forms/sections are a larger, *higher*-layer structure — and they are
  **buildable via a chosen alternative-confidence path** (a form-annotated corpus, or theory-rules-as-oracle) with an
  "empirically-unvalidated" mark, when a need arises. The core is punctuation-spans + key-areas + cadence alignment + the
  hosted schema spans.
```

**In plain words:** Larger formal structures — sections, periods, sentences — are left out of the grouping stage's core because that stage assembles the flat grouping and formal structure is a bigger thing belonging higher up. They are NOT rejected for being uncheckable against our annotated music: the standing contract says that alone never disqualifies sound theory. They may be built when a need arises, with a chosen way of gaining confidence in them and an explicit mark that they are empirically unchecked.

---

## D-457 — A group truncated by the selection edge is marked as truncated, and a group that runs off the edge unclosed carries an extension cue the grouping layer only surfaces

**As decided, in the words it was decided in:**

```
An edge group whose opening/closing tick is the **selection edge rather than a musical boundary** carries the provenance
`clipped-by-selection-edge` (the same principle as the §3 marker-scope provenance and L2's artificial-clip-boundary
distinction) — a truncated group is never presented as a complete one; the same mark applies to an edge **key-area**
(§5.2). And an edge span that reaches the selection edge with **no closing boundary and no cadence** is surfaced with an
`extension-cue` tag — the signal that widening the selection would complete it. Per the forward-only contract L6 only
**surfaces** the cue (like the §5.3 internal-cadence tension tag); acting on it — invoking L1's `extend` and re-running —
is the decision of the **orchestrator** (the pipeline driver that sequences the layers — the region analyzer of the
bounded-context contract, `cowork_bounded_context_design.md` §6) under the §2.15 bounded-context contract (stop
condition + hard bound), never L6's.
```

**In plain words:** When a group begins or ends only because the user's selection stops there, it is marked as clipped by the selection edge, so a cut-off group is never presented as a complete one; the same mark applies to a key area at the edge. When a group reaches the edge with neither a closing boundary nor a cadence, it carries a cue saying that widening the selection would complete it. The grouping stage only shows the cue — deciding to act on it, by asking for more music and re-running, belongs to whatever drives the pipeline.

---

## D-459 — The key-area confidence is a declared margin-class boundary confidence, and its input is the declared key confidence — never the grading diagnostics' sigmoid

**As decided, in the words it was decided in:**

```
*(Contract compliance, added at sign-off review 2026-07-02: any confidence L6 publishes — the key-area
confidence, a span-level aggregate — is a **boundary confidence under the cross-layer confidence contract**
(`cowork_confidence_contract.md` U2): [0,1], declared in the contract's **Class M** (a margin-family quantity, not a
calibrated probability), with its combiner and inputs named; and its **input** is
each unit's DECLARED boundary key confidence per that contract — i.e. once the **D-L3a close-out** (the Layer-3
boundary-confidence declaration item of `cowork_confidence_contract.md` §3) lands, the one declared
L3/L5 number, not the **diagnostic sigmoid** (the Layer-3 emission-scale confidence squash used by the grading
diagnostics, named in the Layer-3 spec banner as the C1 fidelity fix).)*
```

**In plain words:** The confidence the grouping stage publishes for a key area is a quantity crossing a stage boundary, so it obeys the cross-layer confidence rules: it sits between zero and one, it is declared as a margin rather than a calibrated probability, and it names how it was combined and from what. What it is combined FROM is the declared key confidence, not the squashed number the grading diagnostics use.

---

## D-460 — A group counts as fully resolved exactly when no unit in it carries an unresolved mark — no confidence threshold enters the test

**As decided, in the words it was decided in:**

```
A Layer-5 open mark on a unit is surfaced on the punctuation-span and key-area that contain that unit (the group is
reported as carrying an unresolved reading at that location). L6 **never** resolves an open mark — it has no evidence Layer
5 lacked. A punctuation-span composed entirely of units carrying **no open mark** (that is the whole test — no
confidence threshold is involved) is reported as fully resolved; one containing an
open mark is reported with the residual visible.
```

**In plain words:** Where an earlier stage left a reading unresolved, that mark is shown on the group and the key area containing it. The grouping stage never resolves it — it has no evidence the earlier stage lacked. A group is reported as fully resolved when, and only when, none of its units carries such a mark; no confidence number is consulted.

---

## D-461 — The grouping layer is an explainability layer, not an accuracy requirement, and is deliberately kept thin

**As decided, in the words it was decided in:**

```
- **Proportionality.** The SOTA reaches competitive Roman-numeral accuracy with **no** explicit grouping layer (grouping
  falls out of stable key runs — `contrapunctus_findings.md`). L6 is a deliberate **explainability** layer, not an
  accuracy requirement; it stays the thin assembly layer specified here and does not grow detection of its own.
```

**In plain words:** The best published systems reach competitive Roman-numeral accuracy with no grouping stage at all — grouping falls out of stable key runs. Ours exists to make the analysis explainable, not to make it more accurate, and it is held to the thin assembly job on that basis.

---

## D-462 — Cadence validation is scoped to LOCATION; cadence TYPE is only partially attributable and is never a clean gate

**As decided, in the words it was decided in:**

```
- **Cadence alignment → the DCML-TSV `|cadence` oracle, scoped to LOCATION** (robust to Roman-numeral errors; cadence
  *type* is harmony-dependent and only partially attributable on the harder repertoire — measured, caveated, not a clean
  gate).
```

**In plain words:** Cadences are checked against the annotated corpus for WHERE they fall, because that check survives a wrong Roman numeral. WHAT KIND of cadence it is depends on the harmony being right, so on the harder repertoire that can only partly be attributed — it is measured and reported with that caveat, and it never becomes a pass-or-fail gate.

---

## D-464 — No further progression-level signal may be added to the single-step look-around structure; it goes in the progression context instead

**As decided, in the words it was decided in:**

```
- **No further PROGRESSION-LEVEL signal may be added to the single-step look-around structure; a
  progression-level signal goes into the progression-level structure directly.** The struct
  specified above is a one-step look-around — the immediate previous and next harmonic positions.
  Four fields describing the previous winner's competition outcome were added to it that belong to
  the planned progression-level structure instead; **nothing further of that kind goes in**, and
  the migration of those four is planned **explicitly** when the progression analyzer's design
  begins, not left to happen. *Why:* stated with the recommendation and grounded in this
  document's own instruction that the two structures are kept distinct — the finding is that one
  had been growing into the other with no migration plan written down, which is how a boundary
  disappears without a decision.
```

**In plain words:** The structure that carries a chord's immediate neighbours was designed as a one-step look-around, and four fields describing the previous winner's competition outcome were added to it that belong to a planned progression-level structure instead. Nothing further of that kind goes in, and the migration of the four is to be planned explicitly when the progression analyzer's design begins.

---

## D-507 — A catalog entry defined by its melodic or bass lines is recognised by its chord skeleton alone and carries a 'chords-only' mark, with its prior strength reduced

**As decided, in the words it was decided in:**

```
- **D7 — line-defined entries carry the "chords-only" mark** (§4.5) — the verifiability contract's explicit-mark
  path; the mark retires per entry when the voice-leading layer supplies the other half.
```

**In plain words:** Some named patterns are defined by their melody and bass lines as much as by their chords. This consumer can only see the chords, so it recognises such a pattern by its chord skeleton, marks the recognition as chords-only, and trusts it less. The mark comes off, per entry, when the voice-leading work supplies the other half.

---

## D-514 — A newly acquired annotation set whose works OVERLAP the regression corpus is RECORD-ONLY: it may not be wired to, compared against, or bulk-diffed with the gate corpus without a user ruling

**As decided, in the words it was decided in:**

```
**★ AND THE SAME RULE READ FORWARD IN TIME, FOR MATERIAL THAT ARRIVES AFTER THE GATE CORPUS ALREADY EXISTS: A NEWLY
ACQUIRED ANNOTATION SET WHOSE WORKS OVERLAP THE REGRESSION CORPUS IS RECORD-ONLY.** It is cloned, pinned and
enumerated like any other acquisition, and over the overlapping works it may **not** be wired to the analysis,
**not** be compared against the gate corpus, and **not** be bulk-diffed with it. **Any use of it over those works is
a USER RULING**, taken deliberately; a session does not take it. Whatever portion of such a set covers OTHER
repertoire is outside the gate and is unaffected. *Why:* it is the dedupe rule above with time added — a work that is
IN the regression corpus cannot also be a free-standing check ON it, because the two uses are not independent, which
is the contamination lesson this section already generalizes. The recorded instance that produced the rule is a
chorale annotation set whose Bach half re-encodes the gate repertoire while its remaining half does not.
```

**In plain words:** One acquired collection of chorale analyses covers the same works the accuracy gate is measured on. It is recorded and left alone: it may not be connected to the analysis, compared against the gate corpus, or diffed against it in bulk. Using it over those pieces at all is a decision for the user. Whatever portion of it covers other repertoire is outside the gate and unaffected.

---

## D-516 — Two ground-truth classes with named consumers but no needs row were ADOPTED at the first full-needs audit — contrapuntal/imitative structure, and marked part-writing errors

**As decided, in the words it was decided in:**

```
**C. Rulings sought from the user — ★ ALL RULED (2026-07-04, see status banner):**
1. Adopt **N18** (contrapuntal/imitative structure GT)? Candidates already enumerated. → **ADOPTED.**
2. Adopt **N19** (part-writing error/exercise GT)? Would join the union search. → **ADOPTED.**
```

**In plain words:** Scanning the list of things the project intends to build against the list of ground truth it tracks turned up two kinds of annotation that a named future tool needs and nothing was tracking: analyses of fugal and imitative structure, and graded exercises with their mistakes marked.

---

## D-522 — Explaining an inference to the end user is a late-bound DISPLAY consumer of facts that already exist — not a new analysis

**As decided, in the words it was decided in:**

```
**Explainability (user, 2026-07-13): the end user may want to know HOW a mode, chord,
or function was inferred.** If the evidence trail behind every inference is published
— which pitch classes drove the key, which cadence vote confirmed the modulation,
which margin separated the winner from the runner-up, why the analyzer abstained —
then "show me why" is a late-bound DISPLAY consumer of facts that already exist, not
a new analysis. Much of the raw material exists today as internal diagnostics (the
chord-diagnosis replay, the dormant function machinery's structured open marks and
ambiguity kinds, the ranked-candidates-plus-margins confidence contract); the gap is
publication, which is wave 3's job anyway. A register row for the feature follows at
the next free number (numbers are in flight in the current CC session).
```

**In plain words:** If the evidence behind each inference is published — which pitch classes drove the key, which cadence confirmed the change, how far ahead the winner was, why the analyzer declined to decide — then answering 'show me why' is a matter of displaying what is already there, not of analysing anything again.

---

## D-538 — A multi-signal scoring change lands one signal at a time, with the corpus check re-run after each step and any increase in errors a hard stop before the next

**As decided, in the words it was decided in:**

```
## Four-step implementation and validation order

Run corpus check after each step. Each step must not increase total BIR errors before
proceeding.
```

**In plain words:** The change was not landed as a whole. Each new signal was added on its own, the corpus was re-measured, and the next signal was only added if the error count had not risen.

---

## D-542 — Idiom discovery runs DISCOVER-THEN-NAME: structure is learned on a low-level encoding carrying no theory or genre labels, and theory features and genre labels are interpretation lenses applied afterwards, never clustering input

**As decided, in the words it was decided in:**

```
- **The governing order is DISCOVER, THEN NAME.** Structure is learned on a **low-level encoding
  carrying no theory and no genre labels**; only afterwards is the emergent structure held up
  against theory features **and** genre labels, both as **interpretation lenses, never as
  clustering input**. *Why:* stated as a refusal rather than a preference — there is no
  zero-prejudice method, so the discipline is to push the unavoidable priors down to the lowest,
  most theory-neutral level and interpret afterwards, never to pretend they are absent. Feeding
  theory features in could only rediscover the priors already encoded, which is the alternative the
  design rejects by name.
```

**In plain words:** The grouping of music into harmonic idioms is learned from a plain, label-free encoding of the notes and chords. Only afterwards is the result held up against theory terms and against genre labels to see what the emergent groups correspond to. Neither is ever fed in.

---

## D-543 — The encoding is key-normalised tonal-pitch-class TRANSITIONS — spelled where spelling is reliable, mod-12 only where it is genuinely absent — run as two complementary views

**As decided, in the words it was decided in:**

```
- **The encoding is KEY-NORMALIZED TONAL-PITCH-CLASS TRANSITIONS — spelled where spelling is
  reliable, plain pitch classes only where no spelling exists — run as TWO complementary views.**
  Every piece is transposed to a common tonic and encoded as chord-to-chord moves, using the
  written note names wherever the source spells them (classical scores and trusted lead-sheet
  symbols); a second, order-free vocabulary view of the same material runs alongside as a
  cross-check. *Why:* grounded in the prior art the design adopts — the line-of-fifths encoding is
  what made the published topics interpretable, and it stays low-prejudice because it is the raw
  written note rather than a functional label. Three alternatives are rejected with their reasons:
  high-level functional features prejudge the answer; audio or raw performance data lets timbre and
  instrumentation swamp harmony; bare pitch classes everywhere discard the very structure that made
  the published result readable.
```

**In plain words:** Pieces are encoded as sequences of chord-to-chord moves with every piece transposed to a common tonic, using the written note names wherever the source spells them. Where no spelling exists at all, plain pitch classes are used. A second, order-free view of the same material runs alongside as a cross-check.

---

## D-544 — Confound control is a FIRST-CLASS GATE, and the source-leakage test decides validity: if the clusters are explained by which corpus a piece came from, the result is bookkeeping and not idiom

**As decided, in the words it was decided in:**

```
- **Confound control is a FIRST-CLASS VALIDITY GATE, and the source-leakage test decides
  validity.** The dominant failure mode of this kind of study is discovering **which corpus a piece
  came from**, what key it is in, how long it is, its instrumentation or its encoding quirks —
  before it ever reaches idiom. So the controls are mandatory and matched to it one by one:
  key-normalize, length-normalize, balance and stratify sources, de-duplicate, exclude melody-only
  sources, audit extraction noise on a labelled subset. **The source-leakage test is mandatory:**
  hold out the source label and test whether the clusters are explained by source, key or length.
  **If the clusters approximate the source, the study found bookkeeping and not idiom** — back to
  the encoding. A discovered structure earns the word *idiom* only after surviving these. *Why:*
  stated as a gate rather than a footnote precisely because the alternative — naive clustering —
  finds bookkeeping and calls it style; it is #19 in the discovery setting, where a cluster set is
  trusted after being positively established against the confound and never because nothing has
  contradicted it.
```

**In plain words:** The dominant way this kind of study fails is by discovering which collection a piece came from, or what key it is in, or how long it is, and calling that a style. So the source label is held out and the clusters are tested against it. If they are explained by it, the encoding goes back to the drawing board. A discovered structure earns the word idiom only after surviving this.

---

## D-545 — The uniform mechanical extractor for idiom discovery is the external library, stopping at the note-and-slice front — OUR OWN key/chord/function inference must NEVER touch the extraction

**As decided, in the words it was decided in:**

```
- **The uniform mechanical extractor is the EXTERNAL library, and extraction stops at the
  note-and-slice front: OUR OWN key/chord/function inference never touches it.** One external tool
  (music21) is applied identically to every source, and only as far as reading notes and cutting
  them into simultaneities; our own analyzer is deliberately not used for the extraction, and its
  trust is **banked rather than assumed** — a shared subset is run through both and the streams
  compared. *Why:* chosen against our own cleaner slicer for a stated reason that is the study's
  own validity — our slicer cannot ingest every corpus format, so using it would force a **mix** of
  extractors correlated with source, which is exactly the confound the gate above forbids. Using
  the full analyzer would be worse: it is tuned on one repertoire, it would rediscover our own
  priors, and it would inject genre-correlated error into a study about whether the grouping is
  genre. The distinction the rule rests on is stated with it — reading notes and slicing them is
  mechanical, so an error there is a bug rather than a misinference, while everything above is
  inference and would carry our priors. *Mechanical* means unbiased, not clean: the raw
  simultaneities still contain passing tones, which is correct output.
```

**In plain words:** Turning every corpus into chords for this study is done by one external library applied identically to every source, and only as far as reading notes and cutting them into simultaneities. Our own analyzer is deliberately not used for it.

---

## D-614 — Every real difficulty-grade label source is research-only or proprietary at origin — a commercial grading feature needs a licence path or its own labels

**As decided, in the words it was decided in:**

```
**★ AND THE DIFFICULTY-GRADE CASE IS A DIFFERENT PROHIBITION FROM THE FOUR BULLETS ABOVE, STATED APART SO IT IS NOT
READ AS THE SAME ONE.** Those restrict the pool a **shipped FITTED VALUE** may be estimated on. This restricts a
shipped **FEATURE** whose labels are somebody else's property. **Every real difficulty-grade label source is
research-only or proprietary AT ORIGIN:** no machine-readable exam-syllabus dump exists in any form, the open sets
carry no licence file at all, the gated one is request-access and research-use-only, and the largest carries a
free-licence badge over research-use-only text. **So a COMMERCIAL grading feature needs a licence path or labels of
our own** — the held material is enough to validate the idea as research and is not enough to ship it. *Why it is
stated here and not only where it was found:* this is the section a fitter or a feature design reads before declaring
its pool, and a designer who meets the fitted-value rule must also meet the case where the constraint bites on the
feature instead.
```

**In plain words:** Every collection that says how hard a piece is to play is either restricted to research use or belongs to somebody who sells it. So a difficulty feature in a shipped product would need either a licence agreement or labels of our own; the held material is enough to check the idea works and not enough to ship it.

---

## D-623 — A selection-aware capability is a PARAMETER on the one orchestrator, never a sibling — the capability must not duplicate the orchestration

**As decided, in the words it was decided in:**

```
**A selection-aware capability is a PARAMETER on the one orchestrator, never a sibling (D-623;
re-homed into this specification 2026-08-04, from the same document as D-624).** The capability was built as an option on the existing
driver rather than as a second driver beside it, so there remains **one** path that builds the note
model, slices it and decodes — the seam specified below. The option is off by default, so shipped
behaviour and every measurement are unchanged. *Why:* it is one-path-per-concern applied to
orchestration — a second driver would be a second place where build, slice and decode are sequenced,
and the two would drift. Both admissible forms were stated, and the build's choice was gated on
byte-identity plus an explicit unification ledger, so the resolution is evidenced rather than asserted.
```

**In plain words:** A new way of driving the analysis over part of a score was built as an option on the existing driver rather than as a second driver beside it, so there is still one path that builds the note model, cuts it into slices and decodes them. The option is off by default, so the shipped behaviour and every measurement are unchanged.

---

## D-660 — A research-tied name is not renamed but is governed by a two-tier rule, and the terminology cleanup runs in a fixed order with no tree-wide rename

**As decided, in the words it was decided in:**

```
**★ WHAT HAPPENS TO A NAME BORROWED FROM THE PUBLISHED RESEARCH, AND IN WHAT ORDER THE CLEANUP
  RUNS (user-ruled 2026-08-09; the ruling record is `records/cowork/rulings/cowork_rulings_2026_08_09_fifth_stop.md`,
  Ruling 30).** The block above says the existing tree is not renamed unilaterally and that the
  pass is a decision surface rather than a sweep. It does not say what a session does with a term
  that carries correspondence to the research the design is grounded in, and it does not fix the
  order — both are settled here. **A RESEARCH-TIED NAME IS NOT RENAMED (#1/#2), AND IS GOVERNED BY
  TWO TIERS.** *(i)* At the **INTRODUCTION SITE** — where the public research is actually
  discussed, which is expected to be one or very few places — the collision is EXPLAINED and our
  decided synonym STATED; the term standing there with that statement is conformant. *(ii)* **Every
  subsequent use** of the research term outside our own vocabulary carries a **compact inline
  annotation referencing the research**; such a use is conformant if and only if it is annotated,
  and an **unannotated repeat use is a flag**.
```

**In plain words:** A term borrowed from the published research that collides with this project's vocabulary is not renamed. Instead: where the research is actually discussed, the collision is explained and our own synonym stated; and every later use of the borrowed term outside our vocabulary carries a short inline note pointing at the research, so an unannotated repeat use is a flag. The wider terminology cleanup runs in a fixed order — the derived inventory first, then per-word batches the user rules, governing surfaces first — and there is no tree-wide rename.

---
