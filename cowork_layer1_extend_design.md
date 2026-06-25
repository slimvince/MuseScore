# Architectural Layer 1 — build-over-a-selection + extend — detail design (Phase 1 of the L1–L3 stabilization)

> **Status: DRAFT for sign-off. Read-only design — no code.** Implements the supplier side of the bounded-context
> contract (`cowork_bounded_context_design.md`) at Architectural Layer 1: build the note model over the **user's
> selection**, and **extend** the loaded span on request. This is the foundation Phase-1 step; the genuinely hard part
> (the look-up index under extension) is isolated and **deferred behind a byte-identical interim**, so the *contract*
> lands first and the layers above are written against it immediately.

## 1. What is there now (verified at source, `note_model.h`)
- `NoteModel::build(const Score*)` — **walks the whole score** (every staff, voice, segment, grace), resolves ties,
  annotates each note, sorts by onset (then staff, voice, chord-note). One whole-piece build.
- `m_notes` — the onset-sorted `NoteEvent` list (the lossless store).
- `NoteQueryIndex` — the look-up index, **static, built once** from `m_notes`:
  - `m_onsets` — onset keys, ascending (binary search for `onsetLowerBound`/`onsetIn`).
  - `m_segMaxRel` — a **max-release segment tree**, a *perfect binary tree* sized to a power of two, built once;
    `overlapping` descends it, pruning any subtree whose max release ≤ t0.
- Queries: `overlapping(t0,t1)` (`onset < t1 && release > t0`, no horizon) and `onsetIn(t0,t1)`.

The two things that make extension non-trivial: the note list must stay **onset-sorted** as notes are added at the
**front** (earlier extension) or **back** (later extension), and the index is a **static perfect-binary-tree** that
does not natively accept insertions.

## 2. The API change (the contract)
- **`build` over a selection** — given the score and a **selection span** `[selStart, selEnd)`, build the note model
  holding the notes the selection needs (Section 4). The model records its **loaded span** `[loadedStart, loadedEnd)`
  (initially the selection) and the **selection span** (so the layers above can tell output slices from context
  slices — though that labelling is their concern, not Architectural Layer 1's).
- **`extend(direction, amount)`** — grow the loaded span **earlier** or **later** in time by the **requested amount,
  expressed in ticks** (a target tick, or a tick span). Architectural Layer 1 is **unit-blind** — it knows ticks, not
  slices or measures — so the requester converts its own natural unit to a tick target before calling (Architectural
  Layer 3 reach-back: a *measure*, mapped to a tick via the score's time signature; Architectural Layer 4: a
  *neighbour slice*). The **finest meaningful step is the change-point/slice**: within a slice the sounding set is
  constant, so a sub-change-point (beat/tick) extension loads no new note and changes no analysis — requesters never
  ask finer than that. Loading is **append-only** (never drop a loaded note). Returns the **new loaded span** and a
  **boundaryReached** flag (true when clamped at the score start/end). Re-requesting an already-covered span is a
  **no-op** (idempotent). **`extend` does exactly one requested step** — it loads what it is asked for and returns; it
  does **not** loop, and it **never evaluates a stop/convergence condition** (that is inference, which Architectural
  Layer 1 does not do).
- **Queries unchanged** (`overlapping`, `onsetIn`, `notes`) — they simply operate over whatever is currently loaded.
- The decision to extend, the **increment size**, the **convergence/stop test**, and the **extend → re-infer →
  re-check loop** all live in the **requesting layer**, never here (single responsibility — Architectural Layer 1
  supplies the requested notes for one step; it does not reason about key, and it does not loop). The increment is the
  requester's natural inference scale (`cowork_bounded_context_design.md` §3.8), so it is a per-call parameter, not a
  fixed Architectural-Layer-1 constant.

## 3. The two-level delivery — the de-risking
The hard parts (capturing sustained-in notes without a whole-score walk; an extensible index) are **separated from the
contract** so Phase 1 is low-risk:

- **1a — the contract, with an interim that is correct and byte-identical.** `build(selection)` and `extend` present
  the full bounded-context API, but **internally may still walk the whole score and retain the notes overlapping the
  loaded span**, and **rebuild the static index** over the loaded set on build and on each extend. This is trivially
  correct (the whole-score walk already captures every note, including sustained-in ones — Section 4 is free), it is
  **byte-identical to today on the degenerate case** (selection = score → retain everything → identical), and it gives
  the layers above the real API to build against. Performance is *not* improved yet — that is the point: ship the
  contract, not the optimisation.
- **1b — the efficiency, byte-identical, DEFERRED (can land after L4).** Replace the interim with (i) a walk scoped to
  the loaded span plus a leading-edge "sounding-at-`loadedStart`" lookup (Section 4), and (ii) an **extensible index**
  (Section 5). **Gate:** byte-identical to 1a, and `index ≡ linear scan` over extended spans. Because 1b changes no
  behaviour, it is purely a performance step and never blocks the layers above.

This split means the **foundational assumption is corrected now** (everything above is written to build-selection +
extend) while the genuinely tricky code is done later under a byte-identity gate.

## 4. What `build(selection)` must capture — and the sustained-in subtlety
The loaded model must hold **every note whose span overlaps the loaded span** — `onset < loadedEnd && release >
loadedStart` — which includes a note that **started before `loadedStart` and sustains into the selection** (it really
sounds during the selection; it is content, not mere context). 
- **In 1a (interim)** this is free: the whole-score walk sees every note; filtering by overlap keeps the sustained-in
  ones automatically.
- **In 1b (deferred)** it is the non-trivial correctness point: a span-scoped walk must additionally find, at
  `loadedStart`, the note active in each track (the last onset ≤ `loadedStart` with release > `loadedStart`) via the
  score's tick-addressed structure — **without** re-introducing the old backward horizon and **without** walking from
  the score start. This is flagged as the item 1b must verify against the engraving DOM (a read-only spike before 1b).
- Distinguish this from **reach-back** (Architectural Layer 3): reach-back loads notes *entirely before* the selection
  as **key evidence**; sustained-in capture loads notes that *sound inside* the selection. Different needs, same
  supplier mechanism.

## 5. The index under extension (the crux)
- **1a:** **rebuild** `NoteQueryIndex` from the merged onset-sorted `m_notes` on every build and extend — `O(M log M)`
  in the loaded count `M`. Simple, correct, and identical to a fresh build over the enlarged span. Acceptable because
  extensions are few (bounded by the stop condition) and `M` is the selection, not the whole score.
- **1b (deferred) options**, to be chosen on measurement, all byte-identical to the 1a rebuild:
  - a **merge + rebuild** that reuses the sorted halves (earlier/later extension is a prepend/append, so the merge is
    `O(M)`), rebuilding only the segment tree;
  - or a segment tree sized with **headroom** and rebuilt only when capacity is exceeded;
  - or a different overlap structure that accepts ordered insertion (e.g. an interval/Fenwick variant) — only if the
    rebuild proves a measured bottleneck.
  The **interface is unchanged**, so the choice is invisible above Architectural Layer 1.

## 6. Invariants (the correctness contract every step must hold)
1. **Degenerate byte-identity.** `build(selection = whole score)` and a never-extended model are **byte-identical** to
   today's `build(score)` — same notes, same order, same query answers. (The corpus runs this path; it must not move.)
2. **Build-then-extend equivalence.** `build(A)` then `extend` to span `X` yields a model **identical** to `build(X)`
   directly — extension is an optimisation of "load more, build fresh," never a different result. (This is the L1
   half of the cross-layer equivalence invariant in `cowork_bounded_context_design.md` §4.)
3. **Append-only / no-drop.** Extension never removes or alters an already-loaded note; `m_notes` only grows.
4. **Onset-sort preserved** across front (earlier) and back (later) extension.
5. **Idempotent extend.** Re-requesting a covered span is a no-op; overlapping requests load only the genuinely-new
   notes once.
6. **Boundary clamp + report.** Extension never passes the score start/end; it clamps and sets `boundaryReached`.

## 7. Tests
- **Degenerate byte-identity** over the whole corpus (the standing guard for Phases 1–3).
- **Build-then-extend equivalence:** for many selection + extension sequences, assert the model equals `build` over the
  final span (notes, order, and `overlapping`/`onsetIn` answers on random ranges).
- **Extend unit tests:** append-only, idempotent re-request, front/back ordering, boundary clamp + `boundaryReached`.
- **Sustained-in capture:** a note started before the selection and sounding into it is present (1a free; the explicit
  test that guards 1b).
- **Index ≡ linear scan** over extended spans (extends the existing IDX property tests to the post-extension model).

## 8. Risks / hard sub-problems (named, so they are not discovered late)
- **Sustained-in without a whole-score walk** — the 1b correctness point (Section 4); de-risked by a read-only DOM
  spike before 1b, and irrelevant to 1a.
- **The extensible index** — the 1b performance point (Section 5); irrelevant to 1a (rebuild).
- **Determinism independent of extension granularity** — reaching span `X` in one big step or several small ones must
  give an identical model (a required test; falls out of invariant 2).
- **Composition with re-analyse-a-sub-range** — extension (grow the loaded span) and the existing incremental
  re-analysis (re-run part of it) are different operations on the same model; they must not interfere. Flagged for the
  Phase-3 (reach-back) and later incremental work, not blocking Phase 1.

## 9. Spec & delivery
- The Architectural Layer 1 spec already marks *extend* designed-but-unbuilt and §11 as interim behind this contract;
  on build, those become as-built, and the build-state/commits go to the delivery notes (architecture prose stays
  code-free, per the standard).
- **Phase 1a** (contract + interim) is the buildable unit now; **Phase 1b** (efficiency) is a separate, byte-identical,
  deferrable step. Each is its own gated Claude-Code instruction; 1b gets the DOM spike first.
