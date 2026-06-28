# L1–L4 architecture audit — unification, layering, coverage, staleness, dead code, principles

> **★ RESOLUTION UPDATE (2026-06-26, post-L4-build + L1–L4 review).** Several findings here are now CLOSED: the Q4
> STATUS.md gate contradiction is RESOLVED (STATUS synced to 53/24/53); the Q4 stale CMake "NOT wired" comments are
> corrected; the Q1.3 "kMasks re-typed by hand" is closed (kMasks AND `templates[]` now derive from canonical
> `kTemplateIntervals`); and the Q2/Q5 framing of `chordslicedecoder` as "aspirational / not-the-real-path" is superseded
> — the new L4 path is now BUILT (complete) and intentionally **DORMANT** (deferred-engagement, joint with L5), NOT
> dead-code-to-delete. Still-open items (the two segmenters, two pitch-context builders, `analysisutils.h` relocation)
> remain migration debt scheduled for the joint-L5 engagement. Read the findings below with this banner.
>
> **Status: findings, read-only (2026-06-26).** Answers the six standing-quality questions over `src/composing/analysis/`
> (L1 notemodel, L1.5 engravingbridge, L2 slicing, L3 key, L4 chord + the function/decode/harmony/section/scoreharvest
> dirs) and `src/composing/tests/`. Built from three parallel source audits, with every load-bearing claim re-verified
> by Cowork at the file. Each finding is cited; verdicts distinguish **design debt** (wrong cut) from **migration debt**
> (right cut, legacy not yet retired) — almost everything here is the latter.
>
> **The through-line:** the *target* architecture (forward-only L1→L1.5→L2→L3→L4) is sound and the new modules are
> cleanly separated. The deviations are overwhelmingly **incomplete migration** — the new pure module exists and is
> partly/most-wired, but the **legacy implementation still runs in parallel on the production orchestrator**
> (`region/regionanalyzer.cpp`). That is exactly what the stabilization plan exists to retire; this audit sizes it.

## Q1 — 100% unification / no duplicated logic? — **NO. Three real duplications, all on the live path.**

1. **Two live change-point grids (L2).** `harmony/greedyExpandSegmentation` (chord-score-aware, walks the engraving DOM)
   runs at `regionanalyzer.cpp:757` for the chord-rhythm grid, while the new pure `slicing/changePointSlices`
   (interpretation-free, over the L1 NoteModel) runs at `regionanalyzer.cpp:579/651` for the key axis. **Two
   segmentation philosophies coexist in one production call.** Self-documented as transitional (`harmonicsegmenter.cpp:152-156`
   names `changePointSlices` its "Layer-2 successor"). *(Cowork-verified at source.)* This is the single biggest
   deviation from "one path per concern."
2. **Two live pitch-context builders (L3).** `engravingbridge::collectPitchContext` (DOM-walk, point-anchored) is live
   via `keyresolver.cpp:311`; `pitchContextOverSpan` (indexed, span-anchored) is live via `keymodesequence.cpp`. Both
   build the windowed weighted pitch-context for key scoring. The decay math is already unified (both call shared
   `scoreharvest::timeDecay`); only the note-collection walk is duplicated. *(Cowork-verified.)*
3. **`kMasks` hand-mirrors the template interval table (L4 data duplication).** The per-template chord-tone intervals
   live in `chordanalyzer.cpp` (`templates[]`) and are **re-typed by hand** as bitmasks in
   `function/harmonicfunctionlayer.cpp` (`kMasks`). The compiler enforces only the *count*, not the *contents* — a
   wrong/zero mask silently disables Gate R. Derivable from the template intervals; maintained by hand.

**Correctly unified (checked, not duplicated):** the tpc/line-of-fifths interpretation is built once (`tpcForPc` at
`chordanalyzer.cpp:1131`) and threaded — every downstream reads it (good; this is the L4 fold-in target the Phase-4
primitive will eventually subsume). The three "decoders" (`ChordPathDecoder`, `ChordSliceDecoder`,
`KeyModeSequenceDecoder`) decode *different axes* (commit-threading / chord-symbol / key-mode) — legitimately separate,
not duplicates.

## Q2 — Are L1–L4 the right layers? Room for more separation? — **Cut is sound; three refinements; the real issue is migration, not design.**

**Module→layer map is clean and forward-ordered.** notemodel = L1 (narrow, stores facts, no interpretation);
engravingbridge = L1.5 (view-only derived reads); slicing = L2 (interpretation-free); key/ is well-decomposed into
emission (`keymodeanalyzer`) / sequence-decode (`keymodesequence`) / resolution (`keyresolver`) / formatting / presets —
**not a blob**; chord/ separated into oracle / post-passes / gates / voicing / formatting. *(Cowork-verified map.)*

**Dependency direction is forward on the behavioral spine** — no case of L1/L2 reaching up into key/chord *behavior*.
The exceptions are narrow and worth fixing:

- **Type-only header back-edges.** `engravingbridge/regiontonecollector.h:48-49` includes `chordanalyzer.h` +
  `keymodeanalyzer.h`, and `keymodeanalyzer.h:34` includes `chord/analysisutils.h` — **only to name shared value
  types** (no behavior called). Real but minor: L1.5/L3 cannot *compile* without L4 headers. **Candidate: extract a
  leaf `analysis/types/` header** to make the include graph genuinely acyclic.
- **Intra-L4 scorer↔competition near-cycle.** `chordanalyzer.h` forward-declares `function::ScoringSnapshot`
  specifically to avoid a circular include with `harmonicfunctionlayer.h`. Managed, but a genuine mutual dependency.
- **`function/` mixes two layers under one dir name.** `harmonicfunctionlayer` is **L4 winner-selection** (production,
  called inside `analyzeChord`); `tonicizationlabeler` is **L5/L6 functional labeling** (diagnostic-only). They share a
  directory by name only — the labeler's own header says it is "distinct." **Candidate: split the L5/L6 labeler into a
  future `functional/` dir.**

**Possible further separation (the one genuine design question):** the **winner-selection competition**
(`harmonicfunctionlayer`) sits *inside* L4 scoring but is arguably its own concern between "score every candidate" (L4
oracle) and "assign function" (L5). Not urgent — but if any layer is a candidate to become its own unit, it is this.

**The dominant Q2 fact is migration, not design:** L2 runs legacy+new in parallel (Q1.1), and L4's intended pure path
(`chordslicedecoder`) is **not wired at all** — production chord identity still flows through legacy
`analyzeChord` + `ChordPathDecoder` in `regionanalyzer.cpp`. So "L4 = the clean new chord/ path" is **aspirational on
the live path today.** *(Cowork-verified: `ChordSliceDecoder` appears in no `regionanalyzer` line.)*

## Q3 — 100% regression coverage? — **NO, but SUPERSEDED by CC's MEASURED audit (see banner).**

> **★ CORRECTION 2026-06-26 — the coverage claims below were partly WRONG (compromised reads).** The follow-on
> four-criteria test-adequacy audit (Cowork's parallel agents) and parts of this Q3 list were produced by reading the
> working tree through a **flaky Linux mount that served truncated file content** — the same fault that made
> `note_model.h`/`slicer.{h,cpp}` *appear* truncated to the sandbox while they are byte-identical to HEAD on Windows
> (CC-verified; green build is impossible with a truncated `note_model.h`). The agents therefore "saw" missing tests
> that **do exist**. **CC's on-Windows MEASURED audit (`cc_tree_repair_and_coverage_report.md`) is authoritative.**
> Specifically REFUTED at source: the **L2 clip is well-tested** (`slicer_tests.cpp` CP1–CP7, incl. the
> re-slice-equivalence invariant; slicing 100% line); **`chordpostpasses` IS directly tested** (`applyIter8691Pedal`,
> 6 tests); **L3 emission robustness IS tested** (empty/single/chromatic/out-of-range — only *unison* missing);
> `sectioncadencedetection`/`metricweights` are better-covered than stated. Measured union line%: L1 97.7 · L1.5 98.2 ·
> L2 slicing 100 · L2 harmony 98.6 · L3 key 83.3 · L4 chord 93.6 · L4 function 96.2 · region 85.8 · section 89.4.
> **GENUINELY confirmed gaps (the real backfill list):** `chordvoicing` 0% direct; `modepriorpresets` 0%;
> `ChordSymbolFormatter::formatNashvilleNumber` (1 test); L4 `analyzeChord` robustness (only the <3-PC gate); the L3
> option threads (`excludeStaves`, `ignoreDeclaredMode`, lookahead loop, `populateEmissionConfidence`) are
> *line-executed but branch/assertion-untested* — line coverage cannot see which branch ran or whether output was
> asserted; the production L4 has no abstain/uncertain/inherit (spec outcome untestable; the spec-conformant
> `chordslicedecoder` is production-dead, spelling-pin unbuilt). **Branch coverage (criterion 4) could not be measured —
> no coverage toolchain on the machine** (`OpenCppCoverage`/`gcov`/`llvm-cov` absent); only block/line was available.

Three test binaries: **composing_tests** (22 unit/component files), **notation_tests** (the bridge path),
**pipeline_snapshot_tests** (end-to-end P1–P4 goldens over a 12-score DCML corpus, capped at 16 measures, six pinned
arrays). *(The original bullet list that stood here is retracted — see the correction banner; trust the measured
numbers, not the negative-grep gaps.)*

## Q4 — Stale code / docs / comments / tests / tools? — **YES, several; one high-impact.**

- **HIGH IMPACT — the gate baseline contradicts itself.** `STATUS.md` (mandated session-start reading) still presents
  **57/23/57** as the live gate (last updated 2026-06-14); CLAUDE.md is on the ratified **53/24/53**. *(Cowork-verified
  STATUS.md:6/8.)* Same stale 57/23/57 in `docs/score_inventory.md`, `docs/decoder_design.md`,
  `docs/implementation_roadmap.md`, and ~8 stage-design docs. **The two docs CLAUDE.md tells you to trust disagree.**
- **Stale "NOT wired" comments.** `CMakeLists.txt` still calls `keymodesequence`, the `slicer`, and `jointkeydecision`
  "NOT wired" — all three are now wired (`regionanalyzer.cpp:475/579/581`). The headers are correct; the CMake comments
  predate the L3 wiring.
- **Orphaned test fixtures — CORRECTED 2026-06-26 (the original list was partly wrong; CC re-verified whole-repo).**
  Confirmed orphan, zero references: **only** `chord_analysis_test.{musicxml,_expected.json,py}` (literal "content
  moved" stubs). **NOT orphans:** `mono_smoke_test.musicxml` is loaded and asserted by
  `tools/test_batch_analyze_regressions.py:117,137` *(Cowork-verified)* — the original audit used a negative-grep
  scoped to `src/composing/tests/` and missed the `tools/` caller; `data/solid theory.musicxml` is provenance-
  referenced in `note_model_tests.cpp` comments (not a clean orphan). Lesson: orphan claims need a **whole-repo** grep,
  not a per-dir one.
- **Stale tool defaults:** several `tools/` diagnostic scripts still default to the deprecated shared `tools/corpus`
  dir (pre per-preset layout); `analyze_inversion_errors.py` keeps a self-labeled deprecated `--ours-dir` alias.
- **Doc casing:** CLAUDE.md references `build_and_test.md`; the file on disk is `BUILD_AND_TEST.md` (same file on this
  case-insensitive mount — a reference mismatch, not two copies).

## Q5 — Dead / unreachable code? — **YES, but mostly INTENTIONAL staged scaffolding, not rot. The distinction matters.**

- **`DecodeQualityLevel::Normal`/`Deep` are inert** — `ChordPathDecoder::commit()` ignores the level; all levels behave
  as `FastBeam1` (reserved for a future stage; tests assert byte-identity). A real always-FastBeam1 dead branch.
- **`redecodeRange()` (both decoders) is test-only** — the incremental-re-decode seam is built and tested but has no
  production caller (it is the deferred incremental path — the same "build ahead, wire later" pattern).
- **`chordslicedecoder` (intended L4) is production-dead** — reachable only via `batch_analyze --decode-chords`. This is
  the new L4 built byte-identical *ahead* of wiring — deliberate, not accidental.
- **`tonicizationlabeler` (L5/L6) is production-dead** — diagnostic-only (`--dump-tonicization`); staged, not wired.
- **`jointkeydecision` defaults OFF** (`jointKeyWiringEnabled()` false) — diagnostic.

**Crucial framing:** items 3–5 are *deliberate ahead-of-wiring scaffolding* (the same discipline as the bounded-context
capability we just built byte-identical before engaging). They are not "logically unreachable rot" — they are wired-off
by design and have a planned engagement step. Items 1–2 are reserved-but-inert and should be tracked so they don't rot.
*(Cowork-verified `chordslicedecoder` has no `regionanalyzer` reference.)*

## Q6 — Established guiding principles, and adherence

The principles we have set (from the design docs + CLAUDE.md):

1. **Forward-only inference; fact-gathering flows backward.** Inference runs L1→L6; only *context requests* (the
   bounded-context extend) flow down, never an analysis back-edge. **Adhered to on the behavioral spine** (no L1/L2
   reaching up into key/chord behavior). Exceptions: the type-only header back-edges + the intra-L4 scorer↔function
   near-cycle (Q2) — real but narrow.
2. **Maximal information (use all evidence, incl. notated spelling/tpc, early).** **In progress** — Phase 4 is building
   exactly this. Today L4 uses tpc; L3 uses none (the Phase-B term).
3. **Minimality / one (evidence-source × question) per layer.** Mostly adhered to; `key/` is a model decomposition.
4. **Total unification — one path per concern.** **The principle most in tension with current reality** — Q1's two
   segmenters + two pitch-context builders + kMasks are live violations (all migration debt).
5. **Knowledge-based — measure before building; a disproving measurement is a success.** Adhered to (the reach-back
   proxy and the Mozart hypothesis were both killed by measurement).
6. **Byte-identity guards where a step must not move output.** Adhered to (Phases 1–4 gates).
7. **Build-it-right before tune-precision; no inference-fixing until refactor/architecture/algorithmic completion.**
   Adhered to — and this audit *is* part of build-it-right.
8. **Amendments in the proper layer; no cross-layer creep.** Adhered to (the L1 sentinel fix was deferred, not folded
   into Phase 4).
9. **Predicates must be qualified (spec-writing rule).** Adhered to in the rewritten specs.

## What this means for the plan (not new work — sequencing)

The audit converges on one conclusion: **the architecture is right; the debt is unretired legacy on the orchestrator.**
That is precisely the stabilization plan's job. Concretely, it adds/sharpens these items (to schedule, *not* to act on
now — build-it-right order still holds):

- **Unification targets (one path per concern):** retire legacy L2 (`greedyExpandSegmentation`) onto `slicing/slicer`;
  collapse the two pitch-context builders to one; derive `kMasks` from the template intervals. *(These are the
  "engagement" steps the bounded-context/L4 builds lead toward.)*
- **Layering refinements:** extract a types-only header (kill the cross-layer header back-edges); split `function/` so
  the L5/L6 labeler leaves the L4 dir; decide whether winner-selection becomes its own unit.
- **Coverage backfill (Phase 5 / pre-L4):** unit tests for chordvoicing, chordpostpasses, sectionanalyzer,
  formatNashvilleNumber.
- **Doc hygiene (do soon — it is actively misleading):** STATUS.md + the 8 docs to 53/24/53; the stale CMake "NOT wired"
  comments; orphaned fixtures; tool corpus-dir defaults. *(This is the doc-hygiene refresh already on the deferred
  list — the gate contradiction makes it higher priority than "deferred.")*
- **Dead-code tracking:** keep the intentional scaffolding (chordslicedecoder, redecodeRange, tonicizationlabeler) on
  the engagement ledger so it is wired or removed, not left to rot; track the inert DecodeQualityLevel enumerators.

**Confidence & limits:** module map, dependency graph, production-vs-diagnostic status, the gate contradiction, and the
two-live-segmenters / chordslicedecoder-dead findings are Cowork-verified at source. "No direct test" verdicts rest on
negative grep (high, not certain). Read-only throughout — "production path" = static call/include reachability, not a
runtime trace; the "byte-identical" claims for the parallel grids/builders are the headers' own claims, not re-measured
here.
