# ai-assistant test runner

End-to-end test harness for the MuseScore Studio 4 **ai-assistant** extension.
It launches MuseScore with a test score, opens the extension panel, types
natural-language prompts into the chat, and asserts on the **debug log** — the
structured JSON the extension writes for every tool call and result. The LLM is
only the router; the tool result is the ground truth. We never read the chat
UI, the `.mscz` file, or screenshots.

## Layout

```
testing/
├── test_runner.py            the harness
├── tests/                    test specs (one JSON file per scenario)
├── test_scores/
│   ├── empty_4_4.mscz        baseline: 4/4, 8 measures, treble, single staff
│   └── empty_4_4.musicxml    source the .mscz was generated from (music21)
└── README.md
```

## Running

```bash
# Validate the harness logic + live-log parsing — no MuseScore, no API, no GUI:
python test_runner.py --self-test

# Run one spec / a whole directory:
python test_runner.py tests/test_add_note.json --verbose
python test_runner.py tests/
python test_runner.py tests/ --stop-on-fail
```

GUI runs need:

```bash
pip install pywinauto pyautogui --break-system-packages
```

`--self-test` needs neither dependency (they are imported lazily).

> A live run takes over the mouse and keyboard and makes **real, billed Claude
> API calls** using whatever key is configured in the extension's Settings.
> Don't use the machine while it runs. Slam the mouse into a screen corner to
> abort (pyautogui FAILSAFE).

## Step 0 finding — opening the extension panel

There is **no CLI flag** to auto-open an extension's UI. `--extension <uri>`
(`commandlineparser.cpp`) is for batch *conversion* jobs only.

A form extension is opened from the menu. From `appmenumodel.cpp` the top-level
menu is **Plugins** (`&Plugins`) and each enabled extension is listed by its
manifest `title`, here **AI Assistant**:

```
Menu bar → Plugins → AI Assistant
```

The action code is `action://extensions/ai-assistant?action=open`, but that is
only dispatchable from inside MuseScore — not reachable by external automation.

MuseScore 4's menu bar is **Qt-Quick-rendered, not a native Win32 menu**, so
`pywinauto` cannot enumerate or click menu items, and the menu **ignores
Alt-mnemonics**. So the panel is opened by clicking the menu bar at calibrated
pixel coordinates. `test_runner.py` offers these strategies via
`OPEN_PANEL_METHOD`:

| value            | how it opens the panel                                                  |
|------------------|------------------------------------------------------------------------|
| `menu_click`     | **DEFAULT, hands-off.** Clicks Plugins `(290,16)` then AI Assistant `(288,117)` |
| `manual`         | pauses and lets the operator open the panel (un-calibrated machines)    |
| `coords`         | clicks `OPEN_PANEL_CLICKS`                                              |
| `menu_keyboard`  | `Alt+P` — **does not work on MS4** (kept only for reference)            |

`menu_click` coordinates are calibrated for a **maximized window @ 2560×1440**.
For another display, open Plugins → AI Assistant by hand, note the two pixel
positions, and update `PLUGINS_MENU_XY` / `AI_ASSISTANT_ITEM_XY` (or use
`manual`). `--open-method <x>` overrides the default per run.

What had to be solved to make `menu_click` reliable and hands-off:

- **Window found by process id, not title.** The main window's title is the
  *score name* (e.g. `empty_4_4`), never "MuseScore", so title matching failed.
  The runner finds the window by `proc.pid` and maximizes it for predictable
  menu geometry.
- **Direct clicks, no arrow keys.** Arrow-navigation between top menus is
  state-dependent on MS4 (Right opens a submenu when the highlighted item has
  one, otherwise moves sideways), so the runner clicks Plugins and the item
  directly.
- **The chat input auto-focuses; no click needed.** The panel opens as a
  floating dialog whose `TextField` has `focus:true`, so it grabs keyboard focus
  on open — verified by typing a prompt with no click and getting the tool call.
  (The dialog is *not* a separate UIA window, so it can't be focused by handle;
  the runner just relies on the auto-focus.)
- **Settle before typing.** `session_start` fires when `Main.qml` loads, but the
  input needs ~3 s more before it reliably accepts keystrokes — typing too early
  drops the leading characters and truncates the prompt. See `PANEL_SETTLE_SEC`.

**Readiness is detected from the log, not pywinauto.** After launch the runner
waits for a new `{"session_start":...}` line — written by `Main.qml` when the
panel loads — which is the panel's own "I'm up" signal.

**Verified end-to-end** on 2026-05-20: with `menu_click`, fully hands-off,
`test_add_note.json` passed both its write step (`add_note → {ok:true,...}`) and
its verify step (`get_notes_in_range`, with `noteName:"A4"` found nested in
`result.notes`). The harness types and sends with no human interaction.

## Debug-log format (verified against the live log, 2026-05-20)

The original brief described result lines as
`{"t":..,"result":"<tool>","value":{..}}`. The **actual** format written by
`Main.qml::_writeLogViaProcess` is:

```jsonc
{"t":"<ISO>","call":"<tool_name>","args":{...}}
{"t":"<ISO>","result":<value>,"ms":<elapsed_ms>}
{"session_start":true,"version":"v0.5.5","t":"<ISO>"}
```

The runner is built around three consequences:

1. **Result lines carry no tool name.** A result is paired to its call by
   timestamp: `result.t − ms ≈ call.t`.
2. **`<value>` is the raw tool return** — usually `{"ok":true,...}`, and for
   read tools a dict with nested arrays, e.g.
   `get_notes_in_range → {"ok":true,"notes":[...],"rests":[...]}`. So `contains`
   matching searches the result recursively.
3. **Each line is appended by a separate PowerShell process**, so lines can
   land out of file order. The `t` field is authoritative for ordering, never
   byte order. The log is UTF-8 (contains glyphs like `♩`); it is read as
   `utf-8-sig`.

## Test spec format

```jsonc
{
  "name": "add_note_basic",
  "description": "...",
  "score": "empty_4_4.mscz",              // filename in test_scores/ (copied to temp first)
  "steps": [
    {
      "prompt": "Add a quarter note A4 ...",  // typed into the chat
      "expect_tool": "add_note",              // optional: tool the LLM must call
      "expect_result": { "ok": true, "measure": 1 },   // optional: recursive subset of the result
      "expect_result_contains_keys": ["error"],        // optional: keys that must be present
      "verify": {                              // optional follow-up read
        "tool": "get_notes_in_range",          // optional: read tool the follow-up must call
        "prompt": "What notes are in measure 1 ...?",
        "contains": [ { "noteName": "A4" } ]   // each must match some object anywhere in the result
      }
    }
  ]
}
```

Matching rules:
- `expect_result` — recursive **subset**: every listed key/value must appear in
  the result; unlisted keys are ignored; numbers compare with a tiny tolerance.
- `expect_result_contains_keys` — the named keys must exist (any value). Used
  for honest-error checks (`["error"]`).
- `verify.contains` — each entry must subset-match **some object nested
  anywhere** in the read result (so it finds a note inside `result.notes`).

## Deviations from the brief (and why)

1. **Result-line format** — corrected as above; the brief's `value`/tool-named
   result shape does not exist. Pairing is by timestamp.
2. **`noteName`, not `pitch`** — `get_notes_in_range` notes expose
   `noteName` (e.g. `"A4"`), not a MIDI `pitch` integer. Specs assert on
   `noteName`. The result is `{ok,notes,rests}` (nested), so `contains` searches
   recursively rather than treating the result as a flat list.
3. **`test_blocked_tool_honest_error`** — the brief used `add_slur` as a
   "blocked" tool, but `add_slur` **is implemented** and returns `ok`, so it
   does not exercise honest-error handling. Substituted a deterministic error:
   a `get_key_at` on a non-existent measure (999), which returns
   `{"error":"Measure 999 not found"}`.

## How a send works (and the streaming guard)

`send_and_wait()` re-foregrounds MuseScore, clears the chat input, types the
prompt, then **presses Enter repeatedly** (every `NUDGE_ENTER_SEC`) until a tool
call appears. This is required because the extension **ignores Enter while it is
streaming a reply** — both the Enter nav-send handler and `sendMessage()` guard
on `isStreaming`, and a blocked send does *not* clear the input. So after one
step's tool call the LLM keeps streaming its final prose, and a verify prompt
sent during that window would be silently dropped. The typed text persists
across blocked sends, and a second Enter on an already-sent (empty) input is a
guarded no-op, so re-pressing Enter is safe and never double-sends.

## Known fragilities

- **An LLM API error looks like "no tool call".** The extension shows backend
  errors (e.g. `HTTP 500` / `OVERLOADED`, rate limits, bad key) in the chat UI
  but does **not** write them to the debug log — so when the API fails, the
  prompt sends fine yet no `call`/`result` ever appears and the step fails with
  *"no tool call seen"*. On any such failure the runner saves a full-screen
  **screenshot** (path printed in the failure detail) so you can see whether the
  chat shows an API error vs. an unsent prompt. If many steps fail this way,
  check the provider/key in Settings or switch provider; it is not a harness bug.
- **The chat input must hold keyboard focus when typing.** Keystrokes go to
  whatever control has focus. With `menu_click` the input auto-focuses on open
  and nothing steals it during a hands-off run, so no click is needed — but
  don't type into other windows mid-run. If focus is unreliable on your machine,
  set `INPUT_FIELD_COORDS` so the runner clicks the input before each send.
- **Single-instance MuseScore.** Specs run one launch each, fully killing
  MuseScore between files (`taskkill /F`). Don't run two harness processes at
  once.
- **Qt Quick opacity.** Individual chat controls aren't visible to UIA; that is
  why readiness uses the `session_start` log line and input uses simulated
  typing rather than control handles.
- **Force-kill on close** skips the unsaved-changes dialog (the score is a
  throwaway temp copy). Because a hard kill looks like a crash, MuseScore would
  normally show *"The previous session quit unexpectedly. Restore?"* on the next
  launch (and it defaults to **Yes**, which the nudge-Enter would accept). The
  runner prevents this by clearing `session/session.json` (the open-scores list
  MuseScore restores from) both before each launch and after closing, so neither
  the next spec nor a later manual launch shows the dialog. Path is
  `SESSION_STATE_FILE`.

## Baseline score note

`empty_4_4.mscz` was generated `music21 → MusicXML → MuseScore CLI`. The
MusicXML→MuseScore instrument mapping labels the (Piano) part **"Bandoneon"** in
the imported score. It is still a single treble staff in 4/4 over 8 measures, so
this is cosmetic and the specs don't assert on instrument. Regenerate with
`test_scores/empty_4_4.musicxml` if you need a different instrument label.
