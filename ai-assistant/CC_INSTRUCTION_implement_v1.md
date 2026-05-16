# CC Instruction — Implementation v1: File Structure + System Prompt + First 3 Tools

## This instruction is for the ms-core-api worktree (`C:\s\MS-core-api\`)

## Mandatory reads before starting
- `C:\s\MS-core-api\CLAUDE.md`
- `C:\s\MS\STATUS.md` (header only)
- `C:\s\MS\build_and_test.md`
- Relevant memory files under `C:\Users\vince\.claude\projects\c--s-MS-core-api\memory\`
- `C:\s\MS\ai-assistant\HANDOFF.md`
- `C:\s\MS\ai-assistant\api_survey.md`
- `C:\s\MS\ai-assistant\api_read.md` (get_score_info, get_structure)
- `C:\s\MS\ai-assistant\api_write.md` (add_rehearsal_mark, element construction pattern)
- `C:\s\MS\ai-assistant\infomodel_score.md`
- `C:\s\MS\ai-assistant\runtime_probe.md` (confirmed patterns, add-first-then-set)

---

## Overview

This instruction has four parts:

- **Part A** — Survey what MuseScore settings are readable from the extension API
- **Part B** — Implement system prompt construction (dynamic, settings-aware)
- **Part C** — Refactor Main.qml into a layered JS file structure
- **Part D** — Implement the first 3 tools and wire the tool-calling loop

Do them in order. Report Part A findings inline before proceeding to Part B.

---

## Part A — Survey readable MuseScore settings

Before writing any code, investigate what application/score settings are accessible from
a v2 form extension. We want to know what is readable so the system prompt can be
tailored to the user's environment.

**Specifically look for:**

1. **UI language** — Is MuseScore's configured interface language readable? Check:
   - `api.application` surface (if any)
   - `Qt.locale().name` — system locale fallback (always available)
   - Whether MuseScore stores its own language override separately from system locale

2. **Note naming convention** — Does MuseScore expose whether the user has configured
   German/Nordic note naming (H instead of B, B instead of Bb)? Check:
   - Score metadata (`curScore.metaTag(...)`)
   - Any preference property on `api` or `curScore`
   - MuseScore source: `src/notation/` or `src/appshell/` for how this preference is stored
     and whether it is registered in the QML context

3. **Concert pitch** — Is `curScore.concertPitch` (or equivalent) readable? This affects
   whether note names in transposing instrument parts should be concert pitch or written.

4. **Any other settings** that are musically meaningful for an LLM to know upfront.
   Look at what properties are available on `curScore`, `api`, and any other top-level
   QML context objects. Flag anything that seems relevant to how the LLM should
   interpret or generate musical content (e.g. enharmonic spelling preference,
   key signature display, rhythm notation style).

**Output for Part A:** a short table — setting name, how to read it from QML, what values
it can take. Mark each as ✅ confirmed readable / ❌ not accessible / ❓ needs runtime check.

---

## Part B — System prompt construction

Implement a `buildSystemPrompt()` function in Main.qml (or in a new `AppContext.js` if
that is cleaner — your call). This function is called once at startup and whenever
settings change, and returns the full system prompt string to use for all LLM requests.

**The prompt has three layers, concatenated in this order:**

### Layer 1 — Static instructions (hardcoded default)

```
You are a music assistant embedded in MuseScore. A score is open in the editor.

Use the provided tools to read the score when needed. Only fetch what is required
to answer the question — do not call read tools unnecessarily.

You can also modify the score using write tools. All changes land in MuseScore's
undo stack and can be reversed with Ctrl+Z. After a successful write, briefly
confirm what you did.
```

### Layer 2 — Dynamic context (injected from MuseScore settings at runtime)

Append one line per relevant setting found in Part A. At minimum:

- If MuseScore's language is not English (from Part A finding):
  `"The user's MuseScore interface language is [language]. Respond in [language] unless the user writes in a different language."`

- Note naming convention (from Part A finding):
  - If international (default): `"Use international note naming: C D E F G A B."`
  - If German/Nordic: `"The user's note naming convention uses H for B-natural and B for B-flat."`

- Concert pitch (if readable):
  - If on: `"Concert pitch is enabled. All note names are concert pitch."`
  - If off: `"Concert pitch is off. Note names in transposing instruments are written pitch."`

- Any other settings found in Part A that are worth injecting — use judgement.

### Layer 3 — User override (from Settings)

Read a stored string `systemPromptOverride` from `MuseScore 3.0 Settings`. If non-empty,
**append** it after Layers 1 and 2 (do not replace them — appending lets users add
instructions without losing the baseline). If the user wants to fully override, they can
clear Layers 1+2 by starting their override with a special marker (not needed for v1 —
simple append is enough).

**`buildSystemPrompt()` is called:**
- On `Component.onCompleted`
- When the settings panel is closed after a change
- When a new score is opened (if MuseScore exposes a signal for this)

---

## Part C — JS file structure

Split the score-access and tool-dispatch logic out of Main.qml into three companion
`.js` files. All three live alongside `Main.qml` in `C:\s\MS-core-api\share\extensions\ai-assistant\`.

### `ScoreAccess.js`

The MuseScore layer. Contains all functions that read or write `curScore`.
No LLM concepts. No JSON schema. No mention of tool names.
Written for the MuseScore community — readable by someone who knows QML and MuseScore
but has never heard of an LLM.

Functions to implement for v1 (others stubbed as `// TODO`):

- `getScoreInfo()` — returns an object matching `ScoreInfo` from `infomodel_score.md`:
  title, composer, key signature at measure 1, time signature at measure 1, tempo at
  measure 1 (if any), number of measures, array of part names.

- `getStructure(startMeasure, endMeasure)` — returns an array of per-measure objects.
  For each measure: measure number, key signature, time signature, any rehearsal marks
  (text), any tempo marks (text + bpm if readable). Uses `curScore.firstMeasure` /
  `measure.nextMeasure` traversal. Respects `startMeasure`/`endMeasure` bounds
  (both optional, 1-based).

- `addRehearsalMark(measure, text)` — adds a rehearsal mark at the start of the given
  measure. Uses the confirmed add-first-then-set pattern:
  ```js
  curScore.startCmd("add rehearsal mark")
  var c = curScore.newCursor()
  c.track = 0
  c.rewindToTick(measureStartTick)
  var rm = api.engraving.newElement(api.engraving.Element.REHEARSAL_MARK)
  c.add(rm)       // add first
  rm.text = text  // then set
  curScore.endCmd()
  ```
  Returns `{ ok: true }` on success or `{ error: "..." }` on failure (wrap in try/catch).

All functions must guard against `!curScore` and return `{ error: "No score open" }`.

### `ToolSchemas.js`

Tool schema definitions in the format each provider expects. Export a function
`getToolSchemas(providerFormat)` that returns the tools array for the given format:
`"anthropic"`, `"openai"`, or `"gemini"`. The custom provider uses `"openai"` format.

For v1, define schemas for the three tools. The core definition is provider-agnostic;
the wrapper differs:

**Anthropic format:**
```json
{
  "name": "get_score_info",
  "description": "Returns basic information about the open score: title, composer, key signature, time signature, tempo, number of measures, and list of parts/instruments.",
  "input_schema": { "type": "object", "properties": {}, "required": [] }
}
```

**OpenAI format:**
```json
{
  "type": "function",
  "function": {
    "name": "get_score_info",
    "description": "...",
    "parameters": { "type": "object", "properties": {}, "required": [] }
  }
}
```

**Gemini format:**
```json
{
  "name": "get_score_info",
  "description": "...",
  "parameters": { "type": "object", "properties": {} }
}
```

Schemas for all three tools:

**`get_score_info`** — no parameters.

**`get_structure`** — parameters:
- `startMeasure` (integer, optional): first measure, 1-based. Default: 1.
- `endMeasure` (integer, optional): last measure, 1-based. Default: last measure.

**`add_rehearsal_mark`** — parameters:
- `measure` (integer, required): measure number, 1-based.
- `text` (string, required): rehearsal mark text, e.g. "A", "B", "Verse", "Chorus".

### `Dispatch.js`

Maps tool name → ScoreAccess function. Import ScoreAccess.js and export a single
function `dispatchTool(name, args)` that:
1. Looks up the tool name
2. Calls the corresponding ScoreAccess function with the parsed arguments
3. Returns the result object (already `{ ok: true }` or `{ error: "..." }` from ScoreAccess)
4. Wraps the whole thing in try/catch — any uncaught exception becomes `{ error: e.toString() }`

```js
// Example shape
function dispatchTool(name, args) {
    try {
        if (name === "get_score_info")    return ScoreAccess.getScoreInfo()
        if (name === "get_structure")     return ScoreAccess.getStructure(args.startMeasure, args.endMeasure)
        if (name === "add_rehearsal_mark") return ScoreAccess.addRehearsalMark(args.measure, args.text)
        return { error: "Unknown tool: " + name }
    } catch(e) {
        return { error: e.toString() }
    }
}
```

### Main.qml changes

Add at the top of Main.qml (after existing imports):
```qml
import "ScoreAccess.js" as ScoreAccess
import "ToolSchemas.js" as ToolSchemas
import "Dispatch.js" as Dispatch
```

Remove any score-access logic currently inlined in Main.qml and replace with calls to
ScoreAccess. (In v1 there is probably very little — the read pipeline is new.)

---

## Part D — Tool-calling loop

Extend the existing XHR/streaming response handler to support tool calls. The existing
flow sends a message and displays the streamed text response. The new flow:

1. Include tool schemas in every request payload (`tools` / `functions` array per provider).
2. In the response handler, detect whether the response contains a tool call alongside
   or instead of text content.
3. If a tool call is detected:
   a. Extract the tool name and arguments (JSON-parse the arguments string).
   b. Call `Dispatch.dispatchTool(name, args)`.
   c. Append the assistant's tool-call message and a tool-result message to the
      conversation history.
   d. Send a new request with the updated history and continue the loop.
4. When a text response arrives (no tool calls), display it as before.

**Per-provider tool call detection and result format:**

**Anthropic:**
- Tool call in response: `content` array contains a block with `"type": "tool_use"`.
  The block has `id`, `name`, `input` (already parsed object in non-streaming; accumulated
  from `input_json_delta` events in streaming).
- Append to history:
  ```json
  { "role": "assistant", "content": [ ...the full content array from the response... ] }
  { "role": "user", "content": [
      { "type": "tool_result", "tool_use_id": "<id>", "content": "<JSON.stringify(result)>" }
  ]}
  ```

**OpenAI (and custom/Ollama):**
- Tool call in response: `choices[0].message.tool_calls` array.
  Each entry has `id`, `function.name`, `function.arguments` (string, JSON-parse it).
- Append to history:
  ```json
  { "role": "assistant", "tool_calls": [ ...the tool_calls array... ] }
  { "role": "tool", "tool_call_id": "<id>", "content": "<JSON.stringify(result)>" }
  ```

**Gemini:**
- Tool call in response: `candidates[0].content.parts` contains a part with `functionCall`.
  Part has `name` and `args` (already parsed object).
- Append to history:
  ```json
  { "role": "model", "parts": [ ...the original parts... ] }
  { "role": "user", "parts": [
      { "functionResponse": { "name": "<name>", "response": <result object> } }
  ]}
  ```

**Streaming note:** For the first implementation, it is acceptable to not stream the
assistant turn that contains a tool call — wait for the complete response before
executing the tool. Only the final text response (after all tool calls are resolved)
needs to stream. This simplifies the implementation significantly.

**Error handling:** If `dispatchTool` returns `{ error: "..." }`, send that error string
as the tool result content. The LLM will then explain the problem to the user. Never
crash or silently drop a tool call.

**Max iterations:** Guard against infinite loops — if the tool-calling cycle exceeds
10 iterations without a text response, break and display an error message.

---

## Part E — Settings UI for system prompt

Add a system prompt editor to the settings panel in Main.qml:

- A labelled `TextArea` (multi-line) showing the current `systemPromptOverride` value
  from Settings, or empty if not set.
- A "Reset to default" button that clears `systemPromptOverride` and calls
  `buildSystemPrompt()` to refresh.
- Save on change (same pattern as other settings fields).
- Placeholder text explaining what the field does:
  `"Additional instructions appended to the system prompt. Leave empty to use the default."`

Keep it compact — this is a power-user feature, not the main UI.

---

## Deploy and verify

The canonical source is `C:\s\MS-core-api\share\extensions\ai-assistant\`. Deploy from there.

1. Run deploy gate: `grep -nE "^[[:space:]]*(import[[:space:]]+Muse\.|FlatButton)" Main.qml` — must return empty.
2. Deploy to MS4: `copy "C:\s\MS-core-api\share\extensions\ai-assistant\Main.qml" "%LOCALAPPDATA%\MuseScore\MuseScore4\extensions\ai-assistant\Main.qml"`
3. Verify extension loads without errors in MS4.
4. Open a score and confirm:
   - The chat interface still works (send a plain text message, get a response).
   - The LLM calls `get_score_info` when asked "what score is open?" and returns
     intelligible information.
   - The LLM calls `add_rehearsal_mark` when asked to add one, and the mark appears
     in the score.
   - Ctrl+Z removes the mark.
5. Check that the system prompt editor appears in the settings panel and saves/resets correctly.

---

## Output

Report:
1. Part A findings table (settings survey).
2. Whether `buildSystemPrompt()` injects anything beyond the static text (i.e. which
   Part A settings were accessible).
3. The three JS files created (confirm paths and line counts).
4. End-to-end test results for the three tools.
5. Any surprises or deviations from this plan.

Bump the version string in Main.qml to **v0.5.0** — this is the first version with
LLM tool calling.
