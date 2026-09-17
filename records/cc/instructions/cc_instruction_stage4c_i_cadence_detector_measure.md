# CC Instruction: Stage 4c-i — build the key-agnostic cadence detector + MEASURE realized detection (no wiring)

## Authorization + framing

Implements **ratified** `docs/stage4c_cadence_key_design.md` §4 (4c-i). The cadence→key investigation
green-lit this (`cc_cadence_key_investigation_dossier.md`: floor is 91% relative-pair, cadence is a
decoupled note-derived global anchor) **but** the "91% / ~1259" is a **perfect-detection ceiling**. **This
run measures the REALIZED detection fraction BEFORE any production wiring** — the reality check on the
ceiling. **Do NOT wire the detector into key scoring this run** (that is 4c-ii). The detector is *built and
measured*; the production resolver/winner is **untouched** → byte-identical gate + snapshots.

Zone: composing autonomous zone (`src/composing/`) + `tools/` (measurement). No `src/notation`/`src/engraving`
production edit. HELD — no commit. Never-guess: read the region/chord structs at source; tag every claim
`[probe]` (measured) / `[code]` (read at source) / `[oracle]` (DCML/music21).

## Build — the key-agnostic authentic-cadence detector (§2 of the design)

A new composing function (place sensibly — e.g. alongside the section analyzer; **do NOT reuse the broken
`detectCadences`**). It operates ONLY on per-region `chordResult.identity` (absolute root pc + quality) +
region pitch content. **It MUST NOT read `function.degree` or the resolved key** (that circularity is
exactly why the existing detector is unusable — confirm the inputs are key-agnostic at source).

**Authentic cadence only (per ratified §6.1).** For consecutive regions a→b:
- `root(a)` is a descending perfect fifth to `root(b)` (`root_b ≡ (root_a − 7) mod 12` — a is the dominant of b);
- `a` is major/dominant quality (carries the leading tone = major third of a, a semitone below `root(b)`);
- `b` is a stable triad.
⇒ `root(b)` is a **cadential tonic**; `b`'s quality (major/minor) is the **mode**. (Verify the leading-tone
is actually present in a's pitch content, not just implied by quality — read what `chordResult` exposes.)

**Aggregate → anchor:** collect cadences per section; the **final / strongest** cadence is the global
anchor (a piece resolves to its tonic). Output per section + a piece-level **(tonicPc, mode, confidence)**.
KeyArea (already in composing) is the natural carrier — but for 4c-i it only needs to be *computable +
inspectable*, not yet fed into resolution.

## Measure — the realized-detection fraction (read-only; the deliverable)

A read-only diagnostic (tool, or a byte-identity-gated dump) that, after the normal analysis runs, invokes
the new detector on the analyzed regions and compares its anchor to the DCML global key. Reuse the
investigation's `tools/cc_floor_classify.py` to identify the **relative-pair floor population** (~1259
Default regions). Report:

1. **Realized fraction `[probe][oracle]`:** of the relative-pair floor regions, how many does the detector
   anchor **correctly** (anchor tonicPc+mode == DCML global)? Give **precision** (when it fires, right?)
   and **recall** (does it fire at all on these cases — many may have no detectable authentic cadence in
   their span). This is the headline number vs the 91% ceiling.
2. **Per-target `[oracle]`:** bwv365, bwv33.6 (already recovered in 4b-i — does the detector also anchor
   them correctly?), **bwv64.2** (resolve the G-vs-C-major GT discrepancy from the 4b-ii/investigation
   conflict — what does WiR/DCML actually say, and does the detector anchor it?), bwv83.5 (the "other"
   residual — detector should NOT spuriously claim it).
3. **Decoupling preview `[probe]`:** on the cases the 1.0 hint already gets right mode-present, does the
   detector's anchor **agree** (a positive sign for 4c-ii's decoupling) or contradict (a warning)?
4. **Coverage gaps `[probe]`:** characterize the relative-pair floor regions the detector does NOT cover
   (no authentic cadence in span) — these size what plagal/half/deceptive (4c-iii) or richer detection
   would need to add.

## Byte-identity requirement (the 4c-i gate)

The production scoring path is **untouched** — the detector is called ONLY by the diagnostic, never by the
resolver/winner. Prove it:
- BIR gate **57 / 57 / 23 byte-identical** all three presets (identity sets unchanged);
- `pipeline_snapshot_tests` **11/11, zero golden diffs** (no refresh);
- composing/notation suites green.
If any of these move, the detector has leaked into production — STOP and report (4c-i must be a pure
measurement).

## Held / report — `cc_stage4c_i_report.md`
The detector at source (key-agnostic inputs confirmed), the **realized-detection fraction** (precision/
recall vs the 91% ceiling), the per-target + bwv64.2 GT resolution, the decoupling preview, the coverage
gaps, and the byte-identity proof. **Branch recommendation:** realized fraction is worthwhile ⇒ proceed to
4c-ii (wire at section/piece scope); marginal ⇒ 4c-iii richer detection first; far below ceiling ⇒ the
detection-reliability / key-axis A-vs-B finding (report, do not wire). Every number `[probe]`, every root
`[oracle]`. HELD — no commit.

## Stop conditions
- The detector needing `function.degree` or the resolved key (it must be key-agnostic) — if it can't be
  made so, that is a finding; report it.
- Any production behavior change (gate/snapshot/suite movement) — the detector leaked into scoring; STOP.
- Realized detection far below the 91% ceiling — report as the detection-reliability / A-vs-B finding; do
  NOT proceed to wire a weak detector (4c-ii is gated on this number).
- Temptation to wire the anchor into the winner "to see if it helps" — that is 4c-ii, separately ratified; do not.
