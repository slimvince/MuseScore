# API — Read Tools
_Tools for querying the open score. No score mutations. No startCmd/endCmd needed._
_All types reference infomodel_score.md unless noted._

---

## `get_score_info()`

Returns top-level metadata about the open score.

**Parameters:** none

**Returns:** `ScoreInfo`

---

## `get_structure()`

Returns all score-wide structural elements: rehearsal marks, tempo changes, key changes, time signature changes, repeat barlines, voltas, section breaks.

**Parameters:** none

**Returns:** `Structure`

> Implementation note: reads from `segment.annotations` filtered by element type. Subtype strings are not a stable API — see api_survey.md open question C.

---

## `get_measure(measure)`

Returns the full contents of one measure across all staves and voices.

**Parameters:**
- `measure: int` — 1-based measure number

**Returns:** `Measure`

---

## `get_notes_in_range(startMeasure, endMeasure, instrument?, staff?, voice?)`

Returns all notes and rests in the given measure range. Optional filters narrow by instrument, staff within instrument, or voice.

**Parameters:**
- `startMeasure: int` — 1-based, inclusive
- `endMeasure: int` — 1-based, inclusive
- `instrument?: string` — part name as in score; omit for all instruments
- `staff?: int` — 1-based staff within instrument; omit for all staves
- `voice?: Voice` — 1–4; omit for all voices

**Returns:** `{ notes: Note[], rests: Rest[] }`

---

## `get_harmony_in_range(startMeasure, endMeasure)`

Returns all chord symbols in the given measure range.

**Parameters:**
- `startMeasure: int` — 1-based, inclusive
- `endMeasure: int` — 1-based, inclusive

**Returns:** `Harmony[]`

---

## `get_lyrics_in_range(startMeasure, endMeasure, instrument?)`

Returns all lyrics in the given measure range.

**Parameters:**
- `startMeasure: int` — 1-based, inclusive
- `endMeasure: int` — 1-based, inclusive
- `instrument?: string` — part name as in score; omit for all instruments

**Returns:** `Lyric[]`

> Implementation note: verse number is not a Q_PROPERTY in apiv1 — computed by position order per ChordRest. See api_survey.md open question D.

---

## `get_spanners_in_range(startMeasure, endMeasure, instrument?)`

Returns all spanners (slurs, hairpins, ottava lines, pedal markings, etc.) that overlap the given measure range.

**Parameters:**
- `startMeasure: int` — 1-based, inclusive
- `endMeasure: int` — 1-based, inclusive
- `instrument?: string` — part name as in score; omit for all instruments

**Returns:** `Spanner[]`

> Implementation note: reads from `curScore.spanners`, filters by tick range and type. Spanner type distinguished via `subtypeName()` — see api_survey.md open question C.

---

## `get_selection()`

Returns the current selection in the score.

**Parameters:** none

**Returns:**
```
{
  isRange: boolean,
  elements: {
    type: string,         // "note" | "rest" | "chord" | "measure" | "text" | ...
    measure: int,
    beat: Beat,
    instrument: string,
    staff: int,
    voice: Voice
  }[],
  startMeasure: int | null,
  endMeasure: int | null,
  startStaff: int | null,   // global staff index (not per-instrument)
  endStaff: int | null
}
```

---

## `get_midi_channel_settings(instrument?)`

Returns MIDI channel parameters for one or all instruments. See `MidiChannelSettings` in infomodel_settings.md.

**Parameters:**
- `instrument?: string` — part name as in score; omit for all instruments

**Returns:** `MidiChannelSettings[]`

---

## `get_view_settings()`

Returns current score view and display settings. See `ViewSettings` in infomodel_settings.md.

**Parameters:** none

**Returns:** `ViewSettings`

---

## `get_score_metadata()`

Returns writable score metadata tags. See `ScoreMetadata` in infomodel_settings.md.

**Parameters:** none

**Returns:** `ScoreMetadata`
