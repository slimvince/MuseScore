#!/usr/bin/env python3
"""DOES ANYTHING STILL POINT AT A FILE FLAGGED FOR RETIREMENT — established at the objects?

THE STANDING WARNING THIS DISCHARGES.  The ruled artifact inventory flags nine retirement
candidacies, and the user's own ruling attaches the same guard to all of them
(`cowork_rulings_2026_08_15_inventory_sitting.md` §3.16): *"every flag is a CANDIDACY; retirement is
archive-with-record, nothing destroyed (#12); no archiving executes on the name-scan signal alone —
the caller-check at the objects comes first"*.  The pruning plan repeats it
(`ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md` §8): *"no archiving executes
on the citation-scan signal alone — the caller-check at the objects precedes every wave."*  This is
that check.

WHY THE NAME-SCAN SIGNAL WAS NOT ENOUGH, in the surface's own words: an absent citation is evidence
that the GOVERNING RECORD names nothing, not that nothing anywhere depends on the file — *"a tool
imported by another tool is invisible to it"*.  So this check reads the WHOLE tracked tree at an
explicit commit rather than the seven governing documents.

★ THIS TOOL ARCHIVES, MOVES, RENAMES AND DELETES NOTHING.  It publishes a verdict per candidacy and
a caller list per member.  A PASSES-THE-CHECK verdict confers nothing: archiving is a later
dispatch's act, taken after this artifact is verified at the objects.

WHAT IS DERIVED AND WHAT IS AUTHORED.
  DERIVED   the candidacy population — the flagged classes and, for a partly-flagged class, the
            flagged side of its citation split — IMPORTED from `gen_artifact_inventory_surface`
            rather than re-listed here (#6, one path per concern), so this tool and the ruling
            surface cannot disagree about which files are flagged; every member path, read from the
            committed artifact inventory; every reference, found in the tracked tree at an explicit
            commit; every count.
  AUTHORED  the ruled CONDITION per candidacy, each carrying the sentence of the ruling record it
            was read from — and every one of those sentences is LOCATED in that record on every
            run, so a condition cannot outlive the words that imposed it.

★ WHAT A REFERENCE IS HERE, AND WHAT IT IS NOT.  A file REFERENCES a candidate when its text at the
measured commit contains the candidate's base name.  That covers the three kinds the dispatch names
— an import, a path written out, a tool reading a file by name — and it is deliberately GENEROUS:
erring toward finding a caller errs away from archiving something that is still used, which is the
safe direction for a candidacy nobody has ruled on.  What it does NOT cover, stated before its first
use: a reference built at run time from pieces (a directory joined to a name, a name assembled from
a pattern) carries no literal to find, and a binary file is not searched at all.  **So NONE FOUND
means no literal naming was found in text, never that nothing depends on the file.**

★ REFERENCES FROM INSIDE THE CANDIDATE'S OWN CLASS ARE SET ASIDE, NOT DROPPED (#12).  The dispatch
asks for references from outside the candidate's own class, because a class retiring as a whole
carries its internal cross-references with it.  Every such reference is still counted and published
in its own field, so the exclusion can be checked rather than trusted.

WHY THE READING IS PINNED TO A COMMIT.  A check that re-read the working tree would go red the first
time anybody wrote a file that happens to name a candidate — the tree moving on correctly, which is
the OI-301/OI-305 shape.  So the measurement is taken at an explicit commit, that commit is recorded
inside the artifact, and `--check` re-derives at the recorded one.  What stays LIVE is the
population: it is re-imported on every run and reconciled with the graded set in BOTH directions.

THE STOPS:
  * a flagged class the committed inventory does not carry STOPS the tool;
  * a flagged class the inventory publishes no members for STOPS it — the member list cannot be
    derived, and nothing here is hand-listed;
  * a candidacy with no authored condition record, or a condition record naming a candidacy the
    derivation does not carry, STOPS it — in BOTH directions;
  * a condition whose quoted sentence is no longer found in the ruling record STOPS it;
  * a verdict outside the closed three-value vocabulary STOPS it;
  * a candidacy with no verdict, or a verdict count that does not account for the population,
    STOPS it.

Run:
  python tools/audit/gen_retirement_caller_check.py --at <commit>   # measure and write
  python tools/audit/gen_retirement_caller_check.py --check         # re-derive, exit 1 on drift
"""
from __future__ import annotations

import json
import posixpath
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from output_encoding import use_utf8_output                       # noqa: E402  (path set above)
import gen_artifact_inventory as inventory_tool                   # noqa: E402  (the signature, once)
import gen_artifact_inventory_surface as surface                  # noqa: E402  (the flags, once)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

ROOT = Path(__file__).resolve().parent.parent.parent
RULING = ROOT / "cowork_rulings_2026_08_15_inventory_sitting.md"
OUT = ROOT / "tools" / "audit" / "retirement_caller_check.json"

PASSES = "PASSES-THE-CHECK"
HELD_CALLERS = "HELD-BY-CALLERS"
HELD_CONDITION = "HELD-BY-CONDITION"
VERDICTS = (PASSES, HELD_CALLERS, HELD_CONDITION)

NO_CONDITION = "none — the ruling attaches no condition beyond this check"


class Stop(Exception):
    """The check cannot be published as an enumeration. Never a warning."""


# ── AUTHORED: the ruled condition per candidacy, each with the sentence it was read from ─────────
#
# The condition is what the user's ruling attaches to a candidacy BEYOND this check. Three shapes
# appear in the ruling record and no fourth: mining must run first, the members must be seen by the
# user first, or nothing. Every quoted sentence below is LOCATED in the ruling record on every run.
CONDITIONS: dict[str, tuple[str, str]] = {
    "writing-side-scratch-directories": (
        NO_CONDITION,
        "The scratch directories: no role, not mined, retirement candidate CONFIRMED as a flag."),
    "llm-triage-prompts": (
        NO_CONDITION,
        "The LLM triage prompts: retirement candidates (the user was shown the live-consumer "
        "caveat and named none)."),
    "measurement-outputs-recorded-beside-the-tools": (
        "mined first — the class goes to the fact-gate, and only the members it leaves unnamed "
        "are flagged",
        "Class 36: fact-gate, then unnamed members flagged."),
    "idiom-discovery-workspace": (
        "mined first — the fact-gate takes the warnings before the class becomes a candidacy",
        "Idiom-discovery workspace: fact-gate for warnings, then retirement candidate."),
    "ai-assistant-design-notes": (
        NO_CONDITION,
        "The separate-assistant notes: retirement candidate (the user was shown the "
        "bears-on-analysis caveat and named nothing)."),
    "stray-working-files-committed-to-the-repository-root": (
        "the members are seen by the user first — the ruling names the unpacked score-container "
        "members specifically, before any archiving",
        "The stray root files: retirement candidate as a class, the unpacked score-container "
        "members seen by the user before any archiving."),
    "documentation-directory-prose": (
        "mined first — the uncited side becomes a candidacy only once it has been mined",
        "the uncited 15 are retirement candidates once mined."),
    "measurement-and-analysis-tools": (
        "mined first — the uncited side goes to the fact-gate before it is a candidacy, and the "
        "ruling names this very caller-check as preceding any archiving",
        "Class 35's split stands (30 cited: machinery; 100 uncited: fact-gate then retirement "
        "candidates, caller-check at the objects before any archiving executes)."),
    "reports-from-the-coding-side": (
        "mined first — the uncited side becomes a candidacy only once it has been mined",
        "Class 21's split stands; the uncited 30 are retirement candidates once mined."),
}

# A file-name-shaped token, the same shape the ruling surface's own citation scan uses.
NAME_TOKEN = re.compile(r"[A-Za-z0-9_.\-]+\.[A-Za-z0-9]+")


# `core.quotepath=false` is not cosmetic and not optional: without it git C-quotes any path holding
# a non-ASCII byte, and this repository has one — a triage prompt named after a diminished chord
# symbol. A quoted path is not the path, so `cat-file` reports it missing and the walk stops. Set
# once, on every git call this file makes, so the two can never disagree.
GIT_BASE = ["git", "-C", str(ROOT), "-c", "core.quotepath=false"]


def git(*args: str) -> str:
    proc = subprocess.run([*GIT_BASE, *args],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode not in (0, 1):        # git grep exits 1 on "no match", which is not failure
        raise Stop("git failed: " + " ".join(args) + " — "
                   + proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout.decode("utf-8", "replace")


def tree_paths(commit: str) -> list[str]:
    """Every tracked path at `commit`, read from the git object with paths unquoted."""
    return [line for line in git("ls-tree", "-r", "--name-only", commit).splitlines()
            if line.strip()]


def normalized(text: str) -> str:
    """Whitespace collapsed and emphasis marks removed, so a quote survives line wrapping."""
    return re.sub(r"\s+", " ", text.replace("**", "").replace("*", ""))


def locate_conditions() -> dict[str, str]:
    """Every authored condition's sentence, LOCATED in the ruling record. A missing one STOPS."""
    if not RULING.exists():
        raise Stop(f"the ruling record is missing: {RULING}")
    text = normalized(RULING.read_text(encoding="utf-8"))
    missing = [name for name, (_c, quote) in CONDITIONS.items()
               if normalized(quote) not in text]
    if missing:
        raise Stop("a condition's quoted sentence is no longer in the ruling record, so the "
                   f"condition would outlive the words that imposed it: {missing}")
    return {name: quote for name, (_c, quote) in CONDITIONS.items()}


def members_of(inv: dict, classes: dict, name: str) -> tuple[list[str], str]:
    """Every member path of a class, DERIVED — by two routes, neither of them a hand-list.

    ROUTE 1, used wherever it is available: the inventory PUBLISHES `every_member` for the classes
    the ruling surface descends into.

    ROUTE 2, for a flagged class the inventory does not descend into and therefore publishes no
    members for: apply the inventory's OWN published signature — imported from its generator, not
    restated — to the tree at the commit the inventory RECORDS, which is the tree its own class
    counts were taken at. The derived count is then cross-checked against the count the inventory
    publishes for that class, and a disagreement STOPS the tool, so the second route cannot quietly
    produce a different population from the one the ruling classified.

    ★ WHY ROUTE 2 IS NOT HAND-LISTING, which the dispatch forbids: no path is typed here. The rule
    that produces the list is the one the inventory published and the user's ruling was taken over.
    """
    published = classes[name].get("every_member")
    if published:
        return sorted(m["path"] for m in published), "published by the inventory as `every_member`"

    at = inv["derived_at_commit"]
    derived = sorted(p for p in tree_paths(at) if inventory_tool.classify(p)[0] == name)
    expected = classes[name]["files"]
    if len(derived) != expected:
        raise Stop(f"the member list derived for {name!r} by the inventory's own signature at its "
                   f"own commit holds {len(derived)} files where the inventory publishes "
                   f"{expected} — the two disagree, so the population cannot be taken")
    return derived, ("derived by applying the inventory's own published signature to the tree at "
                     f"the commit it records ({at}), because the inventory publishes no member "
                     f"list for this class; the derived count was cross-checked against the "
                     f"{expected} files the inventory reports for it")


def candidacies(inv: dict) -> dict[str, dict]:
    """The flagged population, IMPORTED from the ruling surface's own authored flags (#6)."""
    classes = {c["class"]: c for c in inv["the_classes"]}

    whole = [n for n, e in surface.PROPOSALS.items() if e.get("retirement_candidate") is True]
    partly = {n: [side for side, e in sides.items() if e.get("retirement_candidate")]
              for n, sides in surface.SPLIT_PROPOSALS.items()
              if any(e.get("retirement_candidate") for e in sides.values())}

    for name in whole + list(partly):
        if name not in classes:
            raise Stop(f"a flagged class is not in the committed inventory: {name!r}")
    for name in partly:
        if not classes[name].get("every_member"):
            raise Stop(f"the inventory publishes no members for the mixed class {name!r}, so its "
                       f"citation split cannot be taken and nothing here is hand-listed")

    text, _sources = surface.governing_text()
    names = surface.cited_names(text)

    out: dict[str, dict] = {}
    for name in whole:
        members, how = members_of(inv, classes, name)
        out[name] = {
            "flagged": "the whole class",
            "how_the_member_list_was_derived": how,
            "members": members,
        }
    for name, sides in partly.items():
        members = []
        for member in classes[name]["every_member"]:
            base = posixpath.basename(member["path"])
            side = "cited" if base in names else "uncited"
            if side in sides:
                members.append(member["path"])
        out[name] = {
            "flagged": "the " + " and ".join(sorted(sides)) + " side of the citation split",
            "how_the_member_list_was_derived":
                "published by the inventory as `every_member`, then split by the citation scan "
                "re-run at the governing record — the same scan the ruling surface splits by (#6)",
            "members": sorted(members),
        }

    authored = set(CONDITIONS)
    derived = set(out)
    if authored != derived:
        raise Stop("the authored condition records and the derived candidacies disagree. "
                   f"Derived with no condition record: {sorted(derived - authored)}. "
                   f"Condition records naming no derived candidacy: {sorted(authored - derived)}")
    return out


def class_of_every_path(inv: dict) -> dict[str, str]:
    """Which class each member path belongs to, for the same-class exclusion."""
    owner = {}
    for c in inv["the_classes"]:
        for member in c.get("every_member", []):
            owner[member["path"]] = c["class"]
    return owner


def naming_files(commit: str, bases: set[str]) -> list[str]:
    """Every tracked path at `commit` whose text contains one of the candidate base names.

    One `git grep` over the whole tree: `-F` takes the names as fixed strings, `-I` skips binary
    blobs, `--name-only` returns paths rather than matched lines (a matched line in a generated
    artifact can be megabytes long, and the attribution is taken by re-reading the file anyway).
    """
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                     encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(sorted(bases)) + "\n")
        pattern_file = fh.name
    try:
        listed = git("grep", "-I", "-F", "--name-only", "-f", pattern_file, commit)
    finally:
        Path(pattern_file).unlink(missing_ok=True)

    prefix = commit + ":"
    paths = []
    for line in listed.splitlines():
        if not line.strip():
            continue
        paths.append(line[len(prefix):] if line.startswith(prefix) else line)
    return sorted(set(paths))


def references(commit: str, bases: set[str]) -> dict[str, set[str]]:
    """Every tracked file at `commit` whose text names one of `bases`, mapped base -> paths.

    The naming files are read back through ONE `git cat-file --batch` rather than one process per
    file, so the attribution is exact — each file's whole text is scanned for file-name-shaped
    tokens — without paying a subprocess per naming file.
    """
    paths = naming_files(commit, bases)
    hits: dict[str, set[str]] = {b: set() for b in bases}
    if not paths:
        return hits

    request = "".join(f"{commit}:{p}\n" for p in paths).encode("utf-8")
    proc = subprocess.run(["git", "-C", str(ROOT), "cat-file", "--batch"],
                          input=request, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise Stop("git cat-file --batch failed: "
                   + proc.stderr.decode("utf-8", "replace").strip())

    stream, offset = proc.stdout, 0
    for path in paths:
        end = stream.index(b"\n", offset)
        header = stream[offset:end].decode("utf-8", "replace").split()
        if len(header) != 3 or header[1] != "blob":
            raise Stop(f"git cat-file returned an unexpected header for {path!r}: {header}")
        size = int(header[2])
        body = stream[end + 1:end + 1 + size].decode("utf-8", "replace")
        offset = end + 1 + size + 1          # the trailing newline git writes after each object
        for token in NAME_TOKEN.findall(body):
            if token in hits:
                hits[token].add(path)
    return hits


def build(commit: str) -> dict:
    inv_path = ROOT / "tools" / "audit" / "artifact_inventory.json"
    if not inv_path.exists():
        raise Stop(f"the committed artifact inventory is missing: {inv_path}")
    inv = json.loads(inv_path.read_text(encoding="utf-8"))

    quotes = locate_conditions()
    population = candidacies(inv)
    owner = class_of_every_path(inv)

    every_member = {p for c in population.values() for p in c["members"]}
    bases = {posixpath.basename(p) for p in every_member}
    hits = references(commit, bases)

    rows = []
    for name in sorted(population):
        condition, _quote = CONDITIONS[name]
        members, held, internal_only = [], [], []
        for path in population[name]["members"]:
            base = posixpath.basename(path)
            found = sorted(hits.get(base, set()) - {path})
            outside = [p for p in found if owner.get(p) != name]
            inside = [p for p in found if owner.get(p) == name]
            members.append({
                "path": path,
                "callers_outside_its_own_class": outside,
                "references_from_inside_its_own_class_set_aside_not_dropped": inside,
                "member_verdict": HELD_CALLERS if outside else PASSES,
            })
            if outside:
                held.append(path)
            elif inside:
                internal_only.append(path)

        if held:
            verdict = HELD_CALLERS
            ground = ("at least one member is named from outside its own class at the measured "
                      "commit; the callers are listed per member")
        elif condition != NO_CONDITION:
            verdict = HELD_CONDITION
            ground = ("no member is named from outside its own class at the measured commit, and "
                      f"a ruled condition still stands: {condition}")
        else:
            verdict = PASSES
            ground = ("no member is named from outside its own class at the measured commit, and "
                      "the ruling attaches no further condition")

        if verdict not in VERDICTS:
            raise Stop(f"candidacy {name!r} reached a verdict outside the closed vocabulary")

        rows.append({
            "candidacy": name,
            "what_is_flagged": population[name]["flagged"],
            "how_the_member_list_was_derived": population[name]["how_the_member_list_was_derived"],
            "members_flagged": len(population[name]["members"]),
            "ruled_condition": condition,
            "the_ruling_sentence_it_was_read_from": quotes[name],
            "verdict": verdict,
            "why_this_verdict": ground,
            "members_held_by_callers": sorted(held),
            "members_named_only_from_inside_their_own_class": sorted(internal_only),
            "members_with_no_naming_found_anywhere":
                sorted(m["path"] for m in members
                       if not m["callers_outside_its_own_class"]
                       and not m["references_from_inside_its_own_class_set_aside_not_dropped"]),
            "every_member": members,
        })

    if len(rows) != len(population):
        raise Stop("a candidacy reached no verdict")
    tally = {v: sum(1 for r in rows if r["verdict"] == v) for v in VERDICTS}
    if sum(tally.values()) != len(rows):
        raise Stop("the verdict tally does not account for the candidacies")

    # WHO DOES THE NAMING — derived, and the reason it is published is in the artifact below. A
    # caller naming a large share of the flagged population is enumerating the tree rather than
    # depending on any file in it, and that is visible here as a count instead of being decided by
    # a threshold nobody ruled.
    naming: dict[str, int] = {}
    for row in rows:
        for member in row["every_member"]:
            for caller in member["callers_outside_its_own_class"]:
                naming[caller] = naming.get(caller, 0) + 1
    flagged_total = sum(len(c["members"]) for c in population.values())
    who = [{"caller": c, "flagged_files_it_names": n,
            "share_of_the_flagged_population": round(n / flagged_total, 4)}
           for c, n in sorted(naming.items(), key=lambda kv: (-kv[1], kv[0]))]

    return {
        "what_this_is":
            "THE CALLER-CHECK AT THE OBJECTS, over every ruled retirement candidacy. For each "
            "flagged file it reports what still names it in the tracked tree at an explicit "
            "commit, the ruled condition still governing its archiving, and one verdict per "
            "candidacy. IT ARCHIVES, MOVES, RENAMES AND DELETES NOTHING, and a PASSES-THE-CHECK "
            "verdict confers nothing — archiving is a later dispatch's act, taken after this "
            "artifact is verified at the objects.",
        "generator": "tools/audit/gen_retirement_caller_check.py",
        "dispatch": "cc_instruction_preparation_opening.md, Task 3",
        "the_standing_warning_this_discharges": {
            "source": "cowork_rulings_2026_08_15_inventory_sitting.md §3.16",
            "quoted": "every flag is a CANDIDACY; retirement is archive-with-record, nothing "
                      "destroyed (#12); no archiving executes on the name-scan signal alone — the "
                      "caller-check at the objects comes first",
            "and_the_pruning_plan":
                "ratification_surfaces/cowork_phase_definition_surface_2026_08_15.md §8: \"no "
                "archiving executes on the citation-scan signal alone — the caller-check at the "
                "objects precedes every wave.\"",
        },
        "measured_at_commit": commit,
        "★_why_the_commit_is_recorded_and_what_it_bounds":
            "The reading is a statement about the tracked tree AT THIS COMMIT and at no other. A "
            "later commit can add a caller, and this artifact will not know; its staleness bound "
            "is therefore explicit rather than implied. `--check` re-derives at this recorded "
            "commit, so the check passes indefinitely instead of going red the first time anybody "
            "writes a file naming a candidate — the OI-301/OI-305 shape avoided by construction. "
            "What stays LIVE is the population: the flags are re-imported from the ruling "
            "surface's generator on every run, and the citation split that decides which members "
            "of a mixed class are flagged is RE-SCANNED at the governing record as it stands — the "
            "same live property that generator's own check carries, so a document that starts or "
            "stops being cited moves side here too rather than staying where a dated reading put "
            "it.",
        "what_is_DERIVED": [
            "the candidacy population — the flagged classes and the flagged side of each split — "
            "imported from tools/audit/gen_artifact_inventory_surface.py's own authored flags, so "
            "this check and the ruling surface cannot disagree about what is flagged (#6)",
            "every member path, read from the committed artifact inventory and never hand-listed",
            "every reference, found in the tracked tree at the recorded commit",
            "every count and every verdict tally",
        ],
        "what_is_AUTHORED": [
            "the ruled condition per candidacy, each carrying the sentence of the ruling record it "
            "was read from — and every sentence is located in that record on every run",
        ],
        "★_what_a_reference_is_here_and_what_it_is_not": {
            "what_counts": "A file REFERENCES a candidate when its text at the measured commit "
                           "contains the candidate's base name. That covers an import, a path "
                           "written out and a tool reading a file by name — the three kinds the "
                           "dispatch names.",
            "deliberately_generous": "Erring toward finding a caller errs away from archiving "
                                     "something still in use, which is the safe direction for a "
                                     "candidacy nobody has ruled on.",
            "★_what_NONE_FOUND_does_not_mean":
                "A reference assembled at run time from pieces carries no literal to find, and a "
                "binary blob is not searched at all. NONE FOUND means no literal naming was found "
                "in text at this commit — never that nothing depends on the file.",
            "same_class_references_are_set_aside_not_dropped":
                "The dispatch asks for references from OUTSIDE the candidate's own class, because "
                "a class retiring as a whole carries its internal cross-references with it. Every "
                "such reference is published in its own per-member field, so the exclusion can be "
                "checked rather than trusted (#12).",
        },
        "the_verdict_vocabulary": {
            PASSES: "no member is named from outside its own class, and no ruled condition stands",
            HELD_CALLERS: "at least one member is named from outside its own class; each caller "
                          "is named per member",
            HELD_CONDITION: "no such caller, but a ruled condition still governs archiving",
            "★_the_order_the_three_are_applied_in_and_why":
                "callers first, condition second. A caller is a fact about the tree and a "
                "condition is an act somebody still owes; where both hold, the verdict names the "
                "fact and the condition is still published in the row beside it, so neither is "
                "lost.",
        },
        "the_tally": tally,
        "★_the_finding_this_run_produced_and_the_question_it_leaves_open": {
            "what_was_measured": "Almost every flagged file is named somewhere in tracked content "
                                 "outside its own class, so almost every candidacy is "
                                 "HELD-BY-CALLERS. The verdicts below are exactly what the check "
                                 "the dispatch specifies produces, and they are reported as "
                                 "measured.",
            "what_the_naming_mostly_is": "Artifacts that ENUMERATE THE TREE name every path by "
                                         "construction — the artifact inventory itself, the ruling "
                                         "surface generated from it, and other file-listing "
                                         "records. Such a naming carries no information about "
                                         "whether anything DEPENDS on the file, which is what the "
                                         "check exists to establish.",
            "★_what_is_NOT_decided_here": "Whether an enumeration counts as a caller. Deciding it "
                                          "would mean either excluding named artifacts, which is "
                                          "an authored judgment about which records are exempt, or "
                                          "picking a threshold on how many files a caller may name "
                                          "— a hand-picked number over varying data, which is the "
                                          "shape this record has twice declined. NEITHER IS TAKEN. "
                                          "The question is stated and returned.",
            "what_is_published_instead": "`who_does_the_naming` below: per caller, how many of the "
                                         "flagged population it names and what share that is. The "
                                         "enumerating artifacts are visible there as data rather "
                                         "than removed by a rule nobody ruled, so a later dispatch "
                                         "can rule on the question with the measurement in front "
                                         "of it.",
            "what_this_means_for_archiving": "NOTHING may be archived on these verdicts as they "
                                             "stand — which is the same answer the standing "
                                             "warning already gives, reached now by measurement "
                                             "rather than by caution.",
        },
        "who_does_the_naming": who,
        "the_flagged_population_size": flagged_total,
        "candidacies": rows,
    }


def main(argv: list[str]) -> int:
    check = "--check" in argv
    commit = None
    if "--at" in argv:
        commit = argv[argv.index("--at") + 1]
        if not re.fullmatch(r"[0-9a-f]{7,40}", commit):
            raise Stop(f"--at takes an explicit commit hash, not {commit!r}")

    if check:
        if not OUT.exists():
            print("FAIL: the caller-check artifact is missing:", OUT)
            return 1
        have = json.loads(OUT.read_text(encoding="utf-8"))
        commit = commit or have["measured_at_commit"]

    if commit is None:
        raise Stop("--at <commit> is required when writing: the reading is a statement about one "
                   "tree and the commit is part of the finding")

    artifact = build(commit)
    text = json.dumps(artifact, indent=1, ensure_ascii=False) + "\n"

    if check:
        if OUT.read_text(encoding="utf-8") != text:
            print("FAIL: the caller-check does not re-derive:", OUT)
            return 1
        print("the retirement caller-check re-derives")
        return 0

    OUT.write_text(text, encoding="utf-8", newline="")
    print("wrote", OUT.relative_to(ROOT))
    print(f"  measured at {commit}")
    for row in artifact["candidacies"]:
        print(f"  [{row['verdict']}] {row['candidacy']} "
              f"({row['members_flagged']} flagged, "
              f"{len(row['members_held_by_callers'])} held by callers)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Stop as exc:
        print(f"STOP: {exc}")
        raise SystemExit(2)
