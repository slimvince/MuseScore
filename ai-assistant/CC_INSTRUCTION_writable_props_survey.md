# CC Instruction — Survey Writable Properties + Remove Probe Code

## This instruction is for the master worktree (`C:\s\MS\`)

## Mandatory reads before starting
- `C:\s\MS\CLAUDE.md`
- `C:\s\MS\STATUS.md` (header only)
- `C:\s\MS\build_and_test.md`
- Relevant memory files under `C:\Users\vince\.claude\projects\c--s-MS\memory\`
- `C:\s\MS\ai-assistant\write_api_probe.md`
- `C:\s\MS\ai-assistant\runtime_probe.md`

---

## Part A — Remove probe code from Main.qml

The runtime probe round is complete. Remove the following temporary additions from `C:\s\MS\ai-assistant\Main.qml`:

- The `runRuntimeProbes()` function
- The 🔬 button that triggers it
- The probe results overlay / display
- The `probeResults` and `probeVisible` properties (or whatever they are named — find by searching for "probe" in Main.qml)

Do NOT remove anything else. Verify the extension still loads correctly after the removal. Deploy to the MS4 path.

Also verify: confirm no C++ files were modified in `C:\s\MS-core-api\` as part of the now-cancelled Pid patch instruction. The ms-core-api CC stopped before acting, but confirm the worktree is clean. If any changes were made, revert them and report what was reverted.

---

## Part B — Survey writable Q_PROPERTYs on 6 blocked element types

### Context

Six write tools are blocked because `api.engraving.Pid` is not exposed in v2 extensions, making `element.set(Pid.X, value)` uncallable. We will NOT modify MuseScore's C++ source. Before marking these tools as permanently out of scope, investigate whether any of the 6 element types have dedicated writable Q_PROPERTYs or Q_INVOKABLEs that bypass the need for Pid.

The 6 element types and what each tool needs to set:

| Element type | Tool | Needs to set |
|---|---|---|
| `DYNAMIC` | `add_dynamic` | Dynamic level (pp, mf, ff etc.) |
| `HARMONY` | `add_harmony` | Chord symbol text ("Cmaj7" etc.) |
| `REHEARSAL_MARK` | `add_rehearsal_mark` | Text label ("A", "B" etc.) |
| `TEMPO_TEXT` | `add_tempo_mark` | Display text + functional BPM |
| `STAFF_TEXT` | `add_staff_text` | Arbitrary text |
| `SYSTEM_TEXT` | `add_system_text` | Arbitrary text |

### What to investigate

For each element type, inspect `src/engraving/api/v1/elements.h` (and any related files) for:

1. **Dedicated writable Q_PROPERTYs** — properties declared with a WRITE accessor, e.g.:
   ```cpp
   Q_PROPERTY(int dynamicType READ dynamicType WRITE setDynamicType)
   ```
   or via `API_PROPERTY_T` / `API_PROPERTY` macros that include a write path.

2. **Q_INVOKABLEs that set content** — any method callable from QML that sets text or type without needing Pid, e.g.:
   ```cpp
   Q_INVOKABLE void setXmlText(const QString& text)
   ```

3. **Inherited writable properties** — these elements all inherit from `EngravingItem` and some from `TextBase`. Does `TextBase` expose any writable text property (e.g. `xmlText`, `plainText`) at the apiv1 wrapper level?

4. **The `subtype` property** — `EngravingItem` has a `subtype` accessor. Is it writable for any of these element types? Could `dynamic.subtype = 5` set the dynamic level?

### Where to look

- `src/engraving/api/v1/elements.h` — primary source for wrapper class declarations
- `src/engraving/api/v1/elements.cpp` — implementations
- The `API_PROPERTY` / `API_PROPERTY_T` macro definitions (in the same header) — understand whether the macro creates a read-only or read-write property
- `src/engraving/api/v1/scoreelement.h` — inherited base; check what's exposed there beyond `set(Pid, QVariant)`

### Output

Produce `C:\s\MS\ai-assistant\writable_props_survey.md` with:

For each of the 6 element types:
- **Writable properties found:** list any writable Q_PROPERTY or Q_INVOKABLE that could set the needed content, with the exact property name and type
- **Verdict:** ✅ workable path exists (describe it) / ❌ no path — Pid required / ⚠️ partial (e.g. text settable but BPM not)
- **Revised implementation note** if a path exists

Then a summary table and recommendation: which tools become implementable without C++ changes, which remain blocked.

Update `api_write.md` blocked-tool sections based on findings.
