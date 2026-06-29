# Target Architecture — North Star (user-ratified 2026-06-21)

> **Status: RATIFIED by the user.** This is the target the per-layer design docs implement and the upstream-first
> sweep builds toward. It supersedes the loose "tone collection = layer 1 / segment-first" framing. Existing-code
> descriptions here are verified at source (HEAD `edd33901ed`); the target is design. The mapping of current
> components → target layers is Cowork synthesis, to be refined per-layer.

---

## 1. The core principle
**Analyze at the finest grain where harmony is well-defined; make everything coarser a derived view.** Harmony is
constant between note change-points and changes only when notes change, so the atomic unit of analysis is the
**constant-sonority slice** (the span between consecutive note onsets/offsets) — never the metric beat. Two
consequences:
- **The score's notes are the single lossless source of truth.** Every later layer *annotates* or *derives a
  view*; nothing transforms or discards the notes (annotate-A-with-B, never replace A).
- **"Where the slices are" is a deterministic FACT, not a judgment.** It is read off the notes. This removes
  segmentation-as-a-decision entirely — there is nothing to get right or wrong about slice placement. The only
  judgments live inside *analysis* (is this slice a chord or a decoration? what key? what chord?) and inside
  *display grouping* (cosmetic).

This dissolves the largest measured error class (**over-grab, ~45%**) *by construction*: with every slice analyzed
on its own, no unit ever spans two harmonies. Over-grab stops being a lever and becomes impossible.

> **★ Scope, scale, incrementality (user mandate 2026-06-21 — cross-layer constraint).** The target is **ANY score
> opened in MuseScore — any size, any style** (Tristan Act 1 is in scope, not out of it). **Universality lives in
> the fact layers** (L1/L2 are style-agnostic and lossless); **style-specificity lives ONLY in the analysis-layer
> calibration** (presets/thresholds/gates/key model), never in structure — the architecture must analyze any score
> *structurally* even before it is tuned to analyze it *accurately*.
> **The working unit is a SELECTION** (a note/chord or a user-selected measure run) — **whole-score reading is
> validation-only**, not the shipping model. Binding requirements: **(R1)** cost scales with the working span
> (indexed queries; the validation harness still runs full acts); **(R2)** incremental re-analysis — an edit
> re-analyzes only the dirty span + its bounded context margin, never a whole-score pass; **(R3) the working span
> is EXTENSIBLE** — a later layer pulls context beyond the selection on demand via a **hybrid** (small fixed margin
> + lazy extend-until-stable/cap). The codebase already does this hybrid for key (`keyresolver.cpp`: fixed backward
> lookback + dynamic forward lookahead); L3 unifies it (and makes backward lazy too). Bounded context is what makes
> R2/R3 cheap, and it trades against the (gated) global-joint key direction. See `cowork_layer3_analysis_design.md`
> §0.1.

> **★ "Effort" preset — a planned future calibration knob (user, 2026-06-22).** Alongside the *style* preset
> (Standard / Baroque / Jazz …), a separate **effort** preset (quick / normal / ambitious) will trade analysis
> quality against response time. It is **calibration, not structure**, so it is a *retrofit*: a named preset over
> each layer's cost-driving **settings** (beam/candidate count, scoring- and reach-back-window sizes, caps) and
> on/off switches for the **optional expensive refinements** (e.g. the keyscape multi-timescale check; the gated
> joint key-and-chord step). **It will be added after a real implementation can be profiled**, not guessed now. Two
> rules preserve the cheap retrofit, starting now: **(a)** every cost-driving choice is an explicit *setting*, never
> a hardcoded constant; **(b)** every optional expensive refinement is a cleanly *separable on/off stage*. (The
> performance *floor* — e.g. routing per-slice scoring through the indexed note model — is correctness, not an
> effort dimension; effort scales only the optional work above that floor. A level that needs a fundamentally
> cheaper *algorithm*, not just smaller settings, would be more than a knob — revisit only if profiling shows it.)

## 2. The layer model

**The analysis half is decomposed into single-responsibility layers (user, 2026-06-21) — not one fat "analysis"
layer.** Each does ONE thing and annotates the slice; the order is fixed by dependency. **What "one thing" means
precisely is the *(evidence-source × question)* invariant in the control-flow contract below: a layer owns one
evidence source's contribution to one question — not necessarily the final answer to that question.**

**★ Minimality / maximal separation (user-ratified 2026-06-22).** Each layer does **as little as possible**: whatever
*can* be a separate concern in a later layer **must** be. A layer settles only the part of its question that **its own
evidence** decides, and **defers** everything that needs evidence a later layer owns — handed forward as carried
alternatives + an "uncertain" mark, never guessed. It never reaches for a separable sub-problem. *Worked example:*
resolving a symmetric chord's spelled root (diminished-seventh / augmented) needs spelling + function — a later layer —
so the chord layer names the *quality and bass* and **defers the root**, rather than pinning it by voice-leading or
spelling cleverness it shouldn't own. Likewise it decides *binary* chord-membership (needed to name the chord) but not
the *non-chord-tone type* (passing/neighbour/suspension — separable, so deferred). This is the rule that keeps every
layer thin and is the test applied when drawing a new layer's boundary: if a sub-task can stand alone with its own
evidence, it is its own concern.

**★ Maximal information (the complement to minimality, user-ratified 2026-06-22).** Within its one question, a layer
uses **all** the information available to it — never a reduced projection when a richer one is on hand. In particular
it uses the **notated spelling** (the tonal pitch class — `G♯` vs `A♭`), metric weight, articulation, and voice/staff
assignment that Layer 1 carries losslessly, rather than collapsing to bare pitch class. This composes *with*
minimality, not against it: **minimal scope, maximal evidence within that scope.** *Worked example:* a
diminished-seventh's spelled root is undecidable in *pitch class*, but the **notated** spelling usually names it — so
the chord layer reads the spelling and pins the root where the notation gives one, deferring only where the spelling
is absent or unreliable (a MIDI import, an expedient enharmonic). We do not discard information the score already
provides; the spelling is a strong-but-fallible prior, weighed against the other evidence, not trusted blindly.

| Layer | Name | Contract | Fact or Judgment? |
|---|---|---|---|
| **1** | **Note model** | Read the score once → the lossless, annotated set of sounding notes (pitch, tpc, staff, voice, onset, offset, duration, ties, `isGrace`, `plays`, `visible`, staff-eligibility). Preserved end-to-end. **No** weighting, filtering, or aggregation. ONE representation, ONE path. | Fact |
| **2** | **Change-point slicing** | From the note model → the constant-sonority slices (spans between the union of note onsets/offsets). Deterministic; lossless; not a heuristic. | Fact |
| **3** | **Key/mode** | For each slice, the prevailing **key/mode** (`C-major`, `F-mixolydian`, `B-phrygian`) — as a **context-aware path** over the slice sequence, from the notes alone: **pitch-class content + tonic emphasis** (bass, metric weight, frequency, leading-tone presence) integrated by the path's transition penalty. **Needs NO chord symbols, functions, or cadence detection** (a cadence is a V→I = function-level; cadence-based key refinement is the gated Stage 5). This is the dominant-error layer. | Judgment |
| **4** | **Chord symbol (+ non-chord tones)** | For each slice, the key-independent **chord symbol** (`Bm7`, `Gdim`) AND which notes are **non-chord tones** (one job — you cannot name the symbol without deciding membership). Uses the notes + the layer-3 key/mode as a diatonic prior + context (the prevailing chord, so embellishment slices don't spawn spurious symbols). | Judgment |
| **5** | **Function** | For each chord, the **function** (`V/V`, `IV7`, Roman or Nashville) = the chord symbol read **in** the key/mode. Mostly a derivation once 3 + 4 are known. | Judgment (thin) |
| **6** | **Grouping / display** | Merge adjacent slices carrying the same analysis into human-readable regions. Cosmetic, reversible, downstream. | View |

Sub-points:
- **The dependency order is the spine: key/mode → chord symbol → function → grouping.** Established by dependency
  analysis: **key/mode needs only the notes** (pitch-class content + tonic emphasis — NOT chord symbols, functions,
  or cadence detection); **chord symbol is *helped* by key/mode** (diatonic prior) but key/mode is **not** helped by
  chord symbols (naming the notes "G7" adds nothing key-relevant beyond the pitch content already present);
  **function needs both.** So key/mode is the root and goes first. (Corrections recorded 2026-06-21: an earlier draft
  floated *chord-symbol-first*, a later one imported *cadence detection* into key/mode — both wrong. A cadence is a
  V→I (function-level, downstream); modulation/passing-keys come from the key path's transition penalty, not cadence
  detection; the cadence/function-based key refinement is the gated Stage 5. Matches Temperley key-from-pitch-profile,
  Contrapunctus key-first / "given the key the rest is largely solved", and today's
  key-then-chord code. Full survey + sources in `cowork_layer3_keymode_design.md`.)
- **The residual key↔chord coupling** (relative major/minor; modulation — the measured key floor) is where key and
  chords genuinely co-determine; pure key-first-**and-final** feed-forward plateaus there. The escape is letting
  chords feed *back* to key for those few cases — the **gated joint step (Stage 5)**, NOT the base order.
- **Chord symbol + non-chord tones are ONE layer** (Temperley decides root and ornamental dissonance together;
  JNMR-2024 = chord + per-note membership). Embellishment discrimination lives here with context, NOT a separate
  recompute (the anchor lesson: re-deriving a chord from a flattened union over-reads).
- **The pitch-class weighting** that today lives in `collectRegionTones` is a *derived view* used by the
  chord-symbol layer (4), not a primitive and not a replacement for the notes.

**Control flow — forward-only, no backward edges (user-ratified 2026-06-22).** The layers form an **acyclic forward
dependency**; ambiguity is **never** resolved by re-entering an earlier layer. Concretely:
- **A layer runs once and hands its work forward.** Where a layer cannot decide (the canonical case: key/mode at a
  relative-pair or modulation/tonicization seam), it does **not** emit a single forced answer — it emits the **chosen
  reading plus the ranked alternatives plus an "uncertain" mark** (a *prepared menu*, computed once, including the
  expensive part — e.g. the key path's whole-sequence decode).
- **The later gated step SELECTS from that menu; it does not call back upstream.** The gated joint key-and-chord step
  (Stage 5) resolves an uncertain region by **choosing among the earlier layer's carried alternatives** using the
  evidence that layer was not allowed to use (chord identity, cadence, function). It is a *forward consumer picking
  from a menu*, not a request that travels back into the earlier layer's inference.
- **Resolution triggers only a localized FORWARD recompute.** When the selection differs from the earlier layer's
  tentative pick, only the layers that **depend on** that decision (chord, then function) are recomputed **for the
  affected region** — a bounded, region-scoped forward pass. The earlier layer's algorithm is **not** re-run; its
  output for that region is simply *replaced* by a selection from its own alternative list.
- **A *confident* earlier inference is also overturnable — the general confidence-weighted override (user-ratified
  2026-06-26).** The menu-selection above covers a layer that *flagged* uncertainty. The contract generalizes to every
  earlier inference, confident or not: each later layer brings its independent evidence to bear on all of them.
  **Agreement reinforces** (raises joint confidence); a **confident** commit is **overturned only when the contradicting
  later evidence crosses a threshold scaled to the earlier layer's confidence** — a well-founded commit demands decisively
  stronger evidence than a borderline one, so confidence sets the *bar to overturn*, not an absolute veto. When the bar is
  crossed, the **same localized forward recompute** fires (the overturned decision is **closed for that pass** — the
  recompute does not re-open it, preserving the acyclic guarantee). This keeps a *confidently-wrong* commit recoverable
  instead of locked in — the lever the precision phase tunes (the per-channel thresholds are precision-phase constants;
  the mechanism and direction are fixed here). The function layer's two instances are the **cadence-confirmed modulation**
  (a cadence overturning a confident key) and the **fine-grain chord override**. *Rejected:* a hard confidence-gate
  (locks confident-but-wrong commits); bespoke per-channel one-offs (hide that they are one mechanism); and a backward
  re-derivation / full joint search (measured inert — the gain is soft-evidence quality carried forward). Full treatment:
  `cowork_layer5_function_design.md` §8 / §9-D7.
- **Coverage failures stay in their layer.** If the true reading was never even among the carried alternatives
  (a coverage miss, not a selection miss), the fix is to **widen that layer's candidate set inside that layer** — not
  to add a backward edge.
- **Why:** this preserves the acyclic guarantee (no key←chord cycle), is *why* each judgment layer carries ranked
  alternatives instead of one forced answer, is efficient (the expensive decode runs once; resolution is a cheap local
  re-rank + a scoped recompute), and is deterministic (no iterate-to-fixpoint convergence question). **This contract
  is the spine of the Stage-5 / gated-step design doc** when it is written.

**What "single responsibility" actually means here — one (evidence-source × question) contribution, NOT "one layer
owns the answer" (user-ratified 2026-06-22).** A judgment (key/mode, chord, function) can require evidence that only
becomes available in a later layer, so **no single layer can own the *final answer* to it** — that was an overclaim.
The invariant we hold is finer and more ambitious: **each layer owns the contribution of exactly one evidence source
to one question, delivered once and forward.** Worked through for mode (the case that exposed this):
- **Layer 3 owns the *note-evidence* contribution to key/mode** — the candidate space (the 252 key/modes) and the
  note-fit model — and resolves everything the notes can resolve. This is its sole, exclusive territory: no other layer
  generates or re-scores key/mode candidates from the notes.
- **The gated Stage-5 step owns the *functional-evidence* contribution** (chord / cadence / function) that arbitrates
  **only** the residual Layer 3 flagged "uncertain", by **selecting among Layer 3's carried alternatives** — never
  generating a new candidate, never re-scoring from the notes (that note-evidence model has exactly one home).
So a judgment like "mode" is **built up across layers along an evidence boundary**, each layer's contribution disjoint
and *final-for-its-evidence*. Mode inference is therefore *legitimately* partly outside Layer 3 — and that is not a
leak but the intended factoring, because the deciding evidence for the residual (function) cannot exist at Layer 3 by
the dependency order. **Every layer's responsibility is to be stated this way — not "owns X", but "owns the [named
evidence] contribution to X, delivered once, forward" — and the boundary (what it does NOT own, and which later layer
owns the rest) stated explicitly.**

> **★ The rule is a strong DEFAULT, not dogma — revisable under control (user, 2026-06-22).** If forward-only is found
> to genuinely hinder correctness or quality, it may be relaxed — but only as a **deliberate, surfaced, measured,
> documented** exception, **never a silent cycle**. A sanctioned backward edge (e.g. a bounded feedback iteration)
> must be: justified by evidence that the forward-only path plateaus; **scoped** to the cases that need it; **gated**
> (like the joint step) so it does not fire on the clean majority; **convergence-bounded** if iterative (a fixed
> iteration cap, no oscillation); and **recorded as an architecture decision**. The bar is high precisely because a
> backward edge trades away the acyclic guarantee — but it is on the table if the evidence demands it.

**★ Bounded context — the analysis works on the user's selection, and a layer asks for more (user-ratified
2026-06-24).** A governing cross-cutting contract, applying to **every** layer L1–L(n) (full design:
`cowork_bounded_context_design.md`). The product analyses the **user's selection**, never the whole score
(whole-score is offline batch testing only). A selection is a temporal subset, so a layer that needs evidence beyond
it **requests an extension** from Architectural Layer 1 (the supplier), which loads more notes in the asked direction,
append-only, clamping at — and reporting — the score boundary; the requesting layer carries the **stop condition** and
a **hard bound**, so extension terminates. **No layer may assume infinite context** ("the whole score is always
loaded") — that assumption is the expensive-to-retrofit error this contract exists to forbid; it must be designed into
each layer *before* the next is built on top. Output covers only the selection; extended music is **evidence**.
Requesting notes from a lower layer is a **data-supply call down the stack, not an analysis back-edge**, so it is
consistent with the forward-only contract above. The whole-score load is the **degenerate case** (selection = score,
no extension fires) — which is what keeps the batch-testing path unchanged.

**★ Verifiability is a risk posture, not a permission gate — build sound theory with an explicit confidence path
(user-ratified 2026-06-29).** A construct's **absence from the validation corpus is not evidence it is wrong or
useless** — only that *that* corpus cannot check it. The discipline is therefore: **prefer what we can verify** — a
ground-truth oracle is how we catch our *own* theory errors (the `V/iv` over-trigger was caught only by measuring
against DCML); **but** for **theoretically sound** logic we cannot verify against the current corpus, **do not refuse it
outright.** Require, *before* building it, (a) an **explicit alternative-confidence path** — a different corpus,
theory-rules-as-oracle, or expert spot-check — and (b) an explicit **"empirically-unvalidated" mark** on the output, so
its status is never silently conflated with verified output. This **supersedes the stricter "build-only-what-we-can-
verify" phrasing** (e.g. `cowork_layer5_function_design.md` §9-D1, where unverifiability was one of several rejection
grounds): unverifiability **alone** is a *flag plus a confidence-path requirement*, not a veto. It governs L6 onward —
in particular, the grouping layer's reach **beyond** the DCML-annotated flat phrases / key-areas / cadences (hierarchy,
periods/sentences) is **permitted under this contract with a chosen verification strategy**, not foreclosed by
corpus-absence.

## 3. Why this is the target (the evidence)
- **Dissolves over-grab (~45%, the biggest lever)** by construction — no coarse unit spans two chords.
- **Matches the metric we already built.** The standing oracle-root metric scores per oracle-event (per-slice);
  analyzing per-slice makes the optimized object and the measured object the same.
- **Matches the SOTA.** Contrapunctus — which beats AugmentedNet/AnalysisGNN out-of-sample — labels *every beat*
  rather than coarse-segment-then-analyze; per-event analysis is the winning shape.
- **Embodies annotate-don't-transform.** The note model stays the source of truth; the info-loss that caused the
  anchor failure (no note-level source to recompute from) cannot recur.
- **Removes a whole class of judgment.** Slice placement becomes a fact, not a tunable heuristic — less to be
  wrong about, and one fewer coupled decision.

## 4. How it differs from the existing code (the gap to close)
> **★ AS-BUILT STATUS (2026-06-21): Layer 1 has LANDED** (`e30bb45a4f`, ratified). The §4 "Existing (verified)"
> snapshot below is the **pre-rebuild baseline**; it is preserved as the gap-to-close record. What changed since:
> the **note model** (lossless, tie-resolved) now exists as a separate module (`composing/.../notemodel/note_model.{h,cpp}`),
> and `collectRegionTones`' note-reading half is replaced by it; the weighting half survives as a **derived view**
> (`weightedPcView`) consumed unchanged by the still-live segment-first analyzer. The coarse/sub/merge machinery
> below **still runs and still drives analysis** (it retires only when layer 3 consumes the slicer) — so §4 remains
> an accurate description of the *transitional* spine, with layer-1's note-reading the one piece already swapped.
> The canonical `ARCHITECTURE.md` carries the authoritative as-built; this banner keeps the target doc honest.

Existing (verified): a **segment-first** pipeline — coarse boundaries (`harmonicsegmenter.greedyExpandSegmentation`,
fed by `collectRegionTones`), sub-boundaries (`detectOnset/BassMovementSubBoundaries`), per-region tone
collection + `analyzeChord`, then a chord-dependent **merge** (`coalesceShortSameRootRuns`/`absorbShortRegions`).
Tone collection conflates note-reading with weighting/aggregation and discards the notes.

Target mapping (synthesis, to refine per-layer):
- The **coarse + sub boundary machinery and the merge** are *retired into* the cosmetic **grouping layer (N)** —
  they no longer drive analysis. Their "where to split" judgments become unnecessary (slicing is a fact).
- **`collectRegionTones`** splits: the *note-reading* part → the **note model (layer 1)**; the *weighting* part →
  a **derived view consumed by layer-3 analysis**.
- **`analyzeChord` / key resolution** → **layer-3 per-slice analysis**, now run per constant-sonority slice with
  context, instead of per coarse region.
- The **sub-boundary detectors** (peer leaf primitives, verified) are not needed as *deciders*; the change-point
  set subsumes them. They may survive only as fast change-point enumeration helpers, if at all.

This is a re-shape, not a tidy-up: the segment-first spine is replaced by slice → analyze → group.

## 5. Implications for the upstream-first sweep
- The sweep order becomes: **Layer 1 (note model) → Layer 2 (slicing) → Layer 3 (analysis: key, then chord, with
  NCT context) → Layer N (grouping)**, each with its own signed design doc (current behavior + gaps + target),
  built upstream-first with downstream frozen and the tiered oracle metric as the per-layer done-signal.
- **Layer 1's design doc was re-anchored and is now AS-BUILT (done 2026-06-21):** layer 1 is the **note model
  (lossless source of truth)**, *not* "tone collection." It was rewritten to `cowork_layer1_note_model_design.md`,
  signed, implemented (`e30bb45a4f`), branch-covered, and ratified — the tone-collection/weighting content demoted
  to the derived `weightedPcView`. That design doc is the as-built record for layer 1; layer 2 (slicing) is next.
- The chord axis is confirmed near-ceiling (~2–3%); the real work is layer-2/3 (slicing makes over-grab moot;
  analysis-with-context carries the key + NCT levers).

## 6. Open design questions (for the per-layer docs) — expanded

These are not yet decided; each is resolved in its layer's signed design doc. Options + trade-offs + a Cowork
**lean** (a recommendation, not a decision) are given so the per-layer work starts from a real position.

### 6.1 Layer 2 — the change-point set (what defines a slice boundary)
- **Onsets only, or onsets + offsets?** An **onset** (a note attacking) is the harmonically-primary event — a
  new pitch can change the harmony. An **offset** (a note releasing) shrinks the sounding set; usually the
  harmony persists (dropping a chord tone leaves the same, possibly incomplete, chord), occasionally it matters.
  Including offsets is *complete* but produces extra slices — some redundant (identical harmony before/after,
  which group away in layer N) and some **incomplete-chord** slices (only part of a chord still sounds) that lean
  hard on layer-3 context to carry the harmony. *RESOLVED (user, 2026-06-21):* **boundaries at every onset AND
  every release** — both change the sounding set, so both open a slice; this is what makes each slice a *genuine*
  constant-sonority span. The earlier onsets-only lean broke that property (a chord tone releasing shrinks the
  set mid-span) and pushed incomplete-tail reasoning to layer 3. Redundant same-harmony release-slices are
  harmless — layer N groups them away; it is fact, not judgment.
- **Tie resolution is a LAYER-1 concern, not layer 2.** A tied note is one sounding event from first attack to
  final release; the tie continuation is **not** a new onset. The note model must represent a tied group as a
  single sounding span (onset→release), so layer 2 never sees a spurious change-point at a tie. *(If layer 1 gets
  this wrong, every downstream slice is wrong — it is a correctness obligation for layer 1.)*
- **Grace notes.** Per "collect, don't drop," the note model keeps grace notes flagged `isGrace`. The question is
  whether a grace opens its own micro-slice. *Lean:* **a grace does not open a slice of its own** — it is
  annotated onto the following slice as an ornament, so analysis sees the real harmony, not a one-grace vertical.
  (Equivalent to treating grace as a layer-1 annotation, not a layer-2 boundary.)

### 6.2 Layer 3 — the analysis (the only place judgment lives)
- **★ Diagnostic from layer 1 (recorded 2026-06-21, `cc_layer1_impl_report.md` §5.3):** the current scoring
  **leans on the tie-inflation bug** — a held (tied) note used to get a spurious repetition-boost that happened to
  push some ambiguous sonorities toward the oracle root (e.g. bwv154.8). The faithful note model removed that
  boost, surfacing a small downstream wobble (+3/+1/+1 charged, KEY flat). **When layer-3 scoring is rebuilt/
  re-tuned, do NOT rely on the held-note repetition bonus**; those ~4 cases should recover under correct
  re-calibration. (This is the hidden-dependency the upstream-first sweep exists to surface.)
- **Two different context scales — likely two sub-steps.** Chord/NCT discrimination needs a **narrow** window
  (the slice + its immediate neighbors + metric strength — enough to see "weak, stepwise, between two chord
  tones"). Key needs a **wide** window — the re-assessment + Contrapunctus both found the **keychain structure**
  (long, phrase-aligned key runs) is what matters, not per-event key correctness. So key and chord want different
  context scopes; *lean:* resolve the **keychain over a wide window first**, then chord/NCT per slice over a
  narrow window given the local key.
- **Key↔chord coupling: feed-forward, not heavy joint.** The two genuinely couple (V→I cadences mark keys; keys
  interpret chords). But the re-assessment measured the **joint/lattice search inert** — the win is *soft-evidence
  quality*. *Lean:* **feed-forward — key/mode (from pitch content + tonic emphasis; modulation via the path's
  transition penalty) → chord symbol → function per slice**. The cadence/function-based key refinement (which DOES
  couple — a V→I confirms a key) is a **bounded, gated Stage-5 step**, never a full joint lattice and never folded
  up into the key/mode layer (cadences are function-level, downstream — §2 layer 3).
- **Candidate generation vs re-ranking — generation is the lever.** Audit #6 found the residual is mostly "a
  candidate was never surfaced," not "the wrong candidate was picked" (pure re-rank ~1.7%). So layer 3's chord
  step is first **complete candidate generation per slice**, then selection. A **small learned re-ranker**
  (Contrapunctus's +7pp; LR over tonic-rotated windowed PC features) is a **Stage-5+, secondary** add-on that
  picks among *complete* candidates — not a substitute for getting the candidate set right, and gated on the
  oracle/tier metric + out-of-sample discipline.
- **NCT/embellishment discrimination is chord-first, per slice, with neighbors — never a union recompute.** The
  anchor lesson: re-deriving a chord from a flattened tone union over-reads. The right shape (JNMR 2024 /
  Contrapunctus): hold a basic chord reading and judge each slice's "extra" pitches as chord-tone vs NCT using a
  per-note **chord-membership** test informed by metric position + the prev/next chord. *Open:* the exact
  membership criterion and window — designed in the layer-3 doc.

### 6.3 Layer N — grouping (cosmetic, but it IS the output structure)
- **Equality rule — group on the full label, not just the root.** Two adjacent slices merge only if their
  *analysis* matches at the granularity the output shows. Grouping on root alone would merge `I` and `I6` (same
  root, different inversion) into one region, losing a real display distinction. *Lean:* **merge on the full
  Roman-numeral reading (root + quality + inversion + applied/secondary marking)**; anything finer than the
  output cares about is the right key.
- **Embellishments group automatically — if layer 3 did its job.** A passing-tone slice that layer 3 labels as
  "still chord X (with an NCT)" carries the *same chord analysis* as its neighbors, so grouping merges
  `[X][X+passing→X][X]` into one `X` region with the NCT annotated. Grouping needs no embellishment logic of its
  own; it inherits the correctness of the layer-3 judgment. (This is why the NCT decision must live in layer 3,
  not here.)
- **Display-only feedback.** Grouping must **not** feed back into analysis (no re-analysis of grouped regions —
  that reintroduces the merge-then-stale-chord bug). It is a pure derived view that also happens to be the unit
  the RN output is emitted in. The per-slice analysis remains the source of truth; the region is a presentation
  of it.

### 6.4 Performance (per-slice is more points than per-region)
- The slice count ≈ the **onset density** of the piece (dense homophony → many slices; a held chord with a melody
  over it → a slice per melody onset). Each slice's chord-ID is cheap (a small pitch set); the cost is the
  context build and the key window.
- *Mitigations, all using machinery that already exists:* **cache** each slice's analysis (analyze once);
  **bound** the context/key window; analyze the **visible range first** then backfill (Contrapunctus's
  viewport-incremental approach keeps the editor responsive). None is a blocker; size it in the layer-3 doc.

### 6.5 Cross-cutting — slices vs oracle events (keep them aligned, not equal)
Our slices are **finer** than the oracle's annotation grain (the oracle marks a harmonic event; we slice every
onset). So several slices map to one oracle event, and they should all carry the **same** analysis (or be
NCT-flagged within the same chord). The standing oracle-root metric scores at the **oracle's** event ticks, so a
group of slices covering one oracle event is judged by its (shared) analysis — consistent by construction, and
the reason the metric and the analysis grain compose cleanly. A *disagreement* among slices covering one oracle
event is itself a signal (a real sub-event the oracle didn't annotate, or a spurious split) — a useful diagnostic,
not a metric problem.

*Nothing is implemented from this document directly. It is the north star; each layer is designed, signed, and
built in turn.*
