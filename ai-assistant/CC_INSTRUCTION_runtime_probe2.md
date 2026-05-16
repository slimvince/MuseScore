# CC Instruction — Runtime Probe Round 2 + Mixer Import Test

## This instruction is for the master worktree (`C:\s\MS\`)

## Mandatory reads before starting
- `C:\s\MS\CLAUDE.md`
- `C:\s\MS\STATUS.md` (header only)
- `C:\s\MS\build_and_test.md`
- Relevant memory files under `C:\Users\vince\.claude\projects\c--s-MS\memory\`
- `C:\s\MS\ai-assistant\runtime_probe.md` (prior probe results — context only)
- `C:\s\MS\ai-assistant\writable_props_survey.md` (explains what we're testing)
- `C:\s\MS\ai-assistant\api_write.md` (implementation patterns)

---

## Background

The first probe round confirmed that `api.engraving.Pid` is undefined in v2 extensions, but the
writable-properties survey subsequently found that all needed Pid values are exposed as directly
writable named Q_PROPERTYs (`el.text`, `dyn.dynamicType`, `tt.tempo`, etc.). This probe round
confirms the 4 direct-property write paths actually work end-to-end, plus tests whether
`MuseScore.Playback 1.0` is importable from a v2 form extension.

No C++ changes. No builds. Extension-only work.

---

## What to test (5 probes)

### Probe A — Harmony parser

Does setting `h.text = "Cmaj7"` on a HARMONY element trigger the chord-symbol parser, or does
it land as raw unstyled text?

```js
curScore.startCmd("probe-harmony")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(0)
var h = api.engraving.newElement(api.engraving.Element.HARMONY)
h.text = "Cmaj7"
c.add(h)
curScore.endCmd()

// Read back immediately after add
// (h wrapper may still be valid; record both)
results.push("A1. h.text after add: " + h.text)
results.push("A2. h.harmonyName after add: " + h.harmonyName)
results.push("A3. h.displayText after add: " + (typeof h.displayText !== "undefined" ? h.displayText : "undefined"))
```

Then navigate to tick 0 and read back the annotation from the score data model:
```js
// navigate to tick 0, find the first ChordRest segment, check its annotations
var seg = curScore.firstMeasure.firstSegment
while (seg && seg.segmentType !== 512 /* ChordRest */) {
    seg = seg.next
}
if (seg) {
    for (var i = 0; i < seg.annotations.length; i++) {
        var ann = seg.annotations[i]
        results.push("A4. annotation[" + i + "] type: " + ann.type + " text: " + ann.text + " harmonyName: " + ann.harmonyName)
    }
}
```

**What we want to know:** Is `harmonyName` populated (non-empty) after the add? If so, the parser
fired. If it equals "Cmaj7" exactly but is not styled/parsed, that's raw text mode.

---

### Probe B — TempoText BPM drives playback

Does `tt.tempo = 2.0` (= 120 BPM) with `tempoFollowText = false` actually register a playback
tempo?

```js
curScore.startCmd("probe-tempo")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(0)
var tt = api.engraving.newElement(api.engraving.Element.TEMPO_TEXT)
tt.text = "♩=120"
tt.tempo = 2.0
tt.tempoFollowText = false
c.add(tt)
curScore.endCmd()

results.push("B1. tt.tempo after set (before add): " + tt.tempo)
results.push("B2. tt.tempoFollowText: " + tt.tempoFollowText)
```

Also try to read back tempo from the score at tick 0 if the method exists:
```js
try {
    var t = curScore.tempo(0)
    results.push("B3. curScore.tempo(0) after add: " + t)
} catch(e) {
    results.push("B3. curScore.tempo(0): threw — " + e)
}
```

**What we want to know:** Does `curScore.tempo(0)` exist and return ~2.0 after the add? If not,
record what it returns or whether the method exists at all.

Note: Ultimate playback confirmation (does the score actually play at 120 BPM?) requires a
manual listener test — record in results whether the TempoText *visually* appears above the
measure with the "♩=120" text.

---

### Probe C — Dynamic glyph renders

Does `dyn.dynamicType = 8` (MF) render the MF glyph correctly?

```js
curScore.startCmd("probe-dynamic")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(0)
var dyn = api.engraving.newElement(api.engraving.Element.DYNAMIC)
dyn.dynamicType = 8
c.add(dyn)
curScore.endCmd()

results.push("C1. dyn.dynamicType after set: " + dyn.dynamicType)
```

Then navigate to tick 0 and read back the annotation:
```js
// same segment navigation as Probe A
// record annotation type, dynamicType, text
for (var i = 0; i < seg.annotations.length; i++) {
    var ann = seg.annotations[i]
    results.push("C2. annotation[" + i + "] type: " + ann.type + " dynamicType: " + ann.dynamicType + " text: " + ann.text)
}
```

**What we want to know:** Does `dynamicType = 8` survive the add and render as the MF glyph?
(Visual observation of the score is the final confirmation — describe what appears.)

---

### Probe D — Ottava spanner registration

Does `cursor.add(ottava)` correctly register an Ottava (spanner) in the score?

```js
curScore.startCmd("probe-ottava")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(0)
var ottava = api.engraving.newElement(api.engraving.Element.OTTAVA)
ottava.ottavaType = 0   // 8va
try {
    c.add(ottava)
    results.push("D1. cursor.add(ottava) succeeded without throw")
} catch(e) {
    results.push("D1. cursor.add(ottava) threw: " + e)
}
curScore.endCmd()
results.push("D2. ottava.ottavaType after add: " + ottava.ottavaType)
```

**What we want to know:** Did the add throw? Does an 8va bracket visually appear in the score?
If it doesn't appear or is only a zero-length bracket at the start, the spanner registration
is incomplete (consistent with the write_api_probe.md §7 concern).

---

### Probe E — MuseScore.Playback 1.0 import

Can a v2 form extension import `MuseScore.Playback 1.0`?

Add a small Item to the extension that imports the module. Do this via `Qt.createQmlObject`
so that a failed import does not prevent the rest of the extension from loading:

```js
var mixerTest = Qt.createQmlObject(
    'import MuseScore.Playback 1.0; Item { }',
    probeRoot,    // any QML object that exists
    "mixerProbe"
)
if (mixerTest !== null) {
    results.push("E1. MuseScore.Playback 1.0 import: SUCCESS — object created")
    // try to instantiate something from it to confirm it's real
    var apTest = Qt.createQmlObject(
        'import MuseScore.Playback 1.0; AudioPlug { }',
        probeRoot,
        "apProbe"
    )
    results.push("E2. AudioPlug instantiation: " + (apTest !== null ? "SUCCESS" : "FAILED"))
} else {
    results.push("E1. MuseScore.Playback 1.0 import: FAILED — null returned")
}
```

Also try `MuseScore.Audio 1.0` as an alternative:
```js
var audioTest = Qt.createQmlObject(
    'import MuseScore.Audio 1.0; Item { }',
    probeRoot,
    "audioProbe"
)
results.push("E3. MuseScore.Audio 1.0 import: " + (audioTest !== null ? "SUCCESS" : "FAILED"))
```

**What we want to know:** Does either module load? If so, what types does it expose? The goal
is to determine whether mixer/playback state (volume, mute, solo) is reachable at all from
a v2 form extension.

---

## Implementation

Add a `runProbes2()` function and a 🔬2 button to Main.qml using the same pattern as the
previous probe round (probeResults / probeVisible properties, results overlay). Run each
probe in sequence; collect all output into a single results string. Each probe should be
wrapped in try/catch so one failure does not block the rest.

**Important:** Each probe that writes to the score should do so inside its own
`startCmd`/`endCmd` pair. After all probes run, call `curScore.undo()` (or equivalent)
to undo all probe writes so the user's score is not permanently modified. If undo is not
feasible from QML, note this and leave the probe writes in place — the user can Ctrl+Z
manually.

---

## Undo note

The write probes (A–D) modify the open score. The cleanest approach is to wrap all four
probes in a single `startCmd("probe round 2")` / `endCmd()`, then immediately call
`cmd("undo")` after `endCmd()`. This leaves the score clean. If `cmd("undo")` does not
work (it may conflict with the undo stack state), add a note in the results output
instructing the user to press Ctrl+Z once.

---

## Deploy

Deploy gate first:
```
grep -nE "^[[:space:]]*(import[[:space:]]+Muse\.|FlatButton)" Main.qml
```
Must return empty. Then deploy to MS4:
```
copy "C:\s\MS\ai-assistant\Main.qml" "%LOCALAPPDATA%\MuseScore\MuseScore4\extensions\ai-assistant\Main.qml"
```

Do NOT deploy to MS5 for this probe — probe code is temporary.

---

## Output

Report:
1. The full raw probe output string (all A1–E3 lines)
2. Visual observations: what appeared in the score for each probe (harmony symbol, tempo
   mark, dynamic glyph, ottava bracket)
3. Whether undo worked cleanly

Do NOT remove the probe code — that is a follow-up step once results are reviewed.
