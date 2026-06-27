# Architectural Layer 2 — CHANGE-POINT SLICING — Architecture & Design

> **Status: AS-BUILT (built, reviewed, accepted, and validated on the full test corpus; on the project's own copy
> of the MuseScore source code).** Source-commit identifiers, for traceability only: `e470e2667e`, `566d64d383`.
> Follows the standard section structure in `cowork_design_doc_template.md`. Coding increments are delivery
> sequencing and live in the delivery plan, not here. *(Two template sections do not apply: "Deployment view" and
> "Human-interface design" — this is backend analysis code, no separate deployment, no user interface.)*

## 1. Introduction & purpose
**What Architectural Layer 2 is.** It cuts the analysed music into **slices** and hands the list of slices to the
next architectural layer. A **slice** is a span of time during which the set of sounding, tonal notes does not
change at all — so the set of notes is the same from the slice's start to its end, and it changes only when you
cross into the next slice.

**What music Architectural Layer 2 operates on.** The notes provided by Architectural Layer 1 (the note model) for
the user-selected part of the score. It reads no other source.

**Why Architectural Layer 2 exists.** It makes cutting the music into spans a **fact read directly off the notes,
not a guess.** When boundaries are guessed, a single span can **over-grab** — stretch across two or more different
chords — and is then forced to carry one chord label when it really contains several; over-grab is the largest
single source of error in the analysis. Reading the slices straight off the notes makes over-grab impossible by
construction: because a slice ends the instant the set of sounding-and-tonal notes changes, a chord can change only
**at a slice boundary, never inside a slice.** (The previous guess-based approach, and the size of the over-grab
error, are in Section 13.)

**Scope — what Architectural Layer 2 does:** read the note model and produce the ordered list of slices that exactly
covers the analysed span.

**What Architectural Layer 2 explicitly does NOT do** (stated because each boundary matters):
- It does **not** decide any key, chord, or non-chord-note (Architectural Layer 3 and later).
- It does **not** group equal-sounding neighbouring slices together (Architectural Layer 6).
- It does **not** apply any threshold, smoothing, or merging, and does **not** judge which notes "matter" — it cuts
  at every change in the sounding-and-tonal note set, and re-decides nothing Architectural Layer 1 already marked.
- It does **not** read or change the notes (Architectural Layer 1).

## 2. Constraints
- **A fact, never a guess:** no thresholds, no heuristics, no interpretation of which notes "matter" — every change
  in the sounding-and-tonal note set is a boundary, full stop.
- **The slices completely cover the analysed span, with no gaps and no overlaps**, and they hide nothing: a span of
  time during which no tonal note sounds (silence) is recorded as an explicit empty slice, not skipped over. The
  notes themselves are left untouched (each slice just points at a span of the note model).
- **It uses Architectural Layer 1's "counts toward tonal analysis" markings; it does not re-decide them.** Whether a
  note sounds, is visible, and is on a tonal staff was already decided and marked by Architectural Layer 1;
  Architectural Layer 2 reads those marks and does not second-guess them.
- **Connected into the live analysis pipeline:** Architectural Layer 3 now reads the slices —
  `regionanalyzer.cpp:579` calls `changePointSlices(noteModel)` and feeds the result to the key-mode sequence decoder.
  The slicer itself still produces byte-identical slices on the whole-score live path (the clip is inert there); the
  analysis movement came from **Architectural Layer 3's consumption** of the slices, not from the slicer.
- **Works on the user's selected music, at any size and in any musical style;** the work it does grows only in
  proportion to the number of notes.

## 3. Context & scope (external view)
**What Architectural Layer 2 reads (its input):** the Architectural Layer 1 note model — each note's start time, end
time, and the markings for whether it sounds, is visible, and is on a tonal staff.
**What Architectural Layer 2 offers (the operation other code calls):**
- *Give me the slices* — return the ordered list of slices that covers the analysed span. Each slice is just a pair
  of time-positions, a start and an end; the slice does not store its notes, because the notes for a slice can be
  fetched on demand by asking the Architectural Layer 1 note model "which notes sound during this slice's span?"
**Who uses Architectural Layer 2 (its consumers):** the Architectural Layer 3 key/mode code (it decides key/mode for
each slice); later, Architectural Layer 4 (a chord symbol per slice) and Architectural Layer 6 (grouping equal
slices for display). **What Architectural Layer 2 deliberately knows nothing about:** weighting, keys, chords, or
function.

**Implementation (source files):** `src/composing/analysis/slicing/slicer.{h,cpp}` (`changePointSlices`, `Slice`).

## 4. Solution strategy
Treat **every moment when the set of sounding-and-tonal notes changes** as a slice boundary. A note that is sounding,
visible, and on a tonal staff causes a change both when it **starts** and when it **stops**; collect all those
start- and stop-moments, and the spans between consecutive moments are the slices. This is the well-known
"salami-slicing" idea (Pardo & Birmingham; music21's `chordify`). Architectural Layer 2 produces it as a pure fact:
no selection of which moments count, no smoothing, no special handling of particular kinds of note. Equal-sounding
neighbouring slices are merged later, by Architectural Layer 6 — never here.

## 5. Building-block view (static / internal structure)
Architectural Layer 2 is a single function that does two steps:
1. **Collect the boundary moments.** Go through the note model; for each note that is sounding, visible, and on a
   tonal staff, record its start time-position and its end time-position; sort these time-positions and remove
   duplicates (a moment that is one note's stop and another note's start is a single boundary, not two).
2. **Form the slices.** Each pair of consecutive boundary moments becomes one slice (start moment to next moment).
   A pair of consecutive moments during which no sounding-and-tonal note is present is an explicit **empty slice**
   (it records the silence). If there are fewer than two boundary moments, there are no slices.
There is no stored state, there are no thresholds, and no kind of note is special-cased.

## 6. Runtime view (scenarios)
- **A passing note over a held chord:** a held chord, with one extra note that sounds only briefly in the middle →
  three slices (chord alone / chord plus the extra note / chord alone again).
- **A held chord under a moving melody:** one slice per melody note; every slice contains the same held chord (the
  grouping layer will later merge them).
- **A held sound written as tied notes:** no boundary inside it — Architectural Layer 1 already merged the tied
  notes into one held note, so there is nothing to slice there.
- **One chord-note stops while the rest sound on:** the note set shrinks at that moment, so a new (smaller) slice
  begins there.
- **A span where every tonal voice rests:** an explicit empty slice — the silence is recorded, not skipped (it is
  useful later, for example as a phrase boundary).

## 7. Data design
A slice is a pair of time-positions: a **start** and an **end** (the span is inclusive of the start moment and
exclusive of the end moment). A slice stores no notes; its notes are fetched on demand from the Architectural Layer
1 note model. **A slice's identity is the exact set of sounding, tonal notes inside it — not a folded-down summary
of their pitches.** This matters: if two notes of the same pitch are sounding and one stops, the set of notes has
genuinely changed (so a new slice begins) even though the collection of pitch-letters present has not. The output is
an ordered list of slices that covers the analysed span from its first boundary moment to its last.

## 8. Crosscutting concepts
- **Zero interpretation** — Architectural Layer 2 makes no musical judgement of any kind; this is the principle it
  embodies.
- **Complete coverage with nothing hidden** — every moment of the analysed span lies in exactly one slice, including
  silence; because a slice boundary marks every possible moment a chord could change, a real chord change can never
  be missed. The only cost is harmless extra slices that look identical and are merged later.
- **Deterministic; work proportional to the number of notes; careful edge handling** (an empty range, a single
  note, a moment that is both a stop and a start, a fully silent range).
- **A slice is a unit of constant *content*, not of constant musical *time*.** Two slices are both "one slice" whether
  one is a ten-measure held chord and the other a passing sixteenth — but they carry very different inferential weight,
  so the layers above must **never treat slices as equal-weight units**. A slice's **metric extent** — its **duration**
  (`end − start`, directly on the slice) and its **metric position/weight** (the metric-weight derived view over
  Architectural Layer 1's score, from the time signature) — is **evidence**, and it is weighted by metric structure,
  **not by tempo**: the harmonic reading (and the human ground truth) keys off beat strength and notated duration in
  beats/measures, not absolute clock time. Architectural Layer 2 keeps the slice **minimal** (`[start, end)` only); the
  duration and metric weight are **derived on demand** by the consuming layers (Architectural Layer 3 emission,
  Architectural Layer 4 membership), not stored here. *(How well the inference weights the extremes — a very long held
  chord, a very short embellishment slice — is an Architectural Layer 3 / 4 weighting concern; the metadata to do it
  is available here.)*
- **Bounded context (`cowork_bounded_context_design.md`).** Architectural Layer 2 slices whatever span the note model
  currently holds. When a higher layer **extends** the loaded span (to reach context outside the user's selection),
  Architectural Layer 2 produces the change-point slices for the **newly loaded region**, preserving complete coverage
  and slice identity over the enlarged span. Slices that fall in the **context span** (loaded but outside the
  selection) are usable as evidence by the layers above but are **not** part of the analysis output. Architectural
  Layer 2 itself makes no selection-versus-context distinction — it just slices the loaded span; the output-versus-
  evidence boundary is the consuming layer's concern.

## 9. Architecture decisions (with the alternatives we weighed)
- **A boundary at every note start AND every note stop** (not only at note starts). Alternative considered: cut only
  where notes start. Chosen: cut at both — a note stopping mid-span shrinks the sounding set, so a starts-only rule
  would leave a slice whose note set is not actually constant.
- **Cover the whole span, including silence, as explicit empty slices.** Alternative considered: skip silent spans
  ("no slice there"). Chosen: keep them — dropping silence hides a real fact that is useful later (for example a
  phrase boundary) and breaks complete coverage.
- **Read the change-point fact straight off the notes and apply no selection or smoothing.** Alternative considered:
  build a brand-new slicer from scratch. Chosen: the change-point set already existed in older code; only the
  guessing built on top of it had to be removed (see Section 13).
- **Build Architectural Layer 2 on its own, not yet connected into the live pipeline.** Alternative considered:
  connect it into the running analyzer immediately. Chosen: keep it separate — fine slices need Architectural Layer
  3's reasoning, so connecting it (and dissolving over-grab) belongs to Architectural Layer 3.

## 10. Quality & testing
- **Behaviour tests:** the scenarios in Section 6 plus edge cases, each asserting the exact start/end time-positions
  of the slices and the exact set of tonal notes in each slice.
- **Whole-corpus check:** the real slicer was run over all 353 test pieces and checked, against an **independent
  re-computation of the boundary moments from the note model** (not the slicer's own work), for: complete coverage
  with no gaps or overlaps; a genuinely constant tonal-note set inside each slice; no missing or invented
  boundaries; and identical output on a second run. All 353 passed.
- **Every branch of Architectural Layer 2's code is exercised by a test.**
- **Isolation check (at build time, before wiring):** the slicer was confirmed to leave both automated test suites and
  the pinned analysis outputs unchanged by its existence. It is now connected (Architectural Layer 3 reads the slices,
  `regionanalyzer.cpp:579`); the slicer's own output stays byte-identical on the whole-score live path.
- **Regression tests (source):** `src/composing/tests/slicer_tests.cpp` (the behaviour + edge tests); the
  whole-corpus check is `tools/batch_analyze --validate-slices` driven by `tools/validate_slices_corpus.py`.

## 11. Risks & technical debt
- **Slicing finely creates the opposite problem, left for Architectural Layer 3:** the fine slices produce many
  neighbouring slices that carry the same harmony, and recognising that they are the same is Architectural Layer 3's
  job — not solved here.
- **How often slices are redundant depends on the music** — on the chorale test pieces almost no slice is redundant;
  denser textures (sustained pedals, broken chords) would produce more, which the grouping layer merges regardless.
- **Connected into the live analysis pipeline** — Architectural Layer 3 now reads the slices
  (`regionanalyzer.cpp:579`), the retirement trigger this risk anticipated; its coexistence with the old machinery
  during that transition is described in Section 13.

## 12. Glossary
*(Only terms we coined or use in a specific way — standard musical terms are assumed known.)*
**Slice** — a span of time during which the set of sounding, tonal notes does not change. **Sounding, tonal note** —
a note that, per Architectural Layer 1's markings, sounds, is visible, and is on a tonal staff. **Boundary moment** —
a time-position where a sounding-tonal note starts or stops (and therefore a slice begins/ends). **Complete
coverage** — the slices fill the analysed span with no gaps and no overlaps. **Empty slice** — a slice during which
no sounding-tonal note is present (silence). **Over-grab** — a single span stretching across two or more chords (the
error Architectural Layer 2 removes by construction).

## 13. Background: what Architectural Layer 2 replaces, and corrections on record (NOT needed to understand the layer)
*Kept separate so Sections 1–12 describe only Architectural Layer 2 itself.*
- **What it replaces:** the earlier "segment-first" pipeline (a greedy boundary-expander, several sub-boundary
  detectors, and a chord-dependent merge step). It *guessed* span boundaries using tunable score thresholds before
  any analysis, which let spans over-grab — about 45% of the measured error. Architectural Layer 2 removes that
  guessing entirely.
- **The fact already existed but was thrown away:** older code (`collectNoteChangeTicks`) already computed the same
  note-start/note-stop boundary moments, but the old pipeline then **discarded** most of them by selecting a subset
  using chord-score thresholds (and it also skipped grace notes and snapped mid-tuplet moments). Architectural Layer
  2 keeps the boundary-moment fact and drops the selection and those two special-case heuristics.
- **Still transitional:** the old segment-first pipeline still runs and still drives analysis until Architectural
  Layer 3 is rebuilt to read slices; deciding what of the old machinery moves to the grouping layer versus is
  deleted is scoped when Architectural Layers 3 and 6 are built.

## 14. Related work & external sources (what we borrowed, discarded, and why)
*The project's aim is to be the best harmonic inferrer it can be, so we take the best ideas from the field and say
plainly which we rejected.*
- **Built on:** the **onset-and-offset "salami slice"** — Pardo & Birmingham, "Algorithms for Chordal Analysis"
  (Computer Music Journal, 2002), and the verticalization done by **music21's `chordify`** (Cuthbert & Ariza). Both
  cut at every note start and stop; we adopt that as the lossless change-point fact (the same lineage our own
  `collectNoteChangeTicks` already cited).
- **Considered and discarded / not used:** **fixed metric-grid or beat-synchronous segmentation** (for example
  AugmentedNet's fixed note-value frames; Contrapunctus's per-beat unit) — rejected because a metric grid imposes a
  judgement: it over-slices a held chord on the clock and can miss a change that falls between grid points.
  **Pitch-class-mask change detection** (folding the sounding notes down to which pitch-letters are present) —
  rejected because a slice's identity is the exact set of notes, not the set of pitch-letters (a same-pitch
  doubling that drops is a real change the folded view misses). (Our own earlier threshold-based segmentation is in
  Section 13.)
- **Corpora used:** the **353-piece Bach chorale set (plus a Corelli trio)** — used for the whole-corpus property
  check (complete coverage, constant note set per slice, no missing/invented boundaries, determinism) on every
  piece.
