# Decisions group E — Layer 2 — the slicer

> **GENERATED FILE — do not hand-edit.** Part of the decisions register: the index,
> the how-to-read guide and the terms table are `DECISIONS.md` (repository root);
> the source of record is `tools/audit/decisions/backbone_decisions.json`; the
> generator is `tools/audit/decisions/gen_decisions_register.py`. To change an
> entry, edit the data and regenerate.

### D-041 — The slicer output covers the domain with no gaps and no overlaps

> returns an ordered, **covering, lossless** list of half-open `[start,end)` spans that **tile the domain with no gaps and no overlaps**

**In plain words.** The music is cut into consecutive stretches that between them account for every moment exactly once.

**Why.** Stated constraint, ARCHITECTURE.md:1210: a covering, lossless tiling is what makes the slicer a fact rather than a judgment - every tick lands in exactly one slice, so nothing the score sounds can fall between slices.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1210`

**Provenance.** ARCHITECTURE.md:1200-1210 (Layer 2 - Built+Live)

### D-042 — Slice boundaries are every onset AND every release

> Boundaries = the sorted-unique union of every **onset AND every release** of the **eligible** notes; consecutive boundaries form the slices.

**In plain words.** A new stretch begins whenever any note starts and also whenever any note stops - because a note ending changes what is sounding just as much as a note beginning.

**Why.** Stated constraint, ARCHITECTURE.md:1210 with :1077-1080: taking every onset AND every release makes the boundary set an exhaustive candidate grid - necessary but not sufficient - so a real chord change can never be missed and over-grab is structurally impossible.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1210`

**Provenance.** ARCHITECTURE.md:1210. Cited by open_items/OI-228 as the primary source the joint emission departs from

### D-043 — Slice identity IS the eligible sounding-note set

> **Slice identity is the eligible sounding-NOTE set** (not the octave-folded PC set — a
> unison/octave shrink is a real boundary though the PC set is unchanged).

**In plain words.** What makes one stretch different from the next is the exact set of notes sounding through it - not merely which pitch names are present. Two voices collapsing onto the same note is a real change even though no pitch name was lost.

**Why.** Stated constraint, ARCHITECTURE.md:1217-1218: identity is the note set and not the octave-folded pitch-class set, because a unison or octave shrink is a real boundary even though the pitch-class set is unchanged.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1217-1218`

**Provenance.** ARCHITECTURE.md:1217-1218. The joint decoder's per-event note set is ONSET-only (jointdecoder.h:67) - open_items/OI-228

### D-044 — A note that opens no boundary still rides along in the slice's sounding set

> A muted / invisible / non-tonal-staff note opens
> **no** boundary, yet still rides along in each slice's `overlapping()` set (passed through, not
> dropped).

**In plain words.** A note that is not allowed to create a new stretch is still recorded as sounding during the stretches it spans.

**Why.** Stated constraint, ARCHITECTURE.md:1214-1216: a slice is 'constant TONAL sonority', so an ineligible note opens no boundary; dropping it as well would lose it (#12), and it is carried as passenger metadata instead.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1214-1216`

**Provenance.** ARCHITECTURE.md:1212-1218

### D-045 — The slicer re-decides nothing about eligibility

> **Boundaries over layer-1's eligibility annotation — never re-decided.**

**In plain words.** Whether a note counts was settled by the note reader. The slicer reads that decision and does not second-guess it.

**Why.** Stated constraint, ARCHITECTURE.md:1212-1214: eligibility is Layer 1's decision, and a second filter in Layer 2 would be a second place the same question is answered (#6/#7).

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1212`

**Provenance.** ARCHITECTURE.md:1212-1214

### D-046 — Zero interpretation - the slicer applies no thresholds and no musical judgment

> **Zero interpretation.** No thresholds, min-gap, merge, or snapping; no notion of
> "ornamental/passing/structural".

**In plain words.** The cutting-up step makes no musical decisions at all. It does not decide that a note is ornamental, does not merge short stretches, and has no adjustable numbers.

**Why.** Stated constraint, ARCHITECTURE.md:1237-1239: a threshold or a merge would make the slicer a judgment; with none, its output is a fact and the judgment stays where it belongs, in the layers that decide.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1237-1239`

**Provenance.** ARCHITECTURE.md:1237-1245

### D-047 — No special-casing of any note kind

> **No special-casing of any note kind** — grace and tuplet
> outcomes fall out of the note-model spans as facts

**In plain words.** Grace notes and tuplets need no special code. Their timing is a fact the note reader already carries, and the right answer falls out of it.

**Why.** Stated constraint, ARCHITECTURE.md:1238-1242, verified at the source: a grace note carries onset = the parent chord's tick and duration = its nominal written value, and tuplet ticks are the model's real un-snapped ticks, so both fall out of the note-model spans as facts and the slicer needs no grace or tuplet code at all.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1238-1240`

**Provenance.** ARCHITECTURE.md:1237-1242

### D-048 — Boundaries are necessary but not sufficient; over-grab is structurally impossible

> Boundaries are **necessary but not sufficient** for
> a chord change (the exhaustive candidate grid): a real chord change can never be missed
> (over-grab is structurally impossible), and the slicer never asserts a change

**In plain words.** Every place a chord could change is offered as a candidate, so no real chord change can be missed. Whether a candidate is a real change is decided later, by a stage that judges harmony.

**Why.** Stated constraint, ARCHITECTURE.md:1242-1245: because the boundary grid is exhaustive, the slicer never asserts a change - Layer 3 decides which boundaries are real and a later layer groups equal analyses.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1242-1244`

**Provenance.** ARCHITECTURE.md:1242-1245

### D-049 — An interior stretch where everything rests is an explicit empty slice, not a gap

> An interior span where all eligible voices rest is an **explicit
> EMPTY slice** (empty eligible overlap set), not a gap

**In plain words.** Silence in the middle of the music is recorded as a stretch with nothing in it, rather than as a hole in the coverage.

**Why.** Stated constraint, ARCHITECTURE.md:1228-1230: an explicit empty slice falls out of the consecutive-boundary construction for free, and it keeps the covering guarantee (D-041) true through a silence, which a gap would break.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1228-1230`

**Provenance.** ARCHITECTURE.md:1220-1231

### D-050 — Slicing is clipped to the loaded span and never drags outside it

> slicing never drags outside the loaded span

**In plain words.** The slicer cuts only within the span it was handed: a note sounding across the edge of that span is cut at the edge, and the slicer never reaches outside it. Widening what is analysed is the orchestration's job, not the slicer's, and re-slicing a wider span must reproduce the narrower one exactly - which is what makes widening safe.

**Why.** Stated constraint, ARCHITECTURE.md:1220-1235 with `cowork_layer2_reslice_design.md` §2: the clip is what makes re-slice equivalence hold - re-slicing an enlarged span reproduces the narrower result, with interior change-points stable and only the edge slice abutting the artificial boundary extending - so extending the span is lawful rather than a re-analysis.

**Status.** LIVE · date not stated · ratifier not stated

**Home.** `ARCHITECTURE.md:1225`

**Provenance.** ARCHITECTURE.md:1220-1227; cites cowork_layer2_reslice_design.md §2

