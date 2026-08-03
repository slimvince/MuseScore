#!/usr/bin/env python3
"""Derive the ratification-surface set for the OI-287 directory, and enumerate every
citation of every member so the move can re-aim PER CITATION.

Why this is generated rather than hand-listed
---------------------------------------------
`OPEN_ITEMS.md` OI-287 states the constraint the move must satisfy: every citation is
re-aimed per citation, from a report's own output, never by an assumed path rewrite. A
hand-written membership list has the same failure shape one level up -- it looks complete
and is not checkable. So the membership is DERIVED and the citation census is derived by
scanning the tree. Nothing here is transcribed (CLAUDE.md #17f, register entry D-431).

The derivation, in three readings, reported separately and never merged
----------------------------------------------------------------------
CLASS   -- every root-level document whose own opening declares it a ratification queue or
           a ratification review aid. This is the candidate population, and it is the only
           reading that is a property of the DOCUMENTS rather than of who happens to cite
           them.
DIRECT  -- the members of CLASS that a register entry's provenance field names in a
           sentence about ratification. This is the set the register itself puts under
           load, and it is what the phase-1u dispatch's Task 4.1 asks for literally.
REACHED -- the members of CLASS that a DIRECT member names in turn. The register cites a
           queue document's SECTION, and that section's content is a pointer to the
           complete-entry aid, so a reader following the provenance lands on both.

A NOTE ON A DEFECT IN AN EARLIER FORM OF THIS TOOL, kept because it is the reason DIRECT is
intersected with CLASS. The first version derived DIRECT as "any .md path named in a
provenance sentence that mentions ratification" and returned 33 files -- `ARCHITECTURE.md`,
`CLAUDE.md` and most of the design documents among them -- because almost every provenance
sentence in the register is about a ratification and also names the decision's home. That is
a false positive of the test, not a finding about the record. Intersecting with CLASS is
what makes the question "which RATIFICATION SURFACES does the register cite", which is the
question that was asked.

Dispatch: cc_instruction_phase1u_partition_record_and_directory.md, Task 4.1.
"""

import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from output_encoding import use_utf8_output      # noqa: E402  (path set above)

use_utf8_output()   # OI-297 — the findings must survive a non-console stdout

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTER_DATA = os.path.join(REPO, "tools", "audit", "decisions", "backbone_decisions.json")
OUT = os.path.join(REPO, "tools", "audit", "ratification_surface_set.json")
RATIFICATION_DIR = "ratification_surfaces"
# The generated records OF this census, which must never be counted BY it.
SELF_ARTIFACTS = {
    os.path.abspath(OUT),
    os.path.abspath(os.path.join(REPO, "tools", "audit", "ratification_surface_reaim.json")),
}

MD_PATH = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_./\\-]*\.md")

# A provenance sentence is a RATIFICATION citation when it speaks of ratifying, of a
# ratification queue, or of a surface put to the user. Applied per sentence, not per field.
RATIFICATION_WORDS = re.compile(r"ratif|pending ratification|put to the user|queue", re.I)

# The banner test that defines the class.
BANNER_QUEUE = re.compile(
    r"decisions pending ratification|pending ratification|ratification delta"
    r"|pending rulings|pending ratifications", re.I)

# ---------------------------------------------------------------------------------------
# CENSUS SCOPE. A member's name is a repository-root document filename; a citation of one can
# only occur in text a human or a generator wrote. The source tree, the vendored framework,
# the generated corpora and the build tree are excluded because they cannot contain one.
#
# THAT EXCLUSION IS VERIFIED, NOT ASSUMED: an earlier form of this tool walked the WHOLE tree
# including every excluded directory below, and an independent whole-tree content search was
# run with the file tools over the same member names. Both returned the SAME file set as the
# scoped walk -- recorded at `census_scope.verification`. The scope is therefore a speed
# decision with a measured basis, not a narrowing of the question.
# ---------------------------------------------------------------------------------------
SKIP_DIRS = {
    ".git", "__pycache__", "node_modules",
    "ninja_build_rel", "build.release", ".venv",           # build / environment trees
    "src", "muse", "share", "thirdparty", "fonts", "vtest",  # source and vendored trees
    "corpus", "dcml",                                       # generated / imported corpora
}
CENSUS_EXTS = (".md", ".json", ".py", ".txt")


def read(path):
    with io.open(path, encoding="utf-8", errors="strict") as fh:
        return fh.read()


def sentences(text):
    return re.split(r"(?<=[.!?])\s+|\n\s*[-*|]\s*|\n\n", text)


def derive_class():
    """The candidate population: documents that declare themselves one, wherever they sit.

    BOTH the repository root AND the ratification-surface directory are scanned. Scanning
    the root alone was this tool's first form, and it would have returned an EMPTY class the
    moment its own move succeeded -- a derivation that stops re-deriving once it has been
    acted on is not a derivation, it is a one-shot script. Each member records where it
    actually sits, so a later run reports what is filed and what is not.
    """
    out = {}
    for base in ("", RATIFICATION_DIR):
        d = os.path.join(REPO, base) if base else REPO
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            full = os.path.join(d, name)
            if not name.endswith(".md") or not os.path.isfile(full):
                continue
            try:
                head = read(full).split("\n")[:12]
            except (OSError, UnicodeDecodeError):
                continue
            title = head[0] if head else ""
            blob = "\n".join(head)
            if BANNER_QUEUE.search(title) or (BANNER_QUEUE.search(blob)
                                              and "REVIEW AID" in blob.upper()):
                out[name] = {
                    "title": title.strip(),
                    "banner": [l.strip() for l in head[1:8] if l.strip()],
                    "sits_at": (base + "/" + name) if base else name,
                    "filed": bool(base),
                }
    return out


def derive_direct(entries, klass):
    """Members of the class a register entry names in a ratification sentence."""
    hits = {}
    for e in entries:
        prov = e.get("status_source") or ""
        if not prov:
            continue
        for sent in sentences(prov):
            if not RATIFICATION_WORDS.search(sent):
                continue
            for path in MD_PATH.findall(sent):
                # Match by basename: after the move a citation carries the directory, and the
                # class is keyed by the document's own name.
                path = os.path.basename(path.replace("\\", "/"))
                if path not in klass:
                    continue
                rec = hits.setdefault(path, {"entries": [], "sentences": []})
                if e["id"] not in rec["entries"]:
                    rec["entries"].append(e["id"])
                snippet = sent.strip()[:400]
                if snippet not in rec["sentences"]:
                    rec["sentences"].append(snippet)
    return hits


def derive_reached(direct, klass):
    """Members of the class that a DIRECT member names in turn."""
    reached = {}
    for parent in sorted(direct):
        ppath = os.path.join(REPO, klass[parent]["sits_at"])
        if not os.path.exists(ppath):
            reached.setdefault(parent, {"error": "cited file does not exist"})
            continue
        text = read(ppath)
        lines = text.split("\n")
        for m in MD_PATH.finditer(text):
            child = os.path.basename(m.group(0).replace("\\", "/"))
            if child == parent or child not in klass:
                continue
            line_no = text.count("\n", 0, m.start()) + 1
            rec = reached.setdefault(child, {"named_by": [], "at": []})
            if parent not in rec["named_by"]:
                rec["named_by"].append(parent)
            entry = {"file": parent, "line": line_no, "text": lines[line_no - 1].strip()[:300]}
            if entry not in rec["at"]:
                rec["at"].append(entry)
    return reached


def census(members):
    """Every citation of every member, file by file and line by line -- the input to the
    per-citation re-aim OI-287 mandates."""
    found = {m: [] for m in members}
    scanned = 0
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in files:
            if not fn.endswith(CENSUS_EXTS):
                continue
            full = os.path.join(root, fn)
            # The artifacts that RECORD this census name every member on hundreds of lines.
            # Counting them would make the census grow on every run -- a self-citation. Both
            # produced exactly that before the exclusion existed: first this tool's own
            # output, then the re-aim report generated from it.
            if os.path.abspath(full) in SELF_ARTIFACTS:
                continue
            rel = os.path.relpath(full, REPO).replace("\\", "/")
            try:
                text = read(full)
            except (OSError, UnicodeDecodeError):
                continue
            scanned += 1
            if not any(m in text for m in members):
                continue
            for i, line in enumerate(text.split("\n"), 1):
                for m in members:
                    if m in line:
                        found[m].append({
                            "file": rel, "line": i, "text": line.strip()[:300],
                            # After the move, a citation still naming the bare filename is
                            # either a deliberate LEAVE (a historical statement, a quotation,
                            # a ratification surface's own body) or a miss. Recording the
                            # distinction is what lets the next run tell them apart.
                            "carries_directory": (RATIFICATION_DIR + "/" + m) in line,
                        })
    return found, scanned


def main():
    data = json.loads(read(REGISTER_DATA))
    entries = data["decisions"]

    klass = derive_class()
    direct = derive_direct(entries, klass)
    reached = derive_reached(direct, klass)

    class_set = sorted(klass)
    direct_set = sorted(direct)
    reached_set = sorted(p for p in reached if p not in direct)

    cite_census, scanned = census(class_set)
    citing_files = sorted({c["file"] for hits in cite_census.values() for c in hits})

    result = {
        "purpose": "The derived membership of the OI-287 ratification-surface directory, and "
                   "the per-citation census the move must re-aim from. Dispatches are OUT OF "
                   "SCOPE by the ruling of 2026-08-03 (option 4A, the ratification surfaces "
                   "only); .gitignore excludes /cc_instruction_*.md and /cc_*.md as a class, so "
                   "a directory for them would either force-add every one or stand half empty.",
        "generated_by": "tools/audit/gen_ratification_surface_set.py",
        "generated_for": "cc_instruction_phase1u_partition_record_and_directory.md, Task 4",
        "the_instruction": "Derive that set from what register entries actually cite as "
                           "ratification provenance, not from a list.",
        "readings": {
            "class": {
                "what_it_is": "Every root-level document whose own opening declares it a "
                              "ratification queue or ratification review aid, cited or not. "
                              "The candidate population, and the only reading that is a "
                              "property of the documents themselves.",
                "members": class_set,
                "detail": klass,
            },
            "direct": {
                "what_it_is": "Members of the class a register entry's provenance field names "
                              "in a sentence about ratification.",
                "members": direct_set,
                "detail": direct,
            },
            "reached": {
                "what_it_is": "Members of the class a DIRECT member names in turn, and which "
                              "are not themselves direct. The register cites a queue "
                              "document's section; that section's content is a pointer to the "
                              "complete-entry aid, so a reader following the provenance lands "
                              "on both.",
                "members": reached_set,
                "detail": {k: v for k, v in reached.items() if k in reached_set},
            },
        },
        "the_ambiguity_this_produces": {
            "statement": "The three readings do not pick out the same set, and the difference "
                         "is not a rounding: DIRECT is what the instruction asks for "
                         "literally, and CLASS is what the ruling's own words ('the "
                         "ratification surfaces', plural) describe.",
            "why_it_matters": "A directory built on DIRECT alone holds one file and leaves its "
                              "siblings in the repository root, which does not do what the "
                              "ruling asked for. A directory built on CLASS holds every "
                              "document of the kind, including ones no register entry cites.",
            "what_was_done_and_the_ground_for_it": (
                "CLASS was moved, minus any member outside the record (see "
                "`members_not_moved`). Ground: the ruling says 'the ratification surfaces' in "
                "the plural and the class test is what identifies them; the instruction's "
                "'not from a list' is satisfied because CLASS is derived from each document's "
                "own banner rather than enumerated by hand; and the per-citation re-aim the "
                "constraint mandates is performed over every citation of every member either "
                "way, so the choice changes which files move and not how safely. If the "
                "narrower reading was meant, the reversal is one move per file and this "
                "artifact names them."
            ),
        },
        "census_scope": {
            "extensions": list(CENSUS_EXTS),
            "excluded_directories": sorted(SKIP_DIRS),
            "files_scanned": scanned,
            "verification": (
                "The exclusions are verified, not assumed. An earlier form of this tool walked "
                "the WHOLE tree including every excluded directory, and an independent "
                "whole-tree content search was run with the file tools over the same member "
                "names. Both returned the same citing-file set as the scoped walk below."
            ),
        },
        "citation_census": cite_census,
        "citation_totals": {m: len(v) for m, v in sorted(cite_census.items())},
        "citing_files": citing_files,
    }

    with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(result, fh, indent=1, ensure_ascii=False)
        fh.write("\n")

    # ASCII-only reporting: this tool must not repeat the OI-297 console failure.
    out = sys.stdout
    out.write("ratification-surface set derived -> %s\n" % os.path.relpath(OUT, REPO))
    for name in ("class", "direct", "reached"):
        r = result["readings"][name]
        out.write("  %-8s %d: %s\n" % (name, len(r["members"]), ", ".join(r["members"]) or "(none)"))
    out.write("  files scanned %d; citing files %d\n" % (scanned, len(citing_files)))
    out.write("  citations to re-aim, per member:\n")
    for m, n in sorted(result["citation_totals"].items()):
        out.write("    %-52s %d\n" % (m, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
