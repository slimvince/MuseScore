# The ratified design intent — the entries this pack admits for this subject

This file is GENERATED. It carries the entries of the `DESIGN-INTENT` class of the rulings sort — the decisions the record sorts as ruled design intent rather than as management of the implementation — LESS the family withheld for this subject.

Four fields per entry and no others: the identifier, the title, the decision in the words it was decided in, and its plain restatement. Where a decision is recorded, what defends it, what its status came from and the words a search finds it by are all deliberately absent: each of those names a place or a fact in the implementation's own documents, which this pack does not carry.

Entries are in identifier order. An identifier missing from the run is not an error and is not a gap in the record: it is either outside this class or withheld for this subject, and this pack does not say which.

---

## D-001 — Key, mode and chord are inferred by ONE joint decode

**As decided, in the words it was decided in:**

```
Key, mode, and chord are inferred by ONE probabilistic decode
> over `(tonic, mode, chord)` with segmentation as a modeled (semi-Markov) variable and every enumerated clue
> as a theory-grounded factor
```

**In plain words:** The tonality, the major/minor character and the chord are not worked out one after another. They are worked out together, in a single pass that also decides where one chord ends and the next begins.

---

## D-002 — The fitted tables and weights are compiled into the binary verbatim

**As decided, in the words it was decided in:**

```
compiles the five committed artifacts + the selected weight vector
> VERBATIM (JSON bytes, not a parsed-structure codegen) into the generated `jointembeddedartifacts.{h,cpp}`
```

**In plain words:** The numbers the estimator was trained on are built into the program at compile time rather than read from disk at run time, so a running copy cannot quietly disagree with the numbers we published.

---

## D-003 — Inference is preset-independent; presets are presentation concerns

**As decided, in the words it was decided in:**

```
Inference is **preset-independent** (presets are
> presentation concerns)
```

**In plain words:** Choosing the Baroque, Jazz or Default preset changes nothing about what the estimator concludes; it changes only how the result is shown.

---

## D-005 — The joint estimator is the production inference layer on the batch and corpus surface

**As decided, in the words it was decided in:**

```
the joint estimator
> is now the PRODUCTION inference layer on the batch/corpus surface
```

**In plain words:** Everything the measurement corpus is graded on now comes from the joint estimator, not from the older chord-by-chord pipeline.

---

## D-010 — The switch - the record path is the production in-app notation analysis

**As decided, in the words it was decided in:**

```
flipped `useJointNotationRecord`'s default to **ON**.
```

**In plain words:** Since 27 July 2026 the harmony you see inside the program is produced by the joint estimator. The old path is still compiled in but is only reachable by explicitly turning the new one off.

---

## D-022 — The founding principle - analyse at the finest grain, coarser views are derived

**As decided, in the words it was decided in:**

```
**The founding principle: analyze at the finest grain where harmony is well-defined, and make everything coarser a
*derived view*.**
```

**In plain words:** The analysis works on the smallest stretch over which the sounding harmony does not change. Phrases, key areas and sections are then read off that, never analysed directly.

---

## D-023 — The atomic analysis unit is the constant-sonority slice, never the metric beat

**As decided, in the words it was decided in:**

```
The atomic analysis unit is the **constant-sonority slice** (L2), never the metric beat
```

**In plain words:** The smallest thing analysed is a stretch during which exactly the same notes are sounding - not a beat of the bar.

---

## D-024 — The fact layers are style-agnostic; style lives only in calibration

**As decided, in the words it was decided in:**

```
L1 (notes) and L2 (slicing) are **style-agnostic and
  lossless** — they carry facts, never style. Style-specificity lives **only** in the *calibration* of the judgment
  layers (their priors/weights), **never in structure**.
```

**In plain words:** Reading the notes and cutting the music into constant-sound stretches works the same for every kind of music. Whether a piece is Baroque or jazz can change only the numbers the judging layers use, never the shape of the code.

---

## D-025 — Forward-only, with two scoped escapes

**As decided, in the words it was decided in:**

```
The **ratified** architecture (user-ratified;
`cowork_target_architecture.md` §2) is **forward-only**:
```

**In plain words:** Each stage was to pass its answer forward and never reach back. A confident earlier answer could be overturned only by re-running that one stretch forwards, and the one genuinely tangled key-versus-chord case got a narrow, gated exception.

---

## D-026 — The global joint-lattice decode was measured inert (2026-06-29)

**As decided, in the words it was decided in:**

```
The subsequent investigation
**measured the full joint cross-layer search INERT**
```

**In plain words:** An earlier plan to search all the possibilities at once was tested and found to add nothing, so the effort was redirected into better evidence flowing forwards.

---

## D-027 — Every layer emits ranked candidates plus a confidence, never a forced point estimate

**As decided, in the words it was decided in:**

```
each layer is feed-forward and emits **ranked candidates + a confidence**, never a forced point estimate;
```

**In plain words:** No stage is allowed to report only its single best answer. It reports the runners-up too, with a measure of how clear-cut the choice was.

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

## D-033 — Each layer owns one evidence-source-times-question contribution and uses all of L1's information

**As decided, in the words it was decided in:**

```
each layer owns one *(evidence-source × question)*
  contribution — stated as "owns the *[named evidence]* contribution to *X*", with what it does **not** own made
  explicit — defers what needs later evidence (carried as ranked alternatives + an uncertain mark), and within its scope
  uses *all* the information L1 carries losslessly (notated spelling, metric weight, voice).
```

**In plain words:** Each stage owns one contribution and says plainly what it does not own, handing unresolved cases forward as ranked options. Owning one contribution does not narrow what it may look at: within its scope it uses all the information the note reader carries - how the note is spelt, where it falls in the bar, and which voice it is in.

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

## D-057 — The priority of evidence - actual sounding notes are the strongest evidence

**As decided, in the words it was decided in:**

```
| Strongest | Actual sounding notes | what is literally happening now |
```

**In plain words:** In deciding the key, what is actually sounding right now outranks the surrounding bars, which outrank the printed key signature, which outranks the major/minor tag on it.

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

## D-096 — Fitted values are fit once against ground truth, never per-case tuned

**As decided, in the words it was decided in:**

```
**(a) Factor FORMS come from theory; factor VALUES are fit ONCE against ground truth and are never tuned
per case.** Every factor's shape is derived from established music theory before any number is attached to
```

**In plain words:** The shape of each piece of evidence comes from music theory. Its numerical strength is learned once from annotated music, and never adjusted to make a particular passage come out right.

---

## D-099 — Negative evidence is information - a ruled-out possibility is carried, not dropped

**As decided, in the words it was decided in:**

```
**Negative evidence is information — a ruled-out reading is carried, not dropped.** A layer that
eliminates a reading publishes the elimination rather than discarding it: the ruled-out reading is
carried on the output surface at low confidence, unless the elimination is recomputable from what that
```

**In plain words:** Knowing that something is not the case is itself useful. A reading that has been ruled out is kept at low confidence rather than thrown away, unless we could work out the exclusion again from what we did keep.

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

## D-114 — The decoder commits its best path; there is no abstention on the key axis

**As decided, in the words it was decided in:**

```
**(d) On the key axis the decoder commits its maximum-a-posteriori path; it never abstains.** The estimator
always names a key for every committed segment, so the abstention counter the regression stop reads is
```

**In plain words:** The joint estimator always names a key. It never declines to answer on the key axis, so the abstention counter is always zero.

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

## D-207 — The pedal-point class is defined voice-independently, superseding the bass-only fact

**As decided, in the words it was decided in:**

```
**The pedal-point class is defined VOICE-INDEPENDENTLY (user-ratified 2026-07-26; DEFERRED to its own
increment).** The ornament vocabulary carries a **pedal-point** class: a tone sustained — or continuously
restruck — against changing harmony in **any** voice, sub-labeled by position as **bass**, **internal**, or
**inverted**. This class supersedes the legacy bass-only pair of published facts, `isPedalPoint` and
```

**In plain words:** A pedal point is a note held - or struck again and again - while the harmony changes around it, in ANY voice, not only the bass. It is labelled by where it sits: in the bass, inside the texture, or above it. This replaces the older fact, which could only see a pedal in the lowest voice.

---

## D-220 — The augmented-seventh guard requires both the major third and the augmented fifth

**As decided, in the words it was decided in:**

```
- **B2 aug7 guard requires BOTH M3 and aug5** (`||` not `&&`). M3-only was
  tried and reverted (Schumann D-major, Corelli G-major snapshot flips).
```

**In plain words:** The guard fires only when both intervals are present, not when either one is. Requiring only the third was tried and reverted.

---

## D-221 — A sparse upper-register lowest note does not earn inversion bonuses

**As decided, in the words it was decided in:**

```
- **`hasStructuralBass` gates inversion bonuses.** Sparse upper-register
  "bass" notes do not get inversion bonuses (Corelli op01n08d m2 b3).
```

**In plain words:** A low note that is thin and high in the texture is not treated as a structural bass, so the bonuses that reward a recognisable inversion do not fire for it.

---

## D-222 — If the diminished bonus rotates the winner to a non-diminished chord, the result without it is used

**As decided, in the words it was decided in:**

```
- **Post-bonus winner quality guard for `w_dim`.** The bonus can rotate the
  global winner across bass candidates; if the post-bonus winner is not
  Dim/HalfDim, fall back to the without-wDim variant.
```

**In plain words:** The bonus that favours diminished readings can, in the course of comparing bass notes, end up electing a winner that is not diminished at all. When that happens the analysis falls back to the answer it had before the bonus was applied.

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

## D-224 — Joint bass-and-chord scoring requires accumulated regional evidence

**As decided, in the words it was decided in:**

```
- **Joint scoring requires regional accumulation.** `jointScoringEnabled`
  fires only when at least one tone has `onsetAtRegionStart == true` or
  `distinctMetricPositions > 0` (i.e. came from `collectRegionTones`).
  Single-tick / status-bar / unit-test paths use the legacy single-bass path.
```

**In plain words:** The scoring that considers the bass note and the chord together only switches on when the notes came from accumulating a whole stretch of music. The single-moment paths - the status bar, a unit test - use the simpler single-bass scoring.

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

## D-271 — The capacity budget - a cell keeps its own estimate only above a stated count, and free parameters are bounded against the training tokens

**As decided, in the words it was decided in:**

```
   table, its dimensions, its raw cell-count histogram from the training data, and the resulting free
   parameter count. No prose-only budget.
2. **Budget rule:** a table cell keeps its own maximum-likelihood estimate iff its training count
   ≥ 20 [prov-ratify]; below that it is pooled to its declared parent class (the pooling hierarchy
   declared per table in the artifact) under additive smoothing with a single declared α per table.
   The degree vocabulary's rare-class pooling (factorization §1) is the same rule applied to the state
   space itself.
3. **Global sanity bound:** total effective free parameters ≤ training tokens / 10 [prov-ratify],
   verified in the artifact. The combination-weight vector stays ≤ 14 weights, L2-penalized, per the
   ratified staged-fitting decision. *(Amended ≤ 12 → ≤ 14 by user ratification 2026-07-19 at the
   weight-fit dispatch: the ratified factorization gives the four cadence features their own fitted
   weights, putting the enumerated vector at 12–13; the amendment is the lawful #22 path — capacity
   impact nil, thousands of training tokens per weight either way. Original text: "≤ 12 weights (one
   per factor plus the declared-mode strength)".)*
```

**In plain words:** Before any fit, the parameter inventory is published as a generated artifact: every table, its dimensions, its raw cell-count histogram and its resulting free-parameter count. A table cell keeps its own maximum-likelihood estimate only if its training count reaches twenty; below that it is pooled into its declared parent class under smoothing. Total effective free parameters stay at or below one tenth of the training tokens, and the combination-weight vector stays at or below fourteen weights with a penalty.

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

## D-276 — Modal colour is published as un-rounded per-degree counts; no mode label is inferred or published anywhere

**As decided, in the words it was decided in:**

```
For each key run and each scale degree 1..7 of its key: the sounding duration and onset count of
EVERY chromatic inflection of that degree actually observed in the run (computed from the
published L1 note facts relative to (tonic, mode)). This is the whole publication — counted,
un-rounded, nothing hand-set: minor's variable 6̂/7̂ (Dorian color, subtonic-vs-leading-tone),
major's lowered 7̂ (Mixolydian color) or raised 4̂ (Lydian color), and every borrowing appear as
their actual counts. The presentation layer may FORMAT a reading from it ("Dorian-leaning"); the
published fact is the counts, with establishment status (§5.4). No 21-value mode label is
inferred or published anywhere (C1); the two-mode key plus this table informationally dominates
the retired labels (#12).
```

**In plain words:** For each key run and each scale degree, the record publishes the sounding duration and onset count of every chromatic inflection of that degree actually observed. That is the whole publication - counted, un-rounded, nothing hand-set - so minor's variable sixth and seventh, major's lowered seventh or raised fourth, and every borrowing appear as their actual counts. A presentation layer may format a reading from it; no twenty-one-value mode label is inferred or published.

---

## D-278 — The joint key-and-chord step is SHELVED - measured not to pay

**As decided, in the words it was decided in:**

```
precision gain is measured read-only **before** it is built, exactly as the joint step was. **The joint key↔chord
step is SHELVED — measured NOT to pay** (arc #12: net +0.05–0.16 pp over ~6200 regions, harm 75–90 % of
correction, oracle ceiling +0.6 pp, coupled-minority net ~0, fire-rate only 1.4 % — the carried alternative
keys are diatonic-collection siblings so the chord is almost always key-stable). It **drops off the Stage-3
build inventory.** The #12 reconciliation (no loss): the key alternatives ARE carried (the key discovery is not
discarded); the chord under an alternative key is **never computed** in this path (so nothing computed is
discarded), and the measurement shows the ~1.4 % where it would differ is 50/50 noise — choosing not to compute
a *measured-worthless* possibility is an evidence-based decision, not information loss. **Distinction:** this
gate applies to **precision claims** ("will building X make analysis more correct?" — measure first); the
**structural refactors** (decoder-replaces-tangle, the migrations) are justified by cleanliness and verified
```

**In plain words:** The separate joint key-and-chord decision was measured before being built and does not pay: about a tenth of a percentage point net over roughly 6200 stretches, with harm at three quarters to nine tenths of the correction, an oracle ceiling under a percentage point, and a firing rate of 1.4 per cent. The cause is that the carried alternative keys are siblings within one collection, so the chord is almost always stable across them. It drops off the build inventory. DEPRECATION MADE EXPLICIT (user, 2026-08-02): the shelved step's subject is deprecated legacy-era machinery, to be entirely discarded with the legacy path at the retirement map; the shelving binds that class only and does not bear on the joint estimator (D-001), a different mechanism class.

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

## D-280 — Gates read structured fields only - never a chord symbol string and never a Roman numeral

**As decided, in the words it was decided in:**

```
1. **A gate or scoring rule reads STRUCTURED FIELDS ONLY — never a chord-symbol string, never a
   Roman numeral.** No chord-symbol string parsing and no Roman-numeral inference anywhere in a
   gate, a scoring term, or any future change to either. *Why:* stated with the rule — signals
   derived from a symbol or a Roman numeral are lossy and entangled with the formatter, so they are
   not reliable inputs to chord classification; and reading the rendered form back in would make
   the analysis depend on its own presentation layer, which is the one direction this boundary
```

**In plain words:** Any gate or scoring rule reads structured analysis fields. It never parses a chord-symbol string and never infers from a Roman numeral. Signals derived from symbols or Roman numerals are too lossy and too entangled with the formatter to be reliable inputs to chord classification.

---

## D-282 — Meta-finding: the oracle/tier metric, never a bare proxy - superseded by the robust-unit stop and the two-tier policy

**As decided, in the words it was decided in:**

```
- **Oracle/tier metric, never a bare proxy** (BIR rewards wrong-root=bass). Make the dual metric standing.
```

**In plain words:** Never grade the analysis on the bare bass-is-root number, which rewards a wrong chord root that happens to be the bass; use the oracle-checked, tiered measurement. Its content became standing through the robust-unit regression stop and the two-tier class policy.

---

## D-283 — Meta-finding: never learn keys, the lever is keychain structure - superseded by the joint estimator and the forms-from-theory rule

**As decided, in the words it was decided in:**

```
- **Never learn keys; the lever is keychain structure (cadence precision).** Settled from both sides.
```

**In plain words:** A rejection of a learned key detector in favour of structural levers, cadence precision above all. Whichever reading was intended, the later explicit ratifications govern: the joint estimator infers the key inside a theory-declared generative form whose factor values are fitted once against ground truth, and its cadence factor carries the structural insight forward. This finding binds nothing the current design does.

---

## D-284 — Meta-finding: selection/competition is saturated, stop adding re-ranking gates - superseded by the gates doctrine and the adoption

**As decided, in the words it was decided in:**

```
- **Selection/competition is saturated** — stop adding re-ranking heuristics/gates; the residual is
  candidate-generation, key-quality, or floor.
```

**In plain words:** Stop investing in the legacy scorer’s gate and re-ranking surface; the remaining error lives in candidate generation and key quality. The doctrine lives on generalized in the ratified accumulating-gates rule, and the mechanism it warned about was retired wholesale when the joint estimator replaced the legacy selection surface.

---

## D-285 — Meta-finding: embellishment is chord-first, never a richer vocabulary - absorbed by the emission design and the ornament-label increment

**As decided, in the words it was decided in:**

```
- **Embellishment = chord-first** (segmentation + NCT post-process), never union re-derive / richer vocabulary.
```

**In plain words:** Ornamental tones are handled by classifying them against the committed chord - segmentation first, then a non-chord-tone post-process - never by widening the chord vocabulary until every embellishment is a chord. The ratified factorization’s emission carries exactly this shape (chord-member and non-chord-tone categories), and the ornament-label publication is its own ratified increment.

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

## D-288 — Beam widening is SHELVED - a wider search cannot fix the failure class it was proposed for

**As decided, in the words it was decided in:**

```
**Do not retry widening the search to consider more candidate readings in parallel.** *Why:*
> derived and then cross-checked against independent earlier measurements — the failure it was proposed for
> is not a search failure at all. **The wrong reading is the highest-scoring one**, so examining more
> readings finds the same wrong answer; only changing how readings are scored, or cutting the music
> differently, can move it.
```

**In plain words:** Searching more candidate readings in parallel was withdrawn. The failure it was meant to fix is not a search failure: the wrong reading is the highest-scoring one, so looking at more readings finds the same wrong answer. Only changing how readings are scored, or cutting the music differently, can fix it.

---

## D-289 — Meta-principle: precision lives in the evidence and the functional labelling, not in the search

**As decided, in the words it was decided in:**

```
  correct key never rank-2 in 51.6% of S2) — unrecoverable by any path. **SECOND
  falsified structural fix → META-PRINCIPLE recorded in roadmap: precision lives in
  emission + functional labeling, NOT search/path.** The HMM path is the least valuable
  part of Stage 4 (~10%); KeyArea spans + the key-EMISSION fix are what deliver.
```

**In plain words:** Three independent investigations converged on one rule: accuracy is gained by improving what evidence each reading is judged on and by labelling harmonic function better - not by searching harder over the readings already on the table. The rule is SUPERSEDED as an entry: every part of it is stated by a later decision that is written into a specification, so it is recorded here and homed nowhere, which is what keeps one rule in one place.

---

## D-291 — The tonicization labeller is NOT wired - wiring it would raise the reported agreement while hiding a real key error

**As decided, in the words it was decided in:**

```
**★ THE TONICIZATION LABELLER IS DELIBERATELY LEFT UNWIRED, AND THE REAL LEVER IS AT THE KEY LAYER
(2026-06-14; the record states no ratifier for the decision itself. Written into this section
2026-08-09 on the user's ruling — the BUILD half of register entry **D-291**, whose measurement half
belongs to the grading conventions and is not restated here, #6).** A working labeller for applied
chords exists and **must not be wired on the ground that it raises Roman-numeral agreement**.
```

**In plain words:** A working labeller for applied chords was deliberately left unwired, and the proposal to make the accuracy measurement treat its labels as equivalent to the annotator's was rejected. Both would have raised the reported Roman-numeral agreement while the underlying reading stayed wrong: the annotator has changed key, and labelling the chord relative to the old key hides that.

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

## D-293 — Fitted values are fitted per IDIOM, never for a user preset; presets are regression surfaces and delivery carriers

**As decided, in the words it was decided in:**

```
> **(f) Values are fitted per IDIOM, never for a user preset.** One fit event per musical idiom — a body of
> repertoire sharing a practice — and no value is ever adjusted to make a named preset come out right. A
> preset is a regression surface and a carrier for delivering a fitted set; which presets an end user should
```

**In plain words:** Numbers are fitted once per musical idiom - a body of repertoire that shares a practice - and never tuned to match one of the program's named presets. A preset is a way of delivering a set of values and a surface to check for regressions; which presets a user should see is a separate product question, decided later.

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

## D-306 — The key layer's backward re-reading stays switched off in the shipped configuration

**As decided, in the words it was decided in:**

```
**The backward re-reading facility stays SWITCHED OFF in the shipped configuration.** This layer carries a
facility for returning to an earlier stretch and re-reading it once later evidence has arrived
(`ReachBackOptions`). It is built, and `enabled = false` is the shipped default; turning it on is reopened
```

**In plain words:** The key analysis has a facility for going back and re-reading an earlier stretch once later evidence arrives. It is built but switched off, and turning it on is reopened only when a specific piece of evidence has been gathered.

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

## D-317 — The backward-walk boundary change is a dead end — do not retry it

**As decided, in the words it was decided in:**

```
- **Do not retry the backward-walk boundary change.** Counting notes that stop exactly where a
  stretch begins as belonging to that stretch was tried, in the hope of recovering a missing chord
  root. *Why it is closed:* measured — the notes touching the boundary are OTHER chord tones and the
  root attacks later, so the change would add the wrong pitches and still not add the missing one;
  and the same backward walk serves a dozen call sites, several of them notation display, where
  excluding the previous chord's terminal notes is the correct behaviour. **This is a
  boundary-membership dead end ONLY.**
```

**In plain words:** LEGACY (the analyzer awaiting deletion): a one-tick boundary fix was tried and closed - counting notes that stop exactly where a stretch begins as belonging to that stretch, in the hope of recovering a missing chord root. Measured: the boundary-touching notes are other chord tones (the root attacks later), and five display paths depend on the current convention. A boundary-membership dead end ONLY - it says nothing about extending the temporal context the analysis reads, which is a decided live capability (the extensible working span, D-030).

---

## D-318 — A short-region external merger is a dead end — do not retry it

**As decided, in the words it was decided in:**

```
- **Do not retry a short-region external merger.** A proposed after-the-fact pass merging very short
  neighbouring stretches was tried and closed. *Why:* measured — the trigger never fires, because
  the same-root merge already inside the first pass has combined those stretches before any external
  pass could see them. It was dead code.
```

**In plain words:** LEGACY (the segmenter awaiting deletion): a proposed after-the-fact pass merging very short neighbouring stretches was tried and closed - measured, its trigger never fires, because the earlier inline same-root merge has already combined them. A prohibition on re-adding one redundant merger pass - nothing about collecting notes over time or extending context.

---

## D-319 — Re-analysing the merged aggregate is a dead end — no tone-aggregation approach fixes the arpeggio root failure

**As decided, in the words it was decided in:**

```
- **Do not retry any tone-aggregation approach to the arpeggio root failure.** Pooling an arpeggio's
  notes and re-reading the chord from the pool was implemented, measured and reverted. *Why:*
  pooling makes the answer worse — the aggregate is duration-weighted and the wrong pitch sounds
  longer than the right one, so the wrong root still wins the pooled reading, and the run regressed
  both presets. **The evidence was never the problem:** the vertical scorer already prefers the
  correct root over the stretch where that root actually sounds; what is wrong is the predecessor
  signal.
```

**In plain words:** Pooling an arpeggio's notes and re-reading the chord from the pool was implemented, measured, and reverted: pooling makes the answer worse, because the wrong note sounds for longer than the right one. The evidence was never the problem.

---

## D-320 — The absent-root guard is REVERTED and must not be retried — 'absent root means wrong reading' is false corpus-wide

**As decided, in the words it was decided in:**

```
- **Do not retry the absent-root guard.** A rule rejecting any chord whose own root is not sounding
  was built, measured and reverted entirely. *Why:* it fixed fewer cases than it broke, and two of
  the cases it broke are readings the published human analysis itself makes with an absent root — so
  **the premise "an absent root means a wrong reading" is false corpus-wide.** A second, structural
  reason rides with it: any guard that changes a committed root changes the predecessor every later
  stretch reads, so its effect cascades into regions it never judged. The counts are in the record
  and are not restated here (D-431).
```

**In plain words:** A rule that rejected any chord whose own root is not sounding was built, measured, and removed entirely. It fixed two cases and broke four, and the premise behind it is false across the corpus: sometimes the published human analysis names a chord whose root is not sounding.

---

## D-321 — Winner selection compares candidate scores exactly, with no epsilon anywhere in the ranking

**As decided, in the words it was decided in:**

```
Winner selection compares candidate scores with **exact `double` comparisons — there is no
epsilon anywhere in the ranking.** The final per-bass comparator (`harmonicfunctionlayer.cpp`,
`applyHarmonicFunction`) is, in order:

1. `a.score != b.score` → higher `score` wins (exact inequality on the raw `double`);
2. else lower `tiePriority` wins (`tiePriority` is the template index — see §2 ordering);
3. else lower `rootPc` wins.

This is fully deterministic **given identical floating-point evaluation**: the same inputs
on the same build always produce the same winner. The `tiePriority`-then-`rootPc` keys
resolve genuine exact score ties (identical PC sets across enharmonic templates, e.g.
Sus4♭5 ordered before HalfDim). The omission of an epsilon is intentional — an epsilon
would make the order depend on a threshold that is itself uncalibrated, and would mask
rather than resolve near-ties.
```

**In plain words:** Two candidate readings are ordered by comparing their numbers exactly, with no tolerance band; exact ties are broken by a declared order. This is deliberate.

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

## D-323 — Asking whether a pitch belongs to the key is a question about the collection, never about the tonic — the tonic-anchored form must not return

**As decided, in the words it was decided in:**

```
**⚠ Do not reintroduce `keyTonicPc + scale` for a membership test.** A scale-DEGREE is tonic-relative
by definition and legitimately uses that pair (`buildChordResult`); a membership question must not.
Note that `buildChordResult`'s `diatonicToKey` flag and the Gate I / Gate L `invRootIsDiatonic` checks
(`postscoringgates.cpp`) still answer a *collection* question through the *tonic* pair and so still
carry the OI-168 defect — they are declared, not fixed (see `OPEN_ITEMS.md` OI-170).
```

**In plain words:** A test of the form 'is this note in the key' must read the key signature's own collection of notes, never a scale laid out from a tonic. Asking about a scale degree is a different question and may legitimately use the tonic.

---

## D-324 — Retirement of a post-scoring rule is global — a rule still doing work on any one preset is retained for all

**As decided, in the words it was decided in:**

```
  Baroque but 18 load-bearing Jazz firing sites, §1.2). Retirement is global, so a rule live on ANY
  carrier is retained.
```

**In plain words:** A correction rule is either removed everywhere or kept everywhere. If it still changes an answer under any one of the tuning presets, it stays.

---

## D-325 — A correction rule that changes a committed chord's identity is retired or folded in BEFORE the search is widened past it

**As decided, in the words it was decided in:**

```
- **A correction rule that can change a committed chord's IDENTITY is retired or folded in BEFORE
  the search is widened past it.** Where a later rule can change which root, quality or bass was
  committed, that rule is removed or absorbed into the scoring first; only then may the search be
  allowed to consider more alternatives. *Why:* stated with the decision — a rule that mutates
  root, quality or bass feeds the backward-looking evidence, so it cannot be cleanly separated from
  a wider-beam decode; a wider search would be reading a predecessor a later step is still going to
  change. The alternative — searching against uncorrected identities with a documented re-decision
  — was considered and not taken.
```

**In plain words:** Where a later correction can change which chord was committed, that correction is removed or absorbed into the scoring before the search is allowed to consider more alternatives — otherwise the search would be reading a predecessor that a later step is still going to change.

---

## D-326 — The chord-path search emits the whole path with every stretch's alternatives and margins, not the committed reading alone

**As decided, in the words it was decided in:**

```
- **The chord-path search emits the WHOLE PATH with every stretch's alternatives and its margins —
  not the committed reading alone. ⚠ LEGACY / DORMANT, and the dormancy is stated with the rule
  rather than left to be inferred.** The search hands forward, per node, the chosen reading
  together with the readings it beat and by how much. *Why:* it is the evidence-forwarding
  principle applied to the search's own output surface — the function layer above **consumes the
  alternatives**, so a search that published only its winner would make that selection impossible;
  the committed reading is the first element of the path by construction, so nothing is lost by
  publishing the rest. **The mechanism it governs is the dormant staging described above** — the
  search is not wired, and what becomes of this decoder is open at the retirement map. The rule is
  recorded here because this section specifies the carry the search would publish into, and a
  shelved mechanism's rules still belong at the section that owns the mechanism.
```

**In plain words:** The search hands forward, for each stretch, the chosen reading together with the readings it beat and by how much — because the layer above chooses among them.

---

## D-327 — The root-continuity guard reads the reconstructed inversion credit, superseding the designed sounding-third test

**As decided, in the words it was decided in:**

```
**★ THE DECISION, STATED AS SUCH — the RECONSTRUCTED-CREDIT read is the ratified form of this
guard, and the originally designed literal sounding-third test is NOT what shipped (re-homed into
this specification 2026-08-07 on the user's ruling). ⚠ LEGACY subject — the vertical scorer this
guard belongs to is dormant on both production surfaces.** Gate R asks whether the candidate earned
**any inversion credit at all**; it does not test directly whether the candidate's third is
sounding. *Why:* the derivation is the paragraph immediately above and is not repeated (#6) — the
two tests are provably equivalent everywhere except on Diminished, where the direct test would be
wrong because the only credit a Dim candidate can earn additionally requires stepwise-bass
evidence, a temporal condition no vertical test can see. Reading the pipeline's own reconstructed
credit is therefore the faithful execution of the redesign's intent rather than a compromise, and
it is what closes the cross-layer dependency the redesign set out to remove. The originally
designed mechanism text is retained above **for the record**, and a future reader must not mistake
it for the shipped behaviour.
```

**In plain words:** The guard that withholds the continue-the-same-root reward asks whether the candidate earned any inversion credit at all, rather than testing directly whether its third is sounding. The two agree everywhere except on diminished chords, where the direct test would be wrong.

---

## D-329 — Completeness of the candidate list is the priority — a chord never listed can never be chosen

**As decided, in the words it was decided in:**

```
1. **List the possible chords.** From the slice's pitches, generate **every** tertian chord the pitches could spell —
   each basic type at each root — and score each by how well the pitches fit it. **Completeness is the priority:** a
   chord never listed can never be chosen, and the measured dominant error is "the right chord was never on the list,"
   not "the wrong one was picked among good options." The fit measure is the one stated in §5 (present chord tones
   credited; absent ones a mild shortfall; extra notes carried to the membership decision, not penalised as wrong
```

**In plain words:** LEGACY (the per-slice chord decoder awaiting deletion) IN ITS LETTER, LIVE IN ITS PRINCIPLE: for each stretch the analysis first generates every chord the sounding notes could spell, and only then chooses among them. Leaving a chord off the list is the error that matters most, because nothing downstream can recover it. The letter — this listing step of the dormant Layer-4 decoder — goes with that decoder. The PRINCIPLE was transferred to the live joint estimator by the user's OI-275 ruling (2026-08-02, reading 1-with-transfer): candidate admission complete by default, and any prune derived from the model, measured for established loss, and ratified. So this entry is LEGACY-marked for where its text lives, and it is at the same time the family design's ratified admission premise — the marker below must not be read as retiring the principle.

---

## D-330 — Never a pooled recompute — the chord is never re-derived from several stretches' notes thrown together

**As decided, in the words it was decided in:**

```
- **Never a pooled recompute** (the authoritative statement of this prohibition). Membership is judged per slice
  against the prevailing chord; the layer never pools several slices' pitches into one bag and re-derives a chord from
  the bag — that over-reads, treating every passing note as a chord tone, and was the failure that motivated the
  rebuild (§13). The note model stays the lossless source so membership is decided from the real notes, not a lossy
  aggregate.
```

**In plain words:** The analysis never gathers the notes of several consecutive stretches into one bag and reads a chord off the bag. Each note's membership is judged in its own stretch against the prevailing chord.

---

## D-331 — Every chord decision carries its ranked alternatives and its confidence — committed, inherited, and abstained alike, never pruned

**As decided, in the words it was decided in:**

```
  carries its ranked `alternatives` (together with the prevailing chord) and its `confidenceModel` on **every**
  decision — Commit and
  Inherit included, filled before the trichotomy and never pruned — so Layer 5 overrides **by selecting among the readings
  this layer carried** (never by re-deriving), and the carried confidence is the quantity its override threshold scales
```

**In plain words:** Whatever the chord layer decides for a stretch, it carries the readings it did not choose and how sure it was. That carry is what lets the layer above correct a decision by choosing among readings rather than working the notes out again.

---

## D-335 — The function layer outputs the Roman numeral; the tonic/subdominant/dominant summary is a derived read-out, never a stored output

**As decided, in the words it was decided in:**

```
- **D1 — Output the Roman numeral; the three-role summary is a derived read-out (decided, user, 2026-06-26).** The Roman
  numeral is the complete, precise analysis and is what the reference corpora evaluate; the three-role summary
  (tonic/subdominant/dominant) is deterministically derivable from it and therefore lossy to store as a primary output.
  *Rejected:* a first-class three-role analysis — it would have to resolve the few context-dependent role cases, which no
  reference data can verify, violating the build-only-what-we-can-verify discipline. The read-out, if built for
  accessibility, defaults those cases to their tonic-side bucket. (Full reasoning: methods catalog §1.)
```

**In plain words:** The layer's answer is the Roman numeral — the complete, precise reading. The coarse three-role label can be worked out from it whenever a display needs it, so it is never stored or used to drive the analysis.

---

## D-336 — Cadence detection is key-agnostic and votes for the key rather than reading one

**As decided, in the words it was decided in:**

```
- **D2 — Cadence detection is key-agnostic and votes for the key; it does not read a resolved key.** *Rejected:* the prior
  key-dependent detector, which is circular and conflates the perfect with the imperfect cadence; and the single-chord
  interval test, which false-positives on tonic-to-subdominant and tonic-to-dominant because it tests leading-tone
  presence (the major third of any major triad) rather than leading-tone resolution. The event-pair feature test with the
  phrase gate is the corrected design.
```

**In plain words:** Points of harmonic closure are found without being told the key, and each one casts a vote for what the key is. Reading a key that a cadence is supposed to help decide would be circular.

---

## D-337 — A lean toward another degree is a tonicization by default; a key change needs a confirming cadence AND persistence, expressed as a change-cost

**As decided, in the words it was decided in:**

```
- **D3 — Tonicization is the default; modulation requires cadence confirmation plus persistence, as a change-cost.**
  *Rejected:* a fixed-duration rule (no published threshold exists and the boundary is a continuum); and resolving the
  distinction in the key layer (it needs function). The hysteresis over the local-key decision matches the ground-truth
```

**In plain words:** When the music leans toward a note other than the home tonic, the home key holds and the chord is written as an applied chord. The key changes only when a cadence confirms the new key and the music stays in it; how long it must stay is a cost that falls as the candidate area grows, not a fixed number of bars.

---

## D-338 — The function layer selects among the chord layer's carried readings and never re-derives a chord from the notes

**As decided, in the words it was decided in:**

```
- **D4 — The layer selects among Layer 4's carried readings; it never re-derives.** *Rejected:* re-scoring the slice from
  the notes (that is Layer 4's job and would duplicate it) — the structural content of the ratified resolution-by-
  selection: a case separable by a note cue is a lower-layer case, a case separable only by function is this layer's,
  leaving no third box.
```

**In plain words:** Where the chord layer left a stretch open, this layer picks one of the readings that layer carried. It never goes back to the notes and works out a chord of its own.

---

## D-339 — A confident earlier decision can be overturned by decisive later evidence, through ONE confidence-weighted forward-recompute mechanism — architecture-wide

**As decided, in the words it was decided in:**

```
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
```

**In plain words:** Every later stage brings its own evidence to bear on every earlier decision. Agreement strengthens it; disagreement overturns it only when the contradicting evidence is strong enough, and how strong depends on how sure the earlier stage was. When that happens the affected passage is re-read forward once, and the overturned decision is then closed for the rest of the pass.

---

## D-341 — The licensed root-motion set is completed by theory — the ascending fifth, the descending second and the diatonic diminished fifth are added

**As decided, in the words it was decided in:**

```
  **(★ THE GRAMMAR-COMPLETION AMENDMENT — found 2026-07-02 by the D5 consistency check; ★ RATIFIED by the user
  2026-07-03; in force in this spec, not yet in code — the code increment is pending):** the pre-amendment
  set descended from the old scoring-bonus signals and omitted three theory-licensed motions the catalog's
  musically-correct
  entries exercise; the licensed set now **also includes**: **the ascending fifth** (tonic→dominant and plagal
  motion — I→V, IV→I), **the descending second** (the Phrygian/Andalusian step — i→♭VII, ♭VII→♭VI, ♭VI→V), and **the
  diatonic diminished fifth** (the IV→viiᵒ link of the full circle of fifths). This is **algorithmic completion per
  theory, NOT tuning**. Implementation = its own small dormant
  increment (`isLicensedProgression` + tests, instruction pending dispatch); the consumer's D5 consistency test then
  empties its 11-motion known-gap list and tightens to the clean assert. Until that increment lands, the code
  implements the pre-amendment set — a known, ruled spec-ahead-of-code state.
  **Evidence:** the 6-entry/**11-motion** failure table, measured, enumerated and
  pinned in the consumer's consistency test (`EXPECT_EQ(failing.size(), 11u)`) — the earlier "12" was a Cowork
  arithmetic error, corrected 2026-07-02 (U2); the measured 11 is authoritative.
```

**In plain words:** The list of chord-to-chord root motions the analysis treats as real functional progressions was inherited from an older scoring mechanism and left out three motions that standard theory licenses and the project's own catalogue uses. They are added. This is completing an algorithm against theory, not tuning it.

---

## D-343 — The key/mode layer owns the candidate space and the note-evidence model outright; the residual is SELECTED from its carried alternatives, never re-scored

**As decided, in the words it was decided in:**

```
Architectural Layer 3 owns two things outright: the **candidate space** (the 252 key/modes) and the
**note-evidence model** — how well each candidate fits the pitch content and the sequence. No other architectural layer
infers key/mode from the notes, and no other architectural layer generates or re-scores key/mode candidates. What
Architectural Layer 3 does **not** own is the *final arbitration of the cases the notes alone cannot decide* (relative
major versus minor; a modulation/tonicization seam): that residual — handed forward as the ranked alternatives plus the
"uncertain" mark — is settled by Architectural Layer 5 using **functional evidence** (chord, cadence,
function) that Architectural Layer 3 structurally cannot have. So key/mode inference is split along an **evidence
boundary**: Architectural Layer 3 contributes the note evidence and resolves everything the notes can resolve; the
gated step — Architectural Layer 5's carried-readings resolution, entered under the conditions its own spec states
(`cowork_layer5_function_design.md` §5.5) — contributes the functional evidence and resolves only the flagged
residual — by **selecting among
Architectural Layer 3's carried alternatives**, never by inventing a candidate or re-scoring from the notes (that
note-evidence model has exactly one home).
```

**In plain words:** Working out the tonality from the notes happens in exactly one place: that stage owns the list of possible tonalities and the model of how well each fits the notes, and no other stage infers a tonality from the notes or generates or re-scores a tonality candidate. What the notes cannot settle — relative major against relative minor, and where one tonality gives way to the next — is handed on with the ranked runners-up, and the later function stage settles it by choosing one of those runners-up, never by inventing a candidate or scoring the notes again.

---

## D-344 — A scale outside the twenty-one recognized modes is reported as the best-fitting recognized mode, never as the unrecognized scale

**As decided, in the words it was decided in:**

```
**Which key/modes Architectural Layer 3 does NOT recognize.** Any scale that is **not** one of those 21 seven-note
modes — in particular pentatonic and blues scales, the whole-tone scale, the octatonic (diminished) scale, and any
non-Western or microtonal scale (maqam, raga, and so on). A passage genuinely in one of these is reported as the
**best-fitting** of the 21 recognized modes — the candidate with the highest local-fit score under the §5 sequence
decision, not by any separate scale-distance measure — never as the unrecognized scale itself.
```

**In plain words:** Music written in a scale the analysis does not know — pentatonic, blues, whole-tone, octatonic, or any non-Western or microtonal scale — is reported as whichever of the twenty-one recognized modes fits the notes best, chosen by the ordinary whole-run decision rather than by any separate similarity measurement. The unrecognized scale is never named as such.

---

## D-345 — The style preset first enters the analysis at the key/mode layer, as a deliberately weak prior over the modes that the note evidence overrides

**As decided, in the words it was decided in:**

```
- **This is the first architectural layer where the user's style preset (Standard / Baroque / Jazz / …) is used.**
  Architectural Layers 1 and 2 are pure facts and use no preset. The preset enters here as a **weak prior on which
  of the 21 modes are likely in this style** — the per-mode bias values in the scorer (Baroque pushes the prior
  toward major and minor; Jazz raises the modal and altered modes; "Standard" sits between). It is deliberately
  weak: the note evidence is primary and overrides it, so the preset only tips genuinely ambiguous cases (the same
  stance taken toward the written key signature). The preset is used again in later architectural layers (chord
  symbols, function); this layer is only where it *first* applies.
```

**In plain words:** The user's style setting has no effect on reading the notes or cutting the music into stretches; the first place it acts is the tonality decision, where it nudges which of the twenty-one modes are expected in that style. The nudge is deliberately small: the notes decide, and the setting only tips cases the notes leave genuinely open.

---

## D-347 — The cost of changing tonality is cheap-to-stay plus a term growing with tonal distance plus a large extra penalty on the relative major/minor switch

**As decided, in the words it was decided in:**

```
- **Change cost = cheap-to-stay + grows-with-key-distance + a large relative-pair penalty.** Alternative considered:
  a single flat "don't flip too easily" margin. Chosen: the standard key-finding shape (a flat margin cannot make a
  near modulation cheaper than a remote one, nor guard the relative pair specifically); the starting amounts are
  taken from the existing margin values and tuned later.
```

**In plain words:** Staying in the current tonality costs nothing; changing costs a base amount, plus more the further away the new tonality is, plus a large extra amount for the specific switch between a major key and its relative minor. A single flat 'do not flip too easily' margin was considered and rejected.

---

## D-348 — Tonal distance in the change cost is circle-of-fifths distance — not semitone distance, not differing scale tones — and brief-versus-sustained has no duration threshold at all

**As decided, in the words it was decided in:**

```
The change cost makes keeping the current key/mode cheap and changing it expensive — more expensive the
further the new key is from the current one, **measured as circle-of-fifths (key-signature) distance** (the number of
signature steps between the two keys' parent tonics; `C`→`F♯` and `C`→`G♭` both = 6 — not semitone distance and not a
count of differing scale tones), and most expensive of all between relative major and relative minor (the hardest
pair). The effect: a brief excursion is not worth the change cost over so few slices, so it stays in the original key;
a sustained modulation is worth it, so the key changes; and the relative-major-versus-minor choice is settled by which
reading fits the whole run of music, not one ambiguous slice. **There is no "how many slices" threshold for
brief-versus-sustained — it is purely this fit-versus-cost arithmetic** (a duration threshold a reader might expect
does not exist).
```

**In plain words:** How far apart two tonalities are, for the purpose of the change cost, is counted in steps around the circle of fifths — the number of key-signature steps between them — so C to F sharp and C to G flat are both six. It is not the distance in semitones and not a count of how many scale notes differ. And nothing anywhere counts how long an excursion lasts: whether a passage reads as a passing tonicization or as a real change of tonality falls out of the fit-against-cost arithmetic alone.

---

## D-349 — The key/mode confidence compares whole readings — the winning run against the best run forced to a different tonality there — not the top two candidates at that stretch

**As decided, in the words it was decided in:**

```
- **Confidence = how much better the winning sequence is than the best different-key sequence at that slice** (not
  the gap between the top two scores at the slice on its own). Reason: the decision is the whole sequence, so the
  meaningful confidence compares whole sequences; the near-tied cases are exactly the ones to mark "uncertain."
```

**In plain words:** How sure the analysis is about the tonality at one stretch is measured by re-running the whole passage with that stretch forced to a different tonality and seeing how much worse the best such reading is. It is not the gap between the two best-scoring candidates at that stretch on its own.

---

## D-351 — The key/mode search is its own decoder; the chord decoder is not reused for it

**As decided, in the words it was decided in:**

```
- **A dedicated best-sequence decoder for key/mode.** Alternative considered: reuse the existing chord decoder.
  Chosen: a dedicated one — the existing decoder is specific to chords and cannot be reused.
```

**In plain words:** Finding the best run of tonalities uses a decoder written for that job. Reusing the existing chord decoder was considered and rejected, because that one is specific to chords.

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

## D-376 — The joint key-and-chord step was designed as a BOUNDED COUPLING over the two existing decoders, and the unified single-state alternative was REJECTED — the option later adopted as the production architecture

**As decided, in the words it was decided in:**

```
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
```

**In plain words:** When the coupling of tonality and chord was designed, two shapes were on the table: one decision over a single combined state holding tonic, mode and chord together, or the two existing stages kept apart with a bounded coupling between them. The bounded coupling was chosen, for three stated reasons: the two stages are already built as separate decoders and the combined state would discard both and re-lay the pipeline; the gain is concentrated on a small hard minority, so re-laying the whole pipeline to serve it is disproportionate; and the coupling can be built forward-only, respecting the rule against a later stage reaching back into an earlier one. The step was afterwards shelved against measurement, and the option rejected here is the shape the production engine now has.

---

## D-380 — The carry's meaningful axis is DISTINCT ROOTS, and every above-threshold root is carried at graded confidence — a carry of winner-plus-one discards the third root on about a quarter of slices

**As decided, in the words it was decided in:**

```
The decisive fan-out finding `[data]`: a **≥3rd distinct root clears threshold on 25.1 % / 16.1 % / 24.9 %** of
slices. This is exactly the **load-bearing exclusion tail** (#12, finding-by-exclusion): the ruled-out and
low-confidence roots are **information**, not noise — they are where selection (§3) and the eventual joint step
(§4.3) earn their keep. The contract therefore requires: **carry every above-threshold distinct root, each at its
graded confidence; carry ruled-out roots at low confidence rather than dropping them.** A carry that surfaces only
the winner + one alternate (the legacy cap-of-3 + single diff-root append) **discards the ≥3rd root on ~¼ of
slices** — a #12 violation the engaged carry must not inherit.
```

**In plain words:** What one stretch of music offers is many candidate spellings of very few chord roots: measured, about five candidate readings but only about two distinct roots. So what is handed forward is a distribution over distinct roots, each with its best voicing, its variant set, and its own confidence. A third distinct root passes the bar on roughly a quarter of stretches, and those ruled-out and low-confidence roots are information, not noise — they are where the later selection and any tonality-chord coupling earn their keep. A carry that offers only the winner and one alternative throws the third root away on a quarter of stretches.

---

## D-381 — The carry must cap on DISTINCT ROOTS, not on voicings — the existing voicing-keyed cap gives no structural guarantee that a third root survives

**As decided, in the words it was decided in:**

```
**The owed guarantee (structure only; R5).** The engaged carry must **preserve distinct roots explicitly**, not as
a by-product of a voicing cap. The declared *shape*: a **distinct-root-first carry** — for each distinct root above
threshold, carry its best voicing + its variant set + its confidence, and cap on **distinct roots** (with each
root's own variant depth bounded), rather than capping on a flat voicing list. The exclusion tail (#12) is carried
as the low-confidence roots below the primary set. **The exact cap depths (how many distinct roots, how deep each
root's variant set) are precision-phase constants (R5)** — the fan-out distribution (p90 ≈ 4 roots, max 11)
informs the *floor*, but the value is fitted later, not here. This is an **owed change to the decoder's carry
construction** (Layer 4 / E4), named here so the engagement design and E4 agree on the contract; it is not built
in this pass.
```

**In plain words:** The limit on how many alternatives are kept counts spellings, not roots, so the allowance can be used up entirely by inversions and template variants of the top two roots before a third root is reached. Keeping a third root is therefore a by-product rather than a guarantee. The shape owed is the other way round: for each distinct root above the bar, carry its best voicing, its variants and its confidence, and set the limit on the number of roots, with each root's variant depth bounded separately.

---

## D-382 — The function layer selects by JOINT CONSISTENCY across tonality, root, inversion and bass — not by maximizing any one score — and every ambiguity kind reasons over the full carried distribution

**As decided, in the words it was decided in:**

```
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
```

**In plain words:** Choosing among the readings handed forward is done by picking the one that agrees best across all the evidence at once — the tonality, the root, the inversion and the bass — rather than the one that scores highest on any one kind of evidence alone. Everything else is carried on at graded confidence, and where nothing dominates the stretch is marked open. This generalizes what was built: only the symmetric-rotation case already reasoned over the whole set of alternatives, while every other case decided between just two readings.

---

## D-383 — Bass, spelling and tonality-consistency DECIDE; a licensed progression is only a tie-break among already-consistent readings and may never override a committed root

**As decided, in the words it was decided in:**

```
The **re-ordering vs the as-built resolver** is the load-bearing structural change: the built `resolveAbstained`
leads with `isLicensedProgression` (the weak channel) as its *primary* separator (Transition/ShareTone arms). The
research says bass/inversion + spelling + key-consistency are the primary channels and progression is the
tie-break. Engaged selection **re-orders** so the load-bearing channels decide and progression only breaks ties
among mutually-consistent readings. *(The channel weights and the deciding margin are precision-phase, R5 — only
the ordering/direction is fixed here.)*
```

**In plain words:** The built resolver leads with whether one chord progresses plausibly into the next, and that is the wrong lead. The evidence that actually carries root correctness is the bass and inversion, the written spelling, and how well a root fits the tonality of the passage. Whether the progression is a licensed one is a tidy signal that turns out to be uncorrelated with getting the root right, so it is demoted: it may separate readings that are already equally consistent, and it may never overturn a root the vertical evidence committed to. Only the ordering is fixed here; the weights are left to the fitting phase.

---

## D-384 — Re-ranking the tonality under chord evidence is a SEPARATE step, never part of the function layer's selection — the function layer reasons inside a tonality already fixed

**As decided, in the words it was decided in:**

```
- **The joint key↔chord step (O-18 / contract C3)** is a **distinct step, not L5 selection.** L5 selection reasons
  within a *fixed* region key; the joint step is the coupled machinery that **re-ranks the key under chord
  evidence** (and vice versa) — the "carry a beam of (key, chord) hypotheses and let downstream chord evidence
  re-rank the key" of `[research]` §3. It is the home of the C3 "genuinely-coupled key↔chord minority."
```

**In plain words:** The function stage chooses among readings within a tonality that has already been settled; it never re-opens which tonality that is. Anything that re-ranks the tonality in the light of the chords, or the chords in the light of the tonality, is a distinct piece of machinery upstream of it, and that piece owns the small population of places where the two genuinely depend on each other.

---

## D-385 — Pedal-point detection's home is DECIDED: a reader over the chord layer's carry that annotates a carried reading — never a second analysis that overwrites the winner

**As decided, in the words it was decided in:**

```
- **Home: a reader over the decoder's Layer-4 carry, emitting a pedal-annotated result — an additive annotation on
  a carried reading, NOT a mutation of the winner.** Because the material it needs is the carry's distinct-root
  distribution (§6.2), and chord identity is Layer 4, the reader sits at the **carry side (Layer-4 output / a
  decoder post-reader)** and feeds L5 selection *one* pedal-annotated candidate. It never owns `results.front()`
  and never writes back into the decoder's scoring — it reads the carry forward and annotates.
```

**In plain words:** Deciding that a SUSTAINED NOTE is a pedal - that the real harmony is the chord moving against it - is a chord-identity question, so the detector sits on the chord layer's output side, reading what that layer already carried. THE PEDALED NOTE CAN BE IN ANY VOICE: the bass pedal is the classic case, but the ratified pedal-point class is voice-independent (D-207), and this entry's home decision - an ADDITIVE reader that marks one carried reading as the pedal reading - applies unchanged whichever voice holds the note. It never takes ownership of the winning reading, never writes back into the scoring, and never replaces the set of alternatives; the original reading survives at its own confidence. (The source document's own wording says 'bass' - the legacy-era default; the voice-independent scope is the ruled one, user 2026-08-02 with D-207.)

---

## D-386 — No fourth hand-rolled scan for the best different-root alternative — the pedal reader consumes the carry's own ranking, or the one unified primitive

**As decided, in the words it was decided in:**

```
The confirmation margin (§6.1 (ii)) is the **"best different-root alternative"** decision the audit catalogues as
computed 4× (`[audit §1.3]`, FQ-1). Under the engaged carry it is served two-ways-that-are-one: the decoder already
**reads** the best different-root reading from its carry (`chordslicedecoder.cpp:927-930` `[code]`), and FQ-1
unifies that scan into one primitive (`[audit]` FQ-1, sequenced into E4 — Stage-1 STOP-reported the four legacy
scans are *not* byte-identically one, so the unification lands with the decoder, not pre-L5). The pedal reader
therefore **consumes the carry's distinct-root margin** (or the FQ-1 primitive over the carry) — it adds **no fourth
scan**. This is the concrete pedal instance of Part 1 §2.2's load-bearing exclusion tail: the ≥2nd distinct root's
carried confidence *is* the pedal confirmation signal.
```

**In plain words:** Finding the strongest alternative with a different root is a decision the code already makes in four separate places. The pedal reader adds no fifth: it reads the margin straight off the ranked distinct roots the chord layer already carried, or through the single shared routine that unification replaces the four with. The second-strongest root's carried confidence is the pedal confirmation signal. RULING (user, 2026-08-02, OI-278): the SECOND alternative — 'the one unified primitive' — is STRUCK: measured at the code not to exist (the four scans it presumed one were never one decision, D-403). The FIRST alternative stands: the pedal reader takes its margin from the ranked distinct roots the chord layer already carries.

---

## D-387 — A contradiction between the function context and a committed chord is surfaced on the ONE open mark, enriched with a reason — not on a second parallel flag, and not by overloading the plain undecided mark

**As decided, in the words it was decided in:**

```
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
```

**In plain words:** When the functional context disagrees with a chord the earlier stage committed to confidently, that disagreement is recorded as a reason on the single existing open mark, alongside the genuinely-undecided reason it already carries. Two shapes were rejected. Setting the plain undecided mark would be wrong in meaning: the chord stage was not undecided, it committed, and the reading is carried unchanged. Adding a second flag beside the open mark would be two fields on the same object meaning the same thing, threaded through the same three places.

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

## D-391 — Reads between the two analysis dimensions are admissible only where the combined dependency graph stays acyclic — harmonic layers may take voice-leading FACTS freely; a voice-leading component may take a committed harmonic result only if nothing that result depends on consumes it back

**As decided, in the words it was decided in:**

```
- **D6 — the cross-axis dependency rule (acyclicity by declaration).** Cross-axis reads are admissible only where
  the combined two-axis dependency graph stays acyclic, checked at each wiring: (a) harmonic layers may consume
  axis-2 **facts** (VL-A/B, L1-derived only) freely — e.g. the future L4 non-chord-tone filter — because facts
  depend on no harmonic inference; (b) an axis-2 component may consume a **committed harmonic output** (VL-F
  reads L3's key) provided nothing that harmonic layer depends on, directly or transitively, consumes that
  axis-2 component. VL-F→L3 is safe (L3 consumes no axis-2 output; the planned L4 filter consumes only VL-A/B,
  which don't depend on VL-F). Each future wiring re-states this check in its instruction. *Alternative
  rejected:* a blanket "axis 2 reads nothing harmonic" — it would make schema recognition impossible for no
  structural gain.
```

**In plain words:** The harmonic analysis and the voice-leading analysis may read each other, under one rule checked at every wiring. A harmonic stage may freely use the voice-leading facts derived straight from the notes, because those depend on no harmonic decision. A voice-leading component may use a harmonic result that has already been committed — recognizing a stock pattern needs scale degrees, and scale degrees need the tonality — but only if nothing that harmonic stage depends on, directly or through others, reads that component back. A blanket ban on reading anything harmonic was considered and rejected.

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

## D-406 — The catalog owns the NAMED progressions and substitutions; the pairwise licensing grammar is owned by the function layer — the two are never derived from each other

**As decided, in the words it was decided in:**

```
**The D5 dependency map (one owner per concern — restated here, mirrored in code).** Two places know about chord
successions: **this component** owns the **named progressions and substitutions** (the catalog); **Layer 5's
`functionprogression`** owns the **pairwise licensing grammar** (which root motions are licensed at all). *Changing the
catalog* → change this component only (the grammar never needs an edit; but a new entry must pass the **consistency
test** — every adjacent chord pair licensed — or it is mis-encoded OR a genuine grammar gap). *Changing the grammar* →
change `functionprogression` only. The two are **not derived from each other**; the **only coupling is the consistency
test**, and it runs **one way (catalog → grammar)**. Owner ruling: D5 (`cowork_progression_schema_design.md` §6),
```

**In plain words:** Two places in the system know about which chords may follow which. This reference catalog holds the named progressions and substitutions; the function layer holds the separate rule about which root motions are allowed at all. Neither is computed from the other. The single link between them runs one way: every adjacent pair in a new catalog entry must be allowed by the grammar, and a pair that is not is either a mis-encoded entry or a genuine gap in the grammar.

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

## D-425 — The uncertainty surface's contract IS the full posterior; the local slice is the first delivered step, and the completion is a named step, never an indefinite upgrade

**As decided, in the words it was decided in:**

```
**Recommendation: the contract IS B-full; B-slice is the first DELIVERED step (it is established
today and is a strict subset of B-full's surface), and the marginal completion is a NAMED, ROWED
step of this increment — not an indefinite upgrade.** Register row at ruling time (register rule
(c)); the slice's fields are defined as views of the posterior so nothing is published twice
(#6). If the marginal oracle's establishment surfaces a blocker, that is a #13 STOP returning to
the user — never a silent regression to B-slice-as-end-state.
```

**In plain words:** What the analysis publishes about its own uncertainty is, by contract, the full spread of probability over every reading it considered — not just a note about the runner-up. The narrower runner-up form ships first, because it is the part already checked and it is a subset of the full form; finishing the rest is a named, tracked step of the same piece of work, not something that waits for someone to ask for it. If checking the full form turns up a problem, that stops the work and goes back to the user; it never quietly becomes a decision to keep the narrow form forever.

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

## D-449 — Factor granularity is fixed: the bass factor is evaluated per event, the missing-tone penalty per event of segment length, the emission per tone, and the boundary-family factors per boundary

**As decided, in the words it was decided in:**

```
**Factor granularity is fixed, per factor.** The pitch emission is scored **per tone**. The **bass
factor is evaluated per event** — each event's sounding bass judged against the segment's chord.
The **missing-tone penalty is normalized per event of segment length**, so a segment missing its
third pays in proportion to how long it fails to sound it. The **transition, entry and key-change
factors stay per boundary**. *Why:* measured on a real corpus case, and the measurement is why the
granularity is fixed at all — under per-segment bookkeeping a longer segment pays the bass and
missing-tone terms once where a split pays them twice, so merging harvests a discount unrelated to
the music, which is the classic semi-Markov length bias. On the case that exposed it the
bookkeeping alone decided merge against split, against the ground truth; with the bass factor
evaluated per event the remaining gap is small enough to ride two fittable values rather than the
structure. The per-event bass form is not an invention: it is the published per-frame form of the
work this factorization is grounded in.
```

**In plain words:** The scoring form is written as a term per segment, which left open whether each term is counted once for the whole segment or once for each event inside it. That is now fixed: the bass evidence is judged at every event against the segment's chord, a missing chord tone is charged in proportion to how long it fails to sound, each sounding pitch is judged on its own, and the terms that belong to a boundary stay at the boundary.

---

## D-450 — The key-signature and declared-mode prior conditions the INITIAL key state only, re-entering only at a notated signature change

**As decided, in the words it was decided in:**

```
**The key-signature and declared-mode prior conditions the INITIAL key state ONLY.** What the
written key signature and any declared major/minor say about the key sets the starting key state
and is not applied again — **except at a notated mid-piece signature change**, which is new written
evidence and re-anchors it. The alternative form, a persistent pull toward the signature at every
step, is **rejected**. *Why:* traced and settled by desk simulation on a Dorian-notated opening and
a genuinely modal piece. A persistent pull taxes every away-from-signature key at every segment,
without bound, and it has no basis in the literature — the published work carries no signature
prior at all; it also re-introduces, in soft form, the signature-pull bias an earlier measurement
condemned, in exactly the accidental-free stretches where the prior should be silent. The
initial-state form pays the tax once and lets the music govern thereafter.
```

**In plain words:** What the written key signature and any declared major/minor say about the key is used once, to set the starting key, and then not again — unless the score itself changes signature part way through, which is new written evidence and re-anchors it. The alternative, a pull toward the signature at every point, is rejected.

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

## D-453 — The desk simulation's verdict: the ratified factorization passes nine of ten traces and no finding reopens the structure

**As decided, in the words it was decided in:**

```
1. **The verdict:** the ratified factorization passes nine of ten traces as specified; no finding
   requires re-ratifying the STRUCTURE (variables, factors, decode).
```

**In plain words:** Ten cases were traced by hand against the agreed model. Nine behaved as the model says they should. The tenth exposed one thing the model had not settled — how finely each term is counted — and that was fixed by sharpening the model rather than by changing what the model is made of. So the variables, the factors and the decoding stay as ratified.

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

## D-463 — The temporal signals sitting in the vertical scorer are left where they are, and the gate that depends on them must move with them

**As decided, in the words it was decided in:**

```
- **The temporal signals sitting inside the vertical scorer STAY WHERE THEY ARE, and the gate that
  depends on one MOVES WITH THEM.** Several signals that look backward or forward in time are
  computed inside the part of the scorer that is supposed to judge only what sounds at one moment.
  They are known, documented debt and are **not** to be moved before a scoring-stabilisation phase;
  when they do migrate, Gate R has to move or adapt **simultaneously**. *Why:* stated with the
  recommendation and grounded in the mechanism — Gate R's test uses a score component as a stand-in
  for *this candidate has a sounding third*, and it carries that meaning only because one of those
  signals is computed where it is. Removing the debt without touching the gate would silently
  change what the gate tests: a cross-layer dependency invisible to anyone reading the gate's own
```

**In plain words:** Five signals that look backward or forward in time are computed inside the part of the scorer that is supposed to judge only what sounds at one moment. They are known debt and are not to be moved yet. When they are eventually moved, the gate whose test depends on one of them has to be changed at the same time.

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

## D-465 — The policy for judging a proposed post-scoring gate: another bias correction gets the bias fixed first, a structural condition is sound, and a cascade means the missing thing is functional context

**As decided, in the words it was decided in:**

```
- **The policy for judging a PROPOSED post-scoring gate — three tests.** (1) If the proposal is
  another variant of correcting the bass-as-root bias, first ask whether the bias itself can be
  reduced, or whether functional context would remove the ambiguity; add the gate only if the fix
  is genuinely local. (2) If it turns on a **structural** condition — pitch-class arithmetic plus a
  presence constraint, not temporal evidence — it is likely architecturally sound. (3) If it needs
  the three-step cascade shape, that is a strong signal that the real problem is missing functional
  context, and the gate is the wrong answer. *Why:* derived from a systematic read of the whole
  gate population — two thirds of the gates were solving one problem, the scorer's bass-as-root
  pull, and three separate cascades were each built up step by step for the same shape of failure,
  which the canonical specification already names as the warning sign that accumulating gates
  signal an unresolved architectural problem. The two gates that read came out architecturally
  healthier both turn on structural conditions rather than compensating for the bias, which is
  where test (2) comes from.
```

**In plain words:** Three tests decide whether a proposed gate should be added. If it is one more variant of correcting the scorer's pull toward reading the bass as the root, first ask whether the pull itself can be reduced or whether functional context would remove the ambiguity — add the gate only if the fix really is local. If it turns on pitch arithmetic and what is present rather than on what came before or after, it is likely sound. And if it needs the whole three-step cascade shape, that is a strong sign the real problem is missing functional context.

---

## D-466 — Forward-only is a strong DEFAULT, not dogma — a backward edge is admissible only as a deliberate, surfaced, measured, documented exception

**As decided, in the words it was decided in:**

```
**Forward-only is a strong *default*, not dogma:** a sanctioned backward edge is admissible
  only as a deliberate, surfaced, measured, documented exception (justified by a plateau, scoped, gated,
  convergence-bounded, recorded).
```

**In plain words:** The rule that each stage passes its work forward and never reaches back may be relaxed if it genuinely gets in the way of being right. But only deliberately and in the open: the case must be justified by evidence that the forward-only path has stopped improving, confined to the cases that need it, gated so it does not fire on the ordinary majority, bounded so an iterative one cannot run away, and recorded as an architecture decision. A silent cycle is never admissible.

---

## D-467 — A rebuilt or re-tuned chord scoring must not rely on the held-note repetition bonus the faithful note model removed

**As decided, in the words it was decided in:**

```
**★ A REBUILT OR RE-TUNED CHORD SCORING MUST NOT RELY ON THE HELD-NOTE REPETITION BONUS THE FAITHFUL
NOTE MODEL REMOVED (re-homed into this specification 2026-08-08 on the user's ruling).** Before the
note reader was rebuilt, a note held across a tie was counted more than once, and that spurious extra
weight happened to push a handful of ambiguous sonorities toward the correct root. The faithful note
model removed the duplication. **Whatever replaces or re-tunes this layer's scoring must not lean on
that boost to get those cases right.** *Why:* measured when it surfaced — removing the inflation
moved a small number of cases the wrong way while the key axis stayed flat, which is what identified
those cases as having been carried by an artifact rather than by evidence; a correct re-calibration
is expected to recover them on real evidence. It is exactly the hidden dependency the upstream-first
rebuild exists to surface. **Whether those cases have since recovered is NOT stated here and was not
checked** — the constraint binds regardless, because it forbids leaning on the artifact rather than
asserting anything about the current count.
```

**In plain words:** Before the note reader was rebuilt, a note held across a tie was counted more than once, and that spurious extra weight happened to push a handful of ambiguous sonorities toward the right root. The faithful note model removed it. Whatever replaces or re-tunes the chord scoring must not lean on that boost to get those cases right.

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

## D-490 — FALSIFIED: no threshold can make the fine-grain function override net-positive — the harm rate is flat against both quantities the threshold is built from

**As decided, in the words it was decided in:**

```
- **FALSIFIED — no threshold can make the override net-positive.** Whether a fire helps or hurts is
  unrelated to either quantity its trigger is built from: the incumbent reading's confidence and
  the strength of the progression contradiction. Since the only tunable knob scales the bar by that
  confidence, **no setting separates the cases it fixes from the cases it breaks**, and the best
  measurable setting simply switches the pass off. *Why:* measured and stratified rather than
  argued, on a ground-truth-aligned population of fires — the harm rate is essentially flat across
  the contradiction value and **rises** with the incumbent's confidence, so the one available lever
  pushes the wrong way; the mechanism of the harm is named too, the fourth- and fifth-related root
  moves the progression score rewards accounting for most of both the fires and the harms.
```

**In plain words:** A late correction pass overturns a committed chord when the surrounding progression argues against it. Whether it helps or hurts turns out to be unrelated to either quantity its trigger is made of — how confident the earlier reading was, and how strongly the progression contradicts it. So no setting of the trigger separates the cases it fixes from the cases it breaks, and the best available setting simply switches the pass off.

---

## D-491 — REFUTED: making the override's comparison vertically fair does not repair it — even where the alternative fits the notes at least as well, it is still about 71 % harmful

**As decided, in the words it was decided in:**

```
- **REFUTED — making the comparison vertically fair does not repair it.** The obvious repair is to
  let the pass overturn a reading only when the replacement fits the sounding notes at least as
  well. Measured, that band is still overwhelmingly harmful. The problem is not that the comparison
  was unfair; it is that **the progression contradiction does not predict which root is correct at
  these moments**. *Why:* measured across bands of the vertical gap, every one net-negative, with
  the count and harm rate per band; the conclusion drawn is the one the numbers support and no more
  — the earlier layer's vertical commit is a better predictor of the annotated root than the
  progression re-pick, even where the alternative is its vertical equal.
```

**In plain words:** The obvious repair was to let the pass overturn a chord only when the replacement fits the sounding notes at least as well as the reading it displaces. Measured, that band is still wrong about seven times in ten. The problem is not that the comparison was unfair; it is that the progression argument does not predict which root is correct at these moments.

---

## D-492 — The recommended redesign is to demote the override to an annotation — carrying the earlier reading unchanged and surfacing the contradiction — floored by simply disabling it

**As decided, in the words it was decided in:**

```
- **RECOMMENDED AND NOT ADOPTED — demote the override to an ANNOTATION.** The recommendation on the
  evidence above is to stop overturning the committed chord and instead **record that the
  surrounding progression disagrees**, leaving the chord alone — accuracy-equivalent to simply
  disabling the pass, while keeping the disagreement as calibrated uncertainty a later stage can
  use. Tightening the trigger and repairing the comparison are both rejected as measured
  net-negative. **This is a PROPOSAL, not a specification of this document: it is NOT adopted, and
  no reader may implement it from this paragraph.** It is recorded as an INPUT to the one
  prioritized fix plan, and the row that owns the demotion carries the cross-reference on the
  plan's side. *Why:* every clause of the recommendation is measured and cited in the bullets
  above; the loss it accepts — a modest number of genuine corrections given up — is stated and kept
  in view rather than netted away.
```

**In plain words:** Instead of overturning the committed chord, the pass should record that the surrounding progression disagrees and leave the chord alone. That matches simply switching the pass off on accuracy, while keeping the disagreement as information a later stage can use. Tightening the trigger and repairing the comparison are both rejected: they were measured and both lose.

---

## D-493 — Restricting the override to the genuinely-coupled key-and-chord minority is UN-COMPUTABLE, not merely unmeasured: its trigger is not computed anywhere and building it is the still-owed joint step

**As decided, in the words it was decided in:**

```
- **UN-COMPUTABLE, not merely unmeasured — the principled restriction cannot be built today.**
  Restricting the override to the genuinely coupled key-and-chord minority is the principled form,
  and its trigger **is not computed anywhere**. The binding blocker is the component that asks
  whether a different carried KEY alternative flips the chord reading: that needs a per-key chord
  re-decode, which **is** the joint key-and-chord step the record says is still owed, and the
  closest existing mechanism explicitly leaves the chord unchanged. *Why:* established at the code,
  both components separately; surfacing the trigger would mean **building** the joint step, which
  the standing sequencing rules forbid at this stage. So the verdict is un-computable rather than
  unmeasured, and this option is a long-run successor rather than a near-term choice.
```

**In plain words:** The principled home for this correction is the small set of moments where the key and the chord genuinely depend on each other. That set cannot be measured today, and not for want of a dump: half of the trigger requires re-deciding the chord under a different candidate key, which is precisely the joint step the project has not built. So this option is a long-run successor, not a near-term choice.

---

## D-494 — RATIFIED AMENDMENT A-4: the function layer must gain key-confirmation channels that do not require a cadence, plus an enharmonic-identity rule for key spans

**As decided, in the words it was decided in:**

```
- **The layer needs KEY-CONFIRMATION CHANNELS THAT DO NOT REQUIRE A CADENCE (the Layer-5 half of
  the ratified amendment whose other half — an enharmonic-identity rule for key spans — is at
  Layer 3; the two cross-point).** Named channels: **sustained dominant emphasis**
  (arrival-denied dominants) and **recognized transposition sequences**, the latter entering as an
  input from the recognition consumer this layer is already planned to gain. *Why:* derived from
  the review's stress simulation and stated with it — on resolution-denying music the
  cadence-confirmed modulation gate almost never fires, so the default keeps the home key across
  genuinely modulating spans and every Roman numeral in them is computed against the wrong key. The
  measurement bed named with the amendment is a resolution-denying repertoire.
```

**In plain words:** The program only accepts a change of key when a cadence confirms it. Music that deliberately avoids cadences — a sustained dominant that never resolves, a sequence that transposes step by step — therefore keeps being read in the old key. The amendment requires channels that confirm a key without a cadence, and a rule for deciding whether a span is written in one spelling of a key or its enharmonic twin.

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

## D-499 — RATIFIED AMENDMENT A-10: four documentation riders — a consolidated ownership page for the notation-derived views, the membership tie-breaker recorded as idiom-calibrated, and the producer-agnostic seam pinned as a design property

**As decided, in the words it was decided in:**

```
- **A-10 (from F-4, F-12, F-17, F-18). Doc riders**: L1.5 consolidated ownership page; record the membership
  tie-breaker as an idiom-calibrated constant; pin B-swap readiness as a design property; (optional) STATUS entry
  header schema.
```

**In plain words:** Four small documentation debts, ratified together: the notation-derived view layer owns several things and has no one page saying so; the rule that breaks a tie about whether a note belongs to the chord is calibrated to one style and is not recorded as such; the property that a learned component could be dropped in where the hand-built one sits is currently true but written down nowhere; and the status file's entry format is hard to read.

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

## D-501 — A tool may read a written chord symbol ONLY as a comparison or ground-truth label — never as input that influences what the analyzer computes

**As decided, in the words it was decided in:**

```
2. **A written chord symbol in the score may be read ONLY as a comparison or ground-truth label.**
   Symbols are instructions the user wrote, not analysis results. **Production paths must not read
   them as input to analysis at all.** A measurement tool may set them beside the analysis to see
   how far the two agree, and may **never** let them influence what the analyzer computes. *Why:*
   stated with the principle — a symbol is user content and may be wrong, so reading it as input
   makes the analysis agree with the user rather than with the music; and in a measurement tool it
   additionally destroys the measurement, because the tool would then be comparing the annotation
   with itself.
```

**In plain words:** Chord symbols printed in a score are instructions the user wrote, not results. Production analysis may not read them at all. A measurement tool may put them beside the program's own answer to see how far the two agree, but it may not let them change what the program computes.

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

## D-504 — A recognised harmonic sequence is ALWAYS emitted as key evidence — the earlier gate that emitted it only where no cadence existed threw corroboration away

**As decided, in the words it was decided in:**

```
### 4.6 Harmonic sequences as evidence of the local key (the Layer-5 §5.3 channel; review A-4)
A recognised harmonic sequence implies **motion of the local key** (the tonality — see the §0 "key" row). The consumer exposes each as a typed output
`{progression, transposition step, span, number of repetitions, prior strength}`. **U1 ruling (2026-07-02): a sequence requires ≥2 transposed statements of the SAME recognised entry** — that is
what "repeated at successive transpositions" (§0) means; a run's `repetitions` counts the matched windows, and the
evidence weight scales with it (more repetitions → stronger; direction fixed, values Stage-5). A **single**
recognition of an internally-sequential entry (circle-of-fifths, Monte, Fonte) emits **no** §4.6 sequence — its
key-motion implication is already carried by its schema-span (the entry's internal transposition structure is
catalog knowledge, readable by the F-C consumer when that wiring is designed; recorded in §9 so it is decided
there, not lost). **The consumer ALWAYS emits it —
evidence is never discarded** (the no-information-loss and use-every-clue principles; user-directed correction
2026-07-02, replacing an earlier "only where no cadence exists" gate that threw corroboration away). Layer 5 §5.3
uses it in two roles: **(i) corroboration, always** — sequence evidence agreeing with a confirming cadence raises
the candidate key's vote, disagreeing tempers it; **(ii) the substitute confirming channel** for condition (a)
**only where no authentic cadence confirms the candidate key**, at a weight **below** the cadence channel's
(ordering fixed; values Stage-5) — the cadence remains the stronger confirmation wherever it exists, by weight, not
by suppressing the other evidence. **Frame obligation:** comparing sequence evidence against the home-key
confidence is a NEW comparison; it must be declared in the confidence contract §4 (frame **F-C**) **before** the
§5.3 wiring is built. The consumer's own build (the annotation + the §5.5 feature) does not need it.
```

**In plain words:** When the same progression is recognised at successive transpositions, that is evidence about where the tonality is going. It is now always published. It corroborates a cadence that agrees with it and tempers one that disagrees, and it stands in as the confirming channel only where no authentic cadence confirms the candidate tonality — always at a weight below the cadence's.

---

## D-505 — A harmonic sequence requires at least two transposed statements of the SAME recognised entry; a single internally-sequential entry emits none

**As decided, in the words it was decided in:**

```
A recognised harmonic sequence implies **motion of the local key** (the tonality — see the §0 "key" row). The consumer exposes each as a typed output
`{progression, transposition step, span, number of repetitions, prior strength}`. **U1 ruling (2026-07-02): a sequence requires ≥2 transposed statements of the SAME recognised entry** — that is
what "repeated at successive transpositions" (§0) means; a run's `repetitions` counts the matched windows, and the
evidence weight scales with it (more repetitions → stronger; direction fixed, values Stage-5). A **single**
recognition of an internally-sequential entry (circle-of-fifths, Monte, Fonte) emits **no** §4.6 sequence — its
```

**In plain words:** A recognised progression that is itself built out of transpositions — a circle of fifths, a Monte, a Fonte — does not by itself count as a sequence. Two or more transposed statements of the same catalog entry do. A single internally-sequential recognition publishes its own span instead, and its transposition structure stays where it belongs, in the catalog.

---

## D-506 — Progression recognition is ADDITIVE: the literal Roman numeral is never rewritten, and a substitution is recorded only in the annotation

**As decided, in the words it was decided in:**

```
- **D4 — Additive; the literal Roman numeral is never changed.** *Alternatives weighed and rejected:* rewriting the numeral to the
  substituted-for function — it loses the literal label the ground truth scores.
```

**In plain words:** When the recogniser sees that a chord is standing in for another — a tritone substitute doing a dominant's job — it says so in the annotation and leaves the Roman numeral exactly as the analysis committed it.

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

## D-509 — Where the analysis already committed a chord, a recognised progression corrects it through the EXISTING override frame and may only SELECT an already-carried reading — no new comparison frame, and never a reading built from the notes

**As decided, in the words it was decided in:**

```
- **Where Layer 4 committed:** if an admitted recognised progression's member position demands a **different root
  or quality** than the committed reading, the recognition's prior strength enters the **same contradiction
  quantity frame F-B already compares** (the functional-plausibility difference), and the committed reading is
  overridden **if and only if** that quantity exceeds the §8 threshold scaled to the committed reading's composite
  confidence — the same threshold rule, the same tie-holds-the-incumbent rule, and the same
  overridden-at-most-once-per-pass rule as every other F-B firing (§0). The correction **selects** an existing
  reading (a ranked candidate, or the recognised member's realisation where it is one) — never a reading built from
  the notes. No new comparison frame is introduced.
```

**In plain words:** If a recognised progression demands a different chord than the one already committed, the recogniser does not invent a chord from the notes. It puts its evidence into the comparison the correction mechanism already makes, under the same threshold, the same tie rule and the same once-per-pass rule, and it can only pick a reading that was already on the table.

---

## D-510 — The correct carry is the one that keeps the distinct alternative reading, not the one that appends a near-duplicate of the winner — chosen on the carry's purpose, not on which code is at HEAD

**As decided, in the words it was decided in:**

```
- **Which carry is correct is decided on the carry's PURPOSE, not on which code happened to be at
  HEAD: the correct carry is the one that KEEPS the distinct alternative reading.** Two promotion
  idioms were in use — one swaps a reading already carried in `results[]` to the front, leaving the
  displaced reading in place; the other builds a fresh copy and appends it. The swap idiom is
  correct. *Why:* argued from what the carry is FOR, and the design says so in terms — the
  alternatives exist so the later layer can select among the **distinct** readings, and a copy of
  the winner is not a distinct reading. Measured on the full output surface across the whole
  corpus, the append idiom injects that near-copy and displaces the genuinely different partner,
  which is an information-loss regression under #12. The same principle is already applied
  elsewhere in this layer, where a non-promoting raw pull is popped so it does not pollute the
  list. This is explicitly **not** "prefer the idiom that is at HEAD".
```

**In plain words:** Two ways of promoting a chord to winner were in use. One swaps an alternative already on the list to the front and leaves the displaced reading in place; the other builds a fresh copy and appends it. Measured, the second injects a near-copy of the winner into the alternatives and pushes out the genuinely different reading. The first is therefore the correct behaviour to unify on.

---

## D-511 — One promotion primitive with a present-first dedup guard replaces the two ad-hoc promotion idioms; the append branch fires only when the target is genuinely absent

**As decided, in the words it was decided in:**

```
- **ONE promotion primitive, with a PRESENT-FIRST dedup guard — the append branch fires only when
  the target is genuinely absent.** The ordering is the whole fix: present-first makes an
  already-carried partner *swapped* rather than *appended*, so no duplicate can enter. *Why:* the
  design shows the equivalence rather than claiming it — for the enharmonic flip the caller has
  already computed the in-`results[]` partner index, and the primitive swaps that exact index, so
  the produced permutation is byte-identical to the behaviour it replaces. That is what makes
  retiring the separate rule a no-op on the output rather than a change to be argued about.
```

**In plain words:** Promoting a chord to winner becomes a single shared operation. If the reading is already among the alternatives it is swapped to the front; only if it is genuinely absent is a fresh one built and appended. That ordering is the whole fix, and it reproduces the existing behaviour exactly where the reading is already present.

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

## D-521 — The general law of the circularity map: an abstract circle becomes acyclic in the concrete by one of four named conditions — and every alleged circle in this system fell to one of them

**As decided, in the words it was decided in:**

```
**The general law all five instances obey:** a circle in the ABSTRACT ("A needs B,
B needs A") becomes acyclic in the CONCRETE when one of: the score already contains
one side (spelling, signatures, fermatas, annotations); a key-agnostic form of the
evidence exists (tonic votes, dominant shapes, bass skeletons); the dependency is on
a COARSER fact that is already stable (the collection, not the tonic); or the
ratified forward-override/joint-minority patterns cover the measured-rare remainder.
Every alleged circle above fell to one of these. None survived as a true blocker —
which is the answer to the user's worry: the circularity challenge, named
completely, stops nothing.
```

**In plain words:** The worry that key, chord, cadence and non-chord tones each need one another turns out not to block anything once the cases are named. A circle dissolves when the score already contains one side of it, when a form of the evidence exists that does not need the other side, when the real dependency is on a coarser fact that is already settled, or when the rare remainder is covered by the ratified forward-recompute pattern.

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

## D-524 — The joint state's mode axis is TWO modes — major and composite minor; modal and chromatic colour lives in the pitch emission, and the un-rounded reading is published

**As decided, in the words it was decided in:**

```
**Mode vocabulary (user-ratified 2026-07-19).** The joint state's mode axis is **{major, minor}** —
minor meaning the composite minor practice (natural/harmonic/melodic as one key with variable sixth and
seventh degrees). **Modal and chromatic color is modeled in the pitch-emission factor**, not the state:
the first build carries the minor-scale variants (raised sixth and seventh) only; church-mode variants
(Dorian sixth, Mixolydian seventh, Phrygian second, …) enter later only through their own premise-ledger
entries (#17); the dominant-family exotic scales are **excluded from the state space** (constrained-
optimum ledger record: the 21-mode state space is excluded because its states are ungradable against any
ground truth we possess — #19/#20 — and OI-174 measured them harming inference). **User's condition,
part of the decision: the un-rounded reading is preserved and published.** The emission factor's
modal-variant evidence is published as a derived fact on the output surface, so the presentation layer
can show the end-user that a passage decoded as, say, D minor would — without the rounding to
major/minor — be called D Dorian, and can choose whether/how to display that by user preference (the
eventual preset ↔ mode-prior mapping is a presentation/preference concern, not an inference state).
Inference states stay two-mode under every preset. This resolves the OI-174/OI-132/OI-147 mode-
vocabulary question at the design level; the rows close when the build lands.
```

**In plain words:** The estimator's tonality has only two characters, major and minor, with minor meaning the ordinary minor practice whose sixth and seventh degrees vary. Everything more colourful — Dorian, Mixolydian, the altered scales — is handled as evidence about which notes are likely, not as a separate tonality to decide between. The finer reading is not thrown away: it is published, so the display can tell the user that a passage read as D minor would, unrounded, be called D Dorian.

---

## D-525 — The fit is STAGED: the factor tables are counted from ground truth and frozen, and only a small vector of combination weights is fit discriminatively — with an all-weights-equal ablation arm that must be beaten

**As decided, in the words it was decided in:**

```
**Fitting parameterization (user-ratified 2026-07-19).** The staged form: **the factor TABLES are fit
generatively from ground-truth counts and frozen** (each table established on its own — the
key-conditioned chord-transition table, the bass-note-given-chord-and-inversion table, the tone-category
emission tables, the key-change table — every entry a musically meaningful probability, per the
published forms); **the small vector of COMBINATION WEIGHTS over the factors is fit discriminatively by
convex conditional likelihood** (the semi-Markov conditional-random-field objective with the logarithms
of the frozen tables as features; L2 penalty; the OI-176 held-out gate and OI-177 capacity budget
govern). **Mandatory ablation arm:** all-weights-equal-one IS the pure generative model, so the weight
layer's contribution is measured on held-out data inside the same machinery, never assumed — its
adoption is gated on winning that comparison. **Ledger entries attached to the decision:** (a) the
staged ASSEMBLY is our synthesis (each stage established separately in the literature; the combination
is an assumption with its own #17b prediction); (b) constrained-optimum record — the unconstrained
alternative is the fully joint discriminative fit with rich free features (possibly a higher ceiling),
excluded because fully joint weights sacrifice the modular diagnosability (#3/#19) the error-correction
loop runs on; re-test if that constraint stops binding; (c) fit-scope declaration (the Noland &
Sandler lesson): which components may be re-fit is declared before any fit — tables from counts, once,
frozen; only the combination weights move; (d) the direct-metric few-weight search (the minimum-error-
rate protocol with bootstrap confidence intervals) is the established fallback if the likelihood-fit
weights measurably disagree with the reported metric.
```

**In plain words:** Each table of probabilities is counted from the annotated corpus and then frozen. On top of them sits a short list of weights saying how much each kind of evidence counts, and only those are trained. Because setting every weight to one is exactly the untrained model, the trained weights have to beat that on held-out music before they are adopted at all.

---

## D-526 — The joint state's chord axis is SCALE-DEGREE-VALUED — a Roman numeral relative to the state's own tonic and mode — and the chord symbol is a DERIVED fact published once

**As decided, in the words it was decided in:**

```
**Chord state is scale-degree-valued (user-ratified 2026-07-19).** The joint state's chord axis is a
**Roman numeral — scale degree, quality, inversion — relative to the state's tonic and mode** (the
Raphael-Stoddard / Harasim structure). Consequences, all structural: (a) the tonic/degree coupling
terms (the diatonic-root bonus, `buildChordResult`'s degree, Gate G-E's degree condition,
`applyTonicPriorToSparseChord`, the segmenter's head-gap tonic prior — the gap map's group 1) dissolve
by construction — a degree is key-relative by definition; (b) **transposition invariance**: the chord-
transition table pools all keys' evidence (twelvefold counts per cell — the decisive capacity device on
a 326-piece corpus); (c) the ground truth is natively degree-valued, so tables fit from counts with no
conversion layer, and the OI-173 defect class (four inequivalent `diatonicToKey` definitions, two of
`degree`) is never rebuilt. **The chord symbol (root pitch class, quality, bass) is a DERIVED fact,
published once** (root = tonic + the degree's interval) — the robust stop's root metric is unchanged
and every baseline column stays comparable. **Tonicization is applied-degree classes** (the secondary
dominant V/x, applied leading-tone chords, and the standard chromatic classes — Neapolitan sixth,
augmented-sixth chords — per the ground truth's own vocabulary; this also matches jazz analytical
practice, where the secondary dominant, and later the substitute dominant and extended dominant chains,
are applied-degree devices — jazz-specific classes enter only under the OI-7 jazz-ground-truth gate).
**Excluded alternatives recorded:** root-valued chord state (forfeits transposition tying and
structurally preserves the ad-hoc key coupling the audits condemned); momentary modulation for
tonicization (fits Bach acceptably but shreds jazz tonicization chains into micro-keys and departs from
the ground truth's labeling convention).
```

**In plain words:** The estimator decides chords as scale degrees within the tonality it is considering, not as absolute chord roots. The ordinary chord name is then worked out from the degree and published once. Two things follow by construction: the terms that used to couple a chord to a key dissolve, because a degree is key-relative already; and evidence from every key pools into the same table, which is what makes counting on a corpus of this size possible.

---

## D-527 — There is NO live non-chord-tone cleaning stage: each tone is emitted by category inside the one decode, conditioned on chord-independent melodic and metric covariates, and ornament labels are derived AFTER it

**As decided, in the words it was decided in:**

```
**Non-chord-tone handling (user-ratified 2026-07-19).** **No live cleaning stage exists.** Non-chord
tones live INSIDE the pitch-emission factor: each tone is emitted by category (chord member vs
within-scale non-chord tone vs outside-scale tone — the Raphael-Stoddard structure), with the emission
probability conditioned on **chord-independent melodic and metric covariates** — stepwise approach and
departure, chromatic-neighbor motion, metric weakness, the tied-over/syncopated preparation (the
figuration-feature forms Masada & Bunescu fit on chorales; every covariate computable without knowing
the chord, so no circularity). Chord identity and tone status are decided together in the one decode
(#12 — no ornament verdict is ever committed early). **Ornament labels (passing tone, neighbor tone,
suspension, appoggiatura, pedal point) are derived AFTER the decode** from the committed chord by the
standard definitions and published as a derived fact for the presentation layer — the same pattern as
the modal-color publication. **Style adaptation is values-only:** the chord-tone boundary shift in jazz
(tensions as chord members) is a VOCABULARY matter handled by the degree-valued quality classes; the
changed ornamental/metric conventions (enclosures, anticipations) are covariate TABLE VALUES refit per
preset — same structure, no per-style rule code; jazz-specific covariate additions enter only under the
OI-7 jazz-ground-truth gate with their own ledger entries. **Establishment resource:** the BCMH
reduction is the chorales with non-chord tones removed — aligning the 87 overlapping full-texture
stems against their reductions yields empirically labeled chord-tone/ornament data for fitting and
validating these emission tables (BCMH's declared instrument status applies). **Excluded alternatives
recorded:** a live pre-cleaning stage (the published cleaners' ~28 % error rate would be hard-committed
upstream, violating #12, and the suspension's chord-relative definition makes pre-cleaning circular);
pure category emission without melodic covariates (discards the established voice-leading evidence —
the strongest ornament discriminator).
```

**In plain words:** The estimator does not first decide which notes are decoration and then read the chord from what is left. Every sounding note is scored by what kind of tone it would be under the chord being considered, using only facts computable without knowing the chord — how it is approached and left, how weak its metrical position is, whether it is tied over. Chord and tone status are settled together, and the ornament names are worked out afterwards from the committed chord.

---

## D-528 — The key signature and declared mode enter as a WEAK FITTED SOFT PRIOR with no conditional gate anywhere — the probability calculus delivers 'consult it only when unsure', and the hard declared-mode wall is formally retired

**As decided, in the words it was decided in:**

```
**The key-signature and declared-mode prior (user-ratified 2026-07-19).** A **weak, fitted,
transposition-invariant soft prior on (tonic, mode)** from the notated signature — a small categorical
table (local-key tonic distance from the signature's relative pair on the circle of fifths, by mode)
counted from ground truth; the declared mode, where the score carries one, is a second conditioning
input with its own fitted strength. **No conditional gate and no threshold anywhere:** the user's
intent — the signature consulted only where the analysis is otherwise unsure — is delivered by the
probability calculus itself (a weak prior is negligible where the content likelihood is decisive and
tips the scale only where the evidence is ambiguous), never by an "if uncertain" code path. Bach's
modal notation practice (the Dorian chorale written one flat short) is handled statistically as
measured mass one fifth away in minor — no special case. A mid-piece signature change re-anchors the
prior (discharging the OI-94(a) deferral). **The signature-influence rate is measured by ablation and
published at every fit** (the fraction of committed keys the signature factor changed), with the
recorded expectation that it is SMALL — a large fitted weight or influence rate is a #3 finding to
investigate, not to ship. **The declared-mode wall (the −7 hard penalty) is formally retired.**
```

**In plain words:** The written key signature is used as a gentle nudge whose strength is counted from the corpus, not as a rule and not behind an 'if the analysis is unsure' branch. A weak prior is negligible where the notes are decisive and tips the balance only where they are not, which is exactly the intended behaviour without any threshold. The old hard penalty for contradicting the declared mode is retired.

---

## D-531 — The hand-built emission is CONFIRMED and the learned replacement is NOT triggered — retained as an explicit fallback with a concrete trigger, and scoped to one repertoire with a named re-check gate

**As decided, in the words it was decided in:**

```
**The standing verdict on this principle's own live case: the hand-built analysis is CONFIRMED and
the learned replacement is NOT TRIGGERED — it is retained behind this interface as the explicit
fallback, with a concrete trigger.** The substitution this section exists to keep possible was put
to a measured test on the analysis front — go on improving the hand-built scorer, or replace it
with a trained model. The measured answer is to keep the hand-built one: the error mass decomposes
into causes reachable within it, and the bucket that would genuinely need a learned model came back
empty on the sample. The learned option is **not withdrawn**; it stays a drop-in behind the
interface, and it re-opens for **any slice later established as a genuine ceiling**. *Why:* decided
on measurement, with the measurement's own limits stated as part of the decision — the corrected
metric showed the residual had been inflated by already-correct artifacts and by mis-attributed
cases, the empty bucket is a sample carrying a stated corpus upper bound, and the algorithmic
second opinion fails the same functional roots, which makes it a missing-layer problem rather than
a ceiling of the vertical scorer. **Two limits ride with the verdict and are part of it:** the
decomposition covers one repertoire only, and the fallback's advantage is concentrated on the
harder chromatic material that was not decomposed; and the corrected metric must be **committed
before any fitting**, or the fitter optimises against cases that do not exist.
```

**In plain words:** The open question was whether to keep improving the hand-written scorer or replace it with a trained model. The measured answer is to keep the hand-written one: the error mass decomposes into causes that are fixable within it, and the bucket that would need a learned model came back empty on the sample. The learned option is kept as a stated fallback, to be reconsidered for any slice later shown to be a genuine ceiling.

---

## D-532 — The chord-transition table gains one pooling level that groups a secondary dominant's continuations by their RELATION to its target — restoring from counts the one behaviour that defines the chord class

**As decided, in the words it was decided in:**

```
**The chord-transition table carries one pooling level for a secondary dominant's continuations,
grouped by their RELATION to the target.** A secondary dominant's continuations are pooled across
all targets as *resolves to the chord it is the dominant of* versus *moves elsewhere*, and the
counting is re-run at that level. *Why:* as counted without it, every secondary dominant is too
rare on its own to hold a row, so its continuations fall into the general chord-frequency list and
the table reads the same probability for resolving to the target as for going anywhere else — it is
blind to the one behaviour that defines the chord class. The defect was verified directly in the
table and its cost measured in a checked passage, where the blindness taxed the correct reading.
Two alternatives are excluded on stated grounds: leaving it to the weight layer cannot work,
because a weight can only scale what a table says and cannot restore a distinction the table does
not contain; and hand-setting a resolution probability would recreate exactly the class of
unestablished constants the fit exists to eliminate. The pooling reuses the mechanism the table
design already rests on — counting the same pattern across transpositions — so it adds no new kind
of machinery (#6), and the counts are ample enough that the added cells satisfy the ratified
capacity budget.
```

**In plain words:** As counted, every secondary dominant was too rare on its own to keep its own row, so all its continuations were merged into the general chord-frequency list. The consequence is that 'the dominant of X moving to X' and 'the dominant of X moving anywhere else' read the same probability — the table is blind to what makes the chord a secondary dominant at all. One extra grouping level, pooled across all targets, restores the distinction from real counts.

---

## D-533 — A continuation too rare to have its own stored probability is scored by dividing the row's leftover in PROPORTION to each chord's overall frequency — never evenly, and never as impossible

**As decided, in the words it was decided in:**

```
**A continuation too rare to have its own stored probability is scored by dividing the row's
leftover in PROPORTION to each chord's overall frequency in that mode — never evenly, and never as
impossible.** Each row of the transition table ends in one pooled probability covering everything
too rare to store; when the decode meets a specific rare continuation it turns that pooled value
into a number for that continuation in proportion to how common the chord is generally. *Why:* it
is the standard construction in published back-off models of sequences (#1), and it uses
information already held — a common chord is genuinely a likelier unseen continuation than a rare
one (#12). Both alternatives are excluded on facts: dividing evenly asserts that a rare and a
common chord are equally likely, which the corpus counts contradict; and treating an unseen
continuation as impossible is factually wrong on a corpus of this size and technically fatal, since
a zero destroys any path through it.
```

**In plain words:** Each row of the transition table ends with one pooled probability covering everything too rare to store on its own. When the decoder meets one specific rare continuation it must turn that pooled value into a number for that continuation. It does so in proportion to how common the chord is generally.

---

## D-534 — The penalty for a chord tone that never sounds is COUNTED per chord factor — root, third, fifth, seventh — replacing one invented blanket number; the per-factor asymmetry then comes free

**As decided, in the words it was decided in:**

```
**The penalty for a chord tone that never sounds is COUNTED PER CHORD FACTOR — root, third, fifth,
seventh — and not carried as one blanket value.** Across every humanly labelled chord segment in
the ground-truth corpus, the fraction in which each of the chord's own factors actually sounds is
counted, per chord family (triad versus seventh chord). *Why:* the data is already on disk — the
labelled segments record which notes sound, and the label itself names the chord's factors — so the
counting is direct rather than inferred, which replaces a value invented for a worked example with
an established one (#19). The musical point is what makes per-factor counting the right shape: the
factors are not symmetric and the counts encode that automatically — a seventh is what earns a
seventh-chord label, so a silent seventh is near-prohibitive; the fifth is the factor four-part
writing routinely omits, so its penalty is mild; the third sits between. One blanket number cannot
express any of that, and the invented value demonstrably carried load — a checked passage's margin
moves with it. **The scope limit rides with the values and is part of the decision:** these are
Bach-chorale counts, no jazz values can be counted because no jazz ground truth exists, and that
limit stays declared on the artifact.
```

**In plain words:** Judging a candidate chord means weighing notes that sound but do not belong to it AND chord notes that never sound at all. The second direction was answered by a number invented for a paper walkthrough. It is replaced by counting, for every humanly labelled chord segment in the corpus, how often each of the chord's own factors actually sounds.

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

## D-536 — The bass note and the chord are chosen TOGETHER — the winner is the (bass, root, template) triple — replacing the sequential commit-the-bass-then-score pipeline

**As decided, in the words it was decided in:**

```
**★ THE DECISION THIS SECTION RECORDS, STATED AS A RULE — the bass and the chord are chosen
TOGETHER, as one (bass, root, template) triple (re-homed into this specification 2026-08-07 on the
user's ruling). ⚠ LEGACY subject — this scorer is dormant on both production surfaces.** The
analyzer does **not** commit to a bass and then score chords against it. It enumerates the
plausible bass candidates and the whole root × template grid against each, and the winner is the
best **(bass, root, template)** triple under the composite score. *Why:* both defects that forced
it are diagnosed to the same cause and named with it — a passing note that happens to be the
absolute lowest pitch wins bass selection over the beat-onset bass a step above it, flipping the
chord root; and an incomplete slash-chord reading beats a complete root-position triad because
root-position completeness earned no advantage. **Neither is reachable while the bass is committed
before the chord is scored**, which is what makes this a structural decision rather than a
weighting one. The cost is stated with it and judged acceptable: a few times the scoring loop. It
is the same principle the production estimator carries on its own terms — coupled quantities are
decided together rather than one being committed early.
```

**In plain words:** The analyzer used to pick the bass note first and only then score chords against it. Two confirmed misreadings both came from that order. It now enumerates the plausible bass notes and the chord candidates together and takes the best combination.

---

## D-537 — The completeness bonus fires ONLY for a root-position reading whose three triad tones are all present — the guard that stops it from demoting genuine slash chords

**As decided, in the words it was decided in:**

```
**★ THE GUARD IS THE DECISION, AND IT IS STRUCTURAL RATHER THAN A THRESHOLD (re-homed into this
specification 2026-08-07 on the user's ruling). ⚠ LEGACY subject.** The completeness bonus fires
**only** for a **root-position** reading — the candidate bass IS the triad root — whose three triad
tones are all present above the presence threshold. A genuine slash chord therefore neither gains
the bonus nor is beaten by a rival reading that gains it wrongly. *Why:* derived from a measured
failure rather than chosen. The previous, unconditional version of the same idea caused large
regressions in both directions because it promoted cases where the slash-chord reading was the
correct one; the design works the guard through the exact case that failed and shows that a genuine
slash chord with its own fifth present does not collect the root-position bonus for the rival
reading. It is an early instance of the standing rule that a correction is given a **structural
entry condition** rather than a widened threshold (`CLAUDE.md`, the gate and preset policy).
```

**In plain words:** The bonus that rewards a chord for having all of its notes present applies only when the candidate bass IS the chord's root and all three tones are above threshold. A genuine slash chord therefore neither gains it nor is beaten by a reading that gains it wrongly.

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

## D-565 — Exact score ties in the decode are real and are broken by a declared TOTAL ORDER on paths, implemented identically in every decoder — no epsilon, no platform dependence

**As decided, in the words it was decided in:**

```
**The tie-break rule (user-ratified 2026-07-20 at the C++ module build's parity finding):** exact
score ties between candidate decodes are real (proven at 8 corpus pieces — equal-score
segmentations differing by one boundary on repeated-chord runs) and, unbroken, they make the
committed output depend on the platform's floating-point library — unacceptable for the
diff-based adoption measurement and regression stops (#16, reproducibility). Equal-score
candidates therefore resolve by a declared TOTAL order, implemented identically in every decoder
of this specification: fewer segments first; then the earliest boundary-tick sequence
(lexicographic); then the canonical class-key order of the state sequence. No epsilon, no
platform dependence — a pure order on paths.
```

**In plain words:** Two different readings of a piece can come out exactly equal, and this happens in real music. Left unresolved, which one the program commits to would depend on the machine's floating-point library. So ties are settled by a fixed rule applied in the same way everywhere: prefer fewer segments; if still tied, prefer the earlier sequence of boundary positions; if still tied, prefer the canonical ordering of the states.

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

## D-571 — The declared-mode influence becomes a small additive hint, and SMALLNESS IS THE GATE — no separate confidence test is added

**As decided, in the words it was decided in:**

```
  and keep it as the only declared influence on the 252-candidate score. A small magnitude makes it a
  genuine **tiebreaker**: it can only flip the winner when the raw note-based gap is already within ~1.0
  (i.e. "when genuinely unsure"), and it cannot override clear note evidence. No explicit confidence
  gate is needed — smallness *is* the gate. Keep the application point unchanged. (Optionally rename to
  `declaredHintWeight` for honesty; mechanically identical.)
```

**In plain words:** The written major/minor declaration used to override note evidence outright. It becomes a small bonus instead. Because it is small, it can only decide a case where the evidence was already almost balanced, and it cannot overturn a clear reading — so no extra rule is needed to say when it may apply. Its smallness is that rule.

---

## D-572 — The hard post-hoc declared-mode promotion is REMOVED OUTRIGHT rather than kept in a gated form

**As decided, in the words it was decided in:**

```
**Tried and closed on the declared mode's weight, and it is a SECOND removal at the same increment
— do not retry; the register carries it with its evidence: D-572 (the hard post-hoc "strong
declared-mode prior" promotion, which moved the highest-ranked declared-compatible result to the
front REGARDLESS of the candidate-score gap, REMOVED OUTRIGHT rather than kept in a gated form).**
```

**In plain words:** A step that took the best reading agreeing with the written major/minor declaration and pushed it to the front regardless of how badly it had scored was deleted, not softened. Keeping any version of it would have made the demotion of the declaration pointless wherever the note evidence had already won.

---

## D-575 — The Baroque partial-signature convention is handled by DETECTING it and reinterpreting the signature one step, not by widening the candidate family for every score

**As decided, in the words it was decided in:**

```
**★ THE BAROQUE PARTIAL-SIGNATURE CONVENTION IS HANDLED BY DETECTING IT AND REINTERPRETING THE
SIGNATURE ONE STEP, NEVER BY WIDENING THE CANDIDATE FAMILY FOR EVERY SCORE (re-homed into this
specification 2026-08-08 on the user's ruling). ⚠ LEGACY, AND SUPERSEDED IN FACT: the correction is
applied inside the legacy resolver, which the production arm no longer runs; no ruling superseded
it, a later build replaced what it governs. Whether the joint estimator handles the convention AT
ALL is NOT settled by this entry and is not asserted here.** Baroque scores are often notated with
one accidental fewer than the modern convention, so the sounding key sits one step to the sharp side
of anything a signature-faithful reading could name. The adopted handling DETECTS that situation —
the flattened sixth degree pervasive across the sounding weight and dominating its natural form —
and reinterprets the written signature one step toward the missing accidental for the whole
resolution.
```

**In plain words:** Baroque scores are often written with one accidental fewer than the modern convention, so the true key sits one step to the sharp side of anything the analysis could name. The fix adopted detects that situation — the flattened sixth degree being pervasive and dominating its natural form — and reinterprets the written signature accordingly. The alternative considered and not taken was to let every score choose from two signature families, which would have added a competitor to correctly-written music as well.

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

## D-580 — Two of the twelve post-scoring gates are purely-local vertical refinements and MUST survive the dissolution; the other ten dissolve into the competition

**As decided, in the words it was decided in:**

```
- **Two of the post-scoring gates are PURELY-LOCAL VERTICAL refinements and must SURVIVE the
  dissolution; the others dissolve into the competition. Recorded DEFERRED.** Most of the
  after-the-fact repair steps exist only because the decision preceding them could not see enough
  context, and they disappear once that decision can. Two do not: they refine the reading from the
  notes alone and compensate for nothing, so they are carried across rather than deleted alongside
  the others. *Why:* measured at the code rather than assumed from the design — of the live gates,
  ten read context from beyond their own stretch and are compensation by construction, three were
  already dead code, and the two named ones read nothing outside the sonority. **The dissolution
  was never executed on this path** — the production estimator replaced the pipeline instead — so
  the constraint stands DEFERRED and what it says about those two gates is a fact about this code
  that the retirement map still has to dispose of (#12). One bookkeeping fact a reader needs: the
  *partner-present* half of one of the two named gates has since been unified into the single
  promotion primitive (§6a), so the surviving rule name for that flip is FM2; the unification did
  not perform the dissolution and does not discharge this constraint.
```

**In plain words:** Most of the after-the-fact repair steps in the old chord path exist only because the decision that preceded them could not see enough context, and they disappear once that decision can. Two do not: they refine the reading from the notes alone and are not compensation for anything. Those two must be carried across, not deleted alongside the others.

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

## D-600 — The quality-overwrite information-loss violation is TOLERATED until the gate-dissolution step and stays VISIBLE in the open-items register — tolerated is not forgotten

**As decided, in the words it was decided in:**

```
Two post-scoring passes change the chord quality the scorer committed and keep no record of what
they replaced, which is an information-loss violation (#12). **The verdict is to TOLERATE it until
the gate-dissolution step, with the violation kept VISIBLE in the open-items register — tolerated is
not forgotten.** *Why, as a derivation from three principles rather than a preference:* removing the
overwrites now would be a production behaviour change with no replacement owner, since no component
yet owns deciding quality from the key — which is the cross-layer patch layer adherence forbids
(#7); and #8 puts the structural work first. Deferring to the step that gives the concern a single
home makes the removal ONE ratified, revertible change under the regression stop (#14/#15). The
alternative — ripping the overwrites out now — was considered and rejected on exactly that ground.
**The open-items register row is the mechanism that makes this an acceptance rather than an
oversight**, and it gates the dissolution.
```

**In plain words:** Two later passes change the chord quality the chord stage committed and keep no record of what they replaced, which is information loss. It is left in place for now rather than ripped out, because there is no other component yet that owns deciding quality from the key, and removing it now would be a patch across stages. The violation is kept on the open-items list so that leaving it is a decision and not an oversight.

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

## D-605 — The local-key hypothesis derives from key-agnostic signals ONLY and never from the key-area grouping, which is a post-grouping of the resolved key — a hard design rule, not a preference

**As decided, in the words it was decided in:**

```
- **A local-key hypothesis derives from KEY-AGNOSTIC signals only, and NEVER from the key-area
  grouping — a hard design rule, not a preference.** Deciding that a passage has moved to another
  key may use the cadence detector, which is key-agnostic by construction, and the raw region
  structure — root motion, diatonic-collection consistency. It may **not** read the key-area
  grouping, which is a downstream post-grouping of the already-resolved key. The flow stays
  strictly feed-forward: chords → key-agnostic cadence → local-key hypothesis → re-keyed key path →
  key areas, rebuilt downstream. *Why:* named in the decision as the load-bearing soundness
  property, and the circularity is concrete rather than argued — the grouping is built FROM the
  resolved key, so a detector reading it would find the key it was given. It is the same discipline
  that made the cadence detector usable, applied to the local-key hypothesis and naming the exact
  surface that would make it circular. **Scope:** the mechanism this rule was written for sits on
  the legacy key path, but what it constrains is *what evidence a modulation decision may read*,
  which binds any such decision on any arm.
```

**In plain words:** Deciding that a passage has moved to a new key may only use evidence that does not already assume a key: the closure detector, which works without being told the key, and the plain shape of the music. It may not read the key-area grouping, because that grouping is built FROM the key already decided — using it would mean the detector confirming its own input.

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

## D-616 — A global tonic anchor enters key scoring at RESOLVER/SECTION scope — never as one more local term inside the window scorer, which is what re-enters the coupling that defeated the local levers

**As decided, in the words it was decided in:**

```
- **A global tonic anchor enters key scoring at RESOLVER / SECTION scope — never as one more local
  term inside the window scorer. ⚠ LEGACY: both mechanisms it names are legacy-scoped.** Evidence
  about which key a whole section or piece is in is applied where the section is decided — the
  scope the removed declared anchor occupied — gating the relative-major/minor choice; the
  per-window candidate scoring is left unchanged. *Why:* measured, at the attempt that failed —
  local reweighting was shown unable to carry the relative-major/minor decision, because that floor
  is made of near-ties and any local term strong enough to win them without the mode present also
  overrides the correct reading when it is present. Adding the anchor as one more local term
  re-enters exactly that coupling. The design attaches a proof obligation to the rule: show that
  the anchor reinforces the mode-present cases rather than regressing them. **The LEGACY mark
  follows a check at the code, not the decision's age:** the window scorer this rule excludes
  (`KeyModeAnalyzer::analyzeKeyMode`) is reached only through the legacy resolver and this layer's
  dormant sequence decoder, and the resolver is retired from the production region path — so
  neither named mechanism is on an arm that runs. The rule about WHERE a section-scoped prior is
  applied binds any such prior the key axis later gains.
```

**In plain words:** Evidence about which key a whole passage is in is applied where the passage is decided, not inside the per-window scoring that ranks candidate keys note by note. Adding it as one more local term is what failed before: any local term strong enough to settle a near-tie when the mode is unknown also overrides the correct answer when the mode IS known.

---

## D-622 — The reach-back convergence PROXY was measured FALSE and dropped — the as-built tracks the leading-edge key itself and stops when it stops changing

**As decided, in the words it was decided in:**

```
- **The reach-back convergence PROXY was measured FALSE and is dropped; the as-built tracks the
  leading-edge key itself and stops when that stops changing.** The cheaper stopping rule proposed
  in design — *a settled, stable prevailing key is in view in the reached-back region* — was
  measured and disproved: one settled indication of context does not anchor the leading edge, which flips
  only once a confident earlier key is established over a **run**. So the facility uses the
  headline criterion directly and no proxy. *Why:* measured at the build, and the methodological
  reading is recorded with the result — the proxy was an unlabelled assumption, it was measured, it
  was false, and it was dropped; a determinism test over extension step size is what validates the
  criterion that replaced it. This is the finding that supersedes the proxy clause of the
  bounded-context contract's convergence item; that contract now records the clause as tried and
  closed, and its headline rule — reach back until the answer stops changing, never by a chosen
  amount — is unchanged.
```

**In plain words:** When the analysis has to read backwards for context, it needs a rule for when it has read far enough. The cheap rule proposed in design — stop once a settled key appears anywhere in the material read back — was measured and found to stop too early: one settled measure does not fix the key at the edge of the selection, which only settles once a confident earlier key is established over a stretch. So the built code checks the thing that actually matters and stops when that stops moving.

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

## D-629 — The resolver of carried uncertain readings IS the function layer itself — there is no distinct gated box between the note layers and it

**As decided, in the words it was decided in:**

```
**★ THE RESOLVER OF CARRIED UNCERTAIN READINGS IS THIS LAYER ITSELF — THERE IS NO DISTINCT GATED BOX
BETWEEN THE NOTE LAYERS AND IT (re-homed into this specification 2026-08-08 on the user's ruling).**
When the earlier layers cannot decide between two readings they carry both forward with an
uncertainty mark. **What resolves them is this layer, as part of assigning function**: it reads the
carried alternatives and the marks at its gated entry, assigns function under each carried
key/chord reading, and keeps the reading whose functional and cadential analysis is coherent. The
"gated step" language elsewhere in the specifications describes **this layer's gated entry**, not a
separate layer.
```

**In plain words:** When the earlier stages cannot decide between two readings they hand both forward with a mark. The thing that then picks one is not a separate component: it is the function stage, choosing as part of naming the harmony. The wording elsewhere about a gated step describes the point at which that stage begins, not another stage.

---

## D-656 — The crediting rule is NOT amended to count a tonicization label as agreeing with the annotator's modulated numeral; only a diagnostic partial-sub-split is defensible

**As decided, in the words it was decided in:**

```
**★ THE CREDITING RULE IS NOT AMENDED TO COUNT A TONICIZATION LABEL AS AGREEING WITH THE
ANNOTATOR'S MODULATED NUMERAL; ONLY A DIAGNOSTIC PARTIAL-SUB-SPLIT IS DEFENSIBLE** (2026-06-14; the
record states no ratifier for the decision itself. Homed here 2026-08-09 on the user's ruling —
Ruling 11 of `cowork_rulings_2026_08_09_second_stop.md` — as the MEASUREMENT half of register entry
**D-291**, whose BUILD half belongs to the Layer-5 function specification and is not restated here,
#6. **SPLIT INTO TWO REGISTER IDENTIFIERS 2026-08-09** on the user's Ruling 21 of
`cowork_rulings_2026_08_09_fourth_stop.md`: this half now carries its own entry, **D-656**, and
**D-291** keeps the build half; the two cross-reference each other, and neither text changed).
Where our analysis labels an applied chord relative to the home key and the human annotator
has changed key, the comparison is **not** to be changed so that the label counts as agreement.
```

**In plain words:** Where our analysis names an applied chord relative to the home key and the human annotator has changed key, the accuracy comparison is not to be altered so that our label counts as agreeing. Only a diagnostic that splits such cases out and exposes the masking is defensible. This is the measurement half of a decision whose build half — leaving the labeller unwired — belongs to the function layer's specification.

---

## D-660 — A research-tied name is not renamed but is governed by a two-tier rule, and the terminology cleanup runs in a fixed order with no tree-wide rename

**As decided, in the words it was decided in:**

```
**★ WHAT HAPPENS TO A NAME BORROWED FROM THE PUBLISHED RESEARCH, AND IN WHAT ORDER THE CLEANUP
  RUNS (user-ruled 2026-08-09; the ruling record is `cowork_rulings_2026_08_09_fifth_stop.md`,
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
