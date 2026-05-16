# Information Model — Playback
_Domain: transport control and playback behaviour._
_All control is fire-and-forget via cmd(). Playback position read-back is currently blocked — see constraints below._

---

## Types

### `TransportState`
Values: `"playing"` | `"paused"` | `"stopped"`

> **Constraint:** current transport state cannot be read from extension QML — `IPlaybackController` is not exposed. The LLM cannot ask "are we playing?" — it can only issue commands.

### `LoopState`
```
{
  enabled: boolean,
  startMeasure: int | null,   // null if not set
  endMeasure: int | null
}
```

> **Constraint:** loop in/out points can be set via cmd() but cannot be read back from extension QML.

### `PlaybackPosition`
```
{
  measure: int,
  beat: Beat    // see infomodel_score.md
}
```

> **Constraint:** current playback position cannot be read from extension QML (no QML-exposed property on `IPlaybackController`). Closing this gap requires a C++ patch to `extapi.h`. Until then, tools that report "where is the playhead?" cannot be implemented.

### `PlaybackOptions`
```
{
  playRepeats: boolean,
  playChordSymbols: boolean,
  metronome: boolean,
  countIn: boolean,
  autoPan: boolean            // score scrolls to follow playhead
}
```

> **Constraint:** individual option states cannot be read back — only toggled via cmd().

---

## Notes on implementation

- Seek to a specific measure is **not available** from extension QML. The only position-targeting available is `cmd("play-from-selection")` — which plays from whatever the score's current selection is. To play from measure N, a tool must first move the selection to that measure, then fire `cmd("play-from-selection")`.
- All transport commands are implemented via `cmd()` — no `startCmd`/`endCmd` bracket needed (playback commands do not mutate the score).
- Loop in/out points are set by first selecting the target range in the score, then calling `cmd("loop-in")` / `cmd("loop-out")`.
- Tempo multiplier (playback speed %) is C++ only — not reachable from extension QML.
