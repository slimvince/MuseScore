#!/usr/bin/env python3
"""WHAT AN ORDINARY SESSION READS AT SESSION START, MEASURED — and what the last change to it cost.

WHY THIS EXISTS.  The pruning arc's whole subject is the size of the mandatory session-start read
(the user's direction of 2026-08-16: *"the mandatory reads at session start for you and CC are too
large"*).  Every act in that arc has had to state what it saved, and every one of those values has
so far been measured by hand at git objects and typed into a record.  A figure enters a report by
citation to a generated artifact and never by transcription (`CLAUDE.md` #17f, register entry
D-431), so the measurement is generated here.  Built by `cc_instruction_preparation_tenth.md`
Task 2, whose step 6 orders the effect published with each value read from the files at explicit
objects and not estimated.

WHAT IS AUTHORED AND WHAT IS DERIVED
------------------------------------
authored : the MEMBERSHIP of the ordinary session-start read — the whole documents a session must
           read — each with the clause in `CLAUDE.md` that makes it one.  Three of them, and the
           table is small because the read is.  A CONDITIONAL read (`BUILD_AND_TEST.md`,
           `docs/scoring_model.md`, the joint estimator's section) is NOT a member: it is read by
           the sessions its condition names and not by an ordinary one, which is what CONDITIONAL
           means.
derived  : the FOURTH member — the artifact and key rule (a) names — parsed from rule (a)'s own
           clause rather than listed here, so a later narrowing of that pointer moves this
           measurement without anybody editing this tool; every member's character count; the
           total; and the same total at each recorded earlier commit, read from the git OBJECT at
           an explicit hash.

HOW A KEY'S SIZE IS COUNTED, stated because a convention nobody states is a convention nobody can
check.  The artifact is written with one-space indentation, so a key's span runs from the line that
opens it to the line that opens the next key at the SAME indentation.  The size is the number of
characters of that span — what a reader actually reads, not a re-serialisation.

THE STOPS
  * rule (a)'s clause naming a path the tree does not have, or a key chain the artifact does not
    carry, is a STOP: the pointer a session is told to read must resolve, and a pointer that has
    stopped resolving is exactly the failure this measurement would otherwise hide;
  * an authored member the tree does not have is a STOP;
  * an earlier reading whose commit cannot be read is a STOP rather than a silently dropped row —
    a comparison that quietly loses its baseline reports a saving nobody can check.

WHAT THIS DOES NOT ASSERT.  That the membership is complete: it is AUTHORED, and a mandatory read
added to `CLAUDE.md` without being added here would not appear.  That is why each member carries
the clause it comes from, so the authored half is checkable by reading four clauses rather than a
file.  And it asserts nothing about whether the read is small enough — that is [[OI-370]]'s own
subject.

Run:
    python tools/audit/gen_session_start_read_size.py
    python tools/audit/gen_session_start_read_size.py --check
"""
from __future__ import annotations

import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "session_start_read_size.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

# ── AUTHORED — the whole documents an ordinary session reads, with the clause that makes each one
# a member.  Every citation below was READ IN THIS SESSION, in `CLAUDE.md`, with the file tools.
MEMBERS: tuple[tuple[str, str], ...] = (
    ("CLAUDE.md",
     "the project instructions themselves, which every clause below is written in"),
    ("STATUS.md",
     "`CLAUDE.md`, the build-and-test section's opening list: \"Always read these two files at the "
     "start of every session\""),
    ("DECISIONS.md",
     "the same list, and the decisions register's own rule (a) — \"read the INDEX `DECISIONS.md` "
     "at session start\" — explicitly NOT demoted to a conditional read on 2026-08-17"),
)

# The earlier readings this measurement compares against. Each is read at its git OBJECT by
# explicit hash; no value is carried in this file.
BASELINES: tuple[tuple[str, str], ...] = (
    # WHY THE COMPARISON STARTS HERE AND NOT EARLIER, stated because a bounded comparison that does
    # not say where its bound is reads as the whole story. Before the ninth batch the read regime
    # named a DIFFERENT MEMBER SET — `OPEN_ITEMS.md` whole, `BUILD_AND_TEST.md` unconditionally —
    # and rule (a) named no artifact-and-key pointer at all, so this measurement's shape does not
    # reach it and forcing it would compare two different questions. The cross-regime figures for
    # that arc are recorded in the ruling records that took them and are not re-derived here (#6).
    ("1760d9a4a87f82a6bdbc7cb17e99ccdd8ae4c433",
     "the preparation phase's NINTH batch terminus — this batch's own base, and the state rule "
     "(a)'s pointer was narrowed from"),
)

RULE_A = re.compile(r"Rules:\s*\(a\)(.*?);\s*\(b\)", re.S)
POINTER = re.compile(r"`([A-Za-z0-9_./-]+\.json)`((?:\s*→\s*`[^`]+`)+)")
KEY = re.compile(r"`([^`]+)`")


class Stop(Exception):
    """A demand of the measurement is unmet. Never a warning."""


def git_show(rev: str, path: str) -> str:
    proc = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{path}"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop(f"could not read {path} at the git object {rev[:10]} — "
                   f"{proc.stderr.decode('utf-8', 'replace').strip()}")
    return proc.stdout.decode("utf-8")


def at_tree(path: str) -> str:
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        raise Stop(f"an authored member is not in the tree: {path}")
    with io.open(full, encoding="utf-8") as fh:
        return fh.read()


def rule_a_pointer(claude_md: str) -> dict:
    """The artifact and key chain rule (a) tells a session to read, parsed from the clause itself.

    The FIRST chain rooted at a `.json` path is the read pointer. A later chain in the same clause
    — the grounds a session opens to challenge a verdict — is not what rule (a) sends it to at
    boot, and is reported separately rather than folded in.
    """
    m = RULE_A.search(claude_md)
    if not m:
        raise Stop("rule (a)'s clause could not be located in `CLAUDE.md`")
    clause = m.group(1)
    p = POINTER.search(clause)
    if not p:
        raise Stop("rule (a)'s clause names no artifact-and-key pointer")
    return {"artifact": p.group(1), "keys": KEY.findall(p.group(2)), "clause_characters": len(clause)}


def key_span_characters(text: str, keys: list[str]) -> int:
    """The characters of a key's span: its opening line to the next key at the same indentation."""
    lines = text.split("\n")
    lo, hi, indent = 0, len(lines), 0
    for depth, key in enumerate(keys, start=1):
        indent = depth
        opener = " " * indent + json.dumps(key, ensure_ascii=False) + ":"
        start = None
        for i in range(lo, hi):
            if lines[i].startswith(opener):
                start = i
                break
        if start is None:
            raise Stop(f"the key chain rule (a) names does not resolve: {keys!r} "
                       f"(stopped at {key!r})")
        end = hi
        for i in range(start + 1, hi):
            stripped = lines[i]
            if stripped.startswith(" " * indent + '"') and not stripped.startswith(" " * (indent + 1)):
                end = i
                break
        lo, hi = start, end
    return len("\n".join(lines[lo:hi]))


def measure(claude_md: str, reader) -> dict:
    """One reading of the whole session-start read, at whatever source `reader` supplies."""
    pointer = rule_a_pointer(claude_md)
    artifact_text = reader(pointer["artifact"])
    answer = key_span_characters(artifact_text, pointer["keys"])
    section = key_span_characters(artifact_text, pointer["keys"][:1])

    per_member = {}
    for path, _why in MEMBERS:
        per_member[path] = len(claude_md) if path == "CLAUDE.md" else len(reader(path))
    per_member[pointer["artifact"] + " → " + " → ".join(pointer["keys"])] = answer

    return {
        "the_pointer_rule_a_names": pointer,
        "characters_per_member": per_member,
        "total_characters": sum(per_member.values()),
        "the_section_that_carries_the_pointer": {
            "key": pointer["keys"][0],
            "characters": section,
            "what_it_is": "the whole section the artifact carries at that key — the answer TOGETHER "
                          "with the grounds that establish it. A session reads the answer at boot "
                          "and opens the rest to challenge a verdict.",
        },
        "characters_the_section_carries_beyond_the_answer": section - answer,
    }


def build() -> dict:
    now = measure(at_tree("CLAUDE.md"), at_tree)

    earlier = []
    for rev, what in BASELINES:
        reading = measure(git_show(rev, "CLAUDE.md"), lambda p, r=rev: git_show(r, p))
        earlier.append({
            "commit": rev,
            "what_that_commit_is": what,
            "total_characters": reading["total_characters"],
            "the_pointer_rule_a_named_there": reading["the_pointer_rule_a_names"],
            "characters_per_member": reading["characters_per_member"],
        })

    movement = []
    for row in earlier:
        delta = now["total_characters"] - row["total_characters"]
        movement.append({
            "from_commit": row["commit"],
            "from_total": row["total_characters"],
            "to_total": now["total_characters"],
            "change_in_characters": delta,
            "change_percent": round(100.0 * delta / row["total_characters"], 2),
        })

    return {
        "what_this_is":
            "WHAT AN ORDINARY SESSION READS AT SESSION START, in characters, measured at the tree "
            "and at each recorded earlier commit's git OBJECT. A MEASUREMENT ONLY: it edits "
            "nothing, moves no rule and grades nothing. Every value is computed; none is "
            "transcribed (D-431).",
        "generated_by": "tools/audit/gen_session_start_read_size.py",
        "generated_for": "cc_instruction_preparation_tenth.md, Task 2, step 6",
        "how_a_key_span_is_counted":
            "the artifact is written with one-space indentation, so a key's span runs from the "
            "line that opens it to the line that opens the next key at the SAME indentation, and "
            "the size is the characters of that span — what a reader reads, not a re-serialisation",
        "what_is_authored": "the membership of whole documents, each with the clause in "
                            "`CLAUDE.md` that makes it a member",
        "what_is_derived": "the artifact-and-key pointer, parsed from rule (a)'s own clause, so a "
                           "later narrowing moves this measurement without editing this tool; "
                           "every character count; the total; and each earlier reading",
        "the_membership": [{"document": p, "the_clause_that_makes_it_a_member": w}
                           for p, w in MEMBERS],
        "a_conditional_read_is_not_a_member":
            "`BUILD_AND_TEST.md`, `docs/scoring_model.md` and the joint estimator's section of "
            "`ARCHITECTURE.md` are read by the sessions their conditions name and not by an "
            "ordinary one, which is what CONDITIONAL means. Counting them would report a read no "
            "ordinary session takes.",
        "at_the_tree": now,
        "at_earlier_commits": earlier,
        "movement_against_each_earlier_reading": movement,
        "what_this_does_not_assert": [
            "That the membership is complete — it is AUTHORED, and a mandatory read added to "
            "`CLAUDE.md` without being added here would not appear. Each member carries the clause "
            "it comes from so the authored half is checkable by reading three clauses.",
            "That the read is small enough, which is [[OI-370]]'s own subject.",
            "That a session reads nothing else. A session opens the INDEX when it needs a row, the "
            "grounds when it challenges a verdict, and whatever its own dispatch orders; none of "
            "that is the session-start read.",
        ],
    }


def main(argv: list[str]) -> int:
    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        have = at_tree(os.path.relpath(OUT, ROOT).replace("\\", "/")) if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the measurement: session_start_read_size.json does not re-derive")
            return 1
        print("the session-start read measurement re-derives")
    else:
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote %s" % os.path.relpath(OUT, ROOT).replace("\\", "/"))
    now = art["at_the_tree"]
    print("  rule (a) points at %s -> %s"
          % (now["the_pointer_rule_a_names"]["artifact"],
             " -> ".join(now["the_pointer_rule_a_names"]["keys"])))
    for name, n in now["characters_per_member"].items():
        print("    %-70s %8d" % (name, n))
    print("  total at the tree %d" % now["total_characters"])
    for row in art["movement_against_each_earlier_reading"]:
        print("  vs %s: %d -> %d  (%+d, %+.2f%%)"
              % (row["from_commit"][:10], row["from_total"], row["to_total"],
                 row["change_in_characters"], row["change_percent"]))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print("STOP: %s" % exc)
        sys.exit(2)
