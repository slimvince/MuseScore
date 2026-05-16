# MuseScore 4/5 Extension & Plugin API Survey for an In-Process LLM Assistant

_Survey date: 2026-05-16. Source tree: `C:\s\MS-core-api\` (ms-core-api branch).
Verification anchor: `C:\s\MS\ai-assistant\Main.qml` v0.4.15 (empirically-working
form extension)._

This document inventories the host-to-QML APIs available to an in-process Large
Language Model (LLM) assistant for the purpose of building **tool-call**
endpoints. It exists to answer the prerequisite question for the
`ai-assistant` design: *what can a script in QML actually read, write, control,
and observe in the running MuseScore process today?*

Status markers used below:
- OK — symbol confirmed reachable and used in production, or registered via
  `Q_INVOKABLE` / `Q_PROPERTY` in a class injected into the extension QML
  scope (cited).
- PARTIAL — symbol exists but has caveats (subset of access, limited types,
  read-only when write is wanted, etc.).
- UNCERTAIN — symbol exists in the C++ tree but a path to it from the
  extension QML scope is not confirmed.
- BLOCKED — symbol exists but the loader / validator prevents extension QML
  from reaching it.

---

## 0. Two host APIs — keep them straight

The repo exposes **two separate host-to-QML APIs**, both of which the `ai-assistant`
design needs to reason about. They are NOT the same surface and they are NOT
loaded the same way.

### Surface A — "Extension API" (Muse framework, `type: "form"` extensions)

- Manifest declares `"type": "form"`. The `ai-assistant` extension uses this
  surface (`C:\Users\vince\AppData\Local\MuseScore\MuseScore4\extensions\ai-assistant\manifest.json`).
- Loader: `muse/framework/extensions/internal/extensionsprovider.cpp:150` →
  `interactive()->openSync(...)` → `ExtensionViewer.qml` →
  `ExtensionBuilder::load(...)` at
  `muse/framework/extensions/qml/Muse/Extensions/extensionbuilder.cpp:62`.
- Engine selection: `extensionbuilder.cpp:74-78`. If
  `manifest.apiversion == 1` the engine is
  `ExtensionsUiEngine::qmlEngineApiV1()`; otherwise it is
  `qmlEngine()` (the v2 engine). Default apiversion is 2
  (`extensionstypes.h:41`).
- Import validator: `extensionbuilder.cpp:42-60`,
  applied only when `manifest.apiversion != 1`. Refuses any line that starts
  with `import` and contains the literal substring `Muse.`. Does NOT block
  `MuseScore` or `MuseScore.Plugin` (no dot). Does not scan strings passed
  to `Qt.createQmlObject` at runtime — the `ai-assistant` Enter-key workaround
  exploits this (`Main.qml:140-166`).
- Injection: `muse/framework/extensions/internal/extensionsuiengine.cpp:60-70`
  installs a single global named `api` on the engine. For the v2 engine `api`
  is a `muse::extensions::api::ExtApi` instance (`extapi.h:34`). The v1 engine
  injects a `muse::extensions::apiv1::ExtApiV1` instance (`extapiv1.h:33`)
  with the same `api` name and a smaller surface.

What `api` exposes on the v2 engine (`extapi.h:37-83`):
| Property | Backing API |
| --- | --- |
| `api.log` | `MuseApi.Log` |
| `api.interactive` | `MuseApi.Interactive` (dialogs) |
| `api.theme` | `MuseApi.Theme` |
| `api.engraving` | `MuseApi.Engraving` — see below |
| `api.converter` | `MuseApi.Converter` |
| `api.websocket`, `api.websocketserver` | `MuseApi.Websocket*` |
| `api.dispatcher`, `api.navigation`, `api.shortcuts`, `api.keyboard`, `api.accessibility` | only via `extapi.h:75-79` — these are exposed in the C++ class but commented out of the `Q_PROPERTY` block, so they are NOT visible from QML. Marked in `extapi.h:46-49` as "Providing these APIs requires approval." |

**`api.engraving` is the key one.** It is fulfilled by
`mu::engraving::apiv1::EngravingApiV1` (`src/engraving/api/v1/engravingapiv1.h:42`),
which is registered as `"MuseApi.Engraving"`
(`src/engraving/api/v1/engravingapiv1.cpp` constructs `apiv1::PluginAPI` and
delegates to it). `EngravingApiV1` exposes `curScore` (line 53), the entire
enum surface, plus invokables `cmd`, `newScore`, `newElement`, `removeElement`,
`writeScore`, `readScore`, `closeScore`, `fraction`, `interval`, etc.
(`engravingapiv1.h:282-338`).

> **Net result for Surface A:** `api.engraving.curScore` returns the same
> `mu::engraving::apiv1::Score*` object that classic plugins call `curScore`
> on. This is empirically confirmed in `Main.qml:403`
> (`var s = api.engraving.curScore`). The full v1 plugin object tree
> (Score → Part → Staff → Measure → Segment → Chord → Note, Harmony, Lyrics,
> etc.) is reachable from Surface A.

### Surface B — "Classic plugin API" (`MuseScore { }` dock/dialog plugins)

- Sources: `src/engraving/api/v1/qmlpluginapi.{h,cpp}`, `score.{h,cpp}`,
  `cursor.{h,cpp}`, `elements.{h,cpp}`, `part.{h,cpp}`, `instrument.{h,cpp}`,
  `selection.{h,cpp}`, `excerpt.{h,cpp}`, `style.{h,cpp}`, `playevent.{h,cpp}`,
  `apistructs.{h,cpp}`, `enums.{h,cpp}`, `util.{h,cpp}`.
- The QML element is `MuseScore { pluginType: "dock" | "dialog" }`. It is
  registered globally via `qmlRegisterType<PluginAPI>("MuseScore", 3, 0, "MuseScore")`
  in `src/engraving/api/v1/qmlpluginapi.cpp:162`.
- Legacy loader path: form extensions whose manifest is marked
  `legacyPlugin = true` (set by `muse/framework/extensions/internal/legacy/extpluginsloader.cpp:240`)
  use `apiversion == 1` and go through the v1 engine
  (`extensionbuilder.cpp:139-156`), which calls `plugin->runPlugin()` and
  emits the classic `onRun()` signal. The QML root must be a
  `MuseScore { }` for this path to fire.
- `curScore` is a property of the `PluginAPI` (`MuseScore`) component
  (`qmlpluginapi.h:133`). Inside a plugin's own scope `curScore` is visible as
  a property of `this` (the root `MuseScore` object) and as a context
  property (also reachable as `MuseScore.curScore`).

### Critical equivalence: A and B share the model

`PluginAPI::curScore` (Surface B) and `EngravingApiV1::curScore` (Surface A,
via `api.engraving.curScore`) BOTH return a
`mu::engraving::apiv1::Score *` — the same wrapper class around the same
`mu::engraving::Score *`. Same `Part`, `Staff`, `Measure`, `Note`, `Harmony`,
`Cursor` classes, same Q_PROPERTYs, same Q_INVOKABLE methods. The accessor
path differs (`api.engraving.X` vs `X` at root scope) but the object graph
is identical.

This is the single most important fact for the LLM tool design:
**there is no API gap between what a `MuseScore { }` plugin can do and what
the `ai-assistant` form extension can do.** The Score/Cursor/Note tree is
fully reachable from Surface A today. The tool surface can be designed
against the v1 plugin object model without giving up the chat UI advantages
of the form-extension shell.

### What is NOT reachable from Surface A

- All `qmlRegisterType` calls in `src/playback/qml/MuseScore/Playback/`
  register under the `MuseScore.Playback` QML module URI
  (`src/playback/qml/MuseScore/Playback/CMakeLists.txt:24` declares
  `URI MuseScore.Playback`). These declare C++ models named
  `MixerPanelModel`, `MixerChannelItem`, etc. The validator does not literally
  block `import MuseScore.Playback`, but the type registrations require the
  `playback` module to be loaded into the QML engine in a way that exposes
  them. **Not confirmed accessible from a v2 form extension** — testing
  required.
- Anything in a `Muse.<...>` module (`Muse.Ui`, `Muse.UiComponents`,
  `Muse.Shortcuts`, etc.) is blocked by the import validator at file-parse
  time. Runtime `Qt.createQmlObject` bypasses the validator (this is how
  Main.qml gets `NavigationSection` for the Enter-key workaround).
- The dispatcher (`api.dispatcher` in `extapi.h:75`) and shortcuts
  (`api.shortcuts`) are intentionally not exposed to v2 extensions. The
  v1 `cmd()` invokable on `api.engraving` is the only sanctioned way to
  dispatch actions from a v2 extension.

---

## 1. Read

For the empirically-working baseline, see `Main.qml:401-497`. The walk reads
`api.engraving.curScore.scoreName/title/composer/lyricist/duration/keysig/`
`npages/nmeasures/nstaves/ntracks/hasHarmonies/harmonyCount/hasLyrics/`
`lyricCount/parts`; then iterates `firstMeasure → nextMeasure`,
`firstSegment → next`, calls `segment.elementAt(track)`, checks
`el.type === api.engraving.Element.CHORD`, walks `el.notes[]`, and reads
`.pitch / .tpc / el.duration.str / .tieBack`.

### Score-level

| Field | Path (Surface A) | Status | Cite |
| --- | --- | --- | --- |
| Score name (filename) | `curScore.scoreName` | OK | `src/engraving/api/v1/score.h:78` |
| Title (workTitle meta) | `curScore.title` | OK | `score.h:85`, `score.h:370` |
| Composer | `curScore.composer` | OK | `score.h:92`, `score.h:371` |
| Lyricist | `curScore.lyricist` | OK | `score.h:99`, `score.h:372` |
| Arbitrary meta tag | `curScore.metaTag(tag)` | OK | `score.h:379` |
| Duration (seconds) | `curScore.duration` | OK | `score.h:106`, `score.h:388` |
| MuseScore version of save | `curScore.mscoreVersion`, `mscoreRevision` | OK | `score.h:113`, `score.h:120` |
| Keysig at start (int, ±sharps) | `curScore.keysig` | OK | `score.h:135`, `score.h:393` |
| Page count | `curScore.npages` | OK | `score.h:142` |
| Page list | `curScore.pages` (since 4.6) | OK | `score.h:150` |
| Measure count | `curScore.nmeasures` | OK | `score.h:246` |
| Staff count | `curScore.nstaves` | OK | `score.h:173` |
| Staff list | `curScore.staves` | OK | `score.h:180` |
| Track count | `curScore.ntracks` | OK | `score.h:187` |
| System list | `curScore.systems` (since 4.6) | OK | `score.h:195` |
| Spanner list (all) | `curScore.spanners` (since 4.7) | OK | `score.h:203`, `score.cpp:580` |
| First / last measure | `curScore.firstMeasure`, `lastMeasure`, `firstMeasureMM`, `lastMeasureMM` | OK | `score.h:253-276` |
| Last segment | `curScore.lastSegment` | OK | `score.h:283` |
| Find measure at tick | `curScore.tick2measure(fraction)` | OK (4.6+) | `score.h:472` |
| First segment of type | `curScore.firstSegment(int segmentType)` | OK | `score.h:481` |
| Find segment at tick | `curScore.findSegmentAtTick(types, fraction)` | OK (4.6+) | `score.h:492` |
| Parts list | `curScore.parts` | OK | `score.h:166` |
| Excerpts (linked parts) | `curScore.excerpts` | OK | `score.h:360` |
| Selection | `curScore.selection` | OK | `score.h:353` |
| Style settings | `curScore.style` | OK | `score.h:127` |
| `hasHarmonies` / `harmonyCount` | `curScore.hasHarmonies / harmonyCount` | OK | `score.h:210-217` |
| `hasLyrics` / `lyricCount` | `curScore.hasLyrics / lyricCount` | OK | `score.h:221-231` |
| Lyrics list | `curScore.lyrics` (since 4.7) | OK | `score.h:239` |
| Extract all lyrics as string | `curScore.extractLyrics()` | OK | `score.h:453` |

### Parts / instruments / staves / voices

The `Part` class is at `src/engraving/api/v1/part.h:58`.

| Field | Path | Status | Cite |
| --- | --- | --- | --- |
| Part name | `part.partName` | OK | `part.h:107`, `Main.qml:431` |
| Long / short name | `part.longName / shortName` | OK | `part.h:97-101` |
| Long / short name at a tick | `part.longNameAtTick(f) / shortNameAtTick(f)` | OK (4.6+) | `part.h:168-172` |
| MusicXML sound ID | `part.musicXmlId` | OK | `part.h:76`, `Main.qml:435` |
| Internal instrument ID | `part.instrumentId` (since 4.6) | OK | `part.h:69`, `Main.qml:434` |
| Per-part track range | `part.startTrack`, `part.endTrack` | OK | `part.h:62-64` |
| Has chord-symbol staff | `part.hasChordSymbol` (since 4.6) | OK | `part.h:81` |
| Has drum / pitched / tab staff | `part.hasDrumStaff / hasPitchedStaff / hasTabStaff` | OK | `part.h:82-87` |
| Lyric count per part | `part.lyricCount` | OK | `part.h:89` |
| MIDI channel / program | `part.midiChannel / midiProgram` | OK | `part.h:91-93` |
| Visible | `part.show` (R/W since 3.6) | OK | `part.h:111` |
| Per-part instrument list | `part.instruments` | OK | `part.h:115` |
| Instrument at tick | `part.instrumentAtTick(tick)` | OK | `part.h:158-163` |
| Per-part staff list | `part.staves` (since 4.6) | OK | `part.h:119` |
| Master-score Part | `part.masterPart` (since 4.6) | OK | `part.h:122` |

`Staff` (`src/engraving/api/v1/elements.h:2300`):

| Field | Path | Status | Cite |
| --- | --- | --- | --- |
| Index | `staff.idx` (since 4.6) | OK | `elements.h:2348` |
| Visible | `staff.visible` (R/W), `staff.show` (R, combined) | OK | `elements.h:2352-2356` |
| Owning part | `staff.part` | OK | `elements.h:2344` |
| Per-voice playback enable | `staff.playbackVoice1..4` (R/W) | OK | `elements.h:2311-2317` |
| Clef at tick | `staff.clefType(fraction)` | OK | `elements.h:2400` |
| Time signature at tick | `staff.timeSig(fraction)` | OK | `elements.h:2409` |
| Key signature at tick | `staff.key(fraction)` | OK | `elements.h:2415` |
| Transposition at tick | `staff.transpose(fraction)` | OK | `elements.h:2421` |
| Swing at tick | `staff.swing(fraction)` | OK | `elements.h:2430` |
| Stemless at tick | `staff.stemless(fraction)` | OK | `elements.h:2443` |
| Is pitched / tab / drum at tick | `staff.isPitchedStaff/isTabStaff/isDrumStaff(f)` | OK | `elements.h:2452-2460` |
| Voice visibility | `staff.isVoiceVisible(voice)` | OK | `elements.h:2498` |
| Bracket list | `staff.brackets` | OK | `elements.h:2378` |

**Voices.** No first-class Voice object. Voices are addressed by `track =
staff * 4 + voice` (voice ∈ {0,1,2,3}). Empirically used at `Main.qml:461-462`.
The `Cursor` exposes both `track` and `voice` writable properties
(`cursor.h:70-77`).

`Instrument` (`src/engraving/api/v1/instrument.h:380` ff):

| Field | Path | Status | Cite |
| --- | --- | --- | --- |
| Internal id | `instrument.instrumentId` | OK | `instrument.h:380` |
| MusicXML sound id | `instrument.musicXmlId` | OK | `instrument.h:385` |
| Long / short name | `instrument.longName / shortName` | OK | `instrument.h:390-392` |
| String data | `instrument.stringData.strings`, `.frets` | OK | `instrument.h:180-183`, `396` |
| Drumset (if percussion) | `instrument.drumset` | OK | `instrument.h:401` |
| Channels | `instrument.channels` | OK | `instrument.h:404` |
| Per-channel name / harmony flag | `channel.name`, `channel.isHarmonyChannel` | OK | `instrument.h:81-84` |
| MIDI volume / pan / chorus / reverb | `channel.volume / pan / chorus / reverb` (R/W, **0–127, per-channel — NOT mixer audio dB**) | OK | `instrument.h:90-105` |
| Mute | `channel.mute` (R/W) | OK | `instrument.h:110` |
| Channel MIDI program / bank | `channel.midiProgram / midiBank` (R/W) | OK | `instrument.h:115-119` |

### Measures

`Measure : MeasureBase : EngravingItem` at `elements.h:2005` / `1901`.

| Field | Path | Status | Cite |
| --- | --- | --- | --- |
| 1-based measure number | `measure.measureNumber`, alias `measure.no` | OK | `elements.h:2048-2051`, `Main.qml:467` |
| Tick (Fraction) | `measure.tick`, `.ticks` (length) | OK | `elements.h:1916-1921` |
| Nominal time signature | `measure.timesigNominal` (R/W via Pid) | OK | `elements.h:2034` |
| Actual time signature / duration | `measure.timesigActual` (R/W via Pid) | OK | `elements.h:2036` |
| Repeat count | `measure.repeatCount` (R/W) | OK | `elements.h:2081` |
| Excluded from numbering / irregular | `measure.excludeFromNumbering`, `.irregular` (R/W) | OK | `elements.h:2062-2065` |
| Number-mode (auto / always / never) | `measure.measureNumberMode` (R/W) | OK | `elements.h:2070` |
| User stretch (spacing ratio) | `measure.userStretch` (R/W) | OK | `elements.h:2083` |
| Multimeasure rest start? | `measure.isMMRestStart`, `measure.mmRest` | OK | `elements.h:2088-2091` |
| Segments | `measure.segments` (since 4.6), `firstSegment`, `lastSegment` | OK | `elements.h:2026-2095` |
| Next / prev measure | `measure.nextMeasure`, `prevMeasure` (and MM variants) | OK | `elements.h:1928-1946`, `Main.qml:481` |
| Per-staff vspacers | `measure.vspacerUp(staffIdx) / vspacerDown(staffIdx)` | OK | `elements.h:2121-2125` |
| Per-staff measure number element | `measure.measureNumber(staffIdx)` | OK | `elements.h:2129` |
| MM range text | `measure.mmRangeText(staffIdx)` | OK | `elements.h:2133` |
| Corrupted / visible / stemless flags | `measure.corrupted/visible/stemless(staffIdx)` | OK | `elements.h:2137-2149` |
| Key signature at this measure | not directly — use `staff.key(measure.tick)` | PARTIAL | `elements.h:2415` |
| Tempo at this measure | no direct accessor; tempo is a `TempoText` annotation in a `Segment` — read by iterating `segment.annotations[]` and matching `subtypeName()` / `type` | PARTIAL | — |
| Barline type | reachable via `Segment.elementAt()` for the trailing `BarLine` segment and checking generic EngravingItem properties; no first-class `BarLine` API class | PARTIAL | `elements.h` (no `BarLine` subclass declared) |

### Segments

`Segment : EngravingItem` at `elements.h:1829`.

| Field | Path | Status | Cite |
| --- | --- | --- | --- |
| Tick (int) | `segment.tick` | OK | `elements.h:1862` |
| Fraction | `segment.fraction` | OK | `elements.h:1870` |
| Type bitmask | `segment.segmentType` (use `api.engraving.Segment.X`) | OK | `elements.h:1857` |
| Next / prev in measure or score | `segment.next`, `nextInMeasure`, `prev`, `prevInMeasure` | OK | `elements.h:1840-1852`, `Main.qml:479` |
| Element at a track | `segment.elementAt(track)` | OK | `elements.h:1894`, `Main.qml:462` |
| Annotations at this segment | `segment.annotations` — list of attached items like dynamics, tempo, rehearsal marks, chord symbols | OK | `elements.h:1836` |

### Notes / Rests / Chords

`Chord : ChordRest : DurationElement : EngravingItem` at `elements.h:1679` /
`1547` / `1509` / `148`. `Note : EngravingItem` at `elements.h:1359`.

| Field | Path | Status | Cite |
| --- | --- | --- | --- |
| Chord's notes | `chord.notes` | OK | `elements.h:1691`, `Main.qml:464` |
| Articulations on chord | `chord.articulations` | OK | `elements.h:1694` |
| Stem direction | `chord.up` (inherited from EngravingItem) | OK | `elements.h:284` |
| Beam | `chord.beam` | OK | `elements.h:1633` |
| Stem / hook / stemSlash | `chord.stem`, `chord.hook`, `chord.stemSlash` | OK | `elements.h:1696-1701` |
| Note type (NORMAL/ACCIACCATURA/etc.) | `chord.noteType`, `note.noteType` | OK | `elements.h:1704`, `1406` |
| Grace notes | `chord.graceNotes`, `graceNotesBefore`, `graceNotesAfter` | OK | `elements.h:1683-1689` |
| Top / bottom note | `chord.upNote / downNote` | OK | `elements.h:1721-1724` |
| Arpeggio | `chord.arpeggio` | OK | `elements.h:1727` |
| Tremolo (1- and 2-chord) | `chord.tremoloSingleChord / tremoloTwoChord` | OK | `elements.h:1733-1736` |
| MIDI pitch | `note.pitch` (R/W) | OK | `elements.h:1410`, `Main.qml:470` |
| Concert pitch class | `note.tpc1` (R/W) | OK | `elements.h:1413` |
| Transposing pitch class | `note.tpc2` (R/W) | OK | `elements.h:1416` |
| TPC for currently displayed | `note.tpc` (R/W) | OK | `elements.h:1420`, `Main.qml:471` |
| Velocity (user) | `note.userVelocity` (R/W) | OK | `elements.h:1427` |
| Velocity type | `note.veloType` (R/W) | OK | `elements.h:1425` |
| Tuning (cents) | `note.tuning` (R/W) | OK | `elements.h:1429` |
| Staff line | `note.line` (R/W) | OK | `elements.h:1432` |
| Fixed line / fixed | `note.fixed`, `note.fixedLine` (R/W) | OK | `elements.h:1435-1438` |
| TAB fret / string / dead | `note.fret`, `note.string`, `note.dead` (R/W) | OK | `elements.h:1441-1445` |
| Accidental | `note.accidental`, `note.accidentalType` (R/W) | OK | `elements.h:1362-1363` |
| Dot position | `note.dotPosition` | OK | `elements.h:1423` |
| Note dots list | `note.dots` | OK | `elements.h:1365` |
| Tie back / forward | `note.tieBack / tieForward` | OK | `elements.h:1392-1395`, `Main.qml:473` |
| First / last tied note | `note.firstTiedNote / lastTiedNote` | OK | `elements.h:1399-1403` |
| Attached spanners (forward / back) | `note.spannerForward / spannerBack` (since 4.6) | OK | `elements.h:1377-1380` |
| PlayEvents | `note.playEvents` | OK | `elements.h:1373` |
| Is trill cue note | `note.isTrillCueNote` | OK | `elements.h:1448` |
| Nominal duration | `chord.duration` (Fraction; R/W via `changeCRlen`) | OK | `elements.h:1517`, `Main.qml:472` |
| Global / actual duration | `chord.globalDuration`, `chord.actualDuration` | OK | `elements.h:1522-1527` |
| Tuplet (parent / top) | `chord.tuplet`, `chord.topTuplet` | OK | `elements.h:1531-1535` |
| Parent measure | `chord.measure` | OK | `elements.h:1539` |
| Lyrics attached to ChordRest | `chordRest.lyrics` | OK | `elements.h:1630` |
| Rest: is full-measure | `rest.isFullMeasureRest` | OK | `elements.h:1636` |

### Articulations, dynamics, slurs, ties, hairpins

- **Articulations:** reachable as items in `chord.articulations`
  (`elements.h:1694`). No dedicated `Articulation` wrapper class; treated as
  generic `EngravingItem` whose `subtypeName()` / SymId identifies the
  articulation type.
- **Dynamics:** **no `Dynamic` wrapper class.** Dynamics live as annotations
  on a `Segment` (`segment.annotations`, `elements.h:1836`), readable as
  generic `EngravingItem` with a `subtype` and the generic Pid `text`
  property. Writable via the `Pid::TEXT`-style API_PROPERTY macros on
  `EngravingItem`, but a more reliable insertion path is `cmd("add-dynamic")`
  (interactive popup) or constructing a Dynamic via `newElement(Element.DYNAMIC)`
  and inserting via the `Segment.add()`/`ChordRest.add()` path.
- **Slurs / Hairpins / Pedals / Ottavas / TextLine / Voltas:** all are
  `Spanner` subclasses in the engraving DOM, but the API only exposes a
  generic `Spanner` wrapper (`elements.h:2559`). Read via
  `curScore.spanners`. `Spanner` exposes
  `spannerTick`, `spannerTicks`, `spannerTrack2`, `anchor`, `startElement`,
  `endElement`, and `spannerSegments` (`elements.h:2563-2578`). The specific
  type (Hairpin vs Slur vs Ottava) must be distinguished via the inherited
  `subtype` / `subtypeName()`.
- **Ties:** dedicated `Tie : Spanner` wrapper
  (`elements.h:2609`), with `startNote`, `endNote`, `isInside`. Per-note
  access via `note.tieBack` / `note.tieForward`.

### Chord symbols / Harmony

`Harmony : EngravingItem` at `elements.h:2683` (since 4.7):

| Field | Path | Status | Cite |
| --- | --- | --- | --- |
| Plain text | `harmony.plainText` | OK | `elements.h:2687` |
| Display text (with formatting) | `harmony.displayText` | OK | `elements.h:2689` |
| Internal harmony name | `harmony.harmonyName` | OK | `elements.h:2691` |
| Score-wide harmony list | not via a direct property; iterate `score.spanners` is wrong (Harmony is not a spanner) — iterate measures' `segment.annotations` and filter by type | PARTIAL | — |
| Score-wide count flag | `score.hasHarmonies`, `score.harmonyCount` | OK | `score.h:210-217`, `Main.qml:419-420` |

`FretDiagram` (which can contain a `Harmony`) is at `elements.h:2720`.

### Lyrics

`Lyrics : EngravingItem` at `elements.h:2643` (since 4.7):

| Field | Path | Status | Cite |
| --- | --- | --- | --- |
| Plain text | `lyrics.plainText` | OK | `elements.h:2646` |
| Is melisma | `lyrics.isMelisma` | OK | `elements.h:2647` |
| Syllabic type (BEGIN/END/MIDDLE/SINGLE) | `lyrics.syllabic` (R/W) | OK | `elements.h:2652` |
| Lyric tick length | `lyrics.lyricTicks` (R/W) | OK | `elements.h:2654` |
| Separator (lyrics line) | `lyrics.separator` | OK | `elements.h:2648` |
| Verse number | not exposed as a Q_PROPERTY in the apiv1 wrapper; reachable via attaching to specific notes and walking by index | UNCERTAIN | — |
| Score-wide lyrics array | `curScore.lyrics` | OK | `score.h:239` |
| Extract everything | `curScore.extractLyrics()` | OK | `score.h:453` |

### Structural (rehearsal marks, voltas, section breaks, tempo changes)

- **Rehearsal marks:** annotations on Segments (no dedicated class).
  Read by iterating `segment.annotations` and filtering by
  `el.type === api.engraving.Element.REHEARSAL_MARK`. Write via
  `cmd("rehearsalmark-text")` (interactive) or `addText("REHEARSAL_MARK",
  text)` (`score.h:500`).
- **Voltas:** spanners; via `curScore.spanners` filtered by type.
- **Section breaks:** `LayoutBreak` items attached to a `MeasureBase`. Read
  via `measure.elements`; write via `cmd("section-break")` /
  `cmd("system-break")` / `cmd("page-break")` (`notationactioncontroller.cpp:268-272`).
- **Tempo changes:** `TempoText` annotations on Segments; read by walking
  `segment.annotations` and filtering. Write via `addText("TEMPO", "♩=120")`
  (`score.h:500`) or `cmd("tempo")` (`notationactioncontroller.cpp:396`).
- **Repeats:** `measure.repeatCount` exposed (R/W) (`elements.h:2081`).

### Selection state

`Selection` at `src/engraving/api/v1/selection.h:42`:

| Field | Path | Status | Cite |
| --- | --- | --- | --- |
| Selected elements list | `curScore.selection.elements` | OK | `selection.h:42` |
| Is range selection | `curScore.selection.isRange` | OK | `selection.h:47` |
| Range start / end segment | `curScore.selection.startSegment / endSegment` | OK | `selection.h:52-57` |
| Range start / end staff | `curScore.selection.startStaff / endStaff` | OK | `selection.h:62-67` |
| Programmatically select | `curScore.selection.select(item, add)` | OK | `selection.h:92` |
| Programmatically range-select | `curScore.selection.selectRange(startTick, endTick, startStaff, endStaff)` | OK | `selection.h:93` |
| Deselect element | `curScore.selection.deselect(item)` | OK | `selection.h:94` |
| Clear | `curScore.selection.clear()` | OK | `selection.h:95` |

### Excerpts (linked parts)

`curScore.excerpts` — list of `Excerpt`. Wrapper at
`src/engraving/api/v1/excerpt.h`. Read-only inventory.

### Cursor (read-side)

`Cursor` (`src/engraving/api/v1/cursor.h:66`) provides cursor-mode reads:
current `tick`/`utick`, `fraction`, `tempo`, `keySignature`, current
`element`/`segment`/`measure`, current `track`/`staffIdx`/`voice`/`staff`.
Get one via `curScore.newCursor()` (`score.h:737`).

Notes from `score_context_architecture.md` flag that cursor-based traversal
"behaves differently in Extensions 2.0" — the empirically-working `Main.qml`
uses measure/segment walks. The Cursor object itself IS exposed via
`api.engraving` on Surface A; what differs is some method behaviour, not
existence.

---

## 2. Write

### Direct property writes

Most of the engraving DOM's writable properties are exposed through the
`API_PROPERTY` / `API_PROPERTY_T` macros (`elements.h:88-126`). Setting one
calls `EngravingItem::set(Pid, QVariant)` which uses the internal `Pid`
property system. Each setter routes through the engraving undo machinery
ONLY when wrapped in a Score-level transaction (see Undo section below).

Confirmed writable from Surface A:
- `note.pitch`, `note.tpc`, `note.tpc1`, `note.tpc2`, `note.line`,
  `note.fret`, `note.string`, `note.userVelocity`, `note.tuning`,
  `note.accidentalType`, `note.veloType`, `note.dotPosition`, `note.dead`,
  `note.fixed`, `note.fixedLine` — `elements.h:1408-1448`.
- `chord.duration` (`changeCRlen`) — `elements.h:1517`.
- `measure.timesigActual`, `measure.timesigNominal`, `measure.repeatCount`,
  `measure.userStretch`, `measure.measureNumberMode`,
  `measure.measureNumberOffset`, `measure.excludeFromNumbering` — `elements.h:2034-2083`.
- `spanner.spannerTick`, `spanner.spannerTicks`, `spanner.spannerTrack2`,
  `spanner.anchor` — `elements.h:2563-2571`.
- `part.show` (visible/hidden) — `part.h:111`.
- `staff.visible`, `staff.cutaway`, `staff.playbackVoice1..4`,
  `staff.staffInvisible`, `staff.hideSystemBarLine`,
  `staff.mergeMatchingRests` etc. — `elements.h:2304-2371`.
- `channel.volume / pan / chorus / reverb / mute / midiProgram / midiBank` (per-instrument
  channel; **MIDI velocity, not audio mixer**) — `instrument.h:90-119`.
- `lyrics.syllabic`, `lyrics.lyricTicks` — `elements.h:2652-2654`.
- `curScore.scoreName`, `curScore.pageNumberOffset`, `curScore.layoutMode`,
  `curScore.showVerticalFrames`, `curScore.showInvisible`,
  `curScore.showUnprintable`, `curScore.showFrames`, `curScore.showPageborders`,
  `curScore.showSoundFlags`, `curScore.markIrregularMeasures`,
  `curScore.showInstrumentNames` — `score.h:78-346`.

### Element construction & insertion

- `api.engraving.newElement(type)` — creates a new wrapped `EngravingItem`
  for any of the `api.engraving.Element.*` enum types
  (`engravingapiv1.h:287`).
- `api.engraving.removeElement(item)` — `engravingapiv1.h:288`.
- `chord.add(item)` / `chord.remove(item)` —
  `elements.h:1772-1775`.
- `note.add(item)` / `note.remove(item)` —
  `elements.h:1499-1502`.
- `measureBase.add(item)` / `measureBase.remove(item)` — `elements.h:1988-1991`.
- `curScore.appendMeasures(n)` — `score.h:465`.
- `curScore.appendPart(instrumentId)` / `appendPartByMusicXmlId(...)` — `score.h:407-414`.
- `curScore.appendStaff(part)` / `appendLinkedStaff(srcStaff, dstPart)` (4.7+) — `score.h:663-674`.
- `curScore.insertPart(instrumentId, index)` (4.7+) — `score.h:710`.
- `curScore.replacePart(part, instrumentId)` (4.7+) — `score.h:721`.
- `curScore.replaceInstrument(part, instrumentId)` (4.7+) — `score.h:545`.
- `curScore.removeParts([])` / `removeStaves([])` (4.7+) — `score.h:600-608`.
- `curScore.moveParts(...)` / `moveStaves(...)` (4.7+) — `score.h:618-629`.
- `curScore.addText(textStyleType, text)` — `score.h:500`. (Use to insert
  title/composer/lyricist/rehearsal mark/tempo/staff text/expression/etc.)
- `curScore.setMetaTag(tag, value)` — `score.h:386`.
- `curScore.setScoreOrder(orderId)` (4.7+) — `score.h:730`.

### Cursor-based writes

`Cursor` (`src/engraving/api/v1/cursor.h:120-222`) supports:
- Position: `rewind(mode)`, `rewindToTick(tick)`,
  `rewindToFraction(f)`, `next()`, `nextMeasure()`, `prev()`, plus writable
  `track`, `staffIdx`, `voice`, `staff`, `score`, `filter`.
- Note entry: `addNote(pitch, addToChord)`, `addRest()`,
  `addTuplet(ratio, duration)`, `setDuration(z, n)`, `add(item)`.

### `cmd()` dispatch — inventory by category

`api.engraving.cmd(actionCode)` dispatches to MuseScore's action controller
system (`src/engraving/api/v1/qmlpluginapi.cpp:416-433`). The dispatcher
applies a small `COMPAT_CMD_MAP` for legacy short names (`escape`, `cut`,
`copy`, `paste`, `paste-half`, `paste-double`, `select-all`, `delete`,
`next-chord`, `prev-chord`, `prev-measure`) and otherwise passes through.

Action registrations are split across several controllers — counts measured:
- `src/notationscene/internal/notationactioncontroller.cpp` — 307 registerAction calls.
- `src/playback/internal/playbackcontroller.cpp` — ~20 dispatcher reg calls (PLAY/PAUSE/STOP/etc.).
- `src/project/internal/projectactionscontroller.cpp` — ~20 reg calls (file-open/save/export/print/etc.).
- `src/appshell/internal/applicationactioncontroller.cpp` — ~15 reg calls
  (quit, restart, fullscreen, preference-dialog, etc.).

Representative actions per category, all citation pattern
`src/notationscene/internal/notationactioncontroller.cpp:LINE` unless noted:

| Category | Sample codes | Source |
| --- | --- | --- |
| Note input mode | `note-input`, `note-input-by-note-name`, `note-input-by-duration`, `note-input-rhythm`, `note-input-repitch`, `note-input-realtime-auto`, `note-input-realtime-manual`, `note-input-timewise`, `realtime-advance` | `:95-104` |
| Duration pads | `note-longa`, `note-breve`, `pad-note-1`, `pad-note-2`, `pad-note-4`, `pad-note-8`, `pad-note-16`, `pad-note-32`, `pad-note-64`, `pad-note-128`, `pad-note-256`, `pad-note-512`, `pad-note-1024`, `double-duration`, `half-duration`, `inc-duration-dotted`, `dec-duration-dotted` | `:106-117, 224-227` |
| Pitch / accidentals | `pitch-up`, `pitch-down`, `pitch-up-octave`, `pitch-down-octave`, `pitch-up-diatonic`, `pitch-down-diatonic`, `flat2`, `flat`, `nat`, `sharp`, `sharp2`, `enh-current`, `enh-both`, `sharp-post` / `flat-post` (apply to selected accidental), `pitch-spell`, `pitch-spell-sharps`, `pitch-spell-flats`, `transpose-up`, `transpose-down`, `interval2..interval9` (chord intervals) | `:170-174, 212-215, 434-436, 464-465, 515-516, 531-535, 551` |
| Note insertion / removal | `put-note`, `remove-note`, `note-action`, `rest`, `extend-to-next-note`, `time-delete` | `:125, 176, 194-195, 429-430` |
| Articulations | `add-marcato`, `add-sforzato`, `add-tenuto`, `add-staccato`, `add-up-bow`, `add-down-bow` | `:178-181, 513-514` |
| Ornaments | `add-turn`, `add-turn-inverted`, `add-trill`, `add-short-trill`, `add-mordent`, `add-haydn`, `add-tremblement`, `add-prall-mordent`, `add-shake`, `add-shake-muffat`, `add-tremblement-couperin`, `add-turn-up`, `add-turn-inverted-up`, `add-turn-slash` | `:498-511` |
| Tuplets | `duplet`, `triplet`, `quadruplet`, `quintuplet`, `sextuplet`, `septuplet`, `octuplet`, `nonuplet`, `custom-tuplet`, `tuplet-dialog` | `:183-192` |
| Grace notes | `acciaccatura`, `appoggiatura`, `grace4`, `grace16`, `grace32`, `grace8after`, `grace16after`, `grace32after` | `:443-450` |
| Beam control | `beam-auto`, `beam-none`, `beam-break-left`, `beam-break-inner-8th`, `beam-break-inner-16th`, `beam-join`, `beam-selected-range`, `reset-beammode` | `:405, 452-458` |
| Dynamics / lines | `add-dynamic`, `add-hairpin`, `add-hairpin-reverse`, `add-8va`, `add-8vb`, `add-noteline` | `:337-343` |
| Slurs / ties | `tie`, `chord-tie`, `lv` (laissez-vibrer), `add-slur`, `hammer-on-pull-off` | `:240-244` |
| Text | `title-text`, `subtitle-text`, `composer-text`, `poet-text`, `part-text`, `frame-text`, `system-text`, `staff-text`, `expression-text`, `rehearsalmark-text`, `instrument-change-text`, `fingering-text`, `sticking-text`, `chord-text`, `roman-numeral-text`, `nashville-number-text`, `lyrics`, `tempo`, `figured-bass`, `add-lyric-verse`, `add-melisma`, `next-syllable`, `next-lyric-verse`, `prev-lyric-verse` | `:347-396, 161-168` |
| Auto-fill chord symbols | `add-chord-symbol-from-analysis`, `add-roman-numeral-from-analysis`, `add-nashville-number-from-analysis`, `add-chord-symbols-to-selection`, `add-roman-numerals-to-selection`, `add-nashville-numbers-to-selection`, `realize-chord-symbols` | `:363-384, 324` |
| Bends (guitar) | `standard-bend`, `pre-bend`, `grace-note-bend`, `slight-bend`, `dive`, `pre-dive`, `dip`, `scoop` | `:580-588` |
| Measure / frame ops | `insert-measure`, `insert-measures`, `insert-measures-after-selection`, `insert-measures-at-start-of-score`, `append-measure`, `append-measures`, `split-measure`, `join-measures`, `del-empty-measures`, `insert-hbox`, `insert-vbox`, `insert-textframe`, `insert-fretframe`, `append-hbox`, `append-vbox`, `append-textframe`, `append-fretframe` | `:282-311` |
| Voice ops | `voice-1`, `voice-2`, `voice-3`, `voice-4`, `voice-x12`, `voice-x13`, `voice-x14`, `voice-x23`, `voice-x24`, `voice-x34`, `voice-assignment-all-in-instrument`, `voice-assignment-all-in-staff` | `:330-335, 556-561` |
| Layout breaks / locks | `system-break`, `page-break`, `section-break`, `apply-system-lock`, `move-measure-to-prev-system`, `move-measure-to-next-system`, `toggle-system-lock`, `toggle-score-lock`, `make-into-system` | `:268-280` |
| Brackets | `add-brackets`, `add-parentheses`, `add-braces` | `:460-462` |
| Clef | `clef-violin`, `clef-bass` (the two registered shortcuts; broader clef setting is via palette/clef element insertion) | `:528-529` |
| Selection | `notation-select-all`, `notation-select-section`, `select-similar`, `select-similar-staff`, `select-similar-range`, `first-element`, `last-element`, `top-staff`, `empty-trailing-measure`, `notation-move-right`, `notation-move-left`, `notation-move-right-quickly`, `notation-move-left-quickly`, `up-chord`, `down-chord`, `top-chord`, `bottom-chord`, `select-dialog`, `next-segment-element`, `prev-segment-element`, `next-text-element`, `prev-text-element` | `:151-217, 249-266, 489-496` |
| Clipboard | `action://notation/copy`, `action://notation/cut`, `action://notation/paste`, `notation-paste-half`, `notation-paste-double`, `notation-paste-special`, `notation-swap`, `copy-lyrics-to-clipboard`, `action://copy`, `action://cut`, `action://paste`, `action://delete` | `:229-236, 442`, `applicationactioncontroller.cpp:78-84` |
| Undo / redo | `action://undo`, `action://redo` (global), `undo`, `redo` (notation alias resolved via `UNDO_ACTION_CODE`) | `:246-247`, `applicationactioncontroller.cpp:81-82` |
| View toggles | `show-invisible`, `show-unprintable`, `show-frames`, `show-pageborders`, `show-soundflags`, `show-irregular`, `concert-pitch` | `:409-416` |
| Style / dialogs | `edit-style`, `page-settings`, `staff-properties`, `edit-strings`, `measures-per-system`, `transpose`, `parts`, `staff-text-properties`, `system-text-properties`, `measure-properties`, `config-raster`, `realize-chord-symbols`, `add-fretboard-diagram`, `load-style`, `save-style`, `parts` | `:313-328` |
| Misc | `flip` (stem), `flip-horizontally`, `mirror-note`, `toggle-visible`, `toggle-mmrest`, `toggle-hide-empty`, `full-measure-rest`, `set-visible`, `unset-visible`, `toggle-autoplace`, `autoplace-enabled`, `reset`, `reset-stretch`, `reset-groupings`, `reset-shapes-and-position`, `reset-to-default-layout`, `reset-text-style-overrides`, `unroll-repeats`, `resequence-rehearsal-marks`, `slash-fill`, `slash-rhythm`, `explode`, `implode`, `implode-to-chord-track`, `add-image` | `:238-239, 264, 345, 403-407, 432-440, 519-525, 540-547` |
| Playback | `play`, `play-from-selection`, `pause`, `stop`, `rewind`, `loop`, `loop-in`, `loop-out`, `repeat`, `play-chord-symbols`, `pan`, `metronome`, `countin`, `midi-on`, `input-written-pitch`, `input-sounding-pitch`, `playback-setup`, `toggle-hear-playback-when-editing`, `playback-reload-cache` | `playbackcontroller.cpp:110-129` |
| File / project | `file-new`, `file-open`, `file-close`, `file-save`, `file-save-as`, `file-save-a-copy`, `file-save-selection`, `file-save-to-cloud`, `file-publish`, `file-share-audio`, `file-export`, `file-import-pdf`, `print`, `continue-last-session`, `project-properties`, `clear-recent` | `projectactionscontroller.cpp:67-101` |
| Application | `quit`, `restart`, `fullscreen`, `about-musescore`, `about-qt`, `about-musicxml`, `online-handbook`, `ask-help`, `accessibility-statement`, `preference-dialog`, `revert-factory`, `manage-plugins` | `applicationactioncontroller.cpp:51-78` |

### Undo stack

`Score::startCmd()` / `Score::endCmd(rollback)` are exposed as
`Q_INVOKABLE` on the apiv1 Score
(`src/engraving/api/v1/score.h:746-755`). Implementation at
`src/engraving/api/v1/score.cpp:591-622`. The pattern locks the undo stack so
all changes between `startCmd` and `endCmd` are bundled into a single
user-visible undo step, and ALSO so plugin-initiated `cmd()` dispatches
inside the bracket don't each commit independently.

- **Property writes via API_PROPERTY** go through
  `EngravingItem::set(Pid, value)` which uses the engraving undo system if a
  transaction is open.
- **Direct `add()` / `remove()` / `appendMeasures()`** require a `startCmd`
  / `endCmd` bracket (PluginAPI itself does this in `newScore` —
  `qmlpluginapi.cpp:412`). Without the bracket on the plugin side these can
  corrupt the score (warning in `score.h:740-745`).
- **`cmd()` dispatch:** each `cmd()` invocation goes through MuseScore's own
  action controllers which use their own `prepareChanges` / `commitChanges`
  inside their handlers. Therefore `cmd("flip")` is undoable on its own
  without an explicit plugin-side `startCmd`. If you want to bundle multiple
  `cmd()` calls into a single undo step, wrap them in
  `curScore.startCmd(name)` / `curScore.endCmd()` — `score.cpp:602-604`
  documents this is the intent.

**Write paths that bypass undo:** none observed for the apiv1 surface, but
the warning in `score.h:740-745` is explicit that direct DOM mutation
*without* `startCmd` / `endCmd` can crash or corrupt. The LLM tool layer
MUST wrap every mutating tool call (whether property-set or `cmd()`-based) in
a `startCmd(humanReadableName)` / `endCmd()` pair, both for safety and so
that the user sees a single LLM-attributed undo entry.

---

## 3. Playback

The `iplaybackcontroller.h` interface (`src/playback/iplaybackcontroller.h`)
is a C++ MODULE_CONTEXT_INTERFACE — there is no `Q_OBJECT` and **no
properties / invokables on this interface are exposed to QML**. There is no
`api.playback` analogue of `api.engraving`. All playback control from
extension QML must go through `cmd()` strings.

| Capability | Available via | Status |
| --- | --- | --- |
| Toggle play | `cmd("play")` — `playbackcontroller.cpp:110` | OK |
| Play from selection | `cmd("play-from-selection")` — `:111` | OK |
| Pause | `cmd("pause")` — `:112` | OK |
| Stop | `cmd("stop")` — `:114` | OK |
| Rewind to start | `cmd("rewind")` — `:115` | OK |
| Toggle loop | `cmd("loop")` — `:116` | OK |
| Set loop in / out | `cmd("loop-in")`, `cmd("loop-out")` — `:117-118` | OK |
| Toggle play-repeats | `cmd("repeat")` — `:119` | OK |
| Toggle play-chord-symbols | `cmd("play-chord-symbols")` — `:120` | OK |
| Toggle automatic pan | `cmd("pan")` — `:121` | OK |
| Toggle metronome | `cmd("metronome")` — `:122` | OK |
| Toggle count-in | `cmd("countin")` — `:123` | OK |
| Toggle MIDI input | `cmd("midi-on")` — `:124` | OK |
| Set MIDI input pitch type | `cmd("input-written-pitch")` / `cmd("input-sounding-pitch")` — `:125-126` | OK |
| Open playback setup dialog | `cmd("playback-setup")` — `:127` | OK |
| Seek to specific tick / beat / measure | `IPlaybackController::seekRawTick / seekBeat / seekElement` — C++ only, no `cmd()` registered | BLOCKED via extension QML |
| Query "is playing?" | `isPlaying()` / `isPlayingChanged()` on `IPlaybackController` — C++ only | BLOCKED via extension QML |
| Query current playback position | `currentPlaybackPositionChanged` channel — C++ only | BLOCKED via extension QML |
| Query current tempo | `currentTempo()` / `currentTempoChanged()` — C++ only | BLOCKED via extension QML |
| Set tempo multiplier (playback speed) | `setTempoMultiplier(d)` — C++ only | BLOCKED via extension QML |
| Total play time | `totalPlayTime()` — C++ only | BLOCKED via extension QML |

This is a real gap. Tools like "where is the play head right now?" and
"start playing from measure N" can't be implemented from the extension QML
scope without C++ work to add a `MuseApi.Playback`-style object to the v2
`ExtApi` (`extapi.h`). For now the LLM can only fire-and-forget the
transport-control `cmd()` strings.

Workaround for current playback position: read the cursor — `Cursor.tick`
and `Cursor.fraction` (`cursor.h:91-98`) and the score-level signal
`PluginAPI::scoreStateChanged` (`qmlpluginapi.h:512`) provide indirect
state. `scoreStateChanged` provides `selectionChanged`, `excerptsChanged`,
`instrumentsChanged`, `startLayoutTick`, `endLayoutTick`, `undoRedo` — but
NOT playback position. So this workaround does NOT answer "play head
position" questions.

---

## 4. Mixer and audio settings

Two distinct concepts must be kept separate.

### A. Per-channel MIDI parameters (channel-volume in 0..127)

These ARE exposed via the v1 plugin object model on `Channel`
(`instrument.h:81-119`): `volume`, `pan`, `chorus`, `reverb`, `mute`,
`midiProgram`, `midiBank`, all R/W. Reachable from Surface A via
`part.instruments[0].channels[0].volume = ...` inside a
`startCmd`/`endCmd` bracket. These are MIDI bytes (0–127), not real-time
audio mixer dB.

### B. The Mixer panel (per-instrument audio fader, pan, mute, solo, aux sends, FX)

Implemented in `src/playback/qml/MuseScore/Playback/`:
- `mixerpanelmodel.h` — `MixerPanelModel` (QAbstractListModel) with
  `Q_PROPERTY(int count)`, `Q_INVOKABLE QVariantMap get(int index)`, etc.
- `mixerchannelitem.h` — `MixerChannelItem` with `Q_PROPERTY` for
  `volumeLevel`, `balance`, `solo`, `muted`, `forceMute`,
  `leftChannelPressure`, `rightChannelPressure`, `inputResourceItem`
  (sound source), `outputResourceItemList`, `auxSendItemList`.

These are registered to the `MuseScore.Playback` QML module
(`src/playback/qml/MuseScore/Playback/CMakeLists.txt:24`).

Whether a v2 form extension can `import MuseScore.Playback` and instantiate
`MixerPanelModel` is **not confirmed** — the import validator does not
block the literal string `import MuseScore.Playback` (only `Muse.`), but the
QML module's `qmldir` must be on the v2 engine's import path and the type
must be registered globally rather than engine-specifically. **Empirical
testing required** to settle this. If it works, master volume, per-track
volume, pan, mute, solo, and aux sends become available. If it doesn't, the
audio mixer is not reachable from the extension QML scope at all.

### Master volume / master output / effects / aux

Master output and FX-chain APIs live behind `IPlaybackController` and the
audio module's `IAudioOutput` interface; neither is exposed to QML
extensions. Not reachable from Surface A.

| Capability | Path | Status |
| --- | --- | --- |
| Per-channel MIDI volume / pan / mute (engraving model, 0–127) | `part.instruments[i].channels[j].{volume,pan,mute}` | OK — `instrument.h:90-110` |
| Mixer audio volume per track | `MixerChannelItem.volumeLevel` — registered to `MuseScore.Playback` | UNCERTAIN — needs runtime test |
| Mixer mute / solo per track | `MixerChannelItem.muted / solo` | UNCERTAIN — needs runtime test |
| Mixer balance (audio pan) | `MixerChannelItem.balance` | UNCERTAIN — needs runtime test |
| Aux sends | `MixerChannelItem.auxSendItemList` | UNCERTAIN — needs runtime test |
| FX chain edit | `MuseScore.Playback` toolbar/panel models | UNCERTAIN — needs runtime test |
| Master volume | `IPlaybackController` (C++ only); also master-output via audio module | BLOCKED |

---

## 5. User / score settings, view state

### Score view toggles (R/W from Surface A)

All on `apiv1::Score`, `score.h:286-346`:

| Setting | Path | Cite |
| --- | --- | --- |
| Layout mode (page / continuous / horizontal / float) | `curScore.layoutMode` (use `api.engraving.LayoutMode.*`) | `score.h:290` |
| Show vertical frames | `curScore.showVerticalFrames` | `score.h:297` |
| Show invisible elements | `curScore.showInvisible` | `score.h:304` |
| Show formatting (unprintable) | `curScore.showUnprintable` | `score.h:311` |
| Show frames | `curScore.showFrames` | `score.h:318` |
| Show page borders | `curScore.showPageborders` | `score.h:325` |
| Show sound flags | `curScore.showSoundFlags` | `score.h:332` |
| Mark irregular measures | `curScore.markIrregularMeasures` | `score.h:339` |
| Show instrument names | `curScore.showInstrumentNames` | `score.h:346` |

Same toggles are also reachable via `cmd()`: `show-invisible`,
`show-unprintable`, `show-frames`, `show-pageborders`, `show-soundflags`,
`show-irregular` — `notationactioncontroller.cpp:409-414`.

### Concert pitch toggle

Via `cmd("concert-pitch")` — `notationactioncontroller.cpp:416`. No
property-style toggle exposed.

### Zoom

Not reachable as a direct property on `curScore`. Zoom is a `notationview`
concept. Action codes from the broader controllers (not surveyed
exhaustively) include `zoomin`, `zoomout`, `zoom100` — exact codes need
verification in `src/notation/internal/notationactioncontroller.cpp`
(distinct from the notationscene one).

### Transposition (global)

Via `cmd("transpose")` opens the Transpose dialog. Programmatic
transposition: `cmd("transpose-up")` / `cmd("transpose-down")` semitone steps
(`:515-516`); per-interval `cmd("interval2".."interval9")` (`:551`); diatonic
movement `cmd("pitch-up-diatonic")` / `pitch-down-diatonic` (`:493-494`);
diatonic alterations `cmd("pitch-up-diatonic-alterations")` /
`pitch-down-diatonic-alterations` (`:536-538`).

### Score-properties dialog values

`curScore.metaTag(tag)` and `setMetaTag(tag, value)`
(`score.h:379-386`). Standard tags: `workTitle`, `composer`, `lyricist`,
`copyright`, `arranger`, `subtitle`, `translator`, plus arbitrary user tags.

### Application preferences

Via `cmd("preference-dialog")` — opens the dialog. No programmatic per-setting
access from QML.

---

## Open questions / unknowns

1. **(Answered.)** `api.engraving.curScore` IS available on Surface A and
   returns the same `apiv1::Score *` as the classic plugin `curScore`. The
   ai-assistant has been using it successfully (`Main.qml:403`). The full v1
   object tree (Score / Part / Staff / Measure / Segment / Chord / Note /
   Harmony / Lyrics / Spanner / Cursor / Selection) is reachable. There is
   no API gap that would justify forcing the assistant to migrate to a
   `MuseScore { }` plugin sandbox.

2. **(Answered.)** A v2 form extension's QML CAN write `import MuseScore 3.0`
   — the validator only blocks `Muse.<...>` (note the dot)
   (`extensionbuilder.cpp:55-57`). The ai-assistant already exploits this for
   `Settings` (`Main.qml:177`). What is unverified is whether instantiating a
   nested `MuseScore { id: plugin; pluginType: "dock" }` element inside a v2
   form-extension QML *triggers the legacy v1 loader path* — the legacy path
   is gated on `manifest.apiversion == 1` and on `runPlugin()`/`onRun()`
   signals fired by the extension builder (`extensionbuilder.cpp:139-156`).
   The `MuseScore { }` element would instantiate but its `onRun` handler
   would never fire because the v2 loader doesn't call `runPlugin()`. So
   importing `MuseScore.Plugin` and putting down a `MuseScore { }` element
   inside the v2 form extension is **not equivalent** to running as a v1
   plugin. The reason this doesn't matter in practice is that `curScore` is
   reachable via `api.engraving.curScore` regardless of whether
   `onRun` fires.

3. **(Answered, with the same caveat as in CLAUDE.md.)** There IS a "v2"
   extension API in the sense that `muse/framework/extensions/api/extapi.h`
   exists alongside `v1/extapiv1.h`. The v2 `ExtApi` is a thinner, more
   sandboxed wrapper than the v1 `ExtApiV1` — it exposes `log`,
   `interactive`, `theme`, `engraving`, `converter`, `websocket`,
   `websocketserver`. The v2 surface intentionally omits `dispatcher`,
   `navigation`, `shortcuts`, `keyboard`, `accessibility`, `process`,
   `filesystem` (`extapi.h:46-56`). The "v2" surface is therefore narrower
   than the v1 surface in the dispatcher/shortcuts space, but it shares the
   `engraving` API via the same `EngravingApiV1` class
   (`extapi.h:41`, `engravingapiv1.h:42`). There is no separate `v2/` subdir
   under `muse/framework/extensions/api/` — `extapi.h` itself is the v2
   surface.

4. **(Answered.)** The v2 form extension's QML scope gets `api`
   (`ExtApi`), `ui` (UI engine — flagged as "should not be used directly"
   in `extensionsuiengine.cpp:57`), and `ioc_context`
   (`extensionsuiengine.cpp:51`) as context properties, plus globally
   registered enums (`:65-70`). It does NOT get `curScore` at root scope —
   that name belongs only to the `MuseScore { }` plugin element of the v1
   surface (`qmlpluginapi.h:133`). Surface A scripts must use
   `api.engraving.curScore`.

### Genuine remaining unknowns

A. **Mixer access from Surface A.** Can a v2 form extension actually
   `import MuseScore.Playback 1.0` and instantiate `MixerPanelModel`? The
   import validator does not block it (only `Muse.` is blocked); whether the
   v2 engine has the `MuseScore.Playback` qmldir on its import path is not
   verified from the source alone. Needs a quick runtime test in a
   throwaway extension.

B. **Playback position read-back.** There is no `cmd()` for reading the
   current play head tick, nor is there a QML-exposed playback-state
   property. Tools like "what is currently playing?" or "rewind to bar 17"
   cannot be implemented from extension QML today. Closing this gap requires
   either (a) extending `extapi.h` with a `MuseApi.Playback` property
   backed by `IPlaybackController`, or (b) adding new `cmd("seek-to-tick")`
   / `cmd("seek-to-measure")` actions. Both are C++ patches, not extension
   work.

C. **Subtype-based reads for spanners, dynamics, tempo, time-sig, key-sig,
   barlines.** None of these have dedicated apiv1 wrapper classes (only
   `Spanner` for the line family). Reads must rely on the generic
   `subtype` / `subtypeName()` strings and the `Pid::*` property system,
   neither of which is documented as a stable schema. The tool surface
   should map a small enum-like vocabulary onto these subtype strings and
   accept that the mapping may drift between MuseScore versions.

D. **Lyrics verse number.** `lyrics.plainText`, `.syllabic`, `.isMelisma`,
   `.lyricTicks` are exposed, but the verse index (0 for first verse, 1 for
   second, ...) is not a Q_PROPERTY on `apiv1::Lyrics`. Reachable in C++
   on `mu::engraving::Lyrics::no()` but not surfaced. Needs either DOM-side
   exposure or computed inference (count lyrics per ChordRest in order).

E. **Tempo programmatic write.** Inserting a tempo marking is reachable via
   `cmd("tempo")` (interactive popup) or `curScore.addText("TEMPO",
   "♩=120")`; setting the BPM of an existing tempo marking requires accessing
   the underlying `TempoText` annotation via `segment.annotations` and using
   the generic Pid system (`Pid::TEMPO`, `Pid::TEXT`). Not tested
   end-to-end.

F. **MIDI bytes vs audio dB.** The `Channel.volume` field is MIDI 0..127,
   not audio dB. If the LLM is asked "set the cello to forte" the right
   tool target is probably to insert a `Dynamic` (`cmd("add-dynamic")` with
   a follow-up subtype choice, or constructing one programmatically) rather
   than to nudge MIDI channel volume. Worth documenting explicitly in the
   tool schemas.
