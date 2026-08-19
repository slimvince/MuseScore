#!/usr/bin/env python3
"""THE EPOCH-PINNED PASSES, AND WHAT EACH ONE'S WRITE PATH RESOLVES — derived, published, and
authorizing nothing.

THE RULING THIS EXISTS FOR (user, 2026-08-19, Ruling 3 of
`cowork_rulings_2026_08_19_eleventh_return.md`), quoted verbatim:

    The enumeration is published as data. Each pass is corrected only when a ruled act needs its
    write path, and the published enumeration is the standing input to that act rather than a work
    list.

WHAT AN EPOCH-PINNED PASS IS.  A pass whose `--check` does not re-derive at the tree but at the
commit its OWN COMMITTED ARTIFACT RECORDS, so that the check passes indefinitely rather than going
red the first time anybody commits anything — the pattern register entry **D-646** names.  The
commit is read back out of the artifact the pass itself wrote.

THE DEFECT THIS ENUMERATES, and it is FINDING F77's own shape.  A pass reads the recorded commit on
the CHECK path and resolves `HEAD` on the WRITE path.  The two paths then ask different questions:
the check asks *does the artifact still re-derive at the commit it records*, and the write asks
*what does the tree say today*.  Nobody finds out until a ruled act needs a re-render — and F77's
measured instance is that the asymmetric run does not merely DIFFER, it STOPS, because the
population the pass reads at `HEAD` is no longer the population its recorded commit carries.

★ WHAT THIS AUTHORIZES: NOTHING.  It corrects no write path, edits no enumerated pass, and grades no
member as owed.  The ruling above says each pass is corrected only when a ruled act needs its write
path, and this artifact is the STANDING INPUT to such an act — never a work list.

HOW THE POPULATION IS DERIVED, so that no member is hand-listed (D-431)
----------------------------------------------------------------------
Every `*.py` under `tools/` is parsed with the standard library's own syntax tree.  For each:

  OWN OUTPUTS      a module-level constant bound to a path AND used as a write target, in the two
                   idioms the tools actually use — `NAME.write_text(...)` and `open(NAME, "w"...)`.
  THE SPLIT        inside the tool's `main`, every top-level `if` whose test carries the literal
                   `--check` or `--verify`, or a local name `main` itself bound from such a literal
                   (the `check = "--check" in argv` idiom).  Those bodies are the CHECK path;
                   EVERYTHING ELSE in `main`, including such an `if`'s `else`, is the WRITE path.
  A READ-BACK      a `.get("…commit…")` or `["…commit…"]` whose receiver traces to one of that
                   tool's own outputs being read — through a direct `read_text`/`json.load(...)`
                   chain, through a local bound from one, or through a `with open(OUT) as fh`
                   handle.
  A MEMBER         a tool whose CHECK path carries a read-back.  That is what makes it epoch-pinned.
  THE VERDICT      SYMMETRIC where the WRITE path carries a read-back too; ASYMMETRIC where it does
                   not and carries the literal `HEAD` instead; UNPLACED where it does neither.

THE UNPLACED MEMBERS ARE RETURNED TO THE USER, AND THE RECONCILIATION IS THE STOP.  A member the
recognizers cannot place is never guessed into one of the two verdicts.  It is published as
UNPLACED with the shape the derivation CAN see, and it is a standing STOP-and-report to the user.
What makes that a guard rather than a note is the both-ways reconciliation against the authored,
published set below: a member the derivation cannot place that is NOT in that set halts the run, so
a new unrecognised shape cannot enter silently; and an authored member the derivation now DOES
place halts it too, so an authored reason cannot outlive its subject.

ESTABLISHMENT (#19) — TWO SEEDS, RE-CHECKED ON EVERY RUN.  The record already establishes two
members at the code, one on each side, and the derivation must reproduce both or halt:
`gen_ratified_document_check.py` was corrected to the symmetric shape at
`cc_instruction_preparation_eleventh_amended.md` Task 3 and declared there, and
`gen_artifact_inventory.py` resolves `HEAD` on its write path unconditionally.  A recognizer that
stops reproducing either has stopped recognizing the thing it was built for, and says so by halting
rather than by publishing a smaller population.

THE BOUND — WHAT IT READS, AND WHAT IT CANNOT SEE.  Stated because a derivation over source is a
recognizer over code and not a run of it:

  * It reads SOURCE, never a run.  It reports what each path is written to resolve; it does not
    report what a run would do, and it cannot tell an asymmetric member that would merely differ
    from one that would STOP — that turns on the population the pass reads at `HEAD`, which is a
    property of the tree on the day of the run.
  * It reads the statements of `main` ONLY.  A commit resolved inside a helper that `main` calls —
    a builder's own default argument, for instance — is invisible to it, and so is a tool whose
    check/write split lives outside `main`.  A member of that shape lands in UNPLACED rather than
    being guessed.
  * It reads a tool's OWN outputs.  A pass pinned at the commit ANOTHER tool's artifact records is
    outside this population by construction, having no self-recorded commit for its two paths to
    disagree about.
  * A COMPUTED key name or a COMPUTED output path carries no literal to find, the same bound the
    retirement caller-check publishes of itself.
  * It recognises the read-back by the KEY carrying the word `commit`.  A pass recording its epoch
    under a differently-worded key reports as a non-member, which is the recoverable direction: a
    missing member is a question, a wrongly placed one is a false statement about a write path.

Run:
    python tools/audit/gen_epoch_write_path.py
    python tools/audit/gen_epoch_write_path.py --check
"""
from __future__ import annotations

import ast
import io
import json
import os
import re
import sys
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(HERE, "epoch_write_path.json")

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

TOOL_DIRS = ("tools",)
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv",
             "ninja_build_rel", "build.release", "corpus", "dcml"}

CHECK_FLAGS = ("--check", "--verify")
READ_IDIOMS = ("read_text", "json.load", "open(")

SYMMETRIC = "SYMMETRIC — the write path reads the commit the committed artifact records"
ASYMMETRIC = "ASYMMETRIC — the write path carries the literal HEAD and no read-back"
UNPLACED = "UNPLACED — the write path carries neither, and the resolution is outside what `main` shows"

# ── AUTHORED: the two members the record already establishes at the code, one per verdict ──────
# Neither is a member list — the population is derived. These are the ESTABLISHMENT, re-checked on
# every run, and a disagreement halts the derivation rather than being published.
SEEDS = {
    "tools/audit/gen_ratified_document_check.py": (
        SYMMETRIC,
        "corrected to the symmetric shape at `cc_instruction_preparation_eleventh_amended.md` "
        "Task 3 and DECLARED as a judgment there, in that batch's report and close; the comment "
        "block above its write path states the correction and its measured ground"),
    "tools/audit/gen_artifact_inventory.py": (
        ASYMMETRIC,
        "its write path resolves HEAD unconditionally and reads no recorded commit back, while its "
        "check path re-derives at the commit its committed artifact records — read at the code, "
        "2026-08-19"),
}

# ── AUTHORED: the members the recognizers cannot place, each with the shape they CAN see ───────
# Reconciled BOTH ways against the derivation on every run. Each reason was read in the tool it
# names, with the file tools, on 2026-08-19.
UNPLACED_RETURNED_TO_THE_USER = {
    "tools/audit/gen_discard_reach_split.py":
        "its write path calls its builder with NO argument, so whatever commit the write resolves "
        "is the builder's own default and sits outside `main`. What `main` shows is that the two "
        "paths do NOT pass the same thing: the check path passes the recorded commit explicitly "
        "and the write path passes nothing.",
    "tools/audit/gen_phase1_gate_readers.py":
        "the same shape as the member above: its write path calls its builder with NO argument, so "
        "the resolution is the builder's own default and sits outside `main`, while the check path "
        "passes the recorded commit explicitly.",
    "tools/audit/gen_retirement_caller_check.py":
        "its write path takes the commit from the command line — `--at <commit>` — and REFUSES to "
        "write without one, on its own stated ground that the reading is a statement about one "
        "tree and the commit is part of the finding. So it resolves neither the recorded commit "
        "nor HEAD, and the shape is a third one this recognizer does not name.",
}


class Stop(Exception):
    """A demand of the derivation is unmet. Never a warning."""


def read(path: str) -> str:
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def walk_tools() -> list[str]:
    out = []
    for base in TOOL_DIRS:
        for root, dirs, files in os.walk(os.path.join(ROOT, base)):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for fn in sorted(files):
                if fn.endswith(".py"):
                    out.append(os.path.relpath(os.path.join(root, fn), ROOT).replace("\\", "/"))
    return sorted(out)


def own_outputs(tree: ast.Module, text: str) -> list[str]:
    """Module-level constants bound to a path AND used as a write target."""
    named = []
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        tgt = node.targets[0]
        if not isinstance(tgt, ast.Name) or not tgt.id.isupper():
            continue
        name = tgt.id
        if (re.search(r"\b" + re.escape(name) + r"\.write_text\s*\(", text)
                or re.search(r"open\(\s*" + re.escape(name) + r"\s*,\s*[\"']w", text)):
            named.append(name)
    return sorted(set(named))


def find_main(tree: ast.Module) -> ast.FunctionDef | None:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "main":
            return node
    return None


def carries_check_flag(node: ast.AST) -> bool:
    for sub in ast.walk(node):
        if isinstance(sub, ast.Constant) and isinstance(sub.value, str) \
                and sub.value in CHECK_FLAGS:
            return True
    return False


def check_aliases(fn: ast.FunctionDef) -> set[str]:
    """Local names bound from a check-flag test — the `check = "--check" in argv` idiom."""
    out: set[str] = set()
    for node in fn.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) and carries_check_flag(node.value):
            out.add(node.targets[0].id)
    return out


def split_paths(fn: ast.FunctionDef) -> tuple[list[ast.stmt], list[ast.stmt]] | None:
    """(check path, write path): every check-only branch's body, and everything else in `main`."""
    aliases = check_aliases(fn)
    check_nodes: list[ast.stmt] = []
    write_nodes: list[ast.stmt] = []
    found = False
    for stmt in fn.body:
        is_check_branch = False
        if isinstance(stmt, ast.If):
            if carries_check_flag(stmt.test):
                is_check_branch = True
            else:
                for sub in ast.walk(stmt.test):
                    if isinstance(sub, ast.Name) and sub.id in aliases:
                        is_check_branch = True
                        break
        if is_check_branch:
            found = True
            check_nodes.extend(stmt.body)
            write_nodes.extend(stmt.orelse)
        else:
            write_nodes.append(stmt)
    return (check_nodes, write_nodes) if found else None


def artifact_locals(nodes: list[ast.stmt], outputs: list[str]) -> set[str]:
    """Local names standing for one of the tool's own outputs being READ."""
    handles: set[str] = set()
    for node in nodes:
        for sub in ast.walk(node):
            if not isinstance(sub, ast.With):
                continue
            for item in sub.items:
                src = ast.unparse(item.context_expr)
                if any(o in src for o in outputs) and "open" in src \
                        and isinstance(item.optional_vars, ast.Name):
                    handles.add(item.optional_vars.id)

    names: set[str] = set(handles)
    for node in nodes:
        for sub in ast.walk(node):
            if not isinstance(sub, ast.Assign) or len(sub.targets) != 1:
                continue
            tgt = sub.targets[0]
            if not isinstance(tgt, ast.Name):
                continue
            src = ast.unparse(sub.value)
            direct = any(o in src for o in outputs) and any(k in src for k in READ_IDIOMS)
            viahandle = ("json.load" in src
                         and any(re.search(r"\b" + re.escape(h) + r"\b", src) for h in handles))
            if direct or viahandle:
                names.add(tgt.id)
    return names


def commit_read_back(nodes: list[ast.stmt], outputs: list[str]) -> list[str]:
    """Every `.get("…commit…")` / `["…commit…"]` whose receiver traces to an own output."""
    locals_ = artifact_locals(nodes, outputs)
    hits: list[str] = []

    def receiver_traces(expr: ast.expr) -> bool:
        src = ast.unparse(expr)
        if any(o in src for o in outputs) and any(k in src for k in READ_IDIOMS):
            return True
        return any(re.search(r"\b" + re.escape(n) + r"\b", src) for n in locals_)

    for node in nodes:
        for sub in ast.walk(node):
            key = None
            recv = None
            if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute) \
                    and sub.func.attr == "get" and sub.args:
                arg = sub.args[0]
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    key, recv = arg.value, sub.func.value
            elif isinstance(sub, ast.Subscript) and isinstance(sub.slice, ast.Constant) \
                    and isinstance(sub.slice.value, str):
                key, recv = sub.slice.value, sub.value
            if key is None or "commit" not in key.lower():
                continue
            if receiver_traces(recv):
                hits.append(key)
    return sorted(set(hits))


def carries_head(nodes: list[ast.stmt]) -> bool:
    for node in nodes:
        for sub in ast.walk(node):
            if isinstance(sub, ast.Constant) and isinstance(sub.value, str) \
                    and sub.value == "HEAD":
                return True
    return False


def build() -> dict:
    tools = walk_tools()
    members: dict[str, dict] = {}
    unparsed: list[str] = []
    no_main: list[str] = []
    no_split: list[str] = []

    for rel in tools:
        text = read(os.path.join(ROOT, rel))
        try:
            # A tool carrying a deprecated escape sequence warns on parse. The warning is about
            # that tool and not about this derivation, and letting it reach stderr would put a
            # tool's lint noise inside the guard registry's captured output.
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                tree = ast.parse(text)
        except SyntaxError:
            unparsed.append(rel)
            continue
        outputs = own_outputs(tree, text)
        if not outputs:
            continue
        fn = find_main(tree)
        if fn is None:
            no_main.append(rel)
            continue
        split = split_paths(fn)
        if split is None:
            no_split.append(rel)
            continue
        check_nodes, write_nodes = split
        check_keys = commit_read_back(check_nodes, outputs)
        if not check_keys:
            continue                                  # not epoch-pinned: nothing to enumerate
        write_keys = commit_read_back(write_nodes, outputs)
        head = carries_head(write_nodes)
        if write_keys:
            verdict = SYMMETRIC
        elif head:
            verdict = ASYMMETRIC
        else:
            verdict = UNPLACED
        members[rel] = {
            "verdict": verdict,
            "own_outputs_the_derivation_found": outputs,
            "the_key_the_check_path_reads_back": check_keys,
            "the_key_the_write_path_reads_back": write_keys,
            "the_write_path_carries_the_literal_HEAD": head,
            "why_the_derivation_cannot_place_it": (
                UNPLACED_RETURNED_TO_THE_USER.get(rel) if verdict == UNPLACED else None),
        }

    derived_unplaced = sorted(t for t, r in members.items() if r["verdict"] == UNPLACED)

    seed_check = {}
    for tool, (expected, evidence) in sorted(SEEDS.items()):
        got = members.get(tool, {}).get("verdict")
        seed_check[tool] = {
            "expected": expected,
            "derived": got,
            "agrees": got == expected,
            "why_the_record_establishes_it": evidence,
        }

    return {
        "what_this_is":
            "THE EPOCH-PINNED PASSES AND WHAT EACH ONE'S WRITE PATH RESOLVES. A MEASUREMENT AND A "
            "PUBLICATION: nothing here corrects a write path, edits an enumerated pass, or grades "
            "a member as owed. Every member is derived from the tools' own syntax trees; none is "
            "listed by hand (D-431).",
        "generated_by": "tools/audit/gen_epoch_write_path.py",
        "generated_for": "cc_instruction_preparation_twelfth.md, Task 3",
        "the_ruling_verbatim":
            "The enumeration is published as data. Each pass is corrected only when a ruled act "
            "needs its write path, and the published enumeration is the standing input to that act "
            "rather than a work list.",
        "the_ruling": "User, 2026-08-19, Ruling 3 of "
                      "`cowork_rulings_2026_08_19_eleventh_return.md`.",
        "what_this_authorizes": "NOTHING. No write path is corrected here, no member is acted on, "
                                "and no member is owed by appearing here. A member is corrected "
                                "only when a ruled act needs its write path.",
        "how_it_is_derived": {
            "population": "every `*.py` under `tools/`, parsed with the standard library's own "
                          "syntax tree",
            "own_outputs": "a module-level constant bound to a path AND used as a write target, in "
                           "the two idioms the tools actually use — `NAME.write_text(...)` and "
                           "`open(NAME, \"w\"...)`",
            "the_split": "inside `main`, every top-level `if` whose test carries the literal "
                         "`--check` or `--verify`, or a local name bound from such a literal; "
                         "those bodies are the CHECK path and everything else in `main`, including "
                         "such an `if`'s `else`, is the WRITE path",
            "a_read_back": "a `.get(\"…commit…\")` or `[\"…commit…\"]` whose receiver traces to one "
                           "of that tool's own outputs being read — directly, through a local "
                           "bound from one, or through a `with open(OUT) as fh` handle",
            "a_member": "a tool whose CHECK path carries a read-back — which is what makes it "
                        "epoch-pinned",
            "the_verdict": "SYMMETRIC where the WRITE path carries a read-back too; ASYMMETRIC "
                           "where it does not and carries the literal `HEAD` instead; UNPLACED "
                           "where it carries neither",
        },
        "the_bound_what_it_cannot_see": [
            "It reads SOURCE, never a run. It reports what each path is written to resolve, not "
            "what a run would do — and it cannot tell an asymmetric member that would merely "
            "DIFFER from one that would STOP, which turns on the population the pass reads at "
            "HEAD and is a property of the tree on the day of the run. That an asymmetric run may "
            "STOP rather than differ is F77's measured instance.",
            "It reads the statements of `main` only. A commit resolved inside a helper `main` "
            "calls — a builder's own default argument, for instance — is invisible to it, and so "
            "is a tool whose check/write split lives outside `main`. A member of that shape lands "
            "in UNPLACED rather than being guessed.",
            "It reads a tool's OWN outputs. A pass pinned at the commit ANOTHER tool's artifact "
            "records is outside this population by construction, having no self-recorded commit "
            "for its two paths to disagree about.",
            "A computed key name or a computed output path carries no literal to find.",
            "It recognises a read-back by the KEY carrying the word `commit`. A pass recording its "
            "epoch under a differently-worded key reports as a non-member — the recoverable "
            "direction, a missing member being a question and a wrongly placed one a false "
            "statement about a write path.",
        ],
        "counts": {
            "tools_walked": len(tools),
            "members": len(members),
            "symmetric": sum(1 for r in members.values() if r["verdict"] == SYMMETRIC),
            "asymmetric": sum(1 for r in members.values() if r["verdict"] == ASYMMETRIC),
            "unplaced": len(derived_unplaced),
        },
        "the_members": dict(sorted(members.items())),
        "★_the_unplaced_members_returned_to_the_user": {
            "what_this_is": "members the recognizers cannot place. Each is a STANDING "
                            "STOP-AND-REPORT to the user and is never guessed into one of the two "
                            "verdicts. The authored set and the derived set are reconciled BOTH "
                            "ways on every run: an unplaced member not in the authored set halts "
                            "the run, so a new unrecognised shape cannot enter silently; and an "
                            "authored member the derivation now places halts it too, so an "
                            "authored reason cannot outlive its subject.",
            "members": {t: members[t]["why_the_derivation_cannot_place_it"]
                        for t in derived_unplaced},
        },
        "the_establishment": {
            "what_this_is": "two members the record already establishes at the code, one per "
                            "verdict, re-checked on every run. A disagreement HALTS the "
                            "derivation rather than being published (#19).",
            "seeds": seed_check,
        },
        "what_the_derivation_passed_over": {
            "what_this_is": "tools it could not reach, recorded rather than dropped (#12). None is "
                            "a finding: each is a shape the recognizers do not read.",
            "source_would_not_parse": unparsed,
            "no_main_function": no_main,
            "no_check_write_split_in_main": no_split,
        },
        "what_this_does_not_assert": [
            "That an ASYMMETRIC member is broken. Its check path passes and its artifact stands; "
            "what is asymmetric is which question each path asks.",
            "That a SYMMETRIC member needs nothing. It asserts only that both paths read the same "
            "recorded commit back.",
            "That the population is complete. It is complete relative to the recognizers named "
            "above, whose reach is stated in the bound and is UNMEASURED beyond the two seeds.",
        ],
    }


def main(argv: list[str]) -> int:
    art = build()

    for tool, row in art["the_establishment"]["seeds"].items():
        if not row["agrees"]:
            raise Stop(f"the establishment seed {tool} derives {row['derived']!r}, not "
                       f"{row['expected']!r} — the recognizer no longer recognises the shape it "
                       f"was built for")

    derived_unplaced = set(art["★_the_unplaced_members_returned_to_the_user"]["members"])
    authored_unplaced = set(UNPLACED_RETURNED_TO_THE_USER)
    if derived_unplaced - authored_unplaced:
        raise Stop("a member the derivation cannot place carries no authored reason: "
                   f"{sorted(derived_unplaced - authored_unplaced)}")
    if authored_unplaced - derived_unplaced:
        raise Stop("an authored unplaced reason names a member the derivation now places: "
                   f"{sorted(authored_unplaced - derived_unplaced)}")

    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"
    if "--check" in argv:
        have = read(OUT) if os.path.exists(OUT) else ""
        if have != text:
            print("STALE vs the derivation: epoch_write_path.json does not re-derive")
            return 1
        print("the epoch-pinned write-path enumeration re-derives")
    else:
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote %s" % os.path.relpath(OUT, ROOT).replace("\\", "/"))
    c = art["counts"]
    print("  tools walked %d; members %d — symmetric %d, asymmetric %d, unplaced %d"
          % (c["tools_walked"], c["members"], c["symmetric"], c["asymmetric"], c["unplaced"]))
    for tool, row in art["the_members"].items():
        print("    %-52s %s" % (tool, row["verdict"].split(" — ")[0]))
    if derived_unplaced:
        print("  STANDING STOP-AND-REPORT to the user — unplaced: %s" % sorted(derived_unplaced))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print("STOP: %s" % exc)
        sys.exit(2)
