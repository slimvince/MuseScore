# API — Playback Tools
_All playback tools dispatch via cmd(). No startCmd/endCmd needed — playback commands do not mutate the score._
_Playback state and position cannot be read back from extension QML. All tools are fire-and-forget._
_Types reference infomodel_playback.md._

---

## Transport

### `play()`
Starts or resumes playback from the current position.

**Parameters:** none

**Implementation:** `cmd("play")`

---

### `pause()`
Pauses playback. Position is held — `play()` resumes from the same point.

**Parameters:** none

**Implementation:** `cmd("pause")`

---

### `stop()`
Stops playback and returns to the beginning.

**Parameters:** none

**Implementation:** `cmd("stop")`

---

### `rewind()`
Returns the playhead to the start of the score without stopping if already stopped.

**Parameters:** none

**Implementation:** `cmd("rewind")`

---

### `play_from_selection()`
Starts playback from the current score selection. To play from a specific measure, first move the selection there using score navigation, then call this.

**Parameters:** none

**Implementation:** `cmd("play-from-selection")`

> **Constraint:** seeking to a specific measure or beat is not available from extension QML without a C++ patch. This is the only available position-targeting mechanism.

---

## Loop

### `set_loop(startMeasure, endMeasure)`
Sets loop in/out points to the given measure range and enables looping. Achieves this by selecting the range and calling loop-in / loop-out.

**Parameters:**
- `startMeasure: int` — 1-based
- `endMeasure: int` — 1-based

**Implementation:** Select range + `cmd("loop-in")` + `cmd("loop-out")` + `cmd("loop")` to enable.

---

### `toggle_loop()`
Toggles loop playback on or off.

**Parameters:** none

**Implementation:** `cmd("loop")`

---

## Options

### `toggle_metronome()`
Toggles the metronome click track.

**Parameters:** none

**Implementation:** `cmd("metronome")`

---

### `toggle_count_in()`
Toggles count-in before playback.

**Parameters:** none

**Implementation:** `cmd("countin")`

---

### `toggle_repeat()`
Toggles whether repeat barlines are observed during playback.

**Parameters:** none

**Implementation:** `cmd("repeat")`

---

### `toggle_chord_symbols()`
Toggles whether chord symbols are played back.

**Parameters:** none

**Implementation:** `cmd("play-chord-symbols")`
