#!/usr/bin/env python3
"""THE RECOGNIZERS THE RECORD LEANS ON, SORTED BY WHETHER AN INDEPENDENTLY-KNOWN POPULATION EXISTS
TO RECONCILE AGAINST — derived, published, and authorizing nothing.

THE RULING THIS EXISTS FOR (user, 2026-08-19, Ruling 1 of
`cowork_rulings_2026_08_19_twelfth_return.md`), quoted verbatim:

    A recognizer over a population is established only by both-ways reconciliation against an
    independently-known population. Where no such population exists, the recognizer's output IS
    the population, no seed set can establish it, and its output stands as a LOWER BOUND with its
    reach declared UNMEASURED — never as a census.

and, on what this derivation's own result authorizes:

    a read-only derivation over the recognizers the record leans on ... runs regardless of this
    ruling ... What is ruled is what its result authorizes: NOTHING.

★ WHAT THIS AUTHORIZES: NOTHING.  It edits, widens or acts on no recognizer, writes no enumerated
member's artifact, orders no re-establishment pass, and grades no member as owed.  The published
sort is the STANDING INPUT to a later ruled act — never a work list.

★ AND THIS SORT DECLARES ITS OWN STATUS UNDER THE VERY TEST IT APPLIES, which is the ruling applied
to the act that lands it.  Its POPULATION — every `*.py` under `tools/` — is externally enumerable,
so its membership is checkable; but WHICH of those tools it classes as a recognizer over a
population is its OWN classification, and nothing outside it enumerates that.  So it is MIXED under
its own test, and **its member list is published as a LOWER BOUND with its reach declared
UNMEASURED, never as a census.**  See `★_this_sorts_own_status_under_its_own_test`.

THE TEST, AND IT IS MECHANICAL RATHER THAN A MATTER OF TASTE
------------------------------------------------------------
DOES SOMETHING OTHER THAN THIS RECOGNIZER ENUMERATE THE POPULATION IT CLAIMS TO DESCRIBE?

  ESTABLISHED    the tool reconciles its published population in BOTH DIRECTIONS, against a side
                 that is NOT a set authored inside the tool itself, and HALTS on a member it
                 cannot place.
  MIXED          not that — but the CANDIDATE ENUMERATION it draws from is external (a file-system
                 walk or a read of a document it does not write) and is PUBLISHED WHOLE in its own
                 artifact.  So it is established ON ITS POPULATION and unestablished ON ITS
                 CLASSIFICATION, and the sort says so per member rather than per tool.
  NO INDEPENDENTLY-KNOWN POPULATION
                 neither.  The published class IS the recognizer's own output, no seed set can
                 establish it, and it stands as a LOWER BOUND with its reach UNMEASURED.
  UNPLACED       the derivation cannot decide.  Returned to the user as a STANDING
                 STOP-AND-REPORT, never guessed into one of the three.

HOW THE POPULATION IS DERIVED, so that no member is hand-listed (D-431)
----------------------------------------------------------------------
Every `*.py` under `tools/` is walked and parsed with the standard library's own syntax tree.  The
walk and the own-output recognizer are IMPORTED from `gen_epoch_write_path.py`, which already owns
them and whose own artifact establishes them, rather than written a second time (#6).  A tool is a
MEMBER of this sort when all three hold:

  (i)   it WRITES AN ARTIFACT OF ITS OWN — a module-level constant bound to a path and used as a
        write target;
  (ii)  it draws its candidates from an ENUMERATION SOURCE IT DOES NOT ITSELF WRITE — a
        file-system walk or glob, or a read of a path that is not one of its own outputs — CARRIED
        IN ITS OWN SOURCE OR IN A HELPER IT IMPORTS;
  (iii) it decides membership or class with A RECOGNIZER — a regular expression or a syntax tree
        applied to what it read — CARRIED IN ITS OWN SOURCE OR IN ONE IT IMPORTS.

A tool failing any of the three is not a recognizer over a population and is recorded in
`what_the_derivation_passed_over` rather than dropped (#12).

★ WHY (ii) AND (iii) READ AN IMPORTED HELPER TOO, recorded because it was a CORRECTION and not the
first writing, and because BOTH corrections rest on ONE ground.  Each part was first written to
look at a tool's own source alone, and each was refuted by a case the record itself produces:

  * (iii) — the first establishment seed derived as NOT A MEMBER.
    `gen_nongating_apparatus_rows.py` imports the row split and the leading-token test from
    `index_status_lint.py`, under an explicit #6 comment saying those live in ONE place.
  * (ii)  — THIS DERIVATION could not see ITSELF.  Its own walk is imported from
    `gen_epoch_write_path.py`, which owns it (#6), so no walk appears in its own source and it
    failed its own member test — while the ruled clause requires it to declare its own status
    under the very test it applies.

**The ground is the same one in both places, and it is this project's own #6:** a walk or a
recognizer with several users is given ONE home and imported, so a test reading a tool's own source
alone reports every tool that FOLLOWS that rule as drawing on nothing and recognizing nothing.
Neither widening is made to make a seed pass — that would be the defect the catalog names DT-2 —
and in both places the two cases are published SEPARATELY per member, at `found_in` and at
`where_its_placement_recognizer_lives`, so a reader sees which it is rather than taking the
derivation's word for it.

THE MECHANICAL FACTS DERIVED PER MEMBER, each read at the tool's own source
--------------------------------------------------------------------------
  the population it claims to describe   the FIRST SENTENCE OF ITS OWN MODULE DOCSTRING, quoted.
                                         Derived and never authored here: the tool's own words for
                                         its own subject.
  what enumerates the candidates         the walks with their root expressions, and the paths it
    independently                        reads but does not write, each with the idiom that found
                                         it.
  the reconciliation                     every set-difference or intersection expression GUARDED BY
                                         A RAISE, quoted verbatim; whether two of them form a
                                         REVERSED OPERAND PAIR (both directions); and whether an
                                         operand of that pair traces, at one level of local
                                         assignment, to a collection AUTHORED inside this tool.
  it halts on a member it cannot place   whether a halt exists at all.
  the candidate enumeration is           whether the candidate collection ITSELF — not its length —
    published whole                      is assigned to a key of the artifact the tool builds.

ESTABLISHMENT (#19) — THREE SEEDS, ONE PER VERDICT, RE-CHECKED ON EVERY RUN.  Each was read at its
own tool and at its own artifact on 2026-08-19, and the derivation must reproduce all three or
HALT rather than publish a population it can no longer place correctly:

  * `gen_nongating_apparatus_rows.py` — ESTABLISHED.  Its candidate population is the PARSED INDEX
    (`INDEX = ROOT / "OPEN_ITEMS.md"`, read with `read_text`), and it reconciles against it in both
    directions with a halt: every open row placed as gating or non-gating with none in both and
    none in neither, every gating identity an open row of that parse, every gating row carrying a
    ground, and a row it cannot place raising rather than being defaulted silently.
  * `gen_evidence_pin_membership.py` — MIXED.  Its candidate population is an external file-system
    enumeration (`os.listdir(ROOT)` filtered to the root-level ruling records) PUBLISHED WHOLE as
    `ruling_records_read`; but which route places a member is decided by its own regular
    expressions over the records' text, and its one set-difference is single-directional and is
    published rather than raised on.
  * `gen_epoch_write_path.py` — NO INDEPENDENTLY-KNOWN POPULATION.  It reconciles both ways and
    halts, but against `UNPLACED_RETURNED_TO_THE_USER`, a set AUTHORED INSIDE THE TOOL — so the
    check catches future drift and establishes no coverage; and its candidate enumeration is
    published as a LENGTH (`tools_walked`) rather than whole.  Its own artifact concedes the point.

THE BOUND — WHAT THIS DERIVATION READS, AND WHAT IT CANNOT SEE.  Stated because a derivation over
source is a recognizer over code and not a run of it, and because this sort's own clause requires
it:

  * It reads SOURCE, never a run.  It reports what a tool is written to do, not what a run does.
  * The authored-side test expands ONE LEVEL of local assignment.  A collection authored inside the
    tool and reached through two or more intermediate names reads as non-authored, which would
    place a member ESTABLISHED that is not.  That direction of error is the DANGEROUS one and is
    why the three seeds are re-checked on every run.
  * It recognises a reconciliation only where the set operation is GUARDED BY A RAISE in the same
    `if`.  A tool that reconciles and reports without raising reads as not reconciling.
  * A computed path, a computed key or a collection built through a helper this derivation does
    not follow carries no literal to find.
  * It takes a tool's declared subject from its module docstring's first sentence.  A tool with no
    docstring publishes an empty declaration rather than one this derivation invents.
  * AND THE MEMBERSHIP RECOGNIZER'S OWN REACH IS UNMEASURED beyond the three seeds, which is the
    whole of what the ruled clause requires this artifact to say about itself.

Run:
    python tools/audit/gen_recognizer_establishment_sort.py
    python tools/audit/gen_recognizer_establishment_sort.py --check
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
OUT = os.path.join(HERE, "recognizer_establishment_sort.json")
SELF_REL = "tools/audit/gen_recognizer_establishment_sort.py"

sys.path.insert(0, HERE)
from output_encoding import use_utf8_output      # noqa: E402  (path set above)
# The walk and the own-output recognizer have ONE home and are imported rather than re-written (#6).
from gen_epoch_write_path import walk_tools, own_outputs   # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ESTABLISHED = ("ESTABLISHED — it reconciles BOTH WAYS against a side not authored inside itself, "
               "and halts on a member it cannot place")
MIXED = ("MIXED — established on its POPULATION, which is an external enumeration published whole; "
         "unestablished on its CLASSIFICATION, which is its own recognizers")
NO_EXTERNAL = ("NO INDEPENDENTLY-KNOWN POPULATION — the recognizer's output IS the population; a "
               "LOWER BOUND with its reach UNMEASURED, never a census")
UNPLACED = "UNPLACED — the derivation cannot decide, and returns the member to the user"

WALK_CALLS = ("os.walk", "os.listdir", "glob", "iglob", "rglob", "scandir")
READ_IDIOMS = ("read_text", "json.load", "open(", "readlines", "read()")
RECOGNIZER_IDIOMS = ("re.compile", "re.search", "re.match", "re.findall", "re.finditer",
                     "re.fullmatch", "ast.parse", "ast.walk")

# ── AUTHORED: the three seeds, one per verdict, re-checked on every run ─────────────────────────
# Not a member list — the population is derived. These are the ESTABLISHMENT under #19, and a
# disagreement HALTS the derivation rather than being published. Each was read at its own tool and
# at its own artifact on 2026-08-19; the evidence is in the module docstring above.
SEEDS = {
    "tools/audit/gen_nongating_apparatus_rows.py": (
        ESTABLISHED,
        "its candidate population is the PARSED INDEX (`INDEX = ROOT / \"OPEN_ITEMS.md\"`, read "
        "with `read_text`) and it reconciles against that parse in both directions with a halt — "
        "none in both, none in neither, every gating identity an open row of it, every gating row "
        "carrying a ground, and a row it cannot place raising rather than being defaulted"),
    "tools/audit/gen_evidence_pin_membership.py": (
        MIXED,
        "its candidate population is an external file-system enumeration published WHOLE as "
        "`ruling_records_read`, while which route places a member is decided by its own regular "
        "expressions over the records' text; its one set-difference is single-directional and is "
        "published rather than raised on"),
    "tools/audit/gen_epoch_write_path.py": (
        NO_EXTERNAL,
        "it reconciles both ways and halts, but against `UNPLACED_RETURNED_TO_THE_USER`, a set "
        "AUTHORED INSIDE THE TOOL — so the check catches future drift and establishes no "
        "coverage — and its candidate enumeration is published as a length rather than whole; its "
        "own artifact concedes the point"),
}

# ── AUTHORED: members the derivation cannot place, each with the shape it CAN see ───────────────
# Reconciled BOTH ways against the derivation on every run: an unplaced member with no authored
# reason halts it, so a new unrecognised shape cannot enter silently; and an authored reason naming
# a member the derivation now places halts it too, so a reason cannot outlive its subject.
UNPLACED_RETURNED_TO_THE_USER: dict[str, str] = {}


class Stop(Exception):
    """A demand of the derivation is unmet. Never a warning."""


def read(path: str) -> str:
    with io.open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def parse(text: str) -> ast.Module | None:
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)
            return ast.parse(text)
    except SyntaxError:
        return None


def declared_subject(tree: ast.Module) -> str:
    """The tool's OWN words for its own subject: the first sentence of its module docstring."""
    doc = ast.get_docstring(tree) or ""
    doc = re.sub(r"\s+", " ", doc).strip()
    if not doc:
        return ""
    m = re.match(r"(.+?[.!?])(\s|$)", doc)
    return (m.group(1) if m else doc)[:400]


def module_paths(tree: ast.Module) -> dict[str, str]:
    """Module-level UPPERCASE constants and the expression each is bound to."""
    out: dict[str, str] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) and node.targets[0].id.isupper():
            out[node.targets[0].id] = ast.unparse(node.value)
    return out


def authored_collections(tree: ast.Module) -> list[str]:
    """Module-level UPPERCASE names bound to a LITERAL collection — a set authored in the tool."""
    out = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) and node.targets[0].id.isupper() \
                and isinstance(node.value, (ast.Dict, ast.Set, ast.List, ast.Tuple)):
            out.append(node.targets[0].id)
        # `NAME: dict[str, str] = {...}` — the annotated form the tools also use.
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) \
                and node.target.id.isupper() and isinstance(node.value,
                                                            (ast.Dict, ast.Set, ast.List,
                                                             ast.Tuple)):
            out.append(node.target.id)
    return sorted(set(out))


def imported_tool_modules(tree: ast.Module, byname: dict[str, str]) -> list[str]:
    """Sibling tools this one imports, resolved against the walked population."""
    out: list[str] = []
    for node in ast.walk(tree):
        mods: list[str] = []
        if isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            mods.append(node.module)
        elif isinstance(node, ast.Import):
            mods.extend(a.name for a in node.names)
        for mod in mods:
            rel = byname.get(mod.split(".")[-1])
            if rel:
                out.append(rel)
    return sorted(set(out))


def enumeration_sources(tree: ast.Module, text: str, outputs: list[str],
                        byname: dict[str, str] | None = None) -> list[dict]:
    """The candidate sources this tool draws from and does NOT itself write.

    An enumeration reached through an IMPORTED helper counts, on the same #6 ground as the
    recognizer half: a walk with several users is given ONE home and imported, so a test reading a
    tool's own source alone would report the tools that follow that rule as drawing on nothing.
    Each source records WHERE it was found, so the two are never collapsed.
    """
    found: list[dict] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            src = ast.unparse(node.func)
            if any(src.endswith(w) or src == w for w in WALK_CALLS):
                found.append({"idiom": "a file-system enumeration",
                              "found_in": "its own source",
                              "the_call": ast.unparse(node)[:200]})
    for rel in imported_tool_modules(tree, byname or {}):
        src = read(os.path.join(ROOT, rel))
        sub = parse(src)
        if sub is None:
            continue
        for node in ast.walk(sub):
            if isinstance(node, ast.Call):
                fn = ast.unparse(node.func)
                if any(fn.endswith(w) or fn == w for w in WALK_CALLS):
                    found.append({"idiom": "a file-system enumeration",
                                  "found_in": "a helper it imports: " + rel,
                                  "the_call": ast.unparse(node)[:200]})
    consts = module_paths(tree)
    for name, expr in sorted(consts.items()):
        if name in outputs:
            continue
        if not re.search(r"[\"'][^\"']*[\"']", expr):
            continue
        # A path constant names a FILE. A bare directory constant is the root a walk starts from,
        # which the walk itself already reports, and admitting it here would pad every member's
        # published evidence with the same uninformative row.
        if not re.search(r"[\"'][^\"']*\.[A-Za-z0-9]+[\"']", expr):
            continue
        if (re.search(r"\b" + re.escape(name) + r"\.read_text\s*\(", text)
                or re.search(r"open\(\s*" + re.escape(name), text)
                or re.search(r"json\.load[s]?\([^)]*\b" + re.escape(name) + r"\b", text)
                or re.search(r"\bread\(\s*[^)]*\b" + re.escape(name) + r"\b", text)):
            found.append({"idiom": "a path it reads and does not write",
                          "found_in": "its own source",
                          "the_constant": name, "bound_to": expr[:200]})
    # de-duplicate while keeping order
    seen, out = set(), []
    for f in found:
        key = json.dumps(f, sort_keys=True)
        if key not in seen:
            seen.add(key)
            out.append(f)
    return out


def has_recognizer(text: str, tree: ast.Module, byname: dict[str, str]) -> dict:
    """Where the tool's placement recognizer lives — in its own source, or in one it IMPORTS.

    An imported one counts, and the reason is this project's own #6: a recognizer with several
    users is given ONE home and imported, so a test that only looked at a tool's own source would
    report the tools that follow that rule as carrying no recognizer at all. The two are reported
    SEPARATELY rather than collapsed, so a reader sees which it is.
    """
    own = any(i in text for i in RECOGNIZER_IDIOMS)
    imported: list[str] = []
    for node in ast.walk(tree):
        mods: list[str] = []
        if isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            mods.append(node.module)
        elif isinstance(node, ast.Import):
            mods.extend(a.name for a in node.names)
        for mod in mods:
            rel = byname.get(mod.split(".")[-1])
            if not rel:
                continue
            src = read(os.path.join(ROOT, rel))
            if any(i in src for i in RECOGNIZER_IDIOMS):
                imported.append(rel)
    return {"in_its_own_source": own, "imported_from": sorted(set(imported))}


def local_assignments(tree: ast.Module) -> dict[str, str]:
    """name -> the expression it was last bound to, anywhere in the module."""
    out: dict[str, str] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            out[node.targets[0].id] = ast.unparse(node.value)
    return out


def _set_operands(expr: ast.expr) -> list[tuple[str, str]]:
    """Every (left, right) of a set difference or intersection inside `expr`."""
    pairs = []
    for sub in ast.walk(expr):
        if isinstance(sub, ast.BinOp) and isinstance(sub.op, (ast.Sub, ast.BitAnd)):
            pairs.append((ast.unparse(sub.left), ast.unparse(sub.right)))
    return pairs


def reconciliations(tree: ast.Module) -> list[dict]:
    """Every set difference/intersection GUARDED BY A RAISE, quoted verbatim."""
    assigns = local_assignments(tree)
    out: list[dict] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.If):
            continue
        if not any(isinstance(s, ast.Raise) for s in ast.walk(node)):
            continue
        exprs: list[str] = []
        if _set_operands(node.test):
            exprs.append(ast.unparse(node.test))
        for sub in ast.walk(node.test):
            if isinstance(sub, ast.Name) and sub.id in assigns \
                    and _set_operands(ast.parse(assigns[sub.id], mode="eval").body):
                exprs.append(assigns[sub.id])
        for e in exprs:
            pairs = _set_operands(ast.parse(e, mode="eval").body)
            for left, right in pairs:
                out.append({"the_expression": e[:240], "left": left[:120], "right": right[:120]})
    seen, uniq = set(), []
    for r in out:
        key = (r["the_expression"], r["left"], r["right"])
        if key not in seen:
            seen.add(key)
            uniq.append(r)
    return uniq


def _bare(operand: str) -> str:
    """`set(x)` / `sorted(x)` / `list(x)` -> `x`, so a reversed pair is recognisable."""
    prev = None
    cur = operand.strip()
    while cur != prev:
        prev = cur
        m = re.fullmatch(r"(?:set|sorted|list|frozenset)\((.+)\)", cur)
        if m:
            cur = m.group(1).strip()
    return cur


def both_ways(recs: list[dict]) -> dict | None:
    """A reversed operand pair among the raise-guarded reconciliations, if there is one."""
    pairs = {}
    for r in recs:
        for left in ({_bare(r["left"])} | {_bare(p) for p in re.split(r"\s*-\s*", _bare(r["left"]))}):
            pairs.setdefault((left, _bare(r["right"])), r)
    for (a, b), forward in pairs.items():
        if (b, a) in pairs:
            return {"one_direction": forward["the_expression"],
                    "the_other_direction": pairs[(b, a)]["the_expression"],
                    "the_pair": [a, b]}
    return None


def other_side_authored(tree: ast.Module, pair: list[str], authored: list[str]) -> list[str]:
    """Which side of the both-ways pair traces, at ONE level, to a collection authored here."""
    assigns = local_assignments(tree)
    hits = []
    for side in pair:
        text = side + " " + assigns.get(side.strip(), "")
        for name in authored:
            if re.search(r"\b" + re.escape(name) + r"\b", text):
                hits.append(side)
                break
    return hits


def candidate_names(tree: ast.Module, byname: dict[str, str]) -> set[str]:
    """Names holding a candidate collection: bound from a walk, or from a function that walks.

    A walking function IMPORTED from a sibling tool counts, on the same #6 ground as the two member
    -test parts: the walk has ONE home and is imported, and without this the tools that follow that
    rule publish their candidate enumeration whole and are read as not publishing it at all.
    """
    walking_fns = set()
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            body = ast.unparse(node)
            if any(w in body for w in WALK_CALLS):
                walking_fns.add(node.name)
    for node in ast.walk(tree):
        if not isinstance(node, ast.ImportFrom) or not node.module or node.level != 0:
            continue
        rel = byname.get(node.module.split(".")[-1])
        if not rel:
            continue
        sub = parse(read(os.path.join(ROOT, rel)))
        if sub is None:
            continue
        walks_there = {fn.name for fn in sub.body
                       if isinstance(fn, ast.FunctionDef)
                       and any(w in ast.unparse(fn) for w in WALK_CALLS)}
        for alias in node.names:
            if alias.name in walks_there:
                walking_fns.add(alias.asname or alias.name)
    out: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            src = ast.unparse(node.value)
            if any(w in src for w in WALK_CALLS) or any(
                    re.search(r"\b" + re.escape(f) + r"\s*\(", src) for f in walking_fns):
                out.add(node.targets[0].id)
    return out


def candidates_published_whole(tree: ast.Module, cands: set[str]) -> list[str]:
    """Artifact keys whose VALUE is the candidate collection itself, not its length."""
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for k, v in zip(node.keys, node.values):
            if not isinstance(k, ast.Constant) or not isinstance(k.value, str):
                continue
            if _bare(ast.unparse(v)) in cands:
                hits.append(k.value)
    return sorted(set(hits))


def place(tree: ast.Module, text: str, outputs: list[str], recognizer: dict,
          byname: dict[str, str]) -> dict:
    authored = authored_collections(tree)
    sources = enumeration_sources(tree, text, outputs, byname)
    recs = reconciliations(tree)
    pair = both_ways(recs)
    halts = bool(re.search(r"\braise\s+(Stop|SystemExit)\b", text))
    cands = candidate_names(tree, byname)
    published = candidates_published_whole(tree, cands)

    authored_sides = other_side_authored(tree, pair["the_pair"], authored) if pair else []

    if pair and not authored_sides and halts:
        verdict = ESTABLISHED
    elif published:
        verdict = MIXED
    else:
        verdict = NO_EXTERNAL

    return {
        "verdict": verdict,
        "the_population_it_claims_to_describe": declared_subject(tree),
        "where_its_placement_recognizer_lives": recognizer,
        "what_enumerates_the_candidates_independently": sources,
        "the_reconciliation": {
            "raise_guarded_set_operations": [r["the_expression"] for r in recs],
            "a_reversed_operand_pair": pair,
            "a_side_of_that_pair_is_authored_inside_this_tool": authored_sides,
            "collections_authored_inside_this_tool": authored,
        },
        "it_halts_on_a_member_it_cannot_place": halts,
        "the_candidate_enumeration_is_published_whole_at": published,
        "why_the_derivation_cannot_place_it": None,
    }


def build() -> dict:
    tools = walk_tools()
    if not tools:
        raise Stop("the walk over `tools/` enumerated nothing — A3's own condition. Nothing is "
                   "published.")

    byname = {os.path.basename(t)[:-3]: t for t in tools}
    members: dict[str, dict] = {}
    unparsed: list[str] = []
    no_artifact: list[str] = []
    no_external_candidate_source: list[str] = []
    no_recognizer: list[str] = []

    for rel in tools:
        text = read(os.path.join(ROOT, rel))
        tree = parse(text)
        if tree is None:
            unparsed.append(rel)
            continue
        outputs = own_outputs(tree, text)
        if not outputs:
            no_artifact.append(rel)
            continue
        if not enumeration_sources(tree, text, outputs, byname):
            no_external_candidate_source.append(rel)
            continue
        recognizer = has_recognizer(text, tree, byname)
        if not recognizer["in_its_own_source"] and not recognizer["imported_from"]:
            no_recognizer.append(rel)
            continue
        members[rel] = place(tree, text, outputs, recognizer, byname)

    for rel, row in members.items():
        if row["verdict"] == UNPLACED:
            row["why_the_derivation_cannot_place_it"] = UNPLACED_RETURNED_TO_THE_USER.get(rel)

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
            "THE RECOGNIZERS THE RECORD LEANS ON, SORTED BY WHETHER AN INDEPENDENTLY-KNOWN "
            "POPULATION EXISTS TO RECONCILE AGAINST. A MEASUREMENT AND A PUBLICATION: nothing "
            "here edits, widens or acts on any recognizer, writes any enumerated member's "
            "artifact, or grades any member as owed. Every member is derived from the tools' own "
            "syntax trees; none is listed by hand (D-431).",
        "generated_by": "tools/audit/gen_recognizer_establishment_sort.py",
        "generated_for": "cc_instruction_preparation_thirteenth.md, Task 2",
        "the_ruling_verbatim":
            "A recognizer over a population is established only by both-ways reconciliation "
            "against an independently-known population. Where no such population exists, the "
            "recognizer's output IS the population, no seed set can establish it, and its output "
            "stands as a LOWER BOUND with its reach declared UNMEASURED — never as a census.",
        "the_ruling": "User, 2026-08-19, Ruling 1 of "
                      "`cowork_rulings_2026_08_19_twelfth_return.md`. The clause it lands stands "
                      "at `cowork_audit_protocol.md`'s dispatch-protocol section.",
        "what_this_authorizes":
            "NOTHING. The ruling's own words: 'What is ruled is what its result authorizes: "
            "NOTHING.' No recognizer is corrected here, no member is acted on, and no member is "
            "owed by appearing here. The published sort is the STANDING INPUT to a later ruled "
            "act, never a work list.",
        "★_this_sorts_own_status_under_its_own_test": {
            "the_verdict_on_itself": MIXED,
            "★_and_it_is_DERIVED_rather_than_asserted": {
                "what_this_is": "This tool is a member of its OWN population, and the derivation "
                                "places it like any other member. The declared verdict above and "
                                "the derived one must AGREE, and a disagreement HALTS the run — so "
                                "this artifact cannot claim a status about itself that its own "
                                "test does not give it.",
                "the_derived_verdict": members.get(SELF_REL, {}).get("verdict"),
                "they_agree": members.get(SELF_REL, {}).get("verdict") == MIXED,
            },
            "and_therefore": "ITS MEMBER LIST IS PUBLISHED AS A LOWER BOUND WITH ITS REACH "
                             "DECLARED UNMEASURED, NEVER AS A CENSUS.",
            "the_population_half": "every `*.py` under `tools/` — an external file-system "
                                   "enumeration, published whole below at "
                                   "`the_candidate_population_walked`, so the membership is "
                                   "checkable by anyone who walks the same directory.",
            "the_classification_half": "WHICH of those tools is a recognizer over a population is "
                                       "THIS TOOL'S OWN classification, decided by the three-part "
                                       "member test above, and NOTHING OUTSIDE IT ENUMERATES "
                                       "THAT. No seed set can establish it: the three seeds prove "
                                       "the recognizer is not broken and say nothing about what "
                                       "it covers, which is finding F84's own general form.",
            "so_what_a_reader_may_take_from_it": "That every member listed IS one, on the evidence "
                                                 "published beside it. NOT that the list is "
                                                 "complete: a recognizer over a population this "
                                                 "derivation's member test does not reach is "
                                                 "absent from it, and how many such there are is "
                                                 "UNMEASURED.",
        },
        "the_test": {
            "the_question": "Does something other than this recognizer enumerate the population it "
                            "claims to describe?",
            "ESTABLISHED": "it reconciles its published population in BOTH DIRECTIONS against a "
                           "side that is NOT a collection authored inside the tool itself, and it "
                           "HALTS on a member it cannot place.",
            "MIXED": "not that — but the candidate enumeration it draws from is external and is "
                     "PUBLISHED WHOLE in its own artifact, so it is established on its POPULATION "
                     "and unestablished on its CLASSIFICATION.",
            "NO INDEPENDENTLY-KNOWN POPULATION": "neither. The published class IS the recognizer's "
                                                 "own output, no seed set can establish it, and it "
                                                 "stands as a LOWER BOUND with its reach "
                                                 "UNMEASURED.",
            "UNPLACED": "the derivation cannot decide. Returned to the user as a standing "
                        "STOP-and-report, never guessed into one of the three.",
        },
        "how_it_is_derived": {
            "population": "every `*.py` under `tools/`, walked and parsed with the standard "
                          "library's own syntax tree. The walk and the own-output recognizer are "
                          "IMPORTED from `gen_epoch_write_path.py`, which owns them (#6).",
            "a_member": "a tool that (i) writes an artifact of its own, (ii) draws its candidates "
                        "from an enumeration source it does not itself write, and (iii) decides "
                        "membership or class with a recognizer — a regular expression or a syntax "
                        "tree applied to what it read. FOR BOTH (ii) AND (iii) THE SOURCE MAY BE "
                        "CARRIED IN THE TOOL'S OWN TEXT OR IN A HELPER IT IMPORTS, on this "
                        "project's own #6: a walk or a recognizer with several users is given ONE "
                        "home and imported, so a test reading a tool's own source alone would "
                        "report every tool that FOLLOWS that rule as drawing on nothing and "
                        "recognizing nothing — and this derivation could not see ITSELF. The two "
                        "cases are published separately per member, at `found_in` and at "
                        "`where_its_placement_recognizer_lives`, never collapsed.",
            "the_population_it_claims_to_describe": "the first sentence of the tool's own module "
                                                    "docstring, quoted — the tool's own words for "
                                                    "its own subject, never authored here.",
            "the_reconciliation": "every set difference or intersection GUARDED BY A RAISE, quoted "
                                  "verbatim; whether two of them form a reversed operand pair; and "
                                  "whether a side of that pair traces, at ONE level of local "
                                  "assignment, to a collection authored inside the tool.",
            "the_candidate_enumeration_is_published_whole": "the candidate collection itself — not "
                                                            "its length — assigned to a key of the "
                                                            "artifact the tool builds.",
        },
        "the_bound_what_it_cannot_see": [
            "It reads SOURCE, never a run. It reports what a tool is written to do, not what a run "
            "does.",
            "The authored-side test expands ONE LEVEL of local assignment. A collection authored "
            "inside a tool and reached through two or more intermediate names reads as "
            "non-authored, which would place a member ESTABLISHED that is not — the DANGEROUS "
            "direction, and the reason the three seeds are re-checked on every run.",
            "It recognises a reconciliation only where the set operation is GUARDED BY A RAISE in "
            "the same `if`. A tool that reconciles and reports without raising reads as not "
            "reconciling.",
            "A computed path, a computed key, or a collection built through a helper this "
            "derivation does not follow, carries no literal to find.",
            "It takes a tool's declared subject from its module docstring's first sentence. A tool "
            "with no docstring publishes an empty declaration rather than one this derivation "
            "invents.",
            "AND THE MEMBERSHIP RECOGNIZER'S OWN REACH IS UNMEASURED beyond the three seeds. That "
            "is the ruled clause applied to this artifact itself, and it is why the member list "
            "is a LOWER BOUND.",
        ],
        "counts": {
            "tools_walked": len(tools),
            "members": len(members),
            "established": sum(1 for r in members.values() if r["verdict"] == ESTABLISHED),
            "mixed": sum(1 for r in members.values() if r["verdict"] == MIXED),
            "no_independently_known_population":
                sum(1 for r in members.values() if r["verdict"] == NO_EXTERNAL),
            "unplaced": len(derived_unplaced),
        },
        "the_candidate_population_walked": tools,
        "the_members": dict(sorted(members.items())),
        "★_the_unplaced_members_returned_to_the_user": {
            "what_this_is": "members the derivation cannot place. Each is a STANDING "
                            "STOP-AND-REPORT to the user and is never guessed into one of the "
                            "three verdicts. The authored set and the derived set are reconciled "
                            "BOTH ways on every run: an unplaced member not in the authored set "
                            "halts the run, so a new unrecognised shape cannot enter silently; and "
                            "an authored member the derivation now places halts it too, so an "
                            "authored reason cannot outlive its subject.",
            "members": {t: members[t]["why_the_derivation_cannot_place_it"]
                        for t in derived_unplaced},
        },
        "the_establishment": {
            "what_this_is": "three members the record establishes at the code and at their own "
                            "artifacts, ONE PER VERDICT, re-checked on every run. A disagreement "
                            "HALTS the derivation rather than being published (#19). ★ AND A SEED "
                            "SET PROVES ONLY THAT THE RECOGNIZER IS NOT BROKEN: it says nothing "
                            "about what the recognizer covers, which is finding F84 and the reason "
                            "this artifact publishes a lower bound.",
            "seeds": seed_check,
        },
        "what_the_derivation_passed_over": {
            "what_this_is": "tools it did not reach, recorded rather than dropped (#12). None is a "
                            "finding: each fails one part of the three-part member test, or is a "
                            "shape the recognizers do not read.",
            "source_would_not_parse": unparsed,
            "writes_no_artifact_of_its_own": no_artifact,
            "no_external_candidate_source_found": no_external_candidate_source,
            "no_recognizer_idiom_found": no_recognizer,
        },
        "what_this_does_not_assert": [
            "That a member on the NO INDEPENDENTLY-KNOWN POPULATION side is WRONG, or that its "
            "artifact is unusable. It asserts that the artifact is a floor and that how far below "
            "the truth it sits is unknown.",
            "That an ESTABLISHED member's individual verdicts are right. What is established is "
            "that its partition is complete against a population something other than it "
            "enumerates.",
            "That any member is OWED anything. The ruling that ordered this derivation says in its "
            "own words that the result authorizes NOTHING.",
            "That the member list is complete. It is complete relative to the three-part member "
            "test above, whose reach beyond the three seeds is UNMEASURED and stated as such.",
        ],
    }


def main(argv: list[str]) -> int:
    art = build()

    for tool, row in art["the_establishment"]["seeds"].items():
        if not row["agrees"]:
            raise Stop(f"the establishment seed {tool} derives {row['derived']!r}, not "
                       f"{row['expected']!r} — the recognizer no longer recognises the shape it "
                       f"was built for")

    own = art["★_this_sorts_own_status_under_its_own_test"]["★_and_it_is_DERIVED_rather_than_asserted"]
    if not own["they_agree"]:
        raise Stop("this sort declares itself %r but its own test derives %r for it. The ruled "
                   "clause requires it to declare its own status UNDER THE TEST IT APPLIES, so a "
                   "disagreement halts the run rather than publishing a claim its own derivation "
                   "does not support." % (MIXED, own["the_derived_verdict"]))

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
            print("STALE vs the derivation: recognizer_establishment_sort.json does not re-derive")
            return 1
        print("the recognizer establishment sort re-derives")
    else:
        with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote %s" % os.path.relpath(OUT, ROOT).replace("\\", "/"))
    c = art["counts"]
    print("  tools walked %d; members %d — established %d, mixed %d, no-external %d, unplaced %d"
          % (c["tools_walked"], c["members"], c["established"], c["mixed"],
             c["no_independently_known_population"], c["unplaced"]))
    print("  ★ THIS SORT IS ITSELF MIXED UNDER ITS OWN TEST: its member list is a LOWER BOUND with "
          "its reach UNMEASURED, never a census.")
    if derived_unplaced:
        print("  STANDING STOP-AND-REPORT to the user — unplaced: %s" % sorted(derived_unplaced))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Stop as exc:
        print("STOP: %s" % exc)
        sys.exit(2)
