# Runtime Probe + Architecture Investigation

_Investigation date: 2026-05-16. Companion documents:
[api_write.md](api_write.md) (proposed write tools),
[write_api_probe.md](write_api_probe.md) (source-only findings)._

This document collects findings from two investigations:

- **Part A** — Source-only investigation into how to structure the extension
  code so the MuseScore-layer functions, tool-schema definitions, and the
  dispatch layer can live in separate files for maintainability.
- **Part B** — Runtime probes that exercise the open `❓` questions from
  `write_api_probe.md` against a live score, to confirm enum surfaces,
  Pid values, and that `cursor.add()` renders positional annotations
  correctly.

---

# Part A — File-structure findings (source-only)

## A1 — Local JavaScript imports work

**Finding:** Local `.js` files placed alongside `Main.qml` in the extension
directory **are importable** via the standard QML `import "FileName.js" as Lib`
syntax. No `addImportPath()` is required on the engine, no manifest
declaration is needed.

**Why this works:**

1. The v2 form-extension loader at
   [extensionbuilder.cpp:91](C:/s/MS/muse/framework/extensions/qml/Muse/Extensions/extensionbuilder.cpp#L91)
   constructs a `QQmlComponent` from `a.path.toQString()`, where `a.path` is
   the resolved absolute path to `Main.qml`
   ([extensionsloader.cpp:212](C:/s/MS/muse/framework/extensions/internal/extensionsloader.cpp#L212):
   `a.path = rootDirPath + "/" + a.path;`).

2. Qt's QML engine resolves all relative imports — both `.js` and local `.qml`
   files — against the URL of the file currently being loaded. This is the
   QML engine's "implicit directory import" behaviour, and it does NOT depend
   on `addImportPath()`. `addImportPath()` only affects **module** lookups
   (`import Muse.Foo 1.0`-style), not local-file imports.

3. The v2 engine setup at
   [extensionsuiengine.cpp:44-71](C:/s/MS/muse/framework/extensions/internal/extensionsuiengine.cpp#L44-L71)
   adds no extra import paths (unlike the v1 path at line 123 which adds
   `:/qml` for legacy modules). It only sets the `ioc_context`, `ui`, `api`,
   and global enum properties. Nothing in this setup prevents local imports.

4. The `validateImports()` function at
   [extensionbuilder.cpp:42-60](C:/s/MS/muse/framework/extensions/qml/Muse/Extensions/extensionbuilder.cpp#L42-L60)
   **only scans `Main.qml` itself** (the file at `a.path`), line by line,
   rejecting any line that starts with `import` and contains `Muse.`. It does
   not recurse into other QML files or `.js` files. A local file's contents
   are never validated. (Conversely, this means a side-loaded `.qml` file
   could still bypass the Muse-import check, but that's an orthogonal
   concern — for our purposes, local `.js`/`.qml` imports go through cleanly.)

**Verdict:** ✅ `import "ScoreTools.js" as ScoreTools` from `Main.qml` works.

## A2 — Local QML component imports work

Same mechanism as A1. There are two usable QML import patterns:

- **Same-directory components** (`MyComponent.qml` in the same dir as
  `Main.qml`): no `import` statement at all is needed. QML implicit type
  resolution from the containing directory means `MyComponent { … }` is
  directly usable. This is the simplest layout.

- **Namespaced subdirectories**: `import "components" as Comp` lets you
  organise QML components under a subdirectory and reference them as
  `Comp.MyComponent { … }`.

**Verdict:** ✅ Both patterns work; same-directory is simplest.

## A3 — Manifest implications

The manifest schema is parsed by
[extensionsloader.cpp:108-203](C:/s/MS/muse/framework/extensions/internal/extensionsloader.cpp#L108-L203).
Each `actions[].path` field is a **single** QML/JS file path resolved
relative to the manifest directory. There is no `additionalFiles`,
`resources`, or `include` array in the schema.

The extension installer at
[extensioninstaller.cpp:88-115](C:/s/MS/muse/framework/extensions/internal/extensioninstaller.cpp#L88-L115)
**unzips the entire archive** into the extension directory. Whatever files
are in the zip end up in the user's extension directory; the manifest does
not need to declare them. Uninstall removes the whole directory.

**Verdict:** ✅ No manifest changes needed. Companion `.js` / `.qml` files
ship alongside `Main.qml` in the extension folder, declared nowhere.

## A4 — Proposed file structure

Given that local `.js` and `.qml` imports work, the recommended layout
keeps the MuseScore-facing code in plain `.js` files that a MuseScore
developer can read without LLM context:

```
ai-assistant/
  Main.qml              — UI layer only (chat, settings, score-context chip)
                          imports the modules below, contains zero LLM code
                          and zero score-mutation code
  ScoreReader.js        — MuseScore READ functions (curScore traversal,
                          notes/measures/parts queries, score metadata)
  ScoreWriter.js        — MuseScore WRITE functions (add_dynamic, add_harmony,
                          add_rehearsal_mark, … — each wrapped in startCmd/
                          endCmd, one-call-per-tool)
  PlaybackTools.js      — Playback control (play, pause, seek, loop)
  ToolSchemas.js        — JSON schema array describing the tool surface to
                          the LLM API; one entry per ScoreReader/ScoreWriter/
                          PlaybackTools function
  ToolDispatch.js       — Single function: dispatch(name, args) → fn(args)
                          maps LLM tool-call name to the right module function
  LlmClient.js          — HTTP client for Anthropic / OpenAI / Gemini
                          (already present, just extracted from Main.qml)
  manifest.json         — unchanged; declares only Main.qml
```

`Main.qml` imports each module:

```qml
import "ScoreReader.js"   as ScoreReader
import "ScoreWriter.js"   as ScoreWriter
import "PlaybackTools.js" as PlaybackTools
import "ToolSchemas.js"   as ToolSchemas
import "ToolDispatch.js"  as ToolDispatch
import "LlmClient.js"     as LlmClient
```

### Authorship boundary the layout enforces

- A MuseScore developer who opens `ScoreReader.js` / `ScoreWriter.js` sees
  **only** MuseScore API calls (`api.engraving.curScore`, `cursor.add()`,
  `newElement(...)`, `startCmd/endCmd`). No mention of tools, schemas, LLMs,
  JSON-RPC, or dispatch. They can review for correctness as plain MuseScore
  plugin code.

- A developer working on LLM integration opens `ToolSchemas.js` /
  `ToolDispatch.js` / `LlmClient.js`. None of these touch `curScore`
  directly — they only call into `ScoreReader.ScoreWriter.PlaybackTools`
  by name.

- `Main.qml` orchestrates: receive LLM response → `ToolDispatch.dispatch(
  toolCall.name, toolCall.input)` → render result in chat.

### Trade-offs and notes

- **Single-file deploy is no longer enough.** Manual deployment (copy
  `Main.qml` to `extensions/ai-assistant/`) becomes a 7-file copy. The
  zip-install path handles this automatically once the next release zip
  is built, but manual iterative development needs a deploy script.
  Suggested: a `tools/deploy_extension.sh` (or `.ps1`) that rsyncs the
  `ai-assistant/` source dir to the installed extension dir.

- **Imports are eager**: every `.js` file declared in a QML `import` is
  evaluated at load time. With six small modules this is negligible, but
  the convention is worth noting.

- **`.js` imports are shared by default.** QML's `.js` import gives all
  importers the same module instance (i.e. module-scoped state is shared
  across all callers). Each of our modules above is intended to be a
  namespace of pure functions with no module-scope state, so this is fine.
  If we need per-call state (e.g. a conversation cache), keep it in
  `Main.qml`'s root properties and pass it in explicitly.

- **Component QML files (`MyComponent.qml`)** would be useful only if the
  UI grew enough to warrant a Settings panel as a separate component. For
  now the chat UI is monolithic enough that splitting `Main.qml`'s UI
  itself isn't a near-term priority — the win is moving the **logic** out.

### Migration path (incremental, not a big-bang rewrite)

1. Extract `ScoreReader.js` first (already-stable `refreshScoreContext`
   and note-walking code). Update `Main.qml` to call
   `ScoreReader.refreshScoreContext(root)`.
2. Add `ScoreWriter.js` with the first concrete write tool **after** the
   Pid-exposure blocker (see Part B) is resolved.
3. Extract `ToolSchemas.js` and `ToolDispatch.js` together once there are
   ≥ 3 write tools — the dispatch indirection earns its keep around then.
4. `LlmClient.js` extraction last, since the chat plumbing is the most
   intertwined with the UI.

---

# Part B — Runtime probe results

> _Probe code is implemented in `Main.qml` as `runRuntimeProbes()`, triggered
> by the 🔬 button in the score-context chip row. All mutations are
> `startCmd`/`endCmd`-wrapped — six Ctrl+Z presses fully revert the probe.
> The probe is marked "temporary; remove after probe milestone" in the source
> for easy cleanup._
>
> _Probe ran 2026-05-16 against "forever curious" (6 measures, 7 staves)._

## Headline finding — BLOCKING

**`api.engraving.Pid` is undefined in v2 extension scope.** This kills the
proposed `set(Pid.X, value)` write path for all six text/harmony/dynamic/tempo
tools. Verified empirically (probe output: `api.engraving.Pid present: NO`)
and confirmed in source: the `EngravingApiV1` class
([engravingapiv1.h:55-159](C:/s/MS/src/engraving/api/v1/engravingapiv1.h#L55-L159))
exposes ~100 enums as `Q_PROPERTY(QJSValue Name READ getName CONSTANT)`, but
`Pid` is not among them. The underlying `mu::engraving::Pid` is a plain
`enum class : short` ([property.h:71](C:/s/MS/src/engraving/dom/property.h#L71))
that is **not** `Q_ENUM_NS`-registered anywhere in `apitypes.h`.

The `cursor.add()` insertion path itself **works** (confirmed by the
RehearsalMark visibly appearing in the score, just with no text), so the
plumbing is correct — the missing piece is purely the property-set surface.

## Probe 1 — `api.engraving.Pid.*` accessibility

**Result:** ❌ Pid not exposed.

```
api.engraving present: YES
api.engraving.Pid present: NO
```

All 13 individual `Pid.X` queries returned undefined (because `Pid` itself
is undefined, the dotted property lookup short-circuits and the probe
correctly skipped the inner enumeration).

**Implication:** Status flipped from 🔴 Blocking ❓ → ❌ Confirmed blocked.

**Resolution paths** (in increasing implementation cost):

1. **C++ patch — recommended.** Add a single property to `EngravingApiV1`
   that exposes `Pid` as a frozen JSValue, analogous to how `Element` is
   exposed at line 56 (`ENUM_PROPERTY(Element, enums::ElementType)`). Two
   sub-options:
   - **(a) Q_ENUM_NS the enum.** Add `enum class Pid { … }` mirroring
     `mu::engraving::Pid`'s values into `mu::engraving::apiv1::enums`
     (apitypes.h, with `Q_ENUM_NS(Pid)`). Then a one-line
     `ENUM_PROPERTY(Pid, enums::Pid)` in engravingapiv1.h gives us the
     normal pattern. Cost: ~500 enum values to mirror; copy-pasteable
     but verbose.
   - **(b) Build an Enum object at runtime.** Use Qt's reflection to
     enumerate `mu::engraving::Pid` if it were made `Q_ENUM`, or write
     a single helper that produces a JS object literal from a hardcoded
     table. Smaller patch; loses the type-safety benefit of (a).

2. **Raw-integer fallback — fragile.** Maintain a JS lookup table:
   `const PID_TEXT = 87; const PID_HARMONY_NAME = ...;` and call
   `h.set(PID_TEXT, "Cmaj7")`. The integer values come directly from
   `property.h`'s enum order. Risk: if upstream MuseScore reorders the
   enum (a non-ABI-stable thing), the extension breaks silently with
   no error — values just go to the wrong property.

3. **Channel through `cmd()` actions where possible.** For rehearsal
   marks and tempo marks there may be action handlers we can drive via
   selection + `cmd()`. Worth surveying but not a complete substitute —
   the action handlers all open interactive popups for the parameter
   (the same reason `cmd("add-dynamic")` is unusable in our setting).

**Recommendation:** Path 1(a). The patch is small, type-safe, mirrors the
existing pattern, and removes the only architectural blocker for the
write-tool surface. Should be done before any write tool is exposed.

## Probe 2 — `api.engraving.Element.*` enum spellings

**Result:** ✅ All 15 element types resolve to integer values:

| Element type        | Integer value |
|---------------------|---------------|
| `REHEARSAL_MARK`    | 60            |
| `TEMPO_TEXT`        | 51            |
| `STAFF_TEXT`        | 52            |
| `SYSTEM_TEXT`       | 53            |
| `DYNAMIC`           | 41            |
| `HARMONY`           | 64            |
| `LYRICS`            | 44            |
| `VOLTA`             | 68            |
| `OTTAVA`            | 102           |
| `PEDAL`             | 103           |
| `CHORD`             | 122           |
| `NOTE`              | 23            |
| `REST`              | 28            |
| `HAIRPIN`           | 101           |
| `SLUR`              | 123           |

All proposed enum names are correct (TEMPO_TEXT, not TEMPO; STAFF_TEXT,
not STAFF). The integer form (not string) is what `newElement()` accepts:
`api.engraving.newElement(api.engraving.Element.REHEARSAL_MARK)` is
equivalent to `api.engraving.newElement(60)`.

**Note:** values are integers despite the v2-engine convention of string
enums — this is because `EngravingApiV1` is the v1 class re-served as the
v2 backend ([engravingmodule.cpp:141](C:/s/MS/src/engraving/engravingmodule.cpp#L141)),
and `makeEnum<T>()` picks the integer form when the underlying engine
reports `apiversion == 1` ([engravingapiv1.h:343-351](C:/s/MS/src/engraving/api/v1/engravingapiv1.h#L343-L351)).
In practice this means **always pass enum values where an int is expected**
— don't try the string form even though v2 enum surfaces sometimes give
strings.

## Probe 3 — `cursor.add()` for positional annotations

**Result:** ⚠️ Plumbing works, but text-setting depends on Pid (see Probe 1).

- `cursor.add(rehearsalMark)` — element **does** appear in the score
  (visually confirmed: empty rehearsal-mark box at top-left of measure 1).
  The `m1.firstSegment.annotations.length = 0` read-back from the probe
  was misleading — `firstSegment` in measure 1 is the keysig/clef segment,
  not the ChordRest segment the mark attaches to. To enumerate annotations
  reliably, walk all segments in the measure and filter by `segmentType`.
- `cursor.add(staffText)` — `endCmd` returned OK. Not visually confirmed
  (without text the element renders empty/invisible if at all).
- `cursor.add(harmony)` — `endCmd` returned OK; `plainText`/`harmonyName`
  read back as undefined (no text was set because `Pid.HARMONY_NAME`
  unavailable).
- `cursor.add(dynamic)` — `endCmd` returned OK. `subtype` read back as
  `0` (= `DynamicType.OTHER`, the default), as no DYNAMIC_TYPE was set.
- `cursor.add(tempoText)` — `endCmd` returned OK; no Pid available to
  set text, BPM, or follow-text.

**Implication:** The `cursor.add()` default-branch path is correct for
all six annotation types (the elements are inserted without exceptions).
The blocker is purely Probe 1 — once `Pid.TEXT` and friends are exposed,
these tools become directly usable as designed.

**Read-back gotcha to document for future probes:** when verifying
annotation insertion, do NOT check `measure.firstSegment.annotations` —
walk all segments in the measure and union their annotations, or filter
for `segmentType == ChordRest` first.

## Probe 4 — Harmony Pid path and chord-symbol parsing

**Result:** ❌ Cannot test without Pid.

- Probe 4a (`set(Pid.HARMONY_NAME, "Cmaj7")`) — `Pid.HARMONY_NAME`
  unavailable; the call was skipped. `harmonyName` read-back undefined.
- Probe 4b (`set(Pid.TEXT, "Fm")`) — `Pid.TEXT` unavailable; same.

**Open question (deferred until Pid is exposed):** which Pid is the
correct write path for Harmony — `Pid.TEXT` (inherited from TextBase) or
a Harmony-specific Pid like `HARMONY_TYPE` plus the text? The C++
`Harmony::setHarmony(String)` triggers parsing; setting `Pid.TEXT` may
or may not invoke the parser. Worth re-probing once Pid is accessible.

**Note on Pid naming:** the source has no `Pid.HARMONY_NAME` — the actual
Harmony-related Pids in
[property.h](C:/s/MS/src/engraving/dom/property.h) are
`HARMONY_TYPE` (~line 448), `HARMONY_VOICE_LITERAL`, `HARMONY_VOICING`,
`HARMONY_DURATION`, `HARMONY_BASS_SCALE`, `HARMONY_DO_NOT_STACK_MODIFIERS`.
The text itself appears to use the inherited `Pid::TEXT` (line 165).
`api_write.md` should be corrected to refer to `Pid.TEXT` for the harmony
text path, not the non-existent `Pid.HARMONY_NAME`.

## Probe 5 — Dynamic enum values and rendering

**Result:** ✅ Full enum table recovered; rendering blocked by Pid.

`api.engraving.DynamicType` returns a complete enum object:

| Name      | Value | Name      | Value | Name      | Value |
|-----------|-------|-----------|-------|-----------|-------|
| `OTHER`   | 0     | `FF`      | 10    | `RFZ`     | 25    |
| `PPPPPP`  | 1     | `FFF`     | 11    | `RF`      | 26    |
| `PPPPP`   | 2     | `FFFF`    | 12    | `FZ`      | 27    |
| `PPPP`    | 3     | `FFFFF`   | 13    | `M`       | 28    |
| `PPP`     | 4     | `FFFFFF`  | 14    | `R`       | 29    |
| `PP`      | 5     | `FP`      | 15    | `S`       | 30    |
| `P`       | 6     | `PF`      | 16    | `Z`       | 31    |
| `MP`      | 7     | `SF`      | 17    | `N`       | 32    |
| `MF`      | 8     | `SFZ`     | 18    | `LAST`    | 33    |
| `F`       | 9     | `SFF`     | 19    |           |       |
|           |       | `SFFZ`    | 20    |           |       |
|           |       | `SFFF`    | 21    |           |       |
|           |       | `SFFFZ`   | 22    |           |       |
|           |       | `SFP`     | 23    |           |       |
|           |       | `SFPP`    | 24    |           |       |

This is the lookup table the `add_dynamic` tool needs. Tool-layer
mapping for the canonical Dynamic vocabulary in `infomodel_score.md`:

| Tool string | DynamicType  | Integer |
|-------------|--------------|---------|
| `"ppp"`     | `PPP`        | 4       |
| `"pp"`      | `PP`         | 5       |
| `"p"`       | `P`          | 6       |
| `"mp"`      | `MP`         | 7       |
| `"mf"`      | `MF`         | 8       |
| `"f"`       | `F`          | 9       |
| `"ff"`      | `FF`         | 10      |
| `"fff"`     | `FFF`        | 11      |
| `"fp"`      | `FP`         | 15      |
| `"sf"`      | `SF`         | 17      |
| `"sfz"`     | `SFZ`        | 18      |
| `"sff"`     | `SFF`        | 19      |
| `"sffz"`    | `SFFZ`       | 20      |
| `"sfp"`     | `SFP`        | 23      |
| `"rfz"`     | `RFZ`        | 25      |
| `"fz"`      | `FZ`         | 27      |

Note `FP` is in the FP slot (15), `PF` (16) is the rare reverse, not the
common `fp`. The vocabulary covers all standard dynamic symbols MuseScore
ships in its dynamics palette.

Whether `MF` (value 8) actually renders correctly was not visually
verified — the `cursor.add(dynamic)` was called but the dynamic was
added with subtype 0 (OTHER) because `Pid.DYNAMIC_TYPE` was unavailable
to set. Re-verify once Pid is exposed.

## Probe 6 — TempoText: programmatic BPM drives playback

**Result:** ❌ Cannot test without Pid.

```
Pid.TEXT             present: undefined
Pid.TEMPO            present: undefined
Pid.TEMPO_FOLLOW_TEXT present: undefined
```

All three Pids returned undefined (because `Pid` itself is undefined).
The `cursor.add(tempoText)` call returned, but the tempo text has no
text, no BPM, no follow-text setting — it's a blank shell. Whether
playback would honor a programmatically-set BPM remains untestable.

The Pid integer values from
[property.h](C:/s/MS/src/engraving/dom/property.h) (computed by counting
from line 71 with no gaps in the unbroken declaration):
- `TEXT` ≈ 87
- `TEMPO` ≈ 97
- `TEMPO_FOLLOW_TEXT` ≈ 98

(These would be exact only if the enum has no skipped values up to that
point — verify post-patch by enumerating `Pid` from QML once exposed.)

## Probe 7 — Enum surfaces for LyricsSyllabic / DynamicType / OttavaType

**Result:** ✅/⚠️ — values are accessible, but some via unconventional paths.

| Probed accessor                  | Result |
|----------------------------------|--------|
| `api.engraving.DynamicType`      | ✅ object (full table, see Probe 5) |
| `api.engraving.OttavaType`       | ✅ `{OTTAVA_8VA:0, OTTAVA_8VB:1, OTTAVA_15MA:2, OTTAVA_15MB:3, OTTAVA_22MA:4, OTTAVA_22MB:5}` |
| `api.engraving.HairpinType`      | ✅ `{CRESC_HAIRPIN:0, DECRESC_HAIRPIN:1, DIM_HAIRPIN:1, CRESC_LINE:2, DIM_LINE:3, DECRESC_LINE:3, INVALID:-1}` |
| `api.engraving.DynamicSpeed`     | ✅ `{SLOW:0, NORMAL:1, FAST:2}` |
| `api.engraving.HarmonyType`      | ✅ `{STANDARD:0, ROMAN:1, NASHVILLE:2}` |
| `api.engraving.LyricsSyllabic`   | ❌ undefined |
| `api.engraving.TextStyleType`    | ❌ undefined |
| `api.engraving.VoltaType`        | ❌ undefined |
| `api.engraving.Lyrics` (alt)     | ✅ `{BEGIN:1, END:2, MIDDLE:3, SINGLE:0}` — this is the Syllabic enum exposed via the `Lyrics` property name in `EngravingApiV1` |
| `api.engraving.Dynamic` (alt)    | ❌ undefined |
| `api.engraving.Ottava` (alt)     | ❌ undefined |

**Notable findings:**

- `LyricsSyllabic` is exposed under the name **`Lyrics`** (line 94 of
  `engravingapiv1.h`: `Q_PROPERTY(apiv1::Enum * Lyrics READ lyricsSyllabicEnum CONSTANT)`),
  not `LyricsSyllabic`. Tools must read it as `api.engraving.Lyrics.BEGIN`
  etc.

- **Ottava 15ma/15mb ARE available** in the OttavaType enum (values 2
  and 3). `api_write.md` claimed they were "deferred" — that was based
  on the absence of `cmd("add-15ma")`, not the enum. With Pid exposed,
  `add_ottava` for 15ma/15mb becomes implementable via direct construction
  + `cursor.add()`, sidestepping the cmd() limitation entirely (and
  sidestepping the spanner-insertion problem since OTTAVA appears to
  insert correctly — to be probe-verified).

- `HairpinType` has unusual aliasing — `DECRESC_HAIRPIN` and
  `DIM_HAIRPIN` are both 1; `DECRESC_LINE` and `DIM_LINE` are both 3.
  Tool layer can normalise on either name.

- `TextStyleType` undefined is interesting — it IS declared as
  `ENUM_PROPERTY(TextStyleType, enums::TextStyleType)` at
  [engravingapiv1.h:57](C:/s/MS/src/engraving/api/v1/engravingapiv1.h#L57),
  but the v2 surface doesn't return it. This may be a v2-engine
  registration quirk; not currently blocking since `addText()` is broken
  for positional annotations anyway (per write_api_probe.md §6).

- `VoltaType` undefined matches the deferred status — `add_volta` was
  already blocked by spanner insertion regardless.

---

# Summary of revised `api_write.md` status

| Probe item | Prior status | Post-probe status | Note |
|---|---|---|---|
| `api.engraving.Pid.*` accessible | 🔴 Blocking ❓ | ❌ **Confirmed blocked** | Requires C++ patch (recommended: `ENUM_PROPERTY(Pid, enums::Pid)` in engravingapiv1.h) |
| `Element.X` enum spellings | 🔴 Blocking ❓ | ✅ **Confirmed** | Full integer table in Probe 2; all 15 element types resolve |
| `cursor.add()` for positional annotations | 🔴 Blocking ❓ | ✅ **Confirmed working** | RehearsalMark visibly inserted; readback via `firstSegment.annotations` was the wrong segment, not a real failure |
| Harmony `Pid.HARMONY_NAME` parsing | 🟠 High ❓ | ❌ **Untested + naming wrong** | No `Pid.HARMONY_NAME` exists in source; use `Pid.TEXT` once Pid is exposed |
| Dynamic `Pid.DYNAMIC_TYPE` integer map | 🟠 High ❓ | ⚠️ **Map captured, render unverified** | Full DynamicType table in Probe 5; rendering blocked on Pid |
| TempoText programmatic BPM | 🟠 High ❓ | ❌ **Untestable without Pid** | Pids `TEMPO` (~97), `TEMPO_FOLLOW_TEXT` (~98), `TEXT` (~87) exist in C++ but inaccessible from QML |
| `LyricsSyllabic`/`DynamicType`/`OttavaType` enum surfaces | 🟡 Medium ❓ | ⚠️ **Partial** | DynamicType, OttavaType, HairpinType, HarmonyType, DynamicSpeed: ✅. LyricsSyllabic via `api.engraving.Lyrics`: ✅. TextStyleType, VoltaType: ❌ |

# Recommended next steps

_(Superseded by Probe Round 2 — see below. Pid patch is no longer needed.)_

---

# Probe Round 2 — Results (2026-05-16)

_Probes A–E run against "forever curious" (6 measures, 7 staves) in MS4._
_All write probes used `startCmd`/`endCmd` + `cmd("undo")` — score left clean._
_Source: CC_INSTRUCTION_runtime_probe2.md._

## Key architectural finding — add-first-then-set

**The correct element-construction pattern is `cursor.add(element)` BEFORE setting
properties**, not after. The add call real-parents the element in the engraving layer;
property writes on an unparented floating element may not take effect.

Correct pattern (all write tools):
```js
var el = api.engraving.newElement(api.engraving.Element.X)
c.add(el)          // real-parent FIRST
el.text = "..."    // THEN set properties
```

All code samples in `api_write.md` and `writable_props_survey.md` previously showed the
wrong order (set properties, then add). They have been corrected — see `api_write.md`
cursor positioning section.

## Probe A — Harmony (`h.text = "Cmaj7"`)

| Line | Result |
|------|--------|
| `h.text` after add + set | `"Cmaj7"` ✅ |
| `h.harmonyName` | `undefined` |
| `h.displayText` | `undefined` |
| `h.plainText` | `undefined` |

**Interpretation:** The `text` write works. `harmonyName`/`displayText`/`plainText` returning
`undefined` is ambiguous — these properties exist on the Harmony C++ subclass but
`newElement(HARMONY)` may return a generic `EngravingItem` wrapper at runtime that doesn't
expose them. The chord-symbol parser question remains open: a visual inspection (does the
chord appear styled or as raw text?) is needed. The grep-C++ option (CC's suggested next
step E.3) would resolve whether the parser fires from the `Pid::TEXT` setter.

## Probe B — TempoText

| Line | Result |
|------|--------|
| `tt.text` after add + set | `"♩=120"` ✅ |
| `tt.tempo` after add + set | `2` ✅ |
| `tt.tempoFollowText` after add + set | `false` ✅ |
| `curScore.tempo(tick)` | ❌ not a function |

All three properties survive the add+set correctly. No programmatic readback of playback
BPM is available from QML. Whether the score actually plays at 120 BPM requires a manual
listen test.

## Probe C — Dynamic

| Line | Result |
|------|--------|
| `dyn.dynamicType` after add + set | `8` ✅ |
| `dyn.subtype` after add + set | `8` ✅ |

Property survives the add. Visual glyph check (does the MF symbol appear?) still needed —
but property readback is correct.

## Probe D — Ottava

**SKIPPED** — crashed in a prior attempt. Confirms spanner insertion via `cursor.add()`
is broken for spanners (consistent with write_api_probe.md §7). `add_ottava` 15ma/15mb,
`add_volta`, and `add_pedal` remain deferred. `add_ottava` 8va/8vb already uses `cmd()`.

## Probe E — MuseScore.Playback / MuseScore.Audio

| Test | Result |
|------|--------|
| `import MuseScore.Playback 1.0` | ✅ Module loads |
| `AudioPlug` type | ❌ not a type |
| `PlaybackPanel` type | ❌ not a type |
| `MixerView` type | ❌ not a type |
| `Playback` type | ❌ not a type |
| `PlaybackModel` type | ❌ not a type |
| `MixerPanel` type | ❌ not a type |
| `AudioOutput` type | ❌ not a type |
| `import MuseScore.Audio 1.0` | ❌ module not installed |

The `MuseScore.Playback 1.0` namespace is registered and loads cleanly, but none of the
guessed type names exist. The real type names were found by grepping
`src/playback/qml/MuseScore/Playback/CMakeLists.txt`.

### MuseScore.Playback 1.0 — known surface (from CMakeLists.txt grep)

**C++ models — likely instantiable from a v2 extension** (registered via `qmlRegisterType`
or `setContextProperty`; do not transitively import forbidden modules):

- `MixerPanelModel`
- `MixerChannelItem`
- `PlaybackToolBarModel`
- `PlaybackLoadingModel`
- `MixerPanelContextMenuModel`
- `AuxSendItem`
- `InputResourceItem`
- `OutputResourceItem`
- `SoundFlagSettingsModel`
- `SoundProfilesModel`
- `OnlineSoundsStatusModel`
- `NotationRegionsBeingProcessedModel`
- `AbstractAudioResourceItem`

**QML view files — unusable from v2 extension** (transitively import `Muse.UiComponents`,
which the v2 sandbox forbids):

`MixerPanel.qml`, `PlaybackToolBar.qml`, `SoundFlagPopup.qml`,
`SoundProfilesDialog.qml`, `PlaybackLoadingInfo.qml`,
`OnlineSoundsStatusView.qml`, `NotationRegionsBeingProcessedView.qml`

**`MuseScore.Audio 1.0`** — definitively not installed; unreachable.

**Implication:** mixer/playback state (volume, mute, solo, channel routing, transport) is
probably reachable via the C++ models above, but a future probe round is needed to confirm
instantiation and enumerate which `Q_PROPERTY`s each model exposes. The view files are
blocked by the `Muse.UiComponents` import restriction and cannot be used.

### Structural note on `h.harmonyName` returning `undefined`

`newElement(Element.HARMONY)` returns a generic `EngravingItem` wrapper at runtime, NOT the
`Harmony`-subclass wrapper declared in `elements.h`. The Harmony-specific READ accessors
(`harmonyName`, `displayText`, `plainText`) are therefore unreachable from QML via the
`newElement` path. Visual confirmation of whether `h.text = "Cmaj7"` triggers the
chord-symbol parser remains an open question — it will be settled naturally when the first
`add_harmony` implementation is tested end-to-end.

## Updated status table

| Item | Prior status | Round 2 status |
|------|-------------|----------------|
| `cursor.add()` then property-set pattern | ✅ (add proven, order wrong in docs) | ✅ **Confirmed: add first, set after** |
| `h.text = "Cmaj7"` — text write works | ✅ (via API_PROPERTY) | ✅ **Confirmed round-trip** |
| Harmony chord-symbol parser fires | ❓ open | ❓ **Still open** — `h.harmonyName` unreachable (EngravingItem wrapper, not Harmony subclass); visual check at first implementation |
| `tt.tempo = 2.0` — property write works | ✅ (via API_PROPERTY) | ✅ **Confirmed round-trip** |
| `curScore.tempo(tick)` readable | ❓ open | ❌ **Not a function** on apiv1 Score wrapper |
| TempoText playback BPM | ❓ open | ❓ **Still open** — manual listen test needed |
| `dyn.dynamicType = 8` — property write works | ✅ (via API_PROPERTY) | ✅ **Confirmed round-trip** |
| Dynamic glyph renders correctly | ❓ open | ❓ **Still open** — visual check at first implementation |
| `cursor.add(ottava)` spanner registration | ❓ open | ❌ **Confirmed broken** — crashed |
| `MuseScore.Playback 1.0` loadable | ❓ open | ✅ **Module loads** |
| Playback C++ model names known | ❓ open | ✅ **List captured above** (CMakeLists grep) |
| Playback model Q_PROPERTYs enumerated | ❓ open | ❓ **Still open** — future probe round needed |
