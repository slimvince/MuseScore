# MuseScore Arranger — Submission Scope

> This document defines exactly what is and is not in the Phase 3 submission PR.
> Reviewed and approved: 2026-04-14.

---

## What is submitted (Phase 1 analysis engine)

### Analysis engine — `src/composing/`

| Path | Description |
|------|-------------|
| `src/composing/analysis/key/` | `KeyModeAnalyzer` — 21-mode key and mode inference (7 diatonic + 7 melodic minor family + 7 harmonic minor family) |
| `src/composing/analysis/chord/` | `RuleBasedChordAnalyzer` via `IChordAnalyzer` interface — tertian chord identification, quality, extensions (bitmask), inversions, diatonic degree, chromatic Roman numerals |
| `src/composing/analysis/region/` | `HarmonicRegion`, harmonic rhythm detection, Jaccard boundary detection |
| `src/composing/icomposinganalysisconfiguration.h` | Preference interface with 5 named mode-prior presets (Standard, Jazz, Modal, Baroque, Contemporary) |
| `src/composing/analysis/chord/chordsymbolformatter.*` | `ChordSymbolFormatter` — chord symbols, Roman numerals, Nashville numbers |

### Notation bridge

| Feature | Entry point |
|---------|-------------|
| Status bar display | Chord symbol, Roman numeral, Nashville number, key/mode on note selection |
| Context menu | Add chord symbol / Roman numeral / Nashville number at cursor |
| Selection-range annotation | Add chord symbols / Roman numerals / Nashville numbers to selection (Tools → Annotate selection) |

All three entry points use the same analysis path (`prepareUserFacingHarmonicRegions`). Results are consistent across all entry points for selections of 4+ measures.

### User preferences

- `IComposingAnalysisConfiguration` — analysis settings exposed through Edit → Preferences → Composing
- `IComposingChordStaffConfiguration` — chord staff output settings
- Mode-prior preset system: 5 named presets, one-click application in QML preferences page

### Tests

- All `composing_tests` (304 tests as of 2026-04-14)
- Notation bridge tests covering the above features (status bar, context menu, annotation)
- Notation tuning tests (13 tests)

---

## What is NOT submitted

| Item | Reason |
|------|--------|
| `tools/batch_analyze` | Internal development/validation tool only |
| Implode to chord track (Tools → Implode to chord track) | Structural score modification — separate contribution with additional review requirements |
| Tuning system (Tools → Tune selection, Tools → Tune as) | Separate contribution — score modification with different risk profile |
| Corpus validation scripts (`tools/run_*_validation.py`, `tools/compare_*.py`, DCML data) | Internal validation tooling only; not part of the MuseScore product |
| `tools/test_batch_analyze_regressions.py` | Internal regression harness for batch tool |
| `tools/music21_batch.py`, `tools/inject_m21_rn.py` | Internal corpus tooling |
| Jazz corpus data and Omnibook tooling | Internal validation reference |
| `ARCHITECTURE.md`, `STATUS.md` | Internal development documents |

---

## Known limitations (for reviewers)

Full list: `ARCHITECTURE.md §5.8` (updated 2026-04-13 with 10-score inspection findings).

Key limitations relevant to reviewers:

| Limitation | Scope |
|-----------|-------|
| Thin texture (CPE Bach keyboard, two-voice writing) | Insufficient pitch evidence for confident key inference; output suppressed at low confidence |
| Jazz without complete voicings | Corpus artifact — missing bass and piano voicings; not an engine failure. Confirmed by synthetic injection experiment (98% when bass injected) |
| Modulation tracking | Analyzer stays in home key; labels borrowed chords with chromatic scale degrees (♭VII, II in C major) rather than tonicization notation (V/IV). Design choice, not a bug |
| Over-segmentation on dense arpeggiated piano texture | Many small identical chord regions on arpeggio passages (e.g. Chopin BI16-1 opening) |
| ⁶₄ inversion rendering | Second-inversion Roman numerals may render as `‡`/`½` depending on MuseScore font; needs confirmation |

---

## Accuracy baseline

Corpus validation against DCML harmonic annotations (root pitch-class agreement):

| Corpus | Movements | Root agreement |
|--------|-----------|----------------|
| Dvořák Silhouettes | 12 | 79.2% |
| Chopin Mazurkas | 55 | 71.6% |
| Corelli Trio Sonatas | 149 | 70.3% |
| Beethoven String Quartets | 70 | 64.9% |
| Mozart Piano Sonatas | 54 | 61.8% |
| Schumann | 13 | 61.6% |
| Tchaikovsky | 12 | 61.0% |
| Grieg Lyric Pieces | 66 | 60.7% |
| Bach English/French Suites | 89 | 52.4% |
| C.P.E. Bach keyboard | 66 | 0% (thin texture — known limitation) |
| **Weighted total** | **586** | **64.6%** |

Bach chorales (When in Rome structural comparison): **75.2% chord-identity** on aligned regions (352 chorales, 5823/7748 aligned regions).

---

## Architecture summary

The analysis engine (`src/composing/`) has **no engraving dependency**. It is pure music theory. The bridge layer (`src/notation/internal/notation*bridge*.cpp`) connects the composing module to MuseScore's engraving model. All bridge functions are declared in notation-side headers and live in the `mu::notation` namespace.

All annotation display paths (status bar, context menu, selection-range write) use the same bounded adaptive inference helper. The window expands until the displayed harmonic result stabilizes, capped at 24 beats lookahead.
