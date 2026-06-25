# Architectural Layer 2 — slicing under bounded context (re-slice on extend) — detail design (Phase 2)

> **Status: DRAFT for sign-off. Read-only design — no code.** Phase 2 of the L1–L3 stabilization plan: make
> Architectural Layer 2 produce slices for whatever span Architectural Layer 1 currently holds, and behave correctly
> when that span is **extended** (the bounded-context contract, `cowork_bounded_context_design.md`). The good news,
> established below, is that slicing is a **pure, stateless function** of (the loaded notes, the loaded span), so the
> additive and re-slice-equivalence invariants hold *by construction* once one clipping rule is fixed — the only real
> design decision here.

## 1. What is there now (verified at source)
`changePointSlices(const NoteModel& model)` is a single pure function: boundaries = the sorted-unique union of every
**onset and release** of eligible notes; consecutive boundaries form slices, tiling **`[firstEligibleOnset,
lastEligibleRelease)`** with no gaps/overlaps; an all-rest interior span is an explicit empty slice; it returns empty
with fewer than two boundaries. It has **no stored state** — re-running it on a model just re-derives the slices.

Phase 1a added to `NoteModel`: the **loaded span** `loadedStart()/loadedEnd()` and the **selection span**
`selectionStart()/selectionEnd()`, and `build` retains every note **overlapping** the loaded span — including
**sustained-in** notes whose onset is *before* `loadedStart`.

## 2. The one real design decision — clip the slicing span to the loaded span
**The subtlety:** because sustained-in notes are retained with onsets *before* `loadedStart`, `firstEligibleOnset` can
be **< `loadedStart`**. The current tiling `[firstEligibleOnset, …)` would then create slices in `[noteOnset,
loadedStart)` — analysing music *outside* the loaded span. That is a scope leak under bounded context.

**The rule (the fix):** slice the **intersection of the loaded span and the eligible-notes span** —
```
[ max(loadedStart, firstEligibleOnset) ,  min(loadedEnd, lastEligibleRelease) )
```
with a sustained-in note **present from `loadedStart`** (clipped) and a sustained-out note **ending at `loadedEnd`**
(clipped). This is the whole design decision, and it does two things at once:
- **Degenerate case (whole score) stays byte-identical.** When the loaded span is the whole score,
  `loadedStart ≤ firstEligibleOnset` and `loadedEnd ≥ lastEligibleRelease`, so the clip collapses to exactly
  `[firstEligibleOnset, lastEligibleRelease)` — today's behaviour, unchanged. (This is what preserves the corpus and
  the leading/trailing-rest behaviour.)
- **Partial selection is correct.** Sustained-in/out notes are clipped to the loaded boundary instead of dragging the
  slicing outside the loaded span.

The function therefore needs the loaded span from the model (the Phase-1a accessors); it stops deriving the slicing
span from the notes alone.

**Two implementation specifics (as-built):** (i) the clip is on the **boundary multiset**, not just the two ends —
**drop** every boundary outside `[clipStart, clipEnd]` and **inject** the two clip endpoints (the only out-of-range
boundaries that occur are sustained-in onsets `< clipStart` and sustained-out releases `> clipEnd`; retention
guarantees no eligible release `≤ loadedStart` and no onset `≥ loadedEnd`). (ii) **Selection-edge silence is not
sliced** — `max(loadedStart, firstEligibleOnset)` means leading/trailing rest *within* the loaded span gets no empty
slice, while *interior* silence still does; this is consistent with today's "don't invent silence outside the note
domain," but it is a deliberate semantic and is stated so on purpose.

## 3. What holds under extend (corrected after CC's read-only verification)
Because slicing is a **pure function of (loaded notes, loaded span)**:
- **Stability — seam-aware (the earlier "old slices byte-identical" claim was wrong).** The clip injects an
  **artificial boundary at `loadedStart`** — *not* a real change-point (a sustained-in note sounds on both sides; the
  boundary is there only because the far side was unloaded). Extend earlier and that artificial boundary **vanishes**,
  so the **edge slice grows outward**. (Counterexample: one eligible note A `[100,1000)`; old span `[500,1000)` → one
  slice `[500,1000)`; extend to `[100,1000)` → one slice `[100,1000)` — the edge slice *grew*, it was not "preserved +
  a new slice prepended.") What actually holds: **(a)** interior **real** change-points within the old region are
  **byte-stable** (extend-earlier only adds notes with `release ≤ oldStart`, so no new real boundary appears
  `> oldStart`); **(b)** the **edge slice abutting the clip extends** into the newly-loaded context, its content over
  the original span unchanged. Symmetric on extend-later (trailing edge). **This breaks no correctness:** L3 re-infers
  fresh over the new slices (forward-only contract), and the edge extension is precisely the "more context at the
  leading edge" that **convergence** (`cowork_bounded_context_design.md` §3.6) is built to absorb.
- **Re-slice equivalence — the correctness-critical invariant.** Slicing the model after an extend equals slicing a
  model `build`-t over the enlarged span directly — both are the same pure function of the same (notes, span). Trivial
  because L2 keeps no state, and it is *what makes the seam extension above benign*. A naïve "old slices byte-identical"
  test would fail on any tie-across-the-clip case; the §6 test asserts the real property instead.

## 4. The interim, and what is deferred
- **Interim (Phase 2, now):** on extend, **re-slice the whole loaded model** (`changePointSlices(model)` again, with
  the §2 clip). Correct and simple — purity makes it identical to an incremental result.
- **Deferred (Phase 2b, byte-identical perf):** an **incremental re-slice** that computes boundaries for the
  newly-loaded region and splices them in — but it **must recompute the seam**, not blindly reuse the old edge slice.
  Because the old clip-edge boundary at the previous `loadedStart` is **artificial** and generically **disappears** on
  extend (§3), a naïve prepend/append would keep a spurious boundary the fresh re-slice does not have — **violating
  re-slice equivalence** (§6.3), the one invariant that must hold. So Phase 2b: drop the old clip-edge boundary unless a
  **real** change-point sits there, recompute only the seam + new region, leave interior boundaries reused. Pure
  optimisation, gated byte-identical to the interim; deferrable past L4, like the L1 incremental index.

## 5. Output vs context (the selection boundary)
L2 produces slices for the **loaded** span; the **output** is only the **selection**. The slices in
`[loadedStart, selectionStart)` ∪ `[selectionEnd, loadedEnd)` are **context (evidence), not output**. L2 itself makes
no analysis judgement — it just slices — so the selection-vs-context distinction is a **thin annotation**: either tag
each slice in-selection/context from the model's selection span, or leave it to the consumer to compute from
`selectionStart/End`. Recommended: compute it at the consuming layer (keep the `Slice` minimal — `[start,end)` only,
per the L2 spec), since L2 owns no selection semantics. **Decision to confirm at build.**

## 6. Invariants & tests (the gate)
1. **Degenerate byte-identity:** for the whole-score loaded span, the slices are **byte-identical** to today — the
   corpus `--validate-slices` property and all slicer fixtures unchanged. (The §2 clip is a no-op there.)
2. **Stability on extend (the seam-aware property, §3):** for many (selection, extension) cases, assert the **real**
   property — **interior real change-points are identical** before/after, the **edge slice extends** into the new
   context (it does *not* stay byte-identical), and the **content over the original span is unchanged**. A naïve "all
   old slices byte-identical" assertion is wrong and will fail on any tie-across-the-clip case — do not write it.
3. **Re-slice equivalence:** re-slice after extend == `changePointSlices` over a model built on the enlarged span.
4. **Clip correctness:** a sustained-in note appears in the first slice (from `loadedStart`), not in a slice before it;
   a sustained-out note's last slice ends at `loadedEnd`.
5. Complete coverage, no gaps/overlaps, exact-note-set identity, empty-slice-for-silence — all preserved over extended
   spans.

## 7. What CC verifies read-only before building
- The exact current tiling and the `firstEligibleOnset`/`lastEligibleRelease` derivation (confirm §1).
- That the Phase-1a loaded/selection-span accessors are present and mean what §2 assumes.
- Whether `changePointSlices` already takes the span or derives it purely from notes (it derives it — §2 is the change).
- A quick check that no current caller depends on the pre-`loadedStart` slices that §2 removes (there should be none —
  today the loaded span *is* the notes' span, so §2 changes nothing on the live path).

## 8. Spec & delivery
- The Architectural Layer 2 spec already carries the bounded-context crosscutting note; on build it gains the §2 clip
  rule as as-built, and the build-state goes to the delivery notes.
- **Phase 2 (interim re-slice + the clip)** is the buildable unit; **Phase 2b (incremental re-slice)** is the separate,
  byte-identical, deferrable perf step. Each is its own gated Claude-Code instruction.
