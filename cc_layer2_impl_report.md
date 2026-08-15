# CC — Layer 2 (change-point slicer) IMPLEMENTATION report

> Implements the SIGNED + RATIFIED design (`cowork_layer2_slicing_design.md`) + audit
> (`cc_layer2_audit_dossier.md`). **One increment:** the isolated `slicing/` module +
> 100%-covered tests + code comments + synced canonical docs. **TEST/ISOLATED — no analysis
> behavior change** (the slicer is not wired into the live pipeline). **Local commit (unpushed);
> Cowork verifies at source; user ratifies; then a fork push (origin only, never upstream).**
>
> BEFORE = HEAD `257b55c9f4` working tree (the pre-existing HELD B2 / cowork-doc working-tree
> edits are untouched and excluded from this commit). All numbers below are this session's runs.

---

## §1 — The module as built (`src/composing/analysis/slicing/slicer.{h,cpp}`)

A pure, deterministic, lossless function over the layer-1 note model, in its own module/namespace
`mu::composing::analysis::slicing` (parallel to `notemodel/`, per the user's "each layer lives
separately" mandate).

```cpp
struct Slice { int start = 0; int end = 0; };            // half-open [start, end)
std::vector<Slice> changePointSlices(const notemodel::NoteModel& model);
```

Algorithm (O(n log n), the sort being the only non-linear step):
1. **Boundary ticks** = for every **eligible** note (`plays && visible && staffEligible`), push its
   `onset` and its `release`. Non-eligible notes are skipped (a `continue`) — they open no boundary.
2. **Sorted-unique** the boundary vector (a tick that is simultaneously a release and an onset is
   **one** boundary, not two).
3. If `< 2` distinct boundaries → return empty (no eligible notes, or a single zero-width
   boundary: nothing to slice).
4. Emit consecutive boundary pairs `[b[i], b[i+1])`. This tiles `[b.front(), b.back())` with no
   gaps and no overlaps; an interior pair with no overlapping eligible note is an **explicit empty
   slice** (it falls out for free — no special empty-slice code).

The slicer **stores no notes**: a `Slice` is just `[start,end)`; its content is the lazy
`model.overlapping(start,end)` query, which returns **all** overlapping notes (eligible AND the
flagged non-eligible passengers). Slice identity (for "constant sonority") is the **eligible
sounding-NOTE set**, not the octave-folded PC set.

**Invariants honored (design §5):** zero interpretation (no thresholds/min-gap/merge/snapping, no
note-kind special case); consumes L1's eligibility (reads the flags, never re-decides); passes the
whole model forward; covering/lossless partition; deterministic. Boundaries are **necessary but
not sufficient** for a chord change — over-grab is structurally impossible, and the slicer never
asserts a change (that is L3's judgment).

---

## §2 — §3 verify-at-source findings (the no-assume obligation)

### (1) Grace span representation — VERIFIED, design-anticipated branch confirmed
Source chain read this session:
- `note_model.cpp:45-65` (`makeEvent`) — a grace note's event is built with **onset = the parent
  chord's segment tick** (`segTick`, `build()` passes it for grace at `:120`) and
  `duration = Note::playTicksFraction().ticks()`, `release = onset + duration`.
- `note.cpp:1193` `Note::playTicksFraction()` — for an untied note returns `chord()->actualTicks()`.
- `durationelement.cpp:114` `actualTicks() = globalTicks() / timeStretch` — for a grace chord this
  is its **nominal written duration** (NOT zero).

**Finding:** the design's parenthetical guess ("a zero-duration acciaccatura has an empty `[t,t)`
span") is **not** how layer 1 represents grace. The `nm_grace` acciaccatura is
`durationType=eighth`, so layer 1 gives it span **`[0,240)`** (onset 0 = parent tick, duration 240
= eighth). This is the design's explicitly-anticipated **other** branch — *"a duration-bearing
[grace] genuinely sounds and does open a slice"* (design §5) — and exactly what instruction §4
asks for: *"grace sliced by its layer-1 span (NO special rule)."* So under the zero-interpretation
slicer the grace **opens a boundary at 240**, splitting the main chord's first eighth into
`[0,240){C,E,G,grace}` then `[240,480){C,E,G}`.

**Not a STOP.** This is a redundant **candidate** boundary, not a missed change — the same tolerated
class as the design's redundant release-slices (necessary-but-not-sufficient contract; L3 reads the
grace as an NCT/ornament, LN groups the two equal-analysis slices). The slicer **honors L1's
annotation** (the layer-boundary rule: whether a grace *should* have a `[0,240)` span is a layer-1
question, not the slicer's) and **needs no grace code**. Empirically confirmed by test **S5**
(asserts `grace->onset==0`, `grace->release==240`, and the two slices). *Recorded for the user as a
layer-1 observation:* if a future decision wants grace to NOT open boundaries, that is a layer-1
grace-span change (or an L3 judgment), never an L2 special case.

### (2) Tuplet ticks — VERIFIED, real un-snapped ticks
`note_model.cpp build()` uses `s->tick().ticks()` for onset (the real ChordRest segment tick) and
`playTicksFraction()` (= `actualTicks()` = `globalTicks()/timeStretch`, the real tuplet-ratio-aware
duration) for the span. There is **no** mid-tuplet snapping (unlike the old Score-based
`collectNoteChangeTicks`, harmonicsegmenter.cpp:264-307, which snapped mid-tuplet ticks to the
tuplet start). **Finding:** the note model exposes real tuplet onset/release ticks; the slicer
inherits them and adds no snapping. (No tuplet in the chorale corpus per audit §2c, so this is a
source-read fact, not a corpus measurement.)

---

## §3 — Functional cases + coverage (`slicer_tests.cpp`, 13 tests, all PASS)

Fixtures: 5 NEW (`nm_slice_passing`, `nm_slice_held_melody`, `nm_slice_release`, `nm_slice_rest`,
`nm_slice_ineligible`) authored as `.musicxml` → converted to `.mscx` via `MuseScore5.exe` (both
kept, provenance); plus REUSE of layer-1 `nm_tie_chain` / `nm_unison` / `nm_grace` /
`nm_long_sustain` / `nm_dense_start` / `nm_flags` / `nm_staff_eligibility`.

| Test | Case | Asserted slices `[start,end)` |
|---|---|---|
| S1 | passing tone → 3 slices | `[0,480){CEG}`,`[480,960){CEG+D}`,`[960,1440){CEG}` |
| S2 | held chord under moving melody → slice per onset (+coincident release/onset dedup) | 4 slices, each = chord + current melody note |
| S3 | tie chain → no internal boundary | `[0,1440){C}`,`[1440,1920){D}` |
| S4 | chord tone releases mid-span → new slice (offset boundary) | `[0,480){CEG}`,`[480,960){CE}` |
| S4b | unison shrink (note-set boundary, PC-set constant) | `[0,480)` (2 notes), `[480,960)` (1 note) |
| S5 | grace sliced by L1 span, NO special rule | `[0,240){CEG+grace}`,`[240,480){CEG}` (grace span `[0,240)` verified) |
| S6 | all-rest interior → explicit EMPTY slice (covering) | `[0,480){C}`,`[480,960){}`,`[960,1440){E}` |
| S7a | empty model → no slices | `{}` (size<2 early return) |
| S7b | single note (no horizon) | `[0,9600){C}` |
| S7c | back-to-back onsets / onset-at-boundary | 4 contiguous slices |
| S8a | invisible note MID-SLICE → no boundary, passed through | `[0,1920)`; G4 in `overlapping()` but not eligible set |
| S8b | non-playing (cue) + invisible → no boundary | `[0,480)`; cue B4 + invisible G4 pass through |
| S8c | staff-ineligible (chord-track) → no boundary | `[0,1920)`; chord-track E4 passes through |

Every test asserts the covering/lossless invariant (`expectCoveringPartition`: each slice
non-zero-width, `slices[i].end == slices[i+1].start`).

**Measured branch coverage (the GATE).** Tool: VS BuildTools
`Microsoft.CodeCoverage.Console.exe` (Dynamic Code Coverage → Cobertura), instrumenting the Release
`/Zi` `composing_tests.exe` over `--gtest_filter='Composing_SlicerTests.*'` (same tool as the
layer-1 coverage pass).

| File | Coverage |
|---|---|
| `slicing/slicer.cpp` | **line-rate 1.0 / branch-rate 1.0 — 100%** (all executable lines L30–L71 hit; both arms of the eligibility skip, the `<2 boundaries` early return, and both loops covered) |
| `slicing/slicer.h` | no executable code (a POD struct + a declaration; `Slice` aggregate construction is exercised at slicer.cpp:67) |

**No coverage-fill pass was needed** — the audit §3 functional set + edges reached 100% on the
first measurement. **No unreachable branches** to document; nothing was faked or deleted.

---

## §4 — Isolation / byte-identity proof (§4.3 of the instruction)

- **Production code touched:** exactly one file, **comment-only** — a 6-line `///` successor note
  above `collectNoteChangeTicks` (`harmonicsegmenter.cpp`; `git diff --stat` = 6 insertions, 0
  code). The new module is **not referenced by any production code** (grep for `changePointSlices`
  / `analysis::slicing` / `slicing/slicer` → only `slicer.{h,cpp}`, `slicer_tests.cpp`, the
  `harmonicsegmenter.cpp` comment, and the two CMakeLists). So the analyzer binary's behavior is
  **byte-identical by construction**.
- **Both suites + snapshots:** composing **572/572** (559 + 13 new), notation **57/57**, pipeline
  snapshots **11/11 with NO golden refresh** — the real P1–P4 pipeline output is byte-identical,
  proving the slicer was not wired in by accident.
- **BIR / oracle:** unchanged by construction (the analysis code is untouched; the snapshot
  byte-identity confirms it). A 353-corpus regen would be byte-identical and was not run (same
  rationale as the ratified layer-1 coverage pass).

If any of these had moved, the module would have been wired in by accident → STOP. None moved.

---

## §5 — Docs + comments synced (same increment — standing all-in-sync rule)

- **`ARCHITECTURE.md`** — new "Layer 2 — the deterministic change-point slicer (as-built,
  isolated)" subsection (covering/lossless, boundaries over L1 eligibility, empty-slice rule, slice
  identity = eligible note set, zero-interpretation incl. the verified grace/tuplet facts, isolated
  + 100% covered); layer map updated **L2 → BUILT (isolated)**; layer-1 "Next: layer 2" → "Next:
  layer 3".
- **`docs/implementation_roadmap.md`** — L2 row marked **✅ BUILT — ISOLATED (local commit,
  pending Cowork verify + user ratify)** with evidence (the test set, suite/snapshot counts,
  byte-identity, 100% coverage); L3 promoted to **NEXT**; layer map line updated.
- **Code comments** — `slicer.h` banner (role + the 6 §2 rules in brief + the zero-interpretation /
  consumes-L1-eligibility / passes-whole-model-forward / covering-lossless invariants); the 6-line
  successor note near `collectNoteChangeTicks` (comment only).
- **`docs/scoring_model.md`** — **not touched** (the change touches no template/bonus/guard/gate/
  scoring term; the slicer is isolated and carries no analysis). No edit required.
- `cowork_layer2_slicing_design.md` as-built is **Cowork's** to update post-ratification (not
  edited here).

---

## §6 — Deliverable / workflow
- New module `slicing/slicer.{h,cpp}` + `slicer_tests.cpp` (13 tests) + 5 new fixtures
  (`.musicxml` + `.mscx`) + the CMake wiring (analysis + tests) + the ARCHITECTURE/roadmap edits +
  the `harmonicsegmenter.cpp` comment.
- Committed **locally, unpushed**, as one increment: **`e470e2667e`** (17 files, +1638 / −5).
  Excluded: the pre-existing HELD B2 working-tree edits, the `cowork_*` design docs, **and
  `docs/implementation_roadmap.md`** — per user direction (2026-06-21), the roadmap held unrelated
  pre-existing WIP (a ~585-line rewrite) as a single indivisible diff hunk, so my L2-row edit was
  left **unstaged** in the working tree rather than bundle that WIP into the L2 commit. ARCHITECTURE.md
  was separable (distinct hunks) and its L2 edits ARE committed; its pre-existing 2026-06-15
  joint-inference forward-pointer hunk was left unstaged.
- **For ratification:** the isolated slicer (faithful to L1, no behavior change — proven
  byte-identical), the two source-verified findings (grace = duration-bearing → opens a slice;
  tuplet = real un-snapped ticks), the 13 functional/edge tests, and 100% measured branch coverage.

## §7 — Stop conditions encountered
- **Grace span vs design guess** (§2.1): the acciaccatura is duration-bearing, not zero-width —
  evaluated against the §3/§7 STOP trigger and judged **NOT** a "clearly wrong result" but the
  design's explicitly-anticipated second branch (a redundant candidate boundary the contract
  tolerates; the slicer honors L1's annotation and needs no grace code). Recorded for the user as a
  layer-1 observation, not blocked. No other stop condition hit (no scoring/segmentation/
  regionanalyzer change; no metric moved; no threshold/min-gap/merge/snap needed to pass any test).
