# API — Write Tools
_All write tools must be wrapped in `startCmd(name)` / `endCmd()` for undo correctness._
_Each tool call produces one named undo entry the user can reverse with Ctrl+Z._
_All types reference infomodel_score.md unless noted._
_Implementation notes updated from write_api_probe.md (2026-05-16)._

---

## Cursor positioning pattern
Many write tools position a cursor before acting. The correct order is always:
```js
var c = curScore.newCursor()
c.track = staffIndex * 4 + (voice - 1)  // set BEFORE rewind
c.rewindToTick(tickInt)                  // simpler than rewindToFraction
```
`addNote`/`addRest` do NOT advance the cursor — call `c.next()` between sequential entries.

## Element construction pattern — add-first-then-set

**Always call `cursor.add(element)` BEFORE setting properties on the element.**
The add call real-parents the element in the engraving layer; property writes on an
unparented element may not take effect.

```js
// CORRECT
var el = api.engraving.newElement(api.engraving.Element.X)
c.add(el)          // real-parent FIRST
el.text = "..."    // THEN set properties

// WRONG — properties may not survive
var el = api.engraving.newElement(api.engraving.Element.X)
el.text = "..."    // set before add — may not work
c.add(el)
```

Confirmed by Runtime Probe Round 2 (2026-05-16).

---

## Pitch and note properties

### `set_note_pitch(location, pitch)`
Changes the pitch of an existing note.

**Parameters:**
- `location: Location`
- `pitch: NoteName`

**Implementation:** `note.pitch` + `note.tpc` direct property write inside `startCmd`/`endCmd`.

---

### `set_note_duration(location, duration)`
Changes the duration of an existing note or rest. Overwrites at that position — does not shift subsequent notes.

**Parameters:**
- `location: Location`
- `duration: Duration`

**Implementation:** cursor to location + `cursor.setDuration(z, n)` + `cursor.addNote(pitch, false)`.

---

### `set_note_accidental(location, accidental)`
Sets or removes the accidental on a note.

**Parameters:**
- `location: Location`
- `accidental: "sharp" | "flat" | "natural" | "doubleSharp" | "doubleFlat" | "none"`

**Implementation:** `note.accidentalType` direct property write.

---

### `set_note_velocity(location, velocity)`
Sets the playback velocity override for a note (0–127). Prefer `add_dynamic` for musical expression.

**Parameters:**
- `location: Location`
- `velocity: int` — 0–127

**Implementation:** `note.userVelocity` + `note.veloType` direct property write.

---

## Note entry

### `add_note(location, pitch, duration)`
Adds a new note at the given location, overwriting whatever is currently there.

**Parameters:**
- `location: Location`
- `pitch: NoteName`
- `duration: Duration`

**Implementation:**
```js
curScore.startCmd("add note")
var c = curScore.newCursor()
c.track = staffIdx * 4 + (voice - 1)
c.rewindToTick(tickInt)
c.setDuration(z, n)
c.addNote(pitchInt, false)
curScore.endCmd()
```

---

### `add_note_to_chord(location, pitch)`
Adds a pitch to an existing chord. Duration unchanged.

**Parameters:**
- `location: Location`
- `pitch: NoteName`

**Implementation:** same cursor setup + `c.addNote(pitchInt, true)`.

---

### `add_rest(location, duration)`
Adds a rest at the given location.

**Parameters:**
- `location: Location`
- `duration: Duration`

**Implementation:** same cursor setup + `c.setDuration(z, n)` + `c.addRest()`.

---

## Articulations

### `add_articulation(location, articulation)`
Adds an articulation to the chord at the given location.

**Parameters:**
- `location: Location`
- `articulation: Articulation`

**Implementation:** `cmd("add-staccato")` / `cmd("add-accent")` etc. after setting selection to target chord.

---

### `add_tie(location)`
Ties the note at the given location to the next note of the same pitch.

**Parameters:**
- `location: Location`

**Implementation:** select target note + `cmd("tie")`.

---

## Dynamics and hairpins

### `add_dynamic(location, dynamic)`
Adds a dynamic marking at the given beat position.

**Parameters:**
- `location: Location` — `voice` field ignored; dynamic applies to the staff
- `dynamic: Dynamic`

**Implementation:** direct construction — `cmd("add-dynamic")` is interactive and unusable for tooling.
```js
curScore.startCmd("add dynamic")
var c = curScore.newCursor()
c.track = staffIdx * 4
c.rewindToTick(tickInt)
var d = api.engraving.newElement(api.engraving.Element.DYNAMIC)
c.add(d)                             // real-parent FIRST
d.dynamicType = dynamicTypeEnumInt   // THEN set type (e.g. 8 = MF)
curScore.endCmd()
```
✅ **Implementable today** ([writable_props_survey.md](writable_props_survey.md) §1). `dynamicType` is a directly writable Q_PROPERTY on EngravingItem ([elements.h:634](../src/engraving/api/v1/elements.h#L634)) — the `API_PROPERTY` macro emits a typed setter that internally calls `set(Pid::DYNAMIC_TYPE, val)` at C++ compile time, bypassing the QML Pid problem. Integer values from `api.engraving.DynamicType` (PPP=4, PP=5, P=6, MP=7, MF=8, F=9, FF=10, FFF=11, FP=15, SF=17, SFZ=18, SFP=23, RFZ=25, FZ=27 — full table in [runtime_probe.md](runtime_probe.md) Probe 5). The probe round flagged this as Pid-blocked because it only tried `d.set(Pid.DYNAMIC_TYPE, …)`; the direct-property route was overlooked.

---

### `add_hairpin(startLocation, endLocation, type)`
Adds a crescendo or decrescendo hairpin.

**Parameters:**
- `startLocation: Location`
- `endLocation: Location`
- `type: "cresc" | "decresc"`

**Implementation:** `selection.selectRange(startTick, endTick, staffIdx, staffIdx + 1)` + `cmd("add-hairpin")` / `cmd("add-hairpin-reverse")`. Note: selection is not restored after the cmd.

---

## Spanners

### `add_slur(startLocation, endLocation)`
Adds a slur from one note to another.

**Parameters:**
- `startLocation: Location`
- `endLocation: Location`

**Implementation:** `selection.selectRange(...)` + `cmd("add-slur")`. Selection not restored after cmd.

---

### `add_ottava(startLocation, endLocation, type)`
Adds an ottava line. Only 8va and 8vb are available — 15ma/15mb require a C++ patch and are deferred.

**Parameters:**
- `startLocation: Location`
- `endLocation: Location`
- `type: "8va" | "8vb"` — ⚠️ 15ma/15mb deferred (spanner insertion gap, see below)

**Implementation:** `selection.selectRange(...)` + `cmd("add-8va")` / `cmd("add-8vb")`.

---

### `add_pedal(startLocation, endLocation)`
⚠️ **DEFERRED** — spanner insertion not supported in current apiv1. No `cmd("add-pedal")` exists. Requires either a C++ patch adding `Score.addSpanner()` to apiv1, or a new registered action. See write_api_probe.md §7.

---

### `add_volta(startMeasure, endMeasure, text)`
⚠️ **DEFERRED** — same spanner insertion gap. `cursor.add()` incorrectly parents a Volta to a Segment; spanners must be registered via `Score::undoAddElement()` which is not exposed in apiv1. No `cmd("add-volta")` exists. Requires C++ patch. See write_api_probe.md §7.

---

## Text and marks

### `add_rehearsal_mark(measure, text)`
Adds a rehearsal mark at the start of a measure.

**Parameters:**
- `measure: int` — 1-based
- `text: string` — e.g. `"A"`, `"B"`, `"Verse"`

**Implementation:** `newElement(Element.REHEARSAL_MARK)` + `rm.text = text` + `cursor.add()` after positioning at measure start. Note: `addText("REHEARSAL_MARK", text)` does NOT work — it ignores position and inserts into the title VBox. See write_api_probe.md §6.
```js
curScore.startCmd("add rehearsal mark")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(measureStartTickInt)
var rm = api.engraving.newElement(api.engraving.Element.REHEARSAL_MARK)
c.add(rm)          // real-parent FIRST
rm.text = "A"      // THEN set text
curScore.endCmd()
```
✅ **Implementable today** ([writable_props_survey.md](writable_props_survey.md) §3). `text` is a directly writable Q_PROPERTY inherited from EngravingItem ([elements.h:552](../src/engraving/api/v1/elements.h#L552)); the macro emits a setter that calls `set(Pid::TEXT, val)` at C++ compile time. `cursor.add(RehearsalMark)` plumbing was already runtime-verified (Probe 3a). The earlier "blocked on Pid" call was a probe oversight — the probe used `rm.set(Pid.TEXT, …)` which failed because Pid is undefined in QML, but the direct property route was never tried.

---

### `add_tempo_mark(measure, tempo)`
Adds a tempo marking at the start of a measure.

**Parameters:**
- `measure: int` — 1-based
- `tempo: Tempo`

**Implementation:** `newElement(Element.TEMPO_TEXT)` + direct property writes + `cursor.add()`. Note: `addText("TEMPO", ...)` is broken — ignores position and does not produce a functional BPM. See write_api_probe.md §6.
```js
curScore.startCmd("add tempo")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(measureStartTickInt)
var tt = api.engraving.newElement(api.engraving.Element.TEMPO_TEXT)
c.add(tt)                    // real-parent FIRST
tt.text = "♩=120"            // THEN set properties
tt.tempo = 2.0               // quarters-per-second; 2.0 = 120 BPM
tt.tempoFollowText = false   // honor the .tempo value (true = parse from text on edit)
curScore.endCmd()
```
✅ **Implementable today** ([writable_props_survey.md](writable_props_survey.md) §4). All three writes go through directly writable Q_PROPERTYs on EngravingItem: `text` ([elements.h:552](../src/engraving/api/v1/elements.h#L552)), `tempo` ([elements.h:572](../src/engraving/api/v1/elements.h#L572)), `tempoFollowText` ([elements.h:574](../src/engraving/api/v1/elements.h#L574)). The macros emit setters that call the corresponding `set(Pid::X, val)` at C++ compile time. Whether `tt.tempo = 2.0` actually drives playback remains to be runtime-verified (the probe round couldn't reach this question), but the write surface is no longer the blocker.

---

### `add_staff_text(location, text)`
Adds a staff text annotation. Appears above the specified staff.

**Parameters:**
- `location: Location` — `voice` field ignored
- `text: string`

**Implementation:** `newElement(Element.STAFF_TEXT)` + `st.text = text` + `cursor.add()`. Note: `addText("STAFF", ...)` is broken. See write_api_probe.md §6.
```js
curScore.startCmd("add staff text")
var c = curScore.newCursor()
c.track = staffIdx * 4
c.rewindToTick(tickInt)
var st = api.engraving.newElement(api.engraving.Element.STAFF_TEXT)
c.add(st)          // real-parent FIRST
st.text = "rit."   // THEN set text
curScore.endCmd()
```
✅ **Implementable today** ([writable_props_survey.md](writable_props_survey.md) §5). `text` is a directly writable inherited Q_PROPERTY on EngravingItem; no Pid access required.

---

### `add_system_text(measure, text)`
Adds a system text annotation that appears above all staves.

**Parameters:**
- `measure: int` — 1-based
- `text: string`

**Implementation:** `newElement(Element.SYSTEM_TEXT)` + `sysT.text = text` + `cursor.add()` after positioning at measure start. Note: `addText("SYSTEM", ...)` is broken. See write_api_probe.md §6.
```js
curScore.startCmd("add system text")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(measureStartTickInt)
var sysT = api.engraving.newElement(api.engraving.Element.SYSTEM_TEXT)
c.add(sysT)          // real-parent FIRST
sysT.text = "Coda"   // THEN set text
curScore.endCmd()
```
✅ **Implementable today** ([writable_props_survey.md](writable_props_survey.md) §6). `text` is a directly writable inherited Q_PROPERTY on EngravingItem; no Pid access required.

---

## Harmony and lyrics

### `add_harmony(measure, beat, instrument, text)`
Adds a chord symbol at the given beat position.

**Parameters:**
- `measure: int` — 1-based
- `beat: Beat`
- `instrument: string` — part name as in score
- `text: string` — chord symbol e.g. `"Cmaj7"`, `"Fm"`, `"G7/B"`

**Implementation:**
```js
curScore.startCmd("add chord symbol")
var c = curScore.newCursor()
c.track = staffIdx * 4
c.rewindToTick(tickInt)           // must land on a ChordRest segment
var h = api.engraving.newElement(api.engraving.Element.HARMONY)
c.add(h)                          // real-parent FIRST
h.text = text                     // THEN set text (inherited from EngravingItem)
curScore.endCmd()
```
Note: `harmonyName`, `plainText`, `displayText` on the Harmony subclass are read-only ([elements.h:2687-2691](../src/engraving/api/v1/elements.h#L2687-L2691)) — but the inherited `text` property from EngravingItem ([elements.h:552](../src/engraving/api/v1/elements.h#L552)) is writable. `segment.add()` does not exist in apiv1 — use `cursor.add()`. There is no `Pid.HARMONY_NAME` — the source-investigation guess in `write_api_probe.md` was wrong; the Harmony-specific Pids in `property.h` are `HARMONY_TYPE`, `HARMONY_VOICING`, `HARMONY_DURATION`, etc., but the chord-symbol text uses the inherited `TEXT`.
✅ **Implementable today** ([writable_props_survey.md](writable_props_survey.md) §2). One open runtime question remains: whether `h.text = "Cmaj7"` triggers the chord-symbol parser (which produces the formatted display and the diagram-database lookup) versus just setting raw text. The engraving setter `Harmony::setHarmony(String)` triggers parsing explicitly; `set(Pid::TEXT, …)` may or may not. Re-probe to confirm before relying on parsed-chord behavior.

---

### `add_lyric(location, text, syllabic, verse)`
Adds a lyric syllable to the note at the given location.

**Parameters:**
- `location: Location`
- `text: string`
- `syllabic: SyllabicType`
- `verse: int` — 1-based

**Implementation:**
```js
curScore.startCmd("add lyric")
var c = curScore.newCursor()
c.track = staffIdx * 4 + (voice - 1)
c.rewindToTick(tickInt)
var chord = c.element
var ly = api.engraving.newElement(api.engraving.Element.LYRICS)
chord.add(ly)                  // real-parent FIRST
ly.text = text                 // THEN set properties
ly.verse = verse - 1           // tool is 1-based, internal is 0-based
ly.syllabic = syllabicEnumInt
curScore.endCmd()
```
Note: `text` is writable via the inherited EngravingItem property ([elements.h:552](../src/engraving/api/v1/elements.h#L552)); `verse` is writable via [elements.h:753](../src/engraving/api/v1/elements.h#L753); `syllabic` and `lyricTicks` are writable via API_PROPERTY on EngravingItem. `chord.add()` is preferred over `cursor.add()` for lyrics. Syllabic constants are exposed as `api.engraving.Lyrics.{SINGLE:0, BEGIN:1, END:2, MIDDLE:3}` (under the `Lyrics` property, not `LyricsSyllabic` — runtime probe 2026-05-16).
✅ **Implementable today** ([writable_props_survey.md](writable_props_survey.md) "Knock-on" section). The earlier "partly blocked on Pid" call was the same probe oversight as the text tools — all four writes (`text`, `verse`, `syllabic`, `lyricTicks`) go through dedicated Q_PROPERTYs on EngravingItem.

---

## Structure

### `insert_measures(afterMeasure, count)`
Inserts new empty measures after the given measure.

**Parameters:**
- `afterMeasure: int` — 1-based; use `0` to insert before measure 1
- `count: int`

**Implementation:** navigate to target measure + `cmd("insert-measures")`.

---

### `append_measures(count)`
Appends new empty measures at the end of the score.

**Parameters:**
- `count: int`

**Implementation:** `curScore.appendMeasures(count)`.

---

### `delete_measure(measure)`
Deletes a measure and all its content.

**Parameters:**
- `measure: int` — 1-based

**Implementation:** select measure + `cmd("time-delete")`.

---

### `add_volta(startMeasure, endMeasure, text)`
⚠️ **DEFERRED** — see above under Spanners.

---

### `add_section_break(measure)`
Adds a section break at the end of a measure.

**Parameters:**
- `measure: int` — 1-based

**Implementation:**
```js
curScore.startCmd("section break")
var m = findMeasureByNumber(measureNo)
curScore.selection.selectRange(m.firstSegment.tick, m.firstSegment.tick + m.ticks.ticks, 0, curScore.nstaves)
api.engraving.cmd("section-break")
curScore.endCmd()
```
Same pattern for `system-break`.

---

### `add_system_break(measure)`
Adds a system break at the end of a measure.

**Parameters:**
- `measure: int` — 1-based

**Implementation:** same as `add_section_break` but `cmd("system-break")`.

---

## Score-level

### `set_score_metadata(metadata)`
Sets score metadata fields. Only provided fields are updated.

**Parameters:**
- `metadata: Partial<ScoreMetadata>`

**Implementation:** `curScore.setMetaTag(tag, value)` per field inside `startCmd`/`endCmd`.

---

### `set_view_settings(settings)`
Sets score display toggles. Only provided fields are updated.

**Parameters:**
- `settings: Partial<ViewSettings>`

**Implementation:** direct property writes on `curScore` or `cmd()` equivalents inside `startCmd`/`endCmd`.

---

### `set_midi_channel_settings(settings)`
Sets MIDI channel parameters. These are MIDI bytes (0–127), not audio mixer dB.

**Parameters:**
- `settings: MidiChannelSettings` — must include `instrument` and `channelName`

**Implementation:** property writes on `part.instruments[i].channels[j]` inside `startCmd`/`endCmd`.

---

## Deferred tools (require C++ patch to apiv1)

| Tool | Reason |
|---|---|
| `add_volta` | No `Score.addSpanner()` in apiv1; no `cmd("add-volta")` registered |
| `add_pedal` | Same spanner insertion gap; no `cmd("add-pedal")` registered |
| `add_ottava` 15ma/15mb | cmd covers 8va/8vb only. 15ma/15mb enum values are accessible (`OttavaType.OTTAVA_15MA=2`, `OTTAVA_15MB=3` — runtime probe 2026-05-16). `ottavaType` is a directly writable Q_PROPERTY on EngravingItem ([elements.h:609](../src/engraving/api/v1/elements.h#L609)), so direct construction + `cursor.add()` is the path. **Pid is NOT required** — see [writable_props_survey.md](writable_props_survey.md). The remaining open question is whether `cursor.add()` correctly registers a Spanner subclass (separate from Pid and from the spanner-insertion blocker below — re-probe needed). |

`add_volta` and `add_pedal` need either `Score.addSpanner()` exposed in `engravingapiv1.h`, or new `cmd()` actions registered in `notationactioncontroller.cpp`. `add_ottava` 15ma/15mb does not need the Pid patch (`ottavaType` is directly writable), but does need confirmation that `cursor.add()` registers a Spanner subclass correctly.

---

## Runtime probe results (2026-05-16; see [runtime_probe.md](runtime_probe.md))

| Item | Status | Note |
|---|---|---|
| `api.engraving.Pid.*` accessible | ❌ Not exposed | But ✅ **NOT a blocker for any currently proposed tool** — every Pid the six text/dynamic/tempo tools need has a dedicated writable Q_PROPERTY on `EngravingItem` that the `API_PROPERTY` macro generates with the Pid baked into the C++ setter ([writable_props_survey.md](writable_props_survey.md)). The probe round tested only the `set(Pid.X, …)` route and missed the direct-property route. |
| `Element.X` enum spellings | ✅ Confirmed | All 15 probed types resolve (REHEARSAL_MARK=60, TEMPO_TEXT=51, STAFF_TEXT=52, SYSTEM_TEXT=53, DYNAMIC=41, HARMONY=64, LYRICS=44, VOLTA=68, OTTAVA=102, PEDAL=103, HAIRPIN=101, SLUR=123, CHORD=122, NOTE=23, REST=28). All UPPER_SNAKE; values are integers. |
| `cursor.add()` for positional annotations | ✅ Working | RehearsalMark visibly inserted at m1. Probe's `firstSegment.annotations` read-back was on the keysig segment, not the chord segment — false-negative; the element WAS inserted. |
| Harmony text path | ✅ Use `h.text = "..."` (inherited from EngravingItem) | No `Pid.HARMONY_NAME` exists. `harmonyName` on the Harmony subclass is read-only, but the inherited `text` property is writable. Whether assigning `text` triggers the chord-symbol parser is the one remaining open question. |
| Dynamic `dynamicType` writable | ✅ Direct property; integer map captured | Use `dyn.dynamicType = 8` (MF). Full DynamicType lookup table: PPP=4, PP=5, P=6, MP=7, MF=8, F=9, FF=10, FFF=11, FP=15, SF=17, SFZ=18, SFP=23, RFZ=25, FZ=27. Glyph rendering remains visually unverified; re-probe with the direct setter. |
| TempoText programmatic BPM | ✅ Direct properties `text`, `tempo`, `tempoFollowText` writable | Whether `tempo = 2.0` actually drives playback is the remaining open question. |
| `LyricsSyllabic` / `DynamicType` / `OttavaType` surfaces | ⚠️ Partial | DynamicType ✅, OttavaType ✅ (8VA=0, 8VB=1, 15MA=2, 15MB=3, 22MA=4, 22MB=5 — 15ma/15mb ARE available, un-defer), HairpinType ✅, HarmonyType ✅, DynamicSpeed ✅. LyricsSyllabic exposed as `api.engraving.Lyrics.{SINGLE:0, BEGIN:1, END:2, MIDDLE:3}` (not LyricsSyllabic). TextStyleType ❌ undefined, VoltaType ❌ undefined. |

## Implication for each proposed write tool

| Tool | Implementable today? | Blocker |
|---|---|---|
| `set_note_pitch`, `set_note_duration`, `set_note_accidental`, `set_note_velocity` | ✅ Yes (direct property writes) | none |
| `add_note`, `add_note_to_chord`, `add_rest` | ✅ Yes (cursor API) | none |
| `add_articulation`, `add_tie` | ✅ Yes (cmd()) | none |
| `add_dynamic` | ✅ Yes (direct property `dynamicType`) | none |
| `add_hairpin` | ✅ Yes (cmd()) | none |
| `add_slur` | ✅ Yes (cmd()) | none |
| `add_ottava` 8va/8vb | ✅ Yes (cmd()) | none |
| `add_ottava` 15ma/15mb | ⚠️ Direct property `ottavaType` works; spanner registration via `cursor.add()` still needs runtime verification | Possibly the spanner-insertion gap, separate from Pid |
| `add_pedal` | ❌ Deferred (spanner insertion gap) | Needs `Score.addSpanner()` or `cmd("add-pedal")` |
| `add_volta` | ❌ Deferred (spanner insertion gap) | Needs `Score.addSpanner()` or `cmd("add-volta")` |
| `add_rehearsal_mark` | ✅ Yes (direct property `text`) | none |
| `add_tempo_mark` | ✅ Yes (direct properties `text`, `tempo`, `tempoFollowText`) | none; playback-honors-tempo still needs runtime verification |
| `add_staff_text` | ✅ Yes (direct property `text`) | none |
| `add_system_text` | ✅ Yes (direct property `text`) | none |
| `add_harmony` | ✅ Yes (direct property `text`) | none; chord-symbol parser firing from text-set still needs runtime verification |
| `add_lyric` | ✅ Yes (direct properties `text`, `verse`, `syllabic`, `lyricTicks`) | none |
| `insert_measures`, `append_measures`, `delete_measure` | ✅ Yes | none |
| `add_section_break`, `add_system_break` | ✅ Yes (cmd() with range selection) | none |
| `set_score_metadata`, `set_view_settings`, `set_midi_channel_settings` | ✅ Yes | none |

**Net:** ~21 tools implementable today (was ~13 before the writable-props
survey). 2 tools deferred behind the spanner-insertion C++ gap (`add_volta`,
`add_pedal`). Several tools carry follow-up runtime checks (chord-symbol
parser, playback-honors-tempo, dynamic-glyph render, ottava spanner
registration) but those are runtime confirmations, not implementation
blockers. The previously-recommended Pid C++ patch is **no longer on the
critical path** — it remains a long-tail convenience for any future tool
that needs a Pid not exposed via API_PROPERTY, but no proposed tool depends
on it.
