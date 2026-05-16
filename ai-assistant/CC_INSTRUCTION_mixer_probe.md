# CC Instruction — Probe Mixer Accessibility from v2 Form Extension

## Mandatory reads before starting
- `C:\s\MS\CLAUDE.md`
- `C:\s\MS\STATUS.md` (header only)
- `C:\s\MS\build_and_test.md`
- Relevant memory files under `C:\Users\vince\.claude\projects\c--s-MS\memory\`
- `C:\s\MS\ai-assistant\api_survey.md` — specifically section 4 (Mixer) and open question A

## Goal

Determine whether the MuseScore Playback mixer (`MixerPanelModel`, `MixerChannelItem`) is accessible from a v2 form extension. This is api_survey.md open question A. First investigate from source; if source is ambiguous, do a minimal runtime probe.

---

## Source investigation

### Step 1 — How is the v2 QML engine configured?

In `muse/framework/extensions/internal/extensionsuiengine.cpp`:
- How is the v2 engine initialised?
- What import paths are added to it?
- Are any `MuseScore.*` module paths explicitly added, or only the base Qt paths?

### Step 2 — How is MuseScore.Playback registered?

In `src/playback/qml/MuseScore/Playback/CMakeLists.txt` (or equivalent):
- Is `MuseScore.Playback` registered via `qmlRegisterType` (C++ side, globally at startup) or via a `qmldir` file on a filesystem path?
- If `qmlRegisterType`: globally-registered types are available in any QML engine in the process — this would mean it IS accessible from the v2 extension engine.
- If `qmldir` only: it depends on whether that path is on the v2 engine's import path.

### Step 3 — Check MixerPanelModel and MixerChannelItem registration

In `src/playback/` source files:
- Are `MixerPanelModel` and `MixerChannelItem` registered via `qmlRegisterType<>(...)` calls?
- What URI, major version, minor version, and element name are used?
- Is the registration done at module init time (available to all engines) or engine-specifically?

### Step 4 — Check whether the import validator blocks it

In `muse/framework/extensions/qml/Muse/Extensions/extensionbuilder.cpp:42-60`:
- The validator blocks lines containing `import` + `Muse.` (with dot).
- Confirm `import MuseScore.Playback 1.0` would NOT be blocked (no `Muse.` substring).

---

## Runtime probe (if source is ambiguous)

If the source investigation cannot confirm or deny accessibility, write and deploy a minimal test. Create a throwaway QML file at `C:\s\MS\ai-assistant\mixer_probe_test.qml` (do NOT modify Main.qml) containing:

```qml
import QtQuick 2.15
import MuseScore 3.0
import MuseScore.Playback 1.0

Item {
    Component.onCompleted: {
        console.log("Playback import succeeded")
        var m = Qt.createQmlObject('import MuseScore.Playback 1.0; MixerPanelModel {}', parent)
        console.log("MixerPanelModel count:", m ? m.count : "null")
    }
}
```

Note: this cannot be run standalone — it would need to be temporarily substituted into the extension to test. Only do this if the source investigation is genuinely inconclusive. Document what you found from source first.

---

## Output format

Produce a markdown report `C:\s\MS\ai-assistant\mixer_probe.md`:

- **Registration mechanism:** how/where `MuseScore.Playback` types are registered
- **Accessibility conclusion:** ✅ accessible from v2 extension / ❌ not accessible / ⚠️ uncertain, runtime test needed
- **If accessible:** list what properties on `MixerChannelItem` are readable/writable — cross-reference `src/playback/internal/mixerchannelitem.h`
- **If not accessible:** what would be required to make it accessible (e.g. adding import path to v2 engine setup)
- **Recommendation:** include mixer tools in scope, exclude, or defer pending a C++ patch
