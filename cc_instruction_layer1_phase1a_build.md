# CC Instruction — Architectural Layer 1, Phase 1a: build-over-a-selection + extend (the contract, interim)

> **Context.** Phase 1a of the L1–L3 stabilization plan (`cowork_l1l3_stabilization_plan.md`), per the design
> `cowork_layer1_extend_design.md` and the contract `cowork_bounded_context_design.md`. **Read both designs first.**
> This is a **build** (not read-only), but it must be **byte-identical on the degenerate case** (selection = whole
> score) — the corpus runs that path and must not move. You are building the bounded-context **supplier API** at
> Architectural Layer 1, with the deliberately-simple **interim** (walk the whole score, retain the notes overlapping
> the loaded span, rebuild the existing index). The hard parts (a span-scoped walk, an incremental index) are **Phase
> 1b — do NOT build them here.**
>
> **Grounded facts (verified at source, do not re-derive):** `NoteModel::build(const Score*)` walks every
> `ChordRest` segment across the whole score (`firstMeasure()` → `next1(SegmentType::ChordRest)`), appends notes in
> (onset, staff, voice, chord-note) order (so `m_notes` is onset-sorted by construction), then calls
> `m_index.build(m_notes)`. `NoteQueryIndex::build(const std::vector<NoteEvent>&)` rebuilds the whole index from a
> note set. Reuse both as-is.

## §0 — Baseline first
Establish/confirm the byte-identity baseline at current HEAD: the corpus `.ours.json` outputs (both presets) and the
pinned snapshots. Every step below is measured against it. (Append `; echo "exit:$?"` to commands; redirect large
output to a file and read a slice — CLAUDE.md bash rules.)

## §1 — The API to add (no behaviour change on the existing path)
On `NoteModel`:
- Keep **`static NoteModel build(const Score* sc)`** — same signature, **same behaviour** (the whole score). Implement
  it as a thin delegate to the span overload over the **full score span** (one walk path, no duplication — see §5).
- Add **`static NoteModel build(const Score* sc, int loadedStart, int loadedEnd)`** — walks the score and **retains
  the notes whose span overlaps `[loadedStart, loadedEnd)`** (`onset < loadedEnd && release > loadedStart` — this
  captures sustained-in notes for free), then builds the index. Records the **loaded span** `[loadedStart, loadedEnd)`
  and the **selection span** (= the same range at build time).
- Add **`extend(Direction dir, int amountTicks)`** — `Direction ∈ {Earlier, Later}`. Grows the loaded span by
  `amountTicks` in that direction, **clamped at the score start/end**, re-derives the retained notes for the new
  loaded span (interim: §2), rebuilds the index, and reports whether the clamp was hit (**`boundaryReached`**). It does
  **exactly one step**; it does **not** loop and **never** evaluates any stop/convergence condition (that is the
  caller's job). `amountTicks` is in **ticks** (Architectural Layer 1 is unit-blind); re-requesting an
  already-covered span is a **no-op**.
- Add read accessors: `loadedStart()`, `loadedEnd()`, `selectionStart()`, `selectionEnd()`, and the last
  `boundaryReached`.

## §2 — The interim implementation (correctness first; efficiency is Phase 1b)
- The walk is **unchanged** (the whole score). Retaining = **filter** the walked notes by the overlap test above. The
  degenerate case (loaded span ⊇ every note) retains **everything** → identical `m_notes` → byte-identical.
- For `extend`, you may either **re-walk and re-filter** to the new loaded span, or **cache the full walked set once**
  and re-filter it (cleaner — no re-walk). Either is acceptable; correctness over speed. **Rebuild the index** from the
  re-filtered `m_notes` via `NoteQueryIndex::build` (do not write a second index path).
- **Append-only semantics:** the loaded span only ever grows; `extend` never shrinks it or drops a retained note.
- Keep `m_notes` **onset-sorted** after any extend (the filter of an onset-sorted walk is onset-sorted; an
  earlier-extension's added notes have smaller onsets and must sort to the front).

## §3 — Invariants (these ARE the gate)
1. **Degenerate byte-identity:** `build(sc)` and `build(sc, fullStart, fullEnd)` produce a model **byte-identical** to
   today's `build(sc)` — same notes, order, and `overlapping`/`onsetIn` answers. **The corpus must not move at all.**
2. **Build-then-extend equivalence:** `build(sc, A0, A1)` then `extend`(s) reaching span `[X0, X1)` yields a model
   **identical** to `build(sc, X0, X1)` directly (notes, order, and query answers on random ranges).
3. **Append-only / no-drop; onset-sort preserved; idempotent extend; boundary clamp + report** (per §1–§2).

## §4 — Tests (add to `note_model_tests.cpp`)
- **Degenerate byte-identity** over the corpus (the standing guard — must be zero movement).
- **Build-then-extend equivalence:** many (selection, extension-sequence) cases asserting equality to the direct
  `build(sc, X0, X1)` — including reaching the same final span in one big step vs several small ones (determinism
  independent of increment).
- **Extend unit tests:** earlier/later, append-only, idempotent re-request, clamp at score start/end + `boundaryReached`.
- **Sustained-in capture:** a note onset **before** `loadedStart` whose release is **after** it is retained.
- **Index ≡ linear scan** over the post-extension model (extend the existing IDX property tests).

## §5 — Unification (standing rule)
- `build(sc)` **delegates** to the span overload (one walk path). The index is the **existing** `NoteQueryIndex`,
  rebuilt — **no second index, no second walk, no third structure.** End the report with the reuse-vs-new ledger and
  *"No new parallel path or logic duplication was introduced."*

## §6 — Call sites & scope (keep the live path byte-identical)
- Find the `NoteModel::build` call sites (region analyzer, `batch_analyze`, tests). **Leave them on `build(sc)`** (the
  full-score path) — do **not** thread a partial selection into the live analysis, and do **not** call `extend` from
  any layer. Partial-selection wiring is the product integration; **reach-back (L3 calling `extend`) is Phase 3.**
  Phase 1a delivers the L1 capability + tests only.

## §7 — Deliver
- Commit **locally (unpushed)**; `cc_*` report gitignored. Write `cc_layer1_phase1a_report.md`: the API as built, the
  interim choice (re-walk vs cache), the §3 invariants confirmed, the §4 test results, the corpus byte-identity proof,
  and the §5 ledger. **Do not sync the L1 spec yet** — spec sync is Phase 5 (the spec already marks `extend`
  designed-but-unbuilt; leave it).

## §8 — Stop conditions
- **The corpus moves at all** (degenerate case not byte-identical) → STOP and surface (a real bug, not a snapshot
  refresh).
- You start a **span-scoped walk** or an **incremental/insertable index** → STOP (that is Phase 1b).
- `extend` gets **called by any layer**, or a partial selection is threaded into the live path → STOP (Phase 3 /
  product integration).
- A **second index, second walk path, or new window/query structure** appears → STOP (unification).
- A push would target `upstream` → STOP (fork-local; `origin` only, and only after ratification).
