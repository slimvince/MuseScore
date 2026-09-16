# CC Instruction — SYNC all canonical documentation to the layer-1 as-built reality

> **Standing rule (new, user mandate 2026-06-21): all documentation is kept in sync with the code — like
> regression tests and code comments. Doc drift is a defect, not a backlog item.** Layer 1 (the lossless
> tie-resolved NOTE MODEL, `e30bb45a4f`; coverage `4055f89082`) shipped with **zero** canonical-doc updates.
> Close that now. **DOC/COMMENT-ONLY — no production / behavior / scoring change.** Both suites must stay
> byte-identical (snapshot/BIR/oracle unchanged); if any metric moves, a non-comment edit slipped in → STOP.
>
> Cowork has already synced the `cowork_*` design docs + `cowork_handoff.md` (the standing rule). This
> instruction covers the **tracked canonical docs + code comments**, committed as a doc-sync commit.

## §0 — Verified drift (Cowork, at source, 2026-06-21) — the anchors
- **`ARCHITECTURE.md` (root): 0 mentions of the note model.** It still describes the **old segment-first** spine
  only — `greedyExpandSegmentation` (~L609), sparse "≤2-PC slices" (~L610/634), `analyzeHarmonicRhythm` +
  same-root/quality merge (~L2800/2835). No `notemodel` layer, no rebuild plan.
- **`docs/` tree: 0 mentions of the note model** anywhere (`grep -ri "note.?model" docs/` → empty). The single
  stage tracker `docs/implementation_roadmap.md` does **not** record layer 1 as done.
- **Known stale code comment `[verify before fixing]`:** `regiontoneprimitives.cpp` header comment says the
  backward reach is "**4 quarter notes**" but the code is `Fraction(4,1)` = **4 whole notes**. Confirm the exact
  comment text + the `Fraction` at source before editing; fix the comment to match the code (do NOT change the
  `Fraction` — that is behavior).

## §1 — What "in sync" means here (the as-built facts to land)
Layer 1 introduced a **lossless, tie-resolved note model** as a **separate module** (`composing/.../notemodel/note_model.{h,cpp}`),
the single source of truth (11 fields per note: `{pitch, tpc, staff, voice, onset, release, duration, isGrace,
plays, visible, staffEligible}`), with derived views (`weightedPcView` = the recomputed `collectRegionTones`
weighting incl. tie **de-inflation**; `soundingAt`). `collectRegionTones`' **note-reading** half is replaced by
the model; its **weighting** half survives as that derived view, consumed **unchanged** by the still-live
segment-first analyzer. The coarse/sub/merge machinery **still runs and still drives analysis** — it is
**transitional**, retiring only when layer 3 consumes the slicer. Trade-off on record: faithful tie de-inflation
moved the oracle metric +3/+1/+1 charged (KEY/FLOOR flat, BIR −2/+1/−2), accepted as a correct-upstream /
frozen-downstream wobble that re-tunes at layer 3.

This sits inside the ratified **4-layer target** (`cowork_target_architecture.md`): note model (L1, DONE) →
change-point slicing (L2) → per-slice analysis with context (L3) → grouping for display (LN).

## §2 — Edits (tracked canonical docs)
1. **`ARCHITECTURE.md`** — add the note-model layer as **as-built**: a short section describing the module, its
   role (lossless source of truth), the 11 fields, and the two derived views; state that `collectRegionTones`'
   note-reading is now the note model and the weighting is `weightedPcView`. **Re-frame, do NOT delete**, the
   existing segment-first description as **transitional** (still the running analysis spine until layer 3). Add a
   one-paragraph pointer to the 4-layer rebuild target + that L2 is next. Keep it factual and concise; match the
   doc's existing voice/section style.
2. **`docs/implementation_roadmap.md`** — record **Layer 1 (note model) = DONE/ratified** as a stage item with its
   evidence (commits `edd33901ed` metric tool, `e30bb45a4f` note model, `4055f89082` coverage; ratified
   2026-06-21; the +3/+1/+1 trade-off). Reflect that L2 (slicing) is the next sweep step. Honor the roadmap's
   "evidence required to mark done" standing rule.
3. **`docs/layer_architecture_audit.md`** — add a dated note that layer 1 has been rebuilt as the note-model layer
   (the audit predates it); only if it claims a current layer structure that is now stale. Use judgment — if it
   reads as a historical audit, a one-line "superseded for L1 by the note-model rebuild (2026-06-21)" suffices.
4. **Code comment fix** — the verified `regiontoneprimitives.cpp` "4 quarter notes" → "4 whole notes" (comment
   only, after confirming at source).

## §3 — Drift sweep (the rule is ALL docs, not just the anchors)
Because the standing rule is *all* documentation in sync, do a bounded sweep for residual layer-1 drift, and fix
what you find (doc/comment-only):
- `grep -rin "tone collection" ARCHITECTURE.md docs/` and `grep -rin "note.?model" ARCHITECTURE.md docs/` —
  reconcile any place that frames "tone collection = layer 1" or implies the analyzer reads notes directly.
- Scan the new module + `engravingbridge` for header/inline comments that still describe the **old** ownership
  (e.g. comments claiming the analyzer collects tones rather than reading the note model). Fix only clearly-stale
  comments; when unsure, **list it in the report** rather than guessing (no-assume).
- Do **NOT** chase comments in the soon-to-be-replaced segment/detector code beyond layer-1 ownership facts —
  that churn lands when those layers are rebuilt.

## §4 — Gate
- **Doc/comment-only.** No `.cpp`/`.h` behavior change; `composing_tests` + `notation_tests` + snapshot tests pass
  **byte-identical**; BIR/oracle unchanged. A moved metric = a real code change slipped in → STOP, revert, surface.
- `ARCHITECTURE.md` now describes the note-model layer as-built AND keeps an accurate transitional description of
  the still-live segment-first spine (don't orphan the running code).
- `docs/implementation_roadmap.md` records L1 done with evidence.
- The verified stale comment is fixed; the sweep's findings are either fixed or listed.

## §5 — Workflow + deliver
Commit **locally (unpushed)** as a single doc-sync commit (`docs(composing): sync architecture docs + comments to
the layer-1 note-model as-built`). Write `cc_layer1_doc_sync_report.md`: the exact diffs/sections added to
`ARCHITECTURE.md` + the roadmap, the comment fix (before/after + the `Fraction` confirmation), the sweep findings
(fixed vs listed), and the byte-identity confirmation (both suites + snapshot + BIR/oracle unchanged). Cowork
verifies the commit is doc/comment-only and the as-built statements match source; user ratifies. This closes
layer 1 as **correct + covered + documented** before layer 2.

## §6 — Stop conditions
- Any production/behavior/scoring change (anything beyond docs + verified comment text) → STOP (a moved
  snapshot/BIR/oracle number is the tell).
- A comment's correct wording is genuinely ambiguous at source → do NOT guess; list it in the report.
- The push of the layer-1 checkpoint (`cc_instruction_push_layer1_checkpoint.md`) and this doc-sync are separate;
  if both are pending, this doc-sync commit simply stacks on top — fork-only if pushed, never `upstream`.
