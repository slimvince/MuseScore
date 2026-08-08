# Decisions group E — Layer 2 — the slicer

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-041 — The slicer output covers the domain with no gaps and no overlaps

> returns an ordered, **covering, lossless** list of half-open `[start,end)` spans that **tile the domain with no gaps and no overlaps**

**In plain words.** The music is cut into consecutive stretches that between them account for every moment exactly once.

**Why.** Stated constraint, ARCHITECTURE.md:1210: a covering, lossless tiling is what makes the slicer a fact rather than a judgment - every tick lands in exactly one slice, so nothing the score sounds can fall between slices.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1516`

**Provenance.** ARCHITECTURE.md:1200-1210 (Layer 2 - Built+Live)

### D-042 — Slice boundaries are every onset AND every release

> Boundaries = the sorted-unique union of every **onset AND every release** of the **eligible** notes; consecutive boundaries form the slices.

**In plain words.** A new stretch begins whenever any note starts and also whenever any note stops - because a note ending changes what is sounding just as much as a note beginning.

**Why.** Stated constraint, ARCHITECTURE.md:1210 with :1077-1080: taking every onset AND every release makes the boundary set an exhaustive candidate grid - necessary but not sufficient - so a real chord change can never be missed and over-grab is structurally impossible.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1516`

**Provenance.** ARCHITECTURE.md:1210. Cited by open_items/OI-228 as the primary source the joint emission departs from

### D-043 — Slice identity IS the eligible sounding-note set

> **Slice identity is the eligible sounding-NOTE set** (not the octave-folded PC set — a
> unison/octave shrink is a real boundary though the PC set is unchanged).

**In plain words.** What makes one stretch different from the next is the exact set of notes sounding through it - not merely which pitch names are present. Two voices collapsing onto the same note is a real change even though no pitch name was lost.

**Why.** Stated constraint, ARCHITECTURE.md:1217-1218: identity is the note set and not the octave-folded pitch-class set, because a unison or octave shrink is a real boundary even though the pitch-class set is unchanged.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1523-1524`

**Provenance.** ARCHITECTURE.md:1217-1218. The joint decoder's per-event note set is ONSET-only (jointdecoder.h:67) - open_items/OI-228

### D-044 — A note that opens no boundary still rides along in the slice's sounding set

> A muted / invisible / non-tonal-staff note opens
> **no** boundary, yet still rides along in each slice's `overlapping()` set (passed through, not
> dropped).

**In plain words.** A note that is not allowed to create a new stretch is still recorded as sounding during the stretches it spans.

**Why.** Stated constraint, ARCHITECTURE.md:1214-1216: a slice is 'constant TONAL sonority', so an ineligible note opens no boundary; dropping it as well would lose it (#12), and it is carried as passenger metadata instead.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1520-1522`

**Provenance.** ARCHITECTURE.md:1212-1218

### D-045 — The slicer re-decides nothing about eligibility

> **Boundaries over layer-1's eligibility annotation — never re-decided.**

**In plain words.** Whether a note counts was settled by the note reader. The slicer reads that decision and does not second-guess it.

**Why.** Stated constraint, ARCHITECTURE.md:1212-1214: eligibility is Layer 1's decision, and a second filter in Layer 2 would be a second place the same question is answered (#6/#7).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1518`

**Provenance.** ARCHITECTURE.md:1212-1214

### D-046 — Zero interpretation - the slicer applies no thresholds and no musical judgment

> **Zero interpretation.** No thresholds, min-gap, merge, or snapping; no notion of
> "ornamental/passing/structural".

**In plain words.** The cutting-up step makes no musical decisions at all. It does not decide that a note is ornamental, does not merge short stretches, and has no adjustable numbers.

**Why.** Stated constraint, ARCHITECTURE.md:1237-1239: a threshold or a merge would make the slicer a judgment; with none, its output is a fact and the judgment stays where it belongs, in the layers that decide.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1543-1545`

**Provenance.** ARCHITECTURE.md:1237-1245

### D-047 — No special-casing of any note kind

> **No special-casing of any note kind** — grace and tuplet
> outcomes fall out of the note-model spans as facts

**In plain words.** Grace notes and tuplets need no special code. Their timing is a fact the note reader already carries, and the right answer falls out of it.

**Why.** Stated constraint, ARCHITECTURE.md:1238-1242, verified at the source: a grace note carries onset = the parent chord's tick and duration = its nominal written value, and tuplet ticks are the model's real un-snapped ticks, so both fall out of the note-model spans as facts and the slicer needs no grace or tuplet code at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1544-1546`

**Provenance.** ARCHITECTURE.md:1237-1242

### D-048 — Boundaries are necessary but not sufficient; over-grab is structurally impossible

> Boundaries are **necessary but not sufficient** for
> a chord change (the exhaustive candidate grid): a real chord change can never be missed
> (over-grab is structurally impossible), and the slicer never asserts a change

**In plain words.** Every place a chord could change is offered as a candidate, so no real chord change can be missed. Whether a candidate is a real change is decided later, by a stage that judges harmony.

**Why.** Stated constraint, ARCHITECTURE.md:1242-1245: because the boundary grid is exhaustive, the slicer never asserts a change - Layer 3 decides which boundaries are real and a later layer groups equal analyses.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1548-1550`

**Provenance.** ARCHITECTURE.md:1242-1245

### D-049 — An interior stretch where everything rests is an explicit empty slice, not a gap

> An interior span where all eligible voices rest is an **explicit
> EMPTY slice** (empty eligible overlap set), not a gap

**In plain words.** Silence in the middle of the music is recorded as a stretch with nothing in it, rather than as a hole in the coverage.

**Why.** Stated constraint, ARCHITECTURE.md:1228-1230: an explicit empty slice falls out of the consecutive-boundary construction for free, and it keeps the covering guarantee (D-041) true through a silence, which a gap would break.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1534-1536`

**Provenance.** ARCHITECTURE.md:1220-1231

### D-050 — Slicing is clipped to the loaded span and never drags outside it

> slicing never drags outside the loaded span

**In plain words.** The slicer cuts only within the span it was handed: a note sounding across the edge of that span is cut at the edge, and the slicer never reaches outside it. Widening what is analysed is the orchestration's job, not the slicer's, and re-slicing a wider span must reproduce the narrower one exactly - which is what makes widening safe.

**Why.** Stated constraint, ARCHITECTURE.md:1220-1235 with `cowork_layer2_reslice_design.md` §2: the clip is what makes re-slice equivalence hold - re-slicing an enlarged span reproduces the narrower result, with interior change-points stable and only the edge slice abutting the artificial boundary extending - so extending the span is lawful rather than a re-analysis.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1531`

**Provenance.** ARCHITECTURE.md:1220-1227; cites cowork_layer2_reslice_design.md §2

### D-540 — A slice is a unit of constant CONTENT, not of constant musical TIME — the layers above must never treat slices as equal-weight units, and a slice's metric extent is evidence weighted by metric structure, not by tempo

>   one is a ten-measure held chord and the other a passing sixteenth — but they carry very different inferential weight,
>   so the layers above must **never treat slices as equal-weight units**. A slice's **metric extent** — its **duration**
>   (`end − start`, directly on the slice) and its **metric position/weight** (the metric-weight derived view over
>   Architectural Layer 1's score, from the time signature) — is **evidence**, and it is weighted by metric structure,
>   **not by tempo**: the harmonic reading (and the human ground truth) keys off beat strength and notated duration in
>   beats/measures, not absolute clock time. Architectural Layer 2 keeps the slice **minimal** (`[start, end)` only); the
>   duration and metric weight are **derived on demand** by the consuming layers (Architectural Layer 3 emission,
>   Architectural Layer 4 membership), not stored here. *(How well the inference weights the extremes — a very long held
>   chord, a very short embellishment slice — is an Architectural Layer 3 / 4 weighting concern; the metadata to do it
>   is available here.)*

**In plain words.** Two slices are each one slice whether one is a ten-measure held chord and the other a passing sixteenth, but they are not equally informative. How long a slice is and how strong its metrical position is are evidence. That evidence is weighted by the notated metre, not by clock time. The slice itself stores only its start and end; the rest is derived on demand by whoever needs it.

**Why.** The weighting basis is grounded in what the analysis and the human ground truth actually key off — beat strength and notated duration in beats and measures, not absolute clock time — which is why tempo is excluded. Keeping the slice minimal and deriving the extent is the same layer discipline that keeps the slicer free of judgement: the metadata is available here, and how well the extremes are weighted is the consuming layers' concern.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `cowork_layer2_slicing_design.md:130-139`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8** — `## 8. Crosscutting concepts` (heading at line 121). A delegation at ARCHITECTURE.md:1563 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** A crosscutting concept of the as-built Layer-2 specification, stated as a warning to the layers above. It is the qualification that makes the atomic-unit decision safe: **D-023** makes the constant-sonority slice the analysis unit, and this says what may not be concluded from that. The factor granularity that eventually consumes it is **D-449**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-541 — The metric weight of a slice IS the beat-strength at its start tick, taken from one shared preference-free notation primitive that no consuming layer re-defines

>   - **★ Metric-weight contract (resolved 2026-06-26; the function layer's prerequisite (i)).** "Derived on demand by the
>     consuming layers" is made concrete: the **metric weight of a slice = the beat-strength at the slice's start tick**,
>     computed by the **`scoreharvest/metricweights` primitive** (`regionMetricWeightForOnsetTick(score, slice.start)`) — a
>     **preference-free** (independent of any user setting), key-/chord-agnostic notation-derived value in `[0.5, 1.0]`
>     (downbeat 1.0 → subbeat 0.5), already consumed
>     by Architectural Layer 4. It is owned there (a **Layer-1.5** notation view, §0, beside the bass/spelling/phrase-
>     boundary views), **not** re-defined by any consuming layer. The function layer (Architectural Layer 5) reads it
>     through this same accessor; this contract sentence is the whole of that prerequisite — prerequisite (i) of the
>     function-layer spec's input list, `cowork_layer5_function_design.md` §15-0 — no new code.

**In plain words.** The vague instruction 'derived on demand by the consumer' was made concrete. A slice's metric weight is the beat strength at the moment it begins, computed by one shared routine over the notated metre. It depends on no user setting and knows nothing of keys or chords, and every layer that wants it reads it through that same routine.

**Why.** The properties are stated as the reason for the choice: preference-free and key- and chord-agnostic is what lets the same value serve layers that must not influence one another, and single ownership is what stops a consuming layer from re-deriving a second, subtly different definition of the same quantity — the one-path-per-concern rule applied to a derived view.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Home.** `cowork_layer2_slicing_design.md:140-148`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§8** — `## 8. Crosscutting concepts` (heading at line 121). A delegation at ARCHITECTURE.md:1563 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Recorded as resolving prerequisite (i) of the function layer's input list, with the note that the whole prerequisite is this contract sentence and no new code. It places the primitive in the shared notation-derived-view tier beside the bass, spelling and phrase-boundary views. The phrase-boundary member of that same tier is **D-476**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-605 — The local-key hypothesis derives from key-agnostic signals ONLY and never from the key-area grouping, which is a post-grouping of the resolved key — a hard design rule, not a preference

> - **A local-key hypothesis derives from KEY-AGNOSTIC signals only, and NEVER from the key-area
>   grouping — a hard design rule, not a preference.** Deciding that a passage has moved to another
>   key may use the cadence detector, which is key-agnostic by construction, and the raw region
>   structure — root motion, diatonic-collection consistency. It may **not** read the key-area
>   grouping, which is a downstream post-grouping of the already-resolved key. The flow stays
>   strictly feed-forward: chords → key-agnostic cadence → local-key hypothesis → re-keyed key path →
>   key areas, rebuilt downstream. *Why:* named in the decision as the load-bearing soundness
>   property, and the circularity is concrete rather than argued — the grouping is built FROM the
>   resolved key, so a detector reading it would find the key it was given. It is the same discipline
>   that made the cadence detector usable, applied to the local-key hypothesis and naming the exact
>   surface that would make it circular. **Scope:** the mechanism this rule was written for sits on
>   the legacy key path, but what it constrains is *what evidence a modulation decision may read*,
>   which binds any such decision on any arm.

**In plain words.** Deciding that a passage has moved to a new key may only use evidence that does not already assume a key: the closure detector, which works without being told the key, and the plain shape of the music. It may not read the key-area grouping, because that grouping is built FROM the key already decided — using it would mean the detector confirming its own input.

**Why.** Named in the decision as the load-bearing soundness property, and grounded in a precedent: the same discipline is what made the cadence detector usable. The circularity is concrete and cited — the key-area grouping is built downstream of the resolved stay-home key, so a detector reading it would find the key it was given.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `ARCHITECTURE.md:1709-1721`

**Provenance.** `docs/stage4d_local_modulation_design.md`, the Stage-4d local-modulation design, DRAFT and ratification-gated, 2026-06-14. Read in full by READ WAVE 5, 2026-08-04. The document's banner marks it DRAFT and ratification-gated, and its §7 lists this rule as item 2 for user ratification; the record does not state that the ratification happened, so no ratifier is recorded here. ⚠ The MECHANISM this rule governs is on the LEGACY key path — the joint estimator decides key and segmentation together and is the production inference layer (**D-001**, **D-005**) — but the RULE is about what evidence a modulation decision may read, which binds any such decision. It is the same principle **D-336**/**D-081** state for the cadence detector, applied to the local-key hypothesis and naming the specific surface that would make it circular. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The recorded owner question was that the rule's two ends sit in different sections — Layer 3 for the hypothesis, the key-area grouping for what it may not read. The user ruled that THE INPUT RULE BINDS THE HYPOTHESIS'S DERIVATION, so Layer 3 owns it and the grouping section points. Written into the Layer-3 section in that section's own voice, with its defense and with the scope statement the record carries: the mechanism it was written for is on the legacy key path, while what the rule constrains — what evidence a modulation decision may read — binds any such decision on any arm. Assumption A1 discharged before writing. FORMER HOME, PRESERVED (#12): `docs/stage4d_local_modulation_design.md:51-56`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 49, "section": "## §3 — No circularity / key-agnosticism (the architecture constraint)", "label": "“§3”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**The local-key hypothesis MUST derive from key-agnostic signals — the cadence instrument (key-agnostic by
construction) + raw region structure (root motion, diatonic-collection consistency) — NOT from the current
KeyArea**, which is a downstream post-grouping of the resolved (stay-home) key (`sectionanalyzer.cpp:930`)
and would make the detector circular. The flow stays strictly feed-forward: chords → key-agnostic cadence →
local-key hypothesis → re-keyed key path → KeyArea (rebuilt downstream). This is the same discipline that
made the cadence detector usable; it is the load-bearing soundness property and a hard design rule." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-631 — The boundary at the loaded edge is ARTIFICIAL and vanishes on extension — so the edge slice grows, and an old-slices-byte-identical assertion is false and must not be written as a test

> - **The boundary at the loaded edge is ARTIFICIAL and VANISHES on extension, so the edge slice
>   GROWS — and an "old slices stay byte-identical" assertion is FALSE and must never be written as a
>   test.** The clip injects a boundary at the loaded start that is not a change-point at all: a
>   sustained-in note sounds on both sides of it, and it exists only because the far side was not
>   loaded. Extend earlier and it disappears, so the edge slice extends outward rather than being
>   preserved with a new slice prepended. **What does hold is two things: (a)** every *real*
>   change-point inside the previously loaded region is byte-stable, because extending earlier can add
>   only notes whose release is at or before the old start, so no new real boundary can appear inside
>   it; **(b)** the edge slice abutting the clip extends into the newly loaded context, its content
>   over the original span unchanged. Symmetric on extend-later, at the trailing edge. *Why the
>   prohibition is written as one:* the claim was corrected against a counterexample the design states
>   in full — a single eligible note spanning the loaded start, one slice before the extension and one
>   after, with the edge slice demonstrably grown — so the naive assertion is not merely imprecise, it
>   is false, and it would pass by accident on the cases that do not exercise the edge. **This breaks
>   no correctness:** Layer 3 re-infers fresh over the new slices under the forward-only contract, and
>   the edge extension is exactly the additional leading-edge context the bounded-context contract's
>   convergence rule exists to absorb.

**In plain words.** When the music is cut into stretches, the cut at the edge of what has been loaded is not a real change in the sounding notes — it is there only because nothing beyond it was loaded. Load more and that cut disappears, so the stretch at the edge gets longer rather than staying as it was. What does stay identical is every real cut inside the region already loaded.

**Why.** Corrected against a counterexample the design states in full — one note spanning the boundary, one slice before and one after, with the edge slice demonstrably grown rather than preserved — which is why the earlier claim is recorded as wrong rather than refined. What replaces it is derived: extending earlier can only add notes that end before the old start, so no new real boundary can appear inside the old region. The consequence for testing is stated as a prohibition because the naive assertion would pass by accident and fail on the first case that matters.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1569-1585`

**Provenance.** `cowork_layer2_reslice_design.md` §3, the Layer-2 slicing-under-bounded-context detail design, BUILT. Read in full by READ WAVE 6, 2026-08-04. The correction is marked in the document as made after a read-only verification. **D-050** already carries the clip rule and the re-slice-equivalence invariant that makes widening lawful, and cites this document's §2 for it; this is the separate finding about what does and does not stay stable across an extension, which no other home carries and which the §6 test list turns into a written prohibition. The record states neither a date nor a ratifier. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). Routed to the Layer-2 section of `ARCHITECTURE.md`, in that section's own voice and with the counterexample that produced the correction. THE COUNTEREXAMPLE'S TICK VALUES ARE NOT CARRIED ACROSS (D-431): its SHAPE is what makes the prohibition binding — one eligible note spanning the loaded start — and the arithmetic stays in the design document. FORMER HOME, PRESERVED (#12): `cowork_layer2_reslice_design.md:55-65`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 53, "section": "## 3. What holds under extend (corrected after CC's read-only verification)", "label": "§3", "delegated": null, "delegation": "ARCHITECTURE.md:1339", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "- **Stability — seam-aware (the earlier \"old slices byte-identical\" claim was wrong).** The clip injects an
  **artificial boundary at `loadedStart`** — *not* a real change-point (a sustained-in note sounds on both sides; the
  boundary is there only because the far side was unloaded). Extend earlier and that artificial boundary **vanishes**,
  so the **edge slice grows outward**. (Counterexample: one eligible note A `[100,1000)`; old span `[500,1000)` → one
  slice `[500,1000)`; extend to `[100,1000)` → one slice `[100,1000)` — the edge slice *grew*, it was not \"preserved +
  a new slice prepended.\") What actually holds: **(a)** interior **real** change-points within the old region are
  **byte-stable** (extend-earlier only adds notes with `release ≤ oldStart`, so no new real boundary appears
  `> oldStart`); **(b)** the **edge slice abutting the clip extends** into the newly-loaded context, its content over
  the original span unchanged. Symmetric on extend-later (trailing edge). **This breaks no correctness:** L3 re-infers
  fresh over the new slices (forward-only contract), and the edge extension is precisely the \"more context at the
  leading edge\" that **convergence** (`cowork_bounded_context_design.md` §3.6) is built to absorb." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-632 — The slice stays minimal — no in-selection-or-context tag; the consumer derives it, because the slicer owns no selection semantics

> - **The slice stays MINIMAL — it carries start and end and nothing else; whether a slice is inside
>   the user's selection or is only surrounding context is derived by the consumer.** This layer
>   produces slices for the whole loaded span while the OUTPUT is only the selection, so the slices
>   outside it are context and evidence rather than output. The distinction is a thin annotation and
>   it is deliberately not stored here. *Why:* this layer owns no selection semantics — cutting the
>   music where the sounding set changes involves no judgment about what the user selected — so a
>   selection tag would keep another component's concern in this one's output. The alternative,
>   tagging each slice at the slicer from the model's selection span, was weighed and named rather
>   than passed over, and the minimal form was taken at the build.

**In plain words.** A slice records only where it starts and where it ends. Whether it falls inside the part of the score the user asked about, or is only surrounding context, is worked out by whoever consumes it — the slicer makes no judgment about selections, so it carries no mark about them.

**Why.** It follows from what the slicer is responsible for, and the decision says so: cutting the music at points of change involves no judgment about what the user selected, so a tag about the selection would be a second component's concern stored in this one's output. The alternative was considered and named rather than passed over, and the choice was taken at the build with the built form quoted.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1586-1594`

**Provenance.** `cowork_layer2_reslice_design.md` §5, BUILT; the document's own status block confirms the decision was taken at build. Read in full by READ WAVE 6, 2026-08-04. It is the data-shape consequence of the bounded-context rule that output is the selection while extended context is evidence, and of **D-033**'s one-contribution-per-layer invariant. The record states neither a date nor a ratifier. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)) into the Layer-2 section of `ARCHITECTURE.md`, in that section's own voice, with the alternative that was weighed named rather than dropped and with the defense stated as the layer's own ownership boundary. THE C++ STRUCT LITERAL IS NOT CARRIED ACROSS: the decision is what a slice carries, and D-307 forbids pinning a specification to code text. FORMER HOME, PRESERVED (#12): `cowork_layer2_reslice_design.md:83-90`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 82, "section": "## 5. Output vs context (the selection boundary)", "label": "§5", "delegated": null, "delegation": "ARCHITECTURE.md:1339", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a bare-appended-citation, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "L2 produces slices for the **loaded** span; the **output** is only the **selection**. The slices in
`[loadedStart, selectionStart)` ∪ `[selectionEnd, loadedEnd)` are **context (evidence), not output**. L2 itself makes
no analysis judgement — it just slices — so the selection-vs-context distinction is a **thin annotation**: either tag
each slice in-selection/context from the model's selection span, or leave it to the consumer to compute from
`selectionStart/End`. Recommended: compute it at the consuming layer (keep the `Slice` minimal — `[start,end)` only,
per the L2 spec), since L2 owns no selection semantics. **Decision taken at build: the `Slice` is minimal
(`struct Slice { int start; int end; }`) — no in-selection/context tag; the consumer derives it from the model's
selection span.**" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

