# MuseScore Arranger — Architecture Document

> **Living design document.** Read this AND STATUS.md at the start of every development
> session. ARCHITECTURE.md contains stable design decisions. STATUS.md contains current
> implementation status and immediate next steps. Update STATUS.md as your last act when
> anything changes. Update ARCHITECTURE.md only when architectural decisions change.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Architectural Principles](#2-architectural-principles)
3. [Directory Structure](#3-directory-structure)
   - §3.3 [Module Boundaries and Bridge Architecture](#33-module-boundaries-and-bridge-architecture) ← **read this if touching any bridge or cross-module code**
4. [Existing Components — The Analysis Foundation](#4-existing-components--the-analysis-foundation) (incl. §4.6 User Preferences)
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

### 1.4 Implemented Components

- **ChordAnalyzer** — identifies chord quality, extensions, inversions, diatonic
  degree, and chromatic (borrowed) Roman numerals from a set of simultaneously
  sounding notes
- **KeyModeAnalyzer** — infers the most likely key and mode from a temporal window
  of pitch contexts with duration, beat, and bass weighting
- **ChordSymbolFormatter** — formats analysis results as chord symbols and Roman
  numerals; non-diatonic chords produce chromatic numerals (♭VII, ♭III, ♭VI etc.)
  rather than returning empty
- **HarmonicRhythm** — detects harmonic boundaries across a score range, drives chord
  staff population
- **Chord staff** — a grand-staff part added by the user that is populated on demand
  with a harmonic reduction: chord symbols, Roman numerals, canonical or collected
  voicings, key/mode annotations, borrowed chord labels, pivot detection, and cadence
  markers. Notes on the chord staff have `play = false` (annotation-only; they do not
  double the source staves in playback)
- **Status bar integration** — displays chord, key/mode, and Roman numeral information
  when a note is selected
- **Intonation** — per-note and region tuning via split-and-slur; tonic-anchored JI
  places each chord root at its scale-degree position above the mode tonic rather than
  always at 0¢; optional minimize-retune shift and per-note cent annotation in score;
  sustained-event rewriting is controlled by user preference, existing tie boundaries
  may be converted to slurs when independent retuning is needed, and anchors protect
  the full written duration from segmentation
- **User preferences** — `IComposingAnalysisConfiguration` and
  `IComposingChordStaffConfiguration` expose analysis and output settings; preferences
  page in Edit → Preferences → Composing

The bridge layer (`src/notation/internal/notation*bridge*.cpp`) connects the
`composing` module to MuseScore's engraving model. All bridge functions are declared
in notation-side headers and live in the `mu::notation` namespace. The `composing`
module itself has **no engraving dependency** — it is pure music theory. See §3.3 for
the full bridge architecture.

*For current implementation status, test counts, known gaps, and immediate next steps
see STATUS.md.*

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

### 2.9 Analyze and Suggest — Never Modify Without Explicit User Action

The system presents analytical findings and suggestions. It never modifies the main score
automatically. All score modifications require explicit user action. The chord track, status
bar display, and visualization panels are informational — they show what the system has
inferred without changing anything. When the user wants to act on a suggestion — inserting a
key signature, adding a chord symbol, applying tuning — they do so explicitly through
standard MuseScore editing.

### 2.10 Single Implementation for Shared Logic

Any algorithm that must produce identical results in both the notation bridge and
`batch_analyze` belongs in the `composing` module (`src/composing/`), not in either
consumer. The bridge and `batch_analyze` are both consumers of composing-layer logic —
they should not contain their own copies of it.

Before implementing any new note collection, boundary detection, key/mode resolution,
or chord scoring logic:

1. First ask: does this belong in the `composing` module where both the bridge and
  `batch_analyze` can call it directly?
2. If yes: implement it there first, then wire both consumers to call it.
3. If a composing-layer implementation is not immediately feasible (dependency
  constraints, interface not yet designed), implement in one place only and
  immediately file a technical debt note. Do not copy-paste.
4. Mirroring (duplicating logic across the bridge and `batch_analyze`) is a last
  resort, used only when a shared implementation is blocked by dependency
  constraints that cannot be resolved in the current session. Any mirrored code
  must be marked with a TODO comment referencing this rule and the technical debt
  note.

The current state (two duplicate regional collectors in
`notationcomposingbridgehelpers.cpp` and `batch_analyze.cpp`) violates this rule and
is recorded as technical debt in §4.1c. Resolving it requires moving
`collectRegionTones()`, `detectHarmonicBoundariesJaccard()`, and
`resolveKeyAndMode()` into `src/composing/` with a generic note-provider interface
that both the bridge (Score*-based) and `batch_analyze` (direct engraving access)
can implement.

### 2.11 Score Inspection Before Diagnosis

When a corpus result is unexpected — agreement rate significantly above or below
neighboring corpora, high unmatched rate, zero-region files, or a suspected failure
mode — open a representative score in MuseScore Studio before running any diagnostic
scripts or changing any code.

Score inspection takes 2 minutes and answers questions that corpus statistics cannot:

- What is the actual texture? (SATB, Alberti bass, walking bass, running passages,
  pedal notation, arpeggiation)
- What does the chord track show? (over-segmentation, missing regions, wrong roots,
  empty spans)
- Is the key detection correct at the opening?
- Are pedal markings present and where?
- Is the harmonic rhythm fast or slow relative to what our region count implies?

Specific triggers that require score inspection before any other action:

- Any corpus with >20% drop or rise vs similar repertoire
- Any corpus with >30% unmatched annotation rate
- Any corpus with >10% zero-region files
- Any proposed scoring change that would affect a specific texture type
- Any new corpus being added to the validation suite — inspect at least 3
  representative scores before running `batch_analyze`

The developer (Vincent) performs score inspection in MuseScore Studio and reports
findings. Claude Code does not have direct score access and must not substitute
statistical inference for visual score inspection.

### 2.12 Benchmark Score Set

**Rule 12 — Benchmark score set**

Any change to the analyzer, bridge, or chord-track output must be evaluated visually against
the following three scores before committing:

| Score | File | Key passages |
|-------|------|-------------|
| Bach BWV 227.7 | `tools/corpus/bwv227.7.xml` | Bars 1-2, 8-10, final cadence |
| Chopin BI16-1 | `tools/dcml/chopin_mazurkas/MS3/BI16-1.mscx` | Bars 1-5, 10-16, trio |
| Dvořák op08n06 | `tools/dcml/dvorak_silhouettes/MS3/op08n06.mscx` | Early slow section, chromatic middle |


This is Rule 11 (score inspection before diagnosis) operationalized for the current
development phase. Open the score in MuseScore Studio, implode to chord track, and
confirm the key passages look reasonable before accepting any change. If a change
improves corpus numbers but worsens any benchmark passage visually, treat it as a red
flag and report before committing.

**Rule 14 — Shell discipline for long-running commands**

All build and test commands must run synchronously (foreground). Never use background jobs or split output.

Correct patterns:
```bash
# Build
cmake --build ninja_build_rel --target notation_tests --parallel 2>&1 | tail -20

# Tests — run once, capture tail
./ninja_build_rel/notation_tests.exe 2>&1 | tail -10

# Python scripts
python tools/test_batch_analyze_regressions.py 2>&1 | tail -5

# Long corpus runs — use tee
python tools/run_corpus.py 2>&1 | tee /tmp/corpus_run.txt | tail -5
# Then after completion:
cat /tmp/corpus_run.txt
```

Never do:
- `command &` (background job)
- Run, decide too slow, kill and re-run differently
- Check background task output more than once

One run, one result. If output is unexpected, report it and ask for instructions. Do not silently re-run.

**Rule 13 — Commit before session end**

Every development session must end with a git commit of all working tree changes, even if changes are incomplete or tests are partially failing. An uncommitted working tree that spans multiple sessions makes it impossible to identify what changed between sessions and prevents reliable diagnosis of regressions.

If tests are failing at session end:
- Commit with a clear message noting the failing test names
- Record the failing tests in STATUS.md current state summary
- Do not leave uncommitted changes

A commit with known failing tests is better than no commit. The commit history is the only reliable record of what changed and when.

Corollary: at session start (Rule 9 stale binary checklist), if the working tree is dirty, stash or commit before doing anything else. Never diagnose test failures in a dirty working tree without first knowing what changed.

**Rule 16 — Do not rely on chords.xml**

MuseScore has two chord description files:
- `share/chords/chords_std.xml` — the active standard chord list used by default in all scores
- `share/chords/chords.xml` — legacy file, likely deprecated, contains known bugs and inconsistencies with the parser

When our formatter produces a chord symbol string, it must be valid according to `chords_std.xml` only. Do not add chord symbol strings that exist only in `chords.xml` — they will fail to parse correctly under the Standard chord style and may produce corrupted output.

Confirmed example: `9sus` exists in `chords.xml` (id=134) but not in `chords_std.xml`. When used with Standard chord style, it triggers `generateDescription()` which produces a corrupted render list causing `Fsussus9` in the display. Fix: use `sus(add9)` instead which is correctly handled by the parser.

When adding new chord symbol formats, always verify against `chords_std.xml` first, not `chords.xml`.

### 2.13 Cross-Platform by Default

All code must run on every platform officially supported by MuseScore Studio: Windows,
macOS, and Linux. Platform-specific code is permitted only when absolutely necessary,
must be clearly documented, and must be abstracted so that the rest of the module
remains platform-agnostic. All build scripts, dependencies, and runtime logic must
be verified on all supported platforms before merging.

---

## 3. Directory Structure

### 3.1 Module Layout

The new code lives in `src/composing/` within MuseScore's source tree. This
namespace and directory are already established by the existing chord and key/mode
analyzers.

```
src/
  composing/                        ← NEW module — pure music theory, NO engraving dependency
    CMakeLists.txt
    composingmodule.cpp/.h          ← registers IComposingAnalysisConfiguration +
    composingconfiguration.cpp/.h      IComposingChordStaffConfiguration in IoC
    icomposinganalysisconfiguration.h  ← analysis+tuning prefs; IoC-registered
    icomposingchordstaffconfiguration.h← chord staff prefs; IoC-registered
    icomposingconfiguration.h          ← composite base (NOT IoC-registered; see §3.3)

    analysis/                    ← existing, fully working
      chord/
        ichordanalyzer.h          ← IChordAnalyzer interface
        chordanalyzerfactory.h/.cpp ← ChordAnalyzerFactory
        chordanalyzer.h/.cpp      ← RuleBasedChordAnalyzer implementation
      key/
        keymodeanalyzer.h/.cpp    ← KeyModeAnalyzer, all 21 modes
      region/
        harmonicrhythm.h          ← HarmonicRegion struct (types only)
      analysisutils.h             ← pitch-class helpers shared across subdirectories

    intonation/                  ← existing, fully working
      tuning_system.h            ← TuningSystem abstract base, TuningRegistry
                                    (no bridge decls — those are in notation/)
      tuning_keys.h
      tuning_utils.h
      equal_temperament.h/.cpp
      just_intonation.h/.cpp
      pythagorean.h/.cpp
      quarter_comma_meantone.h/.cpp
      werckmeister.h/.cpp
      kirnberger.h/.cpp

    tests/
      chordanalyzer_tests.cpp
      chordanalyzer_musicxml_tests.cpp
      keymodeanalyzer_tests.cpp
      synthetic_tests.cpp            ← P6 parametrized suite (root coverage, inversions, modes, round-trip)
      tuning_tests.cpp
      chord_mismatch_report.txt      ← written by catalog test run

  notation/
    internal/
      notationanalysisinternal.h     ← internal helpers shared between bridges:
                                        isChordTrackStaff(), staffIsEligible()
      notationcomposingbridge.h/.cpp ← BRIDGE: analyzeNoteHarmonicContext(),
                                        analyzeHarmonicRhythm(), harmonicAnnotation()
                                        Declared AND defined in mu::notation namespace.
      notationimplodebridge.h/.cpp   ← BRIDGE: populateChordTrack()
      notationtuningbridge.h/.cpp    ← BRIDGE: applyTuningAtNote(), applyRegionTuning()
      notationinteraction.cpp        ← NotationInteraction methods incl. composing ops
                                        (implodeToChordTrack, tuneSelection,
                                         addAnalyzedTuning, addAnalyzedHarmony*)
      notationaccessibility.cpp      ← status bar; calls harmonicAnnotation()

  notationscene/
    qml/MuseScore/NotationScene/
      notationcontextmenumodel.cpp   ← right-click menu; calls mu::notation::
                                        analyzeNoteHarmonicContext() via bridge header

  appshell/
    qml/MuseScore/AppShell/
      appmenumodel.cpp/.h            ← top bar "Tune as" and chord track menus;
                                        injects IComposingAnalysisConfiguration

  preferences/
    qml/MuseScore/Preferences/
      composingpreferencesmodel.cpp/.h ← injects BOTH IComposingAnalysisConfiguration
                                          AND IComposingChordStaffConfiguration

  composing/
    resources/
      styles/                    — style JSON files (planned)
      knowledge/                 — knowledge base JSON files (planned)
```

**Planned but not yet present:** `generation/`, `knowledge/`, `visualization/`, `ui/`, `constraints/` subdirectories and their contents (see §§6–10).

### 3.2 Namespace

| Namespace | Where it lives | What goes here |
|-----------|---------------|----------------|
| `mu::composing::analysis` | `src/composing/analysis/` | Pure analysis types and algorithms (ChordAnalyzer, KeyModeAnalyzer, ChordSymbolFormatter, HarmonicRegion struct, …) |
| `mu::composing::intonation` | `src/composing/intonation/` | Tuning systems (TuningSystem, TuningRegistry, concrete systems) |
| `mu::composing` | `src/composing/` | Configuration interfaces (IComposingAnalysisConfiguration, IComposingChordStaffConfiguration) |
| `mu::notation` | `src/notation/` | **All bridge functions** — functions that require engraving access but produce composing-domain results live here, not in `mu::composing`. This is the primary rule of the bridge layer. See §3.3. |
| `mu::notation::internal` | `src/notation/internal/` | Internal notation helpers (isChordTrackStaff, staffIsEligible) |

**Critical rule:** If a free function requires `mu::engraving` types as parameters, it belongs in `mu::notation` regardless of what it returns. The `composing` module must not forward-declare or depend on engraving types.

### 3.3 Module Boundaries and Bridge Architecture

> **Read this section before touching any code that crosses the composing ↔ notation boundary.**

#### The Dependency Rule

```
engraving     ← knows nothing about composing or notation
    ↓
composing     ← pure music theory; NO engraving dependency whatsoever
    ↓              (no forward declarations, no includes of engraving headers)
notation      ← bridges both; owns all bridge function declarations and definitions
    ↓
notationscene ← calls notation bridge API; does NOT include composing headers directly
appshell      ← calls notation API; injects composing config interfaces
preferences   ← injects both composing config interfaces
```

This dependency order is **enforced**. Any code that would invert it (e.g. a composing header forward-declaring `mu::engraving::Note`) must be moved to the notation bridge layer.

#### Why This Matters

The `composing` module is a pure C++ music theory library. It can be unit-tested in complete isolation from MuseScore's engraving model — no score, no staves, no UI, just pitch classes and algorithms. This isolation is what makes the test suite (`composing_tests.exe`) fast and reliable.

If `composing` headers imported engraving types, the unit tests would need to link against the full engraving library. More fundamentally, it would mean the music theory library had knowledge of a specific score representation format — a structural coupling that makes the algorithms harder to reuse or replace.

#### The Bridge Pattern

A "bridge function" is a free function that:
- Takes engraving types as input (Note*, Score*, Fraction, …)
- Produces composing-domain results (ChordAnalysisResult, HarmonicRegion, …)
- Lives in `mu::notation` namespace
- Is declared in a `notation/internal/notation*bridge.h` header
- Is defined in the corresponding `notation/internal/notation*bridge.cpp`

**Callers** of bridge functions include only the notation-side bridge header, not composing headers, for the function itself. They may still include composing headers for the composing types in the function signature.

#### Bridge File Inventory

| File | Declares/defines | Called by |
|------|-----------------|-----------|
| `notationcomposingbridge.h` | Declares `harmonicAnnotation()`, `analyzeNoteHarmonicContext()`, `analyzeHarmonicRhythm()`, and `HarmonicRegionGranularity` | `notationaccessibility.cpp`, `notationinteraction.cpp`, `notationcontextmenumodel.cpp`, `notationimplodebridge.cpp`, `notationtuningbridge.cpp` |
| `notationcomposingbridge.cpp` | `harmonicAnnotation()` — status bar string<br>`analyzeNoteHarmonicContext()` — single-note analysis | (implements declarations above) |
| `notationharmonicrhythmbridge.cpp` | `analyzeHarmonicRhythm()` — time-range harmonic scanner | (implements declaration above) |
| `notationcomposingbridgehelpers.h/.cpp` | Shared bridge helpers: `collectSoundingAt()`, `buildTones()`, `collectPitchContext()`, `resolveKeyAndMode()`, `findTemporalContext()`, … | `notationcomposingbridge.cpp`, `notationharmonicrhythmbridge.cpp` |
| `notationimplodebridge.h/.cpp` | `populateChordTrack()` — write harmonic reduction to chord staff | `notationinteraction.cpp` (via `implodeToChordTrack()`) |
| `notationtuningbridge.h/.cpp` | `applyTuningAtNote()` — tune a single note's chord<br>`applyRegionTuning()` — tune a time range | `notationinteraction.cpp` (via `addAnalyzedTuning()`, `tuneSelection()`) |
| `notationanalysisinternal.h` | `isChordTrackStaff()` — name-based chord staff detection<br>`staffIsEligible()` — exclude drums/hidden/chord-staff staves | `notationcomposingbridgehelpers.cpp`, `notationtuningbridge.cpp`, `notationimplodebridge.cpp` |

#### The `IComposingConfiguration` Split

Configuration is exposed through **two narrow interfaces**, both IoC-registered:

| Interface | IoC-registered? | Used by |
|-----------|----------------|---------|
| `IComposingAnalysisConfiguration` | ✓ | Analysis bridge, tuning bridge, status bar, context menu, app menu, preferences model |
| `IComposingChordStaffConfiguration` | ✓ | Implode bridge, preferences model |
| `IComposingConfiguration` | ✗ | Only `ComposingConfiguration` concrete class inherits this (as a plain base, not IoC-registered) |

**Why split?** The implode bridge has no business knowing about status-bar display preferences; the analysis bridge has no business knowing about chord-staff output settings. Narrow interfaces make the dependency of each component explicit and keep the IoC registrations clean.

`IComposingConfiguration` is not registered because it inherits from both sub-interfaces, and the IoC `modularity_interfaceInfo` static member would be ambiguous with two `MODULE_GLOBAL_INTERFACE` bases. Only the two leaf interfaces are registered; `ComposingConfiguration` (the one concrete class) inherits from `IComposingConfiguration` and thereby implements both.

#### `KeySigMode` Disambiguation

`mu::engraving` defines `KeyMode` (key signature mode: MAJOR, MINOR, DORIAN, …).
`mu::composing::analysis` defines `KeySigMode` (21-mode analysis enum: Ionian, Dorian, …).

The two enums have different names, so no explicit disambiguation is needed. However,
bridge files that use `using mu::composing::analysis::KeySigMode;` alongside
`using namespace mu::engraving` should add a comment for clarity:

```cpp
using mu::composing::analysis::KeySigMode;  // disambiguate from mu::engraving::KeyMode
```

This pattern appears in `notationcomposingbridgehelpers.cpp`, `notationimplodebridge.cpp`,
and `notationtuningbridge.cpp`.

#### Adding New Bridge Functions — Checklist

1. Implement the logic in the appropriate `notation*bridge.cpp`
2. Declare in the corresponding `notation*bridge.h` in `mu::notation` namespace
3. Do **not** add declarations to any `composing/` header
4. Do **not** forward-declare engraving types in any `composing/` header
5. Add the new header to `src/notation/CMakeLists.txt`
6. Callers include the notation-side header, not the composing header

---

## 4. Existing Components — The Analysis Foundation

### 4.1 ChordAnalyzer

**File:** `src/composing/analysis/chord/chordanalyzer.h` and `chord/chordanalyzer.cpp`

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

`ChordAnalysisResult` is split into two orthogonal sub-structs (P8a):

- **`ChordIdentity`** — pitch-content properties: what notes make up the chord.
  Stable across different harmonic readings of the same voicing.
- **`ChordFunction`** — tonal-function properties: how the chord relates to the
  key. Changes when the key context changes even if the voicing is identical.

```cpp
// Extension bitmask (P8b) — replaces 17 individual boolean fields.
// Use hasExtension() / setExtension() / hasAnyNinth() / hasAnyThirteenth() helpers.
enum class Extension : uint32_t {
    MinorSeventh      = 1u << 0,
    MajorSeventh      = 1u << 1,
    DiminishedSeventh = 1u << 2,
    AddedSixth        = 1u << 3,
    NaturalNinth      = 1u << 4,
    FlatNinth         = 1u << 5,
    SharpNinth        = 1u << 6,
    NaturalEleventh   = 1u << 7,
    SharpEleventh     = 1u << 8,
    NaturalThirteenth = 1u << 9,
    FlatThirteenth    = 1u << 10,
    SharpThirteenth   = 1u << 11,
    FlatFifth         = 1u << 12,
    SharpFifth        = 1u << 13,
    SixNine           = 1u << 14,
    OmitsThird        = 1u << 15,
};

struct ChordIdentity {
    double score = 0.0;           // Raw confidence. Higher is better. Not normalized.
    int rootPc = 0;               // Root pitch class (0-11, C=0)
    int bassPc = 0;               // Bass pitch class (0-11)
    int bassTpc = -1;             // Bass TPC for enharmonic display (-1 if unknown)
    ChordQuality quality = ChordQuality::Unknown;
    uint32_t extensions = 0;      // Bitmask of Extension flags
};

struct ChordFunction {
    int degree = -1;              // Diatonic degree 0-6; -1 if non-diatonic
    bool diatonicToKey = false;   // True if all sounding pitches are diatonic
    int keyTonicPc = 0;           // Pitch class of mode tonic (0=C)
    KeySigMode keyMode = KeySigMode::Ionian;
};

struct ChordAnalysisResult {
    ChordIdentity identity;
    ChordFunction function;
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

    // P8c: optimization readiness
    ParameterBoundsMap bounds() const;   // parameter name → {min, max, isManual}
};

inline constexpr ChordAnalyzerPreferences kDefaultChordAnalyzerPreferences{};
```

The `StylePrior` commented-out code is the planned connection between
`ChordAnalyzerPreferences` and the style system (Section 6). When the style system
is implemented, the active style will populate the analyzer's preferences.

#### Public Interface

```cpp
class IChordAnalyzer {
public:
    virtual ~IChordAnalyzer() = default;
    virtual std::vector<ChordAnalysisResult> analyzeChord(
        const std::vector<ChordAnalysisTone>& tones,
        int keySignatureFifths,                         // -7 to +7
        KeySigMode keyMode,                             // detected mode (all 21 modes)
        const ChordTemporalContext* context = nullptr,  // optional preceding-chord context
        const ChordAnalyzerPreferences& prefs = kDefaultChordAnalyzerPreferences
    ) const = 0;
};

/// Default implementation: template-matching rule-based approach.
class RuleBasedChordAnalyzer : public IChordAnalyzer {
public:
    std::vector<ChordAnalysisResult> analyzeChord(...) const override;
};
```

Minimum 3 distinct pitch classes required. Returns empty vector if insufficient data.
Callers instantiate `RuleBasedChordAnalyzer{}` or hold an `IChordAnalyzer*` for
dependency injection (e.g. future ML-based analyzer).

#### Factory — `ChordAnalyzerFactory` (P4b)

```cpp
enum class ChordAnalyzerType { RuleBased };

class ChordAnalyzerFactory {
public:
    static std::unique_ptr<IChordAnalyzer> create(
        ChordAnalyzerType type = ChordAnalyzerType::RuleBased);
};
```

All notation bridge files (`notationcomposingbridge.cpp`, `notationcomposingbridgehelpers.cpp`, `notationharmonicrhythmbridge.cpp`) use `ChordAnalyzerFactory::create()` so the analyzer type is resolved through the factory rather than hard-coded at each call site. Tests that need a direct instance may use `RuleBasedChordAnalyzer{}` on the stack.

#### §4.1b — Contextual Inversion Resolution

**Problem:** The `bassNoteRootBonus` (0.65) biases vertical analysis toward choosing the
bass note as the chord root. For inverted chords (e.g. `Gm/Bb` with Bb in bass) this
produces correct bass-root readings that disagree with music21's functional notation.
74.3% of corpus disagreements have `bassIsRoot=true`. Local scoring fixes for 3-note
inversions consistently regress (see three-attempt history in Section 6).

**Solution:** Contextual bonuses applied only to non-bass-root Major/Minor candidates,
using information from neighbouring chords. Three bonuses added to `contextualBonuses()`:

| Bonus | Condition | Default |
|-------|-----------|---------|
| `stepwiseBassInversionBonus` | Bass moves by diatonic step FROM previous region | 0.5 |
| `stepwiseBassLookaheadBonus` | Bass moves by diatonic step TO next region (deferred) | 0.5 |
| `sameRootInversionBonus` | Candidate root matches previous chord's root | 0.4 |

**Safety constraints (lesson from three-attempt history):** Bonuses never fire for
Diminished, HalfDiminished, Augmented, or Suspended candidates — only Major and Minor.
The existing `inversionSuspicionMargin` / `inversionBonusReduction` mechanism is left
unchanged.

**`ChordTemporalContext` fields (§4.1b additions):**

| Field | Populated by | Status |
|-------|-------------|--------|
| `previousRootPc` | Both bridges | ✅ Active |
| `previousQuality` | Both bridges | ✅ Active |
| `previousChordAge` | — | Reserved (not yet populated) |
| `previousBassPc` | Both bridges | ✅ Active |
| `bassIsStepwiseFromPrevious` | Both bridges | ✅ Active |
| `nextRootPc` | — | Deferred (two-pass only) |
| `nextBassPc` | — | Deferred (two-pass only) |
| `bassIsStepwiseToNext` | — | Deferred (two-pass only) |
| `jazzMode` | Headless jazz path (`batch_analyze`) | ✅ Active for chord-symbol-driven corpus analysis |

`isDiatonicStep(pc1, pc2)` helper declared in `notationcomposingbridgehelpers.h` (inline).
Both bridges (`notationcomposingbridge.cpp` and `notationharmonicrhythmbridge.cpp`) populate
`previousBassPc` and compute `bassIsStepwiseFromPrevious` before each analysis call.

**Validation (20260406_122004, git `bcc0811f67`; retired Bach reference methodology):**

| Metric | Baseline | §4.1b |
|--------|----------|-------|
| Chord identity | 83.4% (3383/4058) | **50.0% (WIR structural, 2026-04-09; supersedes 83.7% onset-only/music21 figure)** |
| chord_disagree | 673 | **661** (−12) |
| bassIsRoot fraction (est.) | 74.3% | ~72.9% |
| Catalog regressions | 0 | 0 |

#### §4.1c — Regional Note Accumulation (Classical Mode)

**Problem:** Per-tick pitch-class snapshots treat all notes as equal regardless of
duration, metric position, or repetition across a region. Short passing tones receive
the same weight as sustained structural pitches.

**Solution:** Replace per-tick evidence with pitch evidence accumulated across the
entire harmonic region, weighted by three factors:

1. **Beat weight** (Pass 1): `(durationInRegion / regionDuration) × beatWeight`
   — DOWNBEAT 1.0, STRESSED 0.85, UNSTRESSED 0.75, SUBBEAT 0.5
2. **Repetition boost** (Pass 2): `weight × (1.0 + 0.3 × (distinctMetricPositions − 1))`
   for pitch classes appearing at more than one distinct metric position
3. **Cross-voice boost** (Pass 3): `weight × 1.5` for pitch classes sounding in more
   than one voice simultaneously

Harmonic boundaries are detected via **Jaccard distance** between consecutive
quarter-note window PC bitsets: `distance = 1 − |A∩B| / |A∪B|`. Threshold 0.6
(`harmonicBoundaryJaccardThreshold` in `ChordAnalyzerPreferences`).

**Sustained notes:** Notes that attack before `startTick` and are held into the
region are captured by a backward walk (matching the `collectSoundingAt` pattern).
This carry-in collection runs even when there is already a `ChordRest` segment exactly
at `startTick`, so region analysis keeps pedal/support tones that continue across beat
boundaries.

**Known gap — piano pedal sustain:** The carry-in walk intentionally preserves held
support tones, but §4.1c still treats a long sustain-pedal sonority as structurally
active for the whole region. In Romantic piano textures this can smear the evidence for
later harmonies instead of letting stale pedal support decay, so the remaining gap is a
pedal-role/decay model rather than missing note collection.

#### Technical debt — duplicate note collection paths

There are now two separate note-collection implementations feeding chord analysis:

1. `src/notation/internal/notationcomposingbridgehelpers.cpp` — canonical
  `collectRegionTones()` used by the live MuseScore notation bridge. This path has
  duration×metric weighting, repetition boost, cross-voice boost, and sustain-pedal
  tail weighting.
2. `tools/batch_analyze.cpp` — duplicate `collectRegionTones()` used by the batch tool
  for both chord-symbol (jazz) and non-jazz (classical) validation. The classical batch
  path now also uses Jaccard boundary detection plus the same smoothed regional-analysis
  flow instead of the former onset-only `collectOnsetTones()` prototype.

This removes the largest product-vs-validation mismatch, but any note-collection
improvement must still be applied in both locations. The first pedal-tail fix landed in
the notation bridge and initially had zero effect on Chopin validation because the batch
tool still used the onset-only prototype at that time.

This violates Rule 10. The correct resolution is to move the shared logic into
`src/composing/` so both consumers call one implementation. Until that refactor is
complete, any change to note collection or boundary detection must be implemented in
`src/composing/` if possible, or if not, applied to BOTH paths simultaneously with a
TODO comment referencing Rule 10.

**Resolution:** move regional note accumulation into a shared location accessible by both
the notation bridge and `batch_analyze` without introducing a notation dependency.
Candidates include:

- a new `src/composing/analysis/region/` utility that works through an abstract note
  provider interface rather than direct score traversal
- or an extracted helper API shared by both callers without pulling notation-only bridge
  dependencies into `composing`

Until this is resolved, all note-collection changes must be ported explicitly to both
active paths.

#### Region identity modes (decided 2026-04-11)

Preserve-all harmonic regions use different identity keys depending on the output mode:

**Harmonic summary mode** (status bar, analysis, tuning): region identity = root pitch
class + quality. Adjacent regions with the same root and quality are merged. Extensions,
inversions, and slash chord bass notes are secondary metadata, not identity keys.

**As-written mode** (chord track "as written"): region identity = full sonority including
extensions and bass note. Octave doublings are preserved. Adjacent regions are merged
only when the full sonority matches.

Current implementation: harmonic summary mode only. As-written mode is deferred —
requires a mode flag in the implode bridge and a separate merge pass. The chord track
octave deduplication limitation (§5.8) is the primary consequence of this deferral.

**New API:**
- `collectRegionTones(score, startTick, endTick, excludeStaves)` — implemented in
  `notationcomposingbridgehelpers.cpp`; declared in `notationcomposingbridgehelpers.h`
- `detectHarmonicBoundariesJaccard(score, startTick, endTick, excludeStaves, threshold)`
  — returns sorted vector of boundary `Fraction` ticks; first = `startTick`
- `ChordAnalysisTone` extended with 3 fields: `durationInRegion`, `distinctMetricPositions`,
  `simultaneousVoiceCount` (all initialize to 0 for backward compatibility)
- `useRegionalAccumulation()` / `setUseRegionalAccumulation()` in `IComposingAnalysisConfiguration`
  (default `true`; settings key `composing/useRegionalAccumulation`)

**Bridge wiring:** `notationharmonicrhythmbridge.cpp` branches on `useRegionalAccumulation`:
- Regional path: `detectHarmonicBoundariesJaccard` → `collectRegionTones` → `analyzeChord`
- Legacy path: per-tick PC bitset comparison (unchanged)

**Validation (20260406_151131; Bach baseline corrected 2026-04-09):**

| Metric | §4.1b | §4.1c |
|--------|-------|-------|
| Chord identity (Bach 352 chorales) | 50.0% (WIR structural, 2026-04-09; supersedes 83.7% onset-only/music21 figure) | **50.0% (WIR structural, 2026-04-09; supersedes 83.7% onset-only/music21 figure)** |
| chord_disagree | 661 | **661** (unchanged) |
| Beethoven BIR% of disagreements | 59.4% | **57.3%** (−2.1 pp) |
| Catalog regressions | 0 | 0 |

#### Temporal context — `ChordTemporalContext` vs future `TemporalContext` (P4b)

`ChordTemporalContext` carries the **immediately preceding chord's** root, quality, and
bass, plus stepwise-motion flags — sufficient for root-continuity, resolution-bias, and
contextual inversion scoring (§4.1b). It is **not** a full progression context. A future
`TemporalContext` will carry the full recent progression (chord sequence, cadence history,
secondary dominants) once secondary dominant analysis (§5.6) is implemented. Keep the
names distinct.

#### Design boundary — vertical sonority vs functional/contextual harmony

`RuleBasedChordAnalyzer` is a **vertical sonority analyzer**: it identifies what chord
is implied by the set of simultaneously sounding notes at a single point in time. It
does not perform functional harmonic analysis (Roman-numeral reductions, cadence
detection, tonicization, secondary dominants) or contextual annotation (what role this
chord plays in the surrounding progression).

This boundary is intentional and has been validated empirically. Corpus analysis against
DCML annotations (four corpora, 2026-04-06) established a retired onset-only/music21
comparison ceiling of ~83–84% for Bach chorales; the official Bach structural baseline is now
50.0% against local When in Rome RomanText annotations (2026-04-09). The remaining divergence is not
an analyzer defect — it represents legitimate cases where:

- **3-note triads in inversion** (bass ≠ functional root): DCML annotates the
  functional root; vertical analysis defaults to bass=root. For bare triads this
  cannot be resolved from local note content alone. 95.8% of all disagreements
  with BIR (bass-is-root) errors are 3-note triads.
- **Functional prolongation**: DCML may annotate a passing or neighboring chord as
  part of a broader harmonic region (e.g. a cadential 6-4 as dominant), while vertical
  analysis identifies the sounding notes independently.

Improving beyond ~84% requires a **contextual harmony layer** (Phase 2) that consumes
a sequence of `ChordAnalysisResult` outputs and applies voice-leading, cadence, and
harmonic-sequence reasoning. That layer is explicitly out of Phase 1 scope. Do not
attempt to improve corpus agreement by adding heuristics to `RuleBasedChordAnalyzer`
that embed contextual assumptions — keep the vertical/contextual boundary clean.

### 4.2 KeyModeAnalyzer

**File:** `src/composing/analysis/key/keymodeanalyzer.h` and `key/keymodeanalyzer.cpp`

**Purpose:** Infers the most likely key and mode from a temporal window of pitch
contexts. Uses duration weight, metric weight, and bass status to give more
influence to harmonically significant notes. Returns up to three ranked candidates.

**Algorithm:** Scores all 12 possible tonics against all **21 modes** (7 diatonic +
7 melodic minor family + 7 harmonic minor family = 252 candidates) using six orthogonal
helper functions:
- `scoreScaleMembership` — how well the pitch classes fit the candidate scale,
  cross-referenced against the notated key-signature scale
- `scoreTriadEvidence` — how strongly the tonic triad is present (tonic 1.6×,
  third 0.7×, fifth 0.5×, leading tone 0.4×; complete triad bonus 2.5)
- `scoreCharacteristicPitch` — boost/penalty for the characteristic pitch(es) that
  most distinguish each mode from its closest neighbor (e.g. Dorian's raised 6th vs
  Aeolian; harmonic minor's raised 7th; multiple compound conditions for non-diatonic modes)
- `scoreTrueLeadingTone` — bonus when the semitone below the tonic is present,
  regardless of diatonicism (chromatic leading tones still signal the tonic strongly)
- `scoreKeySignatureProximity` — preference for keys close to the notated key
  signature (−0.6 per fifth of distance)
- `scoreModePrior` — **21 independent additive priors**, one per mode, user-configurable
  via `IComposingAnalysisConfiguration::modePrior{ModeName}()`; defaults reflect Western
  tonal frequency (Ionian=+1.20, Aeolian=+1.00, down to Altered=−3.50)
- `applyRelativePairDisambiguation` — post-hoc score mutations for the relative
  major/minor pair sharing a key signature (four documented cases; see implementation)

The key-signature path uses a separate focussed `tonalCenterScore` formula for the
final same-key-signature family decision, independent of the main scoring weights so
both can be tuned without cross-interference. For diatonic family decisions, tonal-
centre disambiguation is now guarded by the raw candidate score: it may break close
same-key-signature ties, but it must not overturn a materially stronger raw winner.

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

**Important:** In the current calling code, `durationWeight`, `beatWeight`, and
`isBass` are populated from the score. The bridge collects a 16-beat lookback +
8-beat lookahead window with exponential time decay (0.7× per measure) and
beat-type weights from MuseScore's `BeatType` enum.

#### Output — `KeyModeAnalysisResult`

```cpp
enum class KeySigMode {
    // Diatonic family (7)
    Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian,
    // Melodic minor family (7)
    MelodicMinor, DorianB2, LydianAugmented, LydianDominant,
    MixolydianB6, AeolianB5, Altered,
    // Harmonic minor family (7)
    HarmonicMinor, LocrianSharp6, IonianSharp5, DorianSharp4,
    PhrygianDominant, LydianSharp2, AlteredDomBB7,
};  // 21 modes total

**Harmonic major modes — deferred:** The harmonic major scale and its 7 modes were
considered for inclusion in this expansion but deferred. Harmonic major modes are
significantly rarer as tonal centers than melodic and harmonic minor modes, and the
validation corpus is unlikely to calibrate them well. They can be added as a future
extension following the same pattern as the melodic and harmonic minor families.

struct KeyModeAnalysisResult {
    int keySignatureFifths = 0;             // Resolved key signature (-7..+7, Ionian convention)
    KeySigMode mode = KeySigMode::Ionian;   // Detected mode
    int tonicPc = 0;                        // Pitch class of the mode's tonic (0=C, 2=D, etc.)
    double score = 0.0;                     // Raw confidence score; higher is better
    double normalizedConfidence = 0.0;      // 0.0–1.0 via sigmoid on score gap to runner-up
};
```

All 21 modes are active. `normalizedConfidence` is computed via sigmoid on the score
gap between rank-1 and rank-2 candidates (midpoint 2.0, steepness 1.5). The chord
staff uses this to annotate uncertain detections with "?" or "(?)".

#### Tunable Parameters — `KeyModeAnalyzerPreferences`

All scoring weights and thresholds are collected in `KeyModeAnalyzerPreferences`.
See `keymodeanalyzer.h` for the full struct with documentation. Key groups:

- **Note weight caps** — `noteWeightCap`, `bassMultiplier`
- **Scale membership** — four case weights (`scaleScoreInBoth`, etc.)
- **Tonal centre** — per-tone weights and bonus/penalty for complete triad
- **Characteristic pitch** — `characteristicPitchBoost`, `characteristicPitchPenalty`
- **True leading tone** — `trueLeadingToneBoost`
- **Mode priors** — `modePriorIonian` through `modePriorAlteredDomBB7` (21 independent
  priors); populated from user preferences via `IComposingAnalysisConfiguration::modePrior*()`
  in the bridge; replaces former 4-tier grouping
- **Tonal-centre comparison** — independent weights for the same-key-signature
  family decision (`tonalCenter*`); diatonic family selection also applies a
  raw-score guard before tonal-centre can overturn the current raw winner
- **Key-signature proximity** — `keySignatureDistancePenalty`
- **Disambiguation** — `disambiguationTriadBonus`, `disambiguationTriadCost`,
  `disambiguationTonicBonus`
- **Confidence sigmoid** — `confidenceSigmoidMidpoint`, `confidenceSigmoidSteepness`
- **Beat-type weights** — `beatWeightDownbeat` through `beatWeightSubbeat`

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

#### §4.1c Part 2 — Jazz Mode (chord-symbol-driven boundaries)

**Status: Implemented (2026-04-06).** Bridge: `analyzeHarmonicRhythmJazz()` + `scoreHasChordSymbols()` + `collectChordSymbolBoundaries()` in `notationharmonicrhythmbridge.cpp` / `notationcomposingbridgehelpers.cpp`. Batch: `analyzeScoreJazz()` + `scoreHasChordSymbols()` in `batch_analyze.cpp`. `HarmonicRegion` extended with `fromChordSymbol` and `writtenRootPc`. FiloSax/FiloBass validation unblocked.

**2026-04-08 follow-up:** Temporary jazz-specific scoring experiments were evaluated
and then reverted. `ChordTemporalContext::jazzMode` is retained only as a context
flag for chord-symbol-driven analysis paths and future diagnostics; no accepted
jazz-only scoring adjustments remain in the analyzer.

##### Jazz validation findings (2026-04-08)

A synthetic bass injection experiment confirmed that the vertical analyzer identifies
jazz chords correctly at near-perfect rates when given complete tonal material.

Experiment: `batch_analyze --inject-written-root` adds a synthetic bass tone at the
written chord symbol root before calling `analyzeChord()`. This simulates the bass
player's root note that is present in performance but absent from lead-sheet and
horn-section scores.

Results:

- Rampageswing (horn-only): 39.8% → 98.3%
- Omnibook (melody-only): 18.0% → 99.9%

Conclusion: the 40–60% agreement gap on available jazz corpora is explained by
missing bass/root material in the scores, not by a scoring-model deficiency. The
vertical analyzer requires complete tonal material (bass + harmony voices) to identify
chords reliably.

Jazz validation therefore requires scores with written-out bass and piano voicings.
Lead sheets, horn arrangements, and solo transcriptions are incomplete for this
purpose and should not be treated as analyzer accuracy benchmarks.

The `--inject-written-root` flag in `batch_analyze` provides a diagnostic upper bound.
It is not a production path: chord symbols must never be used as analyzer input in
production because they are user content and may be incorrect.

Known gap: no freely available corpus of jazz scores with complete written-out bass
and piano voicings has yet been found. This is an open corpus-availability problem,
not an analyzer design problem.

### §4.1f — Future: Authoritative Chord Symbol Mode

**Status:** Design note only. Not planned for immediate implementation.

#### Motivation

Chord symbols, Roman numerals, and Nashville numbers already present in a score may
carry different levels of authority depending on context:

- **As-is analysis:** The current analyzer reads notes and infers what chord they
  imply. Written chord symbols are comparison metadata only.
- **To-be annotation:** A composer or arranger may enter chord symbols representing
  the intended harmony, which the written notes may only partially realize (e.g. a
  lead sheet where the pianist improvises the voicing, or an arrangement where the
  bass is tacet).

In the to-be case, the written chord symbol is the ground truth — not the notes.
The analyzer's job shifts from "identify what the notes imply" to "confirm or
annotate what the composer declared."

#### Design

Add a user preference: `trustWrittenChordSymbols` (bool, default false)

When enabled, written chord symbols are treated as authoritative harmonic
declarations rather than comparison metadata. The analyzer uses them as strong
priors or direct answers rather than inferring from notes alone.

Not all chord symbols in a score need to be authoritative. A per-symbol mechanism
is needed to distinguish intentional declarations from approximate or placeholder
annotations.

#### The play/no-play flag as authority marker

MuseScore already exposes a play flag on chord symbols (`Harmony::play()`).
Currently used to suppress audio playback of chord symbol voicings.

Proposed dual use: when `trustWrittenChordSymbols` is enabled, only chord symbols
with `play = true` are treated as authoritative. Symbols with `play = false`
remain comparison metadata only.

This gives the user per-symbol control over which chord symbols the analyzer should
trust, using an existing UI mechanism that is already accessible in MuseScore's
Properties panel. No new UI needed.

#### Relationship to current jazz mode

The current §4.1c jazz mode uses chord symbol positions as region boundaries and
stores written roots as comparison metadata (`writtenRootPc`, `fromChordSymbol`).
This is correct for as-is analysis and must not change.

The authoritative mode is an additional layer that activates only when
`trustWrittenChordSymbols` is enabled. Both modes can coexist:

- Boundaries always come from chord symbol positions when chord symbols are present
- Root identification comes from notes (as-is) or from the symbol (to-be)
  depending on the preference

#### Diagnostic evidence

The synthetic bass injection experiment (2026-04-08) demonstrated that treating
written roots as authoritative (injecting the written root as a synthetic bass
tone) raises Rampageswing agreement from 39.8% to 98.3% and Omnibook from 18.0%
to 99.9%. This confirms that the authoritative mode would be highly effective when
the written chord symbols are correct — and shows the risk when they are not.

#### Implementation prerequisites

- `Harmony::play()` accessor must be accessible from the bridge layer (check
  current availability)
- `IComposingAnalysisConfiguration::trustWrittenChordSymbols()` preference wired
  through config → QML
- Bridge: when trust mode active and symbol has `play=true`, inject written
  root/quality as primary analysis result rather than running note-based analyzer
- Validation: run on a curated small ground truth set of jazz standards with
  verified chord symbols before enabling by default for any preset

##### Problem

The classical §4.1c Jaccard boundary detection is unsuitable for jazz scores because:

1. Jazz scores already contain explicit harmonic annotations — the written chord symbols
  (e.g. `Dm7`, `G7`, `CMaj7`) are useful boundary hints and comparison metadata.
  They are not the analysis result. Inferring region boundaries from pitch-class
  Jaccard distance is often redundant and error-prone when explicit chord-symbol
  boundaries are already present.
2. Jazz harmony uses voicings where the written root is frequently absent from the sounding
   notes (shell voicings: root + 3rd + 7th only; rootless voicings). The vertical note-set
   approach systematically misidentifies these.
3. Monophonic melodic lines (saxophone, bass) cannot produce the 3 simultaneous pitch
   classes required by the current 3-PC minimum.

##### Detection gate

Jazz mode activates automatically when **chord symbols (`Harmony` elements) are present
in the score**. Detection algorithm:

```cpp
// In notationharmonicrhythmbridge.cpp (or a new notationjazzrhythmbridge.cpp)
bool scoreHasChordSymbols(const Score* score,
                          const Fraction& startTick,
                          const Fraction& endTick) {
    for (const Segment* s = score->tick2segment(startTick, true, SegmentType::ChordRest);
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        for (const EngravingItem* ann : s->annotations()) {
            if (ann->isHarmony()) return true;
        }
    }
    return false;
}
```

This is a scan over `segment->annotations()` — O(n_segments). Called once per
`analyzeHarmonicRhythm()` invocation before the main boundary-detection loop.
If `true`, the jazz path runs; otherwise the classical Jaccard path runs.

##### Jazz boundary extraction

Instead of Jaccard distance, region boundaries are the ticks of `Harmony` elements.
Each `Harmony` on a `ChordRest` segment defines a new harmonic region starting at
that segment's tick and ending at the next `Harmony` tick (or `endTick`).

```cpp
std::vector<Fraction> collectChordSymbolBoundaries(
    const Score* score,
    const Fraction& startTick,
    const Fraction& endTick)
{
    std::vector<Fraction> ticks;
    ticks.push_back(startTick);
    for (const Segment* s = score->tick2segment(startTick, true, SegmentType::ChordRest);
         s && s->tick() < endTick;
         s = s->next1(SegmentType::ChordRest)) {
        for (const EngravingItem* ann : s->annotations()) {
            if (ann->isHarmony() && s->tick() > startTick) {
                ticks.push_back(s->tick());
                break;
            }
        }
    }
    return ticks;  // already sorted
}
```

##### Written root as comparison metadata

For jazz regions, the written root pitch class is read from `Harmony::rootTpc()` and
stored as comparison metadata only. The analyzed root still comes from applying the
chord analyzer to `collectRegionTones()` within the chord-symbol-defined region.

```cpp
const Harmony* h = toHarmony(ann);
int writtenRootPc = tpc2pc(h->rootTpc());

auto tones = collectRegionTones(score, regionStart, regionEnd, excludeStaves);
auto results = chordAnalyzer->analyzeChord(tones, keyFifths, keyMode, &temporalCtx);

region.chordResult = results.empty() ? ChordAnalysisResult{} : results.front();
region.writtenRootPc = writtenRootPc;
region.fromChordSymbol = true;
```

This keeps the analyzer non-circular: the score's written harmony can be used for
boundary selection, weak contextual priors, and agreement/disagreement display,
but it must not be copied back into `chordResult`.

Outside this explicit jazz-mode boundary path, existing Harmony annotations are
strictly output/comparison metadata. In notation-side status-bar, context-menu,
and chord-track inference for note-driven workflows, existing Roman, Nashville,
or standard chord symbols on source staves must never be used as harmonic input
or even as boundary hints. Those user-facing paths infer from notes only.

##### Integration point

`analyzeHarmonicRhythm()` in `notationharmonicrhythmbridge.cpp` gains a third branch:

```cpp
const bool hasChordSymbols = scoreHasChordSymbols(score, startTick, endTick);

if (hasChordSymbols) {
  // §4.
    return analyzeHarmonicRhythmJazz(score, startTick, endTick, excludeStaves);
} else if (useRegional) {
    // §4.1c Classical path — Jaccard boundaries + regional accumulation
    ...
} else {
    // Legacy path — per-tick bitset
    ...
}
```

The jazz path can live in `notationharmonicrhythmbridge.cpp` as a static helper,
or in a new `notationjazzrhythmbridge.cpp` if it grows large.

##### Files to touch

| File | Change |
|------|--------|
| `notationharmonicrhythmbridge.cpp` | Add `scoreHasChordSymbols()`, third branch in `analyzeHarmonicRhythm()` |
| `notationcomposingbridgehelpers.h/.cpp` | Add `collectChordSymbolBoundaries()` |
| `engraving/dom/harmony.h` | Read-only — `rootTpc()`, `bassTpc()`, `parsedForm()` |
| `HarmonicRegion` struct | Add `chordSymbolSource` flag (or keep implicit) |
| Tests | New `P7_JazzMode` test suite in `synthetic_tests.cpp` |

No changes to `ChordAnalyzer`, `KeyModeAnalyzer`, or any composing-module files.
The jazz path is entirely in the bridge layer, consistent with principle 2.2.

##### Open questions before implementation

1. **Quality mapping completeness:** The `ParsedChord` kind strings are not fully
   documented in a single place. Need to enumerate all kinds in `chordlist.xml` and
   map each to `ChordQuality`. Low risk — `Unknown` is a safe fallback.
2. **Multi-staff chord symbols:** If chord symbols appear on multiple staves
   (e.g. piano + chord staff), pick the one on the lowest non-excluded staff at each
   tick. Duplicates at the same tick collapse to one region.
3. **Chord symbol gaps:** Some jazz scores have chord symbols only on section starts,
   not every chord change. The `collectChordSymbolBoundaries()` function already handles
   this correctly — a region with no chord symbol simply extends from the previous one.
4. **Interaction with `useRegionalAccumulation`:** The jazz detection gate
   (`hasChordSymbols`) takes priority over `useRegionalAccumulation`. A score with
   chord symbols always uses the jazz path, regardless of the preference setting.

#### §4.1d Monophonic Chord Inference — Provisional Phased Plan

**Status:** provisional design note, updated after Phase 1a validation.
Phase 1a validation completed 2026-04-07, git `0587ec27e1`, on the Charlie
Parker Omnibook (50 public LORIA MusicXML solos with embedded chord symbols).
Result: **4454/4454 comparable regions = 100.0% root agreement**.

This validates the existing §4.1c chord-symbol-driven path, not independent
monophonic inference. In Phase 1a the written root is read directly from the
embedded chord symbols, not inferred from melody notes. The result confirms:
- chord-symbol boundaries are detected correctly in all 50 solos
- `Harmony` elements are parsed correctly from the MusicXML files
- jazz mode fires reliably on monophonic saxophone scores

Critical Phase 1a finding from the `noteCount` distribution:
- `noteCount = 0`: 1581 regions (35.4%)
- `noteCount = 1`: 2873 regions (64.4%)
- `noteCount >= 2`: 0 regions

Implication for Phase 1b: saxophone solos in this validation set provide at
most one sounded note per chord-symbol region. Independent chord inference from
isolated single-note regions is therefore not viable. Phase 1b must use bounded
group expansion across multiple consecutive regions, rather than attempting to
resolve chords from one-note local windows. This makes the bounded-expansion
design necessary, not optional.

The remaining monophonic problem is now narrowed to inference without chord
symbols: e.g. C.P.E. Bach keyboard, Bach suites, and arpeggiated piano or other
thin-texture repertories.

**End-state architecture:**
Monophonic and arpeggiated chord inference should use a separate internal engine
from the current vertical chord analyzer, but both should be hidden behind one
unified orchestration layer.

This separation is necessary because the two engines use different evidence
models:
- the vertical engine reasons from simultaneous pitch-class evidence, bass-root
  relations, and sonority-template matching
- the monophonic engine must reason from temporal accumulation, structural-note
  weighting, subset matching, and implied rather than explicit simultaneity

The unified orchestration layer should expose one harmonic-analysis entry point
to the rest of the system. Status-bar analysis, chord-staff population, tuning,
and validation tooling should not need to know which internal engine produced
the result.

**Shared context:**
Key/mode inference remains shared. The existing key/mode analyzer already
provides a broader temporal prior than chord identity and should be reused by
both vertical and monophonic chord inference. A separate monophonic mode
analyzer is not planned for the initial implementation.

**Score metadata:**
Fields such as `fromChordSymbol` and `writtenRootPc` are score metadata rather
than engine metadata. The unified orchestration layer must preserve them
regardless of which analysis engine produced the winning harmonic result.

### Phase 1a — Validate Existing Chord-Symbol-Driven Path

Phase 1a is now complete.

Corpus: Charlie Parker Omnibook (50 solos, public LORIA MusicXML).

Run result:
- 50/50 files loaded successfully
- 4464 total regions
- 3361 comparable `fromChordSymbol` regions with an analyzed chord
- 605/3361 written-root vs analyzed-root agreement = **18.0%**
- 1103 `fromChordSymbol` regions produced no analyzed chord (`hasAnalyzedChord=false`)
- 0 zero-region solos

Interpretation:
- the previous 100% Omnibook result was invalid because the old jazz path copied
  the written chord-symbol root into the analysis result
- with the corrected non-circular path, the current vertical chord analyzer does
  **not** solve the annotated monophonic jazz case, even when the written chord
  symbols supply exact region boundaries
- this run validates `Harmony` parsing and regionization, but it falsifies the
  assumption that boundary-correct regional accumulation is enough on its own

The corrected Phase 1a note-count evidence is:
- all `fromChordSymbol` regions: `0: 268`, `1: 349`, `2: 476`, `3: 691`, `4: 1088`,
  `5: 610`, `6: 496`, `7: 341`, `8: 110`, `9: 25`, `10: 5`, `11: 5`
- 1103 regions (24.7%) remain unanalyzable by the current vertical analyzer
  because they produce fewer than 3 distinct pitch classes
- the comparable subset is not especially sparse: most analyzable regions contain
  3-6 distinct pitch classes, yet agreement is still only 18.0%

The dominant mismatch pattern is functional reinterpretation rather than total
absence of evidence: written `F` is often analyzed as `C`, `Am`, or `Gm`; written
`Bb` as `F`, `Gm`, `Dm`, or `C`; written `C` as `G` or `Am`.

Therefore the next monophonic step cannot be framed merely as bounded expansion
to overcome 0-1 note sparsity. The current vertical analyzer's evidence model is
itself a poor fit for monophonic jazz melody, even when region boundaries are
supplied correctly. Bounded expansion may still help the 1103 sparse regions, but
it is not sufficient to explain or solve the remaining disagreement.

### Phase 1b — Minimal Monophonic Fallback Without Chord Symbols

If Phase 1a shows that annotated monophonic material is largely handled, the
next step is a minimal monophonic fallback for unannotated single-line or
arpeggiated passages.

This phase should remain intentionally modest:
- simple boundary sources first
- subset-based chord matching rather than full simultaneity requirements
- bounded local-context expansion only when confidence is weak
- lightweight smoothing heuristics rather than full sequence decoding

**Boundary-source selection in Phase 1b:**
Boundary choice should be repertoire- and texture-aware rather than globally
ordered.

Use:
1. written chord symbols when present
2. fine-grained Jaccard-style harmonic-boundary detection for faster harmonic
   rhythm or classical material
3. beat- or bar-quantized boundaries only as a simpler fallback for slower
   harmonic-rhythm contexts

Bar-quantized boundaries are intentionally not the default fallback for
classical keyboard material, where within-bar harmony changes are common.

**Subset-based matching in Phase 1b:**
Phase 1b does not require three simultaneous pitch classes, but it also must not
treat arbitrary one-note fragments as sufficient chord evidence.

Initial rule:
- 2 distinct pitch classes may nominate a candidate set
- 2-PC evidence alone must not finalize a chord without contextual support
- 1-PC evidence is insufficient for independent chord resolution and may only
  participate in continuity-preserving abstention logic

This keeps Phase 1b permissive enough to analyze broken-chord passages while
avoiding over-interpretation of isolated tones.

**Bounded expansion in Phase 1b:**
Chord identity should remain local. When a local group is too weak to resolve,
the analyzer may expand by one neighboring region and re-score. Expansion is
bounded and should stop when:
- confidence crosses threshold
- top-vs-second margin crosses threshold
- the same winner survives repeated expansion
- the hard expansion cap is reached

**Lightweight smoothing in Phase 1b:**
Phase 1b should not implement full dynamic-programming or Viterbi decoding.
Instead, it should use a simple continuity heuristic.

Example intent:
if the same chord wins strongly in adjacent groups, do not let one weak middle
group overturn it unless the competing candidate wins by a substantial margin.

These terms must be implemented as tunable parameters rather than prose-only
rules.

**Initial Phase 1b calibration parameters:**
- `monoMinSubsetDistinctPcs` — initial default: 2
- `monoWeakGroupConfidenceMax` — upper bound below which a local group is
  treated as weak
- `monoAdjacentAgreementMinConfidence` — minimum confidence required for the
  neighboring groups to count as strong agreement
- `monoWeakGroupOverrideMargin` — minimum margin required for a weak middle
  group to overturn adjacent agreement
- `monoExpansionMaxGroups` — hard cap on neighboring-group expansion

As with other analyzer parameters, these should follow the existing
preferences-and-`bounds()` pattern and remain explicitly calibratable.

### Phase 2 — Full Monophonic Engine

The full monophonic engine is still the intended long-term design, but it
should follow Phase 1 validation rather than precede it.

The full engine should add:
- dedicated harmonic grouping from melodic structure
- boundary scoring from duration, metric stress, rests, leaps, register shifts,
  and pitch-class novelty
- chord inference from weighted subsets rather than vertical simultaneity
- sequence-level smoothing across neighboring groups
- compound-melody handling for implied multiple voices in one line
- explicit confidence calibration against the vertical engine

The local grouping problem is intentionally deferred to Phase 2 because it is
the hardest part of monophonic inference.

### Unified Orchestration Layer

The outer harmonic-analysis pipeline remains unified and selects among internal
strategies.

The orchestration layer should:
1. gather texture facts for the requested span
2. resolve shared key/mode prior
3. run vertical analysis on the full texture where appropriate
4. run monophonic analysis on individual staves or voices where appropriate
5. compare calibrated confidence rather than raw internal scores
6. return one ranked harmonic result list
7. abstain when neither engine is sufficiently reliable

**Mixed texture — explicit Phase 2 open question:**
The most common unresolved orchestration problem is staff-level or voice-level
mixed texture. A single passage may contain vertical evidence on one staff and
arpeggiated or single-line evidence on another. The orchestrator must therefore
eventually decide which staves or voices receive which analysis treatment.

This is not required for Phase 1, but it is an explicit Phase 2 design question
and should not be treated as solved by piece-level texture classification.

### Confidence and Abstention

The unified layer must not compare vertical and monophonic raw scores directly.
The two engines use different evidence models and therefore require explicit
confidence calibration.

This remains an open design problem. Acceptable solutions include:
- held-out corpus-based calibration
- normalized confidence derived from score margin, coverage, and texture facts
- a combination of both

Abstention is a first-class outcome. It is preferable to emit no chord result
than to emit a low-confidence result that later drives annotation or tuning
incorrectly.

### Interaction with Existing Temporal Context

The monophonic path should reuse the same broad contextual ideas already used by
the vertical path:
- harmonic continuation
- local stability versus change
- cadence-like expectation
- key/mode compatibility
- continuity bonuses where musically justified

This does not imply identical scoring formulas, but it does mean both engines
should live inside one coherent harmonic-analysis framework rather than evolve
as unrelated systems.

### Implementation Priority

**Immediate priority:**
Run Phase 1a validation on annotated monophonic jazz material and let the corpus
results determine whether a dedicated Phase 1b fallback is necessary.

**Next priority:**
If Phase 1a leaves clear failures on unannotated single-line passages, implement
a minimal Phase 1b monophonic fallback with explicit thresholds and bounded
behavior.

**Later priority:**
Implement the full monophonic engine for non-annotated and compound-melody
repertoires.

This ordering is intentional: it targets the fastest corpus-quality gains first
while preserving the correct long-term architecture.

#### Known limitation — dominant seventh / Mixolydian ambiguity

A dominant seventh chord (major triad + minor seventh) is the characteristic chord of
Mixolydian mode. When such a chord appears in isolation or without sufficient surrounding
diatonic context, the key analyzer may briefly declare Mixolydian even in a major-key
passage. This produces false-positive Mixolydian detections (observed in Grieg corpus
validation 2026-04-06: 32 cases / ~7% of disagreements).

This is **not a prior calibration problem**. Adjusting the Mixolydian prior would either
suppress genuine Mixolydian detection (lower prior) or increase false positives (higher
prior). The correct fix is requiring more sustained evidence of the lowered 7th scale
degree before declaring Mixolydian — an evidence-threshold improvement in `KeyModeAnalyzer`
scoring, deferred to a future session.

The same structural ambiguity applies to the Lydian raised 4th (an augmented fourth
interval may appear briefly in major passages) but at much lower false-positive rates
(12 cases in Grieg vs 32 for Mixolydian) because the raised 4th is less common in
incidental voice leading than the dominant seventh.

**Validated correct behaviour:** Lydian detection in Chopin (4.2% of regions) and
Grieg (11.9%) reflects genuine raised-4th passages. Dorian detection (5.2% Grieg,
5.9% Chopin) similarly reflects real modal content. The Mixolydian false-positive
rate (7%) is a known, bounded limitation — not evidence of a miscalibrated prior.

### 4.3 ChordSymbolFormatter

**File:** `src/composing/analysis/chordanalyzer.h` (namespace within)

**Purpose:** Formats `ChordAnalysisResult` into display strings. Kept separate from
`ChordAnalyzer` so the analysis layer remains display-agnostic. This separation must
be maintained throughout the codebase — analysis produces data, formatters produce strings.

```cpp
namespace ChordSymbolFormatter {

    // Note spelling convention for chord symbol root and bass names.
    // Mirrors NoteSpellingType in src/engraving/types/types.h.
    enum class NoteSpelling { Standard, German, GermanPure };

    // Display options — locale/notation-style concerns kept separate from analysis.
    struct Options {
        NoteSpelling spelling = NoteSpelling::Standard;
    };
    inline constexpr Options kDefaultOptions{};

    // "Cmaj7", "Fm7/Ab", "Bdim7" etc.
    std::string formatSymbol(const ChordAnalysisResult& result, int keySignatureFifths,
                             const Options& opts = kDefaultOptions);

    // "IM7", "ii7", "V7/3", "viiø7" etc.
    // Non-diatonic roots generate chromatic numerals: "♭VII", "♭III7", "♭VIM7" etc.
    // Returns "" only when the root cannot be mapped at all (should not occur in
    // standard 12-tone music).  The result stores keyTonicPc and keyMode so no
    // extra parameters are needed.
    std::string formatRomanNumeral(const ChordAnalysisResult& result);
}
```

Display options (`Options`) live in `ChordSymbolFormatter`, not in
`ChordAnalyzerPreferences`, enforcing the analysis/display separation (principle 2.3).

**Note naming convention:** Root and bass note names in chord symbol output
respect the score's chord symbol spelling preference (Format → Style → Chord
Symbols). The analysis layer implements a self-contained `NoteSpelling` enum
`{Standard, German, GermanPure}` — defined in `chordanalyzer.h`, mirroring
`NoteSpellingType` in `src/engraving/types/types.h`. The bridge reads
`Sid::chordSymbolSpelling` from the score style via `scoreNoteSpelling()`
(defined in `notationcomposingbridgehelpers.cpp`) and maps it to
`ChordSymbolFormatter::Options::spelling`. German mapping mirrors
`tpc2name()` GERMAN case (`pitchspelling.cpp:343-356`): B natural → "H",
Bb → "B". All other note names are unchanged. Solfeggio and French map to
Standard (not yet supported in chord symbol output). Roman numerals and
Nashville numbers do not use note names — they use degree integers and
accidental tokens — so the spelling setting does not affect them.

**Roman numeral scope:** The formatter emits Roman numerals up to the 7th level
(e.g. `I7`, `IM7`, `iø7`). Extensions beyond the 7th (9th, 11th, 13th) are not
yet emitted. Non-diatonic roots produce chromatic numerals by computing semitone
distance from the mode tonic and prefixing with ♭ or ♯ as appropriate (preferring
flat names). The quality/extension suffix is reused from the diatonic path. The
test catalog covers the 7th level only; extending it is a natural future increment.

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
  ("IM7"), figured bass (for baroque contexts — see note below)
- *Spelling conventions:* American ("maj7", "m7b5"), German/Nordic (H/B naming),
  Berklee/jazz ("Δ7", "ø7"), classical (augmented sixth notation)
- *Symbol vocabulary:* half-diminished ø vs "m7b5" vs "ø7"; major seventh Δ vs
  "maj7" vs "M7"; augmented "+" vs "aug"

When `IChordSymbolFormatter` is introduced, `ChordSymbolFormatter::Options` becomes
its configuration struct — the migration path is already established.

#### Note on figured bass

Figured bass (basso continuo) is interval notation above a bass note rather than a
chord name — e.g. "6" = first inversion triad, "6/4" = second inversion, "7" = root
position seventh.  It is architecturally simpler than chord symbols in one critical
respect: **it requires no root detection**.  The algorithm is:

1. Identify the bass note (lowest sounding pitch — already `ChordAnalysisTone::isBass`).
2. Compute each upper tone's interval above the bass, reduced to within one octave.
3. Convert to diatonic scale degrees using TPC spelling and `keySignatureFifths`.
4. Apply the standard omission table (root position triad → nothing; first inversion →
   "6"; second inversion → "6/4"; root position seventh → "7"; etc.).
5. Prefix accidentals (♭ ♯ ♮) where a tone deviates from the key signature.

This can be derived directly from the raw `ChordAnalysisTone` input — `ChordAnalysisResult`
is not required.  Importantly, figured bass annotates *all* sounding pitches including
suspensions and passing tones, which is actually easier than chord symbol analysis (no
need to distinguish chord tones from non-chord tones).  The only tricky parts are the
omission convention table and enharmonically-correct accidental spelling, both of which
are straightforward given TPC data and `keySignatureFifths`.

Figured bass generation is feasible with the current analysis infrastructure and would
work even for sonorities with fewer than 3 distinct pitch classes (where chord symbol
analysis returns empty).  It is not currently planned but is noted here because the
prerequisite data is already present.

### 4.3a Voicing Helpers

**File:** `src/composing/analysis/chordanalyzer.h` (declared) and `chordanalyzer.cpp`
(defined)

Two helpers support chord track population (§11.5):

```cpp
struct ClosePositionVoicing {
    int bassPitch = -1;              // Root MIDI pitch in C2–C3 range (-1 = empty)
    std::vector<int> treblePitches;  // Upper chord tones in C4–C5 close position
};

ClosePositionVoicing closePositionVoicing(const ChordAnalysisResult& result);
std::vector<int> chordTonePitchClasses(const ChordAnalysisResult& result);
```

`closePositionVoicing()` produces a keyboard-reduction voicing: root in bass
register (C2–C3), remaining chord tones stacked ascending above C4 within one
octave.  Returns empty voicing for `ChordQuality::Unknown`.

`chordTonePitchClasses()` derives the canonical pitch-class set from an analysis
result — root first, then remaining tones ascending.  Reflects the idealized chord
(quality + extensions), not a transcription of what was sounding.  Used when the
chord track is set to show canonical tones rather than collected sounding tones.

### 4.3b HarmonicRhythm

**Files:**
- `src/composing/analysis/region/harmonicrhythm.h` — `HarmonicRegion` struct (pure composing type, no engraving dependency)
- `src/notation/internal/notationharmonicrhythmbridge.h/.cpp` — `analyzeHarmonicRhythm()` declaration and definition
- `src/notation/internal/notationcomposingbridgehelpers.h/.cpp` — shared bridge helpers used by both bridges
- `src/notation/internal/notationimplodebridge.h/.cpp` — `populateChordTrack()` declaration and definition

The `HarmonicRegion` struct lives in the composing module (no engraving include needed); the functions that consume `Score*` / `Fraction` are bridge functions in `mu::notation`:

```cpp
// composing/analysis/harmonicrhythm.h
namespace mu::composing::analysis {
struct HarmonicRegion {
    int startTick = 0;                    // Raw tick integer (first tick of region)
    int endTick = 0;                      // First tick of next region (exclusive)
    ChordAnalysisResult chordResult;      // Root, quality, extensions, degree
    KeyModeAnalysisResult keyModeResult;  // Key and mode context
    std::vector<ChordAnalysisTone> tones; // Sounding tones that produced the analysis
};
} // namespace mu::composing::analysis

// notation/internal/notationcomposingbridge.h
namespace mu::notation {
std::vector<mu::composing::analysis::HarmonicRegion> analyzeHarmonicRhythm(
    const mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    const std::set<size_t>& excludeStaves = {});
} // namespace mu::notation

// notation/internal/notationimplodebridge.h
namespace mu::notation {
bool populateChordTrack(
    mu::engraving::Score* score,
    const mu::engraving::Fraction& startTick,
    const mu::engraving::Fraction& endTick,
    mu::engraving::staff_idx_t trebleStaffIdx,
    bool useCollectedTones = false);
} // namespace mu::notation
```

`analyzeHarmonicRhythm()` scans all eligible staves, detects harmonic boundaries
(ticks where the sounding pitch-class set changes), and runs chord analysis at each
boundary. In its default smoothed mode it collapses consecutive same-chord regions and
absorbs short regions; callers may instead request `HarmonicRegionGranularity::PreserveAllChanges`
when every detected harmonic event must survive into output (the chord-staff populate
path now does this). Declared and defined in `mu::notation` (bridge pattern — requires
engraving types `Score*`, `Fraction`).

`populateChordTrack()` clears the target grand-staff region and writes a harmonic
reduction with the following layout:

Before writing notes, the populate path normalizes measure-local gaps between analyzed
regions: if sparse spans inside a measure produced no chord result, the first and last
written region in that measure are extended to the measure boundaries and any internal
gap is absorbed into the preceding written region. This keeps the chord track from
serializing mixed chord/rest measures when the analyzer intentionally skips thin-texture
subspans.

| Position | Content |
|----------|---------|
| Above first stave | Key/mode label (e.g. "C maj", "D Dor?") only when key confidence is at least 0.5; confidence 0.5–0.8 appends "?" |
| Below first stave | Key relationship annotation (e.g. "(→ relative min)", "(→ dominant key)") only on assertive key changes (confidence at least 0.8) |
| Above second stave | Borrowed chord star ★ + source key (e.g. "Bb min") when a non-diatonic chord has an identifiable diatonic source, plus pivot label (e.g. "pivot: IV → I in G maj") at modulation boundaries and cadence marker (PAC, HC, DC, PC); these are written only when key confidence is at least 0.8 |
| Below second stave | Roman numeral (e.g. "IM7", "V7") only when key confidence is at least 0.5 |
| Treble stave notes | Upper chord tones (canonical or collected) |
| Bass stave notes | Root |
| Above treble stave | Chord symbol (e.g. "Cmaj7", "F#m7/A") |

**Borrowed chord rule:** The star ★ and source key are written only when a source
key is found (chord tones all diatonic to some other key within ±7 fifths). Purely
chromatic chords that fit no diatonic scale receive no marker.

The `useCollectedTones` flag controls whether the treble staff uses the original
sounding tones (preserving voicing color) or canonical chord tones.

Tick values in `HarmonicRegion` are raw integers rather than `Fraction` objects,
keeping the header free of the engraving module's `Fraction` include and
preserving `composing_analysis`'s module independence.

### 4.4 AnalysisUtils

**File:** `src/composing/analysis/analysisutils.h`

Shared utilities used by both analyzers and the formatter:

- `normalizePc(int pitch)` — reduces any MIDI pitch to pitch class 0–11
- `ionianTonicPcFromFifths(int fifths)` — converts circle-of-fifths position to
  the pitch class of the Ionian (major) tonic for that key signature
- `endsWith(const std::string&, const char*)` — generic string suffix test

### 4.5 Current Status Bar Integration

**Files:**
- `src/notation/internal/notationaccessibility.cpp` — entry point; calls `harmonicAnnotation()`
- `src/notation/internal/notationcomposingbridge.cpp` — `harmonicAnnotation()` bridge function

The analysis is invoked from `NotationAccessibility::singleElementAccessibilityInfo()`.
This method triggers on every selection change and calls `mu::notation::harmonicAnnotation(note)`
(defined in `notationcomposingbridge.cpp`), which runs `analyzeNoteHarmonicContext()` and formats
the result for display in the status bar.

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

The key/mode inferrer always runs. The notated key signature provides `keySignatureFifths`
as a scoring prior — it biases the inferrer toward nearby keys without overriding note
evidence. The `KeyMode` enum from the key signature is used only as a fallback when pitch
context is genuinely insufficient (fewer than 3 distinct pitch classes). See §5.2 for the
full revised priority logic.

#### Temporal Window for Key/Mode Analysis

16-beat lookback + 8-beat lookahead, with exponential time decay (0.7× per measure).
Dynamic expansion to 24 beats when confidence is below 0.60. Mode-switching hysteresis
prevents spurious mode switches on transient evidence. All `PitchContext` fields
(`durationWeight`, `beatWeight`, `isBass`) are fully populated.

#### Current Status Bar Output Format

```
[Note name]; [bar and beat]; Staff N (Part name); [C maj] Cmaj7 (IM7)
```

Chord symbol, key/mode, and Roman numeral are all appended.

### 4.6 User Preferences — Configuration Interface Split

**Files:**
- `src/composing/icomposinganalysisconfiguration.h` — IoC-registered interface for analysis settings
- `src/composing/icomposingchordstaffconfiguration.h` — IoC-registered interface for chord-staff output settings
- `src/composing/icomposingconfiguration.h` — non-IoC aggregate base (inherits both above; not registered)
- `src/composing/composingconfiguration.h/.cpp` — concrete implementation (registered under both sub-interfaces)
- `src/preferences/qml/MuseScore/Preferences/ComposingPreferencesPage.qml` — preferences UI

The configuration is split into two separately-registered IoC interfaces:

| Interface | Registered? | Inject when... |
|-----------|-------------|----------------|
| `IComposingAnalysisConfiguration` | Yes | Code needs analysis toggles, status-bar flags, mode tier weights |
| `IComposingChordStaffConfiguration` | Yes | Code needs chord-staff output preferences |
| `IComposingConfiguration` | **No** | Not used for injection; plain C++ base uniting both |

`IComposingConfiguration` is **not** registered because `MODULE_GLOBAL_INTERFACE` injects a
`modularity_interfaceInfo` static member, and multiple inheritance would make that member ambiguous.
`ComposingConfiguration` inherits from both sub-interfaces (and therefore from `IComposingConfiguration`
transitively) and is registered under each sub-interface separately.

Callers inject the narrowest interface they need.  The bridge functions in
`notationcomposingbridge.cpp`, `notationtuningbridge.cpp`, and `notationimplodebridge.cpp`
inject `IComposingAnalysisConfiguration` via `muse::GlobalInject`.

The UI is a dedicated preferences page under Edit → Preferences → Composing.

The preferences are organised into three sections: Analysis, Status bar, and Chord staff.

**Analysis section:**
- `analyzeForChordSymbols` (bool, default true) — pitch-structure analysis only;
  does not require key/mode inference
- `analyzeForChordFunction` (bool, default false) — key/mode-aware degree analysis;
  single toggle that feeds both Roman-numeral and Nashville-number display.
  Replaces the former separate `analyzeForRomanNumerals` / `analyzeForNashvilleNumbers`
  toggles.  Roman numerals and Nashville numbers are **presentation choices**, not
  separate analyses — they are alternative formatters on the same `ChordAnalysisResult`.
- `inferKeyMode` (bool, forced on when `analyzeForChordFunction` is active)
- `analysisAlternatives` (int 1–3, default 3) — single universal count applied to
  both the status bar and the context menu (replaces former per-type counts)

**Intonation section** (grouped under a labelled heading in the UI):
- `tuningSystemKey` (string, default "equal") — tuning system for "tune as" action
- `tonicAnchoredTuning` (bool, default true) — anchor each chord root to its JI
  scale-degree position above the mode tonic (§11.2a)
- `tuningMode` (int, default 0 = TonicAnchored) — high-level drift behavior:
  0 = Tonic-anchored (current behavior), 1 = Free drift (see §11.3f)
- `allowSplitSlurOfSustainedEvents` (bool, default true) — allows region retuning
  to rewrite sustained events into independent playback events when a continuation
  needs different tuning; applies to both single sustained notes and tied chains at
  existing tie boundaries in both TonicAnchored and FreeDrift, but anchors still
  protect the full written duration
- `minimizeTuningDeviation` (bool, default false) — subtract the mean offset per
  chord so the chord hovers near 0¢ while preserving internal JI ratios
- `annotateTuningOffsets` (bool, default false) — add a staff text showing the cent
  offset of each tuned note (e.g. "+15 −2 +3") below the chord in the score
- `annotateDriftAtBoundaries` (bool, default false) — in Free drift mode, insert a
  StaffText above the first eligible staff at each harmonic region boundary showing
  the accumulated pitch drift, e.g. "d=+3" or "d=-2" (only emitted when
  |driftAdjustment| ≥ 0.5 ¢; independent of `annotateTuningOffsets`)

**Mode detection weights** (21 independent sliders, one per mode, range −5.0 to +5.0, step 0.5):

Diatonic family:
- `modePriorIonian` (default +1.20)
- `modePriorDorian` (default −0.50)
- `modePriorPhrygian` (default −1.50)
- `modePriorLydian` (default −1.50)
- `modePriorMixolydian` (default −0.50)
- `modePriorAeolian` (default +1.00)
- `modePriorLocrian` (default −3.00)

Melodic minor family:
- `modePriorMelodicMinor` (default −0.50)
- `modePriorDorianB2` (default −1.50)
- `modePriorLydianAugmented` (default −2.00)
- `modePriorLydianDominant` (default −1.00)
- `modePriorMixolydianB6` (default −1.50)
- `modePriorAeolianB5` (default −2.50)
- `modePriorAltered` (default −3.50)

Harmonic minor family:
- `modePriorHarmonicMinor` (default −0.30)
- `modePriorLocrianSharp6` (default −2.50)
- `modePriorIonianSharp5` (default −2.00)
- `modePriorDorianSharp4` (default −2.00)
- `modePriorPhrygianDominant` (default −0.80)
- `modePriorLydianSharp2` (default −2.50)
- `modePriorAlteredDomBB7` (default −3.50)

Five named presets populate all 21 sliders:

| Preset | Character |
|--------|-----------|
| Standard | Classical/baroque defaults as above |
| Jazz | LydianDominant=−0.20, Altered=−0.50, MelodicMinor=−0.50, DorianB2=−1.00, PhrygianDominant=−0.80, HarmonicMinor=−0.50; diatonic at standard weights |
| Modal | All 7 diatonic modes equal at 0.0; melodic and harmonic minor at high penalty |
| Baroque | HarmonicMinor=−0.20, PhrygianDominant=−0.50; all non-diatonic modes at maximum penalty |
| Contemporary | All 21 modes at moderate penalty; optimizer determines final weights from corpus |

Presets are represented by `ModePriorPreset` (a plain struct with 21 `double` fields and a
`std::string name`) declared in `icomposinganalysisconfiguration.h`.  The free function
`mu::composing::modePriorPresets()` returns `std::vector<ModePriorPreset>` with all five.
The interface exposes two extra methods:
- `applyModePriorPreset(const std::string& name)` — writes all 21 priors in one call
- `currentModePriorPreset() const` — returns the name of the active preset, or `""` when
  the current values do not match any preset (epsilon = 1e-6)

The QML preferences page exposes these via `ComposingPreferencesPage.qml` →
`ComposingAnalysisSection.qml` as five `FlatButton` widgets (`accentButton` when active);
the current preset name is tracked in `currentModePriorPreset` Q_PROPERTY.

The bridge reads these at analysis time and populates `KeyModeAnalyzerPreferences`
before calling `analyzeKeyMode()`. The former 4-tier grouping (`modeTierWeight1`–`modeTierWeight4`)
and the internal +0.2 Ionian offset are replaced by these 21 independent priors.

**Status bar section** (boolean checkboxes; each enabled only when its analysis is on):
- `showChordSymbolsInStatusBar` (bool, default true) — requires `analyzeForChordSymbols`
- `showRomanNumeralsInStatusBar` (bool, default false) — requires `analyzeForChordFunction`
- `showNashvilleNumbersInStatusBar` (bool, default false) — requires `analyzeForChordFunction`
- `showKeyModeInStatusBar` (bool, default true) — requires `inferKeyMode`

Status bar format: `Chord: Bmaj / II / 2 (0.65) | Cmin / iv / 4 (0.43) in key: C major`.
Parts within a candidate joined by ` / ` (only active formats included); candidates
separated by ` | `; key appended as ` in key: X` when shown.  When no chord results
are shown but key/mode is on: `key: C major` (no "in" prefix).

**Chord staff section** (controls what "Implode to chord staff" writes — planned):
- `chordStaffWriteChordSymbols` (bool, default true) — write `HarmonyType::STANDARD`
  annotations above the treble staff; requires `analyzeForChordSymbols`
- `chordStaffFunctionNotation` (enum: None / Roman numerals / Nashville numbers,
  default Roman numerals) — write either `HarmonyType::ROMAN` or
  `HarmonyType::NASHVILLE` below the treble staff; requires `analyzeForChordFunction`.
  Roman and Nashville are mutually exclusive here — they encode the same information
  and displaying both would clutter the staff with redundant text.
- `chordStaffWriteKeyAnnotations` (bool, default true) — write key/mode staff text at
  region boundaries; requires `inferKeyMode`

---

## 5. Planned Analysis Extensions

### 5.1 Weight Population — Implemented for KeyModeAnalyzer, Pending for ChordAnalyzer

**KeyModeAnalyzer calling code** (in `NotationComposingBridge`) fully populates all
`PitchContext` fields: duration in quarter notes, beat-type weight from MuseScore's
`BeatType` enum, bass identification via two-pass per-segment scan, and exponential
time decay (0.7× per measure).

**ChordAnalyzer calling code** — `ChordAnalysisTone.weight` is still not populated
from duration or metric position. Populating it is a planned improvement that requires
no analyzer changes — only calling code changes.

### 5.2 Key/Mode Inference — Revised Priority and Expanded Temporal Window

**Notes Always Win — Implemented**

The key/mode inferrer always runs. The notated key signature's `KeyMode` enum
(`MAJOR`, `MINOR`, etc.) is no longer a bypass gate — it is passed as a weak hint
(`declaredMode`) to `analyzeKeyMode()` and influences the scoring prior but does not
skip the inferrer.

The only exception is a **piece-start shortcut** in `resolveKeyAndMode()`: when the
analysis tick is within the first 16 beats, no prior result exists (`prevResult == nullptr`),
and the key signature carries an explicit mode, the function returns the declared mode
immediately (confidence 0.5) rather than waiting for pitch evidence that cannot yet exist.
This is a deliberate pragmatic choice for the score opening, not a general bypass.

Outside the piece-start shortcut, the priority of evidence is:

**Priority of evidence:**

| Priority | Source | Description |
|---|---|---|
| Strongest | Actual sounding notes | what is literally happening now |
| Strong | Temporal context | surrounding measures |
| Weak | Notated key signature | `keySignatureFifths` (circle of fifths position) |
| Weakest | `KeyMode` enum | explicit major/minor tag (rare, only when user sets it) |

**Implemented logic — `resolveKeyAndMode()` in `notationcomposingbridgehelpers.cpp`:**

The key signature's `keySignatureFifths` remains a scoring prior inside the inferrer
(`keySignatureScore` biases toward nearby keys without overriding note evidence).
The `declaredMode` from the key signature is passed to `analyzeKeyMode()` as an optional
hint — it shifts the prior weight for that mode but does not prevent other modes from
winning.

The inferrer output is used for all but two narrow fallback cases:
- **Piece-start shortcut:** tick < 16 beats, no prior result, explicit key-sig mode →
  return declared mode at confidence 0.5 (no pitch evidence to analyze yet)
- **Insufficient data:** `modeResults.empty() || distinctPitchClasses(ctx) < 3` →
  fall back to key signature enum (Aeolian for MINOR, Ionian for all other explicit or
  unknown modes)

The `KeyMode` enum (`MAJOR`, `MINOR`, `IONIAN`, `AEOLIAN` etc.) is only a factor in
these two fallback paths — when pitch data is genuinely insufficient.

**Expanded Temporal Window — Implemented**

The bridge uses a 16-beat lookback + 8-beat lookahead window:

```cpp
const int LOOKBACK_BEATS  = 16;  // ~4 measures in 4/4
const int LOOKAHEAD_BEATS =  8;  // ~2 measures ahead
```

Notes are weighted by `durationWeight × beatWeight × timeDecay`, where time decay
applies an exponential factor of 0.7× per measure of distance from the analysis tick.
Beat-type weights are mapped from MuseScore's `BeatType` enum (downbeat 1.0,
stressed 0.7, unstressed 0.4, subbeat 0.2).

**Normalized Confidence — Implemented**

`KeyModeAnalysisResult::normalizedConfidence` is 0.0–1.0 via sigmoid on the score
gap between rank-1 and rank-2 candidates. The chord staff uses this to add "?" or
"(?)" to key/mode labels when confidence is below 0.8 or 0.5 respectively.

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

### 5.4 Modal Extension — Implemented

All 7 diatonic modes (Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian,
Locrian) are now evaluated. Each mode has a characteristic pitch boost/penalty and
a frequency prior configurable via user preferences (mode tier weights).

Mode suffixes are abbreviated: "maj", "min", "Dor", "Phryg", "Lyd", "Mixolyd", "Loc".

**Melodic minor modes** — still planned for jazz style support:
- Lydian Dominant (mode 4 of melodic minor) — #11 and b7 together
- Altered/Superlocrian (mode 7 of melodic minor) — maximum tension

### 5.5 Monophonic and Arpeggiated Input

Monophonic and arpeggiated chord inference is now tracked under
§4.1d. That section contains the current provisional phased plan,
including the separate-engine / unified-orchestrator design,
Phase 1a validation-first workflow, and the deferred full monophonic
engine for unannotated material.

### 5.6 Extended Harmonic Functions — Planned

Currently, non-diatonic chords show a borrowed source key label (e.g. "Bb min") when
an identifiable source is found. Explicit labeling of harmonic functions is backlogged:

**Classical chromatic vocabulary:**
- Augmented sixth chords (Italian, French, German +6): approach chords to V
- Neapolitan chord (♭II, N6): flat-supertonic major
- Common-tone diminished seventh

**Secondary function:**
- Secondary dominants / leading-tone chords (V/V, vii°/V, etc.)
- Tritone substitutions (subV/x): dom7 whose root is a tritone from the expected dominant
- Backdoor dominant (♭VII7 as V7 substitute) — jazz-specific

**Structural distinctions:**
- Tonicization vs. modulation: brief secondary dominant vs. genuine key change
- Chromatic mediants: major-third key relationships

**Implementation prerequisite:** resolution-target tracking (look-ahead to next chord
region) is required for secondary dominant and tritone sub detection.

### 5.7 Normalized Confidence Scores — Implemented for KeyModeAnalyzer

`KeyModeAnalysisResult::normalizedConfidence` is 0.0–1.0 via sigmoid on the score
gap (midpoint 2.0, steepness 1.5). Usage thresholds:

- Above 0.8 — display without qualifier
- 0.5–0.8 — append "?" to key/mode label
- Below 0.5 — suppress key-dependent chord-track annotations rather than exposing a low-confidence key

`ChordAnalysisResult` still returns only raw scores. Normalized confidence for
chord analysis is a planned extension.

### 5.7a Confidence Interpretation and "Good Enough" Plateau

The current confidence signals must be interpreted as heuristic ranking
stability, not calibrated probability of correctness.

- `KeyModeAnalysisResult::normalizedConfidence` is derived from an internal
  score-gap sigmoid and is suitable for tentative vs assertive UI exposure.
- `ChordAnalysisResult` still exposes raw scores only.
- Current corpus benchmark tables are mostly root-pitch-class agreement metrics,
  not full harmonic-correctness metrics.

Therefore the product target is not "always emit a label". The target is:

- high precision on exposed results
- calibrated abstention when evidence is weak
- strong internal consistency across all entry points
- coverage gains only after precision is acceptable

For planning purposes, the current vertical tertian engine plus targeted texture
fixes should be expected to plateau around 65–75% exact external root+quality
agreement on **full-texture tonal corpora** (SATB choral, chamber, full piano
accompaniment). This band applies specifically to region-centric DCML comparison
methodology. Thin-texture corpora (Mozart piano sonatas, C.P.E. Bach keyboard,
solo melody) are excluded from this target — they require a separate inference
strategy and should not be compared against the same band. The When in Rome and
music21-surface comparisons use different methodologies and are not directly
comparable to this figure.

Exact Roman/function agreement will remain lower because it compounds chord
identity, key/mode, analytical granularity, and reference-philosophy
differences. Beyond that band, diminishing returns should be expected unless
the system adds a second inference family or richer musical representation.

Highest-return work before that plateau:

1. remaining recurring texture fixes: broken-chord/pedal boundary handling,
  Baroque passing-bass handling, and phrase-aware key look-ahead. These address
  primary failure modes that confidence calibration cannot fix.
2. evaluation tier separation: split published quality reporting into
  internal consistency, root-only/root+quality external agreement on
  full-texture corpora, and full harmonic correctness. Baselines must be
  stable before held-out calibration is meaningful.
3. normalized chord confidence plus held-out calibration on stable baselines.
  This becomes useful only after the primary texture failure modes are reduced.
4. mixed-texture orchestration: add a lightweight second strategy for
  obviously arpeggiated or single-line spans. "Obviously arpeggiated" is
  defined as maximum simultaneous pitch-class count in any beat window <= 2.
  Compare calibrated confidence across strategies and treat abstention as a
  valid outcome.
5. an explicit region-identity decision: preserve-all regions must be keyed to
  either `root + quality` (harmonic summary mode) or full sonority identity
  (as-written mode). Fold the deferred chord-track octave-deduplication item
  into this decision. Both modes are needed; neither should remain undecided.

The following should be treated as post-plateau scope expansion rather than
immediate blockers:

- quartal/quintal language detection
- rootless ensemble awareness
- polychordal / upper-structure detection
- register-sensitive add2 vs add9
- the full Phase 2 monophonic engine

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

**Piano left-hand beat-1 pattern over-segmentation**

In piano music with a single bass note on beat 1 followed by a chord block on beats 2–3
(mazurka, waltz, and march accompaniment patterns), the Jaccard boundary detector fires
between beat 1 `{bass pc}` and beats 2–3 `{chord pcs}` because these are completely
different pitch-class sets. Under a pedal marking, all three beats should accumulate to
one pitch-class set. Fix required: include pedal-sustained notes when computing per-beat
pitch-class sets for Jaccard boundary detection. Confirmed on Chopin BI16-1 measure 1.
Next session priority.

**bassNoteRootBonus miscalibration — confirmed by score inspection (2026-04-09):**

Score inspection across four corpora confirms a single root cause:
`bassNoteRootBonus` fires unconditionally on the lowest sounding note,
regardless of whether that note is actually the chord root.

Confirmed failure patterns:

- Chopin mazurka: single bass note on beat 1 (root) isolated from chord block on beats
  2-3 — bass correctly identifies root but creates spurious boundary vs chord beats
- Mozart sonata: arpeggiated left hand (C→E→G) — each successive lowest note promoted
  to root, producing Em / Dm7 / Bdim instead of C
- Corelli trio sonata: walking/stepping bass line — each bass step promoted to root,
  producing one chord per bass note instead of recognizing the underlying harmony
- Beethoven string quartet: cello moving in inversions and stepwise motion — same
  pattern as Corelli

All four cases share the same mechanism: the bass voice moves at a faster rate than the
harmonic rhythm, and each bass note independently receives `bassNoteRootBonus`,
overriding the correct root identification from the chord tones above.

**Implemented fix (2026-04-09):**

`bassNoteRootBonus` is now conditioned on corroborating root-position support in the
accumulated tones:

- Full bonus: the candidate's fifth slot is present, and third-bearing templates also
  retain their own matching third
- Reduced bonus: a major/minor third above the bass is present, but the fifth support
  is absent or contradictory
- Minimal bonus: no third or fifth support above the bass is present

Two new preferences expose the reduced tiers in `ChordAnalyzerPreferences`:

- `bassRootThirdOnlyMultiplier = 0.3`
- `bassRootAloneMultiplier = 0.1`

This preserves the bonus for clear root-position chords while materially reducing the
cross-corpus bass-root failure signal. Validation on 2026-04-09:

- Bach WIR structural improved from 50.0% to 52.3%
- Bach music21 surface re-run now reports 39.3% average agreement
- Beethoven 59.9%, Mozart direct DCML 26.7% root agreement with 59.5%
  `bassIsRoot` in disagreements (not directly comparable to the full-texture
  corpora because only 32.5% of our regions align), Corelli 63.3%, Chopin 57.5%,
  Grieg 50.3%,
  Schumann 58.7%, Tchaikovsky 58.9%, Dvorak 66.2%
- Weighted non-Bach `bassIsRoot` in disagreements dropped from 73.0% to 58.0%
  (piano 58.5%, chamber 57.5%)

The remaining Chopin BI16-1 notation mismatch turned out to be separate from scoring:
the batch path already collapsed adjacent same-root/same-quality regions, but
`analyzeHarmonicRhythm(..., PreserveAllChanges)` did not. The notation bridge now uses
the same collapse rule, so repeated slices that analyze to the same chord merge into one
region even in preserve-all mode. A dedicated notation regression now checks that BI16-1
opening collapses to a single G-major region. A follow-up BI16 regression on the full
populate path also guards against mixed chord/rest measures: sparse unanalysable spans
within a measure are now absorbed into neighboring written chord regions in
`populateChordTrack()` instead of being left behind as visible rests.

Post-fix score inspection isolated three remaining categories, none of which revive the
original unconditional bass-root promotion bug:

- **Dvorak op08n06: accepted ambiguity ceiling.** The chord-track output is musically
  plausible and the disagreement with DCML reflects genuine harmonic ambiguity in
  chromatic Romantic writing. No follow-up scoring change is planned for this movement.
- **Corelli op01n08d: deferred Baroque passing-bass limitation.** Walking bass passing
  tones can still pull the output toward sus/slash-chord spellings rather than the
  underlying triadic harmony. This is now documented as a known limitation of the
  current vertical scorer in Baroque stepwise bass textures.
- **Schumann Kinderszenen: not a comparison artifact.** `tools/compare_analyses.py`
  classifies chord identity from root pitch class and quality, and the direct DCML
  runners compare root pitch class only. Slash-chord spellings such as `D7/C` already
  match inversional DCML spellings when the underlying root pitch class agrees, so the
  58.7% Schumann baseline is accepted as genuine rather than a notation-mapping error.
- **Chord track octave deduplication: deferred.** When imploding to chord track,
  octave duplicates are currently collapsed to a single pitch class. That is correct
  for harmonic-summary analysis but incorrect for "as written" chord-track generation,
  where the original voicing should be preserved. Fixing this requires a separate
  implode-bridge mode flag to distinguish harmonic summary from as-written output.

#### Active follow-up plan (2026-04-10)

The post-fix score-review roadmap now runs under a gated Milestone A before any
later score-review work is allowed to proceed:

- **A1 — shared same-chord merge semantics.** Batch and notation now collapse
  adjacent same-root/same-quality slices by unioning tone sets and recomputing
  the bass from the merged tones. Acceptance is complete: `composing_tests.exe`
  passed 295/295, `notation_tests.exe` passed 19/19, `batch_analyze_regressions`
  passed, Bach WIR structural remains 52.3%, and Chopin remains 57.5%.
- **A2 — mechanical batch/notation parity.** `batch_analyze` now supports
  `--dump-regions batch|notation|notation-premerge`, the notation bridge exposes
  pre/post-merge debug capture, and `tools/check_parity.py` compares both paths on
  one score. Acceptance is complete: BWV 227.7 and Chopin BI16-1 now match exactly
  on region starts, spans, roots, qualities, and tone sets.
- **A3 — confidence/exposure cleanup.** Complete. Key-dependent chord-track output
  is now confidence-gated: below 0.5 it is suppressed, from 0.5 to 0.8 only the
  tentative key label survives, and at 0.8 or above the full key-dependent annotation
  set is allowed. A Dvorak `op08n06` notation regression verifies that low-confidence
  regions do not emit key labels or Roman numerals while confident regions still do.

Use the following benchmark passages for any follow-up score inspection or UI
validation:

- Bach BWV 227.7: bars 1–2, 8–10, final cadence
- Chopin BI16-1: bars 1–5, 10–16, trio
- Dvorak op08n06: early slow section, chromatic middle, late modal stretch

**Formatter: double quality prefix (confirmed 2026-04-13):**
Chord symbol formatter produces unreadable strings when quality and extension share
a prefix: `Csussus2` (suspended + sus extension), `G#aussus5` (augmented + sus
extension), `Dsussus5D+` (worst case).
Confirmed in 7+ scores across all styles.
Fix: sanitize `sussus`→`sus`, `aussus`→`aug(sus...)` in formatSymbol.
**Fixed 2026-04-13** — commit `4c35da17`.

**Formatter: invalid bass note name `/p` (confirmed 2026-04-13):**
TPC resolution failure produces `p` as a bass note name, e.g. `BbMaj7/p`. Occurs
when bassTpc is TPC_INVALID. Fix: guard against invalid TPC before appending
slash bass suffix. Confirmed in Dvořák Silhouettes.
**Fixed 2026-04-13** — commit `4c35da17`.

**Key detection: relative major/minor ambiguity (confirmed 2026-04-13):**
When opening chord is in first inversion, the bass note matches the tonic of the
relative key, causing the inferrer to lock onto the wrong member of the relative pair:
- BWV 227/7 (E minor, 1♯): was reading as G major throughout
- BWV 66.6 (F# minor, 3♯): was reading as A major (BWV 66.6 was already correct per
  music21 ground truth — STATUS.md expectation corrected 2026-04-13)

**Fixed 2026-04-13** — complete-triad bonus + piece-start hysteresis, commit `3ba80cb7`.

**Preset misuse degrades output (confirmed 2026-04-13):**
Jazz preset causes key context drift on Classical scores. Mozart K279 with Jazz preset
reads C major as D Dorian in multiple passages. Standard preset on same score produces
output close to DCML reference. Preset selection is user responsibility — document
clearly in UI and help text. Standard preset is correct default for all non-jazz
repertoire.

**Modulation tracking — philosophy difference (confirmed 2026-04-13):**
Our analyzer stays in the home key and labels borrowed chords with chromatic scale
degrees (e.g. `♭VII`, `II` in C major). DCML reference uses tonicization notation
(e.g. `V/IV`, `IV/III`). Both are valid analytical approaches. Our approach is more
accessible for general users. Not a bug — design choice.

**Third-inversion dominant seventh ambiguity (confirmed 2026-04-13):**
G7/C (G dominant seventh, C in bass) is sometimes identified as Gm/C (G minor over C).
Occurs when B natural evidence is weak and Bb reading is slightly preferred. Confirmed
in Mozart K279 and Chopin Mazurkas. Known limitation of vertical template matching on
passing-bass textures.

**Roman numeral quality at minor tonic cadences (confirmed 2026-04-13):**
At minor key cadences, analyzer occasionally writes major `I` where minor `i` is
correct. Confirmed in Corelli. Likely a chord quality threshold issue at cadential
points.

**Over-segmentation on dense piano texture (confirmed 2026-04-13):**
Dvořák Silhouettes and Chopin Mazurkas show repeated identical chord labels
(e.g. `Bb×8`, `Fsus×20`) from Jaccard boundary firing on dense arpeggiated texture.
Same-chord merge logic is working but the merge threshold may be too fine. Known
limitation — mixed texture orchestration would address this post-plateau.

**`do` abstention in jazz context is correct behavior (confirmed 2026-04-13):**
In "You Must Believe in Spring" (jazz ballad, 5 flats), the analyzer correctly abstains
on highly chromatic passages, writing `do` (no label) rather than guessing wrong. This
is confidence gating working as intended. More trustworthy than wrong labels.

**Campania font rendering artifact (`Dsdim`, `Fsdim` etc.) — MuseScore core issue, not our bug (confirmed 2026-04-17):**
Certain chord symbol strings containing diminished chords on specific roots (D, F, C, A)
render with a spurious `s` prefix in MuseScore's Campania chord symbol font — e.g.
`Ddim7/A` renders visually as `Dsdim7/A`. The internal string produced by our formatter
is correct: confirmed by clicking the element to edit it, which shows the correct string
without the `s`. The same artifact affects other chord symbol tools including third-party
plugins. This is a MuseScore core font rendering issue, not a bug in the composing module.
The same artifact appears in chord symbol plugins used for comparison QA. Fix requires
changes to the Campania font or MuseScore's chord symbol rendering pipeline — outside the
scope of this module.

### 5.9 Key Signature Injection — Not Planned

An earlier design considered automatically suggesting key signature insertions in the main
score when the key/mode inferrer detected extended passages in a different key. This was
superseded by the key/mode annotation feature in the chord track (§11.5). The chord track
provides the same analytical information — inferred key regions with confidence indicators —
without modifying the main score. The user reads the chord track annotations and decides
independently whether to add key signatures to the main score. No automatic key signature
injection is planned.

### §5.10 Tonicization Labels

Secondary dominant and other tonicization labels (V/V, vii°/V, V/ii etc.)
exposed in the annotate path Roman numeral layer. The analyzer already
detects tonicizations internally; this exposes the conclusion as an
annotation. Universal across all presets.

### §5.11 Augmented Sixth Chord Labels

Explicit It+6, Fr+6, Ger+6 labels in the annotate path Roman numeral layer.
These replace the generic chromatic Roman numeral (e.g. ♭VI) when the
analyzer detects the specific augmented sixth interval pattern. Gated to
Standard and Baroque presets only. Jazz and Nashville presets continue to
emit chromatic Roman numerals or chord symbols respectively.

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

### 11.2a Tuning System Preference

A single user preference (`composing/tuningSystemKey`) controls which tuning system
is applied across **all** tuning workflows:

- Per-note tuning from the context menu ("Tune as")
- Chord track population ("Implode to chord track")
- Region tuning ("Tune selection")

The preference is set in Preferences → Composing → Analysis ("Tuning system"
dropdown, enabled only when Roman-numeral analysis is active).  Valid keys:
`"equal"`, `"just"`, `"pythagorean"`, `"quarter_comma_meantone"`.  Default: `"equal"`.

All tuning code paths read the preference at call time via `preferredTuningSystem()`
(defined in `notationtuningbridge.cpp`), which resolves the key through
`TuningRegistry::byKey()` with a `JustIntonation` fallback if the key is unset or
unknown.  No tuning code hardcodes a specific system.

**Tonic-anchored tuning** (`tonicAnchoredTuning`, default on): when enabled, each chord
root is placed at its pure JI scale-degree position above the mode tonic rather than always
at 0¢.  This prevents syntonic-comma drift across a piece.  Implemented as a virtual
`rootOffset(keyMode, rootPc)` method on `TuningSystem` (default: 0.0¢; JI override uses
the mode-relative dev[] table).  `KeyModeAnalysisResult.tonicPc` and `.mode` are populated
by the bridge from `keyFifths` + `keyMode` using `keyModeTonicOffset()`.

**Minimize retune** (`minimizeTuningDeviation`, default off): subtracts the mean of all
attacking-note offsets per chord so the chord hovers near 0¢ while preserving internal
JI ratios.

**Annotate tuning offsets** (`annotateTuningOffsets`, default off): adds a `StaffText`
element below the chord in the score (one per chord voice, space-separated rounded cent
values) for each chord processed in Phase 2 and Phase 3 of the tuning algorithm.

**Allow split/slurring of sustained events for retuning**
(`allowSplitSlurOfSustainedEvents`, default on): lets region tuning rewrite sustained
events when a later harmonic region needs an independent playback event with a
different tuning. In TonicAnchored mode this is the region-local retuning behavior
already described above. In FreeDrift mode it means that a sustained event may be
rewritten only when the continuation's target tuning differs meaningfully from the
carried tuning. For an untied sustained note this uses split-and-slur at the region
boundary. For a tied chain, the bridge may reuse an existing tie boundary: the tie
that crosses the region boundary is removed and replaced with a slur so the later
segment can carry its own tuning. If the preference is off, the whole sustained event
remains one tuning event in both modes.

**Anchor override:** anchor expressions (`alt. rif.` and the other Italian forms)
protect the full written duration of the sustained event. An anchored sustained note is
never split, and an anchored tied chain is never segmented at a tie boundary even when
`allowSplitSlurOfSustainedEvents` is enabled. If the anchor appears on any note in the
tie chain, the chain remains one protected written-duration event.

### 11.2b Adaptive Tuning — Future Exploration

The current tuning implementation computes offsets independently per note against
a fixed interval table.  A more sophisticated approach would solve for optimal
tuning offsets *simultaneously* across all sounding voices, balancing three
competing goals: harmonic purity (intervals close to JI), ET anchoring (notes
not straying too far from equal temperament), and temporal continuity (minimizing
pitch movement between successive chords).

Several algorithmic methods exist in the literature:

- **Spring model** (deLaubenfels, ~2000–2004) — models each note as a node with
  interval springs (rest length = JI ratio) and anchor springs (pulling toward
  ET).  Anchor stiffness per voice controls how much each voice moves.  Solving
  for equilibrium is a linear system.
- **Hermode Tuning** (Mohrlok, 1990s–present; shipped in Logic Pro) — hierarchical
  interval priority (fifths first, then thirds), with a tracked center pitch to
  prevent drift.  Bass and melody receive less movement by design.
- **Weighted least-squares optimization** — generalizes the spring model as a
  cost function with per-voice weights for harmonic purity, ET anchoring, and
  temporal continuity.  Minimizing the quadratic cost yields a linear system.
- **Iterative relaxation** — a real-time-friendly variant that starts at ET and
  iteratively moves notes toward pure intervals scaled by per-voice flexibility,
  converging in 3–5 iterations.

The key design concept across all methods is **per-voice anchor weight**: outer
voices (bass, melody) get high anchor stiffness so they stay close to ET, while
inner voices absorb more of the harmonic adjustment.  Temporal anchoring adds a
penalty for pitch movement at chord boundaries, referencing the previous chord's
solved pitches — tying naturally into the harmonic rhythm regions.

This would evolve the `TuningSystem` interface from independent per-note offsets
to a simultaneous solve across all voices at each harmonic region boundary.  The
`anchorPitch` flag in `InstrumentIntonationConfig` would become a continuous
weight rather than a binary.  No implementation is planned yet — this section
records the design space for future exploration.

Another deferred design question is **which interval family to prefer for
ambiguous sonorities**.  The current shipped tuning systems use fixed lookup
tables (for example, 5-limit just intonation uses 9/5 for a minor seventh and
15/8 for a major seventh) rather than a style-aware policy that can choose
between alternatives such as 5-limit dominant sevenths versus septimal
"harmonic sevenths" (7/4), or other competing targets for altered/extended
sonorities.  This is not specific to seventh chords — similar ambiguity also
appears in tritones, minor sonorities, diminished/augmented chords, and larger
extensions.  This choice architecture should be explored later, but it is not a
current implementation target.

### 11.2c Scoring Parameter Optimization Readiness (P8c)

Both `ChordAnalyzerPreferences` and `KeyModeAnalyzerPreferences` expose a `bounds()` method that returns a `ParameterBoundsMap` — a `std::map<std::string, ParameterBound>` where each entry describes the valid range for one tunable parameter:

```cpp
struct ParameterBound {
    double min;
    double max;
    bool   isManual = false;  // true = skip during automated optimization
};
using ParameterBoundsMap = std::map<std::string, ParameterBound>;
```

`isManual = false` parameters are safe for gradient-based, grid-search, or Bayesian optimization. `isManual = true` parameters are either wired to user-visible preferences (mode priors, hysteresis margins, declared-mode penalty) or have narrow hand-tuned sweet-spots.

**Purpose:** makes the parameter space machine-readable. An optimizer can call `bounds()` to discover all tunable parameters, their valid ranges, and which are off-limits for automated tuning. This is sufficient to wire up a simple grid-search or parameter-sweep runner without manually hardcoding parameter names.

**Not yet implemented:** serialization of `ChordAnalyzerPreferences` and `KeyModeAnalyzerPreferences` to/from JSON. When the settings store is wired in, this is the next step: map each struct field to a settings key, use the `bounds()` method to enforce valid ranges.

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

### 11.3a Zero-Sum Centering

The current tuning implementation applies fixed offsets relative to a single reference
pitch. A more musically effective approach — used by Hermode Tuning — centers the
deviations so that the sum of all tuning offsets across simultaneously sounding voices
equals zero.

**Why this matters:** When all voices are offset in the same direction, the entire chord
drifts away from equal temperament. This creates compatibility problems with fixed-pitch
instruments and with an audience's sense of absolute pitch. Zero-sum centering ensures the
chord is tuned purely internally while its average pitch matches equal temperament.

**Example — C major chord in just intonation:**

```
Raw just offsets:     C=0,   E=-14,  G=+2    sum=-12
Equal centering:      C=+4,  E=-10,  G=+6    sum=0
```

The chord is equally pure in both cases — the intervals between notes are identical. But
the centered version has zero net deviation from equal temperament.

**Implementation:** After computing raw just intonation offsets for all sounding voices,
compute the mean offset and subtract it from each voice's offset. The result is a set of
offsets that sum to zero.

**Status:** Basic (unweighted) zero-sum centering is implemented and ships as the
`minimizeTuningDeviation` user preference in `applyTuningAtNote()` and `applyRegionTuning()`.
When enabled, the arithmetic mean of all note offsets in the chord/region is subtracted from
each note's offset before it is applied. This is the §11.3a definition — "compute the mean
offset and subtract it from each voice's offset." The voice-role-weighted variant (§11.3b)
is not yet implemented; the current implementation weights all voices equally.

### 11.3b Weighted Centering by Voice Role

Pure zero-sum centering distributes the correction equally across all voices. This is
musically too democratic — the melody and bass are more perceptually prominent than inner
voices, and pitch changes in these voices are more audible.

Weighted centering distributes the centering correction inversely proportional to each
voice's musical importance. More important voices receive less correction — they stay
closer to their raw just intonation position. Less important voices absorb more correction.
The zero-sum property is preserved regardless of the weighting.

Voice role weights are defined in the style JSON:

```json
{
  "tuning": {
    "centeringWeights": {
      "melody": 3.0,
      "bass": 2.5,
      "inner": 1.0
    }
  }
}
```

Higher weight = more important = less correction applied to that voice.

**Bass weight by inversion:** The bass voice weight is further modified by the chord's
inversion, since the acoustic anchor role of the bass depends on whether it is playing the
harmonic root:

| Inversion | Bass note | Anchor strength | Weight (example) |
|---|---|---|---|
| Root position | root in bass | strong anchor | high (e.g. 2.5) |
| First inversion | third in bass | moderate anchor | medium (e.g. 1.5) |
| Second inversion | fifth in bass | weak anchor | low (e.g. 1.0) |
| Third inversion | seventh in bass | very weak | very low (e.g. 0.8) |

In inverted chords, the acoustic anchor is the harmonic root even if it is not the lowest
sounding note. The tuning system anchors to the implied root when computing centering, not
just the bass note.

**Pedal points** — a bass note sustained while harmony changes above it — receive maximum
anchor weight regardless of inversion, since they are explicitly the fixed reference in the
musical context.

Automatic melody detection is deferred. For now, voice role is determined by staff position
or explicit user assignment — not automatic detection. Per-staff override of voice role is
a future extension.

### 11.3c Note Retuning Susceptibility

Not all notes should be retuned equally freely. The system must respect that notes which
have been sounding for some time have established a pitch in the listener's ear, and
retuning them mid-sustain is audible as a wobble or portamento.

Rather than discrete protection classes, the system uses a **maximum adjustment budget** —
a continuous value in cents — that caps how much any note can be retuned at a harmonic
boundary. This budget is determined by how long the note has been sounding, modified by
musical context.

**Duration-based maximum adjustment budget:**

| Duration sounded | Maximum adjustment |
|---|---|
| < 30ms | Unlimited — ear has not registered the pitch |
| 30ms – 200ms | Up to 8–10 cents |
| 200ms – 500ms | Up to 4–5 cents |
| 500ms – 1000ms | Up to 2–3 cents |
| > 1000ms | Up to 1–2 cents |

The 30ms threshold corresponds to the minimum time for the ear to register a pitch. Below
this threshold, retuning is inaudible and the note can be placed optimally. Above it, the
budget shrinks as duration increases.

**Harmonic context modifiers** applied to the duration-based budget:

- Note is an **avoid note** in the new harmony → increase budget by 50% (the dissonance
  justifies more movement)
- Note is a **leading tone or chordal seventh** in the new harmony → increase budget by
  30% (tendency tone, movement is musically expected)
- Note is still a **consonant chord tone** in the new harmony → decrease budget by 50%
  (no musical reason to move)
- Note forms a **pure interval with another sustained note** (e.g. a perfect fifth) →
  decrease budget by 70% (breaking a locked resonance is very audible)

**Special cases:**

**Sustained perfect fifth or octave pairs:** Two notes a perfect fifth or octave apart
that have been sounding together for more than ~200ms have established a locked acoustic
resonance — their overtones are interlaced and beats have disappeared. Both notes receive
near-zero budget and effectively become anchors for the new harmony to tune around. Neither
note should be split; the new voices tune to them.

**Tied notes:** A non-partial tie chain explicitly carries a compositional instruction of
continuity. For region tuning, the entire non-partial tie chain is treated as one tuning
event. The chain must not be split. Its tuning is set from a single authority note and
protected thereafter; later harmonic regions tune around that established pitch.

The authority note is chosen as follows:

- If any note in the non-partial tie chain carries an `alt. rif.`-style anchor
  expression, the earliest such note in the chain is authoritative.
- Otherwise, the first note in the chain (the actual attack) is authoritative.

The tuning offset is computed once from that authority note's harmonic context and applied
unchanged to every note in the chain. If a user wants a sustained sound to be retuned when
the harmony changes, they should replace the tie with a slur.

**Unisons and octaves across voices:** Two or more notes sounding the same pitch class
simultaneously (in unison or octave relationship) must receive identical tuning offsets.
They are treated as a linked pair — the offset is computed once for the pair and applied to
both. Neither can be tuned independently.

**Repeated notes:** A note that was just heard in the previous beat and is now repeated —
same pitch class, adjacent position — is compared against the listener's memory of the
previous instance. Even 3–4 cents difference is audible as inconsistency. Repeated notes
receive a reduced budget until sufficient time has elapsed.

**Register sensitivity:** Notes between approximately 500Hz and 4000Hz are most sensitive
to retuning — the ear discriminates pitch most precisely in this range. Notes above or
below this range receive a slightly increased budget. The register modifier is applied as a
multiplier on the duration-based budget.

**Instrument sensitivity:** MuseScore's instrument ID system (e.g. `wind.flutes.flute`,
`voice.soprano`, `strings.violin`) is used to look up a per-instrument sensitivity value
from the knowledge base. This value scales the protection budget — more sensitive
instruments (flute, soprano) receive smaller budgets, less sensitive instruments (brass
with vibrato, electric guitar) receive larger budgets. Family-level fallbacks apply when
specific instrument IDs are not found.

```json
{
  "instrumentTuningSensitivity": {
    "wind.flutes": 0.90,
    "wind.reeds": 0.80,
    "voice": 0.85,
    "strings.bowed": 0.70,
    "brass": 0.55,
    "strings.plucked": 0.40
  },
  "defaultSensitivity": 0.60
}
```

Higher sensitivity = smaller maximum adjustment budget = more protection from retuning.

Fixed-pitch instruments (piano, organ, fretted guitar) are deferred — their handling is not
yet implemented. When implemented, they will serve as absolute anchors that other
instruments tune to, and will never receive tuning offsets themselves.

#### User-defined tuning anchors

A user can mark any note as a **tuning anchor** by attaching a MuseScore
Expression element with any of the accepted Italian forms:

| Form | Context |
|------|---------|
| `altezza di riferimento` | Full form — for performance notes and program text |
| `alt. rif.` | Standard score abbreviation (space after first dot) |
| `alt.rif.` | Compact abbreviation (no space after first dot) |
| `altezza rif.` | Semi-abbreviated form |

Italian: *altezza* = pitch, *riferimento* = reference.

**Rules for anchor notes:**
- **Zero tuning offset** — the note is left exactly at 12-TET.
- **Never split** — anchor notes are not divided at harmonic boundaries.
- **Not a FreeDrift reference** — in FreeDrift mode the anchor note is
  excluded from the drift reference hierarchy (P1/P2/P3); it sits at 0 ¢
  and other notes accumulate drift around it.
- **Excluded from zero-sum centering** — other voices in the harmonic region
  absorb the full centering correction; the anchor contributes zero.
- Applies to the specific note carrying the Expression only — subsequent notes
  on the same staff are not automatically anchored.

**Priority:** Highest. Overrides all duration-based, context-based, and
FreeDrift reference hierarchy rules.

**Keyword matching:** Case-insensitive, leading/trailing whitespace trimmed.
Exact match only — prefix/suffix text does not count.
`"ALT. RIF."`, `"Alt. Rif."`, `"  alt. rif.  "` all match `alt. rif.`.

**Implementation:**
- `kTuningAnchorKeywords` array (`std::array<const char*, 4>`) in
  `composing/intonation/tuning_system.h`
- `trimAndLowercase(std::string_view)` — inline helper for normalization
- `isTuningAnchorText(std::string_view)` — pure function for testable keyword
  matching; iterates `kTuningAnchorKeywords`
- `RetuningSusceptibility` enum in `tuning_system.h` with values
  `AbsolutelyProtected`, `Adjustable`, `Free`
- `hasTuningAnchorExpression(const Note*)` — bridge function in
  `notationtuningbridge.cpp`; scans the note's segment annotations for a
  matching Expression element on the same track
- `computeSusceptibility(const Note*)` — returns `AbsolutelyProtected` for
  anchor notes; `Free` for all others (duration-based classification is a
  future addition)

### 11.3d Tuning Session State

The tuning system maintains session-only state that is not persisted to the MSCZ file and
resets when the score is closed.

**Global session parameters:**

```cpp
class TuningSessionState {
public:
    // Global sensitivity — scales maximum adjustment budget across all voices
    // 1.0 = default, < 1.0 = more aggressive, > 1.0 = more conservative
    float globalSensitivity = 1.0f;

    // Global depth — scales tuning offsets between ET and full just intonation
    // 0.0 = equal temperament, 1.0 = full just intonation offsets
    // 0.6–0.7 recommended when mixing with fixed-pitch instruments (HMT guideline)
    float globalDepth = 1.0f;
};
```

**Sensitivity** scales the maximum adjustment budget. Higher sensitivity means smaller
budgets across all protection tiers — more conservative retuning.

**Depth** scales the final tuning offsets linearly between equal temperament (0%) and the
computed just intonation values (100%). Useful when performing alongside a piano — HMT
recommends 60–70% depth in mixed ensembles to reduce the mismatch between adapted and
fixed-pitch instruments.

Both parameters are exposed as sliders in the tuning preferences panel. They are
session-only — not persisted.

**Future extension:** Per-staff sensitivity and depth overrides, accessible via right-click
on the staff name. This will also be session-only when implemented. Visual indicator on the
staff label when an override is active.

### 11.3e The Complete Tuning Algorithm

Putting the above together, the tuning algorithm for a harmonic region boundary proceeds as
follows:

**Step 1 — Classify all sounding notes by susceptibility**
For each sounding note, compute its maximum adjustment budget from: duration sounded,
harmonic context in the new chord, register, instrument sensitivity, and special cases
(tied, unison pair, sustained fifth/octave pair).

**Step 2 — Identify anchors**
Notes with near-zero budget — sustained perfect fifth/octave pairs, tied notes, very long
sustained notes — become anchors. They do not move. The new harmony must tune around them.

**Step 3 — Compute raw just intonation offsets**
For all non-anchor notes, compute the ideal just intonation offset given the new chord and
the voice's role within it. Apply the depth scalar.

**Step 4 — Apply weighted zero-sum centering**
Compute the weighted centering correction for the non-anchor notes. Voice role weights and
bass inversion weight determine the distribution. Anchors are excluded from the centering
calculation. Apply the correction so the sum of all non-anchor offsets equals zero.

**Step 5 — Clamp to susceptibility budget**
Clamp each note's final offset to its maximum adjustment budget. If a note's ideal offset
exceeds its budget, it moves only as far as its budget allows. The zero-sum property may be
slightly violated by clamping — this is acceptable; the priority is avoiding audible
retuning artifacts.

**Step 6 — Apply sensitivity scalar**
Multiply all offsets by the global sensitivity parameter.

**Step 7 — Determine which notes need splits**
Notes with offsets exceeding `kEpsilonCents` (0.5 cents) and not protected by anchor
semantics may need independent playback events. Untied sustained notes use the normal
split-and-slur mechanism. For tied sustained events, existing tie boundaries may be reused
as segmentation points when preference and harmonic context allow; otherwise the tie chain
remains one event and receives one chain-level tuning. Anchors override both cases and
protect the full written duration from segmentation. Apply the split-and-slur mechanism
(§11.4) for all notes requiring independent playback events.

**Step 8 — Apply tuning offsets**
Write final cent values to all notes via `undoChangeProperty(Pid::TUNING, ...)`.

### 11.3f FreeDrift Mode

The `tuningMode` preference selects one of two high-level drift behaviors:

**TonicAnchored (default):** Each harmonic region independently computes offsets
relative to the mode tonic. The chord root is placed at its JI scale-degree
position; individual chord tones are offset relative to that root. Sustained
notes crossing region boundaries are split-and-slurred so each segment receives
the correct offset for its region. Drift does not accumulate across regions.

**FreeDrift:** Tuning offsets accumulate naturally across harmonic regions.
The reference pitch for each region is determined by a priority hierarchy:

| Priority | Source | Meaning |
|----------|--------|---------|
| P1 | Held note from previous region | Drift reference: existing tuning of the held note |
| P2/P3 | Bass note / analyzer root | No prior drift — fresh baseline (adjustment = 0) |

When a held note bridges regions (P1), the drift adjustment is:
```
driftAdjustment = heldNote.tuning() − desiredOffset(heldNote.ppitch())
```
All notes in the new region receive `desiredOffset(pitch) + driftAdjustment`.

**`alt. rif.` anchor notes in FreeDrift:** Unlike in TonicAnchored mode (where
an anchor forces all notes back to a 0 ¢ reference), in FreeDrift an anchor note
is pitched *at the current drift level* — i.e. it receives `finalOffset(pitch)`
exactly like any other note. It "confirms where we have drifted to" without
pulling other notes back to 12-TET. Anchor notes are excluded from P1 held-note
selection and annotated with a `*` suffix in cent annotations.

**Key differences from TonicAnchored:**
- Held notes carry their existing tuning into the new region first, providing the
  drift baseline for other voices.
- If `allowSplitSlurOfSustainedEvents` is off, sustained events remain whole.
- If `allowSplitSlurOfSustainedEvents` is on, a sustained event may be rewritten
  only when the continuation target differs from the carried tuning. This applies
  to both untied sustained notes and tied chains at existing tie boundaries.
- When no held note exists (no P1 candidate), drift resets to 0.0 (same
  as a fresh TonicAnchored computation without the rootOffset term).

**Drift boundary annotation (`annotateDriftAtBoundaries`, default off):**
When enabled together with FreeDrift, a `StaffText` is inserted above the first
eligible staff at each harmonic region boundary whenever |driftAdjustment| ≥ 0.5 ¢,
showing the accumulated pitch drift, e.g. `d=+3` or `d=-2`. This is independent of
the per-note `annotateTuningOffsets` toggle. A future drift-reset marker
(see `backlog_drift_reset.md`) will allow composers to insert deliberate
intonation resets at structural boundaries.

**Implementation:** `applyRegionTuning()` in `notationtuningbridge.cpp`,
controlled by `cfg->tuningMode()`. The drift computation happens between
the minimizeRetune (meanShift) calculation and the Phase 2 note-assignment loop.

### 11.3g Harmonic Priority (Just Intonation Only)

**Status: Design note.** The `HarmonicPriority` enum and `harmonicPriority()`
preference are not yet implemented. The current JI implementation uses a fixed
5-limit lookup table throughout.

#### Scope

Harmonic priority is only meaningful for just intonation family tuning systems.
For all other implemented systems the interval sizes are uniquely determined by
the system definition and no choice is available:

| Tuning system | Interval sizes | Harmonic priority |
|---------------|----------------|-------------------|
| Equal temperament | Fixed by definition | Not applicable |
| Pythagorean | Uniquely determined by stacking 3/2 fifths | Not applicable — equivalent to "Fifths first" JI |
| Quarter-comma meantone | Uniquely determined by tempering fifths for pure 5/4 thirds | Not applicable |
| Werckmeister / Kirnberger | Uniquely determined by their fixed compromises | Not applicable |
| Just intonation | Multiple legitimate pure ratio interpretations per interval | Applies |
| Adaptive JI (future) | JI ratios simultaneously optimized — same ambiguity | Applies |

Note that Pythagorean tuning is mathematically equivalent to the "Fifths first"
harmonic priority choice in just intonation — both derive all intervals by
stacking pure 3/2 fifths. They are the same system under different names.

The `HarmonicPriority` preference control must be hidden or disabled in the UI
whenever a non-JI tuning system is active.

#### Why the Choice Exists in JI

In just intonation, every interval has multiple legitimate pure ratio
interpretations derived from different prime factors. The choice of which primes
to include as primary consonances determines the character of the tuning:

| Interval | 3-limit (Pythagorean) | 5-limit (classical JI) | 7-limit (harmonic series) |
|----------|-----------------------|------------------------|---------------------------|
| Major third | 81/64 (+8¢) | 5/4 (-14¢) | 5/4 (-14¢) |
| Minor third | 32/27 (-6¢) | 6/5 (+16¢) | 6/5 (+16¢) |
| Perfect fifth | 3/2 (+2¢) | 3/2 (+2¢) | 3/2 (+2¢) |
| Minor seventh | 16/9 (-4¢) | 9/5 (+18¢) | 7/4 (-31¢) |
| Tritone | 729/512 (+12¢) | 45/32 (-10¢) | 7/5 (-17¢) |
| Augmented sixth | — | 225/128 (+41¢) | 7/4 (-31¢) |

Moving from 3-limit to 5-limit: thirds and sixths change dramatically (major
third drops 22¢). The fifth is unchanged.

Moving from 5-limit to 7-limit: sevenths and tritones change dramatically
(minor seventh drops 49¢). Thirds and fifths are unchanged.

The prime-limit choice implicitly sets the priority when simultaneous pure
intervals conflict — four-note chords cannot have all intervals pure
simultaneously, so the system must decide which intervals to prioritize:

- **5-limit:** fifths and thirds are primary; sevenths are derived and end up
  slightly impure.
- **7-limit:** fifths, thirds, and sevenths are all primary; other
  relationships absorb the remaining impurity.

#### The Preference

A single preference controls which prime limit is used as the primary
consonance target:

```cpp
enum class HarmonicPriority {
    /// Pure fifths only — Pythagorean ratios for all intervals.
    /// Bright, tense thirds. Historically appropriate for medieval
    /// and Renaissance music. Mathematically equivalent to the
    /// Pythagorean tuning system.
    FifthsFirst,

    /// Pure fifths and thirds — 5-limit just intonation.
    /// Warm, consonant triads. Standard for classical choral
    /// and orchestral JI. Default.
    ThirdsAndFifths,

    /// Full chord purity — 7-limit harmonic series.
    /// All chord tones (including sevenths) derived from pure
    /// harmonic partials. Seventh chords lock into zero-beat
    /// resonance. Appropriate for barbershop, close vocal harmony,
    /// natural brass ensemble, some jazz vocal.
    FullChordPurity,

    /// Context-dependent — follows the active style preset.
    /// The style preset maps chord function to prime limit:
    /// dominant seventh chords may use 7-limit while triads
    /// use 5-limit, etc.
    Automatic,
};
```

**Default:** `ThirdsAndFifths` — preserves current behavior (5-limit lookup
table) for all existing users.

#### UI Presentation

Exposed in **Preferences → Composing → Intonation** as a radio button group,
visible only when the active tuning system is Just intonation or Adaptive JI:

```text
Harmonic priority:  (only shown for Just intonation)
  ○ Fifths first       — pure fifths, Pythagorean thirds
  ● Thirds and fifths  — pure triads (standard)
  ○ Full chord purity  — harmonic series, all chord tones pure
  ○ Automatic          — follows style preset
```

#### Dominant Seventh Character

When `FullChordPurity` or `Automatic` is active, a second sub-preference becomes
relevant. The minor seventh in a dominant seventh chord has a unique musical
function — it is both a primary consonance (7-limit) and a functional dissonance
(resolution pull toward the tonic). The user may want to control this tension
independently:

```cpp
enum class DominantSeventhCharacter {
    /// Wide seventh (9/5, +18¢) — maximum tension, strong
    /// resolution pull toward tonic. Appropriate for functional
    /// harmony where V7 → I resolution is the goal.
    Tense,

    /// Pure harmonic seventh (7/4, -31¢) — zero-beat resonance,
    /// floating quality. Appropriate for static dominant color,
    /// barbershop tag chords, natural brass sonority.
    Natural,

    /// Pythagorean seventh (16/9, -4¢) — close to equal temperament.
    /// Neutral character, minimal deviation from 12-TET.
    Neutral,
};
```

**Default:** `Natural` when `FullChordPurity` is active.

This control only affects the minor seventh of dominant seventh chords — not the
minor seventh in minor seventh chords (`Dm7`), half-diminished chords, or other
contexts where the seventh does not carry dominant function. Other intervals
(thirds, fifths, extensions) are not affected by this preference.

UI: shown as a sub-option beneath `FullChordPurity` and `Automatic` in the
harmonic priority group, enabled only when those options are selected.

#### Relationship to the Generalized Tuning Algorithm

The `HarmonicPriority` preference is the user-facing control for a deeper
architectural choice: which prime limit to use when computing just intonation
ratios.

The full generalized algorithm (§11.2b, deferred) would:

- Identify each note's harmonic function within the chord.
- Select the prime limit based on `HarmonicPriority` and chord function.
- Compute the canonical ratio via shortest lattice path (minimum Tenney height
  within the chosen prime limit).
- Resolve conflicts between simultaneously sounding notes via the simultaneous
  optimizer.
- Apply context modifiers (dominant tension, leading-tone pull, resolution
  target).

The current fixed 5-limit lookup table is a degenerate case of this algorithm —
it hardcodes `ThirdsAndFifths` with no context modifiers and no simultaneous
optimization. The `HarmonicPriority` preference adds the first degree of freedom
without requiring the full algorithm to be implemented.

#### Implementation Sequence

- Add `HarmonicPriority` and `DominantSeventhCharacter` enums to
  `tuning_system.h`.
- Add `harmonicPriority()` and `dominantSeventhCharacter()` to
  `IComposingAnalysisConfiguration`.
- Wire through `ComposingConfiguration` → `composingpreferencesmodel` → QML
  (same pattern as `TuningMode`).
- In `applyRegionTuning()` and `applyTuningAtNote()`, branch on
  `harmonicPriority()` when selecting the ratio for each interval:
  - `FifthsFirst`: use Pythagorean ratios throughout.
  - `ThirdsAndFifths`: use the current 5-limit table (no change).
  - `FullChordPurity`: use 7-limit ratios for sevenths and tritones, 5-limit
    for thirds and fifths, and apply `DominantSeventhCharacter` for dominant
    seventh context.
  - `Automatic`: consult the style preset for chord-type → prime-limit mapping.
- UI: radio group in `ComposingAnalysisSection.qml`, visible only when tuning
  system is JI or Adaptive JI.
- Validate on a cappella choral scores with known tuning practice (barbershop
  corpus when available).

### 11.4 Score Mutation for Tuning Application

Applying a non-equal temperament writes cent deviations to individual notes via
`Note::undoChangeProperty(Pid::TUNING, cents)`.  For notes that attack exactly at
the target tick this is a direct property change.  Sustained notes — notes that
started before the target tick but are still sounding — require score mutation
because tuning is a single value per note and the note's harmonic role may differ
from when it first attacked.

#### Split-and-slur approach

A sustained note that needs a different tuning at the target tick is split there
into two notes connected by a slur.  The first half (note_A) keeps its existing
tuning.  The second half (note_B) receives the offset for its role in the current
chord.

A **slur** (not a tie) connects the two halves.  This is a deliberate choice:
MuseScore's playback engine treats tied notes as one continuous sound with a single
tuning value, so a tie would silently discard note_B's tuning.  A slur produces two
independent playback events with legato articulation, allowing each half to carry
its own tuning offset.

The split is **visible** — the score shows two shorter notes connected by a slur.
This is the simplest correct approach and is fully undoable via MuseScore's standard
undo system.

**Backlog:** An alternative invisible-voice strategy (silent original + invisible
playing pair in a spare voice) was designed and prototyped but deferred.  It requires
a UI indicator for tuning-applied notes before it is practical.  See
`backlog_invisible_split.md`.

#### Split threshold

A split is only performed when the difference between the note's current tuning and
the desired tuning exceeds `kEpsilonCents` (0.5 cents).  This avoids unnecessary
score mutations for inaudible differences.

#### Slur chain management

When successive splits are applied to the same note (e.g. a whole note in 4/4 with
quarter-note chord changes), existing forward slurs are transferred from the
shortened original to the end of the new note_B chain.  This produces a sequential
slur chain (1→2→3→4) rather than a fan pattern (1→2, 1→3, 1→4).

#### Note collection filter

Chord analysis filters notes with `visible = true` and `play = true`, excluding
both silent notes and any future invisible tuning artifacts from the pitch-class
collection.

#### Idempotency

After a split, note_A ends exactly at the target tick (`noteEnd == anchorTick`),
which is excluded by the `noteEnd <= anchorTick` guard in the lookback loop.
Re-running the operation on the same target tick does not produce additional splits.
Phase 2 (attack-note tuning) handles re-tuning of notes at the anchor tick,
including note_B from a previous split.

#### Bridge function

Declared and defined in `mu::notation` (not in the composing module — requires `Note*`):

```cpp
// notation/internal/notationtuningbridge.h
namespace mu::notation {
bool applyTuningAtNote(const mu::engraving::Note* selectedNote,
                       const mu::composing::intonation::TuningSystem& system);
} // namespace mu::notation
// defined in src/notation/internal/notationtuningbridge.cpp
```

The context menu path passes the tuning system explicitly (resolved from the user
preference at menu-build time).  Other callers (chord track population, region
tuning) use `preferredTuningSystem()` to read the preference at call time.

The caller is responsible for undo grouping (`startCmd`/`endCmd` or the
`NotationInteraction::startEdit`/`apply` pattern).  The function does not manage
its own undo scope.

Returns `false` when the selected note is invisible (no-op) or when fewer than 3
distinct pitch classes are sounding (insufficient data for chord identification).

### 11.5 Region Analysis and the Chord Track

**Status: Implemented** — `analyzeHarmonicRhythm()` is declared and defined in
`notation/internal/notationcomposingbridge.h/.cpp`; `populateChordTrack()` is declared
and defined in `notation/internal/notationimplodebridge.h/.cpp` (both in `mu::notation`
namespace).  Exposed as the "Implode to chord track" action in the Tools menu (see §12.1b).

Single-note analysis (status bar display, single-chord tuning) is the foundation.
Region analysis extends this to a time range, producing a complete harmonic analysis
with chord symbols, roman numerals, and an optional note reduction across an entire
passage.

#### User interaction — selection-based targeting

There is no dedicated staff type or property for the chord track.  The user's
**selection determines the target**:

1. **Select a range on any staff** and invoke "Implode to chord track."
2. The system analyzes all **other** non-hidden tonal staves within that time range.
3. The selected region is cleared and populated with the harmonic reduction.

The target staff is excluded from the analysis input — it is the output, not a
source.  This prevents feedback loops when re-running the analysis.

**Any existing content in the selected region is overwritten.**  Re-analysis after
score edits simply selects the same range and runs again.  If the user wants to
preserve a previous analysis, they can undo or copy it elsewhere first.

#### On-demand staff creation

If no suitable target staff exists yet, the action offers to **create one**:

1. Opens MuseScore's standard Add Instruments dialog — the user picks whatever
   instrument they want (piano, organ, a single-line sketch staff, etc.).
2. The new part is inserted (e.g., at the bottom of the score).
3. A default name like "Chord Track" is suggested (soft hint for future automation,
   not enforced).
4. The selected tick range is applied to the new staff and population proceeds.

The instrument choice is the user's.  The system adapts its output to what the
staff supports (see below).

#### Adaptive output by staff type

- **Grand staff** (e.g., piano, organ): root on the bass staff, upper-structure
  chord tones on the treble staff, chord symbols above, roman numerals below.
  This is the richest output — a full keyboard reduction.
- **Single staff** (e.g., treble clef sketch): chord symbols and roman numerals
  only (no note reduction), or a single-staff reduction with root and upper
  structure combined.  The user's instrument choice drives the output.

#### Harmonic rhythm detection

The region analysis scans **all non-hidden tonal staves** (excluding the target
staff) within the selected time range, left to right, to identify every tick
where the sounding pitch-class set changes — i.e. where any instrument starts or
stops a note.  Each such tick is a potential chord boundary.

Chord analysis runs at each boundary tick. In the default smoothed mode,
consecutive boundaries that produce the **same root and quality** are collapsed into a
single harmonic region, and sub-quarter-note fragments are absorbed so tuning and other
range operations do not overreact to ornaments. Chord-staff population uses the
preserve-all mode instead: every detected harmonic event is kept, even when adjacent
events share root and quality, and sustained carry-in notes still contribute at the new
region start.

The result is a sequence of harmonic regions, each with:
- Start tick and end tick (duration = harmonic rhythm)
- Chord analysis result (root, quality, extensions)
- Key/mode analysis result

#### Chord track population (grand staff)

The selected region is cleared and populated from the region sequence:

**Treble clef (staff 1):** Upper-structure chord tones in close position, placed
in the C4–C5 range.  Duration matches the harmonic region.  When voicing analysis
is available (future), the inferred voicing (drop 2, spread, etc.) replaces the
close-position default.

**Bass clef (staff 2):** Root note only, showing bass motion.  Placed in a
natural bass register (C2–C3 range).

**Chord symbols** (`HarmonyType::STANDARD`) attached above the treble staff —
controlled by the "Write chord symbols to staff" preference.

**Chord function notation** attached below the treble staff — either
`HarmonyType::ROMAN` (Roman numerals) or `HarmonyType::NASHVILLE` (Nashville
numbers), selected by the "Chord function notation" preference (None / Roman
numerals / Nashville numbers).  Roman and Nashville are mutually exclusive on
the staff because they encode identical information; displaying both would be
redundant and legibility-destroying.

**Key/mode annotations** written as staff text at key region boundaries —
controlled by the "Write key/mode annotations" preference.

The instrument's sound makes the harmonic reduction audible on playback — the
composer can audition the harmonic progression independent of the orchestration.

#### Close-position reduction algorithm

Given a chord analysis result with root pitch class and chord tones:

1. Sort pitch classes ascending from the root.
2. Place the root in the bass clef at C2–C3 (nearest octave to middle of range).
3. Stack remaining pitch classes above C4, each ascending from the previous, within
   one octave.  This produces close-position voicing.
4. When voicing inference is implemented (Phase 3), the inferred voicing replaces
   step 3.  The algorithm becomes: "given these pitch classes and the detected
   voicing type, produce the appropriate spacing."

This mirrors how arrangers think — the chord track is a **keyboard reduction** of
the full score, showing harmony and rhythm stripped of orchestration.

#### Relationship to MuseScore's chord symbol realization

MuseScore's existing `Score::cmdRealizeChordSymbols()` converts `Harmony` elements
into notes on a single track.  It supports voicing types (close, drop 2, 3-note,
4-note, 6-note) but places all notes including the bass on one staff.

Our approach differs in two ways:

1. **Grand staff separation** — root on the bass staff, upper structure on treble.
   This matches standard lead-sheet layout and is more readable.
2. **Analysis-derived** — their flow is symbol → notes (user typed the chord,
   system voices it).  Ours is notes → symbol → reduction-notes (system infers the
   chord from sounding notes, then produces the reduction).  The existing
   `RealizedHarmony` and `Voicing` infrastructure may be useful when building our
   voicing generator, but the analysis-first workflow is new.

#### Rest analysis

Single-note analysis requires a selected note as the anchor.  Region analysis does
not — it analyzes at arbitrary ticks based on the harmonic rhythm.  A new entry
point `analyzeHarmonicContextAtTick(Score*, Fraction tick, ...)` provides analysis
without requiring a note anchor.  It uses the same collection and analysis logic,
just without the "selected note" starting point.  This also enables annotation at
ticks where the target staff has a rest.

#### Relationship to intonation

The chord track and intonation are **independent workflows** that share the chord
analysis engine but have no other coupling:

| | Chord track ("Implode to chord track") | Intonation |
|---|---|---|
| **Purpose** | Composition and analysis tool | Playback quality |
| **Output** | Visible: notes, chord symbols, chord function notation (Roman or Nashville), key annotations | Invisible: cent offsets on existing notes |
| **Target** | Any staff the user selects (or creates on demand) | Any staff the user selects |
| **Requires** | Range selection on the target staff | Any note or range selection |
| **Score impact** | Overwrites target region with reduction | Split-and-slur on sustained notes only |

Neither workflow depends on the other.  A user can intonate without a chord track,
and can populate the chord track without applying tuning.  Both use the same
`analyzeHarmonicContextAtTick` entry point internally and the same user-preferred
tuning system (§11.2a).

#### Additional Chord Track Annotations — Planned

The following annotations are planned for the chord track. All derive from data already
computed or planned in the analysis engine — no new analytical components are required
beyond what is already described in this document.

**Non-diatonic chord highlighting** (ready to implement)

Chords where `ChordAnalysisResult.diatonicToKey` is `false` receive distinct visual
treatment — a different color or border on the chord block. Makes borrowed chords,
secondary dominants, and chromatic passing chords immediately visible without requiring
the user to read each Roman numeral. No additional analysis required — the flag is already
computed.

**Relative and parallel key relationships** (ready to implement)

When the inferred key changes, the key label annotation includes the relationship to the
previous key:

- Same `keySignatureFifths`, different `isMajor` → "→ relative minor" / "→ relative major"
- Same `tonicPc`, different `isMajor` → "→ parallel minor" / "→ parallel major"
- `keySignatureFifths` differs by ±1 → "→ dominant key" / "→ subdominant key"
- Other differences → circle of fifths distance stated: "→ mediant (E major)"

All relationships are pure arithmetic on `keySignatureFifths`, `tonicPc`, and `isMajor` —
no additional analysis required.

**Key stability indicator** (depends on §5.7 normalized confidence)

The confidence of the key/mode inference is indicated through staff text annotation:

- Confidence above 0.8 — no annotation (confident, label stands alone)
- Confidence 0.5–0.8 — question mark appended to key label: "D Dorian?"
- Confidence below 0.5 — suppress key-dependent chord-track annotations rather than printing a tentative label

The chord-track writer uses the same thresholds to reduce misleading downstream output:

- Roman/Nashville function labels are written only when confidence is at least 0.5
- Key signatures, modulation relationship labels, pivot labels, borrowed-chord markers,
  and cadence markers are written only when confidence is at least 0.8

Requires normalized confidence scores (§5.7) to be implemented first. Until then, raw
scores from `KeyModeAnalysisResult` can be used with approximate thresholds as a temporary
measure.

**Key distance / borrowed chord annotation** (ready — basic version)

When a chord is non-diatonic to the current inferred key, a small annotation identifies
which nearby key it belongs to — making the borrowing relationship explicit.
Implementation: for each non-diatonic chord, compute which keys contain it as a diatonic
chord, then select the closest key by circle-of-fifths distance to the current inferred
key. Requires the chord dictionary and scale/mode dictionary (§7.1, §7.2) to be populated.

**Cadence markers** (basic version ready, improved with phrase analysis)

Detected cadences annotated above the chord track staff at phrase boundaries:

- Authentic (V→I): Roman numeral sequence in the inferred key
- Half cadence (→V): ending on dominant
- Deceptive (V→vi): dominant resolving to submediant
- Plagal (IV→I): subdominant to tonic

Basic detection uses a heuristic: cadential chord pairs followed by a significant harmonic
change (new key region, long held chord, or rest). Full accuracy requires phrase structure
analysis (planned but not yet implemented). Basic version is implementable now from the
harmonic rhythm regions already computed.

**Modulation path annotation** (basic version ready)

At key region boundaries, annotate the pivot chord when one exists:

"pivot: IV in G → ii in D"

Implementation: the last chord before the key boundary that is diatonic to both the old
and new key is the pivot. `formatRomanNumeral()` is called twice — once with the old key
context, once with the new — to produce both Roman numerals. When no pivot chord exists
(direct chromatic modulation), annotate as "direct modulation". Enharmonic reinterpretation
detection is a future refinement.

### Annotate path annotation layers (Roman numeral mode)

When the user selects a region and runs "Annotate to chord track" in Roman
numeral mode, the following layers are written as StaffText annotations:

- Chord symbols
- Roman numerals (with chromatic/borrowed labels: ♭VII, ♭III etc.)
- Cadence markers (PAC, HC, DC, PC) — **implemented** (Session 14);
  uses `detectCadences()` in `notationcomposingbridgehelpers.cpp`
- Pivot chord labels — **implemented** (Session 14); uses
  `detectPivotChords()` in `notationcomposingbridgehelpers.cpp`
- Tonicization labels (V/V, V/ii, V/IV etc.) — **NOT YET IMPLEMENTED**
  (deferred; no `relativeRoot`/secondary-dominant field in
  `ChordFunction`; requires standalone implementation first)
- Augmented sixth chord labels (It+6, Fr+6, Ger+6) — **NOT YET
  IMPLEMENTED** (deferred; no aug-sixth classifier in composing module;
  requires standalone implementation first)

Nashville annotation mode emits chord symbols and Nashville numbers only.
No cadence markers, no pivot labels, no tonicization labels.

**Cadence detection** (`detectCadences`): pairs of consecutive in-selection
regions are examined. PAC = V→I or viio→I with assertive key confidence
(≥ 0.8) on both. PC = IV→I. DC = V→vi. HC = last in-selection region is
a dominant (degree V or viio). Label is placed at the resolution tick; if
the resolution region is in lookahead (past `selectionEndTick`), the label
is placed at the preparatory chord's tick instead. One harmonic region of
read-only lookahead is used.

**Pivot detection** (`detectPivotChords`): scans for assertive key
transitions (consecutive regions with different `keyTonicPc` or `keyMode`).
The new key is confirmed by finding at least one additional assertive region
within `kMaxPivotLookaheadRegions = 8` regions past the boundary. The pivot
chord is the last in-selection chord diatonic to both the old and new key.
The pivot label format is `vi → ii` (U+2192 RIGHT ARROW, no "pivot:" prefix,
no key-name context). Analysis window extended by up to
`kMaxPivotLookaheadRegions × 1 whole note` past `selectionEndTick` in Roman
numeral mode; no annotations written outside the selection boundary.

**Annotation color policy:**

Interactive annotate path (human use): annotations written in score default
color (black). Publication-ready, indistinguishable from manually entered
symbols. No user preference exposed.

Automated pipeline (`batch_analyze` headless): annotations written in red,
hardcoded in `tools/batch_analyze.cpp`. Never exposed to human user. Used by
`auto_review.py` to filter our inferred annotations from pre-existing score
content by color comparison.

#### Future Extensions — Chord Track

The following are possible future extensions. No implementation is planned.

**Tension curve strip** — a small graph below the chord track staff showing harmonic
tension over time, derived from voice leading complexity and distance from tonic. Connects
to the tension curve editor (§12.4) when implemented.

**Phrase structure markers** — bracket notation showing detected phrase beginnings and
endings. Requires phrase structure analysis component.

**Harmonic rhythm emphasis** — visual weight on chord blocks proportional to harmonic
rhythm density, making acceleration toward cadences immediately visible.

**Actual bass line overlay** — optional display of the original score's bass voice rather
than just the chord root, revealing bass line character (walking bass, pedal point, chromatic
descent).

### 11.6 Region Intonation

Intonation over a region extends the single-note tuning workflow (§11.4) to a
time range. No dedicated staff is needed — intonation is a playback-only concern
that does not add visible notation beyond the split-and-slur artifacts.

For ordinary untied notes, the user selection defines exactly what gets retuned.
For non-partial tie chains, the chain is treated as an indivisible tuning event:
if any note in the chain intersects the selected region, the tuning offset is
applied to the entire chain, including members outside the selected span.

#### Selection-based scoping

The selection determines the scope:

- **Single note** — tune that note using the harmonic context at its tick (the
  existing single-note workflow from §11.4).
- **Range on one or more staves** — detect harmonic rhythm within the range,
  compute a tuning plan per region, split and tune all notes accordingly.
- **Whole staff or Ctrl+A** — same as range, applied to the full extent.

In every case the user selects what they want tuned; the tuning system is read from
the user preference (§11.2a).  The analysis engine figures out the harmonic context
at each tick, and the tuning logic handles the rest.

For non-partial tie chains, the tuning annotation is placed at the first note in the
chain even when that note lies outside the visible selection. This makes the one-event
semantics explicit in the score.

#### Algorithm

1. **Harmonic rhythm detection** — same scan as §11.5: identify every tick in the
   selected time range where the sounding pitch-class set changes across all
   non-hidden tonal staves.  Run chord analysis at each boundary.  Collapse
   consecutive same-chord regions.
2. **Compute tuning plan** — for each harmonic region and each sounding note in the
  selected staves, compute the desired tuning offset. For non-partial tie chains,
  choose the chain authority note (earliest anchor-marked note, otherwise first note
  in the chain), compute the offset once from that authority note's harmonic context,
  and reuse that same offset for every note in the chain. Compare against each note's
  current tuning. Record which notes need changes and which sustained untied notes
  need splits.
3. **Execute splits** — because all boundaries are known upfront, the complete
   split plan is computed before any mutations.  Each sustained note crossing a
   region boundary is split-and-slurred once (§11.4 mechanics).  No cascading
   splits.
4. **Apply tuning** — set cent offsets on all notes (attack and newly-split)
  via `undoChangeProperty(Pid::TUNING, ...)`. If a non-partial tie chain intersects
  the selected range, the final chain offset is written to every note in that chain,
  even when some members lie outside the selection.

The entire operation is one undo group.

#### Entry points

```cpp
// notation/internal/notationtuningbridge.h
namespace mu::notation {
bool applyRegionTuning(mu::engraving::Score* score,
                       const mu::engraving::Fraction& startTick,
                       const mu::engraving::Fraction& endTick);
} // namespace mu::notation
// defined in src/notation/internal/notationtuningbridge.cpp
```

Called from `NotationInteraction::tuneSelection()`, which determines the tick range
from the current selection (range, single note → note span, or full score fallback).
Exposed as the `"tune-selection"` action in the Tools menu.

#### Shared split helper

The split-and-slur logic used by both single-note tuning (§11.4 Phase 3) and region
tuning is factored into a template helper:

```cpp
template<typename TuningFn>
bool splitAndTuneChord(Score* sc, Chord* chordMut,
                       const Fraction& splitTick, TuningFn tuningFn);
```

This shortens the original chord at the split tick, creates a continuation chord
bridged by a slur, and applies the caller-supplied tuning function to the
continuation's notes.  Both `applyTuningAtNote` and `applyRegionTuning` use this
helper, eliminating duplicated mutation logic.

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

### 12.1b Menu Actions (Implemented)

Two actions are registered in the Tools menu via `notationuiactions.cpp` and wired
through `notationactioncontroller.cpp` and `appmenumodel.cpp`:

| Action ID | Menu label | Trigger |
|-----------|-----------|---------|
| `implode-to-chord-track` | Implode to chord track | Requires a range selection on a grand-staff part; analyzes all other staves and populates the selected part with a harmonic reduction |
| `tune-selection` | Tune selection | Tunes the selected note or range using the user-preferred tuning system (§11.2a) |

Both actions are gated by `canReceiveAction(actionCode)` in
`NotationActionController`, which checks that a score is open and the required
selection exists.

The **"Implode to chord track"** submenu is rebuilt dynamically whenever:
- A different score is opened (`currentNotationChanged`)
- A part is added or removed in the current score (`partsChanged`)

This ensures the submenu is enabled as soon as a valid chord staff is added and
disabled immediately when one is removed, without requiring the user to reopen the
menu.  Implemented via `rebuildChordTrackMenu()` called from both notification paths
in `AppMenuModel::setupConnections()`.

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

### Automated annotation review (planned, post-RFC)

`tools/auto_review.py` — headless pipeline that loads a directory of scores
via `batch_analyze`, runs the annotation path, and passes structured output
to an LLM judge (Anthropic API) for music-theory-correctness evaluation
without corpus ground truth dependency. Produces per-score judgment reports
and aggregate quality summaries. Calibration requires a small hand-verified
set of 10–15 scores. Intended as a scalable complement to corpus validation
for repertoire not covered by DCML/WiR/Bach chorale annotations.

**Three-mode design:**

Mode 1 — No pre-existing symbols: judge evaluates our output against music
theory rules only.

Mode 2 — Pre-existing symbols present: treated as a second analyst's opinion,
not ground truth. Judge comments on agreements and disagreements without
scoring disagreements as errors. Framing: "two analysts may reach different
but equally valid conclusions."

Mode 3 — Known ground truth corpus (DCML/WiR/Bach chorales): judge scores
errors directly against reference annotations.

Mode detection is automatic: if Harmony elements exist in the score before
annotation, use Mode 2. If the score is in the DCML registry, use Mode 3.
Otherwise use Mode 1.

**Report format:**
Designed as input to a Claude conversation, not a standalone verdict.
Requirements:
- Compact enough for many scores in a single context window
- Structured to make cross-score patterns visible
- Flags specific measure locations for drill-down
- Separates formatter artifacts (actionable) from analytical disagreements
  (judgment call) from expected limitations (ignore)
- Includes score metadata per entry: title, composer, key, time signature,
  texture type, preset used

**Pipeline boundary:**
Entire `auto_review.py` pipeline lives in `tools/` — no MuseScore core
involvement. Operates on JSON output from `batch_analyze`. Pre-existing
chord symbols read from score as `writtenSymbols` field in JSON, our
inferred symbols as `inferredSymbols` field. Color (red) used as filter
criterion when both are present in the same score file.

---

## 15. Development Phases

*Current implementation status, remaining items, and immediate next steps are in STATUS.md.*

### Development Tools

The following tools live in `tools/` and are **not part of the shipping product**.
They are compiled/run only in development builds (`MUE_BUILD_ENGRAVING_DEVTOOLS=ON`).

**`tools/batch_analyze.cpp`** — headless C++ analysis tool.
Loads a MusicXML (or MSCZ/MSCX) file, runs our harmonic analysis pipeline
(boundary detection, ChordAnalyzer, KeyModeAnalyzer) without any UI, outputs JSON.
Uses the same module-initialization pattern as MuseScore's existing test
infrastructure (DrawModule + EngravingModule + MusicXmlModule, `MScore::noGui = true`).
Compiled as a separate executable; linked against `engraving`, `composing_analysis`,
and `iex_musicxml` — no notation module required. Because the tool only consumes
logical score structure, it deliberately skips forced post-load layout; this avoids
legacy native MSCX cache-overflow crashes (for example Mozart `K533-3`) without
changing the emitted harmonic-analysis JSON.

**`tools/music21_batch.py`** — exports scores from music21's corpus to MusicXML
and produces a JSON harmonic analysis per score.  Supports any composer via
`--composer NAME` (default: `bach`).  The music21 corpus directory is resolved
automatically from the installed library — no hardcoded path required.
Working copies (XML + JSON) are written to `tools/corpus/` using short names
(`bwv1.6.xml`, `beethoven_opus132.xml`, `beethoven_opus59no1_movement1.xml`).
Note: music21's `romanNumeralFromChord()` is stateless and local — it does not
use temporal context.  Key detection uses Krumhansl-Schmuckler (global, stored as
`detectedKey`) and FloatingKey sliding window (local, stored as `keyLocal` per
region).  Both are stored for comparison.

**`tools/inject_m21_rn.py`** — injects music21's Roman numeral labels into an
exported MusicXML file as `<direction type="words">` elements above the first staff.
Source XMLs are read from `tools/corpus/`; annotated output is written to
`tools/corpus_m21_xml/` (default).  Open the result in MuseScore alongside the
chord staff output to compare music21's analysis with ours visually.

**`tools/compare_analyses.py`** — three-level comparison of our analysis against
music21's.  Levels: chord identity (key-independent), key context, Roman numeral
string.  Classifies disagreements into `full_agree`, `near_agree`,
`chord_agree_rn_differs`, `chord_agree_key_differs`, `chord_disagree`, `unaligned`.
Also checks music21's chord against our top-2 alternatives before declaring
`chord_disagree`, classifying such cases as `near_agree`.
The script reports all six comparison categories.  Chord identity agreement rate —
the most diagnostically meaningful figure, counting cases where root pitch class and
quality match regardless of key context — must currently be computed manually as
(full_agree + chord_agree_rn_differs + chord_agree_key_differs) / total aligned
regions.  Adding this as an explicit script output is a planned improvement.

**`tools/run_validation.py`** — orchestrates the full pipeline across all chorales.
Produces an HTML validation report.  Works with any composer supported by
`music21_batch.py`.

```bash
# Full Bach corpus
python tools/run_validation.py --output tools/

# Single chorale for spot-checking
python tools/run_validation.py --single bach/bwv66.6
```

---

### Submission Roadmap (pre-PR phases)

Short-term milestones tracking readiness for MuseScore contribution.

#### Phase 1 — Analysis foundation *(complete)*

The Phase 1 analysis engine, status bar integration, and basic chord staff are
implemented and passing all targeted tests. See STATUS.md for test counts.

#### Phase 2 — Inferrer stabilization **COMPLETE — `bc6f2edb`**

2a — Key annotation display: confirmed working. `minKeyStabilityBeats=8.0`
  suppresses transient key changes. Mode name threshold correctly applied.

2b — Corpus re-run: 64.6% weighted direct DCML confirmed stable after
  formatter and key-detection fixes (Corelli 70.3%, Dvorak 79.2% spot-checked).

2b2 — Complete-voicing jazz transcription QA (2026-04-17): My Funny Valentine
  (Bill Evans, Some Other Time 1968, Felix B. transcription) — 185-measure
  three-layer comparison (our annotations vs human analyst transcription vs
  third-party plugin). Agreement with human transcription: approximately 75–80%
  exact or near-exact chord symbol match. Extended runs of perfect
  measure-by-measure agreement: m.82–102, m.151–185, Coda (m.179–185). Complex
  extended chords correctly identified: AbΔ7#11, F-13, G7(#9b13), EbMaj7add13/Ab,
  AbMaj7add13(no3)/Gm7/F, GbMaj7b9b5, GbMaj7add13, FmMaj7, CmMaj9, Asus(add9b5),
  Eb7sus#5/B, G7sus#5#11, and many others. Bass solo ostinato (F13/Eb, m.106–142):
  correctly held across 36 measures. Pedal point (Bb pedal, m.106): correctly labelled.
  The 75–80% figure on complete voicings vs 64.6% weighted corpus figure reflects the
  sparse-voicing limitation: the vertical analyzer performs substantially better when
  bass notes and complete chord voicings are present. Both figures are cited in the RFC
  with this context. Note: `Dsdim`/`Fsdim` visual artifacts in screenshots are Campania
  font rendering artifacts (§5.8), not formatter output bugs. Internal strings confirmed
  correct via edit dialog.

2c — Benchmark set Rule 12 sign-off: PASSED 2026-04-14.
  BWV 227/7: E minor key annotation, correct Roman numerals ✓
  Chopin BI16-1: single G major region at measure 1 ✓
  Dvořák op08n06: Bb major context, cadence detection, confident opening ✓

2d — Known limitations documented: see §5.8 (updated 2026-04-13 with 10-score
  inspection findings).

2e — Pre-submission backlog items fixed: formatter sussus/bassIsRoot bugs
  (commit `4c35da17`), relative major/minor key ambiguity (commit `3ba80cb7`).

#### Phase 3 — Submission fork preparation *(next)*

- Create submission scope document (`docs/submission_scope.md`)
- Identify files in scope vs out of scope for the PR
- Create fork branch containing only submittable code
- Final PR readiness review

---

### Long-term project phases (post-submission)

### Phase 1 — Analysis Foundation

- `TemporalContext` struct — previous chord continuation scoring
- Duration sensitivity for passing events
- Modal extension — melodic minor and harmonic minor families (21 modes total)
- `KeyModeAnalysisResult` extended with `modeIndex` and `tonicPc`
- Normalized confidence scores in both result structs
- Monophonic/arpeggiated chord inference
- Secondary dominant Roman numeral notation
- Validation pipeline against Bach chorale corpus; DCML and ABC Beethoven corpora

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

- `TuningCalculator` — tuning systems in `composing/intonation/` (JI, Pythagorean, meantone, well temperaments)
- Per-instrument configuration
- `DriftManager` — drift prediction and correction
- Tuning system selector (equal, just, meantone, well temperament, Pythagorean) — user preference in Preferences → Composing
- Region tuning — "Tune selection" in Tools menu; harmonic rhythm analysis + split-and-slur

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

*Document version: 3.26 — Campania font rendering artifact (`Dsdim`/`Fsdim`) documented as MuseScore core issue in §5.8; complete-voicing jazz QA evidence added (MFV 185-measure three-layer comparison, 75–80% agreement); `isValidBassNoteName` guard added to `formatSymbol` suppressing slash chord when bass name is not a plain note name; chord name in bass field bug documented and fixed; RFC draft at `docs/rfc_musescore_forum_post.md`; chordlist.cpp upstream bug report draft at `docs/chordlist_bug_report.md`; previous: 3.25 — cadence markers (PAC/HC/DC/PC) and pivot chord labels (vi → ii format, U+2192) wired into annotate path via `detectCadences()`/`detectPivotChords()` helpers; tonicization and augmented sixth labels deferred (no classifier implemented); pivot annotation format updated from verbose "pivot: vi in C → ii in G" to concise "vi → ii"; `kMaxPivotLookaheadRegions = 8` lookahead for pivot confirmation; 13 new notation unit tests (45/49 passing, 4 deferred); previous: 3.24 — B/H naming convention fix for German locale chord names in jazz path; previous: 3.23 — annotation color policy documented (black for human use, red for headless pipeline); auto_review.py three-mode design and report format requirements added; previous: 3.22 — annotate path Roman numeral layer extended to include cadence markers, pivot labels, tonicization labels, and augmented sixth chord labels (Standard/Baroque presets only); automated annotation review tool design recorded; Session 5 jazz QA outcomes documented; previous: 3.21 — the plateau target is now qualified for full-texture tonal corpora only, the highest-ROI roadmap is reordered so texture fixes precede evaluation separation and confidence calibration, Rule 12 adds a permanent benchmark score set for visual review, region identity modes are now decided conceptually (harmonic summary vs as-written), and the Mozart 26.7% direct-DCML figure is explicitly marked as a thin-texture/non-comparable case; previous: 3.20 — confidence interpretation is now documented explicitly as heuristic rather than probabilistic, a reasonable "good enough" plateau is defined for the current vertical tertian engine, the highest-ROI pre-plateau roadmap is recorded, and the stale Mozart `59.4%` agreement reference is corrected to the current 26.7% direct-DCML root-agreement figure; previous: 3.19 — `batch_analyze` now skips forced post-load layout in headless mode because analysis uses logical score data only; this avoids the legacy native MSCX cache-overflow crash on Mozart `K533-3` while preserving JSON output parity with the mirrored `score.mxl` path; previous: 3.18 — same-key-signature key-mode selection now uses tonal-center comparison with a diatonic raw-score guard, preventing the Mozart `K279-1` opening from flipping to spurious `F Lydian`, while Roman/Nashville analysis annotations are excluded from chord-symbol-driven path activation; previous: 3.17 — Milestone A3 confidence gating is implemented for chord-track exposure, the key-confidence thresholds now suppress low-confidence key-dependent annotations, and the Dvorak `op08n06` regression locks that behavior in; previous: 3.16 — Milestone A benchmark passages are recorded, the reusable batch/notation parity harness is documented, and BWV 227.7 plus Chopin BI16-1 now pass exact parity gates; previous: 3.15 — final post-`bassNoteRootBonus` corpus baselines are recorded, Schumann slash-chord spellings are confirmed not to be a comparator artifact, Dvorak op08n06 is accepted as genuine ambiguity, and Corelli walking-bass sus/slash artifacts are documented as a deferred limitation; previous: 3.14 — `populateChordTrack()` now absorbs sparse intra-measure gaps into neighboring written regions so BI16-style chord-track generation does not leave mixed chord/rest measures; previous: 3.13 — `bassNoteRootBonus` conditioning is now implemented with tiered support checks, corpus validation results are recorded, and the Chopin BI16-1 notation mismatch is resolved by aligning `PreserveAllChanges` collapse semantics with the batch path; previous: 3.12 — `bassNoteRootBonus` conditioning is now implemented with tiered support checks, corpus validation results are recorded, and the remaining Chopin BI16-1 boundary issue is separated from the root-scoring fix; previous: 3.11 — four-corpus score inspection now documents the shared `bassNoteRootBonus` failure mechanism and a concrete conditioning strategy for the fix; previous: 3.10 — 2026-04-09 score inspection confirms `bassNoteRootBonus` as the primary cross-corpus failure mode and the highest-priority next action; previous: 3.9 — removed the false pedal-marking analyzer limitation after Rule 11 score inspection confirmed sparse texture rather than analyzer failure; previous: 3.8 — Rule 11 added: representative MuseScore Studio score inspection is required before diagnosis when corpus statistics are anomalous or a texture-specific failure mode is suspected; previous: 3.6 — §5.8 now records two next-session analyzer limitations: pedal-aware Jaccard boundary detection for piano beat-1 accompaniment patterns and the cross-corpus `bassNoteRootBonus` miscalibration signal; previous: 3.5 — Rule 10 added: shared note collection, boundary detection, key/mode resolution, and chord-scoring logic must live in `src/composing/` whenever bridge and batch_analyze must agree; §4.1c duplicate-path technical debt now references Rule 10 explicitly; Bach baseline corrected to 50.0% WIR structural (2026-04-09), superseding the older 83.7% onset-only/music21 figure; previous: 3.4 — §4.1c batch classical path now uses Jaccard boundaries plus smoothed regional accumulation, reducing note-collection divergence from three active paths to two duplicate regional collectors; previous: 3.3 — §4.1c duplicate note-collection-path technical debt documented, including the batch_analyze jazz-path duplicate regional collector and the onset-only classical batch path that bypasses regional accumulation; previous: 3.2 — §4.1c piano pedal-sustain gap documented as the remaining Romantic-piano accumulator limitation; previous: 3.1 — §4.1c Part 2 Jazz Mode implemented: status updated from "design complete" to "implemented"; `analyzeHarmonicRhythmJazz()` / `analyzeScoreJazz()` / `scoreHasChordSymbols()` / `collectChordSymbolBoundaries()` documented; `HarmonicRegion` `fromChordSymbol` + `writtenRootPc` fields noted; FiloSax/FiloBass unblocked; previous: 3.0 — §4.1c Part 2 Jazz Mode design added (chord-symbol-driven boundaries, Harmony element traversal, quality mapping, integration point, open questions); corpus roadmap updated with deferred status for C.P.E. Bach/Handel/Bach Suites/Debussy/Liszt/Bartók; previous: 2.9 — §4.1c Regional Note Accumulation added: collectRegionTones() + detectHarmonicBoundariesJaccard() + useRegionalAccumulation preference documented; §4.2 KeyModeAnalyzer known limitation (dominant seventh / Mixolydian ambiguity) added from Grieg corpus modal diagnostic; previous: 2.8 — §4.1b Contextual Inversion Resolution added: ChordTemporalContext extended with previousBassPc/previousChordAge/nextRootPc/nextBassPc/bassIsStepwiseFromPrevious/bassIsStepwiseToNext; three new scoring parameters (stepwiseBassInversionBonus, stepwiseBassLookaheadBonus, sameRootInversionBonus) added to ChordAnalyzerPreferences; isDiatonicStep() helper added to bridge helpers header; §4.1b temporal context section updated; validation: 83.7% chord identity (up from 83.4%), 661 disagree (down from 673) in the now-retired onset-only/music21 Bach workflow; previous: 2.6 — §4.2 harmonic major modes deferred note added after KeySigMode enum; §15 compare_analyses.py description extended with chord identity agreement rate note; previous: 2.5 — §4.5 "Remaining Gap" subsection removed (bypass no longer exists); §5.2 rewritten to reflect actual piece-start shortcut instead of claimed full bypass; §11.3a status note added (basic zero-sum centering implemented as minimizeTuningDeviation; weighted variant still planned); §3.1 file tree updated with synthetic_tests.cpp; factory/direct-use guidance updated; preset system (ModePriorPreset, modePriorPresets(), applyModePriorPreset, currentModePriorPreset) documented under §4.6 mode detection weights; previous: 2.4 — §4.6 mode detection weights updated to 21 independent priors with 5 presets; §4.5 key decision logic updated; §4.3b bridge location corrected; §3.1 analysis/ subdirectory structure updated*
*Last updated: April 2026*
*Maintainer: Update this document whenever architectural decisions change*
