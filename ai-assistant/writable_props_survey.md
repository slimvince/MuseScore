# Writable-Property Survey — 6 Pid-Blocked Element Types

_Survey date: 2026-05-16. Source tree: `C:\s\MS\` (master branch).
Cross-reference: [api_write.md](api_write.md), [write_api_probe.md](write_api_probe.md),
[runtime_probe.md](runtime_probe.md).
Question being answered: "before committing to a C++ patch to expose `Pid` in
QML, do any of the 6 blocked element types already have a dedicated writable
property path that bypasses the need for `Pid`?"_

## Headline result

**All 6 tools are implementable today with zero C++ changes.** The Pid-blocking
conclusion in [runtime_probe.md](runtime_probe.md) is correct for the
`element.set(Pid.X, value)` route — but a completely separate route was
overlooked by the probe: the `API_PROPERTY*` macros declared on `EngravingItem`
([elements.h:88-134](../src/engraving/api/v1/elements.h#L88-L134)) emit
**`Q_PROPERTY(... READ get_X WRITE set_X)`** declarations whose `WRITE`
accessor expands at C++ compile time to `set(mu::engraving::Pid::X, val)`.
The macro substitutes the literal `Pid::X` token inside the wrapper's C++ source —
QML never has to name `Pid` at all. QML simply assigns the property by name:

```js
var rm = api.engraving.newElement(api.engraving.Element.REHEARSAL_MARK)
cursor.add(rm)          // ← real-parent FIRST
rm.text = "A"           // ← THEN set; macro-generated setter calls set(Pid::TEXT, "A")
```

The runtime probe rounds tested only the explicit `set(Pid.X, ...)` route and
correctly found `api.engraving.Pid` undefined. They never tried the dedicated
property names (`el.text = ...`, `el.dynamicType = ...`, etc.). Those names
have been writable since the apiv1 wrapper was introduced.

The C++ patch to expose `Pid` remains useful for any **future** tool that needs
a Pid not already exposed as a dedicated property — but it is not needed to
unblock any of the 6 tools listed below.

## Architectural note — why this works

`newElement(Element.X)` for all 5 non-Harmony element types in this survey
returns an `EngravingItem` wrapper directly (no element-specific subclass
exists in [elements.h](../src/engraving/api/v1/elements.h) for Dynamic,
RehearsalMark, TempoText, StaffText, or SystemText). Harmony has its own
subclass ([elements.h:2683](../src/engraving/api/v1/elements.h#L2683)) but
only adds three READ-ONLY accessors on top of the inherited EngravingItem
surface — it inherits every `API_PROPERTY` write path defined on the base.

`EngravingItem` spans [elements.h:148-1352](../src/engraving/api/v1/elements.h#L148)
and declares ~150 `API_PROPERTY*` entries. Each one expands per the macros
at [elements.h:88-134](../src/engraving/api/v1/elements.h#L88-L134):

```cpp
#define API_PROPERTY(name, pid) \
    Q_PROPERTY(QVariant name READ get_##name WRITE set_##name RESET reset_##name) \
    QVariant get_##name() const { return get(mu::engraving::Pid::pid); }  \
    void set_##name(QVariant val) { set(mu::engraving::Pid::pid, val); }  \
    void reset_##name() { reset(mu::engraving::Pid::pid); }
```

The `pid` argument is a literal token, baked into the wrapper's C++ at compile
time. From QML the user sets the property by its `name` — Pid is invisible.

## Per-element findings

### 1. DYNAMIC — `add_dynamic`

Tool needs: dynamic level (pp, mf, ff, …).

**Writable property:** `dynamicType` — [elements.h:634](../src/engraving/api/v1/elements.h#L634):
```cpp
API_PROPERTY(dynamicType,             DYNAMIC_TYPE)
```
QML usage: `dyn.dynamicType = 8  // MF`

Integer values from [runtime_probe.md](runtime_probe.md) Probe 5
(`api.engraving.DynamicType`): PPP=4, PP=5, P=6, MP=7, MF=8, F=9, FF=10, FFF=11,
FP=15, SF=17, SFZ=18, SFP=23, RFZ=25, FZ=27 (full table in that doc).

**Bonus writable property:** `subType` — [elements.h:332](../src/engraving/api/v1/elements.h#L332)
also writable (`API_PROPERTY_T(int, subType, SUBTYPE)`) but `dynamicType` is the
correct route — `SUBTYPE` is the generic Pid that Dynamic overrides to mean its
DynamicType internally; the dedicated `dynamicType` name is the one to use.

**Verdict:** ✅ workable path exists.

**Revised implementation:**
```js
curScore.startCmd("add dynamic")
var c = curScore.newCursor()
c.track = staffIdx * 4
c.rewindToTick(tickInt)
var dyn = api.engraving.newElement(api.engraving.Element.DYNAMIC)
c.add(dyn)
dyn.dynamicType = dynamicTypeEnumInt   // 8 = MF, see DynamicType table
curScore.endCmd()
```

### 2. HARMONY — `add_harmony`

Tool needs: chord-symbol text ("Cmaj7", "F#m7b5", …).

**Writable property:** `text` (inherited from EngravingItem) —
[elements.h:552](../src/engraving/api/v1/elements.h#L552):
```cpp
API_PROPERTY(text,                    TEXT)
```
QML usage: `h.text = "Cmaj7"`

Internally this calls `set(Pid::TEXT, "Cmaj7")` on the underlying engraving
`Harmony` element. Harmony inherits from TextBase; setting `Pid::TEXT` should
route through the same code path the user's typing does (TextBase write
triggers `genericText()`/parser invalidation). ❓ Runtime confirmation that the
chord-symbol parser actually fires from this path would be a one-line QML
re-test once a new probe round is set up.

The Harmony-specific writable properties also visible on EngravingItem
([elements.h:794-808](../src/engraving/api/v1/elements.h#L794-L808)):
`harmonyVoiceLiteral`, `harmonyVoicing`, `harmonyDuration`, `harmonyBassScale`,
`harmonyDoNotStackModifiers`. None of these set the chord-symbol text — they
control voicing/literal display. `text` is the route.

**Verdict:** ✅ workable path exists (assuming parser triggers correctly — re-probe recommended).

**Revised implementation:**
```js
curScore.startCmd("add harmony")
var c = curScore.newCursor()
c.track = staffIdx * 4
c.rewindToTick(tickInt)          // must land on a ChordRest segment
var h = api.engraving.newElement(api.engraving.Element.HARMONY)
c.add(h)
h.text = "Cmaj7"
curScore.endCmd()
```

### 3. REHEARSAL_MARK — `add_rehearsal_mark`

Tool needs: text label ("A", "B", …).

**Writable property:** `text` (inherited from EngravingItem) —
[elements.h:552](../src/engraving/api/v1/elements.h#L552). Same property as Harmony.

QML usage: `rm.text = "A"`

The probe already confirmed `cursor.add(rehearsalMark)` produces a visible
boxed mark above measure 1 ([runtime_probe.md](runtime_probe.md) Probe 3a).
Adding `rm.text = "A"` before `cursor.add()` should fill in the label.

**Verdict:** ✅ workable path exists.

**Revised implementation:**
```js
curScore.startCmd("add rehearsal mark")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(measureStartTickInt)
var rm = api.engraving.newElement(api.engraving.Element.REHEARSAL_MARK)
c.add(rm)
rm.text = "A"
curScore.endCmd()
```

### 4. TEMPO_TEXT — `add_tempo_mark`

Tool needs: display text ("♩=120") + functional BPM that drives playback.

**Writable properties (all on EngravingItem):**
- `text` — [elements.h:552](../src/engraving/api/v1/elements.h#L552). Display text.
- `tempo` — [elements.h:572](../src/engraving/api/v1/elements.h#L572):
  ```cpp
  API_PROPERTY(tempo,                   TEMPO)
  ```
  BPM as a quarters-per-second ratio (2.0 = 120 BPM).
- `tempoFollowText` — [elements.h:574](../src/engraving/api/v1/elements.h#L574):
  ```cpp
  API_PROPERTY_T(bool, tempoFollowText, TEMPO_FOLLOW_TEXT)
  ```
  When `true`, the engraving layer parses BPM out of the text on edit. When
  `false`, the `tempo` value is used as-is.
- `tempoAlignRightOfRehearsalMark` — [elements.h:577](../src/engraving/api/v1/elements.h#L577).
  Positioning, optional.

**Verdict:** ✅ fully workable.

Whether playback actually honors the programmatically-set BPM still needs a
runtime confirmation — but the write surface is no longer the blocker.
Recommend setting both `text` AND `tempo` AND `tempoFollowText = false` to
isolate which value drives playback; if `tempoFollowText = true` instead, set
the text to a parseable form like "♩=120" and let the engraving layer compute
the ratio.

**Revised implementation:**
```js
curScore.startCmd("add tempo")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(measureStartTickInt)
var tt = api.engraving.newElement(api.engraving.Element.TEMPO_TEXT)
c.add(tt)
tt.text = "♩=120"
tt.tempo = 2.0              // quarters per second
tt.tempoFollowText = false  // honor the .tempo value, not text parsing
curScore.endCmd()
```

### 5. STAFF_TEXT — `add_staff_text`

Tool needs: arbitrary text on one staff.

**Writable property:** `text` (inherited) — [elements.h:552](../src/engraving/api/v1/elements.h#L552).

**Verdict:** ✅ workable path exists.

**Revised implementation:**
```js
curScore.startCmd("add staff text")
var c = curScore.newCursor()
c.track = staffIdx * 4
c.rewindToTick(tickInt)
var st = api.engraving.newElement(api.engraving.Element.STAFF_TEXT)
c.add(st)
st.text = "rit."
curScore.endCmd()
```

### 6. SYSTEM_TEXT — `add_system_text`

Tool needs: arbitrary text on the whole system.

**Writable property:** `text` (inherited) — [elements.h:552](../src/engraving/api/v1/elements.h#L552).

**Verdict:** ✅ workable path exists.

**Revised implementation:**
```js
curScore.startCmd("add system text")
var c = curScore.newCursor()
c.track = 0
c.rewindToTick(measureStartTickInt)
var sysT = api.engraving.newElement(api.engraving.Element.SYSTEM_TEXT)
c.add(sysT)
sysT.text = "Coda"
curScore.endCmd()
```

## Summary table

| Tool                  | Element        | Writable property used         | Element line                                                       | Verdict | Re-probe needed?                          |
| --------------------- | -------------- | ------------------------------ | ------------------------------------------------------------------ | ------- | ----------------------------------------- |
| `add_dynamic`         | DYNAMIC        | `dynamicType`                  | [elements.h:634](../src/engraving/api/v1/elements.h#L634)          | ✅      | glyph renders correctly for value         |
| `add_harmony`         | HARMONY        | `text` (inherited)             | [elements.h:552](../src/engraving/api/v1/elements.h#L552)          | ✅      | chord-symbol parser fires from `text` set |
| `add_rehearsal_mark`  | REHEARSAL_MARK | `text` (inherited)             | [elements.h:552](../src/engraving/api/v1/elements.h#L552)          | ✅      | label text shows in the boxed mark        |
| `add_tempo_mark`      | TEMPO_TEXT     | `text`, `tempo`, `tempoFollowText` | [elements.h:552,572,574](../src/engraving/api/v1/elements.h#L552)  | ✅      | playback honors `tempo` value             |
| `add_staff_text`      | STAFF_TEXT     | `text` (inherited)             | [elements.h:552](../src/engraving/api/v1/elements.h#L552)          | ✅      | text renders                              |
| `add_system_text`     | SYSTEM_TEXT    | `text` (inherited)             | [elements.h:552](../src/engraving/api/v1/elements.h#L552)          | ✅      | text renders                              |

## Recommendation

**Implement all 6 tools using the dedicated writable properties.** No C++
patch is required. The next probe round (or first end-to-end tool wiring)
should confirm:

1. `el.text = "..."` actually displays text for each of the 4 text-bearing
   element types (Harmony, RehearsalMark, StaffText, SystemText) — only the
   probe path was wrong, the underlying engraving path has worked since the
   apiv1 wrapper exists.
2. For Harmony specifically, that `h.text = "Cmaj7"` triggers the chord-symbol
   parser (otherwise the chord stays as raw text without the diagram lookup).
3. For TempoText, that `tt.tempo = 2.0` actually drives playback (with
   `tempoFollowText = false`).
4. For Dynamic, that `dyn.dynamicType = 8` renders the MF glyph.

These probes are now trivial — single property assignments instead of the
Pid-blocked `set()` call.

## Knock-on for other "Pid-blocked" tools

The same architectural fact applies to two other tools previously categorized
as Pid-blocked:

- **`add_lyric`** — `verse` is directly writable via
  [elements.h:753](../src/engraving/api/v1/elements.h#L753)
  (`API_PROPERTY_T(int, verse, VERSE)`); `text` via the same inherited route
  as above. Fully unblocked.
- **`add_ottava` 15ma/15mb** — `ottavaType` is directly writable via
  [elements.h:609](../src/engraving/api/v1/elements.h#L609)
  (`API_PROPERTY_T(int, ottavaType, OTTAVA_TYPE)`). Pid not needed. The
  remaining open question for this tool is the spanner-insertion
  question from [write_api_probe.md §7](write_api_probe.md) — whether
  `cursor.add(ottava)` actually registers a spanner correctly. That is
  separate from Pid and not addressed by this survey.

So the practical impact: **8 tools** previously categorized as "blocked on
Pid exposure" are actually implementable today using dedicated writable
properties already on the apiv1 surface.

## What the Pid C++ patch is still useful for

If a future tool needs to set a Pid that does **not** have a dedicated
`API_PROPERTY` entry — for example, properties added to MuseScore's engraving
layer between releases that haven't yet been wrapped — then exposing `Pid` as
a QML enum would let the extension write to them via the generic
`set(Pid.X, value)` route without waiting for an `engravingapiv1.h` patch.

This is a long-tail convenience, not a blocker for any tool currently
proposed in [api_write.md](api_write.md).
