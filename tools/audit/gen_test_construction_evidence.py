#!/usr/bin/env python3
"""HOW WAS EACH TEST OF THE COMPOSING MODULE CONSTRUCTED — from a specification, or beside the code?

THE RULING THIS EXISTS FOR.  User, 2026-08-15, §3.1 of
`cowork_rulings_2026_08_15_inventory_sitting.md`, at the artifact-inventory sitting.  Class 1 of the
inventory (`our-analysis-tests-and-fixtures`) was ruled CONDITIONALLY, in the user's own words:
*"IFF the regression test were constructed based solely on code and not at all on specs - I agree
with you (A)."*  Alternative A excludes the tests and the catalogs from the implementation-blind
redesign and keeps them as audit material.  **The condition requires this check before that verdict
carries load**, and the ruling fixes the two consequences: a test established as SPEC-DERIVED
carries design intent and RETURNS TO THE USER for a follow-up ruling; a test whose construction
CANNOT be established is treated as code-built, because erring toward exclusion is recoverable
through the fact-gate and erring toward admission is not.

WHAT THIS FILE DOES NOT DO.  It edits, moves and runs NO test.  It authors no ruling and carries no
verdict about whether any test is right, useful or worth keeping.  It reports evidence and a
classification drawn from that evidence by a published rule, and nothing else.

WHAT IS DERIVED AND WHAT IS AUTHORED — the difference is the whole value.
  DERIVED   the population, read from the committed artifact inventory's own class membership and
            NEVER hand-listed; every file's text and every commit subject, read from GIT OBJECTS at
            the commit that inventory records; the specification-document name set, read from the
            tree at that same commit; every located quote; every count.
  AUTHORED  the recognizer patterns below, and the classification rule that reads them.  Each is
            published in the artifact beside the verdicts it produced, so the rule can be checked
            against the evidence without opening this file.

★ WHY EVERY READ IS PINNED TO THE INVENTORY'S OWN COMMIT.  A check that re-read the working tree
would fail the first time anybody edited a test — which is the tree moving on correctly, and the
OI-301/OI-305 shape the record has met twice.  So the evidence is read at the commit the committed
inventory RECORDS, by explicit hash, and re-derives forever.  What is LIVE is the reconciliation:
the population is re-read from that inventory on every run and checked against the graded set in
BOTH directions, so a member entering or leaving the class halts this tool rather than being graded
silently or quietly dropped.

THE STOPS, so this cannot silently stop being an enumeration:
  * a population member with no verdict STOPS the tool — the dispatch's own stop rule;
  * a verdict outside the closed two-value vocabulary STOPS it;
  * a SPEC-DERIVED-EVIDENCE verdict with no located statement STOPS it, so the finding that returns
    to the user cannot be an assertion;
  * a graded file the inventory's class no longer carries, or a class member this run did not
    grade, STOPS it;
  * the distribution must reconcile with the population size, or it STOPS.

Run:
  python tools/audit/gen_test_construction_evidence.py           # write the artifact
  python tools/audit/gen_test_construction_evidence.py --check   # re-derive, exit 1 on drift
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                       # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
INVENTORY = ROOT / "tools" / "audit" / "artifact_inventory.json"
OUT = ROOT / "tools" / "audit" / "test_construction_evidence.json"

CLASS = "our-analysis-tests-and-fixtures"

# The closed vocabulary. The ruling fixes it at two values and this tool may not widen it.
SPEC_DERIVED = "SPEC-DERIVED-EVIDENCE"
CODE_BUILT = "CODE-BUILT"

# The two sub-cases of CODE-BUILT, recorded distinctly because the ruling distinguishes them: one
# is positive evidence of construction beside the code, the other is the ruling's own default for a
# construction that cannot be established at all.
SUB_POSITIVE = "positive-evidence-of-construction-beside-or-from-the-code"
SUB_DEFAULT = "no-establishable-construction-evidence — the ruling's default"


class Stop(Exception):
    """The enumeration cannot be published as one. Never a warning."""


# ── AUTHORED: the recognizers ────────────────────────────────────────────────────────────────────
#
# A DERIVATION WORD alone is not evidence — the word "derived" appears in prose about pitch
# derivation. A SPECIFICATION NAMING alone is not evidence either — a file may mention a document
# without taking anything from it. The positive signal this tool reports is the CONJUNCTION, on one
# line: a specification named (or a section mark carried) together with a word of derivation.
DERIVATION_WORD = re.compile(
    r"\b(derived|derives|derive|deriving|per the|as specified|specified|specifies|specification|"
    r"spec|mandated|mandates|required by|requires|contract|conform|conforms|conformance|"
    r"according to)\b", re.I)

SECTION_MARK = re.compile(r"§\s*[0-9A-Za-z]")

# Positive evidence that the file was built beside or from the code: it says of itself that it pins,
# captures or records behaviour rather than asserting an intended one.
CODE_BUILT_WORD = re.compile(
    r"\b(golden|goldens|snapshot|snapshots|pinned|pins|baseline|baselines|regression|as-built|"
    r"asbuilt|current behaviour|current behavior|captured|capture|characterisation|"
    r"characterization|reproduces the current|records what the code|mismatch report)\b", re.I)

# AUTHORED: which lines count as an in-file remark, per extension. A file type with no remark
# convention contributes no in-file statement and is recorded as such rather than silently scanned.
REMARK_PREFIX = {
    ".cpp": ("//", "/*", "*", "*/"),
    ".h": ("//", "/*", "*", "*/"),
    ".hpp": ("//", "/*", "*", "*/"),
    ".py": ("#",),
    ".cmake": ("#",),
    ".musicxml": ("<!--",),
    ".mscx": ("<!--",),
    ".xml": ("<!--",),
}
# AUTHORED: `CMakeLists.txt` is a build script whatever its suffix says, so its remark convention is
# the one its language uses. Without this its comments would be unreadable on a naming accident.
REMARK_BASENAME = {"CMakeLists.txt": ("#",)}

# AUTHORED: extensions whose bytes are not text. A container is not scanned for text and says so.
BINARY_EXT = {".mxl", ".zip", ".mscz"}


def git_bytes(*args: str) -> bytes:
    proc = subprocess.run(["git", "-C", str(ROOT), *args],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop("git failed: " + " ".join(args) + " — "
                   + proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout


def git_text(*args: str) -> str:
    return git_bytes(*args).decode("utf-8", "replace")


def remark_prefixes(path: str) -> tuple[str, ...] | None:
    base = path.rsplit("/", 1)[-1]
    if base in REMARK_BASENAME:
        return REMARK_BASENAME[base]
    ext = ("." + base.rsplit(".", 1)[-1].lower()) if "." in base else ""
    return REMARK_PREFIX.get(ext)


def is_binary(path: str) -> bool:
    base = path.rsplit("/", 1)[-1]
    ext = ("." + base.rsplit(".", 1)[-1].lower()) if "." in base else ""
    return ext in BINARY_EXT


def specification_names(commit: str) -> list[str]:
    """DERIVED: `ARCHITECTURE.md` plus every `docs/*.md` name the tree carries at that commit.

    Read from the git object rather than listed here, so a specification added later is covered
    without editing this tool — and so no name in this file can go stale against the tree.
    """
    names = ["ARCHITECTURE.md"]
    out = git_text("ls-tree", "--name-only", f"{commit}:docs")
    for line in out.splitlines():
        line = line.strip()
        if line.lower().endswith(".md"):
            names.append(line)
    if len(names) == 1:
        raise Stop("no `docs/*.md` names were found at the recorded commit — the specification "
                   "name set would be a single literal, which is not the derived set this tool "
                   "claims to use.")
    return sorted(set(names))


def population(inv: dict) -> tuple[str, list[str]]:
    commit = inv.get("derived_at_commit")
    if not commit:
        raise Stop("the committed inventory records no commit; every read here is pinned to it.")
    for cls in inv["the_classes"]:
        if cls["class"] == CLASS:
            members = [m["path"] for m in cls.get("every_member", [])]
            if not members:
                raise Stop(f"the inventory carries class {CLASS!r} with no member list — the "
                           "population may not be hand-listed here.")
            return commit, members
    raise Stop(f"the committed inventory does not carry class {CLASS!r}. The population is read "
               "from it and is never hand-listed, so this is a STOP rather than a fallback.")


def scan_file(commit: str, path: str, spec_names: list[str]) -> dict:
    """Every reading of ONE file, at the recorded commit. Nothing is judged here."""
    if is_binary(path):
        return {
            "text_scanned": False,
            "why_not": "a container format, not text — scanning its bytes for a document name "
                       "would report an accident of compression",
            "specification_names_found": [],
            "section_marks_found": 0,
            "remark_convention": None,
            "remark_lines": 0,
            "derivation_statements_in_the_file": [],
            "code_built_statements_in_the_file": [],
        }

    text = git_bytes("show", f"{commit}:{path}").decode("utf-8", "replace")
    lines = text.splitlines()

    found = sorted({n for n in spec_names if n in text})
    marks = len(SECTION_MARK.findall(text))

    prefixes = remark_prefixes(path)
    remark_lines: list[str] = []
    if prefixes:
        for ln in lines:
            if ln.lstrip().startswith(prefixes):
                remark_lines.append(ln.strip())

    derivation: list[str] = []
    code_built: list[str] = []
    for ln in remark_lines:
        names_here = any(n in ln for n in spec_names)
        if (names_here or SECTION_MARK.search(ln)) and DERIVATION_WORD.search(ln):
            derivation.append(ln[:400])
        if CODE_BUILT_WORD.search(ln):
            code_built.append(ln[:400])

    return {
        "text_scanned": True,
        "specification_names_found": found,
        "section_marks_found": marks,
        "remark_convention": list(prefixes) if prefixes else None,
        "remark_convention_absent_means": (
            None if prefixes else
            "this file type carries no remark convention this tool recognizes, so it contributes "
            "no in-file statement — its evidence can come only from its commit history"),
        "remark_lines": len(remark_lines),
        "derivation_statements_in_the_file": derivation[:12],
        "code_built_statements_in_the_file": code_built[:12],
    }


def history(commit: str, path: str, spec_names: list[str]) -> dict:
    """Every commit subject that touched the file, up to the recorded commit, verbatim."""
    raw = git_text("log", "--follow", "--format=%H\x1f%s", commit, "--", path)
    entries = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        sha, subject = line.split("\x1f", 1)
        entries.append({"commit": sha, "subject": subject})

    derivation = []
    code_built = []
    for e in entries:
        s = e["subject"]
        names_here = any(n in s for n in spec_names)
        if (names_here or SECTION_MARK.search(s)) and DERIVATION_WORD.search(s):
            derivation.append(e)
        if CODE_BUILT_WORD.search(s):
            code_built.append(e)
    return {
        "commits": entries,
        "commit_count": len(entries),
        "derivation_statements_in_the_history": derivation,
        "code_built_statements_in_the_history": code_built,
    }


def classify(scan: dict, hist: dict) -> tuple[str, str, list]:
    """The published rule. Two values, and the CODE-BUILT sub-case recorded distinctly."""
    statements = (scan["derivation_statements_in_the_file"]
                  + [e["subject"] for e in hist["derivation_statements_in_the_history"]])
    if statements:
        return SPEC_DERIVED, "", statements
    if scan["code_built_statements_in_the_file"] or hist["code_built_statements_in_the_history"]:
        return CODE_BUILT, SUB_POSITIVE, (
            scan["code_built_statements_in_the_file"]
            + [e["subject"] for e in hist["code_built_statements_in_the_history"]])
    return CODE_BUILT, SUB_DEFAULT, []


def build() -> dict:
    if not INVENTORY.is_file():
        raise Stop(f"the committed artifact inventory is absent ({INVENTORY}). The population is "
                   "read from it and is never hand-listed.")
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    commit, members = population(inv)
    spec_names = specification_names(commit)

    rows = []
    for path in members:
        scan = scan_file(commit, path, spec_names)
        hist = history(commit, path, spec_names)
        verdict, sub_case, located = classify(scan, hist)
        if verdict not in (SPEC_DERIVED, CODE_BUILT):
            raise Stop(f"{path}: a verdict outside the closed vocabulary — {verdict!r}")
        if verdict == SPEC_DERIVED and not located:
            raise Stop(f"{path}: a SPEC-DERIVED-EVIDENCE verdict with no located statement. The "
                       "finding that returns to the user may not be an assertion.")
        sources = []
        if scan["derivation_statements_in_the_file"]:
            sources.append("in-the-file")
        if hist["derivation_statements_in_the_history"]:
            sources.append("in-a-commit-subject")
        rows.append({
            "path": path,
            "verdict": verdict,
            "code_built_sub_case": sub_case or None,
            "where_the_statements_were_located": sources,
            "the_located_statements": located[:12],
            "evidence_in_the_file": scan,
            "evidence_in_the_history": hist,
        })

    graded = {r["path"] for r in rows}
    if graded != set(members):
        raise Stop("the graded set and the inventory's class membership disagree — only graded: "
                   f"{sorted(graded - set(members))}; only in the class: "
                   f"{sorted(set(members) - graded)}")
    ungraded = [r["path"] for r in rows if not r["verdict"]]
    if ungraded:
        raise Stop(f"population member(s) with no verdict: {ungraded}")

    spec_members = sorted(r["path"] for r in rows if r["verdict"] == SPEC_DERIVED)
    cb_positive = sorted(r["path"] for r in rows
                         if r["verdict"] == CODE_BUILT and r["code_built_sub_case"] == SUB_POSITIVE)
    cb_default = sorted(r["path"] for r in rows
                        if r["verdict"] == CODE_BUILT and r["code_built_sub_case"] == SUB_DEFAULT)
    if len(spec_members) + len(cb_positive) + len(cb_default) != len(members):
        raise Stop("the distribution does not reconcile with the population size.")

    return {
        "what_this_is": (
            "THE CLASS-1 CONSTRUCTION-EVIDENCE CHECK: for every member of the artifact inventory's "
            "`our-analysis-tests-and-fixtures` class, the DERIVED evidence of how it was "
            "constructed — specification documents named in its own text, its own commit history "
            "subjects verbatim, and whether any of those states derivation from a specification — "
            "and a classification drawn from that evidence by the published rule below."),
        "the_ruling_it_serves": (
            "User, 2026-08-15, §3.1 of `cowork_rulings_2026_08_15_inventory_sitting.md`: class 1 "
            "is ruled CONDITIONALLY — *\"IFF the regression test were constructed based solely on "
            "code and not at all on specs - I agree with you (A).\"* The verdict does not carry "
            "load until this check has run. A member established SPEC-DERIVED carries design "
            "intent and RETURNS TO THE USER for a follow-up ruling; a member whose construction "
            "cannot be established is treated as code-built, because erring toward exclusion is "
            "recoverable through the fact-gate and erring toward admission is not."),
        "dispatch": "cc_instruction_ruled_inventory_landing.md, Task 3",
        "generator": "tools/audit/gen_test_construction_evidence.py",
        "reproduce": "python tools/audit/gen_test_construction_evidence.py --check",
        "what_this_does_NOT_do": (
            "No test is edited, moved or run. No ruling is authored and no verdict is offered on "
            "whether any test is right, useful or worth keeping. It authorizes no fix, no design "
            "and no inference change, and it moves no status cell and no gate."),
        "the_population": {
            "class": CLASS,
            "read_from": "tools/audit/artifact_inventory.json → the class's own `every_member`",
            "never_hand_listed": True,
            "members": len(members),
            "★_reconciled_in_BOTH_directions": (
                "The graded set and the inventory's class membership must be equal. A member "
                "entering or leaving the class halts this tool rather than being graded silently "
                "or quietly dropped — which is the live half of this check."),
        },
        "★_why_every_read_is_pinned": {
            "the_commit": commit,
            "what_is_read_there": "each file's text (`git show <commit>:<path>`), each file's "
                                  "commit history (`git log --follow <commit> -- <path>`), and "
                                  "the specification-document name set (`git ls-tree`).",
            "why": ("A check that re-read the working tree would fail the first time anybody "
                    "edited a test — the tree moving on correctly, which is the OI-301/OI-305 "
                    "shape. Pinned to the commit the committed inventory RECORDS, the evidence "
                    "re-derives forever; what stays live is the two-way population "
                    "reconciliation above."),
        },
        "what_is_AUTHORED_here": {
            "the_recognizers": {
                "derivation_word": DERIVATION_WORD.pattern,
                "section_mark": SECTION_MARK.pattern,
                "code_built_word": CODE_BUILT_WORD.pattern,
                "remark_convention_by_extension": {k: list(v) for k, v in REMARK_PREFIX.items()},
                "remark_convention_by_basename": {k: list(v) for k, v in REMARK_BASENAME.items()},
                "not_scanned_as_text": sorted(BINARY_EXT),
            },
            "the_classification_rule": (
                "SPEC-DERIVED-EVIDENCE if and only if a DERIVATION STATEMENT is located — one "
                "line, in the file's own remarks or in a commit subject that touched it, naming a "
                "specification document or carrying a section mark AND carrying a word of "
                "derivation. Otherwise CODE-BUILT, in one of two sub-cases recorded distinctly: "
                "positive evidence of construction beside or from the code, or no establishable "
                "construction evidence at all, which is the ruling's own default."),
            "why_the_conjunction_and_not_either_half": (
                "A derivation word alone is not evidence — the word appears in prose about pitch "
                "derivation. A specification naming alone is not evidence either — a file may "
                "mention a document without taking anything from it. Requiring both on one line is "
                "what keeps a positive finding worth returning to the user."),
            "nothing_else": "No role, no mining verdict, no retirement flag, no judgment about "
                            "whether any test should exist.",
        },
        "★_the_limitation_of_a_commit_subject_as_PER_FILE_evidence": (
            "A commit subject describes the COMMIT, not one of the files inside it. Where a "
            "member's only located statement sits in a commit subject, what is established is that "
            "a change naming a specification section touched this file — not that this file's own "
            "expectations were read out of that section. Every row records "
            "`where_the_statements_were_located` so the two cases can be told apart without "
            "re-deriving anything, and the distribution below counts them separately. This is "
            "stated rather than corrected: narrowing the evidence to in-file statements would drop "
            "the dispatch's own second source, and weighting one against the other would be this "
            "tool deciding something the ruling sends to the user."),
        "★_the_establishment_caveat_of_the_recognizers": (
            "#19, NOT DISCHARGED HERE. The patterns above are AUTHORED and their REACH against the "
            "text they scan is UNMEASURED — the defect this record has met twice, at a family "
            "enumerated by an unmeasured pattern (OI-367) and at a derived enumeration reporting "
            "its class empty while an instance stood (OI-368). What the STOPs establish is that "
            "every population member carries a verdict and that no positive verdict rests on "
            "nothing; they establish NOTHING about whether a member classified CODE-BUILT by "
            "default would stay so under a reading of the file. **The ruling's own default is what "
            "bounds the error**: an unestablished construction is treated as code-built, so a "
            "pattern that misses evidence errs toward exclusion, which the ruling records as the "
            "recoverable direction. A reader may not take this artifact as evidence that no "
            "further specification-derived test exists."),
        "counted": {
            "population": len(members),
            SPEC_DERIVED: len(spec_members),
            CODE_BUILT: len(cb_positive) + len(cb_default),
            "code_built_" + SUB_POSITIVE: len(cb_positive),
            "code_built_no_establishable_construction_evidence": len(cb_default),
            "reconciles_with_the_population": True,
        },
        "★_the_SPEC_DERIVED_EVIDENCE_members_BY_NAME": {
            "why_by_name": "The ruling sends exactly these back to the user for a follow-up "
                           "ruling, so they are named here rather than counted.",
            "members": spec_members,
            "by_where_the_statement_was_located": {
                "in-the-file": sorted(r["path"] for r in rows if r["verdict"] == SPEC_DERIVED
                                      and "in-the-file" in r["where_the_statements_were_located"]),
                "in-a-commit-subject-only": sorted(
                    r["path"] for r in rows if r["verdict"] == SPEC_DERIVED
                    and r["where_the_statements_were_located"] == ["in-a-commit-subject"]),
            },
        },
        "the_CODE_BUILT_members_by_sub_case": {
            SUB_POSITIVE: cb_positive,
            SUB_DEFAULT: cb_default,
        },
        "rows": rows,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="re-derive and exit 1 if the committed artifact does not match")
    args = ap.parse_args(argv)

    art = build()
    text = json.dumps(art, indent=1, ensure_ascii=False) + "\n"

    if args.check:
        have = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if have != text:
            print("STALE: tools/audit/test_construction_evidence.json does not re-derive")
            return 1
        print("the class-1 construction evidence re-derives")
        c = art["counted"]
        print(f"  population {c['population']} · spec-derived {c[SPEC_DERIVED]} · "
              f"code-built {c[CODE_BUILT]}")
        return 0

    OUT.write_text(text, encoding="utf-8", newline="\n")
    c = art["counted"]
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  population: {c['population']} (class {CLASS}, read at {art['★_why_every_read_is_pinned']['the_commit'][:10]})")
    print(f"  {SPEC_DERIVED}: {c[SPEC_DERIVED]}")
    print(f"  {CODE_BUILT}: {c[CODE_BUILT]} "
          f"(positive evidence {c['code_built_' + SUB_POSITIVE]}, "
          f"no establishable evidence {c['code_built_no_establishable_construction_evidence']})")
    for m in art["★_the_SPEC_DERIVED_EVIDENCE_members_BY_NAME"]["members"]:
        print(f"    SPEC-DERIVED: {m}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        sys.exit(2)
