# Write API Probe — Source Investigation Findings

_Investigation date: 2026-05-16. Source tree: `C:\s\MS-core-api\` (ms-core-api branch).
Cross-reference: `api_survey.md` (read API), `api_write.md` (proposed write tools).
Methodology: read-only source inspection of `src/engraving/api/v1/` and action-controller
sources. Runtime probes deferred — flagged as ❓ in each section that needs them._

## Top-line summary

| # | Approach | Status |
| --- | --- | --- |
| 1 | Cursor-based note entry | ✅ works, with three gotchas |
| 2 | cmd() + selection for spanners/dynamics | ⚠️ works for slur/hairpin/ottava, **`add-dynamic` opens an interactive popup** |
| 3 | Direct construction for Dynamic | ⚠️ works via `cursor.add()`, NOT `segment.add()` (which does not exist in apiv1); `subtype` write path is wrong, use `set(Pid::DYNAMIC_TYPE, …)` |
| 4 | Direct construction for Harmony | ⚠️ works, but `harmonyName` is **read-only** in apiv1; write via `set(Pid::HARMONY_NAME, …)`; attach via `cursor.add()` |
| 5 | Direct construction for Lyrics | ⚠️ works, but `text` is **not exposed** in apiv1 (use `set(Pid::TEXT, …)`); `verse` not exposed either (use `set(Pid::VERSE, …)`); attach via `chord.add()` (preferred) or `cursor.add()` |
| 6 | `addText()` for rehearsal/tempo/staff/system | ❌ **does NOT take a position** — always inserts into the opening VBox at score start. Invalidates 4 proposed tools. Tempo BPM is cosmetic (no `followText`). |
| 7 | Volta construction | ❌ no apiv1-exposed `Score.add()` for spanners; `cursor.add()`'s default branch parents to a segment which is wrong for a spanner. No `cmd()` exists either. **Real gap.** |
| 8 | `cmd("section-break")` / `cmd("system-break")` | ✅ works with a range selection covering the target measure across all staves |

Items 6 and 7 require **changes to `api_write.md` tool signatures or implementation notes**, not just minor adjustments. Details below.

---

## 1. Cursor-based note entry

**Proposed:** `cursor.rewindToFraction(tick)` + `cursor.setDuration(z, n)` + `cursor.addNote(pitch)` for `add_note`; `cursor.addNote(pitch, true)` for `add_note_to_chord`; `cursor.addRest()` for `add_rest`.

### Findings

**Cursor reachability (v2 extension).** [cursor.h:166-205](C:\s\MS-core-api\src\engraving\api\v1\cursor.h#L166-L205), [score.cpp:50-53](C:\s\MS-core-api\src\engraving\api\v1\score.cpp#L50-L53). `Score::newCursor()` returns `new Cursor(score())` directly. No `MuseScore { }` plugin element required; `InputState` is owned by the cursor itself in `INPUT_STATE_INDEPENDENT` mode by default ([cursor.h:130-146](C:\s\MS-core-api\src\engraving\api\v1\cursor.h#L130-L146)). The "behaves differently in Extensions 2.0" note in `api_survey.md` is conservative — no version-branching exists in the cursor source. Confirmed callable as `api.engraving.curScore.newCursor()` from Surface A.

**`rewindToFraction(f)` — gotcha #1: parameter is `Fraction*`, NOT an int.** [cursor.h:205](C:\s\MS-core-api\src\engraving\api\v1\cursor.h#L205): `Q_INVOKABLE void rewindToFraction(apiv1::Fraction* f)`. From QML the caller must construct a Fraction via `api.engraving.fraction(z, n)` ([engravingapiv1.h:282-338](C:\s\MS-core-api\src\engraving\api\v1\engravingapiv1.h#L282)) — passing a bare integer or QVariant will fail type-check. There is also `rewindToTick(int)` which takes a raw tick integer; that is a simpler choice for the tool layer.

**Position semantics — gotcha #2: no auto-advance to first content.** `rewindToFraction` calls `tick2segment(fraction, /*first*/ true, m_filter)` and sets the segment directly. Unlike `rewindToTick()` it does **NOT** call `nextInTrack()` afterwards. If the segment at that tick has no element on the current track, subsequent `addNote()` calls will still create a note at that segment, but the caller should set `cursor.track = …` BEFORE the rewind to land on the right track from the start.

**`setDuration(z, n)`.** [cursor.h:221](C:\s\MS-core-api\src\engraving\api\v1\cursor.h#L221), [cursor.cpp:582-584](C:\s\MS-core-api\src\engraving\api\v1\cursor.cpp#L582-L584). `z` = numerator, `n` = denominator. If `n == 0` defaults to a quarter. Consulted by subsequent `addNote` / `addRest`; does NOT affect cursor advancement.

**`addNote(pitch, addToChord)`.** [cursor.h:213](C:\s\MS-core-api\src\engraving\api\v1\cursor.h#L213), [cursor.cpp:445-460](C:\s\MS-core-api\src\engraving\api\v1\cursor.cpp#L445-L460). Delegates to `Score::addPitch(NoteVal, addToChord, inputState)`. With `addToChord=false` this is MuseScore's normal note-entry behaviour: **overwrites** existing content at the cursor position with a chord of the configured duration. Does NOT shift subsequent notes. With `addToChord=true` appends a pitch to the existing chord at that segment, leaving its duration unchanged.

**`addRest()`.** [cursor.h:214](C:\s\MS-core-api\src\engraving\api\v1\cursor.h#L214), [cursor.cpp:470-480](C:\s\MS-core-api\src\engraving\api\v1\cursor.cpp#L470-L480). Calls `Score::enterRest(duration, inputState)`. Same overwrite semantics as `addNote`.

**Existing-content of different duration.** No special handling. `addPitch` and `enterRest` use the cursor's current `inputState().duration()` and let `Score::addPitch` perform standard note-entry overwrite — i.e., the new note adopts the configured duration and any segment changes propagate normally (could spill into the next beat or absorb a partial-beat rest). This matches the documented "standard note-entry behaviour — does not shift subsequent notes" claim in `api_write.md`.

**No auto-advance — gotcha #3.** Neither `addNote` nor `addRest` call `next()` afterwards. Successive entries against the same cursor without explicit `next()` will keep overwriting at the same segment. The tool layer must call `cursor.next()` between entries when emitting a sequence.

### Status: ✅ works as designed, with these implementation notes

**Revised implementation note for `add_note` / `add_note_to_chord` / `add_rest`:**
```js
var c = curScore.newCursor()
c.track = staffIndex * 4 + voiceIndex   // BEFORE rewind, not after
c.rewindToTick(tickInt)                  // simpler than rewindToFraction
c.setDuration(z, n)
c.addNote(pitch, /*addToChord=*/false)   // or addRest(), or addNote(p, true)
```

`rewindToFraction` works but requires `api.engraving.fraction(z, n)` to construct the argument. `rewindToTick(int)` is cleaner.

---

## 2. cmd() + selection pattern for spanners and dynamics

**Proposed:** `selection.selectRange(startTick, endTick, startStaff, endStaff)` then `cmd("add-slur")` / `cmd("add-hairpin")` / `cmd("add-hairpin-reverse")` / `cmd("add-8va")` / `cmd("add-8vb")` for `add_slur` / `add_hairpin` / `add_ottava`. Same wrapper for `add_dynamic`.

### Findings

**`Selection::selectRange()`.** [selection.h:93](C:\s\MS-core-api\src\engraving\api\v1\selection.h#L93), [selection.cpp:117-146](C:\s\MS-core-api\src\engraving\api\v1\selection.cpp#L117-L146). Signature: `Q_INVOKABLE bool selectRange(int startTick, int endTick, int startStaff, int endStaff)`. All parameters are `int`. Ticks are converted internally via `Fraction::fromTicks()`. **Inclusive/exclusive:** `startTick` and `startStaff` included; `endTick` and `endStaff` excluded. Staff indices are auto-clamped via `qBound`. Returns `false` if locked, `startStaff >= endStaff`, or no start segment exists. Notable internal branch at lines 139-142: when `hasActiveCommand()` is true it calls `setRangeTicks()` (preserves the requested tick boundaries even if segments don't yet exist at those ticks); when false, `setRange()` uses concrete segments. Since the tool layer always wraps in `startCmd`/`endCmd`, the `setRangeTicks` branch is the one used.

**Action handlers.** Registered in [src/notation/internal/notationactioncontroller.cpp:337-342](C:\s\MS-core-api\src\notation\internal\notationactioncontroller.cpp#L337-L342) (path differs from `api_survey.md` cite — `notationscene/internal/` is wrong, actual path is `notation/internal/`). Each handler reads the current selection and applies the spanner:

- `add-slur` → `Interaction::addSlurToSelection()` ([notationinteraction.cpp:5613-5621](C:\s\MS-core-api\src\notation\internal\notationinteraction.cpp#L5613-L5621))
- `add-hairpin` / `add-hairpin-reverse` → `Interaction::addHairpinsToSelection(HairpinType)` ([notationinteraction.cpp:5681-5696](C:\s\MS-core-api\src\notation\internal\notationinteraction.cpp#L5681-L5696))
- `add-8va` / `add-8vb` → `Interaction::addOttavaToSelection(OttavaType)` ([notationinteraction.cpp:5634-5643](C:\s\MS-core-api\src\notation\internal\notationinteraction.cpp#L5634-L5643))

All three wrap the work in their own `startEdit()` / `apply()` (which call `prepareChanges` / `commitChanges` internally).

**Selection state after the cmd().** Not preserved. The hairpin handler in particular reselects the newly-created hairpin segment (notationinteraction.cpp:5692-5693) so the user can grip-edit it. Slur and ottava handlers likewise leave the selection on the new spanner. The tool layer should NOT assume the original range survives — if it needs to keep that range, it must save and restore around the call.

**Nested startCmd/endCmd coalescing.** [score.cpp:591-619](C:\s\MS-core-api\src\engraving\api\v1\score.cpp#L591-L619). Outer `startCmd()` calls `undoStack()->prepareChanges(name)` AND `undoStack()->lock()`. The lock prevents nested `commitChanges()` calls (from the action handlers' own `apply()`) from each pushing their own undo entry. Everything between outer `startCmd` and `endCmd` coalesces into a single user-visible undo step. **Confirmed:** the proposed wrapper pattern in `api_write.md` works correctly.

**`add-dynamic` is interactive — this is the breaking caveat.** Handler is `toggleDynamicPopup()` ([notationinteraction.cpp:5999+](C:\s\MS-core-api\src\notation\internal\notationinteraction.cpp#L5999)). It opens a popup UI for the user to choose a dynamic; it does NOT silently apply a default dynamic to the selection. **This makes `cmd("add-dynamic")` unusable in a non-interactive tool.** Falls back to direct element construction (see §3).

### Status

- `add_slur`, `add_hairpin`, `add_ottava`: ✅ works, selection is not restored
- `add_dynamic` via cmd: ❌ interactive popup — use direct construction instead

**Revised implementation note for `add_slur` / `add_hairpin` / `add_ottava`:**
```js
curScore.startCmd("add slur")
curScore.selection.selectRange(startTick, endTick, staffIdx, staffIdx + 1)
api.engraving.cmd("add-slur")
curScore.endCmd()
// Caller must not assume original selection survives.
```

---

## 3. Direct element construction for Dynamic

**Proposed:** `newElement(Element.DYNAMIC)` + set `subtype` + `segment.add()`.

### Findings

**Element type valid.** [qmlpluginapi.cpp:357-373](C:\s\MS-core-api\src\engraving\api\v1\qmlpluginapi.cpp#L357-L373): `newElement(Element.DYNAMIC)` calls `Factory::createItem(ElementType::DYNAMIC, score->dummy())` and wraps with `Ownership::PLUGIN`. Returns an `EngravingItem` wrapper (no dedicated `Dynamic` wrapper class exists in apiv1).

**Setting the dynamic level — `subtype` is the wrong path.** The engraving `Dynamic` class has `DynamicType` enum (`PP`, `P`, `MP`, `MF`, `F`, `FF`, `FFF`, …, `SFZ`, `RFZ`) at `src/engraving/types/types.h`. The Pid mapping is `Pid::DYNAMIC_TYPE`. Use `d.set(Pid.DYNAMIC_TYPE, intValue)` via the inherited `ScoreElement::set(Pid, QVariant)` ([scoreelement.h:107](C:\s\MS-core-api\src\engraving\api\v1\scoreelement.h#L107)). The proposed `d.subtype = …` won't work — `subtype` is not a writable Q_PROPERTY on `EngravingItem`.

**`segment.add()` does NOT exist in apiv1 — invalidates the proposed insertion path.** [elements.h:1829-1895](C:\s\MS-core-api\src\engraving\api\v1\elements.h#L1829-L1895): `Segment` wrapper exposes only `elementAt(track)` as Q_INVOKABLE. There is no `add()` method.

**Correct insertion path: `cursor.add(dynamic)`.** [cursor.cpp:271-432](C:\s\MS-core-api\src\engraving\api\v1\cursor.cpp#L271-L432). `Cursor::add()` has explicit cases for KEYSIG, TIMESIG, LAYOUT_BREAK, NOTE, ARPEGGIO, LYRICS, etc. DYNAMIC falls into the `default` branch at line 428-430: parent is set to the current segment (line 291), track is set (line 290), and `m_score->undoAddElement(s)` is called. For a Dynamic this correctly registers it as a segment annotation — visible afterwards via `segment.annotations`.

### Status: ⚠️ works with caveats

**Revised implementation note for `add_dynamic`:**
```js
curScore.startCmd("add dynamic")
var c = curScore.newCursor()
c.track = staffIdx * 4
c.rewindToTick(tickInt)
var d = api.engraving.newElement(api.engraving.Element.DYNAMIC)
d.set(api.engraving.Pid.DYNAMIC_TYPE, dynamicTypeEnumInt)  // e.g. MF
c.add(d)
curScore.endCmd()
```

**Open questions needing runtime probe (❓):**
- Confirm the `Pid` enum is exposed under `api.engraving.Pid.*` from the v2 extension scope (it should be — it's part of the engraving QML enum surface — but cross-check at runtime).
- Confirm `DynamicType` integer values are reachable (the api may need a lookup table `{ "mf": 5, "f": 6, ... }`).
- Confirm the resulting Dynamic actually renders and plays back (default Cursor::add path was not designed with Dynamic in mind, so the visual result needs a quick eyeball check).

---

## 4. Direct element construction for Harmony (chord symbols)

**Proposed:** `newElement(Element.HARMONY)` + set `harmonyName` + `segment.add()`.

### Findings

**Element type valid** — `Element.HARMONY` is accepted by `newElement()`.

**`harmonyName` is READ-ONLY in apiv1 — invalidates the proposed write.** [elements.h:2683-2705](C:\s\MS-core-api\src\engraving\api\v1\elements.h#L2683-L2705):
```cpp
Q_PROPERTY(QString plainText READ plainText)
Q_PROPERTY(QString displayText READ displayText)
Q_PROPERTY(QString harmonyName READ harmonyName)   // no WRITE
```

Three exposed properties, all read-only. There is no `WRITE setHarmonyName` declared. The underlying engraving `Harmony::setHarmony(String)` exists but is not bridged. Workaround is the Pid system: `h.set(Pid.HARMONY_NAME, "Cmaj7")`. ❓ The exact Pid name (`HARMONY_NAME` vs `TEXT`) needs runtime confirmation — `Harmony` inherits from `TextBase`, so `Pid::TEXT` might also write through. Suggest probing both.

**Insertion via `cursor.add(h)`** — same fall-through path as Dynamic: HARMONY hits the `default` branch in `Cursor::add`, parent is set to current segment, `undoAddElement` is called. Harmony becomes a segment annotation. ❓ Runtime probe to confirm the harmonyName text is actually parsed/displayed correctly after this path (the engraving Harmony has internal parsing state that is usually triggered through `setHarmony()`; setting a Pid bypasses that).

**Attach must be to a `ChordRest` segment** for the harmony to render with the chord track. [api_survey.md line 361] confirms harmony is an annotation on `segment.annotations`. The tool needs to ensure the cursor is positioned at a ChordRest-type segment, not a clef/keysig/timesig segment.

### Status: ⚠️ works with caveats (Pid write path), needs runtime confirmation

**Revised implementation note for `add_harmony`:**
```js
curScore.startCmd("add harmony")
var c = curScore.newCursor()
c.track = staffIdx * 4
c.rewindToTick(tickInt)        // must land on a ChordRest segment
var h = api.engraving.newElement(api.engraving.Element.HARMONY)
h.set(api.engraving.Pid.HARMONY_NAME, "Cmaj7")
c.add(h)
curScore.endCmd()
```

**`api_write.md` signature change:** The tool description says the implementation is `newElement(Element.HARMONY) + set harmonyName + segment.add()`. Update to: `newElement(Element.HARMONY) + set(Pid.HARMONY_NAME, text) + cursor.add()`.

---

## 5. Direct element construction for Lyrics

**Proposed:** `newElement(Element.LYRICS)` + set `text` / `syllabic` / `verse` + `chord.add()`.

### Findings

**Element type valid.** `Element.LYRICS` is accepted. [factory.cpp:226]: factory creates `new Lyrics(parent->isChordRest() ? toChordRest(parent) : dummy->chord())` — so the parent is normalised to a ChordRest at construction time, even if the wrapper is created via the dummy.

**apiv1 Lyrics surface — minimal.** [elements.h:2643+]:
- `Q_PROPERTY(QString plainText READ plainText)` — **read-only**
- `Q_PROPERTY(bool isMelisma READ isMelisma)` — read-only
- `API_PROPERTY_T(syllabic, ...)` — writable via property assignment ✓
- `API_PROPERTY(lyricTicks, LYRIC_TICKS)` — writable ✓
- **`text` is NOT exposed** — the proposed `ly.text = "syllable"` will not compile in strict QML or will silently no-op.
- **`verse` is NOT exposed** — confirmed in `api_survey.md` open question D.

**Write paths via Pid system** ([scoreelement.h:107](C:\s\MS-core-api\src\engraving\api\v1\scoreelement.h#L107)):
- text: `ly.set(api.engraving.Pid.TEXT, "syllable")` — Lyrics inherits from TextBase
- verse: `ly.set(api.engraving.Pid.VERSE, 0)` — verse index is 0-based internally

**Attach via `chord.add(ly)` — works.** [elements.cpp:344-379](C:\s\MS-core-api\src\engraving\api\v1\elements.cpp#L344-L379): `Chord::add()` enforces `Ownership::PLUGIN`, then calls `Chord::addInternal()` which sets `s->setParent(chord)` and calls `undoAddElement(s)`. Lyrics will be reparented to the chord; the underlying engraving `Lyrics::chordRest()` accessor returns its ChordRest parent. ✓

**Alternative: `cursor.add(ly)`** — [cursor.cpp:352-359](C:\s\MS-core-api\src\engraving\api\v1\cursor.cpp#L352-L359). LYRICS has an explicit case: parents to `currentElement()` (a ChordRest at the cursor's segment+track) and calls `undoAddElement`. Both paths converge to the same DOM state.

**`syllabic` enum.** Writable via direct property: `ly.syllabic = LyricsSyllabic.BEGIN | END | MIDDLE | SINGLE`. ❓ Confirm the enum surface — `LyricsSyllabic` may be reachable as `api.engraving.Lyrics.BEGIN` or similar; needs runtime check.

### Status: ⚠️ works with caveats

**Revised implementation note for `add_lyric`:**
```js
curScore.startCmd("add lyric")
var c = curScore.newCursor()
c.track = staffIdx * 4 + voiceIdx
c.rewindToTick(tickInt)
var chord = c.element  // must be a Chord
var ly = api.engraving.newElement(api.engraving.Element.LYRICS)
ly.set(api.engraving.Pid.TEXT, "syl")
ly.set(api.engraving.Pid.VERSE, verseIdx - 1)  // tool exposes 1-based, internal is 0-based
ly.syllabic = syllabicEnumInt
chord.add(ly)
curScore.endCmd()
```

**`api_write.md` signature change:** Implementation says "set text/syllabic/verse + chord.add()". Verse is exposed in the tool signature as `verse: int` (1-based), but the internal write is via `Pid.VERSE` with 0-based offset — note the subtraction. Text write is via `Pid.TEXT`, not direct property.

---

## 6. `addText()` for various text types — REQUIRES API REDESIGN

**Proposed:** `curScore.addText("REHEARSAL_MARK", text)`, `addText("TEMPO", text)`, `addText("STAFF", text)`, `addText("SYSTEM", text)` for `add_rehearsal_mark`, `add_tempo_mark`, `add_staff_text`, `add_system_text` — all four tools land here.

### Findings

**Type strings accepted.** [score.cpp:55-81](C:\s\MS-core-api\src\engraving\api\v1\score.cpp#L55-L81). `Score::addText(type, txt)` maps the `type` string through `QMetaEnum::fromType<enums::TextStyleType>()` and `keyToValue()`. Valid type strings are the names from the `TextStyleType` enum at [src/engraving/types/types.h:826-905](C:\s\MS-core-api\src\engraving\types\types.h#L826-L905):
- `"REHEARSAL_MARK"` ✓
- `"TEMPO"` ✓
- `"STAFF"` ✓
- `"SYSTEM"` ✓
- and many more (`TITLE`, `SUBTITLE`, `COMPOSER`, `LYRICIST`, `DYNAMICS`, `EXPRESSION`, `METRONOME`, `HARMONY_A`, `HARMONY_B`, `LYRICS_ODD`, `LYRICS_EVEN`, …)

All UPPERCASE with underscores, matching C++ enum names exactly. Unknown strings fall through to a legacy XML-tag parser with a deprecation warning.

**THE PROBLEM: `addText` ignores position entirely. It always inserts into the score's opening VBox.** [score.cpp:71-80](C:\s\MS-core-api\src\engraving\api\v1\score.cpp#L71-L80):

```cpp
mu::engraving::MeasureBase* mb = score()->first();
if (!mb || !mb->isVBox()) {
    score()->insertBox(ElementType::VBOX, mb);
    mb = score()->first();
}

mu::engraving::Text* text = mu::engraving::Factory::createText(mb, tid);
text->setParent(mb);
text->setXmlText(txt);
score()->undoAddElement(text);
```

There is no selection lookup, no cursor consultation, no measure parameter, no segment lookup. The text is **always** parented to the first VBox at the start of the score (one is created if none exists). The TextStyleType only determines the formatting style of the text element; it does NOT route the text to a different parent.

This means `addText("REHEARSAL_MARK", "A")` produces a piece of body text labelled "A" inside the title VBox at the top of the score — not a real RehearsalMark element at the start of a measure. `addText("TEMPO", "Allegro")` produces a piece of header text labelled "Allegro" in the title VBox — not a real TempoText annotation on a Segment.

**`addText` is intended for title-page-style writes only** (title, composer, lyricist, etc.), not for positional annotations. The api_survey.md description of it at score.h:500 is consistent with this — but the survey's open question E and the api_write.md tool implementations assumed it could be used for positional text. It can't.

**Tempo BPM is not parsed.** [tempotext.cpp:260+, 493-500]. `TempoText::updateTempo()` parses BPM from text (e.g. `"♩=120"`) only when `m_followText` is true. Default is `false` ([tempotext.h:113]). The `addText` implementation above does NOT set `followText` and does NOT specifically instantiate a `TempoText` — it always makes a generic `Text` element via `Factory::createText` styled with the requested `TextStyleType`. So even if `addText` did land at the right position, it would produce display text with no functional BPM.

### Status: ❌ does NOT work for any of the four positional-text tools

**Required redesign — for each affected tool:**

**`add_rehearsal_mark(measure, text)`** — Use `newElement(Element.REHEARSAL_MARK)` + `set(Pid.TEXT, …)` + `cursor.add(mark)` after positioning cursor at measure start. The cursor's default branch ([cursor.cpp:428-430](C:\s\MS-core-api\src\engraving\api\v1\cursor.cpp#L428-L430)) parents the element to the current segment and calls `undoAddElement` — should land as a segment annotation. ❓ Runtime probe needed.

**`add_tempo_mark(measure, tempo)`** — Use `newElement(Element.TEMPO_TEXT)` + `set(Pid.TEXT, "♩=120")` + `set(Pid.TEMPO, bpmRatio)` + ❓ `set(Pid.TEMPO_FOLLOW_TEXT, true)` (if that Pid exists), then `cursor.add(tempoText)`. The follow-text question for a programmatically-set tempo is open and needs runtime confirmation that the BPM is honored by playback. **Update `api_write.md` open question E to mark this as confirmed-broken via `addText`.**

**`add_staff_text(location, text)`** — Use `newElement(Element.STAFF_TEXT)` + `set(Pid.TEXT, …)` + `cursor.add(text)`.

**`add_system_text(measure, text)`** — Use `newElement(Element.SYSTEM_TEXT)` + `set(Pid.TEXT, …)` + `cursor.add(text)`.

**Element enum values needed:** `Element.REHEARSAL_MARK`, `Element.TEMPO_TEXT`, `Element.STAFF_TEXT`, `Element.SYSTEM_TEXT` should all be valid (they exist in the `ElementType` enum at types.h). Worth confirming exact spellings (`TEMPO_TEXT` vs `TEMPO`).

---

## 7. Volta construction — REAL GAP

**Proposed:** `newElement(Element.VOLTA)` + set tick range + text.

### Findings

**Element type valid.** `Element.VOLTA` is accepted by `newElement()`. `Volta` extends `TextLineBase` which extends `Spanner`.

**Spanner wrapper writable.** [elements.h:2559-2601]:
- `API_PROPERTY(spannerTick, SPANNER_TICK)` — writable
- `API_PROPERTY(spannerTicks, SPANNER_TICKS)` — writable
- `API_PROPERTY_T(int, spannerTrack2, SPANNER_TRACK2)` — writable
- `API_PROPERTY_T(int, anchor, ANCHOR)` — writable
- No volta-specific wrapper subclass; no `voltaEndings` or `voltaText` property.

**Text via Pid system.** `v.set(Pid.TEXT, "1.")` should work through the inherited TextLineBase. Volta endings (which control the "1.", "2." labels at the bracket) need `Pid.VOLTA_ENDING` with a vector<int> — ❓ Pid serialisation to QML may be awkward.

**The blocker: NO apiv1 path exists to register the spanner with the score.** The score-wide spanner registry (`spanners` accessor at [score.h:203]) is read-only. There is NO `Score.add()` or `Score.addElement()` Q_INVOKABLE — confirmed by grepping the apiv1 directory. The engraving side has `Score::undoAddElement()` which would handle spanners correctly, but it is not bridged.

`cursor.add(v)` for a Volta hits the `default` case in `Cursor::add` ([cursor.cpp:428-430](C:\s\MS-core-api\src\engraving\api\v1\cursor.cpp#L428-L430)): parent is set to the current segment (line 291), track is set, then `m_score->undoAddElement(s)` is called. For a regular annotation that's correct. For a Spanner this is **wrong**: a Volta needs to be in the score's `Spanner` list and needs its `tick2` / `track2` resolved properly. Spanners parented to a Segment via `undoAddElement` will likely not render, will not be reachable via `score.spanners`, and will not survive save/reload cleanly. (This is the same reason the `add-slur`/`add-hairpin`/`add-8va` cmd handlers exist — they call `score->cmdAddOttava()` / `score->addHairpins()` / `score->addSlur()` internally, which know how to register the spanner correctly. There is no analogous `cmd("add-volta")` registered.)

Spanner construction is the one part of the proposed write tool surface that apiv1 just does not support. The Volta tool needs either (a) a C++ patch adding `Score::addSpanner()` to the apiv1 wrapper, or (b) a new `cmd("add-volta")` registered in `notationactioncontroller.cpp` that operates on the current selection.

### Status: ❌ no working path through current apiv1

**Required action:**
- Mark `add_volta` as **deferred** in `api_write.md` until either apiv1 exposes a spanner-insertion method or a `cmd("add-volta")` is added.
- Same caveat applies (silently in the current design) to `add_pedal` (proposed via `newElement(Element.PEDAL)` + set tick range): pedals are also spanners with the same insertion problem. The `cmd("add-pedal")` family is not registered either (no `add-pedal` in the action controller surveys). **Flag `add_pedal` as the same issue.**
- For ottava-15 (`"15ma"` / `"15mb"`), `cmd("add-8va")` / `cmd("add-8vb")` only cover 8va/8vb. There is no `add-15ma` cmd. Construction via `newElement(Element.OTTAVA)` + Pid is the only path — and same spanner-insertion blocker applies. **The proposed `add_ottava` covers only 8va/8vb via cmd; 15ma/15mb is blocked by the same spanner gap.**

---

## 8. Section break and system break

**Proposed:** `cmd("section-break")` / `cmd("system-break")` after navigating to measure.

### Findings

**Action registration.** [notationactioncontroller.cpp:268-273](C:\s\MS-core-api\src\notation\internal\notationactioncontroller.cpp#L268-L273):
```cpp
registerAction("system-break", &Interaction::toggleLayoutBreak, LayoutBreakType::LINE, ...);
registerAction("section-break", &Interaction::toggleLayoutBreak, LayoutBreakType::SECTION, ...);
```

(Also `page-break` → `LayoutBreakType::PAGE`.)

**Handler behaviour.** `Interaction::toggleLayoutBreak` → `Score::cmdToggleLayoutBreak()` at [cmd.cpp:3970-4009](C:\s\MS-core-api\src\engraving\editing\cmd.cpp#L3970-L4009). Requires `selection().isRange()` and calls `selection().measureRange(&startMeasure, &endMeasure)` to extract the affected measures. Returns early if the selection is not a range or contains no measures. Operates on the end measure of the range (line 4003) — attaches the LayoutBreak to that measure-base.

**Single-element selection (e.g. a note inside the measure) is rejected.** The selection must be a range. To target a whole measure programmatically, set the range to span the measure across all staves:

```js
var m = measureLookup(measureNo)
var startTick = m.firstSegment.tick
var endTick = startTick + m.ticks.ticks   // exclusive
curScore.selection.selectRange(startTick, endTick, 0, curScore.nstaves)
api.engraving.cmd("section-break")
```

Note `endStaff = nstaves` (exclusive — selectRange uses exclusive end bounds, see §2). No special preconditions beyond that.

### Status: ✅ works as designed, with the selection setup above

**Revised implementation note for `add_section_break`:**
```js
curScore.startCmd("section break")
var m = findMeasureByNumber(measureNo)  // helper that walks firstMeasure → nextMeasure
var startTick = m.firstSegment.tick
var endTick = startTick + m.ticks.ticks
curScore.selection.selectRange(startTick, endTick, 0, curScore.nstaves)
api.engraving.cmd("section-break")
curScore.endCmd()
```

Same pattern for `system-break` / `page-break`.

---

## Cross-cutting concerns flagged for `api_write.md`

1. **§6 — `addText` insertion-point fallacy.** Four tool implementations (`add_rehearsal_mark`, `add_tempo_mark`, `add_staff_text`, `add_system_text`) must abandon `addText()`. Switch to `newElement(Element.X)` + `set(Pid.TEXT, …)` + `cursor.add()`. The tool signatures themselves do not change — only the implementation note.

2. **§7 — Spanner construction is unsupported in apiv1 today.** `add_volta` and `add_pedal` are blocked. `add_ottava` works for 8va/8vb only (via cmd); 15ma/15mb is blocked. Document these as deferred or mark a C++ patch to `engravingapiv1` as a prerequisite.

3. **§3, §4, §5 — `segment.add()` does not exist.** Three tool implementations mention `segment.add()`; the actual path is `cursor.add()` (default-case fall-through) or `chord.add()` (for Lyrics).

4. **§4, §5 — Direct property writes are read-only for Harmony/Lyrics text.** `harmonyName`, `text`, and `verse` are not writable Q_PROPERTYs. Use `set(Pid.X, …)` instead. This is purely an implementation-note correction, not a signature change.

5. **§2 — `add_dynamic` cannot use `cmd("add-dynamic")`.** That action opens an interactive popup. Forces `add_dynamic` to use direct construction (§3) — which is fine, just remove the "or `cmd("add-dynamic")` with follow-up" sentence from the implementation note.

6. **§1 — Cursor positioning gotchas.** Document the three: (a) set `cursor.track` BEFORE `rewindToFraction`, (b) prefer `rewindToTick(int)` over `rewindToFraction(Fraction*)` to avoid the Fraction-construction step, (c) `addNote`/`addRest` do NOT advance the cursor — explicit `next()` required between sequential entries.

7. **§6 — Open question E in `api_survey.md` ("Tempo programmatic write … not tested end-to-end") can be partly closed.** `addText("TEMPO", "♩=120")` is confirmed broken for two reasons: it ignores position, AND it doesn't produce a real TempoText with parsed BPM. The remaining open question is whether `newElement(Element.TEMPO_TEXT) + set(Pid.TEMPO, …) + set(Pid.TEMPO_FOLLOW_TEXT, true)` actually drives playback tempo. That needs a runtime probe.

---

## Items needing runtime probe before implementation (❓)

In rough priority order:

1. **(blocking)** Confirm `api.engraving.Pid.*` enum is exposed in the v2 form-extension scope. Without it, all the `set(Pid.X, …)` workarounds for Dynamic / Harmony / Lyrics / Volta text are dead.
2. **(blocking)** Confirm `Element.REHEARSAL_MARK`, `Element.TEMPO_TEXT`, `Element.STAFF_TEXT`, `Element.SYSTEM_TEXT` are valid newElement() type values, with correct enum spellings.
3. **(blocking)** Confirm `cursor.add(rehearsalMark)` / `cursor.add(staffText)` actually render as positional annotations and not as floating elements. The `default` branch in `Cursor::add` was designed for the broad miscellaneous case and may not produce correct visuals for elements that need specific segment-type parents (e.g. RehearsalMark needs a `SegmentType::ChordRest` segment, not a clef segment).
4. **(high)** For Harmony: confirm `Pid.HARMONY_NAME` is the right Pid (vs `Pid.TEXT`). Confirm the chord-symbol parser fires correctly when written via Pid (vs the engraving setter `setHarmony(String)` which triggers parsing explicitly).
5. **(high)** For Dynamic: confirm `Pid.DYNAMIC_TYPE` integer values produce the expected glyph (pp, mf, ff, etc.). May need a constant table.
6. **(high)** For TempoText: confirm whether `Pid.TEMPO` accepts a BPM-as-ratio, whether `Pid.TEMPO_FOLLOW_TEXT` exists, and whether the result actually drives playback.
7. **(medium)** Confirm enum surfaces for `LyricsSyllabic`, `DynamicType`, `OttavaType`, etc. are reachable from the v2 extension scope (the v1 `PluginAPI` registers many of these as nested enums; the v2 surface inherits them via the same `EngravingApiV1` wrapper but the exact accessor path needs a runtime print).

These can all be answered with a small throwaway extension that exercises each path against a real score and dumps the resulting `segment.annotations[…].type` and `subtypeName()`. Recommend writing such a probe before the first user-facing tool is wired up.
