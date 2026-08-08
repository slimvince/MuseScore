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
  * It covers the TEXT-UTILITY half in BOTH shell dialects it is armed on — POSIX from the
    start, and PowerShell since 2026-08-08 (`OPEN_ITEMS.md` OI-345, user ruling R1 of
    2026-08-07).  Until that date the utility set was POSIX-only while the hook matcher named
    both tools, so the PowerShell spelling of the same read was admitted.  What a name set
    cannot reach is a command carried INSIDE a quoted argument — `powershell.exe -Command
    "<cmdlet> <repository path>"` is still admitted, is in the corpus, and is rowed.
  * It covers — since 2026-08-03 — `git status`.  The rest of the
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

  ★ THE CORPUS IS EXTENDED BEFORE ANY RATE IS REPUBLISHED (user ruling R1, 2026-08-04; the same
  order ruled again for the PowerShell dialect on 2026-08-07 and applied 2026-08-08).  A
  measured rate is only as wide as the corpus it was measured on, so a shape that defeats the
  guard goes into the corpus FIRST and the rates are then re-measured against it.  Re-establishing
  a repaired guard against the corpus that failed to catch the defect repeats the error being
  fixed: the check passes precisely because the shape is absent.  Both figures are published for
  every change, measured on the SAME corpus, so what is reported is the change's effect and not
  the widening's.

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

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# The utilities `CLAUDE.md` names, plus the obvious siblings of each.
TEXT_UTILITIES = {
    "cat", "head", "tail", "sed", "awk", "grep", "egrep", "fgrep", "rg", "wc",
    "less", "more", "nl", "cut", "sort", "uniq", "strings", "od", "xxd", "tac", "type",
}

# ── the PowerShell dialect, added 2026-08-08 (`OPEN_ITEMS.md` OI-345, user ruling R1) ─────────
# The set above is POSIX-only, and the guard is armed on the PowerShell tool by design. The
# membership rule is the same one that built the set above: the commands that perform one of the
# four acts D-253 names — content, existence, line counts, searches — on a path argument. The
# aliases are read out of PowerShell's own alias table (`Get-Alias -Definition <cmdlet>`); the
# sourcing command, the version it was run on and why the version is pinned are recorded with the
# corpus rows below, once (#6).
#
# `cat` and `type` are aliases of `Get-Content` and are NOT repeated here: they are already in
# the POSIX set under the same spelling, and a name in both sets would have to pick one of the
# two candidate-selection paths below for no gain.
POWERSHELL_UTILITIES = {
    "get-content", "gc",
    "select-string", "sls",
    "get-childitem", "gci", "ls", "dir",
    "get-item", "gi",
    "test-path",
    "resolve-path", "rvpa",
    "measure-object", "measure",
    "import-csv", "ipcsv",
    "import-clixml",
}

# The parameters that NAME a path in this family. PowerShell binds a path either by one of these
# or positionally, never both at once, which is what makes the selection below decidable.
PS_PATH_PARAMETERS = {"-path", "-literalpath", "-filepath"}

# The two members whose FIRST positional argument is not a path: `Select-String`'s is the pattern
# and `Measure-Object`'s is the property name. This is the same special case the POSIX branch
# already makes for `grep` and its siblings, and it is what keeps a pipeline-fed
# `Select-String -Pattern 'FAIL'` from being read as a read of a repository file named `FAIL` —
# the OI-292 false-deny shape, which this dialect would otherwise reproduce.
PS_FIRST_POSITIONAL_IS_NOT_A_PATH = {"select-string", "sls", "measure-object", "measure"}


def powershell_targets(util: str, after_util: list[str]) -> list[str]:
    """The tokens of a PowerShell reading command that could be a path, and no others.

    DERIVED FROM THE CMDLETS' DOCUMENTED PARAMETER POSITIONS, not from what makes the corpus
    pass: every member of the family takes its path either as the value of `-Path` /
    `-LiteralPath` / `-FilePath` or as its FIRST positional argument, so those are the only two
    places a path can be. Everything else is a named parameter's value — `-TotalCount 20`,
    `-Filter *.md`, `-Pattern 'FAIL'` — and reading one of those as a path is the false deny that
    gets a guard switched off.

    THE LIMIT, STATED RATHER THAN LEFT TO BE FOUND: only the first positional argument is
    considered, so a second working-tree path in a multi-path form (`Get-Content a.md, b.md`) is
    covered only through the first. The verdict is the same for the shapes this corpus carries;
    a form whose ONLY repository path is a later positional argument would be missed.
    """
    named: list[str] = []
    positional: list[str] = []
    i = 0
    while i < len(after_util):
        tok = after_util[i]
        if OPTION.match(tok):
            if tok.lower() in PS_PATH_PARAMETERS and i + 1 < len(after_util) \
                    and not OPTION.match(after_util[i + 1]):
                named.append(after_util[i + 1])
                i += 2
                continue
            i += 1
            continue
        positional.append(tok)
        i += 1
    if named:                       # a named path was given; positional binding cannot also apply
        return named
    if util in PS_FIRST_POSITIONAL_IS_NOT_A_PATH:
        positional = positional[1:]
    return positional[:1]

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
#
# THE TEST IS ON THE SUBCOMMAND'S POSITION, NOT ON THE PHRASE ANYWHERE IN THE COMMAND — the same
# shape the text-utility test already uses, and not a special case bolted on. A pattern search
# over the whole command was tried first and produced a FALSE DENY the moment it was armed: a
# `git commit` whose message QUOTES this very rule was blocked, because the words "git status"
# appear in the prose. A commit message, a heredoc body and a quoted argument are all text, and
# the guard must read what is being RUN.
def git_status_invocation(rest: list[str]) -> bool:
    """True when the words after `git` are an actual `status` invocation."""
    j = 0
    if j < len(rest) and rest[j] == "-C":
        j += 2
    while j < len(rest) and rest[j].startswith("-"):
        j += 1
    return j < len(rest) and rest[j].strip("'\"") == "status"

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
    """SUPERSEDED 2026-08-04. The raw-text segment split, kept ONLY for --establish's comparison.

    It cut the command into segments BEFORE anything was tokenized, so a separator inside a
    quoted argument was read as a real one. See `lex_command` below for the defect and the fix.
    """
    return [s for s in re.split(r"\|\||&&|[;|\n]", command) if s.strip()]


# ── segmentation, corrected 2026-08-04 (`OPEN_ITEMS.md` OI-343, user ruling R1) ───────────────
# THE DEFECT, measured at this module's own decision function and never reasoned from its source:
# the segment split above ran over the RAW command text while `tokenize()` applied `shlex` PER
# SEGMENT. A `|` inside a QUOTED pattern was therefore taken for a pipeline separator, the command
# was shredded at the alternation, and the segment carrying the repository path no longer began
# with the text utility — so the utility test never saw the path. `grep -n "alpha|beta"
# src/composing/analysis/key/keyresolver.cpp` was ADMITTED while the identical command without the
# pipe was DENIED.
#
# It is the OI-292/OI-300 lesson — a raw split splits inside quotes — ONE FUNCTION UPSTREAM of the
# one that was fixed, and it fails in the opposite direction: that remedy stopped the guard denying
# legitimate work, this one stops it admitting forbidden work.
#
# THE FIX IS THE ORDER, not a wider pattern. The whole command is lexed ONCE, with the shell's own
# list and pipeline operators recognised as tokens in their own right, and the segments are cut at
# those TOKENS. A quoted argument is a single token before any cut is made, so no separator inside
# one can be mistaken for a separator between commands.
#
# WHY THE PUNCTUATION SET IS `;|&\n` RATHER THAN shlex's default `();<>|&`: the default also turns
# every redirection into its own token (`2>&1` becomes `2`, `>&`, `1`), which changes which token
# the guard classifies as the aimed path — a SECOND behaviour change, on OI-300's shape (5), that
# this act is not authorized to make. The set here is exactly the characters the superseded regex
# cut on, so the only behaviour that moves is WHERE the segment boundaries fall.
SEGMENT_PUNCTUATION = ";|&\n"

# A separator token is one composed only of the operators the superseded regex treated as
# separators: `||`, `&&`, `;`, `|`, newline. A LONE `&` is deliberately NOT one — the superseded
# regex did not treat it as one either, and treating it so would cut `2>&1` in half.
SEPARATOR_TOKEN = re.compile(r"(?:\|\||&&|[;|\n])+")


def lex_command(command: str) -> list[str] | None:
    """Every token of the WHOLE command, quotes respected, operators kept as their own tokens.

    Returns None for a command `shlex` cannot lex (an unbalanced quote), so the caller falls back
    to the superseded raw split rather than raising: a guard that crashes on a strange command is
    a guard that stops guarding — the same reason `tokenize()` carries its own fallback.
    """
    lex = shlex.shlex(command, posix=False, punctuation_chars=SEGMENT_PUNCTUATION)
    lex.whitespace_split = True
    # `\n` is deliberately NOT whitespace here: a newline separates commands, so it has to reach
    # the punctuation test rather than be eaten as a space — the superseded regex split on it too.
    lex.whitespace = " \t\r"
    # A `#` inside a command is data, never a comment. `shlex.split` clears this for the same
    # reason; constructing the lexer directly does not, so it is cleared explicitly.
    lex.commenters = ""
    try:
        return list(lex)
    except ValueError:
        return None


def segments(command: str, group_quotes: bool = True,
             token_first: bool = True) -> list[list[str]]:
    """The command's segments, each as a token list."""
    if token_first:
        tokens = lex_command(command)
        if tokens is not None:
            out: list[list[str]] = []
            cur: list[str] = []
            for tok in tokens:
                if SEPARATOR_TOKEN.fullmatch(tok):
                    if cur:
                        out.append(cur)
                    cur = []
                else:
                    cur.append(tok)
            if cur:
                out.append(cur)
            return out
    return [tokenize(s, group_quotes) for s in split_segments(command)]


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


def decide(command: str, group_quotes: bool = True, token_first: bool = True,
           dialect: bool = True) -> tuple[bool, str]:
    """(deny, reason). A command is denied when a text utility names a repository path.

    `dialect=False` restores the POSIX-only utility set the guard carried before 2026-08-08. It
    exists so `--establish` can publish both arms on the SAME corpus, which is the only way the
    widening's effect is separable from the corpus extension's (D-436).
    """
    if GIT_OBJECT_READ.search(command):
        # The whole command is a git-object pipeline; a text utility downstream of it is
        # formatting object output, not reading the working tree.
        return False, "reads a git object by explicit hash — the sanctioned exemption"
    exempt = False
    for tokens in segments(command, group_quotes, token_first):
        # The enumeration exemption is judged PER SEGMENT, never over the whole command: a
        # whole-command exemption would let `cat CLAUDE.md; python …/changed_paths.py` through
        # on the strength of its second half.
        if any(ENUMERATION_TOOL in t for t in tokens):
            exempt = True
            continue
        i = 0
        while i < len(tokens) and ENV_ASSIGN.match(tokens[i]):
            i += 1
        if i >= len(tokens):
            continue
        util = os.path.basename(tokens[i].strip("'\"")).lower()
        if util.endswith(".exe"):
            util = util[:-4]
        if util == "git" and git_status_invocation(tokens[i + 1:]):
            return True, ("`git status` is not trusted for what is current — `CLAUDE.md` "
                          "Conventions, register entry D-253. The sanctioned way to enumerate "
                          "which paths changed is `python tools/audit/changed_paths.py` "
                          "(`--staged`, or `--commit <hash>`), which reports paths and status "
                          "codes and cannot return file content.")
        if dialect and util in POWERSHELL_UTILITIES:
            # The PowerShell branch selects candidates by that dialect's own parameter model;
            # the POSIX branch below is untouched by it (the dispatch's assumption A2).
            targets = powershell_targets(util, tokens[i + 1:])
        elif util in TEXT_UTILITIES:
            targets = [t for t in tokens[i + 1:] if not OPTION.match(t)]
            # `grep PATTERN file` — the first non-option token is the pattern, not a path.
            if util in ("grep", "egrep", "fgrep", "rg") and targets:
                targets = targets[1:]
        else:
            continue
        inside = [t for t in targets if not outside_repo(t)]
        if inside:
            return True, (f"`{util}` is aimed at a path inside this repository "
                          f"({', '.join(inside[:3])}). Working-tree content, existence, line "
                          "counts and searches go through the file tools (Read / Grep / Glob) — "
                          "`CLAUDE.md` Conventions, register entry D-253. Shell reads are for "
                          "read-only git OBJECT queries by explicit hash.")
    if exempt:
        return False, ("runs the sanctioned changed-path enumeration "
                       "(`tools/audit/changed_paths.py`), and no other segment is denied")
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
    # A SECOND MEASURED FALSE DENY, live, in the same wave that added the `git status` rule: a
    # commit whose message QUOTES the rule was blocked, because a pattern search over the whole
    # command cannot tell prose from an invocation. Fixed by testing the subcommand's POSITION.
    "git commit -q -m 'the `git status` denial is now affordable'",
    "git commit -q -F -",
    "echo 'denying `git status` costs nothing now' > /tmp/note.txt",
    # ── ADDED 2026-08-04 (`cc_instruction_guard_fix_and_item1d.md`, Task 1.2, user ruling R1) ──
    # THE CORPUS IS EXTENDED BEFORE ANY RATE IS RE-MEASURED, and the reason is R1's own: the
    # committed `--establish --check` passed precisely BECAUSE the corpus omitted the shape that
    # defeats the guard, so the published rates did not bound what they appeared to bound.
    # Re-establishing against the same corpus would repeat the error being fixed.
    #
    # (a) THE CONTROL FOR THE FIX. The same quoted-pipe shape aimed OUTSIDE the tree. The
    # segmentation fix must not turn a miss into a false deny here.
    "grep -nE \"alpha|beta\" /tmp/scratch.txt",
    "grep -n \"D-642\\|D-643\" /tmp/reaim_1r.txt",
    # (b) OI-300's OWN SHAPES, each a MEASURED false deny recorded on that row and NOT fixed here.
    # They are in the corpus so the published false-deny rate REPORTS them instead of being
    # silent about them; the fix's effect is read as the with/without delta on this same corpus.
    # Shape (2) — an unexpanded shell variable pointing outside the working tree.
    "tail \"$SC/guards1.txt\"",
    # Shape (5) — a redirection token taken for the aimed path, beside an out-of-tree argument.
    "cat \"$SC/tasks/abc.output\" 2>/dev/null | tail -20",
    # Shape (4) — a heredoc BODY line that begins with a forbidden word and is not a command.
    "python - <<'PYEOF'\nhead = old[:k]\nPYEOF",
    # Redirections beside out-of-tree arguments, the forms OI-300 names.
    "head -20 /tmp/out.txt 2>/dev/null",
    "tail -5 /tmp/out.txt 2>&1",
    "cat /tmp/a.txt >> /tmp/b.txt",
    # (c) THE HASH-BEARING GIT FORMS D-253 EXPLICITLY PERMITS, which no fix may start denying.
    "git cat-file -p 4a9c0d4827",
    "git show 4a9c0d4827:cowork_audit_protocol.md",
    # (d) BUILD, TEST AND MEASUREMENT COMMANDS `BUILD_AND_TEST.md` MANDATES. They are not reads at
    # all, and a guard that denied one would stop the work the rule exists to protect.
    "python tools/audit/gen_guard_state.py --check",
    "cd C:\\s\\MS\\ninja_build_rel && ./composing_tests.exe",
    "python tools/a8_rebaseline_measure.py --out-dir /tmp/cand",
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
    # The BYPASS the enumeration exemption would open if it were judged over the whole command
    # instead of per segment. Found by re-reading the diff before committing, not by a report.
    "cat CLAUDE.md; python tools/audit/changed_paths.py --staged",
    "python tools/audit/changed_paths.py --staged && head -50 ARCHITECTURE.md",
    # ── ADDED 2026-08-04 (`cc_instruction_guard_fix_and_item1d.md`, Task 1.2, user ruling R1) ──
    # THE SHAPE THAT DEFEATED THE GUARD, in the forms it was measured in. The first is Cowork's
    # own run against the guard's decision path (the dispatch's fact F1); the four that follow are
    # commands the preceding session ACTUALLY ISSUED and the guard ADMITTED (`OPEN_ITEMS.md`
    # OI-343). Every one is the read D-253 forbids.
    "grep -n \"alpha|beta\" src/composing/analysis/key/keyresolver.cpp",
    "grep -nE \"summaris|recognis\" tools/audit/gen_guard_state.py cowork_audit_protocol.md",
    "grep -nEi \"carrier|successors s\" tools/audit/gen_phase1_completion_inventory.py",
    "grep -n \"carrier\\|carries the live content\" STATUS.md",
    "grep -n \"D-642\\|D-643\" DECISIONS.md",
    # The same shape inside a REAL pipeline: a fix must protect the quoted pipe AND still cut the
    # command at the genuine one, so the second segment is decided rather than swallowed.
    "grep -n \"a|b\" ARCHITECTURE.md | head -5",
    "python tools/audit/changed_paths.py --staged | grep -n \"a|b\" ARCHITECTURE.md",
    # A REAL forbidden read inside a heredoc body that IS executed as shell. OI-300 asks for this
    # explicitly: a future body-skipping fix for shape (4) must not pass by discarding bodies
    # wholesale.
    "bash <<'SH'\ncat CLAUDE.md\nSH",
    # A working-tree read whose target is written AFTER a redirection — so a future fix that
    # strips redirections (OI-300 shape 5) cannot pass by discarding too much.
    "grep -n \"pattern\" > /tmp/hits.txt ARCHITECTURE.md",
]

# ── THE CORPUS AS IT STOOD BEFORE THE POWERSHELL DIALECT ENTERED IT (2026-08-08) ──────────────
# Frozen here so the dispatch's assumption A2 — that widening the utility set leaves the POSIX
# side's behaviour untouched — is DISCHARGED BY MEASUREMENT rather than asserted: every row
# below is decided with the dialect on and with it off, and any verdict that moves is a STOP.
SANCTIONED_BEFORE_THE_DIALECT = tuple(SANCTIONED)
FORBIDDEN_BEFORE_THE_DIALECT = tuple(FORBIDDEN)

# ── ADDED 2026-08-08 (`cc_instruction_guard_dialect_close_and_push.md`, Task 1.1) ─────────────
# THE POWERSHELL DIALECT, WHICH NEITHER LIST HELD A SINGLE MEMBER OF.
#
# The guard is armed on the PowerShell tool BY DESIGN — the hook block in this module's own
# docstring carries the matcher `"Bash|PowerShell"` — while the utility set above is POSIX-only.
# So a line count, an existence-and-size listing and a search of working-tree files were all
# ADMITTED where `cat` aimed at the same path was DENIED, and the reason string the guard returned
# for them, *"no text utility is aimed at a repository path"*, was true of the set it carried and
# false of the command it read (`OPEN_ITEMS.md` OI-345).
#
# THE CORPUS GOES IN FIRST, AT THE UNWIDENED GUARD, on user ruling R1 of 2026-08-07
# (`cowork_rulings_oi345_oi342_2026_08_07.md`) — the same order that ruling's predecessor fixed
# for OI-343, and for the reason it states in its own words: the committed `--establish --check`
# passed PRECISELY BECAUSE no member of this dialect was in either list, so the published rates
# re-derived exactly while blind to the whole of it. Re-establishing a widened guard against the
# corpus that could not see the defect repeats the error being fixed.
#
# WHERE THE NAMES COME FROM, so the list is sourced and not authored until it works. The cmdlets
# are the PowerShell commands that perform one of the four acts D-253 itself names — content,
# existence, line counts, searches — on a path argument. Their aliases are read out of
# PowerShell's OWN alias table, not recalled: `Get-Alias -Definition <cmdlet>`, run on
# Windows PowerShell 5.1.26100.8875 (Desktop edition, Windows NT 10.0.26200.0), which returns
#   Get-Content : cat gc type      Get-ChildItem : dir gci ls     Select-String : sls
#   Get-Item    : gi               Resolve-Path  : rvpa           Measure-Object : measure
#   Import-Csv  : ipcsv            Test-Path     : (no alias)     Import-Clixml  : (no alias)
# The version is pinned because the alias table is a property of the host: PowerShell 7 is not
# installed on this machine, so its table could not be enumerated and NO claim is made about it —
# the sourcing command is recorded here so a session on another version can re-run it.
#
# `cat` and `type` are PowerShell aliases too and are deliberately NOT repeated below: both are
# already in the POSIX set under the same spelling, `cat CLAUDE.md` is already a forbidden row,
# and a second entry would measure the same name twice.
POWERSHELL_SANCTIONED = [
    # (a) THE SAME COMMANDS AIMED OUTSIDE THE TREE — the control the widening must not break.
    "Get-Content C:\\tmp\\snap_out.txt -TotalCount 20",
    "Get-Content \"C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/x/scratchpad/est.txt\"",
    "Select-String -Path C:\\tmp\\guards.txt -Pattern 'FAIL'",
    "Get-ChildItem C:\\tmp\\cand",
    "Get-ChildItem C:\\tmp -Filter *.json",
    "Test-Path C:\\tmp\\cand\\summary.json",
    "Get-Content C:\\tmp\\out.txt | Measure-Object -Line",
    # (b) THE ALIASES, aimed outside the tree.
    "gc /tmp/split_1p.txt",
    "sls -Path /tmp/snap_out.txt -Pattern 'FAILED'",
    "dir C:\\tmp",
    "ls /tmp/out.txt",
    "gi C:\\tmp\\out.txt",
    "rvpa C:\\tmp",
    # (c) THE PATH-LESS FORMS, which are the ones a widening most easily turns into false denies:
    # a search and a line count fed from a PIPELINE read nothing off disk at all, and their one
    # bare argument is a PATTERN or a property name that a naive path test reads as a path — the
    # OI-292 defect in this dialect. They are the reason the false-deny arm is published.
    "Select-String -Pattern 'FAIL'",
    "Measure-Object -Line",
    # (d) THE GIT-OBJECT FORMS D-253 EXPLICITLY PERMITS, spelled in this dialect.
    "git show 4a9c0d4827:CLAUDE.md | Select-String -Pattern 'D-253'",
    "git cat-file -p bd3a608fec | Measure-Object -Line",
    # (e) THE COMMAND THAT SOURCED THIS WIDENING. It reads PowerShell's alias table, not the
    # working tree, and a guard that denied it would deny its own provenance.
    "Get-Alias -Definition Get-Content",
]

POWERSHELL_FORBIDDEN = [
    # (a) THE BARE CMDLET FORMS, each measured at this module's own `decide()` and recorded on
    # `OPEN_ITEMS.md` OI-345 as ADMITTED. Every one is a read D-253 forbids.
    "Get-Content C:\\s\\MS\\STATUS.md -TotalCount 20",
    "Select-String -Path C:\\s\\MS\\CLAUDE.md -Pattern 'D-253'",
    "Test-Path C:\\s\\MS\\CLAUDE.md",
    "Get-ChildItem C:\\s\\MS\\open_items",
    "Get-Item C:\\s\\MS\\OPEN_ITEMS.md",
    "Resolve-Path C:\\s\\MS\\DECISIONS.md",
    "Import-Csv C:\\s\\MS\\tools\\audit\\decisions\\cluster_dispositions.csv",
    # The RELATIVE form, which is how the PowerShell tool arrives: it starts in the project
    # directory, so a bare file name is a working-tree read with no absolute path in sight.
    "Get-Content STATUS.md",
    # (b) THE ALIASES aimed at repository paths — the half the collision question is about.
    "gc C:\\s\\MS\\STATUS.md",
    "sls -Path C:\\s\\MS\\DECISIONS.md -Pattern 'D-436'",
    "gci C:\\s\\MS\\tools\\audit",
    "dir C:\\s\\MS\\open_items",
    "gi C:\\s\\MS\\OPEN_ITEMS.md",
    "rvpa C:\\s\\MS\\DECISIONS.md",
    "ipcsv C:\\s\\MS\\tools\\audit\\decisions\\cluster_dispositions.csv",
    # `ls` aimed at a repository path is BOTH a Get-ChildItem alias and OI-300's shape (1), which
    # the 2026-08-04 act named as deliberately untouched. It is one row, not two: the same
    # spelling denies the same act in both dialects, and the guard has no model of which shell it
    # was handed. What that means for OI-300 is reported, never claimed as closing it.
    "ls C:\\s\\MS\\ARCHITECTURE.md",
    # (c) PIPELINES — so the 2026-08-04 segmentation fix is exercised in this dialect too: the
    # line count OI-345 records, a forbidden read in the SECOND segment, and a quoted pipe inside
    # a pattern, which is OI-343's own defeating shape one dialect over.
    "Get-Content C:\\s\\MS\\STATUS.md | Measure-Object -Line",
    "Get-ChildItem C:\\tmp | Out-Null; Get-Content C:\\s\\MS\\CLAUDE.md",
    "Select-String -Path C:\\s\\MS\\DECISIONS.md -Pattern 'D-642|D-643'",
    # (d) THE WRAPPER FORM — the three commands the OI-345 session ACTUALLY ISSUED, each through
    # `powershell.exe -Command "…"` from the other shell. They are in the corpus so the published
    # rate REPORTS them; widening a name set cannot reach inside a quoted `-Command` argument, and
    # doing so would be a second behaviour change that D-436 reserves to the user.
    "powershell.exe -NoProfile -Command \"(Get-Content 'C:\\s\\MS\\STATUS.md' | "
    "Measure-Object -Line).Lines\"",
    "powershell.exe -NoProfile -Command \"Get-ChildItem 'C:\\s\\MS\\BUILD_AND_TEST.md' | "
    "Select-Object Name,Length\"",
    "powershell.exe -NoProfile -Command \"Select-String -Path 'C:\\s\\MS\\DECISIONS.md' "
    "-Pattern 'delegation' | Measure-Object\"",
    # (e) AN INTERPRETER-MEDIATED READ, issued live by the session that performed this widening:
    # a line count of a working-tree file obtained through `python -c`. It is neither dialect's
    # vocabulary and no name set reaches it. It is in the corpus for the reason #19 gives — a
    # corpus chosen to make a guard look clean measures nothing — and it is reported as missed
    # rather than fixed here.
    "python -c \"print(sum(1 for _ in open(r'C:/s/MS/STATUS.md')))\"",
]

SANCTIONED += POWERSHELL_SANCTIONED
FORBIDDEN += POWERSHELL_FORBIDDEN


def establish() -> dict:
    san = [{"command": c, "denied": decide(c)[0], "reason": decide(c)[1]} for c in SANCTIONED]
    forb = [{"command": c, "denied": decide(c)[0], "reason": decide(c)[1]} for c in FORBIDDEN]
    false_denies = sum(1 for r in san if r["denied"])
    caught = sum(1 for r in forb if r["denied"])
    # The 2026-08-03 tokenizer change is maintenance on a KEPT mechanism (D-436), so it is
    # RE-established rather than asserted: the same two sets are run with quote grouping off
    # and on, and both figures are published. The dispatch's condition for reverting it is a
    # rise in false denies elsewhere, so that figure must be visible and not inferred.
    # `token_first=False` is REQUIRED here, not incidental: the 2026-08-04 segmentation change
    # made `group_quotes` unreachable on the default path, so without it this comparison would
    # silently compare the current guard against itself and publish a difference of zero.
    old_false = sum(1 for c in SANCTIONED
                    if decide(c, group_quotes=False, token_first=False)[0])
    old_caught = sum(1 for c in FORBIDDEN
                     if decide(c, group_quotes=False, token_first=False)[0])
    # The 2026-08-04 SEGMENTATION change, measured the same way and on the SAME extended corpus,
    # so the delta reported is the fix's and not the corpus widening's (D-436).
    pre_false = sum(1 for c in SANCTIONED if decide(c, token_first=False)[0])
    pre_caught = sum(1 for c in FORBIDDEN if decide(c, token_first=False)[0])
    pre_missed = [c for c in FORBIDDEN if not decide(c, token_first=False)[0]]
    still_missed = [r["command"] for r in forb if not r["denied"]]
    still_false = [r["command"] for r in san if r["denied"]]

    # The 2026-08-08 POWERSHELL DIALECT widening, measured the same way and on the SAME extended
    # corpus, so the delta reported is the widening's and not the corpus extension's (D-436).
    posix_false = sum(1 for c in SANCTIONED if decide(c, dialect=False)[0])
    posix_caught = sum(1 for c in FORBIDDEN if decide(c, dialect=False)[0])
    posix_missed = [c for c in FORBIDDEN if not decide(c, dialect=False)[0]]
    # ASSUMPTION A2, DISCHARGED BY MEASUREMENT: every row that was in the corpus BEFORE the
    # dialect entered it is decided both ways, and any row whose verdict moves is named. A
    # non-empty list is the dispatch's STOP.
    a2_moved = [
        {"command": c,
         "posix_only": "DENY" if decide(c, dialect=False)[0] else "allow",
         "with_the_dialect": "DENY" if decide(c)[0] else "allow"}
        for c in list(SANCTIONED_BEFORE_THE_DIALECT) + list(FORBIDDEN_BEFORE_THE_DIALECT)
        if decide(c, dialect=False)[0] != decide(c)[0]
    ]
    return {
        "purpose": "Establishment (#19) of tools/audit/shell_read_guard.py: its deny rate on "
                   "the forms CLAUDE.md names, and its FALSE-deny rate on real commands this "
                   "repository issues. A guard that fires on legitimate use gets switched off, "
                   "so the false-deny rate is the figure that decides whether it may be armed.",
        "coverage_limits": [
            "Project-scoped: it binds sessions that run in this directory and read this "
            "project's settings. Whether the WRITING side does is not established, so the rule "
            "must not be described as enforced for both sides.",
            "The text-utility half in BOTH dialects the hook is armed on — POSIX from the "
            "start, PowerShell since 2026-08-08 (OI-345). A command carried inside a quoted "
            "argument (`powershell.exe -Command \"…\"`) is still admitted: a name set cannot "
            "reach inside one, it is in the corpus, and it is rowed.",
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
                    "with_the_fix": false_denies, "without_it": old_false, "of": len(san),
                    "read_this_as": "`without_it` is the guard with NEITHER the 2026-08-03 "
                                    "tokenizer nor the 2026-08-04 segmentation — the state before "
                                    "this line of maintenance began. It is measured on the corpus "
                                    "as it stands today, so it is not the figure phase 1s "
                                    "published against the corpus of that date.",
                    "★_corrected_2026_08_08": "The sentence above is preserved as written (#12) "
                                              "and one clause of it is no longer true: `without_it` "
                                              "is NOT the guard as it stood before this line of "
                                              "maintenance began, because the 2026-08-08 "
                                              "PowerShell utility set is present in BOTH arms. It "
                                              "is held constant on purpose — that is what keeps "
                                              "the DIFFERENCE attributable to the tokenizer and "
                                              "the segmentation — so the delta is unaffected and "
                                              "only the description of the absolute value was "
                                              "wrong."},
                "detection_on_the_forbidden_set": {
                    "with_the_fix": caught, "without_it": old_caught, "of": len(forb)},
                "the_revert_condition": "The dispatch says: if the fix raises false denies "
                                        "elsewhere, revert and report. Compare the two figures "
                                        "above — a rise is the condition, and it is published "
                                        "either way rather than inferred.",
            },
        },
        "★_the_2026_08_04_segmentation_fix_and_the_corpus_it_is_measured_on": {
            "the_ruling": (
                "User, 2026-08-04 (R1, `cc_instruction_guard_fix_and_item1d.md`): fix the "
                "shell-read guard, and EXTEND ITS ESTABLISHMENT CORPUS WITH THE SHAPES THAT "
                "DEFEAT IT BEFORE ANY RATE IS REPUBLISHED."
            ),
            "why_the_corpus_came_first": (
                "The ruling states its own reason: re-establishing against the same corpus would "
                "repeat the error being fixed. The committed `--establish --check` passed "
                "PRECISELY BECAUSE the corpus omitted the defeating shape, so the published "
                "false-negative rate was not a bound on the true one. A measured rate is only as "
                "wide as the corpus it was measured on (#19)."
            ),
            "what_changed": (
                "The ORDER, not the pattern. The whole command is lexed ONCE with the shell's "
                "list and pipeline operators recognised as tokens in their own right, and the "
                "segments are cut at those TOKENS. Previously the command was cut into segments "
                "over RAW TEXT and each segment was tokenized afterwards, so a `|` inside a "
                "quoted pattern was read as a pipeline separator. The punctuation set is exactly "
                "the characters the superseded regex cut on, so the only behaviour that moves is "
                "where the segment boundaries fall."
            ),
            "the_miss_it_removes": (
                "`grep -n \"alpha|beta\" src/composing/analysis/key/keyresolver.cpp` was "
                "ADMITTED while the identical command without the pipe was DENIED. Found by the "
                "guard denying one command after admitting four of the same kind, and MEASURED "
                "at this module's own decision function over the commands the preceding session "
                "actually issued — never reasoned from the source (`OPEN_ITEMS.md` OI-343)."
            ),
            "★_what_the_PREVIOUS_published_rates_did_and_did_not_bound": (
                "The rates published before 2026-08-04 are NOT WITHDRAWN AS WRONG (#12): they "
                "were correct for the corpus they were measured on, and they re-derived exactly. "
                "What they did not do is bound the guard's behaviour on the pipe-in-a-quoted-"
                "argument shape, because that shape was not in either corpus. They are recorded "
                "here as not bounding what they appeared to bound, which is a different "
                "statement from being incorrect."
            ),
            "detection_on_the_forbidden_set_SAME_corpus": {
                "with_the_fix": caught, "without_it": pre_caught, "of": len(forb),
                "what_the_fix_newly_catches": sorted(
                    c for c in pre_missed if c not in still_missed),
                "what_is_STILL_missed_and_is_not_this_fix_s_subject": still_missed,
                "★_corrected_2026_08_08": "Both arms now also carry the 2026-08-08 PowerShell "
                                          "utility set, held constant so the difference stays "
                                          "attributable to the segmentation change alone. The "
                                          "absolute values therefore differ from those published "
                                          "on 2026-08-04; the delta does not, and neither list "
                                          "above is a reconstruction of the guard as it stood on "
                                          "any date.",
            },
            "false_denies_on_the_sanctioned_set_SAME_corpus": {
                "with_the_fix": false_denies, "without_it": pre_false, "of": len(san),
                "the_revert_condition": (
                    "The dispatch says: if the fix raises false denials materially, revert and "
                    "report — a guard that blocks correct commands gets disarmed, which is worse "
                    "than one with a known gap. Both figures are measured on the SAME extended "
                    "corpus, so the comparison is of the fix and not of the corpus widening."
                ),
                "the_false_denies_that_remain": still_false,
                "what_they_are": (
                    "Every one is a shape `OPEN_ITEMS.md` OI-300 already records as a MEASURED "
                    "false deny owed a fix — an unexpanded shell variable pointing outside the "
                    "tree (shape 2), a redirection token taken for the aimed path (shape 5), and "
                    "a heredoc BODY line that is not a command at all (shape 4). They are in the "
                    "corpus so the published rate REPORTS them; none is fixed here, because each "
                    "is a further behaviour change that owes its own establishment, and D-436 "
                    "makes changing a mechanism the user's ruling rather than a session's."
                ),
            },
            "★_superseded_in_part_on_2026_08_08": (
                "The first line of `what_this_fix_deliberately_does_NOT_touch` below — OI-300's "
                "shape (1), `ls <repository path>` — is no longer true of the guard, and it is "
                "left standing rather than edited because it is the record of what the 2026-08-04 "
                "act did (#12). `ls` is an enumerated alias of `Get-ChildItem`, so the 2026-08-08 "
                "dialect widening brought it into the utility set; that is reported at "
                "`★_the_2026_08_08_powershell_dialect_widening…` and is NOT a claim that OI-300 "
                "is closed. Its shapes (2), (3), (4) and (5) are untouched and remain that row's "
                "owed establishment run."
            ),
            "what_this_fix_deliberately_does_NOT_touch": [
                "OI-300 shape (1) — `ls <repository path>`, an existence read outside the "
                "TEXT-UTILITY set the guard covers.",
                "OI-300 shape (2) — an unexpanded shell variable read literally.",
                "OI-300 shape (3) — a hashless `git diff` on a working-tree path.",
                "OI-300 shape (4) — a heredoc body read as though it were a command.",
                "OI-300 shape (5) — a redirection token classified as the aimed path.",
                "Each changes WHAT the guard denies rather than WHERE it cuts the command, and "
                "each owes its own measured rate in both directions before it lands (D-436).",
            ],
        },
        "★_the_2026_08_08_powershell_dialect_widening_and_the_corpus_it_is_measured_on": {
            "the_ruling": (
                "User, 2026-08-07 (ruling 1 of `cowork_rulings_oi345_oi342_2026_08_07.md`, "
                "applied by `cc_instruction_guard_dialect_close_and_push.md`): the shell-read "
                "guard's PowerShell blindness is FIXED, CORPUS FIRST. Extend the establishment "
                "corpus with the PowerShell family and its aliases, sanctioned and forbidden "
                "forms both; THEN widen the utility set; publish both rates against the extended "
                "corpus; the revert condition — a material rise in false denials — governs as "
                "before. The mechanism change is licensed by that ruling (D-436)."
            ),
            "the_defect_it_answers": (
                "The guard is armed on the PowerShell tool BY DESIGN — the hook block in this "
                "module's docstring carries the matcher `\"Bash|PowerShell\"` — while its utility "
                "set was POSIX-only. Measured at this module's own `decide()` and never reasoned "
                "from its source, `Get-Content`, `Select-String`, `Get-ChildItem` and `Test-Path` "
                "aimed at repository paths were ALLOWED where `cat` on the same path was DENIED, "
                "and the reason string returned for them — \"no text utility is aimed at a "
                "repository path\" — was true of the set the guard carried and false of the "
                "command it read (`OPEN_ITEMS.md` OI-345)."
            ),
            "why_the_corpus_came_first": (
                "Neither list held a single member of the dialect, so `--establish --check` "
                "re-derived the recorded deny and false-deny rates EXACTLY while blind to the "
                "whole of it — current, reproducible and silent, which is the condition #19 "
                "exists to refuse. Widening first and re-establishing against that same corpus "
                "would have repeated the error being fixed."
            ),
            "★_the_blindness_MEASURED_before_the_widening": {
                "what_was_run": "Every row added to the corpus, decided at the UNWIDENED guard "
                                "— the committed POSIX-only utility set, with the extended "
                                "corpus in place. This is what the old rates could not show.",
                "new_forbidden_rows_missed": len(POWERSHELL_FORBIDDEN) - sum(
                    1 for c in POWERSHELL_FORBIDDEN if decide(c, dialect=False)[0]),
                "new_forbidden_rows": len(POWERSHELL_FORBIDDEN),
                "new_sanctioned_rows_falsely_denied": sum(
                    1 for c in POWERSHELL_SANCTIONED if decide(c, dialect=False)[0]),
                "new_sanctioned_rows": len(POWERSHELL_SANCTIONED),
                "read_this_as": "Every forbidden form of the dialect was admitted and no "
                                "sanctioned form of it was denied — the guard was not wrong "
                                "about this family, it could not see it at all.",
            },
            "where_the_vocabulary_came_from": {
                "the_cmdlets": "The PowerShell commands that perform one of the four acts D-253 "
                               "itself names — content, existence, line counts, searches — on a "
                               "path argument. Stated as a rule so the set is derivable rather "
                               "than authored until the corpus passes, which is the "
                               "vocabulary-assembled-until-it-works failure this act must avoid.",
                "the_aliases": "Read out of PowerShell's OWN alias table, never recalled: "
                               "`Get-Alias -Definition <cmdlet>`.",
                "the_version_it_was_read_on": "Windows PowerShell 5.1.26100.8875, Desktop "
                                              "edition, on Windows NT 10.0.26200.0.",
                "why_the_version_is_pinned": "The alias table is a property of the host, not of "
                                             "the language, so the enumeration is only as wide "
                                             "as the version it was read on. PowerShell 7 is NOT "
                                             "installed on this machine, so its table could not "
                                             "be enumerated and no claim is made about it; the "
                                             "sourcing command is recorded so a session on "
                                             "another version can re-run it. Carrying a name "
                                             "that some other host does not alias costs "
                                             "detection nothing — it simply never matches.",
                "the_utility_names_added": sorted(POWERSHELL_UTILITIES),
                "the_candidate_selection_rule": "Within this family a path is bound either as "
                                                "the value of `-Path` / `-LiteralPath` / "
                                                "`-FilePath` or as the FIRST positional "
                                                "argument, never both, so those are the only two "
                                                "places examined. `Select-String` and "
                                                "`Measure-Object` have their first positional "
                                                "dropped, being a pattern and a property name — "
                                                "the same special case the POSIX branch already "
                                                "makes for `grep`, and what keeps a "
                                                "pipeline-fed `Select-String -Pattern 'FAIL'` "
                                                "from being read as a repository path.",
            },
            "detection_on_the_forbidden_set_SAME_corpus": {
                "with_the_widening": caught, "posix_set_only": posix_caught, "of": len(forb),
                "what_the_widening_newly_catches": sorted(
                    c for c in posix_missed if c not in still_missed),
                "what_is_STILL_missed_and_is_not_this_act_s_subject": still_missed,
            },
            "false_denies_on_the_sanctioned_set_SAME_corpus": {
                "with_the_widening": false_denies, "posix_set_only": posix_false,
                "of": len(san),
                "the_revert_condition": (
                    "The ruling says: a material rise in false denials governs — revert and "
                    "report. Both values are measured on the SAME extended corpus, so the "
                    "comparison is of the widening and not of the corpus rows added with it."
                ),
                "the_false_denies_that_remain": still_false,
            },
            "★_assumption_A2_the_POSIX_side_is_untouched": {
                "what_was_checked": "Every row the corpus carried BEFORE this act, decided with "
                                    "the POSIX-only set and again with the dialect, and any row "
                                    "whose verdict moved named. The dispatch makes a moved "
                                    "verdict a STOP.",
                "rows_checked": len(SANCTIONED_BEFORE_THE_DIALECT)
                                + len(FORBIDDEN_BEFORE_THE_DIALECT),
                "verdicts_that_moved": a2_moved,
            },
            "★_what_the_PREVIOUS_published_rates_did_and_did_not_bound": (
                "The rates published before 2026-08-08 are NOT WITHDRAWN AS WRONG (#12): they "
                "were correct for the corpus they were measured on and they re-derived exactly. "
                "What they did not do is bound the guard's behaviour on the PowerShell dialect, "
                "because no member of it was in either list. THEY WERE BLIND, NOT WRONG — a "
                "different statement, and the reason #19 asks for positive establishment rather "
                "than for a check that has not yet failed."
            ),
            "★_two_consequences_reported_rather_than_claimed": [
                "OI-300's shape (1) — `ls` aimed at a repository path — is now DENIED, because "
                "`ls` is an enumerated alias of `Get-ChildItem` and the guard has no model of "
                "which shell handed it the command. The same spelling denies the same act in "
                "both dialects. This is REPORTED as a measured consequence of the licensed act; "
                "it is NOT a claim that OI-300 is closed, and its shapes (2), (3), (4) and (5) "
                "are untouched.",
                "The WRAPPER form — `powershell.exe -Command \"<cmdlet> <repository path>\"` — "
                "is still ADMITTED, and it is the form the three commands OI-345 records were "
                "actually issued in. Widening a name set cannot reach inside a quoted `-Command` "
                "argument; recursing into one is a SECOND behaviour change, which D-436 reserves "
                "to the user. It is in the corpus so the published rate reports it rather than "
                "being silent about it, and it is rowed.",
            ],
            "what_this_widening_deliberately_does_NOT_touch": [
                "The wrapper form above, and any other command that carries a shell command "
                "inside a quoted argument.",
                "An interpreter-mediated read — a `python -c` that opens a working-tree file. It "
                "is in the corpus, measured as missed, and reachable by no name set.",
                "OI-300's shapes (2), (3), (4) and (5), which remain that row's owed run.",
                "The POSIX branch's own candidate selection, which is unchanged (assumption A2).",
            ],
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
