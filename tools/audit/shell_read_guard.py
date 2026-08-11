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
    both tools, so the PowerShell spelling of the same read was admitted.
  * ★ SINCE THE FAMILY RULING of 2026-08-08 it also covers a command carried inside a WRAPPER's
    quoted code argument (`bash -c`, `sh -c`, `powershell(.exe) -Command`, `pwsh -Command`),
    which is re-run through this same decision; an INTERPRETER's code string (`python -c`,
    `perl -e`, and a heredoc body fed to one) by POLICY, when it carries a literal path this
    repository holds; and a HASHLESS `git diff` aimed at a working-tree path.  The same act
    removed three measured FALSE denies — the redirection tokens and the heredoc body — and
    fixed the case-sensitive path comparison that admitted every repository path written with a
    lowercase drive letter (OI-351).
  * ★ THE CEILING, stated rather than left to be found: interpreter code whose path is COMPUTED
    rather than written carries no literal for the policy to see, and is admitted.  A row of
    exactly that shape is in the corpus and is reported as missed, so the published deny rate
    states the bound instead of being silent about it (#19; a proxy pretending otherwise is
    what #17(d) forbids).
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


def _canonical_drive(path: str) -> str:
    """A Windows drive letter in ONE case, so `ROOT` does not depend on how the process started.

    ★ THE CAUSE OF `OPEN_ITEMS.md` OI-366, ESTABLISHED AT THE OBJECTS 2026-08-11 under the user's
    Ruling 50 and NOT asserted from the source. `ROOT` is derived from `__file__`, which Python
    makes absolute against the process's own current directory — so the drive letter arrives in
    whatever case the invocation happened to use. The FAMILY arm normcases both sides and is
    unaffected; the CONTROL arm (`family=False`) restores the case-SENSITIVE comparison on purpose,
    and it compares against `ROOT` as written. A lowercase drive letter therefore moved that arm's
    verdicts, and only that arm's, which is exactly the shape of a check that reports STALE on one
    invocation and re-derives on the next with nothing edited in between.

    MEASURED, both ways, before this line was written: the module loaded from a path spelled with an
    uppercase drive letter re-derives the committed artifact byte for byte, and the same module
    loaded from the same file spelled with a lowercase one does not. The diagnosis ran OUTSIDE the
    tool, which is why it could be taken before any guard file was touched.

    WHAT THIS FIXES AND WHAT IT DELIBERATELY DOES NOT. It makes the control arm REPRODUCIBLE — it
    now reports the pre-fix guard as launched from the spelling every published rate was measured
    under, instead of reporting whichever spelling the launcher happened to use. It does not change
    the family arm, which is what the live hook decides on, so **no live verdict moves**: the
    published deny and false-deny rates are the same values, now obtainable on demand, which is what
    #19 asks of an established value.
    """
    if len(path) > 1 and path[1] == ":":
        return path[0].upper() + path[1:]
    return path


ROOT = _canonical_drive(os.path.abspath(os.path.join(HERE, "..", "..")))
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

# ── THE 2026-08-08 FAMILY: wrappers, interpreters, redirections, heredocs, hashless git ──────
# The ruling is `cowork_ruling_guard_family_2026_08_08.md`, with OI-351 folded in by Ruling 3 of
# `cowork_rulings_2026_08_08_pre_away.md`. Everything in this block is licensed by it (D-436), and
# every piece is reachable from `decide(..., family=False)` in its previous behaviour so both arms
# are measurable on the same corpus.

# CLAUSE 1 —the wrappers whose code argument is a shell command in a dialect this guard MODELS.
# Recursing into one is composition of the established POSIX and PowerShell branches (#6), not new
# modeling: the code string is re-run through this module's own decision.
SHELL_WRAPPERS = {"bash", "sh", "dash", "zsh", "ksh", "powershell", "pwsh"}
WRAPPER_CODE_FLAGS = {"-c", "-command", "-cmd"}

# CLAUSE 2 —the interpreters whose code argument this guard does NOT model. A shell command is not
# what they carry; source code is, and no name set reaches inside it. They are decided by POLICY.
INTERPRETERS = {"python", "python3", "python2", "py", "perl", "ruby", "node", "php", "lua"}
INTERPRETER_CODE_FLAGS = {"-c", "-e", "--eval", "--exec"}

# A string literal in interpreter code. Deliberately simple: it finds quoted runs, and a prefix
# such as `r` or `f` sits outside the quotes and is therefore not included in the capture.
CODE_STRING_LITERAL = re.compile(r"'([^'\n]{1,400})'|\"([^\"\n]{1,400})\"")

# CLAUSE 3a —redirection. A redirection operator and the file it names are not the command's aimed
# path, and reading one as such is OI-300's shape (5): a measured FALSE DENY. Both spellings occur
# — separated (`2>` `/dev/null`) and fused (`2>/dev/null`).
REDIRECTION_OPERATOR = re.compile(r"^\d*(?:>>|>&|>|<<<|<<|<)&?\d*$")
REDIRECTION_FUSED = re.compile(r"^\d*(?:>>|>|<<<|<<|<)\S+$")

# CLAUSE 3b —heredocs. A heredoc BODY is not a sequence of commands, and classifying its lines as
# commands is OI-300's shape (4): a `head = old[:k]` inside a Python heredoc was DENIED as a read.
# What the body IS depends on who is fed it, which is the whole of the rule below.
HEREDOC_INTRODUCER = re.compile(r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")


def owner_of(line: str) -> str:
    """The command a line invokes — its first token past any environment assignments."""
    toks = tokenize(line)
    i = 0
    while i < len(toks) and ENV_ASSIGN.match(toks[i]):
        i += 1
    if i >= len(toks):
        return ""
    util = os.path.basename(toks[i].strip("'\"")).lower()
    return util[:-4] if util.endswith(".exe") else util


def split_heredocs(command: str) -> tuple[str, list[str]]:
    """(command with non-shell heredoc bodies removed, interpreter heredoc bodies).

    THREE CASES, and the third is why the body cannot simply be dropped:

      * a heredoc fed to a SHELL (`bash <<'SH'`) is shell code — its body STAYS in the command and
        is classified exactly as any other command would be. The corpus carries a forbidden read in
        one, precisely so a body-skipping fix cannot pass by discarding bodies wholesale.
      * a heredoc fed to an INTERPRETER (`python - <<'PY'`) is interpreter code — it is removed
        from command classification and returned separately, so CLAUSE 2's policy runs over it. This
        is the founding instance of `OPEN_ITEMS.md` OI-348's second shape.
      * anything else is DATA and is removed.

    THE LIMIT, stated rather than left to be found: one heredoc per command, introduced on the
    first line. Every instance the corpus carries has that shape; a command with two heredocs, or
    one introduced further down a pipeline, is not modeled and its later body would still be read
    as commands.
    """
    lines = command.split("\n")
    if len(lines) < 2:
        return command, []
    m = HEREDOC_INTRODUCER.search(lines[0])
    if not m:
        return command, []
    terminator = m.group(2)
    end = len(lines)
    for i in range(1, len(lines)):
        if lines[i].strip() == terminator:
            end = i
            break
    body = lines[1:end]
    remainder = lines[:1] + lines[end + 1:]
    owner = owner_of(lines[0])
    if owner in SHELL_WRAPPERS:
        return command, []                      # shell code: leave it to be classified
    if owner in INTERPRETERS:
        return "\n".join(remainder), ["\n".join(body)]
    return "\n".join(remainder), []             # data: it is not a command at all


def wrapper_code(util: str, after_util: list[str]) -> str | None:
    """The code string a wrapper carries, or None if this invocation carries none."""
    if util not in SHELL_WRAPPERS:
        return None
    for i, tok in enumerate(after_util):
        if tok.lower() in WRAPPER_CODE_FLAGS and i + 1 < len(after_util):
            return after_util[i + 1].strip("'\"")
    return None


def interpreter_code(util: str, after_util: list[str]) -> str | None:
    """The code string an interpreter carries with an eval flag, or None."""
    if util not in INTERPRETERS:
        return None
    for i, tok in enumerate(after_util):
        if tok.lower() in INTERPRETER_CODE_FLAGS and i + 1 < len(after_util):
            return after_util[i + 1].strip("'\"")
    return None


def literal_repository_paths(code: str, family: bool = True) -> list[str]:
    """String literals in interpreter code that NAME a path this repository actually has.

    THE POLICY, and its stated bound (#19, #17(d)).  The guard cannot parse interpreter code, and
    a structural proxy standing in for that is exactly what the Premise Gate forbids.  So the test
    is deliberately narrow and checkable: a QUOTED LITERAL that resolves to a path the repository
    HOLDS.  Requiring it to exist is what keeps `print('hello world')` from reading as a read —
    without it every quoted word in every one-liner would be a candidate path, which is the
    false-deny failure that gets a guard switched off.

    WHAT IT CANNOT SEE, and the corpus carries a row for it so the published rate says so: a code
    string that COMPUTES its path — `os.path.join(os.getcwd(), 'CLAUDE.md')` — has no literal
    repository path in it at all.  That residual is the design's stated ceiling, not an oversight.
    """
    found: list[str] = []
    for a, b in CODE_STRING_LITERAL.findall(code):
        s = (a or b).strip()
        if not s or outside_repo(s, family):
            continue
        cand = s if os.path.isabs(s) else os.path.join(ROOT, s)
        if os.path.exists(cand):
            found.append(s)
    return found


def strip_redirections(tokens: list[str]) -> list[str]:
    """Tokens with redirection operators and their targets removed (OI-300 shape 5).

    THE `2>&1` CASE, which is why this is an index loop rather than a skip-the-next-one.  The
    lexer treats `&` as punctuation in its own right, so `2>&1` arrives as THREE tokens — `2>`,
    `&`, `1`.  Skipping only the token after the operator leaves the bare `1`, which then reads as
    a relative path and denies the command: measured on `tail -5 /tmp/out.txt 2>&1`, a row this
    corpus already carried, which stayed a false deny until the `&` was consumed with the operator
    it belongs to.
    """
    out: list[str] = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if REDIRECTION_OPERATOR.fullmatch(tok):
            i += 1
            if i < len(tokens) and tokens[i] == "&":
                i += 1                      # the `&` of `2>&1`, cut out by the lexer
            if i < len(tokens):
                i += 1                      # the redirection target
            continue
        if REDIRECTION_FUSED.fullmatch(tok):
            i += 1
            continue
        out.append(tok)
        i += 1
    return out


# CLAUSE 3c —a HASHLESS `git diff` aimed at a working-tree path. D-253's own text names it: git is
# permitted for read-only OBJECT queries by explicit hash, because a content-addressed read is
# self-verifying and errors loudly rather than returning silently-wrong content. A working-tree
# diff is not one. The test is on the ABSENCE of a hash, which is the property that separates this
# from every form the rule permits.
EXPLICIT_HASH = re.compile(r"^[0-9a-f]{7,40}$")


def hashless_git_worktree_diff(after_git: list[str], family: bool = True) -> list[str]:
    """The repository paths a hashless `git diff` is aimed at — empty when it is not one."""
    j = 0
    if j < len(after_git) and after_git[j] == "-C":
        j += 2
    while j < len(after_git) and after_git[j].startswith("-"):
        j += 1
    if j >= len(after_git) or after_git[j].strip("'\"") != "diff":
        return []
    args = after_git[j + 1:]
    if any(EXPLICIT_HASH.fullmatch(a.strip("'\"")) for a in args):
        return []                               # a hash is present: the sanctioned object query
    return [a for a in args
            if a != "--" and not OPTION.match(a) and not outside_repo(a, family)]


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
def outside_repo(token: str, family: bool = True) -> bool:
    """Is this token a path OUTSIDE this repository's working tree?

    ★ THE CASE FIX (2026-08-08, `OPEN_ITEMS.md` OI-351, the family ruling).  The comparison below
    used to be `os.path.commonpath([...]) != ROOT` — a CASE-SENSITIVE string comparison, on a
    platform whose paths are case-insensitive.  `ntpath.commonpath` takes the drive letter from the
    token AS WRITTEN, so a path spelled `c:/s/MS/…` produced `c:\\s\\MS`, which is not the string
    `C:\\s\\MS`, and the function answered OUTSIDE for a path plainly inside.  Every repository path
    written with a lowercase drive letter was therefore admitted, in EVERY utility — `cat` and
    `grep` as much as `ls`, which is why OI-351's title names `ls` only because `ls` is what was
    observed.  `os.path.normcase` on both sides is the fix: on Windows it lowercases and squares the
    separators, and on POSIX it is the identity, so nothing moves on a case-sensitive platform.

    `family=False` restores the case-sensitive comparison so `--establish` can publish both arms on
    the SAME corpus, which is the only way the family's effect is separable from the corpus
    extension's (D-436).
    """
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
            cand = os.path.abspath(t)
            if family:
                cand, root = os.path.normcase(cand), os.path.normcase(ROOT)
            else:
                root = ROOT
            return os.path.commonpath([cand, root]) != root
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
           dialect: bool = True, family: bool = True, script_argument: bool = True,
           depth: int = 0) -> tuple[bool, str]:
    """(deny, reason). A command is denied when a text utility names a repository path.

    `dialect=False` restores the POSIX-only utility set the guard carried before 2026-08-08. It
    exists so `--establish` can publish both arms on the SAME corpus, which is the only way the
    widening's effect is separable from the corpus extension's (D-436).

    `family=False` restores the guard as it stood before the 2026-08-08 FAMILY ruling — no wrapper
    recursion, no interpreter policy, no redirection or heredoc handling, no hashless-git rule, and
    the case-sensitive path comparison OI-351 turned on. Same purpose, same reason.

    `script_argument=False` restores the guard as it stood before the 2026-08-11 SCRIPT-ARGUMENT
    clause, which drops the script `sed` and `awk` take in the position `grep` takes a pattern.
    Same purpose, same reason (`OPEN_ITEMS.md` OI-355).

    `depth` bounds the wrapper recursion. A wrapper inside a wrapper is real (`bash -c "pwsh
    -Command …"`), and an unbounded recursion on a crafted command is a guard that stops guarding.
    """
    if GIT_OBJECT_READ.search(command):
        # The whole command is a git-object pipeline; a text utility downstream of it is
        # formatting object output, not reading the working tree.
        return False, "reads a git object by explicit hash — the sanctioned exemption"

    interpreter_bodies: list[str] = []
    if family:
        command, interpreter_bodies = split_heredocs(command)
        for body in interpreter_bodies:
            hits = literal_repository_paths(body, family)
            if hits:
                return True, (
                    f"an interpreter's heredoc body names a path inside this repository "
                    f"({', '.join(hits[:3])}). Interpreter code is not shell, so no utility name "
                    "reaches it; a code string carrying a literal repository path is denied by "
                    "policy — `CLAUDE.md` Conventions, register entry D-253, and the guard-family "
                    "ruling of 2026-08-08. Read it with the file tools (Read / Grep / Glob).")

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
        head = tokens[i].strip("'\"")
        if family:
            # PowerShell wraps a pipeline in parentheses to take a property off it —
            # `(Get-Content …).Lines` — so the command name arrives with grouping punctuation
            # attached and matches no name set. Measured on the one wrapper row that survived the
            # recursion until this was stripped; POSIX has the same shape with `{`.
            head = head.lstrip("({")
        util = os.path.basename(head).lower()
        if util.endswith(".exe"):
            util = util[:-4]
        if util == "git" and git_status_invocation(tokens[i + 1:]):
            return True, ("`git status` is not trusted for what is current — `CLAUDE.md` "
                          "Conventions, register entry D-253. The sanctioned way to enumerate "
                          "which paths changed is `python tools/audit/changed_paths.py` "
                          "(`--staged`, or `--commit <hash>`), which reports paths and status "
                          "codes and cannot return file content.")
        if family:
            # CLAUSE 1 —a wrapper's code argument is re-run through this same decision. No new
            # modeling: it is the POSIX and PowerShell branches already established, composed (#6).
            code = wrapper_code(util, tokens[i + 1:])
            if code is not None and depth < 3:
                deny, why = decide(code, group_quotes, token_first, dialect, family,
                                   script_argument, depth + 1)
                if deny:
                    return True, (f"`{util}` carries a command that is itself denied: {why}")
                continue
            # CLAUSE 2 —an interpreter's code argument is decided by POLICY, with a stated bound.
            icode = interpreter_code(util, tokens[i + 1:])
            if icode is not None:
                hits = literal_repository_paths(icode, family)
                if hits:
                    return True, (
                        f"`{util}` is given code naming a path inside this repository "
                        f"({', '.join(hits[:3])}). Interpreter code is not shell, so no utility "
                        "name reaches it; a code string carrying a literal repository path is "
                        "denied by policy — `CLAUDE.md` Conventions, register entry D-253, and "
                        "the guard-family ruling of 2026-08-08. Read it with the file tools "
                        "(Read / Grep / Glob).")
                continue
            # CLAUSE 3c —a hashless `git diff` at a working-tree path.
            if util == "git":
                aimed = hashless_git_worktree_diff(tokens[i + 1:], family)
                if aimed:
                    return True, (
                        f"`git diff` with no commit hash is aimed at a working-tree path "
                        f"({', '.join(aimed[:3])}). D-253 permits git only for read-only OBJECT "
                        "queries named by an explicit hash, because a content-addressed read "
                        "errors loudly rather than returning silently-wrong content; a "
                        "working-tree diff is not one. Use `python tools/audit/changed_paths.py`, "
                        "or name the commits.")
        # CLAUSE 3a —redirection operators and the files they name are not the command's aimed
        # path (OI-300 shape 5). Stripped BEFORE candidate selection, so both dialect branches
        # get the same benefit and neither has to know about redirection.
        rest_tokens = strip_redirections(tokens[i + 1:]) if family else tokens[i + 1:]
        if dialect and util in POWERSHELL_UTILITIES:
            # The PowerShell branch selects candidates by that dialect's own parameter model;
            # the POSIX branch below is untouched by it (the dispatch's assumption A2).
            targets = powershell_targets(util, rest_tokens)
        elif util in TEXT_UTILITIES:
            targets = [t for t in rest_tokens if not OPTION.match(t)]
            # `grep PATTERN file` — the first non-option token is the pattern, not a path.
            if util in ("grep", "egrep", "fgrep", "rg") and targets:
                targets = targets[1:]
            # `sed SCRIPT file`, `awk PROGRAM file` — the first non-option token is a SCRIPT, and
            # it is not a path either. The same correction as the pattern-taking four, one utility
            # class further out (`OPEN_ITEMS.md` OI-355, user Ruling 19 of 2026-08-09, performed
            # under Ruling 50 of 2026-08-11). `script_argument=False` restores the guard as it
            # stood before it, so `--establish` publishes both arms on the SAME extended corpus and
            # the clause's effect stays separable from the corpus rows' (D-436).
            #
            # WHY IT NEVER OPENS A HOLE, which is the half worth stating: what is dropped is ONE
            # token in the script's position, and every remaining token is still tested. A `sed`
            # aimed at a repository file is denied on that file, which is what the corpus rows
            # added with this clause measure in both directions.
            if script_argument and util in ("sed", "awk", "gawk", "mawk") and targets:
                targets = targets[1:]
        else:
            continue
        inside = [t for t in targets if not outside_repo(t, family)]
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

# ── THE CORPUS AS IT STOOD BEFORE THE 2026-08-08 GUARD FAMILY ENTERED IT ──────────────────────
# Frozen here so the family ruling's assumption A5 — that the family's changes move no verdict on
# a pre-existing row except the ones the design names — is DISCHARGED BY MEASUREMENT rather than
# asserted. Every row below is decided with the family on and with it off, and every verdict that
# moves is named and checked against the design.
SANCTIONED_BEFORE_THE_FAMILY = tuple(SANCTIONED)
FORBIDDEN_BEFORE_THE_FAMILY = tuple(FORBIDDEN)

# ── ADDED 2026-08-08 (`cc_instruction_away_execution.md` Task 1) ──────────────────────────────
# THE FAMILY OI-300's, OI-348's AND OI-351's SHAPES BELONG TO, entering the corpus BEFORE one line
# of the mechanism moves.
#
# THE RULING (user, 2026-08-08, `cowork_ruling_guard_family_2026_08_08.md`, with OI-351 folded in
# by Ruling 3 of `cowork_rulings_2026_08_08_pre_away.md`): ONE design over the enumerated family —
# OI-300's shapes (1)–(5) and OI-348's two — never per symptom, applying the standing
# one-fix-per-family rule of 2026-07-28. Its clause 5 fixes the ORDER, in the words the OI-343 and
# OI-345 rulings fixed it: every shape enters the establishment corpus FIRST, the blindness is
# measured at the UNWIDENED guard, both rates are published on the SAME extended corpus, and the
# revert condition — a material rise in false denials — governs.
#
# WHY THE ORDER IS NOT A FORMALITY, in this act's own evidence: at the unwidened guard EVERY row of
# the path-form group below was ADMITTED, including `cat` and `grep` aimed at repository files, and
# the guard returned *"no text utility is aimed at a repository path"* for each. Widening first and
# re-establishing against the corpus that could not see that would have repeated the error being
# fixed — which is what the ruling says in its own words.

AWAY_FORBIDDEN = [
    # ── (A) OI-351'S PATH-FORM GROUP, and it is WIDER than that row supposed ──────────────────
    # OI-351 records `ls` at a repository path ADMITTED by the LIVE hook on 2026-08-08, one day
    # after the widening whose record says that shape is denied, and names two candidate causes
    # without asserting either: the path form, and the gap between the live hook and `decide()`.
    #
    # ★ THE CAUSE IS ESTABLISHED AND IT IS THE FIRST: the DRIVE LETTER'S CASE. `outside_repo`
    # compared `os.path.commonpath(...)` against `ROOT` with `!=`, a case-sensitive string
    # comparison, on a platform whose paths are case-insensitive — and `ntpath.commonpath` takes
    # the drive from the token AS WRITTEN. So a path spelled `c:/s/MS/…` produced `c:\s\MS`, which
    # is not the string `C:\s\MS`, and every repository path written with a lowercase drive letter
    # read as OUTSIDE the repository.
    #
    # ★ THE SECOND CANDIDATE IS REFUTED, and by observation rather than by argument: the live hook
    # and `decide()` agree on BOTH live decisions the record holds. The `ls` OI-351 records as
    # ADMITTED is admitted by `decide()` on the same string; the `ls -la /c/s/MS/…` this batch's
    # own first command issued was DENIED by the live hook and is denied by `decide()` on the same
    # string. No new forbidden command was issued to test this — performing the violation to
    # measure the guard is not a measurement anyone may take.
    #
    # ★ AND IT IS NOT AN `ls` DEFECT. The two rows after the observed command are `cat` and `grep`
    # — the guard's oldest and most central vocabulary — aimed at repository files in the same
    # spelling, and at the unwidened guard both are admitted. OI-351's title names `ls` because
    # `ls` is what was observed, not because the hole has a vocabulary.
    "ls -la c:/s/MS/tools/audit/decisions/ 2>&1 | head -60",
    "cat c:/s/MS/CLAUDE.md",
    "grep -n \"D-253\" c:\\s\\MS\\CLAUDE.md",
    "ls c:/s/MS/ARCHITECTURE.md",
    "dir c:\\s\\MS\\open_items",
    # The CONTROLS for the same group — already denied before this act, and they must stay denied.
    "ls -la /c/s/MS/DECISIONS.md /c/s/MS/OPEN_ITEMS.md",
    "ls -la tools/audit",

    # ── (B) OI-348 SHAPE 1 — a read carried inside a WRAPPER's quoted code argument ───────────
    # The three `powershell.exe -Command` rows the OI-345 session actually issued are already in
    # the corpus above and already reported as missed. These add the POSIX spellings and `pwsh`,
    # so the design's clause 1 — recursion where a dialect model exists — is measured across every
    # wrapper it names rather than on the one that happened to be observed.
    "bash -c \"cat CLAUDE.md\"",
    "sh -c \"grep -n D-253 CLAUDE.md\"",
    "pwsh -Command \"Get-Content C:\\s\\MS\\STATUS.md\"",

    # ── (C) OI-348 SHAPE 2 — an INTERPRETER-mediated read ─────────────────────────────────────
    # The `python -c` line count the 2026-08-08 dialect session issued is already in the corpus.
    # These are the forms the policy in clause 2 is written against: a code string carrying a
    # LITERAL repository path, relative and absolute, and in a second interpreter so the rule is
    # not a single command's special case.
    "python -c \"print(open('CLAUDE.md').read())\"",
    "python -c \"import io; print(io.open(r'C:/s/MS/OPEN_ITEMS.md').read())\"",
    "perl -e 'open(F, \"ARCHITECTURE.md\"); print <F>;'",
    # The HEREDOC-fed interpreter — the founding instance of OI-348's second shape, issued live by
    # the session that rowed it. It is here as well as the `-c` forms because clause 3 excludes
    # heredoc bodies from COMMAND classification, and a body-skipping fix must not turn this into
    # a new blind spot: an interpreter's heredoc body is interpreter CODE, not data.
    "python - <<'PY'\nprint(open(r'C:/s/MS/tools/audit/decisions/backbone_decisions.json').read())\nPY",

    # ── (D) THE CEILING, STATED RATHER THAN HIDDEN (#19, and #17(d) on unvalidated proxies) ───
    # The guard cannot parse interpreter code, and pretending otherwise would be exactly the
    # structural-proxy-for-a-behavioural-quantity the Premise Gate forbids. A code string that
    # COMPUTES its path carries no literal for any policy to see. This row is in the corpus so the
    # published deny rate REPORTS that residual instead of being silent about it — it is expected
    # to be MISSED, and the design says so in terms.
    #
    # ★ THE FIRST WORDING OF THIS ROW WAS NOT THE CEILING IT CLAIMED TO BE, and it is corrected
    # rather than kept: it read `os.path.join(os.getcwd(), 'CLAUDE.md')`, which still carries the
    # literal `'CLAUDE.md'`, so the policy caught it and the corpus would have reported a ceiling
    # it was not measuring. Caught by reading the measurement rather than the intention — the row
    # came back DENIED when the design says it cannot be. The path is now assembled, so no literal
    # in the code names anything the repository has.
    "python -c \"import os; n='CLAUDE'+'.md'; print(open(os.path.join(os.getcwd(), n)).read())\"",

    # ── (E) OI-300 SHAPE 3 — a HASHLESS `git diff` aimed at a working-tree path ───────────────
    # D-253's own text names it: git is permitted for read-only OBJECT queries by explicit hash,
    # because a content-addressed read is self-verifying. A working-tree diff is not one.
    "git diff --stat -- ARCHITECTURE.md",
    "git diff -- tools/audit/decisions/backbone_decisions.json",
    "git diff STATUS.md",
]

AWAY_SANCTIONED = [
    # ── The CONTROLS the path-form fix must not break: the same spellings, aimed OUTSIDE. ─────
    "ls -la c:/tmp/ 2>&1 | head -60",
    "ls -la \"C:/Users/vince/AppData/Local/Temp/claude/c--s-MS/x/scratchpad\"",
    "cat c:/tmp/out.txt",

    # ── The CONTROLS for wrapper recursion. The build command is the one that matters most: it
    # is `BUILD_AND_TEST.md`'s mandated invocation, it is already in the sanctioned set above, and
    # a recursion that denied it would stop the work the rule exists to protect.
    "bash -c \"head -50 /tmp/snap_out.txt\"",
    "powershell.exe -NoProfile -Command \"Get-ChildItem C:\\tmp | Select-Object Name\"",
    # The sanctioned enumeration INSIDE a wrapper — the exemption must survive the recursion, or
    # the guard denies the very tool that makes it affordable.
    "bash -c \"python tools/audit/changed_paths.py --staged\"",
    # A wrapper carrying a git OBJECT read by explicit hash, which D-253 permits.
    "bash -c \"git show 4a9c0d4827:CLAUDE.md | head -20\"",

    # ── The CONTROLS for the interpreter policy. Each is a real shape, and each must stay
    # admitted: no literal at all, a literal that is not a path, and a literal outside the tree.
    "python -c \"print(1+1)\"",
    "python -c \"print('hello world')\"",
    "python -c \"print(open('/tmp/x.txt').read())\"",
    # A script invocation whose argument IS a repository path — this is running a tool, not
    # reading a file, and it is how every generator in this repository is invoked.
    "python tools/audit/decisions/gen_apply_field_diff.py",

    # ── The CONTROLS for the hashless-git rule: the hash-bearing forms D-253 explicitly permits.
    "git diff 4a9c0d4827 03bce02e4b",
    "git diff --stat 82ebfd68d9",
]

SANCTIONED += AWAY_SANCTIONED
FORBIDDEN += AWAY_FORBIDDEN

SANCTIONED_BEFORE_THE_SCRIPT_ARGUMENT = tuple(SANCTIONED)
FORBIDDEN_BEFORE_THE_SCRIPT_ARGUMENT = tuple(FORBIDDEN)

# ── 2026-08-11: the SCRIPT-ARGUMENT rows, added BEFORE the clause that answers them ────────────
# `OPEN_ITEMS.md` OI-355, riding this maintenance act under the user's Ruling 19 of 2026-08-09 and
# performed under Ruling 50 of 2026-08-11. The ORDER is the family ruling's own and is not a
# session's to reorder: the rows go in FIRST, so the blindness is measured at the UNWIDENED guard
# rather than at one already changed to see it, and both rates are then re-measured on the SAME
# extended corpus (D-436).
#
# THE SHAPE. `sed` and `awk` take a SCRIPT in the position `grep` takes a pattern, and only the
# four pattern-taking utilities carried the correction that drops it. So a bare script — `1,2p`,
# `40,60p`, `{print $1}` — has no drive letter and no leading separator, resolves against the
# working directory, and reads as a repository path. The command is denied on that token before
# its real target is considered at all.
SCRIPT_ARGUMENT_SANCTIONED = [
    # The FALSE DENIES themselves: aimed OUTSIDE the tree, where D-253 does not reach.
    "sed -n '40,60p' /tmp/guards1.txt",
    "sed -n '1,2p' c:/tmp/out.txt",
    "awk '{print $1}' /tmp/changed.txt",
    "awk -F, '{print $2}' c:/tmp/rows.csv",
    # The same shapes with the script quoted the other way, and with an option before it, so the
    # clause cannot be satisfied by a quoting accident.
    "sed -n \"1,20p\" /tmp/snap_out.txt",
    "awk 'NR>1 {print}' /tmp/reach.txt",
]

SCRIPT_ARGUMENT_FORBIDDEN = [
    # The CONTROLS in the other direction, and they are what stop the clause from opening a hole:
    # the same utilities aimed INSIDE the tree must stay denied, on their real target rather than
    # on their script.
    "sed -n '40,60p' CLAUDE.md",
    "sed -n '1,2p' tools/audit/shell_read_guard.py",
    "awk '{print $1}' OPEN_ITEMS.md",
    "awk -F'|' '{print $2}' tools/audit/decisions/backbone_decisions.json",
    # A script-only invocation reading standard input is not a path read at all, but the repository
    # path here is the REAL target and must be caught: the script is dropped, the file is not.
    "sed 's/a/b/' STATUS.md",
]

SANCTIONED += SCRIPT_ARGUMENT_SANCTIONED
FORBIDDEN += SCRIPT_ARGUMENT_FORBIDDEN

# ── DENY-ON-INDETERMINATE: OI-300's shape (2), closed BY RULING rather than by code ───────────
# The family ruling's clause 4: an unexpanded shell variable is INDETERMINATE, and deny-on-
# indeterminate is adopted as standing policy. The asymmetry decides it, and the ruling states it
# in terms: a false deny costs a retry through the file tools; a false admit costs an unverified
# read through the very mount whose measured stale-content failure created D-253.
#
# So the two rows below are still DENIED and their denial is now CORRECT BY POLICY. They stay in
# the SANCTIONED list — they are real commands that read outside the tree, and moving them to
# FORBIDDEN would assert they are reads this rule prohibits, which they are not. What changes is
# that the published false-deny rate is reported BOTH raw and net of policy, so the revert
# condition is judged on denials the ruling has NOT accepted. Naming them here is what keeps the
# raw rate honest: a policy that quietly removed rows from the denominator would be a corpus
# chosen to make a guard look clean, which measures nothing (#19).
DENIAL_ACCEPTED_BY_POLICY = {
    "tail \"$SC/guards1.txt\"":
        "OI-300 shape (2) — `$SC` is an unexpanded variable holding the session scratchpad, which "
        "is outside the working tree. The guard reads arguments literally and cannot know that; "
        "under clause 4 of the family ruling the indeterminate case is denied.",
    "cat \"$SC/tasks/abc.output\" 2>/dev/null | tail -20":
        "OI-300 shape (2) again, beside a redirection. The redirection half is fixed by clause 3 "
        "of the design; what still denies this row is the unexpanded variable, which clause 4 is "
        "denied on purpose.",
}


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

    # The 2026-08-08 FAMILY, measured the same way and on the SAME extended corpus, so the delta
    # reported is the family's and not the corpus extension's (D-436).
    fam_off_false = sum(1 for c in SANCTIONED if decide(c, family=False)[0])
    fam_off_caught = sum(1 for c in FORBIDDEN if decide(c, family=False)[0])
    fam_off_missed = [c for c in FORBIDDEN if not decide(c, family=False)[0]]
    # ASSUMPTION A5, DISCHARGED BY MEASUREMENT: every row the corpus carried BEFORE the family is
    # decided both ways, and each moved verdict is named so it can be read against the design.
    a5_moved = [
        {"command": c,
         "list": "sanctioned" if c in SANCTIONED_BEFORE_THE_FAMILY else "forbidden",
         "without_the_family": "DENY" if decide(c, family=False)[0] else "allow",
         "with_the_family": "DENY" if decide(c)[0] else "allow"}
        for c in list(SANCTIONED_BEFORE_THE_FAMILY) + list(FORBIDDEN_BEFORE_THE_FAMILY)
        if decide(c, family=False)[0] != decide(c)[0]
    ]
    # The 2026-08-11 SCRIPT-ARGUMENT clause, measured the same way and on the SAME extended corpus,
    # so the delta reported is the clause's and not the corpus rows' (D-436).
    sa_off_false = sum(1 for c in SANCTIONED if decide(c, script_argument=False)[0])
    sa_off_caught = sum(1 for c in FORBIDDEN if decide(c, script_argument=False)[0])
    sa_off_missed = [c for c in FORBIDDEN if not decide(c, script_argument=False)[0]]
    # Every row the corpus carried BEFORE the clause is decided both ways, and each moved verdict is
    # named. A row moving here that the clause's own shape does not name is a STOP, not a result.
    sa_moved = [
        {"command": c,
         "list": "sanctioned" if c in SANCTIONED_BEFORE_THE_SCRIPT_ARGUMENT else "forbidden",
         "without_the_clause": "DENY" if decide(c, script_argument=False)[0] else "allow",
         "with_the_clause": "DENY" if decide(c)[0] else "allow"}
        for c in list(SANCTIONED_BEFORE_THE_SCRIPT_ARGUMENT)
        + list(FORBIDDEN_BEFORE_THE_SCRIPT_ARGUMENT)
        if decide(c, script_argument=False)[0] != decide(c)[0]
    ]
    # The false denies, split by whether the ruling ACCEPTS the denial. The revert condition is
    # judged on the unaccepted ones; the raw list stays visible so nothing leaves the denominator.
    accepted = [c for c in still_false if c in DENIAL_ACCEPTED_BY_POLICY]
    unaccepted = [c for c in still_false if c not in DENIAL_ACCEPTED_BY_POLICY]
    stale_policy = [c for c in DENIAL_ACCEPTED_BY_POLICY if c not in still_false]
    if stale_policy:
        # An accepted denial that no longer happens is the same defect as an unrecorded one, in
        # the other direction: the policy would go on excusing something the guard has stopped
        # doing, and the next real false deny on that row would read as accepted.
        raise SystemExit(
            "STOP: a denial recorded as accepted by policy is no longer a denial — remove it from "
            f"DENIAL_ACCEPTED_BY_POLICY or say why it is kept: {stale_policy}")

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
            "start, PowerShell since 2026-08-08 (OI-345). ★ SINCE THE FAMILY RULING of "
            "2026-08-08 it also covers a command carried inside a WRAPPER's quoted code "
            "argument (`bash -c`, `sh -c`, `powershell(.exe) -Command`, `pwsh -Command`), which "
            "is re-run through this same decision; an INTERPRETER's code string (`python -c`, "
            "`perl -e`, and a heredoc body fed to one), by POLICY, when it carries a literal "
            "repository path; and a HASHLESS `git diff` aimed at a working-tree path.",
            "★ THE STATED CEILING (#19): interpreter code whose path is COMPUTED rather than "
            "written carries no literal for the policy to see, and is admitted. The guard cannot "
            "parse interpreter code, and a proxy pretending otherwise is what #17(d) forbids. A "
            "row of exactly that shape is in the corpus and is reported as missed, so the "
            "published deny rate states the ceiling rather than being silent about it.",
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
                       "false_deny_rate": round(false_denies / len(san), 3),
                       "false_denies_ACCEPTED_BY_POLICY": accepted,
                       "false_denies_NOT_accepted": unaccepted,
                       "what_the_split_is_for": (
                           "The family ruling's clause 4 adopts DENY-ON-INDETERMINATE as standing "
                           "policy for OI-300's shape (2), the unexpanded shell variable. A "
                           "denial the ruling accepts is not a defect, but removing it from the "
                           "denominator would be a corpus chosen to make a guard look clean, "
                           "which measures nothing (#19). So the raw rate above counts every "
                           "denial and the revert condition is judged on the NOT-accepted list."),
                       "rows": san},
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
            "★_superseded_by_the_2026_08_08_family": (
                "Every line of the list immediately above is answered by the family ruling of "
                "2026-08-08 and is left standing rather than edited, because it is the record of "
                "what the dialect widening did (#12). The wrapper form now recurses, the "
                "interpreter read is decided by policy, and OI-300's shapes (2)–(5) are all "
                "answered — (2) by ruling, (3), (4) and (5) by code. See the block below."
            ),
        },
        "★_the_2026_08_08_guard_family_and_the_corpus_it_is_measured_on": {
            "the_ruling": (
                "User, 2026-08-08 (`cowork_ruling_guard_family_2026_08_08.md`, with "
                "`OPEN_ITEMS.md` OI-351 folded in by Ruling 3 of "
                "`cowork_rulings_2026_08_08_pre_away.md`): ONE design over the whole enumerated "
                "family — OI-300's shapes (1)-(5) and OI-348's two — never per symptom, applying "
                "the standing one-fix-per-family rule of 2026-07-28. The mechanism change is "
                "licensed by that ruling (D-436)."
            ),
            "why_the_corpus_came_first": (
                "The ruling's clause 5 fixes the order, in the words the OI-343 and OI-345 rulings "
                "fixed it: every shape enters the corpus BEFORE one line of the mechanism moves, "
                "the blindness is measured at the UNWIDENED guard, and both rates are published on "
                "the SAME extended corpus. Measured here rather than argued — at the unwidened "
                "guard every path-form row was ADMITTED, `cat` and `grep` aimed at repository "
                "files among them, and the guard returned \"no text utility is aimed at a "
                "repository path\" for each."
            ),
            "the_five_design_clauses_as_built": {
                "1_wrapper_recursion": (
                    "`bash -c`, `sh -c`, `powershell(.exe) -Command`, `pwsh -Command` and kin: the "
                    "code string is re-run through this module's own decision, with the matching "
                    "dialect branch. Composition of the established POSIX and PowerShell branches "
                    "(#6), no new modeling. Bounded to three levels, because an unbounded "
                    "recursion on a crafted command is a guard that stops guarding. Closes "
                    "OI-348 shape 1."),
                "2_interpreter_code_by_policy_with_a_positive_bound": (
                    "`python -c` / `perl -e` and kin, and a heredoc body fed to one: a code string "
                    "carrying a LITERAL path THIS REPOSITORY HOLDS is DENIED; anything else is "
                    "admitted. Requiring the literal to exist is what keeps `print('hello world')` "
                    "from reading as a read. The computed-path residual is in the corpus and is "
                    "reported as missed, so the published rate states the ceiling (#19, #17(d)). "
                    "Closes OI-348 shape 2 TO THAT BOUND."),
                "3_the_false_deny_shapes_fixed_in_the_same_act": (
                    "Redirection operators and their targets are classified as non-path tokens "
                    "(OI-300 shape 5) — including the `&` of `2>&1`, which the lexer cuts into a "
                    "token of its own and which left a bare `1` reading as a path. Heredoc bodies "
                    "are excluded from COMMAND classification (shape 4), except where the heredoc "
                    "is fed to a SHELL, in which case the body IS shell and stays classified. And "
                    "a hashless `git diff` aimed at a working-tree path moves to the DENIED side "
                    "(shape 3), on the ABSENCE of a hash — the property that separates it from "
                    "every git form D-253 permits."),
                "4_shape_2_is_closed_BY_RULING_not_by_code": (
                    "DENY-ON-INDETERMINATE is adopted as standing policy for an unexpanded shell "
                    "variable. The asymmetry decides it, in the ruling's own words: a false deny "
                    "costs a retry through the file tools; a false admit costs an unverified read "
                    "through the very mount whose measured stale-content failure created D-253. "
                    "The two affected rows stay in the SANCTIONED list and their denials are "
                    "listed as accepted, so nothing leaves the denominator."),
                "5_order_and_establishment": (
                    "Corpus first; blindness at the unwidened guard; both rates on the same "
                    "extended corpus; the revert condition governs; a residual that survives is "
                    "recorded in this artifact, never silently."),
            },
            "★_OI_351_the_cause_ESTABLISHED_and_the_candidate_REFUTED": {
                "what_the_row_observed": "`ls` aimed at a repository path was ADMITTED by the LIVE "
                                         "hook on 2026-08-08, one day after the widening whose "
                                         "record says that shape is denied — while a `git status` "
                                         "a minute earlier was denied.",
                "the_two_candidates_the_row_named": ["the path form",
                                                     "the gap between the live hook and decide()"],
                "the_cause": (
                    "THE DRIVE LETTER'S CASE. `outside_repo` compared `os.path.commonpath(...)` "
                    "against `ROOT` with `!=` — a case-sensitive string comparison on a platform "
                    "whose paths are case-insensitive — and `ntpath.commonpath` takes the drive "
                    "from the token AS WRITTEN. A path spelled `c:/s/MS/…` produced `c:\\s\\MS`, "
                    "which is not the string `C:\\s\\MS`, so it read as OUTSIDE the repository. "
                    "Fixed with `os.path.normcase` on both sides: on Windows it lowercases and "
                    "squares the separators; on POSIX it is the identity, so nothing moves there."),
                "★_it_is_not_an_ls_defect": (
                    "The corpus carries `cat` and `grep` — the guard's oldest vocabulary — aimed "
                    "at repository files in the same spelling, and at the unwidened guard both "
                    "are admitted. OI-351's title names `ls` because `ls` is what was observed, "
                    "not because the hole had a vocabulary."),
                "the_second_candidate_is_REFUTED_by_observation": (
                    "The live hook and `decide()` agree on BOTH live decisions the record holds: "
                    "the `ls` OI-351 records as ADMITTED is admitted by `decide()` on the same "
                    "string, and the `ls -la /c/s/MS/…` the 2026-08-08 away batch issued as its "
                    "first command was DENIED by the live hook and is denied by `decide()` on the "
                    "same string. NO NEW FORBIDDEN COMMAND WAS ISSUED to test this: performing "
                    "the violation in order to measure the guard is not a measurement anyone may "
                    "take."),
            },
            "detection_on_the_forbidden_set_SAME_corpus": {
                "with_the_family": caught, "without_it": fam_off_caught, "of": len(forb),
                "what_the_family_newly_catches": sorted(
                    c for c in fam_off_missed if c not in still_missed),
                "what_is_STILL_missed": still_missed,
                "what_the_remaining_miss_IS": (
                    "TWO shapes as of 2026-08-11, and the second is NEW — surfaced by a corpus row "
                    "this act added and REPORTED rather than tuned away. (1) The stated ceiling: "
                    "interpreter code that COMPUTES its path, so no literal in it names anything "
                    "the repository has; the design says in terms that this is where the policy "
                    "stops. (2) A SEPARATOR CHARACTER INSIDE A QUOTED OPTION — `awk -F'|' … "
                    "<repository path>`. Diagnosed at the decision function and not reasoned from "
                    "the source: the lexer does not group that quoting shape, so the tokens come "
                    "out split at the `|` and the segment carrying the repository path has no "
                    "utility at its head. **It is NOT a defect of the script-argument clause and "
                    "the clause does not reach it** — the same command with a comma delimiter is "
                    "denied correctly. It is the 2026-08-04 segmentation class, one quoting shape "
                    "further out, and repairing it is a further mechanism change that Ruling 50 "
                    "does not license. **The row STAYS in the forbidden corpus**: removing a row "
                    "because the guard misses it is a corpus chosen to make a guard look clean, "
                    "which measures nothing (#19)."),
            },
            "false_denies_on_the_sanctioned_set_SAME_corpus": {
                "with_the_family": false_denies, "without_it": fam_off_false, "of": len(san),
                "not_accepted_by_policy": unaccepted,
                "the_revert_condition": (
                    "The ruling says a MATERIAL RISE IN FALSE DENIALS governs — revert and report. "
                    "Both values are measured on the SAME extended corpus, so the comparison is of "
                    "the family and not of the rows added with it. The condition is NOT met: the "
                    "count falls, and every denial that remains is one clause 4 of the design "
                    "accepts on purpose."),
            },
            "★_assumption_A5_no_verdict_moves_except_where_the_design_says_it_does": {
                "what_was_checked": "Every row the corpus carried BEFORE this act, decided with "
                                    "the family off and again with it on; every moved verdict is "
                                    "named here so it can be read against the design.",
                "rows_checked": len(SANCTIONED_BEFORE_THE_FAMILY)
                                + len(FORBIDDEN_BEFORE_THE_FAMILY),
                "verdicts_that_moved": a5_moved,
                "how_to_read_it": (
                    "A moved verdict is expected HERE and only here, because the design names "
                    "these shapes: a sanctioned row moving DENY->allow is one of OI-300's "
                    "measured false denies being removed (shape 4, the heredoc body; shape 5, the "
                    "redirections), and a forbidden row moving allow->DENY is one of OI-348's "
                    "shapes being caught (shape 1, the wrappers; shape 2, the interpreter). A "
                    "moved verdict of any OTHER shape would be this act reaching past its ruling."),
            },
            "★_the_2026_08_11_maintenance_act_ONE_family_TWO_defects": {
                "the_ruling": "User, 2026-08-11, Ruling 50 of "
                              "`cowork_rulings_2026_08_11_tenth_stop.md`: DIAGNOSIS FIRST, with a "
                              "STOP between diagnosis and fix; then the fix under the family "
                              "discipline's fixed order — corpus rows first, both rates "
                              "re-measured on the same extended corpus, the revert condition "
                              "governing. `OPEN_ITEMS.md` OI-355 rides it under Ruling 19 of "
                              "2026-08-09.",
                "the_script_argument_clause_OI_355": {
                    "what_it_is": "`sed` and `awk` take a SCRIPT in the position `grep` takes a "
                                  "pattern, and only the pattern-taking four carried the "
                                  "correction that drops it — so a bare script resolved against "
                                  "the working directory and read as a repository path, denying "
                                  "the command before its real target was considered.",
                    "false_denies": {"with_the_clause": false_denies, "without_it": sa_off_false,
                                     "of": len(san)},
                    "detection": {"with_the_clause": caught, "without_it": sa_off_caught,
                                  "of": len(forb)},
                    "forbidden_rows_of_this_shape_still_missed": [
                        c for c in SCRIPT_ARGUMENT_FORBIDDEN if c in still_missed],
                    "sanctioned_rows_of_this_shape_still_denied": [
                        c for c in SCRIPT_ARGUMENT_SANCTIONED if c in still_false],
                    "the_revert_condition": (
                        "A material rise in false denials governs. Both values are measured on "
                        "the SAME extended corpus, so the comparison is of the CLAUSE and not of "
                        "the rows added with it — which is the order the family ruling fixes and "
                        "which this act followed: the rows went in before the clause, so the "
                        "blindness was measured at the unwidened guard."),
                    "verdicts_that_moved_among_rows_the_corpus_ALREADY_HELD": sa_moved,
                    "how_to_read_a_movement": (
                        "A moved verdict is expected only where the clause's own shape names it — "
                        "a `sed` or `awk` invocation whose script was being read as a path. A "
                        "movement of any other shape would be this act reaching past its ruling."),
                },
                "the_ROOT_determinism_fix_OI_366": {
                    "the_cause_ESTABLISHED_AT_THE_OBJECTS": (
                        "`ROOT` is derived from `__file__`, which Python makes absolute against "
                        "the process's own current directory, so the DRIVE LETTER'S CASE arrived "
                        "in whatever spelling the invocation used. The FAMILY arm normcases both "
                        "sides and is unaffected; the CONTROL arm restores the case-SENSITIVE "
                        "comparison on purpose and compares against `ROOT` as written, so a "
                        "lowercase drive letter moved that arm's verdicts and only that arm's — "
                        "which is exactly the shape of a check reporting STALE on one invocation "
                        "and re-deriving on the next with nothing edited between."),
                    "how_it_was_established": (
                        "The module was loaded twice from its own file, once under each spelling, "
                        "each load re-running `establish()` and applying the SAME string-equality "
                        "test `--check` applies. The uppercase load re-derives the committed "
                        "artifact byte for byte; the lowercase load does not. The probe ran "
                        "OUTSIDE this tool, which is what let the diagnosis be taken before any "
                        "guard file was touched, as the ruling requires."),
                    "the_fix": "`_canonical_drive` puts the drive letter in ONE case at module "
                               "load, so `ROOT` no longer depends on how the process started.",
                    "what_it_moves": (
                        "NO LIVE VERDICT. The family arm — which is what the live hook decides on "
                        "— normcases both sides and never saw the difference. What changes is that "
                        "the control arm, and therefore this artifact and the `--check` verdict "
                        "over it, are REPRODUCIBLE ON DEMAND, which is what #19 asks of an "
                        "established value. The published deny and false-deny rates are the same "
                        "values they were."),
                },
            },
            "★_what_the_PREVIOUS_published_rates_did_and_did_not_bound": (
                "The rates published before 2026-08-08's family act are NOT WITHDRAWN AS WRONG "
                "(#12): they were correct for the corpus they were measured on and they re-derived "
                "exactly. What they did not do is bound the guard on any member of this family — "
                "the wrappers, the interpreters, and every repository path written with a "
                "lowercase drive letter. BLIND, NOT WRONG, for the third time in this file, which "
                "is the reason #19 asks for positive establishment rather than for a check that "
                "has not yet failed."
            ),
            "what_this_act_deliberately_does_NOT_touch": [
                "The computed-path residual above, which is the design's stated bound.",
                "`git log` and `git rev-parse HEAD`, still deliberately unenforced: no tool "
                "replaces them, so denying them would fire on legitimate work.",
                "Whether the guard is ARMED, which is the user's act and not this module's.",
                "A command with more than one heredoc, or one introduced past the first line: "
                "the body model is one heredoc per command and says so.",
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
    try:
        deny, reason = decide(command)
    except Exception:                   # noqa: BLE001
        # A guard that crashes on a strange command is a guard that stops guarding — this
        # module's own stated principle, applied to itself at the point where it decides. The
        # 2026-08-08 family added a heredoc splitter, a wrapper recursion and an interpreter
        # policy to this path; any one of them meeting a command shape nobody anticipated must
        # cost an ADMISSION, never a broken tool call. `--establish` has no such catch, so a
        # crash is still loud where it can be read.
        return 0
    if deny:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
