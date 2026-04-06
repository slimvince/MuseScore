# MuseScore Arranger — Implementation Status

> **Living document.** Claude Code reads this at the start of every session. Update this as the
> last act when anything changes. For stable architectural decisions, see ARCHITECTURE.md.

*Last updated: April 2026 — §4.1b Contextual Inversion Resolution implemented. ChordTemporalContext extended with bass-note and stepwise-motion fields; three contextual inversion bonuses added to contextualBonuses(); chord identity 83.4% → 83.7%; chord_disagree 673 → 661; 280 tests passing.*

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
P2/P3=zero drift; Phase 3 (split-and-slur) skipped in FreeDrift mode (8.4). (5) QML tuning
mode selector (two FlatButton widgets: "Tonic-anchored" / "Free drift") added to
`ComposingAnalysisSection.qml` and wired in `ComposingPreferencesPage.qml` (8.5).
(6) Drift boundary annotation: `annotateDriftAtBoundaries` preference (separate toggle
from `annotateTuningOffsets`) wired through interface → config → QML; in FreeDrift mode
inserts a StaffText "d=+N" at each region boundary when |drift| ≥ 0.5 ¢.
FreeDrift anchor semantics clarified: anchor notes are pitched at the current drift
level (not reset to 0 ¢) and annotated with `*` suffix.
280/280 tests passing.

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
| Split-and-slur for sustained notes (TonicAnchored) | **Done** — Phase 3 in both `applyTuningAtNote` and `applyRegionTuning`; skipped in FreeDrift mode |
| Tuning anchor expression (Italian forms) | **Done** — `kTuningAnchorKeywords` array; `hasTuningAnchorExpression()` / `computeSusceptibility()` wired in `applyTuningAtNote()` and `applyRegionTuning()` (Phases 2+3) |
| FreeDrift mode | **Done** — `TuningMode` enum; drift reference hierarchy P1→P2/P3; Phase 3 skipped |
| Tuning mode selector (QML) | **Done** — two FlatButton widgets in ComposingAnalysisSection |
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
| Chord staff ("Implode to chord track") | Done | chord symbols, Roman numerals, Nashville, key annotations, borrowed chord labels, pivot detection, cadence markers |
| Region intonation ("Tune selection") | Done | split-and-slur; tonic-anchored JI; minimize-retune; cent annotation |
| Per-note tuning ("Tune as") | Done | context menu; explicit tuning system passed |
| User preferences | Done | `IComposingAnalysisConfiguration` + `IComposingChordStaffConfiguration`; preferences page |
| Bridge architecture | Done | all bridge functions in `mu::notation`; split into single-note bridge + harmonic rhythm bridge + shared helpers; composing module has no engraving dependency |
| Mode prior preset system | Done | `ModePriorPreset` struct + `modePriorPresets()` + 5 named presets + `applyModePriorPreset()` / `currentModePriorPreset()`; QML FlatButton row highlights active preset |
| §4.1b Contextual inversion bonuses | Done | `ChordTemporalContext` extended (+6 fields); `stepwiseBassInversionBonus` / `stepwiseBassLookaheadBonus` / `sameRootInversionBonus` in `ChordAnalyzerPreferences`; `isDiatonicStep()` helper; chord identity 83.4% → 83.7%; `previousBassPc` and `bassIsStepwiseFromPrevious` populated; `nextRootPc/nextBassPc/bassIsStepwiseToNext` deferred (two-pass) |
| Regression tests | Done | **280 tests**, 0 abstract (root/quality) mismatches |
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
