# Delta-check (L1–L4) — Cowork verification, proper-layer dispositions, and the L4 build backlog

> CC ran the read-only spec↔implementation delta-check (`cc_spec_impl_delta_L1L4_report.md`). This records what Cowork
> **verified at source**, the **proper-layer disposition** of each finding (per the standing rule: amendments go in
> the right architectural layer), and the resulting **L4 build backlog**. CC's report is held/gitignored and
> CC-authored; the dispositions below rest on Cowork's own source reads, not CC's word.

## Verified at source (Cowork)
- **D1, D2 (L4 membership) — confirmed.** Read `chordslicedecoder.cpp:386–406` directly: an extra note is a non-chord
  tone on `weak OR stepwise` (line 401); basic-template tones bypass the rule entirely (390–393); the penalty charges
  *structural extras outside the template* (405). Both diverge from the spec as CC said.
- **H1 — confirmed.** `cofDistance` (`keymodesequence.cpp:65–73`) is circle-of-fifths / key-signature distance,
  cyclic (`C→F♯` = `C→G♭` = 6). Not semitone, not scale-tone count.
- **H4 — confirmed, and broader than CC framed it.** Grep of `src/composing/analysis` for any reach-back/widen code
  is **empty** at *both* layers. L1's own "widen the span" operation is unbuilt too — so CC's "L1 fully clean" missed
  this; the note model loads the whole score (L1 §11), so reach-back is *unnecessary for now*, not merely unwritten.

## Dispositions (each in its proper layer)

### L4 — chord (the decoder is isolated under the decode diagnostic, NOT in production; nothing below affects shipped output)
- **D1 — membership cue-combination.** The **spec is the correct reference**, not the code. Music-theoretically the
  code's `weak OR stepwise → NCT` is wrong in two quadrants: it marks a *weak leap* (an arpeggiated extension) a
  non-chord tone, and it marks *every* strong-stepwise note a non-chord tone rather than only the accented passing
  tone over a clear prevailing chord. The spec's `weak AND stepwise` rule plus its two hard cases is the right
  behaviour. → **L4 code backlog; no spec change.**
- **D2 — implausibility penalty.** Again the **spec is the correct reference**. The spec's "implausible chord tone =
  a *template* tone the membership rule would call a non-chord tone" is the penalty that discriminates `C` from
  `Cadd9` and triad from seventh (it penalises a candidate whose own chord tones behave like embellishments). The
  code penalises the opposite (extras *outside* the template) and lets template tones bypass — so it cannot make that
  discrimination at all. → **L4 code backlog; no spec change.**
- These two are DIVERGENCEs (built-and-wrong, not merely unbuilt), but because the decoder is isolated they are *top
  of the build backlog*, not a production incident.

**L4 build backlog (sequence for the next, gated increment — bring the decoder to the rewritten spec):**
1. **Sufficiency / inherit / abstain** — the phantom-root rule (spec §4.3, §5.4): a thin slice inherits the prevailing
   chord or abstains; never a new symbol from too few notes. (`chordslicedecoder.cpp:296–319` currently commits.)
2. **Uncertainty = insufficiency OR low margin, and confidence composite** (spec §7): add the insufficiency trigger
   and the sufficiency + membership-cleanliness terms; today it is margin-only (`:309–319`).
3. **Membership fix (D1) — the sharpened three-tier rule (spec §5.3, tightened 2026-06-24).** Drop the blanket
   `weak ||`; the existing `isStepwiseTreated` already computes tier 1 (passing/neighbour both-sides + suspension) and
   is reused as-is. Non-chord-tone ⟺ tier 1 (stepwise-embellishing, regardless of weight) **or** tier 3 one-sided +
   weak/foreign-to-prevailing; no-stepwise (leap both sides) → chord tone regardless of weight. Metric weight enters
   only at tier 3.
4. **Implausibility fix (D2) — same test on required tones (spec §5.3).** Stop letting template tones bypass; run each
   required chord tone through the *same* three-tier behaviour test, and charge the implausibility penalty when a
   required tone behaves as a tier-1 embellishment. (This is the `C` vs `Cadd9` / triad-vs-spurious-seventh
   discriminator; the current penalty-on-extras is removed.)
5. **About-what payload on "uncertain"** (spec §7): carry root / quality / which note, not a bare yes/no.
6. **Window stop on chord-consistency**, not pc-count (spec §2).
7. **Evidence precedence ladder** (spec §5): spelling-pin > note fit > key/prevailing tie-break.
8. **Catalogue = basic types only + spelling-pin**: give the diminished-seventh and minor-major their own four-note
   types and pin the symmetric root from notated spelling; retire the replaced "diminished triad + flag" model
   (`chordanalyzer.cpp:232,246`). Added notes come from membership (spec §1, §9).
- **Unification (standing rule), to fold into the same increment / the wiring:** the parallel `SliceKeyMode` /
  `SliceChord` records, the duplicated `verticalScore`, and the eligibility predicate copied ≥4 sites — unify, do not
  carry forward. The decoder header banner is stale (says "Increment A / membership stubbed" while the `.cpp` is
  Increment B) — correct it at build.

### L3 — key/mode (amendments made now, knowledge-based, in the L3 spec)
- **H1 / H2 / H3 — predicates qualified** from the verified code: change cost sized by circle-of-fifths
  (key-signature) distance; on the **same scale** as the local-fit score; and brief-vs-sustained is **pure
  fit-vs-cost arithmetic with no slice-count threshold**. (Edited §4 + the glossary.)
- **H4 — reach-back marked designed-but-unbuilt** in the L3 spec (and in L1 §3 — see below), with the reason (the
  note model loads the whole score, so it is unnecessary for now; deferred with the selection-based working model).
- **Benign SPEC-GAPs (record, low priority):** a second emission-scale confidence on `normalizedConfidence` feeds the
  0.8 gates (worth a one-line note in the L3 data-design when next touched); the off-by-default `tpcKeyFitWeight`
  measurement term is already the deferred tpc retrofit (spec §15) — no action.

### L1 — note model (thoroughly re-verified by Cowork; CC's light pass had missed the widen gap)
- **Cowork verified the public API directly** (`note_model.h`): `build`, `notes()` (all-notes, fixed order),
  `overlapping` (sounding-during A–B), `onsetIn` (starting-within A–B) are all built — **4 of the 5 spec operations.
  Only `widen` is absent.** The eleven facts, tie-resolution, lossless keep-and-mark, no backward limit, and index ≡
  linear are MATCH (CC + tests). So the **single** L1 gap is widen.
- **Widen / reach-back — a REAL product requirement, currently unbuilt and currently masked (corrected
  2026-06-24).** The shipped product is **selection-based**: it analyses the user's selected range, never the whole
  score (the whole-score path is only the offline batch-testing harness). A selection is a temporal **subset**, so L3
  genuinely needs to **reach back before the selection's start** to read the established key at the leading edge
  (analyse measures 20–40 and the key at m.20 needs the context before m.20). So widen is **needed by design**, not
  speculative. It is currently **unbuilt**, and currently **masked** only because L1 still loads the whole score (the
  §11 inefficiency) — so the pre-selection context happens to be in memory and reach-back is not yet exercised. When
  L1 is fixed to load only the selection (the §11 efficiency fix / selection-based working model), **reach-back must
  land with it**, or selection-edge key inference breaks. *(Earlier "moot / already maximally wide" framing was wrong —
  it described the current whole-score-load stopgap, not the design.)*
- **But it does NOT gate the L4 build.** Chord is purely local (a slice ± 1–3 neighbour slices, §window) and never
  needs context outside the selection. So reach-back is deferred **with the selection-based-loading track (L1 + L3
  together)**, not before L4. The L1 spec §3 / L3 §2 now mark widen designed-but-unbuilt; that documentation is
  correct. The open *product* decision (whenever selection-based loading is scoped) is L1+L3, not L4.

### L2 — slicing (Cowork-verified)
- CLEAN, accepted. Verified `changePointSlices` + the `Slice` `[start,end)` with note-set identity directly; both-edge
  boundaries, complete coverage incl. empty slices, zero-interpretation, `--validate-slices` corpus check. Single
  operation, fully built. No action.

## Net
No production output is affected by any finding (L4 decoder isolated; L1/L2/L3 amendments are documentation precision).
The L3/L1 spec amendments are done. The L4 backlog above is the specification for the next gated build increment —
bringing the chord decoder to the rewritten spec, the divergences first.
