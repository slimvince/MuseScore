# CC Instruction — LAYER 2 (change-point slicing): IMPLEMENTATION

> Layer 2 is signed, audited, and ratified (`cowork_layer2_slicing_design.md`; `cc_layer2_audit_dossier.md`).
> Build the deterministic **change-point slicer** as a **new, isolated `slicing/` module** over the layer-1 note
> model. **One increment delivers all of: the module + 100%-covered tests + code comments + synced canonical docs**
> (standing rules: full coverage AND all-documentation-in-sync). Commit locally (unpushed); Cowork verifies; user
> ratifies; then push.
>
> **★ Context you do NOT have (do not re-derive or "improve"):** this is one layer of a ratified 4-layer rebuild —
> **note model (L1, done) → change-point slicing (L2, THIS) → per-slice analysis (L3) → grouping (LN)**. Layer 2's
> ONLY job is to enumerate **constant-(tonal-)sonority slices** from the note model as a deterministic FACT. It is
> **NOT wired into the live pipeline** and changes **no** analysis behavior. Do not touch scoring, segmentation,
> key, or `regionanalyzer` wiring — that is L3.
>
> **★ No-assume rule (applies to you):** the two `[verify]` items in §3 must be confirmed at source before you rely
> on them; anything you cannot confirm → STOP and surface, do not guess.

## §1 — Placement (each layer lives separately — user mandate)
- **New module:** `src/composing/analysis/slicing/slicer.{h,cpp}` — parallel to `analysis/notemodel/`. Wire it into
  the composing CMake the same way `notemodel/` is wired. Header carries a banner comment in the **same style as
  `notemodel/note_model.h`** stating the layer-2 role (see §6).
- **New test file:** `src/composing/tests/slicer_tests.cpp`, wired into the composing test binary next to
  `note_model_tests.cpp`.
- **Do NOT** modify `harmonicsegmenter.cpp`'s `collectNoteChangeTicks` or `regionanalyzer.cpp`. The old Score-based
  grid keeps running until L3; the new module is standalone. (You may add a one-line *comment* near
  `collectNoteChangeTicks` noting the `slicing/` module is its layer-2 successor — comment only.)

## §2 — The contract (what to build)
A pure, deterministic, lossless function over the note model. Suggested shape (finalize naming to match codebase
conventions; mirror `notemodel`):
```
namespace mu::composing::analysis::slicing {
struct Slice { int start; int end; };               // half-open [start, end); references the model, stores no notes
std::vector<Slice> changePointSlices(const notemodel::NoteModel& model);
}
```
Rules — **every one is a FACT, zero interpretation:**
1. **Eligible tonal sounding set = layer-1's annotation, NOT re-decided here.** A note participates in boundary
   generation iff `plays && visible && staffEligible` (the flags layer 1 already set). Layer 2 **reads** these
   flags; it does **not** re-filter, re-derive, or override eligibility (that would overlap layer 1's
   responsibility). Muted / invisible / non-tonal-staff notes generate **no** boundary.
2. **Boundaries** = the sorted-unique union of every **onset** and every **release** tick among the eligible notes
   (per rule 1), within the domain `[firstEligibleBoundary, lastEligibleBoundary)`. A tick that is simultaneously a
   release and an onset is **one** boundary (set dedup), not two.
3. **Covering, lossless partition.** Consecutive boundary ticks form the slices; they **tile the domain with no
   gaps and no overlaps**. An interior span where **all** eligible voices rest is an **explicit EMPTY slice**
   (its eligible overlap set is empty) — NOT omitted. (Leading/trailing silence outside the domain is not
   invented — there are no notes to bound there.)
4. **Pass the whole model forward.** A `Slice` stores only `[start,end)`; its note set is the **lazy** query
   `model.overlapping(start, end)`, which returns **all** overlapping notes (eligible AND non-eligible, flagged) —
   nothing dropped. Slice identity (for "constant sonority") is the **eligible sounding-NOTE set**, not the
   octave-folded PC set, and not the non-eligible passengers.
5. **No special-casing of any note kind.** No grace rule, no tuplet-tick snapping, no thresholds, no min-gap, no
   merge. Grace and tuplet outcomes fall out of the note-model spans as facts (see §3 verify items).
6. **Deterministic + O(n log n)** (the sort). Same input model → same slices, every run.

## §3 — Verify at source BEFORE relying on them (no-assume)
1. **Grace span representation** — read `notemodel/note_model.cpp` `build()`: how is a grace note's
   `onset`/`release`/`duration` set? Confirm whether a zero-duration acciaccatura gets an empty `[t,t)` span (so it
   forms **no** slice as a fact via `overlapping`'s `release > t0` test) and whether a duration-bearing appoggiatura
   gets a real span (so it **does** open a slice). Record the finding; the slicer must need **no** grace code
   either way. **If grace spans are represented such that uniform slicing produces a clearly wrong result → STOP
   and surface** (do not add a grace special-case to "fix" it — that is an L2 interpretation; it would be a design
   question for Cowork/user).
2. **Tuplet ticks** — confirm the note model exposes **real** tuplet onset/release ticks (no pre-snapping to the
   tuplet start). If the model already snaps, record it (the slicer inherits real ticks; it must not add snapping).

## §4 — Tests (regression coverage — BOTH the cases AND measured 100%)
1. **Functional cases** = the audit dossier §3 set, **as corrected** by the ratified design: passing tone → 3
   slices; held chord under moving melody → slice per onset; tie chain → no internal boundary; mid-span release →
   new slice; unison shrink → new slice though PC set constant; **grace sliced by its layer-1 span (NO special
   rule)**; **all-rest → one EMPTY slice (covering)**; edges (empty range, single note, onset-at-boundary,
   coincident release+onset dedup); **and chord held across a barline → ONE slice** (pins that L2 ignores metric
   position). Assert the exact `[start,end)` list and, for constant-sonority cases, the eligible `overlapping()`
   note set. Reuse the `nm_*` fixtures; the 4 NEW fixtures (passing, held-melody, release, rest) follow the layer-1
   fixture pattern (author `.musicxml` → convert to `.mscx` via MuseScore5.exe; composing_tests cannot import
   MusicXML — see the established fixture-conversion note).
   - Add at least one **eligibility** test: a non-tonal/invisible/muted note mid-slice must **not** open a boundary,
     yet must still appear in that slice's `overlapping()` set (pass-through proof).
2. **Measured 100% branch coverage of the new `slicing/` code** (the GATE — not "the 11 cases"). Instrument
   branch coverage (per `build_and_test.md`), run `slicer_tests`, report the **actual** number + the uncovered
   branches; add targeted tests until every **reachable** branch is hit; document any **genuinely unreachable**
   branch (file:line + why), do not fake or delete it. (Same discipline as the layer-1 coverage pass.)
3. **Isolation proof:** because the slicer is not wired in, `composing_tests`, `notation_tests`, the snapshot tests,
   and BIR/oracle must remain **byte-identical** to pre-change. If ANY existing metric moves, the module got wired
   in by accident → STOP, revert the wiring, surface.

## §5 — Documentation + comments (SAME increment — standing all-in-sync rule)
1. **`ARCHITECTURE.md`** — add the `slicing/` layer as **as-built**: a short section (match the layer-1 note-model
   section's voice) describing the covering/lossless/zero-interpretation slicer, boundaries over layer-1's
   eligibility annotation, the empty-slice rule, that slice identity is the eligible note set, and that it is
   **isolated / not wired in** (consumed at L3). Update the layer map (L1 → L2). Reframe nothing else.
2. **`docs/implementation_roadmap.md`** — record **Layer 2 (change-point slicing) = DONE/ratified** with evidence
   (the commit, the coverage number), L3 next. Honor the roadmap's "evidence required to mark done" rule.
3. **Code comments** — the `slicer.h` banner (role, the 6 §2 rules in brief, the "zero interpretation / consumes
   L1 eligibility / passes whole model forward" invariants); the one-line successor note near
   `collectNoteChangeTicks` (comment only).
4. **`docs/scoring_model.md`** — only if the change touches scoring (it must not). If untouched, no edit; say so.
5. The Cowork design doc (`cowork_layer2_slicing_design.md`) → as-built is **Cowork's** to update after
   ratification; do not edit `cowork_*` files.

## §6 — Workflow + deliver
Commit **locally (unpushed)** as one increment: the `slicing/` module + `slicer_tests.cpp` + new fixtures + the
doc/comment edits + the CMake wiring. Suggested message: `feat(composing): Layer 2 — deterministic change-point
slicer (isolated module) + tests + docs`. Write `cc_layer2_impl_report.md`: the module API as built, the two §3
verify-at-source findings (grace spans, tuplet ticks), the functional-case results, the before→after **measured**
branch coverage (+ any documented-unreachable branches), the byte-identity/isolation proof (both suites + snapshot
+ BIR/oracle unchanged), and the doc/comment diffs. Cowork verifies at source (module is isolated, coverage is
real, docs match as-built); user ratifies; then a fork push (origin only, never upstream).

## §7 — Stop conditions
- Any change to analysis behavior / scoring / segmentation / `regionanalyzer` wiring, or any moved
  snapshot/BIR/oracle number → STOP (the slicer is isolated this layer).
- A §3 verify item contradicts the design's fact-falls-out expectation (e.g. grace spans would force a special
  case) → STOP and surface to Cowork; do NOT add interpretation to "fix" it.
- A branch is coverable only by changing production behavior (dead code) → document as unreachable, do not change
  production.
- The new code needs a threshold / min-gap / merge / snap to pass a test → STOP: that is interpretation leaking in;
  the test or the understanding is wrong, not the zero-interpretation rule.
