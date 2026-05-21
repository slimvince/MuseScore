#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ai-assistant test runner
========================

Drives the MuseScore Studio 4 "ai-assistant" extension end-to-end:

  1. launches MuseScore with a (temp copy of a) test score
  2. opens the ai-assistant extension panel via the MuseScore menu
  3. for each step, types a natural-language prompt in the chat and presses Enter
  4. monitors the extension debug log for the resulting tool call(s) + result(s)
  5. compares against expected values from a JSON test spec
  6. reports pass / fail per step and overall
  7. closes MuseScore when done

The output channel is the DEBUG LOG only -- never the QML chat UI, never the
.mscz file, never screenshots. The log carries one JSON object per line for
every tool call and result. The LLM is just the router; the tool result is the
ground truth we assert against.

----------------------------------------------------------------------------
STEP 0 FINDING -- how the extension panel is opened
----------------------------------------------------------------------------
There is no CLI flag that auto-opens an extension's UI. The `--extension <uri>`
flag (commandlineparser.cpp) is for batch *conversion* jobs only, not for
opening a form extension interactively.

A form extension is opened through the menu. The menu registration lives in
src/appshell/.../appmenumodel.cpp: the top-level menu is "&Plugins" and each
enabled extension is added as an item titled from its manifest -- here
"AI Assistant" (manifest.json "title"). So the open path is:

    Menu bar -> Plugins -> AI Assistant

Because MuseScore 4's menu bar is Qt-Quick-rendered (NOT a native Win32 menu),
pywinauto cannot enumerate or click individual menu items -- it only sees the
top-level window. So the panel is opened by simulated keyboard / coordinate
input (see open_extension_panel + the OPEN_PANEL_* config below), not by a
native menu API. Several strategies are provided; the most robust for a first
run on an un-calibrated machine is OPEN_PANEL_METHOD = "manual".

----------------------------------------------------------------------------
DEBUG LOG FORMAT (verified against the live log, 2026-05-20)
----------------------------------------------------------------------------
The brief described result lines as {"t":..,"result":"tool","value":{..}}.
The ACTUAL format emitted by Main.qml::_writeLogViaProcess is:

    {"t":"<ISO8601>","call":"<tool_name>","args":{...}}
    {"t":"<ISO8601>","result":<value>,"ms":<elapsed_ms>}
    {"session_start":true,"version":"v0.5.5","t":"<ISO8601>"}

Key consequences this runner is built around:
  * The RESULT line carries NO tool name. A result is paired to its call by
    timestamp: result.t - ms ~= call.t  (see pair_result_for_call).
  * <value> is the raw tool return -- often a dict like {"ok":true,...}, and
    for read tools a dict with nested arrays, e.g.
        get_notes_in_range -> {"ok":true,"notes":[...],"rests":[...]}
    so "contains" matching searches the result recursively (find_anywhere).
  * Each line is appended by a SEPARATE PowerShell process, so lines can land
    out of file order. The "t" field is authoritative for ordering, never the
    byte order in the file. The log is UTF-8 (contains glyphs like the quarter
    note); we decode utf-8-sig.
"""

import sys
import os
import re
import json
import time
import shutil
import tempfile
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

# Tool results contain non-cp1252 glyphs (e.g. the quarter-note U+2669 in tempo
# text). On Windows the default console/file encoding is cp1252, so printing
# them raises UnicodeEncodeError and aborts a spec. Force UTF-8 on stdout/stderr.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001  (older Python / non-reconfigurable stream)
        pass

# ---------------------------------------------------------------------------
# Configuration  (edit here)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent

MUSESCORE_EXE   = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"
# As of the process-free logger (Main.qml _flushLogQueue via FileIO), the
# extension writes the debug log to the SYSTEM TEMP DIR — FileIO refuses to
# write under userAppDataPath, so the old logs/ path is no longer used. QML uses
# FileIO.tempPath(); Python's tempfile.gettempdir() resolves to the same dir.
DEBUG_LOG       = os.path.join(tempfile.gettempdir(), "ai-assistant-debug.log")
TEST_SCORES_DIR = str(SCRIPT_DIR / "test_scores")
TESTS_DIR       = str(SCRIPT_DIR / "tests")

# MuseScore lists open scores in session.json and clears it only on a CLEAN
# exit. Our force-kill leaves the temp score in it, so the next launch shows
# "The previous session quit unexpectedly. Restore?" (which defaults to Yes).
# The runner clears this file before each launch and after closing. This is the
# real MuseScore4 app-data location (no longer derivable from DEBUG_LOG, which
# now points at the temp dir).
SESSION_STATE_FILE = r"C:\Users\vince\AppData\Local\MuseScore\MuseScore4\session\session.json"

# How long to wait for each LLM response (seconds). LLM calls typically 3-8s,
# but a multi-tool turn (read then write) can chain and the model can be slow
# under load, so allow generous headroom.
LLM_TIMEOUT_SEC = 30   # lowered from 90: no-tool steps fail fast (text is captured on attempt 1 regardless)

# How long to wait for MuseScore to start and load a score (seconds).
MS_LAUNCH_TIMEOUT_SEC = 30

# Delay between keystrokes when typing prompts (seconds). Increase if MS eats chars.
TYPE_INTERVAL = 0.05

# After the last new log line appears, wait this long with no further lines
# before deciding a step's tool activity is finished (handles multi-tool turns).
SETTLE_SEC = 2.5

# The extension ignores Enter while it is streaming a reply. Re-press Enter this
# often (seconds) until the message actually sends and a tool call appears.
NUDGE_ENTER_SEC = 3.0

# Per-step attempts. The extension's debug logger (separate PowerShell process
# per line) occasionally races and drops a result line; on "call seen but no
# result" (or no call) the runner re-sends the (idempotent) prompt this many
# times before failing.
STEP_ATTEMPTS = 2

# Substring used to find the MuseScore main window title.
WINDOW_TITLE_RE = "MuseScore"

# Readiness is detected from the extension's own debug-log "session_start"
# line (written when the panel's Main.qml loads) -- far more reliable than
# pywinauto, which cannot see Qt-Quick windows consistently. Max time to wait
# for that line after launch (gives a human time to open the panel manually).
PANEL_READY_TIMEOUT_SEC = 90

# After the panel reports ready, time for the operator to click the chat input
# so keystrokes land in it (not the score view). Only used in "manual" mode.
INPUT_FOCUS_GRACE_SEC = 10

# Settle time after the panel is ready before the first send (non-manual modes).
# session_start fires when Main.qml loads, but the input needs a moment more to
# accept keystrokes; typing too early drops leading characters.
PANEL_SETTLE_SEC = 3.0

# ---- Panel-open strategy --------------------------------------------------
# "menu_click"    : fully hands-off. Click the menu bar to open
#                   Plugins -> AI Assistant (see MENU_* coords below). DEFAULT.
# "manual"        : pause and let the operator open Plugins -> AI Assistant.
#                   Use on an un-calibrated machine (see MENU_* recalibration).
# "menu_keyboard" : Alt+P then select "AI Assistant". DOES NOT WORK on MS4 --
#                   its QML menu bar ignores Alt mnemonics (kept for reference).
# "coords"        : click fixed screen coordinates in OPEN_PANEL_CLICKS.
OPEN_PANEL_METHOD = "menu_click"

# ---- "menu_click" calibration (CALIBRATED for a MAXIMIZED window @ 2560x1440)
# MuseScore 4's menu bar is invisible to UIA and ignores Alt-mnemonics, so the
# panel is opened by clicking the menu bar directly: click the Plugins menu,
# then click the "AI Assistant" item in the dropdown. Recalibrate the XY values
# for a different display resolution (open Plugins manually and note the pixels).
PLUGINS_MENU_XY      = (290, 16)    # the Plugins menu in the menu bar
AI_ASSISTANT_ITEM_XY = (288, 117)   # the "AI Assistant" item in the open Plugins menu

# Start a fresh conversation before each run so accumulated history (prior
# "Add a quarter note..." turns, error blocks) can't lead the model to answer
# conversationally instead of calling a tool. Clicks the "+" next to the
# "Conversations" header. The AI Assistant panel is drawn INSIDE the main window
# (not a separate OS window), so these are absolute screen coords for the
# panel's persisted geometry -- recalibrate if you resize/move the panel.
START_NEW_CONVERSATION = True
NEW_CONVERSATION_XY  = (908, 381)   # the "+" (new conversation) button

# For "menu_keyboard" (non-functional on MS4; kept for reference).
PLUGINS_MENU_MNEMONIC = "p"
AI_ASSISTANT_MENU_KEY = "a"

# For "coords": ordered list of (x, y) clicks that open the panel.
OPEN_PANEL_CLICKS = []

# Screen coords of the chat input field. The runner clicks here before typing
# each prompt to guarantee focus -- needed because starting a new conversation
# (clicking "+") moves focus off the input. Set to None to instead rely on the
# input auto-focusing on panel open (only valid if START_NEW_CONVERSATION is
# False). Calibrated for the panel's persisted geometry.
INPUT_FIELD_COORDS = (1335, 1090)

# ---------------------------------------------------------------------------
# Dependency check (GUI deps imported lazily so --self-test needs neither)
# ---------------------------------------------------------------------------
def _check_gui_deps():
    missing = []
    try:
        import pyautogui  # noqa: F401
    except Exception:
        missing.append("pyautogui")
    try:
        import pywinauto  # noqa: F401
    except Exception:
        missing.append("pywinauto")
    if missing:
        print("ERROR: missing GUI automation dependencies: " + ", ".join(missing))
        print("Install with:")
        print("    pip install pywinauto pyautogui --break-system-packages")
        print("(pywinauto: window finding; pyautogui: keyboard/mouse input)")
        sys.exit(2)


# ===========================================================================
# Log reading + event pairing  (pure logic -- exercised by --self-test)
# ===========================================================================
def get_log_offset() -> int:
    """Return current byte offset at end of debug log (0 if absent)."""
    try:
        return os.path.getsize(DEBUG_LOG)
    except OSError:
        return 0


def _read_new_events(offset: int):
    """
    Read bytes appended since `offset`, parse complete (newline-terminated)
    JSON lines, and return (events, new_offset). An incomplete trailing line
    is left unconsumed so the next read picks it up whole.
    """
    try:
        with open(DEBUG_LOG, "rb") as f:
            f.seek(offset)
            data = f.read()
    except OSError:
        return [], offset

    last_nl = data.rfind(b"\n")
    if last_nl < 0:
        return [], offset  # nothing complete yet
    consumed = data[: last_nl + 1]
    new_offset = offset + last_nl + 1

    text = consumed.decode("utf-8-sig", errors="replace")
    events = []
    for line in text.splitlines():
        line = line.strip().lstrip("﻿")
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass  # tolerate a torn line; it will re-appear complete next read
    return events, new_offset


def collect_events(since_offset: int, timeout: float = LLM_TIMEOUT_SEC,
                   settle: float = SETTLE_SEC):
    """
    Poll the log starting at `since_offset` until at least one 'result' event
    has appeared and the log has been quiet for `settle` seconds, or until
    `timeout`. Returns (events, final_offset) where events are only the
    call/result objects (session_start lines are dropped).
    """
    deadline = time.time() + timeout
    offset = since_offset
    events = []
    last_new_t = None
    saw_result = False

    while time.time() < deadline:
        new_events, offset = _read_new_events(offset)
        relevant = [e for e in new_events if ("call" in e or "result" in e)]
        if relevant:
            events.extend(relevant)
            last_new_t = time.time()
            if any("result" in e for e in relevant):
                saw_result = True
        if saw_result and last_new_t is not None and (time.time() - last_new_t) >= settle:
            break
        time.sleep(0.35)

    return events, offset


def wait_for_session_start(since_offset: int, timeout: float):
    """
    Wait for a new {"session_start":...} line to appear in the debug log after
    `since_offset`. This is the extension panel's own "loaded" signal -- the
    definitive, pywinauto-independent readiness check. Returns True if seen.
    """
    deadline = time.time() + timeout
    offset = since_offset
    while time.time() < deadline:
        events, offset = _read_new_events(offset)
        if any(isinstance(e, dict) and e.get("session_start") for e in events):
            return True
        time.sleep(0.5)
    return False


def _parse_iso(t: str) -> float:
    """ISO8601 ('...Z') -> epoch seconds. Returns 0.0 on failure."""
    if not t:
        return 0.0
    try:
        return datetime.fromisoformat(t.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return 0.0


def find_call(events, tool_name):
    """First call event whose tool name matches. `tool_name` may be a single
    name or a list/tuple of acceptable names."""
    names = tool_name if isinstance(tool_name, (list, tuple)) else [tool_name]
    for e in events:
        if e.get("call") in names:
            return e
    return None


def all_calls(events):
    return [e for e in events if "call" in e]


def all_results(events):
    return [e for e in events if "result" in e]


def pair_result_for_call(events, call_event):
    """
    Pair a result to its call. Tools execute sequentially, so a call's result is
    the chronologically next result at/after the call's timestamp -- robust when
    the LLM makes several calls in a turn (results carry no tool name). File
    order is unreliable (separate writer processes), so 't' is authoritative.
    Falls back to nearest implied call-time (result.t - ms) if nothing is after.
    """
    if not call_event:
        return None
    ct = _parse_iso(call_event.get("t", ""))
    results = [(_parse_iso(e.get("t", "")), e) for e in events if "result" in e]
    if not results:
        return None
    results.sort(key=lambda x: x[0])
    EPS = 0.5  # seconds of clock tolerance for "at/after the call"
    after = [e for (rt, e) in results if rt >= ct - EPS]
    if after:
        return after[0]
    best, best_d = None, None
    for rt, e in results:
        implied = rt - (e.get("ms", 0) or 0) / 1000.0
        d = abs(implied - ct)
        if best is None or d < best_d:
            best, best_d = e, d
    return best


# ===========================================================================
# Comparison  (pure logic -- exercised by --self-test)
# ===========================================================================
def _scalar_eq(expected, actual) -> bool:
    if isinstance(expected, bool) or isinstance(actual, bool):
        return expected is actual or expected == actual
    if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
        return expected == actual or abs(float(expected) - float(actual)) < 1e-6
    # String substring matching: if both sides are strings and the expected
    # value is not the full actual, accept if it appears as a substring.
    # This lets honest-error tests use {"error": "24673"} to match a long
    # error message that contains the bug number.
    if isinstance(expected, str) and isinstance(actual, str):
        return expected == actual or expected in actual
    return expected == actual


def subset_match(expected, actual) -> bool:
    """
    Recursive subset match: every key in an expected dict must be present in
    actual with a subset-matching value; every element of an expected list must
    subset-match SOME element of the actual list; scalars compare with a small
    numeric tolerance.
    """
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return False
        for k, v in expected.items():
            if k not in actual:
                return False
            if not subset_match(v, actual[k]):
                return False
        return True
    if isinstance(expected, list):
        if not isinstance(actual, list):
            return False
        for ev in expected:
            if not any(subset_match(ev, av) for av in actual):
                return False
        return True
    return _scalar_eq(expected, actual)


def find_anywhere(expected_dict, actual) -> bool:
    """
    True if any object nested anywhere within `actual` subset-matches
    `expected_dict`. Lets a "contains" entry match an element inside a nested
    array (e.g. a note inside result["notes"]) or the result dict itself.
    """
    if subset_match(expected_dict, actual):
        return True
    if isinstance(actual, dict):
        return any(find_anywhere(expected_dict, v) for v in actual.values())
    if isinstance(actual, list):
        return any(find_anywhere(expected_dict, v) for v in actual)
    return False


def compare_result(actual: dict, expected: dict):
    """
    Check that `actual` is a recursive superset of `expected`.
    Returns (passed, reason).
    """
    if actual is None:
        return False, "no result captured"
    if subset_match(expected, actual):
        return True, "result matched expected subset"
    # Build a focused reason: report the first failing key.
    if isinstance(expected, dict) and isinstance(actual, dict):
        for k, v in expected.items():
            if k not in actual:
                return False, f"expected key '{k}' missing from result"
            if not subset_match(v, actual[k]):
                return False, f"key '{k}': expected {v!r}, got {actual[k]!r}"
    return False, f"result {actual!r} did not match expected {expected!r}"


# ===========================================================================
# GUI automation  (lazy imports; not needed for --self-test)
# ===========================================================================
_pyautogui = None
_pywinauto = None
_ms_window = None   # cached MuseScore window handle, for re-foregrounding before sends


def _gui():
    """Import and configure pyautogui/pywinauto once."""
    global _pyautogui, _pywinauto
    if _pyautogui is None:
        import pyautogui
        pyautogui.FAILSAFE = True       # slam mouse to a corner to abort
        pyautogui.PAUSE = 0.05
        _pyautogui = pyautogui
    if _pywinauto is None:
        import pywinauto
        _pywinauto = pywinauto
    return _pyautogui, _pywinauto


def clear_session_state():
    """
    Empty MuseScore's open-scores list (session.json) so the next launch does
    NOT show the 'previous session quit unexpectedly' recovery dialog -- a side
    effect of force-killing MuseScore. Only the open-projects list is reset; no
    user score is touched. Writing the empty-array form MuseScore itself uses
    avoids any parse-error logging on its side.
    """
    try:
        p = Path(SESSION_STATE_FILE)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("[\n]\n", encoding="utf-8")
    except Exception as e:  # noqa: BLE001
        print(f"  [warn] could not clear session state ({SESSION_STATE_FILE}): {e}")


def launch_musescore(score_path: str) -> subprocess.Popen:
    """Launch MuseScore4.exe with score_path. Return the Popen handle."""
    clear_session_state()  # suppress the recovery dialog from a prior force-kill
    print(f"  launching MuseScore with {score_path}")
    return subprocess.Popen([MUSESCORE_EXE, score_path])


def try_get_musescore_window(proc, timeout: float):
    """
    Return a pywinauto handle for MuseScore's main window, found by PROCESS ID
    (proc.pid) -- the window title is the score name (e.g. "empty_4_4"), not
    "MuseScore", so title matching is unreliable. Picks the largest visible
    top-level window owned by the process (ignores the splash). Returns None on
    failure; on failure prints visible windows for diagnosis.
    """
    _, pywinauto = _gui()
    from pywinauto import Desktop
    pid = getattr(proc, "pid", None)
    deadline = time.time() + timeout
    while time.time() < deadline:
        best, best_area = None, -1
        try:
            for w in Desktop(backend="uia").windows():
                try:
                    if pid is not None and w.process_id() != pid:
                        continue
                    if not w.is_visible():
                        continue
                    r = w.rectangle()
                    area = max(0, r.width()) * max(0, r.height())
                    if area > best_area:
                        best, best_area = w, area
                except Exception:  # noqa: BLE001
                    continue
        except Exception:  # noqa: BLE001
            pass
        if best is not None and best_area > 100_000:  # skip tiny splash windows
            return best
        time.sleep(0.5)
    # Diagnostics: what top-level windows CAN we see?
    for backend in ("uia", "win32"):
        try:
            titles = [w.window_text() for w in Desktop(backend=backend).windows()]
            titles = [t for t in titles if t]
            print(f"  [warn] no MuseScore window (pid {pid}) via {backend}; visible: "
                  + ", ".join(repr(t) for t in titles)[:600])
        except Exception as e:  # noqa: BLE001
            print(f"  [warn] window enumeration ({backend}) failed: {e}")
    return None


def find_panel_window(proc, main_win):
    """
    After the panel opens, find the AI Assistant dialog window: a visible
    top-level window owned by the MuseScore process that is SMALLER than the
    main (maximized) score window. The chat input lives in this dialog, so sends
    must foreground IT, not the main window (foregrounding main steals focus
    from the dialog input). Returns None if not found.
    """
    _, pywinauto = _gui()
    from pywinauto import Desktop
    pid = getattr(proc, "pid", None)
    main_area = -1
    if main_win is not None:
        try:
            r = main_win.rectangle()
            main_area = max(0, r.width()) * max(0, r.height())
        except Exception:  # noqa: BLE001
            pass
    cands = []
    try:
        for w in Desktop(backend="uia").windows():
            try:
                if pid is not None and w.process_id() != pid:
                    continue
                if not w.is_visible():
                    continue
                r = w.rectangle()
                a = max(0, r.width()) * max(0, r.height())
                cands.append((a, w))
            except Exception:  # noqa: BLE001
                continue
    except Exception:  # noqa: BLE001
        return None
    cands.sort(key=lambda t: t[0], reverse=True)
    for a, w in cands:
        # smaller than the maximized main window, but a real panel (not a tooltip)
        if (main_area <= 0 or a < main_area) and a > 50_000:
            return w
    return None


def _focus_window(win):
    if win is None:
        return
    try:
        win.set_focus()
    except Exception:  # noqa: BLE001
        try:
            win.restore()
            win.set_focus()
        except Exception:  # noqa: BLE001
            pass
    time.sleep(0.5)


def open_extension_panel(win):
    """Open Plugins -> AI Assistant. Strategy per OPEN_PANEL_METHOD."""
    pyautogui, _ = _gui()
    _focus_window(win)

    if OPEN_PANEL_METHOD == "manual":
        # No blind wait here: run_test_file waits for the panel's session_start
        # log line, so it proceeds the instant the panel actually opens.
        print("\n  >>> MANUAL STEP: in MuseScore, open  Plugins -> AI Assistant,")
        print("  >>> then click in the chat input box at the bottom of the panel.",
              flush=True)
        return

    if OPEN_PANEL_METHOD == "menu_click":
        # Hands-off: click the Plugins menu, then the AI Assistant item.
        # Two direct clicks -- no arrow keys (arrow-nav between top menus is
        # state-dependent on MS4). See the calibration notes above.
        pyautogui.press("escape")
        time.sleep(0.3)
        pyautogui.click(*PLUGINS_MENU_XY)
        time.sleep(0.9)
        pyautogui.click(*AI_ASSISTANT_ITEM_XY)
        time.sleep(1.0)
        return

    if OPEN_PANEL_METHOD == "menu_keyboard":
        # Alt + mnemonic opens the Plugins menu, first-letter picks the item.
        pyautogui.keyDown("alt")
        time.sleep(0.1)
        pyautogui.press(PLUGINS_MENU_MNEMONIC)
        pyautogui.keyUp("alt")
        time.sleep(0.6)
        pyautogui.press(AI_ASSISTANT_MENU_KEY)
        time.sleep(0.3)
        pyautogui.press("enter")
        time.sleep(1.0)
        return

    if OPEN_PANEL_METHOD == "coords":
        if not OPEN_PANEL_CLICKS:
            raise RuntimeError("OPEN_PANEL_METHOD='coords' but OPEN_PANEL_CLICKS is empty")
        for (x, y) in OPEN_PANEL_CLICKS:
            pyautogui.click(x, y)
            time.sleep(0.6)
        return

    raise ValueError(f"unknown OPEN_PANEL_METHOD: {OPEN_PANEL_METHOD!r}")


def _focus_and_type(text: str):
    """Bring MuseScore forward, focus the chat input, clear it, and type `text`
    (without pressing Enter)."""
    pyautogui, _ = _gui()
    # Re-foreground the AI Assistant dialog (set as _ms_window after the panel
    # opens) so keystrokes land in its input. _focus_window already pauses ~0.5s.
    if _ms_window is not None:
        _focus_window(_ms_window)
        time.sleep(0.3)   # extra settle so leading keys aren't dropped
    if INPUT_FIELD_COORDS:
        pyautogui.click(*INPUT_FIELD_COORDS)
        time.sleep(0.3)
    # Warm-up keystroke: the first key after (re)focus is sometimes swallowed.
    # A throwaway space absorbs that, then select-all + delete clears it plus any
    # residual text (Ctrl+A / Delete are handled by the input's Keys.onPressed).
    pyautogui.press("space")
    time.sleep(0.12)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.12)
    pyautogui.press("delete")
    time.sleep(0.15)
    pyautogui.typewrite(text, interval=TYPE_INTERVAL)
    time.sleep(0.15)


def start_new_conversation():
    """Click the '+' next to 'Conversations' to start a fresh chat, so prior
    history can't bias the model away from calling tools."""
    pyautogui, _ = _gui()
    pyautogui.click(*NEW_CONVERSATION_XY)
    time.sleep(1.0)


def send_and_wait(before_offset: int, prompt: str,
                  timeout: float = LLM_TIMEOUT_SEC, settle: float = SETTLE_SEC):
    """
    Type `prompt` into the chat, then press Enter repeatedly until the message
    actually sends and a tool call appears, collecting events until they settle.

    The extension ignores Enter/sendMessage while isStreaming is true (the
    nav-send handler and sendMessage both guard on it), and a blocked send does
    NOT clear the input -- so the typed text persists and a later Enter sends
    it once streaming ends. Re-pressing Enter on an already-sent (now empty)
    input is a guarded no-op, so this never double-sends.

    Returns (events, final_offset).
    """
    pyautogui, _ = _gui()
    _focus_and_type(prompt)

    deadline = time.time() + timeout
    offset = before_offset
    events = []
    last_new_t = None
    saw_call = False
    saw_result = False
    next_enter = 0.0

    while time.time() < deadline:
        # Nudge: keep pressing Enter until the send takes (a call appears).
        if not saw_call and time.time() >= next_enter:
            if _ms_window is not None:
                _focus_window(_ms_window)
            pyautogui.press("enter")
            next_enter = time.time() + NUDGE_ENTER_SEC

        new_events, offset = _read_new_events(offset)
        relevant = [e for e in new_events if ("call" in e or "result" in e)]
        if relevant:
            events.extend(relevant)
            last_new_t = time.time()
            if any("call" in e for e in relevant):
                saw_call = True
            if any("result" in e for e in relevant):
                saw_result = True
        if saw_result and last_new_t is not None and (time.time() - last_new_t) >= settle:
            break
        time.sleep(0.35)

    return events, offset


def close_musescore(proc: subprocess.Popen):
    """Force-close MuseScore. We force-kill to skip the unsaved-changes dialog;
    the score under test is a throwaway temp copy."""
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", "MuseScore4.exe", "/T"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
        )
    except Exception:  # noqa: BLE001
        pass
    try:
        proc.terminate()
    except Exception:  # noqa: BLE001
        pass
    # Give the OS a moment so the next launch starts a fresh single instance.
    time.sleep(3.0)
    # Wipe the leftover open-scores list so neither the next spec nor a manual
    # MuseScore launch shows the "previous session quit unexpectedly" dialog.
    clear_session_state()


def save_failure_screenshot(tag: str) -> str:
    """
    Save a full-screen screenshot so a failure can be diagnosed by eye -- e.g.
    distinguishing a harness problem (prompt not typed/sent) from a backend
    problem (the chat shows an LLM API error like HTTP 500 / OVERLOADED, which
    the extension does NOT write to the debug log). Returns the path or a note.
    """
    try:
        pyautogui, _ = _gui()
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = os.path.join(tempfile.gettempdir(),
                            f"aiastest_fail_{tag}_{ts}.png")
        pyautogui.screenshot().save(path)
        return path
    except Exception as e:  # noqa: BLE001
        return f"(screenshot failed: {e})"


# ===========================================================================
# Step / verify execution
# ===========================================================================
def run_step(step: dict, index: int, spec_name: str, verbose: bool):
    """Run one step. Returns (passed, line, detail_lines)."""
    prompt = step["prompt"]
    expect_tool = step.get("expect_tool")
    expect_result = step.get("expect_result")
    expect_keys = step.get("expect_result_contains_keys")  # list[str] presence check
    verify = step.get("verify")
    label = f"{spec_name} / step {index}"

    detail = []
    needs_result = (expect_result is not None) or bool(expect_keys)
    events, call, result_value = [], None, None

    # Retry loop: the extension's debug logger writes each line via a separate
    # PowerShell process, and back-to-back call+result writes occasionally race
    # and drop the result line. So if a tool call is seen but no result is
    # captured (or no call at all), re-send the prompt once. The prompts here are
    # idempotent writes (overwrite / update-in-place), so re-sending is safe.
    for attempt in range(max(1, STEP_ATTEMPTS)):
        before = get_log_offset()
        events, _ = send_and_wait(before, prompt, timeout=LLM_TIMEOUT_SEC)
        calls = all_calls(events)
        call = find_call(events, expect_tool) if expect_tool else (calls[0] if calls else None)
        result_event = pair_result_for_call(events, call) if call else None
        result_value = result_event.get("result") if result_event else None
        if (call is not None and (result_value is not None or not needs_result)) \
                or attempt == max(1, STEP_ATTEMPTS) - 1:
            break
        detail.append(f"       (attempt {attempt + 1}: "
                      f"{'no tool call' if call is None else 'call seen but result line dropped'}"
                      f" -- retrying)")

    if verbose:
        detail.append(f'       prompt:   "{prompt}"')
        for e in events:
            detail.append("       log:      " + json.dumps(e, ensure_ascii=False))

    calls = all_calls(events)
    if not calls:
        shot = save_failure_screenshot(f"{spec_name}_step{index}")
        detail = detail + [
            f"       (no tool call -- check the panel for an LLM API error, "
            f"e.g. HTTP 500/OVERLOADED, which is NOT logged)",
            f"       screenshot: {shot}",
        ]
        return False, f"[FAIL] {label}: no tool call seen within {LLM_TIMEOUT_SEC}s", detail

    if expect_tool and call is None:
        got = ", ".join(c.get("call", "?") for c in calls) or "none"
        line = (f"[FAIL] {label}: expected tool '{expect_tool}', got '{got}'")
        detail = [f'       prompt:   "{prompt}"',
                  f"       expected: {expect_tool}",
                  f"       actual:   {got}"] + detail
        return False, line, detail
    if call is None:
        call = calls[0]

    tool = call.get("call")

    # expect_result subset check
    if expect_result is not None:
        ok, reason = compare_result(result_value, expect_result)
        if not ok:
            return (False,
                    f"[FAIL] {label}: {tool} result check failed -- {reason}",
                    detail)

    # presence-of-keys check (e.g. honest-error tests expecting an 'error' key)
    if expect_keys:
        if not isinstance(result_value, dict):
            return (False,
                    f"[FAIL] {label}: {tool} result is not an object; "
                    f"cannot check keys {expect_keys}", detail)
        missing = [k for k in expect_keys if k not in result_value]
        if missing:
            return (False,
                    f"[FAIL] {label}: {tool} result missing expected key(s) "
                    f"{missing}; got keys {list(result_value.keys())}", detail)

    # optional verification follow-up
    if verify:
        vok, vreason = run_verify(verify, verbose, detail)
        if not vok:
            return False, f"[FAIL] {label}: {tool} ok, but verify failed -- {vreason}", detail
        return (True,
                f"[PASS] {label}: {tool} matched; verify ok -- {vreason}", detail)

    summary = _short(result_value)
    return True, f"[PASS] {label}: {tool} -> {summary}", detail


def run_verify(verify: dict, verbose: bool, detail: list):
    """Send a verification prompt, capture a read-tool result, check `contains`."""
    vprompt = verify["prompt"]
    vtool = verify.get("tool") or verify.get("expect_tool")
    contains = verify.get("contains", [])

    before = get_log_offset()
    events, _ = send_and_wait(before, vprompt, timeout=LLM_TIMEOUT_SEC)

    if verbose:
        detail.append(f'       verify:   "{vprompt}"')
        for e in events:
            detail.append("       v-log:    " + json.dumps(e, ensure_ascii=False))

    calls = all_calls(events)
    if not calls:
        shot = save_failure_screenshot("verify")
        detail.append(f"       verify screenshot: {shot}")
        return False, (f"verify produced no tool call within {LLM_TIMEOUT_SEC}s "
                       f"(possible LLM API error; screenshot: {shot})")

    if vtool:
        call = find_call(events, vtool)
        if call is None:
            got = ", ".join(c.get("call", "?") for c in calls) or "none"
            return False, f"verify expected tool '{vtool}', got '{got}'"
    else:
        # accept any read result; prefer the call paired to a result
        call = calls[-1]

    result_event = pair_result_for_call(events, call)
    result_value = result_event.get("result") if result_event else None
    if result_value is None:
        return False, "verify produced no result value"

    for want in contains:
        if not find_anywhere(want, result_value):
            return False, f"expected {want!r} not found in {_short(result_value)}"
    return True, f"all {len(contains)} expected item(s) found in {call.get('call')} result"


def _short(value, limit: int = 160) -> str:
    s = json.dumps(value, ensure_ascii=False)
    return s if len(s) <= limit else s[: limit - 3] + "..."


# ===========================================================================
# Spec running
# ===========================================================================
def run_test_file(spec_path: str, verbose: bool, stop_on_fail: bool):
    """Load a spec, launch MuseScore, run all steps. Returns (passed, failed)."""
    with open(spec_path, "r", encoding="utf-8") as f:
        spec = json.load(f)

    spec_name = spec.get("name", Path(spec_path).stem)
    score_file = spec["score"]
    src_score = os.path.join(TEST_SCORES_DIR, score_file)
    if not os.path.isfile(src_score):
        print(f"[ERROR] {spec_name}: score not found: {src_score}")
        return 0, len(spec.get("steps", []))

    # Copy the score to a temp path so the original is never modified.
    import tempfile
    tmp_dir = tempfile.mkdtemp(prefix="aiastest_")
    tmp_score = os.path.join(tmp_dir, score_file)
    shutil.copy2(src_score, tmp_score)

    print(f"\n--- {spec_name}: {spec.get('description', '')}")
    proc = None
    passed = failed = 0
    results = []
    try:
        global _ms_window
        log_offset_before = get_log_offset()
        proc = launch_musescore(tmp_score)
        # Best-effort foreground handle; the run does NOT depend on finding it,
        # but if found it is reused to re-foreground MuseScore before each send.
        win = try_get_musescore_window(proc, MS_LAUNCH_TIMEOUT_SEC)
        _ms_window = win
        if win is not None:
            try:
                win.maximize()   # predictable geometry for menu navigation
            except Exception:  # noqa: BLE001
                pass
            _focus_window(win)
            print("  MuseScore window found and foregrounded")
        else:
            print("  [warn] MuseScore window handle not found; "
                  "menu/coords open may not land in the right window")
        open_extension_panel(win)

        # Definitive readiness: the panel writes a session_start log line on load.
        if wait_for_session_start(log_offset_before, PANEL_READY_TIMEOUT_SEC):
            print("  panel ready (session_start seen)")
        else:
            print(f"  [warn] no session_start within {PANEL_READY_TIMEOUT_SEC}s; "
                  "proceeding anyway")

        # The chat input lives in a separate floating dialog. Target THAT window
        # for foregrounding before sends -- foregrounding the main score window
        # would steal focus from the input. If found, the input is its
        # auto-focused child; if not, clear _ms_window so sends do NOT foreground
        # (the dialog keeps focus right after opening).
        panel = find_panel_window(proc, win)
        if panel is not None:
            _ms_window = panel
            _focus_window(panel)
            print("  AI Assistant dialog located")
        else:
            _ms_window = None
            print("  [warn] AI Assistant dialog window not found; "
                  "relying on auto-focus (no re-foreground)")

        # Start a fresh conversation so accumulated history doesn't bias the
        # model into answering conversationally instead of calling tools.
        if START_NEW_CONVERSATION and OPEN_PANEL_METHOD != "manual":
            start_new_conversation()
            print("  started a new conversation")

        # session_start fires when Main.qml loads, but the input needs a moment
        # more before it reliably accepts keystrokes -- typing too early drops
        # the leading characters and truncates the prompt. Settle first.
        if OPEN_PANEL_METHOD == "manual":
            print(f"  grace: {INPUT_FOCUS_GRACE_SEC}s for you to click the chat input...",
                  flush=True)
            time.sleep(INPUT_FOCUS_GRACE_SEC)
        else:
            time.sleep(PANEL_SETTLE_SEC)

        for i, step in enumerate(spec.get("steps", []), start=1):
            ok, line, detail = run_step(step, i, spec_name, verbose)
            results.append((ok, line, detail))
            if ok:
                passed += 1
            else:
                failed += 1
            print(line)
            for d in detail:
                print(d)
            if not ok and stop_on_fail:
                break
    finally:
        if proc is not None:
            close_musescore(proc)
        shutil.rmtree(tmp_dir, ignore_errors=True)

    return passed, failed


def gather_specs(path: str):
    p = Path(path)
    if p.is_dir():
        return sorted(str(x) for x in p.glob("*.json"))
    return [str(p)]


# ===========================================================================
# Self-test  (no MuseScore, no API -- validates pure logic + the live log)
# ===========================================================================
def self_test():
    print("=== self-test: pure logic + live-log parsing (no GUI/API) ===")
    ok = True

    def check(name, cond):
        nonlocal ok
        print(("  [ok]   " if cond else "  [FAIL] ") + name)
        ok = ok and cond

    # subset_match
    check("subset dict matches superset",
          subset_match({"ok": True, "measure": 1},
                       {"ok": True, "measure": 1, "bpm": 120}))
    check("subset dict rejects mismatch",
          not subset_match({"bpm": 120}, {"bpm": 96}))
    check("subset numeric tolerance",
          subset_match({"bpm": 120}, {"bpm": 120.0000001}))
    check("nested dict subset",
          subset_match({"location": {"measure": 1}},
                       {"location": {"measure": 1, "beat": 1}}))

    # find_anywhere against a real get_notes_in_range-shaped result
    notes_result = {"ok": True,
                    "notes": [{"noteName": "A4",
                               "location": {"measure": 1, "beat": 1}}],
                    "rests": []}
    check("find_anywhere finds note in nested array",
          find_anywhere({"noteName": "A4"}, notes_result))
    check("find_anywhere honours nested location",
          find_anywhere({"noteName": "A4", "location": {"measure": 1}}, notes_result))
    check("find_anywhere rejects absent note",
          not find_anywhere({"noteName": "B4"}, notes_result))

    # pairing by timestamp, including out-of-file-order lines
    events = [
        {"t": "2026-05-20T06:19:42.132Z", "result": {"ok": True, "bpm": 120}, "ms": 72},
        {"t": "2026-05-20T06:19:42.060Z", "call": "add_tempo_mark", "args": {"bpm": 120}},
    ]
    call = find_call(events, "add_tempo_mark")
    res = pair_result_for_call(events, call)
    check("pair_result_for_call matches by timestamp despite file order",
          res is not None and res.get("result", {}).get("bpm") == 120)

    # compare_result reason text
    p, reason = compare_result({"ok": True, "bpm": 96}, {"bpm": 120})
    check("compare_result reports failing key", (not p) and "bpm" in reason)

    # live-log parse: read the tail of the real debug log if present
    if os.path.isfile(DEBUG_LOG):
        size = get_log_offset()
        start = max(0, size - 200_000)
        evs, _ = _read_new_events(start)
        n_calls = len([e for e in evs if "call" in e])
        n_res = len([e for e in evs if "result" in e])
        print(f"  [info] parsed live log tail: {n_calls} call(s), {n_res} result(s)")
        check("live log tail parsed without crashing", True)
        # spot-check pairing on the last call in the tail
        last_calls = [e for e in evs if "call" in e]
        if last_calls:
            c = last_calls[-1]
            r = pair_result_for_call(evs, c)
            print(f"  [info] last call '{c.get('call')}' paired to result: "
                  f"{_short(r.get('result') if r else None)}")
    else:
        print(f"  [info] live log not found at {DEBUG_LOG} (skipping log parse)")

    print("=== self-test: " + ("ALL PASS ===" if ok else "FAILURES ==="))
    return ok


# ===========================================================================
# main
# ===========================================================================
def main():
    ap = argparse.ArgumentParser(description="ai-assistant extension test runner")
    ap.add_argument("path", nargs="?",
                    help="a test spec .json file or a directory of them")
    ap.add_argument("--stop-on-fail", action="store_true",
                    help="stop a spec at the first failing step")
    ap.add_argument("--verbose", action="store_true",
                    help="print full log entries for each step")
    ap.add_argument("--self-test", action="store_true",
                    help="validate pure logic + live-log parsing; no MuseScore/API")
    ap.add_argument("--open-method",
                    choices=["menu_click", "manual", "menu_keyboard", "coords"],
                    help="override OPEN_PANEL_METHOD for this run")
    args = ap.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    global OPEN_PANEL_METHOD
    if args.open_method:
        OPEN_PANEL_METHOD = args.open_method
        print(f"  open-panel method: {OPEN_PANEL_METHOD}")

    if not args.path:
        ap.error("a spec file/dir is required (or use --self-test)")

    _check_gui_deps()

    specs = gather_specs(args.path)
    if not specs:
        print(f"no .json specs found at {args.path}")
        sys.exit(1)

    print(f"=== ai-assistant test run -- {datetime.now().isoformat(timespec='seconds')} ===")
    total_pass = total_fail = 0
    for spec_path in specs:
        try:
            p, f = run_test_file(spec_path, args.verbose, args.stop_on_fail)
        except Exception as e:  # noqa: BLE001
            print(f"[ERROR] {spec_path}: {e}")
            p, f = 0, 1
        total_pass += p
        total_fail += f
        if f and args.stop_on_fail:
            break

    total = total_pass + total_fail
    print(f"\n=== Results: {total_pass} passed, {total_fail} failed ({total} total) ===")
    sys.exit(0 if total_fail == 0 else 1)


if __name__ == "__main__":
    main()
