#!/usr/bin/env python3
"""Is the shell-read guard ARMED? — the control that puts an untracked control into the record.

WHAT THIS IS.  Task 4 of the phase-1q wave
(`cc_instruction_phase1q_reclassification_and_guards.md` §5), on the user's ruling of
2026-08-03 (X4): arm the shell-read guard, and put a CHECK in the record that verifies it is
armed.

WHY IT EXISTS, which is the whole design point.  `tools/audit/shell_read_guard.py` enforces the
file-tools rule (register entry **D-253**) as a `PreToolUse` hook.  Arming it means one block in
`.claude/settings.json` — and this repository's `.gitignore` puts that file outside the record
as "Claude Code local session state".  A live control that exists only in an untracked file is
the `OPEN_ITEMS.md` OI-285 class exactly: a change on disk and not in the record, which no later
reader can find and no commit can revert.  That objection is what kept the guard unarmed at
phase 1p.

This check answers it without tracking session state and without hard-coding a machine-specific
path into the repository: **the CONTROL enters the record, and the machine-specific settings
file stays out of it.**  What is committed is the requirement and the test of it; what stays
local is the one block that satisfies the test.

WHAT IT CHECKS, and what it cannot.
  * It reads the settings files a session in this directory would read, and reports whether any
    of them declares a `PreToolUse` hook that runs `shell_read_guard.py`, and whether hooks are
    globally switched off (`disableAllHooks`).
  * It CANNOT observe a running session.  A settings file naming the hook is evidence the hook
    is declared, not proof it fired: the settings watcher only reloads directories that held a
    settings file when the session started, so a newly added hook may need `/hooks` opened once.
    That limit is stated in `shell_read_guard.py` itself and is not restated as a figure here.
  * It says nothing about the WRITING side.  Whether that side runs as a session in this
    directory is not established, so an ARMED result must not be read as the rule being
    enforced for both sides.

EXPECTED STATE AT DELIVERY: **NOT ARMED**, and that is the delivered outcome, not a defect.
Arming is the user's act on the user's machine; until it is done this check exits non-zero and
prints the arming block — read verbatim from `shell_read_guard.py`'s own docstring, never
retyped, so the two cannot drift apart.  `STATUS.md` records it as the one expected-failing
guard, and `OPEN_ITEMS.md` OI-292 carries the arming as owed until it is done.

Run:
    python tools/audit/guard_armed_check.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
GUARD = os.path.join(HERE, "shell_read_guard.py")
GUARD_REL = "tools/audit/shell_read_guard.py"

# The settings files a session running in this directory reads, in the order the harness
# resolves them.  The user-level file is included because arming there would also arm this
# directory, and reporting it as unarmed would then be wrong.
def settings_paths() -> list[str]:
    home = os.path.expanduser("~")
    return [
        os.path.join(ROOT, ".claude", "settings.json"),
        os.path.join(ROOT, ".claude", "settings.local.json"),
        os.path.join(home, ".claude", "settings.json"),
    ]


def arming_block() -> str:
    """The block to paste, taken from the guard's own docstring.

    Read from the file rather than repeated here: two copies of one instruction is the
    duplication that goes stale, and this one would go stale silently.
    """
    lines = open(GUARD, encoding="utf-8").read().splitlines()
    start = next((i for i, ln in enumerate(lines) if '"hooks": { "PreToolUse"' in ln), None)
    if start is None:
        raise SystemExit(f"{GUARD_REL}: the arming block is no longer in its docstring — this "
                         "check reads it from there and will not invent one")
    out = []
    for ln in lines[start:]:
        if not ln.strip():
            break
        out.append(ln)
    return "\n".join(out)


def hooks_naming_the_guard(obj) -> list[str]:
    """Every string anywhere under a PreToolUse hook declaration that names the guard."""
    found: list[str] = []

    def walk(node, path):
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, path + [str(k)])
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, path + [str(i)])
        elif isinstance(node, str):
            if "shell_read_guard" in node and "PreToolUse" in path:
                found.append(".".join(path) + " = " + node)

    walk(obj, [])
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.parse_args()

    if not os.path.exists(GUARD):
        print(f"NOT ARMED — {GUARD_REL} is not present at all.")
        return 1

    armed_at: list[tuple[str, list[str]]] = []
    disabled_at: list[str] = []
    read: list[str] = []
    unreadable: list[tuple[str, str]] = []

    for path in settings_paths():
        rel = os.path.relpath(path, ROOT) if path.startswith(ROOT) else path
        if not os.path.exists(path):
            continue
        read.append(rel)
        try:
            obj = json.loads(open(path, encoding="utf-8").read())
        except Exception as exc:                      # a malformed settings file is not armed
            unreadable.append((rel, str(exc)))
            continue
        if obj.get("disableAllHooks"):
            disabled_at.append(rel)
        hits = hooks_naming_the_guard(obj)
        if hits:
            armed_at.append((rel, hits))

    print("settings files read: " + (", ".join(read) if read else "none found"))
    for rel, exc in unreadable:
        print(f"  UNREADABLE: {rel} — {exc}")
    for rel in disabled_at:
        print(f"  hooks are globally disabled by {rel} (disableAllHooks)")

    if armed_at and not disabled_at:
        for rel, hits in armed_at:
            print(f"  declared in {rel}:")
            for h in hits:
                print(f"      {h}")
        print("ARMED — a PreToolUse hook runs the shell-read guard.")
        print("Coverage limits stand and are stated in the guard itself: the text-utility half "
              "only, sessions in this directory only, and a declaration is not proof the hook "
              "fired.")
        return 0

    if armed_at and disabled_at:
        print("NOT ARMED — the hook is declared but hooks are globally disabled.")
        return 1

    print("NOT ARMED — no settings file declares a PreToolUse hook running the shell-read guard.")
    print("")
    print("This is the EXPECTED state until the user arms it; arming is the user's act on the "
          "user's machine, and the file it goes in is outside the record by `.gitignore`.")
    print("The block, read from the guard's own docstring — paste it into "
          "`.claude/settings.json`, replacing <repo> with this repository's absolute path:")
    print("")
    print(arming_block())
    print("")
    print("Then open `/hooks` once: the settings watcher only reloads directories that held a "
          "settings file when the session started.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
