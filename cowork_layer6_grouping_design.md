# Layer 6 — Grouping (design)

> **Status: SIGNED (user, 2026-07-02) — but the BUILD is PROHIBITED/DEFERRED (user directive, same day): L6 work
> (including its TSV-oracle validation infrastructure) resumes only after the L1–L5 extension behavior
> (`cowork_bounded_context_design.md`, SIGNED 2026-07-02 — its §11 acceptance list) is CODED and REGRESSION-TESTED.** Sign-off history: reviewed +
> language-passed (Cowork, 2026-06-30); phrase-terminology correction + polyphony grounding folded
> (2026-07-01); grouping unit renamed phrase → punctuation-span (2026-07-01); external-review amendments +
> edge-provenance/extension-cue amendments folded at sign-off (2026-07-02). The
> **2026-07-01 pass** (user-directed): the grouping unit L6 segments is renamed **phrase → punctuation-span** — the flat,
> surface-punctuation-delimited DCML `{}` grouping span — so the word "phrase" is **reserved for the accepted melodic
> phrase [MT]** (monophonic/linear, text-coinciding when sung), which L6 does *not* segment and which is deferred to the
> future voice-leading/melody-line layer. §2/§14 fold the polyphony deep search
> (`cowork_polyphony_phrase_harmony_research.md`) — onset/verticality harmony, one flat texture-wide grouping, voice
> separation as a separate task, and the non-chord-tone filter as a future **L4** lever. The v1 draft (2026-06-29) went
> through the Cowork review + language-mechanical pass — findings folded: the **schema sequence-span** output
> (§2 / §3 / §5.5, the L6↔encyclopedia annotation home), the **§2.15 span-typology term scrub** (`region` unqualified →
> slice / key-span), and the §15-6 / §15-1 status updates. Research foundation: `cowork_layer6_grouping_research.md`.
> Specified by **rule and direction**; numeric calibration is the later precision phase (the firewall). Build **dormant +
> byte-identical**, validate against the oracles in §10, engagement deferred indefinitely (production out of scope).

## 0. Terminology (read first) — accepted music theory vs. this layer's operational terms
This layer builds on established music-theory concepts. To keep them trustworthy, every term is marked **[MT]** (an
**accepted music-theory** term, used in its accepted sense, with a reference) or **[L6]** (an **operational** term
defined *by this design* — not standard vocabulary). Where our operational use of an [MT] term differs from the textbook
concept, the difference is stated. An [MT] term may also be defined here **precisely to mark it out of scope** — the
accepted **phrase [MT]** is the leading example: it is the melodic unit L6 does *not* segment, defined so it is not
confused with L6's operational **punctuation-span [L6]** grouping unit. Nothing below is used before it is defined here.

### Accepted music-theory terms [MT]
- **Phrase [MT] — the accepted term, and NOT what this layer segments.** In music theory a phrase is a broadly
  *melodic / linear* unit: essentially **monophonic in conception** (in homophonic or polyphonic textures it is still
  carried by a leading line), conventionally closed by a **cadence** (Caplin makes the cadence definitional) or by a
  breath/gesture, and — when sung — usually **coinciding with a text phrase**. **This is a construct of the melodic /
  voice-leading dimension, not of harmonic grouping, so L6 does not segment it.** Identifying the accepted phrase — and the
  **concurrent, overlapping, out-of-phase per-voice phrases** of a contrapuntal texture (e.g. a fugue's staggered subject
  entries) — belongs to the **future voice-leading / melody-line layer** (the confirmed second axis,
  `cowork_idiom_discovery_findings.md`); the method foundation to lean on is recorded in
  `cowork_polyphony_phrase_harmony_research.md`. What L6 actually groups is a *different* object — the **punctuation-span**,
  defined under [L6] below. *(Ref: Caplin 1998 for the cadence-defined phrase; the melodic-grouping and voice-separation
  literature for the linear one.)*
- **Cadence [MT].** A conventional harmonic-melodic closing formula marking a point of repose, in the standard typology:
  **perfect/imperfect authentic** (PAC/IAC), **half**, **plagal**, **deceptive**, **Phrygian half**. Detected upstream by
  Layer 5 (its §5.2 event-pair detector); **L6 reads L5's cadences — it does not define or re-detect them.**
- **Key-area [MT].** A maximal passage governed by a single (local) key — the standard analytic term (e.g. the sonata-form
  "second key area"). Operationally here: a maximal run of adjacent **slices** sharing one local key.
- **Modulation / local key [MT].** Standard senses; the local key at each point is what Layers 3/5 commit.

### This design's operational terms [L6] (mine — not standard vocabulary)
- **Punctuation-span [L6] — the harmonic-grouping span L6 segments (the DCML `{}` unit).** What this layer segments is
  **not** the accepted melodic phrase [MT] above; it is the flat, **non-hierarchical** grouping span of the DCML /
  When-in-Rome annotation standard — the `{ }` unit whose boundaries are the score's *notated punctuation* (fermatas,
  rests, double barlines, key-signature changes, …), **which is what it is named for**. Its boundaries are delimited by
  those **surface cues** via the phrase-boundary primitive (§5.1), **not** by requiring a cadence (defining a span by its
  cadence and then aligning cadences to it in §5.3 would be circular). The DCML standard happens to label this `{}` unit
  "phrase," but it is a **harmonic / annotation grouping construct** — spelling-blind to melody and voice — and it
  **diverges** from the accepted melodic phrase [MT]; this design therefore calls it the **punctuation-span** and never
  "phrase." **★ Naming convention: the word "phrase" appears in this document only as "phrase [MT]" (the accepted melodic
  unit, out of scope); the harmonic-grouping object L6 produces is always the "punctuation-span."** In chorales the two
  coincide (a fermata marks both a punctuation-span edge and a cadence); in general they need not. The cadence↔span
  relation is *checked* in §5.3, never assumed in the definition. *(Ref: the DCML annotation standard.)*
- **Slice [L6].** The atomic analysis unit — one chord-rhythm segment from Layer 2 (the *harmonic region [chord-rhythm]* of
  the §2.15 span typology). The finest unit L6 groups.
- **Boundary [L6].** A tick where the **phrase-boundary primitive** places a picked peak — a surface-cue location (fermata /
  breath / rest / structural barline / key-signature change / subito tempo). Our operational proxy for a punctuation-span
  edge; **choosing which ticks are boundaries is the primitive's job upstream, not L6's.**
- **Key-span [L6].** The §2.15 span-typology name for a key-area (used interchangeably below).
- **Sequence-span [L6].** A recognised-schema span emitted by the recognition consumer and *hosted* by L6 (§5.5).
- **Open mark [L6].** Layer 5's carried honest residual — a slice whose reading L5 left unresolved; L6 surfaces it, never
  resolves it.

### Other terms used below, defined
- **Flat partition.** A division of a span into consecutive, non-overlapping segments that tile the whole with **no
  nesting** — no segment contains another and there are no sub-segments (cutting a line into adjacent pieces). The opposite
  of *hierarchical*.
- **Hierarchical grouping.** Nesting groups inside groups — motifs inside phrases inside themes/periods inside sections
  inside movements: a **tree** over the piece, not one flat row of segments. (Here "phrases" is the accepted melodic sense
  [MT] — this illustrates the nesting L6 does **not** build.)
- **GTTM.** *A Generative Theory of Tonal Music* (Lerdahl & Jackendoff, 1983) — a formal theory that parses a piece into
  **nested tree structures** (grouping, metre, time-span reduction, prolongational reduction). L6 builds **no** such trees.
- **Caplinian formal functions [MT — out of L6's scope].** William Caplin's theory of classical form (*Classical Form*,
  1998), which defines formal units by their temporal **function** (beginning / middle / end). Its two core themes: the
  **sentence** (a *presentation* — a basic idea plus its repetition — then a *continuation*, then a *cadence*) and the
  **period** (an *antecedent* phrase [MT] closing on a weaker cadence, e.g. a half cadence, answered by a *consequent*
  phrase [MT] closing on a stronger one, e.g. a PAC). These are **hierarchical** constructs *above* the melodic phrase — a
  larger structure than L6's flat grouping; §2 and §9-D3 state why they sit outside L6's core and on what terms they could
  be built.

## 1. The core principle
**Grouping is assembly, not detection.** Every signal Layer 6 needs has already been computed by an earlier layer — the
punctuation-span boundaries (the Layer-1.5 phrase-boundary primitive), the cadences and the Roman numerals (Layer 5), the
local keys (Layer 3). Layer 6 **assembles** these into the flat grouping structure the ground truth annotates:
**punctuation-spans**, **key-areas**, and the **alignment of cadences to punctuation-span endings**. It detects nothing new
and re-derives nothing; it reads the upstream outputs and segments/labels the stream into groups. It is the
cosmetic-but-structural top of the pipeline: it does not change any Roman numeral, key, or cadence — it **organises** them
(structural but non-analytical).

## 2. The layer model — what L6 does and does not do
**Does:**
- **Punctuation-span segmentation** — partition the analysed span into contiguous **punctuation-spans** delimited by the
  phrase-boundary primitive (§5.1).
- **Key-area grouping** — group maximal runs of same-local-key **slices** into **key-areas** (key-spans) (§5.2).
- **Cadence-to-punctuation-span alignment** — associate each Layer-5 cadence with the punctuation-span it closes, honouring
  the asymmetric cadence↔span relation (a cadence implies a span ending; a punctuation-span may end without a cadence)
  (§5.3).
- **Carry the honest residual** — Layer-5 open marks pass through to the grouped output unchanged; L6 groups *around*
  uncertainty, it does not resolve it (§5.4).
- **Host the recognised-schema annotations** — when the recognition consumer (the Harmonic Vocabulary's L5/L6
  consumer, `cowork_progression_schema_design.md`) is present, its recognised-schema **sequence-spans** are carried as
  read-only, additive, **cross-cutting** labels (§5.5). L6 is their annotation home; it does **not** recognise schemas
  itself (the consumer does).

**Does not do:**
- **Hierarchical grouping** (nested trees / GTTM reductions — §0). Out for a *precise* reason: **the validatable grouping
  annotation (the DCML `{}`) is itself flat** — the standard is explicitly non-hierarchical, so the oracle *exists and says
  non-nested* — and full hierarchical parsing is computationally below human accuracy. This is **not** a "no-oracle"
  deferral; the oracle is flat (§9-D1).
- **Caplinian formal functions** (sentence, period, … — §0) and multi-span **sections**. Sound theory that *does* lack an
  oracle in our corpus — but **per the verifiability contract, lack of ground truth does NOT disqualify them.** They are
  kept out of **L6's thin core for proportionality** (L6 assembles the *flat* grouping; forms/sections are a larger
  structure that properly belongs to a *higher* layer), and are **buildable via an alternative-confidence path** (a
  form-annotated corpus, or theory-rules-as-oracle) with an "empirically-unvalidated" mark **whenever a need arises**
  (§9-D3). Out of the *core*, **not** disqualified.
- **Melody / structural-line identification, voice-leading, and the accepted (melodic) phrase [MT]** — separate
  dimensions, not L6's. Melody/structural-line is out across the architecture; **voice-leading is the confirmed second
  axis, its own future layer** (`cowork_idiom_discovery_findings.md`); and the **accepted music-theory phrase [MT] (§0)** —
  the melodic, often text-coinciding unit — is a construct of that axis, **not** the punctuation-span L6 segments. In
  particular the **concurrent, overlapping, out-of-phase per-voice phrases** of a contrapuntal texture (a fugue's staggered
  subject entries) are **not** L6's input: the deep search found **no published system that models overlapping per-voice
  phrases for harmonic analysis** — harmony is universally analysed at the **onset / verticality level** (ChordGNN
  onset-wise; music21 `chordify`), so keeping L6's grouping flat omits no standard technique
  (`cowork_polyphony_phrase_harmony_research.md`). (The perfect/imperfect cadence call is Layer-5's, on bass-derived
  inversion, not the top voice.)
- **Any change to the Roman numeral, key, or cadence** decided upstream — L6 is additive and read-only over Layer 5.

## 3. Inputs and outputs (the contract)
**Consumes** (all already produced, no new computation):
- **The Layer-5 output** (`FunctionLayerOutput`, §7 of the L5 design) — per analysis unit: the Roman numeral, the
  function confidence, the open mark, the committed identity; per key-span: the local key (possibly modulated); and the
  Layer-5 cadence markers (type, location, salience).
- **The phrase-boundary primitive** (`phraseBoundaryView` — `phraseBoundaryTicks()` and the graded
  `PhraseBoundaryProfile`): the boundary ticks and their strengths (fermata / breath / rest / barline / key-signature /
  tempo cues, max-normalised, peak-picked).
- **The Layer-3 local-key spans** (the per-region `keyModeResult`, surfaced through the Layer-5 per-region local key).

**Produces** — the flat grouping structure, **additive over Layer 5** (it annotates and segments; it does not replace any
upstream decision):
- **Punctuation-spans** — an ordered, contiguous partition of the analysed span; each punctuation-span a
  `[startTick, endTick)` span with the units it contains, the boundary strength **and the provenance** (which cue fired
  and its **scope** — global/system-wide vs per-part — carried through from the Layer-1.5 primitive,
  `cowork_phrase_boundary_design.md` §11-5) that opened/closed it, and the cadence (if any) that closes it. Carrying the
  scope is what keeps the annotation from silently presenting a **local** boundary (e.g. one part's breath) as a **global**
  one (e.g. a double barline) — L6 annotates the distinction, it does not flatten it.
- **Key-areas** — an ordered, contiguous partition into local-key spans; each `[startTick, endTick)` with its local
  tonic/mode and confidence.
- **Cadence-to-punctuation-span alignments** — each Layer-5 cadence tagged with the punctuation-span it closes (or flagged
  *internal* if it falls mid-span — §5.3), carrying its Layer-5 type and salience.
- **The carried open marks** — Layer-5's honest residuals, surfaced in the grouped view, never resolved here.
- **Recognised-schema sequence-spans** (present only when the recognition consumer is) — each a `[startTick, endTick)`
  span carrying the matched schema's name, its style/idiom tag, the match score, and the underlying-function read-out
  for any substituted member (e.g. "`♭II7` here = `subV7/I`"). **Cross-cutting** — a schema may straddle a punctuation-span
  boundary and a punctuation-span may hold several schemas. Read-only and additive; L6 is the annotation home, the consumer
  is the producer (`cowork_progression_schema_design.md` §2/§4.4).

Punctuation-spans are a flat partition; **key-spans and recognised-schema spans are independent, cross-cutting
segmentations of the same stream** (the target-architecture §2.15 span typology): a key-span may cover several
punctuation-spans and — rarely — a punctuation-span may straddle a key change; a schema span may straddle a
punctuation-span boundary. They are **not** nested. The contract to the display layer above is this structure; L6 is its
only producer.

## 4. As-built starting point (the scattered machinery this layer rebuilds)
Grouping already exists in production, **scattered and key-dependent**: `detectCadences()` (PAC/PC/DC/HC text markers) and
`detectPivotChords()` in `section/sectioncadencedetection`, both using the old key-dependent `ChordFunction::degree`
logic; and the `KeyArea` grouping in `analyzeSection` / `analyzed_section.h`. Layer 6 is the **forward-only rebuild** that
unifies these into one clean layer consuming the Layer-5 output + the phrase-boundary primitive + the Layer-3 spans —
exactly as Layer 5 unified the scattered function machinery. The old paths stay live until the joint engagement
(deferred); L6 is built dormant and byte-identical beside them.

## 5. Building-block view (the internal rules)

### 5.0 Definitions — see §0
All terms (**cadence**, **key-area/key-span** [MT]; **punctuation-span**, **boundary**, **slice**, **open mark**,
**sequence-span** [L6]; and the out-of-scope **phrase [MT]**) are defined once in **§0**; the rules below use them and add
no new vocabulary. The one construction detail §0 leaves to here: a **punctuation-span** is the maximal
`[startTick, endTick)` **flat** span between two adjacent boundaries (the first boundary at/after the span start opens it,
the next closes it), tiling the analysed span with no gaps or overlap (§5.1). The cadence L6 reads is Layer-5's
`FunctionalCadence` (type ∈ {PAC, IAC, Half, PhrygianHalf, Deceptive, Plagal, Evaded}, an approach→arrival tick pair, a
salience weight) — **read, not re-detected.**

### 5.1 Punctuation-span segmentation
Partition the analysed span at the boundary ticks supplied by the primitive: each punctuation-span runs from one boundary
(inclusive) to the next (exclusive). The partition is **total** (covers the whole span) and **flat** (no nesting). The
first punctuation-span opens at the span start even if no boundary marker sits there; the last punctuation-span closes at
the span end. **(Post-sign-off amendment, user-ratified 2026-07-02 — edge-truncation provenance + the extension cue.)**
An edge group whose opening/closing tick is the **selection edge rather than a musical boundary** carries the provenance
`clipped-by-selection-edge` (the same principle as the §3 marker-scope provenance and L2's artificial-clip-boundary
distinction) — a truncated group is never presented as a complete one; the same mark applies to an edge **key-area**
(§5.2). And an edge span that reaches the selection edge with **no closing boundary and no cadence** is surfaced with an
`extension-cue` tag — the signal that widening the selection would complete it. Per the forward-only contract L6 only
**surfaces** the cue (like the §5.3 internal-cadence tension tag); acting on it — invoking L1's `extend` and re-running —
is the **orchestrator's** decision under the §2.15 bounded-context contract (stop condition + hard bound), never L6's. **L6 consumes the primitive's picked-peak set as-is — it does not re-threshold or re-detect boundaries**
(peak selection is the primitive's owned job, §5.1 of the phrase-boundary primitive design); choosing *which* ticks are
boundaries is upstream, and how they *group into punctuation-spans* is the rule here.
- **Span interlocking** (`}{`): where a boundary is simultaneously one punctuation-span's structural end and the next
  span's start, the single boundary tick serves both — there is no gap.
- **Codetta / annexe** (the DCML refinement that the *structural* end can precede the literal next span start): the
  primitive supplies a single boundary tick, so the base partition places the span end there. Distinguishing a
  structural end from a trailing codetta is a **graded-strength refinement** (the structural end is the stronger peak) —
  specified as a refinement (§5.1-a), not required for the flat partition.
  - **(§5.1-a, refinement)** Where two boundaries fall close together (a strong structural peak followed by a weak one),
    the **stronger** peak is the punctuation-span's structural end and the span between them is its codetta; the weaker
    peak does not open a new punctuation-span. The closeness window and the strength margin are precision-phase constants.

### 5.2 Key-area grouping
A **key-area** is a maximal span of constant local key. Read the upstream **local-key track** (the local tonic and mode
carried per analysis unit by Layers 3/5) in order; open a key-area at the first unit; extend it while the local key is
unchanged; **close it and open a new one at each local-key change**. The granularity at which a key change can fall is the
granularity at which the local key is carried upstream — the chord-rhythm analysis unit, which is **finer than a
punctuation-span** — so a key change may fall **within** a punctuation-span; key-areas are therefore an **independent** flat
segmentation, **not** nested in punctuation-spans (§3, §9-D5). Each key-area carries its local tonic and mode and a
**confidence that is non-increasing in its weakest unit's key confidence** (the exact combiner — for example the
duration-weighted mean — is precision-phase; this direction is fixed here). The rule that a key change starts a new area is
fixed here. *(Contract compliance, added at sign-off review 2026-07-02: any confidence L6 publishes — the key-area
confidence, a span-level aggregate — is a **boundary confidence under the cross-layer confidence contract**
(`cowork_confidence_contract.md` U2): [0,1], Class-M-declared, with its combiner and inputs named; and its **input** is
each unit's DECLARED boundary key confidence per that contract — i.e. once the D-L3a close-out lands, the one declared
L3/L5 number, not the diagnostic sigmoid.)*
- **A confirmed Layer-5 modulation** (§5.4 of the L5 design) is already reflected in the local-key track it commits, so a
  key-area boundary falls exactly where the modulation recompute committed the new key — L6 reads that; it does not
  re-decide the modulation.
- **★ Proper-layer flag (review finding, 2026-06-29).** L5 §5.0 defines *region* as "a maximal run of slices between two
  adjacent phrase boundaries, carrying one prevailing key" (L5's own wording) — span-bounded and single-key, which would
  forbid a mid-span key change and force key-areas to nest in punctuation-spans. The **as-built** carries the local key at
  **chord-rhythm** (sub-span) granularity, which **does** permit a mid-span key change, as the ground truth annotates. This
  terminological tension is **L5/L2's to reconcile** (the proper layer): clarify the §5.0 "region" wording to the
  chord-rhythm sense, or state the local-key carry granularity explicitly. L6 consumes the local-key track at whatever
  granularity the reconciled definition fixes; this design assumes the sub-span (as-built) granularity (**reconciled —
  §15-6 RESOLVED**: the §2.15 span typology + the L5 §5.0 disambiguation fixed the term; key-areas group the **key-span**,
  which cross-cuts punctuation-spans).

### 5.3 Cadence-to-punctuation-span alignment
Associate each Layer-5 cadence with a punctuation-span, honouring the **asymmetric** relation (ground truth: a cadence
almost always coincides with a span ending; many punctuation-spans end with no cadence):
- A cadence **closes** the punctuation-span whose **ending boundary lies at the cadence's arrival tick, or within the
  alignment window after it** (a cadence's arrival may slightly precede the notated span end — for example a suspended
  resolution; the window's width is a precision-phase constant, its existence fixed here). That cadence is the
  punctuation-span's **closing cadence**.
- A punctuation-span with **no** cadence arriving within the window before its ending boundary ends **without a cadence** —
  a valid, common case; it is not forced to carry one.
- A cadence whose arrival lies **within the alignment window of no punctuation-span boundary** is tagged **internal**
  (mid-span) and surfaced as such — **not** snapped to a distant boundary and **not** discarded. An internal cadence is a
  *diagnostic signal* (it means either a missed boundary or an over-eager cadence); L6 records it rather than resolving it —
  resolving it would require re-deciding the boundary or the cadence, both upstream and not L6's to override (§8).
- The **perfect/imperfect** and other type distinctions are Layer-5's (carried verbatim); L6 only positions the cadence in
  the punctuation-span structure.

### 5.4 Carrying the residual
A Layer-5 open mark on a unit is surfaced on the punctuation-span and key-area that contain that unit (the group is
reported as carrying an unresolved reading at that location). L6 **never** resolves an open mark — it has no evidence Layer
5 lacked. A punctuation-span composed entirely of confidently-read units is reported as fully resolved; one containing an
open mark is reported with the residual visible.

### 5.5 Hosting the recognised-schema annotations
When the recognition consumer (`cowork_progression_schema_design.md`) is present, each recognised-schema
**sequence-span** it emits is carried verbatim: L6 places the span in the grouped output and exposes it as a
cross-cutting label alongside the punctuation-spans and key-spans it overlaps. L6 **does not recognise schemas, score
matches, or apply substitutions** — the consumer does; L6 only hosts the result, the same reuse-not-duplicate discipline
as the punctuation-span / cadence / key carries. Absent the consumer (the current dormant state), this output is simply
empty and the four core rules (§5.1–§5.4) stand alone — so hosting the annotation adds no detection to L6.

## 6. The layer is exactly its assembly rules + read-through carries (the proportionality bound)
Layer 6 defines **no detection of its own**: it assembles §5.1–§5.3 (punctuation-span segmentation, key-area grouping,
cadence alignment) and hosts the **read-through carries** — §5.4 the Layer-5 residual and §5.5 the consumer's schema
annotations, both carried verbatim, neither *detected* here. There is no additional *detection* rule and no hierarchy.
Pressure to add detection is a signal to check whether the work belongs in an **earlier** layer (a detection that should be
a primitive) or is an **out-of-scope extension** (§9-D3) — not a new Layer-6 mechanism. The proportionality discipline (§7)
holds the layer to the assembly + the carries.

## 7. Crosscutting concepts
- **Additive and read-only over Layer 5.** L6 changes no upstream decision; it segments and labels. This is the
  no-feedback half of the forward-only contract (§8 of the target architecture): grouping is **downstream** of Layer-5's
  resolution and override, and does not feed back into them.
- **Reuse, do not duplicate.** Punctuation-span boundaries come from the one phrase-boundary primitive; cadences and Roman
  numerals from the one Layer-5 output; local keys from the one Layer-3 carry. L6 adds **no** second boundary detector,
  cadence detector, or key segmenter. It **retires** the scattered `detectCadences`/`detectPivotChords`/`KeyArea` paths
  into itself at engagement.
- **The firewall.** The alignment window, the codetta closeness/margin, and the key-area confidence combiner are
  precision-phase constants; this document fixes the rules and their direction, not the numbers.
- **Proportionality.** The SOTA reaches competitive Roman-numeral accuracy with **no** explicit grouping layer (grouping
  falls out of stable key runs — `contrapunctus_findings.md`). L6 is a deliberate **explainability** layer, not an
  accuracy requirement; it stays the thin assembly layer specified here and does not grow detection of its own.

## 8. The Layer-5-override ↔ Layer-6-merge division (the standing joint item, L5 §15-6)
Layer 5 owns the **fine-grain reading** of each slice and the **class-(b) override** of a confidently-wrong commit
(§5.5/§10 of the L5 design): it *corrects* labels. Layer 6 owns the **grouping of the already-corrected stream**: once
Layer 5 has resolved/over­ridden a slice, L6 **merges** the now-consistent slices into punctuation-spans and key-areas. The
boundary is clean and forward-only:
- Correction (changing a slice's reading) is **Layer 5's**, by selection among carried readings, fired by the §8 override
  mechanism. L6 sees only the corrected result.
- Grouping (segmenting the corrected stream) is **Layer 6's**, and it **never feeds back** to request a different
  correction. An internal cadence or a same-key merge that *looks* like it wants a different upstream reading is **surfaced
  (§5.3 internal tag)**, not acted on — the forward-only contract forbids the back-edge.
So there is no overlap and no cycle: Layer 5 decides *what each slice is*; Layer 6 decides *how the slices group*.

## 9. Architecture decisions (with the alternatives weighed)
- **D1 — Flat grouping, not hierarchical.** The ground-truth grouping annotation (the DCML `{}`) is explicitly
  non-hierarchical (a flat partition, §0); the SOTA systems do grouping as flat boundary classification, not tree parsing.
  *Rejected:* a grouping tree (GTTM-style, §0) — **the punctuation-span oracle is itself flat**, so this is *not* a
  lack-of-oracle case; and full hierarchical parsing is computationally below human accuracy.
- **D2 — Assembly, not detection.** L6 reuses the upstream primitives and detects nothing. *Rejected:* an independent L6
  punctuation-span/cadence/key detector — it would duplicate Layers 1.5/5/3 and reintroduce the divergence the rebuild
  exists to remove.
- **D3 — Sections / periods / sentences are out of L6's *core* for PROPORTIONALITY — NOT disqualified for lack of an
  oracle (user-ratified verifiability contract, 2026-06-29).** They are sound theory and *do* lack an oracle in our
  corpus, but the contract is explicit that **lack of ground truth is not a disqualifier.** They stay out of the thin core
  because L6 is the *flat-grouping assembly* layer and forms/sections are a larger, *higher*-layer structure — and they are
  **buildable via a chosen alternative-confidence path** (a form-annotated corpus, or theory-rules-as-oracle) with an
  "empirically-unvalidated" mark, when a need arises. The core is punctuation-spans + key-areas + cadence alignment + the
  hosted schema spans.
- **D4 — Cadences align to punctuation-spans, asymmetrically; an off-boundary cadence is surfaced, not snapped (§5.3).**
  *Rejected:* forcing every punctuation-span to end with a cadence (contradicts the ground truth) and snapping a stray
  cadence to the nearest boundary (hides a real tension signal and would be a covert upstream override).
- **D5 — Punctuation-spans and key-areas are independent flat segmentations, not nested.** *Rejected:* nesting key-areas
  inside punctuation-spans or vice-versa — the two do not align in general (a key change can fall mid-span), and nesting
  would assert a hierarchy the ground truth does not annotate.

## 10. Quality & testing — the validation strategy (the two-step oracle, user-ratified 2026-06-29)
L6's three outputs have three oracle situations (per the corpus-oracle check):
- **Key-areas → directly validatable** against the chorale ground-truth local keys (When-in-Rome `Key:` tokens, 326/353
  human + music21).
- **Punctuation-spans → two oracles:** the chorale **fermatas** (351/353 — the chorale grouping marker the primitive also
  consumes, so a strong but not fully independent check) **and**, once the DCML-TSV corpora are brought in, the **`{}`
  annotations** (DCML's punctuation-span markers; an independent oracle on that repertoire).
- **Cadence alignment → the DCML-TSV `|cadence` oracle, scoped to LOCATION** (robust to Roman-numeral errors; cadence
  *type* is harmony-dependent and only partially attributable on the harder repertoire — measured, caveated, not a clean
  gate).
- **Metrics:** punctuation-span-boundary and cadence-location **precision/recall** against the marker ticks; key-area
  accuracy as the **agreement of key-area boundary ticks with the ground-truth local-key change ticks** (plus the per-area
  tonic/mode match); the residual-honesty principle the lower layers established (a correctly carried open mark beats a
  guessed group).
- **Two-step plan:** (1) now — the narrow TSV oracle for punctuation-span + cadence-location (and the chorale fermatas for
  punctuation-spans); (2) later, at the pre-inference boundary — the wide full-pipeline generalisation baseline on the
  DCML-TSV corpora (`cowork_layer6_grouping_research.md` §6).
- **Dormant + byte-identical** until engagement (deferred): the corpus gate stays 53/24/53 by construction; L6 has no
  production consumer.

## 11. Risks & technical debt
- **The punctuation-span oracle is partly the phrase-boundary primitive's own input** (fermatas) — independent validation
  needs the TSV `{}` oracle; weight the fermata check accordingly.
- **Cadence-type is unvalidated on chorales and only partially attributable on the TSV repertoire** — carried under the
  verifiability contract with an explicit mark until a cleaner oracle exists.
- **The non-chorale TSV repertoire is harder for the chorale-tuned lower layers** — confounds cadence/key measurement;
  mitigated by scoping step 1 to punctuation-span + cadence-**location**.
- **`bwv112.5` has no fermata** — a 1-stem edge for the fermata punctuation-span oracle (handle in the metric, e.g. fall
  back to its graded boundary, or exclude from the fermata-recall denominator — a §10 metric detail, not a layer rule).
- **The scattered live paths** (`detectCadences`/`detectPivotChords`/`KeyArea`) are migration debt — owned and retired by
  L6 only at the deferred engagement.

## 12. Glossary — see §0
The primary terms — **punctuation-span, cadence, key-area/key-span, boundary, slice, open mark, sequence-span** (and the
out-of-scope **phrase [MT]**), and the jargon (**flat partition, hierarchical grouping, GTTM, Caplinian formal
functions**) — are defined once in **§0**, the single source (to avoid the duplicate-definition drift). Two operational
terms specific to §5.3:
- **Cadence alignment [L6]** — the association of a Layer-5 cadence with the punctuation-span it closes (or an *internal*
  tag when it falls mid-span).
- **Internal cadence [L6]** — a detected cadence not at a punctuation-span boundary; surfaced as a tension signal, not
  snapped or discarded.

## 13. Background: the as-built mapping
See §4. The phrase-boundary primitive (`engravingbridge/phraseboundaryview`), the Layer-5 output
(`function/functionoutput`), the Layer-3 local-key carry, and the scattered live `section/` grouping paths are the
concrete reuse/retire targets; the full reuse map is `cowork_layer6_grouping_research.md` §2.

## 14. Related work & external sources
**Borrowed:** the flat punctuation-span + cadence + key-area target and the non-hierarchical grouping-span definition from
the DCML / When-in-Rome annotation standard; the flat boundary-classification framing (grouping + section + cadence as
note-level tasks) from the SOTA unified analysers (AnalysisGNN); the change-point view of tonal segmentation (Spiral Array
/ Argus, change-point methods) as corroboration of the Layer-3-span key-area approach. **Discarded:** hierarchical / GTTM
grouping and prolongational reduction (no oracle, computationally below human accuracy); a standalone L6 detector
(duplicates upstream). Full scan: `cowork_layer6_grouping_research.md` §3.

**Polyphony & counterpoint (deep search, 2026-07-01, `cowork_polyphony_phrase_harmony_research.md`).** Confirms the
consensus this layer relies on: the field analyses harmony at the **onset/verticality level** (ChordGNN, `chordify`),
models phrase/cadence as **one texture-wide layer, not per-voice** (AnalysisGNN, the cadence-GNN), treats **voice
separation** as a *separate* task (Chew & Wu contig-mapping, VISA, Temperley, the link-prediction GNN — the foundation for
the future voice-leading axis), and absorbs the counterpoint / implied-harmony difficulty via an explicit **non-chord-tone
filter** (AnalysisGNN's non-chord-tone module; Contrapunctus) — a future **Layer-4 (emission)** lever, **not** L6's. No
located system models concurrent overlapping per-voice phrases for harmonic analysis, which is why L6's grouping is flat.
(In that literature "phrase/cadence detection" is the field's own term for the texture-wide task; it maps to our
**punctuation-span** + cadence-alignment work, not to the accepted melodic phrase [MT].)

## 15. Open items & deferred refinements
1. **The corpus-oracle gap is resolved** (the two-step TSV plan, §10). **Update (2026-06-30): the corpora are now on
   disk** (`tools/dcml/` + the `corpora/expl/dcml_*` clones), and their `harmonies/*.tsv` **already carry the `cadence`
   and `phraseend` columns** (the DCML TSV column names — unchanged, they are the data's own field names) — so "bring the
   corpora" is **done**. The remaining **TSV-oracle infrastructure** is only: extend `dcml_parser` to read those two
   columns + build the punctuation-span/cadence-location metrics — a build prerequisite for L6 validation, to be specified
   after this design is signed.
   **★ Update (2026-07-02, corpus Wave 1 — the oracle is now MEASURED, at scale):** the full DLC container (40/40) is
   onboarded and inventoried (`cc_corpus_wave1_report.md` §4; registry `layer_label_counts`): **9,662 cadence labels in
   921 of 1,284 files** (PAC 4,667 / HC 2,614 / IAC 1,616 / EC 279 / DC 195 / PC 86 + HC sub-types) and **24,436
   `phraseend` markers** — and `dcml_parser.py` currently **drops all three columns**, so the §10 oracles are a purely
   additive parser extension away. Known coverage limits, for the §10 metrics: **12 sub-corpora carry the column but 0
   cadence labels** (incl. `wagner_overtures`, `monteverdi_madrigals`, `schubert_winterreise` — cadence-location
   validation is unavailable there; punctuation-span validation via `phraseend` mostly remains); the richest cadence beds
   are beethoven / mozart / corelli / cpe_bach / scarlatti / couperin_concerts. The dev/held-out split (registry `split`
   field) applies: the §10 step-1 validation runs on the dev beds; held-out stays untouched per the engage-criteria E2
   discipline.
2. **The §5.1-a codetta refinement** and the **§5.3 alignment window** — confirm the exact rule shapes at build (the
   constants are precision-phase regardless).
3. **Sections / form** — the verifiability-gated extension (§9-D3); decide the verification strategy *if and when* a need
   and an oracle are identified. Default out.
4. **The corpus hygiene** (stray `corelli.xml`; `bwv112.5` no fermata) — handled in the parallel hygiene step; the
   `bwv112.5` metric treatment is a §10 detail.
5. **Engagement** (retiring the scattered live paths into L6) — deferred indefinitely with the rest of the architecture;
   production out of scope.
6. **★ Proper-layer prerequisite — reconcile the L5 §5.0 "region" definition (review finding, §5.2). ✅ RESOLVED
   2026-06-29.** L5 §5.0 read *region* as span-bounded and single-key; verified at the as-built, that conflated three
   distinct spans. Fixed by (a) the **architecture span-typology contract** (target-architecture §2 — the named span
   family, with the nesting-vs-cross-cutting rule and "region" unqualified banned), and (b) the **L5 §5.0 disambiguation**
   into slice / key-span / decision-context span / punctuation-span. L6's key-areas group the **key-span**, which
   **cross-cuts** punctuation-spans — now grounded in the clarified L5. Prerequisite closed.
7. **★ Span-name propagation (2026-07-01) — the grouping unit was renamed `phrase → punctuation-span` in THIS spec.** For
   cross-document consistency the same rename must reach: the **architecture §2.15 span-typology contract**, the **L5 §5.0
   disambiguation** (which names the grouping span — currently "phrase"), and, if the sibling rename is adopted, the
   **sequence-span → schema-span** change in `cowork_progression_schema_design.md`. Until that coordinated docs pass lands,
   those documents still say "phrase" / "sequence-span"; the mapping is 1:1 (`phrase → punctuation-span`). The upstream
   **phrase-boundary primitive** keeps its code name (`phraseBoundaryView` etc.) — a Layer-1.5 identifier, out of scope for
   a Layer-6 vocabulary change. Pending.
