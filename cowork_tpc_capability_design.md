# tpc spelling capability — the shared spelling primitive (Phase 4, the maximal-information foundation) — detail design

> **Status: DRAFT for sign-off. Read-only design — no code.** Phase 4 of the L1–L3 stabilization plan, the **last
> build-it-right step before L4**. It builds the **maximal-information capability**: the algorithm should use the
> *notated spelling* the score gives us, not bare pitch class. Architectural Layer 1 already carries the tonal pitch
> class per note (`NoteEvent.tpc`, a line-of-fifths spelling, real range `−8 … 40`; verified at source). Phase 4 builds the **one
> shared primitive** that interprets that spelling, so both Architectural Layer 3 (key) and Architectural Layer 4
> (chord) read it through a *single* place — **never duplicated per layer** (the unification rule the L3 §15 to-do
> already flagged). **This is capability, not precision tuning:** it lands **BIR-flat**, and the *weight* by which L3
> leans on spelling is a **Phase-B** item.
>
> **Scope ratified (option B, 2026-06-26):** Phase 4 builds the **shared primitive only**. The Architectural Layer 3
> key-spelling *term* and its *weight* both move to **Phase B** (term-with-its-tuning). The primitive is not premature —
> Architectural Layer 4's spelling-pin (the next build) consumes it. So `keymodeanalyzer` is **untouched in Phase 4**.

## 1. The shared tpc-interpretation primitive (the capability)
A single derived primitive — living beside the other Architectural Layer 1 derived views
(`engravingbridge`, with `weightedPcView`/`soundingAt`), **not** inside any analysis layer — that turns the notated
`tpc` into spelling semantics:
- **Per-note:** the **line-of-fifths position** of a note's spelling (so `G♯` and `A♭` are distinguished), and the
  derived **sharp-side / flat-side** sense. This is what Architectural Layer 4's **symmetric-root spelling-pin** needs
  per note (a `G♯dim7` vs `A♭dim7` is decided by spelling).
- **Aggregated over a span:** the **line-of-fifths centroid / sharp-flat distribution** of a window's spellings — the
  **modulation-direction** signal Architectural Layer 3's key emission wants (sharp-side motion ⇒ dominant direction,
  flat-side ⇒ subdominant). The prior decode-only measurement (`cc_layer3_tpc_keymeasure_report.md`) established this
  is genuine spelling signal; its *shape* is known.

Both are the **same interpretation** of the same `tpc` — one primitive, two read shapes (per-note for L4, aggregate
for L3). That is exactly why it is shared, not duplicated.

**Validity & mapping (verified at source, 2026-06-26).** Line-of-fifths position = `tpc − TPC_C` with `TPC_C = 14`
(+1 tpc = +1 fifth; `pitchspelling.h`). Sharp/flat sense = the sign of that offset. **The primitive must test presence
with `tpcIsValid()` (= `−8 ≤ tpc ≤ 40`), never `tpc >= 0` / `tpc != −1`:** the flat side of the line of fifths is
**negative** (`TPC_F_BB = −1`, down to `TPC_F_BBB = −8`), so a `>= 0` guard silently drops every double-flat-ish
spelling — and `−1` is a *legitimate* spelling (Fbb), not "absent."

> **Be precise about what `tpcIsValid` does and does not do (CC pin, verified).** `tpcIsValid(−1)` returns **true**, so
> the function does **not** distinguish a real Fbb (`−1`) from the field's "absent" default (`−1`). It is still the
> right guard — it keeps the real flat-side range that `>= 0` wrongly drops. The thing that actually keeps a spurious
> "absent" out of the primitive is the **build-path invariant**, not `tpcIsValid`: every `NoteEvent` on the build path
> is assigned `e.tpc = n->tpc()` from a real DOM note, so the `−1` default never survives to a consumer. (The latent
> ambiguity this leaves is §5.)

## 2. Architectural Layer 3 — the key-spelling term is DEFERRED to Phase B (scope ratified: option B)
**Phase 4 builds the shared primitive only; it does NOT touch the Architectural Layer 3 key emission.** The ratified
scope keeps the L3 spelling *term* together with its *tuning*: the line-of-fifths / modulation-direction term in the
`keymodeanalyzer` scorer, **and** the weight that realises it, both land in **Phase B**, where the precision work
lives. Reason: a dormant weight-0 L3 term would be code with no effect and no test that exercises its effect; landing
the term *with* its calibration (where the stable-region cost is measured and Layer-5 function can gate the
tonicization-vs-modulation call) is cleaner under "build-it-right **then** tune-precision."

This does **not** make the primitive premature: it is consumed **now** by Architectural Layer 4's spelling-pin (§3,
the next build). The capability lands early and used; only the *tuning-coupled* L3 reading-path waits for Phase B.
(`keymodeanalyzer` is therefore **out of scope for Phase 4** — the §6 verification does not need its scorer seam.)

## 3. Architectural Layer 4 — the spelling-pin (forward note; built with L4, not here)
Architectural Layer 4's rewritten spec already requires the **deterministic spelling-pin** for symmetric roots (the
notated spelling *names* the root — no degradation). It reads the **per-note** shape of this same primitive. It is
built **with L4** (the next algorithmic build), not in Phase 4 — but Phase 4 is what makes the primitive available so
L4 is spelling-aware **from the start**, never retrofitted. This is the clean, deterministic, *Phase-A* use of tpc
(unlike the L3 key term, which is tuning-coupled / Phase B).

**Where the unification actually bites (verified at source).** L3 interprets tpc **not at all** (the `PitchContext` it
decodes from carries no tpc); L4 (`chordanalyzer.cpp`) **already interprets it inline**, heavily — the `tpcForPc` map,
`tpcSpellsAsSharp` / `tpc8SpellsAsFlat` sense booleans, and the `tpcConsistencyBonus` / `countTpcMatches` / `tpcDeltas`
consistency scorer (≈55 sites). So the "one shared interpreter, never duplicated" rule has a single concrete target:
**the L4 spelling-pin build must fold those inline reads into the primitive — not add a second interpreter beside
them.** That fold also **corrects** the inline `>= 0` guards noted in §1 (they currently mis-reject flat-side
spellings). This is a forward note for the L4 build, **not** Phase-4 work.

## 4. Byte-identity (the gate)
- **BIR-flat on both presets — trivially:** the primitive has **no production consumer** in Phase 4 (L4 unbuilt, the
  L3 term deferred to Phase B). Nothing on the live path calls it, so the corpus, both suites, and snapshots are
  **byte-identical** by construction. Any movement → STOP (something wired the primitive into production early).
- The primitive is **unit-tested as a pure function** (tpc → line-of-fifths / sharp-flat; aggregate over a span),
  independent of any consumer — that is the only new test surface in Phase 4.

## 5. Unification (the explicit reason this is one primitive)
The discarded foundation WIP carried a tpc reading **per-layer / decode-only** (the backed-out `--seq-tpc-weight`
diagnostic, Stage-0). Phase 4 builds the spelling interpretation **once**, as a production primitive both layers call —
*not* the per-layer version. Reference the discarded WIP (in stash `bc4fa79…`) **only** for the term's measured shape;
do **not** re-land its code. End with the reuse-vs-new ledger.

**Latent L1 caveat (recorded, NOT fixed in Phase 4 — it is an Architectural Layer 1 matter).** `NoteEvent.tpc` uses
`−1` as its "not provided" default, but `−1` is also the legitimate spelling **Fbb** (`TPC_F_BB`), and the field's
`0–34` comment is wrong on **both** ends (the real range is `−8 … 40`, `TPC_MIN … TPC_MAX`). So the L1 representation
**cannot distinguish a real Fbb from "absent."** This is **latent, not active**, and the guarantee is the **build-path
invariant**, not a corpus count: every `NoteEvent` on the build path is assigned `e.tpc = n->tpc()` from a real DOM
note, so the `−1` default never survives to a consumer. *(The corpus also appears to contain no Fbb — but that figure
is **carried-forward, not re-verified read-only**; a per-note count needs a build+run, and the design does not depend
on it: a real Fbb stored as `−1` is still interpreted correctly as Fbb. Only a never-assigned default `−1` would be
wrong, and that does not occur on the build path.)* The clean L1 fix is **already in hand**: `TPC_INVALID = −9` exists
and `tpcIsValid(−9)` is false, so the L1-pass change is simply **default `NoteEvent.tpc = TPC_INVALID` instead of `−1`
and correct the `−8 … 40` comment** — not "introduce a new sentinel." It is an **L1 change**: record it for the L1
as-built/cleanup pass, do **not** fold it into Phase 4 (no cross-layer creep).

## 6. What CC verifies read-only BEFORE building (ground it — do not assume)
- **`NoteEvent.tpc` is populated on the real path** — the make-or-break premise. Confirm it is **not `-1`** on
  engraved/imported corpus scores (the importer must set it). If the spelling is absent, the primitive has no input
  and Phase 4 stops — so this is checked **first**, against actual scores, not assumed from the field's existence.
- **Where the primitive should live** (the `engravingbridge` derived-view seam beside `weightedPcView`/`soundingAt`)
  and that **no existing spelling-derived view** already does this — extend it rather than add a second.
- **The prior measurement** (`cc_layer3_tpc_keymeasure_report.md`) for the line-of-fifths / sharp-flat **interpretation
  shape** the primitive must reproduce (so the primitive matches the signal already measured to be genuine).
- *(`keymodeanalyzer` scorer seam is NOT in scope — the L3 term is Phase B, §2.)*
- Report; surface any seam that differs before building.

## 7. Tests & delivery
- **Primitive unit tests (the only new test surface):** `G♯`≠`A♭` line-of-fifths distinction; sharp/flat-side sense;
  the span aggregate (centroid / sharp-flat distribution) over a small fixture.
- **Byte-identity:** corpus + both suites + snapshots unchanged — trivial, since nothing in production consumes the
  primitive yet (the gate; any movement → STOP).
- **Phase 4 (the shared primitive alone)** is the buildable unit; a short read-only verification (§6) precedes the
  build, as in Phases 1–3. The L4 spelling-pin that consumes it is the **next** build (with L4), not Phase 4.
