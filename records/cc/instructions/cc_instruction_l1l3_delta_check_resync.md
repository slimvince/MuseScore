# CC Instruction — L1–L3 spec↔as-built delta-check (re-run for Phase-5 sign-off) — READ-ONLY

> **Why.** Phase-5 sign-off (ledger item E15): before the **L1–L4 COMPLETE** gate, confirm the L1–L3 **design docs match
> the as-built**, so Cowork can sync exactly what diverged (not rewrite blind). Much has landed since the last
> delta-check: the **bounded-context capabilities** (L1 `build-over-span` + `extend`; L2 clip + re-slice; L3 reach-back),
> the **tpc `spellingview` primitive**, the **types-only leaf header** (`analysistypes.h`) relocation + the
> `PitchContext` un-nest, and the **kMasks single-source**. **READ-ONLY — findings only, no source/doc edits.**
> *(Reminder: the never-bash rule is Cowork's; it does not constrain your build/test/tool runs.)*

## §1 — Per-layer delta-check (spec doc ↔ as-built source)
For each layer, compare the **design doc** to the **as-built code** and report every **DIVERGENCE** (doc says X,
code does Y), every **MISSING** (built capability not in the doc), and every **STALE** (doc describes something no
longer true). Cite doc-section ↔ file:line.
- **L1 — `cowork_layer1_note_model_design.md`** ↔ `notemodel/note_model.{h,cpp}`: the `build(score)` /
  `build(score,lo,hi)` overloads, `extend(Direction, ticks)` + `boundaryReached()`, the interim rebuild, the
  `NoteEvent.tpc` field. Is the doc's contract the as-built contract?
- **L1.5 — the engraving-bridge / tpc doc(s)** (`cowork_tpc_capability_design.md` + any bridge doc) ↔
  `engravingbridge/spellingview.{h,cpp}` + `regiontonecollector`/`regiontoneprimitives`: the `spellingview` primitive
  (`lineOfFifths`/`sharpFlatSense`/`spanSpelling`, `tpcIsValid`, signature-agnostic span); is it doc-accurate and
  marked capability-only (no production consumer yet)?
- **L2 — `cowork_layer2_slicing_design.md`** ↔ `slicing/slicer.{h,cpp}`: the loaded-span clip + re-slice-on-extend
  (seam-aware), the degenerate byte-identity. Doc ↔ code.
- **L3 — `cowork_layer3_keymode_design.md` + `cowork_layer3_reachback_design.md`** ↔ `key/*` + the reach-back
  orchestration in `regionanalyzer.cpp`: the emission scorer, the sequence Viterbi, the reach-back loop (trigger /
  converge / output-filter), and the §11 leading-tone-gate **known issue** note.

## §2 — Cross-cutting structural deltas (must be reflected in the layer/architecture docs)
- **Types-leaf header:** the value-type closure now lives in `analysis/types/analysistypes.h`; the two header
  back-edges (`regiontonecollector.h`, `keymodeanalyzer.h` → L4) are **gone**; `PitchContext` is un-nested with a
  `KeyModeAnalyzer::PitchContext` alias. Do the docs/`ARCHITECTURE.md` reflect this (or still describe the old layout)?
- **kMasks single-source:** `kTemplateIntervals` is the sole interval source feeding both `templates[]` and `kMasks`.
  `docs/scoring_model.md` was synced — confirm it's accurate; flag any other doc still describing the hand-sync.
- **Bounded-context ENGAGEMENT status:** the docs should say the bounded-context is built as a **capability** with
  production still whole-score (engagement deferred to Phase 5b) — confirm no doc overstates it as engaged.

## §3 — Deliver
Write `cc_l1l3_delta_check_resync_report.md` (gitignored): a per-item table — **doc location ↔ code location ↔
{DIVERGENCE | MISSING | STALE | OK}** — so Cowork can do a precise spec-sync. Flag anything where the *code* looks wrong
vs the *design intent* (a possible defect) separately from doc-staleness. **No edits.**

## §4 — Stops
- Any source/doc edit (read-only) → STOP.
- A push targets `upstream` → STOP.
