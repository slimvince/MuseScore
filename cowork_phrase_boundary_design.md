# Phrase-boundary primitive (Architectural Layer 1.5) — Architecture & Design

> **Status: SIGNED (user, 2026-06-26) — build in progress (`cc_instruction_phrase_boundary_build.md`).** rev. 3 — graded
> + per-voice/aggregate. Rev. 3 (user,
> 2026-06-26) makes the cues run **per eligible voice, aggregated to the texture** (so the primitive yields *both*
> per-voice and texture-level boundaries, and the pitch cue uses every voice, not just the top), and adds **breath marks
> and caesuras** as deterministic markers; the rev-3 changes were independently re-reviewed (1 blocking + 1 cosmetic fix
> applied — a leftover top-voice reference and a vocabulary slip). The prior rev. 2 was audited against the design-doc
> standards of `cowork_design_doc_template.md` (the section structure and the two writing standards) plus the
> language-mechanical sweeps (`cowork_spec_language_sweep.md`, `cowork_layer3_spec_language_sweep.md`) by an independent pass; 6 blocking + 4 cosmetic fixes applied (the local-change
> strength formula made two-sided and complete; max-normalisation, the voice-coincidence window, and the whole-profile
> peak threshold pinned; the silence/sustained-note cues separated; the marker-spike ordering made decidable). The
> acyclicity argument (surface-only, no harmony) was verified airtight. A proper-layer design for the **phrase-boundary**
> primitive, the first of the three earlier-layer input prerequisites the signed function-layer spec (§15-0) surfaced.
> **Revision 2** replaces the rev.-1 binary-union model with a **graded boundary-strength model**, on the research in
> `cowork_phrase_boundary_methods.md` (user-ratified 2026-06-26: the leading harmony-free segmentation models compute a
> continuous boundary strength and pick peaks; a binary union is a degenerate, lower-precision special case). Written to
> the design-doc standard: every rule is stated (constants deferred to the precision phase are allowed; unstated
> *mechanisms* are not), the body (§1–§9) is code-free (mechanisms named by role; the as-built map is in §10), and it uses
> standard music / music-cognition vocabulary (glossed in §9). Scope: this one primitive — *not* the cadence or function
> logic that consumes it.

> **Bounded-context stance (added 2026-07-02, closing gap-analysis v2 finding A-2, `cc_gap_analysis_v2_report.md` —
> ruled by Cowork):** this primitive is a
> **derived view** over the Layer-1/Layer-2 outputs: it **inherits the loaded span and requests no extension of its
> own** (its profile simply ends where the loaded span ends; a consumer wanting boundary evidence beyond the loaded
> span extends via ITS own bounded-context obligation, and this primitive recomputes over the enlarged span — the
> standard re-run, per `cowork_bounded_context_design.md` §4). Its published boundary strength is a **Class-M
> boundary confidence** under the cross-layer confidence contract (`cowork_confidence_contract.md`: [0,1] per-profile
> max-normalised salience, comparable within one score's profile only; it participates in no override frame) —
> closing gap A-3 of the same v2 report for this spec.

## 0. Terms (read first — nothing below uses a term before its row)
*Per the template standard (`cowork_design_doc_template.md`, defined-terms rule). The §9 glossary carries the fuller
definitions of this primitive's own vocabulary; this table is the entry point and the load-bearing rows.*

| Term | Meaning (or citation) |
|---|---|
| **Tick** | The absolute time-position in the score (the engraving time unit). The sibling layer docs say "time-position" — one thing, two project words; this document uses "tick" throughout. |
| **Eligible voice** | A (staff, voice) line whose notes pass the eligibility test — verified at the as-built source: the note **sounds** (is not muted/silent), is **visible**, and lies on a **staff that takes part in tonal analysis** (Layer 1's staff-eligibility flag). Muted and invisible notes are **excluded** from every per-voice cue profile. "Eligible" everywhere below means exactly this three-flag test; Layer 1 defines the staff flag, this row states the voice-level combination Layer 1 does not. |
| **Phrase boundary / boundary tick** | A tick where the surface marks a phrase end (§1). Under the span typology (ARCHITECTURE.md §2.15) this primitive's picked boundary is the **cue that delimits Layer 6's punctuation-span** — the primitive keeps its "phrase-boundary" code name; the grouping *span* it delimits is the punctuation-span, and "phrase [MT]" is reserved for the melodic voice-leading object this primitive does not model. |
| **Boundary-strength profile** | The graded per-onset measure of §4 (per-voice, and aggregated to the texture). Its published form is a **Class-M boundary confidence** under `cowork_confidence_contract.md`. |
| **The cadence gate** | The function layer's rule admitting a cadence candidate only at a phrase boundary (`cowork_layer5_function_design.md` §5.2/§11) — this primitive's main consumer. |
| **Precision-phase constants ("the firewall")** | Numeric values deferred to the project's later tuning phase (Phase B of `cowork_l1l3_stabilization_plan.md`); the mechanism/constant split is the project's inference firewall. This document fixes mechanisms; the named constants are tuned there. |
| **The corpus two-tier gate / both presets** | The project's two-tier **BIR (bass-is-root)** corpus regression gate, run on the Baroque and Jazz tuning presets (gate policy: CLAUDE.md). |
| **Pinned** | Fixed by ratified decision and protected by a regression test (project usage); **pinned snapshots** are stored golden outputs compared exactly. |

## 1. Purpose
A **phrase boundary** is a tick where a musical phrase **ends** (the next phrase begins at the following sounding onset,
which this primitive does not separately mark). This primitive computes, from the notated surface alone, a **graded
boundary-strength profile** over the score — a per-onset measure of how strongly the surface evidence marks a phrase end
— and from it the **picked boundary ticks** and the derived per-region flag **"this region ends a phrase."** It exists
because the layers above — the function layer's cadence detection (which admits a cadence candidate only at a phrase
boundary) and its salience weighting — need phrase boundaries, and their **strength**, as an **input**, and the function
layer must not define its own inputs. It emits a *graded strength*, not only a yes/no, so a consumer can read the
confidence of a boundary, not just its presence. The strength is computed **per voice and aggregated to the whole
texture** (§4.3), so the primitive yields **both** each voice's own phrasing and the texture-level phrase boundaries the
cadence gate consumes. It replaces today's scattered, duplicated, fermata-only computation with
one owned primitive that works for **any instrumentation**, not only chorales. *(Typology role, §0: the picked
boundary is the delimiting cue of Layer 6's **punctuation-span**; "phrase [MT]" — the melodic phrase — is a
voice-leading-axis object this primitive does not model. Stated here at the definition, not only in §11-5.)*

## 2. Constraints
- **Notation-only — key-, chord-, and function-agnostic.** A phrase boundary is read from the written surface (rests,
  durations, pitch intervals, metric position, annotations, barlines), never from a resolved key, a chord reading, or a
  cadence. This is structural: the function layer's cadence detection *consumes* phrase boundaries, so a boundary that
  depended on cadence would be circular. Cadence-based phrase refinement therefore stays a **function-layer** concern,
  downstream of this primitive (§6-D3). A known consequence (accepted): a surface-only primitive **systematically misses
  boundaries marked only harmonically** — a cadence with no surface gap — which the function layer recovers downstream.
- **General, not chorale-specific.** The tool analyses scores of any instrumentation. The fermata is the reliable phrase
  marker *in chorales* but is not universal; the surface-cue model and the other notated markers extend the primitive to
  any texture.
- **Graded model with deferred constants (the firewall, §0).** The primitive is a small notation-only inference, not a pure
  deterministic fact. Its two parts have different character, stated honestly: the **notated markers** (fermata, structural
  barline, all-voice rest) are **deterministic facts**; the **surface-cue boundary strength** is a **computed profile**
  whose combination weights and peak threshold are **precision-phase constants**. This document fixes the **mechanism**
  (which cues, how combined, how peaks are picked); the constants are tuned later. No key/chord/function ever enters.
- **One owner, no duplication.** Exactly one implementation, consumed everywhere; the de-duplication step retires the two
  hand-synced copies that exist today into it.
- **The marker-only path is byte-identical; the graded model is gated.** Retiring the duplicated fermata scans into one
  primitive changes no output. Adding the surface-cue strength and the new notated markers *may* change which ticks are
  boundaries; that change is measured against the corpus two-tier BIR gate on both presets (§0) before it lands (§7).
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

## 3. Context & scope (external view)
**Consumes** (all notation, defined in earlier layers): from Layer 1, the note model — each note's **voice, pitch, onset,
and duration** (a note's **offset** = onset + duration), and the **eligible** voices that take part in analysis; the score's **annotations** (fermatas), **rests**,
and **barlines** as read from the engraved notation; the **breath marks** and **caesuras**; the **tempo markings**
(sudden/subito tempo changes and written ritardandos); and **mid-score key-signature changes** (the *engraved signature
event*, not the inferred key). From Layer 2, the **empty slices** (maximal spans where every eligible voice rests) — the substrate of the all-voice-rest marker and the aggregation
limiting case. *(The pitch-interval cue runs per voice on each voice's own line — §4.3 — so this primitive does not
consume any top-voice primitive. The top voice is at most an *optional* soft cue for the function layer's cadence test —
not a prerequisite (the highest voice is not reliably the melody) and not used here; see the function-layer spec,
`cowork_layer5_function_design.md`.)*

**Produces:** the **per-voice boundary-strength profiles** (one per eligible voice); the **texture boundary-strength
profile** (their per-onset aggregate); the **picked boundary ticks** (the peaks of the texture profile, selected per §4.4);
and the derived **"ends a phrase"** flag for a region (true when a picked boundary tick falls within the region). All are
notation facts carrying no judgement of key, chord, or function.

**Does not do:** detect cadences, weight cadential salience, or read any resolved key/chord/function (all downstream);
apply phrase *grouping* or reduction (a later concern). It marks where phrases end, and how strongly.

## 4. The model (the rules)
The boundary-strength profile is built from a **surface-cue core** plus **deterministic notated-marker spikes**, then
**peaks are picked**. Each part is a stated mechanism; the named numeric constants are precision-phase.

### 4.1 The surface-cue core (a local-change boundary-strength model)
Three independent **cue profiles** are computed over the score, each yielding a per-onset strength:
- the **gap profile** — the offset-to-onset interval (the silence/separation) between successive events;
- the **inter-onset profile** — the time between successive attacks;
- the **pitch-interval profile** — the absolute interval (in semitones) between successive notes **of a single voice's
  line** (computed per voice — see §4.3).

Each profile's per-onset strength is computed by the standard **local-change rule** — the boundary-strength
formulation of Cambouropoulos's **Local Boundary Detection Model (LBDM)** family, per the methods catalog
(`cowork_phrase_boundary_methods.md`): for a value `x` at a point with left neighbour `x_prev` and right neighbour `x_next`, define
the two **change-ratios** — left `= |x_prev − x| / (x_prev + x)` and right `= |x − x_next| / (x + x_next)` — and the
per-point strength is `x · (left + right)`. So the strength rises with **both** (a) the **degree of local change** (the
value differing from its neighbours, captured by the change-ratios) **and** (b) the **size** of the value itself (the
leading `x` — a large gap is a stronger boundary than a small one, even where both are local changes). Each of the three
profiles is then **normalised by dividing by its own per-score maximum** (max-normalisation), placing all three on a
common [0,1] scale so they are comparable.

The **combined surface strength** at a point is the **weighted sum** of the three normalised profiles, with the **gap
profile weighted highest** (the gap/rest is by far the most precise surface cue — the methods-catalog ranking,
`cowork_phrase_boundary_methods.md`; the inter-onset next; the pitch-interval least). The three weights are **precision-phase constants**; the mechanism (a normalised, gap-dominant weighted sum of
the three local-change profiles) is fixed here.

### 4.2 The deterministic notated-marker spikes
The following are **deterministic, high-precision notated boundary signals**; each contributes — **after** the surface-cue
core (§4.1) is combined and normalised — a **fixed additive spike to the combined profile at its tick, of a magnitude set
above the maximum possible surface-cue strength** (the theoretical maximum — the number of eligible voices multiplied
by the sum of the three cue weights, since every voice's every cue could peak at once; the spike default is
**1.5× that**, a precision-phase constant — strictly above, so a *coincident* surface peak that reaches the max does not
merely tie it), so the marker **exceeds any surface-cue peak** and dominates wherever it occurs:
- a **fermata** on an eligible voice;
- a **breath mark** (the comma phrasing symbol) or a **caesura** (the "grand pause" / railroad-tracks symbol) on an
  eligible voice — explicit composer-notated phrase / break signals, the same kind of high-precision channel as the
  fermata;
- a **double, final, or repeat barline** (a structural division — treated, for this primitive, as a phrase boundary);
- a **mid-score key-signature change** — read as the **engraved signature event** (a new set of accidentals written on
  the staff), a notational structural-boundary marker, **NOT the inferred key** (so it adds no key/harmony dependency and
  no cycle with the downstream key layer — the written signature is notation, not the key it implies). Composers
  re-notate the signature at major section / key-area seams, so it is a very sparse, section-level, high-precision marker;
- a **sudden (subito) tempo change** — a new tempo marking reached with **no gradual transition** (a structural
  section/phrase boundary, spiked at the change), or a **written ritardando / rallentando** — a notated slowing into an
  arrival (spiked at the arrival it leads to). *(A **sparse** cue: absent from many scores — e.g. unmarked chorales — and
  it marks section seams more than every phrase, so it adds precision where present and is harmless where absent. Limited
  to **sudden/notated** tempo changes; expressive mid-phrase rubato is not a boundary.)*
- the **onset of a maximal all-voice-rest span** — a span in which every eligible voice rests, that cannot be extended in
  either direction without an eligible voice sounding (a Layer-2 empty slice), whose duration is at least a precision-phase
  **minimum-silence constant**.

### 4.3 Per-voice cues, aggregated to the texture (polyphony)
The local-change cues (§4.1) are defined over a single melodic line, so they are computed **per eligible voice** — each
voice gets its own **gap, inter-onset, and pitch-interval** profiles over that voice's own note sequence. So the
**pitch-interval cue applies to every voice**, not only the top one, and the gap/inter-onset cues read each voice's own
rests and lengthenings.

The per-voice strengths are then **aggregated, per onset, into a texture boundary-strength**: the texture strength at an
onset is the **sum of the per-voice strengths at that onset** — so a point where **many voices phrase together**
(coincident rests, leaps, or lengthenings) scores high, because more voices contribute more terms, while a boundary in a
single inner voice scores low. The whole-texture all-voice rest is the **limiting case** where every voice's gap profile
peaks at once. Because voice onsets do not always align exactly, two voices' events are merged into the **same onset**
for the sum when they fall within a **coincidence window `τ`** (a precision-phase constant absorbing notational
near-alignment — in the chorale convention all voices reach the phrase-final note together, the easy case). The mechanism
— per-voice profiles summed per (τ-merged) onset — is fixed here; `τ` and an **optional explicit coincidence weight**
(boosting onsets where several voices peak at once beyond the plain sum) are precision-phase constants.

The primitive **exposes both**: the **per-voice boundary strengths** (each voice's own phrasing) and the **texture
boundary strength** (the aggregate). The peak-picking (§4.4) that feeds the function layer's cadence gate runs on the
**texture** profile; the per-voice strengths are available for any consumer that wants per-line phrasing. (The deterministic
markers of §4.2 spike the **texture** profile.)

### 4.4 Peak-picking
The picked-boundary set is **the surface-cue peaks UNION every notated marker** — because the §4.2 markers are
**deterministic facts** (a fermata/barline/etc. *is* a phrase boundary), they are emitted **unconditionally**, not
subjected to the threshold; only the **surface-cue** strength is peak-picked. *(As-built realisation, ratified 2026-06-26:
the earlier wording "peak-pick the combined profile" put the markers through the local-maximum test, which a strict
greater-than rule drops for two **adjacent equal-height markers** — e.g. a final fermata abutting the closing barline.
Emitting markers directly is the faithful reading of their "deterministic / dominate wherever they occur" status.)*
**Surface peak-picking:** a surface tick is picked when its texture combined strength (§4.3) is **both** a **local
maximum** (greater than its two immediate onset-neighbours) **and** above an **adaptive threshold** — the **mean of the
whole score's texture combined strength profile plus `k` standard deviations** (the "Simple Picker" of the methods
catalog, `cowork_phrase_boundary_methods.md`; whole profile, not a sliding window; `k` precision-phase). (The marker spikes still sit at/above any surface peak in the
exposed strength profile, so a downstream consumer reading the strength sees them dominate; the *picking* just no longer
gates them.) The **boundary tick** of a picked peak is the onset at which the phrase's sounding ends: the fermata or
last-sounding note's tick, the structural-barline tick, or the onset of the all-voice-rest span. A region **ends a
phrase** when a picked boundary tick falls within its half-open tick span. (Because the final tick of the score carries an end-of-piece
boundary — the score's last barline — the last region ends a phrase automatically; no separate last-region rule is
needed.)

**★ EVERY PICKED BOUNDARY CARRIES WHICH CUE OR MARKER FIRED, AND AT WHAT SCOPE — A REQUIREMENT ON THIS SECTION'S OUTPUT,
STATED AS OWED AND EXPLICITLY NOT BUILT.** A picked boundary — texture **and** per-voice — carries its **provenance**:
which cue or marker produced it, and whether it fired **globally** or **per voice** (and if per voice, which voices, and
how many coincided). **The picked set is SCOPE-BLIND today**, which is the defect this requirement names: a marker
written on one voice — a breath mark — is spiked onto the texture profile and thereafter reads exactly like a marker
that applies to the whole ensemble, so a downstream consumer (the punctuation-span annotation) cannot tell a **local
breath** from a **global barline**. *Why it is a requirement rather than a preference:* dropping the scope is
information loss (#12), and the principled form is already in this section — a per-voice marker should reach the texture
profile through the **same voice-coincidence aggregation** the graded cues use (§4.3), not by being spiked onto it.
*What is deliberately NOT claimed:* that this changes anything on the gate repertoire. It is **chorale-inert by
construction** — in the chorale convention every voice holds together, so global and per-voice coincide — and it matters
for orchestral and contrapuntal textures, where it is to be validated (§8). **It is NOT BUILT**, by the standing rule
that a proper-layer refinement waits for the inference phase to open; §11 carries it as an open item and this is the
requirement that item binds a future build to.

### 4.5 Explicitly excluded
**Not** a boundary signal here: **cadential closure** (a dominant-to-tonic arrival), harmonic-rhythm change, and any
**inferred key change** (the modulation a later layer detects). They are musically real phrase signals but are
*function/key-layer* judgements that consume this primitive; including them would make the primitive depend on a layer
that depends on it (§2, §6-D3). **This is distinct from the admissible §4.2 marker: a written *key-signature change* is a
notational event read off the staff (notation **in**); the *inferred key* and its changes are **out**.** **Deferred** (named, not built): the
**global regularisers** — a phrase-length prior and metric-parallelism bias (they raise accuracy but add a corpus-specific
constant and a whole-score optimisation pass), and the **information-content / surprisal** cue (it matches rule systems
but needs a trained statistical model). Both are §11 open items, not part of the first build.

## 5. Runtime view (scenarios)
- **A chorale phrase end.** All voices reach a fermata note together: the all-voice-rest/long-note gives a strong gap-
  profile peak *and* the fermata marker spikes — a high-strength picked boundary.
- **An instrumental phrase ended by a rest.** All eligible voices rest for a bar between phrases with no fermata: the
  all-voice-rest marker spikes and the gap profile peaks — a boundary, even absent a fermata.
- **A phrase end marked by lengthening, no rest.** The melody reaches a long note among shorter ones with no silence: the
  inter-onset profile peaks at the long note (agogic lengthening) — a moderate-strength boundary the binary-union model
  would have missed.
- **A section break.** A double barline spikes the profile — a boundary.
- **A passing leap (non-boundary).** A single large melodic leap mid-phrase raises only the (low-weighted, noisy) pitch-
  interval profile and does not clear the adaptive threshold alone — no boundary. (This is why the model is gap-dominant
  and threshold-gated, not an OR of cues.)
- **One voice phrases while the others continue (per-voice, not texture).** In a contrapuntal texture a single voice
  rests or leaps at a phrase end while the others play on: that voice's per-voice strength peaks, but the texture
  aggregate stays low (no coincidence) — a per-voice boundary is reported, the texture boundary is not. The cadence gate,
  reading the texture profile, correctly sees no whole-texture phrase end there.
- **A purely harmonic cadence with no surface gap (a miss, by design).** No surface cue fires; the primitive emits no
  boundary there. The function layer recovers it from the cadence downstream (§2).

## 6. Architecture decisions (with the alternatives weighed)
- **D1 — Owner: Architectural Layer 1.5 (the notation-derived views).** The primitive is a notation-derived view, the same
  kind as the bass, top-voice, and spelling views, reading the same notated surface. *Rejected:* the Layer-1 note model
  (deliberately narrow — it records notes, it does not derive phrase structure) and the function layer (it consumes phrase
  boundaries; it cannot own them).
- **D2 — One unified primitive replaces the two duplicated fermata scans.** The fermata logic exists today in two
  hand-synchronised copies; they are retired into the single owned primitive and every consumer re-points at it. The
  retirement is byte-identical.
- **D3 — Notation-only; cadential closure stays in the function layer.** To keep the dependency acyclic (cadence consumes
  phrase boundaries), the primitive reads only the surface, never cadence/function. A function-level phrase refinement, if
  wanted, is a downstream combination in the function layer, not part of this primitive.
- **D4 — A graded boundary-strength model, not a binary union (user-ratified 2026-06-26).** The boundary is a peak in a
  continuous strength profile, not the OR of a few binary signals. *Rejected:* the binary union — a degenerate special
  case that cannot express "a gap larger than its neighbours," inflates recall, and wrecks precision (per the research: a
  weighted combination measurably beats any single cue and beats a naive union; the leading harmony-free models all
  compute graded strength + peaks). The cost — per-cue normalisation, the weight vector, the peak threshold — is modest
  and the constants are precision-phase.
- **D5 — Per-voice cues aggregated to the texture (both per-voice and polyphonic), not a top-voice/whole-texture
  reduction.** The cues run **per eligible voice** and aggregate by **voice-coincidence** into the texture strength,
  exposing **both** the per-voice boundaries and the texture boundaries (§4.3). *Rejected:* (a) a whole-texture reduction
  with **top-voice-only pitch** — it discards every inner voice's pitch cue and yields no per-voice phrasing; (b) running
  the cues on one arbitrary voice — ill-defined in polyphony. Per-voice-then-aggregate is the principled form (the
  local-change cues are defined per line) and produces both outputs. Since the literature's cues are validated only
  monophonically, the aggregation is validated on our own corpus (§7).
- **D6 — Generalise beyond the fermata.** The fermata alone is chorale-specific; the surface-cue model + the rest/barline
  markers extend the primitive to any instrumentation. *Rejected:* keeping it fermata-only (leaves the whole tool
  chorale-scoped — contrary to its purpose).

## 7. Quality & testing
- **Oracle tests** of the cues and the picking, on constructed cases: a rest yields a high-strength peak; a long note
  among short ones yields an inter-onset peak; a fermata and a double/final/repeat barline yield marker spikes; a single
  mid-phrase leap does **not** clear the threshold alone; a region containing a picked boundary reports "ends a phrase."
- **Validation on the chorale corpus** (the per-voice aggregation, D5) — the picked texture boundaries are checked
  against the corpus's **analyst-annotated phrase markers** (the DCML corpora's `{}` / `phraseend` annotations, parsed
  corpus-wide since the TSV-oracle infrastructure landed) — an **independent** ground truth: the markers are supplied
  by the human analyst, not derived from fermatas, so validating the fermata marker against them is not circular. A
  fermata-derived phrase list would be inadmissible as ground truth here, for exactly that circularity. A per-voice
  case (one voice phrasing while others continue) is checked to score a per-voice boundary but a low *texture* strength.
- **The de-duplication step is gated byte-identical** (corpus and suites unchanged — it only unifies existing logic).
- **The graded-model step is measured against the corpus two-tier gate on both presets.** A caveat to verify at build: the
  existing "ends a phrase" consumers may all be dormant/gated, in which case the new strength is byte-identical on
  production *today* and becomes load-bearing only when the function layer engages; the build enumerates the live consumers
  before treating the change as output-moving (§11-2, blocking).

## 8. Risks & technical debt
- **Polyphony is the weakest-supported area** — the cues are validated monophonically; the per-voice aggregation (D5) is
  engineering on top, and must be validated on our corpus, not assumed.
- **A surface-only primitive misses purely-harmonic boundaries** — accepted by design (§2); the function layer recovers
  them. So this primitive should not be expected to reach the accuracy of systems that exploit tonal structure.
- **The weights and the peak threshold are precision-phase constants** — until tuned, the build leaves them at stated
  defaults (gap-dominant weights; a peak threshold of mean + k·SD). The mechanism, not the tuning, is what this doc fixes.
- **The primitive is a small inference, not a pure fact** — a deliberate character change (§2); the notated markers stay
  deterministic, the surface strength does not.
- **Output movement at the graded step** must clear the gate (or be shown byte-identical via dormant consumers, §11-2).
- **★ Proportionality (scope discipline, user-ratified 2026-06-26).** The state-of-the-art-competitive reference
  engine (Contrapunctus) does **no** explicit phrase segmentation or cadence detection and is still competitive at Roman-numeral
  analysis (it captures phrase structure implicitly via stable key runs). So this primitive is **not** an accuracy
  requirement — it is load-bearing for *our* cadence mechanism (a means to key/function), a deliberate bet for an
  explainable, decomposed pipeline. **Build the graded model right, but keep it proportionate — do not let it balloon.**
  If the explicit phrase/cadence path proves hard, there is a proven implicit fallback (phrase-alignment via stable key
  runs). See `contrapunctus_findings.md` addendum and `cowork_phrase_boundary_methods.md`.

## 9. Glossary
- **Phrase boundary** — a tick marking where a phrase **ends**, picked as a peak of the boundary-strength profile; the
  next phrase's start is not separately marked.
- **Per-voice boundary-strength profile** — for one eligible voice, the weighted combination of that voice's three cue
  profiles; a per-onset measure of how strongly the surface marks a phrase end in that voice (§4.3).
- **Texture boundary-strength profile** — the per-onset **sum** of the per-voice profiles (over τ-merged onsets), plus the
  §4.2 marker spikes; the profile the cadence gate consumes and that peak-picking runs on (§4.3, §4.4). Coincidence raises
  it because more voices add more terms; an explicit coincidence weight beyond the plain sum is an optional precision-phase
  constant.
- **Voice-coincidence** — multiple voices contributing boundary strength at the same (τ-merged) onset; the plain sum
  already scores such a point high, so a point where many voices phrase together stands out.
- **Cue profile** — one of the three per-onset strength series (gap, inter-onset, pitch-interval) of a single voice, each
  from the local-change rule.
- **Local-change rule** — the per-profile strength `x · (left change-ratio + right change-ratio)`, so strength rises with
  both the degree of local change and the size `x` of the value; each profile then max-normalised to [0,1] (§4.1). (The
  standard surface boundary-strength formulation.)
- **Change-ratio** — the normalised difference between a value and a neighbour: left `= |x_prev − x|/(x_prev + x)`, right
  `= |x − x_next|/(x + x_next)`; a measure of local change in [0,1].
- **Offset** — the tick at which a note ends (onset + duration); the gap cue reads the offset-to-onset interval.
- **Inter-onset interval** — the time between two successive note attacks.
- **Gap (offset-to-onset)** — the time between one event ending and the next beginning (the silence/separation).
- **Agogic lengthening** — a note long relative to its neighbours (a phrase-final cue; it appears as an inter-onset peak).
- **Peak-picking** — selecting as boundaries the local maxima of the strength profile that exceed the adaptive threshold
  (the **whole-profile mean + k·SD** — the whole score's profile, **not** a sliding window; §4.4 pins this and this row
  matches it).
- **Notated-marker spike** — the large fixed strength added at a fermata, a breath mark/caesura, a structural barline, a
  mid-score key-signature change, a sudden tempo change or written ritardando, or an all-voice-rest onset (the
  deterministic, high-precision part).
- **Key-signature change (marker)** — a new key signature written mid-score (the engraved signature event, **not** the
  inferred key); a very sparse, section-level structural-boundary marker (§4.2).
- **Breath mark / caesura** — explicit composer-notated phrase / break symbols (the comma; the "grand pause" /
  railroad-tracks), read as deterministic marker spikes (§4.2).
- **Sudden (subito) tempo change** — a new tempo marking reached with no gradual transition; a sparse, high-precision
  structural-boundary marker (§4.2). A written ritardando/rallentando into an arrival is the gradual counterpart.
- **Maximal all-voice-rest span** — a span in which every eligible voice rests, not extendable in either direction without
  an eligible voice sounding (a Layer-2 empty slice).
- **Top voice** — the highest sounding voice of the texture (an *optional* Layer-1.5 cue for the function layer, not a
  prerequisite and not used by this primitive — the highest voice is not reliably the melody; what cadence theory calls
  the "soprano," named generally because the tool analyses any instrumentation).
- **Eligible voice** — a (staff, voice) line whose notes **sound**, are **visible**, and lie on an
  **analysis-eligible staff** (the exact three-flag test, §0; Layer 1 defines the staff flag, the voice-level
  combination is stated in this document because Layer 1 does not define voice eligibility).
- **Structural barline** — a double, final, or repeat barline (a notational division).
- **The cadence gate** — the function layer's rule admitting a cadence candidate only at a phrase boundary (§0;
  `cowork_layer5_function_design.md`); the consumer the texture profile and picked ticks feed.
- **Tick** — the absolute time-position in the score (§0); "time-position" in the sibling layer docs names the same
  thing.

## 10. Background: what this replaces, and the as-built map (not needed to understand the primitive)
Today the fermata-boundary scan exists in **two byte-identical copies** kept in hand-sync (one on the production region
path, one in the corpus diagnostic tool), and the per-region "ends a phrase" flag is re-derived inline at every consuming
site (the exact set enumerated at build). Its known consumers are the dormant **key-agnostic cadence anchor** (a
built-but-unengaged cadence detector that anchors on the boundary without a resolved key) and the default-off
**joint-key re-key pass** (a gated re-keying refinement) — both function-layer components, named in
`cowork_layer5_function_design.md`; whether the production cadence/marker path also consumes it is enumerated at build. The
function layer's predecessor already names phrase boundaries as planned input. This primitive unifies the duplicated scan
into one owned Layer-1.5 view and replaces the fermata-only definition with the graded surface-cue + marker model above;
the concrete file map and the cue formulas are in the build instruction and the methods catalog (`cowork_phrase_boundary_methods.md`).

## 11. Open items
1. The **precision-phase constants** — the three cue weights, the peak threshold `k`, the minimum-silence duration, the
   voice-coincidence window `τ` (§4.3), and the notated-marker spike magnitude (§4.2) — left at stated defaults by the
   build, tuned in the precision phase.
2. **Confirm the live consumers** of "ends a phrase" at build — ✅ **DONE 2026-06-26:** the only consumer is the
   default-off joint-key re-key pass (`applyJointKeyWiring`, gated on `jointKeyWiringEnabled()`), so the primitive is
   **unreachable in production** — byte-identical, built-dormant (verified at source). It becomes load-bearing when the
   function layer engages it.
2b. **As-built marker refinements deferred (build, 2026-06-26) — pin when the function layer engages + non-chorale test
   cases land.** (a) The **eligible-voice qualifier** on the fermata/breath markers is not yet applied — they fire at *any*
   fermata/breath (matching the retired byte-identical scan; harmless on chorales where all voices are eligible). (b) The
   **tempo marker** fires at any *discrete* tempo-text tick (incl. the opening tempo); it should fire on a genuine tempo
   **change** only, the way the key-signature marker already tracks change-only. Both are proportionate first-cut
   simplifications, inert while dormant; pin them with non-chorale (orchestral / non-SATB) test cases.
3. **Deferred cues** — the global regularisers (phrase-length prior, metric parallelism) and the information-content /
   surprisal cue — named in the methods catalog, built only if the corpus shows a need (each adds a corpus-specific
   constant or a trained model).
4. **Articulation and dynamics cues** (slur ends, abrupt dynamic changes) — weak/auxiliary in the literature; admissible
   as additional low-weight surface profiles if measured to help, deferred from the first build.
5. **★ Marker scope — global vs per-part — and boundary provenance (recorded 2026-07-01, user-raised).** The §4.2
   deterministic markers mix two **scopes**, and the current model spikes all of them onto the **texture** profile and
   emits them unconditionally (§4.4) — which can promote a *local* event to a *global* boundary and lose the fact that it
   was local:
   - **Globally-scoped (system-wide by notation):** the **structural barline**, the **mid-score key-signature change**,
     the **subito tempo change**, and the **all-voice-rest onset** — these apply to the whole texture and legitimately
     spike the texture profile.
   - **Per-part-scoped (notated on one voice/staff):** the **breath mark**, the **caesura**, and — strictly — the
     **fermata**. A breath in one instrument does **not** mean the whole texture phrases there; spiking it unconditionally
     onto the texture profile discards that locality and over-segments non-chorale textures. The principled form is for a
     per-part marker to enter as a **per-voice** marker event and reach a **texture** boundary only through the same
     **voice-coincidence aggregation** as the graded cues (§4.3) — a lone breath then yields a **per-voice** boundary
     (already exposed by this primitive, and the raw material for the future voice-leading / melody-line axis,
     `cowork_idiom_discovery_findings.md`), not a forced global one. (The fermata is the borderline case: *conventionally*
     an ensemble hold, but *notated* per staff — treating it as per-part-then-coincidence is inert on chorales, where all
     voices hold together, and more correct on orchestral scores.)
   - **Chorale-inert.** In the chorale convention all voices fermata/breathe together, so the texture boundary is
     unchanged; the refinement matters only for orchestral / contrapuntal (non-SATB) textures — consistent with the
     byte-identical-on-chorales discipline and adjacent to the §11-2b(a) eligible-voice qualifier (a related, narrower
     item).
   - **Provenance (the information-loss fix).** Each picked boundary — texture *and* per-voice — should carry **which
     cue/marker fired and at what scope** (global, or per-voice with which / how-many voices coincided), so a downstream
     consumer (Layer 6's punctuation-span annotation) does not lose that a boundary was a *local breath* versus a *global
     barline*. The picked set is scope-blind today. Recorded as a proper-layer refinement; per the standing rule, not
     built until the inference phase opens; validate on a non-chorale corpus (§8).
