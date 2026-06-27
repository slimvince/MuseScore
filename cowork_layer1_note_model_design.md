# Architectural Layer 1 — the NOTE MODEL — Architecture & Design

> **Status: AS-BUILT (built, reviewed, and accepted; on the project's own copy of the MuseScore source code).**
> Source-commit identifiers, for traceability only: `edd33901ed`, `e30bb45a4f`, `4055f89082`, `257b55c9f4`,
> `4bce14e804`. This document follows the standard section structure in `cowork_design_doc_template.md`. The order in
> which the code was built ("coding increments") is delivery sequencing and is recorded in the delivery plan, not in
> this architecture document. *(Two template sections do not apply to this architectural layer: "Deployment view"
> and "Human-interface design" — Architectural Layer 1 is backend analysis code, with no separate hardware
> deployment and no user interface.)*

## 1. Introduction & purpose
**What Architectural Layer 1 is.** It produces a clean, complete list of the notes that actually sound in the music
being analysed, together with the facts about each note that the later architectural layers need. It is built once
and is then read by every later architectural layer; no later architectural layer reads the raw MuseScore score
again.

**What music Architectural Layer 1 operates on.** It never works on "a whole score" in the abstract. It works on
**the part of the score that the user has selected for analysis** — which may be a single note or chord, a run of
several measures, or, in the worst case, the entire piece. (Reading an entire score from beginning to end happens
only in our offline testing of the analysis quality; it never happens in the shipping product.)

**Why Architectural Layer 1 exists.** It gives the whole analysis system **one** shared, accurate reading of the
notes, so that every later architectural layer works from the same correct note list instead of each computing its
own. (What this improves on is in Section 13.)

**Two ideas Architectural Layer 1 is built on:**
- **Tie-resolved.** A group of tied notes is treated as **one single held note** — one start time and one end time —
  instead of as the several separate written notes it appears to be. (Slurred notes are *not* merged this way: a
  slur marks phrasing, not one continuous sound, so slurred notes — whether of the same pitch or of different
  pitches — remain separate notes, each with its own start time, end time, and duration. Only ties join written
  notes into one sounding note; slurs do not.)
- **Lossless.** Architectural Layer 1 **keeps every note, and every fact about each note that any later step might
  need, and never discards any of it or reduces it to a summary.** Specifically, the three things it refuses to
  lose are: (a) any note at all — even a note that will not feed tonal analysis is kept, only marked (see "what we
  keep but mark," below); (b) each note's exact pitch, voice, and timing — the real notes are never replaced by a
  count, an average, or a pitch histogram; (c) the separation between *which notes are present* and *what a later
  architectural layer decides about them* — deciding about the notes (keys, chords, function) is a separate,
  reversible step done in a later architectural layer.

**What Architectural Layer 1 keeps but marks (not every note in a score should feed tonal analysis).** Three kinds
of note should not contribute to key-and-chord reasoning: notes that are **muted** (set not to play), notes that
are **invisible**, and every note that sits on a staff which is not tonal — drum/percussion staves, the chord-symbol
track, and hidden staves. Architectural Layer 1 **keeps all of these notes and sets a flag on each one saying which
case it is; it never drops them.** Choosing to *ignore* such a note is a separate step done later (the summary views
described below skip any note that is muted, invisible, or on a non-tonal staff). Keeping the notes means a later
architectural layer can still see that they were present.

**Scope — what Architectural Layer 1 does:** read the selected music once; resolve ties; record the per-note facts;
and answer the question "which notes are sounding during a given span of time?"

**What Architectural Layer 1 explicitly does NOT do** (stated because each boundary matters):
- It does **not** weight, average, or reduce notes to pitch evidence — that is done by the summary views, on top of
  it, and by later architectural layers.
- It does **not** cut the music into spans (that is Architectural Layer 2) and makes **no** key, chord, or function
  judgement (that is Architectural Layer 3 and later).
- It does **not** drop any note — it keeps every note and only marks the ones that should not feed tonal analysis.
- It does **not** decide *when* to build or rebuild itself, and does **not** watch for score edits — it builds, or
  widens, only when the caller asks.
- It does **not** decide that more music is needed — it supplies a widened span on request, but the request comes
  from a later architectural layer.

## 2. Constraints
- **Lossless, and read-only toward the music:** keep every note, change no note, summarise no note.
- **One reading for the whole analysis system:** there is a single note model; no other code re-reads the raw score.
- **No limit on how far backwards in time a query searches:** when asked which notes sound during a span of time,
  the answer must include notes that started **earlier in time** than that span and are still sounding when it
  begins, no matter how much earlier they started.
- **Operates on the user's selected part of the score, at any selection size and in any musical style** (it makes no
  assumption about style); it must stay fast even when the selected music is the entire piece.
- **The analysed span of music can be widened on request.** A later architectural layer — Architectural Layer 3
  (key/mode) in particular — sometimes needs more music than the user's selection, for example to see what key the
  music was in just **earlier in time than the point where the selection begins**. Architectural Layer 1 can be
  asked to **widen the span of music it covers — earlier in time, later in time, or both — and to take in the extra
  notes.** Architectural Layer 1 is the *supplier* of the extra music; deciding that more music is needed is the
  requesting architectural layer's responsibility, not Architectural Layer 1's.
- **Architectural Layer 1 is not responsible for noticing when its note model has become out of date.** When the
  user edits the score, Architectural Layer 1 does not detect the edit and does not decide that its note model is
  stale. Deciding that the note model must be rebuilt, and requesting that rebuild, is the caller's responsibility
  (the score editor / integration code). Architectural Layer 1 only builds the note model, or widens it, when it is
  told to.
- **Fixed for the architectural layers above it:** once the note model is built, its results do not change; the only
  permitted code changes are speed improvements that return *identical* results.

## 3. Context & scope (external view)
**What Architectural Layer 1 reads (its inputs):** the user-selected portion of the MuseScore score, plus the
notation system's tie information (which written notes are tied to which).
**What Architectural Layer 1 offers (the operations other code calls):**
- *Build the note model* from the selected music (reading it once).
- *Return every note in the note model*, in a fixed order — earliest start time first.
- *Which notes are sounding during the span of time from A to B?* — returns the notes whose own sounding span
  overlaps the span A-to-B, including notes that started **earlier in time** than A and are still sounding at A;
  there is no limit on how far **backwards in time** it searches.
- *Which notes start within the span of time from A to B?*
- *Widen the covered span of music* — extend the analysed range **earlier in time and/or later in time** than the
  range first built, and take in the additional notes, for a later architectural layer that needs more musical
  context than the user's selection provided. This is the **extend** operation of the bounded-context contract —
  designed in full in `cowork_bounded_context_design.md` (build over a selection, then extend on request; append-only;
  clamp at the score boundary and report it). **(Built — Phase-1a: `extend(Direction, int)`, `boundaryReached()`, and
  the loaded/selection-span accessors exist in `note_model.h` and behave to the contract — append-only, exactly one
  step, no convergence loop, clamp at the score boundary and report it. It was built *decoupled* from the §11
  whole-score-load fix: the interim implementation itself re-walks the whole score and re-filters to the enlarged
  loaded span (byte-identical to a fresh build over that span); the span-scoped walk is the deferred Phase-1b.
  Architectural Layer 3's reach-back is written against it.)**
**Who uses Architectural Layer 1 (its consumers):** the derived summary views that condense notes into pitch
evidence for scoring (`weightedPcView`, `soundingAt`); the Architectural Layer 2 slicer; the Architectural Layer 3
key/mode code. **What Architectural Layer 1 deliberately knows nothing about:** keys, chords, and function — it sits
beneath all musical judgement.

**Implementation (source files):** the note model and its look-up index are in
`src/composing/analysis/notemodel/note_model.{h,cpp}` (`NoteModel`, `NoteQueryIndex`); the derived summary views are
in `src/composing/analysis/engravingbridge/regiontonecollector.{h,cpp}` and `regiontoneprimitives.cpp`
(`weightedPcView`, `soundingAt`).

## 4. Solution strategy
Read the user-selected music exactly once into a single list of notes ordered by start time. For each group of tied
notes, record one note that runs from the first tied note's start time to the last tied note's end time, so a held
sound is one note with one start time, not several separate notes. Keep every note; for the notes that should not
feed tonal analysis, set a marking flag rather than dropping them; and answer span-of-time questions directly from
the list. The result is that the notes the analysis is tuned against and the notes the analysis is measured against
are the same notes: a held sound is one note, a long note is never missed, and no note is counted twice.

## 5. Building-block view (static / internal structure)
- **A note record** — one tie-resolved note together with its facts (the eleven fields listed in Section 7).
- **The note model** — owns the list of note records ordered by start time, a borrowed reference to the source
  MuseScore score, and a numeric look-up index. Building the note model walks every staff, every voice, and every
  time-position (including grace notes), resolves ties, records the per-note facts, and sorts the records by start
  time.
- **The numeric look-up index** — a structure that lets the two span-of-time questions ("sounding during A-to-B",
  "starting within A-to-B") be answered quickly even when the selected music is large, instead of scanning the whole
  list of notes every time. It is built once and stores only numbers (each note's start and end time-positions), so
  it copies cheaply together with the note model.
- **Derived summary views (a separate module, not part of Architectural Layer 1's core):** `weightedPcView` condenses
  a span of notes into weighted pitch evidence for scoring; `soundingAt` reports the notes sounding at one instant
  in time. These are read-only summaries built *on top of* the note model — deliberately lossy convenience views,
  with the lossless note model still underneath them.

## 6. Runtime view (scenarios)
- **Building the note model:** given the user-selected music, produce the note model once (walk the music → resolve
  ties → record the per-note facts → sort by start time → build the look-up index).
- **A span-of-time query:** a later architectural layer asks "which notes sound between time-position A and
  time-position B?" and receives them ordered by start time.
- **A held sound made of tied notes:** three tied quarter-notes followed by a different note become **two** notes —
  one long held note and the following note — not four notes, and the held note is not counted three times.
- **A note carried in from earlier in time:** a note that started **earlier in time** than the queried span but is
  still sounding inside it is included in the answer (there is no backward-in-time search limit).
- **Widening the span:** Architectural Layer 3 (key/mode) asks Architectural Layer 1 to extend the covered music
  **earlier in time** than the selection so the prevailing key before the selection can be seen; Architectural Layer
  1 reads the extra earlier music and adds those notes.

## 7. Data design
Each note record carries eleven facts: its **sounding pitch**; its **spelled pitch** (for example F♯ versus G♭);
which **staff** and which **voice** it belongs to; its **start time-position**, its **end time-position**, and its
**duration** (end time minus start time — the tie-resolved sounding length); and four yes/no facts — whether it is a
**grace note**, whether it actually **sounds** (false for muted notes and for imported cue notes), whether it is
**visible**, and whether its **staff takes part in tonal analysis** (false for drum/percussion staves, the
chord-symbol track, and hidden staves). All times are absolute time-positions within the piece. The note model also
holds the start-time-ordered list of note records, a borrowed pointer to the source MuseScore score (which must
outlive the note model), and the numeric look-up index.

## 8. Crosscutting concepts
- **Single source of truth** — the system-wide principle Architectural Layer 1 embodies: every architectural layer
  reads these notes; no architectural layer re-reads the raw MuseScore score.
- **Deterministic** — the same selected music always produces exactly the same note model.
- **Fast at any selection size** — the numeric look-up index keeps span-of-time queries quick even when the selected
  music is the whole piece.
- **Edge handling** — an empty or backwards span of time returns no notes; a silent span returns no notes; grace,
  muted, invisible, and non-tonal-staff notes are kept and marked, never dropped.

## 9. Architecture decisions (with the alternatives we weighed)
- **A group of tied notes is one note, not several.** Alternative considered: keep each tied note separate. Chosen:
  one note — the held parts of a tie still sound, so counting them as separate notes counts the same sustained sound
  more than once.
- **No limit on how far backwards in time a query searches.** Alternative considered: limit the backward-in-time
  search for speed. Chosen: no limit — a limit silently drops notes held longer than the limit; the speed was
  recovered instead by the numeric look-up index.
- **Keep every note and mark it, rather than filter notes out while reading.** Alternative considered: drop
  non-tonal/muted notes during the read. Chosen: keep-and-mark — so that choosing to ignore a note is an explicit,
  reversible step taken in a later architectural layer.
- **A numeric look-up index (a start-time-ordered list plus a "latest end-time so far" tree).** Alternatives
  considered: an interval tree, a bucketed index. Chosen: this structure — it is the simplest one that answers the
  span-of-time queries quickly *and* returns notes in exactly the same order a plain left-to-right scan would.

## 10. Quality & testing
- **Behaviour tests:** tied groups become one note; the span-of-time queries return the correct notes; the per-note
  facts are set correctly; edge cases (empty, backwards, and silent spans) behave correctly.
- **Look-up-index tests:** the fast index returns **exactly** what a plain left-to-right scan returns — the same
  notes in the same order — across many random and deliberately awkward spans of time on every test piece; plus a
  speed measurement confirming it stays fast when the selected music is large.
- **Coverage:** every branch of Architectural Layer 1's code is exercised by a test.
- **System check:** the project-wide per-event accuracy metric and both automated test suites stay green.
- **Regression tests (source):** `src/composing/tests/note_model_tests.cpp` — the behaviour tests (T1–T8), the
  derived-view tests (T9–T14), and the look-up-index-vs-linear-scan tests (IDX1–IDX4).

## 11. Risks & technical debt
- **An accepted, fully-explained shift in the accuracy metric, caused by building Architectural Layer 1 correctly** —
  resolving ties and removing the backward-in-time search limit moved the project's accuracy metric by a small
  amount; this was accepted deliberately and is expected to be re-tuned when Architectural Layer 3 (key/mode) is
  rebuilt (detail in Section 13).
- **Grace-note timing** — exactly how a grace note's start time, end time, and duration are recorded should be
  confirmed when Architectural Layer 3 begins using grace notes (there is deliberately no special grace-note
  handling in Architectural Layer 1).
- **The build currently reads the whole score even when only part of it is queried** — an **interim** behaviour, not
  the target. The product is selection-based (`cowork_bounded_context_design.md`): the target is *build over the
  selection, then extend on request*. Loading the whole score is the degenerate case (selection = score) and is what
  keeps the batch-testing path unchanged. The *extend* operation (§3) is **now built** (Phase-1a), so the whole-score
  build no longer masks a missing capability — it only means *extend*'s interim implementation re-walks the whole score
  rather than a span-scoped slice. The earlier framing that "fixing the whole-score build and building *extend* are one
  coupled change" is **superseded**: *extend* was built **decoupled** (Phase-1a, whole-score re-walk, byte-identical),
  with the span-scoped walk deferred to Phase-1b. The build-selection + extend **contract** is what every layer above
  is written against, so the interim is invisible to them.

## 12. Glossary
*(Only terms we coined or use in a specific way — standard musical terms are assumed known.)*
**Note model** — the clean, complete, tie-resolved, start-time-ordered list of sounding notes for the user-selected
music. **Tie-resolved** — a group of tied notes is treated as one single held note (one start time, one end time).
**Lossless** — keeping every note and its exact facts, never dropping or summarising them (Section 1). **Span of
time / time-position** — a stretch between two absolute positions in the piece; a query asks about notes within
such a stretch. **Widen the span** — extend the analysed music earlier and/or later in time, on a later architectural
layer's request. **Backward-in-time search limit** — an earlier, now-removed cap on how far earlier in time a query
searched (it lost long-held notes). **Derived summary view** — a read-only summary built on top of the note model
(for example `weightedPcView`, `soundingAt`). **Staff-eligible** — the note's staff takes part in tonal analysis
(drum/percussion staves, the chord-symbol track, and hidden staves are not staff-eligible).

## 13. Background: what Architectural Layer 1 replaces, and corrections on record (NOT needed to understand the layer)
*Kept separate so Sections 1–12 describe only Architectural Layer 1 itself.*
- **What it replaces:** the earlier per-consumer note collectors (`collectRegionTones`). They were tie-blind — a
  held note was counted once per written note, which inflated its weight — and they limited their backward-in-time
  search to four whole-notes, which silently dropped notes held longer than that. Architectural Layer 1 fixes both
  problems by construction.
- **The accepted accuracy shift:** resolving ties and removing the backward-in-time search limit moved the project's
  per-event accuracy metric by a small, fully-attributed amount (proven to come entirely from the tie fix and the
  search-limit removal), accepted as correct-now / re-tune-later — the re-tuning happens in Architectural Layer 3.
- **A field we specified then removed:** we had planned a "cue note" flag, then removed it — once a MuseScore score
  is imported, a cue note can no longer be told apart from an ordinary muted note, and the existing "does it sound"
  flag already excludes both.

## 14. Related work & external sources (what we borrowed, discarded, and why)
*The project's aim is to be the best harmonic inferrer it can be, so we take the best ideas from the field and say
plainly which we rejected.*
- **Built on:** the idea of a **lossless symbolic-music event list** (as opposed to a reduced summary) — the same
  stance as music21's note/stream model and the MusicXML/MEI source formats; we keep the notes and summarise only in
  the derived views. **Standard interval-query data structures** (interval trees / segment trees) for the fast
  "which notes sound between A and B" look-up. **Tie and playback resolution** comes from MuseScore's own note model
  (`firstTiedNote`/`lastTiedNote`/`playTicksFraction`), not reinvented.
- **Discarded / not used:** **summarising notes to pitch classes at read time** — rejected here because it is lossy;
  summarising belongs in the derived views, on top of the lossless model. (The earlier per-consumer collectors are
  in Section 13.)
- **Corpora used:** the **353-piece Bach chorale set (plus a Corelli trio)** — used to confirm the look-up index
  stays correct and fast at scale. (The key/chord research corpora are referenced in the later architectural layers
  that use them.)
