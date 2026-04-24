# Symbol-Input Audit — Post Jazz-Path Retirement

## Context

Jazz path retired in commit `02e3733afb`. That commit deleted
`analyzeHarmonicRhythmJazz`, `scoreHasValidChordSymbols`, and
`collectChordSymbolBoundaries` from the production bridge
(`src/notation/internal/`), and removed the `forceClassicalPath`
parameter that guarded against order-of-annotation violations.

This audit confirms the scope of remaining chord-symbol reads across
the full codebase (production and tools) and classifies each by intent,
applying the user's operating principle:

> Symbols are instructions written by the user, not analysis results.
> Production paths must not read them as input to analysis. Tools may
> read them only as comparison/ground-truth labels — never as input that
> influences what the analyzer computes.

---

## Summary

| Category | Count | Concern |
|----------|-------|---------|
| A — Production input | **0** | None (retirement complete) |
| B — Tool comparison | **3 fields** | OK |
| C — Tool input | **2 uses** | User decision |
| D — Engraving / UI | **~60+ sites** | OK (expected) |
| E — Test fixtures | **4 files** | OK |

**Production retirement complete: YES.**  
No production path in `src/composing/` or `src/notation/internal/`
reads a `Harmony` element or tests for chord symbol presence to
influence analysis output.

**Tool-side input uses requiring user decision: 2**  
See §C below.

---

## §A — Production-input findings

None. All hits of `isHarmony()`, `toHarmony`, `->rootTpc`,
`->harmonyType`, `HarmonyType::STANDARD` in `src/composing/` and
`src/notation/internal/` are either:
- Writing annotations as analysis OUTPUT (e.g. `notationcomposingbridge.cpp:816-834`
  sets `h->setHarmonyType(HarmonyType::STANDARD)` on a newly created `Harmony`
  element after the analysis is complete — this is writing the result, not reading input).
- Removing pre-existing annotations as cleanup before a write pass
  (`notationimplodebridge.cpp:814` — iterates annotations to remove
  Harmony+StaffText before populating the chord staff; does not read content).

---

## §B — Tool-as-comparison findings

`tools/batch_analyze.cpp` stores three comparison-metadata fields in
`AnalyzedRegion` alongside note-based analysis results, and emits them
to JSON output:

| Field | Write site | Read/emit site | Purpose |
|-------|-----------|---------------|---------|
| `ar.fromChordSymbol = true` | line 1800, inside `analyzeScoreJazz` | line 2223 (JSON output) | Flags whether the region boundary came from a chord symbol |
| `ar.writtenRootPc = writtenRootPc` | line 1801, inside `analyzeScoreJazz` | line 2224 (JSON output) | Written root PC (0–11) from the chord symbol, for side-by-side comparison with `chord.rootPc` |
| `ar.writtenQuality = writtenQuality` | line 1802, inside `analyzeScoreJazz` | line 2225 (JSON output) | Written quality from `parsedChord->xmlKind()`, for side-by-side comparison |

These are stored alongside the note-based analyzer output, not fed back
into it. A downstream script reading the JSON can compare
`writtenRootPc` against `chord.rootPc` to measure agreement — this is
comparison, not input.

The `convertNotationRegion` helper at line 2002 also copies
`fromChordSymbol` and `writtenRootPc` from a `HarmonicRegion` struct
when converting notation-bridge output to `AnalyzedRegion`; in the
notation path those fields always carry their default values (false / -1)
because no production code sets them.

---

## §C — Tool-as-input findings

### C.1 — `analyzeScore` gateway gate + `analyzeScoreJazz` boundary detection

**File:** `tools/batch_analyze.cpp`  
**Sites:** lines 783–800 (`scoreHasValidChordSymbols`), 1680–1812
(`analyzeScoreJazz`), 1824–1826 (`analyzeScore` gate)

**What it does:**

`analyzeScore` (the top-level tool entry point) checks whether the
score contains any parseable STANDARD chord symbols
(`scoreHasValidChordSymbols`, a tool-local function at line 783).
When it does, analysis is routed to `analyzeScoreJazz` (line 1825)
instead of the Jaccard boundary-detection path.

Inside `analyzeScoreJazz`:
1. All STANDARD `Harmony` elements are collected in score order
   (lines 1703–1719).  Their ticks become region boundaries.
2. `collectRegionTones` is called on each symbol-defined span to
   accumulate sounding note evidence.
3. `analyzeChord()` is called on those notes.

The chord identity comes from the notes. But the **region boundaries**
come from the chord symbols. This means which notes accumulate into
which region is determined by symbol position, not by Jaccard distance
or onset detection. That is symbol-as-input to the boundary-detection
step of the analysis pipeline.

**Distinguishing from comparison:** comparison would be running
Jaccard-based analysis on the notes and then separately collecting
symbol positions to see how they agree. Here the symbols define the
analysis substrate.

**Options (do not choose for user):**

- **Retire.** Delete `analyzeScoreJazz` and the gateway gate.
  `analyzeScore` falls through to Jaccard always. Lead-sheet corpora
  produce near-zero aligned regions (already accepted as collateral in
  commit 02e3733afb). The per-symbol comparison metadata
  (`writtenRootPc`, `writtenQuality`) is lost; it can be reconstructed
  separately if needed.

- **Relocate.** Keep the boundary-extraction step as a separate
  pre-processing pass that writes a TSV of `(tick, rootPc, quality)`.
  `analyzeScoreJazz` is replaced by a second call to the Jaccard path
  restricted to those tick ranges — boundaries come from the notes
  within each symbol span, not from the symbols themselves. Identity
  is always note-based.

- **Accept.** This is a calibration tool, not the production bridge.
  The stated purpose is measuring how well note-based inference agrees
  with expert-written labels; using symbol boundaries as the unit of
  comparison is principled for that purpose. Accept with a comment
  clearly marking the function as tool-only and explaining the
  deliberate use of symbol boundaries.

---

### C.2 — `injectWrittenRootTone` (activated by `--inject-written-root`)

**File:** `tools/batch_analyze.cpp`  
**Sites:** lines 1653–1675 (function definition), 1760–1761 (call inside
`analyzeScoreJazz`)

**What it does:**

When the CLI flag `--inject-written-root` is passed (line 2560),
`injectWrittenRoot=true` is forwarded to `analyzeScoreJazz`.  Inside
that function, before each `analyzeChord()` call the written root PC is
materialized as a synthetic `ChordAnalysisTone`:

- All real tones have `isBass` cleared.
- A synthetic tone is inserted at `writtenRootPc` octave 3, with
  `weight=2.0` (double a normal note), `isBass=true`,
  `distinctMetricPositions=4`.

This synthetic tone enters `analyzeChord()` alongside the real sounding
notes. Because `isBass=true` at high weight, it directly biases the bass
root bonus, the structural penalty, and the inversion detection — all
of which influence which chord candidate wins.

**This is symbol-as-input to the analyzer in the strongest sense:**
the symbol root is injected into the tone evidence list.

**Options (do not choose for user):**

- **Retire.** Delete `injectWrittenRootTone` and the
  `--inject-written-root` CLI flag. The function exists to measure
  how much the analyzer improves when given the correct bass root as a
  hint; that experiment would be lost.

- **Accept (narrow).** Rename the flag to
  `--inject-symbol-root-for-calibration` and add a clear warning in the
  CLI help text that this mode is not representative of production
  analysis and must not be used to measure production accuracy. Keep
  the code but make the intent explicit in naming and documentation.

---

## §D — Engraving / UI findings

All expected. No analysis-influencing reads. Summary by subsystem:

| Subsystem | Representative files | Purpose |
|-----------|---------------------|---------|
| Engraving DOM | `harmony.cpp`, `score.cpp`, `segment.cpp`, `excerpt.cpp`, `fret.cpp`, `chordrest.cpp`, `box.cpp` | Clone, copy, layout, position Harmony elements; copy/paste; measure navigation |
| Rendering | `harmonylayout.cpp`, `systemlayout.cpp`, `horizontalspacing.cpp`, `measurelayout.cpp`, `boxlayout.cpp`, `tlayout.cpp`, `scorerenderer.cpp` | Layout and draw chord symbols and Roman numerals on the page |
| Editing | `edit.cpp`, `cmd.cpp`, `transpose.cpp`, `textedit.cpp` | Add/remove/transpose Harmony elements; realize chord harmony |
| Playback | `playbackmodel.cpp`, `compatmidirenderinternal.cpp` | Render chord symbols to MIDI or playback events |
| Import / Export | `exportmusicxml.cpp`, `importmusicxmlpass2.cpp`, `meiexporter.cpp`, `meiimporter.cpp`, `gpconverter.cpp`, `twrite.cpp`, `read206.cpp`, `tread.cpp` | Serialize/deserialize Harmony elements to/from MusicXML, MEI, GuitarPro |
| Inspector / UI | `generalsettingsmodel.cpp`, `textsettingsmodel.cpp`, `chordsymbolsettingsmodel.cpp`, `notationactioncontroller.cpp`, `notationinteraction.cpp`, `realizeharmonydialog.cpp`, `selectdialog.cpp`, `transposedialog.cpp` | UI controls for selecting, editing, and realizing chord symbols |
| Notation interaction | `notationinteraction.cpp` | Creating, editing, navigating Harmony elements via the notation UI |

---

## §E — Test fixtures

| File | Purpose | Verdict |
|------|---------|---------|
| `src/engraving/tests/chordsymbol_tests.cpp` | Tests Harmony DOM parsing, rootTpc round-trips | E — engraving unit tests |
| `src/engraving/tests/fretdiagram_tests.cpp` | Tests fret diagram + Harmony association | E — engraving unit tests |
| `src/notation/tests/notationimplode_tests.cpp` | Creates/reads STANDARD and ROMAN Harmony elements to verify annotation writer output; includes `WrittenChordSymbolsDoNotInfluenceAnalysis` which verifies symbol-independence | E — test fixtures, acceptable |
| `src/notation/tests/notationinteraction_harmony_pinning_tests.cpp` | Pins `addAnalyzedHarmonyToSelection` output (STANDARD, ROMAN, NASHVILLE types) | E — golden-file pin tests |

---

## §1 — jazzMode flag

### Write sites

| Site | Value set | Condition |
|------|-----------|-----------|
| `tools/batch_analyze.cpp:1742` | `ctx.jazzMode = true` | Always, at start of `analyzeScoreJazz()`, before iterating over chord-symbol regions |

### Read sites

**None.** `jazzMode` is declared on `ChordTemporalContext`
(`src/composing/analysis/chord/chordanalyzer.h:529`) but is never read
in `chordanalyzer.cpp` or any other scoring file. A search of
`src/composing/**/*.cpp` returns zero hits.

The 5 deleted `JazzMode_*` tests
(`chordanalyzer_tests.cpp:563–645`) verified that setting `jazzMode=true`
had no effect on scoring output (all checked `NEAR` equality between
jazz and non-jazz analysis). They passed because the flag is a no-op.

### Conclusion

`jazzMode` is currently a **dead flag** — set in one tool-only call site,
never read by any scoring logic. No production caller sets it. The flag
was carried over from a design sketch where Jazz mode might have
relaxed or changed scoring thresholds; that design was not implemented
before the bridge-side Jazz path was retired.

The field declaration comment in the header now accurately reflects its
status: "Used by tool paths (batch_analyze analyzeScoreJazz);
production analysis paths do not set this."

---

## §3 — fromChordSymbol / writtenRootPc fields

### Write sites

| Site | Value written | Location |
|------|--------------|---------|
| `tools/batch_analyze.cpp:1800` | `ar.fromChordSymbol = true` | Inside `analyzeScoreJazz` — tool only |
| `tools/batch_analyze.cpp:1801` | `ar.writtenRootPc = writtenRootPc` | Inside `analyzeScoreJazz` — tool only |
| `src/composing/analysis/region/harmonicrhythm.h:53,56` | Default `false` / `-1` | Struct field initializer — no production write |

**No production path in `src/composing/` or `src/notation/internal/`
sets either field to a non-default value.** Confirmed.

### Read sites

| Site | Purpose | Location |
|------|---------|---------|
| `tools/batch_analyze.cpp:2015–2016` | Copy fields from `HarmonicRegion` to `AnalyzedRegion` during notation-bridge conversion | Tool only |
| `tools/batch_analyze.cpp:2223–2224` | Emit to JSON output (comparison metadata fields) | Tool only |

All read sites are in `tools/`. The fields are read only for comparison
output, not to feed back into analysis.

---

## §4 — Dead-from-production branches

### jazzMode scoring branches

None exist. As documented in §1, `jazzMode` is never read in the scoring
implementation. There are no `if (ctx.jazzMode)` branches in the
analyzer — the flag is a no-op placeholder.

### Tool-only code paths in shared library

The following code in `tools/batch_analyze.cpp` exercises shared-library
functions (`collectRegionTones`, `analyzeChord`, `inferLocalKey`) via a
path that is not reachable from production:

- `analyzeScoreJazz` — uses chord-symbol ticks as region boundaries,
  then calls `analyzeChord` on accumulated notes.
- `injectWrittenRootTone` — modifies a `std::vector<ChordAnalysisTone>`
  before passing it to `analyzeChord`.

These paths call the same shared library code as production, but with
different region boundaries (symbol-driven instead of Jaccard) and
optionally with an injected tone. They are invisible to production
callers.

### Deleted Jazz tests

The following tests were deleted in commit `02e3733afb` and are no longer present:

- `Composing_ChordAnalyzerTests / JazzMode_KeepsBassRootBonus`
- `Composing_ChordAnalyzerTests / JazzMode_DoesNotChangeDominantGuideToneReading`
- `Composing_ChordAnalyzerTests / JazzMode_DoesNotBoostMinorSeventhReading`
- `Composing_ChordAnalyzerTests / JazzMode_DoesNotBoostDiminishedReading`
- `Composing_ChordAnalyzerTests / JazzMode_DoesNotPenalizeSuspendedFourthReadings`
- `Notation_ImplodeTests / JazzModeUsesChordSymbolPositionsAsBoundaries`
- `Notation_ImplodeTests / JazzModeChordIdentityComesFromNotesNotWrittenSymbol`
- `Notation_ImplodeTests / ScoreHasValidChordSymbolsIgnoresRomanHarmonyImports`
- `Notation_ImplodeTests / ScoreHasValidChordSymbolsDetectsStandardHarmonyAnnotations`

Retained (renamed): `Notation_ComposingBridgeTests /
WrittenChordSymbolsDoNotInfluenceAnalysis` (formerly
`AnnotationOrderDoesNotAffectRomanNumeralOutput`). This test verifies
that running the annotation engine twice — once with chord symbols
present, once without — produces identical Roman numeral output.

---

## Outstanding questions

**Q1: Accept or retire `analyzeScoreJazz` (C.1)?**

The function uses chord symbol positions as region boundaries, which
is symbol-as-input to boundary detection. The identity within each
region is still note-based (unless `--inject-written-root` is also
passed). The user must decide whether this is an acceptable tool design
for jazz-corpus calibration or whether even boundary detection must be
symbol-free.

**Q2: Accept or retire `--inject-written-root` (C.2)?**

This is the strongest form of symbol-as-input: the written root is
injected into the tone list with weight 2.0, directly biasing chord
identity. It exists as an experimental calibration mode ("what if the
analyzer knew the correct bass root?"). Whether this experiment is still
worth running under the new operating principle is a user decision.

**Q3: Should `jazzMode` be deleted from `ChordTemporalContext`?**

The flag is currently dead (never read). Its only remaining write site
is `analyzeScoreJazz` in tools. It could be removed from the shared
struct without functional impact. Retaining it costs nothing; deleting
it slightly simplifies the API surface. If C.1 is accepted, keeping the
flag (as documentation that the tool path is intentionally jazz-mode)
is harmless. If C.1 is retired, the flag's only write site disappears
and it becomes truly orphaned.
