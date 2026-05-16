# CC Instruction — Probe Write API Implementation Approaches

## Mandatory reads before starting
- `C:\s\MS\CLAUDE.md`
- `C:\s\MS\STATUS.md` (header only)
- `C:\s\MS\build_and_test.md`
- Relevant memory files under `C:\Users\vince\.claude\projects\c--s-MS\memory\`
- `C:\s\MS\ai-assistant\api_survey.md` (the ground-truth API survey)
- `C:\s\MS\ai-assistant\api_write.md` (the write tool designs to probe)

## Goal

We have designed a set of write tools for an LLM assistant in the ai-assistant MuseScore extension. Before implementing them, we need confidence that the implementation approaches described in `api_write.md` are sound. This is a **source-code investigation and minimal probing task**, not a full implementation.

For each implementation approach below, investigate the MuseScore source in `C:\s\MS-core-api\` to confirm it works as described, identify any gotchas, and where the source is ambiguous, write and deploy a minimal test snippet to the extension and try it against a real score.

Do NOT rewrite Main.qml. Use small isolated test functions if runtime testing is needed.

---

## Approaches to probe

### 1. Cursor-based note entry
`api_write.md` proposes: `cursor.rewindToFraction(tick)` + `cursor.setDuration(z, n)` + `cursor.addNote(pitch)` for `add_note`.

- Does `rewindToFraction` position the cursor correctly in the v2 extension context? `api_survey.md` notes "cursor-based traversal behaves differently in Extensions 2.0".
- Does `cursor.addNote(pitch, false)` overwrite existing content at that position as expected?
- Does `cursor.addNote(pitch, true)` (addToChord) add to an existing chord correctly?
- Does `cursor.addRest()` work?
- What happens if the cursor is positioned at a location that already has content of a different duration?

### 2. cmd() + selection pattern for spanners and dynamics
Several write tools work by: (a) set score selection to the target range, (b) fire a `cmd()`.

Probe: `add_slur`, `add_hairpin`, `add_ottava`.
- How is the selection set programmatically? Via `curScore.selection.selectRange(startTick, endTick, startStaff, endStaff)`?
- After setting the selection, does `cmd("add-slur")` / `cmd("add-hairpin")` / `cmd("add-8va")` correctly attach to the selected range?
- Is the selection state restored after the cmd(), or does the tool leave the score in a different selection state than before?
- Does this work inside a `startCmd`/`endCmd` bracket without interference?

### 3. Direct element construction for dynamics
`api_write.md` proposes: `newElement(Element.DYNAMIC)` + set subtype + `segment.add()`.

- What subtype value / property identifies the dynamic level (pp, mf, ff etc.)? Is it `subtype`, `text`, or a Pid property?
- Does `segment.add(dynamicElement)` work correctly inside `startCmd`/`endCmd`?
- Alternatively: is `cmd("add-dynamic")` usable non-interactively (does it open a dialog or act on selection silently)?

### 4. Direct element construction for harmony (chord symbols)
`api_write.md` proposes: `newElement(Element.HARMONY)` + set `harmonyName` + `segment.add()`.

- Does setting `harmonyName` on a new Harmony element work, or must it be set via a Pid?
- Does `segment.add()` place the harmony correctly?
- What segment type should the harmony attach to — `CHORD_REST` segment?

### 5. Direct element construction for lyrics
`api_write.md` proposes: `newElement(Element.LYRICS)` + set text/syllabic/verse + `chord.add()`.

- Is `chord.add(lyricsElement)` the right insertion point, or should it be `segment.add()`?
- How is the verse index set — is there a Pid or property for it, given that `api_survey.md` flags it as not a Q_PROPERTY?
- Does syllabic type set correctly via `lyrics.syllabic`?

### 6. addText() for various text types
`api_write.md` uses `curScore.addText(type, text)` for rehearsal marks, tempo marks, staff text, system text.

- Confirm which type strings are valid (`"REHEARSAL_MARK"`, `"TEMPO"`, `"STAFF"`, `"SYSTEM"` etc.) — cross-check against `src/engraving/api/v1/score.h` or `score.cpp`.
- Does `addText` require the cursor to be positioned first, or a selection to be active?
- For tempo marks: does `addText("TEMPO", "♩=120")` set a functional BPM, or just display text? The api_survey.md flagged tempo BPM mutation as untested end-to-end (open question E).

### 7. Volta construction
`api_write.md` proposes: `newElement(Element.VOLTA)` + set tick range + text.

- Is `Element.VOLTA` a valid enum value for `newElement()`?
- How are the start/end ticks and the volta text set on the new element?
- What is the correct insertion call — `curScore.add()`? `measure.add()`?

### 8. Section break and system break
`api_write.md` proposes: `cmd("section-break")` / `cmd("system-break")` after navigating to measure.

- Do these cmd() strings work when the target measure (not a note within it) is selected?
- How should the selection be set to target a whole measure rather than a note?

---

## Output format

Produce a markdown report `C:\s\MS\ai-assistant\write_api_probe.md` with one section per numbered item above.

For each:
- **Finding:** what the source investigation or runtime test revealed
- **Status:** ✅ works as designed / ⚠️ works with caveats (describe them) / ❌ does not work (describe what breaks) / ❓ inconclusive from source alone, needs runtime test
- **Revised implementation note** if the original approach needs adjustment

Flag anything that would require changes to `api_write.md` type signatures (not just implementation details).
