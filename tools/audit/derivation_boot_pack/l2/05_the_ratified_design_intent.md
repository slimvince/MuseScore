# The ratified design intent — the entries this pack admits for this subject

This file is GENERATED. It carries the entries of the `DESIGN-INTENT` class of the rulings sort — the decisions the record sorts as ruled design intent rather than as management of the implementation — LESS the family withheld for this subject.

Four fields per entry and no others: the identifier, the title, the decision in the words it was decided in, and its plain restatement. Where a decision is recorded, what defends it, what its status came from and the words a search finds it by are all deliberately absent: each of those names a place or a fact in the implementation's own documents, which this pack does not carry.

Entries are in identifier order. An identifier missing from the run is not an error and is not a gap in the record: it is either outside this class or withheld for this subject, and this pack does not say which.

---

## D-002 — The fitted tables and weights are compiled into the binary verbatim

**As decided, in the words it was decided in:**

```
compiles the five committed artifacts + the selected weight vector
> VERBATIM (JSON bytes, not a parsed-structure codegen) into the generated `jointembeddedartifacts.{h,cpp}`
```

**In plain words:** The numbers the estimator was trained on are built into the program at compile time rather than read from disk at run time, so a running copy cannot quietly disagree with the numbers we published.

---

## D-028 — The span typology - every layer names the span it operates on; bare 'region' is banned

**As decided, in the words it was decided in:**

```
"Region" unqualified is **banned** as
  ambiguous; every layer names the span it operates on.
```

**In plain words:** The word 'region' on its own is forbidden, because it hides which kind of stretch is meant. Each stretch has its own name: the chord-span, the key-span, the punctuation-span and so on.

---

## D-029 — The verifiability contract

**As decided, in the words it was decided in:**

```
prefer what we can verify against ground truth (it is how we catch our own theory
  errors); for sound theory we cannot verify against the current corpus, build it with an explicit
  **alternative-confidence path** *and* an **"empirically-unvalidated" mark**, rather than refusing it
```

**In plain words:** Prefer what we can check against annotated music. Where the theory is sound but we have nothing to check it against, build it anyway - but mark it as unchecked and give it its own confidence path.

---

## D-030 — Bounded context - cost scales with the working span, not the whole score

**As decided, in the words it was decided in:**

```
The binding scale requirements: **(R1)** cost scales with the working span, not the whole
  score; **(R2)**
  re-analysis is incremental over the dirty span plus a bounded margin; **(R3)** the working span is **extensible**
```

**In plain words:** Analysis runs on what the user has selected. The work must grow with the size of that selection, not with the size of the piece; re-analysis after an edit must only redo the changed part; and a layer that needs more music asks for it rather than reading everything.

---

## D-031 — Whole-score analysis is the degenerate case, not the design

**As decided, in the words it was decided in:**

```
Whole-score analysis is the degenerate case (selection = score).
```

**In plain words:** Analysing the whole piece is what happens when the user has selected the whole piece. It is not the normal mode of operation.

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

## D-034 — A new layer or axis is admitted only through three co-equal gates

**As decided, in the words it was decided in:**

```
**A new layer or axis is admitted only when it clears three co-equal gates,
  all required:**
```

**In plain words:** A new stage is added only if it carries one distinct responsibility, can be validated somehow, and buys something we can actually check. Carrying a distinct responsibility is enough on its own, even with no immediate accuracy gain.

---

## D-035 — The effort setting - every cost-driving choice is a setting, never a hardcoded constant

**As decided, in the words it was decided in:**

```
**(a)** every cost-driving choice is an
explicit *setting*, never a hardcoded constant; **(b)** every optional expensive refinement is a cleanly separable on/off
stage.
```

**In plain words:** Anything that makes the analysis slower must be something the user or the caller can turn down, not a number baked into the code; and any expensive extra step must be separable so it can be switched off.

---

## D-072 — The dependency rule - the analysis library knows nothing about the score format

**As decided, in the words it was decided in:**

```
This dependency order is **enforced**. Any code that would invert it (e.g. a composing header forward-declaring `mu::engraving::Note`) must be moved to the notation bridge layer.
```

**In plain words:** The music-theory library must not know how MuseScore stores a score. Anything that needs both lives in a thin bridge layer in between.

---

## D-095 — The dual path during the joint-estimator build is a declared, bounded, pre-ratified migration state

**As decided, in the words it was decided in:**

```
migration state (#23) is therefore CLOSED on both surfaces, and the legacy `region::analyzeRegions` →
`analyzeSection` path is compiled and dormant, awaiting deletion at the OI-180 retirement map. The first
```

**In plain words:** Building the new estimator beside the old one temporarily breaks the rule that there is one way to do each thing. That was declared in advance, bounded, and given a retirement plan.

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

## D-131 — One shared style taxonomy, not two parallel vocabularies

**As decided, in the words it was decided in:**

```
The style vocabulary the presets select on is **one shared taxonomy** — the **five idioms**: *Diatonic-functional* ·
*Chromatic-functional* · *Seventh-functional* · *Triadic-modal* · *Chromatic-coloristic* — with **mode** (major/minor)
and **chromaticism** (diatonic/chromatic) carried beside them as two **orthogonal cross-attributes**, not folded into
the idiom names. Tags are **multi-valued**: one entry may carry several idioms. It is the **same** set the Harmonic
Vocabulary (§7) tags its entries with, **not two parallel vocabularies** — that shared-set property is what this section
exists to state, and it is unaffected by the 2026-06-30 replacement of the list itself.
```

**In plain words:** The list of style categories the presets choose from is the SAME list the harmonic vocabulary tags its entries with — one shared set, not two that can drift apart. That set is the five idioms (Diatonic-functional, Chromatic-functional, Seventh-functional, Triadic-modal, Chromatic-coloristic), with major/minor and diatonic/chromatic carried separately beside them; an entry may carry more than one idiom.

---

## D-132 — The remaining empirical grounding is the per-preset WEIGHTS alone; the clusters half is delivered by the ratified five-idiom set

**As decided, in the words it was decided in:**

```
**What remains future work is the per-preset WEIGHTS, not the clusters.** Presets become named **idiom-weightings** over
the five — a distribution over the idioms rather than a name picked from a list — and deriving those weights by
clustering corpora is the committed work (`cowork_style_clustering_plan.md`); the weighting itself is a joint decision
with the preset system and the recognition consumer's job, not the Harmonic Vocabulary's
(`cowork_progression_schema_dictionary.md:317-330`). The **clusters half is delivered**: the clusters *are* the five
idioms, discovered and encoded.
```

**In plain words:** Grounding the style system in data was recorded as two pieces of committed work: discovering the categories, and measuring how strongly each one weighs in each preset. The first is done — the five idioms were discovered from corpora, ratified and encoded. What is still owed is the second: a per-preset weighting over those five, derived by clustering corpora rather than asserted.

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

## D-190 — The decision-neutrality corollary - what exists carries no weight in choosing a design

**As decided, in the words it was decided in:**

```
*Decision-neutrality of the existing implementation (corollary to #4/#6/#19; user-ratified
2026-07-26):* Designs are chosen from the principles and the ultimate objective — enabling the
best possible inference — alone. In that choice: **(a)** the value of reusing existing code, and
the cost of making existing code obsolete, are SECONDARY — they may break ties between designs
equal under the principles and the objective, and reuse counts only as carried-forward
establishment (#19), never as sunk cost or saved effort; **(b)** downstream implementation
impact — whether and how many consumers must change — carries NO weight; **(c)**
end-user-visible behavior change carries NO weight (the 2026-07-26 unshipped-scoping ruling),
while every behavior change remains ratification-gated (#14) and verification-gated (#15/#19)
exactly as before. The best-possible-inference design is chosen first; what exists then either
serves it or retires. (This does not weaken #6 — one path per concern is an END-STATE structural
principle, not a preservation claim for the existing path; nor #19 — establishment must still
exist before trust.)
```

**In plain words:** A design is chosen on the principles and the goal of the best possible analysis, and on nothing else. What it would cost to make existing code obsolete is a secondary consideration that can only break a tie between designs already equal; how many places downstream would have to change counts for nothing; and a change in what the user sees counts for nothing either - though every such change still needs ratifying and verifying exactly as before. The best design is chosen first, and what exists then either serves it or is retired.

---

## D-201 — Very large scores must be handled, and are expected to be more common than our corpora

**As decided, in the words it was decided in:**

```
**Very large scores MUST be handled, and are expected to be a MORE COMMON use than our corpora.** A
Wagner act or a symphony has to produce an analysis; the user expects such music to be a more common
```

**In plain words:** A Wagner act or a symphony must work. The user expects such scores to be a more common use than the chorales the system was fitted on. This is a standing requirement every later design is judged against, not a defect report.

---

## D-202 — The effort control is one setting with several dials, and it must bound the time taken

**As decided, in the words it was decided in:**

```
**The effort control is ONE setting with several dials behind it, and among the quantities it must
bound is the TIME the analysis takes. DEFERRED.** How hard the analysis works is a single user-facing
```

**In plain words:** How hard the analysis works is a single setting the user turns, not several. Behind it sit several dials, and among the things it must be able to bound is how long the analysis takes. It is too early to build: which pieces of the analysis have to be switchable is not yet known.

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

## D-206 — Intonation is held as a future feature, and is a declared future consumer of the analysis

**As decided, in the words it was decided in:**

```
**Status of this whole section — HELD, and a declared future CONSUMER of the analysis (user-decided
2026-07-13).** Intonation **is** a future feature: the six unbuilt items specified in §11.3a–g, together
with the tie limitation recorded there, stay on the books as a deliberate long-horizon hold, revisited at a
```

**In plain words:** The six unbuilt pieces of the tuning design stay on the books as a deliberate long-horizon hold, revisited at a natural pause in the analysis work. The reason the hold is strategic rather than neglect: tuning will read the analysis - knowing the mode, the chord, its function and the progression is what lets a just-intonation decision be made, particularly the decision about staying in tune over time versus letting the pitch drift.

---

## D-223 — A gate that judges the pre-correction winner reads a snapshot, not the live result

**As decided, in the words it was decided in:**

```
- **Pre-sort capture for original-winner gates.** Gates that compute against
  the pre-correction winner must read `originalWinner*` snapshots, not the
  live `results[0]` reference (Sub-9a lesson).
```

**In plain words:** Where a gate has to compare against whatever the analysis thought before a correction was applied, it reads a copy taken beforehand rather than the current top result, which the correction may already have changed.

---

## D-229 — The MuseScore-dependency rule - one general rule for what our code may depend on

**As decided, in the words it was decided in:**

```
1. **The analysis library (`composing`) depends on no MuseScore or engraving types** — the
   Dependency Rule above, unchanged.
2. **The bridge layer reads the score model only through the established bridge pattern, and
   never layout-derived state as analysis input.** The Layer-1 note model is the single
   sanctioned reading surface for analysis facts; positions, spacing and other layout products
   are presentation outputs, readable only for placing presentation artifacts, never as
   inference evidence (a layout read entering analysis is the OI-98 class, judged against this
   rule).
3. **Editing MuseScore's own code is admissible only for a defect blocking our feature.** Each
   instance is recorded in `CLAUDE.md`'s local-patches section with a do-not-revert note and an
   explicit per-instance distribution disposition (upstreamable or fork-local), ratified by the
   user. The recorded contribution intent (§1.2) governs our module as a whole; distribution is
   decided per patch — the fork-local constraint on the MusicXML mode-import patch is such an
   instance, not a contradiction of the intent.
```

**In plain words:** Three parts. The music-theory library uses no MuseScore code at all. The bridge code that connects analysis to the score reads the score only through the established bridge functions, and never uses layout results (positions, spacing) as analysis input - the note reader is the one sanctioned reading surface. And changing MuseScore's own code is allowed only to fix a defect blocking our feature, each change recorded, with its distribution (upstreamable or fork-only) decided and ratified case by case.

---

## D-260 — Analysis output covers exactly the selection; everything loaded beyond it is evidence, never a result

**As decided, in the words it was decided in:**

```
**Invariant.** The analysis output covers **exactly the selection**; everything outside it is evidence, never a
result.
```

**In plain words:** The user's selection is the output span: labels are emitted only for it. Music loaded from outside the selection is pulled in as evidence for judging the selection's edges and is never itself labelled.

---

## D-261 — A layer never guesses how much context it needs - the amount is discovered by convergence

**As decided, in the words it was decided in:**

```
3. A layer must distinguish **"unavailable because not loaded"** (→ request extension) from **"unavailable because the
   score starts/ends here"** (→ proceed, truncated). Architectural Layer 1 reports which.
4. A layer **outputs analysis only for the selection**; extended context is evidence, never labelled.
5. A layer **never guesses how much** more context it needs — guessing an amount is the un-knowledge-based move this
   contract forbids. It knows *what* it needs, not how far away that is, so it **extends incrementally and stops on a
   principled condition**; the amount is **discovered, not chosen**.
6. The principled stop is **convergence**: extend until the layer's **in-selection output stops changing** with
   further context. This is self-validating — you have enough context exactly when adding more does not change the
   answer — and it is what keeps the result independent of the extension step size (the equivalence invariant, §4).
   **A layer applies that criterion DIRECTLY, on the in-selection quantity the extension was requested for**: it
   re-infers over the enlarged span, compares that quantity step against step, and stops when it repeats. The
   as-built Architectural Layer 3 reach-back does exactly this — it tracks the **leading-edge settled key across
   iterations and stops when it repeats**, which is the criterion itself and not a stand-in for it (the convergence
   note above the reach-back loop in `regionanalyzer.cpp` states it in the code's own words). §7's safety caps are
   the only other way out of the loop, and a cap that fired is never the discovered amount.
```

**In plain words:** A layer knows what evidence it needs but not how far away it is, so it never picks an amount. It extends the loaded span incrementally and stops on a principled condition: convergence, meaning its in-selection output stops changing as more context arrives. The layer applies that test directly, on the quantity it asked for more context about, and stops when that quantity repeats.

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

## D-265 — Asking a lower layer for more notes is a data-supply call, not a backward inference edge

**As decided, in the words it was decided in:**

```
- **The re-inference cascade IS the forward-only contract, not an exception to it.** The extension **request** is a
  data-supply call **down** to Architectural Layer 1 (a higher layer using a lower layer's service — control, not
  inference). The new notes and every re-inference then flow **forward** (Architectural Layer 1 → 2 → 3 → …), exactly
  as on a first run. **Inference never flows backward** — a later layer re-inferring cannot alter an earlier layer's
  result. So an extension is precisely *"ask down for more raw material, then infer forward again,"* with no backward
  inference edge anywhere; this is what makes it consistent with the project's forward-only analysis contract.
```

**In plain words:** An extension request travels down the stack to the note supplier, and the new notes and every re-inference then flow forward through the layers exactly as on a first run. Inference never flows backward: a later layer re-inferring cannot alter an earlier layer's result. So extension is consistent with the forward-only contract rather than an exception to it.

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

## D-268 — A confidence attaches to a named decision, is compared only within its class and a declared frame, and keeps its identity downstream

**As decided, in the words it was decided in:**

```
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
```

**In plain words:** Five rules of use. A confidence belongs to a named decision, never to a layer in general. At a layer boundary it is zero-to-one, class-declared and decision-named. A consumer may compare two confidences only within one class and one declared comparison frame. A carried-forward confidence keeps its source layer, decision and class, with no silent reinterpretation. An abstention means the decision's confidence is below that layer's declared bar - the same meaning everywhere, not a separate ad-hoc judgment.

---

## D-275 — Every published record carries its own instrument provenance; a provenance-less analysis cannot exist

**As decided, in the words it was decided in:**

```
Every published record carries its instrument provenance: the embedded table set's source-artifact
hashes and the selected weight-vector identity (both compiled in per Decision D1), plus the
decoder's version. A consumer — and any future measurement — can always answer "which fitted
values produced this analysis" from the record itself; a provenance-less analysis cannot exist.
```

**In plain words:** Each record published for the notation path carries the source-artifact hashes of the fitted table set, the identity of the selected weight vector, and the decoder's version. A consumer, or any later measurement, can always answer which fitted values produced a given analysis from the analysis itself.

---

## D-279 — The Stage-3 entry gate - seven conditions before any engagement wiring reaches production

**As decided, in the words it was decided in:**

```
**★ STAGE-3 ENTRY GATE (ratified 2026-07-10 with #17–#19; evidence `cowork_l1_l5_premise_debt_audit.md`).**
Before any E4/L5 engagement wiring can reach production:
- **(EG-1) Tier-1 defusal is a PREREQUISITE, not an inventory item:** the resolver selection re-ordering
  (arc #9 — the as-built `resolveAbstained` still selects progression-first at confidence 1.0, the channel
```

**In plain words:** Before the rebuilt path's wiring can reach production, seven conditions hold: the two measured-harmful mechanisms are defused or provably bypassed; the go/no-go measurement runs under the full Premise Gate with its measurement tool established first; the pedal reader waits on its underpowered premise being settled; the confidence-commensurability premise owes a ledger and a desk simulation before any threshold is fitted; the fit surface is completed; the Jazz preset's validation status is declared honestly; and no step opens until every layer it depends on has passed its audit.

---

## D-282 — Meta-finding: the oracle/tier metric, never a bare proxy - superseded by the robust-unit stop and the two-tier policy

**As decided, in the words it was decided in:**

```
- **Oracle/tier metric, never a bare proxy** (BIR rewards wrong-root=bass). Make the dual metric standing.
```

**In plain words:** Never grade the analysis on the bare bass-is-root number, which rewards a wrong chord root that happens to be the bass; use the oracle-checked, tiered measurement. Its content became standing through the robust-unit regression stop and the two-tier class policy.

---

## D-286 — Whole-score interactive analysis was SHELVED WITH EVIDENCE; the bounded window is the ratified reading

**As decided, in the words it was decided in:**

```
**★ ONE OF THE TWO AXES THE EFFORT CONTROL MUST BOUND ALREADY CARRIES A RECORDED RULING, AND THIS
SECTION MUST NOT BE READ AS OPEN ON IT: WHOLE-SCORE INTERACTIVE ANALYSIS IS SHELVED WITH EVIDENCE
(Cowork, 2026-06-12, at Stage 3.1b; written into this section 2026-08-09 on the user's ruling —
register entry **D-286**).** The bullet above records the user's prediction that always reading the
entire score will very likely not survive. That prediction is not the first word on the question. A
**measured A/B** put a whole-score interactive analysis against a **bounded-window** one, graded
against the published human annotations; **the bounded window won, the whole-score variant was
SHELVED with evidence, and the bounded-window cache was adopted as the ratified reading**.
```

**In plain words:** At Stage 3.1b a measured A/B put a whole-score interactive analysis against a bounded-window one and the window won against the published annotations; the whole-score variant was withdrawn against that measurement and the bounded window adopted. The question of whether a per-note answer must match the whole-piece answer was parked, not settled.

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

## D-295 — Zero information loss to the end user - every inferred object must be displayable

**As decided, in the words it was decided in:**

```
**The governing requirement over everything in this section: ZERO INFORMATION LOSS TO THE END USER — every
inferred object must be displayable.** Anything the analysis works out has to be capable of being shown.
Revealing it gradually, so that a display is not overwhelming, is the intended design; leaving something the
```

**In plain words:** Anything the analysis works out must be capable of being shown to the user. Showing it gradually, so the display is not overwhelming, is fine; leaving something permanently unreachable because the interface has no place for it is not.

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

## D-322 — Any change to optimization flags or to the order of the scoring arithmetic requires a full corpus A/B on both presets

**As decided, in the words it was decided in:**

```
These could **flip** under any change that re-associates the floating-point arithmetic:
different compiler / optimization flags (`-ffast-math`, `/fp:fast`, FMA contraction),
a different platform's libm, or a reordering of the summation in the score expression
`(basisIndep + bassDep) × complexityFactor × augFactor + wComplete + wSeq [+ wDim] [+ step]`.
Treat the exact evaluation order as load-bearing: **any change to optimization flags or to
the order of the scoring arithmetic requires a full corpus A/B on both presets** before it
```

**In plain words:** Because candidate scores are compared exactly, re-ordering the arithmetic or changing compiler optimization settings can flip a reading that was decided by a hair. Such a change is not trusted to leave the output unchanged until it has been checked against the whole corpus on both tuning presets.

---

## D-324 — Retirement of a post-scoring rule is global — a rule still doing work on any one preset is retained for all

**As decided, in the words it was decided in:**

```
  Baroque but 18 load-bearing Jazz firing sites, §1.2). Retirement is global, so a rule live on ANY
  carrier is retained.
```

**In plain words:** A correction rule is either removed everywhere or kept everywhere. If it still changes an answer under any one of the tuning presets, it stays.

---

## D-352 — The key/mode grading bar splits the cases first: agreement where the published analyses are unanimous, any recorded reading (or an uncertain mark) where they are not

**As decided, in the words it was decided in:**

```
The bar, with its partition stated: a case counts as **unambiguous** when the ground-truth
  annotation gives a single local key/mode there, records no alternative reading, and (where more than one published
  analysis covers the piece) the analyses agree; every other case — a recorded alternative reading, disagreeing
  published analyses, or a modal passage the major/minor-only ground truth cannot represent (§1) — counts as
  **genuinely ambiguous**. On the unambiguous cases the bar is agreement with the single reading; on the ambiguous
  cases the bar is met when the layer's answer equals **one of the recorded readings** (that is what "defensible"
  means here) or the case is marked "uncertain."
```

**In plain words:** A case counts as unambiguous when the published human analysis gives one tonality there, records no alternative, and — where more than one published analysis covers the piece — the analyses agree. Everything else counts as genuinely ambiguous: a recorded alternative, disagreeing analyses, or a modal passage the major/minor-only human analysis cannot express. On the unambiguous cases the analysis must match the single reading; on the ambiguous ones it must match one of the recorded readings or declare itself unsure.

---

## D-353 — The key/mode layer is graded on two goals kept apart — agreement where the notes decide, and whether its own uncertainty lands on the genuinely ambiguous cases

**As decided, in the words it was decided in:**

```
- **Two quality goals, measured separately.** (1) *Accuracy on the resolvable cases* — agreement with the human
  analyses where the notes decide; and (2) *calibration of uncertainty* — whether the "uncertain" mark and the
  confidence actually land on the genuinely ambiguous slices (a reliability curve over confidence; the precision and
  recall of the "uncertain" mark on the error set; and whether the true key is carried among the alternatives). The
  second goal is what backs the claim that Architectural Layer 3 is clearer about ambiguity than a single forced
  label, so it is graded in its own right, not folded into accuracy.
```

**In plain words:** Two things are measured, and neither is folded into the other. First, does the tonality agree with the published human analysis where the notes settle it. Second, is the layer's own declared uncertainty honest — whether the unsure mark and the confidence actually fall on the genuinely ambiguous stretches, and whether the true tonality is among the runners-up it carried.

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

## D-388 — Texture is read primarily from HOW VOICES MOVE TOGETHER, not from how far each line leaps — the interval-led alternative was measured weaker and partly an encoding artifact

**As decided, in the words it was decided in:**

```
- **D2 — motion-type-led features.** Measured (§4): the ablation is decisive, and the motion view is the
  extraction-robust one (it never explodes chords; it grouped exploded chamber corpora with the chorales, ruling
  out an encoding artifact). *Alternative rejected:* interval-profile-led (the pilot's view) — weaker (≤0.20) and
  partly a chordal-density artifact by the study's own caveat.
```

**In plain words:** What separates one texture from another is the pattern of parallel, similar, contrary and oblique motion between pairs of lines. The rates of those four motion types alone recover the texture structure; the statistics of how far each single line moves do not, and are used only as a secondary description of melodic complexity.

---

## D-389 — A notated voice is a FACT and an inferred perceptual line is a JUDGMENT — the two are separate types and are never conflated

**As decided, in the words it was decided in:**

```
- **D3 — two-tier voice model: notated voice = fact; stream = inference.** Never conflated; enforced by the §0
  one-sense rule and the type system (VoiceLine vs Stream). *Alternative rejected:* a single "voice" concept with
  a quality flag — exactly the silent fact/judgment mixing the universality principle forbids.
```

**In plain words:** The line the score actually writes and the line a listener hears are different things and are kept apart, in the words used and in the types the code carries. The written one is a fact taken from the score; the heard one is always called a stream, is always marked inferred, and carries its own confidence. Merging them into one idea with a quality flag was considered and rejected.

---

## D-390 — The first version classifies the WHOLE selection as one texture — classifying within a piece is deferred behind a measurement, because the evidence is per-piece

**As decided, in the words it was decided in:**

```
- **D4 — texture classification is v1's only judgment, at whole-selection granularity.** The evidence is
  per-piece; a per-span claim would be assumption-based code. The refinement is a named cheap measurement first
  (§15-1). *Alternative rejected:* shipping windowed per-span classification now — knowledge-based-coding
  violation.
```

**In plain words:** The study that established the texture classes measured whole pieces. Whether the same statistics, computed over a moving window, would find the places where the texture changes inside a piece has not been measured. So the first version gives the whole selection one texture, and finding several within it waits on that measurement. Shipping the windowed version now was considered and rejected as building on an assumption.

---

## D-392 — The later voice-leading components are CLAIMS WITH OWNERS, not builds — each clears its own design document and its own evidence before any instruction exists

**As decided, in the words it was decided in:**

```
- **D5 — staged components behind design gates.** VL-D/E/F/G/H are claims with owners, not builds; each clears its
  own design + footing before an instruction exists. This is the proportionality gate applied *inside* the axis —
  no slot-filling (the Contrapunctus reminder). *Alternative rejected:* one monolithic axis build.
```

**In plain words:** Stream separation, phrase segmentation, pattern recognition, voicing analysis and part-writing advice are all named and assigned, but none is built. Each first needs its own design document and the evidence to stand on. Building the whole dimension in one go was considered and rejected.

---

## D-393 — Every voice-leading inference publishes the committed answer AND the FULL ranked list of all alternatives with their weights — nothing below the top is discarded

**As decided, in the words it was decided in:**

```
- **Output — the committed class PLUS the full ranked alternative list (zero information loss; ratification
  clarification, user 2026-07-03):** the span's voice-leading idiom from the four-class taxonomy (§0) is the
  TOP of a **fully ranked list of ALL class fits, each carried with its weight** — nothing below the top is
  discarded; a downstream consumer (and Stage-5 calibration) sees everything VL-C saw. This is the ARCH §2.15
  minimality-plus-maximal-information contract applied here (the same carried-alternatives discipline as L4's
  ranked chord readings).
```

**In plain words:** The texture stage does not publish only the class it chose. It publishes every class it considered, ranked, each with the weight it earned, so that anything reading it later — including the calibration step — sees exactly what the stage saw. Nothing below the winner is thrown away.

---

## D-394 — Reducing a chord-bearing voice to one line is a DECLARED parameter of the request, uniform across sources — never silent, never chosen per source; the first version offers exactly one rule

**As decided, in the words it was decided in:**

```
- **Reduction is declared, uniform, and per-query — never silent, never per-source.** A consumer needing one line
  from a chordal voice names a reduction rule (v1 provides exactly one: **top-note** — the highest sounding pitch
  per event, the study's curated-branch rule). The rule is a parameter of the *query*, carried in the output's
  provenance. This single uniform rule is what retires the study's per-source explosion asymmetry (its View-A
  caveat) when the production extractor is built.
```

**In plain words:** Where a written voice carries chords rather than single notes, anything needing one line from it must name the rule that picks that line, and the rule travels with the answer as provenance. There is one rule in the first version: take the highest sounding pitch. It is applied the same way everywhere, which is what removes the uneven treatment the exploratory study had between its sources.

---

## D-395 — Three named floors govern abstention, and the FIT floor is the one that lets a passage resembling NO known texture decline rather than be forced to its nearest

**As decided, in the words it was decided in:**

```
- **Honest marks — the three declared floors (named once here, used by these names everywhere):** the
  **evidential floor** (minimum motion-sample count for a profile to support a decision), the **margin floor**
  (minimum best-vs-second-best margin), and the **fit floor** (minimum absolute fit of the best class).
  Abstention (uniform semantics, contract U5) fires when the margin is below the margin floor **or** the best fit
  is below the fit floor — the second clause is what makes a span resembling *no* reference class abstain rather
  than be forced to its nearest class (a relative margin alone cannot deliver that).
```

**In plain words:** The texture stage declines to answer under three named conditions: too few motion samples to support any decision, too small a lead of the best class over the second, or too poor an absolute fit of the best class. The third is the one that matters for music the taxonomy does not cover: without it, a passage unlike every known class would still be assigned to whichever class it least resembled, because a lead over the second-best says nothing about whether either fits.

---

## D-396 — The voice-leading dimension covers NOTATED music only, and its style coordinate is UNDEFINED — not zero — for sources that carry no voices

**As decided, in the words it was decided in:**

```
- **Coverage declaration (honest, structural).** The axis analyses **notated music only** — lead-sheet sources
  carry no voices, so the voice-leading coordinate of the 2-D style structure is simply *undefined* for them
  (undefined, not zero, in every consumer). This is a representational fact, not a corpus accident.
```

**In plain words:** This dimension reads the lines a score writes, so a source that carries no lines at all, such as a lead sheet, has no voice-leading character to read. Every consumer must treat that coordinate as undefined rather than as zero, because a missing measurement is not a measurement of nothing.

---

## D-397 — The homeless analysis objects are ASSIGNED to named owners on the voice-leading dimension — the stock patterns, the melodic phrase, chord voicing, and part-writing advice — as claims, discharged only at each owner's own ratified design

**As decided, in the words it was decided in:**

```
**★ FOUR ANALYSIS OBJECTS THAT HAD NO OWNER ARE OWNED BY THE VOICE-LEADING AXIS, AS CLAIMS (user-ratified
  2026-07-03; written here 2026-08-09).** Growth by axis only works if every analysis object has a named owner, and
  four did not. They are assigned here, and each is recorded **as a CLAIM with an owner rather than as work
  started** — a claim is discharged only when that component's own design is ratified, never by this line.
```

**In plain words:** Four kinds of analysis object that previously had no owner are assigned here: the stock eighteenth-century patterns and the chromatic line cliché, which the chord dictionary already flags as belonging to this dimension; the melodic phrase; chord voicing and arrangement, which the dictionary explicitly excludes from its own scope; and checking and advising on part-writing. Each is recorded as a claim with an owner, not as work started, and the claim is settled only when that owner's own design is ratified.

---

## D-398 — Parallel motion is judged SEMITONE-EXACT, not by generic diatonic size — a same-direction move whose semitone interval changes counts as similar motion

**As decided, in the words it was decided in:**

```
**★ "INTERVAL PRESERVED" IS SEMITONE-EXACT, NOT GENERIC DIATONIC SIZE — CLOSED AT BUILD, 2026-07-03.** Two lines
  count as **parallel** only when they move the same direction AND the SIGNED SEMITONE distance between them is
  unchanged; a same-direction move whose semitone interval changes is **similar**. So a pair moving from a major
  third to a minor third is similar motion, not parallel, although both are thirds on the staff.
```

**In plain words:** Two lines count as moving in parallel only when they move the same way and the distance between them in semitones is unchanged. A pair moving the same way from a major third to a minor third is therefore similar motion, not parallel, even though both are thirds. The alternative — counting by the size of the interval as written on the staff, so that any third to any third is parallel — was the open question, and this is the answer.

---

## D-400 — A PER-VOICE span kind is admitted to the span typology — melodic phrases overlap across voices by construction and tile only within one voice

**As decided, in the words it was decided in:**

```
**★ THE TYPOLOGY ADMITS A PER-VOICE SPAN KIND (user-ratified 2026-07-03; written here 2026-08-09).** Every span
  kind listed above cuts across the whole texture at once — it is a segmentation of the music, and the members of
  one kind tile it. **A MELODIC PHRASE DOES NOT.** In contrapuntal writing the voices' phrases run concurrently and
  out of step with one another, as a fugue's staggered entries do, so phrase-spans **overlap across voices by
  construction and tile only WITHIN one voice**. The typology therefore carries a second kind of member: a
  **per-voice span**, whose tiling law is stated per voice rather than over the texture.
```

**In plain words:** Until now every kind of span the analysis produces cuts across all the music at once. The melodic phrase does not: in contrapuntal writing the voices' phrases run concurrently and out of step with one another, as a fugue's staggered entries do. So a per-voice kind of span is admitted to the catalogue of span kinds, which is what a phrase-segmentation design can then be written against.

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

## D-421 — Idiom re-discovery rides every corpus wave, on research material only, and a changed cluster set is its own ratification event

**As decided, in the words it was decided in:**

```
- **Idiom re-discovery RIDES EVERY CORPUS WAVE, on research material only, and a changed cluster
  set is its own ratification event.** After each material corpus change the discovery pipeline is
  re-run under the protocol above, on the **development set and outside research corpora only** —
  held-out material excluded — asking first whether the five idioms **reproduce**. **A changed
  cluster set is a ratified taxonomy-revision event**: it propagates to the style-tag values and to
  the vocabulary's per-entry mapping, so once those tags are encoded it is a migration and not a
  relabel. *Why:* the held-out exclusion is #20 applied to an unsupervised study — discovery
  outputs become shipped parameters, so material used to discover them can never also measure them.
  The re-run itself is the standing consequence of the finding this section rests on, that the
  categories are empirical rather than asserted, which means new music can falsify them; the record
  names the falsifiable edges in advance — whether the chromatic-coloristic idiom splits under new
  chromatic mass, where the high-chromaticism composers land, and whether early modal material
  separates or folds in — and naming them in advance is what makes the trigger a test rather than a
  formality.
```

**In plain words:** Whenever the body of music the project holds changes materially, the study that discovered the five idioms is re-run under the same protocol, to ask whether the five reproduce. It is run only on the development set and outside research corpora, never on the music held back for evaluation, because what the study produces becomes a shipped parameter. If the clusters come out different, that is a taxonomy revision and needs its own ratification — it changes the tags on every catalog entry, so after the tags were encoded it is a migration, not a relabel.

---

## D-423 — The gate-retirement stage is the only sanctioned way the post-scoring gates change, and three do-not rules hold through every stage

**As decided, in the words it was decided in:**

```
- **Three prohibitions hold through every stage, and the per-gate RETIREMENT STAGE is the only
  sanctioned way these gates change:** no new gates, no threshold widening, no gating of the
  root-continuity bonus. *Why:* each prohibition carries its own defense elsewhere — accumulating
  gates are a warning sign and the answer is iteration rather than more gates; gate thresholds are
  Baroque-calibrated and are not loosened for another style; gating the root-continuity bonus on a
  sparse predecessor was measured a dead end (the bullet above). What this constraint adds is the
  **single sanctioned channel** — the retirement stage's per-gate differential proof obligation —
  which is what stops the gate layer changing by accretion.
```

**In plain words:** LEGACY (the chord analyzer awaiting deletion): three prohibitions hold for the whole programme — no new after-the-fact correction rules, no widening of a threshold, and no gating of the root-continuity bonus. The only sanctioned way any of those correction rules changes is the deliberate per-rule retirement stage, where a rule is removed only once the replacement reproduces the fixes it was pinned to.

---

## D-441 — Analysis and modification are phases of ONE conversation; a follow-up instruction re-uses the reasoning rather than re-analysing

**As decided, in the words it was decided in:**

```
**Conversational continuity.** Analysis and modification occur in one
conversation thread. When the LLM identifies problems in a QA query, "make
the fixes you suggested" executes without re-analysis — the LLM reasons from
its own conversation history.
```

**In plain words:** Asking about the music and then changing it happen in a single conversation. When the model has already worked out what is wrong, an instruction to fix it is carried out from what it already reasoned through, not by analysing the music again.

---

## D-442 — A validation failure goes back to the language model as a tool-call error and is never shown to the user

**As decided, in the words it was decided in:**

```
Violations are fed back to the LLM as tool call errors, not shown to the user.
The LLM corrects and retries. Only clean output reaches the score.
```

**In plain words:** When the checks reject something the model proposed — a note outside an instrument's range, parallel fifths, a malformed bar — the rejection is returned to the model, which corrects itself and tries again. The user never sees the rejected attempt; only output that passed the checks reaches the music.

---

## D-443 — Tool use is the only capability the provider abstraction requires; a provider without it is read-only

**As decided, in the words it was decided in:**

```
Users choose their LLM provider in MuseScore preferences. The abstraction
requires only that a provider supports tool use (function calling). Providers
without tool use support may be used for read-only analysis but cannot drive
score modification.
```

**In plain words:** The user picks which language-model provider to use. The only thing the system demands of a provider is that it can call tools. One that cannot may still be used to answer questions about the music, but it may not be used to change the music.

---

## D-444 — The core access layer is a facade over interfaces that already exist, not a redesign

**As decided, in the words it was decided in:**

```
family already covers almost everything the Core Access Layer needs. **The
Core Access Layer is not a redesign — it is a facade over interfaces that
already exist.**
```

**In plain words:** The shared foundation the language-model bridge and any future plugin interface both sit on is not new machinery. An audit of the existing internal interfaces found they already cover almost everything it needs, so the layer is a clean face over what is there.

---

## D-445 — A musical address does not identify a single note, so the note entity carries its own identifier

**As decided, in the words it was decided in:**

```
**Address alone does not uniquely identify a Note.** Multiple notes in the same
chord share an identical address (same part + staff + measure + beat + voice).
A `NoteId` is required to unambiguously target a single note. `NoteId` must
appear explicitly on the Note entity; it maps internally to the EID system.
```

**In plain words:** Several notes of one chord sit at exactly the same address — same part, staff, bar, beat and voice — so an address cannot name one note. The note therefore carries an identifier of its own, and that identifier is what a change is aimed at.

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

## D-448 — The operation set is curated from observed use, not an exposure of every editing method

**As decided, in the words it was decided in:**

```
~40 curated operations covering the high-value modification tasks. Not an
attempt to expose every `INotationInteraction` method. Chosen by observing
which operations Phase 1 and Phase 2 usage actually reaches for.
```

**In plain words:** The model gets a chosen set of about forty editing operations covering the changes that matter, rather than everything the editor can do. Which ones are chosen is decided by watching what the read-only phases actually reach for.

---

## D-451 — A desk simulation's table values are provisional, enter no fit, and a verdict that would flip inside a provisional value's plausible range is reported as a near-tie, never as a win

**As decided, in the words it was decided in:**

```
    **★ WHAT A DESK SIMULATION'S TABLE VALUES ARE, AND WHAT THEY MAY NEVER BECOME (user-ratified
    2026-07-19).** Every table value a desk simulation under (c) uses is **PROVISIONAL** — declared
    before use, each labeled with its provenance class, and hand-declared stand-ins whose only job
```

**In plain words:** When a mechanism is traced by hand, the numbers used are stand-ins declared up front whose only job is to let the mechanism be followed. None of them may become a fitted value later. And if a trace's answer would change had a stand-in been chosen differently within its believable range, the trace reports a near-tie and names the deciding cell rather than claiming a winner.

---

## D-452 — Every desk-simulation trace runs at identity weights — the ratified ablation baseline — so the trace tests the structure and the tables, not the weighting

**As decided, in the words it was decided in:**

```
    **★ EVERY DESK-SIMULATION TRACE RUNS AT IDENTITY WEIGHTS (user-ratified 2026-07-19).** A trace
    under (c) runs the generative product with every weight at one — exactly the mandatory ablation
    baseline the design already carries. The desk simulation therefore tests the structure and the
```

**In plain words:** Each hand trace is run with every weight set to one, which is the baseline the design already requires be measured. That way what the trace checks is whether the shape of the model and its tables behave, and not whether a weighting was chosen well.

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

## D-469 — The tick-local path is left OUTSIDE the unified pipeline by design — its point-in-time semantics would be distorted by one shared interface

**As decided, in the words it was decided in:**

```
**The point-in-time (tick-local) path is left OUTSIDE this pipeline BY DESIGN — two modules with a
documented relationship, not an unfinished unification.** This section's opening states the scope:
single-note analysis is the foundation and region analysis extends it to a time range. Three of the
four ways the program produces harmony were unified onto that region pipeline; the fourth — the one
that answers *what chord is under this note, right here* — was **deliberately left parallel**.
*Why:* stated with the decision — its point-in-time semantics differ too much from region-based
analysis to force a single interface without distortion, so the cost of unifying here is a
distorted interface rather than a saved duplication. **This is the pipeline's own scope statement
and it is stated once, here**; §5.13, which tabulates the tick-local entry points, points at it and
does not restate it (#6). Distinct from the two later decisions about that path — that it keeps the
older resolver, and that its cold context is accepted: this is the prior decision that it stays a
separate module at all.
```

**In plain words:** Three of the four ways the program produces harmony were merged into one shared pipeline. The fourth — the one that answers 'what chord is under this note, right here' — was deliberately left separate, because forcing it through a pipeline built around stretches of music would bend what it means.

---

## D-470 — The temporal-context extension fields are recorded during the pipeline's own analysis pass; no consumer re-runs the chord analysis to rebuild them

**As decided, in the words it was decided in:**

```
- **The temporal-context EXTENSION FIELDS are recorded during the analysis pass that computes
  them; a consumer READS what was recorded and never re-runs the chord analysis to rebuild them.**
  The fields are populated on each analyzed region during the pipeline's own per-region analysis,
  using the already-built region list as context; a consumer that needs them reads the field. *Why:*
  stated with the decision — a second analysis run with a display-time context can populate the
  same fields differently from what the annotation pass saw, so the two user-facing paths drift
  apart. Recording once and reading the record removes the second computation instead of trying to
  keep two computations in step, which is the fact-publication corollary applied here: the field is
  published by its producer and consumers read, never re-derive. **This rule is stated at the
  producing surface**, which is this section; the consumer sections point at it and do not restate
```

**In plain words:** What the chord analysis saw around each stretch of music is written down while the analysis runs. A consumer that needs it reads what was recorded, instead of analysing the passage a second time with a freshly built context — which is how the two paths used to disagree.

---

## D-471 — The sub-beat annotation duration gate is not retired on argument — it is kept or dropped on a measured observation run, with the verdict stated in advance

**As decided, in the words it was decided in:**

```
**The sub-beat annotation duration gate is KEPT OR DROPPED ON A MEASURED OBSERVATION RUN, and the
verdict is fixed in advance.** A gate hides very short chords from the Roman-numeral annotation
while the chord track and the status bar still show them. Whether it survives is **not** settled by
argument; the decision rule is written down before the measurement and is binding:

- if the gate **measurably reduces clutter or false annotations without suppressing correct ones**
  → it is KEPT, as a documented emitter option with its current default, settable;
- if it **suppresses equally many correct and incorrect annotations** → it is RETIRED, the duration
  parameter's default becomes *no gate*, and the option is removed in the follow-up cleanup.

*Why:* stated with the rule — the question is whether the gate removes clutter or removes correct
labels, which is a measurement and not a preference; and fixing the verdict **before** the
measurement is what stops a live result from being argued into whichever reading suits it. It is
the pre-declared-protocol discipline (#22) applied to a display gate, and it is the pattern the
premise gate (#17b) later made general. **The gate is undischarged at HEAD:** the observation run
has not been made, so neither branch has fired.
```

**In plain words:** A rule hides very short chords from the Roman-numeral annotation. Whether to keep it was not settled by opinion: the decision was written down in advance as a comparison — run the annotation with and without it on real scores, and keep it only if it removes clutter without also removing correct labels.

---

## D-472 — Key areas are grouped by a smoothing pass over regions whose key sequence has already been smoothed, and a region that disagrees without clearing the confidence test keeps its own key while being grouped into the enclosing area

**As decided, in the words it was decided in:**

```
**★ KEY AREAS ARE GROUPED BY A SMOOTHING PASS OVER REGIONS WHOSE KEY SEQUENCE HAS ALREADY BEEN
SMOOTHED, AND A REGION THAT DISAGREES WITHOUT CLEARING THE CONFIDENCE TEST KEEPS ITS OWN KEY WHILE
BEING GROUPED INTO THE ENCLOSING AREA (re-homed into this specification 2026-08-08 on the user's
ruling — the owning layer in the target architecture, with §11.5 pointing; the PRECONDITION half of
the wording corrected 2026-08-09 on the user's ruling, immediately below).** Neighbouring regions in
the same key are collected into one key area. A key area opens at the first region and closes when
the next region's key differs from the current area's **and** that region clears a confidence test; a
region whose key disagrees but does not clear the test **keeps its own key reading** — so the status
bar stays accurate for that region — while being grouped into the enclosing area, so the annotation
emitter writes Roman numerals against the key that actually governs the passage rather than against a
momentary wobble. *Why:* it is a grouping rule and not a second key analysis — it reads the key
fields the earlier layers already published rather than re-deciding them, which is the same
not-a-new-detector reasoning this layer's contract states for grouping generally.
```

**In plain words:** Neighbouring stretches in the same key are collected into one key area. A stretch that reads a different key but is not confident enough to open a new area keeps its own reading for display, yet is counted inside the surrounding area — so the Roman numerals are written against the key that actually governs the passage rather than against a momentary wobble.

---

## D-474 — No published study reports per-axis inter-annotator agreement for Roman-numeral analysis of Baroque/classical symbolic music — the ground-truth ceiling principle #21 demands is unmeasured by the entire field

**As decided, in the words it was decided in:**

```
    **★ THE CEILING CANNOT BE CITED FROM THE LITERATURE; MEASURING IT HERE IS THE ONLY ROUTE
    (recorded 2026-08-04 on the user's ruling with the read-wave-3 ratification; D-474).** A
    dedicated search established a FACT-of-absence: no published study reports per-axis
    inter-annotator agreement for Roman-numeral or key annotation of Baroque/classical symbolic
    music. TAVERN released duplicate annotations but published no such number; ABC split its pieces
    between annotators with no overlap by design; the Mozart-sonatas corpus is consensus-built, so
    agreement cannot be recovered after the fact; *When in Rome* states in its own words that the
    variance is unmeasured; Dilemmadata (2026) identifies dual-annotated pieces and computes
    nothing. **So a session may not satisfy this principle by citation — there is nothing to cite.**
    The obligation is tracked at `OPEN_ITEMS.md` OI-179, which is therefore not "a measurement not
    yet built" among others but **the only available route to the quantity this principle demands**.
```

**In plain words:** Principle #21 says the accuracy of the human annotation is itself something to measure, so that an error we cannot fix is told apart from two experts simply disagreeing. Searching the literature found that nobody has published such a figure for this repertoire — so the ceiling cannot be cited from anywhere and would have to be measured here.

---

## D-475 — The BCMH chorale annotations are NOT established as an instrument: one named annotator with no independent second annotation, the annotations sit on a reduction, and they reached the repository through a machine translation

**As decided, in the words it was decided in:**

```
content to any existing analysis). **Unestablished as an instrument (#19):** annotator count/identity
and validation are UNKNOWN (the JEP:HPP Method section and the dataset zip's headers are the two places
that would settle it — the zip is fetch-blocked in this environment but downloadable on the user's
machine); the annotations sit on a homorhythmic REDUCTION (unit mismatch with our full-texture grading
must be handled in the measurement design); they reached the repo through a machine translation into
rntxt (Nápoles López), whose noise would be part of any measured disagreement. **Consequence:** the
```

**In plain words:** A second set of human chorale analyses is held, and it would be the natural way to measure how far two annotators disagree. It still cannot be trusted, and since 2026-08-11 one of the three grounds has changed rather than gone away: the annotating laboratory has now named its single annotator and stated that nothing was annotated independently, so there is no second reading inside this collection at all. The other two grounds are untouched — the analyses describe a simplified version of the music rather than the full texture, and they were converted automatically into our format, so the conversion's own errors would show up as disagreement.

---

## D-476 — The phrase-boundary primitive is owned by the notation-derived view layer — not by the note model, and not by the function layer that consumes it

**As decided, in the words it was decided in:**

```
- **D1 — Owner: Architectural Layer 1.5 (the notation-derived views).** The primitive is a notation-derived view, the same
  kind as the bass, top-voice, and spelling views, reading the same notated surface. *Rejected:* the Layer-1 note model
  (deliberately narrow — it records notes, it does not derive phrase structure) and the function layer (it consumes phrase
  boundaries; it cannot own them).
```

**In plain words:** Working out where a musical phrase ends is done by the same kind of component that reads the bass line or the written spelling off the page. It is not part of the plain record of the notes, and it is not part of the stage that detects cadences — because that stage uses phrase ends as input and cannot also produce them.

---

## D-477 — Phrase boundaries are read from the written surface alone — never from a resolved key, chord or cadence — and the boundaries this misses are accepted, not recovered here

**As decided, in the words it was decided in:**

```
- **Notation-only — key-, chord-, and function-agnostic.** A phrase boundary is read from the written surface (rests,
  durations, pitch intervals, metric position, annotations, barlines), never from a resolved key, a chord reading, or a
  cadence. This is structural: the function layer's cadence detection *consumes* phrase boundaries, so a boundary that
  depended on cadence would be circular. Cadence-based phrase refinement therefore stays a **function-layer** concern,
  downstream of this primitive (§6-D3). A known consequence (accepted): a surface-only primitive **systematically misses
  boundaries marked only harmonically** — a cadence with no surface gap — which the function layer recovers downstream.
```

**In plain words:** Phrase ends are found from what is printed: rests, note lengths, leaps, metric position, marks and barlines. Nothing about the key or the chords may enter, because the stage that detects cadences uses phrase ends, so a phrase end that depended on a cadence would be circular. The cost is accepted and stated: a phrase that is marked only by its harmony, with no gap in the surface, is missed here and picked up later.

---

## D-478 — A phrase boundary is a peak in a continuous boundary-strength profile, not the OR of a few binary signals

**As decided, in the words it was decided in:**

```
- **D4 — A graded boundary-strength model, not a binary union (user-ratified 2026-06-26).** The boundary is a peak in a
  continuous strength profile, not the OR of a few binary signals. *Rejected:* the binary union — a degenerate special
  case that cannot express "a gap larger than its neighbours," inflates recall, and wrecks precision (per the research: a
  weighted combination measurably beats any single cue and beats a naive union; the leading harmony-free models all
  compute graded strength + peaks). The cost — per-cue normalisation, the weight vector, the peak threshold — is modest
  and the constants are precision-phase.
```

**In plain words:** Rather than declaring a phrase end wherever any one signal fires, the program computes how strongly each moment is marked as an ending and then picks the peaks. The all-or-nothing version is the special case that cannot express 'a bigger gap than its neighbours', and it finds too many endings.

---

## D-479 — The boundary cues run per eligible voice and aggregate to the texture, and BOTH the per-voice and the texture boundaries are published

**As decided, in the words it was decided in:**

```
- **D5 — Per-voice cues aggregated to the texture (both per-voice and polyphonic), not a top-voice/whole-texture
  reduction.** The cues run **per eligible voice** and aggregate by **voice-coincidence** into the texture strength,
  exposing **both** the per-voice boundaries and the texture boundaries (§4.3). *Rejected:* (a) a whole-texture reduction
  with **top-voice-only pitch** — it discards every inner voice's pitch cue and yields no per-voice phrasing; (b) running
  the cues on one arbitrary voice — ill-defined in polyphony. Per-voice-then-aggregate is the principled form (the
  local-change cues are defined per line) and produces both outputs. Since the literature's cues are validated only
  monophonically, the aggregation is validated on our own corpus (§7).
```

**In plain words:** The signals that mark a phrase end are properties of a single melodic line, so they are computed for every voice separately and then added up across the voices. Where many voices phrase together the total is high; where one inner voice alone pauses it is low. Both answers are published: each voice's own phrasing and the whole texture's.

---

## D-480 — The phrase-boundary primitive is NOT an accuracy requirement — a competitive reference engine does no phrase segmentation at all — so it is built right but kept proportionate

**As decided, in the words it was decided in:**

```
- **★ Proportionality (scope discipline, user-ratified 2026-06-26).** The state-of-the-art-competitive reference
  engine (Contrapunctus) does **no** explicit phrase segmentation or cadence detection and is still competitive at Roman-numeral
  analysis (it captures phrase structure implicitly via stable key runs). So this primitive is **not** an accuracy
  requirement — it is load-bearing for *our* cadence mechanism (a means to key/function), a deliberate bet for an
  explainable, decomposed pipeline. **Build the graded model right, but keep it proportionate — do not let it balloon.**
  If the explicit phrase/cadence path proves hard, there is a proven implicit fallback (phrase-alignment via stable key
  runs). See `contrapunctus_findings.md` addendum and `cowork_phrase_boundary_methods.md`.
```

**In plain words:** A comparable system that performs as well as ours at Roman-numeral analysis has no phrase detection whatsoever; it picks up phrase structure indirectly. So this component is not what accuracy depends on. It is a deliberate bet on an explainable, decomposed design — worth building properly, not worth letting grow without limit, and there is a proven fallback if the explicit route proves hard.

---

## D-481 — The notated markers are emitted as boundaries unconditionally; only the surface-cue strength is peak-picked

**As decided, in the words it was decided in:**

```
The picked-boundary set is **the surface-cue peaks UNION every notated marker** — because the §4.2 markers are
**deterministic facts** (a fermata/barline/etc. *is* a phrase boundary), they are emitted **unconditionally**, not
subjected to the threshold; only the **surface-cue** strength is peak-picked. *(As-built realisation, ratified 2026-06-26:
the earlier wording "peak-pick the combined profile" put the markers through the local-maximum test, which a strict
greater-than rule drops for two **adjacent equal-height markers** — e.g. a final fermata abutting the closing barline.
Emitting markers directly is the faithful reading of their "deterministic / dominate wherever they occur" status.)*
```

**In plain words:** A fermata, a breath mark, a structural barline and the other written signs are facts, not evidence to be weighed — so each one is reported as a phrase end directly. Only the computed strength has to clear a local-maximum test and a threshold.

---

## D-482 — The two hand-synchronised copies of the fermata scan retire into one owned primitive, and that retirement changes no output

**As decided, in the words it was decided in:**

```
- **D2 — One unified primitive replaces the two duplicated fermata scans.** The fermata logic exists today in two
  hand-synchronised copies; they are retired into the single owned primitive and every consumer re-points at it. The
  retirement is byte-identical.
```

**In plain words:** The same fermata-finding code existed twice, kept in step by hand. Both copies are replaced by the single owned component and every consumer re-pointed at it. Because the marker-only behaviour is unchanged, the swap produces identical results — the new behaviour is a separate, measured step.

---

## D-484 — The phrase-boundary primitive is a derived view: it inherits the loaded span, requests no extension of its own, and publishes a per-profile max-normalised boundary confidence

**As decided, in the words it was decided in:**

```
- **A DERIVED VIEW: it inherits the loaded span and requests no extension of its own.** Where only a stretch of the
  score is loaded, this primitive does **not** ask for more music. Its profile simply **ends where the loaded span
  ends**. A consumer that wants boundary evidence beyond that stretch extends the span through **its own**
  bounded-context obligation, and this primitive then **recomputes over the enlarged span** — the standard re-run.
  *Why:* a derived view that reached for its own context would hold a second, independent extension policy beside its
  consumers' (#6), and its answer would then depend on which consumer asked.
- **Its published boundary strength is a per-profile MAX-NORMALISED confidence, comparable within ONE score's profile
  only, and it participates in NO override frame.** The number on the wire is a boundary confidence in the cross-layer
  contract's Class-M sense: it ranks ticks inside one score's own profile and says nothing across scores, and it never
  overrides another layer's answer. *Why:* the strength is a max-normalised salience rather than a probability, so two
  scores' values are not on one scale, and a quantity that cannot be compared across scores must not be given the
  authority to overrule one that can.
```

**In plain words:** When only part of a score is loaded, this component does not ask for more music. Its profile simply ends where the loaded stretch ends; a consumer that wants boundary evidence further out asks for the extension itself and this component recomputes. Its published strength is comparable only within one score's own profile — it never overrides another layer's answer.

---

## D-485 — Each picked boundary should carry which cue fired and at what scope; the picked set is scope-blind today and the refinement waits for the inference phase

**As decided, in the words it was decided in:**

```
**★ EVERY PICKED BOUNDARY CARRIES WHICH CUE OR MARKER FIRED, AND AT WHAT SCOPE — A REQUIREMENT ON THIS SECTION'S OUTPUT,
STATED AS OWED AND EXPLICITLY NOT BUILT.** A picked boundary — texture **and** per-voice — carries its **provenance**:
which cue or marker produced it, and whether it fired **globally** or **per voice** (and if per voice, which voices, and
how many coincided). **The picked set is SCOPE-BLIND today**, which is the defect this requirement names: a marker
written on one voice — a breath mark — is spiked onto the texture profile and thereafter reads exactly like a marker
that applies to the whole ensemble, so a downstream consumer (the punctuation-span annotation) cannot tell a **local
breath** from a **global barline**.
```

**In plain words:** The markers that produce a phrase end are of two kinds: some apply to the whole ensemble by notation (a structural barline), and some are written on one instrument (a breath mark). Today both are treated as whole-texture endings, so a local breath is promoted to a global boundary and the fact that it was local is lost. A boundary should record which signal produced it and at what scope — recorded as owed, and deliberately not built yet.

---

## D-495 — RATIFIED AMENDMENT A-5: when the phrase-boundary profile is flat, cadence admission relaxes with vote-weight scaling instead of starving

**As decided, in the words it was decided in:**

```
- **Cadence admission needs a stated FALLBACK for a FEATURELESS phrase-boundary profile: relax admission
  and scale the vote weight down, rather than starve.** Cadences are looked for at phrase ends,
  which this layer reads as a published L1.5 fact — the graded phrase-boundary profile. In music
  with almost no surface punctuation that profile goes featureless and everything gated on it gets nothing
  to work with. The required fallback admits cadences more freely there and weights their votes
  down by the graded strength the profile already carries. *Why:* derived from the review's stress
  simulation — in a punctuation-poor texture the fermatas, rests and structural barlines are
  deliberately absent, so the profile loses its contour and every phrase-gated consumer starves, while the
  graded profile still carries the relative signal a scaled admission needs. **The obligation is
  cadence admission's and therefore this layer's**; the profile it reads is the primitive's
  published output and the primitive's own contract is unchanged by it.
```

**In plain words:** Cadences are only looked for at phrase ends. In music with almost no surface punctuation the phrase-end signal goes flat, and everything that depends on it gets nothing to work with. The amendment requires a specified fallback: admit cadences more freely there but weight their votes down, using the graded strength that is already computed.

---

## D-496 — RATIFIED AMENDMENT A-6: whether the pairwise progression grammar lives inside the harmonic vocabulary or stays a separate store is decided at the recognition-consumer build, explicitly

**As decided, in the words it was decided in:**

```
- **Whether the pairwise progression grammar folds INTO this vocabulary or stays a SECOND store is
  a decision that is OWED, and its trigger is the recognition-consumer build.** Knowledge about
  which chord may follow which is currently held in two places — a pairwise rule set inside the
  function layer, and this catalog of longer patterns. The choice between one store and two by
  declared design **is not to be settled by drift**: it is made, explicitly, when the component
  that queries this catalog is built. *Why:* the consumer design already asserts that this
  vocabulary extends the pairwise grammar while the single-store-or-two decision is unmade, which
  is a total-unification question (#6) and exactly the kind of coexistence the review's own
  criterion says must be **decided** rather than tolerated. Stating the trigger rather than the
  answer is the point: no section can yet state a rule here, and what is owed is the choice.
```

**In plain words:** Knowledge about which chord may follow which is held in two places: a pairwise rule set inside the function layer, and a catalog of longer patterns. Whether these become one store or stay two is not to be settled by drift — the amendment requires the choice to be made, and made when the component that queries the catalog is built.

---

## D-497 — RATIFIED AMENDMENT A-7: the empirically-unvalidated mark must be APPLIED to the Jazz preset constants and the unvalidated idioms, with the validation path named

**As decided, in the words it was decided in:**

```
**Every style constant and every idiom that no ground truth has calibrated CARRIES THE
EMPIRICALLY-UNVALIDATED MARK, and the corpus that would validate it is named beside it (re-homed
into this specification 2026-08-07 on the user's ruling).** The verifiability contract already
defines that mark; this states where it must appear and what must accompany it. It applies to the
**Jazz preset constants** and to the **idioms of the §6.7 taxonomy for which no gate-grade ground
truth exists**, and the mark is not decorative: beside each marked value the record names **the
validation path** — the corpus class that would establish it. **Maintenance is part of the rule:**
a value keeps the mark until an established corpus measures it, and it loses the mark only in the
act that records that measurement, never by a value being changed or a preset being renamed.
*Why:* measured by the architecture review — calibration and validation are Baroque- and
Bach-heavy, the jazz preset and the non-classical idioms have no gate-grade ground truth, and the
mark defined in the specification was found absent from exactly those constants and presets. The
gap is therefore between a stated rule and its application, not in the rule, which is why what is
written here is the rule and its maintenance rather than a new criterion.
```

**In plain words:** The rule that says an unvalidated value must be marked as such already exists. The review found it was not actually applied to the constants only Baroque data has ever calibrated. The amendment requires the mark to be put on them, and the corpus that would validate each to be named alongside.

---

## D-498 — RATIFIED AMENDMENT A-9: a product stance is owed for output that is mostly uncertain, and for music outside the tonal vocabulary altogether

**As decided, in the words it was decided in:**

```
- **A-9 (from F-13, F-15). Write the product stance for dense abstention and out-of-domain input** (what the user
  sees; when the system says "this is outside my tonal vocabulary"). Product-level, small, prevents the honest-marks
  design from becoming a UX failure.
```

**In plain words:** The design deliberately says 'uncertain' rather than guessing. Nobody has decided what the user should see when most of a passage comes back uncertain, or what the program should say about music that is not tonal at all — where the right answer is to state that plainly rather than to produce a confident reading. The amendment requires that stance to be written.

---

## D-500 — The user ratified CORPUS EXPANSION at the architecture review: gate-grade jazz ground truth, chromatic material of the Wagner class, and more non-Bach, non-Baroque annotation generally

**As decided, in the words it was decided in:**

```
**★ THE SCOPE THE TIERS ABOVE IMPLEMENT IS ITSELF A USER RATIFICATION, AND IT IS STATED HERE RATHER THAN LEFT TO BE
INFERRED FROM THE LISTS.** At the 2026-07-02 architecture review the user ratified **CORPUS EXPANSION**: gate-grade
**jazz** ground truth, **chromatic material of the Wagner class**, and, in general, **more non-Bach, non-Baroque
annotated music**. That is what Tier G and Tier J are for. *Why:* the review's own findings F-7 and F-8 — calibration
and validation are Baroque- and Bach-heavy, with no gate-grade ground truth for the jazz preset or for the
non-classical idioms, and a chromatic stress corpus is named there as the measurement bed for the capability
amendments. **The entry rule above is NOT weakened by it, and the two are read together:** material arriving under
this ratification widens what the analysis is MEASURED against, it enters at research tier, and promotion of any of
it into a gate is the separate, deliberate re-baseline event that rule already describes.
```

**In plain words:** At the same review the user approved widening the material the program is measured against: real ground truth for jazz, hard chromatic repertoire, and in general more annotated music that is neither Bach nor Baroque.

---

## D-502 — The span a recognised named progression covers is called the progression-schema-span — the bare word 'sequence' is reserved for the harmonic sequence and 'progression' for the whole committed chord stream

**As decided, in the words it was decided in:**

```
- **D6 — what to NAME the span a recognised progression covers — RESOLVED BY PREFIXING (user direction, 2026-07-02):
  `progression-schema-span`.** The prefix answers the last collision standing: bare "schema" reads as *data* schema
  to any coder, while **"progression schema" is already this component family's own name** (this design and the
```

**In plain words:** The stretch of music covered by a recognised named progression needed a name. It is called the progression-schema-span. The two shorter names were rejected because each already means something else here: a *sequence* is a progression repeated at rising or falling transpositions, and *the progression* is the entire analysed chord stream.

---

## D-503 — The idiom mixture is DISCOVERED from the score and merely SEEDED by the user's preset, in three forward-only phases

**As decided, in the words it was decided in:**

```
The consumer holds a weight vector `w` with one weight per idiom. **`w` is DISCOVERED from the score, seeded by the
user's preference (user-ratified model, 2026-07-02), in three phases — forward-only, no loop:**
```

**In plain words:** How much weight each harmonic idiom carries is worked out from the music itself. The user's chosen preset only supplies the starting point, and the estimate moves away from it as recognised evidence accumulates. It runs in three passes that only ever feed forward, so nothing loops.

---

## D-507 — A catalog entry defined by its melodic or bass lines is recognised by its chord skeleton alone and carries a 'chords-only' mark, with its prior strength reduced

**As decided, in the words it was decided in:**

```
- **D7 — line-defined entries carry the "chords-only" mark** (§4.5) — the verifiability contract's explicit-mark
  path; the mark retires per entry when the voice-leading layer supplies the other half.
```

**In plain words:** Some named patterns are defined by their melody and bass lines as much as by their chords. This consumer can only see the chords, so it recognises such a pattern by its chord skeleton, marks the recognition as chords-only, and trusts it less. The mark comes off, per entry, when the voice-leading work supplies the other half.

---

## D-508 — The catalog/grammar consistency test ships scoped to the MEASURED containment — an explicit known-gap list — and tightens to a clean assertion when the grammar amendment lands

**As decided, in the words it was decided in:**

```
  silently un-license legitimate grammar). The **consistency test** ships scoped to the TRUE containment: every
  pair is licensed OR on the explicit 6-entry known-gap list (any 7th failure = red); when the grammar amendment
  lands, the list empties and the test tightens to the clean assert.
```

**In plain words:** The premise that every adjacent chord pair inside every catalog entry is licensed by the analysis's own grammar was checked and turned out to be false: a handful of entries exercise musically correct motions the grammar did not license. The test therefore ships allowing exactly those, and any further failure is an error. When the grammar is completed the allowance list empties and the test becomes the plain assertion it was meant to be.

---

## D-512 — Gate A becomes removable only once the unified promotion reproduces its carry byte-for-byte — that reproduction IS the retirement condition, not the winner-inertness that preceded it

**As decided, in the words it was decided in:**

```
- **The retirement condition for the separate Gate A rule is BYTE-FOR-BYTE REPRODUCTION OF ITS
  CARRY — not the winner-inertness that preceded it.** Once the flip is one promotion call with
  present-first branching, the former "partner present" and "partner absent" rules are two branches
  of the same promotion and the separate rule — its enum member, its guard, its name-map entry and
  its dedicated fixtures — is redundant. It is removable **because** the primitive reproduces the
  swap byte-for-byte on the present branch, which leaves winner AND carry byte-identical. *Why:*
  the condition is quoted from the earlier ruling it discharges — the rule retires when the
  promotion machinery unifies into one path producing one carry — and the design shows why the
  earlier winner-only inertness was **not** enough: the naive removal was inert on the winner
  across the whole corpus while changing the carry on a named subset of scores. That gap is exactly
  why this document's evidence rule is inertness on the **full** output surface, winner AND
  alternatives, and never the winner alone (#15).
```

**In plain words:** The rule could not simply be deleted: deleting it left the winner unchanged but changed the alternatives on a number of scores. It is removable once the shared promotion produces exactly the same alternatives, at which point exactly one rule name survives for the flip.

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

## D-535 — The checking stage's verdict: the real counted tables overturn no desk-simulation verdict, but margins moved in both directions and one margin expectation was plainly wrong

**As decided, in the words it was decided in:**

```
Across the three passages, no desk-simulation verdict is overturned by the real counted values, but
margins moved by 1.5–3.5 (log difference) in both directions, and one margin expectation was
plainly wrong. Catching exactly this — before any code exists — is what this checking stage is for.
```

**In plain words:** The three passages whose paper outcomes depended most on placeholder numbers were recomputed with the real counted ones. Every verdict held. The margins did not: they moved appreciably in both directions, and one prediction about a margin was simply wrong.

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

## D-569 — Collecting, filtering and weighting are THREE separate responsibilities; the collection layer collects and annotates, and does nothing else

**As decided, in the words it was decided in:**

```
## §1 — Intended role (the single responsibility) — REVISED per user review 2026-06-21
**Collect — and only collect — every sounding note in a region, annotated, losslessly, by ONE path.** It is the
boundary between the engraving model (Score/Segment/Note) and the analysis types. It answers exactly one factual
question: "for region `[startTick, endTick)`, what notes sound?" — and returns the **note set**, each note
annotated with the facts needed downstream (pitch, tpc/spelling, staff, voice, onset, offset, in-region
duration, `isGrace`, `plays`, `visible`, staff-eligibility). It must **NOT** filter (drop grace/non-playing/
invisible), **NOT** weight or aggregate into pitch-class evidence, **NOT** select a bass, and **NOT** make any
harmonic/segmentation/key decision. Those are *separate* responsibilities (see §5):
- **Collection** (this layer): the facts — every sounding note, annotated, preserved, one path.
- **Filtering** (a distinct, explicit decision): which annotated notes are eligible for harmonic analysis.
- **Weighting** (a distinct derived layer): the pitch-class evidence + bass, computed as a *view* over the
  collected notes — never replacing them.
```

**In plain words:** Finding out which notes sound in a stretch of music, deciding which of them the harmonic analysis should consider, and turning them into weighted evidence are three different jobs. The first is a matter of fact, the second a decision, the third an interpretation. The collection layer answers only the factual question and hands the notes on annotated with everything a later step could need.

---

## D-576 — The corpus root-agreement measurement UNDERSTATES the real-world quality impact of a wrong key, because root and bass are largely key-independent

**As decided, in the words it was decided in:**

```
A chord's root and its bass note are **largely
key-independent**: both can be named correctly while the key label is wrong. So the root-agreement
percentage barely moves when the tonality is misread — while the chord's **quality**, its **Roman
numeral** and some of its **inversions** are all corrupted by that same misreading. The corpus
measurement therefore reports **less damage than a reader or listener would see**
```

**In plain words:** A chord's root and its lowest note can both be named correctly while the key is wrong. So a measurement built on root agreement barely moves when the tonality is misread — but the quality of the chord, its Roman numeral and some of its inversions are all corrupted. The measurement therefore reports less damage than a listener or reader would see.

---

## D-584 — The perfect/imperfect cadence call is made on the BASS-DERIVED inversion; the soprano arrival degree is demoted to a soft optional nudge and the tool never attempts melody identification

**As decided, in the words it was decided in:**

```
- **The perfect/imperfect cadence call is made on the BASS-DERIVED INVERSION; the soprano arrival
  degree is a soft optional nudge and this layer never attempts melody identification (D-584).**
  Standard theory decides a full close from the melody note, and this layer may not: the highest
  sounding voice is often a doubling, and in some textures the lead sits below the top, so the
  structural melody the criterion needs is not reliably recoverable. The top voice may nudge the
  confidence in a chordal texture; it never decides. *Why:* the constraint that forces it is the
  unavailability of the structural melody — orchestral doubling and a lead below the top are the two
  cited counter-cases — and the bass-derived inversion criterion is chosen because the catalog
```

**In plain words:** Whether a cadence is a full close or a weaker one is decided from the bass and the chord's inversion, not from which note the melody lands on. Standard theory uses the melody note, but the program cannot reliably tell which line is the melody: the highest sounding voice is often a doubling, and in some music the lead sits below the top. The top voice may nudge the confidence in a chordal texture; it never decides.

---

## D-587 — A user-facing preset presents as a familiar genre-era label plus exemplars the user knows — never as an idiom name or an obscure exemplar; genre names are LABELS over mixtures, never axes

**As decided, in the words it was decided in:**

```
- **A preset presents as a familiar genre-era label plus exemplars the user knows — never as an
  idiom name and never as an obscure exemplar; genre names are LABELS over mixtures, never axes.**
  A preset is named after a period and style a user recognises, anchored by musicians they know
  ("60s pop — The Beatles"); it is never named after one of the five idioms, and never after an
  exemplar most people have not heard of. *Why:* the second half is measured and is §6.7's own
  result — harmony is not organised by genre, and Baroque, galant and Classical share one idiom —
  so a genre name cannot be an axis without asserting a structure the data denies. The exemplar half
  is the user's own reason: an exemplar nobody recognises conveys nothing.
```

**In plain words:** What a user picks is named after a period and style they recognise, anchored by musicians they know. It is never named after one of the five structural idioms, and never after an exemplar most people have not heard of. The genre name is only a label for a blend of idioms — genre is not one of the things the analysis is organised by.

---

## D-588 — Preset coverage beyond the analysed corpora is three tiers with NO bare guessing — measured, editorially declared with a stated theory rationale, or self-correcting by detection

**As decided, in the words it was decided in:**

```
- **Coverage beyond the analysed music is three tiers with NO bare guessing — measured, editorially
  declared with a stated theory rationale, or self-correcting by detection.** A style we hold
  annotated music for gets its mixture measured from that music. A style we hold none for gets a
  mixture written down deliberately with its theory reason stated, and validated when data arrives.
  Either way the analysis moves away from the starting mixture as it reads the actual music. *Why:*
  the third tier is what licenses the second — because a preset is only a cold-start prior the music
  itself refines, a declared mixture that is somewhat wrong degrades gracefully; without the
  self-correction the declared tier would be an unvalidated shipped value (#19).
```

**In plain words:** A style we hold annotated music for gets its blend measured from that music. A style we hold none for gets a blend written down deliberately, with the theory reason for it stated, and checked when data arrives. Either way the analysis moves away from the starting blend as it reads the actual score, so a badly chosen preset degrades gently rather than being wrong throughout.

---

## D-589 — Every idiom mixture is selectable and the discovered cloud is the EVIDENCE MAP, not the boundary — each chosen point carries its evidence status

**As decided, in the words it was decided in:**

```
- **Every idiom mixture is selectable, and the discovered cloud is the EVIDENCE MAP rather than the
  boundary — each chosen point carries its evidence status.** Named presets are cluster centroids
  for progressive disclosure; a custom selector admits any point in the mixture space. Where the
  chosen point sits relative to the music actually measured decides what may be claimed about it:
  inside a discovered cluster it is validated, between clusters it is an interpolation, outside the
  cloud it is still selectable but marked empirically unvalidated. *Why:* two standing rules
  combined — no information loss (#12), since restricting the user to the discovered centroids would
  discard every point between them, and the empirically-unvalidated mark, which lets a value outside
  the measured range be offered without being presented as established (#19).
```

**In plain words:** A user may set any blend of the five idioms, not only the named ones. Where the chosen blend sits relative to the music we actually measured decides what may be claimed about it: inside a measured cluster it is validated, between clusters it is an interpolation, and outside everything measured it is still selectable but is marked as never having been checked against real music.

---

## D-590 — The score's own metadata is the PRIMARY home of that score's idiom mixture, and a user-set mixture is never silently overwritten by re-detection

**As decided, in the words it was decided in:**

```
- **The music's own metadata is the PRIMARY home of that piece's idiom mixture, and a user-set
  mixture is never silently overwritten by re-detection.** The mixture is stored in the score's own
  user-defined properties, the mechanism MuseScore already saves beside title and composer, so it
  travels with the file and a later analysis starts warm rather than cold. The stored value records
  its provenance — auto-detected, with the analyzer version and date, or user-set: a user-set
  mixture is never silently replaced, an auto-detected one may be refreshed, and an edit after
  detection marks the stored mixture refreshable. *Why:* storing it with the music removes the need
  for a separate registry for per-piece behaviour and turns re-analysis into a warm start; the
  no-silent-overwrite half is the no-surprise rule. **Two things are recorded rather than assumed
  away:** custom properties survive the native format but their MusicXML round-trip is only partial
  and needs its own check before the feature relies on it; and the property layout is an
  implementation decision at build time. **This sits against §13.1's rule that our data lives in
  separate files inside the archive and the score file is never touched** — the two are not in
  conflict on their own terms, since this uses MuseScore's existing property mechanism rather than
  extending the file's own schema, but a build must reconcile them explicitly and neither record
  does.
```

**In plain words:** A piece's blend of idioms is stored inside the piece's own file, using the score properties MuseScore already saves beside title and composer. So it travels with the file and a later analysis starts warm instead of cold. The stored value records whether a person set it or the program detected it: a person's setting is never quietly replaced, a detected one may be refreshed, and editing the score marks it as due for refresh.

---

## D-591 — The licence split for the style system: the ANCHORS are the shipped licence-constrained fitted parameters, and the mixture weights are free user configuration

**As decided, in the words it was decided in:**

```
- **The licence split: the ANCHORS are the shipped licence-constrained fitted parameters, and the
  mixture weights are free user configuration.** The constraint that a value which SHIPS may be
  fitted only on freely-licensed music reaches the per-idiom anchors, not the mixture a user chooses
  over them; a user's own mixture carries no constraint at all, and only the mixtures we ship as
  named preset defaults must be derived from a licensed pool or editorially declared. *Why:* it
  follows from what each half is — an anchor is a fitted parameter compiled into the product, so the
  fitting-pool constraint reaches it, while a mixture weight the user selects is configuration
  derived from no corpus at all. This REFINES the fitting-pool constraint by saying which half of
  the style system it reaches; it does not weaken it.
```

**In plain words:** The licensing rule that limits which music our shipped numbers may be fitted on applies to the per-idiom reference values, not to the blend a user chooses over them. A user's own blend carries no constraint at all; only the blends we ship as named defaults must come from freely-licensed music or be declared editorially.

---

## D-598 — The style taxonomy and the per-style weights are ONE data-derived object; VALIDATION is a separate third thing that needs annotated scores and is not delivered by the clustering

**As decided, in the words it was decided in:**

```
- **The taxonomy and the per-style weights are ONE data-derived object; VALIDATION is a separate
  third thing the clustering does not deliver.** Discovering which idioms exist and estimating how
  strongly each one weighs are not two derivations: the clusters and their feature distributions
  are the same object read two ways. Measuring whether the analysis actually improves when it uses
  an idiom is a THIRD job, and it needs annotated music — notes together with a published human
  analysis — which the clustering does not supply. *Why:* it follows from what a cluster is, so no
  second derivation produces the weights; and the separation is forced by what validation measures,
  the analysis's USE of an idiom, which cannot be observed without a human analysis to compare
  against.
```

**In plain words:** Discovering which styles exist and measuring how strongly each one weighs are not two jobs — they are the clusters and their distributions, one result. Checking whether the analysis actually gets better when it uses a style is a third, separate job, and it needs music with both the notes and a published human analysis, which the clustering does not supply.

---

## D-601 — Before any constant that would make two differently-scaled confidences comparable is fitted, the premise that a fitted constant CAN do so must itself pass a premise ledger and a desk simulation

**As decided, in the words it was decided in:**

```
The `conversion`
element of a frame is where two numbers on different scales are made comparable — one bounded, one an unbounded
sum — and fitting the constants that perform it is **hard-gated**: the premise *"a fitted constant CAN make these
scales commensurable"* is itself a load-bearing causal claim and goes through the #17 ledger and desk simulation
BEFORE the fit, not as part of it.
```

**In plain words:** Two confidence numbers in the program are on different scales — one runs from zero to one, the other is an unbounded total — and a comparison between them treats them as the same kind of quantity. Fitting a conversion factor is not allowed to be the first move: the assumption that any single factor could make the two comparable has to be written down as a premise and traced by hand first, because the one attempt at such a calibration did not behave monotonically.

---

## D-613 — Ground truth for IMPLIED polyphony is confirmed ABSENT — do not re-search it

**As decided, in the words it was decided in:**

```
**Negatives (do not re-search):** implied-polyphony GT over monophonic instruments — CONFIRMED ABSENT
(VoiSe 2005 and Gray & Bunescu's perceptual-stream pop corpus were never released; VISA excerpt sets not
public; Chew&Wu/Guiomard-Kagan reused notated voices).
```

**In plain words:** For music where several lines are implied by a single melodic instrument, no published collection of correct line assignments exists — every candidate was either never released or simply reuses the voices the engraver wrote. The absence is the finding, and the record says so rather than leaving the search open.

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

## D-625 — Spelling presence is tested with the validity predicate, never with a non-negative test — the flat side of the line of fifths is negative and a non-negative guard silently drops it

**As decided, in the words it was decided in:**

```
- **Spelling presence is tested with the VALIDITY PREDICATE, never with a non-negative test.** The
  shared line-of-fifths primitive the spelling-pin above reads — the one interpreter, not a
  per-layer copy — represents a spelling as a signed position on the line of fifths, and its
  presence test is `tpcIsValid()`, **never** `tpc >= 0` and never `tpc != -1`. *Why:* established
  at the source rather than asserted — the flat side of the line of fifths is **negative** (down to
  the triple-flat spellings), so a non-negative guard silently discards every heavily flattened
  spelling; and the value a `!= -1` guard treats as absent is itself a **legitimate** spelling. The
  honest bound is recorded with the rule: the validity test cannot tell a real flattest spelling
  from a default-initialised field, and what actually keeps an absent value out is the build-path
  invariant, not this predicate. §5.14, which specifies the enharmonic disambiguation this
  primitive serves, points here and does not restate it (#6).
```

**In plain words:** How a note is spelt is stored as a position on the line of fifths, and that position is negative for the flattest spellings. Code that checks whether a spelling is present by testing for a non-negative number therefore throws away every heavily-flattened spelling — including one that happens to share its number with the field's empty value. The validity test is the correct check.

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

## D-665 — What a voice/stream label set actually MEASURES is said at intake — the labels obtainable today come from engraved notation, not from a listener's judgment

**As decided, in the words it was decided in:**

```
4. **What a voice/stream label set actually MEASURES is said at intake** (user-ruled 2026-08-09) — the
   voice labels obtainable today are derived from **engraved notation**, not from a listener's
   judgment about heard lines, and the intake record says so in those terms.
```

**In plain words:** When a collection of per-note voice labels is taken in, the record states where those labels came from: they are read off the way the music was written down, not off what a listener hears as separate lines. For keyboard music the two are close enough that the field works with the engraved version, and that acceptance is recorded too rather than left unsaid.

---
