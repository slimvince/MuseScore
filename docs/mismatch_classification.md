# Symbol/Roman Mismatch Classification

Date: 2026-04-25  
Source: `src/composing/tests/chord_mismatch_report.txt`  
(post-build run, fresh binary, 376/376 pass, abstract=0, symbol/roman=135)

---

## Summary

All 135 mismatches come from a single synthetic catalog score that exhaustively
enumerates chord-type combinations in C major. The overwhelming pattern (≥83% of
entries) is **extension/alteration stripping**: the catalog annotates a chord at its
base 7th-chord level (IM7, I7, I+7, Isus4, i7, …) while the pitches literally
contain additional extensions or alterations that the analyzer correctly names. A
secondary pattern (7%) is **alteration ordering in the symbol string**—both sides
agree on which alterations are present, they write them in different order. Three
entries show what appear to be **clear analyzer failures** (spurious #11 in
half-diminished inversion labels). Three more show what appear to be **catalog
issues**. The most immediately actionable improvement is standardizing alteration
ordering in the symbol formatter; the extension-stripping pattern requires a policy
decision on annotation depth.

---

## Source format

Each mismatch entry occupies two lines:

```
measure N [type]  [fields depending on type]
  key=Kmaj  pitches=[MIDI…]  pcs=[pitch-classes…]  tpcs=[tonal-pitch-classes…]
```

**type** is one of:
- `[roman]` — roman numeral mismatch only; symbol matched or was not present
- `[symbol+roman]` — both symbol and roman numeral mismatch

**Fields for `[roman]`:**
```
roman xml='CATALOG'  analyzer='ANALYZER'
```

**Fields for `[symbol+roman]`:**
```
xml='CAT_SYMBOL'  analyzer='ANAL_SYMBOL'  roman xml='CAT_ROMAN'  analyzer='ANAL_ROMAN'
```

**Pitch data:**
- `pitches`: MIDI note numbers (middle C = 60)
- `pcs`: pitch classes mod 12 (C=0, C#=1, … B=11)
- `tpcs`: tonal pitch classes (C=15, going up by fifths: G=16, D=17, A=18, …;
  going down by fifths: F=14, Bb=13, Eb=12, Ab=11, Db=10, Gb=9)

**Score context:** All 135 entries have `key=0maj` (C major). The measure numbers run
sequentially from m12 to m368 in a pattern that enumerates chord-type combinations
systematically. This is a synthetic/pedagogical catalog score, not a real piece of
music. There is no composer or style variation — the score is the test fixture.

---

## Classification axes

The data supports five axes; two others from the prompt brief are not well-supported.

**Axis 1 — Failure type:** The most productive axis. Nearly all mismatches fall into
one of: (a) extension stripping, (b) alteration stripping, (c) add-tone labeling,
(d) notation convention disagreement, (e) generic label, (f) spurious content in
analyzer.

**Axis 2 — Chord family:** Useful for grouping fix scope. Six families: Maj7 (IM7),
dom7 (I7), aug7 (I+7), sus4 (Isus4), min7 (i7), half-dim (iø7), and edge cases
(iM7, I+M7).

**Axes dropped:** Composer/style (only one synthetic score), position/beat (not in
report), key context (all C major). Voicing density and inversion are noted where
relevant but don't produce useful groupings at scale.

---

## Pattern summary

| Pattern | Count | % | First-pass impression |
|---|---:|---:|---|
| **A: Extension/alteration stripping** (roman) | **112** | **83%** | Mixed — annotation policy decision; analyzer may be more correct |
| — A1: Maj7 family (IM7, iM7, I+M7) | 13 | 10% | Catalog policy: annotate at 7th, ignore extensions |
| — A2: Dom7 family (I7) | 33 | 24% | Same policy; dom7 section is exhaustive |
| — A3: Aug7 family (I+7) | 17 | 13% | Same policy |
| — A4: Sus4 family (Isus4) | 45 | 33% | Same policy; largest single block |
| — A5: Min7 family (i7) | 5 | 4% | Same policy |
| — A6: Half-dim family (iø7) | 3 | 2% | Partially same; also overlaps B/D |
| **B: Alteration ordering in symbol string** | **9** | **7%** | Clear analyzer formatting issue — needs canonical order |
| **C: Add-tone vs bare triad** | **7** | **5%** | Ambiguous — policy call on when to name an added tone |
| **D: Generic/modal label in catalog** | **3** | **2%** | Mixed — "alt" and "Phryg" are standard labels; "Tristan" is unusual |
| **E: Spurious content in analyzer** | **3** | **2%** | Appears to be clear analyzer failure (spurious #11) |
| **F: Catalog issues** | **3** | **2%** | Appears to be catalog error or internal inconsistency |
| **G: Ambiguous / edge case** | **3** | **2%** | Genuinely ambiguous; both sides defensible |

*Note: 9 entries in Pattern B also have Pattern A in their roman field; counts above
treat B as primary for those 9. Total entries = 135.*

---

## Per-pattern detail

### Pattern A — Extension/alteration stripping (112 entries, 83%)

**Description.** The catalog annotates a chord using only its base chord type
(IM7, I7, I+7, Isus4, i7, iø7) regardless of how many extensions or alterations
are literally sounding. The analyzer names the full voicing. In every case the
analyzer's pitches support its output — the extensions/alterations are in `pitches`.

This is the dominant pattern. It appears to reflect a deliberate catalog annotation
policy: *label the structural chord function, not the full voicing*. The question
for the QA session is whether this policy is correct for this project's use case.

**Representative examples:**

| Meas | Catalog | Analyzer | Notes in pitches |
|---|---|---|---|
| m12 | IM7 | IM9 | {C E G B D} — D is 9th |
| m84 | I7 | I9 | {C E G Bb D} — D is 9th |
| m92 | I7 | I7b9 | {C E G Bb Db} — Db is b9 |
| m146 | I+7 | I+9 | {C E G# Bb D} — D is 9th |
| m167 | Isus4 | I11sus4 | {C F G Bb} — names existing 11th |
| m187 | Isus4 | I11b9sus4 | {C F G Bb Db} — Db is b9 |
| m36 | i7 | i9 | {C Eb G Bb D} — D is 9th |

**First-pass impression.** The catalog's simplification is internally consistent and
appears intentional — every sus4 is "Isus4", every dom7 is "I7" regardless of
extensions. The analyzer is arguably more accurate. This is an annotation policy
disagreement, not a crash or incorrect identification of root/quality. Whether to
align toward the catalog (fix the analyzer to strip extensions) or toward the
analyzer (update the catalog to include extensions) is the core decision for 83% of
the 135 mismatches. If the decision is "analyzer is right, update catalog", 112
entries are resolved in one catalog sweep with no code change.

**Subsystems pointed at if analyzer is correct:** Symbol and roman numeral
formatters are working. The catalog annotation tool/process is the fix target.

**Sub-family breakdown:**

#### A1 — Maj7 family (IM7, iM7, I+M7): 13 entries

| Meas | Catalog roman | Analyzer roman |
|---|---|---|
| m12 | IM7 | IM9 |
| m14 | IM7 | IM9#11 |
| m16 | IM7 | IM13#11 |
| m18 | IM7 | IM13 |
| m20 | IM7 | IM9 |
| m283 | IM7 | IM11 |
| m289 | IM7 | IM13 |
| m312 | IM7 | IM7#11 |
| m325 | IM7 | IM11 |
| m327 | IM7 | IM11 |
| m342 | IM7 | IM7b13 |
| m294 | iM7 | iM9 |
| m314 | I+M7 | I+M9 |

#### A2 — Dom7 family (I7): 33 entries

| Meas | Catalog roman | Analyzer roman | Tag |
|---|---|---|---|
| m74 | I7 | I13 | ext only |
| m76 | I7 | I7b13 | alt only |
| m78 | I7 | I7#11 | alt only |
| m80 | I7 | I13#11 | ext+alt |
| m82 | I7 | I7#11b13 | alt only |
| m84 | I7 | I9 | ext only |
| m86 | I7 | I9b13 | ext+alt |
| m88 | I7 | I9#11 | ext+alt |
| m90 | I7 | I9#11b13 | ext+alt |
| m92 | I7 | I7b9 | alt only |
| m94 | I7 | I13b9 | ext+alt |
| m96 | I7 | I7b9b13 | alt only |
| m98 | I7 | I7b9#11 | alt only |
| m100 | I7 | I13b9#11 | ext+alt; also Pattern B (symbol ordering) |
| m102 | I7 | I7b9#11b13 | alt only |
| m104 | I7 | I7#9 | alt only |
| m106 | I7 | I13#9 | ext+alt |
| m108 | I7 | I7#9b13 | alt only |
| m110 | I7 | I13#9#11 | ext+alt; also Pattern B |
| m112 | I7 | I7#9#11b13 | alt only |
| m114 | I7 | I7b5 | alt only |
| m116 | I7 | I13b5 | ext+alt |
| m119 | I7 | I13b5 | ext+alt |
| m121 | I7 | I9b5 | ext+alt |
| m123 | I7 | I9b5b13 | ext+alt; also Pattern B |
| m125 | I7 | I7b5b9 | alt only; also Pattern B |
| m127 | I7 | I13b5b9 | ext+alt; also Pattern B |
| m129 | I7 | I7b5b9b13 | alt only; also Pattern B |
| m131 | I7 | I7b5#9 | alt only; also Pattern B |
| m133 | I7 | I13b5#9 | ext+alt; also Pattern B |
| m135 | I7 | I7b5#9b13 | alt only; also Pattern B |
| m281 | I7 | I11 | ext only |
| m338 | I7 | I7b9#9 | alt only (both b9 and #9 present) |

Note on m164: classified under Pattern D (generic label), but roman part also has I7→I7b5b9.

#### A3 — Aug7 family (I+7): 17 entries

| Meas | Catalog roman | Analyzer roman |
|---|---|---|
| m67 | I+7 | I+9 | (also Pattern D symbol) |
| m69 | I+7 | I+13 | (also Pattern D symbol) |
| m139 | I+7 | I+13 | |
| m142 | I+7 | I+7#9 | |
| m144 | I+7 | I+13#11 | |
| m146 | I+7 | I+9 | |
| m148 | I+7 | I+9#11 | |
| m150 | I+7 | I+7b9 | |
| m152 | I+7 | I+13b9 | |
| m154 | I+7 | I+7b9#11 | |
| m156 | I+7 | I+13b9#11 | |
| m158 | I+7 | I+7#9 | |
| m160 | I+7 | I+13#9#11 | |
| m162 | I+7 | I+7#9#11 | |
| m165 | I+7 | I+7#9#11 | |
| m302 | I+7 | I+9 | |
| m309 | I+7 | I+13 | |

#### A4 — Sus4 family (Isus4): 45 entries

The catalog labels every sus4-type chord "Isus4" regardless of extensions. The
analyzer systematically names extensions as I11 or I13 plus any alterations. All
45 entries follow this one-dimensional pattern.

| Meas | Catalog | Analyzer |
|---|---|---|
| m167 | Isus4 | I11sus4 |
| m169 | Isus4 | I13sus4 |
| m171 | Isus4 | I11b13sus4 |
| m173 | Isus4 | I11#11sus4 |
| m175 | Isus4 | I13#11sus4 |
| m177 | Isus4 | I11#11b13sus4 |
| m179 | Isus4 | I11sus4 |
| m181 | Isus4 | I11b13sus4 |
| m183 | Isus4 | I11#11sus4 |
| m185 | Isus4 | I11#11b13sus4 |
| m187 | Isus4 | I11b9sus4 |
| m189 | Isus4 | I13b9sus4 |
| m191 | Isus4 | I11b9b13sus4 |
| m193 | Isus4 | I11b9#11sus4 |
| m195 | Isus4 | I13b9#11sus4 |
| m197 | Isus4 | I11b9#11b13sus4 |
| m199 | Isus4 | I11#9sus4 |
| m201 | Isus4 | I13#9sus4 |
| m203 | Isus4 | I11#9b13sus4 |
| m205 | Isus4 | I13#9#11sus4 |
| m207 | Isus4 | I11#9#11b13sus4 |
| m209 | Isus4 | I11b5sus4 |
| m211 | Isus4 | I13b5sus4 |
| m213 | Isus4 | I11b5b13sus4 |
| m215 | Isus4 | I11b5sus4 |
| m217 | Isus4 | I11b5b13sus4 |
| m219 | Isus4 | I11b5b9sus4 |
| m222 | Isus4 | I13b5sus4 |
| m224 | Isus4 | I11b5b9b13sus4 |
| m226 | Isus4 | I11b5#9sus4 |
| m228 | Isus4 | I13b5#9sus4 |
| m230 | Isus4 | I11b5#9b13sus4 |
| m232 | Isus4 | I11#5sus4 |
| m234 | Isus4 | I13#5sus4 |
| m237 | Isus4 | I11#5sus4 |
| m239 | Isus4 | I13#5#11sus4 |
| m241 | Isus4 | I11#5sus4 |
| m243 | Isus4 | I11#5#11sus4 |
| m245 | Isus4 | I11#5b9sus4 |
| m247 | Isus4 | I13#5b9sus4 |
| m250 | Isus4 | I11b5b9b13sus4 |
| m252 | Isus4 | I13#5b9#11sus4 |
| m254 | Isus4 | I11#5#9sus4 |
| m256 | Isus4 | I13#5#9#11sus4 |
| m259 | Isus4 | I11b5#9b13sus4 |

#### A5 — Min7 family (i7): 5 entries

| Meas | Catalog | Analyzer |
|---|---|---|
| m36 | i7 | i9 |
| m38 | i7 | i11 |
| m40 | i7 | i13 |
| m287 | i7 | i11 |
| m331 | i7 | i7b13 |

#### A6 — Half-dim family (iø7): 3 entries

| Meas | Catalog | Analyzer |
|---|---|---|
| m56 | iø7 | iø7#11 |
| m60 | iø7 | iø9#11 |
| m61 | iø7 | iø9#11 |

Note on m60: the catalog *symbol* says Cm9b5 (includes the 9th), but the catalog
*roman* says iø7 (omits the 9th). See also Pattern F.

---

### Pattern B — Alteration ordering in symbol string (9 entries, 7%)

**Description.** The catalog symbol and analyzer symbol agree on which alterations
are present but write them in different order. The roman numeral part of each entry
also has a Pattern A mismatch. These are pure formatting disagreements — the chord
content is the same.

The catalog convention appears to be: list alterations in diatonic interval order
(b5 before b9 before #9 before #11 before b13). The analyzer appears to use a
different order.

**Representative examples:**

| Meas | Catalog symbol | Analyzer symbol |
|---|---|---|
| m100 | C13b9#11 | C13#11b9 |
| m110 | C13#9#11 | C13#11#9 |
| m123 | C9b5b13 | C9b13b5 |
| m125 | C7b5b9 | C7b9b5 |

**First-pass impression: Clear analyzer formatting issue.** The alteration sequence
in the symbol string should follow a canonical order; the catalog appears to have
a consistent convention (lower interval number first). This is fixable in the symbol
formatter without any musical judgment calls.

**Full enumeration:**

| Meas | Catalog symbol | Analyzer symbol | Roman (catalog→analyzer) |
|---|---|---|---|
| m100 | C13b9#11 | C13#11b9 | I7→I13b9#11 |
| m110 | C13#9#11 | C13#11#9 | I7→I13#9#11 |
| m123 | C9b5b13 | C9b13b5 | I7→I9b5b13 |
| m125 | C7b5b9 | C7b9b5 | I7→I7b5b9 |
| m127 | C13b5b9 | C13b9b5 | I7→I13b5b9 |
| m129 | C7b5b9b13 | C7b9b13b5 | I7→I7b5b9b13 |
| m131 | C7b5#9 | C7#9b5 | I7→I7b5#9 |
| m133 | C13b5#9 | C13#9b5 | I7→I13b5#9 |
| m135 | C7b5#9b13 | C7#9b13b5 | I7→I7b5#9b13 |

Catalog pattern: `b5` comes first, then `b9`/`#9`, then `#11`, then `b13`.  
Analyzer pattern: appears to put `#11` before `b9`/`#9`, and `b5` after `b13`.

---

### Pattern C — Add-tone vs bare triad (7 entries, 5%)

**Description.** The catalog labels a chord with a bare triad symbol (I or i)
even when a non-chord tone (9th, 11th, #11th) is present in the pitches. The
analyzer names the extra pitch using "(addX)" notation. These are all triad-class
chords — no 7th present.

**Representative examples:**

| Meas | Catalog | Analyzer | Extra pitch |
|---|---|---|---|
| m26 | I | I(add9) | D above C triad |
| m261 | I | I(add11) | F above C triad |
| m291 | i | i(add9) | D above C minor triad |
| m319 | I | I(add9) | D above C triad |

**First-pass impression: Ambiguous.** Both choices are defensible.
- Catalog position: the structural harmony is I; the extra pitch is a passing/color
  tone not worth naming.
- Analyzer position: the pitch is explicitly sounding; naming it is accurate.
For pieces with genuine "add9" voicings this distinction matters. For catalog
annotation, it's a policy call.

**Full enumeration:**

| Meas | Catalog roman | Analyzer roman | Pitches (MIDI) |
|---|---|---|---|
| m26 | I | I(add9) | 60,62,64,67 |
| m261 | I | I(add11) | 60,64,65,67 |
| m273 | I | I(add#11) | 60,64,67,78,82 |
| m291 | i | i(add9) | 60,62,63,67 |
| m319 | I | I(add9) | 60,62,64,67 |
| m321 | I | I(add9) | 60,62,64,67 |
| m336 | i | i(add9) | 60,62,63,67 |

Note: m319 and m321 have identical pitches and identical mismatch — may be the
same voicing entered twice in the catalog.

---

### Pattern D — Generic/modal label in catalog (3 entries, 2%)

**Description.** The catalog symbol uses a label that describes modal character or
a named harmonic effect rather than a standard chord symbol. The analyzer attempts
to spell out the actual pitches.

| Meas | Catalog symbol | Analyzer symbol | Catalog roman | Analyzer roman | Pitches |
|---|---|---|---|---|---|
| m67 | C9+ | C9#5 | I+7 | I+9 | 60,64,68,70,74 |
| m69 | C13+ | C13#5 | I+7 | I+13 | 60,64,68,70,74,81 |
| m164 | C7alt | C7b9b5 | I7 | I7b5b9 | 60,64,66,70,73 |
| m285 | CTristan | *(empty)* | I | Isus4 | 60,66,70,74 |
| m333 | CPhryg | Cm7add11 | i7 | i11b9 | 60,61,63,65,67,70 |

*Note: m67/m69 use "+" suffix for augmented; m164/m285/m333 use named chord labels.*

**m67/m69 (C9+, C13+):** "+" means augmented fifth in older notation; "#5" is the
explicit spelling. Purely a notation convention choice. First-pass: **ambiguous**.

**m164 (C7alt):** "alt" is standard jazz notation for "7th chord with at least
one altered tension (b9, #9, #11, b13)." The analyzer resolves it to C7b9b5 —
which is one valid alt voicing. First-pass: **ambiguous** — the catalog is using
a valid shorthand; the analyzer's specific spelling may or may not match the
catalog's intent.

**m285 (CTristan):** Pitches {C, F#, Bb, D} — C dominant 7th with tritone
(F# = b5/#4) and major 9th. The analyzer returns an **empty symbol** and labels
the roman as Isus4, which does not match the pitches (there is no perfect 4th
here; Bb is the flat 7th). First-pass: **appears to be a clear analyzer failure**
for the symbol (empty output) and roman (Isus4 does not fit C F# Bb D). The catalog
label "CTristan" is unusual but the pitches support something like C7b5(add9) or
C9b5. This entry warrants close attention.

**m333 (CPhryg):** Pitches {C, Db, Eb, F, G, Bb} — Cm7 with natural 11 (F) and
Phrygian color (Db = b9). "CPhryg" is a modal label, not a standard chord symbol.
The analyzer produces Cm7add11 (symbol) and i11b9 (roman). First-pass: **ambiguous**
— the analyzer's spelling is arguably more useful for harmonic analysis; the catalog
label describes modal color but not function.

---

### Pattern E — Spurious content in analyzer output (3 entries, 2%)

**Description.** The analyzer includes "#11" in the roman numeral for
half-diminished chord inversions where the pitches do not contain a #11.

| Meas | Catalog roman | Analyzer roman | Pitches (MIDI) | Pitches (notes) |
|---|---|---|---|---|
| m364 | viiø65 | viiø7#1165 | 62,65,69,71 | D, F, A, B |
| m366 | viiø43 | viiø7#1143 | 65,69,71,74 | F, A, B, D |
| m368 | viiø42 | viiø7#1142 | 57,59,62,65 | A, B, D, F |

In C major, viiø7 = B–D–F–A (half-diminished seventh). All three entries contain
exactly that tetrachord, in various inversions (first, second, third). None of the
pitches contain a #11 (E# / F# above B). The tpcs confirm no sharps or flats.

The catalog's inversion labels (65, 43, 42) are standard figured-bass notation.
The analyzer's labels (7#1165, 7#1143, 7#1142) include the "#11" token which is
not supported by the pitches.

**First-pass impression: Clear analyzer failure.** The #11 is hallucinated. No
musical judgment call is needed — the pitches are unambiguous. This is a bug in
how the formatter constructs inversion labels for half-diminished chords. Three
entries are affected.

---

### Pattern F — Catalog issues (3 entries, 2%)

**Description.** Entries where the catalog itself appears to have an error or
internal inconsistency, independent of the analyzer.

#### F1 — Catalog symbol/roman internal inconsistency (2 entries)

**m60:** `xml='Cm9b5'  analyzer='Cm7b5'  roman xml='iø7'  analyzer='iø9#11'`  
Pitches: {C, Eb, Gb, Bb, D} = Cm9b5. The catalog *symbol* correctly includes the
9th (Cm9b5) but the catalog *roman* omits it (iø7 instead of iø9#11 or iø9). The
catalog is internally inconsistent. The analyzer symbol omits the 9th (Cm7b5)
while the analyzer roman includes it (iø9#11). First-pass: **catalog issue**.

**m329:** `xml='Cm7b9'  analyzer='Cm7'  roman xml='i7'  analyzer='i7b9'`  
Pitches: {C, Eb, G, Bb, Db} — Db is b9. Catalog symbol includes b9 (Cm7b9) but
catalog roman omits it (i7). Analyzer symbol omits b9 (Cm7) but analyzer roman
includes it (i7b9). Both catalog and analyzer are internally inconsistent in
opposite directions. First-pass: **catalog issue** (roman should be i7b9);
**also analyzer issue** (symbol formatter should output Cm7b9).

#### F2 — Catalog roman missing alteration that is in pitches (1 entry)

**m316:** `xml='CMaj7#9'  analyzer='CMaj7'  roman xml='IM7'  analyzer='IM7#9'`  
Pitches: {C, E, G, B, D#} = CMaj7#9. Catalog *symbol* correctly names the #9
(CMaj7#9). Catalog *roman* omits it (IM7 instead of IM7#9). Analyzer roman
correctly adds it (IM7#9) but analyzer *symbol* drops it (CMaj7).  
First-pass: **catalog roman issue** (should be IM7#9) and **analyzer symbol
issue** (should output CMaj7#9). The analyzer is split: correct in one formatter,
wrong in the other.

---

### Pattern G — Ambiguous / edge cases (3 entries, 2%)

These entries don't fit cleanly into any pattern. Both the catalog and analyzer
labels are questionable on the face of the pitches.

**m296:** `roman xml='Isus4'  analyzer='I11b5#9sus4'`  
Pitches: {C, Eb, Gb, Bb, D, F} pcs=[0,3,6,10,2,5]  
= C, Eb, Gb, Bb, D, F. This is Cm7b5 (half-diminished basis) plus D (9th) and F
(11th). The catalog labels it Isus4 — but the Eb and Gb are characteristic of a
half-dim chord, not a sus4. The "I" (major) quality also seems wrong for a chord
with Eb. First-pass: **looks like a catalog error**, but the analyzer's
I11b5#9sus4 is also hard to parse. This entry may be a mislabeled or
miscategorized catalog entry.

**m340:** `roman xml='I'  analyzer='Isus4'`  
Pitches: {C, F#, G} pcs=[0,6,7]  
= C, F#, G — a 3-note chord. F# is a tritone from C (b5 / #4), not a perfect
fourth (sus4). G is the 5th. The catalog calls this "I" (plain triad); the
analyzer calls it "Isus4". Neither label fits well — there is no E (major 3rd),
no Eb (minor 3rd), and no F (perfect 4th that would make it sus4). First-pass:
**genuinely ambiguous** — both labels are approximations.

**m164** is also listed here partially (see Pattern D): the "C7alt" vs "C7b9b5"
symbol disagreement involves a genuine ambiguity in what "alt" covers, and whether
the specific alteration set in the pitches matches the catalog's intent.

---

## Cross-axis observations

**The catalog is a synthetic enumeration, not real music.** All 135 entries are in
C major. The measure numbers reveal a systematic structure: the dom7 section (mm
74–135) exhaustively walks b9/b13, #9/b13, b5/b9, b5/#9 combinations; the aug7
section (mm 139–165) and sus4 section (mm 167–259) do the same for their base
types. This explains why the sus4 group alone accounts for 45 of 135 mismatches —
it is the largest enumeration block. A catalog annotation pass that updates all
extension/alteration labels would be a mechanical transformation on a known
combinatorial space.

**Alteration ordering is consistent within the catalog.** The 9 Pattern B entries
all show the same ordering rule: interval number ascending (b5 < b9 = #9 < #11 <
b13). The analyzer consistently violates this by placing #11 before b9/#9. This is
a single bug in the alteration-ordering logic.

**The half-dim inversion bug is isolated.** The spurious #11 only appears in the
three half-diminished inversion entries (mm 364–368). No other chord type shows
this behavior. The bug is likely in inversion-label construction for half-dim
chords specifically.

**m319 and m321 are identical.** Same pitches, same mismatch. This is either two
entries that test the same voicing in different metric positions (positions not
shown in the report) or a duplicate catalog entry.

**Pattern F entries cluster around "b9" and "9th" extensions.** Both internal
inconsistency entries (m60, m329) involve the 9th. The catalog may have a specific
rule about the 9th in these chord types that was applied inconsistently when the
catalog was built.

---

## Full enumeration (grouped by primary pattern)

### Pattern A: Extension/alteration stripping (roman)

*(See per-family tables in Pattern A detail above — all 112 entries listed there.)*

Summary of A-group measures:  
**A1 (Maj7 family, 13):** m12, m14, m16, m18, m20, m283, m289, m294, m312, m314, m325, m327, m342  
**A2 (Dom7 family, 33):** m74, m76, m78, m80, m82, m84, m86, m88, m90, m92, m94, m96, m98, m100, m102, m104, m106, m108, m110, m112, m114, m116, m119, m121, m123, m125, m127, m129, m131, m133, m135, m281, m338  
**A3 (Aug7 family, 17):** m67, m69, m139, m142, m144, m146, m148, m150, m152, m154, m156, m158, m160, m162, m165, m302, m309  
**A4 (Sus4 family, 45):** m167, m169, m171, m173, m175, m177, m179, m181, m183, m185, m187, m189, m191, m193, m195, m197, m199, m201, m203, m205, m207, m209, m211, m213, m215, m217, m219, m222, m224, m226, m228, m230, m232, m234, m237, m239, m241, m243, m245, m247, m250, m252, m254, m256, m259  
**A5 (Min7 family, 5):** m36, m38, m40, m287, m331  
**A6 (Half-dim family, 3):** m56, m60, m61  
**m329 roman (i7→i7b9, 1):** m329

### Pattern B: Alteration ordering in symbol

m100, m110, m123, m125, m127, m129, m131, m133, m135  
*(All 9 entries also have Pattern A in their roman field.)*

### Pattern C: Add-tone vs bare triad

m26, m261, m273, m291, m319, m321, m336

### Pattern D: Generic/modal label

m67 (C9+), m69 (C13+), m164 (C7alt), m285 (CTristan), m333 (CPhryg)

### Pattern E: Spurious #11 in analyzer

m364, m366, m368

### Pattern F: Catalog issues

m60 (symbol/roman inconsistency), m316 (roman missing #9), m329 (symbol/roman inconsistency)

### Pattern G: Ambiguous / edge case

m296 (Isus4 label for half-dim-like chord), m340 (I vs Isus4 for 3-note ambiguous chord)

---

## Suggested QA session flow

Ordered by: clarity of decision → ease of batch resolution.

**1. Pattern E: Spurious #11 in inversion (3 entries, ~5 min)**  
m364, m366, m368. These look like clear analyzer bugs — no judgment call expected.
Verdict these as "analyzer-fix" if Vincent confirms the pitches don't support #11.
This is the only block where code change is likely needed.

**2. Pattern B: Alteration ordering (9 entries, ~10 min)**  
Review the ordering convention question. If catalog order (ascending interval number)
is preferred, the fix is in the symbol formatter. No per-entry judgment needed — a
single ordering rule resolves all 9.

**3. Pattern A policy decision (112 entries, ~30 min — mostly batch)**  
The critical question is: does the catalog's "annotate at 7th-chord level" policy
match the project's goals? Three options:
- **a) Catalog is right:** fix analyzer to strip extensions → code change, 0
  catalog changes, 112 mismatches resolved
- **b) Analyzer is right:** update catalog to include extensions → catalog
  annotation sweep, no code change, 112 mismatches resolved  
- **c) Per-chord-type decision:** e.g., keep extensions for dom7 but strip for
  sus4 → mixed policy, partial resolution

Suggested sub-order within Pattern A:
- A5 (min7, 5 entries) — simplest case, no alterations
- A1 (Maj7, 13 entries) — straightforward; #11 and b13 on Maj7 are the edge cases
- A6 (half-dim, 3) — note m60 is also Pattern F
- A2 (dom7, 33) — walk the alteration combinations; b9/b13 group first, then #9, then b5
- A3 (aug7, 17) — same structure as dom7 but aug base
- A4 (sus4, 45) — largest block; likely batch once dom7 policy is decided

**4. Pattern C: Add-tone labeling (7 entries, ~10 min)**  
Six triad-level entries. Once Pattern A policy is settled, C is a parallel decision
for triads. m319/m321 can be decided together (identical).

**5. Pattern D: Generic labels (5 entries, ~15 min)**  
C9+/C13+ notation: pick a convention (2 entries, fast).  
C7alt, CPhryg: discuss annotation goals (2 entries, moderate).  
CTristan (m285): warrants close attention — analyzer failure + unusual catalog label.

**6. Pattern F: Catalog inconsistencies (3 entries, ~10 min)**  
m60, m329, m316. Each needs individual inspection of both symbol and roman fields.
These are the most likely catalog edits.

**7. Pattern G: Edge cases (2 entries, ~10 min)**  
m296 and m340. These are the hardest — no obviously right answer. May end as
"no-action" or "flag for future review."

**Total estimated session time: ~90 minutes** if the Pattern A policy is decided
early and cleanly batched.
