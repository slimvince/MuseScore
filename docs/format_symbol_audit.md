# `formatSymbol()` Per-Quality Branch Audit

Date: 2026-04-26  
Scope: read-only, no source edits.  
Base commit: `e529b736a1`

---

## Verdict

**5 real bugs identified** (2 medium, 3 low severity).  
**~13 acceptable gaps** (structurally suppressed or detection-gated).  
**~6 uncertain cases** (uncommon combinations; flag for empirical follow-up).

The three previously-closed bugs were not the extent of this class.
The most actionable finding is **HalfDiminished + natural eleventh** (bug F1), confirmed
by the existing catalog dump at m296.  The second cluster (bugs F2/F3) affects the
`hasMaj7 && hasExtended` arm of the Minor branch, which silently drops 11th and 13th
for mMaj7 chords.

---

## Q1 — Per-quality branches

`qualitySuffix()` (line 152) is the inner function.  `ChordSymbolFormatter::formatSymbol()`
(line 2186) is the public API: it handles one structural special-case (Sus4+Maj7 requalified
to `Major+OmitsThird`, lines 2192–2205) then calls `qualitySuffix()` directly (line 2208).
The audit covers both, though the bulk of logic is in `qualitySuffix()`.

| Quality | Lines | What the branch produces |
|---|---|---|
| *(isSixNine early return)* | 160–167 | Returns `"69"` / `"m69"` / `"sus69"` / `"sus269"` before the switch; preempts all branches |
| **Major** | 173–224 | Comprehensive: hasMaj7/Min7 × hasThirteenth/Eleventh/Ninth branches; falls through to post-switch for hasThirteenthFlat, hasSharpFifth, hasFlatFifth |
| **Minor** | 226–253 | Handles mMaj7 (line 227), min7 (lines 229–242), bare (lines 244–252); post-switch handles hasThirteenthFlat |
| **Diminished** | 255–257 | `"dim7"` or `"dim"` only; all extensions suppressed |
| **HalfDiminished** | 259–267 | `"m9b5"` / `"m7b5b9"` / `"m7b5"` based on natural/flat ninth; post-switch handles hasThirteenthFlat |
| **Augmented** | 269–290 | hasMaj7 / hasMin7 × hasThirteenth/Ninth branches; post-switch excluded for hasThirteenthFlat |
| **Suspended2** | 292–299 | hasMin7 × hasThirteenth/Eleventh/Ninth; bare branch: hasEleventh → `"sus2(add4)"` |
| **Suspended4** | 301–339 | Most comprehensive suspended branch: hasMaj7, hasMin7 (full alteration set), bare (flat/sharp 9th, #11, natural 9th) |
| **Power** | 341–343 | `"5"` unconditionally |
| **default** | 345–347 | `""` (catch-all for any quality not listed above) |
| *(post-switch: hasThirteenthFlat)* | 354–358 | Appends `"b13"` / `"addb13"` for all qualities except Augmented |
| *(post-switch: hasSharpFifth)* | 363–366 | Appends `"#5"` for all qualities except Augmented (already structural) |
| *(post-switch: hasFlatFifth)* | 367–377 | Appends `"b5"` / `"5b"` for all qualities except Diminished and HalfDiminished |

---

## Q2 — Detection flags

`ExtensionFlags` struct (lines 795–812); `detectExtensions()` (lines 814–927).

| Flag | Struct field | Represents | Detection guard (qualities where flag is NEVER set) |
|---|---|---|---|
| `hasMin7` | `hasMinorSeventh` | Minor 7th (interval 10), not structural | HalfDiminished (line 833), when spelled A# (isSharp13Spelling) |
| `hasMaj7` | `hasMajorSeventh` | Major 7th (interval 11) | None |
| `hasDim7` | `hasDiminishedSeventh` | Diminished 7th (interval 9) | Non-Diminished (line 829) |
| `hasAdd6` | `hasAddedSixth` | Added 6th (interval 9), no 7th present | Diminished (line 846); practically never set when rawMin7/rawMaj7 present |
| `hasNinth` | `hasNinth` | Any ninth (derived: natural OR flat OR sharp) | — (derived from below) |
| `hasNinthNatural` | `hasNinthNatural` | Major/natural 9th (interval 2) | None |
| `hasNinthFlat` | `hasNinthFlat` | Flat 9th (interval 1) | None |
| `hasNinthSharp` | `hasNinthSharp` | Sharp 9th (interval 3) | Minor, Diminished, HalfDiminished (lines 857–859) |
| `hasEleventh` | `hasEleventh` | Natural/perfect 11th (interval 5) | None |
| `hasEleventhSharp` | `hasEleventhSharp` | Augmented 11th (interval 6, sharp spelling or natural 5th present) | HalfDiminished (line 902) |
| `hasThirteenth` | `hasThirteenth` | Natural 13th (interval 9), requires a seventh | — |
| `hasThirteenthFlat` | `hasThirteenthFlat` | Flat 13th (interval 8), requires fifth slot or Minor + flat-6 spelling | — |
| `hasThirteenthSharp` | `hasThirteenthSharp` | Sharp 13th / aug-6 (interval 10, sharp spelling) | Diminished (line 875) |
| `hasSharpFifth` | `hasSharpFifth` | Augmented 5th (interval 8), no fifth-slot filled | — |
| `hasFlatFifth` | `hasFlatFifth` | Flat 5th (interval 6), flat spelling and no natural 5th present | Diminished, HalfDiminished (lines 886–887) |
| `isSixNine` | `isSixNine` | 6/9 chord: added sixth + natural ninth, no 7th (line 924) | Derivation prevents this for qualities where hasAddedSixth = false |

---

## Q3 — Branch × flag consumption matrix

Legend:
- **✓** consumed — branch reads the flag and emits corresponding text
- **—** suppressed — flag never set for this quality (detection-gated) or structurally redundant; no action needed
- **↑** post-switch — not consumed in the per-quality branch but handled by the shared post-switch appends (lines 354–377)
- **✗** silently dropped — flag can be set for this quality, but the branch ignores it

Columns are the flags passed to `qualitySuffix()`.  Only flags that are not
universally detection-gated are shown; `hasDim7` (only Diminished), `hasNinthSharp`
(never Minor/Dim/HalfDim), `hasEleventhSharp` (never HalfDim), and `hasFlatFifth`
(never Dim/HalfDim) are omitted from rows where they are always `—`.

| Quality | Min7 | Maj7 | Add6 | Nth♮ | Nthb | Nth# | 11th | 11th# | 13th | 13thb | 13th# | #5 | b5 | isSixNine |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Major** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ↑ | ↑ | ✓ |
| **Minor** | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ↑ | ✗ | ↑ | ↑ | ✓ |
| **Diminished** | ✗ | ✗ | — | ✗ | ✗ | — | ✗ | ✗ | ✗ | ↑ | — | ↑ | — | — |
| **HalfDiminished** | — | ✗ | — | ✓ | ✓ | — | **✗** | — | ✗ | ↑ | ✗ | ↑ | — | — |
| **Augmented** | ✓ | ✓† | ✓? | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | — | ✗ | — | ↑ | ↑ |
| **Suspended2** | ✓ | ✗ | ✗ | ✓‡ | ✗ | ✗ | ✓ | ✗ | ✓ | ↑ | ✗ | ↑ | ↑ | ✓ |
| **Suspended4** | ✓ | ✓† | ✗ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| **Power** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | — |

**Notes:**
- `†` Augmented and Suspended4: the `hasMaj7 && hasNinth` arm (lines 273, 302) uses the
  composite `hasNinth` flag rather than `hasNinthNatural`.  This means a chord with only a flat
  or sharp ninth (no natural ninth) still takes the `"Maj9#5"` / `"Maj9sus"` arm instead of
  falling to the `hasMaj7` only arm where `hasNinthFlat`/`hasNinthSharp` would be appended.
  **This is bug F4 and F5.**
- `‡` Suspended2: interval 2 IS the suspension note, so `hasNinthNatural` is always true for
  Suspended2 by definition; the non-min7 arm correctly omits it from the label. ✓
- Suspended4 `hasEleventh (—)`: interval 5 IS the sus4 structural note; always true for
  Suspended4; deliberately suppressed. ✓
- Augmented `hasThirteenthFlat (—)`: `pc+8` = the structural #5 for Augmented; the
  post-switch correctly excludes Augmented (line 355).  And since `naturalFifthPresent = false`
  for Augmented, `hasThirteenthFlat` is practically never set for this quality anyway. ✓
- Augmented `hasAdd6 (✓?)`: `hasAddedSixth` requires `!rawMin7 && !rawMaj7`; for bare `C+add6`
  (no 7th), the branch falls to `else { suffix = "+"; }` and drops it.  Marked uncertain (see Q4).

---

## Q4 — Real-bug analysis

### F1 — `HalfDiminished + hasEleventh` (**Medium**)

**Code:** `qualitySuffix()` lines 259–267.  The branch checks only `hasNinthNatural`
and `hasNinthFlat`; `hasEleventh` (interval 5 = P4) is never read.

**Evidence:** Catalog dump at measure 296 (`DumpAllCandidatesForContextFile`):
`pcs={C,Eb,F#,Bb,D,F}`, `quality=HalfDiminished`, `sym=Cm9b5`.  F is present (natural
11th); the formatter correctly outputs "Cm9b5" for the ninth but silently drops the F.
The correct label is something like `"Cm11b5"` or `"Cm9b5add11"`.

**Why this combination occurs:** `Cm11b5` / `Cm9b5` voicings are standard in jazz and
neo-soul harmony.  The half-diminished chord with added 11th is particularly common as a
ii chord in minor keys (e.g., Bø11 in C minor).

**Severity:** Medium.  Catalog-confirmed; the chord appears in real scores.

---

### F2 — `Minor + hasMaj7 + hasThirteenth` (13th silently dropped) (**Medium**)

**Code:** `qualitySuffix()` line 227–228.

```cpp
if (hasMaj7 && hasExtended) {
    suffix = (hasNinth && hasNinthNatural) ? "mMaj9" : "mMaj7";
}
```

`hasExtended = hasThirteenth || hasEleventh || hasNinth` (line 169).  When `hasExtended`
is true because `hasThirteenth = true` (and no natural 9th is present), the branch fires
but emits only `"mMaj7"`.  The 13th is silently dropped.

**Example:** `{C, Eb, G, B, A}` — `CmMaj7add13` or `CmMaj13`.  `hasMaj7 = true`,
`hasThirteenth = true`, `hasNinth = false`.  `hasExtended = true` → branch fires →
suffix = `"mMaj7"`.

**Why this combination occurs:** mMaj7 chords with natural 13th appear in jazz and
neo-soul / R&B.  The Lydian minor scale (C D Eb F# G A B) naturally produces
all these extensions over CmMaj7.

**Severity:** Medium.  mMaj7 chord family is reasonably common.

---

### F3 — `Minor + hasMaj7 + hasEleventh` (11th silently dropped) (**Medium**)

**Code:** Same arm as F2, line 228.  When `hasExtended` is true because `hasEleventh = true`
(no natural 9th), suffix = `"mMaj7"`.

**Example:** `{C, Eb, G, B, F}` — `CmMaj7add11`.  `hasMaj7 = true`, `hasEleventh = true`,
`hasNinth = false`.  `hasExtended = true` → branch fires → suffix = `"mMaj7"`.

Also applies when both natural ninth AND eleventh are present: `{C, Eb, G, B, D, F}` →
`hasNinth = true`, `hasNinthNatural = true` → suffix = `"mMaj9"`.  The eleventh is still
dropped even when the ninth is handled.

**Why this combination occurs:** Same Lydian minor context as F2.  `CmMaj9add11` or
`CmMaj11` voicings appear in jazz composition.

**Severity:** Medium.  Same chord family as F2; the two bugs will typically co-occur.

---

### F4 — `Augmented + hasMaj7 + altered-only ninth` (wrong level) (**Low**)

**Code:** `qualitySuffix()` line 272–273.

```cpp
if (hasMaj7) {
    suffix = hasNinth ? "Maj9#5" : "Maj7#5";
}
```

`hasNinth = hasNinthNatural || hasNinthFlat || hasNinthSharp`.  If the chord has only a
flat or sharp ninth (no natural 9th), the branch still emits `"Maj9#5"` — wrong level —
instead of falling through to the `else { suffix = "7#5"; ... }` arm where altered ninths
are appended correctly.

**Note:** The `hasMin7` arm (lines 274–289) handles this correctly with
`else if (hasNinth && hasNinthNatural)` at line 279.  The `hasMaj7` arm lacks this
precision.

**Example:** `{C, E, Ab, B, Db}` — `CMaj7#5b9`.  `hasMaj7 = true`, `hasNinthFlat = true`,
`hasNinthNatural = false`.  `hasNinth = true` → suffix = `"Maj9#5"` (incorrect; should be
`"Maj7#5b9"`).

**Why this combination occurs:** Altered dominant-type chords with augmented 5th and flat 9th
appear in jazz.  CMaj7#5 itself is uncommon, but the combination exists.

**Severity:** Low.  CMaj7#5 is unusual; the altered-ninth variant is rare.

---

### F5 — `Suspended4 + hasMaj7 + altered-only ninth` (wrong level) (**Low**)

**Code:** `qualitySuffix()` line 302.

```cpp
if (hasMaj7 && hasNinth) {
    suffix = "Maj9sus";
}
```

Same precision defect as F4.  If `hasNinth` is true only from `hasNinthFlat` or
`hasNinthSharp` (no natural ninth), the branch emits `"Maj9sus"` instead of `"Maj7sus"` +
alteration suffix.

**Note:** The `hasMin7` arm within Suspended4 (lines 311–322) handles
`hasNinthFlat`/`hasNinthSharp` correctly.

**Example:** `{C, F, G, B, Db}` — `CMaj7susb9`.  `hasMaj7 = true`, `hasNinthFlat = true`,
`hasNinthNatural = false`.  `hasNinth = true` → suffix = `"Maj9sus"` (should be
`"Maj7susb9"`).

**Severity:** Low.  Maj7sus + altered 9th is unusual in standard harmony.

---

### Diminished + extensions (Acceptable)

The Diminished branch (lines 255–257) drops all flags except `hasDim7`.
`hasNinthNatural`, `hasNinthFlat`, `hasEleventh`, `hasThirteenth`, `hasEleventhSharp` can
all be set for Diminished quality.

This is classified **acceptable** rather than real-bug for three reasons:

1. `hasNinthSharp` is detection-gated for Diminished (line 858), so the most commonly
   expected #9 alteration is already suppressed.
2. `hasAddedSixth` is detection-gated for Diminished (line 846).
3. Diminished chords with added extensions are not in the catalog and are non-standard
   in notation practice.  The catalog test suite would expose any real need.

---

### HalfDiminished + hasThirteenth / hasMajorSeventh (Uncertain)

`hasThirteenth` can be set for HalfDiminished (rawMin7 = true → hasSeventh = true), but
the HalfDiminished branch (lines 259–267) does not consume it.  Similarly, `hasMajorSeventh`
has no HalfDiminished guard in detection but the branch ignores it.

These are classified **uncertain** because `Cm13b5` and `CmMaj7b5` are theoretically possible
but do not appear in the catalog and are uncommon in practice.  If empirically confirmed by
a real score, these would become real bugs.

---

### Suspended2 + hasMaj7 / altered 9th in min7 branch (Uncertain)

`hasMaj7` for Suspended2 quality (`CMaj7sus2`) and altered ninths in the `hasMin7`
arm of Suspended2 (`C7sus2b9`) are not consumed.  Classified **uncertain** — these
combinations are unusual and absent from the catalog.

---

## Q5 — Synthesis

| Category | Count |
|---|---|
| Total per-quality branches in `qualitySuffix()` (inc. post-switch) | 13 |
| Flags in `ExtensionFlags` struct | 16 |
| (branch, flag) pairs examined | 128 + shared post-switch |
| ✓ consumed (emits correct output) | majority |
| — suppressed / detection-gated | ~15 |
| **✗ silently dropped** | ~8 distinct (branch, flag) pairs |
| **Real bugs** | **5** (F1–F5) |
| Acceptable gaps | ~13 |
| Uncertain | ~6 |

### Real bugs by severity

| ID | Quality | Flag(s) dropped | Severity | Line |
|---|---|---|---|---|
| F1 | HalfDiminished | `hasEleventh` | **Medium** | 259–267 |
| F2 | Minor | `hasThirteenth` (with mMaj7) | **Medium** | 227–228 |
| F3 | Minor | `hasEleventh` (with mMaj7) | **Medium** | 227–228 |
| F4 | Augmented | `hasNinthFlat`/`hasNinthSharp` precision (hasMaj7 arm) | Low | 272–273 |
| F5 | Suspended4 | same precision issue (hasMaj7 arm) | Low | 302 |

### Pattern

All five bugs follow the same class as the three closed precedents:
a per-quality branch that was written for the simplest case of that quality and was not
updated when the detection layer started producing richer flag sets.

F1 (HalfDiminished) is the most actionable: catalog-confirmed at m296, and the fix is a
3-line extension of the `if (hasNinthNatural) ... else if (hasNinthFlat) ... else` pattern
already established by `e529b736a1`.

F2/F3 (Minor + mMaj7) are the second priority: the `hasMaj7 && hasExtended` arm at line
227 needs to be expanded to check `hasThirteenth` and `hasEleventh` explicitly before
collapsing to `"mMaj7"`.  Both will be fixed by the same branch expansion.

F4/F5 (Augmented + Suspended4, hasMaj7 arms) are low-priority: narrow chord types.
The fix in both cases is changing `hasNinth` to `hasNinthNatural` in the branch guard
(analogous to how the `hasMin7` arms in the same functions already use `hasNinthNatural`
at lines 279 and 311).

### Recommendation

Fix F1 first (catalog-confirmed, medium severity, small change).  Fix F2/F3 together in
one pass (same branch, similar expansion).  Fix F4/F5 together (same defect pattern in
two branches, two-word change each).  All fixes are isolated per-branch changes of
3–8 lines, with no architectural implications.
