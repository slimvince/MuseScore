#!/usr/bin/env python3
"""THE ONE PLACE WHERE THIS PROJECT'S CHECKS MAKE THEIR OWN OUTPUT PRINTABLE.

WHAT THIS FIXES.  A check writes its artifact and then prints its findings.  On Windows, when
its standard output is anything other than an interactive console -- a pipe, a redirection to a
file, an agent harness capturing the run -- Python encodes that output with the locale codepage,
`cp1252` here, and the default error handler raises.  The first character outside `cp1252` ends
the process with a `UnicodeEncodeError` traceback, after a PREFIX of the findings has already
been printed.  A reader then sees a short list and a crash where the check had more to say.

Measured, 2026-08-03 (phase 1x, Task 1.1), at both tools the record names:

  * `tools/audit/decisions/gen_home_classification.py` died at its per-document movement line, on
    a MINUS SIGN (U+2212) in the tool's OWN format string, BEFORE reaching the `STALE vs the
    files:` block -- so the check exited non-zero having printed a clean-looking summary and none
    of what it found.  That is how `OPEN_ITEMS.md` OI-305 stayed unreported.
  * `tools/audit/process_check.py` died quoting an input document's own sentence, on a RIGHTWARDS
    ARROW (U+2192) in text it had READ, not written.

ONE CAUSE, TWO CHARACTER SOURCES.  Both are the same `UnicodeEncodeError` from the same
`cp1252` encoder on the same stream.  The character SOURCES differ -- the tool's own literal in
one, quoted repository prose in the other -- and that difference is why the author-side remedy
recorded at OI-297's phase-1u note (new tools print ASCII only, and say so in their source)
closes one of them and cannot close the other: a tool that prints text it read cannot promise
anything about that text.  A stream-level fix closes both, which is what this module is.

WHAT IT DOES, AND THE THING IT DELIBERATELY DOES NOT DO.  It reconfigures the standard streams
to UTF-8 with `backslashreplace`, so an unencodable character degrades to a visible escape
instead of ending the process.  It contains NO exception handling around anybody's print, sets
no exit code, and swallows nothing: a check that failed before this module still fails, with the
same status, and an unrelated traceback still reaches stderr.  That property is the point --
a guard that prints but no longer fails would be worse than one that fails invisibly -- and it
is measured rather than asserted, at `--establish` below.

`backslashreplace` rather than `replace`: an escape says which character was dropped, a question
mark does not (#12).  UTF-8 rather than the locale codepage: it is what `PYTHONIOENCODING=utf-8`
already did as the manual workaround when these findings had to be recovered by hand, and on a
real console Python already uses UTF-8, so this changes nothing there.

Run:
    python tools/audit/output_encoding.py --establish          # measure the fix, write the artifact
    python tools/audit/output_encoding.py --establish --check  # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
ESTABLISH_OUT = os.path.join(HERE, "output_encoding_establishment.json")

# The three characters the record has actually caught this on, plus one more that repository
# prose is full of.  Each is outside cp1252; each therefore ends a strict cp1252 print.
PROBE_CHARS = {
    "U+2212 MINUS SIGN": "−",
    "U+2192 RIGHTWARDS ARROW": "→",
    "U+2605 BLACK STAR": "★",
    "U+2713 CHECK MARK": "✓",
}


def use_utf8_output() -> None:
    """Make this process's stdout and stderr able to carry any character it is asked to print.

    Idempotent, and a no-op where the streams already encode UTF-8.  Never raises: a stream
    that cannot be reconfigured (one already replaced by a capture object without the method)
    is left exactly as it was, which is the behaviour that existed before this module.
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding="utf-8", errors="backslashreplace")
        except (ValueError, OSError):
            # A stream that refuses reconfiguration keeps its previous behaviour.  Reported by
            # --establish rather than silently assumed: see `streams` in the artifact.
            pass


# ── establishment ────────────────────────────────────────────────────────────
# Four probes, each a real child process with its stdout PIPED -- which is the failing condition,
# not a simulation of it.  Two measure that the fix removes the crash; two measure that it does
# not remove a failure that ought to happen.

_CHILD_PRINT = (
    "import sys\n"
    "{fix}"
    "print('LINE-1 ' + {payload!r})\n"
    "print('LINE-2 the line a crash on LINE-1 would have hidden')\n"
)

_CHILD_EXIT_1 = (
    "import sys\n"
    "sys.path.insert(0, {here!r})\n"
    "from output_encoding import use_utf8_output\n"
    "use_utf8_output()\n"
    "print('findings: ' + {payload!r})\n"
    "sys.exit(1)\n"
)

_CHILD_RAISE = (
    "import sys\n"
    "sys.path.insert(0, {here!r})\n"
    "from output_encoding import use_utf8_output\n"
    "use_utf8_output()\n"
    "print('findings: ' + {payload!r})\n"
    "raise RuntimeError('a real failure, unrelated to encoding')\n"
)

_FIX_LINES = (
    "sys.path.insert(0, {here!r})\n"
    "from output_encoding import use_utf8_output\n"
    "use_utf8_output()\n"
)


def _run_child(source: str) -> dict:
    """Run a child with stdout and stderr PIPED (never a console) and report what came back."""
    env = dict(os.environ)
    # PYTHONIOENCODING was the manual workaround; leaving it set would establish the workaround
    # rather than the fix.
    env.pop("PYTHONIOENCODING", None)
    proc = subprocess.run(
        [sys.executable, "-c", source],
        capture_output=True, env=env, cwd=ROOT,
    )
    out = proc.stdout.decode("utf-8", errors="replace")
    err = proc.stderr.decode("utf-8", errors="replace")
    return {
        "exit_code": proc.returncode,
        "stdout_lines": [ln for ln in out.splitlines() if ln],
        "stderr_has_unicodeencodeerror": "UnicodeEncodeError" in err,
        "stderr_has_traceback": "Traceback (most recent call last)" in err,
    }


def establish() -> dict:
    payload = " ".join(PROBE_CHARS.values())

    unfixed = _run_child(_CHILD_PRINT.format(fix="", payload=payload))
    fixed = _run_child(_CHILD_PRINT.format(fix=_FIX_LINES.format(here=HERE), payload=payload))
    exit_1 = _run_child(_CHILD_EXIT_1.format(here=HERE, payload=payload))
    raised = _run_child(_CHILD_RAISE.format(here=HERE, payload=payload))

    def _both_lines(r: dict) -> bool:
        return (any(ln.startswith("LINE-1") for ln in r["stdout_lines"])
                and any(ln.startswith("LINE-2") for ln in r["stdout_lines"]))

    def _chars_survived(r: dict) -> dict:
        joined = "\n".join(r["stdout_lines"])
        return {name: (ch in joined) for name, ch in PROBE_CHARS.items()}

    probes = {
        "1_without_the_fix_the_print_crashes": {
            "what_it_measures": "That the failing condition is real and reproduces here: a piped "
                                "stdout, four characters outside cp1252, no fix applied.",
            "expected": "non-zero exit, a UnicodeEncodeError, and stdout TRUNCATED after the "
                        "prefix -- LINE-2 never printed.",
            "observed": unfixed,
            "printed_both_lines": _both_lines(unfixed),
            "verdict": "REPRODUCES" if (unfixed["exit_code"] != 0
                                        and unfixed["stderr_has_unicodeencodeerror"]
                                        and not _both_lines(unfixed)) else "DID NOT REPRODUCE",
        },
        "2_with_the_fix_the_whole_output_arrives": {
            "what_it_measures": "That the fix removes the crash AND loses no line -- the finding "
                                "that used to be hidden is printed.",
            "expected": "exit 0, no UnicodeEncodeError, both lines present, every probe "
                        "character carried through.",
            "observed": fixed,
            "printed_both_lines": _both_lines(fixed),
            "characters_survived": _chars_survived(fixed),
            "verdict": "FIXED" if (fixed["exit_code"] == 0
                                   and not fixed["stderr_has_unicodeencodeerror"]
                                   and _both_lines(fixed)
                                   and all(_chars_survived(fixed).values())) else "NOT FIXED",
        },
        "3_a_deliberate_non_zero_exit_still_exits_non_zero": {
            "what_it_measures": "The negative control the dispatch names: a guard that now prints "
                                "but no longer FAILS is worse than one that fails invisibly.",
            "expected": "exit 1, findings printed in full.",
            "observed": exit_1,
            "verdict": "FAILURE PRESERVED" if (exit_1["exit_code"] == 1
                                               and exit_1["stdout_lines"]) else "FAILURE MASKED",
        },
        "4_an_unrelated_exception_still_ends_the_process": {
            "what_it_measures": "That the module handles no one else's exceptions: a real fault "
                                "still raises, still prints its traceback, still exits non-zero.",
            "expected": "non-zero exit, a traceback on stderr that is NOT a UnicodeEncodeError.",
            "observed": raised,
            "verdict": "EXCEPTION PRESERVED" if (raised["exit_code"] != 0
                                                 and raised["stderr_has_traceback"]
                                                 and not raised["stderr_has_unicodeencodeerror"])
                       else "EXCEPTION SWALLOWED",
        },
    }

    return {
        "purpose": "The measured establishment of tools/audit/output_encoding.py: that it removes "
                   "the truncation, and that it removes nothing else.",
        "generated_by": "tools/audit/output_encoding.py --establish",
        "generated_for": "cc_instruction_phase1x_guard_visibility_and_commit.md, Task 1.3",
        "the_row_it_answers": "OPEN_ITEMS.md OI-297 -- the class, not the one tool. The two "
                              "phase-1w members are named in this module's docstring.",
        "the_failing_condition": {
            "what_it_is": "stdout that is not an interactive console. Measured in this run, "
                          "below -- the establishment does not assume it.",
            "child_stdout_is_a_pipe": True,
            "parent_stdout_encoding": sys.stdout.encoding,
            "parent_stdout_isatty": sys.stdout.isatty(),
        },
        "probe_characters": {k: hex(ord(v)) for k, v in PROBE_CHARS.items()},
        "probes": probes,
        "verdicts": {k: v["verdict"] for k, v in probes.items()},
        "established": all(v["verdict"] in ("REPRODUCES", "FIXED", "FAILURE PRESERVED",
                                            "EXCEPTION PRESERVED") for v in probes.values()),
    }


def main(argv: list[str]) -> int:
    use_utf8_output()
    if "--establish" not in argv:
        print(__doc__.strip().splitlines()[0])
        print("nothing to do: this module is imported by the checks; --establish measures it.")
        return 0

    artifact = establish()
    text = json.dumps(artifact, indent=2, ensure_ascii=False) + "\n"

    if "--check" in argv:
        have = open(ESTABLISH_OUT, encoding="utf-8").read() if os.path.exists(ESTABLISH_OUT) else ""
        if have != text:
            print("STALE vs the check: output_encoding_establishment.json does not re-derive")
            return 1
        print("the output-encoding establishment artifact re-derives")
    else:
        open(ESTABLISH_OUT, "w", encoding="utf-8", newline="").write(text)
        print(f"wrote {os.path.relpath(ESTABLISH_OUT, ROOT)}")

    for name, verdict in artifact["verdicts"].items():
        print(f"  {name}: {verdict}")
    print(f"established: {artifact['established']}")
    return 0 if artifact["established"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
