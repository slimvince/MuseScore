# Investigation — is the "uncertain" resolver Architectural Layer 5, or a distinct gated step? (open item O1)

> **The question.** Both the Layer-3 and Layer-4 specs hand their unresolved slices forward — carried alternatives
> plus an "uncertain" mark — to a step that *selects* among those alternatives using functional/cadential evidence.
> That step is named three ways across the specs ("the later gated key-and-chord step," "the function layer,"
> "Architectural Layer 5"). The architecture must fix **one** answer: is the resolver **Architectural Layer 5
> (function) itself**, or a **distinct gated step** sitting between the note-layers and Layer 5?
>
> **Status: RESOLVED — user-ratified 2026-06-24.** Parts 1, 2, and 4 below (design + literature, Cowork) reached the
> verdict; part 3 (the corpus measurement, `cc_uncertain_resolver_measurement_report.md`) **confirmed** it (every
> separable cue the residual exposes is owned by Layers 1–4; the function-only remainder is small and structural).
> Cowork spot-verified one reclassified case at the score (`bwv10.7@36000` — a 5-note-scale over-grab, not function
> residual). **Verdict: the resolver is Architectural Layer 5 (function) itself; no distinct box.** The three names
> have been collapsed to "Architectural Layer 5" across the Layer-3 and Layer-4 specs; the cross-layer-budget finding
> is recorded in CLAUDE.md and the Layer-4 testing section.

## The decisive test, and the lens

The project's own invariant decides layer identity: **each layer owns one `(evidence-source × question)` contribution.**
So the test is single:

> **Is selecting the right key/chord reading *separable* from naming function, or *co-determined* with it?**

- **Co-determined** — you cannot name the function without first picking the reading, *and* picking the reading needs
  the functional/cadential evidence. That is a circular dependency, which can only be discharged by **one joint
  computation**. Same evidence (function/cadence), same question (which reading is functionally coherent) → **the
  resolver is Layer 5 itself.**
- **Separable** — some criterion that is **not** function can pick the reading on its own. That criterion is a
  distinct `(evidence × question)` and earns **its own gated step** ahead of Layer 5.

**Minimality sets the default and the burden.** Do not add a box. The resolver is presumed to be Layer 5 unless part 1
or part 3 exhibits a residual class resolved by a separable, non-function criterion. The burden is on finding that
class; absent it, no new box.

## Part 1 — enumerate and classify the residual (design, from the specs)

The carried-ambiguity classes are already named in the Layer-3 spec (§11) and Layer-4 spec (§5). For each: what
resolves it, and is that evidence Layer 5's (function / cadence / progression) or something separable?

| Residual class | From | What resolves it | Evidence type |
|---|---|---|---|
| Relative major vs relative minor (same-collection tonic) | L3 | Which tonic receives the cadential confirmation (V→I) | **Function / cadence** |
| Tonicization vs modulation (key-area boundary) | L3 | Whether a cadence confirms a new key area, or the chord is a secondary dominant inside the home key | **Function / cadence** |
| Unspelled dim7 / augmented rotation (spelling absent or contradicted) | L4 | Which rotation functions in context (e.g. `vii°7` of which key; a common-tone diminished) — the spelled cases are already pinned in L4, so only the *function-dependent* remainder reaches here | **Function** |
| Share-tone pairs `V6`↔`vii°`, `iii`↔`I6` | L4 | Which Roman numeral the chord *is* — this **is** the function question | **Function (definitionally)** |

Every class resolves on functional/cadential/progression evidence — Layer 5's evidence. The share-tone pairs are the
sharpest case: naming the function `V6` versus `vii°` **is** selecting the reading, so here selection and
function-naming are not merely co-located, they are the *same act*. No class, on the face of the specs, is resolved by
a criterion outside function. (Part 3 tests this empirically, since the table is a design claim, not a measurement.)

## Part 2 — the circularity check (the crux)

For the key-side residuals (relative major/minor; tonicization vs modulation) there is a dependency circle:

- To **name function**, you need the **key** (a Roman numeral is a chord *read in a key*).
- To **pick the key** in exactly these residual cases, you need the **cadence / functional reading** (the cadence is
  what tells relative major from relative minor, and what tells a confirmed modulation from a passing tonicization).

A circle of that shape cannot be discharged by running one side and then the other in a fixed order — neither side is
prior. It is discharged only by a computation that decides key-reading and function **together**: assign function under
each carried key/chord alternative, and keep the alternative whose functional reading is coherent (a cadence lands, the
progression parses). That joint computation **is** functional analysis. So for the key-side residuals the resolution is
**co-determined with function**, not separable — which, by the decisive test, places it **in Layer 5**.

The chord-side residuals (share-tone pairs, function-dependent dim7 rotation) are even more directly Layer 5: the thing
that resolves them is the Roman-numeral reading itself.

So part 2 finds **no separable non-function criterion** in any class. The circle, not a fixed order, is the reason —
and a circle means one joint layer.

## Part 4 — literature placement (grounded in what we have)

Two lineages, one conclusion:

- **Joint neural models bundle it into one functional step.** AugmentedNet (Nápoles López et al., ISMIR 2021) and the
  GNN successors co-predict key, chord, inversion, and Roman-numeral degree in **one** model — they do not run a
  separate key/chord-disambiguation pass before a function pass. The decomposed pipeline we are building deliberately
  *defers* that joint prediction to "the gated step" rather than using an opaque net — but the literature's own
  structure says the disambiguation lives **inside** the functional prediction, not before it.
- **Decomposed pipelines resolve the residual with functional rules, not a separate selection box.** Our compiled
  Contrapunctus findings (`contrapunctus_findings.md`, §5) report that the residual chord-ID error is
  "candidate/emission-level or key-level, **not selection-level**," and that the un-resolved cases "need a candidate
  never surfaced → **functional rules**, not re-weights." A standalone re-ranking/selection layer was built, measured,
  and found **saturated** (a near-no-op). That is direct evidence *against* a distinct selection step and *for* the
  residual being discharged by functional analysis. Classical pipelines (Temperley/Melisma; Pardo & Birmingham's
  HarmAn carrying multiple labels and deferring) likewise resolve harmonic ambiguity within the harmonic/functional
  reading, not in a separate pre-pass.

*(Flag: the AugmentedNet/GNN architectural claim is from the literature as we have catalogued it; the
Contrapunctus claims are quoted from our own findings doc. Neither requires a new literature pull; if the verdict is
contested, re-confirm the specific AugmentedNet pipeline-ordering claim against the paper.)*

## Provisional verdict (gated on part 3)

**The resolver is Architectural Layer 5 (function) itself — there is no distinct gated box between the note-layers and
Layer 5.** Layer 5 reads the carried alternatives and the "uncertain" marks at its **gated entry**, and resolves them
**as part of** assigning function: it assigns function under the carried key/chord readings and keeps the reading whose
functional/cadential analysis is coherent. The "gated step" language in the specs describes *Layer 5's gated entry*,
not a separate layer. This satisfies minimality (no new box), the `(evidence × question)` invariant (same evidence,
same question), and the forward-only contract (Layer 5 selects among carried alternatives; it does not re-enter L3 or
L4).

**What this means for the specs (on ratification):** replace the three names everywhere with **one** — "Architectural
Layer 5 (function)" — and state once that resolving the carried "uncertain" key/chord readings is part of Layer 5's
job, performed at its gated entry, using functional evidence the note-layers structurally lack.

## What part 3 measures, and what would overturn the verdict

Part 3 (read-only, corpus, handed to Claude Code) tests the part-1 table empirically against the ground-truth
functional analyses, *without* relying on our own cadence detector (verified unusable earlier). For each
carried-ambiguity case it asks: **does the correct reading coincide with the one under which the ground-truth
functional analysis is coherent** (a cadence lands / the progression parses), and **is the disambiguating cue
functional, or something separable** (pure voice-leading, spelling, metric position alone)?

- **Confirms the verdict** if the disambiguator is functional in essentially every case → resolver = Layer 5.
- **Overturns it, partially,** if a class is reliably resolved by a **separable, non-function** cue. That class —
  and only that class — would justify a distinct gated step, defined by its own `(evidence × question)`. The
  measurement names the share and the cue, so any such step is justified by evidence, not asserted.

Until part 3 is in, this is a provisional verdict, not a closed decision. (Investigate-by-default: the cheap design and
literature reasoning is done; the one measurement that could move it is teed up, not skipped.)
