# CC report — the notation consumption-surface audit (READ-ONLY)

**Dispatch:** `cc_instruction_notation_consumption_audit.md` (Cowork, 2026-07-26) — the §8.1
read-only step of the ratified `cowork_notation_adoption_increment.md`.
**Nature:** READ-ONLY on code. No `src/` edit, no build, no test, no golden, no corpus,
no `tools/robust_stop/`. Two commits only: Task 0 (the ratification record) and the audit
artifacts.
**Every figure below is drawn from the generated artifact** `tools/audit/notation_surface/`
(`gen_notation_surface_audit.py` → `consumption_fields.csv` + `summary.json`); nothing is
hand-counted (#17f).

**Purpose (the #12 exhaustiveness for Decision A2):** for every fact the live notation path
consumes from the legacy analysis surface, EITHER name a declared source on A's surface (the
`DecodeResult`/`SegmentSummary` fields + the ratified planned publications: the full posterior
OI-193, the un-rounded modal reading C1, the ornament labels OI-194, the derived chord facts),
OR flag it for a declared retirement-with-rationale — so the Decision-A2 switch drops nothing
silently. **Dispositions here are PROPOSALS** (input to the Cowork/user rulings), never
decisions.

---

## Task 0 — the ratification commit (done, first)

- **Commit `00c0df81c5`** (pushed origin only; `upstream` push confirmed disabled).
- Files (exactly five; nothing else staged): `CLAUDE.md` (the decision-neutrality corollary
  inserted after the fact-publication corollary + the provenance-sentence extension),
  `STATUS.md` (the new 2026-07-26 third entry), `OPEN_ITEMS.md` (Cowork's OI-193/OI-194 rows),
  `cowork_handoff.md` (Cowork's ratification addendum), `cowork_notation_adoption_increment.md`
  (the ratified decision surface, new file).
- **HEAD was `205dd0843a`** as expected; the only tracked working-tree diffs before Task 0 were
  the three Cowork-authored edits, and the untracked `??` set matched the session-start
  snapshot — no unexpected diff, no STOP.
- **Anomaly (harmless):** the dispatch's Task 0.3 prose says "all six files" but explicitly
  enumerates exactly **five** (and the header likewise says "FIVE … edits that ride Task 0"
  naming the same five). The working tree confirmed exactly those five changed and no sixth
  exists (`ARCHITECTURE.md` et al. unmodified). Committed the five named files; "six" is a
  wording slip, not a code-vs-ruling contradiction.

---

## The scope check FIRST (the OI-175 lesson: a scoped sweep proves the scope, not the question)

The audit was scoped by a **tree-wide** sweep of `src/`, not by the decision-doc's named list.
The sweep keyed on: every caller of `analyzeHarmonicRhythm` (the region entry); every
`HarmonicRegion` / `AnalyzedRegion` / `KeyArea` / `AnalyzedSection` reference; every
`analyzeSection` consumer; and — the catch — every caller of the single-note entry
`analyzeNoteHarmonicContext` / `analyzeNoteHarmonicContextDetails`.

**Expected roster (decision-doc §1):** `notationcomposingbridge`, `notationimplodebridge`,
`notationtuningbridge`, `sectionanalyzer` + downstream function-labeling, accessibility.

**Found roster (the sweep decided it):**

| consumer | live? | what it consumes |
|---|---|---|
| `notationharmonicrhythmbridge.cpp` | seam/producer | reads config + plumbs 21 mode priors; returns the `HarmonicRegion` vector (no region field read) |
| `notationcomposingbridge.cpp` (+`helpers.cpp`) | live | single-note context + region-emit annotations + status-bar string |
| `notationimplodebridge.cpp` | live | chord-track implode: key runs, voicing, chord-symbol/roman/nashville, OI-182 constants, cadence |
| `notationtuningbridge.cpp` | live | region + single-note intonation (tuning offsets) |
| `sectionanalyzer.cpp` | live | `HarmonicRegion`→`AnalyzedRegion` translation + key stabilization + gap-fill + key-area grouping |
| `sectioncadencedetection.cpp` | live | `detectCadences` / `detectPivotChords` (cadence + pivot staff-text) |
| **`notationinteraction.cpp`** | live — **OUT OF EXPECTED ROSTER** | `analyzeNoteHarmonicContext` → writes Harmony elements (chord symbol / RN / Nashville) to the score (`:8311`) |
| **`notationscene/…/notationcontextmenumodel.cpp`** | live — **OUT OF EXPECTED ROSTER** | `analyzeNoteHarmonicContextDetails` → the right-click "add chord symbol / roman / nashville / tune-as" menu (`:194`) |
| `notationaccessibility.cpp` | live — **STRING only** | reads NO struct field; consumes only the pre-formatted `harmonicAnnotation(Note*)` string (`:204/:206`) |

**Three sweep results the named roster would have missed (the sweep working):**

1. **A SECOND entry point beyond `analyzeHarmonicRhythm`.** The decision-doc §1 says the in-app
   analysis "enters through ONE function." The sweep shows a second surface: the single-note
   `analyzeNoteHarmonicContext` / `analyzeNoteHarmonicContextDetails`, returning
   `vector<ChordAnalysisResult>` / `NoteHarmonicContext`. It is consumed by the tuning bridge,
   the status-bar/accessibility path, **and two consumers outside the expected roster**
   (`notationinteraction.cpp`, `notationcontextmenumodel.cpp`). Under A2, `ChordAnalysisResult`
   and `NoteHarmonicContext` retire with the legacy path, so this entry and its consumers must
   also read A's record — **in scope; flagged**. (Not a STOP; the dispatch classes an
   out-of-roster live consumer as a finding, not a stop.)
2. **The function-labeling layer is DORMANT, not a live consumer.** `functionresolver`,
   `functionprogression`, `functionromannumeral` read only their own internal L4→L5 contract
   types (`FunctionSlice`, `ProgressionChord`, `BaseRomanNumeralInput`, …), never the region
   surface; their headers state "no production consumer." So "sectionanalyzer + downstream
   function-labeling" resolves to `sectionanalyzer.cpp` + `sectioncadencedetection.cpp` for
   live surface reads; the `function/*` files carry NO surface-consumption load today.
3. **Accessibility reads no struct.** `notationaccessibility.cpp` consumes only the formatted
   string from `harmonicAnnotation`, so its A2 disposition is entirely downstream of the
   composingbridge formatter — it imposes no direct field requirement on A's record.

`groupinglayer.h` and `jointkeydecision.h` name the derived surface only as future
retirement/reuse targets or a dormant, default-disabled J-key-iii wiring flag — not live
consumers.

---

## Task 1 — the consumer / field enumeration

Full row-level detail: `tools/audit/notation_surface/consumption_fields.csv`
(**75 field rows**, one per (live consumer, consumed surface field), with representative
read-site anchors). Class breakdown (from `summary.json`):

| disposition class | count | meaning |
|---|---:|---|
| **A-SOURCED** | 56 | a declared A-surface source exists (SegmentSummary field, posterior OI-193, modal reading C1, or a derived chord fact) |
| **DERIVABLE** | 13 | recomputable from A-published facts (derivation named per row) |
| **RETIRE-CANDIDATE** | 4 | no live consumer reads it (or the concern dissolves under A) |
| **UNRESOLVED** | 2 | cannot be dispositioned from A's surface + the ratified publications → returns to the user |

**No consumed, decision-bearing field is left un-dispositioned except the two UNRESOLVED
findings below.** The bulk map is clean because A's per-segment record is a *richer* native
form of what the legacy record carries: A's chord state is scale-degree-valued relative to
(tonic, major/minor), so `chordResult.function.degree` is `SegmentSummary.degree` directly,
`function.diatonicToKey` is the class's own diatonic/chromatic question, and the applied-chord
`target` is native (replacing the `nextRootPc` heuristic).

**The two structural clusters that ride ratified publications, not raw SegmentSummary fields:**

- **The confidence cluster (→ B-full posterior, OI-193).** Every consumer's confidence read is
  `keyModeResult.normalizedConfidence` (the emission sigmoid) — never `HarmonicRegion.keyConfidence`.
  It feeds the OI-182 exposure gates, `hasAssertiveExposure` (0.8), the cadence/pivot gate,
  the key-area opening bar, `modeNameConfidenceThreshold` (0.35), and the carried
  `NoteHarmonicContext.keyConfidence`. All map to the B-full posterior key-marginal mass/gap
  (this is Task 3's disposition target).
- **The ranked-alternatives read (→ B-full posterior).** `alternatives` flows into
  `NoteHarmonicContext.chordResults[1..]` and is surfaced by the right-click menu and status
  bar → the posterior's ranked alternatives.

**Notable DERIVABLE items (derivation named in the CSV):** the sounding `tones[].pitch/.tpc`
(re-collect from the score over the segment span — the same L1 note surface A's fact adapter
already consumes); `chordResult.identity.bassPc/bassTpc/extensions/rootTpc` and the chord symbol
(the derived chord facts from A's (tonic, mode, class, inversion)); the whole `KeyArea` grouping
+ `keyAreaId` (collapse A's per-segment key sequence, exactly as `analyzeSection` derives them
from regions today); `diatonicToKey` (from A's degree/classKey).

**Per-consumer row counts** (`summary.json` → `rows_per_consumer`): notationcomposingbridge 24
(incl. its `helpers.cpp` reads), sectionanalyzer 17, notationimplodebridge 14,
sectioncadencedetection 7, notationtuningbridge 5, notationcontextmenumodel 5,
notationinteraction 2, notationaccessibility 1 (string-only).

### Tests that pin the surface (follow the switch; do not decide the contract)

| test | pins |
|---|---|
| `pipeline_snapshot_tests.cpp` | P1/P2/P3/P4 output goldens over a 10-score corpus (region + section + single-note paths) |
| `notationimplode_tests.cpp` | chord-track implode output (region stream + `analyzeNoteHarmonicContextDetails`) |
| `notationannotate_tests.cpp` | annotation emission |
| `notationinteraction_harmony_pinning_tests.cpp` | `analyzeNoteHarmonicContext` harmony-writing |
| `notationdecodecache_tests.cpp` | bounded-window decode cache |
| `regionanalysis_tests.cpp`, `reachback_tests.cpp` (composing) | `HarmonicRegion` / `keyAlternatives` at the composing layer |

These refresh (snapshot-class) or STOP (unit-class) at the switch per §8.4; they are not
contract inputs.

---

## Task 2 — the exotic-mode (`KeySigMode` beyond Ionian/Aeolian) consumer list

**12 sites** (`summary.json` → `task2_exotic_mode_sites`). The 21-value mode enum reaches the
notation path through one plumbing stack and a set of display/relationship branches:

- **The 21-mode-prior stack (retires whole under C1's two-mode key):** the seam plumbing
  `notationharmonicrhythmbridge.cpp:92-113`; the interface `icomposinganalysisconfiguration.h:157-252`
  (21 getters/setters/notifications + preset helpers + `modeNameConfidenceThreshold` :117); the
  persisted settings `composingconfiguration.cpp` (21 `MODE_PRIOR_*` keys + `MODE_NAME_CONFIDENCE_THRESHOLD` :48);
  the preferences model `composingpreferencesmodel.{h,cpp}` (88 `modePrior` refs = 21 UI-model
  properties); the UI `ComposingAnalysisSection.qml` (105 refs) + `ComposingPreferencesPage.qml`.
  Under C1 the 19 exotic-mode priors go dead → **retirement-map item 2**.
- **Display/relationship branches on exotic modes:** `notationcomposingbridge.cpp:1047-1059`
  (`makeBracketMarker` — Lydian/Mixolydian case, HarmonicMinor/MelodicMinor bare-colon vs
  suffix); `:771/:863` (`keyModeSuffix(mode)` status-bar/area strings);
  `notationimplodebridge.cpp:103-119` (`fallbackModeSuffix` + `keyAnnotationBaseLabel`, the
  confidence-gated exotic-vs-broad suffix); `:941-1004,:1233-1269` (relationship arrows,
  modulation-pivot, borrowed-key search over all 21 modes with an Ionian/Aeolian tie-break).
- **The per-mode scale/degree lookups** `keyModeScaleIntervals(mode)` — A-SOURCED (A's degree
  state is native scale-degree relative to (tonic, major/minor); the 21-mode scale table is not
  needed).
- **The shared formatter** `keymodeformatting.cpp:82-134` (`keyModeSuffix`/`keyModeTonicName`
  21-mode name tables) the notation path routes through — becomes unreachable from the notation
  surface once the 21-value mode is no longer published (C1).

**Proposed disposition (C1):** none of these needs the 21-value mode. The two-mode key +
the published un-rounded modal reading carries the information; the exotic-mode plumbing, UI,
and display branches retire. The measured OI-174 defect class ("`Altered` emitted over material
with no altered tone") becomes structurally unreachable.

---

## Task 3 — the OI-182 exposure-bucket constants' fate

`summary.json` → `task3_oi182_constants`. All the exposure constants are fed by ONE value —
`keyModeResult.normalizedConfidence` (the emission sigmoid) — and split into two fates:

| construct | loc | fed by | controls | proposed disposition |
|---|---|---|---|---|
| `kTentativeKeyExposureThreshold = 0.5` | implodebridge:79 | normalizedConfidence | `supportsTentativeKeyExposure` → key-run emission gate (:205) + bucket lower bound | **confidence-mapping** → posterior key-marginal mass/gap threshold |
| `kAssertiveKeyExposureThreshold = 0.8` | implodebridge:80 | normalizedConfidence | `keyExposureBucket` 1↔2 boundary → region coalescing | **confidence-mapping** → posterior mass; shares fate with `hasAssertiveExposure` |
| `keyExposureBucket()` | implodebridge:87-96 | normalizedConfidence | `sameUserFacingInference` coalescing → chord-track segmentation | **confidence-mapping** → posterior-mass band |
| `kAnnotateKeyConfidenceThreshold = 0.8` | sectionanalyzer.h:91 | normalizedConfidence | cadence/pivot gate + key-area opening + `hasAssertiveExposure` | **confidence-mapping** → posterior mass threshold |
| `modeNameConfidenceThreshold = 0.35` | icomposinganalysisconfiguration.h:117 | normalizedConfidence | true-suffix vs `fallbackModeSuffix` | **RETIRE under C1** (no exotic suffix to gate); confidence role folds into posterior mass |
| `fallbackModeSuffix()` | implodebridge:103-108 | mode + 0.35 gate | collapse exotic suffix → major/minor under low confidence | **RETIRE under C1** (two-mode label is default; modal reading published beside) |
| `kSameChordReannotationGap = 960 ticks` | implodebridge:661 | tick gap + coalescing | consecutive same-chord merge vs separate re-annotation → segmentation | **NOT a confidence value** — a presentation-timing constant; re-home to the notation emitter over A's segment stream (survives the switch as an emitter-side option, not an inference value) |

The confidence-mapping cluster is the input the contract's confidence-mapping ruling
disposes; the B-full posterior gap/mass replaces `normalizedConfidence` as the feeder.

---

## Task 4 — the in-memory-only fields (confirmed at the code)

Both **unchanged** vs decision-doc §1, confirmed by tree-wide grep:

- **`keyAlternatives`** — defined `harmonicrhythm.h:118`, populated in `regionanalyzer.cpp`
  (`:279/:552/:1043/:1062`); the **only** reader is a composing-layer regression test
  (`regionanalysis_tests.cpp:510-525`). Not even carried into `AnalyzedRegion` (the translation
  copies eight fields; this is dropped at the boundary). **No production consumer.**
- **`fanout`** — defined `harmonicrhythm.h:130`, populated via `computeRawFanoutSummary`
  (`regionanalyzer.cpp:1066/1262/1454`); the **only** reader anywhere is `tools/batch_analyze.cpp`'s
  `--dump-fanout` diagnostic (`:699/:1419-1422`) — batch surface, read-only, not the notation
  path. **No production consumer.**

---

## Findings

### UNRESOLVED (decision-bearing, provably not on A's surface + ratified publications) — return to the user

Two, both the pedal-point annotation on the region-emit path:

- **`chordResult.identity.isPedalPoint`** (`notationcomposingbridge.cpp:1202`) and
  **`chordResult.identity.pedalBassPc`** (`:1203/:1206-1207`) gate and populate the "X ped."
  pedal-point StaffText annotation. A's `DecodeResult`/`SegmentSummary` carries **no
  pedal-point concept**, and whether A's factorization models pedal points is **not
  determinable from the decoder surface** (I did not guess it — #18/never-guess). Per the
  dispatch this is a FINDING, not a stop: reported UNRESOLVED, it returns to the user as its own
  disposition (decision-doc §3 anticipates exactly this — a consumed legacy fact not yet
  publishable from A's surface). If A does not model pedal points, the pedal annotation would
  drop at the switch (a #12 loss to be ruled acceptable or to gate the increment).

### RETIRE-CANDIDATES (no live reader / concern dissolves under A)

Four (`summary.json` → `retire_candidates`): `HarmonicRegion.hasAnalyzedChord` (carried, never
read — A always decodes a segment); `HarmonicRegion.temporalExtensions` and its
`AnalyzedRegion`/`NoteHarmonicContext` copies (the whole struct is copied but **no sub-field is
ever read on any consumer** — decode-time-internal); `keyModeResult.score` (written only on a
dead `*outScore` path no caller supplies). Plus the Task-4 `keyAlternatives`/`fanout` (already
no consumer). These lose no consumed information at the switch.

---

## Unknowns / caveats

- **Whether A models pedal points** — the sole load-bearing unknown (the two UNRESOLVED rows).
  Not determinable from the C++ decoder surface; escalated, not guessed.
- **The aug-sixth P5 discriminator** (`identity.naturalFifthPresent`, Italian vs German +6):
  dispositioned DERIVABLE from A's chromatic aug-sixth vocabulary classes (the GT-derived
  `classKey` distinguishes It/Ger/Fr aug6), but this rests on A's vocabulary preserving that
  distinction — a light open question for the contract-drafting step, not a decision-bearing
  blocker (aug6 is a narrow chromatic case, consumed only inside the formatter).
- **Root/bass spelling** (`rootTpc`/`bassTpc`) dispositioned DERIVABLE from (key, degree/class):
  a deterministic music-theory mapping, but the derivation is an instrument that must be
  *established* (#19) at build time — noted for the drafting step; the term inventory recorded
  the L3 emission is spelling-blind, so the display spelling is a derived (key+degree) fact, not
  an inferred one.
- **Field-read completeness** rests on four independent read-only extraction passes over the
  eight live consumers + the section/function layer, cross-checked against my own tree-wide
  greps for each accessor token; every row carries a file:line anchor. Reads inside the shared
  composing-module formatter/voicing (`ChordSymbolFormatter::format*`, `closePositionVoicing`,
  `chordTonePitchClasses`) are attributed to the whole `chordResult` they are passed, not
  re-enumerated field-by-field (those live outside the notation path and are covered by the
  "derived chord facts" disposition).
- Dispositions are **proposals**, not decisions (dispatch); UNRESOLVED items and every
  disposition return to the Cowork/user rulings at contract drafting.

---

## Reuse-vs-new / what-retires (standing section)

- **Reuse:** the audit generator reuses the existing `tools/audit` tooling pattern (a
  self-contained Python generator emitting CSV + JSON from an embedded, code-verified
  enumeration, the same shape as `gen_dispositions.py` / the L3–L5 audit CSVs). It carries that
  pattern's establishment forward (#19) — no new instrument class.
- **What retires:** **nothing.** This is a read-only investigation; it deletes no code, changes
  no behavior, and adds only two untracked-plus-artifact deliverables. The *findings* name what
  the later build increment will retire (the 21-mode-prior stack, the OI-182 exotic/confidence
  machinery, `temporalExtensions`, `hasAnalyzedChord`), but this audit retires none of it.

---

## Self-check (CLAUDE.md, after the coding exercise)

Re-read the two commits' actual diffs against the principles and `DEFECT_TYPES.md`: Task 0 is a
verbatim insertion of the ratified corollary + the specified STATUS/provenance text (no
self-invented labels; provenance-stamped; #14 ratified record). The artifact is a data
generator with figures derived not hand-typed (#17f); the report cites only artifact figures.
No `src/` touched; no unverified causal claim carried (the one un-checkable premise — whether A
models pedal points — is reported UNRESOLVED, not assumed, #18). No STOP condition tripped;
the out-of-roster consumers are findings, included and flagged, per the dispatch.
