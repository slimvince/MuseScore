# CC Instruction — Architectural Layer 2, Phase 2: slice the loaded span (the clip) + re-slice on extend (interim)

> **Context.** Phase 2 of the L1–L3 stabilization plan, per the **corrected** design `cowork_layer2_reslice_design.md`
> (read it — §3/§4/§6 were corrected to the seam-aware form after read-only verification). This is a **build**, but
> **provably byte-identical on every existing call site** (Cowork verified at source: the only users of the span
> overload `build(sc,start,end)` are the new Phase-1a tests; all production/tooling callers use whole-score
> `build(score)`, where the clip is a no-op). The hard part (incremental re-slice) is **Phase 2b — do NOT build it.**
>
> **Grounded facts (verified at source — do not re-derive):** `changePointSlices` (`slicer.cpp:29-71`) builds the
> sorted-unique boundary set from eligible onsets+releases and tiles `[boundaries.front(), boundaries.back())`.
> `build(score)` delegates to `build(sc, scoreStart, scoreEnd)` with `scoreSpan = {firstMeasure tick, endTick}`
> (`note_model.cpp:85-97`), so on whole-score `loadedStart ≤ firstEligibleOnset` and `loadedEnd ≥ lastEligibleRelease`.
> The model exposes `loadedStart()/loadedEnd()` (Phase 1a).

## §0 — Preamble: protect the uncommitted Cowork doc corrections
There are **uncommitted Cowork doc edits** in the tree (the new `cowork_layer2_reslice_design.md`, and the corrected
`cowork_bounded_context_design.md` §4). Commit them **local-only** first so they cannot be swept:
`docs(cowork): Phase-2 L2 re-slice design (seam-aware) + bounded-context §4 correction`. Confirm `git show --stat`
lists only those two files.

## §1 — The change: clip the boundary set to the loaded span
In `changePointSlices`, after the sorted-unique `boundaries` set is built and **before** tiling, **clip it to the
loaded span** (`cowork_layer2_reslice_design.md` §2):
- `clipStart = max(model.loadedStart(), boundaries.front())`; `clipEnd = min(model.loadedEnd(), boundaries.back())`.
- **Clip the multiset, not just the ends:** drop every boundary `< clipStart` or `> clipEnd`, then **inject**
  `clipStart` and `clipEnd`, and re-establish sorted-unique. Then tile `[…)` as today over the clipped set.
- The only out-of-range boundaries that occur are sustained-in onsets `< clipStart` and sustained-out releases
  `> clipEnd` (retention guarantees no eligible release `≤ loadedStart`, no onset `≥ loadedEnd`).
- **Why this is inert on the live path:** on whole-score, `loadedStart ≤ front` and `loadedEnd ≥ back`, so
  `clipStart = front`, `clipEnd = back`, nothing is out of range, and the injected endpoints are already present — the
  clipped set equals the original. Confirm this collapse holds.

## §2 — Re-slice on extend (interim) — no new code beyond §1
Re-slicing after an extend is simply **re-calling `changePointSlices(model)`** on the now-larger model — it is a pure
function of (loaded notes, loaded span), so the result equals a fresh slice over the enlarged span. **Do NOT** build an
incremental/seam-recompute re-slice — that is **Phase 2b** (and it must recompute the seam, §4 of the design; out of
scope here).

## §3 — Tests (assert the REAL invariants, per the corrected §6)
Add to `slicer_tests.cpp`:
- **Degenerate byte-identity:** whole-score slices unchanged — the existing fixtures and the corpus `--validate-slices`
  property hold (the clip is a no-op there).
- **Clip correctness:** with a span-overload model that has a **sustained-in** note (onset `< loadedStart`), its first
  slice starts at `loadedStart` and the note is **in** it — **no slice exists before `loadedStart`**; symmetric for a
  sustained-out note ending at `loadedEnd`.
- **Seam-aware stability on extend (NOT "old slices byte-identical"):** assert **interior real change-points are
  identical** before/after an extend, the **edge slice extends** into the new context, and the **content over the
  original span is unchanged**. (A naïve "all old slices identical" assertion is wrong — §3 of the design — do not
  write it.)
- **Re-slice equivalence:** re-slice after extend `==` `changePointSlices` over a model `build`-t directly on the
  enlarged span.

## §4 — Gate (still byte-identical on production)
- **Degenerate byte-identity is the hard gate:** `composing_tests`, `notation_tests`, `pipeline_snapshot_tests`, and
  the corpus all **unchanged** — the clip is inert on every existing caller (all whole-score). **Any corpus movement →
  STOP** (it would mean the clip is not actually collapsing on whole-score — a real bug).
- Behaviour: the new partial-span tests pass; determinism holds.

## §5 — Scope & unification
- The clip is **inert on all existing callers** (whole-score); partial spans are exercised only by the new tests. **Do
  NOT** wire L2 re-slice into any layer — **L3 reach-back calling extend is Phase 3.** **Do NOT** thread a partial
  selection into the live path.
- One slicer, one tiling path — the clip is added to the existing function, **no second slicer**. End the report with
  the reuse-vs-new ledger and *"No new parallel path or logic duplication was introduced."*

## §6 — Deliver
Commit **locally (unpushed)**: the slicer change + the new tests (`docs` preamble already committed in §0). Write
`cc_layer2_phase2_report.md` (gitignored): the clip as built, the §1 collapse-on-whole-score confirmation, the §3 test
results, the corpus byte-identity proof, and the §5 ledger.

## §7 — Stop conditions
- The corpus or any existing suite moves → STOP (the clip is not inert — a bug, not a refresh).
- You build an incremental/seam-recompute re-slice → STOP (Phase 2b).
- `extend` gets called by any layer, or a partial selection reaches the live path → STOP (Phase 3).
- A second slicer / tiling path appears → STOP (unification).
- A push targets `upstream` → STOP.
