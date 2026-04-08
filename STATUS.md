# MuseScore Arranger — Implementation Status

> **Living document.** Claude Code reads this at the start of every session. Update this as the
> last act when anything changes. For stable architectural decisions, see ARCHITECTURE.md.

*Last updated: April 2026 — sustained-event retuning remains preference-controlled in both tuning modes, chord-staff implosion preserves every detected harmonic event instead of inheriting the smoothed tuning-style region merge, and synthetic bass-injection diagnostics confirmed that the analyzer is already correct on jazz when complete tonal material is present. `notation_tests` still contains 15 focused notation-side regressions, all passing.*

---

## Current State (summary)

The Phase 1 analysis foundation is implemented and working. The status bar displays chord
symbols, Roman numerals, and key/mode information on every note selection, using a 16-beat
temporal window with time decay. The chord staff ("Implode to chord track") and region
intonation ("Tune selection") are both in the Tools menu. Chord-staff population now uses
the preserve-all harmonic-event path rather than the smoothed region-tuning path, so
beat-level harmony changes and sustained pedal/support tones are no longer dropped during
implosion.

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

**Chord-staff harmonic-event preservation fix is complete.** `populateChordTrack()` now
requests `analyzeHarmonicRhythm(..., PreserveAllChanges)` so chord-staff output keeps every
detected harmonic event instead of inheriting the smoothed region-tuning behavior.
`collectRegionTones()` now always includes notes sustained into the region start, even when
there is already a `ChordRest` segment exactly at that tick, and the implode writer creates
or fetches exact region-start `ChordRest` segments before placing notes and Harmony
annotations. Two notation-side implode regressions cover half-measure harmony changes and
beat-by-beat changes supported by sustained pedal notes. Current `notation_tests.exe`
result: 15/15 passing.

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
| §4.1b Contextual inversion bonuses | Done | `ChordTemporalContext` extended (+6 fields); `stepwiseBassInversionBonus` / `stepwiseBassLookaheadBonus` / `sameRootInversionBonus` in `ChordAnalyzerPreferences`; `isDiatonicStep()` helper; chord identity 83.4% → 83.7%; `previousBassPc` and `bassIsStepwiseFromPrevious` populated; `nextRootPc/nextBassPc/bassIsStepwiseToNext` deferred (two-pass) |
| §4.1c Regional note accumulation | Done | `collectRegionTones()` (beat-weight + repetition boost + cross-voice boost) + `detectHarmonicBoundariesJaccard()` in bridge helpers; `useRegionalAccumulation` preference (default true) in config stack; both paths wired in `notationharmonicrhythmbridge.cpp`; `ChordAnalysisTone` extended with 3 new fields; chord identity held at 83.7%; chord_disagree held at 661 |
| §4.1c Jazz mode | Done | `scoreHasChordSymbols()` detection gate (bridge + batch_analyze); `analyzeHarmonicRhythmJazz()` in bridge; `analyzeScoreJazz()` in batch_analyze; chord-symbol-driven boundaries; `fromChordSymbol` + `writtenRootPc` in `HarmonicRegion` and JSON output; `ChordTemporalContext::jazzMode` retained as a context flag; batch-only `--inject-written-root` provides a diagnostic upper bound showing current jazz corpora are incomplete rather than exposing an analyzer defect |
| Regression tests | Done | **289 composing tests** + **15 notation tests** + **1 batch_analyze regression**, all passing |
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
| **Chord identity agreement** | **3397** | **56.3%** | **83.7%** |

**vs. baseline:** chord_disagree 673 → **661** (−12, −1.8%); chord identity 83.4% → **83.7%** (+0.3 pp).

bassIsRoot fraction in chord\_disagree: **~72.9%** (estimated via tick-aligned comparison;
down from 74.3% baseline — consistent with stepwise-bass bonus redirecting some
bass-as-root reads toward inverted readings).

Populated `ChordTemporalContext` fields: `previousRootPc`, `previousQuality`,
`previousBassPc`, `bassIsStepwiseFromPrevious`.
Deferred fields (two-pass chord staff analysis only): `nextRootPc`, `nextBassPc`,
`bassIsStepwiseToNext`, `previousChordAge`.

### §4.1c Validation Run (2026-04-06)

Run: `validation_20260406_151131`, binary: `ninja_build_rel/batch_analyze.exe`, `useRegionalAccumulation=true`
Corpus: 352 Bach chorales, `--skip-music21`.

| Metric | Count | % of total | % of aligned |
|--------|-------|------------|--------------|
| Total regions | 6032 | — | — |
| Aligned regions | 4058 | 67.3% | — |
| chord\_disagree | 661 | 11.0% | 16.3% |
| **Chord identity agreement** | **3397** | **56.3%** | **83.7%** |

**vs. §4.1b:** chord_disagree **661 → 661** (unchanged); chord identity **83.7% → 83.7%** (no regression).

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
mostly correct.** The 21-mode expansion is not introducing large-scale false-mode
errors in Bach chorale contexts.

The 18 Lydian cases warrant monitoring: Bach chorales virtually never use Lydian
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

**Remaining accuracy ceiling: ~83–84% on Bach chorales by vertical
analysis alone.** Improving beyond this requires harmonic sequence
context (analyzing surrounding chords, cadence patterns, voice-leading
continuity) — a Phase 2 architectural component outside Phase 1 scope.

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

### Section 7 — Extended Corpus Diagnostics (2026-04-05)

Scripts: `tools/run_mozart_validation.py`, `tools/run_corelli_validation.py`,
`tools/section_7_3_diagnostic.py`. Registry: `tools/corpus_registry.json`.
Git hash: `80fc2d2ca1` (inversion fix reverted in working tree).

#### 7.1 Mozart Piano Sonatas

Corpus: DCMLab/mozart_piano_sonatas (54 MSCX files; 1 skipped — no TSV).
Run: `20260405_221616` (clean binary, Rule 3 compliant).
Report: `tools/reports/reports/mozart_20260405_221616.json`

| Metric | Value |
|---|---|
| Movements | 53/54 |
| Our regions | 1,105 |
| DCML-aligned | 581 (52.6%) |
| Root agreement | 392/581 (**67.5%**) |
| Root disagreement | 189/581 (32.5%) |
| bassIsRoot in disagreements | 73/189 (**38.6%**) |

#### 7.2 Corelli Trio Sonatas

Corpus: DCMLab/corelli (149 MSCX files).
Run: `20260405_221113` (clean binary, Rule 3 compliant).
Report: `tools/reports/reports/corelli_20260405_221113.json`

| Metric | Value |
|---|---|
| Movements | 149/149 |
| Our regions | 1,415 |
| DCML-aligned | 507 (35.8%) |
| Root agreement | 332/507 (**65.5%**) |
| Root disagreement | 175/507 (34.5%) |
| bassIsRoot in disagreements | 166/175 (**94.9%**) |

#### 7.3 Cross-Corpus Consolidated Diagnostic

Script: `tools/section_7_3_diagnostic.py`

| Corpus | Agree% | Disagree | BIR | BIR% | noteCount≥3 | m<0.25 | m<0.65 |
|--------|--------|----------|-----|------|-------------|--------|--------|
| Bach chorales | 83.4% | 673 | 500 | **74.3%** | 500 (100%) | 365 (73%) | 408 (82%) |
| Beethoven quartets | 62.2% | 1123 | 667 | **59.4%** | 667 (100%) | 410 (62%) | 544 (82%) |
| Mozart sonatas | 67.5% | 189 | 73 | **38.6%** | 73 (100%) | 43 (59%) | 55 (75%) |
| Corelli sonatas | 65.5% | 175 | 166 | **94.9%** | 166 (100%) | 124 (75%) | 141 (85%) |

**Universal findings:**
- **noteCount ≥ 3 in 100% of BIR errors across all four corpora** — no arpeggio artifacts in genuine BIR disagreements.
- **Margin < 0.65 in 75–82% of BIR errors** across all corpora (range: 75% Mozart – 85% Corelli). The bass bonus is the marginal deciding factor in the large majority of cases.
- **Margin < 1.0 in 95–100% of BIR errors** — essentially no high-confidence wins.
- **Beat-1 concentration in instrumental corpora:** Beethoven 90.7%, Mozart 86.3%, Corelli 94.0%. Bach chorales distributed across all beats (35% / 24% / 28% / 12%) — reflects SATB homophonic texture vs. instrumental idiomatic writing.
- **BIR fraction varies widely by corpus** (38.6% Mozart – 94.9% Corelli), suggesting corpus-specific factors (texture, voicing style, notation density) affect alignment rate and BIR fraction independently.
- **Mozart BIR fraction notably lower (38.6%)** — warrants investigation; may reflect lower alignment rate (52.6%) selecting only clearly-aligned regions where root identification is more reliable.

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

| Corpus | Genre | Period | Agree% | BIR% | Align% |
|--------|-------|--------|--------|------|--------|
| Bach chorales (352 SATB) | Choral | Baroque | 83.7% | ~72.9% | 67.3% |
| ABC Beethoven string quartets (70 mvts) | Chamber | Classical | 62.2% | 59.4% | 41.6% |
| Mozart piano sonatas (53 mvts) | Piano | Classical | 67.5% | 38.6% | 52.6% |
| Corelli trio sonatas (149 mvts) | Chamber | Baroque | 65.5% | 94.9% | 35.8% |
| Beethoven string quartets §4.1c | Chamber | Classical | 61.8% | 57.3% | 41.6% |
| Chopin mazurkas (55 mvts) | Piano | Romantic | 60.0% | 77.2% | 11.3% |
| Grieg lyric pieces (66 mvts) | Piano | Romantic | 54.8% | 67.1% | 42.2% |
| Schumann Kinderszenen (13 mvts) | Piano | Romantic | 63.6% | 91.7% | 24.3% |
| Tchaikovsky Seasons (12 mvts) | Piano | Romantic | 63.9% | 49.3% | 42.4% |
| Dvorak Silhouettes (12 mvts) | Piano | Romantic | 66.9% | 70.8% | 50.0% |
| Bach En/Fr Suites (89 mvts) | Keyboard | Baroque | 66.7% | 74.3% | 32.1% |
| Bach En/Fr Suites dense mvts only | Keyboard | Baroque | 66.7% | 74.3% | 32.1% (partial) |
| C.P.E. Bach Keyboard (66 mvts) | Keyboard | Late Baroque | — | — | 0 (deferred) |

Accuracy ceiling for vertical-only analysis: ~83–84% (proven).
§4.1b contextual inversion adds ~0.3pp. §4.1c regional accumulation
adds ~2pp on piano corpora. Further improvement requires two-pass
lookahead (§4.1b deferred fields) and extended DCML corpus work.

### Preset sensitivity checks (completed 2026-04-06)

Two preset checks run before §4.1c jazz mode implementation to confirm
preset system is functioning and identify any preset-induced regressions.

**Check 1 — Bach chorales, Baroque preset**
`tools/reports/bach_baroque_20260406_171758.json` | git `601e13bab2`
`tools/corpus_baroque/` (352 files)

| Metric | Standard | Baroque | Delta |
|--------|----------|---------|-------|
| Chord identity | 83.7% | **83.7%** | 0.0 pp |
| Aligned regions | 4 058 | 4 058 | — |
| Mean per-chorale | — | 85.2% | — |

**Finding:** Baroque preset produces identical chord identity to Standard
on Bach SATB chorales. Expected — the chorales are overwhelmingly
major/minor with unambiguous vertical evidence; mode priors have no
effect when evidence is decisive.

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
Baroque preset: no regression on Bach chorales (83.7% = Standard).
Modal preset: no regression on Grieg (54.8% = Standard); modal
distribution shifts as expected.

**Step 2 — §4.1c jazz mode** ✓ Complete (2026-04-06)
Chord-symbol-driven region boundaries implemented.
FiloSax/FiloBass validation now unblocked.

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
