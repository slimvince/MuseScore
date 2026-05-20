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
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Configuration  (edit here)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent

MUSESCORE_EXE   = r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"
DEBUG_LOG       = r"C:\Users\vince\AppData\Local\MuseScore\MuseScore4\logs\ai-assistant-debug.log"
TEST_SCORES_DIR = str(SCRIPT_DIR / "test_scores")
TESTS_DIR       = str(SCRIPT_DIR / "tests")

# How long to wait for each LLM response (seconds). LLM calls typically 3-8s,
# but a multi-tool turn (read then write) can chain, so allow headroom.
LLM_TIMEOUT_SEC = 45

# How long to wait for MuseScore to start and load a score (seconds).
MS_LAUNCH_TIMEOUT_SEC = 30

# Delay between keystrokes when typing prompts (seconds). Increase if MS eats chars.
TYPE_INTERVAL = 0.05

# After the last new log line appears, wait this long with no further lines
# before deciding a step's tool activity is finished (handles multi-tool turns).
SETTLE_SEC = 2.5

# Substring used to find the MuseScore main window title.
WINDOW_TITLE_RE = "MuseScore"

# ---- Panel-open strategy --------------------------------------------------
# "manual"        : pause and ask the operator to open Plugins -> AI Assistant
#                   and click the chat input, then press Enter in the console.
#                   Most robust for an un-calibrated machine / first run.
# "menu_keyboard" : Alt+P to open the Plugins menu, then select "AI Assistant".
#                   Works only if MS4's menu bar honours Alt mnemonics.
# "coords"        : click fixed screen coordinates (calibrate OPEN_PANEL_CLICKS).
OPEN_PANEL_METHOD = "manual"

# For "menu_keyboard": the mnemonic letter of the Plugins menu ("&Plugins").
PLUGINS_MENU_MNEMONIC = "p"
# After the Plugins menu opens, the key(s) that select the AI Assistant item.
# The item label is "AI Assistant"; first-letter selection usually picks it.
AI_ASSISTANT_MENU_KEY = "a"

# For "coords": ordered list of (x, y) clicks that open the panel
# (e.g. [(plugins_menu_x, plugins_menu_y), (ai_assistant_item_x, item_y)]).
OPEN_PANEL_CLICKS = []

# Optional: screen coords of the chat input field. If None, send_prompt assumes
# the input already has focus (true right after the panel opens, since the
# TextField has focus:true). Set this if focus is unreliable on your machine.
INPUT_FIELD_COORDS = None

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


def _parse_iso(t: str) -> float:
    """ISO8601 ('...Z') -> epoch seconds. Returns 0.0 on failure."""
    if not t:
        return 0.0
    try:
        return datetime.fromisoformat(t.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return 0.0


def find_call(events, tool_name):
    """First call event with matching tool name, else None."""
    for e in events:
        if e.get("call") == tool_name:
            return e
    return None


def all_calls(events):
    return [e for e in events if "call" in e]


def all_results(events):
    return [e for e in events if "result" in e]


def pair_result_for_call(events, call_event):
    """
    Pair a result to its call by timestamp: a result logged at result.t with
    elapsed `ms` came from a call at approximately (result.t - ms/1000). Pick
    the result whose implied call-time is closest to this call's timestamp.
    File order is unreliable (separate writer processes), so we use 't'.
    """
    if not call_event:
        return None
    ct = _parse_iso(call_event.get("t", ""))
    best, best_d = None, None
    for e in events:
        if "result" not in e:
            continue
        rt = _parse_iso(e.get("t", ""))
        ms = e.get("ms", 0) or 0
        implied_call_t = rt - (ms / 1000.0)
        d = abs(implied_call_t - ct)
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


def launch_musescore(score_path: str) -> subprocess.Popen:
    """Launch MuseScore4.exe with score_path. Return the Popen handle."""
    print(f"  launching MuseScore with {score_path}")
    return subprocess.Popen([MUSESCORE_EXE, score_path])


def wait_for_musescore_window(timeout: float):
    """
    Poll until a MuseScore main window exists and looks ready. Returns the
    pywinauto WindowSpecification. Raises TimeoutError on failure.
    """
    _, pywinauto = _gui()
    from pywinauto import Desktop
    deadline = time.time() + timeout
    last_err = None
    while time.time() < deadline:
        try:
            desk = Desktop(backend="uia")
            win = desk.window(title_re=f".*{WINDOW_TITLE_RE}.*")
            if win.exists() and win.is_visible():
                return win
        except Exception as e:  # noqa: BLE001
            last_err = e
        time.sleep(0.5)
    raise TimeoutError(f"MuseScore window not ready within {timeout}s (last: {last_err})")


def _focus_window(win):
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
        print("\n  >>> MANUAL STEP: in MuseScore, open  Plugins -> AI Assistant,")
        print("  >>> then click in the chat input box at the bottom of the panel.")
        input("  >>> Press Enter here once the chat input is focused... ")
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


def wait_for_extension_ready():
    """
    The panel opens with its chat TextField focus:true, so there is no robust
    cross-process handle to test (Qt Quick controls are invisible to UIA).
    Give the QML form a moment to finish loading and registering navigation.
    """
    time.sleep(1.5)


def send_prompt(text: str):
    """Focus the chat input (if coords known), clear it, type text, press Enter."""
    pyautogui, _ = _gui()
    if INPUT_FIELD_COORDS:
        pyautogui.click(*INPUT_FIELD_COORDS)
        time.sleep(0.2)
    # Clear any residual text: select-all then delete (both handled by the
    # input's Keys.onPressed Ctrl+A / Delete interceptors).
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.05)
    pyautogui.press("delete")
    time.sleep(0.05)
    pyautogui.typewrite(text, interval=TYPE_INTERVAL)
    time.sleep(0.1)
    pyautogui.press("enter")


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

    before = get_log_offset()
    send_prompt(prompt)
    events, after = collect_events(before, timeout=LLM_TIMEOUT_SEC)

    detail = []
    if verbose:
        detail.append(f'       prompt:   "{prompt}"')
        for e in events:
            detail.append("       log:      " + json.dumps(e, ensure_ascii=False))

    calls = all_calls(events)
    if not calls:
        return False, f"[FAIL] {label}: no tool call seen within {LLM_TIMEOUT_SEC}s", detail

    # Resolve which call we assert against.
    if expect_tool:
        call = find_call(events, expect_tool)
        if call is None:
            got = ", ".join(c.get("call", "?") for c in calls) or "none"
            line = (f"[FAIL] {label}: expected tool '{expect_tool}', got '{got}'")
            detail = [f'       prompt:   "{prompt}"',
                      f"       expected: {expect_tool}",
                      f"       actual:   {got}"] + detail
            return False, line, detail
    else:
        call = calls[0]

    result_event = pair_result_for_call(events, call)
    result_value = result_event.get("result") if result_event else None
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
    send_prompt(vprompt)
    events, _ = collect_events(before, timeout=LLM_TIMEOUT_SEC)

    if verbose:
        detail.append(f'       verify:   "{vprompt}"')
        for e in events:
            detail.append("       v-log:    " + json.dumps(e, ensure_ascii=False))

    calls = all_calls(events)
    if not calls:
        return False, f"verify produced no tool call within {LLM_TIMEOUT_SEC}s"

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
        proc = launch_musescore(tmp_score)
        win = wait_for_musescore_window(MS_LAUNCH_TIMEOUT_SEC)
        time.sleep(2.0)  # let the score finish loading
        open_extension_panel(win)
        wait_for_extension_ready()

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
    args = ap.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

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
