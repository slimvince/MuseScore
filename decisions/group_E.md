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

**Home.** `ARCHITECTURE.md:1281`

**Provenance.** ARCHITECTURE.md:1200-1210 (Layer 2 - Built+Live)

### D-042 — Slice boundaries are every onset AND every release

> Boundaries = the sorted-unique union of every **onset AND every release** of the **eligible** notes; consecutive boundaries form the slices.

**In plain words.** A new stretch begins whenever any note starts and also whenever any note stops - because a note ending changes what is sounding just as much as a note beginning.

**Why.** Stated constraint, ARCHITECTURE.md:1210 with :1077-1080: taking every onset AND every release makes the boundary set an exhaustive candidate grid - necessary but not sufficient - so a real chord change can never be missed and over-grab is structurally impossible.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1281`

**Provenance.** ARCHITECTURE.md:1210. Cited by open_items/OI-228 as the primary source the joint emission departs from

### D-043 — Slice identity IS the eligible sounding-note set

> **Slice identity is the eligible sounding-NOTE set** (not the octave-folded PC set — a
> unison/octave shrink is a real boundary though the PC set is unchanged).

**In plain words.** What makes one stretch different from the next is the exact set of notes sounding through it - not merely which pitch names are present. Two voices collapsing onto the same note is a real change even though no pitch name was lost.

**Why.** Stated constraint, ARCHITECTURE.md:1217-1218: identity is the note set and not the octave-folded pitch-class set, because a unison or octave shrink is a real boundary even though the pitch-class set is unchanged.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1288-1289`

**Provenance.** ARCHITECTURE.md:1217-1218. The joint decoder's per-event note set is ONSET-only (jointdecoder.h:67) - open_items/OI-228

### D-044 — A note that opens no boundary still rides along in the slice's sounding set

> A muted / invisible / non-tonal-staff note opens
> **no** boundary, yet still rides along in each slice's `overlapping()` set (passed through, not
> dropped).

**In plain words.** A note that is not allowed to create a new stretch is still recorded as sounding during the stretches it spans.

**Why.** Stated constraint, ARCHITECTURE.md:1214-1216: a slice is 'constant TONAL sonority', so an ineligible note opens no boundary; dropping it as well would lose it (#12), and it is carried as passenger metadata instead.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1285-1287`

**Provenance.** ARCHITECTURE.md:1212-1218

### D-045 — The slicer re-decides nothing about eligibility

> **Boundaries over layer-1's eligibility annotation — never re-decided.**

**In plain words.** Whether a note counts was settled by the note reader. The slicer reads that decision and does not second-guess it.

**Why.** Stated constraint, ARCHITECTURE.md:1212-1214: eligibility is Layer 1's decision, and a second filter in Layer 2 would be a second place the same question is answered (#6/#7).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1283`

**Provenance.** ARCHITECTURE.md:1212-1214

### D-046 — Zero interpretation - the slicer applies no thresholds and no musical judgment

> **Zero interpretation.** No thresholds, min-gap, merge, or snapping; no notion of
> "ornamental/passing/structural".

**In plain words.** The cutting-up step makes no musical decisions at all. It does not decide that a note is ornamental, does not merge short stretches, and has no adjustable numbers.

**Why.** Stated constraint, ARCHITECTURE.md:1237-1239: a threshold or a merge would make the slicer a judgment; with none, its output is a fact and the judgment stays where it belongs, in the layers that decide.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1308-1310`

**Provenance.** ARCHITECTURE.md:1237-1245

### D-047 — No special-casing of any note kind

> **No special-casing of any note kind** — grace and tuplet
> outcomes fall out of the note-model spans as facts

**In plain words.** Grace notes and tuplets need no special code. Their timing is a fact the note reader already carries, and the right answer falls out of it.

**Why.** Stated constraint, ARCHITECTURE.md:1238-1242, verified at the source: a grace note carries onset = the parent chord's tick and duration = its nominal written value, and tuplet ticks are the model's real un-snapped ticks, so both fall out of the note-model spans as facts and the slicer needs no grace or tuplet code at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1309-1311`

**Provenance.** ARCHITECTURE.md:1237-1242

### D-048 — Boundaries are necessary but not sufficient; over-grab is structurally impossible

> Boundaries are **necessary but not sufficient** for
> a chord change (the exhaustive candidate grid): a real chord change can never be missed
> (over-grab is structurally impossible), and the slicer never asserts a change

**In plain words.** Every place a chord could change is offered as a candidate, so no real chord change can be missed. Whether a candidate is a real change is decided later, by a stage that judges harmony.

**Why.** Stated constraint, ARCHITECTURE.md:1242-1245: because the boundary grid is exhaustive, the slicer never asserts a change - Layer 3 decides which boundaries are real and a later layer groups equal analyses.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1313-1315`

**Provenance.** ARCHITECTURE.md:1242-1245

### D-049 — An interior stretch where everything rests is an explicit empty slice, not a gap

> An interior span where all eligible voices rest is an **explicit
> EMPTY slice** (empty eligible overlap set), not a gap

**In plain words.** Silence in the middle of the music is recorded as a stretch with nothing in it, rather than as a hole in the coverage.

**Why.** Stated constraint, ARCHITECTURE.md:1228-1230: an explicit empty slice falls out of the consecutive-boundary construction for free, and it keeps the covering guarantee (D-041) true through a silence, which a gap would break.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1299-1301`

**Provenance.** ARCHITECTURE.md:1220-1231

### D-050 — Slicing is clipped to the loaded span and never drags outside it

> slicing never drags outside the loaded span

**In plain words.** The slicer cuts only within the span it was handed: a note sounding across the edge of that span is cut at the edge, and the slicer never reaches outside it. Widening what is analysed is the orchestration's job, not the slicer's, and re-slicing a wider span must reproduce the narrower one exactly - which is what makes widening safe.

**Why.** Stated constraint, ARCHITECTURE.md:1220-1235 with `cowork_layer2_reslice_design.md` §2: the clip is what makes re-slice equivalence hold - re-slicing an enlarged span reproduces the narrower result, with interior change-points stable and only the edge slice abutting the artificial boundary extending - so extending the span is lawful rather than a re-analysis.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1296`

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

**Home.** `cowork_layer2_slicing_design.md:130-139`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

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

**Home.** `cowork_layer2_slicing_design.md:140-148`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Recorded as resolving prerequisite (i) of the function layer's input list, with the note that the whole prerequisite is this contract sentence and no new code. It places the primitive in the shared notation-derived-view tier beside the bass, spelling and phrase-boundary views. The phrase-boundary member of that same tier is **D-476**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

