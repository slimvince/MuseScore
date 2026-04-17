# MuseScore Arranger — Request for Comments

> **Draft for Vincent's review.** Not posted. Read through and adjust any claims
> before submitting to the MuseScore developer forum.

---

## What this is

A new `composing` module integrated directly into MuseScore Studio's C++ core — not a
plugin. It provides harmonic analysis and arranging assistance for musically literate
users: composers, arrangers, students, and teachers working across the Western tonal
tradition.

The long-term intent is to contribute this to MuseScore Studio as a first-party feature.
This post is an early RFC to get architectural feedback and start the contribution
conversation before a PR is submitted.

---

## What it does

**Harmonic analysis from raw notes — never from existing chord symbols.**
The analyzer works entirely from note pitch, duration, beat position, and voice leading
context. It never reads existing chord symbols, Roman numerals, or Nashville numbers as
input. All inferences are note-driven.

**Annotation modes (Tools menu, works on any user selection):**
- Chord symbols — root, quality, extensions, inversions, slash chords
- Roman numerals — functional harmony including:
  - Cadence markers (PAC, IAC, HC, DC, PC)
  - Pivot chord labels (`vi → ii` format, U+2192)
  - Borrowed chord labels (♭VII, ♭III, ♭VI etc.)
  - Key/mode annotations
- Nashville numbers

**Chord staff ("Implode to chord track"):**
Populates a dedicated grand-staff part with a full harmonic reduction: chord symbols,
Roman numerals, cadence markers, pivot chord labels, key/mode annotations, borrowed
chord labels. Notes on the chord staff have `play = false` — display only, do not double
source staves in playback.

**Status bar integration:**
Chord, key/mode, and Roman numeral displayed on every note selection, using a bounded
adaptive local window that expands only until the displayed result stabilises.

**21-mode key/mode inference:**
Seven diatonic modes + seven melodic minor family + seven harmonic minor family.
Independent mode prior parameters with five named presets (Standard, Jazz, Baroque,
Modal, Contemporary). Adapts to repertoire style.

**Intonation:**
Per-note and region tuning via split-and-slur. Two modes: TonicAnchored (each chord
root placed at its scale-degree position above the mode tonic in just intonation) and
FreeDrift. Italian tuning anchor keywords (`altezza di riferimento`, `alt. rif.`).
Optional cent annotations in score.

**Note naming:**
Respects the score's chord symbol spelling preference (Format → Style → Chord Symbols),
including B/H naming for German and Nordic conventions, implemented by reading
`Sid::chordSymbolSpelling` from the score style.

**Preferences:**
Edit → Preferences → Composing.

---

## Architecture

### New module: `src/composing/`

Pure C++ analysis library — no dependencies on Qt, engraving, or other MuseScore
modules. Contains the chord analyzer, key/mode analyzer, harmonic rhythm detector, and
intonation system. Designed as a self-contained layer that can be tested independently.

```
src/composing/
├── analysis/
│   ├── chord/       RuleBasedChordAnalyzer, ChordSymbolFormatter, ChordAnalyzerPreferences
│   ├── key/         KeyModeAnalyzer, KeySigMode (21 modes), mode-prior presets
│   └── region/      HarmonicRegion, HarmonicRhythmBridge, Jaccard boundary detection
├── icomposinganalysisconfiguration.h   preference interface
├── composingconfiguration.{h,cpp}      concrete implementation
└── tests/           GTest suite (335 unit tests)
```

Public surface is narrow: `IChordAnalyzer`, `IKeyModeAnalyzer`, and
`IComposingAnalysisConfiguration`. Concrete implementations are behind factory functions.

### Bridge layer: `src/notation/internal/notationcomposingbridge*.cpp`

Three bridge files connect the `composing` module to the notation UI. They live in the
`mu::notation` namespace and are the only touch point between the composing module and
MuseScore's engraving model. The bridge uses MuseScore's existing `INotation`, `IScore`,
and `INotationInteraction` interfaces — no engraving model types leak into
`src/composing/`.

### One upstream change: `src/engraving/dom/chordlist.cpp`

A one-line fix for a double-sus render bug in `ParsedChord::parse()`. When
`kind="suspended-fourth"` and the text already contains the suffix `sus`, the existing
code (line 993) reassigns `tok1 = u"sus"` inside the re-attachment block, causing the
sus token to be appended a second time — producing `Csussus`, `Bbsussus` etc. The fix
removes this erroneous reassignment. This is the only modification to an existing
MuseScore source file. Details in `docs/chordlist_bug_report.md`.

### Licensing and CLA

All code is GPL v3, consistent with MuseScore Studio. The Contributor License Agreement
with MuseScore will be signed before any PR is submitted.

---

## Quality evidence

**DCML / When in Rome corpus validation (10 corpora, 16,765 regions):**

| Corpus | Agreement | Movements |
|--------|-----------|-----------|
| Dvořák | 79.2% root agreement | 12 |
| Chopin | 71.6% root agreement | 55 |
| Corelli | 70.3% root agreement | 149 |
| Beethoven string quartets | 64.9% root agreement | 70 |
| Mozart | 61.8% root agreement | 54 |
| Grieg | 60.7% root agreement | 66 |
| Schumann | 61.6% root agreement | 13 |
| Tchaikovsky | 61.0% root agreement | 12 |
| Bach English/French Suites | 52.4% root agreement | 89 |
| **Weighted average** | **64.6%** | — |

Bach chorales separately (ABC corpus): **75.2% chord-identity agreement** on aligned
regions across 352 chorales (7,748 aligned regions).

These figures reflect the sparse-voicing limitation common in Classical and Baroque
scores — many movements have incomplete harmonic voicings (arpeggiated textures, missing
bass notes) that reduce root detection accuracy.

**Complete-voicing jazz transcription (My Funny Valentine, Bill Evans):**
185-measure three-layer comparison against a human analyst's transcription symbols (Felix
B.) and a third-party chord symbol plugin: approximately **75–80% exact or near-exact
chord symbol agreement** with the human transcription. Extended runs of perfect
measure-by-measure agreement across m.82–102, m.151–185, and the Coda. Complex extended
chords correctly identified throughout, including: AbΔ7#11, G7(#9b13), EbMaj7add13/Ab,
GbMaj7b9b5, FmMaj7, CmMaj9, Eb7sus#5/B, G7sus#5#11, and many others. Bass solo
ostinato (F13/Eb, m.106–142): correctly held across 36 measures.

The difference between 64.6% and 75–80% reflects the sparse-voicing limitation: the
vertical analyzer performs substantially better when bass notes and complete chord
voicings are present in the score.

**Internal consistency:**
Batch analysis, chord staff population, status bar, and context menu paths all agree on
chord identity across benchmark scores.

---

## Current status

- **335/335** composing unit tests passing
- **45/49** notation integration tests passing (4 known deferred — Corelli late-beat
  sparse-texture cases that require pedal point detection, not yet implemented)
- 0 abstract chord identity mismatches against the 376-entry chord catalog
- Validated on Classical, Romantic, Baroque, and jazz repertoire

---

## Known limitations

**Sparse voicings:**
Root detection degrades when bass notes or chord tones are absent from the score —
common in solo melodic lines, arpeggiated accompaniment, and lead sheets without bass.
A synthetic bass-injection experiment raised Rampageswing jazz corpus agreement from
39.8% to 98.3%, confirming the analyzer is correct when given complete tonal material;
the limitation is the corpus, not the engine.

**Extension detection on sparse voicings:**
Ninth, eleventh, thirteenth detection requires the extension note to be present with
sufficient weight. Extension detection on sparse jazz piano voicings where Evans omits
chord tones is limited by available note material.

**Melody/harmony conflation:**
Melody notes in the same staff as chord voicings can affect chord root detection.
Melody identification is a planned future capability.

**Pedal point:**
Structural pedal points (sustained bass note while harmony changes above) are not yet
explicitly detected. This affects the 4 deferred notation tests.

**Post-tonal language:**
The current vertical tertian engine does not handle quartal, quintal, or polychordal
harmony.

**Campania font rendering:**
Certain diminished chord symbols on specific roots display with a spurious `s` prefix
in the Campania font (e.g. `Ddim7` renders as `Dsdim7`). The internal string is correct
— confirmed by the edit dialog. The same artifact affects third-party chord symbol
plugins. This is a MuseScore core font rendering issue, not a bug in the composing
module.

---

## What we are looking for

1. **Architecture review** — is the bridge-layer approach (notation bridge files owning
   all cross-module calls, composing module knowing nothing about engraving) the right
   pattern for a feature of this scope? Established precedents in the MuseScore codebase
   we should follow?

2. **Review of the `chordlist.cpp` fix** — the one-line double-sus duplication fix at
   line 993. Should this be submitted as a separate PR ahead of the main module? Is there
   a preferred approach for this kind of chord-kind parser correction?

3. **Contribution process** — expected PR scope for an initial submission, CLA process,
   coding standard requirements. Should the intonation subsystem be scoped out of the
   initial PR?

4. **Campania font** — is the `Dsdim`/`Fsdim` rendering artifact a known issue? Is there
   an existing fix or workaround in the font rendering pipeline?

5. **Interest from other developers** — particularly anyone working on chord symbol
   rendering, music theory pedagogy tools, or the arranging assistance direction.

For deeper reading: [ARCHITECTURE.md](../ARCHITECTURE.md) covers the full design, module
boundaries, algorithm details, corpus results, and planned extensions.

---

## Repository

[Link to be added by Vincent before posting]

---

*Draft prepared 2026-04-17. Vincent Wong.*
