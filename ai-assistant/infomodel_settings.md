# Information Model — Settings
_Domain: score-level view settings, metadata, and per-instrument MIDI parameters._
_Audio mixer (dB faders, solo, send) is a separate concern — see constraints below._

---

## Types

### `LayoutMode`
How the score is displayed in MuseScore.

Values: `"page"` | `"continuous"` | `"horizontal"` | `"float"`

### `ViewSettings`
Score-level display toggles. All are readable and writable.

```
{
  layoutMode: LayoutMode,
  showInvisible: boolean,       // show invisible elements
  showUnprintable: boolean,     // show formatting/unprintable elements
  showFrames: boolean,
  showPageBorders: boolean,
  showSoundFlags: boolean,
  showVerticalFrames: boolean,
  showInstrumentNames: boolean,
  markIrregularMeasures: boolean,
  concertPitch: boolean         // toggle concert pitch / transposing pitch display
}
```

### `ScoreMetadata`
Writable score-level metadata tags.

```
{
  title: string,
  subtitle: string | null,
  composer: string | null,
  lyricist: string | null,
  arranger: string | null,
  copyright: string | null,
  translator: string | null
}
```

Additional arbitrary tags can be read/written by name via `curScore.metaTag(tag)` / `setMetaTag(tag, value)`.

### `MidiChannelSettings`
Per-instrument MIDI parameters. These are **engraving-model values (0–127 MIDI bytes)**, not audio mixer dB levels.

```
{
  instrument: string,    // instrument/part name as in score
  channelName: string,   // channel within the instrument (e.g. "normal", "pizzicato", "tremolo")
  volume: int,           // 0–127
  pan: int,              // 0–127 (64 = centre)
  chorus: int,           // 0–127
  reverb: int,           // 0–127
  mute: boolean,
  midiProgram: int,      // 0–127
  midiBank: int
}
```

> **Important:** `MidiChannelSettings.volume` is a MIDI parameter that affects playback velocity scaling. It is NOT the same as the audio mixer fader. To express a musical dynamic ("make this forte"), use a `Dynamic` notation element — not this setting.

---

## Audio mixer (per-track dB fader, solo, mute, aux sends)

Implemented in `MuseScore.Playback.MixerPanelModel`. Whether this module is accessible from a v2 form extension is **not yet confirmed** — a runtime probe is needed.

If accessible, the mixer exposes per-track:
- `volumeLevel` (audio dB, not MIDI 0–127)
- `balance` (audio pan)
- `muted`, `solo`
- `auxSendItemList` (reverb/FX sends)

Master volume and global FX are behind `IPlaybackController` / `IAudioOutput` — C++ only, not reachable from extension QML.

> **Action required:** runtime probe — try `import MuseScore.Playback 1.0` in a throwaway extension and instantiate `MixerPanelModel`. Result determines whether mixer tools are in or out of scope. See api_survey.md open question A.

---

## Notes on implementation

- `ViewSettings` fields map directly to `curScore.*` writable properties and have `cmd()` equivalents (`show-invisible`, `show-frames` etc.) — either path works.
- `concertPitch` has no direct property; use `cmd("concert-pitch")` to toggle.
- `ScoreMetadata` is read via `curScore.metaTag(tag)` and written via `curScore.setMetaTag(tag, value)`. Changes should be wrapped in `startCmd`/`endCmd` for undo correctness.
- `MidiChannelSettings` is reached via `part.instruments[i].channels[j]`. Changes wrapped in `startCmd`/`endCmd`.
