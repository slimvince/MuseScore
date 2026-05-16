# CC Instruction — Runtime Probes + Architecture Investigation

## Mandatory reads before starting
- `C:\s\MS\CLAUDE.md`
- `C:\s\MS\STATUS.md` (header only)
- `C:\s\MS\build_and_test.md`
- Relevant memory files under `C:\Users\vince\.claude\projects\c--s-MS\memory\`
- `C:\s\MS\ai-assistant\api_write.md` — probe table at the bottom
- `C:\s\MS\ai-assistant\write_api_probe.md` — findings from source investigation

## Overview

Two tasks. Do them in order — architecture first (source only, no score needed), then runtime probes (requires MuseScore open with a score).

---

# Part A — Architecture investigation (source only)

## Goal

Before implementation begins, determine how to structure the extension code so it is maintainable and readable by the MuseScore community — not just by the original developer.

The required layer separation is:
1. **MuseScore layer** — functions that read/write `curScore`. No LLM concepts. MuseScore idioms. Documented for MuseScore developers.
2. **Tool schema definitions** — JSON that describes tools to the LLM API.
3. **Dispatch layer** — maps LLM tool call name → MuseScore function. Thin glue.
4. **UI layer** — existing chat interface. No score access.

Currently everything is in one `Main.qml`. Investigate how to separate these layers cleanly.

## Questions to investigate

### A1 — Can the extension import local JavaScript files?

Standard QML supports `import "MyFile.js" as MyLib` for local JS files. Test whether this works in the v2 form extension context:

- Does the extension loader deploy only `Main.qml`, or does it include all files in the extension directory?
- Check `muse/framework/extensions/internal/extensionsprovider.cpp` and `extensionbuilder.cpp` — how does the loader discover and load the QML file? Does it set an import path that includes the extension's own directory?
- Does the v2 engine's QML import search path include the directory containing `Main.qml`?
- Would a file `ScoreTools.js` placed alongside `Main.qml` in `C:\Users\vince\AppData\Local\MuseScore\MuseScore4\extensions\ai-assistant\` be importable via `import "ScoreTools.js" as ScoreTools`?
- Does the import validator in `extensionbuilder.cpp:42-60` scan or interfere with local file imports (it currently only checks for `Muse.` module imports)?

### A2 — Can the extension import local QML component files?

Similar question for `.qml` component files. Can `Main.qml` instantiate a component defined in `ToolSchemas.qml` placed in the same directory?

### A3 — Manifest implications

Does `manifest.json` need to declare additional files for them to be included in the extension package / installed correctly? Check the manifest schema in the extension loader source.

### A4 — Propose a file structure

Based on the findings above, propose a concrete file layout for the extension. For example:

```
ai-assistant/
  Main.qml              — UI layer only (chat interface, no score access)
  ScoreReader.js        — MuseScore read functions (get_notes_in_range etc.)
  ScoreWriter.js        — MuseScore write functions (add_dynamic etc.)
  PlaybackTools.js      — Playback control functions
  ToolSchemas.js        — JSON schema definitions for all tools (sent to LLM API)
  ToolDispatch.js       — Maps tool name string → function call
  manifest.json
```

Or if `.js` imports don't work, propose the best alternative (e.g. clearly delimited `// === SCORE READER ===` sections within Main.qml, or use of QML `QtObject` components).

The goal is that a MuseScore developer who has never seen an LLM API can open `ScoreReader.js` / `ScoreWriter.js` and understand every function without needing to know what a "tool schema" or "dispatch" is.

---

# Part B — Runtime probes (requires MuseScore open with a score)

## Method

Add a temporary `onCompleted` probe function to `Main.qml` that exercises each item below, logs results to the MuseScore extension log or displays them in an alert, then deploy and run. Remove the probe code when done. Do NOT restructure Main.qml — minimal surgical addition only.

Probe all items in a single deployment if possible to minimise round-trips.

---

## Probe 1 (BLOCKING) — `api.engraving.Pid.*` accessible from v2 extension scope

```js
console.log("Pid.TEXT:", api.engraving.Pid ? api.engraving.Pid.TEXT : "Pid NOT FOUND")
console.log("Pid.DYNAMIC_TYPE:", api.engraving.Pid ? api.engraving.Pid.DYNAMIC_TYPE : "NOT FOUND")
console.log("Pid.HARMONY_NAME:", api.engraving.Pid ? api.engraving.Pid.HARMONY_NAME : "NOT FOUND")
console.log("Pid.VERSE:", api.engraving.Pid ? api.engraving.Pid.VERSE : "NOT FOUND")
console.log("Pid.TEMPO:", api.engraving.Pid ? api.engraving.Pid.TEMPO : "NOT FOUND")
console.log("Pid.TEMPO_FOLLOW_TEXT:", api.engraving.Pid ? api.engraving.Pid.TEMPO_FOLLOW_TEXT : "NOT FOUND")
```

If `api.engraving.Pid` is undefined, try `api.engraving.curScore.newCursor().score` as an alternate path, or check whether `Pid` is available as a top-level QML enum via `import MuseScore 3.0`.

Record exact values if found — the integer values of `Pid.TEXT`, `Pid.DYNAMIC_TYPE`, `Pid.HARMONY_NAME`, `Pid.VERSE`, `Pid.TEMPO`, `Pid.TEMPO_FOLLOW_TEXT` are needed for implementation.

---

## Probe 2 (BLOCKING) — Element enum spellings for text types

```js
var types = ["REHEARSAL_MARK", "TEMPO_TEXT", "STAFF_TEXT", "SYSTEM_TEXT",
             "DYNAMIC", "HARMONY", "LYRICS", "VOLTA", "OTTAVA", "PEDAL"]
for (var i = 0; i < types.length; i++) {
    var val = api.engraving.Element[types[i]]
    console.log("Element." + types[i] + " =", val !== undefined ? val : "NOT FOUND")
}
```

Record exact enum integer values for each that is found. Note any that are missing or named differently.

---

## Probe 3 (BLOCKING) — `cursor.add()` renders positional annotations correctly

With a real score open, attempt to add a RehearsalMark and a StaffText element via cursor.add() and verify they appear in the correct measure:

```js
var s = api.engraving.curScore
s.startCmd("probe: add rehearsal mark")
var c = s.newCursor()
c.rewindToTick(0)  // measure 1
var rm = api.engraving.newElement(api.engraving.Element.REHEARSAL_MARK)
// set text via whatever Pid path probe 1 found
c.add(rm)
s.endCmd()
```

**Observe:** Does a rehearsal mark appear at measure 1? Is it at the correct position visually? Does it survive save/reload? Check `s.firstMeasure.firstSegment.annotations` to confirm the element is present.

Repeat for STAFF_TEXT.

---

## Probe 4 (HIGH) — Harmony Pid path and chord-symbol parsing

```js
var s = api.engraving.curScore
s.startCmd("probe: add harmony")
var c = s.newCursor()
c.track = 0
c.rewindToTick(0)
var h = api.engraving.newElement(api.engraving.Element.HARMONY)
h.set(api.engraving.Pid.HARMONY_NAME, "Cmaj7")  // use value from probe 1
c.add(h)
s.endCmd()
```

**Observe:** Does "Cmaj7" appear above the staff? Is it parsed correctly (root C, quality maj7) or rendered as raw text? Also try `Pid.TEXT` instead of `Pid.HARMONY_NAME` and note which produces correct parsing.

---

## Probe 5 (HIGH) — Dynamic type enum values and rendering

```js
// First find DynamicType enum values
console.log("DynamicType via api.engraving:", JSON.stringify(api.engraving.DynamicType))
// Try known values: PP=0? P=1? MF=?  — enumerate what's accessible
```

Then attempt to add a dynamic:
```js
var s = api.engraving.curScore
s.startCmd("probe: add dynamic")
var c = s.newCursor()
c.track = 0
c.rewindToTick(0)
var d = api.engraving.newElement(api.engraving.Element.DYNAMIC)
d.set(api.engraving.Pid.DYNAMIC_TYPE, 5)  // guess for MF — adjust based on enum probe
c.add(d)
s.endCmd()
```

**Observe:** Does a dynamic glyph appear? Is it the right one? Map the integer values to the `Dynamic` vocabulary from `infomodel_score.md` (ppp, pp, p, mp, mf, f, ff, fff, fp, sfz etc.).

---

## Probe 6 (HIGH) — TempoText: programmatic BPM drives playback

```js
var s = api.engraving.curScore
s.startCmd("probe: add tempo")
var c = s.newCursor()
c.track = 0
c.rewindToTick(0)
var t = api.engraving.newElement(api.engraving.Element.TEMPO_TEXT)
t.set(api.engraving.Pid.TEXT, "♩=120")
if (api.engraving.Pid.TEMPO !== undefined)
    t.set(api.engraving.Pid.TEMPO, 2.0)  // 120 BPM = 2.0 beats/sec
if (api.engraving.Pid.TEMPO_FOLLOW_TEXT !== undefined)
    t.set(api.engraving.Pid.TEMPO_FOLLOW_TEXT, true)
c.add(t)
s.endCmd()
```

**Observe:** Does the tempo mark appear? Does playback actually run at 120 BPM, or does it ignore the marking? If `Pid.TEMPO_FOLLOW_TEXT` is not found, try without it and observe.

---

## Probe 7 (MEDIUM) — Enum surfaces for LyricsSyllabic, DynamicType, OttavaType

```js
console.log("LyricsSyllabic:", JSON.stringify(api.engraving.LyricsSyllabic))
console.log("DynamicType:", JSON.stringify(api.engraving.DynamicType))
console.log("OttavaType:", JSON.stringify(api.engraving.OttavaType))
// Try alternates if not found at top level:
console.log("Lyrics.BEGIN:", api.engraving.Lyrics ? api.engraving.Lyrics.BEGIN : "not found")
```

Record whatever values are found. These are needed to build the vocabulary-to-integer lookup tables the tool layer will use.

---

## Output

Produce `C:\s\MS\ai-assistant\runtime_probe.md` with:
- **Part A:** file structure findings and a concrete proposed file layout
- **Part B:** one section per probe, with the console output observed, what it means for the implementation, and any revised implementation notes

Update `api_write.md` probe table — change 🔴/🟠/🟡 statuses to ✅/⚠️/❌ based on findings. Add a one-line revised note per item if the approach changes.
