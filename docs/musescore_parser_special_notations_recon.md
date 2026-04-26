# MuseScore Parser Acceptance for Special-Notation Catalog Entries

Date: 2026-04-26  
Scope: read-only, no source edits.

---

## Verdict

All four catalog chord-symbol labels are **Recognized** by MuseScore's parser —
each has an explicit entry in `src/engraving/data/chords/chords.xml`. The labels are
NOT vocabulary mismatches in the parser sense. However, three of the four cannot be
**emitted** by `ChordSymbolFormatter::formatSymbol()`, because the formatter's
vocabulary is limited to standard quality + extension strings. The fourth (`Cm9b5`)
is emittable and represents an actionable analyzer gap.

| Measure | Catalog symbol | Analyzer symbol | Parser verdict | Formatter can emit? | Classification |
|---|---|---|---|---|---|
| m60 | `Cm9b5` | `Cm7b5` | Recognized (id=34) | **Yes** | Actionable RealDiff |
| m164 | `C7alt` | `C7b9b5` | Recognized (id=113) | No | Semantic mismatch |
| m285 | `CTristan` | `''` | Recognized (id=195) | No | Formatter-gap |
| m333 | `CPhryg` | `Cm11` | Recognized (id=222) | No | Formatter-gap |
| m340 | `Csus#4` ¹ | `Csus#4` | Recognized | Yes | Symbol matches; Roman mismatch only |

¹ m340's symbol is `Csus#4` per the catalog XML, NOT a special notation; the
analyzer correctly emits `Csus#4`. Only the Roman numeral mismatches (`I` vs
`Isus4`). m340 is out of scope for this recon's special-notation question.

**Recommended resolution: Option (A) + targeted Option (B)**  
Extend `classifyComparison` with a `FormatterGap` sub-category for `CTristan` and
`CPhryg` (formatter can't produce them; requires extending the formatter). Reclassify
`C7alt` as a catalog inaccuracy and update the catalog to `C7b9b5` under Option (B)
(the chords.xml `7alt` definition doesn't match the actual m164 pitches; the
analyzer's output is more accurate). Keep `Cm9b5` as actionable RealDiff. See Q5.

---

## Q1 — Catalog Expected Labels

From `src/composing/tests/chord_mismatch_report.txt`, the 5 RealDiff entries:

| Measure | Catalog xml symbol (verbatim) | Analyzer symbol | Catalog xml Roman | Analyzer Roman |
|---|---|---|---|---|
| m60 | `Cm9b5` | `Cm7b5` | `iø7` | `iø9` |
| m164 | `C7alt` | `C7b9b5` | `I7` | `I7b5b9` |
| m285 | `CTristan` | `` (empty) | `I` | `Isus4` |
| m333 | `CPhryg` | `Cm11` | `i7` | `i11b9` |
| m340 | `Csus#4` ¹ | `Csus#4` | `I` | `Isus4` |

¹ Verified from `chordanalyzer_catalog.musicxml` directly:
`<harmony analysisKind="suspended-fourth"><root><root-step>C</root-step></root><kind text="Csus#4">none</kind>`.
The mismatch report shows `[roman]` only, confirming the symbol matches.

Pitch sets:
- m60: pcs={0,3,6,10,2} — C Eb Gb Bb D (half-diminished + major 9th)
- m164: pcs={0,4,6,10,1} — C E F# Bb Db (dominant, b5, b9)
- m285: pcs={0,6,10,2} — C F# Bb D (Tristan chord)
- m333: pcs={0,1,3,5,7,10} — C Db Eb F G Bb (Phrygian minor-seventh + b9 + 4)
- m340: pcs={0,6,7} — C F# G (sus with tritone instead of perfect 4th)

---

## Q2 — STANDARD Parser Location and Behavior

**Entry point:** `Harmony::setHarmony(const String& s)` at
`src/engraving/dom/harmony.cpp:871`.

```
setHarmony(s)
  → parseHarmony(s)            harmony.cpp:473   pre-process parens; split on "|"
    → parseSingleHarmony(...)  harmony.cpp:518   per-chord parse
```

**Flow inside `parseSingleHarmony`** (`harmony.cpp:518`):

1. ROMAN branch (line 522): sets `rootTpc = TPC_INVALID`, returns immediately. All
   strings accepted as plain text. Not relevant here.
2. STANDARD branch:
   - `convertNote(s, ...)` at line 549: parse a note name at position 0 of the
     string. If this fails, `LOGD("failed")`, `info->setTextName(s)`, `return 0`
     (line 557-559). **This is a hard failure** — root TPC stays invalid.
   - If root succeeds: strips root from `s`, handles slash bass, then:
3. **Chord-list name lookup** (line 600): `info->descr(s, pc)` — walks
   `ChordList::*chordList()` comparing extension text to `cd.names`. Exact
   string match.
4. If name is found → `cd` non-null → sets `id`, `textName = cd.names.front()`.
   **RECOGNIZED**: rootTpc valid, id valid, pitch content from chord list definition.
5. If name is NOT found → `cd = null` → falls through to `setHarmony` (line 880):
   - If `getParsedChord()->parseable()` → `generateDescription()` creates a new
     entry on the fly. `parseable()` always returns `true` after `parse()` is called
     (`chordlist.cpp:598` sets `m_parseable = true` immediately, never sets it false
     within `parse()`). So this path is always taken.
   - The generated description uses whatever `ParsedChord` produced structurally.
   - rootTpc is still valid (root was parsed); chord struct defaults to major triad
     with unrecognized modifier text carried.

**"Successfully parsed":** In the strict sense, any chord with a recognizable root
(A–G, with optional accidentals) gets a valid `rootTpc` and therefore `isRealizable()
== true` (`harmony.cpp:268`). The chord-list lookup (step 3) is the additional check
for whether the chord has a **pre-defined structural meaning** in MuseScore's
vocabulary. Passing that check → Recognized. Failing it but having a valid root →
the chord renders but its pitch content is whatever `ParsedChord` inferred (which
may be wrong for unusual chord types).

**ChordList loaded from:** `chords.xml` when `style.value(Sid::chordsXmlFile) == true`
plus `chords_std.xml` for rendering (`chordlist.cpp`, code near "chords.xml" string).

---

## Q3 — Per-Entry Parseability

### m60 `Cm9b5`

`parseSingleHarmony("Cm9b5")`:
1. `convertNote`: root = C (idx=1), valid TPC.
2. Extension text: `"m9b5"`.
3. `ParsedChord::parse("m9b5")`: quality token `m` → `m_minor.contains("m")` = yes
   → quality = "minor". Extension digit `9` → minor-ninth. Modifier `b5` → flat-fifth
   alteration. Structurally coherent.
4. Name lookup `descr("m9b5", pc)`: finds `<name>m9b5</name>` at chord id=34
   in `chords.xml`:
   ```xml
   <chord id="34">
     <name>m9b5</name>
     <xml>minor-ninth</xml>
     <degree>altb5</degree>
     <voicing>C Eb Gb Bb D</voicing>
   </chord>
   ```
5. **RECOGNIZED.** Exact voicing C Eb Gb Bb D matches m60's pitch set.

### m164 `C7alt`

`parseSingleHarmony("C7alt")`:
1. Root = C, valid.
2. Extension text: `"7alt"`.
3. `ParsedChord::parse("7alt")`: no quality prefix (starts with digit) → quality
   defaults to dominant (extension = "7"). Modifier `alt`: `m_mod` =
   {sus, add, no, omit, ^, type} — does NOT contain "alt". "alt" is added to
   `m_modifierList` but produces no structural HDegree.
4. Name lookup `descr("7alt", pc)`: finds `<name>7alt</name>` at chord id=113:
   ```xml
   <chord id="113">
     <name>7alt</name>
     <xml>dominant</xml>
     <degree>alt#5</degree>
     <degree>add#9</degree>
     <degree>add#11</degree>
     <voicing>C E G# Bb D# F#</voicing>
   </chord>
   ```
5. **RECOGNIZED** — the name match succeeds.

**Semantic note:** The chords.xml `7alt` voicing is C E **G#** Bb **D# F#** (aug 5,
#9, #11). The actual m164 pitches are C E **F#** Bb **Db** (b5, b9). These are
structurally different alterations. The catalog uses `C7alt` as an informal genre
label ("altered dominant") rather than a precise structural match to chords.xml
entry 113.

### m285 `CTristan`

`parseSingleHarmony("CTristan")`:
1. Root = C, valid.
2. Extension text: `"Tristan"`.
3. `ParsedChord::parse("Tristan")`: quality loop reads `tok1L = "tristan"`. During
   the loop, `tok1L = "t"` satisfies `m_major.contains("t")` (line 544: `m_major <<
   ... << u"t" ...`), so `initial = "T"`. But the backtrack guard at line 627 fires:
   ```cpp
   static const std::array<String, 3> modifiersStartingWithQualityCharacters {
       u"tristan", u"omit", u"type"
   };
   if (!initial.empty() && initial != tok1
       && !muse::contains(modifiersStartingWithQualityCharacters, tok1L)) {
   ```
   `tok1L == "tristan"` is in the exclusion list → guard fires → no backtrack.
   `tok1L = "tristan"` matches none of the quality sets → falls to else → quality
   reset to empty, `i` reset to 0. In modifier loop: "Tristan" is not in `m_mod`
   → added as unrecognized modifier token. Quality defaults to major.
4. Name lookup `descr("Tristan", pc)`: finds `<name>Tristan</name>` at chord id=195:
   ```xml
   <chord id="195">
     <name>Tristan</name>
     <xml>Tristan</xml>
     <voicing>C F# A# D</voicing>
   </chord>
   ```
5. **RECOGNIZED.** Voicing C F# A# D exactly matches m285's pitches {60,66,70,74}.

**Caveat re Vincent's note:** Vincent verified "MuseScore cannot parse `C Tristan`"
(with a space). That is correct for the space-separated form: `parseSingleHarmony("C
Tristan")` → root=C, extension=`" Tristan"` (leading space). The name lookup
`descr(" Tristan", pc)` fails because `" Tristan" != "Tristan"` (exact match only,
`harmony.cpp:88-100`). For the catalog's `CTristan` (no space), the lookup succeeds.

### m333 `CPhryg`

`parseSingleHarmony("CPhryg")`:
1. Root = C, valid.
2. Extension text: `"Phryg"`.
3. `ParsedChord::parse("Phryg")`: `tok1L = "phryg"` — no prefix matches any quality
   set. Falls to else → quality reset, i reset to 0. "Phryg" not in `m_mod` → added
   as unrecognized modifier. Quality defaults to major.
4. Name lookup `descr("Phryg", pc)`: finds `<name>Phryg</name>` at chord id=222:
   ```xml
   <chord id="222">
     <name>Phryg</name>
     <xml>minor-seventh</xml>
     <degree>addb9</degree>
     <degree>add4</degree>
     <voicing>C Db Eb F G Bb</voicing>
   </chord>
   ```
5. **RECOGNIZED.** Voicing C Db Eb F G Bb exactly matches m333's pitches {0,1,3,5,7,10}.

### m340 `Csus#4` (symbol only; no charter for this recon)

Confirmed from catalog XML that the expected symbol is `Csus#4` (not a special
notation). `sus#4` is in `chords.xml`. The analyzer correctly emits `Csus#4`. The
only mismatch is the Roman numeral (`I` vs `Isus4`). Out of scope for this recon.

---

## Q4 — Implication Per Entry

### m60 `Cm9b5` → Actionable RealDiff

`Cm9b5` is fully recognized by the parser (id=34, precise voicing), and
`ChordSymbolFormatter::formatSymbol()` CAN produce this string: it emits the
quality prefix `m` + extension `9` + modifier `b5` for minor-ninth-flat-5 chords.
The gap is in the **analyzer's extension detection**: it finds the m7b5 structure
(root, minor third, flat fifth, minor seventh) but doesn't promote the extension to
m9b5 even when a major ninth (interval of 14 semitones = 2 semitones mod 12) is
present. Fix: detect the 9th for m7b5/half-diminished chords and set the
`hasNinth` extension flag.

### m164 `C7alt` → Semantic mismatch (catalog inaccuracy)

`7alt` is recognized by the parser (id=113), but the chords.xml definition for `7alt`
(voicing: C E G# Bb D# F# = dominant +aug5 +#9 +#11) does NOT match the actual m164
pitches (C E F# Bb Db = dominant +b5 +b9). The catalog is using `C7alt` as a
genre shorthand ("heavily altered dominant") rather than a structural description.

The analyzer's output `C7b9b5` is **more accurate** to the actual pitches. The
formatter cannot emit `C7alt` (the formatter generates specific alteration suffixes,
not the generic "alt" shorthand). Emitting `C7alt` would require:
1. Detecting whether the pitch set matches the chords.xml id=113 voicing exactly, or
2. Adding "alt" as a special-case formatter output for heavily-altered dominants.

Neither is warranted when the specific label `C7b9b5` is more accurate. This entry
belongs in a catalog-update bucket, not an analyzer-fix bucket.

### m285 `CTristan` → Formatter-gap

`CTristan` is recognized by the parser (id=195), and the chords.xml voicing exactly
matches the actual pitches. But `ChordSymbolFormatter::formatSymbol()` has no code
path that produces the string "Tristan" — the formatter derives its output from
`ChordAnalysisResult.identity.quality` and extension flags, none of which map to
"Tristan". To emit `CTristan`, both the **analyzer** (detect Tristan chord as a
named type) and the **formatter** (emit "Tristan" for that type) would need
extension. This is a deliberate scope boundary, not a classical analyzer bug.

### m333 `CPhryg` → Formatter-gap

Same structure as m285. `CPhryg` is recognized by the parser (id=222, exact voicing
match). The formatter cannot produce "Phryg" because `ChordQuality` has no Phrygian
enum value and there is no "Phryg" branch in `qualitySuffix()`. The analyzer
classifies the pitch set as minor-eleventh (`Cm11`) — correct in terms of interval
content but missing the modal identity. Emitting `CPhryg` requires extending the
analyzer's quality enum and the formatter's suffix map.

---

## Q5 — Resolution Recommendation

**Recommendation: Option (A) extend classification + targeted Option (B) for m164.**

### For m285 `CTristan` and m333 `CPhryg` — Option (A)

Add a `FormatterGap` category to `classifyComparison` (alongside `DirectMatch`,
`ConventionDiff`, `RealDiff`). Applied when:
- The catalog's expected label is in MuseScore's chord list (parser-recognized), AND
- `ChordSymbolFormatter::formatSymbol()` cannot produce that label from any
  `ChordAnalysisResult` the current analyzer generates.

`CTristan` and `CPhryg` are formatter-gaps: the chord types are named and voiceable
in MuseScore but are outside the formatter's emit vocabulary. They do not belong
in the `RealDiff` (actionable) bucket because fixing the analyzer wouldn't help
without also extending the formatter. They do not belong in `ConventionDiff` because
they're not a spelling/convention disagreement.

No catalog edits required. The `FormatterGap` count tracks the work surface for a
future "named chord types" feature.

### For m164 `C7alt` — Option (B-light)

Update the catalog's expected label from `C7alt` to `C7b9b5`. Rationale: the
chords.xml "7alt" entry (voicing C E G# Bb D# F#) is structurally a different
chord from what's at m164 (C E F# Bb Db). Using `7alt` as the expected label is
a catalog inaccuracy; the analyzer's output `C7b9b5` is the more precise
description of these specific pitches. After the catalog update, m164 would be
a `DirectMatch` or near-`ConventionDiff` (the Roman numeral `I7b5b9` vs `I7`
question is separate).

**Requires explicit approval** per the catalog-edit rule.

### For m60 `Cm9b5` — No change

Stays as Actionable `RealDiff`. The fix is straightforward extension detection in the
analyzer (detect the 9th for m7b5 chords). No category change needed.

### Trade-off summary

| Option | Catalog edits | Test signal clarity | Future scope |
|---|---|---|---|
| **(A) extend classifyComparison** | None for CTristan/CPhryg | Accurate: FormatterGap ≠ RealDiff | Named chord type feature tracked separately |
| **(B) update catalog** | 1 entry (C7alt → C7b9b5) needs approval | Removes one false RealDiff | Doesn't address CTristan/CPhryg |
| **(C) multi-acceptable** | Format change only | Highest precision | More catalog maintenance |

Recommended path closes m164 as a catalog fix, isolates the formatter-gap work for
m285/m333, and leaves m60 as a clean analyzer task.
