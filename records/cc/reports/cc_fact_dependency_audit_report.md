# The whole-graph fact-dependency audit — establishing acyclicity before the key-layer build

> **Status: READ-ONLY ANALYSIS (CC, 2026-07-13). Stage 1 of the #17 funnel — desk work, no build.**
> Executes `cc_instruction_fact_dependency_audit.md` (Cowork, 2026-07-13, at the user's direction).
> No `src/` edit, no build, no golden refresh, no corpus/report write, no existing register row
> re-scoped, no `ARCHITECTURE.md` / evidence-inventory / design-opening edit. **Everything below is a
> PROPOSAL** for the design pass and the user's ratification — nothing here decides anything.
>
> New discoveries are filed as NEW `OPEN_ITEMS.md` rows in this commit (OI-161…OI-167) per the standing
> register rule (c) — "every newly discovered issue gets a register row in the same commit that records
> the discovery". No existing row's scope was touched.
>
> **Premise Gate (#17b) discipline:** the §1 predictions were written to a scratchpad file as the FIRST
> artifact of the session, after reading only `CLAUDE.md`, `OPEN_ITEMS.md`, the `ARCHITECTURE.md` layer
> specs, `cowork_evidence_inventory.md`, and `cowork_key_layer_design_opening.md` — and **before any
> analysis code was opened**. They are reproduced verbatim in §1 with the finding beside each, including
> the three places I was wrong.

---

## §0 — Headline

**The rebuilt spine is acyclic. Every fact cycle in the code today lives in the legacy path that retires
at E4. But the key layer's *planned* consumption re-opens the question, and two of the evidence
inventory's five "broken circles" do not survive contact with the code.**

Five findings, in descending order of consequence:

**1. THE STOP — the cadence→key channel's premise is refuted at the code.** The design opening
(`cowork_key_layer_design_opening.md` §1) proposes that the dormant `functioncadence.cpp` "appears to BE"
the June dossier's called-for key-agnostic cadence pre-scan, and flags the identification as unverified
(its own §5). **Verified: it fails.** The detector is genuinely key-agnostic (FACT — no key parameter
anywhere), but it is **chord-derived**: its tonic hypothesis is *read off the Layer-4 committed chord
root* (`functioncadence.cpp:229` `const int tonicPc = arr.rootPc;`, and four siblings), and every entry
gate reads `.quality`. The dossier specified something different — a pre-scan running **before**
`analyzeKeyMode`, voting from **descending-fifth BASS motion** and leading-tone resolution, **enumerating
candidate tonics** (`cc_cadence_key_investigation_dossier.md:203-209`). That unit was never built.
**Not reading the key and not reaching upward in the layer order are two different properties** — the
evidence inventory's §8 break tests only the first. (Where the report says "key-agnostic ≠ layer-forward"
below, that is the shorthand for exactly this sentence, not a new term of art.)

**2. …and the break IS realizable, at a lower layer than anyone proposed.** The chord-free half of the
detector already exists inside `functioncadence.cpp`: `eventHasPc`, `voiceMovesFromTo`,
`dominantTritonePresent`, `leadingToneResolves` read **only** per-voice notes plus a candidate tonic
(`functioncadence.cpp:38-75, 117-124`) — zero chord fields. So the dossier's pre-scan is buildable as a
**Layer-1.5 derived view** (bass-motion intervals + per-voice semitone-resolution events + the existing
phrase-boundary view) and consumed **strictly forward** by L3. Proposed owning layer: **L1.5**, with L5
keeping the cadence *typology* and the modulation-confirmation vote. Trade-offs in §5.

**3. The collection/tonic split is not a hypothesis — the rebuilt L4 is ALREADY tonic-independent.** The
dormant `ChordSliceDecoder` consumes the key at exactly one point and uses it for exactly two
collection-membership terms; `decideSlice` takes **no key at all** (`chordslicedecoder.h:599-604`), and
because it calls `analyzeChord` with `gateCtxOut=nullptr` it never runs the post-scoring gates, so the
one tonic-dependent scoring site cannot fire. Corroborated by corpus measurement (chord-flip-under-GT
fires on 0.30–0.37 % of key-disagree regions). **THEORY → FACT.** *But* two **live** tonic-dependent sites
remain in the legacy path, and one of them has **no retirement row** — §5.3.

**4. The progression-grammar break is vacuous as built.** `isLicensedProgression` is
**transposition-invariant** — a function of `(toRoot − fromRoot) mod 12` and the two chords' own qualities
(`functionprogression.cpp:125-143`). Scored "under each candidate key" it returns the **identical value
for every key**: zero key-discriminating information. The §8 "broken by enumeration" argument is logically
sound but names an instrument that cannot discriminate keys. The asset that *could* is
`harmonicvocabulary` (degree-offset skeletons, tonic supplied at query time) — dormant, no consumer.

**5. §8 enumerates five circles; the code has at least three more.** `ARCHITECTURE.md` §2.14 itself names
two that §8 omits (segmentation↔chord, functional-role↔chord-identity), and the audit found a third that
appears in neither: a **Layer-1.5 note-view primitive that runs full chord analysis**
(`regiontoneprimitives.cpp:451-592` `findTemporalContext`, LIVE, at `ScoringPhase::Final` — i.e. with all
progression signals active), which the §2.14 mitigation does not cover and which is **not on the
retirement map**.

**Verdict on the question the user asked.** The feed-forward holds for the *rebuilt* spine today, and
holds for *most* of what the key layer wants to consume. It does **not** hold, as currently designed, for
three of the key layer's intended inputs: the cadence vote, progression grammaticality, and NCT-cleaned
tone collections. Each has a proposed resolution (§5); none should be built until the layer assignment is
ratified.

---

## §1 — Premise Gate: the predictions, written before any code was read (#17b)

Recorded verbatim from the scratchpad artifact written as the session's first action. A large gap is
itself diagnostic (#3), so the misses are reported first.

### Where I was WRONG (the diagnostic gaps)

| # | Prediction | Finding | Diagnosis |
|---|---|---|---|
| **P2-c3** | *"I predict I will **not** be able to find that ['chord roots are key-invariant under collection siblings'] measurement as an established artifact, and will have to label the claim ASSUMPTION or THEORY, not FACT. If so, circle 2's break depends on an unestablished premise — a Class-A (#18) exposure and a STOP candidate."* | **WRONG, favorably.** The measurement exists, is established, corpus-wide and reproducible (`cc_mode_key_chord_probe_report.md` §0/§2; artifact `tools/reports/joint_probe_measure.json`; refreshed at OI-159). And the code gives an even *stronger* result than the measurement: the rebuilt L4 is tonic-independent **by construction**, not merely empirically. | My prior underweighted how much of the key↔chord question had already been measured and ratified (OI-43/OI-44). The register carries it; I did not credit it before predicting. |
| **P4** | *"'Relocate it downward so the key layer's consumption is forward' is **NOT achievable** … I predict the audit's honest answer is a **STOP**: the key layer cannot consume a cadence vote in a strictly-forward graph."* | **WRONG in the constructive direction.** The cadence *typology* indeed cannot move below L4 — but the *evidence predicates* are **already chord-free in the realized code**, so the dossier's pre-scan **is** realizable at L1.5, strictly forward. | I reasoned from the header's contract prose ("mapped from the L4 decoder's committed chord") and predicted before reading the bodies. The bodies are more separable than the contract implies. Reading the contract is not reading the code (#15). |
| **P2-c5** | *"key ↔ progression-grammar — expect BROKEN-BY-ENUMERATION in principle, but with the same PLACEMENT problem as cadence."* | **Right about the placement, but I missed the bigger fault:** the as-built `isLicensedProgression` carries **zero** key information, so enumeration over keys is a no-op. I predicted a placement problem and found an instrument problem underneath it. | I assumed the named asset did what the design doc said it did, instead of checking. Same error class as P4 — trusting the prose. |

### Where I was RIGHT

| # | Prediction | Finding |
|---|---|---|
| P1-a | Current upward edges: 3–6, *"most of them in the LEGACY (retiring) path, not the rebuilt spine"*; the rebuilt spine *"clean of upward fact edges, because each was certified"*. | **CONFIRMED in kind, understated in count** (~16 live sites, not 3–6). The rebuilt spine (`note_model` → `slicer` → `keymodesequence` → `chordslicedecoder` → `function/` → `groupinglayer`) has **zero** upward fact edges. `keymodesequence` has no `chord/`, `function/`, `grouping/` or `decode/` include anywhere (§3). |
| P1-b | The OI-86/OI-93 back-edges are *"TYPE includes, not fact dependencies … layering smells but will NOT show up as edges in the fact graph."* | **CONFIRMED.** `metricweights.cpp` contains no `chord`/`function`/`degree` reference at all; its `key/keymodeanalyzer.h` include (`metricweights.h:42`) reaches two types that both now live in the `types/analysistypes.h` leaf. `keymodeanalyzer.cpp:24` / `keyresolver.cpp:41` → `chord/analysisutils.h` are pitch-class utilities, not chord facts. |
| P1-c | *"`greedyExpandSegmentation` consuming `analyzeChord` scores — that is a live L2←L4 fact edge."* | **CONFIRMED** (`harmonicsegmenter.cpp:738-755` and 7 further sites). And the §2.14 mitigation is **partial**, not a cut — §4.1. |
| P2-c1 | key↔spelling: *"expect CONFIRMED BROKEN, upgradeable THEORY→FACT. Highest confidence of the five."* | **CONFIRMED** — `NoteEvent::tpc` (`note_model.h:82`); spelling is INPUT. *But* the channel to the emission does not exist (§5.1). |
| P2-c2 | key↔cadence: *"expect SHAKY. This is the one I expect to break."* | **CONFIRMED** — it is the STOP. |
| P2-c4 | chord↔NCT: *"an intra-layer loop is not a cross-layer fact cycle. But the key layer's wish to consume NCT-cleaned tones re-exports it as an L3←L4 edge."* | **CONFIRMED exactly.** That re-exported edge has no break (§5.4). |
| P3 | *"I expect to find at least two [sixth circles] the §8 map does not enumerate, both of which `ARCHITECTURE.md` §2.14 DOES name — meaning §8 is an incomplete restatement of our own doc."* | **CONFIRMED**, plus an unpredicted third (`findTemporalContext`). |

---

## §2 — Task 1: the canonical layer order

**Source of truth:** `cowork_target_architecture.md` §2 (the ratified layer table) + `ARCHITECTURE.md`
§2.15 (the three kinds of work) + `ARCHITECTURE.md` §3.3 (the per-layer specs). The order below is
confirmed at all three and matches the runtime call order in `regionanalyzer::analyzeRegions`
(signature context `:630-631` → slices `:632` → key decode `:634` → segmentation `:870` → chord `:987`).

| # | Layer | Kind (§2.15) | Fact or Judgment | Build state |
|---|---|---|---|---|
| 0 | **The score / DOM** (input surface) | — | Input | — |
| 1 | **L1 note model** — `notemodel/` | representation | Fact | Built+Live |
| 1.5 | **L1.5 derived views** — `engravingbridge/` (spelling, phrase-boundary), `scoreharvest/` (metric weights); the orthogonal voice-leading axis VL-A/B/C | representation | Fact | Live (spelling, metric weights) / Dormant (phrase-boundary, VL) |
| 2 | **L2 change-point slicer** — `slicing/` | representation | Fact | Built+Live |
| 3 | **L3 key/mode** — `key/keymodesequence` | **inference** | Judgment | Built+Live |
| 4 | **L4 chord + non-chord-tone** — `chord/chordslicedecoder` | **inference** | Judgment | Built+Dormant |
| 5 | **L5 function/cadence** — `function/` | **inference** | Judgment | Built+Dormant |
| 6 | **L6 grouping** — `grouping/` | assembly | View | Built+Dormant |

Off-spine: the **Harmonic Vocabulary** (`vocabulary/`) — a queried knowledge component, *not* a layer, with
no *(evidence-source × question)* contract (`cowork_target_architecture.md` §2). The **voice-leading axis**
is orthogonal, not above or below.

**"Upward" is therefore: a consumer at a lower number reading a fact produced at a higher number.**

### Does the architecture intend a strictly forward feed?

**Yes — with exactly one sanctioned exception class, and one thing that must not be confused with it.**

- **The forward-only rule** (`ARCHITECTURE.md` §2.14 the 2026-06-29 reconciliation; §2.15): "each layer is
  feed-forward and emits ranked candidates + a confidence." The 2026-06-10 global joint-lattice decode is
  **superseded** ("do not build to it").
- **The ONE sanctioned backward edge** (`ARCHITECTURE.md` §2.15): the **confidence-weighted
  forward-override** — "a sanctioned backward edge is admissible only as a deliberate, surfaced, measured,
  documented exception (justified by a plateau, scoped, gated, convergence-bounded, recorded)." Two named
  instances: the **cadence-confirmed key modulation recompute** and the **fine-grain chord override**.
  Both exist in code, dormant: `forwardoverride.{h,cpp}` (a re-entrancy-guarded `OnePassClosure`,
  at-most-once per decision id, forward sweep only), instantiated at `functionresolver.cpp:468/490-497`
  (chord) and `functionmodulation.cpp:143-154` (key). **These ARE upward fact edges.** They are bounded and
  versioned — unrolled over versioned facts they form a DAG (key_v1 → chords_v1 → cadence_v1 → key_v2 →
  …) — but at the *layer* level they are backward, and the architecture says so plainly rather than
  pretending otherwise.
- **NOT a fact cycle: the bounded-context loop.** `ARCHITECTURE.md` §2.15: a layer needing more context
  "requests an **append-only** extension from L1 — **a data-supply call down the stack, not an analysis
  back-edge**". Realized as `NoteModel::extend()` (`note_model.h:198`) and the gated-off reach-back at
  `regionanalyzer.cpp:658-720`. This is a **designed control-flow loop over the input supply**, carries no
  inferred fact upward, and is correctly excluded from the fact graph. I have not conflated the two.

### ⚠ One recorded ruling the design pass must reckon with

`cowork_target_architecture.md` §2, sub-point 1 (user-ratified, corrections recorded 2026-06-21) states the
L3 contract as: **"key/mode needs only the notes … NOT chord symbols, functions, or cadence detection"**,
and explicitly records that *"a later [draft] imported **cadence detection** into key/mode — **both
wrong** … the cadence/function-based key refinement is the **gated Stage 5**."* The L3 layer spec repeats
it: *"Needs NO chord symbols, functions, or cadence detection."*

The design opening's Decision 3(b) proposes precisely what that ruling rejected (a cadence fact consumable
by the key decode) — and the escape hatch that ruling pointed at (the gated Stage-5 joint step) is now
**shelved on both axes** (OI-43/OI-44). This is not a defect in either document; it is a **live
contradiction between two ratified positions** that the design pass must resolve explicitly. Filed
**OI-161**. My §5.2 proposal is one way to resolve it *without* violating either — the pre-scan is not
"cadence detection" in the sense the ruling forbade (it is a bass/voice-leading tonic-evidence primitive,
below the chord layer), and it is not the shelved joint step.

---

## §3 — Task 2: per-layer produced / consumed facts, from the code

Every row derived from the code and cited. **Discrepancies vs `cowork_evidence_inventory.md` are flagged
`▲` and collected as proposed corrections in §3.8.**

### 3.1 — L0, the input surface

| Fact | Status at the code | vs inventory |
|---|---|---|
| Notated pitch + **spelling (tpc)** | INPUT → `NoteEvent::tpc` (`note_model.h:82`) | agrees |
| Notated key signature; declared mode | INPUT → `resolveKeySignatureContext` (`keyresolver.h:105-110`), live at `regionanalyzer.cpp:630-631` | agrees |
| Mid-piece key-signature CHANGE | Read by **two** consumers: never re-anchored by L3 (OI-94(a)) — **but detected as a phrase-boundary marker** at `phraseboundaryview.cpp:137-142` | ▲ partial |
| **Fermatas** | **READ** — `phraseboundaryview.cpp:113` `a->isFermata()` | **▲ the inventory says "UNDISCUSSED … not in the note model's 11 documented facts. Cheap to read"** |
| Breath marks / caesuras | **READ** — `phraseboundaryview.cpp:120-123` | ▲ not in the inventory |
| Double / END / repeat barlines | **READ** — `phraseboundaryview.cpp:163-165` | **▲ the inventory says "the rest UNDISCUSSED — a double barline is a section boundary hint"** |
| Ritardando-family tempo spanners | **READ** — `phraseboundaryview.cpp:183-189` | ▲ not in the inventory |
| Long rests as phrase ends | **READ** — all-voice-rest spans ≥ `minSilenceTicks` (`phraseboundaryview.cpp:200`; threshold **240**, `phraseboundaryview.h:108` — an OI-87 unfit constant) | agrees ("HALF-EMBODIED") |
| Score chord-symbol / RN annotations | Recognized as flags, never read (OI-80) | agrees |

**The headline correction:** the evidence inventory treats fermatas as the *cheapest unread high-value
fact in the system*. They are **not unread** — they are read, together with four other punctuation cues,
by a **built L1.5 view that is gated off** (`phraseBoundaryTicks`'s only `src/` caller is
`regionanalyzer.cpp:431`, inside `applyJointKeyWiring`, gated at `:1472` on `jointKeyWiringEnabled()`,
default OFF at `jointkeydecision.cpp:144-145`). The gap is **publication and wiring, not detection.**
Filed **OI-162**.

### 3.2 — L1, the note model (`notemodel/note_model.{h,cpp}`) — Built+Live

- **PRODUCES:** `NoteEvent` × 11 fields, exactly: `pitch, tpc, staff, voice, onset, release, duration,
  isGrace, plays, visible, staffEligible` (`note_model.h:80-92`). Query API: `overlapping(t0,t1)`,
  `onsetIn(t0,t1)`, `extend(Direction, amount)` (`note_model.h:198-223`).
- **CONSUMES:** the engraving `Score*` only. **Zero higher-layer includes.**
- Agrees with the inventory, including the OI-74 voice-blindness downstream (voice IS on `NoteEvent`; it
  is dropped at the shared `ChordAnalysisTone` surface, not here).

### 3.3 — L1.5, the derived views

| Module | Produces | Consumes | State |
|---|---|---|---|
| `spellingview` | `lineOfFifths(tpc)`, `sharpFlatSense`, `SpanSpelling{count, lofCentroid, sharpCount, flatCount, naturalCount}` (`spellingview.h:86-108`) | a raw `tpc` int | `lineOfFifths` **LIVE** (consumed by `chordslicedecoder.cpp:610`, `functionrelationallabel.cpp:77,83`); `sharpFlatSense`/`spanSpelling` **DORMANT, zero consumers** (self-declared `spellingview.h:48`) |
| `phraseboundaryview` | `PhraseBoundaryProfile{perVoice, textureTicks, textureStrength, pickedTicks}`, `phraseBoundaryTicks()` (`phraseboundaryview.h:132-175`) | `Score*` → `NoteModel` + `changePointSlices`. **Key-, chord-, function-agnostic** (`phraseboundaryview.h:31-33`) | **DORMANT on production** (gated behind `jointKeyWiringEnabled()`) |
| `metricweights` | `beatTypeToWeight`, `regionMetricWeightForBeatType` (1.0/0.85/0.75/0.5), `timeDecay`, `buildPedalWindowIndex` (`metricweights.h:74-128`) | engraving DOM + `KeyModeAnalyzerPreferences` **scalars** | **LIVE** |
| `regiontonecollector` / `regiontoneprimitives` | `weightedPcView`, `soundingAt`, `buildTones`, `collectPitchContext`, `detectOnsetSubBoundaries`, `detectBassMovementSubBoundaries`, **`findTemporalContext`** | notes — **except `findTemporalContext`, which runs full chord analysis** (§4.2) | **LIVE** |
| voice-leading axis (`voicelinearview`, `voiceleadingprofiles`, `textureclassifier`) | `VoiceLinearView`, `MotionProfile`, `IntervalProfile`, `VoiceLeadingSpan` | `NoteModel` only. **Zero higher-layer includes** | **DORMANT** (only `tools/batch_analyze.cpp`) |

**`metricweights.h:42` → `key/keymodeanalyzer.h` is TYPE-ONLY, not a fact edge** — verified: `metricweights.cpp`
contains no `chord`/`function`/`degree` reference, never calls `analyzeKeyMode`, and both types it reaches
(`KeyModeAnalyzerPreferences`, `PitchContext`) now live in the `types/analysistypes.h` leaf. This
**confirms** the OI-86 finding as a layering smell and **excludes** it from the fact graph.

### 3.4 — L2, the change-point slicer (`slicing/slicer.{h,cpp}`) — Built+Live

- **PRODUCES:** `struct Slice { int start; int end; }` — **two fields, nothing else** (`slicer.h:84-87`).
  Content is the lazy query `model.overlapping(start,end)`.
- **CONSUMES:** `NoteModel` only. `slicer.cpp` includes nothing but its own header and `<algorithm>`.
- **Zero interpretation, zero higher-layer facts.** This is the module that structurally kills the
  segmentation↔chord circle (§6.6a).
- ▲ **Does NOT produce boundary STRENGTH or harmonic rhythm.** The inventory lists both as UNDISCUSSED
  L2 facts and the design opening wants both; confirmed absent — they are genuine build items, and both are
  strictly-forward (L2 → L3). No cycle.

### 3.5 — L3, key/mode (`key/keymodesequence.{h,cpp}`) — Built+Live

- **`decode()` signature** (`keymodesequence.h:212-219`): `(slices, noteModel, keySigFifths,
  declaredMode?, keyPrefs, seqPrefs, excludeStaves)`.
- **PRODUCES:** `SliceKeyMode{sliceIndex, chosen, alternatives, confidence, uncertain}`
  (`keymodesequence.h:158-164`). The region reduction folds per-slice alternatives into
  `HarmonicRegion.keyAlternatives` + `keyConfidence` (`regionanalyzer.cpp:790-791, 842, 1031-1032`).
- **CONSUMES ZERO L4/L5 FACTS — structurally.** Its header includes are `keymodeanalyzer.h`,
  `note_model.h`, `metricweights.h`, `slicer.h`; its `.cpp` includes add only STL, `engraving/types/constants.h`,
  and `regiontonecollector.h`. **No `chord/`, no `function/`, no `grouping/`, no `decode/` include
  anywhere.** This is the strongest single fact in the audit: **the live key layer is clean.**
- **The emission's evidence surface is 4 fields.** `PitchContext` (`analysistypes.h:930-935`) =
  `{pitch, durationWeight, beatWeight, isBass}`. ▲ **No `tpc`.** So the spelling-aware emission the design
  opening's Decision 2(a) rests on has **no channel** — an L1→L3 field must be added. Strictly forward; a
  build item, not a cycle. Filed **OI-163**.
- ▲ **Alternatives are published; per-alternative confidence is NOT.** `SliceKeyMode.alternatives` carries
  `score = emission` but `normalizedConfidence = 0.0` (`keymodesequence.cpp:100-101`) — only `chosen` is
  stamped. This is the precise, code-level form of OI-75/OI-81 ("margins DISCARDED"), and it matches the
  probe's independent measurement (`keyConf` populated on 0.01 % of alternatives). The *region-level*
  sequence margin IS published — and has **no production consumer** (`harmonicrhythm.h:113-119`: "has NO
  consumer — it exists for Layer 5").

**The L3-adjacent `section/` modules — all DORMANT, and all consuming L4 chord facts:**

| Module | Consumes | State |
|---|---|---|
| `cadencekeyanchor` | `CadenceRegionInput{startTick, endTick, rootPc, quality, pitchClassMask, endsPhrase}` — **`rootPc` + `quality` are the L4 winner** (supplied at `regionanalyzer.cpp:449-450` from `hr.chordResult.identity`) | DORMANT; kept-as-diagnostic through E4 (**R3**) |
| `localmodulationdetector` | same `CadenceRegionInput` stream ⇒ same L4 fact | DORMANT |
| `jointkeydecision` | L4 winner **+ chord alternatives** (`chordAlts` drives `couplingBonus`), L3 local candidates, the L1.5 `endsPhrase` fact | **GATED OFF** (`jointKeyWiringEnabled()` default false) — **this is the shelved joint step (OI-43/OI-44)** |

### 3.6 — L4, chord (`chord/chordslicedecoder` — Built+Dormant; `chord/chordanalyzer` — the live legacy scorer)

**The rebuilt decoder:**
- `decode()` takes `(slices, noteModel, keySignatureFifths, keyMode, chordPrefs, decoderPrefs, excludeStaves)`
  (`chordslicedecoder.h:524-531`). **`decideSlice()` takes NO key at all** (`chordslicedecoder.h:599-604`).
- The **only** use of the key in the entire decoder is one call —
  `analyzeChord(tones, keySignatureFifths, keyMode, /*context=*/nullptr, prefs, /*gateCtxOut=*/nullptr, &snapshot)`
  (`chordslicedecoder.cpp:452-454`) — from which it reads only the vertical cell scores.
- Because `gateCtxOut = nullptr`, **the decoder never runs `applyPostScoringGates`**, so the one
  tonic-dependent scoring gate (G-E) **cannot fire in L4 at all**.
- Everything downstream — ranking, the spelling pin, membership, sufficiency, commit/inherit/abstain,
  confidence, the open-question label — is **key-free**.
- **PRODUCES:** `SliceChord{chosen, alternatives, confidence, decision, openQuestion, …}`; membership
  verdicts; abstention margins.

**Key → chord, classified TONIC vs COLLECTION (the audit's crux):**

| Site | Uses | Class | Live? |
|---|---|---|---|
| `chordanalyzer.cpp:1403` `dim7CharacteristicBonus` (body `:574-578`) | `keyTonicPc`, `scale` | **COLLECTION-only** | LIVE + in decoder |
| `chordanalyzer.cpp:1406` `diatonicRootContribution` (body `:896-907`) | `keyTonicPc`, `scale` | **COLLECTION-only** | LIVE + in decoder |
| `chordanalyzer.cpp:999-1018` `function.diatonicToKey` | `keyTonicPc`, `scale` | **COLLECTION-only** | LIVE |
| `postscoringgates.cpp:475-480` (Gate I), `:520-525` (Gate L) | `keyTonicPc`, `scale` | **COLLECTION-only** | LIVE |
| **`postscoringgates.cpp:379-385` (Gate G-E)** | `keyTonicPc` → the ii/iii/vii **degrees** | **TONIC-DEPENDENT — changes the committed chord** | **LIVE** (preset-gated `preferMinorOverMajorAdd6`, ON for Baroque; **NOT in the decoder**) |
| **`sparsechordrefinement.cpp:154-159`** (Aeolian lone-tonic/dominant guard) | `keyMode == Aeolian && (degree == 0 \|\| degree == 4)` | **TONIC + MODE-DEPENDENT** | **LIVE** (`regionanalyzer.cpp:1003`; **NOT in the decoder**) |
| the rest of `sparsechordrefinement` | degree → `diatonicTriadShapeForDegree` | **COLLECTION-only in effect** (the tonic cancels: the composition is "the diatonic triad on this root within this collection") | LIVE |

**Why COLLECTION-only is provable, not asserted.** `keyTonicPc = ionianTonicPc + keyModeTonicOffset(mode)`
and `scale = MODES[parent].intervals` are rotations of one another, so the set `{keyTonicPc + scale[i]}` is
**identical for all 7 diatonic modes of one signature**. C-Ionian and A-Aeolian construct the same 7 pitch
classes, and both key-consuming scoring terms only ask *"is pc in that set"*. The oracle **cannot
distinguish relative major from relative minor.** (The code says so itself at `chordanalyzer.cpp:1544-1549`
and `chordslicedecoder.cpp:703-711`.)

### 3.7 — L5 function (`function/`) — Built+Dormant — and L6 grouping

| Module | Key input? | L4 chord input? | State |
|---|---|---|---|
| `functioncadence` | **NO — none** (`detectFunctionalCadences(events, params)`, `functioncadence.h:260-262`) | **YES, foundational** — `CadenceEvent{rootPc, quality, bassPc, notes, metricWeight, endsPhrase, isFinalBar}` | DORMANT |
| `functionprogression` | **NO — none.** `ProgressionChord{rootPc, quality}` is the whole chord input | YES (root + quality, projected) | DORMANT |
| `functionresolver` | YES — `ResolverKey{keyFifths, keyMode, tonicPc}`, but **only** for the §5.7 soft degree prior; the main `plausibility()` is **key-free** | YES, fully (`FunctionSlice`) | DORMANT |
| `functionmodulation` | **No key argument** on the main entry; candidate tonics come from L3 `LocalKeySpan`, confirming votes from L5 cadences | NO | DORMANT — **hosts the cadence-confirmed key recompute** (`.cpp:143-154`) |
| `functionromannumeral`, `functionrelationallabel`, `tonicizationlabeler` | YES — tonic → scale degree (legitimate; `tonicizationlabeler.h:38-41` says so explicitly) | YES | DORMANT |
| `forwardoverride` | NO — includes only `<functional>`, `<set>`; opaque `int decisionId` | NO | DORMANT |
| `harmonicfunctionlayer` | key **structurally excluded** from its context by design (`.h:67-71`) | **it PRODUCES them** | **★ LIVE — this is the L4 legacy competition, not L5** (OI-117 confirmed at `chordanalyzer.cpp:25`, `regionanalyzer.cpp:44`) |
| `grouping/groupinglayer` (L6) | carried per unit, used only for run-equality key-area segmentation; **no degree, no collection** | **NO — no chord field reaches L6 at all** | DORMANT |
| `vocabulary/harmonicvocabulary` | **no resolved key** — entries are **degree-offset skeletons**, tonic supplied at query time (`.h:197-200`) | no L4 struct | DORMANT, **no consumer** |

**Two structural gaps found in the L5→L6 seam** (neither is a cycle; both are #12/#10 items):
- **No code edge `functionoutput` → `groupinglayer`.** `assembleGrouping` takes hand-built `GroupingUnit`s,
  not `FunctionLayerOutput`. The mapping exists only as a comment (`groupinglayer.h:41-47`) and in
  `batch_analyze`.
- **`GroupingUnit::keyConfidence` has no producer** (`groupinglayer.h:106-109`); `FunctionConfidence`
  (`functionoutput.h:85-99`) has no key-confidence field. A dangling consumer input.
Filed **OI-164**.

### 3.8 — Proposed corrections to `cowork_evidence_inventory.md` (evidence, not edits — OI-146's obligation (a))

| § | The inventory says | The code says | Proposed correction |
|---|---|---|---|
| §1 | Fermatas: "UNDISCUSSED as key evidence; not in the note model's 11 documented facts. Cheap to read; enormous leverage." | **Read** at `phraseboundaryview.cpp:113`, inside a built L1.5 view that is **gated off**. | Re-status **DORMANT (built, gated off)**, not UNDISCUSSED. The work is wiring + publication, not detection. |
| §1 | Barlines/repeats: "the rest UNDISCUSSED — a double barline is a section boundary hint". | **Read** at `phraseboundaryview.cpp:163-165`. Also breath/caesura (`:120-123`), mid-score key change (`:137-142`), ritardando (`:183-189`). | Re-status all five as DORMANT; add the three the inventory omits entirely. |
| §6 | "**Dominant-SHAPE detection as a key vote**" and "**Leading-tone-resolution events**" are filed under **Layer 4**. | Both are computable **without any chord decision**: a dom7 pc-set has a unique root by construction, and `leadingToneResolves` (`functioncadence.cpp:117-124`) reads **only** per-voice notes + a candidate tonic. | **Re-assign both to L1/L1.5.** This matters: as filed they look like upward edges into L3; correctly placed they are strictly forward. |
| §7 | "progression licensing (grammaticality)" is offered as key evidence "scored UNDER EACH CANDIDATE key". | `isLicensedProgression` is **transposition-invariant** ⇒ identical under every key ⇒ **zero** key information. | Name `harmonicvocabulary` (degree-offset, tonic-at-query) as the only key-discriminating grammar asset. |
| §5 | "the alternatives list (top-4, margins DISCARDED)". | Alternatives AND the region-level sequence margin **are** published; what is missing is **per-alternative** confidence (`= 0.0`, `keymodesequence.cpp:100-101`). | Sharpen: the loss is the per-alternative margin, not the list. |
| §8 | Five circles. | `ARCHITECTURE.md` §2.14 names two more (segmentation↔chord; functional-role↔chord-identity); the code has a third (`findTemporalContext`). | Add three (§6.6). |

---

## §4 — Task 3: the directed fact graph, with every upward edge flagged

### 4.0 The rebuilt spine — the clean core

```
  L0 score ──► L1 notes ──► L1.5 views ──► L2 slices ──► L3 key ──► L4 chord ──► L5 function ──► L6 grouping
                                                          │            │             │              ▲
                                                          └── collection ─┘          └──────────────┘
```
**Zero upward fact edges.** Proven by include-closure and signature: `keymodesequence` has no `chord/`,
`function/`, `grouping/` or `decode/` include; `chordslicedecoder::decideSlice` takes no key; `slicer`
includes only its own header. **The certified layers are acyclic. FACT.**

### 4.1 CURRENT upward edges — the LIVE legacy path (all retire, except one)

| # | Edge | Producer → Consumer | Site | Retires? |
|---|---|---|---|---|
| C1 | chord winner **score** gates an anchor boundary | L4 → **L2** | `harmonicsegmenter.cpp:738-755` | **R6** (segment-first spine, E4) |
| C2 | post-scoring gates run *inside* segmentation | L4 → **L2** | `harmonicsegmenter.cpp:743-744` | R6 |
| C3 | gap-fill seeds context from neighbour anchors' **committed chord roots** | L4 → **L2** | `harmonicsegmenter.cpp:379-381, 390-405` | R6 |
| C4 | Round-2 promotion: chord **identity** decides a boundary | L4 → **L2** | `harmonicsegmenter.cpp:454-514, 474-485, 534-570` | R6 |
| C5 | head/tail-gap synthesis gated on chord score | L4 → **L2** | `harmonicsegmenter.cpp:816-823, 908-915` | R6 |
| C6 | **head-gap tonic prior**: a resolved key overrides a synthesized region's chord | **L3 → L2** | `harmonicsegmenter.cpp:840-889` | R6 |
| C7 | `tryCollapseSameChordRegion` — a boundary is *removed* because chord identity matched | L4 → **L2** | `regionanalyzer.cpp:209-229` (call sites `:1041, :1239`) | R6 / E4 |
| C8 | `coalesceShortSameRootRuns` — coalescing keyed on chord root | L4 → **L2** | `regionanalyzer.cpp:116-195` | R6 / E4 |
| C9 | Pass-2/2b sub-region analysis reads neighbours' committed **bass** | L4 → **L2/L3 seam** | `regionanalyzer.cpp:1097-1104, 1299-1305` | R6 / E4 |
| C10 | `inferNextRootPc` — the *next* region's chord is analyzed and injected **before** the current region is scored | L4 → **L4 (forward-looking)** / seam | `regionanalyzer.cpp:972-973, 1189-1190, 1375-1379` | R6 / E4 |
| **C11** | **`findTemporalContext` — an L1.5 note-view primitive instantiates a chord analyzer and runs full `analyzeChord` at `ScoringPhase::Final`** | **L4 → L1.5** *and* **L3 → L1.5** | **`regiontoneprimitives.cpp:451-592`**, live at `regionanalyzer.cpp:918-919` | **★ NO RETIREMENT ROW** — see below |
| C12 | `cadencekeyanchor` / `localmodulationdetector` consume the L4 winner (`rootPc`, `quality`) | L4 → **L3-adjacent** | `regionanalyzer.cpp:449-450` | DORMANT (R3) |
| C13 | `jointkeydecision` consumes the L4 winner **+ alternatives** to score a key | L4 → **L3** | `regionanalyzer.cpp:493`, gated `:1472` | **GATED OFF — the shelved joint step (OI-43/OI-44)** |

**On §2.14's claimed mitigation.** `ARCHITECTURE.md` §2.14 says `greedyExpandSegmentation` "already
acknowledges [the segmentation↔chord circularity] by running its exploratory passes in
`ScoringPhase::Segmentation` (progression signals withheld)". **The mitigation is partial, not a cut.**
`analysistypes.h:68-69` defines the phase as: *"progression signals suppressed and Gate R skipped;
**rootContinuityBonus stays active (segmentation depends on it)**"* — so the chord score, root, quality
and a previous-chord-identity bonus all still flow into the boundary decision. And **C11 is not covered at
all**: it passes `kDefaultChordAnalyzerPreferences`, whose `scoringPhase` default is `Final`
(`analysistypes.h:386`) — i.e. it runs chord analysis with **every** progression signal active, from a
Layer-1.5 primitive. Filed **OI-165**.

### 4.2 PLANNED upward edges — what the key layer intends to consume

From `cowork_key_layer_design_opening.md` §2 + `cowork_evidence_inventory.md` §8, each classified at the code:

| Fact the key layer wants | Inventory files it at | **Realizable at** | Edge into L3 | Break? |
|---|---|---|---|---|
| **Cadence tonic+mode vote** | L5 | **L5** as built (chord-derived) | ▲ **UPWARD** | §5.2 — the STOP; **but a chord-free form is realizable at L1.5** |
| **Progression grammaticality under candidate key** | L5 | L5 (needs a chord sequence) | ▲ **UPWARD** | §5.5 — and the named asset carries **zero key information** |
| **NCT-cleaned tone collections** | L4 | **L4 by definition** (NCT needs a chord hypothesis) | ▲ **UPWARD — no break** | §5.4 — the second STOP |
| **Per-chord decision margin** | L4 | L4 | ▲ **UPWARD** | same class as NCT; only needed if the key layer scores chords |
| **Dominant-SHAPE key vote** | L4 | **L1.5/L2** — a dom7 pc-set has a unique root by construction; needs no chord *decision* and no key | **FORWARD** | ▲ **inventory mis-assignment** |
| **Leading-tone-resolution events** | L4 | **L1/L1.5** — `leadingToneResolves` reads only per-voice notes + a candidate tonic (`functioncadence.cpp:117-124`) | **FORWARD** | ▲ **inventory mis-assignment** |
| Bass-motion dominant→tonic skeletons | L1.5 (undiscussed) | **L1/L1.5** | FORWARD | ✓ |
| Fermatas + phrase-end facts | L0/L1.5 | **L1.5 — BUILT, gated off** | FORWARD | ✓ (wiring only) |
| Harmonic rhythm; boundary strength | L2 (undiscussed) | **L2** — genuinely absent, buildable | FORWARD | ✓ |
| Notated spelling + accidentals | L1 | **L1** — but **`PitchContext` has no `tpc`** | FORWARD | ✓ (channel missing — OI-163) |
| Declared mode; signature changes | L0 | L0/L1 | FORWARD | ✓ |
| Chromatic-alteration events | L4 | L1 (vs the **notated** signature) or L3-internal | FORWARD | ✓ |
| Score annotations (chord symbols/RN) | L0 | L0 (OI-80) | FORWARD | ✓ |
| Collection/tonic split; ambiguity/boundary margins | L3 | **L3's own output** | — | ✓ (publication) |

**Score: of the 14 facts on the key layer's shopping list, 10 are strictly forward, 2 are mis-assigned
upward by the inventory and are actually forward, and 4 are genuinely upward** (cadence vote, progression
grammar, NCT-cleaned tones, chord margin). Those four are §5's subject.

---

## §5 — Task 4: the break test per upward edge, and the proposed owning layer

### 5.1 Fixed-input edges — dissolved, FACT

Spelling (`NoteEvent::tpc`), signatures, declared mode, fermatas/barlines/breath marks, and score
annotations all **enter once from the score and are never inferred**. They cannot participate in a cycle.
**FACT**, cited in §3.1/§3.2.

*The one caveat, and it is a build item not a cycle:* the L3 emission's evidence surface is
`PitchContext{pitch, durationWeight, beatWeight, isBass}` (`analysistypes.h:930-935`) — **no `tpc`**. The
spelling-aware emission (Decision 2(a)) needs an L1→L3 channel that does not exist. Strictly forward.
**OI-163.**

### 5.2 ★ THE CADENCE→KEY EDGE — the STOP, and the proposed break

**The break test, applied at the code:**

| Question | Answer | Class |
|---|---|---|
| Is one side a fixed input? | No — a cadence is inferred. | — |
| Is a **key-agnostic** form realizable? | **YES, and it is BUILT.** `detectFunctionalCadences(events, params)` (`functioncadence.h:260-262`) takes **no key**. No key type crosses the module. | **FACT** |
| Is a **chord-agnostic** form realizable — i.e. is the detector *layer-forward* w.r.t. L3? | **NO, as built.** The tonic hypothesis is *read off the L4 committed chord root*: `tryAuthentic` `const int tonicPc = arr.rootPc;` (`functioncadence.cpp:229`); `tryPlagal` `:409` likewise; `tryDeceptive` `:301`, `tryHalf` `:358`, `tryEvaded` `:450` all `norm(root ± 7)`. Every entry gate reads `.quality`. The header confirms the intent: events are "mapped from the L4 decoder's committed chord … root, quality, bass" (`functioncadence.h:82-84`). | **FACT** |

**⇒ The §8 break tests the wrong axis.** §8 says the circle is "BROKEN BY THE KEY-AGNOSTIC FORM … the
rebuilt machinery votes for a tonic FROM root motion, quality, and the raised leading tone — no key
input." Every clause is **true**. But *root* and *quality* **are Layer-4 facts** — the sentence names the
problem without noticing it. **Key-agnostic ≠ layer-forward.** L3 consuming this vote is
**L3 ← L5 ← L4 ← L3**, a real cycle.

**⇒ The design opening's identification is REFUTED.** Its §1 says the machinery "appears to BE that
pre-scan's built form", and its §5 flags this as unverified. The June dossier specified
(`cc_cadence_key_investigation_dossier.md:203-209`):

> *"New key-agnostic cadence pre-scan (new code, runs **before** `analyzeKeyMode`, does **not** read the
> resolved key) … detect a structural dominant→tonic resolution by root motion (**descending-fifth bass**)
> and leading-tone resolution; **for each candidate tonic accumulate** a cadential weight … Integrate over
> the piece/section → a global `(tonicPc, mode)` cadential prior with a confidence."*

That unit is **bass-driven, chord-free, and tonic-enumerating**. `functioncadence.cpp` is **chord-root-driven
and tonic-reading**. They are different units, and the pre-scan **was never built**. Filed **OI-166**.

**⇒ BUT THE BREAK IS REALIZABLE — the chord-free half already exists.** Four predicates in
`functioncadence.cpp` read **only** `CadenceEvent::notes` (per-voice pitch) plus a candidate `tonicPc`, and
touch **no** `rootPc`/`quality`/`bassPc`:

| Predicate | Site | Reads |
|---|---|---|
| `eventHasPc` | `:38-47` | notes |
| `voiceMovesFromTo` | `:52-68` | notes (same-voice motion across the boundary) |
| `dominantTritonePresent` | `:72-75` | notes + candidate tonic |
| `leadingToneResolves` | `:117-124` | notes + candidate tonic |

Everything the dossier asked for is in that set, plus a bass-motion interval (an L1 fact: the lowest
sounding eligible pitch per slice) and phrase-end salience (**already built** at
`phraseboundaryview.cpp:113` et al.).

**★ PROPOSED OWNING LAYER — a candidate for the design pass, not a decision:**

- **L1.5 — a new derived view: the cadential-evidence primitive.** Enumerate the 12 (or 24) tonic
  hypotheses; for each, accumulate a weight from (a) bass motion 5̂→1̂ into a phrase end, (b) the
  same-voice 7̂→1̂ leading-tone resolution, (c) tritone/seventh presence relative to the hypothesis, (d)
  metric weight, (e) the existing phrase-boundary salience. **Consumed FORWARD by L3.** No cycle.
- **L5 KEEPS** the cadence *typology* (PAC/IAC/Half/Phrygian/Deceptive/Plagal/Evaded) and the
  modulation-confirmation vote — both legitimately need committed chords (`isRootPosition`,
  `isSecondInversionTonicTriad`, `isPredominant`, and the five `try*` gates are all chord-dependent).
- **Justified under §2.15's *(evidence-source × question)* invariant:** the L1.5 unit owns *the
  bass/voice-leading contribution to the **TONIC** question*; L5 owns *the chord contribution to the
  **CADENCE-TYPE** and **modulation-confirmation** questions*. Two concerns, two owners — gate (1) of the
  §2.15 new-component test, which is "a structural mandate, sufficient on its own."

**★ THE TRADE-OFFS — flagged honestly, per the instruction:**

1. **#6 duplication risk is REAL.** Two cadence-ish units invite a value-copy divergence (the DT-3 pattern:
   OI-92, OI-63). **Mitigation, mandatory if this is adopted:** the four chord-free predicates are
   **single-sourced into the L1.5 primitive** and *consumed* by `functioncadence.cpp`, never copied. One
   path per concern (#6).
2. **The pre-scan is a COARSER vote — precision loss must be measured, not assumed.** `functioncadence.h:54-74`
   documents the "key-agnostic limit": a plain V→I and a plain I→IV are exact transpositions, so a
   chord-free test cannot separate them. Its three mitigations survive relocation — the seventh/tritone
   strengthener (chord-free ✓), the phrase gate (chord-free ✓), the weak-soft-vote absorption (✓) — but
   the **PAC-vs-IAC distinction and the pre-dominant licensing do NOT** (both chord-dependent). So the L1.5
   vote is strictly weaker than the L5 detector's. **How much weaker is unmeasured.** The design opening's
   §4(2) cadence-vote coverage probe should be re-scoped to measure the **chord-free** predicate set, not
   the built L5 detector's.
3. **The ALTERNATIVE placement is already sanctioned and already built.** The **cadence-confirmed key
   modulation recompute** (`functionmodulation.cpp:143-154`, on `forwardoverride::OnePassClosure`) is
   named by `ARCHITECTURE.md` §2.14/§2.15 as one of the two forward-override instances. It **is** an
   upward L5→L3 fact edge — but a *ratified, bounded, one-pass, region-scoped, re-entrancy-guarded* one,
   which §2.15 explicitly admits ("a sanctioned backward edge … a deliberate, surfaced, measured,
   documented exception"). **The two are not exclusive:** the L1.5 pre-scan *informs the decode*; the L5
   override *corrects it after*. Decision 3(b) frames these as an either/or ("versus"); the audit finds
   they are complementary, and that only the *first* was ever in doubt.
4. **The ruling in `cowork_target_architecture.md` §2** ("key/mode … NOT chord symbols, functions, or
   cadence detection") forbids the L5-vote-into-decode route and points at the now-shelved joint step. The
   L1.5 pre-scan does **not** violate it (it is a bass/voice-leading evidence primitive below the chord
   layer, not "cadence detection" in the sense rejected). But the design pass must say so explicitly and
   amend the ruling's wording, or the two documents stay in contradiction. **OI-161.**

### 5.3 ★ THE KEY→CHORD EDGE (downward) and the collection/tonic split — THEORY → FACT, with a caveat

The split is **established at the code**, not merely measured:
- The rebuilt L4's key consumption is **two collection-membership terms** and nothing else; `decideSlice`
  takes no key; the decoder never runs the post-scoring gates, so **the one tonic-dependent scoring gate
  cannot fire in it** (§3.6).
- The collection is **provably** invariant across the 7 diatonic modes of a signature (§3.6), so the
  oracle cannot distinguish relative major from relative minor.
- Corroborated independently by corpus measurement: chord-flip-under-GT-key fires on **7 / 8 / 6 regions**
  (0.30–0.37 % of key-disagree regions) across all presets (`cc_mode_key_chord_probe_report.md` §0/§2;
  artifact `tools/reports/joint_probe_measure.json`).

**⇒ The pipeline `L3-collection → L4-chords → tonic-evidence → L3-tonic` is structurally available.** This
is the enabling fact for §5.2's proposal and for §8 circle 3. **FACT.**

**★ THE CAVEAT — two LIVE tonic-dependent sites, and one has no retirement row:**

| Site | Class | Retirement |
|---|---|---|
| **Gate G-E** (`postscoringgates.cpp:379-385`) — the ii/iii/vii **degree** test; firing swaps the winner to a HalfDiminished root, i.e. **changes the committed chord** | TONIC | Rides **R1** ("legacy chord competition + Gates A–L") — *G-E is a Gate-G sub-rule, so it is covered by the letter range; the design pass should confirm, since R1's text names gate letters, not sub-rules* |
| **`sparsechordrefinement.cpp:154-159`** — the Aeolian lone-tonic/dominant guard: a single sounding A under A-Aeolian stays `Unknown`; the same A under C-Ionian (identical collection) hardens to A-minor | TONIC + MODE | **★ OPEN.** `sparsechordrefinement`'s retirement is an unresolved question (OI-102 carries "the `sparsechordrefinement` L4/L5 boundary + retire question"); OI-90 re-tagged it L4. **If it survives the engagement, L4 is NOT tonic-independent and the collection/tonic split does not hold.** |

**⇒ The collection/tonic split is a FACT about the *rebuilt* L4 and a CONDITIONAL about the *engaged*
L4.** Its survival is gated on the disposition of `sparsechordrefinement`'s Aeolian guard. Filed
**OI-167** — a concrete, checkable gate the design pass must clear before the split can carry load (#18).

### 5.4 ★ THE NCT-CLEANED-TONES EDGE — the second STOP (no break)

The key layer wants NCT-cleaned tone collections as emission input (inventory §8; design Decision 2).

| Question | Answer |
|---|---|
| Fixed input? | No. |
| Key-agnostic form? | Irrelevant — NCT classification is already key-agnostic. |
| **Chord-agnostic form?** | **NO — by definition.** "Which sounding pitch is structural" *requires a chord hypothesis*. `ARCHITECTURE.md` §2.14 names it as an intrinsic circularity; the ratified resolution is that **L4 owns chord + NCT together** (one layer, one job). |

**⇒ There is no key-agnostic NCT. An L3 consuming NCT-cleaned tones is a genuine L3←L4 back-edge with no
break.** The §8 argument ("chords first, NCTs classified against them, with the forward-override for the
rare case") is correct *for the chord↔NCT circle* — but the key layer's consumption is a **different
edge**, and §8 does not address it.

**Proposed resolutions (one input among several; not decided here):**
- **(a) Drop it from the emission.** Note that the emission **already performs a weak, chord-free version
  of NCT-cleaning**: `PitchContext` carries `durationWeight` and `beatWeight`, so a brief off-beat passing
  tone already contributes less than a sustained downbeat tone. The marginal value of true NCT verdicts
  over duration×metric weighting is **unmeasured** — and measurable read-only. **Recommended first step.**
- **(b) Accept it only in second-pass / forward-override form** — an L3 re-decode on NCT-cleaned collections
  *after* L4, in the same sanctioned class as the cadence-confirmed override. Bounded, versioned, ratified.
- **(c) A chord-free NCT proxy at L1.5** — dissonance/voice-leading-based (the dormant `StepwiseSignals`,
  OI-72, is exactly this, currently trapped inside the decoder's membership internals).

### 5.5 ★ THE PROGRESSION-GRAMMAR EDGE — the break is sound, the named instrument is inert

| Question | Answer |
|---|---|
| Is the §8 "broken by enumeration" argument logically sound? | **Yes.** A key scored as a hypothesis index over a fixed chord sequence feeds nothing back. |
| Does the **as-built** instrument discriminate keys? | **NO — zero.** `isLicensedProgression(from, to)` takes only `ProgressionChord{rootPc, quality}` × 2 (`functionprogression.h:127-130, 212`); its body is pure root-interval arithmetic on `(to − from) mod 12` plus each chord's own quality (`functionprogression.cpp:125-143`). It is **transposition-invariant**, so it returns the **identical value under every candidate key**. The header says so: *"The licensing test needs only the root and quality; the degree-in-key … is derived separately"* (`functionprogression.h:124-126`). |
| Is the edge upward regardless? | **Yes** — scoring any progression grammar needs a chord sequence (L4). Same shape as §5.2. |

**⇒ The design opening's Decision 3(e) names the wrong asset.** It says "the assets exist dormant and
audited (the harmonic vocabulary catalog; the licensed-progression grammar)". Of those two, **only the
first can discriminate keys**: `harmonicvocabulary`'s entries are **degree-offset skeletons**
(`ChordDegreeStep::degreeOffset` = "semitones above the tonic", `harmonicvocabulary.h:197-200`) with the
tonic **supplied at query time** — so the same root sequence maps to different degree sequences under
different tonics, which is exactly the discrimination the channel needs. It is dormant with **no
consumer**.

**⇒ The §4(4) probe's written prediction can be settled at the code before it is run:**
`isLicensedProgression` will show **exactly zero** discrimination — that is provable, not measurable.
**Proposed: re-scope the probe to `harmonicvocabulary`.** (This does not weaken the design opening's
MEASURED CAUTION; it sharpens it.)

**Proposed owning layer:** unchanged — the grammar stays at L5/the Vocabulary. Its consumption by L3 takes
the **same two routes as §5.2**: a chord-free bass-motion grammar at L1.5 (much weaker), or the
forward-override.

---

## §6 — Task 5: the reconciled §8 map, and the STOPs

| # | §8 circle | §8's claimed break | **Verdict at the code** | Class |
|---|---|---|---|---|
| 1 | **key ↔ spelling** | "NOT CIRCULAR FOR US — spelling is INPUT" | ✅ **CONFIRMED.** `NoteEvent::tpc` (`note_model.h:82`). *Caveat: the L1→L3 channel does not exist — `PitchContext` has no `tpc` (OI-163). A build gap, not a cycle.* | THEORY → **FACT** |
| 2 | **key ↔ cadence** | "BROKEN BY THE KEY-AGNOSTIC FORM … what remains is plumbing" | ⚠ **HALF-TRUE — THE STOP.** Key-agnosticism: **FACT**. Layer-forwardness: **REFUTED** — the tonic is read off the L4 committed root (`functioncadence.cpp:229`). It is **not plumbing; it is a missing unit** (the dossier's pre-scan, never built). **A break IS realizable at L1.5** (§5.2). | **STOP** → OI-166 |
| 3 | **key ↔ chord** | "MOSTLY DISSOLVED BY THE COLLECTION/TONIC SPLIT" | ✅ **CONFIRMED AND STRENGTHENED.** The rebuilt L4 is tonic-independent **by construction** (§3.6), not merely by measurement. **Conditional:** two live tonic-dependent sites; one (`sparsechordrefinement`'s Aeolian guard) has **no retirement decision** (OI-167). | THEORY → **FACT** (conditional) |
| 4 | **chord ↔ non-chord-tone** | "SAME SHAPE, SAME BREAK — provisional-then-refine" | ✅ **CONFIRMED as an intra-L4 concern** (L4 owns chord + NCT together). ⚠ **BUT the key layer's wish to consume NCT-cleaned tones is a DIFFERENT, un-addressed edge with NO break** (§5.4). | **FACT** + a **second STOP** |
| 5 | **key ↔ progression-grammar** | "BROKEN BY ENUMERATION — the key is a hypothesis index" | ⚠ **SOUND IN LOGIC, VACUOUS AS BUILT.** `isLicensedProgression` is transposition-invariant ⇒ **zero** key information (§5.5). The right asset (`harmonicvocabulary`) is dormant and unnamed in the design. | THEORY (sound) + **instrument refuted** |

### 6.6 The circles §8 did NOT enumerate

| # | Circle | Source | Verdict |
|---|---|---|---|
| **6a** | **segmentation ↔ chord** | **`ARCHITECTURE.md` §2.14 bullet 2** — omitted from §8 | **LIVE AND REAL** in the legacy path (8 sites, §4.1 C1–C6). §2.14's `ScoringPhase::Segmentation` mitigation is **partial** — `analysistypes.h:68-69`: *"rootContinuityBonus stays active (segmentation depends on it)"*, and the chord score/root/quality still flow. **BROKEN IN THE TARGET by construction:** the rebuilt L2 `Slice` carries `{start, end}` and nothing else (`slicer.h:84-87`); `slicer.cpp` includes only `<algorithm>`. Retires **R6**. |
| **6b** | **note-view ↔ chord** (`findTemporalContext`) | **NEITHER §8 NOR §2.14** — new | **LIVE.** A Layer-1.5 primitive instantiates a chord analyzer and runs full `analyzeChord` at `ScoringPhase::Final` — *all* progression signals active (`regiontoneprimitives.cpp:451-592`, live at `regionanalyzer.cpp:918-919`). It also consumes L3 (`keyFifths`, `keyMode`). **NOT on the retirement map**; tracked only as OI-12 ("ownership move"), which does not name it as a cycle. **OI-165.** |
| **6c** | **functional role ↔ chord identity** | **`ARCHITECTURE.md` §2.14 bullet 4** — omitted from §8 | **BROKEN — sanctioned.** The fine-grain chord forward-override (`functionresolver.cpp:468, 490-497`) on `forwardoverride::OnePassClosure` — at-most-once per decision id, re-entrancy-guarded, forward sweep only. An admitted L5→L4 backward edge under §2.15's exception clause. Dormant. |

### 6.7 The honest summary

> **The fact graph is acyclic on the rebuilt spine, has three live cycles in the legacy path (all but one
> covered by a retirement), and carries ONE ratified backward-edge class (the confidence-weighted
> forward-override, two named instances). Of the four facts the key layer intends to consume from above it,
> ONE (the cadence vote) has a realizable forward break at a lower layer than anyone proposed, ONE (NCT-cleaned
> tones) has NO break and needs a design decision, ONE (progression grammar) has a sound break but a refuted
> instrument, and ONE (the chord margin) rides on whichever way NCT is decided.**

---

## §7 — Proposed register rows (filed in this commit, per the standing rule (c))

New rows only; **no existing row's scope was touched.** Detail lives here; the rows are pointers.

| ID | Item |
|---|---|
| **OI-161** | The **ratified-position contradiction**: `cowork_target_architecture.md` §2 rules that L3 "needs … NOT chord symbols, functions, or **cadence detection**" (the 2026-06-21 correction, user-ratified), and points cadence-based key refinement at the **gated Stage-5 joint step** — which is now **shelved** (OI-43/OI-44). `cowork_key_layer_design_opening.md` Decision 3(b) proposes exactly the rejected thing. Needs an explicit resolution + a wording amendment at the design pass. |
| **OI-162** | **The phrase-boundary punctuation cues are BUILT, not unread.** `phraseboundaryview.cpp` reads fermatas (`:113`), breath/caesura (`:120-123`), mid-score key change (`:137-142`), DOUBLE/END barlines (`:163-165`), ritardando (`:183-189`), long rests (`:200`) — gated off behind `jointKeyWiringEnabled()`. `cowork_evidence_inventory.md` §1 statuses several of these as UNDISCUSSED/unread. Correction owed (OI-146(a)). |
| **OI-163** | **No spelling channel into the L3 emission.** `PitchContext` (`analysistypes.h:930-935`) = `{pitch, durationWeight, beatWeight, isBass}` — **no `tpc`**. Design Decision 2(a) (spelling-aware profiles) has no input path. Strictly forward; a build item at the key layer. |
| **OI-164** | **L5→L6 seam gaps:** (a) no code edge `functionoutput` → `groupinglayer` (the mapping exists only as a comment, `groupinglayer.h:41-47`); (b) `GroupingUnit::keyConfidence` (`groupinglayer.h:106-109`) has **no producer** — `FunctionConfidence` has no key-confidence field. A dangling consumer input. |
| **OI-165** | **`findTemporalContext` — an L1.5→L4 live fact cycle with no retirement row.** `regiontoneprimitives.cpp:451-592` instantiates a chord analyzer and runs full `analyzeChord` at `ScoringPhase::Final` (all progression signals active) from a Layer-1.5 note-view primitive; live at `regionanalyzer.cpp:918-919`. Also consumes L3. The §2.14 `ScoringPhase::Segmentation` mitigation does **not** cover it. Currently tracked only as OI-12 ("ownership move"), which does not name the cycle. |
| **OI-166** | **★ THE CADENCE PRE-SCAN IS NOT BUILT.** `functioncadence.cpp` is key-agnostic (FACT) but **chord-derived** — the tonic is read off the L4 committed root (`:229, :301, :358, :409, :450`). The June dossier specified a **bass-driven, chord-free, tonic-enumerating** pre-scan running *before* `analyzeKeyMode` (`cc_cadence_key_investigation_dossier.md:203-209`). Different unit; never built. The design opening's §1 identification is REFUTED, and its §5 uncertainty flag is discharged **negatively**. A forward break IS realizable at L1.5 (report §5.2). |
| **OI-167** | **The collection/tonic split's survival is CONDITIONAL on `sparsechordrefinement`.** The rebuilt L4 is tonic-independent by construction, but two **live** tonic-dependent sites exist: Gate G-E (`postscoringgates.cpp:379-385`, rides R1 — confirm) and the Aeolian lone-tonic/dominant guard (`sparsechordrefinement.cpp:154-159`), whose retirement is **undecided** (OI-102). If the guard survives the engagement, the split does not hold and every design resting on it loses its premise (#18). |

**Also declared to Cowork (an inference problem, NOT fixed here — per the standing instruction):**
`chordanalyzer.cpp:1341` `DIATONIC_PARENT_INDEX[13] = 0` (Ionian, `keyModeTonicOffset` 0) vs
`keyModeTonicOffset(Altered) = 1`; `[20] = 4` (Mixolydian, offset 7) vs `keyModeTonicOffset(AlteredDomBB7) = 8`.
For those two modes the constructed diatonic collection is the signature collection **transposed up a
semitone**. Live-reachability not traced. This is an inference-correctness question, not an
architecture/refactoring one, so it is **declared, not investigated and not fixed** — Cowork's to route.
It does **not** affect the TONIC-vs-COLLECTION classification either way.

**Doc-precision item found in passing (#10, no code effect):** `regionanalyzer.h:36` claims the canonical
behavior includes "`absorbShortRegions` with the Iter 78 Fix A `sharesPrevRoot` guard". `absorbShortRegions`
(`regionanalyzer.cpp:239-256`) has **no root check** — it is purely duration-based; the root-aware behavior
now lives in the separate `coalesceShortSameRootRuns`. Folded into OI-165's row as a companion note rather
than given its own number (same file family, same touch).

---

## §8 — What this audit does NOT establish

Stated so nothing here is put under load it cannot carry (#19).

1. **It does not measure anything.** Every claim is either a code citation or a citation of an existing,
   established measurement. The precision cost of relocating the cadence primitive to L1.5 (§5.2
   trade-off 2) is **unmeasured** and must be probed before any build.
2. **It does not certify the legacy path's edge list as exhaustive.** The rebuilt spine's acyclicity is
   proven by include-closure (a strong, mechanical argument). The legacy path's 13 edges were found by
   directed search, not by an exhaustive sweep — there may be more. They all retire, so the risk is bounded,
   but "13" is a floor, not a ceiling.
3. **It does not decide any layer placement.** §5's proposed owning layers are ONE candidate input to the
   design pass, with their trade-offs named. The user and the design pass ratify.
4. **It does not re-open OI-43/OI-44.** The shelved joint step stays shelved; nothing here revives it. The
   `jointkeydecision` module appears in the graph only as a gated-off, dormant edge.
5. **The `harmonicvocabulary` key-discrimination claim (§5.5) is STRUCTURAL, not measured.** Degree-offset
   entries *can* discriminate keys; whether they *do*, on our corpus, on the measured failing classes, is
   exactly what the re-scoped §4(4) probe would answer.

---

*Cross-references: `cc_instruction_fact_dependency_audit.md` (the dispatch); `ARCHITECTURE.md` §2.14/§2.15/§3.3;
`cowork_target_architecture.md` §2 (the ratified layer table + the 2026-06-21 cadence ruling);
`cowork_evidence_inventory.md` §8 (the map under test); `cowork_key_layer_design_opening.md` (the design this feeds);
`cc_cadence_key_investigation_dossier.md` §203-209 (the pre-scan spec); `cc_mode_key_chord_probe_report.md`
(the key-invariance measurement); `docs/implementation_roadmap.md:138-145` (the retirement map R1–R10);
OI-12, OI-43/OI-44, OI-72/73/74, OI-75/OI-81, OI-86, OI-90, OI-92/OI-93, OI-94, OI-102, OI-117, OI-118/OI-119,
OI-146; new rows OI-161…OI-167.*
