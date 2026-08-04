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

**Home.** `ARCHITECTURE.md:1244`

**Provenance.** ARCHITECTURE.md:1162-1173 (Layer 1 - Built+Live)

### D-038 — Tied notes are one event; spans are answered by overlap with no horizon

> Tied groups are merged into **one** span/onset (via the DOM `firstTiedNote`/`lastTiedNote`/`playTicksFraction`); spans are true `[onset,release)` answered by **overlap with no horizon** (the old 4-whole-note backward cap is gone).

**In plain words.** A note tied across a barline counts once, starting where it was struck and ending where it stops. Asking what is sounding at a moment looks back as far as needed, with no arbitrary cut-off.

**Why.** Stated constraint, ARCHITECTURE.md:1173: tied groups are merged into one span and one onset via the score model's own tie links, and spans are answered by overlap with no horizon - which retires the old four-whole-note backward cap that could miss a longer sustain.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1244`

**Provenance.** ARCHITECTURE.md:1173; the behaviour change it caused is the ratified trade-off at :1026-1032

### D-039 — Ineligible notes are kept and flagged, never dropped

> Grace / non-playing / invisible / staff-ineligible notes are **kept and flagged, never dropped**.

**In plain words.** Notes that should not drive the analysis - grace notes, hidden notes, notes on a non-musical staff - are still recorded, marked as such. Nothing is thrown away.

**Why.** Stated constraint, ARCHITECTURE.md:1173, and #12: a dropped note is information lost for good, so ineligible notes are kept and flagged and each consumer decides what to do with them.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1244`

**Provenance.** ARCHITECTURE.md:1173; the standing no-information-loss principle is CLAUDE.md #12

### D-040 — The tie-unresolved atoms are republished additively for the joint estimator

> `notatedNotes()` republishes the tie-UNRESOLVED atoms — EVERY notated note incl. tie continuations, each with its OWN notated span, a `tieContinuation` flag, a `hasFermata` flag, and `resolvedIndex` linking to its tie-resolved `NoteEvent`

**In plain words.** As well as merging tied notes, the note reader also publishes them separately, each with a marker saying it is a continuation. The joint estimator needs both views.

**Why.** Stated constraint, ARCHITECTURE.md:1173: the tie-unresolved atoms carry the facts the tie-resolved surface discards and the joint estimator's event lattice and emission covariates need; publishing them additively keeps every existing consumer byte-identical.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1244`

**Provenance.** ARCHITECTURE.md:1173 records it as 'Purely additive' under the OI-180 dual-path sanction

### D-517 — The note model's span query uses a start-time-ordered list plus a running latest-end-time tree, chosen because it is the simplest structure that is fast AND returns notes in scan order

> - **A numeric look-up index (a start-time-ordered list plus a "latest end-time so far" tree).** Alternatives
>   considered: an interval tree, a bucketed index. Chosen: this structure — it is the simplest one that answers the
>   span-of-time queries quickly *and* returns notes in exactly the same order a plain left-to-right scan would.

**In plain words.** Asking which notes sound between two moments must stay fast on a whole piece. The structure chosen is the simplest one that answers quickly while returning the notes in exactly the order a plain left-to-right scan would.

**Why.** Stated with the decision and weighed against two named alternatives, an interval tree and a bucketed index: order preservation is the deciding property, because a faster structure that returned a different order would make the fast path and the obvious path disagree — which is precisely what the layer's own tests compare.

**Status.** NOT STATED · date not stated · ratifier not stated

**Home.** `cowork_layer1_note_model_design.md:204-206`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** One of the four architecture decisions of the as-built Layer-1 specification. The order-equivalence it was chosen for is the acceptance test: the index must return exactly what a linear scan returns, over many random and deliberately awkward spans, on every test piece. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

### D-518 — The planned cue-note flag was specified and then REMOVED: after import a cue note cannot be told from a muted note, and the does-it-sound flag already covers both

> - **A field we specified then removed:** we had planned a "cue note" flag, then removed it — once a MuseScore score
>   is imported, a cue note can no longer be told apart from an ordinary muted note, and the existing "does it sound"
>   flag already excludes both.

**In plain words.** The note model was going to record whether a note is a cue note. That field was removed, because once a score has been imported a cue note is indistinguishable from an ordinary silent note, and the flag that says whether a note plays already excludes both.

**Why.** Stated with the correction: the distinction the field would have carried does not survive import, so the field could only have recorded a guess. Recording the removal rather than deleting the plan keeps the reason available to anyone who proposes the field again.

**Status.** NOT STATED · date not stated · ratifier not stated

**Home.** `cowork_layer1_note_model_design.md:261-263`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

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

**Home.** `cowork_layer1_note_model_design.md:43-47`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

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

**Home.** `cowork_layer1_note_model_design.md:230-238`  ⚠ **home is not the specification that owns it** — a documentation gap; see `OPEN_ITEMS.md`.

**Provenance.** Recorded in the as-built specification's risks section, which states plainly that the whole-score read is an interim behaviour and not the target. The bounded-context contract it is written against is `cowork_bounded_context_design.md` (**D-260**…**D-265**); the remaining half is the span-scoped walk the document names Phase-1b. Entered by the phase-1 reads WAVE 3 (dispatch `cc_instruction_reads_3.md`) from the full read of the document. NOT ratified — it enters with the record's own status and goes to the user in this wave's ratification queue.

