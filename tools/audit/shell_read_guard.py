#!/usr/bin/env python3
"""Deny shell text-utility reads of working-tree files — the file-tools rule, made mechanical.

WHAT THIS IS.  Mechanism 1 of the phase-1p wave
(`cc_instruction_phase1p_home_rulings_and_mechanisms.md` §6.1).  `CLAUDE.md` Conventions carry
a user mandate (register entry **D-253**, 2026-06-21): working-tree file content, existence,
line counts and searches go through the file tools, never through shell text utilities; shell
access is for read-only git OBJECT queries named by an explicit commit hash.  Its defense is a
measured failure — a stale mount made the shell path return wrong content and raise a false
corruption alarm while the file tools read the live disk correctly.

The rule has been prose only.  This makes the half the dispatch names mechanical: a
`PreToolUse` hook on the shell tools reads the command, and DENIES it when a text utility is
aimed at a path inside this repository.

FEASIBILITY, ESTABLISHED BEFORE BUILDING (the dispatch's own instruction).  From the harness's
own settings schema: `hooks.PreToolUse` accepts a `matcher` on tool names, a command hook
receives the tool input as JSON on stdin (`tool_input.command`), and a PreToolUse hook denies by
emitting `hookSpecificOutput.permissionDecision = "deny"` with a
`permissionDecisionReason`.  A hook declared in `.claude/settings.json` is project-scoped.

WHAT IT COVERS, AND WHAT IT DOES NOT — stated plainly, because a control believed to be in place
and not in place is worse than none (#19):

  * It covers sessions that run in THIS project directory and read this project's settings.  The
    rule binds both the writing side and the executing side; whether the writing side runs as a
    session in this directory is NOT established here, so **the rule must not be described as
    enforced for both sides**.
  * It covers the TEXT-UTILITY half only.  The rule's other half — that a branch-tip or index
    read (`git status`, `git log`, `git rev-parse HEAD`) is never trusted for what is current —
    is deliberately NOT enforced.  Blocking those would fire on ordinary git use that the rule's
    own scope note leaves to judgment, and a control that fires on legitimate use gets switched
    off, which is the worst outcome of the three.
  * `disableAllHooks`, and managed settings with `allowManagedHooksOnly`, switch it off. It is a
    guard, not a boundary.

IT IS NOT ARMED, AND THE REASON IS THE PROJECT'S OWN STANDARD.  Arming it means one block in
`.claude/settings.json` — and this repository's `.gitignore:112` puts that file outside the
record, as "Claude Code local session state".  A live control that exists only in an untracked
file is the `OPEN_ITEMS.md` OI-285 class exactly: a change on disk and not in the record, which
no later reader can find and no commit can revert.  So the guard is delivered COMMITTED and
ESTABLISHED, and arming it is left as the user's act.  The block, verbatim, inside `.claude/
settings.json`:

    "hooks": { "PreToolUse": [ { "matcher": "Bash|PowerShell", "hooks": [
      { "type": "command", "command": "python",
        "args": ["<repo>/tools/audit/shell_read_guard.py"],
        "statusMessage": "file-tools rule (D-253)" } ] } ] }

Two things to know before arming.  The settings watcher only reloads directories that held a
settings file when the session started, so a newly added hook may need `/hooks` opened once.
And the `args` exec form takes an absolute path, so a tracked form of this block would need one
that is not machine-specific — which is part of why whether `.claude/settings.json` should be
tracked at all is a question for the user rather than a thing to decide by force-adding it.

ESTABLISHMENT (#19).  `--establish` runs the decision over a corpus of real commands — the ones
this session actually issued, plus the forbidden forms `CLAUDE.md` itself names — and reports
the deny rate on the forbidden set and the false-deny rate on the sanctioned set.  The artifact
is `tools/audit/shell_read_guard_establishment.json`.

Run:
    echo '{"tool_input":{"command":"cat CLAUDE.md"}}' | python tools/audit/shell_read_guard.py
    python tools/audit/shell_read_guard.py --establish [--check]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ESTABLISH_OUT = os.path.join(HERE, "shell_read_guard_establishment.json")

# The utilities `CLAUDE.md` names, plus the obvious siblings of each.
TEXT_UTILITIES = {
    "cat", "head", "tail", "sed", "awk", "grep", "egrep", "fgrep", "rg", "wc",
    "less", "more", "nl", "cut", "sort", "uniq", "strings", "od", "xxd", "tac", "type",
}

# A read of a git OBJECT by explicit hash is self-verifying — it errors loudly rather than
# returning silently-wrong content — which is exactly why the rule exempts it.
GIT_OBJECT_READ = re.compile(
    r"\bgit\s+(?:-C\s+\S+\s+)?(?:show|cat-file|diff)\b[^|;&]*\b[0-9a-f]{7,40}\b")

ENV_ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
OPTION = re.compile(r"^-")

# Paths that are not this repository's working tree, so a text utility aimed at them is
# reading something else and the rule does not reach it.
def outside_repo(token: str) -> bool:
    t = token.strip("'\"")
    if not t or t.startswith("-"):
        return True
    low = t.replace("\\", "/").lower()
    if low.startswith("/dev/") or low in ("-", "/dev/null"):
        return True
    for marker in ("/tmp/", "/temp/", "appdata/local/temp", "/scratchpad/"):
        if marker in low:
            return True
    if low.startswith("/tmp") or low.startswith("c:/tmp"):
        return True
    if os.path.isabs(t):
        try:
            return os.path.commonpath([os.path.abspath(t), ROOT]) != ROOT
        except ValueError:              # different drives
            return True
    return False


def split_segments(command: str) -> list[str]:
    """Pipeline and list segments, keeping the pipeline they came from for the git exemption."""
    return [s for s in re.split(r"\|\||&&|[;|\n]", command) if s.strip()]


def decide(command: str) -> tuple[bool, str]:
    """(deny, reason). A command is denied when a text utility names a repository path."""
    if GIT_OBJECT_READ.search(command):
        # The whole command is a git-object pipeline; a text utility downstream of it is
        # formatting object output, not reading the working tree.
        return False, "reads a git object by explicit hash — the sanctioned exemption"
    for seg in split_segments(command):
        tokens = seg.split()
        i = 0
        while i < len(tokens) and ENV_ASSIGN.match(tokens[i]):
            i += 1
        if i >= len(tokens):
            continue
        util = os.path.basename(tokens[i].strip("'\"")).lower()
        if util.endswith(".exe"):
            util = util[:-4]
        if util not in TEXT_UTILITIES:
            continue
        targets = [t for t in tokens[i + 1:] if not OPTION.match(t)]
        # `grep PATTERN file` — the first non-option token is the pattern, not a path.
        if util in ("grep", "egrep", "fgrep", "rg") and targets:
            targets = targets[1:]
        inside = [t for t in targets if not outside_repo(t)]
        if inside:
            return True, (f"`{util}` is aimed at a path inside this repository "
                          f"({', '.join(inside[:3])}). Working-tree content, existence, line "
                          "counts and searches go through the file tools (Read / Grep / Glob) — "
                          "`CLAUDE.md` Conventions, register entry D-253. Shell reads are for "
                          "read-only git OBJECT queries by explicit hash.")
    return False, "no text utility is aimed at a repository path"


# ── establishment (#19) ──────────────────────────────────────────────────────
# SANCTIONED: real commands issued in this repository, which must NOT be denied.
SANCTIONED = [
    "python tools/audit/decisions/gen_phase1p_delegation_bar.py",
    "PYTHONIOENCODING=utf-8 python tools/audit/process_check.py --establish",
    "cd C:\\s\\MS && python tools/open_items_split_check.py > /tmp/split_1p.txt 2>&1",
    "git show ccc3086ab3:cowork_joint_key_chord_design.md 2>&1 | head -20",
    "git show --stat 41f7c65f63",
    "git diff 41f7c65f63 ccc3086ab3 -- docs/scoring_model.md | head -40",
    "head -50 /tmp/snap_out.txt",
    "tail -14 \"C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/x/scratchpad/est.txt\"",
    "./composing_tests.exe; echo \"exit:$?\"",
    "powershell.exe -Command \"Start-Process 'C:\\s\\MS\\setup_and_build.bat' -Wait -NoNewWindow\"",
    "git commit -m 'docs(cowork): phase 1p'",
    "echo \"exit:$?\"",
]

# FORBIDDEN: the forms `CLAUDE.md` itself names as the rule's target.
FORBIDDEN = [
    "cat CLAUDE.md",
    "grep -n \"pattern\" src/composing/chordanalyzer.cpp",
    "head -50 ARCHITECTURE.md",
    "tail -20 tools/audit/decisions/backbone_decisions.json",
    "sed -n '1,20p' STATUS.md",
    "wc -l OPEN_ITEMS.md",
    "rg --files-with-matches 'delegation' open_items/",
    "cat C:/s/MS/DECISIONS.md",
]


def establish() -> dict:
    san = [{"command": c, "denied": decide(c)[0], "reason": decide(c)[1]} for c in SANCTIONED]
    forb = [{"command": c, "denied": decide(c)[0], "reason": decide(c)[1]} for c in FORBIDDEN]
    false_denies = sum(1 for r in san if r["denied"])
    caught = sum(1 for r in forb if r["denied"])
    return {
        "purpose": "Establishment (#19) of tools/audit/shell_read_guard.py: its deny rate on "
                   "the forms CLAUDE.md names, and its FALSE-deny rate on real commands this "
                   "repository issues. A guard that fires on legitimate use gets switched off, "
                   "so the false-deny rate is the figure that decides whether it may be armed.",
        "coverage_limits": [
            "Project-scoped: it binds sessions that run in this directory and read this "
            "project's settings. Whether the WRITING side does is not established, so the rule "
            "must not be described as enforced for both sides.",
            "The text-utility half only. The branch-tip/index half of D-253 (git status, git "
            "log, git rev-parse HEAD are never trusted for what is current) is deliberately "
            "not enforced.",
            "disableAllHooks and managed allowManagedHooksOnly switch it off. A guard, not a "
            "boundary.",
        ],
        "sanctioned": {"total": len(san), "false_denies": false_denies,
                       "false_deny_rate": round(false_denies / len(san), 3), "rows": san},
        "forbidden": {"total": len(forb), "denied": caught,
                      "deny_rate": round(caught / len(forb), 3), "rows": forb},
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--establish", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    if args.establish:
        art = establish()
        text = json.dumps(art, indent=2, ensure_ascii=False) + "\n"
        if args.check:
            have = open(ESTABLISH_OUT, encoding="utf-8").read() \
                if os.path.exists(ESTABLISH_OUT) else ""
            if have != text:
                print("STALE: shell_read_guard_establishment.json does not re-derive")
                return 1
            print("the shell-read-guard establishment artifact re-derives")
            return 0
        open(ESTABLISH_OUT, "w", encoding="utf-8", newline="").write(text)
        s, f = art["sanctioned"], art["forbidden"]
        print(f"wrote {os.path.relpath(ESTABLISH_OUT, ROOT)}")
        print(f"  forbidden forms denied: {f['denied']}/{f['total']}")
        for r in f["rows"]:
            if not r["denied"]:
                print(f"    MISSED: {r['command']}")
        print(f"  FALSE denies on sanctioned commands: {s['false_denies']}/{s['total']}")
        for r in s["rows"]:
            if r["denied"]:
                print(f"    FALSE DENY: {r['command']}")
        return 0

    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0                        # never block on a malformed payload
    command = (payload.get("tool_input") or {}).get("command") or ""
    deny, reason = decide(command)
    if deny:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
