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
  * It covers the TEXT-UTILITY half, and — since 2026-08-03 — `git status`.  The rest of the
    rule's other half, `git log` and `git rev-parse HEAD`, is still deliberately NOT enforced.
    Blocking those would fire on ordinary git use that the rule's own scope note leaves to
    judgment, and a control that fires on legitimate use gets switched off, which is the worst
    outcome of the three.  **`git status` became separable from them on 2026-08-03**, when the
    user ruled the enumeration tool built (`tools/audit/changed_paths.py`, phase-1s Y1): there
    is now a sanctioned way to ask which paths changed, so denying the raw command costs no
    legitimate work.  A command naming the enumeration tool is exempt, so the guard cannot deny
    the thing that makes it affordable.
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
import shlex
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

# `git status` — denied since 2026-08-03 (user ruling Y1, phase 1s). The rule names it among the
# commands never trusted for what is current, and until the enumeration tool existed there was
# no sanctioned way to answer the question it was being used for, so denying it would have been
# the "fires on legitimate work" failure. `tools/audit/changed_paths.py` is that way, so the raw
# command now costs nothing. `git log` and `git rev-parse HEAD` stay unblocked: no tool replaces
# them, and the reasoning that admits `git status` does not reach them.
GIT_STATUS = re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?status\b")

# The sanctioned enumeration must never be denied by the guard that makes it necessary.
ENUMERATION_TOOL = "changed_paths.py"

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


def tokenize(segment: str, group_quotes: bool = True) -> list[str]:
    """Split a segment into words, keeping a QUOTED argument as ONE word.

    A plain `.split()` splits inside quotes, so `grep -c "^  D-" file` became five tokens and
    its fragment `D-"` was then read as a repository path — a FALSE DENY, measured live on
    2026-08-03 and recorded at `OPEN_ITEMS.md` OI-292. `shlex` in NON-posix mode is what fixes
    it: it groups quoted arguments and, unlike posix mode, leaves backslashes alone, so a
    Windows path such as `C:\\s\\MS` survives tokenization intact. Quotes stay attached to the
    token and `outside_repo` strips them exactly as it already did.

    A malformed command (an unbalanced quote) falls back to `.split()` rather than raising: a
    guard that crashes on a strange command is a guard that stops guarding.
    """
    if not group_quotes:                    # the superseded behaviour, kept for --establish
        return segment.split()
    try:
        return shlex.split(segment, posix=False)
    except ValueError:
        return segment.split()


def decide(command: str, group_quotes: bool = True) -> tuple[bool, str]:
    """(deny, reason). A command is denied when a text utility names a repository path."""
    if ENUMERATION_TOOL in command:
        return False, ("runs the sanctioned changed-path enumeration "
                       "(`tools/audit/changed_paths.py`)")
    if GIT_OBJECT_READ.search(command):
        # The whole command is a git-object pipeline; a text utility downstream of it is
        # formatting object output, not reading the working tree.
        return False, "reads a git object by explicit hash — the sanctioned exemption"
    if GIT_STATUS.search(command):
        return True, ("`git status` is not trusted for what is current — `CLAUDE.md` "
                      "Conventions, register entry D-253. The sanctioned way to enumerate "
                      "which paths changed is `python tools/audit/changed_paths.py` "
                      "(`--staged`, or `--commit <hash>`), which reports paths and status "
                      "codes and cannot return file content.")
    for seg in split_segments(command):
        tokens = tokenize(seg, group_quotes)
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
    # ADDED 2026-08-03 (phase 1s). THE MEASURED FALSE DENY this wave was dispatched to fix
    # (`OPEN_ITEMS.md` OI-292, the phase-1r note): a quoted grep pattern containing a space.
    # It is a real command this repository issued, so it belongs in the sanctioned set whether
    # or not the guard gets it right — a corpus chosen to make a guard look clean measures
    # nothing (#19).
    "grep -c \"^  D-\" /tmp/reaim_1r.txt",
    # The sanctioned enumeration, which the guard must never deny.
    "python tools/audit/changed_paths.py --staged",
    "python tools/audit/changed_paths.py --commit 32d9b47933",
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
    # ADDED 2026-08-03 (phase 1s). The branch-tip/index form the enumeration tool now replaces,
    # in the shapes it actually arrives in — including the one that was issued live and NOT
    # denied while the guard was armed (`OPEN_ITEMS.md` OI-292, the phase-1r note).
    "git status --porcelain",
    "git status",
    "cd C:\\s\\MS && git status --short",
    # A quoted pattern aimed at a REPOSITORY path: the tokenizer fix must not turn the false
    # deny it removes into a false NEGATIVE here.
    "grep -n \"Full spec:\" ARCHITECTURE.md > /tmp/spec.txt",
]


def establish() -> dict:
    san = [{"command": c, "denied": decide(c)[0], "reason": decide(c)[1]} for c in SANCTIONED]
    forb = [{"command": c, "denied": decide(c)[0], "reason": decide(c)[1]} for c in FORBIDDEN]
    false_denies = sum(1 for r in san if r["denied"])
    caught = sum(1 for r in forb if r["denied"])
    # The 2026-08-03 tokenizer change is maintenance on a KEPT mechanism (D-436), so it is
    # RE-established rather than asserted: the same two sets are run with quote grouping off
    # and on, and both figures are published. The dispatch's condition for reverting it is a
    # rise in false denies elsewhere, so that figure must be visible and not inferred.
    old_false = sum(1 for c in SANCTIONED if decide(c, group_quotes=False)[0])
    old_caught = sum(1 for c in FORBIDDEN if decide(c, group_quotes=False)[0])
    return {
        "purpose": "Establishment (#19) of tools/audit/shell_read_guard.py: its deny rate on "
                   "the forms CLAUDE.md names, and its FALSE-deny rate on real commands this "
                   "repository issues. A guard that fires on legitimate use gets switched off, "
                   "so the false-deny rate is the figure that decides whether it may be armed.",
        "coverage_limits": [
            "Project-scoped: it binds sessions that run in this directory and read this "
            "project's settings. Whether the WRITING side does is not established, so the rule "
            "must not be described as enforced for both sides.",
            "The text-utility half, plus `git status` since 2026-08-03. The REST of D-253's "
            "branch-tip/index half — `git log`, `git rev-parse HEAD` — is still deliberately "
            "not enforced: no tool replaces them, so denying them would fire on legitimate "
            "work, which is the ground on which `git status` was left unblocked until the "
            "enumeration tool existed.",
            "Declared, not fired: a settings file naming the hook is evidence it is declared. "
            "`tools/audit/guard_armed_check.py` reports that much and says so.",
            "disableAllHooks and managed allowManagedHooksOnly switch it off. A guard, not a "
            "boundary.",
        ],
        "sanctioned": {"total": len(san), "false_denies": false_denies,
                       "false_deny_rate": round(false_denies / len(san), 3), "rows": san},
        "forbidden": {"total": len(forb), "denied": caught,
                      "deny_rate": round(caught / len(forb), 3), "rows": forb},
        "changes_2026_08_03_phase_1s": {
            "git_status_is_now_denied": {
                "what_changed": "`git status` in any segment is denied; `git log` and `git "
                                "rev-parse HEAD` are not.",
                "why_it_became_affordable": "Until 2026-08-03 there was no sanctioned way to "
                                            "answer the question `git status` was being used "
                                            "for, so denying it would have been the "
                                            "fires-on-legitimate-work failure. "
                                            "`tools/audit/changed_paths.py` is that way (user "
                                            "ruling Y1, phase 1s), and a command naming it is "
                                            "exempt, so the guard cannot deny the thing that "
                                            "makes it affordable.",
                "the_instance_it_closes": "A `git status --porcelain` issued while the guard "
                                          "was armed was NOT denied — the guard behaving as "
                                          "designed and the rule broken anyway "
                                          "(`OPEN_ITEMS.md` OI-292, the phase-1r note).",
            },
            "the_tokenizer_fix": {
                "what_changed": "A segment is split with `shlex` in NON-posix mode, so a "
                                "quoted argument stays one token. Non-posix specifically: "
                                "posix mode would eat the backslashes in a Windows path such "
                                "as `C:\\s\\MS`. A malformed command falls back to `.split()` "
                                "rather than raising.",
                "the_false_deny_it_removes": "`grep -c \"^  D-\" /tmp/reaim_1r.txt` was "
                                             "denied: `.split()` broke the quoted pattern into "
                                             "two tokens and read the fragment `D-\"` as a "
                                             "repository path. Measured live 2026-08-03 and "
                                             "recorded at `OPEN_ITEMS.md` OI-292.",
                "false_denies_on_the_sanctioned_set": {
                    "with_the_fix": false_denies, "without_it": old_false, "of": len(san)},
                "detection_on_the_forbidden_set": {
                    "with_the_fix": caught, "without_it": old_caught, "of": len(forb)},
                "the_revert_condition": "The dispatch says: if the fix raises false denies "
                                        "elsewhere, revert and report. Compare the two figures "
                                        "above — a rise is the condition, and it is published "
                                        "either way rather than inferred.",
            },
        },
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
