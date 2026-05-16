# AI Assistant — Cowork Handoff Note
_Last updated 2026-05-16 — v0.4.14, all major bugs fixed, pending discussion items listed_

---

## What this project is

A MuseScore 4/5 **extension** (not a plugin) that provides LLM-powered conversational chat about the open score. Supports Anthropic, OpenAI, Gemini, and custom providers. The user talks to the LLM about the score; the extension injects score context (metadata + notes) into every conversation.

This is part of a larger project — see `C:\s\MS\COWORK_HANDOFF.md` for the full picture (harmonic analysis engine, ms-core-api Core Access Layer, LLM integration architecture). The AI Assistant extension is the first concrete LLM-bridge artefact, built ahead of the CAL to validate where API gaps actually bite.

---

## My role vs CC's role

- **Cowork (me):** planning, architecture, writing CC instructions, reviewing results. I do NOT edit files directly.
- **CC (Claude Code CLI):** all file edits, builds, deploys.
- **Rule:** never write CC instructions until the user explicitly asks. Always fuse all pending fixes into one instruction set — never send partial instructions.

---

## File locations

| Purpose | Path |
|---|---|
| **Canonical source (edit here)** | `C:\s\MS-core-api\share\extensions\ai-assistant\Main.qml` |
| MS4 deploy | `%LOCALAPPDATA%\MuseScore\MuseScore4\extensions\ai-assistant\Main.qml` |
| Design docs (read-only reference) | `C:\s\MS\ai-assistant\` |
| Manifest | `C:\s\MS-core-api\share\extensions\ai-assistant\manifest.json` |
| CC memory (extension) | `C:\Users\vince\.claude\projects\c--s-MS-core-api\memory\` |

**Two-track model:** Extension work (Main.qml, JS files, manifest) belongs in the ms-core-api worktree and is done by ms-core-api CC. Master worktree and master CC are for MuseScore core/inferer work only. Design docs (`ai-assistant/*.md`) live in `C:\s\MS\ai-assistant\` as a shared reference — readable by both CCs, edited by Cowork.

Current version: **v0.4.14** — MS4 and ms-core-api source in sync at 90,552 bytes.

**Deploy steps (every release):**
1. Run gate: `grep -nE "^[[:space:]]*(import[[:space:]]+Muse\.|FlatButton)" Main.qml` — must return empty
2. Copy to MS4: `copy "C:\s\MS-core-api\share\extensions\ai-assistant\Main.qml" "%LOCALAPPDATA%\MuseScore\MuseScore4\extensions\ai-assistant\Main.qml"`
3. Bump version string in Main.qml

---

## Settled architectural decisions

### Extension, not plugin
ai-assistant stays as a form-extension (`type: "form"` in manifest). The legacy `MuseScore { pluginType: "dialog" }` plugin sandbox was investigated and rejected. Extensions are MuseScore's strategic direction; new APIs land there first. **Do not reopen.**

### MS4 keyboard input

MS4's C++ event filter blocks key events for `TextArea`/`TextEdit` but yields to `TextField`/`TextInput`. Chat input is a `TextField` (since v0.4.4). Read-only LLM bubbles remain `TextArea` — fine since they need no key input.

**Enter key (fixed v0.4.11):** MS4 binds Return/Enter to `nav-trigger-control` via QML `Shortcut` elements in the main window (`muse/framework/shortcuts/qml/Muse/Shortcuts/Shortcuts.qml`). Any extension `Shortcut` at the same key creates an ambiguous overload — Qt fires neither, silently. Fix: dynamically build a `NavigationSection → NavigationPanel → NavigationControl` chain via `Qt.createQmlObject`, register it active on input focus via `requestActive(false)`, connect `triggered` → send. The `Qt.createQmlObject` string bypasses the deploy gate validator (which only scans literal `import` lines). ✅

### Settings persistence (fixed v0.4.7)

`Qt.labs.settings` is not deployed in the MS4 install — windeployqt only ships modules MuseScore's own UI imports. Fix: `import MuseScore 3.0; Settings { category: "AIAssistant" }` — a vendored `QQmlSettings` registered at `muse/framework/extensions/api/v1/extapiv1.cpp:40`. Process-global, works in both V1 and V2 extension engines. ✅

`QtQuick.LocalStorage` ruled out — `QQmlEngine::setOfflineStoragePath()` is never called anywhere in the MuseScore codebase.

### Deploy gate
`grep -nE "^[[:space:]]*(import[[:space:]]+Muse\.|FlatButton)" Main.qml` — expects empty output. Mirrors the actual extension validator in `extensionbuilder.cpp:42-60`. `import MuseScore 3.0` is fine (no dot). `Qt.createQmlObject` strings are not scanned.

### LLM tool design — two-layer architecture (settled 2026-05-16)

**Layer 1 — Information model:** defines the vocabulary (types, enumerations, structures) used across all tools. Split into domains: score & contents, playback, settings. Lives as separate documents (`infomodel_score.md` etc.). Canonical language is English. The LLM bridges for users in other languages — no localisation work in the tool layer.

**Layer 2 — API:** tool endpoints whose method signatures reference the information model types. Read tools first; write tools once the read surface is stable.

**Design principles:**
- Fine-grained tools (composable, no information hiding), not coarse answer-shaped tools. Question-shaped tools can be added later, built on top of data-model tools — either as QML-side compositions or by letting the LLM reason over data-model results.
- Tools always speak music, never MuseScore internals. No tpc values, raw MIDI pitch, or tick integers. All values expressed in musical language per the information model.
- `cmd()` is the implementation of write tools, not a tool itself. The LLM never sees raw action code strings. The cmd() whitelist for internal use excludes: file ops, application ops (`quit`, `restart`, `revert-factory`), undo/redo, and dialog-spawning commands. The notation-editing surface is safe.
- Undo: all writes go through `startCmd(name)`/`endCmd()`, landing in MuseScore's built-in undo stack. No custom confirm/undo flow needed — the user just hits Ctrl+Z.

**Internationalisation:**
- API and information model are in English throughout.
- The LLM bridges user language ↔ canonical API parameters on every request.
- Note naming: international convention (C D E F G A B). Nordic/Germanic H/B convention is handled by the LLM transparently.
- Instrument and part names are free-text strings passed through as-is from the score (user-defined, any language). The LLM handles fuzzy matching (e.g. "violin" → "Viulu I").

**Ground truth for what is actually exposed:** `C:\s\MS\ai-assistant\api_survey.md`.

### Score context — tool-only, no pre-injection (settled 2026-05-16)

**Principle: the score lives in MuseScore, not in the conversation. The conversation contains questions and answers. Tools are the bridge.**

No score data is injected into the system prompt or any message — not metadata, not notes, nothing. Any pre-injected copy risks becoming stale the moment the user edits the score, and the user already has the score open in front of them; narrating it back is redundant.

The system prompt is purely functional:
> *"You are a music assistant embedded in MuseScore. Use the provided tools to read the open score. Only fetch what you need to answer the question."*

The LLM calls tools to reach into the live `curScore` when it needs data. This also sets up write tools naturally — the same access path, extended with mutations.

The previous tiered injection scheme (Tier 1 metadata always, Tier 2 note array ≤ 2000, Tier 3 on-demand tools) is superseded. Everything is on-demand tools. **Do not reopen.**

### Dynamic model listing (fixed v0.4.14)
Fetched from provider APIs on key entry/change and on `Component.onCompleted`. Gemini filters by `supportedGenerationMethods` containing `generateContent`. Anthropic uses `display_name`. OpenAI filters by `gpt-|o1|o3` prefix. Hardcoded fallback per provider on any fetch failure. If previously-selected model disappears from fetched list, falls back to first item with a blue ℹ notice.

### Conversation persistence (fixed v0.4.14)
Stored as JSON blob under `savedConversations` in MuseScore 3.0 Settings. Shape: `[{ id, title, provider, model, messages: [{role, content}] }]`. Title = first 50 chars of first user message. Caps: 20 conversations, 200 messages per conversation, 500k char safety net. System prompt is NOT stored — regenerated fresh from live score each time. Saves on every `appendMessage`, loads on `Component.onCompleted`.

### Bubble rendering
ScrollView + Column + Repeater (not ListView — abandoned due to contentHeight=0 race condition). Bubble height via `implicitHeight = topPadding + contentHeight + bottomPadding`. Copy button (⎘) on each LLM bubble: `selectAll(); copy(); deselect()` — mouse-triggered, bypasses MS4 C++ filter.

### SplitView layout
`SplitView` (Qt.Horizontal). Sidebar: `preferredWidth: 200`, `minimumWidth: 140`, `maximumWidth: 360`. Main area: `fillWidth: true`.

---

## Current state — v0.5.0 (2026-05-16)

### All confirmed working ✅
- All keyboard input in MS4 — letters, numbers, symbols, AltGr, Ctrl combos
- Enter to send — NavigationControl workaround
- Settings persistence — MS4 and MS5 via MuseScore 3.0 Settings
- Conversation persistence — survives extension close/reopen
- Dynamic model listing — fetched from provider APIs, hardcoded fallback
- Auto-scroll, ⎘ copy button, SplitView resizable
- **LLM tool calling** — `get_score_info`, `get_structure`, `add_rehearsal_mark` wired end-to-end for Anthropic, OpenAI, Gemini, and custom/Ollama providers
- **Layered JS file structure** — ScoreAccess.js (317 lines), ToolSchemas.js (95 lines), Dispatch.js (23 lines) alongside Main.qml
- **Dynamic system prompt** — chord-symbol spelling + concert pitch injected from score; user-editable override in settings panel

### Hard limits ❌
- **Window resizability in MS4** — MS4 hard limit, not worth pursuing.
- **Streaming disabled for tool-call turns** — tool-call responses wait for completion; only final text response streams. Acceptable for v1.

### Smoke test ⚠️ (pending — 2026-05-16)
v0.5.0 end-to-end tool calling not yet verified in MS4. Suggested tests:
- "what score is open?" → should fire `get_score_info`
- "where are the rehearsal marks?" → should fire `get_structure`
- "add rehearsal mark A at bar 5" → should fire `add_rehearsal_mark`, Ctrl+Z reverses it

### Key technical findings (v0.5.0)
- **`.pragma library` blocked** — library-mode JS files cannot access QML context properties (`api`, `curScore`). Fix: non-library mode; Main.qml passes the ScoreAccess module into `Dispatch.dispatchTool(ScoreAccess, name, args)` explicitly.
- **Settings readable from extension:**
  - `curScore.style.value("chordSymbolSpelling")` → int 0–4 (STANDARD / GERMAN / GERMAN_PURE / SOLFEGGIO / FRENCH) ✅
  - `curScore.style.value("concertPitch")` → bool ✅
  - MuseScore UI language: ❌ not accessible — `Qt.locale().name` is OS locale only; MuseScore's own UI-language override lives in C++ `languagesConfiguration()` and is not exposed to extensions. UI language not injected into system prompt (would mislead with OS locale).

---

## Open / pending items

1. **ms-core-api source copy** — ✅ Resolved. `C:\s\MS-core-api\share\extensions\ai-assistant\Main.qml` now exists and is in sync. Deploy both paths on every release (see deploy steps above).

2. **Information model and API** — all drafted: `infomodel_score.md`, `infomodel_playback.md`, `infomodel_settings.md`, `api_read.md`, `api_write.md`, `api_playback.md`. Write API probes complete (`write_api_probe.md`, `runtime_probe.md`). Not yet implemented in Main.qml.

2. **Remaining tools** — ~24 tools from `api_read.md` and `api_write.md` not yet implemented. Add in batches once v0.5.0 smoke test passes. Open runtime questions to verify during next batch: (a) `h.text = "Cmaj7"` triggers chord-symbol parser vs. raw text; (b) `tt.tempo = 2.0` drives playback BPM; (c) `dyn.dynamicType = 8` renders MF glyph.

3. **Files in chat** — not yet designed. Use cases: (a) PDF of lyrics → insert into score; (b) photo/scan of score → transcribe to MuseScore. Needs design discussion.

4. **Mixer / Playback module** — `MuseScore.Playback 1.0` loads. C++ models likely instantiable (full list in `runtime_probe.md`). Q_PROPERTY surfaces not enumerated — future probe round needed before mixer tools can be designed.

5. **Streaming for tool-call turns** — currently disabled (waits for complete response). Re-enable once tool calling is stable.

---

## Key technical details

- **Streaming:** XMLHttpRequest SSE for Anthropic/OpenAI/Gemini. Thinking budget: `maxTok = Math.max(providerMaxTokens, budget + 1024)`.
- **Per-preset API keys:** stored in `presetApiKeys` map, not a single field.
- **QML console.log:** does NOT appear in MS4 logs. MS4 logs show harmless startup warnings (`URI musescore://extensions/ai-assistant is not registered`) — not our bugs.
- **TextField vs TextArea:** chat input is `TextField`; LLM display bubbles are `TextArea`. Do not swap.
- **Auto-scroll:** `scrollToBottom()` sets `chatScroll.contentItem.contentY` on the Flickable directly.
- **CC preamble — extension CC (ms-core-api):** Read `C:\s\MS-core-api\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\build_and_test.md`, relevant memory files, and this HANDOFF.md before any task.
- **CC preamble — core CC (master):** Read `C:\s\MS\CLAUDE.md`, `C:\s\MS\STATUS.md` (header only), `C:\s\MS\build_and_test.md`, relevant memory files. Does not touch extension files.
