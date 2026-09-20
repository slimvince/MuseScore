# CC report — Architectural Layer 1, Phase 1a: build-over-a-selection + extend (interim)

> Status: BUILD complete, gated. Fork-local, committed unpushed. Designs:
> `cowork_layer1_extend_design.md`, `cowork_bounded_context_design.md`; plan
> `cowork_l1l3_stabilization_plan.md` (Phase 1a).

## §0 — Baseline (current working tree, before this change)
- Build: `ninja: no work to do` on entry — the existing `ninja_build_rel` binary already
  reflects the working tree. Spot-checked the existing `tools/corpus/{baroque,jazz,default}`
  `.ours.json` against a fresh single-score regen from that binary (bwv10.7, bwv272, bwv352,
  bwv244.15) → **MATCH** on all three presets ⇒ the committed corpus IS the current-binary
  baseline. Snapshotted per-file SHA-256 of all 353 `.ours.json` × 3 presets into
  `scratch_baseline/{baroque,jazz,default}_baseline.sha256`.
- Tests at baseline:
  - `composing_tests`: **617 passed**, 0 failed, 1 disabled.
  - `notation_tests`: 52 passed, **5 FAILED** — PRE-EXISTING in the working tree (Cowork's
    uncommitted changes), NOT introduced here:
    `Notation_ImplodeTests.MozartK279OpeningPrefersCMajorOverFLydian`,
    `Notation_ImplodeTests.CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord`,
    `Notation_ImplodeTests.PopulateChordTrackEmitsCadenceMarkersOnCorelli`,
    `NotationInteractionHarmonyPinning.BehaviorSnapshot_RomanNumeral`,
    `NotationInteractionHarmonyPinning.BehaviorSnapshot_Nashville`.
  - `pipeline_snapshot_tests`: pass (3 disabled, 1 skipped observation).

## §1 — API as built (note_model.h)
On `NoteModel`:
- `enum class Direction { Earlier, Later }`.
- `static NoteModel build(const Score* sc)` — **unchanged signature/behaviour**; now a thin
  delegate to the span overload over the full structural score span (one walk path).
- `static NoteModel build(const Score* sc, int loadedStart, int loadedEnd)` — walks the score,
  retains notes whose span overlaps `[loadedStart, loadedEnd)`
  (`onset < loadedEnd && release > loadedStart`), records loaded span and selection span
  (== same range at build), builds the index.
- `void extend(Direction dir, int amountTicks)` — grows the loaded span by `amountTicks` (ticks)
  in `dir`, clamped at the score start/end; re-derives retained notes (interim re-walk) and
  rebuilds the index; sets `boundaryReached`. Exactly one step; never loops or evaluates a
  stop condition. Non-positive amount, or an already-covered request, is a no-op. Append-only.
- Accessors: `loadedStart()`, `loadedEnd()`, `selectionStart()`, `selectionEnd()`,
  `boundaryReached()`.

## §2 — Interim choice: RE-WALK (not cache)
`extend` calls the private `rebuildForLoadedSpan()`, which **re-walks the whole score** and
re-filters to the current loaded span, then rebuilds the static `NoteQueryIndex`. Chosen over
caching the full walked set because:
- it adds **zero** members/memory to the degenerate (whole-score / corpus) path — the live path
  is untouched in footprint;
- `extend` is never called on the live path (§6), so the re-walk cost is irrelevant to production;
- correctness over speed (Phase 1b is the span-scoped walk + incremental index).
`build(sc, lo, hi)` and `extend` share the SAME `rebuildForLoadedSpan` walk — one walk path.

## §3 — Invariants confirmed
1. **Degenerate byte-identity** — corpus diff below (§ corpus) + EXT1 in-process.
2. **Build-then-extend equivalence** — EXT2 (to full) / EXT3 (interior).
3. **Append-only / no-drop; onset-sort; idempotent extend; boundary clamp + report** — EXT2/EXT4.

## §4 — Tests added (note_model_tests.cpp) — ALL PASS
7 new tests, all green; **`composing_tests` 617 → 624 passed, 0 failed, 1 disabled**.
- **EXT1** degenerate retains-all (`build(sc)` ≡ unbounded-span build; loaded==selection==score
  span) + 100 random query-identity ranges per fixture.
- **EXT2** build→extend reaches the whole-score model (notes/order/loaded span/query answers
  identical to `build(sc)`); one-big-step **and** many-small-steps both land identical
  (determinism vs granularity); append-only asserted each step.
- **EXT3** interior build-then-extend ≡ direct `build(X0,X1)` (no clamp; selection span
  deliberately not compared); 200 random query ranges.
- **EXT4** extend semantics: non-positive = no-op; grow-within-bounds; clamp at start/end +
  `boundaryReached`; idempotent re-request at boundary (notes unchanged); append-only.
- **EXT5** sustained-in capture: C4 [0,9600) retained in selection [4800,5000) (onset < loadedStart).
- **EXT6** index ≡ linear oracle over a post-extension model (300 ranges/fixture).
- **EXT7** extend on a null/empty model is a safe no-op.

Run over every `nm_*` fixture (ties, sustains, grace, multi-staff/voice, flags, eligibility,
dense onsets). Both other suites unchanged: `notation_tests` 52 pass / **same 5 pre-existing
failures, zero new**; `pipeline_snapshot_tests` pass.

## §5 — Unification ledger
- REUSED: the existing whole-score walk (moved verbatim into `rebuildForLoadedSpan`, plus an
  overlap filter); `NoteQueryIndex::build` (the one index, rebuilt); `makeEvent`; the score
  walk structure (`firstMeasure`→`next1`).
- NEW: `build(sc, lo, hi)`, `extend`, `rebuildForLoadedSpan`, `scoreSpan` helper, the span/score
  bookkeeping members, accessors. No second index, no second walk path, no new window/query
  structure.
- `build(sc)` delegates to the span overload. **No new parallel path or logic duplication was introduced.**

## §6 — Call sites
All `NoteModel::build` call sites (region analyzer, section analyzer, batch_analyze, bridge
helpers, tests, regiontone primitives) remain on `build(sc)` (full-score). No partial selection
threaded into the live path; `extend` is not called by any layer (Phase 3).

## Corpus byte-identity gate — PASS (the §3 invariant 1 / §8 stop condition)
Regenerated all three presets from the post-change binary and diffed per-file SHA-256 against the
pre-change baseline snapshot (`scratch_baseline/*_baseline.sha256`, taken before editing):
- **Baroque: BYTE-IDENTICAL** (353/353).
- **Jazz: BYTE-IDENTICAL** (353/353).
- **Default: BYTE-IDENTICAL** (353/353).
- `git status tools/corpus/` clean — even the `corpus_manifest.json` reproduced identically.

The degenerate case did **not move a single byte** → the corpus did not move → Phase 1a is
provably inert on the live path, as designed.

### Note on absolute BIR counts (NOT a Phase-1a effect)
`characterise_bir_false.py` on the regenerated corpus reports **Baroque 53 / Jazz 24 / Default 53**,
which differs from the CLAUDE.md-documented gate (57 / 23 / 57). This gap is **pre-existing in the
working tree** (Cowork's uncommitted in-flight changes already moved it) and is **independent of
this change**: the corpus is byte-identical to the pre-edit snapshot, so Phase 1a moved nothing.
Surfaced here for visibility; the Phase-1a gate is byte-identity vs the pre-change baseline, which
passed. (Not a stop condition for §8 — the corpus did not move relative to baseline.)

## Stop conditions (§8) — none hit
- Corpus did not move (byte-identical) — no STOP.
- No span-scoped walk and no incremental/insertable index introduced (interim re-walk + index
  rebuild only) — Phase 1b boundary respected.
- `extend` is not called by any layer; no partial selection threaded into the live path.
- No second index / second walk path / new window structure.
- No push; fork-local. Committed to the local branch only.

## Delivery
- Local commit (unpushed) of the three files: `note_model.h`, `note_model.cpp`,
  `note_model_tests.cpp`. This `cc_*` report is gitignored.
- Spec NOT synced (Phase 5 owns spec sync; the L1 spec already marks `extend`
  designed-but-unbuilt).
