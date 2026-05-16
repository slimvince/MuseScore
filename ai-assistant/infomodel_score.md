# Information Model — Score & Contents
_Domain: the score and everything inside it._
_Canonical language: English. The LLM bridges for users in other languages._
_Note naming: international convention (C D E F G A B). Nordic H/B handled by LLM._

---

## Primitive types

### `NoteName`
A pitch expressed as pitch class + octave. Always a string.

Format: `"<class><accidental?><octave>"` — e.g. `"C4"`, `"F#3"`, `"Bb5"`, `"B4"` (B natural).

Pitch classes: `C D E F G A B`
Accidentals: `#` (sharp), `b` (flat), `##` (double sharp), `bb` (double flat), `` (natural, omitted)
Octave: integer, middle C = `"C4"`

### `Duration`
A note or rest length expressed as a string.

Values: `"longa"`, `"breve"`, `"whole"`, `"half"`, `"quarter"`, `"eighth"`, `"16th"`, `"32nd"`, `"64th"`, `"128th"`

Dotted: prefix with `"dotted "` — e.g. `"dotted quarter"`, `"dotted eighth"`
Double-dotted: prefix with `"double-dotted "` — e.g. `"double-dotted half"`

### `Beat`
A position within a measure.

```
{
  beat: int,           // 1-based beat number within the measure
  fraction: string     // offset within the beat as a fraction string: "0" | "1/2" | "1/4" | "3/4" | "1/3" | "2/3" | "1/6" | "1/8" etc.
}
```

Examples: beat 1 = `{ beat: 1, fraction: "0" }`, beat 2 and a half = `{ beat: 2, fraction: "1/2" }`

### `Dynamic`
A dynamic marking.

Values: `"ppp"`, `"pp"`, `"p"`, `"mp"`, `"mf"`, `"f"`, `"ff"`, `"fff"`,
`"fp"`, `"sf"`, `"sfz"`, `"fz"`, `"rfz"`, `"rf"`, `"sfp"`

### `Articulation`
An articulation marking.

Values: `"staccato"`, `"staccatissimo"`, `"tenuto"`, `"accent"`, `"marcato"`, `"stress"`, `"unstress"`,
`"fermata"`, `"shortFermata"`, `"longFermata"`, `"veryLongFermata"`,
`"upBow"`, `"downBow"`, `"snapPizzicato"`, `"leftHandPizzicato"`, `"harmonic"`,
`"trill"`, `"mordent"`, `"turn"`, `"tremolo"`

### `KeySignature`
A key expressed as tonic + mode.

Format: `"<tonic> <mode>"` — e.g. `"C major"`, `"G major"`, `"F# minor"`, `"Bb major"`, `"A minor"`

Tonic uses `NoteName` pitch class (no octave). Mode: `"major"` or `"minor"`.

### `TimeSignature`
```
{
  numerator: int,
  denominator: int    // 1 | 2 | 4 | 8 | 16 | 32
}
```
Examples: `{ numerator: 4, denominator: 4 }`, `{ numerator: 6, denominator: 8 }`

### `Tempo`
```
{
  bpm: int,
  unit: Duration,     // the beat unit — typically "quarter" or "half"
  text: string | null // optional text label e.g. "Allegro", "Andante"
}
```

### `Clef`
Values: `"treble"`, `"treble8vb"`, `"treble8va"`, `"bass"`, `"bass8vb"`, `"bass8va"`,
`"alto"`, `"tenor"`, `"soprano"`, `"mezzosoprano"`, `"baritone"`,
`"percussion"`, `"tab"`, `"tab4"`

### `BarlineType`
Values: `"normal"`, `"double"`, `"final"`, `"startRepeat"`, `"endRepeat"`,
`"startEndRepeat"`, `"dashed"`, `"dotted"`, `"short"`, `"tick"`

### `SyllabicType`
Values: `"single"`, `"begin"`, `"middle"`, `"end"`

### `Voice`
Integer `1`, `2`, `3`, or `4`. Voice 1 is the primary voice.

---

## Location

A position in the score used as a parameter in tool calls.

```
{
  measure: int,          // 1-based measure number
  beat: Beat,
  instrument: string,    // instrument/part name as it appears in the score (free text, any language)
  staff: int,            // 1-based staff index within the instrument (piano: 1 = treble, 2 = bass)
  voice: Voice
}
```

`instrument`, `staff`, and `voice` are optional in read tools — omit to query across all.

---

## Structures

### `Note`
```
{
  noteName: NoteName,
  duration: Duration,
  location: Location,
  tiedForward: boolean,      // tied to the next note
  tiedBack: boolean,         // continuation of a tie from the previous note
  grace: boolean,
  articulations: Articulation[],
  accidental: "natural" | "sharp" | "flat" | "doubleSharp" | "doubleFlat" | null
}
```

### `Rest`
```
{
  duration: Duration,
  location: Location,
  isFullMeasure: boolean
}
```

### `Harmony`
A chord symbol.
```
{
  text: string,          // as written in the score e.g. "Cmaj7", "Fm", "G7/B"
  measure: int,
  beat: Beat
}
```

### `Lyric`
```
{
  text: string,
  syllabic: SyllabicType,
  verse: int,            // 1-based verse number (NOTE: not yet a Q_PROPERTY in apiv1 — computed by position)
  location: Location
}
```

### `Spanner`
A spanner element (slur, hairpin, ottava, pedal, volta, etc.).
```
{
  type: string,          // "slur" | "hairpin-cresc" | "hairpin-decresc" | "ottava-8va" | "ottava-8vb" | "pedal" | "volta" | "trill-line" | ...
  startMeasure: int,
  startBeat: Beat,
  endMeasure: int,
  endBeat: Beat,
  instrument: string,
  staff: int
}
```

### `Part`
An instrument/part as seen in the score.
```
{
  name: string,          // full name as in score — free text, any language
  shortName: string,
  staves: int,           // number of staves (piano = 2, most instruments = 1)
  startTrack: int,       // internal track range — for tool use only
  endTrack: int
}
```

### `Measure`
```
{
  number: int,
  keySignature: KeySignature,
  timeSignature: TimeSignature,
  tempo: Tempo | null,
  clefs: { instrument: string, staff: int, clef: Clef }[],
  barlineStart: BarlineType,
  barlineEnd: BarlineType,
  rehearsalMark: string | null,
  notes: Note[],
  rests: Rest[],
  harmonies: Harmony[]
}
```

### `ScoreInfo`
Top-level score metadata — returned by `get_score_info()`.
```
{
  title: string,
  composer: string,
  lyricist: string | null,
  copyright: string | null,
  subtitle: string | null,
  measureCount: int,
  durationSeconds: int,
  parts: Part[],
  initialKeySignature: KeySignature,
  initialTimeSignature: TimeSignature,
  initialTempo: Tempo | null
}
```

### `Structure`
Score-wide structural elements — returned by `get_structure()`.
```
{
  rehearsalMarks:        { measure: int, text: string }[],
  tempoChanges:          { measure: int, beat: Beat, tempo: Tempo }[],
  keyChanges:            { measure: int, beat: Beat, key: KeySignature }[],
  timeSignatureChanges:  { measure: int, timeSignature: TimeSignature }[],
  repeatBarlines:        { measure: int, type: "startRepeat" | "endRepeat" | "startEndRepeat" }[],
  voltas:                { startMeasure: int, endMeasure: int, text: string }[],
  sectionBreaks:         { measure: int }[],
  systemBreaks:          { measure: int }[]
}
```

---

## Notes on implementation

- All measure numbers are **1-based** throughout.
- All staff indices within an instrument are **1-based** (piano treble = staff 1, bass = staff 2).
- All voice numbers are **1-based** (1–4).
- `instrument` in `Location` is a free-text string matching the part name as it appears in the score. The LLM handles fuzzy matching between what the user says and the actual name in the score.
- `Dynamic` values are notation symbols and are language-neutral.
- `Lyric.verse` is computed by the tool implementation (not directly exposed in apiv1) — see api_survey.md open question D.
- MIDI channel volume (`Channel.volume`, 0–127) is NOT a dynamic marking. Tools that set dynamics use `Dynamic` values and insert notation elements, not MIDI parameters.
