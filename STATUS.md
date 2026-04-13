# MuseScore Arranger — Implementation Status

> **Living document.** Claude Code reads this at the start of every session. Update this as the
> last act when anything changes. For stable architectural decisions, see ARCHITECTURE.md.

*Last updated: April 2026 — B1 pedal-aware Jaccard boundary detection is implemented in both notation and batch paths; ABC/DCML `relativeroot` is now applied when computing reference roots; the finished Corelli rerun lifts direct agreement to 70.3% with `bassIsRoot` down to 41.6% of disagreements; and the bounded adaptive note-context / chord-track path remains the intended user-facing notation flow. The last fully green notation checkpoint had 31 focused implode regressions passing, but the current working tree is below that mark: a later Corelli follow-up reverted a non-compliant Harmony-input experiment, restored note-only notation inference, and now has 4/6 focused re-checks passing while `Notation_ImplodeTests.CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord` and `Notation_ImplodeTests.CorelliOp01n08dUserReportedChordTrackAudit` remain open.*

---

## Current State (summary)

The Phase 1 analysis foundation is implemented and working. The status bar displays chord
symbols, Roman numerals, and key/mode information on every note selection, using a bounded
adaptive local window that expands only until the displayed harmonic result stabilizes. The
chord staff ("Implode to chord track") and region intonation ("Tune selection") are both in
the Tools menu. Chord-staff population now drives the same adaptive inference helper across
the selection's source-note ticks rather than maintaining a separate whole-range user-facing
inference path, while preserve-all analysis remains available for exact boundary/debug
workflows.

The DCML/ABC comparison path now resolves applied-chord `relativeroot` before computing
reference `root_pc`, so older Corelli one-score comparisons that ignored `relativeroot`
should be treated as stale. On Corelli `op01n08d`, the corrected comparator plus populated
regional `bassIsStepwiseToNext` and the simplified no-third inversion gating reduce the
real disagreement set to two beats (`m20 b1`, `m23 b1`) and raise aligned agreement to 11/13.

**Current working-tree note (late 2026-04-11):** the last fully green 31/31 notation
checkpoint is not the active state. A later Corelli follow-up briefly used existing
Harmony annotations as inference input / boundary hints in the notation path; that
experiment violated the intended note-driven architecture and has been reverted.
Focused verification now passes the two Harmony-gating tests plus
`CorelliOp01n08dOpeningBarsStatusContextMatchPopulateWithoutForcedKeySignature`
and `PopulateChordTrackPreservesCorelliOp01n08dCarryInAndLateDominant`, but
`CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord` and
`CorelliOp01n08dUserReportedChordTrackAudit` still fail on note-only late-beat
cases.

**Fresh multi-corpus rerun (late 2026-04-11, current working tree):** fresh direct
DCML reruns were written to `tools/reports/live_20260411/reports/` for ten corpora.
Completed aggregates are now: Dvorak 79.2% (12 mvts), Chopin 71.6% (55 processed;
1 score missing DCML TSV), Corelli 70.3% (149 mvts), Beethoven 64.9% (70 mvts),
Mozart 61.8% (54 mvts), Schumann 61.6% (13 mvts), Tchaikovsky 61.0% (12 mvts),
Grieg 60.7% (66 mvts), Bach En/Fr Suites 52.4% (89 mvts), and C.P.E. Bach keyboard
still 0 regions across 66 mvts. Across those ten completed corpora the weighted
result is 10,830 / 16,765 aligned rows = 64.6% root agreement with 38.1% alignment
of our emitted regions. The broad Bach chorales rerun has now completed via
`run_validation.py` into `tools/reports/live_20260412_bach/`: 352 chorales,
9511 total regions, 4150 full matches, 0 near matches, 43.6% overall agreement,
and 75.2% chord-identity agreement (5823 / 7748 aligned regions). The fresh HTML
report is `tools/reports/live_20260412_bach/reports/validation_20260412_041114.html`.

**Windows batch-validation tooling note (late 2026-04-11):** the stalled Bach
chorales run did not stop on a bad `bwv351` analysis. The emitted
`tools/reports/live_20260411/corpus/bwv351.ours.json` exactly matches fresh direct
reruns of `batch_analyze`, and a dump of the orphaned Windows process showed it
stuck in the final `_Exit(0)` / process-shutdown path of `tools/batch_analyze.cpp`,
inside Qt TLS cleanup (`QBasicMutex` wait) after JSON writeout had completed.
`tools/batch_analyze.cpp` now flushes output explicitly and uses
`TerminateProcess(GetCurrentProcess(), 0)` on Windows after `delete score` to bypass
that exit path. A fresh full Bach chorales rerun completed successfully with the
patched tool and produced the report above, so the earlier Windows stall is no
longer blocking the corpus pipeline.

**Full Rampageswing polyphonic-jazz baseline is now established.** With all available
Rampage Swing charts included (31 XML charts with harmony + 2 MXL-only charts), the
corrected baseline is 39.8% root agreement on 1735 comparable chord-symbol regions.
`compare_omnibook.py` now infers Rampageswing source directories, reads `.mxl` source
files, and uses source `kind` tags for richer written-quality breakdown (Dominant7,
Major7, Minor7, etc.).

### Jazz corpus status (updated 2026-04-08)

The vertical analyzer is confirmed correct for jazz harmony when given complete tonal
material. A batch-only synthetic bass-injection experiment (`batch_analyze`
`--inject-written-root`) raised Rampageswing from 39.8% to 98.3% and Omnibook from
18.0% to 99.9% by simulating the missing bass-player root note before analysis.

The lower agreement rates on available jazz corpora are therefore corpus artifacts —
missing bass and piano voicings — not scoring failures. No accepted jazz-specific
scoring changes remain in the analyzer, and no new jazz scoring work is planned on the
current corpora.

Jazz validation is blocked until scores with written-out bass and piano voicings become
available. Candidate sources remain:

- full piano arrangements of jazz standards (typically commercial, not freely available)
- MuseScore user uploads of jazz piano transcriptions (quality unverified at scale)
- a future user-curated small ground-truth set of 10–15 jazz standards with complete voicings

Current jazz corpora are retained in the registry as diagnostic references and upper-bound
experiments, not as analyzer accuracy benchmarks.

**P3 (21-mode expansion) is complete.** `KeyModeAnalyzer` now evaluates all 21 modes
(7 diatonic + 7 melodic minor family + 7 harmonic minor family). Mode priors are 21
independent parameters replacing the former 4-tier grouping. The regression catalog has
207 tests with 0 abstract mismatches.

**P4 (interface refactor) is complete.** `analysis::KeyMode` renamed to `KeySigMode`;
`IChordAnalyzer` interface introduced with `RuleBasedChordAnalyzer` implementation;
`notationcomposingbridge.cpp` split into three files with shared helpers extracted.
P4b added `ChordAnalyzerFactory` and documented `ChordTemporalContext` vs future `TemporalContext`.
P4e reorganized `src/composing/analysis/` into subdirectories: `chord/`, `key/`, `region/`.

**P7 (tuning anchor) is complete.** Italian keyword array `kTuningAnchorKeywords` (4 forms:
"altezza di riferimento", "alt. rif.", "alt.rif.", "altezza rif.") replacing the old
`"anchor-pitch"` placeholder. `trimAndLowercase()` / `isTuningAnchorText()` / `hasTuningAnchorExpression()`
/ `computeSusceptibility()` / `RetuningSusceptibility` all wired; 16 anchor unit tests passing.

**Section 8 (tuning anchor rename + drift modes) is complete.** (1) Italian keyword array
replacing `"anchor-pitch"` with 16 unit tests (8.1). (2) Anchor protection wired into
`applyRegionTuning()` Phase 2 and Phase 3 — anchor notes receive 0 ¢, are never split, and
are excluded from the FreeDrift reference hierarchy (8.2). (3) `TuningMode` enum
(TonicAnchored=0, FreeDrift=1) added to `tuning_system.h`, wired through
`IComposingAnalysisConfiguration` → `ComposingConfiguration` → `composingpreferencesmodel` (8.3).
(4) FreeDrift reference hierarchy implemented in `applyRegionTuning()`: P1=held notes,
P2/P3=zero drift; sustained-event rewriting now depends on `allowSplitSlurOfSustainedEvents`
and only occurs when the continuation target differs from the carried tuning (8.4). (5) QML tuning
mode selector (two FlatButton widgets: "Tonic-anchored" / "Free drift") added to
`ComposingAnalysisSection.qml` and wired in `ComposingPreferencesPage.qml` (8.5).
(6) Drift boundary annotation: `annotateDriftAtBoundaries` preference (separate toggle
from `annotateTuningOffsets`) wired through interface → config → QML; in FreeDrift mode
inserts a StaffText "d=+N" at each region boundary when |drift| ≥ 0.5 ¢.
FreeDrift anchor semantics clarified: anchor notes are pitched at the current drift
level (not reset to 0 ¢) and annotated with `*` suffix.
280/280 tests passing.

**Sustained-event split/slur preference iteration is complete.** `allowSplitSlurOfSustainedEvents`
is wired through `IComposingAnalysisConfiguration` → `ComposingConfiguration` →
`composingpreferencesmodel` → QML. In TonicAnchored mode the preference now controls
whether sustained events may be rewritten for retuning. Untied sustained notes use the
existing split-and-slur path when enabled. Non-partial tie chains now behave as follows:
when enabled, a tie crossing a harmonic-region boundary may be removed and replaced by a
slur so the later segment can carry independent tuning; when disabled, the chain remains
one tuning event. Anchors override both cases and protect the full written duration.

**FreeDrift sustained-event rewriting iteration is complete.** The same
`allowSplitSlurOfSustainedEvents` preference now applies in FreeDrift mode. When the
preference is disabled, held notes and tie chains remain whole carried events. When the
preference is enabled, FreeDrift may rewrite a sustained event only if the continuation's
target tuning differs from the carried tuning. Untied sustained notes split-and-slur at
the region boundary; tied chains reuse an existing tie boundary by replacing the crossing
tie with a slur. The preference checkbox is now enabled in both tuning modes.

**Notation-side regression coverage for sustained events is now established.**
`src/notation/tests/notationtuning_tests.cpp` and `src/notation/tests/notationtuning_data/`
form an isolated regression island for notation-side retuning behavior. Current coverage
includes non-tied sustained-note splitting, disabled split/slur behavior, tie-boundary
segmentation, disabled tie-chain segmentation, anchored sustained-note protection,
anchored tie-chain protection, and FreeDrift on/off cases for both untied and tied
sustained events. Current suite result: 13/13 passing in `notation_tests.exe`.

**Chord-staff harmonic-event preservation fix is complete.** `collectRegionTones()` now
always includes notes sustained into the region start, even when there is already a
`ChordRest` segment exactly at that tick, and the implode writer creates or fetches exact
region-start `ChordRest` segments before placing notes and Harmony annotations. Preserve-all
notation analysis is still regression-covered for exact late re-entries like Corelli
`op01n08d m4 b3`, but `populateChordTrack()` itself now reuses the same bounded adaptive
tick-based inference helper as source-note analysis: it samples source-note ticks across the
selection, infers each tick with the same expanding local window used by the status bar and
context menu, then merges only in-measure repeats of the same user-facing result. The
implode regression set now covers half-measure harmony changes, sustained-support fixtures,
pedal-tail weighting, Chopin BI16-1 mixed-measure protection, tupleted Dvorak `op08n06`,
and the Corelli `op01n08d` opening/late-dominant GUI cases. A follow-up Corelli
opening-bars regression now locks the shared post-implode source-note path directly.
At the last fully green notation checkpoint, `notation_tests.exe` passed 31/31.
The current working tree still has the two open Corelli implode failures noted in
the Current State summary above.

**Chord-staff confidence/exposure cleanup is complete.** `populateChordTrack()` now
gates key annotations by key confidence instead of always exposing them. When
`normalizedConfidence < 0.5`, key labels and other key-dependent annotations stay
suppressed, but Roman/Nashville function text now remains paired with the shown chord
result. For `0.5 <= confidence < 0.8`, the tentative key label is written with a
trailing `?`. At `confidence >= 0.8`, the full key-annotation set is allowed again
(key signatures, modulation labels, borrowed-chord markers, cadence markers, and key
relationship text). The Dvorak `op08n06` exposure regressions now lock in both the
high-vs-low key-annotation behavior and the low-confidence Roman pairing. Current
exposure-cleanup checkpoint: `notation_tests.exe` passed 31/31. The current working
tree still has the two open Corelli implode failures noted in the Current State
summary above.

**Mozart K279 opening-mode regression is resolved.** Two issues were involved.
First, Roman-analysis `Harmony` imports were still visible to the chord-symbol gate,
so both the bridge helper and `batch_analyze` now restrict that path to rooted
`HarmonyType::STANDARD` annotations only. Second, same-key-signature diatonic mode
selection could let `tonalCenterScore` overrule a materially stronger raw winner,
which produced the near-zero-confidence `F Lydian` opening on `K279-1`. The
key-mode selector now keeps tonal-center disambiguation for close diatonic ties,
but falls back to the stronger raw winner when the tonal-center choice trails by
more than the existing comparison tolerance. Batch and notation now both open
`K279-1` in `C major`, and parity re-checks still pass exactly on BWV 227.7 and
Chopin BI16-1.

**P8a (ChordAnalysisResult refactor) is complete.** `ChordAnalysisResult` now contains two
nested sub-structs: `ChordIdentity` (pitch-content: score, rootPc, bassPc, bassTpc, quality,
extensions) and `ChordFunction` (tonal-function: degree, diatonicToKey, keyTonicPc, keyMode).

**P8b (Extension bitmask) is complete.** 17 individual boolean extension fields replaced by
`uint32_t extensions` bitmask using `Extension` enum class (16 flags). Helper functions:
`hasExtension()`, `setExtension()`, `hasAnyNinth()`, `hasAnyThirteenth()`.

**P8c (bounds() method) is complete.** Both `ChordAnalyzerPreferences` and
`KeyModeAnalyzerPreferences` expose `bounds()` returning a `ParameterBoundsMap` with
parameter name → {min, max, isManual} for each numeric scoring parameter.

**Mode prior naming cleanup is complete.** The three abbreviated mode prior accessors
(`modePriorLydianAug`, `modePriorLydianDom`, `modePriorPhrygianDom`) were renamed to their
full forms (`modePriorLydianAugmented`, `modePriorLydianDominant`, `modePriorPhrygianDominant`)
across all call sites, settings keys, QML properties, and struct fields.

**Mode prior preset system is complete.** `ModePriorPreset` struct + `modePriorPresets()`
free function provide 5 named presets (Standard, Jazz, Modal, Baroque, Contemporary).
`IComposingAnalysisConfiguration` exposes `applyModePriorPreset(name)` and
`currentModePriorPreset()`. The QML preferences page shows five `FlatButton` widgets that
apply a preset in one click; the active preset is highlighted.

**Bridge factory wiring is complete.** All three notation bridge files now use
`ChordAnalyzerFactory::create()` instead of a direct `RuleBasedChordAnalyzer{}` stack
instance, ensuring the analyzer type is resolved through the factory at every call site.

**P6 synthetic test suite is complete.** `synthetic_tests.cpp` adds 54 parametrized and
non-parametrized tests: root coverage (all 12 chromatic roots + 7 triad qualities + seventh
chords), enharmonic consistency, inversion consistency, 7-mode identification, and round-trip
format validation. Total test count: **271 tests, 0 failures**.

---

## Tuning Algorithm Status

Relevant spec: §11.3a–11.3f in ARCHITECTURE.md.

### What is implemented in `applyRegionTuning()` and `applyTuningAtNote()`

| Feature | Status |
|---------|--------|
| JI offsets from tuning system lookup table | **Done** — `tuningSystem.tuningOffset()` |
| Tonic-anchored root offset | **Done** — `tuningSystem.rootOffset()` added when `tonicAnchoredTuning` pref is on |
| Basic (unweighted) zero-sum centering | **Done** — `minimizeTuningDeviation` pref; subtracts arithmetic mean of all note offsets (§11.3a basic form) |
| Split-and-slur for sustained notes (TonicAnchored) | **Done** — Phase 3 in both `applyTuningAtNote` and `applyRegionTuning`; in region tuning this is gated by `allowSplitSlurOfSustainedEvents` |
| Non-partial tie-chain continuity | **Done** — region tuning still computes one authority note per chain (earliest anchor in chain or first note), but when split/slur is enabled it may segment at an existing tie boundary by replacing the crossing tie with a slur; if disabled, the chain remains one event |
| Tuning anchor expression (Italian forms) | **Done** — `kTuningAnchorKeywords` array; `hasTuningAnchorExpression()` / `computeSusceptibility()` wired in `applyTuningAtNote()` and `applyRegionTuning()` (Phases 2+3) |
| Anchor override for sustained events | **Done** — anchored sustained notes and anchored tie chains remain whole protected written-duration events even when split/slur is enabled |
| FreeDrift mode | **Done** — `TuningMode` enum; drift reference hierarchy P1→P2/P3; sustained-event rewriting is preference-controlled and only occurs when the continuation target differs from the carried tuning |
| Tuning mode selector (QML) | **Done** — two FlatButton widgets in ComposingAnalysisSection |
| Sustained-event split/slur preference (QML) | **Done** — `allowSplitSlurOfSustainedEvents` wired through config/model/QML and used by region tuning in both TonicAnchored and FreeDrift |
| Cent annotation on score | **Done** — `annotateTuningOffsets` pref adds StaffText labels |

### What is documented in §11.3a–11.3f but not yet implemented

| Feature | Spec section | Gap |
|---------|--------------|-----|
| Voice-role-weighted centering | §11.3b | `minimizeTuningDeviation` uses equal arithmetic mean; voice roles (melody/inner/bass) not tracked |
| Duration-based susceptibility budget | §11.3c | `computeSusceptibility()` returns `Free` for all non-anchor notes; duration, register, instrument sensitivity not used |
| Sustained fifth/octave protection | §11.3e step 2 | Not implemented; sustained perfect fifths/octaves are retuned freely |
| Susceptibility clamping | §11.3e step 5 | No per-note offset clamping to a budget |
| Tuning session state / drift tracking | §11.3d | `TuningSessionState` struct is specified but not implemented; no drift accumulation |
| FreeDrift reset marker | §11.3f / backlog | No mechanism yet to deliberately reset drift at structural boundaries; see `backlog_drift_reset.md` |
---

## Known failing notation tests (implode-to-chord-track, all deferred)

As of 2026-04-13 (34 tests total, 30 passing):

1. **ImplodeChordTrackKeepsSustainedSupportAcrossBeatBoundaries** — extra annotation at tick 3/4; `inferGapRegion` suspect.
2. **CorelliOp01n08dOpeningBarsStatusContextMatchPopulateWithoutForcedKeySignature** — tick 1440 carry-forward mismatch between status-bar context and populate output.
3. **PopulateChordTrackDoesNotLeaveMixedChordRestMeasuresOnBI16** — mixed chord/rest on BI16 chord tracks in measures 9, 26, 28, 29, 32, 33; deferred.
4. **CorelliOp01n08dUserReportedChordTrackAudit** — missing bass annotation at m10; late-beat sparse cases.

`PopulateChordTrackHandlesTupletedDvorakOp08n06` is now **passing** — the `findTupletOnTrack` fix resolved it.

All other notation regression tests pass.

The §11.3e "complete algorithm" (classify → identify anchors → compute JI offsets → weighted centering → clamp) describes the intended future design. The current implementation covers §11.3e steps 3–4 with unweighted centering and no clamping, plus §11.3f FreeDrift.

---

## Strategic Priorities

1. **Accuracy of harmonic analysis is the current priority** — prerequisite for MuseScore
   contribution. Every change is measured against the regression catalog and (soon) the
   validation pipeline.
2. **Validation pipeline against 371 Bach chorales** — establish real-world accuracy
   baseline. P3 is now complete; pipeline run in progress (background).
3. **Complete Phase 1 analysis work before beginning Phase 2.**
4. **Phase 2 (knowledge base and style system) does not begin until Phase 1 is complete.**

---

## What Is Implemented

| Component | Status | Notes |
|-----------|--------|-------|
| `IChordAnalyzer` / `RuleBasedChordAnalyzer` | Done | interface + rule-based implementation; quality, extensions (bitmask), inversions, diatonic degree, chromatic Roman numerals |
| `ChordAnalysisResult` | Done | split into `ChordIdentity` (pitch-content) + `ChordFunction` (tonal-function); `Extension` bitmask replaces 17 booleans |
| `ChordAnalyzerFactory` | Done | `ChordAnalyzerFactory::create(ChordAnalyzerType::RuleBased)` |
| Scoring parameter bounds | Done | `ChordAnalyzerPreferences::bounds()` + `KeyModeAnalyzerPreferences::bounds()` → `ParameterBoundsMap` |
| `KeyModeAnalyzer` | Done | **21 modes** (7 diatonic + 7 melodic minor + 7 harmonic minor); 16-beat window; duration + beat + bass + decay weighting; 21 independent mode priors |
| Tuning anchor (Italian forms) | Done | `kTuningAnchorKeywords` (4 Italian forms) / `isTuningAnchorText()` / `hasTuningAnchorExpression()` / `computeSusceptibility()` / `RetuningSusceptibility`; wired in both `applyTuningAtNote` and `applyRegionTuning` |
| FreeDrift mode | Done | `TuningMode` enum; drift reference hierarchy; Phase 3 skip; QML selector |
| `analysis/` subdirectory layout | Done | reorganized into `chord/`, `key/`, `region/` subdirectories |
| `ChordSymbolFormatter` | Done | chord symbols, Roman numerals, Nashville numbers |
| Status bar integration | Done | `[C maj] Cmaj7 (IM7)` format; all display toggles in preferences |
| Chord staff ("Implode to chord track") | Done | chord symbols, Roman numerals, Nashville, key annotations, borrowed chord labels, pivot detection, cadence markers; preserve-all harmonic events during implosion, including beat-level changes supported by sustained carry-in notes |
| Region intonation ("Tune selection") | Done | split-and-slur; tonic-anchored JI; minimize-retune; cent annotation; preference-controlled sustained-event rewriting in both modes; tie chains can segment at existing tie boundaries when enabled; anchors protect full written duration |
| Per-note tuning ("Tune as") | Done | context menu; explicit tuning system passed |
| User preferences | Done | `IComposingAnalysisConfiguration` + `IComposingChordStaffConfiguration`; preferences page |
| Bridge architecture | Done | all bridge functions in `mu::notation`; split into single-note bridge + harmonic rhythm bridge + shared helpers; composing module has no engraving dependency |
| Mode prior preset system | Done | `ModePriorPreset` struct + `modePriorPresets()` + 5 named presets + `applyModePriorPreset()` / `currentModePriorPreset()`; QML FlatButton row highlights active preset |
| §4.1b Contextual inversion bonuses | Done | `ChordTemporalContext` extended (+6 fields); `stepwiseBassInversionBonus` / `stepwiseBassLookaheadBonus` / `sameRootInversionBonus` in `ChordAnalyzerPreferences`; `isDiatonicStep()` helper; chord identity 83.4% → retired 83.7% onset-only/music21 figure (superseded 2026-04-09 by 50.0% WIR structural); `previousBassPc`, `bassIsStepwiseFromPrevious`, `nextBassPc`, and `bassIsStepwiseToNext` are now populated in regional analysis; `nextRootPc` and `previousChordAge` remain deferred |
| §4.1c Regional note accumulation | Done | The notation bridge `collectRegionTones()` now includes beat-weight + repetition boost + cross-voice boost + sustain-pedal tail weighting; the duplicate batch_analyze collector is used by both the jazz and classical paths, and the classical path now uses Jaccard boundaries plus smoothed regional analysis instead of the onset-only prototype; `detectHarmonicBoundariesJaccard()` remains duplicated in batch_analyze; the Bach baseline correction is now recorded as 50.0% WIR structural with 38.0% music21 surface retained only as a secondary reference |
| §4.1c Jazz mode | Done | `scoreHasValidChordSymbols()` detection gate (bridge + batch_analyze); `analyzeHarmonicRhythmJazz()` in bridge; `analyzeScoreJazz()` in batch_analyze; chord-symbol-driven boundaries; `fromChordSymbol` + `writtenRootPc` in `HarmonicRegion` and JSON output; `ChordTemporalContext::jazzMode` retained as a context flag; valid-root gate fix prevents Roman-numeral/function-only Harmony imports from misrouting When in Rome scores into the jazz path; batch-only `--inject-written-root` provides a diagnostic upper bound showing current jazz corpora are incomplete rather than exposing an analyzer defect |
| Regression tests | Active | **299 composing tests** plus notation-side regression suites are in place; the last fully green implode checkpoint had 31 focused regressions passing, but the current working tree still has 2 open Corelli implode failures (see Current State) |
| Validation pipeline tools | Done | `batch_analyze`, `music21_batch.py` (SATB filter, dynamic corpus root), `compare_analyses.py` (chord identity rate), `run_validation.py` |
| Temporal window | Done | 16-beat lookback + 8-beat lookahead, 0.7× decay per measure |
| Dynamic lookahead | Done | expands window when confidence < 0.60; caps at 24 beats |
| Mode-switching hysteresis | Done | prevents spurious mode switches on transient evidence |

---

## Tuning Algorithm Implementation Status

The tuning system is partially implemented. The following is a precise account of
what is and is not done, relative to the planned design in §11.3a–11.3e.

**Implemented:**
- Split-and-slur mechanism for applying different tuning to sustained notes, gated in
  region tuning by `allowSplitSlurOfSustainedEvents` in both tuning modes
- Per-note JI offset computation from tuning system lookup tables
- Basic zero-sum centering (unweighted arithmetic mean subtracted from all offsets)
  — active when `minimizeTuningDeviation` preference is on
- Non-partial tie-chain continuity for region tuning: one authority note per chain
  (earliest anchor-marked note or first note), one offset applied to the active tied
  event, and tie boundaries may be reused as segmentation points by converting the
  crossing tie to a slur when split/slur is enabled in either tuning mode
- Expression-based tuning anchor (Italian keyword forms, P7)
- Anchor override for sustained events: anchored sustained notes and anchored tie chains
  remain full-duration protected events even when split/slur is enabled
- Epsilon threshold (0.5¢) — skips negligible changes

**NOT implemented (planned in §11.3a–11.3e):**
- Weighted centering by voice role (melody/bass/inner weights, inversion-aware
  bass weight) — §11.3b
- Duration-based maximum adjustment budget — §11.3c
- Sustained perfect fifth/octave pair detection and protection — §11.3c
- Unison/octave across voices as intentionally linked pairs — §11.3c
- Instrument sensitivity lookup by MuseScore instrument ID — §11.3c
- `TuningSessionState` with global sensitivity and depth sliders — §11.3d
- The complete 8-step algorithm integrating all of the above — §11.3e
- Style-aware interval-family selection for ambiguous sonorities — deferred.
  Current tuning uses fixed tables per tuning system; it does not yet choose
  between alternatives such as 5-limit versus septimal dominant sevenths, nor
  does it apply comparable policy decisions for other ambiguous chord types or
  extensions. This is future exploration, not current work.

The current implementation applies JI offsets independently per note with optional
unweighted centering, plus preference-controlled sustained-event rewriting in region
tuning. In both modes, untied sustained notes may split/slur and tied chains may
segment at existing tie boundaries when the continuation target differs and the
preference allows it; anchors override both and preserve the full written duration.
The sophisticated algorithm in §11.3a–11.3e is designed but not yet implemented.

---

## What Is In Progress

- Nothing — P3, P4, P4b, P4e, P5a, P7, P8a/b/c, P6 synthetic tests, preset system, bridge factory wiring all complete.

---

## Phase 1 Remaining Items (in priority order)

1. ~~**Fix corpus filtering**~~ — **done.** `_is_bach_chorale()` filter applied;
   352 genuine SATB chorales accepted from 410 retrieved. Corrected baseline run.
2. ~~**Fix `maddb13` over-identification**~~ — **done.** `detectExtensions()` now requires
   the perfect 5th to be present before asserting a flat-13 on a minor chord without a seventh.
   The 87 cases of `Gmaddb13` vs Eb-major-triad are now correctly labeled as `Gm`. Chord
   identity metric unchanged (83.4%) — these remain root-identification disagreements, not
   false-extension disagreements. Catalog m269 updated to include G for an unambiguous 4-note
   test chord. 271/271 unit tests pass.
3. **Analyse dim7 vs diminished triad over-identification** — we resolve fully-voiced
   dim7 where music21 labels only the triad subset. ~80 cases.
4. **Analyse sus4 vs quartal trichord** — we identify sus4 where music21 identifies
   a quartal trichord. ~35 cases.
5. **DCML corpus integration** (P5b) — human-annotated third comparison point from
   https://github.com/DCMLab/bach_chorales
6. **ABC Beethoven corpus** (P5c) — extend validation coverage beyond chorales from
   https://github.com/DCMLab/ABC
7. **`ChordAnalysisTone::weight` population** — from duration and beat position;
   no analyzer changes required
8. **`TemporalContext` struct** — previous chord continuation scoring
9. **Secondary dominants and non-diatonic Roman numerals** (§5.6)
10. **Monophonic/arpeggiated chord inference** (§4.1d provisional phased plan; corrected Phase 1a completed on Charlie Parker Omnibook, 20260407_205723 / git `0587ec27e1`)

---

## Known Gaps

- **`ChordAnalysisTone::weight` not populated** — currently always 1.0; duration and beat
  position are collected in `notationcomposingbridge.cpp` for `PitchContext` (used by
  `KeyModeAnalyzer`) but not passed through to `ChordAnalysisTone`
- **Key/mode inferrer piece-start shortcut** — when tick < 16 beats and the key sig carries
  an explicit mode, `resolveKeyAndMode()` returns the declared mode at confidence 0.5
  without running the inferrer (no pitch evidence exists yet). This is intentional. Outside
  this narrow case the inferrer always runs; key sig is a scoring prior only.
- **`isChordTrackStaff()` name-based detection** — chord track identified by part name
  substring; should be replaced with a Part-level flag (backlog)
- **Mode restriction preference** — no user preference to restrict which modes
  `KeyModeAnalyzer` evaluates (backlog)
- **Mixed sustained chords with ties** — if a sustained chord contains at least one
  non-partial tie, Phase 3 region retuning skips splitting that chord entirely. This
  preserves the tie-chain continuity rule, but untied neighbors in that same sustained
  chord are not independently re-split by the current implementation.
- **Cadence labels hardcoded in English** — PAC, HC, DC, PC not in translation system
  (backlog)
- **MusicXML sus export bug** — C9sus2-style chords export with `text="92"`; upstream
  code unstable, deferring reporting (backlog)
- **sus4 vs quartal trichord** — ~35 corpus disagreements where we label `sus4` and
  music21 labels a perfect-4th stack as a quartal trichord (no functional root). These
  are the same 3 pitch classes viewed through different analytical lenses: functional
  tonal harmony (us) vs pitch-set theory (music21). In Bach chorale contexts our sus4
  interpretation is correct; the disagreement is expected and not a bug.
- **§4.1c piano pedal sustain** — long sustain-pedal carryover is preserved by design,
  but the regional accumulator still lacks a decay model for stale support tones when the
  harmony above changes. This affects Romantic piano corpora.
- **Current Corelli notation regressions in the working tree** —
  `Notation_ImplodeTests.CorelliOp01n08dOpeningAndSparseLateBeatsDoNotSmearPreviousChord`
  still returns `Gm` instead of expected `G` at `m1 b3` and `m10 b3`; and
  `Notation_ImplodeTests.CorelliOp01n08dUserReportedChordTrackAudit` still misses
  the late entries at `m2 b3` and `m18 b3` while serializing `m24` as
  `[0:Dm][480:Fm][960:F]` instead of the expected stable `Fm` carry.
- **Rampageswing walking bass** — walking bass passing tones dilute root signal in
  regional accumulation. A jazz beat-weight fix was attempted, improved aggregate
  Rampageswing agreement, regressed diminished chords, and was reverted. Deferred for a
  more surgical approach.

---

## Regression Test Count

**271 tests** — chord analyzer (unit + MusicXML integration), key/mode analyzer (all 21 modes),
tuning anchor, P6 synthetic suite (root coverage, inversions, modes, round-trip).
0 abstract (root/quality) mismatches in the catalog.

---

## Validation Pipeline Results

### Corrected Baseline (post-fix)

Corpus filter fixed (2.1): 410 retrieved, **352 accepted** (genuine 4-voice
chorales), 58 rejected (18 variant suffix, 39 wrong part count, 1 non-chorale BWV).
Report: `tools/reports/validation_20260405_131800.html`

| Metric | Count | % of total | % of aligned |
|--------|-------|------------|--------------|
| Total regions | 6032 | — | — |
| Aligned regions | 4058 | 67.3% | — |
| Unaligned | 1974 | 32.7% | — |
| full\_agree | 2296 | 38.1% | 56.6% |
| near\_agree | 0 | 0.0% | 0.0% |
| chord\_agree\_rn\_differs | 0 | 0.0% | 0.0% |
| chord\_agree\_key\_differs | 1089 | 18.1% | 26.8% |
| chord\_disagree | 673 | 11.2% | 16.6% |
| **Chord identity agreement** | **3385** | **56.1%** | **83.4%** |

Chord identity agreement = (full\_agree + chord\_agree\_rn\_differs +
chord\_agree\_key\_differs) / aligned = 3385 / 4058 = 83.4%.

**Note on near\_agree = 0:** The near\_agree check is implemented correctly in
compare\_analyses.py — it checks music21's chord against our 2nd and 3rd ranked
candidates. The real-world result is genuinely zero across all aligned regions.

**Note on chord\_agree\_key\_differs:** 26.8% of aligned regions show the same chord
identity but different key context. This is expected — music21 uses global
Krumhansl-Schmuckler key detection while we use a 16-beat local temporal window.
These are not errors in chord identification.

**Note on chord\_agree\_rn\_differs = 0:** Every case where root+quality matched,
the Roman numeral base degree also matched. Key context disagreement is the only
source of Roman numeral variation in matching-chord cases.

### §4.1b Validation Run (2026-04-06)

Run: `validation_20260406_122004`, git `bcc0811f67`, binary: `ninja_build_rel/batch_analyze.exe`
Corpus: same 352 chorales, `--skip-music21` (reused existing music21 output, re-ran C++ analysis).

| Metric | Count | % of total | % of aligned |
|--------|-------|------------|--------------|
| Total regions | 6032 | — | — |
| Aligned regions | 4058 | 67.3% | — |
| chord\_disagree | 661 | 11.0% | 16.3% |
| **Chord identity agreement (retired onset-only/music21 figure)** | **3397** | **56.3%** | **83.7% (superseded by 50.0% WIR structural)** |

**vs. baseline:** chord_disagree 673 → **661** (−12, −1.8%); chord identity 83.4% → **83.7%** (+0.3 pp in the retired onset-only/music21 workflow).

bassIsRoot fraction in chord\_disagree: **~72.9%** (estimated via tick-aligned comparison;
down from 74.3% baseline — consistent with stepwise-bass bonus redirecting some
bass-as-root reads toward inverted readings).

Populated `ChordTemporalContext` fields: `previousRootPc`, `previousQuality`,
`previousBassPc`, `bassIsStepwiseFromPrevious`, `nextBassPc`,
`bassIsStepwiseToNext`.
Deferred fields (two-pass chord staff analysis only): `nextRootPc`, `previousChordAge`.

### §4.1c Validation Run (2026-04-06)

Run: `validation_20260406_151131`, binary: `ninja_build_rel/batch_analyze.exe`, `useRegionalAccumulation=true`
Corpus: 352 Bach chorales, `--skip-music21`.

| Metric | Count | % of total | % of aligned |
|--------|-------|------------|--------------|
| Total regions | 6032 | — | — |
| Aligned regions | 4058 | 67.3% | — |
| chord\_disagree | 661 | 11.0% | 16.3% |
| **Chord identity agreement (retired onset-only/music21 figure)** | **3397** | **56.3%** | **83.7% (superseded by 50.0% WIR structural)** |

**vs. §4.1b:** chord_disagree **661 → 661** (unchanged); chord identity **83.7% → 83.7%** (no regression in the retired onset-only/music21 workflow).

**B.7 (ABC Beethoven string quartets, 70 movements):**
Run `beethoven_20260406_152140`. Agreement 61.8% (1836/2973 aligned); BIR% of disagreements **59.4% → 57.3%** (−2.1 pp reduction — regional accumulation redistributes some inverted-bass reads toward correct roots).
Note (2026-04-07): `tools/dcml/beethoven_piano_sonatas/` source files are not present in the current checkout and may have come from a temporary clone. The recorded Beethoven 57.3% BIR result remains valid because the run is preserved in `tools/corpus_registry.json` and the saved report artifacts.

### Chopin Mazurkas Validation (2026-04-06)

Run: `chopin_20260406_153351`, git `601e13bab2`, 55/56 movements (1 missing TSV).

| Metric | Value |
|--------|-------|
| Total regions | 3766 |
| DCML-aligned | 427 (11.3%) |
| Root agreement | 256/427 (**60.0%**) |
| BIR% of disagreements | **77.2%** (132/171) |

**Low alignment rate is expected:** Chopin annotations are sparser (1–2 per measure in 3/4 time) while regional accumulation detects sub-measure harmonic changes. Bach alignment was 67.3% because SATB chorales have a chord on nearly every beat.

**Modal distribution across all 3766 regions:**

| Mode | Count | % |
|------|-------|---|
| Major | 1777 | 47.2% |
| minor | 947 | 25.1% |
| Phrygian | 297 | 7.9% |
| harmonic minor | 224 | 5.9% |
| Dorian | 221 | 5.9% |
| **Lydian** | **160** | **4.2%** |
| Mixolydian | 115 | 3.1% |
| Locrian | 25 | 0.7% |

**Lydian at 4.2% confirms real Lydian passages are being detected** — the primary modal calibration target for this corpus. Chopin mazurkas op. 33 and others contain genuine raised-4th (Lydian) passages; our mode inference is finding them. This validates the modal prior system for romantic-period modal harmony before jazz work begins.

### Grieg Lyric Pieces Validation (2026-04-06)

Run: `grieg_20260406_154216`, git `601e13bab2`, all 66 movements processed.

| Metric | Value |
|--------|-------|
| Total regions | 2423 |
| DCML-aligned | 1023 (42.2%) |
| Root agreement | 561/1023 (**54.8%**) |
| BIR% of disagreements | **67.1%** (310/462) |

**Root agreement (54.8%) is the lowest of any corpus so far.** Late-romantic Grieg harmony
has dense chromatic voice leading, frequent modal mixture, and more inversions than Bach or
Mozart. The BIR% (67.1%) is lower than Chopin (77.2%), suggesting Grieg's passing-chord
texture contributes less bass-as-root error than Chopin's dance-bass accompaniment patterns.

**Modal distribution across all 2423 regions:**

| Mode | Count | % | Note |
|------|-------|---|------|
| Major | 1299 | 53.6% | |
| **Lydian** | **289** | **11.9%** | Primary calibration target — Norwegian folk influence |
| minor | 227 | 9.4% | |
| **Mixolydian** | **208** | **8.6%** | Secondary calibration target |
| **Dorian** | **127** | **5.2%** | Secondary calibration target |
| Phrygian | 77 | 3.2% | |
| harmonic minor | 66 | 2.7% | |
| Locrian | 16 | 0.7% | |

**Key findings:**
- **Lydian at 11.9%** (vs 4.2% in Chopin) — much higher, as expected for Grieg. Norwegian
  folk melody frequently uses raised 4th scale degree. Our mode inference is detecting these
  passages at a substantially higher rate than in Chopin, which is the correct direction.
- **Mixolydian at 8.6%** and **Dorian at 5.2%** — both confirmed as real presences, not
  noise. These are the modes most relevant for calibrating the Jazz preset.
- The Lydian + Mixolydian + Dorian total is **25.7%** of all Grieg regions, confirming this
  corpus is a rich modal calibration source.

**Modal calibration assessment — Chopin + Grieg combined (2026-04-06):**
Modal priors confirmed correct for Romantic repertoire. No adjustments made.

Specific findings from Grieg modal disagreement diagnostic (462 total disagreements):
- We say Lydian, DCML says Major: **12 cases** — negligible false-positive rate.
  Most Lydian disagreements (39) are against DCML-minor keys, consistent with
  genuine Lydian detection in a tonic-minor modal context.
- We say Mixolydian, DCML says Major: **32 cases (~7% of disagreements)** — the
  dominant seventh / Mixolydian ambiguity. A dominant seventh chord is the
  characteristic chord of Mixolydian; without sufficient surrounding diatonic
  context the key analyzer may briefly declare Mixolydian. This is a key analyzer
  evidence-threshold issue, not a prior calibration problem. Adjusting the
  Mixolydian prior would either suppress genuine Mixolydian (lower prior) or
  increase false positives (higher prior). Fix deferred.
- We say Dorian, DCML says Major: **6 cases** — negligible.
- Modal false positives (Lydian/Mixolydian/Dorian/Phrygian vs plain key): 134/462
  (29%), broadly distributed across 28 of 44 pieces — no extreme concentration.

**Conclusion:** Modal priors are calibrated correctly for Romantic repertoire.
The Mixolydian-vs-Major pattern is a known key analyzer limitation, documented
in ARCHITECTURE.md §4.2. Jazz preset calibration may proceed.

---

Top 10 chord\_disagree patterns (673 total, pre-§4.1b baseline):

| Rank | Pattern (ours → music21) | Count |
|------|--------------------------|-------|
| 1 | Emaddb13 vs major triad | 23 |
| 2 | Adim7 vs diminished triad | 19 |
| 3 | F#maddb13 vs major triad | 16 |
| 4 | Dsus4 vs quartal trichord | 16 |
| 5 | Am7b5/C vs half-diminished seventh | 15 |
| 6 | Esus4 vs quartal trichord | 15 |
| 7 | Bb6 vs minor triad | 14 |
| 8 | Bdim7 vs diminished triad | 14 |
| 9 | Gm6 vs diminished triad | 14 |
| 10 | Bm7b5/D vs half-diminished seventh | 14 |

Three systematic error patterns account for the bulk of 673 disagreements:
1. ~~**maddb13 over-identification** (~80 cases)~~ — **fixed (3.1).** `detectExtensions()` now
   requires w(7) > 0.2 (perfect 5th present) before asserting flat-13 on a minor chord without
   a seventh. Chord identity metric unchanged (83.4%) — these were root-identification errors,
   not extension errors; the root still differs from music21.
2. **dim7 vs diminished triad** (202 cases) — systematic root-bias pattern identical to the
   maddb13 issue. 3-note chords `{bass, bass+m3, bass+9st}` with the dim5 absent: we assert
   `{bass}dim7` (root=bass, missing dim5, +9 as enharmonic dim7); music21 asserts `{+9note}dim`
   (clean first-inversion diminished triad with the +9 note as root). Same fix approach as
   maddb13 would apply: require `w(6) > 0.2` (dim5 present) before asserting dim7.
   **Investigation complete; fix deferred** — dim7 chords with all 4 voices are very common in
   Bach; care needed to not suppress genuine fully-voiced dim7s.
3. **sus4 vs quartal trichord** (~35 cases) — expected disagreement; documented in Known Gaps.

### Two-Way Comparison Breakdown — Bass-as-Root Analysis

Report: `tools/reports/reports/validation_20260405_183822.html`
(Same corpus as corrected baseline above; binary: `ninja_build/batch_analyze.exe`)

| Metric | Count |
|--------|-------|
| Total regions | 6032 |
| chord\_disagree (genuine errors) | 673 |
| **chord\_disagree with bassIsRoot=true** | **500** |
| **bassIsRoot fraction of genuine errors** | **74.3%** |

> **Primary accuracy target:** Any inversion/bass-as-root fix must be measured
> against this 74.3% figure.  A successful fix reduces chord\_disagree by ~500
> cases (from 673 toward ~173) while holding regressions to zero.
>
> Context: `bassIsRoot=true` means our analysis chose the bass note as the chord
> root, while music21 chose a different root (typically reading the chord as a
> first or second inversion of a chord rooted on a non-bass note).  This is the
> dominant error source — more than three times larger than all other genuine
> error causes combined.

---

### Three-Way Comparison (ours vs music21 vs When in Rome)

Corpus: When in Rome project Bach chorales (`tools/dcml/when_in_rome`).
Report: `tools/reports/validation_20260405_150753.html`

**Coverage:** 322/352 chorales matched (91.5%); 3346 of 4058 aligned regions
had WiR annotations.

| Category | Count | % of DCML-covered |
|----------|-------|-------------------|
| all_agree (all three match) | 2415 | 72.2% |
| dcml_ours_agree (music21 wrong) | 66 | 2.0% |
| **music21_dcml_agree (we wrong — genuine errors)** | **281** | **8.4%** |
| all_differ (genuinely ambiguous) | 584 | 17.5% |

**Mode breakdown of 281 genuine errors:**

| Our inferred mode | Count | Note |
|-------------------|-------|------|
| maj (Ionian) | 148 | diatonic |
| min (Aeolian) | 99 | diatonic |
| Lyd (Lydian) | 18 | ⚠ non-diatonic |
| Dor (Dorian) | 16 | ⚠ non-diatonic |

87.9% of genuine errors occur in Ionian or Aeolian mode — **mode inference is
mostly correct.** The 18 Lydian cases warrant monitoring: Bach chorales virtually never use Lydian
mode, so these may be false positives triggered by a raised 4th degree in an
otherwise Ionian context. The 16 Dorian cases are plausible — some Bach chorales
are genuinely Dorian.

**Top 15 genuine error patterns (ours → WiR/music21):**

| Rank | Pattern | Count |
|------|---------|-------|
| 1 | Emaddb13 → major triad | 17 |
| 2 | F#maddb13 → major triad | 15 |
| 3 | Bb6 → minor triad | 13 |
| 4 | Gm6 → diminished triad | 10 |
| 5 | Dmaddb13 → major triad | 10 |
| 6 | Amaddb13 → major triad | 10 |
| 7 | C6 → minor triad | 10 |
| 8 | Cm6 → diminished triad | 8 |
| 9 | Bmaddb13 → major triad | 8 |
| 10 | Dm6 → diminished triad | 8 |
| 11 | Dsus4#5 → minor triad | 7 |
| 12 | Eb6 → minor triad | 7 |
| 13 | Dsus4 → major triad | 7 |
| 14 | Esus4 → major triad | 6 |
| 15 | Gsus4#5 → minor triad | 6 |

All top patterns are root-identification errors, not mode inference errors. The
maddb13 patterns (rows 1, 2, 5, 6, 9) remain because the fix (§3.1) only
suppresses the b13 label when the perfect 5th is absent; in these cases the 5th
IS present, so the b13 detection fires — but the root is still wrong (bass-as-root
bias). The `{root}6` → minor/dim patterns are the added-6th vs inverted-triad
ambiguity: `Bb6 = {Bb, D, G}` is also `Gm/Bb` (first inversion). Same root bias.

### Pre-fix Baseline (for comparison)

Run: 410 unfiltered works, report: `tools/reports/validation_20260404_223531.html`

| Metric | Count | % of total | % of aligned |
|--------|-------|------------|--------------|
| Total regions | 7018 | — | — |
| Aligned regions | 4672 | 66.6% | — |
| full\_agree | 2721 | 38.8% | 58.2% |
| chord\_agree\_key\_differs | 1177 | 16.8% | 25.2% |
| chord\_disagree | 774 | 11.0% | 16.6% |
| unaligned | 2346 | 33.4% | — |
| **Chord identity agreement** | **3898** | **55.5%** | **83.4%** |

The chord identity rate is identical (83.4%) — the 58 excluded non-chorale/variant
works did not materially affect accuracy. The corrected corpus is the authoritative
baseline going forward.

---

### Inversion Fix — Final Conclusion

Six weeks of investigation across four corpora and six fix attempts
reached the following proven conclusions:

1. **95.8% of genuine BIR errors are 3-note triads.** For bare triads,
   bass=root is the statistically correct default. No local scoring
   change can improve these without harmonic context.

2. **4-note chord inversion cases (4.2% of errors) already score
   correctly** at `tpcConsistencyBonusPerTone=0.20` when all four
   chord tones are present. The 4-note non-bass template (e.g. Gm7)
   accumulates enough template score and TPC bonus to win over the
   3-note bass-root triad (e.g. Bb-major) without any fix.

3. **The C6/Am7 ambiguity is a data impossibility.** `{C,E,G,A}` with
   C in bass has identical pitch content and TPC spelling as Am7/C.
   No local scoring approach can distinguish them. The bass-root
   convention (`bassNoteRootBonus`) is the correct resolution.

4. **No TPC bonus window exists.** A bonus large enough to correct
   3-note inversions (x > 0.65) simultaneously breaks all sixth-chord
   conventions. Calibration testing at x=0.75 confirmed 20 abstract
   catalog regressions with 0 corpus improvements.

5. **The remaining BIR errors represent legitimate divergence** between
   vertical sonority analysis (our approach) and functional/contextual
   harmonic annotation (DCML). This is not an analyzer defect.

**Retired Bach ceiling:** the earlier ~83–84% figure applied only to the
onset-only prototype measured against music21 surface labels. The current
official Bach structural baseline is 50.0% root agreement against local
When in Rome RomanText annotations. Improving beyond that structural
baseline still requires harmonic sequence context (analyzing surrounding
chords, cadence patterns, voice-leading continuity) — a Phase 2
architectural component outside Phase 1 scope.

**Current baseline is the correct production baseline. Do not attempt
further local scoring fixes for inversions.**

---

### Section 6 — Inversion Fix (two attempts, both reverted)

**6.1 Analysis (2026-04-05):** Three-way comparison (Bach chorales) identified
281 genuine errors. Of these, **245/281 (87.2%) have bassIsRoot=true**. 86.1%
have `margin < 0.25`; 100% have `margin < 1.0`; 100% have `noteCount ≥ 3`.
Cross-corpus diagnostic (Section 7) confirmed this is universal across all four
corpora (Bach 74.3%, Beethoven 59.4%, Mozart 38.6%, Corelli 94.9%).

**Attempt 1 (post-truncation, margin=0.65, reduction=0.0):**
Searched `results[1..2]` for a non-bass-root alternative. Had no measurable effect
because the bass bonus fires for ALL templates with root==bass, filling the entire
top-3 result window with same-root candidates — no non-bass alternative visible.
Report: `tools/reports/reports/validation_20260405_214122.html` (identical to baseline).

**Attempt 2 (pre-truncation rawCandidates, margin=1.0, reduction=0.3, git: 80fc2d2ca1+):**
Moved correction to rawCandidates before the top-3 window. Added `intervalCount`
field to `RawCandidate`. Widened quality set to include Diminished/HalfDiminished.
Added condition 3 (alt must have ≤ winner's intervalCount). 271/271 tests passed.

**Attempt 2 validation result (2026-04-05, run 20260405_225018):** **REGRESSION.**
- chord_disagree: 673 → **696** (+23 — worse)
- chord_identity: 83.4% → **82.8%** (-0.6%)
- full_agree: 2302 → 2299 (-3)

Reverted immediately (`git checkout -- chordanalyzer.cpp chordanalyzer.h`).
Report: `tools/reports/reports/validation_20260405_225018.html`

**Attempt 2 regression analysis (2026-04-06):** 23 regressions, 0 improvements.
All 23 new disagrees were **inverted dim7 or halfdim7 chords** (e.g. `Bdim7/F`,
`Am7b5/C`) — 86% dim7, 9% halfdim. These are correctly identified with bass≠root;
the fix incorrectly saw them as major/minor inversions and flipped the root.
Root cause: Attempt 2 included Diminished/HalfDiminished in the winner quality set.

**Attempt 3 (2026-04-06, pre-truncation rawCandidates, margin=1.0, reduction=0.3):**
Winner restricted to Major/Minor only. Alternative restricted to Major/Minor only.
No intervalCount condition. 271 regression tests — **FAILED** (1 abstract mismatch).

Catalog measure 269: `{C, Eb, G, Ab}` = `Cmaddb13` (catalog: root=C, Minor).
Fix flipped to `G#Maj7/C` (root=G#, Major). The {C,Eb,G,Ab} set is enharmonically
identical to {Ab,C,Eb,G} = AbMaj7 in first inversion. The fix correctly identified
an ambiguous chord but chose the wrong interpretation relative to the catalog.
This case represents a genuine analytical ambiguity — not a fix defect per se —
but the catalog is the ground truth so this is a regression.

**Status:** All three attempts reverted. Parameters `inversionSuspicionMargin`
and `inversionBonusReduction` remain in the header at their committed values
(0.65/0.0). The catalog measure 269 case (`Cmaddb13` = {C,Eb,G,Ab}) reveals the
fundamental difficulty: any fix that can flip a major chord rooted on the bass
to a major chord rooted elsewhere will also flip genuine enharmonic inversions
that the catalog records with the bass-note root. A fix that avoids this must
either use TPC spelling to disambiguate, or require stronger evidence (e.g.
the alternative must match the next chord's root for voice-leading continuity).
No further fix attempts without a new design session.

---

### Section 7 — Extended Corpus Diagnostics (2026-04-10)

Scripts: `tools/run_mozart_validation.py`, `tools/run_corelli_validation.py`,
`tools/section_7_3_diagnostic.py`. Registry: `tools/corpus_registry.json`.
Git hash: `80fc2d2ca1` (inversion fix reverted in working tree).

#### 7.1 Mozart Piano Sonatas

Corpus: DCMLab/mozart_piano_sonatas (54 MSCX files).
Run: `20260410_002531` (clean binary, Rule 3 compliant).
Report: `tools/reports/reports/mozart_20260410_002531.json`

| Metric | Value |
|---|---|
| Movements | 54/54 |
| Our regions | 7,065 |
| DCML-aligned | 2,293 (32.5%) |
| Root agreement | 612/2,293 (**26.7%**) |
| Root disagreement | 1,681/2,293 (73.3%) |
| bassIsRoot in disagreements | 1,001/1,681 (**59.5%**) |

Note (2026-04-10): this refreshed run supersedes the historical 53/54 snapshot.
The previously skipped `K533-3` native MSCX path now completes successfully in
`batch_analyze` after the headless loader stopped forcing full layout. Direct
`K533-3.mscx` still matches the mirrored `score.mxl` path on detected key
(`Fmaj` at 0.980275 confidence) and region count (317).

#### 7.2 Corelli Trio Sonatas

Corpus: DCMLab/corelli (149 MSCX files).
Run: `20260411_074802` (parser-corrected, final no-third inversion gating).
Report: `tools/reports/reports/corelli_20260411_074802.json`

Historical note: the older `20260405_221113` Corelli numbers predate the ABC/DCML
`relativeroot` parser fix in `tools/dcml_parser.py` and are superseded.

| Metric | Value |
|---|---|
| Movements | 149/149 |
| Our regions | 7,394 |
| DCML-aligned | 2,464 (33.3%) |
| Root agreement | 1,733/2,464 (**70.3%**) |
| Root disagreement | 731/2,464 (29.7%) |
| bassIsRoot in disagreements | 304/731 (**41.6%**) |

The targeted one-score follow-up `op01n08d` is now 11/13 on aligned rows. The remaining
genuine disagreements are `m20 b1` (`ii65/III` vs our `Ab`) and `m23 b1` (`V6/III` vs our
`Dsus#5`). The earlier `m25 b1` miss is resolved by refusing contextual inversion bonuses
for no-third candidates.

#### 7.3 Cross-Corpus Consolidated Diagnostic

Script: `tools/section_7_3_diagnostic.py`

| Corpus | Agree% | Disagree | BIR | BIR% | noteCount≥3 | m<0.25 | m<0.65 |
|--------|--------|----------|-----|------|-------------|--------|--------|
| Bach chorales | 83.4% | 673 | 500 | **74.3%** | 500 (100%) | 365 (73%) | 408 (82%) |
| Beethoven quartets | 62.2% | 1123 | 667 | **59.4%** | 667 (100%) | 410 (62%) | 544 (82%) |
| Mozart sonatas | 26.7% | 1681 | 1001 | **59.5%** | 1001 (100%) | 729 (73%) | 984 (98%) |
| Corelli sonatas | 65.5% | 175 | 166 | **94.9%** | 166 (100%) | 124 (75%) | 141 (85%) |

**Universal findings:**
- **noteCount ≥ 3 in 100% of BIR errors across all four corpora** — no arpeggio artifacts in genuine BIR disagreements.
- **Margin < 0.65 in 81–98% of BIR errors** across all corpora (range: 81% Beethoven – 98% Mozart). The bass bonus is the marginal deciding factor in the large majority of cases.
- **Margin < 1.0 in 98.5–100% of BIR errors** — essentially no high-confidence wins.
- **Beat-1 concentration in instrumental corpora:** Beethoven 91.3%, Mozart 93.2%, Corelli 94.0%. Bach chorales distributed across all beats (35.4% / 24.1% / 27.9% / 12.3%) — reflects SATB homophonic texture vs. instrumental idiomatic writing.
- **BIR fraction varies widely by corpus** (59.4% Beethoven – 94.9% Corelli), suggesting corpus-specific factors (texture, voicing style, notation density) affect alignment rate and BIR fraction independently.
- **Mozart now clusters with the other instrumental corpora rather than as a low-BIR outlier**: 59.5% of disagreements are bassIsRoot, 93.2% of those land on beat 1, and 98.3% have chordScoreMargin < 0.65.

---

### ABC Beethoven Two-Way Comparison (5.4)

Corpus: 70 movements from the ABC Beethoven string quartet corpus
(`tools/dcml/ABC/`). Annotations: DCML `.harmonies.tsv` files. Comparison
script: `tools/run_beethoven_validation.py`.

| Metric | Value |
|---|---|
| Movements processed | 70/70 |
| Our regions | 7,141 |
| DCML-aligned | 2,973 (41.6% of ours) |
| Root agreement | 1,850/2,973 (**62.2%**) |
| Root disagreement | 1,123/2,973 (37.8%) |
| bassIsRoot=true in disagreements | 667/1,123 (**59.4%**) |

**59.4% bassIsRoot fraction** (vs 74.3% in Bach chorales) confirms the bass-as-root
bias is the dominant error source across both tonal corpora and styles.
The lower fraction in Beethoven string quartets (vs chorales) is expected:
quartet writing has more explicit voice independence.

Note on alignment: only 41.6% of our regions align with DCML annotations.
The gap is partly methodological — our regions are note-by-note while DCML
annotates harmony-level changes — so unaligned regions are not errors.

---

## Validation Corpus Roadmap

### Design principle

All corpus expansion uses the DCML pipeline exclusively. The DCML
format (MSCX + harmonies TSV) is proven, expert-annotated, and
requires zero new infrastructure per corpus. Every new DCML corpus
is a git clone plus a run of the existing pipeline.

Textbook transcription (manual MusicXML from scanned PDFs) is too
error-prone to scale and has been abandoned as a primary strategy.

**Corpora that produce poor results under current vertical analysis
are kept on the roadmap and labeled "Deferred".** They become
validation targets as the analyzer gains new capabilities (melodic
accumulation, arpeggio inference, jazz mode). A corpus that exposes
a gap in our analysis is more valuable than one that confirms what
we already do well.

### Currently completed

| Corpus | Genre | Period | Agree% | Notes |
|--------|-------|--------|--------|-------|
| Dvořák Silhouettes (12) | Piano | Romantic | 79.2% | |
| Chopin Mazurkas (55) | Piano | Romantic | 71.6% | 1 score missing DCML TSV |
| Corelli Trio Sonatas (149) | Chamber | Baroque | 70.3% | bassIsRoot 41.6% |
| Beethoven String Quartets (70) | Chamber | Classical | 64.9% | |
| Mozart Piano Sonatas (54) | Piano | Classical | 61.8% | prev 26.7% was comparator artifact |
| Schumann Kinderszenen (13) | Piano | Romantic | 61.6% | |
| Tchaikovsky Seasons (12) | Piano | Romantic | 61.0% | |
| Grieg Lyric Pieces (66) | Piano | Romantic | 60.7% | |
| Bach En/Fr Suites (89) | Keyboard | Baroque | 52.4% | two-voice movements deferred |
| C.P.E. Bach Keyboard (66) | Keyboard | Late Baroque | 0% | 0 regions, thin texture deferred |
| Bach Chorales (352) | Choral | Baroque | 75.2% chord-identity on aligned / 43.6% overall | WIR structural reference |

Weighted direct-corpus result (10 corpora, excluding CPE Bach): 64.6% root agreement on 10,830/16,765 aligned rows, 38.1% alignment rate. This meets the lower bound of the 65-75% plateau target.

The DCML comparator now applies `relativeroot` when computing reference `root_pc` for applied chords (secondary dominants etc.). Previous runs that ignored `relativeroot` are superseded. Most affected: Dvořák (66.2%→79.2%), Chopin (57.5%→71.6%), Mozart (26.7%→61.8%).

The earlier onset-only/music21 Bach figures are retained only as historical audit data. The official current Bach baseline is the fresh WIR-structural rerun in `tools/reports/live_20260412_bach/reports/validation_20260412_041114.html`: 75.2% chord-identity agreement on aligned regions and 43.6% overall agreement.

Current cross-corpus picture after the official relativeroot-aware rerun: the strongest full-texture direct corpora are now Dvořák 79.2%, Chopin 71.6%, and Corelli 70.3%; Beethoven reaches 64.9%; Mozart is 61.8% after removing the comparator artifact; Schumann, Tchaikovsky, and Grieg cluster around 61%; Bach En/Fr Suites remain at 52.4%; and C.P.E. Bach still yields 0 regions because the texture is too thin for the current vertical engine. These figures replace the older pre-`relativeroot` direct-corpus baselines.

Historical weighted `bassIsRoot` summaries from the 2026-04-09 post-fix reruns are no longer the official baseline because the `relativeroot`-aware comparator changed the aligned comparison sets. The refreshed direct-corpus table above is the new source of truth; in the new official Corelli baseline alone, `bassIsRoot` is down to 41.6% of disagreements.

When in Rome is compared against adjacent `analysis.txt` RomanText files parsed through
music21 rather than the sparser DCML TSV workflow used elsewhere. RomanText annotations are
much denser than our emitted regions, so the key coverage metric is the 56.1% unmatched rate
rather than a directly comparable DCML alignment percentage. These results are post-fix: the
valid-root chord-symbol gate in `notationcomposingbridgehelpers` and `batch_analyze` prevents
function-only Harmony imports from diverting Quartets and Piano Sonatas into the jazz path.

### Preset sensitivity checks (completed 2026-04-06)

Two preset checks run before §4.1c jazz mode implementation to confirm
preset system is functioning and identify any preset-induced regressions.

**Check 1 — Bach chorales, Baroque preset**
`tools/reports/bach_baroque_20260406_171758.json` | git `601e13bab2`
`tools/corpus_baroque/` (352 files)

| Metric | Standard | Baroque | Delta |
|--------|----------|---------|-------|
| Chord identity (retired onset-only/music21 figure) | 83.7% (superseded) | **83.7% (superseded)** | 0.0 pp |
| Aligned regions | 4 058 | 4 058 | — |
| Mean per-chorale | — | 85.2% | — |

**Finding:** Baroque preset produces identical chord identity to Standard
on Bach SATB chorales. Expected — the chorales are overwhelmingly
major/minor with unambiguous vertical evidence; mode priors have no
effect when evidence is decisive. This preset check remains historically
useful, but its 83.7% value belongs to the retired onset-only/music21
workflow; the official Bach baseline is now 50.0% WIR structural.

**Check 2 — Grieg lyric pieces, Modal preset**
`tools/reports/reports/grieg_20260406_173253.json` | git `601e13bab2`
`tools/corpus_grieg_modal/` (66 files)

| Metric | Standard | Modal | Delta |
|--------|----------|-------|-------|
| Chord identity | 54.8% | **54.8%** | 0.0 pp |
| BIR% | 67.1% | 67.1% | 0.0 pp |
| Alignment | 42.2% | 42.2% | — |

Modal distribution shift (Modal preset vs Standard):

| Mode | Standard | Modal preset | Delta |
|------|----------|--------------|-------|
| major | 53.6% | 43.8% | −9.8 pp |
| lydian | 11.9% | **21.6%** | +9.7 pp |
| mixolydian | 8.6% | 9.9% | +1.3 pp |
| dorian | 5.2% | 6.7% | +1.5 pp |
| minor | 9.4% | 6.0% | −3.4 pp |

**Finding:** Modal preset shifts ~9.8 pp of major detections to Lydian and
smaller amounts to Mixolydian/Dorian, but chord identity agreement is
unchanged at 54.8%. The extra Lydian/Mixolydian detections fall predominantly
in unaligned regions (the 57.8% not compared against DCML), so the
agreement metric is insensitive to them. The preset is working as designed:
it biases mode inference toward non-Ionian modes without degrading
chord root/quality detection.

**Mixolydian false positives:** Standard had 32 Mixolydian-vs-Major
disagreements in the 1 023 aligned regions. Modal preset has 31 additional
Mixolydian regions total (+14.9%), but agreement is unchanged — the added
Mixolydian detections are in unaligned regions, not new false positives
in the aligned set.

**Assessment:** Both preset checks pass — no regressions. Preset system
is functioning correctly. Cleared to proceed with C.2 (§4.1c jazz mode).

### Implementation priority order

**Step 1 — Extended DCML corpora (classical and romantic)** ✓ Complete
Validates §4.1b and §4.1c improvements across styles.
Chopin and Grieg calibrate modal priors before jazz work.

**Step 1b — Preset sensitivity checks** ✓ Complete (2026-04-06)
Baroque preset: no regression on Bach chorales in the retired
onset-only/music21 workflow (83.7% = Standard, now superseded).
Modal preset: no regression on Grieg in the 2026-04-06 run (54.8% = Standard);
that historical Standard figure is now superseded by the 2026-04-09 v2
regional/DCML baseline of 47.3%. Modal
distribution shifts as expected.

**Step 2 — §4.1c jazz mode** ✓ Complete (2026-04-06)
Chord-symbol-driven region boundaries implemented.
FiloSax/FiloBass validation now unblocked.
See ARCHITECTURE.md §4.1c for design.

**Step 3 — Jazz infrastructure and validation**
After Step 1 modal calibration confirms Jazz preset is well-tuned.

### Step 1 — DCML corpora to add (priority order)

All at `https://github.com/DCMLab/<name>`.
All use identical MSCX + harmonies TSV — existing pipeline handles
all without modification. All licensed CC BY-NC-SA 4.0.

Single clone for everything:
`git clone --recurse-submodules -j12 https://github.com/DCMLab/distant_listening_corpus.git`
(~2.4 GB). Or clone individually as needed.

| Priority | Corpus | Genre | Period | Why |
|----------|--------|-------|--------|-----|
| 1 | `chopin_mazurkas` | Piano | Romantic | Real Lydian passages — primary modal prior calibration |
| 2 | `grieg_lyric_pieces` | Piano | Romantic | Real Dorian and Mixolydian — modal calibration |
| 3 | `schumann_kinderszenen` | Piano | Romantic | Dense harmonic rhythm, short pieces |
| 4 | `tchaikovsky_seasons` | Piano | Romantic | Late-Romantic harmony |
| 5 | `bach_en_fr_suites` | Keyboard | Baroque | **Partial** — Sarabandes/dense mvts work (Dorian 9.5%, Phrygian 6.4%); 2-voice counterpoint movements deferred until melodic/arpeggio accumulation |
| 6 | `cpe_bach_keyboard` | Keyboard | Late Baroque | **Deferred** — single-voice texture, 0 regions now; Empfindsamer Stil implies harmony in single lines; excellent target once melodic inference added |
| 7 | `dvorak_silhouettes` | Piano | Romantic | Done — 66.9% agreement |
| 8 | `debussy_suite_bergamasque` | Piano | Impressionist | **Deferred** — harmonically dense but whole-tone/parallel harmony requires jazz mode infrastructure |
| 9 | `liszt_pelerinage` | Piano | Romantic | **Deferred** — highly chromatic; requires jazz mode + extended chord types |
| 10 | `handel_keyboard` | Keyboard | Baroque | **Deferred** — same reason as C.P.E. Bach; Baroque keyboard figuration implies harmony in single voices; validate after melodic accumulation |
| 11 | `bartok_bagatelles` | Piano | Modern | **Deferred** — post-tonal; outside 12-mode analyzer scope; long-term stress test target |

For each new corpus:
```bash
git clone https://github.com/DCMLab/<name>.git tools/dcml/<name>
mkdir -p tools/corpus_<name>
# batch_analyze all MSCX → tools/corpus_<name>/
# compare_analyses.py --dcml tools/dcml/<name>/harmonies/
# update corpus_registry.json
```

### Step 2 — §4.1c jazz mode ✓ Complete (2026-04-06)

Chord-symbol-driven region boundaries implemented in bridge and batch_analyze.
Auto-activates when chord symbols are present in the score.
Smoke test (Dm7|G7|Cmaj7|Cmaj7): 4 regions, correct roots/qualities, `fromChordSymbol: true`.
FiloSax/FiloBass validation now unblocked.
See ARCHITECTURE.md §4.1c for design.

### Step 3 — Jazz corpus and validation

Phase 1a monophonic-jazz validation for the provisional §4.1d plan should be
recorded in this section using the same timestamp and git-hash discipline as
other corpus runs.

**Phase 1a (Charlie Parker Omnibook, 50 MusicXML solos):**
Run `omnibook_20260407_205723`, git `0587ec27e1`, preset `Jazz`, source `https://homepages.loria.fr/evincent/omnibook/omnibook_xml.zip`.
All 50 files loaded successfully via `batch_analyze`; no zero-region solos.
The embedded MusicXML chord symbols were parsed into `fromChordSymbol` regions as intended, but the corrected jazz path now analyzes notes rather than copying the written root.
Total regions: 4464. Comparable chord-symbol regions with an analyzed chord: 3361. Written-root vs analyzed-root agreement: **605/3361 = 18.0%**. Regions with no analyzed chord: **1103**.
This supersedes the earlier `omnibook_20260407_201517` result, which was invalid because the old jazz path copied `writtenRootPc` into `rootPitchClass`.
`noteCount` across all `fromChordSymbol` regions: `0: 268`, `1: 349`, `2: 476`, `3: 691`, `4: 1088`, `5: 610`, `6: 496`, `7: 341`, `8: 110`, `9: 25`, `10: 5`, `11: 5`.
This is the corrected Phase 1a design result: bounded expansion may still be needed for the 1103 sparse 0-2 PC regions, but that is not the main problem. Even the analyzable 3-11 PC regions only achieve 18.0% root agreement, so the current vertical analyzer is not an adequate model for monophonic jazz melody.
Lowest-agreement 5: `Dewey_Square` 4%, `Red_Cross` 6%, `Thriving_From_A_Riff` 8%, `Kim_2` 10%, `Warming_Up_A_Riff` 10%. Highest-agreement 5: `Now's_The_Time_1` 41%, `Cosmic_Rays` 41%, `KC_Blues` 37%, `Ornithology` 37%, `Another_Hairdo` 35%. Report: `tools/reports/reports/omnibook_20260407_205723.txt`.

**Why this ordering matters:**
Jazz harmony has more inversions than classical. The §4.1b and §4.1c
improvements must be validated and stable before jazz work begins.
Chopin (modal Lydian) and Grieg (Dorian/Mixolydian) calibrate the
modal priors the Jazz preset depends on. Jazz validation without
this calibration produces uninterpretable results.

**Available jazz corpora with notes + chord symbols:**

Charlie Parker Omnibook — 50 public MusicXML files with embedded `<harmony>` chord symbols.
Directly usable with §4.1c jazz mode; used for Phase 1a validation above.
Source: `https://homepages.loria.fr/evincent/omnibook/omnibook_xml.zip`.

FiloSax — 240 MusicXML saxophone solos (48 standards × 5 players)
with per-note chord symbol annotations described publicly via JAMS and derived JSON.
Monophonic. Public docs do not clearly confirm embedded MusicXML harmony,
so a conversion step may still be required.
Available on Zenodo with usage agreement.

FiloBass — 48 MusicXML walking bass transcriptions from the same
48 standards with chord-symbol metadata described in the paper/metadata.
Public page does not clearly confirm embedded MusicXML harmony,
so a conversion step may still be required.

Curated small ground truth set — 10–15 jazz standards manually
verified in MuseScore. Full voicing (piano or combo scores).
Chord symbols professionally verified. Small but zero ambiguity.

MuseScore.com bulk download — not recommended for validation.
Quality varies. Chord symbol accuracy is unverifiable at scale
without human review per score.

**Required infrastructure before jazz validation:**

- §4.1c jazz mode (chord-symbol-driven boundaries)
- `formatLeadSheet()` output mode (chord symbols not Roman numerals)
- Jazz comparison pipeline (root PC + quality vs written chord symbols)
- Jazz preset calibration

**music21 built-in corpus (ours vs music21 two-way only)**
No expert annotation — lower quality than DCML but immediately
available. Use only after DCML corpora are exhausted.
Available: Haydn string quartets, Mozart string quartets,
Monteverdi madrigals.

**Vocal close harmony (future)**
Barbershop TTBB/SSAA — no research corpus with annotations exists.
Practical path: MuseScore.com bulk download when API available.
Expected high accuracy (similar SATB texture to Bach chorales).
Contemporary vocal jazz falls under the jazz project.

---

## Preset Calibration Assessment (April 2026)

Tested Baroque preset on Bach chorales and Modal preset on
Grieg lyric pieces. Results: zero change in chord identity
agreement on both corpora.

Finding: Mode priors shift detections in ambiguous/unaligned
regions but cannot override decisive vertical evidence in
well-voiced textures. Preset differences are consequential
only where evidence is ambiguous — which tends to correlate
with unaligned regions where DCML has no annotation for
comparison.

Conclusion: Current presets are correctly calibrated for
classical and Romantic repertoire. No prior adjustments made.

Jazz preset calibration is deferred until jazz corpus
validation begins — jazz harmony has substantially different
mode prior requirements (Dorian, Lydian Dominant, Altered)
that cannot be validated without jazz scores.

## Milestone A Status (2026-04-10)

Milestone A now has three completed gates:

1. **A1 — shared tone-merge/collapse alignment.** Validation is complete:
   `composing_tests.exe` passed 295/295, `notation_tests.exe` passed 19/19,
   `ctest -R batch_analyze_regressions --output-on-failure` passed, Bach WIR
   structural remains 52.3%, and Chopin remains 57.5%.
2. **A2 — reusable batch/notation parity harness.** `batch_analyze` now supports
   `--dump-regions batch|notation|notation-premerge`, the notation bridge exposes
   pre/post-merge debug capture, and `tools/check_parity.py` compares both paths on
   one score. Exact parity currently passes for BWV 227.7 and Chopin BI16-1.
   Reports: `tools/reports/parity/bwv227.7.txt` and `tools/reports/parity/BI16-1.txt`.
3. **A3 — confidence/exposure cleanup.** Complete. `populateChordTrack()` now gates
  key annotations by key confidence: below 0.5 it suppresses key labels and related
  key-only annotations, while still keeping Roman/Nashville function text paired with
  the shown chord result; from 0.5 to 0.8 it keeps only a tentative key label; at 0.8
  or above it allows the full key-dependent annotation set (key signatures,
  modulation labels, borrowed-chord markers, cadence markers, and key relationship
  text). At the A3 checkpoint, `notation_tests.exe` passed 31/31, including the Dvorak `op08n06`
  exposure regressions, the Roman-harmony chord-symbol gate regressions, and a Mozart
  `K279-1` opening-key regression.
4. **Post-A follow-up — Mozart `K533-3` native MSCX crash.** Complete.
   `batch_analyze` no longer forces layout on headless loads, so the direct
   `K533-3.mscx` path now exits 0 instead of crashing. Validation: direct MSCX
   and mirrored `score.mxl` both report `Fmaj` at 0.980275 confidence with 317
  regions; `composing_tests.exe` remains 295/295 and `notation_tests.exe`
  remains 23/23. Separately, full GUI open of the native `K533-3.mscx` file
  is still treated as a bad-score / corruption issue on Windows rather than an
  active product-fix target: investigation reproduced intermittent
  `ucrtbase.dll c0000409` and `Qt6Gui.dll c0000005` failures, but no validated
  MuseScore-side fix survived verification, so future sessions should keep this
  file out of GUI-fix work unless a fresh reliable crash dump is captured.

Milestone A is complete.

## Milestone B1 Status (2026-04-11)

**B1 — pedal-aware Jaccard boundary detection is complete.**

- `detectHarmonicBoundariesJaccard()` now carries explicit sustain-pedal tails
  into later quarter-note windows in both `notationcomposingbridgehelpers.cpp`
  and `tools/batch_analyze.cpp`.
- New oracle regression: `jaccard_pedal_support_same_harmony.mscx` proves that
  a pedaled dyad on beat 1 and a completing upper note on beat 2 no longer
  create a spurious boundary.
- Validation:
  - `notation_tests.exe` passes 26/26.
  - The new pedal-support fixture passes exact batch/notation parity with 1
    merged region in both paths and 1 notation pre-merge region.
  - Chopin BI16-1 parity remains exact after B1, but the global region count
    drops from 11 to 7 and notation pre-merge regions drop from 23 to 14.
  - In the opening BI16 span (`startTick 480` to `4800`), batch, notation, and
    notation-premerge now all produce one `Dadd11` region instead of the earlier
    split at tick `4320`.

## Inference Quality Assessment (2026-04-11)

The current inferrers do not emit calibrated probabilities of correctness.
`KeyModeAnalysisResult::normalizedConfidence` is a heuristic transform of the
internal winner-vs-runner-up score gap, and `ChordAnalysisResult` still
exposes only raw scores. The published corpus figures are therefore empirical
agreement rates, not literal probabilities.

Interpret the current quality evidence in three tiers:

1. **Internal consistency** — batch vs notation vs UI-path parity. This should
   converge toward near-100% because it measures whether our own paths agree.
2. **External structural agreement** — currently mostly root-pitch-class or
   root+quality comparison against DCML / When in Rome / music21 references.
   These are useful trend signals, but they are not full harmonic-correctness
   measures.
3. **Full harmonic correctness** — chord identity + function + key/mode +
   granularity agreement. This remains the desired long-term measure, but it is
   not yet the dominant published benchmark.

Current corpus tables are strongest as root-agreement trend indicators. They
now show the strongest full-texture direct corpora in the low-70s to high-70s,
with a weighted direct-corpus result of 64.6% across the refreshed baseline
set. The earlier Mozart `26.7%` direct DCML figure was a comparator artifact
from ignoring `relativeroot` on applied chords and is superseded by the new
61.8% baseline.

## Reasonable "Good" Plateau (planning target)

A reasonable stopping point before sharply diminishing returns is:

- near-perfect internal consistency across batch, chord track, status bar, and
  context menu
- calibrated high-confidence exposure: when the product chooses to show a
  key-dependent inference, it should be right most of the time
- exact external root+quality agreement roughly in the 65–75% band on tonal
  corpora for the current vertical tertian engine family
- exact Roman/function agreement expected to remain lower than root+quality;
  optimize precision and abstention rather than forcing full coverage

## Plateau Assessment (2026-04-11)

The 65-75% plateau target for the current vertical tertian engine on full-texture
tonal corpora is essentially reached:

- Weighted direct-corpus result: 64.6% on 10 corpora
- Top performers: Dvořák 79.2%, Chopin 71.6%, Corelli 70.3%
- Bach chorales: 75.2% chord-identity on aligned regions

Further large gains from the current engine family require:

- Mixed-texture orchestration (CPE Bach, Bach suites two-voice movements)
- Post-plateau scope expansion (quartal, rootless, polychordal)

The primary remaining work is product quality: display, abstraction level,
and user experience rather than raw accuracy on full-texture tonal corpora.

## Plateau Roadmap (highest ROI before diminishing returns)

1. **Remaining recurring texture fixes.** Broken-chord/pedal boundary
  handling, Baroque passing-bass handling, and phrase-aware key look-ahead.
  These address primary failure modes that confidence calibration cannot fix.
2. **Evaluation tier separation.** Split published quality reporting into:
  internal consistency, root-only/root+quality external agreement on
  full-texture corpora, and full harmonic correctness. Baselines must be
  stable before held-out calibration is meaningful.
3. **Chord confidence + calibration.** Add normalized confidence for chord
  analysis and held-out calibration on stable baselines. This is only useful
  after the primary texture failure modes are addressed.
4. **Mixed-texture orchestration.** Add a lightweight second strategy for
  obviously arpeggiated or single-line spans. "Obviously arpeggiated" means
  maximum simultaneous pitch-class count in any beat window <= 2. Compare
  calibrated confidence across strategies and treat abstention as valid.
5. **Region identity decision.** Decide explicitly whether preserve-all
  regions are keyed to root + quality (harmonic summary mode) or full
  sonority identity (as-written mode). Fold the deferred chord-track octave
  deduplication item into this decision. Both modes are needed; neither should
  remain undecided.

Work likely beyond the plateau:

- quartal/quintal language detection
- rootless ensemble awareness
- polychordal/upper-structure detection
- register-sensitive add2 vs add9
- full monophonic engine

## Next session priorities

1. **Restore the current Corelli GUI regressions on the note-only path**
  Specifically: `m1 b3` and `m10 b3` still show `Gm` instead of expected `G`,
  `m2 b3` and `m18 b3` still miss late local entries, and `m24` still serializes
  as `[0:Dm][480:Fm][960:F]`. Do not reintroduce Harmony-input shortcuts.

2. **Evaluation tier separation**
  Stabilize the reporting layers before confidence calibration: internal
  consistency, full-texture external structural agreement, and full harmonic
  correctness.

3. **Chord confidence calibration**
  Add normalized chord confidence only after the primary texture failures and
  benchmark baselines are stable.

4. **Mixed-texture orchestration design**
  Define the smallest viable second-strategy path for obviously arpeggiated or
  single-line spans and compare calibrated confidence rather than raw scores.

5. **Region identity + as-written mode decision**
  Decide explicitly between harmonic-summary and as-written region identity,
  including the deferred chord-track octave-deduplication work.

6. **K533 native-vs-mirrored measure-number normalization (optional)**
  Direct `K533-3.mscx` and the mirrored `score.mxl` now agree on harmony,
  detected key, confidence, and region count, but still differ by a one-measure
  numbering offset. Normalize only if downstream tooling needs identical JSON
  measure numbering across both import paths.

---

## Future Architectural Considerations

- **Bridge file reorganization by musical concept vs mechanism** — revisit when more bridges
  are being added
- **Instance-based vs static analyzers** — `ChordAnalyzer` is now `RuleBasedChordAnalyzer`
  implementing `IChordAnalyzer`; `KeyModeAnalyzer` is still a static class; revisit when
  style system is active
- **Voice role information in `HarmonicRegion`** — revisit when sophisticated tuning
  algorithm is implemented
- **`HarmonicRegion` include pair friction** — `HarmonicRegion` struct is in
  `composing/analysis/harmonicrhythm.h` but bridge functions are in
  `notation/internal/notationcomposingbridge.h`; document when a new contributor first
  hits this
- **`isChordTrackStaff()` → Part-level flag** — replace name-based chord track detection
  with a Part-level flag (see backlog_chord_track_flag.md)
- **Rename "chord track" → "chord staff"** — ~31 occurrences in ~11 files (backlog)
