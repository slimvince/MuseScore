# MuseScore Arranger — Implementation Status

> **Living document.** Claude Code reads this at the start of every session. Update this as the
> last act when anything changes. For stable architectural decisions, see ARCHITECTURE.md.

*Last updated: April 2026 — Section 1 doc corrections; Section 2 corpus filter + baseline; maddb13 fix (3.1); Section 4 three-way comparison vs When in Rome (72.2% all-agree, 8.4% genuine errors, mode inference mostly correct)*

---

## Current State (summary)

The Phase 1 analysis foundation is implemented and working. The status bar displays chord
symbols, Roman numerals, and key/mode information on every note selection, using a 16-beat
temporal window with time decay. The chord staff ("Implode to chord track") and region
intonation ("Tune selection") are both in the Tools menu.

**P3 (21-mode expansion) is complete.** `KeyModeAnalyzer` now evaluates all 21 modes
(7 diatonic + 7 melodic minor family + 7 harmonic minor family). Mode priors are 21
independent parameters replacing the former 4-tier grouping. The regression catalog has
207 tests with 0 abstract mismatches.

**P4 (interface refactor) is complete.** `analysis::KeyMode` renamed to `KeySigMode`;
`IChordAnalyzer` interface introduced with `RuleBasedChordAnalyzer` implementation;
`notationcomposingbridge.cpp` split into three files with shared helpers extracted.
P4b added `ChordAnalyzerFactory` and documented `ChordTemporalContext` vs future `TemporalContext`.
P4e reorganized `src/composing/analysis/` into subdirectories: `chord/`, `key/`, `region/`.

**P7 (tuning anchor) is complete.** `kTuningAnchorKeyword = "anchor-pitch"` constant and
`isTuningAnchorText()` pure function in `tuning_system.h`; `hasTuningAnchorExpression()` and
`computeSusceptibility()` bridge functions in `notationtuningbridge.cpp`; `RetuningSusceptibility`
enum (AbsolutelyProtected / Adjustable / Free); 10 unit tests all passing.

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

Relevant spec: §11.3a–11.3e in ARCHITECTURE.md.

### What is implemented in `applyRegionTuning()` and `applyTuningAtNote()`

| Feature | Status |
|---------|--------|
| JI offsets from tuning system lookup table | **Done** — `tuningSystem.tuningOffset()` |
| Tonic-anchored root offset | **Done** — `tuningSystem.rootOffset()` added when `tonicAnchoredTuning` pref is on |
| Basic (unweighted) zero-sum centering | **Done** — `minimizeTuningDeviation` pref; subtracts arithmetic mean of all note offsets (§11.3a basic form) |
| Split-and-slur for sustained notes | **Done** — Phase 3 in both `applyTuningAtNote` and `applyRegionTuning` |
| Tuning anchor expression (`anchor-pitch`) | **Done** — `hasTuningAnchorExpression()` / `computeSusceptibility()` wired in `applyTuningAtNote()`; **not wired in `applyRegionTuning()`** |
| Cent annotation on score | **Done** — `annotateTuningOffsets` pref adds StaffText labels |

### What is documented in §11.3a–11.3e but not yet implemented

| Feature | Spec section | Gap |
|---------|--------------|-----|
| Voice-role-weighted centering | §11.3b | `minimizeTuningDeviation` uses equal arithmetic mean; voice roles (melody/inner/bass) not tracked |
| Duration-based susceptibility budget | §11.3c | `computeSusceptibility()` returns `Free` for all non-anchor notes; duration, register, instrument sensitivity not used |
| Tuning anchor protection in region tuning | §11.3c | `applyRegionTuning()` does not call `computeSusceptibility()` or `hasTuningAnchorExpression()` — anchor notes in a region are retuned like any other note |
| Sustained fifth/octave protection | §11.3e step 2 | Not implemented; sustained perfect fifths/octaves are retuned freely |
| Susceptibility clamping | §11.3e step 5 | No per-note offset clamping to a budget |
| Tuning session state / drift tracking | §11.3d | `TuningSessionState` struct is specified but not implemented; no drift accumulation |

The §11.3e "complete algorithm" (classify → identify anchors → compute JI offsets → weighted centering → clamp) describes the intended future design. The current implementation is approximately §11.3e steps 3–4 with unweighted centering and no clamping.

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
| Tuning anchor | Done | `kTuningAnchorKeyword` / `isTuningAnchorText()` / `hasTuningAnchorExpression()` / `computeSusceptibility()` / `RetuningSusceptibility` |
| `analysis/` subdirectory layout | Done | reorganized into `chord/`, `key/`, `region/` subdirectories |
| `ChordSymbolFormatter` | Done | chord symbols, Roman numerals, Nashville numbers |
| Status bar integration | Done | `[C maj] Cmaj7 (IM7)` format; all display toggles in preferences |
| Chord staff ("Implode to chord track") | Done | chord symbols, Roman numerals, Nashville, key annotations, borrowed chord labels, pivot detection, cadence markers |
| Region intonation ("Tune selection") | Done | split-and-slur; tonic-anchored JI; minimize-retune; cent annotation |
| Per-note tuning ("Tune as") | Done | context menu; explicit tuning system passed |
| User preferences | Done | `IComposingAnalysisConfiguration` + `IComposingChordStaffConfiguration`; preferences page |
| Bridge architecture | Done | all bridge functions in `mu::notation`; split into single-note bridge + harmonic rhythm bridge + shared helpers; composing module has no engraving dependency |
| Mode prior preset system | Done | `ModePriorPreset` struct + `modePriorPresets()` + 5 named presets + `applyModePriorPreset()` / `currentModePriorPreset()`; QML FlatButton row highlights active preset |
| Regression tests | Done | **271 tests**, 0 abstract (root/quality) mismatches |
| Validation pipeline tools | Done | `batch_analyze`, `music21_batch.py` (SATB filter, dynamic corpus root), `compare_analyses.py` (chord identity rate), `run_validation.py` |
| Temporal window | Done | 16-beat lookback + 8-beat lookahead, 0.7× decay per measure |
| Dynamic lookahead | Done | expands window when confidence < 0.60; caps at 24 beats |
| Mode-switching hysteresis | Done | prevents spurious mode switches on transient evidence |

---

## Tuning Algorithm Implementation Status

The tuning system is partially implemented. The following is a precise account of
what is and is not done, relative to the planned design in §11.3a–11.3e.

**Implemented:**
- Split-and-slur mechanism for applying different tuning to sustained notes
- Per-note JI offset computation from tuning system lookup tables
- Basic zero-sum centering (unweighted arithmetic mean subtracted from all offsets)
  — active when `minimizeTuningDeviation` preference is on
- Expression-based tuning anchor (`anchor-pitch` keyword, P7)
- Epsilon threshold (0.5¢) — skips negligible changes

**NOT implemented (planned in §11.3a–11.3e):**
- Weighted centering by voice role (melody/bass/inner weights, inversion-aware
  bass weight) — §11.3b
- Duration-based maximum adjustment budget — §11.3c
- Tied note protection (`tieBack != nullptr` check) — §11.3c
- Sustained perfect fifth/octave pair detection and protection — §11.3c
- Unison/octave across voices as intentionally linked pairs — §11.3c
- Instrument sensitivity lookup by MuseScore instrument ID — §11.3c
- `TuningSessionState` with global sensitivity and depth sliders — §11.3d
- The complete 8-step algorithm integrating all of the above — §11.3e

The current implementation applies JI offsets independently per note with optional
unweighted centering. The sophisticated algorithm in §11.3a–11.3e is designed but
not yet implemented.

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
10. **Monophonic/arpeggiated chord inference** (§5.5)

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

Top 10 chord\_disagree patterns (673 total):

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

## Future Validation Improvements

- Expert review of validation pipeline failure modes — possibly part of beta test
- Textbook gold-standard cases — deferred until validation pipeline reveals weak areas
- Statistical confidence calibration — plot confidence vs actual agreement rate with DCML
- Temporal consistency testing — adding context should not reverse root identification
- Internal consistency validation — ChordAnalyzer and KeyModeAnalyzer outputs should not contradict each other
- Edge case stress tests: diminished seventh ambiguity, augmented triad ambiguity, pedal points, cross-staff notation
- Comparison against Melisma or other academic harmonic analysis systems
- User correction logging as validation data (beta test phase)

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
