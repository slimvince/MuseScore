# Layer 6 — Grouping (design)

> **Status: first draft (2026-06-29), pending the three-standards + language-mechanical review and Cowork/user sign-off
> (the L5 process).** Research foundation: `cowork_layer6_grouping_research.md`. This layer is specified by **rule and
> direction**; numeric calibration is the later precision phase (the firewall). Build **dormant + byte-identical**, validate
> against the oracles in §10, engagement deferred indefinitely (production out of scope).

## 1. The core principle
**Grouping is assembly, not detection.** Every signal Layer 6 needs has already been computed by an earlier layer — the
phrase boundaries (the Layer-1.5 primitive), the cadences and the Roman numerals (Layer 5), the local keys (Layer 3).
Layer 6 **assembles** these into the flat grouping structure the ground truth annotates: **phrases**, **key-areas**, and
the **alignment of cadences to phrase endings**. It detects nothing new and re-derives nothing; it reads the upstream
outputs and segments/labels the stream into groups. It is the cosmetic-but-structural top of the pipeline: it does not
change any Roman numeral, key, or cadence — it organises them.

## 2. The layer model — what L6 does and does not do
**Does:**
- **Phrase segmentation** — partition the analysed span into contiguous **phrases** delimited by the phrase-boundary
  primitive (§5.1).
- **Key-area grouping** — group maximal runs of same-local-key regions into **key-areas** (§5.2).
- **Cadence-to-phrase alignment** — associate each Layer-5 cadence with the phrase it closes, honouring the asymmetric
  cadence↔phrase relation (a cadence implies a phrase ending; a phrase may end without a cadence) (§5.3).
- **Carry the honest residual** — Layer-5 open marks pass through to the grouped output unchanged; L6 groups *around*
  uncertainty, it does not resolve it (§5.4).

**Does not do (out of scope for the validatable core):**
- **Hierarchical grouping** (grouping trees / GTTM time-span or prolongational reduction). The ground-truth phrase
  annotation is **explicitly non-hierarchical**; a tree has no oracle here. Deferred under the verifiability contract
  (§9-D3).
- **Caplinian formal functions** (period, sentence, antecedent/consequent) and **multi-phrase sections**. Real
  constructs, but with no oracle in our corpus; admitted only as a verifiability-gated extension, default **out** (§9-D3).
- **Melody / structural-line identification** (out of scope across the architecture; the perfect/imperfect cadence call
  is Layer-5's, made on bass-derived inversion, not the top voice).
- **Any change to the Roman numeral, key, or cadence** decided upstream — L6 is additive and read-only over Layer 5.

## 3. Inputs and outputs (the contract)
**Consumes** (all already produced, no new computation):
- **The Layer-5 output** (`FunctionLayerOutput`, §7 of the L5 design) — per analysis unit: the Roman numeral, the
  function confidence, the open mark, the committed identity; per region: the local key (possibly modulated) and the
  cadence markers (type, location, salience).
- **The phrase-boundary primitive** (`phraseBoundaryView` — `phraseBoundaryTicks()` and the graded
  `PhraseBoundaryProfile`): the boundary ticks and their strengths (fermata / breath / rest / barline / key-signature /
  tempo cues, max-normalised, peak-picked).
- **The Layer-3 local-key spans** (the per-region `keyModeResult`, surfaced through the Layer-5 per-region local key).

**Produces** — the flat grouping structure, **additive over Layer 5** (it annotates and segments; it does not replace any
upstream decision):
- **Phrases** — an ordered, contiguous partition of the analysed span; each phrase a `[startTick, endTick)` span with the
  units it contains, the boundary strength that opened/closed it, and the cadence (if any) that closes it.
- **Key-areas** — an ordered, contiguous partition into local-key spans; each `[startTick, endTick)` with its local
  tonic/mode and confidence.
- **Cadence-to-phrase alignments** — each Layer-5 cadence tagged with the phrase it closes (or flagged *internal* if it
  falls mid-phrase — §5.3), carrying its Layer-5 type and salience.
- **The carried open marks** — Layer-5's honest residuals, surfaced in the grouped view, never resolved here.

Phrases and key-areas are **two independent flat segmentations of the same span** (not nested): a key-area may span
several phrases, and — rarely — a phrase may straddle a key change. The contract to the display layer above is this
structure; L6 is its only producer.

## 4. As-built starting point (the scattered machinery this layer rebuilds)
Grouping already exists in production, **scattered and key-dependent**: `detectCadences()` (PAC/PC/DC/HC text markers) and
`detectPivotChords()` in `section/sectioncadencedetection`, both using the old key-dependent `ChordFunction::degree`
logic; and the `KeyArea` grouping in `analyzeSection` / `analyzed_section.h`. Layer 6 is the **forward-only rebuild** that
unifies these into one clean layer consuming the Layer-5 output + the phrase primitive + the Layer-3 spans — exactly as
Layer 5 unified the scattered function machinery. The old paths stay live until the joint engagement (deferred); L6 is
built dormant and byte-identical beside them.

## 5. Building-block view (the internal rules)

### 5.0 Shared definitions
- **Boundary.** A tick at which the phrase-boundary primitive places a picked peak (§5.1 of the phrase-boundary design):
  a local maximum of the texture boundary-strength profile above the pick threshold, or a deterministic marker spike
  (fermata / breath / structural barline / key-signature change / subito tempo / all-voice rest).
- **Phrase.** A maximal `[startTick, endTick)` span between two adjacent boundaries (the first boundary at/after the span
  start opens it; the next boundary closes it). Flat; phrases tile the analysed span with no gaps and no overlap.
- **Key-area.** A maximal run of contiguous regions sharing one local key (the Layer-5 per-region local tonic+mode),
  `[startTick, endTick)`.
- **A cadence (Layer-5).** A `FunctionalCadence`: a type (PAC/IAC/Half/PhrygianHalf/Deceptive/Plagal/Evaded), an
  approach→arrival tick pair, and a salience weight. L6 reads it; it does not re-detect it.

### 5.1 Phrase segmentation
Partition the analysed span at the boundary ticks supplied by the primitive: each phrase runs from one boundary
(inclusive) to the next (exclusive). The partition is **total** (covers the whole span) and **flat** (no nesting). The
first phrase opens at the span start even if no boundary marker sits there; the last phrase closes at the span end. **L6
consumes the primitive's picked-peak set as-is — it does not re-threshold or re-detect boundaries** (peak selection is the
primitive's owned job, §5.1 of the phrase-boundary design); choosing *which* ticks are boundaries is upstream, and how
they *group into phrases* is the rule here.
- **Phrase interlocking** (`}{`): where a boundary is simultaneously one phrase's structural end and the next phrase's
  start, the single boundary tick serves both — there is no gap.
- **Codetta / annexe** (the DCML refinement that the *structural* end can precede the literal next phrase start): the
  primitive supplies a single boundary tick, so the base partition places the phrase end there. Distinguishing a
  structural end from a trailing codetta is a **graded-strength refinement** (the structural end is the stronger peak) —
  specified as a refinement (§5.1-a), not required for the flat partition.
  - **(§5.1-a, refinement)** Where two boundaries fall close together (a strong structural peak followed by a weak one),
    the **stronger** peak is the phrase's structural end and the span between them is its codetta; the weaker peak does
    not open a new phrase. The closeness window and the strength margin are precision-phase constants.

### 5.2 Key-area grouping
A **key-area** is a maximal span of constant local key. Read the upstream **local-key track** (the local tonic and mode
carried per analysis unit by Layers 3/5) in order; open a key-area at the first unit; extend it while the local key is
unchanged; **close it and open a new one at each local-key change**. The granularity at which a key change can fall is the
granularity at which the local key is carried upstream — the chord-rhythm analysis unit, which is **finer than a phrase** —
so a key change may fall **within** a phrase; key-areas are therefore an **independent** flat segmentation, **not** nested
in phrases (§3, §9-D5). Each key-area carries its local tonic and mode and a **confidence that is non-increasing in its
weakest unit's key confidence** (the exact combiner — for example the duration-weighted mean — is precision-phase; this
direction is fixed here). The rule that a key change starts a new area is fixed here.
- **A confirmed Layer-5 modulation** (§5.4 of the L5 design) is already reflected in the local-key track it commits, so a
  key-area boundary falls exactly where the modulation recompute committed the new key — L6 reads that; it does not
  re-decide the modulation.
- **★ Proper-layer flag (review finding, 2026-06-29).** L5 §5.0 defines *region* as "a maximal run of slices between two
  adjacent phrase boundaries, carrying one prevailing key" — phrase-bounded and single-key, which would forbid a mid-phrase
  key change and force key-areas to nest in phrases. The **as-built** carries the local key at **chord-rhythm** (sub-phrase)
  granularity, which **does** permit a mid-phrase key change, as the ground truth annotates. This terminological tension is
  **L5/L2's to reconcile** (the proper layer): clarify the §5.0 "region" wording to the chord-rhythm sense, or state the
  local-key carry granularity explicitly. L6 consumes the local-key track at whatever granularity the reconciled definition
  fixes; this design assumes the sub-phrase (as-built) granularity (open item §15-6).

### 5.3 Cadence-to-phrase alignment
Associate each Layer-5 cadence with a phrase, honouring the **asymmetric** relation (ground truth: a cadence almost always
coincides with a phrase ending; many phrases end with no cadence):
- A cadence **closes** the phrase whose **ending boundary lies at the cadence's arrival tick, or within the alignment
  window after it** (a cadence's arrival may slightly precede the notated phrase end — for example a suspended resolution;
  the window's width is a precision-phase constant, its existence fixed here). That cadence is the phrase's **closing
  cadence**.
- A phrase with **no** cadence arriving within the window before its ending boundary ends **without a cadence** — a valid,
  common case; it is not forced to carry one.
- A cadence whose arrival lies **within the alignment window of no phrase boundary** is tagged **internal** (mid-phrase)
  and surfaced as such — **not** snapped to a distant boundary and **not** discarded. An internal cadence is a *diagnostic
  signal* (it means either a missed boundary or an over-eager cadence); L6 records it rather than resolving it — resolving
  it would require re-deciding the boundary or the cadence, both upstream and not L6's to override (§8).
- The **perfect/imperfect** and other type distinctions are Layer-5's (carried verbatim); L6 only positions the cadence in
  the phrase structure.

### 5.4 Carrying the residual
A Layer-5 open mark on a unit is surfaced on the phrase and key-area that contain that unit (the group is reported as
carrying an unresolved reading at that location). L6 **never** resolves an open mark — it has no evidence Layer 5 lacked.
A phrase composed entirely of confidently-read units is reported as fully resolved; one containing an open mark is
reported with the residual visible.

## 6. The layer is exactly these four rules (the proportionality bound)
Layer 6 defines no mechanism beyond §5.1–§5.4 — there is no fifth rule, no detection of its own, no hierarchy. Pressure to
add a rule is a signal to check whether the work belongs in an **earlier** layer (a detection that should be a primitive)
or is an **out-of-scope extension** (§9-D3) — not a new Layer-6 mechanism. The proportionality discipline (§7) holds the
layer to the assembly of the four.

## 7. Crosscutting concepts
- **Additive and read-only over Layer 5.** L6 changes no upstream decision; it segments and labels. This is the
  no-feedback half of the forward-only contract (§8 of the target architecture): grouping is **downstream** of Layer-5's
  resolution and override, and does not feed back into them.
- **Reuse, do not duplicate.** Phrase boundaries come from the one primitive; cadences and Roman numerals from the one
  Layer-5 output; local keys from the one Layer-3 carry. L6 adds **no** second boundary detector, cadence detector, or key
  segmenter. It **retires** the scattered `detectCadences`/`detectPivotChords`/`KeyArea` paths into itself at engagement.
- **The firewall.** The alignment window, the codetta closeness/margin, and the key-area confidence combiner are
  precision-phase constants; this document fixes the rules and their direction, not the numbers.
- **Proportionality.** The SOTA reaches competitive Roman-numeral accuracy with **no** explicit grouping layer (grouping
  falls out of stable key runs — `contrapunctus_findings.md`). L6 is a deliberate **explainability** layer, not an
  accuracy requirement; it stays the thin assembly layer specified here and does not grow detection of its own.

## 8. The Layer-5-override ↔ Layer-6-merge division (the standing joint item, L5 §15-6)
Layer 5 owns the **fine-grain reading** of each slice and the **class-(b) override** of a confidently-wrong commit
(§5.5/§10 of the L5 design): it *corrects* labels. Layer 6 owns the **grouping of the already-corrected stream**: once
Layer 5 has resolved/over­ridden a slice, L6 **merges** the now-consistent slices into phrases and key-areas. The boundary
is clean and forward-only:
- Correction (changing a slice's reading) is **Layer 5's**, by selection among carried readings, fired by the §8 override
  mechanism. L6 sees only the corrected result.
- Grouping (segmenting the corrected stream) is **Layer 6's**, and it **never feeds back** to request a different
  correction. An internal cadence or a same-key merge that *looks* like it wants a different upstream reading is **surfaced
  (§5.3 internal tag)**, not acted on — the forward-only contract forbids the back-edge.
So there is no overlap and no cycle: Layer 5 decides *what each slice is*; Layer 6 decides *how the slices group*.

## 9. Architecture decisions (with the alternatives weighed)
- **D1 — Flat grouping, not hierarchical.** The ground-truth phrase annotation is explicitly non-hierarchical; the SOTA
  systems do grouping as flat boundary classification, not parsing. *Rejected:* a grouping tree (GTTM-style) — no oracle,
  and the literature finds full hierarchical parsing below human accuracy computationally.
- **D2 — Assembly, not detection.** L6 reuses the upstream primitives and detects nothing. *Rejected:* an independent L6
  phrase/cadence/key detector — it would duplicate Layers 1.5/5/3 and reintroduce the divergence the rebuild exists to
  remove.
- **D3 — Sections / periods / sentences are a verifiability-gated extension, default out (user-ratified verifiability
  contract, 2026-06-29).** They are sound theory but lack an oracle in our corpus. *Not refused outright:* admitted only
  with a chosen alternative-confidence path (a form-annotated corpus, or theory-rules-as-oracle) and an explicit
  "empirically-unvalidated" mark — decided at design time, not built into the core. The core is phrases + key-areas +
  cadence alignment.
- **D4 — Cadences align to phrases, asymmetrically; an off-boundary cadence is surfaced, not snapped (§5.3).** *Rejected:*
  forcing every phrase to end with a cadence (contradicts the ground truth) and snapping a stray cadence to the nearest
  boundary (hides a real tension signal and would be a covert upstream override).
- **D5 — Phrases and key-areas are independent flat segmentations, not nested.** *Rejected:* nesting key-areas inside
  phrases or vice-versa — the two do not align in general (a key change can fall mid-phrase), and nesting would assert a
  hierarchy the ground truth does not annotate.

## 10. Quality & testing — the validation strategy (the two-step oracle, user-ratified 2026-06-29)
L6's three outputs have three oracle situations (per the corpus-oracle check):
- **Key-areas → directly validatable** against the chorale ground-truth local keys (When-in-Rome `Key:` tokens, 326/353
  human + music21).
- **Phrases → two oracles:** the chorale **fermatas** (351/353 — the chorale phrase marker the primitive also consumes,
  so a strong but not fully independent check) **and**, once the DCML-TSV corpora are brought in, the **`{}` phrase
  annotations** (an independent oracle on that repertoire).
- **Cadence alignment → the DCML-TSV `|cadence` oracle, scoped to LOCATION** (robust to Roman-numeral errors; cadence
  *type* is harmony-dependent and only partially attributable on the harder repertoire — measured, caveated, not a clean
  gate).
- **Metrics:** phrase-boundary and cadence-location **precision/recall** against the marker ticks; key-area accuracy as
  the **agreement of key-area boundary ticks with the ground-truth local-key change ticks** (plus the per-area tonic/mode
  match); the residual-honesty principle the lower layers established (a correctly carried open mark beats a guessed
  group).
- **Two-step plan:** (1) now — the narrow TSV oracle for phrase + cadence-location (and the chorale fermatas for phrases);
  (2) later, at the pre-inference boundary — the wide full-pipeline generalisation baseline on the DCML-TSV corpora
  (`cowork_layer6_grouping_research.md` §6).
- **Dormant + byte-identical** until engagement (deferred): the corpus gate stays 53/24/53 by construction; L6 has no
  production consumer.

## 11. Risks & technical debt
- **The phrase oracle is partly the phrase primitive's own input** (fermatas) — independent validation needs the TSV `{}`
  oracle; weight the fermata check accordingly.
- **Cadence-type is unvalidated on chorales and only partially attributable on the TSV repertoire** — carried under the
  verifiability contract with an explicit mark until a cleaner oracle exists.
- **The non-chorale TSV repertoire is harder for the chorale-tuned lower layers** — confounds cadence/key measurement;
  mitigated by scoping step 1 to phrase + cadence-**location**.
- **`bwv112.5` has no fermata** — a 1-stem edge for the fermata phrase oracle (handle in the metric, e.g. fall back to its
  graded boundary, or exclude from the fermata-recall denominator — a §10 metric detail, not a layer rule).
- **The scattered live paths** (`detectCadences`/`detectPivotChords`/`KeyArea`) are migration debt — owned and retired by
  L6 only at the deferred engagement.

## 12. Glossary
- **Phrase** — a maximal flat span between two phrase boundaries; the punctuation/breath-level grouping unit (DCML's
  non-hierarchical `{ }`).
- **Key-area** — a maximal contiguous span of one local key.
- **Cadence alignment** — the association of a Layer-5 cadence with the phrase it closes (or an *internal* tag when it
  falls mid-phrase).
- **Internal cadence** — a detected cadence not at a phrase boundary; surfaced as a tension signal, not snapped or
  discarded.
- **Boundary** — a phrase-boundary primitive's picked peak (graded cue or marker spike).
- **Open mark** — Layer-5's carried honest residual, surfaced in the grouped view, never resolved by L6.

## 13. Background: the as-built mapping
See §4. The phrase primitive (`engravingbridge/phraseboundaryview`), the Layer-5 output (`function/functionoutput`), the
Layer-3 local-key carry, and the scattered live `section/` grouping paths are the concrete reuse/retire targets; the full
reuse map is `cowork_layer6_grouping_research.md` §2.

## 14. Related work & external sources
**Borrowed:** the flat phrase + cadence + key-area target and the non-hierarchical phrase definition from the DCML /
When-in-Rome annotation standard; the flat boundary-classification framing (phrase + section + cadence as note-level
tasks) from the SOTA unified analysers (AnalysisGNN); the change-point view of tonal segmentation (Spiral Array / Argus,
change-point methods) as corroboration of the Layer-3-span key-area approach. **Discarded:** hierarchical / GTTM grouping
and prolongational reduction (no oracle, computationally below human accuracy); a standalone L6 detector (duplicates
upstream). Full scan: `cowork_layer6_grouping_research.md` §3.

## 15. Open items & deferred refinements
1. **The corpus-oracle gap is resolved** (the two-step TSV plan, §10); the **TSV-oracle infrastructure** (bring the
   corpora; extend `dcml_parser` to read the `cadence` + `phraseend` columns; the phrase/cadence-location metrics) is a
   build prerequisite for L6 validation — to be specified after this design is signed.
2. **The §5.1-a codetta refinement** and the **§5.3 alignment window** — confirm the exact rule shapes at build (the
   constants are precision-phase regardless).
3. **Sections / form** — the verifiability-gated extension (§9-D3); decide the verification strategy *if and when* a need
   and an oracle are identified. Default out.
4. **The corpus hygiene** (stray `corelli.xml`; `bwv112.5` no fermata) — handled in the parallel hygiene step; the
   `bwv112.5` metric treatment is a §10 detail.
5. **Engagement** (retiring the scattered live paths into L6) — deferred indefinitely with the rest of the architecture;
   production out of scope.
6. **★ Proper-layer prerequisite — reconcile the L5 §5.0 "region" definition (review finding, §5.2). ✅ RESOLVED
   2026-06-29.** L5 §5.0 read *region* as phrase-bounded and single-key; verified at the as-built, that conflated three
   distinct spans. Fixed by (a) the **architecture span-typology contract** (target-architecture §2 — the named span
   family, with the nesting-vs-cross-cutting rule and "region" unqualified banned), and (b) the **L5 §5.0 disambiguation**
   into slice / key-span / decision-context span / phrase. L6's key-areas group the **key-span**, which **cross-cuts**
   phrases — now grounded in the clarified L5. Prerequisite closed.
