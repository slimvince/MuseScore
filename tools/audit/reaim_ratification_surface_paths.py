#!/usr/bin/env python3
"""Re-aim every citation of a moved ratification surface, ONE CITATION AT A TIME.

Why this is not a path rewrite
------------------------------
`OPEN_ITEMS.md` OI-287 states the constraint: every citation is re-aimed PER CITATION from
a report's own output, never by an assumed path rewrite -- because a sweep "produces a tree
in which every reference resolves and some of them resolve to the wrong thing". The wrong
things here are real and were found by reading all of them:

  * a statement about where a file WAS at a named past commit (OI-285's table of state at
    `b6be14097e`) -- re-aiming it would make the record assert that a directory existed at a
    commit where it did not;
  * a QUOTATION of another surface's wording -- re-aiming it silently edits a quote;
  * the BODY of a ratification surface itself -- D-249 makes the surface part of the ruling,
    and OI-285's own resolution says a ratification surface that has been tidied is no longer
    the surface that was ratified;
  * a GENERATED file -- `decisions/group_*.md` is rendered from `backbone_decisions.json`,
    so editing it would be undone by the next regeneration and would mask the real citation.

So every citation carries an AUTHORED verdict with its reason. A citation with no verdict is
a STOP; a citation whose recorded line no longer contains the name is a STOP. Nothing is
inferred from a pattern.

Usage:
  python tools/audit/reaim_ratification_surface_paths.py            # apply, write the report
  python tools/audit/reaim_ratification_surface_paths.py --dry-run  # classify only
"""

import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CENSUS = os.path.join(REPO, "tools", "audit", "ratification_surface_set.json")
OUT = os.path.join(REPO, "tools", "audit", "ratification_surface_reaim.json")
NEW_DIR = "ratification_surfaces"

REAIM = "RE-AIM"
LEAVE = "LEAVE"
GENERATED = "LEAVE - GENERATED"

# ---------------------------------------------------------------------------------------
# THE AUTHORED VERDICTS. Keyed by the citing FILE; each entry gives the verdict for every
# citation in that file and the reason it holds for all of them. Where one file needs two
# verdicts, the line numbers are named explicitly.
# ---------------------------------------------------------------------------------------
BY_FILE = {
    "OPEN_ITEMS.md": {
        "default": REAIM,
        "reason": "Live pointers in open-item rows: a reader following one must be able to "
                  "open the file.",
        "by_line": {
            314: (LEAVE,
                  "The OI-285 row is a HISTORICAL FINDING about the state of these files at "
                  "commit b6be14097e ('absent from the commit', 'untracked') and about what "
                  "phase 1l then did ('committed IN PLACE, at their current paths'). Both "
                  "statements are true of the paths as they then were; re-aiming them would "
                  "make the record assert a directory that did not exist at that commit. The "
                  "new location is carried by the dated note added to open_items/OI-285.md."),
        },
    },
    "STATUS.md": {
        "default": REAIM,
        "reason": "Live pointers in session entries naming what to read.",
        "by_line": {},
    },
    "open_items/OI-208.md": {
        "default": REAIM,
        "reason": "A live pointer to where the complete entries are rendered.",
        "by_line": {},
    },
    "open_items/OI-279.md": {
        "default": REAIM,
        "reason": "A live pointer to the surface on which the two options were presented.",
        "by_line": {},
    },
    "open_items/OI-285.md": {
        "default": LEAVE,
        "reason": "This row IS the historical finding about these files' location and "
                  "committed state. Every citation in it is either a statement about the "
                  "state at commit b6be14097e, a quotation of the register's provenance "
                  "wording, or the narrative of what phase 1l did at the paths as they then "
                  "were. Re-aiming any of them rewrites history rather than a pointer. The "
                  "new location is carried by the dated note appended to this file.",
        "by_line": {},
    },
    "open_items/OI-287.md": {
        "default": LEAVE,
        "reason": "This row is the argument FOR the move, quoting the citation chain as it "
                  "stood before it. Its dated resolution note carries the new paths.",
        "by_line": {},
    },
    "cowork_handoff.md": {
        "default": REAIM,
        "reason": "Live pointers in the handoff's reading list.",
        "by_line": {},
    },
    "cowork_architecture_reassessment.md": {
        "default": REAIM,
        "reason": "A live pointer in the document's own status banner, naming where its "
                  "banner was ratified.",
        "by_line": {},
    },
    "docs/iteration_path1_summary.md": {
        "default": REAIM,
        "reason": "A live pointer in the document's own status banner.",
        "by_line": {},
    },
    "docs/redesign_plan.md": {
        "default": REAIM,
        "reason": "A live pointer in the document's own status banner.",
        "by_line": {},
    },
    "docs/scoring_model.md": {
        "default": REAIM,
        "reason": "A live pointer in the document's own status banner.",
        "by_line": {},
    },
    "tools/audit/decisions/backbone_decisions.json": {
        "default": REAIM,
        "reason": "The register's SOURCE OF RECORD. These provenance fields are the citations "
                  "OI-287 names as the reason the move is its own act; they are live pointers "
                  "and they are what the rendered group files are generated from, so this is "
                  "the ONE place they are corrected.",
        "by_line": {},
    },
}

# Files whose citations are left for a stated structural reason, with no per-line detail.
WHOLE_FILE_RULES = [
    (lambda f: f.startswith("decisions/group_"), GENERATED,
     "Rendered from tools/audit/decisions/backbone_decisions.json by "
     "gen_decisions_register.py. Editing it would be undone at the next regeneration and "
     "would hide the citation that actually needs correcting. Re-aimed at the source."),
    # Both the new path and the bare pre-move name: the census is taken BEFORE the move, so a
    # member citing a sibling is recorded under its old root-level name.
    (lambda f: f.startswith(NEW_DIR + "/") or f in _MEMBERS, LEAVE,
     "The BODY of a ratification surface. D-249 makes the surface part of the ruling, and "
     "OI-285's resolution states that a ratification surface which has been tidied is no "
     "longer the surface that was ratified. The citation also resolves unchanged, both "
     "files now sitting in the same directory."),
    (lambda f: f.startswith("cc_instruction_"), LEAVE,
     "A dispatch. .gitignore excludes /cc_instruction_*.md and /cc_*.md as a class, so these "
     "are not in the record; and they are another wave's working instruction, which this "
     "wave does not edit. Reported rather than changed."),
]


def read(path):
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


# The class members, read from the census so this tool holds no hand-written list either.
_MEMBERS = set(json.loads(read(CENSUS))["readings"]["class"]["members"])


def classify(citing_file, line_no):
    for pred, verdict, reason in WHOLE_FILE_RULES:
        if pred(citing_file):
            return verdict, reason
    rule = BY_FILE.get(citing_file)
    if rule is None:
        return None, None
    if line_no in rule["by_line"]:
        return rule["by_line"][line_no]
    return rule["default"], rule["reason"]


def main(argv):
    dry = "--dry-run" in argv
    census = json.loads(read(CENSUS))

    # (citing file) -> list of (line, member, verdict, reason)
    plan = {}
    unclassified = []
    for member, hits in census["citation_census"].items():
        for h in hits:
            verdict, reason = classify(h["file"], h["line"])
            if verdict is None:
                unclassified.append({"member": member, "file": h["file"], "line": h["line"],
                                     "text": h["text"]})
                continue
            plan.setdefault(h["file"], []).append(
                {"line": h["line"], "member": member, "verdict": verdict, "reason": reason,
                 "recorded_text": h["text"]})

    if unclassified:
        print("STOP: %d citation(s) carry no authored verdict:" % len(unclassified))
        for u in unclassified:
            print("   %s:%d  %s" % (u["file"], u["line"], u["member"]))
        return 1

    applied, skipped, stops = [], [], []
    for citing_file in sorted(plan):
        todo = [p for p in plan[citing_file] if p["verdict"] == REAIM]
        skipped.extend({"file": citing_file, **p} for p in plan[citing_file]
                       if p["verdict"] != REAIM)
        if not todo:
            continue
        full = os.path.join(REPO, citing_file)
        if not os.path.exists(full):
            stops.append({"file": citing_file, "why": "citing file does not exist"})
            continue
        lines = read(full).split("\n")
        for p in sorted(todo, key=lambda x: x["line"]):
            idx = p["line"] - 1
            if idx >= len(lines) or p["member"] not in lines[idx]:
                stops.append({"file": citing_file, "line": p["line"], "member": p["member"],
                              "why": "the recorded line no longer contains the name -- the "
                                     "census is stale and the re-aim must not guess"})
                continue
            before = lines[idx]
            # Replace the bare name, never one already carrying the directory.
            lines[idx] = before.replace(NEW_DIR + "/" + p["member"], "\x00").replace(
                p["member"], NEW_DIR + "/" + p["member"]).replace(
                "\x00", NEW_DIR + "/" + p["member"])
            applied.append({"file": citing_file, "line": p["line"], "member": p["member"],
                            "reason": p["reason"],
                            "before": before.strip()[:200], "after": lines[idx].strip()[:200]})
        if not dry and not stops:
            with io.open(full, "w", encoding="utf-8", newline="\n") as fh:
                fh.write("\n".join(lines))

    report = {
        "purpose": "The per-citation re-aim of every reference to a moved ratification "
                   "surface. OI-287's constraint: per citation, from the report's own "
                   "output, never by an assumed path rewrite.",
        "generated_by": "tools/audit/reaim_ratification_surface_paths.py",
        "new_directory": NEW_DIR,
        "dry_run": dry,
        "totals": {
            "citations": sum(len(v) for v in plan.values()),
            "re_aimed": len(applied),
            "left": len(skipped),
            "stops": len(stops),
        },
        "left_by_reason": sorted({s["reason"] for s in skipped}),
        "re_aimed": applied,
        "left": skipped,
        "stops": stops,
    }
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(report, fh, indent=1, ensure_ascii=False)
        fh.write("\n")

    out = sys.stdout   # ASCII-only: this tool must not repeat the OI-297 console failure.
    out.write("re-aim %s -> %s\n" % ("DRY RUN" if dry else "APPLIED", os.path.relpath(OUT, REPO)))
    t = report["totals"]
    out.write("  citations %d: re-aimed %d, left %d, stops %d\n"
              % (t["citations"], t["re_aimed"], t["left"], t["stops"]))
    for s in stops:
        out.write("  STOP %s\n" % json.dumps(s, ensure_ascii=True))
    return 1 if stops else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
