# Phase 4 (tpc spelling capability) — read-only verification BEFORE building

**READ-ONLY. No production code written, no behaviour changed, no commit, `upstream` untouched.**
Grounds `cowork_tpc_capability_design.md` (option B — build the **shared spelling primitive only**; the
Architectural Layer 3 key-spelling *term* + weight are Phase B; the per-note shape is consumed next by
Architectural Layer 4's spelling-pin) at source before any build is written. Findings only.

Method: source inspection of the L1 note model, the importer/loader path, the `engravingbridge` derived-view
seam, and a full tpc-usage sweep of `src/composing/analysis/**`; plus a corpus-wide on-disk `<tpc>` population
count over the engraved Bach corpus. HEAD `5b30f855a0`, working tree clean.

---

## §1 — Make-or-break premise: is `NoteEvent.tpc` actually populated on real scores? **YES — 100%.**

### Where `tpc` is set (assignment + source field)

- **Layer-1 note-model build (the field the primitive reads):**
  [`note_model.cpp:53`](src/composing/analysis/notemodel/note_model.cpp#L53) —
  `e.tpc = n->tpc();` in `makeEvent()`. The source field is the engraving DOM **`Note::tpc()`** (the displayed /
  concert tonal pitch class, line-of-fifths spelling). `NoteEvent.tpc` is declared
  [`note_model.h:82`](src/composing/analysis/notemodel/note_model.h#L82): `int tpc = -1; ///< TPC (0-34 …). -1 = not provided.`
- **Upstream — where `Note::tpc` itself comes from:**
  - *MusicXML import path:* [`importmusicxmlpass2.cpp:308-310`](src/importexport/musicxml/internal/import/importmusicxmlpass2.cpp#L308)
    `xmlSetPitch()`: `tpc2 = step2tpc(step, AccidentalVal(alter)); tpc1 = transposeTpc(tpc2, intval); n->setPitch(pitch, tpc1, tpc2);`
    — i.e. the DOM tpc is derived from the **notated `<step>` + `<alter>`** (the score's spelling), not from MIDI pitch.
  - *`.mscx` load path (what the gate corpus actually uses):* the modern MS3 reader
    [`read400/tread.cpp:3075-3078`](src/engraving/rw/read400/tread.cpp#L3075) reads the `<tpc>` element **verbatim**
    into `n->setTpc1(tcp); setTpc2(tcp)` (with `<tpc2>` overriding tpc2 if present, 3088-3089). **No recomputation.**
    → for the corpus, runtime `Note::tpc()` == the on-disk `<tpc>` value, so an on-disk count is a faithful proxy
    for the runtime field the primitive will read.

### The gating fact — measured on real scores (not assumed from the field's existence)

Corpus: `tools/dcml/bach_chorales/MS3/*.mscx` — the engraved Bach corpus the BIR gate and the prior tpc decode both
run on (353 gate stems; the count below spans all **361** `.mscx` in the dir, fully covering them). Counted `<Note>`
elements vs `<tpc>` elements vs in-range/out-of-range tpc values:

| metric | count |
|---|---|
| files | 361 |
| `<Note>` elements | 84,395 |
| `<tpc>` elements | 84,395 |
| tpc in line-of-fifths range **[0, 34]** (populated) | **84,395 (100.00%)** |
| tpc at the `-1` "not provided" sentinel / negative / out of range | **0** |

**Every note carries a valid line-of-fifths spelling; zero are absent.** The primitive's input is fully present on
the real path. This is independently corroborated at **runtime** by the prior decode-only measurement
(`cc_layer3_tpc_keymeasure_report.md`), which threaded the live `NoteEvent.tpc` into a tpc-aware key emission and
obtained a genuine, monotone, theory-predicted line-of-fifths signal — impossible if the field were `-1`-dominated;
its §5 states the engraved corpus spelling is trustworthy and is the **upper bound** of the tpc benefit.

> Reliability scope (carry forward, not a Phase-4 blocker): this 100% holds because the corpus is **engraved**
> (spelling authored). A raw-MIDI import would default enharmonics via `pitch2tpc` and the line-of-fifths fit would
> be noisier — so any *deployment weighting* of the spelling signal must be conditional on spelling provenance.
> That is a Phase-B (L3 term) / L4-pin concern; the **capability's input is present** for Phase 4.

**§1 verdict: PRESENT (100% populated). The §6 stop-condition "tpc largely `-1`" does NOT trigger.**

---

## §2 — Where the primitive should live, and whether one already exists

### The seam the design names is correct — confirmed at source

The L1-derived views live in **`mu::composing::analysis::engravingbridge`**
([`regiontonecollector.h`](src/composing/analysis/engravingbridge/regiontonecollector.h) /
[`regiontoneprimitives.cpp`](src/composing/analysis/engravingbridge/regiontoneprimitives.cpp)): `soundingAt`
(point-in-time per-note), `weightedPcView` (region pc-aggregate), `pitchContextOverSpan` / `collectPitchContext`
(windowed key/mode context). The module's header contract: *"derive VIEWS over this model … never on
notation/internal"*; it depends only on engraving + the composing analysis types. This is exactly the design's
"spelling-derived view living **beside** L1, **not** inside an analysis layer." **The seam is right.**

These views already **carry** tpc but do **not interpret** it: `SoundingNote{ int ppitch; int tpc; }`
([`regiontonecollector.h:108`](src/composing/analysis/engravingbridge/regiontonecollector.h#L108)),
`soundingAt` emits `{ ne->pitch, ne->tpc }`, `buildTones` copies `t.tpc = sn.tpc` into `ChordAnalysisTone.tpc`,
and `weightedPcView` propagates `a.tpc = ne->tpc`. So a **new line-of-fifths / sharp-flat interpretation view**
placed here is genuinely new at this seam — not a second copy of an existing bridge view.

### Existing spelling/line-of-fifths interpretation — IT EXISTS, but inline inside Architectural Layer 4 (the one seam difference to surface)

The §2 search ("if one exists, extend it, don't add a second") turns up **no shared, reusable spelling-interpretation
primitive** anywhere — but it does turn up **existing tpc *interpretation* logic, scattered and inlined inside the
chord analyzer (Layer 4)** and in the symbol formatter (display). Concretely:

- **Layer-4 line-of-fifths interval model + consistency scorer** — [`chordanalyzer.cpp`](src/composing/analysis/chord/chordanalyzer.cpp):
  - `TemplateDef::tpcDeltas` (335-344): *"expected TPC (circle-of-fifths) deltas per interval: P5=+1, M3=+4, m3=−3, P4=−1, A5=+8, d5=−6, m7=−2, M2=+2, A4=+6."* The line-of-fifths interval encoding already exists.
  - `countTpcMatches` (497-516): `actualTpc == rootTpc + tpl.tpcDeltas[i]` — checks each note's spelling against the expected line-of-fifths offset from the root.
  - `tpcConsistencyBonus` (648-653) + `nonBassAdjustment` (532-554): reward/waive on root-relative spelling consistency. The bonus weight `tpcConsistencyBonusPerTone = 0.20` ([`chordanalyzer.h:367`](src/composing/analysis/chord/chordanalyzer.h#L367)).
  - **Per-note sharp-side / flat-side sense, inlined** (288-320): `tpcSpellsAsSharp = (tpc6 - rootTpc > 0)`, `tpc8SpellsAsFlat = (tpc8 - rootTpc < 0)`, `isSharp13Spelling = (tpc10 - rootTpc == 10)` — this is **the exact "sharp/flat sense" read-shape the design lists for the L4 spelling-pin**, already computed (relative to the chord root) for extension spelling.
  - `tpcForPc` (1131-1140): a per-call `array<int,12>` pc→tpc map, the closest existing structure to "per-note spelling, indexed." Rebuilt inside every `analyzeChord` call; carried in the scoring snapshot (`chordanalyzer.h:901`, `harmonicfunctionlayer.h:239`) and read by `chordslicedecoder.cpp:275` for root naming.
- **Display-side spelling** — [`chordsymbolformatter.cpp`](src/composing/analysis/chord/chordsymbolformatter.cpp) `csfPitchClassNameFromTpc()` (85+): enharmonic chord-symbol naming from tpc + key fifths. A tpc consumer, for **output naming**, not analysis.
- **The line-of-fifths *window* already exists as a pc projection** — [`analysisutils.h:96-107`](src/composing/analysis/chord/analysisutils.h#L96) `diatonicMaskFromFifths()`: *"signature fifths selects the seven consecutive circle-of-fifths positions **[fifths−1, fifths+5]**"* — the **same window** the prior report's `tpcKeyFitForSignature` used, here as a 12-bit pc mask.
- **Layer 3 interprets tpc not at all** — the committed `KeyModeAnalyzer::PitchContext`
  ([`keymodeanalyzer.h:498-503`](src/composing/analysis/key/keymodeanalyzer.h#L498)) carries `{pitch, durationWeight,
  beatWeight, isBass}` — **no `tpc`**. (The `int tpc` add + `tpcKeyFitForSignature` from the prior report are the
  uncommitted decode-only edits; the stash `bc4fa79` "foundation WIP" is reachable, reference-only per design §5.)
  Layer 3 is spelling-blind today, exactly as the prior measurement stated.

**Seam-difference to surface before building (this is the §6 "report any seam that differs"):** the design's
unification claim — *"both L3 and L4 read [spelling] through a single place, never duplicated per layer"* (§1) — meets
an as-built reality where **L4 already interprets tpc inline** (root-relative sharp/flat sense, line-of-fifths-delta
consistency, the pc→tpc map) and **L3 does not interpret it at all**. So the unification work is real and
**concentrated at L4**: when the L4 spelling-pin is built (the next build) to consume the new primitive, it should
**fold these inline L4 reads into the primitive** (or the primitive be shaped to subsume them), otherwise the
primitive becomes a *second* spelling interpreter beside the chord analyzer's existing one — the precise outcome §5
warns against. **This does not block Phase 4** (the primitive at the `engravingbridge` seam is new and correct); it is
a design-coupling note so the design's "never duplicated" guarantee is honoured at the L4-pin step, not silently
violated.

---

## §3 — The interpretation shape to reproduce (from `cc_layer3_tpc_keymeasure_report.md`)

The prior decode-only measurement established the **genuine** spelling signal and its exact shape (its §1):

- **TPC → line-of-fifths position:** TPC is a *direct line-of-fifths index*. `Tpc::TPC_C = 14`; **each +1 tpc = +1
  fifth** (confirmed at source: [`pitchspelling.h:40-53`](src/engraving/dom/pitchspelling.h#L40) — the enum runs
  …F♭(6) C♭(7) … F(13) **C(14)** G(15) … and `TPC_DELTA_SEMITONE = 7`). So line-of-fifths position = `tpc − TPC_C`
  (C=0, G=+1, F=−1, F♯=+6, …). `G♯` (tpc 22) and `A♭` (tpc 11) are thereby distinguished — the per-note distinction
  the design's L4 symmetric-root pin needs.
- **Sharp-side / flat-side sense:** the sign of the line-of-fifths offset from a reference — positive = sharp side,
  negative = flat side. (Matches the inline L4 pattern `tpc − rootTpc > 0 ⇒ sharp`, §2.)
- **Diatonic window of a key:** a signature `sf` (Ionian-convention fifths) has its 7 diatonic notes on the contiguous
  line-of-fifths window **[sf−1, sf+5]** (identical to `diatonicMaskFromFifths`, §2). The per-note key-fit penalty in
  the prior term = the note's line-of-fifths **distance from the nearest window edge** (0 inside the window).
- **Span aggregate (the L3 modulation-direction shape):** over a window, the spellings' weighted line-of-fifths
  distribution — concretely, in the prior term, `−Σ wᵢ · lofDistanceOutsideWindowᵢ`, with the **same note weight the
  emission uses** (`min(dur·beat, cap) · (bass ? mult : 1)`), so the term sits on the emission's scale. The design
  generalizes this to a **line-of-fifths centroid / sharp-flat distribution**: sharp-side mass ⇒ dominant direction,
  flat-side ⇒ subdominant. Measured property to preserve: the signal is real at **modulations**, monotone, and beats a
  switch-rate control; it is **blind to same-signature ambiguity** (relative major/minor, modal rotations) by
  construction (the window depends only on the signature). The primitive reproduces this aggregate so the Phase-B L3
  term reweights a signal already proven genuine, not a re-invented one.

The discarded WIP's term (`keymodesequence.cpp::tpcKeyFitForSignature`, stash `bc4fa79`) is **reference only** for this
shape — do not re-land its per-layer / decode-only code (design §5).

---

## §4 — Out of scope (honoured)

- **Did NOT** investigate or touch the `keymodeanalyzer` scorer seam — the L3 spelling term is **Phase B** (design §2).
  (Confirmed only that committed `PitchContext` carries no tpc, to ground the "L3 is spelling-blind today" fact.)
- **Did NOT** write the primitive, wire any consumer, or modify any production file. Read-only throughout; no commit;
  `upstream` untouched.

---

## §5 — Reuse-vs-new ledger (so the build rests on facts, not assumptions)

| concern | reuse (exists) | new (Phase 4) |
|---|---|---|
| tpc → line-of-fifths position | `Tpc::TPC_C` (=14), `TPC_DELTA_SEMITONE` (=7) — `pos = tpc − TPC_C` | the shared per-note accessor on the new view |
| sharp/flat sense | engraving `tpc2alter(tpc)` ([`pitchspelling.h:117`](src/engraving/dom/pitchspelling.h#L117)) → `AccidentalVal`; inline L4 pattern `tpc−ref` sign | the shared, reference-agnostic sense on the view |
| validity / "absent" test | engraving **`tpcIsValid(int)`** ([`pitchspelling.h:128`](src/engraving/dom/pitchspelling.h#L128)) | use it — **do NOT** reuse the composing `tpc >= 0` / `== -1` convention (see caveat) |
| diatonic line-of-fifths window `[sf−1, sf+5]` | `analysisutils.h::diatonicMaskFromFifths` (pc projection) | the lof-form window + distance-outside, for the span aggregate |
| tpc carried per note into views | `SoundingNote.tpc`, `ChordAnalysisTone.tpc`, `weightedPcView`, `soundingAt` | the **interpretation** layered over them (none today) |
| line-of-fifths conversions | engraving `tpc2pitch / tpc2step / tpc2alter / step2tpc` (`pitchspelling.h`) | — (reuse; do not re-derive) |
| existing L4 inline interpretation | `tpcDeltas`, `countTpcMatches`, `tpcConsistencyBonus`, inline sharp/flat booleans, `tpcForPc` | the L4-pin (next build) should **fold these into** the primitive — see §2 seam note |

**Sentinel/range caveat for the primitive (grounded, not a Phase-4 blocker):** the canonical engraving TPC range is
`TPC_MIN = TPC_F_BBB (−8) … TPC_MAX = TPC_B_SSS (40)` with `TPC_INVALID = −9`; the composing "0-34" comment is a
*narrower practical subset*. Critically, `TPC_F_BB = −1` is a **legitimate** spelling (F𝄫), yet the composing
`NoteEvent` uses `−1` as its "not provided" sentinel, and the chord analyzer gates spelling reads on `tpc >= 0`. On
this corpus the collision never bites (0 negative tpc values measured), but the **new primitive must test absence with
`tpcIsValid()`**, not `>= 0` / `== -1`, to be correct for the full notated range.

---

## §6 — Verdict

**Primitive build is GROUNDED.** The make-or-break premise holds — `NoteEvent.tpc` is **100% populated (84,395/84,395,
0 at the `-1` sentinel)** on the real engraved corpus, sourced from the notated spelling via `step2tpc` (MusicXML) /
verbatim `<tpc>` (`.mscx`) and read by the L1 note model. The `engravingbridge` seam the design names is the correct
home and carries no existing spelling-*interpretation* view there. **One seam difference to weigh before the L4-pin
build (not a Phase-4 blocker):** Architectural Layer 4 **already interprets tpc inline** (root-relative sharp/flat
sense, line-of-fifths-delta consistency, the `tpcForPc` map); the primitive should be shaped so the next-build L4
spelling-pin folds those inline reads into it, honouring the design's "never duplicated per layer" unification rather
than adding a second interpreter. No stop-condition triggered.
