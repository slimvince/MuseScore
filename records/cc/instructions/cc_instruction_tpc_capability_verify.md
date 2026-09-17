# CC Instruction — Phase 4 (tpc spelling capability): read-only verification BEFORE building

> **Context.** Phase 4 of the L1–L3 stabilization plan, per the design `cowork_tpc_capability_design.md` (read it —
> **scope is option B**: build the **shared spelling primitive only**; the Architectural Layer 3 key-spelling *term*
> and its weight are **deferred to Phase B**; the primitive is consumed next by Architectural Layer 4's spelling-pin).
> **This is read-only verification — write NO production code, change NO behaviour.** Its job is to ground the design
> at source so the build (a later, separate instruction) rests on verified facts, not assumptions. Findings only.

## §1 — The make-or-break premise: is `NoteEvent.tpc` actually populated on real scores?
The whole capability interprets the notated spelling Architectural Layer 1 carries. Confirm it is **really there**, not
just declared:
- Find where `NoteEvent.tpc` is **set** on the import / build path (the MusicXML importer and/or the note-model build).
  Quote the assignment and the source field it reads.
- **Check actual values on actual scores** (not just that the field exists): on a handful of the Bach corpus stems,
  are the per-note `tpc` values in range **0–34** (populated), or **`-1`** (not provided)? Report the proportion
  populated. *(If a meaningful share is `-1`, the primitive has no input on those notes — surface this as a blocker
  before any build is written; do not proceed to design the primitive around spelling that isn't there.)*

## §2 — Where the primitive should live, and whether one already exists
- Confirm the **derived-view seam**: `engravingbridge` (the home of `weightedPcView` / `soundingAt`) — is that the
  right place for a spelling-derived view living **beside** L1, **not** inside an analysis layer? Quote the relevant
  declarations.
- **Search for an existing spelling / line-of-fifths / sharp-flat derived view** anywhere in the analysis or bridge
  code. If one exists, the primitive should **extend** it, not add a second (unification). Report what you find (or
  confirm none exists).

## §3 — The interpretation shape to reproduce
- Read `cc_layer3_tpc_keymeasure_report.md` (the prior decode-only measurement). Report the **line-of-fifths /
  sharp-flat interpretation** it used — the exact mapping from `tpc` to line-of-fifths position and to the sharp/flat
  sense, and the span-aggregate (centroid / distribution) shape — so the new primitive reproduces a signal already
  measured to be genuine, not a re-invented one. Note the discarded WIP's term in stash `bc4fa79…` is **reference
  only** (do not re-land its per-layer/decode-only code).

## §4 — Explicitly OUT of scope for this verification
- **Do NOT** investigate or touch the `keymodeanalyzer` scorer seam — the L3 spelling term is **Phase B**, not Phase 4.
- **Do NOT** write the primitive, wire any consumer, or modify any production file. Read-only.

## §5 — Deliver
Write `cc_tpc_capability_verify_report.md` (gitignored): the §1 populated-vs-`-1` finding **with the measured
proportion on real scores** (the gating fact), the §2 seam + existing-view search result, the §3 interpretation shape,
and any seam that differs from the design. End with a one-line verdict: **primitive build is grounded / blocked** (and
why). No commits, no code.

## §6 — Stop conditions
- You find `tpc` is largely `-1` on real scores → STOP and surface (the capability's input is missing).
- You are about to edit any production file, or touch `keymodeanalyzer` → STOP (read-only; L3 term is Phase B).
- A push targets `upstream` → STOP.
