# CC Instruction — Expose Pid enum in EngravingApiV1 (ms-core-api worktree)

## This instruction is for the ms-core-api worktree (`C:\s\MS-core-api\`)

## Mandatory reads before starting
- `C:\s\MS-core-api\CLAUDE.md`
- `C:\s\MS\STATUS.md` (header only)
- `C:\s\MS\build_and_test.md`
- Relevant memory files

## Context

The v2 form extension exposes ~100 enums via `api.engraving.*` (all declared via `ENUM_PROPERTY` in `src/engraving/api/v1/engravingapiv1.h`). The `Pid` enum is NOT among them, even though `ScoreElement::set(Pid, QVariant)` — already exposed — requires it as its first argument. Without `Pid`, the entire `set()` method is uncallable from QML for any property that doesn't have a dedicated writable Q_PROPERTY.

This blocks 6 write tools in the ai-assistant extension:
- `add_dynamic` (needs `Pid.DYNAMIC_TYPE`)
- `add_rehearsal_mark`, `add_tempo_mark`, `add_staff_text`, `add_system_text` (need `Pid.TEXT`)
- `add_harmony` (needs `Pid.TEXT`)
- `add_lyric` (needs `Pid.TEXT`, `Pid.VERSE`)
- `add_ottava` 15ma/15mb (needs `Pid.OTTAVA_TYPE`)

One line fixes all of them.

## The patch

### Step 1 — Find the pattern

Open `src/engraving/api/v1/engravingapiv1.h`. Find the block of `ENUM_PROPERTY` declarations — there should be around 100 entries, covering enums like `Element`, `NoteType`, `Direction`, `Placement`, `DynamicType`, `OttavaType` etc.

Note the exact macro syntax used, e.g.:
```cpp
ENUM_PROPERTY(DynamicType,           enums::DynamicType)
ENUM_PROPERTY(OttavaType,            enums::OttavaType)
```

### Step 2 — Find the Pid namespace

Confirm the fully-qualified name for `Pid`. Check:
- `src/engraving/types/propertyvalue.h` or `src/engraving/types/types.h` for the enum definition
- Whether it lives under `mu::engraving::Pid`, `enums::Pid`, or just `Pid` within the `mu::engraving` namespace

The other enums use `enums::X` — confirm whether `Pid` follows this convention or is in a different namespace.

### Step 3 — Add the line

Add one line to the `ENUM_PROPERTY` block in `engravingapiv1.h`:
```cpp
ENUM_PROPERTY(Pid,                   enums::Pid)   // or correct namespace
```

Place it alphabetically or near logically related entries (e.g. near `PlacementV`, `PlayEventType`). Follow the existing formatting exactly.

### Step 4 — Check for side effects

`Pid` is a large enum (~250 entries in MS4). Verify:
- The ENUM_PROPERTY macro handles large enums without issue (check how it wraps enums for QML — it may use `QMetaEnum` or a similar mechanism)
- No compile error from name collision — `Pid` shouldn't conflict with anything in the QML scope already

### Step 5 — Build

Build MuseScore. Fix any compile errors. The patch should be trivially small — if you find yourself making significant changes, stop and report.

### Step 6 — Deploy and verify

Deploy to the MS4 extension path. Open the ai-assistant extension. The existing probe infrastructure in `Main.qml` has a 🔬 button — use it to re-run the probes and confirm `api.engraving.Pid` is now defined and `Pid.TEXT`, `Pid.DYNAMIC_TYPE`, `Pid.VERSE` etc. return integer values.

Report the integer values of at minimum: `Pid.TEXT`, `Pid.DYNAMIC_TYPE`, `Pid.HARMONY_NAME` (if it exists), `Pid.VERSE`, `Pid.TEMPO`, `Pid.TEMPO_FOLLOW_TEXT`, `Pid.OTTAVA_TYPE`.

## Output

- The patch itself (minimal diff)
- Confirmed Pid integer values for the keys listed above
- Any build issues encountered
- No output file needed — findings feed directly into the next master-worktree CC session that implements the write tools
