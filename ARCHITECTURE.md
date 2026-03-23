# MuseScore Arranger — Architecture Document

> **Living document.** Update this file whenever an architectural decision changes.
> Claude Code should read this document at the start of every development session
> involving new components or integration work. For focused tasks on well-understood
> components, reading the relevant section is sufficient.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Architectural Principles](#2-architectural-principles)
3. [Directory Structure](#3-directory-structure)
4. [Existing Components — The Analysis Foundation](#4-existing-components--the-analysis-foundation)
5. [Planned Analysis Extensions](#5-planned-analysis-extensions)
6. [The Style System](#6-the-style-system)
7. [The Knowledge Base](#7-the-knowledge-base)
8. [Planned Generation Components](#8-planned-generation-components)
9. [The Constraint System](#9-the-constraint-system)
10. [Visualization](#10-visualization)
11. [Intonation](#11-intonation)
12. [User Interface](#12-user-interface)
13. [File Persistence](#13-file-persistence)
14. [ML Readiness](#14-ml-readiness)
15. [Development Phases](#15-development-phases)
16. [Scope Reference](#16-scope-reference)
17. [Coding Standards](#17-coding-standards)
18. [Contributing](#18-contributing)

---

## 1. Project Overview

### 1.1 Vision and Purpose

MuseScore Arranger is a harmonic analysis and arranging assistance system integrated
directly into MuseScore Studio's C++ core. It helps composers, arrangers, and musicians
working across the western music tradition by:

- Analyzing harmony, key, and mode in existing scores
- Suggesting chord voicings and progressions
- Assisting with voice leading optimization
- Supporting multiple musical styles from baroque to contemporary
- Providing intonation guidance for performed music

The primary users are musically literate MuseScore Studio users — arrangers, composers,
and musicians with some theoretical knowledge — ranging from students to professionals.

### 1.2 Relationship to MuseScore Studio

This system is implemented as a new module (`composing`) within MuseScore Studio's
existing C++ codebase. It is not a plugin. It integrates directly with MuseScore's
score model, rendering pipeline, playback engine, and UI infrastructure.

The long-term intent is for this to become an official contribution to MuseScore Studio.
All code follows MuseScore's coding standards, licensing requirements, and contribution
guidelines.

### 1.3 Licensing

All code is licensed under **GPL v3** — consistent with MuseScore Studio's open source
license. All external libraries used must be GPL v3 compatible.

The Contributor License Agreement (CLA) with MuseScore must be signed before any
pull requests are submitted.

### 1.4 Current Status

The following components exist and are working:

- **ChordAnalyzer** — identifies chord quality, extensions, inversions, and diatonic
  degree from a set of simultaneously sounding notes
- **KeyModeAnalyzer** — infers the most likely key and mode from a temporal window
  of pitch contexts
- **ChordSymbolFormatter** — formats analysis results as chord symbols and Roman numerals
- **Status bar integration** — displays chord and key information when a note is selected
- **Regression tests** — cover the chord and key/mode analyzers

The system is currently integrated via `NotationAccessibility::singleElementAccessibilityInfo()`
which appends chord and key information to the accessibility string displayed in the
status bar when a single note is selected.

---

## 2. Architectural Principles

These principles apply to every line of code in this project. Claude Code should
treat them as hard constraints, not guidelines.

### 2.1 Style Behavior Is Fully Data-Driven

The C++ implementation contains no conditional logic based on style identity. All
behavioral differences between musical styles are expressed as parameter values in
style JSON files. Adding, renaming, or modifying a style never requires C++ code changes.

```cpp
// WRONG — never do this
if (style.id == "jazz_vocal") {
    applyJazzVocalSpecialCase();
}

// CORRECT — behavior driven by parameters
if (style.voicing.leadVoicePosition == LeadVoicePosition::SecondFromTop) {
    applyLeadVoiceLogic();
}
```

### 2.2 Interface-Based Design for ML Substitutability

Every component that may eventually be replaced or augmented by a machine learning
model must be defined behind a pure abstract interface. The rest of the system
depends only on the interface, never on a specific implementation.

```cpp
// Every major analytical and generative component follows this pattern
class IHarmonizer {
public:
    virtual ~IHarmonizer() = default;
    virtual std::vector<RankedChord> suggestChords(
        const MelodicContext& melody,
        const HarmonicContext& context,
        const StyleContext& style,
        const ConstraintStore& constraints
    ) = 0;
    virtual std::string explainSuggestion(
        const RankedChord& chord,
        const MelodicContext& melody,
        const HarmonicContext& context
    ) = 0;
};
```

### 2.3 Analysis Layer Is Display-Agnostic

Analysis components produce structured data — they never produce display strings.
Formatting is handled by separate formatter classes. This separation is already
established by `ChordSymbolFormatter` and must be maintained throughout.

### 2.4 No Conditional Logic Based on Style Identity

Closely related to 2.1. No `if (styleName == "...")` anywhere in the codebase.
Style-specific behavior flows entirely through the parameters in `StyleContext`.

### 2.5 American English Throughout

All identifiers, comments, and documentation use American English spelling.

```cpp
// CORRECT
HarmonicAnalyzer, VoiceLeadingOptimizer, visualize, behavior, color

// WRONG
HarmonicAnalyser, VoiceLeadingOptimiser, visualise, behaviour, colour
```

### 2.6 Musically Legible Documentation

Every class, method, and non-obvious data structure must be documented in terms
a person with reasonable musical knowledge and basic C++ familiarity can understand.
Comments explain the musical concept being implemented, not just the code mechanics.

See Section 17 for the full documentation standard with examples.

### 2.7 Low-Stability Decisions Are Refactorable

Directory structure, file naming, and internal organization can be refactored
efficiently with Claude Code assistance. Do not spend design energy on these.
Spend design energy on interfaces, data formats, and algorithms — things that
are genuinely expensive to change.

### 2.8 Follow MuseScore's Existing Patterns

Before implementing anything that touches MuseScore's existing infrastructure —
UI panels, score traversal, playback, settings, localization — read how MuseScore
already does it and follow the same pattern. Do not invent parallel infrastructure.

---

## 3. Directory Structure

### 3.1 Module Layout

The new code lives in `src/composing/` within MuseScore's source tree. This
namespace and directory are already established by the existing chord and key/mode
analyzers.

```
src/
  composing/
    CMakeLists.txt
    analysis/                    — analytical components (existing + planned)
      chordanalyzer.h            — existing
      chordanalyzer.cpp          — existing
      keymodeanalyzer.h          — existing
      keymodeanalyzer.cpp        — existing
      analysisutils.h            — existing shared utilities
      temporalcontext.h          — planned
      monoanalyzer.h             — planned — monophonic/arpeggiated input
      progressionanalyzer.h      — planned
    generation/                  — generative components (all planned)
      iharmonizer.h
      rulesbasedharmonizer.h
      voicinggenerator.h
      voiceleadingoptimizer.h
      basslinegenerator.h
      idiomaticgenerator.h
    knowledge/                   — knowledge base (all planned)
      chorddictionary.h
      scaledictionary.h
      substitutionnetwork.h
      styleloader.h
    intonation/                  — intonation module (planned)
      tuningcalculator.h
      driftmanager.h
    visualization/               — harmonic map views (planned)
      iharmonicmap.h
      circleoffifthsmap.h
      tonnetzmap.h
    ui/                          — new UI panels (planned)
      harmonynamigator.h
      voicingalternativespanel.h
    constraints/                 — constraint system (planned)
      constraintstore.h
    tests/                       — all tests
      chordanalyzer_tests.cpp    — existing
      keymodeanalyzer_tests.cpp  — existing
    resources/
      styles/                    — style JSON files
        builtin/
          baroque/
            bach_chorale.json
          jazz/
            jazz_vocal.json
          blues/
            blues.json
          funk/
            funk.json
          rock/
            progressive_rock.json
        user/                    — user-contributed styles
      knowledge/                 — knowledge base JSON files
        chord_dictionary.json
        scale_mode_dictionary.json
        substitution_network.json
```

### 3.2 Namespace

All code uses the namespace `mu::composing::analysis` for analysis components,
`mu::composing::generation` for generation components, and so on. This is
already established by the existing code.

---

## 4. Existing Components — The Analysis Foundation

### 4.1 ChordAnalyzer

**File:** `src/composing/analysis/chordanalyzer.h` and `chordanalyzer.cpp`

**Purpose:** Identifies the chord quality, extensions, inversions, and diatonic
degree from a set of simultaneously sounding notes. Returns up to three ranked
candidates, allowing downstream consumers to consider alternatives.

**Algorithm:** Hybrid — template matching for common chord types combined with
procedural extension detection for the combinatorial space of extensions and
alterations. Template matching uses a scoring system that weights root notes most
heavily (1.8×), thirds next (1.2×), and other chord tones equally (1.0×).
TPC (Tonal Pitch Class) data is used for enharmonic disambiguation when available.

#### Input — `ChordAnalysisTone`

```cpp
struct ChordAnalysisTone {
    int pitch = 0;      // MIDI playback pitch (ppitch — honours ottavas and transpositions)
    int tpc = -1;       // MuseScore TPC (0-34, circle-of-fifths spelling). -1 = not provided.
    double weight = 1;  // Relative evidence weight. TODO: populate from duration/beat position.
    bool isBass = false;
};
```

**Important:** `weight` currently defaults to 1.0 for all notes — it is not yet
populated from duration or metric position. This is a planned improvement (see
Section 5.1). Populating weight will improve analysis quality without any changes
to the analyzer itself.

#### Output — `ChordAnalysisResult`

```cpp
struct ChordAnalysisResult {
    double score = 0.0;        // Raw confidence. Higher is better. Not normalized.
    int rootPc = 0;            // Root pitch class (0-11, C=0)
    int bassPc = 0;            // Bass pitch class (0-11)
    ChordQuality quality = ChordQuality::Unknown;

    // Seventh extensions
    bool hasMinorSeventh = false;
    bool hasMajorSeventh = false;
    bool hasDiminishedSeventh = false;

    // Sixth and ninth
    bool hasAddedSixth = false;
    bool hasNinth = false;
    bool hasNinthNatural = false;
    bool hasNinthFlat = false;
    bool hasNinthSharp = false;

    // Eleventh and thirteenth
    bool hasEleventh = false;
    bool hasEleventhSharp = false;
    bool hasThirteenth = false;
    bool hasThirteenthFlat = false;
    bool hasThirteenthSharp = false;

    // Alterations
    bool hasFlatFifth = false;
    bool hasSharpFifth = false;

    // Special cases
    bool isSixNine = false;
    bool omitsThird = false;

    int degree = -1;            // Diatonic degree 0-6; -1 if non-diatonic
    bool diatonicToKey = false; // True if all sounding pitches are diatonic
};
```

#### Chord Quality Enum

```cpp
enum class ChordQuality {
    Unknown,
    Major,
    Minor,
    Diminished,
    Augmented,
    HalfDiminished,
    Suspended2,
    Suspended4,
    Power
};
```

#### Tunable Parameters — `ChordAnalyzerPreferences`

```cpp
struct ChordAnalyzerPreferences {
    double bassNoteRootBonus = 0.65;          // Bonus when candidate root == bass note
    double diatonicRootBonus = 0.30;          // Bonus when root is in the current key
    double tpcConsistencyBonusPerTone = 0.20; // Bonus per correctly-spelled chord tone
    double rootContinuityBonus = 0.40;        // Bonus for same root as preceding chord
    double resolutionBonus = 0.35;            // Bonus for typical harmonic resolution target

    // Planned — not yet implemented
    bool useExistingChordSymbols = false;
    bool useRomanNumeralAnnotations = false;
    bool useNashvilleAnnotations = false;

    // Planned style prior — not yet implemented
    // enum class StylePrior { General, Classical, Jazz, Pop, Blues, Folk };
    // StylePrior stylePrior = StylePrior::General;
};

inline constexpr ChordAnalyzerPreferences kDefaultChordAnalyzerPreferences{};
```

The `StylePrior` commented-out code is the planned connection between
`ChordAnalyzerPreferences` and the style system (Section 6). When the style system
is implemented, the active style will populate the analyzer's preferences.

#### Public Interface

```cpp
class ChordAnalyzer {
public:
    static std::vector<ChordAnalysisResult> analyzeChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,                         // -7 to +7
        bool keyIsMajor,                                // true = major/Ionian, false = minor/Aeolian
        const ChordTemporalContext* context = nullptr,  // optional preceding-chord context
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences
    );
};
```

Minimum 3 distinct pitch classes required. Returns empty vector if insufficient data.
Both optional parameters default so all existing call sites remain valid without
modification.

### 4.2 KeyModeAnalyzer

**File:** `src/composing/analysis/keymodeanalyzer.h` and `keymodeanalyzer.cpp`

**Purpose:** Infers the most likely key and mode from a temporal window of pitch
contexts. Uses duration weight, metric weight, and bass status to give more
influence to harmonically significant notes. Returns up to three ranked candidates.

**Algorithm:** Scores all 12 possible tonics against currently active modes (Ionian
and Aeolian) using four orthogonal helper functions:
- `scoreScaleMembership` — how well the pitch classes fit the candidate scale,
  cross-referenced against the notated key-signature scale
- `scoreTriadEvidence` — how strongly the tonic triad is present (tonic 1.6×,
  third 0.7×, fifth 0.5×, leading tone 0.4×; complete triad bonus 2.5)
- `scoreKeySignatureProximity` — preference for keys close to the notated key
  signature (−0.6 per fifth of distance)
- `applyRelativePairDisambiguation` — post-hoc score mutations for the relative
  major/minor pair sharing a key signature (four documented cases; see implementation)

The key-signature path uses a separate focussed `tonalCenterScore` formula for the
final relative-pair decision, independent of the main scoring weights so both can
be tuned without cross-interference.

All scoring weights are named constants in `KeyModeAnalyzerPreferences`.

#### Input — `PitchContext`

```cpp
struct PitchContext {
    int pitch = 0;               // MIDI pitch number
    double durationWeight = 1.0; // Duration in quarter notes — longer notes have more influence
    double beatWeight = 1.0;     // 1.0 = downbeat, ~0.2 = offbeat
    bool isBass = false;         // Bass notes weighted 2× in analysis
};
```

**Important:** In the current calling code, only `pitch` is populated. `durationWeight`,
`beatWeight`, and `isBass` default to 1.0, 1.0, and false. Populating these from
the score will significantly improve key/mode inference quality (see Section 5.1).

#### Output — `KeyModeAnalysisResult`

```cpp
enum class KeyMode {
    Ionian,   // Major / Ionian
    Aeolian,  // Natural minor / Aeolian
    // Future: Dorian, Phrygian, Lydian, Mixolydian, Locrian
};

struct KeyModeAnalysisResult {
    int keySignatureFifths = 0;     // Inferred key as circle-of-fifths position (-7 to +7)
    KeyMode mode = KeyMode::Ionian; // Detected mode
    double score = 0.0;             // Raw confidence score — not normalized
};
```

`KeyMode` is an enum rather than a `bool isMajor` so that future modal extensions
(Dorian, Phrygian, etc.) are non-breaking at the call site — adding a new enum
variant is backward-compatible; changing a bool to an enum is not.

#### Tunable Parameters — `KeyModeAnalyzerPreferences`

All scoring weights and thresholds are collected in `KeyModeAnalyzerPreferences`
(parallel to `ChordAnalyzerPreferences`). See `keymodeanalyzer.h` for the full
struct with documentation. Key groups:

- **Note weight caps** — `noteWeightCap`, `bassMultiplier`
- **Scale membership** — four case weights (`scaleScoreInBoth`, etc.)
- **Tonal centre** — per-tone weights and bonus/penalty for complete triad
- **Tonal-centre comparison** — independent weights for the relative-pair
  final decision (`tonalCenter*`)
- **Key-signature proximity** — `keySignatureDistancePenalty`
- **Disambiguation** — `disambiguationTriadBonus`, `disambiguationTriadCost`,
  `disambiguationTonicBonus`

#### Modal Infrastructure

The full mode table is already defined in the implementation:

```cpp
constexpr std::array<ModeDef, 7> MODES = {{ ... }};  // all 7 modes

// Currently only Ionian and Aeolian are evaluated:
constexpr std::array<size_t, 2> ACTIVE_MODE_INDICES = { IONIAN_INDEX, AEOLIAN_INDEX };
```

Enabling additional modes requires only:
1. Extending `ACTIVE_MODE_INDICES`
2. Adding the new `KeyMode` enum variants
3. Calibrating the new mode's characteristic weights in `KeyModeAnalyzerPreferences`

The evaluations table is a flat `std::vector` sized by `ACTIVE_MODE_INDICES.size()`,
so no structural changes are required.

#### Public Interface

```cpp
class KeyModeAnalyzer {
public:
    static std::vector<KeyModeAnalysisResult> analyzeKeyMode(
        const std::vector<PitchContext>& pitches,
        int keySignatureFifths,
        const KeyModeAnalyzerPreferences& prefs = kDefaultKeyModeAnalyzerPreferences
    );
};
```

### 4.3 ChordSymbolFormatter

**File:** `src/composing/analysis/chordanalyzer.h` (namespace within)

**Purpose:** Formats `ChordAnalysisResult` into display strings. Kept separate from
`ChordAnalyzer` so the analysis layer remains display-agnostic. This separation must
be maintained throughout the codebase — analysis produces data, formatters produce strings.

```cpp
namespace ChordSymbolFormatter {

    // Display options — locale/notation-style concerns kept separate from analysis.
    struct Options {
        bool useGermanBHNaming = false;  // H = B natural, B = Bb (Nordic/German)
        // TODO: wire through pitchClassName once implemented
    };
    inline constexpr Options kDefaultOptions{};

    // "Cmaj7", "Fm7/Ab", "Bdim7" etc.
    std::string formatSymbol(const ChordAnalysisResult& result, int keySignatureFifths,
                             const Options& opts = kDefaultOptions);

    // "IM7", "ii7", "V7/3", "viiø7" etc. Returns "" for non-diatonic chords.
    std::string formatRomanNumeral(const ChordAnalysisResult& result, bool keyIsMajor);
}
```

Display options (`Options`) live in `ChordSymbolFormatter`, not in
`ChordAnalyzerPreferences`, enforcing the analysis/display separation (principle 2.3).

**Roman numeral scope:** The formatter currently emits Roman numerals up to the 7th
level only (e.g. `I7`, `IM7`, `iø7`). Extensions beyond the 7th (9th, 11th, 13th)
are not yet emitted. The test catalog covers the 7th level only; extending the
catalog and formatter together is a natural future increment.

#### Planned Trajectory — IChordSymbolFormatter

`ChordSymbolFormatter` will eventually become a substitutable interface, orthogonal
to `IChordAnalyzer` (Section 14.1). The two axes vary independently:

```
IChordAnalyzer          IChordSymbolFormatter
      ↓                         ↓
ChordAnalysisResult  →  formatted string
```

**Planned substitution points for IChordSymbolFormatter:**

- *Notation convention:* lead sheet ("Cmaj7"), Nashville ("1maj7"), Roman numeral
  ("IM7"), figured bass (for baroque contexts)
- *Spelling conventions:* American ("maj7", "m7b5"), German/Nordic (H/B naming),
  Berklee/jazz ("Δ7", "ø7"), classical (augmented sixth notation)
- *Symbol vocabulary:* half-diminished ø vs "m7b5" vs "ø7"; major seventh Δ vs
  "maj7" vs "M7"; augmented "+" vs "aug"

When `IChordSymbolFormatter` is introduced, `ChordSymbolFormatter::Options` becomes
its configuration struct — the migration path is already established.

### 4.4 AnalysisUtils

**File:** `src/composing/analysis/analysisutils.h`

Shared utilities used by both analyzers and the formatter:

- `normalizePc(int pitch)` — reduces any MIDI pitch to pitch class 0–11
- `ionianTonicPcFromFifths(int fifths)` — converts circle-of-fifths position to
  the pitch class of the Ionian (major) tonic for that key signature
- `endsWith(const std::string&, const char*)` — generic string suffix test

### 4.5 Current Status Bar Integration

**File:** `src/notation/notationaccessibility.cpp`

The analysis is invoked from `NotationAccessibility::singleElementAccessibilityInfo()`.
This method triggers on every selection change and appends chord/key information to
the accessibility string displayed in the status bar.

#### Score Traversal Pattern

This is the established pattern for collecting notes at a tick. All future components
that need to collect notes at a specific moment should follow this pattern:

```cpp
// 1. Find the ChordRest segment at the target tick
const Segment* seg = sc->tick2segment(tick, true, SegmentType::ChordRest);

// 2. Iterate all staves and voices — collect from every voice simultaneously
for (size_t si = 0; si < sc->nstaves(); ++si) {
    for (int v = 0; v < VOICES; ++v) {
        const ChordRest* cr = seg->cr(static_cast<track_idx_t>(si) * VOICES + v);

        // Grace notes are ornamental, not harmonic — always exclude from analysis
        if (!cr || !cr->isChord() || cr->isGrace()) {
            continue;
        }

        for (const Note* n : toChord(cr)->notes()) {
            // Use ppitch() not pitch() — honours ottavas and transposing instruments
            // Use tpc() for enharmonic spelling information
        }
    }
}
```

#### Key Decision Logic

```cpp
const KeySigEvent keySig = sc->staff(note->staffIdx())->keySigEvent(tick);
const int keyFifths = static_cast<int>(keySig.concertKey());

// Trust the key signature when it specifies major or minor explicitly
if (mode == KeyMode::MAJOR || mode == KeyMode::IONIAN) {
    isMajor = true;
} else if (mode == KeyMode::MINOR || mode == KeyMode::AEOLIAN) {
    isMajor = false;
} else {
    // KeyMode::UNKNOWN — run the KeyModeAnalyzer on a one-measure lookback window
    // TODO: This window will expand with temporal context (Section 5.3)
}
```

#### Temporal Window for Key/Mode Analysis

Currently: one measure lookback from the current tick, using all notes in that
window with default weights (1.0 for all). This will expand significantly with
temporal context improvements (Section 5.3).

#### Current Status Bar Output Format

```
[Note name]; [bar and beat]; Staff N (Part name); [G major] Cmaj7
```

The chord symbol and key are appended at the end. Roman numeral display is
implemented in `ChordSymbolFormatter::formatRomanNumeral()` but not yet
invoked in the calling code — this is a planned near-term increment (see Section 15).

#### Current Gaps in the Calling Code

Two specific gaps that are the highest-priority near-term improvements:

**Gap 1 — ChordAnalysisTone weight not populated:**
```cpp
// Current — all notes weighted equally
tone.weight = 1.0;  // default

// Planned — weight by duration and metric position
tone.weight = durationInQuarterNotes * beatWeight;
```

**Gap 2 — PitchContext fields not populated:**
```cpp
// Current — only pitch set
p.pitch = n->ppitch();
// p.durationWeight, p.beatWeight, p.isBass — all defaults

// Planned — populate all fields
p.pitch = n->ppitch();
p.durationWeight = durationInQuarterNotes;
p.beatWeight = computeBeatWeight(s->tick(), measure);
p.isBass = (n->ppitch() == lowestPpitch);
```

**Gap 3 — KeyModeAnalyzer not connected to ChordAnalyzer:**
The key/mode inferrer result is used only when `KeyMode` is `UNKNOWN`. When the
key signature explicitly says major or minor, that value is used without running
the inferrer. Planned: always run the inferrer on the temporal context window and
use its result to parameterize the chord analyzer, even when the key signature is
explicit. This handles passages that have departed from the notated key.

---

## 5. Planned Analysis Extensions

### 5.1 Weight Population — Duration and Beat

The most impactful near-term improvement requiring only changes to the calling
code in `notationaccessibility.cpp`, not to the analyzers themselves.

**Duration weight:** Use `cr->ticks().toDuration().toDouble()` or equivalent
to get the duration in quarter notes. Longer notes provide stronger harmonic evidence.

**Beat weight:** Compute from the note's position within the measure. Downbeats
(beat 1) get weight 1.0, strong beats get ~0.7, weak beats ~0.4, off-beats ~0.2.
The exact scale should be consistent with how the key/mode analyzer uses these weights.

**Bass identification:** The lowest sounding `ppitch()` across all staves and voices
at the tick. Already correctly computed for `ChordAnalysisTone.isBass` — apply the
same logic to `PitchContext.isBass`.

### 5.2 Connecting KeyModeAnalyzer to ChordAnalyzer

Currently the chord analyzer receives key information from the notated key signature.
Planned: always run the key/mode inferrer first and use its top result to parameterize
the chord analyzer.

```cpp
// Planned connection
const auto keyModeResults = KeyModeAnalyzer::analyzeKeyMode(contextPitches, keyFifths);
const bool inferredIsMajor = keyModeResults.empty()
    ? isMajor
    : (keyModeResults.front().mode == KeyMode::Ionian);
const auto chordResults = ChordAnalyzer::analyzeChord(tones, keyFifths, inferredIsMajor);
```

This single change improves chord identification in passages that have modulated
away from the notated key signature.

### 5.3 TemporalContext — Full Specification

`TemporalContext` is an optional parameter that will be added to `analyzeChord()`.
The analyzer functions correctly without it (current behavior). When provided,
it improves analysis quality significantly.

```cpp
struct TemporalContext {
    // Previous harmonic position
    std::optional<std::vector<ChordAnalysisResult>> previousChord;
    float distanceFromPreviousBeats = 0.0f;

    // Next harmonic position (look-ahead)
    std::optional<std::vector<ChordAnalysisTone>> nextTones;
    float distanceToNextBeats = 0.0f;

    // Key/mode inference at this position — from KeyModeAnalyzer
    std::optional<KeyModeAnalysisResult> keyModeContext;

    // Metric context
    float metricWeight = 1.0f;         // Strength of this beat
    bool isOnDownbeat = false;
    bool isAtPhraseBeginning = false;
    bool isAtPhraseCadence = false;

    // Duration of current harmonic event
    float durationBeats = 1.0f;

    // Recognized progression pattern if any
    std::optional<ProgressionPattern> ongoingPattern;
};
```

**How temporal context modifies scoring:**

- Previous chord continuation bonus — V7 → I, ii7 → V7 get score bonuses
- Key/mode confidence weighting — high-confidence key inference strengthens
  the diatonic root bonus beyond its flat default value
- Duration sensitivity — events shorter than half a beat get higher extension
  detection thresholds (passing chords flagged conservatively)
- Pattern completion — ii7 at previous position reinforces V7 at current position

**Implementation sequence:**
1. Define `TemporalContext` struct — optional parameter, existing tests unaffected
2. Add key/mode confidence weighting — simplest, uses already-computed data
3. Add previous chord continuation scoring
4. Add duration sensitivity for short events
5. Add pattern recognition — most complex, built on 1-4 being stable

### 5.4 Modal Extension — Beyond Ionian and Aeolian

**To enable additional modes:**

1. Change `ACTIVE_MODE_INDICES` in `keymodeanalyzer.cpp` to include desired modes
2. Calibrate scoring for each mode's characteristic features:
   - Dorian: raised sixth is the defining characteristic — add specific weight
   - Mixolydian: flat seventh defines it — conflicts with Ionian + dom7 chord
   - Lydian: raised fourth — relatively rare, careful calibration needed
   - Phrygian: flat second — very characteristic, should be detectable
   - Locrian: diminished fifth on tonic — rarely used as primary mode
3. Fix the leading tone assumption — currently hardcoded as `(tonicPc + 11) % 12`
   for all modes. Must become mode-dependent.
4. Extend `KeyModeAnalysisResult` with `tonicPc`, `modeIndex`, `modeName` fields
5. Update downstream consumers of `KeyModeAnalysisResult` — particularly the
   `isMajor` boolean passed to `ChordAnalyzer`
6. Update `ChordAnalyzer` to accept mode information beyond the binary `keyIsMajor`

**Melodic minor modes** — important for jazz:
- Lydian Dominant (mode 4 of melodic minor) — #11 and b7 together
- Altered/Superlocrian (mode 7 of melodic minor) — maximum tension
These should be added to the mode table when jazz style support is implemented.

### 5.5 Monophonic and Arpeggiated Input

The current analyzer requires `distinctPcs >= 3`. Monophonic chord inference —
inferring harmony from a single melodic instrument playing arpeggios — requires
a different entry point.

**Key concepts:**
- **Note grouping** — determine which notes belong to the same harmonic unit
  (metric position, register, repetition, duration are all cues)
- **Subset matching** — identify chords consistent with the present notes, not
  requiring an exact match
- **Compound melody** — a single line that implies two or more independent voices
  (Bach cello suites, violin partitas)

**Planned interface:**

```cpp
class MonoAnalyzer {
public:
    // Group a melodic sequence into harmonic units
    std::vector<HarmonicGroup> groupNotes(
        const std::vector<MelodyNote>& notes,
        const TimeSignature& meter,
        const StyleContext& style
    );

    // Identify chord from incomplete note set (subset matching)
    std::vector<ImpliedChord> identifyFromSubset(
        const std::vector<Pitch>& presentNotes,
        const KeyMode& key,
        const HarmonicContext& context,
        float minimumConfidence
    );
};
```

### 5.6 Secondary Dominants and Non-Diatonic Chords

When `degree == -1` (root not in scale), `formatRomanNumeral()` currently returns
an empty string. Planned extensions:

- Secondary dominants: "V7/V", "V7/ii", "V7/IV"
- Borrowed chords: "bVII", "bIII", "iv" (in major context)
- Chromatic mediants: labeled by their relationship to the tonic
- Neapolitan: "N6" or "bII6"
- Augmented sixths: "It+6", "Fr+6", "Ger+6"

### 5.7 Normalized Confidence Scores

Both analyzers return raw scores whose absolute value is meaningless without context.
Planned: add normalized scores (0.0-1.0) to both result structs, enabling UI decisions
about display confidence:

- Above 0.8 — display confidently
- 0.5-0.8 — display with qualification ("possibly")
- Below 0.5 — display tentatively or suppress

### 5.8 Known Analyzer Limitations

These are known cases where the current tertian template-matching approach produces
incorrect or misleading results. Each has a planned resolution noted.

**Quartal and quintal chords**

The analyzer is built entirely on tertian templates — chords built from stacked thirds.
Chords built from stacked fourths or fifths are force-fitted into the nearest tertian
interpretation. The four open strings of a guitar (E-A-D-G) — three stacked perfect
fourths — are analyzed as Em11, which is technically defensible but musically wrong.
The chord has no tertian root in the meaningful sense. The planned resolution is a
musical language detector that switches the analyzer into a quartal/quintal mode before
attempting tertian analysis. Quartal and quintal support is in Prepared scope.

**The add2/add9 distinction**

Cadd2 and Cadd9 contain identical pitch classes — the distinction is registral, not
harmonic. The added D appears within the root's octave (add2) or above it (add9). The
current analyzer discards register information immediately by reducing all pitches to
pitch classes. Distinguishing add2 from add9 requires preserving full MIDI pitch through
the analysis pipeline and running a register-aware second pass after chord identification.
This is a planned extension — not a minor change — and is deferred until the generation
engine requires it.

**Rootless voicings**

When no root is present — common in jazz ensemble writing where the bass instrument
provides the root — the analyzer's bass-note-root bonus misfires. The lowest sounding
note gets promoted to root status incorrectly. Correct handling requires knowing that a
bass instrument is providing the root, which is context the current analyzer does not
have. Planned resolution: the `TemporalContext` struct will carry ensemble awareness,
suppressing the bass root bonus when appropriate.

**Polychordal and upper structure voicings**

Two distinct chords superimposed produce a pitch class set the analyzer interprets as a
single complex tertian chord. The two-chord structure is lost. Planned resolution: a
polychordal detection pass that identifies superimposed triadic structures before tertian
analysis runs.

---

## 6. The Style System

### 6.1 Overview

Musical styles are defined entirely in JSON files. The C++ code implements mechanisms —
voice leading optimization, chord generation, voicing rules — while JSON files define
parameters. Adding a new style never requires C++ changes.

### 6.2 Mixin Architecture

A style is not a monolithic entity but an assembly of independent dimensions. Each
dimension can be inherited from a different source:

```json
{
  "metadata": {
    "id": "bossa_nova",
    "name": "Bossa Nova"
  },
  "mixins": {
    "harmonic_language": "jazz/jazz_vocal",
    "rhythmic_feel": "dimensions/rhythm/samba_pattern",
    "bass_line": "dimensions/bass/samba_bass",
    "voicing": "dimensions/vocal/close_harmony",
    "form": "jazz/jazz_vocal"
  },
  "overrides": {
    "harmonic_language": {
      "substitution_frequency": 0.5
    }
  }
}
```

**Dimensions:**
- `harmonic_language` — available chords, progressions, substitutions
- `voice_leading` — motion type preferences, parallel interval tolerance
- `voicing` — drop voicing technique, lead voice position, spread constraints
- `rhythmic_feel` — meter, groove, harmonic rhythm patterns
- `form` — phrase structure, cadence types, section characteristics
- `bass_line` — walking bass, funk bass, melodic bass character
- `melodic` — scales, ornaments, approach notes
- `idiomatic_material` — fills, riffs, characteristic textures
- `ensemble` — voice count, ranges, blend characteristics
- `tuning` — which tuning system applies
- `generation` — creativity level, substitution frequency, complexity target
- `analysis` — what the analyzer flags as problems vs features

**Conflict resolution priority:**
1. System defaults — lowest priority
2. Mixin sources — in declared order, later overrides earlier
3. Explicit `overrides` in the style file — highest priority, always wins

### 6.3 Style File Naming and Location

```
src/composing/resources/styles/
  builtin/
    baroque/
      bach_chorale.json
    jazz/
      jazz_vocal.json
    blues/
      blues.json
    funk/
      funk.json
    rock/
      progressive_rock.json
  user/
    (user-contributed styles — not shipped with MuseScore)
  dimensions/
    harmonic/
    rhythm/
    bass/
    vocal/
  schema/
    style_schema.json          — JSON Schema — formal validation
    STYLE_AUTHORING_GUIDE.md   — Human-readable guide for style authors
    example_minimal.json       — Simplest possible valid style
    example_inherited.json     — Demonstrates mixin inheritance
```

### 6.4 Style Loader

The style loader scans the styles directory recursively and loads all valid JSON files.
It never references specific style IDs in code — it simply loads whatever it finds.

```cpp
class StyleLoader {
public:
    // Load all styles from the given root directory
    std::vector<StyleContext> loadAll(
        const std::filesystem::path& stylesRoot
    );

    // Load a single style file, resolving mixin inheritance
    StyleContext load(const std::filesystem::path& styleFile);

private:
    // Merge parent dimension into child, child overrides parent
    template<typename T>
    T mergeDimension(const T& parent, const T& child);
};
```

### 6.5 Initial Styles

The five initial styles are chosen for maximum architectural diversity — they stress-test
the schema by requiring different parameter sets:

| Style | Primary challenge |
|-------|------------------|
| Bach Chorale | Strict voice leading rules, SATB ranges, functional harmony |
| Jazz Vocal | Extended harmony, drop voicings, lead voice concept |
| Blues | Non-functional dominant harmony, major/minor ambiguity |
| Funk | Static harmony, rhythmic primacy, horn section |
| Progressive Rock | Odd meter, modal harmony, extended form |

### 6.6 Connection to ChordAnalyzerPreferences

The `StylePrior` enum commented out in `ChordAnalyzerPreferences` is the planned
connection point. When the style system is active, the current style populates
the analyzer's preferences — affecting which chord types are considered idiomatic,
what extensions are expected, and how scoring weights are adjusted.

---

## 7. The Knowledge Base

The knowledge base contains musical theory encoded as structured data. It is shared
across all styles — styles reference knowledge base entries rather than duplicating them.

### 7.1 Chord Dictionary

`resources/knowledge/chord_dictionary.json`

For every chord type — all roots, all qualities, all extensions — defines:
- Interval structure (semitones from root)
- Guide tones (3rd and 7th — most harmonically essential)
- Essential tones (must include in voicing)
- Omissible tones (fifth is usually omissible)
- Color tones (extensions and alterations)
- Implied scale (chord-scale relationship from Berklee/Nettles tradition)
- Tendency tones (which notes want to resolve and where)
- TPC deltas (for enharmonic spelling — already used in ChordAnalyzer)

### 7.2 Scale and Mode Dictionary

`resources/knowledge/scale_mode_dictionary.json`

For every scale and mode — defines:
- Interval structure
- Available tensions (can be added without clashing)
- Avoid notes (create unresolvable dissonance)
- Characteristic chord types
- Connection to chord types (chord-scale relationships)
- Historical period and style associations

### 7.3 Substitution Network

`resources/knowledge/substitution_network.json`

For every chord type — defines available substitutions:
- Tritone substitution (dominant chords — root moves tritone, guide tones exchange)
- Secondary dominant (V7 of any diatonic chord)
- Backdoor dominant (bVII7 → I)
- Modal interchange (borrowed from parallel mode)
- Relative substitution (relative major/minor)
- Each substitution includes voice leading implications and style weights

### 7.4 Ornament Vocabulary

`resources/knowledge/ornament_vocabulary.json`

Style-specific ornament types:
- Baroque: trill, mordent, turn, appoggiatura, acciaccatura, Schleifer
- Jazz: approach notes, encirclement, blues bend notation
- Classical: ornament table per period

---

## 8. Planned Generation Components

All generation components are behind abstract interfaces (Principle 2.2).
No generation is implemented yet — this section documents the planned design.

### 8.1 IHarmonizer

The primary generation interface. Both rule-based and future ML implementations
satisfy this interface.

```cpp
class IHarmonizer {
public:
    virtual ~IHarmonizer() = default;

    virtual std::vector<RankedChord> suggestChords(
        const MelodicContext& melody,
        const HarmonicContext& context,
        const StyleContext& style,
        const ConstraintStore& constraints
    ) = 0;

    // Every implementation must explain its suggestions in musical terms
    virtual std::string explainSuggestion(
        const RankedChord& chord,
        const MelodicContext& melody,
        const HarmonicContext& context
    ) = 0;
};

class RuleBasedHarmonizer : public IHarmonizer { ... };  // First implementation
class MLHarmonizer : public IHarmonizer { ... };          // Future ML implementation
class HybridHarmonizer : public IHarmonizer { ... };      // Rule-generated, ML-ranked
```

### 8.2 VoicingGenerator

Given a chord symbol and context, generates specific voicings appropriate to the
style and ensemble profile. The generator interface is voicing-type agnostic — the
caller specifies a style and the generator selects and applies appropriate voicing
types from the style parameters. The style JSON determines which voicing types are
used and in what proportion. Adding a new voicing type means adding it to the
generator implementation and making it available as a style parameter — the interface
does not change.

```cpp
class VoicingGenerator {
public:
    // Style determines which voicing types are used and in what proportion.
    // Never call with a specific voicing type directly — encode that in the style.
    std::vector<Voicing> generateCandidates(
        const ChordSymbol& chord,
        const StyleContext& style,
        const EnsembleProfile& ensemble,
        const Voicing& previousVoicing,    // for voice leading continuity
        const ConstraintStore& constraints
    );
};
```

**Voicing type taxonomy:**

*Tertian family — close position variants:*
- **Close position** — all voices within one octave, chord tones ascending. Baseline
  for all drop transformations.
- **Drop 2** — second voice from top dropped an octave. Primary jazz vocal voicing.
  Puerling's main tool.
- **Drop 3** — third voice from top dropped an octave. Less common, more open sound.
- **Drop 2 and 4** — second and fourth voices from top both dropped. Very open.
  Puerling's more elaborate arrangements.

*Tertian family — special cases:*
- **Shell voicings** — root, third, seventh only. Fifth omitted. Essential for jazz
  when bass instrument is present.
- **Rootless voicings** — third, seventh, and extensions only. No root. Common in jazz
  ensemble writing where the bass provides the root. Requires ensemble awareness before
  applying.
- **Chorale style** — SATB with specific doubling rules: root doubled in root position,
  leading tone not doubled, seventh not doubled. Bach chorale style. Strict and
  well-defined.
- **Spread triads** — middle note of triad displaced by an octave. Open, resonant.
  Some contemporary choral writing.

*Non-tertian family:*
- **Quartal** — stacked perfect fourths. Modal jazz, contemporary. Generated by
  stacking fourths from a starting pitch, not from a root+quality template. Requires
  quartal mode in the analyzer and musical language detector. In Prepared scope.
- **Quintal** — stacked fifths. Similar generation logic to quartal. In Prepared scope.
- **Mixed quartal/quintal** — alternating fourths and fifths. McCoy Tyner's
  characteristic sound. In Prepared scope.
- **Cluster** — adjacent semitones and seconds. Contemporary choral, avant-garde jazz.
  In Prepared scope.

*Extended tertian:*
- **Upper structure triads** — guide tones (3rd and 7th) in lower voices, a complete
  foreign triad in upper voices. The upper structure triad is selected from the
  knowledge base based on which tensions are available over the chord symbol. Requires
  chord-scale knowledge base. In Important scope.
- **Polychordal** — two complete chords superimposed. Used as a specific compositional
  effect. In Prepared scope.

**Initial implementation scope per style:**

| Style | Primary voicing | Secondary | Notes |
|---|---|---|---|
| Bach Chorale | Chorale style | — | Strict doubling rules throughout |
| Jazz Vocal | Drop 2 | Drop 2+4, close | Shell and rootless when accompanied |
| Blues | Close position | — | Simple voicings appropriate to style |
| Funk | Shell voicings | Close position | Rootless when bass is active |
| Progressive Rock | Close position | Open position | Quartal prepared but not initial |

**Style JSON voicing parameters:**

```json
{
  "voicing": {
    "close": 0.3,
    "drop2": 0.9,
    "drop2and4": 0.6,
    "shell": 0.4,
    "rootless": 0.7,
    "chorale": 0.0,
    "quartal": 0.0,
    "upper_structure": 0.4
  }
}
```

### 8.3 VoiceLeadingOptimizer

Finds the optimal sequence of voicings through a chord progression using dynamic
programming (Viterbi algorithm). Minimizes total voice leading cost subject to
hard constraints (fixed elements) and style-specific soft constraints.

**Cost function:**
```
cost = Σ(semitone distance per voice)
     + penalty for voice crossing
     + penalty for large leaps
     + bonus for common tone retention (negative cost)
     + bonus for half-step motion in inner voices (negative cost)
     + penalty for parallel octaves/fifths (style-weighted)
     + penalty for melody note not in lead voice
```

### 8.4 RuleBasedHarmonizer

The first implementation of `IHarmonizer`. Works in four stages:

1. **Melodic analysis** — phrase structure, scale degrees, climax, chromatic notes
2. **Harmonic rhythm planning** — where chord changes occur
3. **Initial chord suggestion** — most natural chord for each melody note given
   style context and key
4. **Progression coherence** — ensure functional logic, complete ii-V-I patterns,
   appropriate cadences

Chord suggestions include a creativity/temperature parameter (0.0-1.0). At 0.0,
always takes the highest-scored candidate. At higher values, samples from the
distribution — producing more surprising but still stylistically grounded choices.

### 8.5 BassLineGenerator

Generates melodically interesting bass lines appropriate to the style. Walking bass
for jazz, syncopated funk bass, melodic gospel bass, etc. The bass line has its own
melodic logic — not merely root movement through chord changes.

### 8.6 IdiomaticMaterialGenerator

Generates style-idiomatic fills and decorative material:
- Brass fills and riffs (jazz big band, funk, soul)
- Guitar riffs (rock, funk)
- Chord animation — voices moving through chord tones (Poulenc technique)

Requires gap detection — identifying structural spaces where fills are appropriate.

---

## 9. The Constraint System

### 9.1 Fix Levels

Any element of the score can be placed on a spectrum from fixed to free:

```cpp
enum class FixLevel {
    Locked,     // System never modifies this — hard constraint in optimizer
    Preferred,  // System keeps this unless strong voice leading reason to change
    Suggested,  // System's starting point, considered negotiable
    Open        // Fully available for optimization
};
```

Fixing can be applied at multiple granularities:
- Single note (specific pitch in specific voice at specific moment)
- Voice line (entire voice fixed throughout or for a passage)
- Chord (specific chord symbol fixed, voicing free — or both fixed)
- Progression (passage of bars fixed harmonically)
- Parameter (fix a characteristic rather than specific notes)

### 9.2 ConstraintStore

```cpp
class ConstraintStore {
public:
    void fix(const ScoreElement* element, FixLevel level);
    void release(const ScoreElement* element);
    bool isFixed(const ScoreElement* element) const;
    FixLevel fixLevel(const ScoreElement* element) const;

    // Fixed elements propagate influence — compute what fixing X implies
    std::vector<Constraint> propagate(const ScoreElement* element) const;

private:
    std::map<int, FixLevel> fixedElements;  // keyed by MuseScore element ID
};
```

Fixed elements are hard constraints in the voice leading optimizer — they anchor
the dynamic programming search. The optimizer guarantees never modifying them.

### 9.3 Persistence

Constraint data persists with the score as a separate file within the MSCZ archive
(see Section 13). Constraints are keyed by MuseScore element IDs which are stable
within a score. Fixed elements are visually indicated in the score view.

---

## 10. Visualization

### 10.1 IHarmonicMap Interface

All harmonic space visualizations implement this interface. Adding a new map type
means implementing the interface — the preview engine works automatically.

```cpp
class IHarmonicMap {
public:
    virtual ~IHarmonicMap() = default;

    // What chord does this position on the map represent?
    virtual std::optional<ChordSymbol> chordAt(
        const MapPosition& position
    ) const = 0;

    // What chords are harmonically adjacent to this chord on this map?
    virtual std::vector<ChordSymbol> neighboringChords(
        const ChordSymbol& chord
    ) const = 0;

    // Where on the map does this chord appear?
    virtual std::optional<MapPosition> positionOf(
        const ChordSymbol& chord
    ) const = 0;

    // Highlight these chords (substitutes, smooth voice leading targets, etc.)
    virtual void highlight(
        const std::vector<ChordSymbol>& chords,
        HighlightType type
    ) = 0;

    // Show the current score position on the map
    virtual void showCurrentPosition(
        const ChordSymbol& currentChord
    ) = 0;
};
```

### 10.2 Initial Implementation — Circle of Fifths

First harmonic map implementation. Shows key relationships and chord relationships
by fifth. Familiar to all musicians. No IP concerns. Implemented as a QML component
following MuseScore's existing UI patterns.

The circle shows:
- Current key highlighted
- Current chord highlighted
- Harmonically adjacent chords available for preview
- Clicking a chord triggers the preview engine

### 10.3 Planned — Tonnetz

Two-dimensional lattice where horizontal = perfect fifths, diagonals = major/minor
thirds. Every major and minor triad is a triangle. Adjacent triangles share two
common tones — minimum voice leading cost. Geometric distance represents harmonic
distance. No IP concerns — 19th century mathematical structure.

### 10.4 Planned — Functional Harmony Map

MTH Pro-style map based on Berklee chord-scale theory (Nettles, Levine). Positions
chords by functional region (tonic, subdominant, dominant) and shows available
tensions. Our own visual design — not a reproduction of MTH Pro's specific layout.

### 10.5 The Preview Engine

Enables clicking any chord on any map and hearing it immediately in context.

```cpp
class HarmonicPreviewEngine {
public:
    // Play a chord immediately — triggered by map interaction
    // Uses MuseScore's existing note-input preview infrastructure (low latency)
    void previewChord(
        const ChordSymbol& chord,
        const Voicing& voicing,
        const PreviewContext& context
    );

    // Play context chord — preview chord — optional resolution
    void previewProgression(
        const std::vector<ChordSymbol>& chords,
        const StyleContext& style,
        const EnsembleProfile& ensemble
    );

    void stopPreview();
    bool isPlaying() const;
};
```

**Implementation note:** Use MuseScore's note-input preview pathway (same as hearing
a note when clicking in input mode) — not the full score playback pipeline. The
full pipeline has too much latency for interactive map exploration. Inference runs
on a background thread via `QtConcurrent` to keep the UI responsive.

---

## 11. Intonation

### 11.1 Tuning Systems

The intonation module supports multiple western tuning systems for playback:

| System | Description | Primary use |
|--------|-------------|-------------|
| Equal temperament | All semitones equal — modern standard | Default |
| Just intonation | Pure mathematical ratios — maximum acoustic purity | A cappella choral |
| Adaptive just | Pure intervals with managed pitch drift correction | A cappella with modulation |
| Pythagorean | Pure fifths throughout — impure thirds | Medieval, Renaissance |
| Quarter-comma meantone | Pure major thirds, slightly impure fifths | Renaissance, early Baroque |
| Well temperament | All keys usable, each slightly different — Kirnberger, Werckmeister | Bach period |

### 11.2 Per-Instrument Configuration

```cpp
enum class IntonationCapability {
    FullyFlexible,      // Can adjust pitch continuously (voices, bowed strings, trombone)
    PartiallyFlexible,  // Limited adjustment (valved brass, woodwinds)
    Fixed,              // Equal temperament — cannot adjust (piano, organ, guitar)
    Excluded            // Not relevant (unpitched percussion)
};

struct InstrumentIntonationConfig {
    IntonationCapability capability;
    bool includeInAnalysis;   // Contributes to chord identification
    bool includeInTuning;     // Receives tuning offsets
    bool anchorPitch;         // Other instruments tune to this one
    float maxAdjustmentCents; // For partially flexible instruments
};
```

Percussion instruments are excluded from both harmonic analysis and intonation.
Fixed-pitch instruments (piano) serve as intonation anchors when present.

### 11.3 Drift Management

Just intonation creates pitch drift — stacking pure intervals doesn't form a closed
system (the Pythagorean comma: 12 pure fifths overshoot the octave by 23.46 cents).

The drift manager:
- Tracks accumulated pitch drift continuously
- Identifies correction opportunities (repeated notes, unisons, rests, section boundaries)
- Distributes corrections across multiple voices to minimize audibility
- Respects a configurable drift budget per section

When a fixed-pitch instrument is present, it serves as an automatic drift correction
anchor — the choir tunes to it at every piano chord, resetting drift.

---

## 12. User Interface

### 12.1 MuseScore Panel Integration

New panels follow MuseScore's existing panel architecture — KDDockWidgets for
panel management, QML for UI components. Do not create parallel infrastructure.
Read how existing MuseScore panels are implemented before creating new ones.

All user-visible strings use MuseScore's existing Qt localization infrastructure
(`.ts` files, Qt Linguist). English and Swedish translations provided for all new strings.

Accessibility follows MuseScore's existing Qt accessibility patterns — focus
management, keyboard navigation, screen reader hooks.

### 12.1a Harmonic Analysis Display Preference

A user preference controls whether harmonic analysis is shown in the status bar. This
preference exists for UI clarity — some users find the chord and key information
distracting, particularly when doing work unrelated to harmony. It is not a performance
control: analysis cost is negligible (well under 1ms) and suppressing the display does
not require skipping the analysis.

The preference follows MuseScore's existing preferences infrastructure. Toggling it
takes effect immediately on the next selection change without requiring a restart. When
disabled, the status bar reverts to standard MuseScore accessibility information.

### 12.2 Harmony Navigator

Primary temporal view — shows the chord progression over time as a sequence of
colored blocks. Block width proportional to duration. Current position highlighted.
Clicking any block selects it in the score and opens the chord detail panel.

### 12.3 Voicing Alternatives Panel

When a chord is selected, shows ranked alternative voicings. Each alternative displays:
- Notes in each voice with chord function labels
- Voice leading cost indicator
- Tendency tone status
- Brief description of what makes it distinctive

Hover over any alternative to hear it immediately (uses preview engine).

### 12.4 Tension Curve Editor

Shows harmonic tension as a continuous curve over time. The arranger can draw
a desired tension curve and the system suggests reharmonizations that approximate it.

### 12.5 Style Editor

GUI editor for creating and modifying style JSON files — making the style system
accessible to musicians without JSON expertise. A natural second-phase UI component
that doesn't affect the core architecture.

---

## 13. File Persistence

### 13.1 Separate Files in MSCZ Archive

MuseScore's MSCZ format is a ZIP archive. Our metadata lives as additional files
within the archive alongside `score.mscx`:

```
score.mscz (ZIP)
  └── score.mscx              (standard MuseScore — untouched by our code)
  └── arranger_constraints.xml (constraint data — keyed by element ID)
  └── arranger_branches.xml   (version branches)
  └── arranger_analysis.xml   (cached harmonic analysis)
  └── arranger_preferences.json (user preference model)
```

**Advantages:** Zero interference with MuseScore's standard score read/write.
The score is always valid standard MuseScore. Our data travels with the file.

**Limitation:** Exporting to MusicXML, PDF, or MIDI loses our metadata. This is
acceptable — the arranging workflow is MuseScore-native.

### 13.2 Format Versioning

All our custom files include a format version field. When the format changes,
migration code handles existing files. The score.mscx is never modified by our
persistence layer.

---

## 14. ML Readiness

### 14.1 Interface-Based Substitution Points

Every component that may eventually be replaced or augmented by ML is behind a
pure abstract interface. The factory pattern enables runtime selection:

```cpp
class HarmonizerFactory {
public:
    static std::unique_ptr<IHarmonizer> create(const SystemConfig& config) {
        switch (config.harmonizerType) {
            case HarmonizerType::RuleBased:
                return std::make_unique<RuleBasedHarmonizer>(config.knowledgeBase);
            case HarmonizerType::ML:
                return std::make_unique<MLHarmonizer>(config.modelPath);
            case HarmonizerType::Hybrid:
                return std::make_unique<HybridHarmonizer>(
                    config.knowledgeBase, config.modelPath);
        }
    }
};
```

Components with ML substitution interfaces planned:
- `IChordAnalyzer` — chord quality and extension identification from sounding notes.
  `ChordAnalyzer` is currently a static class; when ML substitutability is needed,
  it will be placed behind this interface alongside `RuleBasedChordAnalyzer`.
  Note: `ChordSymbolFormatter` is **not** part of this interface — it operates on
  `ChordAnalysisResult` regardless of which implementation produced it (see Section 4.3).
- `IKeyModeInferrer` — key/mode inference ranking
- `IHarmonizer` — initial chord suggestions
- `IHarmonicRhythmPlanner` — where chord changes occur
- `IVoicingRanker` — ranking voicing alternatives

### 14.2 Data Collection Infrastructure

The system logs arranger interactions from the start — with user consent — as
future ML training data. Every suggestion accepted, modified, or rejected is a
labeled training example specific to vocal jazz arranging, filling the corpus gap
identified in the design phase.

```cpp
struct ArrangerInteraction {
    MelodicContext melody;
    HarmonicContext context;
    StyleContext style;
    RankedChord suggested;       // What the system offered
    ChordSymbol actual;          // What the arranger used
    InteractionType type;        // Accepted, modified, rejected
    float timeToDecision;        // How long the arranger considered it
};
```

---

## 15. Development Phases

### Current Increment (In Progress)

**Status bar display — working:**
- Single note selection triggers analysis
- Chord symbol displayed: "[G major] Cmaj7"
- Roman numeral display: implemented in formatter, not yet invoked in calling code

**Immediate next steps in this increment (in priority order):**
1. **Complete accuracy work** — continue mismatch reduction in the regression test
   catalog until the abstract mismatch count is satisfactory. Better base accuracy
   must come before weight population, because duration/beat weights amplify whatever
   the base scoring does. (Current: 17 abstract mismatches, down from 44 baseline.)
2. **Populate `ChordAnalysisTone::weight`** from duration and beat position in
   `notationaccessibility.cpp` — no analyzer changes required
3. **Invoke `formatRomanNumeral()`** in `notationaccessibility.cpp` — display both
   chord symbol and Roman numeral in status bar. One small change that completes
   the visible increment.
4. **Populate all `PitchContext` fields** for key/mode analyzer
5. **Connect key/mode inferrer result to chord analyzer** — always run inferrer,
   use its result even when key signature is explicit

**Following this increment:**
- User can insert the inferred chord symbol into the score as a chord symbol element
- User can insert the inferred Roman numeral as a Roman numeral annotation
- Both insertions use MuseScore's existing command system for undo/redo compatibility

### Phase 1 — Analysis Foundation Complete

- `TemporalContext` struct defined and integrated
- Previous chord continuation scoring
- Duration sensitivity for passing events
- Modal extension — Dorian and Mixolydian at minimum
- `KeyModeAnalysisResult` extended with `modeIndex` and `tonicPc`
- Normalized confidence scores in both result structs
- Monophonic/arpeggiated chord inference
- Secondary dominant Roman numeral notation

### Phase 2 — Knowledge Base and Style System

- `ChordDictionary` — complete chord-scale relationships from Nettles/Levine
- `ScaleModeDictionary` — all western scales and modes
- `SubstitutionNetwork` — complete substitution types with voice leading implications
- Style JSON schema defined and documented
- `StyleLoader` implemented
- Five initial styles authored: Bach chorale, jazz vocal, blues, funk, progressive rock
- `StylePrior` connection in `ChordAnalyzerPreferences` implemented

### Phase 3 — Generation Engine

- `VoicingGenerator` — style-aware voicing from chord symbols
- `VoiceLeadingOptimizer` — Viterbi algorithm over voicing graph
- `RuleBasedHarmonizer` — complete harmonization from melody
- `ConstraintStore` — full fixing system
- `BassLineGenerator` — walking bass for jazz style

### Phase 4 — UI Panels

- Harmony Navigator panel
- Voicing Alternatives panel
- Chord detail panel
- Style selector
- Tension curve editor

### Phase 5 — Visualization and Preview

- Circle of fifths map (first `IHarmonicMap` implementation)
- `HarmonicPreviewEngine` — low-latency chord audition
- Map interaction — click to preview, path exploration
- Tonnetz map (second implementation)

### Phase 6 — Intonation Module

- `TuningCalculator` — compute just intonation offsets from analysis results
- Per-instrument configuration
- `DriftManager` — drift prediction and correction
- Tuning system selector (equal, just, meantone, well temperament, Pythagorean)

---

## 16. Scope Reference

### Core — Must Be Implemented

Harmonic analysis (functional, modal, extended tonal, jazz), monophonic chord
inference, analysis correction and ground truth override, voice leading analysis
and optimization, tendency tone tracking, tuning system support, per-instrument
tuning configuration, percussion exclusion, ornamentation (analysis and generation),
variable voice count, transposing instruments, chord symbol input, MSCZ file
persistence, undo/redo integration, incremental analysis cache, enharmonic spelling,
score error detection, musical language detector and graceful degradation, extensible
style system, initial five styles, ML interface design throughout, unified temporal
representation, pickup bars and anacrusis, localization (English and Swedish via
MuseScore infrastructure), accessibility (via MuseScore infrastructure).

### Important — Planned for Later Phases

Full generative support for pop, rock, funk, soul, metal, progressive rock (phased
by style), bass line generation, brass fills and idiomatic material, chord animation
(Poulenc model), non-chord tone generation, doubling rules per style, variation
generation, version branching, arrangement comparison, multiple expertise levels in
UI, natural language instruction, education mode, figured bass input and output,
performance markup suggestions, meter changes and mixed meter, drift prediction and
management, comma pumping, historical tuning for fixed instruments, copyright and
attribution metadata.

### Prepared — Architecture Ready, Implementation Deferred

Imitative counterpoint (fugue, canon), motivic tracking, through-composed large-scale
planning, quartal and quintal harmony, polytonality, sacred and liturgical music,
music theatre and opera, headless operation and batch processing, API access for
external tools, community knowledge base.

### Out of Scope

Live and real-time operation, film synchronization, adaptive game music, non-Western
traditions (graceful degradation at boundary), post-tonal and serial music (graceful
degradation at boundary), audio transcription from recording, spatial music, extended
techniques as primary language.

---

## 17. Coding Standards

### 17.1 Follow MuseScore Practice — With Higher Documentation Standard

Follow MuseScore's existing coding style throughout:
- Formatting defined in `.clang-format` — run clang-format before every commit
- Naming conventions — consistent with existing MuseScore code
- File headers — GPL v3 license header on every file (see existing files for template)
- Include ordering — follow MuseScore's convention

Where MuseScore's documentation practice is minimal, use good practice instead.

### 17.2 The Documentation Standard for This Project

Every public class must have a documentation comment explaining:
- What musical concept it implements
- What it receives as input (in musical terms)
- What it produces as output (in musical terms)
- What it does not handle (important for setting expectations)

Every public method must document:
- The musical operation being performed
- All parameters in musical terms
- Return value in musical terms
- Preconditions and postconditions

Every non-obvious scoring weight or threshold must explain its musical reasoning.

**Example — poor documentation (do not write this):**
```cpp
// Calculate x for each element in v
float calcX(std::vector<int>& v) { ... }
```

**Example — good documentation (write this):**
```cpp
/**
 * Calculates the voice leading cost between two chord voicings.
 *
 * Voice leading cost measures the total pitch motion when moving from one
 * voicing to the next. Smaller values indicate smoother voice leading —
 * the goal in most tonal styles.
 *
 * Cost is the average semitone distance moved per voice:
 *   0.0 = all voices hold common tones (maximally smooth)
 *   1.0 = each voice moves an average of one semitone
 *   3.0+ = typically indicates problematic voice leading
 *
 * Style-specific acceptable thresholds are in each style's JSON file.
 *
 * @param fromVoicing  Current chord voicing (one MIDI pitch per voice)
 * @param toVoicing    Target chord voicing (must match voice count)
 * @return             Average semitone distance per voice
 */
float calculateVoiceLeadingCost(
    const Voicing& fromVoicing,
    const Voicing& toVoicing
);
```

### 17.3 The Harmony Analyzer Documentation Rule

The chord and key/mode analyzers are the most complex components in the codebase.
Every scoring weight, threshold, and heuristic must be documented with its musical
rationale. A musician with reasonable theoretical knowledge must be able to read the
analyzer code and understand why each decision was made.

Example of the standard required (from existing code — maintain this quality):
```cpp
// TPC delta = circle-of-fifths distance for each interval, derived from music theory:
//   perfect 5th  = +1,  major 3rd = +4,  minor 3rd  = -3,  perfect 4th = -1,
//   augmented 5th = +8,  dim 5th  = -6,  minor 7th  = -2,  major 2nd   = +2.
```

### 17.4 Test Documentation Standard

Every test must document:
- What musical situation is being tested
- What the expected result is and why it is musically correct
- What a failure would indicate about the system's behavior

Tests should be readable by MuseScore open source contributors without deep
familiarity with this codebase.

---

## 18. Contributing

### 18.1 Before Writing Code

1. Read this document — especially Sections 2 (Principles) and 4 (Existing Components)
2. Read the relevant existing source files
3. For new components — confirm the interface design matches Section 8's patterns
4. For MuseScore integration — read how existing MuseScore code does it first

### 18.2 Pull Request Strategy

Each pull request should implement one coherent piece of functionality. Large
pull requests are hard to review. The phased plan in Section 15 defines natural
PR boundaries.

### 18.3 The MuseScore CLA

Before submitting any pull request to the official MuseScore repository, the
Contributor License Agreement must be signed. See MuseScore's contribution
guidelines on GitHub.

### 18.4 Updating This Document

When an architectural decision changes — update this document in the same commit.
Stale documentation is worse than no documentation because it actively misleads.
Claude Code should update relevant sections of this document as its last act when
a session changes an architectural decision.

---

## Appendix A — Key Musical Concepts

Brief definitions for developers who may be less familiar with music theory terms
used throughout the codebase.

**Pitch class (pc):** A pitch regardless of octave. C in any octave = pitch class 0.
Range 0-11. C=0, C#/Db=1, D=2, D#/Eb=3, E=4, F=5, F#/Gb=6, G=7, G#/Ab=8, A=9,
A#/Bb=10, B=11.

**TPC (Tonal Pitch Class):** MuseScore's representation of enharmonic spelling.
Distinguishes F# from Gb even though they are the same pitch class. Range 0-34 on
the circle of fifths. Used for correct chord naming.

**Circle of fifths:** Arrangement of the 12 pitch classes by perfect fifth.
C-G-D-A-E-B-F#/Gb-Db-Ab-Eb-Bb-F-C. Keys close on the circle are harmonically
related. Key signatures are measured in fifths from C (0 = C major, +1 = G major,
-1 = F major, etc.).

**Guide tones:** The 3rd and 7th of a chord — they define the chord's quality most
essentially and create the strongest tendency to resolve. In G7 the guide tones are
B (major 3rd) and F (minor 7th) — they form a tritone that resolves to C major.

**Tendency tone:** A pitch that has a strong gravitational pull toward a specific
resolution. The leading tone (major 7th of the scale) pulls upward to the tonic.
The chordal 7th pulls downward by step.

**Voice leading:** How individual melodic voices move from one chord to the next.
Good voice leading minimizes motion, prefers stepwise movement, avoids parallel
perfect intervals, and resolves tendency tones appropriately.

**Drop 2 voicing:** Take a close-position four-note chord and drop the second voice
from the top down an octave. Opens the spacing while maintaining smooth voice leading
connections. Characteristic of jazz vocal arranging (Puerling style).

**Roman numeral analysis:** Labeling chords by their scale degree in a key. I = tonic,
IV = subdominant, V = dominant, ii = supertonic, etc. Upper case = major, lower case
= minor. Superscripts indicate extensions: V7 = dominant seventh.

**ii-V-I:** The most fundamental jazz chord progression — minor seventh chord on
scale degree 2, dominant seventh on scale degree 5, major seventh on scale degree 1.
The guide tones resolve by half step: the 7th of ii becomes the 3rd of V, the 7th
of V resolves to the 3rd of I.

---

## Appendix B — MuseScore Score Model Quick Reference

Key classes used in score traversal. Read MuseScore source for full interfaces.

```cpp
Score*        // The complete score
Measure*      // A single measure — score->tick2measure(tick)
Segment*      // A moment in time within a measure — seg->tick(), seg->next1()
ChordRest*    // Either a Chord or a Rest — seg->cr(track)
Chord*        // A chord (collection of notes) — toChord(cr)
Note*         // A single note — n->ppitch(), n->tpc(), n->tick()
Staff*        // A staff — score->staff(staffIdx)
KeySigEvent   // Key signature — staff->keySigEvent(tick)

// Segment types used in analysis
SegmentType::ChordRest  // Notes and rests — what we analyze
SegmentType::KeySig     // Key signature changes

// Traversal
score->tick2segment(tick, true, SegmentType::ChordRest)
score->tick2measure(tick)
measure->first(SegmentType::ChordRest)
segment->next1(SegmentType::ChordRest)

// Always use ppitch() not pitch() — honours ottavas and transposing instruments
// Always exclude grace notes — cr->isGrace()
// Tracks = staffIndex * VOICES + voiceIndex (VOICES = 4)
```

---

*Document version: 1.2 — Added: §5.8 analyzer limitations (quartal, add2/add9, rootless, polychordal), §8.2 voicing type taxonomy, §12.1a status bar display preference*
*Last updated: March 2026*
*Maintainer: Update this document whenever architectural decisions change*
