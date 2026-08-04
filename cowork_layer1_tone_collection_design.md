# Layer 1 — TONE COLLECTION — Design Document (for user sign-off)

> **★ STATUS: HISTORICAL — the concern this document designs was ABSORBED BY THE NOTE MODEL, and this
> document is NOT a contract home (user-ruled 2026-08-04; CC, READ WAVE 6, dispatch
> `cc_instruction_reads_6.md` §0a ruling R6, Task 5.2; `OPEN_ITEMS.md` OI-327).** The single
> responsibility §1 states — collect every sounding note in a stretch of music, annotated, losslessly,
> by one path — **is now the lossless note model's**, specified at `ARCHITECTURE.md`'s Layer-1 section
> and contracted at `cowork_layer1_note_model_design.md`, which that section delegates to by name.
> This document was put to the user for sign-off and its §7 checkboxes were never ticked; what
> happened instead is that the design was superseded by the note model absorbing the role.
> **Why it was ruled NOT delegated rather than delegated late:** a delegation here would create a
> SECOND home for a concern that already has one, which principle #6 forbids — so the record states
> the absorption and the document's historical status, and stops. **What the document is still for:**
> the provenance of how the collection responsibility came to be separated from weighting, bass
> selection and filtering (§1's own revision note records the user's three review comments that forced
> the split). Read it as that record, not as a live contract. Its two register entries — D-569 and
> D-570 — keep the class `gap`, which is the correct class for a decision whose concern is homed
> elsewhere and whose recording surface is historical.
>
> **Upstream-first sweep, layer 1 of N.** This is the design/contract document for the most-upstream layer in
> the pipeline. It (a) states the layer's intended single role, (b) describes **what the code currently does**,
> verified at source, (c) lists **what is missing or currently not appropriate**, and (d) proposes the target
> design. **No code changes until the user signs off (§7). Downstream layers frozen.**
>
> **★ Provenance (Cowork no-assume rule):** every "currently does" statement below is from a source read this
> session of `src/composing/analysis/engravingbridge/regiontonecollector.{h,cpp}` and
> `regiontoneprimitives.cpp` at HEAD `edd33901ed`. Items I did **not** fully read are marked `[unverified]`.
> Preference *values* (e.g. `bassPassingToneMinWeightFraction`) are described by role, not asserted numerically
> (not read this session).

---

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

*(The original §1 conflated collection with weighting/bass — corrected here per the user's three review comments:
no multiple paths, collect don't drop, separate collecting from weighting.)*

## §2 — Scope: what is (and is not) this layer
**IN this layer** (the tone-collection responsibility):
- `staffIsEligible` / `isChordTrackStaff` (eligibility predicates, `.h`).
- `collectRegionTones` (`regiontonecollector.cpp`) — the rich region accumulator (production path).
- `collectSoundingAt` + `buildTones` (`regiontoneprimitives.cpp`) — a simpler point-in-time collector.

**NOT this layer, but living in the same module** (a decomposition smell — see §4.5): the segmentation
sub-boundary detectors `detectOnsetSubBoundaries` / `detectBassMovementSubBoundaries` (layer 2),
`findTemporalContext` (a chord-context helper), `collectPitchContext` (feeds key resolution). The module header
calls itself "single source of truth for score-walking helpers" — i.e. it is organised by *mechanism*
(score-walking), not by *responsibility*.

## §3 — What the code currently does (verified)

### 3.1 Staff eligibility (`staffIsEligible`, `.h`)
A staff is eligible at a tick iff: it is **shown** (`st->show()`), its instrument at that tick does **not** use a
**drumset** (percussion excluded), and it is **not a "Chord Track" staff** (chord-symbol tracks excluded, matched
by part/instrument name containing `"Chord Track"`). Callers also pass an `excludeStaves` set that is honoured on
top. So: hidden, percussion, and chord-symbol staves are dropped; everything else is collected.

### 3.2 `collectRegionTones` — the production path (the rich accumulator)
Input: `(score, startTick, endTick, excludeStaves, parentStartTick=-1, excludeLookAheadOnDenseStart=false)`.
Steps, in order:
1. **Backward sustain walk.** From the first segment at/after `startTick`, walk **backward** while
   `segTick ≥ startTick − Fraction(4,1)`. `Fraction(4,1)` = **4 whole notes** (≈4 bars of 4/4), a **fixed cap**.
   For each prior chord whose `noteEnd > startTick`, the portion sustaining *into* the region is collected (a
   note ending before `startTick` is skipped; weight uses the clipped in-region duration).
2. **Forward region walk.** Walk segments with `tick < endTick`. (If `excludeLookAheadOnDenseStart` AND ≥3 PCs
   already sound at `startTick`, segments after `startTick` are skipped — a **legacy batch-only path; the bridge
   leaves it OFF**.)
3. **Per-note filtering.** Only `ChordRest`s that are chords and **not grace notes**; per note, only those with
   `n->play()` **and** `n->visible()` (silent / invisible notes skipped). Rests contribute nothing. All 4 voices
   per staff are walked.
4. **Weighting.** Base weight per note occurrence = `(durationInRegion / regionDuration) × beatWeight(beatType)`,
   where `beatWeight`: DOWNBEAT 1.0 · stressed 0.85 · unstressed 0.75 · sub-beat 0.5.
5. **Aggregation by PITCH CLASS** into `accum[12]`: sums `totalWeight`, `durationInRegion`; records the set of
   distinct onset ticks (`metricTicks`), the **lowest** pitch + its tpc, a per-tick voice count, and an
   `onsetAtRegionStart` flag (true if the PC truly attacks at `parentStartTick`).
6. **Pass 2 — repetition boost:** `totalWeight ×= (1 + 0.3 × (distinctMetricPositions − 1))`.
7. **Pass 3 — cross-voice boost:** `totalWeight ×= 1.5` if the PC is sounded by `>1` voice at some tick.
8. **Pass 4 — sustain-pedal tail:** **driven by actual pedal markings** (`buildPedalWindowIndex`; if a staff has
   no pedal window, nothing happens). For a note whose written end is inside the region under an active pedal,
   adds a **discounted** tail-weight (`× pedalTailWeightMultiplier`) for the span from note-off to pedal release.
   Gated on `pedalTailWeightMultiplier > 0`. *(It is marking-driven, **not** instrument-type-gated.)*
9. **Normalise** all PC weights to sum to **1.0**.
10. **Bass selection.** Bass PC = the **lowest pitch among PCs whose weight ≥ `bassPassingToneMinWeightFraction
    × total`** (a passing-tone floor so a fleeting low note isn't called bass); falls back to the absolute lowest
    if none clears the floor.
11. **Output:** a `vector<ChordAnalysisTone>` with **one entry per sounding pitch class** (≤12). Each carries:
    `pitch` (the **lowest** occurrence of that PC), `tpc` (spelling of that lowest occurrence), normalised
    `weight`, `isBass`, `durationInRegion`, `distinctMetricPositions`, `simultaneousVoiceCount`,
    `onsetAtRegionStart`.

### 3.3 `collectSoundingAt` + `buildTones` — the point-in-time path
`collectSoundingAt` collects raw `{ppitch, tpc}` for all notes sounding **at** an anchor segment's tick, plus a
**backward walk with the same `Fraction(4,1)` (4-whole-note) cap** for sustains; same chord/not-grace/play/
visible filters. `buildTones` converts those to `ChordAnalysisTone` **one-per-note** (no weighting; `weight`
defaults), marking the single lowest pitch as bass. This path is used by `findTemporalContext` to cold-analyze
neighbor chords. **It is a second, divergent collection semantics** (per-note + unweighted) vs `collectRegionTones`
(per-pitch-class + weighted).

### 3.4 Reach summary (answering the direct questions)
- It reaches **backward** (pre-region sustains) **and forward within the region**; it does **not** reach forward
  past `endTick`. Cross-region/progression look-ahead is a *different* function (`findTemporalContext`), not this
  layer. The backward cap is the fixed `Fraction(4,1)` = 4 whole notes in **both** collectors.

## §4 — What is missing or currently not appropriate

**4.0 — The layer conflates THREE responsibilities (the meta-gap, user review).** As built it does *collection*
+ *filtering* + *weighting/aggregation* in one pass: it walks the score (collect), drops grace/non-playing/
invisible/ineligible (filter — a decision), and computes duration×beat×repetition×cross-voice×pedal weights
aggregated by pitch class with a bass pick (weight — interpretation). These are factual, decisional, and
interpretive jobs respectively; merging them is what forces the information loss (4.1), the silent dropping
(4.1b), and the divergent paths (4.4). The corrected role (§1) is collection only.

**4.1b — It DROPS rather than collects-and-annotates (user review).** It *identifies* grace notes
(`cr->isGrace()`) and discards them, and likewise discards `!play()`, `!visible()`, and ineligible-staff notes.
Discarding is a filtering decision, not collection — and it is irreversible information loss: a downstream layer
that wanted to reason about a grace ornament, an editorial-invisible note, or a cue cannot, because the note is
gone. Since the layer already recognises grace-ness, the fix is to **collect the note and annotate it**, leaving
the keep/drop decision to an explicit filtering step.

**4.1 — It transforms the score into pitch-class evidence and discards the notes (the core concern).**
`collectRegionTones` collapses every note into ≤12 per-pitch-class accumulators. Register beyond "lowest per PC"
is dropped, **voice identity** is dropped (only a count survives), **individual onsets/offsets and tie
structure** are dropped (only a distinct-onset-tick count survives), and **spelling (tpc) is kept only for the
lowest occurrence** of each PC. The raw note set (A) is turned into derived evidence (B); A is not preserved.
This violates the *annotate-A-with-B, don't-replace-A* principle, and it is not academic: downstream
embellishment/NCT discrimination, voice-leading checks, register-aware spelling, and the over-grab/segmentation
analysis all need note-level data that no longer exists here — and the anchor failure traced partly to there
being no clean note-level source to recompute from after the aggregation.

**4.2 — The backward reach is a fixed cap, not "until silent."** Both collectors stop at `startTick − 4 whole
notes`. A note (or pedal tone) sustaining longer than 4 whole notes is silently dropped from the evidence.
Correct behaviour is to walk back to each voice's actual onset (until the voice is genuinely silent), not a
magic horizon. *(Also a doc bug: the header comment says "4 quarter notes"; the code is 4 whole notes — 4× off.)*

**4.3 — No forward reach, and progression context lives elsewhere.** The layer is region-bounded with no
anticipation/cross-region forward read; "what comes next" is answered downstream (`findTemporalContext` + the
competition layer). If we decide a region needs wider context for harmonic understanding, today there is no
single place to extend the reach — it is split across layers. Whether tone collection should expose a
reach-extendable note stream (that downstream queries) is an open design choice.

**4.4 — Two divergent collection semantics.** `collectRegionTones` (weighted, PC-aggregated) and
`collectSoundingAt`+`buildTones` (unweighted, per-note) produce *different* representations of "what sounds
here," used by different consumers. One layer should have one collection contract; the two paths risk drift (the
exact failure mode the module was created to end).

**4.5 — The module is multi-responsibility.** Segmentation sub-boundary detectors, temporal context, and
key-pitch context share the file with tone collection. The layer's single responsibility is blurred by
co-location; these belong to layers 2/3/4.

**4.6 — The evidence weighting is a stack of unvalidated heuristics.** The repetition boost (`0.3`), cross-voice
boost (`1.5`), the four `beatWeight` values, the pedal-tail multiplier, and the bass passing-tone floor are
hardcoded constants that materially decide what counts as chord evidence (a long suspension earns high weight —
the anchor over-read source). None is validated against this layer's own oracle (§6); they are inherited
heuristics, not measured choices.

**4.7 — Minor/dead surface.** `excludeLookAheadOnDenseStart` is a legacy batch-only branch left OFF in
production — a divergent path that should be confirmed dead and removed or justified. `[unverified]`: I have not
re-read `buildPedalWindowIndex`, `safeBeatType`, or the preference *values*; the audit should.

## §5 — Proposed target design (for ratification/amendment)

**Split the one conflated function into three single-responsibility steps; collection is lossless and unified.**

1. **COLLECTION (this layer) — pure, lossless, ONE path.** Output the **note set**: every sounding note in the
   region, each annotated with pitch, tpc/spelling, staff, voice, onset, offset, in-region duration, and the
   *flags* `isGrace` / `plays` / `visible` / staff-eligible. **Nothing is dropped** (flags carry the facts a
   filter will later use) and **nothing is aggregated or weighted.** **One collection path** — `collectRegionTones`
   and `collectSoundingAt`+`buildTones` unify into a single parameterised collector (region-scope vs point-scope a
   parameter), and the legacy `excludeLookAheadOnDenseStart` branch is removed. *(Total-unification objective:
   multiple/divergent paths are forbidden — this is not optional cleanup.)*
2. **Reach until silent, not to a fixed cap.** Within collection, walk back to each voice's true onset (until the
   voice is genuinely silent), not `Fraction(4,1)`. Any forward/context reach is an explicit named capability,
   not a magic horizon. Fix the header doc ("4 quarter notes" → the real reach).
3. **FILTERING (a separate, explicit decision).** A thin step that reads the collection's annotations and decides
   which notes are eligible for harmonic analysis (e.g. exclude grace ornaments, percussion, chord-track). It is
   *reversible* (it selects, it does not destroy) and *inspectable* (the dropped notes remain in the collection).
4. **WEIGHTING (a separate derived layer).** From the filtered notes, compute the pitch-class evidence, the
   weights (duration×beat, repetition, cross-voice, pedal), and the bass — as a **view over the note set, never a
   replacement.** Its heuristics become tunable parameters validated against an oracle, not hardcoded magic.
5. **Single responsibility for the module.** Move the segmentation detectors, temporal context, and pitch context
   out into their own layers; this file becomes collection only.

*(Open question for sign-off: are Filtering and Weighting separate layers, or is this layer "collection +
annotation" with Filtering/Weighting as the immediately-downstream layers 1b/1c? Either is consistent with the
separation — the user decides the granularity.)*

## §6 — Correctness oracle for this layer (it is NOT the RN oracle)
This layer is upstream of key and chord, so its correctness is judged against the **score**, not DCML/music21:
does it collect exactly the notes a human reading the score would say sound in `[start,end)` (right staves,
right sustains, right filters), with bass and weights that faithfully reflect the notation? Completeness = all
note cases handled (sustains past the cap, ties, tuplets, grace, cross-staff, multi-voice unisons, pedal,
invisible/non-playing). The audit builds score-level test cases for each; the per-event tiered metric does **not**
cover this layer.

## §7 — Sign-off
- [ ] **Role (§1)** is the correct single responsibility for layer 1.
- [ ] **Current behaviour (§3)** is accepted as the accurate baseline.
- [ ] **Gaps (§4)** — which to fix now vs defer: ____________________
- [ ] **Target design (§5)** approved / amended: ____________________
- [ ] Proceed to the read-only layer-1 audit (CC reads the `[unverified]` items + builds the §6 score-level
      test cases) before any code change.

*Nothing in layer 1 is modified until this is signed. Downstream layers remain frozen.*
