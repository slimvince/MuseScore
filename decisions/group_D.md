# Decisions group D — Layer 1 — the note model

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-037 — The note model is the single source of truth for what sounds, and reads the score once

> **The lossless, tie-resolved NOTE MODEL — the single source of truth for "what sounds."** `NoteModel::build(score)` reads the score **once**

**In plain words.** One component reads the score and works out which notes are sounding when. Everything else asks it, and nothing else reads the score.

**Why.** Stated constraint, ARCHITECTURE.md:1173: one read of the score into one queryable set is what makes the note model the single source of truth for what sounds; the alternative is several readers that can disagree.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1523`

**Provenance.** ARCHITECTURE.md:1162-1173 (Layer 1 - Built+Live)

### D-038 — Tied notes are one event; spans are answered by overlap with no horizon

> Tied groups are merged into **one** span/onset (via the DOM `firstTiedNote`/`lastTiedNote`/`playTicksFraction`); spans are true `[onset,release)` answered by **overlap with no horizon** (the old 4-whole-note backward cap is gone).

**In plain words.** A note tied across a barline counts once, starting where it was struck and ending where it stops. Asking what is sounding at a moment looks back as far as needed, with no arbitrary cut-off.

**Why.** Stated constraint, ARCHITECTURE.md:1173: tied groups are merged into one span and one onset via the score model's own tie links, and spans are answered by overlap with no horizon - which retires the old four-whole-note backward cap that could miss a longer sustain.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1523`

**Provenance.** ARCHITECTURE.md:1173; the behaviour change it caused is the ratified trade-off at :1026-1032

### D-039 — Ineligible notes are kept and flagged, never dropped

> Grace / non-playing / invisible / staff-ineligible notes are **kept and flagged, never dropped**.

**In plain words.** Notes that should not drive the analysis - grace notes, hidden notes, notes on a non-musical staff - are still recorded, marked as such. Nothing is thrown away.

**Why.** Stated constraint, ARCHITECTURE.md:1173, and #12: a dropped note is information lost for good, so ineligible notes are kept and flagged and each consumer decides what to do with them.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1523`

**Provenance.** ARCHITECTURE.md:1173; the standing no-information-loss principle is CLAUDE.md #12

### D-040 — The tie-unresolved atoms are republished additively for the joint estimator

> `notatedNotes()` republishes the tie-UNRESOLVED atoms — EVERY notated note incl. tie continuations, each with its OWN notated span, a `tieContinuation` flag, a `hasFermata` flag, and `resolvedIndex` linking to its tie-resolved `NoteEvent`

**In plain words.** As well as merging tied notes, the note reader also publishes them separately, each with a marker saying it is a continuation. The joint estimator needs both views.

**Why.** Stated constraint, ARCHITECTURE.md:1173: the tie-unresolved atoms carry the facts the tie-resolved surface discards and the joint estimator's event lattice and emission covariates need; publishing them additively keeps every existing consumer byte-identical.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1523`

**Provenance.** ARCHITECTURE.md:1173 records it as 'Purely additive' under the OI-180 dual-path sanction

### D-517 — The note model's span query uses a start-time-ordered list plus a running latest-end-time tree, chosen because it is the simplest structure that is fast AND returns notes in scan order

> - **A numeric look-up index (a start-time-ordered list plus a "latest end-time so far" tree).** Alternatives
>   considered: an interval tree, a bucketed index. Chosen: this structure — it is the simplest one that answers the
>   span-of-time queries quickly *and* returns notes in exactly the same order a plain left-to-right scan would.

**In plain words.** Asking which notes sound between two moments must stay fast on a whole piece. The structure chosen is the simplest one that answers quickly while returning the notes in exactly the order a plain left-to-right scan would.

**Why.** Stated with the decision and weighed against two named alternatives, an interval tree and a bucketed index: order preservation is the deciding property, because a faster structure that returned a different order would make the fast path and the obvious path disagree — which is precisely what the layer's own tests compare.

**Status.** NOT STATED · date not stated · ratifier not stated

**Home.** `cowork_layer1_note_model_design.md:204-206`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§9** — `## 9. Architecture decisions (with the alternatives we weighed)` (heading at line 194). A delegation at ARCHITECTURE.md:1517 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** One of the four architecture decisions of the as-built Layer-1 specification. The order-equivalence it was chosen for is the acceptance test: the index must return exactly what a linear scan returns, over many random and deliberately awkward spans, on every test piece. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-518 — The planned cue-note flag was specified and then REMOVED: after import a cue note cannot be told from a muted note, and the does-it-sound flag already covers both

> - **A field we specified then removed:** we had planned a "cue note" flag, then removed it — once a MuseScore score
>   is imported, a cue note can no longer be told apart from an ordinary muted note, and the existing "does it sound"
>   flag already excludes both.

**In plain words.** The note model was going to record whether a note is a cue note. That field was removed, because once a score has been imported a cue note is indistinguishable from an ordinary silent note, and the flag that says whether a note plays already excludes both.

**Why.** Stated with the correction: the distinction the field would have carried does not survive import, so the field could only have recorded a guess. Recording the removal rather than deleting the plan keeps the reason available to anyone who proposes the field again.

**Status.** NOT STATED · date not stated · ratifier not stated

**Home.** `cowork_layer1_note_model_design.md:261-263`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **§13** — `## 13. Background: what Architectural Layer 1 replaces, and corrections on record (NOT needed to understand the layer)` (heading at line 252). A delegation at ARCHITECTURE.md:1517 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it RECORDS FINDINGS**.

**Provenance.** Recorded in the specification's own background section, which the document keeps separate so that the layer's description contains only what the layer is. It is why the per-note sounds flag is documented as covering muted notes and imported cue notes together — one flag for two cases, by necessity rather than by convenience. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-519 — Only TIES join written notes into one sounding note — slurred notes stay separate, whatever their pitches

> - **Tie-resolved.** A group of tied notes is treated as **one single held note** — one start time and one end time —
>   instead of as the several separate written notes it appears to be. (Slurred notes are *not* merged this way: a
>   slur marks phrasing, not one continuous sound, so slurred notes — whether of the same pitch or of different
>   pitches — remain separate notes, each with its own start time, end time, and duration. Only ties join written
>   notes into one sounding note; slurs do not.)

**In plain words.** A group of tied notes becomes one held note with one start and one end. A slur does not do this: slurred notes remain separate notes, each with its own start, end and duration, whether or not they share a pitch.

**Why.** Stated with the rule: a slur marks phrasing, not one continuous sound, so merging across one would invent a held note the score does not contain. The tie merge has the opposite justification — the held parts of a tie genuinely sound, so counting them separately counts the same sustained sound more than once.

**Status.** NOT STATED · date not stated · ratifier not stated

**Home.** `cowork_layer1_note_model_design.md:43-47`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§1** — `## 1. Introduction & purpose` (heading at line 26). A delegation at ARCHITECTURE.md:1517 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** The first of the two founding ideas of the as-built Layer-1 specification, stated with its exclusion. Registered because the exclusion is the load-bearing half and no register entry carried it: **D-038** records that tied notes are one event and does not say what does not merge. The unrelated split-note case, where a slur IS the joiner, is **D-147**. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-520 — Widening the loaded span was built DECOUPLED from the whole-score-read fix — superseding the recorded framing that the two were one coupled change

> - **The build currently reads the whole score even when only part of it is queried** — an **interim** behaviour, not
>   the target. The product is selection-based (`cowork_bounded_context_design.md`): the target is *build over the
>   selection, then extend on request*. Loading the whole score is the degenerate case (selection = score) and is what
>   keeps the batch-testing path (the offline corpus harness, `batch_analyze`) unchanged. The *extend* operation (§3) is **now built** (Phase-1a), so the whole-score
>   build no longer masks a missing capability — it only means *extend*'s interim implementation re-walks the whole score
>   rather than a span-scoped slice. The earlier framing that "fixing the whole-score build and building *extend* are one
>   coupled change" is **superseded**: *extend* was built **decoupled** (Phase-1a, whole-score re-walk, byte-identical),
>   with the span-scoped walk deferred to Phase-1b. The build-selection + extend **contract** is what every layer above
>   is written against, so the interim is invisible to them.

**In plain words.** The note model still reads the whole score even when only part of it is asked about. That is interim. The operation that widens the covered music was expected to have to wait for it; it was built first instead, re-walking the whole score and filtering to the enlarged span, which produces exactly what a fresh build over that span would. The span-scoped walk is what remains.

**Why.** The decoupling is justified by the equivalence rather than asserted: the interim implementation is byte-identical to a fresh build over the enlarged span, so the layers above are written against the contract and cannot see the difference. The superseded framing is recorded rather than deleted, which is what lets a reader see that the coupling claim was tested and dropped.

**Status.** DEFERRED · date not stated · ratifier not stated

**Home.** `cowork_layer1_note_model_design.md:230-238`  — homed in a RATIFIED CONTRACT SURFACE the owning `ARCHITECTURE.md` section points to: a proper home (the fifth home case, user-ratified 2026-08-02 at OI-268; its unit narrowed from the document to the SECTION by the user's ruling of 2026-08-03 — see *Home section* below where the entry carries one).

**Home section.** **§11** — `## 11. Risks & technical debt` (heading at line 221). A delegation at ARCHITECTURE.md:1517 reaches this section. Decided by **D-430, the section-level unit — the delegation reaches this section and it STATES RULES**. Home class **re-classified 2026-08-03** (the one re-classification pass) from `gap` to `contract-home`; the former class is kept here rather than overwritten (#12).

**Provenance.** Recorded in the as-built specification's risks section, which states plainly that the whole-score read is an interim behaviour and not the target. The bounded-context contract it is written against is `cowork_bounded_context_design.md` (**D-260**…**D-265**); the remaining half is the span-scoped walk the document names Phase-1b. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-569 — Collecting, filtering and weighting are THREE separate responsibilities; the collection layer collects and annotates, and does nothing else

> ## §1 — Intended role (the single responsibility) — REVISED per user review 2026-06-21
> **Collect — and only collect — every sounding note in a region, annotated, losslessly, by ONE path.** It is the
> boundary between the engraving model (Score/Segment/Note) and the analysis types. It answers exactly one factual
> question: "for region `[startTick, endTick)`, what notes sound?" — and returns the **note set**, each note
> annotated with the facts needed downstream (pitch, tpc/spelling, staff, voice, onset, offset, in-region
> duration, `isGrace`, `plays`, `visible`, staff-eligibility). It must **NOT** filter (drop grace/non-playing/
> invisible), **NOT** weight or aggregate into pitch-class evidence, **NOT** select a bass, and **NOT** make any
> harmonic/segmentation/key decision. Those are *separate* responsibilities (see §5):
> - **Collection** (this layer): the facts — every sounding note, annotated, preserved, one path.
> - **Filtering** (a distinct, explicit decision): which annotated notes are eligible for harmonic analysis.
> - **Weighting** (a distinct derived layer): the pitch-class evidence + bass, computed as a *view* over the
>   collected notes — never replacing them.

**In plain words.** Finding out which notes sound in a stretch of music, deciding which of them the harmonic analysis should consider, and turning them into weighted evidence are three different jobs. The first is a matter of fact, the second a decision, the third an interpretation. The collection layer answers only the factual question and hands the notes on annotated with everything a later step could need.

**Why.** The reason is given as the consequence of merging them, which the document traces at the code: doing all three in one pass is what forces the notes to be thrown away, what makes the dropping silent, and what produced two divergent collection paths. The corrected role was written on the user's own review of 2026-06-21, whose three comments the document records — no multiple paths, collect don't drop, separate collecting from weighting.

**Status.** LIVE · decided 2026-06-21 · ratified by user

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer1_tone_collection_design.md:33-44`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **the opening block (above the first section heading)** — `# Layer 1 — TONE COLLECTION — Design Document (for user sign-off)` (heading at line 1). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_layer1_tone_collection_design.md`, the Layer-1 tone-collection design put to the user for sign-off. Read in full by READ WAVE 4, 2026-08-04. The section is marked *REVISED per user review 2026-06-21* and records the three review comments it was corrected against. **The decision LANDED**: the note model carries the facts losslessly and the weighting survives as a derived view over it — the entries for that as-built state are **D-039** (ineligible notes kept and flagged, never dropped) and **D-038** (spans answered by overlap with no horizon), both homed in `ARCHITECTURE.md`. This entry is the RULE those two implement, with its own defense.

### D-570 — An upstream layer's correctness oracle is the SCORE, not the Roman-numeral ground truth

> ## §6 — Correctness oracle for this layer (it is NOT the RN oracle)
> This layer is upstream of key and chord, so its correctness is judged against the **score**, not DCML/music21:
> does it collect exactly the notes a human reading the score would say sound in `[start,end)` (right staves,
> right sustains, right filters), with bass and weights that faithfully reflect the notation? Completeness = all
> note cases handled (sustains past the cap, ties, tuplets, grace, cross-staff, multi-voice unisons, pedal,
> invisible/non-playing). The audit builds score-level test cases for each; the per-event tiered metric does **not**
> cover this layer.

**In plain words.** Because this layer sits before any decision about tonality or chords, whether it is right is judged against the notation itself: does it collect exactly the notes a musician reading the score would say are sounding in that stretch, from the right staves, with the right sustains. The published harmonic analyses cannot judge it, and the per-event agreement measurement does not reach it.

**Why.** It follows from what the layer decides: a layer that makes no harmonic claim cannot be graded by a harmonic annotation, and grading it by one would make an unrelated downstream disagreement look like a collection error. The document states the completeness condition beside it — every note case handled, enumerated — so the oracle is checkable rather than a sentiment.

**Status.** LIVE · date not stated · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `cowork_layer1_tone_collection_design.md:198-204`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Home section.** **“§5”** — `## §5 — Proposed target design (for ratification/amendment)` (heading at line 171). Not reached: the document's delegation is graded before any section question arises. Decided by **clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade**.

**Provenance.** `cowork_layer1_tone_collection_design.md`, the Layer-1 tone-collection design put to the user for sign-off. Read in full by READ WAVE 4, 2026-08-04. Recorded as the document's §6, headed in terms *it is NOT the RN oracle*. The record states no date and no ratifier for this clause. It is the layer-level statement of the standing rule that ground truth is itself an instrument (`CLAUDE.md` #21).

### D-594 — Bass-as-root promotion is SHELVED WITH EVIDENCE — the information that disambiguates the third-above reading is non-local, so no local discriminator can exist

> - **The information that disambiguates the third-above reading is NON-LOCAL, so no local
>   discriminator can exist — the approach is shelved, the problem is not.** Where C-E-G may be a C
>   chord or an E-minor chord inside something larger, and A-C-E likewise, nothing this scorer can see
>   at the moment of scoring — the sounding pitch classes, their weights, the templates, the key —
>   separates the two readings. What separates them is the surrounding music: the following chord's
>   root, the preceding chord's identity, and whether the bass falls on a strong beat.

**In plain words.** When the notes sounding are C, E and G, the reading could be a C chord or an E-minor chord embedded in something else; the same holds for A, C, E. Nothing the chord scorer can see at that moment — the notes, their weights, the chord templates, the key — separates the two. What separates them is the music around it: the next chord's root, the previous chord's identity, and whether the bass falls on a strong beat.

**Why.** Measured, twice, and both attempts regressed: a simple discriminator stack moved the wrong-root count up on the primary corpus, and a more elaborate one moved it up further, with the wider score-gap overpowering its own added tightenings. The document also records that the cases where the third-above reading is CORRECT are indistinguishable from the cases where it is wrong on local evidence, and that a sample of the regressions flipped one wrong answer into a different wrong answer.

**Status.** SHELVED WITH EVIDENCE · decided 2026-05-15 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1193-1207`

**Provenance.** `docs/iter90_bass_as_root_promotion_shelved.md`, the 2026-05-15 record of the shelved bass-as-root promotion attempt. Read in full by READ WAVE 5, 2026-08-04. The document's own Outcome section records that no code change was committed and the working tree was reverted to the prior commit. It recommends two future angles — a pass that reads the surrounding regions' roots, or a temporal-context gate keyed on the neighbouring roots — neither of which is scheduled at HEAD, and this entry schedules neither. The shelving is of the LOCAL-GATE approach, not of the problem. The record states no ratifier. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)). Routed as the ruling names it, to `docs/scoring_model.md` §8, the section that exists to collect this surface's constraints and dead ends — SHELVED-WITH-EVIDENCE STATUS AND THE EVIDENCE BOTH INTACT, and the ⚠ LEGACY subject stated at the new home so no reader takes it for a statement about the production estimator. The two future angles are carried across as neither scheduled nor endorsed, which is what the record says of them. THE REGRESSION COUNTS ARE NOT CARRIED ACROSS (D-431): the direction and the shape of each failure are stated and the numbers stay in the record. FORMER HOME, PRESERVED (#12): `docs/iter90_bass_as_root_promotion_shelved.md:65-67`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 58, "section": "## Why no local discriminator worked", "label": "“Why no local discriminator worked”", "delegated": null, "delegation": "ARCHITECTURE.md:4141", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "The discriminator the analyzer can see locally — pcSet, pcWeights,
templates, key — does not contain the information that disambiguates
these. The information that does is **non-local**:" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-595 — A chord-level change is not confined to the cases it fires on: chord identity drives boundary placement, so it produces downstream RE-SEGMENTATION artifacts in regions it never touched

> - **A chord-level change is NOT confined to the cases it fires on: chord identity drives boundary
>   placement, so it produces downstream RE-SEGMENTATION artifacts in regions it never touched.**
>   Where one region ends and the next begins depends partly on what the chords are, so changing one
>   chord's identity — even changing it correctly — makes the adjacent regions re-merge differently,
>   and readings that were right can become wrong where the change never looked. **Counting only the
>   cases a change fires on therefore understates its effect, and this is structural rather than a
>   condition that can be tightened away.** *Why it is stated here as a standing constraint:* it was
>   measured at the attempt above, where some of the regressions were not gate fires at all; and it is
>   the reason the governing regression stop is an EXPLAINED PER-RUN DIFF rather than a count — an
>   effect outside the cases a change fires on is exactly what an enumeration of added and removed
>   runs catches and a count does not.

**In plain words.** Where one chord ends and the next begins is decided partly by what the chords are. So changing one chord's name — even changing it correctly — makes the program cut the music differently nearby, and readings that were right can become wrong in places the change never looked at. Counting only the cases a change fires on therefore understates its effect.

**Why.** Measured at the attempt that produced it: of the regressions the second variant caused, some were not cases the mechanism fired on at all. The document states the consequence plainly — this is structural, not a condition that can be tightened away.

**Status.** LIVE · decided 2026-05-15 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `docs/scoring_model.md:1208-1218`

**Provenance.** `docs/iter90_bass_as_root_promotion_shelved.md`, the 2026-05-15 record of the shelved bass-as-root promotion attempt. Read in full by READ WAVE 5, 2026-08-04. Recorded in the document's Cascade-from-segmentation section. It is the measured reason the block-(A) regression stop is an EXPLAINED PER-RUN DIFF rather than a count — `CLAUDE.md` gate block (A) requires every added and removed run to be enumerated, which is what catches an effect outside the cases a change fires on. Stated on the LEGACY segmenter (greedy-expand); whether the joint estimator's modelled segmentation shows the same coupling is NOT stated here and is not asserted. The record states no ratifier. ★ HOMED 2026-08-08 (CC, executing the user's document-route ruling of 2026-08-08, route (ii)) into `docs/scoring_model.md` §8, beside the shelving it was measured at, with the ⚠ LEGACY subject and the not-asserted clause both stated at the new home. THE REGRESSION COUNT IS NOT CARRIED ACROSS (D-431). FORMER HOME, PRESERVED (#12): `docs/iter90_bass_as_root_promotion_shelved.md:86-91`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 84, "section": "## Cascade-from-segmentation effect", "label": "“Cascade-from-segmentation effect”", "delegated": null, "delegation": "ARCHITECTURE.md:4141", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "D-432, the delegation bar — the strongest delegation is a provenance-attribution, which the bar does not admit", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "A subtler issue: when a chord identity changes (e.g. the gate flips
`Dm/Bb → Bb6` correctly at one region), the bridge's greedy-expand
re-merges adjacent regions differently because chord identity drives
boundary placement. Some of the +22 regressions are not direct gate
fires but **downstream re-segmentation artifacts** in regions the gate
never touched. This is structural, not a tunable local condition." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance is recorded in this field and NOT in the specification text (the OI-330 / OI-328 lesson).

### D-606 — The binding metric for the modulation detector is modulation CORRECTNESS — explicitly not the agreement percentage, which the change under test can game

> - **THE BINDING METRIC FOR A MODULATION DETECTOR IS MODULATION CORRECTNESS — explicitly NOT the
>   agreement percentage** (2026-06-14; the record states no ratifier). A change that decides where
>   the music changes key is judged on whether the key changes it commits are real ones (precision)
>   and whether it finds the real ones (recall) — the track rate together with the de-masked partial
>   split — and never on the overall agreement percentage. *Why:* stated with the decision — the
>   agreement percentage is **gameable by the change under test**, so it cannot be that change's own
>   bar. It is the same defect the abstain-aware convention above exists against on the root axis: an
>   agreement percentage a behaviour change can move without analysing anything better is not a
>   measurement of that change. The honesty measurement named with it is the de-masking diagnostic,
>   which exposes a committed home-key label being credited against a ground-truth local key.

**In plain words.** A detector that decides where the music changes key is judged on whether the key changes it commits are real ones and whether it finds the real ones — not on the overall agreement percentage, which a detector can raise without detecting anything better.

**Why.** Stated with the decision: the agreement percentage is gameable by the change under test, so it cannot be the bar for that change. It is the same defect the abstain-aware convention (**D-212**) exists against on the root axis — an agreement figure that a behaviour change can move without analysing anything better is not a measurement of that change.

**Status.** LIVE · decided 2026-06-14 · ratifier not stated

**Entry ratified.** 2026-08-04 · by user

**Home.** `CLAUDE.md:839-848`  — a decision about how the work is done, not about the system; this is its correct home.

**Provenance.** `docs/stage4d_local_modulation_design.md`, the Stage-4d local-modulation design, DRAFT and ratification-gated, 2026-06-14. Read in full by READ WAVE 5, 2026-08-04. Recorded in the staged-build section, which also names the de-masking diagnostic as the honesty measurement — it exposes a committed home-key label credited against a ground-truth local key. ⚠ The detector is on the LEGACY key path and the staged build described was never carried past its own gate on the arm that now runs; the rule about which metric may bind is not legacy-scoped. The record states no ratifier. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). Ruled a GRADING CONVENTION — the binding metric for a modulation detector is modulation correctness — and homed in `CLAUDE.md` gate block (A) beside D-604, where the abstain-aware convention it cites already lives; the home text cites that convention rather than restating it (#6). Written in the gate block's own voice and with its defense. The D-645 licence covers `CLAUDE.md` for homing acts. The edit is ADD-ONLY. FORMER HOME, PRESERVED (#12): `docs/stage4d_local_modulation_design.md:78-80`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 74, "section": "## §5 — Staged build (measure-first, per discipline)", "label": "“§5”", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**The binding metric is modulation
  CORRECTNESS (track-rate + the de-masked partial split), NOT the gameable rn_agree** — a span we commit
  must be a real DCML modulation (precision) without missing the real ones (recall)." The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

### D-625 — Spelling presence is tested with the validity predicate, never with a non-negative test — the flat side of the line of fifths is negative and a non-negative guard silently drops it

> - **Spelling presence is tested with the VALIDITY PREDICATE, never with a non-negative test.** The
>   shared line-of-fifths primitive the spelling-pin above reads — the one interpreter, not a
>   per-layer copy — represents a spelling as a signed position on the line of fifths, and its
>   presence test is `tpcIsValid()`, **never** `tpc >= 0` and never `tpc != -1`. *Why:* established
>   at the source rather than asserted — the flat side of the line of fifths is **negative** (down to
>   the triple-flat spellings), so a non-negative guard silently discards every heavily flattened
>   spelling; and the value a `!= -1` guard treats as absent is itself a **legitimate** spelling. The
>   honest bound is recorded with the rule: the validity test cannot tell a real flattest spelling
>   from a default-initialised field, and what actually keeps an absent value out is the build-path
>   invariant, not this predicate. §5.14, which specifies the enharmonic disambiguation this
>   primitive serves, points here and does not restate it (#6).

**In plain words.** How a note is spelt is stored as a position on the line of fifths, and that position is negative for the flattest spellings. Code that checks whether a spelling is present by testing for a non-negative number therefore throws away every heavily-flattened spelling — including one that happens to share its number with the field's empty value. The validity test is the correct check.

**Why.** Established at the source: the mapping, the constant, the real range and the two named flat-side spellings were all read in the engraving header, and the consequence of the wrong guard is derived from them rather than asserted. The design also states what the check does NOT do — the validity test cannot tell a real flattest spelling from the field's default — and names the build-path invariant as the thing that actually keeps an absent value out, which is the honest bound on the rule.

**Status.** LIVE · decided 2026-06-26 · ratifier not stated

**Home.** `ARCHITECTURE.md:2011-2021`

**Provenance.** `cowork_tpc_capability_design.md` §1, the shared spelling primitive's detail design, BUILT as a capability with no production consumer. Read in full by READ WAVE 6, 2026-08-04. The same section records that the chord scorer's existing inline spelling reads carry the wrong guard and that correcting them rides the fold into the primitive — an open unification question the document flags rather than closes. The record states no ratifier. ★ HOMED 2026-08-07 (CC, the owner-rulings homing wave, executing the user's ruling of 2026-08-07 recorded at `cowork_owner_rulings_2026_08_07.md`). The ruling routes it to THE SECTION SPECIFYING THE SHARED LINE-OF-FIFTHS PRIMITIVE — the Layer-4 section per the record — with §5.14 pointing, and it carries a STOP: STOP IF THE PRIMITIVE IS SPECIFIED ELSEWHERE. ★ THE STOP WAS DISCHARGED BEFORE WRITING AND DID NOT FIRE: `ARCHITECTURE.md` names the primitive in exactly three places and specifies it in none — §3.3's terminology note DEFINES the term Layer 1.5 and lists the primitive among its two views; the Layer-4 section names it as the interpreter the symmetric-root spelling-pin reads through and states the one-interpreter rule about it; and Layer 1's own derived-views list does not mention it at all. Written into the Layer-4 section in that section's own voice, with its defense and with the honest bound the record states (the validity test cannot tell a real flattest spelling from a default-initialised field). §5.14 gains a POINTER, never a copy (#6). ★ AN ADJACENT FACT THE STOP SURFACED IS ROWED AND LEFT, not acted on: the sibling Layer-1.5 primitive is sited at Layer 1 with its reason stated in full, so the two Layer-1.5 primitives sit in different sections — `OPEN_ITEMS.md` OI-347. FORMER HOME, PRESERVED (#12): `cowork_tpc_capability_design.md:39-43`. FORMER CLASS, PRESERVED (#12): `gap`. FORMER HOME-SECTION BLOCK, PRESERVED (#12) — removed because the home-class criteria do not reach this entry at its new home: {"heading_line": 20, "section": "## 1. The shared tpc-interpretation primitive (the capability)", "label": "§1", "delegated": null, "delegation": "named in no user-ratified surface", "states_rules": null, "verdict": "EXCLUDE", "decided_by": "clause (a), the fifth home case (OI-268) — this document is named in none of the three user-ratified surfaces, so no delegation exists to grade", "former_class": "gap", "class_before_phase1q": "gap", "class_before_phase1r": "gap"}. THE FORMER VERBATIM, PRESERVED WHOLE (#12): "**Validity & mapping (verified at source, 2026-06-26).** Line-of-fifths position = `tpc − TPC_C` with `TPC_C = 14`
(+1 tpc = +1 fifth; `pitchspelling.h`). Sharp/flat sense = the sign of that offset. **The primitive must test presence
with `tpcIsValid()` (= `−8 ≤ tpc ≤ 40`), never `tpc >= 0` / `tpc != −1`:** the flat side of the line of fifths is
**negative** (`TPC_F_BB = −1`, down to `TPC_F_BBB = −8`), so a `>= 0` guard silently drops every double-flat-ish
spelling — and `−1` is a *legitimate* spelling (Fbb), not "absent."" The verbatim above is RE-TAKEN from the new home, read out of the file rather than transcribed. Provenance — the wave and its dispatch — is recorded in this field and NOT in the specification text, on the ruling record's own instruction: a file name written into a governing document reads as a new naming and moves a measured population (the OI-330 / OI-328 lesson).

